from __future__ import print_function
import ee
import numpy as np
import datetime as dt
import pandas as pd
import math
from pysmm.utils import gdrive
import time
import pickle
import os
import matplotlib.pyplot as plt
import pytesmo.time_series.anomaly as anomaly
from pytesmo.time_series.plotting import plot_clim_anom
from sklearn.linear_model import LinearRegression
from pytesmo.temporal_matching import df_match


class GEE_pt(object):
    """Class to create an interface with GEE for the extraction of parameter time series

        Attributes:
            lon: longitude in decimal degrees
            lat: latitude in decimal degrees
            workdir: path to a directory to save output e.g. time-series plots
            buffer: radius of the time-series footprint
        """

    def __init__(self, lon, lat, workdir, buffer=20):
        ee.Reset()
        ee.Initialize()
        self.lon = lon
        self.lat = lat
        self.buffer = buffer
        self.workdir = workdir

        # Placeholders
        self.S1TS = None
        self.ASPE = None
        self.SLOP = None
        self.ELEV = None
        self.LC = None

    def _multitemporalDespeckle(self, images, radius, units, opt_timeWindow=None):
        def mapMeanSpace(i):
            reducer = ee.Reducer.mean()
            kernel = ee.Kernel.square(radius, units)
            mean = i.reduceNeighborhood(reducer, kernel).rename(bandNamesMean)
            ratio = i.divide(mean).rename(bandNamesRatio)
            return (i.addBands(mean).addBands(ratio))

        if opt_timeWindow == None:
            timeWindow = dict(before=-3, after=3, units='month')
        else:
            timeWindow = opt_timeWindow

        bandNames = ee.Image(images.first()).bandNames()
        bandNamesMean = bandNames.map(lambda b: ee.String(b).cat('_mean'))
        bandNamesRatio = bandNames.map(lambda b: ee.String(b).cat('_ratio'))

        # compute spatial average for all images
        meanSpace = images.map(mapMeanSpace)

        # computes a multi-temporal despeckle function for a single image

        def multitemporalDespeckleSingle(image):
            t = image.date()
            fro = t.advance(ee.Number(timeWindow['before']), timeWindow['units'])
            to = t.advance(ee.Number(timeWindow['after']), timeWindow['units'])

            meanSpace2 = ee.ImageCollection(meanSpace).select(bandNamesRatio).filterDate(fro, to) \
                .filter(ee.Filter.eq('relativeOrbitNumber_start', image.get('relativeOrbitNumber_start')))

            b = image.select(bandNamesMean)

            return (b.multiply(meanSpace2.sum()).divide(meanSpace2.count()).rename(bandNames)).set('system:time_start',
                                                                                                   image.get(
                                                                                                       'system:time_start'))

        return meanSpace.map(multitemporalDespeckleSingle)

    def _s1_track_ts(self,
                     filtered_collection,
                     track_nr,
                     dual_pol,
                     varmask,
                     returnLIA,
                     masksnow,
                     tempfilter):

        def getAzimuth(f):
            coords = ee.Array(f.geometry().coordinates().get(0)).transpose()
            crdLons = ee.List(coords.toList().get(0))
            crdLats = ee.List(coords.toList().get(1))
            minLon = crdLons.sort().get(0)
            maxLon = crdLons.sort().get(-1)
            minLat = crdLats.sort().get(0)
            maxLat = crdLats.sort().get(-1)
            azimuth = ee.Number(crdLons.get(crdLats.indexOf(minLat))).subtract(minLon).atan2(ee.Number(crdLats
                .get(
                crdLons.indexOf(minLon))).subtract(minLat)).multiply(180.0 / math.pi).add(180.0)
            return ee.Feature(ee.Geometry.LineString([crdLons.get(crdLats.indexOf(maxLat)), maxLat,
                                                      minLon, crdLats.get(crdLons.indexOf(minLon))]),
                              {'azimuth': azimuth}).copyProperties(f)

        def getLIA(imCollection):
            # function to calculate the local incidence angle, based on azimuth angle and srtm
            srtm = ee.Image("USGS/SRTMGL1_003")
            srtm_slope = ee.Terrain.slope(srtm)
            srtm_aspect = ee.Terrain.aspect(srtm)

            tmpImg = imCollection

            inc = tmpImg.select('angle')
            azimuth = getAzimuth(tmpImg).get('azimuth')
            srtm_slope_proj = srtm_slope.multiply(
                ee.Image.constant(azimuth).subtract(9.0).subtract(srtm_aspect).multiply(math.pi / 180).cos())
            lia = inc.subtract(ee.Image.constant(90).subtract(ee.Image.constant(90).subtract(srtm_slope_proj))).abs()

            return tmpImg.addBands(ee.Image(lia.select(['angle'], ['lia'])))

        def miscMask(image):
            # masking of low and high db values as well as areas affected by geometry distortion
            tmp = ee.Image(image)

            # mask pixels
            vv = tmp.select('VV')
            if dual_pol == True:
                vh = tmp.select('VH')
                maskvh = vh.gte(-25).bitwiseAnd(vh.lt(0))  # was -25 and 0
            lia = tmp.select('lia')
            maskvv = vv.gte(-25).bitwiseAnd(vv.lt(0))
            masklia1 = lia.gt(20)  # angle 10
            masklia2 = lia.lt(45)  # angle 50
            masklia = masklia1.bitwiseAnd(masklia2)

            if dual_pol == True:
                mask = maskvv.bitwiseAnd(maskvh)
            else:
                mask = maskvv
            mask = mask.bitwiseAnd(masklia)
            # mask = mask.bitwiseAnd(maskslope)
            tmp = tmp.updateMask(mask)

            return (tmp)

        def toln(image):
            tmp = ee.Image(image)

            # Convert to linear
            vv = ee.Image(10).pow(tmp.select('VV').divide(10))
            if dual_pol == True:
                vh = ee.Image(10).pow(tmp.select('VH').divide(10))

            # Convert to ln
            out = vv.log()
            if dual_pol == True:
                out = out.addBands(vh.log())
                out = out.select(['constant', 'constant_1'], ['VV', 'VH'])
            else:
                out = out.select(['constant'], ['VV'])

            return out.set('system:time_start', tmp.get('system:time_start'))

        def applyvarmask(image):
            tmp = ee.Image(image)
            tmp = tmp.updateMask(varmask)

            return (tmp)

        def tolin(image):
            tmp = ee.Image(image)

            # Convert to linear
            vh = ee.Image(10).pow(tmp.select('VH').divide(10))

            # Output
            out = vh.select(['constant'], ['VH'])

            return out.set('system:time_start', tmp.get('system:time_start'))

        def tolin_dual(image):
            tmp = ee.Image(image)
            if dual_pol == True:
                lin = ee.Image(10).pow(tmp.divide(10))  # .select(['constant', 'constant_1'], ['VV', 'VH'])
            else:
                lin = ee.Image(10).pow(tmp.divide(10))  # .select(['constant'], ['VV'])

            return lin.set('system:time_start', tmp.get('system:time_start'))

        def todb(image):
            tmp = ee.Image(image)

            return ee.Image(10).multiply(tmp.log10()).set('system:time_start', tmp.get('system:time_start'))

        def applysnowmask(image):
            tmp = ee.Image(image)
            sdiff = tmp.select('VH').subtract(snowref)
            wetsnowmap = sdiff.lte(-2.6)  # .focal_mode(100, 'square', 'meters', 3)

            return (tmp.updateMask(wetsnowmap.eq(0)))

        def createAvg(image):
            # average pixels within the time-series foot print
            gee_roi = ee.Geometry.Point(self.lon, self.lat).buffer(self.buffer)
            # tmp = ee.Image(image).resample()
            tmp = ee.Image(image)

            # Conver to linear before averaging
            tmp = tmp.addBands(ee.Image(10).pow(tmp.select('VV').divide(10)))
            if dual_pol == True:
                tmp = tmp.addBands(ee.Image(10).pow(tmp.select('VH').divide(10)))
                tmp = tmp.select(['constant', 'constant_1', 'angle', 'lia'], ['VV', 'VH', 'angle', 'lia'])
            else:
                tmp = tmp.select(['constant', 'angle', 'lia'], ['VV', 'angle', 'lia'])

            reduced_img_data = tmp.reduceRegion(ee.Reducer.median(), gee_roi, 10)
            totcount = ee.Image(1).reduceRegion(ee.Reducer.count(), gee_roi, 10)
            pcount = tmp.reduceRegion(ee.Reducer.count(), gee_roi, 10)
            return ee.Feature(None, {'result': reduced_img_data, 'count': pcount, 'totcount': totcount})

        #  filter for track
        if dual_pol == True:
            gee_s1_track_fltd = filtered_collection.filterMetadata('relativeOrbitNumber_start', 'equals',
                                                                   track_nr).select(['VV', 'VH', 'angle'])
        else:
            gee_s1_track_fltd = filtered_collection.filterMetadata('relativeOrbitNumber_start', 'equals',
                                                                   track_nr).select(['VV', 'angle'])

        # compute lia
        lia_im = getLIA(gee_s1_track_fltd)
        # add as a band to all images
        gee_s1_track_fltd = gee_s1_track_fltd.map(lambda x: x.addBands(lia_im))
        # apply filters to collection
        gee_s1_track_fltd = gee_s1_track_fltd.map(miscMask)

        if varmask == True:
            # mask pixels with low temporal variability
            # compute temporal statistics
            gee_s1_ln = gee_s1_track_fltd.map(toln)
            k2vv = ee.Image(gee_s1_ln.select('VV').reduce(ee.Reducer.stdDev()))
            if dual_pol == True:
                k2vh = ee.Image(gee_s1_ln.select('VH').reduce(ee.Reducer.stdDev()))
                varmask = k2vv.gt(0.4).And(k2vh.gt(0.4))
            else:
                varmask = k2vv.gt(0.4)
            gee_s1_track_fltd = gee_s1_track_fltd.map(applyvarmask)

        if tempfilter == True:
            # apply a temporal speckle filter
            radius = 3
            units = 'pixels'
            gee_s1_linear = gee_s1_track_fltd.map(tolin_dual)
            gee_s1_dspckld_vv = self._multitemporalDespeckle(gee_s1_linear.select('VV'), radius, units,
                                                             {'before': -12, 'after': 12, 'units': 'month'})
            gee_s1_dspckld_vv = gee_s1_dspckld_vv.map(todb).select(['constant'], ['VV'])
            if dual_pol == True:
                gee_s1_dspckld_vh = self._multitemporalDespeckle(gee_s1_linear.select('VH'), radius, units,
                                                                 {'before': -12, 'after': 12, 'units': 'month'})
                gee_s1_dspckld_vh = gee_s1_dspckld_vh.map(todb).select(['constant'], ['VH'])
            if dual_pol == False:
                gee_s1_track_fltd = gee_s1_dspckld_vv.combine(gee_s1_track_fltd.select('angle')) \
                    .combine(gee_s1_track_fltd.select('lia'))
            else:
                gee_s1_track_fltd = gee_s1_dspckld_vv.combine(gee_s1_dspckld_vh) \
                    .combine(gee_s1_track_fltd.select('angle')) \
                    .combine(gee_s1_track_fltd.select('lia'))

        # if masksnow == True:
        #     # apply wet snow mask
        #     gee_s1_lin = gee_s1_track_fltd.select('VH').map(tolin)
        #     snowref = ee.Image(10).multiply(gee_s1_lin.reduce(ee.Reducer.intervalMean(5, 100)).log10())
        #     gee_s1_track_fltd = gee_s1_track_fltd.map(applysnowmask)

        # create average for buffer area - i.e. compute time-series
        gee_s1_mapped = gee_s1_track_fltd.map(createAvg)
        tmp = gee_s1_mapped.getInfo()
        # get vv
        vv_sig0 = 10 * np.log10(
            np.array([x['properties']['result']['VV'] for x in tmp['features']], dtype=np.float))

        ge_dates = np.array([dt.datetime.strptime(x['id'][17:32], '%Y%m%dT%H%M%S') for x in tmp['features']])

        if dual_pol == True:
            # get vh
            vh_sig0_lin = np.array([x['properties']['result']['VH'] for x in tmp['features']], dtype=np.float)
            vh_sig0 = 10 * np.log10(vh_sig0_lin)
            if masksnow == True:
                snowref = 10 * np.log10(np.mean(vh_sig0_lin[vh_sig0_lin > np.percentile(vh_sig0_lin, 5)]))
                snowmask = np.where(vh_sig0 - snowref > -2.6)
                vh_sig0 = vh_sig0[snowmask]
                vv_sig0 = vv_sig0[snowmask]
                ge_dates = ge_dates[snowmask]

        if returnLIA == True:
            # get lia
            lia = np.array([x['properties']['result']['lia'] for x in tmp['features']], dtype=np.float)
        else:
            # get angle
            lia = np.array([x['properties']['result']['angle'] for x in tmp['features']], dtype=np.float)

            # calculate gamma0
        vv_sig0lin = np.power(10, (vv_sig0 / 10))
        vv_gamma0 = 10 * np.log10(vv_sig0lin / np.cos(lia * (math.pi / 180)))
        if dual_pol == True:
            vh_sig0lin = np.power(10, (vh_sig0 / 10))
            vh_gamma0 = 10 * np.log10(vh_sig0lin / np.cos(lia * (math.pi / 180)))

        # get val_count - i.e. compute the fraction of valid pixels within the footprint
        val_count = np.array(
            [np.float(x['properties']['count']['VV']) / np.float(x['properties']['totcount']['constant']) for x in
             tmp['features']], dtype=np.float)

        if masksnow == True:
            val_count = val_count[snowmask]

        if self.buffer <= 100:
            valid = np.where(val_count > 0.01)
        else:
            valid = np.where(val_count > 0.1)
        vv_sig0 = vv_sig0[valid]
        vv_gamma0 = vv_gamma0[valid]
        if dual_pol == True:
            vh_sig0 = vh_sig0[valid]
            vh_gamma0 = vh_gamma0[valid]
        lia = lia[valid]
        ge_dates = ge_dates[valid]

        if dual_pol == True:
            return (
                pd.DataFrame({'sig0': vv_sig0, 'sig02': vh_sig0, 'lia': lia, 'gamma0': vv_gamma0, 'gamma02': vh_gamma0},
                             index=ge_dates))
        else:
            return (pd.DataFrame({'sig0': vv_sig0, 'lia': lia, 'gamma0': vv_gamma0}, index=ge_dates))

    def extr_LC(self, prod='Globcover'):
        # select prod='Globcover', 'Corine', 'USGS' (North America only for USGS)
        if prod == 'Globcover':
            lc_image = ee.Image("ESA/GLOBCOVER_L4_200901_200912_V2_3").select('landcover')
        elif prod == 'Corine':
            lc_image = ee.Image('users/felixgreifeneder/corine')
        elif prod == 'USGS':
            lc_image = ee.Image(ee.ImageCollection("USGS/NLCD").toList(100).get(-1))
        else:
            print('Unknown land-cover product')
            return

        roi = ee.Geometry.Point(self.lon, self.lat).buffer(self.buffer)
        lc = lc_image.reduceRegion(ee.Reducer.mode(), roi).getInfo()
        self.LC = lc['landcover']

    def extr_MODIS_MOD13Q1(self):
        # extract time-series of the MODIS product MOD13Q1

        def createAvg(image):
            gee_roi = ee.Geometry.Point(self.lon, self.lat).buffer(self.buffer)

            # mask image
            immask = image.select('SummaryQA').eq(ee.Image(0))
            image = image.updateMask(immask)

            reduced_img_data = image.reduceRegion(ee.Reducer.median(), gee_roi, 30)
            return ee.Feature(None, {'result': reduced_img_data})

        # load collection
        gee_l8_collection = ee.ImageCollection('MODIS/006/MOD13Q1')

        # filter collection
        gee_roi = ee.Geometry.Point(self.lon, self.lat).buffer(self.buffer)
        gee_l8_fltd = gee_l8_collection.filterBounds(gee_roi)

        # extract time series
        gee_l8_mpd = gee_l8_fltd.map(createAvg)
        tmp = gee_l8_mpd.getInfo()

        EVI = np.array([x['properties']['result']['EVI'] for x in tmp['features']], dtype=np.float)

        ge_dates = np.array([dt.datetime.strptime(x['id'], '%Y_%m_%d') for x in tmp['features']])

        valid = np.where(np.isfinite(EVI))

        # cut out invalid values
        EVI = EVI[valid]
        ge_dates = ge_dates[valid]

        return (pd.Series(EVI, index=ge_dates, name='EVI'))

    def extr_GLDAS_SM(self, yearlist=None):
        # get time series of GLDAS 0 to 10 cm soil moisture

        def createAvg(image):
            gee_roi = ee.Geometry.Point(self.lon, self.lat).buffer(self.buffer)

            reduced_img_data = image.reduceRegion(ee.Reducer.median(), gee_roi, 30, tileScale=4)
            return ee.Feature(None, {'result': reduced_img_data})

        if yearlist == None:
            # yearlist = range(1987,2018)
            yearlist = range(2011, 2018)

        SM_list = list()

        for iyear in yearlist:
            # ee.Reset()
            # ee.Initialize()
            print(iyear)
            # load collection
            if iyear < 2000:
                GLDAS_collection = ee.ImageCollection('NASA/GLDAS/V20/NOAH/G025/T3H').select('SoilMoi0_10cm_inst')
            else:
                GLDAS_collection = ee.ImageCollection('NASA/GLDAS/V021/NOAH/G025/T3H').select('SoilMoi0_10cm_inst')
            GLDAS_collection = GLDAS_collection.filterDate(str(iyear) + '-01-01', str(iyear) + '-12-31')
            GLDAS_collection = GLDAS_collection.filter(ee.Filter.calendarRange(16, 18, 'hour'))

            # clip
            roi = ee.Geometry.Point(self.lon, self.lat).buffer(self.buffer)
            GLDAS_collection = GLDAS_collection.map(lambda image: image.clip(roi))

            # extract time series
            time_series = GLDAS_collection.map(createAvg)
            tmp = time_series.getInfo()

            SM = np.array([x['properties']['result']['SoilMoi0_10cm_inst'] for x in tmp['features']], dtype=np.float)

            ge_dates = np.array([dt.datetime.strptime(x['id'], 'A%Y%m%d_%H%M') for x in tmp['features']])

            valid = np.where(np.isfinite(SM))

            # cut out invalid values
            SM = SM[valid]
            ge_dates = ge_dates[valid]

            SM_series = pd.Series(SM, index=ge_dates, copy=True, name='GLDAS')

            SM_list.append(SM_series)

        return (pd.concat(SM_list))

    def extr_GLDAS_date(self, date):
        doi = ee.Date(date)
        gldas = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G025/T3H") \
            .select(['SoilMoi0_10cm_inst', 'CanopInt_inst']) \
            .filterDate(doi, doi.advance(3, 'hour'))

        gldas_img = ee.Image(gldas.first())
        roi = ee.Geometry.Point(self.lon, self.lat).buffer(self.buffer)
        try:
            return (gldas_img.reduceRegion(ee.Reducer.median(), roi, 50).getInfo())
        except:
            return {'SoilMoi0_10cm_inst': np.nan, 'CanopInt_inst': np.nan}

    def extr_terrain(self):
        roi = ee.Geometry.Point(self.lon, self.lat).buffer(self.buffer)
        elev = ee.Image("CGIAR/SRTM90_V4").reduceRegion(ee.Reducer.median(), roi).getInfo()
        aspe = ee.Terrain.aspect(ee.Image("CGIAR/SRTM90_V4")).reduceRegion(ee.Reducer.median(), roi).getInfo()
        slop = ee.Terrain.slope(ee.Image("CGIAR/SRTM90_V4")).reduceRegion(ee.Reducer.median(), roi).getInfo()
        self.ELEV = elev['elevation']
        self.ASPE = aspe['aspect']
        self.SLOP = slop['slope']

    def extr_S1(self,
                maskwinter=False,
                lcmask=False,
                globcover_mask=True,
                trackflt=None,
                masksnow=True,
                varmask=False,
                ssmcor=None,
                dual_pol=True,
                desc=False,
                tempfilter=False,
                returnLIA=False):
        # extract filtered Sentinel-1 backscatter time-series
        def mask_lc(image):
            tmp = ee.Image(image)

            # load land cover info
            corine = ee.Image('users/felixgreifeneder/corine')

            # create lc mask
            valLClist = [10, 11, 12, 13, 18, 19, 20, 21, 26, 27, 28, 29]

            lcmask = corine.eq(valLClist[0]).bitwiseOr(corine.eq(valLClist[1])) \
                .bitwiseOr(corine.eq(valLClist[2])) \
                .bitwiseOr(corine.eq(valLClist[3])) \
                .bitwiseOr(corine.eq(valLClist[4])) \
                .bitwiseOr(corine.eq(valLClist[5])) \
                .bitwiseOr(corine.eq(valLClist[6])) \
                .bitwiseOr(corine.eq(valLClist[7])) \
                .bitwiseOr(corine.eq(valLClist[8])) \
                .bitwiseOr(corine.eq(valLClist[9])) \
                .bitwiseOr(corine.eq(valLClist[10])) \
                .bitwiseOr(corine.eq(valLClist[11]))

            tmp = tmp.updateMask(lcmask)

            return tmp

        def mask_lc_globcover(image):
            tmp = ee.Image(image)

            # load lc
            glbcvr = ee.Image("ESA/GLOBCOVER_L4_200901_200912_V2_3").select('landcover')

            valLClist = [11, 14, 20, 30, 120, 140, 150]

            lcmask = glbcvr.eq(valLClist[0]) \
                .bitwiseOr(glbcvr.eq(valLClist[1])) \
                .bitwiseOr(glbcvr.eq(valLClist[2])) \
                .bitwiseOr(glbcvr.eq(valLClist[3])) \
                .bitwiseOr(glbcvr.eq(valLClist[4])) \
                .bitwiseOr(glbcvr.eq(valLClist[5])) \
                .bitwiseOr(glbcvr.eq(valLClist[6]))

            tmp = tmp.updateMask(lcmask)

            return tmp

        def addRefSM(image):
            tmp = ee.Image(image)
            img_date = ee.Date(tmp.get('system:time_start'))
            RefSMtmp = RefSMcollection.filterDate(img_date.format('Y-M-d'))
            current_ssm = ee.ImageCollection(RefSMtmp).toList(10).get(0)

            out_image = tmp.addBands(ee.Image(current_ssm))

            return (out_image)

        def s1_simplyfy_date(image):
            return (image.set('system:time_start', ee.Date(ee.Date(image.get('system:time_start')).format('Y-M-d'))))

        def applyCorrelationMask(image):
            mask = ssm_vv_cor.select('correlation').gt(0.1)
            return (image.updateMask(mask))

        import timeit

        tic = timeit.default_timer()

        # load S1 data
        gee_s1_collection = ee.ImageCollection('COPERNICUS/S1_GRD')  # .map(setresample)

        # filter collection
        gee_roi = ee.Geometry.Point(self.lon, self.lat).buffer(self.buffer)

        gee_s1_filtered = gee_s1_collection.filter(ee.Filter.eq('instrumentMode', 'IW')) \
            .filterBounds(gee_roi) \
            .filter(ee.Filter.listContains('transmitterReceiverPolarisation',
                                           'VV'))
        # .filter(ee.Filter.eq('platform_number', 'A')) \

        if desc == False:
            # Select only acquisition from ascending tracks
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))

        if dual_pol == True:
            # select only acquisitions with VV AND VH
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))

        if maskwinter == True:
            # Mask winter based on the DOY
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.dayOfYear(121, 304))

        if trackflt is not None:
            # Select only data from a specific S1 track
            if isinstance(trackflt, list):
                gee_s1_filtered = gee_s1_filtered.filter(
                    ee.Filter.inList(ee.List(trackflt), 'relativeOrbitNumber_start'))
            else:
                gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.eq('relativeOrbitNumber_start', trackflt))

        if lcmask == True:
            # Mask pixels based on Corine land-cover
            gee_s1_filtered = gee_s1_filtered.map(mask_lc)
        if globcover_mask == True:
            # Mask pixels based on the Globcover land-cover classification
            gee_s1_filtered = gee_s1_filtered.map(mask_lc_globcover)

        if ssmcor is not None:
            # Mask pixels with a low correlation toe coarse resolution soil moisture
            # Mostly relevant if aggregating over a larger area
            RefSMlist = list()
            ssmcor = ssmcor.resample('D').mean().dropna()
            ssmcor = ssmcor.astype(np.float)
            for i in range(len(ssmcor)):
                ssm_img = ee.Image(ssmcor[i]).clip(gee_roi).float()
                ssm_img = ssm_img.set('system:time_start', ssmcor.index[i])
                RefSMlist.append(ssm_img)
            RefSMcollection = ee.ImageCollection(RefSMlist)

            # prepare the join
            s1_joined = gee_s1_filtered.map(s1_simplyfy_date)
            join_filter = ee.Filter.equals(leftField='system:time_start', rightField='system:time_start')
            simple_join = ee.Join.simple()
            s1_joined = simple_join.apply(s1_joined, RefSMcollection, join_filter)

            # create ssm reference SM, image collection
            s1_plus_RefSM = ee.ImageCollection(s1_joined.map(addRefSM, True))
            ssm_vv_cor = s1_plus_RefSM.select(['VV', 'constant']).reduce(ee.Reducer.pearsonsCorrelation())
            gee_s1_filtered = gee_s1_filtered.map(applyCorrelationMask)

        # get the track numbers
        tmp = gee_s1_filtered.getInfo()
        track_series = np.array([x['properties']['relativeOrbitNumber_start'] for x in tmp['features']])
        available_tracks = np.unique(track_series)

        print('Extracting data from ' + str(len(available_tracks)) + ' Sentinel-1 tracks...')
        print(available_tracks)

        out_dict = {}
        for track_nr in available_tracks:
            out_dict[str(int(track_nr))] = self._s1_track_ts(gee_s1_filtered,
                                                             track_nr,
                                                             dual_pol,
                                                             varmask,
                                                             returnLIA,
                                                             masksnow,
                                                             tempfilter)

        toc = timeit.default_timer()

        print('Time-series extraction finished in ' + "{:10.2f}".format(toc - tic) + 'seconds')

        self.S1TS = out_dict

    def extr_SM(self,
                tracknr=None,
                masksnow=False,
                tempfilter=True,
                calc_anomalies=False):

        if self.S1TS == None:
            # get S1 time-series
            self.extr_S1(maskwinter=False, lcmask=False, trackflt=tracknr,
                         masksnow=masksnow, tempfilter=tempfilter)

        s1_ts = self.S1TS

        # load SVR model
        modelpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SVRmodel.p')
        MLmodel = pickle.load(open(modelpath, 'rb'))

        # extract land cover
        self.extr_LC()
        # extract terrain information
        self.extr_terrain()

        # check if one of the found tracks contains valid data
        empty = 0
        for track_id in s1_ts.keys():
            if len(s1_ts[track_id]) == 0:
                empty = 1
        if empty == 1:
            print('No valid data was found')
            return None

        # create ts stack
        cntr = 0
        sm_estimated = list()
        anom_estimated = list()
        for track_id in s1_ts.keys():
            # extract model attributes
            reg_model1 = (MLmodel[0], MLmodel[1])
            reg_model2 = (MLmodel[2], MLmodel[3])

            # calculate k1,...,kN and sig0m
            s1_ts[track_id].dropna(axis=0, how='any')
            temp_ts1 = s1_ts[track_id]['sig0']
            temp_ts2 = s1_ts[track_id]['sig02']
            temp_tslia = s1_ts[track_id]['lia']

            ts_length = len(temp_ts1)

            if ts_length < 10:
                print('Estimation for track #' + str(track_id) + ' not possible - time-series too short')
                continue

            temp_ts1_lin = np.power(10, temp_ts1 / 10.)
            temp_ts2_lin = np.power(10, temp_ts2 / 10.)
            meanVV = np.mean(temp_ts1_lin)
            meanVH = np.mean(temp_ts2_lin)
            k1VV = np.mean(np.log(temp_ts1_lin))
            k1VH = np.mean(np.log(temp_ts2_lin))
            k2VV = np.std(np.log(temp_ts1_lin))
            k2VH = np.std(np.log(temp_ts1_lin))

            # get gldas
            gldas_series = pd.Series(index=s1_ts[track_id].index)
            for i in gldas_series.index:
                gldas_tmp = self.extr_GLDAS_date(i.strftime('%Y-%m-%d'))
                gldas_series[i] = gldas_tmp['SoilMoi0_10cm_inst']

            # check for nans in the gldas time-series
            valid2 = np.where(np.isfinite(gldas_series) & np.isfinite(gldas_series))

            fmat_tmp1 = np.array([k1VV, k1VH, k2VV, k2VH, self.LC, np.mean(temp_tslia), self.ASPE,
                                  gldas_series.median()])  # , aspe, slop, elev, gldas_series.mean()])

            fmat_tmp2 = np.hstack(((temp_ts1_lin - meanVV).values.reshape(ts_length, 1),
                                   (temp_ts2_lin - meanVH).values.reshape(ts_length, 1),
                                   (gldas_series - gldas_series.mean()).values.reshape(ts_length, 1)))

            # apply masks to dates and fmat
            fmat_tmp2 = fmat_tmp2[valid2, :]
            dates = s1_ts[track_id].index[valid2]
            # fmat_tmp2 = fmat_tmp2[0]

            nn_model1 = reg_model1[0]
            nn_scaler1 = reg_model1[1]
            nn_model2 = reg_model2[0]
            nn_scaler2 = reg_model2[1]
            fvect1 = nn_scaler1.transform(fmat_tmp1.reshape(1, -1))
            fvect2 = nn_scaler2.transform(fmat_tmp2.squeeze())

            avg_ssm_estimated_tmp = nn_model1.predict(fvect1)
            diff_ssm_estimated_tmp = nn_model2.predict(fvect2)
            ssm_estimated_tmp = pd.Series((diff_ssm_estimated_tmp + avg_ssm_estimated_tmp) * 100, index=dates,
                                          name='S1')
            ssm_estimated_tmp = ssm_estimated_tmp[~ssm_estimated_tmp.index.duplicated(keep='first')]

            sm_estimated.append(ssm_estimated_tmp.copy())

            if calc_anomalies == True:
                # get GLDAS timeseries
                gldas_ts = self.extr_GLDAS_SM()

                # correct GLDAS for local variations
                gldas_ts_matched = df_match(ssm_estimated_tmp, gldas_ts, window=0.5)
                gldas_s1 = pd.concat([ssm_estimated_tmp, gldas_ts_matched['GLDAS']], axis=1, join='inner').dropna()
                lin_fit = LinearRegression()
                lin_fit.fit(gldas_s1['GLDAS'].values.reshape(-1, 1), gldas_s1['S1'].values)
                # calibrate GLDAS
                gldas_tmp = lin_fit.predict(gldas_ts.values.reshape(-1, 1))
                gldas_ts = pd.Series(gldas_tmp, index=gldas_ts.index)

                # calculate climatology
                gldas_clim = anomaly.calc_climatology(gldas_ts, moving_avg_clim=30)
                gldas_clim = pd.DataFrame(pd.Series(gldas_clim, name='S1'))
                # calculate anomaly
                anom_estimated_tmp = pd.Series(
                    [ssm_estimated_tmp[dateI] - gldas_clim['S1'][dateI.dayofyear] for dateI in ssm_estimated_tmp.index],
                    index=ssm_estimated_tmp.index,
                    dtype=np.float64)
                anom_estimated.append(anom_estimated_tmp.copy())

        sm_estimated = pd.concat(sm_estimated)
        sm_estimated.sort_index(inplace=True)
        if calc_anomalies == True:
            anom_estimated = pd.concat(anom_estimated)
            anom_estimated.sort_index(inplace=True)

        if calc_anomalies == False:
            return sm_estimated
        else:
            return pd.DataFrame({'S1SM': sm_estimated, 'ANOM': anom_estimated}, index=sm_estimated.index)

    def get_s1_dates(self, tracknr=None, dualpol=True):
        # get the S1 acquisition dates
        # load S1 data
        gee_s1_collection = ee.ImageCollection('COPERNICUS/S1_GRD')

        # construct roi
        roi = ee.Geometry.Point(self.lon, self.lat).buffer(self.buffer)

        # ASCENDING acquisitions
        gee_s1_filtered = gee_s1_collection.filter(ee.Filter.eq('instrumentMode', 'IW')) \
            .filterBounds(roi) \
            .filter(ee.Filter.eq('platform_number', 'A')) \
            .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
            .filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))

        if dualpol == True:
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))

        if tracknr is not None:
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.eq('relativeOrbitNumber_start', tracknr))

        # create a list of availalbel dates
        tmp = gee_s1_filtered.getInfo()
        tmp_ids = [x['properties']['system:index'] for x in tmp['features']]
        dates = np.array([dt.date(year=int(x[17:21]), month=int(x[21:23]), day=int(x[23:25])) for x in tmp_ids])

        return (dates)


