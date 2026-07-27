# -*- coding: utf-8 -*-
"""
_add_vn_places_20260727.py — Bổ sung địa điểm DU LỊCH VIỆT NAM (đơn vị hành chính MỚI 2025).
Tự động: nhóm theo region, sao lưu, append (bỏ qua slug trùng), giữ nguyên file cũ.
Chạy:  python3 tools/_add_vn_places_20260727.py   (sau đó build.py + refresh_hub_stat.py)
"""
import json, os, datetime, shutil

ROOT = "/sessions/sleepy-focused-thompson/mnt/russia-tourism"
REG = os.path.join(ROOT, "data", "regions")


def rec(region, region_name_vi, fed, slug, name_vi, name_en, name_ru, cats, lat, lon,
        addr, rating, short_vi, short_en, short_ru, long_vi, long_en, long_ru,
        hi_vi, hi_en, hi_ru, practical, tags, review_vi, photo=None, sources=None):
    return {
        "id": region + "-" + slug,
        "slug": slug,
        "region": region,
        "country": "vietnam",
        "region_name_vi": region_name_vi,
        "federal_district": fed,
        "name_vi": name_vi,
        "name_ru": name_ru,
        "name_en": name_en,
        "categories": cats,
        "coordinates": {"lat": lat, "lon": lon},
        "address_vi": addr,
        "rating": rating,
        "review_summary_vi": review_vi,
        "presentation_short_vi": short_vi,
        "presentation_short_en": short_en,
        "presentation_short_ru": short_ru,
        "presentation_long_vi": long_vi,
        "presentation_long_en": long_en,
        "presentation_long_ru": long_ru,
        "highlights_vi": hi_vi,
        "highlights_en": hi_en,
        "highlights_ru": hi_ru,
        "practical": practical,
        "photo": photo,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=%s,%s&z=16&l=map" % (lon, lat),
            "google": "https://www.google.com/maps/search/?api=1&query=%s,%s" % (lat, lon),
        },
        "official_site": None,
        "sources": sources or [],
        "tags": tags,
        "status": "enriched",
        "last_updated": "2026-07-27",
    }


PLACES = []

# ================= QUẢNG TRỊ (Miền Trung) — hợp nhất Quảng Bình 1/7/2025 =================
PLACES += [
    rec(
        region="vn-quang-tri", region_name_vi="Quảng Trị", fed="Miền Trung",
        slug="dong-phong-nha", name_vi="Động Phong Nha",
        name_en="Phong Nha Cave", name_ru="Пещера Фонгня",
        cats=["park_garden", "other"], lat=17.5883, lon=106.2861,
        addr="Xã Phong Nha, tỉnh Quảng Trị (thuộc Vườn quốc gia Phong Nha – Kẻ Bàng)",
        rating={"value": 4.6, "count": 12000, "source": "Google", "as_of": "2026-07"},
        short_vi="Động Phong Nha là hang nước nổi tiếng nhất của Vườn quốc gia Phong Nha – Kẻ Bàng, Di sản Thiên nhiên Thế giới. Du khách ngồi thuyền máy ngược dòng sông Son rồi trôi vào lòng hang, chiêm ngưỡng dòng sông ngầm cùng vô số nhũ đá kỳ ảo hình thành qua hàng triệu năm.",
        short_en="Phong Nha Cave is the most famous river cave of Phong Nha – Ke Bang National Park, a UNESCO Natural World Heritage Site. Visitors board a boat up the Son River and drift into the cavern to admire an underground river and countless stalactites shaped over millions of years.",
        short_ru="Пещера Фонгня — самая знаменитая водная пещера национального парка Фонгня — Кебанг, объекта Всемирного природного наследия ЮНЕСКО. Гости плывут на лодке вверх по реке Шон и заходят в грот, любуясь подземной рекой и бесчисленными сталактитами, формировавшимися миллионы лет.",
        long_vi="Nằm bên dòng sông Son thơ mộng, Động Phong Nha là trái tim của Vườn quốc gia Phong Nha – Kẻ Bàng, khu vực karst đá vôi cổ vào loại lớn nhất châu Á và được UNESCO công nhận là Di sản Thiên nhiên Thế giới. Từ bến thuyền thị trấn Phong Nha, du khách xuôi khoảng ba mươi phút trên chiếc thuyền máy nhỏ, ngắm hai bên bờ là làng mạc, ruộng ngô và những vách núi dựng đứng, trước khi tắt máy và lặng lẽ chèo tay vào cửa hang tối. Bên trong, dòng sông ngầm dài nhiều cây số uốn lượn qua các khoang động rộng lớn; ánh đèn hắt lên trần và vách hang làm hiện ra những khối thạch nhũ, măng đá mang hình thù kỳ lạ được người xưa đặt tên như Sư Tử, Cung Đình, Đền Đài. Phong Nha từng được các nhà thám hiểm và giáo sĩ ghi chép từ cuối thế kỷ 19, và đến nay vẫn giữ nguyên vẻ huyền bí, mát lạnh quanh năm. Đây là điểm khởi đầu lý tưởng để tìm hiểu hệ thống hang động đồ sộ của vùng, trong đó có hang Sơn Đoòng lớn nhất thế giới. Trải nghiệm thuyền luồn hang trên sông ngầm là một trong những hành trình đáng nhớ nhất khi đến miền Trung Việt Nam.",
        long_en="Set on the tranquil Son River, Phong Nha Cave lies at the heart of Phong Nha – Ke Bang National Park, one of the largest ancient limestone karst regions in Asia and a UNESCO Natural World Heritage Site. From the wharf in Phong Nha town, visitors travel about thirty minutes in a small motorboat, watching villages, maize fields and sheer cliffs slip by, before the engine is cut and the boat is paddled silently into the dark cave mouth. Inside, an underground river winds for several kilometres through vast chambers; lamplight catches the ceilings and walls, revealing strange stalactites and stalagmites that earlier generations named after lions, royal courts and temples. Phong Nha was recorded by explorers and missionaries as far back as the late nineteenth century, and it still keeps its air of mystery, cool throughout the year. It is the ideal starting point for discovering the region's colossal cave systems, including Son Doong, the largest cave in the world. Gliding by boat along the subterranean river is one of the most memorable journeys in central Vietnam, blending gentle scenery on the surface with an almost otherworldly world of stone below.",
        long_ru="Расположенная на спокойной реке Шон, пещера Фонгня — сердце национального парка Фонгня — Кебанг, одного из крупнейших древних известняковых карстовых районов Азии и объекта Всемирного природного наследия ЮНЕСКО. От причала в посёлке Фонгня путешественники около тридцати минут плывут на небольшой моторной лодке, глядя, как мимо проносятся деревни, кукурузные поля и отвесные скалы, а затем мотор глушат и лодку тихо вводят вёслами в тёмный вход пещеры. Внутри подземная река тянется на несколько километров через огромные залы; свет ламп выхватывает своды и стены, открывая причудливые сталактиты и сталагмиты, которым прежние поколения дали имена львов, дворцов и храмов. Фонгня описывали исследователи и миссионеры ещё в конце XIX века, и она по сей день хранит атмосферу тайны, оставаясь прохладной круглый год. Это идеальная отправная точка для знакомства с колоссальными пещерными системами региона, включая Шондоонг — крупнейшую пещеру мира. Прогулка на лодке по подземной реке — одно из самых запоминающихся впечатлений в центральном Вьетнаме.",
        hi_vi=[
            "Hang nước biểu tượng của Di sản Thiên nhiên Thế giới Phong Nha – Kẻ Bàng (UNESCO)",
            "Thuyền máy ngược sông Son rồi chèo tay vào sông ngầm dài nhiều cây số trong lòng hang",
            "Cửa ngõ khám phá hệ thống hang động lớn bậc nhất thế giới, gồm cả hang Sơn Đoòng",
        ],
        hi_en=[
            "The iconic river cave of the Phong Nha – Ke Bang UNESCO World Heritage Site",
            "Motorboat up the Son River, then hand-paddled into a multi-kilometre underground river",
            "Gateway to one of the world's greatest cave systems, including Son Doong",
        ],
        hi_ru=[
            "Знаковая водная пещера объекта ЮНЕСКО Фонгня — Кебанг",
            "Моторная лодка вверх по реке Шон, затем на вёслах — в многокилометровую подземную реку",
            "Ворота к одной из величайших пещерных систем мира, включая Шондоонг",
        ],
        practical={
            "hours_vi": "Bến thuyền mở khoảng 7:30–16:00 hằng ngày; nên đến trước đầu giờ chiều.",
            "ticket_vi": "Vé tham quan động khoảng 150.000 VND/người; thuê thuyền tính theo nhóm (mỗi thuyền tối đa ~12 khách).",
            "duration_vi": "Khoảng 2–3 giờ (kể cả di chuyển thuyền).",
            "best_time_vi": "Mùa khô, khoảng tháng 3–8; tránh mùa mưa lũ tháng 9–11 khi nước dâng có thể đóng hang.",
            "tips_vi": "Mang áo khoác mỏng vì trong hang mát; đi giày chống trơn; ghép thuyền để tiết kiệm chi phí.",
        },
        tags=["unesco", "top", "cave", "boat", "nature", "outdoor", "daytrip"],
        review_vi="Du khách trầm trồ trước quy mô và vẻ huyền ảo của sông ngầm cùng hệ nhũ đá; nhiều người thích cảm giác yên tĩnh khi thuyền tắt máy chèo tay vào hang. Một số lưu ý mùa mưa nước lớn có thể tạm dừng đón khách và nên đi sớm để tránh đông.",
        sources=[
            {"title": "UNESCO — Phong Nha-Ke Bang National Park", "url": "https://whc.unesco.org/en/list/951/"},
            {"title": "Wikipedia (EN) — Phong Nha Cave", "url": "https://en.wikipedia.org/wiki/Phong_Nha"},
        ],
    ),
    rec(
        region="vn-quang-tri", region_name_vi="Quảng Trị", fed="Miền Trung",
        slug="dong-thien-duong", name_vi="Động Thiên Đường",
        name_en="Paradise Cave (Thien Duong Cave)", name_ru="Пещера Тхиендыонг (Райская пещера)",
        cats=["park_garden", "other"], lat=17.5196, lon=106.2228,
        addr="Vườn quốc gia Phong Nha – Kẻ Bàng, xã Phong Nha, tỉnh Quảng Trị",
        rating={"value": 4.7, "count": 15000, "source": "Google", "as_of": "2026-07"},
        short_vi="Động Thiên Đường là hang khô dài hơn 31 km, thuộc loại dài nhất châu Á, nổi tiếng với những khối thạch nhũ lộng lẫy như cung điện dưới lòng đất. Hệ thống cầu gỗ và đèn chiếu giúp du khách dạo bước khám phá khoảng một km đầu tiên đầy choáng ngợp.",
        short_en="Paradise Cave is a dry cave over 31 km long, among the longest in Asia, renowned for magnificent stalactite formations resembling an underground palace. A wooden boardwalk and soft lighting let visitors explore the awe-inspiring first kilometre.",
        short_ru="Пещера Тхиендыонг — сухая пещера длиной более 31 км, одна из самых протяжённых в Азии, знаменитая великолепными натёчными образованиями, похожими на подземный дворец. Деревянный настил и мягкая подсветка позволяют пройти впечатляющий первый километр.",
        long_vi="Được phát hiện năm 2005 và mở cửa đón khách vài năm sau đó, Động Thiên Đường nhanh chóng trở thành một trong những kỳ quan hang động được yêu thích nhất ở Vườn quốc gia Phong Nha – Kẻ Bàng. Với chiều dài đo được hơn 31 km, đây là một trong những hang khô dài nhất châu Á, tuy phần lớn dành cho các đoàn thám hiểm chuyên nghiệp. Du khách phổ thông đi bộ hoặc ngồi xe điện tới chân núi, leo bậc thang qua rừng rồi bước vào cửa hang khá nhỏ; nhưng ngay khi xuống tới lòng động, một không gian mênh mông mở ra với trần cao tới bảy tám chục mét. Hệ thống cầu gỗ dài khoảng một km dẫn lối giữa rừng thạch nhũ và măng đá trắng ngà, có khối cao như tháp, có mảng rủ mềm như rèm lụa, được chiếu sáng dịu để tôn lên vẻ đẹp mà không làm hỏng cảnh quan. Nhiệt độ trong hang mát lạnh, tương phản với cái nắng bên ngoài, khiến hành trình càng dễ chịu. Tên gọi Thiên Đường phản ánh đúng cảm nhận của những người đầu tiên đặt chân tới: một cung điện nguy nga do thiên nhiên kiến tạo trong hàng triệu năm. Đây là điểm đến gần như bắt buộc trong hành trình khám phá vương quốc hang động Quảng Bình xưa.",
        long_en="Discovered in 2005 and opened to the public a few years later, Paradise Cave quickly became one of the best-loved cave wonders of Phong Nha – Ke Bang National Park. Measured at more than 31 km, it is among the longest dry caves in Asia, though most of that length is reserved for specialist expeditions. Ordinary visitors reach the foot of the hill on foot or by electric buggy, climb a forest staircase and step through a fairly small entrance; yet the moment they descend into the cave, an immense space unfolds, with ceilings soaring seventy or eighty metres overhead. A wooden boardwalk about a kilometre long threads between forests of ivory stalactites and stalagmites, some rising like towers, others hanging soft as silk curtains, all lit gently to reveal their beauty without spoiling the scene. The cave stays cool, a welcome contrast to the heat outside, making the walk all the more pleasant. The name Paradise captures exactly what its first explorers felt: a magnificent palace sculpted by nature over millions of years. It is an almost essential stop on any journey through the cave kingdom of the former Quang Binh region.",
        long_ru="Открытая в 2005 году и принявшая туристов несколькими годами позже, пещера Тхиендыонг быстро стала одним из самых любимых чудес национального парка Фонгня — Кебанг. Её длина превышает 31 км, что делает её одной из самых протяжённых сухих пещер Азии, хотя большая часть маршрута доступна лишь специальным экспедициям. Обычные посетители добираются до подножия горы пешком или на электромобиле, поднимаются по лесной лестнице и входят через довольно небольшой вход; но стоит спуститься внутрь, как разворачивается огромное пространство со сводами высотой семьдесят-восемьдесят метров. Деревянный настил длиной около километра вьётся между лесами кремово-белых сталактитов и сталагмитов: одни вздымаются башнями, другие свисают мягко, словно шёлковые занавеси, и всё это деликатно подсвечено. В пещере прохладно, что приятно контрастирует с жарой снаружи. Название «Райская» точно передаёт чувства первых исследователей: величественный дворец, созданный природой за миллионы лет. Это почти обязательная остановка в путешествии по пещерному краю бывшей провинции Куангбинь.",
        hi_vi=[
            "Một trong những hang khô dài nhất châu Á (đo được hơn 31 km)",
            "Cầu gỗ khoảng 1 km len giữa rừng nhũ đá trắng ngà, trần hang cao tới 70–80 m",
            "Không khí mát lạnh quanh năm, được ví như cung điện dưới lòng đất",
        ],
        hi_en=[
            "One of the longest dry caves in Asia (surveyed at over 31 km)",
            "A ~1 km boardwalk amid ivory formations beneath 70–80 m high ceilings",
            "Cool year-round, likened to an underground palace",
        ],
        hi_ru=[
            "Одна из самых длинных сухих пещер Азии (более 31 км по съёмке)",
            "Настил длиной ~1 км среди кремово-белых натёков под сводами 70–80 м",
            "Прохладно круглый год; её сравнивают с подземным дворцом",
        ],
        practical={
            "hours_vi": "Mở cửa khoảng 7:00–16:30 hằng ngày.",
            "ticket_vi": "Vé vào cửa khoảng 250.000 VND/người lớn; có thể thêm phí xe điện tới chân núi.",
            "duration_vi": "Khoảng 2 giờ cho tuyến tham quan 1 km bằng cầu gỗ.",
            "best_time_vi": "Quanh năm; đẹp và ổn định nhất vào mùa khô tháng 3–8.",
            "tips_vi": "Mang giày thoải mái vì phải leo bậc; trong hang mát nên mang áo mỏng; hạn chế dùng flash để giữ cảnh quan.",
        },
        tags=["top", "cave", "nature", "outdoor", "family", "daytrip"],
        review_vi="Phần lớn du khách đánh giá đây là hang động đẹp nhất từng thấy, choáng ngợp bởi quy mô và hệ nhũ đá được chiếu sáng tinh tế. Nhiều người khuyên nên đi sớm để vắng và mát; một vài ý kiến cho rằng đoạn leo bậc lên cửa hang khá mệt với người lớn tuổi.",
        sources=[
            {"title": "Wikipedia (EN) — Thien Duong Cave", "url": "https://en.wikipedia.org/wiki/Thi%C3%AAn_%C4%90%C6%B0%E1%BB%9Dng_Cave"},
        ],
    ),
    rec(
        region="vn-quang-tri", region_name_vi="Quảng Trị", fed="Miền Trung",
        slug="phong-nha-ke-bang", name_vi="Vườn quốc gia Phong Nha – Kẻ Bàng",
        name_en="Phong Nha – Ke Bang National Park", name_ru="Национальный парк Фонгня — Кебанг",
        cats=["park_garden", "other"], lat=17.5372, lon=106.1514,
        addr="Huyện lỵ cũ Bố Trạch, nay thuộc xã Phong Nha và lân cận, tỉnh Quảng Trị",
        rating={"value": 4.7, "count": 9000, "source": "Google", "as_of": "2026-07"},
        short_vi="Phong Nha – Kẻ Bàng là Di sản Thiên nhiên Thế giới với vùng karst đá vôi khoảng 400 triệu năm tuổi, rừng nguyên sinh rậm rạp và hàng trăm hang động, trong đó có Sơn Đoòng lớn nhất hành tinh. Đây là thiên đường của người yêu thiên nhiên và thám hiểm.",
        short_en="Phong Nha – Ke Bang is a UNESCO Natural World Heritage Site with limestone karst around 400 million years old, dense primary forest and hundreds of caves, including Son Doong, the largest on Earth. It is a paradise for nature lovers and adventurers.",
        short_ru="Фонгня — Кебанг — объект Всемирного природного наследия ЮНЕСКО с известняковым карстом возрастом около 400 миллионов лет, густыми первичными лесами и сотнями пещер, включая Шондоонг, крупнейшую на Земле. Это рай для любителей природы и приключений.",
        long_vi="Trải rộng trên vùng biên giới Việt – Lào, Vườn quốc gia Phong Nha – Kẻ Bàng bảo tồn một trong những khối karst đá vôi cổ và rộng lớn nhất thế giới, hình thành cách đây khoảng 400 triệu năm. UNESCO đã hai lần ghi danh khu vực này vào Danh mục Di sản Thế giới, ghi nhận cả giá trị địa chất – địa mạo lẫn hệ sinh thái rừng nhiệt đới. Bên dưới lớp rừng thường xanh là mạng lưới hơn ba trăm hang động với tổng chiều dài hàng trăm cây số, trong đó hang Sơn Đoòng được xác nhận là hang động lớn nhất hành tinh, đủ chỗ cho cả một khu rừng và dòng sông riêng bên trong. Ngoài các hang nổi tiếng như Phong Nha, Thiên Đường, Tú Làn hay Hang Én, vườn quốc gia còn là nơi sinh sống của nhiều loài linh trưởng quý hiếm, hàng nghìn loài thực vật và những cánh rừng nguyên sinh gần như chưa bị tác động. Du khách có thể lựa chọn từ chuyến đi bộ nhẹ nhàng, chèo kayak trên sông, cho tới các tour thám hiểm nhiều ngày chinh phục hang sâu. Với cảnh quan hùng vĩ và bầu không khí hoang sơ, Phong Nha – Kẻ Bàng là điểm nhấn du lịch sinh thái hàng đầu của miền Trung Việt Nam.",
        long_en="Straddling the Vietnam-Laos border, Phong Nha – Ke Bang National Park protects one of the oldest and largest limestone karst massifs in the world, formed some 400 million years ago. UNESCO has twice inscribed the area on the World Heritage List, recognising both its geological value and its tropical forest ecosystem. Beneath the evergreen canopy lies a network of more than three hundred caves totalling hundreds of kilometres, among them Son Doong, confirmed as the largest cave on the planet, big enough to hold its own forest and river inside. Besides celebrated caves such as Phong Nha, Paradise, Tu Lan and Hang En, the park shelters rare primates, thousands of plant species and swathes of near-untouched primary forest. Visitors can choose anything from a gentle walk or a kayak trip on the river to multi-day expeditions into the deepest caverns. With its majestic scenery and wild atmosphere, Phong Nha – Ke Bang is a leading ecotourism highlight of central Vietnam, drawing scientists, cavers and travellers who want to experience one of the last great frontiers of the underground world.",
        long_ru="Раскинувшийся вдоль вьетнамско-лаосской границы национальный парк Фонгня — Кебанг охраняет один из древнейших и крупнейших известняковых карстовых массивов мира, сформировавшийся около 400 миллионов лет назад. ЮНЕСКО дважды вносила эту территорию в Список Всемирного наследия, признавая как её геологическую ценность, так и экосистему тропического леса. Под вечнозелёным пологом скрывается сеть из более чем трёхсот пещер общей протяжённостью в сотни километров, среди которых Шондоонг — крупнейшая пещера планеты, вмещающая собственный лес и реку. Помимо знаменитых пещер Фонгня, Тхиендыонг, Тулан и Хангэн, парк служит домом для редких приматов, тысяч видов растений и почти нетронутых первичных лесов. Путешественники могут выбрать что угодно — от лёгкой прогулки или сплава на каяке до многодневных экспедиций в глубочайшие гроты. Благодаря величественным пейзажам и дикой атмосфере Фонгня — Кебанг остаётся ведущим центром экотуризма центрального Вьетнама.",
        hi_vi=[
            "Karst đá vôi khoảng 400 triệu năm tuổi — hai lần được UNESCO ghi danh Di sản Thế giới",
            "Hơn 300 hang động, gồm Sơn Đoòng — hang lớn nhất hành tinh",
            "Rừng nguyên sinh với nhiều loài linh trưởng và thực vật quý hiếm",
        ],
        hi_en=[
            "Limestone karst ~400 million years old — twice inscribed by UNESCO",
            "Over 300 caves, including Son Doong, the largest cave on Earth",
            "Primary forest sheltering rare primates and plant species",
        ],
        hi_ru=[
            "Известняковый карст возрастом ~400 млн лет — дважды в списке ЮНЕСКО",
            "Более 300 пещер, включая Шондоонг — крупнейшую пещеру Земли",
            "Первичные леса с редкими приматами и видами растений",
        ],
        practical={
            "hours_vi": "Khu trung tâm và các tuyến hang mở ban ngày; tour thám hiểm đặt trước theo lịch.",
            "ticket_vi": "Vé tùy điểm; các hang phổ thông 150.000–250.000 VND, tour thám hiểm chuyên sâu giá cao và phải đặt trước.",
            "duration_vi": "Từ nửa ngày (hang phổ thông) đến nhiều ngày (tour Sơn Đoòng, Tú Làn).",
            "best_time_vi": "Mùa khô tháng 2–8; các tour hang lớn thường chỉ chạy ngoài mùa mưa lũ.",
            "tips_vi": "Đặt tour thám hiểm sớm qua đơn vị được cấp phép; chuẩn bị thể lực; tuân thủ hướng dẫn bảo tồn.",
        },
        tags=["unesco", "top", "nature", "cave", "outdoor", "hiking", "daytrip"],
        review_vi="Được ca ngợi là vùng hang động và rừng nguyên sinh đẳng cấp thế giới; du khách thích sự đa dạng trải nghiệm từ nhẹ nhàng đến mạo hiểm. Nhiều người nhấn mạnh nên đặt tour hang qua đơn vị uy tín và đi đúng mùa khô để an toàn.",
        sources=[
            {"title": "UNESCO — Phong Nha-Ke Bang National Park", "url": "https://whc.unesco.org/en/list/951/"},
            {"title": "Wikipedia (EN) — Phong Nha-Ke Bang National Park", "url": "https://en.wikipedia.org/wiki/Phong_Nha%E2%80%93K%E1%BA%BB_B%C3%A0ng_National_Park"},
        ],
    ),
]

