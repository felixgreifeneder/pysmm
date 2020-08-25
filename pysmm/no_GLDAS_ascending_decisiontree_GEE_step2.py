import ee 

def tree(feature_stack): 

  prediction = ee.Image(0.010792619)
  learning_rate = ee.Image(0.1)
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.9868559837341309) ? " + 
"(b('L8b6') <= 2548.5) ? " + 
"(b('lon') <= -120.0948715209961) ? " + 
"0.10856560984319902" + 
":  " + 
"9.00599720916447e-05" + 
":  " + 
"(b('L8dt') <= 864335.0) ? " + 
"-0.022797915608349123" + 
":  " + 
"-0.004691814884260919" + 
":  " + 
"(b('lon') <= -116.47515487670898) ? " + 
"(b('L8b4') <= 836.0) ? " + 
"0.2183477312914635" + 
":  " + 
"0.0646123090949263" + 
":  " + 
"(b('dsvv') <= 1.9904561042785645) ? " + 
"0.019106713989342036" + 
":  " + 
"0.04532831638866693" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 1.4403986930847168) ? " + 
"(b('L8b6') <= 2548.5) ? " + 
"(b('L8b6med') <= 2875.0) ? " + 
"-0.0023400688103258046" + 
":  " + 
"0.0526629247903228" + 
":  " + 
"(b('dgvv') <= -0.5555520057678223) ? " + 
"-0.0240719087633635" + 
":  " + 
"-0.007336955767725377" + 
":  " + 
"(b('lon') <= -107.17316055297852) ? " + 
"(b('ndvi') <= 2307.0) ? " + 
"0.07390914634934322" + 
":  " + 
"0.16306794567879057" + 
":  " + 
"(b('lat') <= 53.60474967956543) ? " + 
"0.03658771746016988" + 
":  " + 
"-0.0021372322495827978" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.9868559837341309) ? " + 
"(b('L8b6') <= 2195.5) ? " + 
"(b('lat') <= 41.45347023010254) ? " + 
"0.053618402086373355" + 
":  " + 
"-0.0004520320569183718" + 
":  " + 
"(b('dgvv') <= -0.3201727867126465) ? " + 
"-0.019514115526340296" + 
":  " + 
"-0.004371230679712467" + 
":  " + 
"(b('lon') <= -116.47515487670898) ? " + 
"(b('L8b6') <= 2730.0) ? " + 
"0.1307645379421179" + 
":  " + 
"0.029924391124187398" + 
":  " + 
"(b('L8b5') <= 2445.5) ? " + 
"0.04311302158532676" + 
":  " + 
"0.017893454209500066" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 1.5014357566833496) ? " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b6med') <= 2875.0) ? " + 
"-0.005626441362236652" + 
":  " + 
"0.03060032624944339" + 
":  " + 
"(b('ndvi_med') <= 1793.0) ? " + 
"-0.007055193150814522" + 
":  " + 
"-0.02293355526257582" + 
":  " + 
"(b('lon') <= -106.99895095825195) ? " + 
"(b('ndvi') <= 2307.0) ? " + 
"0.06330449893217631" + 
":  " + 
"0.13804247204569284" + 
":  " + 
"(b('sand') <= 62.5) ? " + 
"0.03145118453871168" + 
":  " + 
"-0.004405567657195694" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.9520587921142578) ? " + 
"(b('L8b6') <= 2073.5) ? " + 
"(b('lon') <= -118.20269775390625) ? " + 
"0.08992554193574247" + 
":  " + 
"0.011667654673523684" + 
":  " + 
"(b('L8dt') <= 1098066.5) ? " + 
"-0.014062838471307173" + 
":  " + 
"0.002353576817094262" + 
":  " + 
"(b('L8b6') <= 2714.5) ? " + 
"(b('L8b6med') <= 2875.0) ? " + 
"0.020942785968245135" + 
":  " + 
"0.07146010296197794" + 
":  " + 
"(b('dgvv') <= 1.8543510437011719) ? " + 
"0.0014253046223711074" + 
":  " + 
"0.024543813764989677" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.697087287902832) ? " + 
"(b('lon') <= -118.6085319519043) ? " + 
"(b('L8b4') <= 1037.5) ? " + 
"0.0859140576138146" + 
":  " + 
"-0.0026504173240698738" + 
":  " + 
"(b('L8dt') <= 1490687.0) ? " + 
"-0.014545233042376185" + 
":  " + 
"0.005294974319305807" + 
":  " + 
"(b('dsvv') <= 1.9469633102416992) ? " + 
"(b('L8b6') <= 2418.5) ? " + 
"0.029657732824771892" + 
":  " + 
"0.0038323455086115865" + 
":  " + 
"(b('lon') <= -106.89670181274414) ? " + 
"0.0879338147395952" + 
":  " + 
"0.026159768197362668" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 0.4764976501464844) ? " + 
"(b('lon') <= -106.84210205078125) ? " + 
"(b('L8b4') <= 739.0) ? " + 
"0.07833370830516546" + 
":  " + 
"0.0005791422069522536" + 
":  " + 
"(b('L8dt') <= 694046.0) ? " + 
"-0.019091579078329333" + 
":  " + 
"-0.00283783913193335" + 
":  " + 
"(b('L8b6') <= 2760.5) ? " + 
"(b('L8b6med') <= 3015.25) ? " + 
"0.015718040170966938" + 
":  " + 
"0.06251977064684194" + 
":  " + 
"(b('dsvv') <= 1.9897899627685547) ? " + 
"-0.0006245871209000082" + 
":  " + 
"0.020245011609289085" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 0.022423744201660156) ? " + 
"(b('lon') <= -106.73894500732422) ? " + 
"(b('L8b11') <= 1410.5) ? " + 
"0.071742204891309" + 
":  " + 
"0.0006811640197928032" + 
":  " + 
"(b('L8dt') <= 1490687.0) ? " + 
"-0.01845465110940521" + 
":  " + 
"0.002561613531687117" + 
":  " + 
"(b('dsvv') <= 1.9469633102416992) ? " + 
"(b('L8b6') <= 2781.0) ? " + 
"0.014965056928121596" + 
":  " + 
"-0.002088422973466472" + 
":  " + 
"(b('lon') <= -106.89670181274414) ? " + 
"0.07628562868139416" + 
":  " + 
"0.02095267975137578" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 0.022423744201660156) ? " + 
"(b('lon') <= -106.84210205078125) ? " + 
"(b('L8b4') <= 828.0) ? " + 
"0.0585610563928412" + 
":  " + 
"-0.0003142568210588109" + 
":  " + 
"(b('lat') <= 40.922170639038086) ? " + 
"-0.030417580898158762" + 
":  " + 
"-0.009012006494658354" + 
":  " + 
"(b('L8b6') <= 2781.0) ? " + 
"(b('L8b6med') <= 3015.25) ? " + 
"0.010381511805399854" + 
":  " + 
"0.05077308497351562" + 
":  " + 
"(b('L8dt') <= 782254.0) ? " + 
"-0.005214106917113479" + 
":  " + 
"0.013159279428500863" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 1.3616890907287598) ? " + 
"(b('dgvv') <= -2.0888943672180176) ? " + 
"(b('L8b2med') <= 451.25) ? " + 
"-0.08253972330273733" + 
":  " + 
"-0.017097524453428617" + 
":  " + 
"(b('L8b6') <= 2070.5) ? " + 
"0.02382786984337185" + 
":  " + 
"-0.003865193788503416" + 
":  " + 
"(b('lon') <= -106.99930191040039) ? " + 
"(b('L8b4') <= 808.0) ? " + 
"0.12167957072433783" + 
":  " + 
"0.04107709317979727" + 
":  " + 
"(b('lat') <= 44.514474868774414) ? " + 
"0.019726572436433734" + 
":  " + 
"-0.0002064674287280089" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 1.6397111415863037) ? " + 
"(b('dgvv') <= -1.7174835205078125) ? " + 
"(b('L8b2med') <= 451.25) ? " + 
"-0.059607229065371074" + 
":  " + 
"-0.012021872348601036" + 
":  " + 
"(b('L8dt') <= 606066.0) ? " + 
"-0.006287126932207228" + 
":  " + 
"0.00573312208405861" + 
":  " + 
"(b('lon') <= -106.89670181274414) ? " + 
"(b('ndvi') <= 2307.0) ? " + 
"0.03819622106794437" + 
":  " + 
"0.09651771386928089" + 
":  " + 
"(b('sand') <= 62.5) ? " + 
"0.017355081103197886" + 
":  " + 
"-0.015501255645804813" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 0.022423744201660156) ? " + 
"(b('ndvi_med') <= 2042.5) ? " + 
"(b('L8b4') <= 1140.5) ? " + 
"0.03217367889492889" + 
":  " + 
"-0.00472939635799873" + 
":  " + 
"(b('lat') <= 40.75148582458496) ? " + 
"-0.030417085417450463" + 
":  " + 
"-0.008728389847165403" + 
":  " + 
"(b('L8b6') <= 2666.5) ? " + 
"(b('L8b6med') <= 2875.0) ? " + 
"0.007605288770566948" + 
":  " + 
"0.04393745969152821" + 
":  " + 
"(b('L8dt') <= 425926.0) ? " + 
"-0.007283318914774768" + 
":  " + 
"0.007457226214062485" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 1.8409743309020996) ? " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b6med') <= 2875.0) ? " + 
"-0.0026884098371029778" + 
":  " + 
"0.023358863312815618" + 
":  " + 
"(b('L8b7med') <= 2390.25) ? " + 
"-0.014068572387749716" + 
":  " + 
"-0.0012893645604107407" + 
":  " + 
"(b('crops') <= 18.125764846801758) ? " + 
"(b('L8b2med') <= 691.5) ? " + 
"0.02558583696736441" + 
":  " + 
"0.06383544770843043" + 
":  " + 
"(b('L8b5med') <= 2318.75) ? " + 
"-0.027447507629118184" + 
":  " + 
"0.012587260856404874" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 0.022423744201660156) ? " + 
"(b('lon') <= -118.6085319519043) ? " + 
"(b('ndvi') <= 1950.0) ? " + 
"-0.005078726522934318" + 
":  " + 
"0.059334840181046705" + 
":  " + 
"(b('L8dt') <= 1490687.0) ? " + 
"-0.01126332983713899" + 
":  " + 
"0.005363797717430094" + 
":  " + 
"(b('L8b5') <= 2444.5) ? " + 
"(b('L8b6med') <= 2412.0) ? " + 
"-0.0067110478614804125" + 
":  " + 
"0.020886038760347194" + 
":  " + 
"(b('L8b4') <= 531.0) ? " + 
"0.06601249835807294" + 
":  " + 
"0.0012338408957701858" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -0.5555520057678223) ? " + 
"(b('L8b7med') <= 1595.5) ? " + 
"(b('L8b6med') <= 2840.25) ? " + 
"-0.02015450385890509" + 
":  " + 
"-0.08810488127669412" + 
":  " + 
"(b('lon') <= -106.62174606323242) ? " + 
"0.007318550003189327" + 
":  " + 
"-0.007341211045073415" + 
":  " + 
"(b('L8b6') <= 2608.5) ? " + 
"(b('L8b6med') <= 2875.0) ? " + 
"0.0056893651530266435" + 
":  " + 
"0.03658029766757446" + 
":  " + 
"(b('L8dt') <= 685995.5) ? " + 
"-0.005698368090296008" + 
":  " + 
"0.007390610069007626" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 2.2225570678710938) ? " + 
"(b('L8b11') <= 1022.5) ? " + 
"(b('L8b11') <= 1009.5) ? " + 
"0.020578868809577745" + 
":  " + 
"0.082326961467864" + 
":  " + 
"(b('L8b3') <= 453.0) ? " + 
"-0.2330137559603375" + 
":  " + 
"-0.002444161977570518" + 
":  " + 
"(b('lon') <= -116.37591552734375) ? " + 
"(b('ndvi_med') <= 1628.5) ? " + 
"0.0870743897584104" + 
":  " + 
"0.021109047965608325" + 
":  " + 
"(b('sand') <= 62.5) ? " + 
"0.016353902878363403" + 
":  " + 
"-0.020652430170276036" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 0.25139331817626953) ? " + 
"(b('dgvv') <= -2.1742539405822754) ? " + 
"(b('L8b2med') <= 440.25) ? " + 
"-0.06955413563955783" + 
":  " + 
"-0.013218061151161425" + 
":  " + 
"(b('L8b6') <= 2054.5) ? " + 
"0.018700895970253248" + 
":  " + 
"-0.00377115687995311" + 
":  " + 
"(b('L8b5') <= 2445.0) ? " + 
"(b('lat') <= 44.514474868774414) ? " + 
"0.021836966634336062" + 
":  " + 
"0.0017710552149355911" + 
":  " + 
"(b('L8b4') <= 531.0) ? " + 
"0.06115778308066089" + 
":  " + 
"0.0012351327366859795" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 1057223.0) ? " + 
"(b('lon') <= -106.62174606323242) ? " + 
"(b('L8b4') <= 877.5) ? " + 
"0.04745688169898407" + 
":  " + 
"0.0004024776702527604" + 
":  " + 
"(b('dsvv') <= -1.5964689254760742) ? " + 
"-0.019599322911390587" + 
":  " + 
"-0.0040662228375845134" + 
":  " + 
"(b('lon') <= -107.0709114074707) ? " + 
"(b('L8b4') <= 1167.5) ? " + 
"0.04315936744584602" + 
":  " + 
"0.010945783306388101" + 
":  " + 
"(b('L8b11') <= 1137.5) ? " + 
"0.024300262781710283" + 
":  " + 
"0.0046997611442086955" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2603.5) ? " + 
"(b('L8b6med') <= 2875.0) ? " + 
"(b('L8b3') <= 882.5) ? " + 
"-0.003026627751176406" + 
":  " + 
"0.01634906094804304" + 
":  " + 
"(b('lon') <= -116.34695434570312) ? " + 
"0.06045929715906224" + 
":  " + 
"0.02007845457250115" + 
":  " + 
"(b('L8dt') <= 2397054.0) ? " + 
"(b('L8b3') <= 801.5) ? " + 
"-0.017983801201531244" + 
":  " + 
"-0.003160032827198254" + 
":  " + 
"(b('sand') <= 63.5) ? " + 
"0.017073788340837177" + 
":  " + 
"-0.020291398222843208" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 1.9541335105895996) ? " + 
"(b('L8dt') <= 606066.0) ? " + 
"(b('ndvi_med') <= 3324.0) ? " + 
"-0.0031511000886754745" + 
":  " + 
"-0.019010008971149756" + 
":  " + 
"(b('L8b11') <= 1022.5) ? " + 
"0.03253849875704495" + 
":  " + 
"0.0021123339070553576" + 
":  " + 
"(b('crops') <= 18.125764846801758) ? " + 
"(b('L8b6med') <= 2124.125) ? " + 
"-0.0455596399943922" + 
":  " + 
"0.03507563311979675" + 
":  " + 
"(b('L8b5med') <= 2318.75) ? " + 
"-0.026268496517973493" + 
":  " + 
"0.008366123533899584" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b6med') <= 2875.0) ? " + 
"(b('dgvv') <= -0.3139305114746094) ? " + 
"-0.008047025790746658" + 
":  " + 
"0.0032613602951487345" + 
":  " + 
"(b('lon') <= -110.12002944946289) ? " + 
"0.04345012402814266" + 
":  " + 
"0.01327047271151021" + 
":  " + 
"(b('L8b6med') <= 3323.0) ? " + 
"(b('dgvv') <= -1.6332507133483887) ? " + 
"-0.0294739712680794" + 
":  " + 
"-0.006811515783279265" + 
":  " + 
"(b('L8b6') <= 3467.5) ? " + 
"0.013298694657450979" + 
":  " + 
"-0.0029172666380692836" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 781924.5) ? " + 
"(b('L8b6') <= 3156.5) ? " + 
"(b('L8b6med') <= 3120.5) ? " + 
"-0.003297177922687474" + 
":  " + 
"0.022007918914059187" + 
":  " + 
"(b('L8b6med') <= 3380.0) ? " + 
"-0.017253966441700002" + 
":  " + 
"-0.0036614583308978233" + 
":  " + 
"(b('dsvv') <= 0.24383544921875) ? " + 
"(b('sand') <= 20.5) ? " + 
"-0.027608608438904683" + 
":  " + 
"0.001974136494064673" + 
":  " + 
"(b('lat') <= 44.514474868774414) ? " + 
"0.016138887825566477" + 
":  " + 
"-0.0017847377237035222" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2215.5) ? " + 
"(b('L8b6med') <= 2416.75) ? " + 
"(b('ndvi') <= 4751.5) ? " + 
"-0.0012145626346382363" + 
":  " + 
"-0.03565530299826585" + 
":  " + 
"(b('crops') <= 10.490284442901611) ? " + 
"0.046074057669019924" + 
":  " + 
"0.014666195980341436" + 
":  " + 
"(b('L8b2') <= 363.5) ? " + 
"(b('L8b7med') <= 1324.0) ? " + 
"-0.10477307202193521" + 
":  " + 
"-0.008694393783815419" + 
":  " + 
"(b('L8dt') <= 1987972.5) ? " + 
"-0.002147511354939694" + 
":  " + 
"0.010379773216807307" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -2.087989330291748) ? " + 
"(b('L8b7med') <= 1588.25) ? " + 
"(b('L8b6med') <= 2449.0) ? " + 
"-0.0011719083781379907" + 
":  " + 
"-0.07672483821599041" + 
":  " + 
"(b('ndvi_med') <= 1534.25) ? " + 
"0.009597210977032334" + 
":  " + 
"-0.010921473230190645" + 
":  " + 
"(b('L8b6') <= 2215.5) ? " + 
"(b('L8b6med') <= 2416.75) ? " + 
"-0.00543650522973064" + 
":  " + 
"0.021384342265973338" + 
":  " + 
"(b('L8b2') <= 363.5) ? " + 
"-0.021757360633051413" + 
":  " + 
"0.0004073469405273418" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 2.796116828918457) ? " + 
"(b('dgvv') <= -2.1742539405822754) ? " + 
"(b('lat') <= 34.321603775024414) ? " + 
"-0.06157801238534766" + 
":  " + 
"-0.00938314766936837" + 
":  " + 
"(b('L8b6') <= 2054.5) ? " + 
"0.013272411715465764" + 
":  " + 
"-0.0009515868306661422" + 
":  " + 
"(b('crops') <= 18.125764846801758) ? " + 
"(b('L8b6med') <= 2129.125) ? " + 
"-0.04842021173383561" + 
":  " + 
"0.0451410728486331" + 
":  " + 
"(b('L8b5med') <= 2519.0) ? " + 
"-0.028495647023888477" + 
":  " + 
"0.010222807415150248" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 606060.5) ? " + 
"(b('crops') <= 5.957038402557373) ? " + 
"(b('ndvi') <= 3522.5) ? " + 
"0.00041752665833275776" + 
":  " + 
"0.04090560997550236" + 
":  " + 
"(b('ndvi') <= 4614.5) ? " + 
"-0.005344557362926932" + 
":  " + 
"-0.02122037193030114" + 
":  " + 
"(b('lon') <= -106.49531555175781) ? " + 
"(b('L8b4') <= 1253.0) ? " + 
"0.029215563984945743" + 
":  " + 
"0.003921194052794773" + 
":  " + 
"(b('L8dt') <= 2397054.0) ? " + 
"-4.544654627331405e-05" + 
":  " + 
"0.009837593168024288" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -0.5997352600097656) ? " + 
"(b('L8b7med') <= 2543.0) ? " + 
"(b('lon') <= -110.50074768066406) ? " + 
"0.005900590381498827" + 
":  " + 
"-0.010945209147585788" + 
":  " + 
"(b('L8b6') <= 3494.5) ? " + 
"0.01554320837184797" + 
":  " + 
"-0.0015408993501029682" + 
":  " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b6med') <= 3062.5) ? " + 
"0.0025840999985336528" + 
":  " + 
"0.021732128430113993" + 
":  " + 
"(b('ndvi') <= 5081.5) ? " + 
"-0.0006136060540786981" + 
":  " + 
"-0.030519287707425572" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 1094987.5) ? " + 
"(b('ndvi_med') <= 3340.5) ? " + 
"(b('ndvi') <= 3466.5) ? " + 
"-0.0024043874658132404" + 
":  " + 
"0.015187577110272391" + 
":  " + 
"(b('ndvi') <= 2812.0) ? " + 
"0.016745814162864643" + 
":  " + 
"-0.015959295755082484" + 
":  " + 
"(b('L8b6') <= 4860.5) ? " + 
"(b('L8b5med') <= 3493.5) ? " + 
"0.004479935543730813" + 
":  " + 
"0.023068865590647254" + 
":  " + 
"(b('ndvi') <= 2957.0) ? " + 
"-0.03773431588151648" + 
":  " + 
"0.05002832971474596" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 2.9765281677246094) ? " + 
"(b('dgvv') <= -2.87725567817688) ? " + 
"(b('lat') <= 34.80094528198242) ? " + 
"-0.08995218457105489" + 
":  " + 
"-0.010884988406390104" + 
":  " + 
"(b('L8b6') <= 2054.5) ? " + 
"0.01091331073827586" + 
":  " + 
"-0.0009524549764479046" + 
":  " + 
"(b('crops') <= 18.125764846801758) ? " + 
"(b('lat') <= 34.521310806274414) ? " + 
"-0.014180359642407341" + 
":  " + 
"0.045539566189870026" + 
":  " + 
"(b('L8b5med') <= 2218.25) ? " + 
"-0.037824164142567784" + 
":  " + 
"0.008583288797155588" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2659.5) ? " + 
"(b('lat') <= 44.514474868774414) ? " + 
"(b('L8b7med') <= 1932.5) ? " + 
"0.003728098986688368" + 
":  " + 
"0.02473725386337847" + 
":  " + 
"(b('L8b5med') <= 3346.5) ? " + 
"-0.006322416772930574" + 
":  " + 
"0.033521387179968706" + 
":  " + 
"(b('ndvi_med') <= 3958.5) ? " + 
"(b('L8dt') <= 2397054.0) ? " + 
"-0.0023098836065693915" + 
":  " + 
"0.009943428881265115" + 
":  " + 
"(b('L8b3') <= 911.0) ? " + 
"-0.03147266679002286" + 
":  " + 
"0.002788703147556756" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -106.62174606323242) ? " + 
"(b('ndvi') <= 2314.5) ? " + 
"(b('dsvv') <= 3.0228567123413086) ? " + 
"-0.0005533910722083064" + 
":  " + 
"0.037883067036259675" + 
":  " + 
"(b('ndvi_med') <= 2199.0) ? " + 
"0.04954872547175647" + 
":  " + 
"0.004261950150239331" + 
":  " + 
"(b('L8dt') <= 1490687.0) ? " + 
"(b('L8b5') <= 2175.5) ? " + 
"0.006187357956307285" + 
":  " + 
"-0.004812939683267116" + 
":  " + 
"(b('lon') <= -90.42574691772461) ? " + 
"-0.011989304121688828" + 
":  " + 
"0.00758078624439181" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -0.7079930305480957) ? " + 
"(b('L8b3') <= 764.5) ? " + 
"(b('ndvi') <= 3140.5) ? " + 
"-0.004793534346803615" + 
":  " + 
"-0.029078481123023497" + 
":  " + 
"(b('L8b2') <= 409.5) ? " + 
"0.04919433133341477" + 
":  " + 
"-0.002803020495490725" + 
":  " + 
"(b('ndvi') <= 5203.0) ? " + 
"(b('L8b6') <= 2536.5) ? " + 
"0.008316174819190215" + 
":  " + 
"0.00035397341450453936" + 
":  " + 
"(b('L8b2med') <= 660.0) ? " + 
"-0.020988607265499122" + 
":  " + 
"0.01838558792883904" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 538876.0) ? " + 
"(b('L8b6med') <= 2352.5) ? " + 
"(b('L8b3') <= 1440.5) ? " + 
"-0.019211287914353354" + 
":  " + 
"0.18545494629665787" + 
":  " + 
"(b('L8b6') <= 3247.5) ? " + 
"0.0019347902069775365" + 
":  " + 
"-0.006884327352585193" + 
":  " + 
"(b('lon') <= -106.49531555175781) ? " + 
"(b('L8b4') <= 1259.5) ? " + 
"0.021670527038922197" + 
":  " + 
"0.0030582306351255206" + 
":  " + 
"(b('lon') <= -88.72159957885742) ? " + 
"-0.005611147376163243" + 
":  " + 
"0.002956474874481382" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -2.87725567817688) ? " + 
"(b('lat') <= 34.80094528198242) ? " + 
"(b('sand') <= 36.5) ? " + 
"-0.11675665111514205" + 
":  " + 
"0.005643836980582351" + 
":  " + 
"(b('L8b3') <= 460.0) ? " + 
"-0.18649923520760364" + 
":  " + 
"-0.00754720589951751" + 
":  " + 
"(b('L8b6med') <= 2352.5) ? " + 
"(b('L8b3') <= 1440.5) ? " + 
"-0.010207207904038966" + 
":  " + 
"0.17291156510008002" + 
":  " + 
"(b('L8b6') <= 2220.5) ? " + 
"0.01293704941693644" + 
":  " + 
"3.780316706486812e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 3.484816074371338) ? " + 
"(b('L8b6') <= 3190.5) ? " + 
"(b('L8b6med') <= 3112.25) ? " + 
"-0.0009592207137354334" + 
":  " + 
"0.013098273755822336" + 
":  " + 
"(b('L8b11') <= 1976.5) ? " + 
"-0.042135377563577145" + 
":  " + 
"-0.0026992905336744597" + 
":  " + 
"(b('ndvi_med') <= 3604.0) ? " + 
"(b('sand') <= 45.5) ? " + 
"0.03962410786735942" + 
":  " + 
"0.008120403794044474" + 
":  " + 
"(b('L8b4') <= 717.0) ? " + 
"0.022338805622974953" + 
":  " + 
"-0.042500309381872416" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -113.71215057373047) ? " + 
"(b('L8b4') <= 738.5) ? " + 
"(b('L8b3') <= 750.0) ? " + 
"0.04309103725714781" + 
":  " + 
"0.14766205968574775" + 
":  " + 
"(b('ndvi') <= 2111.5) ? " + 
"-0.0006398185931554814" + 
":  " + 
"0.023114650358905874" + 
":  " + 
"(b('L8dt') <= 2397054.0) ? " + 
"(b('dgvv') <= -1.7032928466796875) ? " + 
"-0.010769726239155166" + 
":  " + 
"-0.0009029607805978986" + 
":  " + 
"(b('L8b5med') <= 2863.75) ? " + 
"-0.0015388400427586327" + 
":  " + 
"0.015055480914728438" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 11.22841739654541) ? " + 
"(b('L8b4') <= 604.5) ? " + 
"(b('L8b3') <= 407.5) ? " + 
"-0.03650715761157774" + 
":  " + 
"0.04501179149857004" + 
":  " + 
"(b('dgvv') <= 2.5329575538635254) ? " + 
"0.0009154537112582772" + 
":  " + 
"0.024886484053652947" + 
":  " + 
"(b('L8dt') <= 2354933.0) ? " + 
"(b('sand') <= 57.5) ? " + 
"-0.0016218705651090044" + 
":  " + 
"-0.011310860342749708" + 
":  " + 
"(b('lon') <= -90.42574691772461) ? " + 
"-0.01822751023074952" + 
":  " + 
"0.009782291053507834" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 538876.0) ? " + 
"(b('L8b6med') <= 2377.0) ? " + 
"(b('L8b3') <= 1440.5) ? " + 
"-0.014054996491891488" + 
":  " + 
"0.15046003863585616" + 
":  " + 
"(b('L8b6') <= 2603.5) ? " + 
"0.005794373140105951" + 
":  " + 
"-0.0035340340380403874" + 
":  " + 
"(b('L8b3') <= 770.5) ? " + 
"(b('L8b6') <= 2487.0) ? " + 
"0.0021303922204888854" + 
":  " + 
"-0.01333634565850554" + 
":  " + 
"(b('L8b11') <= 1398.5) ? " + 
"0.025546913539093257" + 
":  " + 
"0.0027164444228002503" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5203.0) ? " + 
"(b('ndvi') <= 5170.0) ? " + 
"(b('dgvv') <= -0.8519721031188965) ? " + 
"-0.004010127156372926" + 
":  " + 
"0.0018692485819367048" + 
":  " + 
"(b('ndvi_med') <= 2744.5) ? " + 
"0.16270118094058517" + 
":  " + 
"0.01784502352761208" + 
":  " + 
"(b('sand') <= 75.5) ? " + 
"(b('lat') <= 35.61929893493652) ? " + 
"-0.054979838208739716" + 
":  " + 
"-0.0025470143455243247" + 
":  " + 
"(b('L8b2') <= 703.5) ? " + 
"-0.051515520777473164" + 
":  " + 
"-0.005253960974927899" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -106.49531555175781) ? " + 
"(b('ndvi') <= 2105.5) ? " + 
"(b('L8b5') <= 1316.0) ? " + 
"-0.07168108887157633" + 
":  " + 
"0.00014849291887752622" + 
":  " + 
"(b('L8b7med') <= 1932.5) ? " + 
"-0.00010377203923282769" + 
":  " + 
"0.033941228584183386" + 
":  " + 
"(b('L8b5') <= 2175.5) ? " + 
"(b('crops') <= 88.85982513427734) ? " + 
"0.008207251899068553" + 
":  " + 
"-0.013875390341428647" + 
":  " + 
"(b('L8b3') <= 516.5) ? " + 
"0.05461361914384908" + 
":  " + 
"-0.0025349208298311573" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 44.514474868774414) ? " + 
"(b('L8b6') <= 2418.5) ? " + 
"(b('L8b2med') <= 841.25) ? " + 
"0.014087743422849559" + 
":  " + 
"-0.01366222307130284" + 
":  " + 
"(b('dsvv') <= 2.682217597961426) ? " + 
"-0.0013412929953896368" + 
":  " + 
"0.01348928294814434" + 
":  " + 
"(b('L8b4') <= 522.0) ? " + 
"(b('L8b5') <= 2444.5) ? " + 
"-0.004610093114867834" + 
":  " + 
"0.047710258396303926" + 
":  " + 
"(b('L8b2') <= 363.5) ? " + 
"-0.022858518411149144" + 
":  " + 
"-0.0018579777980092078" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3335.5) ? " + 
"(b('L8b6') <= 3228.5) ? " + 
"(b('L8b3') <= 770.5) ? " + 
"-0.0039466574125501565" + 
":  " + 
"0.0027705025244499247" + 
":  " + 
"(b('lat') <= 32.90584945678711) ? " + 
"-0.0552442725618553" + 
":  " + 
"-0.006940848422877086" + 
":  " + 
"(b('L8b4') <= 1181.5) ? " + 
"(b('L8b2') <= 535.5) ? " + 
"0.008656422013056239" + 
":  " + 
"0.03191290689473958" + 
":  " + 
"(b('L8b5') <= 4503.5) ? " + 
"0.00094104765602356" + 
":  " + 
"-0.03093061070867027" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 606060.5) ? " + 
"(b('L8b6med') <= 2452.0) ? " + 
"(b('L8b6med') <= 2449.0) ? " + 
"-0.008039910989249341" + 
":  " + 
"-0.05200623702982462" + 
":  " + 
"(b('L8b6') <= 2476.5) ? " + 
"0.008286031786766592" + 
":  " + 
"-0.002237116352942905" + 
":  " + 
"(b('L8dt') <= 606485.0) ? " + 
"(b('L8b6') <= 2337.5) ? " + 
"0.1654831131930256" + 
":  " + 
"0.05403655460677466" + 
":  " + 
"(b('dsvv') <= -2.821107864379883) ? " + 
"-0.010583583218558096" + 
":  " + 
"0.002636056480596859" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5203.0) ? " + 
"(b('ndvi') <= 5170.0) ? " + 
"(b('dsvv') <= -2.8374576568603516) ? " + 
"-0.011242733140396385" + 
":  " + 
"0.0007439915418478484" + 
":  " + 
"(b('ndvi_med') <= 2744.5) ? " + 
"0.14557362217429745" + 
":  " + 
"0.016363436292925766" + 
":  " + 
"(b('sand') <= 75.5) ? " + 
"(b('lon') <= -3.0728151202201843) ? " + 
"-0.017632681478299293" + 
":  " + 
"0.0061008144121645754" + 
":  " + 
"(b('L8b2med') <= 402.0) ? " + 
"-0.06936705220477163" + 
":  " + 
"-0.025023765519692646" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b6') <= 1654.5) ? " + 
"(b('sand') <= 78.0) ? " + 
"-0.028191130142417746" + 
":  " + 
"0.07853067231547285" + 
":  " + 
"(b('dsvv') <= -3.5571441650390625) ? " + 
"-0.17195094081856033" + 
":  " + 
"-0.18204655370034473" + 
":  " + 
"(b('L8b4') <= 532.5) ? " + 
"(b('L8b2') <= 331.0) ? " + 
"0.03527916550349961" + 
":  " + 
"-0.022415942835859373" + 
":  " + 
"(b('L8b3') <= 562.5) ? " + 
"-0.0238607625780495" + 
":  " + 
"0.00017155815595564576" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 1094987.5) ? " + 
"(b('L8b6med') <= 2377.0) ? " + 
"(b('L8b3') <= 1440.5) ? " + 
"-0.010509995200486007" + 
":  " + 
"0.16205178827060474" + 
":  " + 
"(b('L8b6') <= 2410.5) ? " + 
"0.007880606837966613" + 
":  " + 
"-0.0018517485606963837" + 
":  " + 
"(b('L8b5') <= 1298.5) ? " + 
"(b('L8dt') <= 1982669.0) ? " + 
"-0.035943308740415576" + 
":  " + 
"-0.09618049300915531" + 
":  " + 
"(b('L8b6') <= 4860.5) ? " + 
"0.0038000732138887307" + 
":  " + 
"-0.031178759899521603" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -113.71215057373047) ? " + 
"(b('L8b4') <= 1037.0) ? " + 
"(b('crops') <= 30.107266426086426) ? " + 
"0.035211265902438615" + 
":  " + 
"-0.0247697985693856" + 
":  " + 
"(b('L8b5') <= 1844.0) ? " + 
"0.04268775075962792" + 
":  " + 
"-0.0009412047391646484" + 
":  " + 
"(b('L8dt') <= 2397054.0) ? " + 
"(b('dgvv') <= -1.7032928466796875) ? " + 
"-0.008124709374124413" + 
":  " + 
"-0.0007152875561422656" + 
":  " + 
"(b('L8b5med') <= 3499.75) ? " + 
"0.0036614407734595253" + 
":  " + 
"0.03147326365716501" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 4758.5) ? " + 
"(b('ndvi') <= 4420.5) ? " + 
"(b('ndvi_med') <= 4818.25) ? " + 
"-8.14699099701639e-05" + 
":  " + 
"0.04387294677417265" + 
":  " + 
"(b('ndvi_med') <= 3310.5) ? " + 
"0.041801921466950644" + 
":  " + 
"0.0006526583534119552" + 
":  " + 
"(b('sand') <= 69.5) ? " + 
"(b('L8b6') <= 2777.5) ? " + 
"0.00518441211121397" + 
":  " + 
"-0.015056215338156632" + 
":  " + 
"(b('L8b6') <= 1990.0) ? " + 
"-0.07456605959934917" + 
":  " + 
"-0.02079241315607801" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3323.0) ? " + 
"(b('L8b6') <= 3228.5) ? " + 
"(b('L8b3') <= 823.5) ? " + 
"-0.0028639532388555987" + 
":  " + 
"0.003355137022801283" + 
":  " + 
"(b('L8b11') <= 1988.5) ? " + 
"-0.05396462788813573" + 
":  " + 
"-0.006287505294392443" + 
":  " + 
"(b('L8b4') <= 1181.5) ? " + 
"(b('L8b11') <= 1124.5) ? " + 
"-0.022075764147777715" + 
":  " + 
"0.01862433600886291" + 
":  " + 
"(b('ndvi') <= 2056.0) ? " + 
"-0.0010936938924404895" + 
":  " + 
"0.00765761234505839" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 3.523932456970215) ? " + 
"(b('sand') <= 26.0) ? " + 
"(b('dsvv') <= 0.15635013580322266) ? " + 
"-0.01325248140347441" + 
":  " + 
"0.0021654853195135315" + 
":  " + 
"(b('L8b11') <= 1022.5) ? " + 
"0.016146443730574372" + 
":  " + 
"-7.612400594527859e-05" + 
":  " + 
"(b('L8b11') <= 1046.5) ? " + 
"(b('dsvv') <= 4.607161521911621) ? " + 
"-0.08052656040290533" + 
":  " + 
"-0.043206832728905964" + 
":  " + 
"(b('L8b5med') <= 3262.0) ? " + 
"0.01865869431782104" + 
":  " + 
"-0.013618107996165335" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('ndvi') <= 3131.5) ? " + 
"(b('lat') <= 55.997798919677734) ? " + 
"0.002604057702070452" + 
":  " + 
"0.05954040168732859" + 
":  " + 
"(b('L8b4') <= 610.5) ? " + 
"-0.005352854962149662" + 
":  " + 
"-0.030952387961215376" + 
":  " + 
"(b('L8b11') <= 1013.5) ? " + 
"(b('L8b6med') <= 2391.75) ? " + 
"-0.035765619629276636" + 
":  " + 
"0.059536990744565844" + 
":  " + 
"(b('L8b6') <= 1779.5) ? " + 
"-0.03824914096697068" + 
":  " + 
"0.000552267553267372" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2168.0) ? " + 
"(b('L8b5med') <= 3003.25) ? " + 
"(b('crops') <= 87.49077224731445) ? " + 
"0.0037002324129643454" + 
":  " + 
"-0.014746391004250493" + 
":  " + 
"(b('L8b6med') <= 3759.75) ? " + 
"0.03541339326678216" + 
":  " + 
"-0.01817055343169822" + 
":  " + 
"(b('L8b3') <= 516.5) ? " + 
"(b('ndvi') <= 3776.5) ? " + 
"0.06722685337133273" + 
":  " + 
"0.0013380971412652698" + 
":  " + 
"(b('L8b3') <= 759.5) ? " + 
"-0.007643833614805472" + 
":  " + 
"0.0004077478850990914" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b4') <= 494.5) ? " + 
"(b('sand') <= 78.0) ? " + 
"-0.023286250588683763" + 
":  " + 
"0.06918923186722215" + 
":  " + 
"(b('L8b6') <= 1654.5) ? " + 
"-0.08221256751161253" + 
":  " + 
"-0.15789844015013527" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"(b('crops') <= 81.81896209716797) ? " + 
"0.017822033814804208" + 
":  " + 
"-0.03068407147041185" + 
":  " + 
"(b('L8b3') <= 562.5) ? " + 
"-0.032262423043467554" + 
":  " + 
"7.882193921755656e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 411044.5) ? " + 
"(b('ndvi') <= 4760.0) ? " + 
"(b('ndvi') <= 4756.0) ? " + 
"-0.0015700874637105124" + 
":  " + 
"0.2512660211519348" + 
":  " + 
"(b('L8b6') <= 1827.0) ? " + 
"-0.07077416924123639" + 
":  " + 
"-0.009523290774525182" + 
":  " + 
"(b('L8b3') <= 770.5) ? " + 
"(b('lon') <= -69.71229934692383) ? " + 
"-0.01059764731535711" + 
":  " + 
"0.002140630916001626" + 
":  " + 
"(b('L8b11') <= 1323.0) ? " + 
"0.026836038840907694" + 
":  " + 
"0.0021015980804389585" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 48.65084648132324) ? " + 
"(b('dsvv') <= 0.7439312934875488) ? " + 
"(b('sand') <= 26.0) ? " + 
"-0.015830822171335017" + 
":  " + 
"0.000325800709097906" + 
":  " + 
"(b('L8b6med') <= 2091.625) ? " + 
"-0.028963710531887357" + 
":  " + 
"0.010868593748070473" + 
":  " + 
"(b('L8b3') <= 757.5) ? " + 
"(b('L8b5') <= 3535.5) ? " + 
"-0.007035977975623662" + 
":  " + 
"-0.06455523836799008" + 
":  " + 
"(b('L8b6') <= 2659.5) ? " + 
"0.008252292456763073" + 
":  " + 
"-0.0028129258658460055" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 44.514474868774414) ? " + 
"(b('L8b6') <= 2418.5) ? " + 
"(b('L8b2med') <= 841.25) ? " + 
"0.011433965843095856" + 
":  " + 
"-0.014505039391567186" + 
":  " + 
"(b('L8b11') <= 1451.5) ? " + 
"-0.016481206239622594" + 
":  " + 
"0.0001770982071499642" + 
":  " + 
"(b('L8b3') <= 1382.0) ? " + 
"(b('L8b4') <= 522.0) ? " + 
"0.017670893923907055" + 
":  " + 
"-0.0037765805208426215" + 
":  " + 
"(b('L8b7med') <= 1701.0) ? " + 
"0.12242437349774228" + 
":  " + 
"0.0134038040587489" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b4') <= 494.5) ? " + 
"(b('L8b5') <= 1474.5) ? " + 
"-0.03470217654321703" + 
":  " + 
"0.01681811692443931" + 
":  " + 
"(b('L8b5med') <= 2177.0) ? " + 
"-0.07309442511466802" + 
":  " + 
"-0.14182915251035894" + 
":  " + 
"(b('L8b5') <= 2142.5) ? " + 
"(b('L8b5med') <= 2358.75) ? " + 
"-0.0006069492773412877" + 
":  " + 
"0.010992421693209315" + 
":  " + 
"(b('L8b3') <= 516.5) ? " + 
"0.029036606690918187" + 
":  " + 
"-0.0008331339911326345" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1636.5) ? " + 
"(b('L8b7med') <= 2399.5) ? " + 
"(b('lat') <= -0.9345006942749023) ? " + 
"-0.058026707639836604" + 
":  " + 
"-0.007433768731763313" + 
":  " + 
"(b('L8b6') <= 3467.5) ? " + 
"0.007915078028140541" + 
":  " + 
"-0.00317896517551679" + 
":  " + 
"(b('ndvi_med') <= 1635.0) ? " + 
"(b('lon') <= -120.94869613647461) ? " + 
"0.05223966962405448" + 
":  " + 
"0.009169297610101731" + 
":  " + 
"(b('L8b5') <= 2175.5) ? " + 
"0.006524314391218764" + 
":  " + 
"-0.0013964282783380073" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('ndvi') <= 3131.5) ? " + 
"(b('lat') <= 55.997798919677734) ? " + 
"0.0020228326158597174" + 
":  " + 
"0.0509213891934002" + 
":  " + 
"(b('L8b3') <= 656.0) ? " + 
"-0.010926277990316764" + 
":  " + 
"-0.057175503118677" + 
":  " + 
"(b('L8b2') <= 396.5) ? " + 
"(b('L8b2') <= 382.75) ? " + 
"0.0031862482253328106" + 
":  " + 
"0.029856023058833357" + 
":  " + 
"(b('L8b3') <= 822.5) ? " + 
"-0.004444549550199703" + 
":  " + 
"0.0009715566169751978" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 48.65084648132324) ? " + 
"(b('dgvv') <= 0.777130126953125) ? " + 
"(b('sand') <= 26.0) ? " + 
"-0.013931828630579826" + 
":  " + 
"0.00041687362783765627" + 
":  " + 
"(b('L8b5med') <= 1733.25) ? " + 
"0.12629769117020978" + 
":  " + 
"0.008740152279211877" + 
":  " + 
"(b('L8b3') <= 757.5) ? " + 
"(b('L8b5') <= 3535.5) ? " + 
"-0.006531450359116355" + 
":  " + 
"-0.058349741044421456" + 
":  " + 
"(b('L8b6') <= 2659.5) ? " + 
"0.007246222647902588" + 
":  " + 
"-0.002499020832074931" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5203.0) ? " + 
"(b('ndvi') <= 5170.0) ? " + 
"(b('dsvv') <= 3.523932456970215) ? " + 
"-7.077542635702321e-05" + 
":  " + 
"0.010557660884444554" + 
":  " + 
"(b('L8b3') <= 988.0) ? " + 
"0.014156743014476645" + 
":  " + 
"0.13157938775897812" + 
":  " + 
"(b('L8b6med') <= 2632.5) ? " + 
"(b('ndvi') <= 5359.0) ? " + 
"-0.04245866438157105" + 
":  " + 
"-0.011600653117200047" + 
":  " + 
"(b('lat') <= 35.61929893493652) ? " + 
"-0.0439201785526231" + 
":  " + 
"0.009147098567852568" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3172150.0) ? " + 
"(b('crops') <= 61.53006935119629) ? " + 
"(b('dgvv') <= -0.8510103225708008) ? " + 
"-0.0033866847940867283" + 
":  " + 
"0.0026857689567467012" + 
":  " + 
"(b('L8b6med') <= 3310.0) ? " + 
"-0.005494564511814885" + 
":  " + 
"0.00014418790440955587" + 
":  " + 
"(b('L8b5med') <= 3022.0) ? " + 
"(b('lon') <= 9.173149585723877) ? " + 
"-0.0061688053352639246" + 
":  " + 
"0.015001842433391768" + 
":  " + 
"(b('L8b5') <= 2983.0) ? " + 
"0.04185422696206402" + 
":  " + 
"0.004238085261664529" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1636.5) ? " + 
"(b('L8b7med') <= 2399.5) ? " + 
"(b('L8b2med') <= 528.0) ? " + 
"0.009958735607701372" + 
":  " + 
"-0.010964137067322379" + 
":  " + 
"(b('L8b6') <= 3467.5) ? " + 
"0.006803116699938684" + 
":  " + 
"-0.0029606042544951653" + 
":  " + 
"(b('ndvi_med') <= 1635.0) ? " + 
"(b('crops') <= 77.2614974975586) ? " + 
"0.021252840976424166" + 
":  " + 
"0.000737496427964963" + 
":  " + 
"(b('L8b5') <= 3389.5) ? " + 
"0.0010941706622713298" + 
":  " + 
"-0.00589804438209259" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 363.5) ? " + 
"(b('L8b6') <= 2219.5) ? " + 
"(b('ndvi') <= 4804.5) ? " + 
"0.005556509148517761" + 
":  " + 
"-0.03189995677852213" + 
":  " + 
"(b('L8b7med') <= 1324.0) ? " + 
"-0.0786918010725424" + 
":  " + 
"-0.005362070750104523" + 
":  " + 
"(b('L8b2') <= 391.5) ? " + 
"(b('L8b2') <= 382.75) ? " + 
"0.0034049867710026827" + 
":  " + 
"0.02525064301482138" + 
":  " + 
"(b('L8b2med') <= 336.0) ? " + 
"0.0281587829060204" + 
":  " + 
"-0.00025458648052172593" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 179923.5) ? " + 
"(b('L8b7med') <= 1520.0) ? " + 
"(b('L8b6') <= 3386.5) ? " + 
"-0.01270860569942982" + 
":  " + 
"-0.09712517994722274" + 
":  " + 
"(b('ndvi_med') <= 4069.0) ? " + 
"-0.000966168113340956" + 
":  " + 
"-0.016943151092622587" + 
":  " + 
"(b('L8dt') <= 179953.5) ? " + 
"(b('L8b4') <= 1125.5) ? " + 
"0.10298092415455086" + 
":  " + 
"0.007934895791917264" + 
":  " + 
"(b('L8b5') <= 4370.5) ? " + 
"0.0006735144611337411" + 
":  " + 
"-0.015417550498038796" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4784.5) ? " + 
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b2') <= 181.5) ? " + 
"0.011871706321464323" + 
":  " + 
"-0.047896537447722404" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"0.011013326666652539" + 
":  " + 
"-0.00022332863007807854" + 
":  " + 
"(b('L8b7med') <= 2563.0) ? " + 
"(b('dsvv') <= 1.2694721221923828) ? " + 
"0.12638892360295723" + 
":  " + 
"0.10393894227955253" + 
":  " + 
"(b('L8b2med') <= 846.0) ? " + 
"-0.012460232679495968" + 
":  " + 
"-0.0026047275085392257" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('ndvi') <= 3131.5) ? " + 
"(b('L8b7med') <= 2127.0) ? " + 
"0.006040146433359092" + 
":  " + 
"-0.02927857050439242" + 
":  " + 
"(b('dsvv') <= -2.5977559089660645) ? " + 
"-0.07029639143567765" + 
":  " + 
"-0.010317206849517795" + 
":  " + 
"(b('L8b11') <= 1013.5) ? " + 
"(b('L8b11') <= 963.5) ? " + 
"-0.0008503567159271257" + 
":  " + 
"0.06796338380734085" + 
":  " + 
"(b('L8b3') <= 688.5) ? " + 
"0.012448309520654559" + 
":  " + 
"-8.684576293817176e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 411044.5) ? " + 
"(b('sand') <= 14.5) ? " + 
"(b('L8b5') <= 3182.0) ? " + 
"-0.005551079101800659" + 
":  " + 
"-0.0952579612819665" + 
":  " + 
"(b('sand') <= 17.0) ? " + 
"0.03171685937656726" + 
":  " + 
"-0.001826282743768156" + 
":  " + 
"(b('L8b3') <= 826.5) ? " + 
"(b('lon') <= -69.40549850463867) ? " + 
"-0.008376551712343994" + 
":  " + 
"0.0024576485251855728" + 
":  " + 
"(b('L8b11') <= 1391.5) ? " + 
"0.024773956200005633" + 
":  " + 
"0.0022631396679427705" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1355.0) ? " + 
"(b('ndvi') <= 1523.5) ? " + 
"(b('L8b11') <= 1366.0) ? " + 
"-0.08564479154828027" + 
":  " + 
"0.0018791709305492196" + 
":  " + 
"(b('lon') <= -121.31654739379883) ? " + 
"0.22900292615980966" + 
":  " + 
"0.02003469470288221" + 
":  " + 
"(b('ndvi') <= 1636.5) ? " + 
"(b('lat') <= -26.78680992126465) ? " + 
"-0.03580851668012103" + 
":  " + 
"-0.003351936608035958" + 
":  " + 
"(b('lon') <= -121.20288467407227) ? " + 
"0.03193093547465817" + 
":  " + 
"0.00034701445427745624" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2397054.0) ? " + 
"(b('crops') <= 61.53006935119629) ? " + 
"(b('dgvv') <= 0.9243226051330566) ? " + 
"-0.00018133843256559675" + 
":  " + 
"0.006081324715290347" + 
":  " + 
"(b('ndvi') <= 4609.0) ? " + 
"-0.00221633009903228" + 
":  " + 
"-0.012174755677070246" + 
":  " + 
"(b('L8b5') <= 4383.0) ? " + 
"(b('L8b5med') <= 3499.75) ? " + 
"0.0029558486836112167" + 
":  " + 
"0.03305389940523493" + 
":  " + 
"(b('L8b7med') <= 2070.5) ? " + 
"-0.0875344408562928" + 
":  " + 
"-0.05655525010263748" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 363.5) ? " + 
"(b('L8b6') <= 2219.5) ? " + 
"(b('L8b7med') <= 1325.5) ? " + 
"0.02105408777759597" + 
":  " + 
"-0.003652886335183596" + 
":  " + 
"(b('L8b7med') <= 1324.0) ? " + 
"-0.06982187214291002" + 
":  " + 
"-0.005151141593925178" + 
":  " + 
"(b('L8b2') <= 391.5) ? " + 
"(b('L8b7med') <= 1303.5) ? " + 
"-0.03283232793575948" + 
":  " + 
"0.012561973113074998" + 
":  " + 
"(b('lat') <= 56.0489501953125) ? " + 
"-3.755021526781702e-05" + 
":  " + 
"-0.10443657712536532" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2002.0) ? " + 
"(b('L8b6') <= 3236.0) ? " + 
"(b('ndvi') <= 1389.0) ? " + 
"-0.017544992606440542" + 
":  " + 
"0.00022156753452308212" + 
":  " + 
"(b('L8b5') <= 2095.0) ? " + 
"-0.1590331259004508" + 
":  " + 
"-0.058259237230079364" + 
":  " + 
"(b('L8b5') <= 2436.5) ? " + 
"(b('L8b5med') <= 3003.25) ? " + 
"0.0014002393193372406" + 
":  " + 
"0.01592735384406842" + 
":  " + 
"(b('L8b5') <= 2470.5) ? " + 
"-0.02096886524704754" + 
":  " + 
"-0.00020867069942184262" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2312.5) ? " + 
"(b('ndvi_med') <= 3422.5) ? " + 
"(b('L8b7med') <= 2390.25) ? " + 
"-0.005508995083818961" + 
":  " + 
"0.0009647996985816116" + 
":  " + 
"(b('dsvv') <= -1.516937255859375) ? " + 
"0.008837591312917838" + 
":  " + 
"0.049971401057720216" + 
":  " + 
"(b('ndvi_med') <= 2123.25) ? " + 
"(b('crops') <= 27.716090202331543) ? " + 
"0.030850494715965127" + 
":  " + 
"0.00460781097345202" + 
":  " + 
"(b('L8b5') <= 3389.0) ? " + 
"0.001365371135747751" + 
":  " + 
"-0.007404313732063349" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4784.5) ? " + 
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b6') <= 1654.5) ? " + 
"-0.012650066488786272" + 
":  " + 
"-0.11775276899978201" + 
":  " + 
"(b('L8b4') <= 532.5) ? " + 
"0.013962076106011034" + 
":  " + 
"-0.00012997459520554418" + 
":  " + 
"(b('L8b5med') <= 3270.5) ? " + 
"(b('ndvi') <= 3279.5) ? " + 
"0.1063067106487908" + 
":  " + 
"0.08082514500233351" + 
":  " + 
"(b('dgvv') <= 4.151525974273682) ? " + 
"-0.011131817562844877" + 
":  " + 
"-0.0016679731146970467" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('L8b3') <= 656.5) ? " + 
"(b('L8b5med') <= 3292.0) ? " + 
"-0.0015933993274512236" + 
":  " + 
"-0.048346763264811805" + 
":  " + 
"(b('L8b2') <= 376.0) ? " + 
"-0.06465970232336384" + 
":  " + 
"-0.011685912825380795" + 
":  " + 
"(b('L8b11') <= 1013.5) ? " + 
"(b('L8b5med') <= 2733.0) ? " + 
"-0.05073156261638565" + 
":  " + 
"0.0397476756265325" + 
":  " + 
"(b('L8b6') <= 1779.5) ? " + 
"-0.03198633383757213" + 
":  " + 
"0.00042330805736731495" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2100.5) ? " + 
"(b('L8b6med') <= 3771.5) ? " + 
"(b('L8b5med') <= 3004.25) ? " + 
"0.002401582207089473" + 
":  " + 
"0.033109196509431074" + 
":  " + 
"(b('L8b11') <= 1607.0) ? " + 
"-0.04341580428505582" + 
":  " + 
"-0.006032848596703734" + 
":  " + 
"(b('L8b6med') <= 2199.25) ? " + 
"(b('L8b4') <= 613.5) ? " + 
"0.008291831434430335" + 
":  " + 
"-0.02061388009978897" + 
":  " + 
"(b('L8b6') <= 1930.0) ? " + 
"0.01178360592436953" + 
":  " + 
"-0.0005768453468300065" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 363.5) ? " + 
"(b('L8b4') <= 612.5) ? " + 
"(b('sand') <= 24.5) ? " + 
"-0.032275849670690214" + 
":  " + 
"0.009074809257805717" + 
":  " + 
"(b('lat') <= 55.879150390625) ? " + 
"-0.003983169350789043" + 
":  " + 
"-0.037888332049780746" + 
":  " + 
"(b('L8b2') <= 391.5) ? " + 
"(b('L8b2') <= 382.75) ? " + 
"0.001811909666627345" + 
":  " + 
"0.02090085095549559" + 
":  " + 
"(b('L8b2med') <= 336.0) ? " + 
"0.02550244113145418" + 
":  " + 
"-0.00018022284167557162" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 759.5) ? " + 
"(b('L8b5') <= 3381.5) ? " + 
"(b('L8b5med') <= 3285.0) ? " + 
"-0.00029623072985869125" + 
":  " + 
"-0.03183612688431607" + 
":  " + 
"(b('L8b4') <= 647.5) ? " + 
"-0.002734596404866544" + 
":  " + 
"-0.03633736670381964" + 
":  " + 
"(b('L8b11') <= 1323.0) ? " + 
"(b('lon') <= -116.1460952758789) ? " + 
"0.0841951842544263" + 
":  " + 
"0.01287349555297609" + 
":  " + 
"(b('L8b6') <= 1845.0) ? " + 
"0.11050739733753387" + 
":  " + 
"0.00012238639770616438" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3172150.0) ? " + 
"(b('crops') <= 61.53006935119629) ? " + 
"(b('L8b3') <= 933.5) ? " + 
"-0.0009578446633348236" + 
":  " + 
"0.00341178449269644" + 
":  " + 
"(b('L8b4') <= 3016.5) ? " + 
"-0.0021758554337441716" + 
":  " + 
"-0.05291602243223168" + 
":  " + 
"(b('dsvv') <= 6.625141620635986) ? " + 
"(b('dsvv') <= -2.4876136779785156) ? " + 
"0.032969232545832665" + 
":  " + 
"0.0035121758922187006" + 
":  " + 
"0.23216262169325885" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2336.5) ? " + 
"(b('ndvi_med') <= 3422.5) ? " + 
"(b('L8b7med') <= 2390.25) ? " + 
"-0.0051169641594789265" + 
":  " + 
"0.0008960658532212945" + 
":  " + 
"(b('L8b5') <= 2707.0) ? " + 
"0.018333546292706154" + 
":  " + 
"0.05980671235521384" + 
":  " + 
"(b('ndvi_med') <= 3310.5) ? " + 
"(b('L8b6') <= 4638.0) ? " + 
"0.004518132449293627" + 
":  " + 
"0.08081807096475699" + 
":  " + 
"(b('ndvi') <= 2740.0) ? " + 
"0.020471638450016275" + 
":  " + 
"-0.005889504230921273" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 3464.5) ? " + 
"(b('lat') <= 56.023799896240234) ? " + 
"(b('ndvi_med') <= 4458.0) ? " + 
"-0.0012031409981227848" + 
":  " + 
"0.05089161153271353" + 
":  " + 
"(b('L8b6') <= 2954.0) ? " + 
"0.018069367584397474" + 
":  " + 
"0.14730721885789191" + 
":  " + 
"(b('ndvi_med') <= 3531.75) ? " + 
"(b('lat') <= 44.063255310058594) ? " + 
"0.01662865668361649" + 
":  " + 
"0.0012575173740004678" + 
":  " + 
"(b('ndvi_med') <= 3563.5) ? " + 
"-0.037469364249724406" + 
":  " + 
"-0.003615741698744671" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2142.5) ? " + 
"(b('L8b3') <= 538.5) ? " + 
"(b('L8b3') <= 531.0) ? " + 
"-0.008023273184489935" + 
":  " + 
"-0.052438837451259795" + 
":  " + 
"(b('L8b4') <= 539.0) ? " + 
"0.11833484779456625" + 
":  " + 
"0.004346152824721188" + 
":  " + 
"(b('L8b6') <= 1366.0) ? " + 
"(b('L8b6') <= 1299.0) ? " + 
"0.06457821154600599" + 
":  " + 
"0.1483410626451901" + 
":  " + 
"(b('L8b3') <= 728.5) ? " + 
"-0.005245703254131593" + 
":  " + 
"0.00013858267096669819" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 604.5) ? " + 
"(b('dgvv') <= -0.4428224563598633) ? " + 
"0.03747572711456486" + 
":  " + 
"0.19371745501325402" + 
":  " + 
"(b('L8b5') <= 1320.5) ? " + 
"(b('L8b4') <= 830.0) ? " + 
"-0.01414114507982166" + 
":  " + 
"-0.07538358005924638" + 
":  " + 
"(b('L8b5') <= 2100.5) ? " + 
"0.003863055905263799" + 
":  " + 
"-0.00046823946161765866" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3660.0) ? " + 
"(b('L8b5') <= 4389.0) ? " + 
"(b('L8b5') <= 4210.5) ? " + 
"-0.00011257066538312071" + 
":  " + 
"0.024621468201250548" + 
":  " + 
"(b('L8b11') <= 1229.0) ? " + 
"0.08959050228122871" + 
":  " + 
"-0.02680008160488449" + 
":  " + 
"(b('L8dt') <= 2068235.5) ? " + 
"(b('L8b11') <= 3925.5) ? " + 
"0.03222745623256881" + 
":  " + 
"0.0038446761594886814" + 
":  " + 
"(b('dgvv') <= 1.7280030250549316) ? " + 
"-0.01575107498735723" + 
":  " + 
"-0.06061207049033947" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 1490687.0) ? " + 
"(b('ndvi') <= 5203.0) ? " + 
"(b('ndvi') <= 5170.0) ? " + 
"-0.0003690642738612224" + 
":  " + 
"0.07058683949632406" + 
":  " + 
"(b('L8b5') <= 4038.5) ? " + 
"-0.012888637124260372" + 
":  " + 
"0.023285211921926532" + 
":  " + 
"(b('L8b5med') <= 3385.5) ? " + 
"(b('L8b7med') <= 2802.5) ? " + 
"0.002913508145891445" + 
":  " + 
"-0.012290811783190869" + 
":  " + 
"(b('L8b5') <= 3190.0) ? " + 
"0.048512216745512676" + 
":  " + 
"0.0005098815851571037" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 3464.5) ? " + 
"(b('lat') <= 56.023799896240234) ? " + 
"(b('ndvi_med') <= 4458.0) ? " + 
"-0.0011259117024386177" + 
":  " + 
"0.0459556374586534" + 
":  " + 
"(b('L8b6') <= 2954.0) ? " + 
"0.016351378042059855" + 
":  " + 
"0.1326341791992369" + 
":  " + 
"(b('ndvi_med') <= 3531.75) ? " + 
"(b('lat') <= 47.95810508728027) ? " + 
"0.0122849988755134" + 
":  " + 
"-0.004545209078273202" + 
":  " + 
"(b('L8b5') <= 3633.5) ? " + 
"-0.0019368622637318423" + 
":  " + 
"-0.020061705175429864" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 3.523932456970215) ? " + 
"(b('dgvv') <= 3.385451078414917) ? " + 
"(b('L8b5med') <= 3660.0) ? " + 
"-0.00024775444028620695" + 
":  " + 
"0.0123087244550548" + 
":  " + 
"(b('dsvv') <= 3.483914375305176) ? " + 
"-0.03360413845013734" + 
":  " + 
"0.0012591918832684766" + 
":  " + 
"(b('L8b11') <= 1046.5) ? " + 
"(b('dsvv') <= 4.607161521911621) ? " + 
"-0.0670043986471843" + 
":  " + 
"-0.03071803364365745" + 
":  " + 
"(b('L8b5med') <= 3262.0) ? " + 
"0.014115197527723633" + 
":  " + 
"-0.01499480264055945" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -2.87725567817688) ? " + 
"(b('lat') <= 34.80094528198242) ? " + 
"(b('ndvi_med') <= 2762.0) ? " + 
"0.029265675420660674" + 
":  " + 
"-0.07998356735956746" + 
":  " + 
"(b('lon') <= 9.146950244903564) ? " + 
"0.0008382285512250341" + 
":  " + 
"-0.029695026217323783" + 
":  " + 
"(b('L8b5med') <= 2002.0) ? " + 
"(b('L8b11') <= 2558.5) ? " + 
"-0.005426972580985968" + 
":  " + 
"-0.05973676456706773" + 
":  " + 
"(b('L8b5') <= 2100.5) ? " + 
"0.004801349760140492" + 
":  " + 
"-2.8684101408559056e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1339.0) ? " + 
"(b('ndvi') <= 1475.0) ? " + 
"(b('dgvv') <= 1.6982908248901367) ? " + 
"0.0001360904434312523" + 
":  " + 
"0.02288259573985578" + 
":  " + 
"(b('L8b11') <= 2009.5) ? " + 
"-0.000885104341961489" + 
":  " + 
"0.03969956045452424" + 
":  " + 
"(b('L8b4') <= 2025.5) ? " + 
"(b('L8b3') <= 1472.0) ? " + 
"-0.00033062712281664206" + 
":  " + 
"0.01851320224282648" + 
":  " + 
"(b('ndvi') <= 3473.5) ? " + 
"-0.006735106211823227" + 
":  " + 
"0.045808548845346256" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3335.5) ? " + 
"(b('L8b4') <= 2205.0) ? " + 
"(b('dgvv') <= -1.3651700019836426) ? " + 
"-0.005637407276201029" + 
":  " + 
"0.00032943418805373223" + 
":  " + 
"(b('L8b2') <= 1110.0) ? " + 
"-0.052501391315529104" + 
":  " + 
"-0.00542704381900154" + 
":  " + 
"(b('L8b4') <= 1181.5) ? " + 
"(b('L8b2') <= 535.5) ? " + 
"0.001876276181760994" + 
":  " + 
"0.023413872163583243" + 
":  " + 
"(b('L8b6') <= 2361.0) ? " + 
"-0.05417307239413187" + 
":  " + 
"0.0004908548283671751" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 179923.5) ? " + 
"(b('L8b2med') <= 628.5) ? " + 
"(b('L8b5') <= 3477.0) ? " + 
"-0.00418494516942956" + 
":  " + 
"-0.021602777042433643" + 
":  " + 
"(b('L8b4') <= 910.5) ? " + 
"0.022780340282069378" + 
":  " + 
"-0.000979203891607031" + 
":  " + 
"(b('L8dt') <= 179953.5) ? " + 
"(b('L8b4') <= 1125.5) ? " + 
"0.08830136066166733" + 
":  " + 
"0.007968118884981789" + 
":  " + 
"(b('L8b6') <= 604.5) ? " + 
"0.10404078845639039" + 
":  " + 
"0.00035231258175098156" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 1116312.5) ? " + 
"(b('ndvi') <= 3464.5) ? " + 
"(b('lat') <= 56.023799896240234) ? " + 
"-0.0018203342492360882" + 
":  " + 
"0.033807574247690306" + 
":  " + 
"(b('ndvi') <= 3534.5) ? " + 
"0.02788221100968654" + 
":  " + 
"0.0010865470831591447" + 
":  " + 
"(b('L8b6') <= 4860.5) ? " + 
"(b('L8b5med') <= 3385.5) ? " + 
"0.0012249609330312321" + 
":  " + 
"0.01316442401773668" + 
":  " + 
"(b('L8dt') <= 6459549.5) ? " + 
"-0.0337028495739745" + 
":  " + 
"0.05314138308814617" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 882.5) ? " + 
"(b('L8b5') <= 4210.5) ? " + 
"(b('L8b3') <= 860.5) ? " + 
"-0.0007056684804118273" + 
":  " + 
"-0.013706977885569946" + 
":  " + 
"(b('L8dt') <= 1015396.0) ? " + 
"0.08964479828221887" + 
":  " + 
"0.03760966789984774" + 
":  " + 
"(b('ndvi') <= 2184.0) ? " + 
"(b('ndvi_med') <= 3376.25) ? " + 
"-0.0017319453718418235" + 
":  " + 
"0.03615150159652934" + 
":  " + 
"(b('lat') <= 50.52953910827637) ? " + 
"0.007133903697503229" + 
":  " + 
"-0.009067906399996245" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1339.0) ? " + 
"(b('ndvi') <= 1530.5) ? " + 
"(b('L8b2med') <= 970.75) ? " + 
"-0.0041355601884773855" + 
":  " + 
"0.0059006679080706335" + 
":  " + 
"(b('lon') <= -120.8821029663086) ? " + 
"0.20177115482542157" + 
":  " + 
"0.02406803461854472" + 
":  " + 
"(b('L8b4') <= 3016.5) ? " + 
"(b('L8b2') <= 1461.5) ? " + 
"-0.0003505239005964328" + 
":  " + 
"0.04645218200680636" + 
":  " + 
"(b('L8dt') <= 518400.5) ? " + 
"-0.02809755095074427" + 
":  " + 
"-0.05009844973431941" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5med') <= 3385.5) ? " + 
"(b('L8b5') <= 3487.5) ? " + 
"-0.00012680624800012822" + 
":  " + 
"0.01791344570803356" + 
":  " + 
"(b('L8b5') <= 2970.5) ? " + 
"0.029227483565605495" + 
":  " + 
"-0.007301367651860253" + 
":  " + 
"(b('L8b5') <= 3522.0) ? " + 
"(b('dgvv') <= -0.24134254455566406) ? " + 
"-0.0509284652373943" + 
":  " + 
"-0.11043210573502751" + 
":  " + 
"(b('L8b5med') <= 3138.5) ? " + 
"0.005486493907429551" + 
":  " + 
"-0.0078047586046970305" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b2') <= 181.5) ? " + 
"(b('lon') <= 9.173149585723877) ? " + 
"-0.0018347584179136908" + 
":  " + 
"0.05836008649160784" + 
":  " + 
"(b('ndvi') <= 3451.5) ? " + 
"-0.02406752383943864" + 
":  " + 
"-0.09347107569003264" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"(b('L8b7med') <= 1324.0) ? " + 
"0.031187965682156954" + 
":  " + 
"0.0026895600881219318" + 
":  " + 
"(b('L8b2') <= 355.5) ? " + 
"-0.011289570168006538" + 
":  " + 
"0.00026689409938609066" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2390.0) ? " + 
"(b('L8b3') <= 1440.5) ? " + 
"(b('L8b11') <= 2019.5) ? " + 
"-0.00589125608243715" + 
":  " + 
"0.011801423949958645" + 
":  " + 
"(b('dgvv') <= -2.422337532043457) ? " + 
"0.06447092820517102" + 
":  " + 
"0.13629760529076693" + 
":  " + 
"(b('L8b6') <= 2410.5) ? " + 
"(b('L8b2med') <= 841.25) ? " + 
"0.006286597439491689" + 
":  " + 
"-0.018901499901147412" + 
":  " + 
"(b('L8b11') <= 1451.5) ? " + 
"-0.014858767314904221" + 
":  " + 
"0.00039558108892279284" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 737.5) ? " + 
"(b('lon') <= -119.03326797485352) ? " + 
"(b('L8b11') <= 1119.5) ? " + 
"-0.005005119996432383" + 
":  " + 
"0.06539809562731293" + 
":  " + 
"(b('L8b2med') <= 525.25) ? " + 
"0.0034667194642235347" + 
":  " + 
"-0.008656425035794533" + 
":  " + 
"(b('L8b3') <= 603.25) ? " + 
"(b('ndvi') <= 3523.5) ? " + 
"-0.02121694929584997" + 
":  " + 
"-0.10913709326885107" + 
":  " + 
"(b('L8b3') <= 822.5) ? " + 
"-0.004641316119395159" + 
":  " + 
"0.000660834541993351" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 3190.5) ? " + 
"(b('L8b6med') <= 3112.25) ? " + 
"(b('dsvv') <= 5.601175546646118) ? " + 
"-0.00013885397338140698" + 
":  " + 
"-0.043395938746738374" + 
":  " + 
"(b('L8b6med') <= 3671.0) ? " + 
"0.010710242277969455" + 
":  " + 
"-0.006851592267274979" + 
":  " + 
"(b('L8b11') <= 2278.0) ? " + 
"(b('L8b5med') <= 2877.0) ? " + 
"-0.0024884911110272315" + 
":  " + 
"-0.024369283898660134" + 
":  " + 
"(b('L8b7med') <= 1878.5) ? " + 
"0.019612746448868762" + 
":  " + 
"-0.0006598415132252842" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3172150.0) ? " + 
"(b('crops') <= 61.53006935119629) ? " + 
"(b('ndvi') <= 4288.5) ? " + 
"5.9036292829713455e-05" + 
":  " + 
"0.00770387110573335" + 
":  " + 
"(b('L8b6med') <= 3508.5) ? " + 
"-0.0037548883918974724" + 
":  " + 
"0.0007682588341835469" + 
":  " + 
"(b('dgvv') <= 6.626832962036133) ? " + 
"(b('L8b5med') <= 3022.0) ? " + 
"-0.0009461233315748328" + 
":  " + 
"0.012076108329538334" + 
":  " + 
"0.20323495298168398" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4784.5) ? " + 
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5med') <= 3385.5) ? " + 
"4.053015842296448e-05" + 
":  " + 
"0.009629826557585573" + 
":  " + 
"(b('L8b5') <= 3522.0) ? " + 
"-0.060795975809065525" + 
":  " + 
"-0.0021172220263673924" + 
":  " + 
"(b('L8b4') <= 1028.5) ? " + 
"(b('L8dt') <= 927890.5) ? " + 
"0.08488711224082333" + 
":  " + 
"0.05802909126102901" + 
":  " + 
"(b('L8b2med') <= 846.0) ? " + 
"-0.005626179164328303" + 
":  " + 
"0.004499137306367876" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3660.0) ? " + 
"(b('L8b5') <= 4389.0) ? " + 
"(b('L8b5') <= 4326.5) ? " + 
"-3.480933528271584e-05" + 
":  " + 
"0.039528983023225106" + 
":  " + 
"(b('L8b11') <= 1229.0) ? " + 
"0.07156395724037803" + 
":  " + 
"-0.02268479843503708" + 
":  " + 
"(b('L8dt') <= 1689918.5) ? " + 
"(b('L8dt') <= 1399250.5) ? " + 
"0.011623452459259399" + 
":  " + 
"0.12107201196752625" + 
":  " + 
"(b('dsvv') <= 1.7125725746154785) ? " + 
"-0.013668603934239484" + 
":  " + 
"-0.05346936134032785" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 3305.5) ? " + 
"(b('L8b6med') <= 3112.25) ? " + 
"(b('L8b6') <= 3301.5) ? " + 
"-0.0003681483731666055" + 
":  " + 
"0.07588286166114658" + 
":  " + 
"(b('L8b11') <= 1122.0) ? " + 
"-0.018622876737924964" + 
":  " + 
"0.0062448920083506936" + 
":  " + 
"(b('L8b11') <= 2072.0) ? " + 
"(b('sand') <= 32.5) ? " + 
"-0.0840257902538906" + 
":  " + 
"-0.008601768713506154" + 
":  " + 
"(b('ndvi') <= 2627.5) ? " + 
"-0.0018889873854359362" + 
":  " + 
"0.007719482681269645" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 3.8659508228302) ? " + 
"(b('L8b6') <= 1925.5) ? " + 
"(b('L8b3') <= 894.0) ? " + 
"0.0028849519293334533" + 
":  " + 
"0.04955455841851504" + 
":  " + 
"(b('L8b3') <= 461.5) ? " + 
"-0.08880428665486158" + 
":  " + 
"-0.00038566605574699063" + 
":  " + 
"(b('crops') <= 28.942655563354492) ? " + 
"(b('sand') <= 45.5) ? " + 
"0.03948453217036429" + 
":  " + 
"-0.004378229075122335" + 
":  " + 
"(b('lon') <= -104.34579849243164) ? " + 
"-0.06693535527263529" + 
":  " + 
"0.002147080307693738" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5203.0) ? " + 
"(b('ndvi') <= 5170.0) ? " + 
"(b('ndvi') <= 3464.5) ? " + 
"-0.0005160957975014044" + 
":  " + 
"0.0030833501380265467" + 
":  " + 
"(b('L8b2') <= 452.5) ? " + 
"0.010835888780756678" + 
":  " + 
"0.10854716085859802" + 
":  " + 
"(b('L8b5') <= 2777.5) ? " + 
"(b('L8b2') <= 315.5) ? " + 
"0.06035397810239655" + 
":  " + 
"-0.027128807603337406" + 
":  " + 
"(b('L8b5') <= 2961.0) ? " + 
"0.03218304115639483" + 
":  " + 
"-0.0037808282138655515" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('lon') <= 22.38558006286621) ? " + 
"(b('L8b6') <= 2381.5) ? " + 
"-0.0018450207069600278" + 
":  " + 
"-0.024102135644198344" + 
":  " + 
"(b('crops') <= 48.84012222290039) ? " + 
"0.01063800365695589" + 
":  " + 
"-0.01924643038472609" + 
":  " + 
"(b('L8b2') <= 464.5) ? " + 
"(b('lat') <= 41.29464912414551) ? " + 
"0.014812362047485062" + 
":  " + 
"1.4417938127961715e-05" + 
":  " + 
"(b('L8b11') <= 1651.5) ? " + 
"-0.009650635374932005" + 
":  " + 
"0.00046857974314440593" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2436.5) ? " + 
"(b('L8b5med') <= 3003.25) ? " + 
"(b('L8b5') <= 2341.5) ? " + 
"-0.0010323093188994443" + 
":  " + 
"0.007590385568892917" + 
":  " + 
"(b('L8b6med') <= 3759.75) ? " + 
"0.019563121075761376" + 
":  " + 
"-0.007165664267073826" + 
":  " + 
"(b('L8b5') <= 2464.5) ? " + 
"(b('sand') <= 20.5) ? " + 
"-0.08778583447307238" + 
":  " + 
"-0.012535947543768574" + 
":  " + 
"(b('L8b3') <= 518.5) ? " + 
"0.03624848116243559" + 
":  " + 
"-0.00040897406853665795" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2100.5) ? " + 
"(b('crops') <= 91.13764572143555) ? " + 
"(b('L8b5med') <= 3004.25) ? " + 
"0.0027137537387574204" + 
":  " + 
"0.01897866895377806" + 
":  " + 
"(b('L8b2') <= 524.5) ? " + 
"-0.03259511786162687" + 
":  " + 
"0.004024883961289744" + 
":  " + 
"(b('L8b2') <= 200.5) ? " + 
"(b('L8dt') <= 259178.5) ? " + 
"-0.04504590434767429" + 
":  " + 
"-0.12333029569188031" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"0.011148686442356224" + 
":  " + 
"-0.0006540059151641249" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 363.5) ? " + 
"(b('dsvv') <= -0.8575000762939453) ? " + 
"(b('L8b6') <= 2137.5) ? " + 
"-0.0029509008170239205" + 
":  " + 
"-0.039012262694744775" + 
":  " + 
"(b('L8b4') <= 612.5) ? " + 
"0.008493809189388668" + 
":  " + 
"-0.00757838678088794" + 
":  " + 
"(b('L8b2') <= 391.5) ? " + 
"(b('L8b2') <= 382.75) ? " + 
"0.001380987558323947" + 
":  " + 
"0.01921739543288407" + 
":  " + 
"(b('lat') <= 56.0489501953125) ? " + 
"-3.389635375077464e-05" + 
":  " + 
"-0.09208147557698129" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 665.5) ? " + 
"(b('L8b5med') <= 3292.0) ? " + 
"(b('ndvi') <= 3131.5) ? " + 
"0.003088027014726292" + 
":  " + 
"-0.0077877574257954945" + 
":  " + 
"(b('L8b5') <= 3221.0) ? " + 
"-0.04824352855680122" + 
":  " + 
"0.10946249530554031" + 
":  " + 
"(b('L8b4') <= 796.5) ? " + 
"(b('L8b4') <= 792.5) ? " + 
"0.0034845943894685123" + 
":  " + 
"0.05265478846111052" + 
":  " + 
"(b('L8b4') <= 813.5) ? " + 
"-0.013868010203489168" + 
":  " + 
"-6.990647932950873e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 1987972.5) ? " + 
"(b('dsvv') <= 5.5451555252075195) ? " + 
"(b('dgvv') <= 4.7487993240356445) ? " + 
"-0.0004338657027725008" + 
":  " + 
"0.023435962625658953" + 
":  " + 
"(b('L8b4') <= 1440.0) ? " + 
"-0.05493616000359058" + 
":  " + 
"0.02691909599144368" + 
":  " + 
"(b('L8b6') <= 4860.5) ? " + 
"(b('L8b5med') <= 3538.25) ? " + 
"0.0019583645175537414" + 
":  " + 
"0.023644038811831133" + 
":  " + 
"(b('L8dt') <= 6459549.5) ? " + 
"-0.03595986317980978" + 
":  " + 
"0.048106108279780666" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 1198.0) ? " + 
"(b('L8b4') <= 2025.5) ? " + 
"(b('L8b3') <= 1493.5) ? " + 
"-0.00016887342155650546" + 
":  " + 
"0.017055269938381384" + 
":  " + 
"(b('L8b5') <= 3310.0) ? " + 
"-0.012223122926092693" + 
":  " + 
"0.0013585191066328493" + 
":  " + 
"(b('ndvi') <= 3130.0) ? " + 
"(b('L8dt') <= 2634975.0) ? " + 
"0.005040669810132646" + 
":  " + 
"-0.020692143573861746" + 
":  " + 
"(b('L8b6') <= 4416.0) ? " + 
"0.0011326655141033193" + 
":  " + 
"0.06589100728645035" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5med') <= 3385.5) ? " + 
"(b('L8b5') <= 3436.5) ? " + 
"-0.00019533475645683665" + 
":  " + 
"0.00916222968202559" + 
":  " + 
"(b('L8b5') <= 2970.5) ? " + 
"0.024236305071311765" + 
":  " + 
"-0.007016629548091516" + 
":  " + 
"(b('L8b5') <= 3525.5) ? " + 
"(b('ndvi') <= 4326.0) ? " + 
"-0.05892555774477038" + 
":  " + 
"0.09769921264090835" + 
":  " + 
"(b('L8b3') <= 759.0) ? " + 
"-0.033295725009351004" + 
":  " + 
"-0.0006658981706735179" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b6') <= 2841.5) ? " + 
"(b('L8b7med') <= 2880.75) ? " + 
"0.001237480909550588" + 
":  " + 
"-0.019237096193636723" + 
":  " + 
"(b('L8b11') <= 2229.5) ? " + 
"0.02331917103509378" + 
":  " + 
"0.12480767618247131" + 
":  " + 
"(b('L8b2med') <= 340.0) ? " + 
"(b('ndvi') <= 2803.0) ? " + 
"0.11797752986204928" + 
":  " + 
"-0.034107486047264594" + 
":  " + 
"(b('L8b11') <= 2270.5) ? " + 
"-0.005514712794936663" + 
":  " + 
"0.0008776770802511175" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 604.5) ? " + 
"(b('L8dt') <= 518400.5) ? " + 
"0.02081630772692218" + 
":  " + 
"0.15969270768867572" + 
":  " + 
"(b('L8b5') <= 1320.5) ? " + 
"(b('L8b3') <= 693.0) ? " + 
"-0.01101035019838812" + 
":  " + 
"-0.06988425533955098" + 
":  " + 
"(b('L8b5') <= 1681.0) ? " + 
"0.007307587298099613" + 
":  " + 
"-0.00015206292493674567" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 770.5) ? " + 
"(b('L8b5') <= 3612.0) ? " + 
"(b('L8b5med') <= 3285.0) ? " + 
"-0.0005642811001089327" + 
":  " + 
"-0.02102909621283187" + 
":  " + 
"(b('L8b5') <= 3640.0) ? " + 
"-0.07252934330139935" + 
":  " + 
"-0.017574646464466843" + 
":  " + 
"(b('L8b4') <= 799.5) ? " + 
"(b('L8b5med') <= 3385.5) ? " + 
"0.008517571037377117" + 
":  " + 
"0.05937483153362141" + 
":  " + 
"(b('L8dt') <= 846.5) ? " + 
"-0.11787299855029368" + 
":  " + 
"-3.7844058731410806e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -2.87725567817688) ? " + 
"(b('lat') <= 35.83924865722656) ? " + 
"(b('ndvi_med') <= 2762.0) ? " + 
"0.010728939961346419" + 
":  " + 
"-0.0633439770226475" + 
":  " + 
"(b('lon') <= 9.146950244903564) ? " + 
"0.0010568150656183018" + 
":  " + 
"-0.024811627394142215" + 
":  " + 
"(b('ndvi') <= 5203.0) ? " + 
"(b('ndvi') <= 5170.0) ? " + 
"0.0003757604666817173" + 
":  " + 
"0.0464368457177139" + 
":  " + 
"(b('L8b5') <= 2831.5) ? " + 
"-0.01982078049244663" + 
":  " + 
"-0.00024358564560956683" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b2') <= 181.5) ? " + 
"(b('sand') <= 78.0) ? " + 
"-0.0033507974256830543" + 
":  " + 
"0.05075828105172513" + 
":  " + 
"(b('ndvi') <= 3451.5) ? " + 
"-0.020860560857323854" + 
":  " + 
"-0.07664757309989306" + 
":  " + 
"(b('L8b5') <= 2036.5) ? " + 
"(b('L8b2med') <= 841.25) ? " + 
"0.004917221322473249" + 
":  " + 
"-0.01986350876364768" + 
":  " + 
"(b('L8b2') <= 200.5) ? " + 
"-0.0826417047175576" + 
":  " + 
"-0.00030325718044781156" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3369.5) ? " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b3') <= 882.5) ? " + 
"-0.0009261939903622678" + 
":  " + 
"0.006523386067539186" + 
":  " + 
"(b('L8b2med') <= 398.0) ? " + 
"0.02072513007965858" + 
":  " + 
"-0.004136172455180805" + 
":  " + 
"(b('L8b6') <= 3467.5) ? " + 
"(b('L8b6med') <= 3686.5) ? " + 
"0.012578291762115803" + 
":  " + 
"-0.0009364913775484273" + 
":  " + 
"(b('L8b5') <= 3431.0) ? " + 
"-0.0034654806418452735" + 
":  " + 
"0.0054688486536212865" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5med') <= 3153.0) ? " + 
"(b('L8b5') <= 3233.5) ? " + 
"-0.000717303446528107" + 
":  " + 
"0.004693463959646986" + 
":  " + 
"(b('L8b6') <= 2589.5) ? " + 
"0.015188015161178724" + 
":  " + 
"0.0008366762982899271" + 
":  " + 
"(b('L8b5med') <= 3138.5) ? " + 
"(b('ndvi') <= 6604.5) ? " + 
"0.0033070652139749646" + 
":  " + 
"0.09023024732001143" + 
":  " + 
"(b('L8b5med') <= 3213.5) ? " + 
"-0.035177073025984884" + 
":  " + 
"-0.0038418499969863442" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 48.65084648132324) ? " + 
"(b('dgvv') <= 0.777130126953125) ? " + 
"(b('sand') <= 26.0) ? " + 
"-0.010251771194816642" + 
":  " + 
"0.0003101999131511961" + 
":  " + 
"(b('sand') <= 19.0) ? " + 
"0.04210193263795967" + 
":  " + 
"0.005077392492035205" + 
":  " + 
"(b('dsvv') <= 0.6254949569702148) ? " + 
"(b('lat') <= 39.95979881286621) ? " + 
"-0.009775103826719242" + 
":  " + 
"0.0017077817056601267" + 
":  " + 
"(b('lat') <= 41.200754165649414) ? " + 
"0.005086151806132562" + 
":  " + 
"-0.005995161389425974" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 823.5) ? " + 
"(b('lon') <= -69.40549850463867) ? " + 
"(b('crops') <= 33.79139518737793) ? " + 
"-0.0005295161452229734" + 
":  " + 
"-0.015238063744856308" + 
":  " + 
"(b('L8b5med') <= 3206.0) ? " + 
"0.00019977346477435725" + 
":  " + 
"0.019831831596231902" + 
":  " + 
"(b('L8b2med') <= 392.5) ? " + 
"(b('L8b6') <= 2954.0) ? " + 
"-0.02599050731391654" + 
":  " + 
"0.07072994460545423" + 
":  " + 
"(b('L8b4') <= 944.5) ? " + 
"0.00784767359443423" + 
":  " + 
"-0.00013365727967299738" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2907.5) ? " + 
"(b('L8b11') <= 2889.5) ? " + 
"(b('L8b5') <= 3381.5) ? " + 
"0.0005092602836155455" + 
":  " + 
"-0.0046694708399300676" + 
":  " + 
"(b('crops') <= 76.58172988891602) ? " + 
"-0.0021268783204687488" + 
":  " + 
"-0.047619015568981016" + 
":  " + 
"(b('L8b11') <= 2913.0) ? " + 
"(b('ndvi') <= 1258.5) ? " + 
"0.08049175576884222" + 
":  " + 
"0.01998541506087792" + 
":  " + 
"(b('ndvi') <= 2627.5) ? " + 
"8.610619535758125e-05" + 
":  " + 
"0.01648912471753611" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2385.25) ? " + 
"(b('L8b4') <= 1224.5) ? " + 
"(b('lon') <= -118.87322616577148) ? " + 
"0.018121967838817487" + 
":  " + 
"-0.0019818356022871485" + 
":  " + 
"(b('L8b3') <= 1068.5) ? " + 
"-0.01621600808628133" + 
":  " + 
"-0.0033341639286559393" + 
":  " + 
"(b('L8b5med') <= 2399.0) ? " + 
"(b('ndvi') <= 1946.0) ? " + 
"-0.014640638777180129" + 
":  " + 
"0.12723265031630582" + 
":  " + 
"(b('dgvv') <= -2.87725567817688) ? " + 
"-0.007087626168488388" + 
":  " + 
"0.0006005224532020834" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 933.5) ? " + 
"(b('L8b6') <= 3242.5) ? " + 
"(b('lon') <= 25.446414947509766) ? " + 
"0.0003812498038206155" + 
":  " + 
"-0.009900231723787435" + 
":  " + 
"(b('L8b7med') <= 1672.5) ? " + 
"-0.059663571491668975" + 
":  " + 
"-0.0071971753273209265" + 
":  " + 
"(b('L8b4') <= 1289.5) ? " + 
"(b('crops') <= 62.03993225097656) ? " + 
"0.013380234492810898" + 
":  " + 
"-0.0023093007750342016" + 
":  " + 
"(b('L8b2') <= 591.5) ? " + 
"0.020284731532648557" + 
":  " + 
"-0.0013718132179521567" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3255199.5) ? " + 
"(b('lat') <= 44.514474868774414) ? " + 
"(b('ndvi') <= 2646.0) ? " + 
"-0.0007001394074328041" + 
":  " + 
"0.003449122408891044" + 
":  " + 
"(b('L8b3') <= 1382.0) ? " + 
"-0.0026668691797487494" + 
":  " + 
"0.032215308238110966" + 
":  " + 
"(b('dsvv') <= 6.625141620635986) ? " + 
"(b('crops') <= 87.44597244262695) ? " + 
"0.0010220702528883972" + 
":  " + 
"0.01483394719455054" + 
":  " + 
"0.17541300900561785" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3369.5) ? " + 
"(b('L8b4') <= 2109.5) ? " + 
"(b('L8b3') <= 1420.5) ? " + 
"-0.0008609138843724358" + 
":  " + 
"0.01177993093302212" + 
":  " + 
"(b('crops') <= 88.85982513427734) ? " + 
"-0.0020319431191217208" + 
":  " + 
"-0.03731413574910843" + 
":  " + 
"(b('L8b6') <= 3467.5) ? " + 
"(b('L8b11') <= 2275.5) ? " + 
"0.001586625761330522" + 
":  " + 
"0.014387430077429134" + 
":  " + 
"(b('ndvi') <= 3017.5) ? " + 
"-0.0017098882742793394" + 
":  " + 
"0.01207697012576088" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2907.5) ? " + 
"(b('L8b11') <= 2889.5) ? " + 
"(b('L8b5') <= 3381.5) ? " + 
"0.00044591255256553984" + 
":  " + 
"-0.004404760364395888" + 
":  " + 
"(b('crops') <= 76.58172988891602) ? " + 
"-0.0022280149126993973" + 
":  " + 
"-0.04235717771340041" + 
":  " + 
"(b('L8b11') <= 2914.5) ? " + 
"(b('ndvi') <= 1258.5) ? " + 
"0.06907533780753321" + 
":  " + 
"0.01845588001886261" + 
":  " + 
"(b('ndvi') <= 2627.5) ? " + 
"0.0003739313680180681" + 
":  " + 
"0.014214617509456516" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 3245.0) ? " + 
"(b('L8b6') <= 3305.5) ? " + 
"(b('lon') <= -118.93999481201172) ? " + 
"0.006380502339347929" + 
":  " + 
"1.2093979259629546e-05" + 
":  " + 
"(b('L8b11') <= 1917.0) ? " + 
"-0.07484338862576508" + 
":  " + 
"-0.0019620298197982238" + 
":  " + 
"(b('dgvv') <= 0.4458165168762207) ? " + 
"(b('ndvi') <= 2923.0) ? " + 
"0.005716722562247009" + 
":  " + 
"0.03576859147723948" + 
":  " + 
"(b('lon') <= -5.235889911651611) ? " + 
"-0.007262483399617269" + 
":  " + 
"0.029414288121902738" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4784.5) ? " + 
"(b('dsvv') <= 3.8659508228302) ? " + 
"(b('dgvv') <= 3.8783535957336426) ? " + 
"-0.0001524713936533384" + 
":  " + 
"-0.12713690671280406" + 
":  " + 
"(b('ndvi_med') <= 3604.0) ? " + 
"0.011599842324543684" + 
":  " + 
"-0.01908729813054429" + 
":  " + 
"(b('L8b2med') <= 745.5) ? " + 
"(b('ndvi') <= 3279.5) ? " + 
"0.06996288929259774" + 
":  " + 
"0.045326994271821935" + 
":  " + 
"(b('dsvv') <= 4.139361381530762) ? " + 
"0.00189382004154013" + 
":  " + 
"0.008366347395979482" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 1898.0) ? " + 
"(b('L8b2') <= 509.5) ? " + 
"(b('L8b11') <= 1271.5) ? " + 
"-0.007204156234039591" + 
":  " + 
"-0.04867418495608214" + 
":  " + 
"(b('ndvi') <= 2586.0) ? " + 
"-0.009732303898905911" + 
":  " + 
"0.061829701497635815" + 
":  " + 
"(b('L8b5') <= 2036.5) ? " + 
"(b('L8b2med') <= 841.25) ? " + 
"0.004883532463182524" + 
":  " + 
"-0.01831323903120182" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"0.009740743508833196" + 
":  " + 
"-0.0004999520825339264" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('lon') <= 22.38558006286621) ? " + 
"(b('L8b6') <= 2381.5) ? " + 
"-0.0018918473416392235" + 
":  " + 
"-0.020571617212535656" + 
":  " + 
"(b('ndvi') <= 5406.5) ? " + 
"0.004558640931746956" + 
":  " + 
"0.09048652548624847" + 
":  " + 
"(b('L8b2') <= 464.5) ? " + 
"(b('lat') <= 41.29464912414551) ? " + 
"0.013092089517544953" + 
":  " + 
"-0.0001109412541523489" + 
":  " + 
"(b('L8b11') <= 1651.5) ? " + 
"-0.008527383173875787" + 
":  " + 
"0.0004499491431270076" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 759.5) ? " + 
"(b('L8b5med') <= 3285.0) ? " + 
"(b('ndvi') <= 1310.0) ? " + 
"-0.027614261331514907" + 
":  " + 
"-0.00031789440301345067" + 
":  " + 
"(b('L8b3') <= 709.0) ? " + 
"-0.04110764155931332" + 
":  " + 
"-0.0021079404408470472" + 
":  " + 
"(b('L8b2') <= 419.5) ? " + 
"(b('L8b3') <= 865.0) ? " + 
"0.01822681359723147" + 
":  " + 
"-0.01457886775506372" + 
":  " + 
"(b('L8b2') <= 424.5) ? " + 
"-0.025966646846083297" + 
":  " + 
"0.00021282288131854637" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 363.5) ? " + 
"(b('L8b4') <= 612.5) ? " + 
"(b('sand') <= 24.5) ? " + 
"-0.0269489588744526" + 
":  " + 
"0.00729899843583285" + 
":  " + 
"(b('lat') <= 55.879150390625) ? " + 
"-0.003302523805688345" + 
":  " + 
"-0.0262787159637161" + 
":  " + 
"(b('L8b2') <= 396.5) ? " + 
"(b('L8b7med') <= 1303.5) ? " + 
"-0.028814105837136575" + 
":  " + 
"0.0081075375307074" + 
":  " + 
"(b('lat') <= 56.0489501953125) ? " + 
"-5.457012971666423e-05" + 
":  " + 
"-0.08347975817754574" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3255199.5) ? " + 
"(b('L8b3') <= 1708.5) ? " + 
"(b('L8b4') <= 2018.5) ? " + 
"3.761129183936692e-05" + 
":  " + 
"-0.007332321121257413" + 
":  " + 
"(b('ndvi') <= 3112.5) ? " + 
"0.0028813264699010786" + 
":  " + 
"0.04167050494309832" + 
":  " + 
"(b('lat') <= 56.023799896240234) ? " + 
"(b('lat') <= 55.91889953613281) ? " + 
"0.0031177908607770673" + 
":  " + 
"0.025891022596418508" + 
":  " + 
"(b('L8b4') <= 904.0) ? " + 
"-0.005457867994449883" + 
":  " + 
"-0.06269651069411376" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 822.5) ? " + 
"(b('L8b2') <= 478.5) ? " + 
"(b('L8b2') <= 476.5) ? " + 
"-2.1157743028792097e-05" + 
":  " + 
"0.04812159667978882" + 
":  " + 
"(b('L8b2') <= 481.5) ? " + 
"-0.03535953110475978" + 
":  " + 
"-0.0047627280457746765" + 
":  " + 
"(b('L8b2med') <= 392.5) ? " + 
"(b('L8b6') <= 2954.0) ? " + 
"-0.023495589443242565" + 
":  " + 
"0.06387344146833861" + 
":  " + 
"(b('L8b4') <= 944.5) ? " + 
"0.0068930323849088985" + 
":  " + 
"-0.00012007784254141757" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5203.0) ? " + 
"(b('ndvi') <= 5170.0) ? " + 
"(b('L8dt') <= 3717016.5) ? " + 
"-7.786536321029055e-05" + 
":  " + 
"0.006399701614317538" + 
":  " + 
"(b('L8b3') <= 988.0) ? " + 
"0.004912834811088531" + 
":  " + 
"0.09205834765425" + 
":  " + 
"(b('ndvi') <= 5739.5) ? " + 
"(b('L8b5') <= 4015.0) ? " + 
"-0.015072815029712602" + 
":  " + 
"0.0628812815456149" + 
":  " + 
"(b('L8b6') <= 1830.5) ? " + 
"-0.04462634740375697" + 
":  " + 
"0.005457841801243988" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b4') <= 494.5) ? " + 
"(b('sand') <= 78.0) ? " + 
"-0.013956034217938635" + 
":  " + 
"0.044977789156983916" + 
":  " + 
"(b('L8dt') <= 274393.5) ? " + 
"-0.05098469709942358" + 
":  " + 
"-0.07798271733765641" + 
":  " + 
"(b('L8b5') <= 1681.0) ? " + 
"(b('L8b7med') <= 1624.5) ? " + 
"0.03058842081286994" + 
":  " + 
"-0.0016666971506890118" + 
":  " + 
"(b('L8b6med') <= 2069.625) ? " + 
"-0.016821543874603044" + 
":  " + 
"5.006153918855064e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5med') <= 3385.5) ? " + 
"(b('L8b5') <= 3256.5) ? " + 
"-0.00040970045068295177" + 
":  " + 
"0.0041999911552278646" + 
":  " + 
"(b('L8b5') <= 2970.5) ? " + 
"0.0206954798206675" + 
":  " + 
"-0.005698554378953858" + 
":  " + 
"(b('L8b5') <= 3519.5) ? " + 
"(b('dsvv') <= -3.387826442718506) ? " + 
"-0.0010152132812218904" + 
":  " + 
"-0.07887702265878406" + 
":  " + 
"(b('L8b6') <= 2410.5) ? " + 
"0.010218087515620169" + 
":  " + 
"-0.004171893369925481" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2974.5) ? " + 
"(b('L8b5') <= 3518.0) ? " + 
"(b('lat') <= -28.00918483734131) ? " + 
"-0.020701400314854047" + 
":  " + 
"0.00031203216008839" + 
":  " + 
"(b('lat') <= 43.18190002441406) ? " + 
"-0.010191264018723173" + 
":  " + 
"0.00518685258868473" + 
":  " + 
"(b('ndvi') <= 2627.5) ? " + 
"(b('L8b2') <= 935.5) ? " + 
"0.006214685030324976" + 
":  " + 
"-0.0010206007446716967" + 
":  " + 
"(b('lat') <= 41.29277992248535) ? " + 
"0.03200815581779122" + 
":  " + 
"0.005614408241323816" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3665.5) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4326.5) ? " + 
"-1.350731251247402e-05" + 
":  " + 
"0.04578099738999142" + 
":  " + 
"(b('L8b5') <= 4771.0) ? " + 
"-0.01869969440598495" + 
":  " + 
"0.038845163566906635" + 
":  " + 
"(b('L8dt') <= 2068235.5) ? " + 
"(b('L8b11') <= 3943.5) ? " + 
"0.0267185000169014" + 
":  " + 
"0.0017155597573917443" + 
":  " + 
"(b('dgvv') <= 1.7280030250549316) ? " + 
"-0.0170637521278793" + 
":  " + 
"-0.05200713177673355" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3425.75) ? " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b6') <= 2841.5) ? " + 
"0.0005445035764174593" + 
":  " + 
"0.02654469842896214" + 
":  " + 
"(b('L8b2med') <= 340.0) ? " + 
"0.048106700694761285" + 
":  " + 
"-0.003111832841195382" + 
":  " + 
"(b('L8b6') <= 3467.5) ? " + 
"(b('L8b7med') <= 2880.75) ? " + 
"0.00997385800190029" + 
":  " + 
"-0.00435799672615727" + 
":  " + 
"(b('dgvv') <= 0.37421369552612305) ? " + 
"0.0019576854551985874" + 
":  " + 
"-0.005382011613902621" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 882.5) ? " + 
"(b('L8b5') <= 4210.5) ? " + 
"(b('L8b3') <= 860.5) ? " + 
"-0.0005449659767011862" + 
":  " + 
"-0.011140980500797218" + 
":  " + 
"(b('L8dt') <= 1015396.0) ? " + 
"0.07703868669077624" + 
":  " + 
"0.028546213907507886" + 
":  " + 
"(b('L8b4') <= 1231.5) ? " + 
"(b('ndvi_med') <= 1554.5) ? " + 
"0.025010913210075914" + 
":  " + 
"0.004062468990482835" + 
":  " + 
"(b('L8b5') <= 2209.5) ? " + 
"-0.009959547683343978" + 
":  " + 
"5.2632309501311976e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1339.0) ? " + 
"(b('ndvi') <= 1475.0) ? " + 
"(b('dgvv') <= 1.6982908248901367) ? " + 
"-7.627064524451423e-05" + 
":  " + 
"0.020211199889992957" + 
":  " + 
"(b('dsvv') <= -1.0163888931274414) ? " + 
"0.05818750013473197" + 
":  " + 
"0.01300406545271252" + 
":  " + 
"(b('ndvi') <= 1169.0) ? " + 
"(b('ndvi') <= 1166.0) ? " + 
"-0.00454085277377856" + 
":  " + 
"-0.03739212116291267" + 
":  " + 
"(b('ndvi') <= 1179.5) ? " + 
"0.066715237465903" + 
":  " + 
"-3.0198486859718527e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 933.5) ? " + 
"(b('L8b6') <= 3209.0) ? " + 
"(b('L8b4') <= 1206.5) ? " + 
"-7.050062327367732e-05" + 
":  " + 
"-0.02534852297169442" + 
":  " + 
"(b('L8b6med') <= 2683.25) ? " + 
"-0.1070826444962203" + 
":  " + 
"-0.01011874893323514" + 
":  " + 
"(b('L8b4') <= 1289.5) ? " + 
"(b('crops') <= 62.03993225097656) ? " + 
"0.011643288850303562" + 
":  " + 
"-0.00219454455332303" + 
":  " + 
"(b('L8b2') <= 591.5) ? " + 
"0.017751839081611306" + 
":  " + 
"-0.0011563677820033411" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2907.5) ? " + 
"(b('L8b11') <= 2889.5) ? " + 
"(b('lat') <= -28.00918483734131) ? " + 
"-0.019448962269459497" + 
":  " + 
"-0.00014483685975790237" + 
":  " + 
"(b('crops') <= 76.58172988891602) ? " + 
"-0.0021384787873880372" + 
":  " + 
"-0.03776409921367187" + 
":  " + 
"(b('L8b11') <= 2914.5) ? " + 
"(b('ndvi') <= 1258.5) ? " + 
"0.06286618443323964" + 
":  " + 
"0.016351162128709545" + 
":  " + 
"(b('L8b2') <= 935.5) ? " + 
"0.005907887652492265" + 
":  " + 
"-0.0010878759911084957" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5203.0) ? " + 
"(b('ndvi') <= 5170.0) ? " + 
"(b('ndvi') <= 4299.0) ? " + 
"-0.00017800362772762773" + 
":  " + 
"0.004092669205197671" + 
":  " + 
"(b('ndvi_med') <= 2744.5) ? " + 
"0.08330984795835264" + 
":  " + 
"0.0037558079709783866" + 
":  " + 
"(b('lat') <= 35.61929893493652) ? " + 
"(b('ndvi') <= 5355.0) ? " + 
"-0.062044633412186384" + 
":  " + 
"-0.022071144203208503" + 
":  " + 
"(b('L8b5') <= 2831.5) ? " + 
"-0.016412449628973664" + 
":  " + 
"0.003103630462406453" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 3444.0) ? " + 
"(b('L8b3') <= 2317.0) ? " + 
"(b('L8b11') <= 3363.5) ? " + 
"-0.00013088496939373868" + 
":  " + 
"-0.011868601783921158" + 
":  " + 
"(b('ndvi') <= 1006.5) ? " + 
"0.10999556165318516" + 
":  " + 
"0.04596020421953159" + 
":  " + 
"(b('L8b5') <= 3768.0) ? " + 
"(b('ndvi') <= 1945.5) ? " + 
"0.006196580663612661" + 
":  " + 
"0.02854046793980088" + 
":  " + 
"(b('L8dt') <= 1124940.0) ? " + 
"0.002646841492604177" + 
":  " + 
"-0.026335006384993274" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 179923.5) ? " + 
"(b('lat') <= 55.94395065307617) ? " + 
"(b('L8dt') <= 65970.5) ? " + 
"0.002641425387876348" + 
":  " + 
"-0.003355219476467481" + 
":  " + 
"(b('ndvi') <= 3092.5) ? " + 
"0.053397445335489284" + 
":  " + 
"-0.030272124630974725" + 
":  " + 
"(b('L8dt') <= 179953.5) ? " + 
"(b('ndvi') <= 1962.5) ? " + 
"0.006674864226317363" + 
":  " + 
"0.06676389920007605" + 
":  " + 
"(b('crops') <= 48.65084648132324) ? " + 
"0.00135924552117004" + 
":  " + 
"-0.0007559193594170572" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2974.5) ? " + 
"(b('L8b5') <= 3381.5) ? " + 
"(b('ndvi_med') <= 4919.5) ? " + 
"0.00010092234952862595" + 
":  " + 
"0.01688843876359969" + 
":  " + 
"(b('L8b5med') <= 3076.0) ? " + 
"0.003462408109244563" + 
":  " + 
"-0.00810419706920296" + 
":  " + 
"(b('ndvi') <= 1537.0) ? " + 
"(b('ndvi_med') <= 1712.5) ? " + 
"0.0014533288487321532" + 
":  " + 
"-0.014545761975288712" + 
":  " + 
"(b('L8b11') <= 3007.5) ? " + 
"0.02816071626116936" + 
":  " + 
"0.0048850428635651335" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 3.8659508228302) ? " + 
"(b('L8b3') <= 759.5) ? " + 
"(b('L8b2med') <= 502.5) ? " + 
"0.0009869499279939668" + 
":  " + 
"-0.006723415465204813" + 
":  " + 
"(b('L8b2') <= 415.5) ? " + 
"0.013020742815748854" + 
":  " + 
"-2.878186559545144e-05" + 
":  " + 
"(b('L8b5med') <= 3217.75) ? " + 
"(b('L8b5') <= 3126.5) ? " + 
"0.006509678703318358" + 
":  " + 
"0.04874943806093721" + 
":  " + 
"(b('L8dt') <= 1100697.0) ? " + 
"-0.03616881091306853" + 
":  " + 
"0.011153929750209962" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2142.5) ? " + 
"(b('L8b5') <= 2140.5) ? " + 
"(b('L8b6med') <= 3837.0) ? " + 
"0.0023789213888623546" + 
":  " + 
"-0.024227781744998105" + 
":  " + 
"(b('L8dt') <= 302374.5) ? " + 
"0.012870506839845173" + 
":  " + 
"0.07901531807093812" + 
":  " + 
"(b('L8b5') <= 2149.5) ? " + 
"(b('L8b2med') <= 866.0) ? " + 
"-0.01605147075052252" + 
":  " + 
"-0.06701772218473043" + 
":  " + 
"(b('L8b5') <= 2154.5) ? " + 
"0.027760651856136877" + 
":  " + 
"-0.00037219143507781" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 26.056610107421875) ? " + 
"(b('L8b5med') <= 1898.0) ? " + 
"(b('L8b11') <= 2181.5) ? " + 
"-0.017121374929979387" + 
":  " + 
"0.024003043921770696" + 
":  " + 
"(b('L8b5') <= 2036.5) ? " + 
"0.0038861775597535016" + 
":  " + 
"-6.354640357578666e-05" + 
":  " + 
"(b('L8b5') <= 3249.5) ? " + 
"(b('L8b6') <= 2498.5) ? " + 
"-0.016580878538913893" + 
":  " + 
"-6.587308649868255e-05" + 
":  " + 
"(b('L8b4') <= 729.5) ? " + 
"0.0695916619277612" + 
":  " + 
"0.008380061411934562" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 437.0) ? " + 
"(b('L8b2') <= 181.5) ? " + 
"(b('L8dt') <= 1357251.0) ? " + 
"0.019681421668558664" + 
":  " + 
"-0.020639318088597043" + 
":  " + 
"(b('ndvi') <= 3451.5) ? " + 
"-0.018118241169761143" + 
":  " + 
"-0.06304918276245867" + 
":  " + 
"(b('L8b2') <= 316.5) ? " + 
"(b('L8b7med') <= 1324.0) ? " + 
"0.02533534188617246" + 
":  " + 
"0.000675791306525631" + 
":  " + 
"(b('L8b4') <= 463.5) ? " + 
"0.12695246390278586" + 
":  " + 
"-0.00013522278856263717" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 363.5) ? " + 
"(b('dsvv') <= -0.8258671760559082) ? " + 
"(b('L8b6') <= 2137.5) ? " + 
"-0.0008150263917286105" + 
":  " + 
"-0.033181749944420524" + 
":  " + 
"(b('L8b4') <= 612.5) ? " + 
"0.007003435578789998" + 
":  " + 
"-0.006426449044372685" + 
":  " + 
"(b('L8b2med') <= 395.5) ? " + 
"(b('ndvi') <= 3029.0) ? " + 
"0.03624221134043068" + 
":  " + 
"-0.000863552359480255" + 
":  " + 
"(b('L8b6') <= 1385.5) ? " + 
"-0.0458427314713237" + 
":  " + 
"6.777612500699668e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6286332.0) ? " + 
"(b('L8b5') <= 1320.5) ? " + 
"(b('L8dt') <= 1206741.5) ? " + 
"-0.003075562875034402" + 
":  " + 
"-0.05239302533545748" + 
":  " + 
"(b('L8b5') <= 1356.0) ? " + 
"0.028704890190632326" + 
":  " + 
"-3.7591406033570576e-05" + 
":  " + 
"(b('ndvi') <= 1568.5) ? " + 
"(b('ndvi_med') <= 1646.5) ? " + 
"0.04979214236624332" + 
":  " + 
"0.003846550037368307" + 
":  " + 
"(b('L8dt') <= 6350196.0) ? " + 
"0.10187196402376902" + 
":  " + 
"0.005434760377713983" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2385.25) ? " + 
"(b('L8b4') <= 1224.5) ? " + 
"(b('lon') <= -118.87322616577148) ? " + 
"0.014769402844912112" + 
":  " + 
"-0.001561359841641091" + 
":  " + 
"(b('lat') <= 46.50404930114746) ? " + 
"-0.004798034157390607" + 
":  " + 
"-0.02398824595354763" + 
":  " + 
"(b('L8b5med') <= 2399.0) ? " + 
"(b('ndvi') <= 1946.0) ? " + 
"-0.012526327041743224" + 
":  " + 
"0.10795559349282281" + 
":  " + 
"(b('L8b5') <= 2436.5) ? " + 
"0.002916149851162409" + 
":  " + 
"-0.0003286619514923737" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 822.5) ? " + 
"(b('lon') <= -69.40549850463867) ? " + 
"(b('L8b5med') <= 3215.0) ? " + 
"-0.003088844076375802" + 
":  " + 
"-0.02185500550814495" + 
":  " + 
"(b('L8b5med') <= 3206.0) ? " + 
"0.0004090488218692309" + 
":  " + 
"0.01776553834291903" + 
":  " + 
"(b('L8b2med') <= 392.5) ? " + 
"(b('L8b6') <= 2954.0) ? " + 
"-0.023193683691282132" + 
":  " + 
"0.05341695288260454" + 
":  " + 
"(b('L8b4') <= 944.5) ? " + 
"0.006201642203329029" + 
":  " + 
"-5.652711086351898e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1443.5) ? " + 
"(b('L8b6') <= 2410.5) ? " + 
"(b('L8b6') <= 2407.0) ? " + 
"0.0006411800069377417" + 
":  " + 
"0.05495810085630629" + 
":  " + 
"(b('L8b2med') <= 336.0) ? " + 
"-0.0480385210148345" + 
":  " + 
"-0.00754704211457289" + 
":  " + 
"(b('L8b4') <= 835.5) ? " + 
"(b('lon') <= 29.159395217895508) ? " + 
"0.0058756845440721215" + 
":  " + 
"0.11957851926062332" + 
":  " + 
"(b('L8b11') <= 1469.5) ? " + 
"0.03587740786464315" + 
":  " + 
"-0.000619582354060693" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 933.5) ? " + 
"(b('L8b6') <= 3209.0) ? " + 
"(b('L8b4') <= 1206.5) ? " + 
"-0.0001989870511522102" + 
":  " + 
"-0.02237961680051427" + 
":  " + 
"(b('L8b6med') <= 2683.25) ? " + 
"-0.09759963506177131" + 
":  " + 
"-0.008875962215051807" + 
":  " + 
"(b('L8b4') <= 1232.5) ? " + 
"(b('lon') <= -111.32536697387695) ? " + 
"0.03217562184151559" + 
":  " + 
"0.004417591459807254" + 
":  " + 
"(b('L8b7med') <= 1762.5) ? " + 
"0.008603393651837923" + 
":  " + 
"-0.0009495650444831755" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3369.5) ? " + 
"(b('L8b4') <= 2347.5) ? " + 
"(b('L8b11') <= 2725.0) ? " + 
"-0.0008580041043358182" + 
":  " + 
"0.006714644016314104" + 
":  " + 
"(b('crops') <= 88.85982513427734) ? " + 
"-0.011722249968898764" + 
":  " + 
"-0.05698470510332144" + 
":  " + 
"(b('ndvi') <= 3255.0) ? " + 
"(b('dsvv') <= 6.627758979797363) ? " + 
"0.0006586450358506533" + 
":  " + 
"-0.1640759844672201" + 
":  " + 
"(b('lat') <= 41.37735939025879) ? " + 
"0.016334589593315605" + 
":  " + 
"-0.008698556681873682" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 4758.5) ? " + 
"(b('ndvi') <= 4430.5) ? " + 
"(b('ndvi_med') <= 4469.0) ? " + 
"-0.00029259945763082315" + 
":  " + 
"0.020270961153838748" + 
":  " + 
"(b('crops') <= 0.6078431606292725) ? " + 
"0.07299528189734773" + 
":  " + 
"0.0078101596549846955" + 
":  " + 
"(b('sand') <= 73.0) ? " + 
"(b('L8b6') <= 2813.0) ? " + 
"0.0045207821148204475" + 
":  " + 
"-0.010365833874901201" + 
":  " + 
"(b('L8b2med') <= 401.0) ? " + 
"-0.04659470104342096" + 
":  " + 
"-0.012420534012241339" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1651.5) ? " + 
"(b('lon') <= 29.159395217895508) ? " + 
"(b('L8b2') <= 472.5) ? " + 
"0.0004895161696773762" + 
":  " + 
"-0.008737283134092033" + 
":  " + 
"(b('L8b11') <= 1571.5) ? " + 
"0.01148611415818252" + 
":  " + 
"0.12074314165892516" + 
":  " + 
"(b('L8b11') <= 1654.5) ? " + 
"(b('L8dt') <= 1713963.5) ? " + 
"0.040022327573845114" + 
":  " + 
"0.11291079886069405" + 
":  " + 
"(b('L8dt') <= 358.0) ? " + 
"-0.19802731232778742" + 
":  " + 
"0.00038484563859788587" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1708.5) ? " + 
"(b('L8b4') <= 2018.5) ? " + 
"(b('L8b3') <= 1493.5) ? " + 
"-0.00019421456986137107" + 
":  " + 
"0.01286986206558114" + 
":  " + 
"(b('L8dt') <= 2744388.0) ? " + 
"-0.006698117323494772" + 
":  " + 
"0.01625074494189378" + 
":  " + 
"(b('L8b7med') <= 2004.25) ? " + 
"(b('dsvv') <= 0.5230870246887207) ? " + 
"0.02699821515754457" + 
":  " + 
"0.09109246869193165" + 
":  " + 
"(b('L8dt') <= 2526521.5) ? " + 
"0.00382833587481813" + 
":  " + 
"-0.017775791650139993" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 26.74935531616211) ? " + 
"(b('L8b5med') <= 1898.0) ? " + 
"(b('ndvi') <= 1061.0) ? " + 
"0.025608590053373653" + 
":  " + 
"-0.015626356031648636" + 
":  " + 
"(b('L8b5') <= 2036.5) ? " + 
"0.003345219356056691" + 
":  " + 
"-5.836972558337802e-05" + 
":  " + 
"(b('L8b5') <= 2986.5) ? " + 
"(b('lon') <= 28.338205337524414) ? " + 
"-0.01803536382095962" + 
":  " + 
"0.00438788678343357" + 
":  " + 
"(b('dsvv') <= 0.9334778785705566) ? " + 
"0.014445234500171865" + 
":  " + 
"-0.011752030000444516" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 826.5) ? " + 
"(b('L8b4') <= 738.5) ? " + 
"(b('lon') <= -119.03326797485352) ? " + 
"0.026723556853711476" + 
":  " + 
"0.0007243878185545927" + 
":  " + 
"(b('ndvi_med') <= 4919.5) ? " + 
"-0.0047344168282001135" + 
":  " + 
"0.04101910868175228" + 
":  " + 
"(b('L8b4') <= 944.5) ? " + 
"(b('ndvi') <= 1256.5) ? " + 
"0.29066566328978644" + 
":  " + 
"0.006066577167093469" + 
":  " + 
"(b('L8b11') <= 1646.5) ? " + 
"-0.011036455280757439" + 
":  " + 
"0.0006094189906618006" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 4758.5) ? " + 
"(b('ndvi') <= 4430.5) ? " + 
"(b('ndvi_med') <= 4469.0) ? " + 
"-0.0002460598376200529" + 
":  " + 
"0.01799126732814461" + 
":  " + 
"(b('crops') <= 0.6078431606292725) ? " + 
"0.06490587142079196" + 
":  " + 
"0.00705361262358081" + 
":  " + 
"(b('sand') <= 73.0) ? " + 
"(b('L8b5med') <= 3050.5) ? " + 
"0.006536974352553777" + 
":  " + 
"-0.006825857656946583" + 
":  " + 
"(b('L8b6') <= 2081.5) ? " + 
"-0.04677955967440055" + 
":  " + 
"-0.011355269261341257" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1443.5) ? " + 
"(b('L8b6') <= 2410.5) ? " + 
"(b('L8b6') <= 2407.0) ? " + 
"0.0004531928605280531" + 
":  " + 
"0.04891946706053788" + 
":  " + 
"(b('L8b2med') <= 336.0) ? " + 
"-0.04290921321451166" + 
":  " + 
"-0.0069100525367233896" + 
":  " + 
"(b('L8b4') <= 834.5) ? " + 
"(b('L8b6') <= 2613.5) ? " + 
"0.010783481143389546" + 
":  " + 
"-0.0008840175809201582" + 
":  " + 
"(b('L8b11') <= 1469.5) ? " + 
"0.032773853570231035" + 
":  " + 
"-0.0005220963568306956" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2461.0) ? " + 
"(b('L8b4') <= 697.5) ? " + 
"(b('lon') <= -119.03326797485352) ? " + 
"0.06149134981030516" + 
":  " + 
"0.0008963407214556725" + 
":  " + 
"(b('L8b2') <= 396.5) ? " + 
"-0.027979783136373546" + 
":  " + 
"-0.002159998497776122" + 
":  " + 
"(b('L8b5') <= 2436.5) ? " + 
"(b('L8b6') <= 2508.5) ? " + 
"-0.0016248001631206416" + 
":  " + 
"0.007722156138831374" + 
":  " + 
"(b('L8b5') <= 2464.5) ? " + 
"-0.02088952137868075" + 
":  " + 
"0.00015138463348328778" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 604.5) ? " + 
"(b('L8dt') <= 518400.5) ? " + 
"0.01167272532469596" + 
":  " + 
"0.13540291983533387" + 
":  " + 
"(b('L8b3') <= 461.5) ? " + 
"(b('L8b4') <= 507.5) ? " + 
"-0.0070362255905055265" + 
":  " + 
"-0.05182431122138349" + 
":  " + 
"(b('L8b2') <= 228.0) ? " + 
"-0.029675135321085" + 
":  " + 
"9.386276465702803e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2974.5) ? " + 
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b4') <= 1745.0) ? " + 
"0.0006716658037142987" + 
":  " + 
"-0.0041073337438536734" + 
":  " + 
"(b('lon') <= -5.367000102996826) ? " + 
"-0.011192061907816318" + 
":  " + 
"0.0013706839732459185" + 
":  " + 
"(b('ndvi') <= 2627.5) ? " + 
"(b('L8b7med') <= 2425.75) ? " + 
"-0.010743542740502699" + 
":  " + 
"0.0021108902253799784" + 
":  " + 
"(b('L8b3') <= 1445.5) ? " + 
"0.0009888336416668132" + 
":  " + 
"0.02210354025888571" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 933.5) ? " + 
"(b('L8b3') <= 930.5) ? " + 
"(b('lon') <= 26.056610107421875) ? " + 
"-6.851639348209064e-05" + 
":  " + 
"-0.0083036957300811" + 
":  " + 
"(b('L8b2med') <= 467.5) ? " + 
"-0.14831299987970697" + 
":  " + 
"-0.025595243524779876" + 
":  " + 
"(b('L8b4') <= 1289.5) ? " + 
"(b('L8b11') <= 1523.5) ? " + 
"-0.013556808946266041" + 
":  " + 
"0.0074335818284671515" + 
":  " + 
"(b('L8b2') <= 591.5) ? " + 
"0.015737915666455406" + 
":  " + 
"-0.0009645955232110518" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1339.0) ? " + 
"(b('ndvi') <= 1530.5) ? " + 
"(b('L8dt') <= 710878.0) ? " + 
"-0.0006649791134564095" + 
":  " + 
"0.01102824120039105" + 
":  " + 
"(b('lon') <= -120.8821029663086) ? " + 
"0.17202996538593188" + 
":  " + 
"0.017333794484683595" + 
":  " + 
"(b('ndvi') <= 1171.5) ? " + 
"(b('ndvi_med') <= 3287.0) ? " + 
"-0.005123045274136756" + 
":  " + 
"0.15470748385791358" + 
":  " + 
"(b('ndvi') <= 1179.5) ? " + 
"0.06591562526877497" + 
":  " + 
"-3.5721294582856954e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2461.0) ? " + 
"(b('L8b5') <= 1804.5) ? " + 
"(b('L8b5') <= 1801.5) ? " + 
"0.00432577501470858" + 
":  " + 
"0.15516363906563968" + 
":  " + 
"(b('ndvi_med') <= 2716.5) ? " + 
"-0.0015486847945989067" + 
":  " + 
"-0.007812751663364113" + 
":  " + 
"(b('crops') <= 34.76737403869629) ? " + 
"(b('dgvv') <= -1.5349669456481934) ? " + 
"-0.007707390107969785" + 
":  " + 
"0.003605009618673575" + 
":  " + 
"(b('lon') <= -5.546385049819946) ? " + 
"-0.004404794530507524" + 
":  " + 
"0.0005326918717149431" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 727.5) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"(b('L8b5med') <= 3285.0) ? " + 
"0.0002649654798138884" + 
":  " + 
"-0.03128455433655441" + 
":  " + 
"(b('L8b6') <= 2214.0) ? " + 
"-0.04329054294906172" + 
":  " + 
"-0.010489048281372603" + 
":  " + 
"(b('L8b4') <= 731.5) ? " + 
"(b('L8b5') <= 3303.0) ? " + 
"0.019862149907676364" + 
":  " + 
"-0.003145010510602593" + 
":  " + 
"(b('L8b11') <= 1027.5) ? " + 
"0.03861053385236689" + 
":  " + 
"-5.4030614042569215e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 411044.5) ? " + 
"(b('dgvv') <= 1.5580787658691406) ? " + 
"(b('L8b3') <= 601.5) ? " + 
"-0.014331488558984432" + 
":  " + 
"0.00017397963706105855" + 
":  " + 
"(b('L8b11') <= 2048.5) ? " + 
"0.0016315897722512247" + 
":  " + 
"-0.019186573632749702" + 
":  " + 
"(b('dsvv') <= -0.6760125160217285) ? " + 
"(b('crops') <= 91.13764572143555) ? " + 
"-0.003346898083729504" + 
":  " + 
"0.009673891942138396" + 
":  " + 
"(b('lon') <= 26.056610107421875) ? " + 
"0.002306081935114063" + 
":  " + 
"-0.00704048824568711" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4784.5) ? " + 
"(b('L8dt') <= 3219867.0) ? " + 
"(b('lat') <= 44.514474868774414) ? " + 
"0.0003963289389898156" + 
":  " + 
"-0.0018955735723008885" + 
":  " + 
"(b('L8b2med') <= 327.5) ? " + 
"0.028889372407404856" + 
":  " + 
"0.0021346277297552103" + 
":  " + 
"(b('L8b3') <= 1049.5) ? " + 
"(b('dsvv') <= 1.2694721221923828) ? " + 
"0.06931379005169137" + 
":  " + 
"0.05055145608301135" + 
":  " + 
"(b('dsvv') <= 4.139361381530762) ? " + 
"-0.005241575289970178" + 
":  " + 
"0.003925416975329499" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 3.8659508228302) ? " + 
"(b('dgvv') <= 3.8783535957336426) ? " + 
"(b('L8b3') <= 770.5) ? " + 
"-0.0016158882556085502" + 
":  " + 
"0.00035372245079864174" + 
":  " + 
"-0.11123625323552487" + 
":  " + 
"(b('ndvi_med') <= 3694.0) ? " + 
"(b('sand') <= 45.5) ? " + 
"0.025031373219911796" + 
":  " + 
"-2.161637066137705e-05" + 
":  " + 
"(b('ndvi_med') <= 3919.5) ? " + 
"-0.06659629318663879" + 
":  " + 
"-0.0036323699831897543" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 395.5) ? " + 
"(b('ndvi') <= 2750.5) ? " + 
"(b('lat') <= 54.81357002258301) ? " + 
"0.011913392823525687" + 
":  " + 
"0.06658094254963778" + 
":  " + 
"(b('lat') <= 56.023799896240234) ? " + 
"0.00302606452080816" + 
":  " + 
"-0.014825457343302362" + 
":  " + 
"(b('L8b3') <= 538.5) ? " + 
"(b('L8b3') <= 530.5) ? " + 
"-0.0061360712084642145" + 
":  " + 
"-0.04013354695440666" + 
":  " + 
"(b('L8b11') <= 651.5) ? " + 
"0.0515782827098834" + 
":  " + 
"-0.00010333292674967928" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 730.5) ? " + 
"(b('L8b4') <= 724.5) ? " + 
"(b('sand') <= 15.5) ? " + 
"-0.022675699471162512" + 
":  " + 
"0.0015087351730929829" + 
":  " + 
"(b('L8b5med') <= 3254.5) ? " + 
"0.032395930871360376" + 
":  " + 
"-0.0349285319708654" + 
":  " + 
"(b('L8b3') <= 801.5) ? " + 
"(b('ndvi_med') <= 4919.5) ? " + 
"-0.004651640570873904" + 
":  " + 
"0.043008993295535605" + 
":  " + 
"(b('L8b6') <= 1870.0) ? " + 
"0.02981519886416683" + 
":  " + 
"0.00027199929393852796" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2142.5) ? " + 
"(b('L8b5') <= 2140.5) ? " + 
"(b('lon') <= -120.88069915771484) ? " + 
"-0.012330242817640728" + 
":  " + 
"0.002308309158928315" + 
":  " + 
"(b('L8b3') <= 864.5) ? " + 
"0.1068674129844976" + 
":  " + 
"0.02687288502330981" + 
":  " + 
"(b('L8b6') <= 1366.0) ? " + 
"(b('L8dt') <= 854155.5) ? " + 
"0.1049911216039699" + 
":  " + 
"0.03309488266419744" + 
":  " + 
"(b('L8b5') <= 2149.5) ? " + 
"-0.022617972346877208" + 
":  " + 
"-0.0002598515833794337" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 665.5) ? " + 
"(b('L8b3') <= 656.5) ? " + 
"(b('lat') <= 43.76488494873047) ? " + 
"-0.008365685538060575" + 
":  " + 
"0.0013869057555540058" + 
":  " + 
"(b('L8b6') <= 2242.0) ? " + 
"-0.04421103358805583" + 
":  " + 
"0.0004005038407131093" + 
":  " + 
"(b('L8b4') <= 616.0) ? " + 
"(b('L8b11') <= 1310.0) ? " + 
"0.019695735537560436" + 
":  " + 
"-0.01525475548705917" + 
":  " + 
"(b('L8b2med') <= 392.5) ? " + 
"0.009316950988059028" + 
":  " + 
"-9.189305931907551e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 604.5) ? " + 
"(b('dsvv') <= -0.44843053817749023) ? " + 
"0.011514752912694354" + 
":  " + 
"0.12230662997038416" + 
":  " + 
"(b('L8b5') <= 1320.5) ? " + 
"(b('L8b3') <= 693.0) ? " + 
"-0.006789893810865496" + 
":  " + 
"-0.05372850705528315" + 
":  " + 
"(b('L8b5') <= 1681.0) ? " + 
"0.006165299795203553" + 
":  " + 
"-0.0001401540710520581" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3665.5) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4326.5) ? " + 
"-7.384340578111758e-06" + 
":  " + 
"0.0344170758603052" + 
":  " + 
"(b('ndvi_med') <= 2313.5) ? " + 
"-0.017007118905885153" + 
":  " + 
"0.022056813040147775" + 
":  " + 
"(b('L8dt') <= 1689918.5) ? " + 
"(b('L8dt') <= 1344315.0) ? " + 
"0.008978268254605981" + 
":  " + 
"0.10154441833721807" + 
":  " + 
"(b('dsvv') <= 1.7125725746154785) ? " + 
"-0.014089247686492692" + 
":  " + 
"-0.04725862269250566" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6286332.0) ? " + 
"(b('L8dt') <= 6095129.0) ? " + 
"(b('L8dt') <= 5819576.0) ? " + 
"-6.022277078881991e-05" + 
":  " + 
"0.024456058257144735" + 
":  " + 
"(b('ndvi') <= 3825.5) ? " + 
"-0.04575002600523787" + 
":  " + 
"0.02222662497573051" + 
":  " + 
"(b('ndvi') <= 1380.0) ? " + 
"(b('L8b4') <= 1119.0) ? " + 
"0.016858723678503378" + 
":  " + 
"0.052669716550953864" + 
":  " + 
"(b('sand') <= 22.0) ? " + 
"0.09229041502520142" + 
":  " + 
"0.004970715649073948" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -9.805422306060791) ? " + 
"(b('dgvv') <= -12.400606632232666) ? " + 
"0.05060436308002157" + 
":  " + 
"0.08264972941259718" + 
":  " + 
"(b('dsvv') <= -3.260768413543701) ? " + 
"(b('crops') <= 89.96376037597656) ? " + 
"-0.007798749799458963" + 
":  " + 
"0.02158162192744239" + 
":  " + 
"(b('L8b5med') <= 2002.0) ? " + 
"-0.004671816520203023" + 
":  " + 
"0.00027492136242279053" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 4758.5) ? " + 
"(b('ndvi') <= 4430.5) ? " + 
"(b('ndvi_med') <= 4818.25) ? " + 
"-0.00016793964039060717" + 
":  " + 
"0.024609151858562654" + 
":  " + 
"(b('crops') <= 7.257519245147705) ? " + 
"0.047409842786872325" + 
":  " + 
"0.005582424515866588" + 
":  " + 
"(b('sand') <= 79.5) ? " + 
"(b('L8b6') <= 2777.5) ? " + 
"0.001935144680027165" + 
":  " + 
"-0.009475276726665049" + 
":  " + 
"(b('dsvv') <= 0.16709518432617188) ? " + 
"-0.022330750076303096" + 
":  " + 
"-0.08779697627255274" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4653.0) ? " + 
"(b('L8b5') <= 4619.5) ? " + 
"(b('ndvi_med') <= 5073.5) ? " + 
"8.955802786319958e-05" + 
":  " + 
"-0.011287645296488073" + 
":  " + 
"(b('dsvv') <= 2.7193703651428223) ? " + 
"-0.03426345186797239" + 
":  " + 
"0.02280916918656678" + 
":  " + 
"(b('ndvi') <= 5908.5) ? " + 
"(b('L8b2med') <= 677.5) ? " + 
"0.0638528618582608" + 
":  " + 
"0.0011232197886839744" + 
":  " + 
"(b('L8dt') <= 471617.0) ? " + 
"0.023902146608783318" + 
":  " + 
"-0.02674798007283156" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2907.5) ? " + 
"(b('L8b11') <= 2889.5) ? " + 
"(b('lat') <= -28.00918483734131) ? " + 
"-0.015957582634279186" + 
":  " + 
"-9.561792790736146e-05" + 
":  " + 
"(b('lon') <= -5.406574964523315) ? " + 
"-0.0006072687048284257" + 
":  " + 
"-0.03277195852988253" + 
":  " + 
"(b('L8b11') <= 2911.5) ? " + 
"(b('L8b5') <= 2708.5) ? " + 
"0.05318519553903532" + 
":  " + 
"-0.015557358629582893" + 
":  " + 
"(b('L8b2') <= 935.5) ? " + 
"0.005233049492613029" + 
":  " + 
"-0.0011948018167384502" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1708.5) ? " + 
"(b('L8b3') <= 1678.0) ? " + 
"(b('L8b11') <= 3444.0) ? " + 
"-0.0002145351620304355" + 
":  " + 
"0.009954384590981897" + 
":  " + 
"(b('crops') <= 81.73051071166992) ? " + 
"-0.005765536641051315" + 
":  " + 
"-0.041322445566549036" + 
":  " + 
"(b('L8b7med') <= 2004.25) ? " + 
"(b('L8b2') <= 1160.0) ? " + 
"0.05654067624352304" + 
":  " + 
"-0.028324735685061945" + 
":  " + 
"(b('L8dt') <= 2526521.5) ? " + 
"0.0033107866749880824" + 
":  " + 
"-0.017168970824843473" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2436.5) ? " + 
"(b('L8b5') <= 2341.5) ? " + 
"(b('ndvi') <= 1620.5) ? " + 
"-0.004676416720887076" + 
":  " + 
"0.002372025419837093" + 
":  " + 
"(b('sand') <= 18.0) ? " + 
"0.1374325902278877" + 
":  " + 
"0.006709719063958886" + 
":  " + 
"(b('L8b5') <= 2470.5) ? " + 
"(b('sand') <= 20.5) ? " + 
"-0.07275740615420316" + 
":  " + 
"-0.008976092824393843" + 
":  " + 
"(b('L8b3') <= 518.5) ? " + 
"0.02773297359266092" + 
":  " + 
"-0.00019837388282091886" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 666.5) ? " + 
"(b('ndvi') <= 3131.5) ? " + 
"(b('ndvi') <= 3109.5) ? " + 
"0.0013228973269885022" + 
":  " + 
"0.06573830397892096" + 
":  " + 
"(b('lat') <= 43.76488494873047) ? " + 
"-0.01986236471977906" + 
":  " + 
"-0.003070794501343013" + 
":  " + 
"(b('L8b3') <= 689.5) ? " + 
"(b('L8b5med') <= 3256.5) ? " + 
"0.009565165793176325" + 
":  " + 
"-0.06754057523636088" + 
":  " + 
"(b('L8b3') <= 693.5) ? " + 
"-0.0246765096110066" + 
":  " + 
"9.09012201631793e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3425.75) ? " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b6') <= 2841.5) ? " + 
"0.00043951298790409217" + 
":  " + 
"0.0235584493684089" + 
":  " + 
"(b('L8b5') <= 3669.5) ? " + 
"-0.0013823263858946024" + 
":  " + 
"-0.01345732204489121" + 
":  " + 
"(b('L8b6') <= 3467.5) ? " + 
"(b('L8b11') <= 2003.0) ? " + 
"-0.002274911349840252" + 
":  " + 
"0.010514769850426476" + 
":  " + 
"(b('L8b5') <= 3431.0) ? " + 
"-0.002546473246965544" + 
":  " + 
"0.004670920905165548" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2669.75) ? " + 
"(b('ndvi') <= 2729.5) ? " + 
"(b('lat') <= 50.95975112915039) ? " + 
"-0.00021535359034472368" + 
":  " + 
"0.0430023230509001" + 
":  " + 
"(b('L8b5') <= 2959.0) ? " + 
"-0.0077596921238431305" + 
":  " + 
"0.0007576576985632346" + 
":  " + 
"(b('ndvi') <= 6890.0) ? " + 
"(b('ndvi') <= 6838.5) ? " + 
"0.0004253340996400217" + 
":  " + 
"-0.08098554871124267" + 
":  " + 
"(b('L8dt') <= 1573518.5) ? " + 
"0.014857985117897585" + 
":  " + 
"0.07268565713001063" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 653.5) ? " + 
"(b('dsvv') <= 0.7163405418395996) ? " + 
"(b('L8b6') <= 617.0) ? " + 
"0.004714940046503107" + 
":  " + 
"0.07747363478448299" + 
":  " + 
"0.10970218080404823" + 
":  " + 
"(b('L8b5') <= 1320.5) ? " + 
"(b('L8b4') <= 830.0) ? " + 
"-0.008452168301284623" + 
":  " + 
"-0.04773489288663043" + 
":  " + 
"(b('L8b5') <= 1681.0) ? " + 
"0.005710884004524708" + 
":  " + 
"-0.00012869164902324195" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 3.8659508228302) ? " + 
"(b('dgvv') <= 3.8649492263793945) ? " + 
"(b('L8b6') <= 1925.5) ? " + 
"0.003516423769942471" + 
":  " + 
"-0.000278647523594375" + 
":  " + 
"(b('ndvi_med') <= 2190.5) ? " + 
"-0.07385425625324314" + 
":  " + 
"0.011312506263233657" + 
":  " + 
"(b('L8b6') <= 1811.0) ? " + 
"(b('L8b3') <= 905.5) ? " + 
"-0.017351069958589396" + 
":  " + 
"-0.08208587376827378" + 
":  " + 
"(b('L8b5med') <= 3262.0) ? " + 
"0.012081283861808852" + 
":  " + 
"-0.014241901189286395" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2390.0) ? " + 
"(b('L8b3') <= 1440.5) ? " + 
"(b('L8b11') <= 2019.5) ? " + 
"-0.003952288358711631" + 
":  " + 
"0.009044621058587488" + 
":  " + 
"(b('dgvv') <= -2.422337532043457) ? " + 
"0.03340604822874315" + 
":  " + 
"0.0982763592258331" + 
":  " + 
"(b('ndvi') <= 3410.5) ? " + 
"(b('sand') <= 17.0) ? " + 
"0.03243523504340407" + 
":  " + 
"-0.000507285537646222" + 
":  " + 
"(b('lat') <= 56.023799896240234) ? " + 
"0.003117057658309581" + 
":  " + 
"-0.02456807167670226" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 5.5451555252075195) ? " + 
"(b('dsvv') <= 4.705793857574463) ? " + 
"(b('L8b3') <= 593.5) ? " + 
"-0.003826700933022684" + 
":  " + 
"0.00011498942981486975" + 
":  " + 
"(b('crops') <= 26.317363739013672) ? " + 
"0.041864392553573465" + 
":  " + 
"0.000247515334441152" + 
":  " + 
"(b('L8b2med') <= 486.5) ? " + 
"0.14402277072705105" + 
":  " + 
"(b('sand') <= 38.5) ? " + 
"-0.07409873439491943" + 
":  " + 
"-0.007906114967416774" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5med') <= 3046.5) ? " + 
"(b('L8b5') <= 3233.5) ? " + 
"-0.0009892040742964896" + 
":  " + 
"0.005826814146984582" + 
":  " + 
"(b('L8b5') <= 3190.5) ? " + 
"0.005619221792366752" + 
":  " + 
"-0.0029622500790673877" + 
":  " + 
"(b('L8b5') <= 3522.0) ? " + 
"(b('dgvv') <= -0.5868086814880371) ? " + 
"-0.02118060941719044" + 
":  " + 
"-0.06806463266773165" + 
":  " + 
"(b('L8b5med') <= 3138.5) ? " + 
"0.0033957084429966098" + 
":  " + 
"-0.00483246177958138" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 44.79741096496582) ? " + 
"(b('crops') <= 44.31945991516113) ? " + 
"(b('ndvi') <= 4390.5) ? " + 
"-8.914496424670437e-05" + 
":  " + 
"0.008039149446372277" + 
":  " + 
"(b('ndvi') <= 2432.5) ? " + 
"-0.07869170065757138" + 
":  " + 
"0.04237976585665574" + 
":  " + 
"(b('dsvv') <= 0.6497306823730469) ? " + 
"(b('lat') <= 39.95979881286621) ? " + 
"-0.007163629701403953" + 
":  " + 
"0.0013285668819713737" + 
":  " + 
"(b('L8dt') <= 411578.5) ? " + 
"-0.008925189128519112" + 
":  " + 
"-0.000719787645339066" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1355.0) ? " + 
"(b('L8dt') <= 711624.0) ? " + 
"(b('L8dt') <= 4102.5) ? " + 
"0.029947728924986664" + 
":  " + 
"-0.0004182911133940401" + 
":  " + 
"(b('L8b11') <= 1532.5) ? " + 
"-0.11532485712310908" + 
":  " + 
"0.011068247047293237" + 
":  " + 
"(b('ndvi') <= 1138.5) ? " + 
"(b('L8b2med') <= 424.5) ? " + 
"-0.04680451639635839" + 
":  " + 
"-0.004911692201577783" + 
":  " + 
"(b('ndvi') <= 1154.5) ? " + 
"0.01392712558664572" + 
":  " + 
"-7.874889020520735e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2104.5) ? " + 
"(b('L8b6med') <= 3837.0) ? " + 
"(b('L8b5med') <= 3004.25) ? " + 
"0.001226484696371485" + 
":  " + 
"0.015622144105516262" + 
":  " + 
"(b('L8b5med') <= 3125.0) ? " + 
"-0.04456617396662152" + 
":  " + 
"-0.012740089428777331" + 
":  " + 
"(b('L8b6') <= 1366.0) ? " + 
"(b('L8dt') <= 854155.5) ? " + 
"0.09459693676263346" + 
":  " + 
"0.033592342959531035" + 
":  " + 
"(b('L8b3') <= 728.5) ? " + 
"-0.0033320040867098823" + 
":  " + 
"0.0001735162334398411" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 730.5) ? " + 
"(b('L8b4') <= 724.5) ? " + 
"(b('lon') <= -115.11370468139648) ? " + 
"0.017656340666646828" + 
":  " + 
"2.0001280766379544e-05" + 
":  " + 
"(b('crops') <= 20.238818168640137) ? " + 
"0.05269578623278804" + 
":  " + 
"0.01226481157695011" + 
":  " + 
"(b('L8b3') <= 631.0) ? " + 
"(b('ndvi') <= 3523.5) ? " + 
"-0.010452941438001875" + 
":  " + 
"-0.0579727133136531" + 
":  " + 
"(b('L8b3') <= 702.5) ? " + 
"0.007379789004203423" + 
":  " + 
"-0.0004056161608044928" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 392.5) ? " + 
"(b('ndvi') <= 2750.5) ? " + 
"(b('sand') <= 67.5) ? " + 
"0.012509298285671539" + 
":  " + 
"0.05451461157755261" + 
":  " + 
"(b('lat') <= 56.023799896240234) ? " + 
"0.003169294102717321" + 
":  " + 
"-0.012560123499647658" + 
":  " + 
"(b('L8b3') <= 538.5) ? " + 
"(b('L8b3') <= 530.5) ? " + 
"-0.005607844652099668" + 
":  " + 
"-0.03579515832535678" + 
":  " + 
"(b('L8b3') <= 542.5) ? " + 
"0.06599358649749035" + 
":  " + 
"-8.706723622795508e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4653.0) ? " + 
"(b('L8b5') <= 4619.5) ? " + 
"(b('ndvi_med') <= 5073.5) ? " + 
"8.06122418755426e-05" + 
":  " + 
"-0.0103185860901154" + 
":  " + 
"(b('L8dt') <= 368110.5) ? " + 
"-0.008381768889749917" + 
":  " + 
"-0.03418682259289557" + 
":  " + 
"(b('ndvi') <= 5908.5) ? " + 
"(b('L8b2med') <= 677.5) ? " + 
"0.057552472964897" + 
":  " + 
"0.0022364536750312638" + 
":  " + 
"(b('L8dt') <= 471617.0) ? " + 
"0.021425143587089957" + 
":  " + 
"-0.024203689360920665" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 1987972.5) ? " + 
"(b('dsvv') <= 5.5451555252075195) ? " + 
"(b('L8dt') <= 1980781.5) ? " + 
"-0.00016101061870246554" + 
":  " + 
"-0.033297667863518315" + 
":  " + 
"(b('L8b2') <= 748.5) ? " + 
"-0.047050490121434765" + 
":  " + 
"0.013728587465916582" + 
":  " + 
"(b('sand') <= 26.0) ? " + 
"(b('ndvi') <= 1900.5) ? " + 
"0.03593113476969981" + 
":  " + 
"-0.015571135586820396" + 
":  " + 
"(b('L8b7med') <= 2802.5) ? " + 
"0.005642910111009958" + 
":  " + 
"-0.006467267978022115" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 44.514474868774414) ? " + 
"(b('ndvi') <= 6890.0) ? " + 
"(b('ndvi') <= 6596.5) ? " + 
"0.0004076125074688468" + 
":  " + 
"-0.03374087182741407" + 
":  " + 
"(b('lat') <= 39.95979881286621) ? " + 
"0.06948546528958646" + 
":  " + 
"0.01950147681646979" + 
":  " + 
"(b('L8b2med') <= 588.0) ? " + 
"(b('L8b11') <= 2028.0) ? " + 
"-0.0011939356849732323" + 
":  " + 
"0.011324339277032944" + 
":  " + 
"(b('L8b5') <= 3043.5) ? " + 
"-0.0077816117146131325" + 
":  " + 
"0.00575538569543602" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3660.0) ? " + 
"(b('L8b5') <= 3655.5) ? " + 
"(b('L8b5med') <= 3243.0) ? " + 
"-0.00025998257649220653" + 
":  " + 
"0.003919601467203155" + 
":  " + 
"(b('L8dt') <= 455478.5) ? " + 
"0.004763846557166721" + 
":  " + 
"0.039943223978790306" + 
":  " + 
"(b('crops') <= 99.63687133789062) ? " + 
"(b('L8b2med') <= 413.0) ? " + 
"-0.042823354953831216" + 
":  " + 
"-0.002214236252899489" + 
":  " + 
"(b('L8b7med') <= 1651.5) ? " + 
"0.04496502437015618" + 
":  " + 
"0.0074572160634010665" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1636.5) ? " + 
"(b('L8b2med') <= 682.0) ? " + 
"(b('L8b2med') <= 567.25) ? " + 
"0.006153127065132315" + 
":  " + 
"-0.010653076849841422" + 
":  " + 
"(b('dgvv') <= -1.1474838256835938) ? " + 
"0.0064206592451445" + 
":  " + 
"-0.0012623866276902504" + 
":  " + 
"(b('lon') <= -121.20288467407227) ? " + 
"(b('L8b6') <= 2573.5) ? " + 
"-0.0032091082732573096" + 
":  " + 
"0.04423047131045915" + 
":  " + 
"(b('ndvi') <= 1810.0) ? " + 
"0.005689783230569001" + 
":  " + 
"-0.00032168361728616285" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 730.5) ? " + 
"(b('L8b4') <= 724.5) ? " + 
"(b('sand') <= 15.5) ? " + 
"-0.019758616833011652" + 
":  " + 
"0.0014794483483820803" + 
":  " + 
"(b('L8b5med') <= 3254.5) ? " + 
"0.02624913544483861" + 
":  " + 
"-0.03301958545139751" + 
":  " + 
"(b('L8b3') <= 817.5) ? " + 
"(b('lon') <= -80.39629745483398) ? " + 
"-0.007541864361554688" + 
":  " + 
"0.0005587763452047082" + 
":  " + 
"(b('L8b6') <= 1866.5) ? " + 
"0.025704430673762917" + 
":  " + 
"0.0002982126258057049" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2436.5) ? " + 
"(b('L8b5') <= 2341.5) ? " + 
"(b('L8b4') <= 1154.5) ? " + 
"0.002082513325601107" + 
":  " + 
"-0.004454975942516479" + 
":  " + 
"(b('L8b2med') <= 355.5) ? " + 
"0.06740385051044884" + 
":  " + 
"0.005699902011726438" + 
":  " + 
"(b('L8b5') <= 2470.5) ? " + 
"(b('sand') <= 20.5) ? " + 
"-0.06423762366411827" + 
":  " + 
"-0.008037279184604652" + 
":  " + 
"(b('L8b3') <= 518.5) ? " + 
"0.024936236859463803" + 
":  " + 
"-0.00021752310987237992" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 44.79741096496582) ? " + 
"(b('crops') <= 44.31945991516113) ? " + 
"(b('ndvi') <= 4390.5) ? " + 
"-3.6669018574397646e-05" + 
":  " + 
"0.00730115786117233" + 
":  " + 
"(b('ndvi') <= 2432.5) ? " + 
"-0.07213559647043918" + 
":  " + 
"0.03779580284533887" + 
":  " + 
"(b('dsvv') <= 0.6497306823730469) ? " + 
"(b('L8b5med') <= 3254.5) ? " + 
"-0.0006554066382301667" + 
":  " + 
"0.00525939874667335" + 
":  " + 
"(b('dgvv') <= 0.6006307601928711) ? " + 
"-0.19995257684350445" + 
":  " + 
"-0.002627799285575325" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2741.5) ? " + 
"(b('sand') <= 38.5) ? " + 
"(b('lat') <= 34.3631649017334) ? " + 
"-0.03983056805706953" + 
":  " + 
"-0.0016039795103720896" + 
":  " + 
"(b('L8b5med') <= 2647.5) ? " + 
"0.0004816161386386171" + 
":  " + 
"0.00650195130841625" + 
":  " + 
"(b('L8b6med') <= 2051.75) ? " + 
"(b('ndvi') <= 3609.0) ? " + 
"-0.007953353658044003" + 
":  " + 
"-0.04998379201304773" + 
":  " + 
"(b('L8b2med') <= 327.5) ? " + 
"0.04570482314824402" + 
":  " + 
"-0.0006950658671368708" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.83941650390625) ? " + 
"(b('L8b4') <= 833.5) ? " + 
"(b('L8b5med') <= 2422.75) ? " + 
"0.025252406130223774" + 
":  " + 
"0.00017870338180779773" + 
":  " + 
"(b('L8b2') <= 508.5) ? " + 
"-0.021753859213729573" + 
":  " + 
"0.0011519474727709888" + 
":  " + 
"(b('ndvi') <= 1137.5) ? " + 
"(b('ndvi') <= 1104.5) ? " + 
"-0.001609425016417184" + 
":  " + 
"-0.018053619837258145" + 
":  " + 
"(b('L8b5') <= 2396.5) ? " + 
"0.001979450711581754" + 
":  " + 
"-0.00077125325030155" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 727.5) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"(b('L8b5med') <= 3285.0) ? " + 
"0.00014333280342400796" + 
":  " + 
"-0.027109190793346064" + 
":  " + 
"(b('L8b6') <= 2214.0) ? " + 
"-0.03818450721887607" + 
":  " + 
"-0.008522934901209445" + 
":  " + 
"(b('L8b4') <= 946.5) ? " + 
"(b('lon') <= 29.159395217895508) ? " + 
"0.002785472974011998" + 
":  " + 
"0.0819351460525884" + 
":  " + 
"(b('L8b4') <= 1020.5) ? " + 
"-0.008016129559858056" + 
":  " + 
"0.0003398320685747515" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 665.5) ? " + 
"(b('L8b3') <= 656.5) ? " + 
"(b('lat') <= 43.76488494873047) ? " + 
"-0.007786741226526066" + 
":  " + 
"0.0011881731155709454" + 
":  " + 
"(b('lon') <= -98.02571487426758) ? " + 
"0.012563452085984054" + 
":  " + 
"-0.03138369784159239" + 
":  " + 
"(b('L8b2') <= 464.5) ? " + 
"(b('lat') <= 41.29464912414551) ? " + 
"0.011343631624037925" + 
":  " + 
"-0.0009263512183151314" + 
":  " + 
"(b('L8b11') <= 1158.5) ? " + 
"0.05718140495741827" + 
":  " + 
"-0.0004377822064149602" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1443.5) ? " + 
"(b('L8b6') <= 2410.5) ? " + 
"(b('L8b6') <= 2407.0) ? " + 
"0.000405204181861694" + 
":  " + 
"0.04297322199906722" + 
":  " + 
"(b('L8b2med') <= 336.0) ? " + 
"-0.03589124466191341" + 
":  " + 
"-0.006174648439382471" + 
":  " + 
"(b('L8b4') <= 834.5) ? " + 
"(b('lon') <= -113.71215057373047) ? " + 
"0.030167184396491183" + 
":  " + 
"0.0038424341428179042" + 
":  " + 
"(b('L8b11') <= 1469.5) ? " + 
"0.029980809273792527" + 
":  " + 
"-0.0004560074597250416" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5229.5) ? " + 
"(b('ndvi') <= 5018.5) ? " + 
"(b('ndvi') <= 4758.5) ? " + 
"0.00018751286586796956" + 
":  " + 
"-0.006989478844769559" + 
":  " + 
"(b('L8b6') <= 2242.0) ? " + 
"-0.013244353923837725" + 
":  " + 
"0.022400695548455377" + 
":  " + 
"(b('dgvv') <= -1.479440689086914) ? " + 
"(b('dgvv') <= -1.5321149826049805) ? " + 
"0.007212027803951168" + 
":  " + 
"0.07469694769632233" + 
":  " + 
"(b('lon') <= -3.0728151202201843) ? " + 
"-0.013287640964410364" + 
":  " + 
"-0.0005498151533993392" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1651.5) ? " + 
"(b('L8b4') <= 944.5) ? " + 
"(b('L8b4') <= 903.5) ? " + 
"-0.0007725408676259108" + 
":  " + 
"0.014491580814562923" + 
":  " + 
"(b('L8b11') <= 1485.5) ? " + 
"0.007836807693996728" + 
":  " + 
"-0.016467677996353007" + 
":  " + 
"(b('L8b11') <= 1654.5) ? " + 
"(b('L8b6med') <= 2637.75) ? " + 
"0.009689917308351876" + 
":  " + 
"0.06749741464837022" + 
":  " + 
"(b('L8dt') <= 358.0) ? " + 
"-0.17480663974482824" + 
":  " + 
"0.0002946474654187908" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 826.5) ? " + 
"(b('lon') <= -69.40549850463867) ? " + 
"(b('L8b5med') <= 3215.0) ? " + 
"-0.0021943566094767566" + 
":  " + 
"-0.016598903777111006" + 
":  " + 
"(b('L8b6') <= 2989.5) ? " + 
"0.0007640788344406627" + 
":  " + 
"0.03835809076931847" + 
":  " + 
"(b('L8b3') <= 835.5) ? " + 
"(b('L8b5') <= 1782.0) ? " + 
"0.08928827979282894" + 
":  " + 
"0.008638887164899831" + 
":  " + 
"(b('L8b11') <= 954.0) ? " + 
"-0.05654828515302307" + 
":  " + 
"0.0002807774799529784" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1381.5) ? " + 
"(b('L8b3') <= 1062.5) ? " + 
"(b('L8b6') <= 3369.5) ? " + 
"0.00028695269078907285" + 
":  " + 
"-0.008950653359159308" + 
":  " + 
"(b('lon') <= -121.1158447265625) ? " + 
"0.12307809588071836" + 
":  " + 
"0.009461827639681765" + 
":  " + 
"(b('L8b11') <= 1739.0) ? " + 
"(b('L8b5med') <= 3176.5) ? " + 
"0.01167196920578184" + 
":  " + 
"0.13309282515937187" + 
":  " + 
"(b('L8b11') <= 2268.5) ? " + 
"-0.008264674174285757" + 
":  " + 
"-5.3003584780625705e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5229.5) ? " + 
"(b('ndvi') <= 5018.5) ? " + 
"(b('ndvi') <= 4765.5) ? " + 
"0.0001701016957547119" + 
":  " + 
"-0.0063402564471089174" + 
":  " + 
"(b('L8b3') <= 990.5) ? " + 
"0.005027848790667573" + 
":  " + 
"0.04432499723804939" + 
":  " + 
"(b('ndvi') <= 5724.0) ? " + 
"(b('L8b5') <= 4015.0) ? " + 
"-0.012501901640007002" + 
":  " + 
"0.04830917891189785" + 
":  " + 
"(b('L8b6') <= 1830.5) ? " + 
"-0.033941571303676345" + 
":  " + 
"0.0041837365660362105" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 26.74935531616211) ? " + 
"(b('L8dt') <= 366022.5) ? " + 
"(b('L8dt') <= 348342.0) ? " + 
"-0.0003669121058435228" + 
":  " + 
"-0.011144628279634876" + 
":  " + 
"(b('dsvv') <= -0.6760125160217285) ? " + 
"-0.0016529641040757285" + 
":  " + 
"0.001785631109351587" + 
":  " + 
"(b('L8b5') <= 2986.5) ? " + 
"(b('lon') <= 28.338205337524414) ? " + 
"-0.014615601405327985" + 
":  " + 
"0.0040444185483671374" + 
":  " + 
"(b('dsvv') <= 0.9334778785705566) ? " + 
"0.0121300871432983" + 
":  " + 
"-0.01053528965895231" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5med') <= 3046.5) ? " + 
"(b('L8b4') <= 1668.5) ? " + 
"0.0002864688819531792" + 
":  " + 
"-0.004622798180597274" + 
":  " + 
"(b('L8b5') <= 3190.5) ? " + 
"0.005131062178591799" + 
":  " + 
"-0.002539472253779754" + 
":  " + 
"(b('L8b3') <= 1358.5) ? " + 
"(b('L8b2') <= 465.0) ? " + 
"0.004652303952874804" + 
":  " + 
"-0.010172061796314818" + 
":  " + 
"(b('sand') <= 28.5) ? " + 
"0.0500634803040268" + 
":  " + 
"0.0016922549285835486" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 872.5) ? " + 
"(b('L8b5') <= 3915.5) ? " + 
"(b('L8b3') <= 860.5) ? " + 
"-0.0004575853669947913" + 
":  " + 
"-0.012743849905374754" + 
":  " + 
"(b('L8b3') <= 842.5) ? " + 
"-0.0259839409717664" + 
":  " + 
"0.06100288711929589" + 
":  " + 
"(b('L8b4') <= 1231.5) ? " + 
"(b('lon') <= -120.05884170532227) ? " + 
"0.02608275773260824" + 
":  " + 
"0.0029512655891833044" + 
":  " + 
"(b('L8b7med') <= 1878.5) ? " + 
"0.005895350637621541" + 
":  " + 
"-0.0012709402002004887" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1560.5) ? " + 
"(b('L8b4') <= 1154.5) ? " + 
"(b('L8b2') <= 558.5) ? " + 
"0.0020559366310420935" + 
":  " + 
"0.0335421532795279" + 
":  " + 
"(b('ndvi') <= 2819.5) ? " + 
"-0.0005790094834100667" + 
":  " + 
"0.0146801795785949" + 
":  " + 
"(b('L8b4') <= 2108.5) ? " + 
"(b('L8b2') <= 912.5) ? " + 
"-0.0004968410758040872" + 
":  " + 
"0.008056016783634233" + 
":  " + 
"(b('sand') <= 58.5) ? " + 
"-0.0021052024315332462" + 
":  " + 
"-0.028367977963690425" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2461.0) ? " + 
"(b('L8b4') <= 621.75) ? " + 
"(b('lon') <= -119.03326797485352) ? " + 
"0.06933325074041052" + 
":  " + 
"0.0014164454515644066" + 
":  " + 
"(b('L8b11') <= 1364.5) ? " + 
"-0.01602453124837165" + 
":  " + 
"-0.0012226173206800718" + 
":  " + 
"(b('L8b5med') <= 2478.5) ? " + 
"(b('L8b5') <= 1868.5) ? " + 
"-0.10139687317805676" + 
":  " + 
"0.014330837470916015" + 
":  " + 
"(b('dgvv') <= 4.0491416454315186) ? " + 
"6.0754380573757636e-05" + 
":  " + 
"0.009087960075500738" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1339.0) ? " + 
"(b('ndvi') <= 1530.5) ? " + 
"(b('dgvv') <= 1.6982908248901367) ? " + 
"3.59980006786519e-05" + 
":  " + 
"0.017257321833393572" + 
":  " + 
"(b('dsvv') <= -1.0710268020629883) ? " + 
"0.06706559933774621" + 
":  " + 
"0.008897373203527912" + 
":  " + 
"(b('ndvi') <= 1171.5) ? " + 
"(b('L8b5') <= 3293.5) ? " + 
"-0.005385590638553248" + 
":  " + 
"0.01678907649519986" + 
":  " + 
"(b('ndvi') <= 1179.5) ? " + 
"0.05750933151345041" + 
":  " + 
"-4.848816699205155e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 6286332.0) ? " + 
"(b('L8dt') <= 6167534.5) ? " + 
"(b('L8b3') <= 564.5) ? " + 
"-0.004276041494265425" + 
":  " + 
"8.487775254930647e-05" + 
":  " + 
"(b('L8b7med') <= 2885.5) ? " + 
"-0.05376121951587579" + 
":  " + 
"-0.029541398931841593" + 
":  " + 
"(b('ndvi') <= 1568.5) ? " + 
"(b('ndvi_med') <= 1646.5) ? " + 
"0.04137023239864274" + 
":  " + 
"2.6262614424024666e-05" + 
":  " + 
"(b('L8b11') <= 1325.0) ? " + 
"0.04214136211181275" + 
":  " + 
"0.0011001327854689895" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 730.5) ? " + 
"(b('ndvi') <= 2194.5) ? " + 
"(b('L8b4') <= 694.5) ? " + 
"0.005508549987619077" + 
":  " + 
"0.028333915329287137" + 
":  " + 
"(b('L8b3') <= 764.5) ? " + 
"-0.0011473531616069867" + 
":  " + 
"0.009098000418683597" + 
":  " + 
"(b('L8b3') <= 801.5) ? " + 
"(b('L8b11') <= 1348.5) ? " + 
"-0.013163713094264076" + 
":  " + 
"-0.001642424628781011" + 
":  " + 
"(b('L8b6') <= 1870.0) ? " + 
"0.02294444933476889" + 
":  " + 
"0.00025104451548442025" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5') <= 3448.5) ? " + 
"(b('L8b5') <= 3447.5) ? " + 
"0.00010118289178051579" + 
":  " + 
"-0.055427051678079244" + 
":  " + 
"(b('lat') <= 50.490203857421875) ? " + 
"0.010616046352730894" + 
":  " + 
"-0.045980189348208696" + 
":  " + 
"(b('L8b11') <= 2622.0) ? " + 
"(b('L8b6') <= 2410.5) ? " + 
"0.00447184216628998" + 
":  " + 
"-0.008594827566472707" + 
":  " + 
"(b('L8b11') <= 2629.0) ? " + 
"0.07506170243431369" + 
":  " + 
"0.001746089490722003" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 3410.5) ? " + 
"(b('sand') <= 17.0) ? " + 
"(b('ndvi') <= 3102.5) ? " + 
"0.038956073087615756" + 
":  " + 
"-0.10419599083417833" + 
":  " + 
"(b('ndvi') <= 3396.0) ? " + 
"-0.0004558456281481672" + 
":  " + 
"-0.038171215255813275" + 
":  " + 
"(b('lat') <= 56.023799896240234) ? " + 
"(b('sand') <= 24.5) ? " + 
"-0.006447517297305563" + 
":  " + 
"0.003727554319230974" + 
":  " + 
"(b('L8b6') <= 2329.5) ? " + 
"0.0021818671467761412" + 
":  " + 
"-0.021672412321426332" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2669.75) ? " + 
"(b('ndvi') <= 1827.0) ? " + 
"(b('ndvi') <= 1623.0) ? " + 
"-0.0023642804456412893" + 
":  " + 
"0.02056636300363632" + 
":  " + 
"(b('ndvi_med') <= 1649.25) ? " + 
"-0.026115073701348253" + 
":  " + 
"-0.001601816202145967" + 
":  " + 
"(b('L8b11') <= 1124.5) ? " + 
"(b('L8b5med') <= 2422.5) ? " + 
"0.032762185981787116" + 
":  " + 
"-0.013236212036593135" + 
":  " + 
"(b('L8b11') <= 1134.5) ? " + 
"0.06755944882935282" + 
":  " + 
"0.0005716289487292557" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2336.5) ? " + 
"(b('ndvi_med') <= 3422.5) ? " + 
"(b('ndvi') <= 2270.5) ? " + 
"-0.0006574468073324216" + 
":  " + 
"-0.011555661318774368" + 
":  " + 
"(b('L8b5') <= 2707.0) ? " + 
"0.008216273862396204" + 
":  " + 
"0.04110491001974378" + 
":  " + 
"(b('lat') <= -5.20074987411499) ? " + 
"(b('L8b3') <= 735.0) ? " + 
"0.08695621891022226" + 
":  " + 
"0.027544304729194884" + 
":  " + 
"(b('ndvi') <= 2447.5) ? " + 
"0.0096219998672936" + 
":  " + 
"-8.923996780837e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 395.5) ? " + 
"(b('ndvi') <= 3141.0) ? " + 
"(b('crops') <= 11.51313591003418) ? " + 
"0.05576473931655751" + 
":  " + 
"0.006866491734988353" + 
":  " + 
"(b('L8b7med') <= 1395.75) ? " + 
"-0.008758567286955963" + 
":  " + 
"0.008659097989737425" + 
":  " + 
"(b('lat') <= 44.514474868774414) ? " + 
"(b('ndvi') <= 6890.0) ? " + 
"0.00027102942805383055" + 
":  " + 
"0.03257010497542285" + 
":  " + 
"(b('L8b2') <= 426.5) ? " + 
"-0.006240065029229968" + 
":  " + 
"-0.0004868884833514084" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 3466.5) ? " + 
"(b('sand') <= 17.0) ? " + 
"(b('ndvi') <= 3102.5) ? " + 
"0.0342811200798921" + 
":  " + 
"-0.09363438907657046" + 
":  " + 
"(b('ndvi_med') <= 4848.5) ? " + 
"-0.0005931719912411072" + 
":  " + 
"0.04724612682788084" + 
":  " + 
"(b('ndvi') <= 3537.5) ? " + 
"(b('crops') <= 99.63687133789062) ? " + 
"0.012429549943430518" + 
":  " + 
"0.07295512440832505" + 
":  " + 
"(b('L8b2') <= 979.0) ? " + 
"7.45176354006417e-05" + 
":  " + 
"0.027391459300699264" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3660.0) ? " + 
"(b('L8b5') <= 3655.5) ? " + 
"(b('L8b5med') <= 3385.5) ? " + 
"-6.772717655782505e-05" + 
":  " + 
"0.005112091260825418" + 
":  " + 
"(b('L8dt') <= 455478.5) ? " + 
"0.0038931374074760447" + 
":  " + 
"0.03470843888658847" + 
":  " + 
"(b('crops') <= 99.63687133789062) ? " + 
"(b('L8b7med') <= 1980.5) ? " + 
"-0.009148505303558175" + 
":  " + 
"-4.659304694751217e-05" + 
":  " + 
"(b('dsvv') <= 0.8059730529785156) ? " + 
"0.0353826495719869" + 
":  " + 
"-0.004906534556467575" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 730.5) ? " + 
"(b('L8b4') <= 725.5) ? " + 
"(b('L8dt') <= 802.5) ? " + 
"0.0532996461539824" + 
":  " + 
"0.000815868385950725" + 
":  " + 
"(b('crops') <= 20.238818168640137) ? " + 
"0.0651338326100052" + 
":  " + 
"0.004055876926662378" + 
":  " + 
"(b('L8b11') <= 1651.5) ? " + 
"(b('lon') <= 29.159395217895508) ? " + 
"-0.0031668212832025324" + 
":  " + 
"0.04954417521745751" + 
":  " + 
"(b('L8b11') <= 1654.5) ? " + 
"0.04416646315933924" + 
":  " + 
"0.00018899556020731" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1381.5) ? " + 
"(b('L8b3') <= 1062.5) ? " + 
"(b('L8b6') <= 3369.5) ? " + 
"0.0002842704225782273" + 
":  " + 
"-0.008242477280531426" + 
":  " + 
"(b('lon') <= -121.1158447265625) ? " + 
"0.10988027039162462" + 
":  " + 
"0.008868931901347906" + 
":  " + 
"(b('L8b11') <= 1739.0) ? " + 
"(b('L8b5med') <= 3176.5) ? " + 
"0.010137541184315067" + 
":  " + 
"0.11770470158894755" + 
":  " + 
"(b('L8b2') <= 694.5) ? " + 
"-0.008552747546925034" + 
":  " + 
"-0.00016915598209502172" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3369.5) ? " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b6') <= 2841.5) ? " + 
"0.00046483910621922573" + 
":  " + 
"0.01871902884547388" + 
":  " + 
"(b('L8b5') <= 2868.5) ? " + 
"0.00010587023667286264" + 
":  " + 
"-0.005931185932200479" + 
":  " + 
"(b('dgvv') <= 0.37430286407470703) ? " + 
"(b('ndvi_med') <= 4376.0) ? " + 
"0.0025013531370922113" + 
":  " + 
"0.03376040550709287" + 
":  " + 
"(b('L8b4') <= 833.5) ? " + 
"0.014277008864502248" + 
":  " + 
"-0.0027882134470237478" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3218711.5) ? " + 
"(b('lat') <= 44.514474868774414) ? " + 
"(b('ndvi') <= 7131.5) ? " + 
"0.00030538942231833583" + 
":  " + 
"0.04984845181661246" + 
":  " + 
"(b('L8b4') <= 1289.0) ? " + 
"-0.0006948333957831547" + 
":  " + 
"-0.007861941543846755" + 
":  " + 
"(b('L8b2med') <= 327.5) ? " + 
"(b('L8b2med') <= 318.5) ? " + 
"-0.013005686842578414" + 
":  " + 
"0.03512309515387364" + 
":  " + 
"(b('L8b7med') <= 1396.5) ? " + 
"-0.01970432334698779" + 
":  " + 
"0.0035925560210128826" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 5073.5) ? " + 
"(b('ndvi') <= 3464.5) ? " + 
"(b('sand') <= 17.0) ? " + 
"0.021042086859048643" + 
":  " + 
"-0.00048591801267269217" + 
":  " + 
"(b('lat') <= 56.023799896240234) ? " + 
"0.0024205645659568157" + 
":  " + 
"-0.010006909332233605" + 
":  " + 
"(b('dsvv') <= -1.9604120254516602) ? " + 
"(b('L8b3') <= 1133.0) ? " + 
"0.04496830554515526" + 
":  " + 
"-0.06581572271868336" + 
":  " + 
"(b('L8b5') <= 3153.0) ? " + 
"0.016820433900806536" + 
":  " + 
"-0.01622664814632538" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 14.5) ? " + 
"(b('L8b5') <= 3182.0) ? " + 
"(b('L8dt') <= 5788343.5) ? " + 
"0.009461669995783777" + 
":  " + 
"-0.12143174391928806" + 
":  " + 
"(b('L8dt') <= 690415.5) ? " + 
"-0.0868494595205351" + 
":  " + 
"0.0014924957334007621" + 
":  " + 
"(b('ndvi') <= 3410.5) ? " + 
"(b('ndvi') <= 3396.0) ? " + 
"-0.00024525491157933023" + 
":  " + 
"-0.03383770863577425" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"0.004849759559783709" + 
":  " + 
"-0.0016433384087490503" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 933.5) ? " + 
"(b('L8b3') <= 930.5) ? " + 
"(b('lon') <= 26.056610107421875) ? " + 
"-1.269304369269556e-05" + 
":  " + 
"-0.00692255375664713" + 
":  " + 
"(b('L8b2med') <= 467.5) ? " + 
"-0.13156272021426912" + 
":  " + 
"-0.021625560170861133" + 
":  " + 
"(b('L8b3') <= 945.5) ? " + 
"(b('L8b2med') <= 445.25) ? " + 
"-0.0866779674628071" + 
":  " + 
"0.017125010623175143" + 
":  " + 
"(b('L8b7med') <= 1895.5) ? " + 
"0.005037804415330882" + 
":  " + 
"-0.000649844974050593" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2268.5) ? " + 
"(b('L8b6') <= 3723.5) ? " + 
"(b('L8b11') <= 2224.5) ? " + 
"-8.707227170236998e-05" + 
":  " + 
"-0.012466359507817089" + 
":  " + 
"(b('ndvi') <= 3743.5) ? " + 
"-0.05722555894431047" + 
":  " + 
"-0.13056094354784972" + 
":  " + 
"(b('L8b7med') <= 1864.0) ? " + 
"(b('L8b6med') <= 2854.5) ? " + 
"0.007198539571890195" + 
":  " + 
"0.047055826178581006" + 
":  " + 
"(b('L8b7med') <= 2390.25) ? " + 
"-0.004013692193828546" + 
":  " + 
"0.0013210575560391306" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -9.805422306060791) ? " + 
"(b('lon') <= -5.2735350131988525) ? " + 
"0.04243882217276802" + 
":  " + 
"0.0728657281971208" + 
":  " + 
"(b('dsvv') <= -3.261660575866699) ? " + 
"(b('crops') <= 92.66439819335938) ? " + 
"-0.006827669856657394" + 
":  " + 
"0.020814008696921595" + 
":  " + 
"(b('L8b5') <= 3518.0) ? " + 
"0.00039270697162955025" + 
":  " + 
"-0.0018601271376200035" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2669.75) ? " + 
"(b('L8b4') <= 796.5) ? " + 
"(b('ndvi') <= 2729.5) ? " + 
"0.008513779799849032" + 
":  " + 
"-0.0007420455955007847" + 
":  " + 
"(b('L8b6') <= 1845.0) ? " + 
"0.021742422496524465" + 
":  " + 
"-0.0034910509360828127" + 
":  " + 
"(b('L8b5') <= 2867.5) ? " + 
"(b('L8b5med') <= 2991.25) ? " + 
"0.0003714557055506915" + 
":  " + 
"0.007901003835523163" + 
":  " + 
"(b('lon') <= 0.5547499880194664) ? " + 
"-0.0020735115343328307" + 
":  " + 
"0.006657302984266832" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 727.5) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"(b('L8b5med') <= 3285.0) ? " + 
"7.584163250748765e-05" + 
":  " + 
"-0.02347986329038896" + 
":  " + 
"(b('L8b6') <= 2214.0) ? " + 
"-0.03333856447969922" + 
":  " + 
"-0.007838993014910381" + 
":  " + 
"(b('L8b4') <= 701.0) ? " + 
"(b('ndvi') <= 6821.5) ? " + 
"0.010449354055923881" + 
":  " + 
"-0.07399371892021346" + 
":  " + 
"(b('L8b3') <= 735.5) ? " + 
"0.012334020405661434" + 
":  " + 
"-2.076887084217582e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1320.5) ? " + 
"(b('L8b6med') <= 2141.75) ? " + 
"(b('L8b3') <= 407.5) ? " + 
"-0.024215961256128255" + 
":  " + 
"0.02935924577428273" + 
":  " + 
"(b('L8b2') <= 578.0) ? " + 
"-0.014626106261325239" + 
":  " + 
"-0.09127493535666809" + 
":  " + 
"(b('L8b5') <= 1356.0) ? " + 
"(b('L8b11') <= 1419.0) ? " + 
"0.021622881621062098" + 
":  " + 
"0.08681345979452869" + 
":  " + 
"(b('L8b5') <= 1392.0) ? " + 
"-0.025253431018628866" + 
":  " + 
"3.3746531686897714e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2268.5) ? " + 
"(b('L8b6') <= 3723.5) ? " + 
"(b('L8b11') <= 2224.5) ? " + 
"-0.00010983752923426802" + 
":  " + 
"-0.011156840712562576" + 
":  " + 
"(b('ndvi') <= 3743.5) ? " + 
"-0.0510474052865621" + 
":  " + 
"-0.11733806650287892" + 
":  " + 
"(b('L8b7med') <= 1864.0) ? " + 
"(b('L8b11') <= 2820.5) ? " + 
"0.019300853619527058" + 
":  " + 
"-0.017127943659251035" + 
":  " + 
"(b('L8b7med') <= 2390.25) ? " + 
"-0.0036186990749910415" + 
":  " + 
"0.001242920633393476" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 770.5) ? " + 
"(b('L8b2med') <= 502.5) ? " + 
"(b('L8b4') <= 879.5) ? " + 
"0.0004001625158071716" + 
":  " + 
"0.022788006729139734" + 
":  " + 
"(b('L8b7med') <= 1889.0) ? " + 
"-0.011256563287273957" + 
":  " + 
"0.00029618998257627184" + 
":  " + 
"(b('L8b4') <= 702.0) ? " + 
"(b('L8b3') <= 800.5) ? " + 
"0.03812213643708494" + 
":  " + 
"-0.012920039357069089" + 
":  " + 
"(b('lon') <= 6.412564992904663) ? " + 
"0.000696275986426789" + 
":  " + 
"-0.0025918329417560565" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 316.5) ? " + 
"(b('L8b3') <= 620.0) ? " + 
"(b('L8b5') <= 2882.5) ? " + 
"0.0015936030531314717" + 
":  " + 
"-0.049087998778941266" + 
":  " + 
"(b('crops') <= 65.01828002929688) ? " + 
"0.02933624932138229" + 
":  " + 
"-0.014446697344046234" + 
":  " + 
"(b('L8b3') <= 564.0) ? " + 
"(b('L8b7med') <= 1324.0) ? " + 
"-0.037522036106535706" + 
":  " + 
"-0.003855685902829731" + 
":  " + 
"(b('L8b2') <= 320.5) ? " + 
"-0.016967018850762662" + 
":  " + 
"8.704747827299094e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 392.5) ? " + 
"(b('L8b6') <= 2954.0) ? " + 
"(b('L8b11') <= 1733.0) ? " + 
"0.0017290591924676501" + 
":  " + 
"-0.03371524893146713" + 
":  " + 
"(b('L8b5med') <= 2777.5) ? " + 
"0.014406299189455928" + 
":  " + 
"0.06836482405194169" + 
":  " + 
"(b('L8b3') <= 538.5) ? " + 
"(b('L8b6med') <= 3025.5) ? " + 
"-0.003363076753371264" + 
":  " + 
"-0.027087628280485814" + 
":  " + 
"(b('L8b3') <= 542.5) ? " + 
"0.056455950778257255" + 
":  " + 
"-7.871374663581387e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.83941650390625) ? " + 
"(b('L8b4') <= 1208.0) ? " + 
"(b('L8b3') <= 933.5) ? " + 
"0.0028163009043865026" + 
":  " + 
"0.02358380209628928" + 
":  " + 
"(b('ndvi_med') <= 1920.5) ? " + 
"0.00027558340673323925" + 
":  " + 
"-0.01920826710748226" + 
":  " + 
"(b('ndvi') <= 1184.5) ? " + 
"(b('L8b5') <= 3293.5) ? " + 
"-0.006054693783192799" + 
":  " + 
"0.016997408211795247" + 
":  " + 
"(b('ndvi') <= 1189.0) ? " + 
"0.03376862196642653" + 
":  " + 
"-0.00013958506994949356" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2397054.0) ? " + 
"(b('dsvv') <= 5.5451555252075195) ? " + 
"(b('dsvv') <= 5.409830808639526) ? " + 
"-0.00017663624725626403" + 
":  " + 
"0.03839935492316646" + 
":  " + 
"(b('sand') <= 38.5) ? " + 
"-0.08401675366262892" + 
":  " + 
"-0.009645380286783292" + 
":  " + 
"(b('L8b6') <= 4860.5) ? " + 
"(b('L8b5med') <= 3499.75) ? " + 
"0.001209162029366305" + 
":  " + 
"0.022934022379034222" + 
":  " + 
"(b('L8dt') <= 6459549.5) ? " + 
"-0.03444486763448432" + 
":  " + 
"0.03130747558099692" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1925.5) ? " + 
"(b('L8b6') <= 1891.0) ? " + 
"(b('L8b3') <= 891.0) ? " + 
"-0.0014553681118352724" + 
":  " + 
"0.030728384143719763" + 
":  " + 
"(b('L8b5med') <= 2158.5) ? " + 
"-0.018918357476496065" + 
":  " + 
"0.03219709383590434" + 
":  " + 
"(b('L8b2') <= 247.5) ? " + 
"-0.13558115000787632" + 
":  " + 
"(b('L8b3') <= 461.5) ? " + 
"-0.05205759585849578" + 
":  " + 
"-0.00011011421060157292" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2907.5) ? " + 
"(b('L8b11') <= 2839.5) ? " + 
"(b('lat') <= -28.00918483734131) ? " + 
"-0.01383228677908556" + 
":  " + 
"2.3604484537000657e-05" + 
":  " + 
"(b('L8b5') <= 2784.0) ? " + 
"3.915254887665256e-05" + 
":  " + 
"-0.017959359108590617" + 
":  " + 
"(b('L8b11') <= 2911.5) ? " + 
"(b('ndvi') <= 1258.5) ? " + 
"0.054972589163639105" + 
":  " + 
"0.008151340017249388" + 
":  " + 
"(b('L8b2') <= 935.5) ? " + 
"0.004690385703645756" + 
":  " + 
"-0.0012929862355642553" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 653.5) ? " + 
"(b('dgvv') <= 0.7235689163208008) ? " + 
"(b('L8b6') <= 617.0) ? " + 
"0.0020984475863671894" + 
":  " + 
"0.06717303975254336" + 
":  " + 
"0.09640610629270163" + 
":  " + 
"(b('L8b5') <= 1320.5) ? " + 
"(b('dgvv') <= 0.8152203559875488) ? " + 
"-0.002505583114323662" + 
":  " + 
"-0.023290225160864424" + 
":  " + 
"(b('L8b5') <= 1356.0) ? " + 
"0.023053763543434188" + 
":  " + 
"3.474262239193797e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1708.5) ? " + 
"(b('L8b4') <= 2018.5) ? " + 
"(b('L8b3') <= 1493.5) ? " + 
"-0.0001183819338603215" + 
":  " + 
"0.010985557717233758" + 
":  " + 
"(b('L8b5') <= 3785.0) ? " + 
"-0.005846548427703026" + 
":  " + 
"0.01659970712018557" + 
":  " + 
"(b('L8b7med') <= 2004.25) ? " + 
"(b('dgvv') <= 0.5362911224365234) ? " + 
"0.01805511214004639" + 
":  " + 
"0.07422183662027587" + 
":  " + 
"(b('L8dt') <= 3996909.0) ? " + 
"0.002411554627857874" + 
":  " + 
"-0.027299738872885563" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 5819576.0) ? " + 
"(b('L8dt') <= 5788343.5) ? " + 
"(b('L8b2') <= 316.5) ? " + 
"0.003499036581282843" + 
":  " + 
"-0.00015190201482904195" + 
":  " + 
"-0.10923815318396296" + 
":  " + 
"(b('lon') <= -5.3525800704956055) ? " + 
"(b('L8b6') <= 2494.5) ? " + 
"0.031002863593287935" + 
":  " + 
"-0.018051151749952293" + 
":  " + 
"(b('L8dt') <= 6072627.0) ? " + 
"0.034226245925401376" + 
":  " + 
"0.009489628359142155" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 822.5) ? " + 
"(b('lon') <= -69.40549850463867) ? " + 
"(b('L8b5med') <= 3215.0) ? " + 
"-0.002294935325082718" + 
":  " + 
"-0.01504099750476481" + 
":  " + 
"(b('L8b2') <= 581.5) ? " + 
"0.0017136164651581805" + 
":  " + 
"-0.017980686937837675" + 
":  " + 
"(b('L8b11') <= 954.0) ? " + 
"(b('L8dt') <= 1036801.0) ? " + 
"-0.09894798389055438" + 
":  " + 
"0.0017775938242996121" + 
":  " + 
"(b('L8b4') <= 944.5) ? " + 
"0.00511632235113085" + 
":  " + 
"6.316729976111272e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2036.5) ? " + 
"(b('L8b2med') <= 841.25) ? " + 
"(b('ndvi') <= 670.5) ? " + 
"0.19334955236566126" + 
":  " + 
"0.002596918322704937" + 
":  " + 
"(b('L8b5') <= 2024.5) ? " + 
"-0.016344380814359703" + 
":  " + 
"0.032148174137274596" + 
":  " + 
"(b('L8b5') <= 2037.5) ? " + 
"(b('dgvv') <= 0.34427499771118164) ? " + 
"-0.05411994704116303" + 
":  " + 
"-0.08101211935262251" + 
":  " + 
"(b('L8b11') <= 675.5) ? " + 
"0.054377327524638946" + 
":  " + 
"-0.00020519612951405358" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 4.130900621414185) ? " + 
"(b('dgvv') <= 4.121259689331055) ? " + 
"(b('L8b3') <= 759.5) ? " + 
"-0.0012550829072008262" + 
":  " + 
"0.0002646310115570599" + 
":  " + 
"(b('L8b5med') <= 2785.5) ? " + 
"-0.1348785942033483" + 
":  " + 
"-0.06404189076854057" + 
":  " + 
"(b('dgvv') <= 4.152717113494873) ? " + 
"(b('L8b11') <= 2407.5) ? " + 
"0.15287416861884265" + 
":  " + 
"0.1777073481399306" + 
":  " + 
"(b('L8b7med') <= 1539.5) ? " + 
"-0.022694600800261075" + 
":  " + 
"0.005948531496309407" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5') <= 3435.5) ? " + 
"(b('L8b5') <= 3379.5) ? " + 
"0.00024287018919102812" + 
":  " + 
"-0.007978896442894588" + 
":  " + 
"(b('lon') <= -82.97315216064453) ? " + 
"0.024606131777583005" + 
":  " + 
"0.002025643055863995" + 
":  " + 
"(b('dsvv') <= 2.0960893630981445) ? " + 
"(b('L8b5') <= 3562.0) ? " + 
"-0.011395046245200324" + 
":  " + 
"0.0008506832398972354" + 
":  " + 
"(b('L8b6med') <= 2311.5) ? " + 
"0.05979341538755777" + 
":  " + 
"-0.01579704908617645" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2342.5) ? " + 
"(b('ndvi_med') <= 3919.5) ? " + 
"(b('ndvi') <= 2270.5) ? " + 
"-0.00040703895327656535" + 
":  " + 
"-0.010210941220909386" + 
":  " + 
"(b('L8b3') <= 846.0) ? " + 
"0.012349743272723302" + 
":  " + 
"0.04550579423408536" + 
":  " + 
"(b('lat') <= -5.20074987411499) ? " + 
"(b('L8b2med') <= 618.0) ? " + 
"0.06393778966211264" + 
":  " + 
"0.021466650744743097" + 
":  " + 
"(b('ndvi') <= 2447.5) ? " + 
"0.008507531002340493" + 
":  " + 
"-7.907561302694203e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2669.75) ? " + 
"(b('L8b4') <= 1131.5) ? " + 
"(b('L8b4') <= 1092.0) ? " + 
"-0.0005358687804835882" + 
":  " + 
"0.02027789827322086" + 
":  " + 
"(b('L8b3') <= 1061.5) ? " + 
"-0.017501823675302817" + 
":  " + 
"0.0009384019320818831" + 
":  " + 
"(b('ndvi') <= 2654.5) ? " + 
"(b('ndvi') <= 2555.5) ? " + 
"-1.8918990741465712e-05" + 
":  " + 
"-0.013452226405516883" + 
":  " + 
"(b('L8b5') <= 3632.0) ? " + 
"0.003750870584717765" + 
":  " + 
"-0.004777973110339932" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 933.5) ? " + 
"(b('L8b6') <= 3209.0) ? " + 
"(b('L8b4') <= 1206.5) ? " + 
"-3.5835210918114854e-05" + 
":  " + 
"-0.018738500974511914" + 
":  " + 
"(b('L8b6med') <= 2683.25) ? " + 
"-0.08214851041049606" + 
":  " + 
"-0.006176178407016333" + 
":  " + 
"(b('L8b3') <= 945.5) ? " + 
"(b('ndvi_med') <= 1398.25) ? " + 
"0.08251174124616799" + 
":  " + 
"0.009050609707968265" + 
":  " + 
"(b('ndvi') <= 2060.0) ? " + 
"-0.001139837526647783" + 
":  " + 
"0.0028941716308688655" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3425.75) ? " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b5med') <= 3228.0) ? " + 
"-5.8733813893253684e-05" + 
":  " + 
"0.0066524145768137215" + 
":  " + 
"(b('L8b11') <= 1678.5) ? " + 
"-0.01363063529474297" + 
":  " + 
"-0.001281106359418554" + 
":  " + 
"(b('dgvv') <= 0.37430286407470703) ? " + 
"(b('ndvi_med') <= 4376.0) ? " + 
"0.0023004957568784263" + 
":  " + 
"0.030130881748634743" + 
":  " + 
"(b('L8b6med') <= 3501.25) ? " + 
"0.013149215226511933" + 
":  " + 
"-0.0028728313403271638" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2268.5) ? " + 
"(b('L8b6') <= 3723.5) ? " + 
"(b('L8b11') <= 2224.5) ? " + 
"-0.00011017219891084914" + 
":  " + 
"-0.010066274670111893" + 
":  " + 
"(b('ndvi') <= 3743.5) ? " + 
"-0.047307889358337366" + 
":  " + 
"-0.10526007995207197" + 
":  " + 
"(b('L8b7med') <= 1864.0) ? " + 
"(b('L8b6med') <= 2896.0) ? " + 
"0.006778790587195033" + 
":  " + 
"0.04709529986349891" + 
":  " + 
"(b('L8b11') <= 2290.5) ? " + 
"0.01256535968640843" + 
":  " + 
"-0.0002923885304162305" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.83941650390625) ? " + 
"(b('L8b4') <= 877.5) ? " + 
"(b('L8b5med') <= 2422.75) ? " + 
"0.019783219129983334" + 
":  " + 
"-0.0024393121688322966" + 
":  " + 
"(b('L8b2') <= 508.5) ? " + 
"-0.02248638459933837" + 
":  " + 
"0.0007828768175690807" + 
":  " + 
"(b('lon') <= -103.57181930541992) ? " + 
"(b('dsvv') <= 1.1690940856933594) ? " + 
"-0.011960011934938973" + 
":  " + 
"0.014905044738913178" + 
":  " + 
"(b('L8b11') <= 2747.5) ? " + 
"-0.0005926217290408057" + 
":  " + 
"0.0018374378902033966" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 395.5) ? " + 
"(b('ndvi') <= 3141.0) ? " + 
"(b('crops') <= 11.51313591003418) ? " + 
"0.047910056879751056" + 
":  " + 
"0.006087283966157449" + 
":  " + 
"(b('L8b5') <= 3338.5) ? " + 
"-0.0049035388158502205" + 
":  " + 
"0.017555135820716647" + 
":  " + 
"(b('L8b3') <= 538.5) ? " + 
"(b('L8dt') <= 700442.0) ? " + 
"0.0010493276816120015" + 
":  " + 
"-0.01607408548424619" + 
":  " + 
"(b('L8b3') <= 542.5) ? " + 
"0.050270323749297324" + 
":  " + 
"-7.991690028826782e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1681.0) ? " + 
"(b('L8b5') <= 1638.0) ? " + 
"(b('L8dt') <= 695005.5) ? " + 
"0.0055860255652496445" + 
":  " + 
"-0.007162231241131409" + 
":  " + 
"(b('L8b5med') <= 2967.5) ? " + 
"0.019535257835776594" + 
":  " + 
"0.15996810645829515" + 
":  " + 
"(b('L8b6med') <= 2069.625) ? " + 
"(b('dsvv') <= -0.6148228645324707) ? " + 
"0.004982757069569569" + 
":  " + 
"-0.018699861954977245" + 
":  " + 
"(b('L8b6') <= 1580.5) ? " + 
"0.013845792226031602" + 
":  " + 
"-7.976307280127316e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3717016.5) ? " + 
"(b('L8dt') <= 3629242.5) ? " + 
"(b('L8dt') <= 3615282.5) ? " + 
"-7.784286300026747e-05" + 
":  " + 
"0.048313308227219014" + 
":  " + 
"(b('lat') <= 49.19237518310547) ? " + 
"-0.039874340390353064" + 
":  " + 
"0.002582656731726884" + 
":  " + 
"(b('lat') <= 37.76110076904297) ? " + 
"(b('L8b3') <= 734.5) ? " + 
"-0.06731402926358275" + 
":  " + 
"-0.004608081476500108" + 
":  " + 
"(b('crops') <= 39.166316986083984) ? " + 
"0.02065035421335361" + 
":  " + 
"0.002073981677318478" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 3.484816074371338) ? " + 
"(b('dsvv') <= 3.44174861907959) ? " + 
"(b('dsvv') <= 3.1158738136291504) ? " + 
"-0.00011534638479541823" + 
":  " + 
"0.007311487647861667" + 
":  " + 
"(b('lon') <= -100.6578483581543) ? " + 
"-0.08754458952561502" + 
":  " + 
"-0.02565718556129393" + 
":  " + 
"(b('L8b2med') <= 539.0) ? " + 
"(b('L8b2med') <= 460.0) ? " + 
"0.013908634855304441" + 
":  " + 
"-0.02623070092678541" + 
":  " + 
"(b('L8b7med') <= 2897.0) ? " + 
"0.010909313370491855" + 
":  " + 
"-0.013697235904612795" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2669.75) ? " + 
"(b('L8b4') <= 796.5) ? " + 
"(b('ndvi') <= 2693.0) ? " + 
"0.007761389189097229" + 
":  " + 
"-0.0004445969087300051" + 
":  " + 
"(b('L8b6') <= 1862.5) ? " + 
"0.017003447807704464" + 
":  " + 
"-0.0032534601698687576" + 
":  " + 
"(b('L8b11') <= 1124.5) ? " + 
"(b('L8b5med') <= 2422.5) ? " + 
"0.028198357260940513" + 
":  " + 
"-0.011410016072614172" + 
":  " + 
"(b('L8b11') <= 1134.5) ? " + 
"0.05787470046123858" + 
":  " + 
"0.0005002266412574975" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1443.5) ? " + 
"(b('L8b6') <= 2410.5) ? " + 
"(b('L8b6') <= 2407.0) ? " + 
"0.0003775662208952712" + 
":  " + 
"0.03770711016448609" + 
":  " + 
"(b('ndvi_med') <= 2664.5) ? " + 
"-0.034807449147374415" + 
":  " + 
"-0.005333152121572354" + 
":  " + 
"(b('L8b4') <= 835.5) ? " + 
"(b('L8b3') <= 844.0) ? " + 
"0.0030178790908501644" + 
":  " + 
"0.022809343455713938" + 
":  " + 
"(b('L8b6') <= 2498.5) ? " + 
"-0.00587175134252365" + 
":  " + 
"0.00024881358362767106" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1420.5) ? " + 
"(b('L8b3') <= 1062.5) ? " + 
"(b('L8b6') <= 3369.5) ? " + 
"0.00021629083605463135" + 
":  " + 
"-0.007396090562087421" + 
":  " + 
"(b('lon') <= -121.22985458374023) ? " + 
"0.08489441581701702" + 
":  " + 
"0.006978152783723188" + 
":  " + 
"(b('L8b2') <= 590.0) ? " + 
"(b('L8b6') <= 2482.0) ? " + 
"0.10440335530246148" + 
":  " + 
"0.009599892884748065" + 
":  " + 
"(b('L8b2') <= 701.5) ? " + 
"-0.008797894546842816" + 
":  " + 
"-0.00016496520604865634" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 770.5) ? " + 
"(b('L8b5') <= 3612.0) ? " + 
"(b('lon') <= -93.93420028686523) ? " + 
"-0.005170652934015029" + 
":  " + 
"0.0012939204410447522" + 
":  " + 
"(b('L8b3') <= 749.0) ? " + 
"-0.004251129477185626" + 
":  " + 
"-0.046748858271244156" + 
":  " + 
"(b('L8b2') <= 421.0) ? " + 
"(b('L8b3') <= 865.0) ? " + 
"0.015218944242710374" + 
":  " + 
"-0.014012192928656454" + 
":  " + 
"(b('L8b2') <= 424.5) ? " + 
"-0.02183620410794861" + 
":  " + 
"0.00017080645924411503" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3660.0) ? " + 
"(b('L8b5') <= 3655.5) ? " + 
"(b('L8b11') <= 3451.0) ? " + 
"7.800100729861467e-06" + 
":  " + 
"0.006406351018990664" + 
":  " + 
"(b('lon') <= -38.50421404838562) ? " + 
"-0.023971818969326163" + 
":  " + 
"0.025610684774619696" + 
":  " + 
"(b('L8b2') <= 480.5) ? " + 
"(b('L8b11') <= 1355.0) ? " + 
"-0.004268536692797014" + 
":  " + 
"0.022602872644684722" + 
":  " + 
"(b('L8b11') <= 2240.5) ? " + 
"-0.011803342705875663" + 
":  " + 
"0.0008815679607651198" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -120.6328010559082) ? " + 
"(b('lon') <= -120.79582977294922) ? " + 
"(b('L8b6') <= 2797.0) ? " + 
"-0.009329477517637035" + 
":  " + 
"0.0027715830161654793" + 
":  " + 
"(b('ndvi') <= 1904.5) ? " + 
"-0.007761596369571276" + 
":  " + 
"0.06021803262211899" + 
":  " + 
"(b('L8b5') <= 1681.0) ? " + 
"(b('L8b5') <= 1638.0) ? " + 
"-0.0009355038476530702" + 
":  " + 
"0.026855376938998594" + 
":  " + 
"(b('L8b5') <= 1699.5) ? " + 
"-0.018248998270139715" + 
":  " + 
"-0.00021754716133948272" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 665.5) ? " + 
"(b('lat') <= 43.76488494873047) ? " + 
"(b('dgvv') <= 4.587668418884277) ? " + 
"-0.00879117944945123" + 
":  " + 
"0.09362847793971592" + 
":  " + 
"(b('lon') <= -104.23934936523438) ? " + 
"0.0326896385452692" + 
":  " + 
"-0.0005257613449248551" + 
":  " + 
"(b('L8b4') <= 616.0) ? " + 
"(b('L8b11') <= 1310.0) ? " + 
"0.01641504249049458" + 
":  " + 
"-0.014671255985076874" + 
":  " + 
"(b('L8b11') <= 1185.5) ? " + 
"-0.006924201397070716" + 
":  " + 
"0.00020885447196963857" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1420.5) ? " + 
"(b('L8b3') <= 1062.5) ? " + 
"(b('L8b7med') <= 2151.5) ? " + 
"-0.0007791556676023914" + 
":  " + 
"0.003627046630836924" + 
":  " + 
"(b('L8b5') <= 3906.5) ? " + 
"0.009795590670847147" + 
":  " + 
"-0.00921484401662922" + 
":  " + 
"(b('L8b5med') <= 2071.5) ? " + 
"(b('dsvv') <= -1.7829155921936035) ? " + 
"0.052746103921420956" + 
":  " + 
"-0.0368711323685416" + 
":  " + 
"(b('L8b7med') <= 1454.5) ? " + 
"0.04165363280648346" + 
":  " + 
"-0.0007443547720493535" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4766.5) ? " + 
"(b('L8b5') <= 3660.0) ? " + 
"(b('L8b5') <= 3655.5) ? " + 
"0.00012328775311440252" + 
":  " + 
"0.019507020507083753" + 
":  " + 
"(b('L8b2med') <= 413.0) ? " + 
"-0.031977173507654964" + 
":  " + 
"-0.001365131068488971" + 
":  " + 
"(b('L8b2') <= 514.5) ? " + 
"(b('L8dt') <= 927890.5) ? " + 
"0.04495030727294022" + 
":  " + 
"0.021349494145376707" + 
":  " + 
"(b('dsvv') <= -2.0488948822021484) ? " + 
"0.052051854528996105" + 
":  " + 
"0.0010070251799431896" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 3464.5) ? " + 
"(b('sand') <= 17.0) ? " + 
"(b('ndvi') <= 3102.5) ? " + 
"0.028863512707699965" + 
":  " + 
"-0.08511902181637901" + 
":  " + 
"(b('ndvi_med') <= 4848.5) ? " + 
"-0.0004979581230247231" + 
":  " + 
"0.041118983159209345" + 
":  " + 
"(b('sand') <= 23.5) ? " + 
"(b('ndvi') <= 4374.0) ? " + 
"-0.023769723190679687" + 
":  " + 
"0.0066792496242270225" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"0.007076193244807678" + 
":  " + 
"-0.0011288974493999712" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 14.5) ? " + 
"(b('L8b5') <= 3182.0) ? " + 
"(b('L8dt') <= 5788343.5) ? " + 
"0.008198886606416027" + 
":  " + 
"-0.09927149150817727" + 
":  " + 
"(b('L8dt') <= 690415.5) ? " + 
"-0.07727791499018405" + 
":  " + 
"0.0006096227706613277" + 
":  " + 
"(b('ndvi') <= 3464.5) ? " + 
"(b('sand') <= 17.0) ? " + 
"0.02241327349207282" + 
":  " + 
"-0.0003958676982371855" + 
":  " + 
"(b('ndvi') <= 3560.0) ? " + 
"0.010495522204116123" + 
":  " + 
"0.00041130219577980307" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 26.74935531616211) ? " + 
"(b('lat') <= 31.407100677490234) ? " + 
"(b('L8b5') <= 3067.5) ? " + 
"0.00061823858897672" + 
":  " + 
"0.027547325007477735" + 
":  " + 
"(b('L8b6') <= 5456.5) ? " + 
"3.527451119811649e-05" + 
":  " + 
"-0.023442496149077046" + 
":  " + 
"(b('L8dt') <= 374325.5) ? " + 
"(b('L8b2') <= 737.5) ? " + 
"0.0011842507428930546" + 
":  " + 
"0.02902735042084062" + 
":  " + 
"(b('L8b5') <= 1686.0) ? " + 
"-0.03776792351100916" + 
":  " + 
"-0.005769555914523984" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2036.5) ? " + 
"(b('L8b6') <= 2723.5) ? " + 
"(b('crops') <= 95.60836410522461) ? " + 
"0.0004903174176147527" + 
":  " + 
"-0.016327391652603055" + 
":  " + 
"(b('L8b6') <= 2737.5) ? " + 
"0.036932740786290934" + 
":  " + 
"0.006825060725563623" + 
":  " + 
"(b('L8b5') <= 2037.5) ? " + 
"(b('dsvv') <= 0.37320375442504883) ? " + 
"-0.04710873629950348" + 
":  " + 
"-0.0710412723376375" + 
":  " + 
"(b('L8b2') <= 314.5) ? " + 
"0.006900046617787095" + 
":  " + 
"-0.0003284544983074548" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3218711.5) ? " + 
"(b('ndvi_med') <= 1509.0) ? " + 
"(b('dgvv') <= -1.3013687133789062) ? " + 
"0.00718838714901676" + 
":  " + 
"0.0004690273819625144" + 
":  " + 
"(b('ndvi') <= 1137.5) ? " + 
"-0.010672182452994693" + 
":  " + 
"-0.00032839640293803987" + 
":  " + 
"(b('L8b5med') <= 3022.0) ? " + 
"(b('sand') <= 77.5) ? " + 
"-0.0048822250812791635" + 
":  " + 
"0.01872669819247535" + 
":  " + 
"(b('L8b7med') <= 2895.25) ? " + 
"0.012701148260694932" + 
":  " + 
"-0.006616385502457084" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= -3.261660575866699) ? " + 
"(b('crops') <= 88.85982513427734) ? " + 
"(b('L8dt') <= 22559.0) ? " + 
"0.02838263379049825" + 
":  " + 
"-0.007584215258847773" + 
":  " + 
"(b('dsvv') <= -3.685307502746582) ? " + 
"0.024840294700282206" + 
":  " + 
"0.0016235266104185925" + 
":  " + 
"(b('ndvi') <= 5229.5) ? " + 
"(b('ndvi') <= 5018.5) ? " + 
"0.00013067500075489278" + 
":  " + 
"0.011192539050413926" + 
":  " + 
"(b('ndvi') <= 5724.0) ? " + 
"-0.010296791901707335" + 
":  " + 
"0.0016256722046596919" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1595.5) ? " + 
"(b('L8b11') <= 1586.5) ? " + 
"(b('L8b2') <= 543.0) ? " + 
"1.1220021211060966e-05" + 
":  " + 
"-0.010722229266682672" + 
":  " + 
"(b('lat') <= 43.18190002441406) ? " + 
"-0.04124792158111722" + 
":  " + 
"-0.002873356173949719" + 
":  " + 
"(b('L8b11') <= 1614.5) ? " + 
"(b('lon') <= -101.20384979248047) ? " + 
"-0.014920563690394186" + 
":  " + 
"0.027369780123431796" + 
":  " + 
"(b('L8b11') <= 1651.5) ? " + 
"-0.009238537873657048" + 
":  " + 
"0.0003604146496312902" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 727.5) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"(b('L8b5med') <= 3285.0) ? " + 
"8.070355670453821e-05" + 
":  " + 
"-0.020317544131324458" + 
":  " + 
"(b('lat') <= 32.848440170288086) ? " + 
"0.02058075682024946" + 
":  " + 
"-0.020556821540374186" + 
":  " + 
"(b('L8b2') <= 464.5) ? " + 
"(b('lat') <= 41.222354888916016) ? " + 
"0.011754706782743285" + 
":  " + 
"-0.00023475094576136076" + 
":  " + 
"(b('L8b2') <= 468.25) ? " + 
"-0.0175298634079587" + 
":  " + 
"1.985691155802077e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2436.5) ? " + 
"(b('L8b5') <= 2341.5) ? " + 
"(b('L8b6') <= 3629.5) ? " + 
"0.000311183230177948" + 
":  " + 
"-0.01875555252355242" + 
":  " + 
"(b('L8b5') <= 2343.0) ? " + 
"0.056944851461566234" + 
":  " + 
"0.004795899120756554" + 
":  " + 
"(b('L8b5') <= 2470.5) ? " + 
"(b('sand') <= 20.5) ? " + 
"-0.05431111529519995" + 
":  " + 
"-0.0067305176049041225" + 
":  " + 
"(b('L8b3') <= 518.5) ? " + 
"0.02007938483742759" + 
":  " + 
"-0.00015703801473746515" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 665.5) ? " + 
"(b('lat') <= 43.76488494873047) ? " + 
"(b('ndvi') <= 3550.5) ? " + 
"-0.002194212314161747" + 
":  " + 
"-0.020947967871548897" + 
":  " + 
"(b('lon') <= -104.23934936523438) ? " + 
"0.02955882710066381" + 
":  " + 
"-0.0006200908380817082" + 
":  " + 
"(b('L8b2') <= 460.5) ? " + 
"(b('L8b2') <= 459.5) ? " + 
"0.0020088903981200163" + 
":  " + 
"0.09500644915056075" + 
":  " + 
"(b('L8b3') <= 712.5) ? " + 
"-0.015067130905806294" + 
":  " + 
"-5.145762035721316e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2741.5) ? " + 
"(b('sand') <= 38.5) ? " + 
"(b('L8b5') <= 2726.5) ? " + 
"-0.002316602407375444" + 
":  " + 
"0.029936482823968963" + 
":  " + 
"(b('L8b5med') <= 2817.5) ? " + 
"0.0009095149079111616" + 
":  " + 
"0.006680226599545485" + 
":  " + 
"(b('L8b5') <= 2793.5) ? " + 
"(b('L8b3') <= 701.5) ? " + 
"-0.046725962328498995" + 
":  " + 
"-0.006189658564306193" + 
":  " + 
"(b('L8b5') <= 2804.5) ? " + 
"0.017420331199601635" + 
":  " + 
"-0.0002985393199416343" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -120.6328010559082) ? " + 
"(b('lon') <= -120.79582977294922) ? " + 
"(b('L8b5med') <= 1869.0) ? " + 
"-0.044304166295632046" + 
":  " + 
"0.0003993428049963382" + 
":  " + 
"(b('ndvi') <= 1941.0) ? " + 
"-0.0035779631200169456" + 
":  " + 
"0.06101349330885302" + 
":  " + 
"(b('L8b5') <= 1681.0) ? " + 
"(b('L8b5') <= 1638.0) ? " + 
"-0.0005168506605668385" + 
":  " + 
"0.024368860577142108" + 
":  " + 
"(b('L8b5med') <= 1718.75) ? " + 
"0.016042947937475852" + 
":  " + 
"-0.0003330348033339661" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3768.75) ? " + 
"(b('ndvi_med') <= 5674.5) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"4.759113428498747e-05" + 
":  " + 
"-0.007888598908165873" + 
":  " + 
"(b('ndvi') <= 5360.5) ? " + 
"0.01589408188531127" + 
":  " + 
"-0.03713470753202382" + 
":  " + 
"(b('ndvi') <= 820.0) ? " + 
"(b('dgvv') <= 0.08434629440307617) ? " + 
"0.0037138554473438164" + 
":  " + 
"0.06014647250684752" + 
":  " + 
"(b('dgvv') <= 1.659766674041748) ? " + 
"0.004315258954713559" + 
":  " + 
"-0.033644890233236295" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4677.0) ? " + 
"(b('L8b5') <= 4619.5) ? " + 
"(b('ndvi_med') <= 5674.5) ? " + 
"3.3372341974200326e-05" + 
":  " + 
"-0.01332611657856814" + 
":  " + 
"(b('ndvi') <= 5914.0) ? " + 
"-0.00822807745433276" + 
":  " + 
"-0.03263820764424262" + 
":  " + 
"(b('ndvi') <= 5908.5) ? " + 
"(b('L8b3') <= 1098.5) ? " + 
"0.04402917649071809" + 
":  " + 
"0.004065387066404179" + 
":  " + 
"(b('L8dt') <= 471617.0) ? " + 
"0.015218090768042486" + 
":  " + 
"-0.016180393198896078" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1636.5) ? " + 
"(b('L8b6') <= 2758.0) ? " + 
"(b('lat') <= 38.48287391662598) ? " + 
"-0.026722106672926824" + 
":  " + 
"-0.001411776075438136" + 
":  " + 
"(b('ndvi_med') <= 2471.5) ? " + 
"-0.0005853271401423323" + 
":  " + 
"0.025754535326564784" + 
":  " + 
"(b('lon') <= -121.20288467407227) ? " + 
"(b('ndvi') <= 2366.0) ? " + 
"0.044789183346359805" + 
":  " + 
"0.0019110692651634212" + 
":  " + 
"(b('ndvi') <= 1638.5) ? " + 
"0.04438233090500363" + 
":  " + 
"0.00015443668759548886" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 179923.5) ? " + 
"(b('lat') <= 55.93754959106445) ? " + 
"(b('dsvv') <= -0.07076454162597656) ? " + 
"0.0015917725714835657" + 
":  " + 
"-0.00321077725336727" + 
":  " + 
"(b('L8b6') <= 2329.5) ? " + 
"0.012100253482820195" + 
":  " + 
"-0.026260296797001405" + 
":  " + 
"(b('L8dt') <= 180387.5) ? " + 
"(b('ndvi') <= 1668.0) ? " + 
"-0.002987568173789723" + 
":  " + 
"0.03334154350240524" + 
":  " + 
"(b('L8dt') <= 193270.5) ? " + 
"-0.013314901580621185" + 
":  " + 
"0.00018874878149291788" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 872.5) ? " + 
"(b('L8b5') <= 3915.5) ? " + 
"(b('L8b3') <= 860.5) ? " + 
"-0.000327547322845153" + 
":  " + 
"-0.010586951273010117" + 
":  " + 
"(b('L8b3') <= 857.5) ? " + 
"0.00929564184381849" + 
":  " + 
"0.08207732548047406" + 
":  " + 
"(b('L8b4') <= 1231.5) ? " + 
"(b('L8b6') <= 3399.5) ? " + 
"0.004445587440429565" + 
":  " + 
"-0.01057262557955568" + 
":  " + 
"(b('L8b5') <= 2209.5) ? " + 
"-0.007404090863623119" + 
":  " + 
"5.443467750163389e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2142.5) ? " + 
"(b('L8b5') <= 2140.5) ? " + 
"(b('sand') <= 54.5) ? " + 
"0.0025846448497216816" + 
":  " + 
"-0.0033318653806568566" + 
":  " + 
"(b('L8b7med') <= 2107.25) ? " + 
"0.010361860237001648" + 
":  " + 
"0.07338335757889398" + 
":  " + 
"(b('L8b5') <= 2143.5) ? " + 
"(b('lat') <= 40.96779441833496) ? " + 
"0.04322193808600091" + 
":  " + 
"-0.053747048643932704" + 
":  " + 
"(b('L8b6') <= 1366.0) ? " + 
"0.06025043594427677" + 
":  " + 
"-0.00022687516984898828" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4653.0) ? " + 
"(b('L8b5') <= 4619.5) ? " + 
"(b('ndvi_med') <= 5073.5) ? " + 
"5.32234930488274e-05" + 
":  " + 
"-0.00706239060297998" + 
":  " + 
"(b('dsvv') <= 2.7193703651428223) ? " + 
"-0.023988512958254847" + 
":  " + 
"0.02588349176530423" + 
":  " + 
"(b('ndvi') <= 5908.5) ? " + 
"(b('L8b3') <= 1098.5) ? " + 
"0.04244769600081356" + 
":  " + 
"0.003701763922757558" + 
":  " + 
"(b('dsvv') <= -0.3896975517272949) ? " + 
"0.016105118083388187" + 
":  " + 
"-0.0169131849946347" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1339.0) ? " + 
"(b('L8b11') <= 1603.5) ? " + 
"(b('L8dt') <= 826729.5) ? " + 
"-0.011472998610278746" + 
":  " + 
"-0.10299329835607979" + 
":  " + 
"(b('ndvi') <= 1530.5) ? " + 
"0.0009909271726305576" + 
":  " + 
"0.017123480418233028" + 
":  " + 
"(b('ndvi') <= 1636.5) ? " + 
"(b('lat') <= -26.78680992126465) ? " + 
"-0.02188081557589153" + 
":  " + 
"-0.001067809751605699" + 
":  " + 
"(b('ndvi') <= 1637.5) ? " + 
"0.06933015357437289" + 
":  " + 
"0.00020415196866127488" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1443.5) ? " + 
"(b('L8b6') <= 2604.5) ? " + 
"(b('L8b4') <= 1089.0) ? " + 
"-0.0007607596649636063" + 
":  " + 
"0.034429294870607946" + 
":  " + 
"(b('crops') <= 24.55074691772461) ? " + 
"-0.04932762190433531" + 
":  " + 
"-6.453334880930878e-05" + 
":  " + 
"(b('L8b4') <= 834.5) ? " + 
"(b('L8b6') <= 2610.0) ? " + 
"0.00784602098079661" + 
":  " + 
"-0.0011858637632840255" + 
":  " + 
"(b('L8b2') <= 524.5) ? " + 
"-0.004294006548638403" + 
":  " + 
"0.00031395717003890577" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1623.0) ? " + 
"(b('dgvv') <= -1.5321149826049805) ? " + 
"(b('L8b6med') <= 2547.5) ? " + 
"0.003494111675003882" + 
":  " + 
"-0.024866481878855446" + 
":  " + 
"(b('dsvv') <= -1.5277423858642578) ? " + 
"0.10986567892595088" + 
":  " + 
"0.002117933641950134" + 
":  " + 
"(b('L8b11') <= 1594.5) ? " + 
"(b('L8b11') <= 1391.5) ? " + 
"0.001116466039079351" + 
":  " + 
"-0.00887681814125467" + 
":  " + 
"(b('L8b11') <= 1614.5) ? " + 
"0.014838418904655629" + 
":  " + 
"0.00022640342870161218" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1242.5) ? " + 
"(b('L8b6med') <= 2452.0) ? " + 
"(b('L8b6med') <= 2449.0) ? " + 
"0.001672671661395527" + 
":  " + 
"0.03195100470647097" + 
":  " + 
"(b('dsvv') <= 0.5904331207275391) ? " + 
"-0.013470139917622173" + 
":  " + 
"0.0032858719677519477" + 
":  " + 
"(b('L8b6') <= 1895.0) ? " + 
"(b('ndvi') <= 3630.5) ? " + 
"0.0013362079166582242" + 
":  " + 
"0.04394897479045167" + 
":  " + 
"(b('L8b3') <= 570.0) ? " + 
"-0.010584547164708224" + 
":  " + 
"0.0001766479552399077" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2461.0) ? " + 
"(b('L8b4') <= 1262.5) ? " + 
"(b('lon') <= -118.93999481201172) ? " + 
"0.010183876219182604" + 
":  " + 
"-0.001299501386060822" + 
":  " + 
"(b('lat') <= 46.49909973144531) ? " + 
"-0.002745244616280845" + 
":  " + 
"-0.02034006806561566" + 
":  " + 
"(b('L8b5med') <= 2478.5) ? " + 
"(b('L8b5') <= 1868.5) ? " + 
"-0.0884871529878268" + 
":  " + 
"0.013129761686499142" + 
":  " + 
"(b('L8b5') <= 2436.5) ? " + 
"0.002420127571423893" + 
":  " + 
"-0.0003230204617456645" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 31.407100677490234) ? " + 
"(b('L8b2') <= 569.5) ? " + 
"(b('L8b2') <= 482.5) ? " + 
"-9.106763020031038e-05" + 
":  " + 
"0.025241830919681924" + 
":  " + 
"(b('L8b11') <= 2782.5) ? " + 
"-0.011730719044727608" + 
":  " + 
"0.007653995438410378" + 
":  " + 
"(b('L8b3') <= 826.5) ? " + 
"(b('L8b6') <= 3297.0) ? " + 
"-0.000866970682688364" + 
":  " + 
"-0.02568874424440767" + 
":  " + 
"(b('L8b4') <= 944.5) ? " + 
"0.0046862977960337735" + 
":  " + 
"-5.587391646515307e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 653.5) ? " + 
"(b('dsvv') <= 0.7163405418395996) ? " + 
"(b('L8b2') <= 195.0) ? " + 
"0.0010969844747810732" + 
":  " + 
"0.06287791731877733" + 
":  " + 
"0.08637282669684085" + 
":  " + 
"(b('L8b5') <= 1320.5) ? " + 
"(b('L8b11') <= 1819.0) ? " + 
"-0.004937935962197413" + 
":  " + 
"-0.03054373773869553" + 
":  " + 
"(b('L8b5') <= 1356.0) ? " + 
"0.019244450857548775" + 
":  " + 
"1.0145992025225989e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2397054.0) ? " + 
"(b('dsvv') <= 5.5451555252075195) ? " + 
"(b('dsvv') <= 4.70723557472229) ? " + 
"-0.00019580741222107711" + 
":  " + 
"0.011833071976025721" + 
":  " + 
"(b('dsvv') <= 5.868550062179565) ? " + 
"-0.06315652801787972" + 
":  " + 
"-0.0038483120219800463" + 
":  " + 
"(b('L8dt') <= 2398772.0) ? " + 
"(b('L8b5') <= 2440.5) ? " + 
"-0.04061944971789395" + 
":  " + 
"0.05194575948987739" + 
":  " + 
"(b('L8b6') <= 4860.5) ? " + 
"0.0017622519251726733" + 
":  " + 
"-0.02711760552218335" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 316.5) ? " + 
"0.06735567538287761" + 
":  " + 
"(b('sand') <= 87.0) ? " + 
"(b('L8b11') <= 1341.5) ? " + 
"-0.00150437792266497" + 
":  " + 
"0.00018575005531855365" + 
":  " + 
"(b('dgvv') <= 3.287851333618164) ? " + 
"0.003431864402103985" + 
":  " + 
"0.10195032481842439" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 729.5) ? " + 
"(b('L8b5') <= 3754.0) ? " + 
"(b('L8b3') <= 764.5) ? " + 
"0.00037809358805747617" + 
":  " + 
"0.0100192715436724" + 
":  " + 
"(b('L8b6') <= 2560.5) ? " + 
"-0.05166282178361286" + 
":  " + 
"0.00560088234155631" + 
":  " + 
"(b('L8b3') <= 631.0) ? " + 
"(b('L8b5med') <= 2231.5) ? " + 
"-0.03118650913685434" + 
":  " + 
"-0.005788139856254565" + 
":  " + 
"(b('L8b3') <= 702.5) ? " + 
"0.0061322294459958526" + 
":  " + 
"-0.00032450107127460253" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 5819576.0) ? " + 
"(b('L8dt') <= 5788343.5) ? " + 
"(b('L8b3') <= 1708.5) ? " + 
"-0.0001802784935872657" + 
":  " + 
"0.0021713241969116776" + 
":  " + 
"-0.08925492305573746" + 
":  " + 
"(b('lon') <= -5.3525800704956055) ? " + 
"(b('L8b6') <= 2494.5) ? " + 
"0.027426636024345544" + 
":  " + 
"-0.01573007443196298" + 
":  " + 
"(b('lat') <= 56.02764892578125) ? " + 
"0.01615057506608266" + 
":  " + 
"-0.0053139972499347855" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5med') <= 3046.5) ? " + 
"(b('L8b5med') <= 3039.5) ? " + 
"-0.0002503408680858514" + 
":  " + 
"-0.019031083634009748" + 
":  " + 
"(b('L8b5') <= 3124.0) ? " + 
"0.004655001031796092" + 
":  " + 
"-0.0015639172125412341" + 
":  " + 
"(b('L8b5med') <= 3138.5) ? " + 
"(b('ndvi') <= 6589.0) ? " + 
"0.0018594406077778003" + 
":  " + 
"0.05168025180785292" + 
":  " + 
"(b('L8b5med') <= 3228.0) ? " + 
"-0.020544279812529646" + 
":  " + 
"-0.0010553897250157734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1381.5) ? " + 
"(b('L8b3') <= 1129.0) ? " + 
"(b('L8b11') <= 2001.5) ? " + 
"-0.0006056172747641336" + 
":  " + 
"0.00277723092152788" + 
":  " + 
"(b('L8b6med') <= 2451.0) ? " + 
"-0.017103450170923788" + 
":  " + 
"0.021903541797028265" + 
":  " + 
"(b('L8b11') <= 1739.0) ? " + 
"(b('L8b5med') <= 3176.5) ? " + 
"0.009199649286550957" + 
":  " + 
"0.09236358013284453" + 
":  " + 
"(b('L8b6') <= 2831.5) ? " + 
"-0.010559692169577799" + 
":  " + 
"-0.0004615275888549219" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1623.0) ? " + 
"(b('L8b4') <= 1745.5) ? " + 
"(b('L8b11') <= 2343.0) ? " + 
"0.0007403863296411318" + 
":  " + 
"0.025807679663113443" + 
":  " + 
"(b('dgvv') <= 2.592574119567871) ? " + 
"-0.03455200060267626" + 
":  " + 
"0.04984765041013375" + 
":  " + 
"(b('L8b11') <= 1524.5) ? " + 
"(b('L8b11') <= 1398.5) ? " + 
"0.0010387957891051156" + 
":  " + 
"-0.01165718515612328" + 
":  " + 
"(b('L8b11') <= 1526.0) ? " + 
"0.06532643556031197" + 
":  " + 
"0.0001859177503780227" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 729.5) ? " + 
"(b('lat') <= 38.149349212646484) ? " + 
"(b('lat') <= 38.147823333740234) ? " + 
"0.005219287457117923" + 
":  " + 
"0.07724440894131859" + 
":  " + 
"(b('L8b5') <= 3754.0) ? " + 
"0.00024359746377030083" + 
":  " + 
"-0.05374839319959033" + 
":  " + 
"(b('L8dt') <= 1279.0) ? " + 
"(b('L8dt') <= 1277.0) ? " + 
"-0.025525491933958224" + 
":  " + 
"-0.17932984533711732" + 
":  " + 
"(b('L8dt') <= 1289.0) ? " + 
"0.16089791243691223" + 
":  " + 
"-0.00020661741647534803" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -9.844696760177612) ? " + 
"(b('lat') <= 41.29277992248535) ? " + 
"0.03329539077749871" + 
":  " + 
"0.06145969259145889" + 
":  " + 
"(b('dsvv') <= -3.261660575866699) ? " + 
"(b('lon') <= 9.170949935913086) ? " + 
"-0.001470590309904766" + 
":  " + 
"-0.022757748899544628" + 
":  " + 
"(b('L8b5med') <= 2461.0) ? " + 
"-0.0011289230147543724" + 
":  " + 
"0.0003849873461034168" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 45.30614471435547) ? " + 
"(b('ndvi') <= 4390.5) ? " + 
"(b('L8b11') <= 1487.5) ? " + 
"-0.004307693271054386" + 
":  " + 
"0.0010139884706301036" + 
":  " + 
"(b('sand') <= 32.0) ? " + 
"0.02576411448519754" + 
":  " + 
"0.001156771599259226" + 
":  " + 
"(b('dsvv') <= 0.6497306823730469) ? " + 
"(b('lat') <= 39.95979881286621) ? " + 
"-0.005268539893378295" + 
":  " + 
"0.0010604680039490333" + 
":  " + 
"(b('lat') <= 37.1744499206543) ? " + 
"0.008674504836288573" + 
":  " + 
"-0.0032726848069367376" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2754.5) ? " + 
"(b('L8b11') <= 2108.5) ? " + 
"(b('L8b11') <= 2105.5) ? " + 
"0.0008656500917246972" + 
":  " + 
"0.048078660600568014" + 
":  " + 
"(b('L8b5med') <= 2669.75) ? " + 
"-0.0054343809127368825" + 
":  " + 
"-0.027271181439087477" + 
":  " + 
"(b('L8b6') <= 2757.5) ? " + 
"(b('L8dt') <= 422667.0) ? " + 
"0.0013959776787364668" + 
":  " + 
"-0.04382647111169228" + 
":  " + 
"(b('L8b11') <= 1849.5) ? " + 
"-0.004735364832003412" + 
":  " + 
"0.00022697748973861534" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 4.130900621414185) ? " + 
"(b('dgvv') <= 4.108705520629883) ? " + 
"(b('dgvv') <= 4.052122592926025) ? " + 
"-6.778656144426767e-05" + 
":  " + 
"0.026937636958838" + 
":  " + 
"(b('lon') <= -5.326294898986816) ? " + 
"-0.07424274303211989" + 
":  " + 
"0.007570511472736188" + 
":  " + 
"(b('dgvv') <= 4.152717113494873) ? " + 
"(b('ndvi_med') <= 1697.0) ? " + 
"0.1573845918685868" + 
":  " + 
"0.1312222302286456" + 
":  " + 
"(b('sand') <= 34.0) ? " + 
"0.02012900824260122" + 
":  " + 
"-0.0012418589646710988" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 395.5) ? " + 
"(b('L8b6') <= 2954.0) ? " + 
"(b('L8b2') <= 559.0) ? " + 
"0.0010703070623480962" + 
":  " + 
"-0.039206827099189996" + 
":  " + 
"(b('L8b6') <= 2955.5) ? " + 
"0.09973431181724132" + 
":  " + 
"0.017689611490742357" + 
":  " + 
"(b('ndvi') <= 3211.5) ? " + 
"(b('sand') <= 17.0) ? " + 
"0.021502987392114842" + 
":  " + 
"-0.000692435512094177" + 
":  " + 
"(b('ndvi') <= 3283.5) ? " + 
"0.014056762790140303" + 
":  " + 
"0.000254468707853492" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1341.5) ? " + 
"(b('sand') <= 16.5) ? " + 
"(b('L8b4') <= 651.5) ? " + 
"-0.0018891067210277837" + 
":  " + 
"-0.07012745313274595" + 
":  " + 
"(b('L8b11') <= 1335.0) ? " + 
"-6.909474652023835e-05" + 
":  " + 
"-0.022080303568697064" + 
":  " + 
"(b('L8b6') <= 1895.0) ? " + 
"(b('L8b7med') <= 1574.5) ? " + 
"0.058733772496907775" + 
":  " + 
"0.002160536584018126" + 
":  " + 
"(b('L8b11') <= 1344.5) ? " + 
"0.04604294025029554" + 
":  " + 
"7.085787631120217e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5229.5) ? " + 
"(b('ndvi') <= 5018.5) ? " + 
"(b('ndvi') <= 4966.5) ? " + 
"7.924901302040383e-05" + 
":  " + 
"-0.013136785479834753" + 
":  " + 
"(b('L8b6') <= 2242.0) ? " + 
"-0.009613205711440153" + 
":  " + 
"0.01642252929025637" + 
":  " + 
"(b('L8b5') <= 2831.5) ? " + 
"(b('L8b7med') <= 1316.5) ? " + 
"-0.03596964203271195" + 
":  " + 
"-0.007413043252930023" + 
":  " + 
"(b('L8b5') <= 2846.0) ? " + 
"0.0911012346852725" + 
":  " + 
"-6.797086180538163e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1560.5) ? " + 
"(b('L8b4') <= 1154.5) ? " + 
"(b('L8b3') <= 848.5) ? " + 
"0.0016523545893038574" + 
":  " + 
"0.026485573258012294" + 
":  " + 
"(b('ndvi') <= 2819.5) ? " + 
"-0.0006481479855592396" + 
":  " + 
"0.012615703169550652" + 
":  " + 
"(b('L8b4') <= 2271.5) ? " + 
"(b('L8b3') <= 1763.5) ? " + 
"-0.00015993649798397403" + 
":  " + 
"0.03369584978410221" + 
":  " + 
"(b('L8b5') <= 3318.5) ? " + 
"-0.028650068948059715" + 
":  " + 
"-0.0004923513521104709" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2974.5) ? " + 
"(b('L8b6') <= 4165.5) ? " + 
"(b('L8b6') <= 4038.0) ? " + 
"-0.00017995009372356006" + 
":  " + 
"0.014369328318221684" + 
":  " + 
"(b('L8dt') <= 2355340.5) ? " + 
"-0.016073362994675693" + 
":  " + 
"0.03733510986316583" + 
":  " + 
"(b('L8b11') <= 3007.0) ? " + 
"(b('sand') <= 41.5) ? " + 
"0.04434231783913945" + 
":  " + 
"0.004054224823188417" + 
":  " + 
"(b('lon') <= -120.2534408569336) ? " + 
"-0.014987041419794562" + 
":  " + 
"0.0012446531665690791" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 316.5) ? " + 
"(b('lon') <= -38.544898986816406) ? " + 
"(b('L8b2') <= 309.0) ? " + 
"-0.014269314979563755" + 
":  " + 
"0.025856148400822385" + 
":  " + 
"(b('L8b5') <= 1955.5) ? " + 
"-0.005623223732015008" + 
":  " + 
"0.012205055187524275" + 
":  " + 
"(b('L8b3') <= 562.5) ? " + 
"(b('L8b3') <= 561.5) ? " + 
"-0.00809103352686483" + 
":  " + 
"-0.08655419152547925" + 
":  " + 
"(b('L8b11') <= 1242.5) ? " + 
"-0.004241798855726148" + 
":  " + 
"0.00023673884920791876" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 729.5) ? " + 
"(b('L8b6') <= 2686.5) ? " + 
"(b('lat') <= 38.149349212646484) ? " + 
"0.010615104667981115" + 
":  " + 
"0.000569708236555827" + 
":  " + 
"(b('L8b6') <= 2703.5) ? " + 
"-0.06576798575608177" + 
":  " + 
"-0.005012434843775361" + 
":  " + 
"(b('L8b3') <= 811.5) ? " + 
"(b('L8b3') <= 807.5) ? " + 
"-0.0019215609858402344" + 
":  " + 
"-0.024174668412038663" + 
":  " + 
"(b('L8b2') <= 381.0) ? " + 
"-0.02725080085103572" + 
":  " + 
"0.0003459466464450734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2036.5) ? " + 
"(b('L8b3') <= 1102.5) ? " + 
"(b('ndvi') <= 670.5) ? " + 
"0.17323575164747745" + 
":  " + 
"0.0007278380332983397" + 
":  " + 
"(b('L8b6') <= 2084.5) ? " + 
"-0.020197888654905467" + 
":  " + 
"0.028375903999508324" + 
":  " + 
"(b('L8b5') <= 2037.5) ? " + 
"(b('dgvv') <= 0.34427499771118164) ? " + 
"-0.04003451364478751" + 
":  " + 
"-0.06367626135439164" + 
":  " + 
"(b('L8b11') <= 675.5) ? " + 
"0.044215488059363595" + 
":  " + 
"-0.00017738239373446194" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1381.5) ? " + 
"(b('L8b3') <= 1129.0) ? " + 
"(b('L8b11') <= 2001.5) ? " + 
"-0.0004807853887667502" + 
":  " + 
"0.002362213262472292" + 
":  " + 
"(b('lon') <= -117.21749496459961) ? " + 
"0.08595934039244381" + 
":  " + 
"0.011895364125737388" + 
":  " + 
"(b('L8b11') <= 1739.0) ? " + 
"(b('dsvv') <= -1.6576533317565918) ? " + 
"0.07260136797629671" + 
":  " + 
"0.006919207564128927" + 
":  " + 
"(b('L8b2') <= 693.5) ? " + 
"-0.006554823916031754" + 
":  " + 
"-0.00016131298046347675" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 946.5) ? " + 
"(b('L8b4') <= 901.5) ? " + 
"(b('lon') <= -104.0040512084961) ? " + 
"0.0070271997641121" + 
":  " + 
"-0.000848885929658408" + 
":  " + 
"(b('L8b2') <= 464.0) ? " + 
"0.02544891225135855" + 
":  " + 
"0.001639428582916882" + 
":  " + 
"(b('L8dt') <= 1072.0) ? " + 
"(b('dsvv') <= -0.7916836738586426) ? " + 
"-0.0741897604312191" + 
":  " + 
"-0.1415194055981196" + 
":  " + 
"(b('L8b4') <= 1020.5) ? " + 
"-0.005292358048491811" + 
":  " + 
"0.0001383310058240262" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 802.5) ? " + 
"(b('L8b3') <= 885.5) ? " + 
"(b('L8b11') <= 1332.5) ? " + 
"0.0027455594229467816" + 
":  " + 
"0.04726426347626575" + 
":  " + 
"(b('L8dt') <= 549.0) ? " + 
"-0.12736746503830765" + 
":  " + 
"-0.044414395098047954" + 
":  " + 
"(b('L8dt') <= 1279.0) ? " + 
"(b('L8b6') <= 2473.0) ? " + 
"0.0806373478741852" + 
":  " + 
"-0.05748734644215411" + 
":  " + 
"(b('L8dt') <= 1280.5) ? " + 
"0.14555594785721865" + 
":  " + 
"-1.9590883327613505e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 392.5) ? " + 
"(b('ndvi') <= 2750.5) ? " + 
"(b('L8b2med') <= 357.5) ? " + 
"0.03321900757604781" + 
":  " + 
"0.005109713452148637" + 
":  " + 
"(b('L8b5') <= 3337.5) ? " + 
"-0.0023154357790799054" + 
":  " + 
"0.016571354772585818" + 
":  " + 
"(b('L8b4') <= 564.5) ? " + 
"(b('crops') <= 97.71894836425781) ? " + 
"-0.007027398642479086" + 
":  " + 
"0.047248288044695747" + 
":  " + 
"(b('L8b4') <= 621.5) ? " + 
"0.008018294934153286" + 
":  " + 
"-0.00020675095877053615" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2217.25) ? " + 
"(b('L8b4') <= 1155.0) ? " + 
"(b('lat') <= 43.45442581176758) ? " + 
"0.009749141837494443" + 
":  " + 
"-0.001994086637852208" + 
":  " + 
"(b('ndvi_med') <= 2075.25) ? " + 
"-0.003983788320783434" + 
":  " + 
"-0.023034766064339938" + 
":  " + 
"(b('L8dt') <= 8076292.5) ? " + 
"(b('dgvv') <= -6.216428756713867) ? " + 
"0.04929571618470464" + 
":  " + 
"0.0001319782627080104" + 
":  " + 
"(b('L8b7med') <= 2292.5) ? " + 
"0.014749328778141689" + 
":  " + 
"0.05977653588912518" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5med') <= 3046.5) ? " + 
"(b('L8b5') <= 3233.5) ? " + 
"-0.0007904517779213211" + 
":  " + 
"0.00485968967117524" + 
":  " + 
"(b('dsvv') <= -2.5011377334594727) ? " + 
"-0.008742900141554932" + 
":  " + 
"0.00276937371968053" + 
":  " + 
"(b('dsvv') <= 2.070889472961426) ? " + 
"(b('lon') <= -5.546385049819946) ? " + 
"-0.005631024723842999" + 
":  " + 
"0.0016397596272502818" + 
":  " + 
"(b('L8dt') <= 453403.5) ? " + 
"-0.028972925382184236" + 
":  " + 
"-0.0016887794871911696" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2741.5) ? " + 
"(b('L8b3') <= 1453.5) ? " + 
"(b('L8b4') <= 1833.5) ? " + 
"0.0005427084660007288" + 
":  " + 
"-0.01894623359968852" + 
":  " + 
"(b('lon') <= -104.46354293823242) ? " + 
"0.001414028242534541" + 
":  " + 
"0.04073013081275444" + 
":  " + 
"(b('L8b5') <= 2793.5) ? " + 
"(b('L8b3') <= 701.5) ? " + 
"-0.04199004356725015" + 
":  " + 
"-0.005565197380503106" + 
":  " + 
"(b('L8b5') <= 2804.5) ? " + 
"0.015336139687725268" + 
":  " + 
"-0.0002702010153933217" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3768.75) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4326.5) ? " + 
"-7.273864205991784e-06" + 
":  " + 
"0.024407581810954482" + 
":  " + 
"(b('L8b5') <= 4675.5) ? " + 
"-0.011705722871201972" + 
":  " + 
"0.010970225591792391" + 
":  " + 
"(b('ndvi') <= 820.0) ? " + 
"(b('L8b11') <= 3951.25) ? " + 
"0.055230835587952144" + 
":  " + 
"0.0024553993929759812" + 
":  " + 
"(b('dsvv') <= 1.6493310928344727) ? " + 
"0.0036488350701292804" + 
":  " + 
"-0.026684036965076246" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 3410.5) ? " + 
"(b('ndvi') <= 3321.5) ? " + 
"(b('lat') <= 56.023799896240234) ? " + 
"-0.0002100525407659057" + 
":  " + 
"0.017796422434534224" + 
":  " + 
"(b('L8b2med') <= 327.5) ? " + 
"-0.11600784717623809" + 
":  " + 
"-0.007860259018315231" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"(b('sand') <= 24.5) ? " + 
"-0.004764219304756082" + 
":  " + 
"0.007555076085422851" + 
":  " + 
"(b('lat') <= 41.29464912414551) ? " + 
"0.004817559504233439" + 
":  " + 
"-0.0035641303313598714" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2med') <= 392.5) ? " + 
"(b('L8b11') <= 1328.5) ? " + 
"(b('L8b11') <= 1323.0) ? " + 
"-0.0024334647286383144" + 
":  " + 
"-0.07468050553676321" + 
":  " + 
"(b('L8b6') <= 2546.0) ? " + 
"0.025477908673804322" + 
":  " + 
"0.002167133686204972" + 
":  " + 
"(b('ndvi') <= 3218.0) ? " + 
"(b('sand') <= 17.0) ? " + 
"0.019498093202711522" + 
":  " + 
"-0.0006260630423170317" + 
":  " + 
"(b('ndvi') <= 3283.5) ? " + 
"0.01284730108603855" + 
":  " + 
"0.00024135662793949069" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2762.5) ? " + 
"(b('L8b5') <= 2760.5) ? " + 
"(b('sand') <= 38.5) ? " + 
"-0.0017003160244336384" + 
":  " + 
"0.001744415700689898" + 
":  " + 
"(b('dsvv') <= -1.8102807998657227) ? " + 
"0.20984344719490866" + 
":  " + 
"0.05549651854912512" + 
":  " + 
"(b('L8b5') <= 2790.5) ? " + 
"(b('L8b3') <= 695.0) ? " + 
"-0.09166165468243202" + 
":  " + 
"-0.011317370726327707" + 
":  " + 
"(b('L8b6med') <= 2051.75) ? " + 
"-0.026605716332109765" + 
":  " + 
"4.14958864573212e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 181.0) ? " + 
"(b('L8dt') <= 1357251.0) ? " + 
"(b('L8b6med') <= 2452.0) ? " + 
"0.03159015562131694" + 
":  " + 
"0.00685385188363444" + 
":  " + 
"(b('L8dt') <= 1555196.0) ? " + 
"0.0014111065086570666" + 
":  " + 
"-0.01579836360571607" + 
":  " + 
"(b('L8b2') <= 203.5) ? " + 
"(b('dgvv') <= -0.04385232925415039) ? " + 
"-0.004148798091098649" + 
":  " + 
"-0.06492385982955852" + 
":  " + 
"(b('sand') <= 80.5) ? " + 
"-3.300831180890455e-05" + 
":  " + 
"0.01451845682253972" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4653.0) ? " + 
"(b('L8b5') <= 4619.5) ? " + 
"(b('L8b4') <= 2644.5) ? " + 
"-7.572516118749354e-05" + 
":  " + 
"0.0037499854269403697" + 
":  " + 
"(b('ndvi') <= 4946.5) ? " + 
"-0.011773551827049557" + 
":  " + 
"-0.03334342224129684" + 
":  " + 
"(b('ndvi') <= 5908.5) ? " + 
"(b('L8b3') <= 1098.5) ? " + 
"0.03757110075671728" + 
":  " + 
"0.0036101708430039407" + 
":  " + 
"(b('L8dt') <= 471617.0) ? " + 
"0.012095079305547794" + 
":  " + 
"-0.014927872438916" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 3.8659508228302) ? " + 
"(b('dgvv') <= 3.8649492263793945) ? " + 
"(b('L8b2') <= 858.5) ? " + 
"0.0002406997176296162" + 
":  " + 
"-0.0012192259145690238" + 
":  " + 
"(b('ndvi_med') <= 2190.5) ? " + 
"-0.06668927706952646" + 
":  " + 
"0.009161036731027541" + 
":  " + 
"(b('L8b6') <= 3670.0) ? " + 
"(b('L8b5med') <= 3109.75) ? " + 
"0.005968956423799248" + 
":  " + 
"-0.012874259606972674" + 
":  " + 
"(b('lat') <= 41.369455337524414) ? " + 
"0.03220916757992249" + 
":  " + 
"-0.000476730996594937" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('sand') <= 14.5) ? " + 
"(b('ndvi') <= 5887.0) ? " + 
"(b('ndvi') <= 5295.5) ? " + 
"-0.006205771881187144" + 
":  " + 
"0.045621144255479626" + 
":  " + 
"(b('ndvi') <= 7169.0) ? " + 
"-0.07646884313412045" + 
":  " + 
"0.07576633005332445" + 
":  " + 
"(b('L8b11') <= 1242.5) ? " + 
"(b('sand') <= 16.5) ? " + 
"-0.040399702066780306" + 
":  " + 
"-0.0010367775695131357" + 
":  " + 
"(b('sand') <= 17.0) ? " + 
"0.012945616560814084" + 
":  " + 
"9.774220247900763e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 718.5) ? " + 
"(b('L8b4') <= 717.5) ? " + 
"(b('dsvv') <= 3.9012486934661865) ? " + 
"0.0006174480328248206" + 
":  " + 
"0.02216175674999453" + 
":  " + 
"(b('L8b2') <= 457.5) ? " + 
"-0.0014290671881057417" + 
":  " + 
"0.1028132992786094" + 
":  " + 
"(b('L8b4') <= 719.5) ? " + 
"(b('ndvi_med') <= 3679.25) ? " + 
"-0.08663896699837421" + 
":  " + 
"-0.02936915096282818" + 
":  " + 
"(b('L8b6med') <= 2385.5) ? " + 
"-0.003945038249157962" + 
":  " + 
"0.00014135523050230392" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 29.159395217895508) ? " + 
"(b('lat') <= -27.02739429473877) ? " + 
"(b('ndvi') <= 2370.5) ? " + 
"-0.029733989017643087" + 
":  " + 
"0.017973687743184096" + 
":  " + 
"(b('lat') <= 31.407100677490234) ? " + 
"0.004697337158029476" + 
":  " + 
"-7.864963604320958e-05" + 
":  " + 
"(b('ndvi') <= 2003.5) ? " + 
"(b('L8dt') <= 2073605.0) ? " + 
"0.002578305409306179" + 
":  " + 
"-0.05815780299462673" + 
":  " + 
"(b('dsvv') <= 0.5677003860473633) ? " + 
"0.019143869829505628" + 
":  " + 
"0.07677036755832709" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 770.5) ? " + 
"(b('L8b2med') <= 502.5) ? " + 
"(b('L8b4') <= 1051.0) ? " + 
"0.0013676959333478512" + 
":  " + 
"-0.0947000417869607" + 
":  " + 
"(b('L8b7med') <= 1889.0) ? " + 
"-0.009112048777845907" + 
":  " + 
"0.0003890300202059247" + 
":  " + 
"(b('L8b4') <= 702.0) ? " + 
"(b('L8b3') <= 787.5) ? " + 
"0.03598695835978815" + 
":  " + 
"-0.005636074262357067" + 
":  " + 
"(b('lon') <= 6.412564992904663) ? " + 
"0.000535900563334011" + 
":  " + 
"-0.0020915106921120525" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2741.5) ? " + 
"(b('sand') <= 38.5) ? " + 
"(b('lat') <= 34.3631649017334) ? " + 
"-0.030314216451070644" + 
":  " + 
"-0.001116121395577962" + 
":  " + 
"(b('L8b5med') <= 2449.375) ? " + 
"-0.0005530691764423293" + 
":  " + 
"0.0037287965203966775" + 
":  " + 
"(b('L8b5') <= 2793.5) ? " + 
"(b('L8b3') <= 701.5) ? " + 
"-0.0363344538403845" + 
":  " + 
"-0.004633883481870847" + 
":  " + 
"(b('L8b5') <= 2804.5) ? " + 
"0.013701633825887129" + 
":  " + 
"-0.00027988026352406806" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1381.5) ? " + 
"(b('L8b3') <= 1129.0) ? " + 
"(b('L8b3') <= 979.5) ? " + 
"-0.0003100631561037176" + 
":  " + 
"0.0028374602055836807" + 
":  " + 
"(b('L8b7med') <= 1736.0) ? " + 
"-0.008234809319189886" + 
":  " + 
"0.02070583246285982" + 
":  " + 
"(b('L8b2') <= 590.0) ? " + 
"(b('L8b4') <= 1478.0) ? " + 
"-0.00502844435209074" + 
":  " + 
"0.03692141793394447" + 
":  " + 
"(b('L8b3') <= 1241.5) ? " + 
"-0.00367715010158267" + 
":  " + 
"0.0002365525828842718" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1623.0) ? " + 
"(b('L8b4') <= 1745.5) ? " + 
"(b('L8b11') <= 2343.0) ? " + 
"0.0007210359415281368" + 
":  " + 
"0.02329806891475353" + 
":  " + 
"(b('dsvv') <= 2.588033676147461) ? " + 
"-0.031179241028432086" + 
":  " + 
"0.04304599519714585" + 
":  " + 
"(b('L8b11') <= 1596.0) ? " + 
"(b('L8b11') <= 1391.5) ? " + 
"0.00106178745273333" + 
":  " + 
"-0.007058569410060194" + 
":  " + 
"(b('L8b11') <= 1602.5) ? " + 
"0.0313888478079325" + 
":  " + 
"0.00014843855812644822" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3660.0) ? " + 
"(b('L8b5med') <= 3243.0) ? " + 
"(b('L8b4') <= 1665.0) ? " + 
"0.0004403611543906099" + 
":  " + 
"-0.0023007056176185263" + 
":  " + 
"(b('L8b5med') <= 3285.0) ? " + 
"0.02478104787393994" + 
":  " + 
"0.001647979360438833" + 
":  " + 
"(b('L8b2') <= 487.5) ? " + 
"(b('ndvi') <= 3663.5) ? " + 
"0.021299109264980774" + 
":  " + 
"-0.002822626871192935" + 
":  " + 
"(b('L8b2') <= 525.5) ? " + 
"-0.0313836749207325" + 
":  " + 
"-0.0023114000641159867" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -120.6328010559082) ? " + 
"(b('dsvv') <= 0.8429775238037109) ? " + 
"(b('lon') <= -120.79582977294922) ? " + 
"0.0016115850619267042" + 
":  " + 
"0.022135714855436618" + 
":  " + 
"(b('ndvi_med') <= 1596.5) ? " + 
"0.007461472390006235" + 
":  " + 
"-0.02423808562910251" + 
":  " + 
"(b('L8b6') <= 2754.5) ? " + 
"(b('L8b2med') <= 841.75) ? " + 
"0.0010824805884638478" + 
":  " + 
"-0.007316030832472329" + 
":  " + 
"(b('L8b11') <= 1678.5) ? " + 
"-0.0077831439172141755" + 
":  " + 
"-0.00025140675151569047" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1442.5) ? " + 
"(b('L8b11') <= 1440.5) ? " + 
"(b('lon') <= -88.12430191040039) ? " + 
"-0.005435195702113486" + 
":  " + 
"0.0009785555696225458" + 
":  " + 
"(b('L8b2med') <= 397.5) ? " + 
"-0.0900255271613036" + 
":  " + 
"-0.024217440700025867" + 
":  " + 
"(b('L8b4') <= 835.5) ? " + 
"(b('L8b3') <= 844.0) ? " + 
"0.002731263355262822" + 
":  " + 
"0.020568453512489083" + 
":  " + 
"(b('L8b11') <= 1469.5) ? " + 
"0.020965514379309175" + 
":  " + 
"-0.0003684853562066783" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1206.5) ? " + 
"(b('ndvi') <= 2327.5) ? " + 
"(b('ndvi') <= 1250.5) ? " + 
"0.0010035005793089045" + 
":  " + 
"0.017296497354528855" + 
":  " + 
"-0.1514906694995238" + 
":  " + 
"(b('ndvi') <= 1636.5) ? " + 
"(b('ndvi_med') <= 3614.5) ? " + 
"-0.001362619310685797" + 
":  " + 
"0.05288887596632302" + 
":  " + 
"(b('lon') <= -121.20288467407227) ? " + 
"0.01691274122337964" + 
":  " + 
"0.00015228171235554008" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2974.5) ? " + 
"(b('L8b4') <= 1825.5) ? " + 
"(b('L8b3') <= 1398.5) ? " + 
"-2.7100697954162274e-05" + 
":  " + 
"0.0174314596150997" + 
":  " + 
"(b('sand') <= 38.5) ? " + 
"0.013062609677627176" + 
":  " + 
"-0.004881713290480156" + 
":  " + 
"(b('L8b11') <= 3007.0) ? " + 
"(b('sand') <= 40.5) ? " + 
"0.040139737433999914" + 
":  " + 
"0.004184209142853127" + 
":  " + 
"(b('L8b5med') <= 2828.0) ? " + 
"-0.0056910415435439485" + 
":  " + 
"0.0019533566343812115" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 728.5) ? " + 
"(b('L8b6') <= 2487.0) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"0.0014983471217875442" + 
":  " + 
"-0.015436994169320721" + 
":  " + 
"(b('L8b5med') <= 2738.0) ? " + 
"-0.0009243920339352845" + 
":  " + 
"-0.014499870240752069" + 
":  " + 
"(b('L8b3') <= 735.5) ? " + 
"(b('lat') <= 33.206199645996094) ? " + 
"0.07173282096066066" + 
":  " + 
"0.006925765214448181" + 
":  " + 
"(b('L8b3') <= 738.5) ? " + 
"-0.018842210507936222" + 
":  " + 
"0.00018921308523695568" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1242.5) ? " + 
"(b('L8b6med') <= 2452.0) ? " + 
"(b('dgvv') <= 2.655318260192871) ? " + 
"0.004928139493411653" + 
":  " + 
"-0.021399212013778545" + 
":  " + 
"(b('dgvv') <= 0.5912704467773438) ? " + 
"-0.011737044706687495" + 
":  " + 
"0.0028016176134598976" + 
":  " + 
"(b('L8b4') <= 729.5) ? " + 
"(b('L8b6med') <= 3101.75) ? " + 
"0.0019348291014469516" + 
":  " + 
"0.030384413666299324" + 
":  " + 
"(b('L8b11') <= 1348.5) ? " + 
"-0.008047268050281166" + 
":  " + 
"2.569644302756129e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1681.0) ? " + 
"(b('L8b5') <= 1677.5) ? " + 
"(b('lat') <= 37.97694396972656) ? " + 
"-0.012787777070027002" + 
":  " + 
"0.0048024140379858945" + 
":  " + 
"(b('L8b6med') <= 2276.375) ? " + 
"-0.059564263767785085" + 
":  " + 
"0.08485128098639148" + 
":  " + 
"(b('L8b6med') <= 2069.625) ? " + 
"(b('dsvv') <= 1.749596118927002) ? " + 
"-0.005022994661411765" + 
":  " + 
"-0.03165051507549503" + 
":  " + 
"(b('L8b5med') <= 1718.75) ? " + 
"0.015933042396524447" + 
":  " + 
"-4.3640798465263514e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2002.0) ? " + 
"(b('L8b6') <= 3347.5) ? " + 
"(b('L8b5') <= 2347.5) ? " + 
"-0.0033972167442880377" + 
":  " + 
"0.01611859674204733" + 
":  " + 
"(b('L8b4') <= 1383.0) ? " + 
"-0.10131571742834573" + 
":  " + 
"-0.032032951198352304" + 
":  " + 
"(b('L8b5med') <= 2009.5) ? " + 
"(b('dsvv') <= 1.0942745208740234) ? " + 
"-0.004230536234968388" + 
":  " + 
"0.0830891597828731" + 
":  " + 
"(b('lon') <= -105.83941650390625) ? " + 
"0.0012256396927357422" + 
":  " + 
"-0.00022533433483181185" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3218711.5) ? " + 
"(b('L8dt') <= 3089966.0) ? " + 
"(b('L8dt') <= 3089951.5) ? " + 
"-8.11324878985995e-05" + 
":  " + 
"0.04930249995506472" + 
":  " + 
"(b('L8dt') <= 3109071.0) ? " + 
"-0.05843695896085965" + 
":  " + 
"-0.004912110889839146" + 
":  " + 
"(b('L8b5med') <= 3022.0) ? " + 
"(b('lat') <= 38.31925010681152) ? " + 
"-0.024567762870821165" + 
":  " + 
"0.0004028611858585951" + 
":  " + 
"(b('L8b4') <= 2437.5) ? " + 
"0.009707401420737588" + 
":  " + 
"-0.018216642848081926" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1708.5) ? " + 
"(b('L8b3') <= 1675.0) ? " + 
"(b('L8b11') <= 3444.0) ? " + 
"-0.00012471505714697686" + 
":  " + 
"0.00774129603572949" + 
":  " + 
"(b('crops') <= 81.73051071166992) ? " + 
"-0.005987935332744469" + 
":  " + 
"-0.03291011376427087" + 
":  " + 
"(b('L8b2') <= 1036.5) ? " + 
"(b('L8b2med') <= 886.0) ? " + 
"0.032648798947386655" + 
":  " + 
"-0.012518717714288885" + 
":  " + 
"(b('L8dt') <= 2526521.5) ? " + 
"0.0019643465219320107" + 
":  " + 
"-0.014426852350502346" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 146.23104858398438) ? " + 
"(b('lat') <= -28.00918483734131) ? " + 
"(b('ndvi') <= 1832.5) ? " + 
"-0.02225120002405667" + 
":  " + 
"0.007676618376791219" + 
":  " + 
"(b('lat') <= 31.407100677490234) ? " + 
"0.004811095442007417" + 
":  " + 
"-7.797285840242505e-05" + 
":  " + 
"(b('dgvv') <= 1.0272974967956543) ? " + 
"(b('L8b5') <= 2038.0) ? " + 
"-0.04857390414980772" + 
":  " + 
"0.008918745264051748" + 
":  " + 
"(b('dgvv') <= 3.354325771331787) ? " + 
"0.08492390124914735" + 
":  " + 
"0.003865438177535632" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 179923.5) ? " + 
"(b('L8b7med') <= 1520.0) ? " + 
"(b('L8b6') <= 3386.5) ? " + 
"-0.0054159513106326685" + 
":  " + 
"-0.057093870925450936" + 
":  " + 
"(b('dgvv') <= -0.04741048812866211) ? " + 
"0.0022672458957089486" + 
":  " + 
"-0.002883567517064764" + 
":  " + 
"(b('L8dt') <= 179930.5) ? " + 
"(b('dsvv') <= 0.8529796600341797) ? " + 
"-0.0032642717637346506" + 
":  " + 
"0.08764077433353884" + 
":  " + 
"(b('L8dt') <= 179950.5) ? " + 
"-0.014550052444683752" + 
":  " + 
"0.00019419932003387707" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 802.5) ? " + 
"(b('L8b4') <= 935.0) ? " + 
"(b('L8b2') <= 401.5) ? " + 
"0.002027373742623538" + 
":  " + 
"0.04122724487422068" + 
":  " + 
"(b('L8b11') <= 1803.0) ? " + 
"-0.03789812838554886" + 
":  " + 
"-0.11146500568374482" + 
":  " + 
"(b('L8dt') <= 1279.0) ? " + 
"(b('dgvv') <= 1.2217884063720703) ? " + 
"-0.021739108848389786" + 
":  " + 
"-0.15280388604625136" + 
":  " + 
"(b('L8dt') <= 1280.5) ? " + 
"0.13368440498681694" + 
":  " + 
"-2.3325853748732287e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5229.5) ? " + 
"(b('ndvi') <= 5018.5) ? " + 
"(b('ndvi') <= 4966.5) ? " + 
"6.809554921671691e-05" + 
":  " + 
"-0.011398636281902413" + 
":  " + 
"(b('L8b3') <= 977.5) ? " + 
"0.003353052175257055" + 
":  " + 
"0.029106958368195567" + 
":  " + 
"(b('ndvi') <= 5724.0) ? " + 
"(b('L8b5') <= 3754.5) ? " + 
"-0.011048696711233465" + 
":  " + 
"0.012899964604013681" + 
":  " + 
"(b('L8b6') <= 1830.5) ? " + 
"-0.02322776284289802" + 
":  " + 
"0.003319018982149771" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1623.0) ? " + 
"(b('dgvv') <= -1.5321149826049805) ? " + 
"(b('lat') <= 40.992300033569336) ? " + 
"-0.02545854036627264" + 
":  " + 
"0.0012069774765512136" + 
":  " + 
"(b('dsvv') <= -1.5277423858642578) ? " + 
"0.0954293625170568" + 
":  " + 
"0.0018620503353342602" + 
":  " + 
"(b('L8b11') <= 1524.5) ? " + 
"(b('L8b11') <= 1398.5) ? " + 
"0.0010070350538247952" + 
":  " + 
"-0.009885043548219551" + 
":  " + 
"(b('L8b6') <= 2373.5) ? " + 
"-0.006115697966283801" + 
":  " + 
"0.0004767322384269872" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3660.0) ? " + 
"(b('L8b5') <= 3655.5) ? " + 
"(b('L8b5med') <= 3243.0) ? " + 
"-0.00015128838675078837" + 
":  " + 
"0.002490326108363913" + 
":  " + 
"(b('L8dt') <= 1384956.5) ? " + 
"0.02375833304998674" + 
":  " + 
"-0.010007469850336573" + 
":  " + 
"(b('lon') <= -5.50570011138916) ? " + 
"(b('dgvv') <= 1.3502721786499023) ? " + 
"-0.012092643056188302" + 
":  " + 
"0.016039482054908783" + 
":  " + 
"(b('dsvv') <= 1.4992966651916504) ? " + 
"0.0028511355238781625" + 
":  " + 
"-0.013072435143704476" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 47.547691345214844) ? " + 
"(b('dsvv') <= 0.710634708404541) ? " + 
"(b('L8b6') <= 1147.0) ? " + 
"0.03317415537718878" + 
":  " + 
"-0.0004251419359327427" + 
":  " + 
"(b('lat') <= 38.48287391662598) ? " + 
"-0.0033417236599024955" + 
":  " + 
"0.006822325959613627" + 
":  " + 
"(b('dsvv') <= 0.6256508827209473) ? " + 
"(b('L8b6med') <= 3561.0) ? " + 
"-0.0009093189320371635" + 
":  " + 
"0.0030464845727540754" + 
":  " + 
"(b('dgvv') <= 0.6006307601928711) ? " + 
"-0.17441924504136902" + 
":  " + 
"-0.001967489068733672" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 3892.5) ? " + 
"(b('L8b11') <= 2907.5) ? " + 
"(b('L8b11') <= 2891.0) ? " + 
"6.634438220111497e-06" + 
":  " + 
"-0.0171659917945517" + 
":  " + 
"(b('sand') <= 39.5) ? " + 
"0.03642024719064134" + 
":  " + 
"0.003755486384919956" + 
":  " + 
"(b('L8b6') <= 3914.5) ? " + 
"(b('lat') <= 41.365474700927734) ? " + 
"-0.0239035779292895" + 
":  " + 
"0.024128507937186745" + 
":  " + 
"(b('L8b6') <= 3918.0) ? " + 
"0.04737902885447555" + 
":  " + 
"-0.0007995032733400558" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3768.75) ? " + 
"(b('L8b5') <= 4370.5) ? " + 
"(b('L8b5') <= 4326.5) ? " + 
"-7.449181582331125e-06" + 
":  " + 
"0.021372622596874488" + 
":  " + 
"(b('L8dt') <= 993365.0) ? " + 
"-0.00041049934238282136" + 
":  " + 
"-0.0166374081975086" + 
":  " + 
"(b('ndvi') <= 820.0) ? " + 
"(b('ndvi') <= 811.0) ? " + 
"0.013814482462585627" + 
":  " + 
"0.07077607620592961" + 
":  " + 
"(b('dsvv') <= 1.6493310928344727) ? " + 
"0.0032908566504273305" + 
":  " + 
"-0.02143386106380614" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 946.5) ? " + 
"(b('L8b3') <= 882.5) ? " + 
"(b('L8b3') <= 875.5) ? " + 
"0.00018713007472791136" + 
":  " + 
"-0.03255023827202329" + 
":  " + 
"(b('L8b5') <= 3851.5) ? " + 
"0.015447707037660696" + 
":  " + 
"-0.008214965908623013" + 
":  " + 
"(b('lat') <= 48.30685043334961) ? " + 
"(b('L8b3') <= 910.5) ? " + 
"-0.0031917776292672783" + 
":  " + 
"0.0006112948873916358" + 
":  " + 
"(b('sand') <= 78.5) ? " + 
"-0.006623372724309505" + 
":  " + 
"0.018596713143497406" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1259.5) ? " + 
"(b('L8b3') <= 982.5) ? " + 
"(b('L8b6') <= 3369.5) ? " + 
"0.0001957393824218976" + 
":  " + 
"-0.012013270376736404" + 
":  " + 
"(b('ndvi_med') <= 1775.0) ? " + 
"-0.005745128447516327" + 
":  " + 
"0.009140435305621687" + 
":  " + 
"(b('lat') <= 48.30685043334961) ? " + 
"(b('lat') <= 47.354129791259766) ? " + 
"-0.0003677743185988209" + 
":  " + 
"0.02213892049737302" + 
":  " + 
"(b('L8b5') <= 3590.5) ? " + 
"-0.012134409129228594" + 
":  " + 
"0.030136916877397342" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3379.5) ? " + 
"(b('L8b5') <= 3336.5) ? " + 
"(b('L8b4') <= 2020.0) ? " + 
"0.00044297111165569696" + 
":  " + 
"-0.004479944834891178" + 
":  " + 
"(b('L8b2med') <= 396.5) ? " + 
"0.062385561400475714" + 
":  " + 
"0.008314831364293881" + 
":  " + 
"(b('L8b3') <= 1398.5) ? " + 
"(b('dsvv') <= 2.2995166778564453) ? " + 
"-0.0021929054616314594" + 
":  " + 
"-0.015015629859530737" + 
":  " + 
"(b('L8b11') <= 2231.5) ? " + 
"0.07836525991747756" + 
":  " + 
"0.0025556140969101794" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 667.5) ? " + 
"(b('lat') <= 35.81930160522461) ? " + 
"(b('L8dt') <= 2503664.0) ? " + 
"-0.01652681161244538" + 
":  " + 
"0.05978854160891199" + 
":  " + 
"(b('dgvv') <= 1.8975815773010254) ? " + 
"-0.001793504277631929" + 
":  " + 
"0.007799227269768453" + 
":  " + 
"(b('L8b2') <= 460.5) ? " + 
"(b('L8b2') <= 459.5) ? " + 
"0.001992215084115113" + 
":  " + 
"0.08064404268381867" + 
":  " + 
"(b('L8b3') <= 712.5) ? " + 
"-0.013837222518253823" + 
":  " + 
"-8.123087885610976e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3190.0) ? " + 
"(b('L8b5med') <= 3098.0) ? " + 
"(b('L8b4') <= 1835.5) ? " + 
"2.6852573011260324e-05" + 
":  " + 
"-0.005646005008284981" + 
":  " + 
"(b('lat') <= 55.90290069580078) ? " + 
"0.003654797054701347" + 
":  " + 
"0.03408411940886681" + 
":  " + 
"(b('L8b5') <= 3257.5) ? " + 
"(b('sand') <= 14.5) ? " + 
"-0.08332126758495242" + 
":  " + 
"-0.00816887571067479" + 
":  " + 
"(b('L8b5') <= 3263.5) ? " + 
"0.029801806540324893" + 
":  " + 
"-5.721607651960827e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1339.0) ? " + 
"(b('dgvv') <= -1.1807775497436523) ? " + 
"(b('L8b6') <= 3664.5) ? " + 
"0.02387305725108546" + 
":  " + 
"-0.006517637652934628" + 
":  " + 
"(b('L8b11') <= 1580.5) ? " + 
"-0.036434878531412106" + 
":  " + 
"0.0008782549796858246" + 
":  " + 
"(b('L8b3') <= 1567.5) ? " + 
"(b('L8b3') <= 1508.0) ? " + 
"-0.00016970527285856485" + 
":  " + 
"0.006747031761171198" + 
":  " + 
"(b('L8b5') <= 3308.5) ? " + 
"-0.010694048226563826" + 
":  " + 
"0.001931370806495633" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1681.0) ? " + 
"(b('L8b5') <= 1635.5) ? " + 
"(b('L8dt') <= 684098.5) ? " + 
"0.00605004740456474" + 
":  " + 
"-0.005049710078040559" + 
":  " + 
"(b('L8b5med') <= 2967.5) ? " + 
"0.011087482311793859" + 
":  " + 
"0.12788260270833735" + 
":  " + 
"(b('L8b6med') <= 2069.625) ? " + 
"(b('dsvv') <= -0.6148228645324707) ? " + 
"0.0044032296838971054" + 
":  " + 
"-0.014854334371897003" + 
":  " + 
"(b('L8b6') <= 1580.5) ? " + 
"0.011766597447747298" + 
":  " + 
"-7.003309268243176e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3379.5) ? " + 
"(b('L8b5') <= 3336.5) ? " + 
"(b('L8b4') <= 2020.0) ? " + 
"0.00038491406177793133" + 
":  " + 
"-0.0036095816965674185" + 
":  " + 
"(b('lon') <= -91.17789840698242) ? " + 
"-0.014862712438957825" + 
":  " + 
"0.015648697936458737" + 
":  " + 
"(b('L8b5') <= 3409.5) ? " + 
"(b('lat') <= 31.502599716186523) ? " + 
"0.063827086802655" + 
":  " + 
"-0.01327946465794269" + 
":  " + 
"(b('L8b5med') <= 3094.25) ? " + 
"0.004072283643142426" + 
":  " + 
"-0.0021684671132309466" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 5819576.0) ? " + 
"(b('L8dt') <= 5788343.5) ? " + 
"(b('L8b11') <= 1339.5) ? " + 
"-0.0014617957787966369" + 
":  " + 
"0.00015987653740280516" + 
":  " + 
"-0.07965810801265438" + 
":  " + 
"(b('L8b11') <= 1344.5) ? " + 
"(b('sand') <= 22.0) ? " + 
"0.07452211459424209" + 
":  " + 
"0.02679179491400835" + 
":  " + 
"(b('ndvi') <= 1568.5) ? " + 
"0.022499381004707872" + 
":  " + 
"-0.0009783389674090444" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1560.5) ? " + 
"(b('L8b4') <= 1154.5) ? " + 
"(b('L8b2') <= 533.5) ? " + 
"-0.0006149981603319844" + 
":  " + 
"0.020367187740504254" + 
":  " + 
"(b('L8b6') <= 2703.0) ? " + 
"-0.009083570212368355" + 
":  " + 
"0.0007062979870127698" + 
":  " + 
"(b('L8b4') <= 2347.5) ? " + 
"(b('L8b4') <= 2319.0) ? " + 
"-0.00020354792407836103" + 
":  " + 
"0.018485851151165543" + 
":  " + 
"(b('L8b5') <= 3310.5) ? " + 
"-0.06303026288777333" + 
":  " + 
"-0.004160428638025038" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 1206.5) ? " + 
"(b('ndvi') <= 2327.5) ? " + 
"(b('ndvi') <= 1258.0) ? " + 
"0.0010597758832077851" + 
":  " + 
"0.015401919190875983" + 
":  " + 
"-0.13948247574709627" + 
":  " + 
"(b('L8b2') <= 858.5) ? " + 
"(b('L8b4') <= 2091.0) ? " + 
"9.530030173717263e-05" + 
":  " + 
"0.024597101981061374" + 
":  " + 
"(b('dsvv') <= 3.177542209625244) ? " + 
"-0.002075538665446032" + 
":  " + 
"0.014552531849470519" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2673.75) ? " + 
"(b('ndvi') <= 1804.5) ? " + 
"(b('ndvi') <= 1636.5) ? " + 
"-0.0012690365045631244" + 
":  " + 
"0.017970415114432533" + 
":  " + 
"(b('ndvi') <= 1958.0) ? " + 
"-0.010363659469433826" + 
":  " + 
"-0.0009316523957497432" + 
":  " + 
"(b('L8b6med') <= 2700.0) ? " + 
"(b('L8b6') <= 3235.0) ? " + 
"0.0072929071822530845" + 
":  " + 
"0.061686567084542905" + 
":  " + 
"(b('ndvi') <= 6890.0) ? " + 
"8.077568985206458e-05" + 
":  " + 
"0.021726407782790867" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4653.0) ? " + 
"(b('L8b5') <= 4612.5) ? " + 
"(b('ndvi_med') <= 5674.5) ? " + 
"2.3072897778783348e-05" + 
":  " + 
"-0.011072248207237526" + 
":  " + 
"(b('dgvv') <= 2.7186412811279297) ? " + 
"-0.01635629133262204" + 
":  " + 
"0.030961565049812664" + 
":  " + 
"(b('ndvi') <= 5908.5) ? " + 
"(b('L8b7med') <= 2112.5) ? " + 
"0.04536355802842295" + 
":  " + 
"0.009372498273954704" + 
":  " + 
"(b('dsvv') <= -0.3896975517272949) ? " + 
"0.010039038671072744" + 
":  " + 
"-0.012172000912335411" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 29.159395217895508) ? " + 
"(b('lon') <= 26.74935531616211) ? " + 
"(b('L8b5med') <= 1869.0) ? " + 
"-0.00660628216871538" + 
":  " + 
"0.00014253941051636018" + 
":  " + 
"(b('dsvv') <= 0.0020389556884765625) ? " + 
"0.003754969486336562" + 
":  " + 
"-0.010964795364751772" + 
":  " + 
"(b('ndvi') <= 2003.5) ? " + 
"(b('L8b6') <= 2019.0) ? " + 
"0.1291297585269581" + 
":  " + 
"-0.0014666401783715744" + 
":  " + 
"(b('dsvv') <= 0.5677003860473633) ? " + 
"0.017016729901211322" + 
":  " + 
"0.0653890051060061" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 7893108.0) ? " + 
"(b('L8b6') <= 653.5) ? " + 
"(b('dsvv') <= 0.7163405418395996) ? " + 
"0.013202522260710742" + 
":  " + 
"0.07649428202440664" + 
":  " + 
"(b('L8b5') <= 1320.5) ? " + 
"-0.009428420572196448" + 
":  " + 
"2.384340898034612e-06" + 
":  " + 
"(b('sand') <= 69.0) ? " + 
"(b('L8b2') <= 937.5) ? " + 
"0.02064405965075727" + 
":  " + 
"0.06275487515012237" + 
":  " + 
"(b('L8b7med') <= 2186.25) ? " + 
"0.0030024766865351855" + 
":  " + 
"-0.03339664441312985" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3518.0) ? " + 
"(b('L8b5') <= 3486.5) ? " + 
"(b('L8b5med') <= 3046.5) ? " + 
"-0.00039404031603123847" + 
":  " + 
"0.0015604198243326707" + 
":  " + 
"(b('L8b6med') <= 2459.5) ? " + 
"-0.042000034394613986" + 
":  " + 
"0.012526083756787368" + 
":  " + 
"(b('L8b5') <= 3519.5) ? " + 
"(b('ndvi') <= 3458.5) ? " + 
"-0.047276654554888865" + 
":  " + 
"0.020871393925210684" + 
":  " + 
"(b('L8b6') <= 2410.5) ? " + 
"0.005591664632648195" + 
":  " + 
"-0.0021220235773761007" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 817.5) ? " + 
"(b('L8b4') <= 924.5) ? " + 
"(b('L8b4') <= 921.5) ? " + 
"-0.00015228612977638626" + 
":  " + 
"0.04623119562196541" + 
":  " + 
"(b('ndvi_med') <= 4266.25) ? " + 
"-0.005788888144352503" + 
":  " + 
"-0.09926916755772987" + 
":  " + 
"(b('L8b4') <= 944.5) ? " + 
"(b('ndvi') <= 1256.5) ? " + 
"0.2582031443939499" + 
":  " + 
"0.0035512912638609086" + 
":  " + 
"(b('L8b11') <= 1646.5) ? " + 
"-0.005951861355387767" + 
":  " + 
"0.00024035774848799193" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2036.5) ? " + 
"(b('L8b6') <= 2831.5) ? " + 
"(b('L8b6med') <= 3713.75) ? " + 
"0.00046048401351280984" + 
":  " + 
"-0.0184810064054942" + 
":  " + 
"(b('L8b6') <= 2853.5) ? " + 
"0.05114143761151861" + 
":  " + 
"0.006751181278942611" + 
":  " + 
"(b('L8b5') <= 2037.5) ? " + 
"(b('L8b2med') <= 657.75) ? " + 
"-0.046556380234756785" + 
":  " + 
"-0.01793409332089103" + 
":  " + 
"(b('L8b3') <= 728.5) ? " + 
"-0.0021378716970582197" + 
":  " + 
"0.00018180558902871052" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2049.5) ? " + 
"(b('L8b6') <= 2042.5) ? " + 
"(b('ndvi') <= 6611.5) ? " + 
"0.001784662195172657" + 
":  " + 
"-0.024229305858449717" + 
":  " + 
"(b('L8b6med') <= 2413.0) ? " + 
"0.02039200169836371" + 
":  " + 
"0.06794682226748862" + 
":  " + 
"(b('L8b5') <= 1551.5) ? " + 
"(b('L8b2') <= 565.5) ? " + 
"-0.02469611824948976" + 
":  " + 
"0.003176820956473935" + 
":  " + 
"(b('L8b4') <= 491.0) ? " + 
"-0.06589780656109161" + 
":  " + 
"-2.239935269462781e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1681.0) ? " + 
"(b('L8b5') <= 1677.5) ? " + 
"(b('L8b4') <= 1072.5) ? " + 
"0.0032139626566667803" + 
":  " + 
"-0.023279888996070638" + 
":  " + 
"(b('dgvv') <= 0.7161188125610352) ? " + 
"0.01667649273443223" + 
":  " + 
"0.10824135570583193" + 
":  " + 
"(b('L8b5') <= 1683.0) ? " + 
"(b('L8dt') <= 734648.0) ? " + 
"-0.019584169171366003" + 
":  " + 
"-0.061541327462334726" + 
":  " + 
"(b('L8b6med') <= 2069.625) ? " + 
"-0.0075397602759306155" + 
":  " + 
"4.316878144226094e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2754.5) ? " + 
"(b('L8b11') <= 2108.5) ? " + 
"(b('L8b11') <= 2105.5) ? " + 
"0.0007365958059593041" + 
":  " + 
"0.043688113387981564" + 
":  " + 
"(b('dgvv') <= 0.19120025634765625) ? " + 
"-0.0022479536551097017" + 
":  " + 
"-0.020513290844723028" + 
":  " + 
"(b('L8b6') <= 2757.5) ? " + 
"(b('L8dt') <= 29937.0) ? " + 
"0.07388390423191461" + 
":  " + 
"-0.030480008973029504" + 
":  " + 
"(b('ndvi') <= 4423.5) ? " + 
"6.412665135599682e-05" + 
":  " + 
"-0.00616108481869658" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 3717016.5) ? " + 
"(b('L8dt') <= 3629242.5) ? " + 
"(b('L8dt') <= 3615282.5) ? " + 
"-5.1380673356033135e-05" + 
":  " + 
"0.03759389315607866" + 
":  " + 
"(b('lat') <= 43.6068000793457) ? " + 
"-0.04773609822204312" + 
":  " + 
"-0.010701937251558933" + 
":  " + 
"(b('lat') <= 37.76110076904297) ? " + 
"(b('L8b3') <= 734.5) ? " + 
"-0.057967714280627386" + 
":  " + 
"-0.004873899978865818" + 
":  " + 
"(b('crops') <= 39.166316986083984) ? " + 
"0.01720118722324105" + 
":  " + 
"0.0014628417756995071" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.521310806274414) ? " + 
"(b('dsvv') <= -1.4177565574645996) ? " + 
"(b('L8b2med') <= 418.5) ? " + 
"-0.1037811869294027" + 
":  " + 
"-0.007683107789518535" + 
":  " + 
"(b('L8b5') <= 2617.0) ? " + 
"-0.001958920202797011" + 
":  " + 
"0.005964602120207297" + 
":  " + 
"(b('lat') <= 35.787649154663086) ? " + 
"(b('L8b3') <= 914.0) ? " + 
"-0.020532835065434008" + 
":  " + 
"0.00037554122617190674" + 
":  " + 
"(b('lat') <= 36.09165954589844) ? " + 
"0.006796052012546912" + 
":  " + 
"-0.00010011904606470452" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3190.0) ? " + 
"(b('L8b5med') <= 3385.5) ? " + 
"(b('L8b5med') <= 3373.0) ? " + 
"6.958175467021079e-05" + 
":  " + 
"-0.04608874520518824" + 
":  " + 
"(b('ndvi') <= 1023.0) ? " + 
"-0.0351835042178365" + 
":  " + 
"0.012343574264693055" + 
":  " + 
"(b('L8b5') <= 3257.5) ? " + 
"(b('sand') <= 14.5) ? " + 
"-0.07518286143791843" + 
":  " + 
"-0.00738018573439233" + 
":  " + 
"(b('L8b4') <= 587.0) ? " + 
"0.12414876492307536" + 
":  " + 
"0.00018914098883404524" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -120.6328010559082) ? " + 
"(b('dgvv') <= 1.6138911247253418) ? " + 
"(b('ndvi') <= 1944.5) ? " + 
"-0.0002708770013769325" + 
":  " + 
"0.011951885121333168" + 
":  " + 
"(b('ndvi_med') <= 1596.5) ? " + 
"0.002209693119561175" + 
":  " + 
"-0.043452940615531954" + 
":  " + 
"(b('L8b3') <= 1420.5) ? " + 
"(b('L8b4') <= 1745.0) ? " + 
"-3.0344583203571664e-05" + 
":  " + 
"-0.005307825243225286" + 
":  " + 
"(b('L8b5') <= 2684.5) ? " + 
"0.012610353672561561" + 
":  " + 
"9.505992398958601e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1457.25) ? " + 
"(b('L8b4') <= 937.5) ? " + 
"(b('L8b2') <= 532.5) ? " + 
"-0.0012740034307047816" + 
":  " + 
"-0.025233210841875322" + 
":  " + 
"(b('L8b4') <= 944.5) ? " + 
"0.06512941667403245" + 
":  " + 
"0.007245579089771538" + 
":  " + 
"(b('L8b11') <= 1462.5) ? " + 
"(b('L8b2') <= 438.5) ? " + 
"0.012046781569838556" + 
":  " + 
"0.08113054890110166" + 
":  " + 
"(b('L8b4') <= 835.5) ? " + 
"0.00323472846199102" + 
":  " + 
"-0.0002753358487008139" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3425.75) ? " + 
"(b('L8b6') <= 2847.5) ? " + 
"(b('L8b3') <= 1045.5) ? " + 
"0.00021558662020442306" + 
":  " + 
"0.005705772431590662" + 
":  " + 
"(b('L8b11') <= 1678.5) ? " + 
"-0.011692518660137452" + 
":  " + 
"-0.0012471087317954695" + 
":  " + 
"(b('dsvv') <= 6.627758979797363) ? " + 
"(b('L8b6') <= 2436.5) ? " + 
"-0.006390278505612434" + 
":  " + 
"0.0011525324820355325" + 
":  " + 
"-0.14225873441553144" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2215.5) ? " + 
"(b('L8b6') <= 2181.0) ? " + 
"(b('L8b11') <= 1819.0) ? " + 
"0.00045248848564361763" + 
":  " + 
"-0.037059630115038274" + 
":  " + 
"(b('L8b5') <= 2817.5) ? " + 
"0.004886663207633132" + 
":  " + 
"0.03384042157489579" + 
":  " + 
"(b('L8b11') <= 1110.0) ? " + 
"(b('L8b6med') <= 2746.5) ? " + 
"0.08423630130596431" + 
":  " + 
"0.02857077263698571" + 
":  " + 
"(b('L8b11') <= 1228.5) ? " + 
"-0.014442763077820995" + 
":  " + 
"-4.7340087809785936e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 1623.0) ? " + 
"(b('L8b4') <= 1745.5) ? " + 
"(b('L8b11') <= 2343.0) ? " + 
"0.000619155288025807" + 
":  " + 
"0.020793261313811325" + 
":  " + 
"(b('L8b6') <= 4100.0) ? " + 
"-0.03055953939208339" + 
":  " + 
"0.006857668244653445" + 
":  " + 
"(b('L8b11') <= 1524.5) ? " + 
"(b('L8b6') <= 2407.5) ? " + 
"-0.00035221810313923625" + 
":  " + 
"-0.012017071926118436" + 
":  " + 
"(b('L8b6') <= 2373.5) ? " + 
"-0.0053517611330553385" + 
":  " + 
"0.0004119172712636904" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1259.5) ? " + 
"(b('L8b3') <= 1044.5) ? " + 
"(b('L8b4') <= 1246.5) ? " + 
"-5.890897294533169e-05" + 
":  " + 
"0.020151059565318798" + 
":  " + 
"(b('ndvi') <= 2088.5) ? " + 
"-0.00905122211806016" + 
":  " + 
"0.014020856354506178" + 
":  " + 
"(b('L8b4') <= 1268.5) ? " + 
"(b('lon') <= 15.567659854888916) ? " + 
"-0.018773826637721317" + 
":  " + 
"0.041007519207616125" + 
":  " + 
"(b('L8b2') <= 595.5) ? " + 
"0.007860098256549954" + 
":  " + 
"-0.000652943580913925" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1681.0) ? " + 
"(b('L8b5') <= 1635.5) ? " + 
"(b('L8dt') <= 684098.5) ? " + 
"0.005649866872796311" + 
":  " + 
"-0.0042191263834500435" + 
":  " + 
"(b('L8b5med') <= 2967.5) ? " + 
"0.009370914818572253" + 
":  " + 
"0.11370722102984063" + 
":  " + 
"(b('L8b5') <= 1683.0) ? " + 
"(b('L8dt') <= 734648.0) ? " + 
"-0.018438438291983425" + 
":  " + 
"-0.056199880753855284" + 
":  " + 
"(b('L8b5med') <= 1718.75) ? " + 
"0.012586836187152759" + 
":  " + 
"-0.00011831719892809226" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 713.5) ? " + 
"(b('L8b3') <= 764.5) ? " + 
"(b('dgvv') <= 1.7445263862609863) ? " + 
"-0.0011444732328347263" + 
":  " + 
"0.007366592401574974" + 
":  " + 
"(b('L8b5') <= 3321.5) ? " + 
"0.02889129615108253" + 
":  " + 
"-0.00020686873365263194" + 
":  " + 
"(b('L8b11') <= 1348.5) ? " + 
"(b('L8b6') <= 2412.5) ? " + 
"-0.0014021345075041051" + 
":  " + 
"-0.02585952821083281" + 
":  " + 
"(b('L8b6') <= 1852.5) ? " + 
"0.03032072955815461" + 
":  " + 
"-2.1598404642837008e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2673.75) ? " + 
"(b('L8b4') <= 1128.5) ? " + 
"(b('L8b4') <= 1092.0) ? " + 
"-0.00036912034086591163" + 
":  " + 
"0.018708920602972433" + 
":  " + 
"(b('L8b3') <= 1038.5) ? " + 
"-0.015193838520631777" + 
":  " + 
"0.00023505858829911584" + 
":  " + 
"(b('L8b6med') <= 2700.0) ? " + 
"(b('dgvv') <= -0.15908145904541016) ? " + 
"-0.004254871650165296" + 
":  " + 
"0.022371825730481267" + 
":  " + 
"(b('dgvv') <= 6.8929572105407715) ? " + 
"0.00010624026807811392" + 
":  " + 
"0.052460280142699864" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 29.159395217895508) ? " + 
"(b('lat') <= -27.02739429473877) ? " + 
"(b('ndvi') <= 2370.5) ? " + 
"-0.025457682677619616" + 
":  " + 
"0.016342884674250532" + 
":  " + 
"(b('lat') <= 31.407100677490234) ? " + 
"0.004338197855549821" + 
":  " + 
"-7.67371966605892e-05" + 
":  " + 
"(b('L8b4') <= 1049.5) ? " + 
"(b('dgvv') <= -0.22569608688354492) ? " + 
"-0.013926548458010665" + 
":  " + 
"0.05668464234479332" + 
":  " + 
"(b('L8b3') <= 929.0) ? " + 
"-0.023898700825141755" + 
":  " + 
"0.008778419470121155" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 2079724.5) ? " + 
"(b('L8dt') <= 2075358.0) ? " + 
"(b('dsvv') <= 5.5451555252075195) ? " + 
"-0.0001095635964848942" + 
":  " + 
"-0.015375754034918882" + 
":  " + 
"(b('L8b11') <= 1491.5) ? " + 
"-0.004928847206761082" + 
":  " + 
"-0.12273122807139941" + 
":  " + 
"(b('L8b7med') <= 2802.5) ? " + 
"(b('ndvi') <= 1876.5) ? " + 
"0.012059411895149317" + 
":  " + 
"1.5400447545905648e-05" + 
":  " + 
"(b('L8b4') <= 1264.0) ? " + 
"0.015628530961447815" + 
":  " + 
"-0.008835284664021564" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 65970.5) ? " + 
"(b('L8dt') <= 65445.0) ? " + 
"(b('L8b2') <= 263.5) ? " + 
"-0.05652447331608882" + 
":  " + 
"0.001026132291141159" + 
":  " + 
"(b('dgvv') <= -0.4133310317993164) ? " + 
"0.05036205252348739" + 
":  " + 
"0.009197452359360049" + 
":  " + 
"(b('L8dt') <= 88173.5) ? " + 
"(b('L8dt') <= 88052.0) ? " + 
"-0.00544486246681921" + 
":  " + 
"-0.06662208336118519" + 
":  " + 
"(b('L8dt') <= 88764.0) ? " + 
"0.015723259637042467" + 
":  " + 
"2.808249799529015e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 621.5) ? " + 
"(b('L8b5med') <= 3285.0) ? " + 
"(b('L8b5med') <= 2838.0) ? " + 
"0.00031439793360814376" + 
":  " + 
"0.010523888569272392" + 
":  " + 
"(b('L8b3') <= 593.5) ? " + 
"-0.02269689293136551" + 
":  " + 
"-0.05078569287650048" + 
":  " + 
"(b('L8b4') <= 634.5) ? " + 
"(b('L8b7med') <= 1326.5) ? " + 
"-0.08958601137996791" + 
":  " + 
"-0.005563997870127291" + 
":  " + 
"(b('L8b4') <= 660.5) ? " + 
"0.006792399384638716" + 
":  " + 
"-0.00011827042957682964" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dsvv') <= 4.590449094772339) ? " + 
"(b('dsvv') <= 4.570148944854736) ? " + 
"(b('dsvv') <= 4.446338653564453) ? " + 
"-6.720784307306239e-06" + 
":  " + 
"-0.013591412585149803" + 
":  " + 
"(b('L8b2') <= 482.0) ? " + 
"-0.09491664629659395" + 
":  " + 
"-0.028612426497553245" + 
":  " + 
"(b('L8b4') <= 602.0) ? " + 
"(b('L8b11') <= 1307.5) ? " + 
"0.047473284082062195" + 
":  " + 
"0.12149629722864486" + 
":  " + 
"(b('ndvi_med') <= 3519.5) ? " + 
"0.00807682171079223" + 
":  " + 
"-0.02255964756601343" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= 6.695797920227051) ? " + 
"(b('dsvv') <= 6.653006553649902) ? " + 
"(b('L8b6') <= 1518.0) ? " + 
"-0.004033363962850969" + 
":  " + 
"4.319100517892097e-05" + 
":  " + 
"-0.1264142432017315" + 
":  " + 
"(b('L8b6med') <= 2739.5) ? " + 
"(b('L8b6') <= 3064.5) ? " + 
"-0.030994389434159685" + 
":  " + 
"0.004096206506558715" + 
":  " + 
"(b('L8b4') <= 876.5) ? " + 
"0.0963155118267083" + 
":  " + 
"0.04147588860598936" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 56.0489501953125) ? " + 
"(b('L8b2med') <= 392.5) ? " + 
"(b('L8b6') <= 2954.0) ? " + 
"0.0008673611441169799" + 
":  " + 
"0.020997980062586834" + 
":  " + 
"(b('L8b11') <= 1189.5) ? " + 
"-0.0024694353394494484" + 
":  " + 
"4.138318210890577e-05" + 
":  " + 
"(b('L8dt') <= 1098311.0) ? " + 
"(b('L8b11') <= 1374.5) ? " + 
"-0.00486867591270014" + 
":  " + 
"-0.055701266778547365" + 
":  " + 
"(b('L8dt') <= 1616670.5) ? " + 
"0.03290259409857034" + 
":  " + 
"-0.003969966177003335" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2049.5) ? " + 
"(b('L8b6') <= 2042.5) ? " + 
"(b('L8dt') <= 7113.5) ? " + 
"0.03802937546052938" + 
":  " + 
"0.0007795156104656026" + 
":  " + 
"(b('sand') <= 30.0) ? " + 
"0.0934966877513368" + 
":  " + 
"0.03149744341758666" + 
":  " + 
"(b('L8b5') <= 1551.5) ? " + 
"(b('L8b2') <= 565.5) ? " + 
"-0.022362632831590828" + 
":  " + 
"0.0036154418760521883" + 
":  " + 
"(b('L8b5') <= 1650.0) ? " + 
"0.013576579540576504" + 
":  " + 
"-0.00012181194459775271" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 2002.0) ? " + 
"(b('L8b6') <= 3347.5) ? " + 
"(b('L8b5') <= 2347.5) ? " + 
"-0.003102478319800807" + 
":  " + 
"0.01476972814128504" + 
":  " + 
"(b('L8b4') <= 1383.0) ? " + 
"-0.09011368368641559" + 
":  " + 
"-0.02560358042337046" + 
":  " + 
"(b('L8b5med') <= 2009.5) ? " + 
"(b('dsvv') <= 1.0942745208740234) ? " + 
"-0.0040719544722929175" + 
":  " + 
"0.07354876232776002" + 
":  " + 
"(b('L8b6') <= 2049.5) ? " + 
"0.002235801349884236" + 
":  " + 
"-9.108854109881714e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 5819576.0) ? " + 
"(b('L8dt') <= 5617199.0) ? " + 
"(b('L8dt') <= 5550033.0) ? " + 
"-2.5378667893886437e-05" + 
":  " + 
"0.03392789754252302" + 
":  " + 
"(b('ndvi') <= 4192.5) ? " + 
"-0.00755564110896936" + 
":  " + 
"-0.06531146492724234" + 
":  " + 
"(b('L8b11') <= 1344.5) ? " + 
"(b('L8b6') <= 2043.0) ? " + 
"0.06675578875491124" + 
":  " + 
"0.025381367694461456" + 
":  " + 
"(b('L8b2med') <= 410.0) ? " + 
"-0.05149430128557244" + 
":  " + 
"0.003600272914659538" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 952.0) ? " + 
"0.05399619885671876" + 
":  " + 
"(b('L8b3') <= 452.5) ? " + 
"(b('L8b6') <= 1745.5) ? " + 
"-0.003075855974600659" + 
":  " + 
"-0.04577534853465918" + 
":  " + 
"(b('L8b3') <= 516.5) ? " + 
"0.008102196435114816" + 
":  " + 
"-4.394756404718587e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2904.5) ? " + 
"(b('L8b11') <= 2889.5) ? " + 
"(b('L8b6') <= 4272.5) ? " + 
"-4.45243297064434e-05" + 
":  " + 
"-0.021672404346259014" + 
":  " + 
"(b('lon') <= -5.406574964523315) ? " + 
"0.002590157247405469" + 
":  " + 
"-0.02504107405816332" + 
":  " + 
"(b('L8b11') <= 2914.5) ? " + 
"(b('ndvi') <= 1258.5) ? " + 
"0.03962833096080653" + 
":  " + 
"0.004177834889753111" + 
":  " + 
"(b('L8b2') <= 935.5) ? " + 
"0.003669597843368646" + 
":  " + 
"-0.001284074635759726" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 1708.5) ? " + 
"(b('L8b3') <= 1675.0) ? " + 
"(b('L8b11') <= 3444.0) ? " + 
"-0.00011479217281724082" + 
":  " + 
"0.006669466362542702" + 
":  " + 
"(b('dgvv') <= 0.761044979095459) ? " + 
"-0.004906165879238943" + 
":  " + 
"-0.026908452686933516" + 
":  " + 
"(b('L8b2') <= 1036.5) ? " + 
"(b('dsvv') <= 1.175886631011963) ? " + 
"0.010526060885030317" + 
":  " + 
"0.07118385639785604" + 
":  " + 
"(b('dgvv') <= 1.5809388160705566) ? " + 
"0.0018336846245657328" + 
":  " + 
"-0.012664114336499022" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 47.547691345214844) ? " + 
"(b('L8b6') <= 3513.5) ? " + 
"(b('L8b6med') <= 3506.25) ? " + 
"0.0004912927673239333" + 
":  " + 
"0.00870793210236478" + 
":  " + 
"(b('lat') <= 41.75318908691406) ? " + 
"-0.0004603459953462203" + 
":  " + 
"-0.012843553294788423" + 
":  " + 
"(b('dsvv') <= 0.6497306823730469) ? " + 
"(b('L8b7med') <= 2543.0) ? " + 
"-0.001037330446378444" + 
":  " + 
"0.0025333548889416055" + 
":  " + 
"(b('lat') <= 37.1744499206543) ? " + 
"0.00956916965834834" + 
":  " + 
"-0.0026493538681425827" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1646.5) ? " + 
"(b('L8b6') <= 1677.5) ? " + 
"(b('L8b3') <= 407.5) ? " + 
"-0.0018187031834991385" + 
":  " + 
"0.03894703617608373" + 
":  " + 
"(b('L8b2') <= 711.5) ? " + 
"-0.004021246936456014" + 
":  " + 
"0.0003556774147709447" + 
":  " + 
"(b('ndvi') <= 1810.0) ? " + 
"(b('L8b2') <= 477.5) ? " + 
"0.020271246834490227" + 
":  " + 
"0.002898742459676887" + 
":  " + 
"(b('ndvi') <= 1954.5) ? " + 
"-0.004894825278804496" + 
":  " + 
"0.00029003649374227767" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 675.5) ? " + 
"(b('L8b3') <= 674.5) ? " + 
"(b('lat') <= 35.81930160522461) ? " + 
"-0.012366485219281421" + 
":  " + 
"4.054101732373368e-05" + 
":  " + 
"(b('L8dt') <= 709801.0) ? " + 
"-0.06371901626672392" + 
":  " + 
"0.027349448427721978" + 
":  " + 
"(b('L8b3') <= 676.5) ? " + 
"(b('ndvi') <= 4161.5) ? " + 
"0.055018840554068735" + 
":  " + 
"0.007456567033310247" + 
":  " + 
"(b('L8b4') <= 557.0) ? " + 
"0.03571565239373431" + 
":  " + 
"6.581514438868436e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 1664.5) ? " + 
"(b('ndvi_med') <= 1568.5) ? " + 
"(b('L8b3') <= 1220.5) ? " + 
"0.0016502151915487263" + 
":  " + 
"0.015103956341785074" + 
":  " + 
"(b('ndvi') <= 878.5) ? " + 
"-0.035377631015305326" + 
":  " + 
"-0.00017454063429385742" + 
":  " + 
"(b('L8b3') <= 1282.5) ? " + 
"(b('L8b5med') <= 3336.5) ? " + 
"-0.010781710657341159" + 
":  " + 
"0.022639586407564864" + 
":  " + 
"(b('lat') <= 53.43494987487793) ? " + 
"0.0003366005621896372" + 
":  " + 
"-0.05667630682070496" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1673.5) ? " + 
"(b('ndvi_med') <= 2433.0) ? " + 
"(b('ndvi') <= 1666.5) ? " + 
"-0.0010681322706332548" + 
":  " + 
"-0.024291461809069066" + 
":  " + 
"(b('L8b5') <= 2247.5) ? " + 
"-0.0016371227770803217" + 
":  " + 
"0.034490084482127245" + 
":  " + 
"(b('ndvi_med') <= 1633.0) ? " + 
"(b('L8b6med') <= 2554.25) ? " + 
"-0.01955936064262448" + 
":  " + 
"0.006373972162208877" + 
":  " + 
"(b('L8b6') <= 2753.5) ? " + 
"0.0010026119808970726" + 
":  " + 
"-0.0015313632592595155" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 770.5) ? " + 
"(b('L8b5') <= 3612.0) ? " + 
"(b('L8b3') <= 763.5) ? " + 
"-0.0001116470037461437" + 
":  " + 
"-0.011536991202071557" + 
":  " + 
"(b('L8b3') <= 749.0) ? " + 
"-0.004191032125535884" + 
":  " + 
"-0.0359586895567712" + 
":  " + 
"(b('L8b2') <= 415.5) ? " + 
"(b('L8b3') <= 865.0) ? " + 
"0.012819019961254364" + 
":  " + 
"-0.009689651817192849" + 
":  " + 
"(b('L8b2') <= 435.5) ? " + 
"-0.006845591788977548" + 
":  " + 
"0.0001894129630798729" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3660.0) ? " + 
"(b('L8b5') <= 3655.5) ? " + 
"(b('L8b2') <= 858.5) ? " + 
"0.0004320766270130694" + 
":  " + 
"-0.0013528886311118106" + 
":  " + 
"(b('L8dt') <= 455478.5) ? " + 
"-0.003568458509836177" + 
":  " + 
"0.025452954275712213" + 
":  " + 
"(b('L8b2') <= 487.5) ? " + 
"(b('ndvi') <= 3663.5) ? " + 
"0.01857148391753317" + 
":  " + 
"-0.0021633209425034263" + 
":  " + 
"(b('L8b3') <= 1244.0) ? " + 
"-0.009580976074407013" + 
":  " + 
"0.0009016858151627082" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1457.25) ? " + 
"(b('L8b4') <= 937.5) ? " + 
"(b('L8b2') <= 532.5) ? " + 
"-0.0013169584629714535" + 
":  " + 
"-0.022791850376477768" + 
":  " + 
"(b('L8b2med') <= 658.0) ? " + 
"0.02221234496400439" + 
":  " + 
"-0.004315306982207441" + 
":  " + 
"(b('L8b11') <= 1462.5) ? " + 
"(b('L8b2') <= 438.5) ? " + 
"0.010997335168068438" + 
":  " + 
"0.07165905260736542" + 
":  " + 
"(b('L8b4') <= 835.5) ? " + 
"0.0029504779779504654" + 
":  " + 
"-0.0002122709339667356" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 822.5) ? " + 
"(b('L8b2') <= 500.75) ? " + 
"(b('L8b2med') <= 502.5) ? " + 
"0.001474874852615619" + 
":  " + 
"-0.002305979638708696" + 
":  " + 
"(b('ndvi_med') <= 2682.0) ? " + 
"0.0006885157610564207" + 
":  " + 
"-0.011133381379069914" + 
":  " + 
"(b('L8b3') <= 835.5) ? " + 
"(b('L8b7med') <= 1820.0) ? " + 
"-0.0033924380061478186" + 
":  " + 
"0.019916129090408505" + 
":  " + 
"(b('L8b5') <= 1740.5) ? " + 
"-0.013775889291135452" + 
":  " + 
"0.00022060679782945716" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2142.5) ? " + 
"(b('L8b5') <= 2140.5) ? " + 
"(b('ndvi') <= 665.0) ? " + 
"0.0562429172603193" + 
":  " + 
"0.0008206097173106781" + 
":  " + 
"(b('L8b6med') <= 3061.5) ? " + 
"0.008804440616975868" + 
":  " + 
"0.06441729314056296" + 
":  " + 
"(b('L8b5') <= 2149.5) ? " + 
"(b('L8b4') <= 1500.0) ? " + 
"-0.008875434147363559" + 
":  " + 
"-0.042234801396607416" + 
":  " + 
"(b('L8b5') <= 2151.5) ? " + 
"0.036876642418938975" + 
":  " + 
"-0.00016388386945202825" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 872.5) ? " + 
"(b('L8b3') <= 860.5) ? " + 
"(b('L8b3') <= 856.75) ? " + 
"-0.0005233958032519092" + 
":  " + 
"0.022458643245980476" + 
":  " + 
"(b('L8b11') <= 1782.5) ? " + 
"-0.018383579392215955" + 
":  " + 
"0.003693518957888241" + 
":  " + 
"(b('L8b2') <= 487.5) ? " + 
"(b('L8b2') <= 448.0) ? " + 
"-0.003761867918449631" + 
":  " + 
"0.018036721262281678" + 
":  " + 
"(b('L8b6') <= 1880.0) ? " + 
"0.04184410654188534" + 
":  " + 
"3.61856231115658e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1681.0) ? " + 
"(b('L8b5') <= 1677.5) ? " + 
"(b('lat') <= 37.97694396972656) ? " + 
"-0.010190762747914566" + 
":  " + 
"0.004220074824397867" + 
":  " + 
"(b('L8b5med') <= 1838.0) ? " + 
"-0.0545856390663005" + 
":  " + 
"0.0679002293502829" + 
":  " + 
"(b('L8b5') <= 1693.5) ? " + 
"(b('L8dt') <= 919815.5) ? " + 
"0.0031825081325396773" + 
":  " + 
"-0.03735211773076745" + 
":  " + 
"(b('L8b11') <= 651.5) ? " + 
"0.026818943805759443" + 
":  " + 
"-7.150370459497417e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 7893108.0) ? " + 
"(b('lon') <= -120.6328010559082) ? " + 
"(b('dsvv') <= 0.8429775238037109) ? " + 
"0.004046132880130041" + 
":  " + 
"-0.0076614059600770765" + 
":  " + 
"(b('dsvv') <= 2.9765281677246094) ? " + 
"-0.0002519327443545246" + 
":  " + 
"0.0021289531388804747" + 
":  " + 
"(b('L8b2') <= 955.5) ? " + 
"(b('lon') <= 9.119600296020508) ? " + 
"0.0136353948237091" + 
":  " + 
"-0.00492910092103684" + 
":  " + 
"(b('L8dt') <= 8403318.0) ? " + 
"0.07273192320052993" + 
":  " + 
"0.04535769882375993" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3531.75) ? " + 
"(b('ndvi') <= 3879.5) ? " + 
"(b('ndvi_med') <= 3521.5) ? " + 
"-0.0004915116795316793" + 
":  " + 
"-0.025221984638973783" + 
":  " + 
"(b('crops') <= 66.14077377319336) ? " + 
"0.007924648274530021" + 
":  " + 
"-0.004870334282670136" + 
":  " + 
"(b('ndvi') <= 2824.0) ? " + 
"(b('crops') <= 59.452762603759766) ? " + 
"0.021985729888174047" + 
":  " + 
"0.0046230500653744264" + 
":  " + 
"(b('ndvi') <= 2871.0) ? " + 
"-0.031331931190554614" + 
":  " + 
"-0.0009130708648117488" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3020.0) ? " + 
"(b('dgvv') <= 2.909310817718506) ? " + 
"(b('dgvv') <= 2.8941993713378906) ? " + 
"-0.0005577608115577428" + 
":  " + 
"-0.05791326253019282" + 
":  " + 
"(b('lat') <= 43.965354919433594) ? " + 
"0.013430846693411325" + 
":  " + 
"-0.005072500326669445" + 
":  " + 
"(b('L8b5') <= 2872.0) ? " + 
"(b('L8b5') <= 2784.0) ? " + 
"0.0024736268909263327" + 
":  " + 
"0.016899571963050853" + 
":  " + 
"(b('L8dt') <= 1493004.5) ? " + 
"-0.0018161430422250257" + 
":  " + 
"0.003670858179396188" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 728.5) ? " + 
"(b('L8b6') <= 2487.0) ? " + 
"(b('L8b6') <= 2484.5) ? " + 
"0.0004713240601404138" + 
":  " + 
"0.06500768081367043" + 
":  " + 
"(b('sand') <= 24.5) ? " + 
"-0.022121403248198262" + 
":  " + 
"-0.0033634573942428157" + 
":  " + 
"(b('L8b3') <= 735.5) ? " + 
"(b('L8b6med') <= 3070.25) ? " + 
"0.015820473683203887" + 
":  " + 
"-0.024822020628740067" + 
":  " + 
"(b('L8b3') <= 738.5) ? " + 
"-0.016366100569966943" + 
":  " + 
"0.00017938708782326074" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1457.25) ? " + 
"(b('L8b4') <= 937.5) ? " + 
"(b('L8b2') <= 532.5) ? " + 
"-0.001229607376471797" + 
":  " + 
"-0.019923749154167" + 
":  " + 
"(b('L8b4') <= 944.5) ? " + 
"0.05176713131333296" + 
":  " + 
"0.005653464808613379" + 
":  " + 
"(b('L8b11') <= 1462.5) ? " + 
"(b('L8b6') <= 2309.5) ? " + 
"0.08846047786291497" + 
":  " + 
"0.015249900170460856" + 
":  " + 
"(b('L8b4') <= 835.5) ? " + 
"0.0028726244907074" + 
":  " + 
"-0.00020679473804808665" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 933.5) ? " + 
"(b('L8b2med') <= 850.0) ? " + 
"(b('L8b7med') <= 2456.0) ? " + 
"-0.0006589298295295003" + 
":  " + 
"0.007122620494889162" + 
":  " + 
"(b('L8b2') <= 658.5) ? " + 
"-0.012214099159459304" + 
":  " + 
"-0.12527669498419094" + 
":  " + 
"(b('L8b7med') <= 1895.5) ? " + 
"(b('L8b5') <= 2741.0) ? " + 
"0.010743180097308777" + 
":  " + 
"4.304061112951585e-05" + 
":  " + 
"(b('L8b4') <= 1168.5) ? " + 
"0.006567133873076708" + 
":  " + 
"-0.0008255826943979308" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2268.5) ? " + 
"(b('L8b6') <= 3723.5) ? " + 
"(b('L8b7med') <= 2880.75) ? " + 
"-0.0001114689870535446" + 
":  " + 
"-0.009439308266430961" + 
":  " + 
"(b('ndvi') <= 3743.5) ? " + 
"-0.033659954293036067" + 
":  " + 
"-0.0917014672693031" + 
":  " + 
"(b('L8b7med') <= 1864.0) ? " + 
"(b('L8b6med') <= 2727.0) ? " + 
"0.0012557210927630837" + 
":  " + 
"0.028710843179828506" + 
":  " + 
"(b('L8b11') <= 2290.5) ? " + 
"0.010279786108842224" + 
":  " + 
"-0.00025003788599958494" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.521310806274414) ? " + 
"(b('dsvv') <= -1.4177565574645996) ? " + 
"(b('L8b2med') <= 418.5) ? " + 
"-0.0926347934471056" + 
":  " + 
"-0.006234035009905395" + 
":  " + 
"(b('L8b2med') <= 418.5) ? " + 
"0.031555905836266385" + 
":  " + 
"0.002156680891788131" + 
":  " + 
"(b('lat') <= 35.787649154663086) ? " + 
"(b('L8b3') <= 914.0) ? " + 
"-0.017956761345097338" + 
":  " + 
"0.0005106260210499199" + 
":  " + 
"(b('lat') <= 36.09165954589844) ? " + 
"0.005877973082726541" + 
":  " + 
"-0.00010928122517117286" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3020.0) ? " + 
"(b('dgvv') <= 2.909310817718506) ? " + 
"(b('dgvv') <= 2.899557113647461) ? " + 
"-0.0005269678571256955" + 
":  " + 
"-0.058719800799226333" + 
":  " + 
"(b('lat') <= 43.965354919433594) ? " + 
"0.01212369821649193" + 
":  " + 
"-0.004597836304878036" + 
":  " + 
"(b('L8b5') <= 2962.5) ? " + 
"(b('L8b7med') <= 1326.5) ? " + 
"-0.03885436993364377" + 
":  " + 
"0.004587172889568581" + 
":  " + 
"(b('L8b5') <= 2972.5) ? " + 
"-0.025501484112468362" + 
":  " + 
"-0.0005600871390668918" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 3248.5) ? " + 
"(b('L8b7med') <= 3305.0) ? " + 
"(b('L8b2') <= 1081.5) ? " + 
"-0.00016758120469587292" + 
":  " + 
"0.00373001208128152" + 
":  " + 
"(b('dgvv') <= 1.4454612731933594) ? " + 
"-0.002845479867563605" + 
":  " + 
"-0.03131540825912838" + 
":  " + 
"(b('L8b11') <= 3251.5) ? " + 
"(b('L8dt') <= 583887.5) ? " + 
"0.0447596187902179" + 
":  " + 
"0.01163442796245169" + 
":  " + 
"(b('dsvv') <= -0.21075201034545898) ? " + 
"0.004841824282732193" + 
":  " + 
"-0.00234966272013476" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 3410.5) ? " + 
"(b('lat') <= 56.023799896240234) ? " + 
"(b('ndvi') <= 3396.0) ? " + 
"-0.00030554152174729136" + 
":  " + 
"-0.02370363995037005" + 
":  " + 
"(b('ndvi') <= 3336.0) ? " + 
"0.014889025085766831" + 
":  " + 
"-0.05593789765124724" + 
":  " + 
"(b('sand') <= 37.5) ? " + 
"(b('sand') <= 24.5) ? " + 
"-0.0033147670218366893" + 
":  " + 
"0.006457304108132687" + 
":  " + 
"(b('L8b4') <= 697.5) ? " + 
"0.00391546618005385" + 
":  " + 
"-0.003611779995642527" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 630.5) ? " + 
"(b('lon') <= 22.87677574157715) ? " + 
"(b('L8b6') <= 2163.5) ? " + 
"0.00039682965987639335" + 
":  " + 
"-0.00925144520390924" + 
":  " + 
"(b('L8b3') <= 626.5) ? " + 
"0.006222585404763879" + 
":  " + 
"-0.02881054848636572" + 
":  " + 
"(b('L8b2') <= 303.0) ? " + 
"(b('L8b2med') <= 485.5) ? " + 
"0.040669896115446275" + 
":  " + 
"-0.013941951223654258" + 
":  " + 
"(b('L8b4') <= 566.5) ? " + 
"-0.012578931603494967" + 
":  " + 
"0.00013616557705177927" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 6356.5) ? " + 
"(b('ndvi') <= 6186.5) ? " + 
"(b('ndvi_med') <= 5941.25) ? " + 
"-2.2898080216577524e-05" + 
":  " + 
"0.03688636858166581" + 
":  " + 
"(b('lat') <= 56.043649673461914) ? " + 
"-0.009578071370927178" + 
":  " + 
"-0.055776514564885006" + 
":  " + 
"(b('L8b7med') <= 1453.75) ? " + 
"(b('dgvv') <= 0.3106040954589844) ? " + 
"0.0014797164098963194" + 
":  " + 
"0.09035649693379742" + 
":  " + 
"(b('L8b4') <= 687.0) ? " + 
"-0.04296074256494175" + 
":  " + 
"0.004145907164811627" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 604.5) ? " + 
"(b('dgvv') <= -0.4428224563598633) ? " + 
"0.00560593745297288" + 
":  " + 
"0.06983417342659984" + 
":  " + 
"(b('L8b3') <= 461.5) ? " + 
"(b('L8b4') <= 531.5) ? " + 
"-0.0027556391061671435" + 
":  " + 
"-0.04024642236570162" + 
":  " + 
"(b('L8b3') <= 516.5) ? " + 
"0.006930427429844381" + 
":  " + 
"-3.4375666839797745e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 65970.5) ? " + 
"(b('L8dt') <= 65445.0) ? " + 
"(b('ndvi_med') <= 2223.0) ? " + 
"0.004901514671585771" + 
":  " + 
"-0.002870011721494654" + 
":  " + 
"(b('dgvv') <= -0.4133310317993164) ? " + 
"0.045155119465336735" + 
":  " + 
"0.009102965844778568" + 
":  " + 
"(b('L8dt') <= 65988.5) ? " + 
"(b('dgvv') <= -1.5066027641296387) ? " + 
"0.009153142906070876" + 
":  " + 
"-0.02645970429645536" + 
":  " + 
"(b('L8dt') <= 88170.0) ? " + 
"-0.004336519498245716" + 
":  " + 
"6.0252609023903627e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -9.844696760177612) ? " + 
"(b('ndvi_med') <= 1575.0) ? " + 
"0.02546181669164123" + 
":  " + 
"0.04995982383375933" + 
":  " + 
"(b('dsvv') <= -4.535989284515381) ? " + 
"(b('dsvv') <= -4.542520999908447) ? " + 
"-0.004890388553870953" + 
":  " + 
"-0.10217773825130072" + 
":  " + 
"(b('dsvv') <= -4.426722526550293) ? " + 
"0.01881215605467019" + 
":  " + 
"9.645707681972647e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi_med') <= 3418.5) ? " + 
"(b('dgvv') <= 6.695797920227051) ? " + 
"(b('dsvv') <= 6.653006553649902) ? " + 
"-0.00020581799964705544" + 
":  " + 
"-0.11740643278465339" + 
":  " + 
"(b('lon') <= -45.19076919555664) ? " + 
"0.08543699686405176" + 
":  " + 
"0.0347108792794834" + 
":  " + 
"(b('ndvi') <= 2824.0) ? " + 
"(b('crops') <= 46.46669578552246) ? " + 
"0.019479899472153377" + 
":  " + 
"0.0012285376868887944" + 
":  " + 
"(b('ndvi') <= 2881.0) ? " + 
"-0.03266955569762678" + 
":  " + 
"-3.2338650923641364e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 802.5) ? " + 
"(b('L8b4') <= 935.0) ? " + 
"(b('L8b5') <= 3358.5) ? " + 
"0.034897960213899785" + 
":  " + 
"-0.006331658695833765" + 
":  " + 
"(b('lat') <= 36.1617488861084) ? " + 
"-0.09849379892541432" + 
":  " + 
"-0.02918341727024945" + 
":  " + 
"(b('L8dt') <= 1279.0) ? " + 
"(b('L8b5') <= 3428.0) ? " + 
"-0.04410944278124919" + 
":  " + 
"0.07633260589962215" + 
":  " + 
"(b('L8dt') <= 1280.5) ? " + 
"0.12195161452252178" + 
":  " + 
"-3.0278626834178465e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lat') <= 34.521310806274414) ? " + 
"(b('L8dt') <= 3758159.5) ? " + 
"(b('ndvi') <= 2564.0) ? " + 
"-0.0009539373579226924" + 
":  " + 
"0.006721774831584078" + 
":  " + 
"(b('L8b3') <= 734.5) ? " + 
"-0.08619774317457392" + 
":  " + 
"-0.004987189668852011" + 
":  " + 
"(b('L8dt') <= 3738287.0) ? " + 
"(b('L8dt') <= 3544465.5) ? " + 
"-0.00017967425847363806" + 
":  " + 
"-0.01628990086211713" + 
":  " + 
"(b('lon') <= 9.173149585723877) ? " + 
"0.000744608979933729" + 
":  " + 
"0.01712356689259093" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 593.5) ? " + 
"(b('L8b5') <= 2961.0) ? " + 
"(b('L8b5') <= 2591.0) ? " + 
"-0.003998708366592765" + 
":  " + 
"0.01226053544453494" + 
":  " + 
"(b('ndvi') <= 5057.0) ? " + 
"-0.07187198272547111" + 
":  " + 
"-0.00510061656069441" + 
":  " + 
"(b('L8b3') <= 596.5) ? " + 
"(b('L8b7med') <= 1795.75) ? " + 
"0.010767452564411138" + 
":  " + 
"0.07569922507972261" + 
":  " + 
"(b('L8b3') <= 601.5) ? " + 
"-0.02236297279558678" + 
":  " + 
"6.403909419499081e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= 25.16578960418701) ? " + 
"(b('ndvi') <= 2597.5) ? " + 
"(b('lat') <= 50.95975112915039) ? " + 
"-0.0006737485402262944" + 
":  " + 
"0.01736151166024393" + 
":  " + 
"(b('L8b11') <= 1341.5) ? " + 
"-0.0025144810149120853" + 
":  " + 
"0.0019332921793000966" + 
":  " + 
"(b('L8b5') <= 2569.75) ? " + 
"(b('L8b7med') <= 1660.5) ? " + 
"0.014055565869461082" + 
":  " + 
"-0.001420295674356602" + 
":  " + 
"(b('L8b7med') <= 2118.25) ? " + 
"-0.007380120148599797" + 
":  " + 
"0.012781312558060968" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 2049.5) ? " + 
"(b('L8b6') <= 2042.5) ? " + 
"(b('L8b2med') <= 791.5) ? " + 
"0.0022663453305398263" + 
":  " + 
"-0.009675480416259789" + 
":  " + 
"(b('L8b6med') <= 2413.0) ? " + 
"0.014765465224714404" + 
":  " + 
"0.05468093523687012" + 
":  " + 
"(b('L8b4') <= 491.0) ? " + 
"(b('dsvv') <= 0.5571866035461426) ? " + 
"-0.0758445670113686" + 
":  " + 
"-0.00652079679741864" + 
":  " + 
"(b('L8b6') <= 2094.0) ? " + 
"-0.007654655527194151" + 
":  " + 
"-1.4083821205332385e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b4') <= 621.5) ? " + 
"(b('L8b5med') <= 3285.0) ? " + 
"(b('L8b3') <= 683.5) ? " + 
"0.0008408060203977597" + 
":  " + 
"0.011914591910698116" + 
":  " + 
"(b('dsvv') <= -1.0367403030395508) ? " + 
"-0.04736999251889969" + 
":  " + 
"-0.022372440814864735" + 
":  " + 
"(b('L8b4') <= 634.5) ? " + 
"(b('L8b7med') <= 1326.5) ? " + 
"-0.07534495453586734" + 
":  " + 
"-0.004674101273712628" + 
":  " + 
"(b('L8b4') <= 635.5) ? " + 
"0.037133180299099525" + 
":  " + 
"-1.9689457528419103e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -105.83941650390625) ? " + 
"(b('L8b4') <= 877.5) ? " + 
"(b('L8b3') <= 757.0) ? " + 
"0.0012962286637760562" + 
":  " + 
"0.019459982448240615" + 
":  " + 
"(b('L8b2') <= 508.5) ? " + 
"-0.017721036339011773" + 
":  " + 
"0.00046264487679078685" + 
":  " + 
"(b('lon') <= -103.57181930541992) ? " + 
"(b('dsvv') <= 1.1690940856933594) ? " + 
"-0.010204985986851527" + 
":  " + 
"0.01132705094119257" + 
":  " + 
"(b('L8b11') <= 2619.5) ? " + 
"-0.0005076600301444006" + 
":  " + 
"0.001454518934909013" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2036.5) ? " + 
"(b('L8b3') <= 1102.5) ? " + 
"(b('ndvi') <= 670.5) ? " + 
"0.1494326567398122" + 
":  " + 
"0.0005711330861447685" + 
":  " + 
"(b('L8b4') <= 1535.5) ? " + 
"0.02576273654283691" + 
":  " + 
"-0.013963252891878691" + 
":  " + 
"(b('L8b5') <= 2037.5) ? " + 
"(b('dgvv') <= 0.34427499771118164) ? " + 
"-0.030579736169943684" + 
":  " + 
"-0.05286829928873607" + 
":  " + 
"(b('L8b2') <= 314.5) ? " + 
"0.004878736028195434" + 
":  " + 
"-0.0002400506463954045" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 630.5) ? " + 
"(b('L8b5') <= 2591.0) ? " + 
"(b('L8b5') <= 2538.0) ? " + 
"-0.0017614685466004142" + 
":  " + 
"-0.017647646774994204" + 
":  " + 
"(b('L8b11') <= 1316.5) ? " + 
"-0.0008360746673909869" + 
":  " + 
"0.021676691428753943" + 
":  " + 
"(b('L8b4') <= 616.0) ? " + 
"(b('L8b3') <= 649.5) ? " + 
"0.03180953413039004" + 
":  " + 
"0.0017959757253740956" + 
":  " + 
"(b('L8b2') <= 355.5) ? " + 
"-0.006324519950859808" + 
":  " + 
"0.00012337173955747878" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 1681.0) ? " + 
"(b('L8b5') <= 1677.5) ? " + 
"(b('L8b2med') <= 771.5) ? " + 
"0.003263472461766099" + 
":  " + 
"-0.013002237053123943" + 
":  " + 
"(b('dgvv') <= 0.7161188125610352) ? " + 
"0.013112544718130531" + 
":  " + 
"0.09080232957802932" + 
":  " + 
"(b('L8b5') <= 1683.0) ? " + 
"(b('L8dt') <= 734648.0) ? " + 
"-0.018254626300282004" + 
":  " + 
"-0.048414109774757054" + 
":  " + 
"(b('L8b6med') <= 2069.625) ? " + 
"-0.006372859196468008" + 
":  " + 
"8.870194746920493e-07" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 1925.5) ? " + 
"(b('L8b6') <= 1891.0) ? " + 
"(b('sand') <= 32.0) ? " + 
"0.008343844394001272" + 
":  " + 
"-0.003487499754658157" + 
":  " + 
"(b('L8b2') <= 539.5) ? " + 
"0.02108487163746153" + 
":  " + 
"-0.04318931106378562" + 
":  " + 
"(b('L8b2') <= 247.5) ? " + 
"-0.09547985537219542" + 
":  " + 
"(b('sand') <= 80.5) ? " + 
"-0.0001231270830407866" + 
":  " + 
"0.01605570476013825" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3768.75) ? " + 
"(b('L8b4') <= 2861.5) ? " + 
"(b('L8b4') <= 2644.5) ? " + 
"-6.543978756136459e-05" + 
":  " + 
"0.008803168604067175" + 
":  " + 
"(b('crops') <= 96.93007278442383) ? " + 
"-0.0013590508370232325" + 
":  " + 
"-0.019173963354315784" + 
":  " + 
"(b('ndvi') <= 820.0) ? " + 
"(b('dsvv') <= 0.036346435546875) ? " + 
"0.000678443943406758" + 
":  " + 
"0.0459144755600669" + 
":  " + 
"(b('L8dt') <= 528928.0) ? " + 
"-0.002138358784117328" + 
":  " + 
"0.010117439226114964" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crops') <= 48.65084648132324) ? " + 
"(b('dgvv') <= 1.3410148620605469) ? " + 
"(b('dsvv') <= 1.323287010192871) ? " + 
"-4.4378845280032026e-05" + 
":  " + 
"-0.036632977242675405" + 
":  " + 
"(b('L8b5med') <= 2575.75) ? " + 
"-0.0024899051624132497" + 
":  " + 
"0.008886466049347735" + 
":  " + 
"(b('dsvv') <= 1.5743064880371094) ? " + 
"(b('L8b4') <= 891.0) ? " + 
"-0.002618253211161702" + 
":  " + 
"0.0010950995001724425" + 
":  " + 
"(b('lat') <= 36.13958549499512) ? " + 
"0.01714447148608931" + 
":  " + 
"-0.00445442996263584" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2142.5) ? " + 
"(b('L8b6med') <= 3650.5) ? " + 
"(b('lat') <= 43.45442581176758) ? " + 
"0.004010889816590121" + 
":  " + 
"-0.0007902949097394811" + 
":  " + 
"(b('crops') <= 3.819875717163086) ? " + 
"-0.03819785308583797" + 
":  " + 
"-0.004366219552886143" + 
":  " + 
"(b('L8b5') <= 2231.5) ? " + 
"(b('sand') <= 22.0) ? " + 
"-0.05721263517548015" + 
":  " + 
"-0.0032763076443222566" + 
":  " + 
"(b('L8b6') <= 2216.0) ? " + 
"0.0028812685412677222" + 
":  " + 
"-0.0002310089287067303" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3658.5) ? " + 
"(b('L8b5') <= 3656.5) ? " + 
"(b('L8b11') <= 3451.0) ? " + 
"8.823130544278705e-06" + 
":  " + 
"0.004413611170010195" + 
":  " + 
"(b('L8dt') <= 561382.5) ? " + 
"0.003323407419047534" + 
":  " + 
"0.04619752271808249" + 
":  " + 
"(b('L8b5med') <= 2582.5) ? " + 
"(b('ndvi') <= 4939.5) ? " + 
"-0.028255258676276027" + 
":  " + 
"0.018356625980715167" + 
":  " + 
"(b('L8b2') <= 487.5) ? " + 
"0.005629418284022471" + 
":  " + 
"-0.00237875233051636" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1514.5) ? " + 
"(b('L8b3') <= 1176.0) ? " + 
"(b('L8b2') <= 542.0) ? " + 
"-0.00038584841041851514" + 
":  " + 
"-0.014231485273483556" + 
":  " + 
"(b('dsvv') <= -0.8185567855834961) ? " + 
"0.1248774438848145" + 
":  " + 
"0.05535017839413642" + 
":  " + 
"(b('L8b11') <= 1516.5) ? " + 
"(b('L8b6med') <= 3155.0) ? " + 
"0.058788919953999416" + 
":  " + 
"-0.005142830747731382" + 
":  " + 
"(b('L8b2') <= 463.5) ? " + 
"0.0038633374579364692" + 
":  " + 
"-0.00011985033178961816" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 728.5) ? " + 
"(b('L8b6') <= 2472.0) ? " + 
"(b('L8b3') <= 721.5) ? " + 
"0.0014491163411994913" + 
":  " + 
"-0.01314699232575572" + 
":  " + 
"(b('L8b5med') <= 2738.0) ? " + 
"-0.0008389458925038849" + 
":  " + 
"-0.012536387870674078" + 
":  " + 
"(b('L8b4') <= 946.5) ? " + 
"(b('lon') <= -110.7353401184082) ? " + 
"0.015591762874078189" + 
":  " + 
"0.00093075148684902" + 
":  " + 
"(b('L8b3') <= 810.0) ? " + 
"-0.008671692011347097" + 
":  " + 
"-4.975060409780704e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 65970.5) ? " + 
"(b('L8dt') <= 65445.0) ? " + 
"(b('sand') <= 23.5) ? " + 
"0.017383596834251957" + 
":  " + 
"3.514950365168775e-05" + 
":  " + 
"(b('sand') <= 58.5) ? " + 
"0.02034170721330535" + 
":  " + 
"0.12322399792684585" + 
":  " + 
"(b('L8dt') <= 65988.5) ? " + 
"(b('dgvv') <= -1.5066027641296387) ? " + 
"0.00817967321936345" + 
":  " + 
"-0.023729739057841197" + 
":  " + 
"(b('L8dt') <= 88170.0) ? " + 
"-0.003939615846859753" + 
":  " + 
"5.0720232878052083e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1242.5) ? " + 
"(b('L8b5med') <= 3256.5) ? " + 
"(b('L8b6med') <= 2452.0) ? " + 
"0.00354509362821885" + 
":  " + 
"-0.003552590569920181" + 
":  " + 
"(b('L8b4') <= 734.0) ? " + 
"-0.012716723519725673" + 
":  " + 
"-0.09846130472076198" + 
":  " + 
"(b('L8b11') <= 1299.5) ? " + 
"(b('L8b6med') <= 2069.625) ? " + 
"-0.08332234019336644" + 
":  " + 
"0.0057207805808712" + 
":  " + 
"(b('L8b6') <= 1873.0) ? " + 
"0.01671017357119878" + 
":  " + 
"-9.338545543624307e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2673.75) ? " + 
"(b('L8b4') <= 1128.5) ? " + 
"(b('L8b4') <= 1092.0) ? " + 
"-0.00032906125035801786" + 
":  " + 
"0.015698428019909817" + 
":  " + 
"(b('L8b3') <= 1061.5) ? " + 
"-0.012577332644868789" + 
":  " + 
"0.0005326466842616298" + 
":  " + 
"(b('L8b6med') <= 2700.0) ? " + 
"(b('L8b6') <= 3235.0) ? " + 
"0.0062727583105428135" + 
":  " + 
"0.054559177360029944" + 
":  " + 
"(b('ndvi') <= 6890.0) ? " + 
"6.92203890994803e-05" + 
":  " + 
"0.019971681046190983" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('dgvv') <= -0.12257957458496094) ? " + 
"(b('dsvv') <= -0.4114527702331543) ? " + 
"-0.014444852637825828" + 
":  " + 
"-0.1295009073496855" + 
":  " + 
"(b('L8dt') <= 1943997.0) ? " + 
"0.006552076146073494" + 
":  " + 
"-0.057824697027745" + 
":  " + 
"(b('L8b2') <= 181.0) ? " + 
"(b('L8dt') <= 1357251.0) ? " + 
"0.017358603078195374" + 
":  " + 
"-0.013552297868418713" + 
":  " + 
"(b('L8b2') <= 203.5) ? " + 
"-0.02552037386131085" + 
":  " + 
"1.1328983270408792e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 872.5) ? " + 
"(b('L8b3') <= 860.5) ? " + 
"(b('L8b3') <= 856.75) ? " + 
"-0.00044798996532134134" + 
":  " + 
"0.01941155473843666" + 
":  " + 
"(b('lon') <= 1.4101499915122986) ? " + 
"1.0742374375304586e-06" + 
":  " + 
"-0.021603372420523237" + 
":  " + 
"(b('L8b2') <= 591.5) ? " + 
"(b('L8b3') <= 1165.5) ? " + 
"0.003156066957740122" + 
":  " + 
"0.054678125540651996" + 
":  " + 
"(b('L8b5') <= 1865.0) ? " + 
"0.012422669160179185" + 
":  " + 
"-0.0004128399559291506" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3768.75) ? " + 
"(b('L8b7med') <= 3305.0) ? " + 
"(b('L8b6') <= 4861.5) ? " + 
"0.00010223630035515667" + 
":  " + 
"-0.006697406669468611" + 
":  " + 
"(b('dgvv') <= 1.4454612731933594) ? " + 
"0.00018953961831159812" + 
":  " + 
"-0.0266627977042534" + 
":  " + 
"(b('ndvi') <= 820.0) ? " + 
"(b('ndvi') <= 811.0) ? " + 
"0.010776025752717007" + 
":  " + 
"0.059722428112174354" + 
":  " + 
"(b('dsvv') <= 1.6493310928344727) ? " + 
"0.002839547604638523" + 
":  " + 
"-0.017222770054300462" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3369.5) ? " + 
"(b('L8b6') <= 2843.5) ? " + 
"(b('L8b6') <= 2841.5) ? " + 
"0.00039680292801924655" + 
":  " + 
"0.03512665037567677" + 
":  " + 
"(b('L8b2') <= 734.5) ? " + 
"-0.0034001903092085537" + 
":  " + 
"0.0011368039636244789" + 
":  " + 
"(b('dgvv') <= 1.1451258659362793) ? " + 
"(b('L8b4') <= 1642.5) ? " + 
"0.0041575444027928425" + 
":  " + 
"0.00015599074682983937" + 
":  " + 
"(b('L8b7med') <= 2880.75) ? " + 
"0.0004542980987426019" + 
":  " + 
"-0.009058019736915857" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1472.5) ? " + 
"(b('L8b11') <= 1469.5) ? " + 
"(b('L8b6') <= 2604.5) ? " + 
"7.691268618862714e-05" + 
":  " + 
"-0.01007639430051489" + 
":  " + 
"(b('L8b7med') <= 1637.5) ? " + 
"0.003692111693775303" + 
":  " + 
"-0.033627158275151316" + 
":  " + 
"(b('L8b4') <= 946.5) ? " + 
"(b('crops') <= 33.79139518737793) ? " + 
"0.007085972615051282" + 
":  " + 
"-0.0014524686081198478" + 
":  " + 
"(b('L8b11') <= 1531.0) ? " + 
"-0.017511672759951493" + 
":  " + 
"-6.858281534609594e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3020.0) ? " + 
"(b('L8b4') <= 1706.0) ? " + 
"(b('ndvi_med') <= 1564.0) ? " + 
"0.0035821781712720266" + 
":  " + 
"-0.0004214931739727568" + 
":  " + 
"(b('L8b3') <= 1508.0) ? " + 
"-0.0075677392871982" + 
":  " + 
"0.0012786843225329667" + 
":  " + 
"(b('L8b5') <= 2962.5) ? " + 
"(b('ndvi_med') <= 4779.25) ? " + 
"0.0032590587694446738" + 
":  " + 
"0.03724062407794476" + 
":  " + 
"(b('L8b5') <= 2968.5) ? " + 
"-0.029787569607315403" + 
":  " + 
"-0.000557599450862819" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 933.5) ? " + 
"(b('L8b2med') <= 850.0) ? " + 
"(b('L8b7med') <= 2456.0) ? " + 
"-0.0006454430114665006" + 
":  " + 
"0.00621267253574684" + 
":  " + 
"(b('L8b2') <= 658.5) ? " + 
"-0.010237181791375569" + 
":  " + 
"-0.11275359129612539" + 
":  " + 
"(b('L8b4') <= 1231.5) ? " + 
"(b('lon') <= -111.32536697387695) ? " + 
"0.019133508495298043" + 
":  " + 
"0.002533752041553179" + 
":  " + 
"(b('L8b5') <= 2209.5) ? " + 
"-0.006809864868121455" + 
":  " + 
"0.0002405916346689892" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2974.5) ? " + 
"(b('L8b6') <= 4165.5) ? " + 
"(b('L8b6') <= 4038.0) ? " + 
"-0.00014118447670311381" + 
":  " + 
"0.012949618239664746" + 
":  " + 
"(b('L8dt') <= 2355340.5) ? " + 
"-0.013612105707481992" + 
":  " + 
"0.034158518821319976" + 
":  " + 
"(b('ndvi') <= 1537.0) ? " + 
"(b('ndvi_med') <= 1559.0) ? " + 
"0.0013488926741038075" + 
":  " + 
"-0.007409669233153887" + 
":  " + 
"(b('lon') <= -5.310745000839233) ? " + 
"0.0015788867685463553" + 
":  " + 
"0.012117665039558032" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 5819576.0) ? " + 
"(b('L8dt') <= 5529041.5) ? " + 
"(b('L8dt') <= 5454815.0) ? " + 
"-2.742854356950611e-05" + 
":  " + 
"0.021856953815390243" + 
":  " + 
"(b('ndvi') <= 3957.0) ? " + 
"-0.005084510456752343" + 
":  " + 
"-0.061197596280809445" + 
":  " + 
"(b('L8b11') <= 1344.5) ? " + 
"(b('L8b6med') <= 2337.0) ? " + 
"0.056104998510903295" + 
":  " + 
"0.024551852046102447" + 
":  " + 
"(b('ndvi') <= 1380.0) ? " + 
"0.02031134496333867" + 
":  " + 
"-0.0011770140332719866" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 817.5) ? " + 
"(b('lat') <= 32.848440170288086) ? " + 
"(b('L8b3') <= 711.5) ? " + 
"-0.0066193191662209955" + 
":  " + 
"0.013554815378204856" + 
":  " + 
"(b('L8b6') <= 2608.0) ? " + 
"0.00022481025211025198" + 
":  " + 
"-0.005081352898127231" + 
":  " + 
"(b('ndvi_med') <= 3698.5) ? " + 
"(b('ndvi_med') <= 3668.75) ? " + 
"3.691492985924719e-05" + 
":  " + 
"-0.030057684085808258" + 
":  " + 
"(b('L8b2') <= 535.5) ? " + 
"0.014929658094637182" + 
":  " + 
"0.0004763676936897929" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 3658.5) ? " + 
"(b('L8b5') <= 3656.5) ? " + 
"(b('L8b5med') <= 3243.0) ? " + 
"-0.00010939966238172891" + 
":  " + 
"0.002024497483889104" + 
":  " + 
"(b('L8dt') <= 561382.5) ? " + 
"0.0027403222976197196" + 
":  " + 
"0.04142705639520965" + 
":  " + 
"(b('lon') <= -5.50570011138916) ? " + 
"(b('dgvv') <= 1.318563461303711) ? " + 
"-0.010666434279108248" + 
":  " + 
"0.012944249278482048" + 
":  " + 
"(b('dgvv') <= 1.4996399879455566) ? " + 
"0.0023975392122165613" + 
":  " + 
"-0.010043181346581267" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 4260.0) ? " + 
"(b('L8b6med') <= 5567.0) ? " + 
"(b('L8b6') <= 4855.5) ? " + 
"3.338184184411012e-05" + 
":  " + 
"-0.005842456849367725" + 
":  " + 
"-0.07119156055547375" + 
":  " + 
"(b('L8b6') <= 5133.5) ? " + 
"(b('ndvi') <= 703.0) ? " + 
"-0.02161140895153294" + 
":  " + 
"0.01934812779454218" + 
":  " + 
"(b('dsvv') <= 1.516878604888916) ? " + 
"0.0035678327378722723" + 
":  " + 
"-0.017736528724628834" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5med') <= 3768.75) ? " + 
"(b('L8b5') <= 3668.5) ? " + 
"(b('L8b5') <= 3665.5) ? " + 
"8.410817480684473e-05" + 
":  " + 
"0.018565315461612865" + 
":  " + 
"(b('L8b5') <= 3673.5) ? " + 
"-0.02710363793089439" + 
":  " + 
"-0.0008100791956456972" + 
":  " + 
"(b('ndvi') <= 820.0) ? " + 
"(b('L8b11') <= 3951.25) ? " + 
"0.03875557314350216" + 
":  " + 
"-0.00012989354965573245" + 
":  " + 
"(b('L8dt') <= 528928.0) ? " + 
"-0.0011712367925201701" + 
":  " + 
"0.009508654186594032" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lon') <= -120.6328010559082) ? " + 
"(b('dgvv') <= 1.6138911247253418) ? " + 
"(b('L8b5med') <= 2199.75) ? " + 
"-0.02110684868653752" + 
":  " + 
"0.0039781525913786826" + 
":  " + 
"(b('ndvi') <= 1300.0) ? " + 
"0.06570663215229933" + 
":  " + 
"-0.01930668633664495" + 
":  " + 
"(b('L8b3') <= 1420.5) ? " + 
"(b('L8b3') <= 1419.5) ? " + 
"-0.00030127713925260887" + 
":  " + 
"-0.03685924431270528" + 
":  " + 
"(b('sand') <= 42.5) ? " + 
"0.010964067981846867" + 
":  " + 
"-4.982183890099177e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1673.5) ? " + 
"(b('ndvi_med') <= 2433.0) ? " + 
"(b('ndvi') <= 1666.5) ? " + 
"-0.0009565435863748749" + 
":  " + 
"-0.021807589856305275" + 
":  " + 
"(b('L8b5') <= 2247.5) ? " + 
"-0.0012077967837183707" + 
":  " + 
"0.02958933175268565" + 
":  " + 
"(b('ndvi') <= 1810.0) ? " + 
"(b('L8b2') <= 477.5) ? " + 
"0.021319854211197187" + 
":  " + 
"0.0035554768893110945" + 
":  " + 
"(b('ndvi') <= 1919.5) ? " + 
"-0.00495482302842353" + 
":  " + 
"0.00021212570153279146" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 1457.25) ? " + 
"(b('dgvv') <= 2.1364288330078125) ? " + 
"(b('dgvv') <= 2.056309700012207) ? " + 
"-0.0013646682731354364" + 
":  " + 
"-0.02356917222254666" + 
":  " + 
"(b('L8b6med') <= 2084.125) ? " + 
"-0.025826572375279265" + 
":  " + 
"0.0065408799513173915" + 
":  " + 
"(b('L8b11') <= 1463.5) ? " + 
"(b('L8b6') <= 2289.5) ? " + 
"0.0865649052468549" + 
":  " + 
"0.004520010141698568" + 
":  " + 
"(b('L8b4') <= 835.5) ? " + 
"0.0025011884656602405" + 
":  " + 
"-0.00020084723939658568" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 868.5) ? " + 
"(b('L8b3') <= 860.5) ? " + 
"(b('L8b3') <= 856.75) ? " + 
"-0.000438395387486773" + 
":  " + 
"0.01715889670484818" + 
":  " + 
"(b('L8b2med') <= 749.0) ? " + 
"-0.014592959149712217" + 
":  " + 
"0.03302267943678022" + 
":  " + 
"(b('L8b7med') <= 1895.5) ? " + 
"(b('L8b5') <= 3349.0) ? " + 
"0.004548195391734223" + 
":  " + 
"-0.0030198787845129495" + 
":  " + 
"(b('L8b5') <= 1745.0) ? " + 
"-0.022586130694663555" + 
":  " + 
"-0.00021100072849192057" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2606.5) ? " + 
"(b('L8b4') <= 2100.0) ? " + 
"(b('L8b4') <= 1460.0) ? " + 
"0.0002074604032995136" + 
":  " + 
"-0.003424221113561538" + 
":  " + 
"(b('L8b3') <= 1494.5) ? " + 
"0.1415860926211787" + 
":  " + 
"0.00977234089257624" + 
":  " + 
"(b('L8b11') <= 2667.5) ? " + 
"(b('L8b5med') <= 3591.0) ? " + 
"0.0054910809536998974" + 
":  " + 
"0.04470877838337221" + 
":  " + 
"(b('L8b11') <= 2719.0) ? " + 
"-0.011811060358825853" + 
":  " + 
"0.0007194409193832505" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b3') <= 933.5) ? " + 
"(b('L8b3') <= 930.5) ? " + 
"(b('L8b2med') <= 868.5) ? " + 
"-0.00017518509381729658" + 
":  " + 
"-0.010880541597803894" + 
":  " + 
"(b('dgvv') <= 0.6316418647766113) ? " + 
"-0.03318358187229141" + 
":  " + 
"0.0030518430212387662" + 
":  " + 
"(b('L8b3') <= 945.5) ? " + 
"(b('L8b5') <= 1856.5) ? " + 
"0.07913772889056236" + 
":  " + 
"0.006654779519160535" + 
":  " + 
"(b('L8b7med') <= 1895.5) ? " + 
"0.0032727888911720853" + 
":  " + 
"-0.00043726347997782514" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2673.75) ? " + 
"(b('L8b5') <= 2886.0) ? " + 
"(b('L8b6med') <= 2659.0) ? " + 
"-0.0012886627699487292" + 
":  " + 
"-0.024255652865614135" + 
":  " + 
"(b('ndvi') <= 1212.0) ? " + 
"0.22418806505361097" + 
":  " + 
"0.0014183258370741533" + 
":  " + 
"(b('L8b6med') <= 2700.0) ? " + 
"(b('dgvv') <= -0.9597911834716797) ? " + 
"-0.01099204089486032" + 
":  " + 
"0.016208529673466268" + 
":  " + 
"(b('ndvi') <= 6890.0) ? " + 
"8.811613326813764e-05" + 
":  " + 
"0.01742998060855487" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2268.5) ? " + 
"(b('L8b6') <= 3723.5) ? " + 
"(b('L8b11') <= 2258.5) ? " + 
"-0.0001604116737304755" + 
":  " + 
"-0.014476328967345981" + 
":  " + 
"(b('ndvi') <= 3743.5) ? " + 
"-0.028171195729112874" + 
":  " + 
"-0.08257188557847968" + 
":  " + 
"(b('L8b7med') <= 1864.0) ? " + 
"(b('L8b6med') <= 3032.25) ? " + 
"0.003974421459682355" + 
":  " + 
"0.0418184023421151" + 
":  " + 
"(b('L8b5') <= 3309.5) ? " + 
"-0.0009331859118484136" + 
":  " + 
"0.002692260253673465" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 5235.5) ? " + 
"(b('ndvi') <= 5018.5) ? " + 
"(b('ndvi') <= 4994.0) ? " + 
"4.262174301818301e-05" + 
":  " + 
"-0.014000978856640207" + 
":  " + 
"(b('L8b3') <= 990.5) ? " + 
"0.0031815602189108226" + 
":  " + 
"0.027778809799681746" + 
":  " + 
"(b('L8b5') <= 2831.5) ? " + 
"(b('L8b7med') <= 1316.5) ? " + 
"-0.030253918563868196" + 
":  " + 
"-0.006386143531414019" + 
":  " + 
"(b('L8b5med') <= 3053.0) ? " + 
"0.011320426252415835" + 
":  " + 
"-0.003352014368063175" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b2') <= 325.5) ? " + 
"(b('L8b7med') <= 1407.0) ? " + 
"(b('crops') <= 26.25460147857666) ? " + 
"-3.3161106752763486e-05" + 
":  " + 
"0.01570109782469298" + 
":  " + 
"(b('sand') <= 16.5) ? " + 
"0.08635699794733649" + 
":  " + 
"-0.002266479656378411" + 
":  " + 
"(b('L8b4') <= 472.0) ? " + 
"(b('L8b6med') <= 3092.5) ? " + 
"-0.2136166823453087" + 
":  " + 
"0.04250202817552262" + 
":  " + 
"(b('L8b3') <= 562.5) ? " + 
"-0.009004766890825971" + 
":  " + 
"3.786462569750897e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2142.5) ? " + 
"(b('L8b5') <= 2140.5) ? " + 
"(b('L8b2') <= 950.0) ? " + 
"0.0010115529176772061" + 
":  " + 
"-0.02582468188806145" + 
":  " + 
"(b('L8b7med') <= 2107.25) ? " + 
"0.005845890447630008" + 
":  " + 
"0.05734940075291048" + 
":  " + 
"(b('L8b5') <= 2231.5) ? " + 
"(b('ndvi') <= 1527.0) ? " + 
"-0.013805951079776132" + 
":  " + 
"0.0009792598258458567" + 
":  " + 
"(b('dsvv') <= -2.516829013824463) ? " + 
"-0.0031933269171179157" + 
":  " + 
"0.00015853199146856074" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6') <= 3892.5) ? " + 
"(b('L8b6') <= 3811.5) ? " + 
"(b('L8b6') <= 3809.5) ? " + 
"-5.104039294467793e-06" + 
":  " + 
"-0.02136787860684406" + 
":  " + 
"(b('L8b6') <= 3813.5) ? " + 
"0.03995733062463932" + 
":  " + 
"0.004368522329163384" + 
":  " + 
"(b('L8b6') <= 3914.5) ? " + 
"(b('L8dt') <= 12816.0) ? " + 
"0.13877776435299133" + 
":  " + 
"-0.015881506931319737" + 
":  " + 
"(b('L8b6') <= 3921.5) ? " + 
"0.03408155205050934" + 
":  " + 
"-0.0006082040360516969" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b7med') <= 988.0) ? " + 
"(b('dsvv') <= -0.13337230682373047) ? " + 
"(b('dsvv') <= -0.4114527702331543) ? " + 
"-0.014034341550519618" + 
":  " + 
"-0.1177221612784425" + 
":  " + 
"(b('dgvv') <= 4.7125563621521) ? " + 
"0.0051562152205317565" + 
":  " + 
"-0.05258594864370729" + 
":  " + 
"(b('L8b2med') <= 395.5) ? " + 
"(b('L8b11') <= 1328.5) ? " + 
"-0.003549338034380612" + 
":  " + 
"0.005469064003568272" + 
":  " + 
"(b('L8b4') <= 660.5) ? " + 
"0.00200649492499123" + 
":  " + 
"-0.00023941950660383323" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 3369.5) ? " + 
"(b('L8b6') <= 4577.0) ? " + 
"(b('dgvv') <= -1.269556999206543) ? " + 
"-0.0022701120794822553" + 
":  " + 
"0.00021899241659729227" + 
":  " + 
"(b('L8dt') <= 1057232.5) ? " + 
"0.00461461980615595" + 
":  " + 
"-0.029716669957606665" + 
":  " + 
"(b('L8b6') <= 2635.5) ? " + 
"(b('L8b4') <= 1045.0) ? " + 
"-0.0004056241746888168" + 
":  " + 
"-0.014133449811506974" + 
":  " + 
"(b('L8b6') <= 3466.0) ? " + 
"0.005657529724601299" + 
":  " + 
"-0.00041264969715856966" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b11') <= 2974.5) ? " + 
"(b('L8b6') <= 4165.5) ? " + 
"(b('L8b6') <= 4038.0) ? " + 
"-0.00013689517423555038" + 
":  " + 
"0.011131045220614864" + 
":  " + 
"(b('L8dt') <= 2721872.0) ? " + 
"-0.011265183603520842" + 
":  " + 
"0.03933624845229005" + 
":  " + 
"(b('L8b11') <= 3007.0) ? " + 
"(b('L8dt') <= 625501.5) ? " + 
"0.003065189847321706" + 
":  " + 
"0.03405139291232097" + 
":  " + 
"(b('L8b5med') <= 2828.0) ? " + 
"-0.004854226205760453" + 
":  " + 
"0.0015358970698101278" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 4653.0) ? " + 
"(b('L8b5') <= 4612.5) ? " + 
"(b('ndvi_med') <= 5674.5) ? " + 
"1.5258443967707331e-05" + 
":  " + 
"-0.008688785029297324" + 
":  " + 
"(b('ndvi') <= 4946.5) ? " + 
"-0.00522229804048578" + 
":  " + 
"-0.026277412807285256" + 
":  " + 
"(b('ndvi') <= 5908.5) ? " + 
"(b('L8dt') <= 1515346.5) ? " + 
"0.00921967956006481" + 
":  " + 
"0.03966091257330755" + 
":  " + 
"(b('dsvv') <= -0.3896975517272949) ? " + 
"0.009557566150152616" + 
":  " + 
"-0.01047388139796066" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2142.5) ? " + 
"(b('L8b3') <= 1091.0) ? " + 
"(b('L8b4') <= 1168.5) ? " + 
"0.0018391333864032236" + 
":  " + 
"-0.006480341875507717" + 
":  " + 
"(b('dsvv') <= 0.5883440971374512) ? " + 
"-0.002297710576846365" + 
":  " + 
"0.029271763558095288" + 
":  " + 
"(b('L8b3') <= 728.5) ? " + 
"(b('L8b4') <= 764.5) ? " + 
"-0.0004177299767283126" + 
":  " + 
"-0.01147352326519115" + 
":  " + 
"(b('L8b5') <= 2215.5) ? " + 
"-0.00510762584502758" + 
":  " + 
"0.00030463852176864964" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b5') <= 2767.5) ? " + 
"(b('L8b5med') <= 3138.5) ? " + 
"(b('L8b11') <= 3114.0) ? " + 
"0.0002233525279494601" + 
":  " + 
"-0.011080611736726788" + 
":  " + 
"(b('ndvi') <= 2604.5) ? " + 
"0.0002354662774505188" + 
":  " + 
"0.017231020599570136" + 
":  " + 
"(b('L8b5') <= 2790.5) ? " + 
"(b('L8b3') <= 695.0) ? " + 
"-0.09052492323615546" + 
":  " + 
"-0.011763152595615988" + 
":  " + 
"(b('dsvv') <= 1.687027931213379) ? " + 
"0.000493911684332576" + 
":  " + 
"-0.0036134714061465067" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 316.5) ? " + 
"0.04929041596117049" + 
":  " + 
"(b('L8dt') <= 318.0) ? " + 
"-0.06329434655245889" + 
":  " + 
"(b('L8dt') <= 336.0) ? " + 
"0.041762952616396384" + 
":  " + 
"-4.405701815049775e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('dgvv') <= -9.844696760177612) ? " + 
"(b('ndvi') <= 1323.0) ? " + 
"0.022574170901782546" + 
":  " + 
"0.046191128435014835" + 
":  " + 
"(b('dsvv') <= -4.535989284515381) ? " + 
"(b('L8b2med') <= 413.5) ? " + 
"0.04303053630094942" + 
":  " + 
"-0.006930424976912129" + 
":  " + 
"(b('dsvv') <= -4.426722526550293) ? " + 
"0.017321479977711676" + 
":  " + 
"7.276791373549097e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8dt') <= 5819576.0) ? " + 
"(b('L8dt') <= 5518420.5) ? " + 
"(b('L8dt') <= 5454815.0) ? " + 
"-2.744636069348907e-05" + 
":  " + 
"0.0227836929940445" + 
":  " + 
"(b('ndvi') <= 3436.5) ? " + 
"-0.0016664335257679578" + 
":  " + 
"-0.04548217560763882" + 
":  " + 
"(b('L8b11') <= 1344.5) ? " + 
"(b('ndvi_med') <= 3523.5) ? " + 
"0.0148707801221488" + 
":  " + 
"0.032761721614017435" + 
":  " + 
"(b('lon') <= -5.3525800704956055) ? " + 
"-0.00974395802032956" + 
":  " + 
"0.006511826608708811" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('L8b6med') <= 2669.75) ? " + 
"(b('L8b6') <= 3976.5) ? " + 
"(b('L8b5') <= 2886.0) ? " + 
"-0.0016468934468083722" + 
":  " + 
"0.0016073561347525493" + 
":  " + 
"(b('dsvv') <= 2.588033676147461) ? " + 
"-0.02731156504804662" + 
":  " + 
"0.08709194076362288" + 
":  " + 
"(b('L8b6med') <= 2700.0) ? " + 
"(b('L8b5') <= 1979.5) ? " + 
"0.05298345320743317" + 
":  " + 
"0.004203546264082691" + 
":  " + 
"(b('ndvi_med') <= 4344.5) ? " + 
"8.933441028181132e-06" + 
":  " + 
"0.006723943942095" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  return prediction