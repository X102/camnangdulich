# -*- coding: utf-8 -*-
"""_add_places_astrakhan_20260728.py — VÙNG: Tỉnh Astrakhan (Астраханская область)
(lần chạy tự động 2026-07-28).

Bối cảnh: astrakhan.json hiện có 7 địa điểm. Bổ sung 24 địa điểm THẬT SỰ nổi tiếng/đặc
sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31 (≥30, mục tiêu 31–32).

Phân bố loại hình (24 bản ghi mới):
- museum (6): Астраханский краеведческий музей (музей-заповедник), Картинная галерея им.
  Догадина, Дом-музей Велимира Хлебникова, Дом купца Тетюшинова, Музей истории города,
  Музей боевой славы.
- other (2): Астраханский планетарий, Селитренное городище (столица Золотой Орды).
- church (6): Собор Святого Владимира, Покровский кафедральный собор, Иоанно-Предтеченский
  монастырь, Белая мечеть, Чёрная мечеть, Римско-католический храм Успения; + Хошеутовский
  хурул (буддийский, dùng "church").
- theatre (5): Театр оперы и балета, Драматический театр, Театр кукол, Театр юного зрителя,
  Астраханская филармония.
- monument (1): Памятник Петру I.
- park_garden (2): Лебединое озеро, Братский сад.
- square_street (1): Площадь Ленина.

TOẠ ĐỘ — xác minh chéo (ru.wikipedia geohack, 2ГИС карточка организации / og:image center,
sobory.ru, culture.ru, tonkosti/vetert, 2026-07-28). Phạm vi tỉnh Astrakhan: lat ~45–48,5;
lon ~44,5–49,5; các điểm nội thành quanh 46,34–46,36 / 48,01–48,06. Không đảo lat/lon:
  Краеведческий музей 46.349167,48.041389 (ru.wiki 46°20′57″N 48°02′29″E, Советская 15);
  Галерея Догадина 46.349200,48.051900 (Свердлова 81); Дом Хлебникова 46.351300,48.045700
  (Свердлова 53); Дом Тетюшинова 46.355000,48.043800 (Коммунистическая 26); Музей истории
  города 46.352100,48.031700 (Ульяновых 9); Музей боевой славы 46.351000,48.036500
  (Ахматовская 7); Планетарий 46.346400,48.022700 (Адмиралтейская 1/8); Собор Св. Владимира
  46.339100,48.016000 (sobory, Генерала Епишева 4); Покровский собор 46.363500,48.046400
  (sobory obj.01041, Покровская пл. 6); Иоанно-Предтеченский монастырь 46.349387,48.058458
  (Магнитогорская 9); Белая мечеть 46.342900,48.030700 (Зои Космодемьянской 41);
  Чёрная мечеть 46.343056,48.033333 (ru.wiki 46°20′35″N 48°02′00″E, Зои Космодемьянской 48);
  Католический храм 46.345900,48.051000 (Бабушкина 81); Театр оперы и балета 46.360329,
  48.044072 (2ГИС, Анри Барбюса 16); Драмтеатр 46.348280,48.044199 (2ГИС, Советская 28);
  Театр кукол 46.353171,48.030877 (2ГИС, Никольская 7/Фиолетова 12); ТЮЗ 46.346709,
  48.032494 (2ГИС, Мусы Джалиля 4); Филармония 46.350781,48.041091 (2ГИС, Молодой Гвардии
  ст1); Памятник Петру I 46.347153,48.015996 (Петровская наб.); Лебединое озеро 46.345980,
  48.023260; Площадь Ленина 46.347600,48.030200 (у кремля); Братский сад 46.350300,
  48.035000 (Советская 1); Хошеутовский хурул 46.927222,47.613333 (ru.wiki 46°55′38″N
  47°36′48″E, с. Речное, Харабалинский р-н); Селитренное городище 47.185000,47.425000
  (ru.wiki 47°11′06″N 47°25′30″E, с. Селитренное, Харабалинский р-н).

Ghi chú: đã LOẠI "Красная мечеть" (Казанская 62) và "Триумфальная арка" vì không xác minh
được toạ độ độc lập đáng tin (toạ độ Красная мечеть chỉ cách Чёрная мечеть ~40 m, nghi
trùng/geocode kém; Триумфальная арка không có bài wiki/nguồn toạ độ số).

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_astrakhan_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "astrakhan"
REGION_NAME_VI = "Tỉnh Astrakhan"
FD = "Vùng Nam"


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

# 1) Астраханский краеведческий музей (музей-заповедник) ---------------------------
RECORDS.append(rec(
    "astrakhan-museum-reserve",
    "Bảo tàng địa phương Astrakhan (musei-zapovednik)",
    "Астраханский государственный объединённый историко-архитектурный музей-заповедник",
    "Astrakhan Regional Museum (Museum-Reserve)",
    ["museum"],
    46.349167, 48.041389,
    "Ул. Советская, 15, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Là bảo tàng địa phương lâu đời nhất trong số các bảo tàng cấp vùng của nước Nga, khởi nguồn từ 'Bảo tàng tỉnh' năm 1837. Toà nhà chính bề thế đặt bộ sưu tập hơn 300.000 hiện vật về thiên nhiên, khảo cổ, dân tộc học vùng hạ lưu Volga, trong đó nổi tiếng nhất là kho vàng của người Sarmat.",
    "Ra đời từ năm 1837 dưới thời tỉnh trưởng Ivan Timiryazev, Bảo tàng địa phương Astrakhan được xem là bảo tàng cấp vùng cổ nhất nước Nga và là 'trái tim' của cả một tổ hợp bảo tàng-khu bảo tồn với 14 chi nhánh (trong đó có cả Điện Kremlin Astrakhan). Toà nhà chính là công trình 'Các cơ quan thành phố' xây dựng đầu thế kỷ 20, nay vừa là bảo tàng vừa là trụ sở hành chính tỉnh. Bộ sưu tập đồ sộ hơn 300.000 đơn vị trải rộng khắp các lĩnh vực: khảo cổ, tiền cổ (hơn 45.000 hiện vật), dân tộc học, ảnh tư liệu, vũ khí, cổ sinh vật học và thiên nhiên vùng châu thổ Volga–Caspi. Viên ngọc quý của bảo tàng là bộ sưu tập 'Vàng của người Sarmat' – những trang sức vàng, bạc tinh xảo thời Savromat–Sarmat và thời Kim Trướng hãn quốc, từng gây tiếng vang khi triển lãm tại Rome năm 2005. Với các gian trưng bày sinh động về 'Cá vùng Volga–Caspi', lịch sử vùng đất qua các thế kỷ và văn hoá đa sắc tộc, đây là điểm khởi đầu lý tưởng để du khách hiểu về Astrakhan – ngã tư giao thoa của các nền văn minh bên dòng Volga.",
    [
        "Bảo tàng cấp vùng lâu đời nhất nước Nga (khởi nguồn 1837), tổ hợp musei-zapovednik với 14 chi nhánh.",
        "Hơn 300.000 hiện vật; nổi bật bộ 'Vàng của người Sarmat' từng triển lãm tại Rome.",
        "Toà nhà 'Các cơ quan thành phố' đầu thế kỷ 20 ngay trung tâm, gần Điện Kremlin.",
    ],
    {
        "hours_vi": "Thường mở cửa thứ Ba–Chủ nhật, nghỉ thứ Hai; nên kiểm tra lịch theo mùa.",
        "ticket_vi": "Vé vào cửa giá bình dân; có phí riêng cho tour hướng dẫn và triển lãm chuyên đề.",
        "duration_vi": "Khoảng 1,5–2 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà); tiện kết hợp dạo trung tâm và Kremlin.",
        "tips_vi": "Nằm ngay trung tâm trên đường Sovetskaya, đi bộ tới Điện Kremlin và bờ kè; hỏi vé combo nhiều chi nhánh.",
    },
    [
        {"title": "Wikipedia (RU) — Астраханский краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Астраханский_краеведческий_музей"},
        {"title": "Astmuseum.ru — официальный сайт", "url": "https://astmuseum.ru"},
    ],
    ["museum", "museum-reserve", "local-history", "sarmatian-gold", "astrakhan", "volga"],
    maps_text("Астраханский краеведческий музей", "Астрахань", "Astrakhan Regional Museum", "Astrakhan", 46.349167, 48.041389),
    official_site="https://astmuseum.ru",
))

# 2) Астраханская картинная галерея им. П. М. Догадина -----------------------------
RECORDS.append(rec(
    "dogadin-art-gallery",
    "Bảo tàng mỹ thuật Astrakhan mang tên Dogadin (Kartinnaya galereya)",
    "Астраханская государственная картинная галерея имени П. М. Догадина",
    "Astrakhan (Dogadin) Art Gallery",
    ["museum"],
    46.349200, 48.051900,
    "Ул. Свердлова, 81, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Bảo tàng mỹ thuật hàng đầu vùng hạ lưu Volga, mở cửa từ năm 1918 dựa trên bộ sưu tập của nhà bảo trợ Pavel Dogadin. Trưng bày tranh của các bậc thầy Nga như Repin, Aivazovsky, Kustodiev, Vrubel trong một toà biệt thự cổ đẹp đầu thế kỷ 20.",
    "Bảo tàng mỹ thuật Astrakhan mang tên P. M. Dogadin ra đời năm 1918, khi kỹ sư và nhà sưu tầm Pavel Dogadin hiến tặng toàn bộ bộ sưu tập tranh của mình cho quê hương. Từ năm 1921, bảo tàng chuyển về toà nhà ba tầng nguy nga từng là dinh thự của thương gia Plotnikov trên phố Sverdlova – bản thân công trình đã là một di tích kiến trúc. Ngày nay đây là một trong những phòng tranh giàu có nhất vùng nam nước Nga, lưu giữ tác phẩm của các danh hoạ Nga lừng danh: Ilya Repin, Ivan Aivazovsky, Boris Kustodiev (người con của Astrakhan), Mikhail Vrubel, Valentin Serov cùng nhiều họa sĩ trường phái Avant-garde Nga đầu thế kỷ 20. Bên cạnh hội hoạ cổ điển Nga, bảo tàng còn có sưu tập nghệ thuật phương Tây, biểu tượng thánh (icon) và mỹ thuật trang trí. Không gian trưng bày ấm cúng, ánh sáng dịu và những bức tranh chất lượng bảo tàng khiến nơi đây trở thành điểm đến không thể bỏ qua với người yêu nghệ thuật khi tới Astrakhan.",
    [
        "Phòng tranh hàng đầu hạ lưu Volga, mở cửa 1918 từ bộ sưu tập của nhà bảo trợ Dogadin.",
        "Trưng bày Repin, Aivazovsky, Kustodiev, Vrubel, Serov cùng Avant-garde Nga đầu thế kỷ 20.",
        "Đặt trong dinh thự cổ của thương gia Plotnikov – di tích kiến trúc đầu thế kỷ 20.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, nghỉ thứ Hai; một số ngày mở muộn hơn.",
        "ticket_vi": "Vé vào cửa giá bình dân; có phí riêng cho triển lãm chuyên đề và tour.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Nằm gần các bảo tàng khác ở trung tâm; kết hợp thăm Dom-muzei Khlebnikov gần đó.",
    },
    [
        {"title": "Culture.ru — Астраханская картинная галерея им. П. М. Догадина", "url": "https://www.culture.ru/institutes/12000/astrakhanskaya-gosudarstvennaya-kartinnaya-galereya-imeni-p-m-dogadina"},
        {"title": "Dogadinka.ru — официальный сайт", "url": "https://dogadinka.ru/"},
    ],
    ["museum", "art-gallery", "painting", "repin", "kustodiev", "astrakhan"],
    maps_text("Картинная галерея им. Догадина", "Астрахань", "Dogadin Art Gallery", "Astrakhan", 46.349200, 48.051900),
    official_site="https://dogadinka.ru/",
))

# 3) Дом-музей Велимира Хлебникова -------------------------------------------------
RECORDS.append(rec(
    "khlebnikov-house-museum",
    "Nhà lưu niệm nhà thơ Velimir Khlebnikov",
    "Дом-музей Велимира Хлебникова",
    "Velimir Khlebnikov House Museum",
    ["museum"],
    46.351300, 48.045700,
    "Ул. Свердлова, 53, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Bảo tàng tưởng niệm nhà thơ Vị lai (Futurist) lừng danh Velimir Khlebnikov, đặt trong căn hộ xưa của gia đình ông. Nơi lưu giữ thư viện gia đình, di vật, bản thảo và những ấn phẩm gốc của một trong những nhà cách tân thi ca Nga đầu thế kỷ 20.",
    "Velimir Khlebnikov (1885–1922) là một trong những nhà thơ tiên phong táo bạo nhất của trào lưu Vị lai (Futurism) Nga, người mê mải sáng tạo ra 'ngôn ngữ ngoài lý trí' (zaum) và có ảnh hưởng sâu rộng tới thơ ca hiện đại. Ngôi nhà-bảo tàng mở cửa năm 1993, đặt ngay trong căn hộ trên phố Sverdlova nơi cha mẹ nhà thơ từng sinh sống và là điểm dừng chân của ông mỗi khi trở về Astrakhan. Đây là bảo tàng độc nhất trên thế giới dành cho Khlebnikov. Không gian mang hai lớp: phần tưởng niệm tái hiện nếp sinh hoạt của gia đình trí thức Nga cuối thế kỷ 19 – đầu thế kỷ 20 với thư viện, đồ đạc, tài liệu và các ấn phẩm xuất bản khi nhà thơ còn sống; phần trưng bày văn học – nghệ thuật giới thiệu di sản thi ca độc đáo của ông cùng mối liên hệ với các hoạ sĩ, nhà thơ Avant-garde cùng thời. Yên tĩnh và giàu chiều sâu, bảo tàng là điểm đến quý cho những ai yêu văn chương và muốn chạm vào tinh thần cách tân của nghệ thuật Nga đầu thế kỷ 20.",
    [
        "Bảo tàng duy nhất trên thế giới về nhà thơ Vị lai Velimir Khlebnikov (mở cửa 1993).",
        "Đặt trong căn hộ xưa của gia đình nhà thơ; lưu giữ thư viện, di vật và ấn phẩm gốc.",
        "Kể câu chuyện thi ca cách tân và giới nghệ sĩ Avant-garge Nga đầu thế kỷ 20.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật (khoảng 9:30–17:00), nghỉ thứ Hai.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Nằm gần Phòng tranh Dogadin; phù hợp người yêu văn học và lịch sử nghệ thuật.",
    },
    [
        {"title": "Culture.ru — Дом-музей Велимира Хлебникова", "url": "https://www.culture.ru/institutes/11453/dom-muzei-velimira-khlebnikova"},
        {"title": "Domvelimira.ru — официальный сайт", "url": "https://www.domvelimira.ru/"},
    ],
    ["museum", "house-museum", "literature", "khlebnikov", "futurism", "astrakhan"],
    maps_text("Дом-музей Велимира Хлебникова", "Астрахань", "Khlebnikov House Museum", "Astrakhan", 46.351300, 48.045700),
    official_site="https://www.domvelimira.ru/",
))

# 4) Дом купца Г. В. Тетюшинова ----------------------------------------------------
RECORDS.append(rec(
    "tetyushinov-house",
    "Nhà gỗ thương gia Tetyushinov (Dom kuptsa Tetyushinova)",
    "Дом купца Г. В. Тетюшинова",
    "Merchant Tetyushinov's House",
    ["museum"],
    46.355000, 48.043800,
    "Ул. Коммунистическая, 26, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Dinh thự gỗ chạm khắc tinh xảo của thương gia Tetyushinov, xây năm 1872 – một trong những công trình kiến trúc gỗ đẹp và hiếm còn sót lại ở Astrakhan. Nay là bảo tàng tái hiện nếp sống của giới thương nhân Nga cuối thế kỷ 19.",
    "Giữa trung tâm Astrakhan, ngôi nhà gỗ hai tầng với ban công chạm ren, mái đua và những đường trang trí cầu kỳ của thương gia Grigory Tetyushinov nổi bật như một viên ngọc của kiến trúc gỗ Nga. Được xây dựng năm 1872 theo phong cách 'nhà gỗ thị dân' đặc trưng, đây là một trong số rất ít dinh thự gỗ nguyên bản còn giữ được ở thành phố. Sau thời gian dài xuống cấp, công trình đã được trùng tu công phu và mở cửa thành bảo tàng, tái hiện sinh động không gian sống của một gia đình thương nhân Astrakhan cuối thế kỷ 19: phòng khách, phòng làm việc, đồ nội thất, vật dụng và cả sân trong đặc trưng. Bảo tàng thường tổ chức các chương trình trải nghiệm, trà đạo và lễ hội dân gian, giúp du khách hình dung rõ nét đời sống thị dân sung túc thời hoàng kim thương mại của thành phố cửa ngõ Caspi. Với vẻ đẹp mộc mạc và giá trị di sản hiếm có, ngôi nhà Tetyushinov là điểm dừng chân thú vị để cảm nhận một Astrakhan xưa cũ, duyên dáng.",
    [
        "Dinh thự gỗ chạm khắc tinh xảo của thương gia Tetyushinov, xây năm 1872.",
        "Một trong số ít công trình kiến trúc gỗ nguyên bản còn lại ở Astrakhan.",
        "Tái hiện nếp sống thương nhân thế kỷ 19 với các chương trình trải nghiệm, trà đạo.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn và chương trình trải nghiệm.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm; đẹp nhất khi có sự kiện dân gian.",
        "tips_vi": "Chú ý các chi tiết chạm gỗ ngoài mặt tiền; kết hợp dạo trung tâm lịch sử.",
    },
    [
        {"title": "Tonkosti — Дом купца Тетюшинова", "url": "https://tonkosti.ru/Дом_купца_Тетюшинова"},
        {"title": "Astmuseum.ru — филиалы музея-заповедника", "url": "https://astmuseum.ru"},
    ],
    ["museum", "wooden-architecture", "merchant-house", "heritage", "astrakhan"],
    maps_text("Дом купца Тетюшинова", "Астрахань", "Merchant Tetyushinov House", "Astrakhan", 46.355000, 48.043800),
))

# 5) Музей истории города Астрахани ------------------------------------------------
RECORDS.append(rec(
    "astrakhan-city-history-museum",
    "Bảo tàng lịch sử thành phố Astrakhan",
    "Музей истории города Астрахани",
    "Museum of the History of Astrakhan",
    ["museum"],
    46.352100, 48.031700,
    "Ул. Ульяновых, 9, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Bảo tàng chuyên sâu về lịch sử phát triển của chính thành phố Astrakhan, đặt trong ngôi nhà từng gắn với gia đình Ulyanov. Kể câu chuyện từ pháo đài bên Volga tới đô thị đa sắc tộc phồn thịnh của vùng Caspi.",
    "Nằm trong một toà nhà cổ ở trung tâm (vốn là Dom-muzei Ulyanovых), Bảo tàng lịch sử thành phố Astrakhan tập trung kể riêng câu chuyện của đô thị cửa ngõ phương Nam này. Qua các gian trưng bày, du khách theo dòng thời gian từ khi Astrakhan hình thành như một pháo đài trấn giữ nơi Volga đổ ra biển Caspi, trở thành trung tâm thương mại sầm uất trên tuyến giao thương Á–Âu, cho tới thời kỳ hiện đại. Bảo tàng làm nổi bật bản sắc đa sắc tộc, đa tôn giáo độc đáo của thành phố – nơi người Nga, Tatar, Kazakh, Armenia, Ba Tư, Ấn Độ cùng sinh sống và buôn bán qua nhiều thế kỷ, để lại dấu ấn ở các khu phố thương nhân, nhà thờ, đền và giáo đường. Các hiện vật đời thường, ảnh tư liệu, bản đồ và mô hình giúp tái hiện diện mạo đô thị qua từng giai đoạn. Đây là điểm đến lý tưởng để hiểu vì sao Astrakhan được ví như 'cửa ngõ phương Đông' của nước Nga và cảm nhận nhịp sống đa văn hoá đặc trưng của vùng hạ lưu Volga.",
    [
        "Bảo tàng chuyên về lịch sử phát triển của thành phố Astrakhan.",
        "Nhấn mạnh bản sắc đa sắc tộc, đa tôn giáo của đô thị thương mại bên Volga.",
        "Đặt trong toà nhà cổ trung tâm (nguyên là Dom-muzei Ulyanovых).",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nghỉ một ngày đầu tuần.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "Khoảng 1 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Kết hợp với Bảo tàng địa phương chính và dạo trung tâm lịch sử.",
    },
    [
        {"title": "Astmuseum.ru — Музей истории города", "url": "https://astmuseum.ru"},
        {"title": "Wikipedia (RU) — Астраханский краеведческий музей (филиалы)", "url": "https://ru.wikipedia.org/wiki/Астраханский_краеведческий_музей"},
    ],
    ["museum", "city-history", "multicultural", "astrakhan", "volga"],
    maps_text("Музей истории города Астрахани", "Астрахань", "Museum of History of Astrakhan", "Astrakhan", 46.352100, 48.031700),
))

# 6) Музей боевой славы ------------------------------------------------------------
RECORDS.append(rec(
    "military-glory-museum",
    "Bảo tàng Vinh quang Chiến trận (Muzei boevoi slavy)",
    "Музей боевой славы",
    "Museum of Military Glory",
    ["museum"],
    46.351000, 48.036500,
    "Ул. Ахматовская, 7, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Bảo tàng tưởng niệm truyền thống quân sự và chiến công của người dân vùng Astrakhan, đặc biệt trong Thế chiến II khi thành phố là hậu phương và tuyến phòng thủ quan trọng gần Stalingrad. Trưng bày vũ khí, quân trang, tư liệu và mô hình chiến trận.",
    "Bảo tàng Vinh quang Chiến trận ở Astrakhan dành để tôn vinh truyền thống quân sự và những đóng góp, hy sinh của người dân vùng đất này qua các cuộc chiến, mà nổi bật nhất là Chiến tranh Vệ quốc Vĩ đại (Thế chiến II). Nằm không xa Stalingrad (Volgograd ngày nay), trong những năm 1942–1943 Astrakhan là hậu phương trọng yếu, tuyến phòng thủ và điểm trung chuyển dầu, quân nhu cho mặt trận phía nam. Các gian trưng bày giới thiệu vũ khí, quân phục, huân chương, thư từ, ảnh tư liệu và mô hình các trận đánh, kể lại câu chuyện của những người lính và người dân thường vùng hạ lưu Volga. Bảo tàng cũng nhắc tới các đơn vị quân đội gắn với địa phương và những người con Astrakhan được phong Anh hùng. Đây là nơi giàu tính giáo dục, giúp du khách và các thế hệ trẻ hiểu về vai trò của vùng đất này trong lịch sử chiến tranh và tưởng nhớ những người đã ngã xuống.",
    [
        "Bảo tàng tôn vinh truyền thống quân sự và chiến công của vùng Astrakhan.",
        "Nhấn mạnh vai trò hậu phương – phòng thủ của thành phố trong Thế chiến II, gần Stalingrad.",
        "Trưng bày vũ khí, quân trang, huân chương, tư liệu và mô hình chiến trận.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nghỉ một ngày đầu tuần.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà); ý nghĩa dịp 9/5 (Ngày Chiến thắng).",
        "tips_vi": "Phù hợp người quan tâm lịch sử quân sự; kết hợp dạo trung tâm lịch sử.",
    },
    [
        {"title": "Vetert.ru — Музей боевой славы (Астрахань)", "url": "https://vetert.ru/rossiya/astrakhan/sights/509-muzej-boevoj-slavy.php"},
        {"title": "Astmuseum.ru — филиалы музея-заповедника", "url": "https://astmuseum.ru"},
    ],
    ["museum", "military", "wwii", "memorial", "astrakhan"],
    maps_text("Музей боевой славы", "Астрахань", "Museum of Military Glory", "Astrakhan", 46.351000, 48.036500),
))

# 7) Астраханский планетарий -------------------------------------------------------
RECORDS.append(rec(
    "astrakhan-planetarium",
    "Đài thiên văn – Cung thiên văn Astrakhan (Planetarii)",
    "Астраханский планетарий",
    "Astrakhan Planetarium",
    ["other"],
    46.346400, 48.022700,
    "Ул. Адмиралтейская, 1/8, trung tâm thành phố Astrakhan, gần hồ Lebedinoe, tỉnh Astrakhan, Nga.",
    "Cung thiên văn của Astrakhan, điểm đến giáo dục – giải trí về thiên văn học được nhiều gia đình và học sinh yêu thích. Các buổi trình chiếu vòm sao và chương trình khám phá vũ trụ diễn ra ngay gần hồ Thiên nga.",
    "Cung thiên văn Astrakhan là một trong những điểm đến khoa học – giáo dục được yêu thích của thành phố, đặc biệt với các gia đình có trẻ nhỏ và học sinh. Dưới mái vòm chiếu sao, khách tham quan được đưa vào những hành trình khám phá bầu trời đêm, hệ Mặt Trời, các chòm sao và những hiện tượng thiên văn kỳ thú qua các buổi trình chiếu và thuyết minh sinh động. Bên cạnh chương trình về vũ trụ, cung thiên văn còn tổ chức các bài giảng, hoạt động tương tác và triển lãm nhỏ giúp khơi gợi niềm say mê khoa học. Vị trí thuận tiện ngay khu trung tâm, gần hồ Thiên nga (Lebedinoe ozero) và Điện Kremlin, khiến nơi đây dễ dàng kết hợp trong một buổi dạo chơi khám phá thành phố. Đây là điểm dừng chân nhẹ nhàng, bổ ích, mang lại trải nghiệm khác biệt so với các bảo tàng lịch sử và công trình tôn giáo trong vùng.",
    [
        "Cung thiên văn với các buổi trình chiếu vòm sao và chương trình khám phá vũ trụ.",
        "Điểm đến giáo dục – giải trí được các gia đình và học sinh yêu thích.",
        "Vị trí trung tâm, gần hồ Thiên nga và Điện Kremlin, tiện kết hợp tham quan.",
    ],
    {
        "hours_vi": "Mở theo lịch buổi chiếu (thường ban ngày và cuối tuần); nên kiểm tra lịch trước.",
        "ticket_vi": "Vé theo buổi chiếu, giá bình dân; ưu đãi cho học sinh và nhóm.",
        "duration_vi": "Khoảng 45–60 phút mỗi buổi.",
        "best_time_vi": "Quanh năm (trong nhà); tiện đi cùng chuyến dạo hồ Thiên nga.",
        "tips_vi": "Đặt/kiểm tra lịch buổi chiếu trước khi tới; phù hợp gia đình có trẻ em.",
    },
    [
        {"title": "Vetert.ru — Астраханский планетарий", "url": "https://vetert.ru/rossiya/astrakhan/sights/514-planetarij.php"},
    ],
    ["planetarium", "science", "family", "education", "astrakhan"],
    maps_text("Астраханский планетарий", "Астрахань", "Astrakhan Planetarium", "Astrakhan", 46.346400, 48.022700),
))

# 8) Собор Святого Владимира (Князь-Владимирский) ----------------------------------
RECORDS.append(rec(
    "vladimir-cathedral",
    "Nhà thờ Thánh Vladimir (Knyaz-Vladimirsky sobor)",
    "Собор Святого Владимира",
    "St. Vladimir's Cathedral (Astrakhan)",
    ["church"],
    46.339100, 48.016000,
    "Ул. Генерала Епишева, 4, thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Nhà thờ Chính Thống giáo bằng gạch đỏ đồ sộ, xây năm 1895–1902 để kỷ niệm 900 năm nước Nga đón Chính Thống giáo (thời Thánh Vladimir). Là một trong những 'danh thiếp' kiến trúc của Astrakhan với những vòm bạc và mặt tiền tráng lệ.",
    "Vươn cao giữa thành phố với khối gạch đỏ trầm ấm và những mái vòm ánh bạc, Nhà thờ Thánh Vladimir là một trong những công trình tôn giáo đẹp và dễ nhận biết nhất Astrakhan. Nhà thờ được xây dựng trong các năm 1895–1902 bởi hai kỹ sư – kiến trúc sư người Saint Petersburg là Vasily Kosyakov và Nikolai Ikavitts, nhằm kỷ niệm 900 năm sự kiện Đại công Vladimir đưa Chính Thống giáo về nước Nga. Với kiến trúc theo phong cách 'Nga – Byzantine', thánh đường phô diễn những mảng trang trí gạch tinh tế, các cửa vòm, tháp chuông và hệ mái vòm đặc trưng. Thời Xô-viết, nhà thờ từng bị đóng cửa và suýt bị phá; có giai đoạn nơi đây bị biến thành nhà kho, trạm xe buýt, khiến công trình xuống cấp nặng, trước khi được trao trả và trùng tu, khôi phục lại vẻ đẹp nguyên bản. Ngày nay, nhà thờ mang quy chế 'archiery podvorye' (sân giám mục) của giáo phận Astrakhan, vừa là nơi hành lễ sầm uất, vừa là điểm tham quan kiến trúc mà du khách khó bỏ qua khi tới thành phố.",
    [
        "Thánh đường gạch đỏ đồ sộ (1895–1902), phong cách Nga – Byzantine, một 'danh thiếp' của Astrakhan.",
        "Xây để kỷ niệm 900 năm nước Nga đón Chính Thống giáo thời Thánh Vladimir.",
        "Từng bị đóng cửa và xuống cấp thời Xô-viết, nay đã được trùng tu, trả lại vẻ tráng lệ.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp lễ lớn của Chính Thống giáo.",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; giữ yên lặng và xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Wikipedia (RU) — Собор Святого Владимира (Астрахань)", "url": "https://ru.wikipedia.org/wiki/Собор_Святого_Владимира_(Астрахань)"},
        {"title": "Sobory.ru — Собор Владимира равноапостольного", "url": "https://sobory.ru/article/?object=02861"},
    ],
    ["church", "cathedral", "orthodox", "red-brick", "russian-byzantine", "astrakhan"],
    maps_text("Собор Святого Владимира", "Астрахань", "St. Vladimir Cathedral", "Astrakhan", 46.339100, 48.016000),
))

# 9) Покровский кафедральный собор -------------------------------------------------
RECORDS.append(rec(
    "pokrovsky-cathedral",
    "Nhà thờ chính toà Che Chở (Pokrovsky sobor)",
    "Покровский кафедральный собор",
    "Cathedral of the Intercession (Pokrovsky)",
    ["church"],
    46.363500, 48.046400,
    "Покровская площадь, 6, thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Nhà thờ chính toà hiện nay của giáo phận Astrakhan, mang tên lễ Đức Mẹ Che Chở (Pokrov). Ngôi thánh đường năm vòm trắng – vàng ở khu Pokrovskaya là trung tâm sinh hoạt tôn giáo Chính Thống lớn của thành phố.",
    "Nhà thờ chính toà Che Chở (Pokrovsky sobor) là nhà thờ cathedra hiện nay của giáo phận Astrakhan, mang tên ngày lễ Đức Mẹ Che Chở (Pokrov Presvyatoy Bogoroditsy) rất được tôn kính trong Chính Thống giáo Nga. Toạ lạc tại quảng trường Pokrovskaya ở phần bắc trung tâm thành phố, ngôi thánh đường nổi bật với khối kiến trúc năm vòm cân đối, tường sáng màu điểm những đường viền trang trí và tháp chuông vươn cao. Trải qua thời kỳ Xô-viết đầy biến động khi nhiều nhà thờ bị đóng cửa, Pokrovsky sobor vẫn giữ được vai trò trung tâm và trở thành nơi đặt ngai toà của giám mục giáo phận. Bên trong, nhà thờ lưu giữ nhiều thánh tượng được tôn kính và là nơi diễn ra các nghi lễ trọng thể, thu hút đông đảo giáo dân địa phương. Với du khách, đây là điểm đến để chiêm ngưỡng kiến trúc nhà thờ Chính Thống, cảm nhận không khí sùng đạo và tìm hiểu đời sống tâm linh của cộng đồng Chính Thống giáo ở thành phố đa tôn giáo bên dòng Volga.",
    [
        "Nhà thờ chính toà (cathedra) hiện nay của giáo phận Astrakhan.",
        "Mang tên lễ Đức Mẹ Che Chở (Pokrov), rất được tôn kính trong Chính Thống giáo.",
        "Thánh đường năm vòm ở quảng trường Pokrovskaya, trung tâm sinh hoạt tôn giáo lớn.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp lễ lớn, nhất là lễ Pokrov (tháng 10).",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; giữ yên lặng và xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Sobory.ru — Астрахань, Покровский кафедральный собор", "url": "https://sobory.ru/article/?object=01041"},
        {"title": "Wikipedia (RU) — Покровский собор (Астрахань)", "url": "https://ru.wikipedia.org/wiki/Покровский_собор_(Астрахань)"},
    ],
    ["church", "cathedral", "orthodox", "intercession", "astrakhan"],
    maps_text("Покровский кафедральный собор", "Астрахань", "Pokrovsky Cathedral", "Astrakhan", 46.363500, 48.046400),
))

# 10) Иоанно-Предтеченский монастырь -----------------------------------------------
RECORDS.append(rec(
    "john-baptist-monastery",
    "Tu viện Thánh Gioan Tiền Hô (Ioanno-Predtechensky)",
    "Иоанно-Предтеченский монастырь",
    "St. John the Baptist Monastery (Astrakhan)",
    ["church"],
    46.349387, 48.058458,
    "Ул. Магнитогорская, 9, thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Tu viện Chính Thống giáo cổ của Astrakhan, thành lập cuối thế kỷ 17. Quần thể nhà thờ gạch đỏ với những vòm xanh là một trong những trung tâm tu hành lâu đời và thanh tịnh của thành phố.",
    "Được thành lập vào khoảng cuối thế kỷ 17 (thập niên 1680) dưới thời Tổng giám mục Savvaty, Tu viện Thánh Gioan Tiền Hô là một trong những tu viện Chính Thống giáo cổ kính của Astrakhan. Quần thể tu viện với nhà thờ gạch đỏ, các vòm mái xanh lam điểm sao vàng và tường rào cổ tạo nên một không gian tĩnh lặng, trang nghiêm giữa lòng thành phố. Trải qua thời kỳ Xô-viết, tu viện bị đóng cửa và chịu nhiều hư hại, các công trình từng bị trưng dụng cho mục đích khác; đến những thập niên gần đây mới được khôi phục hoạt động tôn giáo và trùng tu dần dần. Ngày nay, đây vừa là nơi tu hành của các tu sĩ, vừa là điểm hành hương và tham quan cho những ai muốn tìm hiểu truyền thống đan tu Chính Thống. Không gian yên bình, kiến trúc nhà thờ nhiều mái vòm đặc trưng và bầu không khí sùng đạo khiến tu viện trở thành một điểm dừng chân ý nghĩa, bổ sung cho bức tranh tôn giáo đa dạng của thành phố bên sông Volga.",
    [
        "Tu viện Chính Thống giáo cổ của Astrakhan, thành lập cuối thế kỷ 17.",
        "Quần thể nhà thờ gạch đỏ với những vòm mái xanh lam điểm sao vàng.",
        "Từng bị đóng cửa thời Xô-viết, nay đã khôi phục hoạt động tu hành và hành hương.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ; nên tới vào ban ngày.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp lễ Chính Thống giáo.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn; giữ trật tự và tôn trọng sinh hoạt của các tu sĩ.",
    },
    [
        {"title": "Wikipedia (RU) — Иоанно-Предтеченский монастырь (Астрахань)", "url": "https://ru.wikipedia.org/wiki/Иоанно-Предтеченский_монастырь_(Астрахань)"},
        {"title": "Ioanno.ru — официальный сайт монастыря", "url": "https://www.ioanno.ru/"},
    ],
    ["church", "monastery", "orthodox", "heritage", "astrakhan"],
    maps_text("Иоанно-Предтеченский монастырь", "Астрахань", "St. John the Baptist Monastery", "Astrakhan", 46.349387, 48.058458),
    official_site="https://www.ioanno.ru/",
))

# 11) Белая мечеть (Ак-мечеть) -----------------------------------------------------
RECORDS.append(rec(
    "white-mosque",
    "Nhà thờ Hồi giáo Trắng (Belaya mechet / Ak-mechet)",
    "Белая мечеть",
    "White Mosque (Ak Mosque, Astrakhan)",
    ["church"],
    46.342900, 48.030700,
    "Ул. Зои Космодемьянской, 41/15, khu Tatar cũ, thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Một trong những nhà thờ Hồi giáo lâu đời và tiêu biểu nhất Astrakhan, nằm ở khu phố Tatar lịch sử. Ngôi Ak-mechet trắng với tháp minaret thanh mảnh là trung tâm tôn giáo quan trọng của cộng đồng Hồi giáo địa phương.",
    "Astrakhan từ lâu là thành phố đa tôn giáo, nơi cộng đồng Tatar và các dân tộc theo đạo Hồi sinh sống đông đúc, và Nhà thờ Hồi giáo Trắng (Ak-mechet) là một trong những biểu tượng tôn giáo lâu đời nhất của họ. Toạ lạc tại khu phố Tatar lịch sử quanh phố Zoi Kosmodemyanskoy, ngôi đền được xây bằng gạch, quét vôi trắng, với khối nhà cầu nguyện mái vòm và tháp minaret vươn cao thanh thoát – nét kiến trúc Hồi giáo đặc trưng nổi bật giữa những dãy nhà cổ. Được dựng từ cuối thế kỷ 18 – đầu thế kỷ 19 và nhiều lần tu sửa, Ak-mechet từng là một trong các nhà thờ Hồi giáo trung tâm của thành phố, nơi cộng đồng tụ họp cầu nguyện và sinh hoạt. Cùng với các nhà thờ Hồi giáo lân cận (như Chёrnaya mechet), nơi đây tạo nên một cụm di sản Hồi giáo độc đáo, minh chứng cho lịch sử chung sống hoà hợp giữa các tín ngưỡng ở Astrakhan. Với du khách, ghé thăm Ak-mechet là dịp để cảm nhận chiều sâu văn hoá phương Đông trong lòng thành phố Nga bên bờ Caspi.",
    [
        "Một trong những nhà thờ Hồi giáo lâu đời, tiêu biểu nhất Astrakhan (Ak-mechet).",
        "Nằm ở khu phố Tatar lịch sử, ngôi đền trắng với tháp minaret thanh mảnh.",
        "Trung tâm tôn giáo của cộng đồng Hồi giáo Tatar, biểu tượng thành phố đa tín ngưỡng.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ cầu nguyện; du khách nên tới ngoài giờ lễ và xin phép.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Ban ngày ngoài giờ cầu nguyện; tránh giờ lễ thứ Sáu đông đúc.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn; bỏ giày khi vào; giữ yên lặng và tôn trọng người hành lễ.",
    },
    [
        {"title": "Ruwiki — Белая мечеть (Астрахань)", "url": "https://ru.ruwiki.ru/wiki/Белая_мечеть_(Астрахань)"},
        {"title": "Wikipedia (RU) — Исторические мечети Астрахани", "url": "https://ru.wikipedia.org/wiki/Исторические_мечети_Астрахани"},
    ],
    ["church", "mosque", "islam", "tatar", "heritage", "astrakhan"],
    maps_text("Белая мечеть", "Астрахань", "White Mosque Ak Mosque", "Astrakhan", 46.342900, 48.030700),
))

# 12) Чёрная мечеть (Кара-мечеть) --------------------------------------------------
RECORDS.append(rec(
    "black-mosque",
    "Nhà thờ Hồi giáo Đen (Chёrnaya mechet / Kara-mechet)",
    "Чёрная мечеть",
    "Black Mosque (Kara Mosque, Astrakhan)",
    ["church"],
    46.343056, 48.033333,
    "Ул. Зои Космодемьянской, 48, khu Tatar cũ, thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Một trong những nhà thờ Hồi giáo cổ nhất Astrakhan, xây bằng đá năm 1816 trên nền một đền gỗ trước đó. Từng là nhà thờ chính của 'sân Bukhara' – cộng đồng thương nhân Trung Á ở thành phố.",
    "Nhà thờ Hồi giáo Đen (Kara-mechet) là một trong những đền thờ Hồi giáo cổ kính nhất còn lại của Astrakhan. Được xây bằng đá vào năm 1816 nhờ công đức của thương gia Yakupov, trên nền một ngôi đền gỗ cũ, nhà thờ từng đóng vai trò 'sobornaya mechet' (thánh đường chính) của 'sân Bukhara' – khu vực sinh sống và buôn bán của các thương nhân đến từ Trung Á. Điều này phản ánh vị thế của Astrakhan như một điểm nút giao thương Á–Âu, nơi hội tụ nhiều cộng đồng phương Đông. Đầu thế kỷ 20, giáo xứ nhà thờ có tới hơn 1.200 tín đồ. Thời Xô-viết, đền bị đóng cửa (năm 1930), chuyển thành trường học rồi dần đổ nát; mãi tới các năm 2005–2008 mới được khôi phục từ đống hoang tàn. Ngày nay, Kara-mechet là một di tích kiến trúc – tôn giáo cấp vùng, nằm trong cụm nhà thờ Hồi giáo cổ ở khu phố Tatar cùng với Ak-mechet trắng. Ghé thăm nơi đây, du khách cảm nhận rõ dấu ấn văn hoá Hồi giáo và lịch sử thương mại Á–Âu đã hoà quyện vào bản sắc của thành phố bên Volga.",
    [
        "Một trong những nhà thờ Hồi giáo cổ nhất Astrakhan, xây bằng đá năm 1816.",
        "Từng là thánh đường chính của 'sân Bukhara' – cộng đồng thương nhân Trung Á.",
        "Bị đóng cửa thời Xô-viết, phục dựng từ hoang tàn trong các năm 2005–2008.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ cầu nguyện; du khách nên tới ngoài giờ lễ và xin phép.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Ban ngày ngoài giờ cầu nguyện; tránh giờ lễ thứ Sáu đông đúc.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn; bỏ giày khi vào; kết hợp thăm Ak-mechet gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Чёрная мечеть (Астрахань)", "url": "https://ru.wikipedia.org/wiki/Чёрная_мечеть_(Астрахань)"},
        {"title": "Wikipedia (RU) — Исторические мечети Астрахани", "url": "https://ru.wikipedia.org/wiki/Исторические_мечети_Астрахани"},
    ],
    ["church", "mosque", "islam", "bukhara-court", "heritage", "astrakhan"],
    maps_text("Чёрная мечеть", "Астрахань", "Black Mosque Kara Mosque", "Astrakhan", 46.343056, 48.033333),
))

# 13) Римско-католический храм Успения Пресвятой Девы Марии -------------------------
RECORDS.append(rec(
    "catholic-church-assumption",
    "Nhà thờ Công giáo Đức Mẹ Lên Trời (Katolichesky khram)",
    "Римско-католический храм Успения Пресвятой Девы Марии",
    "Roman Catholic Church of the Assumption (Astrakhan)",
    ["church"],
    46.345900, 48.051000,
    "Ул. Бабушкина, 81 (phố Католическая cũ), thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Nhà thờ Công giáo La Mã của Astrakhan, gắn với cộng đồng người Ba Lan, Đức, Ý và Armenia Công giáo từng sinh sống nơi đây. Công trình duyên dáng nhắc nhớ quá khứ đa sắc tộc, đa tín ngưỡng của thành phố thương cảng.",
    "Là thành phố thương cảng quốc tế bên đường giao thương Á–Âu, Astrakhan từng quy tụ nhiều cộng đồng ngoại quốc, trong đó có người Công giáo gốc Ba Lan, Đức, Ý và Armenia. Nhà thờ Công giáo La Mã kính Đức Mẹ Lên Trời (Uspenie) ra đời để phục vụ cộng đồng ấy, với lịch sử từ thế kỷ 18–19 và toạ lạc trên con phố từng mang tên 'Katolicheskaya' (phố Công giáo). Công trình mang kiến trúc phương Tây thanh thoát, khác biệt với các nhà thờ Chính Thống giáo mái vòm và các nhà thờ Hồi giáo có minaret quanh vùng, góp thêm một sắc màu vào bức tranh tôn giáo đa dạng bậc nhất nước Nga của thành phố. Trải qua thời Xô-viết với nhiều thăng trầm, nhà thờ nay lại là nơi sinh hoạt của cộng đồng Công giáo địa phương và là một điểm tham quan giàu ý nghĩa lịch sử. Ghé thăm nơi đây, du khách hiểu thêm về tính chất 'ngã tư các nền văn minh' đã làm nên bản sắc độc đáo của Astrakhan.",
    [
        "Nhà thờ Công giáo La Mã của Astrakhan, kính Đức Mẹ Lên Trời (Uspenie).",
        "Gắn với cộng đồng Ba Lan, Đức, Ý, Armenia Công giáo từng sinh sống ở thành phố.",
        "Kiến trúc phương Tây, minh chứng cho bản sắc đa tôn giáo của thành phố thương cảng.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ; du khách nên tới ngoài giờ lễ và xin phép.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Ban ngày ngoài giờ lễ; dịp lễ Công giáo.",
        "tips_vi": "Ăn mặc lịch sự, giữ yên lặng; xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Vetert.ru — Храм Успения Пресвятой Богородицы (католический)", "url": "https://vetert.ru/rossiya/astrakhan/sights/504-hram-uspeniya-presvyatoj-bogorodicy.php"},
    ],
    ["church", "catholic", "assumption", "multicultural", "heritage", "astrakhan"],
    maps_text("Римско-католический храм Успения", "Астрахань", "Roman Catholic Church of the Assumption", "Astrakhan", 46.345900, 48.051000),
))

# 14) Астраханский театр оперы и балета --------------------------------------------
RECORDS.append(rec(
    "opera-ballet-theatre",
    "Nhà hát Opera và Ballet Astrakhan (Teatr opery i baleta)",
    "Астраханский театр оперы и балета",
    "Astrakhan Opera and Ballet Theatre",
    ["theatre"],
    46.360329, 48.044072,
    "Ул. Анри Барбюса, 16 (Театральный парк), thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Nhà hát opera và ballet hoành tráng của Astrakhan, khánh thành năm 2011, được xây theo phong cách 'giả Nga' như một 'cung điện nhà hát'. Sân khấu lớn hiện đại này là trung tâm nghệ thuật hàn lâm hàng đầu của cả vùng nam nước Nga.",
    "Sừng sững như một cung điện nơi công viên Teatralny, Nhà hát Opera và Ballet Astrakhan là một trong những công trình văn hoá bề thế và hiện đại nhất vùng nam nước Nga. Khánh thành năm 2011, toà nhà được thiết kế theo phong cách 'giả Nga' (pseudo-Russian) pha nét 'modern', với những mái vòm, tháp và trang trí gợi nhớ kiến trúc Nga cổ, tạo nên diện mạo tráng lệ hiếm thấy ở một nhà hát tỉnh. Bên trong là tổ hợp văn hoá – giải trí đa năng: khán phòng lớn quy mô hàng nghìn chỗ với sân khấu và hệ thống kỹ thuật hiện đại, khán phòng nhỏ cùng nhiều không gian nghệ thuật mở cửa cho công chúng. Nhà hát dàn dựng các vở opera kinh điển, ballet, hoà nhạc giao hưởng và những chương trình nghệ thuật quy mô lớn, quy tụ nghệ sĩ trong nước và quốc tế. Đây là niềm tự hào của Astrakhan và là điểm đến hấp dẫn cho những ai yêu nghệ thuật hàn lâm; ngay cả khi không xem biểu diễn, du khách vẫn thường ghé chiêm ngưỡng kiến trúc lộng lẫy của 'cung điện nhà hát' này.",
    [
        "Nhà hát opera – ballet hoành tráng, khánh thành 2011, thiết kế như một 'cung điện nhà hát'.",
        "Kiến trúc 'giả Nga' pha nét modern với mái vòm, tháp và trang trí gợi kiến trúc Nga cổ.",
        "Trung tâm nghệ thuật hàn lâm hàng đầu vùng nam nước Nga: opera, ballet, giao hưởng.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch mùa, thường buổi tối và cuối tuần; phòng vé mở ban ngày.",
        "ticket_vi": "Giá vé đa dạng tuỳ chương trình và vị trí ghế; nên đặt trước qua kênh chính thức.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ; tham quan ngoài khoảng 20–30 phút.",
        "best_time_vi": "Mùa biểu diễn (thu–xuân); kiểm tra lịch diễn trước khi tới.",
        "tips_vi": "Mua vé sớm cho các vở nổi bật; trang phục lịch sự; tới sớm để ngắm kiến trúc và nội thất.",
    },
    [
        {"title": "Culture.ru — Астраханский государственный театр оперы и балета", "url": "https://www.culture.ru/institutes/6737/astrakhanskii-gosudarstvennyi-teatr-opery-i-baleta"},
        {"title": "2ГИС — Театр оперы и балета, Астрахань", "url": "https://2gis.ru/astrakhan/firm/1126428188094285"},
    ],
    ["theatre", "opera", "ballet", "architecture", "landmark", "astrakhan"],
    maps_org("https://2gis.ru/astrakhan/firm/1126428188094285", "Astrakhan Opera and Ballet Theatre", "Astrakhan"),
    official_site="http://www.astoperahouse.ru",
))

# 15) Астраханский драматический театр ---------------------------------------------
RECORDS.append(rec(
    "drama-theatre",
    "Nhà hát Kịch Astrakhan (Dramatichesky teatr)",
    "Астраханский драматический театр",
    "Astrakhan Drama Theatre",
    ["theatre"],
    46.348280, 48.044199,
    "Ул. Советская, 28, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Nhà hát kịch nói lâu đời của Astrakhan, với truyền thống biểu diễn chuyên nghiệp từ thế kỷ 19. Sân khấu trung tâm này dàn dựng cả kịch kinh điển Nga lẫn tác phẩm đương đại, là điểm hẹn văn hoá quen thuộc của người dân thành phố.",
    "Astrakhan có truyền thống sân khấu lâu đời gắn với thời kỳ thành phố còn là thương cảng sầm uất bên Volga, và Nhà hát Kịch (Dramatichesky teatr) là hiện thân của di sản ấy. Với lịch sử biểu diễn chuyên nghiệp bắt rễ từ thế kỷ 19, nhà hát đã trở thành trái tim đời sống sân khấu của thành phố: nơi dàn dựng các vở kinh điển của những đại văn hào Nga như Chekhov, Ostrovsky, Gogol cùng nhiều tác phẩm hiện đại và kịch dành cho khán giả trẻ. Toà nhà nằm ngay trên phố Sovetskaya nhộn nhịp ở trung tâm, gần các bảo tàng và Điện Kremlin, tạo thành một cụm văn hoá tiện dạo bộ. Đoàn kịch quy tụ nhiều nghệ sĩ tài năng và thường xuyên ra mắt các vở diễn mới, tham gia liên hoan sân khấu. Với người yêu nghệ thuật, một buổi tối xem kịch nơi đây là cách thú vị để hoà vào nhịp sinh hoạt của người dân Astrakhan; và ngay cả khi rào cản ngôn ngữ, du khách vẫn có thể cảm nhận không khí trang trọng của một nhà hát tỉnh lỵ giàu truyền thống.",
    [
        "Nhà hát kịch nói lâu đời của Astrakhan, truyền thống chuyên nghiệp từ thế kỷ 19.",
        "Dàn dựng kịch kinh điển Nga (Chekhov, Ostrovsky, Gogol) và tác phẩm đương đại.",
        "Vị trí trung tâm trên phố Sovetskaya, gần bảo tàng và Điện Kremlin.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch mùa, thường buổi tối và cuối tuần; phòng vé mở ban ngày.",
        "ticket_vi": "Giá vé bình dân tuỳ chương trình và vị trí ghế; nên đặt trước.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ.",
        "best_time_vi": "Mùa biểu diễn (thu–xuân); kiểm tra lịch diễn trước.",
        "tips_vi": "Đặt vé sớm cho vở nổi bật; trang phục lịch sự; kết hợp dạo trung tâm lịch sử.",
    },
    [
        {"title": "2ГИС — Драматический театр, Астрахань", "url": "https://2gis.ru/astrakhan/firm/1126428187823226"},
        {"title": "Astradram.ru — официальный сайт", "url": "http://astradram.ru"},
    ],
    ["theatre", "drama", "russian-classics", "culture", "astrakhan"],
    maps_org("https://2gis.ru/astrakhan/firm/1126428187823226", "Astrakhan Drama Theatre", "Astrakhan"),
    official_site="http://astradram.ru",
))

# 16) Астраханский театр кукол -----------------------------------------------------
RECORDS.append(rec(
    "puppet-theatre",
    "Nhà hát Múa rối Astrakhan (Teatr kukol)",
    "Астраханский театр кукол",
    "Astrakhan Puppet Theatre",
    ["theatre"],
    46.353171, 48.030877,
    "Никольская ул., 7 (góc ул. Фиолетова, 12), trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Nhà hát múa rối được yêu thích của Astrakhan, đặt trong một toà nhà lịch sử ở trung tâm. Điểm đến giải trí – nghệ thuật hấp dẫn cho gia đình và trẻ em với những vở rối sinh động.",
    "Nhà hát Múa rối Astrakhan là một điểm đến văn hoá được các gia đình và trẻ em đặc biệt yêu thích, nằm trong một toà nhà cổ duyên dáng ở trung tâm thành phố (khu phố Nikolskaya – Fioletova, vốn là công trình của ngân hàng Nga – Á xưa). Sân khấu rối nơi đây dàn dựng những vở diễn dựa trên truyện cổ tích Nga và thế giới, kết hợp con rối, âm nhạc, ánh sáng và diễn xuất để tạo nên các câu chuyện sinh động, giàu tính giáo dục. Không chỉ dành cho thiếu nhi, nhiều chương trình còn hấp dẫn cả khán giả lớn tuổi bởi sự khéo léo trong chế tác con rối và nghệ thuật điều khiển. Với vị trí trung tâm thuận tiện và bầu không khí ấm áp, nhà hát là lựa chọn lý tưởng cho một buổi giải trí nhẹ nhàng khi khám phá Astrakhan cùng gia đình. Đây cũng là nơi nuôi dưỡng tình yêu sân khấu cho các thế hệ nhỏ tuổi của thành phố, góp phần làm phong phú đời sống văn hoá địa phương.",
    [
        "Nhà hát múa rối được yêu thích, lý tưởng cho gia đình và trẻ em.",
        "Đặt trong toà nhà lịch sử ở trung tâm (nguyên là ngân hàng Nga – Á xưa).",
        "Dàn dựng các vở rối từ truyện cổ tích Nga và thế giới, sinh động, giàu tính giáo dục.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch (thường cuối tuần và ban ngày); phòng vé mở ban ngày.",
        "ticket_vi": "Giá vé bình dân; ưu đãi cho trẻ em và nhóm.",
        "duration_vi": "Một buổi diễn khoảng 45–60 phút.",
        "best_time_vi": "Cuối tuần; kiểm tra lịch diễn trước khi tới.",
        "tips_vi": "Phù hợp gia đình có trẻ nhỏ; đặt vé trước cho suất cuối tuần.",
    },
    [
        {"title": "2ГИС — Театр кукол, Астрахань", "url": "https://2gis.ru/astrakhan/firm/1126428187823110"},
        {"title": "Astpupp.ru — официальный сайт", "url": "http://astpupp.ru"},
    ],
    ["theatre", "puppet", "family", "children", "astrakhan"],
    maps_org("https://2gis.ru/astrakhan/firm/1126428187823110", "Astrakhan Puppet Theatre", "Astrakhan"),
    official_site="http://astpupp.ru",
))

# 17) Астраханский театр юного зрителя (ТЮЗ) ---------------------------------------
RECORDS.append(rec(
    "youth-theatre-tyuz",
    "Nhà hát Khán giả Trẻ Astrakhan (TYUZ)",
    "Астраханский театр юного зрителя",
    "Astrakhan Youth Theatre (TYUZ)",
    ["theatre"],
    46.346709, 48.032494,
    "Ул. Мусы Джалиля, 4, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Nhà hát dành cho khán giả trẻ (TYUZ) của Astrakhan, chuyên dàn dựng các vở kịch cho thiếu nhi, thanh thiếu niên và gia đình. Sân khấu năng động này là nơi ươm mầm tình yêu nghệ thuật cho các thế hệ trẻ của thành phố.",
    "Nhà hát Khán giả Trẻ (Teatr yunogo zritelya, viết tắt TYUZ) là một sân khấu đặc trưng trong hệ thống nhà hát Nga, dành riêng cho khán giả thiếu nhi và thanh thiếu niên, và Astrakhan tự hào có một nhà hát như vậy ngay tại trung tâm thành phố. TYUZ Astrakhan dàn dựng đa dạng thể loại: từ truyện cổ tích, kịch thiếu nhi vui nhộn tới những vở dành cho lứa tuổi lớn hơn dựa trên tác phẩm văn học kinh điển, luôn chú trọng tính giáo dục và thẩm mỹ phù hợp với người trẻ. Nhà hát từng được ghi nhận với các giải thưởng địa phương và là điểm hẹn quen thuộc của các trường học, gia đình trong những dịp cuối tuần, lễ hội. Với dàn diễn viên nhiệt huyết và các chương trình được đầu tư dàn dựng công phu, TYUZ góp phần quan trọng nuôi dưỡng đời sống tinh thần và tình yêu sân khấu cho thế hệ trẻ Astrakhan. Đây là gợi ý thú vị cho các gia đình muốn có một trải nghiệm văn hoá gần gũi khi tới thăm thành phố.",
    [
        "Nhà hát dành cho khán giả trẻ (TYUZ), chuyên kịch cho thiếu nhi và thanh thiếu niên.",
        "Dàn dựng từ truyện cổ tích tới kịch dựa trên văn học kinh điển, giàu tính giáo dục.",
        "Điểm hẹn quen thuộc của trường học và gia đình dịp cuối tuần, lễ hội.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch (thường ban ngày và cuối tuần); phòng vé mở ban ngày.",
        "ticket_vi": "Giá vé bình dân; ưu đãi cho trẻ em, học sinh và nhóm.",
        "duration_vi": "Một buổi diễn khoảng 1–1,5 giờ.",
        "best_time_vi": "Cuối tuần; kiểm tra lịch diễn trước.",
        "tips_vi": "Phù hợp gia đình có trẻ em và học sinh; đặt vé trước cho suất cuối tuần.",
    },
    [
        {"title": "2ГИС — Театр юного зрителя, Астрахань", "url": "https://2gis.ru/astrakhan/firm/1126428187823118"},
        {"title": "Astratuz.ru — официальный сайт", "url": "http://astratuz.ru"},
    ],
    ["theatre", "youth", "children", "family", "astrakhan"],
    maps_org("https://2gis.ru/astrakhan/firm/1126428187823118", "Astrakhan Youth Theatre TYUZ", "Astrakhan"),
    official_site="http://astratuz.ru",
))

# 18) Астраханская государственная филармония --------------------------------------
RECORDS.append(rec(
    "astrakhan-philharmonic",
    "Nhạc viện – Nhà hát giao hưởng Astrakhan (Filarmoniya)",
    "Астраханская государственная филармония",
    "Astrakhan State Philharmonic",
    ["theatre"],
    46.350781, 48.041091,
    "Ул. Молодой Гвардии, ст1, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Trung tâm hoà nhạc hàn lâm của Astrakhan, nơi biểu diễn nhạc giao hưởng, nhạc thính phòng, hợp xướng và dân ca. Sân khấu âm nhạc uy tín này là điểm hẹn của giới mộ điệu và các nghệ sĩ trong nước, quốc tế.",
    "Nhạc viện – Nhà hát giao hưởng bang Astrakhan (Filarmoniya) là trung tâm của đời sống âm nhạc hàn lâm thành phố. Đặt trong một toà nhà lịch sử ở trung tâm, đây là nơi biểu diễn thường xuyên của các dàn nhạc giao hưởng, dàn nhạc dân tộc, hợp xướng và các nghệ sĩ độc tấu, với chương trình trải rộng từ nhạc cổ điển châu Âu, nhạc Nga tới dân ca và các dự án đương đại. Filarmoniya cũng là nơi tổ chức các liên hoan âm nhạc, đêm nhạc chủ đề và những chương trình giáo dục âm nhạc cho công chúng, góp phần nuôi dưỡng thẩm mỹ nghệ thuật cho người dân địa phương. Không gian khán phòng ấm áp cùng âm thanh được chăm chút mang lại trải nghiệm thưởng thức chất lượng. Astrakhan vốn có truyền thống đào tạo âm nhạc mạnh (với nhạc viện danh tiếng), nên đời sống hoà nhạc nơi đây khá sôi động. Với du khách yêu âm nhạc, một buổi tối tại Filarmoniya là dịp thư thái để cảm nhận chiều sâu văn hoá của thành phố bên dòng Volga.",
    [
        "Trung tâm hoà nhạc hàn lâm của Astrakhan: giao hưởng, thính phòng, hợp xướng, dân ca.",
        "Đặt trong toà nhà lịch sử ở trung tâm; nơi tổ chức liên hoan và đêm nhạc chủ đề.",
        "Gắn với truyền thống đào tạo âm nhạc mạnh của thành phố.",
    ],
    {
        "hours_vi": "Có chương trình theo lịch mùa (thường buổi tối); phòng vé mở ban ngày.",
        "ticket_vi": "Giá vé đa dạng tuỳ chương trình; nên đặt trước qua kênh chính thức.",
        "duration_vi": "Một buổi hoà nhạc khoảng 1,5–2 giờ.",
        "best_time_vi": "Mùa biểu diễn (thu–xuân); kiểm tra lịch trước.",
        "tips_vi": "Trang phục lịch sự; đặt vé sớm cho các đêm nhạc nổi bật.",
    },
    [
        {"title": "2ГИС — Астраханская государственная филармония", "url": "https://2gis.ru/astrakhan/firm/1126428187823111"},
    ],
    ["theatre", "philharmonic", "classical-music", "concert", "astrakhan"],
    maps_org("https://2gis.ru/astrakhan/firm/1126428187823111", "Astrakhan State Philharmonic", "Astrakhan"),
))

# 19) Памятник Петру I -------------------------------------------------------------
RECORDS.append(rec(
    "peter-the-great-monument",
    "Tượng đài Pyotr Đại đế (Pamyatnik Petru I)",
    "Памятник Петру I",
    "Monument to Peter the Great (Astrakhan)",
    ["monument"],
    46.347153, 48.015996,
    "Bờ kè Petrovskaya (Петровская набережная), bên sông Volga, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Tượng đài Sa hoàng Pyotr Đại đế đứng uy nghi bên bờ kè sông Volga, tôn vinh vị hoàng đế gắn bó với sự phát triển của Astrakhan. Đây là một biểu tượng và điểm chụp ảnh quen thuộc ở khu trung tâm ven sông.",
    "Bên bờ kè Petrovskaya soi bóng dòng Volga, tượng đài Pyotr Đại đế (Pyotr I) sừng sững như một biểu tượng gắn kết thành phố với vị hoàng đế cải cách vĩ đại của nước Nga. Pyotr Đại đế có mối liên hệ đặc biệt với Astrakhan: chính dưới thời ông, năm 1717, tỉnh Astrakhan (guberniya) được thành lập, và nhà vua từng đích thân tới đây để chuẩn bị cho chiến dịch Ba Tư, coi thành phố là bàn đạp chiến lược cho tham vọng vươn ra biển Caspi và phương Đông. Bức tượng khắc hoạ hình ảnh vị hoàng đế trong tư thế uy nghi, đặt trên bệ cao nhìn ra sông, trở thành điểm nhấn của không gian bờ kè được chỉnh trang khang trang. Xung quanh là lối đi lát đá, cây xanh và tầm nhìn thoáng đãng ra mặt nước – nơi người dân và du khách thường dừng chân chụp ảnh, dạo mát và ngắm hoàng hôn. Vừa mang ý nghĩa lịch sử, vừa là một tiểu cảnh đẹp ven sông, tượng đài Pyotr Đại đế là điểm dừng chân dễ chịu khi khám phá trung tâm Astrakhan.",
    [
        "Tượng đài Pyotr Đại đế uy nghi bên bờ kè Petrovskaya, nhìn ra sông Volga.",
        "Tôn vinh vị hoàng đế gắn với việc lập tỉnh Astrakhan (1717) và chiến dịch Ba Tư.",
        "Điểm nhấn và nơi chụp ảnh, dạo mát, ngắm hoàng hôn quen thuộc ở trung tâm ven sông.",
    ],
    {
        "hours_vi": "Không gian ngoài trời, tham quan tự do suốt ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–20 phút.",
        "best_time_vi": "Chiều tối, đặc biệt lúc hoàng hôn; cuối xuân đến đầu thu dễ chịu nhất.",
        "tips_vi": "Kết hợp dạo bờ kè và tham quan trung tâm; mang áo khoác nhẹ vì bờ sông lộng gió.",
    },
    [
        {"title": "Petersmonuments.ru — Памятник Петру I (Астрахань)", "url": "https://petersmonuments.ru/russia/memorials/pamyatnik-petru-i-astrakhan/"},
    ],
    ["monument", "peter-the-great", "embankment", "volga", "landmark", "astrakhan"],
    maps_text("Памятник Петру I", "Астрахань", "Monument to Peter the Great", "Astrakhan", 46.347153, 48.015996),
))

# 20) Лебединое озеро --------------------------------------------------------------
RECORDS.append(rec(
    "swan-lake",
    "Hồ Thiên nga (Lebedinoe ozero)",
    "Лебединое озеро",
    "Swan Lake (Astrakhan)",
    ["park_garden"],
    46.345980, 48.023260,
    "Trung tâm thành phố Astrakhan, giữa quảng trường Lenin, bờ kè 1 Mai và phố Admiralteyskaya, tỉnh Astrakhan, Nga.",
    "Hồ nước trong lành giữa lòng trung tâm Astrakhan, nơi thả nuôi thiên nga và là không gian dạo chơi lãng mạn được người dân yêu thích. Cây cầu và các lối đi ven hồ tạo nên một góc thư thái ngay gần Điện Kremlin.",
    "Ngay giữa trung tâm lịch sử, Hồ Thiên nga (Lebedinoe ozero) là một 'ốc đảo' xanh mát và lãng mạn được người dân Astrakhan gắn bó. Mặt hồ phẳng lặng phản chiếu bầu trời và những hàng cây, trên đó thong dong bơi lội đàn thiên nga trắng, đen cùng các loài chim nước – hình ảnh đã đặt tên cho hồ và trở thành nét duyên riêng của nơi này. Bao quanh hồ là các lối đi dạo lát đá, ghế nghỉ, thảm cỏ, đài phun nước cùng cây cầu bắc qua mặt nước – nơi các cặp đôi thường dừng chân chụp ảnh (nhiều người gọi vui là 'cầu tình yêu'). Nằm sát quảng trường Lenin và không xa Điện Kremlin, hồ là điểm kết nối tự nhiên trong hành trình dạo bộ khám phá trung tâm. Vào chiều tối và những ngày lễ, khu vực quanh hồ trở nên nhộn nhịp với người dân ra hóng mát, trẻ em vui chơi và các hoạt động ngoài trời. Yên bình, thơ mộng và tiện đường tham quan, Hồ Thiên nga là nơi lý tưởng để thư giãn giữa nhịp sống của thành phố phương Nam bên Volga.",
    [
        "Hồ nước giữa trung tâm Astrakhan, nơi thả nuôi thiên nga và chim nước.",
        "Lối đi dạo, đài phun nước và cây cầu lãng mạn ('cầu tình yêu') ven hồ.",
        "Nằm sát quảng trường Lenin và gần Điện Kremlin, tiện kết hợp tham quan.",
    ],
    {
        "hours_vi": "Không gian công cộng ngoài trời, mở cửa tự do.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Chiều tối và cuối tuần; cuối xuân đến đầu thu đẹp nhất.",
        "tips_vi": "Kết hợp dạo quảng trường Lenin và Điện Kremlin; đẹp để chụp ảnh lúc chiều tà.",
    },
    [
        {"title": "Tonkosti — Лебединое озеро в Астрахани", "url": "https://tonkosti.ru/Лебединое_озеро_в_Астрахани"},
    ],
    ["park_garden", "lake", "swans", "promenade", "family", "astrakhan"],
    maps_text("Лебединое озеро", "Астрахань", "Swan Lake", "Astrakhan", 46.345980, 48.023260),
))

# 21) Площадь Ленина ---------------------------------------------------------------
RECORDS.append(rec(
    "lenin-square",
    "Quảng trường Lenin (Ploshchad Lenina)",
    "Площадь Ленина",
    "Lenin Square (Astrakhan)",
    ["square_street"],
    46.347600, 48.030200,
    "Dưới chân tường nam Điện Kremlin, trung tâm thành phố Astrakhan, tỉnh Astrakhan, Nga.",
    "Quảng trường trung tâm chính của Astrakhan, trải dài dưới chân tường thành nam Điện Kremlin. Không gian rộng thoáng với đài phun nước, cây xanh và tầm nhìn ra Kremlin là nơi diễn ra các sự kiện, lễ hội lớn của thành phố.",
    "Quảng trường Lenin là quảng trường trung tâm và là 'phòng khách' của thành phố Astrakhan, trải rộng ngay dưới chân bức tường thành phía nam của Điện Kremlin đá trắng. Từ đây, du khách có tầm nhìn tuyệt đẹp lên các tháp canh và tường thành cổ kính của Kremlin – biểu tượng của thành phố. Quảng trường đã được chỉnh trang thành một không gian công cộng khang trang với lối đi lát đá rộng rãi, thảm cỏ, cây xanh, đài phun nước và ánh sáng nghệ thuật vào buổi tối. Đây là nơi diễn ra các sự kiện quan trọng của thành phố: mít tinh, lễ hội, hoà nhạc ngoài trời, chợ phiên dịp lễ và các màn trình diễn trong những ngày kỷ niệm. Vào buổi tối và cuối tuần, quảng trường trở nên nhộn nhịp với người dân đi dạo, trẻ em vui chơi và du khách chụp ảnh bên Kremlin. Liền kề Hồ Thiên nga và các tuyến phố trung tâm, quảng trường Lenin là điểm khởi đầu thuận tiện cho hành trình khám phá lõi lịch sử của Astrakhan.",
    [
        "Quảng trường trung tâm chính của Astrakhan, dưới chân tường nam Điện Kremlin.",
        "Không gian khang trang với đài phun nước, cây xanh và tầm nhìn đẹp lên Kremlin.",
        "Nơi diễn ra các sự kiện, lễ hội, hoà nhạc và mít tinh lớn của thành phố.",
    ],
    {
        "hours_vi": "Không gian công cộng ngoài trời, mở cửa tự do suốt ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Chiều tối và dịp lễ hội; cuối xuân đến đầu thu dễ chịu nhất.",
        "tips_vi": "Kết hợp tham quan Điện Kremlin và Hồ Thiên nga liền kề; đẹp khi lên đèn buổi tối.",
    },
    [
        {"title": "Vetert.ru — Площадь Ленина (Астрахань)", "url": "https://vetert.ru/rossiya/astrakhan/sights/518-ploschad-lenina.php"},
    ],
    ["square_street", "central-square", "kremlin-view", "events", "astrakhan"],
    maps_text("Площадь Ленина", "Астрахань", "Lenin Square", "Astrakhan", 46.347600, 48.030200),
))

# 22) Братский сад -----------------------------------------------------------------
RECORDS.append(rec(
    "bratsky-garden",
    "Vườn Bratsky (Bratsky sad)",
    "Братский сад",
    "Bratsky Garden (Astrakhan)",
    ["park_garden"],
    46.350300, 48.035000,
    "Ул. Советская, 1, trung tâm thành phố Astrakhan, gần Điện Kremlin, tỉnh Astrakhan, Nga.",
    "Công viên trung tâm lâu đời của Astrakhan, nằm ngay gần Điện Kremlin. Không gian xanh rợp bóng cây với đài tưởng niệm và lối đi dạo là nơi thư giãn quen thuộc của người dân thành phố.",
    "Bratsky sad ('Vườn Anh em') là một trong những công viên trung tâm lâu đời và được yêu thích của Astrakhan, toạ lạc ngay sát Điện Kremlin ở đầu phố Sovetskaya. Có lịch sử hình thành từ đầu thế kỷ 20, khu vườn từng nhiều lần đổi tên và diện mạo theo dòng lịch sử thành phố. Ngày nay đây là một không gian xanh rợp bóng cây cổ thụ với những lối đi dạo lát đá, ghế nghỉ, bồn hoa và các đài tưởng niệm – trong đó có phần mộ và tượng đài tưởng nhớ những người ngã xuống trong các biến động lịch sử, mang lại cho công viên chiều sâu trầm mặc. Người dân Astrakhan thường ra đây tản bộ, nghỉ chân dưới tán cây, trong khi trẻ em vui chơi và du khách dừng lại giữa hành trình tham quan trung tâm. Vị trí liền kề Điện Kremlin và các bảo tàng khiến Bratsky sad trở thành điểm nghỉ ngơi lý tưởng, giúp cân bằng giữa khám phá di tích và thư giãn giữa thiên nhiên trong lòng phố cổ.",
    [
        "Công viên trung tâm lâu đời của Astrakhan, ngay sát Điện Kremlin.",
        "Không gian xanh rợp bóng cây với lối đi dạo, bồn hoa và đài tưởng niệm.",
        "Nơi tản bộ, nghỉ chân quen thuộc, tiện kết hợp tham quan trung tâm lịch sử.",
    ],
    {
        "hours_vi": "Không gian công cộng ngoài trời, mở cửa tự do.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; buổi sáng và chiều mát dễ chịu.",
        "tips_vi": "Kết hợp tham quan Điện Kremlin và các bảo tàng gần đó; chỗ nghỉ chân lý tưởng.",
    },
    [
        {"title": "Vetert.ru — Братский сад (Астрахань)", "url": "https://vetert.ru/rossiya/astrakhan/sights/519-bratskij-sad.php"},
    ],
    ["park_garden", "city-park", "memorial", "green-space", "astrakhan"],
    maps_text("Братский сад", "Астрахань", "Bratsky Garden", "Astrakhan", 46.350300, 48.035000),
))

# 23) Хошеутовский хурул -----------------------------------------------------------
RECORDS.append(rec(
    "khosheutovsky-khurul",
    "Chùa Phật giáo Kalmyk Khosheutovsky (Khosheutovsky khurul)",
    "Хошеутовский хурул",
    "Khosheutovsky Khurul (Kalmyk Buddhist Temple)",
    ["church"],
    46.927222, 47.613333,
    "Làng Rechnoye (Речное), huyện Kharabalinsky, tỉnh Astrakhan, Nga; bên bờ sông Volga.",
    "Ngôi chùa Phật giáo Kalmyk cổ nhất châu Âu còn lại, xây năm 1814–1817 để mừng chiến thắng trước Napoléon 1812. Kiến trúc độc đáo pha trộn cổ điển Nga và truyền thống Kalmyk, lấy cảm hứng từ Nhà thờ Kazan ở Saint Petersburg.",
    "Giữa thảo nguyên bên bờ Volga ở làng Rechnoye, huyện Kharabalinsky, ngôi chùa Khosheutovsky (khurul) sừng sững như một chứng nhân độc đáo của lịch sử. Được xây dựng năm 1814–1817 theo sáng kiến của lãnh chúa Kalmyk Serebdzhab Tyumen – một anh hùng trong Chiến tranh Vệ quốc 1812 – ngôi chùa là đài tưởng niệm chiến thắng của quân đội Nga (trong đó có các trung đoàn Kalmyk) trước Napoléon. Điều làm nên sự đặc biệt của công trình là kiến trúc kết hợp giữa chủ nghĩa cổ điển Nga và truyền thống Phật giáo Kalmyk: bố cục lấy cảm hứng từ Nhà thờ Kazan ở Saint Petersburg với hai dãy hành lang vòng cung (nay đã mất), toà tháp trung tâm cao và những chi tiết trang trí mang biểu tượng Phật giáo. Trải qua thời Xô-viết, chùa bị đóng cửa, hư hại nặng và mất nhiều hạng mục; tới các năm 2009–2014 mới được trùng tu. Đây là ngôi chùa Phật giáo cổ nhất châu Âu còn lại và là công trình tôn giáo Kalmyk thời tiền cách mạng hiếm hoi còn tồn tại, được xếp hạng di sản văn hoá cấp liên bang. Xa xôi nhưng đầy mê hoặc, khurul thu hút những khách hành hương và du khách muốn tìm hiểu văn hoá Phật giáo Kalmyk giữa vùng đất Astrakhan đa tôn giáo.",
    [
        "Ngôi chùa Phật giáo Kalmyk cổ nhất châu Âu còn lại, xây 1814–1817.",
        "Đài tưởng niệm chiến thắng trước Napoléon 1812; kiến trúc lấy cảm hứng Nhà thờ Kazan.",
        "Di sản văn hoá cấp liên bang; được trùng tu trong các năm 2009–2014.",
    ],
    {
        "hours_vi": "Công trình ngoài trời, tham quan ban ngày; cộng đồng Phật giáo địa phương quản lý.",
        "ticket_vi": "Thường miễn phí hoặc quyên góp tuỳ tâm; nên hỏi tại chỗ.",
        "duration_vi": "Khoảng 30–45 phút (chưa kể di chuyển xa).",
        "best_time_vi": "Cuối xuân đến đầu thu; tránh nắng gắt giữa trưa hè.",
        "tips_vi": "Ở xa Astrakhan (~130 km), nên đi ô tô và kết hợp cung đường phía bắc; ăn mặc kín đáo, tôn trọng tín ngưỡng.",
    },
    [
        {"title": "Wikipedia (RU) — Хошеутовский хурул", "url": "https://ru.wikipedia.org/wiki/Хошеутовский_хурул"},
    ],
    ["church", "buddhist", "kalmyk", "khurul", "1812-memorial", "heritage", "astrakhan"],
    maps_text("Хошеутовский хурул", "Речное", "Khosheutovsky Khurul", "Rechnoye", 46.927222, 47.613333),
))

# 24) Селитренное городище (столица Золотой Орды) ----------------------------------
RECORDS.append(rec(
    "selitrennoye-site",
    "Di chỉ Selitrennoye – kinh đô Kim Trướng hãn quốc (Selitrennoe gorodishche)",
    "Селитренное городище",
    "Selitrennoye Site (Golden Horde Capital Ruins)",
    ["other"],
    47.185000, 47.425000,
    "Gần làng Selitrennoye (Селитренное), bên sông Akhtuba, huyện Kharabalinsky, tỉnh Astrakhan, Nga.",
    "Di chỉ khảo cổ của Sarai – kinh đô Kim Trướng hãn quốc thế kỷ 14, trải dài nhiều km bên sông Akhtuba. Đây là tàn tích đô thị Trung cổ thật, khác với phim trường Sarai-Batu gần đó, và là di tích khảo cổ cấp liên bang.",
    "Trải dài thành một dải dài nhiều cây số bên nhánh sông Akhtuba, gần làng Selitrennoye, di chỉ Selitrennoe gorodishche là tàn tích của một trong những đô thị lớn nhất Kim Trướng hãn quốc – được các nhà khoa học xác định là kinh đô Sarai (thường gọi Sarai al-Jadid / Tân Sarai, phát triển rực rỡ từ thời hãn Uzbek những năm 1330). Nhà nghiên cứu Vadim Egorov từng ước tính đô thị này rộng khoảng 10 x 2 km và xếp vào hàng lớn nhất châu Âu Trung cổ. Từ thập niên 1960 tới nay, các đoàn khảo cổ đã khai quật hơn 25.000 m2, phát lộ những khu dinh thự, nhà thờ Hồi giáo, khu xưởng thủ công, lò gạch và các khu mộ táng, hé lộ đời sống phồn thịnh và tính chất đa sắc tộc của một trung tâm quyền lực Á–Âu. Cần phân biệt di chỉ khảo cổ thật này với khu phim trường Sarai-Batu (nằm cách đó không xa) được dựng lại để quay phim: một bên là hiện trường lịch sử nguyên bản còn nằm sâu dưới đất, một bên là bối cảnh tái hiện phục vụ du lịch. Với những ai yêu khảo cổ và lịch sử Kim Trướng hãn quốc, Selitrennoe gorodishche là một điểm đến giàu ý nghĩa – nơi từng đập nhịp trái tim của một đế quốc thảo nguyên hùng mạnh.",
    [
        "Di chỉ khảo cổ của Sarai – kinh đô Kim Trướng hãn quốc thế kỷ 14, di tích cấp liên bang.",
        "Đô thị Trung cổ rộng lớn (~10 x 2 km), từng thuộc hàng lớn nhất châu Âu thời đó.",
        "Là hiện trường lịch sử THẬT, khác với phim trường Sarai-Batu tái hiện gần đó.",
    ],
    {
        "hours_vi": "Khu di chỉ ngoài trời trên thảo nguyên; tham quan ban ngày, không có giờ cố định.",
        "ticket_vi": "Thường không thu phí tại di chỉ; nên đi cùng hướng dẫn viên/tour khảo cổ để hiểu hiện trường.",
        "duration_vi": "Khoảng 1–1,5 giờ (chưa kể di chuyển xa).",
        "best_time_vi": "Cuối xuân và đầu thu để tránh nắng nóng; mùa khô ráo dễ đi lại.",
        "tips_vi": "Ở xa Astrakhan (~120–130 km); mang mũ, nước, giày bám tốt; có thể kết hợp thăm phim trường Sarai-Batu gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Селитренное городище", "url": "https://ru.wikipedia.org/wiki/Селитренное_городище"},
    ],
    ["other", "archaeology", "golden-horde", "sarai", "medieval", "history", "astrakhan"],
    maps_text("Селитренное городище", "Селитренное", "Selitrennoye Site Golden Horde", "Selitrennoye", 47.185000, 47.425000),
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
