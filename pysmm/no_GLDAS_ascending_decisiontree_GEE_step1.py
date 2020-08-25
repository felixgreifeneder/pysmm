import ee 

def tree(feature_stack): 

  prediction = ee.Image(0.16607964)
  learning_rate = ee.Image(0.1)
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -101.20384979248047) ? " + 
"(b('lon') <= -106.62174606323242) ? " + 
"(b('gvvk2') <= 0.059816403314471245) ? " + 
"0.12042036652565002" + 
":  " + 
"-0.07530297376215458" + 
":  " + 
"(b('lat') <= 47.60140037536621) ? " + 
"-0.03159749840519258" + 
":  " + 
"0.02808702654308743" + 
":  " + 
"(b('bulk') <= 121.5) ? " + 
"(b('trees') <= 15.984597206115723) ? " + 
"0.201896608248353" + 
":  " + 
"0.0020870231091976166" + 
":  " + 
"(b('lon') <= -84.7333984375) ? " + 
"0.08926729933947933" + 
":  " + 
"-0.004966003665079673" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.230051040649414) ? " + 
"(b('sand') <= 28.5) ? " + 
"(b('lon') <= -111.3140983581543) ? " + 
"-0.07404934499412774" + 
":  " + 
"0.09943564434686963" + 
":  " + 
"(b('ndvi_med') <= 1920.5) ? " + 
"-0.06582339247801802" + 
":  " + 
"-0.015486387348049866" + 
":  " + 
"(b('bulk') <= 121.5) ? " + 
"(b('L8b3med') <= 753.5) ? " + 
"0.24001069810241474" + 
":  " + 
"0.12856069600830475" + 
":  " + 
"(b('clay') <= 27.0) ? " + 
"0.0275532480954418" + 
":  " + 
"0.15791029674159426" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 49.230051040649414) ? " + 
"(b('sand') <= 28.5) ? " + 
"(b('L8b1med') <= 366.25) ? " + 
"0.1221637738724236" + 
":  " + 
"0.020308293974839846" + 
":  " + 
"(b('lon') <= -106.60049438476562) ? " + 
"-0.06098549453099523" + 
":  " + 
"-0.015066829735171872" + 
":  " + 
"(b('bulk') <= 121.5) ? " + 
"(b('L8b3med') <= 753.5) ? " + 
"0.21600962829217313" + 
":  " + 
"0.11570462640747432" + 
":  " + 
"(b('clay') <= 31.5) ? " + 
"0.026949808591293672" + 
":  " + 
"0.16957760202996178" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -101.20384979248047) ? " + 
"(b('lon') <= -106.62174606323242) ? " + 
"(b('gvvk2') <= 0.059816403314471245) ? " + 
"0.11602551806098951" + 
":  " + 
"-0.0563940493605363" + 
":  " + 
"(b('lat') <= 32.78880023956299) ? " + 
"-0.12733086847566213" + 
":  " + 
"-0.00880418627839664" + 
":  " + 
"(b('bulk') <= 121.5) ? " + 
"(b('ndvi_med') <= 3953.75) ? " + 
"0.16721415212955107" + 
":  " + 
"0.055057582970849506" + 
":  " + 
"(b('L8b6med') <= 3350.5) ? " + 
"0.03254054633334477" + 
":  " + 
"-0.05637312343136828" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.854400634765625) ? " + 
"(b('sand') <= 28.5) ? " + 
"(b('L8b3med') <= 783.5) ? " + 
"0.1169223569720222" + 
":  " + 
"0.026905348989562018" + 
":  " + 
"(b('ndvi_med') <= 1920.5) ? " + 
"-0.04932178524206695" + 
":  " + 
"-0.012147968916948438" + 
":  " + 
"(b('bulk') <= 121.5) ? " + 
"(b('L8b3med') <= 753.5) ? " + 
"0.17768725025000076" + 
":  " + 
"0.09563756362540987" + 
":  " + 
"(b('clay') <= 27.5) ? " + 
"0.019412532979412308" + 
":  " + 
"0.1266617120123931" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -97.97296905517578) ? " + 
"(b('lon') <= -106.62174606323242) ? " + 
"(b('gvvk2') <= 0.059816403314471245) ? " + 
"0.1056377631465854" + 
":  " + 
"-0.04684356221737963" + 
":  " + 
"(b('lat') <= 32.99824905395508) ? " + 
"-0.08238207130268298" + 
":  " + 
"-0.002406416811066514" + 
":  " + 
"(b('bulk') <= 121.5) ? " + 
"(b('ndvi_med') <= 3953.75) ? " + 
"0.1376529633586217" + 
":  " + 
"0.04286234917901981" + 
":  " + 
"(b('lon') <= -85.54829788208008) ? " + 
"0.08492143840582675" + 
":  " + 
"-0.004489602636950311" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.854400634765625) ? " + 
"(b('sand') <= 26.0) ? " + 
"(b('L8b1med') <= 366.25) ? " + 
"0.10380059273960973" + 
":  " + 
"0.00820485726637647" + 
":  " + 
"(b('ndvi_med') <= 1913.0) ? " + 
"-0.04084146356974732" + 
":  " + 
"-0.009793753170697188" + 
":  " + 
"(b('bulk') <= 121.5) ? " + 
"(b('L8b3med') <= 753.5) ? " + 
"0.14615322888913845" + 
":  " + 
"0.07925982263351083" + 
":  " + 
"(b('clay') <= 31.5) ? " + 
"0.019325185423941342" + 
":  " + 
"0.12820747215180914" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.25013542175293) ? " + 
"(b('sand') <= 28.5) ? " + 
"(b('lon') <= -108.939697265625) ? " + 
"-0.06186249936000121" + 
":  " + 
"0.06279632780451988" + 
":  " + 
"(b('L8b1med') <= 303.75) ? " + 
"0.0887976562135922" + 
":  " + 
"-0.027511745588590042" + 
":  " + 
"(b('lon') <= 16.08477020263672) ? " + 
"(b('clay') <= 32.5) ? " + 
"0.017135178018915963" + 
":  " + 
"0.12671476566903306" + 
":  " + 
"(b('trees') <= 3.1386263370513916) ? " + 
"0.08292185316511413" + 
":  " + 
"0.13964362147087925" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.10324096679688) ? " + 
"(b('bulk') <= 132.5) ? " + 
"(b('gvvk2') <= 0.3279925584793091) ? " + 
"-0.06433963768887321" + 
":  " + 
"-0.026291172711254845" + 
":  " + 
"(b('ndvi_med') <= 1920.5) ? " + 
"-0.035033340002156126" + 
":  " + 
"-0.004382953312608239" + 
":  " + 
"(b('bulk') <= 121.5) ? " + 
"(b('ndvi_med') <= 3953.75) ? " + 
"0.10397035505639342" + 
":  " + 
"0.028116182503774307" + 
":  " + 
"(b('L8b6med') <= 3350.5) ? " + 
"0.02061958773611434" + 
":  " + 
"-0.03926483415270969" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.25013542175293) ? " + 
"(b('sand') <= 26.0) ? " + 
"(b('L8b1med') <= 366.25) ? " + 
"0.08507894191158535" + 
":  " + 
"0.00022991654526520466" + 
":  " + 
"(b('svvk3') <= 0.0002485524819348939) ? " + 
"-0.002285623309644842" + 
":  " + 
"-0.028708937293958858" + 
":  " + 
"(b('lon') <= 16.08477020263672) ? " + 
"(b('clay') <= 32.5) ? " + 
"0.013645510867482832" + 
":  " + 
"0.10781379196250432" + 
":  " + 
"(b('trees') <= 3.1386263370513916) ? " + 
"0.06965078752529329" + 
":  " + 
"0.115282223818152" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.10324096679688) ? " + 
"(b('gvvk2') <= 0.041203947737812996) ? " + 
"0.0994713943700809" + 
":  " + 
"(b('gvvk2') <= 0.31293176114559174) ? " + 
"-0.03617356990320276" + 
":  " + 
"-0.014173650006765313" + 
":  " + 
"(b('bulk') <= 129.5) ? " + 
"(b('L8b2med') <= 383.0) ? " + 
"0.10561385494790632" + 
":  " + 
"0.03432487736496288" + 
":  " + 
"(b('sand') <= 26.0) ? " + 
"0.052545490880128186" + 
":  " + 
"-0.005778064309699883" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.10324096679688) ? " + 
"(b('bulk') <= 132.5) ? " + 
"(b('L8b7med') <= 1613.0) ? " + 
"-0.028824863556990588" + 
":  " + 
"-0.054812257923240924" + 
":  " + 
"(b('ndvi_med') <= 3650.75) ? " + 
"-0.02274112163906982" + 
":  " + 
"0.06505116967260752" + 
":  " + 
"(b('L8b7med') <= 2494.0) ? " + 
"(b('lon') <= 24.045809745788574) ? " + 
"0.02975254041417464" + 
":  " + 
"-0.04429101955701853" + 
":  " + 
"(b('L8b7med') <= 2935.5) ? " + 
"-0.012964681619463686" + 
":  " + 
"-0.07344099657039826" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.25013542175293) ? " + 
"(b('sand') <= 26.0) ? " + 
"(b('lon') <= -107.19025039672852) ? " + 
"-0.048936953253384" + 
":  " + 
"0.053126729973830375" + 
":  " + 
"(b('sand') <= 47.5) ? " + 
"-0.008535352363628502" + 
":  " + 
"-0.03216306941091008" + 
":  " + 
"(b('lon') <= 16.08477020263672) ? " + 
"(b('clay') <= 32.5) ? " + 
"0.009197152972595378" + 
":  " + 
"0.09162724453020671" + 
":  " + 
"(b('trees') <= 3.1386263370513916) ? " + 
"0.055259553029379606" + 
":  " + 
"0.09021736190012865" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -106.49531555175781) ? " + 
"(b('gvvk2') <= 0.041203947737812996) ? " + 
"0.09265190233334267" + 
":  " + 
"(b('L8b3med') <= 833.5) ? " + 
"-0.0459817415108534" + 
":  " + 
"-0.01992137890164851" + 
":  " + 
"(b('bulk') <= 129.5) ? " + 
"(b('ndvi_med') <= 3594.5) ? " + 
"0.0676598614173769" + 
":  " + 
"0.011376584572781422" + 
":  " + 
"(b('L8b7med') <= 2935.5) ? " + 
"0.006995021487418199" + 
":  " + 
"-0.06420974670243335" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 390.0) ? " + 
"(b('bulk') <= 130.0) ? " + 
"(b('bulk') <= 124.5) ? " + 
"0.06560233268249177" + 
":  " + 
"0.1637754250885927" + 
":  " + 
"(b('gvvk2') <= 0.2661396265029907) ? " + 
"0.06372864272815537" + 
":  " + 
"-0.007721163015176459" + 
":  " + 
"(b('sand') <= 20.5) ? " + 
"(b('L8b3med') <= 754.5) ? " + 
"0.10968286483390202" + 
":  " + 
"0.04280233155446714" + 
":  " + 
"(b('svvk3') <= -0.011237047612667084) ? " + 
"0.020162004864749818" + 
":  " + 
"-0.01230593407194557" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -106.62174606323242) ? " + 
"(b('bulk') <= 132.5) ? " + 
"(b('bulk') <= 128.0) ? " + 
"-0.05105743948389726" + 
":  " + 
"-0.03144991970548392" + 
":  " + 
"(b('lat') <= 38.14986991882324) ? " + 
"-0.025780601810715485" + 
":  " + 
"-0.005705137575445787" + 
":  " + 
"(b('L8b7med') <= 2494.0) ? " + 
"(b('lon') <= 24.045809745788574) ? " + 
"0.021086740846474536" + 
":  " + 
"-0.03902063918207505" + 
":  " + 
"(b('gvvk2') <= 0.5717740952968597) ? " + 
"-0.03193778755629124" + 
":  " + 
"0.04754637159312138" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 387.0) ? " + 
"(b('L8b6med') <= 2449.0) ? " + 
"(b('gvvk2') <= 0.08803771063685417) ? " + 
"0.11132724933280336" + 
":  " + 
"-0.008021273267388761" + 
":  " + 
"(b('sand') <= 77.5) ? " + 
"0.06088177884008104" + 
":  " + 
"0.14528920849508595" + 
":  " + 
"(b('sand') <= 20.5) ? " + 
"(b('L8b3med') <= 754.5) ? " + 
"0.09660590426586436" + 
":  " + 
"0.03641342431437297" + 
":  " + 
"(b('svvk3') <= 0.0002485524819348939) ? " + 
"0.007569047015269874" + 
":  " + 
"-0.013355892818006778" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.18899917602539) ? " + 
"(b('gvvk2') <= 0.041203947737812996) ? " + 
"0.08443091456322055" + 
":  " + 
"(b('gvvk2') <= 0.31293176114559174) ? " + 
"-0.022305367222950373" + 
":  " + 
"-0.004304223738750394" + 
":  " + 
"(b('L8b7med') <= 2935.5) ? " + 
"(b('bulk') <= 121.5) ? " + 
"0.0375824657876634" + 
":  " + 
"0.007577868002773941" + 
":  " + 
"(b('bulk') <= 148.5) ? " + 
"-0.023165268422357763" + 
":  " + 
"-0.0817822340656064" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.25013542175293) ? " + 
"(b('sand') <= 26.0) ? " + 
"(b('L8b3med') <= 783.5) ? " + 
"0.06236566067448488" + 
":  " + 
"0.005062010225907434" + 
":  " + 
"(b('sand') <= 47.5) ? " + 
"-0.004081855882542523" + 
":  " + 
"-0.024172024938257895" + 
":  " + 
"(b('lon') <= 22.875690460205078) ? " + 
"(b('clay') <= 32.5) ? " + 
"0.004968736779903664" + 
":  " + 
"0.06432429844131184" + 
":  " + 
"(b('trees') <= 7.657010555267334) ? " + 
"0.04027786998130988" + 
":  " + 
"0.07830359266431693" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 310.5) ? " + 
"(b('svvk3') <= 0.017247695475816727) ? " + 
"(b('L8b3med') <= 562.5) ? " + 
"0.09245069884070205" + 
":  " + 
"0.035320321970584524" + 
":  " + 
"(b('ndvi_med') <= 3172.0) ? " + 
"-0.07836999553422705" + 
":  " + 
"0.013519848290199223" + 
":  " + 
"(b('sand') <= 20.5) ? " + 
"(b('L8b3med') <= 754.5) ? " + 
"0.07867243154948338" + 
":  " + 
"0.025568447907588" + 
":  " + 
"(b('ndvi_med') <= 3333.0) ? " + 
"-0.010289490356653025" + 
":  " + 
"0.008252449807718928" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.18899917602539) ? " + 
"(b('bulk') <= 132.5) ? " + 
"(b('lat') <= 43.56180000305176) ? " + 
"-0.022280443443601087" + 
":  " + 
"-0.04004670995739059" + 
":  " + 
"(b('lat') <= 38.14986991882324) ? " + 
"-0.018610707072490414" + 
":  " + 
"-0.0011216871888900643" + 
":  " + 
"(b('L8b7med') <= 2935.5) ? " + 
"(b('lon') <= 24.045809745788574) ? " + 
"0.01346674538016994" + 
":  " + 
"-0.026681759757854435" + 
":  " + 
"(b('bulk') <= 143.0) ? " + 
"0.014713661154443253" + 
":  " + 
"-0.05677491780896735" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 387.0) ? " + 
"(b('L8b6med') <= 2449.0) ? " + 
"(b('gvvk2') <= 0.08803771063685417) ? " + 
"0.09196575667393547" + 
":  " + 
"-0.011271640985752115" + 
":  " + 
"(b('clay') <= 9.0) ? " + 
"0.12177040158872829" + 
":  " + 
"0.042199136871250646" + 
":  " + 
"(b('sand') <= 20.5) ? " + 
"(b('bulk') <= 148.0) ? " + 
"0.02306616281526964" + 
":  " + 
"0.07133140574037586" + 
":  " + 
"(b('svvk3') <= 0.0002485524819348939) ? " + 
"0.006412275133693133" + 
":  " + 
"-0.00987055611560687" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.25013542175293) ? " + 
"(b('sand') <= 47.5) ? " + 
"(b('lon') <= 2.9450849890708923) ? " + 
"0.004934482172755848" + 
":  " + 
"-0.03696081601917507" + 
":  " + 
"(b('L8b2med') <= 517.25) ? " + 
"-0.07186355090170032" + 
":  " + 
"-0.014082705418374756" + 
":  " + 
"(b('trees') <= 15.564701080322266) ? " + 
"(b('lon') <= 9.16319990158081) ? " + 
"0.01014160091338722" + 
":  " + 
"0.03748847150216005" + 
":  " + 
"(b('L8b3med') <= 881.25) ? " + 
"-0.031069437303497104" + 
":  " + 
"0.07742340910705761" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.18899917602539) ? " + 
"(b('svvk3') <= -0.005095629720017314) ? " + 
"(b('gvvk2') <= 0.3577568531036377) ? " + 
"-0.044434024832501466" + 
":  " + 
"0.09457999586631283" + 
":  " + 
"(b('svvk3') <= -0.00452080275863409) ? " + 
"0.0929603169806746" + 
":  " + 
"-0.009044565814586951" + 
":  " + 
"(b('L8b7med') <= 2935.5) ? " + 
"(b('lat') <= 32.39724922180176) ? " + 
"-0.02681231517360001" + 
":  " + 
"0.011362611783988369" + 
":  " + 
"(b('bulk') <= 148.5) ? " + 
"-0.013525312347550824" + 
":  " + 
"-0.06469219830504948" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2543.0) ? " + 
"(b('lon') <= -97.97296905517578) ? " + 
"(b('L8b3med') <= 813.5) ? " + 
"-0.030111636126959763" + 
":  " + 
"1.4226171395817302e-05" + 
":  " + 
"(b('lon') <= -87.08110046386719) ? " + 
"0.0367657273056969" + 
":  " + 
"0.005483188961308017" + 
":  " + 
"(b('gvvk2') <= 0.5717740952968597) ? " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.07731561905203425" + 
":  " + 
"-0.019172668303024852" + 
":  " + 
"(b('sand') <= 52.0) ? " + 
"0.09357709872201847" + 
":  " + 
"0.019808633769294454" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 310.5) ? " + 
"(b('svvk3') <= 0.017247695475816727) ? " + 
"(b('L8b3med') <= 562.5) ? " + 
"0.06955323801616153" + 
":  " + 
"0.025177814600108157" + 
":  " + 
"(b('bulk') <= 135.0) ? " + 
"0.012405047187013227" + 
":  " + 
"-0.05577095374459593" + 
":  " + 
"(b('ndvi_med') <= 4848.5) ? " + 
"(b('sand') <= 47.5) ? " + 
"0.0009394596212581061" + 
":  " + 
"-0.013723924837461366" + 
":  " + 
"(b('trees') <= 17.202927112579346) ? " + 
"0.037761166128147394" + 
":  " + 
"-0.01693476407969034" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -106.62174606323242) ? " + 
"(b('L8b3med') <= 833.5) ? " + 
"(b('L8b3med') <= 824.5) ? " + 
"-0.024257336319489953" + 
":  " + 
"-0.09186810828796436" + 
":  " + 
"(b('ndvi_med') <= 1920.5) ? " + 
"-0.009965685849753169" + 
":  " + 
"0.014382142819791402" + 
":  " + 
"(b('clay') <= 24.5) ? " + 
"(b('L8b6med') <= 2312.25) ? " + 
"-0.028741855900755873" + 
":  " + 
"0.004171029742706091" + 
":  " + 
"(b('lon') <= 1.383899986743927) ? " + 
"0.035444789037542855" + 
":  " + 
"-0.012102883838265743" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 387.0) ? " + 
"(b('ndvi_med') <= 2315.5) ? " + 
"(b('lat') <= 47.4859504699707) ? " + 
"-0.031734673656073076" + 
":  " + 
"-0.061360134697766716" + 
":  " + 
"(b('L8b1med') <= 330.5) ? " + 
"0.024825227951074454" + 
":  " + 
"0.08432826254027942" + 
":  " + 
"(b('sand') <= 39.5) ? " + 
"(b('lon') <= 2.9854149222373962) ? " + 
"0.012916296090490694" + 
":  " + 
"-0.025745695700652" + 
":  " + 
"(b('trees') <= 25.446617126464844) ? " + 
"-0.005625798739584169" + 
":  " + 
"-0.08212888702869449" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2543.0) ? " + 
"(b('lon') <= -97.97296905517578) ? " + 
"(b('L8b3med') <= 813.5) ? " + 
"-0.02614686829896279" + 
":  " + 
"0.00035789679786636306" + 
":  " + 
"(b('svvk3') <= 0.12929637357592583) ? " + 
"0.011237881102400388" + 
":  " + 
"-0.05173144322154115" + 
":  " + 
"(b('gvvk2') <= 0.5717740952968597) ? " + 
"(b('gvvk2') <= 0.5363309979438782) ? " + 
"-0.01300946137430635" + 
":  " + 
"-0.0808167405613758" + 
":  " + 
"(b('L8b1med') <= 597.0) ? " + 
"0.0842709197873786" + 
":  " + 
"0.020159335454847542" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 310.5) ? " + 
"(b('svvk3') <= 0.017247695475816727) ? " + 
"(b('L8b7med') <= 1074.5) ? " + 
"-0.02346103731888652" + 
":  " + 
"0.025486525018692373" + 
":  " + 
"(b('clay') <= 15.5) ? " + 
"0.008786772870866918" + 
":  " + 
"-0.04365899938505558" + 
":  " + 
"(b('L8b7med') <= 1434.5) ? " + 
"(b('clay') <= 25.0) ? " + 
"-0.045342004362211905" + 
":  " + 
"0.05009532089398296" + 
":  " + 
"(b('L8b7med') <= 1442.5) ? " + 
"0.13463348000466688" + 
":  " + 
"-0.0010618267234934822" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2468.0) ? " + 
"(b('L8b3med') <= 1048.5) ? " + 
"(b('lon') <= -97.97296905517578) ? " + 
"-0.009933721080877833" + 
":  " + 
"0.005533945257522242" + 
":  " + 
"(b('lon') <= -113.15608978271484) ? " + 
"-0.00620684788262053" + 
":  " + 
"0.03322384642010034" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.07392272689929069" + 
":  " + 
"(b('gvvk2') <= 0.5717740952968597) ? " + 
"-0.012979175530597402" + 
":  " + 
"0.03748305988147146" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 387.0) ? " + 
"(b('L8b6med') <= 2449.0) ? " + 
"(b('gvvk2') <= 0.08803771063685417) ? " + 
"0.06782053441800256" + 
":  " + 
"-0.012448266278675454" + 
":  " + 
"(b('gvvk2') <= 0.3301797956228256) ? " + 
"0.02314996731792792" + 
":  " + 
"0.09229792066705672" + 
":  " + 
"(b('gvvk2') <= 0.3110143393278122) ? " + 
"(b('lat') <= 36.29348564147949) ? " + 
"0.007634074261686864" + 
":  " + 
"-0.011511288417742172" + 
":  " + 
"(b('gvvk2') <= 0.3210165649652481) ? " + 
"0.03184673766281795" + 
":  " + 
"0.0008060889112948004" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2468.0) ? " + 
"(b('L8b3med') <= 1048.5) ? " + 
"(b('L8b7med') <= 1773.5) ? " + 
"0.005319919596063654" + 
":  " + 
"-0.0087721264468526" + 
":  " + 
"(b('gvvk2') <= 0.304255872964859) ? " + 
"-0.004254022775736983" + 
":  " + 
"0.03151616185655596" + 
":  " + 
"(b('gvvk2') <= 0.5717740952968597) ? " + 
"(b('gvvk2') <= 0.5363309979438782) ? " + 
"-0.009578669197775449" + 
":  " + 
"-0.07141157517095861" + 
":  " + 
"(b('L8b2med') <= 753.25) ? " + 
"0.014420669702435503" + 
":  " + 
"0.07212109560171345" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 13.0) ? " + 
"(b('gvvk2') <= 0.3578432649374008) ? " + 
"0.06515630144361423" + 
":  " + 
"(b('L8b6med') <= 2113.5) ? " + 
"0.0481821461625086" + 
":  " + 
"0.040404554976587126" + 
":  " + 
"(b('L8b1med') <= 310.5) ? " + 
"(b('svvk3') <= 0.0003728241717908809) ? " + 
"0.025915651590932103" + 
":  " + 
"0.003235505473883351" + 
":  " + 
"(b('L8b7med') <= 1434.5) ? " + 
"-0.03081364206924672" + 
":  " + 
"-0.0007837696553574958" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1228.0) ? " + 
"(b('L8b3med') <= 1046.0) ? " + 
"(b('L8b7med') <= 1773.5) ? " + 
"0.004656456612682935" + 
":  " + 
"-0.00856912261391396" + 
":  " + 
"(b('gvvk2') <= 0.28608158230781555) ? " + 
"-0.005791123197233208" + 
":  " + 
"0.024907113343536992" + 
":  " + 
"(b('lat') <= 41.30295944213867) ? " + 
"(b('svvk3') <= -0.015828943345695734) ? " + 
"0.040579572216320484" + 
":  " + 
"-0.0068649300994267776" + 
":  " + 
"(b('lon') <= -5.488860130310059) ? " + 
"-0.013589281132603248" + 
":  " + 
"-0.05285764972235756" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 4.0) ? " + 
"-0.093573163181875" + 
":  " + 
"(b('L8b7med') <= 2280.5) ? " + 
"(b('L8b3med') <= 1048.5) ? " + 
"0.0001708113371144585" + 
":  " + 
"0.022157767615824213" + 
":  " + 
"(b('L8b6med') <= 2820.5) ? " + 
"-0.04462859602524662" + 
":  " + 
"-0.005014630989030439" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.0002485524819348939) ? " + 
"(b('lon') <= -101.20384979248047) ? " + 
"(b('svvk3') <= -8.816841727821156e-05) ? " + 
"-0.0120228861964291" + 
":  " + 
"0.02913212319113231" + 
":  " + 
"(b('lon') <= -74.9410400390625) ? " + 
"0.030509058497771822" + 
":  " + 
"0.0044459190445146155" + 
":  " + 
"(b('trees') <= 25.446617126464844) ? " + 
"(b('sand') <= 26.0) ? " + 
"0.019310988796829347" + 
":  " + 
"-0.004436358013124373" + 
":  " + 
"(b('L8b1med') <= 437.0) ? " + 
"-0.08667313765009599" + 
":  " + 
"-0.08945581739911518" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 387.0) ? " + 
"(b('L8b6med') <= 2862.25) ? " + 
"(b('ndvi_med') <= 2315.5) ? " + 
"-0.038799151804563725" + 
":  " + 
"0.014581545595422732" + 
":  " + 
"(b('svvk3') <= 0.03304598666727543) ? " + 
"0.07066674156625846" + 
":  " + 
"0.07236672563989738" + 
":  " + 
"(b('sand') <= 44.5) ? " + 
"(b('lon') <= 2.9450849890708923) ? " + 
"0.0072088047622388875" + 
":  " + 
"-0.026756534187459522" + 
":  " + 
"(b('trees') <= 25.051298141479492) ? " + 
"-0.0053297245927244954" + 
":  " + 
"-0.08841235833219459" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -110.6124038696289) ? " + 
"(b('svvk3') <= -0.00746589875780046) ? " + 
"(b('L8b6med') <= 3327.5) ? " + 
"-0.06975197827391892" + 
":  " + 
"-0.013989176781445033" + 
":  " + 
"(b('lon') <= -110.7353401184082) ? " + 
"-0.0028331330736231556" + 
":  " + 
"-0.06222824857952908" + 
":  " + 
"(b('svvk3') <= 0.0007185436552390456) ? " + 
"(b('L8b1med') <= 427.5) ? " + 
"0.0026961926650838773" + 
":  " + 
"0.022229649718260767" + 
":  " + 
"(b('sand') <= 26.0) ? " + 
"0.026958658348342282" + 
":  " + 
"-0.005180094134063075" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.2853217273950577) ? " + 
"(b('lat') <= 48.25013542175293) ? " + 
"(b('lat') <= 46.2239990234375) ? " + 
"-0.0004891073263109525" + 
":  " + 
"-0.02756104916258431" + 
":  " + 
"(b('L8b6med') <= 2849.0) ? " + 
"0.0016192017535321143" + 
":  " + 
"0.02384322003866569" + 
":  " + 
"(b('L8b7med') <= 1808.5) ? " + 
"(b('L8b7med') <= 1713.0) ? " + 
"-0.04003690697070039" + 
":  " + 
"-0.04486425529394461" + 
":  " + 
"-0.05813248793901704" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 4.0) ? " + 
"-0.08267231845706521" + 
":  " + 
"(b('L8b7med') <= 2543.0) ? " + 
"(b('svvk3') <= 0.15870565921068192) ? " + 
"0.002773485002456934" + 
":  " + 
"-0.03999437375128305" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.06594323095750458" + 
":  " + 
"-0.00824917687714369" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 32.39724922180176) ? " + 
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.23104858398438) ? " + 
"0.038798048154486585" + 
":  " + 
"-0.011841677281613913" + 
":  " + 
"(b('L8b1med') <= 354.5) ? " + 
"-0.020147034564469743" + 
":  " + 
"-0.053274487381187924" + 
":  " + 
"(b('lon') <= 24.045809745788574) ? " + 
"(b('lat') <= 32.848440170288086) ? " + 
"0.08273749610552317" + 
":  " + 
"0.0014592884365575737" + 
":  " + 
"(b('lat') <= 44.097700119018555) ? " + 
"-0.059909807178142205" + 
":  " + 
"-0.023891329973405505" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -110.6124038696289) ? " + 
"(b('svvk3') <= -0.00746589875780046) ? " + 
"(b('sand') <= 36.5) ? " + 
"-0.08307952887907129" + 
":  " + 
"-0.02249953912790839" + 
":  " + 
"(b('gvvk2') <= 0.059816403314471245) ? " + 
"0.07203510088435644" + 
":  " + 
"-0.004093943001656243" + 
":  " + 
"(b('clay') <= 24.5) ? " + 
"(b('L8b6med') <= 2312.25) ? " + 
"-0.022793661429261407" + 
":  " + 
"0.001965885185825499" + 
":  " + 
"(b('lon') <= 24.045809745788574) ? " + 
"0.020805817936187382" + 
":  " + 
"-0.010665274429899984" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 719.0) ? " + 
"(b('L8b3med') <= 701.75) ? " + 
"(b('lon') <= 9.16319990158081) ? " + 
"-0.010839568194168278" + 
":  " + 
"0.020451715068215633" + 
":  " + 
"(b('trees') <= 9.341397285461426) ? " + 
"0.013547584892985872" + 
":  " + 
"0.06597121963903868" + 
":  " + 
"(b('trees') <= 25.446617126464844) ? " + 
"(b('L8b3med') <= 852.5) ? " + 
"-0.007878675460886015" + 
":  " + 
"0.0022087053535243075" + 
":  " + 
"(b('ndvi_med') <= 4738.75) ? " + 
"-0.08299928255786078" + 
":  " + 
"-0.06651033958468619" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 13.0) ? " + 
"(b('L8b3med') <= 765.5) ? " + 
"(b('L8b1med') <= 451.5) ? " + 
"0.033048693799204276" + 
":  " + 
"0.025786310342001406" + 
":  " + 
"0.051143018454731515" + 
":  " + 
"(b('L8b2med') <= 387.0) ? " + 
"(b('L8b7med') <= 1590.0) ? " + 
"0.008631680402920512" + 
":  " + 
"0.0598337102830043" + 
":  " + 
"(b('L8b3med') <= 852.5) ? " + 
"-0.007148155047628252" + 
":  " + 
"0.0017003832739176986" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1228.0) ? " + 
"(b('L8b3med') <= 1046.0) ? " + 
"(b('L8b7med') <= 1765.5) ? " + 
"0.0036035610300532584" + 
":  " + 
"-0.006549153730783976" + 
":  " + 
"(b('svvk3') <= -0.002754038665443659) ? " + 
"0.03871128491165298" + 
":  " + 
"0.005241749308492615" + 
":  " + 
"(b('lat') <= 41.30295944213867) ? " + 
"(b('svvk3') <= -0.015828943345695734) ? " + 
"0.03414533212541977" + 
":  " + 
"-0.004148662067500821" + 
":  " + 
"(b('lon') <= -5.488860130310059) ? " + 
"-0.011735571765021975" + 
":  " + 
"-0.04624189113541934" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"-0.049826904439704015" + 
":  " + 
"(b('bulk') <= 103.5) ? " + 
"(b('lat') <= 32.84714984893799) ? " + 
"-0.05717022078712358" + 
":  " + 
"-0.023680362494685046" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"0.11357009072659974" + 
":  " + 
"0.00033900585487575506" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 4.0) ? " + 
"-0.06715052855338022" + 
":  " + 
"(b('lon') <= -110.6124038696289) ? " + 
"(b('svvk3') <= -0.006420243764296174) ? " + 
"-0.03280689346176778" + 
":  " + 
"-0.0028312776934876116" + 
":  " + 
"(b('bulk') <= 161.5) ? " + 
"0.0021091073799458853" + 
":  " + 
"0.09823900656392223" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 25.446617126464844) ? " + 
"(b('L8b7med') <= 2280.5) ? " + 
"0.0024780484309829356" + 
":  " + 
"-0.0047440255068788625" + 
":  " + 
"(b('svvk3') <= -0.004009620635770261) ? " + 
"-0.07970146082475588" + 
":  " + 
"-0.064548595763428" + 
":  " + 
"(b('L8b3med') <= 663.5) ? " + 
"(b('lat') <= 39.09149932861328) ? " + 
"0.013794529970625025" + 
":  " + 
"-0.0067101879449442264" + 
":  " + 
"0.10539588731512489" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 24.5) ? " + 
"(b('clay') <= 22.5) ? " + 
"(b('lat') <= 32.78899002075195) ? " + 
"-0.03408838764945023" + 
":  " + 
"0.0018775564283646218" + 
":  " + 
"(b('bulk') <= 117.0) ? " + 
"0.10175436607284694" + 
":  " + 
"-0.016872162538588403" + 
":  " + 
"(b('L8b3med') <= 779.0) ? " + 
"(b('clay') <= 28.5) ? " + 
"0.03924092974410653" + 
":  " + 
"0.0047603794244113155" + 
":  " + 
"(b('L8b1med') <= 393.25) ? " + 
"-0.02805010285447138" + 
":  " + 
"0.005124018500816509" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.1269880346953869) ? " + 
"(b('gvvk2') <= 0.5738271176815033) ? " + 
"(b('L8b7med') <= 2543.0) ? " + 
"0.0014890480687591438" + 
":  " + 
"-0.006686056131337649" + 
":  " + 
"(b('lat') <= 46.25018501281738) ? " + 
"0.06486943658605906" + 
":  " + 
"0.013636679255469707" + 
":  " + 
"(b('lat') <= 0.39439964294433594) ? " + 
"0.03244963845214682" + 
":  " + 
"(b('clay') <= 17.5) ? " + 
"-0.04155465288861774" + 
":  " + 
"-0.013216417111849753" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 103.5) ? " + 
"(b('sand') <= 58.0) ? " + 
"(b('L8b7med') <= 1088.5) ? " + 
"-0.0283981762805956" + 
":  " + 
"-0.01970155640732223" + 
":  " + 
"-0.048651980331435" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"0.09143002465868633" + 
":  " + 
"(b('L8b7med') <= 1355.0) ? " + 
"0.016113995864163094" + 
":  " + 
"-0.000713509304991215" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"-0.04247702129821493" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.060912161297615355" + 
":  " + 
"(b('L8b7med') <= 2543.0) ? " + 
"0.0015450069957289243" + 
":  " + 
"-0.0058345231744128786" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.010399458464235067) ? " + 
"(b('bulk') <= 163.5) ? " + 
"(b('clay') <= 19.5) ? " + 
"-0.004339326378774163" + 
":  " + 
"0.023702943826323562" + 
":  " + 
"(b('ndvi_med') <= 1808.0) ? " + 
"-0.07536896410671048" + 
":  " + 
"-0.06913711987183027" + 
":  " + 
"(b('svvk3') <= -0.008770964108407497) ? " + 
"(b('L8b3med') <= 751.75) ? " + 
"-0.07215112496106643" + 
":  " + 
"-0.04100001967946884" + 
":  " + 
"(b('sand') <= 68.5) ? " + 
"0.0004905090382665387" + 
":  " + 
"-0.010457633783367264" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 4848.5) ? " + 
"(b('ndvi_med') <= 4469.0) ? " + 
"(b('ndvi_med') <= 4424.5) ? " + 
"-0.00025137689527313903" + 
":  " + 
"0.04641089522922833" + 
":  " + 
"(b('bulk') <= 132.5) ? " + 
"-0.037188845314504046" + 
":  " + 
"-0.006951266694126494" + 
":  " + 
"(b('lat') <= 55.933950424194336) ? " + 
"(b('bulk') <= 110.0) ? " + 
"0.00037141442868987573" + 
":  " + 
"0.02733472824865769" + 
":  " + 
"(b('svvk3') <= -0.013070219662040472) ? " + 
"-0.03978157401296306" + 
":  " + 
"-0.033017770455927076" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 25.446617126464844) ? " + 
"(b('lon') <= -110.6124038696289) ? " + 
"-0.0040653328691013235" + 
":  " + 
"0.0021111298496226663" + 
":  " + 
"(b('ndvi_med') <= 4738.75) ? " + 
"-0.06133927693623524" + 
":  " + 
"-0.05004477456276185" + 
":  " + 
"(b('lat') <= 39.5146484375) ? " + 
"(b('gvvk2') <= 0.24988791346549988) ? " + 
"-0.002789145741612195" + 
":  " + 
"0.008235016208902879" + 
":  " + 
"0.09441257515052692" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 4.0) ? " + 
"-0.05664670826924337" + 
":  " + 
"(b('sand') <= 77.5) ? " + 
"(b('sand') <= 68.5) ? " + 
"0.0005854730783527185" + 
":  " + 
"-0.015284526695569263" + 
":  " + 
"(b('lon') <= 9.170949935913086) ? " + 
"0.006032975402934737" + 
":  " + 
"0.07316962857729531" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 103.5) ? " + 
"(b('sand') <= 58.0) ? " + 
"(b('svvk3') <= 0.00658504175953567) ? " + 
"-0.021770707280679837" + 
":  " + 
"-0.010983621955546474" + 
":  " + 
"-0.044234856504961284" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"0.08183894798614788" + 
":  " + 
"(b('L8b3med') <= 719.0) ? " + 
"0.007933345236145448" + 
":  " + 
"-0.001097771809333447" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 928.75) ? " + 
"(b('L8b7med') <= 1611.75) ? " + 
"(b('ndvi_med') <= 3582.0) ? " + 
"0.011570694672346536" + 
":  " + 
"-0.009040228837994295" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"0.07365505318753307" + 
":  " + 
"-0.009073963351842488" + 
":  " + 
"(b('L8b3med') <= 932.5) ? " + 
"(b('sand') <= 34.5) ? " + 
"0.08491780483343114" + 
":  " + 
"0.10812202780294738" + 
":  " + 
"(b('ndvi_med') <= 1920.5) ? " + 
"-0.0024128323444863446" + 
":  " + 
"0.012133500433822015" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.23104858398438) ? " + 
"(b('lon') <= 29.155349731445312) ? " + 
"0.05679628254669036" + 
":  " + 
"0.030522888234045215" + 
":  " + 
"(b('lat') <= -34.78766059875488) ? " + 
"-0.003903109410566652" + 
":  " + 
"-0.018299592010057555" + 
":  " + 
"(b('lat') <= 32.18929862976074) ? " + 
"(b('lat') <= -5.20074987411499) ? " + 
"-0.00888367889069118" + 
":  " + 
"-0.03988053050052559" + 
":  " + 
"(b('lon') <= 24.045809745788574) ? " + 
"0.0013082969125979259" + 
":  " + 
"-0.027488059295057998" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"-0.037685015679495726" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.055365248656751534" + 
":  " + 
"(b('svvk3') <= 0.1269880346953869) ? " + 
"0.00043938131874961066" + 
":  " + 
"-0.01745176556920596" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.3110143393278122) ? " + 
"(b('lat') <= 36.15193557739258) ? " + 
"(b('L8b7med') <= 1778.25) ? " + 
"0.047631361340689904" + 
":  " + 
"0.0013249456081185645" + 
":  " + 
"(b('svvk3') <= -0.004958576988428831) ? " + 
"-0.02697430159328438" + 
":  " + 
"-0.0033634054234211006" + 
":  " + 
"(b('gvvk2') <= 0.3117894232273102) ? " + 
"(b('L8b3med') <= 935.0) ? " + 
"0.05677470470177717" + 
":  " + 
"0.07528441956677204" + 
":  " + 
"(b('trees') <= 32.622979164123535) ? " + 
"0.0015087291407736923" + 
":  " + 
"0.08484869086468907" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 13.0) ? " + 
"(b('svvk3') <= 0.007800380466505885) ? " + 
"(b('L8b6med') <= 2113.5) ? " + 
"0.02615485750935309" + 
":  " + 
"0.02006708116536715" + 
":  " + 
"0.03865557209534293" + 
":  " + 
"(b('L8b3med') <= 852.5) ? " + 
"(b('L8b7med') <= 1794.75) ? " + 
"-2.5412743920479546e-05" + 
":  " + 
"-0.01802245387182051" + 
":  " + 
"(b('ndvi_med') <= 1920.5) ? " + 
"-0.0024246184234896473" + 
":  " + 
"0.008882645660432216" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.23104858398438) ? " + 
"(b('bulk') <= 148.5) ? " + 
"0.02836006935376087" + 
":  " + 
"0.05005195703329132" + 
":  " + 
"(b('L8b7med') <= 3010.5) ? " + 
"-0.016421982012655156" + 
":  " + 
"-0.0034651476731133446" + 
":  " + 
"(b('lat') <= 32.18929862976074) ? " + 
"(b('lat') <= -5.20074987411499) ? " + 
"-0.007929281851959916" + 
":  " + 
"-0.0359218163519304" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"0.0010971464572198271" + 
":  " + 
"-0.02705289708213433" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 0.03652967885136604) ? " + 
"(b('gvvk2') <= 0.40319129824638367) ? " + 
"(b('bulk') <= 163.5) ? " + 
"-0.0004295807387261984" + 
":  " + 
"-0.0335191775628144" + 
":  " + 
"(b('gvvk2') <= 0.40442870557308197) ? " + 
"0.08594319731237601" + 
":  " + 
"0.011744174148296274" + 
":  " + 
"(b('gvvk2') <= 0.40793170034885406) ? " + 
"(b('ndvi_med') <= 2723.0) ? " + 
"-0.006611025468735249" + 
":  " + 
"0.006474153212234768" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"-0.026421170155236363" + 
":  " + 
"-0.0032171867550142065" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 24.5) ? " + 
"(b('clay') <= 22.5) ? " + 
"(b('L8b3med') <= 928.75) ? " + 
"-0.003701451715669646" + 
":  " + 
"0.005800685619763861" + 
":  " + 
"(b('bulk') <= 117.0) ? " + 
"0.06589969183411032" + 
":  " + 
"-0.01397617813925039" + 
":  " + 
"(b('lon') <= -120.32480239868164) ? " + 
"(b('L8b6med') <= 3208.75) ? " + 
"-0.059720377953959985" + 
":  " + 
"-0.0024610793447984226" + 
":  " + 
"(b('lon') <= 1.383899986743927) ? " + 
"0.013604585211527038" + 
":  " + 
"-0.005338225116945148" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.22988472878932953) ? " + 
"(b('bulk') <= 133.5) ? " + 
"(b('L8b3med') <= 708.5) ? " + 
"0.002248243781508586" + 
":  " + 
"-0.025029982437399304" + 
":  " + 
"(b('bulk') <= 134.5) ? " + 
"0.07336852588508488" + 
":  " + 
"-0.001135095331940131" + 
":  " + 
"(b('gvvk2') <= 0.2307891771197319) ? " + 
"0.06921827690317622" + 
":  " + 
"(b('L8b7med') <= 2543.0) ? " + 
"0.0028556788722084118" + 
":  " + 
"-0.005863610063544263" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.23104858398438) ? " + 
"(b('ndvi_med') <= 1900.25) ? " + 
"0.026728255624591354" + 
":  " + 
"0.04681991380353989" + 
":  " + 
"(b('svvk3') <= 0.0372368972748518) ? " + 
"-0.01361664221946808" + 
":  " + 
"-0.0016464190773800014" + 
":  " + 
"(b('lat') <= 32.39724922180176) ? " + 
"(b('L8b1med') <= 354.5) ? " + 
"-0.011965237777104037" + 
":  " + 
"-0.031560289288038376" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"0.001008265171247637" + 
":  " + 
"-0.023763578504843275" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.1269880346953869) ? " + 
"(b('gvvk2') <= 0.5738271176815033) ? " + 
"(b('gvvk2') <= 0.5704429149627686) ? " + 
"-3.6855190424364427e-05" + 
":  " + 
"-0.058404713163432515" + 
":  " + 
"(b('lat') <= 46.25018501281738) ? " + 
"0.05720784189764988" + 
":  " + 
"0.011082486611032567" + 
":  " + 
"(b('clay') <= 17.5) ? " + 
"(b('L8b2med') <= 491.5) ? " + 
"-0.04800638855447348" + 
":  " + 
"-0.025483914473886326" + 
":  " + 
"(b('svvk3') <= 0.22790219634771347) ? " + 
"-0.009978162186866386" + 
":  " + 
"0.023138375030329422" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 852.5) ? " + 
"(b('L8b7med') <= 1794.75) ? " + 
"(b('trees') <= 19.810494422912598) ? " + 
"0.003633628456963128" + 
":  " + 
"-0.017997284057798275" + 
":  " + 
"(b('L8b2med') <= 513.75) ? " + 
"-0.04583472089002668" + 
":  " + 
"-0.007087344461044399" + 
":  " + 
"(b('ndvi_med') <= 1920.5) ? " + 
"(b('svvk3') <= 0.0381929948925972) ? " + 
"-0.004813348441382107" + 
":  " + 
"0.008169241738669125" + 
":  " + 
"(b('svvk3') <= -0.002357953228056431) ? " + 
"0.021326997286500917" + 
":  " + 
"0.0028614257028938207" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 25.446617126464844) ? " + 
"(b('bulk') <= 103.5) ? " + 
"-0.020167182637082885" + 
":  " + 
"0.0004107504862323582" + 
":  " + 
"(b('ndvi_med') <= 4738.75) ? " + 
"-0.05163953487798797" + 
":  " + 
"-0.0428908956308906" + 
":  " + 
"(b('lat') <= 39.5146484375) ? " + 
"(b('ndvi_med') <= 4168.5) ? " + 
"0.004866108315306095" + 
":  " + 
"-0.0011998244359490012" + 
":  " + 
"0.07739639777771037" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"-0.031550222154152735" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.049748494269414426" + 
":  " + 
"(b('L8b6med') <= 3349.5) ? " + 
"0.0013941288288596288" + 
":  " + 
"-0.0038491340485318" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('sand') <= 68.5) ? " + 
"(b('lat') <= 55.933950424194336) ? " + 
"0.0007312317635854703" + 
":  " + 
"-0.029636065169254946" + 
":  " + 
"(b('lat') <= 56.04010009765625) ? " + 
"-0.01708107382437612" + 
":  " + 
"0.011037029781074056" + 
":  " + 
"(b('L8b3med') <= 623.0) ? " + 
"(b('svvk3') <= -0.0008742376230657101) ? " + 
"0.07421305537983397" + 
":  " + 
"0.050318180236184784" + 
":  " + 
"(b('lat') <= 55.906049728393555) ? " + 
"-0.01603546753270045" + 
":  " + 
"0.010119028548439058" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.23104858398438) ? " + 
"(b('lon') <= 146.01818084716797) ? " + 
"0.033573424687777985" + 
":  " + 
"0.017457637438807877" + 
":  " + 
"(b('L8b7med') <= 3010.5) ? " + 
"-0.011499242454469219" + 
":  " + 
"-0.0020243006445950784" + 
":  " + 
"(b('lat') <= 32.39724922180176) ? " + 
"(b('svvk3') <= 0.010638921754434705) ? " + 
"-0.01566325896125717" + 
":  " + 
"-0.0305818161748631" + 
":  " + 
"(b('lon') <= 24.045809745788574) ? " + 
"0.000953538288595668" + 
":  " + 
"-0.01994648114367903" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 4848.5) ? " + 
"(b('ndvi_med') <= 4469.0) ? " + 
"(b('ndvi_med') <= 4424.5) ? " + 
"-0.00019039869562776987" + 
":  " + 
"0.03443020475759397" + 
":  " + 
"(b('ndvi_med') <= 4704.5) ? " + 
"-0.02981172084173273" + 
":  " + 
"-0.00571749866677289" + 
":  " + 
"(b('svvk3') <= 0.006215157685801387) ? " + 
"(b('clay') <= 13.0) ? " + 
"0.02134651234081805" + 
":  " + 
"-0.012712055760814918" + 
":  " + 
"(b('svvk3') <= 0.01217995211482048) ? " + 
"0.038477629416135424" + 
":  " + 
"0.01948981587772024" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 25.446617126464844) ? " + 
"(b('L8b3med') <= 852.5) ? " + 
"-0.002404905303861976" + 
":  " + 
"0.0017881123262062238" + 
":  " + 
"(b('clay') <= 18.0) ? " + 
"-0.04031609514466174" + 
":  " + 
"-0.048272486402755305" + 
":  " + 
"(b('lon') <= -77.63019943237305) ? " + 
"(b('svvk3') <= -0.000584535562666133) ? " + 
"-0.000815982013780886" + 
":  " + 
"0.004090647465234187" + 
":  " + 
"0.06936790798139805" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"-0.02872344830701342" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.04444539647419704" + 
":  " + 
"(b('L8b6med') <= 3349.5) ? " + 
"0.0013344932333579805" + 
":  " + 
"-0.003682419965308679" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.22988472878932953) ? " + 
"(b('bulk') <= 133.5) ? " + 
"(b('L8b3med') <= 708.5) ? " + 
"0.0016584156810737854" + 
":  " + 
"-0.021698794947931352" + 
":  " + 
"(b('bulk') <= 134.5) ? " + 
"0.06534828559268357" + 
":  " + 
"-0.0008048918070887242" + 
":  " + 
"(b('gvvk2') <= 0.2307891771197319) ? " + 
"0.06161306150896584" + 
":  " + 
"(b('L8b7med') <= 2935.5) ? " + 
"0.0017193335573481773" + 
":  " + 
"-0.009831828563253221" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.1269880346953869) ? " + 
"(b('gvvk2') <= 0.5491317212581635) ? " + 
"(b('gvvk2') <= 0.5375914573669434) ? " + 
"-7.653391981702813e-05" + 
":  " + 
"-0.028172681482622242" + 
":  " + 
"(b('lon') <= -103.03784942626953) ? " + 
"0.05455585336154947" + 
":  " + 
"0.008379328833444053" + 
":  " + 
"(b('lon') <= 77.70406484603882) ? " + 
"(b('L8b7med') <= 1688.5) ? " + 
"-0.0063198357156714164" + 
":  " + 
"-0.02407021937062889" + 
":  " + 
"0.018569102067158394" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 923.5) ? " + 
"(b('L8b3med') <= 899.25) ? " + 
"(b('trees') <= 19.598620414733887) ? " + 
"0.0007768560391342729" + 
":  " + 
"-0.012214026488928486" + 
":  " + 
"(b('L8b3med') <= 909.0) ? " + 
"-0.036001875845805054" + 
":  " + 
"-0.010390849237674558" + 
":  " + 
"(b('L8b2med') <= 628.5) ? " + 
"(b('L8b3med') <= 932.5) ? " + 
"0.07691277658866878" + 
":  " + 
"0.010511219293886879" + 
":  " + 
"(b('ndvi_med') <= 3819.25) ? " + 
"-0.0011227236980421672" + 
":  " + 
"0.031983932188991274" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 25.446617126464844) ? " + 
"(b('bulk') <= 119.5) ? " + 
"0.005872737887837413" + 
":  " + 
"-0.0006055443041640359" + 
":  " + 
"(b('svvk3') <= 0.0028934471774846315) ? " + 
"-0.03931392157653077" + 
":  " + 
"-0.033382663212958213" + 
":  " + 
"(b('L8b6med') <= 2496.75) ? " + 
"0.06335479054506216" + 
":  " + 
"(b('lon') <= -93.13629913330078) ? " + 
"0.00019538133702858007" + 
":  " + 
"0.004605256080514708" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.23104858398438) ? " + 
"(b('ndvi_med') <= 1531.0) ? " + 
"0.01499660936551886" + 
":  " + 
"0.030256468221896288" + 
":  " + 
"(b('L8b7med') <= 3010.5) ? " + 
"-0.008977184527021634" + 
":  " + 
"-0.0004497368981349059" + 
":  " + 
"(b('lat') <= 32.39724922180176) ? " + 
"(b('L8b1med') <= 354.5) ? " + 
"-0.009033796497027105" + 
":  " + 
"-0.02412350361077431" + 
":  " + 
"(b('lat') <= 32.848440170288086) ? " + 
"0.046873680335325685" + 
":  " + 
"3.9228661125367266e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('lon') <= -5.546385049819946) ? " + 
"(b('lon') <= -77.86024856567383) ? " + 
"0.00019974568241878024" + 
":  " + 
"0.02691163720124432" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"-0.026849420985053107" + 
":  " + 
"-0.0020992643095298037" + 
":  " + 
"(b('lon') <= 9.170949935913086) ? " + 
"(b('bulk') <= 130.0) ? " + 
"0.009775070355128177" + 
":  " + 
"-0.00708317647110613" + 
":  " + 
"(b('gvvk2') <= 0.36731019616127014) ? " + 
"0.06663714308624147" + 
":  " + 
"0.045131755456957245" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 103.5) ? " + 
"(b('L8b3med') <= 678.0) ? " + 
"(b('lon') <= -78.12623977661133) ? " + 
"-0.025322382601399518" + 
":  " + 
"-0.028618185622547088" + 
":  " + 
"(b('L8b7med') <= 1764.0) ? " + 
"-0.011514955126563017" + 
":  " + 
"-0.015135080780362853" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"0.05481644111689837" + 
":  " + 
"(b('L8b7med') <= 1355.0) ? " + 
"0.010055209756383523" + 
":  " + 
"-0.00042111845015030327" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 852.5) ? " + 
"(b('L8b7med') <= 1794.75) ? " + 
"(b('lon') <= -120.79459762573242) ? " + 
"0.06750177085211001" + 
":  " + 
"-0.0003530819527023052" + 
":  " + 
"(b('L8b2med') <= 513.75) ? " + 
"-0.03996418102091059" + 
":  " + 
"-0.006098644635527487" + 
":  " + 
"(b('trees') <= 17.929956436157227) ? " + 
"(b('trees') <= 13.198651313781738) ? " + 
"0.001547409628524755" + 
":  " + 
"-0.01898818395269277" + 
":  " + 
"(b('sand') <= 38.5) ? " + 
"0.07716491983268495" + 
":  " + 
"0.014230140236854" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('L8b1med') <= 172.5) ? " + 
"-0.03039604923295916" + 
":  " + 
"-0.02572105886502213" + 
":  " + 
"(b('L8b3med') <= 562.5) ? " + 
"(b('gvvk2') <= 0.1796317920088768) ? " + 
"0.022851018472687612" + 
":  " + 
"0.03757163488083501" + 
":  " + 
"(b('trees') <= 0.03652967885136604) ? " + 
"0.002213547079595028" + 
":  " + 
"-0.002024986326068446" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.22988472878932953) ? " + 
"(b('lat') <= 43.55412483215332) ? " + 
"(b('L8b1med') <= 318.875) ? " + 
"0.056388811338555056" + 
":  " + 
"-0.0004143588349887028" + 
":  " + 
"(b('L8b3med') <= 711.5) ? " + 
"0.0013654111859104467" + 
":  " + 
"-0.01719213251879512" + 
":  " + 
"(b('gvvk2') <= 0.2307891771197319) ? " + 
"0.05101485364767161" + 
":  " + 
"(b('L8b7med') <= 2559.5) ? " + 
"0.002147131770682269" + 
":  " + 
"-0.004429339814929962" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 852.5) ? " + 
"(b('L8b2med') <= 625.5) ? " + 
"(b('gvvk2') <= 0.3372344970703125) ? " + 
"0.00204798881821021" + 
":  " + 
"-0.006920688493435965" + 
":  " + 
"(b('gvvk2') <= 0.11209814995527267) ? " + 
"-0.029872988016260565" + 
":  " + 
"-0.06755027853983282" + 
":  " + 
"(b('trees') <= 17.929956436157227) ? " + 
"(b('trees') <= 13.198651313781738) ? " + 
"0.0014106573227998292" + 
":  " + 
"-0.016949280732030152" + 
":  " + 
"(b('L8b6med') <= 3151.5) ? " + 
"0.005119025009334192" + 
":  " + 
"0.033031002825757556" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.3110143393278122) ? " + 
"(b('lat') <= 36.29348564147949) ? " + 
"(b('L8b7med') <= 1778.25) ? " + 
"0.03529247263561868" + 
":  " + 
"0.002165344928162171" + 
":  " + 
"(b('svvk3') <= -0.004958576988428831) ? " + 
"-0.01957611962508605" + 
":  " + 
"-0.0027340159023694854" + 
":  " + 
"(b('gvvk2') <= 0.3117894232273102) ? " + 
"(b('svvk3') <= -0.009993746178224683) ? " + 
"0.06235818034011956" + 
":  " + 
"0.04672774401001514" + 
":  " + 
"(b('L8b2med') <= 552.5) ? " + 
"-0.004081448307659502" + 
":  " + 
"0.004536795464749365" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 13.0) ? " + 
"(b('L8b6med') <= 2628.25) ? " + 
"(b('svvk3') <= -0.08300493098795414) ? " + 
"0.012284094415468405" + 
":  " + 
"0.01867205538158409" + 
":  " + 
"0.0278999108685849" + 
":  " + 
"(b('sand') <= 77.5) ? " + 
"(b('L8b6med') <= 2572.5) ? " + 
"-0.005286312312107618" + 
":  " + 
"0.0008355406047332219" + 
":  " + 
"(b('L8b3med') <= 623.0) ? " + 
"0.0484339596393743" + 
":  " + 
"0.0037779359561718392" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"-0.02585779768256974" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.03950422653746652" + 
":  " + 
"(b('L8b7med') <= 2468.0) ? " + 
"0.0010657634135404534" + 
":  " + 
"-0.003427743508659835" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.23104858398438) ? " + 
"(b('lon') <= 146.01818084716797) ? " + 
"0.027581193350183202" + 
":  " + 
"0.013692226697536919" + 
":  " + 
"(b('L8b7med') <= 3010.5) ? " + 
"-0.008096114476032715" + 
":  " + 
"-0.00020948493975148086" + 
":  " + 
"(b('lon') <= 24.045809745788574) ? " + 
"(b('lat') <= 32.39724922180176) ? " + 
"-0.018758861784916165" + 
":  " + 
"0.0007619241746914433" + 
":  " + 
"(b('lat') <= 44.097700119018555) ? " + 
"-0.027784098455631817" + 
":  " + 
"-0.01060742450579364" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.5717740952968597) ? " + 
"(b('gvvk2') <= 0.5704429149627686) ? " + 
"(b('svvk3') <= -0.027715977281332016) ? " + 
"-0.007730567844089483" + 
":  " + 
"0.00028502254304939214" + 
":  " + 
"-0.052348043707289335" + 
":  " + 
"(b('lat') <= 55.97895050048828) ? " + 
"(b('L8b1med') <= 552.5) ? " + 
"0.011130030318396739" + 
":  " + 
"0.03712444694878931" + 
":  " + 
"(b('L8b6med') <= 2599.25) ? " + 
"-0.014910642751233306" + 
":  " + 
"-0.0014721811835130272" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 13.0) ? " + 
"(b('L8b6med') <= 2628.25) ? " + 
"(b('ndvi_med') <= 1394.25) ? " + 
"0.011645972999507315" + 
":  " + 
"0.016994358349654515" + 
":  " + 
"0.024898648768598264" + 
":  " + 
"(b('gvvk2') <= 0.03510967455804348) ? " + 
"0.034851816909196975" + 
":  " + 
"(b('L8b6med') <= 2273.25) ? " + 
"-0.007318270141431886" + 
":  " + 
"0.00032053092075321344" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('L8b7med') <= 1434.5) ? " + 
"(b('clay') <= 24.5) ? " + 
"-0.015094719738559945" + 
":  " + 
"0.014329911596695688" + 
":  " + 
"(b('L8b7med') <= 1510.0) ? " + 
"0.01862423932741419" + 
":  " + 
"-0.0005284791358807503" + 
":  " + 
"(b('L8b3med') <= 623.0) ? " + 
"(b('svvk3') <= -0.0008742376230657101) ? " + 
"0.05500449506375649" + 
":  " + 
"0.03168998407671031" + 
":  " + 
"(b('lat') <= 55.906049728393555) ? " + 
"-0.008648938077368612" + 
":  " + 
"0.00761517547906881" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.0020157683175057173) ? " + 
"(b('lon') <= -115.53428649902344) ? " + 
"(b('clay') <= 28.0) ? " + 
"-0.008735675262932207" + 
":  " + 
"-0.05371751816123994" + 
":  " + 
"(b('svvk3') <= -0.0029593120561912656) ? " + 
"0.0035818480369738657" + 
":  " + 
"0.029870830807041795" + 
":  " + 
"(b('bulk') <= 106.5) ? " + 
"(b('sand') <= 40.0) ? " + 
"-0.043496151977507336" + 
":  " + 
"-0.00739085667453609" + 
":  " + 
"(b('L8b7med') <= 1608.0) ? " + 
"0.004967369198367139" + 
":  " + 
"-0.002168713722662203" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 923.5) ? " + 
"(b('L8b3med') <= 899.25) ? " + 
"(b('lon') <= 22.88466453552246) ? " + 
"0.00016821569716767926" + 
":  " + 
"-0.01398494045784341" + 
":  " + 
"(b('L8b3med') <= 909.0) ? " + 
"-0.03166104416372818" + 
":  " + 
"-0.009108003371290732" + 
":  " + 
"(b('ndvi_med') <= 1920.5) ? " + 
"(b('ndvi_med') <= 1700.0) ? " + 
"0.0008564782236650351" + 
":  " + 
"-0.011943433668591921" + 
":  " + 
"(b('L8b3med') <= 1228.0) ? " + 
"0.010675923818077372" + 
":  " + 
"-0.03378336174943953" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.03547702915966511) ? " + 
"(b('svvk3') <= 0.03259287588298321) ? " + 
"(b('L8b3med') <= 562.5) ? " + 
"0.02492316165043466" + 
":  " + 
"-0.00045770480245730115" + 
":  " + 
"(b('gvvk2') <= 0.5135599821805954) ? " + 
"-0.02527075907753459" + 
":  " + 
"0.010496824349903622" + 
":  " + 
"(b('trees') <= 12.70752239227295) ? " + 
"(b('svvk3') <= 0.04135633632540703) ? " + 
"0.018683586043523943" + 
":  " + 
"0.003332733264068992" + 
":  " + 
"(b('L8b3med') <= 902.5) ? " + 
"-0.01791272253517613" + 
":  " + 
"-0.0038677015726481523" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.22901411354541779) ? " + 
"(b('lat') <= 43.55412483215332) ? " + 
"(b('L8b2med') <= 641.25) ? " + 
"0.00939750445830063" + 
":  " + 
"-0.004234783509211825" + 
":  " + 
"(b('L8b3med') <= 723.5) ? " + 
"-8.281176543019815e-05" + 
":  " + 
"-0.01512374860315745" + 
":  " + 
"(b('L8b6med') <= 3802.25) ? " + 
"(b('sand') <= 47.5) ? " + 
"0.003967341416804875" + 
":  " + 
"-0.0021972734877460133" + 
":  " + 
"(b('L8b2med') <= 781.75) ? " + 
"0.022014912860713113" + 
":  " + 
"-0.011794136385045353" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 852.5) ? " + 
"(b('L8b2med') <= 625.5) ? " + 
"(b('L8b6med') <= 2871.5) ? " + 
"-0.0032662178413991974" + 
":  " + 
"0.009356271251701192" + 
":  " + 
"(b('svvk3') <= -0.00039357222703984007) ? " + 
"-0.027580248039521124" + 
":  " + 
"-0.06012658071398491" + 
":  " + 
"(b('trees') <= 17.929956436157227) ? " + 
"(b('trees') <= 13.198651313781738) ? " + 
"0.001227821558058444" + 
":  " + 
"-0.014642034058379744" + 
":  " + 
"(b('svvk3') <= 0.0022604166297242045) ? " + 
"0.007478311376538064" + 
":  " + 
"0.038509353176246715" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"-0.022878227539313303" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.03594759425871932" + 
":  " + 
"(b('gvvk2') <= 0.13317912071943283) ? " + 
"-0.007238827765847418" + 
":  " + 
"0.00039435055131791" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.5717740952968597) ? " + 
"(b('gvvk2') <= 0.5704429149627686) ? " + 
"(b('L8b3med') <= 925.5) ? " + 
"-0.001937406424838455" + 
":  " + 
"0.0015067640730991217" + 
":  " + 
"-0.04396901252571839" + 
":  " + 
"(b('bulk') <= 137.0) ? " + 
"(b('lat') <= 55.97895050048828) ? " + 
"0.009312639076468104" + 
":  " + 
"-0.00935662116374677" + 
":  " + 
"(b('L8b6med') <= 3644.5) ? " + 
"0.04417068303603966" + 
":  " + 
"0.010163297140607985" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 25.446617126464844) ? " + 
"(b('bulk') <= 119.5) ? " + 
"0.004856663930069738" + 
":  " + 
"-0.0004872950215026936" + 
":  " + 
"(b('trees') <= 27.291908264160156) ? " + 
"-0.029615530195977263" + 
":  " + 
"-0.03735372583278769" + 
":  " + 
"(b('svvk3') <= -3.257839853176847e-05) ? " + 
"(b('clay') <= 20.5) ? " + 
"0.0006670552818306974" + 
":  " + 
"0.002111177137506026" + 
":  " + 
"0.05263206476285742" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('lon') <= -5.546385049819946) ? " + 
"(b('lon') <= -77.86024856567383) ? " + 
"0.0001411162605776777" + 
":  " + 
"0.02158149156264897" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"-0.023120644106006838" + 
":  " + 
"-0.0014504888086256027" + 
":  " + 
"(b('L8b3med') <= 623.0) ? " + 
"(b('svvk3') <= -0.0008742376230657101) ? " + 
"0.04992419388662939" + 
":  " + 
"0.026264495236859253" + 
":  " + 
"(b('clay') <= 4.0) ? " + 
"-0.021056992572475702" + 
":  " + 
"0.0050319457702512095" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('sand') <= 52.0) ? " + 
"-0.021376738209095913" + 
":  " + 
"-0.023864683313221113" + 
":  " + 
"(b('L8b3med') <= 562.5) ? " + 
"(b('gvvk2') <= 0.1796317920088768) ? " + 
"0.015451392498119165" + 
":  " + 
"0.02513063036428337" + 
":  " + 
"(b('trees') <= 0.03652967885136604) ? " + 
"0.0018249449630523948" + 
":  " + 
"-0.0016067455127026353" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.01818084716797) ? " + 
"(b('L8b3med') <= 891.5) ? " + 
"0.01666477529992924" + 
":  " + 
"0.028598162350310007" + 
":  " + 
"(b('lon') <= 146.23104858398438) ? " + 
"0.010117672989170115" + 
":  " + 
"-0.0022855318507394077" + 
":  " + 
"(b('lat') <= 32.39724922180176) ? " + 
"(b('lon') <= -93.56679916381836) ? " + 
"-0.02562033560603577" + 
":  " + 
"-0.01048813961652266" + 
":  " + 
"(b('lat') <= 33.243980407714844) ? " + 
"0.028958342301228988" + 
":  " + 
"-3.39662941272773e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 852.5) ? " + 
"(b('L8b7med') <= 1794.75) ? " + 
"(b('lon') <= -120.79459762573242) ? " + 
"0.061539104836281056" + 
":  " + 
"-0.0001117003442348286" + 
":  " + 
"(b('L8b2med') <= 513.75) ? " + 
"-0.034072805503239226" + 
":  " + 
"-0.0044190960541733515" + 
":  " + 
"(b('trees') <= 17.929956436157227) ? " + 
"(b('svvk3') <= 0.03550765663385391) ? " + 
"-0.0012907561156150565" + 
":  " + 
"0.006517036203941601" + 
":  " + 
"(b('sand') <= 38.5) ? " + 
"0.06529986676453352" + 
":  " + 
"0.010374562327661542" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.18899917602539) ? " + 
"(b('gvvk2') <= 0.041203947737812996) ? " + 
"0.05538519435265296" + 
":  " + 
"(b('svvk3') <= -0.05287431553006172) ? " + 
"-0.053264811834068296" + 
":  " + 
"-0.002036279720988641" + 
":  " + 
"(b('lon') <= -71.2344970703125) ? " + 
"(b('clay') <= 19.5) ? " + 
"-0.006680317348822032" + 
":  " + 
"0.011961058756151366" + 
":  " + 
"(b('clay') <= 21.5) ? " + 
"0.0017037773666659939" + 
":  " + 
"-0.009028788830566415" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.0018616062588989735) ? " + 
"(b('lon') <= -115.53428649902344) ? " + 
"(b('clay') <= 28.0) ? " + 
"-0.007202093414565568" + 
":  " + 
"-0.045065630059424704" + 
":  " + 
"(b('L8b6med') <= 2915.5) ? " + 
"0.00033429505695031276" + 
":  " + 
"0.015320756963619826" + 
":  " + 
"(b('lat') <= 39.0578498840332) ? " + 
"(b('gvvk2') <= 0.13397134095430374) ? " + 
"-0.009870912605780552" + 
":  " + 
"0.003946173204472739" + 
":  " + 
"(b('L8b7med') <= 2918.0) ? " + 
"-0.0015130623782871428" + 
":  " + 
"-0.024631922575531214" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 852.5) ? " + 
"(b('L8b7med') <= 1611.75) ? " + 
"(b('gvvk2') <= 0.39237427711486816) ? " + 
"0.005501331281398405" + 
":  " + 
"-0.009755733614368102" + 
":  " + 
"(b('ndvi_med') <= 4889.25) ? " + 
"-0.008025140543398673" + 
":  " + 
"0.041274845162484974" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"(b('gvvk2') <= 0.31357690691947937) ? " + 
"-0.0018686279081549764" + 
":  " + 
"0.014288073243306438" + 
":  " + 
"(b('L8b7med') <= 1770.5) ? " + 
"0.01809067195089479" + 
":  " + 
"-0.0023332856690991954" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('ndvi_med') <= 1531.0) ? " + 
"(b('L8b7med') <= 2788.25) ? " + 
"0.009586181815356067" + 
":  " + 
"-0.0017068324125551388" + 
":  " + 
"(b('L8b2med') <= 618.0) ? " + 
"0.016750982992302932" + 
":  " + 
"0.02621862224038196" + 
":  " + 
"(b('lon') <= 24.045809745788574) ? " + 
"(b('lat') <= 32.18929862976074) ? " + 
"-0.015775379407237194" + 
":  " + 
"0.0004997444605200101" + 
":  " + 
"(b('L8b3med') <= 843.25) ? " + 
"-0.018266714330473454" + 
":  " + 
"-0.005762590627593693" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('L8b7med') <= 1434.5) ? " + 
"(b('L8b7med') <= 1407.5) ? " + 
"-0.0023211277218649485" + 
":  " + 
"-0.03491581378472787" + 
":  " + 
"(b('L8b7med') <= 1510.0) ? " + 
"0.01464739454480191" + 
":  " + 
"-0.0003601286899114463" + 
":  " + 
"(b('L8b3med') <= 623.0) ? " + 
"(b('svvk3') <= -0.0008742376230657101) ? " + 
"0.044303100896519454" + 
":  " + 
"0.02052037026755149" + 
":  " + 
"(b('ndvi_med') <= 3846.5) ? " + 
"-0.002323703013390552" + 
":  " + 
"0.008530782039619739" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 0.03652967885136604) ? " + 
"(b('gvvk2') <= 0.40319129824638367) ? " + 
"(b('bulk') <= 163.5) ? " + 
"-0.000511893747553568" + 
":  " + 
"-0.02230516598301696" + 
":  " + 
"(b('gvvk2') <= 0.40442870557308197) ? " + 
"0.0741654617081299" + 
":  " + 
"0.007364533679691038" + 
":  " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"(b('lat') <= 40.44004440307617) ? " + 
"0.0055408122895283535" + 
":  " + 
"-0.020665809416642096" + 
":  " + 
"(b('gvvk2') <= 0.40995487570762634) ? " + 
"0.003020721530016807" + 
":  " + 
"-0.007503944368642848" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"-0.020823782143342504" + 
":  " + 
"(b('L8b3med') <= 719.0) ? " + 
"(b('L8b3med') <= 701.75) ? " + 
"0.0004608787311129928" + 
":  " + 
"0.023710668788920558" + 
":  " + 
"(b('L8b3med') <= 812.5) ? " + 
"-0.005348042743652229" + 
":  " + 
"0.0009512360138761557" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.0020157683175057173) ? " + 
"(b('lon') <= -115.53428649902344) ? " + 
"(b('clay') <= 28.0) ? " + 
"-0.006651129477357114" + 
":  " + 
"-0.038204307066719095" + 
":  " + 
"(b('L8b1med') <= 427.5) ? " + 
"-0.0013934500268956839" + 
":  " + 
"0.011319473128364968" + 
":  " + 
"(b('bulk') <= 106.5) ? " + 
"(b('sand') <= 40.0) ? " + 
"-0.037483010316915255" + 
":  " + 
"-0.0063654542571834226" + 
":  " + 
"(b('L8b7med') <= 1608.0) ? " + 
"0.004024681597143714" + 
":  " + 
"-0.0017737080300698985" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('sand') <= 47.5) ? " + 
"0.0029110969805944934" + 
":  " + 
"-0.0046467752745167415" + 
":  " + 
"(b('lon') <= 6.412564992904663) ? " + 
"-0.027519304106991938" + 
":  " + 
"-0.0015842448869365197" + 
":  " + 
"(b('L8b3med') <= 623.0) ? " + 
"(b('L8b3med') <= 581.0) ? " + 
"0.017717705054969002" + 
":  " + 
"0.03966397578344416" + 
":  " + 
"(b('gvvk2') <= 0.5927262902259827) ? " + 
"0.0008692085870893092" + 
":  " + 
"0.013001649049181621" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 923.5) ? " + 
"(b('lon') <= -97.97296905517578) ? " + 
"(b('gvvk2') <= 0.5443800985813141) ? " + 
"-0.008449529715406745" + 
":  " + 
"0.04214210477910736" + 
":  " + 
"(b('gvvk2') <= 0.3372344970703125) ? " + 
"0.005091201905401717" + 
":  " + 
"-0.004527070263149595" + 
":  " + 
"(b('clay') <= 22.5) ? " + 
"(b('gvvk2') <= 0.29324179887771606) ? " + 
"-0.001172280810337928" + 
":  " + 
"0.009085559831991146" + 
":  " + 
"(b('clay') <= 25.5) ? " + 
"-0.013645252193997077" + 
":  " + 
"0.003336759697238501" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3349.5) ? " + 
"(b('L8b6med') <= 3148.25) ? " + 
"(b('lon') <= -97.97296905517578) ? " + 
"-0.004579188579668942" + 
":  " + 
"0.0022113394179292234" + 
":  " + 
"(b('ndvi_med') <= 1647.5) ? " + 
"-0.003575314349228427" + 
":  " + 
"0.02315179947311393" + 
":  " + 
"(b('L8b6med') <= 3369.5) ? " + 
"(b('bulk') <= 147.5) ? " + 
"-0.015832006465400172" + 
":  " + 
"-0.03706165203265256" + 
":  " + 
"(b('gvvk2') <= 0.5881716310977936) ? " + 
"-0.0019094258061745026" + 
":  " + 
"0.03898960187774428" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.406574964523315) ? " + 
"(b('lon') <= -97.97296905517578) ? " + 
"(b('L8b3med') <= 813.5) ? " + 
"-0.012373195877868393" + 
":  " + 
"0.0011421870722451342" + 
":  " + 
"(b('gvvk2') <= 0.3408670127391815) ? " + 
"0.014455947022679539" + 
":  " + 
"-0.003428263934046682" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"(b('ndvi_med') <= 1463.75) ? " + 
"-0.028769847172789603" + 
":  " + 
"-0.03300138854405722" + 
":  " + 
"(b('lat') <= 43.73078536987305) ? " + 
"0.009578021964694972" + 
":  " + 
"-0.003069448534319154" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('L8b7med') <= 1434.5) ? " + 
"(b('clay') <= 24.5) ? " + 
"-0.011751548774862425" + 
":  " + 
"0.009790881070105542" + 
":  " + 
"(b('L8b7med') <= 1510.0) ? " + 
"0.011529301268011938" + 
":  " + 
"-0.00023955685565631832" + 
":  " + 
"(b('lon') <= 9.170949935913086) ? " + 
"(b('lat') <= 55.906049728393555) ? " + 
"-0.0047985324484566445" + 
":  " + 
"0.006961538269496669" + 
":  " + 
"(b('ndvi_med') <= 3523.5) ? " + 
"0.036236096143053675" + 
":  " + 
"0.016484452487426082" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.1269880346953869) ? " + 
"(b('gvvk2') <= 0.5491317212581635) ? " + 
"(b('svvk3') <= -0.027715977281332016) ? " + 
"-0.007258262497905245" + 
":  " + 
"0.00022306446218510717" + 
":  " + 
"(b('lon') <= -103.03784942626953) ? " + 
"0.038295550137504644" + 
":  " + 
"0.005979427932730426" + 
":  " + 
"(b('sand') <= 35.5) ? " + 
"(b('lat') <= 36.07700538635254) ? " + 
"-0.026641630816462758" + 
":  " + 
"-0.019219695324173988" + 
":  " + 
"(b('clay') <= 25.5) ? " + 
"-0.006810692078162192" + 
":  " + 
"0.005741403633252068" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 0.03652967885136604) ? " + 
"(b('sand') <= 46.5) ? " + 
"(b('lon') <= -104.89989471435547) ? " + 
"-0.0011728586327278668" + 
":  " + 
"0.012273596651879324" + 
":  " + 
"(b('sand') <= 52.5) ? " + 
"-0.01260599355877991" + 
":  " + 
"0.0010395373894277788" + 
":  " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"(b('lat') <= 40.44004440307617) ? " + 
"0.004720091140753745" + 
":  " + 
"-0.017367357040511407" + 
":  " + 
"(b('trees') <= 5.9133620262146) ? " + 
"0.012952236737480092" + 
":  " + 
"-0.000615173602919709" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 923.5) ? " + 
"(b('L8b3med') <= 899.25) ? " + 
"(b('L8b6med') <= 2871.5) ? " + 
"-0.0025084764149688236" + 
":  " + 
"0.006905620881858492" + 
":  " + 
"(b('L8b3med') <= 909.0) ? " + 
"-0.025369228904998438" + 
":  " + 
"-0.007689488322704374" + 
":  " + 
"(b('clay') <= 22.5) ? " + 
"(b('gvvk2') <= 0.29324179887771606) ? " + 
"-0.0006918115823404776" + 
":  " + 
"0.008046056579658166" + 
":  " + 
"(b('clay') <= 25.5) ? " + 
"-0.012024169853127407" + 
":  " + 
"0.0026627563570272394" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('lat') <= 50.68670654296875) ? " + 
"-0.019200288652941322" + 
":  " + 
"-0.017384866682209177" + 
":  " + 
"(b('sand') <= 74.5) ? " + 
"(b('sand') <= 73.0) ? " + 
"-7.161625297038135e-05" + 
":  " + 
"-0.03720816997234121" + 
":  " + 
"(b('L8b3med') <= 606.5) ? " + 
"0.02401430543928626" + 
":  " + 
"0.003476996511043157" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -71.2344970703125) ? " + 
"(b('lon') <= -77.86024856567383) ? " + 
"(b('L8b3med') <= 812.5) ? " + 
"-0.0047837301489767545" + 
":  " + 
"0.001908217220111417" + 
":  " + 
"(b('L8b1med') <= 239.0) ? " + 
"-0.01728025978764719" + 
":  " + 
"0.03335962269341315" + 
":  " + 
"(b('clay') <= 21.5) ? " + 
"(b('sand') <= 37.5) ? " + 
"0.024583917352060634" + 
":  " + 
"-0.00021215152530162872" + 
":  " + 
"(b('lat') <= 47.53986930847168) ? " + 
"-0.004344295422140737" + 
":  " + 
"-0.03434085356323353" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3349.5) ? " + 
"(b('L8b6med') <= 3148.25) ? " + 
"(b('lon') <= -97.97296905517578) ? " + 
"-0.003708182769236311" + 
":  " + 
"0.0018413530705060433" + 
":  " + 
"(b('ndvi_med') <= 1647.5) ? " + 
"-0.0033434838511902515" + 
":  " + 
"0.01996230672848235" + 
":  " + 
"(b('ndvi_med') <= 1612.5) ? " + 
"(b('svvk3') <= -0.015828943345695734) ? " + 
"0.02995326341721933" + 
":  " + 
"-0.0005994174294977154" + 
":  " + 
"(b('lat') <= 41.57524490356445) ? " + 
"-0.012854679628357842" + 
":  " + 
"0.0034012159564676477" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -71.2344970703125) ? " + 
"(b('lon') <= -77.86024856567383) ? " + 
"(b('L8b3med') <= 812.5) ? " + 
"-0.00426805196122775" + 
":  " + 
"0.001877024710269688" + 
":  " + 
"(b('L8b2med') <= 336.0) ? " + 
"-0.01573636911593307" + 
":  " + 
"0.02983952511702125" + 
":  " + 
"(b('svvk3') <= 0.012301221489906311) ? " + 
"(b('L8b7med') <= 2017.0) ? " + 
"-0.0009621372850249492" + 
":  " + 
"-0.012785792832964495" + 
":  " + 
"(b('clay') <= 20.5) ? " + 
"0.008395617817355353" + 
":  " + 
"-0.005140929471168196" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.08964456990361214) ? " + 
"(b('svvk3') <= 0.03547702915966511) ? " + 
"(b('svvk3') <= 0.03259287588298321) ? " + 
"-3.0966262429863974e-05" + 
":  " + 
"-0.016164356049739134" + 
":  " + 
"(b('clay') <= 21.5) ? " + 
"0.010466103271715934" + 
":  " + 
"-0.0004894920335530474" + 
":  " + 
"(b('L8b2med') <= 491.0) ? " + 
"(b('bulk') <= 153.5) ? " + 
"-0.020446231886698224" + 
":  " + 
"-0.005686513423554862" + 
":  " + 
"(b('L8b2med') <= 889.5) ? " + 
"0.0018270974576265417" + 
":  " + 
"-0.01617358471650087" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.13317912071943283) ? " + 
"(b('bulk') <= 147.0) ? " + 
"(b('lat') <= 39.1337947845459) ? " + 
"-0.028621305733296715" + 
":  " + 
"-0.0020255906504865737" + 
":  " + 
"(b('svvk3') <= 0.00014387653209269047) ? " + 
"0.04333203124590776" + 
":  " + 
"-0.0022208025216002777" + 
":  " + 
"(b('sand') <= 14.5) ? " + 
"(b('sand') <= 13.0) ? " + 
"0.01195323123194511" + 
":  " + 
"0.04137422713889827" + 
":  " + 
"(b('sand') <= 15.5) ? " + 
"-0.02737494003492358" + 
":  " + 
"0.00020664667487393468" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.1269880346953869) ? " + 
"(b('gvvk2') <= 0.5534997582435608) ? " + 
"(b('svvk3') <= -0.027715977281332016) ? " + 
"-0.006558559606451738" + 
":  " + 
"0.0002638941430979094" + 
":  " + 
"(b('lon') <= -103.03784942626953) ? " + 
"0.03314813519068294" + 
":  " + 
"0.004432937934610505" + 
":  " + 
"(b('sand') <= 35.5) ? " + 
"(b('L8b2med') <= 734.5) ? " + 
"-0.023666444778058682" + 
":  " + 
"-0.016161442584815125" + 
":  " + 
"(b('L8b7med') <= 2263.5) ? " + 
"-0.006690179835357847" + 
":  " + 
"0.005609285339608999" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.0020157683175057173) ? " + 
"(b('lon') <= -115.53428649902344) ? " + 
"(b('clay') <= 28.0) ? " + 
"-0.005587776664424891" + 
":  " + 
"-0.03342642608557855" + 
":  " + 
"(b('svvk3') <= -0.005416378378868103) ? " + 
"0.0016065213066125256" + 
":  " + 
"0.016024300497083793" + 
":  " + 
"(b('lat') <= 38.87914848327637) ? " + 
"(b('sand') <= 20.5) ? " + 
"0.029315637834378627" + 
":  " + 
"0.0015097163228828525" + 
":  " + 
"(b('L8b7med') <= 2918.0) ? " + 
"-0.001470417878389588" + 
":  " + 
"-0.017756426663991423" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.406574964523315) ? " + 
"(b('sand') <= 47.5) ? " + 
"(b('lon') <= -104.89989471435547) ? " + 
"-0.0008717035029800162" + 
":  " + 
"0.0074565013602015786" + 
":  " + 
"(b('L8b2med') <= 552.5) ? " + 
"-0.01627370647519368" + 
":  " + 
"-0.0006845079264152455" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"(b('ndvi_med') <= 1463.75) ? " + 
"-0.020027130083389588" + 
":  " + 
"-0.02669187457194221" + 
":  " + 
"(b('lat') <= 43.73078536987305) ? " + 
"0.008276125196567752" + 
":  " + 
"-0.0027529722591658114" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.1269880346953869) ? " + 
"(b('gvvk2') <= 0.5491317212581635) ? " + 
"(b('svvk3') <= -0.04907691664993763) ? " + 
"-0.00794502719291346" + 
":  " + 
"0.00016258223168681278" + 
":  " + 
"(b('lon') <= -103.03784942626953) ? " + 
"0.029651123566592524" + 
":  " + 
"0.004027502973053643" + 
":  " + 
"(b('sand') <= 35.5) ? " + 
"(b('L8b3med') <= 1125.5) ? " + 
"-0.022196422068561233" + 
":  " + 
"-0.014609099608323906" + 
":  " + 
"(b('ndvi_med') <= 1708.75) ? " + 
"0.004069772653703063" + 
":  " + 
"-0.006119499814712169" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"(b('ndvi_med') <= 1600.0) ? " + 
"0.006343368960553353" + 
":  " + 
"-0.00042400167879648546" + 
":  " + 
"(b('trees') <= 2.910244882106781) ? " + 
"-0.02056261541230992" + 
":  " + 
"0.017594287446669566" + 
":  " + 
"(b('L8b3med') <= 1147.75) ? " + 
"(b('svvk3') <= -0.0015101225581020117) ? " + 
"0.06390795311756581" + 
":  " + 
"0.019230734934797857" + 
":  " + 
"(b('svvk3') <= 0.018095525912940502) ? " + 
"0.004431423104088934" + 
":  " + 
"-0.005602588984015342" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.13317912071943283) ? " + 
"(b('bulk') <= 147.0) ? " + 
"(b('lat') <= 39.1337947845459) ? " + 
"-0.025996402095245476" + 
":  " + 
"-0.0015739939621538996" + 
":  " + 
"(b('svvk3') <= 0.00014387653209269047) ? " + 
"0.038682648351755375" + 
":  " + 
"-0.0025623531675602676" + 
":  " + 
"(b('sand') <= 14.5) ? " + 
"(b('clay') <= 22.0) ? " + 
"0.03663794860722841" + 
":  " + 
"0.0098392392657847" + 
":  " + 
"(b('sand') <= 15.5) ? " + 
"-0.025390148808461327" + 
":  " + 
"0.00020566803136200172" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 2296.25) ? " + 
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"0.0003832447303043616" + 
":  " + 
"-0.0136125585828534" + 
":  " + 
"(b('L8b3med') <= 1147.75) ? " + 
"0.023031308404537758" + 
":  " + 
"0.000709583076615246" + 
":  " + 
"(b('svvk3') <= 0.0020430886652320623) ? " + 
"(b('lon') <= -115.47503662109375) ? " + 
"-0.007091872008674123" + 
":  " + 
"-0.012983897118347187" + 
":  " + 
"-0.01781420340498857" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 923.5) ? " + 
"(b('lon') <= 22.88466453552246) ? " + 
"(b('lon') <= 22.87806510925293) ? " + 
"-0.001140989664249211" + 
":  " + 
"0.01420214570635996" + 
":  " + 
"(b('lon') <= 23.000134468078613) ? " + 
"-0.02873828378330867" + 
":  " + 
"-0.007376918753402504" + 
":  " + 
"(b('L8b7med') <= 2145.75) ? " + 
"(b('svvk3') <= -0.03350725118070841) ? " + 
"-0.022578471066452624" + 
":  " + 
"0.006624667871996615" + 
":  " + 
"(b('trees') <= 17.931958198547363) ? " + 
"-0.001546916756800526" + 
":  " + 
"0.022828639090539615" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= 1.4101499915122986) ? " + 
"0.0005299150890258273" + 
":  " + 
"0.04814387533727468" + 
":  " + 
"(b('L8b6med') <= 2813.5) ? " + 
"-0.007914714552394272" + 
":  " + 
"0.003823336474322006" + 
":  " + 
"(b('L8b3med') <= 623.0) ? " + 
"(b('ndvi_med') <= 3523.5) ? " + 
"0.030586445389042538" + 
":  " + 
"0.013117660017477939" + 
":  " + 
"(b('ndvi_med') <= 3846.5) ? " + 
"-0.0023129976718741776" + 
":  " + 
"0.00728214404091697" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 103.5) ? " + 
"(b('sand') <= 48.0) ? " + 
"(b('ndvi_med') <= 3380.5) ? " + 
"-0.01477693988200851" + 
":  " + 
"-0.010407592213097491" + 
":  " + 
"(b('L8b1med') <= 428.5) ? " + 
"-0.008293085542279588" + 
":  " + 
"-0.005346729501064421" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"0.03251724110444487" + 
":  " + 
"(b('bulk') <= 106.5) ? " + 
"-0.013987398217092625" + 
":  " + 
"0.0001445243667438652" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 19.598620414733887) ? " + 
"(b('trees') <= 17.942265510559082) ? " + 
"(b('gvvk2') <= 0.041203947737812996) ? " + 
"0.029643335867862566" + 
":  " + 
"-0.0004773712337982286" + 
":  " + 
"(b('sand') <= 39.5) ? " + 
"0.034323875786313365" + 
":  " + 
"0.008204155076324332" + 
":  " + 
"(b('L8b2med') <= 477.75) ? " + 
"(b('L8b3med') <= 759.0) ? " + 
"-0.0070807528922899295" + 
":  " + 
"-0.03845408783958939" + 
":  " + 
"(b('trees') <= 19.723182678222656) ? " + 
"-0.04511750095256639" + 
":  " + 
"0.007020231866349662" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 822.25) ? " + 
"(b('L8b1med') <= 805.0) ? " + 
"(b('L8b6med') <= 3580.25) ? " + 
"0.0006944271896776622" + 
":  " + 
"-0.0035807069798422944" + 
":  " + 
"(b('svvk3') <= -0.00906233057321515) ? " + 
"0.05763569730882953" + 
":  " + 
"0.010802170847025658" + 
":  " + 
"(b('L8b2med') <= 1073.5) ? " + 
"(b('L8b1med') <= 826.0) ? " + 
"-0.04123136262170635" + 
":  " + 
"-0.02744587916258366" + 
":  " + 
"(b('sand') <= 65.5) ? " + 
"0.0028900334907305068" + 
":  " + 
"-0.016222319231033587" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12624889612197876) ? " + 
"(b('trees') <= 18.111291885375977) ? " + 
"(b('L8b7med') <= 1750.0) ? " + 
"0.026609559562108545" + 
":  " + 
"-0.004673969856705064" + 
":  " + 
"(b('L8b3med') <= 859.0) ? " + 
"-0.03633022803568955" + 
":  " + 
"-0.007259953636901961" + 
":  " + 
"(b('sand') <= 14.5) ? " + 
"(b('clay') <= 22.0) ? " + 
"0.032211018388720425" + 
":  " + 
"0.00884194029143584" + 
":  " + 
"(b('sand') <= 15.5) ? " + 
"-0.020635504062171406" + 
":  " + 
"0.00014535498759648508" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 56.04010009765625) ? " + 
"(b('L8b3med') <= 812.5) ? " + 
"(b('L8b7med') <= 1800.75) ? " + 
"-0.0003033607358064536" + 
":  " + 
"-0.014736700072125738" + 
":  " + 
"(b('lat') <= 53.63345909118652) ? " + 
"0.0012860691521157717" + 
":  " + 
"-0.00975437237509085" + 
":  " + 
"(b('L8b6med') <= 2358.5) ? " + 
"(b('L8b6med') <= 2322.0) ? " + 
"0.0048765050364565354" + 
":  " + 
"-0.005695025085795613" + 
":  " + 
"(b('bulk') <= 133.0) ? " + 
"0.019687444684598265" + 
":  " + 
"0.013865202967496285" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.25013542175293) ? " + 
"(b('lat') <= 46.2239990234375) ? " + 
"(b('lat') <= 46.01203918457031) ? " + 
"-0.00017397696121126076" + 
":  " + 
"0.034344092848460545" + 
":  " + 
"(b('L8b3med') <= 800.5) ? " + 
"-0.01939886038249495" + 
":  " + 
"-0.0019026398890700125" + 
":  " + 
"(b('L8b6med') <= 2849.0) ? " + 
"(b('bulk') <= 106.5) ? " + 
"-0.04407399680172816" + 
":  " + 
"-0.0004484679777589432" + 
":  " + 
"(b('trees') <= 8.700934648513794) ? " + 
"0.0032575902493121116" + 
":  " + 
"0.038160406960706945" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= -0.6403000056743622) ? " + 
"7.46511933543378e-05" + 
":  " + 
"0.013960394763380889" + 
":  " + 
"(b('lon') <= 6.412564992904663) ? " + 
"-0.02076394751967313" + 
":  " + 
"-0.0011492852766382376" + 
":  " + 
"(b('L8b3med') <= 623.0) ? " + 
"(b('svvk3') <= -0.0008742376230657101) ? " + 
"0.027552290190472895" + 
":  " + 
"0.011830383356064733" + 
":  " + 
"(b('clay') <= 4.0) ? " + 
"-0.01331955411308354" + 
":  " + 
"0.004153371145864855" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('svvk3') <= -0.0020157683175057173) ? " + 
"(b('sand') <= 49.0) ? " + 
"0.004847835435649321" + 
":  " + 
"-0.0035024970931828935" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"-0.003190114485347213" + 
":  " + 
"0.0006693164290743042" + 
":  " + 
"-0.020603603257583883" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.25013542175293) ? " + 
"(b('lat') <= 46.2239990234375) ? " + 
"(b('lat') <= 46.01203918457031) ? " + 
"-0.00025594833166323234" + 
":  " + 
"0.031236849023205546" + 
":  " + 
"(b('L8b3med') <= 800.5) ? " + 
"-0.01739636738542055" + 
":  " + 
"-0.0016425296177609544" + 
":  " + 
"(b('L8b6med') <= 2849.0) ? " + 
"(b('bulk') <= 106.5) ? " + 
"-0.03727119092105333" + 
":  " + 
"-0.00018860968074090265" + 
":  " + 
"(b('trees') <= 8.700934648513794) ? " + 
"0.0031568658272132693" + 
":  " + 
"0.034760075163591656" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3323.0) ? " + 
"(b('L8b6med') <= 3148.25) ? " + 
"(b('lon') <= -97.97296905517578) ? " + 
"-0.003241385379526548" + 
":  " + 
"0.001638976449834349" + 
":  " + 
"(b('L8b6med') <= 3311.75) ? " + 
"0.01091039796678282" + 
":  " + 
"0.055240217568438305" + 
":  " + 
"(b('lon') <= -121.29663467407227) ? " + 
"(b('L8b3med') <= 1190.0) ? " + 
"0.005181594532121997" + 
":  " + 
"0.018260656071572946" + 
":  " + 
"(b('gvvk2') <= 0.5881716310977936) ? " + 
"-0.0026532825046692195" + 
":  " + 
"0.030996896837846316" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2468.0) ? " + 
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 639.75) ? " + 
"0.0001320312618190545" + 
":  " + 
"-0.03532904067003316" + 
":  " + 
"(b('L8b2med') <= 887.0) ? " + 
"0.024807188459628003" + 
":  " + 
"-0.0001121401723008071" + 
":  " + 
"(b('ndvi_med') <= 1700.0) ? " + 
"(b('svvk3') <= 0.018095525912940502) ? " + 
"0.004508821218883714" + 
":  " + 
"-0.006885888104815863" + 
":  " + 
"(b('trees') <= 14.376446723937988) ? " + 
"-0.01254650864463925" + 
":  " + 
"0.03216320550472959" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.01818084716797) ? " + 
"(b('L8b6med') <= 2686.25) ? " + 
"0.014238585188941194" + 
":  " + 
"0.020755701085845298" + 
":  " + 
"(b('bulk') <= 147.5) ? " + 
"0.0038768694250254595" + 
":  " + 
"-0.003720470566110759" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"(b('lat') <= 32.39724922180176) ? " + 
"-0.009450760158744572" + 
":  " + 
"0.00036431126823320776" + 
":  " + 
"(b('L8b7med') <= 1635.0) ? " + 
"-0.02763128214048275" + 
":  " + 
"-0.005643737574801213" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('sand') <= 53.5) ? " + 
"(b('L8b3med') <= 1416.5) ? " + 
"0.0011832257040399548" + 
":  " + 
"-0.006505170559040143" + 
":  " + 
"(b('L8b6med') <= 2820.5) ? " + 
"-0.008176210459590327" + 
":  " + 
"0.0005750468756308077" + 
":  " + 
"(b('lon') <= 9.170949935913086) ? " + 
"(b('ndvi_med') <= 3846.5) ? " + 
"-0.0013584407607221782" + 
":  " + 
"0.006507216975124757" + 
":  " + 
"(b('L8b3med') <= 581.0) ? " + 
"0.010771685539078424" + 
":  " + 
"0.024952639950829303" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.03547702915966511) ? " + 
"(b('svvk3') <= 0.03259287588298321) ? " + 
"(b('lat') <= 56.000450134277344) ? " + 
"-0.00040723812337379147" + 
":  " + 
"0.009594458629533727" + 
":  " + 
"(b('gvvk2') <= 0.5135599821805954) ? " + 
"-0.014727588377424522" + 
":  " + 
"0.0031435310642569936" + 
":  " + 
"(b('svvk3') <= 0.04135633632540703) ? " + 
"(b('L8b7med') <= 2141.25) ? " + 
"0.006686428771627286" + 
":  " + 
"0.019953368748101535" + 
":  " + 
"(b('trees') <= 12.70752239227295) ? " + 
"0.001673586731769553" + 
":  " + 
"-0.00893494977855255" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 25.446617126464844) ? " + 
"(b('gvvk2') <= 0.13317912071943283) ? " + 
"-0.004070156228411375" + 
":  " + 
"0.0002735801891270481" + 
":  " + 
"(b('clay') <= 18.0) ? " + 
"-0.012730327736371491" + 
":  " + 
"-0.025816503657425452" + 
":  " + 
"(b('lat') <= 39.5146484375) ? " + 
"(b('bulk') <= 116.0) ? " + 
"0.0069904687828337975" + 
":  " + 
"-0.0029867594927540098" + 
":  " + 
"0.03094135367288431" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.01818084716797) ? " + 
"(b('L8b3med') <= 891.5) ? " + 
"0.013645713509430779" + 
":  " + 
"0.01850154189894474" + 
":  " + 
"(b('bulk') <= 147.5) ? " + 
"0.0032860493037613118" + 
":  " + 
"-0.0034966036463952507" + 
":  " + 
"(b('lon') <= 24.045809745788574) ? " + 
"(b('lat') <= 32.39724922180176) ? " + 
"-0.008246377281808843" + 
":  " + 
"0.0003491238569413925" + 
":  " + 
"(b('lat') <= 44.097700119018555) ? " + 
"-0.015503398449043509" + 
":  " + 
"-0.004788881375236055" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2145.75) ? " + 
"(b('bulk') <= 163.5) ? " + 
"(b('lon') <= -120.78776931762695) ? " + 
"0.021267403340541356" + 
":  " + 
"0.0006270551888150996" + 
":  " + 
"(b('lon') <= -121.4896011352539) ? " + 
"-0.0066435831781145455" + 
":  " + 
"-0.02473636955664718" + 
":  " + 
"(b('L8b2med') <= 753.25) ? " + 
"(b('bulk') <= 150.5) ? " + 
"-0.010871785753386232" + 
":  " + 
"0.001978802531296255" + 
":  " + 
"(b('L8b2med') <= 783.75) ? " + 
"0.01174447294581753" + 
":  " + 
"-0.0013852211418619777" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"(b('L8b2med') <= 782.5) ? " + 
"3.46842463885295e-05" + 
":  " + 
"0.014265580776430071" + 
":  " + 
"(b('lon') <= 0.6124000549316406) ? " + 
"-0.016633651660882053" + 
":  " + 
"0.014363333933875904" + 
":  " + 
"(b('L8b7med') <= 2253.75) ? " + 
"(b('L8b7med') <= 2189.5) ? " + 
"0.014796901233479324" + 
":  " + 
"0.051159275857061565" + 
":  " + 
"(b('ndvi_med') <= 1369.0) ? " + 
"-0.0032964529649426324" + 
":  " + 
"0.005253982493862419" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 39.89585876464844) ? " + 
"(b('svvk3') <= -0.051632415503263474) ? " + 
"(b('svvk3') <= -0.06070861406624317) ? " + 
"-0.027910199435759057" + 
":  " + 
"-0.024426097277877507" + 
":  " + 
"(b('sand') <= 65.5) ? " + 
"0.0022729117152523824" + 
":  " + 
"-0.00780803451869167" + 
":  " + 
"(b('L8b7med') <= 2895.25) ? " + 
"(b('clay') <= 32.5) ? " + 
"-0.0007973365730352619" + 
":  " + 
"0.009418163800327993" + 
":  " + 
"(b('ndvi_med') <= 1581.0) ? " + 
"-0.018758335570363476" + 
":  " + 
"-0.006178264648960247" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 19.598620414733887) ? " + 
"(b('trees') <= 17.942265510559082) ? " + 
"(b('gvvk2') <= 0.041203947737812996) ? " + 
"0.023214056062190153" + 
":  " + 
"-0.00038029608926450526" + 
":  " + 
"(b('clay') <= 21.5) ? " + 
"0.005887499102754928" + 
":  " + 
"0.029858788246643276" + 
":  " + 
"(b('L8b2med') <= 477.75) ? " + 
"(b('L8b3med') <= 759.0) ? " + 
"-0.005611180729739691" + 
":  " + 
"-0.03269657885202203" + 
":  " + 
"(b('trees') <= 19.723182678222656) ? " + 
"-0.03692663827189334" + 
":  " + 
"0.00563060086336541" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 613.5) ? " + 
"(b('trees') <= 0.03652967885136604) ? " + 
"0.0026791798895297917" + 
":  " + 
"-0.0010751642207374032" + 
":  " + 
"(b('lon') <= 0.6124000549316406) ? " + 
"-0.014253978264658929" + 
":  " + 
"0.012942422197108705" + 
":  " + 
"(b('L8b7med') <= 2253.75) ? " + 
"(b('L8b6med') <= 2872.0) ? " + 
"0.013434974376361366" + 
":  " + 
"0.0461611115375854" + 
":  " + 
"(b('ndvi_med') <= 1369.0) ? " + 
"-0.0029488158521312926" + 
":  " + 
"0.004885807376899402" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 25.446617126464844) ? " + 
"(b('L8b6med') <= 2527.0) ? " + 
"-0.001810477817690992" + 
":  " + 
"0.0005511079995285479" + 
":  " + 
"(b('bulk') <= 123.5) ? " + 
"-0.010810013139597605" + 
":  " + 
"-0.023711749627856674" + 
":  " + 
"(b('svvk3') <= -3.257839853176847e-05) ? " + 
"(b('L8b2med') <= 418.75) ? " + 
"-0.002347826549170595" + 
":  " + 
"0.006631678898858379" + 
":  " + 
"0.028187475299903897" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('lat') <= 56.04010009765625) ? " + 
"(b('lat') <= 55.933950424194336) ? " + 
"5.447495990717222e-05" + 
":  " + 
"-0.00907879617104858" + 
":  " + 
"(b('L8b2med') <= 425.5) ? " + 
"0.00244576217746309" + 
":  " + 
"0.014656796588585921" + 
":  " + 
"(b('gvvk2') <= 0.39189615845680237) ? " + 
"(b('svvk3') <= -0.0038270524237304926) ? " + 
"0.02177581321473865" + 
":  " + 
"0.008908465273601526" + 
":  " + 
"(b('bulk') <= 130.0) ? " + 
"0.005339715547456335" + 
":  " + 
"-0.003650224410826926" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 348.5) ? " + 
"(b('L8b1med') <= 332.0) ? " + 
"(b('L8b2med') <= 425.5) ? " + 
"-0.002201134728564923" + 
":  " + 
"0.01349192669213922" + 
":  " + 
"(b('L8b3med') <= 772.25) ? " + 
"0.025375365509107385" + 
":  " + 
"0.003624125214383743" + 
":  " + 
"(b('L8b7med') <= 1428.5) ? " + 
"(b('clay') <= 27.0) ? " + 
"-0.012369084942944787" + 
":  " + 
"0.009029964478307145" + 
":  " + 
"(b('trees') <= 17.868996620178223) ? " + 
"-0.0007361220844274393" + 
":  " + 
"0.004857784489476307" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.25013542175293) ? " + 
"(b('bulk') <= 131.5) ? " + 
"(b('svvk3') <= 0.0009490402007941157) ? " + 
"0.0010714262108866774" + 
":  " + 
"-0.011947660470193522" + 
":  " + 
"(b('ndvi_med') <= 3691.75) ? " + 
"-0.0006653302594136772" + 
":  " + 
"0.009317305127951075" + 
":  " + 
"(b('L8b6med') <= 2849.0) ? " + 
"(b('bulk') <= 106.5) ? " + 
"-0.033578811967913874" + 
":  " + 
"-0.0001544368254949651" + 
":  " + 
"(b('trees') <= 8.700934648513794) ? " + 
"0.0024162568488700496" + 
":  " + 
"0.02970872448481717" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1583.0) ? " + 
"(b('ndvi_med') <= 1577.0) ? " + 
"(b('svvk3') <= -0.015828943345695734) ? " + 
"0.016999282815681267" + 
":  " + 
"0.00020761916962545407" + 
":  " + 
"0.048702973166779726" + 
":  " + 
"(b('ndvi_med') <= 1775.0) ? " + 
"(b('lat') <= 36.09249496459961) ? " + 
"0.006253935965839133" + 
":  " + 
"-0.010709908080182594" + 
":  " + 
"(b('L8b1med') <= 641.0) ? " + 
"-0.0002422279630055136" + 
":  " + 
"0.01132424472965878" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 0.03652967885136604) ? " + 
"(b('L8b6med') <= 2797.0) ? " + 
"(b('L8b7med') <= 1740.75) ? " + 
"0.00019757524381827752" + 
":  " + 
"0.010632279071782075" + 
":  " + 
"(b('bulk') <= 145.5) ? " + 
"-0.0050630835766141465" + 
":  " + 
"0.00223256486895026" + 
":  " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"(b('trees') <= 3.5388137102127075) ? " + 
"-0.004335493172448201" + 
":  " + 
"-0.03775441328658446" + 
":  " + 
"(b('trees') <= 5.9133620262146) ? " + 
"0.008871123141204529" + 
":  " + 
"-0.00033533527521589437" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"(b('gvvk2') <= 0.1353890746831894) ? " + 
"-0.008897255757671418" + 
":  " + 
"-0.016716339384562226" + 
":  " + 
"(b('ndvi_med') <= 734.25) ? " + 
"(b('sand') <= 56.5) ? " + 
"0.00026419462258071846" + 
":  " + 
"0.021627452957257765" + 
":  " + 
"(b('L8b1med') <= 822.25) ? " + 
"0.00018955386785049976" + 
":  " + 
"-0.005138163032715728" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('sand') <= 52.0) ? " + 
"-0.013246260760313378" + 
":  " + 
"-0.011410716611443439" + 
":  " + 
"(b('L8b3med') <= 562.5) ? " + 
"(b('L8b6med') <= 2584.5) ? " + 
"0.008396465809245857" + 
":  " + 
"0.015214605278553034" + 
":  " + 
"(b('L8b3med') <= 616.25) ? " + 
"-0.004942944558556041" + 
":  " + 
"0.0001777642709944963" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.09767632186412811) ? " + 
"(b('svvk3') <= 0.03547702915966511) ? " + 
"(b('svvk3') <= 0.018222343176603317) ? " + 
"0.0004275362672688332" + 
":  " + 
"-0.004918281973002593" + 
":  " + 
"(b('svvk3') <= 0.04165135137736797) ? " + 
"0.009528324388341357" + 
":  " + 
"0.0006524247253451871" + 
":  " + 
"(b('sand') <= 46.0) ? " + 
"(b('lat') <= 35.936100006103516) ? " + 
"-0.00044770620384688986" + 
":  " + 
"-0.0153400980344889" + 
":  " + 
"(b('L8b3med') <= 760.5) ? " + 
"-0.0032722734305326295" + 
":  " + 
"0.005577992670143195" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('trees') <= 18.111291885375977) ? " + 
"(b('L8b3med') <= 847.5) ? " + 
"0.02094815406778394" + 
":  " + 
"-0.003107050856290047" + 
":  " + 
"(b('L8b1med') <= 502.25) ? " + 
"-0.02965907488584689" + 
":  " + 
"-0.00760108262021283" + 
":  " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('clay') <= 14.5) ? " + 
"0.0024636420813445243" + 
":  " + 
"-0.0011199237853900237" + 
":  " + 
"(b('trees') <= 19.810494422912598) ? " + 
"0.013270718874421307" + 
":  " + 
"-0.0021285218615532254" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"(b('L8b2med') <= 782.5) ? " + 
"-5.93334002635994e-05" + 
":  " + 
"0.011742938136296156" + 
":  " + 
"(b('trees') <= 2.910244882106781) ? " + 
"-0.012696401529906929" + 
":  " + 
"0.010659944977660393" + 
":  " + 
"(b('L8b7med') <= 2253.75) ? " + 
"(b('L8b6med') <= 2872.0) ? " + 
"0.011525157095844604" + 
":  " + 
"0.04103097814489057" + 
":  " + 
"(b('svvk3') <= 0.018095525912940502) ? " + 
"0.0038792115487349416" + 
":  " + 
"-0.0037859294547261963" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.04986215569078922) ? " + 
"(b('lon') <= -100.68251419067383) ? " + 
"(b('L8b6med') <= 2789.75) ? " + 
"-0.022503579965785087" + 
":  " + 
"-0.02438330633469194" + 
":  " + 
"(b('lat') <= 38.55278015136719) ? " + 
"-0.022260405727886123" + 
":  " + 
"-0.00043139503350944283" + 
":  " + 
"(b('svvk3') <= -0.017486218363046646) ? " + 
"(b('clay') <= 18.5) ? " + 
"-0.006779611485827581" + 
":  " + 
"0.01430069148498886" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.013379361647817152" + 
":  " + 
"0.00010096715374121087" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 923.5) ? " + 
"(b('L8b3med') <= 899.25) ? " + 
"(b('L8b6med') <= 2871.5) ? " + 
"-0.0016427885040067158" + 
":  " + 
"0.005090350351246096" + 
":  " + 
"(b('L8b3med') <= 909.0) ? " + 
"-0.019965301368834745" + 
":  " + 
"-0.005690297893346774" + 
":  " + 
"(b('L8b3med') <= 932.5) ? " + 
"(b('lon') <= -103.69044876098633) ? " + 
"0.0010433115789327096" + 
":  " + 
"0.05055575827772192" + 
":  " + 
"(b('clay') <= 22.5) ? " + 
"0.002130322789316172" + 
":  " + 
"-0.0030090692168095842" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 56.04010009765625) ? " + 
"(b('L8b3med') <= 812.5) ? " + 
"(b('L8b7med') <= 1800.75) ? " + 
"-0.0001211281164322114" + 
":  " + 
"-0.012448375630032371" + 
":  " + 
"(b('lat') <= 55.92889976501465) ? " + 
"0.0008778455458281257" + 
":  " + 
"-0.012854786922959676" + 
":  " + 
"(b('L8b2med') <= 425.5) ? " + 
"(b('gvvk2') <= 0.49347880482673645) ? " + 
"0.003555636212360963" + 
":  " + 
"-0.005752729768011472" + 
":  " + 
"(b('L8b6med') <= 2446.5) ? " + 
"0.011562893934605592" + 
":  " + 
"0.017051257120646507" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('trees') <= 18.111291885375977) ? " + 
"(b('L8b3med') <= 847.5) ? " + 
"0.01897561826458863" + 
":  " + 
"-0.0030713180022548026" + 
":  " + 
"(b('L8b3med') <= 859.0) ? " + 
"-0.026907544736441708" + 
":  " + 
"-0.0072083884454386266" + 
":  " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('clay') <= 14.5) ? " + 
"0.002315877519211541" + 
":  " + 
"-0.0010143988917031398" + 
":  " + 
"(b('L8b6med') <= 3148.0) ? " + 
"0.0002615881118731993" + 
":  " + 
"0.020030333502945325" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 47.5) ? " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= -104.89989471435547) ? " + 
"-0.0009234694145024103" + 
":  " + 
"0.00506277418073261" + 
":  " + 
"(b('clay') <= 17.0) ? " + 
"0.007943581268269218" + 
":  " + 
"-0.010914578777760038" + 
":  " + 
"(b('lon') <= 9.089200019836426) ? " + 
"(b('ndvi_med') <= 1561.75) ? " + 
"0.002229366094040479" + 
":  " + 
"-0.007314212875431061" + 
":  " + 
"(b('svvk3') <= -0.0022346809273585677) ? " + 
"0.009897940973756588" + 
":  " + 
"0.0011837311656768112" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3323.0) ? " + 
"(b('L8b6med') <= 3120.5) ? " + 
"(b('L8b6med') <= 3101.75) ? " + 
"-0.00020011535529157188" + 
":  " + 
"-0.022176261233043115" + 
":  " + 
"(b('L8b6med') <= 3311.75) ? " + 
"0.007319500680378221" + 
":  " + 
"0.04618406652494475" + 
":  " + 
"(b('L8b7med') <= 2018.5) ? " + 
"(b('svvk3') <= -0.005644022952765226) ? " + 
"0.0426337099054635" + 
":  " + 
"-0.0019285968157028432" + 
":  " + 
"(b('L8b1med') <= 518.5) ? " + 
"-0.007416408204122889" + 
":  " + 
"-0.00017508724024370943" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 1067.75) ? " + 
"(b('L8b3med') <= 1796.0) ? " + 
"(b('L8b1med') <= 822.25) ? " + 
"0.00021618309611755814" + 
":  " + 
"-0.00884479012545314" + 
":  " + 
"(b('L8b1med') <= 1046.0) ? " + 
"0.014030332783942105" + 
":  " + 
"0.02339308135283444" + 
":  " + 
"(b('lon') <= -115.02366638183594) ? " + 
"(b('clay') <= 11.5) ? " + 
"-0.019562452159424676" + 
":  " + 
"-0.005375228611984191" + 
":  " + 
"(b('svvk3') <= 0.0073236883617937565) ? " + 
"0.0004607108770575713" + 
":  " + 
"0.02855338522956044" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 168.5) ? " + 
"(b('L8b6med') <= 3580.25) ? " + 
"0.0003790818249401199" + 
":  " + 
"-0.0020096867238190534" + 
":  " + 
"(b('svvk3') <= 0.0014518689131364226) ? " + 
"0.005400808459053025" + 
":  " + 
"0.022137325634440527" + 
":  " + 
"-0.01650604755568641" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('bulk') <= 103.5) ? " + 
"-0.012124520131253369" + 
":  " + 
"-0.010798499169337339" + 
":  " + 
"(b('L8b3med') <= 562.5) ? " + 
"(b('clay') <= 11.0) ? " + 
"0.007050453855090566" + 
":  " + 
"0.013186779377467012" + 
":  " + 
"(b('L8b3med') <= 616.25) ? " + 
"-0.004857335314878947" + 
":  " + 
"0.0001833936565992442" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 348.5) ? " + 
"(b('L8b1med') <= 338.0) ? " + 
"(b('trees') <= 11.076036930084229) ? " + 
"0.003215235797422569" + 
":  " + 
"-0.005049967331948973" + 
":  " + 
"(b('ndvi_med') <= 3117.0) ? " + 
"0.02464400642582447" + 
":  " + 
"0.008801141926294161" + 
":  " + 
"(b('L8b2med') <= 552.5) ? " + 
"(b('L8b2med') <= 543.5) ? " + 
"-0.0013277094819731162" + 
":  " + 
"-0.019723442890995892" + 
":  " + 
"(b('L8b2med') <= 580.5) ? " + 
"0.008915468066372459" + 
":  " + 
"-0.00010631843010784109" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"(b('gvvk2') <= 0.1353890746831894) ? " + 
"-0.007750541388990388" + 
":  " + 
"-0.014787716653192118" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.021247034367283757" + 
":  " + 
"(b('gvvk2') <= 0.12624889612197876) ? " + 
"-0.005412299317580188" + 
":  " + 
"0.00020774738901409921" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('lon') <= -71.2344970703125) ? " + 
"(b('lon') <= -77.86024856567383) ? " + 
"7.461750824280884e-05" + 
":  " + 
"0.016088758936084694" + 
":  " + 
"(b('svvk3') <= 0.012301221489906311) ? " + 
"-0.004135263748073466" + 
":  " + 
"0.0026891595901184684" + 
":  " + 
"(b('gvvk2') <= 0.39189615845680237) ? " + 
"(b('svvk3') <= -0.0038270524237304926) ? " + 
"0.01913253330036907" + 
":  " + 
"0.008215416021995797" + 
":  " + 
"(b('bulk') <= 130.0) ? " + 
"0.004345321742323438" + 
":  " + 
"-0.0035440075611233427" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('ndvi_med') <= 2574.5) ? " + 
"-0.012863242330380165" + 
":  " + 
"-0.010329863530059102" + 
":  " + 
"(b('L8b6med') <= 2201.75) ? " + 
"(b('lon') <= -120.5117073059082) ? " + 
"0.02260452893991765" + 
":  " + 
"0.001766115304988567" + 
":  " + 
"(b('L8b6med') <= 2260.25) ? " + 
"-0.01989336151938406" + 
":  " + 
"9.616241139108438e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.09767632186412811) ? " + 
"(b('svvk3') <= 0.03547702915966511) ? " + 
"(b('svvk3') <= 0.018222343176603317) ? " + 
"0.0003732314178447745" + 
":  " + 
"-0.004196524223848439" + 
":  " + 
"(b('clay') <= 21.5) ? " + 
"0.00586218011231402" + 
":  " + 
"-0.0011095257592291514" + 
":  " + 
"(b('sand') <= 46.0) ? " + 
"(b('lat') <= 35.936100006103516) ? " + 
"-2.591554716272389e-05" + 
":  " + 
"-0.013730588568178928" + 
":  " + 
"(b('L8b7med') <= 1758.5) ? " + 
"-0.004074814251958825" + 
":  " + 
"0.003955668878968706" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('bulk') <= 162.5) ? " + 
"(b('ndvi_med') <= 5217.0) ? " + 
"-0.0003361309925628188" + 
":  " + 
"-0.028983196809005934" + 
":  " + 
"(b('gvvk2') <= 0.32789695262908936) ? " + 
"-0.024659303524152493" + 
":  " + 
"-0.01946285026760392" + 
":  " + 
"(b('svvk3') <= -0.017486218363046646) ? " + 
"(b('lon') <= -97.02780151367188) ? " + 
"0.026192378044649786" + 
":  " + 
"-0.003378198520488036" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.0116256047868707" + 
":  " + 
"0.00011101612664374575" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -121.29663467407227) ? " + 
"(b('L8b7med') <= 2534.75) ? " + 
"(b('gvvk2') <= 0.31023740768432617) ? " + 
"0.002115033656072037" + 
":  " + 
"-0.013337229861097755" + 
":  " + 
"(b('L8b7med') <= 2990.0) ? " + 
"0.019610396668461913" + 
":  " + 
"0.008287864789545796" + 
":  " + 
"(b('lon') <= -120.94869613647461) ? " + 
"(b('ndvi_med') <= 1754.25) ? " + 
"-0.011568307932933378" + 
":  " + 
"-0.002609759898056223" + 
":  " + 
"(b('lon') <= -120.92649459838867) ? " + 
"0.020249691638838226" + 
":  " + 
"-4.499963170547708e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('bulk') <= 103.5) ? " + 
"-0.01162084288862042" + 
":  " + 
"-0.009889696837778433" + 
":  " + 
"(b('L8b3med') <= 555.5) ? " + 
"(b('gvvk2') <= 0.1796317920088768) ? " + 
"0.006783839098137734" + 
":  " + 
"0.016987737828795535" + 
":  " + 
"(b('L8b3med') <= 616.25) ? " + 
"-0.003813999639508874" + 
":  " + 
"0.00016893373107028562" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 540.5) ? " + 
"(b('L8b1med') <= 535.5) ? " + 
"(b('gvvk2') <= 0.3372344970703125) ? " + 
"0.0019662675648311413" + 
":  " + 
"-0.0019321265050699858" + 
":  " + 
"(b('bulk') <= 144.5) ? " + 
"0.022207896843650148" + 
":  " + 
"0.0321779816357769" + 
":  " + 
"(b('L8b1med') <= 545.25) ? " + 
"(b('clay') <= 16.0) ? " + 
"-0.04117916013336867" + 
":  " + 
"-0.018896558684129122" + 
":  " + 
"(b('clay') <= 22.5) ? " + 
"0.0014911414795401939" + 
":  " + 
"-0.005005745344719467" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('ndvi_med') <= 1531.0) ? " + 
"(b('bulk') <= 147.5) ? " + 
"0.002935602639608533" + 
":  " + 
"-0.002102938027903359" + 
":  " + 
"(b('clay') <= 25.0) ? " + 
"0.01633575945001725" + 
":  " + 
"0.011882708010966296" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"(b('sand') <= 47.5) ? " + 
"0.0009121446422698389" + 
":  " + 
"-0.0011584129620609176" + 
":  " + 
"(b('lon') <= 25.446414947509766) ? " + 
"-0.021528081760034186" + 
":  " + 
"-0.0035073339400932702" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 48.25013542175293) ? " + 
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"0.0002480320742921508" + 
":  " + 
"0.05822111039683728" + 
":  " + 
"(b('svvk3') <= 0.046119192615151405) ? " + 
"-0.00467563059972633" + 
":  " + 
"0.015029091402786137" + 
":  " + 
"(b('L8b6med') <= 2849.0) ? " + 
"(b('bulk') <= 106.5) ? " + 
"-0.02911044334803764" + 
":  " + 
"-0.00011076519835208427" + 
":  " + 
"(b('L8b7med') <= 2069.0) ? " + 
"0.01464371812908422" + 
":  " + 
"-0.0027212918336772087" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 6132.5) ? " + 
"(b('ndvi_med') <= 5941.25) ? " + 
"(b('ndvi_med') <= 5916.25) ? " + 
"3.7373404313104267e-05" + 
":  " + 
"-0.014211712177551405" + 
":  " + 
"(b('L8b7med') <= 2025.5) ? " + 
"0.037470104264348436" + 
":  " + 
"0.00852000068865344" + 
":  " + 
"(b('lat') <= 53.63241958618164) ? " + 
"(b('L8b6med') <= 3537.0) ? " + 
"-0.0030258111916913744" + 
":  " + 
"-0.008672938183245216" + 
":  " + 
"-0.015349821885188686" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('lon') <= -120.79476547241211) ? " + 
"(b('trees') <= 16.890581130981445) ? " + 
"0.029930003108941394" + 
":  " + 
"-0.0013342140161950733" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.01898262137459822" + 
":  " + 
"-0.00787282914842478" + 
":  " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('lat') <= 48.39845085144043) ? " + 
"-0.0009368312945464005" + 
":  " + 
"0.0018024707287393697" + 
":  " + 
"(b('trees') <= 19.810494422912598) ? " + 
"0.010842610931998991" + 
":  " + 
"-0.0018288842126726202" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('L8b1med') <= 533.5) ? " + 
"(b('L8b3med') <= 957.5) ? " + 
"-0.0021044503217757305" + 
":  " + 
"-0.022228910078963476" + 
":  " + 
"(b('clay') <= 20.5) ? " + 
"-0.0010669493547847092" + 
":  " + 
"0.01976852321566221" + 
":  " + 
"(b('svvk3') <= -0.017486218363046646) ? " + 
"(b('L8b2med') <= 517.25) ? " + 
"-0.0007922547166268704" + 
":  " + 
"0.0242842120615751" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.010062931905212612" + 
":  " + 
"0.00010768439517533353" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 2366.5) ? " + 
"(b('L8b7med') <= 3254.25) ? " + 
"(b('L8b7med') <= 3008.25) ? " + 
"4.881201695419417e-05" + 
":  " + 
"-0.00808130041586082" + 
":  " + 
"(b('L8b6med') <= 4001.0) ? " + 
"0.016139792655667035" + 
":  " + 
"0.0007381083668911491" + 
":  " + 
"(b('svvk3') <= 0.0006644814275205135) ? " + 
"(b('bulk') <= 153.5) ? " + 
"-0.008153571277409746" + 
":  " + 
"-0.00387425743410285" + 
":  " + 
"-0.01360941251537763" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -5.20074987411499) ? " + 
"(b('ndvi_med') <= 1531.0) ? " + 
"(b('L8b6med') <= 3714.0) ? " + 
"0.0029415664423315425" + 
":  " + 
"-0.0018776161022287102" + 
":  " + 
"(b('clay') <= 25.0) ? " + 
"0.014751676445396739" + 
":  " + 
"0.010709465332754006" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"(b('lat') <= 32.18929862976074) ? " + 
"-0.006691487021462894" + 
":  " + 
"0.00019051745138787615" + 
":  " + 
"(b('L8b7med') <= 1635.0) ? " + 
"-0.01883341437624777" + 
":  " + 
"-0.0033629608612585436" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('sand') <= 53.5) ? " + 
"(b('L8b3med') <= 1432.0) ? " + 
"0.0008190362188894415" + 
":  " + 
"-0.0046259341596562135" + 
":  " + 
"(b('gvvk2') <= 0.26820625364780426) ? " + 
"0.0019896146129744713" + 
":  " + 
"-0.004363073179585972" + 
":  " + 
"(b('gvvk2') <= 0.39189615845680237) ? " + 
"(b('svvk3') <= -0.0038270524237304926) ? " + 
"0.01764858356875698" + 
":  " + 
"0.007775354383165993" + 
":  " + 
"(b('trees') <= 14.095518112182617) ? " + 
"0.003692599487149563" + 
":  " + 
"-0.004081072851355328" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 812.5) ? " + 
"(b('lon') <= -97.97296905517578) ? " + 
"(b('L8b7med') <= 1732.5) ? " + 
"-0.002425551742860872" + 
":  " + 
"-0.01766747909476266" + 
":  " + 
"(b('trees') <= 19.091548919677734) ? " + 
"0.0020274424507420396" + 
":  " + 
"-0.005111575264117847" + 
":  " + 
"(b('lat') <= 55.97799873352051) ? " + 
"(b('L8b7med') <= 2145.75) ? " + 
"0.0024407992982870613" + 
":  " + 
"-0.0008778230459207005" + 
":  " + 
"(b('ndvi_med') <= 3324.0) ? " + 
"-0.036716704785688864" + 
":  " + 
"-0.006932089109506527" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('lon') <= -120.79476547241211) ? " + 
"(b('ndvi_med') <= 2381.0) ? " + 
"-0.0012296153182241726" + 
":  " + 
"0.026576317859977883" + 
":  " + 
"(b('trees') <= 13.5133695602417) ? " + 
"-0.0010013198071490658" + 
":  " + 
"-0.012862735422732955" + 
":  " + 
"(b('trees') <= 17.868996620178223) ? " + 
"(b('trees') <= 12.70752239227295) ? " + 
"0.00016556114258579056" + 
":  " + 
"-0.0040094535567880485" + 
":  " + 
"(b('gvvk2') <= 0.4131945073604584) ? " + 
"0.004885976420671013" + 
":  " + 
"-0.011063602824161373" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 6132.5) ? " + 
"(b('ndvi_med') <= 5941.25) ? " + 
"(b('ndvi_med') <= 5916.25) ? " + 
"3.558998031650282e-05" + 
":  " + 
"-0.012702553861556406" + 
":  " + 
"(b('lat') <= 53.63138008117676) ? " + 
"0.033683816652559206" + 
":  " + 
"0.007628723434433715" + 
":  " + 
"(b('gvvk2') <= 0.1478906273841858) ? " + 
"-0.002313557954442713" + 
":  " + 
"(b('lat') <= 53.63241958618164) ? " + 
"-0.008480190329531123" + 
":  " + 
"-0.014489385661280219" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"(b('ndvi_med') <= 1600.0) ? " + 
"0.0039059869040461615" + 
":  " + 
"-0.00035530004475740163" + 
":  " + 
"(b('sand') <= 29.5) ? " + 
"0.023353741605907058" + 
":  " + 
"-0.009778349197337223" + 
":  " + 
"(b('L8b7med') <= 2269.0) ? " + 
"(b('L8b1med') <= 657.5) ? " + 
"0.036440736391131934" + 
":  " + 
"0.008801536954976763" + 
":  " + 
"(b('lat') <= 41.34071922302246) ? " + 
"0.002556527144060721" + 
":  " + 
"-0.005503522927685119" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 168.5) ? " + 
"(b('sand') <= 74.5) ? " + 
"-0.000209309677059897" + 
":  " + 
"0.002548401499416771" + 
":  " + 
"(b('L8b2med') <= 740.5) ? " + 
"0.0038761107210112528" + 
":  " + 
"0.01718943987762102" + 
":  " + 
"-0.01480358776777449" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 27.291908264160156) ? " + 
"(b('L8b3med') <= 812.5) ? " + 
"-0.001126454896411818" + 
":  " + 
"0.0005277558005025408" + 
":  " + 
"-0.01724778374512101" + 
":  " + 
"(b('L8b6med') <= 2496.75) ? " + 
"0.018912238287069116" + 
":  " + 
"(b('gvvk2') <= 0.24988791346549988) ? " + 
"0.005332688810806327" + 
":  " + 
"-0.000586333275855111" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -101.20384979248047) ? " + 
"(b('lon') <= -101.52000045776367) ? " + 
"(b('gvvk2') <= 0.5322960615158081) ? " + 
"-0.0007929656560488443" + 
":  " + 
"0.014398380015363827" + 
":  " + 
"(b('gvvk2') <= 0.3703693151473999) ? " + 
"-0.03831886227153872" + 
":  " + 
"-0.032721425734867526" + 
":  " + 
"(b('lon') <= -100.3012466430664) ? " + 
"(b('L8b1med') <= 393.5) ? " + 
"0.007595531849820786" + 
":  " + 
"0.024155764813646546" + 
":  " + 
"(b('L8b7med') <= 2026.25) ? " + 
"0.001545795983717248" + 
":  " + 
"-0.0028635815004276572" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2802.5) ? " + 
"(b('L8b7med') <= 2637.0) ? " + 
"(b('L8b7med') <= 2616.25) ? " + 
"4.858209605055339e-06" + 
":  " + 
"0.01325278312099091" + 
":  " + 
"(b('L8b1med') <= 653.5) ? " + 
"-0.01775445948243178" + 
":  " + 
"-0.0037769594760543443" + 
":  " + 
"(b('lat') <= 41.369455337524414) ? " + 
"(b('lat') <= 36.14150428771973) ? " + 
"-0.000705271060029987" + 
":  " + 
"0.008521998350472916" + 
":  " + 
"(b('L8b6med') <= 3825.5) ? " + 
"-0.01882503393003981" + 
":  " + 
"-0.005760962542661372" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('lat') <= 38.4822998046875) ? " + 
"(b('lat') <= 36.20913124084473) ? " + 
"-0.0034701863156965606" + 
":  " + 
"-0.01768857481653332" + 
":  " + 
"(b('lat') <= 41.24547004699707) ? " + 
"0.021476908391463337" + 
":  " + 
"-0.0014030840879509154" + 
":  " + 
"(b('svvk3') <= -0.017486218363046646) ? " + 
"(b('bulk') <= 146.5) ? " + 
"0.006911112691600639" + 
":  " + 
"0.03232047585904625" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.00850809964541553" + 
":  " + 
"0.00010078385106789557" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.09767632186412811) ? " + 
"(b('svvk3') <= 0.09684375673532486) ? " + 
"(b('svvk3') <= 0.03547702915966511) ? " + 
"-0.00023893656078514413" + 
":  " + 
"0.002065455587313694" + 
":  " + 
"0.02009985542255288" + 
":  " + 
"(b('sand') <= 46.0) ? " + 
"(b('clay') <= 18.5) ? " + 
"-0.017649088319165555" + 
":  " + 
"-0.004061575779840075" + 
":  " + 
"(b('L8b7med') <= 1758.5) ? " + 
"-0.00337015259242864" + 
":  " + 
"0.003145804914211825" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('L8b2med') <= 267.5) ? " + 
"-0.009064188545510221" + 
":  " + 
"-0.010500699023615223" + 
":  " + 
"(b('L8b1med') <= 348.5) ? " + 
"(b('L8b1med') <= 338.0) ? " + 
"0.0005024655020137485" + 
":  " + 
"0.009822893020143738" + 
":  " + 
"(b('L8b7med') <= 1428.5) ? " + 
"-0.007174946513584718" + 
":  " + 
"-8.507393253364784e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 56.04010009765625) ? " + 
"(b('L8b3med') <= 812.5) ? " + 
"(b('L8b7med') <= 1611.75) ? " + 
"0.0009302825306475517" + 
":  " + 
"-0.005348388135170087" + 
":  " + 
"(b('sand') <= 65.5) ? " + 
"0.0008590777591526252" + 
":  " + 
"-0.00533999909984399" + 
":  " + 
"(b('L8b6med') <= 2358.5) ? " + 
"(b('L8b6med') <= 2322.0) ? " + 
"0.0021810899377141396" + 
":  " + 
"-0.004252248853335527" + 
":  " + 
"(b('L8b1med') <= 416.25) ? " + 
"0.010303895975902214" + 
":  " + 
"0.01256441331226299" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.13317912071943283) ? " + 
"(b('bulk') <= 147.0) ? " + 
"(b('lat') <= 39.1337947845459) ? " + 
"-0.015408616421151669" + 
":  " + 
"-0.0008552529275635143" + 
":  " + 
"(b('L8b1med') <= 1070.0) ? " + 
"0.016374937187088764" + 
":  " + 
"-0.0038598486561443926" + 
":  " + 
"(b('trees') <= 15.19383430480957) ? " + 
"(b('trees') <= 12.70752239227295) ? " + 
"8.600586110078797e-05" + 
":  " + 
"-0.005113525412557138" + 
":  " + 
"(b('trees') <= 19.810494422912598) ? " + 
"0.006880500719432571" + 
":  " + 
"-0.0016826370064937858" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 74.5) ? " + 
"(b('sand') <= 73.0) ? " + 
"(b('L8b3med') <= 812.5) ? " + 
"-0.0015272669319041005" + 
":  " + 
"0.0005515562672818757" + 
":  " + 
"(b('ndvi_med') <= 3324.0) ? " + 
"-0.03222786971009703" + 
":  " + 
"-0.006738690577530959" + 
":  " + 
"(b('gvvk2') <= 0.39508508145809174) ? " + 
"(b('L8b6med') <= 2573.5) ? " + 
"0.009006060144755598" + 
":  " + 
"-2.7933128040266708e-05" + 
":  " + 
"(b('bulk') <= 129.0) ? " + 
"0.0036196874972723755" + 
":  " + 
"-0.0025144541148469346" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 168.5) ? " + 
"(b('L8b7med') <= 2145.75) ? " + 
"0.0005035494109644255" + 
":  " + 
"-0.0009950013311856507" + 
":  " + 
"(b('ndvi_med') <= 1281.5) ? " + 
"0.0033871934889758287" + 
":  " + 
"0.015369189729924612" + 
":  " + 
"-0.013424535150931338" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 6132.5) ? " + 
"(b('ndvi_med') <= 5941.25) ? " + 
"(b('ndvi_med') <= 5916.25) ? " + 
"2.937115018635721e-05" + 
":  " + 
"-0.011033474236595786" + 
":  " + 
"(b('ndvi_med') <= 6002.25) ? " + 
"0.029986358694477633" + 
":  " + 
"0.006977712546579196" + 
":  " + 
"(b('L8b7med') <= 2100.0) ? " + 
"(b('L8b2med') <= 609.0) ? " + 
"-0.0023171525729576703" + 
":  " + 
"-0.00752030984098917" + 
":  " + 
"-0.01292858563956334" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 616.25) ? " + 
"(b('ndvi_med') <= 2285.5) ? " + 
"-0.025530580899562783" + 
":  " + 
"(b('trees') <= 11.134622573852539) ? " + 
"0.001653028504294891" + 
":  " + 
"-0.00779192315589206" + 
":  " + 
"(b('L8b3med') <= 618.5) ? " + 
"(b('svvk3') <= 0.03304598666727543) ? " + 
"0.026138228531322805" + 
":  " + 
"0.021314041185524435" + 
":  " + 
"(b('L8b1med') <= 307.5) ? " + 
"0.0034211494482732085" + 
":  " + 
"-0.00021261607359830548" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('lat') <= 38.4822998046875) ? " + 
"(b('lat') <= 36.20913124084473) ? " + 
"-0.003279854991367753" + 
":  " + 
"-0.015981356493810855" + 
":  " + 
"(b('lat') <= 41.24547004699707) ? " + 
"0.019254851701247577" + 
":  " + 
"-0.0013158674711493375" + 
":  " + 
"(b('svvk3') <= -0.017486218363046646) ? " + 
"(b('lat') <= 38.62164497375488) ? " + 
"0.029014062422072218" + 
":  " + 
"0.006473903240235658" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.007649219984052144" + 
":  " + 
"9.396799683265382e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('L8b3med') <= 569.0) ? " + 
"-0.008235944824877162" + 
":  " + 
"-0.009804335067863823" + 
":  " + 
"(b('L8b3med') <= 555.5) ? " + 
"(b('svvk3') <= 0.002427630541205872) ? " + 
"0.005313013380020548" + 
":  " + 
"0.014496522237612552" + 
":  " + 
"(b('L8b3med') <= 616.25) ? " + 
"-0.0035831738209766966" + 
":  " + 
"0.0001596129085310086" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 27.291908264160156) ? " + 
"(b('ndvi_med') <= 2473.0) ? " + 
"0.0006123501561138007" + 
":  " + 
"-0.0007354703881369859" + 
":  " + 
"-0.015244998618587247" + 
":  " + 
"(b('lon') <= -77.63019943237305) ? " + 
"(b('L8b1med') <= 346.75) ? " + 
"0.0005835863358320537" + 
":  " + 
"0.005698994006660352" + 
":  " + 
"0.016068048609470642" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -101.20384979248047) ? " + 
"(b('lon') <= -101.52000045776367) ? " + 
"(b('gvvk2') <= 0.5322960615158081) ? " + 
"-0.0007711757380170073" + 
":  " + 
"0.012862635887440854" + 
":  " + 
"(b('ndvi_med') <= 2589.0) ? " + 
"-0.033770015781000834" + 
":  " + 
"-0.028732322897996765" + 
":  " + 
"(b('lon') <= -100.3012466430664) ? " + 
"(b('L8b3med') <= 748.0) ? " + 
"0.006925071861640958" + 
":  " + 
"0.020177538917857674" + 
":  " + 
"(b('L8b7med') <= 2026.25) ? " + 
"0.001422934180664915" + 
":  " + 
"-0.0024364414924698007" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -5.20074987411499) ? " + 
"(b('ndvi_med') <= 1531.0) ? " + 
"(b('L8b6med') <= 3714.0) ? " + 
"0.00217293928562343" + 
":  " + 
"-0.001151650303823623" + 
":  " + 
"(b('clay') <= 25.0) ? " + 
"0.013100589288469966" + 
":  " + 
"0.009739988516955456" + 
":  " + 
"(b('lon') <= 25.16578960418701) ? " + 
"(b('bulk') <= 141.5) ? " + 
"0.0008055305251659368" + 
":  " + 
"-0.0007829233113882393" + 
":  " + 
"(b('lat') <= 44.32053565979004) ? " + 
"-0.014441395319537193" + 
":  " + 
"-0.0029672807288294817" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"(b('ndvi_med') <= 1600.0) ? " + 
"0.0033811339019468" + 
":  " + 
"-0.0003293713390152999" + 
":  " + 
"(b('trees') <= 2.910244882106781) ? " + 
"-0.009811105329195484" + 
":  " + 
"0.008883129406051321" + 
":  " + 
"(b('L8b1med') <= 698.25) ? " + 
"(b('lon') <= -105.95555114746094) ? " + 
"0.01568022803972824" + 
":  " + 
"-0.0018636257495938042" + 
":  " + 
"(b('lon') <= -104.90133666992188) ? " + 
"-0.002724222975205821" + 
":  " + 
"0.01028472844338244" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('ndvi_med') <= 5217.0) ? " + 
"(b('lat') <= 38.4822998046875) ? " + 
"-0.007891974748611967" + 
":  " + 
"0.0006968047666271593" + 
":  " + 
"-0.022849386246055203" + 
":  " + 
"(b('svvk3') <= -0.017486218363046646) ? " + 
"(b('L8b1med') <= 431.75) ? " + 
"-0.0008335638572028459" + 
":  " + 
"0.017731475988396493" + 
":  " + 
"(b('L8b1med') <= 540.5) ? " + 
"0.0006990626871314301" + 
":  " + 
"-0.001241543028004335" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 620.75) ? " + 
"(b('trees') <= 0.03652967885136604) ? " + 
"0.0015288753269629598" + 
":  " + 
"-0.0007954058562547639" + 
":  " + 
"(b('svvk3') <= 0.03734981268644333) ? " + 
"-0.010914217657319591" + 
":  " + 
"0.008259171827025411" + 
":  " + 
"(b('ndvi_med') <= 1658.5) ? " + 
"(b('svvk3') <= 0.018095525912940502) ? " + 
"0.0029381490137685602" + 
":  " + 
"-0.0047988498633856" + 
":  " + 
"(b('ndvi_med') <= 1670.5) ? " + 
"0.03879713360086126" + 
":  " + 
"0.005613364776907824" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"(b('gvvk2') <= 0.3441760092973709) ? " + 
"0.0019569663141871664" + 
":  " + 
"-0.0022111066383777725" + 
":  " + 
"0.051665307223840995" + 
":  " + 
"(b('lat') <= 43.663949966430664) ? " + 
"(b('svvk3') <= 0.008385543478652835) ? " + 
"-0.02960614847219755" + 
":  " + 
"-0.027388081497785308" + 
":  " + 
"(b('bulk') <= 147.5) ? " + 
"-0.000223377496951424" + 
":  " + 
"-0.03139578064899223" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('bulk') <= 153.0) ? " + 
"-0.0048240756353068355" + 
":  " + 
"0.010531617231590691" + 
":  " + 
"(b('L8b6med') <= 2857.75) ? " + 
"-0.0006838320203422786" + 
":  " + 
"0.0009609265890206284" + 
":  " + 
"-0.012751544167727086" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 1701.5) ? " + 
"(b('L8b7med') <= 3254.25) ? " + 
"(b('L8b7med') <= 3008.25) ? " + 
"4.233132943175883e-05" + 
":  " + 
"-0.0065391828177502115" + 
":  " + 
"(b('L8b6med') <= 4001.0) ? " + 
"0.013139928533884238" + 
":  " + 
"0.0005593294831868713" + 
":  " + 
"(b('ndvi_med') <= 889.5) ? " + 
"(b('lon') <= -115.85380172729492) ? " + 
"-0.002649402386466243" + 
":  " + 
"-0.007136053624698463" + 
":  " + 
"-0.012046310738869553" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -101.20384979248047) ? " + 
"(b('lon') <= -101.52000045776367) ? " + 
"(b('gvvk2') <= 0.5322960615158081) ? " + 
"-0.0007122618438628355" + 
":  " + 
"0.011672200294673845" + 
":  " + 
"(b('L8b7med') <= 1806.5) ? " + 
"-0.02568539421163736" + 
":  " + 
"-0.03038379366727731" + 
":  " + 
"(b('lon') <= -100.3012466430664) ? " + 
"(b('L8b7med') <= 1543.25) ? " + 
"0.006207488157893987" + 
":  " + 
"0.01808339956672908" + 
":  " + 
"(b('lon') <= -99.3036994934082) ? " + 
"-0.01657309655206534" + 
":  " + 
"0.0004493940560668247" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.08964456990361214) ? " + 
"(b('svvk3') <= 0.08114498481154442) ? " + 
"(b('lat') <= 56.000450134277344) ? " + 
"-8.104847017175667e-05" + 
":  " + 
"0.004786982838954439" + 
":  " + 
"(b('L8b3med') <= 1090.0) ? " + 
"0.017864863802011466" + 
":  " + 
"0.014144788419941531" + 
":  " + 
"(b('L8b2med') <= 520.5) ? " + 
"(b('L8b7med') <= 1567.0) ? " + 
"-0.0049638357966401885" + 
":  " + 
"-0.012536371739457616" + 
":  " + 
"(b('ndvi_med') <= 1199.5) ? " + 
"-0.016260249843835006" + 
":  " + 
"0.001158071123637511" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 53.5) ? " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= 1.4101499915122986) ? " + 
"0.0008189000707882741" + 
":  " + 
"0.038843882761992354" + 
":  " + 
"(b('clay') <= 17.0) ? " + 
"0.003160403589687401" + 
":  " + 
"-0.00727560175036057" + 
":  " + 
"(b('sand') <= 55.5) ? " + 
"(b('gvvk2') <= 0.31612052023410797) ? " + 
"0.0014221240577576993" + 
":  " + 
"-0.018460883294722223" + 
":  " + 
"(b('ndvi_med') <= 734.25) ? " + 
"0.013937277284702726" + 
":  " + 
"-8.12783239769872e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 616.25) ? " + 
"(b('ndvi_med') <= 2285.5) ? " + 
"-0.02304475928830005" + 
":  " + 
"(b('svvk3') <= 0.005930787650868297) ? " + 
"0.004394668761394595" + 
":  " + 
"-0.004170837058447012" + 
":  " + 
"(b('L8b3med') <= 618.5) ? " + 
"(b('gvvk2') <= 0.2460666447877884) ? " + 
"0.018619688035771742" + 
":  " + 
"0.022961456646990286" + 
":  " + 
"(b('L8b1med') <= 307.5) ? " + 
"0.00302126566357518" + 
":  " + 
"-0.00017777482622274423" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('L8b3med') <= 754.0) ? " + 
"(b('trees') <= 19.401613235473633) ? " + 
"0.005913242971033001" + 
":  " + 
"-0.002629180283832929" + 
":  " + 
"(b('L8b1med') <= 518.25) ? " + 
"-0.008438180412101776" + 
":  " + 
"0.0025230339566967275" + 
":  " + 
"(b('svvk3') <= -0.017486218363046646) ? " + 
"(b('ndvi_med') <= 4896.0) ? " + 
"0.01272409420996841" + 
":  " + 
"-0.012259798185626586" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.006625321644079381" + 
":  " + 
"0.00011270085467386547" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.13317912071943283) ? " + 
"(b('bulk') <= 147.0) ? " + 
"(b('lat') <= 39.1337947845459) ? " + 
"-0.013727568361047632" + 
":  " + 
"-0.00038071483791575765" + 
":  " + 
"(b('L8b1med') <= 1070.0) ? " + 
"0.01362231910242886" + 
":  " + 
"-0.003395717483688732" + 
":  " + 
"(b('trees') <= 15.19383430480957) ? " + 
"(b('trees') <= 12.70752239227295) ? " + 
"6.13033727582075e-05" + 
":  " + 
"-0.004671469624019004" + 
":  " + 
"(b('clay') <= 26.5) ? " + 
"0.003272577241091077" + 
":  " + 
"-0.01338253375120389" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 101.0) ? " + 
"(b('L8b3med') <= 895.5) ? " + 
"(b('ndvi_med') <= 4913.25) ? " + 
"-0.008931416393622285" + 
":  " + 
"-0.006149533890307479" + 
":  " + 
"-0.0006660668974687034" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"(b('ndvi_med') <= 2114.0) ? " + 
"0.00030706001129365834" + 
":  " + 
"0.025364607086891977" + 
":  " + 
"(b('bulk') <= 106.5) ? " + 
"-0.009470069368805623" + 
":  " + 
"6.752949404742272e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 822.25) ? " + 
"(b('L8b1med') <= 805.0) ? " + 
"(b('L8b7med') <= 3356.5) ? " + 
"-6.387212281155146e-05" + 
":  " + 
"0.008146080469958848" + 
":  " + 
"(b('lon') <= -104.46354293823242) ? " + 
"0.009147035317277605" + 
":  " + 
"0.028999184926916416" + 
":  " + 
"(b('L8b1med') <= 877.25) ? " + 
"(b('L8b1med') <= 826.0) ? " + 
"-0.031688355176044194" + 
":  " + 
"-0.014413724711922263" + 
":  " + 
"(b('sand') <= 65.5) ? " + 
"0.0021401832926635474" + 
":  " + 
"-0.01010241909000382" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 6132.5) ? " + 
"(b('ndvi_med') <= 5941.25) ? " + 
"(b('ndvi_med') <= 5916.25) ? " + 
"2.4653341053696738e-05" + 
":  " + 
"-0.009511418257675078" + 
":  " + 
"(b('lat') <= 53.63138008117676) ? " + 
"0.026537786796989593" + 
":  " + 
"0.0062159428311944764" + 
":  " + 
"(b('lat') <= 53.63138008117676) ? " + 
"-0.0019126713002020623" + 
":  " + 
"(b('clay') <= 13.5) ? " + 
"-0.0068322773176170415" + 
":  " + 
"-0.011699725536333805" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -101.20384979248047) ? " + 
"(b('lon') <= -101.52000045776367) ? " + 
"(b('L8b7med') <= 1944.0) ? " + 
"-0.0033448122770117833" + 
":  " + 
"0.0007343884956134394" + 
":  " + 
"(b('L8b7med') <= 1806.5) ? " + 
"-0.02319309396188518" + 
":  " + 
"-0.02742165347196114" + 
":  " + 
"(b('lon') <= -100.3012466430664) ? " + 
"(b('L8b2med') <= 483.5) ? " + 
"0.0055105001706930445" + 
":  " + 
"0.016118476001910565" + 
":  " + 
"(b('L8b7med') <= 2026.25) ? " + 
"0.0012388479758134862" + 
":  " + 
"-0.0020760036007774893" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"(b('svvk3') <= -0.005489814328029752) ? " + 
"-0.0035921064585614105" + 
":  " + 
"0.001072935208187094" + 
":  " + 
"0.04631786319594838" + 
":  " + 
"(b('lat') <= 43.663949966430664) ? " + 
"(b('L8b3med') <= 768.75) ? " + 
"-0.0242556550382398" + 
":  " + 
"-0.026251915315210823" + 
":  " + 
"(b('bulk') <= 147.5) ? " + 
"-0.00024217293251809621" + 
":  " + 
"-0.027460656410763812" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.09767632186412811) ? " + 
"(b('svvk3') <= 0.09684375673532486) ? " + 
"(b('sand') <= 53.5) ? " + 
"0.000543811213145059" + 
":  " + 
"-0.0011028600385983097" + 
":  " + 
"0.018117080698893256" + 
":  " + 
"(b('ndvi_med') <= 1199.5) ? " + 
"-0.014899301248260305" + 
":  " + 
"(b('L8b1med') <= 352.5) ? " + 
"-0.009352352367727232" + 
":  " + 
"-0.0003230885400367766" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.24172427505254745) ? " + 
"(b('lat') <= 42.940900802612305) ? " + 
"(b('L8b7med') <= 1528.5) ? " + 
"0.013973850583974167" + 
":  " + 
"0.0001357297350738836" + 
":  " + 
"(b('svvk3') <= 0.005146448500454426) ? " + 
"-0.0012365355244443308" + 
":  " + 
"-0.011594548482511667" + 
":  " + 
"(b('gvvk2') <= 0.26724953949451447) ? " + 
"(b('L8b6med') <= 2484.75) ? " + 
"-0.006079586297144681" + 
":  " + 
"0.0058662196926830635" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"0.0014143098271641704" + 
":  " + 
"-0.0014661394977657173" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 822.25) ? " + 
"(b('L8b1med') <= 805.0) ? " + 
"(b('L8b2med') <= 1064.5) ? " + 
"5.583257639050818e-06" + 
":  " + 
"0.0177440571259512" + 
":  " + 
"(b('L8b7med') <= 3497.0) ? " + 
"0.020479446990006575" + 
":  " + 
"0.0010654096448712014" + 
":  " + 
"(b('L8b1med') <= 877.25) ? " + 
"(b('L8b1med') <= 826.0) ? " + 
"-0.028610484534463146" + 
":  " + 
"-0.01350820213548708" + 
":  " + 
"(b('sand') <= 65.5) ? " + 
"0.0017441469995403858" + 
":  " + 
"-0.008927985419152901" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"(b('gvvk2') <= 0.1353890746831894) ? " + 
"-0.0037746074101404972" + 
":  " + 
"-0.013036414549527878" + 
":  " + 
"(b('ndvi_med') <= 734.25) ? " + 
"(b('lon') <= -114.60901641845703) ? " + 
"0.0020655890167506157" + 
":  " + 
"0.022779260615265" + 
":  " + 
"(b('ndvi_med') <= 757.25) ? " + 
"-0.009343625726327439" + 
":  " + 
"2.9046270890185798e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2857.75) ? " + 
"(b('L8b6med') <= 2852.75) ? " + 
"(b('bulk') <= 148.5) ? " + 
"-0.0010436377110339666" + 
":  " + 
"0.0067448042530314535" + 
":  " + 
"-0.03467294264245169" + 
":  " + 
"(b('L8b7med') <= 1679.0) ? " + 
"(b('L8b7med') <= 1669.5) ? " + 
"0.0075028581330554844" + 
":  " + 
"0.02662659369746016" + 
":  " + 
"(b('L8b7med') <= 1698.5) ? " + 
"-0.01613360042348598" + 
":  " + 
"8.120368051635257e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 2473.0) ? " + 
"(b('L8b1med') <= 468.5) ? " + 
"(b('L8b3med') <= 650.0) ? " + 
"-0.014736230353275814" + 
":  " + 
"0.005126191291114364" + 
":  " + 
"(b('ndvi_med') <= 2223.5) ? " + 
"-0.0007343338580564695" + 
":  " + 
"0.005682995996358066" + 
":  " + 
"(b('ndvi_med') <= 2723.0) ? " + 
"(b('L8b1med') <= 515.0) ? " + 
"-0.00876204372278595" + 
":  " + 
"0.01752124338571412" + 
":  " + 
"(b('L8b7med') <= 2044.0) ? " + 
"0.001079885566910357" + 
":  " + 
"-0.004166340649185566" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 814.0) ? " + 
"(b('L8b7med') <= 1603.5) ? " + 
"(b('L8b7med') <= 1598.0) ? " + 
"0.0003118142235511526" + 
":  " + 
"0.012359841340846715" + 
":  " + 
"(b('ndvi_med') <= 4889.25) ? " + 
"-0.0048271649025020255" + 
":  " + 
"0.01934191412724151" + 
":  " + 
"(b('sand') <= 22.0) ? " + 
"(b('L8b3med') <= 1144.5) ? " + 
"-0.015068202215484383" + 
":  " + 
"-0.006899947906055241" + 
":  " + 
"(b('L8b1med') <= 470.5) ? " + 
"0.00304142041442497" + 
":  " + 
"-0.00024971938413475143" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= 1.4101499915122986) ? " + 
"(b('L8b3med') <= 699.25) ? " + 
"-0.005848890849901851" + 
":  " + 
"0.0005756479504170801" + 
":  " + 
"0.03443545011283014" + 
":  " + 
"(b('lon') <= 6.412564992904663) ? " + 
"(b('trees') <= 2.1432430148124695) ? " + 
"-0.0007590080980792585" + 
":  " + 
"-0.016123783868476255" + 
":  " + 
"(b('L8b6med') <= 2860.0) ? " + 
"-0.001454301166502397" + 
":  " + 
"0.00314335493479168" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('trees') <= 18.111291885375977) ? " + 
"(b('L8b6med') <= 2978.25) ? " + 
"0.0058090231450563246" + 
":  " + 
"-0.0040701316234231875" + 
":  " + 
"(b('sand') <= 38.5) ? " + 
"-0.019356562739217688" + 
":  " + 
"-0.0029237647322172314" + 
":  " + 
"(b('trees') <= 17.942265510559082) ? " + 
"(b('trees') <= 12.70752239227295) ? " + 
"0.0001189651622850963" + 
":  " + 
"-0.003099198595067063" + 
":  " + 
"(b('L8b1med') <= 361.5) ? " + 
"-0.004149087607802991" + 
":  " + 
"0.0062408429486598685" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 168.5) ? " + 
"(b('L8b7med') <= 2543.0) ? " + 
"0.000284907763944813" + 
":  " + 
"-0.0011816787178724625" + 
":  " + 
"(b('gvvk2') <= 0.27934402227401733) ? " + 
"0.002434962097766974" + 
":  " + 
"0.013218758714620873" + 
":  " + 
"-0.011309041566817918" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 620.75) ? " + 
"(b('L8b7med') <= 2778.0) ? " + 
"-6.393430280823625e-05" + 
":  " + 
"0.0087968799899102" + 
":  " + 
"(b('trees') <= 2.910244882106781) ? " + 
"-0.009810406398411114" + 
":  " + 
"0.007208957050327601" + 
":  " + 
"(b('L8b1med') <= 698.25) ? " + 
"(b('lon') <= -105.95555114746094) ? " + 
"0.013417096811344368" + 
":  " + 
"-0.0016324944311546295" + 
":  " + 
"(b('lon') <= -104.90133666992188) ? " + 
"-0.0022224662341429917" + 
":  " + 
"0.00803210540839656" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= 1.4101499915122986) ? " + 
"(b('L8b3med') <= 699.25) ? " + 
"-0.005294853525591987" + 
":  " + 
"0.0005323209556345247" + 
":  " + 
"0.030957911239204966" + 
":  " + 
"(b('lon') <= 6.412564992904663) ? " + 
"(b('sand') <= 32.0) ? " + 
"-0.006488621796570343" + 
":  " + 
"-0.01895855905361246" + 
":  " + 
"(b('L8b6med') <= 2860.0) ? " + 
"-0.0012877805866920722" + 
":  " + 
"0.0026890065596904796" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 19.598620414733887) ? " + 
"(b('trees') <= 18.005227088928223) ? " + 
"-0.00015504561300764183" + 
":  " + 
"0.008367138323345322" + 
":  " + 
"(b('L8b2med') <= 477.75) ? " + 
"-0.007731129780775826" + 
":  " + 
"0.002445644675495437" + 
":  " + 
"(b('L8b3med') <= 663.5) ? " + 
"(b('L8b7med') <= 1513.75) ? " + 
"0.0003557820665280875" + 
":  " + 
"0.0058135988023469976" + 
":  " + 
"0.013523871143410027" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= 1.4101499915122986) ? " + 
"0.00020478400620952731" + 
":  " + 
"0.027877624676585222" + 
":  " + 
"(b('lon') <= 6.412564992904663) ? " + 
"-0.010065367508470556" + 
":  " + 
"-0.0006701409577749397" + 
":  " + 
"(b('L8b3med') <= 703.0) ? " + 
"(b('gvvk2') <= 0.36731019616127014) ? " + 
"0.013581984163260508" + 
":  " + 
"0.005074357517495987" + 
":  " + 
"(b('gvvk2') <= 0.7149690389633179) ? " + 
"-0.00042465850160040635" + 
":  " + 
"0.006425278092912878" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 348.5) ? " + 
"(b('L8b2med') <= 418.5) ? " + 
"(b('L8b2med') <= 416.25) ? " + 
"0.00042070893827413856" + 
":  " + 
"-0.014316884924496056" + 
":  " + 
"(b('L8b6med') <= 2695.75) ? " + 
"0.009087616206372674" + 
":  " + 
"-0.005700907609712996" + 
":  " + 
"(b('L8b6med') <= 2527.0) ? " + 
"(b('lon') <= -119.64704132080078) ? " + 
"0.009004899489903817" + 
":  " + 
"-0.0032554119691873" + 
":  " + 
"(b('L8b3med') <= 750.5) ? " + 
"0.009236924112295668" + 
":  " + 
"-0.0001169476564065314" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -97.97296905517578) ? " + 
"(b('L8b7med') <= 1925.5) ? " + 
"(b('L8b7med') <= 1901.0) ? " + 
"-0.0026565601681374233" + 
":  " + 
"-0.02541521760832428" + 
":  " + 
"(b('svvk3') <= 0.018095525912940502) ? " + 
"0.002459670582179384" + 
":  " + 
"-0.0025937968678561383" + 
":  " + 
"(b('lon') <= -71.2344970703125) ? " + 
"(b('gvvk2') <= 0.3408670127391815) ? " + 
"0.007790975188884545" + 
":  " + 
"-0.0024155290801052528" + 
":  " + 
"(b('svvk3') <= 0.012301221489906311) ? " + 
"-0.0021930295444584267" + 
":  " + 
"0.00234386438073363" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 141.5) ? " + 
"(b('svvk3') <= -0.00022306357277557254) ? " + 
"(b('L8b7med') <= 1869.25) ? " + 
"0.0004248233913974115" + 
":  " + 
"0.006521600953053285" + 
":  " + 
"(b('svvk3') <= 0.007927745580673218) ? " + 
"-0.002733257574176051" + 
":  " + 
"0.0012084494023225857" + 
":  " + 
"(b('lat') <= 48.39845085144043) ? " + 
"(b('lat') <= 42.05975532531738) ? " + 
"5.543017914164779e-05" + 
":  " + 
"-0.005786347607445946" + 
":  " + 
"(b('L8b3med') <= 943.75) ? " + 
"0.04088827580281573" + 
":  " + 
"3.209312517171714e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2559.5) ? " + 
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 639.75) ? " + 
"4.0441532855816255e-05" + 
":  " + 
"-0.021060336653520806" + 
":  " + 
"(b('L8b1med') <= 691.75) ? " + 
"0.010350873357831927" + 
":  " + 
"-0.0003784656506650328" + 
":  " + 
"(b('svvk3') <= 0.014319155365228653) ? " + 
"(b('svvk3') <= 0.012463945895433426) ? " + 
"-0.0004562773654969164" + 
":  " + 
"0.019638353506663913" + 
":  " + 
"(b('L8b6med') <= 3626.5) ? " + 
"-0.010484364040158527" + 
":  " + 
"-0.00015277118832839244" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('ndvi_med') <= 5217.0) ? " + 
"(b('lat') <= 38.4822998046875) ? " + 
"-0.006463425856860861" + 
":  " + 
"0.000513820715523348" + 
":  " + 
"-0.02058228391652453" + 
":  " + 
"(b('svvk3') <= -0.017486218363046646) ? " + 
"(b('L8b1med') <= 365.0) ? " + 
"-0.009527524483603333" + 
":  " + 
"0.010252716612706828" + 
":  " + 
"(b('L8b1med') <= 459.5) ? " + 
"0.0009347709209975004" + 
":  " + 
"-0.0007792582043015323" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 19.0) ? " + 
"(b('svvk3') <= 0.02013546973466873) ? " + 
"(b('svvk3') <= 0.0003794842923525716) ? " + 
"-0.005570318802529006" + 
":  " + 
"0.005097614923856686" + 
":  " + 
"(b('lon') <= -97.09158706665039) ? " + 
"-0.003150925274906291" + 
":  " + 
"-0.027579013585022627" + 
":  " + 
"(b('sand') <= 20.5) ? " + 
"0.01708316983771327" + 
":  " + 
"(b('gvvk2') <= 0.041203947737812996) ? " + 
"0.010067731433262173" + 
":  " + 
"-3.9291521321944097e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 101.0) ? " + 
"(b('lat') <= 42.565256118774414) ? " + 
"-0.0018885577441474372" + 
":  " + 
"(b('L8b3med') <= 706.5) ? " + 
"-0.006843187640474452" + 
":  " + 
"-0.005453114510300727" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"(b('L8b7med') <= 1430.0) ? " + 
"0.0010031166651983114" + 
":  " + 
"0.021554345049499213" + 
":  " + 
"(b('bulk') <= 106.5) ? " + 
"-0.006939061030048821" + 
":  " + 
"4.7506819977445734e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"(b('svvk3') <= 0.002330337418243289) ? " + 
"-0.0032531534277983054" + 
":  " + 
"-0.011588779853246953" + 
":  " + 
"(b('ndvi_med') <= 734.25) ? " + 
"(b('lon') <= -114.60901641845703) ? " + 
"0.0023075421337992257" + 
":  " + 
"0.020687283475576496" + 
":  " + 
"(b('L8b1med') <= 822.25) ? " + 
"0.00012882966557205725" + 
":  " + 
"-0.003044658277671378" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('L8b3med') <= 836.5) ? " + 
"(b('lon') <= -80.78388977050781) ? " + 
"-0.01736835912697356" + 
":  " + 
"0.001284470373747293" + 
":  " + 
"(b('L8b2med') <= 580.5) ? " + 
"0.016802178909014753" + 
":  " + 
"-0.0019798197666267745" + 
":  " + 
"(b('trees') <= 17.942265510559082) ? " + 
"(b('trees') <= 12.70752239227295) ? " + 
"0.0001322971668513813" + 
":  " + 
"-0.00284137887198236" + 
":  " + 
"(b('L8b3med') <= 791.25) ? " + 
"-0.0015320148125503362" + 
":  " + 
"0.0077147837298854926" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('sand') <= 53.5) ? " + 
"(b('sand') <= 51.5) ? " + 
"4.6511766497649215e-05" + 
":  " + 
"0.0051134063102528885" + 
":  " + 
"(b('gvvk2') <= 0.26820625364780426) ? " + 
"0.0015601938777975379" + 
":  " + 
"-0.003263303244775804" + 
":  " + 
"(b('gvvk2') <= 0.39189615845680237) ? " + 
"(b('ndvi_med') <= 3523.5) ? " + 
"0.012234080009919934" + 
":  " + 
"0.005520053238348505" + 
":  " + 
"(b('gvvk2') <= 0.41833437979221344) ? " + 
"-0.005091644099948588" + 
":  " + 
"0.0027578336483698646" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('trees') <= 0.03652967885136604) ? " + 
"(b('svvk3') <= 0.014892799779772758) ? " + 
"0.0020493014597493826" + 
":  " + 
"-0.0014386471344292116" + 
":  " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"-0.004391580012699544" + 
":  " + 
"0.0003820499370825652" + 
":  " + 
"-0.01042746894784348" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.007927745580673218) ? " + 
"(b('svvk3') <= 0.006862902082502842) ? " + 
"(b('svvk3') <= 0.0063597087282687426) ? " + 
"-0.0004023169970079569" + 
":  " + 
"0.008537159127263369" + 
":  " + 
"(b('lat') <= 49.354835510253906) ? " + 
"-0.0047239497329953" + 
":  " + 
"-0.018594132711029065" + 
":  " + 
"(b('clay') <= 16.5) ? " + 
"(b('gvvk2') <= 0.46479226648807526) ? " + 
"0.005084571507056676" + 
":  " + 
"-0.0023223788739798346" + 
":  " + 
"(b('clay') <= 17.5) ? " + 
"-0.016254577265845335" + 
":  " + 
"0.00022862235775352187" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('gvvk2') <= 0.4162828177213669) ? " + 
"8.444711444919367e-05" + 
":  " + 
"-0.005411418679461637" + 
":  " + 
"-0.039783590770973376" + 
":  " + 
"(b('gvvk2') <= 0.46257317066192627) ? " + 
"(b('L8b6med') <= 2676.5) ? " + 
"0.002417446251955703" + 
":  " + 
"0.019800385402993184" + 
":  " + 
"(b('trees') <= 6.110170364379883) ? " + 
"0.0018172379958713589" + 
":  " + 
"-0.0035170952561970822" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3782.0) ? " + 
"(b('ndvi_med') <= 3733.5) ? " + 
"(b('ndvi_med') <= 3698.5) ? " + 
"-0.00020239810529876952" + 
":  " + 
"0.01283408245575445" + 
":  " + 
"(b('L8b6med') <= 2735.5) ? " + 
"-0.0027809955994289454" + 
":  " + 
"-0.02340101481536598" + 
":  " + 
"(b('trees') <= 10.084112167358398) ? " + 
"(b('lon') <= 22.981855392456055) ? " + 
"-0.0022095793621680444" + 
":  " + 
"0.010268804573437013" + 
":  " + 
"(b('L8b7med') <= 1852.75) ? " + 
"0.0017258719847457586" + 
":  " + 
"0.016173500411747643" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 6132.5) ? " + 
"(b('ndvi_med') <= 5941.25) ? " + 
"(b('ndvi_med') <= 5916.25) ? " + 
"3.158310721207852e-05" + 
":  " + 
"-0.008714828500813862" + 
":  " + 
"(b('L8b7med') <= 2025.5) ? " + 
"0.021375459236056993" + 
":  " + 
"0.005204472741937277" + 
":  " + 
"(b('L8b2med') <= 595.5) ? " + 
"-0.010226135015478421" + 
":  " + 
"(b('L8b1med') <= 464.5) ? " + 
"-0.00289161100387042" + 
":  " + 
"-0.0053449147262474295" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 1067.75) ? " + 
"(b('L8b2med') <= 1064.5) ? " + 
"(b('L8b1med') <= 822.25) ? " + 
"9.590794537657288e-05" + 
":  " + 
"-0.015043260177871345" + 
":  " + 
"(b('L8b7med') <= 4021.5) ? " + 
"0.00827611296721526" + 
":  " + 
"-0.003996494584294061" + 
":  " + 
"(b('svvk3') <= 0.007063381839543581) ? " + 
"(b('lon') <= -115.77193450927734) ? " + 
"-0.008023960476829786" + 
":  " + 
"-0.0011458124991030431" + 
":  " + 
"(b('gvvk2') <= 0.285125270485878) ? " + 
"0.013355761731496794" + 
":  " + 
"-0.0023374889365217013" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2559.5) ? " + 
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 639.75) ? " + 
"3.6362968425176065e-05" + 
":  " + 
"-0.019073615009944256" + 
":  " + 
"(b('L8b1med') <= 645.0) ? " + 
"0.02660942129101454" + 
":  " + 
"0.0032329103470123714" + 
":  " + 
"(b('L8b7med') <= 2802.5) ? " + 
"(b('L8b3med') <= 874.0) ? " + 
"0.016496947457222258" + 
":  " + 
"-0.0045157169394164694" + 
":  " + 
"(b('lat') <= 41.369455337524414) ? " + 
"0.002330451875366211" + 
":  " + 
"-0.00841007155541053" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('L8b3med') <= 836.5) ? " + 
"(b('lat') <= 42.12541389465332) ? " + 
"-0.01563873798794987" + 
":  " + 
"0.0009820834104322107" + 
":  " + 
"(b('L8b1med') <= 424.75) ? " + 
"0.015114746244439592" + 
":  " + 
"-0.002042149876234215" + 
":  " + 
"(b('L8b2med') <= 1322.75) ? " + 
"(b('gvvk2') <= 0.16195345669984818) ? " + 
"0.0037925953906083874" + 
":  " + 
"1.0151259781858871e-05" + 
":  " + 
"(b('L8b7med') <= 2767.0) ? " + 
"-0.00853291504198389" + 
":  " + 
"-0.0007469155623587381" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -106.49531555175781) ? " + 
"(b('lon') <= -107.54017639160156) ? " + 
"(b('L8b1med') <= 426.5) ? " + 
"0.009413681694675583" + 
":  " + 
"-0.0004770129575402668" + 
":  " + 
"(b('lon') <= -107.32173538208008) ? " + 
"-0.02796746303297737" + 
":  " + 
"-0.003968234277218897" + 
":  " + 
"(b('lon') <= -105.20199966430664) ? " + 
"(b('gvvk2') <= 0.3184741586446762) ? " + 
"0.027568256771701646" + 
":  " + 
"-0.005273752421671621" + 
":  " + 
"(b('svvk3') <= 0.012301221489906311) ? " + 
"-0.0007452920915034825" + 
":  " + 
"0.0018829722748095851" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3782.0) ? " + 
"(b('ndvi_med') <= 3733.5) ? " + 
"(b('ndvi_med') <= 3698.5) ? " + 
"-0.00019275158006775613" + 
":  " + 
"0.011607802891249788" + 
":  " + 
"(b('L8b6med') <= 2735.5) ? " + 
"-0.00228462024912951" + 
":  " + 
"-0.020842637543472847" + 
":  " + 
"(b('trees') <= 10.084112167358398) ? " + 
"(b('bulk') <= 107.0) ? " + 
"-0.016555360429987648" + 
":  " + 
"-0.0008217893203131022" + 
":  " + 
"(b('L8b7med') <= 1852.75) ? " + 
"0.0015861754650405213" + 
":  " + 
"0.014572607320705432" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"-0.006872396085929974" + 
":  " + 
"(b('L8b3med') <= 555.5) ? " + 
"(b('gvvk2') <= 0.1796317920088768) ? " + 
"0.004614644155287673" + 
":  " + 
"0.012879802127120477" + 
":  " + 
"(b('L8b3med') <= 616.25) ? " + 
"-0.0027806808337071725" + 
":  " + 
"0.0001178183228910411" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1607.75) ? " + 
"(b('ndvi_med') <= 3582.0) ? " + 
"(b('L8b2med') <= 418.5) ? " + 
"-0.0005810801104804352" + 
":  " + 
"0.0066727979577856185" + 
":  " + 
"(b('L8b1med') <= 360.5) ? " + 
"-0.00014158960601335738" + 
":  " + 
"-0.008337638805146316" + 
":  " + 
"(b('L8b3med') <= 814.0) ? " + 
"(b('lat') <= 44.23267364501953) ? " + 
"-0.009723705206668331" + 
":  " + 
"0.00037865820102546275" + 
":  " + 
"(b('ndvi_med') <= 3530.0) ? " + 
"-0.00020984051071968742" + 
":  " + 
"0.0034571590706191386" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('ndvi_med') <= 5217.0) ? " + 
"(b('bulk') <= 162.5) ? " + 
"-0.0003629599374600614" + 
":  " + 
"-0.011720791519076674" + 
":  " + 
"-0.019402294800253378" + 
":  " + 
"(b('svvk3') <= -0.02579908538609743) ? " + 
"(b('L8b7med') <= 1937.5) ? " + 
"0.007101123454401337" + 
":  " + 
"0.013065253830713663" + 
":  " + 
"(b('L8b1med') <= 540.5) ? " + 
"0.000585800799658532" + 
":  " + 
"-0.0007560473640093431" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 6132.5) ? " + 
"(b('ndvi_med') <= 5941.25) ? " + 
"(b('ndvi_med') <= 5916.25) ? " + 
"3.463194767922936e-05" + 
":  " + 
"-0.008116957546226008" + 
":  " + 
"(b('ndvi_med') <= 6002.25) ? " + 
"0.018964301416957763" + 
":  " + 
"0.004279000353934387" + 
":  " + 
"(b('clay') <= 13.5) ? " + 
"(b('L8b1med') <= 464.5) ? " + 
"-0.0026708316853752967" + 
":  " + 
"-0.005084035149116206" + 
":  " + 
"-0.009477133409424077" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 19.810494422912598) ? " + 
"(b('trees') <= 17.942265510559082) ? " + 
"-9.295331901783608e-05" + 
":  " + 
"0.004036969909951687" + 
":  " + 
"(b('L8b2med') <= 467.5) ? " + 
"-0.00622414119180413" + 
":  " + 
"0.0018272539236950103" + 
":  " + 
"(b('trees') <= 43.34158134460449) ? " + 
"0.011300327320165338" + 
":  " + 
"(b('L8b1med') <= 346.75) ? " + 
"0.00015356583059339401" + 
":  " + 
"0.005488911913588246" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 0.03652967885136604) ? " + 
"(b('svvk3') <= 0.014892799779772758) ? " + 
"(b('svvk3') <= 0.008779367431998253) ? " + 
"0.0003661168658668127" + 
":  " + 
"0.008195236456350919" + 
":  " + 
"(b('svvk3') <= 0.02459165919572115) ? " + 
"-0.007459208417026103" + 
":  " + 
"0.0012056955580001898" + 
":  " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"(b('trees') <= 3.5388137102127075) ? " + 
"-0.0022104732644765888" + 
":  " + 
"-0.0211887958567671" + 
":  " + 
"(b('trees') <= 5.9133620262146) ? " + 
"0.005337850282861038" + 
":  " + 
"-0.00026857279572692957" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1765.5) ? " + 
"(b('L8b7med') <= 1747.25) ? " + 
"(b('L8b6med') <= 2857.25) ? " + 
"-0.00046206257930078346" + 
":  " + 
"0.005593466903300409" + 
":  " + 
"(b('svvk3') <= 0.041771077550947666) ? " + 
"0.008616520803749908" + 
":  " + 
"0.03264364819918672" + 
":  " + 
"(b('L8b2med') <= 513.75) ? " + 
"(b('L8b2med') <= 502.5) ? " + 
"-0.002491479621601393" + 
":  " + 
"-0.020977827998905907" + 
":  " + 
"(b('gvvk2') <= 0.31293176114559174) ? " + 
"-0.0014715377649775021" + 
":  " + 
"0.000999316092134635" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('L8b1med') <= 533.5) ? " + 
"(b('L8b3med') <= 957.5) ? " + 
"-0.00146889053593725" + 
":  " + 
"-0.013391718502910864" + 
":  " + 
"(b('clay') <= 20.5) ? " + 
"-0.0005039808922216806" + 
":  " + 
"0.011684647743267157" + 
":  " + 
"(b('svvk3') <= -0.0181471798568964) ? " + 
"(b('ndvi_med') <= 4896.0) ? " + 
"0.011084261552649743" + 
":  " + 
"-0.007753627285031817" + 
":  " + 
"(b('L8b7med') <= 2573.5) ? " + 
"0.0003771558405665127" + 
":  " + 
"-0.0014325431516349473" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 617.75) ? " + 
"(b('L8b2med') <= 777.75) ? " + 
"-0.00011537284211883989" + 
":  " + 
"0.004125478359247793" + 
":  " + 
"(b('svvk3') <= -0.005527108063688502) ? " + 
"-0.02013582435070317" + 
":  " + 
"-0.003718229902644285" + 
":  " + 
"(b('ndvi_med') <= 1658.5) ? " + 
"(b('L8b2med') <= 867.875) ? " + 
"0.005634093121236431" + 
":  " + 
"-0.0010513034576399474" + 
":  " + 
"(b('ndvi_med') <= 1670.5) ? " + 
"0.03142872070464503" + 
":  " + 
"0.0038977005738938" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('lon') <= 146.01818084716797) ? " + 
"(b('trees') <= 4.824380278587341) ? " + 
"0.010749282163925122" + 
":  " + 
"0.007728612492250722" + 
":  " + 
"(b('bulk') <= 147.5) ? " + 
"0.0013999278788461623" + 
":  " + 
"-0.0012827548568327338" + 
":  " + 
"(b('lon') <= 22.88466453552246) ? " + 
"(b('lon') <= 22.87806510925293) ? " + 
"4.192414878634122e-06" + 
":  " + 
"0.004705362151123421" + 
":  " + 
"(b('lon') <= 22.9342041015625) ? " + 
"-0.01549085291570753" + 
":  " + 
"-0.001818555610248574" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 168.5) ? " + 
"(b('trees') <= 0.03652967885136604) ? " + 
"0.0005413912009561071" + 
":  " + 
"-0.00047673225269806343" + 
":  " + 
"(b('L8b6med') <= 3915.0) ? " + 
"0.0027809529135835315" + 
":  " + 
"0.01248636986875204" + 
":  " + 
"-0.009242720504062815" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1607.75) ? " + 
"(b('gvvk2') <= 0.42163337767124176) ? " + 
"(b('ndvi_med') <= 3594.5) ? " + 
"0.003341207495725936" + 
":  " + 
"-0.0014984359140178293" + 
":  " + 
"(b('clay') <= 21.0) ? " + 
"-0.00011838759544260549" + 
":  " + 
"-0.011035621620799482" + 
":  " + 
"(b('L8b3med') <= 807.5) ? " + 
"(b('svvk3') <= 0.0017463365802541375) ? " + 
"0.0022620644754767307" + 
":  " + 
"-0.006375580060978657" + 
":  " + 
"(b('lat') <= 55.92889976501465) ? " + 
"0.00036981933772344065" + 
":  " + 
"-0.006906837735881807" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3782.0) ? " + 
"(b('ndvi_med') <= 3733.5) ? " + 
"(b('ndvi_med') <= 3698.5) ? " + 
"-0.00020667068294557308" + 
":  " + 
"0.010367202550341644" + 
":  " + 
"(b('L8b6med') <= 2735.5) ? " + 
"-0.0018020673357961453" + 
":  " + 
"-0.017840019490413403" + 
":  " + 
"(b('bulk') <= 110.0) ? " + 
"(b('svvk3') <= 0.010467188665643334) ? " + 
"-0.007764783710997052" + 
":  " + 
"0.006300208356273207" + 
":  " + 
"(b('trees') <= 9.170684337615967) ? " + 
"-0.0003276547156304055" + 
":  " + 
"0.003662524705003886" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 253.5) ? " + 
"(b('L8b2med') <= 305.5) ? " + 
"(b('gvvk2') <= 0.39189615845680237) ? " + 
"0.007458224944945978" + 
":  " + 
"-0.004435813323657879" + 
":  " + 
"(b('ndvi_med') <= 4581.5) ? " + 
"-0.006631529054135081" + 
":  " + 
"0.0015151609121981102" + 
":  " + 
"(b('L8b2med') <= 331.5) ? " + 
"(b('svvk3') <= 0.006145023740828037) ? " + 
"0.00987978869773827" + 
":  " + 
"0.0018662873140156688" + 
":  " + 
"(b('L8b6med') <= 2201.75) ? " + 
"0.0022698841609222957" + 
":  " + 
"-9.501332086941327e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('ndvi_med') <= 5217.0) ? " + 
"(b('svvk3') <= -0.023769686929881573) ? " + 
"-0.00021261892417068174" + 
":  " + 
"-0.007634793481693627" + 
":  " + 
"-0.016717098190907137" + 
":  " + 
"(b('svvk3') <= -0.0181471798568964) ? " + 
"(b('ndvi_med') <= 4896.0) ? " + 
"0.009849853057491798" + 
":  " + 
"-0.007126380835546509" + 
":  " + 
"(b('L8b1med') <= 459.5) ? " + 
"0.0008020734178059711" + 
":  " + 
"-0.0006179237256896269" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.546385049819946) ? " + 
"(b('lon') <= -82.97315216064453) ? " + 
"(b('lon') <= -83.91805267333984) ? " + 
"3.822727300780347e-05" + 
":  " + 
"-0.016348383613504727" + 
":  " + 
"(b('trees') <= 8.635247230529785) ? " + 
"0.012996699826563433" + 
":  " + 
"-0.00017207718796794137" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"(b('gvvk2') <= 0.5816158354282379) ? " + 
"-0.009299611002454496" + 
":  " + 
"0.013578952178489867" + 
":  " + 
"(b('lat') <= 43.73078536987305) ? " + 
"0.003916818172329305" + 
":  " + 
"-0.001074430341210118" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3782.0) ? " + 
"(b('ndvi_med') <= 3733.5) ? " + 
"(b('ndvi_med') <= 3698.5) ? " + 
"-0.00018994167343378023" + 
":  " + 
"0.009039609471827312" + 
":  " + 
"(b('L8b6med') <= 2735.5) ? " + 
"-0.0017590013325896742" + 
":  " + 
"-0.016130546278366506" + 
":  " + 
"(b('bulk') <= 110.0) ? " + 
"(b('svvk3') <= 0.010467188665643334) ? " + 
"-0.006977349834134041" + 
":  " + 
"0.005706924545073266" + 
":  " + 
"(b('L8b7med') <= 1668.25) ? " + 
"-2.0665131898162103e-05" + 
":  " + 
"0.0038316797564867835" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"(b('L8b2med') <= 782.5) ? " + 
"-6.217196373186859e-05" + 
":  " + 
"0.006351198178094521" + 
":  " + 
"(b('svvk3') <= -0.008416643599048257) ? " + 
"-0.01830057954296168" + 
":  " + 
"-0.0031136159363231676" + 
":  " + 
"(b('L8b1med') <= 698.25) ? " + 
"(b('lon') <= -54.86498475074768) ? " + 
"0.009714463313995865" + 
":  " + 
"-0.0029932618869108482" + 
":  " + 
"(b('svvk3') <= 0.017151779495179653) ? " + 
"0.0017029805649434859" + 
":  " + 
"-0.004451272122968232" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('gvvk2') <= 0.4162828177213669) ? " + 
"6.194099774086754e-05" + 
":  " + 
"-0.004484210006164443" + 
":  " + 
"-0.035003156818692455" + 
":  " + 
"(b('gvvk2') <= 0.46257317066192627) ? " + 
"(b('L8b6med') <= 2676.5) ? " + 
"0.0019322402292144616" + 
":  " + 
"0.016980348919277084" + 
":  " + 
"(b('trees') <= 6.110170364379883) ? " + 
"0.0016168028600834258" + 
":  " + 
"-0.0030028232475935944" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('lat') <= 50.68670654296875) ? " + 
"-0.007312320951096796" + 
":  " + 
"-0.0059178208226338125" + 
":  " + 
"(b('sand') <= 74.5) ? " + 
"(b('sand') <= 73.0) ? " + 
"-2.7861456147395565e-05" + 
":  " + 
"-0.013933510753539297" + 
":  " + 
"(b('L8b6med') <= 2859.5) ? " + 
"0.002624583563149157" + 
":  " + 
"-0.0017194641934341586" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 253.5) ? " + 
"(b('L8b2med') <= 305.5) ? " + 
"(b('gvvk2') <= 0.39189615845680237) ? " + 
"0.006667384166987894" + 
":  " + 
"-0.004301176662730305" + 
":  " + 
"(b('ndvi_med') <= 3172.0) ? " + 
"-0.007073626291429094" + 
":  " + 
"-0.0020356861551553604" + 
":  " + 
"(b('L8b7med') <= 1607.75) ? " + 
"(b('ndvi_med') <= 3582.0) ? " + 
"0.0028851301773385107" + 
":  " + 
"-0.001460693502973088" + 
":  " + 
"(b('L8b3med') <= 807.5) ? " + 
"-0.002710287422856809" + 
":  " + 
"0.00021606489341900433" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3782.0) ? " + 
"(b('ndvi_med') <= 3762.25) ? " + 
"(b('trees') <= 1.3649256229400635) ? " + 
"0.0004561339575366687" + 
":  " + 
"-0.0008862986050081768" + 
":  " + 
"-0.015630395937554886" + 
":  " + 
"(b('trees') <= 10.084112167358398) ? " + 
"(b('gvvk2') <= 0.24560555070638657) ? " + 
"-0.006758193839193766" + 
":  " + 
"-0.00014384044333550227" + 
":  " + 
"(b('trees') <= 18.595163345336914) ? " + 
"0.006423961020645646" + 
":  " + 
"-0.0011033675088031594" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('trees') <= 21.869441986083984) ? " + 
"(b('L8b3med') <= 747.0) ? " + 
"0.005968082016272747" + 
":  " + 
"-0.0021351587336719763" + 
":  " + 
"(b('L8b1med') <= 339.5) ? " + 
"-0.007705154983713075" + 
":  " + 
"-0.014865194024525519" + 
":  " + 
"(b('L8b1med') <= 540.5) ? " + 
"(b('L8b1med') <= 507.5) ? " + 
"-4.533392451890299e-05" + 
":  " + 
"0.005686244391585915" + 
":  " + 
"(b('L8b1med') <= 549.5) ? " + 
"-0.011287073082592731" + 
":  " + 
"-0.00010904751964583582" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('L8b3med') <= 836.5) ? " + 
"(b('L8b7med') <= 1741.25) ? " + 
"-0.004877828687602684" + 
":  " + 
"-0.018870819715531423" + 
":  " + 
"(b('L8b1med') <= 424.75) ? " + 
"0.012734288676621519" + 
":  " + 
"-0.0016750498765789894" + 
":  " + 
"(b('trees') <= 17.942265510559082) ? " + 
"(b('trees') <= 15.230875015258789) ? " + 
"2.391895439339229e-05" + 
":  " + 
"-0.00480179252020643" + 
":  " + 
"(b('trees') <= 19.810494422912598) ? " + 
"0.00634472558944782" + 
":  " + 
"-0.000946346829633452" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3782.0) ? " + 
"(b('ndvi_med') <= 3733.5) ? " + 
"(b('ndvi_med') <= 3698.5) ? " + 
"-0.00019173950315029198" + 
":  " + 
"0.008613344027578731" + 
":  " + 
"(b('L8b6med') <= 2735.5) ? " + 
"-0.0011902130370394642" + 
":  " + 
"-0.013478157137883834" + 
":  " + 
"(b('bulk') <= 110.0) ? " + 
"(b('svvk3') <= 0.010467188665643334) ? " + 
"-0.006196435685368651" + 
":  " + 
"0.005056217291666859" + 
":  " + 
"(b('L8b7med') <= 1668.25) ? " + 
"-3.294042866764496e-05" + 
":  " + 
"0.003544143735793071" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('L8b1med') <= 518.25) ? " + 
"(b('L8b3med') <= 754.0) ? " + 
"0.001802029494254287" + 
":  " + 
"-0.0059011105234717046" + 
":  " + 
"(b('clay') <= 20.5) ? " + 
"-0.0008605629196475686" + 
":  " + 
"0.007410504454093903" + 
":  " + 
"(b('svvk3') <= -0.0181471798568964) ? " + 
"(b('lon') <= -100.87807083129883) ? " + 
"0.01985095355339861" + 
":  " + 
"0.0036589153942532316" + 
":  " + 
"(b('L8b1med') <= 459.5) ? " + 
"0.0007836410411239328" + 
":  " + 
"-0.0005856942713528701" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.510674953460693) ? " + 
"(b('lon') <= -82.97315216064453) ? " + 
"(b('lon') <= -83.91805267333984) ? " + 
"3.4747689732761456e-05" + 
":  " + 
"-0.014528528915956206" + 
":  " + 
"(b('trees') <= 8.635247230529785) ? " + 
"0.01044998394700485" + 
":  " + 
"0.000259103475608365" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"(b('gvvk2') <= 0.5816158354282379) ? " + 
"-0.008871750867573736" + 
":  " + 
"0.010868064767519114" + 
":  " + 
"(b('lat') <= 43.73078536987305) ? " + 
"0.003425841547309775" + 
":  " + 
"-0.0009998520603810412" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2802.5) ? " + 
"(b('L8b7med') <= 2637.0) ? " + 
"(b('L8b7med') <= 2616.25) ? " + 
"3.2419984819997594e-05" + 
":  " + 
"0.007909729761437976" + 
":  " + 
"(b('L8b1med') <= 694.5) ? " + 
"-0.010240607879500027" + 
":  " + 
"-0.0013975127254430147" + 
":  " + 
"(b('lat') <= 41.369455337524414) ? " + 
"(b('ndvi_med') <= 1362.0) ? " + 
"-9.28604343856565e-05" + 
":  " + 
"0.005582243705967518" + 
":  " + 
"(b('gvvk2') <= 0.4553770124912262) ? " + 
"-0.00844680602276864" + 
":  " + 
"-0.0024084915287150063" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 9.210049629211426) ? " + 
"(b('sand') <= 39.5) ? " + 
"(b('L8b3med') <= 750.5) ? " + 
"0.006623822339170042" + 
":  " + 
"0.0004479633300336015" + 
":  " + 
"(b('ndvi_med') <= 3678.75) ? " + 
"-0.0008449253910204057" + 
":  " + 
"0.0023025241344668025" + 
":  " + 
"(b('trees') <= 11.076036930084229) ? " + 
"(b('trees') <= 8.889909744262695) ? " + 
"-0.0011489585232690495" + 
":  " + 
"0.0058084660284932615" + 
":  " + 
"(b('gvvk2') <= 0.2873397469520569) ? " + 
"-0.009450063999142853" + 
":  " + 
"0.001276289082321794" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"(b('ndvi_med') <= 1600.0) ? " + 
"0.0021226666516175794" + 
":  " + 
"-0.0002625433453365053" + 
":  " + 
"(b('svvk3') <= -0.008416643599048257) ? " + 
"-0.016033020721960944" + 
":  " + 
"-0.0027546009220890473" + 
":  " + 
"(b('L8b1med') <= 698.25) ? " + 
"(b('lon') <= -109.15076446533203) ? " + 
"0.010673790168998472" + 
":  " + 
"-0.00018976581488521044" + 
":  " + 
"(b('svvk3') <= 0.017151779495179653) ? " + 
"0.0015507638686991464" + 
":  " + 
"-0.004026030531700915" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('trees') <= 21.869441986083984) ? " + 
"(b('lat') <= 38.4822998046875) ? " + 
"-0.0046176075522349645" + 
":  " + 
"0.0003656086557399287" + 
":  " + 
"(b('L8b6med') <= 2197.5) ? " + 
"-0.007988797025918648" + 
":  " + 
"-0.01328149368529763" + 
":  " + 
"(b('svvk3') <= -0.0181471798568964) ? " + 
"(b('L8b7med') <= 1531.0) ? " + 
"-0.00641570215378981" + 
":  " + 
"0.008031896590098514" + 
":  " + 
"(b('L8b1med') <= 459.5) ? " + 
"0.0007046575872701306" + 
":  " + 
"-0.0005003892818720217" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 923.5) ? " + 
"(b('L8b3med') <= 899.25) ? " + 
"(b('L8b6med') <= 2871.5) ? " + 
"-0.0007647591938758109" + 
":  " + 
"0.0022945038091436647" + 
":  " + 
"(b('L8b3med') <= 909.0) ? " + 
"-0.012951245376771836" + 
":  " + 
"-0.0016030772122638316" + 
":  " + 
"(b('L8b6med') <= 2678.5) ? " + 
"(b('L8b3med') <= 948.0) ? " + 
"0.02293672900110143" + 
":  " + 
"0.0011379623505829001" + 
":  " + 
"(b('L8b2med') <= 537.0) ? " + 
"-0.009878236184448488" + 
":  " + 
"0.0001857356066416356" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -120.78556060791016) ? " + 
"(b('L8b7med') <= 1772.0) ? " + 
"(b('L8b3med') <= 949.0) ? " + 
"0.018811625430152634" + 
":  " + 
"-0.005469717441672406" + 
":  " + 
"(b('L8b7med') <= 2401.25) ? " + 
"-0.0054220714675107" + 
":  " + 
"0.0017423969849535484" + 
":  " + 
"(b('lon') <= -120.78532028198242) ? " + 
"(b('lat') <= 38.14932060241699) ? " + 
"0.0069616360452111475" + 
":  " + 
"0.03137650467146669" + 
":  " + 
"(b('lon') <= -120.6328010559082) ? " + 
"-0.01438695109541386" + 
":  " + 
"6.879860059090157e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('lat') <= 50.68670654296875) ? " + 
"-0.007661626271347033" + 
":  " + 
"-0.0047919627448426705" + 
":  " + 
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"-7.954356199660219e-05" + 
":  " + 
"-0.03135240302868411" + 
":  " + 
"(b('gvvk2') <= 0.46257317066192627) ? " + 
"0.008347288748543548" + 
":  " + 
"5.929403047534272e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('L8b3med') <= 836.5) ? " + 
"(b('svvk3') <= -6.796767240757617e-05) ? " + 
"-0.016560503082229387" + 
":  " + 
"-0.004923527458574509" + 
":  " + 
"(b('L8b6med') <= 2978.25) ? " + 
"0.0037186721709603215" + 
":  " + 
"-0.0029853207140046975" + 
":  " + 
"(b('sand') <= 14.5) ? " + 
"(b('L8b3med') <= 789.0) ? " + 
"0.0017129677431598767" + 
":  " + 
"0.01585348365454392" + 
":  " + 
"(b('sand') <= 19.0) ? " + 
"-0.005993932628295768" + 
":  " + 
"0.00013972605528886375" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"(b('lat') <= 42.43240165710449) ? " + 
"-0.00012571297253875837" + 
":  " + 
"0.005343908270969444" + 
":  " + 
"0.03191083150766888" + 
":  " + 
"(b('lat') <= 43.663949966430664) ? " + 
"-0.01564890112615657" + 
":  " + 
"(b('L8b1med') <= 540.5) ? " + 
"0.0003091592009166986" + 
":  " + 
"-0.003225533270613982" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b3med') <= 1252.5) ? " + 
"(b('L8b3med') <= 1234.5) ? " + 
"-0.00014518958579153114" + 
":  " + 
"0.011561223664630735" + 
":  " + 
"(b('gvvk2') <= 0.49583008885383606) ? " + 
"-0.00912702316657754" + 
":  " + 
"0.00879316619094389" + 
":  " + 
"(b('ndvi_med') <= 1658.5) ? " + 
"(b('svvk3') <= 0.018095525912940502) ? " + 
"0.0013887521169526325" + 
":  " + 
"-0.0023095283484421253" + 
":  " + 
"(b('ndvi_med') <= 1670.5) ? " + 
"0.02731287785254763" + 
":  " + 
"0.0034869965315129205" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('ndvi_med') <= 4452.5) ? " + 
"(b('ndvi_med') <= 3765.75) ? " + 
"-0.001950809823452798" + 
":  " + 
"0.0033729106945307266" + 
":  " + 
"(b('L8b6med') <= 2378.5) ? " + 
"0.00040781982328860766" + 
":  " + 
"-0.012626950356655398" + 
":  " + 
"(b('lon') <= -5.546385049819946) ? " + 
"(b('lon') <= -77.86024856567383) ? " + 
"0.00017180140384111356" + 
":  " + 
"0.006808384303307186" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"-0.006958459145446781" + 
":  " + 
"-6.299718388100009e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.007927745580673218) ? " + 
"(b('svvk3') <= 0.007316778646782041) ? " + 
"(b('L8b7med') <= 1765.5) ? " + 
"0.0007679845059512471" + 
":  " + 
"-0.0010361708260370138" + 
":  " + 
"(b('L8b3med') <= 822.75) ? " + 
"-0.016699243100662203" + 
":  " + 
"-0.001799542648137531" + 
":  " + 
"(b('svvk3') <= 0.008157914970070124) ? " + 
"(b('bulk') <= 133.5) ? " + 
"0.009086456426748935" + 
":  " + 
"0.01679751944989835" + 
":  " + 
"(b('L8b2med') <= 1064.5) ? " + 
"9.593959856937594e-05" + 
":  " + 
"0.0056894640253450784" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1242.0) ? " + 
"(b('svvk3') <= -0.0003122568215303545) ? " + 
"(b('bulk') <= 95.5) ? " + 
"-0.007683470092179567" + 
":  " + 
"-0.0067381549286640585" + 
":  " + 
"(b('sand') <= 78.5) ? " + 
"-0.0020650698614460006" + 
":  " + 
"0.006352722687768375" + 
":  " + 
"(b('L8b7med') <= 1355.0) ? " + 
"(b('L8b7med') <= 1349.0) ? " + 
"0.0019405195083597021" + 
":  " + 
"0.017755679977252525" + 
":  " + 
"(b('L8b7med') <= 1399.25) ? " + 
"-0.004524642789808466" + 
":  " + 
"6.527965432660208e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 923.5) ? " + 
"(b('L8b1med') <= 524.75) ? " + 
"(b('L8b1med') <= 507.5) ? " + 
"-0.00045035198105218267" + 
":  " + 
"0.012928843308174499" + 
":  " + 
"(b('gvvk2') <= 0.43681253492832184) ? " + 
"-0.008150163437887319" + 
":  " + 
"0.001562401066606589" + 
":  " + 
"(b('L8b3med') <= 932.5) ? " + 
"(b('L8b6med') <= 2836.5) ? " + 
"0.021974447845258094" + 
":  " + 
"0.0002632313727890162" + 
":  " + 
"(b('svvk3') <= 0.004657700890675187) ? " + 
"-0.0011209773282094126" + 
":  " + 
"0.0011828677724285393" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2802.5) ? " + 
"(b('L8b7med') <= 2786.5) ? " + 
"(b('L8b7med') <= 2637.0) ? " + 
"0.0001188240213043816" + 
":  " + 
"-0.003447110026599885" + 
":  " + 
"(b('clay') <= 22.0) ? " + 
"-0.011796833070113408" + 
":  " + 
"-0.019660916503509707" + 
":  " + 
"(b('L8b7med') <= 2935.5) ? " + 
"(b('bulk') <= 153.5) ? " + 
"0.010203622214993822" + 
":  " + 
"-0.00433048094025441" + 
":  " + 
"(b('L8b3med') <= 1340.5) ? " + 
"0.005579659604954983" + 
":  " + 
"-0.001225698026085369" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 22.880224227905273) ? " + 
"(b('lon') <= 22.87806510925293) ? " + 
"(b('lon') <= 9.25374984741211) ? " + 
"0.00016544621166158382" + 
":  " + 
"-0.0035375438728046976" + 
":  " + 
"(b('gvvk2') <= 0.1796317920088768) ? " + 
"0.0015861664530826824" + 
":  " + 
"0.009394207459585358" + 
":  " + 
"(b('L8b7med') <= 1418.5) ? " + 
"(b('L8b1med') <= 313.5) ? " + 
"-0.017535012145370094" + 
":  " + 
"-0.00835719202596176" + 
":  " + 
"(b('gvvk2') <= 0.41425721347332) ? " + 
"-0.0013102805075083694" + 
":  " + 
"0.004752265260585871" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"(b('L8b2med') <= 777.75) ? " + 
"-9.393036221893702e-05" + 
":  " + 
"0.003733486778263915" + 
":  " + 
"(b('sand') <= 29.5) ? " + 
"0.011734391642759384" + 
":  " + 
"-0.004061004039704565" + 
":  " + 
"(b('ndvi_med') <= 1658.5) ? " + 
"(b('clay') <= 11.5) ? " + 
"-0.010125296907354028" + 
":  " + 
"0.00016786336643095736" + 
":  " + 
"(b('ndvi_med') <= 1670.5) ? " + 
"0.024401574201079745" + 
":  " + 
"0.0033141843859994576" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('trees') <= 21.869441986083984) ? " + 
"(b('L8b3med') <= 747.0) ? " + 
"0.004671679096379701" + 
":  " + 
"-0.0017924105017702396" + 
":  " + 
"(b('gvvk2') <= 0.41087158024311066) ? " + 
"-0.006324637239192937" + 
":  " + 
"-0.011147062631149424" + 
":  " + 
"(b('lon') <= -5.546385049819946) ? " + 
"(b('lon') <= -82.97315216064453) ? " + 
"9.518178453626802e-05" + 
":  " + 
"0.004964346011210332" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"-0.0062382434359529735" + 
":  " + 
"-5.100494604704354e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 101.0) ? " + 
"(b('L8b1med') <= 457.5) ? " + 
"(b('trees') <= 9.591548919677734) ? " + 
"-0.007385556473052168" + 
":  " + 
"-0.0046097433286679396" + 
":  " + 
"-0.00020498606633384542" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"(b('ndvi_med') <= 2114.0) ? " + 
"-0.0018500975478822623" + 
":  " + 
"0.014629129214397185" + 
":  " + 
"(b('ndvi_med') <= 4786.75) ? " + 
"-9.506431146052867e-05" + 
":  " + 
"0.0018554948211559404" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.5458730161190033) ? " + 
"(b('gvvk2') <= 0.5375914573669434) ? " + 
"(b('trees') <= 9.420434951782227) ? " + 
"-0.000404553375734414" + 
":  " + 
"0.000761637941488775" + 
":  " + 
"-0.010442087050650993" + 
":  " + 
"(b('lon') <= -103.03784942626953) ? " + 
"(b('ndvi_med') <= 3367.5) ? " + 
"0.01792291835883819" + 
":  " + 
"-0.00016636289418944794" + 
":  " + 
"(b('sand') <= 76.5) ? " + 
"-0.001026358070312212" + 
":  " + 
"0.003004729404400506" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 923.5) ? " + 
"(b('L8b2med') <= 542.5) ? " + 
"(b('L8b6med') <= 2871.5) ? " + 
"-0.0004005906420312644" + 
":  " + 
"0.005204326568384314" + 
":  " + 
"(b('trees') <= 16.565014839172363) ? " + 
"-0.003596525017163831" + 
":  " + 
"0.003182132700811566" + 
":  " + 
"(b('L8b6med') <= 2678.5) ? " + 
"(b('L8b3med') <= 948.0) ? " + 
"0.01860274819155876" + 
":  " + 
"0.001056924664257991" + 
":  " + 
"(b('lat') <= 45.85858917236328) ? " + 
"-0.00037789748043631126" + 
":  " + 
"0.002971394473133513" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 507.5) ? " + 
"(b('L8b1med') <= 499.25) ? " + 
"(b('L8b7med') <= 2535.5) ? " + 
"-4.498825519950569e-05" + 
":  " + 
"0.015082916583772435" + 
":  " + 
"(b('lat') <= 42.05848503112793) ? " + 
"-0.0029110312833083543" + 
":  " + 
"-0.01801370546772532" + 
":  " + 
"(b('L8b1med') <= 527.25) ? " + 
"(b('L8b3med') <= 934.5) ? " + 
"0.014022909252112078" + 
":  " + 
"0.0004232883569019115" + 
":  " + 
"(b('clay') <= 22.5) ? " + 
"0.0010030005087381104" + 
":  " + 
"-0.002396262753239376" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2802.5) ? " + 
"(b('L8b7med') <= 2786.5) ? " + 
"(b('L8b7med') <= 2637.0) ? " + 
"8.365129323928283e-05" + 
":  " + 
"-0.003012286873542788" + 
":  " + 
"(b('bulk') <= 147.5) ? " + 
"-0.01065792876041731" + 
":  " + 
"-0.017410296197334543" + 
":  " + 
"(b('lat') <= 41.369455337524414) ? " + 
"(b('lat') <= 36.14150428771973) ? " + 
"-0.000415641708939927" + 
":  " + 
"0.0044271932513082896" + 
":  " + 
"(b('gvvk2') <= 0.4553770124912262) ? " + 
"-0.006442576152235653" + 
":  " + 
"-0.001274869190229658" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 2473.0) ? " + 
"(b('L8b3med') <= 650.0) ? " + 
"(b('L8b2med') <= 346.0) ? " + 
"-0.006570352727774342" + 
":  " + 
"-0.015985722976455646" + 
":  " + 
"(b('L8b1med') <= 467.0) ? " + 
"0.0028674012354155845" + 
":  " + 
"-7.926071904889718e-06" + 
":  " + 
"(b('ndvi_med') <= 2723.0) ? " + 
"(b('sand') <= 47.0) ? " + 
"-0.0021843242238800582" + 
":  " + 
"-0.012474895896864896" + 
":  " + 
"(b('L8b7med') <= 2044.0) ? " + 
"0.0008297177691992608" + 
":  " + 
"-0.0029999947923131185" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 881.5) ? " + 
"(b('L8b2med') <= 663.5) ? " + 
"(b('L8b2med') <= 638.0) ? " + 
"-0.0004345059560353116" + 
":  " + 
"-0.013088227569168494" + 
":  " + 
"0.020838927145361175" + 
":  " + 
"(b('L8b3med') <= 887.0) ? " + 
"(b('trees') <= 15.598985195159912) ? " + 
"0.00702932296684608" + 
":  " + 
"0.02522366461083636" + 
":  " + 
"(b('lat') <= 46.01203918457031) ? " + 
"-0.00019128395065689141" + 
":  " + 
"0.002793037591593208" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"(b('svvk3') <= -0.005489814328029752) ? " + 
"-0.002353595868922488" + 
":  " + 
"0.0007727708491832972" + 
":  " + 
"0.024631636006227586" + 
":  " + 
"(b('lat') <= 43.663949966430664) ? " + 
"-0.013602984448458203" + 
":  " + 
"(b('bulk') <= 147.5) ? " + 
"-0.0002404800641152972" + 
":  " + 
"-0.016973753159984728" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 9.210049629211426) ? " + 
"(b('lat') <= 32.18929862976074) ? " + 
"(b('sand') <= 41.0) ? " + 
"-0.012467907142072993" + 
":  " + 
"-0.00316242257928871" + 
":  " + 
"(b('lon') <= 9.089200019836426) ? " + 
"0.00011570269959268908" + 
":  " + 
"0.002555059685326554" + 
":  " + 
"(b('svvk3') <= 0.013326384127140045) ? " + 
"(b('lon') <= 9.281400203704834) ? " + 
"-0.0196136998654928" + 
":  " + 
"-0.001649742240695353" + 
":  " + 
"(b('gvvk2') <= 0.3749391883611679) ? " + 
"0.003850876931415347" + 
":  " + 
"-0.0017408967074338609" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"(b('lat') <= 42.43240165710449) ? " + 
"-2.2260061156679347e-05" + 
":  " + 
"0.004220989178444258" + 
":  " + 
"0.02215690213564553" + 
":  " + 
"(b('lat') <= 43.663949966430664) ? " + 
"-0.01225425627357165" + 
":  " + 
"(b('L8b1med') <= 540.5) ? " + 
"0.00020866903883404804" + 
":  " + 
"-0.002821142254207411" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"(b('ndvi_med') <= 1600.0) ? " + 
"0.0016172463707469487" + 
":  " + 
"-0.0002517462943067408" + 
":  " + 
"(b('svvk3') <= -0.008416643599048257) ? " + 
"-0.01245771568021213" + 
":  " + 
"-0.0018091963345800287" + 
":  " + 
"(b('L8b1med') <= 698.25) ? " + 
"(b('lon') <= -54.86498475074768) ? " + 
"0.007564174524598288" + 
":  " + 
"-0.001291665584002973" + 
":  " + 
"(b('svvk3') <= 0.017151779495179653) ? " + 
"0.0012042127715950115" + 
":  " + 
"-0.003423876937879767" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 168.5) ? " + 
"(b('lon') <= -121.0405044555664) ? " + 
"-0.002893235190520586" + 
":  " + 
"6.69182987607979e-05" + 
":  " + 
"(b('ndvi_med') <= 1281.5) ? " + 
"0.002642762375461752" + 
":  " + 
"0.010240663329418115" + 
":  " + 
"-0.007892076412233343" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"(b('svvk3') <= 0.002330337418243289) ? " + 
"-0.0017341572454802542" + 
":  " + 
"-0.00923622102838402" + 
":  " + 
"(b('ndvi_med') <= 734.25) ? " + 
"(b('sand') <= 56.5) ? " + 
"0.00018785276941562143" + 
":  " + 
"0.008875884812630097" + 
":  " + 
"(b('L8b1med') <= 1059.75) ? " + 
"5.488157798374934e-05" + 
":  " + 
"-0.0029110904767591485" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1312.0) ? " + 
"(b('L8b3med') <= 1252.5) ? " + 
"(b('L8b3med') <= 1235.5) ? " + 
"-2.8685397082219337e-05" + 
":  " + 
"0.009556469083905436" + 
":  " + 
"(b('L8b7med') <= 2543.75) ? " + 
"-0.0022526453132271362" + 
":  " + 
"-0.009692206536591936" + 
":  " + 
"(b('L8b3med') <= 1330.0) ? " + 
"(b('L8b1med') <= 759.0) ? " + 
"0.008414873804860716" + 
":  " + 
"0.021731683327743806" + 
":  " + 
"(b('clay') <= 11.5) ? " + 
"-0.009106762226370434" + 
":  " + 
"0.00036832612889567856" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 22.880224227905273) ? " + 
"(b('lon') <= 22.87806510925293) ? " + 
"(b('lon') <= 9.25374984741211) ? " + 
"0.00015117370216938245" + 
":  " + 
"-0.003008559655137732" + 
":  " + 
"(b('gvvk2') <= 0.1796317920088768) ? " + 
"0.00167269519446539" + 
":  " + 
"0.007948830236027521" + 
":  " + 
"(b('L8b7med') <= 1418.5) ? " + 
"(b('L8b7med') <= 1392.5) ? " + 
"-0.015652984675864484" + 
":  " + 
"-0.007392946568396952" + 
":  " + 
"(b('gvvk2') <= 0.41425721347332) ? " + 
"-0.0012197635227075812" + 
":  " + 
"0.004114853340049199" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 507.5) ? " + 
"(b('L8b1med') <= 499.25) ? " + 
"(b('L8b7med') <= 2535.5) ? " + 
"-3.322265468701323e-05" + 
":  " + 
"0.013237094730618834" + 
":  " + 
"(b('lat') <= 42.05848503112793) ? " + 
"-0.0026281062824989867" + 
":  " + 
"-0.01591929044381243" + 
":  " + 
"(b('L8b1med') <= 512.5) ? " + 
"(b('sand') <= 39.5) ? " + 
"0.0264038650510436" + 
":  " + 
"-0.0014068878445523264" + 
":  " + 
"(b('sand') <= 65.5) ? " + 
"0.0005223424126630849" + 
":  " + 
"-0.0042332187804084015" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -120.78556060791016) ? " + 
"(b('bulk') <= 135.0) ? " + 
"(b('gvvk2') <= 0.3320176601409912) ? " + 
"-0.002693499208902689" + 
":  " + 
"0.016685433292076522" + 
":  " + 
"(b('L8b7med') <= 2401.25) ? " + 
"-0.004939848724998663" + 
":  " + 
"0.0016006767284995835" + 
":  " + 
"(b('lon') <= -120.78532028198242) ? " + 
"(b('lat') <= 38.14932060241699) ? " + 
"0.005775473917219193" + 
":  " + 
"0.01997503610713386" + 
":  " + 
"(b('lon') <= -120.6328010559082) ? " + 
"-0.012175085175528906" + 
":  " + 
"7.447053781165461e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2340.5) ? " + 
"(b('bulk') <= 135.5) ? " + 
"(b('lat') <= 45.324920654296875) ? " + 
"0.004196754431699111" + 
":  " + 
"-0.0011585316020069959" + 
":  " + 
"(b('bulk') <= 137.5) ? " + 
"-0.011701685308054302" + 
":  " + 
"-0.0021531684081908847" + 
":  " + 
"(b('L8b6med') <= 2352.5) ? " + 
"0.015144453923630785" + 
":  " + 
"(b('L8b7med') <= 1509.0) ? " + 
"0.0021430191725796167" + 
":  " + 
"-0.00012654662389767758" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.5746753215789795) ? " + 
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('lat') <= 49.570478439331055) ? " + 
"-0.004053254579060947" + 
":  " + 
"1.8842721876496296e-05" + 
":  " + 
"(b('svvk3') <= 0.06443404033780098) ? " + 
"0.00017491970406429108" + 
":  " + 
"-0.002137540995296228" + 
":  " + 
"(b('bulk') <= 137.0) ? " + 
"(b('L8b2med') <= 434.0) ? " + 
"0.007113899447749983" + 
":  " + 
"3.744969697250707e-05" + 
":  " + 
"(b('L8b1med') <= 588.5) ? " + 
"0.013035297745761315" + 
":  " + 
"0.008449830970253175" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('lat') <= 36.15193557739258) ? " + 
"0.0013270085745529987" + 
":  " + 
"-0.00044942441292229496" + 
":  " + 
"-0.02784437754527097" + 
":  " + 
"(b('gvvk2') <= 0.4510953277349472) ? " + 
"(b('gvvk2') <= 0.44503913819789886) ? " + 
"0.003599861602538834" + 
":  " + 
"0.016068046684998408" + 
":  " + 
"(b('trees') <= 9.015841007232666) ? " + 
"0.0015388514128417423" + 
":  " + 
"-0.0027288992537611847" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 27.5) ? " + 
"(b('svvk3') <= 0.007927745580673218) ? " + 
"(b('svvk3') <= 0.007205476053059101) ? " + 
"-0.00023429105104007104" + 
":  " + 
"-0.008403008431111535" + 
":  " + 
"(b('trees') <= 17.931958198547363) ? " + 
"0.0004680886842437521" + 
":  " + 
"0.005699995792194989" + 
":  " + 
"(b('trees') <= 13.169122695922852) ? " + 
"(b('trees') <= 5.409235715866089) ? " + 
"-0.001245751991213767" + 
":  " + 
"0.002557717137690037" + 
":  " + 
"(b('gvvk2') <= 0.4003211557865143) ? " + 
"-0.0033315832314913577" + 
":  " + 
"-0.021447010989118276" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1239.0) ? " + 
"(b('L8b2med') <= 291.5) ? " + 
"(b('L8b6med') <= 1726.0) ? " + 
"-0.0041889788323343224" + 
":  " + 
"0.0033003141053530582" + 
":  " + 
"(b('svvk3') <= -0.0003122568215303545) ? " + 
"-0.0054322977409046735" + 
":  " + 
"-0.0026719501997311914" + 
":  " + 
"(b('L8b7med') <= 1355.0) ? " + 
"(b('L8b7med') <= 1349.0) ? " + 
"0.0013976886266902375" + 
":  " + 
"0.014971979578941086" + 
":  " + 
"(b('L8b7med') <= 1387.0) ? " + 
"-0.004310326940978691" + 
":  " + 
"3.43465863293514e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('lat') <= 56.000450134277344) ? " + 
"-0.0001915849113445423" + 
":  " + 
"0.004074712792858096" + 
":  " + 
"-0.025110183317801182" + 
":  " + 
"(b('gvvk2') <= 0.46257317066192627) ? " + 
"(b('L8b6med') <= 2676.5) ? " + 
"0.0010398550978018145" + 
":  " + 
"0.012538950052773723" + 
":  " + 
"(b('L8b2med') <= 887.0) ? " + 
"0.0006259199464541556" + 
":  " + 
"-0.005134761537082004" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"(b('svvk3') <= 0.002330337418243289) ? " + 
"-0.001593114728205114" + 
":  " + 
"-0.008344972132818505" + 
":  " + 
"(b('ndvi_med') <= 734.25) ? " + 
"(b('L8b2med') <= 1407.0) ? " + 
"0.007948218633680915" + 
":  " + 
"-0.00022399777289372944" + 
":  " + 
"(b('ndvi_med') <= 1179.0) ? " + 
"-0.0018263525331742574" + 
":  " + 
"7.989003935989774e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 615.0) ? " + 
"(b('L8b1med') <= 606.75) ? " + 
"-7.475836296905861e-05" + 
":  " + 
"0.005131460994006888" + 
":  " + 
"(b('lon') <= 0.6124000549316406) ? " + 
"-0.003773143414732385" + 
":  " + 
"0.004078073089662996" + 
":  " + 
"(b('L8b7med') <= 2269.0) ? " + 
"(b('ndvi_med') <= 1622.0) ? " + 
"0.0038852561907322322" + 
":  " + 
"0.0205065162289928" + 
":  " + 
"(b('ndvi_med') <= 1369.0) ? " + 
"-0.001320825302145756" + 
":  " + 
"0.002078564739157365" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 1.3649256229400635) ? " + 
"(b('svvk3') <= 0.014892799779772758) ? " + 
"(b('svvk3') <= 0.008779367431998253) ? " + 
"0.00018395392325062468" + 
":  " + 
"0.005999852375188474" + 
":  " + 
"(b('svvk3') <= 0.02459165919572115) ? " + 
"-0.004803416520407572" + 
":  " + 
"0.0007685241654089325" + 
":  " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"(b('lat') <= 40.25114440917969) ? " + 
"0.0034530756320716965" + 
":  " + 
"-0.006226755067705239" + 
":  " + 
"(b('trees') <= 6.115110635757446) ? " + 
"0.0030703922543076374" + 
":  " + 
"-0.0002556127848886721" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.546385049819946) ? " + 
"(b('lon') <= -82.97315216064453) ? " + 
"(b('lon') <= -83.91805267333984) ? " + 
"6.638827719273218e-05" + 
":  " + 
"-0.011008136055455142" + 
":  " + 
"(b('trees') <= 8.635247230529785) ? " + 
"0.008676480400742018" + 
":  " + 
"-0.00047638633663714527" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"(b('lat') <= 41.19405937194824) ? " + 
"-0.013629663341266259" + 
":  " + 
"-0.0023908692247791878" + 
":  " + 
"(b('lat') <= 43.73078536987305) ? " + 
"0.0022243935503103262" + 
":  " + 
"-0.000746772333475479" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1242.0) ? " + 
"(b('L8b1med') <= 207.0) ? " + 
"(b('svvk3') <= 0.08850669488310814) ? " + 
"0.0029970844397447377" + 
":  " + 
"-0.003835361294578732" + 
":  " + 
"(b('svvk3') <= -0.0003122568215303545) ? " + 
"-0.005167952518781198" + 
":  " + 
"-0.002446327271812321" + 
":  " + 
"(b('L8b7med') <= 1355.0) ? " + 
"(b('ndvi_med') <= 3538.5) ? " + 
"0.005363044007224649" + 
":  " + 
"-0.0010053304860256987" + 
":  " + 
"(b('L8b7med') <= 1387.0) ? " + 
"-0.003946156761956916" + 
":  " + 
"4.234624670656342e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 27.5) ? " + 
"(b('bulk') <= 145.5) ? " + 
"(b('bulk') <= 141.5) ? " + 
"0.00022645357357646198" + 
":  " + 
"-0.003187156983804186" + 
":  " + 
"(b('lat') <= 44.67049980163574) ? " + 
"0.0006213425463806227" + 
":  " + 
"0.012639140281352221" + 
":  " + 
"(b('trees') <= 13.169122695922852) ? " + 
"(b('bulk') <= 115.5) ? " + 
"-0.0046711975537243045" + 
":  " + 
"3.299397792132472e-05" + 
":  " + 
"(b('gvvk2') <= 0.4003211557865143) ? " + 
"-0.0029685264173808837" + 
":  " + 
"-0.019272411399245126" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -120.78556060791016) ? " + 
"(b('L8b7med') <= 1772.0) ? " + 
"(b('ndvi_med') <= 1465.5) ? " + 
"-0.005351381416660889" + 
":  " + 
"0.01428623893257093" + 
":  " + 
"(b('L8b3med') <= 1016.5) ? " + 
"-0.0047228713053899096" + 
":  " + 
"0.0005493573950184948" + 
":  " + 
"(b('lon') <= -120.78532028198242) ? " + 
"(b('L8b3med') <= 867.5) ? " + 
"0.00526871389748057" + 
":  " + 
"0.018048319868403745" + 
":  " + 
"(b('lon') <= -120.6328010559082) ? " + 
"-0.010886789285992717" + 
":  " + 
"6.984658818036036e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.5746753215789795) ? " + 
"(b('svvk3') <= 0.06443404033780098) ? " + 
"(b('svvk3') <= 0.0628238171339035) ? " + 
"-7.624018999494467e-06" + 
":  " + 
"0.01825273798356994" + 
":  " + 
"(b('sand') <= 46.5) ? " + 
"-0.005334172130410909" + 
":  " + 
"0.0011945619850945582" + 
":  " + 
"(b('bulk') <= 137.0) ? " + 
"(b('L8b6med') <= 2037.5) ? " + 
"0.006698662583527748" + 
":  " + 
"3.598631860505958e-05" + 
":  " + 
"(b('L8b6med') <= 3100.0) ? " + 
"0.011347178255452672" + 
":  " + 
"0.007555190008156354" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2340.5) ? " + 
"(b('L8b6med') <= 2201.75) ? " + 
"(b('L8b7med') <= 1734.25) ? " + 
"-0.0005920149997055456" + 
":  " + 
"0.0043056381693789446" + 
":  " + 
"(b('L8b7med') <= 1363.75) ? " + 
"0.0012041616893580336" + 
":  " + 
"-0.005419697480882245" + 
":  " + 
"(b('L8b7med') <= 1510.0) ? " + 
"(b('bulk') <= 133.5) ? " + 
"-0.00013575724600667434" + 
":  " + 
"0.004839039049316918" + 
":  " + 
"(b('sand') <= 15.5) ? " + 
"-0.007210100333389165" + 
":  " + 
"-4.12208143568492e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 22.880224227905273) ? " + 
"(b('lon') <= 22.87806510925293) ? " + 
"(b('lat') <= 32.18929862976074) ? " + 
"-0.0038579368043838804" + 
":  " + 
"0.00011129620535878117" + 
":  " + 
"(b('svvk3') <= 0.002427630541205872) ? " + 
"0.0012675009558314465" + 
":  " + 
"0.007055245607312369" + 
":  " + 
"(b('L8b7med') <= 1392.5) ? " + 
"-0.011413128550357449" + 
":  " + 
"(b('svvk3') <= -0.009443551767617464) ? " + 
"0.004414042602657746" + 
":  " + 
"-0.0012003061572382948" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -121.75626754760742) ? " + 
"(b('ndvi_med') <= 1364.75) ? " + 
"-0.01143960542212906" + 
":  " + 
"(b('sand') <= 38.5) ? " + 
"-0.002434422677516354" + 
":  " + 
"0.0022835659981139678" + 
":  " + 
"(b('lon') <= -121.29663467407227) ? " + 
"(b('L8b2med') <= 885.0) ? " + 
"0.006424160160742806" + 
":  " + 
"0.0007107213025345643" + 
":  " + 
"(b('lon') <= -120.94869613647461) ? " + 
"-0.004305663969428846" + 
":  " + 
"5.423169102934469e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"(b('svvk3') <= -0.005489814328029752) ? " + 
"-0.001885629867617888" + 
":  " + 
"0.0006070604269554756" + 
":  " + 
"0.019774166824566286" + 
":  " + 
"(b('lat') <= 45.10073471069336) ? " + 
"(b('L8b7med') <= 1606.5) ? " + 
"0.0022262850254101472" + 
":  " + 
"-0.005108789092083327" + 
":  " + 
"(b('bulk') <= 145.5) ? " + 
"-1.1337317384891177e-05" + 
":  " + 
"0.00815024979273768" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 103.5) ? " + 
"(b('L8b2med') <= 444.5) ? " + 
"(b('ndvi_med') <= 4913.25) ? " + 
"-0.004884306378506301" + 
":  " + 
"-0.0033598794431098367" + 
":  " + 
"(b('svvk3') <= 0.010788788989884779) ? " + 
"0.0004695597905658988" + 
":  " + 
"-0.0017174291235032557" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"0.012136108973927473" + 
":  " + 
"(b('L8b7med') <= 1613.0) ? " + 
"0.0005910042944059214" + 
":  " + 
"-0.00018906249338851525" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 507.5) ? " + 
"(b('L8b1med') <= 499.25) ? " + 
"(b('L8b7med') <= 2535.5) ? " + 
"-4.24901260063286e-05" + 
":  " + 
"0.011699140621253226" + 
":  " + 
"(b('lat') <= 42.05848503112793) ? " + 
"-0.002239330571629045" + 
":  " + 
"-0.013593290594146809" + 
":  " + 
"(b('L8b1med') <= 540.5) ? " + 
"(b('L8b7med') <= 2558.5) ? " + 
"0.004084002610645656" + 
":  " + 
"-0.006592802623883759" + 
":  " + 
"(b('L8b1med') <= 549.5) ? " + 
"-0.008156115514266643" + 
":  " + 
"0.00024075370517644514" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 34.5) ? " + 
"(b('clay') <= 32.5) ? " + 
"(b('clay') <= 30.5) ? " + 
"7.999778773692747e-05" + 
":  " + 
"-0.002872742940095749" + 
":  " + 
"(b('L8b1med') <= 460.0) ? " + 
"0.00812004776543658" + 
":  " + 
"-0.0008620151513938733" + 
":  " + 
"(b('lon') <= -97.8183364868164) ? " + 
"-0.010970327411929076" + 
":  " + 
"(b('L8b6med') <= 2094.0) ? " + 
"0.005023381692544904" + 
":  " + 
"-0.0019589479966954293" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.5746753215789795) ? " + 
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('lat') <= 49.570478439331055) ? " + 
"-0.0037177268663719245" + 
":  " + 
"-9.457417797797536e-06" + 
":  " + 
"(b('svvk3') <= -0.02579908538609743) ? " + 
"0.006544411933477032" + 
":  " + 
"1.729710316761549e-05" + 
":  " + 
"(b('bulk') <= 137.0) ? " + 
"(b('clay') <= 6.5) ? " + 
"0.00600972757163154" + 
":  " + 
"0.00017470906189365198" + 
":  " + 
"(b('gvvk2') <= 0.5845170617103577) ? " + 
"0.010126154779056235" + 
":  " + 
"0.006962634385946881" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.546385049819946) ? " + 
"(b('lon') <= -82.97315216064453) ? " + 
"(b('lon') <= -83.91805267333984) ? " + 
"6.867510829280409e-05" + 
":  " + 
"-0.01003962456418607" + 
":  " + 
"(b('trees') <= 8.635247230529785) ? " + 
"0.007722116980198245" + 
":  " + 
"-0.0003748252666035338" + 
":  " + 
"(b('svvk3') <= 0.012563469354063272) ? " + 
"(b('lon') <= -0.6403000056743622) ? " + 
"-0.004835899228573568" + 
":  " + 
"-0.0006145408000475648" + 
":  " + 
"(b('L8b2med') <= 999.5) ? " + 
"0.0008821758788402113" + 
":  " + 
"0.01165683171518718" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 1922.0) ? " + 
"(b('ndvi_med') <= 1935.0) ? " + 
"-0.004910436779968053" + 
":  " + 
"(b('lat') <= 35.63111400604248) ? " + 
"-0.0023233783856625723" + 
":  " + 
"-0.003379895264929031" + 
":  " + 
"(b('gvvk2') <= 0.038837023079395294) ? " + 
"-0.006763582995312212" + 
":  " + 
"(b('sand') <= 14.5) ? " + 
"0.0035509005285473184" + 
":  " + 
"7.4140396248516826e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 911.0) ? " + 
"(b('L8b3med') <= 899.25) ? " + 
"(b('trees') <= 4.605867385864258) ? " + 
"-0.0013113961891345943" + 
":  " + 
"0.0005219239819085767" + 
":  " + 
"(b('svvk3') <= 0.03136119060218334) ? " + 
"-0.00865622191491908" + 
":  " + 
"-0.00017659472489575667" + 
":  " + 
"(b('clay') <= 22.5) ? " + 
"(b('lon') <= -105.85250091552734) ? " + 
"-0.0001284339543289002" + 
":  " + 
"0.0024435429060640592" + 
":  " + 
"(b('ndvi_med') <= 2942.0) ? " + 
"-0.0005115520009657065" + 
":  " + 
"-0.010966060824842486" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 253.5) ? " + 
"(b('L8b2med') <= 305.5) ? " + 
"(b('gvvk2') <= 0.39189615845680237) ? " + 
"0.004178422615107008" + 
":  " + 
"-0.0023847150237164827" + 
":  " + 
"(b('svvk3') <= -0.028644305653870106) ? " + 
"0.0004875362067535971" + 
":  " + 
"-0.004207099505373503" + 
":  " + 
"(b('lat') <= 56.03929901123047) ? " + 
"(b('L8b2med') <= 331.5) ? " + 
"0.0046169436387943075" + 
":  " + 
"-1.6336327617794734e-05" + 
":  " + 
"(b('L8b1med') <= 441.25) ? " + 
"0.0033090919024314214" + 
":  " + 
"0.006239444014424528" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2857.75) ? " + 
"(b('L8b6med') <= 2852.75) ? " + 
"(b('bulk') <= 148.5) ? " + 
"-0.0005083947064616003" + 
":  " + 
"0.0029015485188648472" + 
":  " + 
"-0.018476243543719115" + 
":  " + 
"(b('L8b7med') <= 1679.0) ? " + 
"(b('L8b7med') <= 1669.5) ? " + 
"0.0031757375349568246" + 
":  " + 
"0.015160138342569305" + 
":  " + 
"(b('L8b2med') <= 514.75) ? " + 
"-0.005615780391271562" + 
":  " + 
"0.00015281704196559273" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('L8b3med') <= 836.5) ? " + 
"(b('L8b3med') <= 809.5) ? " + 
"-0.004307602420028714" + 
":  " + 
"-0.013037983939180882" + 
":  " + 
"(b('L8b6med') <= 2978.25) ? " + 
"0.002974512131895249" + 
":  " + 
"-0.0020980357198230504" + 
":  " + 
"(b('L8b6med') <= 2857.75) ? " + 
"(b('L8b6med') <= 2840.75) ? " + 
"-8.727498672705501e-05" + 
":  " + 
"-0.007097401861004364" + 
":  " + 
"(b('L8b7med') <= 1679.0) ? " + 
"0.006093951999516523" + 
":  " + 
"0.00012117058095892869" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.546385049819946) ? " + 
"(b('L8b3med') <= 622.0) ? " + 
"(b('lat') <= 47.27204513549805) ? " + 
"-0.003988521450977889" + 
":  " + 
"-0.012102145753738497" + 
":  " + 
"(b('svvk3') <= 0.018222343176603317) ? " + 
"0.0008946138715675794" + 
":  " + 
"-0.0010089285519864141" + 
":  " + 
"(b('svvk3') <= 0.009431565180420876) ? " + 
"(b('L8b7med') <= 1927.0) ? " + 
"0.00014767660876922938" + 
":  " + 
"-0.003600385263769732" + 
":  " + 
"(b('svvk3') <= 0.009559824597090483) ? " + 
"0.017474074185134025" + 
":  " + 
"0.0005165759227328592" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 923.5) ? " + 
"(b('L8b2med') <= 542.5) ? " + 
"(b('L8b6med') <= 2871.5) ? " + 
"-0.0002875046182302514" + 
":  " + 
"0.004076142217891297" + 
":  " + 
"(b('L8b2med') <= 553.0) ? " + 
"-0.00637861928391984" + 
":  " + 
"-0.0010500317739257118" + 
":  " + 
"(b('L8b7med') <= 2145.75) ? " + 
"(b('L8b7med') <= 2055.5) ? " + 
"-0.00011242286986917253" + 
":  " + 
"0.0048796756946180055" + 
":  " + 
"(b('L8b7med') <= 2183.5) ? " + 
"-0.0066401166747347235" + 
":  " + 
"3.7554214615166974e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.5746753215789795) ? " + 
"(b('svvk3') <= 0.06443404033780098) ? " + 
"(b('svvk3') <= 0.0628238171339035) ? " + 
"-1.1324555647355872e-05" + 
":  " + 
"0.016683222485600974" + 
":  " + 
"(b('gvvk2') <= 0.37841586768627167) ? " + 
"0.007247206102604063" + 
":  " + 
"-0.0028525385128695784" + 
":  " + 
"(b('bulk') <= 137.0) ? " + 
"(b('sand') <= 77.0) ? " + 
"-0.0003575098921203325" + 
":  " + 
"0.0027606487196500384" + 
":  " + 
"(b('L8b3med') <= 1120.5) ? " + 
"0.009504166639944162" + 
":  " + 
"0.00713089264172842" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('lat') <= 36.15193557739258) ? " + 
"0.0009988698584835747" + 
":  " + 
"-0.0003543558158365951" + 
":  " + 
"-0.021256427681398682" + 
":  " + 
"(b('gvvk2') <= 0.4510953277349472) ? " + 
"(b('ndvi_med') <= 3286.25) ? " + 
"0.013130621827122518" + 
":  " + 
"0.003822640774915703" + 
":  " + 
"(b('trees') <= 9.015841007232666) ? " + 
"0.0012490130472369255" + 
":  " + 
"-0.0022157816907464748" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 23.046470642089844) ? " + 
"(b('trees') <= 21.0009708404541) ? " + 
"1.5436260883926634e-07" + 
":  " + 
"0.0040158197366326615" + 
":  " + 
"(b('svvk3') <= -0.019183877855539322) ? " + 
"-0.006643992194931707" + 
":  " + 
"-0.0007299354032404994" + 
":  " + 
"(b('lat') <= 39.09149932861328) ? " + 
"-0.0009161751256226425" + 
":  " + 
"(b('sand') <= 38.5) ? " + 
"0.0075279930178333565" + 
":  " + 
"0.004130044003187713" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3497.75) ? " + 
"(b('L8b6med') <= 3479.5) ? " + 
"(b('L8b7med') <= 2461.0) ? " + 
"0.00025349606793546755" + 
":  " + 
"-0.0018782503535317407" + 
":  " + 
"(b('svvk3') <= -0.005644022952765226) ? " + 
"0.014951132316821214" + 
":  " + 
"0.004216023488911666" + 
":  " + 
"(b('L8b7med') <= 2243.5) ? " + 
"(b('L8b3med') <= 1056.0) ? " + 
"-0.007103057039471452" + 
":  " + 
"-0.0018784893010795928" + 
":  " + 
"(b('L8b7med') <= 2629.5) ? " + 
"0.0029506799716854347" + 
":  " + 
"-0.0008094069801218273" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 814.0) ? " + 
"(b('lat') <= 50.94952583312988) ? " + 
"(b('sand') <= 49.0) ? " + 
"-0.00048626734806054585" + 
":  " + 
"-0.007914143033304868" + 
":  " + 
"(b('L8b6med') <= 2862.25) ? " + 
"0.00044955652966204463" + 
":  " + 
"0.0058984751651418215" + 
":  " + 
"(b('lat') <= 53.63138008117676) ? " + 
"(b('ndvi_med') <= 3422.5) ? " + 
"0.00016220328381466443" + 
":  " + 
"0.0028912895677190623" + 
":  " + 
"(b('ndvi_med') <= 3324.0) ? " + 
"-0.017903423684501985" + 
":  " + 
"-0.001650175009382779" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 9.25374984741211) ? " + 
"(b('lat') <= 32.18929862976074) ? " + 
"(b('clay') <= 30.0) ? " + 
"-0.0023543122966261485" + 
":  " + 
"-0.009582613268260654" + 
":  " + 
"(b('lon') <= -106.49531555175781) ? " + 
"-0.0003000826219700844" + 
":  " + 
"0.0006107342893083275" + 
":  " + 
"(b('svvk3') <= -0.009443551767617464) ? " + 
"(b('svvk3') <= -0.013376248069107533) ? " + 
"0.0007425218030140216" + 
":  " + 
"0.013166890128367192" + 
":  " + 
"(b('svvk3') <= 0.001219265366671607) ? " + 
"-0.003807971050789384" + 
":  " + 
"-0.00017997494909414687" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('ndvi_med') <= 4452.5) ? " + 
"(b('svvk3') <= -0.023769686929881573) ? " + 
"0.00010761689915341695" + 
":  " + 
"-0.005003710277452977" + 
":  " + 
"(b('L8b2med') <= 458.0) ? " + 
"0.00025716938223277475" + 
":  " + 
"-0.010074446422902436" + 
":  " + 
"(b('svvk3') <= -0.017486218363046646) ? " + 
"(b('ndvi_med') <= 1762.0) ? " + 
"0.014544116545226027" + 
":  " + 
"0.0025267137039547177" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.0037002815538973188" + 
":  " + 
"8.353950028728903e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('L8b3med') <= 836.5) ? " + 
"(b('L8b7med') <= 1741.25) ? " + 
"-0.003947150753419157" + 
":  " + 
"-0.01170200677714621" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.007783439051664676" + 
":  " + 
"-0.0010205342479078954" + 
":  " + 
"(b('trees') <= 17.942265510559082) ? " + 
"(b('trees') <= 15.571342945098877) ? " + 
"-5.536132465087777e-06" + 
":  " + 
"-0.003471384912535421" + 
":  " + 
"(b('L8b2med') <= 445.75) ? " + 
"-0.0024908662791560824" + 
":  " + 
"0.002925549777861916" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('lat') <= 36.15193557739258) ? " + 
"0.0009491269485777601" + 
":  " + 
"-0.00033499706722370026" + 
":  " + 
"-0.01915016235927991" + 
":  " + 
"(b('gvvk2') <= 0.4510953277349472) ? " + 
"(b('clay') <= 16.5) ? " + 
"0.003628786174199816" + 
":  " + 
"0.011760245659664145" + 
":  " + 
"(b('L8b2med') <= 887.0) ? " + 
"0.000777327588541018" + 
":  " + 
"-0.0044282445227543455" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1949.75) ? " + 
"(b('L8b3med') <= 1933.0) ? " + 
"(b('L8b2med') <= 1322.75) ? " + 
"4.826275175069005e-05" + 
":  " + 
"-0.0034208951449630513" + 
":  " + 
"(b('L8b3med') <= 1947.5) ? " + 
"0.005878742519011632" + 
":  " + 
"0.006854075480741059" + 
":  " + 
"(b('ndvi_med') <= 889.5) ? " + 
"(b('L8b1med') <= 1426.25) ? " + 
"-0.002170868894528298" + 
":  " + 
"0.0024079019979624527" + 
":  " + 
"(b('bulk') <= 149.5) ? " + 
"-0.00801082126930433" + 
":  " + 
"-0.0073607103518435815" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 133.5) ? " + 
"(b('svvk3') <= -0.0024871755158528686) ? " + 
"(b('svvk3') <= -0.003473088494502008) ? " + 
"0.0007584976276440742" + 
":  " + 
"0.009403292574105751" + 
":  " + 
"(b('svvk3') <= 0.017596827819943428) ? " + 
"-0.0023284919808507967" + 
":  " + 
"0.0012595494697087036" + 
":  " + 
"(b('L8b6med') <= 2684.75) ? " + 
"(b('L8b6med') <= 2659.0) ? " + 
"0.0009610677224898437" + 
":  " + 
"0.010103751788611564" + 
":  " + 
"(b('ndvi_med') <= 2500.5) ? " + 
"0.00026966473322210995" + 
":  " + 
"-0.002012613655282734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('ndvi_med') <= 4452.5) ? " + 
"(b('lon') <= -100.68251419067383) ? " + 
"-0.003611609220443136" + 
":  " + 
"0.0003372447605544988" + 
":  " + 
"(b('lon') <= -30.883347988128662) ? " + 
"-0.009185829430742865" + 
":  " + 
"5.334025097783468e-05" + 
":  " + 
"(b('lon') <= -5.546385049819946) ? " + 
"(b('lon') <= -82.97315216064453) ? " + 
"0.00011423898174124736" + 
":  " + 
"0.003567826885730055" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"-0.004464351287024378" + 
":  " + 
"-0.000103363094525043" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2340.5) ? " + 
"(b('L8b6med') <= 2201.75) ? " + 
"(b('L8b7med') <= 1734.25) ? " + 
"-0.0005237585576812608" + 
":  " + 
"0.0036676951404102168" + 
":  " + 
"(b('L8b6med') <= 2260.25) ? " + 
"-0.006676675229676113" + 
":  " + 
"-0.0011465688622618831" + 
":  " + 
"(b('L8b7med') <= 1510.0) ? " + 
"(b('ndvi_med') <= 4738.75) ? " + 
"0.002959487883605759" + 
":  " + 
"-0.002189799687472157" + 
":  " + 
"(b('L8b7med') <= 1527.25) ? " + 
"-0.004118248310505772" + 
":  " + 
"-8.252579803190807e-07" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 168.5) ? " + 
"(b('L8b6med') <= 3580.25) ? " + 
"0.00013850609642307042" + 
":  " + 
"-0.0007127465269403345" + 
":  " + 
"(b('L8b1med') <= 512.5) ? " + 
"0.0012551307537118361" + 
":  " + 
"0.007145863424528873" + 
":  " + 
"-0.005877822269107547" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1312.0) ? " + 
"(b('L8b3med') <= 1252.5) ? " + 
"(b('L8b3med') <= 1235.5) ? " + 
"-1.1635751395541993e-05" + 
":  " + 
"0.006672634659228446" + 
":  " + 
"(b('L8b7med') <= 2543.75) ? " + 
"-0.0017975456631104739" + 
":  " + 
"-0.007823581275034446" + 
":  " + 
"(b('L8b3med') <= 1330.0) ? " + 
"(b('L8b1med') <= 759.0) ? " + 
"0.0065090352464422276" + 
":  " + 
"0.017813115493619136" + 
":  " + 
"(b('ndvi_med') <= 1771.0) ? " + 
"-0.0003583729866301151" + 
":  " + 
"0.006867938081313914" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1980.5) ? " + 
"(b('lon') <= -97.21606063842773) ? " + 
"(b('lat') <= 38.14833068847656) ? " + 
"-0.005408720002922017" + 
":  " + 
"-0.000803300486415861" + 
":  " + 
"(b('L8b7med') <= 1927.0) ? " + 
"0.0007281093437014272" + 
":  " + 
"-0.006905758756626909" + 
":  " + 
"(b('L8b7med') <= 1983.5) ? " + 
"0.01598544544183597" + 
":  " + 
"(b('L8b2med') <= 544.0) ? " + 
"0.008694676848752128" + 
":  " + 
"9.813916724852515e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= 1.4101499915122986) ? " + 
"(b('L8b3med') <= 701.75) ? " + 
"-0.0028056438660149312" + 
":  " + 
"0.0003110128578077225" + 
":  " + 
"0.014386900897652377" + 
":  " + 
"(b('lon') <= 6.412564992904663) ? " + 
"(b('svvk3') <= 0.002975506125949323) ? " + 
"-0.002259847995175302" + 
":  " + 
"-0.008519642823102226" + 
":  " + 
"(b('clay') <= 26.0) ? " + 
"0.0002435509592385135" + 
":  " + 
"-0.002115407905386605" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 911.0) ? " + 
"(b('L8b1med') <= 459.5) ? " + 
"(b('L8b1med') <= 455.75) ? " + 
"-1.0185796139112584e-05" + 
":  " + 
"0.012920399628296317" + 
":  " + 
"(b('L8b6med') <= 3091.5) ? " + 
"-0.0033448961739099394" + 
":  " + 
"0.0036128669710989805" + 
":  " + 
"(b('svvk3') <= 0.004657700890675187) ? " + 
"(b('L8b7med') <= 2767.25) ? " + 
"-0.0011206738733075415" + 
":  " + 
"0.0019460111405236239" + 
":  " + 
"(b('L8b7med') <= 2543.0) ? " + 
"0.002315707688789491" + 
":  " + 
"-0.0008739457173184664" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.018222343176603317) ? " + 
"(b('svvk3') <= 0.01235300675034523) ? " + 
"(b('svvk3') <= 0.011184026021510363) ? " + 
"1.4298415050006328e-05" + 
":  " + 
"-0.007712442649516509" + 
":  " + 
"(b('L8b6med') <= 2399.75) ? " + 
"-0.004561788076630616" + 
":  " + 
"0.00472712669507388" + 
":  " + 
"(b('sand') <= 16.5) ? " + 
"-0.016430671252972262" + 
":  " + 
"(b('svvk3') <= 0.020897462964057922) ? " + 
"-0.004938937383421421" + 
":  " + 
"0.0001649121127625138" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -121.75626754760742) ? " + 
"(b('ndvi_med') <= 1364.75) ? " + 
"-0.009695754353164207" + 
":  " + 
"(b('ndvi_med') <= 1532.75) ? " + 
"0.0019338813515949183" + 
":  " + 
"-0.002098838238608458" + 
":  " + 
"(b('lon') <= -121.29663467407227) ? " + 
"(b('L8b6med') <= 3628.5) ? " + 
"0.007228341844591382" + 
":  " + 
"0.0028693011605512527" + 
":  " + 
"(b('lon') <= -120.94869613647461) ? " + 
"-0.0034455446748462193" + 
":  " + 
"4.52450838849374e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1949.75) ? " + 
"(b('L8b3med') <= 1933.0) ? " + 
"(b('L8b2med') <= 1322.75) ? " + 
"4.637454273544103e-05" + 
":  " + 
"-0.0031286668313387526" + 
":  " + 
"(b('lon') <= -115.8929672241211) ? " + 
"0.006136999214766306" + 
":  " + 
"0.005033076443981391" + 
":  " + 
"(b('ndvi_med') <= 889.5) ? " + 
"(b('clay') <= 17.5) ? " + 
"0.0021279123953799536" + 
":  " + 
"-0.0021264485658681956" + 
":  " + 
"-0.006956388632302815" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 253.5) ? " + 
"(b('L8b2med') <= 305.5) ? " + 
"(b('gvvk2') <= 0.39189615845680237) ? " + 
"0.003848005109653515" + 
":  " + 
"-0.002050053877025828" + 
":  " + 
"(b('ndvi_med') <= 4581.5) ? " + 
"-0.0037353816114943273" + 
":  " + 
"4.3236822756337334e-05" + 
":  " + 
"(b('L8b7med') <= 1581.25) ? " + 
"(b('ndvi_med') <= 3582.0) ? " + 
"0.0020658569459172877" + 
":  " + 
"-0.0011167913815636964" + 
":  " + 
"(b('L8b3med') <= 814.0) ? " + 
"-0.0016467660766183799" + 
":  " + 
"0.00020584277116489076" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.5746753215789795) ? " + 
"(b('svvk3') <= 0.06443404033780098) ? " + 
"(b('svvk3') <= 0.0628238171339035) ? " + 
"-7.145436968927981e-06" + 
":  " + 
"0.014314216953389025" + 
":  " + 
"(b('sand') <= 46.5) ? " + 
"-0.004322587225273802" + 
":  " + 
"0.000990247262690848" + 
":  " + 
"(b('bulk') <= 137.0) ? " + 
"(b('clay') <= 6.5) ? " + 
"0.005148865022561483" + 
":  " + 
"0.00017582857642920702" + 
":  " + 
"(b('svvk3') <= 0.01606333814561367) ? " + 
"0.005914237402711103" + 
":  " + 
"0.008544257941244915" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 43.65060043334961) ? " + 
"(b('lat') <= 43.59345054626465) ? " + 
"(b('L8b6med') <= 2676.25) ? " + 
"0.0019737850204147654" + 
":  " + 
"-0.0001924068083600615" + 
":  " + 
"0.01633113348322135" + 
":  " + 
"(b('lat') <= 44.28042411804199) ? " + 
"(b('L8b7med') <= 1620.5) ? " + 
"0.0015454851291653948" + 
":  " + 
"-0.005856392231530387" + 
":  " + 
"(b('sand') <= 35.5) ? " + 
"-0.001921665914877323" + 
":  " + 
"0.0005762999034983705" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 507.5) ? " + 
"(b('L8b1med') <= 499.25) ? " + 
"(b('L8b7med') <= 2535.5) ? " + 
"-3.8168483663556096e-05" + 
":  " + 
"0.009859770721204045" + 
":  " + 
"(b('lat') <= 42.05848503112793) ? " + 
"-0.0018710643281892234" + 
":  " + 
"-0.01122841835025086" + 
":  " + 
"(b('sand') <= 65.5) ? " + 
"(b('ndvi_med') <= 2130.0) ? " + 
"0.00015559592700091325" + 
":  " + 
"0.0026911094680957095" + 
":  " + 
"(b('gvvk2') <= 0.3332942724227905) ? " + 
"-0.006169619358011357" + 
":  " + 
"-0.0008333959312477086" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2802.5) ? " + 
"(b('L8b7med') <= 2786.5) ? " + 
"(b('L8b7med') <= 2637.0) ? " + 
"7.551431387384365e-05" + 
":  " + 
"-0.002198158964170598" + 
":  " + 
"(b('L8b1med') <= 753.25) ? " + 
"-0.008554397118978374" + 
":  " + 
"-0.014736446980910686" + 
":  " + 
"(b('L8b7med') <= 2935.5) ? " + 
"(b('bulk') <= 153.5) ? " + 
"0.007327690623738807" + 
":  " + 
"-0.002351213076866995" + 
":  " + 
"(b('L8b3med') <= 1340.5) ? " + 
"0.003162126767492624" + 
":  " + 
"-0.0008399494051954146" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 623.0) ? " + 
"(b('gvvk2') <= 0.13522601872682571) ? " + 
"-0.0019927988072034595" + 
":  " + 
"7.557818730587455e-05" + 
":  " + 
"(b('lon') <= 0.6124000549316406) ? " + 
"-0.0040222103761259" + 
":  " + 
"0.0030397449065812745" + 
":  " + 
"(b('ndvi_med') <= 1771.0) ? " + 
"(b('svvk3') <= 0.018095525912940502) ? " + 
"0.0011142567775504683" + 
":  " + 
"-0.0014763747161438661" + 
":  " + 
"(b('ndvi_med') <= 1936.0) ? " + 
"0.008411955241767688" + 
":  " + 
"-0.0015809423460516614" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('ndvi_med') <= 4452.5) ? " + 
"(b('svvk3') <= -0.023769686929881573) ? " + 
"-8.127938181304395e-06" + 
":  " + 
"-0.004498719553675472" + 
":  " + 
"(b('sand') <= 61.5) ? " + 
"-0.008328457539143644" + 
":  " + 
"-2.9294707923815944e-05" + 
":  " + 
"(b('svvk3') <= -0.017486218363046646) ? " + 
"(b('L8b2med') <= 446.0) ? " + 
"-0.005441293112618262" + 
":  " + 
"0.004643363640839658" + 
":  " + 
"(b('svvk3') <= -0.017296995036303997) ? " + 
"-0.00932901517552015" + 
":  " + 
"4.673863284456773e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 9.25374984741211) ? " + 
"(b('lat') <= 34.168094635009766) ? " + 
"(b('lon') <= -116.09638977050781) ? " + 
"0.008854010535681217" + 
":  " + 
"-0.0023353972368053777" + 
":  " + 
"(b('lat') <= 34.22196960449219) ? " + 
"0.007288860013874236" + 
":  " + 
"0.00019208053435044482" + 
":  " + 
"(b('lon') <= 22.87677574157715) ? " + 
"(b('L8b6med') <= 2779.0) ? " + 
"-0.0018276396013607126" + 
":  " + 
"-0.015842729447329534" + 
":  " + 
"(b('svvk3') <= 0.001219265366671607) ? " + 
"-0.0022209595788826634" + 
":  " + 
"0.0009175373417052543" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('clay') <= 22.5) ? " + 
"(b('lon') <= 0.5252151489257812) ? " + 
"-0.005286789311387291" + 
":  " + 
"0.00030904834142297943" + 
":  " + 
"(b('clay') <= 27.5) ? " + 
"0.0057453630092213675" + 
":  " + 
"-0.0008215096810815654" + 
":  " + 
"(b('svvk3') <= -0.0018616062588989735) ? " + 
"(b('lon') <= -115.78924560546875) ? " + 
"-0.0030549886217048814" + 
":  " + 
"0.0015582446250466879" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"-0.000934338269699422" + 
":  " + 
"0.000297970700524873" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"(b('svvk3') <= 0.002330337418243289) ? " + 
"-0.0008150824600919315" + 
":  " + 
"-0.00689175412424399" + 
":  " + 
"(b('ndvi_med') <= 750.75) ? " + 
"(b('L8b2med') <= 1319.75) ? " + 
"0.009337561402528949" + 
":  " + 
"0.0017235477887418832" + 
":  " + 
"(b('ndvi_med') <= 757.25) ? " + 
"-0.0059939832575120824" + 
":  " + 
"3.949248610301622e-08" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -121.75626754760742) ? " + 
"(b('svvk3') <= 0.0341707244515419) ? " + 
"(b('L8b2med') <= 796.75) ? " + 
"0.0016702513718060835" + 
":  " + 
"-0.002082440559467852" + 
":  " + 
"-0.008815797203543571" + 
":  " + 
"(b('lon') <= -121.29663467407227) ? " + 
"(b('L8b2med') <= 885.0) ? " + 
"0.004575094118465618" + 
":  " + 
"0.0008001029604176174" + 
":  " + 
"(b('lon') <= -120.94869613647461) ? " + 
"-0.002930941914828289" + 
":  " + 
"3.7953103439385726e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 2473.0) ? " + 
"(b('ndvi_med') <= 2130.0) ? " + 
"(b('ndvi_med') <= 2109.25) ? " + 
"-2.6725278927744534e-06" + 
":  " + 
"-0.009797096504689955" + 
":  " + 
"(b('ndvi_med') <= 2133.0) ? " + 
"0.023087170405310026" + 
":  " + 
"0.0013459731683238348" + 
":  " + 
"(b('ndvi_med') <= 2723.0) ? " + 
"(b('sand') <= 47.0) ? " + 
"-0.0013077728592163372" + 
":  " + 
"-0.008951127448658799" + 
":  " + 
"(b('L8b7med') <= 2044.0) ? " + 
"0.0005822684573142538" + 
":  " + 
"-0.0019633522613683512" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2340.5) ? " + 
"(b('bulk') <= 135.5) ? " + 
"(b('bulk') <= 115.5) ? " + 
"-0.0032713631233806106" + 
":  " + 
"0.0006974435224720888" + 
":  " + 
"(b('bulk') <= 137.5) ? " + 
"-0.007546937212515176" + 
":  " + 
"-0.0016956599630733374" + 
":  " + 
"(b('L8b6med') <= 2352.5) ? " + 
"0.009858854432074293" + 
":  " + 
"(b('L8b7med') <= 1454.0) ? " + 
"0.0014917297972996946" + 
":  " + 
"-3.848648661892844e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 814.0) ? " + 
"(b('lat') <= 55.90654945373535) ? " + 
"(b('L8b7med') <= 1613.0) ? " + 
"0.00010144332791154412" + 
":  " + 
"-0.0031332550714036726" + 
":  " + 
"(b('L8b6med') <= 2694.5) ? " + 
"0.0006053001078749082" + 
":  " + 
"0.00910206403302996" + 
":  " + 
"(b('lat') <= 53.63345909118652) ? " + 
"(b('L8b1med') <= 461.0) ? " + 
"0.0015915938397334905" + 
":  " + 
"-1.5017132876116149e-05" + 
":  " + 
"(b('ndvi_med') <= 3324.0) ? " + 
"-0.014842682363439164" + 
":  " + 
"-0.0013775820061081737" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -5.510674953460693) ? " + 
"(b('lon') <= -82.97315216064453) ? " + 
"(b('L8b7med') <= 1925.5) ? " + 
"-0.000790182969075497" + 
":  " + 
"0.0004993766531625746" + 
":  " + 
"(b('trees') <= 8.635247230529785) ? " + 
"0.005558974442494749" + 
":  " + 
"-0.00041347493471083666" + 
":  " + 
"(b('svvk3') <= 0.012301221489906311) ? " + 
"(b('svvk3') <= 0.012219839729368687) ? " + 
"-0.0008702367099642128" + 
":  " + 
"-0.015325264752687862" + 
":  " + 
"(b('L8b3med') <= 1593.5) ? " + 
"0.0006129702301434605" + 
":  " + 
"0.009684156983090914" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1242.0) ? " + 
"(b('L8b1med') <= 207.0) ? " + 
"(b('L8b7med') <= 924.5) ? " + 
"-0.003371785646765213" + 
":  " + 
"0.002013625491736948" + 
":  " + 
"(b('svvk3') <= -0.0003122568215303545) ? " + 
"-0.003292567286659461" + 
":  " + 
"-0.0018587001774824918" + 
":  " + 
"(b('gvvk2') <= 0.5746753215789795) ? " + 
"(b('svvk3') <= 0.06443404033780098) ? " + 
"5.69932987329133e-05" + 
":  " + 
"-0.0014645733128737213" + 
":  " + 
"(b('gvvk2') <= 0.6470171213150024) ? " + 
"0.004382867046914313" + 
":  " + 
"-1.705319966898649e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('trees') <= 18.111291885375977) ? " + 
"(b('sand') <= 65.5) ? " + 
"0.0006867428851828043" + 
":  " + 
"-0.006067947636266467" + 
":  " + 
"(b('clay') <= 21.5) ? " + 
"-0.003142694666913977" + 
":  " + 
"-0.010093582353700156" + 
":  " + 
"(b('trees') <= 17.942265510559082) ? " + 
"(b('trees') <= 12.70752239227295) ? " + 
"5.7870089593945584e-05" + 
":  " + 
"-0.0013954946106134176" + 
":  " + 
"(b('L8b2med') <= 445.75) ? " + 
"-0.0022046121964376564" + 
":  " + 
"0.0026552360437000783" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 24.250454902648926) ? " + 
"(b('L8b6med') <= 2540.5) ? " + 
"-0.0004766152301596859" + 
":  " + 
"0.0001534591105286639" + 
":  " + 
"(b('gvvk2') <= 0.15660593658685684) ? " + 
"0.005691120690477017" + 
":  " + 
"-0.004063063491285693" + 
":  " + 
"(b('L8b1med') <= 321.0) ? " + 
"-0.0011375610692585525" + 
":  " + 
"(b('L8b2med') <= 431.25) ? " + 
"0.006016602552861183" + 
":  " + 
"0.004147447069665702" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('trees') <= 9.420434951782227) ? " + 
"-0.0003729948013668613" + 
":  " + 
"0.0005591811171367637" + 
":  " + 
"-0.017315520587847535" + 
":  " + 
"(b('gvvk2') <= 0.4510953277349472) ? " + 
"(b('svvk3') <= 0.05881730653345585) ? " + 
"0.009533204817853733" + 
":  " + 
"0.0034998386841745555" + 
":  " + 
"(b('L8b2med') <= 887.0) ? " + 
"0.0006572669756627152" + 
":  " + 
"-0.003571338634377756" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"(b('svvk3') <= 0.002330337418243289) ? " + 
"-0.0007712223447530198" + 
":  " + 
"-0.006240226842489871" + 
":  " + 
"(b('ndvi_med') <= 750.75) ? " + 
"(b('L8b2med') <= 1319.75) ? " + 
"0.008366157131605753" + 
":  " + 
"0.0014925824526777765" + 
":  " + 
"(b('ndvi_med') <= 757.25) ? " + 
"-0.005432233062431166" + 
":  " + 
"1.37193926840648e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -121.75626754760742) ? " + 
"(b('svvk3') <= 0.0341707244515419) ? " + 
"(b('svvk3') <= 0.013526610797271132) ? " + 
"-0.002001404109624641" + 
":  " + 
"0.0014692362203722747" + 
":  " + 
"-0.007968207497442426" + 
":  " + 
"(b('lon') <= -121.29663467407227) ? " + 
"(b('L8b3med') <= 1389.5) ? " + 
"0.004049252633131527" + 
":  " + 
"0.0006861026501226442" + 
":  " + 
"(b('lon') <= -120.94869613647461) ? " + 
"-0.0026662220262672087" + 
":  " + 
"3.5735832970206674e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -71.2344970703125) ? " + 
"(b('lon') <= -77.86024856567383) ? " + 
"(b('L8b3med') <= 622.0) ? " + 
"-0.0039049226311889283" + 
":  " + 
"0.0001257674571739098" + 
":  " + 
"(b('L8b6med') <= 2049.5) ? " + 
"-0.002245265895215731" + 
":  " + 
"0.0067947403218421255" + 
":  " + 
"(b('svvk3') <= 0.012301221489906311) ? " + 
"(b('svvk3') <= 0.012219839729368687) ? " + 
"-0.000853887794923193" + 
":  " + 
"-0.013785981824391808" + 
":  " + 
"(b('bulk') <= 151.5) ? " + 
"0.0005189331421904435" + 
":  " + 
"0.008854058066782758" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2468.0) ? " + 
"(b('L8b7med') <= 2342.0) ? " + 
"(b('L8b6med') <= 3489.5) ? " + 
"0.00012359438247299006" + 
":  " + 
"-0.002948890369390958" + 
":  " + 
"(b('L8b6med') <= 3812.5) ? " + 
"0.0035086179824129287" + 
":  " + 
"-0.00754016325975293" + 
":  " + 
"(b('L8b7med') <= 2473.5) ? " + 
"-0.012140507791510602" + 
":  " + 
"(b('gvvk2') <= 0.15030024200677872) ? " + 
"0.0028931032030142193" + 
":  " + 
"-0.0006304640898440048" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('trees') <= 18.111291885375977) ? " + 
"(b('L8b6med') <= 2978.25) ? " + 
"0.002207372760008752" + 
":  " + 
"-0.001603139142336072" + 
":  " + 
"(b('gvvk2') <= 0.12108727544546127) ? " + 
"-0.0029283361841776837" + 
":  " + 
"-0.009184135102285232" + 
":  " + 
"(b('sand') <= 14.5) ? " + 
"(b('sand') <= 13.0) ? " + 
"0.0005718928399543882" + 
":  " + 
"0.011405970359286977" + 
":  " + 
"(b('sand') <= 19.0) ? " + 
"-0.003339165265057707" + 
":  " + 
"7.969742272437764e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('ndvi_med') <= 4452.5) ? " + 
"(b('svvk3') <= -0.023769686929881573) ? " + 
"2.1941225307619233e-05" + 
":  " + 
"-0.003760524537924118" + 
":  " + 
"(b('L8b6med') <= 2378.5) ? " + 
"8.935273484922401e-05" + 
":  " + 
"-0.007049007647757358" + 
":  " + 
"(b('svvk3') <= -0.0181471798568964) ? " + 
"(b('trees') <= 19.219488620758057) ? " + 
"0.005260396890692215" + 
":  " + 
"-0.004989047619319703" + 
":  " + 
"(b('L8b7med') <= 2573.5) ? " + 
"0.00019794303883360982" + 
":  " + 
"-0.0007239905932994488" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 38.950599670410156) ? " + 
"(b('lat') <= 38.14986991882324) ? " + 
"(b('L8b6med') <= 2618.0) ? " + 
"0.0045311878788630135" + 
":  " + 
"-0.00021762022933344085" + 
":  " + 
"(b('L8b1med') <= 816.75) ? " + 
"0.007773451084816214" + 
":  " + 
"-0.013095307674795456" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"(b('bulk') <= 137.5) ? " + 
"-0.00018647766292290713" + 
":  " + 
"0.0017887998193395443" + 
":  " + 
"(b('L8b6med') <= 2994.75) ? " + 
"-0.002597237940995074" + 
":  " + 
"0.0001959966810733086" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.038837023079395294) ? " + 
"(b('ndvi_med') <= 3155.5) ? " + 
"-0.0015520871963662919" + 
":  " + 
"-0.005764793083787745" + 
":  " + 
"(b('gvvk2') <= 0.041203947737812996) ? " + 
"0.005643723008975032" + 
":  " + 
"(b('sand') <= 14.5) ? " + 
"0.0024079628805568688" + 
":  " + 
"-2.547090204325019e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('L8b3med') <= 836.5) ? " + 
"(b('gvvk2') <= 0.03510967455804348) ? " + 
"-0.001396878476729646" + 
":  " + 
"-0.006724760279105679" + 
":  " + 
"(b('L8b6med') <= 2978.25) ? " + 
"0.002075531431364394" + 
":  " + 
"-0.0017835698170709606" + 
":  " + 
"(b('lat') <= 39.55443000793457) ? " + 
"(b('bulk') <= 151.5) ? " + 
"0.0012911272275312354" + 
":  " + 
"-0.0007740988655719804" + 
":  " + 
"(b('lat') <= 41.189334869384766) ? " + 
"-0.002174868909461185" + 
":  " + 
"5.617006687320955e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 253.5) ? " + 
"(b('L8b2med') <= 305.5) ? " + 
"(b('gvvk2') <= 0.39189615845680237) ? " + 
"0.003487495937829025" + 
":  " + 
"-0.001955841274478796" + 
":  " + 
"(b('ndvi_med') <= 4581.5) ? " + 
"-0.0032192475230114798" + 
":  " + 
"-0.0001015324370526316" + 
":  " + 
"(b('L8b2med') <= 331.5) ? " + 
"(b('gvvk2') <= 0.36731019616127014) ? " + 
"0.0055850671836081694" + 
":  " + 
"-0.0007554659880212311" + 
":  " + 
"(b('lat') <= 56.03929901123047) ? " + 
"-1.1145608412046552e-05" + 
":  " + 
"0.003004500610808633" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2340.5) ? " + 
"(b('L8b6med') <= 2201.75) ? " + 
"(b('L8b7med') <= 1734.25) ? " + 
"-0.00036415279526742057" + 
":  " + 
"0.002908698879344735" + 
":  " + 
"(b('L8b7med') <= 1374.75) ? " + 
"0.00019099284512924728" + 
":  " + 
"-0.003754873277669711" + 
":  " + 
"(b('L8b7med') <= 1510.0) ? " + 
"(b('lon') <= -101.66166687011719) ? " + 
"0.012665152882047337" + 
":  " + 
"0.001022923113261735" + 
":  " + 
"(b('L8b7med') <= 1527.25) ? " + 
"-0.003357778021308086" + 
":  " + 
"2.6246729715546925e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('L8b6med') <= 3674.5) ? " + 
"-0.0002103948678931087" + 
":  " + 
"0.001097100413619893" + 
":  " + 
"-0.015385235770920977" + 
":  " + 
"(b('gvvk2') <= 0.46257317066192627) ? " + 
"(b('L8b7med') <= 1969.0) ? " + 
"0.0009329264605483917" + 
":  " + 
"0.0076091243485479285" + 
":  " + 
"(b('trees') <= 9.015841007232666) ? " + 
"0.0007968387373307642" + 
":  " + 
"-0.0017297674300869696" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3782.0) ? " + 
"(b('ndvi_med') <= 3762.25) ? " + 
"(b('svvk3') <= 0.018222343176603317) ? " + 
"0.0001785674585457502" + 
":  " + 
"-0.0006532805203601844" + 
":  " + 
"-0.01173945484194644" + 
":  " + 
"(b('bulk') <= 110.0) ? " + 
"(b('svvk3') <= 0.010467188665643334) ? " + 
"-0.004099051680082459" + 
":  " + 
"0.0025452330906786946" + 
":  " + 
"(b('L8b6med') <= 2915.5) ? " + 
"0.00023199215184508952" + 
":  " + 
"0.0030755790230632407" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.007805905770510435) ? " + 
"(b('svvk3') <= 0.007316778646782041) ? " + 
"(b('L8b2med') <= 490.0) ? " + 
"0.0008243006541999325" + 
":  " + 
"-0.0005444454340311112" + 
":  " + 
"(b('clay') <= 16.5) ? " + 
"-0.01362589055999891" + 
":  " + 
"-0.007377475491070151" + 
":  " + 
"(b('svvk3') <= 0.018222343176603317) ? " + 
"(b('gvvk2') <= 0.3129253685474396) ? " + 
"-0.0005060948954342119" + 
":  " + 
"0.0038698848761847754" + 
":  " + 
"(b('sand') <= 16.5) ? " + 
"-0.014436619423822461" + 
":  " + 
"-0.00018365344005588963" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('L8b1med') <= 518.25) ? " + 
"(b('svvk3') <= -0.06071034446358681) ? " + 
"0.0009103205170252032" + 
":  " + 
"-0.003207129521264888" + 
":  " + 
"(b('gvvk2') <= 0.36643101274967194) ? " + 
"0.005178999735591693" + 
":  " + 
"-0.0005477674267227574" + 
":  " + 
"(b('svvk3') <= -0.0181471798568964) ? " + 
"(b('L8b2med') <= 446.0) ? " + 
"-0.004660332551878615" + 
":  " + 
"0.004755989889192597" + 
":  " + 
"(b('L8b7med') <= 2573.5) ? " + 
"0.0002021978856665976" + 
":  " + 
"-0.0007234786103190107" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1312.0) ? " + 
"(b('L8b3med') <= 1222.0) ? " + 
"(b('L8b1med') <= 641.0) ? " + 
"-3.611395897687997e-05" + 
":  " + 
"0.0025690073803628396" + 
":  " + 
"(b('L8b2med') <= 694.0) ? " + 
"0.007707289719935673" + 
":  " + 
"-0.004116707632297613" + 
":  " + 
"(b('L8b3med') <= 1330.0) ? " + 
"(b('lat') <= 36.81332969665527) ? " + 
"0.015063328455900082" + 
":  " + 
"0.005063144005251666" + 
":  " + 
"(b('ndvi_med') <= 1771.0) ? " + 
"-0.0002536745965035919" + 
":  " + 
"0.005009276524485763" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2540.5) ? " + 
"(b('L8b6med') <= 2471.5) ? " + 
"(b('L8b7med') <= 1420.5) ? " + 
"-0.0011332029308464405" + 
":  " + 
"0.0009482642636812572" + 
":  " + 
"(b('svvk3') <= 0.0009706658020149916) ? " + 
"0.0002299041493197141" + 
":  " + 
"-0.007217062318091179" + 
":  " + 
"(b('L8b6med') <= 2602.5) ? " + 
"(b('trees') <= 19.97240161895752) ? " + 
"0.0034964290927150003" + 
":  " + 
"-0.001973416197441654" + 
":  " + 
"(b('L8b6med') <= 2642.0) ? " + 
"-0.0038561775598636053" + 
":  " + 
"2.746107585183499e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3782.0) ? " + 
"(b('ndvi_med') <= 3762.25) ? " + 
"(b('sand') <= 53.5) ? " + 
"0.0001266257833680785" + 
":  " + 
"-0.0007234826803109201" + 
":  " + 
"-0.01052794781777619" + 
":  " + 
"(b('bulk') <= 110.0) ? " + 
"(b('svvk3') <= 0.010467188665643334) ? " + 
"-0.003560621601278041" + 
":  " + 
"0.0020895152063768463" + 
":  " + 
"(b('L8b6med') <= 2915.5) ? " + 
"0.00024680086326955874" + 
":  " + 
"0.0027960507789025323" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1312.0) ? " + 
"(b('L8b3med') <= 1252.5) ? " + 
"(b('gvvk2') <= 0.13522601872682571) ? " + 
"-0.0015299599117534622" + 
":  " + 
"0.00010044862061911095" + 
":  " + 
"(b('L8b7med') <= 2543.75) ? " + 
"-0.0010830757758525066" + 
":  " + 
"-0.006001462795444636" + 
":  " + 
"(b('L8b3med') <= 1330.0) ? " + 
"(b('L8b1med') <= 759.0) ? " + 
"0.004584012596504702" + 
":  " + 
"0.013544058421214727" + 
":  " + 
"(b('ndvi_med') <= 1771.0) ? " + 
"-0.00018547927894086764" + 
":  " + 
"0.004552085580520458" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1052.0) ? " + 
"(b('L8b7med') <= 2115.5) ? " + 
"(b('L8b7med') <= 2076.5) ? " + 
"-0.00013342534116505446" + 
":  " + 
"0.00664284339366486" + 
":  " + 
"(b('L8b7med') <= 2191.5) ? " + 
"-0.0040269917603421735" + 
":  " + 
"-0.0003725242223969018" + 
":  " + 
"(b('trees') <= 12.48423957824707) ? " + 
"(b('trees') <= 11.904761791229248) ? " + 
"0.00025996240072463016" + 
":  " + 
"-0.011424147716672856" + 
":  " + 
"(b('svvk3') <= -0.007827509194612503) ? " + 
"-0.0009524274442710076" + 
":  " + 
"0.0058526882445906064" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('L8b6med') <= 2135.5) ? " + 
"(b('L8b7med') <= 1267.5) ? " + 
"-0.0021663436788490337" + 
":  " + 
"0.0038491479091328634" + 
":  " + 
"(b('L8b7med') <= 2413.5) ? " + 
"-0.0022575857136582647" + 
":  " + 
"0.0013471021901077574" + 
":  " + 
"(b('L8b6med') <= 2340.5) ? " + 
"(b('bulk') <= 135.5) ? " + 
"-0.00010454365877440298" + 
":  " + 
"-0.0031533001270083014" + 
":  " + 
"(b('L8b6med') <= 2454.25) ? " + 
"0.0020183755738023266" + 
":  " + 
"3.028973945602376e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.04165135137736797) ? " + 
"(b('svvk3') <= 0.04113762825727463) ? " + 
"(b('svvk3') <= 0.030742689967155457) ? " + 
"-7.666535264419947e-05" + 
":  " + 
"0.0014462698725653416" + 
":  " + 
"(b('ndvi_med') <= 2682.5) ? " + 
"0.013049530714702329" + 
":  " + 
"0.0027843042834263254" + 
":  " + 
"(b('svvk3') <= 0.04575645551085472) ? " + 
"(b('svvk3') <= 0.04354680888354778) ? " + 
"-0.003766698727678555" + 
":  " + 
"-0.007159949844666054" + 
":  " + 
"(b('L8b3med') <= 1490.0) ? " + 
"0.0004206577907272096" + 
":  " + 
"-0.004924265358754471" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= 1.4101499915122986) ? " + 
"(b('L8b3med') <= 701.75) ? " + 
"-0.0021172877791003214" + 
":  " + 
"0.00023064400259515205" + 
":  " + 
"0.011638080048593236" + 
":  " + 
"(b('lon') <= 6.412564992904663) ? " + 
"(b('svvk3') <= 0.002975506125949323) ? " + 
"-0.001838522683140241" + 
":  " + 
"-0.006705108979001617" + 
":  " + 
"(b('gvvk2') <= 0.2746471166610718) ? " + 
"0.0009965309584715342" + 
":  " + 
"-0.0006235400968769904" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3678.75) ? " + 
"(b('L8b7med') <= 1587.0) ? " + 
"(b('L8b2med') <= 418.5) ? " + 
"-0.00078017097201147" + 
":  " + 
"0.0027626020365615696" + 
":  " + 
"(b('ndvi_med') <= 2473.5) ? " + 
"0.00015971487357636203" + 
":  " + 
"-0.0017458722737357783" + 
":  " + 
"(b('L8b7med') <= 1666.75) ? " + 
"(b('L8b7med') <= 1658.75) ? " + 
"-0.0004548533903790586" + 
":  " + 
"-0.012234575350692334" + 
":  " + 
"(b('L8b7med') <= 1688.5) ? " + 
"0.010224564932093718" + 
":  " + 
"0.0009874386662059595" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 34.5) ? " + 
"(b('gvvk2') <= 0.5458730161190033) ? " + 
"(b('gvvk2') <= 0.5375914573669434) ? " + 
"4.185363872061073e-06" + 
":  " + 
"-0.006446099215597342" + 
":  " + 
"(b('lon') <= -103.03784942626953) ? " + 
"0.0058044922688614735" + 
":  " + 
"0.00037787466172246035" + 
":  " + 
"(b('bulk') <= 151.5) ? " + 
"(b('L8b6med') <= 2094.0) ? " + 
"0.003297660169886585" + 
":  " + 
"-0.0013387193521992222" + 
":  " + 
"-0.00722633065173614" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('trees') <= 18.111291885375977) ? " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.005232521012025593" + 
":  " + 
"-0.00047920865841061825" + 
":  " + 
"(b('L8b3med') <= 859.0) ? " + 
"-0.006092772660706427" + 
":  " + 
"-0.001954438753489024" + 
":  " + 
"(b('trees') <= 17.942265510559082) ? " + 
"(b('L8b1med') <= 356.0) ? " + 
"0.0007178393273351844" + 
":  " + 
"-0.000258139812373022" + 
":  " + 
"(b('L8b3med') <= 791.25) ? " + 
"-0.0005262285520728243" + 
":  " + 
"0.003229162996925226" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 33.60975933074951) ? " + 
"(b('trees') <= 24.250454902648926) ? " + 
"(b('L8b3med') <= 911.0) ? " + 
"-0.0002195889591258872" + 
":  " + 
"0.00023380277814950503" + 
":  " + 
"(b('L8b6med') <= 2512.0) ? " + 
"0.004789928086728137" + 
":  " + 
"-0.0036061466929812437" + 
":  " + 
"(b('lat') <= 39.09149932861328) ? " + 
"-0.000503451937738153" + 
":  " + 
"0.0040692508152342585" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= 1.4101499915122986) ? " + 
"8.498389393899722e-05" + 
":  " + 
"0.010696213611870148" + 
":  " + 
"(b('lon') <= 5.194149971008301) ? " + 
"-0.006190666132296939" + 
":  " + 
"-0.00040541436825004194" + 
":  " + 
"(b('gvvk2') <= 0.36731019616127014) ? " + 
"(b('L8b7med') <= 1568.5) ? " + 
"0.005878414685457634" + 
":  " + 
"0.002574024184910706" + 
":  " + 
"(b('L8b2med') <= 605.0) ? " + 
"0.00026647617617991997" + 
":  " + 
"0.003214926363559932" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2468.0) ? " + 
"(b('L8b7med') <= 2447.0) ? " + 
"(b('L8b1med') <= 641.0) ? " + 
"-5.506580808452707e-05" + 
":  " + 
"0.0022578428047481474" + 
":  " + 
"(b('sand') <= 48.0) ? " + 
"0.004205841613296346" + 
":  " + 
"0.011699058533256174" + 
":  " + 
"(b('L8b7med') <= 2473.5) ? " + 
"-0.010718784772927786" + 
":  " + 
"(b('gvvk2') <= 0.15030024200677872) ? " + 
"0.002603547044193878" + 
":  " + 
"-0.000550322723937201" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"(b('gvvk2') <= 0.1353890746831894) ? " + 
"-0.0006950716536802126" + 
":  " + 
"-0.005617175701643377" + 
":  " + 
"(b('ndvi_med') <= 750.75) ? " + 
"(b('L8b2med') <= 1319.75) ? " + 
"0.007764836713718137" + 
":  " + 
"0.0013466837431304081" + 
":  " + 
"(b('L8b2med') <= 1281.5) ? " + 
"3.141267309308674e-05" + 
":  " + 
"-0.0019946088808134046" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('lat') <= 49.570478439331055) ? " + 
"(b('bulk') <= 140.0) ? " + 
"-0.007422841738019714" + 
":  " + 
"-0.0006479702978141162" + 
":  " + 
"(b('gvvk2') <= 0.4046826511621475) ? " + 
"-0.0026802902874981244" + 
":  " + 
"0.0007556394374893619" + 
":  " + 
"(b('svvk3') <= -0.00043326523154973984) ? " + 
"(b('svvk3') <= -0.0005696050066035241) ? " + 
"0.0004420086582106934" + 
":  " + 
"0.013333033214905032" + 
":  " + 
"(b('svvk3') <= -0.0003453021345194429) ? " + 
"-0.011520891822947604" + 
":  " + 
"-5.4069068484283464e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('trees') <= 18.111291885375977) ? " + 
"(b('svvk3') <= 0.0008524811128154397) ? " + 
"0.00036989577563036817" + 
":  " + 
"-0.005165221813949371" + 
":  " + 
"(b('sand') <= 45.0) ? " + 
"-0.004178993044402467" + 
":  " + 
"0.0004874820407941155" + 
":  " + 
"(b('trees') <= 17.942265510559082) ? " + 
"(b('L8b1med') <= 356.0) ? " + 
"0.0006844570542921415" + 
":  " + 
"-0.00024092960595250288" + 
":  " + 
"(b('L8b3med') <= 791.25) ? " + 
"-0.0004696824275082832" + 
":  " + 
"0.002946841847354007" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 1.3649256229400635) ? " + 
"(b('svvk3') <= 0.014892799779772758) ? " + 
"(b('svvk3') <= 0.008253635838627815) ? " + 
"6.179955958460215e-05" + 
":  " + 
"0.0035704227518042653" + 
":  " + 
"(b('svvk3') <= 0.02459165919572115) ? " + 
"-0.003188611388453749" + 
":  " + 
"0.0004725533401296953" + 
":  " + 
"(b('trees') <= 3.7982627153396606) ? " + 
"(b('L8b6med') <= 3009.5) ? " + 
"-0.004370518036314762" + 
":  " + 
"0.0007386590494277436" + 
":  " + 
"(b('svvk3') <= 0.012301221489906311) ? " + 
"-0.0003749967775117141" + 
":  " + 
"0.0010291719154682498" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.04165135137736797) ? " + 
"(b('svvk3') <= 0.03547702915966511) ? " + 
"(b('svvk3') <= 0.018222343176603317) ? " + 
"0.00012300940020750214" + 
":  " + 
"-0.0009207547564645946" + 
":  " + 
"(b('bulk') <= 148.0) ? " + 
"0.001316139233786271" + 
":  " + 
"0.010752908378736561" + 
":  " + 
"(b('svvk3') <= 0.04575645551085472) ? " + 
"(b('svvk3') <= 0.04354680888354778) ? " + 
"-0.003390859440981798" + 
":  " + 
"-0.006446830834920064" + 
":  " + 
"(b('L8b3med') <= 1490.0) ? " + 
"0.0003314536924236592" + 
":  " + 
"-0.004491388524348588" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('clay') <= 34.5) ? " + 
"(b('clay') <= 32.5) ? " + 
"(b('clay') <= 30.5) ? " + 
"5.6347337267310035e-05" + 
":  " + 
"-0.002066497216457059" + 
":  " + 
"(b('L8b3med') <= 981.0) ? " + 
"0.00430205794210235" + 
":  " + 
"-0.0006658136834700156" + 
":  " + 
"(b('bulk') <= 151.5) ? " + 
"(b('L8b6med') <= 2094.0) ? " + 
"0.0029395820750202084" + 
":  " + 
"-0.0012467815615219582" + 
":  " + 
"-0.006387737776230223" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.027715977281332016) ? " + 
"(b('lon') <= 8.928900241851807) ? " + 
"(b('clay') <= 22.5) ? " + 
"-0.0029343884690076205" + 
":  " + 
"0.0005716629843351392" + 
":  " + 
"(b('lon') <= 8.984700202941895) ? " + 
"0.0033331732708728606" + 
":  " + 
"0.0009440623961586939" + 
":  " + 
"(b('lon') <= -5.510674953460693) ? " + 
"(b('lon') <= -82.97315216064453) ? " + 
"6.0883352984156566e-05" + 
":  " + 
"0.0025153100364345973" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"-0.0034417658003951844" + 
":  " + 
"-6.898088238163229e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3674.5) ? " + 
"(b('L8b6med') <= 3657.5) ? " + 
"(b('L8b6med') <= 3497.75) ? " + 
"9.44402765641578e-05" + 
":  " + 
"-0.000875990415632831" + 
":  " + 
"(b('gvvk2') <= 0.49324287474155426) ? " + 
"-0.010275807995970651" + 
":  " + 
"-9.66123209362596e-05" + 
":  " + 
"(b('gvvk2') <= 0.41474783420562744) ? " + 
"(b('L8b6med') <= 3825.25) ? " + 
"0.0026501987042560032" + 
":  " + 
"0.00012316777470906026" + 
":  " + 
"(b('gvvk2') <= 0.4885784983634949) ? " + 
"-0.004088033926874748" + 
":  " + 
"-0.0008388054049432584" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b1med') <= 613.5) ? " + 
"(b('L8b1med') <= 606.75) ? " + 
"-3.0385254847007773e-05" + 
":  " + 
"0.004039179274958986" + 
":  " + 
"(b('svvk3') <= -0.008416643599048257) ? " + 
"-0.007588677828319852" + 
":  " + 
"-0.0011493878530883276" + 
":  " + 
"(b('L8b7med') <= 2269.0) ? " + 
"(b('ndvi_med') <= 1622.0) ? " + 
"0.002297075928389095" + 
":  " + 
"0.01633117524585348" + 
":  " + 
"(b('ndvi_med') <= 1369.0) ? " + 
"-0.0008423535996307483" + 
":  " + 
"0.001207863194240326" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 911.0) ? " + 
"(b('L8b1med') <= 459.5) ? " + 
"(b('L8b1med') <= 455.75) ? " + 
"4.260877590025212e-05" + 
":  " + 
"0.008969108755545296" + 
":  " + 
"(b('L8b3med') <= 867.5) ? " + 
"-0.00038271737618594104" + 
":  " + 
"-0.004204702878944545" + 
":  " + 
"(b('L8b2med') <= 530.75) ? " + 
"(b('gvvk2') <= 0.37580204010009766) ? " + 
"-0.009688510282410662" + 
":  " + 
"0.001632382500828422" + 
":  " + 
"(b('L8b1med') <= 429.0) ? " + 
"0.004755364243488001" + 
":  " + 
"0.00015276154565768208" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= 0.06443404033780098) ? " + 
"(b('svvk3') <= 0.0628238171339035) ? " + 
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"-0.00011455654131608596" + 
":  " + 
"0.0009168012221279916" + 
":  " + 
"0.012297755896039708" + 
":  " + 
"(b('gvvk2') <= 0.37841586768627167) ? " + 
"(b('gvvk2') <= 0.3512052297592163) ? " + 
"0.004226533475421748" + 
":  " + 
"0.005466190630126669" + 
":  " + 
"(b('sand') <= 46.5) ? " + 
"-0.00295765954017448" + 
":  " + 
"7.546641261670881e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2340.5) ? " + 
"(b('bulk') <= 135.5) ? " + 
"(b('ndvi_med') <= 1394.25) ? " + 
"-0.004102857232392028" + 
":  " + 
"0.00034909072716557063" + 
":  " + 
"(b('bulk') <= 137.5) ? " + 
"-0.005817744380863628" + 
":  " + 
"-0.001172250503778707" + 
":  " + 
"(b('L8b7med') <= 1510.0) ? " + 
"(b('lon') <= -96.73815155029297) ? " + 
"0.007845172184951926" + 
":  " + 
"0.000720498925326505" + 
":  " + 
"(b('L8b7med') <= 1527.25) ? " + 
"-0.0028239027544001913" + 
":  " + 
"2.8222605218154633e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('L8b1med') <= 518.25) ? " + 
"(b('svvk3') <= -0.06071034446358681) ? " + 
"0.0006234615781064676" + 
":  " + 
"-0.002744413225214615" + 
":  " + 
"(b('gvvk2') <= 0.36643101274967194) ? " + 
"0.004321610356849341" + 
":  " + 
"-0.0003792988957053958" + 
":  " + 
"(b('svvk3') <= -0.01786497700959444) ? " + 
"(b('L8b1med') <= 671.5) ? " + 
"0.0014677212176561853" + 
":  " + 
"0.01004169127837734" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.002393152914557885" + 
":  " + 
"6.921045508839382e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 2961.25) ? " + 
"(b('L8b7med') <= 2056.25) ? " + 
"(b('L8b7med') <= 1588.5) ? " + 
"0.0011950009212710454" + 
":  " + 
"-0.0013982312513748417" + 
":  " + 
"(b('L8b7med') <= 2116.0) ? " + 
"0.005860317816628227" + 
":  " + 
"-0.00013120243270406685" + 
":  " + 
"(b('ndvi_med') <= 3068.25) ? " + 
"(b('gvvk2') <= 0.2798030525445938) ? " + 
"-0.0014102482494187329" + 
":  " + 
"0.0073473802232211505" + 
":  " + 
"(b('svvk3') <= -0.0018054947722703218) ? " + 
"0.0011129616728295553" + 
":  " + 
"-0.0003945316489688744" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('L8b3med') <= 747.0) ? " + 
"(b('bulk') <= 130.5) ? " + 
"0.0027714279358332836" + 
":  " + 
"8.844692797678928e-05" + 
":  " + 
"(b('L8b1med') <= 518.25) ? " + 
"-0.002073498418709338" + 
":  " + 
"0.0006589809543998555" + 
":  " + 
"(b('svvk3') <= -0.01786497700959444) ? " + 
"(b('ndvi_med') <= 4896.0) ? " + 
"0.0035612551892754882" + 
":  " + 
"-0.004305613292935856" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.00224958173906588" + 
":  " + 
"7.159477458500716e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 1922.0) ? " + 
"(b('L8b2med') <= 336.0) ? " + 
"-0.0026363522928366245" + 
":  " + 
"-0.0013833924948866566" + 
":  " + 
"(b('L8b7med') <= 1627.5) ? " + 
"(b('gvvk2') <= 0.42064596712589264) ? " + 
"0.0008235535657079411" + 
":  " + 
"-0.001496648081550125" + 
":  " + 
"(b('L8b7med') <= 1634.75) ? " + 
"-0.008765033333578398" + 
":  " + 
"-1.6815306850974206e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 39.55443000793457) ? " + 
"(b('lat') <= 38.14833068847656) ? " + 
"(b('lat') <= 38.12168502807617) ? " + 
"0.00017423612610674853" + 
":  " + 
"-0.0054416172189011" + 
":  " + 
"(b('gvvk2') <= 0.45409491658210754) ? " + 
"0.0010976186828657432" + 
":  " + 
"0.012385667613845186" + 
":  " + 
"(b('ndvi_med') <= 3324.0) ? " + 
"(b('trees') <= 1.0861334204673767) ? " + 
"0.00011666162706190174" + 
":  " + 
"-0.0014759643483102257" + 
":  " + 
"(b('L8b6med') <= 2855.0) ? " + 
"-0.00011624227229645199" + 
":  " + 
"0.0024417919789842552" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 6132.5) ? " + 
"(b('ndvi_med') <= 5941.25) ? " + 
"(b('svvk3') <= -0.010644129011780024) ? " + 
"-0.0005971081750514484" + 
":  " + 
"9.19479075054887e-05" + 
":  " + 
"(b('L8b7med') <= 2025.5) ? " + 
"0.01079916314042284" + 
":  " + 
"0.00048662700542523307" + 
":  " + 
"(b('gvvk2') <= 0.1478906273841858) ? " + 
"-0.001269385270835699" + 
":  " + 
"(b('L8b7med') <= 2100.0) ? " + 
"-0.0026159266095318046" + 
":  " + 
"-0.003461378404673976" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 53.5) ? " + 
"(b('svvk3') <= 0.018222343176603317) ? " + 
"(b('svvk3') <= 0.01235300675034523) ? " + 
"5.005510219317894e-05" + 
":  " + 
"0.0029503473326026306" + 
":  " + 
"(b('sand') <= 16.5) ? " + 
"-0.012466890903502614" + 
":  " + 
"-0.00040052514499576024" + 
":  " + 
"(b('svvk3') <= 0.02197057567536831) ? " + 
"(b('gvvk2') <= 0.26820625364780426) ? " + 
"0.0006501287920706661" + 
":  " + 
"-0.0018865899375926432" + 
":  " + 
"(b('svvk3') <= 0.05512472987174988) ? " + 
"0.0024930158481705307" + 
":  " + 
"-0.00019329992191865423" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('sand') <= 70.5) ? " + 
"(b('svvk3') <= -0.010644129011780024) ? " + 
"-0.0006300145564442618" + 
":  " + 
"0.0001284195180068088" + 
":  " + 
"(b('gvvk2') <= 0.36231255531311035) ? " + 
"-0.003899535672253473" + 
":  " + 
"-0.0001945486354452223" + 
":  " + 
"(b('gvvk2') <= 0.36731019616127014) ? " + 
"(b('bulk') <= 128.0) ? " + 
"0.002591058656305434" + 
":  " + 
"0.005187755424912843" + 
":  " + 
"(b('gvvk2') <= 0.41833437979221344) ? " + 
"-0.0005908514718666324" + 
":  " + 
"0.001218377638060389" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 415.0) ? " + 
"(b('svvk3') <= 0.002330337418243289) ? " + 
"-0.0006018646289152434" + 
":  " + 
"-0.005031758272082083" + 
":  " + 
"(b('ndvi_med') <= 750.75) ? " + 
"(b('L8b2med') <= 1407.0) ? " + 
"0.003570244948696087" + 
":  " + 
"-0.0003402498551839152" + 
":  " + 
"(b('ndvi_med') <= 757.25) ? " + 
"-0.00433712335690082" + 
":  " + 
"2.5931667959645884e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 6132.5) ? " + 
"(b('ndvi_med') <= 5941.25) ? " + 
"(b('lon') <= 9.210049629211426) ? " + 
"7.903603531576391e-05" + 
":  " + 
"-0.0005891986950736549" + 
":  " + 
"(b('ndvi_med') <= 6002.25) ? " + 
"0.009970647959104628" + 
":  " + 
"0.0006514437338842327" + 
":  " + 
"(b('lat') <= 53.63138008117676) ? " + 
"-0.0012205608914394594" + 
":  " + 
"(b('lat') <= 53.63241958618164) ? " + 
"-0.002432448096265971" + 
":  " + 
"-0.0031933547118939143" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 2961.25) ? " + 
"(b('ndvi_med') <= 2473.0) ? " + 
"(b('svvk3') <= 0.017449820414185524) ? " + 
"0.0005417865593151986" + 
":  " + 
"-0.0006137066589872971" + 
":  " + 
"(b('L8b7med') <= 1613.0) ? " + 
"0.0014040854269179056" + 
":  " + 
"-0.002866235288192464" + 
":  " + 
"(b('L8b7med') <= 2054.5) ? " + 
"(b('L8b6med') <= 2855.0) ? " + 
"6.48446879990397e-06" + 
":  " + 
"0.0033853207650188137" + 
":  " + 
"(b('L8b3med') <= 837.5) ? " + 
"0.003033451718999193" + 
":  " + 
"-0.001997702682008249" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('L8b3med') <= 836.5) ? " + 
"(b('trees') <= 9.834983825683594) ? " + 
"-0.0012011956864746987" + 
":  " + 
"-0.005148814256738693" + 
":  " + 
"(b('L8b6med') <= 2978.25) ? " + 
"0.001718978867165147" + 
":  " + 
"-0.0015502540236694224" + 
":  " + 
"(b('trees') <= 17.942265510559082) ? " + 
"(b('trees') <= 15.571342945098877) ? " + 
"-1.8813658661982256e-06" + 
":  " + 
"-0.002401224454744439" + 
":  " + 
"(b('L8b2med') <= 445.75) ? " + 
"-0.001371341936858562" + 
":  " + 
"0.0018006571035374301" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('L8b7med') <= 1627.5) ? " + 
"0.00047157052536884065" + 
":  " + 
"-0.00025207219054148384" + 
":  " + 
"-0.013157372498929135" + 
":  " + 
"(b('gvvk2') <= 0.4510953277349472) ? " + 
"(b('svvk3') <= 0.05881730653345585) ? " + 
"0.0070841493001532335" + 
":  " + 
"0.0038085262583893442" + 
":  " + 
"(b('L8b2med') <= 887.0) ? " + 
"0.0005185703128889226" + 
":  " + 
"-0.002807025709676114" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 616.25) ? " + 
"(b('bulk') <= 112.0) ? " + 
"(b('svvk3') <= 0.0035718916915357113) ? " + 
"4.435559763030228e-05" + 
":  " + 
"0.003798408778122847" + 
":  " + 
"(b('svvk3') <= -0.0062428872915916145) ? " + 
"0.004613199599380169" + 
":  " + 
"-0.00188429747377134" + 
":  " + 
"(b('L8b3med') <= 618.5) ? " + 
"(b('svvk3') <= 0.03304598666727543) ? " + 
"0.0067889481729351275" + 
":  " + 
"0.0025053735012924294" + 
":  " + 
"(b('L8b6med') <= 2684.75) ? " + 
"0.0003858098581767833" + 
":  " + 
"-0.00015261185823858546" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 911.0) ? " + 
"(b('L8b1med') <= 524.75) ? " + 
"(b('L8b1med') <= 507.5) ? " + 
"-0.0001574828943969611" + 
":  " + 
"0.0050776967593613945" + 
":  " + 
"(b('gvvk2') <= 0.43681253492832184) ? " + 
"-0.004774189215581746" + 
":  " + 
"0.00020000407018789246" + 
":  " + 
"(b('L8b3med') <= 932.5) ? " + 
"(b('L8b6med') <= 2836.5) ? " + 
"0.01193198030629411" + 
":  " + 
"0.00039244753282432425" + 
":  " + 
"(b('trees') <= 6.040303707122803) ? " + 
"0.00039548371783550726" + 
":  " + 
"-0.0011253512598474837" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1179.0) ? " + 
"(b('ndvi_med') <= 1100.0) ? " + 
"(b('clay') <= 19.0) ? " + 
"0.0007713267117921334" + 
":  " + 
"-0.0018432276960613971" + 
":  " + 
"(b('L8b1med') <= 781.0) ? " + 
"-0.006396864743068192" + 
":  " + 
"-0.0034511014550596014" + 
":  " + 
"(b('ndvi_med') <= 1303.0) ? " + 
"(b('L8b6med') <= 2692.5) ? " + 
"0.010248159672669344" + 
":  " + 
"0.0008785811958541319" + 
":  " + 
"(b('ndvi_med') <= 1339.0) ? " + 
"-0.004187835114091545" + 
":  " + 
"3.775379460901015e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 38.950599670410156) ? " + 
"(b('lat') <= 38.14986991882324) ? " + 
"(b('svvk3') <= 0.005008715903386474) ? " + 
"-0.000812630088796845" + 
":  " + 
"0.0007310332183865837" + 
":  " + 
"(b('L8b1med') <= 816.75) ? " + 
"0.005768165946953143" + 
":  " + 
"-0.011372381428676956" + 
":  " + 
"(b('bulk') <= 141.5) ? " + 
"(b('bulk') <= 137.5) ? " + 
"-0.00017644794362568823" + 
":  " + 
"0.0014138108655441326" + 
":  " + 
"(b('L8b6med') <= 2994.75) ? " + 
"-0.0020695564201865086" + 
":  " + 
"0.000276722620688526" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 145.5) ? " + 
"(b('bulk') <= 141.5) ? " + 
"(b('lat') <= 38.14833068847656) ? " + 
"-0.002502344342027194" + 
":  " + 
"0.00020969104602997583" + 
":  " + 
"(b('svvk3') <= -0.008399092592298985) ? " + 
"-0.007178750012620272" + 
":  " + 
"-0.0006328269321437059" + 
":  " + 
"(b('lat') <= 44.67049980163574) ? " + 
"(b('lat') <= 42.23810577392578) ? " + 
"0.0003311271992798935" + 
":  " + 
"-0.004226407898293362" + 
":  " + 
"(b('L8b2med') <= 657.75) ? " + 
"0.013339325613279246" + 
":  " + 
"-0.004579425076319615" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 103.5) ? " + 
"(b('clay') <= 15.5) ? " + 
"(b('lon') <= -101.0928726196289) ? " + 
"-3.613470811826558e-05" + 
":  " + 
"-0.0011702301778412083" + 
":  " + 
"(b('ndvi_med') <= 4913.25) ? " + 
"-0.002632906492382875" + 
":  " + 
"-0.001892585483562803" + 
":  " + 
"(b('bulk') <= 105.5) ? " + 
"0.007990353573745834" + 
":  " + 
"(b('ndvi_med') <= 3678.75) ? " + 
"-9.356182900538449e-05" + 
":  " + 
"0.00041487498472808035" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('lon') <= 1.4101499915122986) ? " + 
"(b('L8b3med') <= 701.75) ? " + 
"-0.0017326785652134941" + 
":  " + 
"0.00019281289823424184" + 
":  " + 
"0.008128258801478272" + 
":  " + 
"(b('lon') <= 6.412564992904663) ? " + 
"(b('lat') <= 50.72260093688965) ? " + 
"-0.005543406614267686" + 
":  " + 
"-0.0013158281831307864" + 
":  " + 
"(b('gvvk2') <= 0.2746471166610718) ? " + 
"0.0008293021101433535" + 
":  " + 
"-0.0005218234393968634" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 9.210049629211426) ? " + 
"(b('lat') <= 32.18929862976074) ? " + 
"(b('sand') <= 63.5) ? " + 
"-0.003520979951902985" + 
":  " + 
"-0.0006752541678115599" + 
":  " + 
"(b('lon') <= -101.20384979248047) ? " + 
"-0.00017754145791972322" + 
":  " + 
"0.0004903615399183844" + 
":  " + 
"(b('svvk3') <= -0.009443551767617464) ? " + 
"(b('svvk3') <= -0.013376248069107533) ? " + 
"0.0008581742658469449" + 
":  " + 
"0.008639754412138934" + 
":  " + 
"(b('svvk3') <= 0.001219265366671607) ? " + 
"-0.0025154246489568865" + 
":  " + 
"-9.257274096418639e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 38.950599670410156) ? " + 
"(b('lat') <= 38.14986991882324) ? " + 
"(b('svvk3') <= 0.005008715903386474) ? " + 
"-0.0007123046772918728" + 
":  " + 
"0.000674786596496075" + 
":  " + 
"(b('L8b2med') <= 1027.5) ? " + 
"0.005183873921716958" + 
":  " + 
"-0.010260426966868172" + 
":  " + 
"(b('ndvi_med') <= 1303.0) ? " + 
"(b('svvk3') <= 0.0510970875620842) ? " + 
"0.0020202436237389343" + 
":  " + 
"-0.00550415131369647" + 
":  " + 
"(b('ndvi_med') <= 1360.5) ? " + 
"-0.002772839154424076" + 
":  " + 
"-0.00014746433366509193" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.038837023079395294) ? " + 
"(b('L8b1med') <= 319.5) ? " + 
"-0.0010098312376468077" + 
":  " + 
"-0.004547420299698818" + 
":  " + 
"(b('gvvk2') <= 0.041203947737812996) ? " + 
"0.003761831711557917" + 
":  " + 
"(b('L8b3med') <= 2799.0) ? " + 
"-4.492962378707215e-06" + 
":  " + 
"0.0036420273634375014" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.12847155332565308) ? " + 
"(b('L8b3med') <= 836.5) ? " + 
"(b('L8b7med') <= 1305.25) ? " + 
"-0.0009088481138821436" + 
":  " + 
"-0.004892763646566609" + 
":  " + 
"(b('ndvi_med') <= 585.5) ? " + 
"0.0040693852880897274" + 
":  " + 
"-0.0006073066880078651" + 
":  " + 
"(b('gvvk2') <= 0.13487395644187927) ? " + 
"(b('bulk') <= 135.5) ? " + 
"-0.005933349945272948" + 
":  " + 
"0.003047341988082706" + 
":  " + 
"(b('gvvk2') <= 0.13522601872682571) ? " + 
"-0.0075101370447146765" + 
":  " + 
"2.4819005447492545e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1179.0) ? " + 
"(b('ndvi_med') <= 1100.0) ? " + 
"(b('clay') <= 17.5) ? " + 
"0.0007772086365029659" + 
":  " + 
"-0.0014971161139049206" + 
":  " + 
"(b('L8b6med') <= 3556.75) ? " + 
"-0.004577858223319953" + 
":  " + 
"-0.0026067995199627082" + 
":  " + 
"(b('L8b1med') <= 641.0) ? " + 
"(b('L8b7med') <= 2116.0) ? " + 
"0.00014287085992241436" + 
":  " + 
"-0.0007752373142736047" + 
":  " + 
"(b('L8b7med') <= 2269.0) ? " + 
"0.008517965142589604" + 
":  " + 
"0.0004241875767302258" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 38.950599670410156) ? " + 
"(b('L8b6med') <= 2618.0) ? " + 
"(b('sand') <= 22.5) ? " + 
"0.00662810503425774" + 
":  " + 
"0.0014394526559015942" + 
":  " + 
"(b('lat') <= 38.14986991882324) ? " + 
"-9.209555061523832e-05" + 
":  " + 
"0.0027760627886939887" + 
":  " + 
"(b('clay') <= 16.5) ? " + 
"(b('lat') <= 46.2239990234375) ? " + 
"0.0015472032809922028" + 
":  " + 
"-1.178684266587749e-05" + 
":  " + 
"(b('svvk3') <= 0.0760432668030262) ? " + 
"-0.0004674600552983252" + 
":  " + 
"0.006319131989679691" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 53.5) ? " + 
"(b('sand') <= 51.5) ? " + 
"(b('svvk3') <= 0.018222343176603317) ? " + 
"0.0003173896420230213" + 
":  " + 
"-0.0007213436069677342" + 
":  " + 
"(b('lon') <= -5.277935028076172) ? " + 
"0.0052829343793424815" + 
":  " + 
"-0.00047305512880280024" + 
":  " + 
"(b('sand') <= 57.5) ? " + 
"(b('L8b1med') <= 512.0) ? " + 
"-0.0037185112539654887" + 
":  " + 
"-0.00014455180310484478" + 
":  " + 
"(b('sand') <= 61.0) ? " + 
"0.001774213451391229" + 
":  " + 
"-0.00014661605296672329" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= -26.78680992126465) ? " + 
"(b('ndvi_med') <= 1900.25) ? " + 
"(b('gvvk2') <= 0.39327745139598846) ? " + 
"0.0015530096645985398" + 
":  " + 
"-0.0019871184253070218" + 
":  " + 
"0.0063856265808596435" + 
":  " + 
"(b('lon') <= 27.154595375061035) ? " + 
"(b('lat') <= 32.18929862976074) ? " + 
"-0.001684994010784968" + 
":  " + 
"3.863125320315978e-05" + 
":  " + 
"(b('svvk3') <= 0.02361979242414236) ? " + 
"-0.00011194320284266951" + 
":  " + 
"-0.005004159656264398" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('ndvi_med') <= 4452.5) ? " + 
"(b('lon') <= -102.1697998046875) ? " + 
"-0.0021894962898542938" + 
":  " + 
"8.179758884465032e-05" + 
":  " + 
"(b('lon') <= -30.883347988128662) ? " + 
"-0.00543438376138064" + 
":  " + 
"0.00034798145155992555" + 
":  " + 
"(b('svvk3') <= -0.01786497700959444) ? " + 
"(b('L8b6med') <= 3404.5) ? " + 
"0.0013427802471338939" + 
":  " + 
"0.008787838669073594" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.0019731855052893023" + 
":  " + 
"5.5874579072587205e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 77.5) ? " + 
"(b('sand') <= 70.5) ? " + 
"(b('svvk3') <= -0.010644129011780024) ? " + 
"-0.0006062478839282139" + 
":  " + 
"0.00012493490296085146" + 
":  " + 
"(b('L8b7med') <= 1627.0) ? " + 
"0.0006378512816389107" + 
":  " + 
"-0.002413080842724624" + 
":  " + 
"(b('gvvk2') <= 0.36731019616127014) ? " + 
"(b('ndvi_med') <= 4247.0) ? " + 
"0.004177847061432038" + 
":  " + 
"0.0022850795340232655" + 
":  " + 
"(b('L8b2med') <= 605.0) ? " + 
"0.00020981626156879894" + 
":  " + 
"0.0027965592561870686" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1179.0) ? " + 
"(b('svvk3') <= 0.04504917562007904) ? " + 
"(b('clay') <= 19.0) ? " + 
"0.0005574525584874923" + 
":  " + 
"-0.0016793442093088475" + 
":  " + 
"-0.004870266348218952" + 
":  " + 
"(b('ndvi_med') <= 1303.0) ? " + 
"(b('L8b6med') <= 2692.5) ? " + 
"0.008608173019469152" + 
":  " + 
"0.0005374735550843908" + 
":  " + 
"(b('ndvi_med') <= 1339.0) ? " + 
"-0.0037521967444504056" + 
":  " + 
"4.883856457606283e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 807.5) ? " + 
"(b('L8b3med') <= 801.75) ? " + 
"(b('L8b6med') <= 2870.5) ? " + 
"-0.00029390831999698334" + 
":  " + 
"0.0018478464089612956" + 
":  " + 
"(b('L8b7med') <= 1748.5) ? " + 
"-0.0030359332048001397" + 
":  " + 
"-0.01239291847590672" + 
":  " + 
"(b('L8b2med') <= 588.5) ? " + 
"(b('L8b2med') <= 572.5) ? " + 
"0.0003705700546255717" + 
":  " + 
"0.003213731493673382" + 
":  " + 
"(b('L8b1med') <= 507.5) ? " + 
"-0.0011209682993668722" + 
":  " + 
"0.00017678102274399287" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.3555718809366226) ? " + 
"(b('gvvk2') <= 0.3535436540842056) ? " + 
"(b('gvvk2') <= 0.33759455382823944) ? " + 
"9.585999156206281e-05" + 
":  " + 
"-0.0016400098970754673" + 
":  " + 
"(b('lon') <= -50.278599858284) ? " + 
"-0.00967921889997813" + 
":  " + 
"-0.0023954335888206058" + 
":  " + 
"(b('L8b1med') <= 451.25) ? " + 
"(b('L8b1med') <= 434.5) ? " + 
"7.78076969535721e-05" + 
":  " + 
"-0.003883531108230539" + 
":  " + 
"(b('L8b1med') <= 461.0) ? " + 
"0.003720468036562846" + 
":  " + 
"0.00029465468752514634" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.31293176114559174) ? " + 
"(b('gvvk2') <= 0.297782763838768) ? " + 
"(b('gvvk2') <= 0.28277742862701416) ? " + 
"-0.00014906896875123646" + 
":  " + 
"0.0025276648051541875" + 
":  " + 
"(b('L8b1med') <= 354.0) ? " + 
"0.0017552758567098332" + 
":  " + 
"-0.0036364483934234314" + 
":  " + 
"(b('gvvk2') <= 0.3137519955635071) ? " + 
"0.01775397600924772" + 
":  " + 
"(b('gvvk2') <= 0.31546850502491) ? " + 
"0.0058782325355127745" + 
":  " + 
"1.0869351244278875e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.00043326523154973984) ? " + 
"(b('svvk3') <= -0.0005696050066035241) ? " + 
"(b('ndvi_med') <= 1927.5) ? " + 
"-0.0008760071317899716" + 
":  " + 
"0.0007435688886859027" + 
":  " + 
"0.009945161510991146" + 
":  " + 
"(b('svvk3') <= -0.0003453021345194429) ? " + 
"-0.00856839413459691" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"-0.0005816282096929648" + 
":  " + 
"0.00014669912098848716" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3678.75) ? " + 
"(b('ndvi_med') <= 3582.0) ? " + 
"(b('ndvi_med') <= 3555.5) ? " + 
"-6.721299228352831e-05" + 
":  " + 
"0.00471705775123558" + 
":  " + 
"(b('svvk3') <= -0.005976802669465543) ? " + 
"0.0016143986659320857" + 
":  " + 
"-0.0026980171974938395" + 
":  " + 
"(b('ndvi_med') <= 3715.5) ? " + 
"(b('lat') <= 40.386375427246094) ? " + 
"0.012020135795430736" + 
":  " + 
"0.0019727753999216266" + 
":  " + 
"(b('lon') <= -99.3036994934082) ? " + 
"-0.0025889986226821557" + 
":  " + 
"0.0003840387562617746" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 49.7714729309082) ? " + 
"(b('L8b3med') <= 814.0) ? " + 
"(b('lat') <= 50.94952583312988) ? " + 
"-0.0007350166369042054" + 
":  " + 
"0.0005152883529216636" + 
":  " + 
"(b('L8b2med') <= 588.5) ? " + 
"0.0009715098761176194" + 
":  " + 
"-8.823041578674691e-05" + 
":  " + 
"0.0033514907182243675" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 53.5) ? " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('sand') <= 52.5) ? " + 
"0.00020724716355016102" + 
":  " + 
"0.005315974509244935" + 
":  " + 
"(b('clay') <= 20.0) ? " + 
"0.0004959812753123463" + 
":  " + 
"-0.001907745302705447" + 
":  " + 
"(b('svvk3') <= 0.02197057567536831) ? " + 
"(b('gvvk2') <= 0.26820625364780426) ? " + 
"0.0005683927608275528" + 
":  " + 
"-0.0016322912419365196" + 
":  " + 
"(b('gvvk2') <= 0.4780919849872589) ? " + 
"0.001804286669196518" + 
":  " + 
"-0.00041742036463162025" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('lat') <= 36.15193557739258) ? " + 
"0.0005716256356899062" + 
":  " + 
"-0.0001992008988581315" + 
":  " + 
"-0.011351146577258192" + 
":  " + 
"(b('gvvk2') <= 0.4510953277349472) ? " + 
"(b('svvk3') <= 0.05881730653345585) ? " + 
"0.006028925166233545" + 
":  " + 
"0.003162165401127265" + 
":  " + 
"(b('lat') <= 36.0643253326416) ? " + 
"-0.0021902675462489416" + 
":  " + 
"0.0005036073913983587" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1179.0) ? " + 
"(b('gvvk2') <= 0.2850046455860138) ? " + 
"(b('gvvk2') <= 0.17715035378932953) ? " + 
"-0.001224542634731847" + 
":  " + 
"0.0011918144506500468" + 
":  " + 
"(b('ndvi_med') <= 750.75) ? " + 
"0.0003353381585526269" + 
":  " + 
"-0.0036439183275482345" + 
":  " + 
"(b('ndvi_med') <= 1303.0) ? " + 
"(b('L8b6med') <= 2692.5) ? " + 
"0.007795928242839895" + 
":  " + 
"0.000533627213830922" + 
":  " + 
"(b('ndvi_med') <= 1339.0) ? " + 
"-0.0031742995517594166" + 
":  " + 
"4.196497505705494e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 616.25) ? " + 
"(b('bulk') <= 112.0) ? " + 
"(b('svvk3') <= 0.0035718916915357113) ? " + 
"6.062549161137132e-05" + 
":  " + 
"0.0033424064573085166" + 
":  " + 
"(b('ndvi_med') <= 3231.5) ? " + 
"-0.002900888263239284" + 
":  " + 
"-0.00016430439242499651" + 
":  " + 
"(b('L8b3med') <= 618.5) ? " + 
"(b('svvk3') <= 0.03304598666727543) ? " + 
"0.0058744852181728535" + 
":  " + 
"0.0020192680136943975" + 
":  " + 
"(b('L8b7med') <= 1581.25) ? " + 
"0.0005573976571031525" + 
":  " + 
"-0.00010275995835689849" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 19.0) ? " + 
"(b('svvk3') <= 0.02013546973466873) ? " + 
"(b('svvk3') <= -0.01772791240364313) ? " + 
"-0.001892958100284059" + 
":  " + 
"0.001233246660240094" + 
":  " + 
"(b('ndvi_med') <= 2935.0) ? " + 
"-0.0018090370829509927" + 
":  " + 
"-0.01100190942144924" + 
":  " + 
"(b('sand') <= 20.5) ? " + 
"0.00628154985277915" + 
":  " + 
"(b('gvvk2') <= 0.38667628169059753) ? " + 
"-0.00014234815323184351" + 
":  " + 
"0.0003457058804293483" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3686.5) ? " + 
"(b('L8b6med') <= 3580.25) ? " + 
"(b('L8b6med') <= 3554.5) ? " + 
"1.439222162186163e-05" + 
":  " + 
"0.003639968791542561" + 
":  " + 
"(b('gvvk2') <= 0.43759483098983765) ? " + 
"-0.0019273823398109696" + 
":  " + 
"0.002015708975012942" + 
":  " + 
"(b('L8b1med') <= 590.25) ? " + 
"(b('svvk3') <= 0.0028061913326382637) ? " + 
"-0.000957566060697114" + 
":  " + 
"0.00436564248328318" + 
":  " + 
"(b('bulk') <= 165.0) ? " + 
"0.0002043408240562828" + 
":  " + 
"-0.00669963958265149" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.00043326523154973984) ? " + 
"(b('svvk3') <= -0.0005696050066035241) ? " + 
"(b('ndvi_med') <= 3572.0) ? " + 
"-0.00025285066180056367" + 
":  " + 
"0.0012105085211471195" + 
":  " + 
"0.00898426016572082" + 
":  " + 
"(b('svvk3') <= -0.0003453021345194429) ? " + 
"-0.007275333219666016" + 
":  " + 
"(b('bulk') <= 133.5) ? " + 
"-0.0005300951882319724" + 
":  " + 
"0.00013263797059900268" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('clay') <= 22.5) ? " + 
"(b('clay') <= 21.5) ? " + 
"-0.0008868720912676868" + 
":  " + 
"-0.008762393968264282" + 
":  " + 
"(b('clay') <= 27.5) ? " + 
"0.0034772977953401937" + 
":  " + 
"-0.0004126782843339546" + 
":  " + 
"(b('svvk3') <= -0.0018616062588989735) ? " + 
"(b('gvvk2') <= 0.37142615020275116) ? " + 
"-7.142948112933978e-05" + 
":  " + 
"0.0024461845596796413" + 
":  " + 
"(b('L8b2med') <= 1822.0) ? " + 
"-6.61451208911701e-05" + 
":  " + 
"-0.005285994409284414" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 1641.5) ? " + 
"(b('L8b3med') <= 2607.5) ? " + 
"(b('bulk') <= 158.5) ? " + 
"-3.798442777931272e-05" + 
":  " + 
"0.0007432420376430331" + 
":  " + 
"-0.00475739496835597" + 
":  " + 
"0.003257981401920927" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bulk') <= 170.0) ? " + 
"(b('bulk') <= 158.5) ? " + 
"(b('bulk') <= 154.5) ? " + 
"2.7857387630486362e-05" + 
":  " + 
"-0.001319862540095219" + 
":  " + 
"(b('L8b3med') <= 885.0) ? " + 
"0.004239110392544272" + 
":  " + 
"-1.6322249988467783e-05" + 
":  " + 
"-0.0032795986848555697" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.010644129011780024) ? " + 
"(b('svvk3') <= -0.010906731709837914) ? " + 
"(b('gvvk2') <= 0.2915903478860855) ? " + 
"-0.005096694893276095" + 
":  " + 
"3.080040274916779e-05" + 
":  " + 
"-0.010129414416062812" + 
":  " + 
"(b('svvk3') <= -0.010399458464235067) ? " + 
"0.011047457150160145" + 
":  " + 
"(b('svvk3') <= -0.0018616062588989735) ? " + 
"0.0009134418954673453" + 
":  " + 
"-7.394043506313786e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3med') <= 1312.0) ? " + 
"(b('L8b3med') <= 1252.5) ? " + 
"(b('L8b3med') <= 1235.5) ? " + 
"-1.2379958125985255e-05" + 
":  " + 
"0.004381572555088142" + 
":  " + 
"(b('L8b7med') <= 2543.75) ? " + 
"-0.0009273530097303022" + 
":  " + 
"-0.004175343752610893" + 
":  " + 
"(b('L8b3med') <= 1375.5) ? " + 
"(b('lat') <= 36.81332969665527) ? " + 
"0.008467548561818021" + 
":  " + 
"0.0020845168881719217" + 
":  " + 
"(b('L8b1med') <= 773.5) ? " + 
"-0.0013951446288050621" + 
":  " + 
"0.0004431961771915663" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 53.5) ? " + 
"(b('lon') <= 1.7617999911308289) ? " + 
"(b('sand') <= 52.5) ? " + 
"0.00018795660578147674" + 
":  " + 
"0.004797493894943457" + 
":  " + 
"(b('clay') <= 20.0) ? " + 
"0.0004970886905276884" + 
":  " + 
"-0.0017484093581754394" + 
":  " + 
"(b('gvvk2') <= 0.26820625364780426) ? " + 
"(b('bulk') <= 151.5) ? " + 
"0.0011548552073632969" + 
":  " + 
"-0.0023222358274329453" + 
":  " + 
"(b('gvvk2') <= 0.3109198212623596) ? " + 
"-0.005441834386949811" + 
":  " + 
"-0.00021510302019073254" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 1641.5) ? " + 
"(b('L8b3med') <= 2366.5) ? " + 
"(b('L8b6med') <= 3674.5) ? " + 
"-5.405250662582495e-05" + 
":  " + 
"0.0005578400640672186" + 
":  " + 
"(b('lat') <= 33.751394271850586) ? " + 
"-0.0020755725487453247" + 
":  " + 
"-0.004084725237991076" + 
":  " + 
"0.003342335118156778" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('svvk3') <= -0.021503237076103687) ? " + 
"(b('clay') <= 22.5) ? " + 
"(b('clay') <= 21.5) ? " + 
"-0.0008026301219776648" + 
":  " + 
"-0.007900374321800852" + 
":  " + 
"(b('clay') <= 27.5) ? " + 
"0.0030292023593232777" + 
":  " + 
"-0.0004020090246592535" + 
":  " + 
"(b('svvk3') <= -0.01786497700959444) ? " + 
"(b('L8b3med') <= 1252.5) ? " + 
"0.001158419951845786" + 
":  " + 
"0.007629680472596406" + 
":  " + 
"(b('svvk3') <= -0.015487065538764) ? " + 
"-0.0018972943808555597" + 
":  " + 
"5.3212496953242884e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b1med') <= 459.5) ? " + 
"(b('lon') <= -111.08124542236328) ? " + 
"(b('gvvk2') <= 0.34371986985206604) ? " + 
"0.0007854660713545856" + 
":  " + 
"0.008476634063093546" + 
":  " + 
"(b('gvvk2') <= 0.3372344970703125) ? " + 
"0.0005703818425554715" + 
":  " + 
"-0.0007459526814393943" + 
":  " + 
"(b('L8b7med') <= 1923.5) ? " + 
"(b('L8b7med') <= 1901.0) ? " + 
"-0.001063918859990578" + 
":  " + 
"-0.0057117222019443005" + 
":  " + 
"(b('clay') <= 12.5) ? " + 
"-0.0015088361192257232" + 
":  " + 
"0.00023143146644010587" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.44356881082057953) ? " + 
"(b('gvvk2') <= 0.4411440044641495) ? " + 
"(b('lat') <= 36.15193557739258) ? " + 
"0.0004779439097345408" + 
":  " + 
"-0.00018112148380544085" + 
":  " + 
"-0.01024451561670213" + 
":  " + 
"(b('gvvk2') <= 0.46257317066192627) ? " + 
"(b('bulk') <= 129.0) ? " + 
"0.0003067429838089682" + 
":  " + 
"0.004466247028842757" + 
":  " + 
"(b('lat') <= 36.0643253326416) ? " + 
"-0.0019974540598399035" + 
":  " + 
"0.0003829817190083389" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3497.75) ? " + 
"(b('L8b6med') <= 3479.5) ? " + 
"(b('L8b6med') <= 3380.0) ? " + 
"8.716877717906033e-05" + 
":  " + 
"-0.002076575864422803" + 
":  " + 
"(b('svvk3') <= -0.005644022952765226) ? " + 
"0.007372383693688256" + 
":  " + 
"0.0021567761485476095" + 
":  " + 
"(b('L8b7med') <= 2243.5) ? " + 
"(b('L8b3med') <= 1056.0) ? " + 
"-0.004226653634313212" + 
":  " + 
"-0.0003714547041449697" + 
":  " + 
"(b('L8b6med') <= 3512.25) ? " + 
"-0.005314027583041413" + 
":  " + 
"0.00019137386907507704" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.5458730161190033) ? " + 
"(b('gvvk2') <= 0.5375914573669434) ? " + 
"(b('gvvk2') <= 0.5322960615158081) ? " + 
"-3.826645042356863e-05" + 
":  " + 
"0.004197044602121794" + 
":  " + 
"-0.0045864630190098656" + 
":  " + 
"(b('lon') <= -100.36590576171875) ? " + 
"(b('svvk3') <= 0.09748711064457893) ? " + 
"0.004886507259885778" + 
":  " + 
"0.001820022487280526" + 
":  " + 
"(b('sand') <= 74.0) ? " + 
"-0.00047932319962072065" + 
":  " + 
"0.0009908465061010743" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('gvvk2') <= 0.038837023079395294) ? " + 
"(b('sand') <= 28.0) ? " + 
"-0.003835554210727815" + 
":  " + 
"-0.0007121782139727362" + 
":  " + 
"(b('L8b6med') <= 2671.5) ? " + 
"(b('L8b6med') <= 2659.0) ? " + 
"6.826899067396683e-05" + 
":  " + 
"0.008448348660999675" + 
":  " + 
"(b('L8b6med') <= 2857.75) ? " + 
"-0.0008128991296943542" + 
":  " + 
"0.00010348732386351487" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 2573.5) ? " + 
"(b('L8b7med') <= 2567.5) ? " + 
"(b('lat') <= -26.78680992126465) ? " + 
"0.00393962905546065" + 
":  " + 
"3.680040816284063e-05" + 
":  " + 
"0.005660931083567203" + 
":  " + 
"(b('L8b2med') <= 770.0) ? " + 
"(b('gvvk2') <= 0.2944342941045761) ? " + 
"-0.00755952762443611" + 
":  " + 
"-0.0013508238707327122" + 
":  " + 
"(b('svvk3') <= 0.014319155365228653) ? " + 
"0.000747601810564978" + 
":  " + 
"-0.001027715794652255" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  return prediction