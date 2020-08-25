import ee 

def tree(feature_stack): 

  prediction = ee.Image(0.15742028)
  learning_rate = ee.Image(0.1)
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1229.5) ? " + 
"(b('b2') <= 391.5) ? " + 
"(b('grass') <= 39.87313461303711) ? " + 
"0.0441453875477395" + 
":  " + 
"0.1525036233137323" + 
":  " + 
"(b('moss') <= 7.396992444992065) ? " + 
"0.03969825578683103" + 
":  " + 
"-0.005471327437269029" + 
":  " + 
"(b('bare') <= 5.53663182258606) ? " + 
"(b('g0vv') <= -10.19192123413086) ? " + 
"-0.038754080697547995" + 
":  " + 
"0.016019439187328347" + 
":  " + 
"(b('grass') <= 15.92530632019043) ? " + 
"-0.10783447332268954" + 
":  " + 
"-0.05341145205866287" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b10') <= 1721.5) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('b2') <= 391.5) ? " + 
"0.09747884455112138" + 
":  " + 
"0.043729190951816356" + 
":  " + 
"(b('moss') <= 7.395158052444458) ? " + 
"0.07552331151610726" + 
":  " + 
"-0.033379974587200927" + 
":  " + 
"(b('b4') <= 1654.0) ? " + 
"(b('g0vv') <= -11.554278373718262) ? " + 
"-0.024551394963219963" + 
":  " + 
"0.014219082594690433" + 
":  " + 
"(b('bare') <= 2.631805181503296) ? " + 
"-0.032811167451990024" + 
":  " + 
"-0.08196138723124526" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1229.5) ? " + 
"(b('b2') <= 396.5) ? " + 
"(b('grass') <= 34.980010986328125) ? " + 
"0.02977581293023241" + 
":  " + 
"0.12255650278226916" + 
":  " + 
"(b('moss') <= 6.692746162414551) ? " + 
"0.0339305314363175" + 
":  " + 
"-0.00451460966986854" + 
":  " + 
"(b('bare') <= 5.53663182258606) ? " + 
"(b('g0vv') <= -8.963788509368896) ? " + 
"-0.027251625875041686" + 
":  " + 
"0.04044856618865115" + 
":  " + 
"(b('bare') <= 5.8496716022491455) ? " + 
"-0.10520571817396392" + 
":  " + 
"-0.05043049252207997" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 1727.5) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('crop') <= 5.957038402557373) ? " + 
"-0.0009846193623839789" + 
":  " + 
"0.06386502840072926" + 
":  " + 
"(b('moss') <= 7.395158052444458) ? " + 
"0.06291833851887542" + 
":  " + 
"-0.03015023011299445" + 
":  " + 
"(b('b4') <= 1382.5) ? " + 
"(b('crop') <= 66.14077377319336) ? " + 
"-0.011179123209124862" + 
":  " + 
"0.03187462685578079" + 
":  " + 
"(b('bare') <= 5.53663182258606) ? " + 
"-0.02201467935398332" + 
":  " + 
"-0.06423858529758468" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 1721.5) ? " + 
"(b('b3') <= 624.5) ? " + 
"(b('b5') <= 2477.0) ? " + 
"0.023423683625227194" + 
":  " + 
"0.15167245351641687" + 
":  " + 
"(b('moss') <= 7.395158052444458) ? " + 
"0.04103369092837244" + 
":  " + 
"0.007170399064124711" + 
":  " + 
"(b('b11') <= 2929.0) ? " + 
"(b('l8dt') <= 688202.0) ? " + 
"-0.024023616538926408" + 
":  " + 
"0.011969429215395375" + 
":  " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"-0.01750732307348921" + 
":  " + 
"-0.059544809643965114" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2336.5) ? " + 
"(b('b6') <= 2754.5) ? " + 
"(b('crop') <= 71.37601852416992) ? " + 
"-0.015852512124034376" + 
":  " + 
"0.05920397788284142" + 
":  " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"0.0003500019938053841" + 
":  " + 
"-0.03901725533197121" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"(b('l8dt') <= 1402819.5) ? " + 
"-0.001681852709158502" + 
":  " + 
"0.034991886110831136" + 
":  " + 
"(b('crop') <= 5.957038402557373) ? " + 
"0.011904816869388475" + 
":  " + 
"0.08648792877748994" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1349.5) ? " + 
"(b('b2') <= 391.5) ? " + 
"(b('grass') <= 39.87313461303711) ? " + 
"0.01900346609355503" + 
":  " + 
"0.09643315411734125" + 
":  " + 
"(b('urban') <= 23.278701782226562) ? " + 
"0.01355789548743328" + 
":  " + 
"-0.04536188277819642" + 
":  " + 
"(b('moss') <= 9.386762142181396) ? " + 
"(b('moss') <= 3.2683908939361572) ? " + 
"-0.03200033703865739" + 
":  " + 
"0.009071586480421043" + 
":  " + 
"(b('crop') <= 81.55975341796875) ? " + 
"-0.05975264411912787" + 
":  " + 
"-4.064362871814754e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2336.5) ? " + 
"(b('g0vv') <= -11.31413221359253) ? " + 
"(b('grass') <= 87.20395278930664) ? " + 
"-0.03619288644669585" + 
":  " + 
"0.0011893156603064244" + 
":  " + 
"(b('moss') <= 1.8418367505073547) ? " + 
"0.04051396161660954" + 
":  " + 
"-0.014396303398573312" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.016050047976282622" + 
":  " + 
"-0.016841653807435093" + 
":  " + 
"(b('crop') <= 5.957038402557373) ? " + 
"0.008613346845210318" + 
":  " + 
"0.07344780488016887" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1354.5) ? " + 
"(b('b3') <= 624.5) ? " + 
"(b('b6') <= 2482.5) ? " + 
"0.029298698497849492" + 
":  " + 
"0.14803350817877634" + 
":  " + 
"(b('g0vv') <= -11.071014404296875) ? " + 
"-0.0019472080004718255" + 
":  " + 
"0.026856061041826525" + 
":  " + 
"(b('moss') <= 9.386762142181396) ? " + 
"(b('lia') <= 43.98294639587402) ? " + 
"-0.01645013895943446" + 
":  " + 
"0.0829208874787568" + 
":  " + 
"(b('crop') <= 81.55975341796875) ? " + 
"-0.05131033687324598" + 
":  " + 
"0.001635529470178073" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 1721.5) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.04497402929654185" + 
":  " + 
"-0.001771664376634568" + 
":  " + 
"(b('moss') <= 7.395158052444458) ? " + 
"0.045207072928515654" + 
":  " + 
"-0.029204481877738973" + 
":  " + 
"(b('l8dt') <= 687708.0) ? " + 
"(b('b6') <= 3729.5) ? " + 
"-0.016466052051068894" + 
":  " + 
"-0.04040961152013068" + 
":  " + 
"(b('moss') <= 1.8418367505073547) ? " + 
"0.030447405927726753" + 
":  " + 
"-0.00764897464055244" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2336.5) ? " + 
"(b('crop') <= 99.63687133789062) ? " + 
"(b('g0vv') <= -11.552824020385742) ? " + 
"-0.02732014463926431" + 
":  " + 
"-0.0035575725950388274" + 
":  " + 
"(b('lia') <= 43.18170356750488) ? " + 
"0.13633122576449305" + 
":  " + 
"-0.0032303165360145682" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"(b('l8dt') <= 1402819.5) ? " + 
"-0.003986848607931484" + 
":  " + 
"0.02684123037439974" + 
":  " + 
"(b('trees') <= 20.289265632629395) ? " + 
"0.046111546107251475" + 
":  " + 
"-0.070978224991126" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 1679.5) ? " + 
"(b('urban') <= 0.9054647088050842) ? " + 
"(b('g0vv') <= -13.579917430877686) ? " + 
"-0.009018448194295751" + 
":  " + 
"0.036543727687090785" + 
":  " + 
"(b('moss') <= 1.4917218685150146) ? " + 
"0.044552779129178995" + 
":  " + 
"-0.014154758742320092" + 
":  " + 
"(b('bare') <= 2.6025168895721436) ? " + 
"(b('bare') <= 2.078667640686035) ? " + 
"-0.005617470931970133" + 
":  " + 
"0.06432589011071103" + 
":  " + 
"(b('trees') <= 1.1431602239608765) ? " + 
"-0.006328730238602769" + 
":  " + 
"-0.04186634390855265" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b10') <= 2386.5) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.030458995841636638" + 
":  " + 
"-0.00951612027510051" + 
":  " + 
"(b('moss') <= 6.056493043899536) ? " + 
"0.025636291520766415" + 
":  " + 
"-0.027720082231343722" + 
":  " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b3') <= 1558.5) ? " + 
"0.026940014036088523" + 
":  " + 
"-0.013000176852902398" + 
":  " + 
"(b('grass') <= 16.769301414489746) ? " + 
"-0.04815388273252428" + 
":  " + 
"-0.008936097921228394" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2312.5) ? " + 
"(b('crop') <= 99.63687133789062) ? " + 
"(b('l8dt') <= 684088.5) ? " + 
"-0.022022415104247413" + 
":  " + 
"-0.00036916799926042625" + 
":  " + 
"(b('ndvi') <= 1815.0) ? " + 
"0.13507751706855908" + 
":  " + 
"0.029320146975914535" + 
":  " + 
"(b('grass') <= 39.87313461303711) ? " + 
"(b('l8dt') <= 1444340.5) ? " + 
"-0.003917930784417948" + 
":  " + 
"0.02321651258506106" + 
":  " + 
"(b('grass') <= 62.16565132141113) ? " + 
"0.06928796358214885" + 
":  " + 
"0.01016511144205417" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1354.5) ? " + 
"(b('urban') <= 23.278701782226562) ? " + 
"(b('g0vv') <= -12.692841529846191) ? " + 
"-0.0054265684733115814" + 
":  " + 
"0.022588053721460676" + 
":  " + 
"(b('moss') <= 1.6670465469360352) ? " + 
"0.05434470395501714" + 
":  " + 
"-0.048314619836894133" + 
":  " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b3') <= 1558.5) ? " + 
"0.02807001361233759" + 
":  " + 
"-0.012335918502431577" + 
":  " + 
"(b('grass') <= 16.769301414489746) ? " + 
"-0.04144617850392643" + 
":  " + 
"-0.006617285108961179" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 704.5) ? " + 
"(b('b6') <= 2647.0) ? " + 
"(b('urban') <= 20.123075485229492) ? " + 
"0.021912470594677186" + 
":  " + 
"-0.039111178207788325" + 
":  " + 
"(b('crop') <= 23.567298889160156) ? " + 
"-0.018914054740540347" + 
":  " + 
"0.1262530597376071" + 
":  " + 
"(b('g0vv') <= -11.108834266662598) ? " + 
"(b('lia') <= 44.315603256225586) ? " + 
"-0.015042775720854707" + 
":  " + 
"0.05441139432101685" + 
":  " + 
"(b('moss') <= 1.8418367505073547) ? " + 
"0.03255216990467356" + 
":  " + 
"-0.002058774149921805" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 688206.0) ? " + 
"(b('ndvi') <= 3467.0) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"-0.0059525431200813436" + 
":  " + 
"-0.02544286021659095" + 
":  " + 
"(b('grass') <= 46.00799369812012) ? " + 
"0.0020584886551873118" + 
":  " + 
"0.040774620584139214" + 
":  " + 
"(b('grass') <= 16.995849609375) ? " + 
"(b('moss') <= 1.5077694058418274) ? " + 
"0.027712662376156355" + 
":  " + 
"-0.021203365867182584" + 
":  " + 
"(b('crop') <= 66.59177017211914) ? " + 
"0.020363533156436252" + 
":  " + 
"0.08985823726491995" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 2544.5) ? " + 
"(b('g0vv') <= -12.690886974334717) ? " + 
"(b('b5') <= 4653.0) ? " + 
"-0.009632619959114071" + 
":  " + 
"0.15876432129377188" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.02343101109326696" + 
":  " + 
"-0.00686330472804543" + 
":  " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b4') <= 2049.5) ? " + 
"0.02555717071633885" + 
":  " + 
"-0.011585566053848017" + 
":  " + 
"(b('crop') <= 77.83634567260742) ? " + 
"-0.010106725197283227" + 
":  " + 
"-0.0462287427937136" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 687710.0) ? " + 
"(b('moss') <= 13.232231140136719) ? " + 
"(b('grass') <= 17.183883666992188) ? " + 
"-0.01633783993545354" + 
":  " + 
"0.004766898864540294" + 
":  " + 
"(b('lia') <= 33.942344665527344) ? " + 
"0.02161544191135099" + 
":  " + 
"-0.03251120716743065" + 
":  " + 
"(b('b2') <= 397.5) ? " + 
"(b('b6') <= 2647.0) ? " + 
"0.025919163554258544" + 
":  " + 
"0.12889183143486418" + 
":  " + 
"(b('lia') <= 44.30132484436035) ? " + 
"0.004633791642099325" + 
":  " + 
"0.0805598805087071" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 2.297703742980957) ? " + 
"(b('bare') <= 2.078667640686035) ? " + 
"(b('g0vh') <= -18.256166458129883) ? " + 
"-0.008119226748173383" + 
":  " + 
"0.019542688640701456" + 
":  " + 
"(b('moss') <= 7.394193649291992) ? " + 
"0.06873051367670398" + 
":  " + 
"0.012151259999236018" + 
":  " + 
"(b('moss') <= 7.337804079055786) ? " + 
"(b('trees') <= 10.541350841522217) ? " + 
"0.032265669061084384" + 
":  " + 
"-0.025928132529411698" + 
":  " + 
"(b('grass') <= 16.769301414489746) ? " + 
"-0.045917703302918965" + 
":  " + 
"-0.012118550837702495" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 704.5) ? " + 
"(b('b6') <= 2647.0) ? " + 
"(b('moss') <= 8.992009162902832) ? " + 
"0.0009377597719904492" + 
":  " + 
"0.03414695876039562" + 
":  " + 
"(b('crop') <= 11.22841739654541) ? " + 
"-0.029633986632799605" + 
":  " + 
"0.10142629360451431" + 
":  " + 
"(b('g0vv') <= -10.9192476272583) ? " + 
"(b('lia') <= 44.29729461669922) ? " + 
"-0.011602621580404905" + 
":  " + 
"0.044291925739793535" + 
":  " + 
"(b('b4') <= 2029.5) ? " + 
"0.012053123750852796" + 
":  " + 
"-0.022617488546223287" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 1985408.5) ? " + 
"(b('b4') <= 1644.5) ? " + 
"(b('urban') <= 23.278701782226562) ? " + 
"0.003945031183139741" + 
":  " + 
"-0.034617498976702035" + 
":  " + 
"(b('trees') <= 11.00907564163208) ? " + 
"-0.018885563171839207" + 
":  " + 
"0.03153939129849024" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"(b('moss') <= 1.5077694058418274) ? " + 
"0.036503492098545184" + 
":  " + 
"0.001464773427631972" + 
":  " + 
"(b('crop') <= 23.28632164001465) ? " + 
"0.012446914163691317" + 
":  " + 
"0.0763799826554225" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"0.02040329374144929" + 
":  " + 
"-0.0206504217711727" + 
":  " + 
"(b('crop') <= 66.59177017211914) ? " + 
"0.007055739605097437" + 
":  " + 
"0.06306456520006819" + 
":  " + 
"(b('lia') <= 33.942344665527344) ? " + 
"(b('bare') <= 0.0648648664355278) ? " + 
"0.057554608781919356" + 
":  " + 
"-0.009046540784399664" + 
":  " + 
"(b('moss') <= 22.977157592773438) ? " + 
"-0.027815267742008827" + 
":  " + 
"0.007184810054692002" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 687710.0) ? " + 
"(b('g0vv') <= -11.068736553192139) ? " + 
"(b('grass') <= 87.20395278930664) ? " + 
"-0.014838582002347027" + 
":  " + 
"0.009646885631217166" + 
":  " + 
"(b('moss') <= 7.358212232589722) ? " + 
"0.015728888926274765" + 
":  " + 
"-0.009668149913213126" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"(b('moss') <= 1.887434184551239) ? " + 
"0.019153622533132155" + 
":  " + 
"-0.005874393200758087" + 
":  " + 
"(b('grass') <= 62.991891860961914) ? " + 
"0.05025718843812075" + 
":  " + 
"0.004916031373084178" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 697.5) ? " + 
"(b('b6') <= 2647.0) ? " + 
"(b('b3') <= 694.5) ? " + 
"0.006823324656843249" + 
":  " + 
"0.0916564627529555" + 
":  " + 
"(b('grass') <= 40.616336822509766) ? " + 
"-0.04000641564313544" + 
":  " + 
"0.09390625134012581" + 
":  " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('g0vv') <= -7.705477952957153) ? " + 
"0.008936761160666282" + 
":  " + 
"0.06009580946906653" + 
":  " + 
"(b('grass') <= 3.1685575246810913) ? " + 
"-0.06299626058722634" + 
":  " + 
"-0.0036457463964921755" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 2028.5) ? " + 
"(b('g0vv') <= -12.63295030593872) ? " + 
"(b('b5') <= 4653.0) ? " + 
"-0.008755156123718133" + 
":  " + 
"0.14167922928324686" + 
":  " + 
"(b('urban') <= 0.9054647088050842) ? " + 
"0.013654061089861133" + 
":  " + 
"-0.01030916306624398" + 
":  " + 
"(b('ndvi') <= 3473.5) ? " + 
"(b('lia') <= 44.30093193054199) ? " + 
"-0.024059481987784567" + 
":  " + 
"0.02734938978003649" + 
":  " + 
"(b('b4') <= 2168.0) ? " + 
"0.006203657197580096" + 
":  " + 
"0.09952319980812627" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 1288415.5) ? " + 
"(b('b4') <= 1354.5) ? " + 
"(b('urban') <= 23.278701782226562) ? " + 
"0.003960034362075477" + 
":  " + 
"-0.033163762813685764" + 
":  " + 
"(b('trees') <= 19.831669807434082) ? " + 
"-0.013055334095767887" + 
":  " + 
"0.05373569743875114" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"(b('moss') <= 1.5077694058418274) ? " + 
"0.024127894504595574" + 
":  " + 
"-0.0028121603227575023" + 
":  " + 
"(b('b5') <= 2469.0) ? " + 
"-0.002012393911499317" + 
":  " + 
"0.04517675892026607" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"0.016608980474806412" + 
":  " + 
"-0.017568015019053824" + 
":  " + 
"(b('crop') <= 66.59177017211914) ? " + 
"0.005821572079994206" + 
":  " + 
"0.056474208465922035" + 
":  " + 
"(b('lia') <= 33.942344665527344) ? " + 
"(b('trees') <= 16.24367094039917) ? " + 
"0.007645482760379514" + 
":  " + 
"0.1193902728217323" + 
":  " + 
"(b('moss') <= 22.977157592773438) ? " + 
"-0.023605334971307918" + 
":  " + 
"0.00790785037776916" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 600693.0) ? " + 
"(b('ndvi') <= 3467.0) ? " + 
"(b('g0vv') <= -8.873780727386475) ? " + 
"-0.010892347269789986" + 
":  " + 
"0.011983180426436838" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"0.004481745380512719" + 
":  " + 
"0.12653804455557954" + 
":  " + 
"(b('grass') <= 16.995849609375) ? " + 
"(b('moss') <= 1.5077694058418274) ? " + 
"0.01730212084336305" + 
":  " + 
"-0.015515563206849098" + 
":  " + 
"(b('crop') <= 66.59177017211914) ? " + 
"0.010666973260001766" + 
":  " + 
"0.06243780954661738" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 644.5) ? " + 
"(b('b6') <= 2647.0) ? " + 
"(b('b5') <= 2784.5) ? " + 
"-0.0036528017708510013" + 
":  " + 
"0.06386717733348947" + 
":  " + 
"(b('b5') <= 2449.5) ? " + 
"-0.03104335158900511" + 
":  " + 
"0.10907524561997631" + 
":  " + 
"(b('g0vv') <= -10.227709770202637) ? " + 
"(b('lia') <= 44.29729461669922) ? " + 
"-0.007096262879122598" + 
":  " + 
"0.03476969190848955" + 
":  " + 
"(b('bare') <= 4.18165922164917) ? " + 
"0.017288767576930885" + 
":  " + 
"-0.012165951077566664" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 2094039.0) ? " + 
"(b('ndvi') <= 2103.5) ? " + 
"(b('crop') <= 99.63687133789062) ? " + 
"-0.009294286794104814" + 
":  " + 
"0.07803608787886601" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"0.0018184114060660055" + 
":  " + 
"0.06593038884073327" + 
":  " + 
"(b('crop') <= 89.04487609863281) ? " + 
"(b('crop') <= 85.84851455688477) ? " + 
"0.016328474551034807" + 
":  " + 
"0.06933803485052428" + 
":  " + 
"(b('grass') <= 2.2221348881721497) ? " + 
"0.03267453647882715" + 
":  " + 
"-0.04469113936808798" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"-0.009530502953153112" + 
":  " + 
"0.05450804412009975" + 
":  " + 
"(b('crop') <= 66.59177017211914) ? " + 
"0.005034568750889001" + 
":  " + 
"0.04769418377743477" + 
":  " + 
"(b('lia') <= 34.07976722717285) ? " + 
"(b('trees') <= 16.24367094039917) ? " + 
"0.006630697270540274" + 
":  " + 
"0.1082367644234589" + 
":  " + 
"(b('bare') <= 10.456055164337158) ? " + 
"-0.022128072697787268" + 
":  " + 
"0.002797829547217646" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -13.039248943328857) ? " + 
"(b('crop') <= 28.176219940185547) ? " + 
"(b('crop') <= 24.69420051574707) ? " + 
"-0.003169351795693897" + 
":  " + 
"0.06699614847564994" + 
":  " + 
"(b('crop') <= 37.13176345825195) ? " + 
"-0.071511882109979" + 
":  " + 
"-0.013959550836925634" + 
":  " + 
"(b('grass') <= 34.49201011657715) ? " + 
"(b('moss') <= 1.887434184551239) ? " + 
"0.015901722794265504" + 
":  " + 
"-0.007234636127790141" + 
":  " + 
"(b('trees') <= 20.289265632629395) ? " + 
"0.02177848201443471" + 
":  " + 
"-0.062332228465241835" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 2032.5) ? " + 
"(b('g0vv') <= -11.03410291671753) ? " + 
"(b('b3') <= 644.5) ? " + 
"0.021877357868768744" + 
":  " + 
"-0.005138117305011996" + 
":  " + 
"(b('urban') <= 1.9490950107574463) ? " + 
"0.015743889599308846" + 
":  " + 
"-0.008554029545767887" + 
":  " + 
"(b('ndvi') <= 3473.5) ? " + 
"(b('lia') <= 44.30093193054199) ? " + 
"-0.01854507198504444" + 
":  " + 
"0.015734773330822304" + 
":  " + 
"(b('b4') <= 2168.0) ? " + 
"0.006206238602641908" + 
":  " + 
"0.08478327045785522" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 600693.0) ? " + 
"(b('l8dt') <= 792.5) ? " + 
"(b('g0vh') <= -19.18735694885254) ? " + 
"-0.008406859528631516" + 
":  " + 
"0.16926300804540084" + 
":  " + 
"(b('g0vv') <= -10.743607521057129) ? " + 
"-0.008274236565091452" + 
":  " + 
"0.0021477255460304536" + 
":  " + 
"(b('crop') <= 89.04487609863281) ? " + 
"(b('crop') <= 85.84851455688477) ? " + 
"0.005423752388440276" + 
":  " + 
"0.04808538420565143" + 
":  " + 
"(b('crop') <= 94.68265533447266) ? " + 
"-0.050298818495148355" + 
":  " + 
"0.012966261558362922" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 2.297703742980957) ? " + 
"(b('bare') <= 1.5240135788917542) ? " + 
"(b('trees') <= 9.328140258789062) ? " + 
"-0.006445094125378313" + 
":  " + 
"0.015614594919542193" + 
":  " + 
"(b('moss') <= 5.656521797180176) ? " + 
"0.052402662163596514" + 
":  " + 
"0.010988588658870748" + 
":  " + 
"(b('trees') <= 1.1431602239608765) ? " + 
"(b('crop') <= 58.756975173950195) ? " + 
"-0.002518599393245855" + 
":  " + 
"0.055324672727023155" + 
":  " + 
"(b('grass') <= 21.1492338180542) ? " + 
"-0.034538441566567296" + 
":  " + 
"-0.0009290867286282663" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 545.5) ? " + 
"(b('b5') <= 2688.5) ? " + 
"(b('trees') <= 22.02607250213623) ? " + 
"0.003787965656774037" + 
":  " + 
"-0.09023441742247036" + 
":  " + 
"(b('b7') <= 1088.5) ? " + 
"0.06253249840667004" + 
":  " + 
"0.1522137832415505" + 
":  " + 
"(b('b1') <= 130.0) ? " + 
"(b('trees') <= 31.51175022125244) ? " + 
"-0.150060388790786" + 
":  " + 
"0.15533436396484157" + 
":  " + 
"(b('g0vv') <= -8.988980770111084) ? " + 
"-0.00255548242627589" + 
":  " + 
"0.01251324166684407" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"-0.005167578747407932" + 
":  " + 
"0.006840541080876131" + 
":  " + 
"(b('ndvi') <= 3570.5) ? " + 
"0.0434355919672894" + 
":  " + 
"0.13229195718277112" + 
":  " + 
"(b('g0vh') <= -20.389952659606934) ? " + 
"(b('moss') <= 17.294462203979492) ? " + 
"-0.013524803221332173" + 
":  " + 
"0.02061655883008609" + 
":  " + 
"(b('grass') <= 65.19527816772461) ? " + 
"-0.009314217785977838" + 
":  " + 
"-0.039509588520512104" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 2094039.0) ? " + 
"(b('g0vh') <= -15.809495449066162) ? " + 
"(b('grass') <= 16.658127784729004) ? " + 
"-0.010395845430615487" + 
":  " + 
"0.0007138269563713354" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.02820315010317631" + 
":  " + 
"-0.011339658292775102" + 
":  " + 
"(b('lia') <= 43.75978088378906) ? " + 
"(b('grass') <= 34.980010986328125) ? " + 
"0.006102028283832005" + 
":  " + 
"0.026000707712559974" + 
":  " + 
"(b('ndvi') <= 5778.5) ? " + 
"0.05574432045999963" + 
":  " + 
"0.19274014101041856" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.690886974334717) ? " + 
"(b('crop') <= 28.176219940185547) ? " + 
"(b('crop') <= 24.69420051574707) ? " + 
"-0.001737708623003035" + 
":  " + 
"0.06393090864803903" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"-0.01040398435901509" + 
":  " + 
"-0.08542460777719364" + 
":  " + 
"(b('grass') <= 34.49201011657715) ? " + 
"(b('moss') <= 1.887434184551239) ? " + 
"0.012812209321323246" + 
":  " + 
"-0.005460287427717834" + 
":  " + 
"(b('trees') <= 20.289265632629395) ? " + 
"0.020081920508366196" + 
":  " + 
"-0.05713098116255365" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('bare') <= 0.2583579495549202) ? " + 
"(b('ndvi') <= 972.0) ? " + 
"0.2306190142301457" + 
":  " + 
"0.028309769408248957" + 
":  " + 
"(b('g0vv') <= -7.72388219833374) ? " + 
"-0.0024279357347105524" + 
":  " + 
"0.032045099334794734" + 
":  " + 
"(b('crop') <= 89.00007629394531) ? " + 
"(b('crop') <= 85.84851455688477) ? " + 
"-0.0012039789759266627" + 
":  " + 
"0.048116282328889995" + 
":  " + 
"(b('lia') <= 42.7987003326416) ? " + 
"-0.04054353122142486" + 
":  " + 
"0.15099615457199822" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 2032.5) ? " + 
"(b('b5') <= 4653.0) ? " + 
"(b('g0vv') <= -13.106256484985352) ? " + 
"-0.00715341197484275" + 
":  " + 
"0.004460233855659976" + 
":  " + 
"(b('b4') <= 1028.5) ? " + 
"0.12147998318994413" + 
":  " + 
"-0.01727513558058506" + 
":  " + 
"(b('ndvi') <= 3473.5) ? " + 
"(b('bare') <= 75.35467147827148) ? " + 
"-0.014472695255960597" + 
":  " + 
"0.03215041362894866" + 
":  " + 
"(b('urban') <= 0.42328041791915894) ? " + 
"0.040547837795175304" + 
":  " + 
"0.18452643843004757" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 2.297703742980957) ? " + 
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 5.855041980743408) ? " + 
"-0.009502818749640584" + 
":  " + 
"0.011115333796305086" + 
":  " + 
"(b('grass') <= 2.972543239593506) ? " + 
"-0.0010550441372759668" + 
":  " + 
"0.030764618037995947" + 
":  " + 
"(b('trees') <= 1.1431602239608765) ? " + 
"(b('crop') <= 58.756975173950195) ? " + 
"-0.0019317682234322193" + 
":  " + 
"0.05004490686758408" + 
":  " + 
"(b('grass') <= 21.1492338180542) ? " + 
"-0.029516620729350566" + 
":  " + 
"-0.0014661763234983805" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('lia') <= 34.08248710632324) ? " + 
"-0.006848591467941301" + 
":  " + 
"0.005234147105799957" + 
":  " + 
"(b('ndvi') <= 3425.0) ? " + 
"0.031756028260630426" + 
":  " + 
"0.1114287578916482" + 
":  " + 
"(b('bare') <= 10.456055164337158) ? " + 
"(b('moss') <= 22.977157592773438) ? " + 
"-0.017954225582637606" + 
":  " + 
"0.022368742230294277" + 
":  " + 
"(b('g0vh') <= -18.011208534240723) ? " + 
"0.014583705839244447" + 
":  " + 
"-0.04168408074295632" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 624.5) ? " + 
"(b('b5') <= 2816.0) ? " + 
"(b('b6') <= 2650.5) ? " + 
"-0.009541197855452172" + 
":  " + 
"0.06676865066742138" + 
":  " + 
"(b('crop') <= 41.87337875366211) ? " + 
"0.09867250411013771" + 
":  " + 
"-0.09535328066075023" + 
":  " + 
"(b('g0vv') <= -8.906886577606201) ? " + 
"(b('grass') <= 86.51207733154297) ? " + 
"-0.004309111783392762" + 
":  " + 
"0.013948262152023603" + 
":  " + 
"(b('crop') <= 80.08920669555664) ? " + 
"0.0009177619875246957" + 
":  " + 
"0.0338025584752786" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 600693.0) ? " + 
"(b('l8dt') <= 792.5) ? " + 
"(b('g0vh') <= -19.18735694885254) ? " + 
"-0.006589233736091289" + 
":  " + 
"0.1497126213520981" + 
":  " + 
"(b('g0vh') <= -12.329197406768799) ? " + 
"-0.004279972093003944" + 
":  " + 
"0.08841254096261644" + 
":  " + 
"(b('l8dt') <= 606649.0) ? " + 
"(b('g0vv') <= -9.934991359710693) ? " + 
"0.03306374493126954" + 
":  " + 
"0.12679731741209993" + 
":  " + 
"(b('b3') <= 697.5) ? " + 
"0.017276741725769325" + 
":  " + 
"0.0009253858215637801" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 2244671.0) ? " + 
"(b('moss') <= 3.2275424003601074) ? " + 
"(b('moss') <= 1.940559446811676) ? " + 
"-0.0003816351141261674" + 
":  " + 
"-0.02743687688370294" + 
":  " + 
"(b('moss') <= 4.659861326217651) ? " + 
"0.0270118185994284" + 
":  " + 
"-0.0021711426473080024" + 
":  " + 
"(b('lia') <= 44.08297157287598) ? " + 
"(b('b6') <= 2340.0) ? " + 
"-0.007585250996243905" + 
":  " + 
"0.01437479187635338" + 
":  " + 
"(b('grass') <= 60.23370933532715) ? " + 
"0.08077476876328382" + 
":  " + 
"-0.09659041593648537" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('bare') <= 0.2583579495549202) ? " + 
"(b('ndvi') <= 972.0) ? " + 
"0.2060657441902367" + 
":  " + 
"0.024449479676996688" + 
":  " + 
"(b('b5') <= 2177.0) ? " + 
"0.02702642460554253" + 
":  " + 
"-0.0022301889419379635" + 
":  " + 
"(b('grass') <= 5.992608308792114) ? " + 
"(b('trees') <= 3.8236643075942993) ? " + 
"-0.030969061580685228" + 
":  " + 
"-0.00244997293420346" + 
":  " + 
"(b('grass') <= 11.09217882156372) ? " + 
"0.03071413665119553" + 
":  " + 
"-4.619026998163247e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 545.5) ? " + 
"(b('b5') <= 2688.5) ? " + 
"(b('moss') <= 5.641550540924072) ? " + 
"-0.02609204772556234" + 
":  " + 
"0.023497879143268008" + 
":  " + 
"(b('b7') <= 1046.5) ? " + 
"0.044149162614502906" + 
":  " + 
"0.12303307996474822" + 
":  " + 
"(b('b1') <= 130.0) ? " + 
"(b('b3') <= 508.0) ? " + 
"0.14274534920309062" + 
":  " + 
"-0.1287429620019233" + 
":  " + 
"(b('g0vv') <= -9.567552089691162) ? " + 
"-0.0022614891785624836" + 
":  " + 
"0.007672139760675907" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('lia') <= 34.08248710632324) ? " + 
"-0.006080605740159996" + 
":  " + 
"0.004482037127598427" + 
":  " + 
"(b('b5') <= 3069.0) ? " + 
"0.037188327417895406" + 
":  " + 
"0.1107225444424395" + 
":  " + 
"(b('g0vh') <= -20.389952659606934) ? " + 
"(b('moss') <= 17.294462203979492) ? " + 
"-0.010063266210301614" + 
":  " + 
"0.01933987927563925" + 
":  " + 
"(b('grass') <= 65.19527816772461) ? " + 
"-0.006716500555968733" + 
":  " + 
"-0.03514929561432598" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -13.560813903808594) ? " + 
"(b('grass') <= 77.9202880859375) ? " + 
"(b('b2') <= 586.5) ? " + 
"-0.029719414887261802" + 
":  " + 
"-0.005270993764533821" + 
":  " + 
"(b('lia') <= 31.96481227874756) ? " + 
"0.055659835131096354" + 
":  " + 
"9.894279657452686e-05" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"(b('trees') <= 16.893975734710693) ? " + 
"-0.003042029683857889" + 
":  " + 
"0.033012880407859546" + 
":  " + 
"(b('trees') <= 20.289265632629395) ? " + 
"0.014506732911175964" + 
":  " + 
"-0.05192627066321871" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('g0vv') <= -7.36534571647644) ? " + 
"(b('b5') <= 3946.5) ? " + 
"0.009022136740900945" + 
":  " + 
"-0.020117553687455426" + 
":  " + 
"(b('lia') <= 42.62941551208496) ? " + 
"0.04122807161948101" + 
":  " + 
"0.21963782543232163" + 
":  " + 
"(b('grass') <= 3.1685575246810913) ? " + 
"(b('b4') <= 956.0) ? " + 
"-0.10540356082802443" + 
":  " + 
"-0.03317281247235635" + 
":  " + 
"(b('grass') <= 4.1582722663879395) ? " + 
"0.0347209978553161" + 
":  " + 
"-0.0010747398660532366" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 23.278701782226562) ? " + 
"(b('lia') <= 44.10676383972168) ? " + 
"(b('g0vv') <= -12.01679515838623) ? " + 
"-0.004745064980728189" + 
":  " + 
"0.0039278176689097445" + 
":  " + 
"(b('moss') <= 1.1933275163173676) ? " + 
"-0.06810774597142687" + 
":  " + 
"0.03185626867248182" + 
":  " + 
"(b('bare') <= 0.4333333373069763) ? " + 
"(b('b2') <= 488.0) ? " + 
"-0.0709920406248738" + 
":  " + 
"-0.027007552763046075" + 
":  " + 
"(b('g0vh') <= -15.495753765106201) ? " + 
"-0.014103780374371046" + 
":  " + 
"0.022163617228142005" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 600693.0) ? " + 
"(b('l8dt') <= 1280.5) ? " + 
"(b('b1') <= 296.5) ? " + 
"-0.02414311963479432" + 
":  " + 
"0.1044150230770399" + 
":  " + 
"(b('g0vh') <= -12.329197406768799) ? " + 
"-0.0036957045547206047" + 
":  " + 
"0.07786939775847534" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"(b('grass') <= 23.881052017211914) ? " + 
"0.0030140294398434287" + 
":  " + 
"-0.017492452862128083" + 
":  " + 
"(b('trees') <= 20.289265632629395) ? " + 
"0.014867661053148528" + 
":  " + 
"-0.05260202867707102" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1135.5) ? " + 
"(b('bare') <= 9.947502613067627) ? " + 
"(b('b3') <= 882.5) ? " + 
"-0.0013641587310024457" + 
":  " + 
"0.016347669337195746" + 
":  " + 
"(b('crop') <= 52.3651237487793) ? " + 
"0.04569980169144634" + 
":  " + 
"0.17307807322929208" + 
":  " + 
"(b('b3') <= 1008.5) ? " + 
"(b('crop') <= 66.59177017211914) ? " + 
"-0.022956944276862356" + 
":  " + 
"0.0030140460233599774" + 
":  " + 
"(b('b5') <= 3680.0) ? " + 
"0.0013212944804108337" + 
":  " + 
"-0.016892898471136765" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 2.297703742980957) ? " + 
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 5.855041980743408) ? " + 
"-0.008290156851457113" + 
":  " + 
"0.00945241722102727" + 
":  " + 
"(b('grass') <= 2.972543239593506) ? " + 
"-0.0009638145614011441" + 
":  " + 
"0.02591404891432851" + 
":  " + 
"(b('trees') <= 1.1431602239608765) ? " + 
"(b('crop') <= 58.756975173950195) ? " + 
"-0.0014576312921584541" + 
":  " + 
"0.04273723516366674" + 
":  " + 
"(b('grass') <= 21.1492338180542) ? " + 
"-0.024875348085044345" + 
":  " + 
"-0.0007692366761332132" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('b3') <= 644.5) ? " + 
"0.0157580135959746" + 
":  " + 
"-0.00031507756363641096" + 
":  " + 
"(b('ndvi') <= 3570.5) ? " + 
"0.030595962858396046" + 
":  " + 
"0.09766844671227436" + 
":  " + 
"(b('b6') <= 2528.0) ? " + 
"(b('moss') <= 20.664283752441406) ? " + 
"-0.028995113536529078" + 
":  " + 
"0.019427455517282883" + 
":  " + 
"(b('b1') <= 267.0) ? " + 
"-0.12088108638253882" + 
":  " + 
"-0.001276009240082791" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('l8dt') <= 2244671.0) ? " + 
"(b('grass') <= 86.51207733154297) ? " + 
"-0.002370341999692746" + 
":  " + 
"0.010987902249649446" + 
":  " + 
"(b('b6') <= 2340.0) ? " + 
"-0.007175133440144708" + 
":  " + 
"0.013453394436883061" + 
":  " + 
"(b('b3') <= 1098.5) ? " + 
"(b('ndvi') <= 5908.5) ? " + 
"0.17030172620081072" + 
":  " + 
"0.06215393918609089" + 
":  " + 
"(b('trees') <= 16.78393316268921) ? " + 
"-0.04480241423491252" + 
":  " + 
"0.02824471623266392" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 545.5) ? " + 
"(b('b5') <= 2688.5) ? " + 
"(b('g0vv') <= -15.802769660949707) ? " + 
"-0.1330646894790382" + 
":  " + 
"-0.0016425750427950206" + 
":  " + 
"(b('grass') <= 60.09731101989746) ? " + 
"0.11062670931079545" + 
":  " + 
"0.0411507167955783" + 
":  " + 
"(b('b1') <= 130.0) ? " + 
"(b('trees') <= 31.51175022125244) ? " + 
"-0.11208506053092271" + 
":  " + 
"0.12409676290331177" + 
":  " + 
"(b('trees') <= 17.868996620178223) ? " + 
"-0.00131174428430071" + 
":  " + 
"0.011840358829255403" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.28085994720459) ? " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('b4') <= 592.5) ? " + 
"0.024424001085706953" + 
":  " + 
"-0.0016667478946020451" + 
":  " + 
"(b('trees') <= 19.04677391052246) ? " + 
"0.08550328861620057" + 
":  " + 
"0.002108630951573295" + 
":  " + 
"(b('grass') <= 33.25920295715332) ? " + 
"(b('ndvi') <= 3955.5) ? " + 
"0.06588115149204676" + 
":  " + 
"-0.014162246118316702" + 
":  " + 
"(b('b2') <= 399.5) ? " + 
"-0.10364552993447648" + 
":  " + 
"-0.033225363586016486" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -16.030210494995117) ? " + 
"(b('grass') <= 87.20395278930664) ? " + 
"(b('bare') <= 0.29949215054512024) ? " + 
"-0.00713839952676259" + 
":  " + 
"0.001832215649919927" + 
":  " + 
"(b('lia') <= 31.96481227874756) ? " + 
"0.10900963650884657" + 
":  " + 
"0.006229973363394686" + 
":  " + 
"(b('bare') <= 4.18165922164917) ? " + 
"(b('grass') <= 80.8361587524414) ? " + 
"0.0180670358427543" + 
":  " + 
"-0.0819903580413863" + 
":  " + 
"(b('crop') <= 80.08920669555664) ? " + 
"-0.014899705718227532" + 
":  " + 
"0.1788596178454045" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -13.560813903808594) ? " + 
"(b('b1') <= 449.5) ? " + 
"(b('lia') <= 43.71833801269531) ? " + 
"-0.023265632596186123" + 
":  " + 
"0.03125663002906029" + 
":  " + 
"(b('grass') <= 98.36243438720703) ? " + 
"-0.0038098544143032" + 
":  " + 
"0.023179654853410007" + 
":  " + 
"(b('lia') <= 33.412641525268555) ? " + 
"(b('grass') <= 98.52795028686523) ? " + 
"-0.006177209335034693" + 
":  " + 
"0.12782273335697353" + 
":  " + 
"(b('moss') <= 7.358212232589722) ? " + 
"0.009659067147793325" + 
":  " + 
"-0.0018749243135998065" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('bare') <= 0.2583579495549202) ? " + 
"(b('ndvi') <= 972.0) ? " + 
"0.1856323645367442" + 
":  " + 
"0.02028777518577363" + 
":  " + 
"(b('g0vv') <= -6.519139766693115) ? " + 
"-0.0015600869068047628" + 
":  " + 
"0.03663681752769498" + 
":  " + 
"(b('grass') <= 5.992608308792114) ? " + 
"(b('trees') <= 3.8236643075942993) ? " + 
"-0.024333176016847587" + 
":  " + 
"-0.0019939150586960486" + 
":  " + 
"(b('crop') <= 66.59177017211914) ? " + 
"-0.0011915872531791814" + 
":  " + 
"0.015087348788503948" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 4619.5) ? " + 
"(b('g0vv') <= -13.039248943328857) ? " + 
"-0.004942412656194973" + 
":  " + 
"0.0018286248158038863" + 
":  " + 
"(b('ndvi') <= 4946.5) ? " + 
"-0.06401021337521401" + 
":  " + 
"-0.11786538929200173" + 
":  " + 
"(b('b4') <= 1028.5) ? " + 
"(b('ndvi') <= 5908.5) ? " + 
"0.15360035322543414" + 
":  " + 
"0.05657489870326031" + 
":  " + 
"(b('bare') <= 0.9388599693775177) ? " + 
"0.02299537607686128" + 
":  " + 
"-0.038867312270579255" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 23.278701782226562) ? " + 
"(b('g0vv') <= -8.988329887390137) ? " + 
"(b('crop') <= 76.58172988891602) ? " + 
"0.002008390678535062" + 
":  " + 
"-0.00761147400065011" + 
":  " + 
"(b('bare') <= 4.18165922164917) ? " + 
"0.018103456111456633" + 
":  " + 
"-0.007210765107062303" + 
":  " + 
"(b('urban') <= 29.42727279663086) ? " + 
"(b('b2') <= 488.0) ? " + 
"-0.06400016022061678" + 
":  " + 
"-0.02259616693827261" + 
":  " + 
"(b('lia') <= 42.42135047912598) ? " + 
"-0.009772832056831434" + 
":  " + 
"0.03460025077873774" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.28085994720459) ? " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('trees') <= 15.571342945098877) ? " + 
"-0.0002214456514794584" + 
":  " + 
"-0.04670028123697029" + 
":  " + 
"(b('trees') <= 19.04677391052246) ? " + 
"0.07665485762410246" + 
":  " + 
"0.0014066223290658477" + 
":  " + 
"(b('lia') <= 42.70411491394043) ? " + 
"(b('grass') <= 33.25920295715332) ? " + 
"-0.006198700064663275" + 
":  " + 
"-0.04504361963967013" + 
":  " + 
"(b('g0vh') <= -16.580275535583496) ? " + 
"0.018507192196556315" + 
":  " + 
"0.10173786144836854" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 3.2683908939361572) ? " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"(b('bare') <= 0.0628272220492363) ? " + 
"-0.017062696868680866" + 
":  " + 
"0.005365566564987822" + 
":  " + 
"(b('bare') <= 3.737146735191345) ? " + 
"0.02250903790194337" + 
":  " + 
"-0.02362073634440332" + 
":  " + 
"(b('moss') <= 3.325586199760437) ? " + 
"(b('b10') <= 1978.5) ? " + 
"0.030589707655726935" + 
":  " + 
"0.1450861125145576" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.006301758865161244" + 
":  " + 
"-0.005636124820810266" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 9.947502613067627) ? " + 
"(b('bare') <= 9.127102851867676) ? " + 
"(b('lia') <= 44.033355712890625) ? " + 
"-0.0011552227334970212" + 
":  " + 
"0.020962903168491785" + 
":  " + 
"(b('lia') <= 37.58181381225586) ? " + 
"-0.04831225841110585" + 
":  " + 
"-0.008181607617898608" + 
":  " + 
"(b('crop') <= 52.3651237487793) ? " + 
"(b('b4') <= 1081.0) ? " + 
"0.0556153596045758" + 
":  " + 
"0.0011148337396300774" + 
":  " + 
"(b('b4') <= 1035.5) ? " + 
"0.13600384933961068" + 
":  " + 
"0.1787250529000055" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('bare') <= 0.2583579495549202) ? " + 
"(b('ndvi') <= 972.0) ? " + 
"0.16925455086891875" + 
":  " + 
"0.018357683068687618" + 
":  " + 
"(b('b5') <= 2032.0) ? " + 
"0.029498127725062353" + 
":  " + 
"-0.0018151776908425273" + 
":  " + 
"(b('crop') <= 76.58172988891602) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.0006437717495466019" + 
":  " + 
"0.043207228829883516" + 
":  " + 
"(b('bare') <= 8.386428356170654) ? " + 
"-0.011914385835519983" + 
":  " + 
"0.1416280060078273" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.28085994720459) ? " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('b4') <= 592.5) ? " + 
"0.02176301833942865" + 
":  " + 
"-0.0013518722153370417" + 
":  " + 
"(b('trees') <= 19.04677391052246) ? " + 
"0.06785009032433222" + 
":  " + 
"0.0008943588462270412" + 
":  " + 
"(b('lia') <= 42.78861999511719) ? " + 
"(b('b3') <= 784.0) ? " + 
"-0.046103261659416604" + 
":  " + 
"-0.010715007934444094" + 
":  " + 
"(b('b1') <= 464.0) ? " + 
"0.06788042632419047" + 
":  " + 
"-0.0034281662181173695" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('moss') <= 9.849056243896484) ? " + 
"(b('b1') <= 213.5) ? " + 
"-0.02554958963933574" + 
":  " + 
"4.001778923586941e-06" + 
":  " + 
"(b('ndvi') <= 3693.5) ? " + 
"0.005921105706320314" + 
":  " + 
"0.056352634536487894" + 
":  " + 
"(b('b4') <= 1029.0) ? " + 
"(b('moss') <= 16.093793869018555) ? " + 
"-0.028419736064358693" + 
":  " + 
"0.007613607597626161" + 
":  " + 
"(b('b1') <= 377.5) ? " + 
"0.0831247038923937" + 
":  " + 
"-0.0014060397029290591" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 2244671.0) ? " + 
"(b('moss') <= 3.2275424003601074) ? " + 
"(b('crop') <= 32.8947639465332) ? " + 
"0.0075191926982289365" + 
":  " + 
"-0.010490925107505577" + 
":  " + 
"(b('moss') <= 4.659861326217651) ? " + 
"0.02052821582861575" + 
":  " + 
"-0.001364947868796375" + 
":  " + 
"(b('l8dt') <= 2245045.5) ? " + 
"(b('grass') <= 9.574844360351562) ? " + 
"0.2138985818546083" + 
":  " + 
"0.10597789588637441" + 
":  " + 
"(b('b6') <= 2153.5) ? " + 
"-0.01346283845289554" + 
":  " + 
"0.010055778817359945" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('g0vv') <= -7.36534571647644) ? " + 
"0.004144676866484682" + 
":  " + 
"0.03265314252770583" + 
":  " + 
"(b('grass') <= 3.1685575246810913) ? " + 
"-0.024292291345002794" + 
":  " + 
"-0.0003953112688550972" + 
":  " + 
"(b('b4') <= 1028.5) ? " + 
"(b('ndvi') <= 5908.5) ? " + 
"0.1362256099262311" + 
":  " + 
"0.04837847457344993" + 
":  " + 
"(b('trees') <= 16.78393316268921) ? " + 
"-0.030524078028053743" + 
":  " + 
"0.01995071945456786" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 255115.5) ? " + 
"(b('l8dt') <= 2936.0) ? " + 
"(b('b3') <= 1037.0) ? " + 
"0.01264514984461671" + 
":  " + 
"0.11783198873320087" + 
":  " + 
"(b('g0vh') <= -12.86878252029419) ? " + 
"-0.005755332208751655" + 
":  " + 
"0.0653950406297953" + 
":  " + 
"(b('l8dt') <= 261034.0) ? " + 
"(b('g0vv') <= -12.266942501068115) ? " + 
"0.023028403201824574" + 
":  " + 
"0.07445297654846263" + 
":  " + 
"(b('g0vv') <= -13.703631401062012) ? " + 
"-0.007279034722004602" + 
":  " + 
"0.0022773394239242167" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.28085994720459) ? " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('trees') <= 15.571342945098877) ? " + 
"-9.519749424147227e-05" + 
":  " + 
"-0.04108561945251372" + 
":  " + 
"(b('trees') <= 19.114258766174316) ? " + 
"0.059179728667347546" + 
":  " + 
"0.0006641171556303165" + 
":  " + 
"(b('grass') <= 21.67176628112793) ? " + 
"(b('lia') <= 41.671926498413086) ? " + 
"-0.0077488926268524504" + 
":  " + 
"0.06411452052117331" + 
":  " + 
"(b('g0vv') <= -11.155078887939453) ? " + 
"-0.040799046526278415" + 
":  " + 
"0.013351326712330604" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 9.947502613067627) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('bare') <= 0.29949215054512024) ? " + 
"-0.0025535879521954284" + 
":  " + 
"0.01214158754154166" + 
":  " + 
"(b('trees') <= 1.1431602239608765) ? " + 
"0.009476476244221007" + 
":  " + 
"-0.010890609764598538" + 
":  " + 
"(b('bare') <= 10.240853786468506) ? " + 
"(b('b4') <= 1035.5) ? " + 
"0.10858813295979108" + 
":  " + 
"0.14684010970349765" + 
":  " + 
"(b('ndvi') <= 2103.0) ? " + 
"-6.492808277919902e-05" + 
":  " + 
"0.03868698431752184" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 87.20395278930664) ? " + 
"(b('g0vv') <= -14.876858234405518) ? " + 
"(b('b1') <= 449.5) ? " + 
"-0.042718037185227764" + 
":  " + 
"-0.0018549643183021288" + 
":  " + 
"(b('b1') <= 352.5) ? " + 
"0.007353908097277953" + 
":  " + 
"-0.0019408985094676518" + 
":  " + 
"(b('lia') <= 31.96481227874756) ? " + 
"(b('g0vv') <= -15.538355350494385) ? " + 
"0.055828744207051896" + 
":  " + 
"0.1290533152536302" + 
":  " + 
"(b('grass') <= 88.49948501586914) ? " + 
"0.05436052316312315" + 
":  " + 
"-0.004925946197623492" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 28.176219940185547) ? " + 
"(b('crop') <= 24.69420051574707) ? " + 
"(b('trees') <= 20.289265632629395) ? " + 
"0.002484828864056841" + 
":  " + 
"-0.02867606650284419" + 
":  " + 
"(b('b3') <= 614.0) ? " + 
"0.015505425852114582" + 
":  " + 
"0.1256955621042631" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"(b('grass') <= 51.60679244995117) ? " + 
"-0.001163487593804563" + 
":  " + 
"0.07641663366838293" + 
":  " + 
"(b('crop') <= 35.33369064331055) ? " + 
"0.012306920255745908" + 
":  " + 
"-0.09124852070122454" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1813.0) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"(b('crop') <= 99.21989440917969) ? " + 
"0.007023712668872355" + 
":  " + 
"0.0830018641131766" + 
":  " + 
"(b('g0vv') <= -10.174977779388428) ? " + 
"0.20979945977819764" + 
":  " + 
"0.2508054700241582" + 
":  " + 
"(b('b4') <= 545.5) ? " + 
"(b('b5') <= 2688.5) ? " + 
"-0.0060762328628793175" + 
":  " + 
"0.06306237638188157" + 
":  " + 
"(b('b4') <= 557.0) ? " + 
"-0.06315080058309565" + 
":  " + 
"-0.0008489213466195827" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 23.278701782226562) ? " + 
"(b('urban') <= 14.72341012954712) ? " + 
"(b('g0vv') <= -9.567555904388428) ? " + 
"-0.0011317649556869375" + 
":  " + 
"0.006593466639410167" + 
":  " + 
"(b('b6') <= 2987.5) ? " + 
"0.11337537771745418" + 
":  " + 
"0.009050870250522074" + 
":  " + 
"(b('b6') <= 3016.0) ? " + 
"(b('bare') <= 0.4333333373069763) ? " + 
"-0.038279523227901166" + 
":  " + 
"-0.010240239162912185" + 
":  " + 
"(b('b4') <= 1011.5) ? " + 
"-0.08329116901858591" + 
":  " + 
"0.010372537133171043" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 33.45884704589844) ? " + 
"(b('grass') <= 98.52795028686523) ? " + 
"(b('lia') <= 32.34379196166992) ? " + 
"-0.0012215148936910792" + 
":  " + 
"-0.024137553251312095" + 
":  " + 
"(b('g0vh') <= -20.675564765930176) ? " + 
"0.05580888659308444" + 
":  " + 
"0.14675512214184835" + 
":  " + 
"(b('lia') <= 34.96310615539551) ? " + 
"(b('bare') <= 2.413899302482605) ? " + 
"0.03961465470130869" + 
":  " + 
"-0.0038374244994738606" + 
":  " + 
"(b('moss') <= 13.232231140136719) ? " + 
"0.002113809275985631" + 
":  " + 
"-0.007016578864983473" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 5.855041980743408) ? " + 
"(b('crop') <= 94.68265533447266) ? " + 
"-0.01007114149260372" + 
":  " + 
"0.01893629992036545" + 
":  " + 
"(b('moss') <= 12.852458953857422) ? " + 
"0.01814602801583317" + 
":  " + 
"-0.007569381505035773" + 
":  " + 
"(b('moss') <= 7.337804079055786) ? " + 
"(b('moss') <= 0.4266425520181656) ? " + 
"-0.003152757217513972" + 
":  " + 
"0.020065430116133952" + 
":  " + 
"(b('moss') <= 9.604410648345947) ? " + 
"-0.013921513538734324" + 
":  " + 
"0.0010591130506405154" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 4619.5) ? " + 
"(b('bare') <= 0.29949215054512024) ? " + 
"-0.0025969654985771484" + 
":  " + 
"0.002376699515452725" + 
":  " + 
"(b('ndvi') <= 4946.5) ? " + 
"-0.056533786797622276" + 
":  " + 
"-0.09954533507522177" + 
":  " + 
"(b('b3') <= 1098.5) ? " + 
"(b('ndvi') <= 5908.5) ? " + 
"0.12230152160360834" + 
":  " + 
"0.044754743045957515" + 
":  " + 
"(b('trees') <= 16.78393316268921) ? " + 
"-0.025489061133324765" + 
":  " + 
"0.015139559979981135" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1813.0) ? " + 
"(b('b6') <= 1500.0) ? " + 
"(b('b2') <= 182.0) ? " + 
"0.029453225207529885" + 
":  " + 
"-0.04757571491140532" + 
":  " + 
"(b('g0vv') <= -13.571380138397217) ? " + 
"-0.018039338142981115" + 
":  " + 
"0.02467901804643447" + 
":  " + 
"(b('b4') <= 545.5) ? " + 
"(b('b5') <= 2688.5) ? " + 
"-0.005175590951661735" + 
":  " + 
"0.05598218845458528" + 
":  " + 
"(b('b4') <= 547.0) ? " + 
"-0.13311479001257068" + 
":  " + 
"-0.0008635470796478962" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 9.947502613067627) ? " + 
"(b('bare') <= 9.127102851867676) ? " + 
"(b('ndvi') <= 980.0) ? " + 
"0.03379776180764398" + 
":  " + 
"-0.0006961173099907751" + 
":  " + 
"(b('b6') <= 2873.0) ? " + 
"-0.012391097986196071" + 
":  " + 
"-0.046977308526548675" + 
":  " + 
"(b('bare') <= 10.240853786468506) ? " + 
"(b('b4') <= 1035.5) ? " + 
"0.09595818702418789" + 
":  " + 
"0.13229200391396562" + 
":  " + 
"(b('b4') <= 1081.0) ? " + 
"0.04589680316194257" + 
":  " + 
"0.0012627440302298944" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 23.278701782226562) ? " + 
"(b('urban') <= 14.72341012954712) ? " + 
"(b('crop') <= 28.176219940185547) ? " + 
"0.0038327398041535054" + 
":  " + 
"-0.0017395638310866227" + 
":  " + 
"(b('b6') <= 2876.5) ? " + 
"0.10661993650649332" + 
":  " + 
"0.008931257604985162" + 
":  " + 
"(b('moss') <= 1.6670465469360352) ? " + 
"(b('b4') <= 1069.5) ? " + 
"-0.0012593824016910245" + 
":  " + 
"0.11347508254287003" + 
":  " + 
"(b('moss') <= 2.433658003807068) ? " + 
"-0.03939738559800264" + 
":  " + 
"-0.00882998182302817" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 1115587.0) ? " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('trees') <= 13.571214199066162) ? " + 
"-0.0015950867513780296" + 
":  " + 
"-0.023039186005687745" + 
":  " + 
"(b('trees') <= 19.04677391052246) ? " + 
"0.07154284422272096" + 
":  " + 
"-0.002995615155540978" + 
":  " + 
"(b('g0vv') <= -14.90896463394165) ? " + 
"(b('b1') <= 490.5) ? " + 
"-0.03508616793102334" + 
":  " + 
"-0.00033541835834672304" + 
":  " + 
"(b('grass') <= 38.20339584350586) ? " + 
"0.0019707496714273637" + 
":  " + 
"0.014662978997799798" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -8.94718074798584) ? " + 
"(b('lia') <= 33.82697677612305) ? " + 
"(b('grass') <= 98.52795028686523) ? " + 
"-0.00806356445172877" + 
":  " + 
"0.05922401628613069" + 
":  " + 
"(b('ndvi') <= 4168.0) ? " + 
"-0.0005090076199553057" + 
":  " + 
"0.01042208482184796" + 
":  " + 
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('grass') <= 98.10429382324219) ? " + 
"0.012124847404412852" + 
":  " + 
"-0.07208842186367487" + 
":  " + 
"(b('crop') <= 48.84012222290039) ? " + 
"0.03140988613485632" + 
":  " + 
"-0.012942562109107015" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 0.06014965660870075) ? " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('b7') <= 1988.5) ? " + 
"-0.016872482604199147" + 
":  " + 
"0.00331170860197135" + 
":  " + 
"(b('b3') <= 786.0) ? " + 
"0.005352017242730923" + 
":  " + 
"0.13825800057230744" + 
":  " + 
"(b('moss') <= 1.940559446811676) ? " + 
"(b('b4') <= 792.5) ? " + 
"-0.01896698438499161" + 
":  " + 
"0.03043539427442007" + 
":  " + 
"(b('moss') <= 3.2275424003601074) ? " + 
"-0.015211492454172904" + 
":  " + 
"0.0015975295979029406" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.28085994720459) ? " + 
"(b('trees') <= 18.062620162963867) ? " + 
"(b('b4') <= 592.5) ? " + 
"0.016684340645215685" + 
":  " + 
"-0.0009278567132991127" + 
":  " + 
"(b('trees') <= 19.04677391052246) ? " + 
"0.07449177217277936" + 
":  " + 
"0.00011966655584825543" + 
":  " + 
"(b('lia') <= 43.255964279174805) ? " + 
"(b('b3') <= 934.0) ? " + 
"-0.033754003234938566" + 
":  " + 
"0.004342759533375385" + 
":  " + 
"(b('b6') <= 2763.5) ? " + 
"0.06481219462971273" + 
":  " + 
"-0.011329152450829057" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.959776878356934) ? " + 
"(b('moss') <= 9.849056243896484) ? " + 
"(b('b1') <= 217.5) ? " + 
"-0.021564691024457527" + 
":  " + 
"0.00020802996062225734" + 
":  " + 
"(b('ndvi') <= 3693.5) ? " + 
"0.0034182827128354013" + 
":  " + 
"0.04635462883318364" + 
":  " + 
"(b('moss') <= 14.038605690002441) ? " + 
"(b('crop') <= 22.816326141357422) ? " + 
"-0.0683332606697955" + 
":  " + 
"-0.028083953139416546" + 
":  " + 
"(b('b6') <= 2528.0) ? " + 
"-0.016913082042229036" + 
":  " + 
"0.000951748572907493" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1813.0) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"(b('crop') <= 99.21989440917969) ? " + 
"0.005981669122206188" + 
":  " + 
"0.07136476723424434" + 
":  " + 
"(b('g0vv') <= -10.174977779388428) ? " + 
"0.18418818580613944" + 
":  " + 
"0.22405019757882247" + 
":  " + 
"(b('b3') <= 486.0) ? " + 
"(b('trees') <= 14.257917881011963) ? " + 
"-0.1509670351183915" + 
":  " + 
"-0.0413544195998827" + 
":  " + 
"(b('b4') <= 545.5) ? " + 
"0.02490958706097944" + 
":  " + 
"-0.000817548798146632" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5439.0) ? " + 
"(b('b5') <= 4653.0) ? " + 
"(b('g0vv') <= -10.227709770202637) ? " + 
"-0.0013915962588008858" + 
":  " + 
"0.0035499622845852727" + 
":  " + 
"(b('b4') <= 1028.5) ? " + 
"0.06728826159943274" + 
":  " + 
"-0.01781374371766826" + 
":  " + 
"(b('g0vh') <= -21.055819511413574) ? " + 
"(b('l8dt') <= 255433.0) ? " + 
"-0.017077059780255734" + 
":  " + 
"0.04120054424643982" + 
":  " + 
"(b('ndvi') <= 1282.0) ? " + 
"-0.027729080071938153" + 
":  " + 
"-0.06212496301561839" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -6.591407537460327) ? " + 
"(b('lia') <= 33.42738151550293) ? " + 
"(b('grass') <= 79.13820266723633) ? " + 
"-0.007655172334618855" + 
":  " + 
"0.0278185742198374" + 
":  " + 
"(b('lia') <= 35.165565490722656) ? " + 
"0.011740563248254506" + 
":  " + 
"5.9217243559266016e-05" + 
":  " + 
"(b('grass') <= 4.1582722663879395) ? " + 
"(b('b5') <= 3510.0) ? " + 
"0.04217118953378444" + 
":  " + 
"-0.003697887469264771" + 
":  " + 
"(b('grass') <= 4.299890756607056) ? " + 
"-0.09428779301461374" + 
":  " + 
"0.003706662001084513" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('moss') <= 13.959776878356934) ? " + 
"(b('moss') <= 9.849056243896484) ? " + 
"-0.0003916692400359884" + 
":  " + 
"0.008235354618161514" + 
":  " + 
"(b('b3') <= 634.0) ? " + 
"-0.040575373384682645" + 
":  " + 
"-0.0040256330177286595" + 
":  " + 
"(b('b6') <= 3242.5) ? " + 
"(b('l8dt') <= 814990.0) ? " + 
"0.09180193501887243" + 
":  " + 
"0.002331919478849219" + 
":  " + 
"(b('b6') <= 4360.0) ? " + 
"0.034642593276026985" + 
":  " + 
"0.00647058774478161" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.35122537612915) ? " + 
"(b('b1') <= 449.5) ? " + 
"(b('grass') <= 63.800655364990234) ? " + 
"-0.039891390104139224" + 
":  " + 
"-0.012173449313929371" + 
":  " + 
"(b('g0vh') <= -21.673279762268066) ? " + 
"0.010248354608618258" + 
":  " + 
"-0.00792128760216176" + 
":  " + 
"(b('b5') <= 1813.0) ? " + 
"(b('b6') <= 1500.0) ? " + 
"-0.02597027057253239" + 
":  " + 
"0.019538086232033347" + 
":  " + 
"(b('b4') <= 544.5) ? " + 
"0.021465215325086225" + 
":  " + 
"-0.00020893788572216623" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 255115.5) ? " + 
"(b('l8dt') <= 2936.0) ? " + 
"(b('b3') <= 1028.0) ? " + 
"0.008218870189338937" + 
":  " + 
"0.09855608330480159" + 
":  " + 
"(b('g0vh') <= -12.86878252029419) ? " + 
"-0.0046120760843874455" + 
":  " + 
"0.057536212429067854" + 
":  " + 
"(b('l8dt') <= 261034.0) ? " + 
"(b('ndvi') <= 2882.5) ? " + 
"0.06084480004489414" + 
":  " + 
"0.014208467640198688" + 
":  " + 
"(b('g0vv') <= -13.129822254180908) ? " + 
"-0.004733089880140634" + 
":  " + 
"0.0020783760941372907" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.28085994720459) ? " + 
"(b('trees') <= 18.062620162963867) ? " + 
"(b('trees') <= 12.501765251159668) ? " + 
"0.0006377478446289909" + 
":  " + 
"-0.00963913695737436" + 
":  " + 
"(b('trees') <= 19.04677391052246) ? " + 
"0.06706958156879489" + 
":  " + 
"0.0006097747587509783" + 
":  " + 
"(b('grass') <= 21.67176628112793) ? " + 
"(b('lia') <= 41.671926498413086) ? " + 
"-0.005661155650207193" + 
":  " + 
"0.05522246487929713" + 
":  " + 
"(b('b4') <= 1295.5) ? " + 
"-0.03009003900836835" + 
":  " + 
"0.03947878236114569" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 0.06014965660870075) ? " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('b10') <= 1988.5) ? " + 
"-0.015187091468570956" + 
":  " + 
"0.0030462008833716503" + 
":  " + 
"(b('b3') <= 786.0) ? " + 
"-0.002203877783013062" + 
":  " + 
"0.11438145687613938" + 
":  " + 
"(b('moss') <= 1.940559446811676) ? " + 
"(b('b4') <= 613.5) ? " + 
"-0.056004157561396865" + 
":  " + 
"0.020710968974650003" + 
":  " + 
"(b('moss') <= 3.2275424003601074) ? " + 
"-0.013693246460881688" + 
":  " + 
"0.0014991130794055666" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 135.0) ? " + 
"(b('g0vv') <= -12.587978839874268) ? " + 
"(b('l8dt') <= 518406.0) ? " + 
"0.09239764955054663" + 
":  " + 
"0.1828404793976095" + 
":  " + 
"(b('b2') <= 97.0) ? " + 
"-0.01589902302507227" + 
":  " + 
"0.06552888950900362" + 
":  " + 
"(b('b3') <= 437.0) ? " + 
"(b('b4') <= 494.5) ? " + 
"-0.029626779198497998" + 
":  " + 
"-0.12839819167092828" + 
":  " + 
"(b('b4') <= 544.5) ? " + 
"0.018768282045618406" + 
":  " + 
"-0.00023184820401991933" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 9.947502613067627) ? " + 
"(b('bare') <= 9.127102851867676) ? " + 
"(b('ndvi') <= 974.5) ? " + 
"0.03146315995619705" + 
":  " + 
"-0.0005517704269634719" + 
":  " + 
"(b('b4') <= 882.25) ? " + 
"0.00924365770126868" + 
":  " + 
"-0.036507556510751805" + 
":  " + 
"(b('bare') <= 10.240853786468506) ? " + 
"(b('b2') <= 603.0) ? " + 
"0.08553476663579446" + 
":  " + 
"0.11822304233979725" + 
":  " + 
"(b('ndvi') <= 2245.5) ? " + 
"-0.00032674517702430665" + 
":  " + 
"0.03492502226504445" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 2391007.0) ? " + 
"(b('b5') <= 1807.0) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"0.009133433356372386" + 
":  " + 
"0.18125877312177696" + 
":  " + 
"(b('grass') <= 87.20395278930664) ? " + 
"-0.001967015180542" + 
":  " + 
"0.009284369539807968" + 
":  " + 
"(b('moss') <= 1.940559446811676) ? " + 
"(b('moss') <= 1.398017704486847) ? " + 
"0.008343481009447824" + 
":  " + 
"0.06608438693012575" + 
":  " + 
"(b('trees') <= 12.64185619354248) ? " + 
"0.005243449265184845" + 
":  " + 
"-0.017534474138339296" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 0.06014965660870075) ? " + 
"(b('lia') <= 43.538774490356445) ? " + 
"(b('crop') <= 32.8947639465332) ? " + 
"0.009137267495496832" + 
":  " + 
"-0.008202900413182621" + 
":  " + 
"(b('lia') <= 43.72256278991699) ? " + 
"-0.08294315394014144" + 
":  " + 
"-0.001649884811484031" + 
":  " + 
"(b('moss') <= 1.940559446811676) ? " + 
"(b('b4') <= 792.5) ? " + 
"-0.017051693730682053" + 
":  " + 
"0.025142982090183022" + 
":  " + 
"(b('moss') <= 2.3705118894577026) ? " + 
"-0.020814613391057807" + 
":  " + 
"0.0007785804901701816" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 66.14077377319336) ? " + 
"(b('crop') <= 62.66942024230957) ? " + 
"(b('moss') <= 0.9462673366069794) ? " + 
"-0.0076249526950426215" + 
":  " + 
"0.002928751398082435" + 
":  " + 
"(b('urban') <= 19.966037273406982) ? " + 
"-0.029202165197879663" + 
":  " + 
"-0.0016512800248798026" + 
":  " + 
"(b('crop') <= 76.58172988891602) ? " + 
"(b('b2') <= 448.0) ? " + 
"-0.013223461372407035" + 
":  " + 
"0.03687966796256417" + 
":  " + 
"(b('bare') <= 8.386428356170654) ? " + 
"-0.0023643480754928147" + 
":  " + 
"0.09233383348318472" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b6') <= 1842.5) ? " + 
"(b('b6') <= 1835.5) ? " + 
"0.024473999864297376" + 
":  " + 
"0.1045367171145593" + 
":  " + 
"(b('b10') <= 1726.0) ? " + 
"-0.011981632232530749" + 
":  " + 
"0.006839738292132152" + 
":  " + 
"(b('grass') <= 5.215661525726318) ? " + 
"(b('lia') <= 30.6566219329834) ? " + 
"0.023566098962161712" + 
":  " + 
"-0.012670522528879848" + 
":  " + 
"(b('grass') <= 5.344100475311279) ? " + 
"0.15963347417057205" + 
":  " + 
"3.650595403762841e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('lia') <= 34.08248710632324) ? " + 
"-0.004020072615380002" + 
":  " + 
"0.0026209601239449375" + 
":  " + 
"(b('l8dt') <= 1878917.0) ? " + 
"0.03540264812015377" + 
":  " + 
"0.1074372125325819" + 
":  " + 
"(b('b4') <= 1029.0) ? " + 
"(b('grass') <= 65.19527816772461) ? " + 
"-0.005953507275013562" + 
":  " + 
"-0.03202827860396068" + 
":  " + 
"(b('b1') <= 371.0) ? " + 
"0.08040609237774371" + 
":  " + 
"-0.00020418036688850014" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.928560256958008) ? " + 
"(b('b7') <= 1413.0) ? " + 
"(b('b3') <= 795.0) ? " + 
"-0.05046193521862558" + 
":  " + 
"0.022233082765254868" + 
":  " + 
"(b('ndvi') <= 4288.5) ? " + 
"-0.004859125868304561" + 
":  " + 
"0.03951305871672949" + 
":  " + 
"(b('grass') <= 39.87313461303711) ? " + 
"(b('grass') <= 23.881052017211914) ? " + 
"0.0013408935712786061" + 
":  " + 
"-0.011801650303519536" + 
":  " + 
"(b('crop') <= 37.13176345825195) ? " + 
"0.00015970115628057715" + 
":  " + 
"0.051367474978050734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 668.5) ? " + 
"(b('b5') <= 3389.5) ? " + 
"(b('crop') <= 66.14077377319336) ? " + 
"-0.00191277287362991" + 
":  " + 
"0.005838809114165112" + 
":  " + 
"(b('b2') <= 343.5) ? " + 
"-0.06614315559887282" + 
":  " + 
"-0.006799158565339793" + 
":  " + 
"(b('b4') <= 2032.5) ? " + 
"(b('b5') <= 3585.0) ? " + 
"0.011774412047088905" + 
":  " + 
"0.06412536598153636" + 
":  " + 
"(b('ndvi') <= 3466.0) ? " + 
"-0.005317278826570316" + 
":  " + 
"0.04865051469129885" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -15.756814956665039) ? " + 
"(b('grass') <= 87.20395278930664) ? " + 
"(b('g0vv') <= -15.837446689605713) ? " + 
"-0.016565908176419168" + 
":  " + 
"-0.0007698911021518331" + 
":  " + 
"(b('lia') <= 31.924128532409668) ? " + 
"0.07326533340168877" + 
":  " + 
"0.004067596861421215" + 
":  " + 
"(b('bare') <= 6.56046462059021) ? " + 
"(b('urban') <= 3.9101978540420532) ? " + 
"0.015164614574563102" + 
":  " + 
"-0.00530523327260456" + 
":  " + 
"(b('grass') <= 6.9276041984558105) ? " + 
"-0.045673289742661445" + 
":  " + 
"0.030685313943118773" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"(b('grass') <= 45.666046142578125) ? " + 
"-0.0010494730888689718" + 
":  " + 
"-0.09526449817370579" + 
":  " + 
"(b('ndvi') <= 4267.0) ? " + 
"-0.00023571448930164202" + 
":  " + 
"0.04351610994694349" + 
":  " + 
"(b('b6') <= 3242.5) ? " + 
"(b('l8dt') <= 814990.0) ? " + 
"0.08270020903665272" + 
":  " + 
"0.0020713203620821505" + 
":  " + 
"(b('b6') <= 4360.0) ? " + 
"0.031767855050722306" + 
":  " + 
"0.006366380289625753" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.28085994720459) ? " + 
"(b('trees') <= 19.831669807434082) ? " + 
"(b('trees') <= 19.15903377532959) ? " + 
"0.0002616399374565525" + 
":  " + 
"-0.03528189372420719" + 
":  " + 
"(b('ndvi') <= 2799.5) ? " + 
"0.040686812586503925" + 
":  " + 
"-0.013372173853491954" + 
":  " + 
"(b('lia') <= 42.620988845825195) ? " + 
"(b('b3') <= 934.0) ? " + 
"-0.029373628337518935" + 
":  " + 
"0.0032355260554822896" + 
":  " + 
"(b('g0vh') <= -16.580275535583496) ? " + 
"0.009533369631320008" + 
":  " + 
"0.07501528526853946" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5439.0) ? " + 
"(b('b1') <= 668.5) ? " + 
"(b('b6') <= 3304.5) ? " + 
"0.0006894790706249952" + 
":  " + 
"-0.006836318859204679" + 
":  " + 
"(b('b4') <= 2032.5) ? " + 
"0.012825534464041652" + 
":  " + 
"-0.002941748541032483" + 
":  " + 
"(b('g0vh') <= -21.055819511413574) ? " + 
"(b('lia') <= 38.14970779418945) ? " + 
"0.01694399493033337" + 
":  " + 
"-0.029167203644141576" + 
":  " + 
"(b('ndvi') <= 1282.0) ? " + 
"-0.023837607069572667" + 
":  " + 
"-0.054762240906855594" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 23.278701782226562) ? " + 
"(b('urban') <= 14.72341012954712) ? " + 
"(b('moss') <= 0.06014965660870075) ? " + 
"-0.0037589168387512917" + 
":  " + 
"0.0013434779638562561" + 
":  " + 
"(b('lia') <= 43.19400215148926) ? " + 
"0.06816246370233216" + 
":  " + 
"-0.004464023240726967" + 
":  " + 
"(b('ndvi') <= 714.5) ? " + 
"0.23694372766465896" + 
":  " + 
"(b('b6') <= 3016.0) ? " + 
"-0.013129059553357678" + 
":  " + 
"0.006213738840506757" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 375.5) ? " + 
"(b('b6') <= 2714.0) ? " + 
"(b('b6') <= 2219.5) ? " + 
"-0.002439231497674446" + 
":  " + 
"-0.027173858319790595" + 
":  " + 
"(b('crop') <= 23.834311485290527) ? " + 
"-0.14220843593606855" + 
":  " + 
"0.04895028661257191" + 
":  " + 
"(b('b2') <= 391.5) ? " + 
"(b('crop') <= 46.296260833740234) ? " + 
"0.04397731108413071" + 
":  " + 
"-0.01256103897568805" + 
":  " + 
"(b('lia') <= 41.80293083190918) ? " + 
"0.0015200089587076619" + 
":  " + 
"-0.005001290809600216" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 135.0) ? " + 
"(b('b6') <= 936.5) ? " + 
"(b('b6') <= 867.5) ? " + 
"-0.014157347620222272" + 
":  " + 
"0.0548024698592364" + 
":  " + 
"(b('l8dt') <= 518406.0) ? " + 
"0.08481670314509313" + 
":  " + 
"0.16494970909807707" + 
":  " + 
"(b('b3') <= 437.0) ? " + 
"(b('b4') <= 494.5) ? " + 
"-0.026806994192540783" + 
":  " + 
"-0.1126751859298434" + 
":  " + 
"(b('b4') <= 544.5) ? " + 
"0.015826903282034795" + 
":  " + 
"-0.00019114377504143395" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 4486.0) ? " + 
"(b('crop') <= 66.14077377319336) ? " + 
"-0.0014361751209124845" + 
":  " + 
"0.0028281659324924024" + 
":  " + 
"(b('ndvi') <= 5095.5) ? " + 
"-0.02570874847286738" + 
":  " + 
"-0.08158853533561058" + 
":  " + 
"(b('b3') <= 1098.5) ? " + 
"(b('ndvi') <= 5908.5) ? " + 
"0.0983814865370076" + 
":  " + 
"0.027132571995326003" + 
":  " + 
"(b('ndvi') <= 4556.0) ? " + 
"-0.016938373431074464" + 
":  " + 
"0.01622080334805734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -15.756814956665039) ? " + 
"(b('bare') <= 6.329379320144653) ? " + 
"(b('moss') <= 13.891517639160156) ? " + 
"-0.00032292275503164496" + 
":  " + 
"-0.0097666451915291" + 
":  " + 
"(b('bare') <= 6.56046462059021) ? " + 
"0.04709070519350346" + 
":  " + 
"0.0016944536129677936" + 
":  " + 
"(b('grass') <= 93.64754104614258) ? " + 
"(b('grass') <= 34.980010986328125) ? " + 
"0.002359155624448864" + 
":  " + 
"0.032089022457872665" + 
":  " + 
"(b('g0vh') <= -13.025058269500732) ? " + 
"-0.10130939858206502" + 
":  " + 
"0.029939651520848765" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 28.176219940185547) ? " + 
"(b('crop') <= 24.69420051574707) ? " + 
"(b('trees') <= 20.289265632629395) ? " + 
"0.0017161864517848421" + 
":  " + 
"-0.022431816866451293" + 
":  " + 
"(b('b3') <= 614.0) ? " + 
"0.009008881145185443" + 
":  " + 
"0.10123299648008854" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"(b('grass') <= 51.60679244995117) ? " + 
"-0.0008119821574183749" + 
":  " + 
"0.061214551419484654" + 
":  " + 
"(b('trees') <= 0.30901288986206055) ? " + 
"-0.07286501067030392" + 
":  " + 
"0.01718228216863756" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 882.5) ? " + 
"(b('b6') <= 3232.0) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"-0.0059687117310749434" + 
":  " + 
"0.006076228033499878" + 
":  " + 
"(b('b4') <= 1048.5) ? " + 
"-0.08306059155001684" + 
":  " + 
"-0.026455731631166695" + 
":  " + 
"(b('b4') <= 941.0) ? " + 
"(b('crop') <= 89.8235092163086) ? " + 
"0.02553598857666553" + 
":  " + 
"0.09877499505553428" + 
":  " + 
"(b('trees') <= 19.831669807434082) ? " + 
"-0.00034643181430446264" + 
":  " + 
"0.026132365079126096" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 347.5) ? " + 
"(b('b1') <= 261.5) ? " + 
"(b('b4') <= 737.5) ? " + 
"0.004655236030368492" + 
":  " + 
"-0.03147956482823247" + 
":  " + 
"(b('b4') <= 530.0) ? " + 
"0.05964568610554396" + 
":  " + 
"-0.062431274491519285" + 
":  " + 
"(b('b1') <= 254.5) ? " + 
"(b('b2') <= 349.5) ? " + 
"0.06494423301400185" + 
":  " + 
"-0.03660115087097038" + 
":  " + 
"(b('b1') <= 295.5) ? " + 
"0.01790865126265385" + 
":  " + 
"-1.7478061686077322e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1998.5) ? " + 
"(b('grass') <= 25.05943489074707) ? " + 
"(b('b3') <= 554.5) ? " + 
"-0.013437554195930079" + 
":  " + 
"0.023806564183481413" + 
":  " + 
"(b('b2') <= 697.0) ? " + 
"-0.00840559240697093" + 
":  " + 
"0.021409407977701647" + 
":  " + 
"(b('b2') <= 318.5) ? " + 
"(b('b2') <= 298.5) ? " + 
"-0.002605687812637063" + 
":  " + 
"0.038657208817212727" + 
":  " + 
"(b('b2') <= 347.5) ? " + 
"-0.02535168391619684" + 
":  " + 
"-0.0003908266096452949" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 169191.5) ? " + 
"(b('b2') <= 374.5) ? " + 
"(b('ndvi') <= 5584.0) ? " + 
"-0.026943694642786908" + 
":  " + 
"0.10057633170587513" + 
":  " + 
"(b('b4') <= 825.5) ? " + 
"0.007649583660194313" + 
":  " + 
"-0.004631293222015376" + 
":  " + 
"(b('l8dt') <= 174600.0) ? " + 
"(b('b2') <= 614.0) ? " + 
"0.010828400456754839" + 
":  " + 
"0.08583387849425868" + 
":  " + 
"(b('l8dt') <= 175067.0) ? " + 
"-0.06673002837359107" + 
":  " + 
"0.0005661510952871652" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 882.5) ? " + 
"(b('b6') <= 3232.0) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"-0.005544582382082117" + 
":  " + 
"0.005750612945075933" + 
":  " + 
"(b('b4') <= 1048.5) ? " + 
"-0.07477918127723392" + 
":  " + 
"-0.023539828160677206" + 
":  " + 
"(b('b4') <= 941.0) ? " + 
"(b('crop') <= 83.88826751708984) ? " + 
"0.020494153942202848" + 
":  " + 
"0.0691919927628042" + 
":  " + 
"(b('trees') <= 19.793859481811523) ? " + 
"-0.00032681184217148884" + 
":  " + 
"0.023243119650648736" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -8.94718074798584) ? " + 
"(b('g0vh') <= -15.123029708862305) ? " + 
"(b('b1') <= 668.5) ? " + 
"-0.00225493105667825" + 
":  " + 
"0.0035151432949993293" + 
":  " + 
"(b('bare') <= 6.56046462059021) ? " + 
"0.019231893824442795" + 
":  " + 
"-0.03858304209627454" + 
":  " + 
"(b('bare') <= 58.920827865600586) ? " + 
"(b('crop') <= 49.023324966430664) ? " + 
"0.02155403526607505" + 
":  " + 
"0.0028008637305521234" + 
":  " + 
"(b('moss') <= 15.96635913848877) ? " + 
"0.11201398201688194" + 
":  " + 
"-0.03531024148371542" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('crop') <= 66.14077377319336) ? " + 
"(b('crop') <= 62.66942024230957) ? " + 
"0.00040125391309215914" + 
":  " + 
"-0.0175830289081375" + 
":  " + 
"(b('grass') <= 23.252870559692383) ? " + 
"0.0029330010296669683" + 
":  " + 
"0.05745161859122385" + 
":  " + 
"(b('b5') <= 3525.5) ? " + 
"(b('moss') <= 4.337218999862671) ? " + 
"-0.09793030166813108" + 
":  " + 
"0.01082069073930493" + 
":  " + 
"(b('grass') <= 79.05599212646484) ? " + 
"-0.0038268914964670834" + 
":  " + 
"0.11223709403199979" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.28085994720459) ? " + 
"(b('trees') <= 18.062620162963867) ? " + 
"(b('trees') <= 12.501765251159668) ? " + 
"0.0005710854457725288" + 
":  " + 
"-0.00869145102658382" + 
":  " + 
"(b('trees') <= 19.04677391052246) ? " + 
"0.055500002936644435" + 
":  " + 
"0.0011360351121449312" + 
":  " + 
"(b('grass') <= 21.67176628112793) ? " + 
"(b('b5') <= 2973.5) ? " + 
"0.037680937116714865" + 
":  " + 
"-0.018684097814203052" + 
":  " + 
"(b('g0vv') <= -11.165242195129395) ? " + 
"-0.02893889881436891" + 
":  " + 
"0.011578961343862756" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('grass') <= 2.4253548979759216) ? " + 
"0.012051727032098706" + 
":  " + 
"-0.004094826828939996" + 
":  " + 
"(b('grass') <= 78.35647583007812) ? " + 
"-0.0011226650284420483" + 
":  " + 
"0.05610272867042578" + 
":  " + 
"(b('moss') <= 7.337804079055786) ? " + 
"(b('moss') <= 0.4266425520181656) ? " + 
"-0.0016210655897042096" + 
":  " + 
"0.015593616444605912" + 
":  " + 
"(b('ndvi') <= 3926.0) ? " + 
"-0.005202223739112734" + 
":  " + 
"0.015151424409429586" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('moss') <= 13.232231140136719) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"0.00031586203522853627" + 
":  " + 
"0.04441145652255551" + 
":  " + 
"(b('b6') <= 2528.0) ? " + 
"-0.015529861582489979" + 
":  " + 
"-0.0002086674643343927" + 
":  " + 
"(b('b6') <= 3242.5) ? " + 
"(b('l8dt') <= 814990.0) ? " + 
"0.0732697941282352" + 
":  " + 
"0.00179053220887216" + 
":  " + 
"(b('b6') <= 4360.0) ? " + 
"0.028759522357797662" + 
":  " + 
"0.006205836227353676" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 3.2683908939361572) ? " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"(b('b7') <= 1991.5) ? " + 
"-0.013997862127708188" + 
":  " + 
"-0.0003549005222522584" + 
":  " + 
"(b('trees') <= 6.157119512557983) ? " + 
"0.029254506050071807" + 
":  " + 
"-0.0018581936852861457" + 
":  " + 
"(b('moss') <= 3.325586199760437) ? " + 
"(b('b4') <= 1221.0) ? " + 
"0.016677272171687758" + 
":  " + 
"0.12576570291180217" + 
":  " + 
"(b('moss') <= 4.659861326217651) ? " + 
"0.01084651825258138" + 
":  " + 
"-0.000604459859049937" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1807.0) ? " + 
"(b('b10') <= 2179.0) ? " + 
"(b('g0vh') <= -21.921608924865723) ? " + 
"-0.03263300022837527" + 
":  " + 
"0.008002214952562196" + 
":  " + 
"(b('b4') <= 1068.0) ? " + 
"0.013324917346306416" + 
":  " + 
"0.08184718665908713" + 
":  " + 
"(b('grass') <= 87.20395278930664) ? " + 
"(b('b11') <= 1022.5) ? " + 
"0.017215132222109263" + 
":  " + 
"-0.0012981065197434395" + 
":  " + 
"(b('b1') <= 384.5) ? " + 
"-0.028655169273772835" + 
":  " + 
"0.016440203237043576" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3281582.0) ? " + 
"(b('moss') <= 3.2683908939361572) ? " + 
"(b('crop') <= 32.8947639465332) ? " + 
"0.005880080833871202" + 
":  " + 
"-0.006250006374784463" + 
":  " + 
"(b('moss') <= 4.659861326217651) ? " + 
"0.013457369476634867" + 
":  " + 
"-0.0007475865825284724" + 
":  " + 
"(b('g0vv') <= -13.693597316741943) ? " + 
"(b('ndvi') <= 1742.5) ? " + 
"0.1046621021331689" + 
":  " + 
"0.023888430985744936" + 
":  " + 
"(b('crop') <= 16.048566341400146) ? " + 
"-0.019788954117200844" + 
":  " + 
"0.007827895785818087" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b4') <= 553.0) ? " + 
"(b('b2') <= 346.5) ? " + 
"0.0379247677742235" + 
":  " + 
"0.15295559385706733" + 
":  " + 
"(b('g0vv') <= -7.122606992721558) ? " + 
"0.002207283681398983" + 
":  " + 
"0.02380042440852538" + 
":  " + 
"(b('crop') <= 76.58172988891602) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.0006648536625065398" + 
":  " + 
"0.0299248711581775" + 
":  " + 
"(b('bare') <= 8.386428356170654) ? " + 
"-0.006979310978781412" + 
":  " + 
"0.08177287952371934" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 135.0) ? " + 
"(b('ndvi') <= 3701.5) ? " + 
"(b('b6') <= 867.5) ? " + 
"-0.011416466362901844" + 
":  " + 
"0.048513270138350356" + 
":  " + 
"(b('l8dt') <= 518406.0) ? " + 
"0.07465341509823845" + 
":  " + 
"0.14677312045592397" + 
":  " + 
"(b('b3') <= 437.0) ? " + 
"(b('b11') <= 865.0) ? " + 
"-0.0214735314420786" + 
":  " + 
"-0.1003712913443308" + 
":  " + 
"(b('b5') <= 1154.5) ? " + 
"0.06395203481022364" + 
":  " + 
"8.383858261455787e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('crop') <= 5.957038402557373) ? " + 
"(b('g0vh') <= -18.439754486083984) ? " + 
"0.00023539704791323892" + 
":  " + 
"-0.01662608942414934" + 
":  " + 
"(b('crop') <= 28.176219940185547) ? " + 
"0.018436411614026284" + 
":  " + 
"-0.00017870853959963995" + 
":  " + 
"(b('b5') <= 3525.5) ? " + 
"(b('moss') <= 4.337218999862671) ? " + 
"-0.09002073206182697" + 
":  " + 
"0.00788378953214059" + 
":  " + 
"(b('grass') <= 79.05599212646484) ? " + 
"-0.0036056898675241216" + 
":  " + 
"0.10171943582658655" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.928560256958008) ? " + 
"(b('trees') <= 0.03652967885136604) ? " + 
"(b('moss') <= 7.53682541847229) ? " + 
"-0.005537411321012791" + 
":  " + 
"0.01401334321933457" + 
":  " + 
"(b('b1') <= 487.5) ? " + 
"-0.029759383365595186" + 
":  " + 
"-0.0037463925594965774" + 
":  " + 
"(b('b5') <= 1807.0) ? " + 
"(b('b6') <= 1500.0) ? " + 
"-0.0190679160485484" + 
":  " + 
"0.01470590151047739" + 
":  " + 
"(b('l8dt') <= 1115586.5) ? " + 
"-0.0012809242245739325" + 
":  " + 
"0.0034577643004941963" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 23.278701782226562) ? " + 
"(b('urban') <= 14.72341012954712) ? " + 
"(b('crop') <= 28.176219940185547) ? " + 
"0.0026538622166939856" + 
":  " + 
"-0.0012348339850039485" + 
":  " + 
"(b('g0vv') <= -11.89726734161377) ? " + 
"0.009284881597630641" + 
":  " + 
"0.10177062500682589" + 
":  " + 
"(b('ndvi') <= 714.5) ? " + 
"0.2108417146775571" + 
":  " + 
"(b('b6') <= 3016.0) ? " + 
"-0.011668809529989024" + 
":  " + 
"0.005311052787900884" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 375.5) ? " + 
"(b('ndvi') <= 2939.0) ? " + 
"(b('b6') <= 2558.5) ? " + 
"0.00039165191066322015" + 
":  " + 
"0.036485343440994564" + 
":  " + 
"(b('trees') <= 13.24367094039917) ? " + 
"-0.004346289364861241" + 
":  " + 
"-0.03553078631811453" + 
":  " + 
"(b('b1') <= 254.0) ? " + 
"(b('b4') <= 790.0) ? " + 
"-0.01383808039456032" + 
":  " + 
"-0.047802514774269174" + 
":  " + 
"(b('b1') <= 299.5) ? " + 
"0.01847344997130959" + 
":  " + 
"1.6350350581780787e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1646.5) ? " + 
"(b('crop') <= 99.63687133789062) ? " + 
"(b('trees') <= 19.814208030700684) ? " + 
"-0.0038643171061582683" + 
":  " + 
"0.029535916828549152" + 
":  " + 
"(b('b2') <= 507.5) ? " + 
"-0.00466884210971079" + 
":  " + 
"0.10531145241762935" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('moss') <= 13.232231140136719) ? " + 
"0.0014887128184414421" + 
":  " + 
"-0.006896077196746043" + 
":  " + 
"(b('bare') <= 12.268785953521729) ? " + 
"0.07005785823561565" + 
":  " + 
"0.01895236251066132" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 668.5) ? " + 
"(b('b5') <= 3389.5) ? " + 
"(b('g0vv') <= -10.089441299438477) ? " + 
"-0.0013046256786966766" + 
":  " + 
"0.005427936386520718" + 
":  " + 
"(b('b2') <= 319.5) ? " + 
"-0.06971736979099848" + 
":  " + 
"-0.006528374834246682" + 
":  " + 
"(b('b4') <= 2032.5) ? " + 
"(b('b5') <= 3585.0) ? " + 
"0.00872471309999083" + 
":  " + 
"0.05527408109123168" + 
":  " + 
"(b('ndvi') <= 3466.0) ? " + 
"-0.003758777050304737" + 
":  " + 
"0.042516736028662044" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('urban') <= 3.522911548614502) ? " + 
"(b('moss') <= 0.06014965660870075) ? " + 
"-0.0035424082678659095" + 
":  " + 
"0.001824510470486478" + 
":  " + 
"(b('b11') <= 1902.0) ? " + 
"0.12745518310129908" + 
":  " + 
"0.1893740519191481" + 
":  " + 
"(b('moss') <= 8.992009162902832) ? " + 
"(b('b5') <= 2990.5) ? " + 
"-0.012864891415207868" + 
":  " + 
"0.002233683123132195" + 
":  " + 
"(b('bare') <= 2.0559067130088806) ? " + 
"0.02510029748357407" + 
":  " + 
"-0.0028962606793501875" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('ndvi') <= 1646.5) ? " + 
"(b('crop') <= 99.63687133789062) ? " + 
"-0.0035063980045766294" + 
":  " + 
"0.05153017854013311" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"0.00030161174332887184" + 
":  " + 
"0.024149502273811043" + 
":  " + 
"(b('b6') <= 3242.5) ? " + 
"(b('l8dt') <= 814990.0) ? " + 
"0.06650858917312345" + 
":  " + 
"0.0021225966678243835" + 
":  " + 
"(b('b6') <= 4360.0) ? " + 
"0.026607183149084022" + 
":  " + 
"0.006147884291700903" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 4392.5) ? " + 
"(b('b5') <= 4360.0) ? " + 
"-2.16367439809515e-05" + 
":  " + 
"0.07566025695933921" + 
":  " + 
"(b('b3') <= 1091.5) ? " + 
"-0.06030577930193329" + 
":  " + 
"-0.016296066245735683" + 
":  " + 
"(b('b3') <= 1098.5) ? " + 
"(b('l8dt') <= 1857353.5) ? " + 
"0.06911404784649369" + 
":  " + 
"-0.0029805491036430155" + 
":  " + 
"(b('ndvi') <= 2668.0) ? " + 
"-0.013252448067351917" + 
":  " + 
"0.006782734726157643" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 309.5) ? " + 
"(b('b5') <= 1477.5) ? " + 
"(b('l8dt') <= 650343.0) ? " + 
"0.027524189348785248" + 
":  " + 
"0.000842354882566726" + 
":  " + 
"(b('l8dt') <= 518406.0) ? " + 
"0.06772618285157792" + 
":  " + 
"0.13236663099056872" + 
":  " + 
"(b('b7') <= 536.0) ? " + 
"(b('b7') <= 478.5) ? " + 
"0.019484757585357868" + 
":  " + 
"-0.07355254399934179" + 
":  " + 
"(b('g0vv') <= -14.352240562438965) ? " + 
"-0.004259206971611089" + 
":  " + 
"0.000674780821661951" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -22.21730136871338) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"(b('b1') <= 361.0) ? " + 
"-0.047745095426311446" + 
":  " + 
"0.003091350057466453" + 
":  " + 
"(b('b4') <= 789.0) ? " + 
"0.09068664947504285" + 
":  " + 
"0.020956607589342372" + 
":  " + 
"(b('g0vv') <= -14.352240562438965) ? " + 
"(b('moss') <= 6.466630697250366) ? " + 
"-0.015192858857374167" + 
":  " + 
"-0.0011814818812330844" + 
":  " + 
"(b('crop') <= 2.4269771575927734) ? " + 
"-0.004043637428154916" + 
":  " + 
"0.0017255383864844469" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 33.82697677612305) ? " + 
"(b('grass') <= 98.52795028686523) ? " + 
"(b('lia') <= 31.64009666442871) ? " + 
"0.001701543998898733" + 
":  " + 
"-0.011038206366662926" + 
":  " + 
"(b('g0vh') <= -20.757600784301758) ? " + 
"0.03328472012446881" + 
":  " + 
"0.11565265496912398" + 
":  " + 
"(b('lia') <= 34.96310615539551) ? " + 
"(b('crop') <= 49.64166831970215) ? " + 
"0.00529187700535439" + 
":  " + 
"0.06477318879300266" + 
":  " + 
"(b('b3') <= 882.5) ? " + 
"-0.0030850836073230237" + 
":  " + 
"0.0023987181742764134" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 802.5) ? " + 
"(b('b2') <= 582.0) ? " + 
"(b('b1') <= 308.0) ? " + 
"-0.005514451791512183" + 
":  " + 
"0.07933687518175339" + 
":  " + 
"-0.10084619040737408" + 
":  " + 
"(b('l8dt') <= 169191.5) ? " + 
"(b('g0vh') <= -17.710686683654785) ? " + 
"-0.0005944675575243967" + 
":  " + 
"-0.010879524789858193" + 
":  " + 
"(b('l8dt') <= 174600.0) ? " + 
"0.025078082493101016" + 
":  " + 
"0.0003605509658337217" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5439.0) ? " + 
"(b('b1') <= 668.5) ? " + 
"(b('b4') <= 1281.5) ? " + 
"0.001046169494207145" + 
":  " + 
"-0.0049777703043806945" + 
":  " + 
"(b('b4') <= 2032.5) ? " + 
"0.009555139358812772" + 
":  " + 
"-0.0018706129141147687" + 
":  " + 
"(b('g0vh') <= -21.055819511413574) ? " + 
"(b('b6') <= 5508.5) ? " + 
"-0.023113855458398988" + 
":  " + 
"0.019275365187261993" + 
":  " + 
"(b('ndvi') <= 1282.0) ? " + 
"-0.014152274854237193" + 
":  " + 
"-0.04540096957214328" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -6.5169548988342285) ? " + 
"(b('lia') <= 33.46067810058594) ? " + 
"(b('grass') <= 79.13820266723633) ? " + 
"-0.005418348625066322" + 
":  " + 
"0.02032900724001542" + 
":  " + 
"(b('crop') <= 5.957038402557373) ? " + 
"-0.003142338904389937" + 
":  " + 
"0.002809278912210603" + 
":  " + 
"(b('trees') <= 11.961585998535156) ? " + 
"(b('b1') <= 172.5) ? " + 
"-0.07357832215397654" + 
":  " + 
"0.01949085423226504" + 
":  " + 
"(b('lia') <= 44.01340293884277) ? " + 
"-0.022790636150107114" + 
":  " + 
"-0.13641106613528792" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 23.278701782226562) ? " + 
"(b('urban') <= 14.72341012954712) ? " + 
"(b('crop') <= 28.176219940185547) ? " + 
"0.0025734454064616392" + 
":  " + 
"-0.0012192723123780203" + 
":  " + 
"(b('b6') <= 2987.5) ? " + 
"0.07665634317481523" + 
":  " + 
"0.005490056752194777" + 
":  " + 
"(b('ndvi') <= 714.5) ? " + 
"0.18991820663447118" + 
":  " + 
"(b('urban') <= 29.42727279663086) ? " + 
"-0.01806827131555562" + 
":  " + 
"-0.003390826834972004" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.928560256958008) ? " + 
"(b('b4') <= 633.5) ? " + 
"(b('b6') <= 1693.5) ? " + 
"0.024602863047767386" + 
":  " + 
"-0.054329638091081094" + 
":  " + 
"(b('g0vh') <= -21.629709243774414) ? " + 
"0.0025332262715372484" + 
":  " + 
"-0.011873143749189177" + 
":  " + 
"(b('b5') <= 1807.0) ? " + 
"(b('b4') <= 1157.0) ? " + 
"0.011062713813438478" + 
":  " + 
"-0.040461762674901036" + 
":  " + 
"(b('b2') <= 318.5) ? " + 
"0.012178065647207893" + 
":  " + 
"-0.0002711983784061734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 375.5) ? " + 
"(b('b6') <= 2714.0) ? " + 
"(b('b6') <= 2219.5) ? " + 
"-0.0010750356378668314" + 
":  " + 
"-0.022329768002182785" + 
":  " + 
"(b('crop') <= 23.834311485290527) ? " + 
"-0.1215797827207718" + 
":  " + 
"0.03390322007452008" + 
":  " + 
"(b('b3') <= 684.5) ? " + 
"(b('crop') <= 43.6307487487793) ? " + 
"0.024048917046075945" + 
":  " + 
"-0.009414809755492215" + 
":  " + 
"(b('b3') <= 727.5) ? " + 
"-0.012359624592715305" + 
":  " + 
"0.0004003235306614507" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -9.567953109741211) ? " + 
"(b('b1') <= 668.5) ? " + 
"(b('lia') <= 44.033355712890625) ? " + 
"-0.0024036317534541747" + 
":  " + 
"0.017316977498139388" + 
":  " + 
"(b('ndvi') <= 2198.5) ? " + 
"0.0013729922838364656" + 
":  " + 
"0.018102522746593044" + 
":  " + 
"(b('grass') <= 98.10429382324219) ? " + 
"(b('grass') <= 73.47041320800781) ? " + 
"0.002715290906834357" + 
":  " + 
"0.05272554859825362" + 
":  " + 
"(b('lia') <= 37.333478927612305) ? " + 
"0.19406872628568933" + 
":  " + 
"-0.060504186278008146" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 833.5) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"(b('grass') <= 44.375732421875) ? " + 
"-0.0017114713109719583" + 
":  " + 
"-0.06012166639950403" + 
":  " + 
"(b('crop') <= 23.048787117004395) ? " + 
"0.0028195496387312465" + 
":  " + 
"0.03828711499178865" + 
":  " + 
"(b('trees') <= 19.789812088012695) ? " + 
"(b('b3') <= 882.5) ? " + 
"-0.008599535518854671" + 
":  " + 
"0.00015330463349025542" + 
":  " + 
"(b('trees') <= 20.416804313659668) ? " + 
"0.06350315890737225" + 
":  " + 
"0.00476125610225148" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 364.5) ? " + 
"(b('b6') <= 2655.5) ? " + 
"(b('b10') <= 1136.5) ? " + 
"0.002244788692762369" + 
":  " + 
"-0.0230945270685228" + 
":  " + 
"(b('trees') <= 13.136719226837158) ? " + 
"0.0297321944130719" + 
":  " + 
"-0.08673586990300906" + 
":  " + 
"(b('b2') <= 366.5) ? " + 
"(b('b1') <= 262.0) ? " + 
"-0.018488133379102753" + 
":  " + 
"0.09607285004270433" + 
":  " + 
"(b('b1') <= 254.0) ? " + 
"-0.03319296576376832" + 
":  " + 
"0.0005605756239361499" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 41.29157829284668) ? " + 
"(b('lia') <= 38.43209266662598) ? " + 
"(b('lia') <= 37.33414840698242) ? " + 
"0.0002745644737998163" + 
":  " + 
"-0.012738953613190732" + 
":  " + 
"(b('lia') <= 38.853179931640625) ? " + 
"0.026390301731359356" + 
":  " + 
"0.002339064211703682" + 
":  " + 
"(b('l8dt') <= 2719.0) ? " + 
"(b('lia') <= 41.55661392211914) ? " + 
"0.15920982401394124" + 
":  " + 
"0.0508549127017948" + 
":  " + 
"(b('grass') <= 62.53530502319336) ? " + 
"-6.511098836004974e-06" + 
":  " + 
"-0.01338944188156571" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('ndvi') <= 1646.5) ? " + 
"(b('crop') <= 99.63687133789062) ? " + 
"-0.003193092427628415" + 
":  " + 
"0.045298648578087394" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"0.0002798862402973723" + 
":  " + 
"0.02203627682794214" + 
":  " + 
"(b('ndvi') <= 642.5) ? " + 
"(b('l8dt') <= 474963.5) ? " + 
"0.06293570106563119" + 
":  " + 
"0.11315642978403449" + 
":  " + 
"(b('b6') <= 4360.0) ? " + 
"0.027075311128108133" + 
":  " + 
"0.006702352826072456" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 87.20395278930664) ? " + 
"(b('g0vv') <= -15.837446689605713) ? " + 
"(b('b3') <= 798.5) ? " + 
"-0.041304630500013456" + 
":  " + 
"-0.003566226231476343" + 
":  " + 
"(b('b4') <= 796.5) ? " + 
"0.004228108306094489" + 
":  " + 
"-0.001139265392365663" + 
":  " + 
"(b('b1') <= 383.5) ? " + 
"(b('grass') <= 90.44964218139648) ? " + 
"0.02506023201439318" + 
":  " + 
"-0.03975966823960144" + 
":  " + 
"(b('b4') <= 734.5) ? " + 
"0.12150063487916518" + 
":  " + 
"0.010781197406448492" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.75) ? " + 
"(b('b1') <= 332.0) ? " + 
"(b('ndvi') <= 4709.0) ? " + 
"-0.0029488676492305556" + 
":  " + 
"-0.027293362611306656" + 
":  " + 
"(b('g0vv') <= -7.980203866958618) ? " + 
"0.04898832482288539" + 
":  " + 
"-0.09025158838551779" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('b6') <= 2346.0) ? " + 
"-0.006515551118122364" + 
":  " + 
"0.04944525530717259" + 
":  " + 
"(b('lia') <= 41.80293083190918) ? " + 
"0.001351874984578958" + 
":  " + 
"-0.003903125604569415" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 7.30760383605957) ? " + 
"(b('moss') <= 6.651747465133667) ? " + 
"-0.004044239416916257" + 
":  " + 
"-0.039959216832712335" + 
":  " + 
"(b('moss') <= 7.598436594009399) ? " + 
"0.06960225213384881" + 
":  " + 
"0.0031365759191294275" + 
":  " + 
"(b('moss') <= 7.337804079055786) ? " + 
"(b('grass') <= 7.583988189697266) ? " + 
"-0.0007195630881400178" + 
":  " + 
"0.01258357316947862" + 
":  " + 
"(b('moss') <= 9.604410648345947) ? " + 
"-0.009939426428035344" + 
":  " + 
"0.000621433315935749" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -8.636510848999023) ? " + 
"(b('g0vh') <= -15.125221252441406) ? " + 
"(b('grass') <= 87.20395278930664) ? " + 
"-0.001465721024522861" + 
":  " + 
"0.00672113496637966" + 
":  " + 
"(b('bare') <= 6.56046462059021) ? " + 
"0.016102371059527103" + 
":  " + 
"-0.03718118760605166" + 
":  " + 
"(b('crop') <= 68.24193572998047) ? " + 
"(b('b5') <= 3062.0) ? " + 
"-0.008217909086018826" + 
":  " + 
"0.015355261854286362" + 
":  " + 
"(b('crop') <= 76.28434753417969) ? " + 
"0.04921780788809742" + 
":  " + 
"0.006421299275544935" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2050.5) ? " + 
"(b('g0vv') <= -11.5765061378479) ? " + 
"(b('b1') <= 510.5) ? " + 
"-0.009768321933316542" + 
":  " + 
"0.009973860259810126" + 
":  " + 
"(b('bare') <= 0.17603477090597153) ? " + 
"-0.0007935669241524192" + 
":  " + 
"0.027385852092363213" + 
":  " + 
"(b('b2') <= 318.5) ? " + 
"(b('b2') <= 298.5) ? " + 
"-0.002627835410932477" + 
":  " + 
"0.030914437205648498" + 
":  " + 
"(b('b3') <= 580.0) ? " + 
"-0.042288218439125974" + 
":  " + 
"-0.0006275633946947273" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 4384.5) ? " + 
"(b('b5') <= 4376.5) ? " + 
"5.2499479355786085e-06" + 
":  " + 
"0.12959874872750138" + 
":  " + 
"(b('ndvi') <= 5095.5) ? " + 
"-0.015556240820291476" + 
":  " + 
"-0.0701739937246661" + 
":  " + 
"(b('b4') <= 1028.5) ? " + 
"(b('ndvi') <= 5908.5) ? " + 
"0.08007418740930856" + 
":  " + 
"0.018331182025769634" + 
":  " + 
"(b('lia') <= 43.036725997924805) ? " + 
"-0.005828098914693013" + 
":  " + 
"-0.027036901265161874" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 24.395869255065918) ? " + 
"(b('b3') <= 944.0) ? " + 
"(b('b10') <= 2411.5) ? " + 
"0.16698062629996102" + 
":  " + 
"0.2140818843167821" + 
":  " + 
"(b('g0vv') <= -14.644976615905762) ? " + 
"0.01694264291823083" + 
":  " + 
"-0.013664373180334097" + 
":  " + 
"(b('g0vv') <= -12.017068862915039) ? " + 
"(b('ndvi') <= 5653.5) ? " + 
"-0.002215219035802994" + 
":  " + 
"0.022075379606986346" + 
":  " + 
"(b('grass') <= 30.423192024230957) ? " + 
"-0.0007855300891331102" + 
":  " + 
"0.007454720209259745" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b6') <= 1842.5) ? " + 
"(b('b6') <= 1753.0) ? " + 
"-0.002830878120336292" + 
":  " + 
"0.048011234625495475" + 
":  " + 
"(b('b11') <= 1726.0) ? " + 
"-0.01099557746834117" + 
":  " + 
"0.005412806522899078" + 
":  " + 
"(b('crop') <= 95.60836410522461) ? " + 
"(b('crop') <= 94.68265533447266) ? " + 
"-0.0006673750123396819" + 
":  " + 
"0.08028357113769555" + 
":  " + 
"(b('g0vv') <= -9.435036182403564) ? " + 
"0.003523130614430024" + 
":  " + 
"-0.06895680150843637" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 364.5) ? " + 
"(b('trees') <= 13.24367094039917) ? " + 
"(b('b6') <= 2655.5) ? " + 
"-0.004139812790581509" + 
":  " + 
"0.026120492776530512" + 
":  " + 
"(b('b6') <= 2136.5) ? " + 
"0.004358845703222667" + 
":  " + 
"-0.042157978811038624" + 
":  " + 
"(b('b2') <= 366.5) ? " + 
"(b('b1') <= 262.0) ? " + 
"-0.017916441906430804" + 
":  " + 
"0.08438718133164164" + 
":  " + 
"(b('b1') <= 254.0) ? " + 
"-0.029856722453353978" + 
":  " + 
"0.0005063025908483548" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 5.957038402557373) ? " + 
"(b('g0vh') <= -20.146995544433594) ? " + 
"(b('ndvi') <= 2179.5) ? " + 
"-0.0025793139354417854" + 
":  " + 
"0.01706058605023483" + 
":  " + 
"(b('moss') <= 12.706889152526855) ? " + 
"-0.0017578833779190593" + 
":  " + 
"-0.016840831593751625" + 
":  " + 
"(b('crop') <= 28.176219940185547) ? " + 
"(b('urban') <= 0.5) ? " + 
"0.028092680055989735" + 
":  " + 
"-0.010224175958237217" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.00015344675558728367" + 
":  " + 
"-0.042787325108455045" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.75) ? " + 
"(b('g0vv') <= -15.815475940704346) ? " + 
"(b('crop') <= 2.995652198791504) ? " + 
"0.009536049170722649" + 
":  " + 
"-0.08207593404633427" + 
":  " + 
"(b('b4') <= 616.0) ? " + 
"0.005708997462380512" + 
":  " + 
"-0.009976018815866995" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('b5') <= 2366.0) ? " + 
"-0.020361511185663924" + 
":  " + 
"0.03830657577189571" + 
":  " + 
"(b('b4') <= 614.0) ? " + 
"-0.021280948412977053" + 
":  " + 
"0.0003374281533640901" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -8.636510848999023) ? " + 
"(b('lia') <= 34.56068420410156) ? " + 
"(b('grass') <= 98.52795028686523) ? " + 
"-0.004469017226348826" + 
":  " + 
"0.027524873136680512" + 
":  " + 
"(b('lia') <= 34.79923439025879) ? " + 
"0.03250026191091971" + 
":  " + 
"8.517930931698525e-05" + 
":  " + 
"(b('grass') <= 98.10429382324219) ? " + 
"(b('grass') <= 73.52653503417969) ? " + 
"0.0035848433842480595" + 
":  " + 
"0.08996557998051018" + 
":  " + 
"(b('b4') <= 1430.5) ? " + 
"-0.07018755965641897" + 
":  " + 
"0.17437013812630597" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('b2') <= 912.5) ? " + 
"-0.00340990084229101" + 
":  " + 
"0.008955312492898198" + 
":  " + 
"(b('b10') <= 2383.0) ? " + 
"0.029261706132700665" + 
":  " + 
"0.10241637169671072" + 
":  " + 
"(b('moss') <= 7.337804079055786) ? " + 
"(b('moss') <= 0.4266425520181656) ? " + 
"-0.0010018113768724252" + 
":  " + 
"0.01109236853526681" + 
":  " + 
"(b('g0vh') <= -19.82557487487793) ? " + 
"0.003636924341330787" + 
":  " + 
"-0.0057884203856288395" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('crop') <= 66.14077377319336) ? " + 
"(b('crop') <= 62.66942024230957) ? " + 
"0.0003710954041384176" + 
":  " + 
"-0.014458444425803931" + 
":  " + 
"(b('crop') <= 66.92900466918945) ? " + 
"0.04505529152445135" + 
":  " + 
"0.002380950775200274" + 
":  " + 
"(b('b5') <= 3525.5) ? " + 
"(b('moss') <= 4.337218999862671) ? " + 
"-0.07999258018548655" + 
":  " + 
"0.006442037159007201" + 
":  " + 
"(b('b1') <= 589.5) ? " + 
"-0.00835256894064717" + 
":  " + 
"0.0045158176152251825" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.928560256958008) ? " + 
"(b('trees') <= 0.03652967885136604) ? " + 
"(b('moss') <= 7.53682541847229) ? " + 
"-0.0053034130031797185" + 
":  " + 
"0.011030699250791604" + 
":  " + 
"(b('g0vh') <= -23.51975440979004) ? " + 
"0.23948819387047798" + 
":  " + 
"-0.014523723936046501" + 
":  " + 
"(b('ndvi') <= 4749.5) ? " + 
"(b('ndvi') <= 3972.0) ? " + 
"0.00019716014622112615" + 
":  " + 
"0.008916467627883493" + 
":  " + 
"(b('b2') <= 288.5) ? " + 
"-0.07186156040599714" + 
":  " + 
"-0.0036271182353674798" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 5.957038402557373) ? " + 
"(b('ndvi') <= 3524.5) ? " + 
"(b('b1') <= 420.5) ? " + 
"-0.015354116655112035" + 
":  " + 
"-0.0008585721101705845" + 
":  " + 
"(b('grass') <= 81.45600891113281) ? " + 
"0.0045559506525739354" + 
":  " + 
"0.05008399065813174" + 
":  " + 
"(b('crop') <= 28.176219940185547) ? " + 
"(b('urban') <= 0.5) ? " + 
"0.02543022630776226" + 
":  " + 
"-0.009079998973888599" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.00020381538383377906" + 
":  " + 
"-0.03786652963128922" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2050.5) ? " + 
"(b('b3') <= 1102.5) ? " + 
"(b('b4') <= 1172.5) ? " + 
"0.005631918548256888" + 
":  " + 
"-0.017628941058876555" + 
":  " + 
"(b('b6') <= 2239.0) ? " + 
"-0.02668880013561853" + 
":  " + 
"0.05284857168956033" + 
":  " + 
"(b('b2') <= 318.5) ? " + 
"(b('trees') <= 13.24367094039917) ? " + 
"0.022624211652222895" + 
":  " + 
"-0.009988234158754437" + 
":  " + 
"(b('b2') <= 347.5) ? " + 
"-0.01985766578873628" + 
":  " + 
"-0.0003236328840457977" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.75) ? " + 
"(b('g0vv') <= -13.47429084777832) ? " + 
"(b('b2') <= 258.0) ? " + 
"0.037394657947756565" + 
":  " + 
"-0.030164954452487857" + 
":  " + 
"(b('grass') <= 46.00799369812012) ? " + 
"-0.006639512991069508" + 
":  " + 
"0.007244468163622458" + 
":  " + 
"(b('b1') <= 299.5) ? " + 
"(b('grass') <= 50.46322441101074) ? " + 
"0.003251199769305902" + 
":  " + 
"0.059367170482729034" + 
":  " + 
"(b('b1') <= 311.5) ? " + 
"-0.012121878788965468" + 
":  " + 
"0.00025105217317795573" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -10.227709770202637) ? " + 
"(b('b2') <= 377.5) ? " + 
"(b('ndvi') <= 2940.0) ? " + 
"0.005563770623955694" + 
":  " + 
"-0.01598645287648419" + 
":  " + 
"(b('b4') <= 743.5) ? " + 
"0.008435173178526986" + 
":  " + 
"-0.0011757940329459645" + 
":  " + 
"(b('grass') <= 34.49201011657715) ? " + 
"(b('b7') <= 1380.5) ? " + 
"0.010460305120762523" + 
":  " + 
"-0.0016115821484737607" + 
":  " + 
"(b('crop') <= 40.340951919555664) ? " + 
"0.005846068846211373" + 
":  " + 
"0.048147267287169365" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 882.5) ? " + 
"(b('b6') <= 3232.0) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"-0.004052657223460511" + 
":  " + 
"0.004037478881823654" + 
":  " + 
"(b('crop') <= 5.668789803981781) ? " + 
"-0.01071191647912818" + 
":  " + 
"-0.057609793140723266" + 
":  " + 
"(b('b4') <= 941.0) ? " + 
"(b('bare') <= 4.077777862548828) ? " + 
"0.03565005899229337" + 
":  " + 
"0.001169011374055914" + 
":  " + 
"(b('trees') <= 19.831669807434082) ? " + 
"-0.0002792622239036039" + 
":  " + 
"0.019744312910677797" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 23.881052017211914) ? " + 
"(b('grass') <= 23.130656242370605) ? " + 
"(b('trees') <= 14.932132720947266) ? " + 
"-0.0009208001306719507" + 
":  " + 
"0.017421911517511397" + 
":  " + 
"(b('b11') <= 2000.0) ? " + 
"0.02471246451890373" + 
":  " + 
"0.07595822276216489" + 
":  " + 
"(b('crop') <= 57.51982307434082) ? " + 
"(b('crop') <= 55.69375419616699) ? " + 
"-0.00015115197953349905" + 
":  " + 
"0.07648563398355192" + 
":  " + 
"(b('b2') <= 520.5) ? " + 
"-0.04374167547346767" + 
":  " + 
"-0.008853616376313026" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('crop') <= 5.957038402557373) ? " + 
"(b('g0vh') <= -18.439754486083984) ? " + 
"-0.00021951718877102167" + 
":  " + 
"-0.013821990232323238" + 
":  " + 
"(b('grass') <= 64.32077598571777) ? " + 
"0.0011105250815254403" + 
":  " + 
"0.027205963448698554" + 
":  " + 
"(b('b1') <= 589.5) ? " + 
"(b('b4') <= 943.0) ? " + 
"0.003940484856682288" + 
":  " + 
"-0.021668467099146615" + 
":  " + 
"(b('b6') <= 3103.5) ? " + 
"0.06905365367743033" + 
":  " + 
"0.00186614245389867" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -11.894443035125732) ? " + 
"(b('lia') <= 34.08219528198242) ? " + 
"(b('lia') <= 31.970730781555176) ? " + 
"0.00444886019277345" + 
":  " + 
"-0.0234501630971679" + 
":  " + 
"(b('lia') <= 34.79923439025879) ? " + 
"0.02036642679948909" + 
":  " + 
"-0.0011066760407148787" + 
":  " + 
"(b('ndvi') <= 4686.5) ? " + 
"(b('moss') <= 1.940559446811676) ? " + 
"0.00885997491057437" + 
":  " + 
"0.00026734217925582617" + 
":  " + 
"(b('grass') <= 46.00799369812012) ? " + 
"-0.013259471812240615" + 
":  " + 
"0.039436494452968776" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5439.0) ? " + 
"(b('b5') <= 2050.5) ? " + 
"(b('b3') <= 558.5) ? " + 
"-0.013280849856274498" + 
":  " + 
"0.006231610524111374" + 
":  " + 
"(b('b5') <= 2321.5) ? " + 
"-0.004806341664756893" + 
":  " + 
"0.00022841301907411234" + 
":  " + 
"(b('ndvi') <= 1593.0) ? " + 
"(b('ndvi') <= 1282.0) ? " + 
"-0.00952788450846774" + 
":  " + 
"-0.042916079087329355" + 
":  " + 
"(b('l8dt') <= 518400.5) ? " + 
"0.028432852114877255" + 
":  " + 
"0.002149325999484364" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -8.636510848999023) ? " + 
"(b('g0vh') <= -15.125221252441406) ? " + 
"(b('grass') <= 87.20395278930664) ? " + 
"-0.0012819214987417715" + 
":  " + 
"0.005971789795401337" + 
":  " + 
"(b('bare') <= 6.56046462059021) ? " + 
"0.014027883131282807" + 
":  " + 
"-0.03146890542757946" + 
":  " + 
"(b('grass') <= 98.10429382324219) ? " + 
"(b('grass') <= 73.52653503417969) ? " + 
"0.003425346696246745" + 
":  " + 
"0.08051861469296696" + 
":  " + 
"(b('b2') <= 891.0) ? " + 
"-0.06258551381796139" + 
":  " + 
"0.15600567755744352" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.928560256958008) ? " + 
"(b('b1') <= 449.5) ? " + 
"(b('crop') <= 82.21492767333984) ? " + 
"-0.014947663415312043" + 
":  " + 
"0.08168187414517086" + 
":  " + 
"(b('b4') <= 1055.0) ? " + 
"0.016295298695828207" + 
":  " + 
"-0.0030886994572217655" + 
":  " + 
"(b('lia') <= 24.252931594848633) ? " + 
"0.18817765569124859" + 
":  " + 
"(b('b5') <= 1807.0) ? " + 
"0.007186831356097636" + 
":  " + 
"6.0914339153856515e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 882.5) ? " + 
"(b('b6') <= 3228.5) ? " + 
"(b('trees') <= 19.15903377532959) ? " + 
"0.0004630592738124642" + 
":  " + 
"-0.012085574381040801" + 
":  " + 
"(b('bare') <= 5.332393407821655) ? " + 
"-0.045732723128583376" + 
":  " + 
"0.0007692199930945027" + 
":  " + 
"(b('b4') <= 1135.5) ? " + 
"(b('ndvi') <= 1780.5) ? " + 
"0.040484654821905094" + 
":  " + 
"0.007056903383455375" + 
":  " + 
"(b('b3') <= 959.5) ? " + 
"-0.01609501641138943" + 
":  " + 
"0.0003441450229688302" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('ndvi') <= 1646.5) ? " + 
"(b('crop') <= 99.63687133789062) ? " + 
"-0.002788078475758585" + 
":  " + 
"0.03973039275429325" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"0.00022931263325524234" + 
":  " + 
"0.01952191756971006" + 
":  " + 
"(b('b6') <= 3242.5) ? " + 
"(b('l8dt') <= 814990.0) ? " + 
"0.056359553275079646" + 
":  " + 
"0.001132612058872301" + 
":  " + 
"(b('l8dt') <= 734873.0) ? " + 
"0.01304543329218454" + 
":  " + 
"0.053401659997848176" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 23.28085994720459) ? " + 
"(b('trees') <= 17.472150802612305) ? " + 
"-0.00028543335610955653" + 
":  " + 
"0.007378963897270408" + 
":  " + 
"(b('moss') <= 2.1891891956329346) ? " + 
"-0.09201109617741446" + 
":  " + 
"-0.010491818429421651" + 
":  " + 
"(b('trees') <= 49.7714729309082) ? " + 
"(b('b5') <= 2661.0) ? " + 
"0.016417182452159527" + 
":  " + 
"0.08047232634577874" + 
":  " + 
"(b('l8dt') <= 345600.5) ? " + 
"-0.051509872064022605" + 
":  " + 
"-0.02148991997530368" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 816.5) ? " + 
"(b('b6') <= 3020.0) ? " + 
"(b('moss') <= 0.905249685049057) ? " + 
"-0.008936527075181553" + 
":  " + 
"0.0016575810389889117" + 
":  " + 
"(b('g0vv') <= -8.34486436843872) ? " + 
"-0.028868799545266843" + 
":  " + 
"0.22129340824013397" + 
":  " + 
"(b('b4') <= 823.5) ? " + 
"(b('b10') <= 1702.5) ? " + 
"0.015541984155858253" + 
":  " + 
"0.0677373395941024" + 
":  " + 
"(b('b11') <= 1332.5) ? " + 
"0.02696485586187534" + 
":  " + 
"-7.012338912317362e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('crop') <= 5.957038402557373) ? " + 
"(b('g0vh') <= -19.415958404541016) ? " + 
"0.000769376007815033" + 
":  " + 
"-0.009378128391029266" + 
":  " + 
"(b('grass') <= 64.32077598571777) ? " + 
"0.0010093394234628717" + 
":  " + 
"0.024886621121857796" + 
":  " + 
"(b('b1') <= 589.5) ? " + 
"(b('b4') <= 943.0) ? " + 
"0.0026782543831355738" + 
":  " + 
"-0.019690493387327885" + 
":  " + 
"(b('ndvi') <= 3113.0) ? " + 
"-0.0003979457822860644" + 
":  " + 
"0.03288828874355895" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 882.5) ? " + 
"(b('b6') <= 3228.5) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"-0.0038884856710910904" + 
":  " + 
"0.003627695929734388" + 
":  " + 
"(b('b4') <= 1067.0) ? " + 
"-0.04976637618197677" + 
":  " + 
"-0.012583436855657184" + 
":  " + 
"(b('b4') <= 1049.5) ? " + 
"(b('bare') <= 9.690493106842041) ? " + 
"0.009391894355782453" + 
":  " + 
"0.06647319209297725" + 
":  " + 
"(b('trees') <= 19.831669807434082) ? " + 
"-0.0006349538053390892" + 
":  " + 
"0.020385197746882144" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 62.53530502319336) ? " + 
"(b('grass') <= 46.57049369812012) ? " + 
"(b('grass') <= 42.47282409667969) ? " + 
"0.0003347006052585185" + 
":  " + 
"-0.018416599521973064" + 
":  " + 
"(b('b4') <= 927.5) ? " + 
"0.027368269135663256" + 
":  " + 
"-0.0076695153046214175" + 
":  " + 
"(b('crop') <= 35.33369064331055) ? " + 
"(b('crop') <= 5.957038402557373) ? " + 
"-0.0019623279773718443" + 
":  " + 
"0.017986692799266606" + 
":  " + 
"(b('g0vv') <= -12.970137119293213) ? " + 
"-0.03979548706447371" + 
":  " + 
"-0.07002826091525993" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 354.5) ? " + 
"(b('trees') <= 13.24367094039917) ? " + 
"(b('crop') <= 50.93680191040039) ? " + 
"0.008085294952205824" + 
":  " + 
"-0.013237157108419474" + 
":  " + 
"(b('b10') <= 1145.0) ? " + 
"0.0011006986914567753" + 
":  " + 
"-0.05096256858265425" + 
":  " + 
"(b('b1') <= 254.5) ? " + 
"(b('b4') <= 727.5) ? " + 
"0.009054391674796197" + 
":  " + 
"-0.03488422831362654" + 
":  " + 
"(b('b1') <= 270.5) ? " + 
"0.022252506836720844" + 
":  " + 
"0.000374102691256266" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.75) ? " + 
"(b('b4') <= 616.0) ? " + 
"(b('crop') <= 94.68265533447266) ? " + 
"0.0012592576479637685" + 
":  " + 
"0.06418153623187062" + 
":  " + 
"(b('crop') <= 11.22841739654541) ? " + 
"-0.03598859559632644" + 
":  " + 
"-0.006446584209216308" + 
":  " + 
"(b('b1') <= 299.5) ? " + 
"(b('grass') <= 50.46322441101074) ? " + 
"0.0025395084858745587" + 
":  " + 
"0.05013704136662905" + 
":  " + 
"(b('b1') <= 311.5) ? " + 
"-0.011621255672456737" + 
":  " + 
"0.0003276790236370978" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.869969367980957) ? " + 
"(b('trees') <= 7.314132928848267) ? " + 
"(b('urban') <= 0.4475524425506592) ? " + 
"0.0001872789524681735" + 
":  " + 
"-0.05895566456727449" + 
":  " + 
"(b('b3') <= 566.0) ? " + 
"-0.09224052167811045" + 
":  " + 
"-0.023999883014854066" + 
":  " + 
"(b('g0vv') <= -15.865667343139648) ? " + 
"(b('b1') <= 485.5) ? " + 
"0.21350643999436222" + 
":  " + 
"0.05546172922915093" + 
":  " + 
"(b('g0vh') <= -22.223341941833496) ? " + 
"0.007090589396318171" + 
":  " + 
"-4.224258048658781e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 23.046470642089844) ? " + 
"(b('trees') <= 17.472150802612305) ? " + 
"-0.00024811659432269397" + 
":  " + 
"0.006645650694075972" + 
":  " + 
"(b('ndvi') <= 1548.5) ? " + 
"0.21953926141757052" + 
":  " + 
"-0.012850355110410777" + 
":  " + 
"(b('moss') <= 5.756144165992737) ? " + 
"(b('b1') <= 464.0) ? " + 
"0.04440992157641178" + 
":  " + 
"-0.059568802852985894" + 
":  " + 
"(b('g0vh') <= -17.867287635803223) ? " + 
"-0.0494349373413254" + 
":  " + 
"-0.024031633083197546" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 882.5) ? " + 
"(b('b6') <= 3228.5) ? " + 
"(b('moss') <= 13.232231140136719) ? " + 
"0.0006471246415128243" + 
":  " + 
"-0.009952682296310758" + 
":  " + 
"(b('bare') <= 5.332393407821655) ? " + 
"-0.03691619631876133" + 
":  " + 
"0.002623705450033829" + 
":  " + 
"(b('b6') <= 2605.0) ? " + 
"(b('bare') <= 16.017282009124756) ? " + 
"0.013776783042559618" + 
":  " + 
"-0.022590486436079422" + 
":  " + 
"(b('b5') <= 1912.5) ? " + 
"0.028882415487372633" + 
":  " + 
"-0.0002615173257383576" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('crop') <= 66.14077377319336) ? " + 
"(b('crop') <= 65.46904754638672) ? " + 
"0.00013907074766271444" + 
":  " + 
"-0.01538311121613183" + 
":  " + 
"(b('crop') <= 76.58172988891602) ? " + 
"0.017265887633769506" + 
":  " + 
"0.00014264459006101138" + 
":  " + 
"(b('b5') <= 3525.5) ? " + 
"(b('ndvi') <= 4326.0) ? " + 
"-0.055076232459954674" + 
":  " + 
"0.08177292253119457" + 
":  " + 
"(b('bare') <= 4.077777862548828) ? " + 
"0.0015091128510071094" + 
":  " + 
"-0.010544915736101506" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 899.5) ? " + 
"(b('b1') <= 783.75) ? " + 
"(b('b5') <= 3381.5) ? " + 
"0.0003963830517627515" + 
":  " + 
"-0.005752773397917299" + 
":  " + 
"(b('b3') <= 1089.5) ? " + 
"-0.08975218486933985" + 
":  " + 
"-0.020427395534486203" + 
":  " + 
"(b('b4') <= 2028.5) ? " + 
"(b('bare') <= 0.35301104187965393) ? " + 
"0.0325610945050816" + 
":  " + 
"0.0026341072412550052" + 
":  " + 
"(b('trees') <= 11.00907564163208) ? " + 
"-0.0029216706583245567" + 
":  " + 
"0.03408232729055236" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('trees') <= 10.145288467407227) ? " + 
"-0.0038840394869227315" + 
":  " + 
"0.00390539909125952" + 
":  " + 
"(b('b10') <= 2383.0) ? " + 
"0.025414983981209473" + 
":  " + 
"0.0910333020183737" + 
":  " + 
"(b('bare') <= 0.3734448403120041) ? " + 
"(b('b6') <= 2895.0) ? " + 
"0.013567219426056747" + 
":  " + 
"0.07165230703304905" + 
":  " + 
"(b('b4') <= 787.0) ? " + 
"0.009669524989764179" + 
":  " + 
"-0.0007199747685839378" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 770.5) ? " + 
"(b('b5') <= 3163.0) ? " + 
"(b('b5') <= 3145.0) ? " + 
"-0.0011879538553333463" + 
":  " + 
"0.06033445740506139" + 
":  " + 
"(b('b3') <= 624.5) ? " + 
"0.08733547741498078" + 
":  " + 
"-0.018683382726396858" + 
":  " + 
"(b('b4') <= 835.5) ? " + 
"(b('b3') <= 772.5) ? " + 
"0.06800281467410978" + 
":  " + 
"0.008291271158293666" + 
":  " + 
"(b('b3') <= 892.25) ? " + 
"-0.005204863343590019" + 
":  " + 
"0.0009859981448015463" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 2907.5) ? " + 
"(b('b11') <= 2889.5) ? " + 
"(b('bare') <= 14.846899032592773) ? " + 
"3.9093796680476655e-05" + 
":  " + 
"-0.010228751710591876" + 
":  " + 
"(b('grass') <= 65.18574714660645) ? " + 
"-0.04555825670721195" + 
":  " + 
"0.014827973283079306" + 
":  " + 
"(b('b7') <= 2910.0) ? " + 
"(b('ndvi') <= 1344.0) ? " + 
"0.08660625242344673" + 
":  " + 
"0.013238271733807597" + 
":  " + 
"(b('ndvi') <= 3015.5) ? " + 
"0.0011258044032558465" + 
":  " + 
"0.01937570917368705" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 9.947502613067627) ? " + 
"(b('bare') <= 9.127102851867676) ? " + 
"(b('b5') <= 2172.5) ? " + 
"0.004013242931102711" + 
":  " + 
"-0.0009754609470707001" + 
":  " + 
"(b('lia') <= 30.104607582092285) ? " + 
"0.13728009557278537" + 
":  " + 
"-0.02628062183666406" + 
":  " + 
"(b('bare') <= 13.728639125823975) ? " + 
"(b('g0vv') <= -11.941830158233643) ? " + 
"0.009338058018817538" + 
":  " + 
"0.06200712399057325" + 
":  " + 
"(b('b5') <= 2781.5) ? " + 
"-0.010005651378859608" + 
":  " + 
"0.007418054627253021" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.054420948028564) ? " + 
"(b('b1') <= 444.5) ? " + 
"(b('b6') <= 2517.0) ? " + 
"0.004936358655981528" + 
":  " + 
"-0.0188518722140031" + 
":  " + 
"(b('b4') <= 1100.5) ? " + 
"0.01276866984342708" + 
":  " + 
"-0.0021430498693051844" + 
":  " + 
"(b('lia') <= 24.395869255065918) ? " + 
"(b('b10') <= 2621.5) ? " + 
"0.1489239479255329" + 
":  " + 
"-0.02423688935683574" + 
":  " + 
"(b('lia') <= 29.347232818603516) ? " + 
"-0.009094441815110892" + 
":  " + 
"0.0008582269209489869" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.75) ? " + 
"(b('g0vv') <= -15.815475940704346) ? " + 
"(b('b6') <= 1693.5) ? " + 
"0.0420127534932929" + 
":  " + 
"-0.060767125734988214" + 
":  " + 
"(b('b4') <= 616.0) ? " + 
"0.004318633421060144" + 
":  " + 
"-0.008161180151501933" + 
":  " + 
"(b('b2') <= 391.5) ? " + 
"(b('grass') <= 59.600934982299805) ? " + 
"0.022570678800050578" + 
":  " + 
"-0.034087816850878784" + 
":  " + 
"(b('b4') <= 614.0) ? " + 
"-0.021862224256037944" + 
":  " + 
"0.0003310710347064004" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 4691.5) ? " + 
"(b('ndvi') <= 4402.0) ? " + 
"(b('ndvi') <= 4397.0) ? " + 
"3.8891833965091196e-05" + 
":  " + 
"-0.08814787981758908" + 
":  " + 
"(b('grass') <= 81.44424438476562) ? " + 
"0.009271110469221626" + 
":  " + 
"0.108049055654874" + 
":  " + 
"(b('crop') <= 88.85982513427734) ? " + 
"(b('b2') <= 288.5) ? " + 
"-0.06925216263663989" + 
":  " + 
"0.0007659339718801247" + 
":  " + 
"(b('ndvi') <= 6535.5) ? " + 
"-0.042346573274982" + 
":  " + 
"0.027398161228536725" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 9.947502613067627) ? " + 
"(b('bare') <= 9.127102851867676) ? " + 
"(b('moss') <= 22.977157592773438) ? " + 
"-0.0003578326247990038" + 
":  " + 
"0.015551532959362969" + 
":  " + 
"(b('g0vv') <= -11.232815742492676) ? " + 
"-0.027490132774860884" + 
":  " + 
"0.009120440262306592" + 
":  " + 
"(b('bare') <= 13.728639125823975) ? " + 
"(b('g0vv') <= -11.941830158233643) ? " + 
"0.008383039250498546" + 
":  " + 
"0.05566221555982739" + 
":  " + 
"(b('b4') <= 760.5) ? " + 
"0.058854831211250624" + 
":  " + 
"-0.0025304765366274424" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('grass') <= 87.20395278930664) ? " + 
"(b('grass') <= 80.30580139160156) ? " + 
"0.0001357979679518245" + 
":  " + 
"-0.009699226704680552" + 
":  " + 
"(b('moss') <= 12.59807300567627) ? " + 
"-0.00013053333823908684" + 
":  " + 
"0.04007684223055529" + 
":  " + 
"(b('b5') <= 2913.5) ? " + 
"(b('l8dt') <= 814990.0) ? " + 
"0.04843850049634531" + 
":  " + 
"-0.0023146051446169685" + 
":  " + 
"(b('l8dt') <= 734873.0) ? " + 
"0.011661989271109655" + 
":  " + 
"0.04795769090460169" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -2.327260732650757) ? " + 
"(b('g0vv') <= -6.5169548988342285) ? " + 
"(b('lia') <= 38.018537521362305) ? " + 
"-0.0017252687225409074" + 
":  " + 
"0.0011511595082579023" + 
":  " + 
"(b('trees') <= 11.961585998535156) ? " + 
"0.014708061776431578" + 
":  " + 
"-0.022157128218350752" + 
":  " + 
"(b('b6') <= 2919.0) ? " + 
"(b('lia') <= 35.77733898162842) ? " + 
"-0.07739454887350164" + 
":  " + 
"-0.07902093400041313" + 
":  " + 
"(b('g0vh') <= -15.40637493133545) ? " + 
"-0.03982155649442196" + 
":  " + 
"-0.05185467195654936" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 816.5) ? " + 
"(b('b2') <= 488.5) ? " + 
"(b('grass') <= 99.8344841003418) ? " + 
"0.0012903002104358932" + 
":  " + 
"-0.031376468838897914" + 
":  " + 
"(b('ndvi') <= 4829.5) ? " + 
"-0.007396957027102644" + 
":  " + 
"-0.060687345437507076" + 
":  " + 
"(b('b4') <= 823.5) ? " + 
"(b('moss') <= 1.750055193901062) ? " + 
"0.03902019609814243" + 
":  " + 
"0.007152455009277221" + 
":  " + 
"(b('b10') <= 1651.5) ? " + 
"-0.007955550214708056" + 
":  " + 
"0.0009646313720478091" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('urban') <= 3.522911548614502) ? " + 
"(b('g0vv') <= -8.902799606323242) ? " + 
"-0.0002113903941580305" + 
":  " + 
"0.005864367822142346" + 
":  " + 
"(b('b2') <= 571.5) ? " + 
"0.11397932811820213" + 
":  " + 
"0.16859912393252843" + 
":  " + 
"(b('b5') <= 4200.0) ? " + 
"(b('trees') <= 11.409454822540283) ? " + 
"-0.0014437577206374123" + 
":  " + 
"-0.013324173167703185" + 
":  " + 
"(b('bare') <= 3.40365070104599) ? " + 
"0.14022692222155342" + 
":  " + 
"0.03136250799715824" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 87.20395278930664) ? " + 
"(b('grass') <= 80.30580139160156) ? " + 
"(b('grass') <= 78.23077011108398) ? " + 
"-0.00032871480829656794" + 
":  " + 
"0.039243549868106936" + 
":  " + 
"(b('bare') <= 2.6389132738113403) ? " + 
"-0.024493069890521146" + 
":  " + 
"0.0029309575019641357" + 
":  " + 
"(b('lia') <= 31.920825004577637) ? " + 
"(b('b5') <= 2397.0) ? " + 
"0.11243558202460625" + 
":  " + 
"0.03855607474836287" + 
":  " + 
"(b('grass') <= 87.40192794799805) ? " + 
"0.03626114461263171" + 
":  " + 
"-0.0033889568720714284" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.928560256958008) ? " + 
"(b('b4') <= 642.0) ? " + 
"(b('b6') <= 1974.5) ? " + 
"0.011863564188709833" + 
":  " + 
"-0.04359801685120417" + 
":  " + 
"(b('ndvi') <= 4859.5) ? " + 
"-0.003578123235622704" + 
":  " + 
"0.03435843673301365" + 
":  " + 
"(b('ndvi') <= 4640.0) ? " + 
"(b('b6') <= 2217.5) ? " + 
"0.006655804650359325" + 
":  " + 
"4.22658145623096e-05" + 
":  " + 
"(b('moss') <= 1.398017704486847) ? " + 
"-0.014535596157873712" + 
":  " + 
"0.002447100803130467" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 347.5) ? " + 
"(b('b1') <= 256.5) ? " + 
"(b('b4') <= 732.0) ? " + 
"0.003960202745801052" + 
":  " + 
"-0.020936818386004093" + 
":  " + 
"(b('b5') <= 2751.5) ? " + 
"-0.005627901784465275" + 
":  " + 
"-0.05159313979000424" + 
":  " + 
"(b('b1') <= 255.5) ? " + 
"(b('b2') <= 349.5) ? " + 
"0.06453034532627747" + 
":  " + 
"-0.022801930145376854" + 
":  " + 
"(b('b1') <= 278.5) ? " + 
"0.016278120131349657" + 
":  " + 
"0.000200664933739599" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5439.0) ? " + 
"(b('b7') <= 3248.5) ? " + 
"(b('g0vv') <= -10.71688175201416) ? " + 
"-0.0014677319023730026" + 
":  " + 
"0.001849535608764865" + 
":  " + 
"(b('b5') <= 2881.0) ? " + 
"0.024845065252804926" + 
":  " + 
"0.0026349360735604334" + 
":  " + 
"(b('g0vh') <= -21.055819511413574) ? " + 
"(b('moss') <= 12.5) ? " + 
"0.017383302748484125" + 
":  " + 
"-0.016383859217876467" + 
":  " + 
"(b('ndvi') <= 1282.0) ? " + 
"-0.010728461427687505" + 
":  " + 
"-0.03546277346936097" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2160.5) ? " + 
"(b('b5') <= 2153.5) ? " + 
"(b('grass') <= 23.696155548095703) ? " + 
"0.008086493540090715" + 
":  " + 
"-0.0020265214498447312" + 
":  " + 
"(b('b11') <= 1788.0) ? " + 
"0.1281811024125032" + 
":  " + 
"0.008972799944389048" + 
":  " + 
"(b('b5') <= 2321.5) ? " + 
"(b('l8dt') <= 2721.0) ? " + 
"0.08225209259655834" + 
":  " + 
"-0.008053637472840078" + 
":  " + 
"(b('grass') <= 35.85540008544922) ? " + 
"-0.0016327664979662994" + 
":  " + 
"0.003582206090983377" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.75) ? " + 
"(b('g0vv') <= -13.337370872497559) ? " + 
"(b('b6') <= 1846.0) ? " + 
"0.021536773698842448" + 
":  " + 
"-0.02540083296050794" + 
":  " + 
"(b('moss') <= 13.232231140136719) ? " + 
"0.0005591858252054608" + 
":  " + 
"-0.018340446760694136" + 
":  " + 
"(b('b1') <= 299.5) ? " + 
"(b('grass') <= 50.46322441101074) ? " + 
"0.0013111445546830907" + 
":  " + 
"0.043794640770640894" + 
":  " + 
"(b('b1') <= 311.5) ? " + 
"-0.010735984629675456" + 
":  " + 
"0.00033078854872870103" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.018537521362305) ? " + 
"(b('lia') <= 37.56567573547363) ? " + 
"(b('grass') <= 87.20395278930664) ? " + 
"-0.0009984035212531783" + 
":  " + 
"0.012855039882188075" + 
":  " + 
"(b('b1') <= 470.5) ? " + 
"-0.04185841438059361" + 
":  " + 
"-0.00513862465766181" + 
":  " + 
"(b('lia') <= 38.853179931640625) ? " + 
"(b('b1') <= 629.5) ? " + 
"0.008057277321163627" + 
":  " + 
"0.04538798879053795" + 
":  " + 
"(b('bare') <= 0.29949215054512024) ? " + 
"-0.0028213351359973513" + 
":  " + 
"0.0018831608783925926" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('urban') <= 3.522911548614502) ? " + 
"(b('trees') <= 3.377434730529785) ? " + 
"-0.0010526060708789871" + 
":  " + 
"0.0022736893730094542" + 
":  " + 
"(b('b10') <= 1902.0) ? " + 
"0.10117783313213748" + 
":  " + 
"0.14975352498193137" + 
":  " + 
"(b('moss') <= 8.992009162902832) ? " + 
"(b('b5') <= 3030.0) ? " + 
"-0.00962014109326657" + 
":  " + 
"0.0020277527846551987" + 
":  " + 
"(b('g0vv') <= -9.26362657546997) ? " + 
"0.00182055381940201" + 
":  " + 
"0.040824958506315" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3450.5) ? " + 
"(b('crop') <= 89.04487609863281) ? " + 
"0.0006175866284105138" + 
":  " + 
"-0.005590845863119867" + 
":  " + 
"(b('lia') <= 26.563937187194824) ? " + 
"0.17355764109309985" + 
":  " + 
"0.010911329735125512" + 
":  " + 
"(b('b1') <= 589.5) ? " + 
"(b('b6') <= 2410.5) ? " + 
"0.008472462040608886" + 
":  " + 
"-0.014301437872891157" + 
":  " + 
"(b('b4') <= 902.5) ? " + 
"0.14242346311773973" + 
":  " + 
"0.002648795590653153" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 62.53530502319336) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"(b('grass') <= 45.666046142578125) ? " + 
"-3.0404564469063287e-05" + 
":  " + 
"-0.06634750448077294" + 
":  " + 
"(b('b4') <= 927.5) ? " + 
"0.024580970200299226" + 
":  " + 
"-0.007104803990513879" + 
":  " + 
"(b('crop') <= 35.33369064331055) ? " + 
"(b('crop') <= 5.957038402557373) ? " + 
"-0.0019068320618701238" + 
":  " + 
"0.017497224246281643" + 
":  " + 
"(b('g0vv') <= -13.069253921508789) ? " + 
"-0.034186796369398864" + 
":  " + 
"-0.060783126740402406" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.75) ? " + 
"(b('b4') <= 616.0) ? " + 
"(b('b3') <= 683.5) ? " + 
"-0.0023919066557981173" + 
":  " + 
"0.03418647204386266" + 
":  " + 
"(b('ndvi') <= 3553.0) ? " + 
"-0.0022303187549188295" + 
":  " + 
"-0.02012624285103725" + 
":  " + 
"(b('b4') <= 835.5) ? " + 
"(b('trees') <= 19.15903377532959) ? " + 
"0.006870831046804818" + 
":  " + 
"-0.018806831214303626" + 
":  " + 
"(b('trees') <= 19.789812088012695) ? " + 
"-0.0008850007982481047" + 
":  " + 
"0.01274993561552851" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 770.5) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"(b('b5') <= 2444.5) ? " + 
"0.0029846026046176605" + 
":  " + 
"-0.01323624942663359" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.01875657499577044" + 
":  " + 
"-0.0065515474215510575" + 
":  " + 
"(b('b11') <= 1323.0) ? " + 
"(b('bare') <= 1.335092842578888) ? " + 
"0.004208639221082485" + 
":  " + 
"0.035613392387270994" + 
":  " + 
"(b('b3') <= 772.5) ? " + 
"0.034009915815884646" + 
":  " + 
"5.5987000926105266e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 882.5) ? " + 
"(b('ndvi') <= 2785.5) ? " + 
"(b('trees') <= 13.24367094039917) ? " + 
"-0.0010195924477022008" + 
":  " + 
"0.02491887339031084" + 
":  " + 
"(b('trees') <= 19.15903377532959) ? " + 
"-0.002143328658698445" + 
":  " + 
"-0.020446631729451232" + 
":  " + 
"(b('b4') <= 1135.5) ? " + 
"(b('ndvi') <= 1780.5) ? " + 
"0.034806885556873196" + 
":  " + 
"0.004831317872435045" + 
":  " + 
"(b('b3') <= 959.5) ? " + 
"-0.013675590561310364" + 
":  " + 
"0.0005561368053660588" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 23.046470642089844) ? " + 
"(b('trees') <= 17.472150802612305) ? " + 
"-0.0002406850397566285" + 
":  " + 
"0.0061140320281267025" + 
":  " + 
"(b('ndvi') <= 1548.5) ? " + 
"0.19824308070794205" + 
":  " + 
"-0.011530994780082782" + 
":  " + 
"(b('grass') <= 33.25920295715332) ? " + 
"(b('l8dt') <= 2767509.0) ? " + 
"0.04222369865141741" + 
":  " + 
"-0.057974834332856925" + 
":  " + 
"(b('l8dt') <= 345600.5) ? " + 
"-0.03653909074235297" + 
":  " + 
"-0.00871690361394615" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 550.5) ? " + 
"(b('b3') <= 519.5) ? " + 
"(b('ndvi') <= 4992.0) ? " + 
"0.004695878824145024" + 
":  " + 
"-0.0697059887638946" + 
":  " + 
"(b('grass') <= 68.10729598999023) ? " + 
"-0.03625401920561047" + 
":  " + 
"0.08794187258183142" + 
":  " + 
"(b('b4') <= 485.5) ? " + 
"(b('b3') <= 603.5) ? " + 
"0.07232219830095055" + 
":  " + 
"-0.024985383315734" + 
":  " + 
"(b('b5') <= 1998.5) ? " + 
"0.005416507211065717" + 
":  " + 
"-0.00039686598613085226" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -16.00978374481201) ? " + 
"(b('b11') <= 1441.5) ? " + 
"(b('b6') <= 2414.75) ? " + 
"-0.0004728876301667841" + 
":  " + 
"-0.017997472667358006" + 
":  " + 
"(b('b4') <= 743.5) ? " + 
"0.013554259232926384" + 
":  " + 
"-0.0004659988608254461" + 
":  " + 
"(b('crop') <= 48.65084648132324) ? " + 
"(b('trees') <= 0.9620741009712219) ? " + 
"-0.02564398000052829" + 
":  " + 
"0.01732298714675865" + 
":  " + 
"(b('crop') <= 64.09599494934082) ? " + 
"-0.012692087877654995" + 
":  " + 
"0.0032632989200954772" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 882.5) ? " + 
"(b('b6') <= 3228.5) ? " + 
"(b('moss') <= 13.232231140136719) ? " + 
"0.0005567569662368534" + 
":  " + 
"-0.009195811754584733" + 
":  " + 
"(b('b11') <= 2124.0) ? " + 
"-0.04405144559111279" + 
":  " + 
"-0.010676923233316699" + 
":  " + 
"(b('b4') <= 944.5) ? " + 
"(b('bare') <= 4.077777862548828) ? " + 
"0.026023169407321606" + 
":  " + 
"-0.006149271003497627" + 
":  " + 
"(b('lia') <= 41.56817054748535) ? " + 
"0.0018778246160334616" + 
":  " + 
"-0.0038176968242452543" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3450.5) ? " + 
"(b('g0vv') <= -10.174442291259766) ? " + 
"-0.0006916490649652379" + 
":  " + 
"0.0028010479947507714" + 
":  " + 
"(b('lia') <= 26.094511032104492) ? " + 
"0.22117242569741274" + 
":  " + 
"0.010253347275832037" + 
":  " + 
"(b('b7') <= 2622.0) ? " + 
"(b('bare') <= 4.077777862548828) ? " + 
"-0.0018208505224470775" + 
":  " + 
"-0.02245224937844036" + 
":  " + 
"(b('b6') <= 3036.0) ? " + 
"0.19367197175691572" + 
":  " + 
"0.002280849581056248" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 593.5) ? " + 
"(b('b5') <= 3092.5) ? " + 
"(b('b4') <= 684.5) ? " + 
"-0.0008965011618900669" + 
":  " + 
"-0.02810873675336348" + 
":  " + 
"(b('ndvi') <= 3848.5) ? " + 
"-0.16062884730687024" + 
":  " + 
"-0.19123281342221257" + 
":  " + 
"(b('b6') <= 1933.0) ? " + 
"(b('bare') <= 1.6170774102210999) ? " + 
"0.0009554899910404508" + 
":  " + 
"0.024525612735010506" + 
":  " + 
"(b('b6') <= 1944.5) ? " + 
"-0.06190385158214131" + 
":  " + 
"8.096972512562603e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 23.046470642089844) ? " + 
"(b('trees') <= 17.472150802612305) ? " + 
"-0.00022183980245515334" + 
":  " + 
"0.0055269738144535655" + 
":  " + 
"(b('moss') <= 2.1891891956329346) ? " + 
"-0.07358245817218592" + 
":  " + 
"-0.007398371537323132" + 
":  " + 
"(b('b1') <= 464.0) ? " + 
"(b('b3') <= 647.5) ? " + 
"0.0008746048965578882" + 
":  " + 
"0.06675864633718304" + 
":  " + 
"(b('b6') <= 2809.5) ? " + 
"-0.06689527607137044" + 
":  " + 
"-0.030149810894832277" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 87.20395278930664) ? " + 
"(b('grass') <= 80.30580139160156) ? " + 
"(b('grass') <= 78.23077011108398) ? " + 
"-0.0003209559942592174" + 
":  " + 
"0.03543390229668742" + 
":  " + 
"(b('b4') <= 807.5) ? " + 
"0.031050824055234287" + 
":  " + 
"-0.011638212489357425" + 
":  " + 
"(b('b1') <= 383.5) ? " + 
"(b('b6') <= 2488.5) ? " + 
"0.005257394696176897" + 
":  " + 
"-0.04108431998369384" + 
":  " + 
"(b('b4') <= 734.5) ? " + 
"0.10281637414998102" + 
":  " + 
"0.00806646003335716" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.43209266662598) ? " + 
"(b('lia') <= 38.30871772766113) ? " + 
"(b('trees') <= 19.15903377532959) ? " + 
"-0.0002710861695974776" + 
":  " + 
"-0.012611849709445693" + 
":  " + 
"(b('bare') <= 2.403625726699829) ? " + 
"-0.05307025169463963" + 
":  " + 
"0.035699652076070794" + 
":  " + 
"(b('lia') <= 38.65497970581055) ? " + 
"(b('grass') <= 95.70454406738281) ? " + 
"0.025541434262633105" + 
":  " + 
"0.07920634553889663" + 
":  " + 
"(b('lia') <= 39.41095733642578) ? " + 
"0.007633022889003761" + 
":  " + 
"-0.0004929920756087901" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.928560256958008) ? " + 
"(b('l8dt') <= 493757.0) ? " + 
"(b('b5') <= 2803.5) ? " + 
"0.00610252121611482" + 
":  " + 
"-0.00828057114345008" + 
":  " + 
"(b('ndvi') <= 4859.5) ? " + 
"-0.010819638750080502" + 
":  " + 
"0.03132035705151924" + 
":  " + 
"(b('lia') <= 29.347232818603516) ? " + 
"(b('g0vv') <= -13.37679386138916) ? " + 
"0.02344571216362743" + 
":  " + 
"-0.009503041088526738" + 
":  " + 
"(b('lia') <= 29.585556983947754) ? " + 
"0.0334552351962322" + 
":  " + 
"0.0005188147416007266" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 2907.5) ? " + 
"(b('b7') <= 2889.5) ? " + 
"(b('b5') <= 3381.5) ? " + 
"0.0004357152618584212" + 
":  " + 
"-0.004609117498003986" + 
":  " + 
"(b('grass') <= 65.18574714660645) ? " + 
"-0.04116868791067896" + 
":  " + 
"0.012636669767395015" + 
":  " + 
"(b('b11') <= 2910.0) ? " + 
"(b('b5') <= 2708.5) ? " + 
"0.07163964073968357" + 
":  " + 
"-0.010214190160045187" + 
":  " + 
"(b('ndvi') <= 3015.5) ? " + 
"0.0010025797599445489" + 
":  " + 
"0.016689518331255048" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -2.327260732650757) ? " + 
"(b('g0vv') <= -6.5169548988342285) ? " + 
"(b('g0vh') <= -13.78833532333374) ? " + 
"-0.0002941187775941282" + 
":  " + 
"0.01233285157400215" + 
":  " + 
"(b('trees') <= 11.961585998535156) ? " + 
"0.01232810001084863" + 
":  " + 
"-0.019885576294743947" + 
":  " + 
"(b('b10') <= 2938.0) ? " + 
"(b('b11') <= 2623.0) ? " + 
"-0.07103116113143447" + 
":  " + 
"-0.07256130396275157" + 
":  " + 
"(b('g0vh') <= -15.40637493133545) ? " + 
"-0.03976081108457466" + 
":  " + 
"-0.05093232321508151" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('b3') <= 715.5) ? " + 
"(b('moss') <= 5.641550540924072) ? " + 
"-0.007026341777258874" + 
":  " + 
"0.006461432774299631" + 
":  " + 
"(b('bare') <= 0.4845890998840332) ? " + 
"-0.032433001283309" + 
":  " + 
"-0.0030108631789248514" + 
":  " + 
"(b('b11') <= 1322.5) ? " + 
"(b('bare') <= 0.955679714679718) ? " + 
"0.0034107449037756384" + 
":  " + 
"0.02831274978897348" + 
":  " + 
"(b('trees') <= 11.215232372283936) ? " + 
"-0.0009228489515511381" + 
":  " + 
"0.004991597743978214" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 354.5) ? " + 
"(b('b1') <= 310.0) ? " + 
"(b('ndvi') <= 3552.5) ? " + 
"0.001826855154740605" + 
":  " + 
"-0.01211707772761609" + 
":  " + 
"(b('b7') <= 1060.0) ? " + 
"-0.14596945406310574" + 
":  " + 
"-0.07376600686267176" + 
":  " + 
"(b('b2') <= 358.5) ? " + 
"(b('b6') <= 1955.0) ? " + 
"0.11010680526668441" + 
":  " + 
"0.016194397090409842" + 
":  " + 
"(b('b1') <= 256.5) ? " + 
"-0.021315790546739505" + 
":  " + 
"0.00038176177429708407" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('ndvi') <= 1646.5) ? " + 
"(b('crop') <= 99.63687133789062) ? " + 
"-0.002420135256060227" + 
":  " + 
"0.03518358582290887" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"0.0002381439457319648" + 
":  " + 
"0.015731345251183904" + 
":  " + 
"(b('b3') <= 1931.5) ? " + 
"(b('b6') <= 3243.0) ? " + 
"0.04337954801022319" + 
":  " + 
"0.018841972718229814" + 
":  " + 
"(b('l8dt') <= 734873.0) ? " + 
"0.008047999955695996" + 
":  " + 
"0.04172906849568686" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 911.5) ? " + 
"(b('b5') <= 3381.5) ? " + 
"(b('b4') <= 1679.5) ? " + 
"0.001040140818658594" + 
":  " + 
"-0.005891117534399144" + 
":  " + 
"(b('grass') <= 74.57086563110352) ? " + 
"-0.005489404955544502" + 
":  " + 
"0.0604527878933092" + 
":  " + 
"(b('b4') <= 2046.5) ? " + 
"(b('bare') <= 0.0628272220492363) ? " + 
"0.033467489237779445" + 
":  " + 
"0.0014786134320747683" + 
":  " + 
"(b('b5') <= 3309.5) ? " + 
"-0.0069629065313157055" + 
":  " + 
"0.00282989625408625" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1017.5) ? " + 
"(b('b6') <= 3242.5) ? " + 
"(b('b4') <= 1183.5) ? " + 
"0.0010340845335366842" + 
":  " + 
"-0.012752146364699573" + 
":  " + 
"(b('b10') <= 1993.0) ? " + 
"-0.048930679299887134" + 
":  " + 
"-0.009783629580247425" + 
":  " + 
"(b('b4') <= 1281.5) ? " + 
"(b('grass') <= 7.54269814491272) ? " + 
"-0.019250563407970003" + 
":  " + 
"0.022396337402471673" + 
":  " + 
"(b('b7') <= 1680.5) ? " + 
"0.054864251582577704" + 
":  " + 
"-9.765214493693387e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 816.5) ? " + 
"(b('b2') <= 545.5) ? " + 
"(b('lia') <= 44.74740982055664) ? " + 
"-0.0008571680195695285" + 
":  " + 
"0.13851324512844176" + 
":  " + 
"(b('b5') <= 2446.5) ? " + 
"-0.006786400643519541" + 
":  " + 
"-0.06270710890180889" + 
":  " + 
"(b('b4') <= 823.5) ? " + 
"(b('b11') <= 1702.5) ? " + 
"0.009101795658079472" + 
":  " + 
"0.054197666657983486" + 
":  " + 
"(b('b11') <= 1651.5) ? " + 
"-0.0077663118658589025" + 
":  " + 
"0.0010353128885169727" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.063567638397217) ? " + 
"(b('crop') <= 98.28740310668945) ? " + 
"(b('b1') <= 444.5) ? " + 
"-0.009179771874306875" + 
":  " + 
"-2.960251298661185e-06" + 
":  " + 
"(b('lia') <= 42.43045997619629) ? " + 
"0.056246922532022375" + 
":  " + 
"0.13227958751171917" + 
":  " + 
"(b('lia') <= 24.395869255065918) ? " + 
"(b('b4') <= 1251.5) ? " + 
"0.12955860941773947" + 
":  " + 
"-0.020331919570532264" + 
":  " + 
"(b('bare') <= 74.97966003417969) ? " + 
"0.00033498863364000156" + 
":  " + 
"0.02025292379635159" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.8708328604698181) ? " + 
"(b('urban') <= 0.513603001832962) ? " + 
"(b('ndvi') <= 5229.5) ? " + 
"0.0006200261025811155" + 
":  " + 
"-0.00816641847795645" + 
":  " + 
"(b('b3') <= 1078.5) ? " + 
"0.04259887579872628" + 
":  " + 
"0.1525829420776927" + 
":  " + 
"(b('b10') <= 1378.0) ? " + 
"(b('crop') <= 45.937931060791016) ? " + 
"0.027731069516337307" + 
":  " + 
"-0.0031852324865354583" + 
":  " + 
"(b('b3') <= 943.5) ? " + 
"-0.010150676915540027" + 
":  " + 
"0.00252877048129511" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 2.4269771575927734) ? " + 
"(b('crop') <= 1.691142737865448) ? " + 
"(b('trees') <= 13.327543258666992) ? " + 
"0.000713979542925048" + 
":  " + 
"-0.012908929605181349" + 
":  " + 
"(b('g0vv') <= -12.158383846282959) ? " + 
"-0.0663202288763761" + 
":  " + 
"0.0627989980369086" + 
":  " + 
"(b('crop') <= 21.2943696975708) ? " + 
"(b('ndvi') <= 3029.0) ? " + 
"0.048128838180848905" + 
":  " + 
"-0.009466305227377935" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.0006596993395071326" + 
":  " + 
"-0.0169772571885622" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.018537521362305) ? " + 
"(b('lia') <= 37.56567573547363) ? " + 
"(b('b4') <= 796.5) ? " + 
"0.004891236100115619" + 
":  " + 
"-0.001745065938792723" + 
":  " + 
"(b('b1') <= 470.5) ? " + 
"-0.03659439676493974" + 
":  " + 
"-0.005083417940411776" + 
":  " + 
"(b('lia') <= 38.853179931640625) ? " + 
"(b('g0vh') <= -15.292126655578613) ? " + 
"0.009297011080972528" + 
":  " + 
"0.07671798170209693" + 
":  " + 
"(b('l8dt') <= 2719.0) ? " + 
"0.023751708318269674" + 
":  " + 
"-0.00024259241431897694" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 364.5) ? " + 
"(b('b2') <= 362.5) ? " + 
"(b('crop') <= 94.68265533447266) ? " + 
"-0.003991842197742612" + 
":  " + 
"0.03437180720684485" + 
":  " + 
"(b('b4') <= 561.5) ? " + 
"0.028489884774241594" + 
":  " + 
"-0.05930679001861299" + 
":  " + 
"(b('b2') <= 366.5) ? " + 
"(b('b1') <= 259.0) ? " + 
"-0.014444732355012166" + 
":  " + 
"0.06668157671248388" + 
":  " + 
"(b('b1') <= 256.5) ? " + 
"-0.019823392173997523" + 
":  " + 
"0.0003827801591357295" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3303668.5) ? " + 
"(b('trees') <= 33.60975933074951) ? " + 
"(b('moss') <= 3.2275424003601074) ? " + 
"-0.001909339876104303" + 
":  " + 
"0.0006144654206845771" + 
":  " + 
"(b('moss') <= 5.756144165992737) ? " + 
"0.03521431285220406" + 
":  " + 
"-0.025574132746540062" + 
":  " + 
"(b('b6') <= 4860.5) ? " + 
"(b('moss') <= 1.940559446811676) ? " + 
"0.016999623393008072" + 
":  " + 
"8.957776942865716e-06" + 
":  " + 
"(b('l8dt') <= 6459549.5) ? " + 
"-0.051593139263770973" + 
":  " + 
"0.04556518929885346" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5439.0) ? " + 
"(b('urban') <= 0.8708328604698181) ? " + 
"(b('urban') <= 0.513603001832962) ? " + 
"0.00030638073521844865" + 
":  " + 
"0.06351356030406759" + 
":  " + 
"(b('g0vv') <= -16.212044715881348) ? " + 
"-0.06816882947158964" + 
":  " + 
"-0.0021466406217881305" + 
":  " + 
"(b('ndvi') <= 1593.0) ? " + 
"(b('ndvi') <= 1282.0) ? " + 
"-0.007193468859653221" + 
":  " + 
"-0.033948094008834556" + 
":  " + 
"(b('g0vh') <= -20.22484016418457) ? " + 
"0.02471408239819342" + 
":  " + 
"0.005660324242633463" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 6923.0) ? " + 
"(b('ndvi') <= 6611.5) ? " + 
"(b('ndvi') <= 6580.5) ? " + 
"-3.5301552011728916e-05" + 
":  " + 
"0.08107807417230756" + 
":  " + 
"(b('b3') <= 775.0) ? " + 
"-0.05460346709202711" + 
":  " + 
"0.00590839346639491" + 
":  " + 
"(b('lia') <= 43.50200653076172) ? " + 
"(b('trees') <= 10.456944465637207) ? " + 
"-0.0015789300124106724" + 
":  " + 
"0.06911879083448426" + 
":  " + 
"(b('g0vv') <= -12.697579860687256) ? " + 
"0.2083494804467019" + 
":  " + 
"0.09917280626788823" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -2.327260732650757) ? " + 
"(b('ndvi') <= 1646.5) ? " + 
"(b('crop') <= 99.63687133789062) ? " + 
"-0.0020246178707475117" + 
":  " + 
"0.03026044044335719" + 
":  " + 
"(b('ndvi') <= 1650.5) ? " + 
"0.04952900575345374" + 
":  " + 
"0.000588319515977585" + 
":  " + 
"(b('b6') <= 2919.0) ? " + 
"(b('lia') <= 35.77733898162842) ? " + 
"-0.06290683408293474" + 
":  " + 
"-0.06450754918440495" + 
":  " + 
"(b('g0vh') <= -15.40637493133545) ? " + 
"-0.03754565279832247" + 
":  " + 
"-0.04583317422814051" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 770.5) ? " + 
"(b('crop') <= 50.40138816833496) ? " + 
"(b('b2') <= 460.5) ? " + 
"0.004626531254283785" + 
":  " + 
"-0.01222179811323481" + 
":  " + 
"(b('trees') <= 14.932132720947266) ? " + 
"-0.01051544412234334" + 
":  " + 
"0.027226013493327532" + 
":  " + 
"(b('b10') <= 1325.5) ? " + 
"(b('bare') <= 0.3353944271802902) ? " + 
"0.00036415250796199817" + 
":  " + 
"0.026843879869736118" + 
":  " + 
"(b('b3') <= 772.5) ? " + 
"0.030176169517043005" + 
":  " + 
"3.674405082816717e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2050.5) ? " + 
"(b('b1') <= 408.5) ? " + 
"(b('crop') <= 93.05965042114258) ? " + 
"0.00015989255876588682" + 
":  " + 
"-0.04559591861838074" + 
":  " + 
"(b('crop') <= 69.35947799682617) ? " + 
"0.002679730474272902" + 
":  " + 
"0.027281182785501987" + 
":  " + 
"(b('l8dt') <= 8076292.5) ? " + 
"(b('b2') <= 318.5) ? " + 
"0.008081085694064924" + 
":  " + 
"-0.0006551586804042969" + 
":  " + 
"(b('b1') <= 667.0) ? " + 
"0.028783030427432254" + 
":  " + 
"0.05976091323028067" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 354.5) ? " + 
"(b('trees') <= 13.24367094039917) ? " + 
"(b('crop') <= 50.93680191040039) ? " + 
"0.006273692558316947" + 
":  " + 
"-0.009489714875521998" + 
":  " + 
"(b('b7') <= 1145.0) ? " + 
"0.0008176937313452664" + 
":  " + 
"-0.040586161553808835" + 
":  " + 
"(b('b2') <= 358.5) ? " + 
"(b('bare') <= 3.047169804573059) ? " + 
"0.0390683370913852" + 
":  " + 
"-0.054672623262040365" + 
":  " + 
"(b('b1') <= 256.5) ? " + 
"-0.017618862054605607" + 
":  " + 
"0.00035504886151447175" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3486.5) ? " + 
"(b('lia') <= 42.50589179992676) ? " + 
"0.0008712960942173258" + 
":  " + 
"-0.0033087792302110924" + 
":  " + 
"(b('grass') <= 0.16759777069091797) ? " + 
"0.050153022033196264" + 
":  " + 
"0.00784061334086208" + 
":  " + 
"(b('b5') <= 3525.5) ? " + 
"(b('trees') <= 6.917280673980713) ? " + 
"-0.021843712387473575" + 
":  " + 
"-0.10324842405414661" + 
":  " + 
"(b('bare') <= 4.077777862548828) ? " + 
"0.001307102888459952" + 
":  " + 
"-0.008817475045143122" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.43072509765625) ? " + 
"(b('lia') <= 38.30871772766113) ? " + 
"(b('lia') <= 38.16310501098633) ? " + 
"-0.001085977391554505" + 
":  " + 
"0.01718261157370341" + 
":  " + 
"(b('bare') <= 2.403625726699829) ? " + 
"-0.05170703476666552" + 
":  " + 
"0.031707574092614633" + 
":  " + 
"(b('lia') <= 38.6629638671875) ? " + 
"(b('trees') <= 19.831669807434082) ? " + 
"0.02145352751699164" + 
":  " + 
"0.08211868640131793" + 
":  " + 
"(b('lia') <= 39.41095733642578) ? " + 
"0.006600714426388603" + 
":  " + 
"-0.000351638732822717" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 2907.5) ? " + 
"(b('b7') <= 2889.5) ? " + 
"(b('b4') <= 1842.0) ? " + 
"0.00016038690478957268" + 
":  " + 
"-0.006480228784659986" + 
":  " + 
"(b('moss') <= 13.362539291381836) ? " + 
"-0.03707932695274112" + 
":  " + 
"0.011810333237301721" + 
":  " + 
"(b('b10') <= 2910.0) ? " + 
"(b('ndvi') <= 1344.0) ? " + 
"0.06947900229142796" + 
":  " + 
"0.003668301857259751" + 
":  " + 
"(b('trees') <= 2.107696294784546) ? " + 
"0.00010978414559201839" + 
":  " + 
"0.008984413246425694" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 364.5) ? " + 
"(b('b2') <= 362.5) ? " + 
"(b('crop') <= 94.68265533447266) ? " + 
"-0.003757069201913866" + 
":  " + 
"0.032549582182040564" + 
":  " + 
"(b('b4') <= 561.5) ? " + 
"0.02693067669794734" + 
":  " + 
"-0.05355420386566922" + 
":  " + 
"(b('b2') <= 366.5) ? " + 
"(b('b3') <= 728.0) ? " + 
"0.06402555184708866" + 
":  " + 
"-0.005207893771360528" + 
":  " + 
"(b('b1') <= 236.5) ? " + 
"-0.03915090661785076" + 
":  " + 
"0.00027125874665548573" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 181.0) ? " + 
"(b('g0vv') <= -12.663116455078125) ? " + 
"(b('l8dt') <= 518406.0) ? " + 
"0.03715355366443543" + 
":  " + 
"0.09585129417814407" + 
":  " + 
"(b('g0vv') <= -9.463024616241455) ? " + 
"0.0019944519391411992" + 
":  " + 
"0.06166232518307572" + 
":  " + 
"(b('b2') <= 229.0) ? " + 
"(b('lia') <= 30.674999237060547) ? " + 
"0.14871481841423878" + 
":  " + 
"-0.04045585087059333" + 
":  " + 
"(b('b2') <= 241.5) ? " + 
"0.032989787959540835" + 
":  " + 
"-2.171766870198945e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 43.71040153503418) ? " + 
"(b('lia') <= 43.592063903808594) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"-0.00034964983872371017" + 
":  " + 
"0.009567660440271393" + 
":  " + 
"(b('grass') <= 98.10429382324219) ? " + 
"-0.002707443944442247" + 
":  " + 
"-0.06548163756263996" + 
":  " + 
"(b('ndvi') <= 6586.5) ? " + 
"(b('grass') <= 12.461678981781006) ? " + 
"-0.011890394942979422" + 
":  " + 
"0.007466837198643378" + 
":  " + 
"(b('g0vh') <= -19.533024787902832) ? " + 
"0.027021970529293643" + 
":  " + 
"0.15166824423544378" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.87747859954834) ? " + 
"(b('trees') <= 7.314132928848267) ? " + 
"(b('urban') <= 0.4475524425506592) ? " + 
"-0.0001648243579604609" + 
":  " + 
"-0.04857539979300373" + 
":  " + 
"(b('l8dt') <= 5328.5) ? " + 
"0.06717848335735006" + 
":  " + 
"-0.024164046387046178" + 
":  " + 
"(b('l8dt') <= 107327.5) ? " + 
"(b('g0vh') <= -17.7103910446167) ? " + 
"-0.00027134642495940295" + 
":  " + 
"-0.010845534098010146" + 
":  " + 
"(b('l8dt') <= 107803.5) ? " + 
"0.03863279711573591" + 
":  " + 
"0.0006359445423132602" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2785.5) ? " + 
"(b('trees') <= 18.005227088928223) ? " + 
"(b('b4') <= 1183.5) ? " + 
"0.0034391512412531608" + 
":  " + 
"-0.0015803989232221843" + 
":  " + 
"(b('crop') <= 11.22841739654541) ? " + 
"-0.005663942348930557" + 
":  " + 
"0.036112555793855826" + 
":  " + 
"(b('trees') <= 19.15903377532959) ? " + 
"(b('grass') <= 44.75456619262695) ? " + 
"-0.0029849269926328194" + 
":  " + 
"0.007968575474318151" + 
":  " + 
"(b('grass') <= 35.01466178894043) ? " + 
"0.005823400068325194" + 
":  " + 
"-0.03028764078430075" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b1') <= 598.5) ? " + 
"(b('b11') <= 1784.0) ? " + 
"-0.0019928461171836538" + 
":  " + 
"0.01831722975957139" + 
":  " + 
"(b('b3') <= 1215.5) ? " + 
"-0.023018309726629257" + 
":  " + 
"0.0006642433097514767" + 
":  " + 
"(b('crop') <= 95.60836410522461) ? " + 
"(b('crop') <= 94.68265533447266) ? " + 
"-0.0005016666770110252" + 
":  " + 
"0.06717363942778504" + 
":  " + 
"(b('ndvi') <= 4235.0) ? " + 
"0.0037539143344024087" + 
":  " + 
"-0.04546986139125386" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 629.5) ? " + 
"(b('b4') <= 1664.5) ? " + 
"(b('b2') <= 876.0) ? " + 
"-0.0001184194792166546" + 
":  " + 
"0.1929761316202463" + 
":  " + 
"(b('b11') <= 2072.0) ? " + 
"-0.0447700273496117" + 
":  " + 
"-0.006721272885566554" + 
":  " + 
"(b('b11') <= 1511.0) ? " + 
"(b('l8dt') <= 212822.0) ? " + 
"0.1723410675043675" + 
":  " + 
"0.15822207855450482" + 
":  " + 
"(b('b4') <= 1910.5) ? " + 
"0.005455150585115743" + 
":  " + 
"-0.0005123976867532357" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1420.5) ? " + 
"(b('b5') <= 3381.5) ? " + 
"(b('b4') <= 1741.5) ? " + 
"0.0009094448190637142" + 
":  " + 
"-0.007285993536201504" + 
":  " + 
"(b('bare') <= 4.871954917907715) ? " + 
"-0.0021864284815376936" + 
":  " + 
"-0.016248579335585628" + 
":  " + 
"(b('b4') <= 1903.0) ? " + 
"(b('bare') <= 0.0628272220492363) ? " + 
"0.05966605184039476" + 
":  " + 
"0.016597589016040862" + 
":  " + 
"(b('ndvi') <= 3111.5) ? " + 
"-0.0007852044307770372" + 
":  " + 
"0.02503138782483726" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 2907.5) ? " + 
"(b('b11') <= 2889.5) ? " + 
"(b('g0vv') <= -10.708893775939941) ? " + 
"-0.0015906155381279511" + 
":  " + 
"0.0019898827865162823" + 
":  " + 
"(b('grass') <= 65.18574714660645) ? " + 
"-0.032317314272016194" + 
":  " + 
"0.012257117599239106" + 
":  " + 
"(b('b7') <= 2910.0) ? " + 
"(b('b5') <= 2708.5) ? " + 
"0.05713638973502573" + 
":  " + 
"-0.015407612041872751" + 
":  " + 
"(b('b5') <= 2287.5) ? " + 
"-0.01859914392974953" + 
":  " + 
"0.002590931242949146" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 593.5) ? " + 
"(b('b5') <= 3092.5) ? " + 
"(b('b4') <= 684.5) ? " + 
"-0.0006783459338297159" + 
":  " + 
"-0.026247444541703056" + 
":  " + 
"(b('g0vv') <= -13.218113422393799) ? " + 
"-0.14057882705497887" + 
":  " + 
"-0.16835346634687282" + 
":  " + 
"(b('b4') <= 520.5) ? " + 
"(b('grass') <= 11.245258808135986) ? " + 
"0.10895143337281181" + 
":  " + 
"-0.004956241773284484" + 
":  " + 
"(b('b2') <= 270.0) ? " + 
"-0.06089114197095289" + 
":  " + 
"0.00019720801259413663" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('ndvi') <= 932.0) ? " + 
"0.07299278249227573" + 
":  " + 
"-0.0015473007005232797" + 
":  " + 
"(b('b10') <= 2383.0) ? " + 
"0.016284533721892532" + 
":  " + 
"0.07473915042635007" + 
":  " + 
"(b('bare') <= 0.3734448403120041) ? " + 
"(b('g0vv') <= -11.470760345458984) ? " + 
"0.08726775876539614" + 
":  " + 
"0.014583806731801714" + 
":  " + 
"(b('grass') <= 87.1015739440918) ? " + 
"0.0008109470755200017" + 
":  " + 
"-0.02944006059052763" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 23.278701782226562) ? " + 
"(b('urban') <= 14.72341012954712) ? " + 
"(b('g0vv') <= -14.063567638397217) ? " + 
"-0.0025842670143907485" + 
":  " + 
"0.0005565764275441101" + 
":  " + 
"(b('g0vv') <= -11.89726734161377) ? " + 
"0.007843192820345235" + 
":  " + 
"0.07702684195081429" + 
":  " + 
"(b('ndvi') <= 714.5) ? " + 
"0.17625786596140158" + 
":  " + 
"(b('b6') <= 3016.0) ? " + 
"-0.007871711370612487" + 
":  " + 
"0.005808094835620506" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 73.84134292602539) ? " + 
"(b('ndvi') <= 1139.5) ? " + 
"(b('lia') <= 43.75522422790527) ? " + 
"-0.0034617848469186362" + 
":  " + 
"-0.029676839826530035" + 
":  " + 
"(b('lia') <= 43.704647064208984) ? " + 
"-0.0001719642884012639" + 
":  " + 
"0.007211744411985887" + 
":  " + 
"(b('b6') <= 4620.0) ? " + 
"(b('lia') <= 43.83162307739258) ? " + 
"0.02210843432238643" + 
":  " + 
"-0.013475873132271126" + 
":  " + 
"(b('g0vh') <= -22.322280883789062) ? " + 
"-0.017101562190386197" + 
":  " + 
"-0.0009640677515543993" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 4636.0) ? " + 
"(b('g0vv') <= -13.039248943328857) ? " + 
"-0.0017153453954691492" + 
":  " + 
"0.0006309836256226393" + 
":  " + 
"(b('g0vh') <= -17.361992835998535) ? " + 
"-0.0852271029973814" + 
":  " + 
"-0.03913872786610848" + 
":  " + 
"(b('lia') <= 43.13669395446777) ? " + 
"(b('l8dt') <= 2049076.0) ? " + 
"0.011338298475728122" + 
":  " + 
"-0.015168430546575039" + 
":  " + 
"(b('lia') <= 43.36713409423828) ? " + 
"0.10385612969257729" + 
":  " + 
"0.0069854708818266956" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 87.20395278930664) ? " + 
"(b('grass') <= 80.30580139160156) ? " + 
"(b('grass') <= 78.23077011108398) ? " + 
"-0.00025796370040024816" + 
":  " + 
"0.029368533746205516" + 
":  " + 
"(b('bare') <= 2.6389132738113403) ? " + 
"-0.019688621459283025" + 
":  " + 
"0.002662662031301037" + 
":  " + 
"(b('moss') <= 12.59807300567627) ? " + 
"(b('b1') <= 380.5) ? " + 
"-0.025469845116957386" + 
":  " + 
"0.005351209658842249" + 
":  " + 
"(b('g0vh') <= -20.432751655578613) ? " + 
"0.00392309812488718" + 
":  " + 
"0.07398005101632388" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.42710304260254) ? " + 
"(b('lia') <= 38.30871772766113) ? " + 
"(b('trees') <= 4.025065779685974) ? " + 
"-0.0025584837671766584" + 
":  " + 
"0.002005782567274457" + 
":  " + 
"(b('bare') <= 2.403625726699829) ? " + 
"-0.05466682383498627" + 
":  " + 
"0.03131355024648324" + 
":  " + 
"(b('lia') <= 38.65497970581055) ? " + 
"(b('grass') <= 95.70454406738281) ? " + 
"0.016069965203166895" + 
":  " + 
"0.06582670482522496" + 
":  " + 
"(b('lia') <= 39.41095733642578) ? " + 
"0.0061455647550592565" + 
":  " + 
"-0.0002735351401380312" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -10.326126098632812) ? " + 
"(b('g0vh') <= -13.813458442687988) ? " + 
"(b('ndvi') <= 6923.0) ? " + 
"-0.00020941627029624944" + 
":  " + 
"0.01659159347410815" + 
":  " + 
"(b('moss') <= 1.2607092261314392) ? " + 
"0.02550234238751368" + 
":  " + 
"-0.0012853471898998073" + 
":  " + 
"(b('l8dt') <= 1036801.0) ? " + 
"-0.10940921709046897" + 
":  " + 
"(b('l8dt') <= 1363306.5) ? " + 
"-0.0013336042026021455" + 
":  " + 
"-0.02922839822873534" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.928560256958008) ? " + 
"(b('g0vv') <= -14.981057167053223) ? " + 
"(b('g0vv') <= -14.98452377319336) ? " + 
"-0.0025089877002173223" + 
":  " + 
"0.1030916587146955" + 
":  " + 
"(b('ndvi') <= 2685.0) ? " + 
"-0.010514089396364248" + 
":  " + 
"-0.061023838538279265" + 
":  " + 
"(b('grass') <= 34.49201011657715) ? " + 
"(b('grass') <= 24.055472373962402) ? " + 
"0.0007469039081167537" + 
":  " + 
"-0.008427392948932423" + 
":  " + 
"(b('crop') <= 39.048561096191406) ? " + 
"-0.0005029050332050347" + 
":  " + 
"0.021170422238104048" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('urban') <= 3.522911548614502) ? " + 
"(b('g0vv') <= -8.906897068023682) ? " + 
"-0.00012794418295101228" + 
":  " + 
"0.004468536866045447" + 
":  " + 
"(b('ndvi') <= 2064.0) ? " + 
"0.130943050363609" + 
":  " + 
"0.08298804162447225" + 
":  " + 
"(b('b5') <= 4200.0) ? " + 
"(b('b5') <= 3734.0) ? " + 
"-0.00200983796487836" + 
":  " + 
"-0.020825303876175646" + 
":  " + 
"(b('b2') <= 565.5) ? " + 
"0.11841217377903938" + 
":  " + 
"0.03599239892453307" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 816.5) ? " + 
"(b('moss') <= 0.905249685049057) ? " + 
"(b('b5') <= 2420.0) ? " + 
"0.005344934772715777" + 
":  " + 
"-0.017470635116926213" + 
":  " + 
"(b('moss') <= 2.0455974340438843) ? " + 
"0.01965894265984186" + 
":  " + 
"-0.0010966142949886133" + 
":  " + 
"(b('b4') <= 943.5) ? " + 
"(b('urban') <= 0.0784313753247261) ? " + 
"0.015026380155902451" + 
":  " + 
"-0.00591988359482854" + 
":  " + 
"(b('b11') <= 1644.0) ? " + 
"-0.013553133160948446" + 
":  " + 
"0.0006422508370685724" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 12.501765251159668) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"-0.0002780719126736118" + 
":  " + 
"0.01944811640146725" + 
":  " + 
"(b('b1') <= 407.5) ? " + 
"0.0029442732997422712" + 
":  " + 
"-0.009615356655700697" + 
":  " + 
"(b('b1') <= 464.0) ? " + 
"(b('b3') <= 647.5) ? " + 
"0.0010638001127473826" + 
":  " + 
"0.057084536055330155" + 
":  " + 
"(b('trees') <= 45.3707218170166) ? " + 
"-0.052225268994017096" + 
":  " + 
"-0.013337906445098385" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('b3') <= 722.5) ? " + 
"(b('trees') <= 11.076036930084229) ? " + 
"0.0028705986429218267" + 
":  " + 
"-0.008703015288431086" + 
":  " + 
"(b('b1') <= 413.5) ? " + 
"-0.037276311173240324" + 
":  " + 
"0.2250626583022661" + 
":  " + 
"(b('b6') <= 2210.0) ? " + 
"(b('b2') <= 631.0) ? " + 
"0.014804745536243393" + 
":  " + 
"-0.03148192382723454" + 
":  " + 
"(b('b6') <= 2375.5) ? " + 
"-0.007800747267377978" + 
":  " + 
"0.0003978362823478772" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 89.04487609863281) ? " + 
"(b('crop') <= 85.84851455688477) ? " + 
"(b('crop') <= 85.4493522644043) ? " + 
"0.00018956355647525573" + 
":  " + 
"-0.018303169797647362" + 
":  " + 
"(b('b6') <= 3152.5) ? " + 
"0.02622624481530967" + 
":  " + 
"-0.0008309390448979152" + 
":  " + 
"(b('b1') <= 449.5) ? " + 
"(b('b10') <= 1109.5) ? " + 
"0.017289925004942724" + 
":  " + 
"-0.025225970751608432" + 
":  " + 
"(b('b6') <= 3119.5) ? " + 
"0.015100748136182177" + 
":  " + 
"-0.002455364557662867" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b10') <= 2906.5) ? " + 
"(b('b5') <= 3381.5) ? " + 
"(b('b4') <= 1842.0) ? " + 
"0.0008128261286173523" + 
":  " + 
"-0.00793289140457499" + 
":  " + 
"(b('bare') <= 4.871954917907715) ? " + 
"-0.0011835606116286873" + 
":  " + 
"-0.015970469462523035" + 
":  " + 
"(b('b7') <= 2910.0) ? " + 
"(b('ndvi') <= 1344.0) ? " + 
"0.05814946606259436" + 
":  " + 
"-0.0001914889293215412" + 
":  " + 
"(b('b5') <= 2287.5) ? " + 
"-0.01686848659886949" + 
":  " + 
"0.0024803364854267865" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 892.25) ? " + 
"(b('b6') <= 3223.5) ? " + 
"(b('moss') <= 13.232231140136719) ? " + 
"0.0006194467237010981" + 
":  " + 
"-0.007470397164336288" + 
":  " + 
"(b('g0vv') <= -8.58899211883545) ? " + 
"-0.02077679679383434" + 
":  " + 
"0.09226387574316235" + 
":  " + 
"(b('b4') <= 1232.5) ? " + 
"(b('grass') <= 63.09731101989746) ? " + 
"-0.00023988531082828237" + 
":  " + 
"0.019546595718439502" + 
":  " + 
"(b('grass') <= 50.71351623535156) ? " + 
"0.001873394252330519" + 
":  " + 
"-0.006525898494904606" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 364.5) ? " + 
"(b('b2') <= 361.5) ? " + 
"(b('g0vv') <= -12.110625743865967) ? " + 
"-0.011632503130104537" + 
":  " + 
"0.0021336091523120274" + 
":  " + 
"(b('b3') <= 705.0) ? " + 
"-0.04835822021111502" + 
":  " + 
"0.06714086957938034" + 
":  " + 
"(b('b2') <= 366.5) ? " + 
"(b('b1') <= 259.0) ? " + 
"-0.015806785260608226" + 
":  " + 
"0.051920900798484805" + 
":  " + 
"(b('b4') <= 743.5) ? " + 
"0.004474371552270241" + 
":  " + 
"-0.00032156423591262774" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 9.947502613067627) ? " + 
"(b('bare') <= 9.127102851867676) ? " + 
"(b('b5') <= 3518.0) ? " + 
"0.00044677213859923285" + 
":  " + 
"-0.003665456066530106" + 
":  " + 
"(b('lia') <= 30.104607582092285) ? " + 
"0.12322280177983094" + 
":  " + 
"-0.020902041390378316" + 
":  " + 
"(b('crop') <= 52.3651237487793) ? " + 
"(b('g0vv') <= -6.204157114028931) ? " + 
"0.0017602932012749438" + 
":  " + 
"0.17320910205673207" + 
":  " + 
"(b('b2') <= 603.0) ? " + 
"0.03488447783541454" + 
":  " + 
"0.07456504055060711" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 812.5) ? " + 
"(b('b3') <= 807.5) ? " + 
"(b('grass') <= 46.57562255859375) ? " + 
"-0.003775418929860114" + 
":  " + 
"0.0031195578110280848" + 
":  " + 
"(b('b2') <= 396.5) ? " + 
"0.06354495399326103" + 
":  " + 
"-0.03405756406822343" + 
":  " + 
"(b('b4') <= 842.5) ? " + 
"(b('moss') <= 0.06295757554471493) ? " + 
"0.026931940978975093" + 
":  " + 
"0.00421757184176363" + 
":  " + 
"(b('b10') <= 1651.5) ? " + 
"-0.008350949079782545" + 
":  " + 
"0.0009156835100053793" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.869969367980957) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"(b('b2') <= 414.5) ? " + 
"-0.03959814378217333" + 
":  " + 
"-0.00621408050890511" + 
":  " + 
"(b('lia') <= 43.92072105407715) ? " + 
"0.010838804300173296" + 
":  " + 
"-0.06991497265614766" + 
":  " + 
"(b('g0vv') <= -15.865667343139648) ? " + 
"(b('b1') <= 485.5) ? " + 
"0.17560773271722951" + 
":  " + 
"0.04064358682330183" + 
":  " + 
"(b('l8dt') <= 107327.5) ? " + 
"-0.0027715674535179705" + 
":  " + 
"0.0006242415935305542" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 7.140108346939087) ? " + 
"(b('moss') <= 6.651747465133667) ? " + 
"-0.00207962325044876" + 
":  " + 
"-0.03925772484590184" + 
":  " + 
"(b('moss') <= 7.598436594009399) ? " + 
"0.035725896927880786" + 
":  " + 
"0.0009199118302616367" + 
":  " + 
"(b('bare') <= 0.3734448403120041) ? " + 
"(b('b6') <= 2895.0) ? " + 
"0.008795441311052152" + 
":  " + 
"0.06025015779589931" + 
":  " + 
"(b('grass') <= 87.1015739440918) ? " + 
"0.0007878094219531929" + 
":  " + 
"-0.026142721904610457" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5439.0) ? " + 
"(b('b10') <= 3248.5) ? " + 
"(b('b4') <= 2652.0) ? " + 
"-0.0002941840664790538" + 
":  " + 
"0.02860290670745835" + 
":  " + 
"(b('b4') <= 2096.5) ? " + 
"0.012960331421664762" + 
":  " + 
"8.723144131390113e-05" + 
":  " + 
"(b('g0vh') <= -21.055819511413574) ? " + 
"(b('lia') <= 38.14970779418945) ? " + 
"0.014172910953715784" + 
":  " + 
"-0.009813947105330699" + 
":  " + 
"(b('l8dt') <= 942151.5) ? " + 
"-0.020940068072745573" + 
":  " + 
"-0.03639458987828659" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('l8dt') <= 3303668.5) ? " + 
"(b('grass') <= 34.49201011657715) ? " + 
"-0.0012261282252785275" + 
":  " + 
"0.0010876478218485473" + 
":  " + 
"(b('b3') <= 1712.5) ? " + 
"0.0057446123445068584" + 
":  " + 
"-0.027805560886656554" + 
":  " + 
"(b('ndvi') <= 3955.5) ? " + 
"(b('ndvi') <= 3758.0) ? " + 
"0.03189722135232616" + 
":  " + 
"0.11225051976564893" + 
":  " + 
"(b('b3') <= 637.0) ? " + 
"-0.029008940597570552" + 
":  " + 
"0.021619133542040807" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -10.326126098632812) ? " + 
"(b('g0vh') <= -12.285078048706055) ? " + 
"(b('g0vv') <= -2.947663903236389) ? " + 
"-2.579695988639331e-06" + 
":  " + 
"-0.0377428485186268" + 
":  " + 
"(b('ndvi') <= 2863.0) ? " + 
"0.07054402135041794" + 
":  " + 
"-0.0015203735817681248" + 
":  " + 
"(b('ndvi') <= 2430.0) ? " + 
"-0.1046831710911979" + 
":  " + 
"(b('crop') <= 78.01056671142578) ? " + 
"-0.02569881136211008" + 
":  " + 
"-0.007415119492117761" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.018537521362305) ? " + 
"(b('lia') <= 37.9957332611084) ? " + 
"(b('lia') <= 37.56567573547363) ? " + 
"-0.00022298728482734277" + 
":  " + 
"-0.01234124578033027" + 
":  " + 
"(b('g0vv') <= -12.485623836517334) ? " + 
"0.019494603915313546" + 
":  " + 
"-0.07282026754359483" + 
":  " + 
"(b('lia') <= 38.85299491882324) ? " + 
"(b('g0vh') <= -15.75604772567749) ? " + 
"0.006283774108221373" + 
":  " + 
"0.055719525625879174" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"-0.001394509144716229" + 
":  " + 
"0.002634498161707206" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 24.395869255065918) ? " + 
"(b('b4') <= 1248.0) ? " + 
"(b('b6') <= 3109.0) ? " + 
"0.10168551835973266" + 
":  " + 
"0.1440816573550936" + 
":  " + 
"(b('g0vv') <= -14.644976615905762) ? " + 
"0.01753932167321496" + 
":  " + 
"-0.014503115956750587" + 
":  " + 
"(b('lia') <= 29.42397689819336) ? " + 
"(b('lia') <= 29.37598419189453) ? " + 
"-0.0046772376445618795" + 
":  " + 
"-0.09889717872526387" + 
":  " + 
"(b('lia') <= 29.42924976348877) ? " + 
"0.15889669635861095" + 
":  " + 
"0.0001393168235279041" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 62.53530502319336) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"(b('grass') <= 45.666046142578125) ? " + 
"-5.8510650606783075e-05" + 
":  " + 
"-0.048565575115682734" + 
":  " + 
"(b('b4') <= 932.5) ? " + 
"0.020065476002993056" + 
":  " + 
"-0.005798161071609127" + 
":  " + 
"(b('crop') <= 35.33369064331055) ? " + 
"(b('crop') <= 5.957038402557373) ? " + 
"-0.0017942334665434795" + 
":  " + 
"0.016297413383791443" + 
":  " + 
"(b('g0vv') <= -12.970137119293213) ? " + 
"-0.027897231479823932" + 
":  " + 
"-0.052865905654435164" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.25) ? " + 
"(b('g0vv') <= -12.110625743865967) ? " + 
"(b('b1') <= 331.5) ? " + 
"-0.013034906329517733" + 
":  " + 
"0.032324660269504105" + 
":  " + 
"(b('bare') <= 2.412587285041809) ? " + 
"-0.0025243701246071273" + 
":  " + 
"0.01378905338284314" + 
":  " + 
"(b('b3') <= 561.5) ? " + 
"(b('ndvi') <= 1901.0) ? " + 
"-0.0014180726699164054" + 
":  " + 
"-0.04684185547982516" + 
":  " + 
"(b('b4') <= 743.5) ? " + 
"0.005518471373504921" + 
":  " + 
"-7.031603478005521e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2785.5) ? " + 
"(b('trees') <= 18.005227088928223) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"0.0002693090846531709" + 
":  " + 
"-0.03765507890379502" + 
":  " + 
"(b('crop') <= 11.22841739654541) ? " + 
"-0.0040804765873818875" + 
":  " + 
"0.032441627554726786" + 
":  " + 
"(b('ndvi') <= 3218.0) ? " + 
"(b('b5') <= 2506.0) ? " + 
"0.002974820305919871" + 
":  " + 
"-0.011646497225867877" + 
":  " + 
"(b('trees') <= 12.86857271194458) ? " + 
"0.0029824837348425425" + 
":  " + 
"-0.007855356171792166" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 771.5) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"(b('b6') <= 2451.5) ? " + 
"-0.00119177847998698" + 
":  " + 
"-0.01618053084004499" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.015217991252911975" + 
":  " + 
"-0.004830943368283415" + 
":  " + 
"(b('b3') <= 772.5) ? " + 
"(b('trees') <= 13.927891731262207) ? " + 
"-0.03439350111348901" + 
":  " + 
"0.1380060369879709" + 
":  " + 
"(b('b10') <= 1325.5) ? " + 
"0.011597360232112002" + 
":  " + 
"0.0001210586678546713" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.25) ? " + 
"(b('lia') <= 41.87085723876953) ? " + 
"(b('g0vv') <= -12.110625743865967) ? " + 
"-0.015108701104820231" + 
":  " + 
"-0.0011752987907482503" + 
":  " + 
"(b('moss') <= 15.613604068756104) ? " + 
"0.004951209257325613" + 
":  " + 
"0.0875788226758391" + 
":  " + 
"(b('b1') <= 351.5) ? " + 
"(b('grass') <= 99.8344841003418) ? " + 
"0.004629347443314641" + 
":  " + 
"-0.037169054092656924" + 
":  " + 
"(b('b7') <= 1426.5) ? " + 
"-0.01120856947021884" + 
":  " + 
"0.0002050029151499679" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2160.5) ? " + 
"(b('b5') <= 2153.5) ? " + 
"(b('b4') <= 1166.0) ? " + 
"0.003981779537866349" + 
":  " + 
"-0.005928922413993055" + 
":  " + 
"(b('b7') <= 1788.0) ? " + 
"0.11329437998233886" + 
":  " + 
"0.006155522308357208" + 
":  " + 
"(b('b5') <= 2321.5) ? " + 
"(b('l8dt') <= 2721.0) ? " + 
"0.06811947470441912" + 
":  " + 
"-0.006715595083912492" + 
":  " + 
"(b('b5') <= 2436.5) ? " + 
"0.007823449769667734" + 
":  " + 
"-0.0005939990545014537" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 927.5) ? " + 
"(b('b6') <= 3242.5) ? " + 
"(b('b4') <= 1180.5) ? " + 
"1.7074169762035886e-05" + 
":  " + 
"-0.022243051799715353" + 
":  " + 
"(b('b7') <= 2001.5) ? " + 
"-0.04758673076128313" + 
":  " + 
"-0.013025678598430032" + 
":  " + 
"(b('b5') <= 1701.0) ? " + 
"(b('g0vv') <= -10.683626174926758) ? " + 
"-0.057768086500532945" + 
":  " + 
"-0.10430219058432288" + 
":  " + 
"(b('b4') <= 1289.5) ? " + 
"0.006417306630264106" + 
":  " + 
"-0.0003954367836275694" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('crop') <= 50.40138816833496) ? " + 
"(b('trees') <= 12.501765251159668) ? " + 
"0.007305551841740879" + 
":  " + 
"-0.008679219621276782" + 
":  " + 
"(b('b5') <= 2137.0) ? " + 
"0.0036940930186509786" + 
":  " + 
"-0.020415591256090007" + 
":  " + 
"(b('b6') <= 2210.0) ? " + 
"(b('ndvi') <= 1450.0) ? " + 
"-0.01632489419436387" + 
":  " + 
"0.014200701772452083" + 
":  " + 
"(b('trees') <= 9.420434951782227) ? " + 
"-0.0009204141242575208" + 
":  " + 
"0.0030320644912103854" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 629.5) ? " + 
"(b('b5') <= 3381.5) ? " + 
"(b('ndvi') <= 1646.5) ? " + 
"-0.004396541205234053" + 
":  " + 
"0.00129758075357179" + 
":  " + 
"(b('bare') <= 4.871954917907715) ? " + 
"-0.001568435133702811" + 
":  " + 
"-0.0158362147733821" + 
":  " + 
"(b('b7') <= 1511.0) ? " + 
"(b('b4') <= 1170.0) ? " + 
"0.1388920216538509" + 
":  " + 
"0.1588851416896189" + 
":  " + 
"(b('b6') <= 3118.5) ? " + 
"0.008404813906350901" + 
":  " + 
"0.0005746025256134168" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 892.25) ? " + 
"(b('b6') <= 3223.5) ? " + 
"(b('moss') <= 19.819469451904297) ? " + 
"-0.00028893916711568115" + 
":  " + 
"-0.02059737709053733" + 
":  " + 
"(b('g0vv') <= -8.58899211883545) ? " + 
"-0.016897087158325788" + 
":  " + 
"0.08409205096233789" + 
":  " + 
"(b('b6') <= 2707.5) ? " + 
"(b('bare') <= 14.027758121490479) ? " + 
"0.009730739876595973" + 
":  " + 
"-0.013254921768587192" + 
":  " + 
"(b('b4') <= 987.5) ? " + 
"0.016075740404994033" + 
":  " + 
"-0.0004035272595530477" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2785.5) ? " + 
"(b('trees') <= 18.005227088928223) ? " + 
"(b('trees') <= 13.571214199066162) ? " + 
"0.000520261091753304" + 
":  " + 
"-0.012712888618939893" + 
":  " + 
"(b('crop') <= 11.22841739654541) ? " + 
"-0.0038546004184476833" + 
":  " + 
"0.02894249889861685" + 
":  " + 
"(b('moss') <= 13.542709827423096) ? " + 
"(b('moss') <= 9.993216514587402) ? " + 
"-0.001957149598390636" + 
":  " + 
"0.011838090358386897" + 
":  " + 
"(b('moss') <= 15.907952785491943) ? " + 
"-0.018767152874114165" + 
":  " + 
"0.011445147367252963" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1039.5) ? " + 
"(b('b6') <= 3365.5) ? " + 
"(b('b3') <= 1029.5) ? " + 
"8.136591324199508e-05" + 
":  " + 
"-0.034644607244210854" + 
":  " + 
"(b('b4') <= 1205.0) ? " + 
"-0.02675911183211173" + 
":  " + 
"-0.0034957168488407723" + 
":  " + 
"(b('l8dt') <= 2833.5) ? " + 
"(b('b3') <= 1223.0) ? " + 
"0.11497383398382081" + 
":  " + 
"-0.047254973026255614" + 
":  " + 
"(b('b2') <= 526.0) ? " + 
"-0.055506143405578634" + 
":  " + 
"0.0011984784117899353" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 801.5) ? " + 
"(b('b2') <= 536.5) ? " + 
"(b('crop') <= 47.92914390563965) ? " + 
"0.002676915297697787" + 
":  " + 
"-0.004191529956172494" + 
":  " + 
"(b('b5') <= 2745.5) ? " + 
"-0.013963779798986291" + 
":  " + 
"-0.08388441777785499" + 
":  " + 
"(b('b5') <= 1842.0) ? " + 
"(b('lia') <= 42.73221206665039) ? " + 
"0.006824995366349813" + 
":  " + 
"0.07952230836817413" + 
":  " + 
"(b('b6') <= 2000.0) ? " + 
"0.01895946709591874" + 
":  " + 
"0.00021263383627593822" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 259.5) ? " + 
"(b('b4') <= 732.0) ? " + 
"(b('b3') <= 705.5) ? " + 
"-0.0005827927814085974" + 
":  " + 
"0.02643104688885422" + 
":  " + 
"(b('moss') <= 25.54065704345703) ? " + 
"-0.017015851698477788" + 
":  " + 
"-0.11066607251691472" + 
":  " + 
"(b('b4') <= 463.5) ? " + 
"(b('b6') <= 1672.5) ? " + 
"0.11564898533747436" + 
":  " + 
"0.1297949097263708" + 
":  " + 
"(b('b2') <= 347.5) ? " + 
"-0.015456814356031159" + 
":  " + 
"0.0003624281321034975" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.869969367980957) ? " + 
"(b('trees') <= 7.314132928848267) ? " + 
"(b('g0vh') <= -19.94096279144287) ? " + 
"-0.0019294047301529388" + 
":  " + 
"0.04087574144993593" + 
":  " + 
"(b('b3') <= 566.0) ? " + 
"-0.06910935704326977" + 
":  " + 
"-0.01554046881054136" + 
":  " + 
"(b('b5') <= 1813.0) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"0.004147267720743403" + 
":  " + 
"0.1420947119380116" + 
":  " + 
"(b('l8dt') <= 8076292.5) ? " + 
"-9.251145744926264e-05" + 
":  " + 
"0.036454204067570425" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('urban') <= 3.522911548614502) ? " + 
"(b('ndvi') <= 5229.5) ? " + 
"0.0005989447013020269" + 
":  " + 
"-0.006235253151266477" + 
":  " + 
"(b('ndvi') <= 2064.0) ? " + 
"0.11302341073312892" + 
":  " + 
"0.07441246958745956" + 
":  " + 
"(b('b5') <= 4200.0) ? " + 
"(b('b6') <= 2286.5) ? " + 
"0.004125581774222284" + 
":  " + 
"-0.004623650273573627" + 
":  " + 
"(b('g0vv') <= -9.41433334350586) ? " + 
"0.10682142114759158" + 
":  " + 
"0.033864191848226255" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('b3') <= 724.5) ? " + 
"(b('trees') <= 12.304713249206543) ? " + 
"0.0014514075911495387" + 
":  " + 
"-0.008327945620024887" + 
":  " + 
"(b('b1') <= 413.5) ? " + 
"-0.03678701632152046" + 
":  " + 
"0.20226634834884374" + 
":  " + 
"(b('b6') <= 2210.0) ? " + 
"(b('b2') <= 631.0) ? " + 
"0.011632584956908325" + 
":  " + 
"-0.02729309263081555" + 
":  " + 
"(b('b7') <= 1651.5) ? " + 
"-0.003849371621829288" + 
":  " + 
"0.0007216893610411354" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('b10') <= 1243.5) ? " + 
"(b('b6') <= 2219.5) ? " + 
"0.0004971535295020422" + 
":  " + 
"-0.023823981577862256" + 
":  " + 
"(b('b4') <= 592.5) ? " + 
"0.018142497979577916" + 
":  " + 
"4.113906415871032e-05" + 
":  " + 
"(b('g0vh') <= -18.530378341674805) ? " + 
"(b('g0vh') <= -18.599775314331055) ? " + 
"0.03210214074477035" + 
":  " + 
"0.1333985178673867" + 
":  " + 
"(b('lia') <= 34.12309455871582) ? " + 
"-0.04226407383593862" + 
":  " + 
"0.01533310423513483" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -10.188087463378906) ? " + 
"(b('crop') <= 89.04487609863281) ? " + 
"(b('crop') <= 85.84851455688477) ? " + 
"-0.00022360831532123175" + 
":  " + 
"0.010299219944177046" + 
":  " + 
"(b('ndvi') <= 3652.0) ? " + 
"0.000362645580563872" + 
":  " + 
"-0.01737730606185818" + 
":  " + 
"(b('ndvi') <= 3436.0) ? " + 
"-0.0985969333013702" + 
":  " + 
"(b('b4') <= 893.5) ? " + 
"-0.010395843472945698" + 
":  " + 
"-0.018743132213008717" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 43.71040153503418) ? " + 
"(b('lia') <= 43.592063903808594) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"-0.00029499394851608123" + 
":  " + 
"0.008073072467258595" + 
":  " + 
"(b('grass') <= 98.10429382324219) ? " + 
"-0.0021856552559817483" + 
":  " + 
"-0.05745700571269352" + 
":  " + 
"(b('ndvi') <= 6586.5) ? " + 
"(b('ndvi') <= 1134.5) ? " + 
"-0.012318756355542469" + 
":  " + 
"0.006109047378685144" + 
":  " + 
"(b('g0vv') <= -12.697579860687256) ? " + 
"0.1608967237474613" + 
":  " + 
"0.06264320863118884" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 9.947502613067627) ? " + 
"(b('bare') <= 9.127102851867676) ? " + 
"(b('b5') <= 2184.5) ? " + 
"0.0028263084464709514" + 
":  " + 
"-0.0006965755042527286" + 
":  " + 
"(b('b5') <= 2547.0) ? " + 
"-0.00881589990635928" + 
":  " + 
"-0.03238099762568004" + 
":  " + 
"(b('crop') <= 52.3651237487793) ? " + 
"(b('g0vv') <= -6.204157114028931) ? " + 
"0.0016854440219699143" + 
":  " + 
"0.15750037677424036" + 
":  " + 
"(b('b4') <= 1035.5) ? " + 
"0.03043821050579637" + 
":  " + 
"0.0661039438355347" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 829.5) ? " + 
"(b('b7') <= 3444.0) ? " + 
"(b('b5') <= 3518.0) ? " + 
"8.246394326468663e-05" + 
":  " + 
"-0.004570764274360484" + 
":  " + 
"(b('b11') <= 3496.5) ? " + 
"0.02634561528897951" + 
":  " + 
"0.0053299467038008365" + 
":  " + 
"(b('b2') <= 990.0) ? " + 
"(b('b6') <= 2952.0) ? " + 
"0.15547271972058946" + 
":  " + 
"-0.02011936643023215" + 
":  " + 
"(b('ndvi') <= 3598.0) ? " + 
"0.0014612292487931648" + 
":  " + 
"0.039648311672386756" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.928560256958008) ? " + 
"(b('crop') <= 87.21756744384766) ? " + 
"(b('crop') <= 85.4493522644043) ? " + 
"-0.0029343930478428083" + 
":  " + 
"-0.051541959916746004" + 
":  " + 
"(b('l8dt') <= 49607.0) ? " + 
"0.21618903963318387" + 
":  " + 
"0.0249690221539169" + 
":  " + 
"(b('grass') <= 34.49201011657715) ? " + 
"(b('trees') <= 14.932132720947266) ? " + 
"-0.0012738751549243265" + 
":  " + 
"0.010035270345582806" + 
":  " + 
"(b('crop') <= 39.048561096191406) ? " + 
"-0.00033941036615292634" + 
":  " + 
"0.018833388026388793" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 593.5) ? " + 
"(b('b5') <= 2961.0) ? " + 
"(b('b5') <= 2630.0) ? " + 
"-0.006817591326413843" + 
":  " + 
"0.023017532950287484" + 
":  " + 
"(b('b7') <= 1008.5) ? " + 
"-0.05383414964131663" + 
":  " + 
"-0.1342945697755718" + 
":  " + 
"(b('b4') <= 520.5) ? " + 
"(b('grass') <= 11.245258808135986) ? " + 
"0.10130261048458562" + 
":  " + 
"-0.00565329619927725" + 
":  " + 
"(b('b4') <= 533.5) ? " + 
"-0.0440463559821684" + 
":  " + 
"0.00019224218604460363" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 181.0) ? " + 
"(b('g0vv') <= -12.663116455078125) ? " + 
"(b('l8dt') <= 518406.0) ? " + 
"0.029954963429265374" + 
":  " + 
"0.08229172536288164" + 
":  " + 
"(b('g0vv') <= -9.463024616241455) ? " + 
"0.0019143704361165124" + 
":  " + 
"0.05513450983818125" + 
":  " + 
"(b('b2') <= 229.0) ? " + 
"(b('lia') <= 30.674999237060547) ? " + 
"0.13153612603560966" + 
":  " + 
"-0.034453046057095135" + 
":  " + 
"(b('b2') <= 241.5) ? " + 
"0.028631858371659456" + 
":  " + 
"-2.0635682286558663e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('trees') <= 10.145288467407227) ? " + 
"(b('g0vh') <= -21.9964542388916) ? " + 
"0.007934881978596627" + 
":  " + 
"-0.0037266311035844745" + 
":  " + 
"(b('crop') <= 1.4046242237091064) ? " + 
"-0.013177757678609231" + 
":  " + 
"0.007578628691204629" + 
":  " + 
"(b('bare') <= 0.3734448403120041) ? " + 
"(b('b11') <= 1662.5) ? " + 
"-0.006093670939607878" + 
":  " + 
"0.03627272956266493" + 
":  " + 
"(b('grass') <= 87.1015739440918) ? " + 
"0.0007391199454794026" + 
":  " + 
"-0.024616860188105816" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 34.498046875) ? " + 
"(b('moss') <= 19.819469451904297) ? " + 
"(b('moss') <= 16.90385627746582) ? " + 
"-0.0015840159596665626" + 
":  " + 
"0.024631260444490485" + 
":  " + 
"(b('b11') <= 1983.5) ? " + 
"-0.0922576291970811" + 
":  " + 
"-0.002729970799282249" + 
":  " + 
"(b('lia') <= 34.96562385559082) ? " + 
"(b('crop') <= 47.52532196044922) ? " + 
"0.00499166831910428" + 
":  " + 
"0.05136334882140322" + 
":  " + 
"(b('b3') <= 927.5) ? " + 
"-0.0014226275914088755" + 
":  " + 
"0.0016578198066810124" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.017068862915039) ? " + 
"(b('crop') <= 94.68265533447266) ? " + 
"(b('lia') <= 34.25613784790039) ? " + 
"-0.006264155123401677" + 
":  " + 
"-2.0634458621032306e-06" + 
":  " + 
"(b('crop') <= 95.60836410522461) ? " + 
"0.09863322964354189" + 
":  " + 
"0.010029135693281689" + 
":  " + 
"(b('grass') <= 30.423192024230957) ? " + 
"(b('b5') <= 2445.0) ? " + 
"0.004191704151933331" + 
":  " + 
"-0.002557872248168521" + 
":  " + 
"(b('grass') <= 31.69418716430664) ? " + 
"0.04196589963491285" + 
":  " + 
"0.004829779821998749" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 550.5) ? " + 
"(b('b3') <= 519.5) ? " + 
"(b('ndvi') <= 4992.0) ? " + 
"0.004303511698870033" + 
":  " + 
"-0.05697619984177579" + 
":  " + 
"(b('grass') <= 68.10729598999023) ? " + 
"-0.02918961517661253" + 
":  " + 
"0.07515267761506579" + 
":  " + 
"(b('b4') <= 485.5) ? " + 
"(b('l8dt') <= 1051052.0) ? " + 
"0.06493091298485856" + 
":  " + 
"-0.008714024276153642" + 
":  " + 
"(b('b5') <= 1472.0) ? " + 
"0.018775713041506874" + 
":  " + 
"-2.1608324781913234e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 24.395869255065918) ? " + 
"(b('b6') <= 3261.5) ? " + 
"(b('b7') <= 2411.5) ? " + 
"0.08981243602327252" + 
":  " + 
"0.13383628219937674" + 
":  " + 
"(b('g0vv') <= -14.644976615905762) ? " + 
"0.018101105280698422" + 
":  " + 
"-0.010822901964421964" + 
":  " + 
"(b('ndvi') <= 1306.5) ? " + 
"(b('b1') <= 436.0) ? " + 
"-0.02059868348551599" + 
":  " + 
"-0.0005699940261124048" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-5.2933448727082186e-06" + 
":  " + 
"0.0072676169140976875" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.063567638397217) ? " + 
"(b('l8dt') <= 4107531.0) ? " + 
"(b('l8dt') <= 343813.5) ? " + 
"0.0018485278386009066" + 
":  " + 
"-0.005527928310551298" + 
":  " + 
"(b('moss') <= 15.5) ? " + 
"0.03158438615138971" + 
":  " + 
"0.15710912220855006" + 
":  " + 
"(b('grass') <= 86.51207733154297) ? " + 
"(b('crop') <= 2.4269771575927734) ? " + 
"-0.0033422075125570604" + 
":  " + 
"0.0009387827604025005" + 
":  " + 
"(b('lia') <= 32.22800064086914) ? " + 
"0.0807193674833209" + 
":  " + 
"0.004718235257148804" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 666.5) ? " + 
"(b('b3') <= 656.5) ? " + 
"(b('b6') <= 2717.0) ? " + 
"-0.0028557076615130204" + 
":  " + 
"0.01620045686653446" + 
":  " + 
"(b('b2') <= 376.0) ? " + 
"-0.05901360248541091" + 
":  " + 
"-0.013281642787993831" + 
":  " + 
"(b('b10') <= 1043.0) ? " + 
"(b('b6') <= 1735.0) ? " + 
"0.0018585937266836277" + 
":  " + 
"0.048128052351140316" + 
":  " + 
"(b('b4') <= 520.5) ? " + 
"0.08107171011202527" + 
":  " + 
"0.00010603382523841362" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 259.5) ? " + 
"(b('b4') <= 732.0) ? " + 
"(b('ndvi') <= 5444.0) ? " + 
"0.0012396568139781859" + 
":  " + 
"0.06706311824066832" + 
":  " + 
"(b('urban') <= 9.834710597991943) ? " + 
"-0.01908823036904661" + 
":  " + 
"0.014083429226673752" + 
":  " + 
"(b('b4') <= 463.5) ? " + 
"(b('b6') <= 1575.0) ? " + 
"0.09563391728811355" + 
":  " + 
"0.1116620868740954" + 
":  " + 
"(b('b3') <= 562.5) ? " + 
"-0.016480035487515317" + 
":  " + 
"0.0003158427589670508" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 1031.5) ? " + 
"(b('b3') <= 1763.5) ? " + 
"(b('b1') <= 842.0) ? " + 
"-0.00035865747118119147" + 
":  " + 
"0.0424410109258441" + 
":  " + 
"(b('l8dt') <= 929376.0) ? " + 
"0.11285564235578849" + 
":  " + 
"0.04027945107368826" + 
":  " + 
"(b('b4') <= 1966.5) ? " + 
"(b('b6') <= 3309.0) ? " + 
"-0.003967447521787083" + 
":  " + 
"0.04370065135117763" + 
":  " + 
"(b('g0vh') <= -18.05737018585205) ? " + 
"0.002874066862218022" + 
":  " + 
"-0.010589940231871231" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5439.0) ? " + 
"(b('b4') <= 2644.5) ? " + 
"(b('ndvi') <= 1312.0) ? " + 
"-0.0026952417570198337" + 
":  " + 
"0.0003168595870646554" + 
":  " + 
"(b('b1') <= 987.5) ? " + 
"0.04676307898408168" + 
":  " + 
"0.0032124005570397453" + 
":  " + 
"(b('g0vh') <= -21.055819511413574) ? " + 
"(b('b2') <= 2062.75) ? " + 
"0.009916333312516713" + 
":  " + 
"-0.00810848301559803" + 
":  " + 
"(b('l8dt') <= 942151.5) ? " + 
"-0.018922738011793505" + 
":  " + 
"-0.03283598222946901" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('trees') <= 10.145288467407227) ? " + 
"(b('g0vh') <= -21.9964542388916) ? " + 
"0.007181185180777022" + 
":  " + 
"-0.0034696994321559314" + 
":  " + 
"(b('b4') <= 1705.0) ? " + 
"0.00254309622595618" + 
":  " + 
"0.07400928816816067" + 
":  " + 
"(b('bare') <= 0.3734448403120041) ? " + 
"(b('g0vv') <= -11.470760345458984) ? " + 
"0.07225373145527836" + 
":  " + 
"0.009208258267321462" + 
":  " + 
"(b('ndvi') <= 3464.5) ? " + 
"-0.0005708507731842706" + 
":  " + 
"0.005705684985228805" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.883069038391113) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"(b('b2') <= 414.5) ? " + 
"-0.03152844413283301" + 
":  " + 
"-0.0054395820876759395" + 
":  " + 
"(b('lia') <= 43.92072105407715) ? " + 
"0.008356615794864387" + 
":  " + 
"-0.06296694139713105" + 
":  " + 
"(b('lia') <= 44.273521423339844) ? " + 
"(b('lia') <= 44.130767822265625) ? " + 
"9.034049335566182e-05" + 
":  " + 
"-0.029722467231517006" + 
":  " + 
"(b('b6') <= 2937.0) ? " + 
"0.026891150586392933" + 
":  " + 
"-0.003347934086140689" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5229.5) ? " + 
"(b('ndvi') <= 5170.0) ? " + 
"(b('b4') <= 729.5) ? " + 
"0.002886065488935254" + 
":  " + 
"-0.000398758962005066" + 
":  " + 
"(b('b3') <= 988.0) ? " + 
"0.006552768073142861" + 
":  " + 
"0.14390308331973836" + 
":  " + 
"(b('ndvi') <= 5724.0) ? " + 
"(b('b5') <= 3749.0) ? " + 
"-0.022895638931274546" + 
":  " + 
"0.02781144765859049" + 
":  " + 
"(b('b6') <= 2393.0) ? " + 
"-0.011896580619428703" + 
":  " + 
"0.013135305829978633" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3450.5) ? " + 
"(b('moss') <= 22.977157592773438) ? " + 
"-5.7520149031669755e-05" + 
":  " + 
"0.010793128423311937" + 
":  " + 
"(b('b5') <= 3455.5) ? " + 
"0.045907033264588976" + 
":  " + 
"0.006071601188728179" + 
":  " + 
"(b('b5') <= 3525.5) ? " + 
"(b('moss') <= 2.838971436023712) ? " + 
"-0.0550727424553191" + 
":  " + 
"0.004848729279908354" + 
":  " + 
"(b('grass') <= 74.57086563110352) ? " + 
"-0.00195350907769697" + 
":  " + 
"0.05486230402182227" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 66.14077377319336) ? " + 
"(b('crop') <= 62.66942024230957) ? " + 
"(b('b1') <= 372.5) ? " + 
"0.00291144395301973" + 
":  " + 
"-0.0009805017581074158" + 
":  " + 
"(b('crop') <= 63.26685333251953) ? " + 
"-0.04119836610335822" + 
":  " + 
"-0.007753667739278872" + 
":  " + 
"(b('trees') <= 11.215232372283936) ? " + 
"(b('b5') <= 2876.5) ? " + 
"0.004742602613425062" + 
":  " + 
"-0.002630517638928624" + 
":  " + 
"(b('b6') <= 2675.5) ? " + 
"0.06672674075442873" + 
":  " + 
"-0.0013931153821885945" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('moss') <= 5.641550540924072) ? " + 
"(b('ndvi') <= 4287.0) ? " + 
"-0.002559497317639199" + 
":  " + 
"-0.021835226688944016" + 
":  " + 
"(b('moss') <= 7.011075973510742) ? " + 
"0.027842093698591187" + 
":  " + 
"-0.0012672223905034338" + 
":  " + 
"(b('b6') <= 2210.0) ? " + 
"(b('b6') <= 2183.5) ? " + 
"0.004949628916797602" + 
":  " + 
"0.04766602718603996" + 
":  " + 
"(b('b7') <= 1651.5) ? " + 
"-0.003493612545426527" + 
":  " + 
"0.0006935568184827124" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 2906.5) ? " + 
"(b('b10') <= 2889.5) ? " + 
"(b('bare') <= 14.846899032592773) ? " + 
"2.9256676988022217e-05" + 
":  " + 
"-0.007446645992854548" + 
":  " + 
"(b('bare') <= 2.0335646867752075) ? " + 
"-0.0350825961088957" + 
":  " + 
"0.001890514763963953" + 
":  " + 
"(b('b7') <= 2910.0) ? " + 
"(b('ndvi') <= 1344.0) ? " + 
"0.05192283902765825" + 
":  " + 
"-0.0005254857779530591" + 
":  " + 
"(b('b5') <= 2287.5) ? " + 
"-0.015258957025727061" + 
":  " + 
"0.0022212466783119843" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 384.5) ? " + 
"(b('bare') <= 19.278925895690918) ? " + 
"(b('b4') <= 620.5) ? " + 
"0.0027973515780477815" + 
":  " + 
"-0.006070119060310779" + 
":  " + 
"(b('g0vh') <= -16.86211585998535) ? " + 
"-0.18060978514892256" + 
":  " + 
"-0.07998617859952334" + 
":  " + 
"(b('b4') <= 743.5) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"-0.0019161189068308247" + 
":  " + 
"0.019011099107948334" + 
":  " + 
"(b('b4') <= 751.5) ? " + 
"-0.028951880396931074" + 
":  " + 
"1.5136262783275384e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 630.5) ? " + 
"(b('b3') <= 627.5) ? " + 
"(b('b5') <= 2630.0) ? " + 
"-0.005403327110869797" + 
":  " + 
"0.01181492735456994" + 
":  " + 
"(b('g0vh') <= -21.807061195373535) ? " + 
"0.1252909397741071" + 
":  " + 
"-0.04097256893657109" + 
":  " + 
"(b('b3') <= 645.5) ? " + 
"(b('b5') <= 2730.5) ? " + 
"0.02920093899391437" + 
":  " + 
"-0.020822210103602235" + 
":  " + 
"(b('b3') <= 665.5) ? " + 
"-0.01545235030092063" + 
":  " + 
"0.0002716845046788677" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.017068862915039) ? " + 
"(b('grass') <= 11.09217882156372) ? " + 
"(b('l8dt') <= 72383.0) ? " + 
"0.02081222226353447" + 
":  " + 
"0.002745167151373895" + 
":  " + 
"(b('crop') <= 76.58172988891602) ? " + 
"-0.0013070353095166215" + 
":  " + 
"-0.020451023794981572" + 
":  " + 
"(b('grass') <= 30.423192024230957) ? " + 
"(b('b5') <= 2445.0) ? " + 
"0.0040866824708217595" + 
":  " + 
"-0.002305041068148099" + 
":  " + 
"(b('grass') <= 70.43687057495117) ? " + 
"0.010225474930933818" + 
":  " + 
"-0.003893953096774267" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('b3') <= 721.5) ? " + 
"(b('moss') <= 5.641550540924072) ? " + 
"-0.005433384675653482" + 
":  " + 
"0.003434350334610536" + 
":  " + 
"(b('b4') <= 661.5) ? " + 
"0.0320418407288681" + 
":  " + 
"-0.02947656476524125" + 
":  " + 
"(b('b4') <= 697.5) ? " + 
"(b('b5') <= 3381.0) ? " + 
"0.030093376853707283" + 
":  " + 
"-0.00903710855885848" + 
":  " + 
"(b('urban') <= 36.35346794128418) ? " + 
"0.00036201802997454095" + 
":  " + 
"-0.01192265408618052" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 12.501765251159668) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"(b('b7') <= 1991.5) ? " + 
"-0.0019312272113350317" + 
":  " + 
"0.0012985494773111019" + 
":  " + 
"(b('g0vv') <= -9.744638442993164) ? " + 
"0.008597736463727544" + 
":  " + 
"0.05010893245796527" + 
":  " + 
"(b('b1') <= 407.5) ? " + 
"(b('b3') <= 755.5) ? " + 
"-0.005057887235904516" + 
":  " + 
"0.015434352478240747" + 
":  " + 
"(b('b2') <= 482.5) ? " + 
"-0.05972845582952357" + 
":  " + 
"-0.006441410581824614" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 19.819469451904297) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('moss') <= 18.02293586730957) ? " + 
"0.00016881792095160069" + 
":  " + 
"-0.012744518285796426" + 
":  " + 
"(b('g0vv') <= -13.614131927490234) ? " + 
"0.010678457456830761" + 
":  " + 
"0.06818249547484612" + 
":  " + 
"(b('moss') <= 20.664283752441406) ? " + 
"(b('l8dt') <= 1214339.5) ? " + 
"-0.08554354570247119" + 
":  " + 
"-0.05081620073432823" + 
":  " + 
"(b('b4') <= 1183.0) ? " + 
"0.023038597402417652" + 
":  " + 
"-0.007681884059076158" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 19.15903377532959) ? " + 
"(b('trees') <= 18.062620162963867) ? " + 
"-0.00013349580006621117" + 
":  " + 
"0.029716998451452835" + 
":  " + 
"(b('moss') <= 0.9972507357597351) ? " + 
"-0.04214872189266688" + 
":  " + 
"0.0002218332630530373" + 
":  " + 
"(b('b1') <= 464.0) ? " + 
"(b('b5') <= 2808.0) ? " + 
"0.008493743137820113" + 
":  " + 
"0.05921225751150345" + 
":  " + 
"(b('lia') <= 39.0131721496582) ? " + 
"0.004504624031400277" + 
":  " + 
"-0.04055649822584213" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 6.115110635757446) ? " + 
"(b('trees') <= 5.304356098175049) ? " + 
"(b('trees') <= 4.276387691497803) ? " + 
"-0.0003531371495216139" + 
":  " + 
"0.00776838001318814" + 
":  " + 
"(b('ndvi') <= 5550.5) ? " + 
"0.02383640521366445" + 
":  " + 
"0.2329159603715507" + 
":  " + 
"(b('ndvi') <= 2728.5) ? " + 
"(b('lia') <= 32.63880920410156) ? " + 
"0.013053805313203378" + 
":  " + 
"-0.0005139882888435524" + 
":  " + 
"(b('grass') <= 5.139582395553589) ? " + 
"-0.030088671389888102" + 
":  " + 
"-0.002719826222788557" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2847.5) ? " + 
"(b('b6') <= 2841.5) ? " + 
"(b('b6') <= 2829.5) ? " + 
"0.0008801259934742394" + 
":  " + 
"-0.01590148806238758" + 
":  " + 
"(b('grass') <= 7.744230508804321) ? " + 
"0.08741380151318306" + 
":  " + 
"0.015550732366757594" + 
":  " + 
"(b('b7') <= 1592.0) ? " + 
"(b('b10') <= 1583.5) ? " + 
"-0.023337234396203256" + 
":  " + 
"-0.08134242114101262" + 
":  " + 
"(b('b1') <= 398.5) ? " + 
"0.012228312694263664" + 
":  " + 
"-0.001297387820228603" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 1031.5) ? " + 
"(b('b3') <= 1763.5) ? " + 
"(b('b2') <= 1000.5) ? " + 
"-0.00010829717261724893" + 
":  " + 
"-0.01109540924770135" + 
":  " + 
"(b('ndvi') <= 2935.5) ? " + 
"0.034337106084388794" + 
":  " + 
"0.09997090560421877" + 
":  " + 
"(b('b2') <= 1043.5) ? " + 
"(b('ndvi') <= 2458.0) ? " + 
"0.02089973520352115" + 
":  " + 
"0.12622255349470218" + 
":  " + 
"(b('b3') <= 1546.0) ? " + 
"0.023273646106373027" + 
":  " + 
"0.0004034207344871448" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b2') <= 832.5) ? " + 
"(b('b3') <= 1222.5) ? " + 
"0.0024750444035160565" + 
":  " + 
"0.03706035248234148" + 
":  " + 
"(b('b3') <= 1477.5) ? " + 
"-0.018529756622198412" + 
":  " + 
"0.0011076821679277616" + 
":  " + 
"(b('b1') <= 663.5) ? " + 
"(b('grass') <= 3.1685575246810913) ? " + 
"-0.013518590119823284" + 
":  " + 
"-0.0005744779213598124" + 
":  " + 
"(b('b4') <= 1987.5) ? " + 
"0.006729844030081654" + 
":  " + 
"-0.0010302587231776192" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 66.14077377319336) ? " + 
"(b('crop') <= 62.66942024230957) ? " + 
"(b('b4') <= 924.5) ? " + 
"0.0023277674175504084" + 
":  " + 
"-0.001329237359505797" + 
":  " + 
"(b('crop') <= 63.26685333251953) ? " + 
"-0.03691397055415301" + 
":  " + 
"-0.006710270662222105" + 
":  " + 
"(b('crop') <= 76.58172988891602) ? " + 
"(b('b2') <= 448.0) ? " + 
"-0.006489811152337253" + 
":  " + 
"0.01615065177999681" + 
":  " + 
"(b('grass') <= 11.09217882156372) ? " + 
"0.0007731341002946931" + 
":  " + 
"-0.01049327388917132" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b10') <= 2906.5) ? " + 
"(b('b6') <= 4272.5) ? " + 
"(b('b11') <= 2889.5) ? " + 
"-0.0001942104075952789" + 
":  " + 
"-0.018898743844146963" + 
":  " + 
"(b('l8dt') <= 734644.5) ? " + 
"-0.01618080658120256" + 
":  " + 
"-0.04849004031410184" + 
":  " + 
"(b('b10') <= 2910.0) ? " + 
"(b('b5') <= 2708.5) ? " + 
"0.04319352420684371" + 
":  " + 
"-0.01437971943922435" + 
":  " + 
"(b('trees') <= 22.12039089202881) ? " + 
"0.001368924413976412" + 
":  " + 
"0.034501750905979366" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('ndvi') <= 1646.5) ? " + 
"-0.002094197491662409" + 
":  " + 
"0.0010286708006780204" + 
":  " + 
"(b('l8dt') <= 1878917.0) ? " + 
"0.014517962402382645" + 
":  " + 
"0.06983398177965287" + 
":  " + 
"(b('ndvi') <= 2772.0) ? " + 
"(b('trees') <= 13.039640426635742) ? " + 
"-0.0009475817735225303" + 
":  " + 
"0.018811632493296333" + 
":  " + 
"(b('moss') <= 15.907952785491943) ? " + 
"-0.01737499241512141" + 
":  " + 
"0.008845279485997" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 12.501765251159668) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"(b('b7') <= 1991.5) ? " + 
"-0.0017572509751283077" + 
":  " + 
"0.001294477514300931" + 
":  " + 
"(b('g0vv') <= -9.744638442993164) ? " + 
"0.007110048136000044" + 
":  " + 
"0.04368415996709397" + 
":  " + 
"(b('b1') <= 407.5) ? " + 
"(b('ndvi') <= 2799.5) ? " + 
"0.016714160593871014" + 
":  " + 
"-0.0031823338457467295" + 
":  " + 
"(b('b2') <= 482.5) ? " + 
"-0.053217924325604134" + 
":  " + 
"-0.005955488355317092" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 19.819469451904297) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('moss') <= 18.02293586730957) ? " + 
"0.00017139580020528625" + 
":  " + 
"-0.012154123844982916" + 
":  " + 
"(b('g0vv') <= -13.614131927490234) ? " + 
"0.009622010140360111" + 
":  " + 
"0.06110679587533184" + 
":  " + 
"(b('moss') <= 20.664283752441406) ? " + 
"(b('g0vh') <= -16.90404224395752) ? " + 
"-0.07335076098672855" + 
":  " + 
"0.005928164306879508" + 
":  " + 
"(b('b4') <= 1183.0) ? " + 
"0.020279025925111743" + 
":  " + 
"-0.0071642332298541235" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 73.84134292602539) ? " + 
"(b('ndvi') <= 1137.5) ? " + 
"(b('crop') <= 99.63687133789062) ? " + 
"-0.00467895581970328" + 
":  " + 
"0.039948162279717626" + 
":  " + 
"(b('lia') <= 43.72114372253418) ? " + 
"-0.00011634957948311837" + 
":  " + 
"0.005486713423378376" + 
":  " + 
"(b('b10') <= 3925.5) ? " + 
"(b('lia') <= 43.83162307739258) ? " + 
"0.021845128959656516" + 
":  " + 
"-0.010965969498513202" + 
":  " + 
"(b('g0vh') <= -22.322280883789062) ? " + 
"-0.016665030731825636" + 
":  " + 
"0.0016957707883437203" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 6.115110635757446) ? " + 
"(b('trees') <= 5.304356098175049) ? " + 
"(b('lia') <= 38.013858795166016) ? " + 
"-0.0017875802064836052" + 
":  " + 
"0.002126628263716614" + 
":  " + 
"(b('ndvi') <= 5550.5) ? " + 
"0.02132639731961839" + 
":  " + 
"0.20945862693882322" + 
":  " + 
"(b('g0vh') <= -21.235203742980957) ? " + 
"(b('lia') <= 44.01401710510254) ? " + 
"-0.008715089801265534" + 
":  " + 
"-0.10150808552631448" + 
":  " + 
"(b('bare') <= 14.255455017089844) ? " + 
"-0.0005567713684384073" + 
":  " + 
"0.052258550775769956" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 41.06464767456055) ? " + 
"(b('lia') <= 40.042823791503906) ? " + 
"(b('trees') <= 12.510594367980957) ? " + 
"0.0005550718484727201" + 
":  " + 
"-0.003989623354249732" + 
":  " + 
"(b('moss') <= 0.044692736119031906) ? " + 
"0.034317853461411786" + 
":  " + 
"0.002435248935763903" + 
":  " + 
"(b('trees') <= 15.104385375976562) ? " + 
"(b('trees') <= 12.489027976989746) ? " + 
"-0.0016257614917546141" + 
":  " + 
"-0.013411962842434197" + 
":  " + 
"(b('trees') <= 19.091548919677734) ? " + 
"0.022516773593147743" + 
":  " + 
"0.0016343850178943582" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 666.5) ? " + 
"(b('b3') <= 656.5) ? " + 
"(b('b2') <= 462.5) ? " + 
"-0.002550148152212682" + 
":  " + 
"0.019921958591368184" + 
":  " + 
"(b('b2') <= 376.0) ? " + 
"-0.050474113973296826" + 
":  " + 
"-0.010212514877563398" + 
":  " + 
"(b('b1') <= 153.5) ? " + 
"(b('urban') <= 6.077227592468262) ? " + 
"0.10229709719413271" + 
":  " + 
"0.046870257341796825" + 
":  " + 
"(b('b6') <= 1518.0) ? " + 
"-0.033225781318095636" + 
":  " + 
"0.0002872917815833134" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1324.0) ? " + 
"(b('l8dt') <= 690921.0) ? " + 
"(b('b6') <= 2003.5) ? " + 
"0.0016556950299721819" + 
":  " + 
"0.08020836641870754" + 
":  " + 
"(b('lia') <= 34.007442474365234) ? " + 
"0.002106624032758223" + 
":  " + 
"-0.041864159773907325" + 
":  " + 
"(b('b5') <= 1405.5) ? " + 
"(b('urban') <= 0.0903225839138031) ? " + 
"0.03901955767958092" + 
":  " + 
"-0.0021458111342947186" + 
":  " + 
"(b('b2') <= 135.0) ? " + 
"0.05068239528490732" + 
":  " + 
"-2.972619314281254e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 20.289265632629395) ? " + 
"(b('trees') <= 19.831669807434082) ? " + 
"-3.331318349574765e-05" + 
":  " + 
"0.017279450799190237" + 
":  " + 
"(b('moss') <= 2.303693011403084) ? " + 
"-0.04259606566937288" + 
":  " + 
"-0.0020429365063216426" + 
":  " + 
"(b('b1') <= 464.0) ? " + 
"(b('b5') <= 2808.0) ? " + 
"0.0080589076067814" + 
":  " + 
"0.053760386700351805" + 
":  " + 
"(b('lia') <= 39.0131721496582) ? " + 
"0.005957069899888569" + 
":  " + 
"-0.0357755013689594" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.928560256958008) ? " + 
"(b('ndvi') <= 4859.5) ? " + 
"(b('g0vv') <= -14.966947555541992) ? " + 
"-0.0027139255375593237" + 
":  " + 
"-0.030337863735599102" + 
":  " + 
"(b('crop') <= 83.56213760375977) ? " + 
"0.02066450353007619" + 
":  " + 
"0.17576647684622912" + 
":  " + 
"(b('grass') <= 86.51207733154297) ? " + 
"(b('grass') <= 83.72659683227539) ? " + 
"0.00014166765139271936" + 
":  " + 
"-0.017042701233039758" + 
":  " + 
"(b('moss') <= 12.59807300567627) ? " + 
"0.0015546434668513294" + 
":  " + 
"0.05611111871703891" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 630.5) ? " + 
"(b('b4') <= 732.0) ? " + 
"(b('trees') <= 9.36296796798706) ? " + 
"0.005894020853776623" + 
":  " + 
"-0.007492425470485368" + 
":  " + 
"(b('grass') <= 75.0) ? " + 
"-0.013165077528305482" + 
":  " + 
"-0.07114721187652302" + 
":  " + 
"(b('b3') <= 645.5) ? " + 
"(b('ndvi') <= 3739.0) ? " + 
"0.023310605594922346" + 
":  " + 
"-0.03447640401705686" + 
":  " + 
"(b('b3') <= 664.5) ? " + 
"-0.013756895636850347" + 
":  " + 
"0.00025145751134452837" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2847.5) ? " + 
"(b('b6') <= 2841.5) ? " + 
"(b('b6') <= 2829.5) ? " + 
"0.0008653338518386999" + 
":  " + 
"-0.014082108536133309" + 
":  " + 
"(b('b11') <= 2229.5) ? " + 
"0.02256683692229226" + 
":  " + 
"0.1315307114630561" + 
":  " + 
"(b('b6') <= 2879.5) ? " + 
"(b('trees') <= 14.47687816619873) ? " + 
"-0.013142915847409026" + 
":  " + 
"-0.06611134425664231" + 
":  " + 
"(b('crop') <= 99.63687133789062) ? " + 
"-0.0004209887951141094" + 
":  " + 
"0.04202370461179065" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.43316370248794556) ? " + 
"(b('bare') <= 0.40279720723629) ? " + 
"(b('trees') <= 10.145288467407227) ? " + 
"-0.0018307354897634646" + 
":  " + 
"0.0033434068441572716" + 
":  " + 
"(b('b4') <= 849.5) ? " + 
"-0.10094187458613713" + 
":  " + 
"-0.020533069937588164" + 
":  " + 
"(b('bare') <= 0.4765203446149826) ? " + 
"(b('b10') <= 1618.5) ? " + 
"0.025773459044898955" + 
":  " + 
"0.15915902878539215" + 
":  " + 
"(b('crop') <= 94.83395767211914) ? " + 
"0.0006030408191940275" + 
":  " + 
"-0.05895588119166476" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3303668.5) ? " + 
"(b('trees') <= 33.60975933074951) ? " + 
"(b('lia') <= 40.82421112060547) ? " + 
"0.0004223103401231926" + 
":  " + 
"-0.0016551938760037584" + 
":  " + 
"(b('crop') <= 12.75460147857666) ? " + 
"-0.015322005127320917" + 
":  " + 
"0.02413151944956971" + 
":  " + 
"(b('ndvi') <= 2693.5) ? " + 
"(b('b6') <= 4860.5) ? " + 
"0.012252563633716336" + 
":  " + 
"-0.04007883853029999" + 
":  " + 
"(b('crop') <= 27.571112632751465) ? " + 
"-0.029555045268174956" + 
":  " + 
"0.0022021930933611086" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 801.5) ? " + 
"(b('b2') <= 536.5) ? " + 
"(b('grass') <= 99.8344841003418) ? " + 
"0.00048119634866341415" + 
":  " + 
"-0.015083607236160998" + 
":  " + 
"(b('b5') <= 2745.5) ? " + 
"-0.011804509995345365" + 
":  " + 
"-0.07377262393324648" + 
":  " + 
"(b('b4') <= 1037.5) ? " + 
"(b('grass') <= 74.02837753295898) ? " + 
"0.0011056085946249646" + 
":  " + 
"0.016428936074375268" + 
":  " + 
"(b('b3') <= 933.5) ? " + 
"-0.006796054964284471" + 
":  " + 
"0.00044321317500076987" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2436.5) ? " + 
"(b('moss') <= 1.6108241081237793) ? " + 
"(b('trees') <= 0.3455425687134266) ? " + 
"0.0011532163412845586" + 
":  " + 
"0.018031717943835967" + 
":  " + 
"(b('b5') <= 2379.5) ? " + 
"-0.002223148759903193" + 
":  " + 
"0.012163599332675811" + 
":  " + 
"(b('b5') <= 2462.5) ? " + 
"(b('trees') <= 17.931958198547363) ? " + 
"-0.008094261241034455" + 
":  " + 
"-0.05776113512026269" + 
":  " + 
"(b('urban') <= 36.35346794128418) ? " + 
"6.64157060038963e-05" + 
":  " + 
"-0.014167176818775846" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2050.5) ? " + 
"(b('b3') <= 1102.5) ? " + 
"(b('b4') <= 1237.5) ? " + 
"0.002791711730304364" + 
":  " + 
"-0.01926979642932559" + 
":  " + 
"(b('b4') <= 1544.5) ? " + 
"0.038907859362960935" + 
":  " + 
"-0.021477221655708267" + 
":  " + 
"(b('l8dt') <= 8154512.5) ? " + 
"(b('b2') <= 314.5) ? " + 
"0.007404772907799126" + 
":  " + 
"-0.0004947285131969402" + 
":  " + 
"(b('b6') <= 3973.0) ? " + 
"0.026765166834944027" + 
":  " + 
"0.05162972869415237" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 630.5) ? " + 
"(b('b3') <= 627.5) ? " + 
"(b('b5') <= 3292.0) ? " + 
"-0.0024581438850415412" + 
":  " + 
"0.06328791378817156" + 
":  " + 
"(b('g0vv') <= -15.527793407440186) ? " + 
"0.11472979172693999" + 
":  " + 
"-0.03439334394846014" + 
":  " + 
"(b('b3') <= 645.5) ? " + 
"(b('b4') <= 627.5) ? " + 
"0.04585995114648194" + 
":  " + 
"0.0070106060893075535" + 
":  " + 
"(b('b3') <= 664.5) ? " + 
"-0.012499296568439535" + 
":  " + 
"0.0002558642272278968" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 259.5) ? " + 
"(b('b4') <= 732.0) ? " + 
"(b('b3') <= 705.5) ? " + 
"-0.001222201677676154" + 
":  " + 
"0.021030310396110752" + 
":  " + 
"(b('moss') <= 25.54065704345703) ? " + 
"-0.012888700027826348" + 
":  " + 
"-0.10601212383489096" + 
":  " + 
"(b('b4') <= 463.5) ? " + 
"(b('g0vh') <= -15.666253566741943) ? " + 
"0.09997279199805098" + 
":  " + 
"0.08530172838899142" + 
":  " + 
"(b('b3') <= 562.5) ? " + 
"-0.014905163913288617" + 
":  " + 
"0.0002976456249278708" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 24.395869255065918) ? " + 
"(b('b6') <= 3261.5) ? " + 
"(b('b7') <= 2411.5) ? " + 
"0.07797117177377233" + 
":  " + 
"0.12105453215327466" + 
":  " + 
"(b('g0vv') <= -15.956379890441895) ? " + 
"0.038614989833695185" + 
":  " + 
"0.000102907406893842" + 
":  " + 
"(b('g0vv') <= -13.102720260620117) ? " + 
"(b('g0vh') <= -17.820756912231445) ? " + 
"-0.0020272396491988797" + 
":  " + 
"0.022111080881943097" + 
":  " + 
"(b('g0vv') <= -13.099620819091797) ? " + 
"0.07029120046005376" + 
":  " + 
"0.0004150690085783487" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 1031.5) ? " + 
"(b('b3') <= 1763.5) ? " + 
"(b('b4') <= 2271.5) ? " + 
"-0.00010501492486651242" + 
":  " + 
"-0.011132311480171018" + 
":  " + 
"(b('g0vh') <= -19.510889053344727) ? " + 
"0.02012414278815163" + 
":  " + 
"0.08281569066878065" + 
":  " + 
"(b('b4') <= 1966.5) ? " + 
"(b('b6') <= 3309.0) ? " + 
"-0.0038716586690092365" + 
":  " + 
"0.03694589287520694" + 
":  " + 
"(b('g0vv') <= -10.021070003509521) ? " + 
"0.003131737920227557" + 
":  " + 
"-0.007307248476388402" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2558.5) ? " + 
"(b('ndvi') <= 2547.0) ? " + 
"(b('ndvi') <= 2542.5) ? " + 
"0.0005335668074490266" + 
":  " + 
"-0.04839346994051172" + 
":  " + 
"(b('trees') <= 13.466797828674316) ? " + 
"0.02152842075092125" + 
":  " + 
"0.1348862801004382" + 
":  " + 
"(b('ndvi') <= 2599.5) ? " + 
"(b('b6') <= 2279.0) ? " + 
"0.02639566282493362" + 
":  " + 
"-0.02985775108084301" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-0.0007010183581005381" + 
":  " + 
"0.01979372249268108" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 87.20395278930664) ? " + 
"(b('grass') <= 80.30580139160156) ? " + 
"(b('grass') <= 78.23077011108398) ? " + 
"-0.00017215828671249917" + 
":  " + 
"0.022093934310248763" + 
":  " + 
"(b('g0vh') <= -19.21277141571045) ? " + 
"-0.011216228394777856" + 
":  " + 
"0.012521729408190541" + 
":  " + 
"(b('moss') <= 12.59807300567627) ? " + 
"(b('lia') <= 31.924128532409668) ? " + 
"0.036005139074117294" + 
":  " + 
"-0.0029510792637224745" + 
":  " + 
"(b('g0vh') <= -20.432751655578613) ? " + 
"0.00330424588899787" + 
":  " + 
"0.06038759553533603" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2708.5) ? " + 
"(b('b4') <= 1132.5) ? " + 
"(b('trees') <= 13.24367094039917) ? " + 
"0.0020270933349766556" + 
":  " + 
"0.018193218709076173" + 
":  " + 
"(b('b11') <= 2133.5) ? " + 
"-0.006376722386232909" + 
":  " + 
"0.0005998301300006931" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('bare') <= 6.56046462059021) ? " + 
"-0.0005847984471321578" + 
":  " + 
"-0.02039420102902589" + 
":  " + 
"(b('b4') <= 501.5) ? " + 
"-0.11869372979129836" + 
":  " + 
"0.025141016680430027" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.869969367980957) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"(b('b2') <= 414.5) ? " + 
"-0.02898481045604209" + 
":  " + 
"-0.00504202107358221" + 
":  " + 
"(b('ndvi') <= 1942.0) ? " + 
"-0.00731655843267528" + 
":  " + 
"0.01901426377574885" + 
":  " + 
"(b('g0vv') <= -15.865667343139648) ? " + 
"(b('b6') <= 2875.5) ? " + 
"0.14742464804671357" + 
":  " + 
"0.03445845273834115" + 
":  " + 
"(b('l8dt') <= 107312.5) ? " + 
"-0.0022820465444000006" + 
":  " + 
"0.0005064257147360016" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -20.81766700744629) ? " + 
"(b('l8dt') <= 423171.0) ? " + 
"(b('b5') <= 2442.5) ? " + 
"0.09438186161789205" + 
":  " + 
"0.06434382084595286" + 
":  " + 
"(b('b5') <= 1803.0) ? " + 
"0.008251185993775001" + 
":  " + 
"-0.009847741660658993" + 
":  " + 
"(b('g0vv') <= -16.97585391998291) ? " + 
"(b('grass') <= 93.87771987915039) ? " + 
"-0.013045271110546213" + 
":  " + 
"0.006988508256065455" + 
":  " + 
"(b('g0vv') <= -16.966025352478027) ? " + 
"0.05850500307289296" + 
":  " + 
"9.039515165016101e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -2.327260732650757) ? " + 
"(b('g0vv') <= -5.72271203994751) ? " + 
"(b('g0vh') <= -13.793797492980957) ? " + 
"-0.00017240203201717897" + 
":  " + 
"0.006404710575265537" + 
":  " + 
"(b('g0vv') <= -5.707797050476074) ? " + 
"0.08524238500387743" + 
":  " + 
"0.006687101205050707" + 
":  " + 
"(b('b4') <= 1155.0) ? " + 
"(b('b1') <= 606.5) ? " + 
"-0.04687352763047109" + 
":  " + 
"-0.05268789003618571" + 
":  " + 
"(b('lia') <= 36.67803382873535) ? " + 
"-0.034533242151141966" + 
":  " + 
"-0.023200628447367908" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 259.5) ? " + 
"(b('b4') <= 732.0) ? " + 
"(b('ndvi') <= 5444.0) ? " + 
"0.00034802112965393885" + 
":  " + 
"0.056272722974323855" + 
":  " + 
"(b('moss') <= 25.54065704345703) ? " + 
"-0.011815769417321511" + 
":  " + 
"-0.09563025985347673" + 
":  " + 
"(b('b4') <= 463.5) ? " + 
"(b('b2') <= 323.0) ? " + 
"0.07512149276121655" + 
":  " + 
"0.0901699784485212" + 
":  " + 
"(b('b2') <= 314.0) ? " + 
"0.04075584489081119" + 
":  " + 
"0.00015259647800813548" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 2990.5) ? " + 
"(b('b6') <= 3864.5) ? " + 
"(b('b5') <= 3381.5) ? " + 
"0.0005007295792834182" + 
":  " + 
"-0.003144401476436977" + 
":  " + 
"(b('b4') <= 1161.0) ? " + 
"-0.08003559669591559" + 
":  " + 
"-0.005112340396584685" + 
":  " + 
"(b('b10') <= 3001.5) ? " + 
"(b('lia') <= 37.63292121887207) ? " + 
"0.06434408758604881" + 
":  " + 
"0.018187832415895503" + 
":  " + 
"(b('b5') <= 2585.0) ? " + 
"-0.01779346319980915" + 
":  " + 
"0.002087926190951212" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('ndvi') <= 1646.5) ? " + 
"-0.0019420400264167376" + 
":  " + 
"0.0009878392218275358" + 
":  " + 
"(b('b5') <= 3026.5) ? " + 
"-0.0015425637227855294" + 
":  " + 
"0.03974564654286358" + 
":  " + 
"(b('bare') <= 10.456055164337158) ? " + 
"(b('g0vv') <= -9.696956634521484) ? " + 
"-0.005634463732072961" + 
":  " + 
"0.010543647363548273" + 
":  " + 
"(b('ndvi') <= 1284.0) ? " + 
"-0.0005016440639157883" + 
":  " + 
"0.021813931735071065" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1039.5) ? " + 
"(b('b6') <= 3365.5) ? " + 
"(b('b3') <= 1032.5) ? " + 
"0.00010458708275372887" + 
":  " + 
"-0.031177938419674322" + 
":  " + 
"(b('b10') <= 2124.0) ? " + 
"-0.031362114995043135" + 
":  " + 
"-0.0053209428039710455" + 
":  " + 
"(b('b4') <= 1354.5) ? " + 
"(b('b6') <= 3279.5) ? " + 
"0.003350454077926661" + 
":  " + 
"0.028472738427869168" + 
":  " + 
"(b('b7') <= 1680.5) ? " + 
"0.05137119957963773" + 
":  " + 
"-0.0003846213550912647" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 817.5) ? " + 
"(b('b4') <= 925.5) ? " + 
"(b('b4') <= 921.5) ? " + 
"-0.0005572341922961806" + 
":  " + 
"0.057360454510513616" + 
":  " + 
"(b('crop') <= 76.28434753417969) ? " + 
"-0.015813051312532692" + 
":  " + 
"0.015165802245721673" + 
":  " + 
"(b('b6') <= 2847.5) ? " + 
"(b('b11') <= 2606.0) ? " + 
"0.002821217876147747" + 
":  " + 
"0.07934998257756025" + 
":  " + 
"(b('b10') <= 1691.5) ? " + 
"-0.025828388037263096" + 
":  " + 
"-9.41593437267878e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 2906.5) ? " + 
"(b('bare') <= 14.846899032592773) ? " + 
"(b('bare') <= 9.947502613067627) ? " + 
"-0.00045219332740490943" + 
":  " + 
"0.011586477637350939" + 
":  " + 
"(b('g0vv') <= -6.204157114028931) ? " + 
"-0.007223116923776601" + 
":  " + 
"0.14222399289848803" + 
":  " + 
"(b('b11') <= 2927.5) ? " + 
"(b('b4') <= 2323.5) ? " + 
"0.022683502460499327" + 
":  " + 
"-0.03201330676210653" + 
":  " + 
"(b('b7') <= 2936.5) ? " + 
"-0.024748950238745494" + 
":  " + 
"0.001694681447269115" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5439.0) ? " + 
"(b('b4') <= 2644.5) ? " + 
"(b('b4') <= 2395.0) ? " + 
"4.808436922512494e-05" + 
":  " + 
"-0.0062028970183937255" + 
":  " + 
"(b('b4') <= 2669.5) ? " + 
"0.04041103947511049" + 
":  " + 
"0.002460173744904517" + 
":  " + 
"(b('g0vh') <= -21.055819511413574) ? " + 
"(b('lia') <= 38.14970779418945) ? " + 
"0.009244416716339895" + 
":  " + 
"-0.0037097428151763243" + 
":  " + 
"(b('g0vh') <= -18.41990852355957) ? " + 
"-0.022872718116371787" + 
":  " + 
"0.0011939584909297501" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5229.5) ? " + 
"(b('ndvi') <= 5170.0) ? " + 
"(b('l8dt') <= 4778442.0) ? " + 
"-6.10693714203543e-05" + 
":  " + 
"0.008449974710526985" + 
":  " + 
"(b('b2') <= 452.5) ? " + 
"0.007086544113651786" + 
":  " + 
"0.12604629937041867" + 
":  " + 
"(b('ndvi') <= 5724.0) ? " + 
"(b('b5') <= 4015.0) ? " + 
"-0.016717996384509545" + 
":  " + 
"0.08564660975390496" + 
":  " + 
"(b('grass') <= 46.00799369812012) ? " + 
"0.001374667737815686" + 
":  " + 
"0.059696052900647195" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 181.0) ? " + 
"(b('g0vv') <= -12.663116455078125) ? " + 
"(b('l8dt') <= 518406.0) ? " + 
"0.0223081262944394" + 
":  " + 
"0.06948120527607414" + 
":  " + 
"(b('g0vv') <= -9.463024616241455) ? " + 
"0.0012482915745445826" + 
":  " + 
"0.04970528063784165" + 
":  " + 
"(b('b3') <= 437.0) ? " + 
"(b('g0vh') <= -16.467368125915527) ? " + 
"-0.018633065305635844" + 
":  " + 
"-0.0688972708961457" + 
":  " + 
"(b('b1') <= 102.0) ? " + 
"-0.04419684309898612" + 
":  " + 
"4.413082458977919e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2050.5) ? " + 
"(b('b5') <= 2048.0) ? " + 
"(b('b1') <= 407.5) ? " + 
"-0.003343321796242309" + 
":  " + 
"0.0062602127822696686" + 
":  " + 
"(b('g0vv') <= -8.833160877227783) ? " + 
"0.11956998347859028" + 
":  " + 
"0.07673813314232765" + 
":  " + 
"(b('l8dt') <= 8154512.5) ? " + 
"(b('g0vv') <= -20.81766700744629) ? " + 
"0.06693394260597434" + 
":  " + 
"-0.0003243327614812875" + 
":  " + 
"(b('l8dt') <= 8368540.5) ? " + 
"0.06131927040229558" + 
":  " + 
"0.02745641276737335" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 19.819469451904297) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('moss') <= 19.465020179748535) ? " + 
"0.00010898783758354093" + 
":  " + 
"-0.020193796963223255" + 
":  " + 
"(b('g0vv') <= -13.614131927490234) ? " + 
"0.00688764145621608" + 
":  " + 
"0.05242514625498289" + 
":  " + 
"(b('grass') <= 70.92327880859375) ? " + 
"(b('b7') <= 2191.0) ? " + 
"0.018654043667418838" + 
":  " + 
"-0.007706464797730289" + 
":  " + 
"(b('b6') <= 2276.5) ? " + 
"0.05012943163618013" + 
":  " + 
"-0.05878809989003876" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 73.84134292602539) ? " + 
"(b('ndvi') <= 1291.0) ? " + 
"(b('b1') <= 436.0) ? " + 
"-0.017051333627550163" + 
":  " + 
"-0.0011323527503091235" + 
":  " + 
"(b('b1') <= 760.5) ? " + 
"-8.388453395263586e-05" + 
":  " + 
"0.005462571190724264" + 
":  " + 
"(b('b7') <= 2804.5) ? " + 
"(b('g0vh') <= -22.370686531066895) ? " + 
"0.12950394727949882" + 
":  " + 
"0.029048615977616238" + 
":  " + 
"(b('ndvi') <= 603.5) ? " + 
"0.07272972770129651" + 
":  " + 
"0.002273397533747325" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 4840.5) ? " + 
"(b('b4') <= 2652.0) ? " + 
"(b('b3') <= 1932.0) ? " + 
"3.813155255615692e-05" + 
":  " + 
"-0.00965152814597198" + 
":  " + 
"(b('b4') <= 2657.0) ? " + 
"0.06797726002817811" + 
":  " + 
"0.008438332112422847" + 
":  " + 
"(b('l8dt') <= 1104001.5) ? " + 
"(b('g0vv') <= -8.654120922088623) ? " + 
"0.006465014313965521" + 
":  " + 
"-0.03954790075446858" + 
":  " + 
"(b('b1') <= 1046.0) ? " + 
"-0.03728972220170971" + 
":  " + 
"-0.0017382820544200822" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -13.039248943328857) ? " + 
"(b('g0vh') <= -17.820756912231445) ? " + 
"(b('lia') <= 31.53292751312256) ? " + 
"0.00845991433375002" + 
":  " + 
"-0.0029596493522087196" + 
":  " + 
"(b('grass') <= 74.8302116394043) ? " + 
"0.015431958314826202" + 
":  " + 
"0.07587652559591196" + 
":  " + 
"(b('g0vv') <= -13.028985977172852) ? " + 
"(b('grass') <= 71.44200134277344) ? " + 
"0.014754157258301221" + 
":  " + 
"0.09945068393240657" + 
":  " + 
"(b('grass') <= 21.24112033843994) ? " + 
"-0.001024857841012071" + 
":  " + 
"0.0021010564494429347" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2708.5) ? " + 
"(b('b4') <= 1132.5) ? " + 
"(b('b3') <= 849.5) ? " + 
"0.0008289034052033388" + 
":  " + 
"0.011570364621308045" + 
":  " + 
"(b('grass') <= 49.03428840637207) ? " + 
"0.001315816235328964" + 
":  " + 
"-0.004615201211290498" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('bare') <= 6.56046462059021) ? " + 
"-0.0005650757653566306" + 
":  " + 
"-0.018574177533281975" + 
":  " + 
"(b('g0vh') <= -16.811928749084473) ? " + 
"0.025461632481728506" + 
":  " + 
"-0.03996557725540011" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('urban') <= 3.522911548614502) ? " + 
"(b('ndvi') <= 5264.5) ? " + 
"0.0004897784343170751" + 
":  " + 
"-0.0053444505672004495" + 
":  " + 
"(b('b11') <= 1902.0) ? " + 
"0.06358521903668482" + 
":  " + 
"0.10329546063231537" + 
":  " + 
"(b('moss') <= 8.992009162902832) ? " + 
"(b('b10') <= 1377.0) ? " + 
"0.006292299831637132" + 
":  " + 
"-0.006012045671202102" + 
":  " + 
"(b('g0vv') <= -9.26362657546997) ? " + 
"0.0012176548432850916" + 
":  " + 
"0.03426194509487988" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('lia') <= 43.72256278991699) ? " + 
"-7.949604699711926e-05" + 
":  " + 
"0.00566410061277452" + 
":  " + 
"(b('b5') <= 3026.5) ? " + 
"-0.001952318652154377" + 
":  " + 
"0.03566657766115502" + 
":  " + 
"(b('b11') <= 1596.0) ? " + 
"(b('b1') <= 507.0) ? " + 
"-0.012816248815210927" + 
":  " + 
"0.048511030638809204" + 
":  " + 
"(b('b11') <= 1613.5) ? " + 
"0.050186906655198725" + 
":  " + 
"-0.00034667419163605234" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1019.5) ? " + 
"(b('b6') <= 3369.5) ? " + 
"(b('b4') <= 1183.5) ? " + 
"0.0005435466976398517" + 
":  " + 
"-0.007866404171079054" + 
":  " + 
"(b('b4') <= 1243.5) ? " + 
"-0.02083330673782766" + 
":  " + 
"0.0007158953226289766" + 
":  " + 
"(b('l8dt') <= 2762.5) ? " + 
"(b('lia') <= 38.130165100097656) ? " + 
"-0.0002006678006401863" + 
":  " + 
"0.12825540671668242" + 
":  " + 
"(b('b4') <= 1281.5) ? " + 
"0.009778684052137014" + 
":  " + 
"-6.813311541052569e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3486.5) ? " + 
"(b('lia') <= 42.50589179992676) ? " + 
"0.0006331657782704613" + 
":  " + 
"-0.0026275115704868473" + 
":  " + 
"(b('g0vv') <= -6.432831287384033) ? " + 
"0.01111724374826298" + 
":  " + 
"0.09412798781670449" + 
":  " + 
"(b('trees') <= 8.326765537261963) ? " + 
"(b('grass') <= 37.13905334472656) ? " + 
"-0.0011417150171999866" + 
":  " + 
"0.028667049994360524" + 
":  " + 
"(b('b6') <= 2679.0) ? " + 
"0.008190327396627159" + 
":  " + 
"-0.016989257258046633" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.43209266662598) ? " + 
"(b('lia') <= 38.30871772766113) ? " + 
"(b('lia') <= 38.16310501098633) ? " + 
"-0.0007636238308645903" + 
":  " + 
"0.014152455432258106" + 
":  " + 
"(b('b6') <= 2037.5) ? " + 
"0.06751066024955651" + 
":  " + 
"-0.03317385894412775" + 
":  " + 
"(b('lia') <= 38.45518112182617) ? " + 
"(b('grass') <= 37.62586736679077) ? " + 
"-0.06457963103656188" + 
":  " + 
"0.054146780836502165" + 
":  " + 
"(b('lia') <= 38.85299491882324) ? " + 
"0.009753864973906208" + 
":  " + 
"-4.3849730681498156e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 1239.0) ? " + 
"(b('b6') <= 2219.5) ? " + 
"(b('crop') <= 94.68265533447266) ? " + 
"-0.001481226994499628" + 
":  " + 
"0.02149054494339901" + 
":  " + 
"(b('g0vh') <= -16.93438148498535) ? " + 
"-0.03873691352630599" + 
":  " + 
"0.011425360243385444" + 
":  " + 
"(b('b4') <= 730.5) ? " + 
"(b('trees') <= 20.289265632629395) ? " + 
"0.007123966068011374" + 
":  " + 
"-0.020679917905349614" + 
":  " + 
"(b('b10') <= 1651.5) ? " + 
"-0.003922912038826841" + 
":  " + 
"0.0005033742294906579" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('crop') <= 43.67561912536621) ? " + 
"(b('b4') <= 834.0) ? " + 
"0.0041097974804945704" + 
":  " + 
"-0.020284111398501812" + 
":  " + 
"(b('b5') <= 2191.0) ? " + 
"0.0022304886032565884" + 
":  " + 
"-0.012796139927782245" + 
":  " + 
"(b('b3') <= 732.5) ? " + 
"(b('moss') <= 20.539013862609863) ? " + 
"0.013823147225915518" + 
":  " + 
"0.1250647523024233" + 
":  " + 
"(b('b4') <= 697.5) ? " + 
"0.009380854357329533" + 
":  " + 
"1.5296473788660662e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 630.5) ? " + 
"(b('trees') <= 9.36296796798706) ? " + 
"(b('b6') <= 2240.0) ? " + 
"-0.005741781644520332" + 
":  " + 
"0.015883191757061862" + 
":  " + 
"(b('b6') <= 2163.5) ? " + 
"0.0046470850550702734" + 
":  " + 
"-0.019449484551011885" + 
":  " + 
"(b('b3') <= 645.5) ? " + 
"(b('ndvi') <= 3577.0) ? " + 
"0.020029185528149165" + 
":  " + 
"-0.024873125801734498" + 
":  " + 
"(b('b3') <= 665.5) ? " + 
"-0.010535817155458005" + 
":  " + 
"0.00024111548256117396" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('bare') <= 0.43316370248794556) ? " + 
"(b('urban') <= 25.92040252685547) ? " + 
"-0.0005920305054295232" + 
":  " + 
"-0.01966898344886454" + 
":  " + 
"(b('bare') <= 0.4765203446149826) ? " + 
"0.06862593210824065" + 
":  " + 
"0.0004695976112971367" + 
":  " + 
"(b('g0vh') <= -18.530378341674805) ? " + 
"(b('g0vh') <= -18.599775314331055) ? " + 
"0.026162089486559036" + 
":  " + 
"0.11317722920548376" + 
":  " + 
"(b('lia') <= 34.12309455871582) ? " + 
"-0.036743129362719645" + 
":  " + 
"0.012953169190500661" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 14.822311401367188) ? " + 
"(b('moss') <= 14.527822494506836) ? " + 
"(b('moss') <= 14.280020236968994) ? " + 
"0.00021312333540771857" + 
":  " + 
"-0.01875174980104932" + 
":  " + 
"(b('ndvi') <= 3281.0) ? " + 
"0.060306458335632765" + 
":  " + 
"-0.02376495651579146" + 
":  " + 
"(b('b4') <= 628.0) ? " + 
"(b('b10') <= 1250.0) ? " + 
"0.016900558826422992" + 
":  " + 
"0.08204755876457381" + 
":  " + 
"(b('b3') <= 778.5) ? " + 
"-0.0164571730502399" + 
":  " + 
"-0.0006990829169168078" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -15.852939128875732) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"(b('b7') <= 1441.5) ? " + 
"-0.002919493753767863" + 
":  " + 
"0.0003329525444654092" + 
":  " + 
"(b('ndvi') <= 3194.5) ? " + 
"-0.04616777627909078" + 
":  " + 
"0.006692181032100464" + 
":  " + 
"(b('crop') <= 40.63101005554199) ? " + 
"(b('b6') <= 2983.0) ? " + 
"0.007251240122923347" + 
":  " + 
"0.05376553418325702" + 
":  " + 
"(b('ndvi') <= 1627.5) ? " + 
"0.017326619590576985" + 
":  " + 
"-0.0017499294508862204" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 181.0) ? " + 
"(b('g0vv') <= -12.663116455078125) ? " + 
"(b('l8dt') <= 518406.0) ? " + 
"0.019670765416486297" + 
":  " + 
"0.06228550794706528" + 
":  " + 
"(b('g0vv') <= -9.463024616241455) ? " + 
"0.0024899170478747375" + 
":  " + 
"0.0462650755641169" + 
":  " + 
"(b('b3') <= 437.0) ? " + 
"(b('g0vh') <= -16.467368125915527) ? " + 
"-0.015627467198696687" + 
":  " + 
"-0.06222937099855177" + 
":  " + 
"(b('b5') <= 1998.5) ? " + 
"0.0024907510253113028" + 
":  " + 
"-0.0002344357869111856" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -10.326126098632812) ? " + 
"(b('g0vh') <= -11.947437763214111) ? " + 
"(b('g0vv') <= -2.947663903236389) ? " + 
"3.0691355255288293e-06" + 
":  " + 
"-0.030502453852935176" + 
":  " + 
"(b('urban') <= 32.577152252197266) ? " + 
"0.01483217201640136" + 
":  " + 
"0.15248606933099773" + 
":  " + 
"(b('ndvi') <= 2430.0) ? " + 
"-0.08200777506746382" + 
":  " + 
"(b('b10') <= 1185.5) ? " + 
"-6.662470932033981e-05" + 
":  " + 
"-0.020321346871143384" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('urban') <= 3.522911548614502) ? " + 
"(b('trees') <= 3.377434730529785) ? " + 
"-0.000681404605749289" + 
":  " + 
"0.0014610892010702683" + 
":  " + 
"(b('b6') <= 2727.5) ? " + 
"0.055435297174158675" + 
":  " + 
"0.09084084247401902" + 
":  " + 
"(b('b5') <= 4200.0) ? " + 
"(b('b3') <= 1014.5) ? " + 
"-0.003907861403838691" + 
":  " + 
"0.0037465018972987723" + 
":  " + 
"(b('lia') <= 33.70068359375) ? " + 
"0.0273386433603188" + 
":  " + 
"0.0924868197236242" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.869969367980957) ? " + 
"(b('l8dt') <= 1638216.0) ? " + 
"(b('b10') <= 1432.5) ? " + 
"-0.017532233712420086" + 
":  " + 
"-6.95315158109668e-05" + 
":  " + 
"(b('trees') <= 13.223126888275146) ? " + 
"-0.014566306297307624" + 
":  " + 
"-0.07291336954799411" + 
":  " + 
"(b('grass') <= 34.49201011657715) ? " + 
"(b('grass') <= 24.055472373962402) ? " + 
"0.0004261965708419085" + 
":  " + 
"-0.0060755516678707745" + 
":  " + 
"(b('crop') <= 40.340951919555664) ? " + 
"-0.00013328226796938074" + 
":  " + 
"0.016539725499265547" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1308.5) ? " + 
"(b('b1') <= 433.5) ? " + 
"(b('moss') <= 7.074994802474976) ? " + 
"-0.0072071255849779775" + 
":  " + 
"-0.037893620338456724" + 
":  " + 
"(b('b4') <= 1099.0) ? " + 
"0.021894132177045444" + 
":  " + 
"-0.0014061316560070808" + 
":  " + 
"(b('b1') <= 699.5) ? " + 
"(b('bare') <= 20.924105644226074) ? " + 
"-3.552537402092255e-05" + 
":  " + 
"-0.025432755087233888" + 
":  " + 
"(b('b3') <= 1081.5) ? " + 
"-0.03277185016180986" + 
":  " + 
"0.005202314017007473" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2217.5) ? " + 
"(b('b4') <= 1281.5) ? " + 
"(b('b3') <= 761.5) ? " + 
"-0.0005460917803482399" + 
":  " + 
"0.012210458683869115" + 
":  " + 
"(b('g0vh') <= -18.15829849243164) ? " + 
"-0.013727959318276597" + 
":  " + 
"-0.09358650128514728" + 
":  " + 
"(b('b11') <= 1229.5) ? " + 
"(b('g0vh') <= -14.936882019042969) ? " + 
"-0.026154625232047642" + 
":  " + 
"0.055454506223633196" + 
":  " + 
"(b('b7') <= 1292.0) ? " + 
"0.01091133970885672" + 
":  " + 
"-0.00026331872726731073" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2436.5) ? " + 
"(b('g0vv') <= -11.710086822509766) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"-0.003526447641685358" + 
":  " + 
"0.00992378538241735" + 
":  " + 
"(b('trees') <= 4.276387691497803) ? " + 
"0.0007055993697566403" + 
":  " + 
"0.010049280834202073" + 
":  " + 
"(b('b5') <= 2462.5) ? " + 
"(b('trees') <= 17.931958198547363) ? " + 
"-0.006962221229777016" + 
":  " + 
"-0.05101511902635849" + 
":  " + 
"(b('urban') <= 36.35346794128418) ? " + 
"5.0322268860483576e-05" + 
":  " + 
"-0.013108938686578253" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3486.5) ? " + 
"(b('lia') <= 42.50589179992676) ? " + 
"0.000611104834277864" + 
":  " + 
"-0.002412981149229475" + 
":  " + 
"(b('grass') <= 0.16759777069091797) ? " + 
"0.04132588720075992" + 
":  " + 
"0.005766034264366608" + 
":  " + 
"(b('b11') <= 2622.0) ? " + 
"(b('b2') <= 466.5) ? " + 
"0.005160414163633851" + 
":  " + 
"-0.009614386450868309" + 
":  " + 
"(b('b11') <= 2629.0) ? " + 
"0.08647463015684358" + 
":  " + 
"0.0010344783192200158" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 34.50992774963379) ? " + 
"(b('g0vv') <= -11.03117036819458) ? " + 
"(b('grass') <= 11.09217882156372) ? " + 
"0.005966985747444751" + 
":  " + 
"-0.007428063062357579" + 
":  " + 
"(b('grass') <= 41.0262393951416) ? " + 
"-0.0008881431927148868" + 
":  " + 
"0.018883437840113752" + 
":  " + 
"(b('lia') <= 34.529273986816406) ? " + 
"(b('moss') <= 0.4507042169570923) ? " + 
"0.12238896189775873" + 
":  " + 
"-0.006885975775792905" + 
":  " + 
"(b('lia') <= 34.56062698364258) ? " + 
"-0.031424158332955976" + 
":  " + 
"0.00047990038395150753" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 89.04487609863281) ? " + 
"(b('crop') <= 85.84851455688477) ? " + 
"(b('crop') <= 85.4493522644043) ? " + 
"0.00018593877609484995" + 
":  " + 
"-0.012592126154383572" + 
":  " + 
"(b('b6') <= 3152.5) ? " + 
"0.018969663466837643" + 
":  " + 
"-0.0026140523193272586" + 
":  " + 
"(b('g0vh') <= -18.83031940460205) ? " + 
"(b('lia') <= 42.53888702392578) ? " + 
"0.002317846546997771" + 
":  " + 
"0.04549678327085904" + 
":  " + 
"(b('b10') <= 1109.5) ? " + 
"0.015896623484738175" + 
":  " + 
"-0.01074257730407752" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 932.5) ? " + 
"(b('b6') <= 3242.5) ? " + 
"(b('b4') <= 1205.5) ? " + 
"-6.873376282223832e-06" + 
":  " + 
"-0.025243648781975887" + 
":  " + 
"(b('trees') <= 15.550819396972656) ? " + 
"-0.007171859371246404" + 
":  " + 
"-0.0379704089409118" + 
":  " + 
"(b('b5') <= 1701.0) ? " + 
"(b('g0vv') <= -10.683626174926758) ? " + 
"-0.0499186275926482" + 
":  " + 
"-0.0899006489213025" + 
":  " + 
"(b('b5') <= 2053.5) ? " + 
"0.013989763999194983" + 
":  " + 
"0.0003305179016555303" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 259.5) ? " + 
"(b('b4') <= 732.0) ? " + 
"(b('b4') <= 724.0) ? " + 
"-3.441690305778668e-05" + 
":  " + 
"0.0364116161727799" + 
":  " + 
"(b('ndvi') <= 3480.5) ? " + 
"-0.005763838368216899" + 
":  " + 
"-0.024049037632050706" + 
":  " + 
"(b('b6') <= 1426.5) ? " + 
"(b('trees') <= 1.6531440019607544) ? " + 
"-0.051196582732937056" + 
":  " + 
"0.051422805397780436" + 
":  " + 
"(b('b4') <= 463.5) ? " + 
"0.07504129003386494" + 
":  " + 
"0.00020811735983657228" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3218711.5) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"(b('g0vh') <= -18.070767402648926) ? " + 
"0.0009224960379281355" + 
":  " + 
"-0.004192138720395203" + 
":  " + 
"(b('g0vv') <= -10.736237049102783) ? " + 
"-0.0008653403514970408" + 
":  " + 
"0.005182679189921397" + 
":  " + 
"(b('crop') <= 60.688377380371094) ? " + 
"(b('crop') <= 50.93680191040039) ? " + 
"0.0008806020172099384" + 
":  " + 
"-0.03449162596747294" + 
":  " + 
"(b('moss') <= 9.441802501678467) ? " + 
"0.011538135465968123" + 
":  " + 
"-0.010754922379471227" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 4840.5) ? " + 
"(b('b4') <= 2652.0) ? " + 
"(b('ndvi') <= 1308.5) ? " + 
"-0.0022537673996244193" + 
":  " + 
"0.0003116462515856751" + 
":  " + 
"(b('b4') <= 2657.0) ? " + 
"0.06080514979829191" + 
":  " + 
"0.007388009360963924" + 
":  " + 
"(b('l8dt') <= 1104001.5) ? " + 
"(b('b5') <= 3672.0) ? " + 
"0.024473431213820392" + 
":  " + 
"-0.0019262780514322294" + 
":  " + 
"(b('b1') <= 1046.0) ? " + 
"-0.03370785233942295" + 
":  " + 
"-0.0025803045160589845" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 630.5) ? " + 
"(b('b4') <= 711.5) ? " + 
"(b('b3') <= 626.5) ? " + 
"0.0010597404335418563" + 
":  " + 
"-0.02386816536566222" + 
":  " + 
"(b('ndvi') <= 3567.5) ? " + 
"-0.007941249136177624" + 
":  " + 
"-0.057794181395495345" + 
":  " + 
"(b('b4') <= 520.5) ? " + 
"(b('crop') <= 54.60833549499512) ? " + 
"0.009267378614350612" + 
":  " + 
"0.07580767387415999" + 
":  " + 
"(b('b4') <= 566.5) ? " + 
"-0.028631244050067183" + 
":  " + 
"0.0002530362162522267" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1324.0) ? " + 
"(b('l8dt') <= 690921.0) ? " + 
"(b('b1') <= 507.0) ? " + 
"0.003956466137856489" + 
":  " + 
"0.07902649822940236" + 
":  " + 
"(b('lia') <= 34.007442474365234) ? " + 
"0.00017904945177939119" + 
":  " + 
"-0.035962730612843385" + 
":  " + 
"(b('b5') <= 1405.5) ? " + 
"(b('urban') <= 0.0903225839138031) ? " + 
"0.035506670803654085" + 
":  " + 
"-0.0034186841788574813" + 
":  " + 
"(b('b5') <= 1418.0) ? " + 
"-0.048005115142079204" + 
":  " + 
"1.3099748989154351e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('urban') <= 3.522911548614502) ? " + 
"(b('moss') <= 0.06014965660870075) ? " + 
"-0.001742436100545205" + 
":  " + 
"0.0008552355612629615" + 
":  " + 
"(b('ndvi') <= 2064.0) ? " + 
"0.08211509522421168" + 
":  " + 
"0.04967496730368955" + 
":  " + 
"(b('b6') <= 2286.5) ? " + 
"(b('crop') <= 45.11186408996582) ? " + 
"0.02103695432665593" + 
":  " + 
"-0.002398430922096174" + 
":  " + 
"(b('b5') <= 3030.0) ? " + 
"-0.007947375027768619" + 
":  " + 
"0.0038971947212597647" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 19.819469451904297) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('moss') <= 18.02293586730957) ? " + 
"0.00016164252748597502" + 
":  " + 
"-0.01033932688571706" + 
":  " + 
"(b('g0vv') <= -13.614131927490234) ? " + 
"0.006424839174889876" + 
":  " + 
"0.047090595065858415" + 
":  " + 
"(b('grass') <= 70.92327880859375) ? " + 
"(b('b4') <= 1183.0) ? " + 
"0.021146256736283037" + 
":  " + 
"-0.0055456030737093785" + 
":  " + 
"(b('b6') <= 2276.5) ? " + 
"0.04292163283736827" + 
":  " + 
"-0.052569040305142714" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 34.980010986328125) ? " + 
"(b('grass') <= 24.055472373962402) ? " + 
"(b('grass') <= 22.53521728515625) ? " + 
"-0.0005718469012592253" + 
":  " + 
"0.01938185391321233" + 
":  " + 
"(b('trees') <= 19.827622413635254) ? " + 
"-0.007344564697157796" + 
":  " + 
"0.03405197976212163" + 
":  " + 
"(b('crop') <= 40.340951919555664) ? " + 
"(b('grass') <= 43.6376953125) ? " + 
"-0.01909821726955244" + 
":  " + 
"0.0003834859813226813" + 
":  " + 
"(b('moss') <= 5.13878059387207) ? " + 
"0.004972452869993363" + 
":  " + 
"0.062485593321069496" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3450.5) ? " + 
"(b('crop') <= 89.04487609863281) ? " + 
"0.0004013735015856697" + 
":  " + 
"-0.003726544660918541" + 
":  " + 
"(b('b5') <= 3455.5) ? " + 
"0.04126986998640897" + 
":  " + 
"0.0038341530014063033" + 
":  " + 
"(b('b5') <= 3519.5) ? " + 
"(b('ndvi') <= 3458.5) ? " + 
"-0.060711150231874775" + 
":  " + 
"0.035888670943944344" + 
":  " + 
"(b('b6') <= 2410.5) ? " + 
"0.006985982196432949" + 
":  " + 
"-0.0031013760598266084" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 4.659861326217651) ? " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"(b('moss') <= 3.2363791465759277) ? " + 
"-0.0027531763960961884" + 
":  " + 
"0.007262560610863709" + 
":  " + 
"(b('trees') <= 4.114237546920776) ? " + 
"0.06223829806611093" + 
":  " + 
"0.0037961287364578176" + 
":  " + 
"(b('grass') <= 87.20395278930664) ? " + 
"(b('grass') <= 71.98248291015625) ? " + 
"-7.52757328583785e-05" + 
":  " + 
"-0.005754232724525526" + 
":  " + 
"(b('g0vh') <= -21.63368034362793) ? " + 
"-0.018204188189498035" + 
":  " + 
"0.02440794685000409" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b10') <= 1782.5) ? " + 
"(b('b1') <= 518.5) ? " + 
"(b('b2') <= 670.0) ? " + 
"-0.00037360955413952935" + 
":  " + 
"0.10104514964529186" + 
":  " + 
"(b('b6') <= 1999.5) ? " + 
"0.014186322753023799" + 
":  " + 
"-0.030978240533925883" + 
":  " + 
"(b('b7') <= 1790.5) ? " + 
"(b('b3') <= 881.5) ? " + 
"0.05918562711959575" + 
":  " + 
"-0.013716185881868613" + 
":  " + 
"(b('b3') <= 774.0) ? " + 
"-0.010762128816518588" + 
":  " + 
"0.0007187946354619848" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3167.5) ? " + 
"(b('b5') <= 3158.5) ? " + 
"(b('lia') <= 38.4306697845459) ? " + 
"-0.001098581155409412" + 
":  " + 
"0.0016984176039831498" + 
":  " + 
"(b('g0vv') <= -11.480023384094238) ? " + 
"0.015661246180015093" + 
":  " + 
"0.07325218612286612" + 
":  " + 
"(b('b3') <= 752.5) ? " + 
"(b('b3') <= 624.5) ? " + 
"0.05574509233153424" + 
":  " + 
"-0.013564329324633096" + 
":  " + 
"(b('urban') <= 36.35346794128418) ? " + 
"-6.526395293939135e-07" + 
":  " + 
"-0.025736600540818506" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2444.5) ? " + 
"(b('g0vv') <= -11.712082386016846) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"-0.003211461123776952" + 
":  " + 
"0.009725535741241504" + 
":  " + 
"(b('b5') <= 2341.5) ? " + 
"0.002051377776362113" + 
":  " + 
"0.014200550219646016" + 
":  " + 
"(b('b5') <= 2462.5) ? " + 
"(b('b6') <= 3619.5) ? " + 
"-0.02074682309514313" + 
":  " + 
"0.05882667099162137" + 
":  " + 
"(b('grass') <= 35.85540008544922) ? " + 
"-0.0012413330047567634" + 
":  " + 
"0.0022058172859382996" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 630.5) ? " + 
"(b('g0vh') <= -22.91350269317627) ? " + 
"(b('b6') <= 2288.0) ? " + 
"0.07273653533045787" + 
":  " + 
"0.12431765556696256" + 
":  " + 
"(b('trees') <= 9.36296796798706) ? " + 
"0.0013543174100413466" + 
":  " + 
"-0.007272596550891667" + 
":  " + 
"(b('b3') <= 645.5) ? " + 
"(b('b7') <= 1551.0) ? " + 
"0.002575412432038558" + 
":  " + 
"0.0361338990273285" + 
":  " + 
"(b('b3') <= 664.5) ? " + 
"-0.009621917081518648" + 
":  " + 
"0.00022373113232201762" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2847.5) ? " + 
"(b('b6') <= 2841.5) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"-0.0010242850972851812" + 
":  " + 
"0.00330141329721944" + 
":  " + 
"(b('b7') <= 2229.5) ? " + 
"0.020596896335522332" + 
":  " + 
"0.10479204401841177" + 
":  " + 
"(b('b6') <= 2891.5) ? " + 
"(b('trees') <= 13.223126888275146) ? " + 
"-0.010128146909574908" + 
":  " + 
"-0.04659067622579844" + 
":  " + 
"(b('b6') <= 2901.5) ? " + 
"0.03099277037122259" + 
":  " + 
"-0.0003773447677219963" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3218711.5) ? " + 
"(b('b5') <= 1697.5) ? " + 
"(b('trees') <= 17.012328624725342) ? " + 
"0.001650489255430648" + 
":  " + 
"0.03357006365055122" + 
":  " + 
"(b('b3') <= 630.5) ? " + 
"-0.0054236678544668186" + 
":  " + 
"-5.454001387377541e-05" + 
":  " + 
"(b('crop') <= 60.688377380371094) ? " + 
"(b('crop') <= 50.93680191040039) ? " + 
"0.000782028053224636" + 
":  " + 
"-0.030163365893301982" + 
":  " + 
"(b('moss') <= 2.8560986518859863) ? " + 
"0.014982131382040367" + 
":  " + 
"-0.001179408900052317" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 24.395869255065918) ? " + 
"(b('b4') <= 1248.0) ? " + 
"(b('b7') <= 2411.5) ? " + 
"0.06772220024047829" + 
":  " + 
"0.10933998483620372" + 
":  " + 
"(b('g0vv') <= -14.644976615905762) ? " + 
"0.016422857822731333" + 
":  " + 
"-0.010326554917435213" + 
":  " + 
"(b('g0vv') <= -15.168814659118652) ? " + 
"(b('ndvi') <= 4859.5) ? " + 
"-0.0030866017496716048" + 
":  " + 
"0.023335813540488658" + 
":  " + 
"(b('g0vv') <= -15.159584522247314) ? " + 
"0.04849482831363279" + 
":  " + 
"0.00016863740583779107" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5229.5) ? " + 
"(b('ndvi') <= 5084.0) ? " + 
"(b('g0vv') <= -6.18162989616394) ? " + 
"-9.828438401680553e-05" + 
":  " + 
"0.007427956454135712" + 
":  " + 
"(b('b3') <= 990.5) ? " + 
"0.008109937070875569" + 
":  " + 
"0.07750981722992113" + 
":  " + 
"(b('ndvi') <= 5724.0) ? " + 
"(b('b5') <= 4015.0) ? " + 
"-0.014889149703234506" + 
":  " + 
"0.07113498326979663" + 
":  " + 
"(b('b4') <= 792.5) ? " + 
"-0.010784516348418123" + 
":  " + 
"0.010009620999949178" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -10.326126098632812) ? " + 
"(b('g0vh') <= -11.947437763214111) ? " + 
"(b('g0vv') <= -2.947663903236389) ? " + 
"2.8809384166912545e-06" + 
":  " + 
"-0.02695383954604878" + 
":  " + 
"(b('g0vh') <= -11.775384902954102) ? " + 
"0.059695922559065875" + 
":  " + 
"0.003885135260911119" + 
":  " + 
"(b('l8dt') <= 1036801.0) ? " + 
"-0.07762342326890898" + 
":  " + 
"(b('b3') <= 1021.0) ? " + 
"-0.007049859952756213" + 
":  " + 
"-0.025053026652322452" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 3248.5) ? " + 
"(b('b7') <= 3207.0) ? " + 
"(b('b10') <= 3191.0) ? " + 
"-0.00014016070014889536" + 
":  " + 
"0.02855242647742462" + 
":  " + 
"(b('g0vh') <= -18.556471824645996) ? " + 
"-0.017225300250447467" + 
":  " + 
"0.017254178473868693" + 
":  " + 
"(b('b4') <= 2096.5) ? " + 
"(b('b1') <= 773.5) ? " + 
"0.0033274254414402326" + 
":  " + 
"0.028360734353634717" + 
":  " + 
"(b('trees') <= 6.08231258392334) ? " + 
"0.0007996833179493392" + 
":  " + 
"-0.0213519578500776" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 20.289265632629395) ? " + 
"(b('trees') <= 19.831669807434082) ? " + 
"-4.1131100863112014e-05" + 
":  " + 
"0.016497072278643814" + 
":  " + 
"(b('grass') <= 50.928749084472656) ? " + 
"0.0023996482540543053" + 
":  " + 
"-0.014842208957471204" + 
":  " + 
"(b('b6') <= 2005.0) ? " + 
"(b('g0vv') <= -10.78778076171875) ? " + 
"0.07160326333211416" + 
":  " + 
"0.024154478245759003" + 
":  " + 
"(b('g0vh') <= -18.530378341674805) ? " + 
"0.03139320322350745" + 
":  " + 
"-0.0005399546064248734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 42.914493560791016) ? " + 
"(b('lia') <= 42.89633369445801) ? " + 
"(b('ndvi') <= 5203.0) ? " + 
"0.0004470764572833344" + 
":  " + 
"-0.004595497431185853" + 
":  " + 
"(b('b5') <= 2190.5) ? " + 
"0.13042133908642717" + 
":  " + 
"0.027986706624902442" + 
":  " + 
"(b('grass') <= 95.59092330932617) ? " + 
"(b('grass') <= 12.461678981781006) ? " + 
"-0.008539399122162974" + 
":  " + 
"0.004004590929223061" + 
":  " + 
"(b('b6') <= 2451.5) ? " + 
"0.10555302208253085" + 
":  " + 
"-0.028541451130568402" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 0.16759777069091797) ? " + 
"(b('b5') <= 3088.5) ? " + 
"(b('g0vv') <= -7.722679615020752) ? " + 
"-0.004713812389484358" + 
":  " + 
"0.019012785359695993" + 
":  " + 
"(b('b5') <= 3686.0) ? " + 
"0.017426205652770616" + 
":  " + 
"0.0013786090102903953" + 
":  " + 
"(b('ndvi') <= 1291.0) ? " + 
"(b('b3') <= 890.0) ? " + 
"-0.0202107202573022" + 
":  " + 
"-0.0014444221509764133" + 
":  " + 
"(b('b5') <= 3167.5) ? " + 
"0.001093923185769332" + 
":  " + 
"-0.0019308061990700094" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -16.97585391998291) ? " + 
"(b('l8dt') <= 1428326.5) ? " + 
"(b('lia') <= 29.290966987609863) ? " + 
"0.0382205511121807" + 
":  " + 
"-0.0035756022023718313" + 
":  " + 
"(b('moss') <= 15.108849048614502) ? " + 
"-0.035235447970382285" + 
":  " + 
"0.04501600238493688" + 
":  " + 
"(b('g0vv') <= -16.966025352478027) ? " + 
"(b('b5') <= 2319.5) ? " + 
"0.034296596751008684" + 
":  " + 
"0.10221880334182659" + 
":  " + 
"(b('crop') <= 43.67561912536621) ? " + 
"0.0009092363341841421" + 
":  " + 
"-0.0005331842901562513" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 2907.5) ? " + 
"(b('b4') <= 1578.5) ? " + 
"(b('b3') <= 1039.5) ? " + 
"-0.0004911140829554912" + 
":  " + 
"0.00359641324703923" + 
":  " + 
"(b('b3') <= 1277.5) ? " + 
"-0.01041120212525058" + 
":  " + 
"2.0464586384850337e-05" + 
":  " + 
"(b('b7') <= 2910.0) ? " + 
"(b('ndvi') <= 1344.0) ? " + 
"0.04200129685017289" + 
":  " + 
"-0.0089991576697749" + 
":  " + 
"(b('ndvi') <= 2819.5) ? " + 
"0.0005246913682161957" + 
":  " + 
"0.010245742066321903" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2847.5) ? " + 
"(b('b6') <= 2841.5) ? " + 
"(b('lia') <= 44.315269470214844) ? " + 
"0.00020234094745538085" + 
":  " + 
"0.01617267966106828" + 
":  " + 
"(b('grass') <= 7.744230508804321) ? " + 
"0.06090837812196741" + 
":  " + 
"0.010847298300960966" + 
":  " + 
"(b('b7') <= 1592.0) ? " + 
"(b('b11') <= 1583.5) ? " + 
"-0.01894017799258513" + 
":  " + 
"-0.06690906193276923" + 
":  " + 
"(b('b1') <= 403.5) ? " + 
"0.01034430243667922" + 
":  " + 
"-0.0011038752916348287" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 666.5) ? " + 
"(b('b7') <= 1489.5) ? " + 
"(b('b3') <= 656.5) ? " + 
"-0.0032200395896636227" + 
":  " + 
"-0.029375995139641203" + 
":  " + 
"(b('ndvi') <= 4582.5) ? " + 
"0.009352005164871318" + 
":  " + 
"-0.03194101254164024" + 
":  " + 
"(b('b1') <= 153.5) ? " + 
"(b('g0vv') <= -9.603841781616211) ? " + 
"0.09950568238566304" + 
":  " + 
"0.04731994543599772" + 
":  " + 
"(b('b4') <= 520.5) ? " + 
"0.06628615794613746" + 
":  " + 
"0.00015171589039326416" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 19.819469451904297) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('moss') <= 18.02293586730957) ? " + 
"0.00014793185440788937" + 
":  " + 
"-0.009824105631661731" + 
":  " + 
"(b('b3') <= 815.0) ? " + 
"0.053884717931492014" + 
":  " + 
"0.008730665596703794" + 
":  " + 
"(b('moss') <= 20.664283752441406) ? " + 
"(b('l8dt') <= 4358711.5) ? " + 
"-0.05409844065233304" + 
":  " + 
"0.002526677328854768" + 
":  " + 
"(b('b4') <= 1183.0) ? " + 
"0.014717023638913277" + 
":  " + 
"-0.005570957352596227" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.063567638397217) ? " + 
"(b('l8dt') <= 4107531.0) ? " + 
"(b('l8dt') <= 343813.5) ? " + 
"0.0017140414591045267" + 
":  " + 
"-0.004557237174478152" + 
":  " + 
"(b('ndvi') <= 1693.0) ? " + 
"0.08234953300088504" + 
":  " + 
"0.0228672824118494" + 
":  " + 
"(b('moss') <= 4.659861326217651) ? " + 
"(b('bare') <= 0.43316370248794556) ? " + 
"-0.0006083028492969827" + 
":  " + 
"0.005297588858075999" + 
":  " + 
"(b('b4') <= 787.5) ? " + 
"0.003407842316585724" + 
":  " + 
"-0.00192772565421371" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 2974.5) ? " + 
"(b('b6') <= 4267.5) ? " + 
"(b('bare') <= 14.846899032592773) ? " + 
"6.084406262678749e-06" + 
":  " + 
"-0.005026437229904593" + 
":  " + 
"(b('trees') <= 9.155172348022461) ? " + 
"-0.02782613113894541" + 
":  " + 
"-0.007173827639713928" + 
":  " + 
"(b('b5') <= 2287.5) ? " + 
"(b('b1') <= 632.5) ? " + 
"-0.0015976095503650648" + 
":  " + 
"-0.040105436352883383" + 
":  " + 
"(b('b6') <= 3892.5) ? " + 
"0.00873068422380624" + 
":  " + 
"0.0007602812941605203" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('urban') <= 3.522911548614502) ? " + 
"(b('moss') <= 0.06014965660870075) ? " + 
"-0.0015358762847427919" + 
":  " + 
"0.000792114970080428" + 
":  " + 
"(b('l8dt') <= 518398.5) ? " + 
"0.07485046241621017" + 
":  " + 
"0.0438551242741049" + 
":  " + 
"(b('trees') <= 11.409454822540283) ? " + 
"(b('trees') <= 9.817587852478027) ? " + 
"-0.0015163198059932163" + 
":  " + 
"0.017145298998428704" + 
":  " + 
"(b('b5') <= 3051.5) ? " + 
"-0.016153822918137432" + 
":  " + 
"0.004367035222259875" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2557.5) ? " + 
"(b('ndvi') <= 2547.0) ? " + 
"(b('ndvi') <= 2542.5) ? " + 
"0.0004578707508684533" + 
":  " + 
"-0.042665207108418896" + 
":  " + 
"(b('trees') <= 12.095959186553955) ? " + 
"0.017510037664418533" + 
":  " + 
"0.11027370776723767" + 
":  " + 
"(b('ndvi') <= 2599.5) ? " + 
"(b('l8dt') <= 6854.0) ? " + 
"0.08260896799814324" + 
":  " + 
"-0.023087578681565118" + 
":  " + 
"(b('trees') <= 19.15903377532959) ? " + 
"0.00042433573036180643" + 
":  " + 
"-0.006921502572414228" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 2.0455974340438843) ? " + 
"(b('moss') <= 1.398017704486847) ? " + 
"(b('b2') <= 508.5) ? " + 
"-0.006198360388327882" + 
":  " + 
"0.0029338763111009416" + 
":  " + 
"(b('b6') <= 2674.0) ? " + 
"0.050887343236843345" + 
":  " + 
"0.002406380980018618" + 
":  " + 
"(b('bare') <= 6.329379320144653) ? " + 
"(b('b6') <= 2281.5) ? " + 
"0.0038040504696949854" + 
":  " + 
"-0.0020538393338908503" + 
":  " + 
"(b('g0vv') <= -10.694484233856201) ? " + 
"2.21739252028273e-06" + 
":  " + 
"0.017430937852897933" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 17.472150802612305) ? " + 
"(b('trees') <= 15.571342945098877) ? " + 
"(b('trees') <= 15.19383430480957) ? " + 
"-0.00011305204626520755" + 
":  " + 
"0.014469522306195023" + 
":  " + 
"(b('b6') <= 3480.5) ? " + 
"-0.027155005926140622" + 
":  " + 
"-0.09476244180496678" + 
":  " + 
"(b('trees') <= 19.15903377532959) ? " + 
"(b('b6') <= 3061.5) ? " + 
"0.038071302309322985" + 
":  " + 
"-0.007490189586380499" + 
":  " + 
"(b('b3') <= 939.0) ? " + 
"-0.00639273643679774" + 
":  " + 
"0.012171393202588828" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('lia') <= 42.914493560791016) ? " + 
"(b('lia') <= 42.80050468444824) ? " + 
"0.00011099897609903183" + 
":  " + 
"0.01249077353144175" + 
":  " + 
"(b('grass') <= 95.59092330932617) ? " + 
"-0.0006842446868667551" + 
":  " + 
"-0.01776184231918343" + 
":  " + 
"(b('l8dt') <= 3285909.0) ? " + 
"(b('l8dt') <= 687511.0) ? " + 
"0.0029046933714498274" + 
":  " + 
"0.032847901589558276" + 
":  " + 
"(b('g0vh') <= -15.685114860534668) ? " + 
"-0.024779030004401847" + 
":  " + 
"-0.07917679120006038" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 259.5) ? " + 
"(b('b4') <= 732.0) ? " + 
"(b('b3') <= 705.5) ? " + 
"-0.0013561566922105275" + 
":  " + 
"0.016704823410601186" + 
":  " + 
"(b('urban') <= 9.834710597991943) ? " + 
"-0.012684430525392844" + 
":  " + 
"0.015409266592363994" + 
":  " + 
"(b('b2') <= 314.0) ? " + 
"(b('l8dt') <= 1047396.0) ? " + 
"0.04410954230873887" + 
":  " + 
"0.011408433298379837" + 
":  " + 
"(b('b3') <= 562.5) ? " + 
"-0.017883058026187067" + 
":  " + 
"0.00024970077599694313" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2696.5) ? " + 
"(b('b5') <= 2663.5) ? " + 
"(b('l8dt') <= 347974.5) ? " + 
"0.003226856924845007" + 
":  " + 
"-0.0014251587966353544" + 
":  " + 
"(b('b5') <= 2668.5) ? " + 
"0.04245703874896129" + 
":  " + 
"0.0035603430791129476" + 
":  " + 
"(b('b5') <= 2793.5) ? " + 
"(b('trees') <= 19.26138973236084) ? " + 
"-0.008654919692279613" + 
":  " + 
"0.03099049765598669" + 
":  " + 
"(b('b5') <= 2809.5) ? " + 
"0.018873785616040896" + 
":  " + 
"-0.0002999231821239553" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 0.16759777069091797) ? " + 
"(b('b1') <= 220.0) ? " + 
"(b('g0vv') <= -9.337562084197998) ? " + 
"-0.06606765979206085" + 
":  " + 
"-0.016654845931950085" + 
":  " + 
"(b('b2') <= 362.0) ? " + 
"0.051880235304085524" + 
":  " + 
"0.0021611007032681746" + 
":  " + 
"(b('ndvi') <= 1291.0) ? " + 
"(b('b3') <= 873.5) ? " + 
"-0.01902224191901988" + 
":  " + 
"-0.0015251559448928042" + 
":  " + 
"(b('b5') <= 3167.5) ? " + 
"0.001033332522232968" + 
":  " + 
"-0.0018247587915634531" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 2990.5) ? " + 
"(b('b4') <= 1614.5) ? " + 
"(b('b4') <= 1603.5) ? " + 
"0.00014105863795947675" + 
":  " + 
"0.023418574980810274" + 
":  " + 
"(b('b3') <= 1277.5) ? " + 
"-0.011971622714504212" + 
":  " + 
"-0.00019845072577308041" + 
":  " + 
"(b('b7') <= 3001.5) ? " + 
"(b('lia') <= 37.63292121887207) ? " + 
"0.05699873437427556" + 
":  " + 
"0.015547260336841815" + 
":  " + 
"(b('b5') <= 2585.0) ? " + 
"-0.01515036820609542" + 
":  " + 
"0.0017593260434259144" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 14.822311401367188) ? " + 
"(b('moss') <= 14.732791900634766) ? " + 
"(b('ndvi') <= 645.0) ? " + 
"0.020333597642988078" + 
":  " + 
"5.719198288190336e-05" + 
":  " + 
"(b('ndvi') <= 3128.5) ? " + 
"0.09812130018243338" + 
":  " + 
"-0.016688380603240686" + 
":  " + 
"(b('b4') <= 628.0) ? " + 
"(b('ndvi') <= 2202.5) ? " + 
"0.16766647468799922" + 
":  " + 
"0.030176641100145327" + 
":  " + 
"(b('bare') <= 4.734025239944458) ? " + 
"-0.006535566646698967" + 
":  " + 
"0.0025739083627710495" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2436.5) ? " + 
"(b('b5') <= 2430.5) ? " + 
"(b('moss') <= 1.6108241081237793) ? " + 
"0.004977787247609895" + 
":  " + 
"-0.0008577608378343486" + 
":  " + 
"(b('trees') <= 19.069180488586426) ? " + 
"0.021331225995760695" + 
":  " + 
"0.16179350178742008" + 
":  " + 
"(b('b5') <= 2462.5) ? " + 
"(b('trees') <= 17.275117874145508) ? " + 
"-0.004899675531564774" + 
":  " + 
"-0.04451256970636491" + 
":  " + 
"(b('grass') <= 35.85540008544922) ? " + 
"-0.0011130864100723106" + 
":  " + 
"0.0018884256781169333" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 2.4269771575927734) ? " + 
"(b('b4') <= 670.5) ? " + 
"(b('b3') <= 754.5) ? " + 
"0.010057176801767844" + 
":  " + 
"0.08237709745165825" + 
":  " + 
"(b('b3') <= 658.5) ? " + 
"-0.026372899447932564" + 
":  " + 
"-0.0012897512928259861" + 
":  " + 
"(b('grass') <= 63.09731101989746) ? " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.00044191509846039877" + 
":  " + 
"-0.0288035480272635" + 
":  " + 
"(b('ndvi') <= 2739.5) ? " + 
"0.044640001677405027" + 
":  " + 
"-0.0011350728590152812" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 384.5) ? " + 
"(b('bare') <= 19.278925895690918) ? " + 
"(b('g0vv') <= -12.836845874786377) ? " + 
"-0.008740621708118661" + 
":  " + 
"-0.00021686929953702115" + 
":  " + 
"(b('g0vv') <= -11.605651378631592) ? " + 
"-0.15100118430414755" + 
":  " + 
"-0.05580447417534873" + 
":  " + 
"(b('b4') <= 835.5) ? " + 
"(b('moss') <= 8.992009162902832) ? " + 
"-0.0008218107193689167" + 
":  " + 
"0.010667616574463338" + 
":  " + 
"(b('b3') <= 892.25) ? " + 
"-0.003491061080170787" + 
":  " + 
"0.0005723619135486311" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2508.5) ? " + 
"(b('bare') <= 14.846899032592773) ? " + 
"(b('b5') <= 2488.5) ? " + 
"0.001056112967234105" + 
":  " + 
"0.01421119193474001" + 
":  " + 
"(b('g0vv') <= -6.204157114028931) ? " + 
"-0.010213585063664005" + 
":  " + 
"0.12233628087089948" + 
":  " + 
"(b('b3') <= 755.5) ? " + 
"(b('b4') <= 775.0) ? " + 
"-0.0011006009578459935" + 
":  " + 
"-0.021799534936184944" + 
":  " + 
"(b('b3') <= 778.5) ? " + 
"0.010810742382212881" + 
":  " + 
"-0.00032422824550654394" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -16.00978374481201) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"(b('b11') <= 1441.5) ? " + 
"-0.0028909862542186135" + 
":  " + 
"0.0003273259764165942" + 
":  " + 
"(b('ndvi') <= 2906.0) ? " + 
"-0.05011774502677083" + 
":  " + 
"0.0025277580861167524" + 
":  " + 
"(b('bare') <= 6.56046462059021) ? " + 
"(b('ndvi') <= 2088.5) ? " + 
"0.014999872414468002" + 
":  " + 
"0.0006281575446320788" + 
":  " + 
"(b('g0vv') <= -7.182415962219238) ? " + 
"-0.02012786525274052" + 
":  " + 
"0.03178949647977609" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 24.503172874450684) ? " + 
"(b('trees') <= 23.840930938720703) ? " + 
"-4.460976325660994e-05" + 
":  " + 
"0.012643165408515292" + 
":  " + 
"(b('b1') <= 342.5) ? " + 
"-0.07465679709311755" + 
":  " + 
"-0.0036597256090986924" + 
":  " + 
"(b('g0vh') <= -14.909619808197021) ? " + 
"(b('g0vh') <= -18.530378341674805) ? " + 
"0.030816696248453027" + 
":  " + 
"-0.001380271850555516" + 
":  " + 
"(b('l8dt') <= 90049.5) ? " + 
"0.030492623242763917" + 
":  " + 
"0.06411525271983315" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2847.5) ? " + 
"(b('b6') <= 2841.5) ? " + 
"(b('grass') <= 46.00799369812012) ? " + 
"-0.0009825049855952386" + 
":  " + 
"0.003191791211280669" + 
":  " + 
"(b('b7') <= 2229.5) ? " + 
"0.016417117386973316" + 
":  " + 
"0.08930353418166191" + 
":  " + 
"(b('b6') <= 2879.5) ? " + 
"(b('trees') <= 14.47687816619873) ? " + 
"-0.010317540126735995" + 
":  " + 
"-0.05355966855286186" + 
":  " + 
"(b('crop') <= 99.63687133789062) ? " + 
"-0.0003506646835703936" + 
":  " + 
"0.03774038136859773" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 5.957038402557373) ? " + 
"(b('b4') <= 629.0) ? " + 
"(b('b2') <= 355.5) ? " + 
"-0.002972177924297803" + 
":  " + 
"0.04311654633012699" + 
":  " + 
"(b('b1') <= 384.5) ? " + 
"-0.01144698476878846" + 
":  " + 
"-0.0004208490691986373" + 
":  " + 
"(b('grass') <= 63.09731101989746) ? " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.0003915624671184587" + 
":  " + 
"-0.02605406145233594" + 
":  " + 
"(b('ndvi') <= 2691.0) ? " + 
"0.049895074395132306" + 
":  " + 
"0.0013527937770538194" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 630.5) ? " + 
"(b('trees') <= 9.36296796798706) ? " + 
"(b('b6') <= 2240.0) ? " + 
"-0.004742259466981067" + 
":  " + 
"0.013191349231000331" + 
":  " + 
"(b('b6') <= 2163.5) ? " + 
"0.003029731106844784" + 
":  " + 
"-0.015665036264690284" + 
":  " + 
"(b('b7') <= 1043.0) ? " + 
"(b('grass') <= 29.252792358398438) ? " + 
"0.020344471469210246" + 
":  " + 
"-0.018412069094703287" + 
":  " + 
"(b('b1') <= 159.0) ? " + 
"0.09846558706979004" + 
":  " + 
"6.126142624397783e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1681.0) ? " + 
"(b('trees') <= 17.012328624725342) ? " + 
"(b('b5') <= 1677.5) ? " + 
"-0.00024402708376132862" + 
":  " + 
"0.0761847934037766" + 
":  " + 
"(b('b6') <= 1748.0) ? " + 
"-0.009651840741259464" + 
":  " + 
"0.07748121083870661" + 
":  " + 
"(b('b5') <= 1693.5) ? " + 
"(b('b4') <= 957.0) ? " + 
"-0.014809684791352232" + 
":  " + 
"-0.06169547979466701" + 
":  " + 
"(b('b5') <= 1694.5) ? " + 
"0.10862036563961897" + 
":  " + 
"-0.00011775955200201301" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -20.81766700744629) ? " + 
"(b('l8dt') <= 423171.0) ? " + 
"(b('moss') <= 4.669075012207031) ? " + 
"0.05117156292052211" + 
":  " + 
"0.07893622489745464" + 
":  " + 
"(b('b5') <= 1803.0) ? " + 
"0.0070099173160594885" + 
":  " + 
"-0.0062917725298207855" + 
":  " + 
"(b('g0vv') <= -16.928504943847656) ? " + 
"(b('grass') <= 93.87771987915039) ? " + 
"-0.010937148313043625" + 
":  " + 
"0.005811507208850763" + 
":  " + 
"(b('g0vv') <= -16.92304515838623) ? " + 
"0.1486210245317" + 
":  " + 
"8.11068226548459e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5439.0) ? " + 
"(b('b11') <= 3248.5) ? " + 
"(b('bare') <= 14.846899032592773) ? " + 
"3.862999060279638e-05" + 
":  " + 
"-0.004205355870629834" + 
":  " + 
"(b('g0vv') <= -9.873640537261963) ? " + 
"0.004537339074513317" + 
":  " + 
"-0.006343294412160292" + 
":  " + 
"(b('ndvi') <= 1282.0) ? " + 
"(b('l8dt') <= 288891.0) ? " + 
"-0.0050217560825083565" + 
":  " + 
"0.006610106632733877" + 
":  " + 
"(b('b4') <= 2103.5) ? " + 
"-0.001150978973794542" + 
":  " + 
"-0.020238212585738106" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 5819576.0) ? " + 
"(b('b1') <= 259.5) ? " + 
"(b('b4') <= 695.0) ? " + 
"0.0013777152480863308" + 
":  " + 
"-0.008470652071652937" + 
":  " + 
"(b('b6') <= 1412.0) ? " + 
"-0.028018327613050828" + 
":  " + 
"0.00015809720174980103" + 
":  " + 
"(b('ndvi') <= 1380.0) ? " + 
"(b('l8dt') <= 6299340.5) ? " + 
"0.008051953016457433" + 
":  " + 
"0.05022524383077722" + 
":  " + 
"(b('ndvi') <= 3194.5) ? " + 
"-0.01069726279204021" + 
":  " + 
"0.013936454609143632" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2829.5) ? " + 
"(b('b2') <= 558.5) ? " + 
"(b('b2') <= 542.5) ? " + 
"0.00019089794923310497" + 
":  " + 
"-0.014382825637300103" + 
":  " + 
"(b('b2') <= 562.5) ? " + 
"0.04283363530361919" + 
":  " + 
"0.0027992203120534537" + 
":  " + 
"(b('b6') <= 2831.5) ? " + 
"(b('b4') <= 1058.5) ? " + 
"0.023143312730627346" + 
":  " + 
"-0.053118335626652344" + 
":  " + 
"(b('b11') <= 2152.0) ? " + 
"-0.004093841886518884" + 
":  " + 
"0.0008509890540713354" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 604.5) ? " + 
"(b('g0vh') <= -19.65249729156494) ? " + 
"-0.02867699604430643" + 
":  " + 
"0.14084736671020368" + 
":  " + 
"(b('b5') <= 1320.5) ? " + 
"(b('l8dt') <= 1080269.0) ? " + 
"0.0011100814605307708" + 
":  " + 
"-0.025010143592356926" + 
":  " + 
"(b('b5') <= 1670.0) ? " + 
"0.00547597427547451" + 
":  " + 
"-0.0001107942926131105" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -10.326126098632812) ? " + 
"(b('g0vh') <= -11.303503513336182) ? " + 
"(b('g0vh') <= -11.56062126159668) ? " + 
"7.337609041543502e-06" + 
":  " + 
"-0.04631527996116299" + 
":  " + 
"(b('ndvi') <= 2863.0) ? " + 
"0.0817628860528785" + 
":  " + 
"0.005929163678317018" + 
":  " + 
"(b('l8dt') <= 1036801.0) ? " + 
"-0.07072738134365941" + 
":  " + 
"(b('b4') <= 893.5) ? " + 
"-0.0012751905870775904" + 
":  " + 
"-0.01703917291339721" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1308.5) ? " + 
"(b('l8dt') <= 2785.5) ? " + 
"(b('l8dt') <= 2476.5) ? " + 
"0.051348466674546914" + 
":  " + 
"0.15830200517015441" + 
":  " + 
"(b('b1') <= 436.0) ? " + 
"-0.014233787020524078" + 
":  " + 
"-0.0005810716873005777" + 
":  " + 
"(b('bare') <= 23.27118682861328) ? " + 
"(b('bare') <= 21.937710762023926) ? " + 
"0.00026151133748018754" + 
":  " + 
"-0.025658981466133695" + 
":  " + 
"(b('g0vh') <= -18.569358825683594) ? " + 
"0.013938781998204393" + 
":  " + 
"0.12235132560360612" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('b3') <= 593.5) ? " + 
"(b('b5') <= 3092.5) ? " + 
"-0.0028554859247035057" + 
":  " + 
"-0.10842367647516493" + 
":  " + 
"(b('b3') <= 596.5) ? " + 
"0.022602123418257788" + 
":  " + 
"5.022503798824957e-05" + 
":  " + 
"(b('l8dt') <= 255523.0) ? " + 
"(b('g0vv') <= -9.936842441558838) ? " + 
"-0.016425588612325518" + 
":  " + 
"0.03987996413635392" + 
":  " + 
"(b('lia') <= 34.12309455871582) ? " + 
"-0.013747870573422425" + 
":  " + 
"0.02564729154585601" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2608.5) ? " + 
"(b('b6') <= 2587.5) ? " + 
"(b('bare') <= 0.16549379378557205) ? " + 
"-0.0025040613206759013" + 
":  " + 
"0.002532993970033656" + 
":  " + 
"(b('trees') <= 9.50001573562622) ? " + 
"0.001983179562332681" + 
":  " + 
"0.04171575128772671" + 
":  " + 
"(b('b11') <= 1446.0) ? " + 
"(b('bare') <= 1.4945245385169983) ? " + 
"-0.00610851018661904" + 
":  " + 
"-0.04723350779081447" + 
":  " + 
"(b('b3') <= 550.0) ? " + 
"-0.09417516431738526" + 
":  " + 
"-0.000201206454713498" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 3.9101978540420532) ? " + 
"(b('urban') <= 3.522911548614502) ? " + 
"(b('ndvi') <= 5264.5) ? " + 
"0.00041096645175314614" + 
":  " + 
"-0.004371913192142406" + 
":  " + 
"(b('lia') <= 38.21141052246094) ? " + 
"0.06755222810252827" + 
":  " + 
"0.03793226713761397" + 
":  " + 
"(b('b5') <= 4200.0) ? " + 
"(b('b6') <= 2286.5) ? " + 
"0.0030540338333192403" + 
":  " + 
"-0.003234505061036769" + 
":  " + 
"(b('g0vh') <= -16.681987762451172) ? " + 
"0.09153450872019561" + 
":  " + 
"0.033424094839265395" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.232231140136719) ? " + 
"(b('ndvi') <= 1646.5) ? " + 
"(b('grass') <= 50.58056831359863) ? " + 
"0.00079091258113982" + 
":  " + 
"-0.00775363342616756" + 
":  " + 
"(b('moss') <= 9.849056243896484) ? " + 
"0.0001774921299974333" + 
":  " + 
"0.006623870733620013" + 
":  " + 
"(b('b11') <= 1596.0) ? " + 
"(b('b1') <= 507.0) ? " + 
"-0.011029090124936906" + 
":  " + 
"0.04518647187936052" + 
":  " + 
"(b('b10') <= 1613.5) ? " + 
"0.040710307940812845" + 
":  " + 
"-0.00023247604392155947" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 2.0455974340438843) ? " + 
"(b('moss') <= 0.9462673366069794) ? " + 
"(b('lia') <= 44.296762466430664) ? " + 
"0.00017229768434207367" + 
":  " + 
"-0.057057028614556714" + 
":  " + 
"(b('g0vv') <= -14.297768592834473) ? " + 
"-0.030990605818649205" + 
":  " + 
"0.016194618547062795" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"(b('trees') <= 19.831669807434082) ? " + 
"-0.002124876227701967" + 
":  " + 
"0.008270550197688806" + 
":  " + 
"(b('crop') <= 47.711137771606445) ? " + 
"0.0003419738534754111" + 
":  " + 
"0.04727177830366698" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 823.5) ? " + 
"(b('b6') <= 2608.0) ? " + 
"(b('b6') <= 2587.5) ? " + 
"-0.0003203821449650625" + 
":  " + 
"0.020772327757156102" + 
":  " + 
"(b('ndvi') <= 4608.0) ? " + 
"-0.0024282648094938854" + 
":  " + 
"-0.022407135125590484" + 
":  " + 
"(b('b4') <= 943.5) ? " + 
"(b('crop') <= 83.88826751708984) ? " + 
"0.0034625716769362755" + 
":  " + 
"0.03207164030115387" + 
":  " + 
"(b('b7') <= 1644.0) ? " + 
"-0.010452248650446238" + 
":  " + 
"0.00045197731733440214" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2436.5) ? " + 
"(b('moss') <= 1.6108241081237793) ? " + 
"(b('ndvi') <= 2036.5) ? " + 
"-0.0006078619860235621" + 
":  " + 
"0.01230183098291858" + 
":  " + 
"(b('b5') <= 2379.5) ? " + 
"-0.0016959430105128537" + 
":  " + 
"0.009825808591432564" + 
":  " + 
"(b('b5') <= 2462.5) ? " + 
"(b('trees') <= 17.931958198547363) ? " + 
"-0.004586899694668142" + 
":  " + 
"-0.040894334105757754" + 
":  " + 
"(b('grass') <= 34.980010986328125) ? " + 
"-0.0011153459478729084" + 
":  " + 
"0.0017535100251185052" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b10') <= 1239.0) ? " + 
"(b('b6') <= 2219.5) ? " + 
"(b('crop') <= 94.68265533447266) ? " + 
"-0.0016390149220934364" + 
":  " + 
"0.01797923158219382" + 
":  " + 
"(b('g0vh') <= -16.93438148498535) ? " + 
"-0.030359926762464646" + 
":  " + 
"0.011585936438556219" + 
":  " + 
"(b('b4') <= 592.5) ? " + 
"(b('b11') <= 1373.0) ? " + 
"0.021499928597922553" + 
":  " + 
"-0.013983334702261535" + 
":  " + 
"(b('b3') <= 545.5) ? " + 
"-0.02557560360581544" + 
":  " + 
"8.066809666364419e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1987.5) ? " + 
"(b('bare') <= 2.5217267274856567) ? " + 
"(b('bare') <= 0.16345614939928055) ? " + 
"0.0009594701672281284" + 
":  " + 
"0.012955991718212032" + 
":  " + 
"(b('moss') <= 24.84316349029541) ? " + 
"-0.010228219166642792" + 
":  " + 
"0.0843470693146823" + 
":  " + 
"(b('b3') <= 738.5) ? " + 
"(b('crop') <= 43.67561912536621) ? " + 
"0.001820261569642742" + 
":  " + 
"-0.008586110912800328" + 
":  " + 
"(b('b10') <= 1322.5) ? " + 
"0.007602149499371634" + 
":  " + 
"-8.316127440229585e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.869969367980957) ? " + 
"(b('g0vh') <= -19.910228729248047) ? " + 
"(b('lia') <= 44.32401657104492) ? " + 
"-0.0027037090897348965" + 
":  " + 
"-0.027139215163878787" + 
":  " + 
"(b('grass') <= 87.14754104614258) ? " + 
"0.006315737787031341" + 
":  " + 
"0.0919288844909739" + 
":  " + 
"(b('g0vv') <= -15.865667343139648) ? " + 
"(b('b6') <= 2875.5) ? " + 
"0.1215858170440503" + 
":  " + 
"0.032761136196116356" + 
":  " + 
"(b('g0vh') <= -23.55073833465576) ? " + 
"0.032848358380476866" + 
":  " + 
"0.00011036040587230333" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 630.5) ? " + 
"(b('g0vh') <= -22.91350269317627) ? " + 
"(b('g0vh') <= -23.355777740478516) ? " + 
"0.11373223222081985" + 
":  " + 
"0.057120137688904185" + 
":  " + 
"(b('crop') <= 23.142868041992188) ? " + 
"-0.009053841181449756" + 
":  " + 
"-2.4631339038106673e-05" + 
":  " + 
"(b('g0vh') <= -15.601629734039307) ? " + 
"(b('b3') <= 645.5) ? " + 
"0.013141888426400579" + 
":  " + 
"-0.0002672814406596248" + 
":  " + 
"(b('b11') <= 1438.5) ? " + 
"0.013383937368334438" + 
":  " + 
"-0.00034230321007428763" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 932.5) ? " + 
"(b('b6') <= 3242.5) ? " + 
"(b('moss') <= 19.819469451904297) ? " + 
"5.87166146292399e-05" + 
":  " + 
"-0.017156531403604767" + 
":  " + 
"(b('b7') <= 2001.5) ? " + 
"-0.03547536807436522" + 
":  " + 
"-0.006828336035627987" + 
":  " + 
"(b('b5') <= 1701.0) ? " + 
"(b('g0vv') <= -10.683626174926758) ? " + 
"-0.04485343346371449" + 
":  " + 
"-0.07885196776844978" + 
":  " + 
"(b('b4') <= 1289.5) ? " + 
"0.0047702111158838345" + 
":  " + 
"-0.00038670608486626805" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b10') <= 1782.5) ? " + 
"(b('b1') <= 518.5) ? " + 
"(b('b4') <= 1479.5) ? " + 
"-0.0004269770292476919" + 
":  " + 
"0.05651791061797895" + 
":  " + 
"(b('b6') <= 1999.5) ? " + 
"0.012044496526464627" + 
":  " + 
"-0.02789391999971341" + 
":  " + 
"(b('b10') <= 1788.5) ? " + 
"(b('bare') <= 7.682890892028809) ? " + 
"0.030383667103330465" + 
":  " + 
"0.17688773343985584" + 
":  " + 
"(b('b3') <= 774.0) ? " + 
"-0.008979786195438162" + 
":  " + 
"0.0006762314867874822" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2179.5) ? " + 
"(b('b4') <= 1163.5) ? " + 
"(b('b3') <= 822.5) ? " + 
"0.0007249830251350325" + 
":  " + 
"0.012011663076240511" + 
":  " + 
"(b('g0vh') <= -18.44800853729248) ? " + 
"-0.010221275922805284" + 
":  " + 
"0.015122340090657221" + 
":  " + 
"(b('b5') <= 2265.5) ? " + 
"(b('b5') <= 2262.5) ? " + 
"-0.0037476136669085222" + 
":  " + 
"-0.04554654418118312" + 
":  " + 
"(b('moss') <= 0.06014965660870075) ? " + 
"-0.0022539936489517813" + 
":  " + 
"0.0005575741232644644" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2696.5) ? " + 
"(b('b5') <= 2689.5) ? " + 
"(b('l8dt') <= 347974.5) ? " + 
"0.0032526105369933426" + 
":  " + 
"-0.0010012658700423356" + 
":  " + 
"(b('b3') <= 1137.5) ? " + 
"0.04278106622754833" + 
":  " + 
"-0.010973612243332547" + 
":  " + 
"(b('b5') <= 2700.5) ? " + 
"(b('ndvi') <= 2595.0) ? " + 
"-0.04683098287045105" + 
":  " + 
"-0.007459241562462031" + 
":  " + 
"(b('urban') <= 36.35346794128418) ? " + 
"-0.00025345359121547187" + 
":  " + 
"-0.012805059016364246" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -10.326126098632812) ? " + 
"(b('g0vh') <= -11.947437763214111) ? " + 
"(b('ndvi') <= 2447.5) ? " + 
"0.0005597411232937693" + 
":  " + 
"-0.0007305157364894825" + 
":  " + 
"(b('urban') <= 32.577152252197266) ? " + 
"0.01092475168525356" + 
":  " + 
"0.1295712433384003" + 
":  " + 
"(b('ndvi') <= 2430.0) ? " + 
"-0.0690501505526726" + 
":  " + 
"(b('b11') <= 1992.0) ? " + 
"-0.008662812382110613" + 
":  " + 
"-0.018961092273833663" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 677.5) ? " + 
"(b('b10') <= 2207.0) ? " + 
"(b('moss') <= 7.395158052444458) ? " + 
"0.10075804069304342" + 
":  " + 
"0.002380659467820248" + 
":  " + 
"(b('b7') <= 2560.5) ? " + 
"-0.009033868216951865" + 
":  " + 
"0.011028622210771511" + 
":  " + 
"(b('crop') <= 5.957038402557373) ? " + 
"(b('b4') <= 738.5) ? " + 
"0.009216599973039112" + 
":  " + 
"-0.0021042160587558547" + 
":  " + 
"(b('grass') <= 63.09731101989746) ? " + 
"-0.0001106927043465882" + 
":  " + 
"0.012149872968851295" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 666.5) ? " + 
"(b('b10') <= 1498.0) ? " + 
"(b('b4') <= 609.5) ? " + 
"0.000656484476920796" + 
":  " + 
"-0.009895993120292414" + 
":  " + 
"(b('b7') <= 1598.0) ? " + 
"0.016361288964442052" + 
":  " + 
"-0.002977535234300826" + 
":  " + 
"(b('b1') <= 153.5) ? " + 
"(b('b6') <= 1270.5) ? " + 
"0.03392304205926848" + 
":  " + 
"0.07850066743338618" + 
":  " + 
"(b('b3') <= 688.5) ? " + 
"0.006469984858325729" + 
":  " + 
"-2.483302812798131e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 932.5) ? " + 
"(b('b6') <= 3364.0) ? " + 
"(b('moss') <= 19.819469451904297) ? " + 
"-5.550373110647413e-05" + 
":  " + 
"-0.015353773903298455" + 
":  " + 
"(b('b2') <= 599.5) ? " + 
"-0.004903134170974" + 
":  " + 
"-0.03474218320988843" + 
":  " + 
"(b('b5') <= 2683.5) ? " + 
"(b('b4') <= 1235.5) ? " + 
"0.014608710721038384" + 
":  " + 
"0.0008442474314262593" + 
":  " + 
"(b('b4') <= 949.0) ? " + 
"0.014528636556783553" + 
":  " + 
"-0.0010443277202593782" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1420.5) ? " + 
"(b('b4') <= 1740.5) ? " + 
"(b('b3') <= 1315.5) ? " + 
"-0.00017010186065197395" + 
":  " + 
"0.014466077431058974" + 
":  " + 
"(b('grass') <= 67.97307968139648) ? " + 
"-0.0034984884188680944" + 
":  " + 
"-0.01913202331262608" + 
":  " + 
"(b('b4') <= 1903.0) ? " + 
"(b('trees') <= 12.48423957824707) ? " + 
"0.015601572770177968" + 
":  " + 
"0.12283265965212607" + 
":  " + 
"(b('b5') <= 3309.5) ? " + 
"-0.003064970145154976" + 
":  " + 
"0.0035949560500133327" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3486.5) ? " + 
"(b('b1') <= 311.5) ? " + 
"-0.002108410334926266" + 
":  " + 
"0.0005586380086462893" + 
":  " + 
"(b('g0vv') <= -6.432831287384033) ? " + 
"0.007987116576097908" + 
":  " + 
"0.08379824968013533" + 
":  " + 
"(b('b10') <= 2622.0) ? " + 
"(b('bare') <= 9.22737455368042) ? " + 
"-0.005162255242282811" + 
":  " + 
"0.04610735293139021" + 
":  " + 
"(b('b7') <= 2629.0) ? " + 
"0.06767984262857697" + 
":  " + 
"0.0012348405703475824" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 1.3701354265213013) ? " + 
"(b('bare') <= 1.3413746356964111) ? " + 
"(b('trees') <= 10.338415622711182) ? " + 
"-0.001220197418457836" + 
":  " + 
"0.002078207945145312" + 
":  " + 
"(b('b1') <= 329.0) ? " + 
"-0.070581508473273" + 
":  " + 
"-0.008398243854461574" + 
":  " + 
"(b('bare') <= 1.3976932764053345) ? " + 
"(b('b5') <= 3263.5) ? " + 
"0.018478368133648473" + 
":  " + 
"0.10473591878407357" + 
":  " + 
"(b('g0vv') <= -10.768578052520752) ? " + 
"-0.0011142421219623988" + 
":  " + 
"0.0034196666783459927" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.43209266662598) ? " + 
"(b('lia') <= 38.30871772766113) ? " + 
"(b('lia') <= 38.30740928649902) ? " + 
"-0.00043195400462474174" + 
":  " + 
"0.1498020569667279" + 
":  " + 
"(b('bare') <= 2.403625726699829) ? " + 
"-0.0355252479922278" + 
":  " + 
"0.026213329753289917" + 
":  " + 
"(b('lia') <= 38.45518112182617) ? " + 
"(b('grass') <= 37.62586736679077) ? " + 
"-0.06025226881626799" + 
":  " + 
"0.04623525933155499" + 
":  " + 
"(b('lia') <= 38.85244369506836) ? " + 
"0.007629818417858159" + 
":  " + 
"-1.3825622889434451e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2447.5) ? " + 
"(b('ndvi') <= 2100.5) ? " + 
"(b('grass') <= 74.57086563110352) ? " + 
"0.0008530946444475921" + 
":  " + 
"-0.004980321415671907" + 
":  " + 
"(b('g0vh') <= -20.863892555236816) ? " + 
"0.016709360814379737" + 
":  " + 
"0.0018080964070819054" + 
":  " + 
"(b('grass') <= 46.00799369812012) ? " + 
"(b('crop') <= 34.76737403869629) ? " + 
"-0.012499522388344198" + 
":  " + 
"-0.0013454449736807867" + 
":  " + 
"(b('g0vv') <= -11.187055587768555) ? " + 
"-0.0005406960098113115" + 
":  " + 
"0.017851939707839912" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1709.5) ? " + 
"(b('b4') <= 1112.0) ? " + 
"(b('b3') <= 802.0) ? " + 
"0.0019351235819111622" + 
":  " + 
"0.030428087793777616" + 
":  " + 
"(b('g0vh') <= -21.258334159851074) ? " + 
"-0.005616377274375086" + 
":  " + 
"-0.05742724702337781" + 
":  " + 
"(b('b5') <= 1713.5) ? " + 
"(b('g0vh') <= -19.214689254760742) ? " + 
"-0.027979258020159492" + 
":  " + 
"-0.07352937547844547" + 
":  " + 
"(b('b3') <= 461.5) ? " + 
"-0.041623701822940465" + 
":  " + 
"-6.613197017994873e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 4840.5) ? " + 
"(b('b6') <= 4769.0) ? " + 
"(b('b2') <= 1996.0) ? " + 
"1.4257291985402978e-05" + 
":  " + 
"0.04983522572333686" + 
":  " + 
"(b('b1') <= 1556.0) ? " + 
"0.0257102927532104" + 
":  " + 
"-0.02060483002487608" + 
":  " + 
"(b('l8dt') <= 1312456.5) ? " + 
"(b('ndvi') <= 2746.0) ? " + 
"0.0014190874233721083" + 
":  " + 
"0.0785253792307779" + 
":  " + 
"(b('b10') <= 3609.0) ? " + 
"-0.0345435758999649" + 
":  " + 
"-0.005623374836261474" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4384.5) ? " + 
"(b('b5') <= 4360.0) ? " + 
"(b('b10') <= 1239.0) ? " + 
"-0.0023564503752788687" + 
":  " + 
"0.00021912375750676326" + 
":  " + 
"(b('moss') <= 1.9971346855163574) ? " + 
"0.04247679534186572" + 
":  " + 
"-0.027827069203125707" + 
":  " + 
"(b('b3') <= 927.0) ? " + 
"(b('lia') <= 31.641416549682617) ? " + 
"0.012525194745861695" + 
":  " + 
"-0.05597427567205107" + 
":  " + 
"(b('l8dt') <= 2030167.0) ? " + 
"0.0009008768741649176" + 
":  " + 
"-0.024223260561461384" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 5819576.0) ? " + 
"(b('l8dt') <= 5788343.5) ? " + 
"(b('b5') <= 1709.5) ? " + 
"0.0032440828257766755" + 
":  " + 
"-0.00017382996300836087" + 
":  " + 
"-0.08681761587176556" + 
":  " + 
"(b('b7') <= 1344.5) ? " + 
"(b('g0vv') <= -10.348659992218018) ? " + 
"0.027763765455402285" + 
":  " + 
"0.07222722529949453" + 
":  " + 
"(b('ndvi') <= 1380.0) ? " + 
"0.03042386586702531" + 
":  " + 
"-0.0005953263595197492" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 24.503172874450684) ? " + 
"(b('trees') <= 23.840930938720703) ? " + 
"-2.780913449569364e-05" + 
":  " + 
"0.010882245997816151" + 
":  " + 
"(b('b1') <= 503.0) ? " + 
"-0.02544497310447463" + 
":  " + 
"0.005384660582300689" + 
":  " + 
"(b('l8dt') <= 255523.0) ? " + 
"(b('g0vh') <= -18.545451164245605) ? " + 
"0.03914780299591111" + 
":  " + 
"-0.015035922248667991" + 
":  " + 
"(b('b6') <= 2423.5) ? " + 
"0.0391407404803529" + 
":  " + 
"0.006099894669602295" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 1.3701354265213013) ? " + 
"(b('bare') <= 1.0953277349472046) ? " + 
"(b('trees') <= 10.338415622711182) ? " + 
"-0.0011338956176397141" + 
":  " + 
"0.0022888974690092752" + 
":  " + 
"(b('g0vv') <= -9.75899362564087) ? " + 
"-0.022542678424715367" + 
":  " + 
"0.03707268100723962" + 
":  " + 
"(b('bare') <= 1.3976932764053345) ? " + 
"(b('b5') <= 3263.5) ? " + 
"0.01664915505043546" + 
":  " + 
"0.094443505805316" + 
":  " + 
"(b('crop') <= 94.83395767211914) ? " + 
"0.0005754276929231095" + 
":  " + 
"-0.04777736425051296" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 4.659861326217651) ? " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"(b('b10') <= 1991.5) ? " + 
"-0.0047976712957638985" + 
":  " + 
"0.0017540269952937637" + 
":  " + 
"(b('trees') <= 4.114237546920776) ? " + 
"0.05276785567317283" + 
":  " + 
"0.0031999165366034727" + 
":  " + 
"(b('b4') <= 787.5) ? " + 
"(b('grass') <= 76.45126724243164) ? " + 
"0.0015559049164699708" + 
":  " + 
"0.024809030791603195" + 
":  " + 
"(b('ndvi') <= 1823.5) ? " + 
"0.000892505066799004" + 
":  " + 
"-0.0037909260416147013" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 675.5) ? " + 
"(b('ndvi') <= 3553.0) ? " + 
"(b('ndvi') <= 3515.0) ? " + 
"9.555745702672994e-06" + 
":  " + 
"0.03003853479655035" + 
":  " + 
"(b('ndvi') <= 3575.5) ? " + 
"-0.05009305281105229" + 
":  " + 
"-0.005494712100588597" + 
":  " + 
"(b('b4') <= 557.0) ? " + 
"(b('lia') <= 41.037363052368164) ? " + 
"0.04286400879231262" + 
":  " + 
"0.07403092328878703" + 
":  " + 
"(b('b3') <= 688.5) ? " + 
"0.009856356240780262" + 
":  " + 
"-4.634270070557252e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 728.5) ? " + 
"(b('l8dt') <= 688397.5) ? " + 
"(b('l8dt') <= 684086.0) ? " + 
"0.0012948808605315284" + 
":  " + 
"0.060438316597912156" + 
":  " + 
"(b('b3') <= 704.5) ? " + 
"-0.00248954398747635" + 
":  " + 
"-0.016137971286085004" + 
":  " + 
"(b('b3') <= 732.5) ? " + 
"(b('moss') <= 18.854540824890137) ? " + 
"0.015869668086549993" + 
":  " + 
"0.10811055222339946" + 
":  " + 
"(b('moss') <= 4.659861326217651) ? " + 
"0.0013931077143236287" + 
":  " + 
"-0.0008912011935753559" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -5.72271203994751) ? " + 
"(b('ndvi') <= 6923.0) ? " + 
"(b('ndvi') <= 6838.5) ? " + 
"-8.879167224583343e-05" + 
":  " + 
"-0.05128980790606511" + 
":  " + 
"(b('trees') <= 10.456944465637207) ? " + 
"0.0012114871434589238" + 
":  " + 
"0.057633550549439784" + 
":  " + 
"(b('g0vv') <= -5.707797050476074) ? " + 
"(b('trees') <= 0.17499999701976776) ? " + 
"0.14550974672709133" + 
":  " + 
"0.05628775719890885" + 
":  " + 
"(b('b4') <= 1872.0) ? " + 
"-0.0013512791345990985" + 
":  " + 
"0.0297454192336183" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1987.5) ? " + 
"(b('bare') <= 2.5217267274856567) ? " + 
"(b('bare') <= 0.16345614939928055) ? " + 
"0.0009368227073671251" + 
":  " + 
"0.011813297114652134" + 
":  " + 
"(b('grass') <= 86.04516220092773) ? " + 
"-0.004129104721893994" + 
":  " + 
"-0.06635533295429016" + 
":  " + 
"(b('b3') <= 738.5) ? " + 
"(b('moss') <= 1.719908595085144) ? " + 
"-0.009910925217521356" + 
":  " + 
"0.0004362153571437775" + 
":  " + 
"(b('b6') <= 2210.0) ? " + 
"0.007468060581996943" + 
":  " + 
"-8.257317205207057e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  return prediction