# ================= CẦN THƠ (Miền Nam) — TP trực thuộc TW, hợp nhất Hậu Giang + Sóc Trăng =================
PLACES += [
    rec(
        region="vn-can-tho", region_name_vi="Cần Thơ", fed="Miền Nam",
        slug="cho-noi-cai-rang", name_vi="Chợ nổi Cái Răng",
        name_en="Cai Rang Floating Market", name_ru="Плавучий рынок Кайранг",
        cats=["square_street", "other"], lat=10.0369, lon=105.7503,
        addr="Sông Cần Thơ, quận Cái Răng, TP. Cần Thơ",
        rating={"value": 4.4, "count": 14000, "source": "Google", "as_of": "2026-07"},
        short_vi="Chợ nổi Cái Răng là chợ đầu mối trên sông lớn và nổi tiếng nhất miền Tây Nam Bộ. Từ sáng sớm, hàng trăm ghe thuyền tụ họp mua bán nông sản, mỗi ghe treo 'cây bẹo' cắm sản vật để rao hàng — một nét văn hóa sông nước độc đáo của đồng bằng sông Cửu Long.",
        short_en="Cai Rang is the largest and most famous floating wholesale market in Vietnam's Mekong Delta. From dawn, hundreds of boats gather to trade produce, each hanging a tall 'beo' pole displaying its goods, a distinctive river culture of the delta.",
        short_ru="Кайранг — крупнейший и самый известный плавучий оптовый рынок дельты Меконга. С рассвета сотни лодок собираются торговать продуктами; на каждой поднят высокий шест «бео» с образцами товара — самобытная речная культура дельты.",
        long_vi="Cách trung tâm Cần Thơ khoảng sáu cây số, Chợ nổi Cái Răng họp ngay trên khúc sông rộng và là biểu tượng của đời sống thương hồ vùng đồng bằng sông Cửu Long. Chợ nhộn nhịp nhất từ khoảng năm giờ đến tám giờ sáng, khi hàng trăm chiếc ghe bầu chở đầy dưa hấu, khóm, khoai, bí, cam quýt từ khắp các tỉnh miền Tây tụ về trao đổi sỉ. Điểm thú vị nhất là 'cây bẹo' — một cây sào dài dựng trước mũi ghe, treo lủng lẳng thứ nông sản mà chủ ghe muốn bán, để người mua từ xa đã biết nên ghé thuyền nào. Xen giữa những chiếc ghe lớn là các xuồng con bán cà phê, hủ tiếu, bún riêu, trái cây, len lỏi phục vụ tận nơi; du khách có thể ngồi trên thuyền, thưởng thức tô hủ tiếu nóng giữa sông nước bồng bềnh trong ánh bình minh. Để cảm nhận trọn vẹn, khách thường thuê thuyền từ bến Ninh Kiều đi từ tờ mờ sáng, vừa ngắm cảnh sinh hoạt vừa tìm hiểu nếp buôn bán đã tồn tại cả trăm năm. Dù giao thông đường bộ ngày càng phát triển khiến quy mô chợ có phần thu hẹp, Cái Răng vẫn là trải nghiệm văn hóa sông nước không thể bỏ qua khi tới Cần Thơ.",
        long_en="About six kilometres from central Can Tho, Cai Rang Floating Market convenes on a broad stretch of river and is a symbol of the trading life of the Mekong Delta. It is busiest from around five to eight in the morning, when hundreds of heavy boats laden with watermelons, pineapples, sweet potatoes, pumpkins and citrus arrive from across the western provinces to trade wholesale. The most charming detail is the 'beo' pole, a tall bamboo mast raised at each boat's prow from which the owner hangs a sample of whatever is for sale, so buyers can spot the right vessel from afar. Weaving between the large boats are small sampans selling coffee, noodle soup and fruit, serving customers on the water; visitors can sit aboard and enjoy a steaming bowl of noodles amid the gentle bustle at sunrise. To experience it fully, travellers usually hire a boat from Ninh Kieu wharf before dawn, watching daily life unfold while learning about a way of trading that has endured for a century. Although better roads have shrunk the market somewhat, Cai Rang remains an essential taste of delta river culture.",
        long_ru="Примерно в шести километрах от центра Кантхо плавучий рынок Кайранг раскинулся на широком участке реки и служит символом торговой жизни дельты Меконга. Наиболее оживлён он с пяти до восьми утра, когда сотни тяжёлых лодок, гружённых арбузами, ананасами, бататом, тыквой и цитрусовыми, съезжаются со всех западных провинций для оптовой торговли. Самая колоритная деталь — шест «бео»: высокая бамбуковая мачта на носу лодки, на которую хозяин вешает образец товара, чтобы покупатели издалека узнавали нужное судно. Между крупными лодками снуют маленькие сампаны, торгующие кофе, супом с лапшой и фруктами прямо на воде; гости могут сидеть в лодке и есть горячую лапшу среди мягкой суеты на рассвете. Чтобы прочувствовать колорит, путешественники обычно нанимают лодку у причала Нинькьеу до рассвета. Хотя развитие дорог несколько уменьшило рынок, Кайранг остаётся обязательным знакомством с речной культурой дельты.",
        hi_vi=[
            "Chợ nổi trên sông lớn và nổi tiếng nhất miền Tây Nam Bộ",
            "Nét độc đáo 'cây bẹo' — treo sản vật lên sào để rao bán từ xa",
            "Ăn sáng trên thuyền (hủ tiếu, cà phê) giữa cảnh mua bán lúc bình minh",
        ],
        hi_en=[
            "The largest, most famous floating market of the Mekong Delta",
            "The distinctive 'beo' pole displaying goods for sale from afar",
            "Breakfast on a boat (noodle soup, coffee) amid the sunrise trade",
        ],
        hi_ru=[
            "Крупнейший и самый известный плавучий рынок дельты Меконга",
            "Самобытный шест «бео» с образцами товара, видимыми издалека",
            "Завтрак прямо в лодке (лапша, кофе) среди рассветной торговли",
        ],
        practical={
            "hours_vi": "Đông vui nhất khoảng 5:00–8:00 sáng; sau 9:00 chợ thưa dần.",
            "ticket_vi": "Miễn phí tham quan; chi phí chính là thuê thuyền, tham khảo 400.000–700.000 VND/thuyền tùy cỡ và tuyến.",
            "duration_vi": "Khoảng 2–3 giờ cả đi và về từ bến Ninh Kiều.",
            "best_time_vi": "Sáng sớm, đặc biệt mùa trái cây (khoảng tháng 5–8); nên đi khi trời còn mát.",
            "tips_vi": "Khởi hành từ 5:00–5:30 để kịp lúc chợ đông; mang mũ, áo phao; đổi tiền lẻ để mua đồ trên thuyền.",
        },
        tags=["top", "market", "boat", "culture", "food", "outdoor", "sunrise"],
        review_vi="Du khách thích không khí sông nước sống động lúc bình minh và trải nghiệm ăn sáng, uống cà phê ngay trên thuyền. Nhiều người khuyên đi thật sớm vì chợ tan nhanh; một số nhận xét chợ nhỏ hơn xưa do vận tải đường bộ phát triển.",
        sources=[
            {"title": "Wikipedia (EN) — Cai Rang Floating Market", "url": "https://en.wikipedia.org/wiki/Cai_Rang_Floating_Market"},
        ],
    ),
    rec(
        region="vn-can-tho", region_name_vi="Cần Thơ", fed="Miền Nam",
        slug="ben-ninh-kieu", name_vi="Bến Ninh Kiều",
        name_en="Ninh Kieu Wharf", name_ru="Набережная Нинькьеу",
        cats=["park_garden", "square_street"], lat=10.0339, lon=105.7887,
        addr="Đường Hai Bà Trưng, bên sông Hậu, trung tâm TP. Cần Thơ",
        rating={"value": 4.4, "count": 20000, "source": "Google", "as_of": "2026-07"},
        short_vi="Bến Ninh Kiều là công viên và bến tàu ven sông Hậu, trái tim của thành phố Cần Thơ. Về đêm, khu bến rực rỡ ánh đèn, có cầu đi bộ Ninh Kiều, tượng đài Bác Hồ, chợ đêm và những chuyến du thuyền nghe đờn ca tài tử trên sông.",
        short_en="Ninh Kieu Wharf is a riverside park and boat pier on the Hau River, the heart of Can Tho city. By night it glows with lights, featuring the Ninh Kieu pedestrian bridge, a statue of Ho Chi Minh, a night market and dinner cruises with traditional southern music.",
        short_ru="Набережная Нинькьеу — прибрежный парк и причал на реке Хау, сердце города Кантхо. По вечерам она сияет огнями: пешеходный мост Нинькьеу, памятник Хо Ши Мину, ночной рынок и прогулочные ужины-круизы под традиционную южную музыку.",
        long_vi="Nằm nơi sông Cần Thơ đổ ra sông Hậu, Bến Ninh Kiều từ lâu đã là biểu tượng và không gian sinh hoạt công cộng được yêu thích nhất của thành phố Cần Thơ. Ban ngày, công viên bến rợp bóng cây, có tượng đài Chủ tịch Hồ Chí Minh uy nghi hướng ra dòng sông tấp nập ghe thuyền. Khi chiều buông, nơi đây trở nên nhộn nhịp: người dân và du khách dạo mát, chụp ảnh bên cầu đi bộ Ninh Kiều hình chữ S uốn lượn qua một nhánh sông, lung linh sắc đèn đổi màu. Dọc bến là các nhà hàng nổi, quán cà phê và khu chợ đêm bày bán đặc sản miền Tây cùng đồ lưu niệm. Nhiều du khách chọn lên du thuyền ăn tối, vừa trôi trên sông Hậu vừa thưởng thức đờn ca tài tử — loại hình âm nhạc dân gian Nam Bộ đã được UNESCO ghi danh. Bến Ninh Kiều cũng là điểm xuất phát quen thuộc của các chuyến thuyền đi chợ nổi Cái Răng từ sáng sớm. Với vị trí trung tâm, khung cảnh sông nước hữu tình và bầu không khí thân thiện, bến sông này gói trọn nhịp sống phóng khoáng, hào sảng của thủ phủ miền Tây.",
        long_en="Set where the Can Tho River meets the Hau River, Ninh Kieu Wharf has long been the emblem and favourite public space of Can Tho city. By day the riverside park is shaded by trees, with a dignified statue of President Ho Chi Minh facing a river busy with boats. As evening falls the area comes alive: residents and visitors stroll and take photos by the S-shaped Ninh Kieu pedestrian bridge, which curves across a river branch aglow with colour-changing lights. Along the wharf are floating restaurants, cafes and a night market selling delta specialities and souvenirs. Many travellers board a dinner cruise, drifting on the Hau River while enjoying don ca tai tu, the southern folk music honoured by UNESCO. Ninh Kieu is also the usual departure point for early-morning boats to Cai Rang Floating Market. With its central location, gentle river scenery and friendly atmosphere, this waterfront captures the open, generous spirit of the delta's capital, and is the natural place to begin or end a day exploring Can Tho.",
        long_ru="Расположенная там, где река Кантхо впадает в реку Хау, набережная Нинькьеу давно стала эмблемой и любимым общественным пространством города Кантхо. Днём прибрежный парк укрыт тенью деревьев, а величественный памятник президенту Хо Ши Мину обращён к реке, полной лодок. С наступлением вечера здесь оживает жизнь: местные жители и туристы прогуливаются и фотографируются у S-образного пешеходного моста Нинькьеу, который изгибается над рукавом реки, сияя меняющими цвет огнями. Вдоль набережной — плавучие рестораны, кафе и ночной рынок с деликатесами дельты и сувенирами. Многие путешественники отправляются на ужин-круиз по реке Хау, слушая донкатайты — южную народную музыку, признанную ЮНЕСКО. Отсюда же ранним утром отходят лодки к плавучему рынку Кайранг. Благодаря центральному положению, мягким речным пейзажам и дружелюбной атмосфере эта набережная передаёт открытый, щедрый дух столицы дельты.",
        hi_vi=[
            "Bến sông và công viên biểu tượng ngay trung tâm Cần Thơ, có tượng đài Bác Hồ",
            "Cầu đi bộ Ninh Kiều hình chữ S lung linh ánh đèn về đêm",
            "Điểm lên du thuyền ăn tối, nghe đờn ca tài tử và xuất phát đi chợ nổi",
        ],
        hi_en=[
            "The emblematic riverside park in central Can Tho, with a statue of Ho Chi Minh",
            "The S-shaped Ninh Kieu pedestrian bridge glowing at night",
            "Departure point for dinner cruises, folk music and floating-market trips",
        ],
        hi_ru=[
            "Знаковый прибрежный парк в центре Кантхо с памятником Хо Ши Мину",
            "S-образный пешеходный мост Нинькьеу, сияющий по ночам",
            "Отправная точка ужинов-круизов, народной музыки и поездок на плавучий рынок",
        ],
        practical={
            "hours_vi": "Không gian công cộng mở cả ngày; đẹp và nhộn nhịp nhất vào buổi tối.",
            "ticket_vi": "Miễn phí; chi phí tùy chọn cho du thuyền ăn tối, chợ đêm hoặc cầu đi bộ.",
            "duration_vi": "Khoảng 1–2 giờ dạo bộ; thêm 1–2 giờ nếu đi du thuyền.",
            "best_time_vi": "Buổi tối mát mẻ, nhất là dịp cuối tuần khi có nhiều hoạt động.",
            "tips_vi": "Kết hợp ăn tối du thuyền rồi sáng hôm sau đi chợ nổi Cái Răng; giữ gìn tư trang nơi đông người.",
        },
        tags=["free", "night", "riverside", "family", "walk", "photo-spot"],
        review_vi="Du khách thấy đây là nơi thư giãn dễ chịu, lên đèn đẹp và tiện ăn uống, mua sắm. Cầu đi bộ và du thuyền được khen; một số ý kiến nói khu vực khá đông và có mời chào dịch vụ, nên thong thả và hỏi giá trước.",
        sources=[
            {"title": "Wikipedia (VI) — Bến Ninh Kiều", "url": "https://vi.wikipedia.org/wiki/B%E1%BA%BFn_Ninh_Ki%E1%BB%81u"},
        ],
    ),
    rec(
        region="vn-can-tho", region_name_vi="Cần Thơ", fed="Miền Nam",
        slug="nha-co-binh-thuy", name_vi="Nhà cổ Bình Thủy",
        name_en="Binh Thuy Ancient House", name_ru="Старинный дом Биньтхюи",
        cats=["other", "monument"], lat=10.0631, lon=105.7369,
        addr="Đường Bùi Hữu Nghĩa, phường Bình Thủy, TP. Cần Thơ",
        rating={"value": 4.4, "count": 3500, "source": "Google", "as_of": "2026-07"},
        short_vi="Nhà cổ Bình Thủy là ngôi nhà của dòng họ Dương xây từ cuối thế kỷ 19 – đầu thế kỷ 20, kết hợp kiến trúc Đông – Tây độc đáo. Ngôi nhà được bảo tồn nguyên vẹn với nội thất cổ và từng là bối cảnh của phim 'Người tình' (L'Amant).",
        short_en="Binh Thuy Ancient House is the home of the Duong family, built in the late 19th to early 20th century in a distinctive blend of Eastern and Western architecture. Beautifully preserved with antique interiors, it served as a setting for the film 'The Lover' (L'Amant).",
        short_ru="Старинный дом Биньтхюи — усадьба семьи Зыонг, построенная в конце XIX — начале XX века в самобытном сочетании восточной и западной архитектуры. Прекрасно сохранившийся, с антикварными интерьерами, он стал декорацией фильма «Любовник» (L'Amant).",
        long_vi="Tọa lạc trong khu vườn rợp bóng cây ở phường Bình Thủy, ngôi nhà cổ của dòng họ Dương là một trong những kiến trúc nhà vườn Nam Bộ đẹp và được gìn giữ tốt nhất còn lại đến ngày nay. Được khởi dựng khoảng cuối thế kỷ 19 và hoàn thiện những năm đầu thế kỷ 20, ngôi nhà thể hiện lối sống của tầng lớp điền chủ giàu có miền Tây thời Pháp thuộc, nơi văn hóa Á Đông giao hòa với thẩm mỹ phương Tây. Mặt tiền mang phong cách Pháp với vòm cong, hoa văn đắp nổi và cầu thang cánh cung, trong khi bên trong lại bài trí theo truyền thống Việt: gian thờ trang nghiêm, bộ liễn đối sơn son thếp vàng, sập gụ, tủ chè và những món đồ gỗ chạm khắc tinh xảo cùng gạch bông nhập từ Pháp. Khu vườn quanh nhà trồng lan, xương rồng và nhiều cây cảnh quý mà gia chủ dày công sưu tầm. Nhờ vẻ đẹp cổ kính và không khí hoài niệm, ngôi nhà đã được chọn làm bối cảnh cho bộ phim điện ảnh nổi tiếng 'Người tình' cùng nhiều tác phẩm khác. Ngày nay con cháu họ Dương vẫn sinh sống và đón khách tham quan, giúp du khách hình dung sinh động về nếp nhà và đời sống thượng lưu vùng đồng bằng sông Cửu Long hơn một thế kỷ trước.",
        long_en="Standing in a shady garden in Binh Thuy ward, the ancient house of the Duong family is one of the finest and best-preserved southern garden houses still surviving. Begun in the late nineteenth century and completed in the early twentieth, it reflects the lifestyle of the wealthy delta landowning class during the French colonial era, where East Asian culture blended with Western taste. The facade is French in spirit, with arches, moulded ornament and a curved staircase, while the interior follows Vietnamese tradition: a solemn ancestral altar, gilded parallel sentences, precious hardwood daybeds and cabinets, intricately carved furniture and patterned tiles imported from France. The surrounding garden is planted with orchids, cacti and rare ornamental plants painstakingly collected by the owners. Thanks to its timeless beauty and nostalgic atmosphere, the house was chosen as a setting for the celebrated film 'The Lover' and several other productions. Today descendants of the Duong family still live here and welcome visitors, helping travellers picture vividly the domestic customs and upper-class life of the Mekong Delta more than a century ago.",
        long_ru="Стоящий в тенистом саду в квартале Биньтхюи старинный дом семьи Зыонг — одна из лучших и наиболее сохранившихся южных усадеб-садов. Начатый в конце XIX века и завершённый в начале XX, он отражает быт богатого землевладельческого сословия дельты во французскую колониальную эпоху, когда восточноазиатская культура сочеталась с западным вкусом. Фасад выдержан во французском духе — с арками, лепниной и изогнутой лестницей, тогда как интерьер следует вьетнамской традиции: торжественный алтарь предков, позолоченные парные надписи, драгоценные лежанки и шкафы из твёрдых пород дерева, тонко резная мебель и узорчатая плитка, привезённая из Франции. В саду вокруг растут орхидеи, кактусы и редкие декоративные растения, кропотливо собранные хозяевами. Благодаря вневременной красоте и ностальгической атмосфере дом стал декорацией знаменитого фильма «Любовник» и ряда других лент. Сегодня потомки семьи Зыонг по-прежнему живут здесь и принимают гостей.",
        hi_vi=[
            "Nhà vườn Nam Bộ hơn 100 năm tuổi, giao thoa kiến trúc Pháp và truyền thống Việt",
            "Nội thất cổ quý: sập gụ, tủ chè, liễn đối thếp vàng, gạch bông nhập từ Pháp",
            "Bối cảnh của phim điện ảnh 'Người tình' (L'Amant)",
        ],
        hi_en=[
            "A 100-year-old southern garden house blending French and Vietnamese styles",
            "Antique interiors: hardwood daybeds, gilded couplets, French tiles",
            "A filming location for the movie 'The Lover' (L'Amant)",
        ],
        hi_ru=[
            "Столетняя южная усадьба-сад, сочетающая французский и вьетнамский стили",
            "Антикварные интерьеры: лежанки, позолоченные надписи, французская плитка",
            "Место съёмок фильма «Любовник» (L'Amant)",
        ],
        practical={
            "hours_vi": "Mở cửa đón khách khoảng 8:00–18:00 hằng ngày.",
            "ticket_vi": "Vé tham quan khoảng 15.000–20.000 VND/người.",
            "duration_vi": "Khoảng 30–45 phút.",
            "best_time_vi": "Buổi sáng mát; kết hợp khi tham quan khu Bình Thủy, chùa và đình lân cận.",
            "tips_vi": "Ăn mặc lịch sự khi vào gian thờ; xin phép trước khi chụp ảnh nội thất; giữ yên tĩnh vì gia chủ vẫn sinh sống.",
        },
        tags=["historic", "architecture", "photo-spot", "culture", "indoor"],
        review_vi="Du khách yêu thích nét cổ kính, đồ nội thất được giữ gìn công phu và câu chuyện dòng họ được chủ nhà kể lại. Vài ý kiến cho rằng nhà nằm hơi khuất, nên dùng bản đồ; không gian không quá lớn nên phù hợp ghé nhanh kết hợp điểm khác.",
        sources=[
            {"title": "Wikipedia (VI) — Nhà cổ Bình Thủy", "url": "https://vi.wikipedia.org/wiki/Nh%C3%A0_c%E1%BB%95_B%C3%ACnh_Th%E1%BB%A7y"},
        ],
    ),
]

