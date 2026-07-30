# -*- coding: utf-8 -*-
"""Bổ sung địa điểm du lịch nổi tiếng tỉnh Thanh Hóa (giữ nguyên sau sáp nhập 2025).
Chèn an toàn: nạp -> append (bỏ qua slug đã có) -> ghi. Link bản đồ để trống,
tools/retrofit_map_links.py sẽ tự sinh theo tên EN + Thanh Hoa + Vietnam."""
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

# 1) Cầu Hàm Rồng
new.append(R(
    "cau-ham-rong", "Cầu Hàm Rồng", "Ham Rong Bridge", "Мост Хамронг",
    ["bridge", "monument"], 19.8215, 105.7765,
    "Phường Hàm Rồng, TP Thanh Hóa, tỉnh Thanh Hóa",
    4.5, 1600,
    "Du khách xúc động khi đứng trên cây cầu huyền thoại bắc qua sông Mã, nghe kể về những trận chiến bảo vệ cầu. Nhiều người thích ngắm hoàng hôn và tham quan cụm di tích Hàm Rồng lân cận; một số lưu ý đường lên đồi hơi dốc.",
    "Cầu Hàm Rồng bắc qua sông Mã ở cửa ngõ TP Thanh Hóa là biểu tượng bất khuất của quân dân xứ Thanh. Trong kháng chiến chống Mỹ, cây cầu thép này hứng chịu hàng nghìn trận bom nhưng vẫn đứng vững, gắn với chiến thắng Hàm Rồng lừng lẫy năm 1965.",
    "Ham Rong Bridge, spanning the Ma River at the gateway to Thanh Hoa city, is a symbol of the province's indomitable spirit. During the war against the United States, this steel bridge withstood thousands of bombing raids yet never fell, tied to the celebrated Ham Rong victory of 1965.",
    "Мост Хамронг через реку Ма у въезда в город Тханьхоа — символ несгибаемого духа провинции. Во время войны против США этот стальной мост выдержал тысячи бомбардировок, но так и не рухнул, и связан со знаменитой победой при Хамронге в 1965 году.",
    "Cầu Hàm Rồng nối hai bờ sông Mã, ngay dưới chân núi Rồng và núi Ngọc, là một trong những cây cầu nổi tiếng nhất lịch sử Việt Nam hiện đại. Được người Pháp xây dựng từ đầu thế kỷ 20 rồi tái thiết nhiều lần, cầu giữ vị trí chiến lược trên tuyến đường sắt và quốc lộ Bắc – Nam. Trong chiến tranh chống Mỹ, Hàm Rồng trở thành \"túi bom\": không quân Mỹ dội xuống đây hàng vạn tấn bom hòng cắt đứt mạch giao thông, nhưng bộ đội phòng không và dân quân địa phương đã bảo vệ cầu suốt nhiều năm, bắn rơi hàng trăm máy bay. Trận thắng ngày 3–4/4/1965 đi vào sử sách như bản anh hùng ca Hàm Rồng – Nam Ngạn. Ngày nay, cây cầu vẫn ngày ngày đón những chuyến tàu, còn khu vực quanh cầu là cụm di tích – danh thắng Hàm Rồng với núi Rồng, động Long Quang, làng cổ Đông Sơn và tượng đài chiến thắng. Từ trên đồi, du khách phóng tầm mắt xuống dòng sông Mã uốn lượn, cảm nhận trọn vẹn khí phách của một vùng đất anh hùng.",
    "Ham Rong Bridge links the two banks of the Ma River at the foot of Dragon Mountain and Ngoc Mountain, and is one of the most famous bridges in modern Vietnamese history. First built by the French in the early 20th century and rebuilt several times, it holds a strategic position on the North–South railway and highway. During the war against the United States, Ham Rong became a \"bomb magnet\": the US air force dropped tens of thousands of tonnes of bombs to sever the transport artery, but anti-aircraft troops and local militia defended it for years, downing hundreds of aircraft. The victory of 3–4 April 1965 entered the history books as the Ham Rong – Nam Ngan epic. Today trains still cross the bridge daily, and the surrounding area forms the Ham Rong relic-and-scenery cluster, with Dragon Mountain, Long Quang Cave, the ancient village of Dong Son and a victory monument. From the hilltop, visitors gaze down at the winding Ma River and take in the full spirit of this heroic land.",
    "Мост Хамронг соединяет два берега реки Ма у подножия горы Дракона и горы Нгок и является одним из самых знаменитых мостов в новейшей истории Вьетнама. Впервые построенный французами в начале XX века и несколько раз перестроенный, он занимает стратегическое положение на железной дороге и шоссе Север — Юг. Во время войны против США Хамронг стал «магнитом для бомб»: американская авиация сбросила здесь десятки тысяч тонн бомб, чтобы перерезать транспортную артерию, но зенитчики и местное ополчение защищали мост годами, сбив сотни самолётов. Победа 3–4 апреля 1965 года вошла в историю как эпопея Хамронг — Намнган. Сегодня по мосту по-прежнему ежедневно идут поезда, а окрестности образуют комплекс достопримечательностей Хамронг с горой Дракона, пещерой Лонгкуанг, древней деревней Донгшон и памятником Победы. С вершины холма посетители смотрят вниз на извилистую реку Ма и в полной мере ощущают дух этой героической земли.",
    ["Cây cầu thép huyền thoại bắc qua sông Mã", "Chiến thắng Hàm Rồng lịch sử năm 1965", "Cụm di tích – danh thắng núi Rồng, làng cổ Đông Sơn"],
    ["Legendary steel bridge over the Ma River", "Historic Ham Rong victory of 1965", "Cluster of relics and scenery: Dragon Mountain, Dong Son village"],
    ["Легендарный стальной мост через реку Ма", "Историческая победа при Хамронге в 1965 году", "Комплекс достопримечательностей: гора Дракона, деревня Донгшон"],
    {"hours_vi": "Khu vực ngoài trời, tham quan cả ngày.", "ticket_vi": "Miễn phí đi qua cầu; một số điểm di tích lân cận thu vé nhỏ.",
     "duration_vi": "Khoảng 1–2 giờ.", "best_time_vi": "Chiều mát để ngắm hoàng hôn trên sông Mã.",
     "tips_vi": "Kết hợp tham quan làng cổ Đông Sơn, động Long Quang và tượng đài Thanh niên xung phong."},
    ["history", "bridge", "war", "top", "outdoor"],
    [{"title": "Wikipedia (VI) — Cầu Hàm Rồng", "url": "https://vi.wikipedia.org/wiki/C%E1%BA%A7u_H%C3%A0m_R%E1%BB%93ng_(Thanh_H%C3%B3a)"}],
))

