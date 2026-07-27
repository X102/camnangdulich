# -*- coding: utf-8 -*-
"""_add_places_tatarstan_extra_20260727.py — Bổ sung THÊM cho VÙNG TIÊU ĐIỂM: Tatarstan.

Lần chạy tự động 2026-07-27 (buổi sáng). GHI CHÚ QUAN TRỌNG:
Một lần chạy SONG SONG khác của cùng tác vụ đã nâng tatarstan.json từ 10 -> 26 địa điểm
(script tools/_add_places_tatarstan_20260727.py + backup tatarstan.json.bak_add_20260727_044942).
Để TRÁNH TRÙNG, script này CHỈ thêm những địa điểm THẬT SỰ nổi tiếng còn THIẾU mà lần chạy kia
CHƯA đưa vào (đối chiếu 26 slug hiện có, và đối chiếu cả theo đối tượng thực tế, không chỉ theo slug).

7 địa điểm bổ sung (đều CHƯA có, đa dạng loại hình):
  1) Bảo tàng Mỹ thuật Tatarstan (Feshin/Shishkin)      — museum
  2) Rạp xiếc Kazan (toà 'đĩa bay' 1967)                 — other/monument
  3) Khu nghỉ dưỡng & công viên nước Kazan Riviera       — other
  4) Tu viện Zilantov (đồi Rồng Zilant, gắn quốc huy)    — church
  5) Tu viện Thánh Gioan Tiền Hô (đối diện Kremlin)      — church
  6) Rừng - công viên Gorkinsko-Ometyevo (eco-park 2016) — park_garden
  7) Vườn thú Kazan 'Sông Zambezi' (mới, 2021)           — other/park_garden

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch nguyên văn), có ghi nguồn.
Toạ độ THẬT — xác minh chéo openarium.ru (thẻ POI có 'Координаты'), 2GIS org-card / URL chỉ đường
(dạng |lon,lat), Wikipedia, các trang du lịch — 2026-07. Kiểm tra thứ tự: lat 55,76–55,82 (∈41–70),
lon 49,05–49,21 (∈19–180), KHÔNG đảo, đều nằm trong Tatarstan.
Link bản đồ TRỎ-ĐỊA-ĐIỂM; nơi có URL trang tổ chức Yandex thì ưu tiên dùng.

Chạy:  python3 tools/_add_places_tatarstan_extra_20260727.py
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

# 1) Bảo tàng Mỹ thuật Tatarstan ----------------------------------------------
RECORDS.append(rec(
    "fine-arts-museum-tatarstan",
    "Bảo tàng Mỹ thuật Cộng hoà Tatarstan (Muzey izobrazitelnykh iskusstv RT)",
    "Государственный музей изобразительных искусств Республики Татарстан",
    "State Museum of Fine Arts of the Republic of Tatarstan",
    ["museum"],
    55.79485, 49.13440,
    "Phố Karla Marksa, số 64, trung tâm Kazan (trong dinh thự đầu thế kỷ 20).",
    "Một trong những bảo tàng mỹ thuật lớn của Nga, đặt trong toà dinh thự sang trọng đầu thế kỷ "
    "20 từng là dinh tư lệnh Quân khu Kazan. Nổi tiếng với bộ sưu tập tranh Nikolai Feshin lớn "
    "nhất nước Nga và nhiều tác phẩm của danh hoạ phong cảnh Ivan Shishkin — người con Tatarstan.",
    "Thành lập năm 1958 trên cơ sở phòng tranh của Bảo tàng Quốc gia Tatarstan, bảo tàng Mỹ thuật "
    "nhanh chóng trở thành một trong những bộ sưu tập nghệ thuật lớn của nước Nga. Từ năm 1967, "
    "bảo tàng chuyển về toà dinh thự lộng lẫy xây đầu thế kỷ 20 vốn là dinh của tư lệnh Quân khu "
    "Kazan — bản thân toà nhà và khu vườn đã là một điểm ngắm. Kho tàng khoảng 25.000 hiện vật "
    "gồm hội hoạ, đồ hoạ, điêu khắc và mỹ thuật ứng dụng. Điểm tự hào lớn nhất là bộ sưu tập tranh "
    "Nikolai Feshin lớn nhất nước Nga — hoạ sĩ chân dung tài hoa sinh tại Kazan, cùng bộ sưu tập "
    "phong phú tranh và ký hoạ của Ivan Shishkin, bậc thầy phong cảnh Nga quê ở Yelabuga thuộc "
    "Tatarstan. Ngoài ra còn có icon Nga cổ thế kỷ 16, tranh khắc châu Âu thế kỷ 15–16 (kể cả tác "
    "phẩm của Albrecht Dürer) và mảng nghệ thuật tiên phong Nga đầu thế kỷ 20. Đây là điểm đến "
    "không thể bỏ qua với người yêu hội hoạ khi tới Kazan.",
    [
        "Bộ sưu tập tranh Nikolai Feshin lớn nhất nước Nga cùng nhiều tác phẩm của Ivan Shishkin.",
        "Đặt trong dinh thự đầu thế kỷ 20 với khu vườn đẹp — bản thân toà nhà là một điểm ngắm.",
        "Có icon Nga cổ và tranh khắc châu Âu thế kỷ 15–16, gồm cả tác phẩm Albrecht Dürer.",
    ],
    {
        "hours_vi": "Mở cửa hầu hết các ngày (thường nghỉ Thứ Hai); giờ khoảng 10:00–18:00 — kiểm tra trước.",
        "ticket_vi": "Có bán vé vào cửa và vé các triển lãm đặc biệt.",
        "duration_vi": "Khoảng 1,5 giờ.",
        "best_time_vi": "Quanh năm; mùa hè có thể dạo thêm khu vườn của dinh thự.",
        "tips_vi": "Cách phố Bauman/Kremlin một quãng đi bộ dọc phố Karla Marksa nhiều dinh thự cổ đẹp.",
    },
    [
        {"title": "openarium.ru — Государственный музей изобразительных искусств РТ", "url": "https://openarium.ru/poi/66093247/"},
        {"title": "Trang chính thức — izo-museum.ru", "url": "https://izo-museum.ru/"},
    ],
    ["museum", "fine-arts", "feshin", "shishkin", "art", "kazan"],
    official_site="https://izo-museum.ru/",
))

# 2) Rạp xiếc Kazan ------------------------------------------------------------
RECORDS.append(rec(
    "kazan-circus",
    "Rạp xiếc Nhà nước Kazan (Kazanskiy gosudarstvennyy tsirk)",
    "Казанский государственный цирк",
    "Kazan State Circus",
    ["other", "monument"],
    55.79876, 49.10060,
    "Quảng trường Tysyacheletiya (Nghìn năm), số 2, bên sông Kazanka, dưới chân đồi Kremlin, Kazan.",
    "Toà rạp xiếc hình 'đĩa bay' khánh thành năm 1967 — công trình bê tông vỏ mỏng táo bạo từng "
    "được ví như 'kiến trúc thế kỷ 21' và đi vào giáo trình kiến trúc. Nằm ngay dưới chân Kremlin "
    "bên sông Kazanka, đây là một biểu tượng hiện đại dễ nhận ra của Kazan.",
    "Rạp xiếc Kazan là một trong những công trình hiện đại mang tính biểu tượng nhất thành phố. "
    "Lịch sử xiếc ở Kazan đã hơn một thế kỷ, từ rạp xiếc cố định đầu tiên của anh em nhà Nikitin "
    "cuối thế kỷ 19. Toà rạp hiện nay khánh thành năm 1967 với hình dáng một chiếc 'đĩa bay' khổng "
    "lồ: đó là một trong những công trình vỏ bê tông mỏng dạng đĩa đầu tiên ở Liên Xô, mái vòm "
    "nhịp lớn không cần cột chống bên trong — một kỳ tích kết cấu ở thời điểm đó, đến mức được đưa "
    "vào giáo trình kiến trúc và gọi là 'toà nhà của thế kỷ 21'. Nằm trên Quảng trường Nghìn năm "
    "bên sông Kazanka, ngay dưới chân đồi Kremlin và gần Trung tâm Văn hoá Dân tộc, silhouette vũ "
    "trụ của rạp xiếc đã trở thành một phần không thể tách rời của cảnh quan trung tâm. Bên trong "
    "vẫn diễn xiếc đều đặn, hấp dẫn cả gia đình có trẻ nhỏ. Dù có xem suất diễn hay không, đây vẫn "
    "là một điểm ngắm và chụp ảnh thú vị khi dạo kè Kremlin.",
    [
        "Kiến trúc 'đĩa bay' năm 1967 — vỏ bê tông mỏng táo bạo, đi vào giáo trình kiến trúc.",
        "Biểu tượng hiện đại của Kazan, ngay dưới chân Kremlin bên sông Kazanka.",
        "Suất diễn xiếc đều đặn, phù hợp cho gia đình có trẻ em.",
    ],
    {
        "hours_vi": "Theo lịch biểu diễn (thường cuối tuần); phòng vé mở khoảng 9:00–18:30.",
        "ticket_vi": "Mua vé theo suất diễn; giá tuỳ chương trình và vị trí.",
        "duration_vi": "Một suất khoảng 2 giờ; ngắm bên ngoài 15 phút.",
        "best_time_vi": "Quanh năm; tiện ghép với dạo kè Kremlin và ngắm Kremlin từ xa.",
        "tips_vi": "Vị trí sát Kremlin và kè Kazanka nên dễ kết hợp; kiểm tra lịch diễn trước khi tới.",
    },
    [
        {"title": "Wikipedia (RU) — Казанский государственный цирк", "url": "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D1%86%D0%B8%D1%80%D0%BA"},
        {"title": "openarium.ru — Казанский государственный цирк (toạ độ)", "url": "https://openarium.ru/poi/53933736/"},
    ],
    ["circus", "modern-architecture", "flying-saucer", "family", "kazan"],
))

# 3) Kazan Riviera ------------------------------------------------------------
RECORDS.append(rec(
    "kazan-riviera",
    "Khu nghỉ dưỡng và Công viên nước Kazan Riviera (Kazanskaya Rivyera)",
    "Казанская Ривьера",
    "Kazan Riviera Resort & Aquapark",
    ["other"],
    55.815283, 49.131331,
    "Phố Fatykha Amirkhana, số 1, tả ngạn sông Kazanka, quận Novo-Savinovsky, Kazan.",
    "Tổ hợp giải trí – nghỉ dưỡng lớn bên sông Kazanka với công viên nước trong nhà mở quanh năm, "
    "khách sạn, bãi tắm mùa hè và vòng đu quay khổng lồ. Điểm vui chơi hiện đại được yêu thích, "
    "đặc biệt hợp với gia đình và những ngày mưa lạnh.",
    "Kazan Riviera là một trong những tổ hợp giải trí – nghỉ dưỡng hiện đại nổi tiếng nhất thành "
    "phố, nằm bên tả ngạn sông Kazanka, nhìn sang trung tâm lịch sử. Trái tim của tổ hợp là công "
    "viên nước (aquapark) trong nhà quy mô lớn với hệ thống cầu trượt, dòng sông lười, sóng nhân "
    "tạo và khu riêng cho trẻ em — mở cửa quanh năm bất kể thời tiết, nên rất hợp cho những ngày "
    "Kazan mưa hoặc mùa đông giá lạnh. Bên cạnh đó là khách sạn, khu spa, bãi tắm ngoài trời mùa "
    "hè bên sông và một vòng đu quay lớn cho tầm nhìn toàn cảnh thành phố. Tuy không phải di tích "
    "lịch sử, Kazan Riviera lại là minh chứng cho diện mạo Kazan năng động, hiện đại và là lựa "
    "chọn thư giãn – giải trí lý tưởng để cân bằng với hành trình tham quan đền đài, bảo tàng. Với "
    "các gia đình đi cùng trẻ nhỏ, đây thường là điểm được mong chờ nhất trong chuyến đi.",
    [
        "Công viên nước trong nhà lớn, mở quanh năm — cứu cánh cho ngày mưa và mùa đông.",
        "Tổ hợp gồm khách sạn, spa, bãi tắm mùa hè bên sông và vòng đu quay ngắm toàn cảnh.",
        "Điểm giải trí hiện đại rất hợp cho gia đình có trẻ em.",
    ],
    {
        "hours_vi": "Công viên nước mở hằng ngày, thường 10:00–22:00 (kiểm tra lịch theo mùa).",
        "ticket_vi": "Bán vé theo giờ/suất cho công viên nước; đu quay và các dịch vụ tính phí riêng.",
        "duration_vi": "Nửa ngày trở lên nếu chơi công viên nước.",
        "best_time_vi": "Quanh năm với khu trong nhà; bãi tắm ngoài trời đẹp vào mùa hè.",
        "tips_vi": "Mang theo đồ bơi; cuối tuần khá đông, nên đi sớm. Có thể ngắm hoàng hôn trên sông Kazanka.",
    },
    [
        {"title": "Yandex Maps — Ривьера, аквапарк (trang tổ chức)", "url": "https://yandex.com/maps/org/rivyera/1369600486/"},
        {"title": "2GIS Казань — Ривьера, аквапарк (toạ độ)", "url": "https://2gis.ru/kazan/firm/2956015537026021"},
    ],
    ["aquapark", "resort", "modern", "family", "kazanka", "kazan"],
    maps={
        "yandex": "https://yandex.com/maps/org/rivyera/1369600486/",
        "google": "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote("Kazan Riviera Aquapark, Kazan, Russia"),
    },
))

# 4) Tu viện Zilantov ----------------------------------------------------------
RECORDS.append(rec(
    "zilantov-monastery",
    "Tu viện Zilantov Uspensky (Svyato-Uspenskiy Zilantov monastyr)",
    "Свято-Успенский Зилантов монастырь",
    "Zilantov Assumption Monastery",
    ["church"],
    55.80796, 49.05847,
    "Đồi Zilant (Zilantova gora), phố Arkhangelskiy, tây bắc Kazan, gần sông Volga và tuyến đường sắt.",
    "Tu viện Chính thống giáo cổ nằm trên đồi Zilant — ngọn đồi gắn với truyền thuyết con rồng "
    "Zilant, biểu tượng trên quốc huy thành phố Kazan. Được lập từ năm 1552, tu viện với các mái "
    "vòm xanh nổi bật khi nhìn từ sông Volga hay tuyến tàu hoả vào thành phố.",
    "Tu viện Zilantov là một trong những tu viện cổ và giàu truyền thuyết nhất Kazan. Được lập "
    "năm 1552 — năm quân đội Sa hoàng Ivan Bạo chúa chiếm Kazan — ban đầu tu viện nằm gần khu mộ "
    "tập thể của binh sĩ Nga tử trận, rồi năm 1559 được dời lên đồi Zilant để tránh ngập. Tên đồi "
    "'Zilant' (tiếng Tatar: Jilantau — 'đồi rắn/rồng') gắn với truyền thuyết về một con rồng "
    "khổng lồ từng ngự trên đồi; chính hình con rồng Zilant này về sau trở thành biểu tượng trung "
    "tâm trên quốc huy thành phố Kazan. Nhờ vị trí trên cao bên rìa tây bắc thành phố, quần thể "
    "tu viện với những mái vòm xanh và tháp chuông có thể được nhìn thấy rõ từ sông Volga cũng như "
    "từ tuyến đường sắt chạy ngang qua từ năm 1890. Sau khi bị tàn phá thời Xô-viết, tu viện được "
    "trao lại cho Giáo hội năm 1998 và trở thành một cộng đoàn nữ tu; nhà thờ Uspensky (Đức Mẹ "
    "Lên Trời) cùng nhiều công trình đã được phục dựng. Đây là điểm đến yên tĩnh, giàu chiều sâu "
    "lịch sử và huyền thoại, hơi tách khỏi trung tâm nên ít đông đúc.",
    [
        "Nằm trên đồi Zilant gắn truyền thuyết con rồng — biểu tượng trên quốc huy thành phố Kazan.",
        "Được lập từ năm 1552, một trong những tu viện cổ nhất Kazan.",
        "Quần thể mái vòm xanh nổi bật khi nhìn từ sông Volga hoặc tuyến tàu hoả vào thành phố.",
    ],
    {
        "hours_vi": "Mở đón khách ban ngày (khoảng 8:00–19:00), có giờ lễ; là cộng đoàn nữ tu.",
        "ticket_vi": "Vào cửa tự do; hoan nghênh quyên góp.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; cảnh nhìn từ đồi đẹp vào ngày trời quang.",
        "tips_vi": "Ăn mặc kín đáo, nữ mang khăn trùm đầu; nằm hơi xa trung tâm nên tiện đi taxi.",
    },
    [
        {"title": "openarium.ru — Свято-Успенский Зилантов монастырь (toạ độ)", "url": "https://openarium.ru/poi/38284139/"},
        {"title": "Wikipedia (RU) — Зилантов монастырь", "url": "https://ru.wikipedia.org/wiki/%D0%97%D0%B8%D0%BB%D0%B0%D0%BD%D1%82%D0%BE%D0%B2_%D0%BC%D0%BE%D0%BD%D0%B0%D1%81%D1%82%D1%8B%D1%80%D1%8C"},
    ],
    ["church", "monastery", "zilant", "dragon", "coat-of-arms", "kazan"],
))

# 5) Tu viện Thánh Gioan Tiền Hô ----------------------------------------------
RECORDS.append(rec(
    "ioanno-predtechensky-monastery",
    "Tu viện Thánh Gioan Tiền Hô (Ioanno-Predtechenskiy monastyr)",
    "Иоанно-Предтеченский монастырь",
    "St John the Baptist Monastery",
    ["church"],
    55.79479, 49.10754,
    "Phố Baumana, đầu phía bắc, ngay đối diện tháp Spasskaya của Kremlin, trung tâm Kazan.",
    "Tu viện nhỏ nhắn thế kỷ 17 với quần thể kiến trúc duyên dáng nằm ngay đối diện lối vào chính "
    "của Kremlin, ở đầu phố đi bộ Bauman. Một điểm dừng chân dễ chịu, gắn với thánh German xứ Kazan.",
    "Tu viện Thánh Gioan Tiền Hô có vị trí đắc địa bậc nhất: ngay đối diện tháp Spasskaya — cổng "
    "chính của Kremlin Kazan, ở đầu phía bắc phố đi bộ Bauman. Tu viện được xây trong các năm "
    "1649–1652; những công trình gỗ ban đầu bị hoả hoạn thiêu rụi rồi được dựng lại bằng đá theo "
    "phong cách kiến trúc Nga thế kỷ 17 với những mái vòm nhỏ và trang trí gạch tinh tế. Trải qua "
    "nhiều lần trùng tu, quần thể tu viện ngày nay được đưa vào danh mục di sản văn hoá của Nga. "
    "Thời Xô-viết, tu viện bị đóng cửa và một phần bị phá; đến năm 1992 mới được trả lại cho Giáo "
    "hội. Bên trong lưu giữ một số thánh tích, trong đó có di hài thánh German xứ Kazan cùng nhiều "
    "icon được tôn kính. Vì nằm ngay điểm khởi đầu tuyến tham quan Kremlin – phố Bauman, tu viện "
    "là nơi rất dễ ghé qua để chiêm ngưỡng một mẫu kiến trúc tu viện Nga cổ kính, thanh nhã giữa "
    "trung tâm sầm uất.",
    [
        "Vị trí đắc địa ngay đối diện cổng chính (tháp Spasskaya) của Kremlin Kazan.",
        "Quần thể kiến trúc tu viện Nga thế kỷ 17 duyên dáng, thuộc danh mục di sản.",
        "Lưu giữ di hài thánh German xứ Kazan và nhiều icon được tôn kính.",
    ],
    {
        "hours_vi": "Mở đón khách ban ngày (khoảng 7:00–19:00), có giờ lễ.",
        "ticket_vi": "Vào cửa tự do; hoan nghênh quyên góp.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; tiện ghé ngay trước hoặc sau khi tham quan Kremlin.",
        "tips_vi": "Ăn mặc kín đáo, nữ mang khăn trùm đầu; nằm đúng đầu phố Bauman nên rất dễ kết hợp lịch trình.",
    },
    [
        {"title": "openarium.ru — Иоанно-Предтеченский монастырь (toạ độ)", "url": "https://openarium.ru/poi/12351871/"},
        {"title": "Wikipedia (RU) — Иоанно-Предтеченский монастырь (Казань)", "url": "https://ru.wikipedia.org/wiki/%D0%98%D0%BE%D0%B0%D0%BD%D0%BD%D0%BE-%D0%9F%D1%80%D0%B5%D0%B4%D1%82%D0%B5%D1%87%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%BE%D0%BD%D0%B0%D1%81%D1%82%D1%8B%D1%80%D1%8C_(%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C)"},
    ],
    ["church", "monastery", "german-of-kazan", "bauman-street", "kazan"],
))

# 6) Rừng - công viên Gorkinsko-Ometyevo --------------------------------------
RECORDS.append(rec(
    "gorkinsko-ometyevo-forest",
    "Rừng - công viên Gorkinsko-Ometyevo (Gorkinsko-Ometyevskiy les)",
    "Горкинско-Ометьевский лес",
    "Gorkinsko-Ometyevo Forest Park",
    ["park_garden"],
    55.76156, 49.21366,
    "Đại lộ Pobedy (Chiến Thắng), số 69, quận Sovetsky, phía nam Kazan.",
    "Công viên rừng đô thị lớn nhất Kazan, cải tạo và mở cửa năm 2016 trên hai cánh rừng thành "
    "phố. Không gian xanh hiện đại rất được yêu thích với đường dạo, làn xe đạp, sân chơi, mùa "
    "đông có đường trượt tuyết — biểu tượng cho xu hướng công viên công cộng mới của Kazan.",
    "Gorkinsko-Ometyevo là công viên rừng đô thị lớn nhất Kazan, hình thành từ hai cánh rừng "
    "thành phố (rừng Gorkinsky ở phía nam và rừng Ometyevsky ở phía bắc) được cải tạo thành một "
    "công viên hiện đại, khánh thành cuối năm 2016. Dự án nổi tiếng vì đã cứu một mảng rừng quý "
    "khỏi bị xây dựng và biến nó thành không gian công cộng kiểu mẫu, giành nhiều giải thưởng quy "
    "hoạch. Công viên có hệ thống lối đi dạo và cầu gỗ len giữa rừng, làn xe đạp và trượt patin, "
    "sân chơi trẻ em sáng tạo, sân khấu ngoài trời, khu tập thể thao, quán cà phê và cả 'công viên "
    "dây' mạo hiểm; mùa đông biến thành nơi trượt tuyết băng đồng và trượt tuyết xuống dốc. Đây là "
    "điểm đến quen thuộc của người dân Kazan để chạy bộ, đạp xe, dã ngoại và cho trẻ vui chơi — "
    "một 'lá phổi xanh' và cũng là ví dụ tiêu biểu cho làn sóng đổi mới không gian công cộng đô "
    "thị ở Tatarstan. Với du khách muốn cảm nhận nhịp sống thường ngày và mảng xanh của Kazan hiện "
    "đại, đây là một lựa chọn thư giãn thú vị ngoài các di tích cổ.",
    [
        "Công viên rừng đô thị lớn nhất Kazan, mở cửa 2016, từng giành giải thưởng quy hoạch.",
        "Đường dạo, cầu gỗ, làn xe đạp, sân chơi sáng tạo; mùa đông có đường trượt tuyết.",
        "Biểu tượng cho làn sóng đổi mới không gian công cộng của Kazan hiện đại.",
    ],
    {
        "hours_vi": "Công viên mở tự do cả ngày; đông vui nhất chiều tối và cuối tuần.",
        "ticket_vi": "Vào tự do; thuê xe đạp/patin, công viên dây và một số dịch vụ tính phí riêng.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Mùa hè để dạo và đạp xe; mùa đông để trượt tuyết.",
        "tips_vi": "Cách trung tâm vài km về phía nam; đi taxi/xe buýt tiện. Mang giày thể thao nếu muốn chạy/đạp xe.",
    },
    [
        {"title": "Wikipedia (RU) — Парк «Горкинско-Ометьевский лес»", "url": "https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%BA_%C2%AB%D0%93%D0%BE%D1%80%D0%BA%D0%B8%D0%BD%D1%81%D0%BA%D0%BE-%D0%9E%D0%BC%D0%B5%D1%82%D1%8C%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%BB%D0%B5%D1%81%C2%BB"},
        {"title": "Yandex Maps — Горкинско-Ометьевский лес (trang tổ chức)", "url": "https://yandex.com/maps/org/gorkinsko_ometyevskiy_les/8416236532/"},
    ],
    ["park", "eco-park", "forest", "modern", "recreation", "kazan"],
    maps={
        "yandex": "https://yandex.com/maps/org/gorkinsko_ometyevskiy_les/8416236532/",
        "google": "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote("Gorkinsko-Ometyevo Forest Park, Kazan, Russia"),
    },
))

# 7) Vườn thú Kazan 'Sông Zambezi' --------------------------------------------
RECORDS.append(rec(
    "kazan-zoo-zambezi",
    "Vườn thú – bách thảo Kazan «Sông Zambezi» (Zoobotanicheskiy sad «Reka Zambezi»)",
    "Казанский зооботанический сад «Река Замбези»",
    "Kazan Zoobotanical Garden «Zambezi River»",
    ["other", "park_garden"],
    55.761509, 49.136804,
    "Phố Khadi Taktasha, số 120 (khu 1), quận Privolzhsky, phía nam Kazan (gần kênh đua thuyền).",
    "Khu vườn thú – bách thảo hiện đại mở rộng của Kazan mang chủ đề 'Sông Zambezi' châu Phi, khánh "
    "thành từ năm 2021. Một trong những vườn thú mới và hấp dẫn bậc nhất vùng Volga, đặc biệt được "
    "gia đình có trẻ nhỏ yêu thích.",
    "Vườn thú – bách thảo Kazan có lịch sử lâu đời, nhưng bước ngoặt lớn đến khi khu mở rộng mang "
    "chủ đề 'Sông Zambezi' (Reka Zambezi) được khánh thành từ năm 2021, biến nơi đây thành một "
    "trong những vườn thú hiện đại và hấp dẫn nhất vùng Volga. Khu mới rộng nhiều hecta nằm ở phía "
    "nam thành phố, gần kênh đua thuyền, được thiết kế theo mô hình vườn thú kiểu công viên: các "
    "loài thú được nuôi trong không gian mô phỏng môi trường sống tự nhiên của lục địa châu Phi và "
    "nhiều vùng khác, có cầu cạn và lối đi cho khách quan sát gần gũi mà vẫn an toàn. Du khách có "
    "thể gặp voi, hươu cao cổ, sư tử, hà mã, khỉ, các loài chim và bò sát… cùng khu nhà kính thực "
    "vật nhiệt đới. Với không gian rộng rãi, sạch đẹp và tính giáo dục cao, đây là điểm đến lý "
    "tưởng cho gia đình đi cùng trẻ em, đồng thời cho thấy sự đầu tư mạnh cho các không gian giải "
    "trí – giáo dục hiện đại ở Kazan. Nên dành ít nhất nửa ngày và tránh giờ nắng gắt mùa hè.",
    [
        "Khu vườn thú chủ đề 'Sông Zambezi' hiện đại, khánh thành từ 2021 — thuộc hàng mới và đẹp nhất vùng Volga.",
        "Chuồng trại kiểu công viên mô phỏng môi trường sống tự nhiên, quan sát gần mà an toàn.",
        "Điểm đến giáo dục – giải trí lý tưởng cho gia đình có trẻ nhỏ.",
    ],
    {
        "hours_vi": "Mở hằng ngày, thường 8:30–17:00 (phòng vé đóng sớm hơn); kiểm tra lịch theo mùa.",
        "ticket_vi": "Có bán vé vào cửa; giá tuỳ mùa và độ tuổi.",
        "duration_vi": "Nửa ngày (2–3 giờ trở lên).",
        "best_time_vi": "Mùa xuân – thu; buổi sáng mát mẻ, thú hoạt động nhiều hơn.",
        "tips_vi": "Đi giày thoải mái vì khuôn viên rộng; mang nước, mũ nắng mùa hè. Có thể tới bằng xe buýt hoặc taxi.",
    },
    [
        {"title": "Yandex Maps — Река Замбези, Казанский зооботанический сад (trang tổ chức)", "url": "https://yandex.ru/maps/org/reka_zambezi_kazanskiy_zoobotanicheskiy_sad/133272202632/"},
        {"title": "2GIS Казань — Река Замбези, зоопарк (toạ độ)", "url": "https://2gis.ru/kazan/firm/2956015536461070"},
    ],
    ["zoo", "botanical-garden", "zambezi", "family", "modern", "kazan"],
    official_site="https://kazzoobotsad.ru/",
    maps={
        "yandex": "https://yandex.ru/maps/org/reka_zambezi_kazanskiy_zoobotanicheskiy_sad/133272202632/",
        "google": "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote("Kazan Zoo Zambezi River, Kazan, Russia"),
    },
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