# ================= GIA LAI (Miền Trung) — hợp nhất Bình Định 1/7/2025, tỉnh lỵ Quy Nhơn =================
PLACES += [
    rec(
        region="vn-gia-lai", region_name_vi="Gia Lai", fed="Miền Trung",
        slug="bien-ho", name_vi="Biển Hồ (Hồ T'Nưng)",
        name_en="Bien Ho Lake (T'Nung Lake)", name_ru="Озеро Бьенхо (Тынынг)",
        cats=["park_garden", "other"], lat=14.0525, lon=108.0064,
        addr="Xã Biển Hồ, TP. Pleiku, tỉnh Gia Lai",
        rating={"value": 4.5, "count": 6000, "source": "Google", "as_of": "2026-07"},
        short_vi="Biển Hồ, hay hồ T'Nưng, là hồ nước ngọt tự nhiên nằm trong miệng núi lửa đã tắt trên cao nguyên Pleiku. Mặt hồ trong xanh, phẳng lặng giữa rừng thông và đồi chè, được ví như 'đôi mắt Pleiku' và là biểu tượng thiên nhiên của Tây Nguyên.",
        short_en="Bien Ho, or T'Nung Lake, is a natural freshwater lake set in the crater of an extinct volcano on the Pleiku plateau. Its clear, calm waters amid pine forest and tea hills are likened to 'the eyes of Pleiku' and are a natural emblem of the Central Highlands.",
        short_ru="Бьенхо, или озеро Тынынг, — природное пресноводное озеро в кратере потухшего вулкана на плато Плейку. Его чистые спокойные воды среди сосновых лесов и чайных холмов называют «глазами Плейку»; это природный символ Центрального нагорья.",
        long_vi="Cách trung tâm thành phố Pleiku khoảng bảy cây số về phía bắc, Biển Hồ là một trong những thắng cảnh nổi tiếng nhất của vùng đất đỏ bazan Tây Nguyên. Đây thực chất là hồ nước ngọt hình thành trong miệng của những ngọn núi lửa đã ngừng hoạt động từ hàng triệu năm trước, nay nối thông thành một mặt nước rộng lớn, quanh năm xanh trong và hiếm khi cạn. Người Gia Rai bản địa gọi hồ là T'Nưng và lưu truyền nhiều truyền thuyết gắn với nguồn gốc của nó. Do nằm ở độ cao khoảng tám trăm mét, khí hậu quanh hồ mát mẻ dễ chịu; những rặng thông reo trong gió, đồi chè xanh mướt và con đường nhỏ dẫn ra đài vọng cảnh tạo nên khung cảnh nên thơ khiến nơi đây được ví von là 'đôi mắt Pleiku'. Du khách thường tản bộ dọc bờ hồ, phóng tầm mắt ra mặt nước mênh mông phản chiếu mây trời, hoặc ghé thăm hàng thông trăm tuổi và những vườn chè, vườn cà phê lân cận. Buổi sáng sớm sương giăng và lúc hoàng hôn là những thời khắc đẹp nhất. Yên bình, khoáng đạt và đậm chất cao nguyên, Biển Hồ là điểm dừng chân lý tưởng để cảm nhận thiên nhiên và bản sắc của Gia Lai.",
        long_en="About seven kilometres north of Pleiku city, Bien Ho is one of the best-known scenic spots of the red-basalt Central Highlands. It is in fact a freshwater lake formed in the craters of volcanoes that fell silent millions of years ago, now joined into a broad expanse of water that stays clear year-round and rarely runs low. The indigenous Jarai people call it T'Nung and pass down many legends about its origin. Lying at around eight hundred metres altitude, the lake enjoys a cool, pleasant climate; whispering pines, emerald tea hills and a small road leading to a viewing platform create a poetic scene that has earned it the nickname 'the eyes of Pleiku'. Visitors usually stroll along the shore, gazing over the vast water that mirrors the sky, or visit the century-old pines and nearby tea and coffee gardens. Early mornings wreathed in mist and the hour of sunset are the most beautiful times. Peaceful, open and thoroughly highland in character, Bien Ho is an ideal stop to feel the nature and identity of Gia Lai.",
        long_ru="Примерно в семи километрах к северу от города Плейку Бьенхо — одно из самых известных живописных мест краснозёмного Центрального нагорья. По сути это пресноводное озеро, образовавшееся в кратерах вулканов, умолкших миллионы лет назад, и слившееся в широкую водную гладь, которая остаётся чистой круглый год и почти не мелеет. Коренной народ джарай называет его Тынынг и хранит множество легенд о его происхождении. На высоте около восьмисот метров у озера прохладный, приятный климат; шелестящие сосны, изумрудные чайные холмы и небольшая дорога к смотровой площадке создают поэтичную картину, за которую его прозвали «глазами Плейку». Гости обычно прогуливаются по берегу, любуясь широкой водой, отражающей небо, или посещают вековые сосны и соседние чайные и кофейные сады. Раннее туманное утро и час заката — самые красивые мгновения. Спокойное, открытое и по-настоящему нагорное, озеро Бьенхо — идеальная остановка, чтобы прочувствовать природу и самобытность Гиалай.",
        hi_vi=[
            "Hồ nước ngọt trong miệng núi lửa cổ trên cao nguyên Pleiku",
            "Được ví như 'đôi mắt Pleiku', biểu tượng thiên nhiên của Tây Nguyên",
            "Khí hậu mát mẻ, hàng thông trăm tuổi và đồi chè bao quanh",
        ],
        hi_en=[
            "A freshwater lake in an ancient volcanic crater on the Pleiku plateau",
            "Nicknamed 'the eyes of Pleiku', a natural emblem of the highlands",
            "Cool climate with century-old pines and surrounding tea hills",
        ],
        hi_ru=[
            "Пресноводное озеро в древнем вулканическом кратере на плато Плейку",
            "Прозвано «глазами Плейку», природный символ нагорья",
            "Прохладный климат, вековые сосны и чайные холмы вокруг",
        ],
        practical={
            "hours_vi": "Tham quan ban ngày, tự do; đẹp nhất sáng sớm và hoàng hôn.",
            "ticket_vi": "Miễn phí (một số khu vực dịch vụ có thể thu phí nhỏ).",
            "duration_vi": "Khoảng 1–1,5 giờ dạo và ngắm cảnh.",
            "best_time_vi": "Mùa khô tháng 11–4; buổi sáng có sương và hoàng hôn rất đẹp.",
            "tips_vi": "Mang áo khoác nhẹ vì buổi sáng se lạnh; kết hợp thăm đồi chè Biển Hồ và các vườn cà phê gần đó.",
        },
        tags=["free", "nature", "lake", "viewpoint", "outdoor", "photo-spot"],
        review_vi="Du khách khen cảnh hồ yên bình, không khí trong lành và view đẹp từ đài vọng cảnh. Nhiều người thích đi sáng sớm khi mặt hồ phủ sương; một số lưu ý dịch vụ ăn uống quanh hồ còn ít nên nên chuẩn bị nước và đồ nhẹ.",
        sources=[
            {"title": "Wikipedia (EN) — Pleiku Lake", "url": "https://en.wikipedia.org/wiki/Pleiku_Lake"},
        ],
    ),
    rec(
        region="vn-gia-lai", region_name_vi="Gia Lai", fed="Miền Trung",
        slug="ky-co", name_vi="Bãi biển Kỳ Co",
        name_en="Ky Co Beach", name_ru="Пляж Кико",
        cats=["park_garden", "other"], lat=13.6842, lon=109.3436,
        addr="Bán đảo Nhơn Lý, TP. Quy Nhơn, tỉnh Gia Lai",
        rating={"value": 4.6, "count": 8000, "source": "Google", "as_of": "2026-07"},
        short_vi="Kỳ Co là bãi biển tuyệt đẹp trên bán đảo Nhơn Lý gần Quy Nhơn, nổi tiếng với làn nước hai màu xanh ngọc và xanh lam, bãi cát trắng mịn cùng vách núi đá bao quanh. Du khách thường đi ca nô vượt sóng hoặc cáp treo để tới vịnh biển hoang sơ này.",
        short_en="Ky Co is a stunning beach on the Nhon Ly peninsula near Quy Nhon, famed for its two-tone turquoise and blue water, fine white sand and encircling rock cliffs. Visitors usually reach this pristine cove by speedboat over the waves or by cable car.",
        short_ru="Кико — потрясающий пляж на полуострове Нёнли близ Куинёна, известный двухцветной бирюзово-синей водой, мелким белым песком и обрамляющими скалами. К этой нетронутой бухте обычно добираются на скоростном катере по волнам или по канатной дороге.",
        long_vi="Nằm ở bán đảo Nhơn Lý, cách trung tâm Quy Nhơn chừng hai mươi lăm cây số, Kỳ Co được nhiều du khách xem là một trong những bãi biển đẹp nhất miền Trung Việt Nam. Vịnh biển nhỏ này lọt thỏm giữa những dãy núi đá granite, tạo nên khung cảnh vừa hùng vĩ vừa nên thơ. Điều làm nên tên tuổi của Kỳ Co là màu nước độc đáo: gần bờ nước trong veo ánh lên sắc xanh ngọc bích, xa hơn chuyển sang xanh lam thẫm, còn bãi cát thì trắng mịn và thoai thoải. Khi thủy triều xuống, nhiều hồ nước nông ấm áp lộ ra giữa các ghềnh đá, trở thành nơi tắm và ngâm mình lý tưởng. Du khách có thể tới Kỳ Co bằng hai cách thú vị: ngồi ca nô phóng qua sóng biển men theo vách đá, hoặc đi tuyến cáp treo ngắm toàn cảnh vịnh từ trên cao. Kề bên là Eo Gió nổi tiếng, nên hai điểm thường được ghép trong cùng một hành trình khám phá vùng biển Quy Nhơn. Với vẻ hoang sơ, nước trong và bãi cát đẹp, Kỳ Co là thiên đường cho những ai yêu thích tắm biển, lặn ngắm san hô và chụp ảnh giữa thiên nhiên khoáng đạt của xứ 'đất võ trời văn'.",
        long_en="On the Nhon Ly peninsula, about twenty-five kilometres from central Quy Nhon, Ky Co is regarded by many travellers as one of the most beautiful beaches in central Vietnam. This small cove nestles among granite mountains, creating a scene at once grand and idyllic. What made Ky Co famous is its unusual water colour: near the shore it is crystal clear with a jade-green tint, further out it deepens to blue, while the sand is fine, white and gently sloping. At low tide, warm shallow pools appear among the rocks, perfect for bathing. Visitors can reach Ky Co in two exciting ways: by speedboat racing over the waves along the cliffs, or by cable car offering a panorama of the bay from above. The renowned Eo Gio lies close by, so the two are usually combined in one trip exploring the Quy Nhon coast. With its pristine feel, clear water and lovely sand, Ky Co is a paradise for swimming, snorkelling over coral and photography amid the open nature of Binh Dinh, the land long known for its martial arts and scholars.",
        long_ru="На полуострове Нёнли, примерно в двадцати пяти километрах от центра Куинёна, Кико многие путешественники считают одним из красивейших пляжей центрального Вьетнама. Эта небольшая бухта укрыта среди гранитных гор, создавая одновременно величественную и идиллическую картину. Славу Кико принёс необычный цвет воды: у берега она кристально прозрачна с нефритово-зелёным оттенком, дальше темнеет до синевы, а песок мелкий, белый и пологий. При отливе среди скал появляются тёплые мелкие лагуны, идеальные для купания. Добраться до Кико можно двумя увлекательными способами: на скоростном катере, мчащемся по волнам вдоль скал, или по канатной дороге с панорамой залива сверху. Рядом расположен знаменитый Эозо, поэтому эти два места обычно объединяют в одну поездку по побережью Куинёна. Благодаря нетронутости, чистой воде и прекрасному песку Кико — рай для купания, снорклинга над кораллами и фотографии.",
        hi_vi=[
            "Bãi biển hoang sơ với nước hai màu xanh ngọc và xanh lam đặc trưng",
            "Đến bằng ca nô vượt sóng hoặc cáp treo ngắm toàn cảnh vịnh",
            "Ghép cùng Eo Gió thành tuyến khám phá biển Quy Nhơn",
        ],
        hi_en=[
            "A pristine beach with signature two-tone jade and blue water",
            "Reached by speedboat over the waves or by scenic cable car",
            "Often combined with nearby Eo Gio on the Quy Nhon coast",
        ],
        hi_ru=[
            "Нетронутый пляж с фирменной двухцветной нефритово-синей водой",
            "Добираются на катере по волнам или по живописной канатной дороге",
            "Часто объединяют с соседним Эозо на побережье Куинёна",
        ],
        practical={
            "hours_vi": "Đón khách ban ngày, thường 7:00–17:00; phụ thuộc thời tiết và lịch ca nô.",
            "ticket_vi": "Combo ca nô/cáp treo + vé bãi tham khảo khoảng 200.000–700.000 VND tùy dịch vụ.",
            "duration_vi": "Nửa ngày (kết hợp Eo Gió có thể trọn ngày).",
            "best_time_vi": "Mùa biển êm, khoảng tháng 3–8; tránh mùa gió bão cuối năm.",
            "tips_vi": "Đặt tour ca nô uy tín, mặc áo phao; mang kem chống nắng, đồ bơi; kiểm tra thời tiết trước khi đi.",
        },
        tags=["top", "beach", "swimming", "snorkeling", "nature", "outdoor", "viewpoint"],
        review_vi="Du khách choáng ngợp trước làn nước trong và màu biển đẹp như tranh, thích trải nghiệm ca nô cảm giác mạnh. Nhiều người khuyên đi sớm để tránh nắng gắt và đông; một số nhắc dịch vụ trên đảo có hạn nên chuẩn bị trước nước uống, đồ ăn nhẹ.",
        sources=[
            {"title": "Wikipedia (VI) — Kỳ Co", "url": "https://vi.wikipedia.org/wiki/K%E1%BB%B3_Co"},
        ],
    ),
    rec(
        region="vn-gia-lai", region_name_vi="Gia Lai", fed="Miền Trung",
        slug="eo-gio", name_vi="Eo Gió",
        name_en="Eo Gio (Windy Strait)", name_ru="Эозо (Ветреный пролив)",
        cats=["park_garden", "other"], lat=13.7003, lon=109.3544,
        addr="Xã Nhơn Lý, TP. Quy Nhơn, tỉnh Gia Lai",
        rating={"value": 4.6, "count": 9000, "source": "Google", "as_of": "2026-07"},
        short_vi="Eo Gió là eo biển tuyệt đẹp ở Nhơn Lý, nơi dãy núi đá ôm cong ra biển tạo thành một 'cửa gió' lộng gió quanh năm. Con đường bê tông men theo vách đá cho tầm nhìn ngoạn mục ra biển xanh, được xem là một trong những nơi ngắm bình minh và hoàng hôn đẹp nhất Quy Nhơn.",
        short_en="Eo Gio is a stunning coastal strait at Nhon Ly, where a curving ridge of rock embraces the sea to form a windy 'gate' blown year-round. A concrete path along the cliffs offers spectacular ocean views, rated among the finest spots to watch sunrise and sunset in Quy Nhon.",
        short_ru="Эозо — потрясающий морской пролив в Нёнли, где изогнутая гряда скал обнимает море, образуя продуваемые круглый год «ворота ветра». Бетонная тропа вдоль утёсов открывает захватывающие виды на океан и считается одним из лучших мест для встречи рассвета и заката в Куинёне.",
        long_vi="Cái tên Eo Gió xuất phát từ địa hình đặc biệt của nơi này: một dải núi đá vươn ra biển rồi uốn cong lại như vòng tay, tạo thành khe eo hẹp mà gió biển thổi qua gần như không ngớt. Nằm ở xã Nhơn Lý, cách trung tâm Quy Nhơn khoảng hai mươi cây số, Eo Gió gây ấn tượng mạnh bởi những vách đá cao dựng đứng, màu nâu đỏ và xám, tương phản với màu xanh thẳm của đại dương phía dưới. Chính quyền địa phương đã xây dựng con đường bê tông và các bậc thang uốn lượn theo triền núi, giúp du khách vừa đi bộ vừa phóng tầm mắt ra những mũi đá, hang yến và bãi sóng vỗ trắng xóa. Từ các đài vọng cảnh, khung cảnh biển trời mở ra bao la, đặc biệt quyến rũ vào lúc bình minh khi mặt trời nhô lên từ đường chân trời, và lúc hoàng hôn khi cả eo biển nhuộm sắc vàng cam. Eo Gió cũng là nơi trú ngụ của nhiều đàn chim yến làm tổ trong các hốc đá. Gần kề bãi Kỳ Co, làng chài Nhơn Lý và các tour lặn ngắm san hô, Eo Gió thường là điểm không thể thiếu trong hành trình khám phá vẻ đẹp biển đảo của vùng đất Quy Nhơn – Bình Định.",
        long_en="The name Eo Gio, meaning 'windy strait', comes from its distinctive terrain: a ridge of rock reaches into the sea and curves back like an embracing arm, forming a narrow gap through which the sea breeze blows almost without pause. In Nhon Ly commune, about twenty kilometres from central Quy Nhon, Eo Gio impresses with tall, sheer cliffs in shades of red-brown and grey, contrasting with the deep blue ocean below. Local authorities have built a concrete path and winding steps along the mountainside, letting visitors walk while taking in the rocky headlands, swiftlet caves and surf breaking white against the shore. From the viewing platforms the sea and sky open out immensely, especially alluring at dawn as the sun rises over the horizon, and at dusk when the whole strait glows amber. Eo Gio is also home to flocks of swiftlets nesting in the rock hollows. Close to Ky Co beach, the Nhon Ly fishing village and coral-snorkelling tours, Eo Gio is an essential stop on any journey exploring the coastal beauty of the Quy Nhon and Binh Dinh area.",
        long_ru="Название Эозо, «ветреный пролив», связано с необычным рельефом: гряда скал уходит в море и загибается обратно, словно обнимающая рука, образуя узкий проём, сквозь который почти без остановки дует морской бриз. В общине Нёнли, примерно в двадцати километрах от центра Куинёна, Эозо впечатляет высокими отвесными утёсами красно-бурых и серых оттенков, контрастирующими с тёмно-синим океаном внизу. Местные власти проложили бетонную тропу и извилистые ступени по склону, позволяя гостям идти, любуясь скалистыми мысами, пещерами саланганов и белой прибойной пеной. Со смотровых площадок море и небо открываются необъятно, особенно чарующе на рассвете, когда солнце встаёт над горизонтом, и на закате, когда весь пролив светится янтарём. Здесь же гнездятся стаи саланганов. Рядом с пляжем Кико, рыбацкой деревней Нёнли и турами по снорклингу Эозо — обязательная остановка в путешествии по побережью Куинёна и Биньдиня.",
        hi_vi=[
            "Eo biển với vách đá uốn cong tạo 'cửa gió' lộng gió quanh năm",
            "Đường bê tông và đài vọng cảnh men vách đá nhìn ra biển xanh",
            "Một trong những nơi ngắm bình minh, hoàng hôn đẹp nhất Quy Nhơn",
        ],
        hi_en=[
            "A strait where curving cliffs form a wind-swept 'gate' year-round",
            "Cliffside concrete path and platforms overlooking the blue sea",
            "Among the best sunrise and sunset viewpoints in Quy Nhon",
        ],
        hi_ru=[
            "Пролив, где изогнутые скалы образуют продуваемые круглый год «ворота»",
            "Бетонная тропа и площадки вдоль утёсов с видом на синее море",
            "Одно из лучших мест для рассвета и заката в Куинёне",
        ],
        practical={
            "hours_vi": "Mở cửa khoảng 6:00–18:00; đẹp nhất lúc bình minh và chiều muộn.",
            "ticket_vi": "Vé vào cửa tham khảo khoảng 25.000 VND/người.",
            "duration_vi": "Khoảng 1–2 giờ đi bộ và ngắm cảnh.",
            "best_time_vi": "Mùa khô tháng 3–8; sáng sớm hoặc chiều mát để tránh nắng gắt.",
            "tips_vi": "Đi giày bám tốt vì có bậc và gió lớn; mang mũ, giữ mũ nón cẩn thận; kết hợp tham quan Kỳ Co gần đó.",
        },
        tags=["top", "viewpoint", "sunrise", "sunset", "nature", "outdoor", "walk"],
        review_vi="Du khách mê mẩn khung cảnh biển đá hùng vĩ và con đường men vách núi, đặc biệt lúc bình minh. Nhiều người khen vé rẻ, cảnh đáng giá; một số lưu ý gió rất mạnh và nắng gắt buổi trưa nên nên đi sớm và chuẩn bị chống nắng.",
        sources=[
            {"title": "Wikipedia (VI) — Eo Gió", "url": "https://vi.wikipedia.org/wiki/Eo_Gi%C3%B3"},
        ],
    ),
]

