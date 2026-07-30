# -*- coding: utf-8 -*-
"""Bổ sung địa điểm du lịch nổi tiếng còn thiếu cho tỉnh AN GIANG (mới, sau sáp nhập 1/7/2025).
An Giang mới = An Giang (cũ) + Kiên Giang (cũ); Phú Quốc là Đặc khu Phú Quốc thuộc An Giang.
Chèn an toàn: nạp -> append (bỏ qua slug đã có) -> ghi lại. Map links do retrofit_map_links.py sinh.
"""
import json, os, urllib.parse, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
F = os.path.join(ROOT, "data", "regions", "vn-an-giang.json")

REG = "vn-an-giang"
REG_NAME = "An Giang"
TODAY = "2026-07-28"


def src(name_en, name_vi):
    return [
        {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Special:Search?search=" + urllib.parse.quote(name_en)},
        {"title": "Wikipedia (VI)", "url": "https://vi.wikipedia.org/wiki/Special:Search?search=" + urllib.parse.quote(name_vi)},
    ]


def mk(slug, name_vi, name_en, name_ru, lat, lon, cats, address, tags, rec):
    d = {
        "id": f"{REG}-{slug}",
        "slug": slug,
        "region": REG,
        "country": "vietnam",
        "region_name_vi": REG_NAME,
        "federal_district": "Miền Nam",
        "name_vi": name_vi,
        "name_ru": name_ru,
        "name_en": name_en,
        "categories": cats,
        "coordinates": {"lat": lat, "lon": lon},
        "address_vi": address,
        "rating": rec.get("rating"),
        "review_summary_vi": rec.get("review_summary_vi", ""),
        "presentation_short_vi": rec["ps_vi"],
        "presentation_short_en": rec["ps_en"],
        "presentation_short_ru": rec["ps_ru"],
        "presentation_long_vi": rec["pl_vi"],
        "presentation_long_en": rec["pl_en"],
        "presentation_long_ru": rec["pl_ru"],
        "highlights_vi": rec["h_vi"],
        "highlights_en": rec["h_en"],
        "highlights_ru": rec["h_ru"],
        "practical": rec.get("practical", {}),
        "photo": None,
        "photo_credit": None,
        "official_site": rec.get("official_site"),
        "sources": src(name_en, name_vi),
        "tags": tags,
        "status": "enriched",
        "last_updated": TODAY,
    }
    return d


NEW = []

NEW.append(mk(
    "chua-ho-quoc", "Thiền viện Trúc Lâm Hộ Quốc (Chùa Hộ Quốc)",
    "Ho Quoc Zen Monastery (Ho Quoc Pagoda)", "Дзен-монастырь Хокуок (пагода Хокуок)",
    10.1287, 104.0286, ["church", "other"],
    "Ấp Suối Lớn, xã Dương Tơ, Đặc khu Phú Quốc, tỉnh An Giang",
    ["top", "temple", "viewpoint", "sea", "spiritual"],
    {
        "rating": {"value": 4.6, "count": 12000, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách khen ngôi thiền viện tựa núi hướng biển có kiến trúc gỗ trang nghiêm và tầm nhìn thoáng đãng ra vịnh. Nhiều người thấy không gian yên tĩnh, mát mẻ vào sáng sớm; một số lưu ý nên mặc kín đáo và tránh giờ trưa nắng gắt.",
        "ps_vi": "Thiền viện Trúc Lâm Hộ Quốc là ngôi chùa lớn nhất Phú Quốc, tựa lưng vào núi và hướng mặt ra biển Đông. Công trình bằng gỗ lim uy nghi trên triền dốc mang lại tầm nhìn khoáng đạt xuống vịnh, là điểm hành hương và ngắm cảnh nổi tiếng bậc nhất đảo ngọc.",
        "ps_en": "Ho Quoc Zen Monastery is the largest pagoda on Phu Quoc, set against a hillside and facing the open sea. Built largely of ironwood on a broad terrace, it offers sweeping views over the bay and is one of the island's most popular spots for pilgrimage and photography.",
        "ps_ru": "Дзен-монастырь Хокуок — самая большая пагода на острове Фукуок, стоящая у подножия горы и обращённая к морю. Возведённый в основном из железного дерева на широкой террасе, он открывает панораму залива и считается одним из главных мест паломничества и фотосъёмки на острове.",
        "pl_vi": "Thiền viện Trúc Lâm Hộ Quốc, thường gọi ngắn là chùa Hộ Quốc, là ngôi chùa lớn nhất và nổi tiếng nhất Phú Quốc. Khánh thành năm 2012, thiền viện toạ lạc trên sườn đồi ở ấp Suối Lớn, xã Dương Tơ, lưng tựa núi và mặt hướng ra biển Đông theo đúng thế phong thuỷ 'tựa sơn hướng thuỷ'. Quần thể được dựng chủ yếu bằng gỗ lim với cổng tam quan, sân rồng, chính điện và nhà tổ, chạm khắc tinh xảo mang đậm phong cách thiền phái Trúc Lâm Yên Tử. Từ khoảng sân rộng trước chính điện, du khách phóng tầm mắt xuống vùng biển xanh và những chiếc thuyền neo đậu phía dưới, đặc biệt đẹp vào lúc bình minh khi mặt trời nhô lên từ biển. Con đường bậc thang dẫn lên chùa được điểm tô bằng tượng và cây xanh, tạo cảm giác thanh tịnh. Không chỉ là nơi thờ tự và tu tập, chùa còn là điểm đến tâm linh kết hợp ngắm cảnh, thu hút đông đảo phật tử và khách du lịch. Từ ngày 1 tháng 7 năm 2025, Phú Quốc trở thành Đặc khu Phú Quốc trực thuộc tỉnh An Giang (trước đây thuộc tỉnh Kiên Giang).",
        "pl_en": "Ho Quoc Zen Monastery, usually shortened to Ho Quoc Pagoda, is the largest and best-known temple on Phu Quoc. Consecrated in 2012, it stands on a hillside in Suoi Lon hamlet, Duong To commune, its back to the mountains and its face to the sea, following the classic geomantic ideal of 'mountain behind, water ahead.' The complex is built mainly of ironwood, with a triple gate, a dragon courtyard, a main hall and an ancestral house, all finely carved in the style of the Truc Lam Zen school of Yen Tu. From the broad terrace before the main hall, visitors look down over turquoise water and moored fishing boats, a view that is especially striking at sunrise when the sun climbs straight out of the sea. A stone stairway lined with statues and greenery leads up to the temple, adding to its calm. More than a place of worship and meditation retreat, it is a spiritual destination combined with sightseeing that draws crowds of pilgrims and tourists alike. Since 1 July 2025, Phu Quoc has become the Phu Quoc Special Zone under An Giang Province (formerly part of Kien Giang Province).",
        "pl_ru": "Дзен-монастырь Хокуок, который часто называют просто пагодой Хокуок, — самый большой и известный храм острова Фукуок. Освящённый в 2012 году, он стоит на склоне холма в деревне Суойлон общины Зыонгто: гора за спиной, море впереди, согласно классическому принципу геомантии «гора позади, вода впереди». Комплекс построен в основном из железного дерева и включает тройные ворота, «драконий» двор, главный зал и дом предков, тонко украшенные резьбой в стиле дзен-школы Чуклам с горы Йентьы. С широкой террасы перед главным залом открывается вид на бирюзовую воду и стоящие на якоре рыбацкие лодки; особенно красиво здесь на рассвете, когда солнце поднимается прямо из моря. К храму ведёт каменная лестница, обрамлённая статуями и зеленью, что усиливает ощущение покоя. Это не только место поклонения и медитации, но и популярная смотровая площадка, куда стекаются и паломники, и туристы. С 1 июля 2025 года Фукуок стал особой зоной Фукуок в составе провинции Анзянг (ранее относился к провинции Кьензянг).",
        "h_vi": ["Ngôi chùa lớn nhất Phú Quốc, khánh thành năm 2012", "Kiến trúc gỗ lim theo phong cách thiền phái Trúc Lâm", "Sân chùa hướng biển Đông, ngắm bình minh tuyệt đẹp"],
        "h_en": ["Largest pagoda on Phu Quoc, consecrated in 2012", "Ironwood architecture in the Truc Lam Zen style", "Sea-facing terrace with spectacular sunrise views"],
        "h_ru": ["Самая большая пагода Фукуока, освящена в 2012 году", "Архитектура из железного дерева в стиле дзен Чуклам", "Терраса, обращённая к морю, с прекрасными рассветами"],
        "practical": {
            "hours_vi": "Mở cửa cả ngày, khoảng 6:00–18:00; nên đến sáng sớm.",
            "ticket_vi": "Miễn phí tham quan; công đức tuỳ tâm.",
            "duration_vi": "Khoảng 1–1,5 giờ.",
            "best_time_vi": "Bình minh hoặc sáng sớm; mùa khô tháng 11–4.",
            "tips_vi": "Mặc kín đáo, lịch sự; mang giày dễ leo bậc; kết hợp tham quan Nam đảo và An Thới.",
        },
    },
))

NEW.append(mk(
    "cau-hon", "Cầu Hôn (Kiss Bridge)",
    "Kiss Bridge (Cau Hon)", "Мост Поцелуя (Кау Хон)",
    10.0413, 103.9626, ["bridge", "monument"],
    "Thị trấn Hoàng Hôn (Sunset Town), An Thới, Đặc khu Phú Quốc, tỉnh An Giang",
    ["top", "viewpoint", "sea", "sunset", "architecture", "night"],
    {
        "rating": {"value": 4.5, "count": 5200, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách ấn tượng với cây cầu hai nhịp gần chạm nhau tạo dáng như một nụ hôn, đặc biệt lung linh lúc hoàng hôn và khi lên đèn. Nhiều người khen đây là nơi 'sống ảo' và ngắm hoàng hôn đẹp; một số nhắc buổi chiều khá đông và nắng.",
        "ps_vi": "Cầu Hôn là cây cầu đi bộ biểu tượng ở Thị trấn Hoàng Hôn, Nam Phú Quốc, do kiến trúc sư lừng danh Marco Casamonti thiết kế. Hai nhịp cầu vươn ra biển với khoảng hở nhỏ ở giữa, gợi hình ảnh một nụ hôn, trở thành điểm ngắm hoàng hôn và chụp ảnh nổi tiếng.",
        "ps_en": "Kiss Bridge is a landmark pedestrian bridge in Sunset Town, southern Phu Quoc, designed by the renowned architect Marco Casamonti. Its two spans reach out over the sea and almost touch, evoking a kiss, and it has become a celebrated spot for watching the sunset and taking photos.",
        "ps_ru": "Мост Поцелуя — знаковый пешеходный мост в «Городе заката» на юге Фукуока, спроектированный известным архитектором Марко Казамонти. Два его пролёта тянутся над морем и почти соприкасаются, напоминая поцелуй; это одно из любимых мест для встречи заката и фотографий.",
        "pl_vi": "Cầu Hôn (tiếng Anh: Kiss Bridge) là công trình biểu tượng nằm trong quần thể Thị trấn Hoàng Hôn (Sunset Town) ở An Thới, cực nam đảo Phú Quốc. Cây cầu đi bộ do kiến trúc sư người Ý nổi tiếng Marco Casamonti thiết kế, gồm hai nhịp cong vươn ra phía biển và gần như chạm vào nhau ở điểm cao nhất, chừa lại một khoảng hở nhỏ gợi liên tưởng đến khoảnh khắc trước một nụ hôn. Ý tưởng lãng mạn ấy khiến cây cầu nhanh chóng trở thành điểm 'phải đến' của giới trẻ và các cặp đôi. Từ trên cầu, du khách có thể phóng tầm mắt ra biển, ngắm quần đảo An Thới và đón hoàng hôn buông xuống mặt nước. Khi màn đêm bắt đầu, cả khu vực rực sáng ánh đèn, kết nối với show trình diễn nghệ thuật đa phương tiện 'Kiss of the Sea' ngay gần đó. Cầu Hôn là một phần trong nỗ lực biến Nam Phú Quốc thành trung tâm giải trí và nghỉ dưỡng cao cấp. Từ ngày 1 tháng 7 năm 2025, Phú Quốc trở thành Đặc khu Phú Quốc trực thuộc tỉnh An Giang (trước đây thuộc tỉnh Kiên Giang).",
        "pl_en": "Kiss Bridge is a signature structure within the Sunset Town complex at An Thoi, the southern tip of Phu Quoc. The pedestrian bridge was designed by the celebrated Italian architect Marco Casamonti and consists of two curving spans that reach toward the sea and almost meet at their highest point, leaving a small gap that suggests the instant before a kiss. That romantic idea quickly turned the bridge into a must-visit for young travellers and couples. From the deck, visitors gaze out to sea, take in the An Thoi archipelago and watch the sun sink into the water. After dark the whole area lights up and connects with the nearby multimedia art show 'Kiss of the Sea.' Kiss Bridge forms part of a broader effort to make southern Phu Quoc a hub of upscale leisure and resorts. Since 1 July 2025, Phu Quoc has become the Phu Quoc Special Zone under An Giang Province (formerly part of Kien Giang Province).",
        "pl_ru": "Мост Поцелуя — знаковое сооружение в составе комплекса «Город заката» в Антхое, на самой южной оконечности Фукуока. Пешеходный мост спроектировал знаменитый итальянский архитектор Марко Казамонти: две изогнутые части тянутся к морю и почти встречаются в высшей точке, оставляя небольшой зазор, который напоминает миг перед поцелуем. Эта романтическая идея быстро сделала мост обязательным для посещения у молодёжи и влюблённых пар. С настила открывается вид на море и архипелаг Антхой, а вечером здесь встречают закат, когда солнце опускается в воду. С наступлением темноты вся зона подсвечивается и связана с расположенным рядом мультимедийным шоу «Поцелуй моря». Мост Поцелуя — часть большого проекта по превращению юга Фукуока в центр премиального отдыха и курортов. С 1 июля 2025 года Фукуок стал особой зоной Фукуок в составе провинции Анзянг (ранее относился к провинции Кьензянг).",
        "h_vi": ["Do kiến trúc sư Marco Casamonti thiết kế, hai nhịp gần chạm như nụ hôn", "Điểm ngắm hoàng hôn và chụp ảnh nổi tiếng ở Nam đảo", "Gần show nghệ thuật đa phương tiện 'Kiss of the Sea'"],
        "h_en": ["Designed by Marco Casamonti; two spans nearly touch like a kiss", "Famous sunset and photo spot at the southern tip", "Next to the 'Kiss of the Sea' multimedia art show"],
        "h_ru": ["Проект Марко Казамонти: два пролёта почти соприкасаются, как поцелуй", "Известное место заката и фотосъёмки на юге острова", "Рядом с мультимедийным шоу «Поцелуй моря»"],
        "practical": {
            "hours_vi": "Khu vực mở cửa cả ngày; đẹp nhất buổi chiều đến tối.",
            "ticket_vi": "Vào cầu miễn phí; show 'Kiss of the Sea' bán vé riêng.",
            "duration_vi": "Khoảng 1–2 giờ (kết hợp dạo Sunset Town).",
            "best_time_vi": "Chiều muộn đón hoàng hôn và xem lên đèn.",
            "tips_vi": "Đến trước hoàng hôn để có chỗ đẹp; mang máy ảnh; ở lại xem show buổi tối.",
        },
    },
))

NEW.append(mk(
    "bai-truong", "Bãi Trường (Long Beach)",
    "Long Beach (Bai Truong)", "Пляж Лонг-Бич (Байчыонг)",
    10.1866, 103.9640, ["park_garden", "other"],
    "Xã Dương Tơ, Đặc khu Phú Quốc, tỉnh An Giang",
    ["beach", "sea", "sunset", "family", "resort"],
    {
        "rating": {"value": 4.4, "count": 7800, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích bãi biển dài, cát vàng và hoàng hôn đẹp cùng chuỗi resort, quán bar ven biển. Nhiều người nói đây là nơi lý tưởng để tắm biển và ngắm mặt trời lặn; một số nhắc vài đoạn bờ có rác theo mùa gió.",
        "ps_vi": "Bãi Trường (Long Beach) là bãi biển dài nhất Phú Quốc, trải hơn 20 km dọc bờ tây đảo. Với cát vàng, nước êm và loạt khu nghỉ dưỡng, quán bar hướng biển, đây là nơi tắm biển và ngắm hoàng hôn được yêu thích bậc nhất trên đảo.",
        "ps_en": "Long Beach (Bai Truong) is the longest beach on Phu Quoc, stretching more than 20 km along the island's west coast. With golden sand, calm water and a string of resorts and beach bars, it is one of the island's favourite places to swim and to watch the sunset.",
        "ps_ru": "Пляж Лонг-Бич (Байчыонг) — самый длинный пляж Фукуока, протянувшийся более чем на 20 км вдоль западного побережья острова. Золотистый песок, спокойная вода, вереница курортов и пляжных баров делают его одним из любимых мест для купания и встречи заката.",
        "pl_vi": "Bãi Trường, tên tiếng Anh là Long Beach, là bãi biển dài nhất và sôi động nhất Phú Quốc, kéo dài hơn hai mươi cây số dọc bờ tây của đảo, từ khu vực Dương Đông xuống phía nam. Bãi có cát vàng mịn thoai thoải, mặt nước êm và hầu như không có sóng lớn nên rất thích hợp để tắm và thư giãn. Do quay mặt về phía tây, đây được xem là một trong những nơi ngắm hoàng hôn đẹp nhất Việt Nam; mỗi chiều, cả dải bờ biển nhuộm sắc cam đỏ khi mặt trời từ từ lặn xuống Vịnh Thái Lan. Dọc bãi là chuỗi resort, khách sạn, nhà hàng hải sản và các quán bar bãi biển sôi động về đêm, biến nơi đây thành trung tâm nghỉ dưỡng của đảo. Du khách có thể tắm biển, chơi thể thao dưới nước, đi dạo hoặc nhâm nhi đồ uống ngắm hoàng hôn. Chính sự kết hợp giữa cảnh quan tự nhiên và tiện nghi du lịch khiến Bãi Trường trở thành điểm đến quen thuộc với hầu hết du khách khi đặt chân tới đảo ngọc. Từ ngày 1 tháng 7 năm 2025, Phú Quốc trở thành Đặc khu Phú Quốc trực thuộc tỉnh An Giang.",
        "pl_en": "Long Beach, or Bai Truong in Vietnamese, is the longest and liveliest beach on Phu Quoc, running more than twenty kilometres down the island's west coast from the Duong Dong area southward. Its golden sand shelves gently into calm, almost waveless water, making it ideal for swimming and lounging. Because it faces west, it is regarded as one of the finest places in Vietnam to watch the sunset; each evening the shore glows orange and red as the sun slips into the Gulf of Thailand. Along the beach runs a chain of resorts, hotels, seafood restaurants and beach bars that come alive after dark, making this the resort heart of the island. Visitors can swim, try water sports, stroll the sand or sip a drink while the light fades. It is precisely this blend of natural scenery and tourist comfort that makes Long Beach a place almost every visitor to the island passes through. Since 1 July 2025, Phu Quoc has become the Phu Quoc Special Zone under An Giang Province (formerly part of Kien Giang Province).",
        "pl_ru": "Лонг-Бич, по-вьетнамски Байчыонг, — самый длинный и оживлённый пляж Фукуока, протянувшийся более чем на двадцать километров вдоль западного побережья острова от района Зыонгдонг к югу. Золотистый песок полого уходит в спокойную, почти без волн воду, поэтому здесь удобно купаться и отдыхать. Поскольку пляж обращён на запад, он считается одним из лучших мест во Вьетнаме для наблюдения заката: каждый вечер берег окрашивается в оранжево-красные тона, когда солнце опускается в Сиамский залив. Вдоль пляжа тянется вереница курортов, отелей, рыбных ресторанов и пляжных баров, которые оживают после наступления темноты, что делает это место курортным сердцем острова. Гости купаются, занимаются водными видами спорта, гуляют по песку или потягивают напитки, любуясь угасающим светом. Именно сочетание природы и туристического комфорта превращает Лонг-Бич в место, через которое проходит почти каждый гость острова. С 1 июля 2025 года Фукуок стал особой зоной Фукуок в составе провинции Анзянг.",
        "h_vi": ["Bãi biển dài nhất Phú Quốc, hơn 20 km dọc bờ tây", "Một trong những nơi ngắm hoàng hôn đẹp nhất Việt Nam", "Trung tâm resort, nhà hàng và bar bãi biển của đảo"],
        "h_en": ["Longest beach on Phu Quoc, over 20 km along the west coast", "One of Vietnam's finest sunset-watching spots", "Resort, restaurant and beach-bar hub of the island"],
        "h_ru": ["Самый длинный пляж Фукуока, более 20 км вдоль западного берега", "Одно из лучших мест заката во Вьетнаме", "Центр курортов, ресторанов и пляжных баров острова"],
        "practical": {
            "hours_vi": "Bãi công cộng, mở cả ngày; đông và đẹp nhất buổi chiều.",
            "ticket_vi": "Miễn phí; một số khu bãi thuộc resort có dịch vụ riêng.",
            "duration_vi": "Nửa ngày đến cả ngày.",
            "best_time_vi": "Chiều muộn ngắm hoàng hôn; mùa khô tháng 11–4.",
            "tips_vi": "Chọn đoạn bờ gần resort để sạch và tiện dịch vụ; mang kem chống nắng; ở lại ngắm hoàng hôn.",
        },
    },
))

NEW.append(mk(
    "bai-ong-lang", "Bãi Ông Lang",
    "Ong Lang Beach", "Пляж Онгланг",
    10.2760, 103.9130, ["park_garden", "other"],
    "Xã Cửa Dương, Đặc khu Phú Quốc, tỉnh An Giang",
    ["beach", "sea", "sunset", "quiet", "nature"],
    {
        "rating": {"value": 4.4, "count": 3400, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách yêu thích bãi biển yên tĩnh, hoang sơ với các mũi đá, dừa xanh và resort nhỏ ấm cúng. Nhiều người khen thích hợp nghỉ dưỡng và ngắm hoàng hôn; một số nói bãi có đoạn đá, nên chọn khu cát để tắm.",
        "ps_vi": "Bãi Ông Lang nằm ở bờ tây Phú Quốc, phía bắc Dương Đông, nổi tiếng yên tĩnh và hoang sơ hơn Bãi Trường. Bãi cát xen những mũi đá, rặng dừa và nhiều khu nghỉ dưỡng nhỏ ẩn trong cây xanh, là nơi lý tưởng để thư giãn và ngắm hoàng hôn.",
        "ps_en": "Ong Lang Beach lies on Phu Quoc's west coast north of Duong Dong and is known for being quieter and more natural than Long Beach. Sand alternates with rocky points, coconut palms and small resorts tucked into greenery, making it an ideal place to relax and watch the sunset.",
        "ps_ru": "Пляж Онгланг находится на западном побережье Фукуока к северу от Зыонгдонга и известен тем, что он тише и первозданнее, чем Лонг-Бич. Песок чередуется со скалистыми мысами, кокосовыми пальмами и небольшими курортами, спрятанными в зелени, — идеальное место для отдыха и заката.",
        "pl_vi": "Bãi Ông Lang là một trong những bãi biển đẹp và bình yên nhất ở bờ tây Phú Quốc, nằm thuộc xã Cửa Dương, cách trung tâm Dương Đông khoảng bảy cây số về phía bắc. Khác với Bãi Trường dài và sôi động, Ông Lang mang vẻ hoang sơ, tĩnh lặng với những dải cát vàng xen kẽ các mũi đá nhô ra biển, tạo thành nhiều 'vịnh' nhỏ kín đáo. Rặng dừa nghiêng mình bên bờ cùng các khu nghỉ dưỡng nhỏ ẩn mình trong vườn cây khiến nơi đây được nhiều du khách chọn để nghỉ dưỡng, tránh xa ồn ào. Nước biển trong, đáy thoải, thích hợp để tắm và bơi lội; buổi chiều, bãi hướng tây trở thành điểm ngắm hoàng hôn tuyệt đẹp khi mặt trời chìm dần xuống biển. Quanh khu vực còn có vườn tiêu, nhà thùng nước mắm và các quán ăn hải sản dân dã để du khách khám phá. Với không gian riêng tư và cảnh quan tự nhiên, Bãi Ông Lang được xem là lựa chọn lý tưởng cho những ai muốn tìm một Phú Quốc chậm rãi, gần gũi thiên nhiên. Từ ngày 1 tháng 7 năm 2025, Phú Quốc trực thuộc tỉnh An Giang.",
        "pl_en": "Ong Lang Beach is one of the prettiest and most peaceful beaches on Phu Quoc's west coast, in Cua Duong commune about seven kilometres north of central Duong Dong. Unlike the long, busy Long Beach, Ong Lang feels wild and calm, with strips of golden sand broken by rocky headlands that create a series of small, secluded coves. Coconut palms lean over the shore and small resorts hide among garden greenery, so many travellers choose it for a quiet stay away from the crowds. The clear water and gently shelving seabed are good for swimming, and in the afternoon this west-facing beach becomes a superb sunset spot as the sun sinks into the sea. Nearby, visitors can explore pepper gardens, traditional fish-sauce workshops and simple seafood eateries. With its privacy and natural scenery, Ong Lang is regarded as an ideal choice for anyone seeking a slower, nature-close side of Phu Quoc. Since 1 July 2025, Phu Quoc has come under An Giang Province (formerly part of Kien Giang Province).",
        "pl_ru": "Пляж Онгланг — один из самых красивых и спокойных пляжей на западном побережье Фукуока, в общине Кыазыонг, примерно в семи километрах к северу от центра Зыонгдонга. В отличие от длинного и шумного Лонг-Бич, Онгланг кажется диким и умиротворённым: полосы золотистого песка прерываются скалистыми мысами, образующими цепочку небольших укромных бухт. Кокосовые пальмы склоняются к берегу, а маленькие курорты прячутся в садовой зелени, поэтому многие путешественники выбирают его для тихого отдыха вдали от толп. Прозрачная вода и полого уходящее дно удобны для купания, а во второй половине дня обращённый на запад пляж становится прекрасным местом для заката, когда солнце опускается в море. Рядом можно осмотреть перечные сады, традиционные мастерские по производству рыбного соуса и простые рыбные кафе. Благодаря уединённости и природным пейзажам Онгланг считается идеальным выбором для тех, кто ищет более неспешную и близкую к природе сторону Фукуока. С 1 июля 2025 года Фукуок относится к провинции Анзянг.",
        "h_vi": ["Bãi biển yên tĩnh, hoang sơ ở bờ tây, nhiều vịnh nhỏ", "Rặng dừa và resort nhỏ ẩn trong vườn cây", "Điểm ngắm hoàng hôn đẹp, gần vườn tiêu và nhà thùng nước mắm"],
        "h_en": ["Quiet, wild west-coast beach with small coves", "Coconut palms and small resorts in garden greenery", "Great sunset spot near pepper gardens and fish-sauce workshops"],
        "h_ru": ["Тихий первозданный пляж на западе с небольшими бухтами", "Кокосовые пальмы и маленькие курорты в зелени", "Отличное место заката рядом с перечными садами и цехами рыбного соуса"],
        "practical": {
            "hours_vi": "Bãi công cộng, mở cả ngày.",
            "ticket_vi": "Miễn phí; khu bãi thuộc resort có dịch vụ riêng.",
            "duration_vi": "Nửa ngày.",
            "best_time_vi": "Chiều muộn ngắm hoàng hôn; mùa khô tháng 11–4.",
            "tips_vi": "Chọn khu nhiều cát để tắm; thuê xe máy để dạo quanh; thử hải sản quán ven bãi.",
        },
    },
))

NEW.append(mk(
    "lang-chai-rach-vem", "Làng chài Rạch Vẹm",
    "Rach Vem Fishing Village", "Рыбацкая деревня Ратьвем",
    10.3930, 103.9290, ["other"],
    "Xã Gành Dầu, Đặc khu Phú Quốc, tỉnh An Giang",
    ["village", "sea", "food", "photo", "nature"],
    {
        "rating": {"value": 4.3, "count": 4100, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích thú ngắm hàng trăm con sao biển đỏ dưới làn nước cạn trong veo và những nhà hàng bè nổi bán hải sản tươi. Nhiều người khen bình dị, đáng đến; lưu ý không nên bắt sao biển lên khỏi mặt nước để bảo vệ chúng.",
        "ps_vi": "Làng chài Rạch Vẹm ở phía bắc Phú Quốc nổi tiếng với bãi cạn đầy sao biển đỏ và những nhà hàng bè nổi phục vụ hải sản tươi sống. Đây là điểm đến dân dã, đậm chất làng chài để ngắm sao biển, thưởng thức đặc sản và tận hưởng khung cảnh biển bình yên.",
        "ps_en": "Rach Vem Fishing Village in northern Phu Quoc is famous for shallows full of red starfish and floating raft restaurants serving fresh seafood. It is a rustic, authentic fishing-village destination for spotting starfish, sampling local dishes and enjoying calm sea views.",
        "ps_ru": "Рыбацкая деревня Ратьвем на севере Фукуока славится мелководьем, усыпанным красными морскими звёздами, и плавучими ресторанами на понтонах со свежими морепродуктами. Это колоритное аутентичное место, чтобы посмотреть на морских звёзд, попробовать местные блюда и полюбоваться спокойным морем.",
        "pl_vi": "Làng chài Rạch Vẹm nằm ở phía bắc đảo Phú Quốc, thuộc xã Gành Dầu, được du khách biết đến nhiều nhất với biệt danh 'làng sao biển'. Vùng nước nông ven bờ ở đây trong vắt và là nơi trú ngụ của hàng trăm con sao biển đỏ nằm rải rác dưới đáy cát, tạo nên khung cảnh độc đáo hiếm nơi nào có được. Du khách có thể lội xuống làn nước mát để ngắm, chụp ảnh với sao biển, nhưng được khuyến cáo không nên nhấc chúng khỏi mặt nước quá lâu để bảo vệ sinh vật. Điểm đặc trưng thứ hai của Rạch Vẹm là những nhà hàng bè nổi dựng trên cọc gỗ vươn ra biển, nơi phục vụ hải sản tươi vừa đánh bắt như ghẹ, tôm, cá, nhum với giá bình dân. Ngồi trên bè, thực khách vừa ăn vừa ngắm thuyền chài, nước biển xanh và những đảo nhỏ phía xa. Con đường dẫn tới làng đi qua rừng và vườn quê, mang lại trải nghiệm khác hẳn khu resort sầm uất. Rạch Vẹm vì thế là lựa chọn quen thuộc cho ai muốn cảm nhận nhịp sống làng chài mộc mạc của đảo ngọc. Từ ngày 1 tháng 7 năm 2025, Phú Quốc trực thuộc tỉnh An Giang.",
        "pl_en": "Rach Vem Fishing Village lies in the north of Phu Quoc, in Ganh Dau commune, and is best known by its nickname the 'starfish village.' The shallow water close to shore is crystal clear and home to hundreds of red starfish scattered across the sandy bottom, an unusual sight found in few other places. Visitors can wade into the cool water to look at and photograph the starfish, though they are urged not to lift them out of the water for long so as to protect the animals. Rach Vem's second trademark is its floating raft restaurants, built on wooden stilts reaching out over the sea, serving freshly caught seafood such as crab, prawns, fish and sea urchin at modest prices. Sitting on the rafts, diners eat while watching fishing boats, blue water and small islands in the distance. The road to the village runs through forest and rural gardens, offering an experience quite unlike the busy resort strips. Rach Vem is therefore a favourite for anyone who wants to feel the simple rhythm of island fishing life. Since 1 July 2025, Phu Quoc has come under An Giang Province.",
        "pl_ru": "Рыбацкая деревня Ратьвем расположена на севере Фукуока, в общине Заньзау, и больше всего известна под прозвищем «деревня морских звёзд». Мелководье у берега кристально чистое и служит домом для сотен красных морских звёзд, разбросанных по песчаному дну, — редкое зрелище, которое можно увидеть немногих местах. Гости заходят в прохладную воду, чтобы рассмотреть и сфотографировать звёзд, но их просят не поднимать надолго из воды, чтобы не навредить животным. Вторая визитная карточка Ратьвема — плавучие рестораны на деревянных сваях, уходящих в море, где подают только что выловленные морепродукты: крабов, креветок, рыбу и морских ежей по умеренным ценам. Сидя на понтонах, посетители едят и наблюдают за рыбацкими лодками, синей водой и небольшими островами вдали. Дорога к деревне идёт через лес и сельские сады, даря впечатление, совсем не похожее на оживлённые курортные кварталы. Поэтому Ратьвем — любимое место для тех, кто хочет почувствовать простой ритм островной рыбацкой жизни. С 1 июля 2025 года Фукуок относится к провинции Анзянг.",
        "h_vi": ["'Làng sao biển' với hàng trăm sao biển đỏ dưới nước nông", "Nhà hàng bè nổi bán hải sản tươi giá bình dân", "Khung cảnh làng chài mộc mạc ở bắc đảo"],
        "h_en": ["The 'starfish village' with hundreds of red starfish in the shallows", "Floating raft restaurants serving fresh, affordable seafood", "Rustic fishing-village scenery in the island's north"],
        "h_ru": ["«Деревня морских звёзд» с сотнями красных звёзд на мелководье", "Плавучие рестораны со свежими и недорогими морепродуктами", "Колоритные рыбацкие пейзажи на севере острова"],
        "practical": {
            "hours_vi": "Ban ngày; ngắm sao biển đẹp khi nước cạn và trong.",
            "ticket_vi": "Miễn phí; trả tiền theo món tại nhà hàng bè.",
            "duration_vi": "Khoảng 2–3 giờ.",
            "best_time_vi": "Sáng hoặc lúc thuỷ triều thấp, nước lặng và trong.",
            "tips_vi": "Không nhấc sao biển khỏi nước; đi giày lội nước; hỏi giá trước khi gọi hải sản.",
        },
    },
))

NEW.append(mk(
    "mui-ganh-dau", "Mũi Gành Dầu",
    "Ganh Dau Cape", "Мыс Заньзау",
    10.3520, 103.8340, ["other"],
    "Xã Gành Dầu, Đặc khu Phú Quốc, tỉnh An Giang",
    ["beach", "sea", "viewpoint", "nature", "sunset"],
    {
        "rating": {"value": 4.3, "count": 2600, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích mũi đất cực tây bắc đảo với bãi đá, nước trong và tầm nhìn xa sang phía Campuchia. Nhiều người khen yên tĩnh, hải sản tươi ngon; một số nói đường tới hơi xa nên kết hợp tham quan Nam đảo hoặc VinWonders gần đó.",
        "ps_vi": "Mũi Gành Dầu là dải đất nhô ra biển ở cực tây bắc Phú Quốc, nơi gần nhất nhìn sang bờ biển Campuchia. Bãi đá và nước trong xanh, làng chài yên bình cùng hải sản tươi khiến đây thành điểm dừng thú vị khi khám phá Bắc đảo.",
        "ps_en": "Ganh Dau Cape is a headland jutting into the sea at the far north-west of Phu Quoc, the closest point to the Cambodian coast. Its rocky shore and clear water, quiet fishing hamlet and fresh seafood make it a rewarding stop while exploring the island's north.",
        "ps_ru": "Мыс Заньзау — коса, вдающаяся в море на крайнем северо-западе Фукуока, ближайшая точка к побережью Камбоджи. Скалистый берег и прозрачная вода, тихая рыбацкая деревушка и свежие морепродукты делают его интересной остановкой при осмотре севера острова.",
        "pl_vi": "Mũi Gành Dầu là điểm cực tây bắc của đảo Phú Quốc, thuộc xã Gành Dầu, nơi bờ biển Việt Nam ở khoảng cách gần nhất với vùng biển Campuchia — trong ngày trời quang, du khách có thể nhìn thấy dải đất mờ xa của nước bạn. Mũi đất là một cung bờ biển cong hình vòng ôm lấy vịnh nhỏ, với bãi đá xen cát, nước trong xanh và những rặng cây rừng chạy sát mép sóng. Đây vốn là làng chài lâu đời, nên du khách vẫn bắt gặp thuyền neo đậu, ngư dân phơi lưới và các quán ăn phục vụ hải sản vừa đánh bắt với giá phải chăng. Từ mỏm đá cao, tầm nhìn mở rộng ra biển khơi, rất thích hợp để ngắm cảnh và đón hoàng hôn. Khu vực Gành Dầu ngày nay còn là cửa ngõ tới quần thể vui chơi, VinWonders và Vinpearl Safari ở Bắc đảo, nên nhiều đoàn thường kết hợp tham quan. Với vẻ hoang sơ và vị trí đặc biệt trên bản đồ, Mũi Gành Dầu mang lại trải nghiệm vừa nghỉ ngơi vừa 'chạm' tới ranh giới biển trời phía tây của Tổ quốc. Từ ngày 1 tháng 7 năm 2025, Phú Quốc trực thuộc tỉnh An Giang.",
        "pl_en": "Ganh Dau Cape is the far north-western point of Phu Quoc, in Ganh Dau commune, where the Vietnamese coast comes closest to Cambodian waters — on a clear day you can make out the hazy outline of the neighbouring country across the sea. The cape is a curving arm of shoreline that wraps around a small bay, with rocks mixed into the sand, clear blue water and forest running down almost to the waves. It has long been a fishing hamlet, so visitors still see moored boats, fishermen drying nets and eateries serving freshly caught seafood at reasonable prices. From the high rocks the view opens out to the open sea, ideal for sightseeing and catching the sunset. Today the Ganh Dau area is also the gateway to the amusement complex, VinWonders and Vinpearl Safari in the island's north, so many tours combine the visits. With its unspoiled feel and special place on the map, Ganh Dau offers both relaxation and the sense of touching the western sea-and-sky edge of the country. Since 1 July 2025, Phu Quoc has come under An Giang Province.",
        "pl_ru": "Мыс Заньзау — крайняя северо-западная точка Фукуока в общине Заньзау, где вьетнамский берег ближе всего подходит к камбоджийским водам: в ясный день можно различить туманные очертания соседней страны за морем. Мыс представляет собой изогнутую линию берега, обнимающую небольшую бухту, со скалами вперемешку с песком, прозрачной синей водой и лесом, спускающимся почти к волнам. Здесь издавна была рыбацкая деревня, поэтому гости и сейчас видят стоящие на якоре лодки, рыбаков, сушащих сети, и кафе с только что выловленными морепродуктами по разумным ценам. С высоких скал вид открывается на открытое море — идеально для прогулок и заката. Сегодня район Заньзау служит воротами к развлекательному комплексу, VinWonders и Vinpearl Safari на севере острова, поэтому многие туры совмещают посещения. Благодаря нетронутости и особому положению на карте мыс Заньзау дарит и отдых, и ощущение прикосновения к западной морской границе страны. С 1 июля 2025 года Фукуок относится к провинции Анзянг.",
        "h_vi": ["Điểm cực tây bắc Phú Quốc, gần nhất nhìn sang Campuchia", "Bãi đá, nước trong và làng chài yên bình", "Cửa ngõ tới VinWonders và Vinpearl Safari Bắc đảo"],
        "h_en": ["Far north-west point of Phu Quoc, closest view toward Cambodia", "Rocky shore, clear water and a quiet fishing hamlet", "Gateway to VinWonders and Vinpearl Safari in the north"],
        "h_ru": ["Крайняя северо-западная точка Фукуока, ближайший вид к Камбодже", "Скалистый берег, прозрачная вода и тихая рыбацкая деревня", "Ворота к VinWonders и Vinpearl Safari на севере острова"],
        "practical": {
            "hours_vi": "Ban ngày; đẹp lúc chiều muộn.",
            "ticket_vi": "Miễn phí.",
            "duration_vi": "Khoảng 1–2 giờ.",
            "best_time_vi": "Trời quang để nhìn xa; chiều muộn ngắm hoàng hôn.",
            "tips_vi": "Kết hợp tham quan Bắc đảo; thử hải sản làng chài; mang nước và mũ.",
        },
    },
))

NEW.append(mk(
    "suoi-da-ban", "Suối Đá Bàn",
    "Da Ban Stream", "Ручей Дабан",
    10.2650, 103.9830, ["park_garden", "other"],
    "Xã Cửa Dương, Đặc khu Phú Quốc, tỉnh An Giang",
    ["nature", "waterfall", "forest", "family", "swimming"],
    {
        "rating": {"value": 4.1, "count": 2900, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích con suối chảy qua rừng với những tảng đá phẳng lớn, nước mát để ngâm chân, tắm suối. Nhiều người khen mát mẻ, hợp gia đình; lưu ý mùa khô nước có thể ít, đẹp nhất vào mùa mưa.",
        "ps_vi": "Suối Đá Bàn là con suối rừng ở trung tâm Phú Quốc, chảy qua những phiến đá granit phẳng và rộng tựa mặt bàn — nguồn gốc của tên gọi. Dòng nước mát giữa rừng nguyên sinh là nơi tắm suối, dã ngoại được du khách và người dân địa phương ưa thích.",
        "ps_en": "Da Ban Stream is a forest stream in central Phu Quoc that flows over broad, flat granite slabs resembling tabletops, which give it its name ('da ban' means 'stone table'). Its cool water amid old-growth forest is a favourite spot for stream-bathing and picnics among visitors and locals alike.",
        "ps_ru": "Ручей Дабан — лесной ручей в центре Фукуока, текущий по широким плоским гранитным плитам, похожим на столешницы, отчего и получил название («дабан» — «каменный стол»). Прохладная вода среди старого леса — любимое место купания и пикников у туристов и местных жителей.",
        "pl_vi": "Suối Đá Bàn là một trong những con suối nổi tiếng nhất Phú Quốc, bắt nguồn từ dãy núi Hàm Ninh và chảy qua vùng rừng của xã Cửa Dương ở trung tâm đảo. Tên gọi 'Đá Bàn' xuất phát từ đặc điểm địa hình độc đáo: lòng suối trải đầy những phiến đá granit lớn, bề mặt phẳng và rộng như những chiếc bàn đá tự nhiên, nơi du khách có thể ngồi nghỉ, bày đồ ăn hay nằm phơi nắng. Dòng nước trong mát len qua rừng cây rậm rạp, tạo thành các vũng nhỏ để ngâm mình và tắm suối, đặc biệt dễ chịu giữa cái nắng nhiệt đới của đảo. Đường vào suối băng qua rừng và vườn tiêu, mang lại cảm giác khám phá thiên nhiên nguyên sơ khác hẳn không khí biển. Vào mùa mưa từ khoảng tháng 5 đến tháng 10, suối nhiều nước và chảy mạnh nhất, cảnh quan xanh tươi; mùa khô nước cạn hơn nhưng vẫn thích hợp dã ngoại. Với không gian mát mẻ, yên tĩnh và gần gũi, Suối Đá Bàn là điểm đến quen thuộc cho các gia đình và nhóm bạn muốn đổi gió khỏi bãi biển khi tới đảo ngọc. Từ ngày 1 tháng 7 năm 2025, Phú Quốc trực thuộc tỉnh An Giang.",
        "pl_en": "Da Ban Stream is one of Phu Quoc's best-known streams, rising in the Ham Ninh range and flowing through the forests of Cua Duong commune in the centre of the island. The name 'Da Ban' comes from a distinctive feature: the streambed is strewn with large granite slabs whose flat, broad surfaces look like natural stone tables, where visitors can sit, lay out food or sunbathe. The clear, cool water threads through dense forest to form small pools for soaking and bathing, wonderfully refreshing in the island's tropical heat. The path in passes through woodland and pepper gardens, giving a sense of exploring unspoiled nature quite different from the seaside. In the rainy season from about May to October the stream runs fullest and strongest and the scenery is lush green; in the dry season the water is lower but the place is still fine for a picnic. With its cool, quiet and intimate setting, Da Ban Stream is a familiar choice for families and groups of friends wanting a change from the beach. Since 1 July 2025, Phu Quoc has come under An Giang Province.",
        "pl_ru": "Ручей Дабан — один из самых известных ручьёв Фукуока; он берёт начало в горах Хамнинь и течёт через леса общины Кыазыонг в центре острова. Название «Дабан» связано с яркой особенностью: русло усыпано крупными гранитными плитами, чьи плоские широкие поверхности похожи на природные каменные столы, где можно сидеть, раскладывать еду или загорать. Прозрачная прохладная вода пробирается сквозь густой лес, образуя небольшие заводи для купания, что особенно приятно в тропической жаре острова. Тропа к ручью проходит через лес и перечные сады, создавая ощущение исследования нетронутой природы, совсем непохожее на морское побережье. В сезон дождей примерно с мая по октябрь ручей полноводнее и сильнее, а пейзаж пышно-зелёный; в сухой сезон воды меньше, но место по-прежнему хорошо для пикника. Благодаря прохладной, тихой и уютной атмосфере ручей Дабан — привычный выбор для семей и компаний друзей, желающих отдохнуть от пляжа. С 1 июля 2025 года Фукуок относится к провинции Анзянг.",
        "h_vi": ["Suối rừng với những phiến đá granit phẳng như bàn đá", "Vũng nước mát để ngâm mình, tắm suối giữa rừng", "Đẹp và nhiều nước nhất vào mùa mưa (tháng 5–10)"],
        "h_en": ["Forest stream with flat granite slabs like stone tables", "Cool pools for soaking and bathing in the woods", "Fullest and finest in the rainy season (May–Oct)"],
        "h_ru": ["Лесной ручей с плоскими гранитными плитами-«столами»", "Прохладные заводи для купания в лесу", "Полноводнее и красивее всего в сезон дождей (май–октябрь)"],
        "practical": {
            "hours_vi": "Ban ngày, khoảng 7:00–17:00.",
            "ticket_vi": "Vé vào tham khảo khoảng 10.000–20.000 VND (có thể thay đổi).",
            "duration_vi": "Khoảng 1,5–2 giờ.",
            "best_time_vi": "Mùa mưa tháng 5–10 nước nhiều; đi buổi sáng cho mát.",
            "tips_vi": "Mang dép chống trơn; cẩn thận đá trơn; giữ vệ sinh, mang rác về.",
        },
    },
))

NEW.append(mk(
    "cho-dem-phu-quoc", "Chợ đêm Phú Quốc (Chợ đêm Dinh Cậu)",
    "Phu Quoc Night Market (Dinh Cau Night Market)", "Ночной рынок Фукуока (Диньку)",
    10.2140, 103.9585, ["square_street", "other"],
    "Đường Bạch Đằng, phường Dương Đông, Đặc khu Phú Quốc, tỉnh An Giang",
    ["market", "food", "night", "shopping", "family"],
    {
        "rating": {"value": 4.1, "count": 15000, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích khu chợ đêm nhộn nhịp với hải sản tươi nướng tại chỗ, quà lưu niệm và đặc sản đảo như nước mắm, tiêu, ngọc trai. Nhiều người khen sôi động, nhiều món ngon; một số nhắc nên hỏi giá trước và mặc cả.",
        "ps_vi": "Chợ đêm Phú Quốc trên đường Bạch Đằng, trung tâm Dương Đông, là khu ẩm thực và mua sắm về đêm sôi động nhất đảo. Hàng dài quán hải sản nướng, chè, trái cây cùng gian hàng nước mắm, tiêu, ngọc trai và quà lưu niệm tạo nên không khí náo nhiệt mỗi tối.",
        "ps_en": "Phu Quoc Night Market on Bach Dang Street in central Duong Dong is the island's liveliest evening food and shopping zone. Rows of grilled-seafood stalls, dessert and fruit vendors, plus shops selling fish sauce, pepper, pearls and souvenirs, create a bustling atmosphere every night.",
        "ps_ru": "Ночной рынок Фукуока на улице Батьданг в центре Зыонгдонга — самая оживлённая вечерняя зона еды и покупок на острове. Ряды палаток с жареными морепродуктами, десертами и фруктами, а также лавки с рыбным соусом, перцем, жемчугом и сувенирами создают шумную атмосферу каждый вечер.",
        "pl_vi": "Chợ đêm Phú Quốc, còn gọi là chợ đêm Dinh Cậu, nằm trên đường Bạch Đằng ven sông Dương Đông, là trung tâm ẩm thực và mua sắm về đêm nhộn nhịp bậc nhất đảo ngọc. Khi mặt trời lặn, cả con phố dài bừng sáng đèn, hai bên là hàng loạt quán ăn bày biện hải sản tươi sống còn giãy trong bể như tôm, ghẹ, mực, hàu, nhum, ốc để khách chọn rồi chế biến tại chỗ. Hương thơm của đồ nướng lan khắp khu chợ, xen lẫn các gánh chè, kem, trái cây nhiệt đới và món ăn vặt địa phương. Bên cạnh ẩm thực, chợ còn có nhiều gian hàng bán đặc sản Phú Quốc nổi tiếng như nước mắm truyền thống, hạt tiêu, rượu sim, cùng ngọc trai, đồ mỹ nghệ từ vỏ ốc và quà lưu niệm. Không khí đông vui, tiếng rao mời và ánh đèn màu khiến đây trở thành nơi hầu như du khách nào cũng ghé một lần để thưởng thức hải sản và cảm nhận nhịp sống về đêm của đảo. Du khách nên hỏi giá và cân đong trước khi gọi món để tránh bất ngờ. Từ ngày 1 tháng 7 năm 2025, Phú Quốc trực thuộc tỉnh An Giang.",
        "pl_en": "Phu Quoc Night Market, also called Dinh Cau Night Market, runs along Bach Dang Street beside the Duong Dong River and is the island's busiest evening food and shopping hub. As the sun sets, the long street blazes with light, lined with eateries displaying live seafood in tanks — prawns, crab, squid, oysters, sea urchin and sea snails — for diners to pick and have cooked on the spot. The smell of grilling drifts through the market, mixing with vendors of sweet soups, ice cream, tropical fruit and local snacks. Beyond food, many stalls sell Phu Quoc's famous specialities: traditional fish sauce, pepper and sim-berry wine, along with pearls, shell handicrafts and souvenirs. The crowds, the calls of vendors and the coloured lights make this a place almost every visitor drops by at least once to eat seafood and feel the island's nightlife. It is wise to ask prices and check the weight before ordering to avoid surprises. Since 1 July 2025, Phu Quoc has come under An Giang Province.",
        "pl_ru": "Ночной рынок Фукуока, который также называют рынком Диньку, тянется вдоль улицы Батьданг у реки Зыонгдонг и является самым оживлённым вечерним центром еды и покупок на острове. С заходом солнца длинная улица заливается светом; вдоль неё стоят закусочные с живыми морепродуктами в аквариумах — креветками, крабами, кальмарами, устрицами, морскими ежами и улитками, — которых посетители выбирают и тут же готовят. Запах жаровен разносится по рынку, смешиваясь с ароматами сладких супов, мороженого, тропических фруктов и местных закусок. Помимо еды, множество лавок торгует знаменитыми деликатесами Фукуока: традиционным рыбным соусом, перцем и вином из ягод сим, а также жемчугом, изделиями из раковин и сувенирами. Толпы, зазывания торговцев и цветные огни делают это место таким, куда почти каждый гость заходит хотя бы раз, чтобы поесть морепродуктов и ощутить ночную жизнь острова. Стоит заранее спрашивать цену и проверять вес, чтобы избежать неожиданностей. С 1 июля 2025 года Фукуок относится к провинции Анзянг.",
        "h_vi": ["Khu ẩm thực đêm sôi động nhất Phú Quốc trên đường Bạch Đằng", "Hải sản tươi chọn và chế biến tại chỗ", "Bán đặc sản đảo: nước mắm, tiêu, rượu sim, ngọc trai"],
        "h_en": ["Phu Quoc's liveliest night food zone on Bach Dang Street", "Live seafood picked and cooked on the spot", "Island specialities: fish sauce, pepper, sim wine, pearls"],
        "h_ru": ["Самая оживлённая ночная зона еды Фукуока на улице Батьданг", "Живые морепродукты на выбор, готовят на месте", "Островные деликатесы: рыбный соус, перец, вино сим, жемчуг"],
        "practical": {
            "hours_vi": "Khoảng 17:00–23:00 hằng ngày.",
            "ticket_vi": "Vào cổng miễn phí; trả tiền theo món.",
            "duration_vi": "Khoảng 1,5–2 giờ.",
            "best_time_vi": "Buổi tối, đông vui nhất khoảng 19:00–21:00.",
            "tips_vi": "Hỏi giá và cân trước khi gọi; mặc cả khi mua quà; giữ ví cẩn thận nơi đông người.",
        },
    },
))

NEW.append(mk(
    "vqg-phu-quoc", "Vườn quốc gia Phú Quốc",
    "Phu Quoc National Park", "Национальный парк Фукуок",
    10.3960, 104.0050, ["park_garden", "other"],
    "Phía bắc đảo, Đặc khu Phú Quốc, tỉnh An Giang",
    ["nature", "forest", "unesco", "trekking", "biosphere"],
    {
        "rating": {"value": 4.4, "count": 3200, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách đánh giá cao khu rừng nguyên sinh rộng lớn với hệ động thực vật phong phú, đường trekking và suối rừng. Nhiều người khuyên nên có hướng dẫn viên; lưu ý mang chống côn trùng và đi vào mùa khô để thuận lợi.",
        "ps_vi": "Vườn quốc gia Phú Quốc bao phủ phần lớn phía bắc đảo, là khu rừng nguyên sinh nằm trong Khu dự trữ sinh quyển thế giới Kiên Giang được UNESCO công nhận. Rừng rậm, suối và đa dạng sinh học phong phú tạo nên điểm đến hấp dẫn cho trekking và khám phá thiên nhiên.",
        "ps_en": "Phu Quoc National Park covers most of the island's north, an old-growth forest within the UNESCO-recognised Kien Giang World Biosphere Reserve. Dense woodland, streams and rich biodiversity make it a compelling destination for trekking and exploring nature.",
        "ps_ru": "Национальный парк Фукуок занимает большую часть севера острова — это старовозрастный лес в составе биосферного заповедника Кьензянг, признанного ЮНЕСКО. Густой лес, ручьи и богатое биоразнообразие делают его привлекательным местом для треккинга и знакомства с природой.",
        "pl_vi": "Vườn quốc gia Phú Quốc trải rộng trên phần lớn diện tích phía bắc và đông bắc đảo, bảo tồn một trong những vùng rừng nhiệt đới nguyên sinh còn nguyên vẹn hiếm hoi trên các đảo của Việt Nam. Khu vườn là hạt nhân của Khu dự trữ sinh quyển thế giới Kiên Giang được UNESCO công nhận năm 2006, với hệ sinh thái đa dạng gồm rừng thường xanh, rừng tràm, rừng ngập mặn ven biển và các dòng suối. Nơi đây là mái nhà của nhiều loài động thực vật quý, trong đó có các loài chim, thú và cây gỗ đặc hữu, cùng thảm thực vật xanh tốt quanh năm. Du khách yêu thiên nhiên có thể tham gia các tuyến đi bộ xuyên rừng, ngắm chim, khám phá suối và tìm hiểu công tác bảo tồn. So với các bãi biển sôi động ở phía nam, vườn quốc gia mang lại một Phú Quốc hoang sơ, mát mẻ và tĩnh lặng, nhấn mạnh giá trị sinh thái đặc biệt của đảo. Việc tham quan thường cần theo tuyến quy định và nên có hướng dẫn viên để an toàn và bảo vệ rừng. Từ ngày 1 tháng 7 năm 2025, Phú Quốc trực thuộc tỉnh An Giang.",
        "pl_en": "Phu Quoc National Park spreads over most of the island's north and north-east, protecting one of the few intact primary tropical forests left on Vietnam's islands. The park is the core of the Kien Giang World Biosphere Reserve, recognised by UNESCO in 2006, with a varied ecosystem of evergreen forest, melaleuca forest, coastal mangroves and streams. It is home to many precious plants and animals, including endemic birds, mammals and timber trees, amid greenery that stays lush year-round. Nature-loving visitors can join forest walks, watch birds, explore streams and learn about conservation work. Compared with the busy beaches of the south, the national park offers a wild, cool and quiet side of Phu Quoc that underlines the island's special ecological value. Visits usually follow set trails and are best done with a guide for safety and to protect the forest. Since 1 July 2025, Phu Quoc has come under An Giang Province (formerly part of Kien Giang Province).",
        "pl_ru": "Национальный парк Фукуок раскинулся на большей части севера и северо-востока острова, сохраняя один из немногих уцелевших нетронутых первичных тропических лесов на островах Вьетнама. Парк — ядро биосферного заповедника Кьензянг, признанного ЮНЕСКО в 2006 году, с разнообразной экосистемой из вечнозелёного леса, мелалеуковых зарослей, прибрежных мангров и ручьёв. Здесь обитает множество ценных растений и животных, включая эндемичных птиц, млекопитающих и деревья, среди зелени, которая остаётся пышной круглый год. Любители природы могут отправиться на лесные прогулки, наблюдать за птицами, исследовать ручьи и узнавать о работе по охране природы. По сравнению с оживлёнными пляжами юга парк открывает дикую, прохладную и тихую сторону Фукуока, подчёркивая особую экологическую ценность острова. Осмотр обычно проходит по установленным маршрутам, и его лучше совершать с гидом ради безопасности и защиты леса. С 1 июля 2025 года Фукуок относится к провинции Анзянг.",
        "h_vi": ["Rừng nguyên sinh chiếm phần lớn bắc đảo Phú Quốc", "Hạt nhân Khu dự trữ sinh quyển thế giới Kiên Giang (UNESCO 2006)", "Trekking, ngắm chim và khám phá suối rừng"],
        "h_en": ["Primary forest covering most of northern Phu Quoc", "Core of the UNESCO Kien Giang Biosphere Reserve (2006)", "Trekking, bird-watching and forest-stream exploring"],
        "h_ru": ["Первичный лес на большей части севера Фукуока", "Ядро биосферного заповедника Кьензянг ЮНЕСКО (2006)", "Треккинг, наблюдение за птицами и лесные ручьи"],
        "practical": {
            "hours_vi": "Ban ngày; tuỳ tuyến và trạm kiểm lâm.",
            "ticket_vi": "Một số tuyến/khu có phí; nên liên hệ đơn vị tổ chức tour.",
            "duration_vi": "Nửa ngày đến cả ngày tuỳ tuyến.",
            "best_time_vi": "Mùa khô tháng 11–4 thuận lợi đi rừng.",
            "tips_vi": "Nên có hướng dẫn viên; mang chống côn trùng, nước, giày đi rừng; không xả rác, không bắt động vật.",
        },
    },
))

NEW.append(mk(
    "lang-mac-cuu", "Lăng Mạc Cửu (Núi Bình San)",
    "Mac Cuu Tomb (Binh San Hill)", "Гробница Мак Кыу (холм Биньшан)",
    10.3835, 104.4835, ["monument", "fortress", "other"],
    "Chân núi Bình San, phường Bình San, Hà Tiên, tỉnh An Giang",
    ["history", "heritage", "viewpoint", "spiritual"],
    {
        "rating": {"value": 4.5, "count": 2300, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách đánh giá cao quần thể lăng mộ cổ tựa lưng vào núi Bình San, tri ân dòng họ Mạc đã khai phá Hà Tiên. Nhiều người khen yên tĩnh, cổ kính, tầm nhìn đẹp; lưu ý leo bậc lên các phần mộ trên cao.",
        "ps_vi": "Lăng Mạc Cửu nằm dưới chân núi Bình San, là quần thể lăng mộ và đền thờ dòng họ Mạc — những người có công khai phá và xây dựng vùng đất Hà Tiên từ thế kỷ 17–18. Di tích cổ kính tựa núi, xếp bậc theo triền dốc, là điểm về nguồn quan trọng của vùng biên viễn Tây Nam.",
        "ps_en": "Mac Cuu Tomb stands at the foot of Binh San Hill, a complex of mausoleums and shrines to the Mac clan who opened up and built the land of Ha Tien in the 17th–18th centuries. The ancient site, backed by the hill and terraced up the slope, is an important place of remembrance in the far south-west.",
        "ps_ru": "Гробница Мак Кыу расположена у подножия холма Биньшан — это комплекс мавзолеев и святилищ рода Мак, который осваивал и обустраивал землю Хатьен в XVII–XVIII веках. Древний памятник, прислонённый к холму и террасами поднимающийся по склону, — важное место памяти на дальнем юго-западе страны.",
        "pl_vi": "Lăng Mạc Cửu, còn gọi là Núi Lăng, là quần thể lăng mộ của dòng họ Mạc tọa lạc dưới chân và trên triền núi Bình San ở thành phố Hà Tiên. Mạc Cửu là người gốc Hoa đã đến khai khẩn, mở mang vùng Hà Tiên vào cuối thế kỷ 17, biến nơi đây thành một thương cảng sầm uất; con ông là Mạc Thiên Tứ tiếp tục phát triển và dâng đất về với chúa Nguyễn. Để tưởng nhớ công lao ấy, khu lăng được xây dựng trong các năm 1735–1739, gồm hàng chục ngôi mộ cổ của Mạc Cửu, con cháu và thân tộc, sắp xếp theo thế phong thuỷ tựa lưng vào núi, mặt hướng ra biển. Kiến trúc lăng mang phong cách Á Đông với tượng đá, bia đá, tượng linh thú và những bậc thang dẫn lên các phần mộ ở lưng chừng núi. Dưới chân núi có đền thờ họ Mạc, quanh năm khói hương. Từ các bậc cao, du khách có thể phóng tầm mắt ra thị xã Hà Tiên, đầm Đông Hồ và biển. Đây là di tích lịch sử — văn hoá cấp quốc gia, gắn liền với quá trình mở cõi phương Nam và là điểm về nguồn ý nghĩa của vùng biên giới Tây Nam. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Mac Cuu Tomb, also called Lang Hill, is the burial complex of the Mac clan set at the foot and on the slope of Binh San Hill in Ha Tien. Mac Cuu was an ethnic-Chinese settler who came to open up Ha Tien in the late 17th century, turning it into a thriving trading port; his son Mac Thien Tu developed it further and offered the land to the Nguyen lords. To honour their contribution, the mausoleum was built in 1735–1739 and holds dozens of ancient tombs of Mac Cuu, his descendants and kin, laid out by geomantic principle with the hill behind and the sea in front. The architecture is East Asian in style, with stone statues, stelae, guardian-animal figures and stairways climbing to graves partway up the hill. At the foot stands a shrine to the Mac clan, kept fragrant with incense all year. From the higher steps, visitors look out over Ha Tien town, Dong Ho Lagoon and the sea. A nationally ranked historical-cultural relic, it is tied to the southward expansion of the country and is a meaningful pilgrimage in the south-western borderland. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Гробница Мак Кыу, которую также называют «холм-усыпальница», — погребальный комплекс рода Мак у подножия и на склоне холма Биньшан в городе Хатьен. Мак Кыу был переселенцем китайского происхождения, который в конце XVII века пришёл осваивать Хатьен и превратил его в оживлённый торговый порт; его сын Мак Тхьен Ты продолжил развитие и передал землю под власть князей Нгуен. В память об их заслугах мавзолей был построен в 1735–1739 годах и хранит десятки старинных могил Мак Кыу, его потомков и родни, расположенных по правилам геомантии: холм за спиной, море впереди. Архитектура выдержана в восточноазиатском стиле — каменные статуи, стелы, фигуры животных-стражей и лестницы, поднимающиеся к могилам на склоне. У подножия стоит святилище рода Мак, круглый год наполненное благовониями. С верхних ступеней открывается вид на город Хатьен, лагуну Донгхо и море. Это памятник истории и культуры национального значения, связанный с продвижением страны на юг и служащий значимым местом паломничества в юго-западном пограничье. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Quần thể lăng mộ dòng họ Mạc, xây 1735–1739", "Tựa lưng núi Bình San, hướng ra biển theo thế phong thuỷ", "Di tích lịch sử — văn hoá cấp quốc gia của Hà Tiên"],
        "h_en": ["Burial complex of the Mac clan, built 1735–1739", "Backed by Binh San Hill and facing the sea by geomancy", "Nationally ranked historical-cultural relic of Ha Tien"],
        "h_ru": ["Погребальный комплекс рода Мак, построен в 1735–1739", "Холм Биньшан за спиной, лицом к морю по геомантии", "Памятник истории и культуры национального значения в Хатьене"],
        "practical": {
            "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
            "ticket_vi": "Miễn phí; công đức tuỳ tâm.",
            "duration_vi": "Khoảng 1 giờ.",
            "best_time_vi": "Sáng sớm hoặc chiều mát; tránh giữa trưa.",
            "tips_vi": "Mặc lịch sự; mang giày dễ leo bậc; kết hợp thăm chùa Phù Dung và đầm Đông Hồ gần đó.",
        },
    },
))

NEW.append(mk(
    "chua-phu-dung", "Chùa Phù Dung (Phù Cừ Am Tự)",
    "Phu Dung Pagoda", "Пагода Фузунг",
    10.3850, 104.4790, ["church", "other"],
    "Chân núi Bình San, phường Bình San, Hà Tiên, tỉnh An Giang",
    ["temple", "history", "spiritual", "legend"],
    {
        "rating": {"value": 4.4, "count": 1500, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích ngôi chùa cổ gắn với truyền thuyết nàng Phù Cừ, không gian tĩnh lặng dưới chân núi. Nhiều người khen cổ kính, nhiều cây xanh; thường ghé cùng lăng Mạc Cửu.",
        "ps_vi": "Chùa Phù Dung, tên chữ Phù Cừ Am Tự, là ngôi chùa cổ dưới chân núi Bình San ở Hà Tiên, gắn với truyền thuyết bi thương về nàng Phù Cừ và Mạc Thiên Tứ. Không gian trầm mặc, nhiều cổ vật và mộ tháp khiến đây thành điểm tâm linh — lịch sử đặc sắc của vùng.",
        "ps_en": "Phu Dung Pagoda, formally Phu Cu Am Tu, is an old temple at the foot of Binh San Hill in Ha Tien, linked to a poignant legend about the concubine Phu Cu and Mac Thien Tu. Its solemn setting, antiques and stupa-tombs make it a distinctive spiritual and historical site.",
        "ps_ru": "Пагода Фузунг, официально Фукы-Амты, — старинный храм у подножия холма Биньшан в Хатьене, связанный с трогательной легендой о наложнице Фукы и Мак Тхьен Ты. Строгая атмосфера, старинные предметы и ступы-гробницы делают его своеобразным духовным и историческим местом.",
        "pl_vi": "Chùa Phù Dung, còn có tên chữ là Phù Cừ Am Tự, là một trong những ngôi chùa cổ nổi tiếng nhất Hà Tiên, nằm dưới chân núi Bình San, không xa lăng Mạc Cửu. Ngôi chùa gắn liền với một truyền thuyết tình yêu bi thương thời khai phá vùng đất: tương truyền đây là nơi nàng Phù Cừ — một người vợ thứ của Tổng trấn Mạc Thiên Tứ — lui về tu hành và sống những năm tháng cuối đời. Vì thế, ngoài giá trị tôn giáo, chùa còn mang màu sắc lịch sử và giai thoại được người dân truyền tụng. Khuôn viên chùa rợp bóng cây, có chính điện thờ Phật, điện thờ Ngọc Hoàng ở phía sau trên triền núi, cùng nhiều tượng, bia và mộ tháp cổ. Không gian tĩnh lặng, trầm mặc, hoà với tiếng chuông và hương trầm tạo cảm giác thanh thản. Từ khu vực chùa, du khách có thể ngắm cảnh núi non và một phần thị xã Hà Tiên. Nhờ vẻ đẹp cổ kính và câu chuyện lãng mạn đằng sau, chùa Phù Dung thường được du khách ghé thăm cùng cụm di tích Bình San khi đến Hà Tiên. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Phu Dung Pagoda, also formally called Phu Cu Am Tu, is one of Ha Tien's best-known old temples, at the foot of Binh San Hill not far from the Mac Cuu Tomb. The pagoda is bound up with a sorrowful love legend from the settling of the region: it is said to be where Phu Cu, a secondary wife of Governor Mac Thien Tu, withdrew to religious life and spent her final years. Beyond its religious value, then, the temple carries a historical and legendary aura passed down among local people. The grounds are shaded by trees, with a main hall dedicated to the Buddha, a shrine to the Jade Emperor behind it on the hillside, and many statues, stelae and old stupa-tombs. The quiet, contemplative atmosphere, blended with the sound of bells and incense, brings a sense of peace. From the temple area visitors can view the hills and part of Ha Tien town. Thanks to its ancient beauty and romantic backstory, Phu Dung Pagoda is usually visited together with the Binh San relic cluster. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Пагода Фузунг, официально также называемая Фукы-Амты, — один из самых известных старинных храмов Хатьена, у подножия холма Биньшан, недалеко от гробницы Мак Кыу. Храм связан с печальной любовной легендой времён освоения края: считается, что именно сюда удалилась для монашеской жизни Фукы, младшая жена наместника Мак Тхьен Ты, и провела здесь последние годы. Поэтому помимо религиозной ценности храм несёт исторический и легендарный ореол, передаваемый местными жителями. Территория затенена деревьями; есть главный зал, посвящённый Будде, святилище Нефритового Императора позади него на склоне, а также множество статуй, стел и старинных ступ-гробниц. Тихая, созерцательная атмосфера в сочетании со звоном колоколов и благовониями дарит ощущение покоя. С территории храма видны холмы и часть города Хатьен. Благодаря древней красоте и романтической истории пагоду Фузунг обычно посещают вместе с кластером памятников Биньшан. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Chùa cổ gắn truyền thuyết nàng Phù Cừ và Mạc Thiên Tứ", "Chính điện thờ Phật, điện Ngọc Hoàng trên triền núi", "Nằm trong cụm di tích Bình San, gần lăng Mạc Cửu"],
        "h_en": ["Old temple tied to the legend of Phu Cu and Mac Thien Tu", "Buddha main hall and a Jade Emperor shrine on the hillside", "Part of the Binh San relic cluster near Mac Cuu Tomb"],
        "h_ru": ["Старинный храм с легендой о Фукы и Мак Тхьен Ты", "Главный зал Будды и святилище Нефритового Императора на склоне", "Часть кластера Биньшан рядом с гробницей Мак Кыу"],
        "practical": {
            "hours_vi": "Khoảng 6:00–18:00 hằng ngày.",
            "ticket_vi": "Miễn phí; công đức tuỳ tâm.",
            "duration_vi": "Khoảng 45–60 phút.",
            "best_time_vi": "Sáng sớm hoặc chiều mát.",
            "tips_vi": "Mặc kín đáo; giữ yên tĩnh; kết hợp thăm lăng Mạc Cửu và núi Bình San.",
        },
    },
))

NEW.append(mk(
    "nui-da-dung", "Núi Đá Dựng",
    "Da Dung Mountain", "Гора Дадынг",
    10.4150, 104.4620, ["fortress", "other"],
    "Xã Mỹ Đức, Hà Tiên, tỉnh An Giang",
    ["cave", "nature", "history", "viewpoint", "trekking"],
    {
        "rating": {"value": 4.4, "count": 1800, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích ngọn núi đá vôi nhiều hang động kỳ thú, mát lạnh, gắn với chiến tích và truyền thuyết. Nhiều người khen leo núi thú vị, tầm nhìn ra biên giới đẹp; lưu ý đường trong hang trơn, nên mang đèn và giày tốt.",
        "ps_vi": "Núi Đá Dựng là núi đá vôi cao khoảng trăm mét ở Hà Tiên, nổi tiếng với hệ thống hang động đá vôi kỳ ảo nằm sát biên giới Campuchia. Bên trong là mê cung hang lớn nhỏ với thạch nhũ, gắn với truyền thuyết dân gian và di tích lịch sử kháng chiến.",
        "ps_en": "Da Dung Mountain is a limestone hill about a hundred metres high in Ha Tien, famous for a maze of magical limestone caves right by the Cambodian border. Inside is a labyrinth of large and small caverns with stalactites, tied to folk legend and to war-time historical relics.",
        "ps_ru": "Гора Дадынг — известняковый холм высотой около ста метров в Хатьене, знаменитый лабиринтом волшебных известняковых пещер у самой границы с Камбоджей. Внутри — сеть больших и малых гротов со сталактитами, связанная с народными легендами и памятниками военной истории.",
        "pl_vi": "Núi Đá Dựng là một ngọn núi đá vôi nằm ở xã Mỹ Đức, thành phố Hà Tiên, gần đường biên giới Việt Nam — Campuchia, cao khoảng trăm mét so với đồng bằng xung quanh. Điều làm nên tên tuổi của núi là hệ thống hang động đá vôi phong phú nằm bên trong: hàng chục hang lớn nhỏ thông nhau tạo thành một mê cung mát lạnh, với vô số thạch nhũ, măng đá đủ hình thù kỳ ảo, mỗi hang lại gắn với một cái tên và truyền thuyết dân gian như hang Bồng Lai, hang Cội Hàng Da, hang Thần Kim Quy. Trong hai cuộc kháng chiến, núi Đá Dựng còn là căn cứ và nơi ẩn náu, nên nơi đây được xếp hạng di tích lịch sử — thắng cảnh. Du khách theo các lối mòn và bậc thang len lỏi qua hang, leo lên đỉnh để phóng tầm mắt ra cánh đồng, biển và vùng biên giới. Không khí trong hang mát mẻ quanh năm, ánh sáng lọt qua các khe đá tạo hiệu ứng huyền ảo. Với sự kết hợp giữa cảnh quan thiên nhiên độc đáo, giá trị lịch sử và những câu chuyện truyền miệng, Núi Đá Dựng là một trong 'Hà Tiên thập cảnh' được nhiều du khách tìm đến. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Da Dung Mountain rises in My Duc commune of Ha Tien, near the Vietnam–Cambodia border, about a hundred metres above the surrounding plain. What made its name is the rich system of limestone caves within: dozens of interconnected caverns form a cool labyrinth full of stalactites and stone formations in fantastic shapes, each cave carrying its own name and folk legend, such as Bong Lai Cave, Coi Hang Da Cave and the Golden Turtle God Cave. During the two resistance wars the mountain also served as a base and hiding place, so it is ranked as a historical and scenic relic. Visitors follow trails and steps threading through the caves and climb to the summit for views over the fields, the sea and the borderland. The air inside stays cool year-round, and light filtering through cracks in the rock creates an eerie glow. With its unique natural scenery, historical value and oral legends, Da Dung Mountain is one of the celebrated 'Ten Scenes of Ha Tien' that many travellers seek out. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Гора Дадынг возвышается в общине Мидык города Хатьен, у границы Вьетнама и Камбоджи, примерно на сто метров над окружающей равниной. Известность ей принесла богатая система известняковых пещер внутри: десятки соединённых между собой гротов образуют прохладный лабиринт, полный сталактитов и каменных образований причудливой формы; каждая пещера носит своё имя и связана с народной легендой — пещера Бонглай, пещера Кой-Ханг-За, пещера Бога Золотой Черепахи. В годы двух войн сопротивления гора служила базой и укрытием, поэтому она отнесена к историко-живописным памятникам. Посетители идут по тропам и ступеням сквозь пещеры и поднимаются на вершину, откуда открывается вид на поля, море и приграничье. Воздух внутри круглый год прохладный, а свет, проникающий сквозь трещины в скале, создаёт таинственное сияние. Благодаря уникальной природе, исторической ценности и устным легендам гора Дадынг входит в число прославленных «Десяти видов Хатьена», которые ищут многие путешественники. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Núi đá vôi với mê cung hang động và thạch nhũ kỳ ảo", "Mỗi hang gắn một truyền thuyết dân gian riêng", "Di tích lịch sử kháng chiến, một trong 'Hà Tiên thập cảnh'"],
        "h_en": ["Limestone mountain with a maze of caves and stalactites", "Each cave carries its own folk legend", "War-time historical relic, one of the 'Ten Scenes of Ha Tien'"],
        "h_ru": ["Известняковая гора с лабиринтом пещер и сталактитами", "У каждой пещеры своя народная легенда", "Памятник военной истории, один из «Десяти видов Хатьена»"],
        "practical": {
            "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
            "ticket_vi": "Vé vào tham khảo khoảng 20.000–40.000 VND (có thể thay đổi).",
            "duration_vi": "Khoảng 1,5–2 giờ.",
            "best_time_vi": "Sáng hoặc chiều mát; tránh mưa lớn khi hang trơn.",
            "tips_vi": "Mang đèn pin, giày bám tốt; cẩn thận đá trơn trong hang; đi cùng người dẫn nếu chưa quen.",
        },
    },
))

NEW.append(mk(
    "dam-dong-ho", "Đầm Đông Hồ",
    "Dong Ho Lagoon", "Лагуна Донгхо",
    10.3950, 104.4880, ["park_garden", "other"],
    "Phường Đông Hồ, Hà Tiên, tỉnh An Giang",
    ["nature", "lagoon", "viewpoint", "sunset", "mangrove"],
    {
        "rating": {"value": 4.3, "count": 900, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích đầm nước lợ mênh mông ôm lấy thị xã Hà Tiên, cảnh hoàng hôn và trăng nước thơ mộng đi vào thơ ca. Nhiều người khen yên bình, chụp ảnh đẹp; thường ngắm từ cầu hoặc bờ đầm.",
        "ps_vi": "Đầm Đông Hồ là đầm nước lợ rộng lớn nằm ngay cạnh thành phố Hà Tiên, nơi sông Giang Thành đổ ra biển. Được ngợi ca trong 'Hà Tiên thập vịnh' xưa với cảnh 'Đông Hồ ấn nguyệt' (trăng in mặt hồ), đây là điểm ngắm hoàng hôn, cảnh sông nước thơ mộng.",
        "ps_en": "Dong Ho Lagoon is a large brackish-water lagoon right beside Ha Tien city, where the Giang Thanh River meets the sea. Praised in the old 'Ten Songs of Ha Tien' for the scene of the moon reflected on its surface, it is a poetic spot for sunsets and river-and-sea views.",
        "ps_ru": "Лагуна Донгхо — обширная солоноватая лагуна прямо у города Хатьен, где река Зянгтхань впадает в море. Воспетая в старинных «Десяти песнях Хатьена» за вид отражённой в её глади луны, она стала поэтичным местом для закатов и водных пейзажей.",
        "pl_vi": "Đầm Đông Hồ là một đầm nước lợ rộng lớn nằm ôm lấy phía đông thành phố Hà Tiên, được tạo thành nơi sông Giang Thành và các nhánh nước hoà vào biển trước khi ra vịnh Thái Lan. Mặt đầm phẳng lặng, bao quanh là núi, rừng ngập mặn và làng chài, tạo nên một bức tranh sông nước hữu tình đặc trưng của vùng biên viễn. Từ xa xưa, cảnh đẹp nơi đây đã đi vào thi ca: trong 'Hà Tiên thập vịnh' do Mạc Thiên Tứ và Chiêu Anh Các xướng họa, hình ảnh 'Đông Hồ ấn nguyệt' — vầng trăng in bóng trên mặt đầm — được xem là một trong mười cảnh đẹp nổi tiếng nhất của Hà Tiên. Ngày nay, du khách có thể ngắm đầm từ trên các cây cầu bắc qua, từ bờ đê hoặc đi thuyền dạo quanh để cảm nhận không gian khoáng đạt, đặc biệt lúc bình minh và hoàng hôn khi mặt nước nhuộm màu rực rỡ. Đầm cũng là nơi mưu sinh của ngư dân với nghề chài lưới, nuôi trồng thuỷ sản. Vẻ đẹp yên bình cùng chiều sâu văn hoá — lịch sử khiến Đông Hồ trở thành điểm dừng chân đáng nhớ khi khám phá Hà Tiên. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Dong Ho Lagoon is a large brackish lagoon wrapping the eastern side of Ha Tien city, formed where the Giang Thanh River and its channels blend into the sea before reaching the Gulf of Thailand. Its calm surface is ringed by hills, mangroves and fishing hamlets, making a graceful water landscape typical of the borderland. Long ago its beauty entered poetry: in the 'Ten Songs of Ha Tien' composed by Mac Thien Tu and the Chieu Anh Cac literary circle, the image of 'the moon stamped on Dong Ho' — the moon reflected on the lagoon — was counted among the ten most famous scenes of Ha Tien. Today visitors can admire the lagoon from the bridges crossing it, from the embankment or by boat, taking in its open expanse, especially at dawn and dusk when the water glows with colour. The lagoon is also a livelihood for fishermen who net fish and farm aquaculture here. Its peaceful beauty and cultural-historical depth make Dong Ho a memorable stop while exploring Ha Tien. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Лагуна Донгхо — большая солоноватая лагуна, охватывающая восточную часть города Хатьен; она образуется там, где река Зянгтхань и её протоки сливаются с морем перед выходом в Сиамский залив. Спокойную гладь окружают холмы, мангры и рыбацкие деревушки, создавая изящный водный пейзаж, характерный для пограничного края. Издавна её красота вошла в поэзию: в «Десяти песнях Хатьена», сложенных Мак Тхьен Ты и литературным кружком Тьеу-Ань-Как, образ «луны, отпечатанной на Донгхо» — отражённой в лагуне луны — вошёл в число десяти самых знаменитых видов Хатьена. Сегодня лагуной любуются с перекинутых через неё мостов, с дамбы или с лодки, наслаждаясь простором, особенно на рассвете и закате, когда вода светится красками. Лагуна также кормит рыбаков, которые ловят рыбу и разводят морепродукты. Умиротворяющая красота и культурно-историческая глубина делают Донгхо запоминающейся остановкой при знакомстве с Хатьеном. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Đầm nước lợ rộng lớn ôm lấy thành phố Hà Tiên", "'Đông Hồ ấn nguyệt' — một trong 'Hà Tiên thập vịnh'", "Cảnh hoàng hôn, sông nước thơ mộng, làng chài ven đầm"],
        "h_en": ["Large brackish lagoon wrapping Ha Tien city", "'Moon on Dong Ho' — one of the 'Ten Songs of Ha Tien'", "Poetic sunsets, waterscapes and lagoon-side fishing villages"],
        "h_ru": ["Большая солоноватая лагуна вокруг города Хатьен", "«Луна на Донгхо» — один из «Десяти видов Хатьена»", "Поэтичные закаты, водные пейзажи и рыбацкие деревни"],
        "practical": {
            "hours_vi": "Ngắm cảnh cả ngày; đẹp nhất bình minh và hoàng hôn.",
            "ticket_vi": "Miễn phí ngắm cảnh; đi thuyền trả phí theo thoả thuận.",
            "duration_vi": "Khoảng 1 giờ.",
            "best_time_vi": "Bình minh, hoàng hôn hoặc đêm trăng.",
            "tips_vi": "Ngắm từ cầu qua đầm; mang máy ảnh; hỏi giá trước khi thuê thuyền.",
        },
    },
))

NEW.append(mk(
    "quan-dao-ba-lua", "Quần đảo Bà Lụa",
    "Ba Lua Archipelago", "Архипелаг Балуа",
    10.1450, 104.3600, ["other"],
    "Xã Sơn Hải, huyện Kiên Lương, tỉnh An Giang",
    ["island", "sea", "nature", "kayak", "quiet"],
    {
        "rating": {"value": 4.4, "count": 800, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách gọi đây là 'Hạ Long của phương Nam' với hàng chục đảo đá nhỏ, nước cạn có thể lội giữa các đảo khi triều xuống. Nhiều người khen hoang sơ, yên tĩnh; lưu ý dịch vụ còn ít, nên đi theo tour hoặc thuê thuyền địa phương.",
        "ps_vi": "Quần đảo Bà Lụa thuộc vùng biển Kiên Lương, gồm hàng chục hòn đảo đá lớn nhỏ nằm rải rác, được ví như 'Hạ Long của phương Nam'. Nước biển nông, khi triều xuống du khách có thể lội bộ giữa vài đảo, cùng bãi biển hoang sơ và làng chài yên bình.",
        "ps_en": "Ba Lua Archipelago, in the sea off Kien Luong, is a scatter of dozens of rocky islands often called the 'Ha Long of the South.' The water is shallow, and at low tide visitors can wade between some islands, amid unspoiled beaches and quiet fishing hamlets.",
        "ps_ru": "Архипелаг Балуа в море у Кьенлыонга — россыпь из десятков скалистых островов, которую часто называют «Халонгом Юга». Вода мелкая, и во время отлива между некоторыми островами можно перейти вброд, среди нетронутых пляжей и тихих рыбацких деревень.",
        "pl_vi": "Quần đảo Bà Lụa nằm trong vùng biển thuộc huyện Kiên Lương, gồm khoảng hơn bốn mươi hòn đảo đá lớn nhỏ rải rác trên mặt biển xanh, trong đó có hơn chục đảo có người sinh sống. Với cảnh sắc núi đá nhấp nhô trên nền nước biển, nơi đây được nhiều người ưu ái gọi là 'Hạ Long của phương Nam'. Điểm đặc biệt của Bà Lụa là vùng biển khá nông; vào lúc thuỷ triều xuống, du khách có thể lội bộ trên bãi cát ngầm để di chuyển giữa một số đảo gần nhau — trải nghiệm hiếm có. Các đảo như Hòn Heo, Hòn Ngang, Hòn Đước còn giữ vẻ hoang sơ với bãi cát, rừng cây và những xóm chài nhỏ, nơi du khách có thể nghỉ lại, thưởng thức hải sản tươi và ngắm hoàng hôn trên biển. Hoạt động ưa thích ở đây là đi thuyền dạo quanh các đảo, câu cá, tắm biển và khám phá đời sống ngư dân. Do du lịch còn ở dạng sơ khai, dịch vụ chưa nhiều nên Bà Lụa phù hợp với những ai thích sự yên tĩnh, nguyên sơ và muốn tránh xa các điểm đông đúc. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Ba Lua Archipelago lies in the sea of Kien Luong district and comprises more than forty large and small rocky islands scattered across blue water, of which over a dozen are inhabited. With craggy hills rising from the sea, it is fondly called the 'Ha Long of the South.' What sets Ba Lua apart is its fairly shallow water: at low tide visitors can walk over submerged sandbars to move between some nearby islands — a rare experience. Islands such as Hon Heo, Hon Ngang and Hon Duoc keep an unspoiled feel, with sandy beaches, woodland and small fishing hamlets where travellers can stay overnight, enjoy fresh seafood and watch the sunset over the sea. Favourite activities are boating among the islands, fishing, swimming and observing fishermen's life. Because tourism is still in its infancy and services are limited, Ba Lua suits those who love quiet, unspoiled places and want to escape the crowds. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Архипелаг Балуа находится в море района Кьенлыонг и состоит более чем из сорока больших и малых скалистых островов, разбросанных по синей воде; более десяти из них обитаемы. Со скалистыми холмами, поднимающимися из моря, его ласково называют «Халонгом Юга». Особенность Балуа — довольно мелкая вода: во время отлива можно пройти по подводным песчаным косам между некоторыми близкими островами, что является редким впечатлением. Острова Хонхео, Хонанг и Хондыок сохраняют первозданность — песчаные пляжи, лес и небольшие рыбацкие деревушки, где путешественники могут остаться на ночь, попробовать свежие морепродукты и полюбоваться закатом. Любимые занятия — прогулки на лодке между островами, рыбалка, купание и знакомство с жизнью рыбаков. Поскольку туризм здесь только зарождается, а услуг немного, Балуа подходит тем, кто ценит тишину, нетронутость и хочет уйти от толп. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Hơn 40 đảo đá — 'Hạ Long của phương Nam'", "Nước cạn, lội bộ giữa vài đảo khi triều xuống", "Đảo hoang sơ, hải sản tươi, hoàng hôn trên biển"],
        "h_en": ["Over 40 rocky islands — the 'Ha Long of the South'", "Shallow water; wade between some islands at low tide", "Unspoiled islands, fresh seafood, sea sunsets"],
        "h_ru": ["Более 40 скалистых островов — «Халонг Юга»", "Мелкая вода; во время отлива можно перейти между островами", "Первозданные острова, свежие морепродукты, морские закаты"],
        "practical": {
            "hours_vi": "Đi trong ngày hoặc nghỉ đêm; phụ thuộc lịch thuyền.",
            "ticket_vi": "Chi phí thuê thuyền/tour theo thoả thuận; nghỉ homestay đảo.",
            "duration_vi": "1 ngày hoặc 2 ngày 1 đêm.",
            "best_time_vi": "Mùa khô tháng 12–4 biển êm; canh lịch thuỷ triều.",
            "tips_vi": "Đi theo tour/thuê thuyền địa phương; mang đủ nước và vật dụng; kiểm tra thời tiết trước khi ra đảo.",
        },
    },
))

NEW.append(mk(
    "quan-dao-hai-tac", "Quần đảo Hải Tặc (Đảo Hải Tặc)",
    "Hai Tac (Pirate) Archipelago", "Пиратский архипелаг Хайтак",
    10.4830, 104.5330, ["other"],
    "Xã Tiên Hải, Hà Tiên, tỉnh An Giang",
    ["island", "sea", "nature", "history", "quiet"],
    {
        "rating": {"value": 4.3, "count": 700, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách tò mò với hòn đảo mang cái tên 'Hải Tặc' cùng bia chủ quyền, bãi biển hoang sơ và làng chài mộc mạc. Nhiều người khen yên tĩnh, biển sạch; lưu ý tàu ra đảo theo giờ, dịch vụ còn giản dị.",
        "ps_vi": "Quần đảo Hải Tặc gồm khoảng mười sáu hòn đảo ngoài khơi Hà Tiên, thuộc xã đảo Tiên Hải. Cái tên gắn với những giai thoại về cướp biển thuở xưa; nay đảo nổi tiếng với bãi biển hoang sơ, bia chủ quyền và làng chài yên bình, hấp dẫn khách thích khám phá.",
        "ps_en": "Hai Tac (Pirate) Archipelago is a group of about sixteen islands off Ha Tien, forming Tien Hai island commune. The name recalls old tales of pirates; today the islands are known for unspoiled beaches, a sovereignty stele and a peaceful fishing village that appeals to explorers.",
        "ps_ru": "Пиратский архипелаг Хайтак — группа из примерно шестнадцати островов у Хатьена, образующая островную общину Тьенхай. Название хранит старые предания о пиратах; сегодня острова известны нетронутыми пляжами, стелой суверенитета и тихой рыбацкой деревней, что привлекает любителей приключений.",
        "pl_vi": "Quần đảo Hải Tặc là một cụm gồm khoảng mười sáu hòn đảo lớn nhỏ nằm ngoài khơi vùng biển Hà Tiên, hợp thành xã đảo Tiên Hải. Cái tên nghe đầy phiêu lưu bắt nguồn từ những giai thoại kể rằng vùng biển này từng là nơi ẩn náu, hoạt động của cướp biển trong các thế kỷ trước, khi đây là tuyến hàng hải sầm uất giữa vịnh Thái Lan. Hòn đảo lớn nhất và có dân cư đông nhất là Hòn Đốc (Hòn Tre Lớn), nơi đặt tấm bia chủ quyền khẳng định quần đảo Hải Tặc thuộc chủ quyền Việt Nam — một điểm check-in mang ý nghĩa thiêng liêng. Đảo còn giữ nét hoang sơ với những bãi biển cát trắng, nước trong, rừng cây xanh và cuộc sống ngư dân mộc mạc. Du khách đến đây thường tắm biển, đi bộ vòng quanh đảo, câu cá, lặn ngắm san hô và nghe người dân kể chuyện về cái tên độc đáo của đảo. Vì dịch vụ còn đơn sơ và tàu ra đảo theo lịch cố định, Hải Tặc phù hợp với những ai ưa trải nghiệm khám phá, tìm sự yên tĩnh và một chút phiêu lưu. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Hai Tac (Pirate) Archipelago is a cluster of about sixteen large and small islands off the sea of Ha Tien, forming Tien Hai island commune. The adventurous name comes from tales that these waters were once a hideout and haunt of pirates in past centuries, when this was a busy shipping route across the Gulf of Thailand. The largest and most populated island is Hon Doc (Hon Tre Lon), where a sovereignty stele affirms that the Pirate Archipelago belongs to Vietnam — a check-in point of solemn meaning. The islands keep a wild feel, with white-sand beaches, clear water, green woods and a simple fishing life. Visitors typically swim, walk around the island, fish, snorkel over coral and listen to locals tell the story behind the island's unusual name. Because services are basic and boats run on a fixed schedule, Hai Tac suits those who enjoy exploration, seek quiet and want a touch of adventure. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Пиратский архипелаг Хайтак — группа из примерно шестнадцати больших и малых островов в море у Хатьена, образующая островную общину Тьенхай. Авантюрное название происходит от преданий о том, что эти воды когда-то были укрытием и пристанищем пиратов в прошлые века, когда здесь пролегал оживлённый морской путь через Сиамский залив. Крупнейший и самый населённый остров — Хондок (Хон-Че-Лон), где установлена стела суверенитета, подтверждающая принадлежность Пиратского архипелага Вьетнаму, — место для фото с торжественным смыслом. Острова сохраняют дикую атмосферу: белопесчаные пляжи, прозрачная вода, зелёные леса и простая рыбацкая жизнь. Гости обычно купаются, обходят остров, рыбачат, ныряют к кораллам и слушают рассказы местных о необычном названии острова. Поскольку услуги здесь скромные, а катера ходят по фиксированному расписанию, Хайтак подходит тем, кто любит исследования, ищет тишину и немного приключений. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Cụm 16 đảo với cái tên gắn giai thoại cướp biển", "Bia chủ quyền trên Hòn Đốc — điểm check-in ý nghĩa", "Bãi biển hoang sơ, nước trong, làng chài mộc mạc"],
        "h_en": ["Cluster of 16 islands with a pirate-legend name", "Sovereignty stele on Hon Doc — a meaningful check-in", "Unspoiled beaches, clear water, simple fishing village"],
        "h_ru": ["Группа из 16 островов с «пиратским» названием", "Стела суверенитета на Хондоке — значимое место для фото", "Нетронутые пляжи, прозрачная вода, простая рыбацкая деревня"],
        "practical": {
            "hours_vi": "Tàu ra đảo theo lịch trong ngày; có thể nghỉ đêm.",
            "ticket_vi": "Vé tàu và homestay theo thoả thuận.",
            "duration_vi": "1 ngày hoặc 2 ngày 1 đêm.",
            "best_time_vi": "Mùa khô tháng 12–4 biển êm.",
            "tips_vi": "Kiểm tra lịch tàu và thời tiết; mang tiền mặt; chuẩn bị đồ dùng vì dịch vụ còn ít.",
        },
    },
))

NEW.append(mk(
    "bao-tang-kien-giang", "Bảo tàng Kiên Giang",
    "Kien Giang Museum", "Музей Кьензянг",
    10.0125, 105.0870, ["museum"],
    "27 Nguyễn Văn Trỗi, phường Rạch Giá, tỉnh An Giang",
    ["museum", "history", "heritage", "indoor", "architecture"],
    {
        "rating": {"value": 4.3, "count": 700, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách khen toà nhà Pháp cổ đẹp, trưng bày phong phú về lịch sử, văn hoá Kiên Giang xưa, có cả hiện vật văn hoá Óc Eo. Nhiều người thấy đáng ghé, mát mẻ; lưu ý kiểm tra giờ mở cửa vì có thể nghỉ trưa.",
        "ps_vi": "Bảo tàng Kiên Giang đặt trong một dinh thự kiểu Pháp cổ kính giữa thành phố Rạch Giá, trưng bày lịch sử, văn hoá và thiên nhiên của vùng đất Kiên Giang cũ. Nơi đây lưu giữ nhiều hiện vật quý, trong đó có cổ vật văn hoá Óc Eo và tư liệu về anh hùng Nguyễn Trung Trực.",
        "ps_en": "Kien Giang Museum occupies a stately old French villa in central Rach Gia, presenting the history, culture and nature of the former Kien Giang region. It holds many valuable artefacts, including relics of the Oc Eo culture and materials on the hero Nguyen Trung Truc.",
        "ps_ru": "Музей Кьензянг располагается в старинной французской вилле в центре Ратьзя и рассказывает об истории, культуре и природе бывшего края Кьензянг. В нём хранится множество ценных экспонатов, включая артефакты культуры Окео и материалы о герое Нгуен Чунг Чыке.",
        "pl_vi": "Bảo tàng Kiên Giang là bảo tàng tổng hợp của vùng đất Kiên Giang (cũ), toạ lạc trong một toà biệt thự kiểu Pháp xây từ đầu thế kỷ 20 tại trung tâm thành phố Rạch Giá. Bản thân toà nhà với kiến trúc thuộc địa, mái ngói, hành lang rộng và những hàng cột cổ đã là một điểm tham quan hấp dẫn, được nhiều du khách chụp ảnh. Bên trong, bảo tàng trưng bày theo nhiều chuyên đề giúp người xem hình dung quá trình hình thành và phát triển của vùng đất: từ điều kiện tự nhiên, tài nguyên biển đảo, đến lịch sử khai phá, đời sống các dân tộc Kinh, Hoa, Khmer cùng chung sống. Đặc biệt, nơi đây lưu giữ nhiều hiện vật khảo cổ thuộc nền văn hoá Óc Eo nổi tiếng từng phát triển rực rỡ ở đồng bằng sông Cửu Long, cùng các tư liệu, kỷ vật về phong trào yêu nước và người anh hùng dân tộc Nguyễn Trung Trực. Với không gian mát mẻ, hiện vật phong phú và giá trị kiến trúc, Bảo tàng Kiên Giang là điểm dừng chân lý tưởng để hiểu thêm về lịch sử — văn hoá miền biển Tây Nam trước khi khám phá các điểm khác. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Kien Giang Museum is the general museum of the former Kien Giang region, housed in an early-20th-century French villa in central Rach Gia. The building itself — colonial in style, with tiled roofs, wide verandas and rows of old columns — is a draw in its own right and a favourite photo subject. Inside, the museum is arranged by theme to help visitors picture how the region took shape and grew: from its natural setting and marine resources to the history of settlement and the shared life of the Kinh, Chinese and Khmer peoples. It notably holds many archaeological artefacts of the famous Oc Eo culture that once flourished in the Mekong Delta, along with documents and mementoes of the patriotic movement and the national hero Nguyen Trung Truc. With its cool interior, rich collection and architectural value, Kien Giang Museum is an ideal stop to understand the history and culture of the south-western coast before exploring other sites. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Музей Кьензянг — краеведческий музей бывшего края Кьензянг, размещённый во французской вилле начала XX века в центре Ратьзя. Само здание в колониальном стиле — с черепичными крышами, широкими верандами и рядами старинных колонн — привлекает внимание и часто становится объектом фотосъёмки. Внутри экспозиция построена по темам, помогая представить, как складывался и развивался край: от природных условий и морских ресурсов до истории освоения и совместной жизни народов кинь, хоа и кхмеров. Особо ценны археологические артефакты знаменитой культуры Окео, некогда процветавшей в дельте Меконга, а также документы и реликвии патриотического движения и национального героя Нгуен Чунг Чыка. Благодаря прохладным залам, богатой коллекции и архитектурной ценности музей Кьензянг — идеальная остановка, чтобы понять историю и культуру юго-западного побережья перед знакомством с другими местами. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Đặt trong biệt thự Pháp cổ đầu thế kỷ 20 ở Rạch Giá", "Lưu giữ cổ vật văn hoá Óc Eo và tư liệu Nguyễn Trung Trực", "Trưng bày lịch sử, văn hoá các dân tộc Kinh, Hoa, Khmer"],
        "h_en": ["Set in an early-1900s French villa in Rach Gia", "Holds Oc Eo culture relics and Nguyen Trung Truc materials", "Displays the history and culture of Kinh, Chinese and Khmer peoples"],
        "h_ru": ["Во французской вилле начала 1900-х годов в Ратьзя", "Хранит артефакты Окео и материалы о Нгуен Чунг Чыке", "Экспозиция об истории и культуре кинь, хоа и кхмеров"],
        "practical": {
            "hours_vi": "Thường 7:30–11:00 và 13:30–17:00; có thể nghỉ một số ngày.",
            "ticket_vi": "Miễn phí hoặc phí thấp; nên kiểm tra tại chỗ.",
            "duration_vi": "Khoảng 1 giờ.",
            "best_time_vi": "Buổi sáng; tránh giờ nghỉ trưa.",
            "tips_vi": "Kiểm tra giờ mở cửa trước khi đến; kết hợp thăm đình Nguyễn Trung Trực gần đó.",
        },
    },
))

NEW.append(mk(
    "chua-lang-cat", "Chùa Láng Cát (Ratana Ranghsây)",
    "Lang Cat Pagoda (Ratana Ranghsay)", "Пагода Лангкат (Ратана Рангсай)",
    10.0110, 105.0830, ["church", "other"],
    "Phường Rạch Giá, tỉnh An Giang",
    ["temple", "khmer", "heritage", "architecture", "spiritual"],
    {
        "rating": {"value": 4.5, "count": 900, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách trầm trồ với ngôi chùa Khmer cổ rực rỡ, chính điện chạm khắc tinh xảo, mái nhọn nhiều tầng và tượng Phật uy nghi. Nhiều người khen đẹp, yên tĩnh; lưu ý ăn mặc lịch sự khi vào chính điện.",
        "ps_vi": "Chùa Láng Cát, tên Khmer là Ratana Ranghsây, là ngôi chùa Khmer Nam tông cổ và lớn bậc nhất ở Rạch Giá. Kiến trúc rực rỡ với mái tháp nhọn nhiều tầng, phù điêu chằn, tiên nữ và tượng Phật, là trung tâm sinh hoạt tôn giáo — văn hoá của cộng đồng Khmer.",
        "ps_en": "Lang Cat Pagoda, Khmer name Ratana Ranghsay, is one of the oldest and largest Theravada Khmer temples in Rach Gia. Its dazzling architecture — tiered pointed roofs, reliefs of guardian giants and apsaras, and Buddha statues — makes it a religious and cultural centre for the Khmer community.",
        "ps_ru": "Пагода Лангкат, кхмерское название Ратана Рангсай, — один из старейших и крупнейших тхеравадинских кхмерских храмов в Ратьзя. Яркая архитектура — многоярусные остроконечные крыши, рельефы великанов-стражей и апсар, статуи Будды — делает её религиозным и культурным центром кхмерской общины.",
        "pl_vi": "Chùa Láng Cát, tên Khmer là Ratana Ranghsây, là một trong những ngôi chùa Khmer Nam tông lâu đời và tiêu biểu nhất ở thành phố Rạch Giá, tương truyền có lịch sử hàng trăm năm. Chùa là nơi tu học của các nhà sư và là trung tâm sinh hoạt tín ngưỡng, văn hoá của cộng đồng người Khmer trong vùng. Ngay từ cổng, du khách đã ấn tượng với lối kiến trúc đặc trưng: mái chính điện xếp nhiều tầng vươn cao, các đầu đao cong vút, cùng hoa văn, phù điêu dày đặc mô tả tượng chằn (Yeak), tiên nữ Kâyno, rắn thần Naga và các tích Phật giáo được sơn son thếp vàng rực rỡ. Bên trong chính điện là tượng Phật Thích Ca uy nghi cùng những bức bích hoạ kể chuyện cuộc đời Đức Phật. Không gian chùa rợp bóng cây thốt nốt và cây sao, mang lại cảm giác thanh tịnh, mát mẻ. Vào các dịp lễ lớn của người Khmer như Chôl Chnăm Thmây, Sen Đôn Ta hay Oóc Om Bóc, chùa trở nên nhộn nhịp với nghi lễ và sinh hoạt cộng đồng. Đây là điểm đến hấp dẫn để tìm hiểu văn hoá Khmer đặc sắc của miền Tây Nam Bộ. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Lang Cat Pagoda, Khmer name Ratana Ranghsay, is one of the oldest and most representative Theravada Khmer temples in the city of Rach Gia, said to date back hundreds of years. It is a place of study for monks and a centre of religious and cultural life for the local Khmer community. From the gate, visitors are struck by its distinctive architecture: the main hall's roof rises in many tiers with sharply curved eaves, dense patterns and reliefs depicting guardian giants (Yeak), Kayno celestial maidens, the Naga serpent and Buddhist tales, all gilded and richly painted. Inside the hall stands a majestic statue of Shakyamuni Buddha, surrounded by murals recounting the Buddha's life. The grounds are shaded by sugar-palm and dipterocarp trees, giving a cool, serene feel. During major Khmer festivals such as Chol Chnam Thmay, Sen Dolta and Ok Om Bok, the temple comes alive with rituals and community activities. It is a rewarding place to learn about the distinctive Khmer culture of the south-western delta. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Пагода Лангкат, кхмерское название Ратана Рангсай, — один из старейших и наиболее характерных тхеравадинских кхмерских храмов в городе Ратьзя; считается, что ему несколько сотен лет. Это место обучения монахов и центр религиозной и культурной жизни местной кхмерской общины. Уже от ворот посетителей поражает самобытная архитектура: крыша главного зала поднимается многими ярусами с резко изогнутыми карнизами, покрыта плотными узорами и рельефами с изображением великанов-стражей (Йеак), небесных дев Кайно, змея Наги и буддийских сюжетов — всё позолочено и богато расписано. Внутри зала стоит величественная статуя Будды Шакьямуни в окружении фресок о жизни Будды. Территорию затеняют сахарные пальмы и деревья сао, создавая прохладу и умиротворение. Во время крупных кхмерских праздников — Чол Чнам Тмей, Сен Донта и Ок Ом Бок — храм оживает от обрядов и общинных действ. Это благодатное место, чтобы узнать самобытную кхмерскую культуру юго-западной дельты. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Chùa Khmer Nam tông cổ và lớn bậc nhất Rạch Giá", "Mái tháp nhiều tầng, phù điêu chằn, tiên nữ, rắn Naga", "Trung tâm lễ hội Khmer: Chôl Chnăm Thmây, Sen Đôn Ta, Oóc Om Bóc"],
        "h_en": ["Oldest and largest Theravada Khmer temple in Rach Gia", "Tiered roofs, reliefs of giants, apsaras and the Naga", "Hub of Khmer festivals: Chol Chnam Thmay, Sen Dolta, Ok Om Bok"],
        "h_ru": ["Старейший и крупнейший кхмерский храм тхеравады в Ратьзя", "Многоярусные крыши, рельефы великанов, апсар и Наги", "Центр кхмерских праздников: Чол Чнам Тмей, Сен Донта, Ок Ом Бок"],
        "practical": {
            "hours_vi": "Khoảng 6:00–18:00 hằng ngày.",
            "ticket_vi": "Miễn phí; công đức tuỳ tâm.",
            "duration_vi": "Khoảng 45–60 phút.",
            "best_time_vi": "Buổi sáng hoặc dịp lễ hội Khmer.",
            "tips_vi": "Mặc kín đáo, bỏ dép khi vào chính điện; giữ yên tĩnh; xin phép trước khi chụp ảnh nhà sư.",
        },
    },
))

NEW.append(mk(
    "lang-be-chau-doc", "Làng bè Châu Đốc (Làng bè sắc màu ngã ba sông)",
    "Chau Doc Floating Fish-Raft Village", "Плавучая деревня рыбных садков Тяудок",
    10.7050, 105.1080, ["other"],
    "Ngã ba sông Châu Đốc, phường Châu Đốc, tỉnh An Giang",
    ["village", "river", "colorful", "photo", "food"],
    {
        "rating": {"value": 4.4, "count": 1200, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích thú với những dãy nhà bè nuôi cá sơn nhiều màu rực rỡ nổi trên sông, đặc biệt đẹp lúc bình minh và hoàng hôn. Nhiều người khen 'sống ảo' đẹp, đi thuyền thú vị; lưu ý nên đi sáng sớm cho mát và ít nắng.",
        "ps_vi": "Làng bè Châu Đốc là cụm nhà bè nuôi cá đặc trưng của vùng đầu nguồn sông Mê Kông, nay được sơn nhiều màu rực rỡ thành 'làng bè sắc màu' nổi trên ngã ba sông Châu Đốc. Đi thuyền len giữa những dãy bè, du khách tìm hiểu nghề nuôi cá và ngắm cảnh sông nước độc đáo.",
        "ps_en": "Chau Doc Floating Fish-Raft Village is a cluster of fish-farming houseboats typical of the upper Mekong, now painted in bright colours as a 'colourful raft village' floating at the Chau Doc river junction. Cruising among the rafts, visitors learn about fish farming and enjoy a unique river scene.",
        "ps_ru": "Плавучая деревня рыбных садков Тяудок — скопление рыбоводных плавучих домов, характерных для верхнего Меконга; теперь они окрашены в яркие цвета как «красочная деревня садков» на слиянии рек у Тяудока. Проплывая между садками, гости узнают о рыбоводстве и любуются самобытным речным пейзажем.",
        "pl_vi": "Làng bè Châu Đốc là một trong những hình ảnh đặc trưng nhất của vùng đầu nguồn sông Cửu Long, nơi hàng trăm ngôi nhà bè nổi trên mặt nước, bên dưới mỗi nhà là lồng nuôi các loài cá như cá basa, cá tra, cá he. Trong những năm gần đây, chính quyền và người dân đã sơn màu cho các nhà bè theo bảng màu rực rỡ — đỏ, cam, vàng, lục, lam, tím — biến cả xóm bè thành một 'làng bè sắc màu' soi bóng xuống dòng nước, tạo nên khung cảnh vô cùng bắt mắt, đặc biệt khi nhìn từ trên cao hoặc lúc bình minh, hoàng hôn. Du khách thường đi thuyền hoặc tắc ráng dọc ngã ba sông Châu Đốc để ngắm toàn cảnh, ghé thăm một số nhà bè để tìm hiểu nghề nuôi cá lồng, xem cách cho cá ăn và trò chuyện với người dân sông nước. Trải nghiệm này thường được kết hợp trong tuyến tham quan Châu Đốc — làng Chăm Châu Giang — rừng tràm để cảm nhận trọn vẹn đời sống miền Tây. Vừa mang giá trị kinh tế, vừa trở thành điểm du lịch 'sống ảo' nổi tiếng, làng bè sắc màu là nét chấm phá đặc biệt của An Giang. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Chau Doc Floating Fish-Raft Village is one of the most emblematic sights of the upper Mekong Delta, where hundreds of houseboats float on the water, each with fish cages beneath it raising species such as basa, tra and he carp. In recent years authorities and residents have painted the rafts in a vivid palette — red, orange, yellow, green, blue and purple — turning the whole hamlet into a 'colourful raft village' mirrored in the water, an eye-catching scene especially from above or at dawn and dusk. Visitors usually take a boat or long-tail skiff along the Chau Doc river junction to admire the panorama, stop at some rafts to learn about cage fish farming, watch feeding and chat with the river folk. The experience is often combined with a Chau Doc – Chau Giang Cham village – melaleuca forest route for a fuller taste of delta life. Both an economic livelihood and a famous photo-worthy attraction, the colourful raft village is a special highlight of An Giang. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Плавучая деревня рыбных садков Тяудок — один из самых характерных видов верхней дельты Меконга, где на воде плавают сотни домов-понтонов, под каждым из которых садки с рыбой — басой, тра, карпом хе. В последние годы власти и жители покрасили садки в яркую палитру — красный, оранжевый, жёлтый, зелёный, синий, фиолетовый, — превратив весь посёлок в «красочную деревню садков», отражённую в воде; особенно эффектно это выглядит сверху или на рассвете и закате. Гости обычно плывут на лодке или моторной пироге вдоль слияния рек у Тяудока, чтобы полюбоваться панорамой, заходят на некоторые садки, узнают о садковом рыбоводстве, наблюдают за кормлением и беседуют с речными жителями. Этот опыт часто совмещают с маршрутом Тяудок — чамская деревня Тяузянг — мелалеуковый лес, чтобы полнее почувствовать жизнь дельты. Будучи и источником дохода, и знаменитой фотогеничной достопримечательностью, красочная деревня садков — особая изюминка Анзянга. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Xóm nhà bè nuôi cá sơn màu rực rỡ trên ngã ba sông", "Đẹp nhất lúc bình minh, hoàng hôn hoặc nhìn từ trên cao", "Kết hợp tuyến Châu Đốc – làng Chăm – rừng tràm"],
        "h_en": ["Fish-raft hamlet painted in bright colours at the river junction", "Best at dawn, dusk or seen from above", "Combines with the Chau Doc – Cham village – melaleuca forest route"],
        "h_ru": ["Посёлок рыбных садков в ярких красках на слиянии рек", "Красивее всего на рассвете, закате или сверху", "Совмещается с маршрутом Тяудок — чамская деревня — мелалеуковый лес"],
        "practical": {
            "hours_vi": "Đi thuyền ban ngày; đẹp nhất sáng sớm và chiều.",
            "ticket_vi": "Thuê thuyền/tắc ráng theo nhóm; giá thoả thuận.",
            "duration_vi": "Khoảng 1–2 giờ.",
            "best_time_vi": "Bình minh hoặc hoàng hôn cho ánh sáng đẹp.",
            "tips_vi": "Mặc áo phao khi đi thuyền; mang máy ảnh; hỏi giá trước và đi ghép đoàn cho tiết kiệm.",
        },
    },
))

NEW.append(mk(
    "lang-cham-chau-giang", "Làng Chăm Châu Giang",
    "Chau Giang Cham Village", "Чамская деревня Тяузянг",
    10.6930, 105.1280, ["other", "church"],
    "Xã Châu Phong, thị xã Tân Châu, tỉnh An Giang",
    ["village", "cham", "culture", "mosque", "craft"],
    {
        "rating": {"value": 4.3, "count": 800, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích khám phá làng người Chăm theo đạo Hồi bên sông Hậu với thánh đường, nhà sàn gỗ và nghề dệt thổ cẩm truyền thống. Nhiều người khen văn hoá độc đáo, người dân thân thiện; lưu ý ăn mặc lịch sự khi thăm thánh đường.",
        "ps_vi": "Làng Chăm Châu Giang nằm bên bờ sông Hậu, đối diện Châu Đốc, là nơi sinh sống lâu đời của cộng đồng người Chăm theo đạo Hồi (Islam). Du khách đến để chiêm ngưỡng các thánh đường Hồi giáo, nhà sàn gỗ truyền thống và tìm hiểu nghề dệt thổ cẩm, đời sống văn hoá đặc sắc.",
        "ps_en": "Chau Giang Cham Village sits on the bank of the Hau River opposite Chau Doc, a long-established home of the Muslim Cham community. Visitors come to see the mosques, traditional wooden stilt houses and to learn about brocade weaving and the community's distinctive culture.",
        "ps_ru": "Чамская деревня Тяузянг стоит на берегу реки Хау напротив Тяудока — давнее поселение мусульманской общины чамов. Гости приезжают, чтобы увидеть мечети, традиционные деревянные свайные дома и узнать о ткачестве парчи и самобытной культуре общины.",
        "pl_vi": "Làng Chăm Châu Giang thuộc xã Châu Phong, nằm bên bờ sông Hậu, chỉ cách trung tâm Châu Đốc một chuyến đò ngang. Đây là một trong những nơi tập trung đông đảo cộng đồng người Chăm theo đạo Hồi (Islam) ở An Giang, với lịch sử định cư hàng trăm năm. Đến đây, du khách được bước vào một không gian văn hoá rất khác biệt so với vùng đồng bằng xung quanh: những thánh đường (masjid) và tiểu thánh đường mang kiến trúc Hồi giáo với vòm cong, tháp nhọn và màu sắc trang nhã; những ngôi nhà sàn bằng gỗ cao ráo, thoáng mát, phù hợp với vùng sông nước; cùng nếp sinh hoạt, trang phục và ẩm thực đậm bản sắc Chăm. Một nét hấp dẫn khác của làng là nghề dệt thổ cẩm truyền thống, nơi du khách có thể xem các khung cửi dệt nên những tấm vải, khăn, xà rông với hoa văn tinh xảo và mua làm quà. Người dân thân thiện, sẵn lòng giới thiệu về tôn giáo, phong tục của mình. Chuyến thăm làng Chăm Châu Giang thường được kết hợp với làng bè sắc màu và Châu Đốc, tạo nên hành trình khám phá sự đa dạng văn hoá độc đáo của vùng đầu nguồn. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Chau Giang Cham Village, in Chau Phong commune on the bank of the Hau River, is just a short ferry ride from central Chau Doc. It is one of the main concentrations of the Muslim Cham community in An Giang, with centuries of settlement. Here visitors step into a cultural world quite different from the surrounding delta: mosques and prayer halls with Islamic architecture — arched domes, pointed minarets and elegant colours; tall, airy wooden stilt houses suited to the watery land; and Cham dress, cuisine and daily customs full of identity. Another draw is the traditional brocade-weaving craft, where visitors can watch looms turn out cloth, scarves and sarongs with intricate patterns and buy them as gifts. The people are welcoming and glad to explain their religion and customs. A visit to Chau Giang Cham Village is usually combined with the colourful raft village and Chau Doc, forming a journey through the striking cultural diversity of the upper delta. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Чамская деревня Тяузянг в общине Тяуфонг на берегу реки Хау находится всего в короткой переправе на пароме от центра Тяудока. Это одно из главных мест сосредоточения мусульманской общины чамов в Анзянге, с многовековой историей поселения. Здесь гости попадают в культурный мир, совсем непохожий на окружающую дельту: мечети и молитвенные залы с исламской архитектурой — арочные купола, остроконечные минареты и сдержанные цвета; высокие, проветриваемые деревянные свайные дома, подходящие для водного края; а также чамская одежда, кухня и повседневные обычаи, полные самобытности. Ещё одна достопримечательность — традиционное ткачество парчи, где можно посмотреть, как на станках создают ткани, платки и саронги со сложными узорами, и купить их в подарок. Жители гостеприимны и охотно рассказывают о своей религии и обычаях. Посещение чамской деревни Тяузянг обычно совмещают с красочной деревней садков и Тяудоком, образуя путешествие по яркому культурному разнообразию верхней дельты. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Cộng đồng người Chăm theo đạo Hồi bên bờ sông Hậu", "Thánh đường Hồi giáo và nhà sàn gỗ truyền thống", "Nghề dệt thổ cẩm Chăm tinh xảo để xem và mua quà"],
        "h_en": ["Muslim Cham community on the bank of the Hau River", "Islamic mosques and traditional wooden stilt houses", "Intricate Cham brocade weaving to watch and buy"],
        "h_ru": ["Мусульманская община чамов на берегу реки Хау", "Исламские мечети и традиционные деревянные свайные дома", "Тонкое чамское ткачество парчи — посмотреть и купить"],
        "practical": {
            "hours_vi": "Ban ngày; qua làng bằng đò ngang từ Châu Đốc.",
            "ticket_vi": "Miễn phí; trả phí đò và mua thổ cẩm nếu thích.",
            "duration_vi": "Khoảng 1,5–2 giờ.",
            "best_time_vi": "Buổi sáng cho mát; tránh giờ cầu nguyện nếu vào thánh đường.",
            "tips_vi": "Ăn mặc kín đáo, lịch sự; xin phép trước khi chụp ảnh; tôn trọng nghi lễ tôn giáo.",
        },
    },
))

NEW.append(mk(
    "cho-chau-doc", "Chợ Châu Đốc",
    "Chau Doc Market", "Рынок Тяудок",
    10.7020, 105.1160, ["square_street", "other"],
    "Phường Châu Đốc, tỉnh An Giang",
    ["market", "food", "shopping", "local", "specialty"],
    {
        "rating": {"value": 4.3, "count": 3500, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách gọi Châu Đốc là 'vương quốc mắm' với vô số sạp mắm cá đủ loại, khô, đường thốt nốt và đặc sản miền Tây. Nhiều người khen nhộn nhịp, nhiều đồ mua về; lưu ý nên mặc cả và hỏi kỹ khi mua mắm, khô.",
        "ps_vi": "Chợ Châu Đốc là khu chợ sầm uất nổi tiếng khắp miền Tây, được mệnh danh là 'vương quốc mắm'. Hàng trăm sạp bày đủ loại mắm cá, khô, đường thốt nốt và đặc sản An Giang, là nơi mua sắm và khám phá ẩm thực hấp dẫn khi ghé Châu Đốc.",
        "ps_en": "Chau Doc Market is a bustling market famous across the Mekong Delta, nicknamed the 'kingdom of fermented fish.' Hundreds of stalls display every kind of mam (fermented fish), dried fish, palm sugar and An Giang specialities, making it a great place to shop and explore local food in Chau Doc.",
        "ps_ru": "Рынок Тяудок — оживлённый рынок, знаменитый на всю дельту Меконга и прозванный «королевством ферментированной рыбы». Сотни прилавков предлагают всевозможные мам (ферментированную рыбу), сушёную рыбу, пальмовый сахар и деликатесы Анзянга — отличное место для покупок и знакомства с местной кухней.",
        "pl_vi": "Chợ Châu Đốc là một trong những khu chợ nổi tiếng và nhộn nhịp nhất miền Tây Nam Bộ, nằm ngay trung tâm thành phố Châu Đốc, gần bến sông và khu vực Miếu Bà Chúa Xứ. Nổi danh khắp cả nước, Châu Đốc được người dân ưu ái gọi là 'vương quốc mắm', bởi nơi đây tập trung hàng trăm sạp bán các loại mắm cá đặc trưng của vùng đầu nguồn: mắm cá linh, mắm cá lóc, mắm cá sặc, mắm thái, cùng vô số loại khô cá, khô rắn. Những dãy sạp mắm chất cao, đủ màu sắc, hương vị đậm đà đã trở thành hình ảnh gắn liền với chợ. Bên cạnh mắm và khô, chợ còn bán đường thốt nốt, bánh bò thốt nốt, tung lò mò (lạp xưởng bò của người Chăm), trái cây và nhiều đặc sản khác để du khách mua về làm quà. Không khí chợ luôn tấp nập, tiếng mua bán rộn ràng, phản ánh đời sống thương hồ sung túc của vùng biên giới Tây Nam. Ghé chợ Châu Đốc, du khách vừa được thưởng thức, mua sắm, vừa cảm nhận rõ nét văn hoá ẩm thực đặc sắc của An Giang. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Chau Doc Market is one of the most famous and lively markets in the south-western delta, right in the centre of Chau Doc city near the riverside and the Ba Chua Xu Temple. Renowned nationwide, Chau Doc is fondly called the 'kingdom of fermented fish,' for it gathers hundreds of stalls selling the region's signature mam: linh-fish mam, snakehead mam, gourami mam and shredded mam, along with countless dried fish and dried snake. The tall, colourful mounds of mam with their rich aromas have become the market's defining image. Besides mam and dried fish, the market sells palm sugar, palm-sugar cakes, tung lo mo (Cham beef sausage), fruit and many other specialities to take home as gifts. The market is always crowded and loud with trading, reflecting the prosperous river-trade life of the south-western borderland. A stop at Chau Doc Market lets visitors taste, shop and clearly feel the distinctive food culture of An Giang. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Рынок Тяудок — один из самых известных и оживлённых рынков юго-западной дельты, прямо в центре города Тяудок, у реки и рядом с храмом Ба Тюа Сы. Знаменитый по всей стране, Тяудок ласково называют «королевством ферментированной рыбы»: здесь сотни прилавков торгуют фирменными мам края — мам из рыбы линь, из змееголова, из гурами и рубленым мам, а также бесчисленной сушёной рыбой и вяленой змеёй. Высокие пёстрые горки мам с насыщенным ароматом стали визитной карточкой рынка. Помимо мам и сушёной рыбы, здесь продают пальмовый сахар, пирожные из пальмового сахара, тунг-ло-мо (чамскую говяжью колбасу), фрукты и множество других деликатесов на подарки. Рынок всегда полон народа и шумит торговлей, отражая зажиточную речную торговую жизнь юго-западного пограничья. Заглянув на рынок Тяудок, гости пробуют, покупают и ясно ощущают самобытную гастрономическую культуру Анзянга. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["'Vương quốc mắm' với hàng trăm sạp mắm và khô", "Đặc sản: đường thốt nốt, bánh bò, tung lò mò của người Chăm", "Gần bến sông và Miếu Bà Chúa Xứ Núi Sam"],
        "h_en": ["'Kingdom of fermented fish' with hundreds of mam and dried-fish stalls", "Specialities: palm sugar, palm cakes, Cham beef sausage", "Near the riverside and the Ba Chua Xu Temple"],
        "h_ru": ["«Королевство ферментированной рыбы» с сотнями прилавков мам и сушёной рыбы", "Деликатесы: пальмовый сахар, пирожные, чамская говяжья колбаса", "Рядом с рекой и храмом Ба Тюа Сы"],
        "practical": {
            "hours_vi": "Khoảng 5:00–18:00; sáng đông và nhiều hàng nhất.",
            "ticket_vi": "Vào chợ miễn phí; trả tiền theo món mua.",
            "duration_vi": "Khoảng 1 giờ.",
            "best_time_vi": "Buổi sáng cho hàng tươi và không khí nhộn nhịp.",
            "tips_vi": "Mặc cả khi mua; hỏi kỹ loại mắm/khô và hạn dùng; đóng gói kỹ khi mang đi xa.",
        },
    },
))

NEW.append(mk(
    "cu-lao-gieng", "Cù lao Giêng",
    "Cu Lao Gieng Island", "Остров Кулаозьенг",
    10.4400, 105.4000, ["church", "other"],
    "Huyện Chợ Mới, tỉnh An Giang",
    ["island", "river", "church", "heritage", "quiet"],
    {
        "rating": {"value": 4.4, "count": 600, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích cù lao xanh mát giữa sông Tiền với nhà thờ cổ bề thế, tu viện, chùa và vườn cây trái. Nhiều người khen yên bình, kiến trúc đẹp; lưu ý phải qua phà và nên thuê xe máy để đi quanh cù lao.",
        "ps_vi": "Cù lao Giêng là dải đất trù phú giữa sông Tiền thuộc huyện Chợ Mới, nổi tiếng với nhà thờ Cù lao Giêng cổ kính — một trong những nhà thờ lâu đời nhất Nam Bộ — cùng nhiều tu viện, chùa và vườn cây trái. Không gian xanh mát, thanh bình mang đậm nét miền Tây sông nước.",
        "ps_en": "Cu Lao Gieng is a fertile island in the middle of the Tien River in Cho Moi district, famous for the ancient Cu Lao Gieng Church — one of the oldest churches in southern Vietnam — along with convents, pagodas and orchards. Its cool green, peaceful setting is quintessential Mekong Delta.",
        "ps_ru": "Кулаозьенг — плодородный остров посреди реки Тьен в районе Тьомой, знаменитый старинной церковью Кулаозьенг — одной из древнейших на юге Вьетнама — а также монастырями, пагодами и фруктовыми садами. Прохладная зелёная и мирная атмосфера типична для дельты Меконга.",
        "pl_vi": "Cù lao Giêng là một cù lao lớn nằm giữa dòng sông Tiền, thuộc huyện Chợ Mới, tỉnh An Giang, được bao bọc bởi những vườn cây trái xum xuê và ruộng đồng trù phú. Nơi đây nổi tiếng bởi sự hội tụ của nhiều công trình tôn giáo có giá trị lịch sử và kiến trúc. Đáng chú ý nhất là nhà thờ Cù lao Giêng, được xây dựng từ nửa cuối thế kỷ 19, mang phong cách kiến trúc Roman với mặt tiền bề thế, tháp chuông cao và những mái vòm uy nghi, được xem là một trong những nhà thờ cổ và đẹp nhất vùng Nam Bộ. Bên cạnh đó, cù lao còn có tu viện Chúa Quan Phòng, các ngôi chùa và đình cổ, phản ánh sự chung sống hoà hợp giữa các tôn giáo và cộng đồng dân cư. Đến Cù lao Giêng, du khách phải qua phà băng sông, rồi thong dong đạp xe hay chạy xe máy trên những con đường nhỏ rợp bóng cây, ghé thăm các công trình tín ngưỡng, vườn trái cây và trò chuyện với người dân hiền hoà. Vẻ đẹp yên bình, cổ kính cùng không khí trong lành khiến cù lao trở thành điểm đến lý tưởng cho ai muốn tìm sự tĩnh lặng giữa miền Tây sông nước. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "Cu Lao Gieng is a large island in the middle of the Tien River in Cho Moi district of An Giang, ringed by lush orchards and fertile fields. It is renowned for a cluster of religious buildings of historical and architectural value. The most notable is Cu Lao Gieng Church, built in the latter half of the 19th century in Romanesque style with an imposing façade, a tall bell tower and stately arches, regarded as one of the oldest and most beautiful churches in southern Vietnam. The island also has the Providence convent, old pagodas and communal houses, reflecting the harmonious coexistence of different faiths and communities. Reaching Cu Lao Gieng means crossing the river by ferry and then cycling or riding a motorbike along small tree-shaded lanes, stopping at the places of worship and orchards and chatting with the gentle locals. Its peaceful, old-world beauty and fresh air make the island an ideal destination for anyone seeking quiet in the watery delta. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Кулаозьенг — большой остров посреди реки Тьен в районе Тьомой провинции Анзянг, окружённый пышными садами и плодородными полями. Он известен скоплением религиозных сооружений исторической и архитектурной ценности. Самое примечательное — церковь Кулаозьенг, построенная во второй половине XIX века в романском стиле с внушительным фасадом, высокой колокольней и величественными арками; её считают одной из старейших и красивейших церквей юга Вьетнама. На острове также есть монастырь Провидения, старинные пагоды и общинные дома, что отражает гармоничное сосуществование разных верований и общин. Чтобы добраться до Кулаозьенга, нужно переправиться через реку на пароме, а затем неспешно ехать на велосипеде или мотоцикле по узким тенистым дорожкам, заходя в храмы и сады и беседуя с приветливыми жителями. Мирная старинная красота и свежий воздух делают остров идеальным местом для тех, кто ищет тишину в водной дельте. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Cù lao trù phú giữa sông Tiền, nhiều vườn cây trái", "Nhà thờ Cù lao Giêng cổ, một trong những nhà thờ đẹp nhất Nam Bộ", "Tu viện, chùa, đình cổ — không gian tôn giáo đa dạng, yên bình"],
        "h_en": ["Fertile island in the Tien River with many orchards", "Ancient Cu Lao Gieng Church, among southern Vietnam's finest", "Convent, pagodas and old communal houses — a diverse, peaceful setting"],
        "h_ru": ["Плодородный остров на реке Тьен с фруктовыми садами", "Старинная церковь Кулаозьенг — одна из красивейших на юге", "Монастырь, пагоды и старинные дома — разнообразная и мирная атмосфера"],
        "practical": {
            "hours_vi": "Ban ngày; qua cù lao bằng phà.",
            "ticket_vi": "Miễn phí tham quan; trả phí phà và thuê xe.",
            "duration_vi": "Nửa ngày.",
            "best_time_vi": "Mùa trái cây (khoảng tháng 5–8) hoặc sáng mát.",
            "tips_vi": "Thuê xe đạp/xe máy để đi quanh; mặc lịch sự khi vào nhà thờ, chùa; mang nước và mũ.",
        },
    },
))

NEW.append(mk(
    "oc-eo-ba-the", "Khu di tích Óc Eo – Ba Thê",
    "Oc Eo – Ba The Archaeological Site", "Археологический памятник Окео — Батхе",
    10.2350, 105.1470, ["monument", "museum", "other"],
    "Thị trấn Óc Eo, huyện Thoại Sơn, tỉnh An Giang",
    ["history", "archaeology", "heritage", "unesco-tentative", "ancient"],
    {
        "rating": {"value": 4.3, "count": 500, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách quan tâm lịch sử thích thú với di chỉ nền văn hoá Óc Eo — vương quốc Phù Nam cổ, cùng hiện vật, nền gạch và núi Ba Thê. Nhiều người khen ý nghĩa khảo cổ lớn; lưu ý nên có hướng dẫn để hiểu rõ và nắng nóng vùng đồng bằng.",
        "ps_vi": "Khu di tích Óc Eo – Ba Thê ở huyện Thoại Sơn là trung tâm của nền văn hoá Óc Eo, gắn với vương quốc Phù Nam cổ phát triển rực rỡ những thế kỷ đầu Công nguyên. Các di chỉ khảo cổ, nền kiến trúc gạch, tượng và hiện vật quý cùng núi Ba Thê tạo nên điểm đến giàu giá trị lịch sử.",
        "ps_en": "The Oc Eo – Ba The Archaeological Site in Thoai Son district is the heart of the Oc Eo culture, tied to the ancient kingdom of Funan that flourished in the first centuries CE. Excavations, brick foundations, statues and precious artefacts, together with Ba The Mountain, make it a destination rich in history.",
        "ps_ru": "Археологический памятник Окео — Батхе в районе Тхоайшон — сердце культуры Окео, связанной с древним царством Фунань, процветавшим в первые века нашей эры. Раскопки, кирпичные фундаменты, статуи и ценные артефакты вместе с горой Батхе делают это место богатым историей.",
        "pl_vi": "Khu di tích Óc Eo – Ba Thê nằm ở thị trấn Óc Eo và vùng núi Ba Thê, huyện Thoại Sơn, được xem là trung tâm quan trọng nhất của nền văn hoá Óc Eo — một nền văn minh cổ gắn liền với vương quốc Phù Nam từng phát triển rực rỡ ở đồng bằng sông Cửu Long trong khoảng thế kỷ 1 đến thế kỷ 7 sau Công nguyên. Qua nhiều đợt khai quật, các nhà khảo cổ đã phát hiện tại đây hàng loạt di chỉ có giá trị: nền móng kiến trúc bằng gạch và đá, hệ thống kênh cổ, cùng vô số hiện vật như tượng thần, tượng Phật, đồ trang sức vàng, con dấu, tiền cổ và các mảnh gốm, cho thấy Óc Eo từng là một thương cảng sầm uất giao thương với Ấn Độ, Ba Tư và cả La Mã. Ngày nay, du khách có thể tham quan các hố khai quật được bảo tồn, nhà trưng bày hiện vật và leo núi Ba Thê để viếng chùa, ngắm cảnh đồng bằng bao la. Với tầm vóc là một trong những di tích khảo cổ tiêu biểu của Đông Nam Á, Óc Eo – Ba Thê đang được đề cử là Di sản văn hoá thế giới, mang lại trải nghiệm khám phá chiều sâu lịch sử hiếm có cho du khách. An Giang (mới) hình thành từ ngày 1 tháng 7 năm 2025 trên cơ sở hợp nhất An Giang và Kiên Giang.",
        "pl_en": "The Oc Eo – Ba The Archaeological Site, spread over Oc Eo town and the Ba The hills in Thoai Son district, is regarded as the most important centre of the Oc Eo culture — an ancient civilisation linked to the kingdom of Funan that flourished in the Mekong Delta from roughly the 1st to the 7th century CE. Through many excavation campaigns, archaeologists have uncovered a wealth of remains: brick and stone architectural foundations, ancient canal systems, and countless artefacts such as deity and Buddha statues, gold jewellery, seals, old coins and pottery shards, showing that Oc Eo was once a thriving port trading with India, Persia and even Rome. Today visitors can see preserved excavation pits, an artefact display house, and climb Ba The Mountain to visit temples and take in the vast delta landscape. As one of Southeast Asia's most significant archaeological sites, Oc Eo – Ba The is being nominated as a World Cultural Heritage site, offering a rare journey into historical depth. The new An Giang Province was formed on 1 July 2025 by merging An Giang and Kien Giang.",
        "pl_ru": "Археологический памятник Окео — Батхе, раскинувшийся вокруг посёлка Окео и холмов Батхе в районе Тхоайшон, считается важнейшим центром культуры Окео — древней цивилизации, связанной с царством Фунань, которое процветало в дельте Меконга примерно с I по VII век нашей эры. В ходе многих раскопочных кампаний археологи обнаружили здесь множество памятников: кирпичные и каменные архитектурные фундаменты, древние каналы, а также бесчисленные артефакты — статуи божеств и Будды, золотые украшения, печати, старинные монеты и черепки керамики, — что свидетельствует: Окео был оживлённым портом, торговавшим с Индией, Персией и даже Римом. Сегодня посетители могут осмотреть сохранённые раскопы, зал с артефактами и подняться на гору Батхе, чтобы посетить храмы и полюбоваться бескрайней дельтой. Как один из значимейших археологических памятников Юго-Восточной Азии, Окео — Батхе номинируется в список Всемирного культурного наследия, даря редкое погружение в глубину истории. Новая провинция Анзянг образована 1 июля 2025 года путём объединения Анзянга и Кьензянга.",
        "h_vi": ["Trung tâm văn hoá Óc Eo — vương quốc Phù Nam cổ (thế kỷ 1–7)", "Nền gạch, kênh cổ, tượng thần, vàng, con dấu, tiền cổ", "Đang được đề cử Di sản văn hoá thế giới; có núi Ba Thê"],
        "h_en": ["Centre of Oc Eo culture — ancient Funan (1st–7th c.)", "Brick foundations, old canals, deity statues, gold, seals, coins", "Nominated as World Cultural Heritage; includes Ba The Mountain"],
        "h_ru": ["Центр культуры Окео — древнего Фунаня (I–VII вв.)", "Кирпичные фундаменты, древние каналы, статуи, золото, печати, монеты", "Номинируется во Всемирное наследие; включает гору Батхе"],
        "practical": {
            "hours_vi": "Khoảng 7:00–17:00; nhà trưng bày có thể nghỉ trưa.",
            "ticket_vi": "Phí tham quan thấp; nên kiểm tra tại chỗ.",
            "duration_vi": "Khoảng 2–3 giờ (gồm leo núi Ba Thê).",
            "best_time_vi": "Sáng sớm cho mát; mùa khô tháng 11–4.",
            "tips_vi": "Nên có hướng dẫn viên để hiểu di chỉ; mang mũ, nước vì nắng; giày thoải mái để leo núi Ba Thê.",
        },
    },
))

# ===INSERT_RECORDS_ABOVE===

def main():
    d = json.load(open(F, encoding="utf-8")) if os.path.exists(F) else []
    have = {p["slug"] for p in d}
    added = [p for p in NEW if p["slug"] not in have]
    d += added
    json.dump(d, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Them moi:", len(added), "| tong hien co:", len(d))
    print("Slug them:", ", ".join(p["slug"] for p in added))
    skipped = [p["slug"] for p in NEW if p["slug"] in have]
    if skipped:
        print("Bo qua (da co):", ", ".join(skipped))


if __name__ == "__main__":
    main()
