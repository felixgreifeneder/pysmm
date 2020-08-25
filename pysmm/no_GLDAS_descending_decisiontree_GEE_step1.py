import ee 

def tree(feature_stack): 

  prediction = ee.Image(0.1452395)
  learning_rate = ee.Image(0.1)
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('lon') <= -105.8655014038086) ? " + 
"(b('sand') <= 47.5) ? " + 
"-0.041838402481197" + 
":  " + 
"-0.07006904808804393" + 
":  " + 
"(b('L8b6med') <= 3715.5) ? " + 
"0.005559887759750936" + 
":  " + 
"-0.07760313779793003" + 
":  " + 
"(b('grass') <= 37.746646881103516) ? " + 
"(b('sand') <= 77.5) ? " + 
"0.03603991011486334" + 
":  " + 
"0.07176049705594778" + 
":  " + 
"(b('sand') <= 59.0) ? " + 
"0.2804882758193546" + 
":  " + 
"0.1838566523331862" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('lon') <= -105.10324096679688) ? " + 
"(b('lat') <= 41.11815643310547) ? " + 
"-0.054006967775903976" + 
":  " + 
"-0.028553605009745273" + 
":  " + 
"(b('L8b6med') <= 3715.5) ? " + 
"0.0077318422970309025" + 
":  " + 
"-0.069842824018137" + 
":  " + 
"(b('grass') <= 37.746646881103516) ? " + 
"(b('lon') <= 9.200799942016602) ? " + 
"0.048698485746262565" + 
":  " + 
"-0.001093494285847633" + 
":  " + 
"(b('lat') <= 53.61935043334961) ? " + 
"0.2524394482374191" + 
":  " + 
"0.16547098709986763" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('ndvi_med') <= 1879.5) ? " + 
"(b('gvhk2') <= 0.5126813054084778) ? " + 
"-0.04532694694033736" + 
":  " + 
"0.026094069271919807" + 
":  " + 
"(b('bulk') <= 137.5) ? " + 
"-0.03348887888545035" + 
":  " + 
"0.015499363187822886" + 
":  " + 
"(b('gvvmean') <= -13.141220569610596) ? " + 
"(b('sand') <= 53.5) ? " + 
"0.23163647702998588" + 
":  " + 
"0.16309045869964167" + 
":  " + 
"(b('L8b3med') <= 563.5) ? " + 
"0.20152774297274076" + 
":  " + 
"0.03951366617867846" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('lon') <= -105.8655014038086) ? " + 
"(b('ndvi_med') <= 1239.25) ? " + 
"-0.055954766430822006" + 
":  " + 
"-0.031161311506094636" + 
":  " + 
"(b('ndvi_med') <= 3353.5) ? " + 
"-0.00893226084970186" + 
":  " + 
"0.08275945120580253" + 
":  " + 
"(b('gvvmean') <= -13.141220569610596) ? " + 
"(b('gvhmean') <= -14.11482572555542) ? " + 
"0.13216868996384315" + 
":  " + 
"0.19643311216628745" + 
":  " + 
"(b('L8b3med') <= 563.5) ? " + 
"0.18137496867546668" + 
":  " + 
"0.03556229956081059" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('lon') <= -106.60049438476562) ? " + 
"(b('sand') <= 47.5) ? " + 
"-0.027188019389370148" + 
":  " + 
"-0.0488093115743409" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.011483145101206021" + 
":  " + 
"-0.04129093945518334" + 
":  " + 
"(b('grass') <= 37.746646881103516) ? " + 
"(b('sand') <= 77.5) ? " + 
"0.02093715595536846" + 
":  " + 
"0.05220700220177786" + 
":  " + 
"(b('L8b3med') <= 626.0) ? " + 
"0.18364300240281334" + 
":  " + 
"0.11650734064023864" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('ndvi_med') <= 1879.5) ? " + 
"(b('gvhk2') <= 0.5126813054084778) ? " + 
"-0.034436865584050985" + 
":  " + 
"0.024447578222516808" + 
":  " + 
"(b('L8b3med') <= 842.25) ? " + 
"-0.032194620323576506" + 
":  " + 
"0.01370589707558218" + 
":  " + 
"(b('gvhmean') <= -13.141220569610596) ? " + 
"(b('lat') <= 53.63138008117676) ? " + 
"0.16324200749985726" + 
":  " + 
"0.10958652910836439" + 
":  " + 
"(b('L8b3med') <= 563.5) ? " + 
"0.14487317156763868" + 
":  " + 
"0.0285826272605152" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('lon') <= -105.8655014038086) ? " + 
"(b('bulk') <= 132.5) ? " + 
"-0.05376174324594058" + 
":  " + 
"-0.024278320035157886" + 
":  " + 
"(b('ndvi_med') <= 3353.5) ? " + 
"-0.006788305499401986" + 
":  " + 
"0.0741281545319997" + 
":  " + 
"(b('gvvmean') <= -13.141220569610596) ? " + 
"(b('gvvmean') <= -14.11482572555542) ? " + 
"0.0946168462761118" + 
":  " + 
"0.14523341332466896" + 
":  " + 
"(b('sand') <= 78.5) ? " + 
"0.019003261642046125" + 
":  " + 
"0.05445556496316471" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('ndvi_med') <= 1879.5) ? " + 
"(b('grass') <= 17.183883666992188) ? " + 
"-0.04960671948052037" + 
":  " + 
"-0.022366993731366375" + 
":  " + 
"(b('bulk') <= 137.5) ? " + 
"-0.023471811126900066" + 
":  " + 
"0.015449133595958538" + 
":  " + 
"(b('grass') <= 41.50375556945801) ? " + 
"(b('L8b6med') <= 2848.75) ? " + 
"0.01688416459606442" + 
":  " + 
"0.05557465676212284" + 
":  " + 
"(b('L8b3med') <= 626.0) ? " + 
"0.1365653473774171" + 
":  " + 
"0.08632588355697209" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('ndvi_med') <= 3353.5) ? " + 
"(b('gvhk2') <= 0.4439784288406372) ? " + 
"-0.022362065685389957" + 
":  " + 
"0.015091728047508777" + 
":  " + 
"(b('gvvmean') <= -10.278248310089111) ? " + 
"0.02034131474900476" + 
":  " + 
"0.12677425810944656" + 
":  " + 
"(b('grass') <= 41.50375556945801) ? " + 
"(b('crops') <= 47.066659927368164) ? " + 
"-0.005268835141796951" + 
":  " + 
"0.026981537804218223" + 
":  " + 
"(b('L8b3med') <= 626.0) ? " + 
"0.12290881263967542" + 
":  " + 
"0.07769329520127487" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 50.691999435424805) ? " + 
"(b('lat') <= 41.426435470581055) ? " + 
"(b('grass') <= 91.94809341430664) ? " + 
"-0.02627012834391476" + 
":  " + 
"0.027254879573253076" + 
":  " + 
"(b('crops') <= 68.13479995727539) ? " + 
"-0.005386884494970431" + 
":  " + 
"0.06099906675132728" + 
":  " + 
"(b('gvhmean') <= -13.141220569610596) ? " + 
"(b('gvhmean') <= -14.11482572555542) ? " + 
"0.06855335810029106" + 
":  " + 
"0.10794448869912099" + 
":  " + 
"(b('lon') <= 9.210049629211426) ? " + 
"0.025124600512724783" + 
":  " + 
"-0.018225432830066307" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('ndvi_med') <= 3353.5) ? " + 
"(b('gvhk2') <= 0.4439784288406372) ? " + 
"-0.01876426541422465" + 
":  " + 
"0.014162248889833697" + 
":  " + 
"(b('gvhk3') <= 0.0017232734244316816) ? " + 
"0.06135288177774405" + 
":  " + 
"-0.017322567172524717" + 
":  " + 
"(b('gvvmean') <= -13.141220569610596) ? " + 
"(b('gvhk3') <= -0.021371884271502495) ? " + 
"0.16120705833512206" + 
":  " + 
"0.07980442086928992" + 
":  " + 
"(b('sand') <= 78.5) ? " + 
"0.010373869575945585" + 
":  " + 
"0.04094861116227996" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('L8b10med') <= 2543.0) ? " + 
"(b('crops') <= 68.13479995727539) ? " + 
"-0.007386300956194051" + 
":  " + 
"0.036870631447648454" + 
":  " + 
"(b('sand') <= 46.5) ? " + 
"-0.008655608108799654" + 
":  " + 
"-0.037188824891021" + 
":  " + 
"(b('grass') <= 41.50375556945801) ? " + 
"(b('L8b6med') <= 2848.75) ? " + 
"0.009490491456828395" + 
":  " + 
"0.042900324352395186" + 
":  " + 
"(b('L8b3med') <= 626.0) ? " + 
"0.09263968232913078" + 
":  " + 
"0.055707770469339286" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.62804985046387) ? " + 
"(b('sand') <= 53.5) ? " + 
"(b('gvhk2') <= 0.4439784288406372) ? " + 
"-0.008812761500269273" + 
":  " + 
"0.026693457203184893" + 
":  " + 
"(b('gvhk3') <= -0.0031420664163306355) ? " + 
"-0.06730985630315808" + 
":  " + 
"-0.02319696071704654" + 
":  " + 
"(b('grass') <= 41.50375556945801) ? " + 
"(b('L8b6med') <= 2848.75) ? " + 
"0.008541442311145562" + 
":  " + 
"0.038610291917155676" + 
":  " + 
"(b('lat') <= 53.63138008117676) ? " + 
"0.08209696967628179" + 
":  " + 
"0.04821974021695364" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 2914.25) ? " + 
"(b('gvhk2') <= 0.4439784288406372) ? " + 
"(b('lat') <= 49.80514907836914) ? " + 
"-0.016449177577233562" + 
":  " + 
"0.0706261373245412" + 
":  " + 
"(b('sand') <= 49.5) ? " + 
"0.03036724581265003" + 
":  " + 
"-0.02344918069946234" + 
":  " + 
"(b('gvhmean') <= -13.141220569610596) ? " + 
"(b('sand') <= 41.0) ? " + 
"-0.01084109941628076" + 
":  " + 
"0.06253453328251136" + 
":  " + 
"(b('lat') <= 39.301645278930664) ? " + 
"-0.05020003062961633" + 
":  " + 
"0.015945912541308057" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 2914.25) ? " + 
"(b('bare') <= 1.1451977491378784) ? " + 
"(b('lon') <= -107.54017639160156) ? " + 
"-0.021957349098302017" + 
":  " + 
"0.011998864323943653" + 
":  " + 
"(b('gvhmean') <= -11.820406436920166) ? " + 
"-0.009821101791593836" + 
":  " + 
"-0.0368138181318841" + 
":  " + 
"(b('gvvmean') <= -13.141220569610596) ? " + 
"(b('sand') <= 41.0) ? " + 
"-0.009756989474652679" + 
":  " + 
"0.05628107995426023" + 
":  " + 
"(b('lat') <= 39.301645278930664) ? " + 
"-0.04518002756665471" + 
":  " + 
"0.014351321287177251" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 41.426435470581055) ? " + 
"(b('grass') <= 91.94809341430664) ? " + 
"(b('lat') <= 41.37735939025879) ? " + 
"-0.015848822664530617" + 
":  " + 
"-0.06656407745827961" + 
":  " + 
"(b('lon') <= -104.94619369506836) ? " + 
"-0.018841462661230293" + 
":  " + 
"0.04164198747840586" + 
":  " + 
"(b('L8b3med') <= 619.0) ? " + 
"(b('lon') <= 22.87806510925293) ? " + 
"0.04773281590334368" + 
":  " + 
"0.09109765276240094" + 
":  " + 
"(b('L8b5med') <= 2406.5) ? " + 
"-0.00848720159385279" + 
":  " + 
"0.016231274690561064" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 41.426435470581055) ? " + 
"(b('grass') <= 91.94809341430664) ? " + 
"(b('L8b5med') <= 2628.25) ? " + 
"-0.023408619684996336" + 
":  " + 
"-0.00835139376098143" + 
":  " + 
"(b('L8b6med') <= 2957.5) ? " + 
"-0.029212338366112492" + 
":  " + 
"0.03373715608260752" + 
":  " + 
"(b('L8b3med') <= 619.0) ? " + 
"(b('lon') <= 22.87806510925293) ? " + 
"0.04295953431300932" + 
":  " + 
"0.08198788748616086" + 
":  " + 
"(b('lat') <= 41.73293495178223) ? " + 
"0.050104547790034946" + 
":  " + 
"0.003959992052448982" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 2914.25) ? " + 
"(b('gvhk2') <= 0.35234180092811584) ? " + 
"(b('lat') <= 51.1732292175293) ? " + 
"-0.014663103566734025" + 
":  " + 
"0.0630277481954982" + 
":  " + 
"(b('sand') <= 49.5) ? " + 
"0.016183267668089068" + 
":  " + 
"-0.022122224193001427" + 
":  " + 
"(b('bare') <= 11.304055213928223) ? " + 
"(b('lon') <= -76.4552993774414) ? " + 
"-0.01978182743824417" + 
":  " + 
"0.01763850864420942" + 
":  " + 
"0.15096757670798794" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 1.3976932764053345) ? " + 
"(b('lon') <= -107.54017639160156) ? " + 
"(b('L8b6med') <= 2327.5) ? " + 
"0.059657678998692676" + 
":  " + 
"-0.026641514337733326" + 
":  " + 
"(b('L8b6med') <= 3724.0) ? " + 
"0.016662542460656706" + 
":  " + 
"-0.031417976530305126" + 
":  " + 
"(b('bulk') <= 137.5) ? " + 
"(b('grass') <= 6.984619319438934) ? " + 
"0.018624444006013402" + 
":  " + 
"-0.03366782879790843" + 
":  " + 
"(b('lat') <= 41.426435470581055) ? " + 
"-0.014833400638589834" + 
":  " + 
"0.02250269867634189" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 1.3976932764053345) ? " + 
"(b('lon') <= -107.54017639160156) ? " + 
"(b('gvvmean') <= -11.454290866851807) ? " + 
"-0.02397736290396" + 
":  " + 
"0.0536919110988234" + 
":  " + 
"(b('L8b6med') <= 3724.0) ? " + 
"0.014996288214591029" + 
":  " + 
"-0.028276178877274613" + 
":  " + 
"(b('bulk') <= 137.5) ? " + 
"(b('ndvi_med') <= 2831.0) ? " + 
"-0.03767963599224015" + 
":  " + 
"-0.01200420239252236" + 
":  " + 
"(b('ndvi_med') <= 2181.5) ? " + 
"-0.010152049235635601" + 
":  " + 
"0.03540844820858734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('L8b5med') <= 2365.25) ? " + 
"(b('L8b5med') <= 1898.0) ? " + 
"0.046222869384820536" + 
":  " + 
"-0.010651182048620375" + 
":  " + 
"(b('L8b6med') <= 2659.5) ? " + 
"-0.003273784558790194" + 
":  " + 
"0.017457801645159615" + 
":  " + 
"(b('grass') <= 14.918523788452148) ? " + 
"(b('gvhk2') <= 0.4062114655971527) ? " + 
"-0.01741841620298059" + 
":  " + 
"-0.07568053026620673" + 
":  " + 
"(b('grass') <= 51.18161964416504) ? " + 
"0.015379947440838534" + 
":  " + 
"-0.02073939880774972" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 678.0) ? " + 
"(b('lon') <= 9.173149585723877) ? " + 
"(b('lat') <= 39.22870063781738) ? " + 
"-0.03014222913636528" + 
":  " + 
"0.016447833868090903" + 
":  " + 
"(b('gvhk3') <= -0.013198153348639607) ? " + 
"0.07224069961032477" + 
":  " + 
"0.037122979664576505" + 
":  " + 
"(b('ndvi_med') <= 4415.0) ? " + 
"(b('L8b3med') <= 845.0) ? " + 
"-0.01744111683396226" + 
":  " + 
"-0.0015302755617361756" + 
":  " + 
"(b('lat') <= 55.933950424194336) ? " + 
"0.034279004052514335" + 
":  " + 
"-0.0006247630982788577" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('L8b5med') <= 2417.5) ? " + 
"(b('L8b5med') <= 1898.0) ? " + 
"0.04080302282708072" + 
":  " + 
"-0.008331800754249831" + 
":  " + 
"(b('lat') <= 41.189334869384766) ? " + 
"-0.004617377311094553" + 
":  " + 
"0.016045276845838067" + 
":  " + 
"(b('gvhk2') <= 0.4412725418806076) ? " + 
"(b('ndvi_med') <= 1709.5) ? " + 
"-0.013185506483740088" + 
":  " + 
"-0.04791623784537673" + 
":  " + 
"(b('crops') <= 77.83634567260742) ? " + 
"0.019736173633544223" + 
":  " + 
"-0.07996798394903454" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 1.3976932764053345) ? " + 
"(b('lon') <= -108.28863525390625) ? " + 
"(b('lon') <= -120.89466857910156) ? " + 
"0.032743282098439616" + 
":  " + 
"-0.027820668674435656" + 
":  " + 
"(b('L8b6med') <= 2588.0) ? " + 
"-0.0018394350099098205" + 
":  " + 
"0.015881802288780885" + 
":  " + 
"(b('lat') <= 32.43104076385498) ? " + 
"(b('gvhmean') <= -13.804054260253906) ? " + 
"-0.0877784202381843" + 
":  " + 
"-0.07137785226905562" + 
":  " + 
"(b('bulk') <= 137.5) ? " + 
"-0.02354218638921619" + 
":  " + 
"-0.0014145015875066747" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('gvhmean') <= -13.529685497283936) ? " + 
"(b('ndvi_med') <= 1933.0) ? " + 
"0.0014521710223442442" + 
":  " + 
"0.022699274076198973" + 
":  " + 
"(b('crops') <= 68.24193572998047) ? " + 
"-0.007554021386808382" + 
":  " + 
"0.018187562359484367" + 
":  " + 
"(b('sand') <= 46.5) ? " + 
"(b('crops') <= 77.1611442565918) ? " + 
"0.0050623599849907615" + 
":  " + 
"-0.06849844803597245" + 
":  " + 
"(b('L8b5med') <= 2593.75) ? " + 
"-0.03479236247936625" + 
":  " + 
"-0.011308407099391335" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 678.0) ? " + 
"(b('lon') <= 22.87806510925293) ? " + 
"(b('lat') <= 39.22870063781738) ? " + 
"-0.02572692285194749" + 
":  " + 
"0.01740573854218705" + 
":  " + 
"(b('lon') <= 22.880224227905273) ? " + 
"0.06463097152121104" + 
":  " + 
"0.025587704176191717" + 
":  " + 
"(b('ndvi_med') <= 4415.0) ? " + 
"(b('L8b3med') <= 845.0) ? " + 
"-0.015655042631082822" + 
":  " + 
"-0.0006871075718223724" + 
":  " + 
"(b('lat') <= 55.933950424194336) ? " + 
"0.02720049649015346" + 
":  " + 
"-0.0017699604848642747" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 41.426435470581055) ? " + 
"(b('sand') <= 60.5) ? " + 
"(b('gvhk2') <= 0.6108855605125427) ? " + 
"-0.0032213730191125883" + 
":  " + 
"-0.0559903528812834" + 
":  " + 
"(b('L8b5med') <= 2540.0) ? " + 
"0.01304338643107938" + 
":  " + 
"-0.03175119210635587" + 
":  " + 
"(b('lat') <= 41.73293495178223) ? " + 
"(b('gvhmean') <= -12.828277111053467) ? " + 
"0.008208449997058304" + 
":  " + 
"0.07618470691007087" + 
":  " + 
"(b('L8b3med') <= 619.0) ? " + 
"0.031362815633735636" + 
":  " + 
"0.0006208926945750255" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('gvhmean') <= -15.657236576080322) ? " + 
"(b('L8b6med') <= 2816.5) ? " + 
"0.077744944394514" + 
":  " + 
"0.01894393186114959" + 
":  " + 
"(b('crops') <= 68.24193572998047) ? " + 
"-0.0018068748019067066" + 
":  " + 
"0.015533660168519916" + 
":  " + 
"(b('gvhk2') <= 0.4412725418806076) ? " + 
"(b('ndvi_med') <= 1690.5) ? " + 
"-0.009785261360178616" + 
":  " + 
"-0.038770053868421736" + 
":  " + 
"(b('crops') <= 77.83634567260742) ? " + 
"0.01870645523907175" + 
":  " + 
"-0.0648100955864102" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 37.80069923400879) ? " + 
"(b('gvhk3') <= -0.01713892910629511) ? " + 
"(b('bulk') <= 154.5) ? " + 
"-0.0625832858485825" + 
":  " + 
"-0.08254698299310205" + 
":  " + 
"(b('grass') <= 91.94809341430664) ? " + 
"-0.009637999674707258" + 
":  " + 
"0.01960262212177065" + 
":  " + 
"(b('L8b5med') <= 2365.25) ? " + 
"(b('sand') <= 74.5) ? " + 
"-0.011104663035133546" + 
":  " + 
"0.01883461365070567" + 
":  " + 
"(b('L8b10med') <= 2940.0) ? " + 
"0.009244104261072871" + 
":  " + 
"-0.02066469112951609" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 678.0) ? " + 
"(b('lon') <= 22.87806510925293) ? " + 
"(b('gvhk3') <= -0.008954548044130206) ? " + 
"0.02707583746321635" + 
":  " + 
"0.002949983711055557" + 
":  " + 
"(b('ndvi_med') <= 3393.0) ? " + 
"0.0553126006244384" + 
":  " + 
"0.019148929249282354" + 
":  " + 
"(b('L8b3med') <= 845.0) ? " + 
"(b('crops') <= 66.47800827026367) ? " + 
"-0.018619799979648143" + 
":  " + 
"0.0075552581893650285" + 
":  " + 
"(b('ndvi_med') <= 1898.25) ? " + 
"-0.004553328872864951" + 
":  " + 
"0.01073741197014457" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('gvvmean') <= -13.529685497283936) ? " + 
"(b('lat') <= -35.25544357299805) ? " + 
"-0.05739869846073871" + 
":  " + 
"0.011561003732114904" + 
":  " + 
"(b('crops') <= 67.3132438659668) ? " + 
"-0.00643263084391328" + 
":  " + 
"0.012266456119593311" + 
":  " + 
"(b('L8b5med') <= 2625.25) ? " + 
"(b('L8b5med') <= 2546.5) ? " + 
"-0.009932963410907738" + 
":  " + 
"-0.034126245395918436" + 
":  " + 
"(b('gvhk3') <= 0.08668017759919167) ? " + 
"-0.005509119234255222" + 
":  " + 
"0.05901368937625005" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.521310806274414) ? " + 
"(b('lon') <= 147.47109985351562) ? " + 
"(b('ndvi_med') <= 1762.5) ? " + 
"-0.010409030130363102" + 
":  " + 
"-0.03186180432071328" + 
":  " + 
"(b('lat') <= -35.233184814453125) ? " + 
"-0.018867311112639784" + 
":  " + 
"0.04232491521300906" + 
":  " + 
"(b('gvhmean') <= -15.623340129852295) ? " + 
"(b('gvvmean') <= -16.183561325073242) ? " + 
"0.003796264050830366" + 
":  " + 
"0.039434534081340185" + 
":  " + 
"(b('gvhk3') <= 0.003098049317486584) ? " + 
"0.005052488609001482" + 
":  " + 
"-0.005289641113896502" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.020603183656930923) ? " + 
"(b('L8b5med') <= 3287.0) ? " + 
"(b('gvvmean') <= -8.632915258407593) ? " + 
"0.022194811898687716" + 
":  " + 
"0.02031295085144391" + 
":  " + 
"0.08441328952197047" + 
":  " + 
"(b('gvhk2') <= 0.11113361269235611) ? " + 
"(b('ndvi_med') <= 3783.5) ? " + 
"-0.030863894112184716" + 
":  " + 
"0.0008629197068730429" + 
":  " + 
"(b('bulk') <= 119.0) ? " + 
"0.016321569689532214" + 
":  " + 
"-0.0006781405247681734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2030.0) ? " + 
"(b('L8b6med') <= 2659.5) ? " + 
"(b('sand') <= 77.5) ? " + 
"-0.00776095712386267" + 
":  " + 
"0.016918913359147667" + 
":  " + 
"(b('gvhmean') <= -10.499673843383789) ? " + 
"0.010365333451430224" + 
":  " + 
"0.06109814997363355" + 
":  " + 
"(b('gvvmean') <= -9.81239652633667) ? " + 
"(b('gvhmean') <= -10.102759838104248) ? " + 
"-0.002197039156143" + 
":  " + 
"0.04941372026363742" + 
":  " + 
"(b('crops') <= 69.84283447265625) ? " + 
"-0.03836044145119528" + 
":  " + 
"-0.0011096825534884641" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 37.80069923400879) ? " + 
"(b('gvhk3') <= -0.01713892910629511) ? " + 
"(b('L8b3med') <= 987.0) ? " + 
"-0.07466765687568036" + 
":  " + 
"-0.048185130214502395" + 
":  " + 
"(b('L8b5med') <= 2263.0) ? " + 
"0.019577428972242142" + 
":  " + 
"-0.00701939963537065" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"(b('grass') <= 70.95670318603516) ? " + 
"0.006646993568113415" + 
":  " + 
"-0.00614587302816316" + 
":  " + 
"(b('gvhk3') <= 0.006865940056741238) ? " + 
"-0.01536486887119961" + 
":  " + 
"-0.03639046505791263" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -13.529685497283936) ? " + 
"(b('ndvi_med') <= 1879.5) ? " + 
"(b('crops') <= 54.728538513183594) ? " + 
"-0.004356605935270721" + 
":  " + 
"0.033428922820468714" + 
":  " + 
"(b('bare') <= 11.245529174804688) ? " + 
"0.010269752122767964" + 
":  " + 
"0.06864167489504107" + 
":  " + 
"(b('gvhk3') <= 0.003098049317486584) ? " + 
"(b('lat') <= 39.34249496459961) ? " + 
"-0.01488450288474743" + 
":  " + 
"0.0070076514721727325" + 
":  " + 
"(b('bare') <= 2.5896307229995728) ? " + 
"-0.004860056793750746" + 
":  " + 
"-0.020668869686810944" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 22.0) ? " + 
"(b('lat') <= 43.56470489501953) ? " + 
"-0.003159905948321412" + 
":  " + 
"(b('ndvi_med') <= 4014.0) ? " + 
"-0.045942624331931275" + 
":  " + 
"-0.05744262528560559" + 
":  " + 
"(b('L8b5med') <= 2436.5) ? " + 
"(b('lon') <= -120.90679931640625) ? " + 
"0.048561284577523116" + 
":  " + 
"-0.006339835443957049" + 
":  " + 
"(b('L8b5med') <= 2453.5) ? " + 
"0.08581671740157039" + 
":  " + 
"0.002053040413138131" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 600.5) ? " + 
"(b('L8b3med') <= 557.5) ? " + 
"(b('bulk') <= 118.0) ? " + 
"0.043075363996901705" + 
":  " + 
"0.04232405888912555" + 
":  " + 
"(b('lon') <= 16.02862024307251) ? " + 
"0.013527086391477594" + 
":  " + 
"0.0218433406561927" + 
":  " + 
"(b('gvhmean') <= -15.623340129852295) ? " + 
"(b('L8b6med') <= 2816.5) ? " + 
"0.06224277543963705" + 
":  " + 
"0.006870416563828132" + 
":  " + 
"(b('gvhk2') <= 0.020603183656930923) ? " + 
"0.04265521096011042" + 
":  " + 
"-0.0019893484025343866" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('gvhmean') <= -15.758374214172363) ? " + 
"-0.022816480205753983" + 
":  " + 
"(b('sand') <= 67.0) ? " + 
"-0.03769578458115311" + 
":  " + 
"-0.04439996160638933" + 
":  " + 
"(b('gvhmean') <= -13.529685497283936) ? " + 
"(b('ndvi_med') <= 1879.5) ? " + 
"-0.0021251766680686177" + 
":  " + 
"0.01474247049554562" + 
":  " + 
"(b('gvhk3') <= 0.003098049317486584) ? " + 
"0.002702942699525278" + 
":  " + 
"-0.008631217513091751" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.521310806274414) ? " + 
"(b('lat') <= -34.90736961364746) ? " + 
"(b('lat') <= -35.25544357299805) ? " + 
"-0.031473667917988925" + 
":  " + 
"0.02027530829144416" + 
":  " + 
"(b('L8b5med') <= 2319.5) ? " + 
"0.005862144655102437" + 
":  " + 
"-0.02206973710572957" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"(b('lon') <= -105.18899917602539) ? " + 
"-0.0022604495476589038" + 
":  " + 
"0.005934638438545808" + 
":  " + 
"(b('L8b6med') <= 2602.25) ? " + 
"-0.012602941762275565" + 
":  " + 
"-0.028542678041055997" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 22.0) ? " + 
"(b('gvhk3') <= 0.03296667221002281) ? " + 
"(b('gvhk2') <= 0.41970019042491913) ? " + 
"-0.04201318517229183" + 
":  " + 
"-0.052363186030598724" + 
":  " + 
"-0.0015558138071607719" + 
":  " + 
"(b('L8b10med') <= 2030.0) ? " + 
"(b('L8b10med') <= 1965.5) ? " + 
"0.0014362884912395343" + 
":  " + 
"0.024570261131212866" + 
":  " + 
"(b('gvhmean') <= -9.81239652633667) ? " + 
"-0.0008591863073494399" + 
":  " + 
"-0.02110398149831349" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 1898.0) ? " + 
"(b('gvhk3') <= -0.05219591804780066) ? " + 
"(b('ndvi_med') <= 4995.5) ? " + 
"0.02309371734090851" + 
":  " + 
"0.010758268371689528" + 
":  " + 
"0.05240376972824626" + 
":  " + 
"(b('L8b5med') <= 2436.5) ? " + 
"(b('lon') <= 9.200799942016602) ? " + 
"-0.004121142934497702" + 
":  " + 
"-0.028865430298633837" + 
":  " + 
"(b('L8b5med') <= 2453.5) ? " + 
"0.07602093077978572" + 
":  " + 
"0.0013590262945097757" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= -0.019478777423501015) ? " + 
"(b('gvhk3') <= -0.02122032456099987) ? " + 
"(b('L8b10med') <= 1698.5) ? " + 
"0.024676748937673517" + 
":  " + 
"-0.006745868141491874" + 
":  " + 
"(b('gvvmean') <= -12.04888916015625) ? " + 
"0.02951453596231718" + 
":  " + 
"0.06805594642856141" + 
":  " + 
"(b('gvhk3') <= -0.01885722018778324) ? " + 
"-0.06604259089445953" + 
":  " + 
"(b('grass') <= 18.52322292327881) ? " + 
"-0.007638652097685684" + 
":  " + 
"0.0014022197116976827" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.020603183656930923) ? " + 
"(b('sand') <= 51.0) ? " + 
"0.06274234436750475" + 
":  " + 
"(b('grass') <= 33.76572322845459) ? " + 
"0.013770080190952994" + 
":  " + 
"0.012519068512069728" + 
":  " + 
"(b('gvhk2') <= 0.11113361269235611) ? " + 
"(b('L8b10med') <= 1988.5) ? " + 
"0.005469661967112946" + 
":  " + 
"-0.022655126440847603" + 
":  " + 
"(b('gvhk2') <= 0.13928855955600739) ? " + 
"0.017469032867283935" + 
":  " + 
"-0.00022203245237355473" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2626.0) ? " + 
"(b('L8b10med') <= 2586.5) ? " + 
"(b('L8b3med') <= 1133.0) ? " + 
"-0.004015676846851641" + 
":  " + 
"0.01299670013522015" + 
":  " + 
"(b('bare') <= 5.713076591491699) ? " + 
"-0.008429352811881726" + 
":  " + 
"-0.026288444689162006" + 
":  " + 
"(b('gvhmean') <= -15.623340129852295) ? " + 
"(b('L8b5med') <= 2699.25) ? " + 
"0.06995402151101575" + 
":  " + 
"0.014324807890544966" + 
":  " + 
"(b('L8b5med') <= 2651.25) ? " + 
"0.0243959296181199" + 
":  " + 
"0.0001642246722434236" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 600.5) ? " + 
"(b('L8b3med') <= 557.5) ? " + 
"(b('gvhk3') <= -0.015091527486220002) ? " + 
"0.03490445944398618" + 
":  " + 
"0.036704134183980275" + 
":  " + 
"(b('lat') <= 54.79445457458496) ? " + 
"0.017595313177342142" + 
":  " + 
"0.011470082463306323" + 
":  " + 
"(b('L8b5med') <= 2626.0) ? " + 
"(b('bulk') <= 132.5) ? " + 
"-0.013955601323488387" + 
":  " + 
"-0.0006588196944255272" + 
":  " + 
"(b('L8b5med') <= 2694.5) ? " + 
"0.0178360970999196" + 
":  " + 
"0.0007224692208192406" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 1898.0) ? " + 
"(b('L8b3med') <= 723.5) ? " + 
"(b('gvhk2') <= 0.797989010810852) ? " + 
"0.02170713262927995" + 
":  " + 
"0.009633791032261668" + 
":  " + 
"0.04751282368361692" + 
":  " + 
"(b('gvvmean') <= -13.529685497283936) ? " + 
"(b('crops') <= 6.391192436218262) ? " + 
"-0.00012574264000364253" + 
":  " + 
"0.013449650013332778" + 
":  " + 
"(b('gvhmean') <= -13.478110313415527) ? " + 
"-0.04221982214728914" + 
":  " + 
"-0.002017614092407687" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.521310806274414) ? " + 
"(b('gvhk3') <= 0.01707080751657486) ? " + 
"(b('lat') <= 32.43484020233154) ? " + 
"-0.044945572881713046" + 
":  " + 
"-0.00823328213034529" + 
":  " + 
"(b('ndvi_med') <= 1543.5) ? " + 
"-0.03319628977482525" + 
":  " + 
"0.003784634244686409" + 
":  " + 
"(b('gvhmean') <= -15.623340129852295) ? " + 
"(b('gvhmean') <= -16.183561325073242) ? " + 
"0.0020437402777709426" + 
":  " + 
"0.027400452381750963" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"0.0006942718249240619" + 
":  " + 
"-0.01781655439284762" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 22.0) ? " + 
"(b('gvvmean') <= -11.79568862915039) ? " + 
"-0.0016104889443859793" + 
":  " + 
"(b('ndvi_med') <= 4014.0) ? " + 
"-0.03711803599206559" + 
":  " + 
"-0.0464330367645418" + 
":  " + 
"(b('crops') <= 67.3132438659668) ? " + 
"(b('grass') <= 21.1055850982666) ? " + 
"-0.014879179262085434" + 
":  " + 
"0.0009060657917555942" + 
":  " + 
"(b('bare') <= 5.524640083312988) ? " + 
"0.01042297044133975" + 
":  " + 
"-0.05425464122430876" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('sand') <= 63.0) ? " + 
"-0.017103146607041236" + 
":  " + 
"-0.031664972097214306" + 
":  " + 
"(b('gvhk3') <= -0.019478777423501015) ? " + 
"(b('gvhk3') <= -0.02122032456099987) ? " + 
"0.00518108012911878" + 
":  " + 
"0.04813144815091455" + 
":  " + 
"(b('gvhmean') <= -14.541287422180176) ? " + 
"0.005935839119587953" + 
":  " + 
"-0.002362740789972317" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 153.5) ? " + 
"(b('sand') <= 22.0) ? " + 
"(b('gvhk3') <= -0.005964890122413635) ? " + 
"-0.04155345900909038" + 
":  " + 
"-0.0331699583138618" + 
":  " + 
"(b('L8b5med') <= 2436.5) ? " + 
"-0.003580129990630542" + 
":  " + 
"0.0036158578907688715" + 
":  " + 
"(b('L8b10med') <= 1841.0) ? " + 
"-0.054650456373590325" + 
":  " + 
"(b('gvhk2') <= 0.23666847497224808) ? " + 
"-0.01548352433111375" + 
":  " + 
"-0.002679311705469597" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('L8b10med') <= 2525.25) ? " + 
"(b('bulk') <= 133.5) ? " + 
"-0.0033848569462109897" + 
":  " + 
"0.004403180079678841" + 
":  " + 
"(b('gvvmean') <= -11.941969394683838) ? " + 
"0.09754529962387648" + 
":  " + 
"0.0083142683515042" + 
":  " + 
"(b('gvhk2') <= 0.2062721624970436) ? " + 
"(b('ndvi_med') <= 1241.75) ? " + 
"-0.0034454304892809896" + 
":  " + 
"0.045196412373593335" + 
":  " + 
"(b('grass') <= 14.918523788452148) ? " + 
"-0.024974110536304182" + 
":  " + 
"-0.004967686666755983" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2030.0) ? " + 
"(b('L8b10med') <= 2011.5) ? " + 
"(b('L8b6med') <= 2793.5) ? " + 
"-0.0010460159798026513" + 
":  " + 
"0.012735284915180441" + 
":  " + 
"(b('gvhk3') <= 0.022151708602905273) ? " + 
"0.04174343507301001" + 
":  " + 
"0.06588085547549263" + 
":  " + 
"(b('gvvmean') <= -9.81239652633667) ? " + 
"(b('L8b10med') <= 2056.5) ? " + 
"-0.01867119772751301" + 
":  " + 
"0.00011439561898236419" + 
":  " + 
"(b('gvhk2') <= 0.39091283082962036) ? " + 
"-0.0331865651616887" + 
":  " + 
"-0.006682456010013664" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 1898.0) ? " + 
"(b('bare') <= 0.2461538463830948) ? " + 
"(b('L8b5med') <= 1720.0) ? " + 
"0.018404553155102907" + 
":  " + 
"0.008405323984182783" + 
":  " + 
"0.04363888192424892" + 
":  " + 
"(b('L8b5med') <= 2626.0) ? " + 
"(b('grass') <= 15.331648826599121) ? " + 
"-0.018903597044928604" + 
":  " + 
"-0.0014564024189744863" + 
":  " + 
"(b('L8b10med') <= 1429.75) ? " + 
"-0.01288238571519889" + 
":  " + 
"0.004069307141608937" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"(b('gvhk3') <= -0.015091527486220002) ? " + 
"0.0311647748796704" + 
":  " + 
"0.03199213782700011" + 
":  " + 
"(b('gvhk2') <= 0.020603183656930923) ? " + 
"(b('bulk') <= 133.5) ? " + 
"0.05495388296788334" + 
":  " + 
"0.01086862119703147" + 
":  " + 
"(b('gvhk2') <= 0.11113361269235611) ? " + 
"-0.016024258399445688" + 
":  " + 
"0.00024279191166601694" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('L8b10med') <= 2525.25) ? " + 
"(b('crops') <= 67.3132438659668) ? " + 
"-0.0005960205039359619" + 
":  " + 
"0.008886423022517853" + 
":  " + 
"(b('gvhmean') <= -11.941969394683838) ? " + 
"0.08790069115032145" + 
":  " + 
"0.006663272329903158" + 
":  " + 
"(b('lat') <= 41.222354888916016) ? " + 
"(b('lat') <= 37.80069923400879) ? " + 
"-0.006432791035740855" + 
":  " + 
"0.0148956012017678" + 
":  " + 
"(b('grass') <= 1.7143399715423584) ? " + 
"0.03572984213454368" + 
":  " + 
"-0.020873972305339137" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 153.5) ? " + 
"(b('bulk') <= 152.5) ? " + 
"(b('L8b10med') <= 2545.5) ? " + 
"0.001939806875556274" + 
":  " + 
"-0.005761440484181994" + 
":  " + 
"(b('crops') <= 9.99725717306137) ? " + 
"-0.017732805717451214" + 
":  " + 
"0.03431119696907918" + 
":  " + 
"(b('L8b10med') <= 1841.0) ? " + 
"-0.05071829413459277" + 
":  " + 
"(b('gvhk2') <= 0.23666847497224808) ? " + 
"-0.013496106804228209" + 
":  " + 
"-0.002441506357846559" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= -0.014465656131505966) ? " + 
"(b('grass') <= 60.0) ? " + 
"(b('lat') <= 55.94179916381836) ? " + 
"0.024888434715139966" + 
":  " + 
"-0.0025136760243366523" + 
":  " + 
"(b('bare') <= 3.7610509395599365) ? " + 
"-0.0388076384609275" + 
":  " + 
"0.0022669494881262103" + 
":  " + 
"(b('bulk') <= 132.5) ? " + 
"(b('L8b6med') <= 2517.75) ? " + 
"-0.01887668243199518" + 
":  " + 
"0.00046383862399853167" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"0.006570147181942196" + 
":  " + 
"-0.0024651781758096855" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 99.8344841003418) ? " + 
"(b('grass') <= 70.92141723632812) ? " + 
"(b('bulk') <= 145.5) ? " + 
"0.003550030249919744" + 
":  " + 
"-0.004758125629617757" + 
":  " + 
"(b('bulk') <= 132.5) ? " + 
"-0.024274492302449956" + 
":  " + 
"-0.002769654850174917" + 
":  " + 
"(b('lon') <= -101.27885055541992) ? " + 
"(b('lon') <= -106.41360092163086) ? " + 
"0.0010905113890328291" + 
":  " + 
"0.014409622800057479" + 
":  " + 
"0.03729426723653295" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 600.5) ? " + 
"(b('L8b3med') <= 557.5) ? " + 
"0.02803372092586462" + 
":  " + 
"(b('sand') <= 61.5) ? " + 
"0.014234154205305327" + 
":  " + 
"0.008750817330433432" + 
":  " + 
"(b('L8b3med') <= 845.0) ? " + 
"(b('L8b10med') <= 1722.0) ? " + 
"-0.00032881501881472635" + 
":  " + 
"-0.01818071029138246" + 
":  " + 
"(b('sand') <= 27.5) ? " + 
"0.023878670779868275" + 
":  " + 
"0.0004884867434563106" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 25.16578960418701) ? " + 
"(b('lat') <= 32.43104076385498) ? " + 
"(b('lat') <= 26.839200019836426) ? " + 
"-0.012664902090048669" + 
":  " + 
"-0.042784987377128256" + 
":  " + 
"(b('lon') <= -105.18899917602539) ? " + 
"-0.001751288044175213" + 
":  " + 
"0.0038306266685964115" + 
":  " + 
"(b('L8b10med') <= 2926.5) ? " + 
"(b('grass') <= 46.57049369812012) ? " + 
"-0.01921360317856247" + 
":  " + 
"0.0012235454862352375" + 
":  " + 
"0.04025001574103912" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('gvhmean') <= -15.758374214172363) ? " + 
"-0.013576024348284199" + 
":  " + 
"-0.026878543718146054" + 
":  " + 
"(b('gvvmean') <= -13.529685497283936) ? " + 
"(b('lon') <= -105.18899917602539) ? " + 
"-0.0009013932280806875" + 
":  " + 
"0.009720042058587246" + 
":  " + 
"(b('gvhk3') <= 0.003098049317486584) ? " + 
"0.002578987132285177" + 
":  " + 
"-0.006502485754738099" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 133.5) ? " + 
"(b('gvhk3') <= 0.0011666404316201806) ? " + 
"(b('sand') <= 24.5) ? " + 
"-0.03207652877218037" + 
":  " + 
"0.0044839492315202865" + 
":  " + 
"(b('lon') <= -120.29602432250977) ? " + 
"0.03838618101026005" + 
":  " + 
"-0.01130973358567329" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"(b('crops') <= 68.06966018676758) ? " + 
"0.0060830945486961534" + 
":  " + 
"0.03783393678139798" + 
":  " + 
"(b('gvhk2') <= 0.4449174553155899) ? " + 
"-0.003974661418410824" + 
":  " + 
"0.005629399053256715" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 76.5) ? " + 
"(b('L8b6med') <= 2563.75) ? " + 
"(b('bulk') <= 132.5) ? " + 
"-0.020279813806920913" + 
":  " + 
"0.003101940178964235" + 
":  " + 
"(b('L8b10med') <= 2030.0) ? " + 
"0.007567872277113151" + 
":  " + 
"-0.001000733124334153" + 
":  " + 
"(b('lon') <= -36.25764846801758) ? " + 
"-0.03207790618236772" + 
":  " + 
"(b('gvhk3') <= -0.005376655142754316) ? " + 
"0.015192424786596524" + 
":  " + 
"0.005286300449173428" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.020603183656930923) ? " + 
"(b('L8b5med') <= 3287.0) ? " + 
"(b('bare') <= 23.074840545654297) ? " + 
"0.0072073290547853275" + 
":  " + 
"0.009510682721103197" + 
":  " + 
"0.04702773694124404" + 
":  " + 
"(b('gvhk2') <= 0.11013723909854889) ? " + 
"(b('lat') <= 37.16975021362305) ? " + 
"-0.032139547875756985" + 
":  " + 
"-0.011434389187041285" + 
":  " + 
"(b('gvhk2') <= 0.15307045727968216) ? " + 
"0.011864715468714418" + 
":  " + 
"-0.00041561035981246727" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 1927.0) ? " + 
"(b('L8b3med') <= 761.0) ? " + 
"(b('gvvmean') <= -4.673092842102051) ? " + 
"0.00901772555891231" + 
":  " + 
"0.016254444430966186" + 
":  " + 
"0.03796937035832196" + 
":  " + 
"(b('L8b6med') <= 2241.0) ? " + 
"(b('L8b6med') <= 2133.75) ? " + 
"0.004045429353970698" + 
":  " + 
"-0.027807435231324788" + 
":  " + 
"(b('L8b10med') <= 2030.0) ? " + 
"0.003380281293459178" + 
":  " + 
"-0.0016515044186657714" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 11.910642623901367) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('lon') <= -108.28863525390625) ? " + 
"-0.010105399531477694" + 
":  " + 
"0.002838083083916628" + 
":  " + 
"(b('lon') <= -118.33930969238281) ? " + 
"0.0046316552046643" + 
":  " + 
"-0.01366824515757038" + 
":  " + 
"(b('ndvi_med') <= 2128.0) ? " + 
"(b('lon') <= -115.53868103027344) ? " + 
"-0.004465193422891333" + 
":  " + 
"0.009533280346494711" + 
":  " + 
"(b('gvhmean') <= -12.980433940887451) ? " + 
"0.06832758448436557" + 
":  " + 
"-0.0038595522037398328" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -15.623340129852295) ? " + 
"(b('gvhmean') <= -16.178815841674805) ? " + 
"(b('lon') <= -105.89213562011719) ? " + 
"-0.005972343949735081" + 
":  " + 
"0.008412642871405925" + 
":  " + 
"(b('sand') <= 56.5) ? " + 
"0.02550147196181098" + 
":  " + 
"-0.015528923666123975" + 
":  " + 
"(b('gvhk3') <= 0.003098049317486584) ? " + 
"(b('grass') <= 79.0247802734375) ? " + 
"0.0030713688813638813" + 
":  " + 
"-0.011117809752485096" + 
":  " + 
"(b('L8b5med') <= 3021.0) ? " + 
"-0.0009840743206460908" + 
":  " + 
"-0.015347152798913773" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 25.16578960418701) ? " + 
"(b('lat') <= 32.43104076385498) ? " + 
"(b('lon') <= -100.43519973754883) ? " + 
"-0.044603800590476035" + 
":  " + 
"-0.018835653946174327" + 
":  " + 
"(b('bulk') <= 132.5) ? " + 
"-0.002732171843514077" + 
":  " + 
"0.002345219081379729" + 
":  " + 
"(b('L8b10med') <= 2926.5) ? " + 
"(b('gvhk2') <= 0.4787442237138748) ? " + 
"-0.005464490696046449" + 
":  " + 
"-0.030973162270453738" + 
":  " + 
"0.034811453969705" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2061.5) ? " + 
"(b('bare') <= 0.2461538463830948) ? " + 
"(b('grass') <= 77.19597625732422) ? " + 
"0.007440911502315477" + 
":  " + 
"-0.02297655825297676" + 
":  " + 
"(b('lon') <= -118.16548538208008) ? " + 
"0.03342843059155359" + 
":  " + 
"0.02006329509089142" + 
":  " + 
"(b('L8b5med') <= 2436.5) ? " + 
"(b('sand') <= 74.5) ? " + 
"-0.0063283193169668545" + 
":  " + 
"0.01358530941840559" + 
":  " + 
"(b('L8b5med') <= 2453.5) ? " + 
"0.051000925726265134" + 
":  " + 
"0.0005603601715678902" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 137.5) ? " + 
"(b('bare') <= 1.2342107892036438) ? " + 
"(b('bare') <= 0.955679714679718) ? " + 
"0.00034205323056279687" + 
":  " + 
"0.0610525956814941" + 
":  " + 
"(b('bare') <= 5.14908766746521) ? " + 
"-0.020374883501446124" + 
":  " + 
"-0.006110123732923283" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"(b('grass') <= 49.423410415649414) ? " + 
"0.0248093502679225" + 
":  " + 
"0.0035052585279986208" + 
":  " + 
"(b('gvhk2') <= 0.4449174553155899) ? " + 
"-0.0035429018597260523" + 
":  " + 
"0.005252802383596403" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 845.0) ? " + 
"(b('L8b10med') <= 1722.0) ? " + 
"(b('L8b6med') <= 2815.5) ? " + 
"-0.00093280126007733" + 
":  " + 
"0.02677732741939122" + 
":  " + 
"(b('grass') <= 13.302776336669922) ? " + 
"0.012304298008592706" + 
":  " + 
"-0.02297522741749597" + 
":  " + 
"(b('L8b3med') <= 866.5) ? " + 
"(b('bare') <= 0.6858288645744324) ? " + 
"0.012187677963908794" + 
":  " + 
"0.04890745515454592" + 
":  " + 
"(b('sand') <= 27.5) ? " + 
"0.017833536175721882" + 
":  " + 
"-0.00020569950686532456" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1429.75) ? " + 
"(b('L8b5med') <= 3093.0) ? " + 
"(b('sand') <= 45.5) ? " + 
"-0.019285917410514497" + 
":  " + 
"0.005432930294382017" + 
":  " + 
"(b('L8b10med') <= 1349.0) ? " + 
"-0.04389823837945844" + 
":  " + 
"-0.023318986498413935" + 
":  " + 
"(b('L8b10med') <= 1622.5) ? " + 
"(b('bulk') <= 132.5) ? " + 
"0.0026870691885064646" + 
":  " + 
"0.022478362414440012" + 
":  " + 
"(b('L8b3med') <= 761.5) ? " + 
"-0.01613290984985006" + 
":  " + 
"0.00041038407325516384" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"(b('gvvmean') <= -13.215603828430176) ? " + 
"0.023998586766901087" + 
":  " + 
"0.02124386310831189" + 
":  " + 
"(b('L8b10med') <= 1429.75) ? " + 
"(b('L8b5med') <= 3093.0) ? " + 
"-0.0006500370448287569" + 
":  " + 
"-0.024073975630729213" + 
":  " + 
"(b('lat') <= 55.97799873352051) ? " + 
"0.0009206897136510723" + 
":  " + 
"-0.010316163469007768" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('L8b3med') <= 963.0) ? " + 
"-0.00951292111269636" + 
":  " + 
"(b('L8b10med') <= 2621.25) ? " + 
"-0.022451597499403675" + 
":  " + 
"-0.02312240309509521" + 
":  " + 
"(b('gvvmean') <= -14.541287422180176) ? " + 
"(b('ndvi_med') <= 1948.25) ? " + 
"-0.0014445807300551227" + 
":  " + 
"0.01433224514840839" + 
":  " + 
"(b('gvhk3') <= 0.003098049317486584) ? " + 
"0.002051160239139676" + 
":  " + 
"-0.00388146765369029" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2061.5) ? " + 
"(b('bare') <= 0.2461538463830948) ? " + 
"(b('grass') <= 77.19597625732422) ? " + 
"0.007182351020763859" + 
":  " + 
"-0.01932816450225178" + 
":  " + 
"(b('L8b6med') <= 2704.75) ? " + 
"0.029312434554098928" + 
":  " + 
"0.018093602315856806" + 
":  " + 
"(b('L8b5med') <= 2436.5) ? " + 
"(b('sand') <= 74.5) ? " + 
"-0.005316450724789913" + 
":  " + 
"0.01126543644655552" + 
":  " + 
"(b('L8b5med') <= 2453.5) ? " + 
"0.043905803035847304" + 
":  " + 
"0.00039942959200851727" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 3352.25) ? " + 
"(b('L8b10med') <= 3011.25) ? " + 
"(b('L8b6med') <= 3707.0) ? " + 
"0.0008040800817334454" + 
":  " + 
"-0.0075461836831177" + 
":  " + 
"(b('lat') <= 40.38764572143555) ? " + 
"-0.0050784911386902686" + 
":  " + 
"-0.02728939191667662" + 
":  " + 
"(b('lat') <= 35.51546859741211) ? " + 
"(b('L8b10med') <= 3781.75) ? " + 
"0.0022639485743739737" + 
":  " + 
"-0.0069541186290386255" + 
":  " + 
"(b('bare') <= 16.12496042251587) ? " + 
"0.015301543962478376" + 
":  " + 
"0.02731335616208822" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.031004308681869104" + 
":  " + 
"(b('bare') <= 11.910642623901367) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.0010104220756055255" + 
":  " + 
"-0.005776111916172411" + 
":  " + 
"(b('ndvi_med') <= 2128.0) ? " + 
"0.0020319850657185517" + 
":  " + 
"0.03793114338711325" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 99.8344841003418) ? " + 
"(b('L8b10med') <= 2030.0) ? " + 
"(b('L8b10med') <= 2011.5) ? " + 
"0.0011086546459912628" + 
":  " + 
"0.03849745269295196" + 
":  " + 
"(b('ndvi_med') <= 1716.0) ? " + 
"0.0013657545359102516" + 
":  " + 
"-0.006457103817807495" + 
":  " + 
"(b('L8b5med') <= 2637.5) ? " + 
"(b('bulk') <= 142.5) ? " + 
"-0.00319743977999469" + 
":  " + 
"0.008050942876328118" + 
":  " + 
"0.02648782106476441" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.020603183656930923) ? " + 
"(b('L8b6med') <= 3017.0) ? " + 
"(b('L8b3med') <= 1133.5) ? " + 
"0.0018548652964967272" + 
":  " + 
"0.008150101226234913" + 
":  " + 
"0.0409290536739321" + 
":  " + 
"(b('gvhk2') <= 0.11113361269235611) ? " + 
"(b('L8b10med') <= 2042.5) ? " + 
"-0.0017585616537818816" + 
":  " + 
"-0.014524115711496633" + 
":  " + 
"(b('gvhk2') <= 0.2062721624970436) ? " + 
"0.006080332303113064" + 
":  " + 
"-0.0007281679159267203" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1429.75) ? " + 
"(b('L8b5med') <= 3093.0) ? " + 
"(b('sand') <= 45.5) ? " + 
"-0.017531394244684806" + 
":  " + 
"0.004170329092712697" + 
":  " + 
"(b('L8b10med') <= 1349.0) ? " + 
"-0.03697231206101184" + 
":  " + 
"-0.01880694304164156" + 
":  " + 
"(b('L8b10med') <= 1622.5) ? " + 
"(b('bulk') <= 132.5) ? " + 
"0.0018833129705680192" + 
":  " + 
"0.01967082254933759" + 
":  " + 
"(b('L8b3med') <= 761.5) ? " + 
"-0.013958302420999734" + 
":  " + 
"0.00039476314035482776" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('L8b10med') <= 2523.5) ? " + 
"(b('L8b3med') <= 845.0) ? " + 
"-0.0025692475276087837" + 
":  " + 
"0.002517613738762731" + 
":  " + 
"(b('bare') <= 17.45813751220703) ? " + 
"0.008992076449541886" + 
":  " + 
"0.06139150807542146" + 
":  " + 
"(b('lat') <= 41.222354888916016) ? " + 
"(b('lat') <= 41.17720985412598) ? " + 
"-0.00031680717681722086" + 
":  " + 
"0.05280104985259282" + 
":  " + 
"(b('grass') <= 1.7143399715423584) ? " + 
"0.032385791127587986" + 
":  " + 
"-0.016543314685966436" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"(b('sand') <= 65.0) ? " + 
"0.021796026463342832" + 
":  " + 
"0.018494810769115133" + 
":  " + 
"(b('L8b10med') <= 1429.75) ? " + 
"(b('L8b5med') <= 3093.0) ? " + 
"-0.0008617285867234388" + 
":  " + 
"-0.019394129337622076" + 
":  " + 
"(b('L8b5med') <= 2626.0) ? " + 
"-0.0018383380855419415" + 
":  " + 
"0.002625986669553403" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2061.5) ? " + 
"(b('L8b3med') <= 927.5) ? " + 
"(b('L8b5med') <= 1927.0) ? " + 
"0.012344780550065697" + 
":  " + 
"-0.009775679008272198" + 
":  " + 
"(b('grass') <= 65.95267486572266) ? " + 
"0.015148623006266036" + 
":  " + 
"0.025896953913886397" + 
":  " + 
"(b('gvhmean') <= -13.568512916564941) ? " + 
"(b('L8b3med') <= 912.5) ? " + 
"0.010408883509128514" + 
":  " + 
"-2.433897578489715e-05" + 
":  " + 
"(b('L8b5med') <= 4002.25) ? " + 
"-0.002044282742854755" + 
":  " + 
"0.03628231195167175" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('gvhmean') <= -15.758374214172363) ? " + 
"-0.007050996516724001" + 
":  " + 
"-0.019585821304110303" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"(b('L8b6med') <= 3622.25) ? " + 
"0.00526741978900417" + 
":  " + 
"0.026242412940775076" + 
":  " + 
"(b('lat') <= -34.72389030456543) ? " + 
"-0.030249396025550587" + 
":  " + 
"0.00011476445000774807" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 99.8344841003418) ? " + 
"(b('bulk') <= 141.5) ? " + 
"(b('bulk') <= 138.5) ? " + 
"-0.0012598233866248647" + 
":  " + 
"0.012588422639801944" + 
":  " + 
"(b('L8b3med') <= 887.0) ? " + 
"0.009770025091245997" + 
":  " + 
"-0.003353821361567978" + 
":  " + 
"(b('L8b5med') <= 2637.5) ? " + 
"(b('L8b3med') <= 1200.5) ? " + 
"0.005103294796230044" + 
":  " + 
"0.01591055888660134" + 
":  " + 
"0.023348976847591296" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 3352.25) ? " + 
"(b('L8b10med') <= 3011.25) ? " + 
"(b('crops') <= 67.3132438659668) ? " + 
"-0.0006757686607358762" + 
":  " + 
"0.004231089972367133" + 
":  " + 
"(b('lon') <= -5.404855012893677) ? " + 
"-0.011080611922441223" + 
":  " + 
"-0.0414238835176918" + 
":  " + 
"(b('lat') <= 35.51546859741211) ? " + 
"(b('L8b6med') <= 4297.25) ? " + 
"0.0015871140511932863" + 
":  " + 
"-0.006120346230453051" + 
":  " + 
"(b('bare') <= 16.12496042251587) ? " + 
"0.013560377723085756" + 
":  " + 
"0.02382482159863529" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 4757.25) ? " + 
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 41.426435470581055) ? " + 
"-0.0014431594210808148" + 
":  " + 
"0.012432039887262498" + 
":  " + 
"(b('L8b10med') <= 1622.5) ? " + 
"0.003197591216196473" + 
":  " + 
"-0.006087717292317697" + 
":  " + 
"(b('ndvi_med') <= 5188.0) ? " + 
"(b('gvvmean') <= -10.409653186798096) ? " + 
"0.016332015083281907" + 
":  " + 
"0.027273539212390077" + 
":  " + 
"(b('gvhk3') <= -0.0014241323806345463) ? " + 
"0.008455484811856975" + 
":  " + 
"-0.011248606085077717" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -15.623340129852295) ? " + 
"(b('gvhmean') <= -16.178815841674805) ? " + 
"(b('ndvi_med') <= 1410.5) ? " + 
"-0.011659571217635653" + 
":  " + 
"0.0007592181860663412" + 
":  " + 
"(b('bare') <= 8.043295860290527) ? " + 
"0.009804743795303699" + 
":  " + 
"0.05415125905738494" + 
":  " + 
"(b('gvhmean') <= -15.526941776275635) ? " + 
"(b('lat') <= 46.884769439697266) ? " + 
"-0.019404226481147317" + 
":  " + 
"0.006015721771186838" + 
":  " + 
"(b('ndvi_med') <= 4757.25) ? " + 
"-0.0007015898633154741" + 
":  " + 
"0.006071363326072344" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.025885059815526405" + 
":  " + 
"(b('bare') <= 11.910642623901367) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.0008855685415440722" + 
":  " + 
"-0.004839608076427141" + 
":  " + 
"(b('ndvi_med') <= 1362.5) ? " + 
"-0.0024377945187671764" + 
":  " + 
"0.01156060934331797" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"(b('gvhk3') <= -0.015091527486220002) ? " + 
"0.016693683736781928" + 
":  " + 
"0.018419461236388546" + 
":  " + 
"(b('L8b3med') <= 761.5) ? " + 
"(b('L8b6med') <= 2794.0) ? " + 
"-0.0053476844939498456" + 
":  " + 
"0.01812597189480343" + 
":  " + 
"(b('ndvi_med') <= 4153.25) ? " + 
"-0.00034154400985708113" + 
":  " + 
"0.009182367590955502" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2061.5) ? " + 
"(b('bare') <= 0.2461538463830948) ? " + 
"(b('grass') <= 77.19597625732422) ? " + 
"0.0064791359407251874" + 
":  " + 
"-0.016216273052061952" + 
":  " + 
"(b('lat') <= 44.184736251831055) ? " + 
"0.015066555655854802" + 
":  " + 
"0.025094893271927113" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"(b('gvhk3') <= -0.004809212172403932) ? " + 
"0.003922338612718177" + 
":  " + 
"-0.006553589086067926" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"0.006219646805459384" + 
":  " + 
"-0.0014243333692932941" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 3352.25) ? " + 
"(b('L8b10med') <= 3011.25) ? " + 
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"-0.0016745007716758844" + 
":  " + 
"0.0019476231718594647" + 
":  " + 
"(b('sand') <= 42.5) ? " + 
"0.00406781913778792" + 
":  " + 
"-0.017552320053119203" + 
":  " + 
"(b('L8b3med') <= 2152.0) ? " + 
"(b('gvvmean') <= -12.147471904754639) ? " + 
"0.02130023272595614" + 
":  " + 
"0.012370347789732547" + 
":  " + 
"(b('gvhk3') <= -7.714841922279447e-05) ? " + 
"-0.004873469489176364" + 
":  " + 
"0.002063244764305333" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 41.426435470581055) ? " + 
"(b('lat') <= 41.30295944213867) ? " + 
"-9.116873084989625e-05" + 
":  " + 
"-0.016457263730887968" + 
":  " + 
"(b('L8b10med') <= 2107.0) ? " + 
"0.022295081185297085" + 
":  " + 
"-0.0012920236808076765" + 
":  " + 
"(b('lat') <= 43.663949966430664) ? " + 
"(b('ndvi_med') <= 2620.0) ? " + 
"-0.02720931980779081" + 
":  " + 
"-0.03889016977009014" + 
":  " + 
"(b('L8b10med') <= 2024.0) ? " + 
"0.001532240161067095" + 
":  " + 
"-0.00639213880797602" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 99.8344841003418) ? " + 
"(b('gvhk3') <= 0.027968889102339745) ? " + 
"(b('gvhk3') <= 0.023529446683824062) ? " + 
"-0.00022350498919266693" + 
":  " + 
"0.02043048296827343" + 
":  " + 
"(b('gvhk3') <= 0.029254012741148472) ? " + 
"-0.04300358673287191" + 
":  " + 
"-0.002146760473232422" + 
":  " + 
"(b('gvhk2') <= 0.5329283177852631) ? " + 
"(b('ndvi_med') <= 1373.75) ? " + 
"-0.0026085592759981374" + 
":  " + 
"0.0056340451583065075" + 
":  " + 
"(b('bulk') <= 152.0) ? " + 
"0.017325911631628638" + 
":  " + 
"0.0075913566014050304" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2374.0) ? " + 
"(b('grass') <= 83.7240104675293) ? " + 
"(b('sand') <= 76.5) ? " + 
"-0.011735286811347466" + 
":  " + 
"0.003059441897900081" + 
":  " + 
"(b('L8b5med') <= 1955.25) ? " + 
"0.02104421613920754" + 
":  " + 
"0.022134346074474953" + 
":  " + 
"(b('L8b6med') <= 2405.5) ? " + 
"(b('lat') <= 42.658050537109375) ? " + 
"0.046863365267001245" + 
":  " + 
"0.009276939983631065" + 
":  " + 
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"-0.0018701380870733972" + 
":  " + 
"0.0020868554189293494" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 41.5) ? " + 
"(b('bare') <= 25.768656730651855) ? " + 
"(b('ndvi_med') <= 4314.0) ? " + 
"-0.002897388803782491" + 
":  " + 
"0.016035568867448058" + 
":  " + 
"(b('gvvmean') <= -11.55178689956665) ? " + 
"0.06221439748050232" + 
":  " + 
"0.006314040595219658" + 
":  " + 
"(b('sand') <= 46.5) ? " + 
"(b('lon') <= -5.394804954528809) ? " + 
"0.009222481596017712" + 
":  " + 
"-0.026981877193182888" + 
":  " + 
"(b('L8b10med') <= 2180.0) ? " + 
"0.0025239861491700684" + 
":  " + 
"-0.0035175772064759197" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 997.5) ? " + 
"(b('L8b3med') <= 979.0) ? " + 
"(b('bare') <= 11.304055213928223) ? " + 
"-0.0011372772783904287" + 
":  " + 
"0.016919820175108288" + 
":  " + 
"(b('lat') <= 45.85979080200195) ? " + 
"-0.028831631839904438" + 
":  " + 
"0.018529189152659248" + 
":  " + 
"(b('gvhk3') <= 0.08321710303425789) ? " + 
"(b('L8b6med') <= 3130.75) ? " + 
"0.006513907581657578" + 
":  " + 
"-0.0011384174615186582" + 
":  " + 
"(b('gvhk3') <= 0.0928984247148037) ? " + 
"0.017284358166485603" + 
":  " + 
"0.03301577591306988" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 4160.75) ? " + 
"(b('L8b6med') <= 3707.0) ? " + 
"(b('L8b6med') <= 3683.25) ? " + 
"-7.484460538778625e-05" + 
":  " + 
"0.027741462798973476" + 
":  " + 
"(b('crops') <= 77.41878509521484) ? " + 
"-0.001945780359580658" + 
":  " + 
"-0.026453329318631626" + 
":  " + 
"(b('lon') <= -113.27935028076172) ? " + 
"(b('L8b5med') <= 3060.0) ? " + 
"0.009915859761478338" + 
":  " + 
"-0.0023312367432903464" + 
":  " + 
"(b('L8b5med') <= 3581.0) ? " + 
"0.023095060785234225" + 
":  " + 
"0.031396399475214914" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 67.3132438659668) ? " + 
"(b('gvhmean') <= -10.222922801971436) ? " + 
"(b('gvhk2') <= 0.1062636561691761) ? " + 
"-0.009710345247018169" + 
":  " + 
"0.000835066426620355" + 
":  " + 
"(b('gvhk2') <= 0.020603183656930923) ? " + 
"0.01275698508130331" + 
":  " + 
"-0.011797881535494418" + 
":  " + 
"(b('crops') <= 77.41421890258789) ? " + 
"(b('sand') <= 70.0) ? " + 
"0.02425542243397009" + 
":  " + 
"0.001662679474835634" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"-0.01714475687768881" + 
":  " + 
"0.0030186468497919255" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 584.5) ? " + 
"(b('L8b3med') <= 557.5) ? " + 
"(b('crops') <= 28.8680477142334) ? " + 
"0.013883067056364273" + 
":  " + 
"0.017241771320842647" + 
":  " + 
"(b('lon') <= 16.02862024307251) ? " + 
"0.004736822708608909" + 
":  " + 
"0.010965814389800987" + 
":  " + 
"(b('lat') <= 55.93754959106445) ? " + 
"(b('gvhk3') <= -0.019478777423501015) ? " + 
"0.008881427722698948" + 
":  " + 
"-0.00015566356545514799" + 
":  " + 
"(b('sand') <= 74.5) ? " + 
"-0.014245848007364375" + 
":  " + 
"0.0012711617117890858" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 3352.25) ? " + 
"(b('L8b10med') <= 3011.25) ? " + 
"(b('L8b3med') <= 1349.25) ? " + 
"-0.0005469609150050286" + 
":  " + 
"0.004885919871271865" + 
":  " + 
"(b('bare') <= 3.066513255238533) ? " + 
"-0.025485242069980672" + 
":  " + 
"-0.0060383665633093305" + 
":  " + 
"(b('lon') <= -113.27935028076172) ? " + 
"(b('L8b5med') <= 3454.5) ? " + 
"0.00599098209458078" + 
":  " + 
"-0.0021779251864709123" + 
":  " + 
"(b('gvhmean') <= -12.147471904754639) ? " + 
"0.022959411121946167" + 
":  " + 
"0.011944031408111885" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 1927.0) ? " + 
"(b('ndvi_med') <= 3449.5) ? " + 
"(b('L8b5med') <= 1737.0) ? " + 
"0.016084285465851694" + 
":  " + 
"0.019337501399426832" + 
":  " + 
"(b('L8b5med') <= 1720.0) ? " + 
"0.0033583929390505474" + 
":  " + 
"0.005525151054382754" + 
":  " + 
"(b('L8b6med') <= 2241.0) ? " + 
"(b('L8b6med') <= 2133.75) ? " + 
"0.0015030995244284528" + 
":  " + 
"-0.016546583241374934" + 
":  " + 
"(b('crops') <= 67.3132438659668) ? " + 
"-0.0004953020077582285" + 
":  " + 
"0.003985055358299021" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.022269890691415335" + 
":  " + 
"(b('L8b10med') <= 2545.5) ? " + 
"(b('L8b3med') <= 1316.75) ? " + 
"0.00031578769642212715" + 
":  " + 
"0.018621756599898457" + 
":  " + 
"(b('gvhk2') <= 0.2062721624970436) ? " + 
"0.006767982096489094" + 
":  " + 
"-0.004870058746712065" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"(b('gvhk2') <= 0.2706858962774277) ? " + 
"(b('lat') <= 32.43484020233154) ? " + 
"-0.028110883418586557" + 
":  " + 
"0.0010654472852863464" + 
":  " + 
"(b('grass') <= 9.205488204956055) ? " + 
"0.04273064659941997" + 
":  " + 
"-0.008707178818619987" + 
":  " + 
"(b('gvhk2') <= 0.33247002959251404) ? " + 
"(b('gvhmean') <= -13.73606538772583) ? " + 
"0.02565651247625777" + 
":  " + 
"0.004477428702026421" + 
":  " + 
"(b('L8b5med') <= 3021.0) ? " + 
"0.0020261928419941563" + 
":  " + 
"-0.007745888205085972" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2626.0) ? " + 
"(b('bare') <= 66.87108612060547) ? " + 
"(b('bare') <= 29.32122039794922) ? " + 
"-0.0014419452234052338" + 
":  " + 
"0.01841509093027413" + 
":  " + 
"(b('gvhmean') <= -9.959864616394043) ? " + 
"-0.02508103185706507" + 
":  " + 
"-0.01834403767930985" + 
":  " + 
"(b('L8b5med') <= 2694.5) ? " + 
"(b('gvvmean') <= -14.590583801269531) ? " + 
"0.03244232876098112" + 
":  " + 
"0.005957185291633955" + 
":  " + 
"(b('lon') <= 0.756400004029274) ? " + 
"0.003039041086962097" + 
":  " + 
"-0.002761717053682498" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 56.04010009765625) ? " + 
"(b('lat') <= 56.031551361083984) ? " + 
"(b('crops') <= 67.3132438659668) ? " + 
"-0.0005204390874448783" + 
":  " + 
"0.0033953186757734164" + 
":  " + 
"(b('bulk') <= 127.0) ? " + 
"-0.018259120861998615" + 
":  " + 
"-0.010686998322468624" + 
":  " + 
"(b('L8b6med') <= 2364.0) ? " + 
"(b('gvhk2') <= 0.5014166831970215) ? " + 
"-0.00037948361820613896" + 
":  " + 
"0.005749666167050388" + 
":  " + 
"(b('gvhk2') <= 0.49348171055316925) ? " + 
"0.012425705730962439" + 
":  " + 
"0.014699019198910729" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 99.8344841003418) ? " + 
"(b('gvhk3') <= 0.027968889102339745) ? " + 
"(b('gvhk3') <= 0.023529446683824062) ? " + 
"-0.00010808782829515101" + 
":  " + 
"0.016499636463912844" + 
":  " + 
"(b('gvhk3') <= 0.029254012741148472) ? " + 
"-0.034244952579699145" + 
":  " + 
"-0.002136333874629404" + 
":  " + 
"(b('gvhk2') <= 0.5329283177852631) ? " + 
"(b('sand') <= 40.5) ? " + 
"0.006051236283057379" + 
":  " + 
"0.0018321571665365737" + 
":  " + 
"(b('bulk') <= 152.0) ? " + 
"0.014302137102293042" + 
":  " + 
"0.005820939829863647" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('L8b3med') <= 570.0) ? " + 
"(b('gvhmean') <= -14.234665393829346) ? " + 
"0.003136717114843701" + 
":  " + 
"0.012768320986232077" + 
":  " + 
"(b('lat') <= 43.65060043334961) ? " + 
"0.001092673267951272" + 
":  " + 
"-0.001505070835206242" + 
":  " + 
"-0.02087807250925444" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.2869482487440109) ? " + 
"(b('gvhk2') <= 0.2732113152742386) ? " + 
"(b('lat') <= 32.43484020233154) ? " + 
"-0.025202015189608507" + 
":  " + 
"0.0008412412466573745" + 
":  " + 
"(b('L8b3med') <= 794.5) ? " + 
"-0.0009066261966868041" + 
":  " + 
"-0.018192254679061975" + 
":  " + 
"(b('L8b6med') <= 3707.0) ? " + 
"(b('L8b6med') <= 3673.5) ? " + 
"0.0015172022416849917" + 
":  " + 
"0.027306570089643812" + 
":  " + 
"(b('L8b3med') <= 1563.0) ? " + 
"-0.009172313150731788" + 
":  " + 
"0.012216985435186206" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.002807944343658164) ? " + 
"(b('crops') <= 29.342199325561523) ? " + 
"0.03212569606163396" + 
":  " + 
"0.012048975353792159" + 
":  " + 
"(b('grass') <= 44.59784507751465) ? " + 
"-0.00824075650142127" + 
":  " + 
"0.002926119208334587" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"(b('lon') <= -119.65214157104492) ? " + 
"0.018401735190536967" + 
":  " + 
"-0.003914660309772631" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"0.004660730460301624" + 
":  " + 
"-0.001148191087675074" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.18899917602539) ? " + 
"(b('gvhk3') <= -0.006211616564542055) ? " + 
"(b('gvhk2') <= 0.2965504080057144) ? " + 
"-0.022622744883643613" + 
":  " + 
"-0.002436043705989435" + 
":  " + 
"(b('lon') <= -112.48027038574219) ? " + 
"0.002530719095678025" + 
":  " + 
"-0.00397050993723106" + 
":  " + 
"(b('lon') <= -71.2344970703125) ? " + 
"(b('lat') <= 32.78880023956299) ? " + 
"-0.01735906904570261" + 
":  " + 
"0.011338421846793678" + 
":  " + 
"(b('gvhk3') <= -0.004809212172403932) ? " + 
"0.005078664738258836" + 
":  " + 
"-0.0024421447240434257" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 67.3132438659668) ? " + 
"(b('grass') <= 21.1055850982666) ? " + 
"(b('lat') <= 36.37240028381348) ? " + 
"0.003083154596473609" + 
":  " + 
"-0.010346878732574788" + 
":  " + 
"(b('grass') <= 48.60617256164551) ? " + 
"0.0031712399615621235" + 
":  " + 
"-0.0007316154236675545" + 
":  " + 
"(b('bare') <= 5.524640083312988) ? " + 
"(b('L8b5med') <= 3232.5) ? " + 
"0.0004200303278705968" + 
":  " + 
"0.020701792063156737" + 
":  " + 
"(b('ndvi_med') <= 1794.0) ? " + 
"-0.02434908904233416" + 
":  " + 
"-0.02966360583910585" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.11113361269235611) ? " + 
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('grass') <= 27.1253719329834) ? " + 
"0.02577471278700183" + 
":  " + 
"0.000826820662501726" + 
":  " + 
"(b('lon') <= -118.22820281982422) ? " + 
"-0.004419956342563712" + 
":  " + 
"-0.011655759662658196" + 
":  " + 
"(b('gvhk2') <= 0.13928855955600739) ? " + 
"(b('gvhk2') <= 0.1391236111521721) ? " + 
"0.005172352544012119" + 
":  " + 
"0.044976784321516305" + 
":  " + 
"(b('L8b10med') <= 3352.25) ? " + 
"-0.0002716917199358482" + 
":  " + 
"0.012091167381260006" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('L8b3med') <= 1133.0) ? " + 
"(b('lon') <= -120.94869613647461) ? " + 
"-0.022263672596641276" + 
":  " + 
"-0.00011422034078378273" + 
":  " + 
"(b('L8b5med') <= 3177.0) ? " + 
"0.0066241253536395706" + 
":  " + 
"-0.031715778832508396" + 
":  " + 
"(b('crops') <= 77.83634567260742) ? " + 
"(b('grass') <= 51.18161964416504) ? " + 
"0.004830760318265627" + 
":  " + 
"-0.004931582407550931" + 
":  " + 
"(b('grass') <= 1.0924532413482666) ? " + 
"0.021256401454339158" + 
":  " + 
"-0.02815212982165154" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.18899917602539) ? " + 
"(b('gvhk3') <= -0.006211616564542055) ? " + 
"(b('bare') <= 4.342553377151489) ? " + 
"-0.02324103693535719" + 
":  " + 
"-0.004626054964458401" + 
":  " + 
"(b('bulk') <= 130.5) ? " + 
"-0.008824654757164053" + 
":  " + 
"0.001049534507503041" + 
":  " + 
"(b('lon') <= -105.1441421508789) ? " + 
"0.03699617557774958" + 
":  " + 
"(b('bare') <= 4.103881359100342) ? " + 
"0.0016750543036198322" + 
":  " + 
"-0.008867495334962863" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1207.25) ? " + 
"(b('L8b3med') <= 1443.0) ? " + 
"(b('bulk') <= 139.5) ? " + 
"0.023267929361503" + 
":  " + 
"7.546237447779956e-05" + 
":  " + 
"(b('bare') <= 72.05937194824219) ? " + 
"-0.009268538488499942" + 
":  " + 
"0.0018237807449600545" + 
":  " + 
"(b('bare') <= 25.768656730651855) ? " + 
"(b('L8b10med') <= 3352.25) ? " + 
"-0.00017504824311936228" + 
":  " + 
"0.015769252321815787" + 
":  " + 
"(b('ndvi_med') <= 1401.75) ? " + 
"0.014740446308822458" + 
":  " + 
"0.046252053350413574" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 570.0) ? " + 
"(b('gvhmean') <= -14.234665393829346) ? " + 
"0.003268757824961166" + 
":  " + 
"(b('sand') <= 52.0) ? " + 
"0.014243142667448971" + 
":  " + 
"0.00979170830466844" + 
":  " + 
"(b('L8b3med') <= 761.5) ? " + 
"(b('L8b3med') <= 753.5) ? " + 
"-0.0010258410020670466" + 
":  " + 
"-0.018145765126945088" + 
":  " + 
"(b('ndvi_med') <= 4153.25) ? " + 
"-0.0002996499549619372" + 
":  " + 
"0.006669807388680844" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= -0.187941275537014) ? " + 
"(b('gvhk3') <= -0.40707144141197205) ? " + 
"0.004146216917632173" + 
":  " + 
"(b('gvvmean') <= -4.690158128738403) ? " + 
"0.015082158719592703" + 
":  " + 
"0.012758318334648883" + 
":  " + 
"(b('gvhmean') <= -6.832682847976685) ? " + 
"(b('gvhk2') <= 0.6213062107563019) ? " + 
"0.0003324204427097078" + 
":  " + 
"-0.007872833633742348" + 
":  " + 
"(b('gvvmean') <= -6.493995904922485) ? " + 
"-0.03340806959895826" + 
":  " + 
"-0.005449526739620465" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.11607062816619873) ? " + 
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('grass') <= 27.1253719329834) ? " + 
"0.022358440153190995" + 
":  " + 
"0.0005363559216714515" + 
":  " + 
"(b('lon') <= -118.22820281982422) ? " + 
"-0.0030434781733211323" + 
":  " + 
"-0.009911750406115886" + 
":  " + 
"(b('gvhk2') <= 0.13928855955600739) ? " + 
"(b('gvhk2') <= 0.1391236111521721) ? " + 
"0.005725146823465889" + 
":  " + 
"0.03508325751943431" + 
":  " + 
"(b('L8b6med') <= 4153.5) ? " + 
"-0.00019839054122453912" + 
":  " + 
"0.01085872215596036" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2030.0) ? " + 
"(b('L8b10med') <= 2011.5) ? " + 
"(b('ndvi_med') <= 2814.0) ? " + 
"-0.0035393560611121375" + 
":  " + 
"0.003085217036455248" + 
":  " + 
"(b('lat') <= 44.500009536743164) ? " + 
"0.009278321590696498" + 
":  " + 
"0.043405387150059926" + 
":  " + 
"(b('L8b10med') <= 2056.5) ? " + 
"(b('bare') <= 4.8516905307769775) ? " + 
"-0.023321524853624577" + 
":  " + 
"-0.008645460098125154" + 
":  " + 
"(b('ndvi_med') <= 2884.5) ? " + 
"0.0006386334844952743" + 
":  " + 
"-0.0068393619380290906" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2061.5) ? " + 
"(b('L8b3med') <= 927.5) ? " + 
"(b('L8b3med') <= 778.0) ? " + 
"0.006057273188749062" + 
":  " + 
"-0.010065311158404547" + 
":  " + 
"(b('L8b5med') <= 2004.75) ? " + 
"0.01039032649343144" + 
":  " + 
"0.015667210651771384" + 
":  " + 
"(b('L8b5med') <= 2436.5) ? " + 
"(b('lat') <= -34.72389030456543) ? " + 
"-0.024584481855269395" + 
":  " + 
"-0.0019409644597488528" + 
":  " + 
"(b('gvvmean') <= -7.417926073074341) ? " + 
"0.0009674145654905483" + 
":  " + 
"-0.014119679333787993" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1207.25) ? " + 
"(b('gvhk3') <= -0.0031420664163306355) ? " + 
"(b('gvhmean') <= -9.959864616394043) ? " + 
"-0.018502176275044115" + 
":  " + 
"-0.013716378188700133" + 
":  " + 
"(b('gvhk3') <= 0.01757759228348732) ? " + 
"-0.0003142633709939677" + 
":  " + 
"-0.00764271442032831" + 
":  " + 
"(b('bare') <= 25.768656730651855) ? " + 
"(b('gvhmean') <= -14.55401086807251) ? " + 
"0.0026267966112257482" + 
":  " + 
"-0.0006889942251113358" + 
":  " + 
"(b('gvvmean') <= -11.365689754486084) ? " + 
"0.03412495963615624" + 
":  " + 
"0.0033072844734867157" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('ndvi_med') <= 2387.5) ? " + 
"-0.004276348997787477" + 
":  " + 
"(b('grass') <= 79.14345169067383) ? " + 
"-0.014496764908185064" + 
":  " + 
"-0.012664844549731685" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"(b('L8b5med') <= 2703.5) ? " + 
"0.014923315167080273" + 
":  " + 
"-0.0005302717505571708" + 
":  " + 
"(b('lat') <= -34.72389030456543) ? " + 
"-0.022222923789048173" + 
":  " + 
"5.9692349014448524e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.18899917602539) ? " + 
"(b('gvhk3') <= -0.006211616564542055) ? " + 
"(b('bare') <= 4.342553377151489) ? " + 
"-0.02063001639232296" + 
":  " + 
"-0.0036998941144361364" + 
":  " + 
"(b('bulk') <= 130.5) ? " + 
"-0.007363177865659951" + 
":  " + 
"0.0007896398129735167" + 
":  " + 
"(b('L8b6med') <= 3707.5) ? " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"0.006554688949905189" + 
":  " + 
"-0.0006405541185973895" + 
":  " + 
"(b('sand') <= 54.5) ? " + 
"-0.01862016517390039" + 
":  " + 
"-0.0010615880491780466" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 145.5) ? " + 
"(b('bulk') <= 137.5) ? " + 
"(b('bare') <= 1.2342107892036438) ? " + 
"0.0008286670850628698" + 
":  " + 
"-0.006353272048852556" + 
":  " + 
"(b('grass') <= 80.87865447998047) ? " + 
"0.005677067322956076" + 
":  " + 
"-0.005639788163215982" + 
":  " + 
"(b('gvhk3') <= -0.019478777423501015) ? " + 
"(b('L8b3med') <= 1419.75) ? " + 
"0.038854656408656874" + 
":  " + 
"0.0077445229935851345" + 
":  " + 
"(b('lat') <= 39.750959396362305) ? " + 
"0.0002048231140271378" + 
":  " + 
"-0.007449635217718459" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.002807944343658164) ? " + 
"(b('L8b5med') <= 4710.5) ? " + 
"0.013928743475225491" + 
":  " + 
"-0.00480622795191088" + 
":  " + 
"(b('L8b5med') <= 2517.5) ? " + 
"0.004689759220361321" + 
":  " + 
"-0.005719546339444371" + 
":  " + 
"(b('bulk') <= 123.5) ? " + 
"(b('gvvmean') <= -10.37366247177124) ? " + 
"-0.013349827553061577" + 
":  " + 
"-0.018075759697167765" + 
":  " + 
"(b('gvhk2') <= 0.35234180092811584) ? " + 
"-0.0012491850219665632" + 
":  " + 
"0.0015518943084229424" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('L8b3med') <= 1133.0) ? " + 
"(b('lon') <= -120.94869613647461) ? " + 
"-0.020320448332479604" + 
":  " + 
"5.787434645155327e-06" + 
":  " + 
"(b('L8b5med') <= 3177.0) ? " + 
"0.005433221194647404" + 
":  " + 
"-0.027093577189268164" + 
":  " + 
"(b('L8b10med') <= 2822.25) ? " + 
"(b('grass') <= 13.37189245223999) ? " + 
"-0.021761209191980907" + 
":  " + 
"-0.00261725947400235" + 
":  " + 
"(b('L8b10med') <= 2851.0) ? " + 
"0.019655491450716378" + 
":  " + 
"-0.00029926442715605726" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('L8b3med') <= 963.0) ? " + 
"-0.004203725508828596" + 
":  " + 
"(b('ndvi_med') <= 2553.75) ? " + 
"-0.013664404519051168" + 
":  " + 
"-0.011437946589370113" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"(b('L8b5med') <= 2703.5) ? " + 
"0.013128904683601735" + 
":  " + 
"-0.00045828730391886396" + 
":  " + 
"(b('lat') <= -34.72389030456543) ? " + 
"-0.02037118610134954" + 
":  " + 
"6.38387705624245e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1429.75) ? " + 
"(b('L8b5med') <= 3093.0) ? " + 
"(b('sand') <= 45.5) ? " + 
"-0.009439686680601966" + 
":  " + 
"0.0029438403119884425" + 
":  " + 
"(b('L8b10med') <= 1349.0) ? " + 
"-0.0296156303585815" + 
":  " + 
"-0.01129744061284833" + 
":  " + 
"(b('L8b10med') <= 1622.5) ? " + 
"(b('ndvi_med') <= 3483.0) ? " + 
"0.008975673278236364" + 
":  " + 
"-0.0035400706187194027" + 
":  " + 
"(b('L8b3med') <= 761.5) ? " + 
"-0.007764858344014612" + 
":  " + 
"0.00015607879966410488" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= -0.187941275537014) ? " + 
"(b('gvhk2') <= 0.8838767409324646) ? " + 
"(b('gvvmean') <= -4.690158128738403) ? " + 
"0.013345715603718888" + 
":  " + 
"0.012238987104235988" + 
":  " + 
"0.004488095828920957" + 
":  " + 
"(b('lat') <= 55.93754959106445) ? " + 
"(b('gvhk3') <= -0.019478777423501015) ? " + 
"0.00660789938302518" + 
":  " + 
"-9.133429681839028e-05" + 
":  " + 
"(b('sand') <= 74.5) ? " + 
"-0.011370387970655907" + 
":  " + 
"0.000853062928950579" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.11356435716152191) ? " + 
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('grass') <= 27.1253719329834) ? " + 
"0.01915340899318152" + 
":  " + 
"0.0004978414507010066" + 
":  " + 
"(b('lon') <= -118.22820281982422) ? " + 
"-0.002340834904970472" + 
":  " + 
"-0.009968021332843854" + 
":  " + 
"(b('gvhk2') <= 0.13928855955600739) ? " + 
"(b('gvhk2') <= 0.1391236111521721) ? " + 
"0.004509108665731601" + 
":  " + 
"0.02691792910577337" + 
":  " + 
"(b('gvhk2') <= 0.1473740190267563) ? " + 
"-0.014865193469998303" + 
":  " + 
"9.512632097386632e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -120.94869613647461) ? " + 
"(b('L8b5med') <= 2640.0) ? " + 
"(b('L8b5med') <= 2527.0) ? " + 
"-0.021802189552395893" + 
":  " + 
"-0.012574272461068889" + 
":  " + 
"(b('L8b6med') <= 3868.0) ? " + 
"-0.004373786929124468" + 
":  " + 
"0.008512069393922864" + 
":  " + 
"(b('lon') <= -120.89466857910156) ? " + 
"(b('lon') <= -120.92649459838867) ? " + 
"0.01496829104668497" + 
":  " + 
"0.0069327821642308635" + 
":  " + 
"(b('lon') <= -120.88069915771484) ? " + 
"-0.027425864695029646" + 
":  " + 
"0.00014808402366849293" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1207.25) ? " + 
"(b('bare') <= 1.7483659982681274) ? " + 
"(b('gvhk2') <= 0.3000176325440407) ? " + 
"0.020293545597413976" + 
":  " + 
"-0.0002704102772244227" + 
":  " + 
"(b('ndvi_med') <= 1146.25) ? " + 
"-0.002466765274110719" + 
":  " + 
"-0.013305476930777388" + 
":  " + 
"(b('bare') <= 25.768656730651855) ? " + 
"(b('sand') <= 41.5) ? " + 
"-0.0014464211862234245" + 
":  " + 
"0.0010730590718240002" + 
":  " + 
"(b('gvhmean') <= -12.050698280334473) ? " + 
"0.03414348806335543" + 
":  " + 
"0.010831672059762279" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('L8b3med') <= 1133.0) ? " + 
"(b('L8b6med') <= 3602.0) ? " + 
"0.0002328684310013965" + 
":  " + 
"-0.007946801561789516" + 
":  " + 
"(b('L8b5med') <= 3177.0) ? " + 
"0.004841681301854622" + 
":  " + 
"-0.024276756713524056" + 
":  " + 
"(b('crops') <= 77.83634567260742) ? " + 
"(b('gvhk2') <= 0.4412725418806076) ? " + 
"-0.0026001012067926785" + 
":  " + 
"0.007666100762710393" + 
":  " + 
"(b('grass') <= 1.0924532413482666) ? " + 
"0.01669193105430833" + 
":  " + 
"-0.02225785749575154" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.3996696472168) ? " + 
"(b('L8b5med') <= 2200.5) ? " + 
"0.022260937414184376" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"0.002101617601529385" + 
":  " + 
"-0.006848158732763588" + 
":  " + 
"(b('lat') <= 34.940629959106445) ? " + 
"(b('gvhk3') <= 0.014237639959901571) ? " + 
"0.002562516121096977" + 
":  " + 
"0.022152340304251422" + 
":  " + 
"(b('L8b10med') <= 3352.25) ? " + 
"-0.00016469157383153387" + 
":  " + 
"0.009640817032090734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.002807944343658164) ? " + 
"(b('bulk') <= 117.5) ? " + 
"0.008469941120026178" + 
":  " + 
"0.02499841010332704" + 
":  " + 
"(b('crops') <= 53.35454559326172) ? " + 
"0.001152055746841428" + 
":  " + 
"-0.01001873920322884" + 
":  " + 
"(b('L8b3med') <= 765.0) ? " + 
"(b('bare') <= 2.9754223823547363) ? " + 
"-0.0020952738125231594" + 
":  " + 
"-0.019342233315380056" + 
":  " + 
"(b('ndvi_med') <= 4153.25) ? " + 
"-0.00030806119596470095" + 
":  " + 
"0.00826003384719384" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2061.5) ? " + 
"(b('L8b3med') <= 927.5) ? " + 
"(b('L8b3med') <= 778.0) ? " + 
"0.005316484527539265" + 
":  " + 
"-0.007936414127238577" + 
":  " + 
"(b('L8b5med') <= 2004.75) ? " + 
"0.00886720647367304" + 
":  " + 
"0.013277275060692382" + 
":  " + 
"(b('L8b5med') <= 2436.5) ? " + 
"(b('lat') <= 46.397640228271484) ? " + 
"-0.003901830646961742" + 
":  " + 
"0.002945802843117691" + 
":  " + 
"(b('gvvmean') <= -7.417926073074341) ? " + 
"0.0008104930522519188" + 
":  " + 
"-0.012653455970797773" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('gvhmean') <= -15.758374214172363) ? " + 
"-0.0039218491749793555" + 
":  " + 
"(b('gvvmean') <= -15.517379760742188) ? " + 
"-0.010432648147466722" + 
":  " + 
"-0.012571713616664329" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"(b('L8b6med') <= 3622.25) ? " + 
"0.0032634050070273132" + 
":  " + 
"0.015311113037193319" + 
":  " + 
"(b('lon') <= 146.15660095214844) ? " + 
"6.495844085415259e-05" + 
":  " + 
"-0.017761312285262405" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1429.75) ? " + 
"(b('L8b5med') <= 3093.0) ? " + 
"(b('lat') <= 41.60874938964844) ? " + 
"-0.016252243230777383" + 
":  " + 
"0.0015033945071739024" + 
":  " + 
"(b('L8b10med') <= 1349.0) ? " + 
"-0.026661396288463368" + 
":  " + 
"-0.009694572664690477" + 
":  " + 
"(b('L8b10med') <= 1622.5) ? " + 
"(b('ndvi_med') <= 3435.0) ? " + 
"0.008290555813388308" + 
":  " + 
"-0.0028027086743979053" + 
":  " + 
"(b('gvhk2') <= 0.35234180092811584) ? " + 
"-0.001511894395740538" + 
":  " + 
"0.0018046206523962757" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3232.5) ? " + 
"(b('L8b5med') <= 3213.5) ? " + 
"(b('gvhk2') <= 0.35234180092811584) ? " + 
"-0.0012647876071782652" + 
":  " + 
"0.0016076852764765454" + 
":  " + 
"(b('gvhk3') <= 0.03051651269197464) ? " + 
"-0.019895027316208666" + 
":  " + 
"-0.001620858571566991" + 
":  " + 
"(b('gvvmean') <= -10.855828762054443) ? " + 
"(b('gvhk3') <= -0.001903281023260206) ? " + 
"0.0068476516387015645" + 
":  " + 
"-0.005636068103227683" + 
":  " + 
"(b('bare') <= 3.8496270179748535) ? " + 
"0.017012080378698034" + 
":  " + 
"-0.0062236979128220335" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.014705294081915898" + 
":  " + 
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 42.838584899902344) ? " + 
"0.00019735592498962068" + 
":  " + 
"0.01175841851559101" + 
":  " + 
"(b('lat') <= 43.663949966430664) ? " + 
"-0.019756184129403963" + 
":  " + 
"-0.0006119471399120037" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.002807944343658164) ? " + 
"(b('L8b6med') <= 3691.5) ? " + 
"0.010643160584774228" + 
":  " + 
"-0.005066440127227789" + 
":  " + 
"(b('crops') <= 53.35454559326172) ? " + 
"0.0012613050217825303" + 
":  " + 
"-0.008438969969933152" + 
":  " + 
"(b('bulk') <= 123.5) ? " + 
"(b('gvhk3') <= -0.055018717888742685) ? " + 
"-0.014871650969909195" + 
":  " + 
"-0.01091274851010457" + 
":  " + 
"(b('gvhmean') <= -15.623340129852295) ? " + 
"0.0031733178799445215" + 
":  " + 
"-0.0004391970924951665" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('lat') <= 55.93754959106445) ? " + 
"(b('lat') <= 55.89159965515137) ? " + 
"3.497941081535091e-07" + 
":  " + 
"0.006635991110282305" + 
":  " + 
"(b('crops') <= 41.668046951293945) ? " + 
"0.005521338698740039" + 
":  " + 
"-0.005959045001920129" + 
":  " + 
"(b('gvhk2') <= 0.8954881727695465) ? " + 
"0.01111247337166868" + 
":  " + 
"0.0033361085334317198" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('L8b3med') <= 963.0) ? " + 
"-0.004207997210272915" + 
":  " + 
"(b('grass') <= 79.14345169067383) ? " + 
"-0.011631623710545436" + 
":  " + 
"-0.009706464788267588" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"(b('L8b5med') <= 2703.5) ? " + 
"0.00994309423501117" + 
":  " + 
"-0.0013639278391638088" + 
":  " + 
"(b('lon') <= 146.15660095214844) ? " + 
"7.303145145945848e-05" + 
":  " + 
"-0.016302262512283706" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -120.94869613647461) ? " + 
"(b('L8b6med') <= 3868.0) ? " + 
"(b('gvhk3') <= 0.002438183466438204) ? " + 
"-0.002655369155012348" + 
":  " + 
"-0.012533367522055819" + 
":  " + 
"(b('L8b5med') <= 2715.5) ? " + 
"0.011546308856679927" + 
":  " + 
"0.004349030920429042" + 
":  " + 
"(b('lon') <= -120.92649459838867) ? " + 
"(b('gvhk2') <= 0.21932660043239594) ? " + 
"0.011884852398345275" + 
":  " + 
"0.013293608920736222" + 
":  " + 
"(b('L8b6med') <= 2381.0) ? " + 
"-0.003278687387826" + 
":  " + 
"0.0004287861248887407" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2473.75) ? " + 
"(b('L8b10med') <= 2428.5) ? " + 
"(b('L8b5med') <= 2543.75) ? " + 
"-0.001259884408482632" + 
":  " + 
"0.0014327766572323714" + 
":  " + 
"(b('lon') <= -108.2667350769043) ? " + 
"0.002276770967901366" + 
":  " + 
"0.03147507544993724" + 
":  " + 
"(b('gvhk2') <= 0.2062721624970436) ? " + 
"(b('gvhk2') <= 0.20436525344848633) ? " + 
"0.0018120990828030916" + 
":  " + 
"0.041132675355891296" + 
":  " + 
"(b('gvhk2') <= 0.4329407513141632) ? " + 
"-0.005506687679571254" + 
":  " + 
"0.0027489745277970066" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2061.5) ? " + 
"(b('ndvi_med') <= 1591.25) ? " + 
"(b('gvhmean') <= -13.20015811920166) ? " + 
"0.00855532497359524" + 
":  " + 
"0.012509361627079787" + 
":  " + 
"(b('gvhmean') <= -11.941157817840576) ? " + 
"-0.008440023387586435" + 
":  " + 
"0.0037973827485164938" + 
":  " + 
"(b('L8b5med') <= 2078.0) ? " + 
"(b('L8b10med') <= 1877.5) ? " + 
"0.011280953150166806" + 
":  " + 
"-0.013118983360134777" + 
":  " + 
"(b('grass') <= 91.94809341430664) ? " + 
"-0.00034037008063291473" + 
":  " + 
"0.004685538843525083" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.3996696472168) ? " + 
"(b('L8b5med') <= 2200.5) ? " + 
"0.0208609980418816" + 
":  " + 
"(b('L8b6med') <= 3492.25) ? " + 
"-0.0073703732660783455" + 
":  " + 
"-0.0007164706742813099" + 
":  " + 
"(b('lat') <= 34.940629959106445) ? " + 
"(b('gvhk3') <= 0.014237639959901571) ? " + 
"0.0029261731876372224" + 
":  " + 
"0.019397129345141245" + 
":  " + 
"(b('L8b10med') <= 3352.25) ? " + 
"-0.0001627403065063064" + 
":  " + 
"0.0088186075158098" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 145.5) ? " + 
"(b('bulk') <= 137.5) ? " + 
"(b('gvvmean') <= -15.11733102798462) ? " + 
"-0.012587096141449577" + 
":  " + 
"-0.00038520630683285066" + 
":  " + 
"(b('gvhk3') <= -0.006239350885152817) ? " + 
"-0.004932450732150043" + 
":  " + 
"0.004866488619065874" + 
":  " + 
"(b('L8b3med') <= 996.0) ? " + 
"(b('L8b3med') <= 975.5) ? " + 
"-0.005099375887815049" + 
":  " + 
"-0.02375284922099307" + 
":  " + 
"(b('gvhk3') <= -0.014193722046911716) ? " + 
"0.015750490269223198" + 
":  " + 
"-0.0003954113288366139" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2030.0) ? " + 
"(b('L8b10med') <= 1965.5) ? " + 
"(b('L8b6med') <= 3095.5) ? " + 
"0.00039533290297237057" + 
":  " + 
"-0.01161840445599855" + 
":  " + 
"(b('lat') <= 41.49301528930664) ? " + 
"-0.011624544354295975" + 
":  " + 
"0.014333119157325167" + 
":  " + 
"(b('L8b10med') <= 2056.5) ? " + 
"(b('bare') <= 4.8516905307769775) ? " + 
"-0.02099882994104659" + 
":  " + 
"-0.006874683190617625" + 
":  " + 
"(b('sand') <= 71.0) ? " + 
"0.00017619380966407501" + 
":  " + 
"-0.009385711296094822" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -5.297438144683838) ? " + 
"(b('gvvmean') <= -6.832682847976685) ? " + 
"(b('L8b5med') <= 2436.5) ? " + 
"-0.0012712694577871613" + 
":  " + 
"0.0006034217035404574" + 
":  " + 
"(b('bulk') <= 127.0) ? " + 
"0.00598254214157079" + 
":  " + 
"-0.01463016319682687" + 
":  " + 
"(b('ndvi_med') <= 4110.5) ? " + 
"0.010310171969595675" + 
":  " + 
"(b('ndvi_med') <= 5067.5) ? " + 
"0.004829490713902929" + 
":  " + 
"0.00310648872008934" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 760.5) ? " + 
"(b('bare') <= 72.05937194824219) ? " + 
"(b('L8b3med') <= 1692.5) ? " + 
"-0.0016224773091341922" + 
":  " + 
"-0.010865239995011511" + 
":  " + 
"(b('L8b3med') <= 1915.75) ? " + 
"0.002963738088647791" + 
":  " + 
"0.00025927832030285997" + 
":  " + 
"(b('bare') <= 29.32122039794922) ? " + 
"(b('L8b10med') <= 2473.75) ? " + 
"0.0005900394746686266" + 
":  " + 
"-0.0018903604687091468" + 
":  " + 
"(b('ndvi_med') <= 946.0) ? " + 
"-0.0004840760655067805" + 
":  " + 
"0.016624434317721985" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 41.426435470581055) ? " + 
"(b('ndvi_med') <= 1716.0) ? " + 
"0.0012917811865462297" + 
":  " + 
"-0.0032271976218586624" + 
":  " + 
"(b('ndvi_med') <= 2208.0) ? " + 
"0.0004513976940002155" + 
":  " + 
"0.018404021997305068" + 
":  " + 
"(b('L8b3med') <= 1204.5) ? " + 
"(b('lat') <= 43.663949966430664) ? " + 
"-0.017543452925999597" + 
":  " + 
"-0.00020089275436503" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"-0.005371304877307838" + 
":  " + 
"-0.02205998432959612" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -5.297438144683838) ? " + 
"(b('gvhmean') <= -6.832682847976685) ? " + 
"(b('grass') <= 15.331648826599121) ? " + 
"-0.0016885227315004995" + 
":  " + 
"0.0004618304730466168" + 
":  " + 
"(b('L8b10med') <= 1847.0) ? " + 
"0.005345373255383368" + 
":  " + 
"-0.013123381551061944" + 
":  " + 
"(b('ndvi_med') <= 4110.5) ? " + 
"0.009364260097774663" + 
":  " + 
"(b('lon') <= 9.138250350952148) ? " + 
"0.002756925176050057" + 
":  " + 
"0.004555666964820071" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.11013723909854889) ? " + 
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('grass') <= 27.1253719329834) ? " + 
"0.012519625694496939" + 
":  " + 
"0.0005438810980704159" + 
":  " + 
"(b('bulk') <= 134.5) ? " + 
"-0.0025017056270613125" + 
":  " + 
"-0.009030996546727956" + 
":  " + 
"(b('gvhk2') <= 0.2062721624970436) ? " + 
"(b('gvhk2') <= 0.2059495896100998) ? " + 
"0.0017092483002587252" + 
":  " + 
"0.03651878332670069" + 
":  " + 
"(b('gvhk2') <= 0.21302480250597) ? " + 
"-0.010414223572849296" + 
":  " + 
"0.0001295248131264742" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 570.0) ? " + 
"(b('gvhk3') <= 0.008902890840545297) ? " + 
"(b('grass') <= 56.41641807556152) ? " + 
"0.007476760309651526" + 
":  " + 
"0.009937878452359938" + 
":  " + 
"0.000616770088314289" + 
":  " + 
"(b('L8b3med') <= 761.5) ? " + 
"(b('bare') <= 2.9754223823547363) ? " + 
"-0.0011791094498736741" + 
":  " + 
"-0.014796325937911602" + 
":  " + 
"(b('L8b3med') <= 795.5) ? " + 
"0.006835640960821289" + 
":  " + 
"-8.753641213785806e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.027968889102339745) ? " + 
"(b('gvhk3') <= 0.023529446683824062) ? " + 
"(b('gvvmean') <= -15.884497165679932) ? " + 
"0.009053598223095309" + 
":  " + 
"-0.00033398704708900186" + 
":  " + 
"(b('L8b3med') <= 901.5) ? " + 
"0.035240078169034045" + 
":  " + 
"0.006978799069349901" + 
":  " + 
"(b('gvhk3') <= 0.029254012741148472) ? " + 
"(b('bare') <= 3.522136151790619) ? " + 
"-0.028634303812667794" + 
":  " + 
"-0.013348528944370684" + 
":  " + 
"(b('lon') <= -119.46337890625) ? " + 
"-0.00898336275675282" + 
":  " + 
"0.0002472349773320584" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('gvhmean') <= -15.758374214172363) ? " + 
"-0.004127249468329777" + 
":  " + 
"(b('L8b5med') <= 2805.5) ? " + 
"-0.0077241140729979035" + 
":  " + 
"-0.009886917388292643" + 
":  " + 
"(b('gvhmean') <= -14.541287422180176) ? " + 
"(b('ndvi_med') <= 1915.5) ? " + 
"-0.001466371725600835" + 
":  " + 
"0.006777109709834612" + 
":  " + 
"(b('gvhmean') <= -14.526463508605957) ? " + 
"-0.024386032129409624" + 
":  " + 
"-0.00021610497975453946" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"(b('lat') <= 41.426435470581055) ? " + 
"-0.00031177666559289617" + 
":  " + 
"0.004112310566778593" + 
":  " + 
"0.027799671312530083" + 
":  " + 
"(b('L8b3med') <= 1204.5) ? " + 
"(b('gvhk3') <= -0.009556657169014215) ? " + 
"0.0028802553042703823" + 
":  " + 
"-0.0014374958061978596" + 
":  " + 
"(b('lat') <= 45.51217842102051) ? " + 
"-0.01974184092112833" + 
":  " + 
"-0.005054216483819547" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 166.0) ? " + 
"(b('ndvi_med') <= 1322.5) ? " + 
"-0.0018469436720295268" + 
":  " + 
"0.00026582186007788913" + 
":  " + 
"(b('crops') <= 49.58632469177246) ? " + 
"0.009892384893969144" + 
":  " + 
"-0.0029161600915040414" + 
":  " + 
"-0.012216759900681898" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"(b('gvhmean') <= -12.406572818756104) ? " + 
"-0.0006445641398497944" + 
":  " + 
"0.0027877271278024117" + 
":  " + 
"0.02499312199526932" + 
":  " + 
"(b('L8b10med') <= 2024.0) ? " + 
"(b('L8b10med') <= 2011.5) ? " + 
"0.0001757211539196356" + 
":  " + 
"0.031155526775759168" + 
":  " + 
"(b('lon') <= -110.83245468139648) ? " + 
"-0.012044497027252824" + 
":  " + 
"-0.0015573075338172185" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.002807944343658164) ? " + 
"(b('lat') <= 53.60487365722656) ? " + 
"0.020243477699750878" + 
":  " + 
"0.005892240807284205" + 
":  " + 
"(b('L8b5med') <= 2287.5) ? " + 
"0.01310797017938492" + 
":  " + 
"-0.0017070094539593536" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"(b('sand') <= 76.5) ? " + 
"-0.00342246570089784" + 
":  " + 
"0.003376683769911926" + 
":  " + 
"(b('L8b6med') <= 2680.0) ? " + 
"0.0044203690165911455" + 
":  " + 
"-0.000250305797402646" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1429.75) ? " + 
"(b('gvhk3') <= -0.009009881177917123) ? " + 
"(b('gvhk3') <= -0.015217631589621305) ? " + 
"0.001218195086839058" + 
":  " + 
"0.02438487821982177" + 
":  " + 
"(b('lat') <= 55.96179962158203) ? " + 
"-0.00817964472301739" + 
":  " + 
"0.0009402977504672394" + 
":  " + 
"(b('L8b10med') <= 1622.5) ? " + 
"(b('ndvi_med') <= 3435.0) ? " + 
"0.006703399351009974" + 
":  " + 
"-0.0027259817131515657" + 
":  " + 
"(b('gvhk2') <= 0.35234180092811584) ? " + 
"-0.0011074977100224712" + 
":  " + 
"0.001326855173425414" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3232.5) ? " + 
"(b('grass') <= 19.320551872253418) ? " + 
"(b('lat') <= 41.27712059020996) ? " + 
"-0.0077990706800246485" + 
":  " + 
"-0.0010925855706516382" + 
":  " + 
"(b('grass') <= 23.62397003173828) ? " + 
"0.005323856150880684" + 
":  " + 
"-5.3228323893325305e-06" + 
":  " + 
"(b('gvhmean') <= -10.855828762054443) ? " + 
"(b('gvhk3') <= 0.018007025122642517) ? " + 
"-0.00010635047240689501" + 
":  " + 
"-0.01425521702420969" + 
":  " + 
"(b('bare') <= 3.8496270179748535) ? " + 
"0.013745288945772928" + 
":  " + 
"-0.005166923849092453" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 41.426435470581055) ? " + 
"(b('lat') <= 39.927019119262695) ? " + 
"0.0009255255184283598" + 
":  " + 
"-0.004457854615827441" + 
":  " + 
"(b('grass') <= 78.74732971191406) ? " + 
"0.007061629720920549" + 
":  " + 
"-0.01137972448471239" + 
":  " + 
"(b('L8b3med') <= 1204.5) ? " + 
"(b('L8b3med') <= 1079.0) ? " + 
"-0.0008989293956033378" + 
":  " + 
"0.006057421790403056" + 
":  " + 
"(b('gvhk2') <= 0.29793746769428253) ? " + 
"-0.016972784770987466" + 
":  " + 
"-0.004123332220563727" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('lat') <= -35.35686492919922) ? " + 
"-0.003845147833166501" + 
":  " + 
"(b('L8b5med') <= 2805.5) ? " + 
"-0.007082325977367812" + 
":  " + 
"-0.009028848961133082" + 
":  " + 
"(b('gvhmean') <= -13.548450469970703) ? " + 
"(b('ndvi_med') <= 1884.5) ? " + 
"-0.0009083513418765197" + 
":  " + 
"0.0036491762839498073" + 
":  " + 
"(b('gvhmean') <= -13.340893745422363) ? " + 
"-0.007662944093739525" + 
":  " + 
"-8.097076271362685e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"(b('gvvmean') <= -12.406572818756104) ? " + 
"-0.0004839263660146934" + 
":  " + 
"0.0025132802490479755" + 
":  " + 
"0.021322992669341012" + 
":  " + 
"(b('L8b10med') <= 2024.0) ? " + 
"(b('lon') <= -119.2177848815918) ? " + 
"0.015941716691986407" + 
":  " + 
"-0.00017962567555941338" + 
":  " + 
"(b('lat') <= 45.48440933227539) ? " + 
"-0.008875318266301136" + 
":  " + 
"-0.0009258374368093904" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.11013723909854889) ? " + 
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('ndvi_med') <= 4134.0) ? " + 
"-0.0009288895791748283" + 
":  " + 
"0.006720282097273073" + 
":  " + 
"(b('bulk') <= 134.5) ? " + 
"-0.0020897001003117102" + 
":  " + 
"-0.008081656629363703" + 
":  " + 
"(b('gvhk2') <= 0.13928855955600739) ? " + 
"(b('gvhk2') <= 0.13301168382167816) ? " + 
"0.0019057623916238844" + 
":  " + 
"0.010432020624133273" + 
":  " + 
"(b('gvhk2') <= 0.1473740190267563) ? " + 
"-0.01186115102151409" + 
":  " + 
"4.0878528675094754e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= -0.187941275537014) ? " + 
"(b('gvhk3') <= -0.40707144141197205) ? " + 
"0.002980341509564277" + 
":  " + 
"(b('L8b10med') <= 2168.5) ? " + 
"0.007835925639281344" + 
":  " + 
"0.00898096394319825" + 
":  " + 
"(b('lat') <= 55.93754959106445) ? " + 
"(b('gvhk3') <= -0.019478777423501015) ? " + 
"0.004642835880510556" + 
":  " + 
"-4.966136174403276e-05" + 
":  " + 
"(b('sand') <= 74.5) ? " + 
"-0.007618830054090966" + 
":  " + 
"0.00024145151342232462" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 3352.25) ? " + 
"(b('L8b6med') <= 3707.0) ? " + 
"(b('L8b6med') <= 3683.25) ? " + 
"-7.68404877105746e-05" + 
":  " + 
"0.017285744318006703" + 
":  " + 
"(b('bulk') <= 152.0) ? " + 
"-0.006209201721079744" + 
":  " + 
"0.0014385660918131227" + 
":  " + 
"(b('lat') <= 35.94334411621094) ? " + 
"(b('bulk') <= 149.0) ? " + 
"-0.006037896030650011" + 
":  " + 
"0.0009933824912473875" + 
":  " + 
"(b('gvhk2') <= 0.17413702607154846) ? " + 
"0.00789718779499763" + 
":  " + 
"0.01760383294909776" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -17.05683422088623) ? " + 
"(b('bulk') <= 156.5) ? " + 
"(b('bulk') <= 147.0) ? " + 
"-0.0059140487941819475" + 
":  " + 
"-0.005199089188975402" + 
":  " + 
"-0.007991282069054459" + 
":  " + 
"(b('gvhmean') <= -15.623340129852295) ? " + 
"(b('gvhmean') <= -16.178815841674805) ? " + 
"-0.0016628410305804158" + 
":  " + 
"0.007732893431644474" + 
":  " + 
"(b('gvhmean') <= -15.353689670562744) ? " + 
"-0.004909531351230596" + 
":  " + 
"2.4010183727396536e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.11013723909854889) ? " + 
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('bulk') <= 133.5) ? " + 
"0.006058503054118508" + 
":  " + 
"-0.0008354552171901697" + 
":  " + 
"(b('bulk') <= 134.5) ? " + 
"-0.0019098939740715207" + 
":  " + 
"-0.007263241799854613" + 
":  " + 
"(b('gvhk2') <= 0.2062721624970436) ? " + 
"(b('gvhk2') <= 0.2059495896100998) ? " + 
"0.00146017731230739" + 
":  " + 
"0.03245589368426616" + 
":  " + 
"(b('gvhk2') <= 0.21302480250597) ? " + 
"-0.0083539098783121" + 
":  " + 
"8.09987061106484e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 166.0) ? " + 
"(b('sand') <= 37.5) ? " + 
"-0.0016340039574017984" + 
":  " + 
"0.00034234201538376277" + 
":  " + 
"(b('gvvmean') <= -14.60058069229126) ? " + 
"-0.001751204245535612" + 
":  " + 
"0.008742659918682524" + 
":  " + 
"-0.010839603627167377" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 761.5) ? " + 
"(b('ndvi_med') <= 3821.25) ? " + 
"(b('grass') <= 65.43255615234375) ? " + 
"0.003271036848850026" + 
":  " + 
"-0.005821682103537451" + 
":  " + 
"(b('gvvmean') <= -12.779816627502441) ? " + 
"-0.016345281275254323" + 
":  " + 
"-0.0038580901678048137" + 
":  " + 
"(b('L8b3med') <= 795.5) ? " + 
"(b('L8b5med') <= 2992.0) ? " + 
"0.0010400773259888925" + 
":  " + 
"0.011630875418473935" + 
":  " + 
"(b('L8b3med') <= 849.5) ? " + 
"-0.0038815967004397897" + 
":  " + 
"0.0003363697689976271" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('lat') <= 55.93754959106445) ? " + 
"(b('gvhk3') <= -0.019478777423501015) ? " + 
"0.004115656371911849" + 
":  " + 
"-5.288709867322615e-05" + 
":  " + 
"(b('crops') <= 41.668046951293945) ? " + 
"0.0031805733559355696" + 
":  " + 
"-0.003910613919240437" + 
":  " + 
"(b('gvhk2') <= 0.8954881727695465) ? " + 
"(b('gvhmean') <= -6.224896669387817) ? " + 
"0.008524853184727593" + 
":  " + 
"0.0074034417036460964" + 
":  " + 
"0.0030310653336372284" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2473.75) ? " + 
"(b('L8b10med') <= 2428.5) ? " + 
"(b('grass') <= 0.6753926873207092) ? " + 
"-0.005754914911452818" + 
":  " + 
"0.0002932498284478175" + 
":  " + 
"(b('lon') <= -108.2667350769043) ? " + 
"0.002438554654055543" + 
":  " + 
"0.027372947022895375" + 
":  " + 
"(b('gvhk2') <= 0.23249638080596924) ? " + 
"(b('bulk') <= 143.0) ? " + 
"0.013416559874336953" + 
":  " + 
"-0.00034957805126549746" + 
":  " + 
"(b('gvhk2') <= 0.4329407513141632) ? " + 
"-0.005051796380901836" + 
":  " + 
"0.002659169852602128" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -5.297438144683838) ? " + 
"(b('gvvmean') <= -6.832682847976685) ? " + 
"(b('L8b3med') <= 761.5) ? " + 
"-0.0015013024386498516" + 
":  " + 
"0.0003501638302321796" + 
":  " + 
"(b('gvhmean') <= -6.493995904922485) ? " + 
"-0.018590351235617752" + 
":  " + 
"-0.0027883923437166482" + 
":  " + 
"(b('ndvi_med') <= 4110.5) ? " + 
"(b('crops') <= 89.71894836425781) ? " + 
"0.006633772550436706" + 
":  " + 
"0.007843857228906154" + 
":  " + 
"(b('gvhk3') <= -0.26245076581835747) ? " + 
"0.0026986338174287416" + 
":  " + 
"0.0038076722240623917" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvhk2') <= 0.2723564878106117) ? " + 
"0.021927131697206476" + 
":  " + 
"-0.007399142594350316" + 
":  " + 
"(b('L8b10med') <= 1429.75) ? " + 
"(b('L8b5med') <= 3172.0) ? " + 
"-0.0008323676392011962" + 
":  " + 
"-0.008228461740409166" + 
":  " + 
"(b('L8b10med') <= 1622.5) ? " + 
"0.002697172957265911" + 
":  " + 
"-0.00018021266189489525" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 91.94809341430664) ? " + 
"(b('grass') <= 87.31079864501953) ? " + 
"(b('sand') <= 38.5) ? " + 
"-0.0013665624593133829" + 
":  " + 
"0.0004365056329418211" + 
":  " + 
"(b('lat') <= 41.58543014526367) ? " + 
"-0.0034506371917679226" + 
":  " + 
"-0.016967715196207163" + 
":  " + 
"(b('gvhk2') <= 0.22952740639448166) ? " + 
"-0.016806343029994036" + 
":  " + 
"(b('gvvmean') <= -13.183092594146729) ? " + 
"0.0024139931349300378" + 
":  " + 
"0.01148711086885916" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2473.75) ? " + 
"(b('L8b10med') <= 2428.5) ? " + 
"(b('lon') <= -120.94869613647461) ? " + 
"-0.0053247732397035934" + 
":  " + 
"0.00029701748749273694" + 
":  " + 
"(b('lon') <= -108.2667350769043) ? " + 
"0.0019028650799305293" + 
":  " + 
"0.024575006640477924" + 
":  " + 
"(b('ndvi_med') <= 1685.0) ? " + 
"(b('ndvi_med') <= 1538.0) ? " + 
"-0.0008079191672981166" + 
":  " + 
"0.007458721990083469" + 
":  " + 
"(b('L8b3med') <= 1173.0) ? " + 
"-0.0009646639868771084" + 
":  " + 
"-0.01477612818961646" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 137.5) ? " + 
"(b('gvvmean') <= -15.11733102798462) ? " + 
"(b('ndvi_med') <= 4734.0) ? " + 
"-0.013644481229833819" + 
":  " + 
"-0.008489357229296973" + 
":  " + 
"(b('L8b5med') <= 3241.0) ? " + 
"-0.0012185847820727995" + 
":  " + 
"0.004036924282136156" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"(b('lon') <= -116.1243896484375) ? " + 
"-0.00248515360981263" + 
":  " + 
"0.006420504258220318" + 
":  " + 
"(b('ndvi_med') <= 2510.5) ? " + 
"-9.398775763880061e-05" + 
":  " + 
"-0.007005293806544268" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.11013723909854889) ? " + 
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('grass') <= 27.1253719329834) ? " + 
"0.006883049513551676" + 
":  " + 
"0.00038354169756027803" + 
":  " + 
"(b('lon') <= -118.22820281982422) ? " + 
"-0.0006628249931539959" + 
":  " + 
"-0.0065623477307824645" + 
":  " + 
"(b('gvhk2') <= 0.13928855955600739) ? " + 
"(b('gvhk2') <= 0.13301168382167816) ? " + 
"0.0014718594283065073" + 
":  " + 
"0.008466436079646256" + 
":  " + 
"(b('L8b10med') <= 3352.25) ? " + 
"-0.0001400071015293238" + 
":  " + 
"0.007479279206914706" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1487.5) ? " + 
"(b('L8b3med') <= 1399.5) ? " + 
"(b('L8b10med') <= 2473.75) ? " + 
"0.0003104095600818683" + 
":  " + 
"-0.002593339380334308" + 
":  " + 
"(b('bare') <= 0.1420118361711502) ? " + 
"0.019429832847652435" + 
":  " + 
"0.002124111765481349" + 
":  " + 
"(b('sand') <= 40.5) ? " + 
"(b('L8b10med') <= 2915.5) ? " + 
"0.026371498265029686" + 
":  " + 
"0.0022427503258587375" + 
":  " + 
"(b('grass') <= 55.38705825805664) ? " + 
"-0.0009904855508154429" + 
":  " + 
"-0.010386666537869066" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"(b('L8b5med') <= 2544.5) ? " + 
"0.00786709241342387" + 
":  " + 
"0.0061658573098508085" + 
":  " + 
"(b('L8b3med') <= 761.5) ? " + 
"(b('bare') <= 2.9754223823547363) ? " + 
"-0.0008150175765225312" + 
":  " + 
"-0.011925734068432508" + 
":  " + 
"(b('L8b3med') <= 888.5) ? " + 
"0.002476600017320622" + 
":  " + 
"-0.00030029729357431236" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.027968889102339745) ? " + 
"(b('gvhk3') <= 0.023529446683824062) ? " + 
"(b('gvhmean') <= -15.884497165679932) ? " + 
"0.007279636672152651" + 
":  " + 
"-0.0002927722365540963" + 
":  " + 
"(b('ndvi_med') <= 2204.5) ? " + 
"0.012588822214794718" + 
":  " + 
"-0.0031149273828895915" + 
":  " + 
"(b('gvhk3') <= 0.029254012741148472) ? " + 
"(b('gvhmean') <= -10.727792739868164) ? " + 
"-0.025209017004164086" + 
":  " + 
"-0.011206516073017123" + 
":  " + 
"(b('lon') <= -119.46337890625) ? " + 
"-0.007695966147526144" + 
":  " + 
"0.00038056890218779633" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -16.209970474243164) ? " + 
"(b('gvhk2') <= 0.537092536687851) ? " + 
"(b('bare') <= 15.181381702423096) ? " + 
"-0.0028177396259230674" + 
":  " + 
"0.010186855188537111" + 
":  " + 
"-0.01521086884952047" + 
":  " + 
"(b('gvhmean') <= -15.980653285980225) ? " + 
"(b('grass') <= 75.39257049560547) ? " + 
"0.027686066685427335" + 
":  " + 
"0.005822693556675605" + 
":  " + 
"(b('L8b3med') <= 997.5) ? " + 
"-0.0007850094583749025" + 
":  " + 
"0.0007554008095036668" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -5.297438144683838) ? " + 
"(b('gvhmean') <= -6.832682847976685) ? " + 
"(b('gvhk2') <= 0.618810385465622) ? " + 
"0.0001284999644933207" + 
":  " + 
"-0.003196456298949089" + 
":  " + 
"(b('gvvmean') <= -6.493995904922485) ? " + 
"-0.016821710757797093" + 
":  " + 
"-0.002354729098407319" + 
":  " + 
"(b('ndvi_med') <= 4110.5) ? " + 
"(b('gvhmean') <= -4.690158128738403) ? " + 
"0.005880000649651912" + 
":  " + 
"0.007714781661137371" + 
":  " + 
"(b('ndvi_med') <= 5067.5) ? " + 
"0.0033511511952743767" + 
":  " + 
"0.00266753754932908" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('ndvi_med') <= 3821.25) ? " + 
"0.019942314378490228" + 
":  " + 
"-0.006451332483910888" + 
":  " + 
"(b('L8b10med') <= 1429.75) ? " + 
"(b('lat') <= 55.96179962158203) ? " + 
"-0.00511333967818765" + 
":  " + 
"0.000808666925094277" + 
":  " + 
"(b('L8b10med') <= 1622.5) ? " + 
"0.0025020272324334986" + 
":  " + 
"-0.00017038498771579917" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.11013723909854889) ? " + 
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('sand') <= 42.5) ? " + 
"-0.0034688617598441843" + 
":  " + 
"0.0027666564750079697" + 
":  " + 
"(b('bulk') <= 134.5) ? " + 
"-0.0013362093539406178" + 
":  " + 
"-0.006297515094534984" + 
":  " + 
"(b('gvhk2') <= 0.2062721624970436) ? " + 
"(b('gvhk2') <= 0.2059495896100998) ? " + 
"0.0012498356144469505" + 
":  " + 
"0.02372230381291146" + 
":  " + 
"(b('gvhk2') <= 0.20911672711372375) ? " + 
"-0.011208619895768447" + 
":  " + 
"1.7095189907813834e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1487.5) ? " + 
"(b('L8b3med') <= 1399.5) ? " + 
"(b('L8b3med') <= 1373.75) ? " + 
"-5.8110767223681895e-05" + 
":  " + 
"-0.011658674801334517" + 
":  " + 
"(b('bare') <= 0.1420118361711502) ? " + 
"0.01742413339996719" + 
":  " + 
"0.0018295218047308325" + 
":  " + 
"(b('L8b5med') <= 3040.0) ? " + 
"(b('grass') <= 55.38705825805664) ? " + 
"-0.0022559094969900263" + 
":  " + 
"-0.009424264369403126" + 
":  " + 
"(b('L8b5med') <= 3093.5) ? " + 
"0.013069986616653165" + 
":  " + 
"0.00043735329275708737" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2061.5) ? " + 
"(b('L8b3med') <= 927.5) ? " + 
"(b('L8b3med') <= 778.0) ? " + 
"0.0030718376860437236" + 
":  " + 
"-0.004533113810051783" + 
":  " + 
"(b('gvhmean') <= -13.608022212982178) ? " + 
"0.0030397182436764786" + 
":  " + 
"0.007560017296440642" + 
":  " + 
"(b('L8b5med') <= 2068.5) ? " + 
"(b('gvvmean') <= -9.070109367370605) ? " + 
"-0.014252729813635318" + 
":  " + 
"-0.004873458865711472" + 
":  " + 
"(b('sand') <= 28.5) ? " + 
"0.0026085352474447855" + 
":  " + 
"-0.00023346832648585842" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 166.0) ? " + 
"(b('sand') <= 37.5) ? " + 
"-0.0013990487210614037" + 
":  " + 
"0.00028178907868650274" + 
":  " + 
"(b('gvhmean') <= -14.60058069229126) ? " + 
"-0.0009723177560260754" + 
":  " + 
"0.008221771979202505" + 
":  " + 
"-0.009332184008720185" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -17.05683422088623) ? " + 
"(b('gvhmean') <= -17.338250160217285) ? " + 
"-0.0036630599569610137" + 
":  " + 
"(b('L8b5med') <= 2433.5) ? " + 
"-0.006931455690424623" + 
":  " + 
"-0.005303972691410655" + 
":  " + 
"(b('gvvmean') <= -15.623340129852295) ? " + 
"(b('gvhmean') <= -16.178815841674805) ? " + 
"-0.001399311301248334" + 
":  " + 
"0.005722712047075675" + 
":  " + 
"(b('gvvmean') <= -15.133948802947998) ? " + 
"-0.0029982252641530074" + 
":  " + 
"7.484848691975475e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 3352.25) ? " + 
"(b('L8b10med') <= 2473.75) ? " + 
"(b('L8b10med') <= 2428.5) ? " + 
"9.889737328304426e-05" + 
":  " + 
"0.008141513266197784" + 
":  " + 
"(b('gvhk2') <= 0.4412725418806076) ? " + 
"-0.0024682583458032798" + 
":  " + 
"0.0026643040948270574" + 
":  " + 
"(b('lon') <= -113.27935028076172) ? " + 
"(b('lon') <= -115.47503662109375) ? " + 
"0.0008230965995037979" + 
":  " + 
"-0.0058218226562638115" + 
":  " + 
"(b('gvhk3') <= 0.005131373560288921) ? " + 
"0.006524297692363644" + 
":  " + 
"0.01506482323659833" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -112.57361602783203) ? " + 
"(b('gvhk3') <= -0.01524945255368948) ? " + 
"(b('gvvmean') <= -14.383522510528564) ? " + 
"-0.0034842119731655075" + 
":  " + 
"-0.017324819600700328" + 
":  " + 
"(b('lon') <= -113.06564331054688) ? " + 
"0.0006501355962462116" + 
":  " + 
"0.02977763189786256" + 
":  " + 
"(b('lon') <= -108.2274055480957) ? " + 
"(b('bare') <= 3.809523820877075) ? " + 
"-0.009284571240303137" + 
":  " + 
"-7.463698540774906e-05" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.0007373726944066312" + 
":  " + 
"-0.00263638749792276" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1125.75) ? " + 
"(b('bulk') <= 145.5) ? " + 
"(b('gvvmean') <= -16.04317569732666) ? " + 
"0.02136253243698799" + 
":  " + 
"4.506810082132153e-05" + 
":  " + 
"(b('sand') <= 41.5) ? " + 
"-0.006343816651566418" + 
":  " + 
"0.0007338445023116012" + 
":  " + 
"(b('L8b3med') <= 1208.0) ? " + 
"(b('gvhk3') <= -0.01524945255368948) ? " + 
"-0.013895144972494014" + 
":  " + 
"0.006169767477764472" + 
":  " + 
"(b('L8b3med') <= 1316.75) ? " + 
"-0.004526686425875286" + 
":  " + 
"0.0010469895619534947" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 133.5) ? " + 
"(b('gvhk3') <= -0.00421099248342216) ? " + 
"(b('gvhk2') <= 0.2142050936818123) ? " + 
"0.011251434350450014" + 
":  " + 
"0.00014434482293268312" + 
":  " + 
"(b('gvhmean') <= -14.9026460647583) ? " + 
"-0.00937478462176867" + 
":  " + 
"-0.001574018443661226" + 
":  " + 
"(b('L8b6med') <= 2680.0) ? " + 
"(b('L8b6med') <= 2654.25) ? " + 
"0.0021991572145685545" + 
":  " + 
"0.01641120386463607" + 
":  " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"0.006037103938765897" + 
":  " + 
"-0.0005556929911945642" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 28.5) ? " + 
"(b('L8b3med') <= 864.5) ? " + 
"(b('ndvi_med') <= 2934.5) ? " + 
"9.892194604342041e-05" + 
":  " + 
"-0.007385146126807056" + 
":  " + 
"(b('gvhk2') <= 0.28085392713546753) ? " + 
"0.014179467961460107" + 
":  " + 
"0.0035066452305645424" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"(b('ndvi_med') <= 4268.0) ? " + 
"-0.002461291881994095" + 
":  " + 
"0.0172994998787791" + 
":  " + 
"(b('L8b3med') <= 1487.5) ? " + 
"0.000466938002162016" + 
":  " + 
"-0.0016435419877507142" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 41.426435470581055) ? " + 
"(b('L8b10med') <= 2154.0) ? " + 
"-0.0033725747932853564" + 
":  " + 
"0.0007369100823957386" + 
":  " + 
"(b('L8b10med') <= 2107.0) ? " + 
"0.008242962383549924" + 
":  " + 
"-0.0017053113346625027" + 
":  " + 
"(b('lat') <= 47.74028396606445) ? " + 
"(b('L8b10med') <= 1542.5) ? " + 
"0.004461177046673689" + 
":  " + 
"-0.0034054836570879977" + 
":  " + 
"(b('L8b10med') <= 1529.25) ? " + 
"-0.0019971019955488047" + 
":  " + 
"0.0015945964682778386" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"(b('bulk') <= 118.0) ? " + 
"0.007140716249646739" + 
":  " + 
"0.005607104360505488" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"(b('gvhk3') <= -0.00421099248342216) ? " + 
"0.001080494405048712" + 
":  " + 
"-0.0018764371191403078" + 
":  " + 
"(b('L8b6med') <= 2680.0) ? " + 
"0.003066205560385156" + 
":  " + 
"-0.00014464513093945537" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 39.927019119262695) ? " + 
"(b('L8b5med') <= 2197.0) ? " + 
"(b('bulk') <= 145.5) ? " + 
"0.017868095771517323" + 
":  " + 
"0.018851859737005233" + 
":  " + 
"(b('lat') <= 37.45932960510254) ? " + 
"-0.0007576476707222579" + 
":  " + 
"0.0026153129787308627" + 
":  " + 
"(b('lat') <= 41.189334869384766) ? " + 
"(b('lat') <= 40.97825622558594) ? " + 
"-0.005010195991603018" + 
":  " + 
"-0.021917734404737085" + 
":  " + 
"(b('lat') <= 41.222354888916016) ? " + 
"0.01694094179265916" + 
":  " + 
"-2.2470100293695447e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -112.57361602783203) ? " + 
"(b('lon') <= -115.51697540283203) ? " + 
"(b('gvhk3') <= 0.035602232441306114) ? " + 
"0.0006995457396172831" + 
":  " + 
"-0.004772735499788715" + 
":  " + 
"(b('gvvmean') <= -14.951804637908936) ? " + 
"0.024930779464857375" + 
":  " + 
"0.002904979459438966" + 
":  " + 
"(b('L8b10med') <= 3352.25) ? " + 
"(b('lon') <= -108.2274055480957) ? " + 
"-0.0036020172224319833" + 
":  " + 
"6.305282560394211e-05" + 
":  " + 
"(b('gvhmean') <= -12.147471904754639) ? " + 
"0.01086619153813722" + 
":  " + 
"0.0028906850915451365" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2381.0) ? " + 
"(b('bulk') <= 131.5) ? " + 
"(b('L8b5med') <= 1867.0) ? " + 
"0.00041007067028370203" + 
":  " + 
"-0.0064406014986714945" + 
":  " + 
"(b('gvvmean') <= -12.134212970733643) ? " + 
"-0.011065867452079312" + 
":  " + 
"0.0008609728935367586" + 
":  " + 
"(b('L8b6med') <= 2409.5) ? " + 
"(b('grass') <= 10.067039012908936) ? " + 
"0.01858839819777708" + 
":  " + 
"0.004603811887886914" + 
":  " + 
"(b('L8b6med') <= 2478.5) ? " + 
"-0.0031711339555263243" + 
":  " + 
"0.00020338344602272192" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 570.0) ? " + 
"(b('gvhmean') <= -14.234665393829346) ? " + 
"-0.0003409193179526593" + 
":  " + 
"(b('bulk') <= 123.0) ? " + 
"0.006250226244797069" + 
":  " + 
"0.005359449047476539" + 
":  " + 
"(b('L8b10med') <= 1516.75) ? " + 
"(b('gvvmean') <= -12.134212970733643) ? " + 
"-0.006849856119603287" + 
":  " + 
"2.6089656243123638e-05" + 
":  " + 
"(b('L8b10med') <= 1519.5) ? " + 
"0.01198438628747489" + 
":  " + 
"4.816306181755717e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1487.5) ? " + 
"(b('L8b3med') <= 1399.5) ? " + 
"(b('L8b3med') <= 1373.75) ? " + 
"-4.993917378760779e-05" + 
":  " + 
"-0.010507002467997437" + 
":  " + 
"(b('bare') <= 0.1420118361711502) ? " + 
"0.014632506169934008" + 
":  " + 
"0.002151550742200465" + 
":  " + 
"(b('sand') <= 40.5) ? " + 
"(b('gvhk3') <= 0.008353158191312104) ? " + 
"0.019691384272951196" + 
":  " + 
"0.0022179597158367426" + 
":  " + 
"(b('L8b3med') <= 1563.0) ? " + 
"-0.008491437129844449" + 
":  " + 
"-0.0012203058370819277" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('lon') <= 147.44310760498047) ? " + 
"-0.007695479214955392" + 
":  " + 
"(b('gvhmean') <= -15.758374214172363) ? " + 
"-0.003911047840814225" + 
":  " + 
"-0.003060149117410038" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"(b('L8b6med') <= 3622.25) ? " + 
"0.0022095435774753536" + 
":  " + 
"0.009971209719058988" + 
":  " + 
"(b('lon') <= 146.15660095214844) ? " + 
"4.5861158596253304e-05" + 
":  " + 
"-0.013683896204578716" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.11356435716152191) ? " + 
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('L8b5med') <= 2402.5) ? " + 
"-0.0009887641571610824" + 
":  " + 
"0.0031735218564907103" + 
":  " + 
"(b('L8b6med') <= 3691.5) ? " + 
"-0.004158542826769652" + 
":  " + 
"0.00033951022503606737" + 
":  " + 
"(b('gvhk2') <= 0.13928855955600739) ? " + 
"(b('L8b6med') <= 3994.0) ? " + 
"0.005138185066590687" + 
":  " + 
"-0.0030984095605782816" + 
":  " + 
"(b('L8b6med') <= 4153.5) ? " + 
"-0.00012168627007200191" + 
":  " + 
"0.006482111115902498" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.027968889102339745) ? " + 
"(b('gvhk3') <= 0.023529446683824062) ? " + 
"(b('gvhk2') <= 0.3871832937002182) ? " + 
"-0.0005125537933548294" + 
":  " + 
"0.0021603157937041587" + 
":  " + 
"(b('L8b3med') <= 901.5) ? " + 
"0.02216064085272204" + 
":  " + 
"0.005250536454779532" + 
":  " + 
"(b('gvhk3') <= 0.029254012741148472) ? " + 
"(b('L8b3med') <= 1405.0) ? " + 
"-0.020017847534324104" + 
":  " + 
"-0.00933271956175026" + 
":  " + 
"(b('lon') <= -119.46337890625) ? " + 
"-0.006253854343026026" + 
":  " + 
"0.0002734766434357097" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.015737397596240044) ? " + 
"(b('gvhmean') <= -13.97707462310791) ? " + 
"0.00388522727238641" + 
":  " + 
"0.013228449677900933" + 
":  " + 
"(b('grass') <= 43.48554611206055) ? " + 
"-0.0032649142794446894" + 
":  " + 
"0.0022023259950554874" + 
":  " + 
"(b('bulk') <= 123.5) ? " + 
"(b('gvhk3') <= 0.04640178522095084) ? " + 
"-0.00916206492208324" + 
":  " + 
"-0.00495981985964726" + 
":  " + 
"(b('lat') <= 43.976104736328125) ? " + 
"0.00042544912762917524" + 
":  " + 
"-0.000916640306907543" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 893.25) ? " + 
"(b('L8b3med') <= 855.0) ? " + 
"(b('bare') <= 2.9754223823547363) ? " + 
"0.00017648347137742495" + 
":  " + 
"-0.0065069716199145835" + 
":  " + 
"(b('lon') <= -120.41248321533203) ? " + 
"-0.011915597556697313" + 
":  " + 
"0.00694859384737787" + 
":  " + 
"(b('L8b3med') <= 997.5) ? " + 
"(b('bare') <= 11.304055213928223) ? " + 
"-0.004036546666588235" + 
":  " + 
"0.011118331941053817" + 
":  " + 
"(b('gvhk3') <= 0.08321710303425789) ? " + 
"0.00023245441006076504" + 
":  " + 
"0.01057742806824651" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -17.05683422088623) ? " + 
"(b('lat') <= 33.79914474487305) ? " + 
"-0.0073347552133814775" + 
":  " + 
"(b('sand') <= 51.5) ? " + 
"-0.00470090614716584" + 
":  " + 
"-0.0029775960851884734" + 
":  " + 
"(b('L8b3med') <= 1487.5) ? " + 
"(b('L8b3med') <= 1416.5) ? " + 
"-2.3545047266578918e-05" + 
":  " + 
"0.005404370077714395" + 
":  " + 
"(b('sand') <= 40.5) ? " + 
"0.007202488753558028" + 
":  " + 
"-0.0023380788479214457" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2473.75) ? " + 
"(b('L8b10med') <= 2397.25) ? " + 
"(b('L8b6med') <= 3602.0) ? " + 
"0.00025353588677132075" + 
":  " + 
"-0.0046899154867580395" + 
":  " + 
"(b('lon') <= -108.2667350769043) ? " + 
"0.002636660953978888" + 
":  " + 
"0.01675001036915412" + 
":  " + 
"(b('ndvi_med') <= 1685.0) ? " + 
"(b('ndvi_med') <= 1538.0) ? " + 
"-0.000600406273909367" + 
":  " + 
"0.005537904912122134" + 
":  " + 
"(b('L8b3med') <= 1173.0) ? " + 
"-0.000682133180182187" + 
":  " + 
"-0.012396595144297496" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3232.5) ? " + 
"(b('gvvmean') <= -10.222922801971436) ? " + 
"(b('L8b5med') <= 3115.5) ? " + 
"0.00043823634898234855" + 
":  " + 
"-0.004719907124484303" + 
":  " + 
"(b('crops') <= 65.67342758178711) ? " + 
"-0.004754413217823595" + 
":  " + 
"0.0007533992260771897" + 
":  " + 
"(b('gvhmean') <= -10.855828762054443) ? " + 
"(b('gvhk3') <= 0.018007025122642517) ? " + 
"0.00015351502456572262" + 
":  " + 
"-0.010160937176080707" + 
":  " + 
"(b('gvhk3') <= 0.02711830660700798) ? " + 
"0.009316385190219578" + 
":  " + 
"-0.004196048236871615" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 33.261295318603516) ? " + 
"(b('L8b5med') <= 2200.5) ? " + 
"0.015230828008854475" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"0.0011331411276739327" + 
":  " + 
"-0.007419332250999976" + 
":  " + 
"(b('lat') <= 34.940629959106445) ? " + 
"(b('lat') <= 34.521310806274414) ? " + 
"-0.00020087311754159808" + 
":  " + 
"0.008059913477535388" + 
":  " + 
"(b('L8b6med') <= 4103.5) ? " + 
"-0.00013222098871347874" + 
":  " + 
"0.005571340333010634" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.015737397596240044) ? " + 
"(b('gvhmean') <= -13.97707462310791) ? " + 
"0.003684065665995745" + 
":  " + 
"0.011845793262282356" + 
":  " + 
"(b('gvhk2') <= 0.26522815227508545) ? " + 
"0.0016885674920204144" + 
":  " + 
"-0.0036669878660912647" + 
":  " + 
"(b('bulk') <= 123.5) ? " + 
"(b('L8b3med') <= 716.75) ? " + 
"-0.008057474918649749" + 
":  " + 
"-0.004535086840797634" + 
":  " + 
"(b('gvhmean') <= -12.406572818756104) ? " + 
"-0.0005920704744318535" + 
":  " + 
"0.0005089370468779557" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('ndvi_med') <= 3821.25) ? " + 
"0.01671368448773078" + 
":  " + 
"-0.0054623592566001855" + 
":  " + 
"(b('L8b6med') <= 2241.0) ? " + 
"(b('L8b6med') <= 2154.25) ? " + 
"-0.0004940836638915799" + 
":  " + 
"-0.006258332130223093" + 
":  " + 
"(b('gvhk2') <= 0.6582140624523163) ? " + 
"-8.893467467027802e-06" + 
":  " + 
"0.003919395582828282" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 166.0) ? " + 
"(b('sand') <= 37.5) ? " + 
"-0.0010376241580391944" + 
":  " + 
"0.00019350471730655245" + 
":  " + 
"(b('ndvi_med') <= 1663.0) ? " + 
"0.007558504761112629" + 
":  " + 
"-0.0005154532273965173" + 
":  " + 
"-0.007838477891324164" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2473.75) ? " + 
"(b('L8b10med') <= 2397.25) ? " + 
"(b('L8b6med') <= 3602.0) ? " + 
"0.00023340109005744644" + 
":  " + 
"-0.004098076448003959" + 
":  " + 
"(b('gvhk3') <= 0.003014804795384407) ? " + 
"-0.00022797282753720256" + 
":  " + 
"0.009698686154385586" + 
":  " + 
"(b('L8b10med') <= 2822.25) ? " + 
"(b('L8b10med') <= 2738.5) ? " + 
"-0.0010658941391436059" + 
":  " + 
"-0.010046603518587766" + 
":  " + 
"(b('L8b10med') <= 2851.0) ? " + 
"0.010009646197381048" + 
":  " + 
"0.00026952132230415873" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 16.995849609375) ? " + 
"(b('L8b10med') <= 1928.0) ? " + 
"(b('lat') <= 43.732351303100586) ? " + 
"0.008570909987088385" + 
":  " + 
"-2.636028184776577e-05" + 
":  " + 
"(b('crops') <= 85.12629318237305) ? " + 
"-0.004549949836721382" + 
":  " + 
"0.0022563953527964015" + 
":  " + 
"(b('grass') <= 17.66968059539795) ? " + 
"(b('L8b6med') <= 3697.5) ? " + 
"0.022490847273567205" + 
":  " + 
"-0.00023289420087417578" + 
":  " + 
"(b('L8b3med') <= 1900.25) ? " + 
"0.0002331213913011037" + 
":  " + 
"-0.008394973205138274" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -112.57361602783203) ? " + 
"(b('gvhk3') <= -0.01524945255368948) ? " + 
"(b('gvvmean') <= -14.383522510528564) ? " + 
"-0.003097801089111979" + 
":  " + 
"-0.013412106449958829" + 
":  " + 
"(b('lon') <= -113.06564331054688) ? " + 
"0.0005942802636417567" + 
":  " + 
"0.02122319210108757" + 
":  " + 
"(b('L8b10med') <= 3352.25) ? " + 
"(b('lon') <= -108.2274055480957) ? " + 
"-0.003129791531817154" + 
":  " + 
"4.988071735767276e-05" + 
":  " + 
"(b('gvhk2') <= 0.13714973628520966) ? " + 
"0.001960690747091612" + 
":  " + 
"0.00953195077419073" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.027968889102339745) ? " + 
"(b('gvhk3') <= 0.023529446683824062) ? " + 
"(b('gvhk2') <= 0.3871832937002182) ? " + 
"-0.0004179846840709091" + 
":  " + 
"0.0019093406431839098" + 
":  " + 
"(b('lon') <= -115.55241012573242) ? " + 
"0.011241370804134329" + 
":  " + 
"0.0006594741074439532" + 
":  " + 
"(b('gvhk3') <= 0.028507420793175697) ? " + 
"-0.017278578223049693" + 
":  " + 
"(b('lon') <= -119.46337890625) ? " + 
"-0.005705789133407726" + 
":  " + 
"6.203491569791843e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.015737397596240044) ? " + 
"(b('gvvmean') <= -13.97707462310791) ? " + 
"0.0035039299998507745" + 
":  " + 
"0.010632910959605668" + 
":  " + 
"(b('L8b5med') <= 2287.5) ? " + 
"0.009946974261296579" + 
":  " + 
"-0.00010975546810920649" + 
":  " + 
"(b('lon') <= 9.146950244903564) ? " + 
"(b('lat') <= 32.43104076385498) ? " + 
"-0.007960585436711961" + 
":  " + 
"0.00028018081120013104" + 
":  " + 
"(b('L8b5med') <= 2201.5) ? " + 
"0.013690647318986837" + 
":  " + 
"-0.0018480144792461528" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -17.05683422088623) ? " + 
"(b('ndvi_med') <= 1242.5) ? " + 
"-0.002692260165749631" + 
":  " + 
"(b('L8b6med') <= 3267.5) ? " + 
"-0.004338324621906989" + 
":  " + 
"-0.005804583185633844" + 
":  " + 
"(b('gvvmean') <= -13.548450469970703) ? " + 
"(b('L8b3med') <= 934.5) ? " + 
"0.0029327273553245233" + 
":  " + 
"-0.00012000988882656635" + 
":  " + 
"(b('gvhmean') <= -13.340893745422363) ? " + 
"-0.00506865331833054" + 
":  " + 
"2.2101398976491653e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1125.75) ? " + 
"(b('bulk') <= 145.5) ? " + 
"(b('gvhk3') <= 0.006678904872387648) ? " + 
"-0.0008006580009731291" + 
":  " + 
"0.0019656378856498903" + 
":  " + 
"(b('sand') <= 41.5) ? " + 
"-0.004701165644126951" + 
":  " + 
"0.0003919602994707866" + 
":  " + 
"(b('L8b3med') <= 1208.0) ? " + 
"(b('gvhk3') <= -0.01524945255368948) ? " + 
"-0.009924695760848243" + 
":  " + 
"0.004969481760483933" + 
":  " + 
"(b('L8b3med') <= 1316.75) ? " + 
"-0.0034795833738932806" + 
":  " + 
"0.0007274335053104773" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.18267665803432465) ? " + 
"(b('gvhk3') <= 0.11796966567635536) ? " + 
"(b('gvhk3') <= 0.11459998413920403) ? " + 
"3.62827956342888e-05" + 
":  " + 
"-0.008691785220859498" + 
":  " + 
"(b('gvvmean') <= -15.606000900268555) ? " + 
"0.002554465884430715" + 
":  " + 
"0.007622337200676972" + 
":  " + 
"(b('bulk') <= 138.5) ? " + 
"(b('gvvmean') <= -8.461088180541992) ? " + 
"-0.002887054400580083" + 
":  " + 
"-0.00167073587626565" + 
":  " + 
"(b('L8b6med') <= 3660.5) ? " + 
"-0.004108450736710734" + 
":  " + 
"-0.005263320897017532" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 28.5) ? " + 
"(b('L8b6med') <= 2569.75) ? " + 
"(b('gvhmean') <= -10.128739356994629) ? " + 
"-0.004907860842160258" + 
":  " + 
"0.0006512394132455468" + 
":  " + 
"(b('gvhk2') <= 0.25576619803905487) ? " + 
"0.010148900055025611" + 
":  " + 
"0.0020883561515808737" + 
":  " + 
"(b('sand') <= 35.5) ? " + 
"(b('gvhk2') <= 0.21291857957839966) ? " + 
"-0.009049397000110034" + 
":  " + 
"-0.00027135729322221746" + 
":  " + 
"(b('gvhk2') <= 0.2062721624970436) ? " + 
"0.001268844133344732" + 
":  " + 
"-0.0002612884900619142" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('ndvi_med') <= 3821.25) ? " + 
"0.015111410031599826" + 
":  " + 
"-0.004847029338298031" + 
":  " + 
"(b('L8b6med') <= 2374.0) ? " + 
"(b('lon') <= -120.5117073059082) ? " + 
"0.005780728782393579" + 
":  " + 
"-0.0022130291525225727" + 
":  " + 
"(b('L8b6med') <= 2409.5) ? " + 
"0.004550250946960464" + 
":  " + 
"-6.366488408304663e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 146.23104858398438) ? " + 
"(b('lon') <= 87.17928886413574) ? " + 
"(b('lat') <= 32.43104076385498) ? " + 
"-0.00688475711897436" + 
":  " + 
"7.183998282996928e-05" + 
":  " + 
"(b('bulk') <= 146.0) ? " + 
"0.009677975861267035" + 
":  " + 
"0.0019174638146204903" + 
":  " + 
"(b('lat') <= -34.78766059875488) ? " + 
"(b('grass') <= 28.303702354431152) ? " + 
"0.007179187903667172" + 
":  " + 
"-0.001539291521872023" + 
":  " + 
"-0.017497686537338603" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.0070518004527418965" + 
":  " + 
"(b('lat') <= 39.55443000793457) ? " + 
"(b('L8b5med') <= 2377.25) ? " + 
"0.00546604210231368" + 
":  " + 
"-2.6785979868827186e-05" + 
":  " + 
"(b('lat') <= 41.189334869384766) ? " + 
"-0.003805941395255107" + 
":  " + 
"0.00012985761996875828" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 41.426435470581055) ? " + 
"(b('lat') <= 39.927019119262695) ? " + 
"0.0005199680672321779" + 
":  " + 
"-0.002701709521250096" + 
":  " + 
"(b('grass') <= 78.74732971191406) ? " + 
"0.004354581621069915" + 
":  " + 
"-0.006732095658007965" + 
":  " + 
"(b('L8b3med') <= 1204.5) ? " + 
"(b('L8b3med') <= 1079.0) ? " + 
"-0.0005472712817319002" + 
":  " + 
"0.0042140404274201675" + 
":  " + 
"(b('gvhk2') <= 0.29793746769428253) ? " + 
"-0.011832666529312814" + 
":  " + 
"-0.0022636946509867403" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1487.5) ? " + 
"(b('L8b3med') <= 1399.5) ? " + 
"(b('L8b3med') <= 1383.0) ? " + 
"-3.9251357355317105e-05" + 
":  " + 
"-0.013342351605168078" + 
":  " + 
"(b('bare') <= 0.1420118361711502) ? " + 
"0.01139521681447607" + 
":  " + 
"0.0015179818432612693" + 
":  " + 
"(b('L8b5med') <= 3040.0) ? " + 
"(b('grass') <= 55.38705825805664) ? " + 
"-0.0017752018866961914" + 
":  " + 
"-0.006843143583851455" + 
":  " + 
"(b('L8b5med') <= 3093.5) ? " + 
"0.009687466101120333" + 
":  " + 
"0.0003135550614522158" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.027968889102339745) ? " + 
"(b('gvhk3') <= 0.023529446683824062) ? " + 
"(b('gvhmean') <= -15.884497165679932) ? " + 
"0.004105451675034553" + 
":  " + 
"-0.00011990685798980607" + 
":  " + 
"(b('L8b3med') <= 901.5) ? " + 
"0.01764780431723359" + 
":  " + 
"0.0034154086185210486" + 
":  " + 
"(b('gvhk3') <= 0.029254012741148472) ? " + 
"(b('L8b6med') <= 3737.0) ? " + 
"-0.014556616997418934" + 
":  " + 
"-0.00724652489413595" + 
":  " + 
"(b('lon') <= -119.46337890625) ? " + 
"-0.005190717047747256" + 
":  " + 
"0.00011571409659131224" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.002807944343658164) ? " + 
"(b('grass') <= 42.485931396484375) ? " + 
"-0.004252039857627843" + 
":  " + 
"0.005448457697828146" + 
":  " + 
"(b('gvhk3') <= 0.008020753972232342) ? " + 
"-0.0017555919545118835" + 
":  " + 
"0.005041320624294354" + 
":  " + 
"(b('lat') <= 43.976104736328125) ? " + 
"(b('bulk') <= 128.5) ? " + 
"-0.005855195479556497" + 
":  " + 
"0.0005336496561444674" + 
":  " + 
"(b('gvhk3') <= 0.004092698101885617) ? " + 
"-0.002094943895319122" + 
":  " + 
"0.0005002948587717396" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.018644212745130062) ? " + 
"(b('gvhk2') <= 0.3871832937002182) ? " + 
"(b('gvhmean') <= -7.043510437011719) ? " + 
"-3.264216800581016e-05" + 
":  " + 
"-0.014374722989315775" + 
":  " + 
"(b('lat') <= 44.46230888366699) ? " + 
"0.006621059060712608" + 
":  " + 
"-0.0008923065635224652" + 
":  " + 
"(b('gvhk3') <= 0.021156606264412403) ? " + 
"(b('L8b5med') <= 2764.0) ? " + 
"-0.003375757815683072" + 
":  " + 
"-0.013621950828281992" + 
":  " + 
"(b('gvhk2') <= 0.4012780338525772) ? " + 
"0.0014439067957732854" + 
":  " + 
"-0.0015403728411831914" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 893.25) ? " + 
"(b('L8b3med') <= 849.5) ? " + 
"(b('bare') <= 2.9754223823547363) ? " + 
"0.00023401611799586295" + 
":  " + 
"-0.005139925653778812" + 
":  " + 
"(b('bulk') <= 145.5) ? " + 
"0.0066091738669012716" + 
":  " + 
"-0.0008521361895426516" + 
":  " + 
"(b('L8b3med') <= 997.5) ? " + 
"(b('bare') <= 10.462992668151855) ? " + 
"-0.0034314932878016726" + 
":  " + 
"0.00771822591488158" + 
":  " + 
"(b('gvhk3') <= 0.08321710303425789) ? " + 
"0.0001228936229105723" + 
":  " + 
"0.008510475818110985" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 33.261295318603516) ? " + 
"(b('gvhk3') <= 0.01707080751657486) ? " + 
"(b('sand') <= 57.0) ? " + 
"-0.01474009755511474" + 
":  " + 
"-0.004933888786067958" + 
":  " + 
"(b('ndvi_med') <= 1543.5) ? " + 
"-0.009517333768006356" + 
":  " + 
"0.0014440002096857002" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"(b('lon') <= 22.9816255569458) ? " + 
"0.00010293003765581804" + 
":  " + 
"0.003753402791278466" + 
":  " + 
"(b('bare') <= 4.019245982170105) ? " + 
"-0.0009955599783298987" + 
":  " + 
"-0.004994740867070826" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -16.209970474243164) ? " + 
"(b('L8b5med') <= 2797.0) ? " + 
"(b('lon') <= -118.50161361694336) ? " + 
"0.006267682226324192" + 
":  " + 
"-0.002027899210113686" + 
":  " + 
"-0.010456476677942694" + 
":  " + 
"(b('gvvmean') <= -15.980653285980225) ? " + 
"(b('L8b10med') <= 2201.0) ? " + 
"0.00886665157387112" + 
":  " + 
"0.00137932488422092" + 
":  " + 
"(b('gvhmean') <= -12.406572818756104) ? " + 
"-0.00045513753184943666" + 
":  " + 
"0.0004476384771746789" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"0.005255672219911384" + 
":  " + 
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('lat') <= 55.93754959106445) ? " + 
"7.624053056957764e-05" + 
":  " + 
"-0.0016590505327290991" + 
":  " + 
"(b('L8b3med') <= 686.0) ? " + 
"0.0010567010061769133" + 
":  " + 
"0.005529282840869662" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 893.25) ? " + 
"(b('L8b3med') <= 849.5) ? " + 
"(b('bare') <= 2.9754223823547363) ? " + 
"0.0001899149034345288" + 
":  " + 
"-0.0044587043835012455" + 
":  " + 
"(b('lon') <= -120.41248321533203) ? " + 
"-0.008662545971784216" + 
":  " + 
"0.004904250213359506" + 
":  " + 
"(b('L8b10med') <= 1675.25) ? " + 
"(b('ndvi_med') <= 3315.5) ? " + 
"-0.011974720912155512" + 
":  " + 
"-0.00945627824518222" + 
":  " + 
"(b('gvhk2') <= 0.6108855605125427) ? " + 
"-9.04491118052968e-05" + 
":  " + 
"-0.006994148971315492" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -16.209970474243164) ? " + 
"(b('L8b5med') <= 2797.0) ? " + 
"(b('lon') <= -118.50161361694336) ? " + 
"0.00564233486181534" + 
":  " + 
"-0.0019170499097566516" + 
":  " + 
"-0.009409408152024845" + 
":  " + 
"(b('gvvmean') <= -15.933977127075195) ? " + 
"(b('L8b5med') <= 2358.0) ? " + 
"0.0007695578083652954" + 
":  " + 
"0.0072976497388118275" + 
":  " + 
"(b('lat') <= 33.261295318603516) ? " + 
"-0.001951822872718045" + 
":  " + 
"8.540638870928139e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3232.5) ? " + 
"(b('gvhk3') <= -0.0020414553000591695) ? " + 
"(b('ndvi_med') <= 1890.5) ? " + 
"-0.004308722905771794" + 
":  " + 
"1.3671462775381726e-05" + 
":  " + 
"(b('gvvmean') <= -10.195457458496094) ? " + 
"0.0005218698005679555" + 
":  " + 
"-0.0021654932241210664" + 
":  " + 
"(b('gvhmean') <= -10.855828762054443) ? " + 
"(b('gvhk3') <= 0.018007025122642517) ? " + 
"8.22828265150311e-05" + 
":  " + 
"-0.007927094133126998" + 
":  " + 
"(b('gvhk3') <= 0.02711830660700798) ? " + 
"0.0075202853776145" + 
":  " + 
"-0.003439614003862985" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 166.0) ? " + 
"(b('L8b3med') <= 893.25) ? " + 
"0.0004868999386293101" + 
":  " + 
"-0.0003544683151499817" + 
":  " + 
"(b('crops') <= 49.58632469177246) ? " + 
"0.0068147227817517" + 
":  " + 
"3.3432230838653654e-05" + 
":  " + 
"-0.006777219015013131" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 570.0) ? " + 
"(b('gvhmean') <= -14.234665393829346) ? " + 
"-0.0008288745058168678" + 
":  " + 
"0.004693762995500801" + 
":  " + 
"(b('L8b3med') <= 615.5) ? " + 
"(b('lat') <= 53.60642433166504) ? " + 
"-0.007112677242215353" + 
":  " + 
"0.0008126268660857694" + 
":  " + 
"(b('L8b3med') <= 619.0) ? " + 
"0.011049010584235741" + 
":  " + 
"3.0122228500561855e-07" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvvmean') <= -11.045052528381348) ? " + 
"-0.00431361635041011" + 
":  " + 
"0.013699798916277206" + 
":  " + 
"(b('L8b3med') <= 761.5) ? " + 
"(b('ndvi_med') <= 4096.5) ? " + 
"8.880011155925132e-05" + 
":  " + 
"-0.0037252228527636286" + 
":  " + 
"(b('L8b3med') <= 795.5) ? " + 
"0.003561021730273616" + 
":  " + 
"-4.5673468406131354e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -5.297438144683838) ? " + 
"(b('gvhmean') <= -6.832682847976685) ? " + 
"(b('crops') <= 89.04487609863281) ? " + 
"0.00011832188403621658" + 
":  " + 
"-0.001785167606823812" + 
":  " + 
"(b('gvhmean') <= -6.493995904922485) ? " + 
"-0.012922856145136663" + 
":  " + 
"-0.0019643424953228648" + 
":  " + 
"(b('ndvi_med') <= 4110.5) ? " + 
"(b('L8b10med') <= 2168.5) ? " + 
"0.004023927668092175" + 
":  " + 
"0.005451314410381158" + 
":  " + 
"(b('ndvi_med') <= 5067.5) ? " + 
"0.0021782925420869015" + 
":  " + 
"0.0011647012348721675" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 28.5) ? " + 
"(b('L8b3med') <= 864.5) ? " + 
"(b('gvhk3') <= -0.006902431370690465) ? " + 
"-0.006827768398952744" + 
":  " + 
"-0.0001837141652023295" + 
":  " + 
"(b('gvhk3') <= 0.015396119095385075) ? " + 
"0.0049559139370044724" + 
":  " + 
"0.00011819199886863724" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"(b('ndvi_med') <= 4268.0) ? " + 
"-0.0015158343318857038" + 
":  " + 
"0.0126906417650402" + 
":  " + 
"(b('gvhk2') <= 0.2010231539607048) ? " + 
"0.0012311918121077929" + 
":  " + 
"-0.00019261585512304872" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1207.25) ? " + 
"(b('bare') <= 1.7483659982681274) ? " + 
"(b('L8b3med') <= 1301.0) ? " + 
"0.0015569944600633129" + 
":  " + 
"0.009116312664550583" + 
":  " + 
"(b('ndvi_med') <= 1146.25) ? " + 
"-0.0008811079573931602" + 
":  " + 
"-0.007146277387970151" + 
":  " + 
"(b('bare') <= 25.768656730651855) ? " + 
"(b('lat') <= 39.927019119262695) ? " + 
"0.0009000776799079419" + 
":  " + 
"-0.0003515610268314709" + 
":  " + 
"(b('gvvmean') <= -11.365689754486084) ? " + 
"0.011299661781135303" + 
":  " + 
"0.0006547564846836329" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 33.261295318603516) ? " + 
"(b('bulk') <= 147.5) ? " + 
"(b('ndvi_med') <= 2233.0) ? " + 
"0.003813396915778708" + 
":  " + 
"-0.0018782190685002417" + 
":  " + 
"(b('L8b6med') <= 3548.0) ? " + 
"-0.009267248187052863" + 
":  " + 
"-0.001899344915663334" + 
":  " + 
"(b('lat') <= 34.940629959106445) ? " + 
"(b('lat') <= 34.521310806274414) ? " + 
"-0.0002782572007817336" + 
":  " + 
"0.006317261962726767" + 
":  " + 
"(b('L8b10med') <= 3352.25) ? " + 
"-0.00010531269907912992" + 
":  " + 
"0.004028002649746634" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 893.25) ? " + 
"(b('L8b3med') <= 849.5) ? " + 
"(b('bare') <= 2.9754223823547363) ? " + 
"0.0001915617850352398" + 
":  " + 
"-0.004036826461818499" + 
":  " + 
"(b('bulk') <= 145.5) ? " + 
"0.005376541022949928" + 
":  " + 
"-0.000856807054040648" + 
":  " + 
"(b('L8b3med') <= 997.5) ? " + 
"(b('bare') <= 11.304055213928223) ? " + 
"-0.00280149886212344" + 
":  " + 
"0.007922702737169357" + 
":  " + 
"(b('gvhk2') <= 0.4450976401567459) ? " + 
"-0.00018288920082976405" + 
":  " + 
"0.0033560970191612327" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -17.05683422088623) ? " + 
"(b('bare') <= 13.214245796203613) ? " + 
"(b('L8b5med') <= 2469.0) ? " + 
"-0.0022260292548559324" + 
":  " + 
"-0.0032701175245869046" + 
":  " + 
"-0.005885393551648854" + 
":  " + 
"(b('L8b3med') <= 1487.5) ? " + 
"(b('L8b3med') <= 1399.5) ? " + 
"-2.1646364202563526e-05" + 
":  " + 
"0.0036200741663369343" + 
":  " + 
"(b('L8b5med') <= 3040.0) ? " + 
"-0.0031027217128684493" + 
":  " + 
"0.0013501182071559827" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2545.5) ? " + 
"(b('L8b3med') <= 1133.0) ? " + 
"(b('lon') <= -120.94869613647461) ? " + 
"-0.006949802553814326" + 
":  " + 
"-2.83902368818013e-05" + 
":  " + 
"(b('L8b5med') <= 3177.0) ? " + 
"0.002187454126789379" + 
":  " + 
"-0.009891045027300177" + 
":  " + 
"(b('L8b10med') <= 2822.25) ? " + 
"(b('crops') <= 78.07051467895508) ? " + 
"-0.001378987979265631" + 
":  " + 
"-0.011904106802036128" + 
":  " + 
"(b('L8b10med') <= 2851.0) ? " + 
"0.007723318056803814" + 
":  " + 
"4.2985844140211164e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3232.5) ? " + 
"(b('L8b5med') <= 3213.5) ? " + 
"(b('gvhk2') <= 0.35234180092811584) ? " + 
"-0.0005482339293297848" + 
":  " + 
"0.0007115126443869067" + 
":  " + 
"(b('gvhk3') <= 0.03051651269197464) ? " + 
"-0.009905601090138133" + 
":  " + 
"0.0031128076121813286" + 
":  " + 
"(b('gvhk3') <= -0.0011066314182244241) ? " + 
"(b('L8b3med') <= 1075.5) ? " + 
"0.0022082568043551493" + 
":  " + 
"0.011855981859474568" + 
":  " + 
"(b('crops') <= 81.04289245605469) ? " + 
"-0.0019478376494327988" + 
":  " + 
"0.009163308170664478" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2473.75) ? " + 
"(b('L8b10med') <= 2397.25) ? " + 
"(b('gvhk3') <= 0.06370549276471138) ? " + 
"0.00028805880897949917" + 
":  " + 
"-0.0018116696117905116" + 
":  " + 
"(b('lon') <= -108.2667350769043) ? " + 
"0.001385861184409803" + 
":  " + 
"0.011555958194409258" + 
":  " + 
"(b('ndvi_med') <= 1685.0) ? " + 
"(b('ndvi_med') <= 1538.0) ? " + 
"-0.00048740793839471174" + 
":  " + 
"0.004059539853734127" + 
":  " + 
"(b('L8b3med') <= 1173.0) ? " + 
"-0.0005358992099852738" + 
":  " + 
"-0.008595579044437873" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -12.406572818756104) ? " + 
"(b('L8b6med') <= 2448.5) ? " + 
"(b('gvhk3') <= 0.013427001889795065) ? " + 
"-0.004962129654505414" + 
":  " + 
"-0.012735991247298878" + 
":  " + 
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"-0.0010805532617427565" + 
":  " + 
"0.0008667335693956806" + 
":  " + 
"(b('gvhmean') <= -11.956430435180664) ? " + 
"(b('ndvi_med') <= 1491.0) ? " + 
"-2.695276661181245e-05" + 
":  " + 
"0.00900563475500366" + 
":  " + 
"(b('L8b10med') <= 1928.0) ? " + 
"0.0007964193326408283" + 
":  " + 
"-0.0013091923435779888" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -16.209970474243164) ? " + 
"(b('L8b5med') <= 2797.0) ? " + 
"(b('lon') <= -118.50161361694336) ? " + 
"0.004819852095220484" + 
":  " + 
"-0.0016367664726227033" + 
":  " + 
"-0.008859981063733119" + 
":  " + 
"(b('gvvmean') <= -15.980653285980225) ? " + 
"(b('L8b5med') <= 2343.0) ? " + 
"0.0013404492193977713" + 
":  " + 
"0.0070865298256220415" + 
":  " + 
"(b('gvhk2') <= 0.3535355180501938) ? " + 
"-0.0003245626606748456" + 
":  " + 
"0.0005541701095408974" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 33.261295318603516) ? " + 
"(b('bulk') <= 147.5) ? " + 
"(b('sand') <= 54.5) ? " + 
"0.005742341116068375" + 
":  " + 
"-0.0007594862847472387" + 
":  " + 
"(b('L8b3med') <= 905.0) ? " + 
"0.0011008708582511198" + 
":  " + 
"-0.0065328433660754555" + 
":  " + 
"(b('lat') <= 34.940629959106445) ? " + 
"(b('lat') <= 34.521310806274414) ? " + 
"-3.1289720087167924e-05" + 
":  " + 
"0.0057234884591093995" + 
":  " + 
"(b('L8b10med') <= 3352.25) ? " + 
"-9.896156954880954e-05" + 
":  " + 
"0.0035092867386909226" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2061.5) ? " + 
"(b('ndvi_med') <= 1591.25) ? " + 
"(b('gvhmean') <= -13.502954959869385) ? " + 
"0.002804032221398925" + 
":  " + 
"0.00615189406693017" + 
":  " + 
"(b('L8b3med') <= 778.0) ? " + 
"0.0018614629255791176" + 
":  " + 
"-0.0032765277690291715" + 
":  " + 
"(b('L8b5med') <= 2216.25) ? " + 
"(b('L8b5med') <= 2180.0) ? " + 
"-0.0004205356522143216" + 
":  " + 
"-0.010475188050737648" + 
":  " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"0.0005627143688524314" + 
":  " + 
"-0.0006956984982198549" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1487.5) ? " + 
"(b('L8b3med') <= 1399.5) ? " + 
"(b('L8b3med') <= 1383.0) ? " + 
"3.1588293389722393e-06" + 
":  " + 
"-0.011780934285671597" + 
":  " + 
"(b('L8b10med') <= 2943.75) ? " + 
"0.0054788434689144695" + 
":  " + 
"-0.002726628716176469" + 
":  " + 
"(b('sand') <= 40.5) ? " + 
"(b('L8b5med') <= 3134.0) ? " + 
"0.012397618168202867" + 
":  " + 
"0.000824528017625531" + 
":  " + 
"(b('bare') <= 72.05937194824219) ? " + 
"-0.0029749133694666552" + 
":  " + 
"0.0010637057361714938" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 893.25) ? " + 
"(b('L8b6med') <= 2854.5) ? " + 
"(b('gvhk3') <= 0.006678904872387648) ? " + 
"-0.0010658043296402975" + 
":  " + 
"0.0019233118630878445" + 
":  " + 
"(b('lon') <= -39.862648248672485) ? " + 
"0.00040511184366810575" + 
":  " + 
"0.007627780276988548" + 
":  " + 
"(b('L8b10med') <= 1675.25) ? " + 
"(b('gvhk3') <= 0.02111726999282837) ? " + 
"-0.010081720991924059" + 
":  " + 
"-0.0074961947914611166" + 
":  " + 
"(b('L8b3med') <= 1001.75) ? " + 
"-0.001361103710198771" + 
":  " + 
"0.00022015367389666105" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.017636760137975216) ? " + 
"(b('gvhk3') <= 0.016927449963986874) ? " + 
"(b('gvhk3') <= 0.015915646217763424) ? " + 
"0.00019411133627148295" + 
":  " + 
"-0.0065394096433265695" + 
":  " + 
"(b('lat') <= 36.20848846435547) ? " + 
"0.011623638446311382" + 
":  " + 
"0.006381677584977559" + 
":  " + 
"(b('bare') <= 14.208101749420166) ? " + 
"(b('bare') <= 12.266788005828857) ? " + 
"-0.0005453499163779044" + 
":  " + 
"0.008954216814957953" + 
":  " + 
"(b('grass') <= 57.7474250793457) ? " + 
"-0.0012856381527998704" + 
":  " + 
"-0.005761159207809559" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvvmean') <= -11.045052528381348) ? " + 
"-0.0036981391960462517" + 
":  " + 
"0.012513934543972344" + 
":  " + 
"(b('L8b3med') <= 557.5) ? " + 
"(b('grass') <= 54.9877986907959) ? " + 
"0.003973000491839185" + 
":  " + 
"0.004659747450115992" + 
":  " + 
"(b('L8b3med') <= 761.5) ? " + 
"-0.000924384899174016" + 
":  " + 
"0.00012120443497139321" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('grass') <= 17.183883666992188) ? " + 
"(b('L8b10med') <= 1928.0) ? " + 
"0.0008273258921072053" + 
":  " + 
"-0.0018572596506020347" + 
":  " + 
"(b('grass') <= 17.66968059539795) ? " + 
"0.016976954008831813" + 
":  " + 
"9.702731648315977e-05" + 
":  " + 
"(b('gvhk3') <= -0.35762954503297806) ? " + 
"0.0010776143998775523" + 
":  " + 
"(b('L8b6med') <= 2423.0) ? " + 
"0.005923869380441593" + 
":  " + 
"0.003563997946518488" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 166.0) ? " + 
"(b('L8b6med') <= 3379.0) ? " + 
"(b('L8b6med') <= 3371.5) ? " + 
"0.00011249072796738063" + 
":  " + 
"0.00805039650589779" + 
":  " + 
"(b('gvvmean') <= -10.163280963897705) ? " + 
"-0.0008104667450799412" + 
":  " + 
"0.015279258607948626" + 
":  " + 
"(b('gvhk2') <= 0.2414945811033249) ? " + 
"(b('gvvmean') <= -13.868578433990479) ? " + 
"0.0002291947963950075" + 
":  " + 
"-0.0047994578583308856" + 
":  " + 
"(b('L8b10med') <= 2364.0) ? " + 
"0.008460712476427282" + 
":  " + 
"0.004705317067631547" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -5.297438144683838) ? " + 
"(b('gvhmean') <= -6.832682847976685) ? " + 
"(b('L8b5med') <= 2216.25) ? " + 
"-0.0009270898744319708" + 
":  " + 
"0.00015901268881760472" + 
":  " + 
"(b('gvvmean') <= -6.493995904922485) ? " + 
"-0.011257133903216837" + 
":  " + 
"-0.0014853581063065853" + 
":  " + 
"(b('gvhmean') <= -4.673092842102051) ? " + 
"(b('L8b6med') <= 2396.0) ? " + 
"0.000958603887093068" + 
":  " + 
"0.0027442301075202152" + 
":  " + 
"0.005192438951995587" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2061.5) ? " + 
"(b('L8b3med') <= 927.5) ? " + 
"(b('L8b3med') <= 778.0) ? " + 
"0.0017659500666560221" + 
":  " + 
"-0.0028695011896008645" + 
":  " + 
"(b('gvvmean') <= -13.502954959869385) ? " + 
"0.00257849641744181" + 
":  " + 
"0.005684664883148796" + 
":  " + 
"(b('L8b5med') <= 2068.5) ? " + 
"(b('L8b10med') <= 2015.0) ? " + 
"-0.01010535391170636" + 
":  " + 
"-0.00234538747204642" + 
":  " + 
"(b('L8b3med') <= 935.5) ? " + 
"0.000483426125813529" + 
":  " + 
"-0.0003966341094450415" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 27.5) ? " + 
"(b('gvhk2') <= 0.25576619803905487) ? " + 
"(b('gvvmean') <= -11.864870071411133) ? " + 
"0.008553534392839929" + 
":  " + 
"0.003749623072122704" + 
":  " + 
"(b('L8b5med') <= 3191.5) ? " + 
"0.001321999944199592" + 
":  " + 
"-0.004465177524020043" + 
":  " + 
"(b('L8b5med') <= 2061.5) ? " + 
"(b('L8b10med') <= 1822.0) ? " + 
"-0.00023255754369070486" + 
":  " + 
"0.003596091039677937" + 
":  " + 
"(b('L8b5med') <= 2216.25) ? " + 
"-0.001973290636216983" + 
":  " + 
"1.1479945139645826e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 570.0) ? " + 
"(b('gvhk3') <= 0.008902890840545297) ? " + 
"(b('lon') <= 16.02862024307251) ? " + 
"0.0034893567622331645" + 
":  " + 
"0.004345888449330371" + 
":  " + 
"-0.0010844477149143383" + 
":  " + 
"(b('L8b3med') <= 615.5) ? " + 
"(b('crops') <= 29.969650268554688) ? " + 
"-0.006012418850516177" + 
":  " + 
"0.0007624813817012743" + 
":  " + 
"(b('L8b3med') <= 619.0) ? " + 
"0.00944377864224999" + 
":  " + 
"-1.0601262051472346e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3232.5) ? " + 
"(b('gvhk3') <= -0.0025061245542019606) ? " + 
"(b('ndvi_med') <= 1890.5) ? " + 
"-0.004050372942712124" + 
":  " + 
"2.096784368560388e-05" + 
":  " + 
"(b('gvhmean') <= -13.692728042602539) ? " + 
"0.0011948679333380243" + 
":  " + 
"-0.0003078837297050397" + 
":  " + 
"(b('gvhk3') <= 0.02711830660700798) ? " + 
"(b('L8b5med') <= 3308.0) ? " + 
"0.007292757010635725" + 
":  " + 
"0.0005305692668659843" + 
":  " + 
"(b('lat') <= 48.73336410522461) ? " + 
"-0.006467462463394792" + 
":  " + 
"-0.00032157096463653057" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 166.0) ? " + 
"(b('gvhk2') <= 0.2732113152742386) ? " + 
"(b('L8b10med') <= 1112.5) ? " + 
"0.011101176779842542" + 
":  " + 
"0.00030961917948521946" + 
":  " + 
"(b('gvhk2') <= 0.2869482487440109) ? " + 
"-0.003952925522483385" + 
":  " + 
"7.35688618936262e-05" + 
":  " + 
"(b('gvhk2') <= 0.2414945811033249) ? " + 
"(b('bare') <= 12.5) ? " + 
"0.00010950868359099752" + 
":  " + 
"-0.004266003539357993" + 
":  " + 
"(b('L8b6med') <= 3458.0) ? " + 
"0.008042398683225066" + 
":  " + 
"0.004475418354658547" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -16.209970474243164) ? " + 
"(b('gvhk2') <= 0.537092536687851) ? " + 
"(b('bare') <= 15.181381702423096) ? " + 
"-0.0015089991040517737" + 
":  " + 
"0.004181244170066878" + 
":  " + 
"-0.00751147358682408" + 
":  " + 
"(b('gvhmean') <= -15.980653285980225) ? " + 
"(b('L8b10med') <= 2201.0) ? " + 
"0.006245425594149044" + 
":  " + 
"0.0014290067361521913" + 
":  " + 
"(b('gvhk2') <= 0.3535355180501938) ? " + 
"-0.00027180189902421196" + 
":  " + 
"0.0004633261875581697" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 33.261295318603516) ? " + 
"(b('gvhk3') <= 0.01707080751657486) ? " + 
"(b('gvhk3') <= 0.008133047660521697) ? " + 
"-0.0036804209950444255" + 
":  " + 
"-0.009791484381197816" + 
":  " + 
"(b('ndvi_med') <= 1543.5) ? " + 
"-0.0070091239706102995" + 
":  " + 
"0.0009577307140238809" + 
":  " + 
"(b('lat') <= 34.940629959106445) ? " + 
"(b('lat') <= 34.521310806274414) ? " + 
"-1.8773575631831678e-05" + 
":  " + 
"0.004868838707854629" + 
":  " + 
"(b('grass') <= 21.1055850982666) ? " + 
"-0.0006989520472237193" + 
":  " + 
"0.00024617424929403446" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -12.406572818756104) ? " + 
"(b('L8b6med') <= 2448.5) ? " + 
"(b('lat') <= 49.89837646484375) ? " + 
"-0.004085597868412323" + 
":  " + 
"-0.011617772939139431" + 
":  " + 
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"-0.0008969766039366382" + 
":  " + 
"0.0006662111032599773" + 
":  " + 
"(b('gvvmean') <= -11.956430435180664) ? " + 
"(b('gvhk2') <= 0.3025819957256317) ? " + 
"0.006224508627008878" + 
":  " + 
"-0.001358085380568139" + 
":  " + 
"(b('gvvmean') <= -11.933264255523682) ? " + 
"-0.010496456121500096" + 
":  " + 
"-6.102294315930238e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('L8b6med') <= 3834.0) ? " + 
"-0.004657263929032332" + 
":  " + 
"-0.0025184021568410084" + 
":  " + 
"(b('gvvmean') <= -16.209970474243164) ? " + 
"(b('L8b5med') <= 2797.0) ? " + 
"-0.000990933267993245" + 
":  " + 
"-0.006851564763397072" + 
":  " + 
"(b('gvhmean') <= -15.980653285980225) ? " + 
"0.003863560175386255" + 
":  " + 
"3.268470016164809e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.017636760137975216) ? " + 
"(b('gvhk3') <= 0.016927449963986874) ? " + 
"(b('gvhk3') <= 0.015915646217763424) ? " + 
"0.00016900730386240178" + 
":  " + 
"-0.005624046776904045" + 
":  " + 
"(b('grass') <= 77.68656539916992) ? " + 
"0.005284360146012269" + 
":  " + 
"0.01007747447842379" + 
":  " + 
"(b('L8b3med') <= 934.5) ? " + 
"(b('L8b3med') <= 933.0) ? " + 
"0.0005142197290527688" + 
":  " + 
"0.02150439418452313" + 
":  " + 
"(b('crops') <= 87.49077224731445) ? " + 
"-0.0017264582426827866" + 
":  " + 
"0.004784668991275821" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.005342131273723353" + 
":  " + 
"(b('L8b3med') <= 1125.75) ? " + 
"(b('L8b3med') <= 934.5) ? " + 
"0.0002696667859276573" + 
":  " + 
"-0.0010016080292176855" + 
":  " + 
"(b('L8b3med') <= 1169.75) ? " + 
"0.004163669832288341" + 
":  " + 
"1.6662253250409786e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 6045.25) ? " + 
"(b('ndvi_med') <= 5188.0) ? " + 
"(b('ndvi_med') <= 4777.75) ? " + 
"-8.19948523520649e-05" + 
":  " + 
"0.004681493486261373" + 
":  " + 
"(b('gvhk3') <= -0.012432136572897434) ? " + 
"0.001961666318554267" + 
":  " + 
"-0.003733751628913179" + 
":  " + 
"(b('gvvmean') <= -13.779605865478516) ? " + 
"(b('grass') <= 44.59784507751465) ? " + 
"-0.002011172628291554" + 
":  " + 
"0.004308225661562665" + 
":  " + 
"0.010765841439131618" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3232.5) ? " + 
"(b('grass') <= 19.320551872253418) ? " + 
"(b('gvhk2') <= 0.35624825954437256) ? " + 
"-0.0024736160588234714" + 
":  " + 
"0.00012358060691144672" + 
":  " + 
"(b('gvhk3') <= -0.0020414553000591695) ? " + 
"-0.001156148151458985" + 
":  " + 
"0.0004587373685656645" + 
":  " + 
"(b('gvhk3') <= 0.02711830660700798) ? " + 
"(b('crops') <= 66.23950004577637) ? " + 
"0.00016633170527791696" + 
":  " + 
"0.005385226681203571" + 
":  " + 
"(b('gvhk3') <= 0.07929259538650513) ? " + 
"-0.005647961987405103" + 
":  " + 
"-0.000916917038756182" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 166.0) ? " + 
"(b('bulk') <= 163.5) ? " + 
"(b('lon') <= -120.42640686035156) ? " + 
"0.0014510988992342555" + 
":  " + 
"-7.521822086291259e-05" + 
":  " + 
"(b('L8b6med') <= 3167.0) ? " + 
"-0.010751249182508329" + 
":  " + 
"-0.00018432076450993853" + 
":  " + 
"(b('gvhk2') <= 0.2414945811033249) ? " + 
"(b('gvhk3') <= 0.007996083237230778) ? " + 
"0.0005190565356404525" + 
":  " + 
"-0.003515278854502993" + 
":  " + 
"(b('L8b10med') <= 2364.0) ? " + 
"0.007377906372450033" + 
":  " + 
"0.003721295006098961" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.002807944343658164) ? " + 
"(b('sand') <= 64.5) ? " + 
"0.00198692466981434" + 
":  " + 
"0.007870845880704191" + 
":  " + 
"(b('gvhk3') <= 0.008020753972232342) ? " + 
"-0.0014134559990925273" + 
":  " + 
"0.0037830344241886332" + 
":  " + 
"(b('bulk') <= 123.5) ? " + 
"(b('L8b3med') <= 716.75) ? " + 
"-0.0054668638305954975" + 
":  " + 
"-0.0030379018040029016" + 
":  " + 
"(b('lat') <= 43.65060043334961) ? " + 
"0.00028385215416772526" + 
":  " + 
"-0.0005049568940859612" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 27.5) ? " + 
"(b('L8b3med') <= 864.5) ? " + 
"(b('gvhk3') <= -0.001660263689700514) ? " + 
"-0.0021377754122216784" + 
":  " + 
"0.0011680320271936669" + 
":  " + 
"(b('gvhk3') <= 0.015396119095385075) ? " + 
"0.005176898091201027" + 
":  " + 
"-0.00023090609720155184" + 
":  " + 
"(b('L8b5med') <= 2061.5) ? " + 
"(b('L8b10med') <= 1822.0) ? " + 
"-0.00016638007204179982" + 
":  " + 
"0.0032851446125037576" + 
":  " + 
"(b('L8b5med') <= 2216.25) ? " + 
"-0.0018102316021383691" + 
":  " + 
"9.600597307947303e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvvmean') <= -11.045052528381348) ? " + 
"-0.003100993027081639" + 
":  " + 
"0.010354227389801157" + 
":  " + 
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('gvhk3') <= -0.006239350885152817) ? " + 
"-0.0008445797277584338" + 
":  " + 
"0.00010306640385138845" + 
":  " + 
"(b('gvhk3') <= -0.35762954503297806) ? " + 
"-0.0002611471268767207" + 
":  " + 
"0.004518992038439626" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.017636760137975216) ? " + 
"(b('gvhk3') <= 0.016927449963986874) ? " + 
"(b('gvhk3') <= 0.015915646217763424) ? " + 
"0.0001625690486964586" + 
":  " + 
"-0.0051500475641941" + 
":  " + 
"(b('lat') <= 36.20848846435547) ? " + 
"0.009100083488435398" + 
":  " + 
"0.004508503430258363" + 
":  " + 
"(b('L8b5med') <= 3021.0) ? " + 
"(b('bare') <= 14.208101749420166) ? " + 
"0.0004495786464000791" + 
":  " + 
"-0.0032422070041506603" + 
":  " + 
"(b('bulk') <= 152.0) ? " + 
"-0.004996095863054634" + 
":  " + 
"0.002217574688239625" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 146.23104858398438) ? " + 
"(b('lat') <= -4.096814155578613) ? " + 
"(b('crops') <= 31.451263427734375) ? " + 
"0.0065965302794140646" + 
":  " + 
"0.0023227310085142255" + 
":  " + 
"(b('lat') <= 32.43104076385498) ? " + 
"-0.003709729683283152" + 
":  " + 
"5.152241403521032e-05" + 
":  " + 
"(b('lat') <= -34.78766059875488) ? " + 
"(b('lat') <= -35.233184814453125) ? " + 
"-0.0023488178373534552" + 
":  " + 
"0.0015174374714291075" + 
":  " + 
"-0.01147116978293139" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 570.0) ? " + 
"(b('gvhmean') <= -14.234665393829346) ? " + 
"-0.001299886242468018" + 
":  " + 
"(b('gvhk2') <= 0.21919842809438705) ? " + 
"0.004273227354424036" + 
":  " + 
"0.0034181071499585214" + 
":  " + 
"(b('L8b3med') <= 615.5) ? " + 
"(b('lat') <= 53.60642433166504) ? " + 
"-0.00497680600608736" + 
":  " + 
"0.0005195227111896072" + 
":  " + 
"(b('L8b3med') <= 619.0) ? " + 
"0.008506199044337248" + 
":  " + 
"-3.517985971358255e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 166.0) ? " + 
"(b('bulk') <= 145.5) ? " + 
"(b('gvhk3') <= 0.006678904872387648) ? " + 
"-0.00027855850943319163" + 
":  " + 
"0.0010550221102822448" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"-0.004366111418833464" + 
":  " + 
"-1.8853621124807856e-06" + 
":  " + 
"(b('grass') <= 79.94424438476562) ? " + 
"(b('crops') <= 45.766448974609375) ? " + 
"-0.002883982626976714" + 
":  " + 
"0.0004064416188676867" + 
":  " + 
"(b('L8b10med') <= 2364.0) ? " + 
"0.006674171085157277" + 
":  " + 
"0.0032884562422803368" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.017636760137975216) ? " + 
"(b('gvhk3') <= 0.016927449963986874) ? " + 
"(b('lat') <= 33.261295318603516) ? " + 
"-0.00400195844376498" + 
":  " + 
"0.00017026101807899376" + 
":  " + 
"(b('lat') <= 36.20848846435547) ? " + 
"0.008185463232996737" + 
":  " + 
"0.00412805488436845" + 
":  " + 
"(b('L8b10med') <= 1356.5) ? " + 
"-0.010139269274511253" + 
":  " + 
"(b('L8b3med') <= 934.5) ? " + 
"0.0014471600742621033" + 
":  " + 
"-0.0011366513535708965" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 42.838584899902344) ? " + 
"(b('lat') <= 42.611045837402344) ? " + 
"0.00016787017477153774" + 
":  " + 
"-0.008735016679889698" + 
":  " + 
"(b('L8b10med') <= 1847.0) ? " + 
"-0.005330837284933609" + 
":  " + 
"0.0065669452411199975" + 
":  " + 
"(b('ndvi_med') <= 1698.0) ? " + 
"(b('L8b3med') <= 990.0) ? " + 
"0.0033488074274631526" + 
":  " + 
"-0.008055007529818392" + 
":  " + 
"(b('lon') <= -119.66800308227539) ? " + 
"0.008447179633179924" + 
":  " + 
"-0.00023957769363408597" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -13.692728042602539) ? " + 
"(b('gvhmean') <= -13.75554084777832) ? " + 
"(b('ndvi_med') <= 1884.5) ? " + 
"-0.0007855658561464117" + 
":  " + 
"0.0014224557145683615" + 
":  " + 
"(b('L8b3med') <= 1312.5) ? " + 
"0.009923543919252174" + 
":  " + 
"0.003159650258444946" + 
":  " + 
"(b('gvhmean') <= -12.406572818756104) ? " + 
"(b('gvhk2') <= 0.4474491775035858) ? " + 
"-0.0015383495329676323" + 
":  " + 
"0.006174006953028009" + 
":  " + 
"(b('gvhmean') <= -12.389698028564453) ? " + 
"0.012554211217727068" + 
":  " + 
"0.00015117852061600473" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('gvhk3') <= 0.009486398193985224) ? " + 
"(b('gvhk2') <= 0.3871832937002182) ? " + 
"0.0004865396100892656" + 
":  " + 
"0.005324710639158519" + 
":  " + 
"(b('gvhk3') <= 0.009995386935770512) ? " + 
"-0.014914629213352515" + 
":  " + 
"-0.0004312175352580876" + 
":  " + 
"(b('gvhk3') <= 0.00598120060749352) ? " + 
"(b('ndvi_med') <= 3333.0) ? " + 
"-0.0024232384981725257" + 
":  " + 
"0.0003456841248496193" + 
":  " + 
"(b('gvhk2') <= 0.3682187348604202) ? " + 
"0.0023459157272731792" + 
":  " + 
"-0.0006648784304213898" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('sand') <= 67.0) ? " + 
"-0.0022329746895374536" + 
":  " + 
"-0.003966303923565104" + 
":  " + 
"(b('gvvmean') <= -13.692728042602539) ? " + 
"(b('gvhmean') <= -13.75554084777832) ? " + 
"0.00028699755185393016" + 
":  " + 
"0.006888654555762093" + 
":  " + 
"(b('grass') <= 92.84939193725586) ? " + 
"-0.0002720806137650245" + 
":  " + 
"0.003948388638971925" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2822.25) ? " + 
"(b('L8b10med') <= 2738.5) ? " + 
"(b('L8b3med') <= 1692.5) ? " + 
"0.00010839742665722019" + 
":  " + 
"-0.004036996781975697" + 
":  " + 
"(b('bulk') <= 147.0) ? " + 
"-0.00298165236345075" + 
":  " + 
"-0.010103652757762769" + 
":  " + 
"(b('ndvi_med') <= 1460.5) ? " + 
"(b('ndvi_med') <= 1432.0) ? " + 
"0.00012148026952206811" + 
":  " + 
"-0.010000229692918333" + 
":  " + 
"(b('L8b6med') <= 3776.0) ? " + 
"0.009012836829832484" + 
":  " + 
"-0.00021158326921832138" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -16.72476100921631) ? " + 
"(b('ndvi_med') <= 2426.5) ? " + 
"(b('gvhk2') <= 0.37174341082572937) ? " + 
"-0.0019321171787682195" + 
":  " + 
"-0.003916271694114695" + 
":  " + 
"0.002006040199828002" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"(b('bare') <= 0.6794871836900711) ? " + 
"-7.1186446820317375e-06" + 
":  " + 
"-0.0020885607120733826" + 
":  " + 
"(b('L8b6med') <= 2680.0) ? " + 
"0.002124086351856808" + 
":  " + 
"-8.488972042529092e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 11.910642623901367) ? " + 
"(b('L8b10med') <= 2942.25) ? " + 
"(b('L8b3med') <= 1349.25) ? " + 
"-0.00021016624579883167" + 
":  " + 
"0.0033836132903802066" + 
":  " + 
"(b('L8b5med') <= 2822.0) ? " + 
"0.0035380491083740057" + 
":  " + 
"-0.005618082446832614" + 
":  " + 
"(b('ndvi_med') <= 1897.0) ? " + 
"(b('lon') <= -115.78924560546875) ? " + 
"-0.0012754406434408812" + 
":  " + 
"0.0013905181649771072" + 
":  " + 
"(b('sand') <= 40.5) ? " + 
"0.0188102458552927" + 
":  " + 
"0.004714462087910894" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvvmean') <= -11.045052528381348) ? " + 
"-0.002788753010338374" + 
":  " + 
"0.009320945364856142" + 
":  " + 
"(b('L8b6med') <= 2241.0) ? " + 
"(b('grass') <= 69.24871444702148) ? " + 
"-0.0020786884385378935" + 
":  " + 
"0.0031248636532269086" + 
":  " + 
"(b('gvhk2') <= 0.6582140624523163) ? " + 
"-1.3509909728533021e-05" + 
":  " + 
"0.002567109303585458" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 146.23104858398438) ? " + 
"(b('lat') <= 39.518320083618164) ? " + 
"(b('L8b5med') <= 2297.0) ? " + 
"0.003869365750291759" + 
":  " + 
"0.0001969206285591892" + 
":  " + 
"(b('lat') <= 41.189334869384766) ? " + 
"-0.002221911832023952" + 
":  " + 
"0.0001070151275046994" + 
":  " + 
"(b('lat') <= -34.78766059875488) ? " + 
"(b('crops') <= 4.558724880218506) ? " + 
"-0.0021049556193887906" + 
":  " + 
"0.0012527912752001921" + 
":  " + 
"-0.010113638923065299" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1125.75) ? " + 
"(b('L8b3med') <= 934.5) ? " + 
"(b('bare') <= 10.39842176437378) ? " + 
"2.853633579392114e-05" + 
":  " + 
"0.004558889978200506" + 
":  " + 
"(b('sand') <= 42.5) ? " + 
"-0.002109610813437065" + 
":  " + 
"0.00020037484369319088" + 
":  " + 
"(b('gvhk2') <= 0.4450976401567459) ? " + 
"(b('lon') <= -119.94356536865234) ? " + 
"0.0021463063319113007" + 
":  " + 
"-0.000524152234447704" + 
":  " + 
"(b('gvhk3') <= 0.00949416309595108) ? " + 
"0.00973633621837545" + 
":  " + 
"0.001379090201475937" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.2183675915002823) ? " + 
"(b('gvhk3') <= 0.1156606525182724) ? " + 
"(b('gvhk3') <= 0.11459998413920403) ? " + 
"1.2316887014671544e-05" + 
":  " + 
"-0.009122312515128086" + 
":  " + 
"(b('sand') <= 74.5) ? " + 
"0.0013854962371219505" + 
":  " + 
"0.005213421401951329" + 
":  " + 
"(b('bulk') <= 151.5) ? " + 
"(b('L8b10med') <= 2056.0) ? " + 
"-0.0021519551844492724" + 
":  " + 
"-0.0009717059348261017" + 
":  " + 
"-0.004146456458935147" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 3352.25) ? " + 
"(b('L8b6med') <= 3707.0) ? " + 
"(b('L8b6med') <= 3683.25) ? " + 
"-2.8066996649186285e-05" + 
":  " + 
"0.006424366432247173" + 
":  " + 
"(b('gvhk2') <= 0.33053188025951385) ? " + 
"0.0009178374753864618" + 
":  " + 
"-0.002623213034435002" + 
":  " + 
"(b('gvhk3') <= 0.005745887290686369) ? " + 
"(b('gvhk3') <= -0.001903281023260206) ? " + 
"0.003945906973196314" + 
":  " + 
"-0.0003882164706620672" + 
":  " + 
"(b('ndvi_med') <= 1244.0) ? " + 
"0.0019159629772915465" + 
":  " + 
"0.008879092027267083" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 27.5) ? " + 
"(b('gvhk2') <= 0.25576619803905487) ? " + 
"(b('ndvi_med') <= 3390.5) ? " + 
"0.0029402576626697957" + 
":  " + 
"0.006301827324831311" + 
":  " + 
"(b('L8b6med') <= 2828.5) ? " + 
"-0.0009860234476094815" + 
":  " + 
"0.0023085913536762975" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"(b('ndvi_med') <= 4268.0) ? " + 
"-0.0010790825986298823" + 
":  " + 
"0.009947153245584761" + 
":  " + 
"(b('gvhk2') <= 0.2010231539607048) ? " + 
"0.0009864871077512683" + 
":  " + 
"-0.0001531803723652531" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 166.0) ? " + 
"(b('L8b3med') <= 893.25) ? " + 
"(b('L8b6med') <= 2815.5) ? " + 
"-8.37807381998853e-05" + 
":  " + 
"0.002517876700449787" + 
":  " + 
"(b('L8b10med') <= 1675.25) ? " + 
"-0.006628194250809669" + 
":  " + 
"-0.0001734543522245468" + 
":  " + 
"(b('ndvi_med') <= 1574.0) ? " + 
"(b('L8b6med') <= 3458.0) ? " + 
"0.00642609904526463" + 
":  " + 
"0.0027727744168188906" + 
":  " + 
"(b('L8b6med') <= 3501.25) ? " + 
"-0.001939835126818501" + 
":  " + 
"0.00013377417962158467" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 41.426435470581055) ? " + 
"(b('L8b5med') <= 2079.5) ? " + 
"-0.01038966832570598" + 
":  " + 
"-5.602642981544451e-05" + 
":  " + 
"(b('grass') <= 78.74732971191406) ? " + 
"0.0027837196013349042" + 
":  " + 
"-0.003924139909802027" + 
":  " + 
"(b('gvhk3') <= 0.00598120060749352) ? " + 
"(b('ndvi_med') <= 3333.0) ? " + 
"-0.002186218495777645" + 
":  " + 
"0.0002615515644717696" + 
":  " + 
"(b('gvhk2') <= 0.3682187348604202) ? " + 
"0.0022080754265281877" + 
":  " + 
"-0.0005602033282334126" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.004369281879081664" + 
":  " + 
"(b('lon') <= -112.57361602783203) ? " + 
"(b('ndvi_med') <= 2921.25) ? " + 
"0.0006158931874481035" + 
":  " + 
"-0.007584374033612951" + 
":  " + 
"(b('lon') <= -111.68005752563477) ? " + 
"-0.00319673505125428" + 
":  " + 
"-5.9618722617104904e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 570.0) ? " + 
"(b('gvvmean') <= -14.234665393829346) ? " + 
"-0.0012869877271636798" + 
":  " + 
"(b('L8b6med') <= 2561.5) ? " + 
"0.0022621591470450286" + 
":  " + 
"0.0037879452604517305" + 
":  " + 
"(b('L8b3med') <= 615.5) ? " + 
"(b('lat') <= 53.60642433166504) ? " + 
"-0.004311601030232152" + 
":  " + 
"0.000503683869114907" + 
":  " + 
"(b('L8b3med') <= 619.0) ? " + 
"0.00758043794558555" + 
":  " + 
"-4.907395493061607e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -16.178815841674805) ? " + 
"(b('gvhk2') <= 0.25228671729564667) ? " + 
"(b('L8b10med') <= 2671.0) ? " + 
"0.003011163746180781" + 
":  " + 
"0.0005647471686967345" + 
":  " + 
"(b('bare') <= 15.181381702423096) ? " + 
"-0.0012826758776093704" + 
":  " + 
"-0.005157384658890096" + 
":  " + 
"(b('gvhmean') <= -15.980653285980225) ? " + 
"(b('lon') <= -107.69564819335938) ? " + 
"0.005086099703873914" + 
":  " + 
"0.0031244021239798248" + 
":  " + 
"(b('gvhk2') <= 0.3535355180501938) ? " + 
"-0.00021900746595626948" + 
":  " + 
"0.0003793259668052637" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 21.3190860748291) ? " + 
"(b('crops') <= 65.67342758178711) ? " + 
"(b('gvhk2') <= 0.21858274191617966) ? " + 
"0.0012278006061751709" + 
":  " + 
"-0.0032920911474392427" + 
":  " + 
"(b('gvvmean') <= -10.876780033111572) ? " + 
"-0.002153156403623893" + 
":  " + 
"0.0013658067846154605" + 
":  " + 
"(b('gvvmean') <= -12.406572818756104) ? " + 
"(b('L8b6med') <= 2443.5) ? " + 
"-0.004842825377252096" + 
":  " + 
"-6.476274723338528e-05" + 
":  " + 
"(b('gvvmean') <= -12.065759181976318) ? " + 
"0.004047580323003494" + 
":  " + 
"0.00041373835780413054" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -10.35920000076294) ? " + 
"(b('gvhmean') <= -10.898516654968262) ? " + 
"(b('gvhmean') <= -11.252465724945068) ? " + 
"0.00015040020683089355" + 
":  " + 
"-0.0024279783588942736" + 
":  " + 
"(b('lon') <= 9.128300189971924) ? " + 
"0.0033087822850585234" + 
":  " + 
"-0.0008956030041609881" + 
":  " + 
"(b('crops') <= 65.67342758178711) ? " + 
"(b('grass') <= 25.489541053771973) ? " + 
"-0.0037002572123119174" + 
":  " + 
"-8.375689680916304e-05" + 
":  " + 
"(b('lon') <= -5.394804954528809) ? " + 
"0.010545090481016012" + 
":  " + 
"0.0003231097141604069" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 893.25) ? " + 
"(b('L8b3med') <= 849.5) ? " + 
"(b('L8b5med') <= 3538.5) ? " + 
"-0.0001552746643888362" + 
":  " + 
"0.008869148117228498" + 
":  " + 
"(b('lon') <= -120.41248321533203) ? " + 
"-0.007835853799910114" + 
":  " + 
"0.0027962609584347106" + 
":  " + 
"(b('L8b10med') <= 1675.25) ? " + 
"(b('L8b3med') <= 921.25) ? " + 
"-0.008040744250894294" + 
":  " + 
"-0.004183028836097433" + 
":  " + 
"(b('lat') <= 43.91702461242676) ? " + 
"0.00014188858175618677" + 
":  " + 
"-0.0011370596755513455" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 89.04487609863281) ? " + 
"(b('crops') <= 88.85982513427734) ? " + 
"(b('L8b10med') <= 1622.5) ? " + 
"0.0008442540487182256" + 
":  " + 
"-0.00013257140947895256" + 
":  " + 
"0.008123037336956296" + 
":  " + 
"(b('crops') <= 95.01214981079102) ? " + 
"(b('gvhk3') <= -0.0011899704113602638) ? " + 
"-0.0018443352460201547" + 
":  " + 
"-0.007590135844830179" + 
":  " + 
"(b('ndvi_med') <= 3425.5) ? " + 
"0.0019690981037428015" + 
":  " + 
"-0.0013764995612142062" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1487.5) ? " + 
"(b('bare') <= 29.32122039794922) ? " + 
"(b('L8b3med') <= 1470.0) ? " + 
"-3.110870723977894e-05" + 
":  " + 
"0.004279168803618009" + 
":  " + 
"(b('L8b5med') <= 2487.75) ? " + 
"0.005899791045731545" + 
":  " + 
"0.007748087421654587" + 
":  " + 
"(b('grass') <= 55.38705825805664) ? " + 
"(b('L8b10med') <= 2815.0) ? " + 
"-0.001879867014475131" + 
":  " + 
"0.001078844973910712" + 
":  " + 
"(b('L8b6med') <= 3682.5) ? " + 
"-0.005148491665022249" + 
":  " + 
"0.00046845559027335754" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvhk3') <= -0.003810879308730364) ? " + 
"0.007883319649187731" + 
":  " + 
"-0.0019897436487305853" + 
":  " + 
"(b('L8b6med') <= 2374.0) ? " + 
"(b('bulk') <= 131.5) ? " + 
"-0.0025085491354602347" + 
":  " + 
"4.04651813544953e-05" + 
":  " + 
"(b('L8b6med') <= 2409.5) ? " + 
"0.00300844343836453" + 
":  " + 
"-5.611104058034872e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 166.0) ? " + 
"(b('bulk') <= 163.5) ? " + 
"(b('L8b6med') <= 3379.0) ? " + 
"0.0001908089045311829" + 
":  " + 
"-0.0004672773847956877" + 
":  " + 
"(b('sand') <= 36.5) ? " + 
"-0.008803135946600194" + 
":  " + 
"-0.00023084137081556821" + 
":  " + 
"(b('gvhmean') <= -13.06681203842163) ? " + 
"(b('gvhk3') <= 0.007996083237230778) ? " + 
"0.0010948078595212768" + 
":  " + 
"-0.0017802202921604476" + 
":  " + 
"(b('sand') <= 33.5) ? " + 
"0.005749120462714377" + 
":  " + 
"0.003091001254332759" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 39.55443000793457) ? " + 
"(b('L8b5med') <= 2297.0) ? " + 
"(b('L8b3med') <= 1066.5) ? " + 
"0.0016162150092254302" + 
":  " + 
"0.008450612184626213" + 
":  " + 
"(b('L8b3med') <= 1004.25) ? " + 
"-0.001733142102968362" + 
":  " + 
"0.0005913772997690296" + 
":  " + 
"(b('lat') <= 41.189334869384766) ? " + 
"(b('lat') <= 40.97825622558594) ? " + 
"-0.0014251619376738024" + 
":  " + 
"-0.011052635917699356" + 
":  " + 
"(b('L8b6med') <= 3729.0) ? " + 
"0.0002122018565463717" + 
":  " + 
"-0.0031025028575957384" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('L8b6med') <= 2741.75) ? " + 
"(b('crops') <= 65.2109375) ? " + 
"0.001307317010847745" + 
":  " + 
"0.00838645205235905" + 
":  " + 
"(b('L8b10med') <= 1679.25) ? " + 
"-0.005470593924458256" + 
":  " + 
"4.6080770817586374e-05" + 
":  " + 
"(b('ndvi_med') <= 1297.0) ? " + 
"(b('sand') <= 39.5) ? " + 
"0.003421417790504977" + 
":  " + 
"-0.009544110477478392" + 
":  " + 
"(b('lon') <= -119.66800308227539) ? " + 
"0.005925232696129966" + 
":  " + 
"-0.0002827273122389684" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -13.692728042602539) ? " + 
"(b('ndvi_med') <= 1884.5) ? " + 
"(b('gvhk3') <= -0.003393527236767113) ? " + 
"-0.003434294416361445" + 
":  " + 
"4.859088719504271e-05" + 
":  " + 
"(b('bare') <= 12.442737102508545) ? " + 
"0.0009367463688013522" + 
":  " + 
"0.011492916334601894" + 
":  " + 
"(b('gvhk3') <= 0.044428421184420586) ? " + 
"(b('gvhk3') <= 0.03783573769032955) ? " + 
"-8.672102278474761e-05" + 
":  " + 
"0.00408959327971823" + 
":  " + 
"(b('gvhk3') <= 0.08871250972151756) ? " + 
"-0.004494509604847145" + 
":  " + 
"0.00026238348773622715" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -16.178815841674805) ? " + 
"(b('gvhk2') <= 0.25228671729564667) ? " + 
"(b('bare') <= 13.701829433441162) ? " + 
"0.0004198131771903091" + 
":  " + 
"0.0026873967258586456" + 
":  " + 
"(b('L8b5med') <= 2796.5) ? " + 
"-0.0012177815473028266" + 
":  " + 
"-0.004664296838705118" + 
":  " + 
"(b('gvvmean') <= -15.980653285980225) ? " + 
"(b('L8b5med') <= 2471.0) ? " + 
"0.002952585717221956" + 
":  " + 
"0.004518520272029633" + 
":  " + 
"(b('lat') <= 39.55443000793457) ? " + 
"0.00039844160776598194" + 
":  " + 
"-0.00018068242013361162" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1207.25) ? " + 
"(b('ndvi_med') <= 1189.0) ? " + 
"(b('grass') <= 60.29493713378906) ? " + 
"-0.0008669957925648326" + 
":  " + 
"0.001415332760912934" + 
":  " + 
"(b('gvhk2') <= 0.17863165587186813) ? " + 
"-0.0023196035476222843" + 
":  " + 
"-0.007750802073596387" + 
":  " + 
"(b('bare') <= 25.768656730651855) ? " + 
"(b('lat') <= 39.927019119262695) ? " + 
"0.0005545936752001433" + 
":  " + 
"-0.00021973505221147474" + 
":  " + 
"(b('L8b5med') <= 3136.5) ? " + 
"0.007118209937672426" + 
":  " + 
"-2.072958053189744e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 28.5) ? " + 
"(b('L8b5med') <= 3216.5) ? " + 
"(b('gvhk2') <= 0.25576619803905487) ? " + 
"0.0033894360690534205" + 
":  " + 
"0.0008693009712219803" + 
":  " + 
"(b('L8b6med') <= 2385.5) ? " + 
"-0.0042539584310878065" + 
":  " + 
"-0.0014135602146220783" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"(b('L8b5med') <= 3538.5) ? " + 
"-0.0009788435971818156" + 
":  " + 
"0.007943215380044971" + 
":  " + 
"(b('gvhk2') <= 0.2010231539607048) ? " + 
"0.000753532840234245" + 
":  " + 
"-0.00010807352713461753" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 33.261295318603516) ? " + 
"(b('bulk') <= 147.5) ? " + 
"(b('ndvi_med') <= 2233.0) ? " + 
"0.0023692895932647924" + 
":  " + 
"-0.0014152959642798658" + 
":  " + 
"(b('L8b3med') <= 905.0) ? " + 
"0.0003308783343414015" + 
":  " + 
"-0.004018412109895076" + 
":  " + 
"(b('lat') <= 36.15193557739258) ? " + 
"(b('gvhk3') <= 0.038123464211821556) ? " + 
"0.0015048911015351127" + 
":  " + 
"-0.0015928639370225888" + 
":  " + 
"(b('lat') <= 37.28743934631348) ? " + 
"-0.0021118014261330208" + 
":  " + 
"2.326178765606025e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('lat') <= 55.93754959106445) ? " + 
"(b('lat') <= 55.91939926147461) ? " + 
"2.196423993826902e-05" + 
":  " + 
"0.0031786039753342737" + 
":  " + 
"(b('L8b3med') <= 678.0) ? " + 
"0.0011232734676338964" + 
":  " + 
"-0.00196474515866484" + 
":  " + 
"(b('gvhk2') <= 0.8954881727695465) ? " + 
"(b('gvhk3') <= -0.11274298606440425) ? " + 
"0.0024348769191508135" + 
":  " + 
"0.004619437759982359" + 
":  " + 
"-0.0003552667567862655" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1207.25) ? " + 
"(b('ndvi_med') <= 1189.0) ? " + 
"(b('grass') <= 60.29493713378906) ? " + 
"-0.0008247343825725946" + 
":  " + 
"0.0012450796248998583" + 
":  " + 
"(b('bulk') <= 150.0) ? " + 
"-0.002167519079642924" + 
":  " + 
"-0.007117600047670619" + 
":  " + 
"(b('bare') <= 25.768656730651855) ? " + 
"(b('lat') <= 39.927019119262695) ? " + 
"0.0005138534522372421" + 
":  " + 
"-0.00019467601890931" + 
":  " + 
"(b('gvhk2') <= 0.22771423310041428) ? " + 
"0.00635523326936797" + 
":  " + 
"-1.237187252468852e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvhk2') <= 0.2723564878106117) ? " + 
"0.007157425540743084" + 
":  " + 
"-0.001728331427383406" + 
":  " + 
"(b('L8b6med') <= 2241.0) ? " + 
"(b('grass') <= 69.24871444702148) ? " + 
"-0.0017194665282687445" + 
":  " + 
"0.0026726656010914174" + 
":  " + 
"(b('gvhk2') <= 0.6582140624523163) ? " + 
"-1.0271945400878572e-05" + 
":  " + 
"0.0020590994975134874" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 28.5) ? " + 
"(b('L8b5med') <= 3216.5) ? " + 
"(b('gvhk3') <= 0.017642876133322716) ? " + 
"0.0017223705498221726" + 
":  " + 
"-0.0004382352869474887" + 
":  " + 
"(b('L8b10med') <= 1653.75) ? " + 
"-0.0036416709360206634" + 
":  " + 
"-0.0012562319994882942" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"(b('ndvi_med') <= 4268.0) ? " + 
"-0.0008777478207823701" + 
":  " + 
"0.007782454140481565" + 
":  " + 
"(b('gvhk3') <= 0.0002743174627539702) ? " + 
"-0.00037468717192934447" + 
":  " + 
"0.00030424347831684565" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 33.261295318603516) ? " + 
"(b('gvhk3') <= 0.01707080751657486) ? " + 
"(b('L8b5med') <= 2596.0) ? " + 
"-0.00653941721747028" + 
":  " + 
"-0.002359230946134381" + 
":  " + 
"(b('ndvi_med') <= 1543.5) ? " + 
"-0.004455657953602338" + 
":  " + 
"0.0005753562338612848" + 
":  " + 
"(b('lat') <= 36.29348564147949) ? " + 
"(b('gvhk3') <= 0.038123464211821556) ? " + 
"0.0013319819276619489" + 
":  " + 
"-0.0014849085692480854" + 
":  " + 
"(b('lat') <= 37.28743934631348) ? " + 
"-0.0021076737685289493" + 
":  " + 
"2.567558496050492e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('ndvi_med') <= 1200.25) ? " + 
"0.0032756108439588594" + 
":  " + 
"(b('L8b5med') <= 3178.5) ? " + 
"0.0008339878198835582" + 
":  " + 
"0.001798895330551581" + 
":  " + 
"(b('gvhk2') <= 0.08685321733355522) ? " + 
"(b('lat') <= 38.521549224853516) ? " + 
"-0.0011154730569055207" + 
":  " + 
"-0.0037214337912820686" + 
":  " + 
"(b('L8b5med') <= 3532.0) ? " + 
"-4.869063808331252e-05" + 
":  " + 
"0.0012162530543827022" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2473.75) ? " + 
"(b('grass') <= 49.85152626037598) ? " + 
"(b('grass') <= 49.03428840637207) ? " + 
"-0.0001809152998973365" + 
":  " + 
"-0.011962325189214099" + 
":  " + 
"(b('gvhk3') <= 0.08491826429963112) ? " + 
"0.0006561733133058935" + 
":  " + 
"-0.008935408411698889" + 
":  " + 
"(b('grass') <= 73.36912155151367) ? " + 
"(b('ndvi_med') <= 1596.0) ? " + 
"0.0008003569801809417" + 
":  " + 
"-0.0014859893739585402" + 
":  " + 
"(b('grass') <= 83.5473747253418) ? " + 
"-0.003260606599167007" + 
":  " + 
"0.0008665344523990983" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1207.25) ? " + 
"(b('ndvi_med') <= 1189.0) ? " + 
"(b('grass') <= 60.29493713378906) ? " + 
"-0.0008065175801590575" + 
":  " + 
"0.0010751065717484762" + 
":  " + 
"(b('bare') <= 14.019552826881409) ? " + 
"-0.006237505665236315" + 
":  " + 
"-0.0020578985176760295" + 
":  " + 
"(b('bare') <= 25.768656730651855) ? " + 
"(b('L8b10med') <= 2813.5) ? " + 
"-6.751739367567506e-05" + 
":  " + 
"0.0011455266065811512" + 
":  " + 
"(b('gvhmean') <= -11.365689754486084) ? " + 
"0.005635209618108622" + 
":  " + 
"-0.00011826603126961766" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 1619.0) ? " + 
"0.0037356284227606507" + 
":  " + 
"(b('lat') <= 56.031551361083984) ? " + 
"(b('gvhmean') <= -10.898516654968262) ? " + 
"-0.00011617049158935725" + 
":  " + 
"0.0005634978553150393" + 
":  " + 
"(b('lat') <= 56.04010009765625) ? " + 
"-0.0028373108961067353" + 
":  " + 
"0.0006493128659472325" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 893.25) ? " + 
"(b('L8b6med') <= 2815.5) ? " + 
"(b('gvhk3') <= 0.006678904872387648) ? " + 
"-0.0007369505742449206" + 
":  " + 
"0.0012693724731948474" + 
":  " + 
"(b('L8b5med') <= 2642.5) ? " + 
"0.0005552793479406404" + 
":  " + 
"0.005739741579652374" + 
":  " + 
"(b('L8b3med') <= 1001.75) ? " + 
"(b('gvhmean') <= -15.315587520599365) ? " + 
"0.0021837340557329613" + 
":  " + 
"-0.0020453115757989174" + 
":  " + 
"(b('gvhk3') <= 0.08321710303425789) ? " + 
"3.407960135885473e-05" + 
":  " + 
"0.005428131444930105" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.521310806274414) ? " + 
"(b('L8b5med') <= 2200.5) ? " + 
"0.004176263036112543" + 
":  " + 
"(b('grass') <= 20.64785861968994) ? " + 
"0.0007263225625086671" + 
":  " + 
"-0.001376100583541903" + 
":  " + 
"(b('lat') <= 34.940629959106445) ? " + 
"(b('L8b6med') <= 3098.25) ? " + 
"0.005355617721601212" + 
":  " + 
"0.001018002789730461" + 
":  " + 
"(b('L8b5med') <= 2236.0) ? " + 
"-0.0006773348743132533" + 
":  " + 
"0.0001522064687269584" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1487.5) ? " + 
"(b('L8b3med') <= 1472.5) ? " + 
"(b('bare') <= 28.288668632507324) ? " + 
"-6.186412383392795e-06" + 
":  " + 
"0.004058050064851618" + 
":  " + 
"(b('L8b5med') <= 2708.75) ? " + 
"0.0016267892536878381" + 
":  " + 
"0.0058959543836881526" + 
":  " + 
"(b('L8b3med') <= 1563.0) ? " + 
"(b('gvhmean') <= -14.111579895019531) ? " + 
"-0.006022242580009433" + 
":  " + 
"-0.0019137804100204615" + 
":  " + 
"(b('ndvi_med') <= 1285.5) ? " + 
"-0.0004687994611071814" + 
":  " + 
"0.005290204562007905" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.35234180092811584) ? " + 
"(b('gvhk2') <= 0.34677062928676605) ? " + 
"(b('L8b10med') <= 1620.5) ? " + 
"0.0009998706167243109" + 
":  " + 
"-0.0003112115691692124" + 
":  " + 
"(b('L8b6med') <= 3609.0) ? " + 
"-0.007889616344313115" + 
":  " + 
"-0.0031731596630324432" + 
":  " + 
"(b('lon') <= 9.146950244903564) ? " + 
"(b('L8b5med') <= 3021.0) ? " + 
"0.001185976183387052" + 
":  " + 
"-0.000907064569551405" + 
":  " + 
"(b('ndvi_med') <= 4391.0) ? " + 
"-0.00039509386444600323" + 
":  " + 
"-0.003551276937885405" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -16.178815841674805) ? " + 
"(b('gvhk2') <= 0.537092536687851) ? " + 
"(b('bare') <= 15.181381702423096) ? " + 
"-0.0010011542884748332" + 
":  " + 
"0.001978070525188308" + 
":  " + 
"-0.00419670790462795" + 
":  " + 
"(b('gvhmean') <= -15.980653285980225) ? " + 
"(b('grass') <= 96.24354934692383) ? " + 
"0.003571960961647608" + 
":  " + 
"0.0020054236280497018" + 
":  " + 
"(b('gvhk2') <= 0.3535355180501938) ? " + 
"-0.00020395974643122003" + 
":  " + 
"0.0003747444773114319" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.2183675915002823) ? " + 
"(b('gvhk3') <= 0.1156606525182724) ? " + 
"(b('gvhk3') <= 0.11459998413920403) ? " + 
"8.223070519889853e-06" + 
":  " + 
"-0.006924631052341784" + 
":  " + 
"(b('sand') <= 74.5) ? " + 
"0.0010954502295065435" + 
":  " + 
"0.004227018089807175" + 
":  " + 
"(b('gvhk2') <= 0.6248702704906464) ? " + 
"-0.0025376496587665234" + 
":  " + 
"(b('lat') <= 10.564464569091797) ? " + 
"-0.0005427365357550396" + 
":  " + 
"-0.0013307072508689372" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"(b('crops') <= 28.8680477142334) ? " + 
"0.001935432417446703" + 
":  " + 
"0.0030977211955671713" + 
":  " + 
"(b('L8b3med') <= 761.5) ? " + 
"(b('ndvi_med') <= 4096.5) ? " + 
"0.0001926534552541475" + 
":  " + 
"-0.0023768756638990604" + 
":  " + 
"(b('L8b3med') <= 795.5) ? " + 
"0.0018076618063008853" + 
":  " + 
"-1.9816642257791683e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -5.297438144683838) ? " + 
"(b('gvvmean') <= -6.832682847976685) ? " + 
"(b('L8b5med') <= 2236.0) ? " + 
"-0.0005946436971504089" + 
":  " + 
"0.00013046525286883375" + 
":  " + 
"(b('gvvmean') <= -6.493995904922485) ? " + 
"-0.007326806232836686" + 
":  " + 
"-0.0012068547234349765" + 
":  " + 
"(b('ndvi_med') <= 5067.5) ? " + 
"(b('L8b3med') <= 739.0) ? " + 
"0.0033279530479315145" + 
":  " + 
"0.0019436720063768093" + 
":  " + 
"-0.00028365984433800784" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -16.178815841674805) ? " + 
"(b('L8b5med') <= 2797.0) ? " + 
"(b('gvhk2') <= 0.4862928092479706) ? " + 
"-0.000993300409501499" + 
":  " + 
"0.0010046039067351312" + 
":  " + 
"-0.0037889242822782554" + 
":  " + 
"(b('gvhmean') <= -15.933977127075195) ? " + 
"(b('lat') <= 48.39845085144043) ? " + 
"0.0028271542399421145" + 
":  " + 
"6.247036602077816e-05" + 
":  " + 
"(b('gvhk2') <= 0.3535355180501938) ? " + 
"-0.00018704009615259627" + 
":  " + 
"0.0003217499671506057" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('L8b10med') <= 2497.5) ? " + 
"(b('L8b6med') <= 3050.0) ? " + 
"0.0006799259929627308" + 
":  " + 
"0.00166180670595939" + 
":  " + 
"0.0029789013461936353" + 
":  " + 
"(b('gvhk2') <= 0.08685321733355522) ? " + 
"(b('sand') <= 65.0) ? " + 
"-0.0032603552656122053" + 
":  " + 
"-0.0008657690123659682" + 
":  " + 
"(b('L8b5med') <= 3532.0) ? " + 
"-4.568028339222365e-05" + 
":  " + 
"0.0010941543340261225" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 166.0) ? " + 
"(b('lon') <= -121.0405044555664) ? " + 
"(b('bare') <= 5.824693918228149) ? " + 
"-0.006668041584908468" + 
":  " + 
"-0.0007340664901698615" + 
":  " + 
"(b('lon') <= -120.42640686035156) ? " + 
"0.001474179253880125" + 
":  " + 
"-4.079529251862732e-05" + 
":  " + 
"(b('gvvmean') <= -13.06681203842163) ? " + 
"(b('lat') <= 37.12553024291992) ? " + 
"0.0009409476905703484" + 
":  " + 
"-0.0018271282464430993" + 
":  " + 
"(b('L8b6med') <= 3653.0) ? " + 
"0.0048757610042008265" + 
":  " + 
"0.002741211168406102" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvvmean') <= -11.045052528381348) ? " + 
"-0.0015734414545453268" + 
":  " + 
"0.006423666047102677" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"(b('ndvi_med') <= 1617.0) ? " + 
"0.002961483162930545" + 
":  " + 
"-0.0004675986535315472" + 
":  " + 
"(b('L8b6med') <= 2680.0) ? " + 
"0.0015935686084126992" + 
":  " + 
"-0.00013102077321365936" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -13.692728042602539) ? " + 
"(b('gvvmean') <= -13.75554084777832) ? " + 
"(b('L8b5med') <= 2148.75) ? " + 
"-0.0026359052697595676" + 
":  " + 
"0.0003434666753614975" + 
":  " + 
"(b('lat') <= 42.37171936035156) ? " + 
"0.0015441939362937224" + 
":  " + 
"0.007549747942489894" + 
":  " + 
"(b('gvhmean') <= -12.406572818756104) ? " + 
"(b('gvhk3') <= 0.07626939192414284) ? " + 
"-0.0006568315464211209" + 
":  " + 
"-0.007652922627412059" + 
":  " + 
"(b('gvhmean') <= -12.389698028564453) ? " + 
"0.009949743160874325" + 
":  " + 
"0.0001304761179902311" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('gvhk3') <= 0.009975441731512547) ? " + 
"-0.002869614902728551" + 
":  " + 
"-0.001530453923701127" + 
":  " + 
"(b('lat') <= 39.518320083618164) ? " + 
"(b('L8b5med') <= 2297.0) ? " + 
"0.002485424215767723" + 
":  " + 
"0.00013202382529501496" + 
":  " + 
"(b('bulk') <= 145.5) ? " + 
"0.00012088757618792614" + 
":  " + 
"-0.0015089859647988146" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.521310806274414) ? " + 
"(b('L8b5med') <= 2200.5) ? " + 
"0.0036289607876033025" + 
":  " + 
"(b('gvhmean') <= -11.730230808258057) ? " + 
"-0.00097253646587175" + 
":  " + 
"0.002170258178093888" + 
":  " + 
"(b('lat') <= 34.940629959106445) ? " + 
"(b('gvhk3') <= 0.009608345339074731) ? " + 
"0.0009306736478350933" + 
":  " + 
"0.004850894938152421" + 
":  " + 
"(b('gvhmean') <= -14.307159423828125) ? " + 
"0.0006534577361244708" + 
":  " + 
"-0.00014467376093577132" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 4751.0) ? " + 
"(b('bulk') <= 119.0) ? " + 
"(b('gvhmean') <= -11.419847011566162) ? " + 
"0.0012451406054863586" + 
":  " + 
"-0.004252201643118764" + 
":  " + 
"(b('bulk') <= 123.5) ? " + 
"-0.0030736615940518456" + 
":  " + 
"-1.8341471637552847e-05" + 
":  " + 
"-0.0034153428897672478" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.35234180092811584) ? " + 
"(b('gvhk2') <= 0.34677062928676605) ? " + 
"(b('ndvi_med') <= 3328.5) ? " + 
"-0.0002826256725184759" + 
":  " + 
"0.0009284873647583046" + 
":  " + 
"(b('L8b6med') <= 3609.0) ? " + 
"-0.006721947551860286" + 
":  " + 
"-0.002711306386856401" + 
":  " + 
"(b('gvhk2') <= 0.3584425300359726) ? " + 
"(b('gvhmean') <= -15.557076930999756) ? " + 
"0.0017925293459602476" + 
":  " + 
"0.009455731037561699" + 
":  " + 
"(b('L8b3med') <= 1113.25) ? " + 
"-0.0002802215854388423" + 
":  " + 
"0.0013769090811438587" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2111.5) ? " + 
"(b('lat') <= 40.11824989318848) ? " + 
"-0.008159791482558396" + 
":  " + 
"(b('L8b10med') <= 1961.0) ? " + 
"-8.46392533339267e-05" + 
":  " + 
"0.0019012388102763278" + 
":  " + 
"(b('L8b5med') <= 2123.5) ? " + 
"-0.008499855155445907" + 
":  " + 
"(b('L8b5med') <= 2216.25) ? " + 
"-0.0017810533018525717" + 
":  " + 
"5.595698741204874e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 133.5) ? " + 
"(b('ndvi_med') <= 1617.0) ? " + 
"(b('lon') <= -119.20192337036133) ? " + 
"0.003432229623447018" + 
":  " + 
"0.0018273365107203121" + 
":  " + 
"(b('ndvi_med') <= 2814.0) ? " + 
"-0.0018915004437228464" + 
":  " + 
"-2.0365677103071124e-05" + 
":  " + 
"(b('L8b6med') <= 2680.0) ? " + 
"(b('lat') <= 39.22870063781738) ? " + 
"-0.003963941254949189" + 
":  " + 
"0.001763447823653159" + 
":  " + 
"(b('gvvmean') <= -10.855900764465332) ? " + 
"-0.0003154218984172756" + 
":  " + 
"0.0018658563225130292" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 39.518320083618164) ? " + 
"(b('gvvmean') <= -14.750941753387451) ? " + 
"(b('gvhk2') <= 0.32675252854824066) ? " + 
"0.0009912948521086234" + 
":  " + 
"-0.0011935698264392035" + 
":  " + 
"(b('gvhmean') <= -14.69206953048706) ? " + 
"0.008264084402190397" + 
":  " + 
"0.0006198605905175148" + 
":  " + 
"(b('bulk') <= 145.5) ? " + 
"(b('gvvmean') <= -15.062663555145264) ? " + 
"0.0016059872146103938" + 
":  " + 
"-5.6346921734114224e-05" + 
":  " + 
"(b('gvhmean') <= -10.881607055664062) ? " + 
"-0.002398954698728836" + 
":  " + 
"0.003001965360434816" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('gvhk3') <= 0.009486398193985224) ? " + 
"(b('gvhk2') <= 0.3871832937002182) ? " + 
"0.0003249899531460544" + 
":  " + 
"0.00363722554831633" + 
":  " + 
"(b('gvhk3') <= 0.009995386935770512) ? " + 
"-0.010620071055848085" + 
":  " + 
"-0.0002809918653666363" + 
":  " + 
"(b('gvhk3') <= 0.00598120060749352) ? " + 
"(b('lat') <= 53.604108810424805) ? " + 
"-0.0017019033502089194" + 
":  " + 
"0.000220840081774253" + 
":  " + 
"(b('gvhk2') <= 0.3682187348604202) ? " + 
"0.0017263649529437423" + 
":  " + 
"-0.0003997301541424888" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 21.3190860748291) ? " + 
"(b('gvvmean') <= -10.898516654968262) ? " + 
"(b('sand') <= 54.5) ? " + 
"-0.0025717571062789666" + 
":  " + 
"0.0007881232633324914" + 
":  " + 
"(b('gvhmean') <= -10.820080280303955) ? " + 
"0.005650534354683555" + 
":  " + 
"-0.00010730081822197315" + 
":  " + 
"(b('grass') <= 23.62397003173828) ? " + 
"(b('gvhk3') <= -0.004023110086563975) ? " + 
"-0.006030345657196123" + 
":  " + 
"0.003432563326527063" + 
":  " + 
"(b('grass') <= 25.489541053771973) ? " + 
"-0.0022770529284183195" + 
":  " + 
"0.00011062873336649593" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.0002743174627539702) ? " + 
"(b('L8b5med') <= 2708.0) ? " + 
"(b('gvhmean') <= -13.985540390014648) ? " + 
"-0.0036702184514514516" + 
":  " + 
"-0.00022585877347587718" + 
":  " + 
"(b('gvhk3') <= 0.00015709890431025997) ? " + 
"0.000489248608733343" + 
":  " + 
"-0.0070029664187716" + 
":  " + 
"(b('gvhk3') <= 0.00042635008867364377) ? " + 
"(b('bare') <= 0.9017595052719116) ? " + 
"0.003826335011076404" + 
":  " + 
"0.007059579434504221" + 
":  " + 
"(b('L8b5med') <= 2879.5) ? " + 
"0.00029954393550526813" + 
":  " + 
"-0.0009427512151034541" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"(b('gvvmean') <= -13.215603828430176) ? " + 
"0.0026597687270027426" + 
":  " + 
"0.0018415077124449009" + 
":  " + 
"(b('L8b3med') <= 615.5) ? " + 
"(b('lat') <= 53.6043701171875) ? " + 
"-0.00362615212465744" + 
":  " + 
"-0.00018241286369134052" + 
":  " + 
"(b('L8b3med') <= 619.0) ? " + 
"0.006046565455861963" + 
":  " + 
"6.258452406275504e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2111.5) ? " + 
"(b('lat') <= 40.11824989318848) ? " + 
"-0.006983801321034169" + 
":  " + 
"(b('L8b6med') <= 2413.5) ? " + 
"-0.00020694816395743867" + 
":  " + 
"0.0016080819654544524" + 
":  " + 
"(b('L8b5med') <= 2123.5) ? " + 
"-0.007087169296297435" + 
":  " + 
"(b('gvvmean') <= -7.417926073074341) ? " + 
"1.571956219191079e-05" + 
":  " + 
"-0.0022208212135191216" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 166.0) ? " + 
"(b('bulk') <= 163.5) ? " + 
"(b('L8b6med') <= 3379.0) ? " + 
"0.00014841544795118956" + 
":  " + 
"-0.0003566499285446092" + 
":  " + 
"(b('sand') <= 36.5) ? " + 
"-0.00717172822996643" + 
":  " + 
"-0.00017943590930408204" + 
":  " + 
"(b('gvvmean') <= -13.06681203842163) ? " + 
"(b('L8b10med') <= 2239.0) ? " + 
"-0.0015854239316171748" + 
":  " + 
"0.0008227934515155771" + 
":  " + 
"(b('gvhk3') <= -0.0022007226943969727) ? " + 
"0.004439118483009208" + 
":  " + 
"0.002447350775305973" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -13.692728042602539) ? " + 
"(b('gvhmean') <= -13.75554084777832) ? " + 
"(b('ndvi_med') <= 1884.5) ? " + 
"-0.0005218167872213313" + 
":  " + 
"0.0009136658140428297" + 
":  " + 
"(b('L8b3med') <= 1312.5) ? " + 
"0.00654682353179125" + 
":  " + 
"0.0014743801698727937" + 
":  " + 
"(b('gvhmean') <= -13.623824119567871) ? " + 
"(b('bulk') <= 143.0) ? " + 
"-0.005007314364982973" + 
":  " + 
"-0.001524004153021975" + 
":  " + 
"(b('gvhk3') <= 0.04456311836838722) ? " + 
"6.188341553592104e-05" + 
":  " + 
"-0.001318927971218517" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('gvhk3') <= 0.009486398193985224) ? " + 
"(b('gvhk3') <= 0.008563306648284197) ? " + 
"0.00048819189357577865" + 
":  " + 
"0.0069605923142860016" + 
":  " + 
"(b('gvhk3') <= 0.009995386935770512) ? " + 
"-0.009354070320994418" + 
":  " + 
"-0.00023219241345952935" + 
":  " + 
"(b('gvhk3') <= 0.00598120060749352) ? " + 
"(b('gvhk3') <= -0.0002864523994503543) ? " + 
"7.467884009586256e-05" + 
":  " + 
"-0.0017601290610633525" + 
":  " + 
"(b('ndvi_med') <= 1282.0) ? " + 
"-0.006506438488496011" + 
":  " + 
"0.0006825080776233386" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 4751.0) ? " + 
"(b('gvhk3') <= 0.0002743174627539702) ? " + 
"(b('gvhk2') <= 0.3154679983854294) ? " + 
"-0.0006890530099814713" + 
":  " + 
"0.00036021923848082515" + 
":  " + 
"(b('gvhk3') <= 0.00042635008867364377) ? " + 
"0.004305384725605432" + 
":  " + 
"8.338044280877738e-05" + 
":  " + 
"-0.0032129092289226446" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 21.3190860748291) ? " + 
"(b('L8b5med') <= 3232.5) ? " + 
"(b('gvhk2') <= 0.35624825954437256) ? " + 
"-0.001531773989597951" + 
":  " + 
"8.082463616415541e-05" + 
":  " + 
"(b('grass') <= 17.183883666992188) ? " + 
"0.00047686780329275703" + 
":  " + 
"0.008582414689511597" + 
":  " + 
"(b('grass') <= 23.62397003173828) ? " + 
"(b('gvhk3') <= -0.004023110086563975) ? " + 
"-0.005438026223169801" + 
":  " + 
"0.0030960769585004727" + 
":  " + 
"(b('grass') <= 25.489541053771973) ? " + 
"-0.002085657399549751" + 
":  " + 
"0.00010640586926823906" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 934.5) ? " + 
"(b('bare') <= 10.39842176437378) ? " + 
"(b('L8b3med') <= 933.0) ? " + 
"0.00011322921951339975" + 
":  " + 
"-0.008273823934216079" + 
":  " + 
"(b('sand') <= 39.5) ? " + 
"0.014172272202334552" + 
":  " + 
"0.0014772530840738319" + 
":  " + 
"(b('L8b3med') <= 949.5) ? " + 
"(b('L8b6med') <= 2961.5) ? " + 
"-0.003906508172267423" + 
":  " + 
"-0.000342431343057302" + 
":  " + 
"(b('L8b6med') <= 2618.5) ? " + 
"0.0017958983148799472" + 
":  " + 
"-0.00011835409388429183" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -16.178815841674805) ? " + 
"(b('gvhk2') <= 0.537092536687851) ? " + 
"(b('gvhk2') <= 0.4862928092479706) ? " + 
"-0.0009147753685671184" + 
":  " + 
"0.0009547293061651987" + 
":  " + 
"-0.003237210454071049" + 
":  " + 
"(b('gvvmean') <= -15.933977127075195) ? " + 
"(b('gvhk2') <= 0.4392503798007965) ? " + 
"0.002341025817854292" + 
":  " + 
"0.0002400331776297171" + 
":  " + 
"(b('bare') <= 5.712439060211182) ? " + 
"-0.00014265859803653188" + 
":  " + 
"0.00033191400532861975" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.233184814453125) ? " + 
"(b('gvhk2') <= 0.462603896856308) ? " + 
"-0.001057242187141233" + 
":  " + 
"-0.002861230096408117" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"(b('L8b6med') <= 3622.25) ? " + 
"0.0013244248264345688" + 
":  " + 
"0.002448701861382463" + 
":  " + 
"(b('lat') <= 33.261295318603516) ? " + 
"-0.0014726603513816631" + 
":  " + 
"3.693695609290532e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 39.55443000793457) ? " + 
"(b('L8b5med') <= 2377.25) ? " + 
"(b('lon') <= -112.1821060180664) ? " + 
"-0.0005353725507481321" + 
":  " + 
"0.0029478795722365455" + 
":  " + 
"(b('L8b3med') <= 1004.25) ? " + 
"-0.0017041065397107077" + 
":  " + 
"0.00047091833670706427" + 
":  " + 
"(b('lat') <= 41.189334869384766) ? " + 
"(b('lon') <= -55.33573842048645) ? " + 
"-0.0009356268668782557" + 
":  " + 
"-0.00734403251312819" + 
":  " + 
"(b('L8b6med') <= 3729.0) ? " + 
"0.0001425136803599987" + 
":  " + 
"-0.0024672910030092885" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 934.5) ? " + 
"(b('bare') <= 10.39842176437378) ? " + 
"(b('L8b3med') <= 933.0) ? " + 
"0.00010801713322420881" + 
":  " + 
"-0.00670146612528727" + 
":  " + 
"(b('sand') <= 39.5) ? " + 
"0.012703908517922913" + 
":  " + 
"0.0013615605780215312" + 
":  " + 
"(b('L8b3med') <= 997.5) ? " + 
"(b('L8b3med') <= 995.0) ? " + 
"-0.001029760752653012" + 
":  " + 
"-0.010032267548838167" + 
":  " + 
"(b('gvhk3') <= 0.08321710303425789) ? " + 
"4.042856800625133e-06" + 
":  " + 
"0.004174408181528709" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2483.5) ? " + 
"(b('L8b3med') <= 1302.75) ? " + 
"(b('bare') <= 5.712439060211182) ? " + 
"-0.00015419298008031556" + 
":  " + 
"0.0009251208631319851" + 
":  " + 
"(b('gvhk2') <= 0.2606791853904724) ? " + 
"-0.000402806599490625" + 
":  " + 
"0.0075120207363905955" + 
":  " + 
"(b('gvhk2') <= 0.23249638080596924) ? " + 
"(b('grass') <= 78.62461853027344) ? " + 
"0.0011003364005681652" + 
":  " + 
"-0.003983503990061726" + 
":  " + 
"(b('gvhk2') <= 0.2878238558769226) ? " + 
"-0.003457812773939094" + 
":  " + 
"-6.771228368485017e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -16.178815841674805) ? " + 
"(b('gvhk2') <= 0.537092536687851) ? " + 
"(b('L8b5med') <= 2780.0) ? " + 
"-0.000778038596507384" + 
":  " + 
"0.0016374207093677734" + 
":  " + 
"-0.0030571913099372294" + 
":  " + 
"(b('gvhmean') <= -15.933977127075195) ? " + 
"(b('gvhk2') <= 0.4392503798007965) ? " + 
"0.0020335075995534134" + 
":  " + 
"0.00031648016949475943" + 
":  " + 
"(b('grass') <= 73.93266296386719) ? " + 
"-0.00010004616492134418" + 
":  " + 
"0.00034892433935439064" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 893.25) ? " + 
"(b('L8b6med') <= 2815.5) ? " + 
"(b('ndvi_med') <= 2244.0) ? " + 
"0.0036660682885152236" + 
":  " + 
"-0.00022339093159840144" + 
":  " + 
"(b('lon') <= -118.96649932861328) ? " + 
"-0.0036253908282857517" + 
":  " + 
"0.002453913209580443" + 
":  " + 
"(b('L8b3med') <= 920.0) ? " + 
"(b('gvhk2') <= 0.21925845742225647) ? " + 
"-0.0055309370397312214" + 
":  " + 
"0.00034199939411540855" + 
":  " + 
"(b('L8b3med') <= 934.5) ? " + 
"0.002459154547140111" + 
":  " + 
"-0.00014295180675803315" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('gvhmean') <= -10.35920000076294) ? " + 
"(b('gvvmean') <= -10.898516654968262) ? " + 
"-6.541602293156687e-05" + 
":  " + 
"0.001445185181188883" + 
":  " + 
"(b('L8b5med') <= 3288.5) ? " + 
"-0.0007768633407072092" + 
":  " + 
"0.002549791247499572" + 
":  " + 
"(b('gvhmean') <= -6.224896669387817) ? " + 
"0.0038665392397058407" + 
":  " + 
"(b('sand') <= 74.0) ? " + 
"-0.0003958016779564699" + 
":  " + 
"0.0016636877060245137" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"(b('gvvmean') <= -13.215603828430176) ? " + 
"0.0024715468176202404" + 
":  " + 
"0.0016091254746857242" + 
":  " + 
"(b('L8b3med') <= 615.5) ? " + 
"(b('gvhk2') <= 0.1956348642706871) ? " + 
"0.0015847949654754223" + 
":  " + 
"-0.0018787832267707309" + 
":  " + 
"(b('L8b3med') <= 619.0) ? " + 
"0.005230874254489426" + 
":  " + 
"3.3717984998038023e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.0002743174627539702) ? " + 
"(b('L8b10med') <= 1112.5) ? " + 
"0.005185630453315965" + 
":  " + 
"(b('L8b10med') <= 1504.5) ? " + 
"-0.001582950668597414" + 
":  " + 
"-2.58250395315394e-05" + 
":  " + 
"(b('gvhk3') <= 0.00042635008867364377) ? " + 
"(b('L8b6med') <= 3368.0) ? " + 
"0.0029820831169349443" + 
":  " + 
"0.005787427462794537" + 
":  " + 
"(b('L8b5med') <= 2879.5) ? " + 
"0.00025357014305495373" + 
":  " + 
"-0.0007438454526661552" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -12.406572818756104) ? " + 
"(b('L8b6med') <= 2448.5) ? " + 
"(b('ndvi_med') <= 3834.5) ? " + 
"-0.0025499838206385836" + 
":  " + 
"-0.007228079019105077" + 
":  " + 
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"-0.00047490051713260214" + 
":  " + 
"0.00039779122919972017" + 
":  " + 
"(b('gvvmean') <= -12.389698028564453) ? " + 
"0.007958199184700754" + 
":  " + 
"(b('L8b10med') <= 1677.0) ? " + 
"0.0009516011469407156" + 
":  " + 
"-0.00024935922368488783" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1316.75) ? " + 
"(b('L8b3med') <= 1208.0) ? " + 
"(b('L8b3med') <= 1125.75) ? " + 
"-8.7787866784462e-05" + 
":  " + 
"0.001297495763931656" + 
":  " + 
"(b('L8b5med') <= 2983.0) ? " + 
"-0.0005449306499993393" + 
":  " + 
"-0.005327262901291856" + 
":  " + 
"(b('ndvi_med') <= 1538.0) ? " + 
"(b('gvhk3') <= 0.08407099545001984) ? " + 
"-0.000353213981724973" + 
":  " + 
"0.007044661594389212" + 
":  " + 
"(b('L8b6med') <= 3754.5) ? " + 
"0.006158440878574559" + 
":  " + 
"-0.0006116369963646727" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -16.178815841674805) ? " + 
"(b('gvhk2') <= 0.25228671729564667) ? " + 
"(b('gvhmean') <= -16.64906406402588) ? " + 
"0.0013865617025645705" + 
":  " + 
"2.8972307075811332e-05" + 
":  " + 
"(b('gvhk2') <= 0.537092536687851) ? " + 
"-0.000850179218940918" + 
":  " + 
"-0.00278732992637154" + 
":  " + 
"(b('gvvmean') <= -15.933977127075195) ? " + 
"(b('lat') <= 48.39845085144043) ? " + 
"0.0017973899690432505" + 
":  " + 
"0.0002489744051172582" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"6.418064394076384e-05" + 
":  " + 
"-0.0007207116050433357" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2705.5) ? " + 
"(b('L8b6med') <= 3432.0) ? " + 
"(b('gvhmean') <= -10.222922801971436) ? " + 
"0.0003053336596869123" + 
":  " + 
"-0.0010063684604753036" + 
":  " + 
"(b('gvhk2') <= 0.31843774020671844) ? " + 
"-0.0028494196190187475" + 
":  " + 
"-0.0003764007274713398" + 
":  " + 
"(b('gvhmean') <= -15.11733102798462) ? " + 
"(b('gvhmean') <= -15.360464572906494) ? " + 
"-0.0007819292463301701" + 
":  " + 
"-0.0036343218178091358" + 
":  " + 
"(b('gvvmean') <= -14.69206953048706) ? " + 
"0.003712010123860198" + 
":  " + 
"0.00026541300512736174" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('lat') <= 43.65060043334961) ? " + 
"(b('L8b6med') <= 3055.5) ? " + 
"0.0008433314062486277" + 
":  " + 
"-0.00017311677681745106" + 
":  " + 
"(b('gvhk3') <= 0.00598120060749352) ? " + 
"-0.0006685707342184429" + 
":  " + 
"0.0004933119881686948" + 
":  " + 
"(b('gvvmean') <= -6.224896669387817) ? " + 
"0.003610064130538826" + 
":  " + 
"(b('bulk') <= 128.5) ? " + 
"0.0016274977502256371" + 
":  " + 
"-3.782719283018654e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('bulk') <= 143.5) ? " + 
"(b('L8b6med') <= 3050.0) ? " + 
"0.0007284951917901072" + 
":  " + 
"0.001346666936612284" + 
":  " + 
"0.00241937634063559" + 
":  " + 
"(b('gvhk2') <= 0.08685321733355522) ? " + 
"(b('sand') <= 65.0) ? " + 
"-0.0030268729434418107" + 
":  " + 
"-0.0007037927287151212" + 
":  " + 
"(b('L8b5med') <= 2637.5) ? " + 
"-0.00018387355109075458" + 
":  " + 
"0.00022793820075553607" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -5.297438144683838) ? " + 
"(b('gvhk3') <= -0.14948104321956635) ? " + 
"-0.003834313427116598" + 
":  " + 
"(b('gvhk3') <= -0.10665059834718704) ? " + 
"0.002409326376388049" + 
":  " + 
"-2.352758078378658e-05" + 
":  " + 
"(b('gvhk3') <= -0.40707144141197205) ? " + 
"-1.565711843809492e-05" + 
":  " + 
"(b('lat') <= 56.01410102844238) ? " + 
"0.0014930788370633996" + 
":  " + 
"0.002938741288300767" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 166.0) ? " + 
"(b('lon') <= -121.0405044555664) ? " + 
"(b('gvhk3') <= 0.027749701403081417) ? " + 
"-0.0005506841613903019" + 
":  " + 
"-0.005384486834068572" + 
":  " + 
"(b('lon') <= -120.42640686035156) ? " + 
"0.0012165265999740924" + 
":  " + 
"-3.5443370383063106e-05" + 
":  " + 
"(b('gvvmean') <= -13.06681203842163) ? " + 
"(b('bare') <= 13.870503664016724) ? " + 
"0.0008069452338176283" + 
":  " + 
"-0.001576267808512291" + 
":  " + 
"(b('L8b10med') <= 2424.0) ? " + 
"0.003686768398006149" + 
":  " + 
"0.0026521917120316957" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 893.25) ? " + 
"(b('L8b3med') <= 849.5) ? " + 
"(b('gvhk2') <= 0.1819647178053856) ? " + 
"-0.002228509153407941" + 
":  " + 
"0.00015562841095264357" + 
":  " + 
"(b('lon') <= -120.41248321533203) ? " + 
"-0.004846038150661716" + 
":  " + 
"0.0018577481355856" + 
":  " + 
"(b('L8b3med') <= 900.75) ? " + 
"(b('gvhk3') <= 0.016453418880701065) ? " + 
"-0.005402358036439986" + 
":  " + 
"-0.002211589735627864" + 
":  " + 
"(b('lat') <= 43.91702461242676) ? " + 
"9.649154435703273e-05" + 
":  " + 
"-0.0007557760057816602" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 119.0) ? " + 
"(b('gvhk3') <= -0.015737397596240044) ? " + 
"(b('gvhmean') <= -13.97707462310791) ? " + 
"0.00208222545221437" + 
":  " + 
"0.004855104520449571" + 
":  " + 
"(b('gvvmean') <= -11.419847011566162) ? " + 
"0.0003333935961819978" + 
":  " + 
"-0.0033249354420794366" + 
":  " + 
"(b('bulk') <= 123.5) ? " + 
"(b('gvhk2') <= 0.7747202813625336) ? " + 
"-0.0029761578702077046" + 
":  " + 
"-0.0014094501056693826" + 
":  " + 
"(b('ndvi_med') <= 4980.0) ? " + 
"1.5313519982580554e-05" + 
":  " + 
"-0.0016588029636181861" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('lon') <= -114.52702331542969) ? " + 
"0.0021721552952547463" + 
":  " + 
"0.0010000192507564048" + 
":  " + 
"(b('gvhk2') <= 0.08685321733355522) ? " + 
"(b('lat') <= 38.521549224853516) ? " + 
"-0.0005224468322726286" + 
":  " + 
"-0.0027116628112835903" + 
":  " + 
"(b('L8b5med') <= 3232.5) ? " + 
"-5.6943444879211934e-05" + 
":  " + 
"0.0005530955805922308" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 1927.0) ? " + 
"(b('ndvi_med') <= 3875.0) ? " + 
"(b('L8b5med') <= 1737.0) ? " + 
"0.0026370116479033645" + 
":  " + 
"0.001830502666164871" + 
":  " + 
"-6.691568489862465e-05" + 
":  " + 
"(b('crops') <= 89.04487609863281) ? " + 
"(b('crops') <= 88.85982513427734) ? " + 
"7.870681778126518e-06" + 
":  " + 
"0.0047650459336865125" + 
":  " + 
"(b('bare') <= 0.0628272220492363) ? " + 
"-0.001738573174480629" + 
":  " + 
"0.0014997882897665252" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 934.5) ? " + 
"(b('bare') <= 10.39842176437378) ? " + 
"(b('L8b3med') <= 933.0) ? " + 
"0.00011708542275721623" + 
":  " + 
"-0.0063179681573287405" + 
":  " + 
"(b('sand') <= 39.5) ? " + 
"0.010951668462605979" + 
":  " + 
"0.0010310200283959986" + 
":  " + 
"(b('L8b3med') <= 997.5) ? " + 
"(b('L8b3med') <= 979.0) ? " + 
"-0.0004529033414443447" + 
":  " + 
"-0.004050785611436779" + 
":  " + 
"(b('gvhk2') <= 0.4450976401567459) ? " + 
"-0.00010888736661173414" + 
":  " + 
"0.0013667915298220346" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -16.178815841674805) ? " + 
"(b('gvhk2') <= 0.25228671729564667) ? " + 
"(b('bulk') <= 151.0) ? " + 
"0.001331128916201324" + 
":  " + 
"4.175334484436688e-05" + 
":  " + 
"(b('L8b6med') <= 2696.0) ? " + 
"-0.0026467116317881456" + 
":  " + 
"-0.0008040376661352176" + 
":  " + 
"(b('gvvmean') <= -15.933977127075195) ? " + 
"(b('bulk') <= 140.0) ? " + 
"0.002939855886988696" + 
":  " + 
"0.0011743308013882014" + 
":  " + 
"(b('L8b3med') <= 678.0) ? " + 
"0.0005876916810986987" + 
":  " + 
"-5.249238518889035e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 39.55443000793457) ? " + 
"(b('gvvmean') <= -14.750941753387451) ? " + 
"(b('gvhmean') <= -15.461314678192139) ? " + 
"-5.16816171382583e-05" + 
":  " + 
"-0.0015105181505564364" + 
":  " + 
"(b('grass') <= 67.55332565307617) ? " + 
"-8.430962480376708e-05" + 
":  " + 
"0.0013774831893914542" + 
":  " + 
"(b('bulk') <= 145.5) ? " + 
"(b('lat') <= 39.65203857421875) ? " + 
"-0.004603839113351729" + 
":  " + 
"9.859652360197263e-05" + 
":  " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"0.0024061236514266587" + 
":  " + 
"-0.0017108190421199325" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('gvhk3') <= -0.006556568201631308) ? " + 
"(b('gvhk3') <= -0.009026424493640661) ? " + 
"6.454674457372577e-05" + 
":  " + 
"-0.0029013764882291635" + 
":  " + 
"(b('gvhk3') <= -0.004809212172403932) ? " + 
"0.0026556833671267043" + 
":  " + 
"1.09492074122629e-05" + 
":  " + 
"(b('gvhk3') <= -0.11274298606440425) ? " + 
"(b('gvvmean') <= -5.098753213882446) ? " + 
"0.0013088659107436396" + 
":  " + 
"7.181893594257471e-05" + 
":  " + 
"0.0032448362948102327" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 3276.0) ? " + 
"(b('L8b6med') <= 3707.0) ? " + 
"(b('L8b6med') <= 3683.25) ? " + 
"-6.083320442486089e-06" + 
":  " + 
"0.0031496616621178794" + 
":  " + 
"(b('gvhk2') <= 0.272418737411499) ? " + 
"0.0013701927863937313" + 
":  " + 
"-0.001427897232865585" + 
":  " + 
"(b('gvhk2') <= 0.13824796676635742) ? " + 
"(b('lon') <= -115.47503662109375) ? " + 
"-7.473261081548249e-05" + 
":  " + 
"-0.0015787342885474134" + 
":  " + 
"(b('L8b3med') <= 1330.75) ? " + 
"0.006091225139160397" + 
":  " + 
"0.0012685612168806693" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"(b('L8b3med') <= 555.5) ? " + 
"0.002184675177383133" + 
":  " + 
"0.0015313271291778063" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"(b('lat') <= 44.82858085632324) ? " + 
"-0.0010946468389511986" + 
":  " + 
"5.9466910422865484e-05" + 
":  " + 
"(b('L8b6med') <= 2680.0) ? " + 
"0.0010738678722603966" + 
":  " + 
"-7.589766913815882e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('L8b6med') <= 3055.5) ? " + 
"(b('L8b6med') <= 3029.5) ? " + 
"0.0004732089286314072" + 
":  " + 
"0.004303132550605916" + 
":  " + 
"(b('L8b10med') <= 1874.0) ? " + 
"-0.003148060139369136" + 
":  " + 
"-3.6498639277135055e-05" + 
":  " + 
"(b('lat') <= 45.2860050201416) ? " + 
"(b('gvhk2') <= 0.32861660420894623) ? " + 
"-0.0021373136495275624" + 
":  " + 
"0.0008975169817486868" + 
":  " + 
"(b('ndvi_med') <= 1297.0) ? " + 
"-0.006039333767832174" + 
":  " + 
"0.00024936898866960905" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 89.04487609863281) ? " + 
"(b('crops') <= 88.85982513427734) ? " + 
"(b('grass') <= 5.889207363128662) ? " + 
"-0.0008094696147898297" + 
":  " + 
"7.66013208184844e-05" + 
":  " + 
"0.004074819992499784" + 
":  " + 
"(b('crops') <= 95.01214981079102) ? " + 
"(b('gvhk3') <= -0.0011899704113602638) ? " + 
"-0.0008968437373832357" + 
":  " + 
"-0.0045584431722892615" + 
":  " + 
"(b('L8b10med') <= 2467.0) ? " + 
"-0.0003212641426957134" + 
":  " + 
"0.002491226010200534" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2822.25) ? " + 
"(b('L8b10med') <= 2738.5) ? " + 
"(b('L8b3med') <= 1302.75) ? " + 
"-5.831804687348872e-05" + 
":  " + 
"0.0012531201123690567" + 
":  " + 
"(b('bulk') <= 147.0) ? " + 
"-0.001630847062954334" + 
":  " + 
"-0.005640347630754307" + 
":  " + 
"(b('ndvi_med') <= 1460.5) ? " + 
"(b('ndvi_med') <= 1398.0) ? " + 
"0.00014282791368537922" + 
":  " + 
"-0.0035507212602584473" + 
":  " + 
"(b('L8b6med') <= 3776.0) ? " + 
"0.004140361834170006" + 
":  " + 
"0.00036402850662618547" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -12.406572818756104) ? " + 
"(b('L8b6med') <= 2443.5) ? " + 
"(b('gvhk3') <= 0.013427001889795065) ? " + 
"-0.0025069785475714187" + 
":  " + 
"-0.006657383998099842" + 
":  " + 
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"-0.00043373032128938096" + 
":  " + 
"0.0003415297864755291" + 
":  " + 
"(b('gvhmean') <= -12.389698028564453) ? " + 
"0.006944828444655549" + 
":  " + 
"(b('L8b10med') <= 1677.0) ? " + 
"0.0008181518562349974" + 
":  " + 
"-0.00019759101441734362" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.2732113152742386) ? " + 
"(b('gvhk2') <= 0.2617492973804474) ? " + 
"(b('bare') <= 3.7248884439468384) ? " + 
"-0.000541994294363358" + 
":  " + 
"0.0004477646438769737" + 
":  " + 
"(b('L8b5med') <= 2470.5) ? " + 
"0.0005528346729990925" + 
":  " + 
"0.005121166638832254" + 
":  " + 
"(b('gvhk2') <= 0.2763971984386444) ? " + 
"(b('L8b6med') <= 2958.0) ? " + 
"-0.0004394028772274419" + 
":  " + 
"-0.0045136816485893405" + 
":  " + 
"(b('L8b3med') <= 704.75) ? " + 
"-0.0012087104571701396" + 
":  " + 
"0.00011749747092374022" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.0026162464339542085" + 
":  " + 
"(b('gvhmean') <= -9.219711780548096) ? " + 
"(b('gvhmean') <= -9.48308277130127) ? " + 
"3.215627787088072e-07" + 
":  " + 
"-0.0026565585350406887" + 
":  " + 
"(b('grass') <= 18.78471565246582) ? " + 
"-0.00018152136177525442" + 
":  " + 
"0.0017642397208572174" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 4751.0) ? " + 
"(b('L8b5med') <= 3232.5) ? " + 
"(b('gvhk3') <= -0.006795636843889952) ? " + 
"-0.0006366697503235779" + 
":  " + 
"4.92057388196668e-05" + 
":  " + 
"(b('L8b3med') <= 747.0) ? " + 
"-0.005552459072408256" + 
":  " + 
"0.0006646555909722559" + 
":  " + 
"-0.0026011265033109576" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('lat') <= 55.93754959106445) ? " + 
"(b('lat') <= 55.91939926147461) ? " + 
"6.278201640161019e-06" + 
":  " + 
"0.0020025276151411434" + 
":  " + 
"(b('L8b3med') <= 678.0) ? " + 
"0.0007824087702925456" + 
":  " + 
"-0.0011794634464936994" + 
":  " + 
"(b('gvvmean') <= -6.224896669387817) ? " + 
"0.0029780775456289543" + 
":  " + 
"(b('L8b5med') <= 1934.5) ? " + 
"0.0002947692618088804" + 
":  " + 
"0.0012357041999690455" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -16.178815841674805) ? " + 
"(b('gvhk2') <= 0.537092536687851) ? " + 
"(b('gvhk2') <= 0.4862928092479706) ? " + 
"-0.0007523310827766391" + 
":  " + 
"0.0006392801370498497" + 
":  " + 
"-0.0025299280724709328" + 
":  " + 
"(b('gvhmean') <= -15.933977127075195) ? " + 
"(b('bulk') <= 140.0) ? " + 
"0.0025648653218212636" + 
":  " + 
"0.0010621007079346378" + 
":  " + 
"(b('L8b5med') <= 2705.5) ? " + 
"-0.00013967921139642698" + 
":  " + 
"0.0001944340676070155" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -5.297438144683838) ? " + 
"(b('gvvmean') <= -6.832682847976685) ? " + 
"(b('gvhmean') <= -8.499517440795898) ? " + 
"-3.477877952839869e-05" + 
":  " + 
"0.0009265751767405975" + 
":  " + 
"(b('gvhmean') <= -6.493995904922485) ? " + 
"-0.005057588335170948" + 
":  " + 
"-0.0007540758260045818" + 
":  " + 
"(b('gvhk2') <= 0.8838767409324646) ? " + 
"(b('L8b3med') <= 739.0) ? " + 
"0.002171128694191171" + 
":  " + 
"0.001263614526511317" + 
":  " + 
"0.0002792602567676383" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.017636760137975216) ? " + 
"(b('gvhk3') <= 0.016927449963986874) ? " + 
"(b('gvhk3') <= 0.015915646217763424) ? " + 
"7.280145152781194e-05" + 
":  " + 
"-0.0026603085711564577" + 
":  " + 
"(b('gvhk3') <= 0.017288035713136196) ? " + 
"0.00449250835579184" + 
":  " + 
"0.001947254690538719" + 
":  " + 
"(b('L8b10med') <= 1356.5) ? " + 
"-0.005892320631704556" + 
":  " + 
"(b('L8b6med') <= 2712.0) ? " + 
"0.0013777096157331784" + 
":  " + 
"-0.0004907990172515317" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"0.0017376534256487441" + 
":  " + 
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"9.712791310459128e-05" + 
":  " + 
"0.005407158947378643" + 
":  " + 
"(b('gvhk3') <= 0.005068940808996558) ? " + 
"-0.0005954006324572501" + 
":  " + 
"0.00044364406781725814" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.017636760137975216) ? " + 
"(b('gvhk3') <= 0.016927449963986874) ? " + 
"(b('lat') <= 33.261295318603516) ? " + 
"-0.00219221498915397" + 
":  " + 
"8.404955107837503e-05" + 
":  " + 
"(b('sand') <= 47.0) ? " + 
"0.0017254906224387564" + 
":  " + 
"0.0040335447289021956" + 
":  " + 
"(b('gvhk3') <= 0.021156606264412403) ? " + 
"(b('L8b5med') <= 2764.0) ? " + 
"-0.0005683717458084874" + 
":  " + 
"-0.005084036830087332" + 
":  " + 
"(b('gvhk2') <= 0.2682465612888336) ? " + 
"0.0044749593795253215" + 
":  " + 
"-0.00010321747832799569" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2705.5) ? " + 
"(b('gvhmean') <= -10.222922801971436) ? " + 
"(b('gvhk3') <= -0.000725600024452433) ? " + 
"-0.0009881392043922367" + 
":  " + 
"0.00029441824833979275" + 
":  " + 
"(b('gvvmean') <= -10.004114151000977) ? " + 
"-0.004797701513089257" + 
":  " + 
"-0.0005097913391404798" + 
":  " + 
"(b('gvhk2') <= 0.5286999940872192) ? " + 
"(b('gvvmean') <= -10.119505882263184) ? " + 
"0.00011697180719394797" + 
":  " + 
"0.0018934371392219556" + 
":  " + 
"(b('L8b3med') <= 750.5) ? " + 
"0.0031604421457281096" + 
":  " + 
"-0.0023055984666627144" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('L8b5med') <= 2236.0) ? " + 
"(b('L8b5med') <= 2180.0) ? " + 
"0.00015797468045384677" + 
":  " + 
"-0.001968010145198288" + 
":  " + 
"(b('grass') <= 76.27609634399414) ? " + 
"-9.819937191237886e-05" + 
":  " + 
"0.0006516735670571043" + 
":  " + 
"(b('gvhmean') <= -6.224896669387817) ? " + 
"0.0026964142914308042" + 
":  " + 
"(b('grass') <= 7.121815323829651) ? " + 
"0.00034616832799003183" + 
":  " + 
"0.0010945743453598111" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1622.5) ? " + 
"(b('ndvi_med') <= 4391.0) ? " + 
"(b('L8b5med') <= 3538.5) ? " + 
"0.0005131238711163009" + 
":  " + 
"0.005873262946515745" + 
":  " + 
"(b('gvhk2') <= 0.5695222616195679) ? " + 
"-0.002628767270458382" + 
":  " + 
"0.002854217868346526" + 
":  " + 
"(b('L8b10med') <= 1643.0) ? " + 
"(b('grass') <= 21.921671867370605) ? " + 
"-0.003177990232306818" + 
":  " + 
"-0.0018263185904633383" + 
":  " + 
"(b('L8b10med') <= 1658.5) ? " + 
"0.0024747880476663022" + 
":  " + 
"-5.608832454084809e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.2062721624970436) ? " + 
"(b('sand') <= 35.5) ? " + 
"(b('gvhk3') <= -0.0002864523994503543) ? " + 
"0.002071090709763121" + 
":  " + 
"-0.0032581791654043048" + 
":  " + 
"(b('gvhk2') <= 0.1850445792078972) ? " + 
"0.0001418902579618986" + 
":  " + 
"0.0019455280987844006" + 
":  " + 
"(b('gvhk2') <= 0.20911672711372375) ? " + 
"(b('grass') <= 60.23898696899414) ? " + 
"-0.005896849198016876" + 
":  " + 
"-0.0011724322133771573" + 
":  " + 
"(b('ndvi_med') <= 6187.75) ? " + 
"2.567565432383211e-05" + 
":  " + 
"-0.004334054688861638" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2705.5) ? " + 
"(b('L8b6med') <= 3432.0) ? " + 
"(b('gvhmean') <= -10.222922801971436) ? " + 
"0.00025034329188459834" + 
":  " + 
"-0.0008246545259959736" + 
":  " + 
"(b('gvhk2') <= 0.31843774020671844) ? " + 
"-0.0024727697708884326" + 
":  " + 
"-0.00024940789421242155" + 
":  " + 
"(b('gvhk2') <= 0.5286999940872192) ? " + 
"(b('gvhk2') <= 0.5126813054084778) ? " + 
"0.00022589093674272516" + 
":  " + 
"0.004237198998077035" + 
":  " + 
"(b('sand') <= 79.0) ? " + 
"-0.0020715508275206016" + 
":  " + 
"0.0025662285160794884" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 1927.0) ? " + 
"(b('ndvi_med') <= 3449.5) ? " + 
"0.002053036175909198" + 
":  " + 
"(b('L8b5med') <= 1839.0) ? " + 
"0.00011634442376483312" + 
":  " + 
"0.0010213804181511965" + 
":  " + 
"(b('L8b5med') <= 2216.25) ? " + 
"(b('L8b5med') <= 2180.0) ? " + 
"9.872633041936269e-05" + 
":  " + 
"-0.005373482788516121" + 
":  " + 
"(b('grass') <= 76.27609634399414) ? " + 
"-6.0910227685870325e-05" + 
":  " + 
"0.00048584021111370965" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -12.406572818756104) ? " + 
"(b('L8b6med') <= 2443.5) ? " + 
"(b('gvhk2') <= 0.29323916882276535) ? " + 
"-0.0021350672805187467" + 
":  " + 
"-0.0045971154451274615" + 
":  " + 
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"-0.000413057416508207" + 
":  " + 
"0.00030971868535992485" + 
":  " + 
"(b('gvhmean') <= -12.389698028564453) ? " + 
"0.006189539283254303" + 
":  " + 
"(b('gvvmean') <= -11.305431842803955) ? " + 
"0.000739020786647115" + 
":  " + 
"-0.00016049529483803525" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.027968889102339745) ? " + 
"(b('gvhk3') <= 0.023529446683824062) ? " + 
"(b('gvhk3') <= 0.019175725057721138) ? " + 
"8.0249850441043e-05" + 
":  " + 
"-0.0011728416363254554" + 
":  " + 
"(b('grass') <= 75.16565704345703) ? " + 
"0.0004443735564471279" + 
":  " + 
"0.00479636993136089" + 
":  " + 
"(b('lon') <= -119.46337890625) ? " + 
"(b('L8b5med') <= 2521.25) ? " + 
"-0.004795565833902872" + 
":  " + 
"-0.0009795911153270248" + 
":  " + 
"(b('gvhk3') <= 0.029254012741148472) ? " + 
"-0.0036077150119714447" + 
":  " + 
"7.88557529313075e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -16.72476100921631) ? " + 
"(b('ndvi_med') <= 2426.5) ? " + 
"(b('gvhmean') <= -17.102243423461914) ? " + 
"-0.0006832737418270632" + 
":  " + 
"-0.001851766005835041" + 
":  " + 
"0.0008927058228778151" + 
":  " + 
"(b('gvhmean') <= -13.692728042602539) ? " + 
"(b('gvhmean') <= -13.75554084777832) ? " + 
"0.00012200888102781924" + 
":  " + 
"0.003989846291144503" + 
":  " + 
"(b('gvvmean') <= -13.064693450927734) ? " + 
"-0.0007981184971153079" + 
":  " + 
"7.218613874582915e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 47.569419860839844) ? " + 
"(b('lat') <= 43.976104736328125) ? " + 
"(b('gvvmean') <= -10.84829330444336) ? " + 
"-5.616609024490186e-05" + 
":  " + 
"0.0011010365427457016" + 
":  " + 
"(b('L8b3med') <= 994.5) ? " + 
"-0.00019865609171501467" + 
":  " + 
"-0.0038466821424156766" + 
":  " + 
"(b('gvhk2') <= 0.2859973758459091) ? " + 
"(b('gvhk3') <= 0.005616369657218456) ? " + 
"0.00042372113885123135" + 
":  " + 
"0.003687540254870038" + 
":  " + 
"(b('L8b3med') <= 1066.5) ? " + 
"-0.0002583019446048043" + 
":  " + 
"0.0016124004746177257" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.0023366446476614476" + 
":  " + 
"(b('gvvmean') <= -9.219711780548096) ? " + 
"(b('gvhmean') <= -9.74667501449585) ? " + 
"2.0987732681378724e-05" + 
":  " + 
"-0.001284915826522937" + 
":  " + 
"(b('lat') <= 55.97799873352051) ? " + 
"0.0012402464282604184" + 
":  " + 
"-0.00035339479060457355" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 934.5) ? " + 
"(b('bare') <= 7.983341932296753) ? " + 
"(b('bare') <= 4.103881359100342) ? " + 
"0.00013472902301583868" + 
":  " + 
"-0.0027474607562912616" + 
":  " + 
"(b('L8b3med') <= 933.0) ? " + 
"0.001064443051152988" + 
":  " + 
"0.009742432118523048" + 
":  " + 
"(b('L8b3med') <= 949.5) ? " + 
"(b('gvhk2') <= 0.4547490030527115) ? " + 
"-0.0030904634265805225" + 
":  " + 
"-0.00034978858299401506" + 
":  " + 
"(b('L8b6med') <= 2618.5) ? " + 
"0.0012592962717650341" + 
":  " + 
"-9.011336847462712e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -16.72476100921631) ? " + 
"(b('ndvi_med') <= 2426.5) ? " + 
"(b('L8b5med') <= 2436.0) ? " + 
"-0.0017509094117980767" + 
":  " + 
"-0.0006024171950405471" + 
":  " + 
"0.0008077291741918069" + 
":  " + 
"(b('gvhmean') <= -13.548450469970703) ? " + 
"(b('L8b6med') <= 3243.25) ? " + 
"0.0007885212204443369" + 
":  " + 
"-0.00018545881874153456" + 
":  " + 
"(b('gvvmean') <= -13.478110313415527) ? " + 
"-0.0028897959980465665" + 
":  " + 
"-1.4408978027408174e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -5.297438144683838) ? " + 
"(b('gvhmean') <= -6.832682847976685) ? " + 
"(b('crops') <= 89.04487609863281) ? " + 
"4.256858522863111e-05" + 
":  " + 
"-0.0007143292832129713" + 
":  " + 
"(b('gvhmean') <= -6.493995904922485) ? " + 
"-0.0043056341255863495" + 
":  " + 
"-0.00043962995242871616" + 
":  " + 
"(b('gvhmean') <= -4.673092842102051) ? " + 
"(b('sand') <= 73.0) ? " + 
"0.0004353673720230711" + 
":  " + 
"0.0010746992977350434" + 
":  " + 
"0.001963199155243456" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 4751.0) ? " + 
"(b('ndvi_med') <= 4777.75) ? " + 
"(b('ndvi_med') <= 4434.0) ? " + 
"1.1533308393476827e-05" + 
":  " + 
"-0.0014357919978506342" + 
":  " + 
"(b('ndvi_med') <= 4980.0) ? " + 
"0.002770095397051786" + 
":  " + 
"-0.00023317429051974186" + 
":  " + 
"-0.002236760818202732" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1207.25) ? " + 
"(b('ndvi_med') <= 1189.0) ? " + 
"(b('L8b5med') <= 2041.0) ? " + 
"0.0019258239279145231" + 
":  " + 
"-0.0003523027820940167" + 
":  " + 
"(b('gvhmean') <= -13.214736461639404) ? " + 
"-0.004295774332201324" + 
":  " + 
"-0.0011070854588479812" + 
":  " + 
"(b('bare') <= 25.768656730651855) ? " + 
"(b('ndvi_med') <= 1268.5) ? " + 
"0.0021255991922568503" + 
":  " + 
"-2.011840888786831e-05" + 
":  " + 
"(b('gvvmean') <= -11.365689754486084) ? " + 
"0.0035894848401874604" + 
":  " + 
"0.00018571120266545893" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 39.518320083618164) ? " + 
"(b('L8b5med') <= 2197.5) ? " + 
"(b('bare') <= 6.734113693237305) ? " + 
"0.0026055213638151165" + 
":  " + 
"0.0046906227118934385" + 
":  " + 
"(b('lat') <= 39.38346481323242) ? " + 
"4.255043523782977e-05" + 
":  " + 
"0.0034515821398477045" + 
":  " + 
"(b('bulk') <= 145.5) ? " + 
"(b('grass') <= 80.87865447998047) ? " + 
"0.000169961713683098" + 
":  " + 
"-0.0008722192162441909" + 
":  " + 
"(b('gvhk3') <= -0.017140694428235292) ? " + 
"0.0063338029968467435" + 
":  " + 
"-0.0011388433304602564" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2822.25) ? " + 
"(b('L8b10med') <= 2738.5) ? " + 
"(b('L8b3med') <= 1302.75) ? " + 
"-4.7223103585741355e-05" + 
":  " + 
"0.0010184035991124742" + 
":  " + 
"(b('bulk') <= 147.0) ? " + 
"-0.0014152664794470336" + 
":  " + 
"-0.004700637257346478" + 
":  " + 
"(b('ndvi_med') <= 1460.5) ? " + 
"(b('ndvi_med') <= 1398.0) ? " + 
"0.0001324590473943518" + 
":  " + 
"-0.0029984777293333336" + 
":  " + 
"(b('L8b6med') <= 3776.0) ? " + 
"0.0035185434136906085" + 
":  " + 
"0.00025104679247523837" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 760.5) ? " + 
"(b('gvhk3') <= -0.005989341530948877) ? " + 
"-0.0032280472481862332" + 
":  " + 
"(b('L8b5med') <= 2447.5) ? " + 
"-0.0021207166130036304" + 
":  " + 
"3.649381880025358e-05" + 
":  " + 
"(b('L8b3med') <= 1316.75) ? " + 
"(b('L8b3med') <= 1208.0) ? " + 
"5.113772882799711e-05" + 
":  " + 
"-0.001127900514889091" + 
":  " + 
"(b('L8b10med') <= 2629.5) ? " + 
"0.0038781031020134" + 
":  " + 
"-8.700989447728255e-07" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.233184814453125) ? " + 
"-0.0010987200245687768" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"(b('crops') <= 36.508955001831055) ? " + 
"0.0009482995170400632" + 
":  " + 
"0.0017919817064068384" + 
":  " + 
"(b('lat') <= 33.261295318603516) ? " + 
"-0.0011500869488623383" + 
":  " + 
"2.650042015864869e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('L8b3med') <= 1816.0) ? " + 
"(b('L8b3med') <= 1797.0) ? " + 
"8.702220980203851e-07" + 
":  " + 
"0.004506178228217361" + 
":  " + 
"(b('lon') <= -116.71189880371094) ? " + 
"-0.0024268472724042526" + 
":  " + 
"-0.0002714703965170601" + 
":  " + 
"(b('L8b5med') <= 3648.5) ? " + 
"(b('gvhmean') <= -11.06414794921875) ? " + 
"0.002507887305836197" + 
":  " + 
"0.0008609429475043978" + 
":  " + 
"-0.0014500744924948045" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3956.0) ? " + 
"(b('L8b6med') <= 3707.0) ? " + 
"(b('L8b6med') <= 3683.25) ? " + 
"-9.593858752700146e-06" + 
":  " + 
"0.0022755020103649923" + 
":  " + 
"(b('gvhk2') <= 0.272418737411499) ? " + 
"0.0014124228699878758" + 
":  " + 
"-0.0015469644035972382" + 
":  " + 
"(b('sand') <= 62.5) ? " + 
"(b('lon') <= -113.32568359375) ? " + 
"0.00042696171835063707" + 
":  " + 
"0.00196010355095016" + 
":  " + 
"(b('sand') <= 68.0) ? " + 
"-0.0011420237571987298" + 
":  " + 
"-8.897521115604906e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvhk3') <= -0.003810879308730364) ? " + 
"0.004558035615351674" + 
":  " + 
"-0.0015117663174645246" + 
":  " + 
"(b('L8b6med') <= 2241.0) ? " + 
"(b('grass') <= 69.24871444702148) ? " + 
"-0.001075292883569423" + 
":  " + 
"0.0016696512810494904" + 
":  " + 
"(b('L8b6med') <= 2409.5) ? " + 
"0.0006609478724493182" + 
":  " + 
"-2.9263713230445435e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"(b('gvhk2') <= 0.27408288419246674) ? " + 
"(b('gvhk2') <= 0.2617492973804474) ? " + 
"-5.288389106843454e-05" + 
":  " + 
"0.0020063046025616833" + 
":  " + 
"(b('L8b6med') <= 2401.5) ? " + 
"0.00313783173280092" + 
":  " + 
"-0.0014039980824525156" + 
":  " + 
"(b('gvhk2') <= 0.3175591081380844) ? " + 
"(b('L8b10med') <= 2386.5) ? " + 
"0.0031268530475869194" + 
":  " + 
"0.004222317671152553" + 
":  " + 
"(b('ndvi_med') <= 6045.25) ? " + 
"5.222017834816551e-05" + 
":  " + 
"0.0040896190296226265" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.1156606525182724) ? " + 
"(b('gvhk3') <= 0.11459998413920403) ? " + 
"(b('gvhk3') <= 0.06370549276471138) ? " + 
"4.103681371592797e-05" + 
":  " + 
"-0.0006627836968143341" + 
":  " + 
"-0.004684503880041518" + 
":  " + 
"(b('gvhk3') <= 0.18267665803432465) ? " + 
"(b('L8b6med') <= 3579.75) ? " + 
"0.0026714566590513855" + 
":  " + 
"0.0007658534398534006" + 
":  " + 
"(b('gvhk2') <= 0.6248702704906464) ? " + 
"-0.0010166517114361326" + 
":  " + 
"-0.00014261542338179015" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2827.5) ? " + 
"(b('L8b10med') <= 2718.0) ? " + 
"(b('L8b3med') <= 1302.75) ? " + 
"-4.0573657092048544e-05" + 
":  " + 
"0.0009778709829036424" + 
":  " + 
"(b('L8b3med') <= 1383.0) ? " + 
"-0.004180576970319906" + 
":  " + 
"-0.0014883592444902307" + 
":  " + 
"(b('ndvi_med') <= 1460.5) ? " + 
"(b('ndvi_med') <= 1432.0) ? " + 
"8.627312978789078e-05" + 
":  " + 
"-0.003706189141607537" + 
":  " + 
"(b('L8b6med') <= 3776.0) ? " + 
"0.004018110684444918" + 
":  " + 
"0.00023828522939316372" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"(b('gvhk2') <= 0.27408288419246674) ? " + 
"(b('L8b3med') <= 702.5) ? " + 
"0.0013811067482969333" + 
":  " + 
"-0.00010729606424681292" + 
":  " + 
"(b('L8b5med') <= 2642.0) ? " + 
"-0.0021603420132077786" + 
":  " + 
"0.00024428348353361997" + 
":  " + 
"(b('gvhk2') <= 0.3175591081380844) ? " + 
"(b('L8b5med') <= 2356.0) ? " + 
"0.0038000395883749094" + 
":  " + 
"0.0028141214271658332" + 
":  " + 
"(b('ndvi_med') <= 6045.25) ? " + 
"5.753238773097235e-05" + 
":  " + 
"0.003680610810997964" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 761.5) ? " + 
"(b('gvhk2') <= 0.1819647178053856) ? " + 
"(b('bulk') <= 129.5) ? " + 
"-0.006475834731119037" + 
":  " + 
"-0.00018450590381141144" + 
":  " + 
"(b('gvhk2') <= 0.1990862637758255) ? " + 
"0.0026643089633850334" + 
":  " + 
"-0.00019496770210008168" + 
":  " + 
"(b('L8b3med') <= 795.5) ? " + 
"(b('L8b10med') <= 1551.5) ? " + 
"0.004035058012345781" + 
":  " + 
"0.0003947137865957278" + 
":  " + 
"(b('gvhk3') <= -0.02122032456099987) ? " + 
"-0.0011201815973305579" + 
":  " + 
"5.329176146391097e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2381.0) ? " + 
"(b('gvhmean') <= -12.134212970733643) ? " + 
"(b('grass') <= 72.9458999633789) ? " + 
"-0.0027468062045995917" + 
":  " + 
"-0.0018400983335628701" + 
":  " + 
"(b('gvvmean') <= -11.305431842803955) ? " + 
"0.0024298668986394018" + 
":  " + 
"-0.0004341223913084562" + 
":  " + 
"(b('L8b6med') <= 2409.5) ? " + 
"(b('L8b10med') <= 1524.0) ? " + 
"0.00411008677185723" + 
":  " + 
"0.0008984712237994682" + 
":  " + 
"(b('L8b6med') <= 2413.5) ? " + 
"-0.004794262726635093" + 
":  " + 
"1.54699732597594e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -5.297438144683838) ? " + 
"(b('gvhmean') <= -6.832682847976685) ? " + 
"(b('gvvmean') <= -8.499517440795898) ? " + 
"-3.2303644805470884e-05" + 
":  " + 
"0.0007467541719094622" + 
":  " + 
"(b('gvhmean') <= -6.493995904922485) ? " + 
"-0.003789609256168003" + 
":  " + 
"-0.0003848220923239147" + 
":  " + 
"(b('gvhk2') <= 0.7451199889183044) ? " + 
"0.001467939477254085" + 
":  " + 
"0.0006565546222672136" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.06370549276471138) ? " + 
"(b('gvhk3') <= 0.060448601841926575) ? " + 
"(b('grass') <= 73.93266296386719) ? " + 
"-0.0001134196107750829" + 
":  " + 
"0.00040647390079263636" + 
":  " + 
"0.008656424411564279" + 
":  " + 
"(b('lon') <= -106.29857635498047) ? " + 
"(b('L8b6med') <= 2829.0) ? " + 
"-0.004430450945676213" + 
":  " + 
"-0.0006822696867734905" + 
":  " + 
"(b('L8b3med') <= 1289.0) ? " + 
"-5.4879093635864315e-05" + 
":  " + 
"0.0037174501953719796" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 4751.0) ? " + 
"(b('lat') <= 47.74028396606445) ? " + 
"(b('lat') <= 43.976104736328125) ? " + 
"8.083380556452697e-05" + 
":  " + 
"-0.0006965911372448302" + 
":  " + 
"(b('L8b6med') <= 2569.75) ? " + 
"-0.00022002161837457877" + 
":  " + 
"0.0006621451640203411" + 
":  " + 
"-0.0020292449590049166" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 3276.0) ? " + 
"(b('L8b10med') <= 3093.0) ? " + 
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"-0.0001407547475042472" + 
":  " + 
"0.00013079017548022102" + 
":  " + 
"(b('bare') <= 13.268656730651855) ? " + 
"-0.0033403183970972666" + 
":  " + 
"-0.0006921463530848958" + 
":  " + 
"(b('gvhk2') <= 0.13824796676635742) ? " + 
"(b('L8b3med') <= 2368.75) ? " + 
"-0.0012847051315351618" + 
":  " + 
"-9.299800003913228e-05" + 
":  " + 
"(b('L8b3med') <= 1330.75) ? " + 
"0.004959369903511909" + 
":  " + 
"0.000921000227844815" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('bare') <= 46.51470375061035) ? " + 
"(b('L8b3med') <= 1899.75) ? " + 
"3.540005532594609e-05" + 
":  " + 
"-0.0023091056680515573" + 
":  " + 
"(b('gvvmean') <= -13.426556587219238) ? " + 
"0.00033319362253661153" + 
":  " + 
"-0.0013368579393407626" + 
":  " + 
"(b('grass') <= 1.8120805025100708) ? " + 
"-0.0010551757127451183" + 
":  " + 
"(b('gvhmean') <= -11.06414794921875) ? " + 
"0.002127779258252478" + 
":  " + 
"0.0007971019550064573" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvhk2') <= 0.2723564878106117) ? " + 
"0.004079382418385513" + 
":  " + 
"-0.0012887467843326061" + 
":  " + 
"(b('L8b6med') <= 2381.0) ? " + 
"(b('lon') <= -120.5117073059082) ? " + 
"0.001480320340492891" + 
":  " + 
"-0.000588062232667252" + 
":  " + 
"(b('L8b6med') <= 2409.5) ? " + 
"0.0014000454115728326" + 
":  " + 
"-1.7161970697765722e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.044578563421964645) ? " + 
"(b('grass') <= 76.27609634399414) ? " + 
"(b('gvvmean') <= -12.406572818756104) ? " + 
"-0.00040086457493964935" + 
":  " + 
"0.00020074042849342792" + 
":  " + 
"(b('bare') <= 3.5051686763763428) ? " + 
"-0.0003594357965656582" + 
":  " + 
"0.0014900447480592838" + 
":  " + 
"(b('L8b3med') <= 940.5) ? " + 
"(b('gvhk2') <= 0.40932148694992065) ? " + 
"0.007767795763840596" + 
":  " + 
"-2.011621287850784e-05" + 
":  " + 
"(b('L8b10med') <= 2555.0) ? " + 
"-0.0019690805128772166" + 
":  " + 
"0.00026697086959336856" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"0.001411036527292131" + 
":  " + 
"(b('L8b3med') <= 615.5) ? " + 
"(b('L8b5med') <= 2517.5) ? " + 
"0.0009679505357642545" + 
":  " + 
"-0.0016551305139226116" + 
":  " + 
"(b('L8b3med') <= 678.0) ? " + 
"0.0010603623126352974" + 
":  " + 
"-3.24550060746013e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2478.5) ? " + 
"(b('gvvmean') <= -11.771821022033691) ? " + 
"(b('L8b6med') <= 2464.0) ? " + 
"-0.0010955515567310338" + 
":  " + 
"-0.007529144713041076" + 
":  " + 
"(b('lon') <= -71.2344970703125) ? " + 
"0.0019211249601209265" + 
":  " + 
"-0.00034798666657314705" + 
":  " + 
"(b('L8b6med') <= 2491.75) ? " + 
"(b('grass') <= 8.961464643478394) ? " + 
"0.004998760157719134" + 
":  " + 
"0.0024980002594308937" + 
":  " + 
"(b('gvhk2') <= 0.5480722784996033) ? " + 
"6.552603559845381e-05" + 
":  " + 
"-0.0009266038470299368" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2827.5) ? " + 
"(b('L8b10med') <= 2718.0) ? " + 
"(b('L8b3med') <= 1302.75) ? " + 
"-4.11236584951968e-05" + 
":  " + 
"0.000920689271582423" + 
":  " + 
"(b('ndvi_med') <= 1505.0) ? " + 
"-0.0008096204782634224" + 
":  " + 
"-0.00302921107739966" + 
":  " + 
"(b('L8b10med') <= 2851.0) ? " + 
"(b('L8b10med') <= 2835.5) ? " + 
"0.0022009305828032677" + 
":  " + 
"0.0034215899591099885" + 
":  " + 
"(b('crops') <= 77.41878509521484) ? " + 
"0.0002912235699958919" + 
":  " + 
"-0.002241463810498027" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"(b('gvhk3') <= -0.006556568201631308) ? " + 
"(b('bulk') <= 135.5) ? " + 
"0.0003689332498879486" + 
":  " + 
"-0.003707756643435745" + 
":  " + 
"(b('lat') <= 43.31694984436035) ? " + 
"0.00028990013835337536" + 
":  " + 
"-0.00047311846831506605" + 
":  " + 
"(b('gvhk2') <= 0.3175591081380844) ? " + 
"(b('bare') <= 9.604617357254028) ? " + 
"0.002318622964495462" + 
":  " + 
"0.00320594930958365" + 
":  " + 
"(b('ndvi_med') <= 6045.25) ? " + 
"6.057991299555874e-05" + 
":  " + 
"0.00328141255755543" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 934.5) ? " + 
"(b('bulk') <= 145.5) ? " + 
"(b('L8b3med') <= 933.0) ? " + 
"0.00021220199816896932" + 
":  " + 
"0.006985763459054134" + 
":  " + 
"(b('L8b3med') <= 925.5) ? " + 
"-0.0009342012669056543" + 
":  " + 
"-0.005058982200832202" + 
":  " + 
"(b('L8b3med') <= 949.5) ? " + 
"(b('gvhk3') <= 0.007267483975738287) ? " + 
"-0.0054537896597121605" + 
":  " + 
"-0.0010081758260266716" + 
":  " + 
"(b('gvhk2') <= 0.4450976401567459) ? " + 
"-0.0001270410979891744" + 
":  " + 
"0.0006332535973271337" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -11.305431842803955) ? " + 
"(b('gvvmean') <= -11.597250938415527) ? " + 
"(b('L8b5med') <= 2248.0) ? " + 
"-0.0006646319031274244" + 
":  " + 
"0.00010839231129078348" + 
":  " + 
"(b('L8b3med') <= 771.0) ? " + 
"0.004676864976945458" + 
":  " + 
"0.0016864838464535291" + 
":  " + 
"(b('gvhmean') <= -10.936347007751465) ? " + 
"(b('lat') <= 39.58083915710449) ? " + 
"0.0016569006376001376" + 
":  " + 
"-0.0019185712330802638" + 
":  " + 
"(b('crops') <= 68.24193572998047) ? " + 
"-0.00037591893871674517" + 
":  " + 
"0.0007318795017368236" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 133.5) ? " + 
"(b('lat') <= 44.645219802856445) ? " + 
"(b('lat') <= 42.85914611816406) ? " + 
"0.0003091588962836009" + 
":  " + 
"-0.0019029032479842794" + 
":  " + 
"(b('gvhk2') <= 0.2859973758459091) ? " + 
"0.0008365089405093917" + 
":  " + 
"-0.000354471718891835" + 
":  " + 
"(b('L8b6med') <= 2680.0) ? " + 
"(b('L8b6med') <= 2654.25) ? " + 
"0.0004718126687617376" + 
":  " + 
"0.0036353139029237" + 
":  " + 
"(b('gvvmean') <= -10.855900764465332) ? " + 
"-0.00016598326990262404" + 
":  " + 
"0.0009746763042674467" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.1156606525182724) ? " + 
"(b('gvhk3') <= 0.11459998413920403) ? " + 
"(b('gvhk2') <= 0.5480722784996033) ? " + 
"2.9987116638551634e-05" + 
":  " + 
"-0.0005599193796479244" + 
":  " + 
"-0.004103412114689647" + 
":  " + 
"(b('gvhk3') <= 0.18267665803432465) ? " + 
"(b('gvvmean') <= -14.359652519226074) ? " + 
"0.0007600983610643666" + 
":  " + 
"0.0023552767345687564" + 
":  " + 
"(b('gvhk2') <= 0.6248702704906464) ? " + 
"-0.0008695493721421269" + 
":  " + 
"-0.00019037218140150955" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('lat') <= 55.93754959106445) ? " + 
"(b('gvhk3') <= -0.014465656131505966) ? " + 
"0.0006226789382957719" + 
":  " + 
"-2.9737519335399673e-05" + 
":  " + 
"(b('gvhmean') <= -12.964019298553467) ? " + 
"-0.002850168764076233" + 
":  " + 
"-0.000205743969844831" + 
":  " + 
"(b('gvhk3') <= -0.11274298606440425) ? " + 
"0.0006009206517799542" + 
":  " + 
"0.0020132307081248413" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhmean') <= -11.305431842803955) ? " + 
"(b('gvvmean') <= -11.597250938415527) ? " + 
"(b('L8b5med') <= 2248.0) ? " + 
"-0.0005912933280187467" + 
":  " + 
"0.0001038652420303668" + 
":  " + 
"(b('L8b3med') <= 771.0) ? " + 
"0.004134302947995133" + 
":  " + 
"0.0014496312529446802" + 
":  " + 
"(b('gvhmean') <= -10.936347007751465) ? " + 
"(b('lat') <= 39.58083915710449) ? " + 
"0.0014865240764779335" + 
":  " + 
"-0.001709431992196638" + 
":  " + 
"(b('crops') <= 68.24193572998047) ? " + 
"-0.00033994795910094396" + 
":  " + 
"0.0006311756857608288" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2111.5) ? " + 
"(b('lat') <= 40.11824989318848) ? " + 
"-0.004702013891373702" + 
":  " + 
"(b('L8b10med') <= 1961.0) ? " + 
"-0.00012000378461361413" + 
":  " + 
"0.0011759840425587353" + 
":  " + 
"(b('L8b5med') <= 2123.5) ? " + 
"-0.004826485310745893" + 
":  " + 
"(b('L8b5med') <= 2216.25) ? " + 
"-0.0008934974524116575" + 
":  " + 
"2.4748025183816818e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 91.94809341430664) ? " + 
"(b('grass') <= 89.08682632446289) ? " + 
"(b('L8b5med') <= 2180.0) ? " + 
"0.00042815646780938006" + 
":  " + 
"-6.275644878733655e-05" + 
":  " + 
"(b('ndvi_med') <= 1985.75) ? " + 
"-0.0011915368511414837" + 
":  " + 
"-0.0036636139146602326" + 
":  " + 
"(b('gvhk2') <= 0.22952740639448166) ? " + 
"-0.004231812502236337" + 
":  " + 
"(b('gvhk3') <= 0.008598358836025) ? " + 
"0.0031627700678696358" + 
":  " + 
"0.0003835197242675253" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 1112.5) ? " + 
"(b('gvvmean') <= -11.045052528381348) ? " + 
"-0.0008723261615749267" + 
":  " + 
"0.003517843088496092" + 
":  " + 
"(b('gvhk3') <= -0.006556568201631308) ? " + 
"(b('gvhk3') <= -0.009026424493640661) ? " + 
"3.349858287136126e-05" + 
":  " + 
"-0.0020639500643250893" + 
":  " + 
"(b('gvhk3') <= -0.00421099248342216) ? " + 
"0.0017636468853866744" + 
":  " + 
"3.338180271013838e-07" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 56.031551361083984) ? " + 
"(b('L8b3med') <= 934.5) ? " + 
"(b('bulk') <= 145.5) ? " + 
"0.00034067424747315374" + 
":  " + 
"-0.0011889981363196996" + 
":  " + 
"(b('lat') <= 44.06207466125488) ? " + 
"5.027779180977806e-05" + 
":  " + 
"-0.0006978669734031969" + 
":  " + 
"(b('gvhk3') <= -0.10665059834718704) ? " + 
"(b('gvhk2') <= 0.797989010810852) ? " + 
"0.0019346315478153686" + 
":  " + 
"1.97044647855249e-05" + 
":  " + 
"(b('gvhk3') <= 0.04623102769255638) ? " + 
"-0.002061963617853959" + 
":  " + 
"-0.00040030721155114024" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -13.548450469970703) ? " + 
"(b('gvvmean') <= -13.585102558135986) ? " + 
"(b('lon') <= -121.92677688598633) ? " + 
"-0.0039859292195589535" + 
":  " + 
"0.00011745504938260004" + 
":  " + 
"(b('sand') <= 53.5) ? " + 
"0.0034505036446759035" + 
":  " + 
"0.0008753338198703026" + 
":  " + 
"(b('gvhmean') <= -13.478110313415527) ? " + 
"(b('L8b6med') <= 2710.0) ? " + 
"-0.0005842880283950698" + 
":  " + 
"-0.003498858156332665" + 
":  " + 
"(b('gvvmean') <= -13.455461502075195) ? " + 
"0.003715084119146325" + 
":  " + 
"-4.417905766592121e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.0023724050261080265) ? " + 
"(b('gvhk3') <= 0.0018904488533735275) ? " + 
"(b('gvhk3') <= 0.0017356299213133752) ? " + 
"-9.626392724810666e-05" + 
":  " + 
"0.0016445053736895941" + 
":  " + 
"(b('L8b3med') <= 1115.5) ? " + 
"-0.004447170675034015" + 
":  " + 
"-0.0006782538638209212" + 
":  " + 
"(b('gvhk3') <= 0.003070435719564557) ? " + 
"(b('L8b6med') <= 2983.5) ? " + 
"0.0004999988716191117" + 
":  " + 
"0.004130909775764417" + 
":  " + 
"(b('gvhk2') <= 0.1819647178053856) ? " + 
"-0.002964204516286803" + 
":  " + 
"7.741337618979886e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 73.93266296386719) ? " + 
"(b('gvhk2') <= 0.3871832937002182) ? " + 
"(b('sand') <= 28.0) ? " + 
"0.0010220785218174892" + 
":  " + 
"-0.0002795035391323663" + 
":  " + 
"(b('gvhk2') <= 0.41281338036060333) ? " + 
"0.0023565736240236876" + 
":  " + 
"-0.000100161942530782" + 
":  " + 
"(b('L8b10med') <= 2583.25) ? " + 
"(b('L8b5med') <= 2282.5) ? " + 
"-0.00042357468767782844" + 
":  " + 
"0.0009686166487189734" + 
":  " + 
"(b('gvhk2') <= 0.2878238558769226) ? " + 
"-0.0031088158931057534" + 
":  " + 
"2.3258475408262568e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('gvvmean') <= -9.522472858428955) ? " + 
"0.001413131849413364" + 
":  " + 
"0.00042550253092318396" + 
":  " + 
"(b('gvhk2') <= 0.08685321733355522) ? " + 
"(b('lat') <= 38.521549224853516) ? " + 
"-0.0003953776608808142" + 
":  " + 
"-0.002362883784354943" + 
":  " + 
"(b('gvhk2') <= 0.09861317649483681) ? " + 
"0.00180283412995242" + 
":  " + 
"5.936358448751011e-07" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.233184814453125) ? " + 
"-0.0009177838619025581" + 
":  " + 
"(b('lat') <= -34.90736961364746) ? " + 
"0.0010617632527531117" + 
":  " + 
"(b('lat') <= -34.72389030456543) ? " + 
"-0.0018547905803016074" + 
":  " + 
"7.169205344101871e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"0.0012719285062997299" + 
":  " + 
"(b('bulk') <= 132.5) ? " + 
"(b('L8b6med') <= 2569.75) ? " + 
"-0.0007385067758559148" + 
":  " + 
"0.0002811617503004928" + 
":  " + 
"(b('L8b6med') <= 2680.0) ? " + 
"0.00047219676140970615" + 
":  " + 
"-5.780338817150872e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 166.0) ? " + 
"(b('lon') <= -121.0405044555664) ? " + 
"-0.0007494105354295677" + 
":  " + 
"1.0561756259084916e-05" + 
":  " + 
"(b('gvhmean') <= -13.798814296722412) ? " + 
"0.0002747122695896456" + 
":  " + 
"0.001709478370842149" + 
":  " + 
"-0.0017642933354745233" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 43.6143741607666) ? " + 
"(b('grass') <= 37.14488410949707) ? " + 
"(b('ndvi_med') <= 4980.0) ? " + 
"1.656081780224671e-05" + 
":  " + 
"-0.001145496230743323" + 
":  " + 
"(b('gvhk3') <= 0.0008025229253689758) ? " + 
"-8.082523324396083e-05" + 
":  " + 
"-0.0024974049351551633" + 
":  " + 
"(b('L8b3med') <= 1486.0) ? " + 
"(b('L8b5med') <= 2843.75) ? " + 
"7.266374053761866e-05" + 
":  " + 
"0.0013663544018568555" + 
":  " + 
"(b('L8b6med') <= 3682.5) ? " + 
"-0.0014299979224659514" + 
":  " + 
"0.0007177616867166114" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.0023724050261080265) ? " + 
"(b('gvhk3') <= 0.0018904488533735275) ? " + 
"(b('L8b10med') <= 1112.5) ? " + 
"0.0031232777896377795" + 
":  " + 
"-6.64876797683626e-05" + 
":  " + 
"(b('bare') <= 43.826087951660156) ? " + 
"-0.0033678370371686556" + 
":  " + 
"0.00015844253099849687" + 
":  " + 
"(b('gvhk3') <= 0.003070435719564557) ? " + 
"(b('sand') <= 41.0) ? " + 
"0.004411840472027036" + 
":  " + 
"0.0011881852146796712" + 
":  " + 
"(b('gvhk2') <= 0.1819647178053856) ? " + 
"-0.0026419653576761223" + 
":  " + 
"6.951542381213479e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2827.5) ? " + 
"(b('L8b10med') <= 2718.0) ? " + 
"(b('L8b3med') <= 1302.75) ? " + 
"-4.055853290387461e-05" + 
":  " + 
"0.000839325656850438" + 
":  " + 
"(b('gvvmean') <= -12.207300662994385) ? " + 
"-0.0011058437037214954" + 
":  " + 
"-0.0032850579770268666" + 
":  " + 
"(b('L8b5med') <= 2844.0) ? " + 
"(b('lat') <= 35.5047492980957) ? " + 
"-0.0001219178245129059" + 
":  " + 
"0.0016840645040805604" + 
":  " + 
"(b('L8b10med') <= 2903.25) ? " + 
"0.0026286773551150305" + 
":  " + 
"-0.0005712859473780778" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.0018428146037772625" + 
":  " + 
"(b('gvvmean') <= -9.219711780548096) ? " + 
"(b('gvhmean') <= -9.335216999053955) ? " + 
"-1.141351696545733e-05" + 
":  " + 
"-0.0035683369798750197" + 
":  " + 
"(b('bulk') <= 137.5) ? " + 
"0.00017230979268022912" + 
":  " + 
"0.00237381989661134" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('bare') <= 46.51470375061035) ? " + 
"(b('L8b3med') <= 1899.75) ? " + 
"2.8097005839586266e-05" + 
":  " + 
"-0.0018981349862448316" + 
":  " + 
"(b('gvvmean') <= -13.426556587219238) ? " + 
"0.00029772456190565143" + 
":  " + 
"-0.0011043690134663387" + 
":  " + 
"(b('L8b6med') <= 4419.0) ? " + 
"(b('L8b5med') <= 3089.0) ? " + 
"0.0007323574948471662" + 
":  " + 
"0.0018270262475870713" + 
":  " + 
"-0.0008694418041876872" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -11.252465724945068) ? " + 
"(b('gvhmean') <= -11.597250938415527) ? " + 
"(b('L8b10med') <= 1356.5) ? " + 
"-0.0014177098673511912" + 
":  " + 
"4.0007543260587976e-05" + 
":  " + 
"(b('gvhk3') <= -0.00931989517994225) ? " + 
"-0.0014725824370238894" + 
":  " + 
"0.0018689731537656004" + 
":  " + 
"(b('gvvmean') <= -11.105718612670898) ? " + 
"(b('L8b5med') <= 2963.75) ? " + 
"-0.0010533539817736955" + 
":  " + 
"-0.003226839802333785" + 
":  " + 
"(b('gvvmean') <= -11.078354358673096) ? " + 
"0.004117020967519133" + 
":  " + 
"-2.668975597600277e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.044578563421964645) ? " + 
"(b('grass') <= 76.27609634399414) ? " + 
"(b('gvvmean') <= -12.406572818756104) ? " + 
"-0.00031553954521527006" + 
":  " + 
"0.00015070012742656922" + 
":  " + 
"(b('bare') <= 3.5051686763763428) ? " + 
"-0.00022899440978022082" + 
":  " + 
"0.0011950348145439169" + 
":  " + 
"(b('gvvmean') <= -14.079734325408936) ? " + 
"(b('bulk') <= 141.5) ? " + 
"0.005985207268641574" + 
":  " + 
"-3.7796906002642364e-05" + 
":  " + 
"(b('gvhk3') <= 0.08871250972151756) ? " + 
"-0.0018867493384910293" + 
":  " + 
"0.00013240556027157012" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"0.0012390882939169734" + 
":  " + 
"(b('ndvi_med') <= 2561.5) ? " + 
"(b('L8b6med') <= 2618.5) ? " + 
"0.0012388062137809737" + 
":  " + 
"-2.6985282149709893e-05" + 
":  " + 
"(b('ndvi_med') <= 2814.0) ? " + 
"-0.0013728408232272357" + 
":  " + 
"-1.3957206624510259e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2385.0) ? " + 
"(b('L8b5med') <= 3218.0) ? " + 
"(b('L8b5med') <= 3172.0) ? " + 
"-0.00028287917770145364" + 
":  " + 
"0.0021583871684548173" + 
":  " + 
"(b('gvvmean') <= -10.588149547576904) ? " + 
"-0.0015305166771331646" + 
":  " + 
"-0.002270481614433578" + 
":  " + 
"(b('L8b6med') <= 2409.5) ? " + 
"(b('gvhk3') <= 0.0061456491239368916) ? " + 
"0.0005645235919757546" + 
":  " + 
"0.0032152354744193015" + 
":  " + 
"(b('L8b6med') <= 2413.5) ? " + 
"-0.0037269671251189546" + 
":  " + 
"4.265444086622117e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 3276.0) ? " + 
"(b('L8b10med') <= 3093.0) ? " + 
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"-0.00012469304541963647" + 
":  " + 
"0.000111689272693362" + 
":  " + 
"(b('L8b10med') <= 3122.0) ? " + 
"-0.0027479830792386806" + 
":  " + 
"-0.000412459478191584" + 
":  " + 
"(b('gvhk2') <= 0.13824796676635742) ? " + 
"(b('L8b3med') <= 2368.75) ? " + 
"-0.0011140202714696318" + 
":  " + 
"-3.674849719474682e-05" + 
":  " + 
"(b('grass') <= 44.49862861633301) ? " + 
"0.0008240525585286483" + 
":  " + 
"0.004214390293304962" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1316.75) ? " + 
"(b('L8b3med') <= 1208.0) ? " + 
"(b('L8b3med') <= 1125.75) ? " + 
"-4.204831670035628e-05" + 
":  " + 
"0.0007259810114429557" + 
":  " + 
"(b('gvhk3') <= 0.00439100107178092) ? " + 
"1.9115339197528388e-05" + 
":  " + 
"-0.0021270333902477533" + 
":  " + 
"(b('ndvi_med') <= 1538.0) ? " + 
"(b('ndvi_med') <= 1505.0) ? " + 
"0.0001074118846494551" + 
":  " + 
"-0.0024340024806333523" + 
":  " + 
"(b('L8b6med') <= 3754.5) ? " + 
"0.003093229249470053" + 
":  " + 
"-0.0002993238701102328" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('L8b6med') <= 2385.0) ? " + 
"(b('L8b10med') <= 1218.75) ? " + 
"0.0007489287965224203" + 
":  " + 
"-0.0004242615468122831" + 
":  " + 
"(b('L8b6med') <= 2409.5) ? " + 
"0.0014075415134092353" + 
":  " + 
"-2.5964148760558606e-06" + 
":  " + 
"-0.0017042525297212424" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2705.5) ? " + 
"(b('gvhk3') <= -0.0009279971709474921) ? " + 
"(b('bulk') <= 140.5) ? " + 
"3.0285999773112814e-05" + 
":  " + 
"-0.001737503678596635" + 
":  " + 
"(b('gvvmean') <= -10.195457458496094) ? " + 
"0.00020515492076936793" + 
":  " + 
"-0.000936278055557608" + 
":  " + 
"(b('gvhk2') <= 0.5286999940872192) ? " + 
"(b('gvvmean') <= -9.61302661895752) ? " + 
"0.0001239943855295412" + 
":  " + 
"0.00186600674499376" + 
":  " + 
"(b('L8b10med') <= 1539.5) ? " + 
"0.0021738314652363644" + 
":  " + 
"-0.0015912195748541795" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2111.5) ? " + 
"(b('lat') <= 40.11824989318848) ? " + 
"-0.0033784927203572984" + 
":  " + 
"(b('L8b10med') <= 1961.0) ? " + 
"-0.00012984494945601034" + 
":  " + 
"0.000991899242982232" + 
":  " + 
"(b('L8b5med') <= 2123.5) ? " + 
"-0.004064840762255453" + 
":  " + 
"(b('gvhmean') <= -13.548450469970703) ? " + 
"0.00018940232593044407" + 
":  " + 
"-0.00014252657066464314" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.1156606525182724) ? " + 
"(b('gvhk3') <= 0.11459998413920403) ? " + 
"(b('gvhk2') <= 0.5480722784996033) ? " + 
"2.8386429208370135e-05" + 
":  " + 
"-0.0005276956520804627" + 
":  " + 
"-0.0035770104555139653" + 
":  " + 
"(b('gvhk3') <= 0.18267665803432465) ? " + 
"(b('bulk') <= 130.0) ? " + 
"0.002983034995273748" + 
":  " + 
"0.0010280080531762242" + 
":  " + 
"(b('L8b5med') <= 2375.5) ? " + 
"0.0001437092818295585" + 
":  " + 
"-0.0004928223662337937" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"(b('gvhk2') <= 0.27408288419246674) ? " + 
"(b('gvhk2') <= 0.2617492973804474) ? " + 
"-5.4358937064355585e-05" + 
":  " + 
"0.0014830620303343306" + 
":  " + 
"(b('L8b5med') <= 2642.0) ? " + 
"-0.0016717770273945508" + 
":  " + 
"0.00018838230088441543" + 
":  " + 
"(b('gvhk2') <= 0.3175591081380844) ? " + 
"(b('gvhk2') <= 0.31713680922985077) ? " + 
"0.0018352303743807974" + 
":  " + 
"0.0028496514030352804" + 
":  " + 
"(b('L8b6med') <= 3707.0) ? " + 
"0.00015790633769250048" + 
":  " + 
"-0.0005860399022107795" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 4160.75) ? " + 
"(b('L8b5med') <= 2918.0) ? " + 
"(b('L8b5med') <= 2907.0) ? " + 
"1.2765669009660825e-05" + 
":  " + 
"0.003360674240359088" + 
":  " + 
"(b('L8b5med') <= 3005.5) ? " + 
"-0.0015977835470753735" + 
":  " + 
"1.2294620423343995e-05" + 
":  " + 
"(b('ndvi_med') <= 932.5) ? " + 
"-0.00036632662157272053" + 
":  " + 
"(b('lon') <= -115.18332290649414) ? " + 
"0.0007230428558887766" + 
":  " + 
"0.0016799537313011217" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1316.75) ? " + 
"(b('L8b3med') <= 1208.0) ? " + 
"(b('ndvi_med') <= 952.0) ? " + 
"0.0033152444604789555" + 
":  " + 
"9.920361568701774e-06" + 
":  " + 
"(b('gvhk3') <= 0.00439100107178092) ? " + 
"4.1252074955646735e-05" + 
":  " + 
"-0.0018856843940277842" + 
":  " + 
"(b('sand') <= 41.5) ? " + 
"(b('L8b6med') <= 3703.5) ? " + 
"0.003358669840755705" + 
":  " + 
"0.00037702579878778203" + 
":  " + 
"(b('grass') <= 69.35115432739258) ? " + 
"0.00021746416155925168" + 
":  " + 
"-0.0013348499978389436" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 25.16578960418701) ? " + 
"(b('lon') <= 22.981855392456055) ? " + 
"(b('ndvi_med') <= 4980.0) ? " + 
"3.145276002083084e-05" + 
":  " + 
"-0.0006779420415482454" + 
":  " + 
"(b('gvhk3') <= 0.011928407009691) ? " + 
"0.0006904269383353479" + 
":  " + 
"0.002616175195488485" + 
":  " + 
"(b('ndvi_med') <= 2199.75) ? " + 
"(b('ndvi_med') <= 1543.5) ? " + 
"-0.0015519617757229834" + 
":  " + 
"0.0013419533235546502" + 
":  " + 
"(b('sand') <= 36.5) ? " + 
"-0.0020458261032948815" + 
":  " + 
"-0.00042346195581835413" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.521310806274414) ? " + 
"(b('L8b5med') <= 2200.5) ? " + 
"0.0024358313486982086" + 
":  " + 
"(b('L8b10med') <= 2664.25) ? " + 
"-0.0007786026795682311" + 
":  " + 
"1.3411690155711229e-05" + 
":  " + 
"(b('lat') <= 34.940629959106445) ? " + 
"(b('gvhk2') <= 0.23021845519542694) ? " + 
"0.0005671154035615059" + 
":  " + 
"0.00272953168618173" + 
":  " + 
"(b('lat') <= 35.37127494812012) ? " + 
"-0.0010723167304750216" + 
":  " + 
"1.4417249562397787e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2705.5) ? " + 
"(b('L8b6med') <= 3397.75) ? " + 
"(b('gvvmean') <= -13.548450469970703) ? " + 
"0.0005070840100077337" + 
":  " + 
"-0.0001893698287865317" + 
":  " + 
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"-0.0018837207035897147" + 
":  " + 
"-0.00010701326740923426" + 
":  " + 
"(b('gvhmean') <= -15.11733102798462) ? " + 
"(b('gvhmean') <= -15.360464572906494) ? " + 
"-0.0005051423114021313" + 
":  " + 
"-0.0019732281515861907" + 
":  " + 
"(b('gvvmean') <= -14.510242938995361) ? " + 
"0.0015949079952950352" + 
":  " + 
"0.0001151268286757915" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.1156606525182724) ? " + 
"(b('gvhk3') <= 0.10750368982553482) ? " + 
"(b('gvhk3') <= 0.0991559848189354) ? " + 
"-1.265398658197677e-05" + 
":  " + 
"0.002747421886392709" + 
":  " + 
"(b('gvhk3') <= 0.11459998413920403) ? " + 
"-0.0013061607103826978" + 
":  " + 
"-0.0029936108745196033" + 
":  " + 
"(b('gvhk3') <= 0.15443094074726105) ? " + 
"(b('sand') <= 78.0) ? " + 
"0.0010110554866067888" + 
":  " + 
"0.002681022240839631" + 
":  " + 
"(b('lon') <= 77.77219295501709) ? " + 
"-0.00028798357339427093" + 
":  " + 
"0.00044855951363279023" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 600.5) ? " + 
"(b('gvvmean') <= -14.234665393829346) ? " + 
"-0.0015032215625035428" + 
":  " + 
"(b('lat') <= 53.60539627075195) ? " + 
"0.0022910823033007732" + 
":  " + 
"0.0006624598988005881" + 
":  " + 
"(b('L8b3med') <= 615.5) ? " + 
"(b('L8b10med') <= 1537.5) ? " + 
"-0.0021260600669747616" + 
":  " + 
"0.0006562934769039075" + 
":  " + 
"(b('L8b3med') <= 648.5) ? " + 
"0.0008794064641119981" + 
":  " + 
"-1.7349514739992237e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvmean') <= -16.72476100921631) ? " + 
"(b('gvhmean') <= -16.98458480834961) ? " + 
"(b('gvhk2') <= 0.49988730251789093) ? " + 
"-0.0003927142891149242" + 
":  " + 
"0.0008775836939783621" + 
":  " + 
"-0.0017303856711831378" + 
":  " + 
"(b('grass') <= 91.94809341430664) ? " + 
"(b('grass') <= 89.08682632446289) ? " + 
"3.421419819433512e-06" + 
":  " + 
"-0.0017142581555165404" + 
":  " + 
"(b('gvhk2') <= 0.22952740639448166) ? " + 
"-0.0030926098524206858" + 
":  " + 
"0.0007894573546097883" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.05663141794502735) ? " + 
"(b('gvvmean') <= -9.522472858428955) ? " + 
"0.001175380738031459" + 
":  " + 
"0.0003472583969970934" + 
":  " + 
"(b('gvhk2') <= 0.08685321733355522) ? " + 
"(b('sand') <= 65.0) ? " + 
"-0.0020636925758042665" + 
":  " + 
"-0.00014154720763588646" + 
":  " + 
"(b('gvhk2') <= 0.09861317649483681) ? " + 
"0.001605968847607657" + 
":  " + 
"-4.524382624543557e-07" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 133.5) ? " + 
"(b('lat') <= 44.645219802856445) ? " + 
"(b('lat') <= 42.85914611816406) ? " + 
"0.00024512517161405745" + 
":  " + 
"-0.0014594669533508537" + 
":  " + 
"(b('gvhk2') <= 0.2859973758459091) ? " + 
"0.0006492288946287313" + 
":  " + 
"-0.0002921634381271851" + 
":  " + 
"(b('L8b6med') <= 2665.5) ? " + 
"(b('L8b6med') <= 2654.25) ? " + 
"0.0003485619364714358" + 
":  " + 
"0.004167613374203155" + 
":  " + 
"(b('gvvmean') <= -10.855900764465332) ? " + 
"-0.00012152606537635196" + 
":  " + 
"0.0007661623671937666" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.0023724050261080265) ? " + 
"(b('gvhk3') <= 0.0018904488533735275) ? " + 
"(b('lat') <= 44.11789512634277) ? " + 
"0.0001821763164891706" + 
":  " + 
"-0.0002937362388688894" + 
":  " + 
"(b('bare') <= 43.826087951660156) ? " + 
"-0.0028601147398086696" + 
":  " + 
"0.00019634862439742162" + 
":  " + 
"(b('gvhk3') <= 0.003070435719564557) ? " + 
"(b('L8b6med') <= 2983.5) ? " + 
"0.0003464987049676266" + 
":  " + 
"0.0033678928823345777" + 
":  " + 
"(b('gvhk2') <= 0.1819647178053856) ? " + 
"-0.0023429777431541164" + 
":  " + 
"6.144533692252175e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 166.0) ? " + 
"(b('lon') <= -121.0405044555664) ? " + 
"-0.0007128468537432835" + 
":  " + 
"1.058160821580284e-05" + 
":  " + 
"(b('gvvmean') <= -13.798814296722412) ? " + 
"0.00025623721280409323" + 
":  " + 
"0.0014733251708660966" + 
":  " + 
"-0.0015166999572895912" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.11607062816619873) ? " + 
"(b('ndvi_med') <= 6071.5) ? " + 
"(b('gvhk2') <= 0.04939664155244827) ? " + 
"0.0005011514562709481" + 
":  " + 
"-0.0009199077616648021" + 
":  " + 
"(b('L8b5med') <= 4692.5) ? " + 
"0.0007699566502739064" + 
":  " + 
"0.0020290238188428456" + 
":  " + 
"(b('L8b5med') <= 4710.5) ? " + 
"(b('L8b5med') <= 3820.5) ? " + 
"1.4281654752405428e-05" + 
":  " + 
"0.0012914061736340298" + 
":  " + 
"(b('lat') <= 53.63397979736328) ? " + 
"-0.0029249554478574247" + 
":  " + 
"-0.0012242236314470856" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.8269027173519135) ? " + 
"(b('gvhk3') <= -0.006239350885152817) ? " + 
"(b('lon') <= -105.14809799194336) ? " + 
"-0.0012168325714284312" + 
":  " + 
"0.0001266380831669831" + 
":  " + 
"(b('gvhk3') <= -0.004809212172403932) ? " + 
"0.0020513080910840725" + 
":  " + 
"1.3686859628446094e-06" + 
":  " + 
"(b('sand') <= 74.0) ? " + 
"0.0002803783719592112" + 
":  " + 
"0.0011575064630622162" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1316.75) ? " + 
"(b('L8b3med') <= 1311.75) ? " + 
"(b('L8b3med') <= 1208.0) ? " + 
"2.173115165951411e-05" + 
":  " + 
"-0.0005698544627915981" + 
":  " + 
"-0.003364800628116775" + 
":  " + 
"(b('sand') <= 41.5) ? " + 
"(b('L8b6med') <= 3703.5) ? " + 
"0.0030453494793916077" + 
":  " + 
"0.0003530781253982644" + 
":  " + 
"(b('gvvmean') <= -12.312299251556396) ? " + 
"-0.00037722617366145206" + 
":  " + 
"0.0006259297076842763" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 400.0) ? " + 
"-0.0014766004228951336" + 
":  " + 
"(b('gvhmean') <= -9.219711780548096) ? " + 
"(b('gvvmean') <= -9.335216999053955) ? " + 
"-1.1004103469840158e-05" + 
":  " + 
"-0.002996493868470812" + 
":  " + 
"(b('gvvmean') <= -8.284955501556396) ? " + 
"0.0012331566035478042" + 
":  " + 
"-6.728691663136695e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.06370549276471138) ? " + 
"(b('gvhk3') <= 0.060448601841926575) ? " + 
"(b('grass') <= 73.93266296386719) ? " + 
"-7.743289696013736e-05" + 
":  " + 
"0.00029211167911662834" + 
":  " + 
"0.00527162069020487" + 
":  " + 
"(b('gvhk3') <= 0.08321710303425789) ? " + 
"(b('L8b6med') <= 2829.0) ? " + 
"-0.0031317615789050596" + 
":  " + 
"-0.0006451644109167799" + 
":  " + 
"(b('gvhk2') <= 0.4881007522344589) ? " + 
"-0.0012409072048284397" + 
":  " + 
"0.0006571375028116873" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2637.5) ? " + 
"(b('L8b6med') <= 3432.0) ? " + 
"(b('L8b10med') <= 2074.75) ? " + 
"-0.00023663516402076793" + 
":  " + 
"0.0003231383426111975" + 
":  " + 
"(b('L8b6med') <= 3488.5) ? " + 
"-0.0026686726790343535" + 
":  " + 
"-0.0004394071425531484" + 
":  " + 
"(b('L8b5med') <= 2655.5) ? " + 
"(b('sand') <= 36.0) ? " + 
"0.004399801386235719" + 
":  " + 
"0.0006549155862147632" + 
":  " + 
"(b('gvhk3') <= -0.0002864523994503543) ? " + 
"0.00039453836772063784" + 
":  " + 
"-0.00011938177854315211" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.005068940808996558) ? " + 
"(b('gvhk3') <= 0.004517511697486043) ? " + 
"(b('lat') <= 44.11789512634277) ? " + 
"0.0002773542972537019" + 
":  " + 
"-0.00033728724239318633" + 
":  " + 
"(b('gvhk3') <= 0.0045777440536767244) ? " + 
"-0.005154723990658524" + 
":  " + 
"-0.0015468294377372384" + 
":  " + 
"(b('gvhk2') <= 0.2010231539607048) ? " + 
"(b('gvvmean') <= -11.971923351287842) ? " + 
"0.0037120747564711315" + 
":  " + 
"0.0025687591229841406" + 
":  " + 
"(b('gvhk2') <= 0.21418041735887527) ? " + 
"-0.0022932033168743073" + 
":  " + 
"0.00010106253608522283" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 934.5) ? " + 
"(b('bulk') <= 145.5) ? " + 
"(b('bare') <= 12.442737102508545) ? " + 
"0.00015535652158932202" + 
":  " + 
"0.0036082365840869116" + 
":  " + 
"(b('L8b3med') <= 925.5) ? " + 
"-0.0007296610763233818" + 
":  " + 
"-0.004169481670285385" + 
":  " + 
"(b('L8b6med') <= 2934.5) ? " + 
"(b('L8b6med') <= 2749.0) ? " + 
"0.0002839790655910087" + 
":  " + 
"-0.0013202820768511946" + 
":  " + 
"(b('L8b6med') <= 3055.0) ? " + 
"0.00093741046482665" + 
":  " + 
"-6.448224797339403e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.0023724050261080265) ? " + 
"(b('gvhk3') <= 0.0018904488533735275) ? " + 
"(b('L8b10med') <= 1112.5) ? " + 
"0.002709159686922896" + 
":  " + 
"-6.650043422635332e-05" + 
":  " + 
"(b('L8b3med') <= 1115.5) ? " + 
"-0.0031854654344119007" + 
":  " + 
"-0.0003149565819685803" + 
":  " + 
"(b('gvhk3') <= 0.002843111054971814) ? " + 
"(b('L8b5med') <= 2120.5) ? " + 
"0.0004270162731156435" + 
":  " + 
"0.0033543871299071756" + 
":  " + 
"(b('lat') <= 44.878801345825195) ? " + 
"-0.0001347221744565789" + 
":  " + 
"0.0004568986113266535" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 56.031551361083984) ? " + 
"(b('ndvi_med') <= 4792.25) ? " + 
"(b('ndvi_med') <= 4434.0) ? " + 
"2.32230386005058e-05" + 
":  " + 
"-0.0021483317137643947" + 
":  " + 
"(b('ndvi_med') <= 5284.0) ? " + 
"0.002182182283947162" + 
":  " + 
"-0.00010991675997528798" + 
":  " + 
"(b('gvhk3') <= -0.10665059834718704) ? " + 
"(b('sand') <= 75.0) ? " + 
"0.0006625402453125095" + 
":  " + 
"0.001969117617719729" + 
":  " + 
"(b('gvhk3') <= 0.04623102769255638) ? " + 
"-0.0016130485763284977" + 
":  " + 
"-0.00037643586179869626" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 557.5) ? " + 
"0.0010212765008764946" + 
":  " + 
"(b('L8b10med') <= 1516.75) ? " + 
"(b('L8b10med') <= 1476.0) ? " + 
"-2.9988160879878506e-05" + 
":  " + 
"-0.0026043147065026953" + 
":  " + 
"(b('L8b10med') <= 1548.5) ? " + 
"0.0012450204868748374" + 
":  " + 
"-8.096476098964604e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b10med') <= 2822.25) ? " + 
"(b('L8b10med') <= 2738.5) ? " + 
"(b('L8b3med') <= 1755.5) ? " + 
"1.7329177833801185e-05" + 
":  " + 
"-0.0018097393039836034" + 
":  " + 
"(b('bulk') <= 147.0) ? " + 
"-0.0005573848316819374" + 
":  " + 
"-0.0025063002859174364" + 
":  " + 
"(b('L8b5med') <= 2844.0) ? " + 
"(b('L8b5med') <= 2784.25) ? " + 
"0.0003080835495161312" + 
":  " + 
"0.0019070820381246688" + 
":  " + 
"(b('bare') <= 5.7313196659088135) ? " + 
"-0.0016035730245165815" + 
":  " + 
"0.00016330414908644801" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk2') <= 0.3164534270763397) ? " + 
"(b('sand') <= 44.5) ? " + 
"(b('L8b3med') <= 1301.25) ? " + 
"-0.00048087916525937094" + 
":  " + 
"0.0016398882969546418" + 
":  " + 
"(b('L8b10med') <= 2180.0) ? " + 
"0.0005503325493140224" + 
":  " + 
"-0.00028673635496928227" + 
":  " + 
"(b('lon') <= -121.02084732055664) ? " + 
"(b('L8b5med') <= 2527.0) ? " + 
"-0.003121823962248818" + 
":  " + 
"-0.000494526957377589" + 
":  " + 
"(b('sand') <= 42.5) ? " + 
"0.00041515890379776287" + 
":  " + 
"-7.787467393620112e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvhk3') <= 0.044578563421964645) ? " + 
"(b('grass') <= 76.27609634399414) ? " + 
"(b('gvhk2') <= 0.3871832937002182) ? " + 
"-0.00015052250832145298" + 
":  " + 
"0.0003192915151175969" + 
":  " + 
"(b('bare') <= 3.5051686763763428) ? " + 
"-0.00017036030981513832" + 
":  " + 
"0.0009664569645203739" + 
":  " + 
"(b('gvvmean') <= -15.352062225341797) ? " + 
"(b('gvhmean') <= -15.422348499298096) ? " + 
"3.138553125915308e-05" + 
":  " + 
"0.004309925627938388" + 
":  " + 
"(b('gvhk3') <= 0.08871250972151756) ? " + 
"-0.0012192015065170926" + 
":  " + 
"0.00017679295454743813" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 4160.75) ? " + 
"(b('L8b5med') <= 2918.0) ? " + 
"(b('L8b5med') <= 2907.0) ? " + 
"1.5992189487202122e-05" + 
":  " + 
"0.0028534402338554615" + 
":  " + 
"(b('gvhk3') <= -0.0002864523994503543) ? " + 
"0.00038238944631123484" + 
":  " + 
"-0.0005841130452276625" + 
":  " + 
"(b('L8b6med') <= 4419.0) ? " + 
"(b('grass') <= 12.479963421821594) ? " + 
"0.0015138024147574036" + 
":  " + 
"0.00063098262278731" + 
":  " + 
"(b('gvhk3') <= -0.0008417265198659152) ? " + 
"-0.0006692338955677224" + 
":  " + 
"0.00011454747685221006" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  return prediction