# ================= ĐẮK LẮK (Miền Trung) — hợp nhất Phú Yên 1/7/2025 =================
PLACES += [
    rec(
        region="vn-dak-lak", region_name_vi="Đắk Lắk", fed="Miền Trung",
        slug="thac-dray-nur", name_vi="Thác Dray Nur",
        name_en="Dray Nur Waterfall", name_ru="Водопад Зрайнур",
        cats=["park_garden", "other"], lat=12.5419, lon=107.8897,
        addr="Xã Krông Ana (giáp Đắk Nông cũ), tỉnh Đắk Lắk, trên dòng sông Sêrêpốk",
        rating={"value": 4.4, "count": 5000, "source": "Google", "as_of": "2026-07"},
        short_vi="Thác Dray Nur là một trong những thác nước hùng vĩ nhất Tây Nguyên, rộng khoảng 250 m, đổ ầm ào trên dòng sông Sêrêpốk. Phía sau màn nước là hang động lớn, cùng truyền thuyết tình yêu của người Ê Đê khiến thác thêm phần huyền bí.",
        short_en="Dray Nur is one of the most majestic waterfalls in the Central Highlands, roughly 250 m wide, thundering across the Serepok River. A large cave hides behind the curtain of water, and an Ede love legend adds to its mystery.",
        short_ru="Зрайнур — один из самых величественных водопадов Центрального нагорья, шириной около 250 м, с грохотом низвергающийся на реке Серепок. За водной завесой скрыта большая пещера, а легенда о любви народа эдэ добавляет ему таинственности.",
        long_vi="Nằm trên dòng Sêrêpốk huyền thoại, con sông hiếm hoi ở Việt Nam chảy ngược về phía tây sang lưu vực Mê Kông, Thác Dray Nur là điểm đến thiên nhiên tiêu biểu của cao nguyên Đắk Lắk. Với chiều rộng tới khoảng hai trăm năm mươi mét và độ cao vài chục mét, vào mùa mưa thác tung bọt trắng xóa, gầm vang cả một vùng, tạo nên khung cảnh vừa dữ dội vừa nên thơ giữa rừng già bạt ngàn. Trong tiếng Ê Đê, Dray Nur có nghĩa là 'thác cái' — gắn với truyền thuyết về đôi trai gái yêu nhau nhưng bị ngăn cách, hóa thân vào dòng nước. Điểm thú vị là phía sau màn nước đổ có một hang động rộng, du khách bạo dạn có thể men theo vách đá để cảm nhận sức mạnh của thiên nhiên từ bên trong. Xung quanh thác là hệ sinh thái rừng phong phú, những tảng đá bazan đen bóng và các cây cầu treo bắc qua sông, thuận tiện cho việc dạo ngắm và chụp ảnh. Dray Nur thường được ghép cùng thác Dray Sáp kề bên trong cùng một tuyến tham quan. Hùng vĩ, hoang sơ và thấm đẫm sắc màu văn hóa bản địa, thác là nơi lý tưởng để cảm nhận vẻ đẹp mãnh liệt của núi rừng Tây Nguyên.",
        long_en="On the legendary Serepok River, one of the few rivers in Vietnam that flows west toward the Mekong basin, Dray Nur Waterfall is a signature natural attraction of the Dak Lak plateau. Roughly two hundred and fifty metres wide and some tens of metres high, in the rainy season it throws up white spray and roars across the whole area, creating a scene at once fierce and poetic amid vast old forest. In the Ede language Dray Nur means 'the female waterfall', linked to a legend of two lovers who were kept apart and merged into the water. A striking feature is the large cave hidden behind the falling curtain of water; bold visitors can edge along the rock to feel nature's power from within. Around the falls lies a rich forest ecosystem, glossy black basalt boulders and suspension bridges across the river, convenient for walking and photography. Dray Nur is usually combined with the neighbouring Dray Sap falls on the same tour. Majestic, wild and steeped in indigenous culture, it is an ideal place to feel the fierce beauty of the Central Highlands.",
        long_ru="На легендарной реке Серепок — одной из немногих во Вьетнаме, текущих на запад к бассейну Меконга, — водопад Зрайнур является характерной природной достопримечательностью плато Даклак. Шириной около двухсот пятидесяти метров и высотой в несколько десятков метров, в сезон дождей он вздымает белые брызги и грохочет на всю округу, создавая одновременно суровую и поэтичную картину среди бескрайнего древнего леса. На языке эдэ Зрайнур означает «водопад-жена» и связан с легендой о влюблённых, разлучённых и слившихся с водой. Поразительная особенность — большая пещера, скрытая за падающей завесой воды; смелые гости могут пройти вдоль скалы, чтобы ощутить мощь природы изнутри. Вокруг — богатая лесная экосистема, глянцевые чёрные базальтовые валуны и подвесные мосты через реку. Зрайнур обычно объединяют с соседним водопадом Зрайшап. Величественный, дикий и пропитанный местной культурой, он идеален, чтобы почувствовать неистовую красоту Центрального нагорья.",
        hi_vi=[
            "Thác rộng ~250 m trên dòng Sêrêpốk chảy ngược về Tây",
            "Hang động lớn ẩn sau màn nước đổ",
            "Gắn với truyền thuyết tình yêu và văn hóa người Ê Đê",
        ],
        hi_en=[
            "A ~250 m wide waterfall on the westward-flowing Serepok River",
            "A large cave hidden behind the falling water",
            "Tied to an Ede love legend and local culture",
        ],
        hi_ru=[
            "Водопад шириной ~250 м на текущей на запад реке Серепок",
            "Большая пещера, скрытая за падающей водой",
            "Связан с легендой о любви и культурой народа эдэ",
        ],
        practical={
            "hours_vi": "Tham quan ban ngày, khoảng 7:00–17:00.",
            "ticket_vi": "Vé vào khu du lịch thác tham khảo khoảng 30.000 VND/người.",
            "duration_vi": "Khoảng 1,5–2 giờ (đi bộ, xuống chân thác).",
            "best_time_vi": "Mùa mưa (tháng 6–11) thác nhiều nước và hùng vĩ nhất; mùa khô nước hiền hơn, dễ vào hang.",
            "tips_vi": "Đi giày bám tốt vì đá trơn; cẩn thận khi men vào hang sau thác; mang áo mưa mỏng vì hơi nước lớn.",
        },
        tags=["top", "waterfall", "nature", "outdoor", "cave", "hiking"],
        review_vi="Du khách ấn tượng với thác rộng, nước mạnh và trải nghiệm chui sau màn nước. Nhiều người khuyên đi mùa mưa để thấy thác hùng vĩ; một số nhắc đường xuống trơn, cần cẩn thận và nên có người địa phương dẫn đường.",
        sources=[
            {"title": "Wikipedia (VI) — Thác Đray Nur", "url": "https://vi.wikipedia.org/wiki/Th%C3%A1c_%C4%90ray_Nur"},
        ],
    ),
    rec(
        region="vn-dak-lak", region_name_vi="Đắk Lắk", fed="Miền Trung",
        slug="ho-lak", name_vi="Hồ Lắk",
        name_en="Lak Lake", name_ru="Озеро Лак",
        cats=["park_garden", "other"], lat=12.4225, lon=108.1800,
        addr="Thị trấn Liên Sơn, huyện Lắk cũ, tỉnh Đắk Lắk",
        rating={"value": 4.4, "count": 3800, "source": "Google", "as_of": "2026-07"},
        short_vi="Hồ Lắk là hồ nước ngọt tự nhiên lớn nhất Tây Nguyên, mặt nước rộng mênh mông giữa rừng và buôn làng người M'Nông. Du khách có thể chèo thuyền độc mộc, ngắm hoàng hôn và ghé thăm biệt điện Bảo Đại trên đồi nhìn xuống hồ.",
        short_en="Lak Lake is the largest natural freshwater lake in the Central Highlands, a vast expanse of water among forests and M'Nong villages. Visitors can paddle dugout canoes, watch the sunset and visit Emperor Bao Dai's villa on a hill overlooking the lake.",
        short_ru="Озеро Лак — крупнейшее природное пресноводное озеро Центрального нагорья, широкая водная гладь среди лесов и деревень народа мнонг. Гости могут плавать на лодках-долблёнках, любоваться закатом и посетить виллу императора Бао Дая на холме над озером.",
        long_vi="Trải rộng khoảng năm trăm héc-ta giữa vùng cao nguyên Đắk Lắk, Hồ Lắk là hồ nước ngọt tự nhiên lớn nhất Tây Nguyên và lớn thứ nhì cả nước, chỉ sau Hồ Ba Bể. Mặt hồ phẳng lặng được bao quanh bởi những dãy núi, rừng nguyên sinh và các buôn làng lâu đời của người M'Nông, tạo nên bức tranh thiên nhiên yên bình đậm chất bản địa. Nước hồ quanh năm đầy, là nguồn sống và cũng là không gian văn hóa của cộng đồng dân tộc nơi đây. Đến Hồ Lắk, du khách thường trải nghiệm ngồi thuyền độc mộc do người bản địa chèo, lướt nhẹ trên mặt nước phủ sen và súng, hoặc cưỡi voi thong dong ven hồ theo tập quán truyền thống. Bên bờ hồ, buôn Jun và buôn M'Liêng vẫn giữ những ngôi nhà dài, nghề dệt thổ cẩm và các lễ hội cồng chiêng. Trên ngọn đồi cao nhìn bao quát cả vùng là biệt điện của cựu hoàng Bảo Đại, nơi ông từng dừng chân nghỉ ngơi và săn bắn, nay trở thành điểm ngắm cảnh và hoàng hôn tuyệt đẹp. Với vẻ đẹp khoáng đạt, không khí trong lành và chiều sâu văn hóa, Hồ Lắk là điểm đến lý tưởng để chậm lại và hòa mình vào nhịp sống Tây Nguyên.",
        long_en="Spreading over some five hundred hectares in the Dak Lak highlands, Lak Lake is the largest natural freshwater lake in the Central Highlands and the second largest in Vietnam after Ba Be. Its calm surface is ringed by mountains, primary forest and long-established M'Nong villages, forming a peaceful, deeply indigenous scene. The lake stays full year-round, providing both livelihood and cultural space for the local communities. At Lak Lake, visitors typically ride a dugout canoe paddled by local people, gliding over water dotted with lotus and water lilies, or take a leisurely elephant ride along the shore in the traditional way. On the banks, Jun and M'Lieng villages still keep their longhouses, brocade weaving and gong festivals. On a hilltop overlooking the whole area stands the villa of former Emperor Bao Dai, where he once rested and hunted, now a superb spot for views and sunsets. With its open beauty, fresh air and cultural depth, Lak Lake is an ideal place to slow down and immerse oneself in the rhythm of highland life.",
        long_ru="Раскинувшись на площади около пятисот гектаров в нагорье Даклак, озеро Лак — крупнейшее природное пресноводное озеро Центрального нагорья и второе по величине во Вьетнаме после Бабе. Его спокойную гладь окружают горы, первичный лес и давние деревни народа мнонг, образуя мирную, глубоко самобытную картину. Озеро полноводно круглый год, служа и источником жизни, и культурным пространством местных общин. На озере Лак гости обычно катаются на лодке-долблёнке, которой правят местные жители, скользя по воде среди лотосов и кувшинок, или неспешно едут на слоне вдоль берега по традиции. На берегах деревни Джун и Мльенг хранят длинные дома, ткачество и праздники гонгов. На вершине холма, откуда виден весь край, стоит вилла бывшего императора Бао Дая, где он когда-то отдыхал и охотился, — теперь это прекрасное место для видов и закатов. Благодаря простору, свежему воздуху и культурной глубине озеро Лак идеально, чтобы замедлиться и погрузиться в ритм жизни нагорья.",
        hi_vi=[
            "Hồ nước ngọt tự nhiên lớn nhất Tây Nguyên",
            "Chèo thuyền độc mộc, trải nghiệm văn hóa buôn làng M'Nông",
            "Biệt điện Bảo Đại trên đồi ngắm hoàng hôn xuống hồ",
        ],
        hi_en=[
            "The largest natural freshwater lake in the Central Highlands",
            "Dugout-canoe rides and M'Nong village culture",
            "Emperor Bao Dai's hilltop villa with sunset views over the lake",
        ],
        hi_ru=[
            "Крупнейшее природное пресноводное озеро Центрального нагорья",
            "Прогулки на лодках-долблёнках и культура деревень мнонг",
            "Вилла императора Бао Дая на холме с видами заката над озером",
        ],
        practical={
            "hours_vi": "Tham quan ban ngày; hoạt động thuyền chủ yếu sáng và chiều mát.",
            "ticket_vi": "Tham quan quanh hồ cơ bản miễn phí; thuyền, dịch vụ và vé biệt điện Bảo Đại thu phí riêng.",
            "duration_vi": "Nửa ngày; có thể nghỉ đêm tại buôn để trải nghiệm sâu hơn.",
            "best_time_vi": "Mùa khô tháng 11–4 trời đẹp; sáng sớm và hoàng hôn cảnh hồ đẹp nhất.",
            "tips_vi": "Ưu tiên dịch vụ cộng đồng để hỗ trợ người bản địa; cân nhắc về phúc lợi động vật khi chọn cưỡi voi; mang chống muỗi.",
        },
        tags=["nature", "lake", "boat", "culture", "sunset", "outdoor"],
        review_vi="Du khách yêu thích không gian hồ rộng, yên bình và trải nghiệm văn hóa buôn làng. View từ biệt điện Bảo Đại được khen đẹp; một số ý kiến cân nhắc dịch vụ cưỡi voi vì lý do phúc lợi động vật và gợi ý chọn chèo thuyền thay thế.",
        sources=[
            {"title": "Wikipedia (EN) — Lak Lake", "url": "https://en.wikipedia.org/wiki/Lak_Lake"},
        ],
    ),
    rec(
        region="vn-dak-lak", region_name_vi="Đắk Lắk", fed="Miền Trung",
        slug="ganh-da-dia", name_vi="Gành Đá Đĩa",
        name_en="Ganh Da Dia (Da Dia Reef)", name_ru="Гандадиа (Каменные плиты)",
        cats=["park_garden", "other"], lat=13.3350, lon=109.2981,
        addr="Xã An Ninh Đông, huyện Tuy An cũ (Phú Yên), tỉnh Đắk Lắk",
        rating={"value": 4.5, "count": 6500, "source": "Google", "as_of": "2026-07"},
        short_vi="Gành Đá Đĩa là danh thắng ven biển độc đáo gồm hàng chục nghìn cột đá bazan đen xếp khít nhau như chồng đĩa khổng lồ. Được hình thành từ hoạt động núi lửa hàng triệu năm trước, đây là Di tích Quốc gia đặc biệt và là biểu tượng thiên nhiên của vùng Phú Yên.",
        short_en="Ganh Da Dia is a unique coastal wonder of tens of thousands of black basalt columns packed together like giant stacked plates. Formed by volcanic activity millions of years ago, it is a Special National Relic and a natural emblem of the Phu Yen area.",
        short_ru="Гандадиа — уникальное прибрежное чудо из десятков тысяч чёрных базальтовых колонн, сложенных плотно, словно гигантские стопки тарелок. Образованный вулканической активностью миллионы лет назад, он является особым национальным памятником и природным символом края Фуйен.",
        long_vi="Nằm bên bờ biển thuộc xã An Ninh Đông, Gành Đá Đĩa là một trong những kỳ quan địa chất độc đáo bậc nhất Việt Nam. Trên diện tích khoảng hai héc-ta, hàng chục nghìn khối đá bazan màu đen và xám xếp liền kề nhau, phần lớn có tiết diện hình lục giác hoặc ngũ giác đều đặn đến kinh ngạc, trông như vô số chiếc đĩa chồng lên nhau trải dài ra tận mép sóng. Hiện tượng này hình thành cách đây nhiều triệu năm, khi dung nham núi lửa nóng chảy gặp nước biển lạnh và đông cứng đột ngột, nứt tách thành các cột đá đều đặn, tương tự những kỳ quan nổi tiếng thế giới như Giant's Causeway ở Ireland. Sóng biển vỗ vào chân gành tung bọt trắng, tương phản với màu đá thẫm, tạo nên khung cảnh vừa kỳ vĩ vừa cuốn hút. Du khách có thể leo trèo, dạo bước trên bề mặt các cột đá, khám phá những hõm nước trong vắt giữa các khe và phóng tầm mắt ra biển Đông bao la. Gần đó còn có bãi Bàng, nhà thờ Mằng Lăng cổ và đầm Ô Loan, thuận tiện ghép thành tuyến tham quan. Đã được xếp hạng Di tích Quốc gia đặc biệt, Gành Đá Đĩa là điểm đến không thể bỏ lỡ khi khám phá dải đất Phú Yên nay thuộc tỉnh Đắk Lắk.",
        long_en="On the coast of An Ninh Dong commune, Ganh Da Dia is one of Vietnam's most remarkable geological wonders. Over an area of about two hectares, tens of thousands of black and grey basalt blocks lie packed together, most with astonishingly regular hexagonal or pentagonal cross-sections, resembling countless plates stacked and stretching to the water's edge. The formation arose many millions of years ago when molten volcanic lava met cold seawater and solidified abruptly, cracking into regular columns, much like world-famous sites such as the Giant's Causeway in Ireland. Waves striking the base throw up white foam that contrasts with the dark stone, creating a scene both grand and captivating. Visitors can clamber and walk across the surface of the columns, explore clear pools between the cracks and gaze out over the vast East Sea. Nearby are Bang beach, the old Mang Lang church and O Loan lagoon, easily combined into one itinerary. Ranked as a Special National Relic, Ganh Da Dia is an unmissable destination when exploring the Phu Yen coast, now part of Dak Lak province.",
        long_ru="На побережье общины Аниньдонг Гандадиа — одно из самых примечательных геологических чудес Вьетнама. На площади около двух гектаров десятки тысяч чёрных и серых базальтовых блоков лежат плотно, большинство — с поразительно правильным шести- или пятиугольным сечением, напоминая бесчисленные тарелки, сложенные стопками до самой кромки воды. Образование возникло много миллионов лет назад, когда раскалённая вулканическая лава встретилась с холодной морской водой и резко застыла, растрескавшись на правильные колонны, подобно всемирно известным местам вроде Дороги гигантов в Ирландии. Волны, бьющие о подножие, вздымают белую пену, контрастирующую с тёмным камнем. Гости могут взбираться и ходить по поверхности колонн, исследовать прозрачные лужицы между трещинами и смотреть на бескрайнее Восточное море. Рядом — пляж Банг, старая церковь Мангланг и лагуна Олоан. Признанный особым национальным памятником, Гандадиа — обязательная цель при знакомстве с побережьем Фуйена, ныне частью провинции Даклак.",
        hi_vi=[
            "Hàng chục nghìn cột đá bazan lục giác xếp khít như chồng đĩa khổng lồ",
            "Hình thành do dung nham gặp nước biển đông cứng hàng triệu năm trước",
            "Di tích Quốc gia đặc biệt, biểu tượng thiên nhiên Phú Yên",
        ],
        hi_en=[
            "Tens of thousands of hexagonal basalt columns like stacked plates",
            "Formed as lava met seawater and solidified millions of years ago",
            "A Special National Relic and natural emblem of Phu Yen",
        ],
        hi_ru=[
            "Десятки тысяч шестиугольных базальтовых колонн, как стопки тарелок",
            "Образован при застывании лавы в морской воде миллионы лет назад",
            "Особый национальный памятник и природный символ Фуйена",
        ],
        practical={
            "hours_vi": "Tham quan ban ngày, khoảng 6:30–18:00.",
            "ticket_vi": "Vé vào tham khảo khoảng 20.000–25.000 VND/người.",
            "duration_vi": "Khoảng 1–1,5 giờ.",
            "best_time_vi": "Mùa khô tháng 1–8; sáng sớm hoặc chiều mát tránh nắng và trơn.",
            "tips_vi": "Đi giày bám tốt vì đá có thể trơn khi sóng đánh; cẩn thận mép nước; kết hợp nhà thờ Mằng Lăng và đầm Ô Loan.",
        },
        tags=["top", "geology", "nature", "sea", "viewpoint", "outdoor", "photo-spot"],
        review_vi="Du khách thán phục sự kỳ lạ của các cột đá xếp khít và cảnh biển đẹp, chụp ảnh rất ấn tượng. Nhiều người khen vé rẻ; một số nhắc bề mặt đá trơn khi sóng lớn, cần đi cẩn thận và tránh leo ra sát mép nước.",
        sources=[
            {"title": "Wikipedia (EN) — Ganh Da Dia", "url": "https://en.wikipedia.org/wiki/Ganh_Da_Dia"},
        ],
    ),
]

