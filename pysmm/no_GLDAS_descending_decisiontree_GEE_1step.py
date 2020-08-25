import ee 

def tree(feature_stack): 

  prediction = ee.Image(0.14258337)
  learning_rate = ee.Image(0.1)
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 1720.5) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('b3') <= 620.5) ? " + 
"0.11808639691868263" + 
":  " + 
"0.055933972152061924" + 
":  " + 
"(b('moss') <= 6.307743549346924) ? " + 
"0.08478444634840407" + 
":  " + 
"-0.01646329509936264" + 
":  " + 
"(b('bare') <= 5.53663182258606) ? " + 
"(b('g0vv') <= -10.523284912109375) ? " + 
"-0.018436079804975802" + 
":  " + 
"0.030394924459998626" + 
":  " + 
"(b('grass') <= 21.3190860748291) ? " + 
"-0.09989837580880541" + 
":  " + 
"-0.04044140321447661" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1229.5) ? " + 
"(b('b2') <= 391.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"0.03698070065636452" + 
":  " + 
"0.16402757508029284" + 
":  " + 
"(b('urban') <= 20.123075485229492) ? " + 
"0.025995665006441203" + 
":  " + 
"-0.038697511845123704" + 
":  " + 
"(b('bare') <= 5.53663182258606) ? " + 
"(b('g0vv') <= -10.151272773742676) ? " + 
"-0.024398637609639333" + 
":  " + 
"0.04568767140970594" + 
":  " + 
"(b('grass') <= 15.92530632019043) ? " + 
"-0.09300673577246665" + 
":  " + 
"-0.04538708122124096" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 1720.5) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('crop') <= 2.4269771575927734) ? " + 
"-0.0065494527286960764" + 
":  " + 
"0.06529683819286025" + 
":  " + 
"(b('moss') <= 6.307743549346924) ? " + 
"0.07138044536533955" + 
":  " + 
"-0.016696998862751323" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('g0vh') <= -17.55005168914795) ? " + 
"-0.01153212513142964" + 
":  " + 
"0.03765725888053805" + 
":  " + 
"(b('b4') <= 1583.0) ? " + 
"-0.024401889949789927" + 
":  " + 
"-0.06421789312546515" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2312.5) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('g0vv') <= -10.671287536621094) ? " + 
"-0.02080694043412765" + 
":  " + 
"0.0372309755154278" + 
":  " + 
"(b('b7') <= 2386.5) ? " + 
"-0.024179966636307542" + 
":  " + 
"-0.05695771578802202" + 
":  " + 
"(b('b3') <= 640.5) ? " + 
"(b('b6') <= 2431.5) ? " + 
"0.05490039703712874" + 
":  " + 
"0.19070466888013549" + 
":  " + 
"(b('l8dt') <= 1398549.0) ? " + 
"0.009213270462736121" + 
":  " + 
"0.05429313339221058" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1229.5) ? " + 
"(b('urban') <= 20.123075485229492) ? " + 
"(b('b3') <= 627.5) ? " + 
"0.08375251484400123" + 
":  " + 
"0.02346602590415171" + 
":  " + 
"(b('grass') <= 2.9389312267303467) ? " + 
"0.011010702650448618" + 
":  " + 
"-0.050422400233806085" + 
":  " + 
"(b('moss') <= 9.386762142181396) ? " + 
"(b('g0vv') <= -11.032591342926025) ? " + 
"-0.021748816333979543" + 
":  " + 
"0.02812418152863779" + 
":  " + 
"(b('lia') <= 39.955238342285156) ? " + 
"-0.033812236824980885" + 
":  " + 
"-0.06689643854650636" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b10') <= 1720.5) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('crop') <= 2.4269771575927734) ? " + 
"-0.010506354575977836" + 
":  " + 
"0.05186210360150045" + 
":  " + 
"(b('b6') <= 1933.5) ? " + 
"0.08236086038878894" + 
":  " + 
"-0.014354536876879787" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('g0vh') <= -17.55005168914795) ? " + 
"-0.009337272077225343" + 
":  " + 
"0.030682098164531973" + 
":  " + 
"(b('crop') <= 79.08531951904297) ? " + 
"-0.037240443162174175" + 
":  " + 
"0.04335373088859647" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2336.5) ? " + 
"(b('l8dt') <= 815694.5) ? " + 
"(b('grass') <= 90.44964218139648) ? " + 
"-0.030632330288155745" + 
":  " + 
"0.03161384677284316" + 
":  " + 
"(b('g0vv') <= -9.45964527130127) ? " + 
"-0.0023538886422256526" + 
":  " + 
"0.04477550544350056" + 
":  " + 
"(b('grass') <= 42.76229476928711) ? " + 
"(b('bare') <= 5.524640083312988) ? " + 
"0.014909461147524969" + 
":  " + 
"-0.06826363775561586" + 
":  " + 
"(b('crop') <= 23.98758888244629) ? " + 
"0.024179664462066416" + 
":  " + 
"0.14602556117356208" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 2318.5) ? " + 
"(b('l8dt') <= 1401151.5) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.017545827009488507" + 
":  " + 
"-0.01675104425318725" + 
":  " + 
"(b('b2') <= 391.5) ? " + 
"0.08520440377092268" + 
":  " + 
"0.035567568431910904" + 
":  " + 
"(b('moss') <= 9.386762142181396) ? " + 
"(b('lia') <= 38.95977783203125) ? " + 
"0.007564446680299977" + 
":  " + 
"-0.022112610490173164" + 
":  " + 
"(b('lia') <= 39.955238342285156) ? " + 
"-0.029854490629736254" + 
":  " + 
"-0.05781556813941704" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2312.5) ? " + 
"(b('g0vv') <= -8.89116382598877) ? " + 
"(b('grass') <= 90.44964218139648) ? " + 
"-0.02179446160442337" + 
":  " + 
"0.030713657288396094" + 
":  " + 
"(b('bare') <= 5.524640083312988) ? " + 
"0.060416970018312484" + 
":  " + 
"-0.0482942523288793" + 
":  " + 
"(b('grass') <= 42.76229476928711) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.01821250385538885" + 
":  " + 
"-0.01685227157826517" + 
":  " + 
"(b('crop') <= 5.652343273162842) ? " + 
"0.00994690917007576" + 
":  " + 
"0.10810447926274111" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 2416.5) ? " + 
"(b('l8dt') <= 793952.5) ? " + 
"(b('ndvi') <= 3219.5) ? " + 
"-0.00839357726735498" + 
":  " + 
"0.01944698326438724" + 
":  " + 
"(b('urban') <= 20.123075485229492) ? " + 
"0.03634974183144234" + 
":  " + 
"-0.026323855608631225" + 
":  " + 
"(b('moss') <= 9.386762142181396) ? " + 
"(b('lia') <= 38.95977783203125) ? " + 
"0.007059814982398447" + 
":  " + 
"-0.020691706770779025" + 
":  " + 
"(b('lia') <= 39.955238342285156) ? " + 
"-0.025482557384561715" + 
":  " + 
"-0.05263419753861778" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 1679.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"(b('g0vv') <= -9.436891078948975) ? " + 
"0.0024950974526123993" + 
":  " + 
"0.04220677595780234" + 
":  " + 
"(b('grass') <= 59.79380416870117) ? " + 
"0.145818961749773" + 
":  " + 
"0.020802129688181303" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('g0vv') <= -11.097115516662598) ? " + 
"-0.009630800480173425" + 
":  " + 
"0.021857041910477607" + 
":  " + 
"(b('grass') <= 21.3190860748291) ? " + 
"-0.0401486451458356" + 
":  " + 
"-0.014520090548217937" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 800762.5) ? " + 
"(b('moss') <= 13.474450588226318) ? " + 
"(b('b4') <= 1167.5) ? " + 
"0.011501097933236948" + 
":  " + 
"-0.014644177832971943" + 
":  " + 
"(b('lia') <= 30.069743156433105) ? " + 
"0.005548836407076648" + 
":  " + 
"-0.03762175566739816" + 
":  " + 
"(b('b2') <= 391.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"0.01856168305589953" + 
":  " + 
"0.12374764840752456" + 
":  " + 
"(b('moss') <= 1.9861568808555603) ? " + 
"0.03540112175044209" + 
":  " + 
"0.003992477812894516" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 2658.5) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('g0vh') <= -18.797061920166016) ? " + 
"0.0011304687605007816" + 
":  " + 
"0.029239715855836422" + 
":  " + 
"(b('lia') <= 43.62149620056152) ? " + 
"-0.013446503580179067" + 
":  " + 
"0.05200590247662684" + 
":  " + 
"(b('lia') <= 42.22518348693848) ? " + 
"(b('lia') <= 39.03585433959961) ? " + 
"-0.010576062657744608" + 
":  " + 
"-0.03931655842825833" + 
":  " + 
"(b('l8dt') <= 700686.0) ? " + 
"-0.006725228807878548" + 
":  " + 
"0.06535240892427108" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 800762.5) ? " + 
"(b('moss') <= 13.474450588226318) ? " + 
"(b('ndvi') <= 3293.5) ? " + 
"-0.008533442085171606" + 
":  " + 
"0.020012394763243523" + 
":  " + 
"(b('lia') <= 30.069743156433105) ? " + 
"0.0054485982888476305" + 
":  " + 
"-0.03277691020309598" + 
":  " + 
"(b('urban') <= 22.551812171936035) ? " + 
"(b('b3') <= 701.5) ? " + 
"0.053212631948708164" + 
":  " + 
"0.015284811927849628" + 
":  " + 
"(b('grass') <= 2.9389312267303467) ? " + 
"-0.0034166138839497743" + 
":  " + 
"-0.03866726708349819" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 1335235.5) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"(b('ndvi') <= 3219.5) ? " + 
"-0.013239545439745206" + 
":  " + 
"0.012152518667887881" + 
":  " + 
"(b('g0vv') <= -12.063790321350098) ? " + 
"0.028776698417971282" + 
":  " + 
"0.1219012780036715" + 
":  " + 
"(b('ndvi') <= 3992.5) ? " + 
"(b('moss') <= 1.9861568808555603) ? " + 
"0.03690964802044319" + 
":  " + 
"0.006470098367369115" + 
":  " + 
"(b('grass') <= 39.24336242675781) ? " + 
"0.037103477383917616" + 
":  " + 
"0.1048619064072063" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 2416.5) ? " + 
"(b('urban') <= 22.551812171936035) ? " + 
"(b('trees') <= 24.201680183410645) ? " + 
"0.013228408316241402" + 
":  " + 
"-0.05840920534673547" + 
":  " + 
"(b('grass') <= 2.9389312267303467) ? " + 
"-0.005392607303511647" + 
":  " + 
"-0.04361722199957789" + 
":  " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('grass') <= 0.8429904580116272) ? " + 
"0.0002118786784117559" + 
":  " + 
"0.04098941856941541" + 
":  " + 
"(b('grass') <= 14.918523788452148) ? " + 
"-0.04032631925909704" + 
":  " + 
"-0.006249517553940196" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 2.297703742980957) ? " + 
"(b('g0vh') <= -17.516615867614746) ? " + 
"(b('b3') <= 642.0) ? " + 
"0.04324832503313256" + 
":  " + 
"-0.004063408267891756" + 
":  " + 
"(b('urban') <= 22.551812171936035) ? " + 
"0.03712696930737157" + 
":  " + 
"-0.023317522810965358" + 
":  " + 
"(b('b6') <= 1933.5) ? " + 
"(b('bare') <= 3.7568026781082153) ? " + 
"-0.015213878106894422" + 
":  " + 
"0.07767465654923657" + 
":  " + 
"(b('grass') <= 21.3190860748291) ? " + 
"-0.029928542878384326" + 
":  " + 
"-0.0056855347908298035" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 800762.5) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"(b('g0vv') <= -8.560012340545654) ? " + 
"-0.01103322521346541" + 
":  " + 
"0.029959274125511734" + 
":  " + 
"(b('g0vv') <= -12.063790321350098) ? " + 
"0.025853367613775588" + 
":  " + 
"0.0972948808294585" + 
":  " + 
"(b('grass') <= 17.072710037231445) ? " + 
"(b('moss') <= 1.5077694058418274) ? " + 
"0.02960545409168927" + 
":  " + 
"-0.015228495528941855" + 
":  " + 
"(b('crop') <= 71.31087875366211) ? " + 
"0.018784271550428312" + 
":  " + 
"0.09763107828619104" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b10') <= 2822.5) ? " + 
"(b('l8dt') <= 1403100.0) ? " + 
"(b('urban') <= 22.551812171936035) ? " + 
"0.002211356270966518" + 
":  " + 
"-0.02998887081796466" + 
":  " + 
"(b('urban') <= 0.9776536226272583) ? " + 
"0.029653995458310056" + 
":  " + 
"0.001992368835924255" + 
":  " + 
"(b('lia') <= 42.23679542541504) ? " + 
"(b('lia') <= 39.03585433959961) ? " + 
"-0.009067232037247075" + 
":  " + 
"-0.032370522506554526" + 
":  " + 
"(b('crop') <= 50.01498222351074) ? " + 
"-0.01670214913314228" + 
":  " + 
"0.037955079942880145" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.474450588226318) ? " + 
"(b('b11') <= 1679.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"0.008137720570690654" + 
":  " + 
"0.06092139444005644" + 
":  " + 
"(b('grass') <= 90.44964218139648) ? " + 
"-0.004804495267016684" + 
":  " + 
"0.031202284758761967" + 
":  " + 
"(b('b7') <= 1060.0) ? " + 
"(b('b11') <= 872.5) ? " + 
"-0.0160726428738699" + 
":  " + 
"0.10218744165457663" + 
":  " + 
"(b('moss') <= 25.020339012145996) ? " + 
"-0.021753088330044287" + 
":  " + 
"0.027114416661015193" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 2.297703742980957) ? " + 
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('lia') <= 39.09046745300293) ? " + 
"0.010850256340396573" + 
":  " + 
"-0.014540605625786398" + 
":  " + 
"(b('grass') <= 2.972543239593506) ? " + 
"-0.0014573651254409824" + 
":  " + 
"0.04307864765492398" + 
":  " + 
"(b('crop') <= 79.08531951904297) ? " + 
"(b('grass') <= 21.3190860748291) ? " + 
"-0.031280605003199735" + 
":  " + 
"-0.0022443631822368342" + 
":  " + 
"(b('b6') <= 3658.5) ? " + 
"0.04520264406411484" + 
":  " + 
"-0.01928217406854359" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 1335235.5) ? " + 
"(b('g0vv') <= -8.781595706939697) ? " + 
"(b('grass') <= 90.44964218139648) ? " + 
"-0.007861915066161951" + 
":  " + 
"0.02682146089124774" + 
":  " + 
"(b('lia') <= 28.388022422790527) ? " + 
"0.09639621354119829" + 
":  " + 
"0.019002557243248473" + 
":  " + 
"(b('g0vh') <= -18.724651336669922) ? " + 
"(b('moss') <= 17.294462203979492) ? " + 
"0.0008785623510003878" + 
":  " + 
"0.08960314667907514" + 
":  " + 
"(b('urban') <= 0.9290642738342285) ? " + 
"0.03614068319036118" + 
":  " + 
"0.0015708798298366376" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 3467.0) ? " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('grass') <= 0.8429904580116272) ? " + 
"0.003722541938464661" + 
":  " + 
"0.047627663787787065" + 
":  " + 
"(b('grass') <= 3.1685575246810913) ? " + 
"-0.07327029948254636" + 
":  " + 
"-0.004433652027764179" + 
":  " + 
"(b('grass') <= 42.76229476928711) ? " + 
"(b('b3') <= 882.5) ? " + 
"-0.0032994035581758023" + 
":  " + 
"0.02262623419597188" + 
":  " + 
"(b('trees') <= 13.24367094039917) ? " + 
"0.08811649953207293" + 
":  " + 
"-0.015396011829229776" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.474450588226318) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('trees') <= 22.41502571105957) ? " + 
"0.004242491544058424" + 
":  " + 
"-0.04404211266014992" + 
":  " + 
"(b('ndvi') <= 3570.5) ? " + 
"0.04867323650890563" + 
":  " + 
"0.12316427581471073" + 
":  " + 
"(b('crop') <= 44.79741096496582) ? " + 
"(b('lia') <= 30.069137573242188) ? " + 
"0.029744862162903386" + 
":  " + 
"-0.013597307673078096" + 
":  " + 
"(b('g0vv') <= -8.36837100982666) ? " + 
"-0.035160549213551426" + 
":  " + 
"0.019560099718817375" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 352.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"(b('g0vv') <= -9.437768459320068) ? " + 
"-0.006979501279651993" + 
":  " + 
"0.023200015085895028" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.10297059711391826" + 
":  " + 
"0.019809650830599088" + 
":  " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('grass') <= 0.8429904580116272) ? " + 
"0.0024917175802200145" + 
":  " + 
"0.04131686578074882" + 
":  " + 
"(b('grass') <= 3.1685575246810913) ? " + 
"-0.06651570795575507" + 
":  " + 
"-0.004725673384015948" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 800762.5) ? " + 
"(b('g0vv') <= -8.560012340545654) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"-0.00793862433543261" + 
":  " + 
"0.02536384627654106" + 
":  " + 
"(b('grass') <= 16.110694408416748) ? " + 
"0.007977697870505451" + 
":  " + 
"0.04676687864706504" + 
":  " + 
"(b('b5') <= 4653.0) ? " + 
"(b('trees') <= 24.201680183410645) ? " + 
"0.010067347965512839" + 
":  " + 
"-0.06567597644407495" + 
":  " + 
"(b('lia') <= 40.413368225097656) ? " + 
"0.182854694564941" + 
":  " + 
"-0.0746353291694567" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 2.297703742980957) ? " + 
"(b('bare') <= 2.2187036275863647) ? " + 
"(b('g0vh') <= -17.516615867614746) ? " + 
"-0.0027988027516627615" + 
":  " + 
"0.01886964150539887" + 
":  " + 
"(b('b3') <= 1065.0) ? " + 
"0.12374611109042798" + 
":  " + 
"0.06216756195464826" + 
":  " + 
"(b('grass') <= 21.3190860748291) ? " + 
"(b('grass') <= 4.001386761665344) ? " + 
"0.023856471938368373" + 
":  " + 
"-0.02775403314058088" + 
":  " + 
"(b('b7') <= 1354.0) ? " + 
"0.07554023111785935" + 
":  " + 
"-0.004611807755770497" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 24.201680183410645) ? " + 
"(b('b4') <= 1354.5) ? " + 
"(b('urban') <= 20.123075485229492) ? " + 
"0.01034659720126575" + 
":  " + 
"-0.025371022761018335" + 
":  " + 
"(b('lia') <= 42.20660972595215) ? " + 
"-0.011335386584739026" + 
":  " + 
"0.015978041008515687" + 
":  " + 
"(b('g0vv') <= -12.887189388275146) ? " + 
"(b('ndvi') <= 3221.0) ? " + 
"-0.08113962980299466" + 
":  " + 
"-0.022130319260078656" + 
":  " + 
"(b('lia') <= 44.392215728759766) ? " + 
"-0.042443221511814275" + 
":  " + 
"0.02274692044281525" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 1880360.5) ? " + 
"(b('trees') <= 23.231947898864746) ? " + 
"(b('grass') <= 16.658127784729004) ? " + 
"-0.009623383478163383" + 
":  " + 
"0.003974093311653763" + 
":  " + 
"(b('g0vv') <= -11.482315063476562) ? " + 
"-0.0481295682825359" + 
":  " + 
"-0.014320162045357573" + 
":  " + 
"(b('g0vh') <= -18.73760986328125) ? " + 
"(b('l8dt') <= 1884259.5) ? " + 
"0.17642358301484054" + 
":  " + 
"0.0011862143387129467" + 
":  " + 
"(b('urban') <= 1.9267486333847046) ? " + 
"0.034978121809835463" + 
":  " + 
"0.0012843985007628177" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.474450588226318) ? " + 
"(b('g0vh') <= -20.387579917907715) ? " + 
"(b('b4') <= 1167.5) ? " + 
"0.007458525359735596" + 
":  " + 
"-0.012745596070818363" + 
":  " + 
"(b('grass') <= 16.658127784729004) ? " + 
"-0.0031112313591193166" + 
":  " + 
"0.022507321643028818" + 
":  " + 
"(b('bare') <= 11.910642623901367) ? " + 
"(b('moss') <= 22.99738883972168) ? " + 
"-0.022675974556855476" + 
":  " + 
"0.034233246827981685" + 
":  " + 
"(b('ndvi') <= 2094.0) ? " + 
"0.0028043853167460287" + 
":  " + 
"0.12022193083273937" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('grass') <= 0.8429904580116272) ? " + 
"(b('b6') <= 1620.5) ? " + 
"0.11447242777482183" + 
":  " + 
"0.004464937406686881" + 
":  " + 
"(b('b4') <= 2106.0) ? " + 
"0.0423964040242416" + 
":  " + 
"-0.019771954169009596" + 
":  " + 
"(b('grass') <= 3.1685575246810913) ? " + 
"(b('g0vv') <= -8.311199188232422) ? " + 
"-0.060384780251584294" + 
":  " + 
"0.018681421888882818" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.0049129582101324065" + 
":  " + 
"-0.00902723443318522" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('g0vv') <= -9.493937492370605) ? " + 
"(b('b3') <= 627.5) ? " + 
"0.026502337918761512" + 
":  " + 
"-0.0042429839456543" + 
":  " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.0009323464621407797" + 
":  " + 
"0.028053121405097355" + 
":  " + 
"(b('b3') <= 1098.5) ? " + 
"(b('l8dt') <= 2073598.5) ? " + 
"0.1652671956272573" + 
":  " + 
"0.05924479004525092" + 
":  " + 
"(b('bare') <= 0.9388599693775177) ? " + 
"0.016244175977494238" + 
":  " + 
"-0.06044380865627721" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.231947898864746) ? " + 
"(b('b4') <= 2029.0) ? " + 
"(b('urban') <= 22.551812171936035) ? " + 
"0.005034333064103426" + 
":  " + 
"-0.018933005573956066" + 
":  " + 
"(b('lia') <= 42.752872467041016) ? " + 
"-0.019854655839977104" + 
":  " + 
"0.024158968668013966" + 
":  " + 
"(b('crop') <= 1.4046242237091064) ? " + 
"(b('g0vv') <= -10.236309051513672) ? " + 
"-0.0468920659064959" + 
":  " + 
"-0.011650931743416687" + 
":  " + 
"(b('b5') <= 3005.0) ? " + 
"0.05043494777857809" + 
":  " + 
"-0.030852591792254126" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('grass') <= 0.8429904580116272) ? " + 
"(b('b11') <= 1016.5) ? " + 
"0.06058020589993727" + 
":  " + 
"0.0038230426515808926" + 
":  " + 
"(b('b5') <= 3487.5) ? " + 
"0.03987449266679552" + 
":  " + 
"-0.0014933900123756583" + 
":  " + 
"(b('crop') <= 77.83634567260742) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.002153325700051733" + 
":  " + 
"0.048690522619402314" + 
":  " + 
"(b('trees') <= 3.8236643075942993) ? " + 
"-0.042806703879295804" + 
":  " + 
"0.0026166649511839796" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 800762.5) ? " + 
"(b('g0vh') <= -15.113541603088379) ? " + 
"(b('grass') <= 90.44964218139648) ? " + 
"-0.0063733860225451515" + 
":  " + 
"0.019197521775964236" + 
":  " + 
"(b('b3') <= 712.5) ? " + 
"-0.008925599965038153" + 
":  " + 
"0.0314668908861228" + 
":  " + 
"(b('grass') <= 35.55763244628906) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"-0.0015449662062315198" + 
":  " + 
"0.03091969857908164" + 
":  " + 
"(b('b2') <= 436.0) ? " + 
"0.056922401292805326" + 
":  " + 
"0.007802052858630604" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('grass') <= 0.8429904580116272) ? " + 
"0.005371557308260831" + 
":  " + 
"0.029334564001284487" + 
":  " + 
"(b('grass') <= 3.1685575246810913) ? " + 
"-0.048552215314325964" + 
":  " + 
"-0.0008621166128985593" + 
":  " + 
"(b('b4') <= 1028.5) ? " + 
"(b('lia') <= 37.78306770324707) ? " + 
"0.2135847986520484" + 
":  " + 
"0.11472960014022433" + 
":  " + 
"(b('trees') <= 16.78393316268921) ? " + 
"-0.05205901967498142" + 
":  " + 
"0.014968996245594154" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.474450588226318) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('urban') <= 17.62513542175293) ? " + 
"0.003699286299118232" + 
":  " + 
"-0.0157879456002768" + 
":  " + 
"(b('ndvi') <= 3425.0) ? " + 
"0.03289934714975426" + 
":  " + 
"0.09649948388788662" + 
":  " + 
"(b('bare') <= 10.456055164337158) ? " + 
"(b('moss') <= 22.99738883972168) ? " + 
"-0.020283019602917174" + 
":  " + 
"0.031322256049169155" + 
":  " + 
"(b('g0vh') <= -17.27714729309082) ? " + 
"0.015337310039844398" + 
":  " + 
"-0.03575796412868253" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 2353526.5) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"(b('b1') <= 344.5) ? " + 
"0.008311717540391476" + 
":  " + 
"-0.005292236783256487" + 
":  " + 
"(b('g0vv') <= -12.063790321350098) ? " + 
"0.01131850352745306" + 
":  " + 
"0.08530472046481909" + 
":  " + 
"(b('lia') <= 41.31414985656738) ? " + 
"(b('lia') <= 39.101484298706055) ? " + 
"0.01848920867927742" + 
":  " + 
"-0.006424563817547945" + 
":  " + 
"(b('lia') <= 43.210580825805664) ? " + 
"0.05562488991748028" + 
":  " + 
"0.010294809674786404" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.231947898864746) ? " + 
"(b('trees') <= 20.873432159423828) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"-0.006284608882032854" + 
":  " + 
"0.0045854271796023595" + 
":  " + 
"(b('b5') <= 3011.0) ? " + 
"0.06596128983303397" + 
":  " + 
"0.018257027201651062" + 
":  " + 
"(b('g0vv') <= -11.482315063476562) ? " + 
"(b('ndvi') <= 3183.5) ? " + 
"-0.05563888824007063" + 
":  " + 
"-0.016122208963991688" + 
":  " + 
"(b('moss') <= 8.346091270446777) ? " + 
"0.020095991329320495" + 
":  " + 
"-0.02116838225133493" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -10.249711990356445) ? " + 
"(b('b4') <= 561.5) ? " + 
"(b('b6') <= 2319.5) ? " + 
"0.013338967982085956" + 
":  " + 
"0.17598676460066603" + 
":  " + 
"(b('b5') <= 4653.0) ? " + 
"-0.003942570847849573" + 
":  " + 
"0.08438250161188156" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"0.0026650933204455805" + 
":  " + 
"0.03742293163355953" + 
":  " + 
"(b('grass') <= 73.52653503417969) ? " + 
"-0.012179710739022838" + 
":  " + 
"0.08580958169410725" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 468582.0) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"0.011128673977567895" + 
":  " + 
"-0.007527922382272297" + 
":  " + 
"(b('lia') <= 35.73617744445801) ? " + 
"0.03494964984935324" + 
":  " + 
"-0.0228750407062085" + 
":  " + 
"(b('g0vh') <= -20.641429901123047) ? " + 
"(b('moss') <= 7.287195682525635) ? " + 
"-0.01750076546198097" + 
":  " + 
"0.010605629648939517" + 
":  " + 
"(b('grass') <= 34.49201011657715) ? " + 
"0.002359907565005665" + 
":  " + 
"0.023956553329639804" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -11.372849941253662) ? " + 
"(b('b4') <= 561.5) ? " + 
"(b('b6') <= 2052.5) ? " + 
"-0.01433798991385193" + 
":  " + 
"0.11180557586180331" + 
":  " + 
"(b('lia') <= 30.273048400878906) ? " + 
"0.01727326353361568" + 
":  " + 
"-0.00663547047152156" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('urban') <= 22.551812171936035) ? " + 
"0.017215143793915182" + 
":  " + 
"-0.0162833254761262" + 
":  " + 
"(b('grass') <= 73.403076171875) ? " + 
"-0.01110709933322325" + 
":  " + 
"0.05966386731618772" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('grass') <= 0.8429904580116272) ? " + 
"(b('b6') <= 1620.5) ? " + 
"0.0939896997250156" + 
":  " + 
"0.003249558876681142" + 
":  " + 
"(b('b4') <= 2106.0) ? " + 
"0.030685079407647826" + 
":  " + 
"-0.021826666631947798" + 
":  " + 
"(b('crop') <= 89.96376037597656) ? " + 
"(b('crop') <= 85.84851455688477) ? " + 
"-0.0009665310074123023" + 
":  " + 
"0.04532027650714014" + 
":  " + 
"(b('b1') <= 450.5) ? " + 
"-0.06319253332834364" + 
":  " + 
"-0.019960382724805447" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.231947898864746) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"(b('grass') <= 16.658127784729004) ? " + 
"-0.008486694978056762" + 
":  " + 
"0.004584815998242662" + 
":  " + 
"(b('crop') <= 55.285356521606445) ? " + 
"0.0016177815459049137" + 
":  " + 
"0.04850647835982349" + 
":  " + 
"(b('b7') <= 1002.5) ? " + 
"(b('g0vh') <= -19.240538597106934) ? " + 
"-0.07052596033903559" + 
":  " + 
"-0.12101539029267344" + 
":  " + 
"(b('crop') <= 42.75235939025879) ? " + 
"-0.028176304103946948" + 
":  " + 
"0.020339620506284364" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 13.474450588226318) ? " + 
"(b('moss') <= 13.084601402282715) ? " + 
"(b('b5') <= 4653.0) ? " + 
"0.0011841679624244594" + 
":  " + 
"0.07363544969443567" + 
":  " + 
"(b('ndvi') <= 3425.0) ? " + 
"0.030467788425364396" + 
":  " + 
"0.08723072096395258" + 
":  " + 
"(b('bare') <= 11.910642623901367) ? " + 
"(b('moss') <= 22.99738883972168) ? " + 
"-0.01764111490390743" + 
":  " + 
"0.028234429218976474" + 
":  " + 
"(b('ndvi') <= 2005.5) ? " + 
"0.005384481795909913" + 
":  " + 
"0.10173360156616235" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 2353526.5) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"(b('b1') <= 344.5) ? " + 
"0.0065285758877804976" + 
":  " + 
"-0.004331627893188557" + 
":  " + 
"(b('g0vv') <= -12.063790321350098) ? " + 
"0.008910111681035397" + 
":  " + 
"0.07276804247055033" + 
":  " + 
"(b('lia') <= 41.31414985656738) ? " + 
"(b('moss') <= 1.9861568808555603) ? " + 
"0.023947871641954138" + 
":  " + 
"0.0008630431527496743" + 
":  " + 
"(b('lia') <= 43.179250717163086) ? " + 
"0.04987261527440618" + 
":  " + 
"0.010980916999717589" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('grass') <= 0.8429904580116272) ? " + 
"(b('b6') <= 1842.5) ? " + 
"0.03964303242973383" + 
":  " + 
"0.0025880576768611443" + 
":  " + 
"(b('b5') <= 3487.5) ? " + 
"0.030182045206755128" + 
":  " + 
"-0.006229387319198285" + 
":  " + 
"(b('crop') <= 77.83634567260742) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.001874958380471131" + 
":  " + 
"0.04037438045182389" + 
":  " + 
"(b('trees') <= 3.8236643075942993) ? " + 
"-0.033851887436620993" + 
":  " + 
"0.0031000045699714363" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -8.796432495117188) ? " + 
"(b('b4') <= 544.5) ? " + 
"(b('b6') <= 2024.5) ? " + 
"-0.007801844443239855" + 
":  " + 
"0.10010984335788174" + 
":  " + 
"(b('b1') <= 130.0) ? " + 
"-0.11245419751316799" + 
":  " + 
"-0.0016385821741725461" + 
":  " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('moss') <= 7.30760383605957) ? " + 
"-0.008913154641462423" + 
":  " + 
"0.07031229552027775" + 
":  " + 
"(b('bare') <= 3.107935905456543) ? " + 
"0.042948710164254125" + 
":  " + 
"-0.0023814145517412565" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b6') <= 3127.5) ? " + 
"(b('urban') <= 0.9776536226272583) ? " + 
"0.007587287960472711" + 
":  " + 
"-0.008976127473688552" + 
":  " + 
"(b('lia') <= 30.148881912231445) ? " + 
"0.019672716816819986" + 
":  " + 
"-0.006503357391429958" + 
":  " + 
"(b('b4') <= 1028.5) ? " + 
"(b('l8dt') <= 2073598.5) ? " + 
"0.11854752849766127" + 
":  " + 
"0.02336858226414541" + 
":  " + 
"(b('ndvi') <= 4513.0) ? " + 
"-0.05534176987236672" + 
":  " + 
"-0.007043636283790733" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -15.116506576538086) ? " + 
"(b('grass') <= 90.44964218139648) ? " + 
"(b('l8dt') <= 655679.0) ? " + 
"-0.00494832016804038" + 
":  " + 
"0.0030625173705820415" + 
":  " + 
"(b('g0vv') <= -12.421417236328125) ? " + 
"0.006259363164085749" + 
":  " + 
"0.06538256247362248" + 
":  " + 
"(b('b3') <= 665.0) ? " + 
"(b('b5') <= 1927.0) ? " + 
"0.009428197398031354" + 
":  " + 
"-0.04882132170551695" + 
":  " + 
"(b('bare') <= 5.524640083312988) ? " + 
"0.02435006047660233" + 
":  " + 
"-0.01626434841025788" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.231947898864746) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"-0.0072283858902409005" + 
":  " + 
"0.0040535411005029305" + 
":  " + 
"(b('trees') <= 12.0613431930542) ? " + 
"0.04688359349611343" + 
":  " + 
"0.0021607127130750547" + 
":  " + 
"(b('g0vv') <= -11.482315063476562) ? " + 
"(b('ndvi') <= 3183.5) ? " + 
"-0.04513498050658175" + 
":  " + 
"-0.010895308461420583" + 
":  " + 
"(b('b6') <= 1699.5) ? " + 
"-0.10249740723106514" + 
":  " + 
"-0.004023191715664584" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('grass') <= 0.8429904580116272) ? " + 
"(b('b6') <= 1620.5) ? " + 
"0.08105706663845007" + 
":  " + 
"0.0038742361896763754" + 
":  " + 
"(b('b4') <= 2106.0) ? " + 
"0.025646936088512894" + 
":  " + 
"-0.019814293286906676" + 
":  " + 
"(b('grass') <= 3.1685575246810913) ? " + 
"(b('b6') <= 1366.0) ? " + 
"-0.11612493407811866" + 
":  " + 
"-0.03478398783254885" + 
":  " + 
"(b('grass') <= 4.1582722663879395) ? " + 
"0.037234789280755534" + 
":  " + 
"-0.001055457892982459" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 65.5) ? " + 
"(b('l8dt') <= 690100.0) ? " + 
"(b('b2') <= 116.5) ? " + 
"0.06726930803436126" + 
":  " + 
"0.09896445886240357" + 
":  " + 
"(b('l8dt') <= 1014244.5) ? " + 
"0.2015548815717558" + 
":  " + 
"0.17743005289970032" + 
":  " + 
"(b('b1') <= 130.0) ? " + 
"(b('b4') <= 525.5) ? " + 
"0.002987762871105379" + 
":  " + 
"-0.09790571434684171" + 
":  " + 
"(b('moss') <= 13.474450588226318) ? " + 
"0.0019393444527004134" + 
":  " + 
"-0.006728897569834062" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 382124.5) ? " + 
"(b('l8dt') <= 368719.0) ? " + 
"(b('moss') <= 8.152628898620605) ? " + 
"0.0007264736754351966" + 
":  " + 
"-0.008947955457450611" + 
":  " + 
"(b('bare') <= 0.1420118361711502) ? " + 
"-0.06614823198898008" + 
":  " + 
"-0.01589479860712431" + 
":  " + 
"(b('moss') <= 25.491960525512695) ? " + 
"(b('trees') <= 4.231653451919556) ? " + 
"-0.0014861374364873606" + 
":  " + 
"0.007333927880900834" + 
":  " + 
"(b('b5') <= 1801.5) ? " + 
"0.21191731400221941" + 
":  " + 
"0.035852875666589165" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b5') <= 3946.5) ? " + 
"(b('grass') <= 0.8429904580116272) ? " + 
"0.006068683201296966" + 
":  " + 
"0.023021780316030954" + 
":  " + 
"(b('g0vv') <= -11.524848461151123) ? " + 
"0.001580103932397881" + 
":  " + 
"-0.022342224011561794" + 
":  " + 
"(b('crop') <= 77.83634567260742) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.0016464662746572465" + 
":  " + 
"0.03499397607775768" + 
":  " + 
"(b('trees') <= 3.8236643075942993) ? " + 
"-0.02854340960710955" + 
":  " + 
"0.002347339198095212" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('g0vv') <= -11.896080017089844) ? " + 
"(b('b3') <= 642.0) ? " + 
"0.022653066997964426" + 
":  " + 
"-0.00518227248575166" + 
":  " + 
"(b('grass') <= 87.89813995361328) ? " + 
"0.002547880792597909" + 
":  " + 
"0.058526823708530774" + 
":  " + 
"(b('b3') <= 1098.5) ? " + 
"(b('lia') <= 37.78306770324707) ? " + 
"0.16247436906482182" + 
":  " + 
"0.07637313762399016" + 
":  " + 
"(b('ndvi') <= 4513.0) ? " + 
"-0.048403001586763444" + 
":  " + 
"-0.006387274016238009" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('b4') <= 1134.5) ? " + 
"(b('b3') <= 841.5) ? " + 
"0.0011216690368669186" + 
":  " + 
"0.026456566003434535" + 
":  " + 
"(b('lia') <= 30.273048400878906) ? " + 
"0.022073458839121003" + 
":  " + 
"-0.004982370517397487" + 
":  " + 
"(b('b1') <= 440.5) ? " + 
"(b('urban') <= 4.676470994949341) ? " + 
"-0.0308373944015559" + 
":  " + 
"-0.006233192730728865" + 
":  " + 
"(b('b10') <= 2289.5) ? " + 
"0.014846946607952227" + 
":  " + 
"-0.009575259931741086" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 24.201680183410645) ? " + 
"(b('urban') <= 22.551812171936035) ? " + 
"(b('b4') <= 1354.5) ? " + 
"0.0050374762384059165" + 
":  " + 
"-0.00305662945745264" + 
":  " + 
"(b('moss') <= 2.433658003807068) ? " + 
"-0.030434760258668307" + 
":  " + 
"-0.006610667925844326" + 
":  " + 
"(b('b11') <= 1719.0) ? " + 
"(b('b1') <= 492.0) ? " + 
"-0.053563954026879954" + 
":  " + 
"0.018727083061654694" + 
":  " + 
"(b('b6') <= 2763.0) ? " + 
"0.04714648112700186" + 
":  " + 
"-0.023529042178121583" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 10.783052444458008) ? " + 
"(b('moss') <= 13.474450588226318) ? " + 
"(b('moss') <= 13.070855617523193) ? " + 
"0.0003818152009066683" + 
":  " + 
"0.04538637383744572" + 
":  " + 
"(b('lia') <= 43.39015769958496) ? " + 
"-0.009662997734889024" + 
":  " + 
"-0.0612610406877212" + 
":  " + 
"(b('b4') <= 1150.0) ? " + 
"(b('b5') <= 2111.0) ? " + 
"0.01923976172733861" + 
":  " + 
"0.10887100195565969" + 
":  " + 
"(b('g0vh') <= -16.948575019836426) ? " + 
"0.006671832792202867" + 
":  " + 
"-0.026374597589816796" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 2353526.5) ? " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.0005632523470259825" + 
":  " + 
"-0.009915527419586356" + 
":  " + 
"(b('ndvi') <= 3131.0) ? " + 
"0.005288685544952995" + 
":  " + 
"0.11212164428426985" + 
":  " + 
"(b('b5') <= 1429.0) ? " + 
"(b('g0vv') <= -7.2048609256744385) ? " + 
"-0.030497841273028365" + 
":  " + 
"-0.0941138755858213" + 
":  " + 
"(b('g0vh') <= -18.294078826904297) ? " + 
"0.002360809033982856" + 
":  " + 
"0.01838796955070015" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 65.5) ? " + 
"(b('l8dt') <= 690100.0) ? " + 
"(b('ndvi') <= 2890.0) ? " + 
"0.05900842170872045" + 
":  " + 
"0.087151727167257" + 
":  " + 
"(b('g0vh') <= -20.281959533691406) ? " + 
"0.1778549192718388" + 
":  " + 
"0.15714783277725725" + 
":  " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('moss') <= 7.140108346939087) ? " + 
"-0.00867119671674743" + 
":  " + 
"0.010583217269041077" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.014088355328644076" + 
":  " + 
"-0.0028413392434794124" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -15.116506576538086) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"(b('lia') <= 37.147111892700195) ? " + 
"-0.0061717809166542" + 
":  " + 
"0.0012563592675471705" + 
":  " + 
"(b('lia') <= 36.049360275268555) ? " + 
"0.025784145771730195" + 
":  " + 
"-0.019034910801041617" + 
":  " + 
"(b('crop') <= 89.04487609863281) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"0.003354363294272612" + 
":  " + 
"0.03546274788778339" + 
":  " + 
"(b('b6') <= 1857.0) ? " + 
"0.09722428216185224" + 
":  " + 
"-0.03285591979129037" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.231947898864746) ? " + 
"(b('trees') <= 20.873432159423828) ? " + 
"(b('grass') <= 34.49201011657715) ? " + 
"-0.0028730455376742656" + 
":  " + 
"0.004854041422784313" + 
":  " + 
"(b('b5') <= 3011.0) ? " + 
"0.05148986977073868" + 
":  " + 
"0.009282050623435815" + 
":  " + 
"(b('g0vv') <= -11.482315063476562) ? " + 
"(b('ndvi') <= 3183.5) ? " + 
"-0.03774500989223868" + 
":  " + 
"-0.010400094059285936" + 
":  " + 
"(b('b6') <= 3496.5) ? " + 
"-0.006622391912834456" + 
":  " + 
"0.07165355346966373" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -10.747495174407959) ? " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('moss') <= 15.544372081756592) ? " + 
"-0.0019175985747049312" + 
":  " + 
"-0.02371756289454087" + 
":  " + 
"(b('ndvi') <= 2545.5) ? " + 
"0.00619275096266306" + 
":  " + 
"0.08837354721127515" + 
":  " + 
"(b('grass') <= 50.18180274963379) ? " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.008301313762743966" + 
":  " + 
"-0.008773685507148759" + 
":  " + 
"(b('b5') <= 2389.0) ? " + 
"0.008253304946539568" + 
":  " + 
"0.06692727507606434" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('moss') <= 7.140108346939087) ? " + 
"-0.008574392897160579" + 
":  " + 
"0.01031857408323847" + 
":  " + 
"(b('moss') <= 7.337804079055786) ? " + 
"0.012309854089705849" + 
":  " + 
"-0.002856781379531186" + 
":  " + 
"(b('b4') <= 1028.5) ? " + 
"(b('l8dt') <= 2073598.5) ? " + 
"0.09321911596215694" + 
":  " + 
"0.010111604624500748" + 
":  " + 
"(b('grass') <= 7.649911642074585) ? " + 
"-0.04496747962748646" + 
":  " + 
"-0.013193043942527632" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 22.551812171936035) ? " + 
"(b('g0vv') <= -12.077213764190674) ? " + 
"(b('b3') <= 642.0) ? " + 
"0.021687959693297017" + 
":  " + 
"-0.004038653691228961" + 
":  " + 
"(b('grass') <= 73.22198486328125) ? " + 
"0.0027387094721954912" + 
":  " + 
"0.02751452894276367" + 
":  " + 
"(b('moss') <= 2.433658003807068) ? " + 
"(b('b5') <= 1912.5) ? " + 
"0.004443268583941092" + 
":  " + 
"-0.042487008902326345" + 
":  " + 
"(b('g0vh') <= -15.613205909729004) ? " + 
"-0.01232708089730181" + 
":  " + 
"0.018328584588355692" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 2353526.5) ? " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('bare') <= 9.324472427368164) ? " + 
"-0.0016026439338135095" + 
":  " + 
"-0.039463551175870554" + 
":  " + 
"(b('b4') <= 1150.0) ? " + 
"0.06041976041958112" + 
":  " + 
"0.0031302565406474835" + 
":  " + 
"(b('grass') <= 76.81272506713867) ? " + 
"(b('grass') <= 70.14357376098633) ? " + 
"0.00924878713201537" + 
":  " + 
"-0.046685428692291836" + 
":  " + 
"(b('g0vv') <= -13.092808246612549) ? " + 
"0.017546928042263966" + 
":  " + 
"0.13931151711089806" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 65.5) ? " + 
"(b('l8dt') <= 690100.0) ? " + 
"(b('b2') <= 116.5) ? " + 
"0.04565823329493662" + 
":  " + 
"0.07534829226390649" + 
":  " + 
"(b('l8dt') <= 1014244.5) ? " + 
"0.1569811651580301" + 
":  " + 
"0.13929224982396177" + 
":  " + 
"(b('b3') <= 437.0) ? " + 
"(b('b4') <= 499.0) ? " + 
"-0.0280310658493248" + 
":  " + 
"-0.16200293046209982" + 
":  " + 
"(b('b1') <= 130.0) ? " + 
"-0.08133271020353415" + 
":  " + 
"0.0002786074845474808" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 2030.5) ? " + 
"(b('b2') <= 956.5) ? " + 
"(b('lia') <= 37.147111892700195) ? " + 
"-0.005039282682809849" + 
":  " + 
"0.002673137753797312" + 
":  " + 
"(b('bare') <= 0.0628272220492363) ? " + 
"0.07882878493486366" + 
":  " + 
"0.010540247605296307" + 
":  " + 
"(b('l8dt') <= 19345.5) ? " + 
"(b('b5') <= 3281.5) ? " + 
"0.162187269542708" + 
":  " + 
"0.2724496129702265" + 
":  " + 
"(b('lia') <= 42.752872467041016) ? " + 
"-0.01107433114877355" + 
":  " + 
"0.014893371462352341" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 382124.5) ? " + 
"(b('l8dt') <= 368719.0) ? " + 
"(b('grass') <= 98.36243438720703) ? " + 
"-0.0035724981816240716" + 
":  " + 
"0.015042690372349376" + 
":  " + 
"(b('bare') <= 0.1420118361711502) ? " + 
"-0.05855952324893675" + 
":  " + 
"-0.013291268846508943" + 
":  " + 
"(b('moss') <= 25.491960525512695) ? " + 
"(b('trees') <= 4.231653451919556) ? " + 
"-0.0015669940407927964" + 
":  " + 
"0.00615803023566456" + 
":  " + 
"(b('b5') <= 1801.5) ? " + 
"0.1900956205506318" + 
":  " + 
"0.034627429376639325" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.231947898864746) ? " + 
"(b('trees') <= 20.873432159423828) ? " + 
"(b('trees') <= 15.564701080322266) ? " + 
"0.000600809360353365" + 
":  " + 
"-0.026024812434208844" + 
":  " + 
"(b('b5') <= 2131.5) ? " + 
"0.08010277128674279" + 
":  " + 
"0.01673739241403497" + 
":  " + 
"(b('b3') <= 836.0) ? " + 
"(b('b6') <= 2583.0) ? " + 
"-0.018343241445469272" + 
":  " + 
"-0.06232763215260644" + 
":  " + 
"(b('b6') <= 2858.0) ? " + 
"0.02236326771513392" + 
":  " + 
"-0.017719894482078714" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -8.796432495117188) ? " + 
"(b('b4') <= 544.5) ? " + 
"(b('b6') <= 2112.5) ? " + 
"0.0017849279874612104" + 
":  " + 
"0.12246696691969758" + 
":  " + 
"(b('b1') <= 130.0) ? " + 
"-0.07631706690901521" + 
":  " + 
"-0.001160584004353633" + 
":  " + 
"(b('ndvi') <= 4628.0) ? " + 
"(b('bare') <= 3.6172980070114136) ? " + 
"0.01869928646359937" + 
":  " + 
"-0.009750029125971497" + 
":  " + 
"(b('b5') <= 2796.0) ? " + 
"-0.039163169581989114" + 
":  " + 
"0.013003070469952565" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('moss') <= 7.140108346939087) ? " + 
"-0.007465443164219799" + 
":  " + 
"0.008647585737238799" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"0.01152961964888991" + 
":  " + 
"-0.0022855562315408817" + 
":  " + 
"(b('b3') <= 1098.5) ? " + 
"(b('lia') <= 37.78306770324707) ? " + 
"0.13459058115040778" + 
":  " + 
"0.05824754554090972" + 
":  " + 
"(b('crop') <= 69.59964752197266) ? " + 
"-0.012359343319892857" + 
":  " + 
"-0.03922913607356686" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 98.36243438720703) ? " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('trees') <= 4.087827920913696) ? " + 
"-0.011688424626327977" + 
":  " + 
"0.004907471847771668" + 
":  " + 
"(b('moss') <= 7.337804079055786) ? " + 
"0.010130306185422424" + 
":  " + 
"-0.0024971109073024023" + 
":  " + 
"(b('b4') <= 1209.5) ? " + 
"(b('g0vv') <= -15.058745861053467) ? " + 
"0.011129181221758619" + 
":  " + 
"0.05313793116668499" + 
":  " + 
"(b('ndvi') <= 1404.0) ? " + 
"0.03208907362587066" + 
":  " + 
"-0.01706021803547461" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('urban') <= 0.513603001832962) ? " + 
"(b('lia') <= 30.273048400878906) ? " + 
"0.014204386638421813" + 
":  " + 
"-0.0008093532106347974" + 
":  " + 
"(b('ndvi') <= 4263.5) ? " + 
"0.024373986034729227" + 
":  " + 
"0.09838195323305521" + 
":  " + 
"(b('crop') <= 44.1535701751709) ? " + 
"(b('trees') <= 9.817587852478027) ? " + 
"-0.001879663265358813" + 
":  " + 
"0.034883014143094165" + 
":  " + 
"(b('b3') <= 871.5) ? " + 
"-0.017168113695251955" + 
":  " + 
"-3.229628835499948e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 24.454398155212402) ? " + 
"(b('b4') <= 1292.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"-0.0016670759267137182" + 
":  " + 
"0.012370382606795169" + 
":  " + 
"(b('b1') <= 676.5) ? " + 
"-0.0070012616625132916" + 
":  " + 
"0.0032366928660859445" + 
":  " + 
"(b('b1') <= 503.0) ? " + 
"(b('b5') <= 2281.5) ? " + 
"-0.016371334255482685" + 
":  " + 
"-0.06006720158535981" + 
":  " + 
"(b('b6') <= 2763.0) ? " + 
"0.031216598665095383" + 
":  " + 
"-0.011978222333910138" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -10.249711990356445) ? " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('moss') <= 15.544372081756592) ? " + 
"-0.0013988734522122727" + 
":  " + 
"-0.019295932237078837" + 
":  " + 
"(b('ndvi') <= 2155.0) ? " + 
"0.004381815642198501" + 
":  " + 
"0.055522434409418855" + 
":  " + 
"(b('grass') <= 80.8479232788086) ? " + 
"(b('b5') <= 2213.0) ? " + 
"0.016645091835757662" + 
":  " + 
"0.0005287940236940452" + 
":  " + 
"(b('b4') <= 799.5) ? " + 
"0.16179295622471423" + 
":  " + 
"0.038408618985849984" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -11.92972469329834) ? " + 
"(b('b5') <= 2441.5) ? " + 
"(b('b10') <= 2026.5) ? " + 
"-0.01989855399851391" + 
":  " + 
"-0.0006531456860164895" + 
":  " + 
"(b('b3') <= 627.5) ? " + 
"0.050468266457400546" + 
":  " + 
"-0.001344214951924307" + 
":  " + 
"(b('grass') <= 87.89813995361328) ? " + 
"(b('b5') <= 2170.5) ? " + 
"0.012578752204900286" + 
":  " + 
"-0.00018445756795948363" + 
":  " + 
"(b('g0vh') <= -20.57002353668213) ? " + 
"-0.017156723635085015" + 
":  " + 
"0.06145192616416688" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 25.020339012145996) ? " + 
"(b('moss') <= 19.819469451904297) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"-0.00019294949404837557" + 
":  " + 
"0.05231791924515403" + 
":  " + 
"(b('grass') <= 66.96076965332031) ? " + 
"0.015096793176993549" + 
":  " + 
"-0.05770101348641456" + 
":  " + 
"(b('b5') <= 1786.5) ? " + 
"(b('b11') <= 1894.5) ? " + 
"0.06815397491176119" + 
":  " + 
"0.22442222203243004" + 
":  " + 
"(b('b11') <= 2118.0) ? " + 
"0.044841849655872394" + 
":  " + 
"-0.007202165978443111" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 22.551812171936035) ? " + 
"(b('urban') <= 14.72341012954712) ? " + 
"(b('grass') <= 1.8034681677818298) ? " + 
"0.009232775650545802" + 
":  " + 
"-0.0006466830643610847" + 
":  " + 
"(b('g0vh') <= -18.107023239135742) ? " + 
"0.015495362402119222" + 
":  " + 
"0.12796921594714586" + 
":  " + 
"(b('b4') <= 618.0) ? " + 
"(b('g0vh') <= -15.350207328796387) ? " + 
"-0.05570877030364336" + 
":  " + 
"-0.004721791661142859" + 
":  " + 
"(b('moss') <= 2.433658003807068) ? " + 
"-0.020071799777551677" + 
":  " + 
"-0.00366312103329692" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 2030.5) ? " + 
"(b('b2') <= 956.5) ? " + 
"(b('lia') <= 37.147111892700195) ? " + 
"-0.0046879563670651015" + 
":  " + 
"0.002540972641713961" + 
":  " + 
"(b('bare') <= 0.0628272220492363) ? " + 
"0.07101654909451581" + 
":  " + 
"0.00911121185116931" + 
":  " + 
"(b('l8dt') <= 19345.5) ? " + 
"(b('ndvi') <= 2005.0) ? " + 
"0.2475328281271341" + 
":  " + 
"0.14675310513335393" + 
":  " + 
"(b('lia') <= 42.752872467041016) ? " + 
"-0.009939649387081894" + 
":  " + 
"0.012874687185743134" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 3124.5) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"0.000946581945874213" + 
":  " + 
"0.04617259153084475" + 
":  " + 
"(b('b3') <= 727.5) ? " + 
"-0.049709133605636044" + 
":  " + 
"-0.0018984507102455196" + 
":  " + 
"(b('b4') <= 1028.5) ? " + 
"(b('l8dt') <= 2073598.5) ? " + 
"0.07818885850639319" + 
":  " + 
"0.005277981923559572" + 
":  " + 
"(b('trees') <= 11.505031108856201) ? " + 
"-0.03515366032971025" + 
":  " + 
"-0.010319595586827162" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 68.5) ? " + 
"(b('l8dt') <= 690100.0) ? " + 
"(b('g0vv') <= -11.082416534423828) ? " + 
"0.06115882291694072" + 
":  " + 
"0.026914996962396354" + 
":  " + 
"(b('g0vh') <= -20.281959533691406) ? " + 
"0.13951108043235366" + 
":  " + 
"0.12196719132152142" + 
":  " + 
"(b('b3') <= 437.0) ? " + 
"(b('b10') <= 918.5) ? " + 
"-0.02668269356665112" + 
":  " + 
"-0.14604336186201655" + 
":  " + 
"(b('b1') <= 130.0) ? " + 
"-0.06848917689846702" + 
":  " + 
"0.00023661838798121895" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -15.116506576538086) ? " + 
"(b('b3') <= 684.5) ? " + 
"(b('b6') <= 2646.0) ? " + 
"-0.003084838632830897" + 
":  " + 
"0.08957517219420107" + 
":  " + 
"(b('b7') <= 1013.5) ? " + 
"0.05864902446675134" + 
":  " + 
"-0.0017561332204812906" + 
":  " + 
"(b('b3') <= 665.0) ? " + 
"(b('b5') <= 1927.0) ? " + 
"0.004866828025586926" + 
":  " + 
"-0.04044005081806808" + 
":  " + 
"(b('trees') <= 4.132562160491943) ? " + 
"0.004515079746102727" + 
":  " + 
"0.025458629498119934" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 2957789.5) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"-0.006246383894297957" + 
":  " + 
"0.023170059147585187" + 
":  " + 
"(b('crop') <= 71.31087875366211) ? " + 
"-0.00047201424734604174" + 
":  " + 
"0.025372834909439413" + 
":  " + 
"(b('moss') <= 1.9861568808555603) ? " + 
"(b('crop') <= 89.7787094116211) ? " + 
"0.04109143396627103" + 
":  " + 
"0.007009239778983053" + 
":  " + 
"(b('ndvi') <= 5329.0) ? " + 
"0.004603871109058135" + 
":  " + 
"-0.04381174947610213" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('moss') <= 7.30760383605957) ? " + 
"(b('trees') <= 0.9217877388000488) ? " + 
"-0.014241240679845873" + 
":  " + 
"0.0026249443704318785" + 
":  " + 
"(b('moss') <= 7.598436594009399) ? " + 
"0.06738178419637363" + 
":  " + 
"-0.0012493672879561532" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('g0vh') <= -16.614316940307617) ? " + 
"0.004779648707443037" + 
":  " + 
"0.027832473085967254" + 
":  " + 
"(b('crop') <= 48.535308837890625) ? " + 
"0.0016734752930843584" + 
":  " + 
"-0.011813504512674874" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 98.36243438720703) ? " + 
"(b('grass') <= 62.543413162231445) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"-0.0011894396587159848" + 
":  " + 
"0.02677782864734975" + 
":  " + 
"(b('crop') <= 32.0) ? " + 
"-0.001765708434222303" + 
":  " + 
"-0.1101078579170206" + 
":  " + 
"(b('lia') <= 36.049360275268555) ? " + 
"(b('lia') <= 26.987869262695312) ? " + 
"-0.016356753881318405" + 
":  " + 
"0.030036503233057617" + 
":  " + 
"(b('b4') <= 1174.0) ? " + 
"0.013946690192574308" + 
":  " + 
"-0.033245420567580654" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.231947898864746) ? " + 
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('b4') <= 1185.5) ? " + 
"0.006883886832361539" + 
":  " + 
"-0.0019057334478850667" + 
":  " + 
"(b('b1') <= 436.5) ? " + 
"-0.009839570681056247" + 
":  " + 
"0.002367538108621505" + 
":  " + 
"(b('trees') <= 40.03965091705322) ? " + 
"(b('g0vv') <= -12.875124454498291) ? " + 
"-0.02492423846801071" + 
":  " + 
"-0.0040681727914649015" + 
":  " + 
"(b('b2') <= 291.5) ? " + 
"0.06208123253300124" + 
":  " + 
"-0.07278733835705888" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('b10') <= 1328.5) ? " + 
"(b('b4') <= 601.5) ? " + 
"0.013903097093420337" + 
":  " + 
"-0.04785003302264666" + 
":  " + 
"(b('b2') <= 413.5) ? " + 
"0.04960506853382618" + 
":  " + 
"-0.003888591385036165" + 
":  " + 
"(b('moss') <= 1.9861568808555603) ? " + 
"(b('b5') <= 3219.0) ? " + 
"0.019375222233304432" + 
":  " + 
"-0.004237993694702141" + 
":  " + 
"(b('moss') <= 3.2275424003601074) ? " + 
"-0.01728163712798386" + 
":  " + 
"0.0019652625459052157" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 4386.5) ? " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"-0.0026880050741194994" + 
":  " + 
"0.0022516534875857666" + 
":  " + 
"(b('b3') <= 1056.5) ? " + 
"-0.07501081203580359" + 
":  " + 
"-0.025587780173445904" + 
":  " + 
"(b('b3') <= 1098.5) ? " + 
"(b('lia') <= 37.78306770324707) ? " + 
"0.11627598879028671" + 
":  " + 
"0.048359331743390126" + 
":  " + 
"(b('l8dt') <= 150658.0) ? " + 
"-0.008508851161960117" + 
":  " + 
"-0.02832310579351432" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 99.8344841003418) ? " + 
"(b('moss') <= 0.04188481718301773) ? " + 
"(b('trees') <= 0.4900990128517151) ? " + 
"-0.017388507034126192" + 
":  " + 
"0.002982628455630792" + 
":  " + 
"(b('moss') <= 1.9861568808555603) ? " + 
"0.023142770444786357" + 
":  " + 
"-0.0010060855930655763" + 
":  " + 
"(b('lia') <= 36.049360275268555) ? " + 
"(b('lia') <= 28.30226421356201) ? " + 
"-0.014187301062408134" + 
":  " + 
"0.03140464247373739" + 
":  " + 
"(b('b4') <= 1174.0) ? " + 
"0.012008878003733962" + 
":  " + 
"-0.029615467837879803" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b5') <= 3946.5) ? " + 
"(b('b5') <= 3848.0) ? " + 
"0.007502639954734947" + 
":  " + 
"0.052294398354170386" + 
":  " + 
"(b('g0vv') <= -11.524848461151123) ? " + 
"0.0022045939536821874" + 
":  " + 
"-0.02124395460648522" + 
":  " + 
"(b('crop') <= 77.41421890258789) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.0011149072284112051" + 
":  " + 
"0.025443269287199772" + 
":  " + 
"(b('trees') <= 3.8236643075942993) ? " + 
"-0.019299241007679786" + 
":  " + 
"0.0005380123788740254" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 24.454398155212402) ? " + 
"(b('l8dt') <= 361813.5) ? " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-0.004201891326156092" + 
":  " + 
"0.00484456012092802" + 
":  " + 
"(b('l8dt') <= 362191.5) ? " + 
"0.07547553551929037" + 
":  " + 
"0.0018256246915183127" + 
":  " + 
"(b('b7') <= 1719.0) ? " + 
"(b('b1') <= 492.0) ? " + 
"-0.04624854705962972" + 
":  " + 
"0.01605543756769787" + 
":  " + 
"(b('b6') <= 2763.0) ? " + 
"0.042209946425212565" + 
":  " + 
"-0.01674542236101393" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 15.564701080322266) ? " + 
"(b('trees') <= 15.104385375976562) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"-0.0034160437944390095" + 
":  " + 
"0.002838477327333843" + 
":  " + 
"(b('b5') <= 3027.5) ? " + 
"0.18310643178082972" + 
":  " + 
"-0.005334779071126859" + 
":  " + 
"(b('trees') <= 17.320652961730957) ? " + 
"(b('b5') <= 2487.5) ? " + 
"-0.041852382011049" + 
":  " + 
"-0.09761414831431317" + 
":  " + 
"(b('crop') <= 2.0734140276908875) ? " + 
"-0.01609728283925921" + 
":  " + 
"0.008534491736743281" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b3') <= 1607.5) ? " + 
"(b('crop') <= 72.66402816772461) ? " + 
"-0.0039034336543059263" + 
":  " + 
"0.012813236611220611" + 
":  " + 
"(b('g0vv') <= -11.073793411254883) ? " + 
"0.004181293753921248" + 
":  " + 
"-0.02005360635698829" + 
":  " + 
"(b('grass') <= 3.1685575246810913) ? " + 
"(b('lia') <= 41.84072494506836) ? " + 
"-0.017939695990207775" + 
":  " + 
"-0.050316922394878914" + 
":  " + 
"(b('grass') <= 4.1582722663879395) ? " + 
"0.023454117980474743" + 
":  " + 
"-0.000578779385347997" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 68.5) ? " + 
"(b('l8dt') <= 690100.0) ? " + 
"(b('b5') <= 1719.5) ? " + 
"0.05252949619560144" + 
":  " + 
"0.019979839601079574" + 
":  " + 
"(b('l8dt') <= 1014244.5) ? " + 
"0.12135648067482763" + 
":  " + 
"0.10616387220245432" + 
":  " + 
"(b('b3') <= 437.0) ? " + 
"(b('b3') <= 424.0) ? " + 
"-0.030699327900920427" + 
":  " + 
"-0.16497866137975623" + 
":  " + 
"(b('b4') <= 544.5) ? " + 
"0.021840270812011345" + 
":  " + 
"-0.00025004994139533795" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -8.007503509521484) ? " + 
"(b('ndvi') <= 2098.5) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"-0.0031657069043638073" + 
":  " + 
"0.045397154064480416" + 
":  " + 
"(b('grass') <= 46.59696388244629) ? " + 
"-0.0027203639430529855" + 
":  " + 
"0.013289747625850187" + 
":  " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('moss') <= 7.30760383605957) ? " + 
"-0.008539603293654692" + 
":  " + 
"0.054276200403440604" + 
":  " + 
"(b('b5') <= 2260.0) ? " + 
"0.0564328925184155" + 
":  " + 
"0.011362336170692862" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 15.706994533538818) ? " + 
"(b('g0vh') <= -20.387579917907715) ? " + 
"(b('b7') <= 1395.5) ? " + 
"-0.029738676443344787" + 
":  " + 
"-0.0015386312291474909" + 
":  " + 
"(b('grass') <= 46.59696388244629) ? " + 
"-0.0005895261856370001" + 
":  " + 
"0.01889567156844945" + 
":  " + 
"(b('b2') <= 553.0) ? " + 
"(b('ndvi') <= 3358.5) ? " + 
"-0.04418405049956421" + 
":  " + 
"0.060005282310596" + 
":  " + 
"(b('grass') <= 80.30580139160156) ? " + 
"0.003277763094305415" + 
":  " + 
"-0.04477081600443439" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 12.501765251159668) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"(b('b3') <= 684.5) ? " + 
"0.010471915144427801" + 
":  " + 
"-0.0015610019928120145" + 
":  " + 
"(b('g0vv') <= -10.868317127227783) ? " + 
"0.014138830462464799" + 
":  " + 
"0.060471833839521906" + 
":  " + 
"(b('grass') <= 19.990763664245605) ? " + 
"(b('b5') <= 3011.0) ? " + 
"0.04720793252838386" + 
":  " + 
"-0.007931067049751788" + 
":  " + 
"(b('lia') <= 30.064973831176758) ? " + 
"0.034042741810432604" + 
":  " + 
"-0.013853863605180665" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 377.5) ? " + 
"(b('b6') <= 2714.0) ? " + 
"(b('g0vv') <= -15.372703075408936) ? " + 
"-0.08769074484728111" + 
":  " + 
"-0.009530883484542186" + 
":  " + 
"(b('b5') <= 3179.5) ? " + 
"0.09419607125117894" + 
":  " + 
"-0.14282962315443867" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('b6') <= 2448.0) ? " + 
"0.004794086969336445" + 
":  " + 
"0.07643307922674872" + 
":  " + 
"(b('g0vv') <= -8.144237041473389) ? " + 
"-0.0007542891548107844" + 
":  " + 
"0.010252842786372484" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 10.783052444458008) ? " + 
"(b('moss') <= 13.891517639160156) ? " + 
"(b('bare') <= 5.53663182258606) ? " + 
"0.0018567286419768512" + 
":  " + 
"-0.01052374983215314" + 
":  " + 
"(b('b4') <= 1040.5) ? " + 
"-0.020825113888173503" + 
":  " + 
"0.000720246978502312" + 
":  " + 
"(b('ndvi') <= 3131.0) ? " + 
"(b('ndvi') <= 1529.0) ? " + 
"-0.0007046594314105666" + 
":  " + 
"0.015914385135249367" + 
":  " + 
"(b('b4') <= 707.5) ? " + 
"0.16020907596381195" + 
":  " + 
"0.05357531265429955" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('trees') <= 12.893048286437988) ? " + 
"-0.0012978805778131174" + 
":  " + 
"-0.01701941832364046" + 
":  " + 
"(b('grass') <= 90.44964218139648) ? " + 
"0.0009962571822028476" + 
":  " + 
"0.0338176943185507" + 
":  " + 
"(b('b3') <= 1098.5) ? " + 
"(b('g0vv') <= -13.43687915802002) ? " + 
"0.06726797534067153" + 
":  " + 
"0.010678258653031894" + 
":  " + 
"(b('l8dt') <= 44198.5) ? " + 
"0.0010849862134435506" + 
":  " + 
"-0.023059855362773992" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('b2') <= 945.5) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"-0.004543805515703441" + 
":  " + 
"0.03634956114625532" + 
":  " + 
"(b('b4') <= 2055.0) ? " + 
"0.05355121219654692" + 
":  " + 
"-0.009356670986002055" + 
":  " + 
"(b('trees') <= 0.1420118361711502) ? " + 
"(b('b10') <= 2109.5) ? " + 
"0.02401566546649285" + 
":  " + 
"0.003040787372989534" + 
":  " + 
"(b('b4') <= 787.0) ? " + 
"0.010831860611669873" + 
":  " + 
"-0.00475671071430715" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 37.147111892700195) ? " + 
"(b('lia') <= 36.9949893951416) ? " + 
"(b('b3') <= 882.5) ? " + 
"-0.006681539189935869" + 
":  " + 
"0.0019646887474807037" + 
":  " + 
"(b('moss') <= 2.596715211868286) ? " + 
"-0.0888345408409433" + 
":  " + 
"-0.00909251318486951" + 
":  " + 
"(b('lia') <= 37.2614631652832) ? " + 
"(b('b3') <= 674.5) ? " + 
"0.09767197976104272" + 
":  " + 
"0.012600240992278378" + 
":  " + 
"(b('lia') <= 39.11750793457031) ? " + 
"0.006733116012573356" + 
":  " + 
"-0.0009706015131254724" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 377.5) ? " + 
"(b('b6') <= 2714.0) ? " + 
"(b('g0vv') <= -15.372703075408936) ? " + 
"-0.07870774282956282" + 
":  " + 
"-0.008528059753799219" + 
":  " + 
"(b('b5') <= 3179.5) ? " + 
"0.0822365265806338" + 
":  " + 
"-0.1251345060109448" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('crop') <= 43.6307487487793) ? " + 
"0.06721223766566471" + 
":  " + 
"0.002159743004488287" + 
":  " + 
"(b('b1') <= 252.0) ? " + 
"-0.053178980465007374" + 
":  " + 
"1.768300071998689e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 65.5) ? " + 
"(b('l8dt') <= 690100.0) ? " + 
"(b('grass') <= 30.50802230834961) ? " + 
"0.01417105552869502" + 
":  " + 
"0.06226146546268185" + 
":  " + 
"(b('l8dt') <= 1014244.5) ? " + 
"0.11202034520250775" + 
":  " + 
"0.0933688558881915" + 
":  " + 
"(b('b3') <= 437.0) ? " + 
"(b('b5') <= 1717.5) ? " + 
"-0.023672235828254624" + 
":  " + 
"-0.1309814747547925" + 
":  " + 
"(b('b3') <= 520.0) ? " + 
"0.023959519165211607" + 
":  " + 
"-0.000180317425899198" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 75.35467147827148) ? " + 
"(b('b4') <= 2030.5) ? " + 
"(b('b2') <= 908.5) ? " + 
"-0.0006270643314394933" + 
":  " + 
"0.015592841787724618" + 
":  " + 
"(b('ndvi') <= 3478.5) ? " + 
"-0.006881024897380656" + 
":  " + 
"0.04198687220228298" + 
":  " + 
"(b('grass') <= 1.8120805025100708) ? " + 
"(b('b5') <= 3727.5) ? " + 
"-0.0068254448279844475" + 
":  " + 
"0.010032680831435912" + 
":  " + 
"(b('b6') <= 3242.5) ? " + 
"0.09047385323822417" + 
":  " + 
"0.03221532915423714" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 15.706994533538818) ? " + 
"(b('lia') <= 37.147111892700195) ? " + 
"(b('lia') <= 36.90300941467285) ? " + 
"-0.0010561699851463636" + 
":  " + 
"-0.03763042048522164" + 
":  " + 
"(b('lia') <= 39.105838775634766) ? " + 
"0.009555468176810383" + 
":  " + 
"-5.2445841230802455e-05" + 
":  " + 
"(b('lia') <= 30.271445274353027) ? " + 
"(b('grass') <= 80.47436141967773) ? " + 
"0.031654556417492305" + 
":  " + 
"-0.07867034085391209" + 
":  " + 
"(b('b2') <= 580.0) ? " + 
"-0.028232759173279998" + 
":  " + 
"-0.0040087233349804284" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -11.92972469329834) ? " + 
"(b('b5') <= 2590.5) ? " + 
"(b('b11') <= 1329.5) ? " + 
"-0.032386985320321277" + 
":  " + 
"-0.004277140044669457" + 
":  " + 
"(b('b3') <= 627.5) ? " + 
"0.05767706903345882" + 
":  " + 
"2.835965335695653e-05" + 
":  " + 
"(b('b5') <= 2161.0) ? " + 
"(b('moss') <= 22.17501163482666) ? " + 
"0.009025621082382066" + 
":  " + 
"0.12382044284495175" + 
":  " + 
"(b('grass') <= 34.49201011657715) ? " + 
"-0.0018455517250837057" + 
":  " + 
"0.012455488938812948" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b10') <= 1016.5) ? " + 
"(b('b2') <= 265.5) ? " + 
"-0.03388278465232543" + 
":  " + 
"0.06423929094366765" + 
":  " + 
"(b('b6') <= 1724.5) ? " + 
"-0.05970066743620613" + 
":  " + 
"0.004987708362919646" + 
":  " + 
"(b('grass') <= 5.3386664390563965) ? " + 
"(b('lia') <= 39.11960411071777) ? " + 
"0.008515334715680126" + 
":  " + 
"-0.01844213210488562" + 
":  " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.001173266170440475" + 
":  " + 
"0.007009546974850561" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('b2') <= 945.5) ? " + 
"(b('trees') <= 4.087827920913696) ? " + 
"-0.008276607812456272" + 
":  " + 
"0.002448435792013556" + 
":  " + 
"(b('b4') <= 2055.0) ? " + 
"0.04662095791126229" + 
":  " + 
"-0.007694737728398" + 
":  " + 
"(b('moss') <= 8.152628898620605) ? " + 
"(b('b6') <= 2851.0) ? " + 
"0.01452531747263345" + 
":  " + 
"0.0007342138907740405" + 
":  " + 
"(b('moss') <= 9.917112350463867) ? " + 
"-0.01614770484362452" + 
":  " + 
"0.0008730724655003219" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 99.8344841003418) ? " + 
"(b('grass') <= 61.717172622680664) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"-0.0006969931856329987" + 
":  " + 
"0.019902741908740303" + 
":  " + 
"(b('crop') <= 32.0) ? " + 
"-0.0014861404973063898" + 
":  " + 
"-0.08857115406177979" + 
":  " + 
"(b('lia') <= 36.049360275268555) ? " + 
"(b('lia') <= 26.987869262695312) ? " + 
"-0.014370969040457739" + 
":  " + 
"0.027192837220686123" + 
":  " + 
"(b('b4') <= 1174.0) ? " + 
"0.01100737927874161" + 
":  " + 
"-0.025571570494650885" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 377.5) ? " + 
"(b('b6') <= 2714.0) ? " + 
"(b('b6') <= 2288.0) ? " + 
"-0.0035839053013423617" + 
":  " + 
"-0.03646971999435959" + 
":  " + 
"(b('b3') <= 647.5) ? " + 
"0.07052284051514769" + 
":  " + 
"-0.11312388165749465" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('b5') <= 2489.0) ? " + 
"-0.021758397471271066" + 
":  " + 
"0.04001159593060349" + 
":  " + 
"(b('b1') <= 258.5) ? " + 
"-0.0392564356893658" + 
":  " + 
"0.00013867075685641052" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 4370.5) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.0013244149359346712" + 
":  " + 
"0.0032855247015620166" + 
":  " + 
"(b('ndvi') <= 4581.5) ? " + 
"-0.022351143858066597" + 
":  " + 
"-0.07538403012632554" + 
":  " + 
"(b('b3') <= 1098.5) ? " + 
"(b('l8dt') <= 2073598.5) ? " + 
"0.05875164906890879" + 
":  " + 
"-0.0011840556477230035" + 
":  " + 
"(b('l8dt') <= 44198.5) ? " + 
"0.0017303347801359836" + 
":  " + 
"-0.017792539025134224" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 24.454398155212402) ? " + 
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('urban') <= 0.513603001832962) ? " + 
"0.0007440547462075595" + 
":  " + 
"0.026800966854915863" + 
":  " + 
"(b('b5') <= 2568.75) ? " + 
"0.0026567037165108175" + 
":  " + 
"-0.008306242427940622" + 
":  " + 
"(b('b7') <= 1719.0) ? " + 
"(b('b1') <= 492.0) ? " + 
"-0.038759135946124845" + 
":  " + 
"0.01638406882455545" + 
":  " + 
"(b('b6') <= 2763.0) ? " + 
"0.03955736765207197" + 
":  " + 
"-0.014974253658116755" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('moss') <= 14.924424648284912) ? " + 
"-0.0016519744178046909" + 
":  " + 
"-0.02818610064134238" + 
":  " + 
"(b('b11') <= 2383.0) ? " + 
"0.023993554743396837" + 
":  " + 
"0.11263253541394483" + 
":  " + 
"(b('b6') <= 1944.0) ? " + 
"(b('b6') <= 1886.5) ? " + 
"0.012043908091445699" + 
":  " + 
"0.07408630313461134" + 
":  " + 
"(b('trees') <= 0.1420118361711502) ? " + 
"0.006449688418494429" + 
":  " + 
"-0.0024944396958366667" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 99.8344841003418) ? " + 
"(b('lia') <= 37.147111892700195) ? " + 
"(b('lia') <= 37.138017654418945) ? " + 
"-0.0027765126436310027" + 
":  " + 
"-0.05010552199751563" + 
":  " + 
"(b('lia') <= 37.2614631652832) ? " + 
"0.02701615055166901" + 
":  " + 
"0.000777551258733777" + 
":  " + 
"(b('b4') <= 1209.5) ? " + 
"(b('g0vv') <= -16.284887313842773) ? " + 
"-0.0019145651746035552" + 
":  " + 
"0.03367377768457671" + 
":  " + 
"(b('ndvi') <= 1406.0) ? " + 
"0.025212473175408028" + 
":  " + 
"-0.014386353596760092" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('b10') <= 1328.5) ? " + 
"(b('b4') <= 601.5) ? " + 
"0.009798274620319847" + 
":  " + 
"-0.03585192518979275" + 
":  " + 
"(b('b4') <= 758.5) ? " + 
"0.030064621870428094" + 
":  " + 
"-0.003314881058425655" + 
":  " + 
"(b('trees') <= 8.786274433135986) ? " + 
"(b('grass') <= 90.44964218139648) ? " + 
"-0.0016128077827497452" + 
":  " + 
"0.028605890381977094" + 
":  " + 
"(b('urban') <= 14.72341012954712) ? " + 
"0.005661507633231336" + 
":  " + 
"0.07182160615912721" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -14.666974544525146) ? " + 
"(b('b5') <= 1935.5) ? " + 
"(b('moss') <= 24.448779106140137) ? " + 
"0.004815881262731691" + 
":  " + 
"0.08207629676729135" + 
":  " + 
"(b('b5') <= 2315.5) ? " + 
"-0.006263771112247034" + 
":  " + 
"0.00029384285008336746" + 
":  " + 
"(b('crop') <= 93.26061248779297) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"0.0015640165981293443" + 
":  " + 
"0.027210184492819197" + 
":  " + 
"(b('b4') <= 1198.5) ? " + 
"-0.042716624998612604" + 
":  " + 
"0.01867816358639994" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 375.5) ? " + 
"(b('b6') <= 2714.0) ? " + 
"(b('g0vv') <= -15.372703075408936) ? " + 
"-0.0676708692239762" + 
":  " + 
"-0.007640779915187531" + 
":  " + 
"(b('moss') <= 12.535022735595703) ? " + 
"0.061389563030268074" + 
":  " + 
"-0.10376995569093116" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"0.0008281133091060157" + 
":  " + 
"0.05299722563597407" + 
":  " + 
"(b('g0vv') <= -8.144237041473389) ? " + 
"-0.0004818438013790073" + 
":  " + 
"0.0084895880359277" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -3.308971643447876) ? " + 
"(b('b5') <= 1935.5) ? " + 
"(b('b3') <= 1026.5) ? " + 
"0.004904029210501631" + 
":  " + 
"0.06406413750658016" + 
":  " + 
"(b('b5') <= 2315.5) ? " + 
"-0.005357535420659065" + 
":  " + 
"0.0006405617050445192" + 
":  " + 
"(b('crop') <= 89.71894836425781) ? " + 
"(b('g0vv') <= -3.1440563201904297) ? " + 
"-0.07543629494135586" + 
":  " + 
"0.0008944134454612618" + 
":  " + 
"(b('grass') <= 1.6218153238296509) ? " + 
"-0.03627208308399059" + 
":  " + 
"-0.07614563760628384" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 68.5) ? " + 
"(b('l8dt') <= 690100.0) ? " + 
"(b('g0vh') <= -21.020716667175293) ? " + 
"0.07400458187806264" + 
":  " + 
"0.03129153323965122" + 
":  " + 
"(b('g0vh') <= -20.281959533691406) ? " + 
"0.1010707911271142" + 
":  " + 
"0.08242065877344878" + 
":  " + 
"(b('b3') <= 437.0) ? " + 
"(b('b4') <= 461.0) ? " + 
"-0.01440669022591832" + 
":  " + 
"-0.08698713951118267" + 
":  " + 
"(b('b1') <= 130.0) ? " + 
"-0.04776577287325925" + 
":  " + 
"0.00014873727872636599" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('b4') <= 2030.5) ? " + 
"(b('b3') <= 1470.5) ? " + 
"-0.0002645684587308904" + 
":  " + 
"0.01895449347352609" + 
":  " + 
"(b('l8dt') <= 19345.5) ? " + 
"0.17634275414137593" + 
":  " + 
"-0.006041618097357563" + 
":  " + 
"(b('grass') <= 1.8120805025100708) ? " + 
"(b('b2') <= 1416.0) ? " + 
"0.022326385154116137" + 
":  " + 
"-0.0011648520366739643" + 
":  " + 
"(b('b4') <= 2106.5) ? " + 
"0.09922180604515826" + 
":  " + 
"0.02566561648493938" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 4370.5) ? " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"-0.0020734165450507825" + 
":  " + 
"0.001747945355542568" + 
":  " + 
"(b('b2') <= 566.5) ? " + 
"-0.06110256297503808" + 
":  " + 
"-0.01888876061406333" + 
":  " + 
"(b('b4') <= 924.5) ? " + 
"(b('ndvi') <= 5908.5) ? " + 
"0.09702507136831093" + 
":  " + 
"0.034095941097402084" + 
":  " + 
"(b('g0vh') <= -13.574585437774658) ? " + 
"-0.014141125637767721" + 
":  " + 
"0.01526153054882362" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 15.706994533538818) ? " + 
"(b('moss') <= 14.076149940490723) ? " + 
"(b('moss') <= 13.959776878356934) ? " + 
"0.0007119609040371141" + 
":  " + 
"-0.015365144384493063" + 
":  " + 
"(b('ndvi') <= 3315.5) ? " + 
"0.022259164776187803" + 
":  " + 
"-0.021760642574777958" + 
":  " + 
"(b('lia') <= 30.271445274353027) ? " + 
"(b('grass') <= 80.47436141967773) ? " + 
"0.02795624773871292" + 
":  " + 
"-0.07011890001477825" + 
":  " + 
"(b('b1') <= 455.0) ? " + 
"-0.026105030086756027" + 
":  " + 
"-0.003915285217321883" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3390323.5) ? " + 
"(b('b5') <= 1808.5) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"0.006870537619763605" + 
":  " + 
"0.17092315324332671" + 
":  " + 
"(b('b4') <= 529.0) ? " + 
"0.023111668279829824" + 
":  " + 
"-0.0010012984772249168" + 
":  " + 
"(b('b3') <= 552.5) ? " + 
"(b('ndvi') <= 3455.0) ? " + 
"-0.010626973998287046" + 
":  " + 
"-0.0660372678705468" + 
":  " + 
"(b('b5') <= 2049.5) ? " + 
"0.038604906990286014" + 
":  " + 
"0.008790027726887887" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 98.36243438720703) ? " + 
"(b('lia') <= 37.147111892700195) ? " + 
"(b('lia') <= 37.033138275146484) ? " + 
"-0.002188009560238342" + 
":  " + 
"-0.0290430413552316" + 
":  " + 
"(b('b4') <= 1662.5) ? " + 
"0.0034182517283995392" + 
":  " + 
"-0.003537559773069891" + 
":  " + 
"(b('b4') <= 1209.5) ? " + 
"(b('g0vv') <= -15.058745861053467) ? " + 
"0.0060113268826231065" + 
":  " + 
"0.03565683729639349" + 
":  " + 
"(b('ndvi') <= 1404.0) ? " + 
"0.02261052263497715" + 
":  " + 
"-0.013867583821968305" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 23.231947898864746) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"(b('trees') <= 11.076036930084229) ? " + 
"-0.00011428476286311124" + 
":  " + 
"-0.01882546080500816" + 
":  " + 
"(b('trees') <= 12.0613431930542) ? " + 
"0.028204961074735132" + 
":  " + 
"0.00045131078916396856" + 
":  " + 
"(b('b11') <= 1002.5) ? " + 
"(b('lia') <= 39.137529373168945) ? " + 
"-0.07748632579979929" + 
":  " + 
"-0.022356856916782644" + 
":  " + 
"(b('b10') <= 1348.0) ? " + 
"0.036353325227095945" + 
":  " + 
"-0.010974698876389861" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -11.412848949432373) ? " + 
"(b('b5') <= 2652.5) ? " + 
"(b('b11') <= 1329.5) ? " + 
"-0.024322503220642364" + 
":  " + 
"-0.0028964697093448936" + 
":  " + 
"(b('b3') <= 627.5) ? " + 
"0.04699931306820629" + 
":  " + 
"0.0003540645051056015" + 
":  " + 
"(b('b5') <= 2161.0) ? " + 
"(b('moss') <= 21.151470184326172) ? " + 
"0.010120764739257293" + 
":  " + 
"0.1333528924138687" + 
":  " + 
"(b('grass') <= 31.86778163909912) ? " + 
"-0.0017683011173545966" + 
":  " + 
"0.011441577666822545" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('moss') <= 7.30760383605957) ? " + 
"(b('moss') <= 6.624295234680176) ? " + 
"-0.003059908867277489" + 
":  " + 
"-0.033238131309279446" + 
":  " + 
"(b('moss') <= 7.598436594009399) ? " + 
"0.05153940149973015" + 
":  " + 
"-0.00019704702953486834" + 
":  " + 
"(b('bare') <= 2.297703742980957) ? " + 
"(b('b10') <= 2078.0) ? " + 
"0.014763558489601635" + 
":  " + 
"-0.0009010529650408079" + 
":  " + 
"(b('b3') <= 871.5) ? " + 
"-0.009106936866553984" + 
":  " + 
"0.0011935269431084625" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 377.5) ? " + 
"(b('b6') <= 2714.0) ? " + 
"(b('b6') <= 2288.0) ? " + 
"-0.002708026990668621" + 
":  " + 
"-0.03040241685722714" + 
":  " + 
"(b('b10') <= 1391.0) ? " + 
"-0.09117768003766219" + 
":  " + 
"0.0545976567444855" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('moss') <= 13.451612949371338) ? " + 
"0.02261358976632882" + 
":  " + 
"-0.10783901460968585" + 
":  " + 
"(b('b1') <= 258.5) ? " + 
"-0.03465657404156482" + 
":  " + 
"0.00015358600754313662" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 68.5) ? " + 
"(b('bare') <= 0.28179189562797546) ? " + 
"(b('l8dt') <= 281736.0) ? " + 
"0.04331278212692197" + 
":  " + 
"0.0808931666959033" + 
":  " + 
"(b('trees') <= 11.304795563220978) ? " + 
"0.037960637648892265" + 
":  " + 
"0.0028837317611653535" + 
":  " + 
"(b('b6') <= 1724.5) ? " + 
"(b('lia') <= 41.805036544799805) ? " + 
"-0.018036216692803062" + 
":  " + 
"0.024989028618817157" + 
":  " + 
"(b('b6') <= 1921.0) ? " + 
"0.014709295482026076" + 
":  " + 
"-0.00023375041206510005" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 4.231653451919556) ? " + 
"(b('trees') <= 3.533814549446106) ? " + 
"(b('moss') <= 3.255519390106201) ? " + 
"-0.005083125018834297" + 
":  " + 
"0.0037160520918598453" + 
":  " + 
"(b('moss') <= 16.95894765853882) ? " + 
"-0.020452020856039362" + 
":  " + 
"-0.0725076276335813" + 
":  " + 
"(b('trees') <= 6.304144859313965) ? " + 
"(b('moss') <= 0.044692736119031906) ? " + 
"0.06457812325358898" + 
":  " + 
"0.009434847290962941" + 
":  " + 
"(b('lia') <= 41.83385467529297) ? " + 
"0.0022807466179042887" + 
":  " + 
"-0.00972024271616253" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 98.36243438720703) ? " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('moss') <= 7.140108346939087) ? " + 
"-0.0056043154285419575" + 
":  " + 
"0.005415570261053023" + 
":  " + 
"(b('moss') <= 8.152628898620605) ? " + 
"0.005668319846271315" + 
":  " + 
"-0.0019907816712759893" + 
":  " + 
"(b('b5') <= 2469.0) ? " + 
"(b('g0vv') <= -13.093931198120117) ? " + 
"0.006624887621873222" + 
":  " + 
"0.04671480594307993" + 
":  " + 
"(b('lia') <= 26.987046241760254) ? " + 
"-0.04446097868930744" + 
":  " + 
"0.0022313882866777557" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1379.5) ? " + 
"(b('b3') <= 1058.5) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"-0.00018716400684712101" + 
":  " + 
"0.045344429245113636" + 
":  " + 
"(b('b6') <= 2754.5) ? " + 
"0.042637034545436214" + 
":  " + 
"0.009929664804893058" + 
":  " + 
"(b('b7') <= 1680.5) ? " + 
"(b('b4') <= 1534.5) ? " + 
"0.03161815735952679" + 
":  " + 
"0.1516140412375441" + 
":  " + 
"(b('b3') <= 1007.5) ? " + 
"-0.03684089768303737" + 
":  " + 
"-0.0016958656234715222" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3385.5) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"(b('crop') <= 62.41747283935547) ? " + 
"0.0004307942188524228" + 
":  " + 
"-0.01161720756903275" + 
":  " + 
"(b('crop') <= 76.58172988891602) ? " + 
"0.03654794163162387" + 
":  " + 
"0.000789752098986986" + 
":  " + 
"(b('b3') <= 759.0) ? " + 
"(b('b6') <= 2599.5) ? " + 
"-0.023753919212555735" + 
":  " + 
"-0.06593508356952753" + 
":  " + 
"(b('b6') <= 1967.5) ? " + 
"0.0650532186724061" + 
":  " + 
"-0.002867746481537554" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1134.5) ? " + 
"(b('b3') <= 874.5) ? " + 
"(b('crop') <= 43.67561912536621) ? " + 
"0.005830002923080723" + 
":  " + 
"-0.005919986102550759" + 
":  " + 
"(b('moss') <= 24.863394737243652) ? " + 
"0.011705690054508678" + 
":  " + 
"0.09075977130493132" + 
":  " + 
"(b('b7') <= 1523.0) ? " + 
"(b('b6') <= 1843.0) ? " + 
"0.13263651035592244" + 
":  " + 
"-0.07247346928682122" + 
":  " + 
"(b('grass') <= 49.03428840637207) ? " + 
"0.0014710609131273367" + 
":  " + 
"-0.00594992675375343" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 15.706994533538818) ? " + 
"(b('trees') <= 24.454398155212402) ? " + 
"(b('lia') <= 27.911441802978516) ? " + 
"-0.016120984089801674" + 
":  " + 
"0.0010165182863149456" + 
":  " + 
"(b('b7') <= 1719.0) ? " + 
"-0.03478241839899915" + 
":  " + 
"0.009315273408581083" + 
":  " + 
"(b('bare') <= 11.910642623901367) ? " + 
"(b('g0vv') <= -10.747961521148682) ? " + 
"-0.01598873708767589" + 
":  " + 
"0.011161289217765885" + 
":  " + 
"(b('b11') <= 2351.5) ? " + 
"0.02946277870596595" + 
":  " + 
"-0.0021137573727370075" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -3.308971643447876) ? " + 
"(b('g0vv') <= -7.955878496170044) ? " + 
"(b('g0vh') <= -15.01952838897705) ? " + 
"-0.0006367151070570322" + 
":  " + 
"0.009939317856204758" + 
":  " + 
"(b('ndvi') <= 2883.5) ? " + 
"0.017125263431250804" + 
":  " + 
"-0.001820972576484269" + 
":  " + 
"(b('grass') <= 7.610584497451782) ? " + 
"(b('grass') <= 1.6218153238296509) ? " + 
"-0.030834975650154424" + 
":  " + 
"-0.06780380010144646" + 
":  " + 
"(b('g0vv') <= -3.1440563201904297) ? " + 
"-0.06602525896049975" + 
":  " + 
"0.0017987284934744042" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3385.5) ? " + 
"(b('crop') <= 67.3132438659668) ? " + 
"(b('crop') <= 62.41747283935547) ? " + 
"0.0004999927958973936" + 
":  " + 
"-0.011329548351971329" + 
":  " + 
"(b('trees') <= 14.932132720947266) ? " + 
"0.003333106804728102" + 
":  " + 
"0.08682534715601295" + 
":  " + 
"(b('b3') <= 759.0) ? " + 
"(b('b6') <= 2599.5) ? " + 
"-0.021360917228218215" + 
":  " + 
"-0.05974015648953981" + 
":  " + 
"(b('b6') <= 1967.5) ? " + 
"0.05760901130646565" + 
":  " + 
"-0.0028219053860069213" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('ndvi') <= 863.5) ? " + 
"(b('l8dt') <= 1036565.5) ? " + 
"-0.01001393095725645" + 
":  " + 
"-0.03888606541870156" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-0.0005282472677690809" + 
":  " + 
"0.0064736118207807565" + 
":  " + 
"(b('b2') <= 1342.0) ? " + 
"(b('b5') <= 2537.0) ? " + 
"0.0762259273759008" + 
":  " + 
"0.032335333401955296" + 
":  " + 
"(b('grass') <= 1.8120805025100708) ? " + 
"0.0029620638685009036" + 
":  " + 
"0.01955481861648242" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 98.36243438720703) ? " + 
"(b('trees') <= 4.231653451919556) ? " + 
"(b('trees') <= 3.533814549446106) ? " + 
"-0.0006390110042750764" + 
":  " + 
"-0.022930965675254697" + 
":  " + 
"(b('crop') <= 2.4269771575927734) ? " + 
"-0.006602842023612223" + 
":  " + 
"0.004002607954016361" + 
":  " + 
"(b('lia') <= 35.79117965698242) ? " + 
"(b('b5') <= 2469.0) ? " + 
"0.023994747062794423" + 
":  " + 
"2.9801007011226704e-05" + 
":  " + 
"(b('lia') <= 40.46782302856445) ? " + 
"-0.027757185181070475" + 
":  " + 
"0.0072199092328790815" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 30.27625846862793) ? " + 
"(b('urban') <= 1.4490950107574463) ? " + 
"(b('b10') <= 1358.0) ? " + 
"-0.013035574032194115" + 
":  " + 
"0.013296392994470848" + 
":  " + 
"(b('b11') <= 1349.5) ? " + 
"0.04374729118280792" + 
":  " + 
"-0.014270633667548459" + 
":  " + 
"(b('lia') <= 31.2601261138916) ? " + 
"(b('g0vv') <= -12.410733699798584) ? " + 
"-0.02927601938523498" + 
":  " + 
"-0.006518975850717708" + 
":  " + 
"(b('bare') <= 0.29949215054512024) ? " + 
"-0.0023354738427803336" + 
":  " + 
"0.0022325724171248793" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1134.5) ? " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('b4') <= 1108.5) ? " + 
"9.914816160876992e-06" + 
":  " + 
"0.025340590841665202" + 
":  " + 
"(b('b11') <= 2225.0) ? " + 
"0.0500978200158247" + 
":  " + 
"-0.050608193157192616" + 
":  " + 
"(b('b11') <= 1523.0) ? " + 
"(b('b6') <= 1843.0) ? " + 
"0.11912644690484595" + 
":  " + 
"-0.06519485434663619" + 
":  " + 
"(b('grass') <= 49.03428840637207) ? " + 
"0.0012124843541215422" + 
":  " + 
"-0.005346476875173474" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 16.995849609375) ? " + 
"(b('trees') <= 14.932132720947266) ? " + 
"(b('grass') <= 11.09217882156372) ? " + 
"-4.288430269124945e-05" + 
":  " + 
"-0.0092613635200267" + 
":  " + 
"(b('b5') <= 3011.0) ? " + 
"0.046269905545142834" + 
":  " + 
"-0.005353852831241625" + 
":  " + 
"(b('crop') <= 71.31087875366211) ? " + 
"(b('b4') <= 757.5) ? " + 
"0.009116112311932522" + 
":  " + 
"-0.0018638446102178816" + 
":  " + 
"(b('b5') <= 2327.0) ? " + 
"0.04609454576246015" + 
":  " + 
"0.009272133200685559" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.75) ? " + 
"(b('b6') <= 2714.0) ? " + 
"(b('b4') <= 620.0) ? " + 
"0.006339045016063893" + 
":  " + 
"-0.01790625190859188" + 
":  " + 
"(b('crop') <= 17.2618670463562) ? " + 
"-0.07238846250929208" + 
":  " + 
"0.04663853480542669" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('b6') <= 2266.5) ? " + 
"-0.00014949568602494532" + 
":  " + 
"0.060921256883736966" + 
":  " + 
"(b('b4') <= 793.5) ? " + 
"0.005540950449436649" + 
":  " + 
"-0.0006751257939437027" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 657.5) ? " + 
"(b('b4') <= 1662.5) ? " + 
"(b('lia') <= 38.07048988342285) ? " + 
"-0.0026298187344728544" + 
":  " + 
"0.0030143695663943483" + 
":  " + 
"(b('crop') <= 76.58172988891602) ? " + 
"-0.002378683816258838" + 
":  " + 
"-0.019608637739498433" + 
":  " + 
"(b('b4') <= 2030.5) ? " + 
"(b('b5') <= 3842.0) ? " + 
"0.006632868842905488" + 
":  " + 
"0.08733923544466964" + 
":  " + 
"(b('ndvi') <= 3471.0) ? " + 
"-0.0037762850665905433" + 
":  " + 
"0.04704146141110604" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 15.564701080322266) ? " + 
"(b('trees') <= 15.104385375976562) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"-0.0026312917930327324" + 
":  " + 
"0.0021574648676039587" + 
":  " + 
"(b('b6') <= 2591.5) ? " + 
"0.13476588280424104" + 
":  " + 
"-0.012589929912160474" + 
":  " + 
"(b('trees') <= 17.320652961730957) ? " + 
"(b('b5') <= 2316.5) ? " + 
"-0.029835188787932558" + 
":  " + 
"-0.07283435341799704" + 
":  " + 
"(b('b10') <= 2342.5) ? " + 
"-0.00915766918402732" + 
":  " + 
"0.015899235725502597" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 608.5) ? " + 
"(b('b6') <= 2655.5) ? " + 
"(b('b4') <= 534.0) ? " + 
"0.009980069171989297" + 
":  " + 
"-0.023200352152471824" + 
":  " + 
"(b('ndvi') <= 2295.0) ? " + 
"0.13619559470984188" + 
":  " + 
"0.050912883303298316" + 
":  " + 
"(b('b3') <= 620.5) ? " + 
"(b('grass') <= 15.762518882751465) ? " + 
"-0.02429175019029133" + 
":  " + 
"0.03861631010015866" + 
":  " + 
"(b('b11') <= 1013.5) ? " + 
"0.024807325616022516" + 
":  " + 
"-0.00011025674713132558" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3390323.5) ? " + 
"(b('b5') <= 1492.5) ? " + 
"(b('l8dt') <= 1511463.0) ? " + 
"0.024251011576225272" + 
":  " + 
"-0.01643740227797343" + 
":  " + 
"(b('b3') <= 608.5) ? " + 
"-0.011926594735494142" + 
":  " + 
"-0.00013597846001989306" + 
":  " + 
"(b('b3') <= 552.5) ? " + 
"(b('ndvi') <= 4773.0) ? " + 
"-0.01548772802735273" + 
":  " + 
"-0.07561407970943602" + 
":  " + 
"(b('b3') <= 1760.0) ? " + 
"0.011566007225445764" + 
":  " + 
"-0.034920968811405426" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('b5') <= 4370.5) ? " + 
"(b('b5') <= 4282.0) ? " + 
"-3.4577672363131227e-05" + 
":  " + 
"0.04122115016111403" + 
":  " + 
"(b('b2') <= 640.0) ? " + 
"-0.04854709027225096" + 
":  " + 
"-0.012578079854559887" + 
":  " + 
"(b('trees') <= 0.8948863744735718) ? " + 
"(b('ndvi') <= 5908.5) ? " + 
"0.08697243545780094" + 
":  " + 
"0.03014814605035993" + 
":  " + 
"(b('l8dt') <= 259195.0) ? " + 
"0.003512296109814208" + 
":  " + 
"-0.01659914681151855" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('b6') <= 2594.5) ? " + 
"(b('bare') <= 0.34665676206350327) ? " + 
"-0.017147018326698536" + 
":  " + 
"0.005549599670280235" + 
":  " + 
"(b('b4') <= 911.0) ? " + 
"0.030968163668342215" + 
":  " + 
"-0.0030321415372503366" + 
":  " + 
"(b('trees') <= 8.639616012573242) ? " + 
"(b('b5') <= 1998.5) ? " + 
"0.011437671339544365" + 
":  " + 
"-0.002194087911708435" + 
":  " + 
"(b('urban') <= 14.72341012954712) ? " + 
"0.004638830414823077" + 
":  " + 
"0.06187551170044363" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 657.5) ? " + 
"(b('b4') <= 1662.5) ? " + 
"(b('b2') <= 884.5) ? " + 
"8.650440263536108e-07" + 
":  " + 
"0.1087774422323923" + 
":  " + 
"(b('crop') <= 76.58172988891602) ? " + 
"-0.0021567088143781502" + 
":  " + 
"-0.017283542094268713" + 
":  " + 
"(b('ndvi') <= 1776.0) ? " + 
"(b('l8dt') <= 19841.0) ? " + 
"0.09017934929423017" + 
":  " + 
"-0.0004082584102600396" + 
":  " + 
"(b('b4') <= 1896.5) ? " + 
"0.018014513781504284" + 
":  " + 
"0.001152368274682409" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('ndvi') <= 863.5) ? " + 
"(b('ndvi') <= 858.5) ? " + 
"-0.008971486166642444" + 
":  " + 
"-0.05401300094775953" + 
":  " + 
"(b('b2') <= 957.75) ? " + 
"-0.0005715272688418261" + 
":  " + 
"0.005178005501152409" + 
":  " + 
"(b('b2') <= 1342.0) ? " + 
"(b('b5') <= 2537.0) ? " + 
"0.0689766328804045" + 
":  " + 
"0.02983278270032778" + 
":  " + 
"(b('lia') <= 43.39209175109863) ? " + 
"0.013406615692279916" + 
":  " + 
"-0.010001996480019584" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('lia') <= 30.312915802001953) ? " + 
"(b('lia') <= 28.096532821655273) ? " + 
"-0.007342345353259211" + 
":  " + 
"0.012975636520651956" + 
":  " + 
"(b('lia') <= 31.2601261138916) ? " + 
"-0.013291966637145275" + 
":  " + 
"0.0004298065137969574" + 
":  " + 
"(b('b5') <= 2568.75) ? " + 
"(b('moss') <= 7.398061752319336) ? " + 
"-0.0041515356961815365" + 
":  " + 
"0.015095903788526899" + 
":  " + 
"(b('b5') <= 2855.5) ? " + 
"-0.0197399923032737" + 
":  " + 
"-0.0016577877099033908" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -3.308971643447876) ? " + 
"(b('g0vv') <= -10.249711990356445) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"-0.0006227791306584227" + 
":  " + 
"-0.031615035370387796" + 
":  " + 
"(b('grass') <= 9.205488204956055) ? " + 
"-0.00360293501958042" + 
":  " + 
"0.006751880584963146" + 
":  " + 
"(b('crop') <= 89.71894836425781) ? " + 
"(b('l8dt') <= 1792098.5) ? " + 
"-0.022707895871808707" + 
":  " + 
"0.01884274110736664" + 
":  " + 
"(b('grass') <= 1.6218153238296509) ? " + 
"-0.02947056909862768" + 
":  " + 
"-0.06287981219770951" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b5') <= 3946.5) ? " + 
"(b('b1') <= 583.5) ? " + 
"0.011345578863100982" + 
":  " + 
"2.591777350495571e-05" + 
":  " + 
"(b('g0vv') <= -11.732499599456787) ? " + 
"0.005082709297159921" + 
":  " + 
"-0.017287598467344116" + 
":  " + 
"(b('grass') <= 5.3386664390563965) ? " + 
"(b('lia') <= 39.133155822753906) ? " + 
"0.003608121266170181" + 
":  " + 
"-0.015541533859975455" + 
":  " + 
"(b('g0vv') <= -11.411035537719727) ? " + 
"-0.0015239356497868477" + 
":  " + 
"0.0033882354615976306" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 761.5) ? " + 
"(b('b5') <= 3124.5) ? " + 
"(b('b6') <= 2713.0) ? " + 
"-0.0023953598694524845" + 
":  " + 
"0.025701040644399084" + 
":  " + 
"(b('moss') <= 13.451612949371338) ? " + 
"-0.017467157023447928" + 
":  " + 
"-0.059287139497850645" + 
":  " + 
"(b('b10') <= 1383.5) ? " + 
"(b('ndvi') <= 4041.0) ? " + 
"0.03236869683600787" + 
":  " + 
"0.001975919570377329" + 
":  " + 
"(b('b4') <= 701.0) ? " + 
"0.028252466179421395" + 
":  " + 
"-0.00012313647422819616" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('lia') <= 30.273048400878906) ? " + 
"(b('lia') <= 29.140652656555176) ? " + 
"-0.00023479396464065852" + 
":  " + 
"0.016649930100040226" + 
":  " + 
"(b('b1') <= 364.5) ? " + 
"0.00502755248304069" + 
":  " + 
"-0.0013201094542319625" + 
":  " + 
"(b('b1') <= 414.5) ? " + 
"(b('b4') <= 715.0) ? " + 
"0.004067071968067834" + 
":  " + 
"-0.014190308387943606" + 
":  " + 
"(b('b7') <= 2289.5) ? " + 
"0.008294972918426695" + 
":  " + 
"-0.0049923138493377026" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 882.5) ? " + 
"(b('crop') <= 43.28263282775879) ? " + 
"(b('b5') <= 2315.0) ? " + 
"-0.01090967658417094" + 
":  " + 
"0.0152745432946619" + 
":  " + 
"(b('b5') <= 2161.0) ? " + 
"0.007152756777154745" + 
":  " + 
"-0.010957567447532159" + 
":  " + 
"(b('b4') <= 951.5) ? " + 
"(b('b3') <= 885.5) ? " + 
"0.07319141478994463" + 
":  " + 
"0.020740484753383807" + 
":  " + 
"(b('b6') <= 2667.0) ? " + 
"0.011106748586483148" + 
":  " + 
"-0.0008592208503096872" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 608.5) ? " + 
"(b('b5') <= 2592.0) ? " + 
"(b('g0vv') <= -15.372703075408936) ? " + 
"-0.06582303755395005" + 
":  " + 
"-0.010508267804075593" + 
":  " + 
"(b('b5') <= 2998.5) ? " + 
"0.031159471063485312" + 
":  " + 
"-0.0727897992019813" + 
":  " + 
"(b('b3') <= 620.5) ? " + 
"(b('grass') <= 15.762518882751465) ? " + 
"-0.021917365143899956" + 
":  " + 
"0.03200820733141404" + 
":  " + 
"(b('b10') <= 1013.5) ? " + 
"0.022308822815490546" + 
":  " + 
"-4.3728229728109154e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 761.5) ? " + 
"(b('b5') <= 3124.5) ? " + 
"(b('b6') <= 2713.0) ? " + 
"-0.0022856923196399297" + 
":  " + 
"0.02188135500431099" + 
":  " + 
"(b('grass') <= 55.73245429992676) ? " + 
"-0.015780323091418687" + 
":  " + 
"-0.05733867083409802" + 
":  " + 
"(b('b11') <= 1383.5) ? " + 
"(b('ndvi') <= 4041.0) ? " + 
"0.02804595638904245" + 
":  " + 
"0.0011039641295835974" + 
":  " + 
"(b('b4') <= 701.0) ? " + 
"0.025544213706595587" + 
":  " + 
"-2.0020526027947937e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 657.5) ? " + 
"(b('b5') <= 3381.5) ? " + 
"(b('crop') <= 67.3132438659668) ? " + 
"-0.0016401825021796234" + 
":  " + 
"0.005548015663173216" + 
":  " + 
"(b('grass') <= 65.31989097595215) ? " + 
"-0.008567390327605442" + 
":  " + 
"0.08295802933802027" + 
":  " + 
"(b('b4') <= 2030.5) ? " + 
"(b('b5') <= 3842.0) ? " + 
"0.005759143898798617" + 
":  " + 
"0.07675009297666888" + 
":  " + 
"(b('ndvi') <= 3471.0) ? " + 
"-0.002845755616170638" + 
":  " + 
"0.0414841171971925" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 24.454398155212402) ? " + 
"(b('lia') <= 43.82534217834473) ? " + 
"(b('lia') <= 43.39883613586426) ? " + 
"0.0003642574113833702" + 
":  " + 
"-0.012178860617232048" + 
":  " + 
"(b('lia') <= 44.06046104431152) ? " + 
"0.025668144449461062" + 
":  " + 
"-0.0006001480933407228" + 
":  " + 
"(b('b5') <= 2281.5) ? " + 
"(b('b11') <= 1679.5) ? " + 
"-0.017089341464199825" + 
":  " + 
"0.034832870446164316" + 
":  " + 
"(b('ndvi') <= 2482.5) ? " + 
"-0.008093504605713038" + 
":  " + 
"-0.03672132034885484" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('b1') <= 68.5) ? " + 
"(b('b11') <= 482.5) ? " + 
"0.012907815044793325" + 
":  " + 
"0.06464994583530649" + 
":  " + 
"(b('b6') <= 1709.0) ? " + 
"-0.010988062983628467" + 
":  " + 
"3.103864237434381e-05" + 
":  " + 
"(b('grass') <= 1.8120805025100708) ? " + 
"(b('g0vh') <= -21.38139247894287) ? " + 
"-0.005009129913632485" + 
":  " + 
"0.011078856049091354" + 
":  " + 
"(b('g0vh') <= -20.866625785827637) ? " + 
"0.02760365926976142" + 
":  " + 
"0.007213189984091665" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -3.308971643447876) ? " + 
"(b('g0vh') <= -14.666974544525146) ? " + 
"(b('ndvi') <= 4627.5) ? " + 
"0.00023766700816050493" + 
":  " + 
"-0.0067981930841544465" + 
":  " + 
"(b('ndvi') <= 6025.0) ? " + 
"0.004929240723950484" + 
":  " + 
"0.04394338395572591" + 
":  " + 
"(b('crop') <= 89.71894836425781) ? " + 
"(b('g0vv') <= -3.1440563201904297) ? " + 
"-0.053634630547548856" + 
":  " + 
"-0.0008587952915919151" + 
":  " + 
"(b('grass') <= 1.6218153238296509) ? " + 
"-0.02731861034709624" + 
":  " + 
"-0.05816891681395669" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 90.44964218139648) ? " + 
"(b('grass') <= 88.09611511230469) ? " + 
"(b('l8dt') <= 21116.5) ? " + 
"0.012345333819830958" + 
":  " + 
"-0.000277594358947549" + 
":  " + 
"(b('ndvi') <= 2589.0) ? " + 
"-0.04643420528137731" + 
":  " + 
"0.01588882762235932" + 
":  " + 
"(b('g0vh') <= -18.026637077331543) ? " + 
"(b('moss') <= 6.485493421554565) ? " + 
"0.0014525065511585662" + 
":  " + 
"0.05515475032671236" + 
":  " + 
"(b('b1') <= 601.5) ? " + 
"0.039794120276076685" + 
":  " + 
"0.11057730108566835" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('b5') <= 2592.5) ? " + 
"(b('b11') <= 2216.5) ? " + 
"-0.011287339776801816" + 
":  " + 
"0.0025853692949080755" + 
":  " + 
"(b('b3') <= 627.5) ? " + 
"0.04801131478961426" + 
":  " + 
"0.0001017401553554364" + 
":  " + 
"(b('trees') <= 8.639616012573242) ? " + 
"(b('ndvi') <= 2736.0) ? " + 
"0.001347764270457689" + 
":  " + 
"-0.006220294696046977" + 
":  " + 
"(b('b3') <= 837.0) ? " + 
"-0.00035376016678612094" + 
":  " + 
"0.013335875268596932" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 15.564701080322266) ? " + 
"(b('trees') <= 15.104385375976562) ? " + 
"(b('grass') <= 16.995849609375) ? " + 
"-0.00217473409456458" + 
":  " + 
"0.0018054211938536761" + 
":  " + 
"(b('b6') <= 2591.5) ? " + 
"0.12044194632088667" + 
":  " + 
"-0.012064775920443128" + 
":  " + 
"(b('trees') <= 17.320652961730957) ? " + 
"(b('b6') <= 2229.5) ? " + 
"-0.020791445643849996" + 
":  " + 
"-0.0618587481651373" + 
":  " + 
"(b('b7') <= 2342.5) ? " + 
"-0.007800685830175269" + 
":  " + 
"0.013839793547141863" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('g0vv') <= -11.78309965133667) ? " + 
"(b('crop') <= 72.66402816772461) ? " + 
"-0.0029087546561731" + 
":  " + 
"0.01597596076495059" + 
":  " + 
"(b('b5') <= 3528.5) ? " + 
"0.0043594911552930415" + 
":  " + 
"-0.010095931854641424" + 
":  " + 
"(b('grass') <= 5.3386664390563965) ? " + 
"(b('ndvi') <= 4124.0) ? " + 
"-0.005193731570159709" + 
":  " + 
"-0.03322038227590055" + 
":  " + 
"(b('g0vv') <= -11.411035537719727) ? " + 
"-0.0014679654243692343" + 
":  " + 
"0.0031627311875665164" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('ndvi') <= 863.5) ? " + 
"(b('g0vv') <= -14.205132007598877) ? " + 
"0.025410681188585683" + 
":  " + 
"-0.010912906935582204" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-0.000480103273796988" + 
":  " + 
"0.005533518594504276" + 
":  " + 
"(b('b6') <= 2943.0) ? " + 
"(b('b3') <= 1637.0) ? " + 
"0.07152355289178751" + 
":  " + 
"0.0356976392796359" + 
":  " + 
"(b('grass') <= 1.8120805025100708) ? " + 
"0.003419998177693018" + 
":  " + 
"0.01675019115080686" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 43.82485580444336) ? " + 
"(b('lia') <= 43.39883613586426) ? " + 
"(b('lia') <= 42.24803924560547) ? " + 
"-0.0003554981742130784" + 
":  " + 
"0.008711512389104135" + 
":  " + 
"(b('g0vh') <= -22.849122047424316) ? " + 
"0.10583818819493701" + 
":  " + 
"-0.011679920574899446" + 
":  " + 
"(b('lia') <= 44.06427764892578) ? " + 
"(b('b2') <= 1049.0) ? " + 
"0.018604720365868813" + 
":  " + 
"0.07398640860712212" + 
":  " + 
"(b('g0vh') <= -16.62160873413086) ? " + 
"-0.0040318947382129485" + 
":  " + 
"0.02478387782311089" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b1') <= 583.5) ? " + 
"(b('b2') <= 777.5) ? " + 
"0.006849248825284769" + 
":  " + 
"0.08015734986320536" + 
":  " + 
"(b('b6') <= 2987.5) ? " + 
"-0.02263850197821306" + 
":  " + 
"0.0023835888881161373" + 
":  " + 
"(b('crop') <= 77.41421890258789) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.0006280755503278758" + 
":  " + 
"0.013077815596490527" + 
":  " + 
"(b('grass') <= 11.09217882156372) ? " + 
"-0.00150133297776677" + 
":  " + 
"-0.02760922037587815" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 98.36243438720703) ? " + 
"(b('lia') <= 34.4125919342041) ? " + 
"(b('lia') <= 33.70889091491699) ? " + 
"-0.001740080348567329" + 
":  " + 
"-0.015303896914908627" + 
":  " + 
"(b('lia') <= 34.449153900146484) ? " + 
"0.05446460572804541" + 
":  " + 
"0.00037244761970650603" + 
":  " + 
"(b('lia') <= 36.049360275268555) ? " + 
"(b('lia') <= 26.987046241760254) ? " + 
"-0.012743494365291909" + 
":  " + 
"0.016717854340041423" + 
":  " + 
"(b('ndvi') <= 1263.5) ? " + 
"-0.059998694277097975" + 
":  " + 
"-0.0044715819012851165" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 68.5) ? " + 
"(b('b6') <= 936.5) ? " + 
"(b('trees') <= 11.304795563220978) ? " + 
"0.030569229729380143" + 
":  " + 
"-0.004453841475811071" + 
":  " + 
"(b('l8dt') <= 281736.0) ? " + 
"0.030840604956031414" + 
":  " + 
"0.06491901155299055" + 
":  " + 
"(b('b3') <= 608.5) ? " + 
"(b('b5') <= 2592.0) ? " + 
"-0.013512600916495088" + 
":  " + 
"0.021023608062789027" + 
":  " + 
"(b('b4') <= 757.5) ? " + 
"0.00514557873991177" + 
":  " + 
"-0.000437286675171479" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1938.5) ? " + 
"(b('moss') <= 0.2824763059616089) ? " + 
"(b('b6') <= 2588.5) ? " + 
"-0.019164635255817873" + 
":  " + 
"0.008976006031089353" + 
":  " + 
"(b('moss') <= 0.641522616147995) ? " + 
"0.0725870602788423" + 
":  " + 
"0.007162720578491597" + 
":  " + 
"(b('b3') <= 456.0) ? " + 
"(b('g0vh') <= -18.973949432373047) ? " + 
"-0.08592474486603517" + 
":  " + 
"-0.004008457328229964" + 
":  " + 
"(b('b2') <= 314.5) ? " + 
"0.011706891355887306" + 
":  " + 
"-0.0005971430925589748" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.75) ? " + 
"(b('b4') <= 620.0) ? " + 
"(b('b2') <= 361.5) ? " + 
"0.00042624096504752116" + 
":  " + 
"0.03269086049238827" + 
":  " + 
"(b('moss') <= 10.476681232452393) ? " + 
"-0.005859610639563462" + 
":  " + 
"-0.03275089419952834" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('b4') <= 725.5) ? " + 
"0.005149369242072423" + 
":  " + 
"0.058806821180766876" + 
":  " + 
"(b('b1') <= 252.0) ? " + 
"-0.039898765676516575" + 
":  " + 
"0.00014758323371768422" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3390323.5) ? " + 
"(b('b5') <= 1492.5) ? " + 
"(b('g0vv') <= -7.370482444763184) ? " + 
"0.004967775882722297" + 
":  " + 
"0.037083182403530104" + 
":  " + 
"(b('b3') <= 608.5) ? " + 
"-0.010219335564958524" + 
":  " + 
"-0.00012405380009484945" + 
":  " + 
"(b('b3') <= 543.5) ? " + 
"(b('g0vv') <= -12.250389099121094) ? " + 
"0.01682530862265052" + 
":  " + 
"-0.06366546633977892" + 
":  " + 
"(b('b6') <= 4860.5) ? " + 
"0.009270215244916247" + 
":  " + 
"-0.03589076232778713" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 314.5) ? " + 
"(b('b6') <= 2368.0) ? " + 
"(b('ndvi') <= 4726.5) ? " + 
"0.007720022167003506" + 
":  " + 
"-0.03898478167706814" + 
":  " + 
"(b('ndvi') <= 5557.5) ? " + 
"0.04929745312518992" + 
":  " + 
"0.17881378295376574" + 
":  " + 
"(b('b2') <= 347.5) ? " + 
"(b('b1') <= 261.5) ? " + 
"-0.007870182558562132" + 
":  " + 
"-0.047915004055811686" + 
":  " + 
"(b('b1') <= 254.5) ? " + 
"-0.016439462458713906" + 
":  " + 
"0.00042991937210367493" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 4653.0) ? " + 
"(b('ndvi') <= 5233.5) ? " + 
"(b('ndvi') <= 5133.5) ? " + 
"9.019335056804383e-05" + 
":  " + 
"0.03443695782424169" + 
":  " + 
"(b('crop') <= 87.44597244262695) ? " + 
"-0.002256642425057189" + 
":  " + 
"-0.027417448069533962" + 
":  " + 
"(b('b4') <= 924.5) ? " + 
"(b('l8dt') <= 2073598.5) ? " + 
"0.04368300823881415" + 
":  " + 
"-0.008405721503634578" + 
":  " + 
"(b('l8dt') <= 259195.0) ? " + 
"0.0035951851593410793" + 
":  " + 
"-0.013446839181422178" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -15.064626693725586) ? " + 
"(b('ndvi') <= 5233.5) ? " + 
"(b('ndvi') <= 5168.5) ? " + 
"-0.0001469148497687154" + 
":  " + 
"0.04260361253395561" + 
":  " + 
"(b('b5') <= 4015.0) ? " + 
"-0.0128784524955113" + 
":  " + 
"0.027550476437057" + 
":  " + 
"(b('g0vh') <= -15.063008785247803) ? " + 
"0.22624924502323956" + 
":  " + 
"(b('b3') <= 1471.0) ? " + 
"0.0030079864703405237" + 
":  " + 
"0.04034493570902982" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.31542158126831) ? " + 
"(b('b10') <= 1416.5) ? " + 
"(b('bare') <= 0.28179189562797546) ? " + 
"-0.03445333100822638" + 
":  " + 
"0.008893825412709925" + 
":  " + 
"(b('b4') <= 758.0) ? " + 
"0.03651720299363302" + 
":  " + 
"-0.0026970978261082945" + 
":  " + 
"(b('grass') <= 90.44964218139648) ? " + 
"(b('trees') <= 4.231653451919556) ? " + 
"-0.0016158743852701402" + 
":  " + 
"0.0024440724587506692" + 
":  " + 
"(b('b5') <= 2526.5) ? " + 
"0.026386504086797612" + 
":  " + 
"-0.009798768991898302" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b1') <= 727.5) ? " + 
"(b('b5') <= 3523.5) ? " + 
"0.007973008514385559" + 
":  " + 
"-0.004195980300999555" + 
":  " + 
"(b('ndvi') <= 3020.0) ? " + 
"-0.007256443083977873" + 
":  " + 
"0.02876599674584208" + 
":  " + 
"(b('grass') <= 5.3386664390563965) ? " + 
"(b('lia') <= 39.12819290161133) ? " + 
"0.006273202320632326" + 
":  " + 
"-0.012517372962103885" + 
":  " + 
"(b('grass') <= 11.09217882156372) ? " + 
"0.005744133553189047" + 
":  " + 
"-0.0005903041630495999" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 908.5) ? " + 
"(b('b4') <= 1614.5) ? " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-0.00034675997789977486" + 
":  " + 
"0.012842739382542231" + 
":  " + 
"(b('g0vh') <= -16.627461433410645) ? " + 
"-0.00770067388952775" + 
":  " + 
"0.011118281997411964" + 
":  " + 
"(b('l8dt') <= 21618.5) ? " + 
"(b('b3') <= 1387.0) ? " + 
"0.042068101703527636" + 
":  " + 
"0.14517355337609766" + 
":  " + 
"(b('b4') <= 2029.5) ? " + 
"0.009334422936406262" + 
":  " + 
"-0.0018908306218539802" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 24.454398155212402) ? " + 
"(b('lia') <= 38.07048988342285) ? " + 
"(b('lia') <= 38.01721382141113) ? " + 
"-0.0005600021426733643" + 
":  " + 
"-0.05198196204729319" + 
":  " + 
"(b('lia') <= 38.16269874572754) ? " + 
"0.03176625242265421" + 
":  " + 
"0.0008427771970677522" + 
":  " + 
"(b('l8dt') <= 1547367.5) ? " + 
"(b('ndvi') <= 4010.0) ? " + 
"-0.0028195225424923055" + 
":  " + 
"-0.04882808499661999" + 
":  " + 
"(b('b5') <= 2281.5) ? " + 
"0.012792188742004875" + 
":  " + 
"-0.04703227847550863" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -23.013851165771484) ? " + 
"(b('b5') <= 3008.0) ? " + 
"(b('g0vv') <= -14.730862140655518) ? " + 
"-0.000751192071223508" + 
":  " + 
"0.028816028116038252" + 
":  " + 
"(b('l8dt') <= 693432.0) ? " + 
"0.021524656470639454" + 
":  " + 
"0.07410810533288614" + 
":  " + 
"(b('g0vv') <= -14.32249927520752) ? " + 
"(b('b10') <= 1416.5) ? " + 
"-0.022050989301466165" + 
":  " + 
"-0.0021756069932127716" + 
":  " + 
"(b('l8dt') <= 323247.0) ? " + 
"-0.0021754361685610265" + 
":  " + 
"0.0018361040902724192" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('l8dt') <= 50860.5) ? " + 
"(b('l8dt') <= 22356.0) ? " + 
"0.006828309636420888" + 
":  " + 
"-0.010338771241339645" + 
":  " + 
"(b('l8dt') <= 70515.5) ? " + 
"0.010496148149521293" + 
":  " + 
"-0.00014038823560177555" + 
":  " + 
"(b('b6') <= 2943.0) ? " + 
"(b('b2') <= 1206.5) ? " + 
"0.06392744132604872" + 
":  " + 
"0.033255582909946874" + 
":  " + 
"(b('lia') <= 42.78582572937012) ? " + 
"0.0130809925959681" + 
":  " + 
"-0.0011270100439904427" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 1.9490950107574463) ? " + 
"(b('b4') <= 1185.5) ? " + 
"(b('b3') <= 836.5) ? " + 
"-0.0018910746963618284" + 
":  " + 
"0.011368082400511263" + 
":  " + 
"(b('b3') <= 920.5) ? " + 
"-0.027923634508253543" + 
":  " + 
"-0.00032734176804884396" + 
":  " + 
"(b('b5') <= 2568.75) ? " + 
"(b('crop') <= 48.84012222290039) ? " + 
"0.012964687973972025" + 
":  " + 
"-0.005222479071907821" + 
":  " + 
"(b('b5') <= 2855.5) ? " + 
"-0.01724469556672846" + 
":  " + 
"-0.0009892507028019157" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 13.571214199066162) ? " + 
"(b('trees') <= 11.215232372283936) ? " + 
"(b('trees') <= 11.076036930084229) ? " + 
"-7.425133142118896e-06" + 
":  " + 
"-0.014280881543031108" + 
":  " + 
"(b('b5') <= 2037.0) ? " + 
"-0.021878680785886024" + 
":  " + 
"0.010005751410711987" + 
":  " + 
"(b('grass') <= 20.509230613708496) ? " + 
"(b('b5') <= 3011.0) ? " + 
"0.03153751439557914" + 
":  " + 
"-0.008179950627315503" + 
":  " + 
"(b('b5') <= 2942.5) ? " + 
"-0.014754389998307811" + 
":  " + 
"0.005639352848960164" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1938.5) ? " + 
"(b('moss') <= 24.448779106140137) ? " + 
"(b('moss') <= 19.819469451904297) ? " + 
"0.004895219933857647" + 
":  " + 
"-0.04398136986863529" + 
":  " + 
"(b('ndvi') <= 2267.0) ? " + 
"0.0950095750400454" + 
":  " + 
"-0.1066720257863069" + 
":  " + 
"(b('b5') <= 2314.5) ? " + 
"(b('crop') <= 67.3132438659668) ? " + 
"-0.007572830626502073" + 
":  " + 
"0.016258050163314188" + 
":  " + 
"(b('grass') <= 35.55763244628906) ? " + 
"-0.0019331912723917818" + 
":  " + 
"0.005069184558097119" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('b10') <= 2199.5) ? " + 
"(b('moss') <= 0.11378024518489838) ? " + 
"-0.016262953501405206" + 
":  " + 
"-0.0009059601939875409" + 
":  " + 
"(b('crop') <= 4.842228651046753) ? " + 
"-0.0033787091171335213" + 
":  " + 
"0.007165906961803686" + 
":  " + 
"(b('grass') <= 73.25521087646484) ? " + 
"(b('grass') <= 72.42327880859375) ? " + 
"0.0005427987870061645" + 
":  " + 
"-0.057510803615410014" + 
":  " + 
"(b('b4') <= 829.0) ? " + 
"0.05934178077857678" + 
":  " + 
"0.003107503957620816" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('moss') <= 15.027272701263428) ? " + 
"-0.0008525364164062223" + 
":  " + 
"-0.015459028498076689" + 
":  " + 
"(b('b11') <= 2383.0) ? " + 
"0.02237281350062614" + 
":  " + 
"0.10238343780091856" + 
":  " + 
"(b('b4') <= 715.5) ? " + 
"(b('grass') <= 23.295454025268555) ? " + 
"0.004504764262691196" + 
":  " + 
"0.04160271458836816" + 
":  " + 
"(b('lia') <= 35.41839027404785) ? " + 
"-0.005223324324165787" + 
":  " + 
"0.0024726592768948463" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -23.63000202178955) ? " + 
"(b('l8dt') <= 129158.0) ? " + 
"(b('b5') <= 2243.0) ? " + 
"-0.03374053827910711" + 
":  " + 
"-0.025134344995071417" + 
":  " + 
"(b('grass') <= 99.8344841003418) ? " + 
"0.023853545922395174" + 
":  " + 
"0.09100207717645896" + 
":  " + 
"(b('g0vv') <= -16.012653350830078) ? " + 
"(b('ndvi') <= 3372.0) ? " + 
"-0.0022552404364940735" + 
":  " + 
"-0.03921536325344738" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-0.0002847805308129023" + 
":  " + 
"0.0044426127718555294" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 99.8344841003418) ? " + 
"(b('moss') <= 0.04188481718301773) ? " + 
"(b('b10') <= 2263.5) ? " + 
"-0.010598197069668205" + 
":  " + 
"0.004768780083918997" + 
":  " + 
"(b('moss') <= 1.9861568808555603) ? " + 
"0.010710937527058572" + 
":  " + 
"-0.00036521180576442664" + 
":  " + 
"(b('g0vv') <= -9.487696170806885) ? " + 
"(b('lia') <= 35.36849784851074) ? " + 
"0.010943914468766684" + 
":  " + 
"-0.01090249920028467" + 
":  " + 
"(b('g0vh') <= -18.97841167449951) ? " + 
"0.06684171156941449" + 
":  " + 
"0.10648852314087703" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1938.5) ? " + 
"(b('b3') <= 1026.5) ? " + 
"(b('b4') <= 1186.5) ? " + 
"0.005640357583234517" + 
":  " + 
"-0.034696031543366694" + 
":  " + 
"(b('moss') <= 18.74301242828369) ? " + 
"0.03384658379572547" + 
":  " + 
"0.10516746849292764" + 
":  " + 
"(b('l8dt') <= 3385997.0) ? " + 
"(b('b4') <= 529.0) ? " + 
"0.015114543168927384" + 
":  " + 
"-0.0007947116703704423" + 
":  " + 
"(b('b5') <= 1979.0) ? " + 
"0.07927865620640337" + 
":  " + 
"0.005271688004278298" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 608.5) ? " + 
"(b('b6') <= 2655.5) ? " + 
"(b('b6') <= 2409.5) ? " + 
"-0.004574382203229589" + 
":  " + 
"-0.042518917234406164" + 
":  " + 
"(b('b10') <= 1443.0) ? " + 
"0.009290228239603824" + 
":  " + 
"0.04346025573561304" + 
":  " + 
"(b('b4') <= 757.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"-0.0022467039005633076" + 
":  " + 
"0.02881094730771263" + 
":  " + 
"(b('b3') <= 839.5) ? " + 
"-0.004691728877603553" + 
":  " + 
"0.0005671048416333243" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 12.501765251159668) ? " + 
"(b('trees') <= 11.430836200714111) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"-0.00035545060777516114" + 
":  " + 
"0.030503459321870596" + 
":  " + 
"(b('g0vv') <= -10.365392684936523) ? " + 
"0.012684656606388843" + 
":  " + 
"0.05518110379545298" + 
":  " + 
"(b('b3') <= 638.5) ? " + 
"(b('b6') <= 2127.0) ? " + 
"-0.0004765612337242943" + 
":  " + 
"-0.04802249688464326" + 
":  " + 
"(b('lia') <= 30.069433212280273) ? " + 
"0.0394718467936185" + 
":  " + 
"-0.002084281653011328" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -7.955878496170044) ? " + 
"(b('g0vh') <= -15.049027442932129) ? " + 
"(b('urban') <= 25.92040252685547) ? " + 
"-0.00019557252241780062" + 
":  " + 
"-0.00688053523297687" + 
":  " + 
"(b('g0vv') <= -8.635303497314453) ? " + 
"0.013406753043028295" + 
":  " + 
"-0.01027626231214061" + 
":  " + 
"(b('ndvi') <= 4453.5) ? " + 
"(b('b5') <= 3509.0) ? " + 
"0.01309834465842219" + 
":  " + 
"-0.012174732092716281" + 
":  " + 
"(b('b5') <= 2796.0) ? " + 
"-0.0289499504891078" + 
":  " + 
"0.013264762154281556" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2992.5) ? " + 
"(b('b5') <= 2793.5) ? " + 
"(b('b5') <= 2784.0) ? " + 
"-0.00020666036525858583" + 
":  " + 
"-0.035070598327122386" + 
":  " + 
"(b('b4') <= 798.0) ? " + 
"0.027576583773114706" + 
":  " + 
"0.004355094259542481" + 
":  " + 
"(b('b4') <= 545.0) ? " + 
"(b('l8dt') <= 518400.5) ? " + 
"0.0915023924101383" + 
":  " + 
"0.05324905924757932" + 
":  " + 
"(b('b3') <= 692.0) ? " + 
"-0.02560754284389789" + 
":  " + 
"-0.0009005710815375215" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b1') <= 583.5) ? " + 
"(b('b2') <= 777.5) ? " + 
"0.0062176616326179435" + 
":  " + 
"0.07086294074870034" + 
":  " + 
"(b('b6') <= 2987.5) ? " + 
"-0.019244744877986154" + 
":  " + 
"0.0018667231969896878" + 
":  " + 
"(b('grass') <= 2.471597671508789) ? " + 
"(b('lia') <= 41.84072494506836) ? " + 
"-0.00245691419520938" + 
":  " + 
"-0.037489413635606365" + 
":  " + 
"(b('trees') <= 4.231653451919556) ? " + 
"-0.001912617719946548" + 
":  " + 
"0.0014107616765222136" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 12.501765251159668) ? " + 
"(b('trees') <= 11.430836200714111) ? " + 
"(b('moss') <= 3.2275424003601074) ? " + 
"-0.002662570926690423" + 
":  " + 
"0.0012809311105631764" + 
":  " + 
"(b('lia') <= 34.949974060058594) ? " + 
"-0.00783962986288443" + 
":  " + 
"0.021704200268936342" + 
":  " + 
"(b('moss') <= 7.011075973510742) ? " + 
"(b('b6') <= 2862.0) ? " + 
"0.019288590653140685" + 
":  " + 
"-0.006371904333330213" + 
":  " + 
"(b('ndvi') <= 2731.5) ? " + 
"0.0037206076760829625" + 
":  " + 
"-0.01606482682190326" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1938.5) ? " + 
"(b('ndvi') <= 4669.5) ? " + 
"(b('b5') <= 1927.0) ? " + 
"0.0038895263570112647" + 
":  " + 
"0.034239171036402144" + 
":  " + 
"(b('grass') <= 39.79831123352051) ? " + 
"-0.035561235964926816" + 
":  " + 
"0.04740636374139012" + 
":  " + 
"(b('b3') <= 727.5) ? " + 
"(b('b6') <= 2762.5) ? " + 
"-0.0068283817668848" + 
":  " + 
"0.040121851716112975" + 
":  " + 
"(b('b11') <= 1383.5) ? " + 
"0.012124857469866605" + 
":  " + 
"-0.00037062897704390944" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 99.8344841003418) ? " + 
"(b('lia') <= 34.4125919342041) ? " + 
"(b('g0vv') <= -15.087001323699951) ? " + 
"-0.01405487685838698" + 
":  " + 
"-0.0014111092242776214" + 
":  " + 
"(b('lia') <= 34.449153900146484) ? " + 
"0.04754890584009751" + 
":  " + 
"0.0002719854800978681" + 
":  " + 
"(b('g0vh') <= -18.026637077331543) ? " + 
"(b('b4') <= 1418.5) ? " + 
"0.011447098577318182" + 
":  " + 
"-0.006319131208813336" + 
":  " + 
"(b('b7') <= 2435.5) ? " + 
"0.016769705146368823" + 
":  " + 
"0.10273276720909877" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 1724.5) ? " + 
"(b('lia') <= 41.805036544799805) ? " + 
"(b('b1') <= 68.5) ? " + 
"0.040650961180185706" + 
":  " + 
"-0.014338496622110088" + 
":  " + 
"(b('lia') <= 43.20364952087402) ? " + 
"0.08787678018730836" + 
":  " + 
"0.005524815179087616" + 
":  " + 
"(b('b6') <= 1921.0) ? " + 
"(b('g0vv') <= -14.124295234680176) ? " + 
"-0.042255741109791356" + 
":  " + 
"0.013588764343787394" + 
":  " + 
"(b('b6') <= 1935.5) ? " + 
"-0.030215158928782283" + 
":  " + 
"-5.537517569524866e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -23.391468048095703) ? " + 
"(b('lia') <= 36.29470252990723) ? " + 
"(b('b5') <= 2281.0) ? " + 
"-0.0008838522466401533" + 
":  " + 
"0.03426420458356272" + 
":  " + 
"(b('g0vh') <= -23.46958637237549) ? " + 
"-0.00212702461625131" + 
":  " + 
"-0.04476553552735518" + 
":  " + 
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('moss') <= 7.169239282608032) ? " + 
"-0.004118259646524159" + 
":  " + 
"0.0015137674476790133" + 
":  " + 
"(b('g0vv') <= -12.917322158813477) ? " + 
"0.027437773578635152" + 
":  " + 
"0.0005783611543296682" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3385.5) ? " + 
"(b('b5') <= 3316.5) ? " + 
"(b('b4') <= 2020.5) ? " + 
"0.0007681355530530326" + 
":  " + 
"-0.005892842183728491" + 
":  " + 
"(b('b4') <= 2201.0) ? " + 
"0.003368497087198175" + 
":  " + 
"0.040692413379642425" + 
":  " + 
"(b('grass') <= 79.93707656860352) ? " + 
"(b('b6') <= 1967.5) ? " + 
"0.029154362374865964" + 
":  " + 
"-0.004124143329350261" + 
":  " + 
"(b('b4') <= 1473.5) ? " + 
"0.14754237853378496" + 
":  " + 
"0.014544965272195813" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 657.5) ? " + 
"(b('b1') <= 650.5) ? " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-0.0009534517796370986" + 
":  " + 
"0.010246761963780757" + 
":  " + 
"(b('g0vh') <= -12.908830165863037) ? " + 
"-0.022762211711344734" + 
":  " + 
"0.1389919143927537" + 
":  " + 
"(b('ndvi') <= 2160.0) ? " + 
"(b('b5') <= 2062.5) ? " + 
"0.028243382088319426" + 
":  " + 
"-0.0001889498158537169" + 
":  " + 
"(b('g0vv') <= -7.345085859298706) ? " + 
"0.015395706498900227" + 
":  " + 
"-0.02607979597539293" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('ndvi') <= 1536.5) ? " + 
"(b('ndvi') <= 1383.5) ? " + 
"-0.00030738133511857456" + 
":  " + 
"-0.0074436466977878864" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-3.694275779993559e-05" + 
":  " + 
"0.014165530556408687" + 
":  " + 
"(b('b6') <= 2943.0) ? " + 
"(b('b2') <= 1206.5) ? " + 
"0.05824860366822131" + 
":  " + 
"0.03139964180847077" + 
":  " + 
"(b('lia') <= 36.049673080444336) ? " + 
"0.01664868389239984" + 
":  " + 
"0.004683374441546389" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -7.955878496170044) ? " + 
"(b('b1') <= 657.5) ? " + 
"(b('b4') <= 1439.75) ? " + 
"0.00018362928240876105" + 
":  " + 
"-0.005419862150398181" + 
":  " + 
"(b('ndvi') <= 2215.0) ? " + 
"0.00025685532832300795" + 
":  " + 
"0.01456876447748926" + 
":  " + 
"(b('ndvi') <= 2883.5) ? " + 
"(b('b6') <= 2764.0) ? " + 
"0.02241191495540733" + 
":  " + 
"0.002343165995229136" + 
":  " + 
"(b('moss') <= 7.30760383605957) ? " + 
"-0.007409033241613088" + 
":  " + 
"0.02433328843578598" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 19.819469451904297) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('moss') <= 18.02293586730957) ? " + 
"0.0002614275667534962" + 
":  " + 
"-0.017105317703944665" + 
":  " + 
"(b('g0vh') <= -21.567888259887695) ? " + 
"0.02680284981273455" + 
":  " + 
"0.08931993644444068" + 
":  " + 
"(b('grass') <= 67.60882186889648) ? " + 
"(b('b5') <= 1788.0) ? " + 
"0.1056448417980653" + 
":  " + 
"0.004146257261554451" + 
":  " + 
"(b('b2') <= 562.5) ? " + 
"-0.05257708092903158" + 
":  " + 
"-0.02167501089133622" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 28.096532821655273) ? " + 
"(b('moss') <= 16.90385627746582) ? " + 
"(b('moss') <= 14.077044010162354) ? " + 
"-0.013847765012467627" + 
":  " + 
"-0.06243966118212913" + 
":  " + 
"(b('b4') <= 1539.0) ? " + 
"0.044869964640955814" + 
":  " + 
"-0.013875188868711698" + 
":  " + 
"(b('lia') <= 28.386530876159668) ? " + 
"(b('b11') <= 1667.5) ? " + 
"-0.006598554967470533" + 
":  " + 
"0.03398196840765428" + 
":  " + 
"(b('lia') <= 28.638394355773926) ? " + 
"-0.012136703201065777" + 
":  " + 
"0.0001729977071718135" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 90.44964218139648) ? " + 
"(b('grass') <= 88.09611511230469) ? " + 
"(b('l8dt') <= 21116.5) ? " + 
"0.010403030208377536" + 
":  " + 
"-0.00022659883511479828" + 
":  " + 
"(b('g0vh') <= -19.338757514953613) ? " + 
"-0.041017642652699006" + 
":  " + 
"0.01337312038047638" + 
":  " + 
"(b('g0vh') <= -19.330784797668457) ? " + 
"(b('b1') <= 544.5) ? " + 
"0.014536009086467745" + 
":  " + 
"-0.004389089176882403" + 
":  " + 
"(b('g0vv') <= -13.6617431640625) ? " + 
"-0.0727008165342655" + 
":  " + 
"0.043285295410107734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.07048988342285) ? " + 
"(b('lia') <= 38.01721382141113) ? " + 
"(b('lia') <= 37.84523963928223) ? " + 
"-0.0010040736677036884" + 
":  " + 
"0.022915725466967535" + 
":  " + 
"(b('grass') <= 49.92256546020508) ? " + 
"-0.0237577128867652" + 
":  " + 
"-0.07788200869192179" + 
":  " + 
"(b('lia') <= 38.16269874572754) ? " + 
"(b('b2') <= 611.0) ? " + 
"0.048524552975155" + 
":  " + 
"-0.021869185330367556" + 
":  " + 
"(b('b5') <= 2992.5) ? " + 
"0.0026550620210620303" + 
":  " + 
"-0.0024361592101414414" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 292.5) ? " + 
"(b('l8dt') <= 1000294.0) ? " + 
"(b('l8dt') <= 518400.5) ? " + 
"-0.04258543291037672" + 
":  " + 
"-0.046321752903315985" + 
":  " + 
"(b('b7') <= 2339.5) ? " + 
"-0.06450866302743404" + 
":  " + 
"-0.06760936980293357" + 
":  " + 
"(b('b2') <= 957.75) ? " + 
"(b('moss') <= 19.819469451904297) ? " + 
"-9.573644106053288e-05" + 
":  " + 
"-0.010891034791197938" + 
":  " + 
"(b('b4') <= 1807.0) ? " + 
"0.01930478919063291" + 
":  " + 
"0.0006485051651184056" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 27.25572967529297) ? " + 
"(b('b5') <= 2356.0) ? " + 
"(b('b10') <= 2132.5) ? " + 
"-0.014671555917754311" + 
":  " + 
"0.032292884691643535" + 
":  " + 
"(b('g0vh') <= -22.59356117248535) ? " + 
"0.012851374849027038" + 
":  " + 
"-0.02733413570386954" + 
":  " + 
"(b('lia') <= 27.311138153076172) ? " + 
"(b('b4') <= 1477.0) ? " + 
"0.06930309786396677" + 
":  " + 
"-0.01641093290596361" + 
":  " + 
"(b('grass') <= 99.8344841003418) ? " + 
"-0.00016991442341662786" + 
":  " + 
"0.008431406117524617" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.282082080841064) ? " + 
"(b('b3') <= 600.0) ? " + 
"(b('b4') <= 534.0) ? " + 
"0.038278473521202554" + 
":  " + 
"-0.05550747734861402" + 
":  " + 
"(b('b4') <= 759.0) ? " + 
"0.02514499372977378" + 
":  " + 
"-0.003675827362968891" + 
":  " + 
"(b('grass') <= 90.44964218139648) ? " + 
"(b('trees') <= 4.231653451919556) ? " + 
"-0.0014355673532334462" + 
":  " + 
"0.00177510762461951" + 
":  " + 
"(b('grass') <= 93.51450729370117) ? " + 
"0.08660356417992926" + 
":  " + 
"0.007038614323663425" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 761.5) ? " + 
"(b('b5') <= 3139.5) ? " + 
"(b('moss') <= 0.2824763059616089) ? " + 
"-0.012966044859653992" + 
":  " + 
"0.0023301246415097865" + 
":  " + 
"(b('b5') <= 3226.5) ? " + 
"-0.039094240927079305" + 
":  " + 
"-0.009139899693783185" + 
":  " + 
"(b('b4') <= 697.5) ? " + 
"(b('bare') <= 5.588325500488281) ? " + 
"0.015735266269768247" + 
":  " + 
"0.11820643082442138" + 
":  " + 
"(b('b6') <= 1850.5) ? " + 
"0.033922515235213405" + 
":  " + 
"6.189003587733077e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 1.9490950107574463) ? " + 
"(b('lia') <= 30.312915802001953) ? " + 
"(b('lia') <= 29.140652656555176) ? " + 
"-0.0011199206353311104" + 
":  " + 
"0.01372150719780682" + 
":  " + 
"(b('grass') <= 60.067331314086914) ? " + 
"0.0013865746153808019" + 
":  " + 
"-0.00306183016885865" + 
":  " + 
"(b('b5') <= 4200.0) ? " + 
"(b('b1') <= 436.5) ? " + 
"-0.006333537288398872" + 
":  " + 
"0.003057375143052911" + 
":  " + 
"(b('b1') <= 447.0) ? " + 
"0.13881008425205305" + 
":  " + 
"0.026041352106726257" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 43.82485580444336) ? " + 
"(b('lia') <= 43.48938179016113) ? " + 
"(b('lia') <= 42.24803924560547) ? " + 
"-0.0003099862623998258" + 
":  " + 
"0.005534277162033465" + 
":  " + 
"(b('g0vh') <= -22.849122047424316) ? " + 
"0.12818618877502924" + 
":  " + 
"-0.011355230527057916" + 
":  " + 
"(b('lia') <= 44.065185546875) ? " + 
"(b('b10') <= 3213.5) ? " + 
"0.01435539284266218" + 
":  " + 
"0.06616883666243684" + 
":  " + 
"(b('g0vh') <= -16.778313636779785) ? " + 
"-0.003429016154282265" + 
":  " + 
"0.020707624170007856" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 1709.0) ? " + 
"(b('ndvi') <= 1441.0) ? " + 
"(b('b6') <= 1695.5) ? " + 
"0.06350463773812229" + 
":  " + 
"-0.11324605389773099" + 
":  " + 
"(b('b7') <= 1098.0) ? " + 
"-0.005390255794643401" + 
":  " + 
"-0.049417119688427054" + 
":  " + 
"(b('b2') <= 314.5) ? " + 
"(b('b2') <= 298.5) ? " + 
"0.00408601524145728" + 
":  " + 
"0.03682932365651974" + 
":  " + 
"(b('b2') <= 347.5) ? " + 
"-0.016162214622404983" + 
":  " + 
"0.00028306958788861864" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3533.0) ? " + 
"(b('b5') <= 3531.0) ? " + 
"(b('crop') <= 67.1409683227539) ? " + 
"-0.0007095168214089945" + 
":  " + 
"0.00295959433920453" + 
":  " + 
"(b('g0vv') <= -11.015426635742188) ? " + 
"-0.017485732734131065" + 
":  " + 
"0.09298363489200602" + 
":  " + 
"(b('crop') <= 62.33124351501465) ? " + 
"(b('b4') <= 1144.5) ? " + 
"0.018781988649887373" + 
":  " + 
"-0.0077236659112388285" + 
":  " + 
"(b('b1') <= 617.0) ? " + 
"-0.015604523236312177" + 
":  " + 
"0.00381844747175901" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b1') <= 688.5) ? " + 
"(b('b2') <= 515.0) ? " + 
"-0.002799140589413864" + 
":  " + 
"0.008894291935338474" + 
":  " + 
"(b('g0vv') <= -11.10599946975708) ? " + 
"0.003703252253603963" + 
":  " + 
"-0.011161536198727121" + 
":  " + 
"(b('crop') <= 77.41421890258789) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.0005032499265311068" + 
":  " + 
"0.010719081232655202" + 
":  " + 
"(b('grass') <= 11.09217882156372) ? " + 
"-0.001090373075623595" + 
":  " + 
"-0.023881996664143226" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 4627.5) ? " + 
"(b('ndvi') <= 4602.5) ? " + 
"(b('crop') <= 85.84851455688477) ? " + 
"-0.00043957771440741536" + 
":  " + 
"0.005214892789717795" + 
":  " + 
"(b('bare') <= 1.3686903417110443) ? " + 
"0.015416348520264989" + 
":  " + 
"0.08394634341392285" + 
":  " + 
"(b('crop') <= 87.44597244262695) ? " + 
"(b('b6') <= 2154.5) ? " + 
"-0.01953767799763111" + 
":  " + 
"0.003750940063641973" + 
":  " + 
"(b('b6') <= 1859.0) ? " + 
"0.019119051083467776" + 
":  " + 
"-0.029499026024122847" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('ndvi') <= 1190.5) ? " + 
"(b('b4') <= 924.0) ? " + 
"-0.08014781563407843" + 
":  " + 
"-0.0032060298871438987" + 
":  " + 
"(b('bare') <= 29.32122039794922) ? " + 
"0.00022332996707307627" + 
":  " + 
"0.06408092719839181" + 
":  " + 
"(b('b2') <= 1363.5) ? " + 
"(b('l8dt') <= 49428.5) ? " + 
"0.03614031084927535" + 
":  " + 
"0.01522765657391322" + 
":  " + 
"(b('lia') <= 42.78291702270508) ? " + 
"0.010153680446661926" + 
":  " + 
"-0.0026713583031194054" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1935.5) ? " + 
"(b('b5') <= 1927.0) ? " + 
"(b('b2') <= 705.0) ? " + 
"0.0006879641743473031" + 
":  " + 
"0.028379198714997698" + 
":  " + 
"(b('trees') <= 8.625309228897095) ? " + 
"0.021707854180446986" + 
":  " + 
"0.09772618730126616" + 
":  " + 
"(b('b5') <= 2314.5) ? " + 
"(b('crop') <= 4.842228651046753) ? " + 
"-0.010703215968643928" + 
":  " + 
"0.004855520671322963" + 
":  " + 
"(b('grass') <= 35.55763244628906) ? " + 
"-0.001800564052214677" + 
":  " + 
"0.004516576340693593" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -14.666974544525146) ? " + 
"(b('ndvi') <= 4627.5) ? " + 
"(b('ndvi') <= 4602.5) ? " + 
"4.795676396725816e-05" + 
":  " + 
"0.04318014226091725" + 
":  " + 
"(b('g0vh') <= -17.853862762451172) ? " + 
"0.004470804638375506" + 
":  " + 
"-0.013028869592145402" + 
":  " + 
"(b('crop') <= 93.26061248779297) ? " + 
"(b('crop') <= 64.4262866973877) ? " + 
"-0.0037007535633937576" + 
":  " + 
"0.014943456534894855" + 
":  " + 
"(b('b1') <= 328.5) ? " + 
"0.017024651778954014" + 
":  " + 
"-0.028882952848020484" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -10.249711990356445) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"-0.0005622492100080843" + 
":  " + 
"0.03901487361823178" + 
":  " + 
"(b('ndvi') <= 2906.0) ? " + 
"-0.06849906262650057" + 
":  " + 
"-0.0034803167393722043" + 
":  " + 
"(b('grass') <= 9.205488204956055) ? " + 
"(b('b4') <= 699.0) ? " + 
"-0.021385502104673" + 
":  " + 
"-0.00142357066598119" + 
":  " + 
"(b('crop') <= 68.24193572998047) ? " + 
"0.001336384729152466" + 
":  " + 
"0.015424411139979189" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('b1') <= 827.0) ? " + 
"-0.002008042305454396" + 
":  " + 
"0.021572817978573456" + 
":  " + 
"(b('b11') <= 2383.0) ? " + 
"0.018737586033285243" + 
":  " + 
"0.0814323172178396" + 
":  " + 
"(b('b4') <= 715.5) ? " + 
"(b('grass') <= 23.295454025268555) ? " + 
"0.004349258977651108" + 
":  " + 
"0.03448370473420989" + 
":  " + 
"(b('b3') <= 882.5) ? " + 
"-0.005799159974312765" + 
":  " + 
"0.0016925359016349496" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1292.5) ? " + 
"(b('b3') <= 1054.5) ? " + 
"(b('crop') <= 43.67561912536621) ? " + 
"0.0036991898823898342" + 
":  " + 
"-0.00242307541577979" + 
":  " + 
"(b('trees') <= 9.308863162994385) ? " + 
"0.030553897972100244" + 
":  " + 
"-0.004850927246933725" + 
":  " + 
"(b('b6') <= 2212.0) ? " + 
"(b('b6') <= 2126.0) ? " + 
"-0.08163715325740212" + 
":  " + 
"-0.03625305768350841" + 
":  " + 
"(b('b3') <= 998.5) ? " + 
"-0.013744320255566262" + 
":  " + 
"-0.0003606259939599015" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('b11') <= 2199.5) ? " + 
"(b('b2') <= 865.5) ? " + 
"-0.005094028432675119" + 
":  " + 
"0.055816805651457926" + 
":  " + 
"(b('crop') <= 4.842228651046753) ? " + 
"-0.003159932153498967" + 
":  " + 
"0.006716030639612635" + 
":  " + 
"(b('trees') <= 8.639616012573242) ? " + 
"(b('b5') <= 1991.5) ? " + 
"0.007563106495273278" + 
":  " + 
"-0.0015587342357062486" + 
":  " + 
"(b('urban') <= 14.72341012954712) ? " + 
"0.0033934354726237047" + 
":  " + 
"0.04980623491271734" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 608.5) ? " + 
"(b('b5') <= 2594.5) ? " + 
"(b('b5') <= 1564.5) ? " + 
"0.004861130917578356" + 
":  " + 
"-0.018175224935764532" + 
":  " + 
"(b('l8dt') <= 4904117.5) ? " + 
"0.01972240318202374" + 
":  " + 
"-0.10273568619361823" + 
":  " + 
"(b('b3') <= 624.5) ? " + 
"(b('b5') <= 2989.0) ? " + 
"0.004076932977911291" + 
":  " + 
"0.05042014381555849" + 
":  " + 
"(b('b3') <= 630.5) ? " + 
"-0.021617161519110483" + 
":  " + 
"0.00018459370454112763" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 362.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"(b('b5') <= 2161.0) ? " + 
"0.009296694540970965" + 
":  " + 
"-0.005066750963069994" + 
":  " + 
"(b('b11') <= 1330.0) ? " + 
"-0.00631328145577518" + 
":  " + 
"0.028804473519869315" + 
":  " + 
"(b('b1') <= 400.5) ? " + 
"(b('b4') <= 1122.0) ? " + 
"-0.013699227749945099" + 
":  " + 
"0.008071515738956578" + 
":  " + 
"(b('b2') <= 517.5) ? " + 
"0.013133646128393052" + 
":  " + 
"-0.0001716761808627661" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.32249927520752) ? " + 
"(b('b7') <= 1416.5) ? " + 
"(b('b4') <= 532.5) ? " + 
"0.020538041353184502" + 
":  " + 
"-0.022961407936072813" + 
":  " + 
"(b('b4') <= 976.5) ? " + 
"0.014660519394765707" + 
":  " + 
"-0.00349832072589624" + 
":  " + 
"(b('l8dt') <= 322756.5) ? " + 
"(b('grass') <= 11.09217882156372) ? " + 
"0.003444452192546946" + 
":  " + 
"-0.0032688627496857228" + 
":  " + 
"(b('moss') <= 20.739794731140137) ? " + 
"0.0012260170294598701" + 
":  " + 
"0.021296119598673894" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 18.02293586730957) ? " + 
"(b('moss') <= 17.294462203979492) ? " + 
"(b('lia') <= 27.911441802978516) ? " + 
"-0.014996475771996639" + 
":  " + 
"0.00019195575720642262" + 
":  " + 
"(b('b1') <= 609.5) ? " + 
"0.06389568432623315" + 
":  " + 
"0.0011543511639772375" + 
":  " + 
"(b('lia') <= 29.166658401489258) ? " + 
"(b('g0vv') <= -15.313351154327393) ? " + 
"0.00046654876067429044" + 
":  " + 
"0.07251977732386469" + 
":  " + 
"(b('b3') <= 810.5) ? " + 
"-0.021840208622392044" + 
":  " + 
"-0.0012109647556813885" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 98.36243438720703) ? " + 
"(b('lia') <= 34.4125919342041) ? " + 
"(b('g0vv') <= -11.86080265045166) ? " + 
"-0.006697859624657754" + 
":  " + 
"0.0008338886295461316" + 
":  " + 
"(b('lia') <= 34.449153900146484) ? " + 
"0.041586504364782124" + 
":  " + 
"0.0002837971264253276" + 
":  " + 
"(b('b5') <= 2469.0) ? " + 
"(b('b2') <= 975.5) ? " + 
"0.01076411583582448" + 
":  " + 
"0.09049300039841737" + 
":  " + 
"(b('g0vh') <= -23.450998306274414) ? " + 
"0.06995701248567869" + 
":  " + 
"-0.00776794857295043" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('b1') <= 827.0) ? " + 
"-0.001907104504328062" + 
":  " + 
"0.01866733849812579" + 
":  " + 
"(b('lia') <= 38.8431282043457) ? " + 
"0.028641207457960276" + 
":  " + 
"-0.01965033394517207" + 
":  " + 
"(b('b4') <= 787.0) ? " + 
"(b('grass') <= 22.319518089294434) ? " + 
"0.0007900270193117541" + 
":  " + 
"0.027130372009029687" + 
":  " + 
"(b('trees') <= 1.1431602239608765) ? " + 
"0.003529376758739796" + 
":  " + 
"-0.0036945642172666886" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 4.231653451919556) ? " + 
"(b('trees') <= 3.533814549446106) ? " + 
"(b('lia') <= 39.43572425842285) ? " + 
"-0.0023864881539140837" + 
":  " + 
"0.002823783100220232" + 
":  " + 
"(b('b5') <= 1756.0) ? " + 
"0.01968634265594213" + 
":  " + 
"-0.02039386409029948" + 
":  " + 
"(b('trees') <= 6.304144859313965) ? " + 
"(b('moss') <= 0.044692736119031906) ? " + 
"0.04390219928076766" + 
":  " + 
"0.008083134136947225" + 
":  " + 
"(b('lia') <= 41.83385467529297) ? " + 
"0.0013704090749771078" + 
":  " + 
"-0.007175488892077511" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1381.5) ? " + 
"(b('b3') <= 1062.5) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"-0.00019412039879623577" + 
":  " + 
"0.031961230573490367" + 
":  " + 
"(b('grass') <= 76.86819076538086) ? " + 
"0.005396136483984976" + 
":  " + 
"0.03296724462316109" + 
":  " + 
"(b('b11') <= 1680.5) ? " + 
"(b('trees') <= 2.170520305633545) ? " + 
"0.018570993161366574" + 
":  " + 
"0.13373730320343374" + 
":  " + 
"(b('b3') <= 1112.5) ? " + 
"-0.01036057116578215" + 
":  " + 
"-0.0004216765267685296" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3533.0) ? " + 
"(b('b5') <= 3531.0) ? " + 
"(b('g0vh') <= -15.942423343658447) ? " + 
"-0.00019771443678404015" + 
":  " + 
"0.0045663010195936115" + 
":  " + 
"(b('g0vh') <= -16.89544153213501) ? " + 
"-0.016064270182554394" + 
":  " + 
"0.08266555500562521" + 
":  " + 
"(b('crop') <= 62.33124351501465) ? " + 
"(b('b4') <= 1144.5) ? " + 
"0.016383189988860156" + 
":  " + 
"-0.006998016394554896" + 
":  " + 
"(b('b1') <= 617.0) ? " + 
"-0.013888590996638589" + 
":  " + 
"0.0026610372432151605" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 1724.5) ? " + 
"(b('ndvi') <= 2411.0) ? " + 
"(b('b5') <= 2214.5) ? " + 
"-0.00023435011146370136" + 
":  " + 
"0.08321475863888195" + 
":  " + 
"(b('b6') <= 1584.5) ? " + 
"-0.0035234671866881235" + 
":  " + 
"-0.034197826241734536" + 
":  " + 
"(b('b10') <= 1022.5) ? " + 
"(b('g0vh') <= -18.622857093811035) ? " + 
"-0.02833955410689771" + 
":  " + 
"0.02730915147581503" + 
":  " + 
"(b('b3') <= 506.5) ? " + 
"-0.05037307903002503" + 
":  " + 
"5.819755954967468e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5456.5) ? " + 
"(b('b5') <= 1280.0) ? " + 
"(b('b7') <= 672.0) ? " + 
"-0.05303598111853096" + 
":  " + 
"-0.022469468025491258" + 
":  " + 
"(b('b5') <= 1439.0) ? " + 
"0.011954312438820659" + 
":  " + 
"-3.178783450798617e-05" + 
":  " + 
"(b('g0vh') <= -19.21955966949463) ? " + 
"(b('lia') <= 39.747976303100586) ? " + 
"-0.00431678936186021" + 
":  " + 
"-0.02483340401398" + 
":  " + 
"(b('b3') <= 2114.5) ? " + 
"-0.08425770082922296" + 
":  " + 
"-0.049632365471500295" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 608.5) ? " + 
"(b('b5') <= 2594.5) ? " + 
"(b('b5') <= 1498.0) ? " + 
"0.0044643770179362795" + 
":  " + 
"-0.015875625880545287" + 
":  " + 
"(b('b5') <= 3092.5) ? " + 
"0.016524762922816072" + 
":  " + 
"-0.12554979113436338" + 
":  " + 
"(b('b4') <= 757.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"-0.0015850347895322529" + 
":  " + 
"0.02350734108701117" + 
":  " + 
"(b('b1') <= 259.0) ? " + 
"-0.015863209824701283" + 
":  " + 
"-8.032238609945896e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 666.5) ? " + 
"(b('b6') <= 2762.5) ? " + 
"(b('b2') <= 314.5) ? " + 
"0.006280742676731513" + 
":  " + 
"-0.009889190410722669" + 
":  " + 
"(b('b3') <= 655.5) ? " + 
"0.04382822291109118" + 
":  " + 
"-0.08629881877197766" + 
":  " + 
"(b('b3') <= 684.5) ? " + 
"(b('b1') <= 304.5) ? " + 
"0.02995706426165741" + 
":  " + 
"0.0013370487336088685" + 
":  " + 
"(b('b11') <= 1013.5) ? " + 
"0.02770280472009933" + 
":  " + 
"-0.00019392276447670055" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -20.058966636657715) ? " + 
"(b('g0vh') <= -22.129555702209473) ? " + 
"(b('trees') <= 5.7725629806518555) ? " + 
"0.03611167088725649" + 
":  " + 
"0.014518418123145499" + 
":  " + 
"(b('ndvi') <= 1507.0) ? " + 
"0.059001096735226743" + 
":  " + 
"0.055791292098979546" + 
":  " + 
"(b('g0vv') <= -16.012653350830078) ? " + 
"(b('ndvi') <= 3372.0) ? " + 
"-0.002116174205394187" + 
":  " + 
"-0.031492963064485714" + 
":  " + 
"(b('grass') <= 98.36243438720703) ? " + 
"1.559533216952159e-05" + 
":  " + 
"0.00882050966006183" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 292.5) ? " + 
"(b('l8dt') <= 1000294.0) ? " + 
"(b('l8dt') <= 518400.5) ? " + 
"-0.037222021216518617" + 
":  " + 
"-0.041477292580470324" + 
":  " + 
"(b('b1') <= 1099.0) ? " + 
"-0.057845511692176554" + 
":  " + 
"-0.06063614779012613" + 
":  " + 
"(b('b3') <= 761.5) ? " + 
"(b('moss') <= 0.2824763059616089) ? " + 
"-0.012175049636017241" + 
":  " + 
"4.2846479773361484e-05" + 
":  " + 
"(b('b4') <= 839.5) ? " + 
"0.008734676424723756" + 
":  " + 
"-0.0001479851546202575" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 65.5) ? " + 
"(b('b4') <= 339.0) ? " + 
"(b('g0vh') <= -20.64984130859375) ? " + 
"0.06039259027819379" + 
":  " + 
"0.03523367287031626" + 
":  " + 
"-0.013310098697597805" + 
":  " + 
"(b('b6') <= 1529.5) ? " + 
"(b('b11') <= 1095.0) ? " + 
"-0.006670773517994843" + 
":  " + 
"-0.07920349067279285" + 
":  " + 
"(b('b2') <= 231.5) ? " + 
"-0.11287070363278387" + 
":  " + 
"0.00010660773632050311" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3385.5) ? " + 
"(b('crop') <= 67.1409683227539) ? " + 
"(b('crop') <= 62.41747283935547) ? " + 
"0.0002980649544761669" + 
":  " + 
"-0.008959105302575942" + 
":  " + 
"(b('trees') <= 14.932132720947266) ? " + 
"0.0022755029935952833" + 
":  " + 
"0.05371932320062355" + 
":  " + 
"(b('grass') <= 79.93707656860352) ? " + 
"(b('b3') <= 1465.5) ? " + 
"-0.006140178616681118" + 
":  " + 
"0.003863223260344377" + 
":  " + 
"(b('l8dt') <= 698872.5) ? " + 
"0.03527754606025701" + 
":  " + 
"0.18304647580651795" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1536.5) ? " + 
"(b('ndvi') <= 1383.5) ? " + 
"(b('b4') <= 1522.5) ? " + 
"0.006448081559746218" + 
":  " + 
"-0.002245970003760765" + 
":  " + 
"(b('bare') <= 2.0621386766433716) ? " + 
"-0.011601607627228259" + 
":  " + 
"0.0003645605525325966" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('bare') <= 6.473585605621338) ? " + 
"0.0005572490302841456" + 
":  " + 
"-0.013362477670804968" + 
":  " + 
"(b('b5') <= 2475.5) ? " + 
"-0.004948061639683275" + 
":  " + 
"0.020464620585820676" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 60.067331314086914) ? " + 
"(b('grass') <= 46.57049369812012) ? " + 
"(b('b5') <= 2170.5) ? " + 
"0.006903266538064987" + 
":  " + 
"-0.0013797071015666754" + 
":  " + 
"(b('crop') <= 1.4046242237091064) ? " + 
"-0.005250019996180721" + 
":  " + 
"0.023762214284908205" + 
":  " + 
"(b('crop') <= 35.05769157409668) ? " + 
"(b('b5') <= 2315.5) ? " + 
"-0.0061317946609300514" + 
":  " + 
"0.003751922043329333" + 
":  " + 
"(b('lia') <= 37.17656898498535) ? " + 
"-0.0433441949919721" + 
":  " + 
"-0.07367737275748348" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 11.09217882156372) ? " + 
"(b('grass') <= 8.483705759048462) ? " + 
"(b('ndvi') <= 3656.5) ? " + 
"0.002101276508064462" + 
":  " + 
"-0.008480195205416036" + 
":  " + 
"(b('lia') <= 43.16842460632324) ? " + 
"0.007560408899557035" + 
":  " + 
"0.059566195249013756" + 
":  " + 
"(b('crop') <= 77.41421890258789) ? " + 
"(b('crop') <= 68.24193572998047) ? " + 
"-0.0009330281400393683" + 
":  " + 
"0.010022867236655035" + 
":  " + 
"(b('b5') <= 2739.0) ? " + 
"-0.00022500992728626408" + 
":  " + 
"-0.030381481838386445" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 13.811414241790771) ? " + 
"(b('trees') <= 13.466797828674316) ? " + 
"(b('b4') <= 757.5) ? " + 
"0.003501968902646667" + 
":  " + 
"-0.00048396178435126925" + 
":  " + 
"(b('ndvi') <= 3281.0) ? " + 
"0.08920410347050643" + 
":  " + 
"-0.028990934726498906" + 
":  " + 
"(b('moss') <= 6.853561639785767) ? " + 
"(b('ndvi') <= 5096.5) ? " + 
"-0.00020376052784874287" + 
":  " + 
"0.04128071110651734" + 
":  " + 
"(b('ndvi') <= 1165.5) ? " + 
"0.12353860679799829" + 
":  " + 
"-0.01313207568467791" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 761.5) ? " + 
"(b('ndvi') <= 1132.5) ? " + 
"(b('l8dt') <= 717558.5) ? " + 
"-0.06220114708445174" + 
":  " + 
"-0.08770399022921009" + 
":  " + 
"(b('b5') <= 3139.5) ? " + 
"-0.00015550505335878203" + 
":  " + 
"-0.013256144164048777" + 
":  " + 
"(b('b10') <= 1484.5) ? " + 
"(b('g0vh') <= -22.19931697845459) ? " + 
"0.12843633865713602" + 
":  " + 
"0.00839220427767063" + 
":  " + 
"(b('b1') <= 307.5) ? " + 
"-0.02076907447158612" + 
":  " + 
"0.00028722629710321217" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 666.5) ? " + 
"(b('crop') <= 48.6511173248291) ? " + 
"(b('ndvi') <= 5584.0) ? " + 
"0.0017171840271463454" + 
":  " + 
"0.14988174465751428" + 
":  " + 
"(b('b5') <= 1852.5) ? " + 
"0.0019825416329521187" + 
":  " + 
"-0.022411460637778397" + 
":  " + 
"(b('b3') <= 684.5) ? " + 
"(b('trees') <= 11.701707363128662) ? " + 
"0.017603176045169297" + 
":  " + 
"-0.018618961523461826" + 
":  " + 
"(b('b3') <= 727.5) ? " + 
"-0.007362067335636694" + 
":  " + 
"0.00040829104648338325" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.31542158126831) ? " + 
"(b('b2') <= 1020.0) ? " + 
"(b('l8dt') <= 564876.5) ? " + 
"-0.0002270550515800311" + 
":  " + 
"-0.008782294860983468" + 
":  " + 
"(b('bare') <= 0.2048390582203865) ? " + 
"0.04026829083651583" + 
":  " + 
"-0.0013989312055912417" + 
":  " + 
"(b('grass') <= 90.44964218139648) ? " + 
"(b('trees') <= 4.231653451919556) ? " + 
"-0.001050758210501686" + 
":  " + 
"0.001737723057409505" + 
":  " + 
"(b('b5') <= 2526.5) ? " + 
"0.02008154811855248" + 
":  " + 
"-0.009741772049527723" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 1.8034681677818298) ? " + 
"(b('b1') <= 583.5) ? " + 
"(b('b2') <= 777.5) ? " + 
"0.005885908273955262" + 
":  " + 
"0.06214802180986434" + 
":  " + 
"(b('b6') <= 2987.5) ? " + 
"-0.01651545293108074" + 
":  " + 
"0.0009144377308174938" + 
":  " + 
"(b('grass') <= 2.471597671508789) ? " + 
"(b('b11') <= 3035.0) ? " + 
"-0.025695204019974795" + 
":  " + 
"0.016581137871412584" + 
":  " + 
"(b('b10') <= 3244.5) ? " + 
"-0.0005524097265942055" + 
":  " + 
"0.005156592761695329" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 28.096532821655273) ? " + 
"(b('b5') <= 1951.0) ? " + 
"(b('b1') <= 308.0) ? " + 
"-0.050680192382583894" + 
":  " + 
"0.06868181524560941" + 
":  " + 
"(b('moss') <= 16.90385627746582) ? " + 
"-0.01432218418931033" + 
":  " + 
"0.005505988037442999" + 
":  " + 
"(b('lia') <= 28.386530876159668) ? " + 
"(b('l8dt') <= 1871767.5) ? " + 
"0.014760991147440106" + 
":  " + 
"0.08169419282944093" + 
":  " + 
"(b('lia') <= 28.638394355773926) ? " + 
"-0.009439010948240668" + 
":  " + 
"0.00014737109439020047" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('l8dt') <= 20391.0) ? " + 
"0.01875756255844135" + 
":  " + 
"-0.0017660127464056102" + 
":  " + 
"(b('b6') <= 2517.0) ? " + 
"-0.020572163599385337" + 
":  " + 
"0.025242319267909676" + 
":  " + 
"(b('ndvi') <= 3929.5) ? " + 
"(b('bare') <= 0.35301104187965393) ? " + 
"0.0226964563449536" + 
":  " + 
"-0.0003718822266599128" + 
":  " + 
"(b('b5') <= 3954.0) ? " + 
"0.012188379215087747" + 
":  " + 
"-0.0083948053671349" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 16563.0) ? " + 
"(b('b2') <= 911.5) ? " + 
"(b('grass') <= 78.08131408691406) ? " + 
"-0.009062907061267129" + 
":  " + 
"-0.05026869148366315" + 
":  " + 
"(b('b4') <= 2190.0) ? " + 
"0.08554707401270457" + 
":  " + 
"0.16483823813255252" + 
":  " + 
"(b('l8dt') <= 20391.0) ? " + 
"(b('bare') <= 0.4333333373069763) ? " + 
"0.06365249216363764" + 
":  " + 
"-0.026015792070554256" + 
":  " + 
"(b('l8dt') <= 50860.5) ? " + 
"-0.005477714379629935" + 
":  " + 
"0.00022677903078668313" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -11.432883739471436) ? " + 
"(b('g0vh') <= -14.666974544525146) ? " + 
"(b('ndvi') <= 4627.5) ? " + 
"0.00015624109800725343" + 
":  " + 
"-0.005024456367830637" + 
":  " + 
"(b('urban') <= 29.42727279663086) ? " + 
"0.002609931382358117" + 
":  " + 
"0.032318824956601794" + 
":  " + 
"(b('l8dt') <= 1123644.5) ? " + 
"(b('lia') <= 34.40300369262695) ? " + 
"-0.034692569550660746" + 
":  " + 
"-0.09396557376703792" + 
":  " + 
"(b('b4') <= 1200.0) ? " + 
"-0.016000705262596247" + 
":  " + 
"0.038000463120844805" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 44.96173286437988) ? " + 
"(b('g0vv') <= -15.087481021881104) ? " + 
"(b('lia') <= 34.2064266204834) ? " + 
"-0.009865540844224667" + 
":  " + 
"-3.529942046024763e-05" + 
":  " + 
"(b('g0vv') <= -15.038439273834229) ? " + 
"0.03128307645553942" + 
":  " + 
"0.00023302989204496746" + 
":  " + 
"0.1019747426987011" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 608.5) ? " + 
"(b('b2') <= 314.5) ? " + 
"(b('b2') <= 304.5) ? " + 
"-0.00019137208304732502" + 
":  " + 
"0.051055500070770296" + 
":  " + 
"(b('b5') <= 1746.0) ? " + 
"0.003265760695999548" + 
":  " + 
"-0.0264525531188526" + 
":  " + 
"(b('b4') <= 919.5) ? " + 
"(b('grass') <= 76.45126724243164) ? " + 
"0.0004880652812886929" + 
":  " + 
"0.023040620489719457" + 
":  " + 
"(b('b3') <= 888.5) ? " + 
"-0.006249676884086475" + 
":  " + 
"0.0003887746043780073" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('ndvi') <= 1190.5) ? " + 
"(b('b5') <= 2062.5) ? " + 
"0.01197968647603" + 
":  " + 
"-0.005868906120954487" + 
":  " + 
"(b('bare') <= 29.32122039794922) ? " + 
"0.0002316124686893369" + 
":  " + 
"0.05335913856497074" + 
":  " + 
"(b('b7') <= 2777.5) ? " + 
"(b('b3') <= 1637.0) ? " + 
"0.04913473778846532" + 
":  " + 
"0.023709566141357646" + 
":  " + 
"(b('lia') <= 42.78582572937012) ? " + 
"0.009987340615452991" + 
":  " + 
"-0.0023204360558911623" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5456.5) ? " + 
"(b('crop') <= 85.84851455688477) ? " + 
"(b('crop') <= 85.4493522644043) ? " + 
"5.7580914835478504e-05" + 
":  " + 
"-0.02123732998904354" + 
":  " + 
"(b('ndvi') <= 3929.0) ? " + 
"0.006079319920118477" + 
":  " + 
"-0.012414657377128518" + 
":  " + 
"(b('g0vh') <= -19.21955966949463) ? " + 
"(b('lia') <= 39.747976303100586) ? " + 
"-0.004197706072430474" + 
":  " + 
"-0.022194877378164918" + 
":  " + 
"(b('ndvi') <= 1449.5) ? " + 
"-0.044358015396208726" + 
":  " + 
"-0.0762859241546825" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1280.0) ? " + 
"(b('g0vv') <= -13.93202829360962) ? " + 
"(b('b4') <= 437.5) ? " + 
"0.00947408276702083" + 
":  " + 
"-0.014778136450212559" + 
":  " + 
"(b('g0vh') <= -17.386487007141113) ? " + 
"-0.03387316261914293" + 
":  " + 
"-0.0059670942537122795" + 
":  " + 
"(b('b4') <= 1274.5) ? " + 
"(b('b2') <= 653.5) ? " + 
"-0.0002598338570833497" + 
":  " + 
"0.009321555499142004" + 
":  " + 
"(b('b6') <= 2212.0) ? " + 
"-0.05259442142346968" + 
":  " + 
"-0.0007900084749635976" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 18.02293586730957) ? " + 
"(b('moss') <= 17.294462203979492) ? " + 
"(b('lia') <= 27.911441802978516) ? " + 
"-0.012334053228218895" + 
":  " + 
"0.00016913498345692441" + 
":  " + 
"(b('b1') <= 609.5) ? " + 
"0.05666459587232948" + 
":  " + 
"0.0005168155157089039" + 
":  " + 
"(b('b10') <= 1761.0) ? " + 
"(b('g0vv') <= -10.936163425445557) ? " + 
"-0.030501836434447198" + 
":  " + 
"0.021559141763518" + 
":  " + 
"(b('b5') <= 1786.5) ? " + 
"0.05736568945465343" + 
":  " + 
"-0.00135622521460923" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 13.571214199066162) ? " + 
"(b('trees') <= 13.466797828674316) ? " + 
"(b('b4') <= 757.5) ? " + 
"0.0033480316282856353" + 
":  " + 
"-0.0004774340358174214" + 
":  " + 
"(b('ndvi') <= 3128.5) ? " + 
"0.10878923366051252" + 
":  " + 
"-0.02078261820072187" + 
":  " + 
"(b('moss') <= 6.853561639785767) ? " + 
"(b('ndvi') <= 5096.5) ? " + 
"-0.0002505054958213333" + 
":  " + 
"0.037504266527204004" + 
":  " + 
"(b('ndvi') <= 1165.5) ? " + 
"0.11099122182369564" + 
":  " + 
"-0.011576294186829483" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.75) ? " + 
"(b('b4') <= 620.0) ? " + 
"(b('ndvi') <= 5604.0) ? " + 
"0.00240186412857065" + 
":  " + 
"0.09819334003926612" + 
":  " + 
"(b('ndvi') <= 3553.0) ? " + 
"-0.0019152072812928063" + 
":  " + 
"-0.017192988190629626" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('b4') <= 725.5) ? " + 
"0.004188996531482754" + 
":  " + 
"0.03903770280131123" + 
":  " + 
"(b('b1') <= 250.5) ? " + 
"-0.04217163651772877" + 
":  " + 
"0.00011310285700829857" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 16563.0) ? " + 
"(b('b2') <= 911.5) ? " + 
"(b('g0vv') <= -15.286935806274414) ? " + 
"-0.0373180575442185" + 
":  " + 
"-0.006155450824122005" + 
":  " + 
"(b('ndvi') <= 1652.0) ? " + 
"0.14834621088853334" + 
":  " + 
"0.07698416318067018" + 
":  " + 
"(b('l8dt') <= 20391.0) ? " + 
"(b('grass') <= 28.24617576599121) ? " + 
"-0.00422527701705938" + 
":  " + 
"0.07600544710831532" + 
":  " + 
"(b('l8dt') <= 63281.0) ? " + 
"-0.004652015134397232" + 
":  " + 
"0.0002264498413294439" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 666.5) ? " + 
"(b('trees') <= 12.304713249206543) ? " + 
"(b('crop') <= 32.8998908996582) ? " + 
"0.014308749758358812" + 
":  " + 
"-0.004859978327162594" + 
":  " + 
"(b('b1') <= 229.0) ? " + 
"0.004827360243528598" + 
":  " + 
"-0.024576232401204698" + 
":  " + 
"(b('b3') <= 684.5) ? " + 
"(b('moss') <= 0.31213873624801636) ? " + 
"-0.04291943783424974" + 
":  " + 
"0.01258252289789318" + 
":  " + 
"(b('b11') <= 1013.5) ? " + 
"0.02433891587658359" + 
":  " + 
"-0.0001085878038300379" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 1.9490950107574463) ? " + 
"(b('b4') <= 1185.5) ? " + 
"(b('b3') <= 836.5) ? " + 
"-0.0014701102029146174" + 
":  " + 
"0.008729572923979939" + 
":  " + 
"(b('b3') <= 916.5) ? " + 
"-0.02351859431166033" + 
":  " + 
"-0.0002937736153143757" + 
":  " + 
"(b('b5') <= 2568.75) ? " + 
"(b('crop') <= 48.84012222290039) ? " + 
"0.011081721749613534" + 
":  " + 
"-0.0038989610900069423" + 
":  " + 
"(b('trees') <= 2.3446444869041443) ? " + 
"0.004066086704719239" + 
":  " + 
"-0.00984050352494002" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -13.86854600906372) ? " + 
"(b('crop') <= 87.21756744384766) ? " + 
"(b('b11') <= 1382.0) ? " + 
"-0.015095437713616064" + 
":  " + 
"-0.0014475424495873346" + 
":  " + 
"(b('b5') <= 2537.0) ? " + 
"0.0722217201335096" + 
":  " + 
"0.01064696720319217" + 
":  " + 
"(b('trees') <= 8.639616012573242) ? " + 
"(b('bare') <= 6.329379320144653) ? " + 
"-0.0015253299565711617" + 
":  " + 
"0.004868188213899214" + 
":  " + 
"(b('urban') <= 14.72341012954712) ? " + 
"0.0022155503732040633" + 
":  " + 
"0.04282131023418005" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -10.249711990356445) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"-0.0004915519371960198" + 
":  " + 
"0.030561483581125166" + 
":  " + 
"(b('ndvi') <= 2906.0) ? " + 
"-0.061010858883242106" + 
":  " + 
"-0.0037634568925682716" + 
":  " + 
"(b('crop') <= 48.65084648132324) ? " + 
"(b('trees') <= 7.712669610977173) ? " + 
"-0.001199271030572952" + 
":  " + 
"0.018254668908090438" + 
":  " + 
"(b('crop') <= 64.4262866973877) ? " + 
"-0.007958941693133725" + 
":  " + 
"0.0017378347092098317" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -23.391468048095703) ? " + 
"(b('g0vh') <= -23.392501831054688) ? " + 
"(b('lia') <= 36.29470252990723) ? " + 
"0.015119801712566478" + 
":  " + 
"-0.019842208217135508" + 
":  " + 
"0.11175903210808799" + 
":  " + 
"(b('g0vv') <= -15.28081226348877) ? " + 
"(b('b3') <= 600.0) ? " + 
"-0.030330000075889426" + 
":  " + 
"-0.0022427401834346056" + 
":  " + 
"(b('grass') <= 90.44964218139648) ? " + 
"1.6642456609141218e-05" + 
":  " + 
"0.008442378650185208" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3533.0) ? " + 
"(b('b5') <= 3471.5) ? " + 
"(b('crop') <= 67.1409683227539) ? " + 
"-0.0007067842681834605" + 
":  " + 
"0.0022365207689576234" + 
":  " + 
"(b('ndvi') <= 3875.5) ? " + 
"0.0030976719463349104" + 
":  " + 
"0.03978963428679044" + 
":  " + 
"(b('crop') <= 62.33124351501465) ? " + 
"(b('b4') <= 1144.5) ? " + 
"0.014221714124375048" + 
":  " + 
"-0.006285366073733889" + 
":  " + 
"(b('b1') <= 617.0) ? " + 
"-0.012182141470504573" + 
":  " + 
"0.0026270975498587762" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -7.955878496170044) ? " + 
"(b('g0vv') <= -7.958283185958862) ? " + 
"(b('g0vh') <= -14.159617900848389) ? " + 
"-0.00031597084024190454" + 
":  " + 
"0.010896061117192789" + 
":  " + 
"(b('moss') <= 0.7387820482254028) ? " + 
"-0.09387358314446084" + 
":  " + 
"-0.09662943050673262" + 
":  " + 
"(b('ndvi') <= 3293.5) ? " + 
"(b('ndvi') <= 3271.5) ? " + 
"0.00944069310228303" + 
":  " + 
"0.1720908374724599" + 
":  " + 
"(b('moss') <= 7.30760383605957) ? " + 
"-0.007994506270614349" + 
":  " + 
"0.02258341144449569" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 1.9490950107574463) ? " + 
"(b('trees') <= 4.231653451919556) ? " + 
"(b('trees') <= 3.533814549446106) ? " + 
"-0.0001552412109534738" + 
":  " + 
"-0.022612396928901254" + 
":  " + 
"(b('crop') <= 2.4269771575927734) ? " + 
"-0.003760307492478678" + 
":  " + 
"0.004497509057504366" + 
":  " + 
"(b('b5') <= 4200.0) ? " + 
"(b('b5') <= 2403.5) ? " + 
"0.003616971868060279" + 
":  " + 
"-0.004668108494087391" + 
":  " + 
"(b('crop') <= 59.23684501647949) ? " + 
"0.109273167870445" + 
":  " + 
"0.024387024420641678" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 10.783052444458008) ? " + 
"(b('bare') <= 9.324472427368164) ? " + 
"(b('bare') <= 8.550963878631592) ? " + 
"-0.0003084468225723263" + 
":  " + 
"0.03131403598281295" + 
":  " + 
"(b('b3') <= 748.5) ? " + 
"-0.061150935484025795" + 
":  " + 
"-0.013991194784880414" + 
":  " + 
"(b('b4') <= 1150.0) ? " + 
"(b('b10') <= 2228.5) ? " + 
"0.03371713780061547" + 
":  " + 
"-0.04086255252202846" + 
":  " + 
"(b('b6') <= 2710.0) ? " + 
"-0.02345645221914641" + 
":  " + 
"0.002761728197435565" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 28.096532821655273) ? " + 
"(b('b5') <= 1951.0) ? " + 
"(b('b4') <= 736.5) ? " + 
"-0.04660039100587282" + 
":  " + 
"0.05927865531551061" + 
":  " + 
"(b('b5') <= 3819.5) ? " + 
"-0.0069602888748578106" + 
":  " + 
"-0.08716112245613596" + 
":  " + 
"(b('lia') <= 28.386530876159668) ? " + 
"(b('ndvi') <= 875.5) ? " + 
"-0.04584659938316388" + 
":  " + 
"0.01956463312274192" + 
":  " + 
"(b('lia') <= 28.638394355773926) ? " + 
"-0.008856747155495979" + 
":  " + 
"0.0001489701535280459" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3385.5) ? " + 
"(b('b5') <= 3316.5) ? " + 
"(b('b4') <= 2020.5) ? " + 
"0.0006054225458049802" + 
":  " + 
"-0.004903383836845525" + 
":  " + 
"(b('b4') <= 2201.0) ? " + 
"0.003302539454380275" + 
":  " + 
"0.03319331458883991" + 
":  " + 
"(b('grass') <= 79.93707656860352) ? " + 
"(b('grass') <= 0.16759777069091797) ? " + 
"0.011602859393936973" + 
":  " + 
"-0.003821454308476791" + 
":  " + 
"(b('grass') <= 83.99470901489258) ? " + 
"0.1413425034522012" + 
":  " + 
"0.022091967867449762" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 908.5) ? " + 
"(b('b1') <= 764.5) ? " + 
"(b('bare') <= 29.32122039794922) ? " + 
"-0.0002951300109236186" + 
":  " + 
"-0.10485453144090402" + 
":  " + 
"(b('l8dt') <= 460057.5) ? " + 
"-0.013420329360446433" + 
":  " + 
"-0.06729917097440942" + 
":  " + 
"(b('b2') <= 910.5) ? " + 
"(b('b10') <= 2367.0) ? " + 
"0.1497506350020489" + 
":  " + 
"0.04453805179821778" + 
":  " + 
"(b('l8dt') <= 21618.5) ? " + 
"0.06674895137989428" + 
":  " + 
"0.0014221821392896789" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1536.5) ? " + 
"(b('b6') <= 2149.5) ? " + 
"(b('b6') <= 2110.5) ? " + 
"-0.005245073113291584" + 
":  " + 
"-0.05629029370868697" + 
":  " + 
"(b('lia') <= 43.52163505554199) ? " + 
"-0.0001647466578548324" + 
":  " + 
"-0.013547000329704167" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('bare') <= 6.473585605621338) ? " + 
"0.0004924283736130606" + 
":  " + 
"-0.01187773837639623" + 
":  " + 
"(b('b5') <= 2646.0) ? " + 
"0.00043772178353657733" + 
":  " + 
"0.021487957241953667" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 43.82485580444336) ? " + 
"(b('lia') <= 43.405202865600586) ? " + 
"(b('lia') <= 42.24803924560547) ? " + 
"-0.0002511062520144845" + 
":  " + 
"0.005454621140831837" + 
":  " + 
"(b('trees') <= 16.57373857498169) ? " + 
"-0.0052797191698999435" + 
":  " + 
"-0.060105709176685805" + 
":  " + 
"(b('lia') <= 44.066463470458984) ? " + 
"(b('b5') <= 3033.0) ? " + 
"0.0031605405803389547" + 
":  " + 
"0.024734896598219706" + 
":  " + 
"(b('g0vv') <= -11.0991849899292) ? " + 
"-0.0034095855958726044" + 
":  " + 
"0.012823660660066755" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 44.96173286437988) ? " + 
"(b('b5') <= 2992.5) ? " + 
"(b('b5') <= 2794.5) ? " + 
"-0.0005293399744342338" + 
":  " + 
"0.006282358240015687" + 
":  " + 
"(b('b5') <= 3029.5) ? " + 
"-0.012860175610193553" + 
":  " + 
"-0.0002737562520253575" + 
":  " + 
"0.09209225974045411" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -20.058966636657715) ? " + 
"(b('b11') <= 2756.5) ? " + 
"(b('g0vh') <= -22.5668363571167) ? " + 
"0.03688931944912427" + 
":  " + 
"0.05111074169147036" + 
":  " + 
"(b('grass') <= 42.49268341064453) ? " + 
"0.02085391421010599" + 
":  " + 
"0.011018890142796584" + 
":  " + 
"(b('g0vv') <= -17.144234657287598) ? " + 
"(b('ndvi') <= 2675.5) ? " + 
"-0.002871308818911171" + 
":  " + 
"-0.03010291602198392" + 
":  " + 
"(b('g0vh') <= -22.881443977355957) ? " + 
"0.007158812366512757" + 
":  " + 
"-2.3128249139991375e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('b6') <= 2762.5) ? " + 
"(b('b3') <= 721.5) ? " + 
"-0.0021992118232516586" + 
":  " + 
"-0.02725130718065187" + 
":  " + 
"(b('b1') <= 365.0) ? " + 
"0.041222402525105346" + 
":  " + 
"-0.01682208050847706" + 
":  " + 
"(b('b4') <= 919.5) ? " + 
"(b('grass') <= 73.06093978881836) ? " + 
"0.002290489988788447" + 
":  " + 
"0.025226751570098876" + 
":  " + 
"(b('b3') <= 791.0) ? " + 
"-0.019155968879906945" + 
":  " + 
"-0.00017824416397560836" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('ndvi') <= 2624.5) ? " + 
"(b('grass') <= 52.99222183227539) ? " + 
"0.0020089666599972427" + 
":  " + 
"-0.0032123898926136028" + 
":  " + 
"(b('ndvi') <= 2633.0) ? " + 
"0.06742479459029552" + 
":  " + 
"0.010384515249904854" + 
":  " + 
"(b('b6') <= 3483.5) ? " + 
"(b('grass') <= 77.6886215209961) ? " + 
"-0.0037383128164587744" + 
":  " + 
"0.016600709198607917" + 
":  " + 
"(b('b1') <= 445.0) ? " + 
"0.11576102580036522" + 
":  " + 
"0.013018721183716539" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('b1') <= 827.0) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"-0.0015892099936920111" + 
":  " + 
"0.01650381372527486" + 
":  " + 
"(b('trees') <= 1.6470285207033157) ? " + 
"0.0035100021554224725" + 
":  " + 
"0.12024554606179332" + 
":  " + 
"(b('ndvi') <= 3929.5) ? " + 
"(b('bare') <= 0.35301104187965393) ? " + 
"0.019106475216959743" + 
":  " + 
"-0.00032149399849836283" + 
":  " + 
"(b('l8dt') <= 1361392.0) ? " + 
"0.003601326242217269" + 
":  " + 
"0.01997276215415458" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3218.5) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"(b('crop') <= 67.1409683227539) ? " + 
"-0.0005290968451819177" + 
":  " + 
"0.002855145924072625" + 
":  " + 
"(b('b1') <= 254.0) ? " + 
"-0.0704333981904022" + 
":  " + 
"0.022461337958571654" + 
":  " + 
"(b('b5') <= 3233.5) ? " + 
"(b('g0vv') <= -7.240060567855835) ? " + 
"-0.02294883205064834" + 
":  " + 
"0.12755229917898667" + 
":  " + 
"(b('urban') <= 34.57631492614746) ? " + 
"-0.00033075259978092764" + 
":  " + 
"-0.025616862135344507" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 362.5) ? " + 
"(b('b2') <= 563.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"-0.0014749550163239765" + 
":  " + 
"0.01028833375146054" + 
":  " + 
"(b('b5') <= 2778.5) ? " + 
"0.027808941653101146" + 
":  " + 
"0.19178553088726547" + 
":  " + 
"(b('b1') <= 400.5) ? " + 
"(b('b7') <= 1898.5) ? " + 
"-0.01107441708096828" + 
":  " + 
"0.009100185080562373" + 
":  " + 
"(b('b2') <= 517.5) ? " + 
"0.01091330622053881" + 
":  " + 
"-0.00017377884649302845" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('b2') <= 912.5) ? " + 
"(b('b4') <= 1439.75) ? " + 
"-6.995303103179297e-05" + 
":  " + 
"-0.007345022673459207" + 
":  " + 
"(b('b6') <= 2977.5) ? " + 
"0.149462757248824" + 
":  " + 
"0.004429217868793302" + 
":  " + 
"(b('ndvi') <= 3929.5) ? " + 
"(b('b6') <= 2074.5) ? " + 
"0.010243191099117017" + 
":  " + 
"-0.0004662238122051185" + 
":  " + 
"(b('l8dt') <= 1361392.0) ? " + 
"0.0034857887906544253" + 
":  " + 
"0.018342803323537653" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3533.0) ? " + 
"(b('b5') <= 3471.5) ? " + 
"(b('ndvi') <= 4747.5) ? " + 
"0.0003999224781013001" + 
":  " + 
"-0.005303222524934628" + 
":  " + 
"(b('ndvi') <= 3875.5) ? " + 
"0.0030111751279372095" + 
":  " + 
"0.03560279569648299" + 
":  " + 
"(b('b6') <= 2410.5) ? " + 
"(b('ndvi') <= 2568.0) ? " + 
"0.054048121490440866" + 
":  " + 
"0.0028734806398000583" + 
":  " + 
"(b('b6') <= 2502.5) ? " + 
"-0.04090475795831122" + 
":  " + 
"-0.0031429448737406874" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -11.432883739471436) ? " + 
"(b('g0vv') <= -7.955878496170044) ? " + 
"(b('g0vv') <= -7.958283185958862) ? " + 
"-0.00017727073858335115" + 
":  " + 
"-0.08468965730394684" + 
":  " + 
"(b('b5') <= 4367.5) ? " + 
"0.005086819203637064" + 
":  " + 
"-0.031589578684286995" + 
":  " + 
"(b('l8dt') <= 1123644.5) ? " + 
"(b('lia') <= 34.40300369262695) ? " + 
"-0.029896023953339207" + 
":  " + 
"-0.08381023806229866" + 
":  " + 
"(b('b6') <= 3192.5) ? " + 
"-0.01566594439301198" + 
":  " + 
"0.03480160221788632" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 614.5) ? " + 
"(b('l8dt') <= 1700033.5) ? " + 
"(b('trees') <= 19.807273864746094) ? " + 
"0.003808583937929273" + 
":  " + 
"-0.028530500015441912" + 
":  " + 
"(b('b6') <= 2106.0) ? " + 
"-0.027351766850778506" + 
":  " + 
"0.001586531698068077" + 
":  " + 
"(b('b3') <= 624.5) ? " + 
"(b('trees') <= 7.479882001876831) ? " + 
"-0.0032352115516185477" + 
":  " + 
"0.037760484938794" + 
":  " + 
"(b('b3') <= 629.5) ? " + 
"-0.01787870757719239" + 
":  " + 
"0.00017348714804759754" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('ndvi') <= 2624.5) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"0.0001788758381512997" + 
":  " + 
"-0.046563204937393236" + 
":  " + 
"(b('ndvi') <= 2633.0) ? " + 
"0.06079934955074723" + 
":  " + 
"0.00937470875893649" + 
":  " + 
"(b('b6') <= 3595.0) ? " + 
"(b('grass') <= 77.6886215209961) ? " + 
"-0.0032400334184068988" + 
":  " + 
"0.013615463818523287" + 
":  " + 
"(b('b5') <= 2658.5) ? " + 
"0.07618410022384751" + 
":  " + 
"0.00984008348540192" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 28.102611541748047) ? " + 
"(b('b1') <= 380.0) ? " + 
"(b('g0vh') <= -14.927433013916016) ? " + 
"-0.05892274482195884" + 
":  " + 
"-0.12650375977660422" + 
":  " + 
"(b('b5') <= 1951.0) ? " + 
"0.04563668128609004" + 
":  " + 
"-0.00634641490558377" + 
":  " + 
"(b('lia') <= 28.386530876159668) ? " + 
"(b('ndvi') <= 875.5) ? " + 
"-0.04395255224452954" + 
":  " + 
"0.020934009599687473" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-0.0003187677390519564" + 
":  " + 
"0.0028928433193769567" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.218039989471436) ? " + 
"(b('b2') <= 1020.0) ? " + 
"(b('b1') <= 700.5) ? " + 
"-0.0013462608406409895" + 
":  " + 
"-0.013861092247259767" + 
":  " + 
"(b('bare') <= 0.2048390582203865) ? " + 
"0.038963225911095564" + 
":  " + 
"-0.001378308700187531" + 
":  " + 
"(b('g0vv') <= -14.217326641082764) ? " + 
"0.18750132353015211" + 
":  " + 
"(b('g0vv') <= -14.198684692382812) ? " + 
"0.028325200168023375" + 
":  " + 
"0.00031445244897596475" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1662.5) ? " + 
"(b('b3') <= 1313.5) ? " + 
"(b('b1') <= 783.5) ? " + 
"0.00042055511881699035" + 
":  " + 
"-0.02635264283475706" + 
":  " + 
"(b('b5') <= 3499.5) ? " + 
"0.03643879031308444" + 
":  " + 
"-0.02121610361654152" + 
":  " + 
"(b('b10') <= 2451.0) ? " + 
"(b('b6') <= 3806.0) ? " + 
"-0.012526499348985901" + 
":  " + 
"0.03407279916841193" + 
":  " + 
"(b('b6') <= 2869.5) ? " + 
"0.117080420237304" + 
":  " + 
"-0.00041033993897570114" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3992931.5) ? " + 
"(b('g0vh') <= -15.064626693725586) ? " + 
"(b('g0vv') <= -8.144237041473389) ? " + 
"-0.0006022161939055129" + 
":  " + 
"0.005292483317515767" + 
":  " + 
"(b('b3') <= 1471.0) ? " + 
"0.0027248796425060557" + 
":  " + 
"0.0420985051143554" + 
":  " + 
"(b('b3') <= 552.5) ? " + 
"(b('lia') <= 29.243504524230957) ? " + 
"0.09009596175403867" + 
":  " + 
"-0.033434399952532785" + 
":  " + 
"(b('b1') <= 776.0) ? " + 
"0.011134734481418301" + 
":  " + 
"-0.030894649606439523" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 4.231653451919556) ? " + 
"(b('trees') <= 3.533814549446106) ? " + 
"(b('lia') <= 39.43572425842285) ? " + 
"-0.0020604934034903865" + 
":  " + 
"0.002428579815707549" + 
":  " + 
"(b('b5') <= 1599.0) ? " + 
"0.02180751821207953" + 
":  " + 
"-0.01542070603648689" + 
":  " + 
"(b('trees') <= 6.304144859313965) ? " + 
"(b('b5') <= 2853.0) ? " + 
"0.021449594146020167" + 
":  " + 
"0.0022659048059527286" + 
":  " + 
"(b('grass') <= 80.9476318359375) ? " + 
"0.000399508310923789" + 
":  " + 
"-0.012030209995334325" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1274.5) ? " + 
"(b('b3') <= 1005.5) ? " + 
"(b('g0vv') <= -10.845878601074219) ? " + 
"-0.00196415173645767" + 
":  " + 
"0.003237553413131507" + 
":  " + 
"(b('grass') <= 83.88994216918945) ? " + 
"0.007240080071186299" + 
":  " + 
"0.03892062460028305" + 
":  " + 
"(b('b6') <= 2126.0) ? " + 
"(b('l8dt') <= 734891.0) ? " + 
"-0.046378607571090615" + 
":  " + 
"-0.08404711187195282" + 
":  " + 
"(b('b3') <= 998.5) ? " + 
"-0.010207329763088531" + 
":  " + 
"-0.00030026865848939926" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3471.5) ? " + 
"(b('b5') <= 3385.5) ? " + 
"0.000365495266490266" + 
":  " + 
"-0.0057867638637678" + 
":  " + 
"(b('grass') <= 0.16759777069091797) ? " + 
"0.04269727307475088" + 
":  " + 
"0.009774567494460581" + 
":  " + 
"(b('b5') <= 3519.5) ? " + 
"(b('g0vv') <= -11.965662002563477) ? " + 
"-0.046169593260404575" + 
":  " + 
"-0.0984459016615591" + 
":  " + 
"(b('b4') <= 947.0) ? " + 
"0.006191978038928847" + 
":  " + 
"-0.004958244060270308" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('ndvi') <= 1190.5) ? " + 
"(b('b5') <= 2094.5) ? " + 
"0.008912440155757876" + 
":  " + 
"-0.005326119578179732" + 
":  " + 
"(b('bare') <= 29.32122039794922) ? " + 
"0.00020884031399903558" + 
":  " + 
"0.04887966265829408" + 
":  " + 
"(b('lia') <= 36.049673080444336) ? " + 
"(b('b2') <= 1265.0) ? " + 
"0.03550309337690439" + 
":  " + 
"0.011535527219962682" + 
":  " + 
"(b('l8dt') <= 86644.0) ? " + 
"0.017295586099552108" + 
":  " + 
"0.0009444882747450565" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('ndvi') <= 2626.5) ? " + 
"(b('b1') <= 336.5) ? " + 
"0.00700024048925782" + 
":  " + 
"-0.000551066479117216" + 
":  " + 
"(b('ndvi') <= 2633.0) ? " + 
"0.07774297054358874" + 
":  " + 
"0.008519267526222283" + 
":  " + 
"(b('b6') <= 3595.0) ? " + 
"(b('b6') <= 3133.5) ? " + 
"-0.000808058635558047" + 
":  " + 
"-0.01364616025883057" + 
":  " + 
"(b('b5') <= 2658.5) ? " + 
"0.06876141599630194" + 
":  " + 
"0.00897473991940198" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 10.783052444458008) ? " + 
"(b('moss') <= 15.544372081756592) ? " + 
"(b('b1') <= 628.5) ? " + 
"-0.0005299114230689037" + 
":  " + 
"0.002586969240513686" + 
":  " + 
"(b('g0vv') <= -9.042971134185791) ? " + 
"-0.007116873553346622" + 
":  " + 
"0.033161006296140896" + 
":  " + 
"(b('ndvi') <= 1746.0) ? " + 
"(b('b6') <= 2703.5) ? " + 
"-0.017881616976441295" + 
":  " + 
"0.001626529870904539" + 
":  " + 
"(b('lia') <= 39.29873847961426) ? " + 
"0.00653527721975031" + 
":  " + 
"0.03839301134740712" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 5248578.0) ? " + 
"(b('b5') <= 3533.0) ? " + 
"(b('b5') <= 3531.0) ? " + 
"0.0001862924155893507" + 
":  " + 
"0.04647166091669147" + 
":  " + 
"(b('crop') <= 62.33124351501465) ? " + 
"0.0036091828806900945" + 
":  " + 
"-0.005922070646607237" + 
":  " + 
"(b('g0vh') <= -20.223941802978516) ? " + 
"(b('b4') <= 724.5) ? " + 
"0.12098727696850996" + 
":  " + 
"0.023756936726804147" + 
":  " + 
"(b('ndvi') <= 5019.0) ? " + 
"0.005550576369079963" + 
":  " + 
"-0.04655690698418744" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('urban') <= 0.513603001832962) ? " + 
"(b('b4') <= 980.5) ? " + 
"0.0023324077530072116" + 
":  " + 
"-0.000643018070844291" + 
":  " + 
"(b('ndvi') <= 5073.5) ? " + 
"0.00846941536798764" + 
":  " + 
"0.08456759240921988" + 
":  " + 
"(b('b1') <= 414.5) ? " + 
"(b('b4') <= 715.0) ? " + 
"0.003370548197099868" + 
":  " + 
"-0.009158753193313237" + 
":  " + 
"(b('b11') <= 2289.5) ? " + 
"0.006579164307266806" + 
":  " + 
"-0.004253515429002655" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('b6') <= 2762.5) ? " + 
"(b('b3') <= 726.5) ? " + 
"-0.0027712161323652077" + 
":  " + 
"-0.05235987524609463" + 
":  " + 
"(b('b4') <= 718.5) ? " + 
"0.07848215006512893" + 
":  " + 
"0.011469448853668893" + 
":  " + 
"(b('b3') <= 743.5) ? " + 
"(b('b3') <= 741.5) ? " + 
"0.007901034735999514" + 
":  " + 
"0.0635279563067723" + 
":  " + 
"(b('b3') <= 761.5) ? " + 
"-0.009744391340917556" + 
":  " + 
"0.00042631814818688574" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 65.5) ? " + 
"(b('moss') <= 8.681296110153198) ? " + 
"-0.010708752117220943" + 
":  " + 
"(b('g0vh') <= -20.64984130859375) ? " + 
"0.053085602261768026" + 
":  " + 
"0.0276202262493912" + 
":  " + 
"(b('b3') <= 614.5) ? " + 
"(b('b5') <= 2594.5) ? " + 
"-0.007951406329734057" + 
":  " + 
"0.010910990589367326" + 
":  " + 
"(b('b3') <= 624.5) ? " + 
"0.018318386944560366" + 
":  " + 
"5.95131583032868e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 43.82485580444336) ? " + 
"(b('lia') <= 43.50736999511719) ? " + 
"(b('g0vv') <= -15.08692741394043) ? " + 
"-0.002980004783879736" + 
":  " + 
"0.0004255553410367753" + 
":  " + 
"(b('g0vh') <= -22.849122047424316) ? " + 
"0.11175822779790652" + 
":  " + 
"-0.00808545446718666" + 
":  " + 
"(b('g0vv') <= -10.818886280059814) ? " + 
"(b('b3') <= 848.5) ? " + 
"-0.00790429141688272" + 
":  " + 
"0.007035906731441959" + 
":  " + 
"(b('ndvi') <= 1279.5) ? " + 
"-0.0656945171132412" + 
":  " + 
"0.01620806322204273" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 0.29949215054512024) ? " + 
"(b('moss') <= 7.140108346939087) ? " + 
"(b('moss') <= 6.624295234680176) ? " + 
"-0.0011929204381605641" + 
":  " + 
"-0.028630193552819448" + 
":  " + 
"(b('moss') <= 7.598436594009399) ? " + 
"0.024882770406660794" + 
":  " + 
"-0.00045531420554688107" + 
":  " + 
"(b('ndvi') <= 3511.5) ? " + 
"(b('bare') <= 0.35301104187965393) ? " + 
"0.016181629748960893" + 
":  " + 
"-0.00038858346025777136" + 
":  " + 
"(b('grass') <= 81.3282585144043) ? " + 
"0.004765963449054034" + 
":  " + 
"0.05869154021823417" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"(b('trees') <= 1.8166741132736206) ? " + 
"-0.001096940474101986" + 
":  " + 
"0.003650396898122738" + 
":  " + 
"(b('g0vh') <= -15.721728324890137) ? " + 
"-0.04588113832603568" + 
":  " + 
"0.04251602644097535" + 
":  " + 
"(b('grass') <= 77.6886215209961) ? " + 
"(b('ndvi') <= 2836.0) ? " + 
"-0.016528763549096263" + 
":  " + 
"-0.0011472974176699197" + 
":  " + 
"(b('b1') <= 548.5) ? " + 
"0.021092082970662323" + 
":  " + 
"-0.021278569673919688" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 5695172.5) ? " + 
"(b('b5') <= 1935.5) ? " + 
"(b('b5') <= 1927.0) ? " + 
"0.0018075803739947968" + 
":  " + 
"0.04926204005977911" + 
":  " + 
"(b('b3') <= 727.5) ? " + 
"-0.003708630532181394" + 
":  " + 
"0.00019327459097991608" + 
":  " + 
"(b('l8dt') <= 9267340.0) ? " + 
"(b('g0vv') <= -10.725082874298096) ? " + 
"0.028198858140392198" + 
":  " + 
"0.004253479592809492" + 
":  " + 
"(b('l8dt') <= 9526514.5) ? " + 
"-0.033266093450162626" + 
":  " + 
"-0.010908208927798996" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 28.15742301940918) ? " + 
"(b('g0vh') <= -13.760127544403076) ? " + 
"(b('ndvi') <= 4495.0) ? " + 
"-0.004574081610049246" + 
":  " + 
"-0.07982768941995316" + 
":  " + 
"(b('b5') <= 3331.5) ? " + 
"0.0672808690258524" + 
":  " + 
"0.09484112097717073" + 
":  " + 
"(b('lia') <= 28.16038703918457) ? " + 
"(b('b7') <= 2237.5) ? " + 
"0.12109527049494997" + 
":  " + 
"0.044790064703995935" + 
":  " + 
"(b('grass') <= 98.36243438720703) ? " + 
"-8.491144078729287e-05" + 
":  " + 
"0.005709879827585722" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -13.90178108215332) ? " + 
"(b('crop') <= 87.21756744384766) ? " + 
"(b('moss') <= 7.169239282608032) ? " + 
"-0.0047347244728050564" + 
":  " + 
"0.0015919717611477095" + 
":  " + 
"(b('g0vv') <= -13.950667381286621) ? " + 
"0.012149412192753358" + 
":  " + 
"0.09873392469868753" + 
":  " + 
"(b('trees') <= 8.639616012573242) ? " + 
"(b('bare') <= 6.329379320144653) ? " + 
"-0.0014208431317175565" + 
":  " + 
"0.004627173568312269" + 
":  " + 
"(b('urban') <= 14.72341012954712) ? " + 
"0.0019905818152890923" + 
":  " + 
"0.036624453840030595" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -11.432883739471436) ? " + 
"(b('g0vh') <= -14.666974544525146) ? " + 
"(b('ndvi') <= 4627.5) ? " + 
"0.00011953702833447336" + 
":  " + 
"-0.0038593762024890788" + 
":  " + 
"(b('urban') <= 29.42727279663086) ? " + 
"0.0016909028606052897" + 
":  " + 
"0.028224608955403744" + 
":  " + 
"(b('l8dt') <= 1123644.5) ? " + 
"(b('lia') <= 34.40300369262695) ? " + 
"-0.027442693891339354" + 
":  " + 
"-0.07580582050132977" + 
":  " + 
"(b('b4') <= 1200.0) ? " + 
"-0.013805676192357341" + 
":  " + 
"0.03062040308808904" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 3244.5) ? " + 
"(b('b4') <= 1662.5) ? " + 
"(b('b3') <= 1313.5) ? " + 
"0.00024067318110897675" + 
":  " + 
"0.019397054420494473" + 
":  " + 
"(b('g0vh') <= -14.840832710266113) ? " + 
"-0.003032077960854026" + 
":  " + 
"0.028532877402237828" + 
":  " + 
"(b('b4') <= 2096.5) ? " + 
"(b('b2') <= 1042.5) ? " + 
"0.005407975008411144" + 
":  " + 
"0.04645729374963718" + 
":  " + 
"(b('ndvi') <= 3471.0) ? " + 
"-0.0020418271057211636" + 
":  " + 
"0.03868231290271867" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('b1') <= 363.5) ? " + 
"(b('b2') <= 563.5) ? " + 
"0.0027549936661607354" + 
":  " + 
"0.11378854044303147" + 
":  " + 
"(b('b3') <= 728.5) ? " + 
"-0.014034525262948358" + 
":  " + 
"0.00014831569178248838" + 
":  " + 
"(b('b5') <= 4200.0) ? " + 
"(b('b5') <= 2568.75) ? " + 
"0.0021758752839813214" + 
":  " + 
"-0.0046075009735953906" + 
":  " + 
"(b('b5') <= 4416.5) ? " + 
"0.09519573016777677" + 
":  " + 
"0.023064543750126138" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.25) ? " + 
"(b('g0vh') <= -17.350119590759277) ? " + 
"(b('b1') <= 309.0) ? " + 
"-0.009182487210715903" + 
":  " + 
"0.019641863232947972" + 
":  " + 
"(b('l8dt') <= 3649681.5) ? " + 
"0.005232243106114638" + 
":  " + 
"-0.03340140326120244" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('b4') <= 725.5) ? " + 
"0.0035479368082985963" + 
":  " + 
"0.03298231280860605" + 
":  " + 
"(b('b1') <= 258.5) ? " + 
"-0.02342791472550548" + 
":  " + 
"0.00012767716524743767" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3385997.0) ? " + 
"(b('b5') <= 1439.0) ? " + 
"(b('b6') <= 1738.5) ? " + 
"-0.005489884040156735" + 
":  " + 
"0.036291941371796727" + 
":  " + 
"(b('b2') <= 314.5) ? " + 
"0.007194359437993522" + 
":  " + 
"-0.0004402920753746189" + 
":  " + 
"(b('trees') <= 12.64185619354248) ? " + 
"(b('lia') <= 41.29780387878418) ? " + 
"0.003281560108532773" + 
":  " + 
"0.020160324710470058" + 
":  " + 
"(b('trees') <= 14.932132720947266) ? " + 
"-0.0400202908078978" + 
":  " + 
"0.009110976556137204" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 614.5) ? " + 
"(b('b5') <= 2594.5) ? " + 
"(b('trees') <= 9.36296796798706) ? " + 
"-0.00025251868860188116" + 
":  " + 
"-0.01655816915395993" + 
":  " + 
"(b('b5') <= 3095.5) ? " + 
"0.011987244969210623" + 
":  " + 
"-0.10684356686870337" + 
":  " + 
"(b('b3') <= 624.5) ? " + 
"(b('b7') <= 1461.5) ? " + 
"0.030724652814141863" + 
":  " + 
"-0.008912046524283587" + 
":  " + 
"(b('b11') <= 997.0) ? " + 
"0.01721607709737963" + 
":  " + 
"-3.9738536246627335e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 65.5) ? " + 
"(b('b6') <= 936.5) ? " + 
"-0.00828320846251318" + 
":  " + 
"(b('g0vh') <= -20.64984130859375) ? " + 
"0.049206624568507384" + 
":  " + 
"0.02617426748653771" + 
":  " + 
"(b('b6') <= 1724.5) ? " + 
"(b('ndvi') <= 2411.0) ? " + 
"0.006159564841085096" + 
":  " + 
"-0.01169054448244146" + 
":  " + 
"(b('b5') <= 1439.0) ? " + 
"0.01796694940815983" + 
":  " + 
"1.7348955443928477e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 44.96173286437988) ? " + 
"(b('b3') <= 882.5) ? " + 
"(b('moss') <= 0.08657755330204964) ? " + 
"-0.008623509899574971" + 
":  " + 
"0.0003299975723364573" + 
":  " + 
"(b('b4') <= 951.5) ? " + 
"0.019161877245251053" + 
":  " + 
"-2.7846157346457962e-06" + 
":  " + 
"0.08215180050306245" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3471.5) ? " + 
"(b('moss') <= 1.9861568808555603) ? " + 
"0.002119848359493758" + 
":  " + 
"-0.0005487117004440943" + 
":  " + 
"(b('g0vh') <= -19.790437698364258) ? " + 
"-0.0031137913083708574" + 
":  " + 
"0.02041221997933607" + 
":  " + 
"(b('b5') <= 3519.5) ? " + 
"(b('g0vv') <= -11.965662002563477) ? " + 
"-0.041963712513033456" + 
":  " + 
"-0.08950864318802251" + 
":  " + 
"(b('b6') <= 1967.5) ? " + 
"0.018791581931799396" + 
":  " + 
"-0.002789999347200082" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('ndvi') <= 2626.5) ? " + 
"(b('grass') <= 52.127288818359375) ? " + 
"0.0017658721463962913" + 
":  " + 
"-0.0025598709963829884" + 
":  " + 
"(b('ndvi') <= 2633.0) ? " + 
"0.06963060163698664" + 
":  " + 
"0.007634838937952505" + 
":  " + 
"(b('b6') <= 3483.5) ? " + 
"(b('b6') <= 3245.0) ? " + 
"-0.0010282729160785598" + 
":  " + 
"-0.02006510266680567" + 
":  " + 
"(b('g0vh') <= -20.617650032043457) ? " + 
"-0.010167051914496092" + 
":  " + 
"0.014595343565130958" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 10.783052444458008) ? " + 
"(b('bare') <= 9.324472427368164) ? " + 
"(b('bare') <= 8.550963878631592) ? " + 
"-0.0003022263849827702" + 
":  " + 
"0.02813843204793435" + 
":  " + 
"(b('l8dt') <= 37632.5) ? " + 
"0.11407595829455225" + 
":  " + 
"-0.014055673774564285" + 
":  " + 
"(b('b4') <= 731.5) ? " + 
"(b('b4') <= 595.0) ? " + 
"-0.02896417150914497" + 
":  " + 
"0.06059987140550261" + 
":  " + 
"(b('b1') <= 310.5) ? " + 
"-0.05445427635649193" + 
":  " + 
"0.001932632959348997" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 11.215232372283936) ? " + 
"(b('trees') <= 11.076036930084229) ? " + 
"(b('trees') <= 10.893646240234375) ? " + 
"-0.00016190481630596327" + 
":  " + 
"0.041050707204120074" + 
":  " + 
"(b('g0vv') <= -9.553959846496582) ? " + 
"-0.017471460507774154" + 
":  " + 
"0.015385543971843843" + 
":  " + 
"(b('trees') <= 12.501765251159668) ? " + 
"(b('g0vv') <= -10.868317127227783) ? " + 
"0.005564068831924959" + 
":  " + 
"0.028641881983241888" + 
":  " + 
"(b('l8dt') <= 1057727.5) ? " + 
"0.001751942453245459" + 
":  " + 
"-0.010178756249301488" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2965.5) ? " + 
"(b('b5') <= 2956.5) ? " + 
"(b('b5') <= 2794.5) ? " + 
"-0.00044266032174312655" + 
":  " + 
"0.004757389157739756" + 
":  " + 
"(b('trees') <= 11.2122802734375) ? " + 
"0.0038584416608508027" + 
":  " + 
"0.08508462362526921" + 
":  " + 
"(b('grass') <= 0.16759777069091797) ? " + 
"(b('b5') <= 3020.0) ? " + 
"-0.021315064962661657" + 
":  " + 
"0.013283442233527773" + 
":  " + 
"(b('moss') <= 3.2875311374664307) ? " + 
"-0.006087703390430497" + 
":  " + 
"0.0004695796511265238" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3992931.5) ? " + 
"(b('l8dt') <= 3924788.5) ? " + 
"(b('b5') <= 1935.5) ? " + 
"0.00337203462152176" + 
":  " + 
"-0.000355578770052664" + 
":  " + 
"(b('b2') <= 431.5) ? " + 
"-0.09499223779244254" + 
":  " + 
"-0.019901645844206752" + 
":  " + 
"(b('b3') <= 543.5) ? " + 
"(b('b1') <= 178.0) ? " + 
"0.08024272966042484" + 
":  " + 
"-0.04404973215750876" + 
":  " + 
"(b('b1') <= 776.0) ? " + 
"0.008853645317972477" + 
":  " + 
"-0.027418903163853255" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('grass') <= 98.36243438720703) ? " + 
"(b('grass') <= 96.63224411010742) ? " + 
"(b('lia') <= 34.4125919342041) ? " + 
"-0.0020146260813032266" + 
":  " + 
"0.00045454548155888944" + 
":  " + 
"(b('ndvi') <= 1748.0) ? " + 
"0.032078579004424415" + 
":  " + 
"-0.04589061346294181" + 
":  " + 
"(b('b5') <= 2413.0) ? " + 
"(b('lia') <= 34.144195556640625) ? " + 
"0.02201294279882464" + 
":  " + 
"-0.003022395573802347" + 
":  " + 
"(b('ndvi') <= 1251.5) ? " + 
"0.05111232591623717" + 
":  " + 
"-0.0069770345936457645" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 85.84851455688477) ? " + 
"(b('crop') <= 85.4493522644043) ? " + 
"(b('b2') <= 1020.5) ? " + 
"-0.00036386360165717603" + 
":  " + 
"0.003659469483538197" + 
":  " + 
"(b('b5') <= 2739.0) ? " + 
"0.00906248145170004" + 
":  " + 
"-0.02508144406703329" + 
":  " + 
"(b('grass') <= 9.401607036590576) ? " + 
"(b('ndvi') <= 3652.0) ? " + 
"0.0038366235044633794" + 
":  " + 
"-0.01093526600122693" + 
":  " + 
"(b('b5') <= 2909.5) ? " + 
"0.0596139628738063" + 
":  " + 
"0.01836319562005558" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1190.5) ? " + 
"(b('l8dt') <= 38479.0) ? " + 
"(b('b5') <= 2047.5) ? " + 
"0.061748089981092644" + 
":  " + 
"0.011932465121382055" + 
":  " + 
"(b('b4') <= 924.0) ? " + 
"-0.05018809959170482" + 
":  " + 
"-0.002761863552000276" + 
":  " + 
"(b('bare') <= 29.32122039794922) ? " + 
"(b('bare') <= 20.924105644226074) ? " + 
"0.00034981726168829656" + 
":  " + 
"-0.011602261979000566" + 
":  " + 
"(b('b11') <= 2090.5) ? " + 
"-0.12618524750523344" + 
":  " + 
"0.05413056542100068" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 50860.5) ? " + 
"(b('g0vh') <= -16.571227073669434) ? " + 
"(b('l8dt') <= 22356.0) ? " + 
"0.008396444403094387" + 
":  " + 
"-0.005133979878997863" + 
":  " + 
"(b('b6') <= 2123.5) ? " + 
"0.011577097247836123" + 
":  " + 
"-0.02866953993549212" + 
":  " + 
"(b('l8dt') <= 70515.5) ? " + 
"(b('grass') <= 46.57049369812012) ? " + 
"0.0033427812876995052" + 
":  " + 
"0.030295142649950594" + 
":  " + 
"(b('l8dt') <= 121900.5) ? " + 
"-0.007025648186983135" + 
":  " + 
"0.00014795369468165095" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 16563.0) ? " + 
"(b('b3') <= 1245.5) ? " + 
"(b('b7') <= 2820.5) ? " + 
"-0.006774663954675309" + 
":  " + 
"-0.06494067781120103" + 
":  " + 
"(b('lia') <= 40.555023193359375) ? " + 
"0.07469440479916814" + 
":  " + 
"0.013824801630156988" + 
":  " + 
"(b('l8dt') <= 20391.0) ? " + 
"(b('bare') <= 0.4333333373069763) ? " + 
"0.04827998583759884" + 
":  " + 
"-0.022645452577386933" + 
":  " + 
"(b('l8dt') <= 50860.5) ? " + 
"-0.004298884193859385" + 
":  " + 
"0.0001882270920592833" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5456.5) ? " + 
"(b('b10') <= 3900.0) ? " + 
"(b('b6') <= 4860.5) ? " + 
"2.814308018515986e-05" + 
":  " + 
"-0.013058236166392534" + 
":  " + 
"(b('grass') <= 25.167882919311523) ? " + 
"0.00679603838062477" + 
":  " + 
"0.04135239718219116" + 
":  " + 
"(b('g0vh') <= -19.21955966949463) ? " + 
"(b('g0vv') <= -10.935465335845947) ? " + 
"-0.017792765632369548" + 
":  " + 
"-0.0015953114572085508" + 
":  " + 
"(b('moss') <= 2.083815097808838) ? " + 
"-0.03773958984860897" + 
":  " + 
"-0.0644954328910379" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.28081226348877) ? " + 
"(b('ndvi') <= 3376.5) ? " + 
"(b('l8dt') <= 16564.0) ? " + 
"-0.028890822335070128" + 
":  " + 
"-0.0005485155595852901" + 
":  " + 
"(b('bare') <= 13.356775760650635) ? " + 
"-0.019406378007269295" + 
":  " + 
"0.09137404390789686" + 
":  " + 
"(b('grass') <= 90.44964218139648) ? " + 
"(b('grass') <= 83.72659683227539) ? " + 
"0.0002561909542392394" + 
":  " + 
"-0.008491333512264675" + 
":  " + 
"(b('moss') <= 6.485493421554565) ? " + 
"0.005706676130538511" + 
":  " + 
"0.10084914906019976" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 28.653759002685547) ? " + 
"(b('crop') <= 2.4269771575927734) ? " + 
"(b('crop') <= 1.691142737865448) ? " + 
"2.19826670697841e-05" + 
":  " + 
"-0.02921557870451966" + 
":  " + 
"(b('b10') <= 1335.5) ? " + 
"-0.008805656750512468" + 
":  " + 
"0.0165445180505748" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"(b('crop') <= 43.28263282775879) ? " + 
"0.008811447852968005" + 
":  " + 
"-0.0006082051612117344" + 
":  " + 
"(b('lia') <= 37.17656898498535) ? " + 
"-0.034651616417981666" + 
":  " + 
"-0.06173552556206183" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('b6') <= 3119.5) ? " + 
"(b('b6') <= 3058.5) ? " + 
"0.0006915629186105539" + 
":  " + 
"0.01880719826583108" + 
":  " + 
"(b('b11') <= 2301.0) ? " + 
"-0.007633009179406608" + 
":  " + 
"0.0002965980284004557" + 
":  " + 
"(b('g0vv') <= -10.10158634185791) ? " + 
"(b('b1') <= 314.5) ? " + 
"-0.01187221189246884" + 
":  " + 
"-0.0017408485745729957" + 
":  " + 
"(b('crop') <= 48.84012222290039) ? " + 
"0.015252905171681019" + 
":  " + 
"-0.0038472070181633294" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1536.5) ? " + 
"(b('b6') <= 2149.5) ? " + 
"(b('b6') <= 2110.5) ? " + 
"-0.005938506194402345" + 
":  " + 
"-0.04474827120280049" + 
":  " + 
"(b('b4') <= 1429.0) ? " + 
"0.005045671852639748" + 
":  " + 
"-0.0023810508522681038" + 
":  " + 
"(b('bare') <= 10.783052444458008) ? " + 
"(b('moss') <= 13.891517639160156) ? " + 
"0.001018062853880596" + 
":  " + 
"-0.004692870724946191" + 
":  " + 
"(b('b1') <= 913.5) ? " + 
"0.006920452947058597" + 
":  " + 
"0.061799901997705735" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('b4') <= 986.5) ? " + 
"(b('b3') <= 836.5) ? " + 
"-0.00034770072959542194" + 
":  " + 
"0.015469927628631497" + 
":  " + 
"(b('b4') <= 1008.5) ? " + 
"-0.016332211781196718" + 
":  " + 
"-4.746235132372736e-05" + 
":  " + 
"(b('b5') <= 4200.0) ? " + 
"(b('b5') <= 2568.75) ? " + 
"0.0017451162585274157" + 
":  " + 
"-0.00430073981696706" + 
":  " + 
"(b('grass') <= 12.508757293224335) ? " + 
"0.02210207038455893" + 
":  " + 
"0.08461207203349613" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3471.5) ? " + 
"(b('b3') <= 910.5) ? " + 
"-0.0010617961570150356" + 
":  " + 
"0.0009916708299886128" + 
":  " + 
"(b('lia') <= 43.163883209228516) ? " + 
"0.009030784755504489" + 
":  " + 
"0.04181367637134186" + 
":  " + 
"(b('b5') <= 3519.5) ? " + 
"(b('g0vv') <= -11.965662002563477) ? " + 
"-0.03573772356111876" + 
":  " + 
"-0.07934295084382241" + 
":  " + 
"(b('grass') <= 49.40912055969238) ? " + 
"-0.002347135828402644" + 
":  " + 
"0.02804429386039331" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 314.5) ? " + 
"(b('b6') <= 2118.5) ? " + 
"(b('g0vh') <= -17.254621505737305) ? " + 
"-0.007164867034918763" + 
":  " + 
"0.012816930230578671" + 
":  " + 
"(b('trees') <= 13.069013595581055) ? " + 
"0.04277184529272915" + 
":  " + 
"-0.050613615087457355" + 
":  " + 
"(b('b3') <= 562.5) ? " + 
"(b('b5') <= 1413.5) ? " + 
"0.004262452051970802" + 
":  " + 
"-0.02384936868602573" + 
":  " + 
"(b('b5') <= 1442.5) ? " + 
"0.0390983839077677" + 
":  " + 
"-4.692507433870274e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2662.5) ? " + 
"(b('b3') <= 882.5) ? " + 
"(b('b3') <= 860.5) ? " + 
"-0.0003302294290676844" + 
":  " + 
"-0.017962179919923753" + 
":  " + 
"(b('lia') <= 44.433509826660156) ? " + 
"0.008787653328868517" + 
":  " + 
"0.24283936645490822" + 
":  " + 
"(b('b6') <= 2699.5) ? " + 
"(b('ndvi') <= 2584.0) ? " + 
"-0.03008858156227821" + 
":  " + 
"0.00926431311531402" + 
":  " + 
"(b('b4') <= 947.5) ? " + 
"0.006639696081931519" + 
":  " + 
"-0.0007719782729054707" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.087481021881104) ? " + 
"(b('l8dt') <= 329036.5) ? " + 
"(b('b2') <= 461.0) ? " + 
"0.02302118800296746" + 
":  " + 
"0.00016328722353010203" + 
":  " + 
"(b('lia') <= 42.930320739746094) ? " + 
"-0.008688201149799521" + 
":  " + 
"0.015689804140049522" + 
":  " + 
"(b('g0vv') <= -15.02292776107788) ? " + 
"(b('crop') <= 62.37214469909668) ? " + 
"0.03445751821872564" + 
":  " + 
"-0.019768589295911514" + 
":  " + 
"(b('g0vh') <= -22.59265422821045) ? " + 
"0.010351670897311526" + 
":  " + 
"1.682649600316502e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 3244.5) ? " + 
"(b('b10') <= 3204.5) ? " + 
"(b('b5') <= 3162.5) ? " + 
"0.0004929144202178581" + 
":  " + 
"-0.0021186756552086564" + 
":  " + 
"(b('b5') <= 3146.0) ? " + 
"-0.02578995823419052" + 
":  " + 
"0.010540411047418527" + 
":  " + 
"(b('grass') <= 87.88689041137695) ? " + 
"(b('b4') <= 1984.5) ? " + 
"0.011952292119578475" + 
":  " + 
"0.00023491587630909556" + 
":  " + 
"(b('g0vh') <= -22.574913024902344) ? " + 
"-0.08458670792946382" + 
":  " + 
"-0.08979754294223993" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 28.15742301940918) ? " + 
"(b('lia') <= 28.144105911254883) ? " + 
"(b('b5') <= 1951.0) ? " + 
"0.02983454801041551" + 
":  " + 
"-0.005334603140602222" + 
":  " + 
"(b('b5') <= 2645.5) ? " + 
"-0.07967223956253265" + 
":  " + 
"-0.023627023028914684" + 
":  " + 
"(b('lia') <= 28.16038703918457) ? " + 
"(b('b2') <= 780.0) ? " + 
"0.10838168090578618" + 
":  " + 
"0.04027495421272581" + 
":  " + 
"(b('lia') <= 28.386530876159668) ? " + 
"0.015654139925193485" + 
":  " + 
"3.3983310066166275e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.218039989471436) ? " + 
"(b('l8dt') <= 219271.0) ? " + 
"(b('b4') <= 797.5) ? " + 
"0.019231929453999565" + 
":  " + 
"0.001656234027335359" + 
":  " + 
"(b('b2') <= 1020.0) ? " + 
"-0.005020859796633449" + 
":  " + 
"0.008479273508060462" + 
":  " + 
"(b('g0vv') <= -14.217326641082764) ? " + 
"0.1657495639744737" + 
":  " + 
"(b('g0vv') <= -14.198684692382812) ? " + 
"0.02527657474318497" + 
":  " + 
"0.00026601478635254744" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 666.5) ? " + 
"(b('crop') <= 48.6511173248291) ? " + 
"(b('ndvi') <= 5584.0) ? " + 
"0.0012056221374069215" + 
":  " + 
"0.11435301841639618" + 
":  " + 
"(b('b5') <= 2614.5) ? " + 
"-0.004873488195786361" + 
":  " + 
"-0.03224414141623409" + 
":  " + 
"(b('b3') <= 684.5) ? " + 
"(b('b1') <= 304.5) ? " + 
"0.022081049177744144" + 
":  " + 
"-0.0007423448516328097" + 
":  " + 
"(b('b3') <= 689.5) ? " + 
"-0.023359314770427828" + 
":  " + 
"7.934169241154598e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 5248578.0) ? " + 
"(b('b5') <= 1935.5) ? " + 
"(b('b5') <= 1927.0) ? " + 
"0.0017237676736322229" + 
":  " + 
"0.04445800255061764" + 
":  " + 
"(b('b3') <= 727.5) ? " + 
"-0.003356526365924297" + 
":  " + 
"0.0001535513068934198" + 
":  " + 
"(b('b6') <= 2116.5) ? " + 
"(b('crop') <= 45.897708892822266) ? " + 
"-0.06967832092020192" + 
":  " + 
"-0.008029093095688689" + 
":  " + 
"(b('b7') <= 1298.0) ? " + 
"0.10779393510681956" + 
":  " + 
"0.011067477095190075" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1536.5) ? " + 
"(b('lia') <= 43.52163505554199) ? " + 
"(b('b6') <= 2149.5) ? " + 
"-0.017135724791929936" + 
":  " + 
"-0.00013124593668393183" + 
":  " + 
"(b('b2') <= 526.0) ? " + 
"0.020110320205719873" + 
":  " + 
"-0.014523054345000097" + 
":  " + 
"(b('ndvi') <= 1545.5) ? " + 
"(b('grass') <= 83.44424438476562) ? " + 
"0.031751699927208485" + 
":  " + 
"-0.0524314104556455" + 
":  " + 
"(b('b1') <= 827.0) ? " + 
"0.000118487975813049" + 
":  " + 
"0.01062908989734786" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3551.5) ? " + 
"(b('b5') <= 3550.5) ? " + 
"(b('g0vh') <= -15.956182956695557) ? " + 
"-0.00015406879609446115" + 
":  " + 
"0.0033395460186685356" + 
":  " + 
"(b('lia') <= 41.03728675842285) ? " + 
"0.18083123773113974" + 
":  " + 
"0.10858708066938039" + 
":  " + 
"(b('b5') <= 3591.0) ? " + 
"(b('b3') <= 756.0) ? " + 
"-0.05676127415475825" + 
":  " + 
"-0.011995217224671107" + 
":  " + 
"(b('bare') <= 4.651249885559082) ? " + 
"0.0022751300271541056" + 
":  " + 
"-0.008961676555744742" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -11.432883739471436) ? " + 
"(b('b2') <= 314.5) ? " + 
"(b('l8dt') <= 1639051.5) ? " + 
"0.00977344357515086" + 
":  " + 
"-0.010011207216266079" + 
":  " + 
"(b('b2') <= 347.5) ? " + 
"-0.008306689266141221" + 
":  " + 
"0.00011071801577495202" + 
":  " + 
"(b('l8dt') <= 1123644.5) ? " + 
"(b('lia') <= 34.40300369262695) ? " + 
"-0.023670615850974408" + 
":  " + 
"-0.07165009347165273" + 
":  " + 
"(b('b4') <= 1200.0) ? " + 
"-0.012608071618826827" + 
":  " + 
"0.027558810606583883" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 362.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"(b('ndvi') <= 1906.0) ? " + 
"0.00951121740469963" + 
":  " + 
"-0.0026252159599906596" + 
":  " + 
"(b('b3') <= 843.5) ? " + 
"0.0062367869218476835" + 
":  " + 
"0.06451176576280945" + 
":  " + 
"(b('b1') <= 400.5) ? " + 
"(b('b4') <= 1122.0) ? " + 
"-0.009820980409023877" + 
":  " + 
"0.007508220736853604" + 
":  " + 
"(b('b2') <= 517.5) ? " + 
"0.00955973243266643" + 
":  " + 
"-0.00017376442089996663" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1134.5) ? " + 
"(b('b4') <= 1115.5) ? " + 
"(b('b3') <= 937.5) ? " + 
"-0.0006111891233565913" + 
":  " + 
"0.0092525347597423" + 
":  " + 
"(b('b4') <= 1116.5) ? " + 
"0.10075712197302104" + 
":  " + 
"0.01249452991385814" + 
":  " + 
"(b('b5') <= 1793.5) ? " + 
"(b('grass') <= 56.776649475097656) ? " + 
"-0.07297940299297584" + 
":  " + 
"-0.0031384889503112226" + 
":  " + 
"(b('b7') <= 1523.0) ? " + 
"-0.03857330423952535" + 
":  " + 
"-0.0003852714659448759" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2662.5) ? " + 
"(b('b3') <= 882.5) ? " + 
"(b('moss') <= 13.570855617523193) ? " + 
"0.0005912208078451103" + 
":  " + 
"-0.00859857351181025" + 
":  " + 
"(b('b3') <= 885.5) ? " + 
"0.045626520998072045" + 
":  " + 
"0.006542764027805832" + 
":  " + 
"(b('b5') <= 1673.0) ? " + 
"(b('b2') <= 653.0) ? " + 
"-0.06056127025623862" + 
":  " + 
"0.06413535450262789" + 
":  " + 
"(b('ndvi') <= 4626.5) ? " + 
"-0.00012052588732262923" + 
":  " + 
"-0.00920928714540353" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 919.5) ? " + 
"(b('grass') <= 76.45126724243164) ? " + 
"(b('b4') <= 902.5) ? " + 
"-0.000650687075147225" + 
":  " + 
"0.018048637710705806" + 
":  " + 
"(b('moss') <= 6.904706001281738) ? " + 
"0.0009921388983678892" + 
":  " + 
"0.04305886054230639" + 
":  " + 
"(b('b3') <= 910.5) ? " + 
"(b('trees') <= 14.47687816619873) ? " + 
"-0.0025866670160291073" + 
":  " + 
"-0.020510258003370183" + 
":  " + 
"(b('b4') <= 1131.5) ? " + 
"0.007488142261693224" + 
":  " + 
"-0.00035082586477259026" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 6342931.5) ? " + 
"(b('b5') <= 3533.0) ? " + 
"(b('b5') <= 3471.5) ? " + 
"7.142029902809297e-05" + 
":  " + 
"0.008252333151983765" + 
":  " + 
"(b('g0vh') <= -16.031259536743164) ? " + 
"-0.000358687340408212" + 
":  " + 
"-0.010919315973245546" + 
":  " + 
"(b('b7') <= 2695.0) ? " + 
"(b('ndvi') <= 3159.5) ? " + 
"-0.006437791166643366" + 
":  " + 
"0.01779671654787107" + 
":  " + 
"(b('g0vh') <= -19.190723419189453) ? " + 
"-0.03223335929418787" + 
":  " + 
"0.0656720336978905" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 757.5) ? " + 
"(b('grass') <= 74.05612182617188) ? " + 
"(b('b1') <= 325.5) ? " + 
"-0.002355665294449239" + 
":  " + 
"0.00511333556236184" + 
":  " + 
"(b('grass') <= 84.6655158996582) ? " + 
"0.04490603161392074" + 
":  " + 
"-0.013763514402696716" + 
":  " + 
"(b('b4') <= 771.5) ? " + 
"(b('moss') <= 7.189647436141968) ? " + 
"-0.02600312666788304" + 
":  " + 
"0.003306619367365261" + 
":  " + 
"(b('b1') <= 259.0) ? " + 
"-0.010350646120798867" + 
":  " + 
"1.4247156035269255e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 27.249680519104004) ? " + 
"(b('b5') <= 2328.5) ? " + 
"(b('b3') <= 1141.5) ? " + 
"-0.0018331152425115772" + 
":  " + 
"0.07793225792769756" + 
":  " + 
"(b('b2') <= 670.0) ? " + 
"-0.05426721221302317" + 
":  " + 
"-0.010987465191927417" + 
":  " + 
"(b('lia') <= 27.300000190734863) ? " + 
"(b('b1') <= 530.5) ? " + 
"0.10801990787609038" + 
":  " + 
"0.015083391451998798" + 
":  " + 
"(b('grass') <= 99.8344841003418) ? " + 
"-0.0001034332692405383" + 
":  " + 
"0.005465220749441615" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('b7') <= 2199.5) ? " + 
"(b('b2') <= 871.0) ? " + 
"-0.0044429222139215855" + 
":  " + 
"0.059109612518633774" + 
":  " + 
"(b('crop') <= 4.842228651046753) ? " + 
"-0.0015914437926604155" + 
":  " + 
"0.005517038474488859" + 
":  " + 
"(b('g0vv') <= -12.917322158813477) ? " + 
"(b('b5') <= 1701.0) ? " + 
"0.2615351608366416" + 
":  " + 
"0.01822343094610869" + 
":  " + 
"(b('trees') <= 8.639616012573242) ? " + 
"-0.0007404486416994908" + 
":  " + 
"0.002940772252876201" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 879.0) ? " + 
"(b('g0vh') <= -16.77571153640747) ? " + 
"(b('g0vv') <= -11.952876091003418) ? " + 
"-0.017726477239397225" + 
":  " + 
"-0.030906798292955128" + 
":  " + 
"-0.05545395666397358" + 
":  " + 
"(b('b6') <= 1222.0) ? " + 
"(b('ndvi') <= 1957.5) ? " + 
"-0.011913633018732836" + 
":  " + 
"0.024194105636791103" + 
":  " + 
"(b('b2') <= 230.5) ? " + 
"-0.022951006224978344" + 
":  " + 
"8.865974437224016e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 362.5) ? " + 
"(b('b2') <= 563.5) ? " + 
"(b('grass') <= 84.6655158996582) ? " + 
"0.001567975586639391" + 
":  " + 
"-0.029236467481595297" + 
":  " + 
"(b('b3') <= 975.5) ? " + 
"0.14339306288698594" + 
":  " + 
"0.014607153253910633" + 
":  " + 
"(b('b1') <= 383.5) ? " + 
"(b('b4') <= 1162.0) ? " + 
"-0.012334747158159206" + 
":  " + 
"0.02215698822538697" + 
":  " + 
"(b('b1') <= 384.5) ? " + 
"0.04986201276642168" + 
":  " + 
"-5.629883627196827e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('water') <= 0.49180328845977783) ? " + 
"(b('ndvi') <= 876.5) ? " + 
"-0.005877996161123387" + 
":  " + 
"0.00011277435125973196" + 
":  " + 
"(b('g0vh') <= -20.098700523376465) ? " + 
"-0.0325080251617233" + 
":  " + 
"0.11116259767076811" + 
":  " + 
"(b('b4') <= 2104.5) ? " + 
"(b('grass') <= 4.809688568115234) ? " + 
"0.025913684104746378" + 
":  " + 
"0.04272010068214212" + 
":  " + 
"(b('lia') <= 36.049673080444336) ? " + 
"0.011247494252690208" + 
":  " + 
"0.002455772878328785" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 10.783052444458008) ? " + 
"(b('moss') <= 15.544372081756592) ? " + 
"(b('b1') <= 628.5) ? " + 
"-0.0004787442056173969" + 
":  " + 
"0.002263464037475431" + 
":  " + 
"(b('b5') <= 1789.0) ? " + 
"0.023388343695891774" + 
":  " + 
"-0.006401288304652983" + 
":  " + 
"(b('b4') <= 1150.0) ? " + 
"(b('g0vv') <= -14.217384338378906) ? " + 
"-0.0030884096460114443" + 
":  " + 
"0.03312022102337631" + 
":  " + 
"(b('b6') <= 2710.0) ? " + 
"-0.018561503918723937" + 
":  " + 
"0.0025015677147489316" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3385997.0) ? " + 
"(b('b6') <= 2217.5) ? " + 
"(b('bare') <= 16.016435146331787) ? " + 
"0.002846692124932252" + 
":  " + 
"-0.03120798823641179" + 
":  " + 
"(b('b6') <= 2226.5) ? " + 
"-0.04135970809953801" + 
":  " + 
"-0.0003670320336092012" + 
":  " + 
"(b('trees') <= 12.64185619354248) ? " + 
"(b('moss') <= 14.125167846679688) ? " + 
"0.0045742886686033525" + 
":  " + 
"0.03849370848690829" + 
":  " + 
"(b('trees') <= 14.932132720947266) ? " + 
"-0.03338063789292716" + 
":  " + 
"0.008759344221552548" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -20.058966636657715) ? " + 
"(b('grass') <= 54.54540252685547) ? " + 
"(b('moss') <= 3.7803738117218018) ? " + 
"0.010393315952017701" + 
":  " + 
"0.007660525147338448" + 
":  " + 
"(b('g0vh') <= -22.5668363571167) ? " + 
"0.03156420136301247" + 
":  " + 
"0.045021890424347705" + 
":  " + 
"(b('lia') <= 44.96173286437988) ? " + 
"(b('lia') <= 44.94993591308594) ? " + 
"1.4500313904687896e-06" + 
":  " + 
"-0.023021405099109032" + 
":  " + 
"0.07519214283578649" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -23.63000202178955) ? " + 
"(b('l8dt') <= 129158.0) ? " + 
"(b('grass') <= 78.1655158996582) ? " + 
"-0.017845708092315823" + 
":  " + 
"-0.027448325987378508" + 
":  " + 
"(b('grass') <= 99.8344841003418) ? " + 
"0.013638484144229837" + 
":  " + 
"0.06090244120743402" + 
":  " + 
"(b('bare') <= 0.07329842634499073) ? " + 
"(b('bare') <= 0.010471204295754433) ? " + 
"-0.000604278282294691" + 
":  " + 
"-0.032991193959083516" + 
":  " + 
"(b('ndvi') <= 3929.5) ? " + 
"-0.00012217766403856142" + 
":  " + 
"0.007126121650787511" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"(b('ndvi') <= 2626.5) ? " + 
"0.00023803194791645349" + 
":  " + 
"0.010062885965730281" + 
":  " + 
"(b('g0vh') <= -15.721728324890137) ? " + 
"-0.041351700649437724" + 
":  " + 
"0.03609486525981159" + 
":  " + 
"(b('b6') <= 3483.5) ? " + 
"(b('b6') <= 3245.0) ? " + 
"-0.0010239760433340035" + 
":  " + 
"-0.017495776063045688" + 
":  " + 
"(b('ndvi') <= 2926.5) ? " + 
"-0.007980458007744256" + 
":  " + 
"0.013220704049433943" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('ndvi') <= 1576.5) ? " + 
"(b('b2') <= 696.5) ? " + 
"-0.00798224934579386" + 
":  " + 
"0.00022678699805768953" + 
":  " + 
"(b('b5') <= 3218.5) ? " + 
"0.002232574674689864" + 
":  " + 
"-0.0018624329528309639" + 
":  " + 
"(b('urban') <= 11.721758842468262) ? " + 
"(b('ndvi') <= 1827.0) ? " + 
"0.012513072617345515" + 
":  " + 
"-0.00680376823537584" + 
":  " + 
"(b('trees') <= 9.817587852478027) ? " + 
"-0.000515989456564734" + 
":  " + 
"0.02179220723650954" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1662.5) ? " + 
"(b('b3') <= 1243.5) ? " + 
"(b('b7') <= 3212.5) ? " + 
"0.00014554025398010183" + 
":  " + 
"-0.03610920651358011" + 
":  " + 
"(b('lia') <= 39.80718994140625) ? " + 
"0.0007673157062854948" + 
":  " + 
"0.0306113528101916" + 
":  " + 
"(b('b2') <= 679.5) ? " + 
"(b('b5') <= 3222.5) ? " + 
"-0.036232035878333936" + 
":  " + 
"-0.0017192338288801296" + 
":  " + 
"(b('b10') <= 2451.0) ? " + 
"-0.008024574875477494" + 
":  " + 
"0.00013964920853997377" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('b7') <= 2027.5) ? " + 
"(b('b2') <= 865.5) ? " + 
"-0.00465821465328613" + 
":  " + 
"0.10802899521877438" + 
":  " + 
"(b('grass') <= 42.90423011779785) ? " + 
"0.0049550810654054415" + 
":  " + 
"-0.001376927334530905" + 
":  " + 
"(b('g0vv') <= -12.917322158813477) ? " + 
"(b('b5') <= 1701.0) ? " + 
"0.23472634644541845" + 
":  " + 
"0.016453701665532002" + 
":  " + 
"(b('trees') <= 8.639616012573242) ? " + 
"-0.0006403512017437247" + 
":  " + 
"0.0026912587322404304" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 24.454398155212402) ? " + 
"(b('trees') <= 19.945929527282715) ? " + 
"(b('trees') <= 15.564701080322266) ? " + 
"0.00013676171042300778" + 
":  " + 
"-0.014793680323737039" + 
":  " + 
"(b('b10') <= 2342.5) ? " + 
"-0.0025690692668791032" + 
":  " + 
"0.018032380532265885" + 
":  " + 
"(b('l8dt') <= 1475001.0) ? " + 
"(b('g0vv') <= -13.090781211853027) ? " + 
"-0.029996474158771512" + 
":  " + 
"0.0023180450123748463" + 
":  " + 
"(b('b5') <= 2293.0) ? " + 
"0.005414175806301417" + 
":  " + 
"-0.04244019571152377" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1134.5) ? " + 
"(b('b4') <= 1115.5) ? " + 
"(b('grass') <= 81.45600891113281) ? " + 
"-0.0003531163961503608" + 
":  " + 
"0.01013301104009778" + 
":  " + 
"(b('b4') <= 1116.5) ? " + 
"0.08949570755019795" + 
":  " + 
"0.011177707449858562" + 
":  " + 
"(b('b1') <= 353.5) ? " + 
"(b('moss') <= 4.419529438018799) ? " + 
"-0.001296607468902547" + 
":  " + 
"-0.038052723508868784" + 
":  " + 
"(b('b1') <= 370.5) ? " + 
"0.03853139768801244" + 
":  " + 
"-0.0006392984580679962" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 10.783052444458008) ? " + 
"(b('moss') <= 15.027272701263428) ? " + 
"(b('moss') <= 14.589334487915039) ? " + 
"-9.179765520808928e-05" + 
":  " + 
"0.009905153658445208" + 
":  " + 
"(b('grass') <= 83.36150741577148) ? " + 
"-0.002589121546246794" + 
":  " + 
"-0.030677972120290574" + 
":  " + 
"(b('grass') <= 78.23077011108398) ? " + 
"(b('grass') <= 75.92367172241211) ? " + 
"0.001450331639379149" + 
":  " + 
"-0.028614257948904667" + 
":  " + 
"(b('b11') <= 2584.0) ? " + 
"0.03190252629416528" + 
":  " + 
"-0.0066974586026157185" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1988.5) ? " + 
"(b('b10') <= 1936.5) ? " + 
"(b('b11') <= 1868.5) ? " + 
"0.0010426564313495408" + 
":  " + 
"-0.03749148652454899" + 
":  " + 
"(b('b10') <= 1940.5) ? " + 
"0.06337090910011262" + 
":  " + 
"0.006473885928161402" + 
":  " + 
"(b('b5') <= 2081.5) ? " + 
"(b('b3') <= 1102.5) ? " + 
"-0.011379589334299615" + 
":  " + 
"0.03789614552526831" + 
":  " + 
"(b('b5') <= 2082.5) ? " + 
"0.0937131137801812" + 
":  " + 
"2.589985699987759e-06" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2667.5) ? " + 
"(b('b6') <= 2561.5) ? " + 
"(b('lia') <= 38.32318878173828) ? " + 
"-0.003635529334230124" + 
":  " + 
"0.0027807624226420823" + 
":  " + 
"(b('b3') <= 856.5) ? " + 
"-0.0005823648864212759" + 
":  " + 
"0.02292515055166389" + 
":  " + 
"(b('b6') <= 2699.5) ? " + 
"(b('b1') <= 364.0) ? " + 
"0.014091652318828012" + 
":  " + 
"-0.024997410103771937" + 
":  " + 
"(b('ndvi') <= 3523.0) ? " + 
"0.00031403246973351674" + 
":  " + 
"-0.005306338857340153" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 987.5) ? " + 
"(b('grass') <= 76.45126724243164) ? " + 
"(b('moss') <= 13.570855617523193) ? " + 
"0.0016185333152206893" + 
":  " + 
"-0.007879600761343055" + 
":  " + 
"(b('b3') <= 838.0) ? " + 
"0.0015488151419869645" + 
":  " + 
"0.03675794327328695" + 
":  " + 
"(b('b4') <= 1008.5) ? " + 
"(b('b1') <= 327.5) ? " + 
"0.021672120072252502" + 
":  " + 
"-0.018701128192668816" + 
":  " + 
"(b('b6') <= 2662.5) ? " + 
"0.0055191837056098505" + 
":  " + 
"-0.0008375026896022403" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -13.90178108215332) ? " + 
"(b('crop') <= 87.21756744384766) ? " + 
"(b('moss') <= 7.169239282608032) ? " + 
"-0.004139933219107795" + 
":  " + 
"0.0014069649229629443" + 
":  " + 
"(b('b5') <= 2537.0) ? " + 
"0.0606354371319623" + 
":  " + 
"0.007773735733610643" + 
":  " + 
"(b('g0vh') <= -22.5554838180542) ? " + 
"(b('b6') <= 2319.5) ? " + 
"0.1225981482087329" + 
":  " + 
"0.009128949716563082" + 
":  " + 
"(b('trees') <= 8.639616012573242) ? " + 
"-0.0005867651408891323" + 
":  " + 
"0.002161291250526619" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 614.5) ? " + 
"(b('l8dt') <= 1448115.0) ? " + 
"(b('b6') <= 2162.5) ? " + 
"0.00717750671169507" + 
":  " + 
"-0.012393517044445832" + 
":  " + 
"(b('urban') <= 0.0903225839138031) ? " + 
"-0.0070079633767207525" + 
":  " + 
"-0.03569543524407694" + 
":  " + 
"(b('b10') <= 997.0) ? " + 
"(b('b7') <= 970.0) ? " + 
"-0.0004148257986260736" + 
":  " + 
"0.04571579127029912" + 
":  " + 
"(b('b6') <= 1367.0) ? " + 
"-0.06570941706516624" + 
":  " + 
"8.875793280305805e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -8.018159866333008) ? " + 
"(b('urban') <= 25.92040252685547) ? " + 
"(b('urban') <= 14.72341012954712) ? " + 
"-0.0001619075944220421" + 
":  " + 
"0.009737323717759996" + 
":  " + 
"(b('g0vv') <= -11.88091516494751) ? " + 
"-0.013494584610593326" + 
":  " + 
"-0.001472596083060965" + 
":  " + 
"(b('crop') <= 42.59130668640137) ? " + 
"(b('b6') <= 2133.0) ? " + 
"-0.045781276733264875" + 
":  " + 
"0.04396898071019" + 
":  " + 
"(b('grass') <= 17.66968059539795) ? " + 
"0.005255504671750534" + 
":  " + 
"-0.0066814540362950614" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 879.0) ? " + 
"(b('g0vh') <= -16.77571153640747) ? " + 
"(b('ndvi') <= 3871.0) ? " + 
"-0.02960101263807771" + 
":  " + 
"-0.017783147091169824" + 
":  " + 
"-0.051606990906157515" + 
":  " + 
"(b('b2') <= 316.5) ? " + 
"(b('b6') <= 2118.5) ? " + 
"0.0009646930683186933" + 
":  " + 
"0.023436066938680635" + 
":  " + 
"(b('b2') <= 347.5) ? " + 
"-0.008250108668295486" + 
":  " + 
"0.00010411376966461305" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 5293547.5) ? " + 
"(b('b5') <= 3551.5) ? " + 
"(b('b5') <= 3550.5) ? " + 
"0.00015871492199335356" + 
":  " + 
"0.12965972971844913" + 
":  " + 
"(b('b5') <= 3591.0) ? " + 
"-0.017393015292165793" + 
":  " + 
"-0.0008625280014548075" + 
":  " + 
"(b('moss') <= 13.460219860076904) ? " + 
"(b('b1') <= 538.0) ? " + 
"0.021176255696872818" + 
":  " + 
"-0.001264771095939942" + 
":  " + 
"(b('b6') <= 2160.5) ? " + 
"-0.06471306330853993" + 
":  " + 
"-0.01571682394984199" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 1280.0) ? " + 
"(b('g0vv') <= -13.93202829360962) ? " + 
"(b('g0vh') <= -19.776747703552246) ? " + 
"-0.00033746155446641907" + 
":  " + 
"-0.01920617104558528" + 
":  " + 
"(b('g0vh') <= -17.590858459472656) ? " + 
"-0.02661866173858523" + 
":  " + 
"-0.009654313199216011" + 
":  " + 
"(b('b5') <= 1935.5) ? " + 
"(b('b4') <= 1154.5) ? " + 
"0.004693526779727198" + 
":  " + 
"-0.013672272470794493" + 
":  " + 
"(b('b2') <= 230.5) ? " + 
"-0.033990766254796446" + 
":  " + 
"-0.00013979733643361232" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 5456.5) ? " + 
"(b('b10') <= 3900.0) ? " + 
"(b('b6') <= 4842.0) ? " + 
"3.2991361242623e-05" + 
":  " + 
"-0.011133123474265075" + 
":  " + 
"(b('grass') <= 25.167882919311523) ? " + 
"0.005944329885760726" + 
":  " + 
"0.03643102090563829" + 
":  " + 
"(b('g0vh') <= -19.21955966949463) ? " + 
"(b('lia') <= 39.747976303100586) ? " + 
"-0.0008660182202753497" + 
":  " + 
"-0.01544372697792025" + 
":  " + 
"(b('b3') <= 2114.5) ? " + 
"-0.0571740285463983" + 
":  " + 
"-0.03339586877253573" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 28.15742301940918) ? " + 
"(b('g0vh') <= -13.760127544403076) ? " + 
"(b('ndvi') <= 4495.0) ? " + 
"-0.0039046382360337743" + 
":  " + 
"-0.06349500521027857" + 
":  " + 
"(b('g0vv') <= -7.141582489013672) ? " + 
"0.06150430278379215" + 
":  " + 
"0.08984313534939964" + 
":  " + 
"(b('lia') <= 28.160892486572266) ? " + 
"(b('b5') <= 3063.5) ? " + 
"0.03664061791602957" + 
":  " + 
"0.09726686625099146" + 
":  " + 
"(b('grass') <= 98.36243438720703) ? " + 
"-6.820261660513005e-05" + 
":  " + 
"0.004591195366999604" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 63281.0) ? " + 
"(b('g0vh') <= -16.571227073669434) ? " + 
"(b('b4') <= 789.5) ? " + 
"0.013180089360988332" + 
":  " + 
"-0.002733164623946591" + 
":  " + 
"(b('b6') <= 2123.5) ? " + 
"0.009096512512888299" + 
":  " + 
"-0.026531947556578183" + 
":  " + 
"(b('l8dt') <= 70515.5) ? " + 
"(b('l8dt') <= 70338.5) ? " + 
"0.00929372041653331" + 
":  " + 
"0.049813172376632596" + 
":  " + 
"(b('l8dt') <= 121900.5) ? " + 
"-0.0060416626046296" + 
":  " + 
"0.00010768754892049803" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.28081226348877) ? " + 
"(b('ndvi') <= 2682.0) ? " + 
"(b('ndvi') <= 2672.5) ? " + 
"-0.0008991387533290086" + 
":  " + 
"0.11735306870058053" + 
":  " + 
"(b('trees') <= 6.157119512557983) ? " + 
"0.00202537266339409" + 
":  " + 
"-0.02251370379978798" + 
":  " + 
"(b('grass') <= 90.44964218139648) ? " + 
"(b('grass') <= 83.4222640991211) ? " + 
"0.00027061993391380024" + 
":  " + 
"-0.007583141444136839" + 
":  " + 
"(b('grass') <= 93.51450729370117) ? " + 
"0.06381443668539555" + 
":  " + 
"0.0035370552833552463" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 11.215232372283936) ? " + 
"(b('trees') <= 11.076036930084229) ? " + 
"(b('trees') <= 10.893646240234375) ? " + 
"-0.00012710581936357435" + 
":  " + 
"0.034920376988864535" + 
":  " + 
"(b('g0vh') <= -13.84345006942749) ? " + 
"-0.01141167221380609" + 
":  " + 
"0.09066336351044184" + 
":  " + 
"(b('b3') <= 694.5) ? " + 
"(b('b6') <= 2898.0) ? " + 
"-0.0065690238657067634" + 
":  " + 
"-0.08916112270356717" + 
":  " + 
"(b('crop') <= 2.0734140276908875) ? " + 
"-0.0025510499555487652" + 
":  " + 
"0.007811703174614363" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('urban') <= 0.513603001832962) ? " + 
"(b('ndvi') <= 5278.5) ? " + 
"0.000405120162877429" + 
":  " + 
"-0.0055368214679658275" + 
":  " + 
"(b('ndvi') <= 5073.5) ? " + 
"0.005730019022281901" + 
":  " + 
"0.06705922447505427" + 
":  " + 
"(b('g0vv') <= -10.045888423919678) ? " + 
"(b('b1') <= 313.5) ? " + 
"-0.010217198971495754" + 
":  " + 
"-0.0013825149749508256" + 
":  " + 
"(b('crop') <= 48.84012222290039) ? " + 
"0.014703195983820158" + 
":  " + 
"-0.0035758327115256805" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 744.5) ? " + 
"(b('b6') <= 2762.5) ? " + 
"(b('b4') <= 742.5) ? " + 
"0.00031741254109872837" + 
":  " + 
"0.029554333808262608" + 
":  " + 
"(b('grass') <= 29.35964870452881) ? " + 
"-0.04268812339125612" + 
":  " + 
"0.044057257792064326" + 
":  " + 
"(b('b4') <= 747.5) ? " + 
"(b('b10') <= 1406.0) ? " + 
"-0.010427399295734201" + 
":  " + 
"-0.04402872121560792" + 
":  " + 
"(b('b1') <= 259.0) ? " + 
"-0.009878834191202121" + 
":  " + 
"-4.186778934825992e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 853.5) ? " + 
"(b('grass') <= 74.05612182617188) ? " + 
"(b('grass') <= 59.79380416870117) ? " + 
"0.0013470697118768138" + 
":  " + 
"-0.008421112712726301" + 
":  " + 
"(b('ndvi') <= 1721.5) ? " + 
"0.0958695683303683" + 
":  " + 
"0.012390426860441008" + 
":  " + 
"(b('b2') <= 368.0) ? " + 
"(b('b6') <= 2250.0) ? " + 
"0.021069538512709367" + 
":  " + 
"0.0822339071334444" + 
":  " + 
"(b('b4') <= 860.5) ? " + 
"-0.027167938093514202" + 
":  " + 
"-0.00036130720282420275" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 908.5) ? " + 
"(b('bare') <= 20.924105644226074) ? " + 
"(b('bare') <= 10.783052444458008) ? " + 
"-0.000540282841490666" + 
":  " + 
"0.006522588023894425" + 
":  " + 
"(b('ndvi') <= 1377.0) ? " + 
"0.01419947400814235" + 
":  " + 
"-0.032118990107911374" + 
":  " + 
"(b('b4') <= 1905.5) ? " + 
"(b('b5') <= 3842.0) ? " + 
"0.0063928227369196644" + 
":  " + 
"0.08361475757637815" + 
":  " + 
"(b('ndvi') <= 3101.5) ? " + 
"-0.0012656367041486418" + 
":  " + 
"0.018595603094825386" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -13.90178108215332) ? " + 
"(b('crop') <= 87.21756744384766) ? " + 
"(b('crop') <= 85.4493522644043) ? " + 
"-0.0014663403536151233" + 
":  " + 
"-0.030362792477145257" + 
":  " + 
"(b('g0vv') <= -13.950667381286621) ? " + 
"0.009488233201835325" + 
":  " + 
"0.08318501188900962" + 
":  " + 
"(b('grass') <= 34.49201011657715) ? " + 
"(b('moss') <= 1.5077694058418274) ? " + 
"0.0034612862699473644" + 
":  " + 
"-0.0013295094883109863" + 
":  " + 
"(b('b5') <= 2315.0) ? " + 
"-0.004014321746180846" + 
":  " + 
"0.005409069107180603" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 919.5) ? " + 
"(b('grass') <= 76.45126724243164) ? " + 
"(b('b4') <= 902.5) ? " + 
"-0.000320488462746736" + 
":  " + 
"0.01539742838313901" + 
":  " + 
"(b('moss') <= 6.904706001281738) ? " + 
"-0.0016975001511818598" + 
":  " + 
"0.035708721816107555" + 
":  " + 
"(b('b5') <= 1701.0) ? " + 
"(b('ndvi') <= 1404.0) ? " + 
"0.00704895378788286" + 
":  " + 
"-0.04097237855101359" + 
":  " + 
"(b('b7') <= 1483.5) ? " + 
"0.01399649579424074" + 
":  " + 
"-0.0005162441110164542" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"(b('trees') <= 1.8166741132736206) ? " + 
"-0.0008903181518252537" + 
":  " + 
"0.002977177604403379" + 
":  " + 
"(b('g0vh') <= -15.721728324890137) ? " + 
"-0.03818085116312223" + 
":  " + 
"0.03355985957001656" + 
":  " + 
"(b('b6') <= 3483.5) ? " + 
"(b('b6') <= 3245.0) ? " + 
"-0.00095368827571655" + 
":  " + 
"-0.015928375303794196" + 
":  " + 
"(b('b4') <= 1331.0) ? " + 
"0.028261743462710036" + 
":  " + 
"0.005074815954479866" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('b11') <= 2199.5) ? " + 
"(b('b2') <= 871.0) ? " + 
"-0.003918038885463308" + 
":  " + 
"0.04922232906752482" + 
":  " + 
"(b('b7') <= 2201.5) ? " + 
"0.047150695540426404" + 
":  " + 
"0.0008737345043373685" + 
":  " + 
"(b('g0vv') <= -12.933012008666992) ? " + 
"(b('b5') <= 1701.0) ? " + 
"0.2084552444020516" + 
":  " + 
"0.020263626844472218" + 
":  " + 
"(b('l8dt') <= 211317.5) ? " + 
"-0.002231709544457521" + 
":  " + 
"0.0010996818766378419" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3471.5) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"7.178931689795228e-06" + 
":  " + 
"0.01035562310970389" + 
":  " + 
"(b('g0vh') <= -19.790437698364258) ? " + 
"-0.004399694037138148" + 
":  " + 
"0.01668729093837211" + 
":  " + 
"(b('b5') <= 3520.5) ? " + 
"(b('g0vv') <= -11.849279880523682) ? " + 
"-0.026509542170996058" + 
":  " + 
"-0.06908701823295985" + 
":  " + 
"(b('b6') <= 2410.5) ? " + 
"0.005579796811689116" + 
":  " + 
"-0.0033687454560664943" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1708.5) ? " + 
"(b('b3') <= 1646.5) ? " + 
"(b('water') <= 0.49180328845977783) ? " + 
"4.5264720551562195e-05" + 
":  " + 
"-0.026497421836548168" + 
":  " + 
"(b('trees') <= 1.036898210644722) ? " + 
"-0.014617719170454692" + 
":  " + 
"0.01182639536191522" + 
":  " + 
"(b('b4') <= 2051.0) ? " + 
"(b('g0vh') <= -18.069981575012207) ? " + 
"0.02412868067030825" + 
":  " + 
"0.12034669450811551" + 
":  " + 
"(b('l8dt') <= 1344163.0) ? " + 
"0.002895983026362172" + 
":  " + 
"-0.014260964842510035" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1470.5) ? " + 
"(b('b4') <= 1662.5) ? " + 
"(b('b3') <= 1313.5) ? " + 
"0.0001500813380810532" + 
":  " + 
"0.017303184982068537" + 
":  " + 
"(b('b2') <= 1021.5) ? " + 
"-0.0047751797160261915" + 
":  " + 
"0.022859064932674738" + 
":  " + 
"(b('b4') <= 1815.5) ? " + 
"(b('b10') <= 2585.0) ? " + 
"0.0004912813054523737" + 
":  " + 
"0.06071127696932523" + 
":  " + 
"(b('b7') <= 2194.0) ? " + 
"0.07523582516746022" + 
":  " + 
"0.0004138044106124782" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b10') <= 3244.5) ? " + 
"(b('b4') <= 1830.5) ? " + 
"(b('b3') <= 1467.5) ? " + 
"0.00010106728947013319" + 
":  " + 
"0.023469379244342854" + 
":  " + 
"(b('b3') <= 1508.0) ? " + 
"-0.00926398450195974" + 
":  " + 
"0.000855761938143287" + 
":  " + 
"(b('b3') <= 1271.5) ? " + 
"(b('b5') <= 2886.5) ? " + 
"-0.03844837592129411" + 
":  " + 
"0.02430374216470152" + 
":  " + 
"(b('b5') <= 2877.0) ? " + 
"0.024808947061357795" + 
":  " + 
"0.0012966524195874415" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.07048988342285) ? " + 
"(b('lia') <= 38.01721382141113) ? " + 
"(b('lia') <= 37.84523963928223) ? " + 
"-0.0006563192425432471" + 
":  " + 
"0.016708946104470955" + 
":  " + 
"(b('crop') <= 37.13176345825195) ? " + 
"-0.049961312038887144" + 
":  " + 
"-0.014623541721954776" + 
":  " + 
"(b('grass') <= 16.995849609375) ? " + 
"(b('b5') <= 2041.5) ? " + 
"0.009869225370447134" + 
":  " + 
"-0.0019918707521783675" + 
":  " + 
"(b('lia') <= 38.37963676452637) ? " + 
"0.0158800692175551" + 
":  " + 
"0.001151376212087637" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 2.4269771575927734) ? " + 
"(b('crop') <= 1.691142737865448) ? " + 
"(b('trees') <= 12.852040767669678) ? " + 
"0.0007594210738099862" + 
":  " + 
"-0.007002627426318019" + 
":  " + 
"(b('l8dt') <= 899749.5) ? " + 
"-0.04139788154080747" + 
":  " + 
"0.03148270847733113" + 
":  " + 
"(b('crop') <= 20.82846736907959) ? " + 
"(b('ndvi') <= 3300.5) ? " + 
"0.041745996730907835" + 
":  " + 
"-0.014711526833113409" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.0005250625007624597" + 
":  " + 
"-0.02077417381279943" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1190.5) ? " + 
"(b('l8dt') <= 38479.0) ? " + 
"(b('b5') <= 2047.5) ? " + 
"0.05313339352322831" + 
":  " + 
"0.011077424234781785" + 
":  " + 
"(b('b2') <= 774.5) ? " + 
"-0.009011130463608744" + 
":  " + 
"-0.0008824545133894016" + 
":  " + 
"(b('ndvi') <= 1215.5) ? " + 
"(b('b10') <= 3214.5) ? " + 
"0.005313940648837409" + 
":  " + 
"0.06620948868683788" + 
":  " + 
"(b('bare') <= 29.32122039794922) ? " + 
"7.690957973083028e-05" + 
":  " + 
"0.02559293836346059" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 879.0) ? " + 
"(b('g0vv') <= -9.589491844177246) ? " + 
"(b('g0vv') <= -11.952876091003418) ? " + 
"-0.01844991465341188" + 
":  " + 
"-0.026657474817698094" + 
":  " + 
"-0.04803946253440965" + 
":  " + 
"(b('b6') <= 1240.5) ? " + 
"(b('ndvi') <= 1957.5) ? " + 
"-0.014338845335195286" + 
":  " + 
"0.01835538249811453" + 
":  " + 
"(b('b2') <= 230.5) ? " + 
"-0.032634004164003645" + 
":  " + 
"1.0311821682553194e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3551.5) ? " + 
"(b('b5') <= 3550.5) ? " + 
"(b('g0vv') <= -11.41415023803711) ? " + 
"-0.0005651316512619045" + 
":  " + 
"0.001389627333385051" + 
":  " + 
"(b('l8dt') <= 1621087.5) ? " + 
"0.14846541760044507" + 
":  " + 
"0.08344567624486166" + 
":  " + 
"(b('g0vh') <= -16.031259536743164) ? " + 
"(b('g0vh') <= -16.036385536193848) ? " + 
"-0.0003815694616769502" + 
":  " + 
"0.16562845531845052" + 
":  " + 
"(b('g0vh') <= -14.797223091125488) ? " + 
"-0.018985401815303157" + 
":  " + 
"0.0018301131026993553" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 318.5) ? " + 
"(b('b4') <= 1030.5) ? " + 
"(b('b1') <= 299.5) ? " + 
"0.0012656971673424661" + 
":  " + 
"-0.0064699304296563604" + 
":  " + 
"(b('ndvi') <= 4800.5) ? " + 
"-0.024151557854885257" + 
":  " + 
"0.1046427012917448" + 
":  " + 
"(b('b1') <= 344.5) ? " + 
"(b('crop') <= 32.8998908996582) ? " + 
"0.028609946358790384" + 
":  " + 
"0.00045677952663761333" + 
":  " + 
"(b('b6') <= 2561.5) ? " + 
"-0.003223299130506679" + 
":  " + 
"0.0004308517267273302" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 665.5) ? " + 
"(b('crop') <= 57.618377685546875) ? " + 
"(b('ndvi') <= 5604.0) ? " + 
"0.0005964302541134563" + 
":  " + 
"0.10297729915718952" + 
":  " + 
"(b('crop') <= 71.03791046142578) ? " + 
"-0.021766402167835753" + 
":  " + 
"0.0006481393970722803" + 
":  " + 
"(b('b3') <= 684.5) ? " + 
"(b('bare') <= 5.925170183181763) ? " + 
"0.009408768893700393" + 
":  " + 
"-0.04713578175810282" + 
":  " + 
"(b('b3') <= 689.5) ? " + 
"-0.019433941489587894" + 
":  " + 
"7.072975755360247e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('b6') <= 2750.5) ? " + 
"(b('b3') <= 705.5) ? " + 
"-0.00047745116238482883" + 
":  " + 
"-0.011275432469228571" + 
":  " + 
"(b('b5') <= 2616.5) ? " + 
"0.0010054156419420216" + 
":  " + 
"0.03909977349600516" + 
":  " + 
"(b('b3') <= 743.5) ? " + 
"(b('b10') <= 1916.0) ? " + 
"0.016755408348372462" + 
":  " + 
"-0.04211283849085787" + 
":  " + 
"(b('b4') <= 697.5) ? " + 
"0.010817549751225907" + 
":  " + 
"-0.00016217922244418" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"(b('trees') <= 1.8166741132736206) ? " + 
"-0.0007634855856059787" + 
":  " + 
"0.0027500516017015426" + 
":  " + 
"(b('ndvi') <= 2432.5) ? " + 
"-0.04381608172666342" + 
":  " + 
"-0.01388103324073778" + 
":  " + 
"(b('moss') <= 13.570855617523193) ? " + 
"(b('grass') <= 64.24228477478027) ? " + 
"-0.0008005539150791148" + 
":  " + 
"0.010505054670442892" + 
":  " + 
"(b('moss') <= 16.250526428222656) ? " + 
"-0.011537737425508504" + 
":  " + 
"0.005669303452624466" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 2.4269771575927734) ? " + 
"(b('crop') <= 1.691142737865448) ? " + 
"(b('moss') <= 8.33512544631958) ? " + 
"0.0027209032654448304" + 
":  " + 
"-0.002583808432446912" + 
":  " + 
"(b('l8dt') <= 899749.5) ? " + 
"-0.0377490630073218" + 
":  " + 
"0.027870663111748885" + 
":  " + 
"(b('crop') <= 13.887192249298096) ? " + 
"(b('b3') <= 841.0) ? " + 
"-0.0034858632627485526" + 
":  " + 
"0.05826157890426865" + 
":  " + 
"(b('grass') <= 62.17375946044922) ? " + 
"0.000529686583427333" + 
":  " + 
"-0.01909404471946217" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2003.5) ? " + 
"(b('b6') <= 3043.0) ? " + 
"(b('g0vv') <= -19.020509719848633) ? " + 
"0.14041762276952857" + 
":  " + 
"0.0006224344009608486" + 
":  " + 
"(b('trees') <= 10.719449520111084) ? " + 
"0.02397783899095871" + 
":  " + 
"-0.021010835422440335" + 
":  " + 
"(b('b5') <= 2006.5) ? " + 
"(b('l8dt') <= 648004.0) ? " + 
"-0.0663479337337007" + 
":  " + 
"-0.09488480398713206" + 
":  " + 
"(b('b5') <= 2081.5) ? " + 
"-0.006721763183856036" + 
":  " + 
"2.0305550957884455e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -16.012653350830078) ? " + 
"(b('ndvi') <= 2664.0) ? " + 
"(b('crop') <= 1.691142737865448) ? " + 
"-0.0040603750944847505" + 
":  " + 
"0.009697022258314165" + 
":  " + 
"(b('trees') <= 11.158273220062256) ? " + 
"-0.007819576321212501" + 
":  " + 
"-0.031113733776099745" + 
":  " + 
"(b('g0vv') <= -16.002360343933105) ? " + 
"(b('b2') <= 601.5) ? " + 
"0.06853993840239854" + 
":  " + 
"0.013159161098589608" + 
":  " + 
"(b('g0vh') <= -22.985011100769043) ? " + 
"0.008993839129920432" + 
":  " + 
"7.288940940258917e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.31542158126831) ? " + 
"(b('l8dt') <= 903577.5) ? " + 
"(b('l8dt') <= 903179.0) ? " + 
"-0.0001324433354859847" + 
":  " + 
"0.1000027987915947" + 
":  " + 
"(b('crop') <= 62.54383087158203) ? " + 
"-0.0040313699058119245" + 
":  " + 
"-0.02136940500379524" + 
":  " + 
"(b('g0vh') <= -22.5554838180542) ? " + 
"(b('moss') <= 18.861797332763672) ? " + 
"0.007169431255641435" + 
":  " + 
"0.10401622153201957" + 
":  " + 
"(b('g0vh') <= -22.075679779052734) ? " + 
"-0.007244318940117837" + 
":  " + 
"0.0003625031730853019" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 27.911441802978516) ? " + 
"(b('b5') <= 2328.5) ? " + 
"(b('b3') <= 1141.5) ? " + 
"-0.0018188429111257775" + 
":  " + 
"0.06091882682288165" + 
":  " + 
"(b('g0vv') <= -9.297230243682861) ? " + 
"-0.01346901519203265" + 
":  " + 
"0.05475115533012498" + 
":  " + 
"(b('lia') <= 27.91947841644287) ? " + 
"0.10089040476879148" + 
":  " + 
"(b('g0vv') <= -15.28081226348877) ? " + 
"-0.002146038223667159" + 
":  " + 
"0.00033548629464635594" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 16563.0) ? " + 
"(b('b3') <= 1245.5) ? " + 
"(b('b7') <= 2820.5) ? " + 
"-0.005761718440921415" + 
":  " + 
"-0.05376218493685697" + 
":  " + 
"(b('lia') <= 42.717525482177734) ? " + 
"0.05799854247439493" + 
":  " + 
"-0.001632857205854904" + 
":  " + 
"(b('l8dt') <= 16595.0) ? " + 
"(b('grass') <= 70.20273208618164) ? " + 
"0.01326911474094379" + 
":  " + 
"0.07387367899452538" + 
":  " + 
"(b('l8dt') <= 16629.5) ? " + 
"-0.04613421928949476" + 
":  " + 
"2.9294284776015822e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 568285.5) ? " + 
"(b('l8dt') <= 489297.0) ? " + 
"(b('b6') <= 2217.5) ? " + 
"0.005781296225956017" + 
":  " + 
"-0.0005985776699231935" + 
":  " + 
"(b('lia') <= 41.557655334472656) ? " + 
"0.01080720853554545" + 
":  " + 
"-0.008902096338251052" + 
":  " + 
"(b('g0vv') <= -12.946414470672607) ? " + 
"(b('moss') <= 16.11005973815918) ? " + 
"-0.00465964922810397" + 
":  " + 
"0.008064269120449725" + 
":  " + 
"(b('grass') <= 76.45126724243164) ? " + 
"-0.00012850018898598756" + 
":  " + 
"0.011707740018480559" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 34.4125919342041) ? " + 
"(b('g0vh') <= -17.027827262878418) ? " + 
"(b('lia') <= 33.70698165893555) ? " + 
"-0.0013596387946578704" + 
":  " + 
"-0.011612302378779393" + 
":  " + 
"(b('b1') <= 608.5) ? " + 
"0.006012672892395162" + 
":  " + 
"-0.010096793650422854" + 
":  " + 
"(b('lia') <= 34.449153900146484) ? " + 
"(b('ndvi') <= 1324.0) ? " + 
"0.06585351800140019" + 
":  " + 
"0.018627811394068997" + 
":  " + 
"(b('bare') <= 8.550963878631592) ? " + 
"-0.00023228875533184873" + 
":  " + 
"0.0039872002955352185" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 666.5) ? " + 
"(b('crop') <= 57.618377685546875) ? " + 
"(b('b1') <= 377.5) ? " + 
"0.0027790412171134066" + 
":  " + 
"-0.023524166865290158" + 
":  " + 
"(b('crop') <= 71.03791046142578) ? " + 
"-0.01999675881732105" + 
":  " + 
"0.0004902118866219915" + 
":  " + 
"(b('b4') <= 793.5) ? " + 
"(b('b4') <= 792.5) ? " + 
"0.002469723095637211" + 
":  " + 
"0.059262790898044176" + 
":  " + 
"(b('b4') <= 800.5) ? " + 
"-0.029570093103584206" + 
":  " + 
"-0.00015290400814102045" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"0.0004395129650416272" + 
":  " + 
"0.024803549070015335" + 
":  " + 
"(b('b3') <= 1277.5) ? " + 
"-0.04263353610425244" + 
":  " + 
"-0.014939420873955184" + 
":  " + 
"(b('ndvi') <= 2836.0) ? " + 
"(b('urban') <= 34.57631492614746) ? " + 
"-0.009123831313801272" + 
":  " + 
"-0.06094018858332743" + 
":  " + 
"(b('b6') <= 3624.5) ? " + 
"-0.001016118120016408" + 
":  " + 
"0.012356480753200057" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3385.5) ? " + 
"(b('b5') <= 3332.5) ? " + 
"(b('moss') <= 26.31478500366211) ? " + 
"-3.0383016421021224e-05" + 
":  " + 
"0.015100573841106255" + 
":  " + 
"(b('grass') <= 16.84616184234619) ? " + 
"0.0006796474117779606" + 
":  " + 
"0.020591426901009836" + 
":  " + 
"(b('urban') <= 34.57631492614746) ? " + 
"(b('trees') <= 10.084112167358398) ? " + 
"0.0009452538074616845" + 
":  " + 
"-0.006722843830636465" + 
":  " + 
"(b('b7') <= 1292.5) ? " + 
"-0.0684387552316833" + 
":  " + 
"-0.020207035914336726" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1544.5) ? " + 
"(b('b4') <= 1541.5) ? " + 
"(b('b1') <= 772.5) ? " + 
"0.0004516131223677517" + 
":  " + 
"-0.022729059154544803" + 
":  " + 
"(b('ndvi') <= 1721.0) ? " + 
"0.01137467195215318" + 
":  " + 
"0.07336300596566546" + 
":  " + 
"(b('b3') <= 1211.5) ? " + 
"(b('b7') <= 1746.0) ? " + 
"0.09029616226908434" + 
":  " + 
"-0.011553117704464815" + 
":  " + 
"(b('b2') <= 600.5) ? " + 
"0.0765622369968812" + 
":  " + 
"-2.5875737903823625e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -11.45814323425293) ? " + 
"(b('g0vv') <= -7.955878496170044) ? " + 
"(b('g0vv') <= -7.958283185958862) ? " + 
"-0.00013546051121160512" + 
":  " + 
"-0.06907342198670245" + 
":  " + 
"(b('b5') <= 4367.5) ? " + 
"0.003899974125414547" + 
":  " + 
"-0.023837756802400217" + 
":  " + 
"(b('l8dt') <= 1123644.5) ? " + 
"(b('lia') <= 34.40300369262695) ? " + 
"-0.02047035117464517" + 
":  " + 
"-0.06250292741667485" + 
":  " + 
"(b('crop') <= 59.458757400512695) ? " + 
"0.04074479906701872" + 
":  " + 
"-0.008101382537886673" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 18.02293586730957) ? " + 
"(b('moss') <= 17.294462203979492) ? " + 
"(b('lia') <= 27.911441802978516) ? " + 
"-0.008679124892628167" + 
":  " + 
"0.00010649871014394123" + 
":  " + 
"(b('b1') <= 609.5) ? " + 
"0.04724721607860369" + 
":  " + 
"-0.001515054875621595" + 
":  " + 
"(b('lia') <= 29.166658401489258) ? " + 
"(b('g0vv') <= -12.717386722564697) ? " + 
"0.0019249825558031557" + 
":  " + 
"0.06459797597470608" + 
":  " + 
"(b('g0vv') <= -10.199311256408691) ? " + 
"-0.006456193430811708" + 
":  " + 
"0.01233735209290276" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 26.05080795288086) ? " + 
"(b('g0vh') <= -20.765707969665527) ? " + 
"(b('b10') <= 2487.5) ? " + 
"-0.004280585691467785" + 
":  " + 
"0.03395187063237964" + 
":  " + 
"(b('b10') <= 2314.0) ? " + 
"0.07571520514093975" + 
":  " + 
"0.027381542474895975" + 
":  " + 
"(b('lia') <= 27.249680519104004) ? " + 
"(b('b5') <= 2328.5) ? " + 
"0.006349730527980147" + 
":  " + 
"-0.02157879194968769" + 
":  " + 
"(b('lia') <= 27.264925003051758) ? " + 
"0.035478264540171944" + 
":  " + 
"3.9613655169010876e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 568285.5) ? " + 
"(b('l8dt') <= 489297.0) ? " + 
"(b('grass') <= 1.6627711057662964) ? " + 
"0.006197788793768519" + 
":  " + 
"-0.0004329385057143606" + 
":  " + 
"(b('lia') <= 41.557655334472656) ? " + 
"0.0097690298193519" + 
":  " + 
"-0.008098313633148045" + 
":  " + 
"(b('b6') <= 4860.5) ? " + 
"(b('g0vv') <= -12.296576499938965) ? " + 
"-0.0027907343039234064" + 
":  " + 
"0.0008519947755866425" + 
":  " + 
"(b('g0vv') <= -10.9080228805542) ? " + 
"-0.008542343123264901" + 
":  " + 
"-0.051122530847977646" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 1.9490950107574463) ? " + 
"(b('b4') <= 1439.75) ? " + 
"(b('b3') <= 1082.5) ? " + 
"0.00043210064958694737" + 
":  " + 
"0.010385669922449627" + 
":  " + 
"(b('b3') <= 1112.5) ? " + 
"-0.010126250657879168" + 
":  " + 
"-0.00012339818159990546" + 
":  " + 
"(b('g0vh') <= -15.9645357131958) ? " + 
"(b('b5') <= 2623.5) ? " + 
"0.0003465531627554761" + 
":  " + 
"-0.005178621151075288" + 
":  " + 
"(b('bare') <= 0.4333333373069763) ? " + 
"-0.00648680105866593" + 
":  " + 
"0.008463303118227626" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 43.82534217834473) ? " + 
"(b('lia') <= 43.20435905456543) ? " + 
"(b('lia') <= 42.24803924560547) ? " + 
"-0.00019480688257601865" + 
":  " + 
"0.005043577275319254" + 
":  " + 
"(b('b6') <= 1855.0) ? " + 
"0.017208748237444636" + 
":  " + 
"-0.0057919939093449765" + 
":  " + 
"(b('crop') <= 82.96915435791016) ? " + 
"(b('b5') <= 3074.0) ? " + 
"-0.0001371360498043461" + 
":  " + 
"0.010373354757821949" + 
":  " + 
"(b('g0vh') <= -19.265411376953125) ? " + 
"0.05666600330944985" + 
":  " + 
"0.08744163686699458" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -23.840018272399902) ? " + 
"(b('l8dt') <= 523617.0) ? " + 
"(b('b11') <= 2691.5) ? " + 
"0.020790027996714398" + 
":  " + 
"-0.022721601925976855" + 
":  " + 
"(b('b1') <= 615.5) ? " + 
"0.038062853920787586" + 
":  " + 
"0.06601353961290755" + 
":  " + 
"(b('g0vv') <= -19.141870498657227) ? " + 
"(b('g0vv') <= -19.158891677856445) ? " + 
"0.008759969126379559" + 
":  " + 
"0.12767950548980186" + 
":  " + 
"(b('g0vv') <= -17.148531913757324) ? " + 
"-0.005444558087372822" + 
":  " + 
"6.512131735058815e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('trees') <= 1.8166741132736206) ? " + 
"(b('moss') <= 3.4934709072113037) ? " + 
"-0.003584509335197383" + 
":  " + 
"0.0008708614848110808" + 
":  " + 
"(b('trees') <= 3.377434730529785) ? " + 
"0.03326153675571427" + 
":  " + 
"0.0013681057908636687" + 
":  " + 
"(b('moss') <= 13.570855617523193) ? " + 
"(b('grass') <= 44.59784507751465) ? " + 
"-0.001308853360268696" + 
":  " + 
"0.0067683447662343745" + 
":  " + 
"(b('moss') <= 16.250526428222656) ? " + 
"-0.010357450981404333" + 
":  " + 
"0.004601176081506292" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('moss') <= 0.4290978014469147) ? " + 
"(b('trees') <= 6.157119512557983) ? " + 
"-0.004358472854618167" + 
":  " + 
"-0.03060074904958432" + 
":  " + 
"(b('g0vh') <= -21.187747955322266) ? " + 
"0.021235810788392494" + 
":  " + 
"-0.0008842654962742771" + 
":  " + 
"(b('b3') <= 743.5) ? " + 
"(b('b3') <= 741.5) ? " + 
"0.006456697081082274" + 
":  " + 
"0.05142790633493449" + 
":  " + 
"(b('b4') <= 697.5) ? " + 
"0.00985594886651591" + 
":  " + 
"-0.00012771504531314278" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 18.02293586730957) ? " + 
"(b('moss') <= 17.294462203979492) ? " + 
"(b('lia') <= 28.971567153930664) ? " + 
"-0.004675824739123714" + 
":  " + 
"0.0001957801804621804" + 
":  " + 
"(b('b2') <= 768.5) ? " + 
"0.04475199157397849" + 
":  " + 
"-0.0007296500903152709" + 
":  " + 
"(b('trees') <= 0.3045685291290283) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"-0.020495755813521893" + 
":  " + 
"0.007685246039042405" + 
":  " + 
"(b('g0vh') <= -17.354702949523926) ? " + 
"-0.01599934775853413" + 
":  " + 
"0.006034096062237873" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 44.96173286437988) ? " + 
"(b('lia') <= 44.94993591308594) ? " + 
"(b('lia') <= 44.90682029724121) ? " + 
"-9.369475948390025e-06" + 
":  " + 
"0.022576775871046888" + 
":  " + 
"(b('g0vv') <= -14.044851779937744) ? " + 
"-0.009907873477961213" + 
":  " + 
"-0.05494242086266606" + 
":  " + 
"0.06628142102339643" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3518.0) ? " + 
"(b('b5') <= 3471.5) ? " + 
"(b('crop') <= 2.854820489883423) ? " + 
"-0.001071123930162085" + 
":  " + 
"0.0007191560196360675" + 
":  " + 
"(b('grass') <= 0.16759777069091797) ? " + 
"0.03155772030119278" + 
":  " + 
"0.006193057567285999" + 
":  " + 
"(b('b5') <= 3520.5) ? " + 
"(b('g0vv') <= -11.849279880523682) ? " + 
"-0.023314714259912803" + 
":  " + 
"-0.06252529971866558" + 
":  " + 
"(b('b6') <= 2410.5) ? " + 
"0.005059146901676833" + 
":  " + 
"-0.003089762031032224" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 2644.5) ? " + 
"(b('b6') <= 4973.5) ? " + 
"(b('b4') <= 2553.0) ? " + 
"7.444133523533168e-06" + 
":  " + 
"-0.014207391911869916" + 
":  " + 
"(b('l8dt') <= 1189977.5) ? " + 
"-0.006881735320108603" + 
":  " + 
"-0.0488972669449577" + 
":  " + 
"(b('b1') <= 991.0) ? " + 
"(b('g0vh') <= -14.067272663116455) ? " + 
"0.0402238119353347" + 
":  " + 
"-0.08251407535941668" + 
":  " + 
"(b('ndvi') <= 2264.0) ? " + 
"-0.0008535143098132764" + 
":  " + 
"0.04986461537612132" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1708.5) ? " + 
"(b('bare') <= 20.924105644226074) ? " + 
"(b('bare') <= 19.116829872131348) ? " + 
"-3.135870049388023e-05" + 
":  " + 
"0.02180910416681791" + 
":  " + 
"(b('moss') <= 12.933144569396973) ? " + 
"-0.016298671953005727" + 
":  " + 
"0.002516160309577918" + 
":  " + 
"(b('b4') <= 2051.0) ? " + 
"(b('g0vh') <= -18.069981575012207) ? " + 
"0.021243767695179498" + 
":  " + 
"0.1072283830242656" + 
":  " + 
"(b('b1') <= 723.0) ? " + 
"0.05213402517924505" + 
":  " + 
"0.0010858646587028013" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('g0vv') <= -5.449887037277222) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"0.0004553180304857639" + 
":  " + 
"-0.026943181572755992" + 
":  " + 
"(b('trees') <= 0.17499999701976776) ? " + 
"0.054901355495001955" + 
":  " + 
"0.00821986479872525" + 
":  " + 
"(b('ndvi') <= 2836.0) ? " + 
"(b('b4') <= 563.0) ? " + 
"-0.1659419739814853" + 
":  " + 
"-0.009473814202958966" + 
":  " + 
"(b('b6') <= 3624.5) ? " + 
"-0.0009598190557096632" + 
":  " + 
"0.011105293126184893" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3551.5) ? " + 
"(b('b5') <= 3550.5) ? " + 
"(b('trees') <= 14.304625511169434) ? " + 
"0.0004414754082431731" + 
":  " + 
"-0.0028293789774428697" + 
":  " + 
"(b('g0vh') <= -17.019862174987793) ? " + 
"0.07505428544639742" + 
":  " + 
"0.13357205266642247" + 
":  " + 
"(b('b5') <= 3591.0) ? " + 
"(b('l8dt') <= 2225271.5) ? " + 
"-0.01684200754637134" + 
":  " + 
"0.03128617207775363" + 
":  " + 
"(b('bare') <= 4.651249885559082) ? " + 
"0.002037276078171016" + 
":  " + 
"-0.007976442193525422" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 11.215232372283936) ? " + 
"(b('trees') <= 11.076036930084229) ? " + 
"(b('trees') <= 10.893646240234375) ? " + 
"-0.00012066009554902358" + 
":  " + 
"0.025582377936762178" + 
":  " + 
"(b('g0vv') <= -13.304911613464355) ? " + 
"-0.08351031913789615" + 
":  " + 
"-0.006965070975581184" + 
":  " + 
"(b('trees') <= 12.501765251159668) ? " + 
"(b('b6') <= 3911.5) ? " + 
"0.011116199972845821" + 
":  " + 
"-0.015641451858873195" + 
":  " + 
"(b('l8dt') <= 1057727.5) ? " + 
"0.0016127247616098711" + 
":  " + 
"-0.008329648272978173" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 314.5) ? " + 
"(b('l8dt') <= 1639051.5) ? " + 
"(b('ndvi') <= 5604.0) ? " + 
"0.006456090544279852" + 
":  " + 
"0.1058375318090618" + 
":  " + 
"(b('crop') <= 81.81896209716797) ? " + 
"-0.004749927900399687" + 
":  " + 
"-0.08318100993659351" + 
":  " + 
"(b('b3') <= 562.5) ? " + 
"(b('b5') <= 1761.5) ? " + 
"-0.0009590962214290257" + 
":  " + 
"-0.024579999909743522" + 
":  " + 
"(b('b5') <= 1442.5) ? " + 
"0.03164485722392821" + 
":  " + 
"-2.8564663926900653e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 4817392.5) ? " + 
"(b('l8dt') <= 1260122.5) ? " + 
"(b('l8dt') <= 1187961.0) ? " + 
"2.9783832082489603e-05" + 
":  " + 
"0.012984497822816958" + 
":  " + 
"(b('b6') <= 4860.5) ? " + 
"-0.0010110795473922461" + 
":  " + 
"-0.030796136063255958" + 
":  " + 
"(b('ndvi') <= 4742.0) ? " + 
"(b('grass') <= 76.81272506713867) ? " + 
"0.009545585833107743" + 
":  " + 
"0.14055067410354313" + 
":  " + 
"(b('g0vh') <= -16.40074062347412) ? " + 
"-0.04849153207092863" + 
":  " + 
"0.0008304568368882826" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3385997.0) ? " + 
"(b('l8dt') <= 3346463.0) ? " + 
"(b('b6') <= 2217.5) ? " + 
"0.0019501816428731471" + 
":  " + 
"-0.0003816339775757305" + 
":  " + 
"(b('b6') <= 3166.5) ? " + 
"-0.00932864917475654" + 
":  " + 
"-0.048801392990798456" + 
":  " + 
"(b('b6') <= 2252.5) ? " + 
"(b('g0vh') <= -19.4749755859375) ? " + 
"0.024110993938048123" + 
":  " + 
"-0.014066599993893106" + 
":  " + 
"(b('lia') <= 41.29780387878418) ? " + 
"0.0026722033815327474" + 
":  " + 
"0.016715786188960045" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 2644.5) ? " + 
"(b('b5') <= 3533.0) ? " + 
"(b('b5') <= 3531.0) ? " + 
"0.0001510440650716931" + 
":  " + 
"0.0340837638479355" + 
":  " + 
"(b('bare') <= 6.334192276000977) ? " + 
"-0.0012731097834517372" + 
":  " + 
"-0.01637158669377465" + 
":  " + 
"(b('b1') <= 991.0) ? " + 
"(b('g0vh') <= -14.067272663116455) ? " + 
"0.036480286699305295" + 
":  " + 
"-0.07457040620971406" + 
":  " + 
"(b('ndvi') <= 2264.0) ? " + 
"-0.0004821454080677389" + 
":  " + 
"0.04461843780712454" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 26.05080795288086) ? " + 
"(b('g0vh') <= -20.765707969665527) ? " + 
"(b('b11') <= 2487.5) ? " + 
"-0.00369054713962985" + 
":  " + 
"0.03188470990742786" + 
":  " + 
"(b('b11') <= 2217.5) ? " + 
"0.07836232732999197" + 
":  " + 
"0.029259232321867567" + 
":  " + 
"(b('lia') <= 27.173502922058105) ? " + 
"(b('b5') <= 2328.5) ? " + 
"0.003612454530180697" + 
":  " + 
"-0.021502972005115327" + 
":  " + 
"(b('lia') <= 27.17487907409668) ? " + 
"0.09286505653401722" + 
":  " + 
"2.7265601774143216e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 19.819469451904297) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('moss') <= 19.47174644470215) ? " + 
"5.332692606196241e-05" + 
":  " + 
"-0.020803883928727684" + 
":  " + 
"(b('lia') <= 34.84456443786621) ? " + 
"0.008381328287877614" + 
":  " + 
"0.05075173586401839" + 
":  " + 
"(b('lia') <= 29.158616065979004) ? " + 
"(b('b6') <= 3237.5) ? " + 
"0.13903640799688016" + 
":  " + 
"0.02193549049084026" + 
":  " + 
"(b('b5') <= 1786.5) ? " + 
"0.049864361784998756" + 
":  " + 
"-0.005484145153101987" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 16563.0) ? " + 
"(b('b3') <= 1245.5) ? " + 
"(b('l8dt') <= 16543.0) ? " + 
"0.0012453831096378193" + 
":  " + 
"-0.026842393215717793" + 
":  " + 
"(b('urban') <= 11.893129348754883) ? " + 
"0.05040630348474804" + 
":  " + 
"-0.002256478662872499" + 
":  " + 
"(b('l8dt') <= 21116.5) ? " + 
"(b('crop') <= 45.75570487976074) ? " + 
"0.03715737493727251" + 
":  " + 
"-0.004929968186339685" + 
":  " + 
"(b('l8dt') <= 39972.0) ? " + 
"-0.004875839441553721" + 
":  " + 
"0.00012801409844235558" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 568256.5) ? " + 
"(b('lia') <= 41.02482223510742) ? " + 
"(b('lia') <= 39.76312828063965) ? " + 
"0.0007578542804401499" + 
":  " + 
"0.008422992018000506" + 
":  " + 
"(b('g0vh') <= -15.692923069000244) ? " + 
"-0.0027581484763447173" + 
":  " + 
"0.011458145019816917" + 
":  " + 
"(b('b3') <= 761.5) ? " + 
"(b('grass') <= 83.60148620605469) ? " + 
"-0.0027216435509992984" + 
":  " + 
"-0.040577683748423646" + 
":  " + 
"(b('b11') <= 1470.5) ? " + 
"0.010865849514549258" + 
":  " + 
"-0.0006430566383765562" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -23.54457378387451) ? " + 
"(b('g0vh') <= -23.57124423980713) ? " + 
"(b('b3') <= 1062.5) ? " + 
"-0.005317010432030571" + 
":  " + 
"0.021123096375034345" + 
":  " + 
"0.09425575553976386" + 
":  " + 
"(b('trees') <= 4.231653451919556) ? " + 
"(b('trees') <= 3.2742620706558228) ? " + 
"7.088170587456774e-05" + 
":  " + 
"-0.007781091069773318" + 
":  " + 
"(b('trees') <= 6.304144859313965) ? " + 
"0.007258114759593603" + 
":  " + 
"-0.0002750117007070929" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2518.5) ? " + 
"(b('crop') <= 8.081742763519287) ? " + 
"(b('crop') <= 0.668789803981781) ? " + 
"-0.0007925022272580098" + 
":  " + 
"-0.01966692604926341" + 
":  " + 
"(b('b2') <= 884.0) ? " + 
"0.002858481274299228" + 
":  " + 
"0.042217365007472925" + 
":  " + 
"(b('b5') <= 2594.5) ? " + 
"(b('grass') <= 12.02562427520752) ? " + 
"0.006730058586388574" + 
":  " + 
"-0.009378928232869975" + 
":  " + 
"(b('grass') <= 35.55763244628906) ? " + 
"-0.0011894775590031545" + 
":  " + 
"0.0036792314005678053" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 1532.5) ? " + 
"(b('ndvi') <= 1530.5) ? " + 
"(b('grass') <= 91.94809341430664) ? " + 
"-0.0013095183712182265" + 
":  " + 
"0.009411275680863395" + 
":  " + 
"(b('g0vv') <= -13.247760772705078) ? " + 
"-0.05788253873319625" + 
":  " + 
"-0.002301285046821618" + 
":  " + 
"(b('b11') <= 2529.0) ? " + 
"(b('bare') <= 21.937710762023926) ? " + 
"-0.0001554398856944759" + 
":  " + 
"-0.029835927272365607" + 
":  " + 
"(b('b6') <= 3700.0) ? " + 
"0.008533160474521318" + 
":  " + 
"0.00037792106323521516" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1708.5) ? " + 
"(b('b3') <= 1612.0) ? " + 
"(b('b3') <= 1508.0) ? " + 
"-0.00022125220337623555" + 
":  " + 
"0.004918038623812456" + 
":  " + 
"(b('l8dt') <= 2701530.5) ? " + 
"-0.008346559399908603" + 
":  " + 
"0.026602941405054367" + 
":  " + 
"(b('b4') <= 2051.0) ? " + 
"(b('g0vh') <= -18.069981575012207) ? " + 
"0.018375405549914903" + 
":  " + 
"0.0953645805880616" + 
":  " + 
"(b('g0vh') <= -13.81140947341919) ? " + 
"0.0016867706203896411" + 
":  " + 
"-0.05474982586728621" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1292.5) ? " + 
"(b('b3') <= 1054.5) ? " + 
"(b('bare') <= 21.937710762023926) ? " + 
"4.71138821343711e-05" + 
":  " + 
"-0.039997775881514236" + 
":  " + 
"(b('trees') <= 7.2768025398254395) ? " + 
"0.02518750545026753" + 
":  " + 
"2.5699053776644686e-05" + 
":  " + 
"(b('b4') <= 1298.5) ? " + 
"(b('l8dt') <= 1354125.0) ? " + 
"-0.04178944529923056" + 
":  " + 
"0.007082923892632414" + 
":  " + 
"(b('b6') <= 2126.0) ? " + 
"-0.05274764552625892" + 
":  " + 
"-0.0004195472706192527" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3189.5) ? " + 
"(b('b5') <= 3187.5) ? " + 
"(b('b5') <= 3186.5) ? " + 
"0.00030202336066823595" + 
":  " + 
"-0.05255402447745618" + 
":  " + 
"(b('lia') <= 39.17761421203613) ? " + 
"0.09256115581012621" + 
":  " + 
"0.0036806504051900284" + 
":  " + 
"(b('grass') <= 0.16759777069091797) ? " + 
"(b('g0vv') <= -8.28941535949707) ? " + 
"0.009021137820490957" + 
":  " + 
"0.0589270285353376" + 
":  " + 
"(b('b7') <= 2563.0) ? " + 
"-0.004517981882509905" + 
":  " + 
"0.0014524246055724619" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 8.639616012573242) ? " + 
"(b('bare') <= 1.7923067808151245) ? " + 
"(b('trees') <= 7.263728618621826) ? " + 
"-0.0015774856592031725" + 
":  " + 
"-0.0509592116776006" + 
":  " + 
"(b('moss') <= 6.307743549346924) ? " + 
"0.007063542845463458" + 
":  " + 
"-0.0005146599085678981" + 
":  " + 
"(b('crop') <= 2.4269771575927734) ? " + 
"(b('bare') <= 1.0) ? " + 
"-0.010724990097935688" + 
":  " + 
"0.0008477241896465465" + 
":  " + 
"(b('grass') <= 45.792701721191406) ? " + 
"0.000497345124577744" + 
":  " + 
"0.015014239685433875" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 1292.5) ? " + 
"(b('b3') <= 1054.5) ? " + 
"(b('b6') <= 3058.5) ? " + 
"-0.0006998243239316434" + 
":  " + 
"0.0055046683159512425" + 
":  " + 
"(b('b6') <= 2730.0) ? " + 
"0.03727977412616705" + 
":  " + 
"0.0068529858026141624" + 
":  " + 
"(b('b4') <= 1298.5) ? " + 
"(b('g0vh') <= -18.420310020446777) ? " + 
"-0.03702566654479726" + 
":  " + 
"0.009478154587570497" + 
":  " + 
"(b('b6') <= 2126.0) ? " + 
"-0.04745161731884307" + 
":  " + 
"-0.0004288708983306632" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 2662.5) ? " + 
"(b('b6') <= 2660.5) ? " + 
"(b('b6') <= 2561.5) ? " + 
"-0.0005760549413608282" + 
":  " + 
"0.006864431511472226" + 
":  " + 
"(b('ndvi') <= 2221.0) ? " + 
"0.022748904701407766" + 
":  " + 
"0.10594116019359809" + 
":  " + 
"(b('ndvi') <= 3538.5) ? " + 
"(b('b4') <= 738.5) ? " + 
"0.022932655595197138" + 
":  " + 
"-0.00020163113974722732" + 
":  " + 
"(b('b3') <= 756.0) ? " + 
"-0.03154879765104125" + 
":  " + 
"-0.0027004229460249373" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 630.5) ? " + 
"(b('b5') <= 2594.5) ? " + 
"(b('b5') <= 1746.0) ? " + 
"0.0024360442943479983" + 
":  " + 
"-0.010429095709532427" + 
":  " + 
"(b('b3') <= 627.5) ? " + 
"0.011170781428750639" + 
":  " + 
"-0.024655218048554486" + 
":  " + 
"(b('b3') <= 644.5) ? " + 
"(b('crop') <= 48.16310119628906) ? " + 
"0.02667380318986388" + 
":  " + 
"-0.015762000413575325" + 
":  " + 
"(b('b3') <= 665.5) ? " + 
"-0.007510337468683377" + 
":  " + 
"0.0001822721690146605" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b4') <= 853.5) ? " + 
"(b('grass') <= 74.05612182617188) ? " + 
"(b('b2') <= 448.5) ? " + 
"-0.0011341360598088122" + 
":  " + 
"0.004431456575759921" + 
":  " + 
"(b('ndvi') <= 1721.5) ? " + 
"0.08254618925997684" + 
":  " + 
"0.010656567495297932" + 
":  " + 
"(b('b2') <= 368.0) ? " + 
"(b('b6') <= 2250.0) ? " + 
"0.01579797711949295" + 
":  " + 
"0.0719485969002076" + 
":  " + 
"(b('b4') <= 860.5) ? " + 
"-0.022621089064136592" + 
":  " + 
"-0.00033358559563946664" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -15.087481021881104) ? " + 
"(b('lia') <= 34.31712341308594) ? " + 
"(b('ndvi') <= 1251.0) ? " + 
"0.012415792782919205" + 
":  " + 
"-0.010178782105241015" + 
":  " + 
"(b('lia') <= 38.07935333251953) ? " + 
"0.005768706464847429" + 
":  " + 
"-0.0030076727685810767" + 
":  " + 
"(b('g0vv') <= -15.02292776107788) ? " + 
"(b('ndvi') <= 1392.0) ? " + 
"-0.02954208763748113" + 
":  " + 
"0.02996057470551725" + 
":  " + 
"(b('grass') <= 90.44964218139648) ? " + 
"-1.9815003671159313e-05" + 
":  " + 
"0.0056083979925845235" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 2518.5) ? " + 
"(b('b11') <= 3114.0) ? " + 
"(b('b7') <= 3087.5) ? " + 
"0.0008848605116088322" + 
":  " + 
"0.05152092702925096" + 
":  " + 
"(b('b2') <= 884.0) ? " + 
"-0.0284566660412166" + 
":  " + 
"0.024529083345880567" + 
":  " + 
"(b('b5') <= 2592.5) ? " + 
"(b('ndvi') <= 3619.5) ? " + 
"-0.0073471822600793555" + 
":  " + 
"0.023679849148284953" + 
":  " + 
"(b('grass') <= 35.55763244628906) ? " + 
"-0.0010530359902125907" + 
":  " + 
"0.0030209532190336114" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 38.08793258666992) ? " + 
"(b('lia') <= 38.01721382141113) ? " + 
"(b('lia') <= 37.84523963928223) ? " + 
"-0.0005842984330912155" + 
":  " + 
"0.013150003594160449" + 
":  " + 
"(b('b2') <= 445.5) ? " + 
"0.0030587333328329627" + 
":  " + 
"-0.03495704693686931" + 
":  " + 
"(b('lia') <= 38.138084411621094) ? " + 
"(b('g0vv') <= -15.28798246383667) ? " + 
"-0.02616764666560254" + 
":  " + 
"0.044457127823674475" + 
":  " + 
"(b('b6') <= 2619.5) ? " + 
"0.00267698565081205" + 
":  " + 
"-0.000498170162575768" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.218039989471436) ? " + 
"(b('g0vv') <= -14.247675895690918) ? " + 
"(b('l8dt') <= 275265.5) ? " + 
"0.002450060605446732" + 
":  " + 
"-0.0030534986547911857" + 
":  " + 
"(b('b2') <= 993.5) ? " + 
"-0.017682638498905084" + 
":  " + 
"-0.0991113243095765" + 
":  " + 
"(b('g0vv') <= -14.217326641082764) ? " + 
"0.15157930941429668" + 
":  " + 
"(b('g0vv') <= -14.198684692382812) ? " + 
"0.021104511431140893" + 
":  " + 
"0.0002182220032246831" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 665.5) ? " + 
"(b('b2') <= 314.5) ? " + 
"(b('b5') <= 3261.5) ? " + 
"0.003085004954818504" + 
":  " + 
"0.09711786915457532" + 
":  " + 
"(b('ndvi') <= 3553.0) ? " + 
"-0.00046148335913107075" + 
":  " + 
"-0.01319271589880438" + 
":  " + 
"(b('b4') <= 757.5) ? " + 
"(b('grass') <= 46.59696388244629) ? " + 
"0.00018560847107786997" + 
":  " + 
"0.0238882870859894" + 
":  " + 
"(b('b3') <= 669.0) ? " + 
"0.03148595907911412" + 
":  " + 
"-0.00023172880124834927" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b6') <= 879.0) ? " + 
"(b('g0vh') <= -16.77571153640747) ? " + 
"(b('g0vv') <= -12.98040246963501) ? " + 
"-0.012754755153671263" + 
":  " + 
"-0.02322485404818763" + 
":  " + 
"-0.04499838952223524" + 
":  " + 
"(b('b5') <= 2003.5) ? " + 
"(b('b3') <= 966.5) ? " + 
"0.0004896927370102953" + 
":  " + 
"0.014972818924799462" + 
":  " + 
"(b('b5') <= 2006.5) ? " + 
"-0.06384384363556941" + 
":  " + 
"-0.00013240665209129197" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('moss') <= 0.4290978014469147) ? " + 
"(b('trees') <= 6.157119512557983) ? " + 
"-0.0035445333509058095" + 
":  " + 
"-0.02799215544826349" + 
":  " + 
"(b('b3') <= 726.5) ? " + 
"0.0004527948263151188" + 
":  " + 
"-0.036078139639830926" + 
":  " + 
"(b('b4') <= 853.5) ? " + 
"(b('grass') <= 73.06093978881836) ? " + 
"0.0026510180595334595" + 
":  " + 
"0.019668494037599488" + 
":  " + 
"(b('b11') <= 1713.0) ? " + 
"-0.004238725225452525" + 
":  " + 
"0.00026225162788463406" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('bare') <= 72.05937194824219) ? " + 
"(b('ndvi') <= 1182.5) ? " + 
"(b('ndvi') <= 1179.5) ? " + 
"-0.002073043631666176" + 
":  " + 
"-0.08420522602675279" + 
":  " + 
"(b('bare') <= 29.32122039794922) ? " + 
"0.00015833794802769783" + 
":  " + 
"0.03131148045850937" + 
":  " + 
"(b('b4') <= 2104.5) ? " + 
"(b('g0vh') <= -21.358267784118652) ? " + 
"0.03889970409297952" + 
":  " + 
"0.021511856960984475" + 
":  " + 
"(b('g0vh') <= -22.675891876220703) ? " + 
"0.022375862889728395" + 
":  " + 
"0.004019466496269217" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 50860.5) ? " + 
"(b('bare') <= 2.9720497131347656) ? " + 
"(b('l8dt') <= 23123.0) ? " + 
"0.000858311792542948" + 
":  " + 
"-0.013822607557994315" + 
":  " + 
"(b('b3') <= 806.5) ? " + 
"0.019403443131912043" + 
":  " + 
"0.0006165601812518806" + 
":  " + 
"(b('l8dt') <= 70691.0) ? " + 
"(b('grass') <= 46.57049369812012) ? " + 
"0.003301609840246638" + 
":  " + 
"0.023319839647849908" + 
":  " + 
"(b('l8dt') <= 121900.5) ? " + 
"-0.004927734870774381" + 
":  " + 
"6.994864817873181e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -14.32249927520752) ? " + 
"(b('moss') <= 12.811606407165527) ? " + 
"(b('moss') <= 7.169239282608032) ? " + 
"-0.002206775410694184" + 
":  " + 
"0.008123872360330985" + 
":  " + 
"(b('ndvi') <= 866.0) ? " + 
"0.027110721743809612" + 
":  " + 
"-0.006752388886755087" + 
":  " + 
"(b('lia') <= 38.29970741271973) ? " + 
"(b('lia') <= 38.26570129394531) ? " + 
"-0.0005767688268838414" + 
":  " + 
"-0.03406116781119415" + 
":  " + 
"(b('lia') <= 38.37252616882324) ? " + 
"0.025989377539013262" + 
":  " + 
"0.0007858402790594798" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 318.5) ? " + 
"(b('b6') <= 2601.0) ? " + 
"(b('b3') <= 1016.5) ? " + 
"-6.958610082710847e-05" + 
":  " + 
"0.06946253168262351" + 
":  " + 
"(b('b7') <= 1442.5) ? " + 
"-0.033267418359435814" + 
":  " + 
"-0.005642551881143638" + 
":  " + 
"(b('b1') <= 336.5) ? " + 
"(b('b2') <= 448.0) ? " + 
"-0.0010962776446906519" + 
":  " + 
"0.029338705569554053" + 
":  " + 
"(b('b1') <= 338.5) ? " + 
"-0.04111769142669284" + 
":  " + 
"-1.9762635921740398e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3533.0) ? " + 
"(b('g0vh') <= -15.956182956695557) ? " + 
"(b('urban') <= 29.42727279663086) ? " + 
"0.00011560204209188661" + 
":  " + 
"-0.006157436847669238" + 
":  " + 
"(b('urban') <= 29.42727279663086) ? " + 
"0.001406147383247197" + 
":  " + 
"0.015161060589164258" + 
":  " + 
"(b('g0vh') <= -16.031259536743164) ? " + 
"(b('g0vh') <= -16.036385536193848) ? " + 
"-0.00019090270210516113" + 
":  " + 
"0.14825211452667095" + 
":  " + 
"(b('g0vh') <= -14.797223091125488) ? " + 
"-0.01765723991163629" + 
":  " + 
"0.0011311181489550247" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vh') <= -11.432883739471436) ? " + 
"(b('g0vv') <= -8.018159866333008) ? " + 
"(b('g0vh') <= -13.123357772827148) ? " + 
"-9.162066804372985e-05" + 
":  " + 
"-0.02610327583192179" + 
":  " + 
"(b('l8dt') <= 63284.0) ? " + 
"-0.028674612378198218" + 
":  " + 
"0.0031705824591638588" + 
":  " + 
"(b('l8dt') <= 1123644.5) ? " + 
"(b('b3') <= 825.0) ? " + 
"-0.01905926307952034" + 
":  " + 
"-0.056948702222437066" + 
":  " + 
"(b('b6') <= 3192.5) ? " + 
"-0.012041560445028465" + 
":  " + 
"0.023737195137029224" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 5293547.5) ? " + 
"(b('l8dt') <= 1260122.5) ? " + 
"(b('l8dt') <= 1187961.0) ? " + 
"6.360948095905467e-05" + 
":  " + 
"0.01163951460897688" + 
":  " + 
"(b('trees') <= 12.64185619354248) ? " + 
"-0.00013868154337861764" + 
":  " + 
"-0.010300424615399114" + 
":  " + 
"(b('g0vv') <= -11.658533573150635) ? " + 
"(b('b10') <= 1298.0) ? " + 
"0.09610802690590656" + 
":  " + 
"0.01720284051423693" + 
":  " + 
"(b('b1') <= 539.5) ? " + 
"0.00960634044029463" + 
":  " + 
"-0.009342296117447864" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 29.965818405151367) ? " + 
"(b('lia') <= 29.95256233215332) ? " + 
"(b('g0vv') <= -5.97988748550415) ? " + 
"-0.0008383589250192257" + 
":  " + 
"-0.031775854333719024" + 
":  " + 
"(b('l8dt') <= 2592014.0) ? " + 
"-0.041499384952113326" + 
":  " + 
"0.07407472550842772" + 
":  " + 
"(b('lia') <= 30.273048400878906) ? " + 
"(b('ndvi') <= 3284.5) ? " + 
"0.02456480773311766" + 
":  " + 
"-0.0036206164893137645" + 
":  " + 
"(b('lia') <= 31.2601261138916) ? " + 
"-0.005515219332494183" + 
":  " + 
"0.00011794286587003015" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 607.5) ? " + 
"(b('b5') <= 3092.5) ? " + 
"(b('b11') <= 2099.0) ? " + 
"-0.0029580735168395615" + 
":  " + 
"0.04630871684241228" + 
":  " + 
"(b('g0vh') <= -17.36738395690918) ? " + 
"-0.09618401519122466" + 
":  " + 
"-0.09255660351528075" + 
":  " + 
"(b('b10') <= 997.0) ? " + 
"(b('b10') <= 972.5) ? " + 
"0.0007526857266315923" + 
":  " + 
"0.03622677431638343" + 
":  " + 
"(b('b6') <= 1367.0) ? " + 
"-0.062105697277621615" + 
":  " + 
"6.896726495271678e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b7') <= 3244.5) ? " + 
"(b('b11') <= 3204.5) ? " + 
"(b('b4') <= 1830.5) ? " + 
"0.0002950826360873199" + 
":  " + 
"-0.0020938219001268086" + 
":  " + 
"(b('b5') <= 3146.0) ? " + 
"-0.021440463073822753" + 
":  " + 
"0.008220945004597883" + 
":  " + 
"(b('b3') <= 1271.5) ? " + 
"(b('b5') <= 2886.5) ? " + 
"-0.03383304674935458" + 
":  " + 
"0.019426341182564408" + 
":  " + 
"(b('b5') <= 2877.0) ? " + 
"0.020802818943434807" + 
":  " + 
"0.0011985901004102648" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1708.5) ? " + 
"(b('bare') <= 20.924105644226074) ? " + 
"(b('bare') <= 12.624931335449219) ? " + 
"-0.00023012380630083008" + 
":  " + 
"0.004708333796268424" + 
":  " + 
"(b('moss') <= 12.933144569396973) ? " + 
"-0.013895859250287837" + 
":  " + 
"0.0024980512179755697" + 
":  " + 
"(b('b4') <= 2051.0) ? " + 
"(b('g0vh') <= -18.069981575012207) ? " + 
"0.016207314526618374" + 
":  " + 
"0.08520329712479832" + 
":  " + 
"(b('l8dt') <= 1344163.0) ? " + 
"0.002601681556396219" + 
":  " + 
"-0.010882439512025699" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 28.15742301940918) ? " + 
"(b('g0vh') <= -13.760127544403076) ? " + 
"(b('g0vv') <= -12.24680471420288) ? " + 
"0.000955805803616064" + 
":  " + 
"-0.01160962478339413" + 
":  " + 
"(b('b3') <= 1234.0) ? " + 
"0.055070426057950705" + 
":  " + 
"0.07767230680816772" + 
":  " + 
"(b('lia') <= 28.160892486572266) ? " + 
"(b('b5') <= 3063.5) ? " + 
"0.030681909668496626" + 
":  " + 
"0.07868146556632777" + 
":  " + 
"(b('lia') <= 28.39741325378418) ? " + 
"0.009536141942174456" + 
":  " + 
"1.7712733536836496e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 85.84851455688477) ? " + 
"(b('crop') <= 85.4493522644043) ? " + 
"(b('crop') <= 79.23170852661133) ? " + 
"-0.00024520459065977083" + 
":  " + 
"0.003371038855276421" + 
":  " + 
"(b('b5') <= 2739.0) ? " + 
"0.010226092163366713" + 
":  " + 
"-0.019651023420795333" + 
":  " + 
"(b('crop') <= 87.44597244262695) ? " + 
"(b('b5') <= 2909.5) ? " + 
"0.04789533457480434" + 
":  " + 
"0.01203329589217196" + 
":  " + 
"(b('ndvi') <= 3652.0) ? " + 
"0.0032219152831307264" + 
":  " + 
"-0.009466149030932186" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 44.96173286437988) ? " + 
"(b('lia') <= 44.9576416015625) ? " + 
"(b('b3') <= 937.5) ? " + 
"-0.0006532621443958342" + 
":  " + 
"0.0005057318153938934" + 
":  " + 
"(b('g0vv') <= -14.031932830810547) ? " + 
"-0.0198825418931188" + 
":  " + 
"-0.045548306374035605" + 
":  " + 
"0.06062468658890824" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('trees') <= 8.639616012573242) ? " + 
"(b('b1') <= 449.5) ? " + 
"(b('b2') <= 435.5) ? " + 
"0.001868881579933995" + 
":  " + 
"-0.005541843462248546" + 
":  " + 
"(b('b4') <= 1147.5) ? " + 
"0.007636841875417013" + 
":  " + 
"-0.000699030541170366" + 
":  " + 
"(b('crop') <= 2.4269771575927734) ? " + 
"(b('b2') <= 1017.5) ? " + 
"-0.005032364115959" + 
":  " + 
"0.021912153013726354" + 
":  " + 
"(b('grass') <= 45.792701721191406) ? " + 
"0.0005338283747119274" + 
":  " + 
"0.013403559172409126" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b2') <= 382.25) ? " + 
"(b('g0vh') <= -17.33863353729248) ? " + 
"(b('lia') <= 30.982579231262207) ? " + 
"-0.019847116512863465" + 
":  " + 
"-0.004606023811635202" + 
":  " + 
"(b('b10') <= 1399.0) ? " + 
"0.006066415067110753" + 
":  " + 
"-0.016874412965323677" + 
":  " + 
"(b('b2') <= 388.5) ? " + 
"(b('moss') <= 13.451612949371338) ? " + 
"0.011847026205931208" + 
":  " + 
"-0.03826956239245775" + 
":  " + 
"(b('b2') <= 389.5) ? " + 
"-0.024675229332293158" + 
":  " + 
"0.00010676977275957491" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b1') <= 318.5) ? " + 
"(b('b4') <= 1030.5) ? " + 
"(b('b4') <= 974.0) ? " + 
"-0.0011007389390526787" + 
":  " + 
"0.020492030173978444" + 
":  " + 
"(b('ndvi') <= 4800.5) ? " + 
"-0.021066608461970594" + 
":  " + 
"0.08847488655635523" + 
":  " + 
"(b('b1') <= 362.5) ? " + 
"(b('crop') <= 39.25741386413574) ? " + 
"0.01709845237271458" + 
":  " + 
"-0.000370887793939531" + 
":  " + 
"(b('b1') <= 383.5) ? " + 
"-0.006671887478540872" + 
":  " + 
"0.0001459061838807988" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('g0vv') <= -13.90178108215332) ? " + 
"(b('crop') <= 87.21756744384766) ? " + 
"(b('g0vh') <= -18.09006404876709) ? " + 
"-0.0013186339446131874" + 
":  " + 
"-0.0273699168624141" + 
":  " + 
"(b('b5') <= 2537.0) ? " + 
"0.05149834173974428" + 
":  " + 
"0.006992837179864628" + 
":  " + 
"(b('trees') <= 8.639616012573242) ? " + 
"(b('bare') <= 1.7923067808151245) ? " + 
"-0.00197483325898832" + 
":  " + 
"0.001541268867045116" + 
":  " + 
"(b('urban') <= 14.72341012954712) ? " + 
"0.0015341030913184847" + 
":  " + 
"0.024859471316594803" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2695.5) ? " + 
"(b('ndvi') <= 2694.0) ? " + 
"(b('ndvi') <= 2626.5) ? " + 
"0.0001418759730937114" + 
":  " + 
"0.009175567892353593" + 
":  " + 
"(b('g0vv') <= -12.222703456878662) ? " + 
"0.004129861894013993" + 
":  " + 
"0.0792583675738438" + 
":  " + 
"(b('ndvi') <= 2700.0) ? " + 
"(b('g0vv') <= -9.96617603302002) ? " + 
"-0.03818350601283195" + 
":  " + 
"-0.07946289049388866" + 
":  " + 
"(b('grass') <= 77.6886215209961) ? " + 
"-0.0012658756921757343" + 
":  " + 
"0.008528316019001923" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 43.82534217834473) ? " + 
"(b('lia') <= 43.81620216369629) ? " + 
"(b('lia') <= 43.7987174987793) ? " + 
"-0.00014725253007473102" + 
":  " + 
"0.01921473152256839" + 
":  " + 
"(b('ndvi') <= 1952.0) ? " + 
"-0.03790926208205458" + 
":  " + 
"0.004438603668181018" + 
":  " + 
"(b('b3') <= 838.0) ? " + 
"(b('g0vv') <= -11.042319774627686) ? " + 
"-0.007326764572328333" + 
":  " + 
"0.010377888664266647" + 
":  " + 
"(b('ndvi') <= 2056.5) ? " + 
"-0.0016608856256933693" + 
":  " + 
"0.012845898907125713" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('crop') <= 85.84851455688477) ? " + 
"(b('crop') <= 85.4493522644043) ? " + 
"(b('l8dt') <= 8416202.5) ? " + 
"-3.3082767843065754e-05" + 
":  " + 
"0.031042288123880164" + 
":  " + 
"(b('g0vv') <= -10.001349925994873) ? " + 
"-0.015466868010349369" + 
":  " + 
"0.027750919724722604" + 
":  " + 
"(b('grass') <= 9.401607036590576) ? " + 
"(b('g0vh') <= -19.644466400146484) ? " + 
"0.007507609261606487" + 
":  " + 
"-0.0024759671297620977" + 
":  " + 
"(b('b3') <= 1435.5) ? " + 
"0.026836840040074365" + 
":  " + 
"-0.08794972290798109" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 28.096532821655273) ? " + 
"(b('b5') <= 1951.0) ? " + 
"(b('b10') <= 1198.0) ? " + 
"-0.031051714081696075" + 
":  " + 
"0.040120153960152546" + 
":  " + 
"(b('l8dt') <= 212778.0) ? " + 
"-0.013081058631972474" + 
":  " + 
"-0.0010532867946129421" + 
":  " + 
"(b('lia') <= 28.09913158416748) ? " + 
"(b('b4') <= 1387.0) ? " + 
"0.07543980884630286" + 
":  " + 
"0.006232412333213089" + 
":  " + 
"(b('lia') <= 28.09951877593994) ? " + 
"-0.08431454355538659" + 
":  " + 
"7.532128584688793e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 973517.0) ? " + 
"(b('l8dt') <= 970876.5) ? " + 
"(b('b6') <= 2217.5) ? " + 
"0.00472570379016289" + 
":  " + 
"-0.0003008672447757689" + 
":  " + 
"(b('g0vh') <= -21.354448318481445) ? " + 
"0.09744623434651264" + 
":  " + 
"0.021182317743400257" + 
":  " + 
"(b('trees') <= 12.64185619354248) ? " + 
"(b('trees') <= 10.893646240234375) ? " + 
"-0.0006993874435277111" + 
":  " + 
"0.011741378237289893" + 
":  " + 
"(b('b2') <= 1005.5) ? " + 
"-0.008794437221307403" + 
":  " + 
"0.16460784685149682" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 3385997.0) ? " + 
"(b('l8dt') <= 1618442.0) ? " + 
"(b('crop') <= 79.23170852661133) ? " + 
"-0.00032707336981721986" + 
":  " + 
"0.0027765861778402848" + 
":  " + 
"(b('crop') <= 89.04487609863281) ? " + 
"-0.00043907673302015623" + 
":  " + 
"-0.01359998746976551" + 
":  " + 
"(b('b6') <= 2252.5) ? " + 
"(b('ndvi') <= 1814.5) ? " + 
"0.020636966342563234" + 
":  " + 
"-0.01399568403459727" + 
":  " + 
"(b('b6') <= 2606.5) ? " + 
"0.013227892496761227" + 
":  " + 
"0.0014248181200125403" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 937.5) ? " + 
"(b('b4') <= 987.5) ? " + 
"(b('b4') <= 975.0) ? " + 
"0.00010656175526577615" + 
":  " + 
"0.022710890229021893" + 
":  " + 
"(b('grass') <= 76.29081726074219) ? " + 
"-0.0009650277085243316" + 
":  " + 
"-0.015557417220453295" + 
":  " + 
"(b('b3') <= 945.5) ? " + 
"(b('b6') <= 2631.5) ? " + 
"0.041760541774238026" + 
":  " + 
"0.00010626381038496186" + 
":  " + 
"(b('b5') <= 1793.5) ? " + 
"-0.03348600977860263" + 
":  " + 
"0.00022270499665596156" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('urban') <= 0.9776536226272583) ? " + 
"(b('b4') <= 1439.75) ? " + 
"(b('b3') <= 1004.5) ? " + 
"-5.050669034889432e-05" + 
":  " + 
"0.005831720543920159" + 
":  " + 
"(b('b11') <= 1919.5) ? " + 
"0.014527085796893947" + 
":  " + 
"-0.0011363132276724617" + 
":  " + 
"(b('b4') <= 715.5) ? " + 
"(b('b6') <= 2091.5) ? " + 
"-0.004351708953010833" + 
":  " + 
"0.010249592549340096" + 
":  " + 
"(b('b4') <= 717.5) ? " + 
"-0.03906147554140021" + 
":  " + 
"-0.0019802609568184194" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1470.5) ? " + 
"(b('b5') <= 3381.5) ? " + 
"(b('b4') <= 1677.5) ? " + 
"0.0007011517638948624" + 
":  " + 
"-0.0027729385817472727" + 
":  " + 
"(b('grass') <= 65.31989097595215) ? " + 
"-0.004181094565609653" + 
":  " + 
"0.03187468880944333" + 
":  " + 
"(b('b4') <= 1806.5) ? " + 
"(b('crop') <= 88.4096565246582) ? " + 
"0.018483892470260846" + 
":  " + 
"0.09984773713626487" + 
":  " + 
"(b('b1') <= 706.5) ? " + 
"0.007295175476400916" + 
":  " + 
"-0.0007331356505245598" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 727.5) ? " + 
"(b('b3') <= 726.5) ? " + 
"(b('moss') <= 0.4290978014469147) ? " + 
"-0.00835477710059519" + 
":  " + 
"0.0002199882087412491" + 
":  " + 
"(b('ndvi') <= 4904.5) ? " + 
"-0.041265392792916335" + 
":  " + 
"0.1090795306736371" + 
":  " + 
"(b('b3') <= 743.5) ? " + 
"(b('g0vh') <= -20.61678409576416) ? " + 
"-0.017541739024978954" + 
":  " + 
"0.016130900400885214" + 
":  " + 
"(b('b3') <= 745.5) ? " + 
"-0.03196664011976149" + 
":  " + 
"0.00013312943463456156" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('moss') <= 19.819469451904297) ? " + 
"(b('moss') <= 19.694199562072754) ? " + 
"(b('moss') <= 19.47174644470215) ? " + 
"5.558241603952746e-05" + 
":  " + 
"-0.018056449832077767" + 
":  " + 
"(b('lia') <= 34.84456443786621) ? " + 
"0.006975571079356187" + 
":  " + 
"0.04475491124911269" + 
":  " + 
"(b('grass') <= 67.60882186889648) ? " + 
"(b('b11') <= 2194.5) ? " + 
"0.01710504110859975" + 
":  " + 
"-0.003993892030790205" + 
":  " + 
"(b('b2') <= 492.5) ? " + 
"-0.06138207023249185" + 
":  " + 
"-0.01306460744171182" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('ndvi') <= 2738.0) ? " + 
"(b('moss') <= 27.690022468566895) ? " + 
"(b('trees') <= 11.430836200714111) ? " + 
"-9.419152648758655e-06" + 
":  " + 
"0.004519791688162406" + 
":  " + 
"(b('ndvi') <= 2432.5) ? " + 
"-0.03668312301952676" + 
":  " + 
"-0.00692211315924697" + 
":  " + 
"(b('g0vv') <= -15.678635120391846) ? " + 
"(b('trees') <= 6.102396249771118) ? " + 
"-0.0008869980658929765" + 
":  " + 
"-0.022761942562815402" + 
":  " + 
"(b('grass') <= 77.6886215209961) ? " + 
"-0.0009618544531694517" + 
":  " + 
"0.010712772427782168" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b3') <= 1708.5) ? " + 
"(b('b4') <= 2018.5) ? " + 
"(b('b3') <= 1508.0) ? " + 
"-0.00017842373903961944" + 
":  " + 
"0.010925343280870805" + 
":  " + 
"(b('b5') <= 3331.5) ? " + 
"-0.007865508968362732" + 
":  " + 
"0.0032475172729092296" + 
":  " + 
"(b('b4') <= 2051.0) ? " + 
"(b('g0vh') <= -18.069981575012207) ? " + 
"0.014547830845921735" + 
":  " + 
"0.07750007750030587" + 
":  " + 
"(b('ndvi') <= 3571.5) ? " + 
"0.0010423850972152448" + 
":  " + 
"0.029735092963570485" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 29.97120475769043) ? " + 
"(b('b1') <= 438.5) ? " + 
"(b('b1') <= 430.5) ? " + 
"-0.004622522244884004" + 
":  " + 
"-0.03731369511562461" + 
":  " + 
"(b('b10') <= 1558.5) ? " + 
"0.12348083508751145" + 
":  " + 
"0.0006114960464291679" + 
":  " + 
"(b('lia') <= 30.273048400878906) ? " + 
"(b('ndvi') <= 3284.5) ? " + 
"0.02233402421441067" + 
":  " + 
"-0.003028062032396222" + 
":  " + 
"(b('grass') <= 83.16818618774414) ? " + 
"0.00021366648755131917" + 
":  " + 
"-0.003287064248514227" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b11') <= 3244.5) ? " + 
"(b('b6') <= 3892.5) ? " + 
"(b('b6') <= 3888.5) ? " + 
"6.591522677616834e-05" + 
":  " + 
"0.02518985113681955" + 
":  " + 
"(b('l8dt') <= 2355184.5) ? " + 
"-0.00501605273965327" + 
":  " + 
"0.025156277808002364" + 
":  " + 
"(b('b4') <= 1790.25) ? " + 
"(b('g0vh') <= -19.36262035369873) ? " + 
"-0.02095142040429326" + 
":  " + 
"0.019545981817733156" + 
":  " + 
"(b('b5') <= 2639.5) ? " + 
"0.04724777058712258" + 
":  " + 
"0.002265913006171979" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('l8dt') <= 568285.5) ? " + 
"(b('l8dt') <= 489297.0) ? " + 
"(b('moss') <= 4.141507387161255) ? " + 
"0.0022965540154849663" + 
":  " + 
"-0.0011078951285842748" + 
":  " + 
"(b('l8dt') <= 538841.5) ? " + 
"0.012276953587877783" + 
":  " + 
"0.0002140899781320572" + 
":  " + 
"(b('g0vv') <= -12.296576499938965) ? " + 
"(b('b11') <= 2026.0) ? " + 
"-0.005913120782655984" + 
":  " + 
"-6.534596887484957e-06" + 
":  " + 
"(b('grass') <= 76.45126724243164) ? " + 
"2.6293458735200017e-05" + 
":  " + 
"0.017700895278763413" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('b5') <= 3551.5) ? " + 
"(b('b5') <= 3550.5) ? " + 
"(b('g0vv') <= -11.434404850006104) ? " + 
"-0.0004937669352240565" + 
":  " + 
"0.0011973493898061072" + 
":  " + 
"(b('l8dt') <= 1621087.5) ? " + 
"0.12142876938553193" + 
":  " + 
"0.06889829466421088" + 
":  " + 
"(b('grass') <= 49.40912055969238) ? " + 
"(b('b5') <= 3585.0) ? " + 
"-0.014769410262159147" + 
":  " + 
"-0.0013083216448346968" + 
":  " + 
"(b('l8dt') <= 36783.5) ? " + 
"0.08668264006572746" + 
":  " + 
"0.010251550431735335" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 28.15742301940918) ? " + 
"(b('ndvi') <= 914.5) ? " + 
"(b('b1') <= 1088.0) ? " + 
"-0.033652104876910095" + 
":  " + 
"-0.07459709129082295" + 
":  " + 
"(b('g0vh') <= -17.50337505340576) ? " + 
"-0.004931742391464413" + 
":  " + 
"0.011601054986093744" + 
":  " + 
"(b('lia') <= 28.160892486572266) ? " + 
"(b('b5') <= 3063.5) ? " + 
"0.028320412538482498" + 
":  " + 
"0.06959478445827569" + 
":  " + 
"(b('lia') <= 28.39741325378418) ? " + 
"0.008528834557778604" + 
":  " + 
"2.104851754718389e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  tree_prediction = ee.Image(0) 
  tree_weight = ee.Image(1) 
  tree_prediction = tree_prediction.where(feature_stack.mask().reduce(ee.Reducer.allNonZero()).eq(1), feature_stack.expression(
"(b('lia') <= 26.05080795288086) ? " + 
"(b('g0vh') <= -20.765707969665527) ? " + 
"(b('lia') <= 26.036118507385254) ? " + 
"0.0003878963756680313" + 
":  " + 
"0.05838591162578226" + 
":  " + 
"(b('g0vv') <= -13.272767543792725) ? " + 
"0.02584672079821898" + 
":  " + 
"0.07003065709264104" + 
":  " + 
"(b('lia') <= 27.173502922058105) ? " + 
"(b('g0vv') <= -9.914340496063232) ? " + 
"-0.00873565342956939" + 
":  " + 
"-0.06792468983581292" + 
":  " + 
"(b('lia') <= 27.17487907409668) ? " + 
"0.08410208717109867" + 
":  " + 
"2.350707990650351e-05" + 
""))
  prediction = prediction.add(learning_rate.multiply(tree_prediction)) 
  return prediction