# -*- coding:utf8 -*-
LINES = {
"1号线":["0111","0112","0113","0114","0115","0116","0117","0118","0119","0120","0121","0122","0123","0124","0125","0126","0127","0128","0129","0130","0131","0132","0133","0134","0135","0136","0137","0138"],
"2号线":["0234","0235","0236","0237","0238","0239","0240","0241","0242","0243","0244","0245","0246","0247","0248","0249","0250","0251","0252","0253","0254","0255","0256","0257","0258","0259","0260","0261","0262","0263"],
"3号线":["0311","0312","0313","0314","0315","0316","0317","0318","0319","0320","0321","0322","0323","0324","0325","0326","0327","0328","0329","0330","0331","0332","0333","0334","0335","0336","0337","0338","0339"],
"4号线":["0401","0402","0403","0404","0405","0406","0407","0408","0409","0410","0411","0412","0413","0414","0415","0416","0417","0418","0419","0420","0421","0422","0423","0424","0425","0426"],
"5号线":["0501","0502","0503","0505","0507","0508","0509","0510","0511","0512","0513"],
"6号线":["0621","0622","0623","0624","0625","0626","0627","0628","0629","0630","0631","0632","0633","0634","0635","0636","0637","0638","0639","0640","0641","0642","0643","0644","0645","0646","0647","0648"],
"7号线":["0721","0722","0723","0724","0725","0726","0727","0728","0729","0730","0731","0732","0733","0734","0735","0736","0737","0738","0739","0740","0741","0742","0743","0744","0745","0746","0747","0748","0749","0750","0751","0752","0753"],
"8号线":["0820","0821","0822","0823","0824","0825","0826","0827","0828","0829","0830","0831","0832","0833","0834","0835","0836","0837","0838","0839","0840","0841","0842","0843","0844","0845","0846","0847","0848","0849"],
"9号线":["0918","0919","0920","0921","0922","0923","0924","0925","0926","0927","0928","0929","0930","0931","0932","0933","0934","0935","0936","0937","0938","0939","0940","0941","0942","0943","0944","0945","0946","0947","0948","0949","0950","0951","0952"],
"10号线":["1018","1019","1020","1041","1042","1043","1044","1045","1046","1047","1048","1049","1050","1051","1052","1053","1054","1055","1056","1057","1058","1059","1060","1061","1062","1063","1064","1065","1066","1067","1068"],
"11号线":["1114","1115","1116","1117","1118","1119","1120","1131","1132","1133","1134","1135","1137","1138","1139","1140","1141","1142","1143","1144","1145","1146","1147","1148","1149","1150","1151","1152","1153","1154","1155","1156","1157","1158","1159","1160","1161","1162","1163"],
"12号线":["1220","1221","1222","1223","1224","1225","1226","1227","1228","1229","1230","1231","1232","1233","1234","1235","1236","1237","1238","1239","1240","1241","1242","1243","1244","1245","1246","1247","1248","1249","1250","1251"],
"13号线":["1321","1322","1323","1324","1325","1326","1327","1328","1329","1330","1331","1332","1333","1334","1335","1336","1337","1338","1339"],
"16号线":["1621","1622","1623","1624","1625","1626","1627","1628","1629","1630","1631","1632","1633"],
"17号线":["1721","1722","1723","1724","1725","1726","1727","1728","1729","1730","1731","1732","1733"]
}

