# -*- coding: utf-8 -*-
"""Thanh Hóa — batch E (records 19-24)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.normpath(os.path.join(HERE, "..", "data", "regions", "vn-thanh-hoa.json"))
REG, RNV, FD, TODAY = "vn-thanh-hoa", "Thanh Hóa", "Miền Trung", "2026-07-27"


def R(slug, nv, ne, nr, cats, lat, lon, addr, rval, rcount, review,
      psv, pse, psr, plv, ple, plr, hlv, hle, hlr, practical, tags, sources=None):
    return {
        "id": f"{REG}-{slug}", "slug": slug, "region": REG, "country": "vietnam",
        "region_name_vi": RNV, "federal_district": FD,
        "name_vi": nv, "name_ru": nr, "name_en": ne,
        "categories": cats, "coordinates": {"lat": lat, "lon": lon},
        "address_vi": addr,
        "rating": {"value": rval, "count": rcount, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": review,
        "presentation_short_vi": psv, "presentation_short_en": pse, "presentation_short_ru": psr,
        "presentation_long_vi": plv, "presentation_long_en": ple, "presentation_long_ru": plr,
        "highlights_vi": hlv, "highlights_en": hle, "highlights_ru": hlr,
        "practical": practical, "photo": None, "photo_credit": None,
        "official_site": None, "sources": sources or [],
        "tags": tags, "status": "enriched", "last_updated": TODAY,
    }


new = []

# 19) Vườn quốc gia Xuân Liên
new.append(R(
    "vqg-xuan-lien", "Vườn quốc gia Xuân Liên", "Xuan Lien National Park", "Национальный парк Суанльен",
    ["park_garden"], 19.9200, 105.1500,
    "Huyện Thường Xuân, tỉnh Thanh Hóa",
    4.5, 300,
    "Du khách yêu thích rừng nguyên sinh mát lành với những cây sa mu, pơ mu cổ thụ ngàn năm tuổi và thác nước hoang sơ. Nhiều người thích trekking, ngắm chim thú; một số nhắc cần đăng ký và có hướng dẫn viên.",
    "Vườn quốc gia Xuân Liên ở huyện Thường Xuân (nâng hạng năm 2025) bảo tồn vùng rừng thượng nguồn sông Chu với đa dạng sinh học cao. Nơi đây nổi tiếng có những cây sa mu, pơ mu cổ thụ hàng nghìn năm tuổi được xem như \"báu vật\" của rừng.",
    "Xuan Lien National Park in Thuong Xuan district (upgraded in 2025) protects the upper Chu River forests with high biodiversity. It is famous for thousand-year-old samu and pomu trees, regarded as treasures of the forest.",
    "Национальный парк Суанльен в уезде Тхыонгсуан (повышен в статусе в 2025 году) охраняет леса верховьев реки Тю с высоким биоразнообразием. Он известен тысячелетними деревьями саму и пому, которые считаются сокровищами леса.",
    "Vườn quốc gia Xuân Liên nằm ở vùng rừng thượng nguồn sông Chu, thuộc huyện Thường Xuân, phía tây tỉnh Thanh Hóa, giáp với nước bạn Lào. Vốn là khu bảo tồn thiên nhiên, đến tháng 2 năm 2025 Xuân Liên chính thức được nâng hạng thành vườn quốc gia, trở thành một trong ba vườn quốc gia của xứ Thanh với tổng diện tích quản lý hơn 25.000 ha. Đây là một trong những khu rừng có tính đa dạng sinh học cao bậc nhất khu vực bắc Trường Sơn, là nơi cư trú của nhiều loài động thực vật quý hiếm như voọc xám, vượn đen má trắng, mang, gấu, cùng hàng nghìn loài thực vật. Xuân Liên đặc biệt nổi tiếng với quần thể cây sa mu, pơ mu cổ thụ khổng lồ, trong đó có những cây được công nhận là Cây Di sản Việt Nam, tuổi đời ước tính lên tới cả nghìn năm, thân to mấy người ôm. Du khách yêu thiên nhiên có thể tham gia các tuyến trekking xuyên rừng, chinh phục đỉnh Pù Gió, ngắm thác Yên, hồ Cửa Đạt, quan sát chim thú và tìm hiểu văn hóa của đồng bào Thái sinh sống quanh vùng đệm. Vì là rừng đặc dụng, du khách nên liên hệ ban quản lý để đăng ký, thuê hướng dẫn viên và tuân thủ quy định bảo vệ rừng.",
    "Xuan Lien National Park lies in the upper Chu River forests of Thuong Xuan district, western Thanh Hoa, bordering Laos. Formerly a nature reserve, in February 2025 Xuan Lien was officially upgraded to a national park, becoming one of the province's three national parks, with a managed area of over 25,000 ha. It is among the most biodiverse forests of the northern Truong Son range, home to many rare animals and plants — grey langurs, white-cheeked gibbons, muntjac, bears — and thousands of plant species. Xuan Lien is especially famed for its stands of giant ancient samu and pomu trees, some recognised as Vietnam Heritage Trees, estimated to be a thousand years old, with trunks several people cannot span. Nature-loving visitors can join treks through the forest, climb Pu Gio peak, admire Yen Waterfall and Cua Dat Lake, watch wildlife and learn about the culture of the Thai people living in the buffer zone. As it is a special-use forest, visitors should contact the management board to register, hire a guide and observe forest-protection rules.",
    "Национальный парк Суанльен расположен в лесах верховьев реки Тю в уезде Тхыонгсуан на западе Тханьхоа, у границы с Лаосом. Прежде природный заповедник, в феврале 2025 года Суанльен официально повышен до национального парка и стал одним из трёх нацпарков провинции с управляемой площадью более 25 000 га. Это один из самых биоразнообразных лесов северного хребта Чыонгшон, дом многих редких животных и растений — серых лангуров, белощёких гиббонов, мунтжаков, медведей — и тысяч видов растений. Суанльен особенно славится рощами гигантских древних деревьев саму и пому, некоторые из которых признаны Наследственными деревьями Вьетнама, их возраст оценивают в тысячу лет, а стволы не могут обхватить несколько человек. Любители природы могут участвовать в походах по лесу, подниматься на пик Пузо, любоваться водопадом Йен и озером Кыадат, наблюдать за дикой природой и знакомиться с культурой народа тай, живущего в буферной зоне. Поскольку это лес особого назначения, посетителям следует связаться с администрацией для регистрации, найма гида и соблюдения правил охраны леса.",
    ["Nâng hạng thành vườn quốc gia năm 2025", "Cây sa mu, pơ mu cổ thụ nghìn năm tuổi (Cây Di sản)", "Trekking, ngắm chim thú giữa rừng nguyên sinh"],
    ["Upgraded to national park in 2025", "Thousand-year-old samu and pomu heritage trees", "Trekking and wildlife watching in primeval forest"],
    ["Повышен до национального парка в 2025 году", "Тысячелетние деревья-наследие саму и пому", "Треккинг и наблюдение за дикой природой в девственном лесу"],
    {"hours_vi": "Tham quan ban ngày; cần đăng ký trước.", "ticket_vi": "Phí tham quan/hướng dẫn theo quy định của vườn.",
     "duration_vi": "Nửa ngày đến vài ngày (tùy tuyến).", "best_time_vi": "Mùa khô (tháng 11–4).",
     "tips_vi": "Liên hệ ban quản lý để đăng ký và thuê hướng dẫn viên; mang giày trekking, đồ chống vắt/muỗi."},
    ["nature", "national-park", "forest", "trekking", "eco"],
    [{"title": "Wikipedia (VI) — Vườn quốc gia Xuân Liên", "url": "https://vi.wikipedia.org/wiki/V%C6%B0%E1%BB%9Dn_qu%E1%BB%91c_gia_Xu%C3%A2n_Li%C3%AAn"}],
))

# 20) Động Kim Sơn
new.append(R(
    "dong-kim-son", "Động Kim Sơn (Vĩnh An)", "Kim Son Cave", "Пещера Кимшон",
    ["other", "park_garden"], 20.0330, 105.6640,
    "Xã Vĩnh An, huyện Vĩnh Lộc, tỉnh Thanh Hóa",
    4.4, 350,
    "Du khách thích ngồi thuyền len qua hang nước, ngắm nhũ đá lung linh và cảnh núi non sông nước hữu tình. Nhiều người ví như \"Tràng An thu nhỏ\"; một số nhắc nên đi thuyền để trải nghiệm trọn vẹn.",
    "Động Kim Sơn ở xã Vĩnh An, huyện Vĩnh Lộc là quần thể hang động – sông nước với những dãy núi đá vôi soi bóng, được ví như \"Hạ Long trên cạn\" hay \"Tràng An của xứ Thanh\". Du khách đi thuyền xuyên hang, ngắm nhũ đá kỳ ảo.",
    "Kim Son Cave in Vinh An commune, Vinh Loc district, is a complex of caves and waterways with limestone peaks mirrored in the water, likened to a \"Ha Long on land\" or the \"Trang An of Thanh Hoa\". Visitors ride boats through the caves to see fantastical stalactites.",
    "Пещера Кимшон в общине Виньан уезда Виньлок — комплекс пещер и водных путей с известняковыми вершинами, отражёнными в воде, прозванный «Халонгом на суше» или «Чанганом Тханьхоа». Посетители плывут на лодках сквозь пещеры, любуясь причудливыми натёками.",
    "Động Kim Sơn thuộc xã Vĩnh An, huyện Vĩnh Lộc, cách Thành nhà Hồ không xa, là một danh thắng sơn thủy hữu tình còn khá hoang sơ của xứ Thanh. Quần thể gồm những dãy núi đá vôi trùng điệp xen giữa là dòng suối, hồ nước trong xanh và hệ thống hang động, tạo nên khung cảnh nước non giao hòa khiến nhiều người liên tưởng đến vịnh Hạ Long trên cạn hay khu Tràng An của Ninh Bình. Điểm nhấn của khu vực là hang Kim Sơn xuyên thủy: du khách ngồi trên thuyền nhỏ, theo dòng nước luồn qua lòng hang tối, hai bên là những khối nhũ đá, măng đá rủ xuống với muôn hình vạn trạng, lung linh dưới ánh đèn. Ra khỏi hang, không gian mở ra với mặt nước phẳng lặng phản chiếu vách núi và bầu trời, thấp thoáng chùa chiền và làng mạc yên bình. Cảnh sắc nơi đây thay đổi theo mùa, đẹp nhất là khi lúa xanh hoặc mùa nước đầy. Vì gần cụm di tích Vĩnh Lộc, du khách có thể kết hợp tham quan Thành nhà Hồ, Phủ Trịnh và các đền chùa lân cận trong cùng một hành trình, vừa khám phá thiên nhiên vừa tìm hiểu lịch sử vùng đất cố đô nhà Hồ.",
    "Kim Son Cave, in Vinh An commune, Vinh Loc district, not far from the Ho Citadel, is a still fairly untouched scenic gem of Thanh Hoa. The complex comprises ranges of limestone peaks interspersed with streams, clear lakes and cave systems, forming a harmony of water and mountains that recalls a Ha Long Bay on land or the Trang An area of Ninh Binh. Its highlight is the water-piercing Kim Son cave: visitors sit in small boats and follow the current through the dark cave, flanked by stalactites and stalagmites of countless shapes shimmering in the lamplight. Emerging from the cave, the space opens onto still water reflecting cliffs and sky, with glimpses of pagodas and peaceful villages. The scenery changes with the seasons, at its finest when the rice is green or the water is high. Being near the Vinh Loc relic cluster, visitors can combine a trip here with the Ho Citadel, Trinh Lords' Palace and nearby temples and pagodas, exploring nature and the history of the old Ho dynasty capital in a single journey.",
    "Пещера Кимшон в общине Виньан уезда Виньлок, недалеко от цитадели Хо, — всё ещё довольно нетронутая живописная жемчужина Тханьхоа. Комплекс состоит из гряд известняковых вершин, чередующихся с ручьями, чистыми озёрами и пещерными системами, образуя гармонию воды и гор, что напоминает бухту Халонг на суше или район Чанган в Ниньбине. Его изюминка — водная пещера Кимшон: посетители садятся в небольшие лодки и следуют по течению сквозь тёмную пещеру, по бокам которой сталактиты и сталагмиты бесчисленных форм мерцают в свете ламп. Выйдя из пещеры, пространство раскрывается на спокойную воду, отражающую скалы и небо, с проблесками пагод и мирных деревень. Пейзаж меняется по сезонам, красивее всего, когда рис зелен или вода высока. Находясь рядом с комплексом памятников Виньлок, посетители могут совместить поездку сюда с цитаделью Хо, дворцом князей Чинь и близлежащими храмами, исследуя природу и историю древней столицы династии Хо за одно путешествие.",
    ["Hang xuyên thủy, đi thuyền ngắm nhũ đá kỳ ảo", "Núi đá vôi soi bóng nước – \"Tràng An của xứ Thanh\"", "Gần cụm di tích Vĩnh Lộc (Thành nhà Hồ, Phủ Trịnh)"],
    ["Water-piercing cave, boat rides past fantastical stalactites", "Limestone peaks mirrored in water – the \"Trang An of Thanh Hoa\"", "Near the Vinh Loc relic cluster (Ho Citadel, Trinh Palace)"],
    ["Водная пещера, лодки среди причудливых натёков", "Известняковые вершины в отражении воды — «Чанган Тханьхоа»", "Рядом комплекс памятников Виньлок (цитадель Хо, дворец Чинь)"],
    {"hours_vi": "Khoảng 7:00–17:00 hằng ngày.", "ticket_vi": "Vé tham quan và thuê thuyền theo bảng giá địa phương.",
     "duration_vi": "Khoảng 1,5–2 giờ.", "best_time_vi": "Mùa lúa xanh hoặc mùa nước; buổi sáng mát.",
     "tips_vi": "Nên đi thuyền để vào hang; mang áo phao; kết hợp Thành nhà Hồ, Phủ Trịnh."},
    ["cave", "nature", "boat", "scenery", "outdoor"],
    [{"title": "Cổng TTĐT huyện Vĩnh Lộc — Danh thắng Kim Sơn", "url": "https://vinhloc.thanhhoa.gov.vn/"}],
))

# 21) Phủ Trịnh
new.append(R(
    "phu-trinh", "Phủ Trịnh (Nghè Vẹt)", "Trinh Lords' Palace (Phu Trinh)", "Дворец князей Чинь (Фучинь)",
    ["monument", "other"], 19.9930, 105.6150,
    "Xã Vĩnh Hùng, huyện Vĩnh Lộc, tỉnh Thanh Hóa",
    4.3, 250,
    "Du khách quan tâm tới nơi phát tích dòng họ Trịnh – các chúa từng nắm quyền lực ở Đàng Ngoài suốt hai thế kỷ. Nhiều người khen không gian trầm mặc, hiện vật quý; một số mong có thêm thuyết minh chi tiết.",
    "Phủ Trịnh ở xã Vĩnh Hùng, huyện Vĩnh Lộc là nơi phát tích và thờ tự dòng chúa Trịnh – những người nắm thực quyền ở Đàng Ngoài thời Lê trung hưng. Gần đó là Nghè Vẹt, tạo thành cụm di tích gắn với lịch sử \"vua Lê – chúa Trịnh\".",
    "Phu Trinh in Vinh Hung commune, Vinh Loc district, is the ancestral seat and shrine of the Trinh lords, who held real power in the north during the Le restoration. Nearby stands Nghe Vet, forming a relic cluster tied to the \"Le kings – Trinh lords\" era.",
    "Фучинь в общине Виньхунг уезда Виньлок — родовое гнездо и святилище князей Чинь, державших реальную власть на севере в эпоху реставрации Ле. Рядом стоит Нгевет, образуя комплекс памятников, связанный с эпохой «королей Ле — князей Чинь».",
    "Phủ Trịnh tọa lạc tại xã Vĩnh Hùng, huyện Vĩnh Lộc, là nơi phát tích của dòng họ Trịnh – dòng chúa đã nắm giữ thực quyền cai trị ở Đàng Ngoài trong hơn hai thế kỷ dưới thời Lê trung hưng, tạo nên cục diện lịch sử độc đáo \"vua Lê – chúa Trịnh\". Đây từng là phủ đệ, nơi thờ tự tổ tiên và các đời chúa Trịnh, lưu giữ nhiều hiện vật, sắc phong, đồ tế khí phản ánh một thời kỳ quyền lực và văn hóa đặc sắc. Trải qua thăng trầm lịch sử, di tích đã được trùng tu, tôn tạo khang trang với các tòa nhà thờ, sân vườn, cổng phủ mang nét kiến trúc truyền thống. Cách Phủ Trịnh không xa là Nghè Vẹt – nơi thờ Thành hoàng và các chúa Trịnh, với những hiện vật chạm khắc tinh xảo, đặc biệt là đôi chim vẹt gỗ gắn với tên gọi của di tích. Cả hai hợp thành cụm di tích lịch sử – văn hóa quan trọng của vùng đất Vĩnh Lộc, nơi có bề dày trầm tích lịch sử với cả Thành nhà Hồ – di sản thế giới. Đến đây, du khách không chỉ tìm hiểu về vai trò của họ Trịnh trong lịch sử phong kiến Việt Nam mà còn cảm nhận không gian trầm mặc, cổ kính giữa vùng quê yên bình bên bờ sông Mã.",
    "Phu Trinh stands in Vinh Hung commune, Vinh Loc district, the ancestral home of the Trinh family — the line of lords who wielded real ruling power in the north for more than two centuries during the Le restoration, creating the distinctive historical arrangement of \"Le kings and Trinh lords\". It was once a residence and place of worship for the ancestors and successive Trinh lords, keeping many artefacts, royal edicts and ceremonial objects that reflect an era of remarkable power and culture. Through historical vicissitudes the relic has been restored and handsomely embellished, with worship halls, gardens and a palace gate in traditional style. Not far away is Nghe Vet — a shrine to the tutelary god and the Trinh lords, with finely carved objects, notably the pair of wooden parrots (vet) that give the site its name. Together they form an important historical-cultural cluster of the Vinh Loc area, a land layered with history that also holds the world-heritage Ho Citadel. Here visitors not only learn about the role of the Trinh family in Vietnam's feudal history but also feel the solemn, ancient atmosphere amid peaceful countryside by the Ma River.",
    "Фучинь стоит в общине Виньхунг уезда Виньлок — родовой дом семьи Чинь, линии князей, что более двух веков держали реальную власть на севере в эпоху реставрации Ле, создав своеобразное историческое устройство «короли Ле и князья Чинь». Некогда это была резиденция и место поклонения предкам и сменявшим друг друга князьям Чинь, где хранятся многие артефакты, царские указы и церемониальные предметы, отражающие эпоху замечательной власти и культуры. Пройдя через исторические превратности, памятник был отреставрирован и красиво украшен — с залами для поклонения, садами и дворцовыми воротами в традиционном стиле. Неподалёку — Нгевет, святилище богу-покровителю и князьям Чинь, с тонко вырезанными предметами, прежде всего парой деревянных попугаев (вет), давших название месту. Вместе они образуют важный историко-культурный комплекс района Виньлок, земли, насыщенной историей, где есть и цитадель Хо — объект всемирного наследия. Здесь посетители не только узнают о роли семьи Чинь в феодальной истории Вьетнама, но и ощущают торжественную, древнюю атмосферу среди мирной сельской местности у реки Ма.",
    ["Nơi phát tích và thờ tự dòng chúa Trịnh", "Gắn cục diện lịch sử \"vua Lê – chúa Trịnh\"", "Cụm di tích cùng Nghè Vẹt ở Vĩnh Lộc"],
    ["Ancestral seat and shrine of the Trinh lords", "Tied to the 'Le kings – Trinh lords' era", "Relic cluster with Nghe Vet in Vinh Loc"],
    ["Родовое гнездо и святилище князей Чинь", "Связан с эпохой «короли Ле — князья Чинь»", "Комплекс памятников вместе с Нгевет в Виньлоке"],
    {"hours_vi": "Khoảng 7:00–17:30 hằng ngày.", "ticket_vi": "Vào cửa tự do (công đức tùy tâm).",
     "duration_vi": "Khoảng 45 phút.", "best_time_vi": "Buổi sáng; kết hợp lộ trình di tích Vĩnh Lộc.",
     "tips_vi": "Kết hợp Thành nhà Hồ, động Kim Sơn; ăn mặc lịch sự khi vào nơi thờ tự."},
    ["history", "heritage", "dynasty", "temple"],
    [{"title": "Cổng TTĐT huyện Vĩnh Lộc — Phủ Trịnh, Nghè Vẹt", "url": "https://vinhloc.thanhhoa.gov.vn/"}],
))

# 22) Hang Con Moong
new.append(R(
    "hang-con-moong", "Hang Con Moong", "Con Moong Cave", "Пещера Конмоонг",
    ["other", "monument"], 20.3000, 105.6150,
    "Xã Thành Yên, huyện Thạch Thành, tỉnh Thanh Hóa",
    4.3, 200,
    "Du khách và giới nghiên cứu quan tâm tới hang chứa dấu tích người tiền sử cư trú liên tục qua nhiều nghìn năm. Nhiều người thấy giá trị khảo cổ đặc biệt; một số nhắc đường vào xa, nên có hướng dẫn.",
    "Hang Con Moong ở xã Thành Yên, huyện Thạch Thành (vùng đệm Cúc Phương) là di chỉ khảo cổ nổi tiếng, lưu giữ dấu tích người tiền sử cư trú liên tục qua nhiều giai đoạn văn hóa. Đây là Di tích quốc gia đặc biệt về khảo cổ học.",
    "Con Moong Cave in Thanh Yen commune, Thach Thanh district (in the Cuc Phuong buffer zone), is a famous archaeological site preserving traces of continuous prehistoric habitation across several cultural phases. It is a Special National Archaeological Relic.",
    "Пещера Конмоонг в общине Тханьйен уезда Тхактхань (в буферной зоне Кукфыонга) — знаменитый археологический памятник, хранящий следы непрерывного доисторического обитания на протяжении нескольких культурных этапов. Это особый национальный археологический памятник.",
    "Hang Con Moong nằm ở xã Thành Yên, huyện Thạch Thành, thuộc vùng rừng núi đá vôi phía bắc tỉnh Thanh Hóa, giáp ranh vườn quốc gia Cúc Phương. Đây là một trong những di chỉ khảo cổ học tiền sử quan trọng bậc nhất Việt Nam và Đông Nam Á. Qua nhiều đợt khai quật, các nhà khoa học đã tìm thấy trong hang một tầng văn hóa dày, liên tục, chứa đựng dấu tích cư trú của người nguyên thủy kéo dài hàng chục nghìn năm, phản ánh sự chuyển tiếp giữa nhiều giai đoạn và loại hình văn hóa khảo cổ – từ thời đại đồ đá cũ sang đá mới. Những phát hiện gồm công cụ đá, xương động vật, vỏ nhuyễn thể, bếp lửa, mộ táng… cho thấy quá trình sinh sống, lao động và tiến hóa của con người thời tiền sử ngay tại vùng đất này. Chính vì giá trị đặc biệt đó, hang Con Moong và các di tích phụ cận đã được xếp hạng Di tích quốc gia đặc biệt, đồng thời được đề cử vào danh mục dự kiến di sản thế giới. Với du khách yêu lịch sử và khảo cổ, đây là điểm đến độc đáo để hình dung về buổi bình minh của loài người; do nằm ở vùng núi xa, nên đi cùng hướng dẫn viên và tìm hiểu trước thông tin để chuyến tham quan trọn vẹn.",
    "Con Moong Cave lies in Thanh Yen commune, Thach Thanh district, in the limestone mountains of northern Thanh Hoa, bordering Cuc Phuong National Park. It is one of the most important prehistoric archaeological sites in Vietnam and Southeast Asia. Through several excavations, scientists have found within the cave a thick, continuous cultural layer containing traces of primitive habitation spanning tens of thousands of years, reflecting the transition across many phases and types of archaeological culture — from the Palaeolithic to the Neolithic. Finds include stone tools, animal bones, mollusc shells, hearths and burials, revealing the living, working and evolution of prehistoric people on this very land. For that exceptional value, Con Moong Cave and its neighbouring relics have been ranked a Special National Relic and nominated to the tentative list of world heritage. For visitors who love history and archaeology, it is a unique destination to picture the dawn of humankind; as it lies in a remote mountain area, it is best to go with a guide and read up beforehand for a rewarding visit.",
    "Пещера Конмоонг находится в общине Тханьйен уезда Тхактхань, в известняковых горах северного Тханьхоа, у границы национального парка Кукфыонг. Это один из важнейших доисторических археологических памятников Вьетнама и Юго-Восточной Азии. В ходе нескольких раскопок учёные обнаружили в пещере толстый, непрерывный культурный слой со следами первобытного обитания протяжённостью в десятки тысяч лет, отражающий переход через многие этапы и типы археологической культуры — от палеолита к неолиту. Находки включают каменные орудия, кости животных, раковины моллюсков, очаги и погребения, раскрывая жизнь, труд и эволюцию доисторических людей именно на этой земле. За эту исключительную ценность пещера Конмоонг и соседние памятники отнесены к особым национальным памятникам и номинированы в предварительный список всемирного наследия. Для посетителей, любящих историю и археологию, это уникальное место, чтобы представить зарю человечества; поскольку оно находится в отдалённом горном районе, лучше идти с гидом и заранее ознакомиться с информацией для полноценного посещения.",
    ["Di chỉ người tiền sử cư trú liên tục hàng chục nghìn năm", "Di tích quốc gia đặc biệt về khảo cổ học", "Nằm trong vùng đệm rừng Cúc Phương"],
    ["Site of continuous prehistoric habitation over tens of thousands of years", "Special National Archaeological Relic", "In the Cuc Phuong forest buffer zone"],
    ["Памятник непрерывного доисторического обитания в десятки тысяч лет", "Особый национальный археологический памятник", "В буферной зоне леса Кукфыонг"],
    {"hours_vi": "Tham quan ban ngày; nên liên hệ trước.", "ticket_vi": "Phí tham quan/hướng dẫn theo quy định địa phương.",
     "duration_vi": "Khoảng 1 giờ.", "best_time_vi": "Mùa khô (tháng 11–4).",
     "tips_vi": "Đường vào xa, nên đi cùng hướng dẫn viên; mang giày đi bộ, đèn pin; kết hợp Cúc Phương."},
    ["archaeology", "history", "cave", "prehistory"],
    [{"title": "Wikipedia (VI) — Hang Con Moong", "url": "https://vi.wikipedia.org/wiki/Hang_Con_Moong"}],
))

# 23) Thái miếu nhà Hậu Lê
new.append(R(
    "thai-mieu-nha-hau-le", "Thái miếu nhà Hậu Lê", "Ancestral Temple of the Later Le Dynasty", "Храм предков династии Поздние Ле",
    ["church", "monument"], 19.7920, 105.7790,
    "Phường Đông Vệ, TP Thanh Hóa, tỉnh Thanh Hóa",
    4.4, 300,
    "Du khách trân trọng nơi thờ các vua và hoàng hậu triều Hậu Lê, khen kiến trúc gỗ cổ và hiện vật quý. Nhiều người tới dâng hương dịp lễ; một số mong biết thêm về lịch sử di dời của miếu.",
    "Thái miếu nhà Hậu Lê ở phường Đông Vệ (TP Thanh Hóa) là nơi thờ tổ tiên, các vua và hoàng hậu triều Hậu Lê. Được rước từ Thăng Long về đất phát tích xứ Thanh, thái miếu lưu giữ nhiều hiện vật và bài vị quý giá.",
    "The Ancestral Temple of the Later Le Dynasty in Dong Ve ward (Thanh Hoa city) enshrines the ancestors, kings and queens of the Later Le. Moved from Thang Long to the dynasty's homeland in Thanh Hoa, it keeps many precious artefacts and tablets.",
    "Храм предков династии Поздние Ле в квартале Донгве (город Тханьхоа) хранит предков, королей и королев Поздних Ле. Перенесённый из Тханглонга на родину династии в Тханьхоа, он бережёт многие ценные реликвии и таблички.",
    "Thái miếu nhà Hậu Lê nằm ở phường Đông Vệ, thành phố Thanh Hóa, là nơi thờ tổ tiên và các vị hoàng đế, hoàng hậu của vương triều Hậu Lê – triều đại phong kiến tồn tại lâu dài bậc nhất trong lịch sử Việt Nam, khởi nghiệp từ cuộc khởi nghĩa Lam Sơn của người anh hùng Lê Lợi trên chính đất xứ Thanh. Nguyên trước kia thái miếu được đặt ở kinh đô Thăng Long; về sau, các bài vị, đồ thờ được rước về vùng đất phát tích Thanh Hóa để phụng thờ, gìn giữ. Ngôi miếu mang kiến trúc gỗ truyền thống với hệ thống cột, kèo, cửa võng chạm khắc rồng phượng, hoa văn tinh xảo, sơn son thếp vàng, cùng nhiều hiện vật, bài vị, sắc phong có giá trị lịch sử và mỹ thuật cao. Không gian miếu trầm mặc, uy nghiêm, là nơi con cháu dòng họ và người dân đến dâng hương tưởng nhớ công lao dựng nước, giữ nước của các bậc tiền nhân. Vào các dịp lễ, giỗ, nơi đây tổ chức nghi lễ tế tự trang trọng theo nghi thức cổ truyền. Thái miếu nhà Hậu Lê là điểm đến ý nghĩa để tìm hiểu về một triều đại rực rỡ gắn bó máu thịt với vùng đất Thanh Hóa – nơi được xem là \"đất căn bản\" của nhà Lê.",
    "The Ancestral Temple of the Later Le Dynasty stands in Dong Ve ward, Thanh Hoa city, enshrining the ancestors and the emperors and empresses of the Later Le — the longest-lasting feudal dynasty in Vietnamese history, which began with the Lam Son uprising of the hero Le Loi on the soil of Thanh Hoa itself. The ancestral temple was originally in the capital Thang Long; later its spirit tablets and ritual objects were brought to the dynasty's homeland in Thanh Hoa for worship and safekeeping. The temple has traditional wooden architecture, with columns, beams and openwork screens carved with dragons, phoenixes and intricate patterns in gilt lacquer, along with many artefacts, tablets and edicts of high historical and artistic value. Its solemn, dignified space is where descendants of the family and local people come to offer incense and remember the merits of their forebears in building and defending the nation. On festival and memorial days, dignified rites are held in the ancient manner. The Ancestral Temple of the Later Le is a meaningful destination for learning about a brilliant dynasty intimately bound to Thanh Hoa — regarded as the \"foundational land\" of the Le.",
    "Храм предков династии Поздние Ле стоит в квартале Донгве города Тханьхоа и хранит предков, а также императоров и императриц Поздних Ле — самой долговечной феодальной династии в истории Вьетнама, начавшейся с восстания Лamшон героя Ле Лоя на самой земле Тханьхоа. Изначально храм предков находился в столице Тханглонг; позже его поминальные таблички и ритуальные предметы перенесли на родину династии в Тханьхоа для поклонения и сохранения. Храм имеет традиционную деревянную архитектуру: колонны, балки и ажурные ширмы, украшенные резьбой драконов, фениксов и затейливыми узорами в позолоте, а также множество реликвий, табличек и указов высокой исторической и художественной ценности. Его торжественное, величавое пространство — место, куда потомки рода и местные жители приходят возжечь благовония и вспомнить заслуги предков в созидании и защите страны. В праздничные и поминальные дни здесь по древнему обычаю совершают торжественные обряды. Храм предков Поздних Ле — значимое место, чтобы узнать о блестящей династии, кровно связанной с Тханьхоа, которую считают «коренной землёй» рода Ле.",
    ["Thờ tổ tiên, vua và hoàng hậu triều Hậu Lê", "Bài vị được rước từ Thăng Long về đất phát tích xứ Thanh", "Kiến trúc gỗ chạm khắc, sơn son thếp vàng"],
    ["Enshrines the ancestors, kings and queens of the Later Le", "Tablets brought from Thang Long to the dynasty's homeland", "Carved wooden architecture with gilt lacquer"],
    ["Хранит предков, королей и королев Поздних Ле", "Таблички, перенесённые из Тханглонга на родину династии", "Резная деревянная архитектура с позолотой"],
    {"hours_vi": "Khoảng 7:00–17:30 hằng ngày.", "ticket_vi": "Vào cửa tự do (công đức tùy tâm).",
     "duration_vi": "Khoảng 30–45 phút.", "best_time_vi": "Buổi sáng hoặc dịp lễ, giỗ.",
     "tips_vi": "Ăn mặc lịch sự; kết hợp tham quan các di tích trong thành phố và Lam Kinh."},
    ["history", "temple", "dynasty", "heritage"],
    [{"title": "Wikipedia (VI) — Nhà Hậu Lê", "url": "https://vi.wikipedia.org/wiki/Nh%C3%A0_H%E1%BA%ADu_L%C3%AA"}],
))

# 24) Bãi biển Tiên Trang
new.append(R(
    "bien-tien-trang", "Bãi biển Tiên Trang", "Tien Trang Beach", "Пляж Тьенчанг",
    ["other"], 19.6600, 105.8280,
    "Xã Quảng Thái, huyện Quảng Xương, tỉnh Thanh Hóa",
    4.1, 250,
    "Du khách thích bãi biển hoang sơ, vắng vẻ, cát trắng dài và rừng phi lao xanh mát. Nhiều người tìm sự yên tĩnh, hải sản rẻ; một số nhắc dịch vụ còn ít, phù hợp đi trong ngày hoặc cắm trại.",
    "Bãi biển Tiên Trang thuộc huyện Quảng Xương là bãi biển hoang sơ, yên tĩnh với bờ cát dài và rừng phi lao ven biển. Đây là lựa chọn dành cho những ai muốn tránh xa đám đông, tận hưởng thiên nhiên mộc mạc của biển xứ Thanh.",
    "Tien Trang Beach in Quang Xuong district is a wild, quiet beach with a long stretch of sand and coastal casuarina forest. It suits those wishing to escape the crowds and enjoy the rustic nature of Thanh Hoa's coast.",
    "Пляж Тьенчанг в уезде Куангсыонг — дикий, тихий пляж с длинной полосой песка и прибрежным лесом казуарин. Он подходит тем, кто хочет уйти от толп и насладиться безыскусной природой побережья Тханьхоа.",
    "Bãi biển Tiên Trang nằm ở xã Quảng Thái, huyện Quảng Xương, cách thành phố Thanh Hóa khoảng 20 km về phía đông nam và cách Sầm Sơn không xa. Khác với sự sầm uất của các bãi tắm lớn, Tiên Trang vẫn giữ được vẻ hoang sơ, tĩnh lặng với bờ cát trắng trải dài, thoai thoải, nước biển trong và những rặng phi lao xanh rì chạy dọc bờ tạo bóng mát. Bãi biển thoáng đãng, ít người, mang lại cảm giác riêng tư, gần gũi với thiên nhiên, rất hợp cho những ai muốn tìm chốn nghỉ ngơi yên bình, tránh xa ồn ào phố thị. Du khách có thể tắm biển, dạo bộ trên cát, cắm trại, đốt lửa trại qua đêm, hoặc đơn giản là ngồi dưới bóng phi lao nghe sóng vỗ và ngắm bình minh, hoàng hôn trên biển. Vùng này cũng nổi tiếng với hải sản tươi ngon do ngư dân địa phương đánh bắt, giá bình dân. Những năm gần đây, khu vực Tiên Trang bắt đầu được quy hoạch, đầu tư phát triển du lịch nghỉ dưỡng, nhưng hiện tại dịch vụ vẫn còn khiêm tốn, phù hợp cho chuyến đi trong ngày hoặc dã ngoại cuối tuần. Với những ai yêu thích sự mộc mạc, Tiên Trang là một góc biển đáng để khám phá ở xứ Thanh.",
    "Tien Trang Beach lies in Quang Thai commune, Quang Xuong district, about 20 km south-east of Thanh Hoa city and not far from Sam Son. Unlike the bustle of the large resorts, Tien Trang keeps its wild, quiet charm, with a long, gently sloping stretch of white sand, clear water and rows of green casuarina trees running along the shore to give shade. The beach is open and uncrowded, offering a sense of privacy and closeness to nature, ideal for those seeking a peaceful retreat away from urban noise. Visitors can swim, stroll on the sand, camp, hold a bonfire overnight, or simply sit under the casuarinas listening to the waves and watching sunrise and sunset over the sea. The area is also known for fresh, inexpensive seafood landed by local fishermen. In recent years Tien Trang has begun to be planned and developed for resort tourism, but services remain modest for now, suiting a day trip or weekend outing. For those who love the rustic, Tien Trang is a corner of coast well worth discovering in Thanh Hoa.",
    "Пляж Тьенчанг находится в общине Куангтхай уезда Куангсыонг, примерно в 20 км к юго-востоку от города Тханьхоа и недалеко от Шамшона. В отличие от суеты крупных курортов, Тьенчанг сохраняет свою дикую, тихую прелесть: длинная, полого спускающаяся полоса белого песка, чистая вода и ряды зелёных казуарин вдоль берега, дающие тень. Пляж открытый и немноголюдный, дарит ощущение уединения и близости к природе, идеален для тех, кто ищет спокойный отдых вдали от городского шума. Посетители могут купаться, гулять по песку, ставить палатки, жечь костёр на ночь или просто сидеть под казуаринами, слушая волны и наблюдая восход и закат над морем. Район также известен свежими недорогими морепродуктами, которые добывают местные рыбаки. В последние годы Тьенчанг начали планировать и осваивать для курортного туризма, но услуги пока скромны, что подходит для однодневной поездки или выходных. Для любителей безыскусного Тьенчанг — уголок побережья, который стоит открыть в Тханьхоа.",
    ["Bãi biển hoang sơ, vắng vẻ, cát trắng dài", "Rừng phi lao ven biển, không gian riêng tư", "Thích hợp cắm trại, dã ngoại; hải sản rẻ"],
    ["Wild, quiet beach with a long stretch of white sand", "Coastal casuarina forest and a sense of privacy", "Good for camping and picnics; cheap seafood"],
    ["Дикий, тихий пляж с длинной полосой белого песка", "Прибрежный лес казуарин и ощущение уединения", "Хорош для кемпинга и пикников; дешёвые морепродукты"],
    {"hours_vi": "Bãi biển mở cả ngày.", "ticket_vi": "Miễn phí.",
     "duration_vi": "Nửa ngày.", "best_time_vi": "Mùa hè (tháng 5–8); sáng sớm hoặc chiều mát.",
     "tips_vi": "Mang theo đồ ăn, nước vì ít hàng quán; chú ý an toàn khi tắm vì ít cứu hộ."},
    ["beach", "sea", "quiet", "camping"],
    [{"title": "Cổng TTĐT tỉnh Thanh Hóa — Du lịch biển Quảng Xương", "url": "https://thanhhoa.gov.vn/"}],
))

print("Batch E (records 19-24) defined:", len(new))

data = json.load(open(F, encoding="utf-8")) if os.path.exists(F) else []
have = {p["slug"] for p in data}
added = [p for p in new if p["slug"] not in have]
data += added
json.dump(data, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Đã thêm:", len(added), "| giờ có", len(data))