class GEE_extent(object):
    """Class to create an interface with GEE for the extraction of arrays

        Attributes:
            minlon: minimum longitude in decimal degrees
            minlat: minumum latitude in decimal degress
            maxlon: maximum longitude in decimal degrees
            maxlat: maximum latitude in decimal degrees
            workdir: path to directory for exported files
            sampling: sampling of exported grids
        """

    def __init__(self, minlon, minlat, maxlon, maxlat, workdir, sampling=20):
        """Return a new GEE extent object"""
        ee.Reset()
        ee.Initialize()

        # construct roi
        roi = ee.Geometry.Polygon([[minlon, minlat], [minlon, maxlat],
                                   [maxlon, maxlat], [maxlon, minlat],
                                   [minlon, minlat]])

        self.roi = roi
        self.MINLON = minlon
        self.MINLAT = minlat
        self.sampling = sampling
        self.workdir = workdir

        # Placeholders
        self.S1_SIG0_VV_db = None
        self.S1_SIG0_VH_db = None
        self.S1_ANGLE = None
        self.K1VV = None
        self.K1VH = None
        self.K2VV = None
        self.K2VH = None
        self.K3VV = None
        self.K3VH = None
        self.K4VV = None
        self.K4VH = None
        self.S1_DATE = None
        self.S1MEAN_VV = None
        self.S1MEAN_VH = None
        self.S1STD_VV = None
        self.S1STD_VH = None
        self.S1_LIA = None
        self.ESTIMATED_SM = None
        self.GLDAS_IMG = None
        self.GLDAS_MEAN = None
        self.LAND_COVER = None
        self.TERRAIN = None
        self.L8_IMG = None
        self.L8_MEAN = None
        self.TREE_COVER = None
        self.LAST_GLDAS = dt.date.today()  # temporary
        self.LC_ID = None
        self.FOREST_TYPE = None
        self.BARE_COVER = None
        self.CROPS_COVER = None
        self.GRASS_COVER = None
        self.MOSS_COVER = None
        self.SHRUB_COVER = None
        self.TREE_COVER = None
        self.URBAN_COVER = None
        self.WATERP_COVER = None
        self.WATERS_COVER = None
        self.SAND = None
        self.CLAY = None
        self.BULK = None
        self.EVI_IMG = None
        self.EVI_MEAN = None

    def _multitemporalDespeckle(self, images, radius, units, opt_timeWindow=None):
        """Function for multi-temporal despeckling"""

        def mapMeanSpace(i):
            reducer = ee.Reducer.mean()
            kernel = ee.Kernel.square(radius, units)
            mean = i.reduceNeighborhood(reducer, kernel).rename(bandNamesMean)
            ratio = i.divide(mean).rename(bandNamesRatio)
            return (i.addBands(mean).addBands(ratio))

        if opt_timeWindow == None:
            timeWindow = dict(before=-3, after=3, units='month')
        else:
            timeWindow = opt_timeWindow

        bandNames = ee.Image(images.first()).bandNames()
        bandNamesMean = bandNames.map(lambda b: ee.String(b).cat('_mean'))
        bandNamesRatio = bandNames.map(lambda b: ee.String(b).cat('_ratio'))

        # compute spatial average for all images
        meanSpace = images.map(mapMeanSpace)

        # computes a multi-temporal despeckle function for a single image

        def multitemporalDespeckleSingle(image):
            t = image.date()
            fro = t.advance(ee.Number(timeWindow['before']), timeWindow['units'])
            to = t.advance(ee.Number(timeWindow['after']), timeWindow['units'])

            meanSpace2 = ee.ImageCollection(meanSpace).select(bandNamesRatio).filterDate(fro, to) \
                .filter(ee.Filter.eq('relativeOrbitNumber_start', image.get('relativeOrbitNumber_start')))

            b = image.select(bandNamesMean)

            return (b.multiply(meanSpace2.sum()).divide(meanSpace2.count()).rename(bandNames)).set('system:time_start',
                                                                                                   image.get(
                                                                                                       'system:time_start'))

        return meanSpace.map(multitemporalDespeckleSingle)

    def init_SM_retrieval(self, year, month, day, hour=12, minute=0, model_version='GBRT_nogldas'):
        # initiate all datasets for the retrieval of soil moisture
        self.get_copernicus_lc()
        self.get_S1(year,
                    month,
                    day,
                    hour,
                    minute,
                    tempfilter=False,
                    mask_copernicuslc=True,
                    ascending=False)
        self.get_l8()
        self.get_sand_content()
        self.get_clay_content()
        self.get_bulk_density()
        self.get_modis_evi()

    def get_S1(self, year, month, day, hour, minute,
               tempfilter=True,
               tempfilter_radius=7,
               applylcmask=False,
               mask_globcover=False,
               mask_copernicuslc=False,
               dualpol=True,
               trackflt=None,
               maskwinter=False,
               masksnow=False,
               mask_snow_frozen_GLDAS=False,
               explicit_t_mask=None,
               ascending=True,
               maskLIA=True):
        """Retrieve the S1 image for a given day from GEE and apply specific filters.
           Assigns outputs to respective instance attributes

        """

        def getAzimuth(f):
            coords = ee.Array(f.geometry().coordinates().get(0)).transpose()
            crdLons = ee.List(coords.toList().get(0))
            crdLats = ee.List(coords.toList().get(1))
            minLon = crdLons.sort().get(0)
            maxLon = crdLons.sort().get(-1)
            minLat = crdLats.sort().get(0)
            maxLat = crdLats.sort().get(-1)
            azimuth = ee.Number(crdLons.get(crdLats.indexOf(minLat))).subtract(minLon).atan2(ee.Number(crdLats
                                                                                                       .get(
                crdLons.indexOf(minLon))).subtract(minLat)).multiply(180.0 / math.pi).add(180.0)
            return ee.Feature(ee.Geometry.LineString([crdLons.get(crdLats.indexOf(maxLat)), maxLat,
                                                      minLon, crdLats.get(crdLons.indexOf(minLon))]),
                              {'azimuth': azimuth}).copyProperties(f)

        def getLIA(imCollection):
            # function to calculate the local incidence angle, based on azimuth angle and srtm
            srtm = ee.Image("USGS/SRTMGL1_003").resample()
            srtm_slope = ee.Terrain.slope(srtm)
            srtm_aspect = ee.Terrain.aspect(srtm)

            # tmpImg = ee.Image(imCollection.first())
            tmpImg = ee.Image(imCollection)

            inc = tmpImg.select('angle').resample()
            azimuth = getAzimuth(tmpImg).get('azimuth')
            srtm_slope_proj = srtm_slope.multiply(
                ee.Image.constant(azimuth).subtract(9.0).subtract(srtm_aspect).multiply(math.pi / 180.0).cos())
            lia = inc.subtract(ee.Image.constant(90.0).subtract(ee.Image.constant(90.0).subtract(srtm_slope_proj))).abs()

            return tmpImg.addBands(ee.Image(lia.select(['angle'], ['lia'])))

        def maskterrain(image):
            # mask for terrain, local incidence angle and high and low backscatter
            tmp = ee.Image(image)
            # srtm dem
            if maskLIA == False:
                gee_srtm = ee.Image("USGS/SRTMGL1_003")
                gee_srtm_slope = ee.Terrain.slope(gee_srtm)
                mask = gee_srtm_slope.lt(20)
            else:
                lia = tmp.select('lia')
                mask = lia.gt(20).bitwiseAnd(lia.lt(50))  # modified!! should be 45
            #mask2 = tmp.lt(0).bitwiseAnd(tmp.gt(-25))
            #mask = mask.bitwiseAnd(mask2)
            tmp = tmp.updateMask(mask)

            return tmp

        def masklc(image):
            # load land cover info
            corine = ee.Image('users/felixgreifeneder/corine')

            # create lc mask
            valLClist = [10, 11, 12, 13, 18, 19, 20, 21, 26, 27, 28, 29]

            lcmask = corine.eq(valLClist[0]).bitwiseOr(corine.eq(valLClist[1])) \
                .bitwiseOr(corine.eq(valLClist[2])) \
                .bitwiseOr(corine.eq(valLClist[3])) \
                .bitwiseOr(corine.eq(valLClist[4])) \
                .bitwiseOr(corine.eq(valLClist[5])) \
                .bitwiseOr(corine.eq(valLClist[6])) \
                .bitwiseOr(corine.eq(valLClist[7])) \
                .bitwiseOr(corine.eq(valLClist[8])) \
                .bitwiseOr(corine.eq(valLClist[9])) \
                .bitwiseOr(corine.eq(valLClist[10])) \
                .bitwiseOr(corine.eq(valLClist[11])) \
                .reduceResolution(ee.Reducer.mode()).reproject(crs=image.select(0).projection()).clip(self.roi)

            tmp = ee.Image(image)

            tmp = tmp.updateMask(lcmask)
            return (tmp)

        def mask_lc_globcover(image):

            tmp = ee.Image(image)

            # load lc
            glbcvr = ee.Image("ESA/GLOBCOVER_L4_200901_200912_V2_3").select('landcover')

            # valLClist = [11, 14, 20, 30, 120, 140, 150]
            invalLC = [190, 210, 220]

            lcmask = glbcvr.neq(invalLC[0]) \
                .bitwiseOr(glbcvr.neq(invalLC[1])) \
                .bitwiseOr(glbcvr.neq(invalLC[2]))

            tmp = tmp.updateMask(lcmask)

            return tmp

        def mask_lc_copernicus(image):
            copernicus_collection = ee.ImageCollection('COPERNICUS/Landcover/100m/Proba-V/Global')
            copernicus_image = ee.Image(copernicus_collection.toList(1000).get(0)).select('discrete_classification')

            valLClist = [30, 40, 60, 90]

            lcmask = copernicus_image.eq(valLClist[0]).bitwiseOr(copernicus_image.eq(valLClist[1])) \
                .bitwiseOr(copernicus_image.eq(valLClist[2])) \
                .bitwiseOr(copernicus_image.eq(valLClist[3]))

            tmp = ee.Image(image)
            tmp = tmp.updateMask(lcmask)

            return tmp

        def setresample(image):
            image = image.select(['VV', 'VH']).resample()
            return image

        def toln(image):

            tmp = ee.Image(image)

            # Convert to linear
            vv = ee.Image(10).pow(tmp.select('VV').divide(10))
            if dualpol == True:
                vh = ee.Image(10).pow(tmp.select('VH').divide(10))

            # Convert to ln
            out = vv.log()
            if dualpol == True:
                out = out.addBands(vh.log())
                out = out.select(['constant', 'constant_1'], ['VV', 'VH'])
            else:
                out = out.select(['constant'], ['VV'])

            return out.set('system:time_start', tmp.get('system:time_start'))

        def tolin(image):

            tmp = ee.Image(image)

            # Covert to linear
            vv = ee.Image(10).pow(tmp.select('VV').divide(10))
            if dualpol == True:
                vh = ee.Image(10).pow(tmp.select('VH').divide(10))

            # Convert to
            if dualpol == True:
                out = vv.addBands(vh)
                out = out.select(['constant', 'constant_1'], ['VV', 'VH'])
            else:
                out = vv.select(['constant'], ['VV'])

            return out.set('system:time_start', tmp.get('system:time_start'))

        def todb(image):

            tmp = ee.Image(image)

            return ee.Image(10).multiply(tmp.log10()).set('system:time_start', tmp.get('system:time_start'))

        def applysnowmask(image):

            tmp = ee.Image(image)
            sdiff = tmp.select('VH').subtract(snowref)
            wetsnowmap = sdiff.lte(-2.6).focal_mode(100, 'square', 'meters', 3)

            return (tmp.updateMask(wetsnowmap.eq(0)))

        def projectlia(image):
            tmp = ee.Image(image)
            trgtprj = tmp.select('VV').projection()
            tmp = tmp.addBands(tmp.select('lia').reproject(trgtprj), ['lia'], True)
            return (tmp)

        def apply_explicit_t_mask(image):

            t_mask = ee.Image('users/felixgreifeneder/' + explicit_t_mask)
            mask = t_mask.eq(0)
            return (image.updateMask(mask))

        def mask_gldas_snow_frozen(image):
            # frozen soil / snow
            doi = ee.Date(image.get('system:time_start'))
            snow = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G025/T3H") \
                .select('SWE_inst') \
                .filterDate(doi, doi.advance(3, 'hour'))

            snow_img = ee.Image(snow.first()).resample().clip(self.roi)

            snow_mask = snow_img.expression('(b(0) < 3) ? 1 : 0')

            fs = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G025/T3H") \
                .select('SoilTMP0_10cm_inst') \
                .filterDate(doi, doi.advance(3, 'hour'))

            fs_img = ee.Image(fs.first()).resample().clip(self.roi)

            fs_mask = fs_img.expression('(b(0) > 275) ? 1 : 0')

            return image.updateMask(ee.Image(snow_mask.And(fs_mask)))

        def mask_trees(image):
            # load lc
            # glbcvr = ee.Image("ESA/GLOBCOVER_L4_200901_200912_V2_3").select('landcover')
            # mask water
            # watermask = glbcvr.neq(210)
            return image.updateMask(treemask)

        def calc_g0(image):
            # Calculate gamma0

            tmp = ee.Image(image)
            # vv
            vv_lin = ee.Image(10).pow(tmp.select('VV').divide(10))
            vv_g0_lin = vv_lin.divide(tmp.select('lia').multiply(ee.Image(math.pi).divide(180.0)).cos())
            vv_g0 = ee.Image(10).multiply(vv_g0_lin.log10())
            if dualpol:
                vh_lin = ee.Image(10).pow(tmp.select('VH').divide(10))
                vh_g0_lin = vh_lin.divide(tmp.select('lia').multiply(ee.Image(math.pi).divide(180.0)).cos())
                vh_g0 = ee.Image(10).multiply(vh_g0_lin.log10())

            # Convert to
            if dualpol:
                out = vv_g0.addBands(vh_g0).addBands(vv_g0_lin).addBands(vh_g0_lin)
                out = out.select(['constant', 'constant_1', 'constant_2', 'constant_3'], ['VV', 'VH', 'VVlin', 'VHlin'])
            else:
                out = vv_g0.addBands(vv_g0_lin)
                out = out.select(['constant', 'constant_1'], ['VV', 'VVlin'])

            return out.set('system:time_start', tmp.get('system:time_start'))

        # ee.Reset()
        # ee.Initialize()

        # load S1 data
        gee_s1_collection = ee.ImageCollection('COPERNICUS/S1_GRD')

        # Filter the image collection
        gee_s1_filtered = gee_s1_collection.filter(ee.Filter.eq('instrumentMode', 'IW')) \
            .filterBounds(self.roi) \
            .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
            .filterDate('2014-01-01', self.LAST_GLDAS.strftime('%Y-%m-%d'))  # UPDATE: Using S1A and S1B
        # .filter(ee.Filter.eq('platform_number', 'A')) \

        if ascending == True:
            # Consider only image from ascending orbits
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))

        if dualpol == True:
            # Consider only dual-pol scenes
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))

        if trackflt is not None:
            # Specify track
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.eq('relativeOrbitNumber_start', trackflt))

        if maskwinter == True:
            # Mask winter based on DOY
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.dayOfYear(121, 304))

        if mask_snow_frozen_GLDAS == True:
            # Mask snow and frozen soil based on GLDAS data
            gee_s1_filtered = gee_s1_filtered.map(mask_gldas_snow_frozen)

        # add LIA
        if maskLIA == True:
            # compute the local incidence angle if it shall be used for masking
            gee_s1_filtered = gee_s1_filtered.map(getLIA)
            s1_lia = gee_s1_filtered.select('lia')
        else:
            s1_lia = None

        s1_angle = gee_s1_filtered.select('angle')

        if applylcmask == True:
            # apply land-cover mask based on Corine
            gee_s1_filtered = gee_s1_filtered.map(masklc)
        if mask_globcover == True:
            # apply land-cover mask based on globcover
            gee_s1_filtered = gee_s1_filtered.map(mask_lc_globcover)
        if mask_copernicuslc:
            gee_s1_filtered = gee_s1_filtered.map(mask_lc_copernicus)
        # if (applylcmask == False) and (mask_globcover == False):
        # apply mask based on tree cover threshold
        treemask = self.TREE_COVER.lte(20)
        gee_s1_filtered = gee_s1_filtered.map(mask_trees)

        # Enable bilinear resampling (instead of NN)
        # gee_s1_filtered = gee_s1_filtered.map(setresample)
        # if maskLIA:
        #     gee_s1_filtered = gee_s1_filtered.combine(s1_lia, overwrite=True)
        # else:
        #     gee_s1_filtered = gee_s1_filtered.combine(s1_angle, overwrite=True)

        if explicit_t_mask == None:
            # apply masking based on the terraing (LIA)
            gee_s1_filtered = gee_s1_filtered.map(maskterrain)
        else:
            # apply specific terrain mask
            gee_s1_filtered = gee_s1_filtered.map(apply_explicit_t_mask)

        if masksnow == True:
            # automatic wet snow masking
            gee_s1_linear_vh = gee_s1_filtered.map(tolin).select('VH')
            snowref = ee.Image(10).multiply(gee_s1_linear_vh.reduce(ee.Reducer.intervalMean(5, 100)).log10())
            gee_s1_filtered = gee_s1_filtered.map(applysnowmask)

        # create a list of availalbel dates
        tmp = gee_s1_filtered.getInfo()
        #tmp_ids = [x['properties']['system:index'] for x in tmp['features']]
        #dates = np.array([dt.datetime(int(x[17:21]), int(x[21:23]), int(x[23:25]), hour=int(x[26:28]),
        #                              minute=int(x[28:30]), second=int(x[30:32])) for x in tmp_ids])
        tmp_ids = [x['properties']['system:time_start'] for x in tmp['features']]
        dates = np.array([dt.datetime.fromtimestamp(int(int(x / 1000))) for x in tmp_ids])

        # find the closest acquisitions
        doi = dt.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
        doi_index = np.argmin(np.abs(dates - doi))
        date_selected = dates[doi_index]

        # filter imagecollection for respective date
        gee_s1_drange = gee_s1_filtered.filterDate(date_selected.strftime('%Y-%m-%dT%H:%M'),
                                                   (date_selected + dt.timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M'))
        s1_angle_drange = s1_angle.filterDate(date_selected.strftime('%Y-%m-%dT%H:%M'),
                                              (date_selected + dt.timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M'))
        if maskLIA == True:
            s1_lia_drange = s1_lia.filterDate(date_selected.strftime('%Y-%m-%dT%H:%M'),
                                              (date_selected + dt.timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M'))
        if gee_s1_drange.size().getInfo() > 1:
            if maskLIA == True:
                s1_lia = s1_lia_drange.mosaic()
                s1_lia = ee.Image(s1_lia.copyProperties(s1_lia_drange.first()))
            s1_angle = s1_angle_drange.mosaic()
            s1_sig0 = gee_s1_drange.mosaic()
            s1_sig0 = ee.Image(s1_sig0.copyProperties(gee_s1_drange.first()))
        else:
            s1_sig0 = ee.Image(gee_s1_drange.first())
            s1_angle = ee.Image(s1_angle_drange.first())
            if maskLIA == True:
                s1_lia = ee.Image(s1_lia_drange.first())

        # fetch image from image collection
        # get the track number
        s1_sig0_info = s1_sig0.getInfo()
        track_nr = s1_sig0_info['properties']['relativeOrbitNumber_start']
        self.TRACK_NR = track_nr
        self.ORBIT = s1_sig0_info['properties']['orbitProperties_pass']

        # only uses images of the same track
        gee_s1_filtered = gee_s1_filtered.filterMetadata('relativeOrbitNumber_start', 'equals', track_nr)
        # calculate g0
        gee_s1g0_filtered = gee_s1_filtered.map(calc_g0)
        # filter g0 collection to date of interest
        gee_s1g0_drange = gee_s1g0_filtered.filterDate(date_selected.strftime('%Y-%m-%dT%H:%M'),
                                                       (date_selected + dt.timedelta(hours=1)).strftime(
                                                           '%Y-%m-%dT%H:%M'))
        if gee_s1g0_drange.size().getInfo() > 1:
            s1_g0 = gee_s1g0_drange.mosaic()
            s1_g0 = ee.Image(s1_g0.copyProperties(gee_s1g0_drange.first()))
        else:
            s1_g0 = ee.Image(gee_s1g0_drange.first())

        if tempfilter == True:
            # despeckle
            radius = tempfilter_radius
            units = 'pixels'
            gee_s1_linear = gee_s1_filtered.map(tolin)
            gee_s1_dspckld_vv = self._multitemporalDespeckle(gee_s1_linear.select('VV'), radius, units,
                                                             {'before': -12, 'after': 12, 'units': 'month'})
            gee_s1_dspckld_vv = gee_s1_dspckld_vv.map(todb)
            gee_s1_fltrd_vv = gee_s1_dspckld_vv.filterDate(date_selected.strftime('%Y-%m-%d'),
                                                           (date_selected + dt.timedelta(days=1)).strftime('%Y-%m-%d'))
            s1_sig0_vv = gee_s1_fltrd_vv.mosaic()

            if dualpol == True:
                gee_s1_dspckld_vh = self._multitemporalDespeckle(gee_s1_linear.select('VH'), radius, units,
                                                                 {'before': -12, 'after': 12, 'units': 'month'})
                gee_s1_dspckld_vh = gee_s1_dspckld_vh.map(todb)
                gee_s1_fltrd_vh = gee_s1_dspckld_vh.filterDate(date_selected.strftime('%Y-%m-%d'),
                                                               (date_selected + dt.timedelta(days=1)).strftime(
                                                                   '%Y-%m-%d'))
                s1_sig0_vh = gee_s1_fltrd_vh.mosaic()

            if dualpol == True:
                s1_sig0 = s1_sig0_vv.addBands(s1_sig0_vh).select(['constant', 'constant_1'], ['VV', 'VH'])
            else:
                s1_sig0 = s1_sig0_vv.select(['constant'], ['VV'])

        # extract information
        s1_sig0_vv = s1_sig0.select('VV')
        s1_sig0_vv = s1_sig0_vv.clip(self.roi)
        s1_g0_vv = s1_g0.select('VV').clip(self.roi)
        if dualpol == True:
            s1_sig0_vh = s1_sig0.select('VH')
            s1_sig0_vh = s1_sig0_vh.clip(self.roi)
            s1_g0_vh = s1_g0.select('VH').clip(self.roi)

        # calculate statistical moments
        gee_s1_ln = gee_s1_filtered.map(toln)
        gee_s1_lin = gee_s1_filtered.map(tolin)
        k1vv = ee.Image(gee_s1_ln.select('VV').mean()).clip(self.roi)
        k2vv = ee.Image(gee_s1_ln.select('VV').reduce(ee.Reducer.stdDev())).clip(self.roi)
        k3vv = ee.Image(gee_s1_ln.select('VV').reduce(ee.Reducer.skew())).clip(self.roi)
        k4vv = ee.Image(gee_s1_ln.select('VV').reduce(ee.Reducer.kurtosis())).clip(self.roi)
        mean_vv = ee.Image(gee_s1_lin.select('VV').mean()).clip(self.roi)
        std_vv = ee.Image(gee_s1_lin.select('VV').reduce(ee.Reducer.stdDev())).clip(self.roi)
        # g0
        gee_s1g0_ln = gee_s1g0_filtered.map(toln)
        k1gvv = ee.Image(gee_s1g0_ln.select('VV').mean()).clip(self.roi)
        k2gvv = ee.Image(gee_s1g0_ln.select('VV').reduce(ee.Reducer.stdDev())).clip(self.roi)
        k3gvv = ee.Image(gee_s1g0_ln.select('VV').reduce(ee.Reducer.skew())).clip(self.roi)
        k4gvv = ee.Image(gee_s1g0_ln.select('VV').reduce(ee.Reducer.kurtosis())).clip(self.roi)
        mean_gvv = ee.Image(gee_s1g0_filtered.select('VVlin').mean()).clip(self.roi)
        std_gvv = ee.Image(gee_s1g0_filtered.select('VVlin').reduce(ee.Reducer.stdDev())).clip(self.roi)

        if dualpol == True:
            k1vh = ee.Image(gee_s1_ln.select('VH').mean()).clip(self.roi)
            k2vh = ee.Image(gee_s1_ln.select('VH').reduce(ee.Reducer.stdDev())).clip(self.roi)
            k3vh = ee.Image(gee_s1_ln.select('VH').reduce(ee.Reducer.skew())).clip(self.roi)
            k4vh = ee.Image(gee_s1_ln.select('VH').reduce(ee.Reducer.kurtosis())).clip(self.roi)
            mean_vh = ee.Image(gee_s1_lin.select('VH').mean()).clip(self.roi)
            std_vh = ee.Image(gee_s1_lin.select('VH').reduce(ee.Reducer.stdDev())).clip(self.roi)
            # g0
            k1gvh = ee.Image(gee_s1g0_ln.select('VH').mean()).clip(self.roi)
            k2gvh = ee.Image(gee_s1g0_ln.select('VH').reduce(ee.Reducer.stdDev())).clip(self.roi)
            k3gvh = ee.Image(gee_s1g0_ln.select('VH').reduce(ee.Reducer.skew())).clip(self.roi)
            k4gvh = ee.Image(gee_s1g0_ln.select('VH').reduce(ee.Reducer.kurtosis())).clip(self.roi)
            mean_gvh = ee.Image(gee_s1g0_filtered.select('VHlin').mean()).clip(self.roi)
            std_gvh = ee.Image(gee_s1g0_filtered.select('VHlin').reduce(ee.Reducer.stdDev())).clip(self.roi)

        # export
        if dualpol == False:
            self.S1_SIG0_VV_db = s1_sig0_vv
            self.S1_G0_VV_db = s1_g0_vv
            self.S1_ANGLE = s1_angle
            self.K1VV = k1vv
            self.K2VV = k2vv
            self.K3VV = k3vv
            self.K4VV = k4vv
            self.K1g0VV = k1gvv
            self.K2g0VV = k2gvv
            self.K3g0VV = k3gvv
            self.K4g0VV = k4gvv
            self.S1_DATE = date_selected
        else:
            self.S1_SIG0_VV_db = s1_sig0_vv
            self.S1_SIG0_VH_db = s1_sig0_vh
            self.S1_G0_VV_db = s1_g0_vv
            self.S1_G0_VH_db = s1_g0_vh
            self.S1_ANGLE = s1_angle
            self.K1VV = k1vv
            self.K1VH = k1vh
            self.K2VV = k2vv
            self.K2VH = k2vh
            self.K3VV = k3vv
            self.K3VH = k3vh
            self.K4VV = k4vv
            self.K4VH = k4vh
            self.K1g0VV = k1gvv
            self.K2g0VV = k2gvv
            self.K3g0VV = k3gvv
            self.K4g0VV = k4gvv
            self.K1g0VH = k1gvh
            self.K2g0VH = k2gvh
            self.K3g0VH = k3gvh
            self.K4g0VH = k4gvh
            self.S1_DATE = date_selected
            self.S1MEAN_VV = ee.Image(10).multiply(mean_vv.log10()).copyProperties(mean_vv)
            self.S1MEAN_VH = ee.Image(10).multiply(mean_vh.log10()).copyProperties(mean_vh)
            self.S1STD_VV = ee.Image(10).multiply(std_vv.log10()).copyProperties(std_vv)
            self.S1STD_VH = ee.Image(10).multiply(std_vh.log10()).copyProperties(std_vh)
            self.S1g0MEAN_VV = ee.Image(10).multiply(mean_gvv.log10()).copyProperties(mean_gvv)
            self.S1g0MEAN_VH = ee.Image(10).multiply(mean_gvh.log10()).copyProperties(mean_gvh)
            self.S1g0STD_VV = ee.Image(10).multiply(std_gvv.log10()).copyProperties(std_gvv)
            self.S1g0STD_VH = ee.Image(10).multiply(std_gvh.log10()).copyProperties(std_gvh)

        if maskLIA == True:
            self.S1_LIA = s1_lia

    def estimate_SM(self):
        # load SVR model
        modelpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SVRmodel.p')
        MLmodel_tuple = pickle.load(open(modelpath, 'rb'))
        MLmodel1 = {'SVRmodel': MLmodel_tuple[0], 'scaler': MLmodel_tuple[1]}
        MLmodel2 = {'SVRmodel': MLmodel_tuple[2], 'scaler': MLmodel_tuple[3]}

        # create parameter images
        alpha1 = [ee.Image(MLmodel1['SVRmodel'].best_estimator_.dual_coef_[0][i]) for i in
                  range(len(MLmodel1['SVRmodel'].best_estimator_.dual_coef_[0]))]
        gamma1 = ee.Image(-MLmodel1['SVRmodel'].best_estimator_.gamma)
        intercept1 = ee.Image(MLmodel1['SVRmodel'].best_estimator_.intercept_[0])

        # support vectors stack
        sup_vectors1 = MLmodel1['SVRmodel'].best_estimator_.support_vectors_
        n_vectors1 = sup_vectors1.shape[0]
        n_features1 = 8

        tmp_list = [ee.Image(sup_vectors1[0, i]) for i in range(n_features1)]

        sup_image1 = ee.Image.cat(tmp_list).select(['constant', 'constant_1', 'constant_2',
                                                    'constant_3', 'constant_4', 'constant_5',
                                                    'constant_6', 'constant_7'],
                                                   ['VVk1', 'VHk1', 'VVk2', 'VHk2',
                                                    'lc', 'lia', 'aspect', 'gldas_mean'])
        sup_list1 = [sup_image1]

        for i in range(1, n_vectors1):
            tmp_list = [ee.Image(sup_vectors1[i, j]) for j in range(n_features1)]

            sup_image1 = ee.Image.cat(tmp_list).select(['constant', 'constant_1', 'constant_2',
                                                        'constant_3', 'constant_4', 'constant_5',
                                                        'constant_6', 'constant_7'],
                                                       ['VVk1', 'VHk1', 'VVk2', 'VHk2',
                                                        'lc', 'lia', 'aspect', 'gldas_mean'])
            sup_list1.append(sup_image1)

        # create estimation stack
        vv = self.S1_SIG0_VV_db
        k1_vv = self.K1VV
        k1_vh = self.K1VH
        k2_vv = self.K2VV
        k2_vh = self.K2VH
        lia = self.S1_ANGLE.rename(['lia'])
        aspect = self.TERRAIN[2].rename(['aspect'])
        slope = self.TERRAIN[1].rename(['slope'])
        height = self.TERRAIN[0].rename(['height'])
        gldas_img = self.GLDAS_IMG
        gldas_mean = self.GLDAS_MEAN
        lc = self.LAND_COVER

        input_image1 = ee.Image([k1_vv.toFloat(),
                                 k1_vh.toFloat(),
                                 k2_vv.toFloat(),
                                 k2_vh.toFloat(),
                                 lc.toFloat(),
                                 lia.toFloat(),
                                 aspect.toFloat(),
                                 gldas_mean.toFloat()])
        ipt_img_mask1 = input_image1.mask().reduce(ee.Reducer.allNonZero())
        S1mask = vv.mask()
        zeromask = input_image1.neq(ee.Image(0)).reduce(ee.Reducer.allNonZero())
        combined_mask = S1mask.And(zeromask).And(ipt_img_mask1)

        input_image1 = input_image1.updateMask(ee.Image(combined_mask))

        # scale the estimation image
        scaling_std_img1 = ee.Image(
            [ee.Image(MLmodel1['scaler'].scale_[i].astype(np.float)) for i in range(n_features1)])

        scaling_std_img1 = scaling_std_img1.select(['constant', 'constant_1', 'constant_2',
                                                    'constant_3', 'constant_4', 'constant_5',
                                                    'constant_6', 'constant_7'],
                                                   ['VVk1', 'VHk1', 'VVk2', 'VHk2',
                                                    'lc', 'lia', 'aspect', 'gldas_mean'])

        scaling_mean_img1 = ee.Image(
            [ee.Image(MLmodel1['scaler'].center_[i].astype(np.float)) for i in range(n_features1)])

        scaling_mean_img1 = scaling_mean_img1.select(['constant', 'constant_1', 'constant_2',
                                                      'constant_3', 'constant_4', 'constant_5',
                                                      'constant_6', 'constant_7'],
                                                     ['VVk1', 'VHk1', 'VVk2', 'VHk2',
                                                      'lc', 'lia', 'aspect', 'gldas_mean'])

        input_image_scaled1 = input_image1.subtract(scaling_mean_img1).divide(scaling_std_img1)

        k_x1x2_1 = [sup_list1[i].subtract(input_image_scaled1) \
                        .pow(ee.Image(2)) \
                        .reduce(ee.Reducer.sum()) \
                        .sqrt() \
                        .pow(ee.Image(2)) \
                        .multiply(ee.Image(gamma1)) \
                        .exp() for i in range(n_vectors1)]

        alpha_times_k1 = [ee.Image(alpha1[i].multiply(k_x1x2_1[i])) for i in range(n_vectors1)]

        print(n_vectors1)

        alpha_times_k_sum_1 = ee.ImageCollection(alpha_times_k1).reduce(ee.Reducer.sum())
        # alpha_times_k_sum = alpha_times_k.reduce(ee.Reducer.sum())

        # print(alpha_times_k_sum.getInfo())

        estimated_smc_average = alpha_times_k_sum_1.add(intercept1)

        # estimate relative smc

        # create parameter images
        alpha2 = [ee.Image(MLmodel2['SVRmodel'].best_estimator_.dual_coef_[0][i]) for i in
                  range(len(MLmodel2['SVRmodel'].best_estimator_.dual_coef_[0]))]
        gamma2 = ee.Image(-MLmodel2['SVRmodel'].best_estimator_.gamma)
        intercept2 = ee.Image(MLmodel2['SVRmodel'].best_estimator_.intercept_[0])

        # support vectors stack
        sup_vectors2 = MLmodel2['SVRmodel'].best_estimator_.support_vectors_
        n_vectors2 = sup_vectors2.shape[0]
        n_features2 = 3

        tmp_list = [ee.Image(sup_vectors2[0, i]) for i in range(n_features2)]

        sup_image2 = ee.Image.cat(tmp_list).select(['constant', 'constant_1', 'constant_2'],
                                                   ['relVV', 'relVH', 'gldas'])
        sup_list2 = [sup_image2]

        for i in range(1, n_vectors2):
            tmp_list = [ee.Image(sup_vectors2[i, j]) for j in range(n_features2)]

            sup_image2 = ee.Image.cat(tmp_list).select(['constant', 'constant_1', 'constant_2'],
                                                       ['relVV', 'relVH', 'gldas'])
            sup_list2.append(sup_image2)

        # create estimation stack
        vv = self.S1_SIG0_VV_db
        vh = self.S1_SIG0_VH_db
        vv_mean = self.S1MEAN_VV
        vh_mean = self.S1MEAN_VH
        vv_std = self.S1STD_VV
        vh_std = self.S1STD_VH

        vv_lin = ee.Image(10).pow(vv.divide(10)).rename(['relVV'])
        vh_lin = ee.Image(10).pow(vh.divide(10)).rename(['relVH'])

        input_image2 = ee.Image([vv_lin.subtract(vv_mean).toFloat(),
                                 vh_lin.subtract(vh_mean).toFloat(),
                                 gldas_img.subtract(gldas_mean).rename(['gldas']).toFloat()])
        ipt_img_mask2 = input_image2.mask().reduce(ee.Reducer.allNonZero())
        S1mask = vv.mask()
        zeromask = input_image2.neq(ee.Image(0)).reduce(ee.Reducer.allNonZero())
        combined_mask = S1mask.And(zeromask).And(ipt_img_mask2)

        input_image2 = input_image2.updateMask(ee.Image(combined_mask))

        # scale the estimation image
        scaling_std_img2 = ee.Image(
            [ee.Image(MLmodel2['scaler'].scale_[i].astype(np.float)) for i in range(n_features2)])

        scaling_std_img2 = scaling_std_img2.select(['constant', 'constant_1', 'constant_2'],
                                                   ['relVV', 'relVH', 'gldas'])

        scaling_mean_img2 = ee.Image(
            [ee.Image(MLmodel2['scaler'].center_[i].astype(np.float)) for i in range(n_features2)])

        scaling_mean_img2 = scaling_mean_img2.select(['constant', 'constant_1', 'constant_2'],
                                                     ['relVV', 'relVH', 'gldas'])

        input_image_scaled2 = input_image2.subtract(scaling_mean_img2).divide(scaling_std_img2)

        k_x1x2_2 = [sup_list2[i].subtract(input_image_scaled2) \
                        .pow(ee.Image(2)) \
                        .reduce(ee.Reducer.sum()) \
                        .sqrt() \
                        .pow(ee.Image(2)) \
                        .multiply(ee.Image(gamma2)) \
                        .exp() for i in range(n_vectors2)]

        alpha_times_k2 = [ee.Image(alpha2[i].multiply(k_x1x2_2[i])) for i in range(n_vectors2)]

        print(n_vectors2)

        alpha_times_k_sum_2 = ee.ImageCollection(alpha_times_k2).reduce(ee.Reducer.sum())

        estimated_smc_relative = alpha_times_k_sum_2.add(intercept2)

        estimated_smc = estimated_smc_average.add(estimated_smc_relative).multiply(100).round().int8()

        # mask negative values
        estimated_smc = estimated_smc.updateMask(estimated_smc.gt(0))
        self.ESTIMATED_SM = estimated_smc

    def estimate_SM_GBR(self):
        # load GBR models
        from pysmm.no_GLDAS_ascending_decisiontree_GEE_step1 import tree as GBR_tree_step1_A
        from pysmm.no_GLDAS_ascending_decisiontree_GEE_step2 import tree as GBR_tree_step2_A
        from pysmm.no_GLDAS_descending_decisiontree_GEE_step1 import tree as GBR_tree_step1_D
        from pysmm.no_GLDAS_descending_decisiontree_GEE_step2 import tree as GBR_tree_step2_D
        import sys

        svv = self.S1_SIG0_VV_db
        svh = self.S1_SIG0_VH_db
        gvv = self.S1_G0_VV_db
        gvh = self.S1_G0_VH_db
        dsvv = svv.subtract(self.S1MEAN_VV)
        dsvh = svh.subtract(self.S1MEAN_VH)
        dgvv = gvv.subtract(self.S1g0MEAN_VV)
        dgvh = gvh.subtract(self.S1g0MEAN_VH)
        vv_mean = self.S1MEAN_VV
        vh_mean = self.S1MEAN_VH
        gvv_mean = ee.Image(self.S1g0MEAN_VV)
        gvh_mean = ee.Image(self.S1g0MEAN_VH)
        k1_vv = self.K1VV
        k1_vh = self.K1VH
        k2_vv = self.K2VV
        k2_vh = self.K2VH
        k3_vv = self.K3VV
        k3_vh = self.K3VH
        k4_vv = self.K4VV
        k4_vh = self.K4VH
        k1_gvv = self.K1g0VV
        k1_gvh = self.K1g0VH
        k2_gvv = self.K2g0VV
        k2_gvh = self.K2g0VH
        k3_gvv = self.K3g0VV
        k3_gvh = self.K3g0VH
        k4_gvv = self.K4g0VV
        k4_gvh = self.K4g0VH
        lia = self.S1_LIA
        l8_b1 = self.L8_IMG.select('B1')
        l8_b2 = self.L8_IMG.select('B2')
        l8_b3 = self.L8_IMG.select('B3')
        l8_b4 = self.L8_IMG.select('B4')
        l8_b5 = self.L8_IMG.select('B5')
        l8_b6 = self.L8_IMG.select('B6')
        l8_b7 = self.L8_IMG.select('B7')
        l8_b10 = self.L8_IMG.select('B10')
        l8_b11 = self.L8_IMG.select('B11')
        l8_b1_mean = self.L8_MEAN.select('B1_median')
        l8_b2_mean = self.L8_MEAN.select('B2_median')
        l8_b3_mean = self.L8_MEAN.select('B3_median')
        l8_b4_mean = self.L8_MEAN.select('B4_median')
        l8_b5_mean = self.L8_MEAN.select('B5_median')
        l8_b6_mean = self.L8_MEAN.select('B6_median')
        l8_b7_mean = self.L8_MEAN.select('B7_median')
        l8_b10_mean = self.L8_MEAN.select('B10_median')
        l8_b11_mean = self.L8_MEAN.select('B11_median')
        l8dt = self.L8_DDATE
        trees = self.TREE_COVER
        ndvi = self.EVI_IMG
        ndvi_mean = self.EVI_MEAN
        bulk = self.BULK
        clay = self.CLAY
        sand = self.SAND
        crop = self.CROPS_COVER
        moss = self.MOSS_COVER
        grass = self.GRASS_COVER
        bare = self.BARE_COVER
        # create lon lat rasters
        coords_tmp = self.S1_SIG0_VV_db.pixelLonLat()
        lon = coords_tmp.select('longitude')
        lat = coords_tmp.select('latitude')

        # # Average SMC asset name
        avg_asset_name = 'users/felixgreifeneder/AVG_SM/AVG_SM_' + str(math.trunc(self.MINLON * 100)) + '_' + \
                         str(math.trunc(self.MINLAT * 100)) + '_' + \
                         str(math.trunc((self.MINLON) + 1) * 100) + '_' + \
                         str(math.trunc((self.MINLAT) + 1) * 100) + '_' + \
                         str(math.trunc(self.TRACK_NR)) + '_' + \
                         str(self.sampling) + 'm'

        # try:
        #     estimated_smc_avg = ee.Image(avg_asset_name)
        #     estimated_smc_avg = estimated_smc_avg.clip(self.roi)
        #     testit = estimated_smc_avg.getInfo()
        #
        # except:
        # create estimation stack for step-1 (average soil moisture prediction)
        if self.ORBIT == 'ASCENDING':
            input_image1 = ee.Image([k3_vv.toFloat(),
                                     k2_gvv.toFloat(),
                                     trees.toFloat(),
                                     l8_b1_mean.toFloat(),
                                     l8_b2_mean.toFloat(),
                                     l8_b3_mean.toFloat(),
                                     l8_b6_mean.toFloat(),
                                     l8_b7_mean.toFloat(),
                                     ndvi_mean.toFloat(),
                                     bulk.toFloat(),
                                     clay.toFloat(),
                                     sand.toFloat(),
                                     lon.toFloat(),
                                     lat.toFloat()])
            # self.input_image1 = input_image1
            # self.GEE_2_disk(outdir='C:/Users/FGreifeneder/Documents/Temp_Documents/', raster='input_image1', name='ip1')
            input_image1 = input_image1.rename(['svvk3', 'gvvk2', 'trees', 'L8b1med', 'L8b2med', 'L8b3med', 'L8b6med',
                                                'L8b7med', 'ndvi_med', 'bulk', 'clay', 'sand', 'lon', 'lat'])
        elif self.ORBIT == 'DESCENDING':
            input_image1 = ee.Image([k2_gvh.toFloat(),
                                     k3_gvh.toFloat(),
                                     gvv_mean.toFloat(),
                                     gvh_mean.toFloat(),
                                     bare.toFloat(),
                                     crop.toFloat(),
                                     grass.toFloat(),
                                     l8_b3_mean.toFloat(),
                                     l8_b5_mean.toFloat(),
                                     l8_b6_mean.toFloat(),
                                     l8_b10_mean.toFloat(),
                                     ndvi_mean.toFloat(),
                                     bulk.toFloat(),
                                     sand.toFloat(),
                                     lon.toFloat(),
                                     lat.toFloat()])
            input_image1 = input_image1.rename(['gvhk2', 'gvhk3', 'gvvmean', 'gvhmean', 'bare', 'crops',
                                                'grass', 'L8b3med', 'L8b5med', 'L8b6med', 'L8b10med', 'ndvi_med',
                                                'bulk', 'sand', 'lon', 'lat'])

        ipt_img_mask1 = input_image1.mask().reduce(ee.Reducer.allNonZero())
        # S1mask = vv.mask()
        # zeromask = input_image1.neq(ee.Image(0)).reduce(ee.Reducer.allNonZero())
        # combined_mask = zeromask.And(ipt_img_mask1)
        combined_mask = ipt_img_mask1

        input_image1 = input_image1.updateMask(ee.Image(combined_mask))

        sys.setrecursionlimit(5000)
        if self.ORBIT == 'ASCENDING':
            estimated_smc_avg = GBR_tree_step1_A(input_image1)
        else:
            estimated_smc_avg = GBR_tree_step1_D(input_image1)
        estimated_smc_avg = estimated_smc_avg.updateMask(combined_mask)

        # # export as asset
        # # TODO automatically get user path
        # avg_asset_name = 'users/felixgreifeneder/AVG_SM/AVG_SM_' + str(math.trunc(self.MINLON * 100)) + '_' + \
        #                  str(math.trunc(self.MINLAT * 100)) + '_' + \
        #                  str(math.trunc((self.MINLON) + 1) * 100) + '_' + \
        #                  str(math.trunc((self.MINLAT) + 1) * 100) + '_' + \
        #                  str(math.trunc(self.TRACK_NR)) + '_' + \
        #                  str(self.sampling) + 'm'
        #
        # file_exp = ee.batch.Export.image.toAsset(estimated_smc_avg,
        #                                          description='AvgSM2Asset',
        #                                          assetId=avg_asset_name,
        #                                          region=self.roi.getInfo()['coordinates'],
        #                                          scale=self.sampling)
        #
        # file_exp.start()
        #
        # start = time.time()
        #
        # while (file_exp.active() == True):
        #     time.sleep(2)
        # else:
        #     print('Export of ' + avg_asset_name + ' average soil moisture completed')
        #
        # estimated_smc_avg = ee.Image(avg_asset_name)

        # create estimation stack for relative soil moisture

        if self.ORBIT == 'ASCENDING':
            input_image2 = ee.Image([dsvv.toFloat(),
                                     dgvv.toFloat(),
                                     crop.toFloat(),
                                     l8_b2.toFloat(),
                                     l8_b2_mean.toFloat(),
                                     l8_b3.toFloat(),
                                     l8_b4.toFloat(),
                                     l8_b5.toFloat(),
                                     l8_b5_mean.toFloat(),
                                     l8_b6.toFloat(),
                                     l8_b6_mean.toFloat(),
                                     l8_b7_mean.toFloat(),
                                     l8_b11.toFloat(),
                                     l8dt.toFloat(),
                                     ndvi.toFloat(),
                                     ndvi_mean.toFloat(),
                                     lon.toFloat(),
                                     lat.toFloat(),
                                     sand.toFloat()])

            input_image2 = input_image2.rename(['dsvv', 'dgvv', 'crops', 'L8b2', 'L8b2med', 'L8b3', 'L8b4', 'L8b5',
                                                'L8b5med', 'L8b6', 'L8b6med', 'L8b7med', 'L8b11', 'L8dt', 'ndvi',
                                                'ndvi_med', 'lon', 'lat', 'sand'])
        elif self.ORBIT == 'DESCENDING':
            input_image2 = ee.Image([dsvv.toFloat(),
                                     dsvh.toFloat(),
                                     gvv.toFloat(),
                                     dgvv.toFloat(),
                                     dgvh.toFloat(),
                                     crop.toFloat(),
                                     moss.toFloat(),
                                     l8_b1.toFloat(),
                                     l8_b2.toFloat(),
                                     l8_b3.toFloat(),
                                     l8_b3_mean.toFloat(),
                                     l8_b4.toFloat(),
                                     l8_b4_mean.toFloat(),
                                     l8_b5.toFloat(),
                                     l8_b6.toFloat(),
                                     l8_b6_mean.toFloat(),
                                     l8_b7.toFloat(),
                                     l8_b11_mean.toFloat(),
                                     l8dt.toFloat(),
                                     ndvi.toFloat(),
                                     ndvi_mean.toFloat(),
                                     lon.toFloat(),
                                     lat.toFloat(),
                                     bulk.toFloat(),
                                     clay.toFloat(),
                                     sand.toFloat()])
            input_image2 = input_image2.rename(['dsvv', 'dsvh', 'gvv', 'dgvv', 'dgvh', 'crop',
                                                'moss', 'L8b1', 'L8b2', 'L8b3', 'L8b3med',
                                                'L8b4', 'L8b4med', 'L8b5', 'L8b6', 'L8b6med',
                                                'L8b7', 'L8b11', 'L8dt', 'ndvi', 'ndvi_med', 'lon', 'lat',
                                                'bulk', 'clay', 'sand'])

        ipt_img_mask2 = input_image2.mask().reduce(ee.Reducer.allNonZero())
        # S1mask = vv.mask()
        # zeromask = input_image2.neq(ee.Image(0)).reduce(ee.Reducer.allNonZero())
        # combined_mask = S1mask.And(zeromask).And(ipt_img_mask2)
        combined_mask = ipt_img_mask2

        input_image2 = input_image2.updateMask(ee.Image(combined_mask))

        sys.setrecursionlimit(5000)
        if self.ORBIT == 'ASCENDING':
            estimated_smc_rel = GBR_tree_step2_A(input_image2)
        else:
            estimated_smc_rel = GBR_tree_step2_D(input_image2)
        estimated_smc_rel = estimated_smc_rel.updateMask(combined_mask)

        estimated_smc = estimated_smc_avg.add(estimated_smc_rel).multiply(100).round().int8()

        # mask negative values
        estimated_smc = estimated_smc.updateMask(estimated_smc.gt(0))
        self.ESTIMATED_SM = estimated_smc
        self.ESTIMATED_MEAN_SM = estimated_smc_avg.multiply(100).round().int8()

    def estimate_SM_GBR_1step(self):
        # load GBR models
        from pysmm.no_GLDAS_ascending_decisiontree_GEE_1step import tree as GBR_tree_A
        from pysmm.no_GLDAS_descending_decisiontree_GEE_1step import tree as GBR_tree_D
        import sys

        svv = self.S1_SIG0_VV_db
        svh = self.S1_SIG0_VH_db
        gvv = self.S1_G0_VV_db
        gvh = self.S1_G0_VH_db
        dsvv = svv.subtract(self.S1MEAN_VV)
        dsvh = svh.subtract(self.S1MEAN_VH)
        dgvv = gvv.subtract(self.S1g0MEAN_VV)
        dgvh = gvh.subtract(self.S1g0MEAN_VH)
        vv_mean = self.S1MEAN_VV
        vh_mean = self.S1MEAN_VH
        gvv_mean = ee.Image(self.S1g0MEAN_VV)
        gvh_mean = ee.Image(self.S1g0MEAN_VH)
        k1_vv = self.K1VV
        k1_vh = self.K1VH
        k2_vv = self.K2VV
        k2_vh = self.K2VH
        k3_vv = self.K3VV
        k3_vh = self.K3VH
        k4_vv = self.K4VV
        k4_vh = self.K4VH
        k1_gvv = self.K1g0VV
        k1_gvh = self.K1g0VH
        k2_gvv = self.K2g0VV
        k2_gvh = self.K2g0VH
        k3_gvv = self.K3g0VV
        k3_gvh = self.K3g0VH
        k4_gvv = self.K4g0VV
        k4_gvh = self.K4g0VH
        lia = self.S1_LIA
        l8_b1 = self.L8_IMG.select('B1')
        l8_b2 = self.L8_IMG.select('B2')
        l8_b3 = self.L8_IMG.select('B3')
        l8_b4 = self.L8_IMG.select('B4')
        l8_b5 = self.L8_IMG.select('B5')
        l8_b6 = self.L8_IMG.select('B6')
        l8_b7 = self.L8_IMG.select('B7')
        l8_b10 = self.L8_IMG.select('B10')
        l8_b11 = self.L8_IMG.select('B11')
        l8_b1_mean = self.L8_MEAN.select('B1_median')
        l8_b2_mean = self.L8_MEAN.select('B2_median')
        l8_b3_mean = self.L8_MEAN.select('B3_median')
        l8_b4_mean = self.L8_MEAN.select('B4_median')
        l8_b5_mean = self.L8_MEAN.select('B5_median')
        l8_b6_mean = self.L8_MEAN.select('B6_median')
        l8_b7_mean = self.L8_MEAN.select('B7_median')
        l8_b10_mean = self.L8_MEAN.select('B10_median')
        l8_b11_mean = self.L8_MEAN.select('B11_median')
        l8dt = self.L8_DDATE
        trees = self.TREE_COVER
        ndvi = self.EVI_IMG
        ndvi_mean = self.EVI_MEAN
        bulk = self.BULK
        clay = self.CLAY
        sand = self.SAND
        crop = self.CROPS_COVER
        moss = self.MOSS_COVER
        grass = self.GRASS_COVER
        bare = self.BARE_COVER
        urban = self.URBAN_COVER
        water = self.WATERP_COVER
        # create lon lat rasters
        coords_tmp = self.S1_SIG0_VV_db.pixelLonLat()
        lon = coords_tmp.select('longitude')
        lat = coords_tmp.select('latitude')

        input_image1 = ee.Image([gvv.toFloat(),
                                 gvh.toFloat(),
                                 lia.toFloat(),
                                 bare.toFloat(),
                                 crop.toFloat(),
                                 trees.toFloat(),
                                 grass.toFloat(),
                                 moss.toFloat(),
                                 urban.toFloat(),
                                 water.toFloat(),
                                 l8_b1.toFloat(),
                                 l8_b2.toFloat(),
                                 l8_b3.toFloat(),
                                 l8_b4.toFloat(),
                                 l8_b5.toFloat(),
                                 l8_b6.toFloat(),
                                 l8_b7.toFloat(),
                                 l8_b10.toFloat(),
                                 l8_b11.toFloat(),
                                 l8dt.toFloat(),
                                 ndvi.toFloat()])

        input_image1 = input_image1.rename(['g0vv','g0vh','lia','bare','crop','trees','grass',
                                            'moss','urban','water','b1','b2','b3','b4','b5','b6','b7',
                                            'b10','b11','l8dt','ndvi'])

        ipt_img_mask1 = input_image1.mask().reduce(ee.Reducer.allNonZero())

        combined_mask = ipt_img_mask1

        input_image1 = input_image1.updateMask(ee.Image(combined_mask))

        sys.setrecursionlimit(5000)
        if self.ORBIT == 'ASCENDING':
            estimated_smc = GBR_tree_A(input_image1)
        else:
            estimated_smc = GBR_tree_D(input_image1)

        estimated_smc = estimated_smc.updateMask(combined_mask)

        # mask negative values
        estimated_smc = estimated_smc.updateMask(estimated_smc.gt(0))
        self.ESTIMATED_SM = estimated_smc
        self.ESTIMATED_MEAN_SM = None

    def _init_avg_sm_GBR(self):
        # load GBR models
        from decisiontree_GEE_step1 import tree as GBR_tree_step1

        avg_asset_name = 'users/felixgreifeneder/AVG_SM/AVG_SM_' + str(math.trunc(self.MINLON)) + '_' + \
                         str(math.trunc(self.MINLAT)) + '_' + \
                         str(math.trunc(self.MINLON) + 1) + '_' + \
                         str(math.trunc(self.MINLAT) + 1) + '_' + \
                         str(math.trunc(self.TRACK_NR)) + '_' + \
                         str(self.sampling) + 'm'

        vv = self.S1_SIG0_VV_db
        k1_vv = self.K1VV
        k1_vh = self.K1VH
        k2_vv = self.K2VV
        k2_vh = self.K2VH
        k3_vv = self.K3VV
        k3_vh = self.K3VH
        k4_vv = self.K4VV
        k4_vh = self.K4VH
        gldas_img = self.GLDAS_IMG
        gldas_mean = self.GLDAS_MEAN
        l8_b1 = self.L8_IMG.select('B1')
        l8_b2 = self.L8_IMG.select('B2')
        l8_b3 = self.L8_IMG.select('B3')
        l8_b4 = self.L8_IMG.select('B4')
        l8_b5 = self.L8_IMG.select('B5')
        l8_b6 = self.L8_IMG.select('B6')
        l8_b7 = self.L8_IMG.select('B7')
        l8_b10 = self.L8_IMG.select('B10')
        l8_b11 = self.L8_IMG.select('B11')
        l8_b1_mean = self.L8_MEAN.select('B1_median')
        l8_b2_mean = self.L8_MEAN.select('B2_median')
        l8_b3_mean = self.L8_MEAN.select('B3_median')
        l8_b4_mean = self.L8_MEAN.select('B4_median')
        l8_b5_mean = self.L8_MEAN.select('B5_median')
        l8_b6_mean = self.L8_MEAN.select('B6_median')
        l8_b7_mean = self.L8_MEAN.select('B7_median')
        l8_b10_mean = self.L8_MEAN.select('B10_median')
        l8_b11_mean = self.L8_MEAN.select('B11_median')
        trees = self.TREE_COVER

        input_image1 = ee.Image([k1_vv.toFloat(),
                                 k1_vh.toFloat(),
                                 k2_vv.toFloat(),
                                 k2_vh.toFloat(),
                                 k3_vv.toFloat(),
                                 k3_vh.toFloat(),
                                 k4_vv.toFloat(),
                                 k4_vh.toFloat(),
                                 l8_b1_mean.toFloat(),
                                 l8_b2_mean.toFloat(),
                                 l8_b3_mean.toFloat(),
                                 l8_b4_mean.toFloat(),
                                 l8_b5_mean.toFloat(),
                                 l8_b6_mean.toFloat(),
                                 l8_b7_mean.toFloat(),
                                 l8_b10_mean.toFloat(),
                                 l8_b11_mean.toFloat(),
                                 trees.toFloat()])

        input_image1 = input_image1.rename(['vvk1', 'vhk1',
                                            'vvk2', 'vhk2',
                                            'vvk3', 'vhk3',
                                            'vvk4', 'vhk4',
                                            'b1', 'b2',
                                            'b3', 'b4',
                                            'b5', 'b6',
                                            'b7', 'b10',
                                            'b11', 'trees'])

        ipt_img_mask1 = input_image1.mask().reduce(ee.Reducer.allNonZero())
        # S1mask = vv.mask()
        # zeromask = input_image1.neq(ee.Image(0)).reduce(ee.Reducer.allNonZero())
        # combined_mask = zeromask.And(ipt_img_mask1)
        combined_mask = ipt_img_mask1

        input_image1 = input_image1.updateMask(ee.Image(combined_mask))
        # test = combined_mask.reduceRegion(ee.Reducer.sum(), geometry=self.roi, scale=250, tileScale=4).getInfo()

        import sys
        sys.setrecursionlimit(3000)
        estimated_smc_avg = GBR_tree_step1(input_image1)
        estimated_smc_avg = estimated_smc_avg.updateMask(combined_mask)

        file_exp = ee.batch.Export.image.toAsset(estimated_smc_avg,
                                                 description='AvgSM2Asset',
                                                 assetId=avg_asset_name,
                                                 region=self.roi.getInfo()['coordinates'],
                                                 scale=self.sampling)

        file_exp.start()

        start = time.time()

        while (file_exp.active() == True):
            time.sleep(2)
        else:
            print('Export of ' + avg_asset_name + ' average soil moisture completed')

    def get_S1_dates(self, tracknr=None, dualpol=True, ascending=True, start='2014-01-01', stop='2020-01-01'):
        # load S1 data
        gee_s1_collection = ee.ImageCollection('COPERNICUS/S1_GRD')

        # ASCENDING acquisitions
        gee_s1_filtered = gee_s1_collection.filter(ee.Filter.eq('instrumentMode', 'IW')) \
            .filterBounds(self.roi) \
            .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
            .filterDate(start, opt_end=stop)
        # .filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'))
        #           .filter(ee.Filter.eq('platform_number', 'A')) \

        if ascending == True:
            # Consider only image from ascending orbits
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))

        if dualpol == True:
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))

        if tracknr is not None:
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.eq('relativeOrbitNumber_start', tracknr))

        # create a list of availalbel dates
        tmp = gee_s1_filtered.getInfo()
        tmp_ids = [x['properties']['system:time_start'] for x in tmp['features']]

        #dates = np.array([dt.datetime(int(x[17:21]), int(x[21:23]), int(x[23:25]), hour=int(x[26:28]),
        #                              minute=int(x[28:30]), second=int(x[30:32])) for x in tmp_ids])
        dates = np.array([dt.datetime.fromtimestamp(int(int(x / 1000))) for x in tmp_ids])

        return dates

    def get_available_S1_tracks(self, dualpol=True):
        # load S1 data
        gee_s1_collection = ee.ImageCollection('COPERNICUS/S1_GRD')

        # ASCENDING acquisitions
        gee_s1_filtered = gee_s1_collection.filter(ee.Filter.eq('instrumentMode', 'IW')) \
            .filterBounds(self.roi) \
            .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
            .filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))
        #           .filter(ee.Filter.eq('platform_number', 'A')) \

        if dualpol == True:
            gee_s1_filtered = gee_s1_filtered.filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))

        # create a list of availalbel dates
        tmp = gee_s1_filtered.getInfo()
        tmp_tracks = [x['properties']['relativeOrbitNumber_start'] for x in tmp['features']]
        tracks = np.unique(tmp_tracks)

        return tracks

    def check_gldas_availability(self, year, month, day):
        gldas_test = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G025/T3H") \
            .select('SoilMoi0_10cm_inst')
        last_gldas = dt.datetime.strptime(gldas_test.aggregate_max('system:index').getInfo(),
                                          "A%Y%m%d_%H%M")
        self.LAST_GLDAS = last_gldas
        doi = dt.date(year=year, month=month, day=day)
        return last_gldas.date() > doi

    def get_gldas(self, date=None):
        # get GLDAS, date can be passed as a string or copied from the extracted S1 scene
        if date is None:
            doi = ee.Date(self.S1_DATE.strftime(format='%Y-%m-%d'))

        # check if Sentinel-1 was retrieved and date is available
        if hasattr(self, 'S1_DATE'):
            gldas_mean = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G025/T3H") \
                .select('SoilMoi0_10cm_inst') \
                .filterDate('2014-10-01', dt.datetime.today().strftime('%Y-%m-%d')) \
                .filter(ee.Filter.calendarRange(self.S1_DATE.hour, self.S1_DATE.hour + 3, field='hour')) \
                .reduce(ee.Reducer.median())
        else:
            gldas_mean = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G025/T3H") \
                .select('SoilMoi0_10cm_inst') \
                .filterDate('2014-10-01', dt.datetime.today().strftime('%Y-%m-%d')) \
                .reduce(ee.Reducer.median())

        gldas_mean = ee.Image(gldas_mean).resample().clip(self.roi)

        # gldas = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G025/T3H") \
        #     .select('SoilMoi0_10cm_inst') \
        #     .filterDate(doi, doi.advance(3, 'hour'))
        #
        # if gldas.size().getInfo() == 0:
        #     print('No GLDAS product for specified date')
        #     gldas_test = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G025/T3H") \
        #                             .select('SoilMoi0_10cm_inst')
        #     last_gldas = gldas_test.aggregate_max('system:index').getInfo()
        #     print('ID of latest available product: ' + last_gldas)
        #     self.GLDAS_IMG = None
        #     self.GLDAS_MEAN = None
        #     return
        #
        # gldas_img = ee.Image(gldas.first()).resample().clip(self.roi)
        gldas_img = gldas_mean

        try:
            self.GLDAS_IMG = gldas_img
            self.GLDAS_MEAN = gldas_mean
        except:
            return None

    def get_l8(self, date=None):
        # get Landsat-8, date can be passed as a string or copied from the extracted S1 scene
        def setresample(image):
            image = image.resample()
            return image

        def mask(image):
            # aerosols
            # image = image.updateMask(image.select('sr_aerosol').eq(2).bitwiseOr(
            #     image.select('sr_aerosol').eq(32).bitwiseOr(
            #         image.select('sr_aerosol').eq(96).bitwiseOr(
            #             image.select('sr_aerosol').eq(160).bitwiseOr(
            #                 image.select('sr_aerosol').eq(66).bitwiseOr(
            #                     image.select('sr_aerosol').eq(130)
            #                 ))))))

            # clouds
            def getQABits(image, start, end, newName):
                pattern = 0
                for i in range(start, end + 1):
                    pattern = pattern + int(math.pow(2, i))

                return image.select([0], [newName]).bitwiseAnd(pattern).rightShift(start)

            def cloud_shadows(image):
                QA = image.select('pixel_qa')
                return getQABits(QA, 3, 3, 'Cloud_shadows').eq(0)

            def clouds(image):
                QA = image.select('pixel_qa')
                return getQABits(QA, 5, 5, 'Cloud').eq(0)

            # frozen soil / snow
            def frzn(image):
                doi = ee.Date(image.get('system:time_start'))
                snow = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G025/T3H") \
                    .select('SWE_inst') \
                    .filterDate(doi, doi.advance(3, 'hour'))

                snow_img = ee.Image(snow.first()).resample().clip(self.roi)

                snow_mask = snow_img.expression('(b(0) < 3) ? 1 : 0')

                fs = ee.ImageCollection("NASA/GLDAS/V021/NOAH/G025/T3H") \
                    .select('SoilTMP0_10cm_inst') \
                    .filterDate(doi, doi.advance(3, 'hour'))

                fs_img = ee.Image(fs.first()).resample().clip(self.roi)

                fs_mask = fs_img.expression('(b(0) > 275) ? 1 : 0')

                return snow_mask.And(fs_mask)

            image = image.updateMask(cloud_shadows(image))
            image = image.updateMask(clouds(image))
            # image = image.updateMask(frzn(image))

            # # radiometric saturation
            # image = image.updateMask(image.select('radsat_qa').eq(2))
            return image

        def addDate(image):
            date_img = ee.Image(image.date().difference(doi.strftime('%Y-%m-%d'), 'second')).abs().float().rename(
                ['Ddate']).multiply(-1)
            # date_img = date_img.changeProj(date_img.projection(), image.select('B1').projection())

            return (image.addBands(date_img))

        gee_l8_collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')  # .map(setresample)

        if date is None:
            doi = self.S1_DATE
        gee_l8_collection = gee_l8_collection.map(addDate)

        # load collection
        gee_l8_collection = gee_l8_collection.map(mask)

        gee_l8_mean = gee_l8_collection.filterDate('2014-10-01', doi.strftime('%Y-%m-%d')) \
            .reduce(ee.Reducer.median()) \
            .clip(self.roi)

        # fiter
        sdate = doi - dt.timedelta(days=30)
        edate = doi + dt.timedelta(days=30)
        gee_l8_fltd = gee_l8_collection.filterBounds(self.roi).filterDate(sdate.strftime('%Y-%m-%d'),
                                                                          edate.strftime('%Y-%m-%d'))

        # # create a list of availalbel dates
        # tmp = gee_l8_fltd.getInfo()
        # tmp_ids = [x['properties']['system:index'] for x in tmp['features']]
        # dates = np.array([dt.datetime.strptime(x[12::], '%Y%m%d').date() for x in tmp_ids])
        #
        # # find the closest acquisitions
        # doi_index = np.argmin(np.abs(dates - doi))
        # date_selected = dates[doi_index]
        # date_diff = np.min(abs(dates - doi)).total_seconds()
        #
        # # filter collection for respective dates
        # edate = date_selected + dt.timedelta(days=1)
        # gee_l8_fltd = gee_l8_fltd.filterDate(date_selected.strftime('%Y-%m-%d'), edate.strftime('%Y-%m-%d'))
        # mosaic scenes
        # gee_l8_mosaic = ee.Image(gee_l8_fltd.mosaic().clip(self.roi))

        # select pixels with the smalles time gap to doi and mosaic spatially
        gee_l8_mosaic = gee_l8_fltd.qualityMosaic('Ddate').float()

        try:
            self.L8_IMG = gee_l8_mosaic.clip(self.roi)
            self.L8_MEAN = gee_l8_mean
            self.L8_DDATE = gee_l8_mosaic.select('Ddate').clip(self.roi).multiply(-1)
        except:
            return None

    def get_tree_cover(self):
        tree_cover_image = ee.ImageCollection("GLCF/GLS_TCC").filterBounds(self.roi).filter(
            ee.Filter.eq('year', 2010)).mosaic()
        # tree_cover_image = tree_cover_image.updateMask(tree_cover_image.select('tree_canopy_cover').lt(20))
        self.TREE_COVER = tree_cover_image.select('tree_canopy_cover').clip(self.roi)

    def get_globcover(self):
        # get the globcover land-cover classification
        globcover_image = ee.Image("ESA/GLOBCOVER_L4_200901_200912_V2_3")
        land_cover = globcover_image.select('landcover').clip(self.roi)
        self.LAND_COVER = land_cover

    def get_terrain(self):
        # get SRTM data
        elev = ee.Image("CGIAR/SRTM90_V4").select('elevation').clip(self.roi).resample()
        aspe = ee.Terrain.aspect(ee.Image("CGIAR/SRTM90_V4")).select('aspect').clip(self.roi).resample()
        slop = ee.Terrain.slope(ee.Image("CGIAR/SRTM90_V4")).select('slope').clip(self.roi).resample()
        self.TERRAIN = (elev, aspe, slop)

    def get_modis_evi(self, date=None):

        def mask(image):
            # mask image
            immask = image.select('SummaryQA').eq(ee.Image(0))
            image = image.updateMask(immask)

            return image

        def addDate(image):
            date_img = ee.Image(image.date().difference(doi.strftime('%Y-%m-%d'), 'second')).abs().float().rename(
                ['Ddate']).multiply(-1)

            return image.addBands(date_img)

        # load collection
        evi_collection = ee.ImageCollection('MODIS/006/MOD13Q1')

        if date is None:
            doi = self.S1_DATE
        evi_collection = evi_collection.map(addDate)

        # apply mask
        evi_collection = evi_collection.map(mask)

        # compute avg
        evi_mean = evi_collection.filterDate('2014-10-01', doi.strftime('%Y-%m-%d')) \
            .reduce(ee.Reducer.median()) \
            .clip(self.roi)

        # fiter
        sdate = doi - dt.timedelta(days=30)
        edate = doi + dt.timedelta(days=30)
        evi_fltd = evi_collection.filterBounds(self.roi).filterDate(sdate.strftime('%Y-%m-%d'),
                                                                    edate.strftime('%Y-%m-%d'))

        # select pixels with the smallest time gap to doi and mosaic spatially
        evi_mosaic = evi_fltd.qualityMosaic('Ddate').float()

        try:
            self.EVI_IMG = evi_mosaic.select('EVI').clip(self.roi)
            self.EVI_MEAN = evi_mean.select('EVI_median')
        except:
            return None

    def get_bulk_density(self):
        bulkimg = ee.Image("OpenLandMap/SOL/SOL_BULKDENS-FINEEARTH_USDA-4A1H_M/v02").select('b0')
        self.BULK = bulkimg.resample()

    def get_clay_content(self):
        clayimg = ee.Image("OpenLandMap/SOL/SOL_CLAY-WFRACTION_USDA-3A1A1A_M/v02").select('b0')
        self.CLAY = clayimg.resample()

    def get_sand_content(self):
        sandimg = ee.Image("OpenLandMap/SOL/SOL_SAND-WFRACTION_USDA-3A1A1A_M/v02").select('b0')
        self.SAND = sandimg.resample()

    def get_copernicus_lc(self):

        copernicus_collection = ee.ImageCollection('COPERNICUS/Landcover/100m/Proba-V/Global')
        copernicus_image = ee.Image(copernicus_collection.toList(1000).get(0))
        self.LC_ID = copernicus_image.select('discrete_classification')
        self.FOREST_TYPE = copernicus_image.select('forest_type')
        self.BARE_COVER = copernicus_image.select('bare-coverfraction').resample()
        self.CROPS_COVER = copernicus_image.select('crops-coverfraction').resample()
        self.GRASS_COVER = copernicus_image.select('grass-coverfraction').resample()
        self.MOSS_COVER = copernicus_image.select('moss-coverfraction').resample()
        self.SHRUB_COVER = copernicus_image.select('shrub-coverfraction').resample()
        self.TREE_COVER = copernicus_image.select('tree-coverfraction').resample()
        self.URBAN_COVER = copernicus_image.select('urban-coverfraction').resample()
        self.WATERP_COVER = copernicus_image.select('water-permanent-coverfraction').resample()
        self.WATERS_COVER = copernicus_image.select('water-seasonal-coverfraction').resample()

    def GEE_2_disk(self, outdir=None, raster='ESTIMATED_SM', name='SM', timeout=True):
        # Download GEE rasters - specify raster as string

        geds = self.__getattribute__(raster)

        if outdir is None:
            outdir = self.workdir

        file_exp = ee.batch.Export.image.toDrive(image=geds, description='fileexp' + name,
                                                 fileNamePrefix=name, scale=self.sampling,
                                                 region=self.roi.getInfo()['coordinates'],
                                                 maxPixels=1000000000000)

        file_exp.start()

        start = time.time()
        success = 1

        while (file_exp.active() == True):
            time.sleep(2)
            if timeout == True and (time.time() - start) > 4800:
                success = 0
                break
        else:
            print('Export completed')

        # if success == 1:
        #     # initialise Google Drive
        #     drive_handler = gdrive()
        #     print('Downloading files ...')
        #     print(name)
        #     drive_handler.download_file(name + '.tif',
        #                                 outdir + name + '.tif')
        #     drive_handler.delete_file(name + '.tif')
        # else:
        #     file_exp.cancel()