# 2) Đền Bà Triệu
new.append(R(
    "den-ba-trieu", "Đền Bà Triệu", "Ba Trieu Temple", "Храм Ба Чьеу",
    ["church", "monument"], 19.9060, 105.8365,
    "Núi Gai, xã Triệu Lộc, huyện Hậu Lộc, tỉnh Thanh Hóa",
    4.6, 1200,
    "Du khách trân trọng không gian cổ kính thờ nữ anh hùng Triệu Thị Trinh, khen kiến trúc đền uy nghi dưới chân núi Gai. Nhiều người về dự lễ hội tháng Hai âm lịch; một số góp ý nên có thêm hướng dẫn viên kể tích.",
    "Đền Bà Triệu dưới chân núi Gai (huyện Hậu Lộc) thờ nữ anh hùng Triệu Thị Trinh, người lãnh đạo khởi nghĩa chống quân Đông Ngô năm 248. Ngôi đền cổ kính là Di tích quốc gia đặc biệt, gắn với câu nói bất hủ về khát vọng \"cưỡi cơn gió mạnh, đạp luồng sóng dữ\".",
    "Ba Trieu Temple, at the foot of Gai Mountain in Hau Loc district, honours the heroine Trieu Thi Trinh, who led an uprising against the Eastern Wu in 248 AD. This ancient temple is a Special National Relic, tied to her immortal vow to \"ride the strong wind and trample the fierce waves\".",
    "Храм Ба Чьеу у подножия горы Гай в уезде Хаулок посвящён героине Чьеу Тхи Чинь, возглавившей восстание против царства Восточная У в 248 году. Этот древний храм — особый национальный памятник, связанный с её бессмертными словами о желании «оседлать сильный ветер и попрать свирепые волны».",
    "Đền Bà Triệu tọa lạc dưới chân núi Gai bên quốc lộ 1A, là nơi tưởng niệm Triệu Thị Trinh (Bà Triệu) – nữ tướng đã phất cờ khởi nghĩa chống ách đô hộ của nhà Đông Ngô vào năm 248 khi mới ngoài hai mươi tuổi. Tương truyền bà cưỡi voi trắng ra trận, khí phách lẫm liệt khiến quân giặc khiếp sợ. Quần thể di tích gồm đền chính, lăng mộ Bà Triệu trên đỉnh núi Tùng, đình làng Phú Điền và khu miếu thờ, mang đậm phong cách kiến trúc truyền thống với cổng nghi môn, sân rồng, các tòa tiền đường – hậu cung chạm khắc tinh xảo. Cây cối cổ thụ và không gian trầm mặc tạo nên vẻ linh thiêng hiếm có. Hằng năm, lễ hội Bà Triệu diễn ra vào khoảng ngày 21–24 tháng Hai âm lịch với rước kiệu, tế lễ, trò diễn dân gian, thu hút đông đảo người dân và du khách thập phương. Đền đã được xếp hạng Di tích lịch sử và kiến trúc nghệ thuật quốc gia đặc biệt, là điểm đến không thể bỏ qua khi tìm hiểu truyền thống chống ngoại xâm bất khuất của dân tộc Việt Nam.",
    "Ba Trieu Temple sits at the foot of Gai Mountain beside National Highway 1A, commemorating Trieu Thi Trinh (Lady Trieu), the woman general who raised the banner of revolt against Eastern Wu rule in 248 AD when barely in her twenties. Legend says she rode a white elephant into battle, her fierce bearing terrifying the enemy. The relic complex comprises the main temple, Lady Trieu's tomb atop Tung Mountain, the Phu Dien communal house and shrines, all in traditional style with ceremonial gates, a dragon courtyard and finely carved front-hall and sanctuary. Ancient trees and a solemn atmosphere lend a rare sense of the sacred. Each year the Ba Trieu Festival is held around the 21st–24th of the second lunar month, with palanquin processions, rites and folk performances drawing crowds of pilgrims and visitors. The temple is ranked a Special National Relic of history and artistic architecture, an essential stop for understanding Vietnam's indomitable tradition of resisting foreign invasion.",
    "Храм Ба Чьеу расположен у подножия горы Гай возле национального шоссе № 1, увековечивая Чьеу Тхи Чинь (госпожу Чьеу) — женщину-полководца, поднявшую знамя восстания против власти Восточной У в 248 году, когда ей едва исполнилось двадцать. По преданию, она шла в бой на белом слоне, и её грозный облик наводил ужас на врага. Комплекс включает главный храм, гробницу госпожи Чьеу на вершине горы Тунг, общинный дом Фудьен и святилища в традиционном стиле — с церемониальными воротами, «драконьим» двором и тонкой резьбой переднего зала и святилища. Древние деревья и торжественная атмосфера создают редкое ощущение священного. Ежегодно около 21–24-го числа второго лунного месяца проходит фестиваль Ба Чьеу с процессиями паланкинов, обрядами и народными представлениями, привлекающий множество паломников и туристов. Храм отнесён к особым национальным памятникам истории и художественной архитектуры и является обязательной остановкой для тех, кто хочет понять несгибаемую традицию сопротивления вьетнамцев иноземным нашествиям.",
    ["Thờ nữ anh hùng Triệu Thị Trinh (khởi nghĩa năm 248)", "Di tích quốc gia đặc biệt dưới chân núi Gai", "Lễ hội Bà Triệu tháng Hai âm lịch"],
    ["Honours heroine Trieu Thi Trinh (248 AD uprising)", "Special National Relic at the foot of Gai Mountain", "Ba Trieu Festival in the second lunar month"],
    ["Посвящён героине Чьеу Тхи Чинь (восстание 248 года)", "Особый национальный памятник у подножия горы Гай", "Фестиваль Ба Чьеу во втором лунном месяце"],
    {"hours_vi": "Khoảng 7:00–18:00 hằng ngày.", "ticket_vi": "Vào cửa tự do (công đức tùy tâm).",
     "duration_vi": "Khoảng 1–1,5 giờ.", "best_time_vi": "Dịp lễ hội tháng Hai âm lịch hoặc buổi sáng mát.",
     "tips_vi": "Ăn mặc lịch sự; leo núi Tùng viếng lăng mộ Bà Triệu; kết hợp Lam Kinh, Thành nhà Hồ."},
    ["history", "temple", "heritage", "top", "spiritual"],
    [{"title": "Wikipedia (VI) — Đền Bà Triệu", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%81n_B%C3%A0_Tri%E1%BB%87u"}],
))

# 3) Đền Sòng Sơn
new.append(R(
    "den-song-son", "Đền Sòng Sơn", "Song Son Temple", "Храм Шонгшон",
    ["church"], 20.0770, 105.8590,
    "Phường Bắc Sơn, thị xã Bỉm Sơn, tỉnh Thanh Hóa",
    4.5, 900,
    "Người hành hương tin đây là ngôi đền Mẫu linh thiêng bậc nhất, khen không gian trang nghiêm và giếng nước trong. Nhiều người đến cầu tài lộc, bình an; một số nhắc dịp lễ khá đông đúc.",
    "Đền Sòng Sơn ở thị xã Bỉm Sơn thờ Thánh Mẫu Liễu Hạnh – một trong \"Tứ bất tử\" của tín ngưỡng Việt. Dân gian truyền tụng \"Sòng thiêng\" là ngôi đền Mẫu linh thiêng nổi tiếng bậc nhất xứ Bắc Trung Bộ.",
    "Song Son Temple in Bim Son town is dedicated to Holy Mother Lieu Hanh, one of the \"Four Immortals\" of Vietnamese belief. Folk tradition holds that \"sacred Song\" is among the most revered Mother-Goddess temples in the north-central region.",
    "Храм Шонгшон в городе Бимшон посвящён Святой Матери Льеу Хань — одной из «Четырёх бессмертных» вьетнамских верований. По народному преданию, «священный Шонг» — один из самых почитаемых храмов Богини-Матери на севере центрального Вьетнама.",
    "Đền Sòng Sơn (còn gọi là đền Sòng) nằm ở thị xã Bỉm Sơn, cửa ngõ phía bắc tỉnh Thanh Hóa, được xây dựng từ thời Cảnh Hưng triều Lê để thờ Thánh Mẫu Liễu Hạnh. Theo tín ngưỡng thờ Mẫu, Liễu Hạnh là công chúa con Ngọc Hoàng giáng trần, được tôn là một trong bốn vị thánh bất tử của người Việt. Câu ca \"Sòng thiêng\" từ lâu khẳng định vị thế của ngôi đền trong đời sống tâm linh xứ Thanh. Đền tọa lạc trong khung cảnh sơn thủy hữu tình, phía trước có dòng suối và giếng nước tự nhiên nước trong vắt quanh năm gọi là giếng Ngọc. Kiến trúc đền gồm nhiều lớp cung thờ, mái cong, chạm khắc rồng phượng, sơn son thếp vàng lộng lẫy. Hằng năm, lễ hội đền Sòng diễn ra vào khoảng ngày 26 tháng Hai âm lịch, gắn với nghi thức rước bóng Thánh Mẫu và diễn xướng hầu đồng – một phần của di sản Thực hành tín ngưỡng thờ Mẫu Tam phủ được UNESCO ghi danh. Du khách đến đây không chỉ để chiêm bái, cầu an mà còn cảm nhận nét đẹp của văn hóa tâm linh và nghệ thuật chầu văn truyền thống.",
    "Song Son Temple (also called Den Song) stands in Bim Son town at the northern gateway of Thanh Hoa province. Built in the Canh Hung era of the Le dynasty, it is dedicated to Holy Mother Lieu Hanh. In the Mother-Goddess faith, Lieu Hanh is a daughter of the Jade Emperor who descended to earth and is revered as one of the four Vietnamese immortals. The saying \"sacred Song\" has long affirmed the temple's place in the spiritual life of the region. It sits amid picturesque scenery, fronted by a stream and a natural well of crystal-clear water known as the Jade Well. The architecture comprises successive worship chambers with curved roofs, carvings of dragons and phoenixes and lavish gilt lacquer. Each year the Song Temple Festival is held around the 26th of the second lunar month, featuring the procession of the Holy Mother and spirit-medium performances — part of the Practices Related to the Viet Beliefs in the Mother Goddesses of Three Realms, inscribed by UNESCO. Visitors come not only to pray for peace but also to experience the beauty of spiritual culture and the traditional chau van art.",
    "Храм Шонгшон (также Дэншонг) стоит в городе Бимшон у северных ворот провинции Тханьхоа. Построенный в эпоху Каньхынг династии Ле, он посвящён Святой Матери Льеу Хань. В культе Богини-Матери Льеу Хань — дочь Нефритового императора, сошедшая на землю и почитаемая как одна из четырёх вьетнамских бессмертных. Поговорка «священный Шонг» издавна утверждает место храма в духовной жизни края. Он расположен среди живописных пейзажей, перед ним — ручей и природный колодец с кристально чистой водой, называемый Нефритовым колодцем. Архитектура состоит из последовательных залов для поклонения с изогнутыми крышами, резьбой драконов и фениксов и роскошной позолотой. Ежегодно около 26-го числа второго лунного месяца проходит фестиваль храма Шонг с процессией Святой Матери и обрядами медиумов — частью практик поклонения Богиням-Матерям Трёх миров, внесённых ЮНЕСКО в список наследия. Посетители приходят сюда не только помолиться о мире, но и ощутить красоту духовной культуры и традиционного искусства тямван.",
    ["Thờ Thánh Mẫu Liễu Hạnh – một trong Tứ bất tử", "Ngôi đền Mẫu \"Sòng thiêng\" nổi tiếng linh thiêng", "Lễ hội và diễn xướng hầu đồng (di sản UNESCO)"],
    ["Dedicated to Holy Mother Lieu Hanh, one of the Four Immortals", "The revered \"sacred Song\" Mother-Goddess temple", "Festival and spirit-medium rites (UNESCO heritage)"],
    ["Посвящён Святой Матери Льеу Хань — одной из Четырёх бессмертных", "Почитаемый храм Богини-Матери «священный Шонг»", "Фестиваль и обряды медиумов (наследие ЮНЕСКО)"],
    {"hours_vi": "Khoảng 6:30–18:00 hằng ngày.", "ticket_vi": "Vào cửa tự do (công đức tùy tâm).",
     "duration_vi": "Khoảng 45–60 phút.", "best_time_vi": "Dịp lễ hội tháng Hai âm lịch hoặc đầu năm.",
     "tips_vi": "Ăn mặc kín đáo; kết hợp viếng đền Chín Giếng gần đó."},
    ["temple", "spiritual", "mother-goddess", "heritage"],
    [{"title": "Wikipedia (VI) — Đền Sòng Sơn", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%81n_S%C3%B2ng_S%C6%A1n"}],
))

# 4) Đền Chín Giếng
new.append(R(
    "den-chin-gieng", "Đền Chín Giếng (Đền Cô Chín)", "Chin Gieng Temple (Nine Wells Temple)", "Храм Тьинзиенг (Девяти колодцев)",
    ["church"], 20.0755, 105.8650,
    "Phường Bắc Sơn, thị xã Bỉm Sơn, tỉnh Thanh Hóa",
    4.5, 700,
    "Du khách thích cảnh chín mạch nước tự nhiên trong vắt và không khí linh thiêng thờ Cô Chín. Nhiều người đi cùng lộ trình với đền Sòng; một số cho biết ngày rằm khá đông.",
    "Đền Chín Giếng cách đền Sòng Sơn khoảng 1 km, thờ Cửu Thiên Huyền Nữ (Cô Chín). Đền nổi tiếng bởi chín mạch nước tự nhiên (chín giếng) không bao giờ cạn, được xem là điểm cầu tài lộc linh thiêng của xứ Thanh.",
    "Chin Gieng Temple, about 1 km from Song Son Temple, is dedicated to Co Chin (the Ninth Fairy, Cuu Thien Huyen Nu). It is famous for nine natural springs (nine wells) that never run dry, and is regarded as a sacred place to pray for fortune in Thanh Hoa.",
    "Храм Тьинзиенг примерно в 1 км от храма Шонгшон посвящён Ко Тьин (Девятой фее, Кыутхьен Хюентны). Он известен девятью природными источниками («девять колодцев»), которые никогда не пересыхают, и считается священным местом для молитв об удаче в Тханьхоа.",
    "Đền Chín Giếng (đền Cô Chín) tọa lạc gần đền Sòng Sơn tại thị xã Bỉm Sơn, tạo thành cụm di tích tâm linh nổi tiếng ở cửa ngõ phía bắc Thanh Hóa. Đền thờ Cửu Thiên Huyền Nữ – tương truyền là con gái thứ chín của Ngọc Hoàng, quen gọi là Cô Chín, một vị thánh cô trong tín ngưỡng thờ Mẫu. Điều làm nên tên gọi và sự đặc biệt của đền là chín mạch nước tự nhiên phun trào ngay trong khuôn viên, quanh năm trong xanh, mát lạnh và không bao giờ cạn; người dân tin rằng đây là dòng nước thiêng gột rửa muộn phiền, đem lại may mắn. Ngôi đền có quy mô vừa phải nhưng được tôn tạo khang trang, nằm bên dòng suối uốn quanh tạo cảnh sơn thủy thanh tịnh. Vào các dịp đầu năm và lễ hội (thường gắn với lễ hội đền Sòng cuối tháng Hai âm lịch, cùng ngày rước bóng), khách hành hương đổ về rất đông để dâng lễ, xin lộc và trải nghiệm nghi thức hầu đồng. Đền Chín Giếng cùng đền Sòng Sơn là điểm dừng chân quen thuộc của các đoàn hành hương trên hành trình về xứ Thanh.",
    "Chin Gieng Temple (Co Chin Temple) lies near Song Son Temple in Bim Son town, forming a famous spiritual cluster at Thanh Hoa's northern gateway. It is dedicated to Cuu Thien Huyen Nu — by legend the ninth daughter of the Jade Emperor, popularly called Co Chin, a saintly lady in the Mother-Goddess faith. What gives the temple its name and character are the nine natural springs bubbling up within its grounds: clear, cool and never drying, believed by locals to be sacred water that washes away sorrow and brings luck. The temple is modest in scale but handsomely restored, set beside a winding stream in serene scenery. At the start of the year and during festivals — usually tied to the Song Temple Festival at the end of the second lunar month — pilgrims flock here to make offerings, seek blessings and witness spirit-medium rites. Together with Song Son Temple, Chin Gieng is a familiar stop for pilgrim groups journeying through Thanh Hoa.",
    "Храм Тьинзиенг (храм Ко Тьин) находится рядом с храмом Шонгшон в городе Бимшон, образуя знаменитый духовный комплекс у северных ворот Тханьхоа. Он посвящён Кыутхьен Хюентны — по преданию, девятой дочери Нефритового императора, которую в народе называют Ко Тьин, святой деве в культе Богини-Матери. Название и особенность храму дают девять природных источников, бьющих прямо на его территории: чистые, прохладные и никогда не пересыхающие; местные жители верят, что это священная вода, смывающая печали и приносящая удачу. Храм невелик, но красиво отреставрирован и стоит у извилистого ручья среди безмятежных пейзажей. В начале года и во время фестивалей — обычно приуроченных к фестивалю храма Шонг в конце второго лунного месяца — паломники стекаются сюда, чтобы совершить подношения, попросить благословения и увидеть обряды медиумов. Вместе с храмом Шонгшон Тьинзиенг — привычная остановка паломнических групп в путешествии по Тханьхоа.",
    ["Thờ Cô Chín (Cửu Thiên Huyền Nữ)", "Chín mạch nước tự nhiên không bao giờ cạn", "Cụm hành hương cùng đền Sòng Sơn"],
    ["Dedicated to Co Chin (Cuu Thien Huyen Nu)", "Nine natural springs that never run dry", "Pilgrimage cluster with Song Son Temple"],
    ["Посвящён Ко Тьин (Кыутхьен Хюентны)", "Девять природных источников, которые не пересыхают", "Паломнический комплекс вместе с храмом Шонгшон"],
    {"hours_vi": "Khoảng 6:30–18:00 hằng ngày.", "ticket_vi": "Vào cửa tự do (công đức tùy tâm).",
     "duration_vi": "Khoảng 30–45 phút.", "best_time_vi": "Đầu năm hoặc dịp lễ hội đền Sòng.",
     "tips_vi": "Đi bộ từ đền Sòng sang; ăn mặc lịch sự, giữ trật tự nơi thờ tự."},
    ["temple", "spiritual", "mother-goddess"],
    [{"title": "Wikipedia (VI) — Đền Chín Giếng", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%81n_S%C3%B2ng_S%C6%A1n"}],
))

print("Batch A (records 1-4) defined:", len(new))

data = json.load(open(F, encoding="utf-8")) if os.path.exists(F) else []
have = {p["slug"] for p in data}
added = [p for p in new if p["slug"] not in have]
data += added
json.dump(data, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Đã thêm:", len(added), "| giờ có", len(data))