# ================= TÂY NINH (Miền Nam) — hợp nhất Long An 1/7/2025 =================
PLACES += [
    rec(
        region="vn-tay-ninh", region_name_vi="Tây Ninh", fed="Miền Nam",
        slug="nui-ba-den", name_vi="Núi Bà Đen",
        name_en="Ba Den Mountain (Black Virgin Mountain)", name_ru="Гора Бàден (Чёрной Девы)",
        cats=["park_garden", "other"], lat=11.3673, lon=106.1697,
        addr="Khu du lịch quốc gia Núi Bà Đen, TP. Tây Ninh, tỉnh Tây Ninh",
        rating={"value": 4.6, "count": 26000, "source": "Google", "as_of": "2026-07"},
        short_vi="Núi Bà Đen cao 986 m, là ngọn núi cao nhất Nam Bộ, được mệnh danh 'nóc nhà Đông Nam Bộ'. Núi nổi tiếng với hệ thống chùa linh thiêng, tuyến cáp treo hiện đại và quần thể tâm linh trên đỉnh thường mây phủ, thu hút hàng triệu khách hành hương mỗi năm.",
        short_en="Ba Den Mountain rises 986 m, the highest peak in southern Vietnam, dubbed 'the roof of the southeast'. It is famous for its sacred temples, a modern cable car and a spiritual complex on the often cloud-wreathed summit, drawing millions of pilgrims each year.",
        short_ru="Гора Баден высотой 986 м — высочайшая вершина юга Вьетнама, прозванная «крышей юго-востока». Она известна священными храмами, современной канатной дорогой и духовным комплексом на часто окутанной облаками вершине, привлекая миллионы паломников ежегодно.",
        long_vi="Sừng sững giữa vùng đồng bằng tương đối bằng phẳng của miền Đông Nam Bộ, Núi Bà Đen cao chín trăm tám mươi sáu mét và từ lâu đã là ngọn núi thiêng gắn với đời sống tâm linh của người dân Nam Bộ. Truyền thuyết về Bà Đen (Linh Sơn Thánh Mẫu) đã biến nơi đây thành trung tâm hành hương lớn, đặc biệt vào dịp lễ vía Bà và đầu xuân, khi hàng vạn người đổ về lễ Phật, cầu an. Lưng chừng núi là hệ thống chùa Bà, chùa Hang, các hang động và điện thờ nép trong vách đá và cây rừng. Những năm gần đây, một tuyến cáp treo hiện đại đưa du khách lên tận đỉnh chỉ trong ít phút, nơi hình thành cả một quần thể quảng trường, tượng Phật Bà Tây Bổ Đà Sơn bằng đồng cao vào loại lớn nhất châu Á, cùng khu triển lãm và vườn hoa. Trên độ cao gần một nghìn mét, đỉnh núi thường bồng bềnh trong mây, khí hậu mát lạnh, phóng tầm mắt bao quát cả một vùng đồng bằng, hồ Dầu Tiếng và biên giới Việt Nam – Campuchia. Kết hợp giữa cảnh quan thiên nhiên hùng vĩ, giá trị tâm linh sâu sắc và trải nghiệm hiện đại, Núi Bà Đen là điểm đến tiêu biểu và là biểu tượng của tỉnh Tây Ninh.",
        long_en="Rising abruptly from the relatively flat plains of southeastern Vietnam, Ba Den Mountain stands nine hundred and eighty-six metres high and has long been a sacred peak woven into the spiritual life of the southern people. The legend of the Black Lady (the Holy Mother of Linh Son) has made it a major pilgrimage centre, especially during her festival and the early spring, when tens of thousands come to worship and pray for peace. On the mountainside cluster the Ba pagoda, the Cave pagoda, grottoes and shrines tucked into the cliffs and forest. In recent years a modern cable car has carried visitors to the very summit in minutes, where a whole complex has taken shape: a plaza, a bronze statue of the Bodhisattva Tay Bo Da Son among the tallest in Asia, exhibition halls and flower gardens. At nearly a thousand metres, the summit often floats in cloud, the air is cool, and the view sweeps over the plains, Dau Tieng reservoir and the Vietnam-Cambodia border. Blending majestic natural scenery, deep spiritual meaning and a modern experience, Ba Den Mountain is a signature destination and the emblem of Tay Ninh province.",
        long_ru="Резко вздымаясь над сравнительно плоскими равнинами юго-восточного Вьетнама, гора Баден высотой девятьсот восемьдесят шесть метров издавна является священной вершиной, вплетённой в духовную жизнь южан. Легенда о Чёрной Госпоже (Святой Матери Линьшон) сделала её крупным центром паломничества, особенно во время её праздника и ранней весной, когда десятки тысяч людей приходят молиться о мире. На склоне теснятся пагода Ба, Пещерная пагода, гроты и святилища, укрытые в скалах и лесу. В последние годы современная канатная дорога за считанные минуты поднимает гостей на саму вершину, где сложился целый комплекс: площадь, бронзовая статуя бодхисаттвы Тэйбодашон, одна из самых высоких в Азии, выставочные залы и цветники. На высоте почти тысячи метров вершина часто плывёт в облаках, воздух прохладен, а вид охватывает равнины, водохранилище Заутьенг и границу Вьетнама с Камбоджей. Сочетая величественные пейзажи, глубокий духовный смысл и современные впечатления, гора Баден — знаковая достопримечательность и символ провинции Тэйнинь.",
        hi_vi=[
            "Đỉnh cao 986 m — 'nóc nhà Đông Nam Bộ', thường mây phủ",
            "Trung tâm hành hương với chùa Bà, chùa Hang và tượng Phật Bà bằng đồng cao hàng đầu châu Á",
            "Cáp treo hiện đại lên đỉnh, view bao quát hồ Dầu Tiếng và biên giới",
        ],
        hi_en=[
            "A 986 m summit — 'roof of the southeast', often cloud-wreathed",
            "A pilgrimage centre with Ba and Cave pagodas and a top-ranking bronze Buddha statue",
            "A modern cable car to the peak with views over Dau Tieng reservoir and the border",
        ],
        hi_ru=[
            "Вершина 986 м — «крыша юго-востока», часто в облаках",
            "Центр паломничества с пагодами и одной из высочайших бронзовых статуй Будды в Азии",
            "Современная канатная дорога на вершину с видом на водохранилище и границу",
        ],
        practical={
            "hours_vi": "Khu du lịch và cáp treo mở khoảng 6:00–18:00; dịp lễ có thể kéo dài hơn.",
            "ticket_vi": "Vé cáp treo khứ hồi tham khảo khoảng 250.000–350.000 VND tùy tuyến; leo bộ miễn phí.",
            "duration_vi": "Nửa ngày (đi cáp treo, tham quan đỉnh và chùa).",
            "best_time_vi": "Mùa khô tháng 11–4; dịp hội xuân và lễ vía Bà rất đông.",
            "tips_vi": "Ăn mặc lịch sự khi vào chùa; mang áo ấm nhẹ vì đỉnh mát và nhiều gió; tránh ngày cao điểm lễ nếu ngại đông.",
        },
        tags=["top", "mountain", "temple", "pilgrimage", "cable-car", "viewpoint", "outdoor"],
        review_vi="Du khách ấn tượng với quần thể trên đỉnh, tượng Phật lớn và biển mây; cáp treo được khen nhanh, tiện. Nhiều người nhắc dịp lễ Tết rất đông đúc, nên đi sớm; một số thích leo bộ đường mòn để rèn sức và ngắm cảnh.",
        sources=[
            {"title": "Wikipedia (EN) — Black Virgin Mountain", "url": "https://en.wikipedia.org/wiki/Black_Virgin_Mountain"},
        ],
    ),
    rec(
        region="vn-tay-ninh", region_name_vi="Tây Ninh", fed="Miền Nam",
        slug="toa-thanh-tay-ninh", name_vi="Tòa Thánh Cao Đài Tây Ninh",
        name_en="Cao Dai Holy See (Tay Ninh Great Temple)", name_ru="Святой престол Каодай (Храм в Тэйнине)",
        cats=["church", "monument"], lat=11.3007, lon=106.1289,
        addr="Phường Long Hoa, TP. Tây Ninh (Hòa Thành cũ), tỉnh Tây Ninh",
        rating={"value": 4.6, "count": 12000, "source": "Google", "as_of": "2026-07"},
        short_vi="Tòa Thánh Tây Ninh là thánh địa trung tâm của đạo Cao Đài, tôn giáo bản địa ra đời tại Việt Nam năm 1926. Ngôi đền rực rỡ sắc màu, hòa trộn kiến trúc phương Đông và phương Tây, nổi bật với hình con mắt Thiên Nhãn và các lễ cầu nguyện đông đảo tín đồ áo trắng.",
        short_en="The Tay Ninh Holy See is the central sanctuary of Cao Dai, an indigenous religion founded in Vietnam in 1926. The vividly colourful temple blends Eastern and Western architecture, marked by the Divine Eye symbol and large prayer ceremonies of white-robed followers.",
        short_ru="Святой престол в Тэйнине — центральное святилище каодай, самобытной религии, возникшей во Вьетнаме в 1926 году. Ярко раскрашенный храм сочетает восточную и западную архитектуру, выделяясь символом Божественного Ока и многолюдными молебнами последователей в белых одеждах.",
        long_vi="Tọa lạc trong một khuôn viên rộng lớn ở phường Long Hoa, Tòa Thánh Tây Ninh là công trình tôn giáo tiêu biểu và là trung tâm của đạo Cao Đài — một tôn giáo bản địa được khai sinh tại Việt Nam vào năm 1926, kết hợp tư tưởng của nhiều tín ngưỡng lớn như Phật giáo, Đạo giáo, Nho giáo, Thiên Chúa giáo và tín ngưỡng dân gian. Được khởi công từ thập niên 1930 và hoàn thành sau nhiều năm, ngôi đền chính gây choáng ngợp bởi sự pha trộn phong cách hiếm thấy: mặt tiền có hai tháp chuông cao như nhà thờ phương Tây, bên trong là hàng cột chạm rồng uốn lượn sặc sỡ theo lối Á Đông, trần vòm sơn màu trời sao, và khắp nơi hiện diện biểu tượng Thiên Nhãn — con mắt trái tượng trưng cho Đấng Cao Đài đang dõi theo muôn loài. Điểm hấp dẫn nhất với du khách là các buổi lễ cầu nguyện diễn ra bốn lần mỗi ngày, khi hàng trăm tín đồ mặc áo dài trắng, cùng các chức sắc trong phẩm phục vàng, xanh, đỏ, trang nghiêm quỳ lễ trong tiếng nhạc và kinh. Du khách được phép quan sát từ ban công tầng trên với thái độ tôn trọng. Vừa là nơi thờ tự linh thiêng, vừa là một kỳ quan kiến trúc độc đáo, Tòa Thánh Tây Ninh mang đến trải nghiệm văn hóa – tâm linh khó quên.",
        long_en="Set within a vast compound in Long Hoa ward, the Tay Ninh Holy See is the emblematic religious monument and the centre of Cao Dai, an indigenous religion founded in Vietnam in 1926 that combines ideas from Buddhism, Taoism, Confucianism, Christianity and folk belief. Begun in the 1930s and finished after many years, the main temple astonishes with a rare blend of styles: a facade with two bell towers tall as a Western church, an interior of brightly painted columns wound with Asian dragons, a vaulted ceiling painted like a starry sky, and everywhere the Divine Eye, the single left eye symbolising the Supreme Being watching over all. The greatest draw for visitors is the prayer ceremony held four times a day, when hundreds of followers in white robes, alongside dignitaries in yellow, blue and red vestments, kneel solemnly amid music and chanting. Visitors may watch respectfully from the upper balcony. At once a sacred place of worship and a singular architectural wonder, the Tay Ninh Holy See offers an unforgettable cultural and spiritual experience, and remains one of the most distinctive sights in southern Vietnam.",
        long_ru="Расположенный в обширном комплексе в квартале Лонгхоа, Святой престол Тэйнинь — знаковый религиозный памятник и центр каодай, самобытной религии, основанной во Вьетнаме в 1926 году и объединяющей идеи буддизма, даосизма, конфуцианства, христианства и народных верований. Начатый в 1930-х и завершённый спустя много лет, главный храм поражает редким сочетанием стилей: фасад с двумя колокольнями, высокими, как у западной церкви, интерьер с ярко расписанными колоннами, обвитыми азиатскими драконами, сводчатый потолок, расписанный как звёздное небо, и повсюду Божественное Око — единственный левый глаз, символизирующий Высшее Существо, наблюдающее за всем. Больше всего гостей привлекает молебен, проходящий четырежды в день, когда сотни последователей в белых одеждах вместе со священнослужителями в жёлтых, синих и красных облачениях торжественно преклоняют колени под музыку и пение. Наблюдать можно с верхнего балкона с уважением. Одновременно священное место и уникальное архитектурное чудо, Святой престол дарит незабываемое культурно-духовное впечатление.",
        hi_vi=[
            "Trung tâm của đạo Cao Đài — tôn giáo bản địa ra đời tại Việt Nam năm 1926",
            "Kiến trúc pha trộn Đông – Tây rực rỡ, biểu tượng Thiên Nhãn khắp nơi",
            "Lễ cầu nguyện 4 lần/ngày với tín đồ áo trắng, chức sắc phẩm phục nhiều màu",
        ],
        hi_en=[
            "Centre of Cao Dai, an indigenous religion founded in Vietnam in 1926",
            "A vivid East-West architectural blend with the Divine Eye everywhere",
            "Prayer ceremonies four times daily with white-robed and colourfully vested followers",
        ],
        hi_ru=[
            "Центр каодай — самобытной религии, основанной во Вьетнаме в 1926 году",
            "Яркое сочетание восточной и западной архитектуры с Божественным Оком",
            "Молебны четырежды в день с последователями в белом и цветных облачениях",
        ],
        practical={
            "hours_vi": "Mở cửa ban ngày; lễ chính diễn ra vào khoảng 6:00, 12:00, 18:00 và 24:00.",
            "ticket_vi": "Miễn phí tham quan; nên tùy tâm đóng góp và giữ trang nghiêm.",
            "duration_vi": "Khoảng 1–1,5 giờ (nên canh giờ lễ 12:00 để xem trọn nghi lễ).",
            "best_time_vi": "Buổi trưa để dự lễ 12:00; kết hợp cùng ngày với Núi Bà Đen gần đó.",
            "tips_vi": "Ăn mặc kín đáo, bỏ giày khi vào chính điện, đi theo lối nam bên phải nữ bên trái; không làm ồn và tôn trọng tín đồ đang hành lễ.",
        },
        tags=["top", "temple", "architecture", "culture", "historic", "indoor"],
        review_vi="Du khách choáng ngợp trước màu sắc và kiến trúc độc đáo, ấn tượng với nghi lễ trang nghiêm giữa trưa. Nhiều người khen vào cửa miễn phí và giàu trải nghiệm văn hóa; một số nhắc cần giữ yên lặng, ăn mặc phù hợp và tôn trọng nơi thờ tự.",
        sources=[
            {"title": "Wikipedia (EN) — Cao Dai", "url": "https://en.wikipedia.org/wiki/Caodaism"},
        ],
    ),
]