STATIONS = {"0111":"莘庄","0112":"外环路","0113":"莲花路","0114":"锦江乐园","0115":"上海南站","0116":"漕宝路","0117":"上海体育馆","0118":"徐家汇","0119":"衡山路","0120":"常熟路","0121":"陕西南路","0122":"黄陂南路","0123":"人民广场","0124":"新闸路","0125":"汉中路","0126":"上海火车站","0127":"中山北路","0128":"延长路","0129":"上海马戏城","0130":"汶水路","0131":"彭浦新村","0132":"共康路","0133":"通河新村","0134":"呼兰路","0135":"共富新村","0136":"宝安公路","0137":"友谊西路","0138":"富锦路","0234":"徐泾东","0235":"虹桥火车站","0236":"虹桥2号航站楼","0237":"淞虹路","0238":"北新泾","0239":"威宁路","0240":"娄山关路","0241":"中山公园","0242":"江苏路","0243":"静安寺","0244":"南京西路","0245":"人民广场","0246":"南京东路","0247":"陆家嘴","0248":"东昌路","0249":"世纪大道","0250":"上海科技馆","0251":"世纪公园","0252":"龙阳路","0253":"张江高科","0254":"金科路","0255":"广兰路","0256":"唐镇","0257":"创新中路","0258":"华夏东路","0259":"川沙","0260":"凌空路","0261":"远东大道","0262":"海天三路","0263":"浦东国际机场","0311":"上海南站","0312":"石龙路","0313":"龙漕路","0314":"漕溪路","0315":"宜山路","0316":"虹桥路","0317":"延安西路","0318":"中山公园","0319":"金沙江路","0320":"曹杨路","0321":"镇坪路","0322":"中潭路","0323":"上海火车站","0324":"宝山路","0325":"东宝兴路","0326":"虹口足球场","0327":"赤峰路","0328":"大柏树","0329":"江湾镇","0330":"殷高西路","0331":"长江南路","0332":"淞发路","0333":"张华浜","0334":"淞滨路","0335":"水产路","0336":"宝杨路","0337":"友谊路","0338":"铁力路","0339":"江杨北路","0401":"上海体育馆","0402":"宜山路","0403":"虹桥路","0404":"延安西路","0405":"中山公园","0406":"金沙江路","0407":"曹杨路","0408":"镇坪路","0409":"中潭路","0410":"上海火车站","0411":"宝山路","0412":"海伦路","0413":"临平路","0414":"大连路","0415":"杨树浦路","0416":"浦东大道","0417":"世纪大道","0418":"浦电路","0419":"蓝村路","0420":"塘桥","0421":"南浦大桥","0422":"西藏南路","0423":"鲁班路","0424":"大木桥路","0425":"东安路","0426":"上海体育场","0501":"莘庄","0502":"春申路","0503":"银都路","0505":"颛桥","0507":"北桥","0508":"剑川路","0509":"东川路","0510":"金平路","0511":"华宁路","0512":"文井路","0513":"闵行开发区","0621":"东方体育中心","0622":"灵岩南路","0623":"上南路","0624":"华夏西路","0625":"高青路","0626":"东明路","0627":"高科西路","0628":"临沂新村","0629":"上海儿童医学中心","0630":"蓝村路","0631":"浦电路","0632":"世纪大道","0633":"源深体育中心","0634":"民生路","0635":"北洋泾路","0636":"德平路","0637":"云山路","0638":"金桥路","0639":"博兴路","0640":"五莲路","0641":"巨峰路","0642":"东靖路","0643":"五洲大道","0644":"洲海路","0645":"外高桥保税区南站","0646":"航津路","0647":"外高桥保税区北站","0648":"港城路",
"0721":"美兰湖","0722":"罗南新村","0723":"潘广路","0724":"刘行","0725":"顾村公园","0726":"祁华路","0727":"上海大学","0728":"南陈路","0729":"上大路","0730":"场中路","0731":"大场镇","0732":"行知路","0733":"大华三路","0734":"新村路","0735":"岚皋路","0736":"镇坪路","0737":"长寿路","0738":"昌平路","0739":"静安寺","0740":"常熟路","0741":"肇嘉浜路","0742":"东安路","0743":"龙华中路","0744":"后滩","0745":"长清路","0746":"耀华路","0747":"云台路","0748":"高科西路","0749":"杨高南路","0750":"锦绣路","0751":"芳华路","0752":"龙阳路","0753":"花木路","0820":"沈杜公路","0821":"联航路","0822":"江月路","0823":"浦江镇","0824":"芦恒路","0825":"凌兆新村","0826":"东方体育中心","0827":"杨思","0828":"成山路","0829":"耀华路","0830":"中华艺术宫","0831":"西藏南路","0832":"陆家浜路","0833":"老西门","0834":"大世界","0835":"人民广场","0836":"曲阜路","0837":"中兴路","0838":"西藏北路","0839":"虹口足球场","0840":"曲阳路","0841":"四平路","0842":"鞍山新村","0843":"江浦路","0844":"黄兴路","0845":"延吉中路","0846":"黄兴公园","0847":"翔殷路","0848":"嫩江路","0849":"市光路","0918":"松江南站","0919":"醉白池","0920":"松江体育中心","0921":"松江新城","0922":"松江大学城","0923":"洞泾","0924":"佘山","0925":"泗泾","0926":"九亭","0927":"中春路","0928":"七宝","0929":"星中路","0930":"合川路","0931":"漕河泾开发区","0932":"桂林路","0933":"宜山路","0934":"徐家汇","0935":"肇嘉浜路","0936":"嘉善路","0937":"打浦桥","0938":"马当路","0939":"陆家浜路","0940":"小南门","0941":"商城路","0942":"世纪大道","0943":"杨高中路","0944":"芳甸路","0945":"蓝天路","0946":"台儿庄路","0947":"金桥","0948":"金吉路","0949":"金海路","0950":"顾唐路","0951":"民雷路","0952":"曹路","1018":"航中路","1019":"紫藤路","1020":"龙柏新村","1041":"虹桥火车站","1042":"虹桥2号航站楼","1043":"虹桥1号航站楼","1044":"上海动物园","1045":"龙溪路","1046":"水城路","1047":"伊犁路","1048":"宋园路","1049":"虹桥路","1050":"交通大学","1051":"上海图书馆","1052":"陕西南路","1053":"新天地","1054":"老西门","1055":"豫园","1056":"南京东路","1057":"天潼路","1058":"四川北路","1059":"海伦路","1060":"邮电新村","1061":"四平路","1062":"同济大学","1063":"国权路","1064":"五角场","1065":"江湾体育场","1066":"三门路","1067":"殷高东路","1068":"新江湾城","1114":"花桥","1115":"光明路","1116":"兆丰路","1117":"安亭","1118":"上海汽车城","1119":"昌吉东路","1120":"上海赛车场","1131":"嘉定北","1132":"嘉定西","1133":"白银路","1134":"嘉定新城","1135":"马陆","1137":"南翔","1138":"桃浦新村","1139":"武威路","1140":"祁连山路","1141":"李子园","1142":"上海西站","1143":"真如","1144":"枫桥路","1145":"曹杨路","1146":"隆德路","1147":"江苏路","1148":"交通大学","1149":"徐家汇","1150":"上海游泳馆","1151":"龙华","1152":"云锦路","1153":"龙耀路","1154":"东方体育中心","1155":"三林","1156":"三林东","1157":"浦三路","1158":"（预留车站）","1159":"御桥","1160":"罗山路","1161":"秀沿路","1162":"康新公路","1163":"迪士尼","1220":"七莘路","1221":"虹莘路","1222":"顾戴路","1223":"东兰路","1224":"虹梅路","1225":"虹漕路","1226":"桂林公园","1227":"漕宝路","1228":"龙漕路","1229":"龙华","1230":"龙华中路","1231":"大木桥路","1232":"嘉善路","1233":"陕西南路","1234":"南京西路","1235":"汉中路","1236":"曲阜路","1237":"天潼路","1238":"国际客运中心","1239":"提篮桥","1240":"大连路","1241":"江浦公园","1242":"宁国路","1243":"隆昌路","1244":"爱国路","1245":"复兴岛","1246":"东陆路","1247":"巨峰路","1248":"杨高北路","1249":"金京路","1250":"申江路","1251":"金海路","1321":"金运路","1322":"金沙江西路","1323":"丰庄","1324":"祁连山南路","1325":"真北路","1326":"大渡河路","1327":"金沙江路","1328":"隆德路","1329":"武宁路","1330":"长寿路","1331":"江宁路","1332":"汉中路","1333":"自然博物馆","1334":"南京西路","1335":"淮海中路","1336":"新天地","1337":"马当路","1338":"世博会博物馆","1339":"世博大道","1621":"龙阳路","1622":"华夏中路","1623":"罗山路","1624":"周浦东","1625":"鹤沙航城","1626":"航头东","1627":"新场","1628":"野生动物园","1629":"惠南","1630":"惠南东","1631":"书院","1632":"临港大道","1633":"滴水湖","1721":"虹桥火车站","1722":"诸光路","1723":"蟠龙路","1724":"徐盈路","1725":"徐泾北城","1726":"嘉松中路","1727":"赵巷","1728":"汇金路","1729":"青浦新城","1730":"漕盈路","1731":"淀山湖大道","1732":"朱家角","1733":"东方绿舟"}