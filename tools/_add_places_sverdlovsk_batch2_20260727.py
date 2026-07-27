# -*- coding: utf-8 -*-
"""_add_places_sverdlovsk_batch2_20260727.py — VÙNG TIÊU ĐIỂM: Tỉnh Sverdlovsk
(lần chạy tự động 2026-07-27, đợt 2).

Bối cảnh: sverdlovsk.json hiện có 22 địa điểm (sau đợt 1 sáng nay). tatarstan (60) và
nizhny-novgorod (58) đã ≥50 => vùng tiêu điểm vẫn là Sverdlovsk (slug kế trong danh sách
ưu tiên còn <50). Nâng dần tới ~50–100.

Đợt này bổ sung 15 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình
(museum 5 · church 3 · monument 2 · square_street 2 · park_garden 2 · other 1):
- Bảo tàng: Музей истории и археологии Урала (giữ Шигирский идол — tượng gỗ cổ nhất thế giới),
  Екатеринбургский музей ИЗО (Каслинский чугунный павильон — Grand Prix Paris 1900),
  Мемориальный дом-музей Бажова, Нижнетагильский музей ИЗО («Тагильская Мадонна» ~Rafael),
  Музей золота (Берёзовский — cái nôi khai thác vàng Nga).
- Nhà thờ: Большой Златоуст (Екб), Спасо-Преображенский собор (Невьянск),
  Казанская церковь trên «Церковный камень» (Арамашево).
- Đài/tượng: Памятник клавиатуре, Памятник Татищеву и де Геннину.
- Quảng trường/phố: Площадь 1905 года, пешеходная улица Вайнера («Уральский Арбат»).
- Thiên nhiên: Природный парк «Река Чусовая», Конжаковский Камень (đỉnh cao nhất tỉnh).
- Khác: буддийский монастырь Шедруб Линг trên núi Качканар.

TOẠ ĐỘ — xác minh chéo (2026-07):
  Музей ИЗО 56.835128,60.603236 (en.wiki geohack Воеводина 5); Большой Златоуст
  56.834394,60.601014 (en.wiki Great Zlatoust); Памятник клавиатуре 56.832176,60.607760
  (2GIS, набережная Исети/Горького); Площадь 1905 56.837917,60.597220 (ru.wiki);
  Памятник Татищеву и де Геннину / Площадь Труда 56.838378,60.606778 (ru.wiki);
  Дом-музей Бажова 56.818398,60.613311 (2GIS Чапаева 11); Музей истории и археологии
  56.84155,60.61330 (ДК Дзержинского, Городок чекистов, пр. Ленина 69/10);
  ул. Вайнера (điểm giữa đoạn đi bộ) 56.83300,60.60130; Спасо-Преображенский собор
  Невьянск 57.489598,60.222402 (ru.wiki, Сквер Демидова 1); Нижнетагильский музей ИЗО
  57.905733,59.955517 (2GIS Уральская 7); Музей золота Берёзовский 56.912717,60.801861
  (56°54'45.78"N 60°48'06.70"E — có URL Яндекс-организации); монастырь Шедруб Линг /
  Качканар 58.777173,59.385043; Конжаковский Камень 59.61670,59.13330 (en.wiki, 59°37'N
  59°08'E — đỉnh cao nhất tỉnh, nằm ở rìa tây, lon ~59,13 là ĐÚNG); Арамашево, Казанская
  церковь 57.608252,61.737509 (sobory.ru).
  Kiểm tra thứ tự & phạm vi (tỉnh Sverdlovsk: lat ~56,3–59,6; lon ~59,1–63,1; KHÔNG đảo
  lat/lon; đều nằm trong tỉnh). Link bản đồ TRỎ-ĐỊA-ĐIỂM: text-search theo tên_ru + thành phố,
  canh giữa theo toạ độ đã kiểm; riêng Музей золота dùng URL trang tổ chức Яндекс.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_sverdlovsk_batch2_20260727.py
       python3 tools/normalize_categories.py && python3 tools/build.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"

REGION = "sverdlovsk"
REGION_NAME_VI = "Tỉnh Sverdlovsk"
FD = "Vùng Ural"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def maps_org(yandex_org_url, name_en, city_en):
    """Ưu tiên URL trang tổ chức/địa điểm Yandex (chính xác nhất) + Google text-search."""
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": yandex_org_url,
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def rec(slug, name_vi, name_ru, name_en, categories, lat, lon, address_vi,
        short, long, highlights, practical, sources, tags, maps,
        official_site=None):
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
        "rating": {"value": None, "count": None, "source": None, "as_of": None},
        "review_summary_vi": "",
        "presentation_short_vi": short,
        "presentation_long_vi": long,
        "highlights_vi": highlights,
        "practical": practical,
        "photo": None,
        "photo_credit": None,
        "maps": maps,
        "official_site": official_site,
        "sources": sources,
        "tags": tags,
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia",
    }


RECORDS = []

# 1) Музей истории и археологии Урала (Шигирский идол) -------------------------
RECORDS.append(rec(
    "museum-history-archaeology-urals",
    "Bảo tàng Lịch sử và Khảo cổ Ural (Thần tượng gỗ Shigir)",
    "Музей истории и археологии Урала",
    "Museum of History and Archaeology of the Urals",
    ["museum"],
    56.84155, 60.61330,
    "Проспект Ленина, 69/10, toà nhà Cung Văn hoá Dzerzhinsky trong «Городок чекистов», trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Bảo tàng chủ lực của Bảo tàng địa phương tỉnh Sverdlovsk, nơi lưu giữ báu vật tầm cỡ thế giới: Thần tượng gỗ Shigir (Большой Шигирский идол) – tác phẩm điêu khắc bằng gỗ cổ nhất còn tồn tại của nhân loại, khoảng 12.000 năm tuổi. Bảo tàng đặt trong toà nhà kiến trúc kiến tạo (constructivism) thập niên 1930 thuộc quần thể «Thị trấn chekist».",
    "Nằm trong toà Cung Văn hoá Dzerzhinsky – một mảnh của quần thể kiến trúc kiến tạo nổi tiếng «Городок чекистов» (Thị trấn của các chekist) – Bảo tàng Lịch sử và Khảo cổ Ural là điểm phải đến để hiểu bề dày lịch sử vùng Ural từ thời đồ đá tới thế kỷ 20. Ngôi sao của bộ sưu tập là Thần tượng gỗ Shigir: được tìm thấy năm 1890 dưới lớp than bùn gần Kirovgrad, pho tượng cao nguyên bản tới hơn năm mét, khắc đầy hoa văn hình học và những khuôn mặt bí ẩn. Các phân tích định tuổi bằng đồng vị phóng xạ cho thấy tượng có niên đại khoảng 12.000 năm – nghĩa là cổ gấp đôi các kim tự tháp Ai Cập hay Stonehenge, khiến nó trở thành tác phẩm điêu khắc gỗ nguyên khối lâu đời nhất mà con người còn giữ được. Nhờ lớp than bùn yếm khí, gỗ được bảo tồn kỳ diệu và nay được trưng bày trong tủ kính khí trơ, kiểm soát nhiệt – ẩm nghiêm ngặt tại khu «Kho báu Shigir». Ngoài thần tượng, năm tầng trưng bày còn dẫn khách qua khảo cổ tiền sử, văn hoá các dân tộc Ural, quá trình khai mỏ – luyện kim và đời sống đô thị Yekaterinburg. Đây là nơi kết nối trực tiếp du khách với chiều sâu hàng vạn năm của lịch sử loài người trên đất Ural.",
    [
        "Trưng bày Thần tượng gỗ Shigir – tác phẩm điêu khắc gỗ cổ nhất thế giới, khoảng 12.000 năm tuổi.",
        "Đặt trong Cung Văn hoá Dzerzhinsky thuộc quần thể kiến tạo «Городок чекистов» thập niên 1930.",
        "Năm tầng trưng bày lịch sử Ural từ thời đồ đá đến thế kỷ 20; khu «Kho báu Shigir» kiểm soát vi khí hậu.",
    ],
    {
        "hours_vi": "Thường mở 11:00–20:00, đóng cửa Thứ Hai (nên kiểm tra lịch chính thức).",
        "ticket_vi": "Vé vào có thu phí (khoảng 300 ₽ người lớn, giảm cho học sinh/sinh viên); giá tham khảo 2026.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Quanh năm (không gian trong nhà).",
        "tips_vi": "Đừng bỏ lỡ khu «Kho báu Shigir»; kết hợp ngắm kiến trúc kiến tạo của Городок чекистов và khách sạn Iset liền kề.",
    },
    [
        {"title": "Wikipedia (EN) — Shigir Idol", "url": "https://en.wikipedia.org/wiki/Shigir_Idol"},
        {"title": "Свердловский областной краеведческий музей — trang chính thức", "url": "https://uole-museum.ru/museums/muzej-istorii-i-arheologii-urala/"},
    ],
    ["museum", "archaeology", "shigir-idol", "prehistory", "constructivism", "yekaterinburg"],
    maps_text("Музей истории и археологии Урала", "Екатеринбург", "Museum of History and Archaeology of the Urals", "Yekaterinburg", 56.84155, 60.61330),
    official_site="https://uole-museum.ru/",
))

# 2) Екатеринбургский музей изобразительных искусств (Каслинский павильон) -----
RECORDS.append(rec(
    "yekaterinburg-fine-arts-museum",
    "Bảo tàng Mỹ thuật Yekaterinburg (Đình gang Kasli)",
    "Екатеринбургский музей изобразительных искусств",
    "Yekaterinburg Museum of Fine Arts",
    ["museum"],
    56.835128, 60.603236,
    "Улица Воеводина, 5, bên bờ sông Iset cạnh quảng trường Lịch sử (Plotinka), Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Bảo tàng mỹ thuật hàng đầu vùng Ural, nổi danh nhờ báu vật độc nhất vô nhị: Đình gang Kasli (Каслинский чугунный павильон) – công trình đúc gang nghệ thuật từng đoạt Grand Prix tại Hội chợ Thế giới Paris 1900. Toà nhà chính nằm ngay bên sông Iset, sát quảng trường Lịch sử.",
    "Bảo tàng Mỹ thuật Yekaterinburg giữ một trong những bộ sưu tập nghệ thuật quan trọng nhất ngoài hai thủ đô, nhưng điều khiến nơi đây thật sự nổi tiếng là Đình gang Kasli. Đây là một gian triển lãm bằng gang đúc đồ sộ – gồm hơn 1.500 chi tiết, nặng khoảng 20 tấn – do các nghệ nhân xưởng đúc Kasli (nam Ural) chế tác riêng cho Hội chợ Thế giới Paris năm 1900, nơi nó giành Grand Prix cùng huy chương vàng lớn. Toàn bộ kết cấu, hoa văn, tượng nhỏ đều đúc từ gang nhưng tinh xảo tới mức trông nhẹ như ren, được xem là đỉnh cao của nghệ thuật đúc gang Ural và là hiện vật gang duy nhất trên thế giới được ghi vào danh mục di sản bảo tàng cấp quốc gia. Sau khi mang về Nga, đình từng bị tháo rời và hư hại; đến năm 1958 mới được phục dựng, rồi năm 1986 chuyển về toà nhà bệnh viện cũ của Nhà máy sắt Yekaterinburg trên phố Voevodina và trưng bày cho tới nay. Bên cạnh đình Kasli, bảo tàng còn có bộ sưu tập tranh Nga, nghệ thuật trang trí Ural (đá bán quý, gang, thép Zlatoust) và hội hoạ châu Âu. Vị trí ngay bên sông Iset, sát quảng trường Lịch sử, khiến đây là điểm dừng lý tưởng trong hành trình dạo trung tâm.",
    [
        "Trưng bày Đình gang Kasli – công trình đúc gang đoạt Grand Prix Paris 1900, ~1.500 chi tiết, nặng ~20 tấn.",
        "Hiện vật gang duy nhất thế giới được ghi vào danh mục di sản bảo tàng quốc gia Nga.",
        "Bộ sưu tập nghệ thuật trang trí Ural và hội hoạ Nga; toà nhà bên sông Iset, cạnh Plotinka.",
    ],
    {
        "hours_vi": "Thường mở 11:00–20:00, đóng cửa Thứ Hai (kiểm tra lịch chính thức).",
        "ticket_vi": "Có thu phí vé vào; nhiều mức giảm cho học sinh, sinh viên, người hưu trí.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (không gian trong nhà); kết hợp dạo bờ sông Iset khi trời đẹp.",
        "tips_vi": "Vào xem gian Đình gang Kasli trước tiên; toà nhà nằm sát quảng trường Lịch sử (Plotinka).",
    },
    [
        {"title": "Wikipedia (EN) — Yekaterinburg Museum of Fine Arts", "url": "https://en.wikipedia.org/wiki/Yekaterinburg_Museum_of_Fine_Arts"},
        {"title": "Wikipedia (EN) — Kasli iron sculpture", "url": "https://en.wikipedia.org/wiki/Kasli_iron_sculpture"},
    ],
    ["museum", "art", "kasli-pavilion", "cast-iron", "decorative-arts", "yekaterinburg"],
    maps_text("Екатеринбургский музей изобразительных искусств", "Екатеринбург", "Yekaterinburg Museum of Fine Arts", "Yekaterinburg", 56.835128, 60.603236),
    official_site="https://i-z-o.art/",
))

# 3) Большой Златоуст (Максимилиановская церковь) ------------------------------
RECORDS.append(rec(
    "bolshoy-zlatoust-church",
    "Nhà thờ Bolshoy Zlatoust (Đại Kim Khẩu)",
    "Большой Златоуст (Максимилиановская церковь)",
    "Great Zlatoust Church",
    ["church"],
    56.834394, 60.601014,
    "Улица 8 Марта, 17, góc với ул. Малышева, trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Nhà thờ – tháp chuông Chính thống giáo màu đỏ trắng nổi bật giữa trung tâm Yekaterinburg, cao khoảng 77 mét, từng là công trình cao nhất vùng Ural. Bị phá huỷ năm 1930 và được dựng lại gần như từ đầu vào năm 2006–2013.",
    "«Bolshoy Zlatoust» – tên dân gian của nhà thờ mang tên Thánh Maximilian, còn gọi là nhà thờ Đại Kim Khẩu (theo Thánh Gioan Kim Khẩu) – là một trong những công trình tôn giáo dễ nhận biết nhất Yekaterinburg. Nguyên bản được xây trong thế kỷ 19 theo phong cách Nga–Byzantine với tháp chuông cao khoảng 77 mét, biến nó thành toà nhà cao nhất vùng Ural thời bấy giờ và nổi tiếng với bộ chuông đồ sộ, trong đó có quả chuông nặng hàng chục tấn. Năm 1930, dưới thời Xô Viết, nhà thờ bị cho nổ phá huỷ hoàn toàn. Phải tới đầu thế kỷ 21, công trình mới được tái thiết gần như từ con số không dựa trên tư liệu và ảnh cũ; nhà thờ mới được thánh hiến năm 2013, phục dựng lại dáng vẻ đỏ – trắng rực rỡ với các mái vòm mạ vàng. Ngày nay Bolshoy Zlatoust vừa là nơi hành lễ, vừa là điểm nhấn kiến trúc quen thuộc ở góc phố 8 Tháng Ba và Malysheva, thường được du khách ghé thăm khi dạo bộ khu trung tâm lịch sử.",
    [
        "Tháp chuông cao ~77 m, từng là công trình cao nhất vùng Ural trước năm 1930.",
        "Bị phá huỷ năm 1930, tái thiết gần như từ đầu và thánh hiến lại năm 2013.",
        "Kiến trúc Nga–Byzantine đỏ – trắng với mái vòm mạ vàng, giữa trung tâm Yekaterinburg.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường sáng sớm đến tối; vào tự do.",
        "ticket_vi": "Vào nhà thờ miễn phí.",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Quanh năm; ấn tượng khi lên đèn buổi tối.",
        "tips_vi": "Ăn mặc kín đáo khi vào bên trong; kết hợp dạo phố đi bộ Vaynera và quảng trường 1905 gần đó.",
    },
    [
        {"title": "Wikipedia (EN) — Great Zlatoust Church", "url": "https://en.wikipedia.org/wiki/Great_Zlatoust_Church"},
        {"title": "Wikidata — Great Zlatoust Church (Q4092626)", "url": "https://www.wikidata.org/wiki/Q4092626"},
    ],
    ["church", "orthodox-church", "bell-tower", "architecture", "yekaterinburg"],
    maps_text("Большой Златоуст", "Екатеринбург", "Great Zlatoust Church", "Yekaterinburg", 56.834394, 60.601014),
))

# 4) Памятник клавиатуре -------------------------------------------------------
RECORDS.append(rec(
    "keyboard-monument-yekaterinburg",
    "Đài kỷ niệm Bàn phím (Pamyatnik klaviature)",
    "Памятник клавиатуре",
    "Keyboard Monument",
    ["monument"],
    56.832176, 60.607760,
    "Kè sông Iset phía đường Gorkogo (giữa nhà 14а và 28а), khu Dendrary, trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Tác phẩm land-art độc đáo bên bờ sông Iset: một bàn phím máy tính khổng lồ tỉ lệ 30:1 với 104 phím bê tông đặt thẳng trên mặt đất. Ra đời năm 2005, nay là một trong những biểu tượng vui nhộn và được tìm kiếm nhiều nhất của Yekaterinburg.",
    "Đài kỷ niệm Bàn phím là một trong những công trình nghệ thuật đường phố dí dỏm và nổi tiếng nhất nước Nga. Do nghệ sĩ địa phương Anatoly Vyatkin thực hiện và khánh thành tháng 10 năm 2005, tác phẩm tái hiện nguyên một bàn phím máy tính theo bố cục chữ cái Nga ЙЦУКЕН, phóng to tỉ lệ 30:1: 104 phím đúc bê tông rải trên khoảng đất 16×4 mét ngay ven kè sông Iset. Mỗi phím thường nặng khoảng 80 kg, riêng phím cách (space) nặng gần nửa tấn. Người dân và du khách thích thú «gõ» lên các phím, nhảy từ chữ này sang chữ kia hay đứng chụp ảnh; có cả tục lệ ước nguyện rồi bước qua đủ các phím. Nơi đây trở thành điểm tụ họp quen thuộc, đặc biệt vào Ngày Quản trị hệ thống (Sysadmin Day) cuối tháng Bảy với những «cuộc thi» hài hước của giới IT. Trong một khảo sát năm 2019, đài Bàn phím được xếp là tượng đài được tìm kiếm nhiều thứ nhì ở Nga, chỉ sau Kỵ sĩ Đồng của Sankt-Peterburg. Dù nhỏ và giản dị, đây là một điểm dừng chân thú vị, phản ánh tinh thần hiện đại, hóm hỉnh của thành phố.",
    [
        "Bàn phím máy tính khổng lồ tỉ lệ 30:1 với 104 phím bê tông, khánh thành năm 2005.",
        "Tác giả Anatoly Vyatkin; phím cách nặng gần nửa tấn; gắn với Ngày Quản trị hệ thống cuối tháng 7.",
        "Xếp thứ nhì trong khảo sát tượng đài được tìm kiếm nhiều nhất nước Nga (2019).",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Ban ngày để chụp ảnh; mùa hè dễ kết hợp dạo kè sông Iset.",
        "tips_vi": "Nằm bên bờ sông giữa Rạp xiếc và Plotinka; thử «gõ» đủ các phím theo tục ước nguyện của dân địa phương.",
    },
    [
        {"title": "Wikipedia (EN) — Keyboard Monument", "url": "https://en.wikipedia.org/wiki/Keyboard_Monument"},
        {"title": "The New York Times — Yekaterinburg keyboard monument (2018)", "url": "https://www.nytimes.com/2018/07/03/sports/world-cup/yekaterinburg-keyboard-monument.html"},
    ],
    ["monument", "land-art", "modern", "quirky", "iset-river", "yekaterinburg"],
    maps_text("Памятник клавиатуре", "Екатеринбург", "Keyboard Monument", "Yekaterinburg", 56.832176, 60.607760),
))

# 5) Площадь 1905 года --------------------------------------------------------
RECORDS.append(rec(
    "ploshchad-1905-goda",
    "Quảng trường Năm 1905 (Ploshchad 1905 goda)",
    "Площадь 1905 года",
    "1905 Square",
    ["square_street"],
    56.837917, 60.597220,
    "Trung tâm lịch sử Yekaterinburg, giao giữa проспект Ленина và ул. 8 Марта, bên hữu ngạn sông Iset, tỉnh Sverdlovsk, Nga.",
    "Quảng trường trung tâm và chính của Yekaterinburg, hình thành từ khu chợ và quảng trường nhà thờ cũ. Nơi đặt tượng Lenin bằng granit, toà thị chính và là sân khấu của các sự kiện lớn, hội chợ, sân trượt băng dịp Năm mới.",
    "Quảng trường Năm 1905 là trái tim của Yekaterinburg, nơi tập trung đời sống công cộng của thành phố suốt hơn hai thế kỷ. Trong lịch sử, đây từng là hai quảng trường: quảng trường Nhà thờ (Kafedralnaya) với Nhà thờ lớn Bogoyavlensky, và quảng trường Chợ chính. Sau khi nhà thờ bị phá năm 1930, hai khu gộp lại thành một không gian rộng lớn mang tên «Năm 1905» để tưởng nhớ các cuộc biểu tình của công nhân đầu thế kỷ 20. Bao quanh quảng trường là những công trình bề thế, nổi bật là toà nhà Hành chính thành phố (thị chính) với tháp đồng hồ và chóp nhọn. Từ năm 1957, tượng đài Lenin bằng granit cao khoảng sáu mét đứng trên bệ cao ở rìa quảng trường, tạo nên diện mạo quen thuộc tới nay. Ngày thường, đây là điểm hẹn và giao lộ đông đúc; vào các dịp lễ lớn, quảng trường biến thành sân khấu của diễu hành, hoà nhạc, hội chợ, và đặc biệt mỗi mùa đông lại được dựng thành «thị trấn băng» khổng lồ với cầu trượt và sân trượt băng rực rỡ đèn màu – một trải nghiệm rất Ural mà du khách nên thử nếu tới vào dịp Năm mới.",
    [
        "Quảng trường chính và trung tâm lịch sử của Yekaterinburg, hình thành sau khi phá Nhà thờ Bogoyavlensky (1930).",
        "Tượng Lenin bằng granit cao ~6 m (từ 1957) và toà thị chính với tháp đồng hồ.",
        "Mùa đông trở thành «thị trấn băng» với cầu trượt, sân trượt băng dịp Năm mới.",
    ],
    {
        "hours_vi": "Không gian công cộng ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút; lâu hơn nếu có sự kiện.",
        "best_time_vi": "Cuối tháng 12 đến đầu tháng 1 để xem thị trấn băng; mùa hè thoáng đãng dễ dạo bộ.",
        "tips_vi": "Là điểm khởi đầu tiện lợi để đi bộ sang phố Vaynera và quảng trường Lịch sử (Plotinka).",
    },
    [
        {"title": "Wikipedia (RU) — Площадь 1905 года (Екатеринбург)", "url": "https://ru.wikipedia.org/wiki/Площадь_1905_года_(Екатеринбург)"},
    ],
    ["square_street", "city-center", "lenin-monument", "events", "yekaterinburg"],
    maps_text("Площадь 1905 года", "Екатеринбург", "1905 Square", "Yekaterinburg", 56.837917, 60.597220),
))

# 6) Памятник Татищеву и де Геннину -------------------------------------------
RECORDS.append(rec(
    "founders-monument-tatishchev-de-gennin",
    "Đài tưởng niệm Người sáng lập Tatishchev và de Gennin",
    "Памятник Татищеву и де Геннину",
    "Monument to Tatishchev and de Gennin",
    ["monument"],
    56.838378, 60.606778,
    "Площадь Труда (Quảng trường Lao động), gần nhà nguyện Thánh Ekaterina, sát quảng trường Lịch sử, Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Tượng đài đôi vinh danh hai «người cha khai sinh» Yekaterinburg: nhà bác học – chính khách Vasily Tatishchev và kỹ sư quân sự gốc Đức–Hà Lan Georg Wilhelm de Gennin. Khánh thành năm 1998 nhân 275 năm thành phố, đặt trên Quảng trường Lao động ngay trung tâm.",
    "Đứng trên Quảng trường Lao động (Ploshchad Truda), sát cạnh quảng trường Lịch sử, tượng đài Tatishchev và de Gennin là một trong những biểu tượng được yêu mến nhất Yekaterinburg. Công trình do nhà điêu khắc Pyotr Chusovitin thực hiện, khánh thành ngày 14 tháng 8 năm 1998 đúng dịp kỷ niệm 275 năm ngày thành lập thành phố. Hai nhân vật được tạc đứng cạnh nhau bằng đồng: Vasily Tatishchev – nhà sử học, địa lý học và quan chức khai mỏ lỗi lạc, cùng Georg Wilhelm de Gennin (người Nga quen gọi Vilim de Gennin) – viên tướng, kỹ sư gốc Đức–Hà Lan phục vụ Pyotr Đại đế. Chính hai ông đã chỉ đạo dựng nhà máy – pháo đài bên sông Iset năm 1723, khai sinh Yekaterinburg. Bức tượng được đúc từ 19 mảnh đồng tại chính nhà máy Uralmash danh tiếng của thành phố. Người dân đôi khi hóm hỉnh gọi hai ông là «Bim và Bom» vì đứng sóng đôi giống nhau; dù vậy, tượng đài vẫn là nơi trang trọng để hiểu về nguồn gốc công nghiệp của «thủ phủ vùng Ural» và là điểm chụp ảnh quen thuộc giữa trung tâm.",
    [
        "Vinh danh hai người sáng lập Yekaterinburg: Vasily Tatishchev và Wilhelm de Gennin (1723).",
        "Khánh thành 14/8/1998 nhân 275 năm thành phố; nhà điêu khắc P. Chusovitin.",
        "Đúc từ 19 mảnh đồng tại nhà máy Uralmash; dân địa phương gọi vui là «Bim và Bom».",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Quanh năm; kết hợp cùng quảng trường Lịch sử (Plotinka) liền kề.",
        "tips_vi": "Ngay cạnh là nhà nguyện Thánh Ekaterina và bờ hồ; tiện gộp vào lộ trình đi bộ trung tâm.",
    },
    [
        {"title": "Wikipedia (RU) — Памятник Татищеву и де Геннину", "url": "https://ru.wikipedia.org/wiki/Памятник_Татищеву_и_де_Геннину"},
    ],
    ["monument", "city-founders", "history", "bronze", "yekaterinburg"],
    maps_text("Памятник Татищеву и де Геннину", "Екатеринбург", "Monument to Tatishchev and de Gennin", "Yekaterinburg", 56.838378, 60.606778),
))

# 7) Пешеходная улица Вайнера («Уральский Арбат») -----------------------------
RECORDS.append(rec(
    "vaynera-street",
    "Phố đi bộ Vaynera («Arbat của Ural»)",
    "Улица Вайнера",
    "Vaynera Street",
    ["square_street"],
    56.83300, 60.60130,
    "Đoạn đi bộ giữa проспект Ленина và ул. Куйбышева, khu trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Phố đi bộ trung tâm sầm uất của Yekaterinburg, quen gọi là «Arbat của Ural». Con phố cổ với các dinh thự thương gia thế kỷ 19, san sát cửa hàng, quán cà phê và rải rác nhiều bức tượng đồng ngộ nghĩnh làm điểm sống ảo.",
    "Là một trong những con phố lâu đời nhất Yekaterinburg (có từ thập niên 1740), phố Vaynera nay là tuyến đi bộ nhộn nhịp bậc nhất thành phố. Đoạn giữa đại lộ Lenin và phố Kuybysheva được biến thành phố đi bộ từ năm 2003 và nhanh chóng có biệt danh trìu mến «Uralsky Arbat» – Arbat của vùng Ural, ví với phố đi bộ Arbat nổi tiếng ở Moskva. Dạo dọc con phố, du khách vừa ngắm những dinh thự, nhà buôn bằng gạch – đá từ thế kỷ 19 được bảo tồn, vừa gặp một «bảo tàng ngoài trời» gồm nhiều tượng đồng sinh động: chàng trai đi xe đạp cổ, cặp tình nhân, người thợ chạm, nhà buôn, hay bức tượng dành cho người yêu nhau… mỗi tác phẩm đều gắn với một câu chuyện và trở thành điểm chụp ảnh yêu thích. Xen giữa là hàng loạt cửa hàng, quán cà phê, nhà hàng và các gánh biểu diễn đường phố, khiến Vaynera luôn sống động từ sáng tới khuya. Đây là nơi lý tưởng để cảm nhận nhịp sống đời thường, mua sắm và thư giãn ngay giữa lòng «thủ phủ vùng Ural».",
    [
        "Phố đi bộ trung tâm từ 2003, biệt danh «Arbat của Ural».",
        "Nhiều dinh thự thương gia thế kỷ 19 và một «bảo tàng ngoài trời» gồm các tượng đồng sinh động.",
        "San sát cửa hàng, quán cà phê, biểu diễn đường phố – sống động cả ngày lẫn tối.",
    ],
    {
        "hours_vi": "Không gian công cộng ngoài trời, dạo bộ tự do mọi lúc; cửa hàng/quán theo giờ riêng.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 45–60 phút thong thả.",
        "best_time_vi": "Chiều tối và cuối tuần khi phố đông vui, nhiều biểu diễn đường phố.",
        "tips_vi": "Tìm và chụp ảnh cùng các tượng đồng dọc phố; nối liền với quảng trường 1905 và Bolshoy Zlatoust.",
    },
    [
        {"title": "Wikipedia (RU) — Улица Вайнера (Екатеринбург)", "url": "https://ru.wikipedia.org/wiki/Улица_Вайнера_(Екатеринбург)"},
    ],
    ["square_street", "pedestrian", "shopping", "sculptures", "city-center", "yekaterinburg"],
    maps_text("Улица Вайнера", "Екатеринбург", "Vaynera Street", "Yekaterinburg", 56.83300, 60.60130),
))

# 8) Мемориальный дом-музей П. П. Бажова ---------------------------------------
RECORDS.append(rec(
    "bazhov-house-museum",
    "Nhà lưu niệm nhà văn P. P. Bazhov",
    "Мемориальный дом-музей П. П. Бажова",
    "P. P. Bazhov Memorial House-Museum",
    ["museum"],
    56.818398, 60.613311,
    "Улица Чапаева, 11, khu phố cổ ven trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Ngôi nhà gỗ do chính nhà văn Pavel Bazhov tự tay dựng cho gia đình, nơi ông sống và sáng tác tập truyện cổ Ural trứ danh «Chiếc hộp malachite». Nay là bảo tàng lưu niệm giữ gần như nguyên vẹn không gian sống đầu thế kỷ 20.",
    "Pavel Petrovich Bazhov (1879–1950) là nhà văn Ural nổi tiếng nhất, người đã thu thập và kể lại những truyện cổ dân gian vùng mỏ thành tập «Malakhitovaya shkatulka» (Chiếc hộp malachite) – với các nhân vật đã thành huyền thoại như Bà Chúa Núi Đồng, chú thằn lằn và người thợ đá Danila. Ngôi nhà gỗ một tầng trên phố Chapaeva do chính Bazhov dựng năm 1911 – 1914, và ông đã sống ở đây gần bốn thập niên cho tới khi qua đời. Sau khi vợ ông mất, ngôi nhà được chuyển thành bảo tàng lưu niệm và mở cửa từ năm 1969. Điều quý giá là gần như toàn bộ nội thất, đồ đạc, sách vở, bàn viết và cả khu vườn với những cây do gia đình trồng đều được giữ nguyên, tạo cảm giác nhà văn chỉ vừa mới rời đi. Khách tham quan được dẫn qua phòng làm việc nơi Bazhov viết nên các sказ (truyện cổ) trứ danh, phòng khách, gian bếp và khoảng sân yên tĩnh. Với những ai yêu văn học và muốn hiểu tâm hồn vùng Ural, đây là một điểm đến ấm áp, đưa người xem bước thẳng vào thế giới cổ tích đá quý đã làm nên tên tuổi Bazhov.",
    [
        "Ngôi nhà gỗ do chính Bazhov dựng (1911–1914), nơi ông viết «Chiếc hộp malachite».",
        "Nội thất, bàn viết, sách vở và khu vườn được giữ gần như nguyên vẹn; mở làm bảo tàng từ 1969.",
        "Đưa du khách vào thế giới truyện cổ Ural: Bà Chúa Núi Đồng, người thợ đá Danila…",
    ],
    {
        "hours_vi": "Thường mở 10:00–18:00, đóng cửa Chủ Nhật – Thứ Hai (kiểm tra lịch chính thức).",
        "ticket_vi": "Vé vào phí thấp; có giảm cho học sinh, sinh viên, người hưu trí.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm; mùa hè có thể dạo thêm khu vườn.",
        "tips_vi": "Nên đi cùng thuyết minh để hiểu các truyện cổ; đọc trước vài truyện trong «Chiếc hộp malachite».",
    },
    [
        {"title": "Wikipedia (EN) — Pavel Bazhov", "url": "https://en.wikipedia.org/wiki/Pavel_Bazhov"},
        {"title": "Объединённый музей писателей Урала — dom-muzey Bazhova", "url": "https://ompural.ru/museum/dom-muzey-ppbazhova"},
    ],
    ["museum", "literature", "bazhov", "house-museum", "folklore", "yekaterinburg"],
    maps_text("Дом-музей П. П. Бажова", "Екатеринбург", "Bazhov House Museum", "Yekaterinburg", 56.818398, 60.613311),
))

# 9) Природный парк «Река Чусовая» --------------------------------------------
RECORDS.append(rec(
    "chusovaya-river-nature-park",
    "Công viên thiên nhiên «Sông Chusovaya»",
    "Природный парк «Река Чусовая»",
    "Chusovaya River Nature Park",
    ["park_garden"],
    57.218098, 59.341522,
    "Trải trên các huyện Nizhny Tagil, Prigorodny và Shalinsky; trạm sinh thái tại làng Староуткинск, tỉnh Sverdlovsk, Nga.",
    "Công viên thiên nhiên bảo vệ đoạn thượng – trung lưu con sông Chusovaya huyền thoại, dòng sông duy nhất cắt ngang dãy Ural từ châu Á sang châu Âu. Nổi tiếng với những vách đá «lính gác» (bойцы) dựng đứng hai bên bờ, là thiên đường của du lịch chèo thuyền (splav).",
    "Sông Chusovaya là một trong những dòng sông nổi tiếng và được yêu thích nhất vùng Ural, độc đáo ở chỗ nó bắt nguồn ở sườn châu Á rồi xuyên thẳng qua dãy Ural để đổ sang phần châu Âu của nước Nga. Công viên thiên nhiên «Sông Chusovaya», thành lập năm 2004, bảo vệ đoạn thượng và trung lưu đẹp nhất của con sông cùng vùng rừng taiga, làng cổ và di tích công nghiệp mỏ hai bên bờ. Điểm làm nên tên tuổi Chusovaya là những vách đá vôi khổng lồ dựng đứng sát mép nước, được dân địa phương gọi là «bойцы» (lính gác/đấu sĩ) – bởi xưa kia các bè gỗ, bè quặng trôi theo dòng thường đâm vào chúng mà vỡ tan. Nhiều vách đá là di tích thiên nhiên có tên riêng và gắn với truyền thuyết. Ngày nay, chèo thuyền – bè xuôi dòng Chusovaya (splav) vào mùa hè là một trong những trải nghiệm du lịch mạo hiểm kinh điển của Ural: du khách lướt giữa hẻm núi, cắm trại ven sông, ngắm hang động và leo lên các vách đá để phóng tầm mắt. Công viên có các trạm sinh thái (ở Староуткинск và làng Baronskaya) hỗ trợ du khách, cùng nhiều tuyến đi bộ và điểm ngắm cảnh, phù hợp cho cả người ưa vận động lẫn khách muốn hoà mình vào thiên nhiên Ural.",
    [
        "Bảo vệ dòng Chusovaya – con sông cắt ngang dãy Ural, nối châu Á với châu Âu.",
        "Nổi tiếng với các vách đá «bойцы» dựng đứng ven sông, nhiều vách là di tích thiên nhiên có truyền thuyết.",
        "Thiên đường chèo thuyền – bè (splav) mùa hè; có trạm sinh thái, tuyến đi bộ và điểm cắm trại.",
    ],
    {
        "hours_vi": "Khu thiên nhiên ngoài trời; các tuyến splav và trạm sinh thái hoạt động chủ yếu mùa ấm (khoảng tháng 5–9).",
        "ticket_vi": "Vào tham quan có thể cần đăng ký/nộp phí sinh thái; tour chèo thuyền tính phí riêng theo nhà tổ chức.",
        "duration_vi": "Từ nửa ngày tham quan điểm ngắm tới nhiều ngày cho hành trình splav.",
        "best_time_vi": "Cuối tháng 5 đến tháng 8 cho chèo thuyền và thời tiết thuận lợi.",
        "tips_vi": "Đặt tour splav qua đơn vị uy tín, chuẩn bị đồ chống nước và giày phù hợp; liên hệ trạm sinh thái để biết tuyến.",
    },
    [
        {"title": "Wikipedia (RU) — Река Чусовая (природный парк)", "url": "https://ru.wikipedia.org/wiki/Река_Чусовая_(природный_парк)"},
        {"title": "Наш Урал — Природный парк «Река Чусовая»", "url": "https://nashural.ru/mesta/sverdlovskaya-oblast/prirodniy-park-reka-chusovaya/"},
    ],
    ["park_garden", "nature", "river", "rafting", "cliffs", "ural"],
    maps_text("Природный парк Река Чусовая", "Староуткинск", "Chusovaya River Nature Park", "Staroutkinsk", 57.218098, 59.341522),
))

# 10) Спасо-Преображенский собор (Невьянск) -----------------------------------
RECORDS.append(rec(
    "nevyansk-spaso-preobrazhensky-cathedral",
    "Nhà thờ Chúa Biến Hình ở Nevyansk (Spaso-Preobrazhensky sobor)",
    "Спасо-Преображенский собор (Невьянск)",
    "Spaso-Preobrazhensky Cathedral (Nevyansk)",
    ["church"],
    57.489598, 60.222402,
    "Сквер Демидова, 1, ngay cạnh Tháp nghiêng Nevyansk, thành phố Nevyansk, tỉnh Sverdlovsk, Nga.",
    "Nhà thờ chính toà bề thế đứng ngay cạnh Tháp nghiêng Nevyansk trứ danh, tạo thành quần thể lịch sử Demidov của thành phố. Tháp chuông cao 64 mét khiến đây là một trong những nhà thờ cao nhất vùng, phục dựng sau thời Xô Viết.",
    "Nằm ngay bên chân Tháp nghiêng Nevyansk – biểu tượng của dòng họ chủ mỏ Demidov – nhà thờ Chúa Biến Hình (Spaso-Preobrazhensky) là công trình tôn giáo lớn và nổi bật nhất thành phố Nevyansk. Nhà thờ được khởi công năm 1824 theo lệnh của gia tộc Demidov, chỉ cách tháp nghiêng vài chục mét về phía tây bắc, và trong trang trí tháp chuông có nhắc lại các mô-típ của chính tháp nghiêng nổi tiếng. Với chiều cao tính cả chóp và thánh giá khoảng 64 mét, tháp chuông của nhà thờ vươn cao trên nền trời Nevyansk, thuộc hàng cao nhất vùng. Thời Xô Viết, nhà thờ bị đóng cửa, tháo dỡ mái vòm và biến thành xưởng cơ khí, gần như mất hết diện mạo ban đầu. Sau năm 2000, công trình được trùng tu quy mô lớn và trở lại là nhà thờ chính toà thứ hai của giáo phận Nizhny Tagil, phục hồi các mái vòm và tháp chuông. Ngày nay, du khách tới Nevyansk thường tham quan trọn cụm di tích: Tháp nghiêng, nhà thờ Chúa Biến Hình và bảo tàng địa phương – một hành trình sống động về lịch sử khai mỏ, đúc chuông và văn hoá Ural thế kỷ 18–19.",
    [
        "Đứng sát Tháp nghiêng Nevyansk, tạo thành quần thể lịch sử Demidov của thành phố.",
        "Khởi công 1824; tháp chuông cao ~64 m, thuộc hàng cao nhất vùng.",
        "Bị biến thành xưởng thời Xô Viết, trùng tu sau năm 2000 thành nhà thờ chính toà.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ, thường ban ngày; kiểm tra lịch của giáo phận.",
        "ticket_vi": "Vào nhà thờ miễn phí; vé tham quan Tháp nghiêng và bảo tàng tính riêng.",
        "duration_vi": "Khoảng 30–45 phút cho nhà thờ; nửa ngày cho cả cụm di tích.",
        "best_time_vi": "Quanh năm; kết hợp tham quan Tháp nghiêng liền kề.",
        "tips_vi": "Đi cùng vé tham quan Tháp nghiêng Nevyansk và bảo tàng để trọn vẹn câu chuyện Demidov; ăn mặc kín đáo khi vào nhà thờ.",
    },
    [
        {"title": "Wikipedia (RU) — Спасо-Преображенский собор (Невьянск)", "url": "https://ru.wikipedia.org/wiki/Спасо-Преображенский_собор_(Невьянск)"},
        {"title": "Соборы.ру — Невьянск, собор Преображения Господня", "url": "https://sobory.ru/article/?object=01204"},
    ],
    ["church", "orthodox-church", "demidov", "nevyansk", "architecture"],
    maps_text("Спасо-Преображенский собор", "Невьянск", "Spaso-Preobrazhensky Cathedral", "Nevyansk", 57.489598, 60.222402),
))

# 11) Нижнетагильский музей изобразительных искусств (Тагильская Мадонна) ------
RECORDS.append(rec(
    "nizhny-tagil-fine-arts-museum",
    "Bảo tàng Mỹ thuật Nizhny Tagil («Đức Mẹ Tagil»)",
    "Нижнетагильский музей изобразительных искусств",
    "Nizhny Tagil Museum of Fine Arts",
    ["museum"],
    57.905733, 59.955517,
    "Улица Уральская, 7, thành phố Nizhny Tagil, tỉnh Sverdlovsk, Nga.",
    "Bảo tàng mỹ thuật lớn thứ hai tỉnh Sverdlovsk, nổi tiếng nhờ bức «Đức Mẹ Tagil» (Thánh Gia) – bức tranh được cho là của danh hoạ Raffaello. Bộ sưu tập trải rộng từ hội hoạ Nga, châu Âu tới nghệ thuật sơn khay Tagil truyền thống.",
    "Thành lập năm 1944, Bảo tàng Mỹ thuật Nizhny Tagil là một trong những bảo tàng nghệ thuật quan trọng nhất vùng Ural, chỉ sau bảo tàng ở Yekaterinburg. Viên ngọc của bộ sưu tập là bức «Thánh Gia» – quen gọi «Đức Mẹ Tagil» (Тагильская Мадонна) – một bức tranh thế kỷ 16 mang chữ ký và niên đại 1509, được nhiều chuyên gia cho là tác phẩm thời trẻ của thiên tài Phục Hưng Raffaello. Bức tranh được phát hiện một cách tình cờ tại Nizhny Tagil vào năm 1924, khi người ta tìm thấy nó trong tình trạng hư hỏng, dùng che một ô cửa; sau khi phục chế, nó trở thành hiện vật gây chấn động và là niềm tự hào của bảo tàng. Bên cạnh «Đức Mẹ Tagil», bảo tàng còn trưng bày hội hoạ Nga thế kỷ 18–20, tranh châu Âu (Ý, Hà Lan, Flanders) và đặc biệt là bộ sưu tập nghệ thuật sơn khay kim loại Tagil (тагильский поднос) – nghề thủ công truyền thống lâu đời được xem là tiền thân của dòng khay sơn Zhostovo nổi tiếng. Đây là điểm đến hấp dẫn cho người yêu nghệ thuật khi ghé thăm «thủ phủ công nghiệp» Nizhny Tagil.",
    [
        "Sở hữu «Đức Mẹ Tagil» (Thánh Gia, ký 1509) – bức tranh được cho là của Raffaello.",
        "Bức tranh được tìm thấy tình cờ ở Nizhny Tagil năm 1924 trong tình trạng hư hỏng.",
        "Bộ sưu tập hội hoạ Nga – châu Âu và nghệ thuật sơn khay Tagil truyền thống.",
    ],
    {
        "hours_vi": "Thường mở 09:30–18:00, đóng cửa Thứ Hai (kiểm tra lịch chính thức).",
        "ticket_vi": "Có thu phí vé vào; nhiều mức giảm.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (không gian trong nhà).",
        "tips_vi": "Hỏi nhân viên vị trí trưng bày «Đức Mẹ Tagil»; kết hợp tham quan các bảo tàng công nghiệp của Nizhny Tagil.",
    },
    [
        {"title": "Нижнетагильский музей изобразительных искусств — trang chính thức", "url": "https://artmnt.ru/"},
        {"title": "Культура.РФ — Нижнетагильский музей изобразительных искусств", "url": "https://www.culture.ru/institutes/11960/nizhnetagilskii-muzei-izobrazitelnykh-iskusstv"},
    ],
    ["museum", "art", "tagil-madonna", "raphael", "nizhny-tagil"],
    maps_text("Нижнетагильский музей изобразительных искусств", "Нижний Тагил", "Nizhny Tagil Museum of Fine Arts", "Nizhny Tagil", 57.905733, 59.955517),
    official_site="https://artmnt.ru/",
))

# 12) Музей золота (Берёзовский) ----------------------------------------------
RECORDS.append(rec(
    "berezovsky-gold-museum",
    "Bảo tàng Vàng ở Berezovsky (Muzey zolota)",
    "Музей золота",
    "Gold Museum (Berezovsky)",
    ["museum"],
    56.912717, 60.801861,
    "Улица Коммуны, 4, thành phố Berezovsky (ngoại ô Yekaterinburg), tỉnh Sverdlovsk, Nga.",
    "Bảo tàng chuyên đề độc đáo tại Berezovsky – nơi được coi là cái nôi của ngành khai thác vàng quặng gốc ở Nga. Kể lại lịch sử «cơn sốt vàng» Ural qua năm gian trưng bày, từ hạt vàng đầu tiên tìm thấy năm 1745 tới đời sống thợ đãi vàng.",
    "Thành phố Berezovsky, sát ngay Yekaterinburg, có một vị trí đặc biệt trong lịch sử nước Nga: chính tại đây, năm 1745, người thợ Erofey Markov đã tìm thấy vàng, mở đầu cho ngành khai thác vàng quặng gốc (vàng nguyên sinh) đầu tiên của cả đế quốc Nga. Bảo tàng Vàng, thành lập năm 1970, kể lại toàn bộ câu chuyện hấp dẫn ấy. Năm gian trưng bày lần lượt dẫn khách qua: lịch sử khai thác vàng ở Ural, đời sống của những người thợ đãi vàng (старатели) thế kỷ 19, kiến thức khoa học về vàng như một nguyên tố và khoáng vật, cùng lịch sử phát triển của chính Berezovsky. Du khách được xem các mẫu quặng, dụng cụ đãi và khai mỏ, mô hình hầm lò, bản đồ, tài liệu và cả những câu chuyện đời thường thấm đẫm không khí «cơn sốt vàng». Nhiều chương trình còn cho khách trải nghiệm tự tay đãi vàng để hiểu công việc nhọc nhằn của thợ mỏ xưa. Kết hợp với «mỏ – bảo tàng» tham quan hầm lò gần đó, Berezovsky mang lại một trải nghiệm hiếm có về di sản khai khoáng đã làm nên sự giàu có của vùng Ural.",
    [
        "Đặt tại Berezovsky – nơi tìm thấy vàng quặng gốc đầu tiên của Nga (1745).",
        "Năm gian trưng bày về lịch sử khai thác vàng, đời thợ đãi vàng và khoáng vật học.",
        "Có chương trình cho khách tự tay trải nghiệm đãi vàng; gần «mỏ – bảo tàng» tham quan hầm lò.",
    ],
    {
        "hours_vi": "Thường mở 10:00–18:00, đóng cửa Thứ Hai (kiểm tra lịch chính thức).",
        "ticket_vi": "Vé vào phí thấp (khoảng 150 ₽ người lớn, giá tham khảo 2026); trải nghiệm đãi vàng có thể tính thêm.",
        "duration_vi": "Khoảng 1 giờ; lâu hơn nếu tham gia trải nghiệm đãi vàng.",
        "best_time_vi": "Quanh năm (không gian trong nhà).",
        "tips_vi": "Đặt trước nếu muốn thử đãi vàng; kết hợp tham quan mỏ – bảo tàng «Русское золото» gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Музей золота (Берёзовский)", "url": "https://ru.wikipedia.org/wiki/Музей_золота_(Берёзовский)"},
        {"title": "Музей золота — trang Bảo tàng địa phương tỉnh Sverdlovsk", "url": "https://uole-museum.ru/museums/muzej-zolota/"},
    ],
    ["museum", "gold-mining", "history", "berezovsky", "ural"],
    maps_org("https://yandex.com/maps/org/muzey_zolota/1200618198/", "Gold Museum", "Berezovsky"),
    official_site="https://uole-museum.ru/museums/muzej-zolota/",
))

# 13) Буддийский монастырь Шедруб Линг (гора Качканар) ------------------------
RECORDS.append(rec(
    "kachkanar-buddhist-monastery",
    "Tu viện Phật giáo Shad Tchup Ling trên núi Kachkanar",
    "Буддийский монастырь Шедруб Линг (Шад Тчуп Линг)",
    "Shad Tchup Ling Buddhist Monastery",
    ["other"],
    58.777173, 59.385043,
    "Trên sườn núi Kachkanar (gần thành phố Kachkanar và làng Kosya), tỉnh Sverdlovsk, Nga.",
    "Tu viện Phật giáo Tây Tạng duy nhất ở vùng Ural, nằm cheo leo trên sườn núi Kachkanar giữa những khối đá kỳ vĩ. Được xây dựng bền bỉ bằng tay từ năm 1995, là điểm hành hương – leo núi độc đáo với tầm nhìn bao la và các công trình sắc màu.",
    "Trên sườn núi Kachkanar ở phía bắc tỉnh Sverdlovsk có một điểm đến hết sức bất ngờ: tu viện Phật giáo Tây Tạng Shad Tchup Ling (còn phiên là Shedrub Ling) – ngôi chùa Phật giáo duy nhất và đầu tiên của cả vùng Ural. Tu viện do Mikhail Sannikov, một cựu quân nhân từng tham chiến ở Afghanistan (pháp danh lama Sanye Tenzin Dokshit), khởi dựng từ năm 1995 và kiên trì xây đắp gần như hoàn toàn bằng sức người suốt nhiều thập niên. Nằm ở độ cao khoảng 800 mét giữa những khối đá granit kỳ vĩ của đỉnh Kachkanar, quần thể gồm các gian nhà, bảo tháp (stupa), tượng Phật và cờ cầu nguyện đủ màu, tạo nên khung cảnh vừa tâm linh vừa siêu thực trên nền núi rừng Ural. Để tới nơi, du khách phải đi bộ leo núi khoảng 6–8 km, băng qua rừng taiga và những vỉa đá lô nhô; phần thưởng là không khí thanh tịnh và tầm nhìn khoáng đạt xuống cả vùng. Dù từng đối mặt nguy cơ bị di dời do nằm trong khu vực khai thác quặng, tu viện vẫn là biểu tượng của lòng bền bỉ và là một trong những trải nghiệm leo núi – hành hương đáng nhớ nhất của Ural. Khách tới thăm được đề nghị tôn trọng nếp sinh hoạt và sự tĩnh lặng của các nhà sư.",
    [
        "Tu viện Phật giáo Tây Tạng duy nhất ở vùng Ural, khởi dựng năm 1995.",
        "Nằm trên sườn núi Kachkanar (~800 m) giữa các khối đá granit; phải leo bộ 6–8 km để tới.",
        "Quần thể chùa, bảo tháp, tượng Phật và cờ cầu nguyện sắc màu, tầm nhìn bao la.",
    ],
    {
        "hours_vi": "Điểm hành hương ngoài trời; thuận lợi nhất vào mùa ấm, nên đi ban ngày.",
        "ticket_vi": "Không bán vé; khuyến khích đóng góp tuỳ tâm để duy trì tu viện.",
        "duration_vi": "Cả ngày (gồm 3–4 giờ leo núi mỗi chiều).",
        "best_time_vi": "Cuối tháng 6 đến tháng 9, khi đường mòn khô ráo và an toàn.",
        "tips_vi": "Chuẩn bị giày leo núi, nước, áo ấm và đồ mưa; tôn trọng sự tĩnh lặng, xin phép trước khi chụp ảnh nhà sư.",
    },
    [
        {"title": "Ураловед — Гора Качканар и буддийский монастырь", "url": "https://uraloved.ru/gora-kachkanar"},
        {"title": "Наш Урал — Качканар: буддийская обитель «Шедруб Линг»", "url": "https://nashural.ru/dostoprimechatelnosti-urala/kachkanar-buddijskaya-obitel-shedrub-ling-i-kamennyj-gorod/"},
    ],
    ["other", "buddhist", "mountain", "pilgrimage", "hiking", "kachkanar"],
    maps_text("Буддийский монастырь Шедруб Линг", "Качканар", "Shad Tchup Ling Buddhist Monastery", "Kachkanar", 58.777173, 59.385043),
))

# 14) Конжаковский Камень -----------------------------------------------------
RECORDS.append(rec(
    "konzhakovsky-kamen",
    "Núi Konzhakovsky Kamen (đỉnh cao nhất tỉnh)",
    "Конжаковский Камень",
    "Konzhakovsky Kamen",
    ["park_garden", "other"],
    59.61670, 59.13330,
    "Bắc Ural, gần thành phố Karpinsk, tây bắc tỉnh Sverdlovsk, Nga.",
    "Đỉnh núi cao nhất tỉnh Sverdlovsk (1.569 m), thuộc dãy Bắc Ural. Nổi tiếng với cảnh quan lãnh nguyên núi cao, đồng cỏ hoa, dòng suối trong và là điểm đến kinh điển của dân leo núi cùng giải marathon núi «Konzhak» thường niên.",
    "Konzhakovsky Kamen là mái nhà của tỉnh Sverdlovsk – đỉnh núi cao nhất vùng với độ cao 1.569 mét, nằm ở phần Bắc Ural gần thành phố Karpinsk. Tên núi gắn với người thợ săn dân tộc Mansi tên Konzhakov từng sống dưới chân núi. Đây là một khối núi lớn với nhiều đỉnh phụ, dòng sông Konzhakovka và các suối băng trong vắt, được giới leo núi Ural đặc biệt yêu thích. Hành trình chinh phục thường dài và nhiều tầng cảnh quan: từ rừng taiga rậm rạp dưới thấp, lên đai rừng thưa, rồi tới vùng lãnh nguyên núi cao (gольцы) với thảm rêu, địa y, đồng cỏ hoa mùa hè và những bãi đá tảng khổng lồ, cuối cùng là đỉnh trọc lộng gió với tầm nhìn mênh mông sang tận Kosvinsky Kamen và các dãy núi lân cận. Mỗi mùa hè, tuyến đường mòn nổi tiếng «Konzhakovsky marathon» (dài khoảng 42 km khứ hồi) thu hút hàng nghìn vận động viên chạy núi từ khắp nước Nga. Với người đi bộ đường dài, Konzhakovsky Kamen là một trong những chuyến trekking đáng giá nhất Ural, nhưng đòi hỏi thể lực tốt, chuẩn bị kỹ và tôn trọng thời tiết vốn thay đổi nhanh trên núi cao.",
    [
        "Đỉnh cao nhất tỉnh Sverdlovsk – 1.569 m, thuộc Bắc Ural.",
        "Cảnh quan nhiều tầng: taiga, rừng thưa, lãnh nguyên núi cao với bãi đá và đồng hoa.",
        "Tuyến chạy núi «Konzhakovsky marathon» (~42 km) thu hút hàng nghìn vận động viên mỗi hè.",
    ],
    {
        "hours_vi": "Khu núi tự nhiên; leo núi khả thi nhất vào mùa ấm, cần cả ngày hoặc cắm trại qua đêm.",
        "ticket_vi": "Không thu phí; là khu vực hoang dã, tự chịu trách nhiệm.",
        "duration_vi": "Trekking khứ hồi thường 2 ngày; vận động viên chạy có thể trong ngày.",
        "best_time_vi": "Tháng 7 đến đầu tháng 9 khi tuyết đã tan và thời tiết ổn định hơn.",
        "tips_vi": "Chuẩn bị lều, đồ ấm, đồ mưa và định vị GPS; thời tiết đỉnh núi đổi nhanh, xuất phát sớm và theo dõi dự báo.",
    },
    [
        {"title": "Wikipedia (EN) — Konzhakovskiy Kamen", "url": "https://en.wikipedia.org/wiki/Konzhakovskiy_Kamen"},
        {"title": "Wikidata — Konzhakovsky Kamen (Q4230794)", "url": "https://www.wikidata.org/wiki/Q4230794"},
    ],
    ["park_garden", "mountain", "hiking", "north-ural", "highest-peak"],
    maps_text("Конжаковский Камень", "Карпинск", "Konzhakovsky Kamen", "Karpinsk", 59.61670, 59.13330),
))

# 15) Казанская церковь (Арамашево, «Церковный камень») -----------------------
RECORDS.append(rec(
    "aramashevo-kazan-church",
    "Nhà thờ Đức Mẹ Kazan ở Aramashevo (trên «Đá Nhà thờ»)",
    "Церковь Казанской иконы Божией Матери (Арамашево)",
    "Church of the Kazan Icon (Aramashevo)",
    ["church"],
    57.608252, 61.737509,
    "Улица Совхозная, 6, làng Aramashevo, huyện Alapayevsky, tỉnh Sverdlovsk, Nga.",
    "Nhà thờ đá trắng nhỏ nhắn đứng chênh vênh trên vách đá cao 40 mét bên sông Rezh, được dân gian gọi là «Đá Nhà thờ». Một trong những khung cảnh nên thơ và được chụp ảnh nhiều nhất vùng Ural, do chính người dân địa phương phục dựng.",
    "Nằm ở làng cổ Aramashevo bên sông Rezh, cách Yekaterinburg khoảng 110 km, nhà thờ Đức Mẹ Kazan là một trong những công trình có vị trí ngoạn mục nhất tỉnh Sverdlovsk. Ngôi nhà thờ đá được xây năm 1800 trên đỉnh một vách đá dựng đứng cao khoảng 40 mét soi bóng xuống dòng Rezh – vách đá mà dân gian quen gọi là «Церковный камень» (Đá Nhà thờ). Vị trí này vốn là nơi đặt tiền đồn Aramashevo từ thế kỷ 17, giúp quan sát và phòng thủ trước các cuộc tập kích. Thời Xô Viết, nhà thờ bị đóng cửa năm 1929, tháo dỡ tháp chuông và dần hoang phế, lại thêm một trận hoả hoạn năm 1970 khiến công trình gần như đổ nát. Điều đặc biệt cảm động là từ năm 2005, chính người dân trong làng cùng cán bộ bảo tàng địa phương đã tự nguyện chung tay phục dựng nhà thờ; tới năm 2011 công trình cơ bản hồi sinh với tháp chuông được dựng lại. Ngày nay, nhà thờ trắng thanh thoát trên vách đá, với dòng sông uốn lượn và cánh đồng trải dài phía dưới, là điểm ngắm cảnh, chụp ảnh và hành hương yêu thích; du khách có thể leo lên vách «Đá Nhà thờ» để phóng tầm mắt ra toàn cảnh thung lũng Rezh thơ mộng.",
    [
        "Nhà thờ đá (1800) đứng trên vách «Đá Nhà thờ» cao ~40 m bên sông Rezh.",
        "Vốn là vị trí tiền đồn Aramashevo thế kỷ 17; bị đóng cửa 1929, cháy năm 1970.",
        "Được dân làng tự nguyện phục dựng từ 2005, hồi sinh khoảng năm 2011 – khung cảnh nên thơ bậc nhất Ural.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ và thoả thuận với giáo xứ; khuôn viên vách đá tham quan tự do ban ngày.",
        "ticket_vi": "Vào tự do; khuyến khích đóng góp tuỳ tâm.",
        "duration_vi": "Khoảng 30–45 phút; lâu hơn nếu leo vách đá ngắm cảnh.",
        "best_time_vi": "Cuối xuân đến đầu thu; sáng sớm hoặc chiều muộn cho ánh sáng đẹp chụp ảnh.",
        "tips_vi": "Cẩn thận khi lên mép vách đá; kết hợp tham quan bảo tàng làng Aramashevo và các vách đá Shaytan-kamen gần đó.",
    },
    [
        {"title": "Соборы.ру — Арамашево, Церковь Казанской Иконы Божией Матери", "url": "https://sobory.ru/article/?object=11369"},
        {"title": "Приход Казанской иконы — trang chính thức", "url": "https://hramaramashevo.cerkov.ru/"},
    ],
    ["church", "orthodox-church", "cliff", "rezh-river", "scenic", "aramashevo"],
    maps_text("Церковь Казанской иконы Божией Матери", "Арамашево", "Church of the Kazan Icon", "Aramashevo", 57.608252, 61.737509),
))


def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    existing_slugs = {p.get("slug") for p in data}
    existing_ids = {p.get("id") for p in data}

    added, skipped = [], []
    for r in RECORDS:
        if r["slug"] in existing_slugs or r["id"] in existing_ids:
            skipped.append(r["slug"])
            continue
        data.append(r)
        existing_slugs.add(r["slug"])
        existing_ids.add(r["id"])
        added.append(r["slug"])

    if added:
        bak = f"{path}.bak_add_{TS}"
        shutil.copyfile(path, bak)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Backup: {os.path.basename(bak)}")

    print(f"REGION={REGION}  ADDED={len(added)}  SKIPPED(dup)={len(skipped)}  TOTAL_NOW={len(data)}")
    if added:
        print("  + " + "\n  + ".join(added))
    if skipped:
        print("  (skip dup): " + ", ".join(skipped))


if __name__ == "__main__":
    main()
