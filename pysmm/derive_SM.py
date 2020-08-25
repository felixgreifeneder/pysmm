from pysmm.GEE_wrappers import GEE_extent
from pysmm.GEE_wrappers import GEE_pt
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import math
import datetime as dt

def get_map(minlon, minlat, maxlon, maxlat,
            outpath,
            sampling=100,
            year=None, month=None, day=None,
            tracknr=None,
            overwrite=False,
            tempfilter=True,
            mask='Globcover',
            masksnow=False,
            start=None,
            stop=None):
    """Get S1 soil moisture map

            Atributes:
            minlon, minlat, maxlon, maxlat: (float) extent of soil moisture map
            outpath: (string) destination for soil moisture map export
            sampling: (integer) map sampling
            year, month, day (optional): specify date for extracted map - if not specified, the entire
                                         time-series of maps will be extracted; if specified, the S1 acquisition
                                         closest (in time) will be selected
            tracknr (optional): (integer) Use data from a specific Sentinel-1 track only
            tempfilter: (boolean) apply multi-temporal speckle filter
            mask: (string) select 'Globcover' or 'Corine' (europe only) land-cover classifications for the
                   masking of the map
            masksnow: (boolean) apply snow mask

        """

    maskcorine=False
    maskglobcover=False

    if mask == 'Globcover':
        maskglobcover = True
    elif mask == 'Corine':
        maskcorine = True
    elif mask == None:
        pass
    else:
        print(mask + ' is not recognised as a valid land-cover classification')
        return

    if year is not None:
        # initialise GEE retrieval dataset
        GEE_interface = GEE_extent(minlon, minlat, maxlon, maxlat, outpath, sampling=sampling)
        GEE_interface.init_SM_retrieval(year, month, day)

        if GEE_interface.ORBIT == 'ASCENDING':
            orbit_prefix='A'
        else:
            orbit_prefix='D'
        outname = 'SMCS1_' + \
                  str(GEE_interface.S1_DATE.year) + \
                  '{:02d}'.format(GEE_interface.S1_DATE.month) + \
                  '{:02d}'.format(GEE_interface.S1_DATE.day) + '_' + \
                  '{:02d}'.format(GEE_interface.S1_DATE.hour) + \
                  '{:02d}'.format(GEE_interface.S1_DATE.minute) + \
                  '{:02d}'.format(GEE_interface.S1_DATE.second) + '_' + \
                  '{:03d}'.format(math.trunc(GEE_interface.TRACK_NR)) + '_' + orbit_prefix
            # Estimate soil moisture
        GEE_interface.estimate_SM_GBR()

        #if GEE_interface.ESTIMATED_SM is not None:
        #    GEE_interface.GEE_2_disk(name=outname, timeout=False)
            #GEE_interface.GEE_2_disk(raster='ESTIMATED_MEAN_SM', name='SMC_map_avg', timeout=False)

        GEE_interface = None

    else:

        # if no specific date was specified extract entire time series
        GEE_interface = GEE_extent(minlon, minlat, maxlon, maxlat, outpath, sampling=sampling)

        # get list of S1 dates
        dates = GEE_interface.get_S1_dates(tracknr=tracknr, ascending=False, start=start, stop=stop)
        dates = np.unique(dates)
        # delete dates belonging to the same track
        i = 0
        while i + 2 <= len(dates):
            if dates.size == 1:
                break
            if (dates[i + 1] - dates[i]) < dt.timedelta(hours=1):
                dates = np.delete(dates, i + 1)
            else:
                i = i + 1
        print(dates)

        for dateI in dates:

            # initialise retrieval
            GEE_interface.init_SM_retrieval(dateI.year, dateI.month, dateI.day, hour=dateI.hour, minute=dateI.minute)

            if GEE_interface.ORBIT == 'ASCENDING':
                orbit_prefix = 'A'
            else:
                orbit_prefix = 'D'
            outname = 'SMCS1_' + \
                      str(GEE_interface.S1_DATE.year) + \
                      '{:02d}'.format(GEE_interface.S1_DATE.month) + \
                      '{:02d}'.format(GEE_interface.S1_DATE.day) + '_' + \
                      '{:02d}'.format(GEE_interface.S1_DATE.hour) + '_' + \
                      '{:03d}'.format(math.trunc(GEE_interface.TRACK_NR)) + '_' + orbit_prefix

            if overwrite == False and os.path.exists(outpath + outname + '.tif'):
                print(outname + ' already done')
                continue

            # Estimate soil moisture
            GEE_interface.estimate_SM_GBR_1step()

            if GEE_interface.ESTIMATED_SM is not None:
                GEE_interface.GEE_2_disk(name=outname, timeout=False)

        GEE_interface = None