# ================= TUYÊN QUANG (Miền Bắc) — hợp nhất Hà Giang 1/7/2025 =================
PLACES += [
    rec(
        region="vn-tuyen-quang", region_name_vi="Tuyên Quang", fed="Miền Bắc",
        slug="cao-nguyen-da-dong-van", name_vi="Cao nguyên đá Đồng Văn",
        name_en="Dong Van Karst Plateau Geopark", name_ru="Каменное плато Донгван",
        cats=["park_garden", "other"], lat=23.2769, lon=105.3622,
        addr="Vùng Đồng Văn – Mèo Vạc (Hà Giang cũ), tỉnh Tuyên Quang",
        rating={"value": 4.8, "count": 9000, "source": "Google", "as_of": "2026-07"},
        short_vi="Cao nguyên đá Đồng Văn là Công viên Địa chất Toàn cầu UNESCO, trải trên vùng núi đá vôi hiểm trở nơi địa đầu Tổ quốc. Nổi bật với những dãy núi tai mèo, hẻm vực sâu, ruộng bậc thang và bản làng của đồng bào Mông, Lô Lô, Dao... đầy bản sắc.",
        short_en="The Dong Van Karst Plateau is a UNESCO Global Geopark spread across a rugged limestone highland at Vietnam's far north. It is renowned for jagged rock ranges, deep gorges, terraced fields and the colourful villages of the Hmong, Lo Lo and Dao peoples.",
        short_ru="Каменное плато Донгван — глобальный геопарк ЮНЕСКО, раскинувшийся по суровому известняковому нагорью на крайнем севере Вьетнама. Оно славится зубчатыми скальными грядами, глубокими ущельями, террасными полями и колоритными деревнями народов хмонг, лоло и зао.",
        long_vi="Nằm ở cực bắc đất nước, Cao nguyên đá Đồng Văn được UNESCO công nhận là Công viên Địa chất Toàn cầu đầu tiên của Việt Nam vào năm 2010, trải rộng qua các huyện Đồng Văn, Mèo Vạc, Yên Minh và Quản Bạ của tỉnh Hà Giang cũ, nay thuộc tỉnh Tuyên Quang. Đây là một bảo tàng địa chất sống động, nơi lộ ra các tầng đá vôi có tuổi tới hàng trăm triệu năm, ghi dấu quá trình vận động của vỏ Trái Đất và những sinh vật cổ đại. Cảnh quan nơi đây khắc nghiệt mà kỳ vĩ: những dãy núi đá tai mèo xám nhọn trải dài đến tận chân trời, xen giữa là các thung lũng, hẻm vực và dòng sông Nho Quế xanh biếc. Trên nền đá cằn cỗi, đồng bào các dân tộc Mông, Lô Lô, Dao, Tày vẫn bám trụ, canh tác ngô trong hốc đá, dựng nhà trình tường và gìn giữ những phiên chợ vùng cao rực rỡ sắc màu thổ cẩm. Du khách đến đây để chinh phục các cung đường đèo ngoạn mục, ghé phố cổ Đồng Văn, dinh thự họ Vương, cột cờ Lũng Cú và đèo Mã Pí Lèng huyền thoại. Mỗi mùa cao nguyên lại khoác một vẻ riêng: hoa tam giác mạch tím hồng cuối thu, hoa đào hoa mận mùa xuân. Hùng vĩ, nguyên sơ và đậm đà bản sắc, Đồng Văn là một trong những vùng đất đáng nhớ nhất của núi rừng phía Bắc.",
        long_en="At the country's northern tip, the Dong Van Karst Plateau was recognised by UNESCO as Vietnam's first Global Geopark in 2010, spreading across the Dong Van, Meo Vac, Yen Minh and Quan Ba districts of the former Ha Giang province, now part of Tuyen Quang. It is a living geological museum, where limestone strata hundreds of millions of years old lie exposed, recording the movement of the Earth's crust and ancient life. The scenery is harsh yet magnificent: ranges of grey, needle-sharp karst stretch to the horizon, broken by valleys, gorges and the jade-green Nho Que River. On this barren stone, the Hmong, Lo Lo, Dao and Tay peoples still hold on, growing maize in rock hollows, building rammed-earth houses and keeping vivid upland markets bright with brocade. Travellers come to conquer spectacular mountain passes, to visit Dong Van old quarter, the Vuong family mansion, Lung Cu flag tower and the legendary Ma Pi Leng Pass. Each season gives the plateau a different face: pink-purple buckwheat flowers in late autumn, peach and plum blossom in spring. Grand, pristine and rich in identity, Dong Van is one of the most memorable lands of Vietnam's northern mountains.",
        long_ru="На самом севере страны Каменное плато Донгван было признано ЮНЕСКО первым во Вьетнаме глобальным геопарком в 2010 году; оно охватывает районы Донгван, Меовак, Йенминь и Куанба бывшей провинции Хазянг, ныне части Туенкуанга. Это живой геологический музей, где обнажаются известняковые пласты возрастом в сотни миллионов лет, хранящие следы движения земной коры и древней жизни. Пейзаж суров и великолепен: гряды серого игольчато-острого карста тянутся к горизонту, перемежаясь долинами, ущельями и нефритово-зелёной рекой Нокуэ. На этом бесплодном камне народы хмонг, лоло, зао и тай по-прежнему держатся, выращивая кукурузу в каменных лунках, строя дома из утрамбованной земли и сохраняя яркие горные рынки. Путешественники приезжают покорять впечатляющие перевалы, посетить старый квартал Донгван, усадьбу семьи Выонг, флаговую башню Лунгку и легендарный перевал Мапиленг. Каждый сезон дарит плато иной облик: розово-фиолетовая гречиха поздней осенью, цветение персика и сливы весной. Величественное, нетронутое и самобытное, Донгван — одна из самых запоминающихся земель северных гор Вьетнама.",
        hi_vi=[
            "Công viên Địa chất Toàn cầu UNESCO đầu tiên của Việt Nam (2010)",
            "Núi đá tai mèo, hẻm vực và sông Nho Quế xanh biếc nơi cực Bắc",
            "Bản sắc đồng bào Mông, Lô Lô, Dao; mùa hoa tam giác mạch nổi tiếng",
        ],
        hi_en=[
            "Vietnam's first UNESCO Global Geopark (2010)",
            "Needle-sharp karst, gorges and the jade Nho Que River at the far north",
            "Hmong, Lo Lo and Dao heritage; famed buckwheat-flower season",
        ],
        hi_ru=[
            "Первый во Вьетнаме глобальный геопарк ЮНЕСКО (2010)",
            "Игольчатый карст, ущелья и нефритовая река Нокуэ на крайнем севере",
            "Наследие хмонг, лоло и зао; знаменитый сезон цветения гречихи",
        ],
        practical={
            "hours_vi": "Vùng cảnh quan mở tự do; nên đi theo cung đường và nghỉ tại Đồng Văn, Mèo Vạc.",
            "ticket_vi": "Nhiều điểm miễn phí; một số như dinh họ Vương, phố cổ, thuyền sông Nho Quế thu phí riêng.",
            "duration_vi": "Nên dành 2–3 ngày cho trọn cung cao nguyên đá.",
            "best_time_vi": "Tháng 10–12 mùa hoa tam giác mạch; tháng 1–3 hoa đào, mận; tránh mưa lũ mùa hè.",
            "tips_vi": "Đi xe vững tay lái hoặc thuê tài xế bản địa; mang áo ấm; đổ xăng đầy vì trạm thưa; tôn trọng phong tục bản làng.",
        },
        tags=["unesco", "top", "geopark", "mountain", "culture", "viewpoint", "outdoor"],
        review_vi="Du khách coi đây là vùng cảnh quan hùng vĩ bậc nhất Việt Nam, mê cung đường đèo và bản sắc dân tộc. Nhiều người khuyên đi 2–3 ngày, thuê tài xế nếu không quen đường núi; một số nhắc thời tiết đổi nhanh và cần chuẩn bị áo ấm.",
        sources=[
            {"title": "UNESCO Global Geoparks — Dong Van Karst Plateau", "url": "https://en.unesco.org/global-geoparks/dong-van-karst-plateau"},
        ],
    ),
    rec(
        region="vn-tuyen-quang", region_name_vi="Tuyên Quang", fed="Miền Bắc",
        slug="ma-pi-leng", name_vi="Đèo Mã Pí Lèng",
        name_en="Ma Pi Leng Pass", name_ru="Перевал Мапиленг",
        cats=["park_garden", "other"], lat=23.2408, lon=105.4108,
        addr="Trên Quốc lộ 4C nối Đồng Văn – Mèo Vạc (Hà Giang cũ), tỉnh Tuyên Quang",
        rating={"value": 4.8, "count": 11000, "source": "Google", "as_of": "2026-07"},
        short_vi="Mã Pí Lèng là một trong 'tứ đại đỉnh đèo' của miền Bắc, cao khoảng 1.500 m, nối Đồng Văn với Mèo Vạc. Con đèo hiểm trở uốn lượn bên vực sâu, nhìn xuống dòng sông Nho Quế xanh ngọc, được mệnh danh 'vua của các con đèo' vùng cao nguyên đá.",
        short_en="Ma Pi Leng is one of northern Vietnam's 'four great passes', about 1,500 m high, linking Dong Van and Meo Vac. The perilous road winds along a deep abyss above the jade-green Nho Que River and is hailed as the 'king of passes' of the karst plateau.",
        short_ru="Мапиленг — один из «четырёх великих перевалов» севера Вьетнама, высотой около 1500 м, соединяющий Донгван и Меовак. Опасная дорога вьётся вдоль глубокой пропасти над нефритово-зелёной рекой Нокуэ и провозглашена «королём перевалов» каменного плато.",
        long_vi="Được xem là 'vua của các con đèo' ở vùng cực Bắc, Mã Pí Lèng nằm trên con đường mang tên Hạnh Phúc, đoạn nối hai huyện Đồng Văn và Mèo Vạc. Cái tên theo tiếng Mông thường được hiểu là 'sống mũi con ngựa', ám chỉ sự hiểm trở đến mức con ngựa đi qua cũng phải tắt thở. Con đèo dài chừng hai mươi cây số, đỉnh cao khoảng một nghìn năm trăm mét, được hàng vạn thanh niên xung phong và người dân các dân tộc mở bằng sức người qua nhiều năm gian khổ trong thập niên 1960, chủ yếu bằng cuốc, xẻ và dây treo mình trên vách đá. Đứng trên đỉnh đèo, du khách choáng ngợp trước khung cảnh hùng vĩ: một bên là vách núi đá dựng đứng, một bên là vực sâu hun hút mà dưới đáy, dòng sông Nho Quế hiện ra như một dải lụa xanh ngọc len giữa hẻm Tu Sản, một trong những hẻm vực sâu nhất Đông Nam Á. Trạm dừng chân và đường đi bộ trên vách đá cho những góc nhìn ngoạn mục để ngắm cảnh và chụp ảnh. Nhiều du khách còn xuống thung lũng đi thuyền trên sông Nho Quế để chiêm ngưỡng hẻm núi từ dưới nước. Vừa là kỳ tích chinh phục thiên nhiên, vừa là điểm ngắm cảnh tuyệt đẹp, Mã Pí Lèng là biểu tượng không thể thiếu của cao nguyên đá.",
        long_en="Regarded as the 'king of passes' in the far north, Ma Pi Leng lies on the road known as Happiness Road, the stretch connecting Dong Van and Meo Vac districts. The name, from the Hmong language, is usually taken to mean 'the horse's nose bridge', suggesting a road so perilous that even a horse crossing it would lose its breath. About twenty kilometres long and peaking near one thousand five hundred metres, the pass was carved out largely by hand over years of hardship in the 1960s by volunteer youth and local ethnic people, using picks, shovels and ropes to hang from the cliffs. Standing at the summit, visitors are overwhelmed by the majestic scene: a sheer rock wall on one side, a plunging abyss on the other, at the bottom of which the Nho Que River appears like a ribbon of jade winding through the Tu San canyon, one of the deepest gorges in Southeast Asia. A rest stop and a cliffside walkway offer spectacular vantage points. Many travellers descend into the valley to take a boat on the Nho Que River and view the canyon from the water. At once a feat of conquering nature and a superb viewpoint, Ma Pi Leng is an essential symbol of the karst plateau.",
        long_ru="Считающийся «королём перевалов» крайнего севера, Мапиленг лежит на дороге, известной как Дорога Счастья, соединяющей районы Донгван и Меовак. Название с языка хмонг обычно понимают как «переносица коня», намекая на дорогу столь опасную, что даже конь, переходя её, теряет дыхание. Длиной около двадцати километров и высотой почти полторы тысячи метров, перевал прокладывали в основном вручную в течение тяжёлых лет 1960-х годов добровольцы-молодёжь и местные народы, орудуя кирками, лопатами и верёвками, свисая со скал. Стоя на вершине, гости потрясены величественной картиной: с одной стороны отвесная скальная стена, с другой — обрывающаяся пропасть, на дне которой река Нокуэ кажется лентой нефрита, вьющейся сквозь каньон Тушан, один из глубочайших в Юго-Восточной Азии. Смотровая площадка и тропа вдоль утёса открывают впечатляющие виды. Многие путешественники спускаются в долину и плывут по реке Нокуэ, любуясь каньоном с воды. Одновременно подвиг покорения природы и великолепная смотровая точка, Мапиленг — незаменимый символ каменного плато.",
        hi_vi=[
            "Một trong 'tứ đại đỉnh đèo' miền Bắc, cao ~1.500 m",
            "Nhìn xuống hẻm Tu Sản và sông Nho Quế xanh ngọc",
            "Con đường Hạnh Phúc mở bằng sức người thập niên 1960",
        ],
        hi_en=[
            "One of northern Vietnam's 'four great passes', ~1,500 m high",
            "Overlooking the Tu San canyon and the jade Nho Que River",
            "On Happiness Road, carved by hand in the 1960s",
        ],
        hi_ru=[
            "Один из «четырёх великих перевалов» севера, высотой ~1500 м",
            "Вид на каньон Тушан и нефритовую реку Нокуэ",
            "На Дороге Счастья, проложенной вручную в 1960-х",
        ],
        practical={
            "hours_vi": "Đèo đi lại tự do; ngắm cảnh đẹp nhất ban ngày, sáng sớm ít mây mù.",
            "ticket_vi": "Miễn phí; thuyền sông Nho Quế và một số điểm dừng thu phí riêng.",
            "duration_vi": "1–2 giờ dừng ngắm; thêm 1–2 giờ nếu đi thuyền Nho Quế.",
            "best_time_vi": "Mùa khô tháng 10–4 trời quang; tránh mưa lớn dễ sạt lở.",
            "tips_vi": "Lái xe chậm, chắc tay vì đường hẹp nhiều khúc cua; dừng đúng nơi an toàn; mang áo ấm vì gió lạnh trên đỉnh.",
        },
        tags=["top", "mountain-pass", "viewpoint", "nature", "outdoor", "photo-spot"],
        review_vi="Du khách mô tả cảnh đèo và hẻm Nho Quế đẹp đến nghẹt thở, là trải nghiệm đáng nhớ nhất chuyến Hà Giang. Nhiều người khen đi thuyền dưới sông; một số nhắc đường đèo nguy hiểm, cần tay lái vững và không dừng xe tùy tiện.",
        sources=[
            {"title": "Wikipedia (EN) — Ma Pi Leng Pass", "url": "https://en.wikipedia.org/wiki/M%C3%A3_P%C3%AD_L%C3%A8ng_Pass"},
        ],
    ),
    rec(
        region="vn-tuyen-quang", region_name_vi="Tuyên Quang", fed="Miền Bắc",
        slug="cot-co-lung-cu", name_vi="Cột cờ Lũng Cú",
        name_en="Lung Cu Flag Tower", name_ru="Флаговая башня Лунгку",
        cats=["monument", "other"], lat=23.3636, lon=105.3161,
        addr="Xã Lũng Cú, huyện Đồng Văn cũ (Hà Giang), tỉnh Tuyên Quang",
        rating={"value": 4.7, "count": 8000, "source": "Google", "as_of": "2026-07"},
        short_vi="Cột cờ Lũng Cú là cột cờ thiêng liêng đánh dấu điểm cực Bắc của Tổ quốc, dựng trên đỉnh núi Rồng ở độ cao khoảng 1.470 m. Lá quốc kỳ rộng 54 m² tung bay tượng trưng cho 54 dân tộc, cùng tầm nhìn bao la ra vùng biên giới khiến nơi đây đầy xúc động.",
        short_en="Lung Cu Flag Tower is the revered marker near Vietnam's northernmost point, raised on Dragon Mountain at about 1,470 m. Its 54 m² national flag, symbolising the 54 ethnic groups, flies above a sweeping border panorama, making the spot deeply moving.",
        short_ru="Флаговая башня Лунгку — почитаемый знак у самой северной точки Вьетнама, воздвигнутый на Драконовой горе на высоте около 1470 м. Государственный флаг площадью 54 м², символизирующий 54 народа, реет над широкой панорамой границы, придавая месту особую волнующую силу.",
        long_vi="Nằm trên đỉnh núi Rồng thuộc xã Lũng Cú, gần điểm cực Bắc của Việt Nam, Cột cờ Lũng Cú từ lâu đã là biểu tượng thiêng liêng về chủ quyền và tinh thần dân tộc. Một cột cờ đã tồn tại ở vùng đất địa đầu này từ nhiều đời; công trình hiện nay được xây dựng kiên cố theo mô phỏng cột cờ Hà Nội, với thân bát giác trang trí phù điêu trống đồng Đông Sơn và hoa văn các dân tộc, vươn cao trên nền núi ở độ cao khoảng một nghìn bốn trăm bảy mươi mét so với mực nước biển. Trên đỉnh, lá quốc kỳ có diện tích năm mươi tư mét vuông tung bay lồng lộng, tượng trưng cho năm mươi tư dân tộc anh em của cả nước. Để lên tới chân cột, du khách vượt qua con đường và hàng trăm bậc thang uốn theo sườn núi; từ vọng đài trên cao, tầm mắt mở ra bát ngát: những thửa ruộng, bản làng người Mông, Lô Lô nằm nép giữa núi đá, và xa xa là đường biên giới với hai hồ nước được ví như 'mắt rồng'. Cảm giác đứng nơi cực Bắc, ngước nhìn lá cờ đỏ sao vàng in trên nền trời biên cương, khiến nhiều người xúc động và tự hào. Cột cờ Lũng Cú vì thế không chỉ là điểm tham quan mà còn là nơi hành hương thiêng liêng của du khách Việt khi đến cao nguyên đá.",
        long_en="On the summit of Dragon Mountain in Lung Cu commune, near Vietnam's northernmost point, Lung Cu Flag Tower has long been a sacred symbol of sovereignty and national spirit. A flag pole has stood in this frontier land for generations; the present structure is solidly built in the manner of the Hanoi flag tower, with an octagonal shaft decorated with Dong Son bronze-drum reliefs and ethnic motifs, rising on the mountain at about one thousand four hundred and seventy metres above sea level. At the top, a national flag of fifty-four square metres flies proudly, symbolising the country's fifty-four ethnic groups. To reach the base of the tower, visitors climb a road and hundreds of steps winding up the slope; from the high viewing gallery the eye ranges far and wide over fields, Hmong and Lo Lo villages nestled among the karst, and, in the distance, the border with two lakes likened to 'dragon's eyes'. Standing at the far north, looking up at the red flag with its gold star against the frontier sky, moves many with pride. Lung Cu Flag Tower is thus not only a sight but a sacred pilgrimage for Vietnamese travellers on the karst plateau.",
        long_ru="На вершине Драконовой горы в общине Лунгку, близ самой северной точки Вьетнама, Флаговая башня Лунгку издавна служит священным символом суверенитета и национального духа. Флагшток стоял на этой пограничной земле из поколения в поколение; нынешнее сооружение прочно возведено по образцу ханойской флаговой башни: восьмигранный ствол украшен рельефами бронзовых барабанов Донгшон и этническими мотивами и поднимается на горе на высоте около тысячи четырёхсот семидесяти метров над уровнем моря. На вершине гордо реет государственный флаг площадью пятьдесят четыре квадратных метра, символизируя пятьдесят четыре народа страны. Чтобы добраться до основания башни, гости преодолевают дорогу и сотни ступеней, вьющихся по склону; со смотровой галереи взгляд охватывает поля, деревни хмонг и лоло, укрытые среди карста, и вдали — границу с двумя озёрами, которые называют «глазами дракона». Стоять на крайнем севере, глядя на красный флаг с золотой звездой на пограничном небе, — волнующее переживание. Поэтому Лунгку — не только достопримечательность, но и священное место паломничества.",
        hi_vi=[
            "Cột cờ thiêng nơi điểm cực Bắc, trên đỉnh núi Rồng ~1.470 m",
            "Lá quốc kỳ 54 m² tượng trưng cho 54 dân tộc Việt Nam",
            "Thân cột bát giác chạm trống đồng Đông Sơn; view biên giới bát ngát",
        ],
        hi_en=[
            "A sacred flag tower near the northernmost point, on Dragon Mountain ~1,470 m",
            "A 54 m² national flag symbolising Vietnam's 54 ethnic groups",
            "Octagonal shaft with Dong Son drum reliefs; sweeping border views",
        ],
        hi_ru=[
            "Священная флаговая башня у крайней северной точки, на горе ~1470 м",
            "Флаг площадью 54 м², символ 54 народов Вьетнама",
            "Восьмигранный ствол с рельефами барабанов Донгшон; виды границы",
        ],
        practical={
            "hours_vi": "Mở cửa khoảng 7:00–18:00 hằng ngày.",
            "ticket_vi": "Vé vào tham khảo khoảng 25.000 VND/người (có thể thêm xe điện lên gần chân cột).",
            "duration_vi": "Khoảng 1–1,5 giờ (gồm leo bậc thang).",
            "best_time_vi": "Mùa khô tháng 10–4; sáng trời quang nhìn xa nhất.",
            "tips_vi": "Chuẩn bị sức để leo bậc; mang áo ấm và nước; đi giày thể thao; tránh ngày mưa mù hạn chế tầm nhìn.",
        },
        tags=["top", "monument", "viewpoint", "historic", "outdoor", "border"],
        review_vi="Du khách xúc động khi đứng nơi cực Bắc dưới lá cờ lớn và ngắm cảnh biên cương hùng vĩ. Nhiều người thấy đáng công leo bậc thang; một số nhắc nên đi ngày trời quang vì sương mù có thể che tầm nhìn.",
        sources=[
            {"title": "Wikipedia (VI) — Cột cờ Lũng Cú", "url": "https://vi.wikipedia.org/wiki/C%E1%BB%99t_c%E1%BB%9D_L%C5%A9ng_C%C3%BA"},
        ],
    ),
]

