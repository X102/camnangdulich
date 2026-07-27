# -*- coding: utf-8 -*-
"""_add_places_tatarstan_batch2_20260727.py — VÙNG TIÊU ĐIỂM: Tatarstan (lần chạy tự động 2026-07-27, đợt 2).

Bối cảnh: các lần chạy trước đã nâng tatarstan.json: 10 -> 26 -> 33 địa điểm.
Đợt này bổ sung 15 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU (đối chiếu 33 slug hiện có,
đối chiếu cả theo đối tượng thực tế) => mục tiêu ~48/50.

Đa dạng loại hình: tháp biểu tượng, nhà thờ cổ trong kremlin, nhà hát múa rối, sân vận động
hiện đại, công viên trung tâm & công viên cải tạo, bảo tàng tư nhân & bảo tàng nhà văn,
hang động & núi cảnh quan bên sông Volga, tu viện trên sông, thành cổ khảo cổ, thị trấn Volga,
đài tưởng niệm kiểu kim tự tháp.

TOẠ ĐỘ: xác minh chéo Wikipedia (RU, mục geo), Wikidata, tourister.ru, sobory.ru, 2GIS,
visit-tatarstan, Yandex Maps — 2026-07. Kiểm tra thứ tự (Nga: lat 54–56,7; lon 47–54 với
Tatarstan; KHÔNG đảo lat/lon; đều nằm trong Tatarstan). Link bản đồ TRỎ-ĐỊA-ĐIỂM (text search
theo tên+thành phố, hoặc URL trang tổ chức Yandex nơi tra được).

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

GHI CHÚ (để lần sau xử tiếp, KHÔNG bịa toạ độ):
  - Thư viện Quốc gia Tatarstan (toà NKЦ «Казань» cũ, Пушкина 86): là điểm hiện đại đáng thêm
    nhưng CHƯA xác minh được toạ độ đáng tin (nguồn cho giá trị đáng ngờ ~55.8018 lệch bắc so
    với Пушкина 86). => HOÃN, thêm khi có toạ độ chuẩn.
  - Dendrarium Raifa (Волжско-Камский заповедник, п. Садовый): hay nhưng hơi trùng cụm Raifa
    (đã có tu viện Raifa) và chưa chốt được toạ độ chính xác. => HOÃN.

Chạy:  python3 tools/_add_places_tatarstan_batch2_20260727.py
       python3 tools/normalize_categories.py && python3 tools/build.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"

REGION = "tatarstan"
REGION_NAME_VI = "Cộng hoà Tatarstan"
FD = "Vùng Volga"


def maps_for(name_ru, name_en, city_ru, city_en, lat, lon):
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    parts = [name_en]
    if city_en.lower() not in name_en.lower():
        parts.append(city_en)
    parts.append("Russia")
    gq = urllib.parse.quote(", ".join(parts))
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def gmaps(query):
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(query)


def rec(slug, name_vi, name_ru, name_en, categories, lat, lon, address_vi,
        short, long, highlights, practical, sources, tags,
        maps=None, official_site=None):
    return {
        "id": f"{REGION}-{slug}",
        "slug": slug,
        "region": REGION,
        "region_name_vi": REGION_NAME_VI,
        "federal_district": FD,
        "name_vi": name_vi,
        "name_ru": name_ru,
        "name_en": name_en,
        "categories": categories,
        "coordinates": {"lat": lat, "lon": lon},
        "address_vi": address_vi,
        "rating": None,
        "presentation_short_vi": short,
        "presentation_long_vi": long,
        "highlights_vi": highlights,
        "practical": practical,
        "photo": None,
        "photo_credit": None,
        "maps": maps if maps else maps_for(name_ru, name_en, "Казань", "Kazan", lat, lon),
        "official_site": official_site,
        "sources": sources,
        "tags": tags,
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia",
    }


RECORDS = []

# 1) Tháp Söyembikä ------------------------------------------------------------
RECORDS.append(rec(
    "soyembika-tower",
    "Tháp nghiêng Söyembikä (Bashnya Syuyumbike)",
    "Башня Сююмбике",
    "Söyembikä Tower",
    ["monument", "other"],
    55.80028, 49.10500,
    "Bên trong Điện Kremlin Kazan, phần phía bắc, gần dinh Thống đốc, trung tâm Kazan.",
    "Ngọn tháp gạch bảy tầng cao 58 m nghiêng rõ về phía đông bắc — được coi là biểu tượng kiến "
    "trúc của Kazan và là 'tháp nghiêng' nổi tiếng bậc nhất nước Nga. Tháp gắn với truyền thuyết "
    "bi thương về hoàng hậu Söyembikä của hãn quốc Kazan.",
    "Tháp Söyembikä đứng sừng sững ở phần bắc Điện Kremlin Kazan và là hình ảnh gần như đồng nghĩa "
    "với thành phố. Cao 58 m, tháp gồm bảy tầng thu nhỏ dần — ba tầng dưới hình vuông, hai tầng "
    "bát giác, rồi đến chóp gạch nhọn và ngọn tháp xanh gắn 'trái táo' mạ vàng đội hình lưỡi liềm. "
    "Điểm khiến tháp nổi danh khắp thế giới là độ nghiêng: đỉnh tháp lệch khỏi phương thẳng đứng "
    "khoảng 2 m do móng yếu, xếp tháp vào nhóm 'tháp nghiêng' cùng Pisa. Thời điểm xây dựng vẫn "
    "gây tranh cãi trong giới học thuật: đa số cho rằng tháp được dựng vào cuối thế kỷ 17 – đầu "
    "thế kỷ 18 (khi lập tỉnh Kazan năm 1708) như một tháp canh trên điểm cao nhất thành phố, một "
    "số ý kiến gắn nó với thời hãn quốc. Tên gọi lãng mạn 'Söyembikä' chỉ xuất hiện trong văn học "
    "từ năm 1832, theo tên vị hoàng hậu Tatar cuối cùng; nhiều truyền thuyết dân gian (bà gieo "
    "mình từ tầng bảy để không phải cải giá với Sa hoàng) đều không có căn cứ lịch sử. Năm 1918 "
    "tháp được trao cho cộng đồng Hồi giáo và gắn lưỡi liềm bạc; năm 1993 lưỡi liềm mạ vàng được "
    "phục hồi. Từ đỉnh tháp, ngày trời quang có thể nhìn xa tới tận Sviyazhsk.",
    [
        "Biểu tượng kiến trúc số một của Kazan — 'tháp nghiêng' cao 58 m, đỉnh lệch khoảng 2 m.",
        "Gắn với truyền thuyết bi thương về hoàng hậu Söyembikä của hãn quốc Kazan.",
        "Nằm ngay trong quần thể Kremlin (Di sản UNESCO), dễ ghé cùng Kul-Sharif.",
    ],
    {
        "hours_vi": "Ngắm bên ngoài tự do trong giờ mở cửa Kremlin (thường 8:00–22:00, mùa hè muộn hơn).",
        "ticket_vi": "Vào khuôn viên Kremlin miễn phí; không lên được bên trong tháp.",
        "duration_vi": "Khoảng 15–20 phút để ngắm và chụp ảnh.",
        "best_time_vi": "Chiều muộn – hoàng hôn khi ánh nắng xiên đẹp; ban đêm tháp được chiếu sáng.",
        "tips_vi": "Kết hợp trong lộ trình tham quan Kremlin và Kul-Sharif; đứng lệch góc để thấy rõ độ nghiêng.",
    },
    [
        {"title": "Wikipedia (RU) — Башня Сююмбике (toạ độ 55°48′01″N 49°06′18″E)", "url": "https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D1%88%D0%BD%D1%8F_%D0%A1%D1%8E%D1%8E%D0%BC%D0%B1%D0%B8%D0%BA%D0%B5"},
        {"title": "2GIS Казань — Башня Сююмбике", "url": "https://2gis.ru/kazan/firm/70000001097287719"},
    ],
    ["symbol", "leaning-tower", "kremlin", "monument", "soyembika", "kazan"],
))

# 2) Nhà thờ Truyền Tin (Blagoveshchensky) ------------------------------------
RECORDS.append(rec(
    "annunciation-cathedral",
    "Nhà thờ Truyền Tin trong Kremlin Kazan (Blagoveshchensky sobor)",
    "Благовещенский собор Казанского кремля",
    "Annunciation Cathedral of the Kazan Kremlin",
    ["church"],
    55.79986, 49.10611,
    "Bên trong Điện Kremlin Kazan, phía đông bắc, sát tháp Söyembikä, trung tâm Kazan.",
    "Nhà thờ Chính thống giáo cổ nhất còn lại trong quần thể Kremlin Kazan, khởi dựng ngay sau khi "
    "Kazan bị chiếm năm 1552 và hoàn thành năm 1562 bởi các thợ cả Pskov. Suốt gần bốn thế kỷ đây "
    "là nhà thờ chính toà của giáo phận Kazan.",
    "Nhà thờ Truyền Tin là công trình lịch sử – kiến trúc lâu đời nhất còn tồn tại trong quần thể "
    "Điện Kremlin Kazan. Theo lệnh Sa hoàng Ivan Bạo chúa, nhà thờ được khởi dựng bằng gỗ ngay sau "
    "khi thành Kazan thất thủ tháng 10 năm 1552, rồi được xây lại bằng đá trắng và hoàn thành, "
    "cung hiến năm 1562. Công trình do nhóm thợ cả xứ Pskov thực hiện — được xem là ví dụ xa nhất "
    "về phía đông của trường phái kiến trúc Pskov, với khối nhà thờ năm mái vòm bề thế và khối tháp "
    "chuông (tháp chuông cổ đã bị phá thời Xô-viết). Từ năm 1552 đến 1918, đây là nhà thờ chính toà "
    "của giáo phận Kazan, nơi diễn ra các nghi lễ quan trọng nhất của Chính thống giáo trong vùng. "
    "Nhà thờ từng bị đóng cửa và hư hại nặng thời Liên Xô, sau đó được trùng tu quy mô lớn cùng cả "
    "quần thể Kremlin và mở cửa trở lại; bên dưới có hầm mộ – nơi an nghỉ của một số giám mục Kazan. "
    "Cùng với Kul-Sharif và tháp Söyembikä, nhà thờ tạo nên bộ ba biểu tượng thể hiện sự chung sống "
    "của hai nền văn hoá Hồi giáo và Chính thống giáo trong Kremlin Kazan — Di sản Thế giới UNESCO.",
    [
        "Công trình cổ nhất còn lại trong Kremlin Kazan (1562), do thợ cả Pskov xây dựng.",
        "Từng là nhà thờ chính toà của giáo phận Kazan suốt 1552–1918.",
        "Bộ ba biểu tượng cùng Kul-Sharif và tháp Söyembikä trong quần thể Di sản UNESCO.",
    ],
    {
        "hours_vi": "Mở đón khách trong giờ Kremlin, thường 8:00–18:00; có giờ lễ.",
        "ticket_vi": "Vào cửa tự do; hoan nghênh quyên góp.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; đẹp khi kết hợp lộ trình Kremlin.",
        "tips_vi": "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu; ghé ngay cạnh tháp Söyembikä.",
    },
    [
        {"title": "Wikipedia (RU) — Благовещенский собор Казанского кремля", "url": "https://ru.wikipedia.org/wiki/%D0%91%D0%BB%D0%B0%D0%B3%D0%BE%D0%B2%D0%B5%D1%89%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80_%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%BA%D1%80%D0%B5%D0%BC%D0%BB%D1%8F"},
        {"title": "sobory.ru — Кремль. Кафедральный собор Благовещения", "url": "https://sobory.ru/article/?object=02525"},
    ],
    ["church", "cathedral", "kremlin", "pskov-school", "unesco", "kazan"],
))

# 3) Nhà hát múa rối Ekiyat ----------------------------------------------------
RECORDS.append(rec(
    "ekiyat-puppet-theatre",
    "Nhà hát Múa rối Tatar «Ekiyat» (Teatr kukol «Ekият»)",
    "Татарский государственный театр кукол «Экият»",
    "Ekiyat Tatar State Puppet Theatre",
    ["theatre"],
    55.78000, 49.13806,
    "Phố Peterburgskaya, số 57, gần ga metro Sukonnaya Sloboda, trung tâm Kazan.",
    "Nhà hát múa rối nổi tiếng của Tatarstan trong toà nhà mô phỏng lâu đài cổ tích rực rỡ — một "
    "trong những công trình 'sống ảo' được yêu thích nhất Kazan. Thành lập năm 1934, chuyển sang "
    "toà nhà mới từ 2012, thuộc hàng nhà hát múa rối lớn nhất nước Nga.",
    "«Ekiyat» (tiếng Tatar nghĩa là 'Cổ tích') là nhà hát múa rối quốc gia của Tatarstan, thành lập "
    "năm 1934 và là một trong những đoàn múa rối lâu đời nhất nước Nga. Từ ngày 1/3/2012, nhà hát "
    "chuyển về toà nhà mới trên phố Peterburgskaya, rộng hơn 17.000 m² — được xây theo hình một lâu "
    "đài cổ tích phương Đông với những tháp nhỏ, cột xoắn, đồng hồ trang trí khổng lồ và các mảng "
    "màu rực rỡ, khiến bản thân toà nhà trở thành điểm tham quan và chụp ảnh hút khách. Bên trong có "
    "hai khán phòng (lớn khoảng 250 chỗ, nhỏ khoảng 100 chỗ) trang bị âm thanh – ánh sáng hiện đại; "
    "tiết mục biểu diễn bằng cả tiếng Tatar và tiếng Nga, với hơn 40–50 vở dựa trên cổ tích của các "
    "dân tộc trên thế giới. Tầng bốn có một bảo tàng con rối độc đáo trưng bày rối từ các vở diễn "
    "xưa và của nhiều nhà hát trong, ngoài nước. Đây là điểm đến lý tưởng cho gia đình có trẻ nhỏ, "
    "đồng thời là ví dụ tiêu biểu cho làn sóng công trình văn hoá giàu tính biểu tượng của Kazan "
    "hiện đại. Nhà hát nằm ngay cạnh phố đi bộ Peterburgskaya, thuận tiện kết hợp dạo phố.",
    [
        "Toà nhà hình lâu đài cổ tích rực rỡ — một trong những công trình đẹp và 'sống ảo' nhất Kazan.",
        "Thuộc hàng nhà hát múa rối lớn nhất nước Nga; biểu diễn song ngữ Tatar – Nga.",
        "Có bảo tàng con rối trên tầng bốn; điểm đến lý tưởng cho gia đình có trẻ em.",
    ],
    {
        "hours_vi": "Phòng vé thường mở 9:00–19:00 (nghỉ trưa 13:00–13:30); biểu diễn theo lịch.",
        "ticket_vi": "Vé xem biểu diễn giá phải chăng (khoảng 280–600 rúp tuỳ suất/chỗ).",
        "duration_vi": "Ngắm ngoài 15 phút; một suất diễn khoảng 1 giờ.",
        "best_time_vi": "Quanh năm; kiểm tra lịch diễn trước, đặc biệt cuối tuần.",
        "tips_vi": "Nằm cạnh phố đi bộ Peterburgskaya, gần metro Sukonnaya Sloboda; tiện đi cùng trẻ nhỏ.",
    },
    [
        {"title": "Wikidata — Tatar State Puppet Theatre «Ekiyat» (toạ độ)", "url": "https://www.wikidata.org/wiki/Q13207309"},
        {"title": "Yandex Maps — Экият (trang tổ chức)", "url": "https://yandex.com/maps/org/ekiyat/140266089270/"},
    ],
    ["theatre", "puppet", "fairy-tale-castle", "family", "modern", "kazan"],
    maps={
        "yandex": "https://yandex.com/maps/org/ekiyat/140266089270/",
        "google": gmaps("Ekiyat Tatar Puppet Theatre, Kazan, Russia"),
    },
))

# 4) Sân vận động Ak Bars Arena ------------------------------------------------
RECORDS.append(rec(
    "ak-bars-arena",
    "Sân vận động Ak Bars Arena (Kazan Arena)",
    "Ак Барс Арена",
    "Ak Bars Arena (Kazan Arena)",
    ["other", "monument"],
    55.82104, 49.16096,
    "Phố Chistopolskaya, số 42 / đại lộ Yamasheva 115A, quận Novo-Savinovsky, bên sông Kazanka, Kazan.",
    "Sân vận động hiện đại sức chứa hơn 40.000 chỗ, xây 2010–2013, từng là địa điểm khai mạc "
    "Universiade 2013 và một trong các sân của World Cup 2018. Nổi bật với mặt tiền màn hình LED "
    "khổng lồ — biểu tượng thể thao của Kazan bên sông Kazanka.",
    "Ak Bars Arena (trước đây gọi là Kazan Arena) là sân vận động đa năng lớn nhất Tatarstan, xây "
    "trong các năm 2010–2013 bên bờ sông Kazanka ở quận Novo-Savinovsky, gần công viên nước Riviera "
    "và cụm thể thao phía bắc thành phố. Với sức chứa hơn 40.000 khán giả, sân được thiết kế bởi "
    "cùng nhóm kiến trúc từng làm sân Wembley và Emirates, có hình khối uốn lượn hiện đại và đặc biệt "
    "là một trong những màn hình LED ngoài trời lớn nhất châu Âu phủ kín mặt tiền, biến cả toà nhà "
    "thành một 'màn hình' khổng lồ khi lên đèn. Sân là nơi tổ chức lễ khai mạc và bế mạc "
    "Universiade mùa hè 2013, các trận của Cúp Liên đoàn 2017 và Vòng chung kết World Cup 2018 "
    "(khi mặt sân được cải tạo theo chuẩn FIFA), cùng nhiều sự kiện thể thao – ca nhạc lớn. Đây là "
    "sân nhà của câu lạc bộ bóng đá Rubin Kazan. Ngay cả khi không có trận đấu, kiến trúc và quy mô "
    "của Ak Bars Arena vẫn là một điểm ngắm ấn tượng, minh chứng cho vị thế 'thủ đô thể thao' mà "
    "Kazan đã xây dựng trong hơn một thập kỷ qua.",
    [
        "Sân vận động hơn 40.000 chỗ, biểu tượng 'thủ đô thể thao' Kazan.",
        "Mặt tiền màn hình LED khổng lồ thuộc hàng lớn nhất châu Âu.",
        "Từng tổ chức Universiade 2013 và các trận World Cup 2018.",
    ],
    {
        "hours_vi": "Bên ngoài ngắm tự do; bên trong vào theo sự kiện/tour (kiểm tra lịch).",
        "ticket_vi": "Vé theo trận đấu/sự kiện; một số thời điểm có tour tham quan sân.",
        "duration_vi": "Ngắm ngoài 20–30 phút; xem trận 2 giờ trở lên.",
        "best_time_vi": "Đẹp nhất buổi tối khi mặt tiền LED sáng đèn; theo mùa giải bóng đá.",
        "tips_vi": "Đi tram số 5/6 hoặc taxi; kết hợp dạo kè Kazanka và công viên nước Riviera gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Ак Барс Арена", "url": "https://ru.wikipedia.org/wiki/%D0%90%D0%BA_%D0%91%D0%B0%D1%80%D1%81_%D0%90%D1%80%D0%B5%D0%BD%D0%B0"},
        {"title": "Yandex Maps — Ак Барс Арена (trang tổ chức)", "url": "https://yandex.com/maps/org/ak_bars_arena/1216041023/"},
    ],
    ["stadium", "modern-architecture", "sport", "world-cup", "universiade", "kazan"],
    maps={
        "yandex": "https://yandex.com/maps/org/ak_bars_arena/1216041023/",
        "google": gmaps("Ak Bars Arena, Kazan, Russia"),
    },
))

# 5) Công viên Trung tâm Gorky -------------------------------------------------
RECORDS.append(rec(
    "gorky-park-kazan",
    "Công viên Trung tâm Văn hoá – Nghỉ ngơi Gorky (TsPKiO im. Gorkogo)",
    "Центральный парк культуры и отдыха имени Горького",
    "Gorky Central Park of Culture and Leisure",
    ["park_garden"],
    55.798935, 49.147745,
    "Phố Nikolaya Ershova, số 1, quận Vakhitovsky, gần trung tâm thương mại Korston, Kazan.",
    "Công viên trung tâm lâu đời và được yêu thích của Kazan, không gian xanh rộng cho đi dạo, đạp "
    "xe, chạy bộ và các hoạt động gia đình. Sau đợt cải tạo, công viên trở thành một trong những "
    "'lá phổi' đô thị đẹp và tiện nghi bậc nhất thành phố, mở cửa cả ngày.",
    "Công viên mang tên đại văn hào Maxim Gorky là công viên trung tâm truyền thống của Kazan, nằm "
    "ở quận Vakhitovsky và được giới hạn bởi các phố Ershova, Vishnevskogo, Podluzhnaya cùng khu "
    "trường quân sự Suvorov. Có lịch sử lâu đời, công viên trải qua đợt cải tạo lớn trong thập niên "
    "2010 để trở thành không gian công cộng hiện đại: các lối đi dạo và làn chạy bộ được lát lại, "
    "thêm làn xe đạp – patin, sân chơi trẻ em, khu tập thể thao ngoài trời, quán cà phê, sân khấu "
    "và nhiều tiểu cảnh cây xanh. Đây là nơi người dân Kazan quen lui tới để chạy bộ buổi sáng, đạp "
    "xe, dắt trẻ đi chơi hay dã ngoại cuối tuần; mùa đông một phần công viên biến thành khu trượt "
    "tuyết và sân băng. Nằm sát trung tâm và mở cửa suốt ngày đêm, Gorky là lựa chọn thư giãn dễ "
    "chịu, giúp du khách cảm nhận nhịp sống thường nhật của Kazan giữa những điểm tham quan lịch sử.",
    [
        "Công viên trung tâm lâu đời, đã cải tạo hiện đại — 'lá phổi xanh' của Kazan.",
        "Lối dạo, làn xe đạp – chạy bộ, sân chơi trẻ em, quán cà phê; mở cửa cả ngày.",
        "Mùa đông có khu trượt tuyết và sân băng.",
    ],
    {
        "hours_vi": "Mở tự do cả ngày (24/7); dịch vụ thuê xe đạp/patin theo giờ mở.",
        "ticket_vi": "Vào tự do; thuê xe đạp, patin và một số trò chơi tính phí riêng.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Mùa hè để dạo và đạp xe; mùa đông cho trượt tuyết – trượt băng.",
        "tips_vi": "Gần trung tâm, dễ đi bộ hoặc bắt taxi; mang giày thể thao nếu muốn chạy/đạp xe.",
    },
    [
        {"title": "Wikipedia (RU) — ЦПКиО имени Горького (Казань)", "url": "https://ru.wikipedia.org/wiki/%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%BF%D0%B0%D1%80%D0%BA_%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D1%8B_%D0%B8_%D0%BE%D1%82%D0%B4%D1%8B%D1%85%D0%B0_%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8_%D0%93%D0%BE%D1%80%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE_(%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C)"},
        {"title": "culture.ru — Парк им. Горького г. Казани", "url": "https://www.culture.ru/institutes/87259/park-im-gorkogo-g-kazani"},
    ],
    ["park", "recreation", "family", "cycling", "kazan"],
))

# 6) Công viên Hồ Đen (Chёrnoye Ozero) ----------------------------------------
RECORDS.append(rec(
    "black-lake-park",
    "Công viên Hồ Đen (Park «Chёrnoye Ozero»)",
    "Парк «Чёрное озеро»",
    "Black Lake Park",
    ["park_garden"],
    55.794932, 49.117697,
    "Giữa các phố Dzerzhinskogo, Chernyshevskogo và Lobachevskogo, quận Vakhitovsky, trung tâm Kazan.",
    "Công viên nhỏ ngay trung tâm Kazan, gắn với 'Vòm Tình yêu' (Arka vlyublyonnykh) nổi tiếng có "
    "hiệu ứng âm thanh thì thầm. Sau đợt cải tạo, đây là không gian dạo chơi, hẹn hò và trượt băng "
    "mùa đông được người dân yêu thích.",
    "Công viên Hồ Đen nằm trong một vùng trũng kéo dài theo hướng đông – tây ở ngay trung tâm Kazan, "
    "được giới hạn bởi các phố Dzerzhinskogo, Chernyshevskogo và Lobachevskogo. Điểm nổi tiếng nhất "
    "của công viên là 'Vòm Tình yêu' — một vòm parabol bằng bê tông trắng dựng từ thập niên 1930 ở "
    "lối vào khu vườn phía đông: nhờ hình dạng đặc biệt, hai người đứng quay mặt vào hai chân vòm "
    "và thì thầm vẫn nghe rõ tiếng nhau, nên vòm trở thành điểm hẹn hò và chụp ảnh cưới quen thuộc. "
    "Phần phía tây công viên có một hồ nước; mùa đông hồ được cải tạo thành sân trượt băng với điểm "
    "cho thuê giày ngay gần đó. Trải qua đợt cải tạo lớn trong thập niên 2010, công viên có thêm "
    "lối dạo lát mới, ghế ngồi, cây xanh và ánh sáng, trở thành một không gian công cộng nhỏ nhưng "
    "duyên dáng giữa lòng thành phố. Vì nằm sát phố Kremlyovskaya và khu đại học, đây là chỗ nghỉ "
    "chân lý tưởng khi đi bộ tham quan trung tâm lịch sử Kazan.",
    [
        "'Vòm Tình yêu' bê tông trắng thập niên 1930 với hiệu ứng âm thanh thì thầm độc đáo.",
        "Công viên trung tâm đã cải tạo, có hồ nước; mùa đông thành sân trượt băng.",
        "Vị trí đắc địa sát phố Kremlyovskaya, tiện nghỉ chân khi dạo trung tâm.",
    ],
    {
        "hours_vi": "Mở tự do cả ngày; sân băng hoạt động theo mùa đông.",
        "ticket_vi": "Vào tự do; thuê giày trượt băng tính phí riêng.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Chiều tối mùa hè; mùa đông để trượt băng trên hồ.",
        "tips_vi": "Thử hiệu ứng thì thầm ở 'Vòm Tình yêu'; gần Kremlin và phố đi bộ, dễ kết hợp.",
    },
    [
        {"title": "Wikipedia (RU) — Чёрное озеро (парк, Казань)", "url": "https://ru.wikipedia.org/wiki/%D0%A7%D1%91%D1%80%D0%BD%D0%BE%D0%B5_%D0%BE%D0%B7%D0%B5%D1%80%D0%BE_(%D0%BF%D0%B0%D1%80%D0%BA,_%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C)"},
        {"title": "Yandex Maps — Парк «Чёрное озеро» (trang tổ chức)", "url": "https://yandex.com/maps/org/chernoye_ozero/4342596674/"},
    ],
    ["park", "arch-of-lovers", "ice-rink", "romantic", "kazan"],
    maps={
        "yandex": "https://yandex.com/maps/org/chernoye_ozero/4342596674/",
        "google": gmaps("Black Lake Park Chernoye Ozero, Kazan, Russia"),
    },
))

# 7) Bảo tàng Đời sống Xã hội chủ nghĩa ----------------------------------------
RECORDS.append(rec(
    "museum-socialist-life",
    "Bảo tàng Đời sống Xã hội chủ nghĩa (Muzey sotsialisticheskogo byta)",
    "Музей социалистического быта",
    "Museum of Socialist Life (Soviet Lifestyle Museum)",
    ["museum"],
    55.78703, 49.11965,
    "Phố Universitetskaya, số 6 (gần góc phố Ostrovskogo), sát phố đi bộ Bauman, trung tâm Kazan.",
    "Bảo tàng tư nhân độc đáo về đời sống thời Liên Xô những năm 1960–1980, đặt trong một căn hộ "
    "tập thể (kommunalka) cũ. Không gian 'cỗ máy thời gian' đầy hoài niệm với hàng nghìn đồ vật đời "
    "thường, cùng 'Đại sảnh Rock-n-roll' trưng bày guitar có chữ ký nghệ sĩ.",
    "Bảo tàng Đời sống Xã hội chủ nghĩa là một trong những bảo tàng tư nhân được yêu thích nhất "
    "Kazan, do nhiếp ảnh gia – nhà thiết kế Rustem Valiakhmetov gây dựng từ bộ sưu tập cá nhân bắt "
    "đầu thập niên 1990, khi nhiều người vứt bỏ đồ dùng thời Xô-viết. Bảo tàng nằm trong một căn hộ "
    "tập thể (kommunalka) của toà nhà xây từ giữa thế kỷ 19, giữ nguyên tường gạch, hệ dây điện cũ, "
    "lò sưởi gang và công tắc thời bao cấp — bản thân không gian đã là một hiện vật. Khoảng vài trăm "
    "hiện vật tái hiện đời sống Liên Xô thập niên 1960–1980: đồ gia dụng, đồ chơi, máy ảnh, xe đạp, "
    "nước hoa, quân trang, huy hiệu thiếu niên tiền phong và đoàn viên… tất cả đều là đồ thật, khách "
    "được chạm và thử. Điểm nhấn thú vị là 'Đại sảnh Rock-n-roll' với khoảng một trăm cây guitar và "
    "kỷ vật có chữ ký của các nhạc sĩ Nga nổi tiếng, cùng những góc trưng bày về quần jean, thói "
    "quen thời bao cấp và văn hoá ngầm. Vui nhộn, giàu hoài niệm và rất 'chụp ảnh được', đây là điểm "
    "dừng chân thú vị ngay cạnh phố đi bộ Bauman, phù hợp cho cả người lớn muốn hoài niệm lẫn du "
    "khách trẻ tò mò về nước Nga Xô-viết.",
    [
        "Đặt trong căn hộ tập thể (kommunalka) cũ — không gian 'cỗ máy thời gian' thời Liên Xô.",
        "Hàng trăm hiện vật đời thường 1960–1980 mà khách được chạm và thử.",
        "'Đại sảnh Rock-n-roll' với nhiều guitar và kỷ vật có chữ ký nghệ sĩ nổi tiếng.",
    ],
    {
        "hours_vi": "Mở hằng ngày, khoảng 10:00–20:00 (kiểm tra trước khi tới).",
        "ticket_vi": "Có bán vé vào cửa (vé người lớn/trẻ em khác nhau).",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm; tiện ghé khi dạo phố Bauman.",
        "tips_vi": "Cách phố Bauman/quảng trường Tukay vài phút đi bộ; đồ vật được phép chụp và thử.",
    },
    [
        {"title": "tourister.ru — Музей социалистического быта в Казани", "url": "https://www.tourister.ru/world/europe/russia/city/kazan/museum/17906"},
        {"title": "visit-tatarstan.com — Музей социалистического быта", "url": "https://visit-tatarstan.com/en/places/cultural/muzej_socialisticheskogo_byta/"},
    ],
    ["museum", "soviet", "nostalgia", "rock-n-roll", "private-museum", "kazan"],
))

# 8) Nhà Shamil & Bảo tàng Tukay ----------------------------------------------
RECORDS.append(rec(
    "shamil-house-tukay-museum",
    "Nhà Shamil & Bảo tàng Văn học Gabdulla Tukay (Dom Shamilya)",
    "Литературный музей Габдуллы Тукая (Дом Шамиля)",
    "Gabdulla Tukay Literary Museum (Shamil House)",
    ["museum", "monument"],
    55.777494, 49.115469,
    "Phố Gabdully Tukaya, số 74, khu phố Tatar Cổ (Staro-Tatarskaya Sloboda), Kazan.",
    "Bảo tàng về Gabdulla Tukay — nhà thơ dân tộc vĩ đại của người Tatar — đặt trong 'Nhà Shamil', "
    "một trong những dinh thự đẹp nhất khu phố Tatar Cổ. Toà nhà kiểu lâu đài lãng mạn cuối thế kỷ "
    "19 gắn với gia đình con trai của lãnh tụ Imam Shamil.",
    "Bảo tàng Văn học Gabdulla Tukay tôn vinh nhà thơ được coi là biểu tượng của văn học và ngôn "
    "ngữ Tatar hiện đại. Bảo tàng đặt trong 'Nhà Shamil' — một dinh thự hai tầng lộng lẫy ở khu phố "
    "Tatar Cổ, xây cuối thế kỷ 19 cho thương gia giàu có Ibragim Apakov. Sau khi con gái ông kết hôn "
    "với Muhammad-Shafi Shamil (con trai của Imam Shamil, lãnh tụ kháng chiến vùng Kavkaz), toà nhà "
    "được dùng làm của hồi môn và từ đó dân gian quen gọi là 'Nhà Shamil'. Với đường nét kiểu lâu "
    "đài lãng mạn – phương Đông, tháp góc và trang trí tinh tế, bản thân toà nhà đã là một di tích "
    "kiến trúc đáng ngắm. Bảo tàng Tukay mở cửa năm 1986 nhân 100 năm ngày sinh nhà thơ, là chi "
    "nhánh của Bảo tàng Quốc gia Tatarstan. Các phòng trưng bày bản thảo, sách, ảnh, đồ dùng và tái "
    "hiện không gian sống, giúp khách hiểu cuộc đời ngắn ngủi (1886–1913) nhưng rực rỡ của Tukay và "
    "bối cảnh văn hoá Tatar đầu thế kỷ 20. Nằm giữa khu phố Tatar Cổ bên hồ Kaban, bảo tàng rất tiện "
    "kết hợp dạo bộ ngắm những ngôi nhà gỗ, nhà thờ Hồi giáo cổ và không khí truyền thống của cộng "
    "đồng Tatar tại Kazan.",
    [
        "Đặt trong 'Nhà Shamil' — dinh thự kiểu lâu đài cuối thế kỷ 19, một di tích kiến trúc đẹp.",
        "Tôn vinh Gabdulla Tukay, nhà thơ dân tộc biểu tượng của người Tatar.",
        "Nằm giữa khu phố Tatar Cổ, tiện kết hợp dạo bộ ngắm nhà gỗ và nhà thờ Hồi giáo cổ.",
    ],
    {
        "hours_vi": "Mở hầu hết các ngày (thường nghỉ Thứ Hai), khoảng 10:00–18:00.",
        "ticket_vi": "Có bán vé vào cửa; giá phải chăng.",
        "duration_vi": "Khoảng 45 phút.",
        "best_time_vi": "Quanh năm; đẹp khi kết hợp dạo khu phố Tatar Cổ và hồ Kaban.",
        "tips_vi": "Nằm gần nhà thờ Hồi giáo Al-Marjani và hồ Kaban; kết hợp lộ trình Staro-Tatarskaya Sloboda.",
    },
    [
        {"title": "tourister.ru — Музей Габдуллы Тукая", "url": "https://www.tourister.ru/world/europe/russia/city/kazan/museum/25337"},
        {"title": "culture.ru — Литературный музей Габдуллы Тукая", "url": "https://www.culture.ru/institutes/22034/literaturnyi-muzei-gabdully-tukaya"},
    ],
    ["museum", "tukay", "shamil-house", "tatar-culture", "old-tatar-sloboda", "kazan"],
))

# 9) Hang động Yuryevskaya -----------------------------------------------------
RECORDS.append(rec(
    "yuryevskaya-cave",
    "Hang động Yuryevskaya (Yuryevskaya peshchera)",
    "Юрьевская пещера",
    "Yuryevskaya Cave",
    ["park_garden", "other"],
    55.232738, 49.233895,
    "Vùng núi Bogorodskoe, đông nam làng Tenishevo, huyện Kamsko-Ustyinsky, Tatarstan (bên sông Volga).",
    "Hang động thạch cao dài nhất vùng Volga và là hang nổi tiếng nhất Tatarstan, tổng chiều dài "
    "hơn 1 km. Được công nhận là di tích thiên nhiên cấp vùng từ 1986, đây là điểm đến ưa thích của "
    "dân thám hiểm hang động và du khách ưa mạo hiểm.",
    "Hang động Yuryevskaya nằm trong dãy núi Bogorodskoe ở huyện Kamsko-Ustyinsky, khu vực hữu ngạn "
    "sông Volga phía nam Tatarstan — vùng nổi tiếng với các mỏ thạch cao và cảnh quan đá vôi. Đây là "
    "hang karst – thạch cao dài nhất vùng Volga, được khảo sát lần đầu năm 1953; đến năm 1971, các "
    "nhà thám hiểm hang động Kazan dịch chuyển một đống đá lấp và mở thông sang phần hang mới dài hơn "
    "360 m, nâng tổng chiều dài các tuyến lên khoảng 1.005 m. Bên trong là hệ thống hành lang, ngách "
    "và 'phòng' nối nhau, có chỗ phải bò qua khe hẹp, có chỗ mở rộng thành sảnh với nhũ đá và tinh "
    "thể thạch cao; nhiệt độ trong hang mát lạnh quanh năm. Từ năm 1986, hang được xếp hạng di tích "
    "thiên nhiên cấp vùng. Ngày nay Yuryevskaya là điểm đến quen thuộc của các nhóm thám hiểm hang "
    "động (speleo) và tour mạo hiểm khởi hành từ Kazan; khu vực quanh hang, bên bờ Volga rộng lớn, "
    "cũng có phong cảnh đẹp. Do lối vào và di chuyển trong hang cần bò trườn và trang bị phù hợp, "
    "đây là trải nghiệm hợp với người có sức khoẻ và nên đi cùng hướng dẫn viên.",
    [
        "Hang thạch cao dài nhất vùng Volga (hơn 1 km) — hang nổi tiếng nhất Tatarstan.",
        "Di tích thiên nhiên cấp vùng từ 1986; điểm đến ưa thích của dân thám hiểm hang động.",
        "Nằm bên hữu ngạn sông Volga, phong cảnh quanh vùng Kamsko-Ustyinsky rất đẹp.",
    ],
    {
        "hours_vi": "Không có giờ cố định; nên đi theo tour/hướng dẫn viên, chủ yếu mùa khô ấm.",
        "ticket_vi": "Vào tự do nếu tự đi; tour thám hiểm có phí (kèm đèn, mũ bảo hộ).",
        "duration_vi": "Nửa ngày cả di chuyển; trong hang 1–2 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; tránh sau mưa lớn vì lối vào trơn.",
        "tips_vi": "Mang đèn pin/đèn đội đầu, quần áo bẩn được, giày bám tốt; nên có người dẫn quen hang.",
    },
    [
        {"title": "Wikipedia (RU) — Юрьевская пещера (toạ độ)", "url": "https://ru.wikipedia.org/wiki/%D0%AE%D1%80%D1%8C%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D0%BF%D0%B5%D1%89%D0%B5%D1%80%D0%B0"},
        {"title": "visit-tatarstan.com — Юрьевская пещера", "url": "https://visit-tatarstan.com/places/camping/yurjevskaya_peshhera/"},
    ],
    ["cave", "nature", "speleology", "volga", "adventure", "kamskoye-ustye"],
    maps=maps_for("Юрьевская пещера", "Yuryevskaya Cave", "Камское Устье", "Kamskoye Ustye", 55.232738, 49.233895),
))

# 10) Núi Lobach ---------------------------------------------------------------
RECORDS.append(rec(
    "lobach-mountain",
    "Núi Lobach và cửa sông Kama (Gora Lobach)",
    "Гора Лобач",
    "Mount Lobach",
    ["park_garden"],
    55.200817, 49.298285,
    "Đông nam thị trấn Kamskoye Ustye, hữu ngạn sông Volga, đối diện nơi Kama hợp lưu, Tatarstan.",
    "Ngọn núi – khu bảo tồn cảnh quan cao khoảng 136 m bên hữu ngạn Volga, ngay đối diện nơi sông "
    "Kama đổ vào Volga. Điểm ngắm toàn cảnh ngoạn mục bậc nhất Tatarstan, kết hợp giá trị cảnh quan, "
    "lịch sử và địa chất.",
    "Núi Lobach là một khối núi sót (ostanets) cao khoảng 136 m nằm ở đông nam thị trấn Kamskoye "
    "Ustye, trên hữu ngạn sông Volga — ngay đối diện điểm hợp lưu hùng vĩ nơi sông Kama đổ vào Volga. "
    "Từ năm 1991, khu vực rộng khoảng 241 ha quanh núi được lập thành khu bảo tồn cảnh quan (zakaznik) "
    "nhằm bảo vệ hệ thực vật thảo nguyên đá vôi quý và các thắng cảnh. Đứng trên đỉnh Lobach, du "
    "khách có tầm nhìn toàn cảnh mênh mông xuống 'biển' Volga (hồ chứa Kuybyshev) mở rộng nơi hai "
    "dòng sông gặp nhau — cảnh tượng được xem là một trong những panorama đẹp nhất Tatarstan, đặc "
    "biệt vào lúc bình minh và hoàng hôn. Ngọn núi còn mang dấu tích khảo cổ và gắn với nhiều truyền "
    "thuyết địa phương (các tên gọi khác như Obach, Aygyr-tau), cùng những vách đá vôi lộ ra tầng "
    "địa chất cổ. Đây là điểm dã ngoại, chụp ảnh và ngắm cảnh yêu thích, thường kết hợp cùng hang "
    "Yuryevskaya và cụm mỏ thạch cao trong cùng huyện Kamsko-Ustyinsky. Đường lên là đường mòn tự "
    "nhiên, phù hợp cho những ai thích đi bộ đường dài nhẹ nhàng.",
    [
        "Núi cao ~136 m bên Volga, đối diện nơi sông Kama hợp lưu — panorama đẹp bậc nhất Tatarstan.",
        "Khu bảo tồn cảnh quan (zakaznik) từ 1991, có hệ thực vật thảo nguyên đá vôi quý.",
        "Điểm dã ngoại – ngắm bình minh/hoàng hôn, tiện ghép với hang Yuryevskaya.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do ban ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 1–2 giờ kể cả leo lên đỉnh.",
        "best_time_vi": "Cuối xuân đến đầu thu; đẹp nhất bình minh và hoàng hôn, ngày trời quang.",
        "tips_vi": "Đi giày bám tốt, mang nước và mũ; gió mạnh trên đỉnh, cẩn thận sát mép vách đá.",
    },
    [
        {"title": "Wikipedia (RU) — Лобач (гора)", "url": "https://ru.wikipedia.org/wiki/%D0%9B%D0%BE%D0%B1%D0%B0%D1%87_(%D0%B3%D0%BE%D1%80%D0%B0)"},
        {"title": "tourister.ru — Гора Лобач в Камском Устье (toạ độ)", "url": "https://www.tourister.ru/world/europe/russia/city/kamskoye-ustye/mount/38261"},
    ],
    ["nature", "mountain", "viewpoint", "volga", "kama", "kamskoye-ustye"],
    maps=maps_for("Гора Лобач", "Mount Lobach", "Камское Устье", "Kamskoye Ustye", 55.200817, 49.298285),
))

# 11) Tu viện Makaryevskaya Pustyn ---------------------------------------------
RECORDS.append(rec(
    "makaryevsky-hermitage",
    "Tu viện Makaryevskaya (Sviyazhskaya Makaryevskaya pustyn)",
    "Свияжская Макарьевская пустынь",
    "Makaryevsky Hermitage",
    ["church"],
    55.782290, 48.702912,
    "Làng Vvedenskaya Sloboda, huyện Verkhneuslonsky, hữu ngạn sông Volga, gần đảo Sviyazhsk.",
    "Tu viện Chính thống giáo tuyệt đẹp nằm nép bên chân đồi rừng trên hữu ngạn sông Volga, đối "
    "diện đảo–thị trấn Sviyazhsk. Khung cảnh sông nước – rừng núi thanh bình khiến đây là một trong "
    "những tu viện 'ăn ảnh' và tĩnh lặng nhất vùng.",
    "Tu viện Makaryevskaya (Makaryevskaya pustyn) nằm ở làng Vvedenskaya Sloboda thuộc huyện "
    "Verkhneuslonsky, trên hữu ngạn sông Volga và cách đảo–thị trấn Sviyazhsk chỉ khoảng 1,5 km "
    "theo đường sông. Tu viện được lập vào nửa đầu thế kỷ 17 bởi tu sĩ khổ hạnh Isaia, người từ tu "
    "viện Makaryevsky-Unzhensky tới đây ẩn tu, và được đặt theo tên Thánh Makary xứ Unzha. Vị trí "
    "của tu viện đặc biệt nên thơ: các nhà thờ và nhà tu với mái vòm sáng màu nằm trên một dải đất "
    "hẹp giữa mặt nước Volga mênh mông và sườn đồi phủ rừng dựng đứng phía sau, tạo nên khung cảnh "
    "gần như tách biệt khỏi thế giới. Tu viện bị đóng cửa năm 1922 dưới thời Xô-viết và xuống cấp, "
    "rồi được hồi sinh từ năm 1996; các công trình dần được trùng tu và đời sống tu trì được khôi "
    "phục. Ngày nay đây là điểm hành hương và tham quan yên tĩnh, thường được ghé thăm kết hợp với "
    "Sviyazhsk — có thể tới bằng đường bộ hoặc bằng tàu/thuyền trên sông Volga trong mùa nước. Với "
    "khách du lịch, sức hấp dẫn nằm ở sự tĩnh lặng, kiến trúc mộc mạc và toàn cảnh sông nước tuyệt đẹp.",
    [
        "Tu viện thế kỷ 17 nằm giữa mặt nước Volga và sườn đồi rừng — khung cảnh thanh bình, nên thơ.",
        "Chỉ cách đảo–thị trấn Sviyazhsk khoảng 1,5 km, dễ kết hợp tham quan.",
        "Được hồi sinh từ 1996 sau thời gian dài đóng cửa; điểm hành hương yên tĩnh.",
    ],
    {
        "hours_vi": "Mở đón khách ban ngày, có giờ lễ; là tu viện đang hoạt động.",
        "ticket_vi": "Vào cửa tự do; hoan nghênh quyên góp.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; mùa nước có thể đi thuyền từ Sviyazhsk.",
        "tips_vi": "Ăn mặc kín đáo, nữ mang khăn trùm đầu; kết hợp cùng chuyến thăm Sviyazhsk.",
    },
    [
        {"title": "Wikipedia (RU) — Свияжская Макарьевская пустынь", "url": "https://ru.wikipedia.org/wiki/%D0%A1%D0%B2%D0%B8%D1%8F%D0%B6%D1%81%D0%BA%D0%B0%D1%8F_%D0%9C%D0%B0%D0%BA%D0%B0%D1%80%D1%8C%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%BD%D1%8C"},
        {"title": "sobory.ru — Макарьевская пустынь (toạ độ)", "url": "https://sobory.ru/article/?object=02903"},
    ],
    ["church", "monastery", "volga", "sviyazhsk", "pilgrimage", "verkhneuslonsky"],
    maps=maps_for("Макарьевская пустынь", "Makaryevsky Hermitage", "Верхнеуслонский район", "Verkhneuslonsky District", 55.782290, 48.702912),
))

# 12) Tu viện Sedmiozyornaya Pustyn --------------------------------------------
RECORDS.append(rec(
    "sedmiozerny-monastery",
    "Tu viện Bảy Hồ – Sedmiozyornaya Bogoroditskaya pustyn",
    "Седмиозёрная Богородицкая пустынь",
    "Sedmiozerny (Seven Lakes) Bogoroditsky Hermitage",
    ["church"],
    55.954157, 49.101552,
    "Làng Semiozyorka, huyện Vysokogorsky, cách Kazan khoảng 17 km về phía bắc, Tatarstan.",
    "Tu viện hành hương nổi tiếng gần Kazan, lập từ đầu thế kỷ 17, gắn với icon linh thiêng 'Đức Mẹ "
    "Smolensk – Sedmiozyornaya'. Không gian thanh tịnh giữa rừng và đồng quê, là điểm đến tâm linh "
    "quan trọng của vùng.",
    "Tu viện Sedmiozyornaya (nghĩa là 'Bảy Hồ') nằm ở làng Semiozyorka thuộc huyện Vysokogorsky, "
    "cách trung tâm Kazan khoảng 17 km về phía bắc. Theo truyền thống, năm 1615 tu sĩ khổ hạnh "
    "Yevfimy tới ẩn tu ở vùng đất hoang vắng nhiều hồ nước này, và đến năm 1627 tu viện chính thức "
    "được thành lập. Trong nhiều thế kỷ, Sedmiozyornaya là một trong những trung tâm hành hương lớn "
    "nhất vùng Kazan, nổi tiếng nhờ báu vật là icon 'Đức Mẹ Smolensk – Sedmiozyornaya' được tôn "
    "kính vì gắn với nhiều sự tích cứu thành phố khỏi dịch bệnh. Sau thời kỳ đóng cửa và tàn phá "
    "dưới chính quyền Xô-viết, tu viện được khôi phục từ cuối thế kỷ 20: các nhà thờ, nhà tu và "
    "nguồn nước thánh dần được phục dựng, đời sống tu trì trở lại. Ngày nay tu viện thu hút đông đảo "
    "khách hành hương và du khách tìm sự tĩnh lặng, đặc biệt vào các ngày lễ liên quan đến icon Đức "
    "Mẹ; khuôn viên rợp cây xanh giữa cảnh đồng quê – rừng thưa mang lại cảm giác thanh bình, tách "
    "biệt khỏi nhịp sống đô thị. Vị trí gần Kazan khiến đây là chuyến đi trong ngày dễ thực hiện.",
    [
        "Tu viện hành hương lập từ đầu thế kỷ 17, chỉ cách Kazan ~17 km.",
        "Gắn với icon linh thiêng 'Đức Mẹ Smolensk – Sedmiozyornaya'.",
        "Không gian thanh tịnh giữa rừng và đồng quê; có nguồn nước thánh.",
    ],
    {
        "hours_vi": "Mở đón khách ban ngày, có giờ lễ; là tu viện đang hoạt động.",
        "ticket_vi": "Vào cửa tự do; hoan nghênh quyên góp.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm; đông khách hành hương vào các ngày lễ Đức Mẹ.",
        "tips_vi": "Ăn mặc kín đáo, nữ mang khăn trùm đầu; đi taxi/xe riêng từ Kazan tiện nhất.",
    },
    [
        {"title": "sobory.ru — Семиозёрка, Седмиозёрская Богородицкая пустынь", "url": "https://sobory.ru/article/?object=05121"},
        {"title": "2GIS Казань — Седмиозерная Богородицкая пустынь (toạ độ)", "url": "https://2gis.ru/kazan/geo/2956174450229338"},
    ],
    ["church", "monastery", "pilgrimage", "icon", "vysokogorsky", "kazan-area"],
    maps=maps_for("Седмиозёрная Богородицкая пустынь", "Sedmiozerny Monastery", "Семиозёрка", "Semiozerka", 55.954157, 49.101552),
))

# 13) Iske-Kazan (Kazan Cổ) ----------------------------------------------------
RECORDS.append(rec(
    "iske-kazan",
    "Khu bảo tồn Iske-Kazan (Kazan Cổ) – thành cổ Kamayevo",
    "Иске-Казанский музей-заповедник",
    "Iske-Kazan State Museum-Reserve (Old Kazan)",
    ["museum", "monument", "fortress"],
    56.02556, 49.65056,
    "Làng Kamayevo, huyện Vysokogorsky, bên sông Kazanka, cách Kazan khoảng 45 km, Tatarstan.",
    "Khu bảo tồn lịch sử – văn hoá – thiên nhiên trên nền 'Kazan Cổ' (Iske Kazan), nơi được nhiều "
    "nhà khoa học cho là tiền thân của thành phố Kazan trước khi dời về vị trí hiện nay. Gồm thành "
    "cổ Kamayevo, khu dân cư Russko-Urmatskoe và bảo tàng lịch sử – dân tộc học.",
    "Iske-Kazan (tiếng Tatar: 'Kazan Cổ') là khu bảo tồn nhà nước về lịch sử, văn hoá và thiên nhiên "
    "được lập năm 1992 quanh làng Kamayevo, huyện Vysokogorsky, bên bờ sông Kazanka, cách Kazan hiện "
    "nay khoảng 45 km. Theo giả thuyết được ủng hộ rộng rãi (gắn với nhà khảo cổ Ravil Fakhrutdinov), "
    "đây chính là nơi toạ lạc của một 'Kazan cũ' — một trung tâm chính trị, kinh tế quan trọng của "
    "vùng Zakazanye trong các thế kỷ 13–15, trước khi kinh đô hãn quốc Kazan dời về cửa sông "
    "Kazanka–Bulak nơi thành phố ngày nay đứng. Khu bảo tồn rộng khoảng 137 ha bao gồm: thành cổ "
    "Iske-Kazan (Kamayevskoe) — di chỉ pháo đài mũi đất bị quân Ivan Bạo chúa phá năm 1552; khu dân "
    "cư – thủ công Russko-Urmatskoe với lò gốm, lò luyện kim; các nghĩa địa cổ có bia đá; cùng cảnh "
    "quan tự nhiên của thung lũng sông Kazanka với hồ bãi bồi. Bảo tàng lịch sử – dân tộc học ở làng "
    "Kamayevo trưng bày hiện vật khảo cổ (khoá – chìa khoá đồng, cân tiểu ly, vũ khí, gốm, kho tiền "
    "bạc thời Kim Trướng), cùng đồ dân tộc học và cả những cổ vật quý như vạc đồng thời Hung Nô. Khu "
    "còn có 'những nơi thiêng' như mộ Gaysha-bike và các nguồn nước thánh. Đây là điểm đến giàu "
    "chiều sâu cho người quan tâm lịch sử Tatar và Volga Bulgar, thường được xếp cùng Bolgar, Bilyar "
    "và Sviyazhsk như một 'vành đai di sản' của Tatarstan.",
    [
        "Được xem là 'Kazan Cổ' — tiền thân của thành phố Kazan trước khi dời về vị trí hiện nay.",
        "Gồm thành cổ Kamayevo, khu thủ công Russko-Urmatskoe và bảo tàng lịch sử – dân tộc học.",
        "Thuộc 'vành đai di sản' Tatarstan cùng Bolgar, Bilyar và Sviyazhsk.",
    ],
    {
        "hours_vi": "Bảo tàng mở hầu hết các ngày (thường nghỉ đầu tuần); di chỉ ngoài trời thăm ban ngày.",
        "ticket_vi": "Có bán vé bảo tàng; tham quan di chỉ ngoài trời chủ yếu tự do.",
        "duration_vi": "Khoảng 1,5–2 giờ (chưa kể di chuyển).",
        "best_time_vi": "Cuối xuân đến đầu thu; đồng bãi ven Kazanka đẹp vào mùa ấm.",
        "tips_vi": "Cách Kazan ~45 km, nên đi xe riêng/taxi; kết hợp với các di sản Bolgar – Sviyazhsk nếu có thời gian.",
    },
    [
        {"title": "Wikipedia (RU) — Иске-Казань (toạ độ 56°01′32″N 49°39′02″E)", "url": "https://ru.wikipedia.org/wiki/%D0%98%D1%81%D0%BA%D0%B5-%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C"},
        {"title": "visit-tatarstan.com — Иске-Казанский музей-заповедник", "url": "https://visit-tatarstan.com/places/sightseeings/iske-kazanskiy-muzey-zapovednik/"},
    ],
    ["archaeology", "old-kazan", "gorodishche", "museum-reserve", "tatar-history", "vysokogorsky"],
    maps=maps_for("Иске-Казанский музей-заповедник", "Iske-Kazan Museum Reserve", "Камаево", "Kamayevo", 56.02556, 49.65056),
))

# 14) Thị trấn cổ Tetyushi -----------------------------------------------------
RECORDS.append(rec(
    "tetyushi",
    "Thị trấn cổ Tetyushi bên sông Volga",
    "Тетюши",
    "Tetyushi",
    ["square_street", "monument"],
    54.928018, 48.835958,
    "Thành phố Tetyushi, hữu ngạn cao của hồ chứa Kuybyshev (sông Volga), tây nam Tatarstan.",
    "Thị trấn thương mại cổ trên vách bờ cao sông Volga, được công nhận là đô thị lịch sử của Nga. "
    "Nổi tiếng với cầu thang dài hàng trăm bậc dẫn xuống bến sông, phố cổ thương gia và truyền "
    "thống đánh bắt cá tầm khổng lồ trên Volga.",
    "Tetyushi là một thị trấn nhỏ nằm trên bờ tây cao của hồ chứa Kuybyshev (sông Volga), ở phần "
    "tây nam Tatarstan thuộc vùng cao nguyên Volga. Pháo đài Tetyushi được dựng vào khoảng những năm "
    "1570 như một tiền đồn phòng thủ của nhà nước Nga; qua nhiều thế kỷ nơi đây phát triển thành một "
    "thị trấn thương mại sầm uất nhờ vị trí trên tuyến sông Volga, và ngày nay được xếp vào danh "
    "sách các đô thị lịch sử của Nga. Điểm nhận diện nổi bật nhất của Tetyushi là cầu thang dài "
    "hàng trăm bậc (thường nhắc tới con số hơn 360 bậc) nối khu phố trên vách cao xuống bến tàu bên "
    "mép nước — vừa là công trình tiện ích vừa là điểm ngắm toàn cảnh Volga rộng như biển. Khu "
    "trung tâm còn giữ nhiều ngôi nhà thương gia, nhà thờ và công trình từ thế kỷ 19 – đầu 20, mang "
    "không khí tỉnh lỵ Volga xưa. Thị trấn cũng gắn với truyền thống đánh bắt cá tầm (beluga) khổng "
    "lồ trên Volga — có đài kỷ niệm con cá tầm lớn từng bắt được, một chi tiết thú vị của văn hoá "
    "sông nước địa phương. Với du khách, Tetyushi là điểm dừng yên bình để cảm nhận cảnh quan Volga "
    "hùng vĩ, dạo phố cổ và thưởng thức không khí một thị trấn ven sông đậm chất Nga tỉnh lẻ.",
    [
        "Đô thị lịch sử của Nga trên vách bờ cao sông Volga, có từ thập niên 1570.",
        "Cầu thang dài hàng trăm bậc xuống bến sông — điểm ngắm toàn cảnh Volga nổi tiếng.",
        "Phố cổ thương gia thế kỷ 19 và truyền thống đánh bắt cá tầm khổng lồ trên Volga.",
    ],
    {
        "hours_vi": "Thị trấn tham quan tự do; bảo tàng địa phương mở theo giờ hành chính.",
        "ticket_vi": "Dạo phố miễn phí; bảo tàng có vé.",
        "duration_vi": "Nửa ngày (chưa kể di chuyển).",
        "best_time_vi": "Cuối xuân đến đầu thu; mùa hè có tàu du lịch trên Volga cập bến.",
        "tips_vi": "Cách Kazan khá xa về phía nam; đi xe riêng hoặc theo tour tàu sông. Đừng bỏ lỡ cầu thang xuống bến.",
    },
    [
        {"title": "Wikipedia (RU) — Тетюши (toạ độ)", "url": "https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%82%D1%8E%D1%88%D0%B8"},
        {"title": "cruiseinform.ru — Тетюши: город на Волге", "url": "https://cruiseinform.ru/catalog/07/071/tetyushi/"},
    ],
    ["historic-town", "volga", "staircase", "merchant-town", "sturgeon", "tetyushi"],
    maps=maps_for("Тетюши", "Tetyushi", "Татарстан", "Tatarstan", 54.928018, 48.835958),
))

# 15) Đài tưởng niệm – nhà thờ kim tự tháp cho binh sĩ tử trận 1552 -------------
RECORDS.append(rec(
    "fallen-soldiers-monument",
    "Đài tưởng niệm – nhà thờ hình kim tự tháp cho binh sĩ tử trận năm 1552",
    "Храм-памятник воинам, павшим при взятии Казани в 1552 году",
    "Temple-Monument to the Soldiers Fallen at the Capture of Kazan (1552)",
    ["monument", "church"],
    55.80097, 49.07746,
    "Trên đảo nhỏ giữa sông Kazanka, cạnh đê Kirovskaya (Kirovskaya damba), tây bắc Kremlin, Kazan.",
    "Đài tưởng niệm hình kim tự tháp cụt cao 20 m dựng đầu thế kỷ 19 để tưởng nhớ binh sĩ Nga tử "
    "trận khi chiếm Kazan năm 1552 — một trong những đài tưởng niệm quân sự cổ nhất nước Nga. Bên "
    "trong là một nhà thờ nhỏ; công trình nổi bật cô độc giữa mặt nước sông Kazanka.",
    "Đài tưởng niệm này là một trong những công trình tưởng niệm quân sự lâu đời và khác thường nhất "
    "nước Nga. Được xây theo lệnh Hoàng đế Aleksandr I, theo thiết kế của kiến trúc sư Peterburg "
    "Nikolai Alfyorov (khánh thành khoảng năm 1823), đài có hình một kim tự tháp cụt bằng đá cao "
    "khoảng 20 m, mỗi mặt có một cổng vòm, xưa đỉnh gắn thánh giá mạ vàng. Bên trong là nhà thờ nhỏ "
    "kính Ảnh Chúa Không Do Tay Người Vẽ (Nerukotvorny Obraz) — nhắc tới lá cờ chiến của Sa hoàng "
    "khi vây thành; bốn góc từng có phòng cho các tu sĩ làm lễ cầu hồn cho binh sĩ tử trận. Dưới "
    "phần trung tâm là hầm mộ lưu giữ hài cốt những người lính Nga ngã xuống trong cuộc chiếm thành "
    "Kazan năm 1552. Công trình đứng trên một gò đất/đảo nhỏ nổi giữa dòng Kazanka, cách Kremlin "
    "khoảng 2 km về phía tây bắc, gắn với đê Kirovskaya bằng một lối đắp và cây cầu nhỏ. Silhouette "
    "kim tự tháp cô độc giữa mặt nước tạo nên một hình ảnh ấn tượng, dễ nhận ra khi đi qua khu vực "
    "cầu – đê nối trung tâm với quận Kirovsky. Đây là điểm dừng ngắn giàu ý nghĩa lịch sử, có thể "
    "ngắm và chụp ảnh khi kết hợp lộ trình quanh sông Kazanka.",
    [
        "Đài tưởng niệm quân sự hình kim tự tháp cụt cao 20 m, dựng đầu thế kỷ 19 — thuộc hàng cổ nhất nước Nga.",
        "Tưởng nhớ binh sĩ Nga tử trận khi chiếm Kazan năm 1552; bên dưới có hầm mộ.",
        "Đứng cô độc trên đảo nhỏ giữa sông Kazanka — hình ảnh độc đáo, dễ nhận ra.",
    ],
    {
        "hours_vi": "Ngắm bên ngoài tự do; bên trong mở hạn chế theo lịch nhà thờ.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–20 phút.",
        "best_time_vi": "Mùa ấm khi có thể đi bộ theo lối đắp ra gần đài; đẹp lúc nắng chiều.",
        "tips_vi": "Tiếp cận từ phía đê Kirovskaya; kết hợp ngắm cảnh sông Kazanka và Kremlin từ xa.",
    },
    [
        {"title": "Wikipedia (RU) — Храм-памятник воинам, павшим при взятии Казани в 1552 году", "url": "https://ru.wikipedia.org/wiki/%D0%A5%D1%80%D0%B0%D0%BC-%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D0%BD%D0%B8%D0%BA_%D0%B2%D0%BE%D0%B8%D0%BD%D0%B0%D0%BC,_%D0%BF%D0%B0%D0%B2%D1%88%D0%B8%D0%BC_%D0%BF%D1%80%D0%B8_%D0%B2%D0%B7%D1%8F%D1%82%D0%B8%D0%B8_%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8_%D0%B2_1552_%D0%B3%D0%BE%D0%B4%D1%83"},
        {"title": "2GIS Казань — Храм-памятник павшим воинам (toạ độ)", "url": "https://2gis.ru/kazan/firm/2956016536684364"},
    ],
    ["monument", "memorial", "pyramid", "1552", "kazanka", "kazan"],
))


PLAN = {"tatarstan.json": RECORDS}


def main():
    total_added = 0
    for fname, recs in PLAN.items():
        path = os.path.join(REGIONS, fname)
        arr = json.load(open(path, encoding="utf-8"))
        existing_slugs = {p.get("slug") for p in arr}
        existing_ids = {p.get("id") for p in arr}
        to_add = []
        for r in recs:
            if r["slug"] in existing_slugs or r["id"] in existing_ids:
                print(f"  = BO QUA (da co): {fname} :: {r['slug']}")
                continue
            to_add.append(r)
        if not to_add:
            print(f"  (khong co gi de them cho {fname})")
            continue
        bak = path + f".bak_add_{TS}"
        with open(bak, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        arr.extend(to_add)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        total_added += len(to_add)
        print(f"  + {fname}: them {len(to_add)} dia diem -> tong {len(arr)} (backup: {os.path.basename(bak)})")
        for r in to_add:
            print(f"        - {r['name_vi']}  [{','.join(r['categories'])}]  ({r['coordinates']['lat']},{r['coordinates']['lon']})")

    print(f"\nTong da them lan nay: {total_added} dia diem.")


if __name__ == "__main__":
    main()