def _init_avg_sm(outpath,
                 sampling=100,
                 overwrite=False,
                 tempfilter=False,
                 mask=None,
                 masksnow=False):
    """Get S1 soil moisture map

            Atributes:
            minlon, minlat, maxlon, maxlat: (float) extent of soil moisture map
            outpath: (string) destination for soil moisture map export
            sampling: (integer) map sampling
            year, month, day (optional): specify date for extracted map - if not specified, the entire
                                         time-series of maps will be extracted; if specified, the S1 acquisition
                                         closest (in time) will be selected
            tracknr (optional): (integer) Use data from a specific Sentinel-1 track only
            tempfilter: (boolean) apply multi-temporal speckle filter
            mask: (string) select 'Globcover' or 'Corine' (europe only) land-cover classifications for the
                   masking of the map
            masksnow: (boolean) apply snow mask

        """

    maskcorine=False
    maskglobcover=False

    if mask == 'Globcover':
        maskglobcover = True
    elif mask == 'Corine':
        maskcorine = True
    elif mask == None:
        pass
    else:
        print(mask + ' is not recognised as a valid land-cover classification')
        return

    year = 2017
    month = 1
    day = 1

    for ilon in range(25,-11,-1):
        for ilat in range(36,60):
            if (ilon < -9) and (ilat < 50):
                continue
            GEE_interface = GEE_extent(ilon, ilat, ilon+1, ilat+1, outpath, sampling=sampling)

            # check availability of GLDAS
            if GEE_interface.check_gldas_availability(year, month, day) == False:
                print('No GLDAS data available for given date')
                return

            # get tree cover
            GEE_interface.get_tree_cover()

            available_tracks = GEE_interface.get_available_S1_tracks()
            for itrack in available_tracks:
                try:
                    # retrieve S1
                    GEE_interface.get_S1(year, month, day,
                                         tempfilter=tempfilter,
                                         applylcmask=maskcorine,
                                         mask_globcover=maskglobcover,
                                         trackflt=itrack,
                                         masksnow=masksnow)
                    # retrieve GLDAS
                    GEE_interface.get_gldas()
                    # get Globcover
                    GEE_interface.get_globcover()
                    # get the SRTM
                    GEE_interface.get_terrain()
                    # get L8
                    GEE_interface.get_l8()

                    # Estimate soil moisture
                    GEE_interface._init_avg_sm_GBR()
                except:
                    continue

            GEE_interface = None


def get_ts(loc,
           workpath,
           tracknr=None,
           footprint=50,
           masksnow=True,
           calc_anomalies=False,
           create_plots=False,
           names=None):
    """Get S1 soil moisture time-series

        Atributes:
        loc: (tuple or list of tuples) longitude and latitude in decimal degrees
        workpath: destination for output files
        tracknr (optional): Use data from a specific Sentinel-1 track only
        footprint: time-series footprint
        masksnow: apply automatic wet snow mask
        calc_anomalies: (boolean) calculate anomalies
        create_plots: (boolean) generate and save time-series plots to workpath
        names: (string or list of strings, optional): list of time-series names

    """

    if isinstance(loc, list):
        print('list')
    else:
        loc = [loc]

    if names is not None:
        if isinstance(names, list):
            print('Name list specified')
        else:
            names = [names]

    sm_ts_out = list()
    names_out = list()

    cntr = 0
    for iloc in loc:
        # iterate through the list of points to extract
        lon = iloc[0]
        lat = iloc[1]

        if names is not None:
            iname = names[cntr]
        else:
            iname = None

        print('Estimating surface soil moisture for lon: ' + str(lon) + ' lat: ' + str(lat))

        # initialize GEE point object
        gee_pt_obj = GEE_pt(lon, lat, workpath, buffer=footprint)
        #sm_ts = gee_pt_obj.extr_SM(tracknr=tracknr, masksnow=masksnow, calc_anomalies=calc_anomalies)
        sm_ts = gee_pt_obj.extr_S1(maskwinter=False, trackflt=117, masksnow=False, tempfilter=False, returnLIA=True,
                                   globcover_mask=False)

        #if isinstance(sm_ts, pd.Series) or isinstance(gee_pt_obj.S1TS, pd.DataFrame):
        if iname is not None:
            # create plots
            if create_plots == True:
                if calc_anomalies == False:
                    # plot s1 soil moisture vs gldas_downscaled
                    fig, ax = plt.subplots(figsize=(6.5,2.7))
                    line1, = ax.plot(sm_ts.index, sm_ts,
                                     color='b',
                                     linestyle='-',
                                     marker='+',
                                     label='S1 Soil Moisture',
                                     linewidth=0.2)
                    ax.set_ylabel('Soil Moisture [%-Vol.]')
                    if iname is None:
                        plotname = 's1_sm_' + str(lon) + '_' + str(lat) + '.png'
                    else:
                        plotname = 's1_sm_' + iname + '.png'
                else:
                    fig, ax = plt.subplots(figsize=(6.5,2.7))
                    line1, = ax.plot(sm_ts.index, sm_ts['ANOM'].values,
                                     color='r',
                                     linestyle='-',
                                     marker='+',
                                     label='S1 Soil Moisture Anomaly',
                                     linewidth=0.2)
                    x0 = [sm_ts.index[0], sm_ts.index[-1]]
                    y0 = [0, 0]
                    line2, = ax.plot(x0, y0,
                                     color='k',
                                     linestyle='--',
                                     linewidth=0.2)
                    ax.set_ylabel('Soil Moisture Anomaly [%-Vol.]')
                    #plt.legend(handles=[line1, line2])
                    if iname is None:
                        plotname = 's1_sm_anom_' + str(lon) + '_' + str(lat) + '.png'
                    else:
                        plotname = 's1_sm_anom_' + iname + '.png'
                plt.setp(ax.get_xticklabels(), fontsize=6)
                plt.savefig(workpath + plotname, dpi=300)
            sm_ts_out.append(0)
            names_out.append(iname)
            gee_pt_obj.S1TS['117'].sort_index().to_csv(workpath + iname + '.csv')

        gee_pt_obj = None
        cntr = cntr + 1
    if names is not None:
        return (sm_ts_out, names_out)
    else:
        return sm_ts_out