# ================= AN GIANG (Miền Nam) — bổ sung điểm Châu Đốc =================
PLACES += [
    rec(
        region="vn-an-giang", region_name_vi="An Giang", fed="Miền Nam",
        slug="mieu-ba-chua-xu", name_vi="Miếu Bà Chúa Xứ Núi Sam",
        name_en="Ba Chua Xu Temple (Sam Mountain)", name_ru="Храм Ба Чуа Сы (гора Сам)",
        cats=["church"], lat=10.6817, lon=105.0894,
        addr="Chân núi Sam, phường Núi Sam, TP. Châu Đốc, tỉnh An Giang",
        rating={"value": 4.6, "count": 18000, "source": "Google", "as_of": "2026-07"},
        short_vi="Miếu Bà Chúa Xứ Núi Sam ở Châu Đốc là một trong những điểm hành hương linh thiêng và đông khách bậc nhất miền Tây Nam Bộ. Lễ hội Vía Bà Chúa Xứ được UNESCO ghi danh Di sản văn hóa phi vật thể, mỗi năm đón hàng triệu người đến cầu tài lộc, bình an.",
        short_en="Ba Chua Xu Temple at Sam Mountain in Chau Doc is one of the most sacred and busiest pilgrimage sites in the Mekong Delta. Its Lady Chua Xu festival is inscribed by UNESCO as Intangible Cultural Heritage, drawing millions each year to pray for fortune and peace.",
        short_ru="Храм Ба Чуа Сы у горы Сам в Тяудоке — одно из самых священных и посещаемых мест паломничества дельты Меконга. Праздник Госпожи Чуа Сы внесён ЮНЕСКО в список нематериального наследия и ежегодно собирает миллионы людей, молящихся о достатке и покое.",
        long_vi="Nằm dưới chân núi Sam, cách trung tâm Châu Đốc khoảng năm cây số, Miếu Bà Chúa Xứ là ngôi miếu nổi tiếng linh thiêng bậc nhất vùng đồng bằng sông Cửu Long và là trái tim tín ngưỡng của cả một vùng biên giới Tây Nam. Tương truyền, pho tượng Bà được người dân phát hiện trên đỉnh núi Sam và rước xuống lập miếu thờ từ đầu thế kỷ 19; từ đó, danh tiếng hiển linh của Bà lan rộng, biến nơi đây thành trung tâm hành hương thu hút tín đồ khắp Nam Bộ và cả người Việt ở nước ngoài. Ngôi miếu được xây theo lối kiến trúc phương Đông bề thế, mái cong lợp ngói xanh, các hàng cột chạm khắc tinh xảo, gian chính điện trang nghiêm với tượng Bà ngồi uy nghi, quanh năm nghi ngút khói hương. Cao điểm là Lễ hội Vía Bà Chúa Xứ diễn ra vào tháng Tư âm lịch, với các nghi lễ tắm Bà, thỉnh sắc, túc yết và những đoàn người tấp nập dâng lễ; lễ hội này đã được UNESCO ghi danh là Di sản văn hóa phi vật thể đại diện của nhân loại. Du khách đến đây không chỉ để lễ bái, cầu tài lộc, bình an mà còn kết hợp tham quan lăng Thoại Ngọc Hầu, chùa Tây An và leo núi Sam ngắm toàn cảnh vùng biên giới. Sầm uất, linh thiêng và giàu bản sắc, miếu Bà là điểm đến tâm linh tiêu biểu của An Giang.",
        long_en="At the foot of Sam Mountain, about five kilometres from central Chau Doc, Ba Chua Xu Temple is among the most sacred shrines of the Mekong Delta and the spiritual heart of the whole southwestern border region. According to tradition, the statue of the Lady was found on the summit of Sam Mountain and brought down to a temple in the early nineteenth century; her reputation for miracles spread, making this a pilgrimage centre drawing devotees from all over the south and overseas Vietnamese. The temple is built in a grand Eastern style, with curved roofs of green tiles, intricately carved rows of columns and a solemn main hall where the majestic seated statue of the Lady is wreathed year-round in incense. The high point is the Lady Chua Xu festival in the fourth lunar month, with rites of bathing the statue and processions of offerings; this festival has been inscribed by UNESCO as Intangible Cultural Heritage of Humanity. Visitors come not only to worship and pray for fortune and peace but also to see the Thoai Ngoc Hau mausoleum and Tay An pagoda and to climb Sam Mountain for a panorama of the borderland. Bustling, sacred and rich in identity, the temple is a signature spiritual destination of An Giang.",
        long_ru="У подножия горы Сам, примерно в пяти километрах от центра Тяудока, храм Ба Чуа Сы — один из самых священных храмов дельты Меконга и духовное сердце всего юго-западного пограничья. По преданию, статую Госпожи нашли на вершине горы Сам и в начале XIX века перенесли в храм; слава о её чудесах распространилась, превратив это место в центр паломничества, притягивающий верующих со всего юга и вьетнамцев из-за рубежа. Храм построен в величественном восточном стиле: изогнутые крыши из зелёной черепицы, тонко резные ряды колонн и торжественный главный зал, где величавая сидящая статуя Госпожи круглый год окутана благовониями. Кульминация — праздник Госпожи Чуа Сы в четвёртом лунном месяце с обрядами омовения статуи и процессиями подношений; этот праздник внесён ЮНЕСКО в список нематериального наследия человечества. Гости приходят не только молиться о достатке и покое, но и осматривать мавзолей Тхоай Нгок Хау и пагоду Тэйан, а также подниматься на гору Сам ради панорамы пограничья. Оживлённый, священный и самобытный, храм — знаковая духовная цель Анзянга.",
        hi_vi=[
            "Điểm hành hương linh thiêng và đông khách bậc nhất miền Tây",
            "Lễ hội Vía Bà Chúa Xứ — Di sản văn hóa phi vật thể của UNESCO",
            "Kết hợp lăng Thoại Ngọc Hầu, chùa Tây An và leo núi Sam",
        ],
        hi_en=[
            "One of the most sacred, crowded pilgrimage sites in the delta",
            "The Lady Chua Xu festival — UNESCO Intangible Cultural Heritage",
            "Combined with the Thoai Ngoc Hau mausoleum, Tay An pagoda and Sam Mountain",
        ],
        hi_ru=[
            "Одно из самых священных и посещаемых мест паломничества дельты",
            "Праздник Госпожи Чуа Сы — нематериальное наследие ЮНЕСКО",
            "Сочетается с мавзолеем Тхоай Нгок Хау, пагодой Тэйан и горой Сам",
        ],
        practical={
            "hours_vi": "Mở cửa gần như cả ngày; đông nhất vào sáng sớm và mùa lễ hội.",
            "ticket_vi": "Miễn phí vào lễ; cẩn thận các dịch vụ chèo kéo, xem bói, bán nhang quanh khu vực.",
            "duration_vi": "Khoảng 1–2 giờ (thêm thời gian nếu leo núi Sam).",
            "best_time_vi": "Ngoài mùa lễ hội (tháng 4 âm lịch) nếu ngại quá đông; sáng sớm mát mẻ.",
            "tips_vi": "Ăn mặc kín đáo, giữ tư trang cẩn thận nơi đông người; từ chối dứt khoát các dịch vụ mời chào; tự mua nhang đèn với giá niêm yết.",
        },
        tags=["top", "temple", "pilgrimage", "festival", "culture", "unesco"],
        review_vi="Du khách cảm nhận không khí tâm linh sôi động và kiến trúc miếu bề thế; nhiều người đến cầu an, cầu tài đầu năm. Một số nhắc khu vực rất đông và có tình trạng chèo kéo, xin lộc, nên cảnh giác, giữ ví và hỏi giá trước khi dùng dịch vụ.",
        sources=[
            {"title": "Wikipedia (VI) — Miếu Bà Chúa Xứ Núi Sam", "url": "https://vi.wikipedia.org/wiki/Mi%E1%BA%BFu_B%C3%A0_Ch%C3%BAa_X%E1%BB%A9_n%C3%BAi_Sam"},
        ],
    ),
    rec(
        region="vn-an-giang", region_name_vi="An Giang", fed="Miền Nam",
        slug="rung-tram-tra-su", name_vi="Rừng tràm Trà Sư",
        name_en="Tra Su Cajuput Forest", name_ru="Мелалеуковый лес Тràшы",
        cats=["park_garden", "other"], lat=10.5878, lon=105.0578,
        addr="Xã Văn Giáo, thị xã Tịnh Biên cũ, tỉnh An Giang",
        rating={"value": 4.6, "count": 9000, "source": "Google", "as_of": "2026-07"},
        short_vi="Rừng tràm Trà Sư là khu rừng ngập nước tiêu biểu của vùng Tây sông Hậu, nổi tiếng với thảm bèo xanh mướt phủ kín mặt nước dưới tán tràm. Du khách đi xuồng máy rồi chuyển xuồng chèo tay len giữa rừng, ngắm chim cò và hệ sinh thái đất ngập nước phong phú.",
        short_en="Tra Su Cajuput Forest is a signature flooded forest west of the Hau River, famed for a vivid green carpet of duckweed covering the water beneath the melaleuca canopy. Visitors take a motorboat then a hand-paddled sampan through the forest to watch birds and rich wetland life.",
        short_ru="Мелалеуковый лес Тряшы — характерный затопленный лес к западу от реки Хау, знаменитый ярко-зелёным ковром ряски, покрывающим воду под пологом мелалеуки. Гости плывут на моторной лодке, затем на вёсельном сампане сквозь лес, наблюдая птиц и богатую жизнь водно-болотных угодий.",
        long_vi="Trải rộng khoảng gần một trăm năm mươi héc-ta ở vùng Bảy Núi, gần biên giới Campuchia, Rừng tràm Trà Sư là một trong những khu rừng ngập nước đẹp và được yêu thích nhất miền Tây Nam Bộ. Rừng được trồng và bảo vệ như một khu bảo tồn cảnh quan, đóng vai trò quan trọng trong việc điều hòa nguồn nước, cải thiện môi trường và giữ gìn đa dạng sinh học cho vùng Tây sông Hậu. Trải nghiệm kinh điển khi tới đây là hành trình 'hai chặng thuyền': du khách lên tắc ráng (xuồng máy) chạy dọc kênh dẫn vào rừng, rồi chuyển sang xuồng ba lá do người dân chèo tay, lặng lẽ luồn giữa hai hàng tràm. Điều làm nên vẻ đẹp mê hoặc của Trà Sư là lớp bèo tấm li ti phủ kín mặt nước, xanh mướt như một tấm thảm nhung, khiến chiếc xuồng như trôi trên nhung lụa. Rừng là nơi cư ngụ của nhiều loài chim nước, cò, vạc, cồng cộc cùng các loài cá, dơi và thực vật thủy sinh; vào chiều muộn, từng đàn chim bay về tổ tạo nên khung cảnh sống động. Trên khu vực có đài quan sát cao và cây cầu tre dài kỷ lục để du khách ngắm toàn cảnh rừng tràm. Yên bình, trong lành và giàu sức sống, Trà Sư là điểm đến sinh thái đặc trưng của An Giang.",
        long_en="Spreading over nearly one hundred and fifty hectares in the Seven Mountains area near the Cambodian border, Tra Su Cajuput Forest is one of the most beautiful and beloved flooded forests of the Mekong Delta. Planted and protected as a landscape reserve, it plays an important role in regulating water, improving the environment and preserving biodiversity west of the Hau River. The classic experience here is the two-stage boat journey: visitors ride a motor sampan along the canal into the forest, then transfer to a small hand-paddled boat that glides quietly between rows of melaleuca. What makes Tra Su so enchanting is the layer of tiny duckweed blanketing the water, a velvety green carpet so that the boat seems to drift over silk. The forest shelters many water birds, herons, night herons and cormorants, along with fish, bats and aquatic plants; in late afternoon flocks return to roost in a lively spectacle. The site has a tall observation tower and a record-length bamboo bridge for viewing the whole forest. Peaceful, fresh and teeming with life, Tra Su is a signature ecotourism destination of An Giang.",
        long_ru="Раскинувшийся почти на сто пятьдесят гектаров в районе Семи гор у камбоджийской границы, мелалеуковый лес Тряшы — один из красивейших и любимых затопленных лесов дельты Меконга. Высаженный и охраняемый как ландшафтный заповедник, он играет важную роль в регулировании воды, улучшении среды и сохранении биоразнообразия к западу от реки Хау. Классическое впечатление здесь — двухэтапное плавание: гости едут на моторном сампане по каналу в лес, затем пересаживаются в маленькую вёсельную лодку, тихо скользящую между рядами мелалеуки. Очарование Тряшы создаёт слой крошечной ряски, укрывающий воду бархатисто-зелёным ковром, так что лодка будто плывёт по шёлку. Лес служит домом множеству водных птиц — цаплям, кваквам и бакланам, а также рыбам, летучим мышам и водным растениям; под вечер стаи возвращаются на ночлег в живом зрелище. На территории есть высокая смотровая башня и бамбуковый мост рекордной длины. Тихий, свежий и полный жизни, Тряшы — характерная экотуристическая цель Анзянга.",
        hi_vi=[
            "Rừng ngập nước với thảm bèo xanh phủ kín mặt nước dưới tán tràm",
            "Trải nghiệm 'hai chặng thuyền': tắc ráng rồi xuồng chèo tay",
            "Sân chim đa dạng, đài quan sát và cầu tre dài kỷ lục",
        ],
        hi_en=[
            "A flooded forest with a green duckweed carpet under melaleuca",
            "The two-stage boat trip: motor sampan then hand-paddled boat",
            "A rich bird sanctuary, observation tower and record-length bamboo bridge",
        ],
        hi_ru=[
            "Затопленный лес с зелёным ковром ряски под мелалеукой",
            "Двухэтапное плавание: моторный сампан, затем вёсельная лодка",
            "Богатый птичий заказник, смотровая башня и рекордный бамбуковый мост",
        ],
        practical={
            "hours_vi": "Đón khách ban ngày, khoảng 7:00–17:00.",
            "ticket_vi": "Vé cổng và vé thuyền (tắc ráng + xuồng chèo) tham khảo khoảng 100.000–200.000 VND/người tùy gói.",
            "duration_vi": "Khoảng 2–3 giờ.",
            "best_time_vi": "Mùa nước nổi khoảng tháng 9–11 khi bèo xanh đẹp nhất; buổi sáng hoặc chiều mát để ngắm chim.",
            "tips_vi": "Đi sớm hoặc chiều để tránh nắng và xem chim về tổ; mang chống muỗi, mũ nón; ngồi yên khi xuồng chèo để không làm động chim.",
        },
        tags=["top", "nature", "boat", "birdwatching", "wetland", "outdoor", "photo-spot"],
        review_vi="Du khách thích cảm giác xuồng trôi trên thảm bèo xanh và không khí trong lành, chụp ảnh rất đẹp. Nhiều người khen đa dạng chim, cò; một số nhắc buổi trưa nắng và muỗi nhiều, nên đi sáng sớm hoặc chiều và mang theo đồ chống nắng, chống muỗi.",
        sources=[
            {"title": "Wikipedia (VI) — Rừng tràm Trà Sư", "url": "https://vi.wikipedia.org/wiki/R%E1%BB%ABng_tr%C3%A0m_Tr%C3%A0_S%C6%B0"},
        ],
    ),
]

