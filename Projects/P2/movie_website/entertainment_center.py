import media
import fresh_tomatoes

gong_shou_dao = media.Movie("功守道","人民币玩家大战屌丝","http://g3.ykimg.com/051600005A07EC22ADBC092D8C0A7FB4","http://v.youku.com/v_show/id_XMzE0ODM1ODg1Ng==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
Rampage_of_the_beast = media.Movie("狂兽","重案督察西狗（张晋 饰）与搭档阿德（吴樾 饰）到某渔村追捕涉嫌多桩凶案的歹徒江贵成，却意外发现大量被虐杀的帮派分子尸体和数额惊人的黑市黄金，一场各怀鬼胎的混战因西狗和阿德的闯入变成了整个江湖针对两个警察的困兽之斗，随着调查的深入，西狗发现拥有超高犯罪才智的江贵成竟然嚣张到要借十号风球的天威，谋划跨国掠夺一批价...","http://r1.ykimg.com/0516000059E59912ADBC096FA504478C","http://v.youku.com/v_show/id_XMjYzNDcyMDY5Mg==.html?spm=a2h1n.8261147.0.0")
murder_of_the_orient_express = media.Movie("东方快车谋杀案","影片讲述大侦探在东方快车上巧破一桩谋杀奇案的故事。波洛乘上东方快车，夜间三次被吵醒，第二天清晨便发现同车的美国富商雷切尔被人谋杀，死者被戳了12刀。波洛根据他所观察到的各种可疑迹象以及同车人士的讯问，并结合美国实行的12人陪审团制度等情况进行逻辑推理，成功地揭开了一起“集体复仇”奇案。","http://r1.ykimg.com/0516000059FFD7E2ADBA1F049F08BC08","http://v.youku.com/v_show/id_XMjc5OTI0MDY2NA==.html?spm=a2h1n.8261147.0.0")
the_chinese_window = media.Movie("烽火芳菲","影片通过中国军民用自己的生命救助美国飞行员的过程，再现了烽火岁月下人性真善美的故事。","http://r1.ykimg.com/0516000059A7841FADBDD3031507A077","http://v.youku.com/v_show/id_XMjk5OTI3NzIwOA==.html?spm=a2h1n.8261147.0.0")
wolf_warriors_2 = media.Movie("战狼2","被开除军籍的冷锋（吴京 饰）本是因找寻龙小云（余男 饰）来到非洲，但是却突然被卷入一场非洲国家的叛乱。因为国家之间政治立场的关系，中国军队无法在非洲实行武装行动撤离华侨。而作为退伍老兵的冷锋无法忘记曾经为军人的使命，本来可以安全撤离的他毅然决然地回到了沦陷区，孤身一人带领身陷屠杀中的同胞和难民，展开生死逃亡。...","http://r1.ykimg.com/0516000059EEA362ADBA1FA27503A6DF","http://v.youku.com/v_show/id_XMzA4OTA4OTQyMA==.html?spm=a2hmv.20020200.search.5&from=y1.8-4.999")
pokeman = media.Movie("精灵宝可梦:波尔凯尼恩与机巧的玛吉安娜","小智一行人依旧在无尽的旅途中前行着。某日，一个巨大的宝可梦忽然从天而降，它的真身竟然是幻之宝可梦波尔凯尼恩！波尔凯尼恩生活在偏僻的尼贝尔高原之上，在那里生活着很多和它一样曾经遭到人类伤害而对人类失去信任的宝可梦们。而如今，波尔凯尼恩为何会出现在此地？它究竟想要做什么呢？","http://r1.ykimg.com/0516000059313487ADBAC346FC06AB07","http://v.youku.com/v_show/id_XMjc5NjE3NzM0NA==.html?spm=a2h1n.8261147.0.0")

movies = [gong_shou_dao, Rampage_of_the_beast,murder_of_the_orient_express,the_chinese_window,wolf_warriors_2,pokeman]

fresh_tomatoes.open_movies_page(movies)