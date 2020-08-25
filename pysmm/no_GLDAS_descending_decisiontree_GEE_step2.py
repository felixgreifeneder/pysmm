import ee 

def tree(feature_stack): 

  prediction = ee.Image(0.013654683)
  learning_rate = ee.Image(0.1)
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 1.1855096817016602) ? " + 
"(b('L8b6') <= 2659.5) ? " + 
"(b('bulk') <= 144.5) ? " + 
"-0.005745659339842359" + 
":  " + 
"0.04543138690808389" + 
":  " + 
"(b('L8dt') <= 800762.5) ? " + 
"-0.02244512896136357" + 
":  " + 
"-0.005901733039264105" + 
":  " + 
"(b('crop') <= 5.652343273162842) ? " + 
"(b('L8b6') <= 2845.0) ? " + 
"0.11129111582961153" + 
":  " + 
"0.04360671181870929" + 
":  " + 
"(b('L8b6') <= 2662.0) ? " + 
"0.04628807980495919" + 
":  " + 
"0.017180744972436362" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 0.9197440147399902) ? " + 
"(b('L8b6') <= 2603.5) ? " + 
"(b('L8b6med') <= 2818.5) ? " + 
"-0.007009591289580325" + 
":  " + 
"0.037602705728909044" + 
":  " + 
"(b('L8dt') <= 927243.5) ? " + 
"-0.02056828215039719" + 
":  " + 
"-0.004953429233952966" + 
":  " + 
"(b('dgvv') <= 2.172456741333008) ? " + 
"(b('L8b6') <= 2822.5) ? " + 
"0.03322397863860075" + 
":  " + 
"0.004581322828103184" + 
":  " + 
"(b('crop') <= 4.842228651046753) ? " + 
"0.0924981169321158" + 
":  " + 
"0.03965371029755896" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 1.4437060356140137) ? " + 
"(b('dsvv') <= -0.021214962005615234) ? " + 
"(b('L8dt') <= 1145308.0) ? " + 
"-0.01964045641148892" + 
":  " + 
"-0.001994484436649035" + 
":  " + 
"(b('L8b6') <= 2659.5) ? " + 
"0.019794868014876208" + 
":  " + 
"-0.006214669363610061" + 
":  " + 
"(b('lon') <= -116.37591552734375) ? " + 
"(b('ndvi') <= 2173.5) ? " + 
"0.050836146070601065" + 
":  " + 
"0.15559689999962628" + 
":  " + 
"(b('clay') <= 12.5) ? " + 
"-0.012229993887284173" + 
":  " + 
"0.03798110565972799" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 0.9197440147399902) ? " + 
"(b('L8b6') <= 2193.5) ? " + 
"(b('bulk') <= 144.5) ? " + 
"-0.0008270083772831002" + 
":  " + 
"0.06084207765968442" + 
":  " + 
"(b('L8dt') <= 1404520.0) ? " + 
"-0.014615744650320023" + 
":  " + 
"0.0038353122651302645" + 
":  " + 
"(b('dgvv') <= 2.330021381378174) ? " + 
"(b('L8b5') <= 2417.5) ? " + 
"0.036508912871410504" + 
":  " + 
"0.007856912438162715" + 
":  " + 
"(b('lat') <= 55.879150390625) ? " + 
"0.05411496478649139" + 
":  " + 
"-0.025146830028092062" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 0.5687389373779297) ? " + 
"(b('L8dt') <= 713553.5) ? " + 
"(b('lon') <= -105.18899917602539) ? " + 
"-0.00494079830174356" + 
":  " + 
"-0.020707433183851334" + 
":  " + 
"(b('L8b6') <= 2086.5) ? " + 
"0.027014260979454745" + 
":  " + 
"-0.0032155721845088347" + 
":  " + 
"(b('dgvv') <= 2.172456741333008) ? " + 
"(b('L8b6') <= 2822.5) ? " + 
"0.02344266984276327" + 
":  " + 
"-0.0005005522119165013" + 
":  " + 
"(b('lon') <= -106.84210205078125) ? " + 
"0.08698092270363941" + 
":  " + 
"0.0319840122646337" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 1.4425129890441895) ? " + 
"(b('dsvv') <= -0.08262062072753906) ? " + 
"(b('ndvi_med') <= 1884.5) ? " + 
"-0.004097129672298217" + 
":  " + 
"-0.019131898164379046" + 
":  " + 
"(b('L8b6') <= 3140.5) ? " + 
"0.01118004420163404" + 
":  " + 
"-0.010023015871364472" + 
":  " + 
"(b('crop') <= 4.842228651046753) ? " + 
"(b('ndvi') <= 3032.0) ? " + 
"0.0413921798093001" + 
":  " + 
"0.11614810613600708" + 
":  " + 
"(b('clay') <= 17.5) ? " + 
"-0.009212211250794486" + 
":  " + 
"0.0278245310797052" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.5396823883056641) ? " + 
"(b('L8b6') <= 3155.0) ? " + 
"(b('L8b6med') <= 3095.5) ? " + 
"-0.008974357071516607" + 
":  " + 
"0.02297784739333364" + 
":  " + 
"(b('L8b11') <= 2543.0) ? " + 
"-0.022848504416983984" + 
":  " + 
"-0.01007233791224259" + 
":  " + 
"(b('L8b6') <= 2760.5) ? " + 
"(b('L8b4med') <= 1166.0) ? " + 
"0.01259563225685537" + 
":  " + 
"0.061837740998375024" + 
":  " + 
"(b('L8dt') <= 816280.0) ? " + 
"-0.0018231324186202263" + 
":  " + 
"0.02049426527480172" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 1.688237190246582) ? " + 
"(b('L8b6') <= 2217.5) ? " + 
"(b('bulk') <= 144.5) ? " + 
"0.0028341377321758304" + 
":  " + 
"0.05411081465561327" + 
":  " + 
"(b('L8b2') <= 363.5) ? " + 
"-0.05293688995087477" + 
":  " + 
"-0.006128371431622131" + 
":  " + 
"(b('lon') <= -116.37591552734375) ? " + 
"(b('ndvi') <= 1976.0) ? " + 
"0.028792644560595826" + 
":  " + 
"0.12142127948998016" + 
":  " + 
"(b('clay') <= 9.5) ? " + 
"-0.021003147807889273" + 
":  " + 
"0.02593875829899986" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -5.421676158905029) ? " + 
"(b('L8dt') <= 800762.5) ? " + 
"(b('lon') <= -105.18899917602539) ? " + 
"-0.000934962721595932" + 
":  " + 
"-0.015229875560331518" + 
":  " + 
"(b('lon') <= 7.651569843292236) ? " + 
"0.012184928346320125" + 
":  " + 
"-0.00904283947081893" + 
":  " + 
"(b('dsvv') <= 2.387307643890381) ? " + 
"(b('L8b4') <= 543.5) ? " + 
"0.0669879691609488" + 
":  " + 
"0.010358117430902524" + 
":  " + 
"(b('lon') <= -107.0709114074707) ? " + 
"0.09039543283987186" + 
":  " + 
"0.03374237140648134" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.3151097297668457) ? " + 
"(b('L8dt') <= 1404520.0) ? " + 
"(b('clay') <= 10.5) ? " + 
"-0.03851067024934437" + 
":  " + 
"-0.008523744058828312" + 
":  " + 
"(b('L8b6') <= 2603.5) ? " + 
"0.015183707809127414" + 
":  " + 
"-0.003060429666045248" + 
":  " + 
"(b('L8b6') <= 2662.5) ? " + 
"(b('bulk') <= 147.5) ? " + 
"0.015383166667592346" + 
":  " + 
"0.07148261806760142" + 
":  " + 
"(b('dgvh') <= -3.0671377182006836) ? " + 
"0.0012024327756787368" + 
":  " + 
"0.03530641873056693" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -5.421676158905029) ? " + 
"(b('L8dt') <= 800762.5) ? " + 
"(b('lon') <= -105.18899917602539) ? " + 
"-0.0004262089405530044" + 
":  " + 
"-0.013184617804757826" + 
":  " + 
"(b('lon') <= 7.651569843292236) ? " + 
"0.01074679314316886" + 
":  " + 
"-0.0082755267261811" + 
":  " + 
"(b('dgvv') <= 2.84679913520813) ? " + 
"(b('L8b4') <= 543.5) ? " + 
"0.06293822828750538" + 
":  " + 
"0.009722150985119509" + 
":  " + 
"(b('lon') <= -107.0709114074707) ? " + 
"0.08715237433132349" + 
":  " + 
"0.031592254154914644" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.3151097297668457) ? " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('lat') <= 41.40902519226074) ? " + 
"0.02220172100502538" + 
":  " + 
"-0.007052201838330909" + 
":  " + 
"(b('ndvi_med') <= 1884.5) ? " + 
"-0.00654851035779588" + 
":  " + 
"-0.01948327605362978" + 
":  " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b6med') <= 2818.5) ? " + 
"0.007421639783535866" + 
":  " + 
"0.040981610563362234" + 
":  " + 
"(b('lon') <= 147.51610565185547) ? " + 
"2.8716070986427657e-05" + 
":  " + 
"0.11706748319566633" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvh') <= -5.832070827484131) ? " + 
"(b('L8b5') <= 1935.5) ? " + 
"(b('ndvi') <= 4556.5) ? " + 
"0.019209325484210504" + 
":  " + 
"-0.06371980757022996" + 
":  " + 
"(b('L8b3') <= 456.0) ? " + 
"-0.2687167338105566" + 
":  " + 
"-0.006223860055869413" + 
":  " + 
"(b('lon') <= -116.70380401611328) ? " + 
"(b('ndvi') <= 2672.0) ? " + 
"0.020176164670691086" + 
":  " + 
"0.12457141578415941" + 
":  " + 
"(b('dgvv') <= 1.9994592666625977) ? " + 
"0.0036406819714161908" + 
":  " + 
"0.023766354950793163" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.3151097297668457) ? " + 
"(b('clay') <= 9.5) ? " + 
"(b('gvv') <= -15.553319454193115) ? " + 
"-0.11056842989573659" + 
":  " + 
"-0.017769189038154377" + 
":  " + 
"(b('L8b6') <= 2603.5) ? " + 
"0.006441414808411407" + 
":  " + 
"-0.00824981638590214" + 
":  " + 
"(b('L8b5') <= 2454.0) ? " + 
"(b('L8b3med') <= 964.5) ? " + 
"0.009914027022128433" + 
":  " + 
"0.03389398204515371" + 
":  " + 
"(b('L8b2') <= 306.5) ? " + 
"0.05772338474418278" + 
":  " + 
"0.0015172111754123778" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvh') <= -5.832070827484131) ? " + 
"(b('L8dt') <= 634135.5) ? " + 
"(b('L8b6') <= 1922.0) ? " + 
"0.021780365629710488" + 
":  " + 
"-0.009466833851909901" + 
":  " + 
"(b('lon') <= 7.651569843292236) ? " + 
"0.007561850949842486" + 
":  " + 
"-0.008264087978066914" + 
":  " + 
"(b('lon') <= -116.70380401611328) ? " + 
"(b('ndvi') <= 2672.0) ? " + 
"0.017802022467555582" + 
":  " + 
"0.11102343383584726" + 
":  " + 
"(b('L8dt') <= 815741.0) ? " + 
"0.0016587113905709944" + 
":  " + 
"0.018725573263377124" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 1.9310264587402344) ? " + 
"(b('L8b6') <= 2068.5) ? " + 
"(b('lon') <= -120.94869613647461) ? " + 
"0.15572443319235937" + 
":  " + 
"0.014099717047552005" + 
":  " + 
"(b('L8dt') <= 1405250.5) ? " + 
"-0.005788312271575519" + 
":  " + 
"0.006452811421649938" + 
":  " + 
"(b('moss') <= 22.26679039001465) ? " + 
"(b('L8b6med') <= 2158.75) ? " + 
"-0.08128302916125454" + 
":  " + 
"0.01636327922994343" + 
":  " + 
"(b('gvv') <= -12.434161186218262) ? " + 
"-0.014545377349945718" + 
":  " + 
"0.13443238401015953" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -0.1168966293334961) ? " + 
"(b('ndvi_med') <= 1884.5) ? " + 
"(b('L8b6') <= 3254.5) ? " + 
"0.016239699877397342" + 
":  " + 
"-0.006900163164889685" + 
":  " + 
"(b('gvv') <= -15.078478336334229) ? " + 
"-0.027389558996795522" + 
":  " + 
"-0.008914920591415977" + 
":  " + 
"(b('L8b6') <= 2659.5) ? " + 
"(b('L8b4med') <= 1166.0) ? " + 
"0.005400764610005578" + 
":  " + 
"0.03618414576079765" + 
":  " + 
"(b('L8dt') <= 655690.0) ? " + 
"-0.00474001405610032" + 
":  " + 
"0.007796724956143968" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvh') <= -5.815939903259277) ? " + 
"(b('L8b5') <= 2123.5) ? " + 
"(b('ndvi') <= 4556.5) ? " + 
"0.009606135770899383" + 
":  " + 
"-0.03851899624534453" + 
":  " + 
"(b('L8b4med') <= 1348.25) ? " + 
"-0.010699066291424015" + 
":  " + 
"-0.0008705742069435748" + 
":  " + 
"(b('moss') <= 22.670955657958984) ? " + 
"(b('dgvv') <= 2.8459320068359375) ? " + 
"0.004653643359562501" + 
":  " + 
"0.025555550786647573" + 
":  " + 
"(b('L8b1') <= 635.0) ? " + 
"0.10701667533702752" + 
":  " + 
"0.011506701083445106" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b6med') <= 2818.5) ? " + 
"(b('L8b6') <= 2846.0) ? " + 
"-0.0019443666704460174" + 
":  " + 
"0.17264157340740605" + 
":  " + 
"(b('lon') <= -112.61119079589844) ? " + 
"0.05052936710141748" + 
":  " + 
"0.01554705269074362" + 
":  " + 
"(b('ndvi_med') <= 3617.5) ? " + 
"(b('lat') <= 56.00399971008301) ? " + 
"-0.0039487305321223845" + 
":  " + 
"0.10989476953021556" + 
":  " + 
"(b('L8b3') <= 759.5) ? " + 
"-0.1083741773672016" + 
":  " + 
"-0.02391656867432309" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 800762.5) ? " + 
"(b('crop') <= 8.081742763519287) ? " + 
"(b('ndvi') <= 3132.5) ? " + 
"-0.0008730233679353506" + 
":  " + 
"0.043186921733968826" + 
":  " + 
"(b('L8b3med') <= 564.0) ? " + 
"-0.05751157999198569" + 
":  " + 
"-0.006908313005189068" + 
":  " + 
"(b('dsvv') <= -0.15652990341186523) ? " + 
"(b('ndvi_med') <= 1370.0) ? " + 
"0.021449798053403038" + 
":  " + 
"-0.003472038309456405" + 
":  " + 
"(b('bulk') <= 135.5) ? " + 
"0.0024948928222748553" + 
":  " + 
"0.02123739245010984" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2603.5) ? " + 
"(b('L8b6med') <= 2584.0) ? " + 
"(b('gvv') <= -15.692749500274658) ? " + 
"-0.0941467395788402" + 
":  " + 
"-0.0006007837076879477" + 
":  " + 
"(b('lon') <= -116.34695434570312) ? " + 
"0.05778711476492486" + 
":  " + 
"0.013767496108884524" + 
":  " + 
"(b('L8b11') <= 2243.0) ? " + 
"(b('dsvh') <= -5.915660858154297) ? " + 
"-0.011954582106387305" + 
":  " + 
"0.0006760863795266306" + 
":  " + 
"(b('L8b6') <= 3467.5) ? " + 
"0.00932740268706356" + 
":  " + 
"-0.005030943118348924" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2353526.5) ? " + 
"(b('dgvh') <= -6.352293014526367) ? " + 
"(b('lon') <= -105.18899917602539) ? " + 
"0.0018959080706354395" + 
":  " + 
"-0.008113072966042838" + 
":  " + 
"(b('moss') <= 26.31478500366211) ? " + 
"0.003482960125740733" + 
":  " + 
"0.07372897708711854" + 
":  " + 
"(b('clay') <= 10.5) ? " + 
"(b('ndvi') <= 2945.0) ? " + 
"0.05112660362580145" + 
":  " + 
"-0.018792738274676642" + 
":  " + 
"(b('L8b5') <= 2020.5) ? " + 
"0.05195479611601381" + 
":  " + 
"0.017438000611998305" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 1346052.0) ? " + 
"(b('ndvi_med') <= 3346.0) ? " + 
"(b('L8b6') <= 2274.0) ? " + 
"0.0155212273652317" + 
":  " + 
"-0.002556485911694449" + 
":  " + 
"(b('ndvi') <= 2801.0) ? " + 
"0.02080999885274357" + 
":  " + 
"-0.02006429497623838" + 
":  " + 
"(b('clay') <= 10.5) ? " + 
"(b('ndvi') <= 2955.0) ? " + 
"0.05671692282664487" + 
":  " + 
"-0.016961367627710028" + 
":  " + 
"(b('L8b6') <= 2604.5) ? " + 
"0.022227217935278765" + 
":  " + 
"0.004871066557365206" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 2.330021381378174) ? " + 
"(b('L8b4') <= 532.5) ? " + 
"(b('L8b5') <= 2507.5) ? " + 
"0.004569608052833237" + 
":  " + 
"0.06037055041216892" + 
":  " + 
"(b('L8b11') <= 1364.5) ? " + 
"-0.02859107375003755" + 
":  " + 
"-0.0011612790845401601" + 
":  " + 
"(b('crop') <= 4.842228651046753) ? " + 
"(b('bulk') <= 158.0) ? " + 
"0.03070717755952035" + 
":  " + 
"0.09592682438002206" + 
":  " + 
"(b('clay') <= 17.5) ? " + 
"-0.02034379677373346" + 
":  " + 
"0.012912201924769995" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 3127.5) ? " + 
"(b('L8b6med') <= 3096.5) ? " + 
"(b('dgvv') <= -0.8056073188781738) ? " + 
"-0.011338058502643715" + 
":  " + 
"0.0029946733229206744" + 
":  " + 
"(b('sand') <= 39.5) ? " + 
"0.04271928431749089" + 
":  " + 
"0.012755403364085541" + 
":  " + 
"(b('dsvh') <= -3.046065330505371) ? " + 
"(b('L8b3med') <= 944.5) ? " + 
"-0.01728627502696505" + 
":  " + 
"-0.0036184236403563707" + 
":  " + 
"(b('crop') <= 28.164958000183105) ? " + 
"0.06717080098055253" + 
":  " + 
"0.011611376468962348" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2353526.5) ? " + 
"(b('L8b6') <= 1921.0) ? " + 
"(b('dgvv') <= -1.257734775543213) ? " + 
"-0.021497664182059888" + 
":  " + 
"0.025222958120145682" + 
":  " + 
"(b('L8b3') <= 456.0) ? " + 
"-0.20730224479327847" + 
":  " + 
"-0.0020618826066497765" + 
":  " + 
"(b('lon') <= 6.310510158538818) ? " + 
"(b('L8b6') <= 2604.0) ? " + 
"0.04101403392728265" + 
":  " + 
"0.01352419647463317" + 
":  " + 
"(b('ndvi') <= 2844.5) ? " + 
"0.01923974091223741" + 
":  " + 
"-0.0046207547634261196" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 800762.5) ? " + 
"(b('crop') <= 44.79741096496582) ? " + 
"(b('ndvi') <= 2314.5) ? " + 
"-0.0031854514952423" + 
":  " + 
"0.010804533592905011" + 
":  " + 
"(b('L8b6') <= 1917.0) ? " + 
"0.014146467104364648" + 
":  " + 
"-0.007596776978477139" + 
":  " + 
"(b('bulk') <= 137.5) ? " + 
"(b('ndvi') <= 2751.5) ? " + 
"0.009713138912033419" + 
":  " + 
"-0.007037095446741105" + 
":  " + 
"(b('dsvv') <= 0.8484463691711426) ? " + 
"0.0037043490755386964" + 
":  " + 
"0.02374504829578499" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -5.421253204345703) ? " + 
"(b('clay') <= 9.5) ? " + 
"(b('L8b7') <= 1332.5) ? " + 
"-0.04458891217902645" + 
":  " + 
"-0.0058225781346893084" + 
":  " + 
"(b('L8b6') <= 2067.5) ? " + 
"0.01519615420285328" + 
":  " + 
"-0.001991456532386995" + 
":  " + 
"(b('L8b4') <= 543.5) ? " + 
"(b('L8b5') <= 2440.5) ? " + 
"-0.004806294220001414" + 
":  " + 
"0.06285677475691523" + 
":  " + 
"(b('L8b3med') <= 673.25) ? " + 
"-0.017405775757996345" + 
":  " + 
"0.007663669932545183" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2847.5) ? " + 
"(b('lat') <= 41.383649826049805) ? " + 
"(b('lon') <= -120.0948715209961) ? " + 
"0.04304023002741939" + 
":  " + 
"0.013815858783614401" + 
":  " + 
"(b('L8b3') <= 1459.5) ? " + 
"-0.0008579557313959746" + 
":  " + 
"0.17378789616543464" + 
":  " + 
"(b('L8b11') <= 2243.0) ? " + 
"(b('L8b11') <= 1349.0) ? " + 
"0.04477045816942049" + 
":  " + 
"-0.009547613377561682" + 
":  " + 
"(b('dsvv') <= 3.054617404937744) ? " + 
"-0.0015661270873381038" + 
":  " + 
"0.022677566269298066" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2353526.5) ? " + 
"(b('dgvv') <= -2.487499713897705) ? " + 
"(b('L8b11') <= 1319.0) ? " + 
"-0.10212984617919753" + 
":  " + 
"-0.014892183101800812" + 
":  " + 
"(b('L8b6') <= 1921.0) ? " + 
"0.01616506585002849" + 
":  " + 
"-0.0010624137996705673" + 
":  " + 
"(b('lon') <= -5.374845027923584) ? " + 
"(b('gvv') <= -11.104038715362549) ? " + 
"0.013211858468828903" + 
":  " + 
"0.05233003032160075" + 
":  " + 
"(b('L8b6') <= 4860.5) ? " + 
"0.007912816741345413" + 
":  " + 
"-0.045536688713173054" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -0.578129768371582) ? " + 
"(b('L8b2') <= 363.5) ? " + 
"(b('L8b4') <= 534.0) ? " + 
"0.021507075760240878" + 
":  " + 
"-0.049522862454530414" + 
":  " + 
"(b('ndvi_med') <= 1492.5) ? " + 
"0.009034874445590797" + 
":  " + 
"-0.005461021622564856" + 
":  " + 
"(b('L8b6') <= 2410.5) ? " + 
"(b('L8b6med') <= 2391.5) ? " + 
"-0.009421759412424076" + 
":  " + 
"0.019159534642070392" + 
":  " + 
"(b('L8b2') <= 333.5) ? " + 
"-0.05322574280498077" + 
":  " + 
"0.00026058358753104356" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 1346052.0) ? " + 
"(b('lat') <= 44.78466033935547) ? " + 
"(b('L8b6') <= 3102.5) ? " + 
"0.005714569876419" + 
":  " + 
"-0.0038031285777335145" + 
":  " + 
"(b('L8b4') <= 523.5) ? " + 
"0.03741225692133126" + 
":  " + 
"-0.009493013902521582" + 
":  " + 
"(b('moss') <= 24.536961555480957) ? " + 
"(b('L8b6') <= 4860.5) ? " + 
"0.0066352661381131935" + 
":  " + 
"-0.04402695610708258" + 
":  " + 
"(b('lon') <= -118.07294464111328) ? " + 
"0.208981861367432" + 
":  " + 
"0.033928167431047124" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -106.99930191040039) ? " + 
"(b('L8b4') <= 826.5) ? " + 
"(b('L8b3') <= 724.5) ? " + 
"0.029798163693039316" + 
":  " + 
"0.09717638261893896" + 
":  " + 
"(b('dsvv') <= 2.392037868499756) ? " + 
"-4.41197611737487e-05" + 
":  " + 
"0.03342033110822281" + 
":  " + 
"(b('L8dt') <= 1880360.5) ? " + 
"(b('dsvv') <= -1.1768131256103516) ? " + 
"-0.0109137593235487" + 
":  " + 
"-0.0011343523351069267" + 
":  " + 
"(b('lon') <= 6.310510158538818) ? " + 
"0.014525446753704624" + 
":  " + 
"-0.0004896910321301517" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -6.351731300354004) ? " + 
"(b('L8b3med') <= 952.5) ? " + 
"(b('L8b3') <= 1438.5) ? " + 
"-0.0071821523134487615" + 
":  " + 
"0.04704777535231081" + 
":  " + 
"(b('L8b4') <= 1402.5) ? " + 
"0.013462857307337296" + 
":  " + 
"-0.0035968505594288895" + 
":  " + 
"(b('moss') <= 26.31478500366211) ? " + 
"(b('lon') <= -116.70380401611328) ? " + 
"0.020116267777298996" + 
":  " + 
"0.0016405837091639478" + 
":  " + 
"(b('dgvv') <= 0.7308597564697266) ? " + 
"0.006668589504719221" + 
":  " + 
"0.08460288260019633" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 653115.0) ? " + 
"(b('ndvi') <= 4623.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"-0.0017874227768112751" + 
":  " + 
"0.14622685998194696" + 
":  " + 
"(b('sand') <= 78.5) ? " + 
"-0.014485986636876539" + 
":  " + 
"-0.09156468887827277" + 
":  " + 
"(b('lon') <= -5.3890299797058105) ? " + 
"(b('L8b4') <= 1413.5) ? " + 
"0.020172185176253576" + 
":  " + 
"0.0008602204989646952" + 
":  " + 
"(b('dgvh') <= -10.107518196105957) ? " + 
"-0.0166709719179108" + 
":  " + 
"0.0014394306562392658" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -16.012653350830078) ? " + 
"(b('L8b3') <= 576.5) ? " + 
"(b('L8b4') <= 534.0) ? " + 
"0.04416493725555646" + 
":  " + 
"-0.13271327505213232" + 
":  " + 
"(b('L8b3') <= 1146.5) ? " + 
"-0.0011087558932556276" + 
":  " + 
"-0.018716774708347685" + 
":  " + 
"(b('crop') <= 8.081742763519287) ? " + 
"(b('ndvi') <= 2661.0) ? " + 
"0.0015534778756358771" + 
":  " + 
"0.02714929056423661" + 
":  " + 
"(b('L8b3') <= 518.5) ? " + 
"0.02571509730790617" + 
":  " + 
"-0.0017767510541963844" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2437721.5) ? " + 
"(b('crop') <= 53.104082107543945) ? " + 
"(b('dgvv') <= 1.4912981986999512) ? " + 
"-0.0006476629206130449" + 
":  " + 
"0.016808345579829298" + 
":  " + 
"(b('sand') <= 57.5) ? " + 
"-0.0027646681439994704" + 
":  " + 
"-0.014240272292720449" + 
":  " + 
"(b('clay') <= 10.5) ? " + 
"(b('ndvi') <= 2945.0) ? " + 
"0.03363145366819264" + 
":  " + 
"-0.013213275741675695" + 
":  " + 
"(b('L8b5') <= 2020.5) ? " + 
"0.03651007954969851" + 
":  " + 
"0.010080114541931924" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2355.5) ? " + 
"(b('L8b5') <= 3800.0) ? " + 
"(b('dsvv') <= 3.633577585220337) ? " + 
"-0.00942623149776367" + 
":  " + 
"-0.05733094086353798" + 
":  " + 
"(b('gvv') <= -12.212881088256836) ? " + 
"0.1345592361405754" + 
":  " + 
"0.17466453321744357" + 
":  " + 
"(b('L8b6') <= 2191.5) ? " + 
"(b('crop') <= 16.058724880218506) ? " + 
"0.03613350859536555" + 
":  " + 
"0.007375596884168315" + 
":  " + 
"(b('L8b2') <= 370.5) ? " + 
"-0.028310530687616776" + 
":  " + 
"0.0002604605103675254" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 3155.0) ? " + 
"(b('L8b6med') <= 3096.5) ? " + 
"(b('dgvv') <= -0.8056073188781738) ? " + 
"-0.007629342580660631" + 
":  " + 
"0.0014626310677407404" + 
":  " + 
"(b('sand') <= 39.5) ? " + 
"0.03125355561375503" + 
":  " + 
"0.007867276089453215" + 
":  " + 
"(b('L8b6med') <= 3416.5) ? " + 
"(b('ndvi_med') <= 4600.25) ? " + 
"-0.007839602557463817" + 
":  " + 
"-0.0420614408628463" + 
":  " + 
"(b('ndvi') <= 2689.5) ? " + 
"-0.0018279670101024954" + 
":  " + 
"0.021202622308263558" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2437721.5) ? " + 
"(b('ndvi') <= 4627.5) ? " + 
"(b('ndvi_med') <= 4757.25) ? " + 
"-0.000382833720297843" + 
":  " + 
"0.05885946651305215" + 
":  " + 
"(b('clay') <= 11.5) ? " + 
"-0.029108491852955696" + 
":  " + 
"-0.002594785618739637" + 
":  " + 
"(b('clay') <= 10.5) ? " + 
"(b('ndvi') <= 2945.0) ? " + 
"0.0301970395278615" + 
":  " + 
"-0.011271457010448356" + 
":  " + 
"(b('L8b11') <= 2835.5) ? " + 
"0.013973455454346107" + 
":  " + 
"-0.00850505699545714" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 2.8459320068359375) ? " + 
"(b('L8dt') <= 480816.0) ? " + 
"(b('gvv') <= -16.014039993286133) ? " + 
"-0.012026266169601818" + 
":  " + 
"-0.0023073256237480565" + 
":  " + 
"(b('moss') <= 25.491960525512695) ? " + 
"0.0014437463485427165" + 
":  " + 
"0.044628783297367434" + 
":  " + 
"(b('lat') <= 55.879150390625) ? " + 
"(b('lon') <= -110.59786224365234) ? " + 
"0.04171371464345688" + 
":  " + 
"0.010709982186569414" + 
":  " + 
"(b('ndvi') <= 3553.0) ? " + 
"0.03222826396634963" + 
":  " + 
"-0.04336915652369165" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 26.31478500366211) ? " + 
"(b('L8b6') <= 1921.0) ? " + 
"(b('L8b3') <= 891.0) ? " + 
"0.006655288875468235" + 
":  " + 
"0.07961813458932221" + 
":  " + 
"(b('L8b3') <= 456.0) ? " + 
"-0.15498400062718617" + 
":  " + 
"-0.0006877348286543545" + 
":  " + 
"(b('dsvv') <= 0.7392244338989258) ? " + 
"(b('L8dt') <= 1346330.0) ? " + 
"-0.005567977480109065" + 
":  " + 
"0.1383241039165858" + 
":  " + 
"(b('gvv') <= -9.91248893737793) ? " + 
"0.1306710909263243" + 
":  " + 
"0.04833767780352385" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2154.25) ? " + 
"(b('ndvi') <= 4380.5) ? " + 
"(b('L8b5') <= 3404.0) ? " + 
"0.0015009147539408582" + 
":  " + 
"-0.0953659787430148" + 
":  " + 
"(b('gvv') <= -12.875963687896729) ? " + 
"-0.13347077763227205" + 
":  " + 
"-0.0383208970766258" + 
":  " + 
"(b('L8b6') <= 2213.5) ? " + 
"(b('lon') <= -121.48147201538086) ? " + 
"0.08951254635034661" + 
":  " + 
"0.006491998178494923" + 
":  " + 
"(b('L8b2') <= 366.5) ? " + 
"-0.03188986721971983" + 
":  " + 
"6.286751962019482e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 3376.5) ? " + 
"(b('L8b6med') <= 3411.25) ? " + 
"(b('bulk') <= 139.5) ? " + 
"-0.0025445839495827445" + 
":  " + 
"0.003340627470315482" + 
":  " + 
"(b('sand') <= 40.5) ? " + 
"0.036254846214765934" + 
":  " + 
"0.007813447590064242" + 
":  " + 
"(b('dsvh') <= -3.0597314834594727) ? " + 
"(b('ndvi') <= 3017.0) ? " + 
"-0.005075235731989943" + 
":  " + 
"0.009968575329639821" + 
":  " + 
"(b('lat') <= -35.2979850769043) ? " + 
"0.1269650823976845" + 
":  " + 
"0.017799595267446712" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3390323.5) ? " + 
"(b('L8b6med') <= 2311.5) ? " + 
"(b('L8b5') <= 3800.0) ? " + 
"-0.01373948133283289" + 
":  " + 
"0.13979492138220143" + 
":  " + 
"(b('L8b4') <= 1184.5) ? " + 
"0.002762065681807787" + 
":  " + 
"-0.0022667394024617434" + 
":  " + 
"(b('L8b4med') <= 722.5) ? " + 
"(b('dgvv') <= 0.12847042083740234) ? " + 
"-0.00521017318262301" + 
":  " + 
"-0.05226348656278349" + 
":  " + 
"(b('lat') <= 37.94038963317871) ? " + 
"-0.03547230618714193" + 
":  " + 
"0.01628068761284617" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b1') <= 66.0) ? " + 
"(b('L8dt') <= 690100.0) ? " + 
"0.022100697284685403" + 
":  " + 
"0.09103549141969537" + 
":  " + 
"(b('L8b5') <= 1717.5) ? " + 
"-0.04052813804230806" + 
":  " + 
"-0.14015654855553955" + 
":  " + 
"(b('L8b3') <= 518.5) ? " + 
"(b('ndvi') <= 2273.5) ? " + 
"-0.006053253768606089" + 
":  " + 
"0.042336015360844734" + 
":  " + 
"(b('L8b3') <= 562.5) ? " + 
"-0.025671319449853715" + 
":  " + 
"0.00017508013689417632" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -16.012653350830078) ? " + 
"(b('L8b3') <= 576.5) ? " + 
"(b('L8b4') <= 534.0) ? " + 
"0.03775165792556977" + 
":  " + 
"-0.10510760975389057" + 
":  " + 
"(b('lon') <= -120.35504531860352) ? " + 
"0.02463143748334204" + 
":  " + 
"-0.008281301839445235" + 
":  " + 
"(b('lon') <= 147.53404998779297) ? " + 
"(b('lon') <= -105.18899917602539) ? " + 
"0.004365427127064621" + 
":  " + 
"-0.0009472844307082626" + 
":  " + 
"(b('ndvi') <= 2589.0) ? " + 
"-0.012434373777678599" + 
":  " + 
"0.09942385557305745" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 800741.0) ? " + 
"(b('crop') <= 44.79741096496582) ? " + 
"(b('L8b4') <= 530.5) ? " + 
"0.05505735615723713" + 
":  " + 
"0.000358865061313773" + 
":  " + 
"(b('L8b6') <= 1917.0) ? " + 
"0.00874731532197386" + 
":  " + 
"-0.00461088556201816" + 
":  " + 
"(b('moss') <= 16.250526428222656) ? " + 
"(b('dsvh') <= -10.98243236541748) ? " + 
"-0.024659103160313108" + 
":  " + 
"0.00248058516134056" + 
":  " + 
"(b('L8b4') <= 688.5) ? " + 
"0.10049693800930337" + 
":  " + 
"0.01602632150629195" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1280.0) ? " + 
"(b('ndvi_med') <= 4808.75) ? " + 
"(b('gvv') <= -10.880935668945312) ? " + 
"-0.05754381752456642" + 
":  " + 
"-0.028811103070545643" + 
":  " + 
"(b('dgvh') <= -8.199480056762695) ? " + 
"-0.07178092307824704" + 
":  " + 
"-0.0775641060264046" + 
":  " + 
"(b('L8b4') <= 530.5) ? " + 
"(b('L8b5') <= 2407.5) ? " + 
"-0.006134055275374044" + 
":  " + 
"0.04090214435454031" + 
":  " + 
"(b('L8b1') <= 126.0) ? " + 
"-0.08731367559590299" + 
":  " + 
"-9.493072688913424e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 2.8459320068359375) ? " + 
"(b('L8dt') <= 3385997.0) ? " + 
"(b('L8b5') <= 2154.5) ? " + 
"0.0040051358157947485" + 
":  " + 
"-0.0018269077983151028" + 
":  " + 
"(b('L8b4med') <= 689.0) ? " + 
"-0.022193170263314157" + 
":  " + 
"0.012607666894568022" + 
":  " + 
"(b('sand') <= 45.5) ? " + 
"(b('ndvi_med') <= 1695.0) ? " + 
"0.04934914952584738" + 
":  " + 
"0.015876358222864897" + 
":  " + 
"(b('L8b6med') <= 3445.75) ? " + 
"-0.018510978073207774" + 
":  " + 
"0.010691475457814226" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 44.514474868774414) ? " + 
"(b('L8b6') <= 2410.5) ? " + 
"(b('L8b6') <= 2404.0) ? " + 
"0.00951249302624336" + 
":  " + 
"0.06070721699569422" + 
":  " + 
"(b('L8b11') <= 2243.0) ? " + 
"-0.0047571313738111855" + 
":  " + 
"0.0019790322755891573" + 
":  " + 
"(b('L8b2') <= 363.5) ? " + 
"(b('L8b4') <= 534.0) ? " + 
"0.021866035466844187" + 
":  " + 
"-0.030395167103254756" + 
":  " + 
"(b('L8b3med') <= 564.0) ? " + 
"0.053015003412146454" + 
":  " + 
"-0.0022821262884855638" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1620.0) ? " + 
"(b('L8b11') <= 1421.0) ? " + 
"(b('lat') <= 43.47266960144043) ? " + 
"-0.02224140327678457" + 
":  " + 
"-0.09589466759580609" + 
":  " + 
"(b('ndvi_med') <= 2907.5) ? " + 
"-0.0031388712700677205" + 
":  " + 
"0.03381780755316176" + 
":  " + 
"(b('ndvi_med') <= 1585.5) ? " + 
"(b('lon') <= -112.14097595214844) ? " + 
"0.039566058758762714" + 
":  " + 
"0.007748633448376046" + 
":  " + 
"(b('L8b5') <= 2160.5) ? " + 
"0.006925452820282652" + 
":  " + 
"-0.0014846473497810825" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -6.351731300354004) ? " + 
"(b('L8b4med') <= 1529.5) ? " + 
"(b('dgvh') <= -10.108880996704102) ? " + 
"-0.016612257216457038" + 
":  " + 
"-0.0029852942241141564" + 
":  " + 
"(b('L8b4') <= 1547.0) ? " + 
"0.018185555053813186" + 
":  " + 
"-0.0013916150880273804" + 
":  " + 
"(b('moss') <= 26.31478500366211) ? " + 
"(b('dgvh') <= -6.347343921661377) ? " + 
"0.09449566305206222" + 
":  " + 
"0.0019792826154009214" + 
":  " + 
"(b('L8b1') <= 554.5) ? " + 
"0.07128772010478054" + 
":  " + 
"0.015922561676587753" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b1') <= 66.0) ? " + 
"(b('L8dt') <= 690100.0) ? " + 
"0.012446409164572505" + 
":  " + 
"0.07653381735254869" + 
":  " + 
"(b('L8b5') <= 1717.5) ? " + 
"-0.03727186099607615" + 
":  " + 
"-0.1134115388889099" + 
":  " + 
"(b('L8b3') <= 518.5) ? " + 
"(b('sand') <= 53.5) ? " + 
"-4.496087768499305e-05" + 
":  " + 
"0.037964151161601095" + 
":  " + 
"(b('L8b3') <= 562.5) ? " + 
"-0.02198593397294686" + 
":  " + 
"0.00018676440026265412" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -15.45765733718872) ? " + 
"(b('L8b2') <= 363.5) ? " + 
"(b('ndvi') <= 3190.5) ? " + 
"-0.005780222914550738" + 
":  " + 
"-0.08676343382948891" + 
":  " + 
"(b('dgvv') <= 1.4946579933166504) ? " + 
"-0.004705347269767844" + 
":  " + 
"0.1419838416650425" + 
":  " + 
"(b('lon') <= 147.53404998779297) ? " + 
"(b('crop') <= 49.023324966430664) ? " + 
"0.0025407062663031304" + 
":  " + 
"-0.0014683575922121482" + 
":  " + 
"(b('ndvi') <= 2568.0) ? " + 
"-0.06649121260577279" + 
":  " + 
"0.09391936472426021" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2353526.5) ? " + 
"(b('ndvi') <= 4627.5) ? " + 
"(b('ndvi_med') <= 4757.25) ? " + 
"-0.0003350854047252811" + 
":  " + 
"0.0536678131329775" + 
":  " + 
"(b('moss') <= 4.798989772796631) ? " + 
"-0.019896127415059323" + 
":  " + 
"0.0019933103882390493" + 
":  " + 
"(b('L8b6') <= 4860.5) ? " + 
"(b('lon') <= 9.122849941253662) ? " + 
"0.010696747561929862" + 
":  " + 
"-0.002951328572943646" + 
":  " + 
"(b('dsvv') <= -1.5324668884277344) ? " + 
"0.05222564435501313" + 
":  " + 
"-0.04573515200006343" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1280.0) ? " + 
"(b('L8b6') <= 1401.5) ? " + 
"(b('dsvv') <= 1.5588736534118652) ? " + 
"-0.046604793391784714" + 
":  " + 
"-0.02214248663716196" + 
":  " + 
"(b('gvv') <= -8.21831226348877) ? " + 
"-0.06909677780567305" + 
":  " + 
"-0.045156116363557444" + 
":  " + 
"(b('L8b6') <= 1921.0) ? " + 
"(b('L8b6') <= 1891.0) ? " + 
"0.004538456058699348" + 
":  " + 
"0.05541539640435064" + 
":  " + 
"(b('L8b7') <= 1020.5) ? " + 
"0.03607820370121739" + 
":  " + 
"-0.0005131783258058146" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1620.0) ? " + 
"(b('L8b11') <= 1421.0) ? " + 
"(b('L8b2') <= 366.0) ? " + 
"-0.01818584206692872" + 
":  " + 
"-0.08612465751086702" + 
":  " + 
"(b('L8b11') <= 2350.5) ? " + 
"-0.00848250315830703" + 
":  " + 
"-0.0005087675344469635" + 
":  " + 
"(b('ndvi_med') <= 1585.5) ? " + 
"(b('ndvi') <= 2658.5) ? " + 
"0.006166376178186194" + 
":  " + 
"0.03723648682671528" + 
":  " + 
"(b('L8b5') <= 2160.5) ? " + 
"0.006333897818672047" + 
":  " + 
"-0.0013006599808425812" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 26.31478500366211) ? " + 
"(b('L8b4') <= 853.5) ? " + 
"(b('lon') <= -115.05220413208008) ? " + 
"0.0440752042945864" + 
":  " + 
"0.0006073544513833176" + 
":  " + 
"(b('L8b4med') <= 1444.75) ? " + 
"-0.004330725605099988" + 
":  " + 
"0.0016887982534453763" + 
":  " + 
"(b('dsvv') <= 0.7392244338989258) ? " + 
"(b('L8dt') <= 1346330.0) ? " + 
"-0.005759937139760551" + 
":  " + 
"0.12134846659911608" + 
":  " + 
"(b('gvv') <= -9.91248893737793) ? " + 
"0.11220636565459524" + 
":  " + 
"0.03613407314577314" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -3.027046322822571) ? " + 
"(b('dsvv') <= 3.218355178833008) ? " + 
"(b('L8dt') <= 480816.0) ? " + 
"-0.0022195421464633455" + 
":  " + 
"0.0013818570106429741" + 
":  " + 
"(b('sand') <= 43.5) ? " + 
"0.028112740458708013" + 
":  " + 
"0.0008394804053131914" + 
":  " + 
"(b('L8dt') <= 1792100.5) ? " + 
"(b('lon') <= 9.11115026473999) ? " + 
"-0.04065475468444144" + 
":  " + 
"-0.06111236241087906" + 
":  " + 
"(b('moss') <= 1.6297770738601685) ? " + 
"-0.03788415784651916" + 
":  " + 
"0.006897551239056561" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2184.5) ? " + 
"(b('L8b5') <= 3800.0) ? " + 
"(b('ndvi') <= 3761.0) ? " + 
"0.0018314832447082867" + 
":  " + 
"-0.027765263490902966" + 
":  " + 
"(b('gvv') <= -12.395779609680176) ? " + 
"0.1316097549354077" + 
":  " + 
"0.15040525097669585" + 
":  " + 
"(b('ndvi') <= 2100.5) ? " + 
"(b('lat') <= 50.95975112915039) ? " + 
"-0.0020623369090899254" + 
":  " + 
"0.0634142586168527" + 
":  " + 
"(b('lon') <= -115.05220413208008) ? " + 
"0.0282851798392778" + 
":  " + 
"0.0007188323007635354" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1529.5) ? " + 
"(b('L8b7') <= 1095.0) ? " + 
"(b('bulk') <= 129.5) ? " + 
"0.04415896033491885" + 
":  " + 
"-0.017157465420698563" + 
":  " + 
"(b('L8dt') <= 2701531.0) ? " + 
"-0.09760039480825435" + 
":  " + 
"-0.14678841596938336" + 
":  " + 
"(b('L8b6') <= 1921.0) ? " + 
"(b('L8b3') <= 891.0) ? " + 
"0.008564530274579714" + 
":  " + 
"0.07500244166200422" + 
":  " + 
"(b('L8b2') <= 382.25) ? " + 
"-0.008532149361939377" + 
":  " + 
"0.00019914289216632164" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -2.432307243347168) ? " + 
"(b('L8b3') <= 763.0) ? " + 
"(b('sand') <= 74.0) ? " + 
"-0.013539803206597817" + 
":  " + 
"-0.053431898253069564" + 
":  " + 
"(b('L8b3') <= 772.5) ? " + 
"0.09324010042005704" + 
":  " + 
"-0.00522533527170994" + 
":  " + 
"(b('ndvi') <= 4632.5) ? " + 
"(b('ndvi_med') <= 4757.25) ? " + 
"0.0006707152806378232" + 
":  " + 
"0.04699492326696593" + 
":  " + 
"(b('L8b11') <= 1268.25) ? " + 
"-0.07700674965510523" + 
":  " + 
"-0.0053867373968194" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3390323.5) ? " + 
"(b('L8b6med') <= 2391.5) ? " + 
"(b('L8b5') <= 3820.5) ? " + 
"-0.0066534068386123356" + 
":  " + 
"0.07944801071756495" + 
":  " + 
"(b('L8b6') <= 2410.5) ? " + 
"0.006498348925837301" + 
":  " + 
"-0.0009229261497409664" + 
":  " + 
"(b('L8b4med') <= 699.5) ? " + 
"(b('ndvi') <= 3455.0) ? " + 
"0.011499308679338363" + 
":  " + 
"-0.05116186493070629" + 
":  " + 
"(b('L8b11') <= 2835.5) ? " + 
"0.013564909933225986" + 
":  " + 
"-0.010366310425672652" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1280.0) ? " + 
"(b('L8b4') <= 493.0) ? " + 
"(b('dgvh') <= -5.607247829437256) ? " + 
"-0.02977002080565314" + 
":  " + 
"-0.04894716546479656" + 
":  " + 
"(b('gvv') <= -8.21831226348877) ? " + 
"-0.06447363775198992" + 
":  " + 
"-0.04245807540517467" + 
":  " + 
"(b('moss') <= 26.31478500366211) ? " + 
"(b('L8b4') <= 853.5) ? " + 
"0.0028087705996402324" + 
":  " + 
"-0.0010452226431589423" + 
":  " + 
"(b('dsvv') <= 0.7392244338989258) ? " + 
"-0.0004437577103281634" + 
":  " + 
"0.057025161903622876" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b1') <= 66.0) ? " + 
"(b('L8dt') <= 281736.0) ? " + 
"-0.0250655767708622" + 
":  " + 
"0.05118637925186861" + 
":  " + 
"(b('L8b6') <= 1707.5) ? " + 
"-0.03152481584539187" + 
":  " + 
"-0.09089573718513182" + 
":  " + 
"(b('L8b3') <= 518.5) ? " + 
"(b('gvv') <= -12.263354778289795) ? " + 
"0.045242813824768024" + 
":  " + 
"0.00787322555472896" + 
":  " + 
"(b('L8b3') <= 562.5) ? " + 
"-0.020105402074943473" + 
":  " + 
"0.00018307363518756993" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 16.250526428222656) ? " + 
"(b('dgvh') <= -8.234763145446777) ? " + 
"(b('L8b6med') <= 3397.5) ? " + 
"-0.0073480593444938055" + 
":  " + 
"0.0008355922109854297" + 
":  " + 
"(b('L8b5') <= 2160.5) ? " + 
"0.007186812738392862" + 
":  " + 
"-0.0006054981543602321" + 
":  " + 
"(b('ndvi') <= 3136.0) ? " + 
"(b('dsvh') <= -8.699013233184814) ? " + 
"0.019766246861225713" + 
":  " + 
"-0.0007311379338787824" + 
":  " + 
"(b('L8b5') <= 3421.5) ? " + 
"0.042181965693268465" + 
":  " + 
"0.0026536966690699705" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 1346052.0) ? " + 
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b6') <= 3368.5) ? " + 
"-0.001247463393309172" + 
":  " + 
"-0.00986639006658158" + 
":  " + 
"(b('L8b6') <= 3470.5) ? " + 
"0.009919939364444947" + 
":  " + 
"-0.0014106188041889665" + 
":  " + 
"(b('lon') <= 146.3602294921875) ? " + 
"(b('lat') <= 38.48287391662598) ? " + 
"-0.013743572763693371" + 
":  " + 
"0.004181764520606618" + 
":  " + 
"(b('L8b7') <= 2974.5) ? " + 
"0.041824762289945396" + 
":  " + 
"0.22612552407052347" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('L8b5') <= 3061.0) ? " + 
"(b('L8b3med') <= 564.0) ? " + 
"-0.033553007652427615" + 
":  " + 
"0.0005628926930067241" + 
":  " + 
"(b('moss') <= 14.397151947021484) ? " + 
"-0.023297439107003087" + 
":  " + 
"-0.08681943438943775" + 
":  " + 
"(b('L8b4') <= 793.5) ? " + 
"(b('lon') <= -118.20269775390625) ? " + 
"0.08070783649807024" + 
":  " + 
"0.0055511513794496955" + 
":  " + 
"(b('L8b4') <= 800.5) ? " + 
"-0.0472601562812334" + 
":  " + 
"-0.000478708362324815" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1529.5) ? " + 
"(b('L8b7') <= 1095.0) ? " + 
"(b('bulk') <= 129.5) ? " + 
"0.03827335721456875" + 
":  " + 
"-0.015295027049416965" + 
":  " + 
"(b('L8dt') <= 2701531.0) ? " + 
"-0.08870006136489807" + 
":  " + 
"-0.13382925278196287" + 
":  " + 
"(b('L8b7') <= 1042.5) ? " + 
"(b('sand') <= 32.0) ? " + 
"0.05281633773246464" + 
":  " + 
"0.004894656159832791" + 
":  " + 
"(b('L8b2') <= 347.5) ? " + 
"-0.01157314999689929" + 
":  " + 
"0.00024132888466270265" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4med') <= 1444.75) ? " + 
"(b('L8b4') <= 1274.5) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"7.168471242515298e-05" + 
":  " + 
"0.038186615218481226" + 
":  " + 
"(b('L8b1') <= 808.5) ? " + 
"-0.008671783572993742" + 
":  " + 
"0.04419988932330991" + 
":  " + 
"(b('L8b4') <= 1416.0) ? " + 
"(b('L8b1') <= 449.5) ? " + 
"0.0015708273471128317" + 
":  " + 
"0.027174498107768553" + 
":  " + 
"(b('L8b7') <= 1741.5) ? " + 
"0.03716062610963497" + 
":  " + 
"-0.000878897302428823" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 5456.5) ? " + 
"(b('gvv') <= -15.45765733718872) ? " + 
"(b('L8b3') <= 606.5) ? " + 
"-0.047282679912089995" + 
":  " + 
"-0.0034097174430250026" + 
":  " + 
"(b('lon') <= 147.53404998779297) ? " + 
"0.0004409026200924233" + 
":  " + 
"0.05408485463949293" + 
":  " + 
"(b('dgvh') <= -8.447190284729004) ? " + 
"(b('gvv') <= -10.935465335845947) ? " + 
"-0.0534698003260914" + 
":  " + 
"-0.026680808555221328" + 
":  " + 
"(b('gvv') <= -10.967976093292236) ? " + 
"-0.07534128325200201" + 
":  " + 
"-0.06647604643338342" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -3.027046322822571) ? " + 
"(b('dsvv') <= 3.218355178833008) ? " + 
"(b('dgvv') <= 3.249246597290039) ? " + 
"-0.0002726907258011632" + 
":  " + 
"-0.16189606867964296" + 
":  " + 
"(b('bulk') <= 159.5) ? " + 
"0.007081898009945901" + 
":  " + 
"0.09895495279703374" + 
":  " + 
"(b('L8dt') <= 1792100.5) ? " + 
"(b('ndvi') <= 5903.0) ? " + 
"-0.037002840162962077" + 
":  " + 
"-0.05730039245070957" + 
":  " + 
"(b('crop') <= 92.0) ? " + 
"0.006538806961291715" + 
":  " + 
"-0.034338433617249475" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2391.5) ? " + 
"(b('L8b7') <= 1953.0) ? " + 
"(b('L8b4') <= 761.5) ? " + 
"0.00021510427441923653" + 
":  " + 
"-0.014381863535512983" + 
":  " + 
"(b('sand') <= 38.5) ? " + 
"0.04792301466710586" + 
":  " + 
"-0.010457360866685934" + 
":  " + 
"(b('L8b6') <= 2410.5) ? " + 
"(b('lon') <= -116.34695434570312) ? " + 
"0.029062894772480505" + 
":  " + 
"0.0029006895888167147" + 
":  " + 
"(b('L8b7') <= 1328.5) ? " + 
"-0.036836712952901786" + 
":  " + 
"0.00011525792530940451" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2874353.5) ? " + 
"(b('crop') <= 50.22887420654297) ? " + 
"(b('dgvv') <= 0.9199080467224121) ? " + 
"-0.0006487570779173112" + 
":  " + 
"0.008022585104049993" + 
":  " + 
"(b('dsvv') <= 1.0196118354797363) ? " + 
"-0.0006528115093575493" + 
":  " + 
"-0.00713271731480433" + 
":  " + 
"(b('lat') <= 41.32645606994629) ? " + 
"(b('lon') <= -109.55375671386719) ? " + 
"-0.03179821179237335" + 
":  " + 
"0.03244758757837065" + 
":  " + 
"(b('L8b6') <= 3304.0) ? " + 
"0.0065993584261795435" + 
":  " + 
"-0.011083860741388098" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1620.0) ? " + 
"(b('L8b11') <= 1421.0) ? " + 
"(b('lon') <= -42.01006603240967) ? " + 
"-0.012681573760117908" + 
":  " + 
"-0.07173857758050747" + 
":  " + 
"(b('L8b11') <= 2738.5) ? " + 
"-0.0047294312192488535" + 
":  " + 
"0.0015148879125828213" + 
":  " + 
"(b('ndvi_med') <= 1362.5) ? " + 
"(b('bulk') <= 167.0) ? " + 
"0.02448381909436994" + 
":  " + 
"0.16430122858562776" + 
":  " + 
"(b('lon') <= -111.2929458618164) ? " + 
"0.006965306542163913" + 
":  " + 
"-0.0003856215939547128" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 878.5) ? " + 
"(b('dgvv') <= 2.2133798599243164) ? " + 
"(b('ndvi_med') <= 1400.5) ? " + 
"0.15964280689478974" + 
":  " + 
"-0.012154181297639295" + 
":  " + 
"(b('lon') <= -38.50918889045715) ? " + 
"-0.16993110338287426" + 
":  " + 
"-0.04922161111367753" + 
":  " + 
"(b('L8b7') <= 1020.0) ? " + 
"(b('dgvh') <= -7.602212905883789) ? " + 
"-0.028647089212131133" + 
":  " + 
"0.02541596220368455" + 
":  " + 
"(b('L8b3') <= 506.5) ? " + 
"-0.041608250461703945" + 
":  " + 
"-5.084642511104769e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3385.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"(b('L8b3med') <= 964.5) ? " + 
"-0.0018374697204215072" + 
":  " + 
"0.002527582846794559" + 
":  " + 
"(b('L8b2') <= 446.5) ? " + 
"-0.04570010226818279" + 
":  " + 
"0.06587561939234293" + 
":  " + 
"(b('L8b3') <= 761.5) ? " + 
"(b('L8dt') <= 1546172.0) ? " + 
"-0.03953236068780205" + 
":  " + 
"0.002611106695860066" + 
":  " + 
"(b('L8b6') <= 1929.5) ? " + 
"0.06635481130464906" + 
":  " + 
"-0.002087150395458751" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2100.5) ? " + 
"(b('L8b11') <= 1394.25) ? " + 
"(b('L8b7') <= 1542.5) ? " + 
"0.01893395183421429" + 
":  " + 
"0.09253213925586956" + 
":  " + 
"(b('L8b4') <= 1154.5) ? " + 
"0.004496468698536321" + 
":  " + 
"-0.003138396620124037" + 
":  " + 
"(b('lon') <= -116.11370086669922) ? " + 
"(b('L8b4') <= 1037.5) ? " + 
"0.03320872840434582" + 
":  " + 
"0.001964092993119288" + 
":  " + 
"(b('L8b3') <= 1527.5) ? " + 
"-0.00032328552085426866" + 
":  " + 
"0.021219492234186017" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -11.445321083068848) ? " + 
"(b('clay') <= 26.0) ? " + 
"(b('L8b6') <= 3511.0) ? " + 
"-0.0011906402749969197" + 
":  " + 
"-0.03720356126427192" + 
":  " + 
"(b('dgvh') <= -11.906160354614258) ? " + 
"-0.11305530809380836" + 
":  " + 
"-0.02563133899891995" + 
":  " + 
"(b('L8b6med') <= 2184.5) ? " + 
"(b('ndvi') <= 4186.5) ? " + 
"0.0020267308664036286" + 
":  " + 
"-0.026783192097338256" + 
":  " + 
"(b('ndvi') <= 3898.5) ? " + 
"-0.0002944773965865953" + 
":  " + 
"0.004570573485128044" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 16.250526428222656) ? " + 
"(b('dgvh') <= -9.14317512512207) ? " + 
"(b('L8b11') <= 2638.0) ? " + 
"-0.0091524239296533" + 
":  " + 
"0.003482668681957966" + 
":  " + 
"(b('moss') <= 7.472553253173828) ? " + 
"0.001567672233994456" + 
":  " + 
"-0.002362816131878754" + 
":  " + 
"(b('ndvi') <= 3136.0) ? " + 
"(b('dsvh') <= -8.719909191131592) ? " + 
"0.01831550277641352" + 
":  " + 
"-0.0005241052784876382" + 
":  " + 
"(b('L8b5') <= 3421.5) ? " + 
"0.03609050210157531" + 
":  " + 
"0.002509545506676174" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1297.5) ? " + 
"(b('sand') <= 50.5) ? " + 
"(b('dgvv') <= 1.5594372749328613) ? " + 
"-0.030885918637477222" + 
":  " + 
"-0.008410763599682413" + 
":  " + 
"(b('dgvh') <= -6.4578986167907715) ? " + 
"-0.05787297131657604" + 
":  " + 
"-0.038795959335404626" + 
":  " + 
"(b('L8b4') <= 530.5) ? " + 
"(b('L8b5') <= 2342.0) ? " + 
"-0.009235487684847629" + 
":  " + 
"0.029611231342987397" + 
":  " + 
"(b('L8b1') <= 126.0) ? " + 
"-0.06720291637289989" + 
":  " + 
"-4.2760749396444175e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4169.5) ? " + 
"(b('ndvi') <= 5278.5) ? " + 
"0.00032037915434346057" + 
":  " + 
"-0.008954096143131838" + 
":  " + 
"(b('L8b3') <= 893.0) ? " + 
"0.07624193938572373" + 
":  " + 
"0.014421178072669755" + 
":  " + 
"(b('gvv') <= -13.349421501159668) ? " + 
"(b('dgvh') <= -6.303203582763672) ? " + 
"-0.013468471101666477" + 
":  " + 
"0.04233890873584107" + 
":  " + 
"(b('L8b7') <= 1229.0) ? " + 
"0.08644484094280895" + 
":  " + 
"-0.03929287638158707" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 382067.5) ? " + 
"(b('L8b11') <= 2180.0) ? " + 
"(b('ndvi') <= 1554.5) ? " + 
"-0.012882002811459677" + 
":  " + 
"-0.002835355331011861" + 
":  " + 
"(b('L8b5') <= 2527.5) ? " + 
"0.0068827807557440175" + 
":  " + 
"-0.0020700735190761197" + 
":  " + 
"(b('dgvh') <= -5.421253204345703) ? " + 
"(b('dgvh') <= -5.5057573318481445) ? " + 
"0.0001545250625694521" + 
":  " + 
"-0.018134322057255896" + 
":  " + 
"(b('crop') <= 76.83937072753906) ? " + 
"0.009264580603808229" + 
":  " + 
"-0.005008004153229165" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('L8b5') <= 3061.0) ? " + 
"(b('L8b3med') <= 564.0) ? " + 
"-0.026444936418169928" + 
":  " + 
"0.000225754236376794" + 
":  " + 
"(b('moss') <= 14.397151947021484) ? " + 
"-0.019401932237351115" + 
":  " + 
"-0.0726001470121795" + 
":  " + 
"(b('L8b3med') <= 587.0) ? " + 
"(b('ndvi') <= 2579.5) ? " + 
"0.11435733540694533" + 
":  " + 
"0.03978983674458536" + 
":  " + 
"(b('L8b4') <= 793.5) ? " + 
"0.006391373575139498" + 
":  " + 
"-0.0006033674206100336" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2494.25) ? " + 
"(b('dsvh') <= -0.03885698318481445) ? " + 
"(b('dsvh') <= -9.155388832092285) ? " + 
"-0.009271810266749716" + 
":  " + 
"-0.00026989334817618867" + 
":  " + 
"(b('L8b5') <= 3036.5) ? " + 
"0.10396181815030625" + 
":  " + 
"0.0012907611808387759" + 
":  " + 
"(b('L8b4') <= 1446.5) ? " + 
"(b('L8b11') <= 2531.0) ? " + 
"0.08722545478896158" + 
":  " + 
"0.005950415884935128" + 
":  " + 
"(b('L8b3') <= 1112.5) ? " + 
"-0.016332741919633336" + 
":  " + 
"0.0006875069169569369" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -15.280674457550049) ? " + 
"(b('dgvv') <= 1.4946579933166504) ? " + 
"(b('L8b3') <= 562.5) ? " + 
"-0.04190832749638784" + 
":  " + 
"-0.003547276427837121" + 
":  " + 
"(b('L8b6') <= 3024.0) ? " + 
"0.16153934512223378" + 
":  " + 
"0.04428447700036345" + 
":  " + 
"(b('lon') <= 147.53404998779297) ? " + 
"(b('lat') <= -35.01868438720703) ? " + 
"-0.013595030700833455" + 
":  " + 
"0.0006459808626812902" + 
":  " + 
"(b('ndvi') <= 2568.0) ? " + 
"-0.06885229790901883" + 
":  " + 
"0.08141227346928853" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3385.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"(b('L8b3med') <= 964.5) ? " + 
"-0.0016737737065528788" + 
":  " + 
"0.0023105562890914826" + 
":  " + 
"(b('L8b2') <= 446.5) ? " + 
"-0.04016423713427536" + 
":  " + 
"0.05889480387981553" + 
":  " + 
"(b('clay') <= 16.5) ? " + 
"(b('L8b6med') <= 2985.75) ? " + 
"-0.025069609861084686" + 
":  " + 
"0.006896380198005184" + 
":  " + 
"(b('ndvi_med') <= 2546.5) ? " + 
"-0.003961965759830909" + 
":  " + 
"0.013787622244748788" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2100.5) ? " + 
"(b('lat') <= 50.95975112915039) ? " + 
"(b('dgvh') <= -12.092339992523193) ? " + 
"-0.06377315978870685" + 
":  " + 
"-0.0015818531975389045" + 
":  " + 
"(b('L8b5') <= 3005.0) ? " + 
"0.022282926727836227" + 
":  " + 
"0.09513684352851097" + 
":  " + 
"(b('lon') <= -116.11370086669922) ? " + 
"(b('L8b4med') <= 1407.75) ? " + 
"0.008866733125652802" + 
":  " + 
"0.039323321448719646" + 
":  " + 
"(b('L8b4') <= 1082.5) ? " + 
"-0.0021845333926373816" + 
":  " + 
"0.0050239732392734805" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 38.5) ? " + 
"(b('gvv') <= -15.280674457550049) ? " + 
"(b('dgvv') <= 1.4946579933166504) ? " + 
"-0.0040789956472546225" + 
":  " + 
"0.09163989553462559" + 
":  " + 
"(b('lon') <= 147.53404998779297) ? " + 
"0.0004773312124464906" + 
":  " + 
"0.04368197555064952" + 
":  " + 
"(b('dsvv') <= 0.3476085662841797) ? " + 
"(b('L8b5') <= 2255.5) ? " + 
"0.015372880883215236" + 
":  " + 
"-0.02270759407495591" + 
":  " + 
"(b('L8b5') <= 2166.0) ? " + 
"-0.02655423301204901" + 
":  " + 
"-0.0632259317900268" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2998.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"(b('L8b4med') <= 1444.75) ? " + 
"-0.0016917017469814182" + 
":  " + 
"0.005023754949210714" + 
":  " + 
"(b('ndvi_med') <= 4980.0) ? " + 
"0.11949495547518252" + 
":  " + 
"0.005717458559341359" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"(b('L8b3') <= 762.0) ? " + 
"-0.009287093039957423" + 
":  " + 
"0.009427804782422007" + 
":  " + 
"(b('L8b2') <= 339.5) ? " + 
"-0.0360356176547198" + 
":  " + 
"-0.00437084361388285" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1314.5) ? " + 
"(b('dsvv') <= -0.0651555061340332) ? " + 
"(b('L8b4med') <= 757.0) ? " + 
"-0.002690998930374545" + 
":  " + 
"-0.02003037503108994" + 
":  " + 
"(b('L8dt') <= 317330.0) ? " + 
"-0.01798144192504646" + 
":  " + 
"-0.042092566358830893" + 
":  " + 
"(b('L8b5') <= 1935.5) ? " + 
"(b('L8b3med') <= 1375.75) ? " + 
"0.008326020395033416" + 
":  " + 
"-0.05846745073851556" + 
":  " + 
"(b('L8b4') <= 529.0) ? " + 
"0.017825784381703368" + 
":  " + 
"-0.0005358896504374373" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -6.351731300354004) ? " + 
"(b('L8b11') <= 2440.5) ? " + 
"(b('L8b4') <= 2109.5) ? " + 
"-0.0023073472144447037" + 
":  " + 
"-0.030436926382148757" + 
":  " + 
"(b('L8b6') <= 3471.0) ? " + 
"0.007854536382894439" + 
":  " + 
"-0.0020626388113693544" + 
":  " + 
"(b('dgvh') <= -6.346902847290039) ? " + 
"(b('L8b1') <= 368.0) ? " + 
"0.20121098312729535" + 
":  " + 
"0.0357286756967217" + 
":  " + 
"(b('L8b6med') <= 4086.0) ? " + 
"0.0010896233294403984" + 
":  " + 
"0.021916058890999082" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 5456.5) ? " + 
"(b('L8dt') <= 1360284.0) ? " + 
"(b('L8b6med') <= 3416.5) ? " + 
"-0.001797616055279913" + 
":  " + 
"0.0016196310175227951" + 
":  " + 
"(b('lon') <= 146.3602294921875) ? " + 
"0.002250303273507024" + 
":  " + 
"0.0705135909330713" + 
":  " + 
"(b('dsvh') <= -8.503643035888672) ? " + 
"(b('dgvv') <= -0.16309595108032227) ? " + 
"-0.04263304971134485" + 
":  " + 
"-0.018411727188479506" + 
":  " + 
"(b('dsvh') <= -7.976777076721191) ? " + 
"-0.057223649997269546" + 
":  " + 
"-0.06590647881888442" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2312.5) ? " + 
"(b('ndvi') <= 2278.5) ? " + 
"(b('dgvv') <= 4.9693803787231445) ? " + 
"-0.0008866754098653636" + 
":  " + 
"0.0486790172128357" + 
":  " + 
"(b('moss') <= 6.747191667556763) ? " + 
"0.00035940854764457804" + 
":  " + 
"-0.03722277903915013" + 
":  " + 
"(b('lon') <= -116.11370086669922) ? " + 
"(b('dgvh') <= -4.439622402191162) ? " + 
"0.02502372329374367" + 
":  " + 
"-0.021170292714410052" + 
":  " + 
"(b('L8b3') <= 1450.0) ? " + 
"-5.9975456255834194e-05" + 
":  " + 
"0.015890415566826983" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvh') <= 4.280712604522705) ? " + 
"(b('L8b4') <= 853.5) ? " + 
"(b('L8b3') <= 841.5) ? " + 
"0.0007238727445534788" + 
":  " + 
"0.023706216099065196" + 
":  " + 
"(b('L8b3') <= 888.5) ? " + 
"-0.005383811193681424" + 
":  " + 
"0.00032910354199629314" + 
":  " + 
"-0.1315582747972041" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3385.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"(b('L8b5') <= 3318.0) ? " + 
"5.758330516624201e-05" + 
":  " + 
"0.011345119741665893" + 
":  " + 
"(b('L8b2') <= 446.5) ? " + 
"-0.03577562143411193" + 
":  " + 
"0.04829621439435845" + 
":  " + 
"(b('bulk') <= 165.5) ? " + 
"(b('clay') <= 16.5) ? " + 
"-0.016208170532039087" + 
":  " + 
"-0.00018497785743802338" + 
":  " + 
"(b('dgvv') <= -0.5773601531982422) ? " + 
"0.1489088804470874" + 
":  " + 
"0.22156063682404958" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1529.5) ? " + 
"(b('L8b7') <= 1095.0) ? " + 
"(b('bulk') <= 129.5) ? " + 
"0.035856435080439154" + 
":  " + 
"-0.012235834014384517" + 
":  " + 
"(b('L8dt') <= 2701531.0) ? " + 
"-0.07931887662047254" + 
":  " + 
"-0.11859793723638501" + 
":  " + 
"(b('L8b6') <= 1584.5) ? " + 
"(b('lat') <= 3.0288543701171875) ? " + 
"-0.08433389845620837" + 
":  " + 
"0.04623634738231588" + 
":  " + 
"(b('L8b7') <= 851.0) ? " + 
"-0.17125931114680612" + 
":  " + 
"5.7437589473475104e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 822.5) ? " + 
"(b('L8b5') <= 3385.5) ? " + 
"(b('L8b3med') <= 964.5) ? " + 
"-0.0009032524448659606" + 
":  " + 
"0.005802078658895364" + 
":  " + 
"(b('crop') <= 69.92036819458008) ? " + 
"0.0033050261260481775" + 
":  " + 
"-0.012714737386377049" + 
":  " + 
"(b('L8b11') <= 1466.25) ? " + 
"(b('L8b6med') <= 2191.0) ? " + 
"0.10349535893799498" + 
":  " + 
"0.08334477308122118" + 
":  " + 
"(b('L8b3') <= 1420.5) ? " + 
"-0.007631993834734661" + 
":  " + 
"0.0007042124919772377" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1620.0) ? " + 
"(b('L8b11') <= 1421.0) ? " + 
"(b('L8dt') <= 593843.0) ? " + 
"-0.04227302951037547" + 
":  " + 
"-0.07438876626826138" + 
":  " + 
"(b('ndvi_med') <= 2907.5) ? " + 
"-0.0020214115234402177" + 
":  " + 
"0.02745424393070483" + 
":  " + 
"(b('ndvi_med') <= 1273.75) ? " + 
"(b('lat') <= 36.67852020263672) ? " + 
"0.027655660426910728" + 
":  " + 
"0.09566159836102303" + 
":  " + 
"(b('ndvi_med') <= 1699.5) ? " + 
"0.005945688981181752" + 
":  " + 
"-0.00019993777639180894" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1184.5) ? " + 
"(b('L8b2') <= 636.5) ? " + 
"(b('lon') <= 147.47109985351562) ? " + 
"0.00039640396749475904" + 
":  " + 
"-0.03849786710433987" + 
":  " + 
"(b('moss') <= 26.31478500366211) ? " + 
"0.00931941524718056" + 
":  " + 
"0.08774290082966821" + 
":  " + 
"(b('L8b5') <= 1795.0) ? " + 
"(b('L8b3med') <= 1455.25) ? " + 
"-0.01869384860414988" + 
":  " + 
"-0.122453302351804" + 
":  " + 
"(b('L8b7') <= 1680.5) ? " + 
"0.02210099026833442" + 
":  " + 
"-0.0012790013558094508" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3385997.0) ? " + 
"(b('crop') <= 88.85982513427734) ? " + 
"(b('L8b5') <= 1934.0) ? " + 
"0.007075691045521308" + 
":  " + 
"-0.0003247711426175954" + 
":  " + 
"(b('ndvi') <= 6542.0) ? " + 
"-0.005761664994926042" + 
":  " + 
"0.047764794935294626" + 
":  " + 
"(b('L8b4med') <= 699.5) ? " + 
"(b('ndvi') <= 3455.0) ? " + 
"0.01267294161127116" + 
":  " + 
"-0.049595541488763925" + 
":  " + 
"(b('L8b1') <= 851.0) ? " + 
"0.009410024450209078" + 
":  " + 
"-0.031132860058623073" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2184.5) ? " + 
"(b('L8b5') <= 1699.5) ? " + 
"(b('L8b1') <= 528.0) ? " + 
"0.04958684862399314" + 
":  " + 
"0.00807002666523914" + 
":  " + 
"(b('L8b3') <= 1440.5) ? " + 
"-0.013750979360616058" + 
":  " + 
"0.09386988345690822" + 
":  " + 
"(b('ndvi') <= 3898.5) ? " + 
"(b('dgvv') <= 3.8172192573547363) ? " + 
"-0.0007088923072835436" + 
":  " + 
"0.012700643574643159" + 
":  " + 
"(b('clay') <= 21.5) ? " + 
"-0.002591995359053173" + 
":  " + 
"0.013903869899931696" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1314.5) ? " + 
"(b('dsvv') <= -0.0651555061340332) ? " + 
"(b('gvv') <= -11.817963123321533) ? " + 
"-0.016497964070155823" + 
":  " + 
"-0.003021005557075894" + 
":  " + 
"(b('L8b2') <= 157.0) ? " + 
"-0.0005058774246166353" + 
":  " + 
"-0.03663189255859488" + 
":  " + 
"(b('L8b4') <= 612.5) ? " + 
"(b('L8b4') <= 611.5) ? " + 
"0.004505091106914942" + 
":  " + 
"0.06315990667321945" + 
":  " + 
"(b('L8b2') <= 377.5) ? " + 
"-0.00996402739416799" + 
":  " + 
"0.00032122732545731376" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1370.0) ? " + 
"(b('ndvi') <= 1506.0) ? " + 
"(b('dsvv') <= -1.099656581878662) ? " + 
"0.015921877533984316" + 
":  " + 
"-0.001734331002093683" + 
":  " + 
"(b('L8b1') <= 501.0) ? " + 
"-0.008400912660060352" + 
":  " + 
"0.02794413057823023" + 
":  " + 
"(b('ndvi') <= 2076.5) ? " + 
"(b('L8b11') <= 1394.25) ? " + 
"0.03987912593469269" + 
":  " + 
"-0.002614031291119387" + 
":  " + 
"(b('ndvi_med') <= 2145.0) ? " + 
"0.007321431704607898" + 
":  " + 
"-0.0005111232006710961" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -3.027046322822571) ? " + 
"(b('dsvv') <= 5.050154209136963) ? " + 
"(b('dsvv') <= 4.769896984100342) ? " + 
"2.546410139944225e-05" + 
":  " + 
"-0.0320658291648215" + 
":  " + 
"(b('lat') <= -35.01868438720703) ? " + 
"-0.06586284737146249" + 
":  " + 
"0.027559905935472345" + 
":  " + 
"(b('L8dt') <= 1792100.5) ? " + 
"(b('L8b6') <= 3188.0) ? " + 
"-0.030781670712842366" + 
":  " + 
"-0.06485617478673482" + 
":  " + 
"(b('L8b6') <= 2800.5) ? " + 
"-0.02889364989863311" + 
":  " + 
"0.007260112923262448" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2998.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"(b('L8b4med') <= 1444.75) ? " + 
"-0.001461620395046204" + 
":  " + 
"0.004455015929332733" + 
":  " + 
"(b('L8b6med') <= 2684.5) ? " + 
"0.00215098436557464" + 
":  " + 
"0.10279391921137825" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"(b('L8b7') <= 1029.0) ? " + 
"0.05217087143897026" + 
":  " + 
"0.003674953651736164" + 
":  " + 
"(b('L8b7') <= 2953.5) ? " + 
"-0.008520773499801963" + 
":  " + 
"0.0014280550238153502" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 236044.5) ? " + 
"(b('dsvh') <= -4.714461803436279) ? " + 
"(b('ndvi') <= 2340.0) ? " + 
"-0.0031279788857418575" + 
":  " + 
"0.003574424710018765" + 
":  " + 
"(b('L8b1') <= 731.5) ? " + 
"-0.014435796952085916" + 
":  " + 
"0.036800244163775676" + 
":  " + 
"(b('L8dt') <= 236051.5) ? " + 
"(b('L8dt') <= 236050.5) ? " + 
"0.012020982508540251" + 
":  " + 
"0.09388109161201288" + 
":  " + 
"(b('dgvh') <= -5.353282451629639) ? " + 
"-0.00045461995230484253" + 
":  " + 
"0.0038605639395896682" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1529.5) ? " + 
"(b('L8b7') <= 1095.0) ? " + 
"(b('L8b4med') <= 689.0) ? " + 
"-0.03961218058618073" + 
":  " + 
"-0.0011831494008568656" + 
":  " + 
"(b('L8dt') <= 2701531.0) ? " + 
"-0.0728510512028946" + 
":  " + 
"-0.10785779417837463" + 
":  " + 
"(b('L8b7') <= 1042.5) ? " + 
"(b('lon') <= -38.50918889045715) ? " + 
"-0.05670882015897828" + 
":  " + 
"0.016811343374934732" + 
":  " + 
"(b('L8b3') <= 506.5) ? " + 
"-0.044476058596298856" + 
":  " + 
"-2.0183354070943656e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -2.432307243347168) ? " + 
"(b('L8b3') <= 763.0) ? " + 
"(b('L8b1') <= 397.5) ? " + 
"-0.025963370380715434" + 
":  " + 
"0.003587768775584345" + 
":  " + 
"(b('L8b3') <= 772.5) ? " + 
"0.06463592816421933" + 
":  " + 
"-0.0032860436000433113" + 
":  " + 
"(b('ndvi') <= 4627.5) ? " + 
"(b('ndvi') <= 4602.5) ? " + 
"0.0004816872231477088" + 
":  " + 
"0.05388509684231046" + 
":  " + 
"(b('moss') <= 4.798989772796631) ? " + 
"-0.012239619729759904" + 
":  " + 
"0.004346127704039643" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 5456.5) ? " + 
"(b('dsvv') <= -6.711760997772217) ? " + 
"(b('L8b2') <= 834.5) ? " + 
"-0.017275351790073504" + 
":  " + 
"-0.10300274879712817" + 
":  " + 
"(b('L8b1') <= 68.5) ? " + 
"0.040799705249410095" + 
":  " + 
"2.1202729735375555e-05" + 
":  " + 
"(b('dgvh') <= -8.447190284729004) ? " + 
"(b('gvv') <= -10.935465335845947) ? " + 
"-0.03726561974754197" + 
":  " + 
"-0.015600097423635023" + 
":  " + 
"(b('ndvi_med') <= 1430.0) ? " + 
"-0.052152893708425435" + 
":  " + 
"-0.061482106022799285" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2874353.5) ? " + 
"(b('crop') <= 88.85982513427734) ? " + 
"(b('L8b5') <= 1935.5) ? " + 
"0.006568612335715141" + 
":  " + 
"-0.0003329978221185768" + 
":  " + 
"(b('L8b3') <= 1572.5) ? " + 
"-0.0018783885788238705" + 
":  " + 
"-0.01804162447920725" + 
":  " + 
"(b('lat') <= 41.32645606994629) ? " + 
"(b('lon') <= -109.55375671386719) ? " + 
"-0.028820052025099307" + 
":  " + 
"0.02790174399994016" + 
":  " + 
"(b('L8b11') <= 2816.0) ? " + 
"0.0036879902130869478" + 
":  " + 
"-0.018711618137098367" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1314.5) ? " + 
"(b('dsvv') <= -0.0651555061340332) ? " + 
"(b('gvv') <= -11.817963123321533) ? " + 
"-0.015194541867538136" + 
":  " + 
"-0.002778676375424211" + 
":  " + 
"(b('L8b4med') <= 880.0) ? " + 
"-0.009987555928894335" + 
":  " + 
"-0.0343224500578459" + 
":  " + 
"(b('L8b4') <= 793.5) ? " + 
"(b('L8b3') <= 761.5) ? " + 
"-0.0007664042012924349" + 
":  " + 
"0.01536774072313338" + 
":  " + 
"(b('L8b4') <= 800.5) ? " + 
"-0.03660368081216068" + 
":  " + 
"-0.00038796751692028465" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 38.5) ? " + 
"(b('L8b2') <= 314.5) ? " + 
"(b('L8b6') <= 1707.5) ? " + 
"-0.006706575407215683" + 
":  " + 
"0.01751706901101058" + 
":  " + 
"(b('L8b3') <= 562.5) ? " + 
"-0.021196053362628683" + 
":  " + 
"0.00015486873162689382" + 
":  " + 
"(b('dsvv') <= 0.3476085662841797) ? " + 
"(b('L8b5') <= 2745.0) ? " + 
"0.006666387425713789" + 
":  " + 
"-0.05423419612198986" + 
":  " + 
"(b('L8dt') <= 691198.0) ? " + 
"-0.03265917451433734" + 
":  " + 
"-0.07914062018722162" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 50288.5) ? " + 
"(b('dsvh') <= -2.7721152305603027) ? " + 
"(b('L8b11') <= 1261.75) ? " + 
"0.1086811269345189" + 
":  " + 
"-0.0035476437554864478" + 
":  " + 
"(b('L8b1') <= 263.0) ? " + 
"-0.11852476634787505" + 
":  " + 
"-0.03275653100922438" + 
":  " + 
"(b('L8dt') <= 70769.5) ? " + 
"(b('dgvv') <= 2.8632001876831055) ? " + 
"0.00504691664388023" + 
":  " + 
"0.04515830038259466" + 
":  " + 
"(b('L8dt') <= 125027.5) ? " + 
"-0.006872325622187347" + 
":  " + 
"0.0003621685400797848" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b6') <= 3147.5) ? " + 
"(b('L8b4med') <= 1502.25) ? " + 
"-0.00033558049100630954" + 
":  " + 
"0.0070737377403008814" + 
":  " + 
"(b('ndvi_med') <= 4600.25) ? " + 
"-0.003934108523247196" + 
":  " + 
"-0.029185193267720743" + 
":  " + 
"(b('ndvi') <= 2866.5) ? " + 
"(b('L8b5') <= 2473.5) ? " + 
"0.007656699030511423" + 
":  " + 
"-0.0016513417825780698" + 
":  " + 
"(b('L8b11') <= 2651.5) ? " + 
"0.0264636392368501" + 
":  " + 
"-6.16729859232598e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4348.5) ? " + 
"(b('ndvi') <= 5278.5) ? " + 
"0.0002909645554344168" + 
":  " + 
"-0.006105216600816512" + 
":  " + 
"(b('dgvh') <= -8.225106239318848) ? " + 
"0.05156080040937848" + 
":  " + 
"0.09455344742053999" + 
":  " + 
"(b('dsvv') <= 1.1198410987854004) ? " + 
"(b('dsvh') <= -6.303547382354736) ? " + 
"-0.011553369302610151" + 
":  " + 
"0.02412741962823648" + 
":  " + 
"(b('L8b6') <= 2263.5) ? " + 
"0.012174837638003552" + 
":  " + 
"-0.05897338807008998" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -16.012653350830078) ? " + 
"(b('moss') <= 4.057692289352417) ? " + 
"(b('L8b3') <= 1146.5) ? " + 
"0.00798635020188364" + 
":  " + 
"-0.007851526429381507" + 
":  " + 
"(b('L8b7') <= 1381.5) ? " + 
"-0.03836958474053429" + 
":  " + 
"-0.008977917718006413" + 
":  " + 
"(b('lon') <= 147.53404998779297) ? " + 
"(b('lat') <= -35.01868438720703) ? " + 
"-0.010384146870201344" + 
":  " + 
"0.0004432100541013379" + 
":  " + 
"(b('ndvi') <= 2589.0) ? " + 
"-0.017317114099918617" + 
":  " + 
"0.0626425603434118" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 16.250526428222656) ? " + 
"(b('dgvh') <= -10.005043983459473) ? " + 
"(b('crop') <= 76.58172988891602) ? " + 
"-0.01332847248624891" + 
":  " + 
"0.0035736630393706885" + 
":  " + 
"(b('dsvh') <= -9.931183338165283) ? " + 
"0.025018143325314986" + 
":  " + 
"-0.00017262782459985708" + 
":  " + 
"(b('ndvi') <= 3136.0) ? " + 
"(b('ndvi_med') <= 2852.25) ? " + 
"0.0021819862634141255" + 
":  " + 
"-0.035763419696232" + 
":  " + 
"(b('L8b5') <= 3421.5) ? " + 
"0.030365199670140928" + 
":  " + 
"-0.0004127893962869521" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2184.5) ? " + 
"(b('L8b5') <= 1699.5) ? " + 
"(b('L8dt') <= 9267340.0) ? " + 
"0.033626900314855455" + 
":  " + 
"-0.003500579416779472" + 
":  " + 
"(b('ndvi') <= 3761.0) ? " + 
"0.000457273159989466" + 
":  " + 
"-0.021415074397430744" + 
":  " + 
"(b('ndvi') <= 3901.0) ? " + 
"(b('lat') <= 56.023799896240234) ? " + 
"-0.0005746293959757288" + 
":  " + 
"0.01514345270486371" + 
":  " + 
"(b('clay') <= 21.5) ? " + 
"-0.002055663401277088" + 
":  " + 
"0.011739850631009472" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('L8b5') <= 3061.0) ? " + 
"(b('L8b11') <= 2365.0) ? " + 
"0.0006848264601670032" + 
":  " + 
"-0.02181904559009909" + 
":  " + 
"(b('L8b3med') <= 582.5) ? " + 
"0.09542671457788932" + 
":  " + 
"-0.03377167487572212" + 
":  " + 
"(b('L8b3med') <= 565.0) ? " + 
"(b('dgvh') <= -6.796824932098389) ? " + 
"0.07346765767317348" + 
":  " + 
"0.030236747173657288" + 
":  " + 
"(b('L8b7') <= 1013.5) ? " + 
"0.029318730263794633" + 
":  " + 
"2.177856578382234e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b6') <= 3147.5) ? " + 
"(b('L8b4med') <= 1502.25) ? " + 
"-0.0003704777328654878" + 
":  " + 
"0.00630131486142246" + 
":  " + 
"(b('L8b5') <= 2006.5) ? " + 
"0.040386046042128955" + 
":  " + 
"-0.004563537991903657" + 
":  " + 
"(b('L8b4') <= 757.0) ? " + 
"(b('L8b3') <= 753.5) ? " + 
"0.007959370449632127" + 
":  " + 
"0.10073778137230553" + 
":  " + 
"(b('L8b4') <= 811.25) ? " + 
"-0.02616417508282546" + 
":  " + 
"0.001302769492906111" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2874353.5) ? " + 
"(b('crop') <= 88.85982513427734) ? " + 
"(b('L8b5') <= 1935.5) ? " + 
"0.0061121197175396345" + 
":  " + 
"-0.00033122610568566487" + 
":  " + 
"(b('L8b1') <= 449.5) ? " + 
"-0.01392794681862691" + 
":  " + 
"0.00018220897507151905" + 
":  " + 
"(b('L8b6') <= 4860.5) ? " + 
"(b('moss') <= 2.2056541442871094) ? " + 
"0.013928063057127014" + 
":  " + 
"0.00039409580670943337" + 
":  " + 
"(b('dsvv') <= -1.5324668884277344) ? " + 
"0.042209978086750186" + 
":  " + 
"-0.04411102570030974" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1529.5) ? " + 
"(b('L8b7') <= 1095.0) ? " + 
"(b('dsvh') <= -3.333728313446045) ? " + 
"-0.0028058493294858076" + 
":  " + 
"-0.05457779725273636" + 
":  " + 
"(b('L8dt') <= 2701531.0) ? " + 
"-0.064162704773025" + 
":  " + 
"-0.1013031695676158" + 
":  " + 
"(b('L8b6') <= 1584.5) ? " + 
"(b('dgvv') <= 0.40509605407714844) ? " + 
"0.05742683184505887" + 
":  " + 
"0.0007184537113010923" + 
":  " + 
"(b('L8b7') <= 851.0) ? " + 
"-0.14776812627008107" + 
":  " + 
"4.408319869580549e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -11.705314636230469) ? " + 
"(b('clay') <= 26.0) ? " + 
"(b('L8b4') <= 1561.5) ? " + 
"-0.0008852042416402353" + 
":  " + 
"-0.030724449798178607" + 
":  " + 
"(b('dsvh') <= -11.910575866699219) ? " + 
"-0.09111136510868063" + 
":  " + 
"-0.007074447527579519" + 
":  " + 
"(b('gvv') <= -15.280674457550049) ? " + 
"(b('dgvv') <= 1.4946579933166504) ? " + 
"-0.003211565207034953" + 
":  " + 
"0.07975079615944253" + 
":  " + 
"(b('dgvv') <= -4.724893093109131) ? " + 
"-0.03559170310164163" + 
":  " + 
"0.0004765222510675418" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4169.5) ? " + 
"(b('ndvi') <= 5278.5) ? " + 
"0.00024027373450707094" + 
":  " + 
"-0.0072891632237112244" + 
":  " + 
"(b('L8b3') <= 893.0) ? " + 
"0.06517315999605808" + 
":  " + 
"0.012884163883301476" + 
":  " + 
"(b('dsvv') <= 1.1198410987854004) ? " + 
"(b('L8dt') <= 2073598.5) ? " + 
"0.005804152987050338" + 
":  " + 
"-0.07038877166312996" + 
":  " + 
"(b('L8b3') <= 1001.0) ? " + 
"0.010536453128462877" + 
":  " + 
"-0.053402050347454134" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 68.5) ? " + 
"(b('dsvv') <= 0.30853796005249023) ? " + 
"(b('dgvh') <= -8.488377571105957) ? " + 
"0.03641291932390651" + 
":  " + 
"0.06305711648121796" + 
":  " + 
"(b('L8dt') <= 453436.0) ? " + 
"-0.027549673455273836" + 
":  " + 
"0.033195782499206725" + 
":  " + 
"(b('L8b7') <= 820.5) ? " + 
"(b('L8dt') <= 143426.0) ? " + 
"0.04730108392919211" + 
":  " + 
"-0.027466519115722517" + 
":  " + 
"(b('L8b1') <= 126.0) ? " + 
"-0.05822766618005811" + 
":  " + 
"9.762135241902989e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1620.0) ? " + 
"(b('L8b11') <= 2738.5) ? " + 
"(b('gvv') <= -8.554477214813232) ? " + 
"-0.004785935599657033" + 
":  " + 
"0.015645538006204027" + 
":  " + 
"(b('L8b7') <= 2651.5) ? " + 
"0.01024700090391551" + 
":  " + 
"-4.682784201864158e-05" + 
":  " + 
"(b('ndvi_med') <= 1273.75) ? " + 
"(b('lat') <= 36.67852020263672) ? " + 
"0.02212744475328496" + 
":  " + 
"0.08289783550430538" + 
":  " + 
"(b('L8b5') <= 2160.5) ? " + 
"0.004731249369697262" + 
":  " + 
"-0.00023706655954396568" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 16.388042449951172) ? " + 
"(b('dgvh') <= -8.234763145446777) ? " + 
"(b('moss') <= 12.878343105316162) ? " + 
"-0.003909521728503295" + 
":  " + 
"0.0034905500828009174" + 
":  " + 
"(b('moss') <= 7.472553253173828) ? " + 
"0.001744727031586124" + 
":  " + 
"-0.001827914284238901" + 
":  " + 
"(b('L8b5') <= 1785.5) ? " + 
"(b('ndvi') <= 1487.0) ? " + 
"0.014879904106218653" + 
":  " + 
"0.07149102982248498" + 
":  " + 
"(b('L8b5') <= 2308.5) ? " + 
"-0.006800128404923577" + 
":  " + 
"0.006359859892602049" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 7.796026229858398) ? " + 
"(b('gvv') <= -5.816392660140991) ? " + 
"(b('dsvv') <= 3.218355178833008) ? " + 
"-0.00015267197504394367" + 
":  " + 
"0.006476693961972775" + 
":  " + 
"(b('L8b3med') <= 799.5) ? " + 
"-0.021533438262350147" + 
":  " + 
"0.00018155519345039654" + 
":  " + 
"(b('dsvv') <= 8.369709253311157) ? " + 
"0.08684033481497379" + 
":  " + 
"0.060611897357138386" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 38.5) ? " + 
"(b('L8b2') <= 316.5) ? " + 
"(b('L8b1') <= 230.5) ? " + 
"0.002058571235976175" + 
":  " + 
"0.031159818882164396" + 
":  " + 
"(b('L8b3') <= 562.5) ? " + 
"-0.020220024276587634" + 
":  " + 
"0.000143185962296755" + 
":  " + 
"(b('dsvv') <= 0.7563490867614746) ? " + 
"(b('L8b5') <= 2180.0) ? " + 
"0.013502446670142408" + 
":  " + 
"-0.016281415548095247" + 
":  " + 
"(b('L8b5') <= 2154.5) ? " + 
"-0.026280233239971796" + 
":  " + 
"-0.06948019859914824" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 253.5) ? " + 
"(b('L8b4') <= 733.5) ? " + 
"(b('L8b4') <= 726.0) ? " + 
"0.0032889260831972223" + 
":  " + 
"0.14370327116523302" + 
":  " + 
"(b('moss') <= 10.11153793334961) ? " + 
"-0.01405185371246815" + 
":  " + 
"-0.04818502991442721" + 
":  " + 
"(b('L8b1') <= 295.5) ? " + 
"(b('L8b2') <= 348.5) ? " + 
"-0.01447698948339779" + 
":  " + 
"0.012075388284016705" + 
":  " + 
"(b('lat') <= 56.0489501953125) ? " + 
"-0.00013093565581465117" + 
":  " + 
"-0.1183928011547284" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3385997.0) ? " + 
"(b('L8b4') <= 612.5) ? " + 
"(b('L8b5') <= 2402.0) ? " + 
"-0.00621793836381971" + 
":  " + 
"0.011962843362252078" + 
":  " + 
"(b('L8b2') <= 377.5) ? " + 
"-0.009709610356470989" + 
":  " + 
"3.162018037165811e-05" + 
":  " + 
"(b('clay') <= 34.5) ? " + 
"(b('L8b4med') <= 722.5) ? " + 
"-0.013293400467117203" + 
":  " + 
"0.007481200050761199" + 
":  " + 
"-0.1417086191099206" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6342931.5) ? " + 
"(b('L8b5') <= 3141.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"0.0002814129851545074" + 
":  " + 
"0.037450311310115406" + 
":  " + 
"(b('L8b3') <= 762.0) ? " + 
"-0.018568737655012983" + 
":  " + 
"8.789907529464584e-05" + 
":  " + 
"(b('ndvi') <= 1380.0) ? " + 
"(b('L8dt') <= 7522938.0) ? " + 
"0.052982184144777504" + 
":  " + 
"-0.020542758666273964" + 
":  " + 
"(b('bulk') <= 131.0) ? " + 
"0.020100567128512416" + 
":  " + 
"-0.005005547668397348" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 830.5) ? " + 
"(b('L8b3') <= 761.5) ? " + 
"(b('L8b5') <= 3139.5) ? " + 
"0.0014908842250238039" + 
":  " + 
"-0.016935109374519218" + 
":  " + 
"(b('lon') <= -110.59786224365234) ? " + 
"0.059291726608406495" + 
":  " + 
"0.00861152980087397" + 
":  " + 
"(b('L8b3') <= 832.5) ? " + 
"(b('lon') <= -111.45058822631836) ? " + 
"-0.02180260568773963" + 
":  " + 
"-0.0025999049455539386" + 
":  " + 
"(b('L8b6') <= 1850.5) ? " + 
"0.04633997320543477" + 
":  " + 
"4.390158999148078e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2100.5) ? " + 
"(b('lat') <= 50.95975112915039) ? " + 
"(b('lat') <= 44.82858085632324) ? " + 
"-0.00046171245458969203" + 
":  " + 
"-0.00915279071317133" + 
":  " + 
"(b('L8b4') <= 1015.0) ? " + 
"0.015014989494529124" + 
":  " + 
"0.06978037669137849" + 
":  " + 
"(b('lon') <= -111.12804794311523) ? " + 
"(b('ndvi_med') <= 2297.25) ? " + 
"0.0226977595397823" + 
":  " + 
"-0.004695131368173603" + 
":  " + 
"(b('L8b4') <= 1056.5) ? " + 
"-0.002050807466673762" + 
":  " + 
"0.0037299354830213254" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 697.5) ? " + 
"(b('L8b3') <= 759.5) ? " + 
"(b('crop') <= 54.728538513183594) ? " + 
"0.00517388275127689" + 
":  " + 
"-0.007551972612690019" + 
":  " + 
"(b('L8b5') <= 3744.5) ? " + 
"0.031207647304114624" + 
":  " + 
"-0.08056010773389416" + 
":  " + 
"(b('L8b1') <= 255.5) ? " + 
"(b('moss') <= 10.11153793334961) ? " + 
"-0.00727726717337249" + 
":  " + 
"-0.04291199114619629" + 
":  " + 
"(b('L8b3med') <= 565.0) ? " + 
"0.042079749460731376" + 
":  " + 
"-0.00015277629233413178" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 50288.5) ? " + 
"(b('L8dt') <= 38960.0) ? " + 
"(b('dsvh') <= -7.32289457321167) ? " + 
"0.005547774067984327" + 
":  " + 
"-0.006170157709590899" + 
":  " + 
"(b('dsvv') <= -2.200188636779785) ? " + 
"-0.0918643307312879" + 
":  " + 
"-0.011285016294140169" + 
":  " + 
"(b('L8dt') <= 70515.5) ? " + 
"(b('L8dt') <= 70338.5) ? " + 
"0.004897472451185778" + 
":  " + 
"0.046807346979606805" + 
":  " + 
"(b('L8dt') <= 124934.0) ? " + 
"-0.005631742336413606" + 
":  " + 
"0.0003088746445598313" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1370.0) ? " + 
"(b('ndvi') <= 1506.0) ? " + 
"(b('dsvv') <= -1.099656581878662) ? " + 
"0.014006820175618918" + 
":  " + 
"-0.001614864296215377" + 
":  " + 
"(b('L8b1') <= 501.0) ? " + 
"-0.008158254475888194" + 
":  " + 
"0.024000290492369084" + 
":  " + 
"(b('L8b3med') <= 1375.75) ? " + 
"(b('ndvi') <= 1137.5) ? " + 
"-0.010371097756872135" + 
":  " + 
"0.0003662963630290187" + 
":  " + 
"(b('L8b6med') <= 3770.5) ? " + 
"-0.014877698671034412" + 
":  " + 
"-0.000322948411443587" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 7.796026229858398) ? " + 
"(b('dgvv') <= -6.715389013290405) ? " + 
"(b('L8b6') <= 3845.5) ? " + 
"-0.01502280805664473" + 
":  " + 
"-0.08914936834484752" + 
":  " + 
"(b('gvv') <= -5.816392660140991) ? " + 
"0.00010122775028291635" + 
":  " + 
"-0.009243008602983238" + 
":  " + 
"(b('ndvi') <= 1968.5) ? " + 
"0.05966052716987759" + 
":  " + 
"0.08416495001517345" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 352.5) ? " + 
"(b('L8b3') <= 845.5) ? " + 
"(b('L8b2') <= 481.0) ? " + 
"0.0004831327282180016" + 
":  " + 
"-0.03136850985938257" + 
":  " + 
"(b('sand') <= 74.0) ? " + 
"0.009029351348110917" + 
":  " + 
"0.10372182757983632" + 
":  " + 
"(b('L8b1') <= 399.5) ? " + 
"(b('L8b7') <= 1894.0) ? " + 
"-0.010514839619961141" + 
":  " + 
"0.009823180444885128" + 
":  " + 
"(b('L8b2') <= 517.5) ? " + 
"0.012627502033881967" + 
":  " + 
"-9.109134489621903e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2998.5) ? " + 
"(b('ndvi_med') <= 4777.75) ? " + 
"(b('L8b4med') <= 1444.75) ? " + 
"-0.0014021802029745229" + 
":  " + 
"0.003820344339138613" + 
":  " + 
"(b('L8b6med') <= 2684.5) ? " + 
"0.009529475175480239" + 
":  " + 
"0.08443285066025191" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"(b('sand') <= 30.0) ? " + 
"-0.0014454611219245842" + 
":  " + 
"0.012453446708222037" + 
":  " + 
"(b('L8b7') <= 2953.5) ? " + 
"-0.007183797274563991" + 
":  " + 
"0.0015536862323442654" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1184.5) ? " + 
"(b('L8b7') <= 2019.5) ? " + 
"(b('lon') <= 25.963054656982422) ? " + 
"0.0009273899100042365" + 
":  " + 
"-0.007936824639564985" + 
":  " + 
"(b('L8b3med') <= 1016.0) ? " + 
"0.0035422484949071175" + 
":  " + 
"0.03228224423490988" + 
":  " + 
"(b('L8b5') <= 1795.0) ? " + 
"(b('L8b3med') <= 1455.25) ? " + 
"-0.01685486458285736" + 
":  " + 
"-0.11381275434542022" + 
":  " + 
"(b('L8b3') <= 916.5) ? " + 
"-0.017329634053024016" + 
":  " + 
"-0.0004192082301571951" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 853.5) ? " + 
"(b('L8b3') <= 845.5) ? " + 
"(b('L8b11') <= 2898.5) ? " + 
"0.0009238181334849586" + 
":  " + 
"-0.03546530256110834" + 
":  " + 
"(b('L8b6med') <= 3078.0) ? " + 
"0.006937363809869662" + 
":  " + 
"0.06485317029606491" + 
":  " + 
"(b('L8b11') <= 1342.5) ? " + 
"(b('L8b6') <= 2954.0) ? " + 
"0.00042099730112718346" + 
":  " + 
"0.08727122051341493" + 
":  " + 
"(b('L8b3') <= 888.5) ? " + 
"-0.005775210051437233" + 
":  " + 
"0.0003307604434857793" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1134.5) ? " + 
"(b('L8b4') <= 1084.5) ? " + 
"(b('lon') <= 25.963054656982422) ? " + 
"0.0011498457609643617" + 
":  " + 
"-0.00723059150170421" + 
":  " + 
"(b('L8b3med') <= 705.0) ? " + 
"0.15700138592550755" + 
":  " + 
"0.012286267155116378" + 
":  " + 
"(b('L8b7') <= 1523.0) ? " + 
"(b('L8b6') <= 1843.0) ? " + 
"0.08720460773718544" + 
":  " + 
"-0.05589775011342913" + 
":  " + 
"(b('L8b5') <= 1793.5) ? " + 
"-0.053408105544171386" + 
":  " + 
"-0.0005157004797201013" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1935.5) ? " + 
"(b('L8b3med') <= 1375.75) ? " + 
"(b('L8b5') <= 1927.0) ? " + 
"0.0040556460040100705" + 
":  " + 
"0.05720188519427236" + 
":  " + 
"(b('L8b4') <= 1235.0) ? " + 
"-0.028007146837236107" + 
":  " + 
"-0.09712374440080963" + 
":  " + 
"(b('L8b6med') <= 2154.25) ? " + 
"(b('gvv') <= -13.102675437927246) ? " + 
"-0.0674165738790691" + 
":  " + 
"-0.00939073599356354" + 
":  " + 
"(b('L8b6') <= 1930.5) ? " + 
"0.008385303429755221" + 
":  " + 
"-0.00037117675171175434" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('L8b2') <= 994.5) ? " + 
"(b('ndvi') <= 2593.5) ? " + 
"-0.003306162449326253" + 
":  " + 
"0.023189324795417448" + 
":  " + 
"(b('gvv') <= -15.038346767425537) ? " + 
"0.11937608229037078" + 
":  " + 
"0.10868134815174725" + 
":  " + 
"(b('lat') <= -35.01868438720703) ? " + 
"(b('L8b7') <= 2336.0) ? " + 
"-0.03188923806414835" + 
":  " + 
"0.003924089649952779" + 
":  " + 
"(b('dsvv') <= 4.98840856552124) ? " + 
"1.1238081131507994e-05" + 
":  " + 
"0.014689616182059316" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4348.5) ? " + 
"(b('ndvi') <= 5278.5) ? " + 
"0.00023990251697948982" + 
":  " + 
"-0.004980623102808743" + 
":  " + 
"(b('dgvh') <= -8.225106239318848) ? " + 
"0.041127328956314796" + 
":  " + 
"0.08087726016476593" + 
":  " + 
"(b('dgvv') <= 1.1202073097229004) ? " + 
"(b('L8b5') <= 4762.5) ? " + 
"-0.0018523449502119487" + 
":  " + 
"0.07162905068795537" + 
":  " + 
"(b('moss') <= 1.7488588690757751) ? " + 
"0.01754271869220973" + 
":  " + 
"-0.047009289610688086" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 468.0) ? " + 
"(b('L8b1') <= 66.0) ? " + 
"(b('L8dt') <= 281736.0) ? " + 
"-0.02618878473477039" + 
":  " + 
"0.03857114316032103" + 
":  " + 
"(b('ndvi_med') <= 3316.0) ? " + 
"-0.009840627125461306" + 
":  " + 
"-0.036530934597019116" + 
":  " + 
"(b('L8b3') <= 518.5) ? " + 
"(b('ndvi') <= 5314.5) ? " + 
"0.020219706909649148" + 
":  " + 
"-0.04708921736769177" + 
":  " + 
"(b('L8b1') <= 126.0) ? " + 
"-0.03895745273777295" + 
":  " + 
"-3.172536908797971e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6342931.5) ? " + 
"(b('dsvh') <= -11.270516872406006) ? " + 
"(b('clay') <= 26.0) ? " + 
"-0.0030780088339404537" + 
":  " + 
"-0.041084497396612345" + 
":  " + 
"(b('crop') <= 88.85982513427734) ? " + 
"0.00035035116374594" + 
":  " + 
"-0.003000149514837757" + 
":  " + 
"(b('ndvi') <= 1380.0) ? " + 
"(b('L8b6med') <= 3006.0) ? " + 
"-0.018604331071233056" + 
":  " + 
"0.047844868075953985" + 
":  " + 
"(b('bulk') <= 131.0) ? " + 
"0.01954076936703013" + 
":  " + 
"-0.005234897185371759" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 236044.5) ? " + 
"(b('L8dt') <= 236042.0) ? " + 
"(b('dsvh') <= -4.714461803436279) ? " + 
"-0.0002750395359919368" + 
":  " + 
"-0.010255713754256032" + 
":  " + 
"(b('L8b5') <= 3745.5) ? " + 
"-0.04054779722035034" + 
":  " + 
"0.0006684266472245749" + 
":  " + 
"(b('L8dt') <= 238704.5) ? " + 
"(b('dgvh') <= -4.040650367736816) ? " + 
"0.012016396340194533" + 
":  " + 
"0.07791569707767756" + 
":  " + 
"(b('L8b7') <= 846.5) ? " + 
"-0.017447008925700412" + 
":  " + 
"0.0003143011965439516" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1934.0) ? " + 
"(b('L8b3med') <= 1416.5) ? " + 
"(b('L8b5') <= 1927.0) ? " + 
"0.0033973264341004023" + 
":  " + 
"0.05685695431415732" + 
":  " + 
"(b('L8b1') <= 459.0) ? " + 
"-0.03721602610175682" + 
":  " + 
"-0.1101840324459063" + 
":  " + 
"(b('L8b4') <= 529.0) ? " + 
"(b('L8dt') <= 3887976.0) ? " + 
"0.015955209062453332" + 
":  " + 
"-0.048705105967111896" + 
":  " + 
"(b('L8b3') <= 601.5) ? " + 
"-0.017088145283968778" + 
":  " + 
"-0.00013363007855116889" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 352.5) ? " + 
"(b('bulk') <= 152.5) ? " + 
"(b('ndvi') <= 2731.5) ? " + 
"0.010273859964539583" + 
":  " + 
"-0.0008729822516014796" + 
":  " + 
"(b('L8b4') <= 880.5) ? " + 
"-0.007407290817281294" + 
":  " + 
"-0.062127099727053575" + 
":  " + 
"(b('L8b1') <= 400.5) ? " + 
"(b('L8b6') <= 2436.0) ? " + 
"-0.014923360608746557" + 
":  " + 
"-0.002130438707002097" + 
":  " + 
"(b('L8b2') <= 517.5) ? " + 
"0.011980543453340708" + 
":  " + 
"-0.00013802807101787488" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b6') <= 2659.5) ? " + 
"(b('L8b3') <= 882.5) ? " + 
"-0.0008533400118103863" + 
":  " + 
"0.008888809231386833" + 
":  " + 
"(b('L8b6') <= 2699.5) ? " + 
"-0.02049437561124878" + 
":  " + 
"-0.0013435261510748784" + 
":  " + 
"(b('L8b6') <= 3467.5) ? " + 
"(b('L8b1') <= 500.5) ? " + 
"-0.0014601670054775644" + 
":  " + 
"0.018670390005199055" + 
":  " + 
"(b('ndvi') <= 2872.5) ? " + 
"-0.0016549577004068394" + 
":  " + 
"0.01409926329688857" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4348.5) ? " + 
"(b('L8dt') <= 2038067.0) ? " + 
"-0.0002766338453190099" + 
":  " + 
"0.002675046925056285" + 
":  " + 
"(b('L8dt') <= 2701531.0) ? " + 
"0.07169817569338009" + 
":  " + 
"0.03590359291468954" + 
":  " + 
"(b('L8dt') <= 2073598.5) ? " + 
"(b('L8b3med') <= 1145.5) ? " + 
"0.021101506341803706" + 
":  " + 
"-0.018961417823923743" + 
":  " + 
"(b('ndvi_med') <= 1565.5) ? " + 
"-0.028715300015975564" + 
":  " + 
"-0.07798373707544394" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1728.0) ? " + 
"(b('L8b4') <= 936.5) ? " + 
"(b('L8b2') <= 339.5) ? " + 
"-0.0028875874487551416" + 
":  " + 
"-0.02425640389927952" + 
":  " + 
"(b('L8b11') <= 1706.5) ? " + 
"0.06249721472237694" + 
":  " + 
"-0.02003801884373726" + 
":  " + 
"(b('L8b6') <= 1921.0) ? " + 
"(b('gvv') <= -14.124295234680176) ? " + 
"-0.03506423093286812" + 
":  " + 
"0.012543951078308935" + 
":  " + 
"(b('L8b6') <= 2011.5) ? " + 
"-0.011561472488346316" + 
":  " + 
"1.1241079582192005e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 756.5) ? " + 
"(b('lon') <= -115.05220413208008) ? " + 
"(b('L8b7') <= 1215.5) ? " + 
"-0.005535703652144489" + 
":  " + 
"0.05063845094310845" + 
":  " + 
"(b('lon') <= 9.210049629211426) ? " + 
"-0.003197548868131202" + 
":  " + 
"0.006433761681083656" + 
":  " + 
"(b('L8b1') <= 255.5) ? " + 
"(b('L8b6') <= 2598.5) ? " + 
"-0.01281537312157626" + 
":  " + 
"-0.10238043793420781" + 
":  " + 
"(b('L8b1') <= 295.5) ? " + 
"0.015379957012816291" + 
":  " + 
"-0.0005230726894415414" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 16.250526428222656) ? " + 
"(b('dsvh') <= -8.33658742904663) ? " + 
"(b('L8b7') <= 3243.0) ? " + 
"-0.0031534048756109616" + 
":  " + 
"0.006298580691787665" + 
":  " + 
"(b('L8b5') <= 2545.5) ? " + 
"0.002334123650660497" + 
":  " + 
"-0.0008886469555429031" + 
":  " + 
"(b('ndvi') <= 3136.0) ? " + 
"(b('dsvh') <= -9.633480072021484) ? " + 
"0.023566635719288954" + 
":  " + 
"-9.377335754786339e-05" + 
":  " + 
"(b('L8dt') <= 21116.5) ? " + 
"0.11362876549753355" + 
":  " + 
"0.016728332351885408" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 701.5) ? " + 
"(b('dgvv') <= 2.148322105407715) ? " + 
"(b('dgvv') <= 2.0047073364257812) ? " + 
"-0.007561136849336097" + 
":  " + 
"0.0976308869420221" + 
":  " + 
"(b('L8b4') <= 2931.5) ? " + 
"-0.07406793603754959" + 
":  " + 
"-0.04285705454134708" + 
":  " + 
"(b('L8b3med') <= 1653.0) ? " + 
"(b('ndvi') <= 1182.5) ? " + 
"-0.005046956040001088" + 
":  " + 
"0.0002102091063774086" + 
":  " + 
"(b('dgvv') <= -1.0485200881958008) ? " + 
"0.02315491614838888" + 
":  " + 
"0.0029836894824817315" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b4') <= 2046.5) ? " + 
"(b('L8b3') <= 1527.5) ? " + 
"-0.0006915725415909151" + 
":  " + 
"0.02006441633040636" + 
":  " + 
"(b('L8b6med') <= 3370.0) ? " + 
"-0.0027884528847283156" + 
":  " + 
"-0.04384760921253467" + 
":  " + 
"(b('L8b5') <= 2456.5) ? " + 
"(b('L8b3') <= 1216.0) ? " + 
"0.004052010086053053" + 
":  " + 
"0.04784937396293177" + 
":  " + 
"(b('ndvi') <= 2866.5) ? " + 
"-0.0013346074910599776" + 
":  " + 
"0.009848075066514228" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -16.012653350830078) ? " + 
"(b('lon') <= -120.35504531860352) ? " + 
"(b('L8b7') <= 2563.0) ? " + 
"0.03759447489067869" + 
":  " + 
"-0.0024943516382243173" + 
":  " + 
"(b('L8dt') <= 16543.0) ? " + 
"0.12908157091481562" + 
":  " + 
"-0.00504070689324841" + 
":  " + 
"(b('lon') <= 147.53404998779297) ? " + 
"(b('lat') <= -35.01868438720703) ? " + 
"-0.008396035836058274" + 
":  " + 
"0.0003585595629850732" + 
":  " + 
"(b('L8b5') <= 2046.5) ? " + 
"-0.07365226875546815" + 
":  " + 
"0.03901101916251446" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 46936.5) ? " + 
"(b('L8dt') <= 38977.0) ? " + 
"(b('dgvh') <= -2.7669973373413086) ? " + 
"1.0348451647487633e-06" + 
":  " + 
"-0.03461448887466796" + 
":  " + 
"(b('gvv') <= -14.737429141998291) ? " + 
"-0.07478472974103233" + 
":  " + 
"-0.016173199842544606" + 
":  " + 
"(b('L8dt') <= 102066.5) ? " + 
"(b('dsvv') <= 2.874256134033203) ? " + 
"0.0031971329058221947" + 
":  " + 
"0.0405853701114188" + 
":  " + 
"(b('L8dt') <= 124934.0) ? " + 
"-0.005988283916319374" + 
":  " + 
"0.000253921776701177" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3904.0) ? " + 
"(b('L8b5') <= 3846.0) ? " + 
"(b('L8b5') <= 3533.0) ? " + 
"0.00028387078966762337" + 
":  " + 
"-0.004362675957199977" + 
":  " + 
"(b('L8b5') <= 3854.0) ? " + 
"0.07421799235922251" + 
":  " + 
"0.01681806034885974" + 
":  " + 
"(b('sand') <= 29.5) ? " + 
"(b('L8b2') <= 836.5) ? " + 
"-0.031270729497345676" + 
":  " + 
"0.05261097422560454" + 
":  " + 
"(b('L8b1') <= 304.0) ? " + 
"0.026500162869691365" + 
":  " + 
"-0.0033667047689734286" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('L8b5') <= 3061.0) ? " + 
"(b('L8b11') <= 1655.0) ? " + 
"0.003529317462077794" + 
":  " + 
"-0.007781470749716123" + 
":  " + 
"(b('L8b4') <= 608.0) ? " + 
"-0.06359797461858387" + 
":  " + 
"-0.012325160121984813" + 
":  " + 
"(b('L8b3med') <= 565.0) ? " + 
"(b('dgvh') <= -6.796824932098389) ? " + 
"0.06098174677524328" + 
":  " + 
"0.02252883394837855" + 
":  " + 
"(b('L8b3') <= 671.5) ? " + 
"0.021375063467380585" + 
":  " + 
"-4.288451346805583e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 316.5) ? " + 
"(b('L8b3med') <= 619.0) ? " + 
"(b('L8b5') <= 2524.0) ? " + 
"0.005738836846022828" + 
":  " + 
"0.06669163091620725" + 
":  " + 
"(b('L8b5') <= 3135.0) ? " + 
"0.0036430563578883305" + 
":  " + 
"-0.03499413319958342" + 
":  " + 
"(b('L8b2') <= 347.5) ? " + 
"(b('lat') <= 55.997798919677734) ? " + 
"-0.0034332055037960933" + 
":  " + 
"-0.03701547573722235" + 
":  " + 
"(b('L8b2') <= 350.5) ? " + 
"0.02443820323294795" + 
":  " + 
"2.4585472740235737e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6342931.5) ? " + 
"(b('L8b4med') <= 1444.75) ? " + 
"(b('L8b4') <= 1274.5) ? " + 
"0.00039687751345694153" + 
":  " + 
"-0.005165182052229361" + 
":  " + 
"(b('L8b5') <= 2903.5) ? " + 
"0.0038588811811658915" + 
":  " + 
"-0.0018604288025263233" + 
":  " + 
"(b('L8b11') <= 1712.0) ? " + 
"(b('dgvv') <= 1.5020928382873535) ? " + 
"-3.986303250865493e-05" + 
":  " + 
"0.028999352361354386" + 
":  " + 
"(b('L8b3') <= 1431.0) ? " + 
"0.029364779216645882" + 
":  " + 
"-0.009365811907130659" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 7.796026229858398) ? " + 
"(b('gvv') <= -5.816392660140991) ? " + 
"(b('dsvv') <= 3.218355178833008) ? " + 
"-0.00014480946433156886" + 
":  " + 
"0.005855904229464805" + 
":  " + 
"(b('L8b3med') <= 716.75) ? " + 
"-0.026477844684265683" + 
":  " + 
"-0.003289981103453105" + 
":  " + 
"(b('dsvv') <= 8.369709253311157) ? " + 
"0.07495475329518807" + 
":  " + 
"0.051744513074791346" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 5456.5) ? " + 
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b2') <= 822.5) ? " + 
"0.00010164536543905286" + 
":  " + 
"-0.004333365770750003" + 
":  " + 
"(b('L8b4') <= 757.0) ? " + 
"0.016550646633772457" + 
":  " + 
"0.0008273701987179331" + 
":  " + 
"(b('dsvh') <= -8.415994644165039) ? " + 
"(b('dgvv') <= -0.07757377624511719) ? " + 
"-0.028222363775912477" + 
":  " + 
"-0.00860702128767643" + 
":  " + 
"(b('L8b6med') <= 3826.5) ? " + 
"-0.053495777516981764" + 
":  " + 
"-0.04362579630820522" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('sand') <= 31.5) ? " + 
"(b('lon') <= 26.368294715881348) ? " + 
"0.012633748388199393" + 
":  " + 
"-0.03335790175182573" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"0.005383543869579593" + 
":  " + 
"-0.009908697324852996" + 
":  " + 
"(b('L8b3med') <= 565.0) ? " + 
"(b('ndvi') <= 2579.5) ? " + 
"0.0859717075384455" + 
":  " + 
"0.025934462340631976" + 
":  " + 
"(b('L8b4') <= 697.5) ? " + 
"0.007667161191598558" + 
":  " + 
"-0.00022494563838406644" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 468.0) ? " + 
"(b('L8b1') <= 66.0) ? " + 
"(b('L8dt') <= 281736.0) ? " + 
"-0.02316661627965077" + 
":  " + 
"0.035127129473230496" + 
":  " + 
"(b('gvv') <= -10.424904823303223) ? " + 
"-0.022444356420832926" + 
":  " + 
"0.012520651046154407" + 
":  " + 
"(b('L8b3') <= 518.5) ? " + 
"(b('gvv') <= -12.263354778289795) ? " + 
"0.03573007477378595" + 
":  " + 
"0.0003082553393325341" + 
":  " + 
"(b('L8b3') <= 528.5) ? " + 
"-0.026314765054397296" + 
":  " + 
"-2.6692248539945713e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1728.0) ? " + 
"(b('L8b4') <= 936.5) ? " + 
"(b('dgvv') <= 3.4883100986480713) ? " + 
"-0.0051828204234641235" + 
":  " + 
"-0.042755862226911384" + 
":  " + 
"(b('lat') <= 40.10690879821777) ? " + 
"-0.017647239912869393" + 
":  " + 
"0.056312948084685045" + 
":  " + 
"(b('L8b6') <= 1921.0) ? " + 
"(b('gvv') <= -12.977222442626953) ? " + 
"-0.014942526582166854" + 
":  " + 
"0.012718134657095" + 
":  " + 
"(b('L8b6') <= 2011.5) ? " + 
"-0.010537521712074142" + 
":  " + 
"2.025711239389313e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -6.715389013290405) ? " + 
"(b('L8b3') <= 1277.5) ? " + 
"(b('L8b4') <= 1294.0) ? " + 
"-0.004454666280470183" + 
":  " + 
"-0.029067882345605242" + 
":  " + 
"(b('gvv') <= -13.589753150939941) ? " + 
"-0.07494206530404941" + 
":  " + 
"-0.07944206697297947" + 
":  " + 
"(b('lat') <= 52.296464920043945) ? " + 
"(b('dgvh') <= -12.092339992523193) ? " + 
"-0.04623675239958435" + 
":  " + 
"-0.0002030923289543653" + 
":  " + 
"(b('ndvi') <= 2731.5) ? " + 
"0.04001319231328896" + 
":  " + 
"-0.001662257507967103" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 872.5) ? " + 
"(b('L8b3') <= 860.5) ? " + 
"(b('L8b3') <= 856.5) ? " + 
"-0.0008096791600976098" + 
":  " + 
"0.02273556729954391" + 
":  " + 
"(b('ndvi_med') <= 2857.5) ? " + 
"-0.001131202356493824" + 
":  " + 
"-0.035043022592171576" + 
":  " + 
"(b('L8b4') <= 1134.5) ? " + 
"(b('lon') <= -112.09711837768555) ? " + 
"0.03683207378652342" + 
":  " + 
"0.004727364091547658" + 
":  " + 
"(b('L8b7') <= 1523.0) ? " + 
"-0.04236293951527248" + 
":  " + 
"-0.00041661048261930437" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2026.5) ? " + 
"(b('L8b11') <= 2889.25) ? " + 
"(b('L8b7') <= 1970.5) ? " + 
"0.0002677674443525543" + 
":  " + 
"-0.012038516035358373" + 
":  " + 
"(b('lat') <= 35.94770431518555) ? " + 
"-0.07085237366850049" + 
":  " + 
"-0.015846555890727945" + 
":  " + 
"(b('L8b4') <= 1273.25) ? " + 
"(b('moss') <= 24.165419578552246) ? " + 
"0.006546038726128485" + 
":  " + 
"0.06884222644948185" + 
":  " + 
"(b('L8b4') <= 1286.5) ? " + 
"-0.03221149641873705" + 
":  " + 
"-0.0004982807562691993" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4med') <= 1521.5) ? " + 
"(b('L8b3') <= 1474.5) ? " + 
"(b('L8b2') <= 833.5) ? " + 
"-0.00045429902051604976" + 
":  " + 
"-0.008988470535836568" + 
":  " + 
"(b('ndvi_med') <= 2623.25) ? " + 
"0.009819551683814822" + 
":  " + 
"0.054793523365373555" + 
":  " + 
"(b('L8b4') <= 1547.0) ? " + 
"(b('L8b5') <= 3015.0) ? " + 
"0.013502746464688468" + 
":  " + 
"-0.010494784263905299" + 
":  " + 
"(b('L8b2') <= 590.0) ? " + 
"0.11938034163496955" + 
":  " + 
"-0.000787661544251155" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1508.0) ? " + 
"(b('L8b2') <= 822.5) ? " + 
"(b('L8b2') <= 818.5) ? " + 
"0.00020024676254925058" + 
":  " + 
"0.03200828362299668" + 
":  " + 
"(b('L8b11') <= 1466.25) ? " + 
"0.06524416212324784" + 
":  " + 
"-0.004187011896775039" + 
":  " + 
"(b('lat') <= -35.10758972167969) ? " + 
"(b('ndvi') <= 1475.5) ? " + 
"0.15884427974055124" + 
":  " + 
"0.07492088493739132" + 
":  " + 
"(b('L8b4') <= 2026.5) ? " + 
"0.014076640682653865" + 
":  " + 
"-0.0014927513351250612" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4med') <= 2251.5) ? " + 
"(b('ndvi') <= 1182.5) ? " + 
"(b('ndvi') <= 1179.5) ? " + 
"-0.0031710782212805186" + 
":  " + 
"-0.1111452802457452" + 
":  " + 
"(b('ndvi') <= 1373.5) ? " + 
"0.004115062976800222" + 
":  " + 
"-0.00023728016076696534" + 
":  " + 
"(b('L8b3') <= 1610.5) ? " + 
"(b('L8b7') <= 2182.5) ? " + 
"0.0039962820773966675" + 
":  " + 
"0.03453871644177311" + 
":  " + 
"(b('L8b1') <= 769.5) ? " + 
"-0.03165240078388266" + 
":  " + 
"0.002959508723244392" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4med') <= 1444.75) ? " + 
"(b('L8b5') <= 1802.5) ? " + 
"(b('lat') <= 44.514474868774414) ? " + 
"0.016655839171299338" + 
":  " + 
"-0.0027542547120532777" + 
":  " + 
"(b('L8b5') <= 2794.5) ? " + 
"-0.002528118147351206" + 
":  " + 
"0.0012704850128106126" + 
":  " + 
"(b('L8b5') <= 1803.5) ? " + 
"(b('ndvi') <= 1417.5) ? " + 
"0.00949254560510685" + 
":  " + 
"-0.03810100059445221" + 
":  " + 
"(b('L8b4') <= 1416.0) ? " + 
"0.008460423906663468" + 
":  " + 
"-0.00014339047891786562" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('ndvi') <= 2688.5) ? " + 
"(b('dsvh') <= -4.055212020874023) ? " + 
"0.005463280133419399" + 
":  " + 
"-0.03729487155621599" + 
":  " + 
"(b('dgvh') <= -1.5524482727050781) ? " + 
"0.014859958996068387" + 
":  " + 
"0.08581932991951184" + 
":  " + 
"(b('lat') <= -35.01868438720703) ? " + 
"(b('L8b7') <= 2336.0) ? " + 
"-0.027925731846141288" + 
":  " + 
"0.003584758460814775" + 
":  " + 
"(b('dgvh') <= -0.7274341583251953) ? " + 
"4.490834190718237e-05" + 
":  " + 
"0.022918527524199265" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1620.0) ? " + 
"(b('L8b6med') <= 2342.0) ? " + 
"(b('L8b5') <= 2125.0) ? " + 
"0.0007358665805032583" + 
":  " + 
"-0.04398727107960455" + 
":  " + 
"(b('ndvi') <= 1373.5) ? " + 
"0.0011208378486193215" + 
":  " + 
"-0.004189641270084446" + 
":  " + 
"(b('ndvi_med') <= 1273.75) ? " + 
"(b('ndvi_med') <= 1141.5) ? " + 
"-0.02833307025080962" + 
":  " + 
"0.04686342754951953" + 
":  " + 
"(b('ndvi') <= 1659.5) ? " + 
"0.010667743328345882" + 
":  " + 
"0.00015050791657572314" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4169.5) ? " + 
"(b('L8b5') <= 3964.0) ? " + 
"0.00011103325555416207" + 
":  " + 
"-0.008757724673679813" + 
":  " + 
"(b('ndvi') <= 5248.5) ? " + 
"0.006886609177812516" + 
":  " + 
"0.04502786474452595" + 
":  " + 
"(b('dgvv') <= 0.4430675506591797) ? " + 
"(b('dsvh') <= -5.994700908660889) ? " + 
"-0.007576576532739364" + 
":  " + 
"0.030651827561786846" + 
":  " + 
"(b('L8b7') <= 1229.0) ? " + 
"0.06164134325602254" + 
":  " + 
"-0.03369279343596088" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 727.5) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"(b('ndvi') <= 2733.5) ? " + 
"0.004929551568667521" + 
":  " + 
"-0.004001261703498412" + 
":  " + 
"(b('ndvi') <= 5326.5) ? " + 
"-0.03060212739375035" + 
":  " + 
"0.04362361299241004" + 
":  " + 
"(b('L8b4') <= 830.5) ? " + 
"(b('lon') <= -106.99895095825195) ? " + 
"0.041972289232180486" + 
":  " + 
"0.003546906283388712" + 
":  " + 
"(b('L8b4') <= 831.5) ? " + 
"-0.06786772598365819" + 
":  " + 
"-0.0002478081019033834" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 872.5) ? " + 
"(b('lon') <= 25.963054656982422) ? " + 
"(b('L8b7') <= 1325.5) ? " + 
"-0.0045392411531862045" + 
":  " + 
"0.001968935823957499" + 
":  " + 
"(b('L8b4') <= 756.0) ? " + 
"0.00958092270634389" + 
":  " + 
"-0.013487930588133619" + 
":  " + 
"(b('L8b4') <= 1134.5) ? " + 
"(b('lon') <= -110.83245468139648) ? " + 
"0.029939865356162082" + 
":  " + 
"0.004004003107623382" + 
":  " + 
"(b('L8b7') <= 1523.0) ? " + 
"-0.038208433469242166" + 
":  " + 
"-0.0003154759020518965" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b6') <= 4607.5) ? " + 
"(b('L8b7') <= 3309.5) ? " + 
"-0.0005972716169682137" + 
":  " + 
"0.03426793256859163" + 
":  " + 
"(b('dsvv') <= 1.60880708694458) ? " + 
"-0.017289413199471592" + 
":  " + 
"-0.07729675681785092" + 
":  " + 
"(b('L8b4') <= 757.0) ? " + 
"(b('L8b6med') <= 3496.75) ? " + 
"0.06320079621273138" + 
":  " + 
"0.004584698971559028" + 
":  " + 
"(b('L8b3') <= 867.5) ? " + 
"-0.007909371679630664" + 
":  " + 
"0.001489704128731815" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3042769.5) ? " + 
"(b('dsvv') <= 4.071635484695435) ? " + 
"(b('dsvh') <= -1.3166069984436035) ? " + 
"-0.00024850363992569974" + 
":  " + 
"-0.03888305790793175" + 
":  " + 
"(b('ndvi') <= 4067.0) ? " + 
"0.013169496160970604" + 
":  " + 
"-0.013295336382347563" + 
":  " + 
"(b('L8dt') <= 3045071.0) ? " + 
"(b('L8b7') <= 1277.0) ? " + 
"0.060240265312618536" + 
":  " + 
"0.10867369666455004" + 
":  " + 
"(b('L8b6') <= 4860.5) ? " + 
"0.003639253574724603" + 
":  " + 
"-0.034386613677592874" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 52.296464920043945) ? " + 
"(b('dgvh') <= -11.592209815979004) ? " + 
"(b('lon') <= 14.096795082092285) ? " + 
"-0.014653623648261168" + 
":  " + 
"-0.060916920848478204" + 
":  " + 
"(b('bulk') <= 129.5) ? " + 
"-0.00596823214366101" + 
":  " + 
"0.00011292871032550673" + 
":  " + 
"(b('ndvi') <= 2835.0) ? " + 
"(b('moss') <= 10.476681232452393) ? " + 
"0.017147545231060365" + 
":  " + 
"0.07027390263237601" + 
":  " + 
"(b('moss') <= 13.384493827819824) ? " + 
"0.0003098821281435597" + 
":  " + 
"-0.019582129982201532" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -15.280674457550049) ? " + 
"(b('ndvi_med') <= 1884.5) ? " + 
"(b('ndvi') <= 1894.5) ? " + 
"-0.0022014302555965265" + 
":  " + 
"0.01614965442308555" + 
":  " + 
"(b('lon') <= -105.8655014038086) ? " + 
"-0.022411305001162635" + 
":  " + 
"-0.003937961785390775" + 
":  " + 
"(b('dgvv') <= -4.558484077453613) ? " + 
"(b('crop') <= 73.88997650146484) ? " + 
"-0.04725059111665115" + 
":  " + 
"-0.0007806382480446021" + 
":  " + 
"(b('dsvv') <= -4.552097320556641) ? " + 
"0.13505849370951137" + 
":  " + 
"0.00030426252674640194" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -6.351504802703857) ? " + 
"(b('dsvv') <= 2.131354808807373) ? " + 
"(b('dgvv') <= 2.180492877960205) ? " + 
"-0.00026640300829276466" + 
":  " + 
"0.18344123501139653" + 
":  " + 
"(b('ndvi') <= 1589.5) ? " + 
"-0.021305744798603796" + 
":  " + 
"-0.003953978184584755" + 
":  " + 
"(b('dgvh') <= -6.350805282592773) ? " + 
"(b('dgvh') <= -6.350888729095459) ? " + 
"0.042202295345797204" + 
":  " + 
"0.22948700156352306" + 
":  " + 
"(b('L8b11') <= 3276.0) ? " + 
"0.0012838302496702523" + 
":  " + 
"-0.017022408900793724" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2026.5) ? " + 
"(b('L8b6') <= 2856.5) ? " + 
"(b('L8b11') <= 2889.25) ? " + 
"0.0005330282982988427" + 
":  " + 
"-0.02089648789372739" + 
":  " + 
"(b('lat') <= 55.97825050354004) ? " + 
"-0.010498203105147612" + 
":  " + 
"0.07532657403135497" + 
":  " + 
"(b('L8b11') <= 1682.0) ? " + 
"(b('L8b6') <= 2714.0) ? " + 
"0.06710351800916256" + 
":  " + 
"0.007516536490379317" + 
":  " + 
"(b('dsvh') <= -3.0452423095703125) ? " + 
"-0.0001226106010399861" + 
":  " + 
"0.018930506173923067" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1370.0) ? " + 
"(b('ndvi') <= 1696.5) ? " + 
"(b('L8b6') <= 2601.5) ? " + 
"-0.016224372008769663" + 
":  " + 
"0.0017116435536548593" + 
":  " + 
"(b('dsvh') <= -1.1574716567993164) ? " + 
"0.015426082869140996" + 
":  " + 
"-0.18092571006110844" + 
":  " + 
"(b('ndvi') <= 878.5) ? " + 
"(b('dsvh') <= -7.183012962341309) ? " + 
"-0.046732797010290504" + 
":  " + 
"0.028165169994719623" + 
":  " + 
"(b('lon') <= -5.546385049819946) ? " + 
"-0.0019166180124859968" + 
":  " + 
"0.00043647292234441046" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 68.5) ? " + 
"(b('dsvv') <= 0.30853796005249023) ? " + 
"(b('dgvh') <= -8.488377571105957) ? " + 
"0.027971590409696438" + 
":  " + 
"0.05046780682754173" + 
":  " + 
"(b('dsvv') <= 0.43216848373413086) ? " + 
"-0.01916546172645557" + 
":  " + 
"0.022668993838634566" + 
":  " + 
"(b('L8b7') <= 820.5) ? " + 
"(b('dgvh') <= -5.737475872039795) ? " + 
"-0.004068473267862781" + 
":  " + 
"-0.04321496286523948" + 
":  " + 
"(b('L8b4') <= 612.5) ? " + 
"0.005033904263739228" + 
":  " + 
"-0.00013523588644792205" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 6114.5) ? " + 
"(b('ndvi') <= 6025.0) ? " + 
"(b('L8b6med') <= 2285.5) ? " + 
"-0.0050576263853478" + 
":  " + 
"0.00022047184707666" + 
":  " + 
"(b('dgvh') <= -7.935764789581299) ? " + 
"0.009688090417165526" + 
":  " + 
"0.09117180517699901" + 
":  " + 
"(b('clay') <= 22.0) ? " + 
"(b('dsvv') <= 0.3930058479309082) ? " + 
"-0.0022286345487954333" + 
":  " + 
"-0.029878790657790116" + 
":  " + 
"(b('L8b3') <= 892.0) ? " + 
"-0.001884654596919323" + 
":  " + 
"0.07009693315546812" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 35512.5) ? " + 
"(b('bulk') <= 134.5) ? " + 
"(b('L8b5') <= 2684.5) ? " + 
"0.01919381227678769" + 
":  " + 
"-0.0013542646473610421" + 
":  " + 
"(b('L8b3') <= 823.5) ? " + 
"-0.032308030656191214" + 
":  " + 
"-0.0035178142563807775" + 
":  " + 
"(b('L8b6med') <= 3416.5) ? " + 
"(b('gvv') <= -15.07451581954956) ? " + 
"-0.005206946354467827" + 
":  " + 
"-5.1005812696952436e-05" + 
":  " + 
"(b('L8b5') <= 2456.5) ? " + 
"0.006616223006517435" + 
":  " + 
"5.519334906531392e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 701.5) ? " + 
"(b('dgvv') <= 2.148322105407715) ? " + 
"(b('dsvv') <= 2.0129055976867676) ? " + 
"-0.006480655996733029" + 
":  " + 
"0.0884897298391837" + 
":  " + 
"(b('L8b4') <= 2931.5) ? " + 
"-0.06513049025052756" + 
":  " + 
"-0.03657604222925852" + 
":  " + 
"(b('L8b3med') <= 1691.0) ? " + 
"(b('ndvi') <= 1182.5) ? " + 
"-0.004025083801439005" + 
":  " + 
"0.00016596417997170377" + 
":  " + 
"(b('dsvv') <= -0.9058661460876465) ? " + 
"0.018722184235000983" + 
":  " + 
"0.002355587635002974" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 840.5) ? " + 
"(b('lat') <= -35.01868438720703) ? " + 
"(b('L8b1') <= 359.0) ? " + 
"-0.002592756385530842" + 
":  " + 
"-0.04227564845812662" + 
":  " + 
"(b('L8b3med') <= 964.5) ? " + 
"-0.0014169143726765945" + 
":  " + 
"0.004928538708240326" + 
":  " + 
"(b('L8b4') <= 876.0) ? " + 
"(b('L8b2') <= 439.0) ? " + 
"-0.006542416858840235" + 
":  " + 
"0.0227873432334918" + 
":  " + 
"(b('L8b3') <= 843.5) ? " + 
"0.0320592397845276" + 
":  " + 
"-0.00010140647811249165" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5278.5) ? " + 
"(b('ndvi') <= 5169.5) ? " + 
"(b('L8b5') <= 3904.0) ? " + 
"0.00022937996201895277" + 
":  " + 
"-0.007069294474399384" + 
":  " + 
"(b('bulk') <= 144.0) ? " + 
"0.0030228420781014376" + 
":  " + 
"0.12192922204456044" + 
":  " + 
"(b('L8b11') <= 1364.5) ? " + 
"(b('L8b2') <= 454.0) ? " + 
"-0.02181021803708113" + 
":  " + 
"-0.0713626128990549" + 
":  " + 
"(b('L8b4') <= 866.5) ? " + 
"0.006594894972421491" + 
":  " + 
"-0.009404891766308973" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 3244.5) ? " + 
"(b('L8b11') <= 3352.25) ? " + 
"(b('L8b6') <= 3892.5) ? " + 
"0.0001975313631742237" + 
":  " + 
"-0.003998960606058537" + 
":  " + 
"(b('L8b2') <= 792.5) ? " + 
"-0.09585675409147064" + 
":  " + 
"-0.022086006876647885" + 
":  " + 
"(b('L8b3') <= 1271.5) ? " + 
"(b('crop') <= 70.19128227233887) ? " + 
"-0.01670213363665008" + 
":  " + 
"-0.09993117956209745" + 
":  " + 
"(b('L8b4med') <= 1806.0) ? " + 
"0.016698569320786418" + 
":  " + 
"0.0008343903098551479" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('dgvv') <= -1.103938102722168) ? " + 
"(b('dgvv') <= -2.3224611282348633) ? " + 
"0.0037199387664392353" + 
":  " + 
"-0.015062807219580587" + 
":  " + 
"(b('L8b4') <= 1599.0) ? " + 
"0.009541186386373078" + 
":  " + 
"0.0571683017727244" + 
":  " + 
"(b('lat') <= -35.01868438720703) ? " + 
"(b('L8b2') <= 1042.5) ? " + 
"-0.009615117331363079" + 
":  " + 
"0.07077380476502321" + 
":  " + 
"(b('dsvv') <= 4.98840856552124) ? " + 
"-1.3419983275386187e-05" + 
":  " + 
"0.01177211338637431" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 1598.5) ? " + 
"(b('L8b2') <= 543.0) ? " + 
"(b('L8b1') <= 440.0) ? " + 
"-0.0009245718837169946" + 
":  " + 
"0.023383640379944868" + 
":  " + 
"(b('crop') <= 26.773255348205566) ? " + 
"0.014625625818058057" + 
":  " + 
"-0.02569291643438967" + 
":  " + 
"(b('L8b7') <= 1624.5) ? " + 
"(b('bulk') <= 112.0) ? " + 
"-0.051063022807491434" + 
":  " + 
"0.02202688021838623" + 
":  " + 
"(b('lat') <= 56.0489501953125) ? " + 
"0.0001939274121536083" + 
":  " + 
"-0.09595717733692842" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 872.5) ? " + 
"(b('L8b3') <= 860.5) ? " + 
"(b('L8b3') <= 856.5) ? " + 
"-0.0007241570200945146" + 
":  " + 
"0.020476139394437872" + 
":  " + 
"(b('crop') <= 34.502431869506836) ? " + 
"0.00617724618778173" + 
":  " + 
"-0.02438385316107088" + 
":  " + 
"(b('L8b7') <= 1371.5) ? " + 
"(b('ndvi') <= 6162.0) ? " + 
"0.012620668826673714" + 
":  " + 
"0.07318442642408954" + 
":  " + 
"(b('L8b7') <= 1524.5) ? " + 
"-0.013784269459888266" + 
":  " + 
"0.0005088155160347207" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 4009.0) ? " + 
"(b('ndvi') <= 3942.5) ? " + 
"(b('lat') <= 50.95975112915039) ? " + 
"-0.0005840151562827563" + 
":  " + 
"0.006248674452354219" + 
":  " + 
"(b('L8b11') <= 1414.25) ? " + 
"-0.052667334699841535" + 
":  " + 
"0.0020955427078663265" + 
":  " + 
"(b('ndvi') <= 4089.5) ? " + 
"(b('sand') <= 36.0) ? " + 
"0.04057258729766788" + 
":  " + 
"0.00837771921254529" + 
":  " + 
"(b('bulk') <= 135.5) ? " + 
"-0.0032483915643702925" + 
":  " + 
"0.006996903608559193" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('sand') <= 31.5) ? " + 
"(b('lon') <= 26.368294715881348) ? " + 
"0.01180966200443372" + 
":  " + 
"-0.029528614462992382" + 
":  " + 
"(b('bulk') <= 126.5) ? " + 
"0.006757754249311658" + 
":  " + 
"-0.00867119559091738" + 
":  " + 
"(b('L8b7') <= 1013.5) ? " + 
"(b('L8b2') <= 310.5) ? " + 
"-0.03796305915825159" + 
":  " + 
"0.034242757883254905" + 
":  " + 
"(b('L8b3') <= 671.5) ? " + 
"0.019362069149403444" + 
":  " + 
"-1.4495519123644109e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 1325.5) ? " + 
"(b('L8b3') <= 865.5) ? " + 
"(b('L8b6') <= 2248.5) ? " + 
"-0.0007356983773795092" + 
":  " + 
"-0.017643186664132667" + 
":  " + 
"(b('L8b3med') <= 933.0) ? " + 
"0.04062794186901786" + 
":  " + 
"0.006036315371465248" + 
":  " + 
"(b('L8b6') <= 1850.5) ? " + 
"(b('ndvi') <= 2337.5) ? " + 
"-0.0005906597993016642" + 
":  " + 
"0.07758986075387518" + 
":  " + 
"(b('L8b4') <= 744.5) ? " + 
"0.004899959142350907" + 
":  " + 
"-0.00027754723164000265" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3385997.0) ? " + 
"(b('L8b3') <= 1892.5) ? " + 
"(b('L8b11') <= 3352.25) ? " + 
"-0.00022851832213323123" + 
":  " + 
"-0.017722304690827157" + 
":  " + 
"(b('L8b3') <= 1937.5) ? " + 
"0.0162404019116294" + 
":  " + 
"0.00226444241866369" + 
":  " + 
"(b('clay') <= 34.5) ? " + 
"(b('lat') <= 37.94038963317871) ? " + 
"-0.03246882512789486" + 
":  " + 
"0.004736483950567333" + 
":  " + 
"-0.13015378191760857" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 5456.5) ? " + 
"(b('L8b7') <= 3048.5) ? " + 
"(b('L8b11') <= 3352.25) ? " + 
"-0.00020868420558347106" + 
":  " + 
"-0.04402343768934548" + 
":  " + 
"(b('L8b7') <= 3050.5) ? " + 
"0.06189532201041939" + 
":  " + 
"0.0016091016633477439" + 
":  " + 
"(b('dsvh') <= -8.415994644165039) ? " + 
"(b('dgvv') <= -0.07757377624511719) ? " + 
"-0.024349617595081207" + 
":  " + 
"-0.006872825326292228" + 
":  " + 
"(b('gvv') <= -12.140446186065674) ? " + 
"-0.04884259337385005" + 
":  " + 
"-0.03785867493289777" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -1.9995975494384766) ? " + 
"(b('L8b6med') <= 2129.75) ? " + 
"(b('dgvv') <= -2.2381744384765625) ? " + 
"-0.0384793185471718" + 
":  " + 
"-0.08632510513160344" + 
":  " + 
"(b('lon') <= -108.81814956665039) ? " + 
"0.01278647016647581" + 
":  " + 
"-0.003183485342320637" + 
":  " + 
"(b('dgvv') <= -2.102396011352539) ? " + 
"0.1542440094608633" + 
":  " + 
"(b('sand') <= 28.5) ? " + 
"-0.002848722170803868" + 
":  " + 
"0.000510752062766326" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 727.5) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"(b('dgvv') <= -1.3354649543762207) ? " + 
"-0.010979359938178853" + 
":  " + 
"0.0010042947815928711" + 
":  " + 
"(b('ndvi') <= 3377.0) ? " + 
"-0.034743391380481714" + 
":  " + 
"-0.0035399203614501443" + 
":  " + 
"(b('L8b4') <= 697.5) ? " + 
"(b('L8b4') <= 686.5) ? " + 
"0.004675569055716238" + 
":  " + 
"0.03884961688631301" + 
":  " + 
"(b('L8b3') <= 743.5) ? " + 
"0.014670191490264892" + 
":  " + 
"-0.0001855993469270588" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.41945409774780273) ? " + 
"(b('ndvi') <= 3854.5) ? " + 
"(b('ndvi') <= 3739.0) ? " + 
"7.936228781099432e-05" + 
":  " + 
"-0.01975196278838331" + 
":  " + 
"(b('ndvi') <= 3943.0) ? " + 
"0.033334188181744835" + 
":  " + 
"0.004060905811272314" + 
":  " + 
"(b('ndvi_med') <= 5680.5) ? " + 
"(b('crop') <= 49.023324966430664) ? " + 
"0.002332696470525603" + 
":  " + 
"-0.0037566612785754094" + 
":  " + 
"(b('L8b6') <= 2395.0) ? " + 
"-0.005247212082220662" + 
":  " + 
"-0.07124642532593857" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2026.5) ? " + 
"(b('L8b6') <= 2852.5) ? " + 
"(b('L8b11') <= 2861.0) ? " + 
"0.0004408956341600234" + 
":  " + 
"-0.018059334371750224" + 
":  " + 
"(b('lat') <= 55.97825050354004) ? " + 
"-0.009289978516494062" + 
":  " + 
"0.06571691102155344" + 
":  " + 
"(b('L8b4') <= 1274.5) ? " + 
"(b('L8b2') <= 636.5) ? " + 
"-0.0009991166108362802" + 
":  " + 
"0.011731142109804867" + 
":  " + 
"(b('L8b4') <= 1286.5) ? " + 
"-0.03281426774514895" + 
":  " + 
"-0.0004237114050975232" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4med') <= 1444.75) ? " + 
"(b('L8b1') <= 816.5) ? " + 
"(b('L8b4') <= 1274.5) ? " + 
"6.55625620079668e-05" + 
":  " + 
"-0.003936424701385733" + 
":  " + 
"(b('L8b2') <= 1139.0) ? " + 
"0.031424176441244074" + 
":  " + 
"-0.01734157098446846" + 
":  " + 
"(b('L8b5') <= 2903.5) ? " + 
"(b('L8b4') <= 1545.0) ? " + 
"0.00944169281280804" + 
":  " + 
"-0.0005830285924679471" + 
":  " + 
"(b('dsvv') <= 1.814626932144165) ? " + 
"3.582831607074518e-05" + 
":  " + 
"-0.010845829674161808" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 872.5) ? " + 
"(b('L8b4') <= 919.5) ? " + 
"(b('L8b7') <= 1439.5) ? " + 
"-0.002377579001016059" + 
":  " + 
"0.0030275119469403604" + 
":  " + 
"(b('L8b7') <= 1761.0) ? " + 
"-0.013140226793885702" + 
":  " + 
"0.000603913319059975" + 
":  " + 
"(b('L8b4') <= 1134.5) ? " + 
"(b('ndvi_med') <= 1884.5) ? " + 
"0.024114998639694168" + 
":  " + 
"0.0027223283356543073" + 
":  " + 
"(b('L8b5') <= 2208.5) ? " + 
"-0.006954570289743048" + 
":  " + 
"0.00044187464702228333" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.59345054626465) ? " + 
"(b('dsvv') <= -0.9803581237792969) ? " + 
"(b('moss') <= 12.665012836456299) ? " + 
"0.0010854285394186261" + 
":  " + 
"0.01163099962527014" + 
":  " + 
"(b('dsvh') <= -5.541437149047852) ? " + 
"-0.0013182925947223434" + 
":  " + 
"0.0033648627014159125" + 
":  " + 
"(b('dsvh') <= -1.5241951942443848) ? " + 
"(b('dgvv') <= -1.0063838958740234) ? " + 
"-0.0046308280783735" + 
":  " + 
"0.00042863420255104446" + 
":  " + 
"(b('L8dt') <= 2360298.5) ? " + 
"-0.06205163761183527" + 
":  " + 
"-0.00033362918305254903" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6342931.5) ? " + 
"(b('L8b2') <= 316.5) ? " + 
"(b('L8b1') <= 259.0) ? " + 
"0.0026857448584594974" + 
":  " + 
"0.045297960714036856" + 
":  " + 
"(b('L8b3') <= 562.5) ? " + 
"-0.016020715551563508" + 
":  " + 
"-1.1998772584148413e-05" + 
":  " + 
"(b('L8b6med') <= 2382.5) ? " + 
"(b('L8dt') <= 11081765.0) ? " + 
"-0.0031779098238005265" + 
":  " + 
"-0.015027275155814646" + 
":  " + 
"(b('crop') <= 80.92045593261719) ? " + 
"0.009435331855296209" + 
":  " + 
"0.033119567053834974" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 6114.5) ? " + 
"(b('ndvi') <= 6025.0) ? " + 
"(b('ndvi_med') <= 6045.25) ? " + 
"9.03432681082556e-06" + 
":  " + 
"0.052765743140878084" + 
":  " + 
"(b('dgvh') <= -7.935764789581299) ? " + 
"0.0052609633129384915" + 
":  " + 
"0.08144573604344857" + 
":  " + 
"(b('clay') <= 22.0) ? " + 
"(b('ndvi') <= 6780.5) ? " + 
"-0.021862369643230815" + 
":  " + 
"0.0034746137953850266" + 
":  " + 
"(b('dsvh') <= -5.716547966003418) ? " + 
"-0.003376971794823927" + 
":  " + 
"0.048047325636771394" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 50288.5) ? " + 
"(b('dsvh') <= -7.044209957122803) ? " + 
"(b('ndvi') <= 5166.5) ? " + 
"0.0013456961279292926" + 
":  " + 
"0.11874476260078316" + 
":  " + 
"(b('ndvi') <= 2305.0) ? " + 
"-0.015704183485538217" + 
":  " + 
"0.00042404098554542146" + 
":  " + 
"(b('L8dt') <= 70515.5) ? " + 
"(b('L8dt') <= 70338.5) ? " + 
"0.0038531241411358013" + 
":  " + 
"0.042047843308350305" + 
":  " + 
"(b('clay') <= 33.5) ? " + 
"0.00016982957226531045" + 
":  " + 
"-0.0056678276309792145" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5278.5) ? " + 
"(b('ndvi') <= 5169.5) ? " + 
"(b('L8b5') <= 3904.0) ? " + 
"0.00019950793738760547" + 
":  " + 
"-0.005974757282120029" + 
":  " + 
"(b('lat') <= 41.38369941711426) ? " + 
"0.10898942957079481" + 
":  " + 
"0.002928898671198291" + 
":  " + 
"(b('L8b11') <= 1364.5) ? " + 
"(b('L8b5') <= 2917.0) ? " + 
"-0.05132120171401402" + 
":  " + 
"-0.009610230046165628" + 
":  " + 
"(b('crop') <= 39.885589599609375) ? " + 
"0.024295918871954193" + 
":  " + 
"-0.003284725767763659" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 7.336734771728516) ? " + 
"(b('moss') <= 5.812525033950806) ? " + 
"(b('L8b7') <= 1524.5) ? " + 
"-0.00428904989049183" + 
":  " + 
"0.0009111647042614529" + 
":  " + 
"(b('L8b7') <= 1685.0) ? " + 
"0.018572697485522503" + 
":  " + 
"0.0001056363207574717" + 
":  " + 
"(b('moss') <= 9.457935333251953) ? " + 
"(b('L8b1') <= 701.0) ? " + 
"-0.0018991739829698263" + 
":  " + 
"-0.016778282800482547" + 
":  " + 
"(b('L8b7') <= 2004.0) ? " + 
"-0.0019310271662907569" + 
":  " + 
"0.0024107211804683354" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 236044.5) ? " + 
"(b('dgvv') <= 1.2423334121704102) ? " + 
"(b('dgvv') <= 1.2354412078857422) ? " + 
"1.4491595867812747e-05" + 
":  " + 
"0.11789196019607959" + 
":  " + 
"(b('dgvv') <= 2.873173713684082) ? " + 
"-0.012909659867125571" + 
":  " + 
"0.0031298450488820287" + 
":  " + 
"(b('L8dt') <= 236051.5) ? " + 
"(b('L8dt') <= 236050.5) ? " + 
"0.008723013089830218" + 
":  " + 
"0.08293983924592342" + 
":  " + 
"(b('lat') <= 38.48287391662598) ? " + 
"-0.0022708617799044074" + 
":  " + 
"0.0008550700783368843" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 7.796026229858398) ? " + 
"(b('gvv') <= -6.216152667999268) ? " + 
"(b('gvv') <= -6.294252157211304) ? " + 
"3.815402668641181e-05" + 
":  " + 
"0.04047050741605767" + 
":  " + 
"(b('L8b3med') <= 792.0) ? " + 
"-0.0176635499799347" + 
":  " + 
"0.001011170797846962" + 
":  " + 
"(b('L8b5') <= 1601.0) ? " + 
"0.043589977021826515" + 
":  " + 
"0.06245820444745878" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 612.5) ? " + 
"(b('L8b4') <= 606.5) ? " + 
"(b('L8b5') <= 3061.0) ? " + 
"0.004541770977334212" + 
":  " + 
"-0.01850410021269573" + 
":  " + 
"(b('dsvv') <= 1.5556316375732422) ? " + 
"0.011315715823477701" + 
":  " + 
"0.07261592887050194" + 
":  " + 
"(b('L8b4') <= 634.5) ? " + 
"(b('sand') <= 78.5) ? " + 
"-0.004680956221783248" + 
":  " + 
"-0.08518273176905243" + 
":  " + 
"(b('L8b4') <= 638.5) ? " + 
"0.024249778274342628" + 
":  " + 
"-3.695561553792907e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -6.715389013290405) ? " + 
"(b('L8b1') <= 628.5) ? " + 
"(b('L8b5') <= 2879.0) ? " + 
"-0.003553491464114834" + 
":  " + 
"-0.02399090444221534" + 
":  " + 
"(b('L8dt') <= 1232137.0) ? " + 
"-0.06527284660061805" + 
":  " + 
"-0.0693228481026551" + 
":  " + 
"(b('lat') <= 52.296464920043945) ? " + 
"(b('dgvh') <= -11.592209815979004) ? " + 
"-0.024710062061544816" + 
":  " + 
"-0.00014947130254266175" + 
":  " + 
"(b('ndvi') <= 2731.5) ? " + 
"0.02961632065914317" + 
":  " + 
"-0.000963449293830724" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b4') <= 2046.5) ? " + 
"(b('L8b3') <= 1527.5) ? " + 
"-0.00054297557513549" + 
":  " + 
"0.01587376262242779" + 
":  " + 
"(b('L8b6med') <= 3370.0) ? " + 
"-0.002303586896113316" + 
":  " + 
"-0.03595270847931961" + 
":  " + 
"(b('ndvi') <= 2866.5) ? " + 
"(b('L8dt') <= 16540.0) ? " + 
"0.11089661865141306" + 
":  " + 
"0.00023462547790534607" + 
":  " + 
"(b('ndvi_med') <= 1615.5) ? " + 
"0.01961875622803001" + 
":  " + 
"-0.0016116901815485575" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2561.0) ? " + 
"(b('L8b2') <= 817.5) ? " + 
"(b('L8b11') <= 3352.25) ? " + 
"0.00015040570178136056" + 
":  " + 
"-0.07009584085318046" + 
":  " + 
"(b('L8b7') <= 2352.0) ? " + 
"0.004191254391758082" + 
":  " + 
"-0.011583656067353978" + 
":  " + 
"(b('dgvh') <= -2.990079879760742) ? " + 
"(b('L8b7') <= 2571.5) ? " + 
"0.02228801496110175" + 
":  " + 
"0.0004698754897548187" + 
":  " + 
"(b('dsvh') <= -2.5628719329833984) ? " + 
"0.07537860601170909" + 
":  " + 
"-0.004848305271382078" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1314.5) ? " + 
"(b('dgvv') <= 4.6177449226379395) ? " + 
"(b('bulk') <= 131.5) ? " + 
"-0.018317786903600145" + 
":  " + 
"-0.006373489298673463" + 
":  " + 
"(b('clay') <= 13.5) ? " + 
"-0.03458789784696728" + 
":  " + 
"-0.045167651242826484" + 
":  " + 
"(b('L8b5') <= 1430.0) ? " + 
"(b('dsvh') <= -5.535567760467529) ? " + 
"0.024213507073085852" + 
":  " + 
"-0.029090844816950748" + 
":  " + 
"(b('L8dt') <= 3369578.0) ? " + 
"-0.00020861654094842156" + 
":  " + 
"0.004096058116338659" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 840.5) ? " + 
"(b('lat') <= -35.07992362976074) ? " + 
"(b('L8b1') <= 359.0) ? " + 
"0.0005708084913649084" + 
":  " + 
"-0.04477649054935151" + 
":  " + 
"(b('L8b7') <= 2997.0) ? " + 
"-0.0007716168094790571" + 
":  " + 
"0.031184997877817595" + 
":  " + 
"(b('L8b3') <= 843.5) ? " + 
"(b('sand') <= 24.0) ? " + 
"0.10434985501552857" + 
":  " + 
"0.009046221359686019" + 
":  " + 
"(b('L8b4') <= 943.5) ? " + 
"0.008331101388747703" + 
":  " + 
"-0.0001504530773680409" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3381.5) ? " + 
"(b('L8b5') <= 3318.0) ? " + 
"(b('L8b4') <= 2020.5) ? " + 
"0.0005333095029755467" + 
":  " + 
"-0.00501558584381137" + 
":  " + 
"(b('L8b5') <= 3321.5) ? " + 
"0.08475872539540627" + 
":  " + 
"0.008783026276567558" + 
":  " + 
"(b('bulk') <= 165.5) ? " + 
"(b('L8b3') <= 1465.5) ? " + 
"-0.004637236680940452" + 
":  " + 
"0.0038435456924408775" + 
":  " + 
"(b('dsvv') <= -0.5800786018371582) ? " + 
"0.10024249503334148" + 
":  " + 
"0.1584258463535793" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 41.365474700927734) ? " + 
"(b('L8b5') <= 2928.5) ? " + 
"(b('lat') <= 39.927019119262695) ? " + 
"-0.0004411098121783824" + 
":  " + 
"0.010576445295388455" + 
":  " + 
"(b('L8b7') <= 2953.5) ? " + 
"-0.006483989293167474" + 
":  " + 
"0.0018858008065263689" + 
":  " + 
"(b('L8b5') <= 2794.5) ? " + 
"(b('dgvv') <= -0.9883632659912109) ? " + 
"-0.008650057456405468" + 
":  " + 
"-0.0005462733370934844" + 
":  " + 
"(b('L8b6med') <= 2023.0) ? " + 
"-0.03967483202504613" + 
":  " + 
"0.0017849993222836995" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.41945409774780273) ? " + 
"(b('dgvh') <= -3.971261501312256) ? " + 
"(b('L8b5') <= 2794.5) ? " + 
"-0.0010563877167711346" + 
":  " + 
"0.0021393117514676885" + 
":  " + 
"(b('dgvv') <= -0.40035486221313477) ? " + 
"-0.019602241000015286" + 
":  " + 
"0.025410404925432253" + 
":  " + 
"(b('ndvi_med') <= 5680.5) ? " + 
"(b('crop') <= 49.023324966430664) ? " + 
"0.0019974987342686193" + 
":  " + 
"-0.003461708905432739" + 
":  " + 
"(b('dsvv') <= 1.5580627918243408) ? " + 
"-0.07134777093024817" + 
":  " + 
"-0.01848141248593947" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('dsvv') <= 5.168562412261963) ? " + 
"(b('dgvh') <= -1.5524482727050781) ? " + 
"0.005023429210007579" + 
":  " + 
"0.07269597517671363" + 
":  " + 
"-0.10124750287346776" + 
":  " + 
"(b('lat') <= -35.01868438720703) ? " + 
"(b('L8b2') <= 1042.5) ? " + 
"-0.007864357341669705" + 
":  " + 
"0.06391050157028678" + 
":  " + 
"(b('dgvv') <= 5.326527118682861) ? " + 
"-1.8030788409700584e-05" + 
":  " + 
"0.013382138701292274" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 5456.5) ? " + 
"(b('L8b3') <= 1898.5) ? " + 
"(b('L8b11') <= 3352.25) ? " + 
"-3.5174950126847654e-05" + 
":  " + 
"-0.014590853231171394" + 
":  " + 
"(b('L8b1') <= 885.0) ? " + 
"0.04017012413936316" + 
":  " + 
"0.0027607507301938847" + 
":  " + 
"(b('dsvh') <= -8.415994644165039) ? " + 
"(b('gvv') <= -10.849943161010742) ? " + 
"-0.02220127080421096" + 
":  " + 
"-0.006500177045049849" + 
":  " + 
"(b('lat') <= 41.32942008972168) ? " + 
"-0.034387441690994835" + 
":  " + 
"-0.044419202404594814" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3189.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"(b('L8b5') <= 3187.5) ? " + 
"0.00012675013690187484" + 
":  " + 
"0.02217548173019282" + 
":  " + 
"(b('L8b3') <= 731.0) ? " + 
"-0.01615372306428133" + 
":  " + 
"0.04193090351293399" + 
":  " + 
"(b('L8b3') <= 762.0) ? " + 
"(b('L8dt') <= 1771255.5) ? " + 
"-0.01596921594835032" + 
":  " + 
"0.013041755961078757" + 
":  " + 
"(b('L8b7') <= 1398.5) ? " + 
"0.009820657334525817" + 
":  " + 
"-0.001473254438769621" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 697.5) ? " + 
"(b('L8b3') <= 759.5) ? " + 
"(b('crop') <= 54.728538513183594) ? " + 
"0.004011135276553679" + 
":  " + 
"-0.005794430447461568" + 
":  " + 
"(b('L8b5') <= 3744.5) ? " + 
"0.022089785647861314" + 
":  " + 
"-0.07441227605424461" + 
":  " + 
"(b('L8b1') <= 255.5) ? " + 
"(b('moss') <= 13.848764896392822) ? " + 
"-0.007677949538752126" + 
":  " + 
"-0.06155721757254581" + 
":  " + 
"(b('L8b3med') <= 565.0) ? " + 
"0.028642381117387858" + 
":  " + 
"-9.407676028021542e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2026.5) ? " + 
"(b('L8b7') <= 2016.5) ? " + 
"(b('L8b11') <= 2889.25) ? " + 
"-0.0001185320810726981" + 
":  " + 
"-0.01993174301533443" + 
":  " + 
"(b('L8dt') <= 3692641.0) ? " + 
"-0.02994729994038537" + 
":  " + 
"0.005385567916150317" + 
":  " + 
"(b('L8b7') <= 2066.5) ? " + 
"(b('sand') <= 33.5) ? " + 
"0.04390066394521066" + 
":  " + 
"0.0074137112622328" + 
":  " + 
"(b('L8b6med') <= 2395.5) ? " + 
"0.015750651512959877" + 
":  " + 
"-0.00020986309547693204" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -9.149760723114014) ? " + 
"(b('moss') <= 12.958944320678711) ? " + 
"(b('crop') <= 76.58172988891602) ? " + 
"-0.009378481643372537" + 
":  " + 
"0.0008614786782431633" + 
":  " + 
"(b('L8b5') <= 1802.5) ? " + 
"-0.10962255430185935" + 
":  " + 
"0.010569857116338179" + 
":  " + 
"(b('moss') <= 7.336734771728516) ? " + 
"(b('moss') <= 5.812525033950806) ? " + 
"0.0005719518619953121" + 
":  " + 
"0.00788764141323041" + 
":  " + 
"(b('gvv') <= -15.784631252288818) ? " + 
"-0.008117500280052049" + 
":  " + 
"-0.0004452553173508574" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.41945409774780273) ? " + 
"(b('dgvh') <= -4.466362953186035) ? " + 
"(b('sand') <= 24.0) ? " + 
"-0.0068236930116138345" + 
":  " + 
"0.0005533896663445571" + 
":  " + 
"(b('L8dt') <= 21260.0) ? " + 
"0.0812140963856134" + 
":  " + 
"0.009761316236108337" + 
":  " + 
"(b('ndvi_med') <= 5680.5) ? " + 
"(b('crop') <= 49.023324966430664) ? " + 
"0.0016682008518288786" + 
":  " + 
"-0.003061146194251947" + 
":  " + 
"(b('dsvh') <= -6.249026298522949) ? " + 
"-0.0019090458280779446" + 
":  " + 
"-0.05720324362366788" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -8.796432495117188) ? " + 
"(b('gvv') <= -8.863539218902588) ? " + 
"(b('gvv') <= -8.869343757629395) ? " + 
"-0.00014921227141285342" + 
":  " + 
"0.09806077695173991" + 
":  " + 
"(b('L8b6') <= 1654.5) ? " + 
"0.05078058766468046" + 
":  " + 
"-0.021896453515260136" + 
":  " + 
"(b('ndvi') <= 4632.5) ? " + 
"(b('L8b11') <= 2924.75) ? " + 
"0.006143699085460226" + 
":  " + 
"-0.015309108248541758" + 
":  " + 
"(b('clay') <= 27.5) ? " + 
"-0.005196816919422759" + 
":  " + 
"-0.047450616092366185" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4med') <= 1444.75) ? " + 
"(b('L8b7') <= 2941.5) ? " + 
"(b('dsvh') <= -0.03885698318481445) ? " + 
"-0.0008303218023044881" + 
":  " + 
"0.05067426613857684" + 
":  " + 
"(b('L8b1') <= 537.5) ? " + 
"-0.033393846391994886" + 
":  " + 
"0.015611119719022891" + 
":  " + 
"(b('L8b5') <= 2903.5) ? " + 
"(b('L8b4') <= 1545.0) ? " + 
"0.008525928960432578" + 
":  " + 
"-0.0006641696370402846" + 
":  " + 
"(b('L8b3') <= 1314.0) ? " + 
"-0.006554701181393435" + 
":  " + 
"0.000692271490368154" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.472105026245117) ? " + 
"(b('L8b6') <= 3629.5) ? " + 
"(b('L8b7') <= 2026.5) ? " + 
"-0.0030692334401369553" + 
":  " + 
"0.0026749419525261206" + 
":  " + 
"(b('lat') <= 41.77997970581055) ? " + 
"-0.0032274961997753064" + 
":  " + 
"-0.03626636821583997" + 
":  " + 
"(b('dgvv') <= 0.7545242309570312) ? " + 
"(b('dsvh') <= -4.162288665771484) ? " + 
"0.0010997741240027256" + 
":  " + 
"0.0216383471921719" + 
":  " + 
"(b('L8b11') <= 2904.5) ? " + 
"-0.00026937653611479507" + 
":  " + 
"-0.014498965960990042" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b6') <= 4607.5) ? " + 
"(b('L8b7') <= 3309.5) ? " + 
"-0.0005139382863059216" + 
":  " + 
"0.028413749927715445" + 
":  " + 
"(b('dgvv') <= 3.098926067352295) ? " + 
"-0.01830576404569262" + 
":  " + 
"-0.08847190738492883" + 
":  " + 
"(b('L8b4') <= 757.0) ? " + 
"(b('L8b2') <= 386.0) ? " + 
"0.0021984529682089866" + 
":  " + 
"0.04477446936921222" + 
":  " + 
"(b('L8b3') <= 867.5) ? " + 
"-0.006758661109737267" + 
":  " + 
"0.0013005148197051404" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -6.711760997772217) ? " + 
"(b('ndvi') <= 3271.0) ? " + 
"(b('dsvv') <= -7.361246109008789) ? " + 
"-0.06219513076885139" + 
":  " + 
"-0.05855012941701804" + 
":  " + 
"(b('L8b6') <= 2794.0) ? " + 
"0.0014720954556963102" + 
":  " + 
"-0.018552379882662333" + 
":  " + 
"(b('ndvi') <= 1620.0) ? " + 
"(b('lon') <= 146.95569610595703) ? " + 
"-0.001093193812167531" + 
":  " + 
"0.043799749283745956" + 
":  " + 
"(b('ndvi_med') <= 1273.75) ? " + 
"0.03042826584882312" + 
":  " + 
"0.0003389082351149041" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4762.5) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4348.5) ? " + 
"2.2594809276083217e-05" + 
":  " + 
"0.05061735204529402" + 
":  " + 
"(b('dgvv') <= 0.5547199249267578) ? " + 
"-0.00028826067809462524" + 
":  " + 
"-0.023012905123744373" + 
":  " + 
"(b('ndvi') <= 5903.5) ? " + 
"(b('ndvi') <= 1986.5) ? " + 
"-0.00015762602771170892" + 
":  " + 
"0.06528681021623645" + 
":  " + 
"(b('gvv') <= -14.421696662902832) ? " + 
"0.008101363400350134" + 
":  " + 
"-0.02094044160713801" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 35512.5) ? " + 
"(b('bulk') <= 134.5) ? " + 
"(b('dgvv') <= 1.388923168182373) ? " + 
"0.010412912872686485" + 
":  " + 
"-0.019826297611786094" + 
":  " + 
"(b('L8b3') <= 804.0) ? " + 
"-0.02960256504550755" + 
":  " + 
"-0.004199118349135055" + 
":  " + 
"(b('gvv') <= -8.514279842376709) ? " + 
"(b('gvv') <= -8.635880470275879) ? " + 
"1.3360922775551872e-05" + 
":  " + 
"-0.015296291389189648" + 
":  " + 
"(b('ndvi_med') <= 3118.5) ? " + 
"0.006838757022086621" + 
":  " + 
"-0.0038897872980762794" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 38.5) ? " + 
"(b('L8b2') <= 314.5) ? " + 
"(b('L8b2') <= 267.5) ? " + 
"-0.004578516744628821" + 
":  " + 
"0.009977005998463564" + 
":  " + 
"(b('L8b4') <= 534.5) ? " + 
"-0.02561317351912568" + 
":  " + 
"8.094998866824391e-06" + 
":  " + 
"(b('dsvv') <= 0.3476085662841797) ? " + 
"(b('L8b4') <= 1354.5) ? " + 
"0.009918698106557693" + 
":  " + 
"-0.02885200144886226" + 
":  " + 
"(b('L8b1') <= 682.5) ? " + 
"-0.02819691678101254" + 
":  " + 
"-0.10210985938022965" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2043.5) ? " + 
"(b('L8b3med') <= 1316.75) ? " + 
"(b('crop') <= 97.10931015014648) ? " + 
"0.0040682154379217345" + 
":  " + 
"-0.03446876837513763" + 
":  " + 
"(b('clay') <= 19.0) ? " + 
"-0.08577166800955925" + 
":  " + 
"-0.01436844405715905" + 
":  " + 
"(b('L8b5') <= 2068.5) ? " + 
"(b('L8b6med') <= 3715.5) ? " + 
"-0.015730761439765845" + 
":  " + 
"0.07668209902839737" + 
":  " + 
"(b('L8b3') <= 727.5) ? " + 
"-0.0033345730186470665" + 
":  " + 
"0.0003657109787445248" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 464.5) ? " + 
"(b('L8b1') <= 66.0) ? " + 
"(b('L8dt') <= 281736.0) ? " + 
"-0.020669138710779626" + 
":  " + 
"0.028322595982350623" + 
":  " + 
"(b('gvv') <= -10.424904823303223) ? " + 
"-0.017321129557200554" + 
":  " + 
"0.010746498342992617" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"(b('L8b3med') <= 564.0) ? " + 
"0.044771483158362414" + 
":  " + 
"0.003408255627385142" + 
":  " + 
"(b('L8b4') <= 535.0) ? " + 
"-0.02282050629233556" + 
":  " + 
"-3.4542430747847936e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 612.5) ? " + 
"(b('gvv') <= -12.332101345062256) ? " + 
"(b('dsvh') <= -6.6433210372924805) ? " + 
"-0.005556442065668856" + 
":  " + 
"0.022038938799456165" + 
":  " + 
"(b('L8b6med') <= 2488.75) ? " + 
"0.0058470793420035815" + 
":  " + 
"-0.012854749942988167" + 
":  " + 
"(b('L8b4') <= 634.5) ? " + 
"(b('sand') <= 78.5) ? " + 
"-0.004401559503171212" + 
":  " + 
"-0.07446631675240752" + 
":  " + 
"(b('L8b4') <= 638.5) ? " + 
"0.021160472243470445" + 
":  " + 
"-3.024100186052143e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -11.414001941680908) ? " + 
"(b('dgvv') <= 1.7685985565185547) ? " + 
"(b('dgvh') <= -2.487959384918213) ? " + 
"-1.9394425965405843e-05" + 
":  " + 
"0.06123433195085621" + 
":  " + 
"(b('bulk') <= 152.5) ? " + 
"-0.006254565138785475" + 
":  " + 
"-0.036626550277492856" + 
":  " + 
"(b('L8b11') <= 3276.0) ? " + 
"(b('L8b1') <= 453.5) ? " + 
"-0.0013602255640455094" + 
":  " + 
"0.0036208586586150057" + 
":  " + 
"(b('dsvh') <= -6.261636734008789) ? " + 
"-0.003267453381179653" + 
":  " + 
"-0.024044743738728794" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 697.5) ? " + 
"(b('L8b3') <= 764.0) ? " + 
"(b('ndvi_med') <= 2860.5) ? " + 
"0.007005561551109386" + 
":  " + 
"-0.0024521945718134533" + 
":  " + 
"(b('L8b3') <= 822.0) ? " + 
"0.03001618781607525" + 
":  " + 
"-0.008351467120833334" + 
":  " + 
"(b('L8b1') <= 255.5) ? " + 
"(b('L8b1') <= 247.5) ? " + 
"-0.004917475120680705" + 
":  " + 
"-0.03381754072009575" + 
":  " + 
"(b('L8b3med') <= 565.0) ? " + 
"0.02629307635876812" + 
":  " + 
"-0.00010175806511181419" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 876.5) ? " + 
"(b('bulk') <= 141.0) ? " + 
"(b('dgvv') <= -0.29620981216430664) ? " + 
"-0.06587509475033168" + 
":  " + 
"-0.012964792758399684" + 
":  " + 
"(b('dgvh') <= -7.899949073791504) ? " + 
"0.0049749454883523106" + 
":  " + 
"-0.007978666072948646" + 
":  " + 
"(b('L8b3med') <= 1653.0) ? " + 
"(b('L8b4') <= 2063.0) ? " + 
"0.00023148340518949707" + 
":  " + 
"-0.0031445374572948233" + 
":  " + 
"(b('gvv') <= -9.249156951904297) ? " + 
"0.007758120862286349" + 
":  " + 
"0.07757448226856793" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b6') <= 2659.5) ? " + 
"(b('L8b6') <= 2561.5) ? " + 
"-0.0004884243458409992" + 
":  " + 
"0.0072975949829908555" + 
":  " + 
"(b('L8b6') <= 2699.5) ? " + 
"-0.01819239686279269" + 
":  " + 
"-0.0008027893284670967" + 
":  " + 
"(b('L8b5') <= 2456.5) ? " + 
"(b('L8b3') <= 1216.0) ? " + 
"0.002469284676285692" + 
":  " + 
"0.04215610187012664" + 
":  " + 
"(b('moss') <= 20.356952667236328) ? " + 
"-0.000363748188125918" + 
":  " + 
"0.024552805265575583" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -6.351504802703857) ? " + 
"(b('dsvv') <= 2.131354808807373) ? " + 
"(b('dgvv') <= 2.180492877960205) ? " + 
"-0.0002272944519235542" + 
":  " + 
"0.16273761640126613" + 
":  " + 
"(b('gvv') <= -13.87392807006836) ? " + 
"-0.12963553012910348" + 
":  " + 
"-0.008793494989781428" + 
":  " + 
"(b('dgvh') <= -6.346902847290039) ? " + 
"(b('crop') <= 54.60833549499512) ? " + 
"0.035142079959221" + 
":  " + 
"0.18190297295653512" + 
":  " + 
"(b('L8b11') <= 3276.0) ? " + 
"0.0010007795687645908" + 
":  " + 
"-0.011740814376175196" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 3244.5) ? " + 
"(b('L8b11') <= 3352.25) ? " + 
"(b('L8b6') <= 3892.5) ? " + 
"0.00016948015111382833" + 
":  " + 
"-0.0036015286146765676" + 
":  " + 
"(b('dgvv') <= 0.15166282653808594) ? " + 
"-0.0026982211544667777" + 
":  " + 
"-0.051875920754876716" + 
":  " + 
"(b('L8b7') <= 3255.5) ? " + 
"(b('L8b6') <= 4089.0) ? " + 
"0.04683777974323197" + 
":  " + 
"0.008565099889017226" + 
":  " + 
"(b('L8b3') <= 1271.5) ? " + 
"-0.02500308970727388" + 
":  " + 
"0.0023365705592529604" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2591.0) ? " + 
"(b('L8b2') <= 817.5) ? " + 
"(b('L8b2') <= 816.5) ? " + 
"1.6097696265809428e-05" + 
":  " + 
"0.10828218198739499" + 
":  " + 
"(b('lat') <= 35.84549903869629) ? " + 
"0.018954234461559995" + 
":  " + 
"-0.007148026249004247" + 
":  " + 
"(b('dgvh') <= -2.990079879760742) ? " + 
"(b('L8b6') <= 3693.5) ? " + 
"0.004211457991867473" + 
":  " + 
"-0.0012293850439247165" + 
":  " + 
"(b('dgvv') <= 1.4627165794372559) ? " + 
"0.18004612513210216" + 
":  " + 
"0.01923856121565122" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6342931.5) ? " + 
"(b('L8b4med') <= 1444.75) ? " + 
"(b('L8b5') <= 1802.5) ? " + 
"0.005397834134288993" + 
":  " + 
"-0.0009239119457678274" + 
":  " + 
"(b('L8b4') <= 1416.0) ? " + 
"0.004866155366183036" + 
":  " + 
"-0.00021017098587634107" + 
":  " + 
"(b('L8b6med') <= 2382.5) ? " + 
"(b('L8dt') <= 11081765.0) ? " + 
"-0.003798384382454866" + 
":  " + 
"-0.014960773154799788" + 
":  " + 
"(b('crop') <= 80.92045593261719) ? " + 
"0.009015339629310384" + 
":  " + 
"0.02942250789413058" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2147.5) ? " + 
"(b('ndvi') <= 2137.5) ? " + 
"(b('L8b11') <= 1394.25) ? " + 
"0.02921968130456367" + 
":  " + 
"-0.0006122143886167196" + 
":  " + 
"(b('lon') <= 147.47109985351562) ? " + 
"-0.01999789300498962" + 
":  " + 
"-0.1084390186939758" + 
":  " + 
"(b('ndvi_med') <= 2145.0) ? " + 
"(b('lon') <= -105.00619506835938) ? " + 
"0.016755788218415613" + 
":  " + 
"0.0006060279713077125" + 
":  " + 
"(b('L8b3') <= 1005.5) ? " + 
"-0.0013574868440092563" + 
":  " + 
"0.003558745585805607" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.472105026245117) ? " + 
"(b('ndvi') <= 5640.0) ? " + 
"(b('ndvi') <= 3024.0) ? " + 
"-0.001467888784083722" + 
":  " + 
"0.005963208148877248" + 
":  " + 
"(b('gvv') <= -10.522767543792725) ? " + 
"-0.02279137399852591" + 
":  " + 
"-0.06412450951795497" + 
":  " + 
"(b('dgvv') <= 0.7536702156066895) ? " + 
"(b('dsvh') <= -4.262305736541748) ? " + 
"0.0010518317039847692" + 
":  " + 
"0.01840012758371308" + 
":  " + 
"(b('L8b11') <= 2904.5) ? " + 
"-0.0003079325819903129" + 
":  " + 
"-0.012453345277504883" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2591.0) ? " + 
"(b('L8b5') <= 3385.5) ? " + 
"(b('ndvi_med') <= 4777.75) ? " + 
"-5.811324862265798e-05" + 
":  " + 
"0.01233814013540389" + 
":  " + 
"(b('L8b5') <= 3397.0) ? " + 
"-0.026421172127722107" + 
":  " + 
"-0.0026021229844997596" + 
":  " + 
"(b('dgvh') <= -2.990079879760742) ? " + 
"(b('L8b7') <= 2651.5) ? " + 
"0.008691945583630083" + 
":  " + 
"-1.5140283515418623e-06" + 
":  " + 
"(b('dsvh') <= -1.2266345024108887) ? " + 
"0.04691502444208223" + 
":  " + 
"-0.03348915282947529" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 3244.5) ? " + 
"(b('L8b11') <= 3352.25) ? " + 
"(b('dgvh') <= -9.149760723114014) ? " + 
"-0.0027185276991325597" + 
":  " + 
"0.00019261195077202895" + 
":  " + 
"(b('dsvv') <= 0.15221595764160156) ? " + 
"-0.0029978250362018826" + 
":  " + 
"-0.046858059922291535" + 
":  " + 
"(b('L8b7') <= 3296.5) ? " + 
"(b('L8b1') <= 675.5) ? " + 
"-0.009422616458678857" + 
":  " + 
"0.020243280775498883" + 
":  " + 
"(b('L8dt') <= 16561.5) ? " + 
"0.09072956492278503" + 
":  " + 
"0.0001807668662354988" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 103.0) ? " + 
"(b('L8dt') <= 50834.0) ? " + 
"(b('ndvi') <= 3067.0) ? " + 
"-0.04289469623769177" + 
":  " + 
"-0.0656929441346678" + 
":  " + 
"(b('gvv') <= -10.60936689376831) ? " + 
"-0.004536720788331787" + 
":  " + 
"-0.022673491562118855" + 
":  " + 
"(b('gvv') <= -11.414001941680908) ? " + 
"(b('dgvv') <= 1.7685985565185547) ? " + 
"1.8618893783496785e-05" + 
":  " + 
"-0.01194046720008163" + 
":  " + 
"(b('lon') <= -120.92649459838867) ? " + 
"-0.027535764921148384" + 
":  " + 
"0.0009834817478551812" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -6.216152667999268) ? " + 
"(b('gvv') <= -6.294252157211304) ? " + 
"(b('dgvv') <= 3.967639923095703) ? " + 
"-5.956745298785251e-05" + 
":  " + 
"0.006526117938421392" + 
":  " + 
"(b('dsvv') <= 4.663687467575073) ? " + 
"0.01679243360946428" + 
":  " + 
"0.11279249814814166" + 
":  " + 
"(b('L8b3med') <= 792.0) ? " + 
"(b('L8dt') <= 2419203.5) ? " + 
"-0.013104065382094755" + 
":  " + 
"-0.04791781326663012" + 
":  " + 
"(b('L8b11') <= 2902.5) ? " + 
"0.0049412120092264585" + 
":  " + 
"-0.02606341885534749" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6342931.5) ? " + 
"(b('L8b4med') <= 1521.5) ? " + 
"(b('L8b3') <= 1645.5) ? " + 
"-0.0006161725059477694" + 
":  " + 
"0.03146753710793934" + 
":  " + 
"(b('L8b4') <= 1445.5) ? " + 
"0.005661305307691281" + 
":  " + 
"-0.00025121357533696375" + 
":  " + 
"(b('L8b6med') <= 2382.5) ? " + 
"(b('L8dt') <= 11600114.0) ? " + 
"-0.004531405736896543" + 
":  " + 
"-0.017588636076905667" + 
":  " + 
"(b('L8b4') <= 1940.0) ? " + 
"0.019133766058650917" + 
":  " + 
"-0.009292461218477582" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 468.0) ? " + 
"(b('L8b1') <= 66.0) ? " + 
"(b('L8dt') <= 281736.0) ? " + 
"-0.02110885713054484" + 
":  " + 
"0.02420871391775904" + 
":  " + 
"(b('gvv') <= -10.161942481994629) ? " + 
"-0.015200962352247872" + 
":  " + 
"0.017149186332869364" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"(b('L8b3med') <= 564.0) ? " + 
"0.04024110933182075" + 
":  " + 
"0.003128488750294561" + 
":  " + 
"(b('L8b1') <= 152.0) ? " + 
"0.08395996220677827" + 
":  " + 
"-9.79656219242983e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 872.5) ? " + 
"(b('L8b3') <= 860.5) ? " + 
"(b('L8b3') <= 856.5) ? " + 
"-0.0006211173506884759" + 
":  " + 
"0.01816864678906889" + 
":  " + 
"(b('ndvi_med') <= 2857.5) ? " + 
"-0.00033741193228804025" + 
":  " + 
"-0.027317101163881367" + 
":  " + 
"(b('L8b4') <= 1134.5) ? " + 
"(b('lon') <= -110.83245468139648) ? " + 
"0.024170305696675404" + 
":  " + 
"0.0027735593023529613" + 
":  " + 
"(b('L8b5') <= 2208.5) ? " + 
"-0.006212882934877809" + 
":  " + 
"0.0003374484774482828" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5') <= 3479.5) ? " + 
"(b('gvv') <= -8.560012340545654) ? " + 
"-0.00022282128914125068" + 
":  " + 
"0.00346970607198745" + 
":  " + 
"(b('clay') <= 13.5) ? " + 
"-0.04674662902250115" + 
":  " + 
"0.018666866279914512" + 
":  " + 
"(b('L8b5') <= 3520.5) ? " + 
"(b('gvv') <= -11.849279880523682) ? " + 
"-0.04018202452513708" + 
":  " + 
"-0.09355281687599729" + 
":  " + 
"(b('dgvv') <= 1.1607327461242676) ? " + 
"0.0011601313177828816" + 
":  " + 
"-0.008986399737855266" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -18.447688102722168) ? " + 
"(b('ndvi') <= 2666.0) ? " + 
"(b('bulk') <= 163.0) ? " + 
"0.011020023484142659" + 
":  " + 
"0.10951726627476452" + 
":  " + 
"(b('L8b4med') <= 1382.0) ? " + 
"-0.03154901956861219" + 
":  " + 
"-0.06989131556186842" + 
":  " + 
"(b('gvv') <= -18.44324779510498) ? " + 
"-0.11190675802935586" + 
":  " + 
"(b('dsvv') <= -3.221768379211426) ? " + 
"-0.005743997247780315" + 
":  " + 
"8.687069639886678e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 5456.5) ? " + 
"(b('L8b7') <= 3244.5) ? " + 
"(b('L8b6') <= 3892.5) ? " + 
"0.00010840256875675534" + 
":  " + 
"-0.0031865663927850333" + 
":  " + 
"(b('dsvv') <= 2.2053380012512207) ? " + 
"0.003996758533684842" + 
":  " + 
"-0.011866879196800857" + 
":  " + 
"(b('dgvh') <= -8.35959243774414) ? " + 
"(b('dgvv') <= -0.07757377624511719) ? " + 
"-0.020450245237999026" + 
":  " + 
"-0.006319260854754025" + 
":  " + 
"(b('lat') <= 41.32942008972168) ? " + 
"-0.03141779903610452" + 
":  " + 
"-0.0393322585520317" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1063.5) ? " + 
"(b('L8b3') <= 1055.5) ? " + 
"(b('L8b4med') <= 1502.25) ? " + 
"-0.0008343650800551714" + 
":  " + 
"0.004336113230949591" + 
":  " + 
"(b('gvv') <= -13.292133331298828) ? " + 
"-0.008660743022572422" + 
":  " + 
"-0.036182359468596485" + 
":  " + 
"(b('L8b4') <= 1294.0) ? " + 
"(b('L8b11') <= 2243.0) ? " + 
"0.019649310786272547" + 
":  " + 
"-0.007459945281346629" + 
":  " + 
"(b('L8b7') <= 1680.5) ? " + 
"0.040892098719070125" + 
":  " + 
"-0.0001338375728594579" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4762.5) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4290.5) ? " + 
"8.372093953685629e-06" + 
":  " + 
"0.022075957655950443" + 
":  " + 
"(b('L8dt') <= 2073598.5) ? " + 
"-0.004697734053308045" + 
":  " + 
"-0.04094233277274244" + 
":  " + 
"(b('ndvi') <= 5903.5) ? " + 
"(b('L8b11') <= 2567.5) ? " + 
"0.057346811939474905" + 
":  " + 
"0.0022442576685359587" + 
":  " + 
"(b('dgvh') <= -4.724499702453613) ? " + 
"0.007566665850730464" + 
":  " + 
"-0.012848741796576614" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 730.5) ? " + 
"(b('dgvv') <= -0.5813393592834473) ? " + 
"(b('bulk') <= 121.5) ? " + 
"0.015128599914492051" + 
":  " + 
"-0.007477287093137444" + 
":  " + 
"(b('lon') <= -109.57164764404297) ? " + 
"0.06942088941934614" + 
":  " + 
"0.004419532256268853" + 
":  " + 
"(b('L8b5') <= 1890.5) ? " + 
"(b('L8b3med') <= 1457.25) ? " + 
"-0.0033107493781647664" + 
":  " + 
"-0.04441507398491906" + 
":  " + 
"(b('L8b5') <= 1934.0) ? " + 
"0.013574615390570031" + 
":  " + 
"-0.00013762336391228336" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2043.5) ? " + 
"(b('L8b3') <= 1094.0) ? " + 
"(b('L8b3med') <= 1316.75) ? " + 
"0.0021866494670553186" + 
":  " + 
"-0.0218774457456161" + 
":  " + 
"(b('dsvh') <= -7.934507369995117) ? " + 
"0.010462008545699378" + 
":  " + 
"0.05668483289506085" + 
":  " + 
"(b('L8b5') <= 2056.5) ? " + 
"(b('moss') <= 7.033738374710083) ? " + 
"-0.026517532795587072" + 
":  " + 
"0.005282600302004406" + 
":  " + 
"(b('L8b3') <= 727.5) ? " + 
"-0.0031935949858447653" + 
":  " + 
"0.00030339276737752067" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 362.5) ? " + 
"(b('L8b3') <= 982.0) ? " + 
"(b('bulk') <= 152.5) ? " + 
"0.0014273554069037114" + 
":  " + 
"-0.0136478694535472" + 
":  " + 
"(b('L8dt') <= 86930.5) ? " + 
"0.16572346975177665" + 
":  " + 
"0.017513341240093884" + 
":  " + 
"(b('L8b1') <= 400.5) ? " + 
"(b('gvv') <= -13.275745391845703) ? " + 
"0.0031028649443892967" + 
":  " + 
"-0.010326293371075705" + 
":  " + 
"(b('L8b2') <= 517.5) ? " + 
"0.008853517226944637" + 
":  " + 
"-4.315607147261692e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -6.216152667999268) ? " + 
"(b('gvv') <= -6.294252157211304) ? " + 
"(b('dgvv') <= 3.967639923095703) ? " + 
"-5.180759107457753e-05" + 
":  " + 
"0.006052908807535456" + 
":  " + 
"(b('dsvv') <= 4.663687467575073) ? " + 
"0.014363121334210206" + 
":  " + 
"0.10212141394683188" + 
":  " + 
"(b('L8b3med') <= 792.0) ? " + 
"(b('L8b2') <= 387.0) ? " + 
"0.0066592364363720295" + 
":  " + 
"-0.019993117867309913" + 
":  " + 
"(b('ndvi') <= 866.0) ? " + 
"-0.08584604123891966" + 
":  " + 
"0.002343174697441589" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 697.5) ? " + 
"(b('L8b4') <= 686.25) ? " + 
"(b('L8b5') <= 3744.5) ? " + 
"0.0006957707003298638" + 
":  " + 
"-0.06550775718112856" + 
":  " + 
"(b('crop') <= 63.619285583496094) ? " + 
"0.03199710702828275" + 
":  " + 
"-0.001826088092460725" + 
":  " + 
"(b('L8b1') <= 255.5) ? " + 
"(b('moss') <= 13.848764896392822) ? " + 
"-0.006450757596228494" + 
":  " + 
"-0.05295212485626814" + 
":  " + 
"(b('L8b3med') <= 565.0) ? " + 
"0.024144560276880014" + 
":  " + 
"-8.679324786197587e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2990.5) ? " + 
"(b('L8b5') <= 3381.5) ? " + 
"(b('L8b5') <= 3336.5) ? " + 
"-6.24851222521294e-06" + 
":  " + 
"0.01395241138739474" + 
":  " + 
"(b('clay') <= 21.5) ? " + 
"-0.007509543540423035" + 
":  " + 
"0.0018404373740374344" + 
":  " + 
"(b('L8b4') <= 1442.0) ? " + 
"(b('L8b4') <= 1423.0) ? " + 
"0.011103867811523385" + 
":  " + 
"0.118226977492437" + 
":  " + 
"(b('L8b5') <= 2352.5) ? " + 
"-0.038809814169759475" + 
":  " + 
"0.0011436528075769615" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6342931.5) ? " + 
"(b('dgvv') <= -4.768918037414551) ? " + 
"(b('ndvi_med') <= 4038.5) ? " + 
"-0.0008617936708621217" + 
":  " + 
"-0.0319986218454855" + 
":  " + 
"(b('dsvv') <= -4.876387119293213) ? " + 
"0.0951188783832573" + 
":  " + 
"-8.411551693422559e-06" + 
":  " + 
"(b('L8b6med') <= 2382.5) ? " + 
"(b('L8dt') <= 11081765.0) ? " + 
"-0.002269743726532253" + 
":  " + 
"-0.01163895471034183" + 
":  " + 
"(b('L8b3') <= 1431.0) ? " + 
"0.017759333320177807" + 
":  " + 
"-0.007804486335897987" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 477.5) ? " + 
"(b('L8b2') <= 476.5) ? " + 
"(b('ndvi') <= 1915.0) ? " + 
"0.008930179662511356" + 
":  " + 
"-0.00024233604752664848" + 
":  " + 
"(b('dsvv') <= 0.6599349975585938) ? " + 
"0.04990071538820363" + 
":  " + 
"-0.028683037054127045" + 
":  " + 
"(b('L8b1') <= 409.5) ? " + 
"(b('L8b4') <= 1064.5) ? " + 
"-0.011182648110240648" + 
":  " + 
"0.0043076273310646935" + 
":  " + 
"(b('L8b1') <= 410.5) ? " + 
"0.047548676774045076" + 
":  " + 
"0.00017609350518812836" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1533.5) ? " + 
"(b('lat') <= -35.10758972167969) ? " + 
"(b('ndvi') <= 1331.5) ? " + 
"0.13308900290141784" + 
":  " + 
"0.06585523085623035" + 
":  " + 
"(b('ndvi') <= 1373.5) ? " + 
"0.0005533399973572654" + 
":  " + 
"-0.005796103380780581" + 
":  " + 
"(b('ndvi_med') <= 1362.5) ? " + 
"(b('dgvh') <= -1.2936954498291016) ? " + 
"0.012040891664962276" + 
":  " + 
"-0.15867561681765738" + 
":  " + 
"(b('ndvi') <= 1545.5) ? " + 
"0.013204156567073883" + 
":  " + 
"-1.254228609016512e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.472105026245117) ? " + 
"(b('L8b6') <= 3629.5) ? " + 
"(b('L8b7') <= 2026.5) ? " + 
"-0.002730115444811034" + 
":  " + 
"0.002424364688706156" + 
":  " + 
"(b('lat') <= 41.77997970581055) ? " + 
"-0.0030125282989558622" + 
":  " + 
"-0.032137876464647525" + 
":  " + 
"(b('dsvv') <= 0.41945409774780273) ? " + 
"(b('lon') <= -5.4481751918792725) ? " + 
"0.01624216541103708" + 
":  " + 
"0.0011760916711225826" + 
":  " + 
"(b('L8b11') <= 2904.5) ? " + 
"-0.0003497531982974492" + 
":  " + 
"-0.009416054209514765" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1184.5) ? " + 
"(b('ndvi') <= 1179.5) ? " + 
"(b('L8b2') <= 778.0) ? " + 
"-0.008137358606306204" + 
":  " + 
"0.0006239787996380455" + 
":  " + 
"(b('ndvi') <= 1182.5) ? " + 
"-0.09590946964022407" + 
":  " + 
"-0.004190575077984845" + 
":  " + 
"(b('ndvi') <= 1216.5) ? " + 
"(b('L8b7') <= 2763.5) ? " + 
"-0.004602774167157541" + 
":  " + 
"0.02100121099616439" + 
":  " + 
"(b('ndvi_med') <= 965.0) ? " + 
"-0.02060786564384751" + 
":  " + 
"0.0001124485931350597" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 876.5) ? " + 
"(b('gvv') <= -10.827631950378418) ? " + 
"(b('moss') <= 1.5226585865020752) ? " + 
"-0.09961261965983001" + 
":  " + 
"0.0016421696287773563" + 
":  " + 
"(b('L8b7') <= 2556.0) ? " + 
"-0.017915713047767148" + 
":  " + 
"-0.0027172033736832164" + 
":  " + 
"(b('ndvi_med') <= 1220.75) ? " + 
"(b('gvv') <= -9.359025001525879) ? " + 
"0.004291258352821373" + 
":  " + 
"0.0686918338840242" + 
":  " + 
"(b('L8b2') <= 987.0) ? " + 
"0.00017593984286409163" + 
":  " + 
"-0.0036758150717703885" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3707.0) ? " + 
"(b('L8b6med') <= 3695.0) ? " + 
"(b('dsvh') <= -0.7264900207519531) ? " + 
"-0.00016764441686563283" + 
":  " + 
"0.024729035292965895" + 
":  " + 
"(b('L8b7') <= 3211.0) ? " + 
"-0.027679828303777798" + 
":  " + 
"0.017114996540351674" + 
":  " + 
"(b('L8b7') <= 2071.0) ? " + 
"(b('clay') <= 22.5) ? " + 
"-0.00015565451335455247" + 
":  " + 
"-0.018146977798611946" + 
":  " + 
"(b('L8dt') <= 16540.0) ? " + 
"0.09403239166737833" + 
":  " + 
"0.0025096886992076683" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 35512.5) ? " + 
"(b('ndvi') <= 2312.5) ? " + 
"(b('dgvh') <= -7.475337982177734) ? " + 
"-0.0010736540337508915" + 
":  " + 
"-0.021118771942439416" + 
":  " + 
"(b('L8dt') <= 21116.5) ? " + 
"0.008346289685220696" + 
":  " + 
"-0.016267563888665588" + 
":  " + 
"(b('L8b3') <= 666.5) ? " + 
"(b('sand') <= 31.5) ? " + 
"0.008003142592213812" + 
":  " + 
"-0.004385540609160255" + 
":  " + 
"(b('L8b7') <= 1013.5) ? " + 
"0.021254497136259164" + 
":  " + 
"0.00020336460400085203" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 612.5) ? " + 
"(b('L8b4') <= 606.5) ? " + 
"(b('L8b5') <= 3061.0) ? " + 
"0.0037806927738143195" + 
":  " + 
"-0.01669575640152856" + 
":  " + 
"(b('dgvv') <= 2.7716455459594727) ? " + 
"0.016934877848892887" + 
":  " + 
"0.10024583968458999" + 
":  " + 
"(b('L8b4') <= 634.5) ? " + 
"(b('sand') <= 78.5) ? " + 
"-0.0039240610378454945" + 
":  " + 
"-0.06500429660163076" + 
":  " + 
"(b('L8b4') <= 662.5) ? " + 
"0.007972053732200416" + 
":  " + 
"-0.0001165358965581108" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 52.296464920043945) ? " + 
"(b('dgvh') <= -12.092339992523193) ? " + 
"(b('L8b4') <= 1445.5) ? " + 
"-0.05937315666982195" + 
":  " + 
"-0.0014214160067358699" + 
":  " + 
"(b('L8b3') <= 872.5) ? " + 
"-0.001603494914533481" + 
":  " + 
"0.0004866233308294455" + 
":  " + 
"(b('ndvi') <= 2835.0) ? " + 
"(b('L8b4') <= 1089.5) ? " + 
"0.015049969213429859" + 
":  " + 
"0.06307028889368087" + 
":  " + 
"(b('dsvh') <= -3.06563663482666) ? " + 
"-0.0003745938098003949" + 
":  " + 
"-0.025821349107735703" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 362.5) ? " + 
"(b('L8b3') <= 982.0) ? " + 
"(b('bulk') <= 153.5) ? " + 
"0.0012587161831866332" + 
":  " + 
"-0.012984668110941115" + 
":  " + 
"(b('L8dt') <= 86930.5) ? " + 
"0.1490957261987689" + 
":  " + 
"0.015660876130894962" + 
":  " + 
"(b('L8b1') <= 399.5) ? " + 
"(b('L8b11') <= 2188.25) ? " + 
"-0.008775570579114524" + 
":  " + 
"0.00529395771376184" + 
":  " + 
"(b('lat') <= 56.0489501953125) ? " + 
"0.00024584845266854616" + 
":  " + 
"-0.07691072595477129" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2100.5) ? " + 
"(b('ndvi') <= 2092.5) ? " + 
"(b('L8b11') <= 1394.25) ? " + 
"0.026192464425368562" + 
":  " + 
"-0.0005784076791560969" + 
":  " + 
"(b('ndvi') <= 2094.5) ? " + 
"-0.055077705797626345" + 
":  " + 
"-0.011139432039080629" + 
":  " + 
"(b('ndvi_med') <= 2145.0) ? " + 
"(b('lon') <= -105.00619506835938) ? " + 
"0.014696619831175898" + 
":  " + 
"0.0009288405568613018" + 
":  " + 
"(b('ndvi_med') <= 2160.5) ? " + 
"-0.02087677789236702" + 
":  " + 
"-0.00016867070916831302" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 88.85982513427734) ? " + 
"(b('L8b5') <= 1935.5) ? " + 
"(b('L8b3med') <= 717.5) ? " + 
"0.01653989191499867" + 
":  " + 
"0.00015458822680122425" + 
":  " + 
"(b('dsvv') <= 5.340885162353516) ? " + 
"-0.00011804622460170522" + 
":  " + 
"0.021118300359499066" + 
":  " + 
"(b('L8b1') <= 444.0) ? " + 
"(b('L8b7') <= 1099.5) ? " + 
"0.010804219833345431" + 
":  " + 
"-0.013302867673744584" + 
":  " + 
"(b('L8b1') <= 721.0) ? " + 
"0.005394270841345957" + 
":  " + 
"-0.009436379379615329" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 464.5) ? " + 
"(b('L8b1') <= 123.5) ? " + 
"(b('dsvh') <= -6.076297760009766) ? " + 
"0.018254614705449885" + 
":  " + 
"-0.004274559259934447" + 
":  " + 
"(b('dsvh') <= -4.400491237640381) ? " + 
"-0.018796298592093374" + 
":  " + 
"0.010427295074648216" + 
":  " + 
"(b('L8b5') <= 1500.0) ? " + 
"(b('L8b7') <= 1334.0) ? " + 
"0.022480194705894102" + 
":  " + 
"-0.002058558212549342" + 
":  " + 
"(b('L8b5') <= 1508.0) ? " + 
"-0.05091893081157673" + 
":  " + 
"-2.3614665286102113e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1728.0) ? " + 
"(b('ndvi') <= 1441.0) ? " + 
"(b('L8b6') <= 1674.0) ? " + 
"0.0466416703778472" + 
":  " + 
"0.004244077057931459" + 
":  " + 
"(b('L8b7') <= 1098.0) ? " + 
"-0.003197314569807196" + 
":  " + 
"-0.030178285929335226" + 
":  " + 
"(b('L8b6') <= 1745.0) ? " + 
"(b('dgvh') <= -9.319348335266113) ? " + 
"-0.003205451794129387" + 
":  " + 
"0.03068246810311653" + 
":  " + 
"(b('L8b6') <= 1750.5) ? " + 
"-0.03339108196504551" + 
":  " + 
"4.6038869599718875e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= 0.2746467590332031) ? " + 
"(b('dsvh') <= -0.03885698318481445) ? " + 
"(b('ndvi') <= 4009.0) ? " + 
"-0.00023165686978500626" + 
":  " + 
"0.0015173482433732382" + 
":  " + 
"(b('L8b4med') <= 1002.5) ? " + 
"0.0006151042740970558" + 
":  " + 
"0.06788629241314714" + 
":  " + 
"(b('L8b6med') <= 3546.5) ? " + 
"(b('moss') <= 3.3424856662750244) ? " + 
"0.048371646642175525" + 
":  " + 
"-0.0244951399715842" + 
":  " + 
"(b('L8b4med') <= 1486.5) ? " + 
"-0.08525904196809714" + 
":  " + 
"-0.03163601534322259" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('ndvi') <= 6364.5) ? " + 
"(b('sand') <= 31.5) ? " + 
"0.006897585322901462" + 
":  " + 
"-0.0033938222111086305" + 
":  " + 
"(b('L8b3') <= 545.0) ? " + 
"-0.03683818207276934" + 
":  " + 
"-0.06777935071574843" + 
":  " + 
"(b('L8b3') <= 671.5) ? " + 
"(b('L8b11') <= 2217.0) ? " + 
"0.021708302200006104" + 
":  " + 
"-0.047894123374597385" + 
":  " + 
"(b('L8b7') <= 1013.5) ? " + 
"0.018738555805232603" + 
":  " + 
"-2.6963849352022432e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 7.796026229858398) ? " + 
"(b('gvv') <= -6.216152667999268) ? " + 
"(b('gvv') <= -6.294252157211304) ? " + 
"3.798380783332113e-05" + 
":  " + 
"0.028292749214331135" + 
":  " + 
"(b('L8b3med') <= 792.0) ? " + 
"-0.014067341006799518" + 
":  " + 
"0.0002541799505716595" + 
":  " + 
"(b('dgvv') <= 8.369114637374878) ? " + 
"0.051758909372292466" + 
":  " + 
"0.03524440956702249" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b4') <= 2347.5) ? " + 
"(b('L8b7') <= 3421.5) ? " + 
"-0.0003742592348607172" + 
":  " + 
"0.041353311820799064" + 
":  " + 
"(b('L8b4') <= 2364.0) ? " + 
"-0.04515111933474178" + 
":  " + 
"-0.008610021265804405" + 
":  " + 
"(b('L8b5') <= 2417.5) ? " + 
"(b('L8b5') <= 2229.0) ? " + 
"-0.003364614497502143" + 
":  " + 
"0.01427350368647428" + 
":  " + 
"(b('ndvi') <= 2866.5) ? " + 
"-0.0008818981832923272" + 
":  " + 
"0.006672944188240745" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2043.5) ? " + 
"(b('L8b3') <= 1094.0) ? " + 
"(b('L8b4') <= 1237.5) ? " + 
"0.0023464988497583815" + 
":  " + 
"-0.015612544633279619" + 
":  " + 
"(b('L8b6') <= 3035.5) ? " + 
"0.021997743799683483" + 
":  " + 
"0.08958454361115867" + 
":  " + 
"(b('L8b5') <= 2068.5) ? " + 
"(b('L8b6med') <= 3715.5) ? " + 
"-0.012965463080114087" + 
":  " + 
"0.06504085811868542" + 
":  " + 
"(b('L8b3') <= 727.5) ? " + 
"-0.0030088951303794595" + 
":  " + 
"0.00031598674955415283" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 730.5) ? " + 
"(b('L8b4med') <= 829.0) ? " + 
"(b('dsvv') <= -0.575904369354248) ? " + 
"-0.004759929596395346" + 
":  " + 
"0.004085115828204372" + 
":  " + 
"(b('dsvv') <= 0.09009408950805664) ? " + 
"-0.009773130658390897" + 
":  " + 
"0.184710798612599" + 
":  " + 
"(b('L8b3') <= 727.5) ? " + 
"(b('ndvi_med') <= 2600.0) ? " + 
"0.0018392717430536572" + 
":  " + 
"-0.0098617015096794" + 
":  " + 
"(b('L8b3') <= 734.5) ? " + 
"0.016507378010217257" + 
":  " + 
"-8.737577098133045e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 477.5) ? " + 
"(b('L8b2') <= 476.5) ? " + 
"(b('moss') <= 3.1626508235931396) ? " + 
"-0.0037223457102774733" + 
":  " + 
"0.002348965052876839" + 
":  " + 
"(b('dgvv') <= 0.7399349212646484) ? " + 
"0.04310137391212277" + 
":  " + 
"-0.03112886878436754" + 
":  " + 
"(b('L8b3') <= 822.5) ? " + 
"(b('L8b1') <= 410.5) ? " + 
"-0.013915096879540463" + 
":  " + 
"-0.0010247251168678413" + 
":  " + 
"(b('L8b4med') <= 715.5) ? " + 
"0.01565493727338334" + 
":  " + 
"-5.097639993695851e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.41397809982299805) ? " + 
"(b('ndvi') <= 3854.5) ? " + 
"(b('ndvi') <= 3745.0) ? " + 
"8.788246692801926e-05" + 
":  " + 
"-0.017669210673070763" + 
":  " + 
"(b('sand') <= 22.0) ? " + 
"-0.01690718238064216" + 
":  " + 
"0.005473548351875198" + 
":  " + 
"(b('clay') <= 38.5) ? " + 
"(b('crop') <= 49.023324966430664) ? " + 
"0.0014717965900097225" + 
":  " + 
"-0.0026135793328286006" + 
":  " + 
"(b('L8dt') <= 691198.0) ? " + 
"-0.021237615756820934" + 
":  " + 
"-0.058767224499529876" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -8.796432495117188) ? " + 
"(b('gvv') <= -8.863539218902588) ? " + 
"(b('gvv') <= -8.869343757629395) ? " + 
"-0.00012863781901872257" + 
":  " + 
"0.08204216768058721" + 
":  " + 
"(b('L8b2') <= 308.5) ? " + 
"0.04353022613248576" + 
":  " + 
"-0.019036082208402885" + 
":  " + 
"(b('lon') <= 26.74935531616211) ? " + 
"(b('ndvi') <= 3327.0) ? " + 
"0.007507740967442452" + 
":  " + 
"-0.002503522300394188" + 
":  " + 
"(b('dsvv') <= 5.603370904922485) ? " + 
"-0.018151610545848226" + 
":  " + 
"0.011306672110940075" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1508.0) ? " + 
"(b('L8b3') <= 1497.5) ? " + 
"(b('L8b2') <= 1053.5) ? " + 
"-0.00020245154783857648" + 
":  " + 
"0.020803988040548418" + 
":  " + 
"(b('dgvv') <= 4.910737037658691) ? " + 
"-0.019983928245659623" + 
":  " + 
"-0.1281099550742426" + 
":  " + 
"(b('lon') <= 146.3602294921875) ? " + 
"(b('L8b4') <= 2026.5) ? " + 
"0.011448051508851103" + 
":  " + 
"-0.0015098103190633709" + 
":  " + 
"(b('dgvh') <= -10.05540657043457) ? " + 
"-0.046567854726709684" + 
":  " + 
"0.08850682892509561" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -2.388568878173828) ? " + 
"(b('ndvi') <= 3613.5) ? " + 
"(b('ndvi') <= 3539.5) ? " + 
"-0.0038861961110814164" + 
":  " + 
"-0.04342341582084631" + 
":  " + 
"(b('L8b5') <= 3412.5) ? " + 
"0.011873159970802617" + 
":  " + 
"-0.01020739315649389" + 
":  " + 
"(b('dgvv') <= -2.3780198097229004) ? " + 
"(b('dgvv') <= -2.3817248344421387) ? " + 
"0.019989908667771943" + 
":  " + 
"0.09370494202164897" + 
":  " + 
"(b('ndvi') <= 4627.5) ? " + 
"0.0002866829122259578" + 
":  " + 
"-0.0025977172488873784" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.472105026245117) ? " + 
"(b('ndvi') <= 5640.0) ? " + 
"(b('ndvi') <= 3024.0) ? " + 
"-0.001296467194887546" + 
":  " + 
"0.005514442301892721" + 
":  " + 
"(b('L8b3') <= 828.5) ? " + 
"-0.05833428067663464" + 
":  " + 
"-0.019932600541929805" + 
":  " + 
"(b('dgvv') <= 0.7536702156066895) ? " + 
"(b('dsvh') <= -4.162288665771484) ? " + 
"0.0009485336125717755" + 
":  " + 
"0.01722322582011635" + 
":  " + 
"(b('L8b11') <= 2968.0) ? " + 
"-0.0005497510061374576" + 
":  " + 
"-0.012360957315216265" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3707.0) ? " + 
"(b('L8b6med') <= 3695.0) ? " + 
"(b('ndvi') <= 1536.5) ? " + 
"-0.0019998643495107555" + 
":  " + 
"0.00042965111792189753" + 
":  " + 
"(b('L8b7') <= 3211.0) ? " + 
"-0.02439834751756419" + 
":  " + 
"0.01494839396209493" + 
":  " + 
"(b('L8b7') <= 2071.0) ? " + 
"(b('L8b2') <= 431.0) ? " + 
"0.006108286832500892" + 
":  " + 
"-0.013356088510789265" + 
":  " + 
"(b('L8b5') <= 2480.0) ? " + 
"0.012260549181897203" + 
":  " + 
"0.0015696196992539587" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2043.5) ? " + 
"(b('L8b6med') <= 3736.25) ? " + 
"(b('L8b3') <= 1094.0) ? " + 
"0.0017457095159824786" + 
":  " + 
"0.028209269212032644" + 
":  " + 
"(b('dgvv') <= 1.337587833404541) ? " + 
"-0.006778168468776832" + 
":  " + 
"-0.05373977763519482" + 
":  " + 
"(b('L8b5') <= 2068.5) ? " + 
"(b('L8b6med') <= 3715.5) ? " + 
"-0.011627632477767871" + 
":  " + 
"0.05726926989912131" + 
":  " + 
"(b('L8b3') <= 727.5) ? " + 
"-0.0028245846937332455" + 
":  " + 
"0.000276151499618829" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 756.5) ? " + 
"(b('lon') <= -107.14787673950195) ? " + 
"(b('L8b3') <= 658.5) ? " + 
"-0.00851833784489876" + 
":  " + 
"0.03107471194742463" + 
":  " + 
"(b('dgvv') <= 2.5355966091156006) ? " + 
"-0.0008407325007273434" + 
":  " + 
"0.012560301572772551" + 
":  " + 
"(b('L8b1') <= 255.5) ? " + 
"(b('L8b2') <= 358.5) ? " + 
"0.0012572503263769185" + 
":  " + 
"-0.024291844006179068" + 
":  " + 
"(b('L8b1') <= 295.5) ? " + 
"0.010508624532837702" + 
":  " + 
"-0.00033858413002072483" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4med') <= 1521.5) ? " + 
"(b('L8b3') <= 1474.5) ? " + 
"(b('L8b4') <= 1895.5) ? " + 
"-0.0005414766127937878" + 
":  " + 
"-0.0374963624689931" + 
":  " + 
"(b('dgvv') <= 0.40576696395874023) ? " + 
"0.004835556458027567" + 
":  " + 
"0.03944621813951965" + 
":  " + 
"(b('L8b4') <= 1445.5) ? " + 
"(b('bulk') <= 144.5) ? " + 
"0.032119170245219354" + 
":  " + 
"0.001844664395643004" + 
":  " + 
"(b('L8b7') <= 1680.5) ? " + 
"0.07990674566802805" + 
":  " + 
"-0.0003254321536717582" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2605.5) ? " + 
"(b('L8b2') <= 820.5) ? " + 
"(b('L8b2') <= 819.5) ? " + 
"2.98892759626189e-05" + 
":  " + 
"0.06884276269262171" + 
":  " + 
"(b('lat') <= 35.84549903869629) ? " + 
"0.018405733589483754" + 
":  " + 
"-0.006730227472549179" + 
":  " + 
"(b('L8b7') <= 2651.5) ? " + 
"(b('L8b5') <= 3665.0) ? " + 
"0.0069106904348994426" + 
":  " + 
"0.05865972581545069" + 
":  " + 
"(b('L8dt') <= 4299682.0) ? " + 
"0.0004647408584979276" + 
":  " + 
"-0.021402818134019896" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -11.414001941680908) ? " + 
"(b('dgvv') <= 1.7685985565185547) ? " + 
"(b('dgvv') <= 1.7618999481201172) ? " + 
"-4.455725255043458e-05" + 
":  " + 
"0.1087329050187316" + 
":  " + 
"(b('L8b3') <= 500.0) ? " + 
"-0.1487099240418212" + 
":  " + 
"-0.009727419511911663" + 
":  " + 
"(b('bulk') <= 158.5) ? " + 
"(b('lon') <= -120.46174621582031) ? " + 
"-0.0264046644982401" + 
":  " + 
"0.0007052500152198384" + 
":  " + 
"(b('L8b6') <= 2127.0) ? " + 
"-0.11225532354271353" + 
":  " + 
"0.03293920797375063" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 697.5) ? " + 
"(b('crop') <= 57.618377685546875) ? " + 
"(b('L8b4') <= 683.5) ? " + 
"0.0027789468251414816" + 
":  " + 
"0.02978439726110037" + 
":  " + 
"(b('lon') <= -38.50918889045715) ? " + 
"-0.028765855760703236" + 
":  " + 
"-0.0013556717501403829" + 
":  " + 
"(b('L8b4') <= 703.5) ? " + 
"(b('L8b5') <= 2135.0) ? " + 
"0.016567250143249994" + 
":  " + 
"-0.026266509972806693" + 
":  " + 
"(b('L8b1') <= 255.5) ? " + 
"-0.007099012230237064" + 
":  " + 
"6.83501983274154e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3042769.5) ? " + 
"(b('L8b5') <= 1430.0) ? " + 
"(b('L8b3') <= 560.0) ? " + 
"-0.0002415983205850885" + 
":  " + 
"0.04215100999923433" + 
":  " + 
"(b('L8b4') <= 529.0) ? " + 
"0.0068706013477115345" + 
":  " + 
"-0.00028090855199011764" + 
":  " + 
"(b('L8b11') <= 2835.5) ? " + 
"(b('L8b6') <= 4860.5) ? " + 
"0.004918261333927462" + 
":  " + 
"-0.03149385431826778" + 
":  " + 
"(b('L8b6') <= 3336.5) ? " + 
"0.01572270796423928" + 
":  " + 
"-0.01858628533914694" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 464.5) ? " + 
"(b('L8b1') <= 123.5) ? " + 
"(b('dgvv') <= 0.3523235321044922) ? " + 
"0.018729490221069473" + 
":  " + 
"-0.003391434116560748" + 
":  " + 
"(b('dgvh') <= -4.347221851348877) ? " + 
"-0.016400249924255938" + 
":  " + 
"0.012917957190468525" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"(b('L8b3med') <= 564.0) ? " + 
"0.03612372557992409" + 
":  " + 
"0.0028944982424621265" + 
":  " + 
"(b('L8b1') <= 152.0) ? " + 
"0.07575049839552109" + 
":  " + 
"-8.942174020553766e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2908.5) ? " + 
"(b('L8b7') <= 2862.5) ? " + 
"(b('L8b7') <= 2858.5) ? " + 
"-9.315315577194114e-05" + 
":  " + 
"0.029588892513156315" + 
":  " + 
"(b('L8b6') <= 3526.5) ? " + 
"0.0011803332321090533" + 
":  " + 
"-0.01681359207202254" + 
":  " + 
"(b('L8b7') <= 2909.5) ? " + 
"(b('L8dt') <= 92589.0) ? " + 
"0.18982761940884532" + 
":  " + 
"0.04631422534716626" + 
":  " + 
"(b('L8b1') <= 537.5) ? " + 
"-0.02581461587823102" + 
":  " + 
"0.0012958348931368625" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.59345054626465) ? " + 
"(b('L8b4') <= 995.5) ? " + 
"(b('L8b3') <= 845.5) ? " + 
"0.0007335572024257764" + 
":  " + 
"0.020663541750132148" + 
":  " + 
"(b('L8b4') <= 1020.5) ? " + 
"-0.018729650510063183" + 
":  " + 
"0.00020771376066692376" + 
":  " + 
"(b('dgvh') <= -1.5272550582885742) ? " + 
"(b('lon') <= 0.756400004029274) ? " + 
"-0.003609949552828392" + 
":  " + 
"0.00048086320478972684" + 
":  " + 
"(b('L8dt') <= 2360298.5) ? " + 
"-0.05277253392247712" + 
":  " + 
"0.0005580593235040357" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 314.5) ? " + 
"(b('L8b6') <= 2321.5) ? " + 
"(b('L8b3') <= 761.5) ? " + 
"-0.0009795704345960735" + 
":  " + 
"0.015095456918829799" + 
":  " + 
"(b('L8b4') <= 1001.5) ? " + 
"-0.004567152208836069" + 
":  " + 
"-0.028220321034362686" + 
":  " + 
"(b('L8b1') <= 347.5) ? " + 
"(b('ndvi') <= 2718.5) ? " + 
"0.01662622397908377" + 
":  " + 
"-0.0005814992872740034" + 
":  " + 
"(b('L8b6') <= 2555.0) ? " + 
"-0.003455223749479802" + 
":  " + 
"0.00044274703329598154" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3189.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"(b('L8b5') <= 3187.5) ? " + 
"9.840064157866843e-05" + 
":  " + 
"0.020777593925078983" + 
":  " + 
"(b('dsvh') <= -5.357793807983398) ? " + 
"0.006365162516710406" + 
":  " + 
"0.06396991546035187" + 
":  " + 
"(b('bulk') <= 168.5) ? " + 
"(b('L8b7') <= 2589.0) ? " + 
"-0.0031510975475953474" + 
":  " + 
"0.0020289034965278573" + 
":  " + 
"(b('dgvv') <= -0.5773601531982422) ? " + 
"0.08511864137906844" + 
":  " + 
"0.1340178153716279" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6342931.5) ? " + 
"(b('dgvv') <= -4.768918037414551) ? " + 
"(b('ndvi_med') <= 4038.5) ? " + 
"-0.0013441000317725071" + 
":  " + 
"-0.02926496237846095" + 
":  " + 
"(b('dsvv') <= -4.876387119293213) ? " + 
"0.08280760375474833" + 
":  " + 
"-6.2676089676127106e-06" + 
":  " + 
"(b('L8b6med') <= 2382.5) ? " + 
"(b('L8dt') <= 11600114.0) ? " + 
"-0.004348129301144715" + 
":  " + 
"-0.015498769424271659" + 
":  " + 
"(b('L8b5') <= 3128.5) ? " + 
"0.02484662011343579" + 
":  " + 
"0.0073684136060702616" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -8.234763145446777) ? " + 
"(b('moss') <= 13.875449180603027) ? " + 
"(b('crop') <= 77.25693130493164) ? " + 
"-0.0040907909035930385" + 
":  " + 
"0.0003038991882951301" + 
":  " + 
"(b('dsvv') <= -0.8206992149353027) ? " + 
"0.01227484918581334" + 
":  " + 
"1.9560795431312572e-05" + 
":  " + 
"(b('dsvh') <= -8.078860759735107) ? " + 
"(b('moss') <= 10.28225564956665) ? " + 
"0.012270550071083734" + 
":  " + 
"-0.0005917053612620747" + 
":  " + 
"(b('L8b5') <= 2160.5) ? " + 
"0.0029427216412699388" + 
":  " + 
"-0.0004138720414041576" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 35512.5) ? " + 
"(b('bulk') <= 134.5) ? " + 
"(b('L8b5') <= 2684.5) ? " + 
"0.015129627774484174" + 
":  " + 
"-0.0013124231600882413" + 
":  " + 
"(b('L8b3') <= 852.5) ? " + 
"-0.02131607258808665" + 
":  " + 
"-0.002466923464073182" + 
":  " + 
"(b('gvv') <= -15.07451581954956) ? " + 
"(b('clay') <= 26.5) ? " + 
"-0.004646072523868194" + 
":  " + 
"0.0038122843180979286" + 
":  " + 
"(b('gvv') <= -15.044612407684326) ? " + 
"0.039930145151545644" + 
":  " + 
"0.0002456575304713701" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -18.447688102722168) ? " + 
"(b('ndvi') <= 2666.0) ? " + 
"(b('lon') <= -120.53757858276367) ? " + 
"0.10131798696872754" + 
":  " + 
"0.010058423428474371" + 
":  " + 
"(b('L8b3') <= 913.5) ? " + 
"-0.06665407066631741" + 
":  " + 
"-0.02744966150534776" + 
":  " + 
"(b('gvv') <= -18.44324779510498) ? " + 
"-0.09949184515748288" + 
":  " + 
"(b('dsvv') <= -3.221768379211426) ? " + 
"-0.0048247784329541014" + 
":  " + 
"7.018400497928068e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4762.5) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4290.5) ? " + 
"7.416055143040567e-06" + 
":  " + 
"0.019537429618307938" + 
":  " + 
"(b('L8dt') <= 2073598.5) ? " + 
"-0.004165446823059473" + 
":  " + 
"-0.036196896134559266" + 
":  " + 
"(b('ndvi') <= 5903.5) ? " + 
"(b('L8b6med') <= 3748.5) ? " + 
"0.047672660627561037" + 
":  " + 
"0.005768839244355579" + 
":  " + 
"(b('dgvh') <= -4.724499702453613) ? " + 
"0.007039385703950716" + 
":  " + 
"-0.00974424224084018" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1190.5) ? " + 
"(b('L8b2') <= 776.5) ? " + 
"(b('L8b4') <= 1612.0) ? " + 
"-0.0026598718496819267" + 
":  " + 
"-0.031748219745101454" + 
":  " + 
"(b('L8b4med') <= 1258.5) ? " + 
"-0.07303825431198395" + 
":  " + 
"0.0007127541286545869" + 
":  " + 
"(b('ndvi') <= 1216.5) ? " + 
"(b('lat') <= 46.435110092163086) ? " + 
"0.009040104671021306" + 
":  " + 
"0.0937276450036904" + 
":  " + 
"(b('ndvi_med') <= 1423.0) ? " + 
"0.002862906099476632" + 
":  " + 
"-0.0001646458467598393" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 876.5) ? " + 
"(b('sand') <= 53.5) ? " + 
"(b('dgvh') <= -7.158897876739502) ? " + 
"-0.03562085976593597" + 
":  " + 
"0.00996235265130749" + 
":  " + 
"(b('dsvv') <= -0.3313426971435547) ? " + 
"0.007901251040884634" + 
":  " + 
"-0.0057821841880122665" + 
":  " + 
"(b('ndvi_med') <= 939.5) ? " + 
"(b('gvv') <= -8.927423000335693) ? " + 
"0.009276583781900364" + 
":  " + 
"0.0964246006188536" + 
":  " + 
"(b('L8b4') <= 2063.0) ? " + 
"0.00021966558112906164" + 
":  " + 
"-0.002353539436299233" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -11.414001941680908) ? " + 
"(b('dgvv') <= 1.3782858848571777) ? " + 
"(b('dgvh') <= -2.396106243133545) ? " + 
"2.1876413484282006e-05" + 
":  " + 
"0.0590854645736279" + 
":  " + 
"(b('bulk') <= 162.0) ? " + 
"-0.0061629373988086305" + 
":  " + 
"-0.052226729150346304" + 
":  " + 
"(b('lon') <= -120.92649459838867) ? " + 
"(b('L8b5') <= 2013.5) ? " + 
"0.006294396414914068" + 
":  " + 
"-0.03764751085068404" + 
":  " + 
"(b('bulk') <= 163.5) ? " + 
"0.0007113115251193596" + 
":  " + 
"0.08052755321200734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -121.13610458374023) ? " + 
"(b('dsvv') <= 1.2880163192749023) ? " + 
"(b('ndvi') <= 2107.0) ? " + 
"0.0020909673955536896" + 
":  " + 
"0.03329383004893994" + 
":  " + 
"(b('L8b2') <= 249.0) ? " + 
"-0.11819470280125985" + 
":  " + 
"-0.018566717752236304" + 
":  " + 
"(b('L8dt') <= 236046.5) ? " + 
"(b('dsvh') <= -4.713353157043457) ? " + 
"-0.0002977637339005737" + 
":  " + 
"-0.008802103946668742" + 
":  " + 
"(b('L8dt') <= 236051.5) ? " + 
"0.02704076538955237" + 
":  " + 
"0.00011537064225437722" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -6.351504802703857) ? " + 
"(b('dsvv') <= 2.131354808807373) ? " + 
"(b('dsvv') <= 1.7715129852294922) ? " + 
"-0.00038046695467344803" + 
":  " + 
"0.013071476749216604" + 
":  " + 
"(b('L8b5') <= 1758.5) ? " + 
"-0.03129469338805566" + 
":  " + 
"-0.005256656522871832" + 
":  " + 
"(b('dgvh') <= -6.346902847290039) ? " + 
"(b('ndvi') <= 4904.5) ? " + 
"0.029992021694462686" + 
":  " + 
"0.15627559260191642" + 
":  " + 
"(b('L8b1') <= 269.5) ? " + 
"-0.004253085868867904" + 
":  " + 
"0.0011827910144840178" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 715.5) ? " + 
"(b('L8b5') <= 3774.5) ? " + 
"(b('ndvi_med') <= 2928.0) ? " + 
"0.0071876122437944875" + 
":  " + 
"-0.0005573635354797195" + 
":  " + 
"(b('sand') <= 41.0) ? " + 
"-0.06288901363819398" + 
":  " + 
"0.08535151049705286" + 
":  " + 
"(b('L8b4') <= 717.5) ? " + 
"(b('dsvh') <= -6.230070114135742) ? " + 
"-0.00020210499720739344" + 
":  " + 
"-0.05923351017605289" + 
":  " + 
"(b('L8b1') <= 255.5) ? " + 
"-0.009759913650024045" + 
":  " + 
"7.114587250152688e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 2.9752492904663086) ? " + 
"(b('dsvv') <= 2.9516441822052) ? " + 
"(b('ndvi') <= 4009.0) ? " + 
"-0.0003705211019454801" + 
":  " + 
"0.0018607014077788213" + 
":  " + 
"(b('crop') <= 66.27124786376953) ? " + 
"-0.01786928648019981" + 
":  " + 
"-0.0862090899796007" + 
":  " + 
"(b('L8b3') <= 504.0) ? " + 
"-0.145989071394183" + 
":  " + 
"(b('sand') <= 24.0) ? " + 
"0.03031082152808256" + 
":  " + 
"0.001575038391579369" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 26.31478500366211) ? " + 
"(b('dsvv') <= 0.41397809982299805) ? " + 
"(b('dgvh') <= -2.749488353729248) ? " + 
"0.0003746942232915319" + 
":  " + 
"0.043951048002103255" + 
":  " + 
"(b('L8dt') <= 1361386.5) ? " + 
"-0.0019502505519529395" + 
":  " + 
"0.0026046336131323703" + 
":  " + 
"(b('L8b7') <= 2118.0) ? " + 
"(b('L8b6') <= 2446.0) ? " + 
"-0.005675192001969472" + 
":  " + 
"0.04216580864515177" + 
":  " + 
"(b('L8b7') <= 2570.0) ? " + 
"-0.02581810543964401" + 
":  " + 
"0.03270449513213374" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 85.84851455688477) ? " + 
"(b('dgvv') <= 2.8459320068359375) ? " + 
"(b('dsvv') <= 2.8066301345825195) ? " + 
"3.0303620489269907e-05" + 
":  " + 
"-0.032535677272348754" + 
":  " + 
"(b('crop') <= 84.48699569702148) ? " + 
"0.002587054823426723" + 
":  " + 
"0.030995758651793326" + 
":  " + 
"(b('L8b1') <= 723.5) ? " + 
"(b('L8b2') <= 942.5) ? " + 
"-0.0009398685761368715" + 
":  " + 
"0.02804242196008232" + 
":  " + 
"(b('crop') <= 89.8235092163086) ? " + 
"-0.02740816658993462" + 
":  " + 
"-0.0036307954340459325" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 4176.5) ? " + 
"(b('L8b6') <= 4820.0) ? " + 
"(b('L8b6') <= 4782.0) ? " + 
"1.4941865603480102e-05" + 
":  " + 
"0.029871113139222565" + 
":  " + 
"(b('L8dt') <= 1189024.0) ? " + 
"0.002065505438198638" + 
":  " + 
"-0.02262241442608902" + 
":  " + 
"(b('clay') <= 18.5) ? " + 
"(b('dgvv') <= -0.9901890754699707) ? " + 
"0.048682515826949546" + 
":  " + 
"0.017339958415044005" + 
":  " + 
"(b('L8dt') <= 289239.5) ? " + 
"0.011614506116667013" + 
":  " + 
"-0.0066134618641903176" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 464.5) ? " + 
"(b('L8b1') <= 123.5) ? " + 
"(b('L8b6med') <= 2464.5) ? " + 
"0.013639989944054565" + 
":  " + 
"-0.005566573576873614" + 
":  " + 
"(b('dgvh') <= -4.347221851348877) ? " + 
"-0.014930730911627351" + 
":  " + 
"0.011931548785053219" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"(b('ndvi') <= 2039.5) ? " + 
"-0.040489205963472226" + 
":  " + 
"0.006102538017822185" + 
":  " + 
"(b('L8b4') <= 538.5) ? " + 
"-0.0176666042592925" + 
":  " + 
"-2.0742063028136572e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= 0.2746467590332031) ? " + 
"(b('dsvh') <= -0.03885698318481445) ? " + 
"(b('lat') <= -35.25544357299805) ? " + 
"0.0050740864049118066" + 
":  " + 
"-5.541575467041431e-05" + 
":  " + 
"(b('clay') <= 34.5) ? " + 
"0.05375897599920134" + 
":  " + 
"0.0010965494827339661" + 
":  " + 
"(b('L8b6med') <= 3546.5) ? " + 
"(b('crop') <= 57.40461540222168) ? " + 
"0.040972453905746706" + 
":  " + 
"-0.01877888801982623" + 
":  " + 
"(b('L8b3med') <= 1105.5) ? " + 
"-0.07048428599585276" + 
":  " + 
"-0.029121441552610754" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 612.5) ? " + 
"(b('gvv') <= -12.332101345062256) ? " + 
"(b('L8b7') <= 1320.0) ? " + 
"0.006134101853314603" + 
":  " + 
"0.04554449922241527" + 
":  " + 
"(b('L8b4') <= 591.0) ? " + 
"-0.006433544918648425" + 
":  " + 
"0.011378631945090376" + 
":  " + 
"(b('L8b4') <= 634.5) ? " + 
"(b('sand') <= 78.5) ? " + 
"-0.003957709516771363" + 
":  " + 
"-0.056080372234636036" + 
":  " + 
"(b('L8b4') <= 638.5) ? " + 
"0.016720583091076047" + 
":  " + 
"-2.078730291300155e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -6.216152667999268) ? " + 
"(b('gvv') <= -6.23303484916687) ? " + 
"(b('ndvi') <= 7065.0) ? " + 
"2.1478170299168752e-05" + 
":  " + 
"0.016878881248258246" + 
":  " + 
"(b('L8b5') <= 2943.5) ? " + 
"0.11779371714806049" + 
":  " + 
"-0.0012915233924781777" + 
":  " + 
"(b('L8b3med') <= 799.5) ? " + 
"(b('L8dt') <= 777827.0) ? " + 
"-0.0014775377870171731" + 
":  " + 
"-0.019638975194167404" + 
":  " + 
"(b('ndvi') <= 866.0) ? " + 
"-0.07430541035364349" + 
":  " + 
"0.0024295155281071528" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5') <= 3479.5) ? " + 
"(b('moss') <= 7.336734771728516) ? " + 
"0.0008513029497098663" + 
":  " + 
"-0.0008722933672434554" + 
":  " + 
"(b('sand') <= 58.5) ? " + 
"0.018193888544795193" + 
":  " + 
"-0.03364578924832788" + 
":  " + 
"(b('L8b5') <= 3520.5) ? " + 
"(b('gvv') <= -11.849279880523682) ? " + 
"-0.03213676406175134" + 
":  " + 
"-0.08151041594639216" + 
":  " + 
"(b('L8b3') <= 895.5) ? " + 
"0.006571981346404557" + 
":  " + 
"-0.0030172228479488357" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6342931.5) ? " + 
"(b('L8b3') <= 666.5) ? " + 
"(b('ndvi') <= 6364.5) ? " + 
"-0.0014621852984186576" + 
":  " + 
"-0.05024973130096052" + 
":  " + 
"(b('L8b3') <= 669.0) ? " + 
"0.02054686701269043" + 
":  " + 
"4.7612897948407556e-05" + 
":  " + 
"(b('L8b6med') <= 2382.5) ? " + 
"(b('dsvh') <= -8.555030345916748) ? " + 
"-0.009647779716942211" + 
":  " + 
"-0.002085270928818613" + 
":  " + 
"(b('crop') <= 80.92045593261719) ? " + 
"0.006596056915298368" + 
":  " + 
"0.024255019611570394" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 730.5) ? " + 
"(b('lon') <= -109.57164764404297) ? " + 
"(b('dsvv') <= 0.09009408950805664) ? " + 
"-0.006596123735197297" + 
":  " + 
"0.1663895644213352" + 
":  " + 
"(b('L8b5') <= 1903.5) ? " + 
"0.011185054913241349" + 
":  " + 
"-0.0005060853117806436" + 
":  " + 
"(b('L8b3') <= 694.5) ? " + 
"(b('L8b5') <= 2353.0) ? " + 
"0.0010442373105145554" + 
":  " + 
"-0.012842146729771414" + 
":  " + 
"(b('L8b7') <= 1027.5) ? " + 
"0.016399382866274025" + 
":  " + 
"-5.4831562291542094e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 756.5) ? " + 
"(b('lon') <= -107.14787673950195) ? " + 
"(b('L8b3') <= 658.5) ? " + 
"-0.0067349540496995" + 
":  " + 
"0.027101273228532643" + 
":  " + 
"(b('lon') <= -38.202388048172) ? " + 
"-0.011698352265757255" + 
":  " + 
"0.0010544662758750708" + 
":  " + 
"(b('L8b6med') <= 2124.5) ? " + 
"(b('L8b7') <= 1756.0) ? " + 
"-0.02996380887550845" + 
":  " + 
"0.008744526413646649" + 
":  " + 
"(b('L8b11') <= 1342.5) ? " + 
"0.014285584889698862" + 
":  " + 
"-0.00024372057835298058" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -121.92677688598633) ? " + 
"(b('ndvi') <= 3460.5) ? " + 
"(b('L8b6') <= 1866.5) ? " + 
"0.07858414395962879" + 
":  " + 
"0.00860209863876175" + 
":  " + 
"-0.10577447818453686" + 
":  " + 
"(b('L8b7') <= 2606.5) ? " + 
"(b('L8b2') <= 820.5) ? " + 
"5.242943734675972e-05" + 
":  " + 
"-0.004396811352702222" + 
":  " + 
"(b('L8b7') <= 2651.5) ? " + 
"0.00908978061649115" + 
":  " + 
"0.00016420207558621658" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1370.0) ? " + 
"(b('dgvv') <= -0.3374648094177246) ? " + 
"(b('gvv') <= -14.271472930908203) ? " + 
"-0.003707025116593992" + 
":  " + 
"0.009754444568457293" + 
":  " + 
"(b('L8b4') <= 536.5) ? " + 
"-0.06541452030776505" + 
":  " + 
"-0.0007034661499267696" + 
":  " + 
"(b('L8b4') <= 2648.5) ? " + 
"(b('L8b2') <= 1139.5) ? " + 
"-0.0001376659312860503" + 
":  " + 
"-0.009890560490508217" + 
":  " + 
"(b('L8b1') <= 977.5) ? " + 
"0.029974366752214487" + 
":  " + 
"-0.0028209664956149014" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 464.5) ? " + 
"(b('L8b1') <= 123.5) ? " + 
"(b('dsvh') <= -6.076297760009766) ? " + 
"0.013363705080356794" + 
":  " + 
"-0.004819129432215459" + 
":  " + 
"(b('dgvh') <= -4.388234615325928) ? " + 
"-0.014339346949932167" + 
":  " + 
"0.007360007719683656" + 
":  " + 
"(b('L8b4') <= 501.5) ? " + 
"(b('ndvi') <= 2392.5) ? " + 
"0.09352797928253143" + 
":  " + 
"0.009338848288913295" + 
":  " + 
"(b('L8b7') <= 901.5) ? " + 
"-0.014620858997786675" + 
":  " + 
"3.6849553714321904e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 88.85982513427734) ? " + 
"(b('gvv') <= -11.413715362548828) ? " + 
"(b('dgvv') <= 1.7685985565185547) ? " + 
"-6.517808227774433e-05" + 
":  " + 
"-0.008397668759368922" + 
":  " + 
"(b('L8b6') <= 3503.5) ? " + 
"8.894982756487644e-05" + 
":  " + 
"0.006381842666175054" + 
":  " + 
"(b('L8b3') <= 1572.5) ? " + 
"(b('L8b3') <= 1527.5) ? " + 
"-0.0014031475773924156" + 
":  " + 
"0.021010227936288952" + 
":  " + 
"(b('L8b5') <= 3302.5) ? " + 
"-0.032022473613901724" + 
":  " + 
"8.972000616794295e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 612.5) ? " + 
"(b('L8b5') <= 2952.5) ? " + 
"(b('L8b5') <= 2402.0) ? " + 
"-0.0030788266570169445" + 
":  " + 
"0.014883198924961193" + 
":  " + 
"(b('moss') <= 14.398427486419678) ? " + 
"-0.0018455829401163924" + 
":  " + 
"-0.06334745614934917" + 
":  " + 
"(b('L8b4') <= 634.5) ? " + 
"(b('L8b11') <= 1319.0) ? " + 
"-0.05644032257315082" + 
":  " + 
"-0.003959727037392723" + 
":  " + 
"(b('L8b4') <= 638.5) ? " + 
"0.014925080983264893" + 
":  " + 
"-2.7502390524878828e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -18.447688102722168) ? " + 
"(b('ndvi') <= 2666.0) ? " + 
"(b('bulk') <= 163.0) ? " + 
"0.00909233893616239" + 
":  " + 
"0.09115382730043561" + 
":  " + 
"(b('dgvh') <= -5.214958190917969) ? " + 
"-0.0248623300461752" + 
":  " + 
"-0.06000499073632526" + 
":  " + 
"(b('gvv') <= -18.44324779510498) ? " + 
"-0.08940266198145841" + 
":  " + 
"(b('dsvv') <= -3.221768379211426) ? " + 
"-0.004238675653565595" + 
":  " + 
"6.088979923599433e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1533.5) ? " + 
"(b('lon') <= 146.95569610595703) ? " + 
"(b('ndvi_med') <= 1751.0) ? " + 
"-0.0021490103718293393" + 
":  " + 
"0.005209265595769606" + 
":  " + 
"(b('ndvi') <= 1331.5) ? " + 
"0.11366069351042338" + 
":  " + 
"0.057011180780378035" + 
":  " + 
"(b('ndvi_med') <= 1538.0) ? " + 
"(b('crop') <= 13.148343086242676) ? " + 
"0.01585920352881492" + 
":  " + 
"6.0196454604112104e-05" + 
":  " + 
"(b('ndvi_med') <= 1554.5) ? " + 
"-0.019745739992170094" + 
":  " + 
"-6.025417747134935e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1708.5) ? " + 
"(b('L8b3') <= 1691.5) ? " + 
"(b('L8b1') <= 1085.0) ? " + 
"-2.5251630502670757e-05" + 
":  " + 
"-0.019017260878802032" + 
":  " + 
"(b('L8dt') <= 714325.0) ? " + 
"-0.01211696635101324" + 
":  " + 
"-0.043208663127165495" + 
":  " + 
"(b('L8b4') <= 2051.0) ? " + 
"(b('dgvh') <= -8.383004665374756) ? " + 
"0.0038151805487241786" + 
":  " + 
"0.07501833836862905" + 
":  " + 
"(b('L8dt') <= 4429550.5) ? " + 
"0.001590892900589775" + 
":  " + 
"-0.03404655894259781" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 4176.5) ? " + 
"(b('L8b6') <= 4820.0) ? " + 
"(b('L8b6') <= 4782.0) ? " + 
"1.1050911806759891e-05" + 
":  " + 
"0.026721350203718897" + 
":  " + 
"(b('L8dt') <= 1189024.0) ? " + 
"0.001855409620839934" + 
":  " + 
"-0.01979458107603205" + 
":  " + 
"(b('clay') <= 18.5) ? " + 
"(b('ndvi') <= 867.5) ? " + 
"0.04455821531156028" + 
":  " + 
"0.01591325266394377" + 
":  " + 
"(b('L8dt') <= 289239.5) ? " + 
"0.011027490826122116" + 
":  " + 
"-0.005556503160708279" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3533.0) ? " + 
"(b('L8b5') <= 3531.0) ? " + 
"(b('L8b5') <= 3450.5) ? " + 
"-1.1175225978147223e-05" + 
":  " + 
"0.006147251445469466" + 
":  " + 
"(b('dgvv') <= -0.38790225982666016) ? " + 
"-0.02207759157275534" + 
":  " + 
"0.06874641850249029" + 
":  " + 
"(b('L8b1') <= 344.5) ? " + 
"(b('L8b2') <= 438.5) ? " + 
"-6.180355111000861e-05" + 
":  " + 
"0.03102375896793179" + 
":  " + 
"(b('dgvv') <= 1.3796820640563965) ? " + 
"-0.0003712381990922107" + 
":  " + 
"-0.01547783127442338" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 939.5) ? " + 
"(b('L8b4') <= 1001.5) ? " + 
"(b('lon') <= 25.963054656982422) ? " + 
"0.001259530521093734" + 
":  " + 
"-0.005526377458746575" + 
":  " + 
"(b('L8b3med') <= 655.25) ? " + 
"0.0626445357220283" + 
":  " + 
"-0.004948217200971995" + 
":  " + 
"(b('L8b3') <= 945.5) ? " + 
"(b('L8b5') <= 3176.0) ? " + 
"0.02873621023589484" + 
":  " + 
"-0.060973770183644624" + 
":  " + 
"(b('L8b7') <= 1523.0) ? " + 
"-0.015341351691371723" + 
":  " + 
"0.00031925019438671303" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4762.5) ? " + 
"(b('ndvi') <= 5233.5) ? " + 
"(b('ndvi') <= 5165.0) ? " + 
"7.095773237039226e-06" + 
":  " + 
"0.02999993452842187" + 
":  " + 
"(b('L8b11') <= 1364.5) ? " + 
"-0.03061625519164734" + 
":  " + 
"-0.0008086767473910198" + 
":  " + 
"(b('ndvi') <= 5903.5) ? " + 
"(b('gvv') <= -12.17595386505127) ? " + 
"0.06330462912217262" + 
":  " + 
"0.019717305674662455" + 
":  " + 
"(b('dgvv') <= 0.7311115264892578) ? " + 
"0.006359101047307656" + 
":  " + 
"-0.006048081723132202" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -6.715389013290405) ? " + 
"(b('L8b3') <= 1277.5) ? " + 
"(b('dgvv') <= -7.834865093231201) ? " + 
"0.003292235404006867" + 
":  " + 
"-0.01070881118697109" + 
":  " + 
"(b('gvv') <= -13.589753150939941) ? " + 
"-0.04760609182323364" + 
":  " + 
"-0.05088659303988366" + 
":  " + 
"(b('bulk') <= 103.0) ? " + 
"(b('L8dt') <= 50834.0) ? " + 
"-0.044563326912926915" + 
":  " + 
"-0.009568063486760425" + 
":  " + 
"(b('ndvi') <= 2062.5) ? " + 
"-0.0004973326968435807" + 
":  " + 
"0.0004891080493179508" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1418.5) ? " + 
"(b('L8b4') <= 1825.5) ? " + 
"(b('L8b11') <= 3352.25) ? " + 
"7.834443431994761e-05" + 
":  " + 
"-0.04047247230958395" + 
":  " + 
"(b('L8b3') <= 1413.5) ? " + 
"-0.004949207659521811" + 
":  " + 
"-0.049073793122353" + 
":  " + 
"(b('L8b3') <= 1433.5) ? " + 
"(b('L8b3') <= 1432.5) ? " + 
"0.01983663004425805" + 
":  " + 
"0.16757946096491388" + 
":  " + 
"(b('lon') <= 146.3602294921875) ? " + 
"3.690727628673172e-05" + 
":  " + 
"0.042040554890818184" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.59345054626465) ? " + 
"(b('L8b6') <= 1881.0) ? " + 
"(b('L8b5') <= 1536.5) ? " + 
"0.011817911938041324" + 
":  " + 
"-0.013311549852048991" + 
":  " + 
"(b('L8b6') <= 1952.5) ? " + 
"0.023846673180748453" + 
":  " + 
"0.000443398172983563" + 
":  " + 
"(b('dgvh') <= -1.5272550582885742) ? " + 
"(b('lon') <= 0.756400004029274) ? " + 
"-0.00323908789515115" + 
":  " + 
"0.00043169185714604175" + 
":  " + 
"(b('L8dt') <= 2360298.5) ? " + 
"-0.04790044729380219" + 
":  " + 
"1.1479374300942674e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 3.218355178833008) ? " + 
"(b('dgvv') <= 3.249246597290039) ? " + 
"(b('dsvv') <= 3.213723659515381) ? " + 
"-7.721475781963484e-05" + 
":  " + 
"-0.08119565635741166" + 
":  " + 
"-0.13696644772351377" + 
":  " + 
"(b('sand') <= 43.5) ? " + 
"(b('moss') <= 0.04188481718301773) ? " + 
"0.03638870018549166" + 
":  " + 
"0.005261164645790612" + 
":  " + 
"(b('lon') <= -118.50275039672852) ? " + 
"-0.07254586053550038" + 
":  " + 
"-0.0018742948660350153" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 1594.5) ? " + 
"(b('L8b2') <= 566.0) ? " + 
"(b('L8b7') <= 1562.5) ? " + 
"0.0002631058337947418" + 
":  " + 
"-0.010170436252969749" + 
":  " + 
"(b('lon') <= -117.80759811401367) ? " + 
"0.028280959055608557" + 
":  " + 
"-0.0289018248707468" + 
":  " + 
"(b('L8b7') <= 1624.5) ? " + 
"(b('L8b2') <= 664.0) ? " + 
"0.00984838680839071" + 
":  " + 
"0.12706887537662875" + 
":  " + 
"(b('lat') <= 56.0489501953125) ? " + 
"9.133562373584243e-05" + 
":  " + 
"-0.06134269876726408" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 727.5) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"(b('ndvi') <= 2733.5) ? " + 
"0.003466821675915974" + 
":  " + 
"-0.0027494309096724404" + 
":  " + 
"(b('ndvi') <= 3377.0) ? " + 
"-0.027223272697024955" + 
":  " + 
"-0.0025024833183094615" + 
":  " + 
"(b('L8b3') <= 744.5) ? " + 
"(b('L8b5') <= 2469.0) ? " + 
"0.024305590979749887" + 
":  " + 
"-0.0026248936647329706" + 
":  " + 
"(b('L8b3') <= 752.5) ? " + 
"-0.009629508422137598" + 
":  " + 
"0.000159327172729055" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3042769.5) ? " + 
"(b('L8b5') <= 1430.0) ? " + 
"(b('L8b3') <= 560.0) ? " + 
"0.00019921419113952792" + 
":  " + 
"0.03675207393501692" + 
":  " + 
"(b('L8b7') <= 1339.5) ? " + 
"-0.002424408757839906" + 
":  " + 
"6.987370398603929e-05" + 
":  " + 
"(b('L8b11') <= 2835.5) ? " + 
"(b('ndvi_med') <= 1698.5) ? " + 
"0.018813893753151213" + 
":  " + 
"0.001663918425785693" + 
":  " + 
"(b('crop') <= 89.93249893188477) ? " + 
"-0.018055216990905343" + 
":  " + 
"0.010525462082932183" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.472105026245117) ? " + 
"(b('L8b6') <= 3629.5) ? " + 
"(b('L8b7') <= 2026.5) ? " + 
"-0.0023662617887712477" + 
":  " + 
"0.0022904765166257245" + 
":  " + 
"(b('lat') <= 41.77997970581055) ? " + 
"-0.0028450099802129277" + 
":  " + 
"-0.027929558589925765" + 
":  " + 
"(b('dsvv') <= 0.41945409774780273) ? " + 
"(b('lon') <= -5.4481751918792725) ? " + 
"0.014373080230818276" + 
":  " + 
"0.0009810455050592475" + 
":  " + 
"(b('gvv') <= -11.426303386688232) ? " + 
"-0.006121295837219828" + 
":  " + 
"-4.337009643960868e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -6.351504802703857) ? " + 
"(b('dgvh') <= -6.488469123840332) ? " + 
"(b('dsvh') <= -6.425196647644043) ? " + 
"-0.0001443394738358718" + 
":  " + 
"0.07983190022001457" + 
":  " + 
"(b('lat') <= -35.029008865356445) ? " + 
"-0.06503386169044534" + 
":  " + 
"-0.005125192828035714" + 
":  " + 
"(b('dgvh') <= -6.346902847290039) ? " + 
"(b('ndvi') <= 4904.5) ? " + 
"0.025709362390523325" + 
":  " + 
"0.13461454433333872" + 
":  " + 
"(b('clay') <= 28.5) ? " + 
"0.0011768163652423533" + 
":  " + 
"-0.0033435613722222904" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2990.5) ? " + 
"(b('dgvh') <= -9.15176773071289) ? " + 
"(b('moss') <= 12.958944320678711) ? " + 
"-0.004950492083453906" + 
":  " + 
"0.007916426864306547" + 
":  " + 
"(b('L8b7') <= 2927.5) ? " + 
"0.0002608175900145913" + 
":  " + 
"-0.006643834054710802" + 
":  " + 
"(b('L8b4') <= 1432.0) ? " + 
"(b('L8b4') <= 1423.0) ? " + 
"0.009905632161926067" + 
":  " + 
"0.20378455912978868" + 
":  " + 
"(b('L8b5') <= 2352.5) ? " + 
"-0.034742898426048996" + 
":  " + 
"0.0009613360757169279" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 876.5) ? " + 
"(b('L8dt') <= 1036565.5) ? " + 
"(b('dsvh') <= -9.876604080200195) ? " + 
"0.011461172555935671" + 
":  " + 
"-0.003412867800781972" + 
":  " + 
"(b('L8b6') <= 3327.5) ? " + 
"-0.017167563035456267" + 
":  " + 
"-0.06138751103156717" + 
":  " + 
"(b('L8b1') <= 1140.5) ? " + 
"(b('L8b2') <= 1377.5) ? " + 
"4.705564647016433e-05" + 
":  " + 
"-0.015195407571108472" + 
":  " + 
"(b('L8b1') <= 1162.5) ? " + 
"0.045734391080331276" + 
":  " + 
"0.00525688567660389" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 35512.5) ? " + 
"(b('ndvi') <= 2312.5) ? " + 
"(b('dsvh') <= -7.473391056060791) ? " + 
"-0.0008784533259842494" + 
":  " + 
"-0.018888996247368263" + 
":  " + 
"(b('L8b5') <= 3280.0) ? " + 
"0.006959504409630963" + 
":  " + 
"-0.016964157963146237" + 
":  " + 
"(b('L8dt') <= 103039.5) ? " + 
"(b('clay') <= 34.5) ? " + 
"0.0012084250183620065" + 
":  " + 
"0.022943749995451422" + 
":  " + 
"(b('L8dt') <= 125027.5) ? " + 
"-0.004994236383760901" + 
":  " + 
"0.00014365520641107572" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b6') <= 2659.5) ? " + 
"(b('L8b6') <= 2644.5) ? " + 
"0.000455023049330258" + 
":  " + 
"0.022023535329737932" + 
":  " + 
"(b('L8b6') <= 2690.5) ? " + 
"-0.0165839996954423" + 
":  " + 
"-0.0007768124510027629" + 
":  " + 
"(b('L8b6') <= 3467.5) ? " + 
"(b('L8b1') <= 500.5) ? " + 
"-0.0018021087465525918" + 
":  " + 
"0.012469415174391712" + 
":  " + 
"(b('L8b5') <= 2237.0) ? " + 
"-0.0199974681555616" + 
":  " + 
"0.00019879005609040775" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1137.5) ? " + 
"(b('ndvi') <= 1136.5) ? " + 
"(b('L8b2') <= 443.0) ? " + 
"-0.02970037066379919" + 
":  " + 
"-0.0009534210493079331" + 
":  " + 
"(b('L8b11') <= 2564.5) ? " + 
"-0.1092814688005322" + 
":  " + 
"-0.027672076200491235" + 
":  " + 
"(b('ndvi') <= 1154.5) ? " + 
"(b('lat') <= 41.222354888916016) ? " + 
"0.028467170909071384" + 
":  " + 
"0.0030699689526880614" + 
":  " + 
"(b('ndvi') <= 1156.0) ? " + 
"-0.047700391438545174" + 
":  " + 
"9.033488573215683e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 7.796026229858398) ? " + 
"(b('gvv') <= -6.22589373588562) ? " + 
"(b('gvv') <= -6.23303484916687) ? " + 
"4.2847153996386476e-05" + 
":  " + 
"0.10598748228704014" + 
":  " + 
"(b('L8b3med') <= 716.75) ? " + 
"-0.016790767910857127" + 
":  " + 
"-0.0014628184750489362" + 
":  " + 
"(b('dsvh') <= -3.571408271789551) ? " + 
"0.029712609361526754" + 
":  " + 
"0.04390777066937093" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2062.5) ? " + 
"(b('ndvi') <= 2058.5) ? " + 
"(b('ndvi_med') <= 2991.25) ? " + 
"-0.0007051327672489631" + 
":  " + 
"0.009215939686017381" + 
":  " + 
"(b('dgvv') <= 1.657846212387085) ? " + 
"-0.03685518155267365" + 
":  " + 
"-0.09914822924506066" + 
":  " + 
"(b('ndvi') <= 2063.5) ? " + 
"(b('gvv') <= -11.09424352645874) ? " + 
"0.12401938346272284" + 
":  " + 
"0.06923571905859931" + 
":  " + 
"(b('ndvi_med') <= 2145.0) ? " + 
"0.00397961059939912" + 
":  " + 
"-0.00042598011197020834" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2619.5) ? " + 
"(b('L8b4') <= 1582.5) ? " + 
"(b('L8b4') <= 1580.5) ? " + 
"5.470052479071575e-05" + 
":  " + 
"0.04048007302057825" + 
":  " + 
"(b('L8b3') <= 1228.5) ? " + 
"-0.012676811433576" + 
":  " + 
"-0.0009072357448513186" + 
":  " + 
"(b('L8b7') <= 2651.5) ? " + 
"(b('L8b4') <= 1890.5) ? " + 
"0.016859184575765154" + 
":  " + 
"-0.008674976469873393" + 
":  " + 
"(b('dsvh') <= -2.988497257232666) ? " + 
"-7.609369719375588e-05" + 
":  " + 
"0.021081790811129597" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 612.5) ? " + 
"(b('gvv') <= -12.332101345062256) ? " + 
"(b('L8b7') <= 1320.0) ? " + 
"0.005955634034885332" + 
":  " + 
"0.039881114087989014" + 
":  " + 
"(b('gvv') <= -10.44883108139038) ? " + 
"-0.008044894337506322" + 
":  " + 
"0.006093858354935188" + 
":  " + 
"(b('L8b4') <= 634.5) ? " + 
"(b('sand') <= 78.5) ? " + 
"-0.00327916042570849" + 
":  " + 
"-0.04541835905687195" + 
":  " + 
"(b('L8b4') <= 662.5) ? " + 
"0.006057771986039434" + 
":  " + 
"-9.567513847660207e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 65.5) ? " + 
"(b('ndvi') <= 2965.0) ? " + 
"(b('ndvi') <= 2739.5) ? " + 
"-7.628208158602382e-05" + 
":  " + 
"-0.008404353081511055" + 
":  " + 
"(b('clay') <= 21.5) ? " + 
"-0.0023925024987382533" + 
":  " + 
"0.0040788803532940026" + 
":  " + 
"(b('ndvi') <= 3336.0) ? " + 
"(b('L8b1') <= 446.0) ? " + 
"0.02011334229932817" + 
":  " + 
"-0.0005721478612145598" + 
":  " + 
"(b('moss') <= 12.735962390899658) ? " + 
"0.00010845849101776777" + 
":  " + 
"-0.030006756271599013" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 464.5) ? " + 
"(b('L8b6') <= 1057.0) ? " + 
"(b('dsvv') <= 0.30853796005249023) ? " + 
"0.02148438057955366" + 
":  " + 
"-0.0021454273832342352" + 
":  " + 
"(b('ndvi') <= 2341.0) ? " + 
"-0.004936501146253475" + 
":  " + 
"-0.016990221808039645" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"(b('gvv') <= -15.243398189544678) ? " + 
"0.055530153586963824" + 
":  " + 
"0.003585859163564267" + 
":  " + 
"(b('L8b1') <= 152.0) ? " + 
"0.06832895059465642" + 
":  " + 
"-8.549224168090027e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 727.5) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"(b('bulk') <= 153.5) ? " + 
"0.0002275176739199371" + 
":  " + 
"-0.014266283278667038" + 
":  " + 
"(b('L8dt') <= 665130.0) ? " + 
"-0.0031937818731280973" + 
":  " + 
"-0.02584696094923171" + 
":  " + 
"(b('L8b3') <= 743.5) ? " + 
"(b('L8b5') <= 2462.5) ? " + 
"0.022835941614123056" + 
":  " + 
"-0.002056115178518826" + 
":  " + 
"(b('L8b4') <= 697.5) ? " + 
"0.00814522181657978" + 
":  " + 
"-0.0001154385335293316" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1508.0) ? " + 
"(b('L8b3') <= 1497.5) ? " + 
"(b('L8b2') <= 1053.5) ? " + 
"-0.00017379621128194923" + 
":  " + 
"0.019129043833104178" + 
":  " + 
"(b('dgvv') <= 4.910737037658691) ? " + 
"-0.01822515672132921" + 
":  " + 
"-0.11426160359099426" + 
":  " + 
"(b('L8b3') <= 1531.0) ? " + 
"(b('L8b5') <= 2976.5) ? " + 
"0.029298145191633117" + 
":  " + 
"0.005766927318933038" + 
":  " + 
"(b('lat') <= -35.09726524353027) ? " + 
"0.06956911919708056" + 
":  " + 
"-0.0005561811075435785" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 3244.5) ? " + 
"(b('L8b7') <= 3184.0) ? " + 
"(b('L8b5') <= 3220.5) ? " + 
"0.0003891842930195151" + 
":  " + 
"-0.0017364443222228222" + 
":  " + 
"(b('L8b5') <= 3146.0) ? " + 
"-0.016186313904297714" + 
":  " + 
"0.009010539768543747" + 
":  " + 
"(b('dgvh') <= -2.7966628074645996) ? " + 
"(b('L8b7') <= 3296.5) ? " + 
"0.012744449572458466" + 
":  " + 
"0.0004585377533454875" + 
":  " + 
"(b('L8b4') <= 1992.0) ? " + 
"-0.022006413595561023" + 
":  " + 
"-0.0923374965871119" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1063.5) ? " + 
"(b('L8b3') <= 1055.5) ? " + 
"(b('L8b1') <= 670.5) ? " + 
"-0.00038834753001129184" + 
":  " + 
"0.011376139184365159" + 
":  " + 
"(b('clay') <= 23.5) ? " + 
"-0.011365641012435531" + 
":  " + 
"-0.036378818775877" + 
":  " + 
"(b('L8b4') <= 1354.5) ? " + 
"(b('L8b11') <= 2107.5) ? " + 
"0.015322469124768014" + 
":  " + 
"-0.001782604063755627" + 
":  " + 
"(b('L8b7') <= 1894.5) ? " + 
"0.015356618698563263" + 
":  " + 
"-0.0005127866256438904" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2908.5) ? " + 
"(b('L8b7') <= 2889.5) ? " + 
"(b('L8b6') <= 4220.0) ? " + 
"-1.791537131520278e-05" + 
":  " + 
"-0.01881730547179926" + 
":  " + 
"(b('crop') <= 80.98532485961914) ? " + 
"-0.005903481337305927" + 
":  " + 
"-0.03352944786261089" + 
":  " + 
"(b('L8b7') <= 2909.5) ? " + 
"(b('L8dt') <= 92589.0) ? " + 
"0.16186870670340991" + 
":  " + 
"0.036262180106842686" + 
":  " + 
"(b('ndvi') <= 1931.5) ? " + 
"-0.00086732005160072" + 
":  " + 
"0.006637026635246699" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3619.5) ? " + 
"(b('L8b6') <= 4618.5) ? " + 
"(b('L8b7') <= 2992.5) ? " + 
"-0.00042900550033156425" + 
":  " + 
"0.005218080737696629" + 
":  " + 
"(b('gvv') <= -12.772926330566406) ? " + 
"-0.0003584950833400102" + 
":  " + 
"-0.02570619485967803" + 
":  " + 
"(b('L8b6med') <= 3622.0) ? " + 
"(b('L8b6') <= 3361.5) ? " + 
"0.11048653858060462" + 
":  " + 
"-0.0037915606556209705" + 
":  " + 
"(b('gvv') <= -17.066712379455566) ? " + 
"-0.009161827207264269" + 
":  " + 
"0.001049723624041659" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4762.5) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4290.5) ? " + 
"1.2414765839069072e-05" + 
":  " + 
"0.014220657084399381" + 
":  " + 
"(b('ndvi') <= 6302.5) ? " + 
"-0.007996575213362386" + 
":  " + 
"0.025261090843389723" + 
":  " + 
"(b('ndvi') <= 5903.5) ? " + 
"(b('ndvi') <= 1986.5) ? " + 
"0.006573904602021743" + 
":  " + 
"0.039328254002847396" + 
":  " + 
"(b('dgvh') <= -4.724499702453613) ? " + 
"0.00683525422261557" + 
":  " + 
"-0.003620976136552396" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 4176.5) ? " + 
"(b('L8b5') <= 3190.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"0.00012432876492663182" + 
":  " + 
"0.019008170170082658" + 
":  " + 
"(b('bulk') <= 168.5) ? " + 
"-0.0009881857127676242" + 
":  " + 
"0.09267899547102837" + 
":  " + 
"(b('clay') <= 18.5) ? " + 
"(b('ndvi') <= 867.5) ? " + 
"0.04158613574005335" + 
":  " + 
"0.014863249221029906" + 
":  " + 
"(b('L8dt') <= 289239.5) ? " + 
"0.010580090120200211" + 
":  " + 
"-0.0045466647721220735" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 362.5) ? " + 
"(b('L8b2') <= 563.5) ? " + 
"(b('bulk') <= 153.5) ? " + 
"0.0012222864533272218" + 
":  " + 
"-0.01117415186788672" + 
":  " + 
"(b('ndvi') <= 1336.0) ? " + 
"0.008457924478837867" + 
":  " + 
"0.07605097140902772" + 
":  " + 
"(b('L8b1') <= 400.5) ? " + 
"(b('L8b4') <= 1116.5) ? " + 
"-0.007197903350154335" + 
":  " + 
"0.005478637174086044" + 
":  " + 
"(b('L8b2') <= 517.5) ? " + 
"0.006801464040432489" + 
":  " + 
"-7.284303286818667e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 22.5) ? " + 
"(b('ndvi') <= 3327.0) ? " + 
"(b('L8b11') <= 1261.75) ? " + 
"0.04260552166515596" + 
":  " + 
"0.00024657213704450814" + 
":  " + 
"(b('moss') <= 14.037330150604248) ? " + 
"-0.0011914441207333188" + 
":  " + 
"-0.0112783771840619" + 
":  " + 
"(b('ndvi') <= 2880.0) ? " + 
"(b('ndvi') <= 2867.0) ? " + 
"-0.0005373085366806432" + 
":  " + 
"-0.06359682532087013" + 
":  " + 
"(b('L8b6') <= 3463.5) ? " + 
"0.0026495828009439927" + 
":  " + 
"0.025236984366369973" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 477.5) ? " + 
"(b('L8b2') <= 447.5) ? " + 
"(b('L8b6') <= 2408.5) ? " + 
"0.0018732135521427242" + 
":  " + 
"-0.00417473261526119" + 
":  " + 
"(b('lat') <= 55.885250091552734) ? " + 
"0.002456930662847979" + 
":  " + 
"0.03288155183354741" + 
":  " + 
"(b('L8b3') <= 822.5) ? " + 
"(b('dgvv') <= 1.2409977912902832) ? " + 
"-0.001999241275889594" + 
":  " + 
"-0.015838605869814813" + 
":  " + 
"(b('L8b2') <= 484.5) ? " + 
"-0.016836513039932006" + 
":  " + 
"0.0003143866292896648" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1168.5) ? " + 
"(b('L8b2') <= 636.5) ? " + 
"(b('L8b2') <= 614.5) ? " + 
"0.0001623959428213609" + 
":  " + 
"-0.011552949305581092" + 
":  " + 
"(b('moss') <= 10.425388813018799) ? " + 
"0.001742379538858622" + 
":  " + 
"0.020824318188217963" + 
":  " + 
"(b('L8b4') <= 1169.5) ? " + 
"(b('dsvh') <= -5.200483322143555) ? " + 
"-0.04960518374426565" + 
":  " + 
"-0.10998415690526128" + 
":  " + 
"(b('L8b7') <= 1912.5) ? " + 
"0.006510361377525987" + 
":  " + 
"-0.00092272962745176" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1728.0) ? " + 
"(b('dgvv') <= 3.4883100986480713) ? " + 
"(b('gvv') <= -10.403301239013672) ? " + 
"-0.006950592793308249" + 
":  " + 
"0.007809876835193179" + 
":  " + 
"(b('dsvv') <= 4.209017992019653) ? " + 
"-0.05966617449715269" + 
":  " + 
"-0.013686132748224404" + 
":  " + 
"(b('L8b6') <= 1745.0) ? " + 
"(b('dsvh') <= -9.299202919006348) ? " + 
"-0.0010804108936601229" + 
":  " + 
"0.02605076879327407" + 
":  " + 
"(b('L8b6') <= 1750.5) ? " + 
"-0.028572033555913173" + 
":  " + 
"3.443746178248497e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 2.9752492904663086) ? " + 
"(b('dsvv') <= 2.9516441822052) ? " + 
"(b('dsvh') <= -1.5768170356750488) ? " + 
"-5.375862429877149e-05" + 
":  " + 
"-0.027642029274423108" + 
":  " + 
"(b('L8b7') <= 1436.5) ? " + 
"0.01844724483863091" + 
":  " + 
"-0.039297013132774145" + 
":  " + 
"(b('ndvi_med') <= 1212.25) ? " + 
"(b('L8b5') <= 2608.5) ? " + 
"0.08142609940956504" + 
":  " + 
"0.014462580430399961" + 
":  " + 
"(b('L8b7') <= 2080.5) ? " + 
"0.006196303196765058" + 
":  " + 
"-0.0038802746329439485" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1708.5) ? " + 
"(b('L8b3') <= 1691.5) ? " + 
"(b('L8b4med') <= 2360.5) ? " + 
"-8.815193305102215e-05" + 
":  " + 
"0.03204325908640952" + 
":  " + 
"(b('L8dt') <= 714325.0) ? " + 
"-0.01039398433222921" + 
":  " + 
"-0.03823861694004403" + 
":  " + 
"(b('L8b4') <= 2051.0) ? " + 
"(b('dgvh') <= -8.383004665374756) ? " + 
"0.00245451864856974" + 
":  " + 
"0.0668645172519908" + 
":  " + 
"(b('dsvh') <= -2.9954957962036133) ? " + 
"0.0008670915454726731" + 
":  " + 
"0.03986683117942571" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 7.336734771728516) ? " + 
"(b('moss') <= 4.7504541873931885) ? " + 
"(b('ndvi') <= 4418.0) ? " + 
"0.0002535859792333396" + 
":  " + 
"-0.005569267141897674" + 
":  " + 
"(b('L8b2') <= 483.0) ? " + 
"0.009668825759850718" + 
":  " + 
"0.0011641086093042102" + 
":  " + 
"(b('dgvh') <= -1.2315287590026855) ? " + 
"(b('dsvh') <= -9.732986450195312) ? " + 
"0.005785668403532851" + 
":  " + 
"-0.0007334920515701302" + 
":  " + 
"(b('sand') <= 33.5) ? " + 
"-0.1402685109458498" + 
":  " + 
"-0.021709108878156313" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 314.5) ? " + 
"(b('L8b1') <= 299.5) ? " + 
"(b('L8b6') <= 2321.5) ? " + 
"0.003281296485198354" + 
":  " + 
"-0.003945174617200831" + 
":  " + 
"(b('bulk') <= 106.5) ? " + 
"0.11869370226273" + 
":  " + 
"-0.008106643244847346" + 
":  " + 
"(b('L8b1') <= 352.5) ? " + 
"(b('ndvi') <= 2731.5) ? " + 
"0.013240365863975288" + 
":  " + 
"-0.00046007365026227645" + 
":  " + 
"(b('L8b3') <= 717.5) ? " + 
"-0.00565276566447547" + 
":  " + 
"8.84252089573451e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 1229.5) ? " + 
"(b('L8b7') <= 1224.0) ? " + 
"(b('ndvi_med') <= 1576.75) ? " + 
"0.017800744670214603" + 
":  " + 
"-0.002005436924074021" + 
":  " + 
"(b('ndvi') <= 5005.0) ? " + 
"-0.04607337269486406" + 
":  " + 
"-0.11265079084446439" + 
":  " + 
"(b('L8b4') <= 744.5) ? " + 
"(b('lon') <= -107.14787673950195) ? " + 
"0.019520937967864724" + 
":  " + 
"0.0012848286362930166" + 
":  " + 
"(b('L8b1') <= 199.0) ? " + 
"0.03750956447341299" + 
":  " + 
"-0.00022512964107009094" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('L8b11') <= 2365.0) ? " + 
"(b('L8b11') <= 2242.5) ? " + 
"-0.0012019176914144262" + 
":  " + 
"0.02548567442800573" + 
":  " + 
"(b('L8b5') <= 2359.0) ? " + 
"-0.0010086229642317587" + 
":  " + 
"-0.03251592463773431" + 
":  " + 
"(b('L8b3') <= 669.0) ? " + 
"(b('dsvv') <= 0.03764629364013672) ? " + 
"-0.0018167631727060542" + 
":  " + 
"0.031179315376069338" + 
":  " + 
"(b('L8b3med') <= 587.0) ? " + 
"0.016767214701596544" + 
":  " + 
"2.1915547671355403e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2794.5) ? " + 
"(b('L8b5') <= 2775.5) ? " + 
"(b('L8b6med') <= 4086.0) ? " + 
"-0.00023478516466166448" + 
":  " + 
"0.02010640191504211" + 
":  " + 
"(b('L8b4') <= 969.0) ? " + 
"0.007039935789544564" + 
":  " + 
"-0.02360788422180608" + 
":  " + 
"(b('L8b5') <= 2821.5) ? " + 
"(b('moss') <= 26.86719799041748) ? " + 
"0.009650984133516678" + 
":  " + 
"0.13276911162476326" + 
":  " + 
"(b('sand') <= 39.5) ? " + 
"0.0025241022254848663" + 
":  " + 
"-0.0013937812256820338" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2591.0) ? " + 
"(b('L8b1') <= 632.5) ? " + 
"(b('L8b7') <= 2571.5) ? " + 
"0.00016609053471095786" + 
":  " + 
"-0.02488399565824123" + 
":  " + 
"(b('L8b1') <= 702.5) ? " + 
"-0.007773686411230915" + 
":  " + 
"0.001248153540552991" + 
":  " + 
"(b('dsvh') <= -2.988497257232666) ? " + 
"(b('L8b11') <= 1624.5) ? " + 
"0.02730258212098167" + 
":  " + 
"0.0004184184564056193" + 
":  " + 
"(b('dsvh') <= -2.5628719329833984) ? " + 
"0.06032413687007076" + 
":  " + 
"-0.005667047703640827" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 1229.5) ? " + 
"(b('L8b7') <= 1224.0) ? " + 
"(b('clay') <= 23.5) ? " + 
"0.002129654254903825" + 
":  " + 
"-0.006090259250372794" + 
":  " + 
"(b('ndvi') <= 5005.0) ? " + 
"-0.04136106337201955" + 
":  " + 
"-0.10165692259080467" + 
":  " + 
"(b('L8b6') <= 1815.5) ? " + 
"(b('L8b6') <= 1775.0) ? " + 
"-0.0018675421314961397" + 
":  " + 
"0.04655281939471308" + 
":  " + 
"(b('L8b7') <= 1232.0) ? " + 
"0.044264501477271345" + 
":  " + 
"6.714384437707976e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2026.5) ? " + 
"(b('L8b2') <= 640.5) ? " + 
"(b('L8b4') <= 1482.0) ? " + 
"2.8951614232134662e-05" + 
":  " + 
"0.06104047382539072" + 
":  " + 
"(b('L8b7') <= 1919.5) ? " + 
"0.0012628130516939456" + 
":  " + 
"-0.0170100089951524" + 
":  " + 
"(b('L8b4') <= 1218.5) ? " + 
"(b('L8b3med') <= 1010.5) ? " + 
"0.0019455954613169049" + 
":  " + 
"0.018983126684848688" + 
":  " + 
"(b('L8b7') <= 2036.5) ? " + 
"0.03550993251086046" + 
":  " + 
"-0.000499255323348645" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1063.5) ? " + 
"(b('L8b3') <= 1055.5) ? " + 
"(b('ndvi_med') <= 1297.0) ? " + 
"-0.013269551943188889" + 
":  " + 
"-0.00016824573008371603" + 
":  " + 
"(b('L8b1') <= 538.5) ? " + 
"-0.028996854650650876" + 
":  " + 
"-0.007005888812922965" + 
":  " + 
"(b('L8b4') <= 1294.0) ? " + 
"(b('ndvi') <= 1731.0) ? " + 
"0.04579079913606451" + 
":  " + 
"0.006567612384581354" + 
":  " + 
"(b('L8b2') <= 590.5) ? " + 
"0.01894740125210797" + 
":  " + 
"-0.00015372365571136553" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.41945409774780273) ? " + 
"(b('dsvv') <= 0.41921091079711914) ? " + 
"(b('L8b5') <= 2794.5) ? " + 
"-0.0007228729072627679" + 
":  " + 
"0.0016841374502564682" + 
":  " + 
"0.10245996229380638" + 
":  " + 
"(b('L8b1') <= 497.5) ? " + 
"(b('L8b7') <= 2080.5) ? " + 
"-0.0012310152092640048" + 
":  " + 
"-0.013187266790587408" + 
":  " + 
"(b('L8b4') <= 1164.0) ? " + 
"0.00972210199323572" + 
":  " + 
"-0.0001840057146864071" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -1.9995975494384766) ? " + 
"(b('dgvh') <= -8.891875267028809) ? " + 
"(b('moss') <= 8.623376369476318) ? " + 
"-0.00810823894763059" + 
":  " + 
"0.007912593785649269" + 
":  " + 
"(b('L8b4') <= 1548.5) ? " + 
"-0.0011244341444873085" + 
":  " + 
"0.008523678399624271" + 
":  " + 
"(b('dgvv') <= -2.102396011352539) ? " + 
"0.11659061771054416" + 
":  " + 
"(b('dsvv') <= -1.9376583099365234) ? " + 
"0.011255253059402353" + 
":  " + 
"6.478736885858959e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 5695172.5) ? " + 
"(b('L8dt') <= 5486302.0) ? " + 
"(b('L8dt') <= 5247269.0) ? " + 
"-4.090864956752267e-05" + 
":  " + 
"0.013282741313657141" + 
":  " + 
"(b('ndvi') <= 1233.5) ? " + 
"0.021307815549900133" + 
":  " + 
"-0.04331064704350697" + 
":  " + 
"(b('ndvi') <= 5459.0) ? " + 
"(b('L8b1') <= 539.5) ? " + 
"0.014700314573631273" + 
":  " + 
"-0.0012262762967357014" + 
":  " + 
"-0.07153658699162684" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 699.75) ? " + 
"(b('ndvi') <= 3390.0) ? " + 
"(b('ndvi') <= 3358.5) ? " + 
"0.00661786206117012" + 
":  " + 
"0.08663276599366865" + 
":  " + 
"(b('moss') <= 14.397151947021484) ? " + 
"0.001790420594625341" + 
":  " + 
"-0.02436389182975588" + 
":  " + 
"(b('L8b3') <= 727.5) ? " + 
"(b('L8b5') <= 2209.5) ? " + 
"0.002871110104359363" + 
":  " + 
"-0.006337591446507868" + 
":  " + 
"(b('L8b3') <= 734.5) ? " + 
"0.012576825274226723" + 
":  " + 
"3.771817250123704e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 607.5) ? " + 
"(b('L8b5') <= 3092.5) ? " + 
"(b('L8dt') <= 228813.0) ? " + 
"0.00984020280597718" + 
":  " + 
"-0.004147063570776667" + 
":  " + 
"(b('L8b11') <= 1277.5) ? " + 
"-0.07349399622937171" + 
":  " + 
"-0.09880830121708586" + 
":  " + 
"(b('L8b3med') <= 565.0) ? " + 
"(b('L8b3') <= 668.0) ? " + 
"0.07324409030109157" + 
":  " + 
"0.015236710674783674" + 
":  " + 
"(b('L8b7') <= 997.0) ? " + 
"0.010507650086080192" + 
":  " + 
"-4.8345327662505505e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 35512.5) ? " + 
"(b('ndvi') <= 2396.5) ? " + 
"(b('L8b4med') <= 709.0) ? " + 
"-0.07796138700391367" + 
":  " + 
"-0.007811643531671237" + 
":  " + 
"(b('L8b6') <= 3337.5) ? " + 
"-0.0028805282874167443" + 
":  " + 
"0.022804851633363717" + 
":  " + 
"(b('L8dt') <= 103529.5) ? " + 
"(b('lat') <= 34.684539794921875) ? " + 
"0.012589587348091609" + 
":  " + 
"0.00022524008132660957" + 
":  " + 
"(b('L8dt') <= 124550.5) ? " + 
"-0.004593360559782866" + 
":  " + 
"0.00011355802123925277" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 38.5) ? " + 
"(b('dgvv') <= 2.9752492904663086) ? " + 
"(b('dsvv') <= 2.9516441822052) ? " + 
"-3.848645131987389e-05" + 
":  " + 
"-0.02299904443506326" + 
":  " + 
"(b('clay') <= 37.0) ? " + 
"0.0014260574540625362" + 
":  " + 
"0.06305323994956777" + 
":  " + 
"(b('gvv') <= -13.194663524627686) ? " + 
"(b('L8b4') <= 1354.5) ? " + 
"0.008925766672130893" + 
":  " + 
"-0.0202272147352469" + 
":  " + 
"(b('L8b1') <= 514.0) ? " + 
"-0.010693858277734194" + 
":  " + 
"-0.04267047416001861" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -6.22589373588562) ? " + 
"(b('gvv') <= -6.23303484916687) ? " + 
"(b('ndvi') <= 7065.0) ? " + 
"1.8187788486778664e-05" + 
":  " + 
"0.016539690089452053" + 
":  " + 
"0.09500326972249959" + 
":  " + 
"(b('lat') <= 41.39085006713867) ? " + 
"(b('dgvh') <= -6.87490701675415) ? " + 
"-0.022022749656556845" + 
":  " + 
"0.024854677139973115" + 
":  " + 
"(b('lon') <= -0.6403000056743622) ? " + 
"-0.025229925768102443" + 
":  " + 
"-0.003302631708072578" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1728.0) ? " + 
"(b('L8b6') <= 1686.5) ? " + 
"(b('L8b6') <= 1678.5) ? " + 
"-0.0024172895166170356" + 
":  " + 
"0.10130163591906217" + 
":  " + 
"(b('L8b11') <= 1702.5) ? " + 
"-0.0410447854209953" + 
":  " + 
"-0.0027438127706394407" + 
":  " + 
"(b('L8b6') <= 1745.0) ? " + 
"(b('L8dt') <= 238377.5) ? " + 
"0.07989620129093654" + 
":  " + 
"0.015616597225169174" + 
":  " + 
"(b('L8b2') <= 313.5) ? " + 
"0.005679317687333432" + 
":  " + 
"-6.3635450631994e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvh') <= 0.26318931579589844) ? " + 
"(b('dgvh') <= -0.7274341583251953) ? " + 
"(b('dsvh') <= -1.1070261001586914) ? " + 
"2.3830891135057904e-05" + 
":  " + 
"-0.02718735247812967" + 
":  " + 
"(b('crop') <= 46.676687240600586) ? " + 
"0.03840296924660891" + 
":  " + 
"-0.001900908405998257" + 
":  " + 
"(b('L8b4med') <= 1383.5) ? " + 
"(b('L8b6med') <= 2983.0) ? " + 
"-0.019930705693495795" + 
":  " + 
"0.037551011014540246" + 
":  " + 
"(b('L8b4med') <= 1486.5) ? " + 
"-0.06295791690201227" + 
":  " + 
"-0.025400127229527426" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -1.9995975494384766) ? " + 
"(b('lon') <= -116.70380401611328) ? " + 
"(b('L8b7') <= 2584.5) ? " + 
"0.019866112714784598" + 
":  " + 
"-0.014454626318886435" + 
":  " + 
"(b('crop') <= 76.83937072753906) ? " + 
"-0.0050295158525274115" + 
":  " + 
"0.002286043439770252" + 
":  " + 
"(b('dgvv') <= -2.102396011352539) ? " + 
"0.1049313640400717" + 
":  " + 
"(b('dsvv') <= -1.9376583099365234) ? " + 
"0.010174796798274294" + 
":  " + 
"6.13222327231355e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -121.13610458374023) ? " + 
"(b('L8dt') <= 1779308.0) ? " + 
"(b('dsvv') <= 1.2880163192749023) ? " + 
"0.008412708390377097" + 
":  " + 
"-0.018813325120798332" + 
":  " + 
"(b('ndvi') <= 1663.5) ? " + 
"-0.03966627715263433" + 
":  " + 
"-0.1067480071769003" + 
":  " + 
"(b('gvv') <= -15.07451581954956) ? " + 
"(b('ndvi_med') <= 1884.5) ? " + 
"0.000982013587080643" + 
":  " + 
"-0.005164517395792131" + 
":  " + 
"(b('gvv') <= -15.038439273834229) ? " + 
"0.03406046510091774" + 
":  " + 
"6.923642478951873e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -18.447688102722168) ? " + 
"(b('clay') <= 26.5) ? " + 
"(b('ndvi') <= 2666.0) ? " + 
"0.0040394130125791655" + 
":  " + 
"-0.029078418774484995" + 
":  " + 
"(b('dgvh') <= -7.703619480133057) ? " + 
"0.08036013797417267" + 
":  " + 
"0.015632629737295328" + 
":  " + 
"(b('gvv') <= -18.44324779510498) ? " + 
"-0.07560816482852613" + 
":  " + 
"(b('dsvv') <= -3.221768379211426) ? " + 
"-0.003549265300217949" + 
":  " + 
"4.8816392079928184e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -35.25544357299805) ? " + 
"(b('L8b3') <= 895.5) ? " + 
"(b('L8b1') <= 499.0) ? " + 
"0.012373243808986358" + 
":  " + 
"0.07598965878189953" + 
":  " + 
"(b('dgvh') <= -1.5524482727050781) ? " + 
"-0.004024533101795574" + 
":  " + 
"0.05894635206211338" + 
":  " + 
"(b('lat') <= -35.01868438720703) ? " + 
"(b('gvv') <= -16.177024841308594) ? " + 
"0.015158844930934312" + 
":  " + 
"-0.010364711560251759" + 
":  " + 
"(b('L8dt') <= 382067.5) ? " + 
"-0.0006355568662797005" + 
":  " + 
"0.000514128206439675" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 85.84851455688477) ? " + 
"(b('dsvv') <= 2.8495688438415527) ? " + 
"(b('dsvv') <= 2.8142433166503906) ? " + 
"3.197747136408723e-05" + 
":  " + 
"-0.029386863095934544" + 
":  " + 
"(b('dsvv') <= 2.8532066345214844) ? " + 
"0.0979544699919986" + 
":  " + 
"0.002790075363104906" + 
":  " + 
"(b('L8b1') <= 721.0) ? " + 
"(b('L8b2') <= 942.5) ? " + 
"-0.0009020084061897752" + 
":  " + 
"0.027834789238865117" + 
":  " + 
"(b('crop') <= 89.8235092163086) ? " + 
"-0.02319329453843876" + 
":  " + 
"-0.0024079615238470973" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.41397809982299805) ? " + 
"(b('ndvi') <= 3854.5) ? " + 
"(b('ndvi') <= 3745.0) ? " + 
"7.545427834992155e-05" + 
":  " + 
"-0.014535214042229717" + 
":  " + 
"(b('ndvi') <= 3943.0) ? " + 
"0.022339065819422434" + 
":  " + 
"0.0023713355537428467" + 
":  " + 
"(b('ndvi_med') <= 4921.5) ? " + 
"(b('L8dt') <= 887139.0) ? " + 
"-0.0017660111387525171" + 
":  " + 
"0.001925487533819894" + 
":  " + 
"(b('L8b3') <= 765.0) ? " + 
"0.0037546741669574803" + 
":  " + 
"-0.027035954798947152" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 2561.0) ? " + 
"(b('L8b2') <= 811.5) ? " + 
"(b('L8b2') <= 789.5) ? " + 
"-0.00011675402013258901" + 
":  " + 
"0.011075622347938104" + 
":  " + 
"(b('L8b7') <= 2352.0) ? " + 
"0.004239650932243452" + 
":  " + 
"-0.008758714226636391" + 
":  " + 
"(b('ndvi_med') <= 1733.5) ? " + 
"(b('L8b1') <= 478.5) ? " + 
"-0.024178128617432557" + 
":  " + 
"-0.00023744404394366572" + 
":  " + 
"(b('dsvh') <= -4.3114495277404785) ? " + 
"0.0026721031160788678" + 
":  " + 
"0.021208487936858842" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1370.0) ? " + 
"(b('dgvv') <= -0.3374648094177246) ? " + 
"(b('gvv') <= -14.271472930908203) ? " + 
"-0.0033361126130057317" + 
":  " + 
"0.008321481403988376" + 
":  " + 
"(b('L8b2') <= 291.5) ? " + 
"-0.057449518055539266" + 
":  " + 
"-0.000502662978143475" + 
":  " + 
"(b('L8b4') <= 2648.5) ? " + 
"(b('L8b2') <= 1139.5) ? " + 
"-0.0001179603723996802" + 
":  " + 
"-0.009084222740069063" + 
":  " + 
"(b('L8b5') <= 3665.5) ? " + 
"0.04716306516249125" + 
":  " + 
"0.0048995301479149355" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 5695172.5) ? " + 
"(b('L8dt') <= 5486302.0) ? " + 
"(b('L8b3') <= 1508.0) ? " + 
"-0.00020481400953088587" + 
":  " + 
"0.0011515326033193348" + 
":  " + 
"(b('gvv') <= -11.000389575958252) ? " + 
"-0.052859066911325504" + 
":  " + 
"0.0006389708405094702" + 
":  " + 
"(b('ndvi_med') <= 5338.5) ? " + 
"(b('L8b1') <= 539.5) ? " + 
"0.013562587065451558" + 
":  " + 
"-0.0011010629458510861" + 
":  " + 
"-0.06173269221043064" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5') <= 3479.5) ? " + 
"(b('L8b5') <= 3381.5) ? " + 
"0.00018704232494678273" + 
":  " + 
"-0.0034574660576359296" + 
":  " + 
"(b('L8b11') <= 1664.25) ? " + 
"-0.01248134594009354" + 
":  " + 
"0.018268923606575893" + 
":  " + 
"(b('L8b5') <= 3520.5) ? " + 
"(b('gvv') <= -11.849279880523682) ? " + 
"-0.027391359998693028" + 
":  " + 
"-0.07357007432374842" + 
":  " + 
"(b('L8b3') <= 895.5) ? " + 
"0.005723804909152466" + 
":  " + 
"-0.002631313687231379" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 1594.5) ? " + 
"(b('L8b2') <= 566.0) ? " + 
"(b('L8b7') <= 1562.5) ? " + 
"0.00026048978354730173" + 
":  " + 
"-0.00951464115187672" + 
":  " + 
"(b('L8dt') <= 622900.5) ? " + 
"0.004037773888967645" + 
":  " + 
"-0.031905621906985954" + 
":  " + 
"(b('L8b7') <= 1624.5) ? " + 
"(b('L8b5') <= 3289.5) ? " + 
"0.003909739291718168" + 
":  " + 
"0.03562418339673372" + 
":  " + 
"(b('lat') <= 56.0489501953125) ? " + 
"8.458165971514282e-05" + 
":  " + 
"-0.052529070701974406" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 876.5) ? " + 
"(b('bulk') <= 141.0) ? " + 
"(b('dsvh') <= -7.183012962341309) ? " + 
"-0.029592180544048732" + 
":  " + 
"0.03103367567574346" + 
":  " + 
"(b('gvv') <= -9.302560329437256) ? " + 
"0.00028116142741165255" + 
":  " + 
"-0.013098457587316651" + 
":  " + 
"(b('L8b1') <= 1140.5) ? " + 
"(b('L8b2') <= 1377.5) ? " + 
"4.485890977655261e-05" + 
":  " + 
"-0.014310917218275484" + 
":  " + 
"(b('gvv') <= -9.3058443069458) ? " + 
"0.006566444495511099" + 
":  " + 
"0.07608157233260063" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 314.5) ? " + 
"(b('L8b4') <= 1208.5) ? " + 
"(b('L8b3') <= 1019.0) ? " + 
"-0.0009160552807306002" + 
":  " + 
"0.07962281199110716" + 
":  " + 
"(b('lon') <= -63.178314208984375) ? " + 
"-0.09128094427591776" + 
":  " + 
"-0.022112361540282774" + 
":  " + 
"(b('L8b1') <= 359.5) ? " + 
"(b('L8b5') <= 3900.0) ? " + 
"0.003954416461662197" + 
":  " + 
"-0.06986835733697097" + 
":  " + 
"(b('L8b1') <= 399.5) ? " + 
"-0.004195240292564987" + 
":  " + 
"0.00022406340543289422" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvh') <= -9.112457275390625) ? " + 
"(b('dsvv') <= 0.6705317497253418) ? " + 
"(b('dsvv') <= -2.0489444732666016) ? " + 
"-0.0046609980871206306" + 
":  " + 
"0.002098628821429328" + 
":  " + 
"(b('clay') <= 23.5) ? " + 
"-0.007934888284103" + 
":  " + 
"-0.025458039270820805" + 
":  " + 
"(b('dsvh') <= -9.096367359161377) ? " + 
"(b('dsvh') <= -9.103642463684082) ? " + 
"0.010911895962212523" + 
":  " + 
"0.07344907234912632" + 
":  " + 
"(b('moss') <= 7.336734771728516) ? " + 
"0.0007643684870241094" + 
":  " + 
"-0.0005710596834664889" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 38.5) ? " + 
"(b('L8b3') <= 1004.5) ? " + 
"(b('L8b4') <= 1172.5) ? " + 
"0.0001290631670360631" + 
":  " + 
"-0.00445272723934711" + 
":  " + 
"(b('L8b7') <= 1928.0) ? " + 
"0.007610259574625446" + 
":  " + 
"-2.8003799856131052e-05" + 
":  " + 
"(b('dgvv') <= 0.7557668685913086) ? " + 
"(b('L8b5') <= 2180.0) ? " + 
"0.012636359369914673" + 
":  " + 
"-0.008008381312461973" + 
":  " + 
"(b('L8b1') <= 523.0) ? " + 
"-0.015921505054368054" + 
":  " + 
"-0.04591482302600811" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3190.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"(b('L8b5') <= 3187.5) ? " + 
"6.165429439842815e-05" + 
":  " + 
"0.018487400881785" + 
":  " + 
"(b('dgvh') <= -5.333315372467041) ? " + 
"0.004474383956948579" + 
":  " + 
"0.05354812407770076" + 
":  " + 
"(b('L8b7') <= 2429.5) ? " + 
"(b('L8b3') <= 1261.5) ? " + 
"-0.001603085495862114" + 
":  " + 
"-0.018538049944608097" + 
":  " + 
"(b('L8b3med') <= 1332.0) ? " + 
"0.006660514628319491" + 
":  " + 
"-0.0010979080116094474" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -6.22589373588562) ? " + 
"(b('gvv') <= -6.23303484916687) ? " + 
"(b('ndvi') <= 7065.0) ? " + 
"1.8269904579698812e-05" + 
":  " + 
"0.015364110872069724" + 
":  " + 
"0.08578743844799983" + 
":  " + 
"(b('lat') <= 41.39085006713867) ? " + 
"(b('sand') <= 50.0) ? " + 
"-0.0064399947520196975" + 
":  " + 
"0.02644273728640499" + 
":  " + 
"(b('lon') <= -0.6403000056743622) ? " + 
"-0.023275652557550496" + 
":  " + 
"-0.003161700655555534" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4762.5) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4169.5) ? " + 
"-3.1112445113572804e-06" + 
":  " + 
"0.007375384124669489" + 
":  " + 
"(b('gvv') <= -13.280883312225342) ? " + 
"0.002474507796384049" + 
":  " + 
"-0.011722082459257278" + 
":  " + 
"(b('dgvv') <= 1.85280179977417) ? " + 
"(b('L8dt') <= 541527.0) ? " + 
"0.017333378047922357" + 
":  " + 
"0.056422741787028496" + 
":  " + 
"(b('L8b7') <= 1335.0) ? " + 
"0.02546136048527539" + 
":  " + 
"0.0025513390709077884" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1137.5) ? " + 
"(b('ndvi') <= 1132.5) ? " + 
"(b('L8dt') <= 36772.0) ? " + 
"0.021164498905609046" + 
":  " + 
"-0.0013240030829171365" + 
":  " + 
"(b('dsvh') <= -6.613880157470703) ? " + 
"-0.02217255180031168" + 
":  " + 
"-0.09832693840155482" + 
":  " + 
"(b('ndvi') <= 1154.5) ? " + 
"(b('sand') <= 44.5) ? " + 
"0.02913015093090545" + 
":  " + 
"0.004740480420827369" + 
":  " + 
"(b('ndvi') <= 1156.0) ? " + 
"-0.04113794102797653" + 
":  " + 
"7.541096501976794e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 826.5) ? " + 
"(b('lat') <= -35.07992362976074) ? " + 
"(b('L8b2') <= 463.0) ? " + 
"-0.0023827619232768596" + 
":  " + 
"-0.04840136876318881" + 
":  " + 
"(b('L8b7') <= 2945.5) ? " + 
"-0.0005257609539635283" + 
":  " + 
"0.04099919133149706" + 
":  " + 
"(b('L8b4') <= 946.5) ? " + 
"(b('lat') <= 43.94677543640137) ? " + 
"0.01895487473216589" + 
":  " + 
"0.0014799666190135291" + 
":  " + 
"(b('L8b7') <= 1651.5) ? " + 
"-0.00842679164943671" + 
":  " + 
"0.00022509964127993774" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= 0.2746467590332031) ? " + 
"(b('dsvh') <= -0.7264900207519531) ? " + 
"(b('dgvh') <= -1.1112289428710938) ? " + 
"2.2981756980296086e-05" + 
":  " + 
"-0.024846629669624924" + 
":  " + 
"(b('moss') <= 1.2583333253860474) ? " + 
"0.03252930425105944" + 
":  " + 
"-0.008004551508711367" + 
":  " + 
"(b('L8b4med') <= 1383.5) ? " + 
"(b('L8b3med') <= 979.0) ? " + 
"-0.02077947778295537" + 
":  " + 
"0.033579056849060214" + 
":  " + 
"(b('L8b4med') <= 1486.5) ? " + 
"-0.057424260130675225" + 
":  " + 
"-0.024070686729755136" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 730.5) ? " + 
"(b('L8b4med') <= 829.0) ? " + 
"(b('L8b5') <= 1903.5) ? " + 
"0.00959750491609576" + 
":  " + 
"-0.00048004936996626896" + 
":  " + 
"(b('L8b3') <= 748.5) ? " + 
"-0.004356374734250404" + 
":  " + 
"0.15264844340675945" + 
":  " + 
"(b('L8b5') <= 1898.5) ? " + 
"(b('lon') <= -5.326294898986816) ? " + 
"0.0018932635341725019" + 
":  " + 
"-0.011409327997728733" + 
":  " + 
"(b('L8b5') <= 1904.0) ? " + 
"0.08210458484507224" + 
":  " + 
"-1.1658797970010958e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.472105026245117) ? " + 
"(b('L8b6') <= 3629.5) ? " + 
"(b('bulk') <= 129.5) ? " + 
"-0.006454880459589985" + 
":  " + 
"0.0010012941529528713" + 
":  " + 
"(b('lon') <= -105.1441421508789) ? " + 
"0.00018994595787658863" + 
":  " + 
"-0.010369934804925037" + 
":  " + 
"(b('L8dt') <= 581648.5) ? " + 
"(b('L8b7') <= 1444.5) ? " + 
"-0.0033394001974198406" + 
":  " + 
"0.002839773138803291" + 
":  " + 
"(b('ndvi') <= 885.0) ? " + 
"-0.035878305174513694" + 
":  " + 
"-0.0005439367157896197" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 715.5) ? " + 
"(b('L8b5') <= 3774.5) ? " + 
"(b('ndvi_med') <= 2928.0) ? " + 
"0.005920017526480467" + 
":  " + 
"-0.0004022934880162552" + 
":  " + 
"(b('lat') <= 42.56540107727051) ? " + 
"0.07668201498491994" + 
":  " + 
"-0.051482665938870666" + 
":  " + 
"(b('L8b4') <= 717.5) ? " + 
"(b('dgvh') <= -6.228463172912598) ? " + 
"-0.0017049071571282087" + 
":  " + 
"-0.05220777319896608" + 
":  " + 
"(b('L8b1') <= 255.5) ? " + 
"-0.008993653171349678" + 
":  " + 
"7.790225531975454e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3042769.5) ? " + 
"(b('L8b3med') <= 557.5) ? " + 
"(b('L8b7') <= 1348.0) ? " + 
"-0.03658671428506411" + 
":  " + 
"0.005864659670818843" + 
":  " + 
"(b('L8dt') <= 2916892.0) ? " + 
"-1.2558439327831368e-05" + 
":  " + 
"-0.008902194463908664" + 
":  " + 
"(b('L8dt') <= 3045071.0) ? " + 
"(b('gvv') <= -10.13068675994873) ? " + 
"0.05055816433167353" + 
":  " + 
"0.07222689176768236" + 
":  " + 
"(b('lat') <= 37.94038963317871) ? " + 
"-0.02632231255809007" + 
":  " + 
"0.0022503179943675023" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 612.5) ? " + 
"(b('gvv') <= -12.314494609832764) ? " + 
"(b('dsvh') <= -6.6433210372924805) ? " + 
"-0.0040118088714995205" + 
":  " + 
"0.01668739925200643" + 
":  " + 
"(b('gvv') <= -12.299822330474854) ? " + 
"-0.14593733797987854" + 
":  " + 
"-0.0008467340266164012" + 
":  " + 
"(b('L8b3') <= 607.5) ? " + 
"(b('clay') <= 8.5) ? " + 
"-0.02124326981749495" + 
":  " + 
"-0.00010541312489930603" + 
":  " + 
"(b('L8b3med') <= 587.0) ? " + 
"0.018440765313280434" + 
":  " + 
"-4.3020119597050496e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -8.796432495117188) ? " + 
"(b('gvv') <= -8.863539218902588) ? " + 
"(b('gvv') <= -8.869343757629395) ? " + 
"-9.430419500241188e-05" + 
":  " + 
"0.06938336162240104" + 
":  " + 
"(b('L8b4med') <= 1966.5) ? " + 
"-0.018076026312148764" + 
":  " + 
"0.008813353200971735" + 
":  " + 
"(b('gvv') <= -8.79248571395874) ? " + 
"(b('dsvh') <= -5.345668792724609) ? " + 
"6.98843514129674e-05" + 
":  " + 
"0.08307950420522643" + 
":  " + 
"(b('lon') <= 26.74935531616211) ? " + 
"0.0020973434329365124" + 
":  " + 
"-0.011689901687970109" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 88.85982513427734) ? " + 
"(b('gvv') <= -9.360228061676025) ? " + 
"(b('L8b7') <= 1339.5) ? " + 
"-0.0029022295961966104" + 
":  " + 
"0.00016507659154164106" + 
":  " + 
"(b('lon') <= 26.74935531616211) ? " + 
"0.0031423878349245253" + 
":  " + 
"-0.009903310735609249" + 
":  " + 
"(b('dsvh') <= -4.89664363861084) ? " + 
"(b('L8b4') <= 1892.5) ? " + 
"0.0026337583332597062" + 
":  " + 
"-0.004910212855199321" + 
":  " + 
"(b('ndvi') <= 6542.0) ? " + 
"-0.012582689033127755" + 
":  " + 
"0.059338036059757404" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 756.5) ? " + 
"(b('ndvi_med') <= 1579.75) ? " + 
"(b('L8b3') <= 702.0) ? " + 
"0.0037693609890162515" + 
":  " + 
"0.05401301126425201" + 
":  " + 
"(b('L8b4') <= 751.5) ? " + 
"0.0002305649751246764" + 
":  " + 
"0.016251190664459514" + 
":  " + 
"(b('L8b6med') <= 2124.5) ? " + 
"(b('L8b7') <= 1756.0) ? " + 
"-0.026315840358723187" + 
":  " + 
"0.007707759025752588" + 
":  " + 
"(b('L8b4med') <= 685.0) ? " + 
"0.008942565167536267" + 
":  " + 
"-0.00021532047294159132" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 50341.0) ? " + 
"(b('L8dt') <= 38977.0) ? " + 
"(b('L8dt') <= 38969.5) ? " + 
"-3.7698256189936e-05" + 
":  " + 
"0.10065693358327468" + 
":  " + 
"(b('L8dt') <= 39972.0) ? " + 
"-0.03881726771262641" + 
":  " + 
"-0.0030383361243193937" + 
":  " + 
"(b('L8dt') <= 50416.0) ? " + 
"(b('dsvh') <= -5.421163558959961) ? " + 
"0.019935054310785134" + 
":  " + 
"0.15504073478782981" + 
":  " + 
"(b('L8dt') <= 103039.5) ? " + 
"0.0033881612124063197" + 
":  " + 
"-8.411976263041693e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 3244.5) ? " + 
"(b('L8b11') <= 3352.25) ? " + 
"(b('L8b6') <= 3892.5) ? " + 
"0.0001343434807646765" + 
":  " + 
"-0.0026277588504479074" + 
":  " + 
"(b('L8b7') <= 3193.5) ? " + 
"-0.026080853750100642" + 
":  " + 
"0.029052132558884683" + 
":  " + 
"(b('L8b3') <= 1274.0) ? " + 
"(b('L8dt') <= 27295.0) ? " + 
"-0.13471091807403635" + 
":  " + 
"-0.014796397286636953" + 
":  " + 
"(b('L8b5') <= 2877.0) ? " + 
"0.01821892166979719" + 
":  " + 
"0.0008817371459180466" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 5247269.0) ? " + 
"(b('L8dt') <= 5075596.0) ? " + 
"(b('L8b4') <= 612.5) ? " + 
"0.002432586620349811" + 
":  " + 
"-0.0001197328025429266" + 
":  " + 
"(b('sand') <= 42.5) ? " + 
"-0.011722516860804885" + 
":  " + 
"-0.041019878702494836" + 
":  " + 
"(b('sand') <= 25.0) ? " + 
"(b('L8b7') <= 1667.5) ? " + 
"0.10885481488481004" + 
":  " + 
"-0.02087429678639917" + 
":  " + 
"(b('sand') <= 77.0) ? " + 
"-0.0019334812453082936" + 
":  " + 
"0.020120089284896715" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3508.75) ? " + 
"(b('L8b6') <= 2659.5) ? " + 
"(b('L8b6') <= 2643.5) ? " + 
"0.00045358771596038915" + 
":  " + 
"0.018040282629117256" + 
":  " + 
"(b('L8b6') <= 2660.5) ? " + 
"-0.04307537069682124" + 
":  " + 
"-0.0009630489046557437" + 
":  " + 
"(b('L8b3') <= 705.0) ? " + 
"(b('L8b2') <= 443.5) ? " + 
"-0.006744593045269586" + 
":  " + 
"-0.09095251447153624" + 
":  " + 
"(b('L8b4') <= 783.0) ? " + 
"0.03582387501126351" + 
":  " + 
"0.0008831905780056237" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -9.137753009796143) ? " + 
"(b('dgvv') <= 0.7428970336914062) ? " + 
"(b('L8dt') <= 586046.5) ? " + 
"0.003238614072602946" + 
":  " + 
"-0.0032154536536762594" + 
":  " + 
"(b('clay') <= 23.5) ? " + 
"-0.006764730238309607" + 
":  " + 
"-0.030174626219269158" + 
":  " + 
"(b('dgvh') <= -9.13132381439209) ? " + 
"(b('lat') <= 39.00896072387695) ? " + 
"0.023859394354402628" + 
":  " + 
"0.07776465456356324" + 
":  " + 
"(b('dgvv') <= -2.633321762084961) ? " + 
"0.004220637945578098" + 
":  " + 
"3.7365036672197274e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3369578.0) ? " + 
"(b('L8dt') <= 3346463.0) ? " + 
"(b('L8dt') <= 3327042.0) ? " + 
"-7.435069197673767e-05" + 
":  " + 
"0.04720953633899208" + 
":  " + 
"(b('L8b4med') <= 1896.5) ? " + 
"-0.01873338566504263" + 
":  " + 
"-0.09550195036347718" + 
":  " + 
"(b('clay') <= 34.5) ? " + 
"(b('lat') <= 41.32645606994629) ? " + 
"0.013054736212254222" + 
":  " + 
"0.00016294861579922585" + 
":  " + 
"-0.11406073366746997" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2043.5) ? " + 
"(b('L8b3med') <= 1316.75) ? " + 
"(b('crop') <= 97.10931015014648) ? " + 
"0.0028516643538032426" + 
":  " + 
"-0.02658093220566962" + 
":  " + 
"(b('clay') <= 19.0) ? " + 
"-0.06494801371414453" + 
":  " + 
"-0.010269209903323475" + 
":  " + 
"(b('L8b5') <= 2068.5) ? " + 
"(b('dgvh') <= -4.564844608306885) ? " + 
"-0.008133219151648385" + 
":  " + 
"-0.05082800716711631" + 
":  " + 
"(b('L8b5') <= 2069.5) ? " + 
"0.08698918879997752" + 
":  " + 
"-4.334949083774296e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1373.5) ? " + 
"(b('ndvi') <= 1361.5) ? " + 
"(b('lon') <= 146.95569610595703) ? " + 
"9.30573269089938e-05" + 
":  " + 
"0.08411221236350734" + 
":  " + 
"(b('L8b4') <= 954.0) ? " + 
"-0.020491148516167804" + 
":  " + 
"0.021633233517450952" + 
":  " + 
"(b('ndvi') <= 1479.5) ? " + 
"(b('L8b6med') <= 3754.5) ? " + 
"-0.01088534067334394" + 
":  " + 
"0.005357490772445294" + 
":  " + 
"(b('ndvi') <= 1481.5) ? " + 
"0.04369953118037533" + 
":  " + 
"0.0001275603485638136" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -6.715389013290405) ? " + 
"(b('ndvi') <= 3271.0) ? " + 
"(b('L8dt') <= 1232137.0) ? " + 
"-0.04010524161101589" + 
":  " + 
"-0.043057692706000905" + 
":  " + 
"(b('L8b6med') <= 2371.0) ? " + 
"-0.010771662188398354" + 
":  " + 
"0.005094729098068771" + 
":  " + 
"(b('L8b3') <= 826.5) ? " + 
"(b('L8b3') <= 805.5) ? " + 
"-4.249969034643614e-05" + 
":  " + 
"-0.006824488312585647" + 
":  " + 
"(b('L8b4') <= 946.5) ? " + 
"0.0052907737043442074" + 
":  " + 
"-9.475189224112815e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5') <= 3471.5) ? " + 
"(b('L8b5') <= 3385.5) ? " + 
"0.00016520934827690526" + 
":  " + 
"-0.003538700387076913" + 
":  " + 
"(b('clay') <= 13.5) ? " + 
"-0.042245542718638576" + 
":  " + 
"0.014598099142240388" + 
":  " + 
"(b('L8b5') <= 3520.5) ? " + 
"(b('gvv') <= -11.849279880523682) ? " + 
"-0.02404075574876514" + 
":  " + 
"-0.06566425603363278" + 
":  " + 
"(b('L8b3') <= 895.5) ? " + 
"0.005166312253929604" + 
":  " + 
"-0.0024799470291770914" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 939.5) ? " + 
"(b('lon') <= -120.2534408569336) ? " + 
"(b('dgvh') <= -4.770719051361084) ? " + 
"-0.00170059147893227" + 
":  " + 
"-0.04433291496993012" + 
":  " + 
"(b('L8b3med') <= 964.5) ? " + 
"-0.000798908544996125" + 
":  " + 
"0.0035617135870165684" + 
":  " + 
"(b('L8b3') <= 945.5) ? " + 
"(b('L8b6med') <= 2983.0) ? " + 
"0.0330628358370094" + 
":  " + 
"-0.013801070418309028" + 
":  " + 
"(b('L8b3med') <= 693.0) ? " + 
"-0.0320915664071199" + 
":  " + 
"0.00018218477401363395" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -121.92677688598633) ? " + 
"(b('gvv') <= -12.414659976959229) ? " + 
"(b('ndvi') <= 1352.0) ? " + 
"0.0008388688101829945" + 
":  " + 
"0.03187485023083046" + 
":  " + 
"(b('L8b6') <= 1677.0) ? " + 
"-0.07645212589536399" + 
":  " + 
"-0.011503781823513288" + 
":  " + 
"(b('L8b7') <= 4176.5) ? " + 
"(b('L8b6') <= 4820.0) ? " + 
"7.830670279488493e-07" + 
":  " + 
"-0.005148305580656487" + 
":  " + 
"(b('L8b4med') <= 1877.5) ? " + 
"0.022091601790809087" + 
":  " + 
"0.006027403578333899" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 4342.0) ? " + 
"(b('L8b6') <= 4295.5) ? " + 
"(b('L8b6') <= 4264.0) ? " + 
"-7.824380534100898e-05" + 
":  " + 
"0.007649834894988714" + 
":  " + 
"(b('gvv') <= -13.54757308959961) ? " + 
"0.00690263319346813" + 
":  " + 
"-0.02014864728531484" + 
":  " + 
"(b('L8b6') <= 4346.5) ? " + 
"(b('dsvh') <= -6.928178787231445) ? " + 
"0.08604798934063054" + 
":  " + 
"0.009462142258652627" + 
":  " + 
"(b('dsvv') <= 1.3357510566711426) ? " + 
"0.0031153071583333875" + 
":  " + 
"-0.012952220602986009" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1190.5) ? " + 
"(b('L8dt') <= 36772.0) ? " + 
"(b('lat') <= 40.962100982666016) ? " + 
"0.0020392059120636075" + 
":  " + 
"0.051273432014395284" + 
":  " + 
"(b('L8b2') <= 774.5) ? " + 
"-0.006857702052370041" + 
":  " + 
"-0.00016462523826100346" + 
":  " + 
"(b('ndvi') <= 1216.5) ? " + 
"(b('L8b5') <= 2131.0) ? " + 
"-0.01381000119903997" + 
":  " + 
"0.016792878146930746" + 
":  " + 
"(b('ndvi_med') <= 1075.5) ? " + 
"-0.016204600721885246" + 
":  " + 
"7.528143400879097e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 50848.5) ? " + 
"(b('bulk') <= 153.5) ? " + 
"(b('bulk') <= 151.5) ? " + 
"-0.0020395997270289488" + 
":  " + 
"-0.022692515196036867" + 
":  " + 
"(b('gvv') <= -10.996897220611572) ? " + 
"0.0035010271922375573" + 
":  " + 
"0.03670172319091436" + 
":  " + 
"(b('L8dt') <= 63268.0) ? " + 
"(b('lon') <= -5.422399997711182) ? " + 
"0.003151687048916851" + 
":  " + 
"0.04790026742808518" + 
":  " + 
"(b('L8dt') <= 63281.0) ? " + 
"-0.015735836615931822" + 
":  " + 
"0.0001176998918493657" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2043.5) ? " + 
"(b('L8b3') <= 1094.0) ? " + 
"(b('L8b3med') <= 1316.75) ? " + 
"0.0015748971968694847" + 
":  " + 
"-0.016302533210741762" + 
":  " + 
"(b('dgvh') <= -7.936768054962158) ? " + 
"0.005841602522573151" + 
":  " + 
"0.042512145694064446" + 
":  " + 
"(b('L8b5') <= 2068.5) ? " + 
"(b('L8b6med') <= 3715.5) ? " + 
"-0.010460171125123588" + 
":  " + 
"0.04188459969177716" + 
":  " + 
"(b('L8b5') <= 2069.5) ? " + 
"0.07833358171507543" + 
":  " + 
"-5.4899728262736687e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -8.234763145446777) ? " + 
"(b('moss') <= 16.83380126953125) ? " + 
"(b('lon') <= 25.963054656982422) ? " + 
"-0.0018679875692198904" + 
":  " + 
"0.005183679292457107" + 
":  " + 
"(b('L8b2') <= 781.5) ? " + 
"0.02355492333505009" + 
":  " + 
"-0.0008236135557557901" + 
":  " + 
"(b('dgvh') <= -8.230491161346436) ? " + 
"(b('ndvi') <= 1649.0) ? " + 
"0.0637478811953009" + 
":  " + 
"-0.001960293646046312" + 
":  " + 
"(b('dsvh') <= -8.078860759735107) ? " + 
"0.004942552375984959" + 
":  " + 
"3.3918407086180225e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 65.5) ? " + 
"(b('ndvi') <= 4321.0) ? " + 
"(b('ndvi_med') <= 4189.5) ? " + 
"-0.0002705740766679958" + 
":  " + 
"-0.015282303004594367" + 
":  " + 
"(b('moss') <= 5.082603454589844) ? " + 
"-0.002860835239137652" + 
":  " + 
"0.008070154044398177" + 
":  " + 
"(b('ndvi') <= 3100.5) ? " + 
"(b('L8b1') <= 446.0) ? " + 
"0.029168593699979824" + 
":  " + 
"-0.00051279659640413" + 
":  " + 
"(b('moss') <= 12.735962390899658) ? " + 
"-0.00026538393791011687" + 
":  " + 
"-0.013067236299834282" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1004.5) ? " + 
"(b('dgvh') <= -2.8319411277770996) ? " + 
"(b('L8b5') <= 2546.0) ? " + 
"0.001033307969351251" + 
":  " + 
"-0.001495300841880558" + 
":  " + 
"(b('L8b4') <= 1246.0) ? " + 
"-0.005646667359382232" + 
":  " + 
"-0.057415243463659976" + 
":  " + 
"(b('L8b7') <= 1937.5) ? " + 
"(b('L8b6med') <= 2257.0) ? " + 
"-0.01623508444219783" + 
":  " + 
"0.010423292469302538" + 
":  " + 
"(b('L8b7') <= 1955.0) ? " + 
"-0.03222193714513802" + 
":  " + 
"9.404642571982726e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2122105.5) ? " + 
"(b('L8b6med') <= 3484.5) ? " + 
"(b('L8b5') <= 3385.5) ? " + 
"-0.00016359223889322603" + 
":  " + 
"-0.004103411583809996" + 
":  " + 
"(b('L8b6') <= 3511.5) ? " + 
"0.003769155469693221" + 
":  " + 
"-0.0003124222833871392" + 
":  " + 
"(b('L8dt') <= 2139526.5) ? " + 
"(b('L8b6med') <= 3530.0) ? " + 
"0.0469570253265724" + 
":  " + 
"-0.00785827373729316" + 
":  " + 
"(b('lon') <= 22.981159210205078) ? " + 
"0.0018967948338724134" + 
":  " + 
"-0.009889508023432867" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1418.5) ? " + 
"(b('L8b1') <= 752.5) ? " + 
"(b('L8b1') <= 731.5) ? " + 
"-0.00016783705720793777" + 
":  " + 
"0.015294832858798037" + 
":  " + 
"(b('sand') <= 46.5) ? " + 
"-0.013786296791934383" + 
":  " + 
"0.004507035225841958" + 
":  " + 
"(b('L8b3') <= 1433.5) ? " + 
"(b('lon') <= -5.284249782562256) ? " + 
"0.028980942238299463" + 
":  " + 
"-0.050975654481307975" + 
":  " + 
"(b('dsvh') <= -5.619801998138428) ? " + 
"-0.0006991026045374315" + 
":  " + 
"0.008857805683021877" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1508.0) ? " + 
"(b('L8b3') <= 1497.5) ? " + 
"(b('L8b3') <= 1493.5) ? " + 
"-0.00013774900466070826" + 
":  " + 
"0.020135913340497306" + 
":  " + 
"(b('gvv') <= -10.09725284576416) ? " + 
"-0.011233811476771797" + 
":  " + 
"-0.051937416493981675" + 
":  " + 
"(b('L8b4') <= 2020.0) ? " + 
"(b('L8b3') <= 1519.0) ? " + 
"0.03352323090200185" + 
":  " + 
"0.00638126076264751" + 
":  " + 
"(b('L8b5') <= 3309.5) ? " + 
"-0.004347010659133915" + 
":  " + 
"0.003448173720873108" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1708.5) ? " + 
"(b('L8b2') <= 971.5) ? " + 
"(b('L8b2') <= 960.5) ? " + 
"3.6731620739205776e-05" + 
":  " + 
"0.017509569073589457" + 
":  " + 
"(b('L8b5') <= 3845.0) ? " + 
"-0.004045533843971154" + 
":  " + 
"0.023393898425748967" + 
":  " + 
"(b('L8b4') <= 2051.0) ? " + 
"(b('dgvh') <= -8.383004665374756) ? " + 
"0.002238473654688193" + 
":  " + 
"0.059429658172517504" + 
":  " + 
"(b('L8dt') <= 2253076.0) ? " + 
"0.0017495337291199668" + 
":  " + 
"-0.012566838401607227" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4045.5) ? " + 
"(b('L8b5') <= 4031.0) ? " + 
"(b('ndvi') <= 5233.5) ? " + 
"0.0001251014920277848" + 
":  " + 
"-0.0027689897699396566" + 
":  " + 
"(b('ndvi_med') <= 2256.5) ? " + 
"0.008905859190416855" + 
":  " + 
"0.08815463098440124" + 
":  " + 
"(b('L8b5') <= 4051.5) ? " + 
"(b('dsvh') <= -5.944215774536133) ? " + 
"-0.03953637688674962" + 
":  " + 
"-0.07972541204234801" + 
":  " + 
"(b('ndvi') <= 6364.5) ? " + 
"-0.003436661925323216" + 
":  " + 
"0.03735289234923279" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4med') <= 718.0) ? " + 
"(b('ndvi') <= 2336.0) ? " + 
"(b('L8b7') <= 1400.0) ? " + 
"-0.04364160274662046" + 
":  " + 
"-0.00046427148756716865" + 
":  " + 
"(b('ndvi') <= 2346.0) ? " + 
"0.0507282338194954" + 
":  " + 
"0.0027544647602556456" + 
":  " + 
"(b('L8dt') <= 4817392.5) ? " + 
"(b('L8b3') <= 613.0) ? " + 
"-0.005044243387159173" + 
":  " + 
"-5.3842561733219676e-05" + 
":  " + 
"(b('gvv') <= -11.675329208374023) ? " + 
"0.024729699739602914" + 
":  " + 
"-0.00018309785895634476" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 715.5) ? " + 
"(b('dgvv') <= 2.566814661026001) ? " + 
"(b('L8b3med') <= 880.0) ? " + 
"0.0016849961034130464" + 
":  " + 
"-0.005423947509044742" + 
":  " + 
"(b('bulk') <= 149.5) ? " + 
"0.01764949439411328" + 
":  " + 
"-0.015674249789993586" + 
":  " + 
"(b('L8b4') <= 717.5) ? " + 
"(b('dsvh') <= -6.230070114135742) ? " + 
"-0.002024371590053789" + 
":  " + 
"-0.04719147027939549" + 
":  " + 
"(b('L8b1') <= 255.5) ? " + 
"-0.007799756944020202" + 
":  " + 
"6.36447001437247e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 22.5) ? " + 
"(b('L8b1') <= 344.5) ? " + 
"(b('L8b2') <= 504.5) ? " + 
"0.002114267659489486" + 
":  " + 
"0.055277795616001234" + 
":  " + 
"(b('L8b1') <= 404.0) ? " + 
"-0.0068400216442685725" + 
":  " + 
"-0.0003225334926567727" + 
":  " + 
"(b('ndvi') <= 3424.0) ? " + 
"(b('L8b1') <= 314.5) ? " + 
"-0.006700860444757167" + 
":  " + 
"0.0005660676078982044" + 
":  " + 
"(b('crop') <= 66.54314804077148) ? " + 
"0.009870590726459438" + 
":  " + 
"-0.0048544573822336436" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 477.5) ? " + 
"(b('ndvi') <= 1999.0) ? " + 
"(b('L8b4med') <= 704.5) ? " + 
"-0.025498031003755566" + 
":  " + 
"0.008370642950299654" + 
":  " + 
"(b('L8b2') <= 476.5) ? " + 
"-0.0002497880931615328" + 
":  " + 
"0.02155753591485489" + 
":  " + 
"(b('L8b1') <= 409.5) ? " + 
"(b('L8b6') <= 1894.5) ? " + 
"-0.05237694934000447" + 
":  " + 
"-0.002717956951246689" + 
":  " + 
"(b('L8b1') <= 410.5) ? " + 
"0.03562557840378068" + 
":  " + 
"7.96056777979844e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1168.5) ? " + 
"(b('ndvi_med') <= 1361.5) ? " + 
"(b('dgvh') <= -5.948042869567871) ? " + 
"0.03004652620365084" + 
":  " + 
"-0.007388865277449599" + 
":  " + 
"(b('L8b2') <= 700.0) ? " + 
"-1.9447471222324533e-05" + 
":  " + 
"0.010200679292769852" + 
":  " + 
"(b('L8b4') <= 1169.5) ? " + 
"(b('dsvh') <= -5.200483322143555) ? " + 
"-0.04300242040144294" + 
":  " + 
"-0.09650367605617852" + 
":  " + 
"(b('L8b5') <= 2208.5) ? " + 
"-0.005682587475007529" + 
":  " + 
"0.00023138280242989507" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3533.0) ? " + 
"(b('L8b5') <= 3531.0) ? " + 
"(b('L8b5') <= 3450.5) ? " + 
"-2.6429073156630507e-06" + 
":  " + 
"0.005023489351641962" + 
":  " + 
"(b('gvv') <= -11.015426635742188) ? " + 
"-0.02121260013641404" + 
":  " + 
"0.056588525554100905" + 
":  " + 
"(b('dgvv') <= 1.1607327461242676) ? " + 
"(b('dsvv') <= 1.1764116287231445) ? " + 
"0.0003262607255281395" + 
":  " + 
"0.17939359698126742" + 
":  " + 
"(b('L8b4') <= 670.5) ? " + 
"0.039801558596786274" + 
":  " + 
"-0.009134165482702381" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4762.5) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 3846.0) ? " + 
"-5.165791506815102e-05" + 
":  " + 
"0.0026294526266965666" + 
":  " + 
"(b('L8b3') <= 1036.0) ? " + 
"-0.023144768698869906" + 
":  " + 
"-0.002657248595839011" + 
":  " + 
"(b('dsvv') <= 1.8524069786071777) ? " + 
"(b('L8dt') <= 541527.0) ? " + 
"0.016428194402543842" + 
":  " + 
"0.05096667191098424" + 
":  " + 
"(b('lat') <= 41.31007957458496) ? " + 
"0.02558616759999227" + 
":  " + 
"0.002726563985282284" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 3892.5) ? " + 
"(b('L8b6') <= 3888.5) ? " + 
"(b('L8b7') <= 2993.5) ? " + 
"-0.00012056262572654876" + 
":  " + 
"0.005857538036869607" + 
":  " + 
"(b('ndvi_med') <= 2324.5) ? " + 
"0.014579054474904537" + 
":  " + 
"0.10592134568687084" + 
":  " + 
"(b('L8b6') <= 3893.5) ? " + 
"(b('L8dt') <= 290759.5) ? " + 
"-0.06335011720979644" + 
":  " + 
"-0.09119100189389176" + 
":  " + 
"(b('dgvh') <= -4.868512153625488) ? " + 
"-0.0016368617895438217" + 
":  " + 
"0.010183888761456062" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 314.5) ? " + 
"(b('L8dt') <= 1757672.5) ? " + 
"(b('ndvi') <= 5604.0) ? " + 
"0.004736410649513335" + 
":  " + 
"0.07007521042600194" + 
":  " + 
"(b('L8dt') <= 1780209.0) ? " + 
"-0.10839855122686373" + 
":  " + 
"-0.00629938174769476" + 
":  " + 
"(b('L8b1') <= 152.0) ? " + 
"(b('gvv') <= -10.601109504699707) ? " + 
"0.05798503326197523" + 
":  " + 
"0.06290240787131698" + 
":  " + 
"(b('L8b1') <= 253.5) ? " + 
"-0.004349518313597665" + 
":  " + 
"4.547900662602183e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -1.97100830078125) ? " + 
"(b('L8dt') <= 884439.5) ? " + 
"(b('crop') <= 76.83937072753906) ? " + 
"-0.001444734065260934" + 
":  " + 
"0.006887849191769572" + 
":  " + 
"(b('lat') <= 47.19705009460449) ? " + 
"-0.01056418880242084" + 
":  " + 
"0.0015350859698653803" + 
":  " + 
"(b('dgvv') <= -1.9608802795410156) ? " + 
"(b('L8b7') <= 2136.5) ? " + 
"-0.006159411303930577" + 
":  " + 
"0.06764175764156592" + 
":  " + 
"(b('dsvv') <= -1.9376583099365234) ? " + 
"0.012104486714340171" + 
":  " + 
"5.603387820186795e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 295.5) ? " + 
"(b('L8b1') <= 292.5) ? " + 
"(b('dsvv') <= -0.0005025863647460938) ? " + 
"0.004560363718244494" + 
":  " + 
"-0.002481806284852272" + 
":  " + 
"(b('L8b4') <= 784.75) ? " + 
"-0.006566523745078025" + 
":  " + 
"0.04792225151665436" + 
":  " + 
"(b('L8b1') <= 314.5) ? " + 
"(b('ndvi') <= 3422.0) ? " + 
"-0.010189046202353598" + 
":  " + 
"0.005200094121244088" + 
":  " + 
"(b('L8b1') <= 329.5) ? " + 
"0.0053832954058595246" + 
":  " + 
"-8.510628687774035e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 4627.5) ? " + 
"(b('ndvi') <= 4607.0) ? " + 
"(b('ndvi_med') <= 4777.75) ? " + 
"-1.7781562899279087e-05" + 
":  " + 
"0.01521327282850266" + 
":  " + 
"(b('L8b7') <= 1158.0) ? " + 
"-0.015013736977244337" + 
":  " + 
"0.037391367347961196" + 
":  " + 
"(b('L8b3') <= 892.0) ? " + 
"(b('L8dt') <= 1539331.0) ? " + 
"-0.010788062785556324" + 
":  " + 
"0.005051133505135708" + 
":  " + 
"(b('L8b6') <= 2780.0) ? " + 
"0.015742078635564826" + 
":  " + 
"-0.002529725178785034" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 464.5) ? " + 
"(b('L8b2') <= 459.5) ? " + 
"(b('L8b6') <= 2410.5) ? " + 
"0.0019034867532408514" + 
":  " + 
"-0.0029467221331752635" + 
":  " + 
"(b('L8b5') <= 1711.0) ? " + 
"0.1963403549720759" + 
":  " + 
"0.015782745305002642" + 
":  " + 
"(b('L8b6') <= 2502.0) ? " + 
"(b('L8b1') <= 403.5) ? " + 
"-0.010144246138006354" + 
":  " + 
"0.0008804764324365596" + 
":  " + 
"(b('L8b5') <= 1539.5) ? " + 
"-0.08643696125974966" + 
":  " + 
"0.0002143698406333105" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -6.351504802703857) ? " + 
"(b('dgvh') <= -6.791726589202881) ? " + 
"(b('dsvh') <= -6.805658340454102) ? " + 
"8.80298041834239e-05" + 
":  " + 
"0.020871893355470544" + 
":  " + 
"(b('dsvh') <= -6.732064723968506) ? " + 
"-0.011308246731314631" + 
":  " + 
"-0.0017409811890996888" + 
":  " + 
"(b('L8b11') <= 3276.0) ? " + 
"(b('ndvi') <= 1373.5) ? " + 
"0.005795049571728874" + 
":  " + 
"0.000265033042629662" + 
":  " + 
"(b('dgvv') <= 1.0319304466247559) ? " + 
"0.0038658640463185164" + 
":  " + 
"-0.018613361791872327" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1154.5) ? " + 
"(b('L8b4') <= 1144.5) ? " + 
"(b('ndvi_med') <= 1547.75) ? " + 
"0.009203220873317462" + 
":  " + 
"-0.00011332582759723056" + 
":  " + 
"(b('moss') <= 12.0119047164917) ? " + 
"0.007302205347744371" + 
":  " + 
"0.060529723861272436" + 
":  " + 
"(b('L8b5') <= 2208.5) ? " + 
"(b('L8b3') <= 1071.0) ? " + 
"-0.009142255500050551" + 
":  " + 
"0.005102924301133227" + 
":  " + 
"(b('L8b5') <= 2249.5) ? " + 
"0.015496823208633501" + 
":  " + 
"-0.0001656814744799358" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -15.07451581954956) ? " + 
"(b('clay') <= 26.5) ? " + 
"(b('sand') <= 43.5) ? " + 
"-0.009248782619199161" + 
":  " + 
"-0.00019543068372637824" + 
":  " + 
"(b('L8b5') <= 2231.5) ? " + 
"0.014094540031598194" + 
":  " + 
"-0.0005297147435658117" + 
":  " + 
"(b('gvv') <= -15.02292776107788) ? " + 
"(b('gvv') <= -15.02381944656372) ? " + 
"0.017391903942462445" + 
":  " + 
"0.11512832096092017" + 
":  " + 
"(b('clay') <= 29.5) ? " + 
"0.000278913717763597" + 
":  " + 
"-0.0023572783554094644" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvh') <= -8.244302749633789) ? " + 
"(b('moss') <= 12.878343105316162) ? " + 
"(b('moss') <= 10.661625862121582) ? " + 
"-0.0014277168189761383" + 
":  " + 
"-0.011807968277349846" + 
":  " + 
"(b('dsvv') <= 0.10538148880004883) ? " + 
"0.005514372184928673" + 
":  " + 
"-0.006678764061165972" + 
":  " + 
"(b('dsvh') <= -8.078860759735107) ? " + 
"(b('L8b5') <= 2022.5) ? " + 
"-0.011649890415926444" + 
":  " + 
"0.007098120872975462" + 
":  " + 
"(b('clay') <= 20.5) ? " + 
"-0.0011697687957513284" + 
":  " + 
"0.0007498306518407776" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 103.0) ? " + 
"(b('L8dt') <= 50834.0) ? " + 
"(b('L8b1') <= 545.0) ? " + 
"-0.043619673659471975" + 
":  " + 
"-0.029583053178305264" + 
":  " + 
"(b('L8b3') <= 1074.0) ? " + 
"0.0005247462892957389" + 
":  " + 
"-0.01610848046099817" + 
":  " + 
"(b('gvv') <= -11.414001941680908) ? " + 
"(b('dsvv') <= 2.2117323875427246) ? " + 
"-7.649867504806103e-05" + 
":  " + 
"-0.009199017051197552" + 
":  " + 
"(b('bulk') <= 158.5) ? " + 
"0.0003601016009925461" + 
":  " + 
"0.02000959486794192" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1772.0) ? " + 
"(b('ndvi') <= 2101.5) ? " + 
"(b('L8b1') <= 497.5) ? " + 
"-0.005636354715992425" + 
":  " + 
"-0.0003495776849351653" + 
":  " + 
"(b('lon') <= -5.486745119094849) ? " + 
"0.010503224305346462" + 
":  " + 
"-0.0013010989739509228" + 
":  " + 
"(b('ndvi') <= 1804.5) ? " + 
"(b('ndvi_med') <= 2991.25) ? " + 
"0.003710206021056267" + 
":  " + 
"0.02577208492169532" + 
":  " + 
"(b('ndvi') <= 1872.5) ? " + 
"-0.009832096353767071" + 
":  " + 
"-0.0001406119374072268" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 464.5) ? " + 
"(b('L8b1') <= 142.5) ? " + 
"(b('dsvh') <= -6.076297760009766) ? " + 
"0.013089333178236882" + 
":  " + 
"-0.006316006531554595" + 
":  " + 
"(b('dgvh') <= -7.434535503387451) ? " + 
"-0.021405705251274748" + 
":  " + 
"-0.006036683110354661" + 
":  " + 
"(b('L8b3') <= 490.5) ? " + 
"(b('L8dt') <= 1814375.0) ? " + 
"0.0410891373220951" + 
":  " + 
"-0.016371967053937373" + 
":  " + 
"(b('L8b3') <= 506.5) ? " + 
"-0.02042956373331055" + 
":  " + 
"1.2013923271763973e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvv') <= -18.447688102722168) ? " + 
"(b('clay') <= 26.5) ? " + 
"(b('L8b6') <= 2380.0) ? " + 
"-0.03214084580948037" + 
":  " + 
"0.003118073443627769" + 
":  " + 
"(b('dgvh') <= -7.703619480133057) ? " + 
"0.0712232393683104" + 
":  " + 
"0.013935411051436853" + 
":  " + 
"(b('gvv') <= -18.413028717041016) ? " + 
"(b('ndvi') <= 1924.0) ? " + 
"-0.07304549194286425" + 
":  " + 
"0.004586509448914512" + 
":  " + 
"(b('dsvv') <= -3.221768379211426) ? " + 
"-0.003190691493558285" + 
":  " + 
"5.079834721189641e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7') <= 4351.0) ? " + 
"(b('L8b6') <= 4860.5) ? " + 
"(b('L8b6') <= 4342.0) ? " + 
"-7.745921411759188e-05" + 
":  " + 
"0.00303106076261277" + 
":  " + 
"(b('L8dt') <= 986148.0) ? " + 
"0.004768776057672376" + 
":  " + 
"-0.020231068043226035" + 
":  " + 
"(b('L8b7') <= 4399.5) ? " + 
"(b('L8dt') <= 777585.0) ? " + 
"0.030522339361169534" + 
":  " + 
"0.0070952701281664235" + 
":  " + 
"(b('ndvi') <= 1498.5) ? " + 
"0.0057009881137833965" + 
":  " + 
"-0.007490345848888767" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3042769.5) ? " + 
"(b('L8b3med') <= 557.5) ? " + 
"(b('L8b7') <= 1348.0) ? " + 
"-0.030662630792294587" + 
":  " + 
"0.003395522082740991" + 
":  " + 
"(b('L8b5') <= 1430.0) ? " + 
"0.007076826094450007" + 
":  " + 
"-0.00010329285864019723" + 
":  " + 
"(b('bulk') <= 129.5) ? " + 
"(b('gvv') <= -8.712647438049316) ? " + 
"0.015226455411476998" + 
":  " + 
"-0.007917485988048627" + 
":  " + 
"(b('lat') <= 41.32645606994629) ? " + 
"0.009184570508159033" + 
":  " + 
"-0.0028993343864226044" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 727.5) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"(b('L8b1') <= 372.5) ? " + 
"0.0008430175281949429" + 
":  " + 
"-0.005445636493346669" + 
":  " + 
"(b('L8b7') <= 1546.5) ? " + 
"-0.01621629166274698" + 
":  " + 
"0.009969648047143084" + 
":  " + 
"(b('L8b4') <= 803.5) ? " + 
"(b('L8b5') <= 3769.5) ? " + 
"0.004950897803318774" + 
":  " + 
"-0.016716737352464966" + 
":  " + 
"(b('L8b4') <= 809.5) ? " + 
"-0.01638538923563371" + 
":  " + 
"-5.394022095249113e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 6128.0) ? " + 
"(b('ndvi') <= 5975.5) ? " + 
"(b('ndvi_med') <= 6045.25) ? " + 
"-1.553212059648173e-05" + 
":  " + 
"0.04354072048466961" + 
":  " + 
"(b('lon') <= -38.15167808532715) ? " + 
"-0.010222664623779746" + 
":  " + 
"0.032323999545689465" + 
":  " + 
"(b('sand') <= 40.0) ? " + 
"(b('dgvh') <= -5.571438789367676) ? " + 
"-0.003295191267131527" + 
":  " + 
"0.03760592447550073" + 
":  " + 
"(b('ndvi') <= 6780.5) ? " + 
"-0.01879097499890929" + 
":  " + 
"0.0030848909021592933" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3189.5) ? " + 
"(b('ndvi_med') <= 4878.5) ? " + 
"(b('L8b5') <= 3187.5) ? " + 
"6.1029998835549936e-05" + 
":  " + 
"0.01782124663740415" + 
":  " + 
"(b('dgvh') <= -6.593605995178223) ? " + 
"-0.0034405451914398173" + 
":  " + 
"0.03531110494892671" + 
":  " + 
"(b('bulk') <= 168.5) ? " + 
"(b('L8b5') <= 3257.5) ? " + 
"-0.006222067209011891" + 
":  " + 
"1.2202955357737967e-05" + 
":  " + 
"(b('dgvh') <= -9.115730285644531) ? " + 
"0.05854030743651267" + 
":  " + 
"0.10077183720313351" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.41945409774780273) ? " + 
"(b('dgvh') <= -3.1938037872314453) ? " + 
"(b('dsvh') <= -3.3229475021362305) ? " + 
"0.00027756066034411825" + 
":  " + 
"-0.040284787111336366" + 
":  " + 
"(b('L8b6med') <= 2960.5) ? " + 
"0.04249331526783609" + 
":  " + 
"-0.007115640893091712" + 
":  " + 
"(b('L8b1') <= 453.5) ? " + 
"(b('lon') <= -120.3383903503418) ? " + 
"-0.016692179975347436" + 
":  " + 
"-0.0017244232890327943" + 
":  " + 
"(b('L8b7') <= 2241.5) ? " + 
"0.005558738369424832" + 
":  " + 
"-0.0008622797083547181" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1') <= 362.5) ? " + 
"(b('bulk') <= 153.5) ? " + 
"(b('lon') <= -115.47969818115234) ? " + 
"0.020945288728339662" + 
":  " + 
"0.000791089142685188" + 
":  " + 
"(b('ndvi') <= 3241.5) ? " + 
"-0.020591703070006167" + 
":  " + 
"0.008469026565187951" + 
":  " + 
"(b('L8b1') <= 383.5) ? " + 
"(b('L8b7') <= 1346.0) ? " + 
"0.01348757425296855" + 
":  " + 
"-0.007755872260162409" + 
":  " + 
"(b('L8b1') <= 384.5) ? " + 
"0.028060112423885487" + 
":  " + 
"-2.5122682567796356e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -121.92677688598633) ? " + 
"(b('gvv') <= -12.414659976959229) ? " + 
"(b('ndvi') <= 1352.0) ? " + 
"0.0006798501720923412" + 
":  " + 
"0.028639196746066964" + 
":  " + 
"(b('L8b5') <= 2650.5) ? " + 
"-0.0516490840014899" + 
":  " + 
"-0.00509004631864094" + 
":  " + 
"(b('L8b5') <= 2043.5) ? " + 
"(b('L8b2') <= 776.0) ? " + 
"0.0004718584501365889" + 
":  " + 
"0.020333248321935078" + 
":  " + 
"(b('L8b5') <= 2056.5) ? " + 
"-0.012007276301678272" + 
":  " + 
"-9.81275684869628e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 657.5) ? " + 
"(b('L8b2') <= 654.5) ? " + 
"(b('L8b4') <= 1638.5) ? " + 
"0.00020316533187806095" + 
":  " + 
"-0.023861821784911256" + 
":  " + 
"(b('L8b4') <= 1105.0) ? " + 
"0.04698029113285394" + 
":  " + 
"0.004924505839759125" + 
":  " + 
"(b('L8b6') <= 2126.0) ? " + 
"(b('L8dt') <= 294870.0) ? " + 
"0.037051574329696024" + 
":  " + 
"-0.052399271505090377" + 
":  " + 
"(b('bulk') <= 125.0) ? " + 
"0.016814868841213294" + 
":  " + 
"-0.0004445332750031456" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.31694984436035) ? " + 
"(b('L8b5') <= 2895.5) ? " + 
"(b('ndvi_med') <= 1733.5) ? " + 
"-0.0005914323050278464" + 
":  " + 
"0.004890254415828201" + 
":  " + 
"(b('lat') <= 43.18190002441406) ? " + 
"-0.001311641351908606" + 
":  " + 
"0.021321883906310662" + 
":  " + 
"(b('L8b3') <= 1471.0) ? " + 
"(b('L8b2') <= 837.5) ? " + 
"-0.00030377232986913386" + 
":  " + 
"-0.00987247836725969" + 
":  " + 
"(b('gvv') <= -10.486175537109375) ? " + 
"0.003739831369741054" + 
":  " + 
"0.03201142086871207" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3416.5) ? " + 
"(b('L8b1') <= 557.5) ? " + 
"(b('L8b6') <= 3742.5) ? " + 
"0.00014774991832831037" + 
":  " + 
"0.027405272546570273" + 
":  " + 
"(b('lon') <= 9.09754991531372) ? " + 
"-0.0030566658361853415" + 
":  " + 
"0.007490398993607067" + 
":  " + 
"(b('L8b5') <= 2456.5) ? " + 
"(b('L8b3') <= 1216.0) ? " + 
"0.0017329065727636947" + 
":  " + 
"0.033857296390680316" + 
":  " + 
"(b('moss') <= 20.356952667236328) ? " + 
"-0.00038347582009141533" + 
":  " + 
"0.01741648994188754" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4med') <= 1521.5) ? " + 
"(b('L8b2') <= 906.0) ? " + 
"(b('L8b3') <= 1298.0) ? " + 
"-0.0002191607274811208" + 
":  " + 
"-0.017639429886904867" + 
":  " + 
"(b('dsvh') <= -4.526712894439697) ? " + 
"0.002814557425322488" + 
":  " + 
"0.04571704914176431" + 
":  " + 
"(b('L8b4') <= 1644.0) ? " + 
"(b('L8b3') <= 1318.5) ? " + 
"0.002128043580981185" + 
":  " + 
"0.03640677258058724" + 
":  " + 
"(b('L8b3') <= 1224.5) ? " + 
"-0.012605041024920069" + 
":  " + 
"-9.37579499390918e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1708.5) ? " + 
"(b('L8b2') <= 971.5) ? " + 
"(b('L8b2') <= 960.5) ? " + 
"3.554578907745868e-05" + 
":  " + 
"0.015405853641527622" + 
":  " + 
"(b('L8b5') <= 3845.0) ? " + 
"-0.003723997563292609" + 
":  " + 
"0.02066438209590102" + 
":  " + 
"(b('L8b6med') <= 3028.75) ? " + 
"(b('dgvv') <= 0.449338436126709) ? " + 
"0.00087662552226049" + 
":  " + 
"0.05437464783158582" + 
":  " + 
"(b('L8b3') <= 1719.0) ? " + 
"0.021080856954552002" + 
":  " + 
"0.00041678526116717147" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 1034.5) ? " + 
"(b('L8b2') <= 987.0) ? " + 
"(b('L8b4') <= 2271.5) ? " + 
"0.00016476397193585649" + 
":  " + 
"-0.01097775926723405" + 
":  " + 
"(b('lat') <= 46.34564971923828) ? " + 
"-0.006673513787929229" + 
":  " + 
"-0.10210085471309097" + 
":  " + 
"(b('L8b2') <= 1047.5) ? " + 
"(b('L8b4med') <= 1752.0) ? " + 
"0.040290688532594335" + 
":  " + 
"0.008981537253204157" + 
":  " + 
"(b('lat') <= -35.09726524353027) ? " + 
"0.057676656309090364" + 
":  " + 
"0.0002318482586251707" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1418.5) ? " + 
"(b('L8b1') <= 752.5) ? " + 
"(b('L8b1') <= 709.5) ? " + 
"-0.0002468511280087191" + 
":  " + 
"0.00914003181264937" + 
":  " + 
"(b('ndvi') <= 2102.5) ? " + 
"-0.01110709377912817" + 
":  " + 
"0.007318823219637558" + 
":  " + 
"(b('L8b3') <= 1433.5) ? " + 
"(b('L8b11') <= 2406.0) ? " + 
"0.09326157556142592" + 
":  " + 
"0.012733806389745257" + 
":  " + 
"(b('dsvh') <= -5.619801998138428) ? " + 
"-0.0004310423383487254" + 
":  " + 
"0.007304896924491072" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1508.0) ? " + 
"(b('L8b3') <= 1499.0) ? " + 
"(b('L8b2') <= 1053.5) ? " + 
"-0.00016505681874444706" + 
":  " + 
"0.015067491648164608" + 
":  " + 
"(b('dgvv') <= 4.910737037658691) ? " + 
"-0.01645781366941884" + 
":  " + 
"-0.09594085991753913" + 
":  " + 
"(b('L8b3') <= 1531.0) ? " + 
"(b('L8b4') <= 1798.0) ? " + 
"0.04514007229683628" + 
":  " + 
"0.008701430520704101" + 
":  " + 
"(b('dgvh') <= -2.9981374740600586) ? " + 
"-0.0005120457783793116" + 
":  " + 
"0.029558835419320244" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1370.0) ? " + 
"(b('ndvi') <= 1258.5) ? " + 
"(b('L8b1') <= 421.5) ? " + 
"0.06324897242398465" + 
":  " + 
"-0.0011011659103617043" + 
":  " + 
"(b('ndvi') <= 1261.0) ? " + 
"0.07883491041683131" + 
":  " + 
"0.0031813109160675314" + 
":  " + 
"(b('dgvv') <= 4.765422105789185) ? " + 
"(b('dsvv') <= 4.083662986755371) ? " + 
"-0.00018851820461162909" + 
":  " + 
"0.008159298952630862" + 
":  " + 
"(b('clay') <= 36.5) ? " + 
"-0.008517961026765069" + 
":  " + 
"0.11023558844593545" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.41945409774780273) ? " + 
"(b('dsvv') <= 0.4165806770324707) ? " + 
"(b('L8b5') <= 2794.5) ? " + 
"-0.0006908029458427221" + 
":  " + 
"0.0014642157784986736" + 
":  " + 
"(b('L8b6med') <= 2689.0) ? " + 
"0.09179422455245337" + 
":  " + 
"0.014576870835239288" + 
":  " + 
"(b('ndvi_med') <= 4921.5) ? " + 
"(b('L8dt') <= 1361386.5) ? " + 
"-0.0012596772864715631" + 
":  " + 
"0.0025158206674018558" + 
":  " + 
"(b('L8b3') <= 765.0) ? " + 
"0.003375989205108575" + 
":  " + 
"-0.023868146589148435" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4045.5) ? " + 
"(b('L8b5') <= 4031.0) ? " + 
"(b('ndvi') <= 5233.5) ? " + 
"0.00012629260538445875" + 
":  " + 
"-0.002797455389866083" + 
":  " + 
"(b('L8b3med') <= 1150.5) ? " + 
"0.07731743706314695" + 
":  " + 
"0.007904149701252495" + 
":  " + 
"(b('L8b5') <= 4051.5) ? " + 
"(b('L8b4med') <= 1453.75) ? " + 
"-0.08222959268865995" + 
":  " + 
"-0.039187739988159366" + 
":  " + 
"(b('ndvi') <= 6364.5) ? " + 
"-0.0031820034468160742" + 
":  " + 
"0.031854550423887705" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4762.5) ? " + 
"(b('L8b5') <= 4045.5) ? " + 
"(b('L8b5') <= 4031.0) ? " + 
"2.256640045739085e-05" + 
":  " + 
"0.034879049675885024" + 
":  " + 
"(b('dsvv') <= 1.01743745803833) ? " + 
"0.0008322735248979951" + 
":  " + 
"-0.014335206739131546" + 
":  " + 
"(b('dgvv') <= 3.534224510192871) ? " + 
"(b('ndvi') <= 5903.5) ? " + 
"0.032453721008781015" + 
":  " + 
"0.00565947103269474" + 
":  " + 
"(b('dgvv') <= 4.152749300003052) ? " + 
"0.0008696921947283429" + 
":  " + 
"0.0024982433640721863" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 103.0) ? " + 
"(b('L8b5') <= 2343.5) ? " + 
"(b('L8b2') <= 641.5) ? " + 
"-0.01206167252423266" + 
":  " + 
"-0.0009911070340042185" + 
":  " + 
"(b('dgvv') <= 0.5466384887695312) ? " + 
"-0.023875209386491583" + 
":  " + 
"-0.040125663123879544" + 
":  " + 
"(b('gvv') <= -11.414001941680908) ? " + 
"(b('dgvh') <= -4.013646602630615) ? " + 
"-5.184237329443497e-05" + 
":  " + 
"-0.007529623073688871" + 
":  " + 
"(b('ndvi') <= 3656.5) ? " + 
"0.0014082548773740732" + 
":  " + 
"-0.002152025262180957" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 947.5) ? " + 
"(b('L8b3') <= 846.5) ? " + 
"(b('L8b6') <= 3038.0) ? " + 
"-2.869338035618165e-05" + 
":  " + 
"-0.026302404785983547" + 
":  " + 
"(b('lon') <= -111.17835998535156) ? " + 
"0.05235069005801195" + 
":  " + 
"0.004672502392578378" + 
":  " + 
"(b('L8b7') <= 1485.5) ? " + 
"(b('gvv') <= -16.83011817932129) ? " + 
"0.136020226240693" + 
":  " + 
"0.009354346888176972" + 
":  " + 
"(b('L8b7') <= 1523.0) ? " + 
"-0.03257046282706911" + 
":  " + 
"-0.00017868112610271327" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1728.0) ? " + 
"(b('dsvh') <= -8.909214496612549) ? " + 
"(b('gvv') <= -10.370579719543457) ? " + 
"-0.030348320723241617" + 
":  " + 
"-0.007413450592576109" + 
":  " + 
"(b('dsvh') <= -6.1689958572387695) ? " + 
"0.0037694426904121814" + 
":  " + 
"-0.007739733390465129" + 
":  " + 
"(b('L8b6') <= 1745.0) ? " + 
"(b('L8dt') <= 238377.5) ? " + 
"0.07195361614859476" + 
":  " + 
"0.014356690260804064" + 
":  " + 
"(b('L8b6') <= 1750.5) ? " + 
"-0.027110464088461378" + 
":  " + 
"2.555418687480764e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  return prediction