# ================= LÂM ĐỒNG (Miền Trung) — hợp nhất Bình Thuận + Đắk Nông 1/7/2025 =================
PLACES += [
    rec(
        region="vn-lam-dong", region_name_vi="Lâm Đồng", fed="Miền Trung",
        slug="doi-cat-mui-ne", name_vi="Đồi cát bay Mũi Né",
        name_en="Mui Ne Sand Dunes", name_ru="Песчаные дюны Муйне",
        cats=["park_garden", "other"], lat=10.9497, lon=108.2869,
        addr="Phường Mũi Né, TP. Phan Thiết cũ, tỉnh Lâm Đồng",
        rating={"value": 4.3, "count": 11000, "source": "Google", "as_of": "2026-07"},
        short_vi="Đồi cát bay Mũi Né là những triền cát đỏ vàng trải rộng ven biển Phan Thiết, hình dáng luôn thay đổi theo gió nên gọi là 'cát bay'. Đây là điểm ngắm bình minh, hoàng hôn và trượt cát nổi tiếng, một biểu tượng du lịch của dải đất Bình Thuận xưa.",
        short_en="The Mui Ne Sand Dunes are sweeping red-gold dunes along the Phan Thiet coast whose shapes constantly shift with the wind, hence 'flying sand'. A famous spot for sunrise, sunset and sand-sledding, they are a tourism emblem of the former Binh Thuan area.",
        short_ru="Песчаные дюны Муйне — раскинувшиеся красно-золотые барханы у побережья Фантьета, чьи очертания постоянно меняет ветер, отчего их зовут «летящим песком». Знаменитое место для рассветов, закатов и катания по песку, они — туристический символ бывшего края Биньтхуан.",
        long_vi="Trải dài ven bờ biển đầy nắng gió của vùng Mũi Né – Phan Thiết, những đồi cát nơi đây là một trong những cảnh quan độc đáo và nổi tiếng nhất của dải đất Bình Thuận cũ, nay thuộc tỉnh Lâm Đồng sau sáp nhập. Có hai khu cát chính: đồi cát đỏ vàng gần Hòn Rơm với sắc màu rực rỡ đặc trưng, và đồi cát trắng (Bàu Trắng) rộng lớn hơn nằm cạnh hồ sen. Được gọi là 'đồi cát bay' bởi gió biển liên tục thổi khiến hình dáng và những đường vân trên cát thay đổi mỗi ngày, không bao giờ lặp lại; buổi sáng và chiều, khi nắng xiên chiếu, các triền cát chuyển màu từ vàng, cam đến hồng tím tuyệt đẹp, trở thành thiên đường của giới nhiếp ảnh. Du khách thường tới đây từ sớm để đón bình minh hoặc canh lúc hoàng hôn, thuê tấm trượt để lướt xuống các sườn dốc, hoặc đi xe địa hình băng qua biển cát mênh mông. Cảm giác đứng giữa những đụn cát nhấp nhô như tiểu sa mạc, phóng tầm mắt ra biển xanh phía xa, mang lại trải nghiệm rất khác biệt so với phần còn lại của Việt Nam. Kết hợp với bãi biển, làng chài, suối Tiên và các khu nghỉ dưỡng ven biển, đồi cát Mũi Né là điểm nhấn không thể bỏ qua khi du lịch vùng duyên hải Nam Trung Bộ.",
        long_en="Stretching along the sun-and-wind-swept coast of the Mui Ne and Phan Thiet area, these dunes are one of the most distinctive and famous landscapes of the former Binh Thuan region, now part of Lam Dong after the merger. There are two main sand areas: the red-gold dunes near Hon Rom with their vivid signature colour, and the larger white dunes (Bau Trang) beside a lotus lake. They are called 'flying dunes' because the sea wind constantly reshapes their contours and ripples day by day, never the same twice; in morning and late afternoon, when the light slants low, the slopes turn from gold and orange to pink and violet, a paradise for photographers. Visitors usually arrive early to catch sunrise or time their trip for sunset, rent a sled to glide down the slopes, or ride all-terrain vehicles across the vast sand. Standing among the rolling dunes like a miniature desert, gazing at the blue sea beyond, offers an experience quite unlike the rest of Vietnam. Combined with the beach, fishing village, Fairy Stream and coastal resorts, the Mui Ne dunes are an unmissable highlight of the south-central coast.",
        long_ru="Протянувшиеся вдоль залитого солнцем и ветром побережья района Муйне и Фантьета, эти дюны — один из самых характерных и знаменитых пейзажей бывшего края Биньтхуан, ныне части Ламдонга после слияния. Есть две основные песчаные зоны: красно-золотые дюны у Хонром с ярким фирменным цветом и более крупные белые дюны (Баучанг) у лотосового озера. Их зовут «летящими» потому, что морской ветер постоянно меняет очертания и рябь песка изо дня в день, никогда не повторяясь; утром и под вечер, когда свет падает низко, склоны переходят от золотого и оранжевого к розовому и фиолетовому — рай для фотографов. Гости обычно приезжают рано, чтобы застать рассвет или подгадать закат, берут доску, чтобы скатиться со склонов, или катаются на вездеходах по бескрайнему песку. Стоять среди волнистых барханов, будто в миниатюрной пустыне, глядя на синее море вдали, — переживание, совсем не похожее на остальной Вьетнам. В сочетании с пляжем, рыбацкой деревней, Сказочным ручьём и курортами дюны Муйне — обязательная жемчужина юго-центрального побережья.",
        hi_vi=[
            "Đồi cát đỏ vàng và cát trắng đổi hình theo gió — 'cát bay'",
            "Ngắm bình minh, hoàng hôn; trượt cát và xe địa hình",
            "Biểu tượng du lịch dải Bình Thuận, kết hợp biển và suối Tiên",
        ],
        hi_en=[
            "Red-gold and white dunes reshaped by the wind — 'flying sand'",
            "Sunrise, sunset, sand-sledding and ATV rides",
            "A tourism emblem of Binh Thuan, combined with beaches and Fairy Stream",
        ],
        hi_ru=[
            "Красно-золотые и белые дюны, меняемые ветром, — «летящий песок»",
            "Рассветы, закаты, катание по песку и на вездеходах",
            "Туристический символ Биньтхуана, рядом с пляжами и Сказочным ручьём",
        ],
        practical={
            "hours_vi": "Tự do; đẹp nhất lúc bình minh (khoảng 5:00–6:30) và hoàng hôn.",
            "ticket_vi": "Khu cát cơ bản miễn phí/vé nhỏ; thuê tấm trượt và xe địa hình tính phí riêng, nên hỏi giá trước.",
            "duration_vi": "Khoảng 1–2 giờ.",
            "best_time_vi": "Mùa khô tháng 11–4; đi sớm hoặc chiều muộn tránh nắng gắt và cát nóng.",
            "tips_vi": "Đội mũ, mang nước, kính chống cát; thỏa thuận rõ giá thuê trượt cát/xe; giữ máy ảnh tránh bụi cát.",
        },
        tags=["top", "dunes", "sunrise", "sunset", "viewpoint", "outdoor", "photo-spot"],
        review_vi="Du khách thích cảnh cát đổi màu lúc bình minh, hoàng hôn và trò trượt cát vui nhộn. Nhiều người khen view đẹp, lạ; một số phàn nàn nắng nóng buổi trưa và tình trạng chèo kéo thuê ván, nên đi sớm và thống nhất giá trước.",
        sources=[
            {"title": "Wikipedia (EN) — Mui Ne", "url": "https://en.wikipedia.org/wiki/Mui_Ne"},
        ],
    ),
]

# ================= TP. HỒ CHÍ MINH (Miền Nam) — hợp nhất Bình Dương + BR-VT 1/7/2025 =================
PLACES += [
    rec(
        region="vn-ho-chi-minh", region_name_vi="TP. Hồ Chí Minh", fed="Miền Nam",
        slug="dia-dao-cu-chi", name_vi="Địa đạo Củ Chi",
        name_en="Cu Chi Tunnels", name_ru="Тоннели Кучи",
        cats=["monument", "other"], lat=11.1442, lon=106.4636,
        addr="Khu di tích Địa đạo Củ Chi (Bến Dược/Bến Đình), xã An Nhơn Tây, TP. Hồ Chí Minh",
        rating={"value": 4.6, "count": 40000, "source": "Google", "as_of": "2026-07"},
        short_vi="Địa đạo Củ Chi là hệ thống đường hầm dài hơn 250 km do quân dân Củ Chi đào trong chiến tranh, trở thành biểu tượng của ý chí kiên cường. Du khách có thể chui thử hầm, xem bẫy, bếp Hoàng Cầm và tìm hiểu cuộc sống dưới lòng đất suốt những năm khốc liệt.",
        short_en="The Cu Chi Tunnels are a network of more than 250 km dug by the people and soldiers of Cu Chi during the war, a symbol of resilient will. Visitors can crawl through the tunnels, see traps, the Hoang Cam kitchen and learn about underground life through the harsh years.",
        short_ru="Тоннели Кучи — сеть протяжённостью более 250 км, вырытая жителями и бойцами Кучи во время войны и ставшая символом несгибаемой воли. Гости могут проползти по тоннелям, увидеть ловушки, кухню Хоангкам и узнать о подземной жизни в суровые годы.",
        long_vi="Nằm ở vùng đất thép Củ Chi, cách trung tâm Thành phố Hồ Chí Minh khoảng bảy mươi cây số về phía tây bắc, hệ thống địa đạo Củ Chi là một trong những di tích lịch sử nổi tiếng nhất Việt Nam và là điểm đến gây xúc động mạnh với du khách quốc tế. Được đào và mở rộng dần trong suốt hai cuộc kháng chiến, đặc biệt là thời kỳ chống Mỹ, mạng lưới đường hầm chằng chịt này có tổng chiều dài ước tính hơn hai trăm năm mươi cây số, gồm nhiều tầng với các phòng họp, bệnh xá, kho lương, bếp, giếng nước và lối thoát bí mật. Trong điều kiện bom đạn ác liệt, quân và dân Củ Chi đã sống, chiến đấu ngay dưới lòng đất, biến vùng này thành một 'pháo đài' ngầm khiến đối phương nhiều phen bất lực. Ngày nay, hai khu Bến Dược và Bến Đình được bảo tồn và mở cửa đón khách; tại đây, du khách được xem phim tư liệu, tham quan các đoạn hầm được gia cố và nới rộng để chui thử, tận mắt thấy những chiếc bẫy chông, cửa hầm ngụy trang tài tình, bếp Hoàng Cầm tỏa khói loãng khó phát hiện, cùng mô hình sinh hoạt và xưởng chế tạo vũ khí thô sơ. Trải nghiệm cúi mình bò qua đoạn hầm tối, chật hẹp và ngột ngạt giúp người ta phần nào hình dung sự gian khổ phi thường của những năm tháng chiến tranh. Địa đạo Củ Chi vì thế vừa là bài học lịch sử sống động, vừa là biểu tượng của tinh thần bền bỉ.",
        long_en="In the 'land of steel' of Cu Chi, about seventy kilometres northwest of central Ho Chi Minh City, the Cu Chi Tunnel system is one of Vietnam's most famous historical sites and a deeply moving destination for international visitors. Dug and gradually extended through two wars, especially the war against the United States, this dense network of tunnels is estimated at more than two hundred and fifty kilometres in total, arranged on several levels with meeting rooms, field clinics, food stores, kitchens, wells and secret exits. Under fierce bombardment, the people and soldiers of Cu Chi lived and fought underground, turning the area into a hidden fortress that repeatedly frustrated their opponents. Today the Ben Duoc and Ben Dinh sites are preserved and open to visitors; here travellers watch documentary footage, tour sections of tunnel that have been reinforced and widened for crawling, and see for themselves the spike traps, ingeniously camouflaged trapdoors, the Hoang Cam kitchen that dispersed smoke to avoid detection, and displays of daily life and rudimentary weapon workshops. Stooping through a dark, cramped, airless stretch of tunnel gives some sense of the extraordinary hardship of those war years. The Cu Chi Tunnels are thus both a vivid history lesson and a symbol of enduring resilience.",
        long_ru="В «стальной земле» Кучи, примерно в семидесяти километрах к северо-западу от центра Хошимина, система тоннелей Кучи — одна из самых знаменитых исторических достопримечательностей Вьетнама и глубоко волнующая цель для зарубежных гостей. Вырытая и постепенно расширявшаяся в двух войнах, особенно в войне против США, эта густая сеть тоннелей оценивается более чем в двести пятьдесят километров и располагается на нескольких уровнях с залами собраний, полевыми лазаретами, складами провизии, кухнями, колодцами и тайными выходами. Под жестокими бомбёжками жители и бойцы Кучи жили и сражались под землёй, превратив район в скрытую крепость, не раз ставившую противника в тупик. Сегодня участки Бендыок и Бендинь сохранены и открыты для посетителей; здесь путешественники смотрят документальные кадры, проходят по укреплённым и расширенным для ползания отрезкам тоннелей и своими глазами видят ловушки с кольями, искусно замаскированные люки, кухню Хоангкам, рассеивавшую дым, а также экспозиции быта и кустарные оружейные мастерские. Пробираясь согнувшись по тёмному, тесному и душному участку, отчасти ощущаешь необычайные тяготы военных лет. Поэтому тоннели Кучи — и живой урок истории, и символ стойкости.",
        hi_vi=[
            "Mạng đường hầm ước tính hơn 250 km, nhiều tầng dưới lòng đất",
            "Chui thử hầm, xem bẫy chông, cửa hầm ngụy trang và bếp Hoàng Cầm",
            "Di tích lịch sử biểu tượng của 'đất thép' Củ Chi",
        ],
        hi_en=[
            "A tunnel network estimated at over 250 km on several underground levels",
            "Crawl through tunnels; see spike traps, hidden trapdoors and the Hoang Cam kitchen",
            "An emblematic historic site of the 'land of steel'",
        ],
        hi_ru=[
            "Сеть тоннелей более 250 км на нескольких подземных уровнях",
            "Ползание по тоннелям; ловушки, скрытые люки и кухня Хоангкам",
            "Знаковая историческая достопримечательность «стальной земли»",
        ],
        practical={
            "hours_vi": "Mở cửa khoảng 7:00–17:00 hằng ngày.",
            "ticket_vi": "Vé vào tham khảo khoảng 35.000 VND (khách Việt) và cao hơn với khách nước ngoài; trường bắn tính phí riêng.",
            "duration_vi": "Khoảng 2–3 giờ (chưa kể di chuyển từ trung tâm).",
            "best_time_vi": "Mùa khô tháng 12–4; đi buổi sáng cho mát và vắng.",
            "tips_vi": "Mặc đồ gọn, giày bệt vì phải cúi bò; người sợ không gian hẹp nên cân nhắc; có thể đi tour ghép nửa ngày hoặc thuyền cao tốc trên sông Sài Gòn.",
        },
        tags=["top", "history", "war", "historic", "monument", "daytrip", "family"],
        review_vi="Du khách, đặc biệt khách quốc tế, đánh giá đây là trải nghiệm lịch sử ấn tượng và nhiều cảm xúc; hướng dẫn viên nhiệt tình. Một số nhắc đường hầm chật, nóng, không hợp người sợ không gian kín; nên đi sớm để tránh đông và nắng.",
        sources=[
            {"title": "Wikipedia (EN) — Cu Chi tunnels", "url": "https://en.wikipedia.org/wiki/C%E1%BB%A7_Chi_tunnels"},
        ],
    ),
    rec(
        region="vn-ho-chi-minh", region_name_vi="TP. Hồ Chí Minh", fed="Miền Nam",
        slug="con-dao", name_vi="Côn Đảo (Đặc khu Côn Đảo)",
        name_en="Con Dao Islands", name_ru="Острова Кондао",
        cats=["park_garden", "other"], lat=8.6931, lon=106.6094,
        addr="Đặc khu Côn Đảo, TP. Hồ Chí Minh (quần đảo ngoài khơi biển Đông)",
        rating={"value": 4.7, "count": 12000, "source": "Google", "as_of": "2026-07"},
        short_vi="Côn Đảo là quần đảo hoang sơ giữa biển Đông, nay là đặc khu thuộc TP. Hồ Chí Minh. Nơi đây kết hợp bãi biển đẹp, vườn quốc gia biển và hệ thống nhà tù lịch sử cùng nghĩa trang Hàng Dương, vừa là thiên đường nghỉ dưỡng vừa là chốn hành hương, tưởng niệm.",
        short_en="Con Dao is a pristine archipelago in the East Sea, now a special zone of Ho Chi Minh City. It blends beautiful beaches, a marine national park and historic prisons with Hang Duong Cemetery, at once a resort paradise and a place of pilgrimage and remembrance.",
        short_ru="Кондао — нетронутый архипелаг в Восточном море, ныне особая зона города Хошимин. Он сочетает прекрасные пляжи, морской национальный парк и исторические тюрьмы с кладбищем Хангзыонг — одновременно курортный рай и место паломничества и памяти.",
        long_vi="Nằm cách đất liền khoảng một trăm tám mươi cây số về phía đông nam, quần đảo Côn Đảo gồm mười sáu hòn đảo lớn nhỏ, trong đó Côn Sơn là đảo chính. Sau sắp xếp hành chính năm 2025, Côn Đảo trở thành đặc khu trực thuộc Thành phố Hồ Chí Minh. Vùng đất và biển đảo này mang trong mình hai vẻ đẹp đối lập mà hòa quyện: một bên là thiên nhiên hoang sơ tuyệt mỹ, một bên là chiều sâu lịch sử bi tráng. Về thiên nhiên, Côn Đảo sở hữu những bãi biển cát trắng nước trong như Đầm Trầu, Bãi Nhát, cùng Vườn quốc gia Côn Đảo bảo tồn rừng nguyên sinh, rạn san hô và là nơi rùa biển lên đẻ trứng mỗi mùa; đây là điểm lý tưởng để lặn ngắm san hô, ngắm rùa và tận hưởng sự yên tĩnh hiếm có. Về lịch sử, nơi đây từng là 'địa ngục trần gian' với hệ thống nhà tù do thực dân và chính quyền cũ dựng lên, giam cầm và đày ải hàng vạn chiến sĩ cách mạng và người yêu nước suốt hơn một thế kỷ; các di tích như Trại Phú Hải, 'chuồng cọp' và nghĩa trang Hàng Dương, nơi yên nghỉ của nữ anh hùng Võ Thị Sáu, khiến du khách lặng người. Nhiều người đến viếng nghĩa trang vào ban đêm để thắp hương tưởng niệm. Bình yên, linh thiêng và giàu ý nghĩa, Côn Đảo là điểm đến vừa để nghỉ dưỡng vừa để chiêm nghiệm.",
        long_en="About one hundred and eighty kilometres southeast of the mainland, the Con Dao archipelago comprises sixteen islands large and small, of which Con Son is the main one. After the 2025 administrative reorganisation, Con Dao became a special zone under Ho Chi Minh City. This land and sea hold two contrasting yet intertwined kinds of beauty: pristine, exquisite nature on one hand, tragic historical depth on the other. In nature, Con Dao boasts white-sand, clear-water beaches such as Dam Trau and Bai Nhat, along with Con Dao National Park, which protects primary forest and coral reefs and where sea turtles come ashore to nest each season; it is ideal for snorkelling over coral, watching turtles and enjoying rare tranquillity. In history, this was once a 'hell on earth', with prisons built by colonial and former regimes that held and tormented tens of thousands of revolutionaries and patriots for over a century; sites such as Phu Hai Camp, the 'tiger cages' and Hang Duong Cemetery, resting place of the heroine Vo Thi Sau, leave visitors stilled. Many pay their respects at the cemetery by night, lighting incense in remembrance. Peaceful, sacred and full of meaning, Con Dao is a destination both for rest and for reflection.",
        long_ru="Примерно в ста восьмидесяти километрах к юго-востоку от материка архипелаг Кондао состоит из шестнадцати островов, крупных и малых, главный из которых — Коншон. После административной реформы 2025 года Кондао стал особой зоной в составе города Хошимин. Эта земля и море хранят две контрастные, но переплетённые красоты: нетронутую изысканную природу и трагическую историческую глубину. В природном отношении Кондао славится пляжами с белым песком и прозрачной водой, такими как Дамчау и Байнят, а также национальным парком Кондао, охраняющим первичный лес и коралловые рифы, куда каждый сезон выходят откладывать яйца морские черепахи; это идеальное место для снорклинга, наблюдения за черепахами и редкого покоя. В историческом отношении здесь некогда был «ад на земле» с тюрьмами колониальных и прежних режимов, где более века содержали и мучили десятки тысяч революционеров и патриотов; такие места, как лагерь Фухай, «тигриные клетки» и кладбище Хангзыонг, где покоится героиня Во Тхи Шау, заставляют гостей замереть. Многие приходят к кладбищу ночью, зажигая благовония в память. Тихий, священный и полный смысла, Кондао — место и для отдыха, и для размышления.",
        hi_vi=[
            "Quần đảo hoang sơ, nay là đặc khu thuộc TP. Hồ Chí Minh",
            "Bãi biển đẹp, vườn quốc gia biển, mùa rùa lên đẻ trứng",
            "Nhà tù lịch sử và nghĩa trang Hàng Dương (mộ Võ Thị Sáu)",
        ],
        hi_en=[
            "A pristine archipelago, now a special zone of Ho Chi Minh City",
            "Lovely beaches, a marine national park and sea-turtle nesting season",
            "Historic prisons and Hang Duong Cemetery (grave of Vo Thi Sau)",
        ],
        hi_ru=[
            "Нетронутый архипелаг, ныне особая зона города Хошимин",
            "Прекрасные пляжи, морской нацпарк и сезон гнездования черепах",
            "Исторические тюрьмы и кладбище Хангзыонг (могила Во Тхи Шау)",
        ],
        practical={
            "hours_vi": "Đảo tham quan quanh năm; di tích nhà tù và bảo tàng mở ban ngày, nghĩa trang Hàng Dương nhiều người viếng về đêm.",
            "ticket_vi": "Vé tham quan di tích và vườn quốc gia thu phí riêng; tự do dạo biển.",
            "duration_vi": "Nên dành 2–3 ngày để trọn cả nghỉ dưỡng và di tích.",
            "best_time_vi": "Tháng 3–9 biển êm, thuận đi tàu/lặn; mùa rùa đẻ khoảng tháng 6–9.",
            "tips_vi": "Đặt vé máy bay hoặc tàu cao tốc sớm; giữ gìn môi trường biển, không xả rác; ăn mặc trang nghiêm khi viếng nghĩa trang, di tích.",
        },
        tags=["top", "island", "beach", "nature", "history", "diving", "pilgrimage"],
        review_vi="Du khách mô tả Côn Đảo yên bình, biển đẹp và giàu cảm xúc lịch sử; nhiều người xúc động khi viếng nghĩa trang Hàng Dương ban đêm. Một số nhắc chi phí ra đảo và ăn ở khá cao, nên đặt vé sớm và chuẩn bị lịch trình phù hợp thời tiết.",
        sources=[
            {"title": "Wikipedia (EN) — Côn Đảo", "url": "https://en.wikipedia.org/wiki/C%C3%B4n_%C4%90%E1%BA%A3o"},
        ],
    ),
]
# ===DATA===


def main():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    by_region = {}
    for p in PLACES:
        by_region.setdefault(p["region"], []).append(p)
    grand = 0
    for region, recs in sorted(by_region.items()):
        path = os.path.join(REG, region + ".json")
        existing = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
        if existing:
            shutil.copy(path, path + ".bak_add_" + ts)
        have = {r["slug"] for r in existing}
        added = 0
        for r in recs:
            if r["slug"] not in have:
                existing.append(r)
                have.add(r["slug"])
                added += 1
        json.dump(existing, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("%-22s +%d -> %d" % (region, added, len(existing)))
        grand += added
    print("TOTAL ADDED:", grand)


if __name__ == "__main__":
    main()
