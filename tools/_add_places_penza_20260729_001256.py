# -*- coding: utf-8 -*-
"""_add_places_penza_<ts>.py — VÙNG: Tỉnh Penza (Пензенская область), Vùng Volga.
(lần chạy tự động 2026-07-29).

Bối cảnh: penza.json hiện có 7 địa điểm (Тарханы/Lermontov, Музей одной картины, Картинная галерея
им. Савицкого, Золотарёвское городище, Наровчат, памятник «Первопоселенец», Спасский собор). Bổ sung
25 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 32. TRÁNH trùng 7 điểm.

Phân bố loại hình (25 bản ghi mới):
- museum (7): краеведческий музей, музей Ключевского, Дом Мейерхольда (kèm theatre), музей стекла и
  хрусталя (Никольск), музей народного творчества, дом-музей Куприна (Наровчат), музей-усадьба Радищева.
- church (6): Успенский собор, Соборная мечеть (tag mosque), Троице-Сканов монастырь, Сканов пещерный
  монастырь, Михайло-Архангельский собор (Сердобск), Нижнеломовский Казанский монастырь.
- square_street (2): улица Московская, Фонтанная площадь.
- monument (1): Монумент воинской и трудовой славы «Росток».
- park_garden (3): ЦПКиО им. Белинского, Пензенский зоопарк, Ботанический сад им. Спрыгина.
- theatre (3): драмтеатр им. Луначарского, Пензенский цирк, филармония. (Дом Мейерхольда xếp museum+theatre.)
- bridge (1): подвесной мост через Суру («Мост Дружбы»).
- other (2): заповедник «Приволжская лесостепь» (участок «Попереченская степь»), город Кузнецк.

TOẠ ĐỘ — xác minh chéo (columbista.com DMS; autotravel.ru meta-geo; sobory.ru cho nhà thờ/tu viện;
Yandex Maps org ll=LON,LAT; museum.ru; zpls.ru; 2026-07-29). Phạm vi Penza lat ~52.3–54.2, lon ~42.5–47.5
(TP Penza ~53.19, 45.00) — tất cả toạ độ trong phạm vi, KHÔNG đảo lat/lon.

GHI CHÚ: đã BỎ QUA скульптура «Кот учёный» (không xác minh được toạ độ chính xác đáng tin). KHÔNG bịa toạ độ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_penza_<ts>.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "penza"
REGION_NAME_VI = "Tỉnh Penza"
FD = "Vùng Volga"


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


def p(hours, ticket, duration, best, tips):
    return {"hours_vi": hours, "ticket_vi": ticket, "duration_vi": duration,
            "best_time_vi": best, "tips_vi": tips}


RECORDS = []

# ============================ BẢO TÀNG (museum) ============================

# 1) Пензенский краеведческий музей ------------------------------------------------
RECORDS.append(rec(
    "penza-regional-local-lore-museum",
    "Bảo tàng Địa phương học Tỉnh Penza (Kra-ê-vét-trê-xki)",
    "Пензенский краеведческий музей",
    "Penza Regional Museum of Local Lore",
    ["museum"],
    53.186383, 45.007592,
    "Phố Krasnaya 73, trung tâm thành phố Penza, tỉnh Penza, Nga",
    "Bảo tàng lâu đời bậc nhất tỉnh Penza (mở cửa năm 1911), giới thiệu tổng quan thiên nhiên, khảo cổ, dân tộc học và lịch sử vùng đất bên sông Sura. Đây là điểm khởi đầu lý tưởng để hiểu bức tranh toàn cảnh của tỉnh trước khi khám phá những điểm khác.",
    "Bảo tàng Địa phương học Tỉnh Penza (Пензенский краеведческий музей) được thành lập năm 1905 và mở cửa đón khách từ năm 1911, là một trong những bảo tàng lâu đời và giàu sưu tập nhất trong vùng. Toà nhà bảo tàng nằm trên phố Krasnaya, ngay trung tâm lịch sử của thành phố. Các gian trưng bày dẫn dắt du khách đi qua nhiều chủ đề: thế giới tự nhiên của rừng-thảo nguyên vùng Volga với bộ sưu tập động thực vật nhồi, các phát hiện khảo cổ từ những di chỉ cổ (trong đó có văn hoá của người Mordva, Burtas), đời sống dân tộc học của các cộng đồng cư dân, và lịch sử vùng đất từ khi pháo đài Penza được dựng năm 1663 qua các thời kỳ. Bảo tàng cũng lưu giữ nhiều hiện vật gắn với những danh nhân sinh ra hoặc gắn bó với vùng Penza. Với cách sắp đặt mạch lạc và lượng hiện vật phong phú, đây là nơi giúp du khách nắm được cội nguồn và bản sắc của tỉnh Penza chỉ trong một buổi tham quan.",
    [
        "Bảo tàng tổng hợp lâu đời nhất tỉnh (mở cửa 1911) với sưu tập thiên nhiên, khảo cổ, dân tộc học phong phú",
        "Hiện vật về các dân tộc bản địa vùng rừng-thảo nguyên Volga (Mordva, Burtas) và lịch sử pháo đài Penza",
        "Vị trí ngay trung tâm lịch sử, dễ kết hợp với phố đi bộ Moskovskaya và các bảo tàng lân cận",
    ],
    p("Thường mở cửa các ngày trong tuần (trừ thứ Hai), khoảng 10:00-18:00; nên kiểm tra lịch trước khi đi.",
      "Vé vào cửa mức phổ thông, giá phải chăng; có ưu đãi cho học sinh, sinh viên và người cao tuổi.",
      "Khoảng 1-1,5 giờ.",
      "Quanh năm; thuận tiện làm điểm khởi đầu buổi tham quan trung tâm thành phố.",
      "Kết hợp với phòng tranh Savitsky và Bảo tàng một bức tranh ở gần đó; hỏi về tour có hướng dẫn để hiểu sâu hơn."),
    [
        {"title": "Wikipedia (RU) — Пензенский краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Пензенский_краеведческий_музей"},
        {"title": "Columbista — Пензенский краеведческий музей", "url": "https://www.columbista.com/ru/showplace/penzenskii-oblastnoi-kraevedcheskii-muzei"},
    ],
    ["museum", "local-lore", "history", "penza", "volga"],
    maps_org("https://yandex.com/maps/org/penza_state_museum_of_local_lore/1088776353/", "Penza Regional Museum of Local Lore", "Penza"),
))

# 2) Дом-музей В.О. Ключевского -----------------------------------------------------
RECORDS.append(rec(
    "klyuchevsky-house-museum-penza",
    "Nhà-Bảo tàng Sử gia V.O. Klyuchevsky",
    "Дом-музей В.О. Ключевского",
    "V.O. Klyuchevsky House Museum",
    ["museum"],
    53.191903, 45.007731,
    "Phố Klyuchevskogo 66, thành phố Penza, tỉnh Penza, Nga",
    "Bảo tàng tưởng niệm nhà sử học lừng danh người Nga Vasily Klyuchevsky, đặt trong chính ngôi nhà gỗ nơi ông sống thời niên thiếu ở Penza. Không gian tái hiện đời sống thị dân Nga thế kỷ 19 và hành trình trở thành học giả của ông.",
    "Nhà-Bảo tàng V.O. Klyuchevsky (Дом-музей В.О. Ключевского) tôn vinh Vasily Osipovich Klyuchevsky (1841-1911), một trong những nhà sử học vĩ đại nhất của nước Nga, tác giả bộ giáo trình lịch sử Nga kinh điển. Bảo tàng nằm trong ngôi nhà gỗ nơi gia đình Klyuchevsky từng sinh sống khi ông theo học tại chủng viện Penza. Các phòng trưng bày phục dựng nội thất của một gia đình tăng lữ - thị dân Nga giữa thế kỷ 19, đồng thời kể lại chặng đường từ cậu học trò tỉnh lẻ đến vị giáo sư Đại học Moskva được cả nước kính trọng. Du khách có thể xem những kỷ vật, tư liệu, bản thảo và ấn phẩm gắn với sự nghiệp của ông. Đây là một bảo tàng nhỏ nhưng ấm cúng và giàu chất văn hoá, đặc biệt thú vị với những ai yêu lịch sử và văn học Nga; đồng thời cho ta cảm nhận sinh động về nếp sống tỉnh lẻ Nga thời xưa.",
    [
        "Đặt trong ngôi nhà gỗ gắn với thời niên thiếu của sử gia Vasily Klyuchevsky ở Penza",
        "Nội thất phục dựng đời sống gia đình thị dân - tăng lữ Nga giữa thế kỷ 19",
        "Tư liệu, bản thảo, ấn phẩm về sự nghiệp của một trong những nhà sử học lớn nhất nước Nga",
    ],
    p("Thường mở cửa các ngày trong tuần (trừ thứ Hai), khoảng 10:00-18:00; nên kiểm tra lịch trước.",
      "Vé mức phổ thông, giá phải chăng; có ưu đãi cho học sinh, sinh viên.",
      "Khoảng 45-60 phút.",
      "Quanh năm.",
      "Thú vị nhất khi đi cùng hướng dẫn viên để hiểu bối cảnh lịch sử; kết hợp dạo trung tâm lịch sử Penza."),
    [
        {"title": "Wikipedia (RU) — Ключевский, Василий Осипович", "url": "https://ru.wikipedia.org/wiki/Ключевский,_Василий_Осипович"},
        {"title": "Columbista — Дом-музей В.О. Ключевского", "url": "https://www.columbista.com/ru/showplace/dom-muzei-vo-kliuchevskogo"},
    ],
    ["museum", "memorial", "history", "literature", "penza"],
    maps_org("https://yandex.com/maps/org/v_o_klyuchevsky_house_museum/1014456709/", "V.O. Klyuchevsky House Museum", "Penza"),
))

# 3) Дом Мейерхольда (театр-музей) --------------------------------------------------
RECORDS.append(rec(
    "meyerhold-house-museum-penza",
    "Ngôi nhà Meyerhold (Nhà hát - Bảo tàng)",
    "Дом Мейерхольда",
    "Meyerhold House (Theatre-Museum)",
    ["museum", "theatre"],
    53.194557, 45.014561,
    "Phố Volodarskogo 59, thành phố Penza, tỉnh Penza, Nga",
    "Bảo tàng kiêm nhà hát thể nghiệm tưởng niệm đạo diễn sân khấu cách tân Vsevolod Meyerhold, đặt trong ngôi nhà gỗ thời thơ ấu của ông ở Penza. Đây là nhà hát duy nhất trên thế giới mang tên Meyerhold, kết hợp trưng bày bảo tàng với các buổi diễn sống động.",
    "Ngôi nhà Meyerhold (Дом Мейерхольда), còn gọi là Trung tâm Sân khấu tưởng niệm V.E. Meyerhold, là một địa chỉ văn hoá độc đáo của Penza. Vsevolod Meyerhold (1874-1940) sinh ra và lớn lên tại chính ngôi nhà này trước khi trở thành một trong những đạo diễn sân khấu cách tân và có ảnh hưởng nhất thế kỷ 20. Ngày nay, toà nhà gỗ được phục dựng vừa là bảo tàng lưu giữ kỷ vật, tư liệu về cuộc đời và di sản nghệ thuật của ông, vừa là một nhà hát thể nghiệm nhỏ hoạt động thường xuyên - được xem là nhà hát duy nhất trên thế giới mang tên Meyerhold. Trước nhà là bức tượng đài Meyerhold độc đáo. Du khách có thể vừa tham quan phần trưng bày bảo tàng, vừa (nếu đúng lịch) thưởng thức một vở diễn trong không gian ấm cúng, cảm nhận tinh thần tìm tòi, phá cách mà tên tuổi Meyerhold đại diện. Đây là điểm đến hấp dẫn cho người yêu sân khấu và văn hoá Nga.",
    [
        "Nhà hát duy nhất trên thế giới mang tên đạo diễn cách tân Vsevolod Meyerhold",
        "Đặt trong ngôi nhà gỗ thời thơ ấu của ông, kết hợp bảo tàng và nhà hát thể nghiệm còn hoạt động",
        "Tượng đài Meyerhold ấn tượng phía trước và không gian sân khấu ấm cúng",
    ],
    p("Phần bảo tàng mở ban ngày (trừ thứ Hai); các buổi diễn theo lịch riêng, thường vào buổi tối.",
      "Vé tham quan bảo tàng phải chăng; vé xem kịch tuỳ suất diễn, nên đặt trước.",
      "Tham quan bảo tàng khoảng 45 phút; xem một vở diễn khoảng 1,5-2 giờ.",
      "Quanh năm; kiểm tra lịch diễn nếu muốn xem kịch.",
      "Xem trước lịch suất diễn trên trang chính thức và đặt vé sớm vì khán phòng nhỏ."),
    [
        {"title": "Wikipedia (RU) — Мейерхольд, Всеволод Эмильевич", "url": "https://ru.wikipedia.org/wiki/Мейерхольд,_Всеволод_Эмильевич"},
        {"title": "Yandex Maps — Дом Мейерхольда", "url": "https://yandex.com/maps/org/dom_meyerkholda/1055830396/"},
    ],
    ["museum", "theatre", "memorial", "meyerhold", "penza"],
    maps_org("https://yandex.com/maps/org/dom_meyerkholda/1055830396/", "Meyerhold House Theatre-Museum", "Penza"),
))

# 4) Музей стекла и хрусталя (Никольск) ---------------------------------------------
RECORDS.append(rec(
    "glass-crystal-museum-nikolsk",
    "Bảo tàng Thuỷ tinh và Pha lê Nikolsk",
    "Никольский музей стекла и хрусталя",
    "Nikolsk Museum of Glass and Crystal",
    ["museum"],
    53.716083, 46.093717,
    "Phố Komsomolskaya 21, thành phố Nikolsk, tỉnh Penza, Nga",
    "Bảo tàng nghề thuỷ tinh - pha lê nổi tiếng nhất vùng Volga, ở thị trấn Nikolsk - cái nôi của nghề pha lê Nga từ nhà máy Bakhmetev thế kỷ 18. Bộ sưu tập hàng nghìn tác phẩm thuỷ tinh, pha lê tinh xảo trải dài hơn hai thế kỷ.",
    "Bảo tàng Thuỷ tinh và Pha lê ở Nikolsk (Никольский музей стекла и хрусталя) là một trong những bảo tàng chuyên đề độc đáo và giá trị nhất nước Nga về nghệ thuật thuỷ tinh. Thị trấn Nikolsk gắn liền với xưởng thuỷ tinh - pha lê Bakhmetev (thành lập cuối thế kỷ 18), nơi từng cung cấp sản phẩm cho cả hoàng gia Nga. Bảo tàng lưu giữ bộ sưu tập lên tới hàng chục nghìn hiện vật, từ những kiệt tác pha lê chạm khắc, thổi tay, mạ vàng đẽo gọt công phu cho tới đồ thuỷ tinh nghệ thuật hiện đại và các sản phẩm thời Xô Viết. Qua các gian trưng bày, du khách thấy được sự phát triển của kỹ thuật và thẩm mỹ thuỷ tinh Nga suốt hơn 200 năm: những bộ ly, bình, chân đèn, tác phẩm điêu khắc bằng pha lê lung linh dưới ánh sáng. Đây là điểm đến đáng để đi thêm quãng đường từ Penza, đặc biệt với người yêu nghệ thuật ứng dụng và lịch sử thủ công.",
    [
        "Cái nôi nghề pha lê Nga - gắn với xưởng Bakhmetev từ cuối thế kỷ 18",
        "Bộ sưu tập hàng chục nghìn hiện vật thuỷ tinh - pha lê trải dài hơn 200 năm",
        "Kiệt tác pha lê chạm khắc, thổi tay, mạ vàng cùng đồ thuỷ tinh nghệ thuật thời Xô Viết và hiện đại",
    ],
    p("Thường mở cửa các ngày trong tuần (trừ thứ Hai), ban ngày; nên gọi kiểm tra vì ở xa.",
      "Vé mức phổ thông; có thể có phụ phí cho chụp ảnh.",
      "Khoảng 1-1,5 giờ (chưa kể thời gian di chuyển).",
      "Quanh năm; nên đi ban ngày để tiện đường về.",
      "Nikolsk cách Penza khoảng 120 km về phía đông bắc - nên chủ động phương tiện và tính thời gian đi lại."),
    [
        {"title": "Museum.ru — Никольский музей стекла и хрусталя (M2771)", "url": "http://www.museum.ru/M2771"},
        {"title": "Wikipedia (RU) — Никольск (Пензенская область)", "url": "https://ru.wikipedia.org/wiki/Никольск_(Пензенская_область)"},
    ],
    ["museum", "glass", "crystal", "craft", "nikolsk", "penza"],
    maps_text("Музей стекла и хрусталя", "Никольск", "Museum of Glass and Crystal", "Nikolsk", 53.716083, 46.093717),
))

# 5) Пензенский музей народного творчества ------------------------------------------
RECORDS.append(rec(
    "museum-of-folk-art-penza",
    "Bảo tàng Nghệ thuật Dân gian Penza",
    "Пензенский музей народного творчества",
    "Penza Museum of Folk Art",
    ["museum"],
    53.175240, 45.005550,
    "Phố Kuybysheva 45A, thành phố Penza, tỉnh Penza, Nga",
    "Bảo tàng nghề thủ công dân gian đặt trong một biệt thự gỗ chạm khắc tinh xảo cuối thế kỷ 19 - bản thân toà nhà đã là một tác phẩm. Nơi đây tôn vinh các nghề truyền thống của vùng Penza: chạm gỗ, dệt, gốm, thêu, đồ chơi Abashevo.",
    "Bảo tàng Nghệ thuật Dân gian Penza (Пензенский музей народного творчества) là nơi lưu giữ và tôn vinh di sản thủ công của vùng đất Penza. Điểm đặc biệt đầu tiên chính là toà nhà: một biệt thự gỗ cuối thế kỷ 19 với những đường chạm khắc gỗ (rezba) cầu kỳ ở lan can, mái hiên, khung cửa - được xem như một mẫu mực của kiến trúc gỗ trang trí Nga. Bên trong trưng bày các bộ sưu tập nghề dân gian tiêu biểu của tỉnh: đồ chơi gốm Abashevo với hình thú ngộ nghĩnh phủ men óng ánh (một thương hiệu nổi tiếng của Penza), sản phẩm chạm gỗ, đan lát, dệt vải, thêu ren, gốm và đồ sứ. Du khách có thể chiêm ngưỡng tay nghề của các nghệ nhân qua nhiều thế hệ và hiểu thêm về đời sống, tín ngưỡng, thẩm mỹ dân gian của người dân vùng Volga. Không gian ấm cúng, đậm chất truyền thống, thích hợp cho cả gia đình.",
    [
        "Toà biệt thự gỗ chạm khắc tinh xảo cuối thế kỷ 19 - bản thân là một tác phẩm kiến trúc",
        "Đồ chơi gốm Abashevo nổi tiếng cùng nghề chạm gỗ, dệt, thêu, gốm của vùng Penza",
        "Không gian trưng bày ấm cúng, phù hợp tìm hiểu văn hoá dân gian và đi cùng gia đình",
    ],
    p("Thường mở cửa các ngày trong tuần (trừ thứ Hai), ban ngày; nên kiểm tra lịch trước.",
      "Vé mức phổ thông, giá phải chăng.",
      "Khoảng 45-60 phút.",
      "Quanh năm.",
      "Dành thời gian ngắm phần chạm gỗ bên ngoài toà nhà; hỏi mua đồ chơi Abashevo làm quà lưu niệm nếu có gian bán."),
    [
        {"title": "Wikipedia (RU) — Музей народного творчества (Пенза)", "url": "https://ru.wikipedia.org/wiki/Музей_народного_творчества_(Пенза)"},
        {"title": "Autotravel.ru — Музей народного творчества", "url": "https://autotravel.ru/otklik.php/2559"},
    ],
    ["museum", "folk-art", "craft", "wooden-architecture", "penza"],
    maps_org("https://yandex.com/maps/org/museum_of_folk_art/1016033363/", "Penza Museum of Folk Art", "Penza"),
))

# 6) Дом-музей А.И. Куприна (Наровчат) ----------------------------------------------
RECORDS.append(rec(
    "kuprin-house-museum-narovchat",
    "Nhà-Bảo tàng Nhà văn A.I. Kuprin (Narovchat)",
    "Дом-музей А.И. Куприна",
    "A.I. Kuprin House Museum",
    ["museum"],
    53.876950, 43.699920,
    "Phố Kuprina 2, làng Narovchat, huyện Narovchatsky, tỉnh Penza, Nga",
    "Bảo tàng văn học duy nhất trên thế giới dành cho nhà văn Nga Aleksandr Kuprin, đặt tại chính quê hương ông - làng cổ Narovchat. Nơi tái hiện tuổi thơ và sự nghiệp của tác giả những tác phẩm kinh điển như 'Chiếc vòng thạch lựu', 'Olesya'.",
    "Nhà-Bảo tàng A.I. Kuprin (Дом-музей А.И. Куприна) ở Narovchat là bảo tàng đầu tiên và duy nhất trên thế giới dành riêng cho nhà văn Aleksandr Ivanovich Kuprin (1870-1938) - một trong những cây bút văn xuôi lớn của văn học Nga, tác giả các truyện nổi tiếng như 'Chiếc vòng thạch lựu' (Гранатовый браслет), 'Olesya', 'Song đấu'. Kuprin sinh ra tại Narovchat, và bảo tàng được lập tại khu nhà gắn với gia đình ông. Các phòng trưng bày phục dựng không gian sống của gia đình Kuprin cuối thế kỷ 19, giới thiệu ảnh, thư từ, bản thảo, ấn phẩm và kỷ vật kể lại cuộc đời nhiều thăng trầm của nhà văn - từ tuổi thơ nghèo khó, những năm binh nghiệp, đến sự nghiệp văn chương và quãng đời lưu vong rồi trở về Tổ quốc. Kết hợp với chuyến thăm thị trấn cổ Narovchat, đây là điểm dừng chân giàu cảm xúc cho người yêu văn học Nga.",
    [
        "Bảo tàng duy nhất trên thế giới dành cho nhà văn Aleksandr Kuprin, tại chính quê hương ông",
        "Phục dựng không gian sống của gia đình Kuprin và trưng bày bản thảo, thư từ, kỷ vật",
        "Gắn với các tác phẩm kinh điển như 'Chiếc vòng thạch lựu', 'Olesya'",
    ],
    p("Thường mở cửa ban ngày (trừ thứ Hai); nên kiểm tra lịch vì ở xa trung tâm tỉnh.",
      "Vé mức phổ thông, giá phải chăng.",
      "Khoảng 45-60 phút.",
      "Quanh năm; đẹp nhất khi kết hợp tour Narovchat vào mùa ấm.",
      "Narovchat cách Penza khoảng 140 km về phía tây bắc - nên gộp thăm cùng tu viện Troitse-Skanov và hang động Skanov."),
    [
        {"title": "Wikipedia (RU) — Куприн, Александр Иванович", "url": "https://ru.wikipedia.org/wiki/Куприн,_Александр_Иванович"},
        {"title": "Autotravel.ru — Дом-музей А.И. Куприна", "url": "https://autotravel.ru/otklik.php/2555"},
    ],
    ["museum", "literature", "memorial", "kuprin", "narovchat", "penza"],
    maps_text("Дом-музей А.И. Куприна", "Наровчат", "Kuprin House Museum", "Narovchat", 53.876950, 43.699920),
))

# 7) Музей-усадьба А.Н. Радищева (Верхнее Аблязово) ---------------------------------
RECORDS.append(rec(
    "radishchev-estate-museum",
    "Điền trang - Bảo tàng A.N. Radishchev (Verkhnee Ablyazovo)",
    "Музей-усадьба А.Н. Радищева",
    "A.N. Radishchev Estate Museum",
    ["museum"],
    53.048069, 46.434872,
    "Làng Radishchevo (Verkhnee Ablyazovo), huyện Kuznetsky, tỉnh Penza, Nga",
    "Điền trang - bảo tàng tưởng niệm nhà văn, nhà tư tưởng Aleksandr Radishchev (tác giả 'Hành trình từ Peterburg đến Moskva'), nơi ông sống thời thơ ấu. Quần thể gồm bảo tàng và nhà thờ Đấng Cứu Thế barok thế kỷ 18 tuyệt đẹp.",
    "Điền trang - Bảo tàng A.N. Radishchev (Музей-усадьба А.Н. Радищева) nằm ở làng Radishchevo (tên cũ Verkhnee Ablyazovo), gắn với tuổi thơ của Aleksandr Nikolaevich Radishchev (1749-1802) - nhà văn, triết gia khai sáng nổi tiếng, tác giả tác phẩm 'Hành trình từ Peterburg đến Moskva' từng gây chấn động vì phê phán chế độ nông nô. Khu điền trang tổ tiên của dòng họ Radishchev nay là một quần thể bảo tàng - văn học - lịch sử. Bên cạnh phần trưng bày về cuộc đời và di sản tư tưởng của Radishchev, điểm nhấn kiến trúc là nhà thờ Đấng Cứu Thế Không Do Tay Người Tạo (Спаса Нерукотворного Образа) xây giữa thế kỷ 18 theo phong cách barok, với nội thất chạm khắc gỗ mạ vàng và bộ tượng thánh (iконостас) được đánh giá cao. Không gian yên bình của làng quê Nga cùng câu chuyện về một nhân vật quan trọng trong lịch sử tư tưởng Nga khiến đây là điểm đến ý nghĩa cho những chuyến đi sâu vào vùng Kuznetsky.",
    [
        "Điền trang tổ tiên gắn với tuổi thơ nhà tư tưởng khai sáng Aleksandr Radishchev",
        "Nhà thờ Đấng Cứu Thế barok giữa thế kỷ 18 với bộ tượng thánh chạm gỗ mạ vàng đặc sắc",
        "Không gian làng quê Nga yên bình, gắn với 'Hành trình từ Peterburg đến Moskva'",
    ],
    p("Thường mở cửa ban ngày (trừ thứ Hai); nên liên hệ trước vì ở vùng nông thôn xa.",
      "Vé mức phổ thông, giá phải chăng.",
      "Khoảng 1-1,5 giờ.",
      "Mùa xuân đến mùa thu, khi đường sá và cảnh quan làng quê thuận lợi.",
      "Nằm ở huyện Kuznetsky, cách Penza hơn 150 km - nên chủ động ô tô và kết hợp thăm thành phố Kuznetsk."),
    [
        {"title": "Wikipedia (RU) — Радищево (Пензенская область)", "url": "https://ru.wikipedia.org/wiki/Радищево_(Пензенская_область)"},
        {"title": "Altertravel.ru — Музей-усадьба Радищева", "url": "https://altertravel.ru/poi/4337"},
    ],
    ["museum", "estate", "literature", "church", "radishchev", "penza"],
    maps_text("Музей-усадьба А.Н. Радищева", "Радищево Пензенская область", "Radishchev Estate Museum", "Radishchevo", 53.048069, 46.434872),
))

# ============================ TÔN GIÁO (church) ============================

# 8) Успенский кафедральный собор ---------------------------------------------------
RECORDS.append(rec(
    "uspensky-cathedral-penza",
    "Nhà thờ Chính toà Đức Mẹ An Giấc (Uspensky)",
    "Успенский кафедральный собор",
    "Dormition (Uspensky) Cathedral",
    ["church"],
    53.193481, 44.994477,
    "Phố Zakharova 6, thành phố Penza, tỉnh Penza, Nga",
    "Nhà thờ chính toà lớn của giáo phận Penza, công trình gạch đỏ phong cách chiết trung đầu thế kỷ 20, nổi bật với năm mái vòm. Ngôi thánh đường từng sống sót qua thời Xô Viết và nay là trung tâm đời sống Chính Thống giáo của thành phố.",
    "Nhà thờ Chính toà Đức Mẹ An Giấc (Успенский кафедральный собор) là ngôi thánh đường Chính Thống giáo quan trọng bậc nhất của thành phố Penza. Được xây dựng vào những năm 1895-1905 bằng gạch đỏ theo phong cách chiết trung (kết hợp yếu tố tân-Nga), nhà thờ gây ấn tượng với khối kiến trúc bề thế cùng năm mái vòm (kupol) và tháp chuông vươn cao. Trong thời kỳ Xô Viết, khi phần lớn nhà thờ ở Penza bị phá huỷ hoặc đóng cửa, Uspensky là một trong số ít công trình tôn giáo được giữ lại và có giai đoạn giữ vai trò nhà thờ chính toà của giáo phận. Ngày nay đây là trung tâm sinh hoạt tôn giáo sầm uất: nội thất được trang hoàng với các bức icon, tranh tường và bộ tượng thánh, không gian thanh tịnh và trang nghiêm. Du khách ghé thăm sẽ cảm nhận được nhịp sống tâm linh của người dân Penza cũng như vẻ đẹp của kiến trúc nhà thờ Nga đầu thế kỷ 20.",
    [
        "Nhà thờ chính toà giáo phận Penza, công trình gạch đỏ đầu thế kỷ 20 với năm mái vòm",
        "Một trong số ít thánh đường sống sót qua thời Xô Viết ở Penza",
        "Nội thất icon, tranh tường và bộ tượng thánh trang nghiêm, trung tâm đời sống Chính Thống giáo",
    ],
    p("Mở cửa hằng ngày cho tín đồ và khách tham quan, thường từ sáng sớm đến chiều tối theo giờ lễ.",
      "Miễn phí (hoan nghênh quyên góp tuỳ tâm).",
      "Khoảng 20-40 phút.",
      "Quanh năm; các dịp lễ lớn của Chính Thống giáo rất trang trọng nhưng đông người.",
      "Ăn mặc kín đáo; nữ nên trùm khăn khi vào; giữ yên lặng và xin phép trước khi chụp ảnh bên trong."),
    [
        {"title": "Wikipedia (RU) — Успенский собор (Пенза)", "url": "https://ru.wikipedia.org/wiki/Успенский_собор_(Пенза)"},
        {"title": "Sobory.ru — Успенский кафедральный собор (object 18552)", "url": "https://sobory.ru/article/?object=18552"},
    ],
    ["church", "cathedral", "orthodox", "architecture", "penza"],
    maps_org("https://yandex.com/maps/org/cathedral_of_the_assumption_of_our_lady/1125131838/", "Dormition Cathedral", "Penza"),
))

# 9) Пензенская соборная мечеть -----------------------------------------------------
RECORDS.append(rec(
    "penza-cathedral-mosque",
    "Thánh đường Hồi giáo Trung tâm Penza",
    "Пензенская соборная мечеть",
    "Penza Cathedral Mosque",
    ["church"],
    53.198200, 45.026700,
    "Phố Bakunina 8/10, thành phố Penza, tỉnh Penza, Nga",
    "Thánh đường Hồi giáo trung tâm của Penza, phục vụ cộng đồng Hồi giáo Tatar đông đảo trong vùng. Công trình với mái vòm và tháp minaret là một nét chấm phá đa văn hoá giữa lòng thành phố Volga.",
    "Thánh đường Hồi giáo Trung tâm Penza (Пензенская соборная мечеть) là ngôi đền thờ Hồi giáo chính của thành phố, phục vụ cộng đồng người Tatar và các dân tộc theo đạo Hồi vốn có mặt lâu đời ở vùng Volga - Penza. Penza từng có nhà thờ Hồi giáo từ cuối thế kỷ 19; công trình hiện nay tiếp nối truyền thống đó và là trung tâm sinh hoạt tôn giáo, văn hoá của cộng đồng Hồi giáo địa phương. Kiến trúc với mái vòm và tháp minaret mang phong cách đền thờ Hồi giáo cổ điển, tạo nên sự tương phản thú vị với những mái vòm nhà thờ Chính Thống giáo gần đó - phản ánh bức tranh đa tôn giáo, đa sắc tộc đặc trưng của vùng Volga. Du khách ghé thăm (ngoài giờ cầu nguyện, và tôn trọng quy tắc) có thể tìm hiểu về đời sống của cộng đồng Hồi giáo Nga và chiêm ngưỡng một công trình tôn giáo khác biệt trong lòng thành phố.",
    [
        "Thánh đường Hồi giáo trung tâm của Penza, phục vụ cộng đồng Tatar và người Hồi giáo vùng Volga",
        "Kiến trúc mái vòm và tháp minaret cổ điển, điểm nhấn đa văn hoá của thành phố",
        "Phản ánh bức tranh đa tôn giáo, đa sắc tộc đặc trưng của vùng sông Volga",
    ],
    p("Mở cửa theo giờ cầu nguyện; khách không theo đạo nên đến ngoài giờ lễ và hỏi phép trước.",
      "Miễn phí.",
      "Khoảng 15-30 phút.",
      "Quanh năm; tránh giờ cầu nguyện thứ Sáu (jumu'ah) nếu chỉ muốn tham quan.",
      "Ăn mặc kín đáo, bỏ giày trước khi vào khu cầu nguyện; nữ nên trùm khăn; giữ thái độ tôn trọng."),
    [
        {"title": "Wikipedia (RU) — Пензенская соборная мечеть", "url": "https://ru.wikipedia.org/wiki/Пензенская_соборная_мечеть"},
    ],
    ["church", "mosque", "islam", "tatar", "penza"],
    maps_text("Пензенская соборная мечеть", "Пенза", "Penza Cathedral Mosque", "Penza", 53.198200, 45.026700),
))

# 10) Троице-Сканов монастырь (Наровчат) --------------------------------------------
RECORDS.append(rec(
    "trinity-scanov-monastery",
    "Tu viện Troitse-Skanov (Chúa Ba Ngôi)",
    "Троице-Сканов монастырь",
    "Trinity-Scanov Monastery",
    ["church"],
    53.864846, 43.752707,
    "Làng Skanovo, gần Narovchat, huyện Narovchatsky, tỉnh Penza, Nga",
    "Tu viện nữ Chính Thống giáo tuyệt đẹp gần Narovchat, với quần thể thánh đường barok - cổ điển màu trắng xây cuối thế kỷ 18. Đây là một trong những trung tâm hành hương và điểm đến kiến trúc nổi bật nhất tỉnh Penza.",
    "Tu viện Troitse-Skanov (Троице-Сканов монастырь) là một quần thể tu viện Chính Thống giáo nằm bên rìa làng Skanovo, gần thị trấn cổ Narovchat, cách Penza khoảng 160 km. Được xây dựng chủ yếu vào cuối thế kỷ 18 - đầu thế kỷ 19, tu viện gây ấn tượng mạnh với nhà thờ Chúa Ba Ngôi hai tầng bề thế màu trắng, kết hợp phong cách barok muộn và cổ điển, cùng tường bao, tháp góc và cổng tu viện tạo thành một tổng thể hài hoà giữa khung cảnh đồng quê. Ban đầu là tu viện nam, ngày nay đây là tu viện nữ đang hoạt động và là một trung tâm hành hương quan trọng, đặc biệt gắn với icon Đức Mẹ Trubchevskaya được tôn kính. Vẻ đẹp thanh bình, kiến trúc trắng nổi bật trên nền trời và không khí tĩnh lặng khiến Troitse-Skanov trở thành một trong những điểm đến tâm linh - kiến trúc đáng nhớ nhất của tỉnh, thường được kết hợp cùng chuyến thăm hang động Skanov gần đó.",
    [
        "Quần thể tu viện màu trắng barok - cổ điển cuối thế kỷ 18 giữa khung cảnh đồng quê",
        "Tu viện nữ đang hoạt động, trung tâm hành hương với icon Đức Mẹ Trubchevskaya",
        "Thường kết hợp cùng hang động Skanov và thị trấn cổ Narovchat trong một hành trình",
    ],
    p("Mở cửa cho khách hành hương và tham quan ban ngày; giữ trật tự khu tu viện.",
      "Miễn phí (hoan nghênh quyên góp).",
      "Khoảng 40-60 phút.",
      "Mùa xuân đến mùa thu khi cảnh quan đẹp và đường thuận lợi.",
      "Ăn mặc kín đáo, nữ trùm khăn và mặc váy (thường có khăn/váy cho mượn ở cổng); gộp thăm hang động Skanov cách vài km."),
    [
        {"title": "Wikipedia (RU) — Троице-Сканов монастырь", "url": "https://ru.wikipedia.org/wiki/Троице-Сканов_монастырь"},
        {"title": "Sobory.ru — Троице-Сканов монастырь (object 02766)", "url": "https://sobory.ru/article/?object=02766"},
    ],
    ["church", "monastery", "orthodox", "pilgrimage", "narovchat", "penza"],
    maps_text("Троице-Сканов монастырь", "Наровчат", "Trinity-Scanov Monastery", "Narovchat", 53.864846, 43.752707),
))

# 11) Сканов пещерный монастырь (пещеры) --------------------------------------------
RECORDS.append(rec(
    "scanov-caves-monastery",
    "Tu viện Hang động Skanov (hang động Naravchat)",
    "Сканов пещерный монастырь",
    "Scanov Cave Monastery",
    ["church"],
    53.858615, 43.779094,
    "Núi Plodskaya, gần làng Skanovo và Narovchat, huyện Narovchatsky, tỉnh Penza, Nga",
    "Tu viện hang động đào sâu trong lòng núi Plodskaya, với hệ thống địa đạo nhiều tầng dài hàng trăm mét - được coi là dài bậc nhất trong các tu viện hang động ở Nga. Điểm hành hương độc đáo gần tu viện Troitse-Skanov.",
    "Tu viện Hang động Skanov (Сканов пещерный монастырь), thờ hai vị thánh Anthony và Feodosy vùng Pechersk, là một quần thể tu viện đào trong lòng núi Plodskaya, cách tu viện Troitse-Skanov vài km. Từ thế kỷ 18-19, các tu sĩ đã đào một hệ thống địa đạo, phòng nguyện và hầm mộ nhiều tầng xuyên vào sườn đồi đá vôi; tổng chiều dài các đường hầm được ước tính lên tới hàng trăm mét, khiến đây được xem là một trong những tu viện hang động dài nhất nước Nga. Đi trong lòng núi mát lạnh, tĩnh mịch, chỉ với ánh nến hoặc đèn, du khách và người hành hương cảm nhận rõ đời sống khổ hạnh của các đan sĩ xưa. Ngày nay tu viện hang động đã được phục hồi hoạt động; một phần địa đạo mở cho khách thăm có hướng dẫn. Kết hợp cùng tu viện Troitse-Skanov và thị trấn Narovchat, đây là một trong những trải nghiệm độc đáo và ấn tượng nhất của du lịch tỉnh Penza.",
    [
        "Hệ thống địa đạo nhiều tầng đào trong núi đá vôi - thuộc hàng dài nhất trong các tu viện hang động ở Nga",
        "Không gian tĩnh mịch, mát lạnh gợi lại đời sống khổ hạnh của các đan sĩ xưa",
        "Gần tu viện Troitse-Skanov, tạo thành cụm hành hương độc đáo của Narovchat",
    ],
    p("Tham quan hang động thường theo tour có hướng dẫn ban ngày; nên liên hệ trước.",
      "Có thể miễn phí hoặc quyên góp tuỳ tâm; tour hang động đôi khi thu phí nhỏ.",
      "Khoảng 40-60 phút.",
      "Quanh năm (trong hang mát ổn định), thuận tiện nhất vào mùa ấm khi đường tốt.",
      "Mang áo khoác vì trong hang lạnh; mang đèn pin; đi giày bám tốt; theo hướng dẫn viên và giữ trật tự."),
    [
        {"title": "Wikipedia (RU) — Сканов пещерный монастырь", "url": "https://ru.wikipedia.org/wiki/Сканов_пещерный_монастырь"},
        {"title": "Sobory.ru — Пещерный монастырь (object 20475)", "url": "https://sobory.ru/article/?object=20475"},
    ],
    ["church", "monastery", "caves", "pilgrimage", "narovchat", "penza"],
    maps_text("Сканов пещерный монастырь", "Наровчат", "Scanov Cave Monastery", "Narovchat", 53.858615, 43.779094),
))

# 12) Михайло-Архангельский собор (Сердобск) ----------------------------------------
RECORDS.append(rec(
    "mikhailo-arkhangelsk-cathedral-serdobsk",
    "Nhà thờ Tổng lãnh Thiên thần Mikael (Serdobsk)",
    "Михайло-Архангельский собор",
    "Cathedral of the Archangel Michael",
    ["church"],
    52.454487, 44.203767,
    "Quảng trường Sobornaya 1, thành phố Serdobsk, tỉnh Penza, Nga",
    "Nhà thờ chính toà nguy nga của thành phố Serdobsk, công trình gạch đỏ đầu thế kỷ 20 với năm mái vòm và tháp chuông cao vút - một trong những thánh đường đẹp và đồ sộ nhất tỉnh Penza.",
    "Nhà thờ Tổng lãnh Thiên thần Mikael (Михайло-Архангельский собор) ở Serdobsk là một trong những công trình tôn giáo bề thế và đẹp nhất tỉnh Penza. Được xây dựng vào những năm 1895-1905 bằng gạch đỏ theo phong cách tân-Byzantine, nhà thờ nổi bật với khối kiến trúc đồ sộ, năm mái vòm lớn và tháp chuông vươn cao, có sức chứa hàng nghìn người. Đứng giữa quảng trường trung tâm thị trấn nhỏ Serdobsk (nằm ở phía tây nam tỉnh), ngôi thánh đường tạo nên một điểm nhấn thị giác mạnh mẽ, được ví như 'viên ngọc' của thành phố. Sống sót qua thời Xô Viết dù chịu nhiều tổn thất, nhà thờ đã được trùng tu và ngày nay là trung tâm đời sống Chính Thống giáo của cả vùng. Vẻ tráng lệ của kiến trúc gạch đỏ với những chi tiết trang trí tinh xảo khiến đây là điểm dừng chân xứng đáng cho du khách khám phá vùng Serdobsk - Bekovo.",
    [
        "Một trong những nhà thờ đồ sộ và đẹp nhất tỉnh Penza, xây đầu thế kỷ 20",
        "Kiến trúc gạch đỏ tân-Byzantine với năm mái vòm và tháp chuông cao vút",
        "Trung tâm Chính Thống giáo của thành phố Serdobsk ở phía tây nam tỉnh",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường từ sáng đến chiều tối.",
      "Miễn phí (hoan nghênh quyên góp).",
      "Khoảng 20-40 phút.",
      "Quanh năm.",
      "Serdobsk cách Penza khoảng 110 km về phía tây nam; ăn mặc kín đáo, nữ trùm khăn khi vào."),
    [
        {"title": "Wikipedia (RU) — Сердобск", "url": "https://ru.wikipedia.org/wiki/Сердобск"},
        {"title": "Sobory.ru — Михайло-Архангельский собор, Сердобск (object 21381)", "url": "https://sobory.ru/article/?object=21381"},
    ],
    ["church", "cathedral", "orthodox", "architecture", "serdobsk", "penza"],
    maps_text("Михайло-Архангельский собор", "Сердобск", "Cathedral of the Archangel Michael", "Serdobsk", 52.454487, 44.203767),
))

# 13) Нижнеломовский Казанский Богородицкий монастырь -------------------------------
RECORDS.append(rec(
    "nizhnelomovsky-kazansky-monastery",
    "Tu viện Kazan Đức Mẹ Nizhny Lomov",
    "Нижнеломовский Казанский Богородицкий монастырь",
    "Nizhny Lomov Kazan Monastery",
    ["church"],
    53.530480, 43.635049,
    "Làng Norovka, gần thành phố Nizhny Lomov, huyện Nizhnelomovsky, tỉnh Penza, Nga",
    "Tu viện nam Chính Thống giáo cổ gắn với sự hiển linh của icon Đức Mẹ Kazan ở đầu nguồn suối thiêng. Trung tâm hành hương lâu đời ở phía tây bắc tỉnh Penza, được phục dựng sau thời Xô Viết.",
    "Tu viện Kazan Đức Mẹ Nizhny Lomov (Нижнеломовский Казанский Богородицкий монастырь) là một trong những tu viện lâu đời và được tôn kính của vùng Penza, toạ lạc ở làng Norovka gần thành phố Nizhny Lomov. Theo truyền thuyết, tu viện ra đời từ giữa thế kỷ 17 tại nơi hiển linh của một bản icon Đức Mẹ Kazan bên một dòng suối, và nhanh chóng trở thành điểm hành hương thu hút tín đồ khắp vùng. Trải qua thời hưng thịnh với nhiều thánh đường, tu viện bị đóng cửa và tàn phá trong thời Xô Viết, rồi được khôi phục trong những thập niên gần đây. Ngày nay, quần thể tu viện cùng dòng suối thiêng và giếng nước thánh (kupel) tiếp tục đón khách hành hương đến cầu nguyện và lấy nước. Không khí tĩnh lặng, câu chuyện lịch sử - tâm linh và khung cảnh đồng quê khiến đây là điểm đến ý nghĩa cho những ai muốn tìm hiểu đời sống Chính Thống giáo truyền thống của vùng Penza.",
    [
        "Tu viện gắn với truyền thuyết hiển linh icon Đức Mẹ Kazan từ giữa thế kỷ 17",
        "Dòng suối thiêng và giếng nước thánh (kupel) thu hút khách hành hương",
        "Trung tâm hành hương lâu đời ở phía tây bắc tỉnh, được phục dựng sau thời Xô Viết",
    ],
    p("Mở cửa cho khách hành hương và tham quan ban ngày.",
      "Miễn phí (hoan nghênh quyên góp).",
      "Khoảng 30-45 phút.",
      "Mùa xuân đến mùa thu; các dịp lễ Đức Mẹ Kazan rất đông khách hành hương.",
      "Nizhny Lomov cách Penza khoảng 110 km về phía tây bắc; ăn mặc kín đáo; mang chai nếu muốn lấy nước thánh."),
    [
        {"title": "Wikipedia (RU) — Нижнеломовский Казанский монастырь", "url": "https://ru.wikipedia.org/wiki/Нижнеломовский_Казанский_монастырь"},
        {"title": "Sobory.ru — Нижнеломовский Казанский монастырь (object 20477)", "url": "https://sobory.ru/article/?object=20477"},
    ],
    ["church", "monastery", "orthodox", "pilgrimage", "nizhny-lomov", "penza"],
    maps_text("Нижнеломовский Казанский монастырь", "Норовка Пензенская область", "Nizhny Lomov Kazan Monastery", "Norovka", 53.530480, 43.635049),
))

# ============================ QUẢNG TRƯỜNG / PHỐ (square_street) ============================

# 14) Улица Московская (phố đi bộ) --------------------------------------------------
RECORDS.append(rec(
    "moskovskaya-street-penza",
    "Phố đi bộ Moskovskaya",
    "Улица Московская",
    "Moskovskaya Street",
    ["square_street"],
    53.190690, 45.015650,
    "Phố Moskovskaya (đoạn đi bộ), trung tâm thành phố Penza, tỉnh Penza, Nga",
    "Trục phố đi bộ chính và cổ nhất của Penza, trái tim sinh hoạt của thành phố. Con phố lát đá quy tụ những công trình lịch sử, cửa hàng, quán cà phê, đài phun nước và các tác phẩm điêu khắc đường phố thú vị.",
    "Phố Moskovskaya (Улица Московская) là con phố trung tâm và giàu lịch sử bậc nhất của Penza, phần lớn đã được cải tạo thành khu đi bộ - nơi được ví như 'Arbat của Penza'. Đây từng là tuyến phố thương mại chính từ thế kỷ 18-19, hai bên là những toà nhà cổ mang phong cách chiết trung, tân cổ điển và hiện đại (modern) được bảo tồn. Dạo bộ dọc con phố lát đá, du khách sẽ bắt gặp các cửa hiệu, nhà hàng, quán cà phê, ngân hàng lịch sử, cùng nhiều điểm nhấn thú vị: đài phun nước (Фонтанная площадь), đồng hồ thành phố, các tác phẩm điêu khắc đường phố và những góc chụp ảnh đẹp. Về chiều tối, phố Moskovskaya càng nhộn nhịp với người dân dạo chơi, nghệ sĩ đường phố biểu diễn. Con phố kết nối nhiều điểm tham quan quan trọng của trung tâm - từ quảng trường, nhà thờ đến các bảo tàng - nên là nơi lý tưởng để bắt đầu và cảm nhận nhịp sống của thành phố Penza.",
    [
        "Phố đi bộ trung tâm giàu lịch sử - được ví như 'Arbat của Penza'",
        "Kiến trúc chiết trung, tân cổ điển và modern hai bên phố lát đá",
        "Đài phun nước, đồng hồ thành phố, điêu khắc đường phố và không khí nhộn nhịp buổi tối",
    ],
    p("Không gian công cộng ngoài trời, dạo chơi tự do mọi lúc; cửa hàng và quán theo giờ riêng.",
      "Miễn phí.",
      "Khoảng 45-90 phút tuỳ ý dạo và nghỉ quán.",
      "Chiều tối và buổi tối, đặc biệt mùa hè, khi phố đông vui nhất; mùa lễ hội càng rực rỡ.",
      "Kết hợp tham quan các bảo tàng và nhà thờ ở trung tâm dọc theo phố; thử quán cà phê địa phương."),
    [
        {"title": "Wikipedia (RU) — Московская улица (Пенза)", "url": "https://ru.wikipedia.org/wiki/Московская_улица_(Пенза)"},
        {"title": "Autotravel.ru — Улица Московская, Пенза", "url": "https://autotravel.ru/otklik.php/37744"},
    ],
    ["square_street", "pedestrian", "cityscape", "historic", "penza"],
    maps_text("Улица Московская", "Пенза", "Moskovskaya Street", "Penza", 53.190690, 45.015650),
))

# 15) Фонтанная площадь -------------------------------------------------------------
RECORDS.append(rec(
    "fountain-square-penza",
    "Quảng trường Đài phun nước (Fontannaya)",
    "Фонтанная площадь",
    "Fountain Square",
    ["square_street"],
    53.191130, 45.017180,
    "Trên phố đi bộ Moskovskaya, trung tâm thành phố Penza, tỉnh Penza, Nga",
    "Quảng trường có đài phun nước sôi động ngay trên phố đi bộ Moskovskaya - điểm hẹn được yêu thích của người dân Penza. Về đêm, đài phun nước sáng đèn và có nhạc nước, tạo không gian giải trí sống động.",
    "Quảng trường Đài phun nước (Фонтанная площадь) là một trong những không gian công cộng được yêu thích nhất ở trung tâm Penza, nằm ngay trên tuyến phố đi bộ Moskovskaya. Điểm nhấn của quảng trường là đài phun nước lớn - vào mùa ấm, các vòi nước phun theo nhịp, buổi tối được chiếu đèn màu và đôi khi kết hợp nhạc nước, thu hút đông đảo người dân và du khách đến hóng mát, chụp ảnh, hẹn hò. Xung quanh là những toà nhà lịch sử, hàng cây, ghế đá và các quán cà phê, khiến nơi đây trở thành 'phòng khách ngoài trời' của thành phố. Trẻ em thích thú nô đùa quanh đài phun nước, còn người lớn thư giãn trên các băng ghế. Đây là điểm dừng chân dễ chịu trong hành trình dạo bộ trung tâm Penza, đặc biệt vào những buổi chiều hè.",
    [
        "Đài phun nước sôi động ngay trên phố đi bộ Moskovskaya - điểm hẹn quen thuộc của người Penza",
        "Nhạc nước và ánh đèn màu về đêm tạo không gian giải trí sống động",
        "'Phòng khách ngoài trời' với ghế đá, hàng cây và quán cà phê bao quanh",
    ],
    p("Không gian công cộng ngoài trời, tự do mọi lúc; đài phun nước hoạt động chủ yếu mùa ấm.",
      "Miễn phí.",
      "Khoảng 15-30 phút.",
      "Buổi tối mùa hè khi đài phun nước sáng đèn và có nhạc nước.",
      "Đến vào buổi tối để xem đài phun nước sáng đèn; kết hợp dạo phố Moskovskaya và ăn tối gần đó."),
    [
        {"title": "Wikipedia (RU) — Московская улица (Пенза)", "url": "https://ru.wikipedia.org/wiki/Московская_улица_(Пенза)"},
        {"title": "Autotravel.ru — Фонтанная площадь, Пенза", "url": "https://autotravel.ru/otklik.php/21309"},
    ],
    ["square_street", "fountain", "cityscape", "leisure", "penza"],
    maps_text("Фонтанная площадь", "Пенза", "Fountain Square", "Penza", 53.191130, 45.017180),
))

# ============================ TƯỢNG ĐÀI (monument) ============================

# 16) Монумент воинской и трудовой славы «Росток» -----------------------------------
RECORDS.append(rec(
    "monument-glory-rostok-penza",
    "Đài Vinh quang Chiến sĩ và Lao động «Rostok» (Mầm cây)",
    "Монумент воинской и трудовой славы «Росток»",
    "Monument of Military and Labour Glory 'Rostok'",
    ["monument"],
    53.195000, 45.025270,
    "Bờ sông Sura (khu vực đường ven sông), thành phố Penza, tỉnh Penza, Nga",
    "Đài tưởng niệm cao vút bên sông Sura, biểu tượng cách tân của Penza thời Xô Viết. Khối bê tông trắng vươn lên như một mầm cây được người dân trìu mến gọi là 'Rostok' (Mầm cây) hay 'cái đục'.",
    "Đài Vinh quang Chiến sĩ và Lao động (Монумент воинской и трудовой славы), quen thuộc với người dân dưới tên 'Rostok' ( Росток - mầm cây), là một trong những biểu tượng hiện đại dễ nhận biết nhất của Penza. Khánh thành năm 1975 nhân kỷ niệm 30 năm Chiến thắng trong Chiến tranh Vệ quốc Vĩ đại, đài đài tưởng niệm này gồm một cột bê tông trắng cao vút, dáng vươn lên và hơi cong tựa một mầm cây đang nhú - cũng vì hình dáng độc đáo mà dân địa phương hài hước gọi là 'cái đục' (стамеска). Công trình tôn vinh những người con Penza đã chiến đấu ngoài mặt trận và lao động ở hậu phương. Đài nằm ở khu vực ven sông Sura, xung quanh có không gian mở, là nơi diễn ra các nghi lễ tưởng niệm và cũng là điểm dạo chơi, chụp ảnh. Dáng vẻ táo bạo của kiến trúc điêu khắc thời Xô Viết khiến 'Rostok' trở thành một điểm mốc thị giác đặc trưng của thành phố.",
    [
        "Biểu tượng hiện đại của Penza - cột bê tông trắng cao vút hình 'mầm cây' (Rostok)",
        "Khánh thành 1975 tôn vinh chiến sĩ và người lao động thời Chiến tranh Vệ quốc",
        "Kiến trúc điêu khắc Xô Viết táo bạo, điểm mốc thị giác bên sông Sura",
    ],
    p("Ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15-20 phút.",
      "Ban ngày để chụp ảnh; các dịp 9/5 (Ngày Chiến thắng) có nghi lễ trang trọng.",
      "Kết hợp dạo khu ven sông Sura; đây là điểm định hướng dễ thấy trong thành phố."),
    [
        {"title": "Wikipedia (RU) — Монумент воинской и трудовой славы (Пенза)", "url": "https://ru.wikipedia.org/wiki/Монумент_воинской_и_трудовой_славы_(Пенза)"},
        {"title": "Autotravel.ru — Монумент «Росток»", "url": "https://autotravel.ru/otklik.php/21317"},
    ],
    ["monument", "soviet", "memorial", "cityscape", "penza"],
    maps_text("Монумент воинской и трудовой славы Росток", "Пенза", "Monument of Military and Labour Glory Rostok", "Penza", 53.195000, 45.025270),
))

# ============================ CÔNG VIÊN (park_garden) ============================

# 17) ЦПКиО имени В.Г. Белинского ---------------------------------------------------
RECORDS.append(rec(
    "belinsky-central-park-penza",
    "Công viên Trung tâm mang tên V.G. Belinsky",
    "ЦПКиО имени В.Г. Белинского",
    "Belinsky Central Park",
    ["park_garden"],
    53.185030, 44.998820,
    "Phố Karla Marksa 1, trên đồi Boevaya gora, thành phố Penza, tỉnh Penza, Nga",
    "Một trong những công viên lâu đời nhất nước Nga (có gốc từ năm 1821), nằm trên ngọn đồi rợp bóng cây ở Penza. Kết hợp rừng cây cổ thụ, khu vui chơi, đài quan sát và các trò giải trí - lá phổi xanh yêu thích của thành phố.",
    "Công viên Trung tâm Văn hoá và Nghỉ ngơi mang tên V.G. Belinsky (ЦПКиО им. В.Г. Белинского) là một trong những công viên lâu đời nhất ở Nga: khu vườn dạo đầu tiên trên đồi này (Boevaya gora) đã hình thành từ năm 1821. Trải rộng trên một ngọn đồi rợp bóng cây cổ thụ ở trung tâm Penza, công viên là điểm nghỉ ngơi, vui chơi được người dân mọi lứa tuổi yêu thích. Bên trong có khu trò chơi giải trí (đu quay, vòng đu, các trò cho trẻ em), sân khấu ngoài trời, những lối đi dạo dài dưới tán rừng, và đặc biệt là điểm quan sát nhìn ra thành phố. Công viên cũng gắn với tên tuổi nhà phê bình văn học lừng danh Vissarion Belinsky - người đã sống thời niên thiếu ở Penza. Vào mùa hè, đây là nơi lý tưởng để tránh nóng, đi dạo, cho trẻ vui chơi; mùa đông cũng có các hoạt động riêng. Sự kết hợp giữa thiên nhiên lâu đời, không khí trong lành và các tiện ích giải trí khiến Belinsky là 'lá phổi xanh' và điểm hẹn quen thuộc của Penza.",
    [
        "Một trong những công viên lâu đời nhất nước Nga (gốc từ năm 1821)",
        "Rừng cây cổ thụ trên đồi cùng khu trò chơi giải trí và điểm quan sát thành phố",
        "Gắn với tên nhà phê bình văn học Vissarion Belinsky - lá phổi xanh của Penza",
    ],
    p("Công viên mở cửa hằng ngày; các trò chơi giải trí hoạt động chủ yếu mùa ấm và cuối tuần.",
      "Vào cửa công viên miễn phí; các trò chơi tính phí riêng.",
      "Khoảng 1-2 giờ.",
      "Mùa hè để tránh nóng và chơi các trò giải trí; mùa thu lá vàng rất đẹp.",
      "Thích hợp đi cùng gia đình và trẻ em; kết hợp thăm sở thú và vườn bách thảo gần đó."),
    [
        {"title": "Wikipedia (RU) — ЦПКиО имени В.Г. Белинского", "url": "https://ru.wikipedia.org/wiki/Центральный_парк_культуры_и_отдыха_имени_В._Г._Белинского_(Пенза)"},
        {"title": "Autotravel.ru — Парк им. Белинского", "url": "https://autotravel.ru/otklik.php/3011"},
    ],
    ["park_garden", "nature", "leisure", "family", "penza"],
    maps_org("https://yandex.com/maps/org/belinsky_central_park_of_culture_and_leisure/1078449529/", "Belinsky Central Park", "Penza"),
))

# 18) Пензенский зоопарк ------------------------------------------------------------
RECORDS.append(rec(
    "penza-zoo",
    "Vườn thú Penza",
    "Пензенский зоопарк",
    "Penza Zoo",
    ["park_garden"],
    53.175702, 45.002948,
    "Phố Krasnaya 10, thành phố Penza, tỉnh Penza, Nga",
    "Vườn thú của thành phố Penza, nằm trong khu công viên xanh mát ngay gần trung tâm. Nơi quy tụ hàng trăm loài động vật, điểm đến quen thuộc và yêu thích cho các gia đình và trẻ em.",
    "Vườn thú Penza (Пензенский зоопарк) là một trong những điểm đến gia đình được yêu thích nhất thành phố. Được thành lập từ năm 1981 trên nền một khu vườn - công viên cũ (từng thuộc quần thể nhà thờ), vườn thú nằm trong không gian xanh mát, có địa hình lên xuống và hồ nước tự nhiên, ngay gần trung tâm Penza. Nơi đây nuôi dưỡng hàng trăm loài động vật từ khắp nơi trên thế giới: thú lớn như gấu, sư tử, hổ, đại bàng và các loài chim, bò sát, cùng nhiều loài thú nhỏ và gia súc trong khu tiếp xúc dành cho trẻ em. Các lối đi dạo dưới bóng cây, khu tiểu cảnh và không khí trong lành khiến vườn thú vừa là nơi giáo dục về thiên nhiên, vừa là điểm dạo chơi thư giãn. Đặc biệt hấp dẫn với trẻ nhỏ, vườn thú Penza là lựa chọn lý tưởng cho một buổi tham quan nhẹ nhàng, kết hợp cùng công viên Belinsky và vườn bách thảo lân cận.",
    [
        "Vườn thú trong khu công viên xanh mát, hồ nước tự nhiên, ngay gần trung tâm Penza",
        "Hàng trăm loài động vật cùng khu tiếp xúc dành cho trẻ em",
        "Điểm đến gia đình lý tưởng, dễ kết hợp với công viên Belinsky gần đó",
    ],
    p("Mở cửa hằng ngày; giờ mở dài hơn vào mùa hè, ngắn hơn vào mùa đông.",
      "Vé vào cửa mức phổ thông, giá phải chăng; có ưu đãi cho trẻ em.",
      "Khoảng 1,5-2 giờ.",
      "Mùa xuân đến mùa thu khi thời tiết dễ chịu và động vật hoạt động nhiều.",
      "Đi cùng trẻ em nên dành cả buổi; mang nước và mũ mùa hè; kết hợp công viên Belinsky và vườn bách thảo."),
    [
        {"title": "Wikipedia (RU) — Пензенский зоопарк", "url": "https://ru.wikipedia.org/wiki/Пензенский_зоопарк"},
        {"title": "Yandex Maps — Пензенский зоопарк", "url": "https://yandex.com/maps/org/penzensky_zoopark/1105594629/"},
    ],
    ["park_garden", "zoo", "family", "nature", "penza"],
    maps_org("https://yandex.com/maps/org/penzensky_zoopark/1105594629/", "Penza Zoo", "Penza"),
))

# 19) Ботанический сад имени И.И. Спрыгина -------------------------------------------
RECORDS.append(rec(
    "botanical-garden-sprygin-penza",
    "Vườn Bách thảo mang tên I.I. Sprygin",
    "Ботанический сад имени И.И. Спрыгина",
    "Sprygin Botanical Garden",
    ["park_garden"],
    53.187548, 45.004491,
    "Phố Karla Marksa 2A, thành phố Penza, tỉnh Penza, Nga",
    "Vườn bách thảo lâu đời của Penza (thành lập 1917), một góc xanh yên tĩnh với bộ sưu tập cây cối phong phú, nhà kính nhiệt đới và các khu vườn theo chủ đề. Điểm đến thư giãn và giáo dục về thực vật ngay trong thành phố.",
    "Vườn Bách thảo mang tên I.I. Sprygin (Ботанический сад им. И.И. Спрыгина) là một trong những vườn bách thảo lâu đời ở vùng Volga, được thành lập năm 1917 và mang tên nhà thực vật học Ivan Sprygin - người có công lớn trong nghiên cứu và bảo tồn thiên nhiên vùng Penza. Nằm trong khu trung tâm, cạnh công viên Belinsky, vườn là một ốc đảo xanh yên tĩnh với hàng nghìn loài cây cỏ được sưu tầm từ nhiều vùng khí hậu. Du khách có thể dạo qua các khu vườn theo chủ đề (cây bản địa, cây thảo dược, cây cảnh), chiêm ngưỡng những cây cổ thụ và ghé nhà kính nơi trồng các loài cây nhiệt đới và cận nhiệt không thể sống ngoài trời ở khí hậu Nga. Đây là địa chỉ quen thuộc cho các buổi tham quan học tập của học sinh, đồng thời là nơi thư giãn nhẹ nhàng cho ai muốn tìm chút tĩnh lặng và không gian xanh giữa thành phố.",
    [
        "Vườn bách thảo lâu đời (1917) mang tên nhà thực vật học Ivan Sprygin",
        "Bộ sưu tập cây phong phú theo chủ đề cùng nhà kính cây nhiệt đới",
        "Ốc đảo xanh yên tĩnh ngay trung tâm, cạnh công viên Belinsky",
    ],
    p("Thường mở cửa ban ngày; nhà kính có thể có giờ riêng - nên kiểm tra trước.",
      "Vé vào cửa mức nhỏ, phải chăng.",
      "Khoảng 45-60 phút.",
      "Mùa xuân đến mùa thu khi cây cối tươi tốt; nhà kính thú vị cả mùa đông.",
      "Kết hợp cùng công viên Belinsky và vườn thú ở ngay gần; thích hợp cho gia đình và người yêu thực vật."),
    [
        {"title": "Wikipedia (RU) — Ботанический сад имени И. И. Спрыгина", "url": "https://ru.wikipedia.org/wiki/Ботанический_сад_имени_И._И._Спрыгина"},
        {"title": "Yandex Maps — Ботанический сад им. И.И. Спрыгина", "url": "https://yandex.com/maps/org/botanichesky_sad_imeni_i_i_sprygina/1017565764/"},
    ],
    ["park_garden", "botanical", "nature", "education", "penza"],
    maps_org("https://yandex.com/maps/org/botanichesky_sad_imeni_i_i_sprygina/1017565764/", "Sprygin Botanical Garden", "Penza"),
))

# ============================ NHÀ HÁT / GIẢI TRÍ (theatre) ============================

# 20) Пензенский драматический театр имени А.В. Луначарского ------------------------
RECORDS.append(rec(
    "lunacharsky-drama-theatre-penza",
    "Nhà hát Kịch Penza mang tên A.V. Lunacharsky",
    "Пензенский драматический театр имени А.В. Луначарского",
    "Penza Regional Drama Theatre",
    ["theatre"],
    53.198343, 45.019376,
    "Phố Moskovskaya 89, thành phố Penza, tỉnh Penza, Nga",
    "Nhà hát kịch chính của tỉnh Penza, một trong những đoàn kịch tỉnh lẻ lâu đời và uy tín của Nga (từ năm 1793). Toà nhà hiện đại khang trang nằm trên phố Moskovskaya, dàn dựng cả kịch cổ điển lẫn đương đại.",
    "Nhà hát Kịch Penza mang tên A.V. Lunacharsky (Пензенский драматический театр им. А.В. Луначарского) là sân khấu kịch nói hàng đầu của tỉnh, với lịch sử được tính từ năm 1793 - thuộc hàng nhà hát tỉnh lẻ lâu đời nhất nước Nga. Trải qua hơn hai thế kỷ, nhà hát đã gắn bó với đời sống văn hoá của thành phố qua nhiều thế hệ nghệ sĩ. Toà nhà hát cũ bị hoả hoạn thiêu rụi năm 2008, và một toà nhà hát mới hiện đại, khang trang đã được xây dựng ngay tại vị trí trung tâm trên phố Moskovskaya, khánh thành năm 2010 với khán phòng tiện nghi và trang thiết bị sân khấu tiên tiến. Tiết mục của nhà hát đa dạng, từ các vở kinh điển Nga và thế giới (Chekhov, Ostrovsky, Gogol...) đến những dàn dựng đương đại, hài kịch và kịch thiếu nhi. Xem một buổi diễn ở đây là cách tuyệt vời để cảm nhận đời sống sân khấu sôi động của tỉnh lẻ Nga và thư giãn một buổi tối ở Penza.",
    [
        "Một trong những nhà hát kịch tỉnh lâu đời nhất nước Nga (từ 1793)",
        "Toà nhà hát hiện đại khang trang trên phố Moskovskaya (xây lại sau hoả hoạn 2008)",
        "Tiết mục đa dạng từ kịch cổ điển Nga - thế giới đến kịch đương đại và thiếu nhi",
    ],
    p("Các buổi diễn chủ yếu vào buổi tối và cuối tuần; phòng vé mở ban ngày.",
      "Vé xem kịch tuỳ vở và vị trí ghế, giá phải chăng; nên đặt trước.",
      "Một buổi diễn khoảng 2-3 giờ.",
      "Mùa diễn thường từ mùa thu đến mùa xuân; kiểm tra lịch trước khi đến.",
      "Xem lịch và đặt vé trên trang chính thức; nhiều vở diễn bằng tiếng Nga nên tìm hiểu nội dung trước."),
    [
        {"title": "Wikipedia (RU) — Пензенский драматический театр", "url": "https://ru.wikipedia.org/wiki/Пензенский_драматический_театр_имени_А._В._Луначарского"},
        {"title": "Yandex Maps — Драмтеатр им. Луначарского", "url": "https://yandex.com/maps/org/penza_regional_drama_theater_named_after_a_v_lunacharsky/1167200618/"},
    ],
    ["theatre", "drama", "culture", "penza"],
    maps_org("https://yandex.com/maps/org/penza_regional_drama_theater_named_after_a_v_lunacharsky/1167200618/", "Penza Regional Drama Theatre", "Penza"),
))

# 21) Пензенский государственный цирк -----------------------------------------------
RECORDS.append(rec(
    "penza-circus",
    "Rạp xiếc Nhà nước Penza",
    "Пензенский государственный цирк",
    "Penza State Circus",
    ["theatre"],
    53.198095, 45.011848,
    "Phố Plekhanova 13, thành phố Penza, tỉnh Penza, Nga",
    "Rạp xiếc của thành phố Penza, gắn với truyền thống xiếc Nga và ký ức của nhiều thế hệ. Nơi từng mang đến những chương trình xiếc sôi động cho các gia đình; công trình đang trong quá trình cải tạo, tái thiết.",
    "Rạp xiếc Nhà nước Penza (Пензенский государственный цирк) là một phần trong ký ức văn hoá - giải trí của nhiều thế hệ người dân thành phố. Nằm ở khu trung tâm trên phố Plekhanova, rạp xiếc trong nhiều thập niên đã là nơi diễn ra các chương trình xiếc lưu động và cố định - với những màn nhào lộn, thú biểu diễn, ảo thuật và hề - mang lại niềm vui cho trẻ em và các gia đình. Rạp xiếc Penza cũng gắn với truyền thống xiếc lâu đời và đẳng cấp của nước Nga, nơi từng đón các đoàn xiếc danh tiếng lưu diễn. Những năm gần đây, toà nhà rạp xiếc cũ đã xuống cấp và bước vào giai đoạn cải tạo, tái thiết để có một không gian biểu diễn hiện đại hơn. Với du khách quan tâm nghệ thuật xiếc và đi cùng trẻ em, nên kiểm tra tình trạng hoạt động và lịch biểu diễn hiện thời trước khi ghé.",
    [
        "Rạp xiếc gắn với truyền thống xiếc Nga và ký ức của nhiều thế hệ người Penza",
        "Vị trí trung tâm trên phố Plekhanova, từng đón nhiều đoàn xiếc danh tiếng lưu diễn",
        "Đang trong giai đoạn cải tạo, tái thiết - nên kiểm tra lịch trước khi đến",
    ],
    p("Theo lịch biểu diễn; công trình đang cải tạo nên cần kiểm tra tình trạng hoạt động trước.",
      "Vé tuỳ chương trình; thường có ưu đãi cho trẻ em.",
      "Một suất diễn khoảng 2 giờ.",
      "Kiểm tra lịch và tình trạng hoạt động hiện thời trước khi lên kế hoạch.",
      "Vì đang tái thiết, nên xác nhận qua kênh chính thức; nếu tạm đóng, cân nhắc các điểm giải trí khác trong trung tâm."),
    [
        {"title": "Wikipedia (RU) — Пензенский цирк", "url": "https://ru.wikipedia.org/wiki/Пензенский_цирк"},
        {"title": "Yandex Maps — Пензенский цирк", "url": "https://yandex.com/maps/org/tsirk/1118957942/"},
    ],
    ["theatre", "circus", "entertainment", "family", "penza"],
    maps_org("https://yandex.com/maps/org/tsirk/1118957942/", "Penza State Circus", "Penza"),
))

# 22) Пензенская областная филармония -----------------------------------------------
RECORDS.append(rec(
    "penza-philharmonic",
    "Nhà hát Giao hưởng Tỉnh Penza (Filarmonia)",
    "Пензенская областная филармония",
    "Penza Regional Philharmonic",
    ["theatre"],
    53.202632, 44.986919,
    "Phố Suvorova 215, thành phố Penza, tỉnh Penza, Nga",
    "Trung tâm âm nhạc hàn lâm của tỉnh Penza, với phòng hoà nhạc hiện đại trang bị đại phong cầm (organ). Nơi tổ chức các buổi hoà nhạc giao hưởng, thính phòng, organ và nhiều chương trình nghệ thuật đa dạng.",
    "Nhà hát Giao hưởng Tỉnh Penza (Пензенская областная филармония) là trung tâm của đời sống âm nhạc hàn lâm trong vùng. Tổ hợp phòng hoà nhạc hiện đại được khánh thành năm 2012 nằm trong quần thể văn hoá cạnh Quảng trường Chiến thắng, gồm một đại sảnh hoà nhạc lớn và các phòng nhỏ hơn. Điểm nhấn đặc biệt là cây đại phong cầm (organ) - một trong số ít nhạc cụ organ hoà nhạc ở vùng, mang đến những buổi diễn organ trang trọng và cuốn hút. Chương trình của filarmonia rất phong phú: hoà nhạc giao hưởng, nhạc thính phòng, nhạc organ, nhạc jazz, các buổi diễn cho thiếu nhi và những đêm nhạc tôn vinh tác phẩm kinh điển Nga và thế giới. Với âm học tốt và không gian sang trọng, đây là điểm đến lý tưởng cho những ai muốn thưởng thức âm nhạc chất lượng cao trong một buổi tối ở Penza, đồng thời cảm nhận đời sống văn hoá tinh tế của thành phố.",
    [
        "Phòng hoà nhạc hiện đại (2012) - trung tâm âm nhạc hàn lâm của tỉnh",
        "Đại phong cầm (organ) hoà nhạc hiếm có trong vùng",
        "Chương trình đa dạng: giao hưởng, thính phòng, organ, jazz và nhạc thiếu nhi",
    ],
    p("Các buổi hoà nhạc chủ yếu vào buổi tối và cuối tuần; phòng vé mở ban ngày.",
      "Vé tuỳ chương trình và vị trí ghế, giá phải chăng.",
      "Một buổi hoà nhạc khoảng 1,5-2 giờ.",
      "Mùa diễn từ mùa thu đến mùa xuân; kiểm tra lịch trước.",
      "Xem lịch và đặt vé trên trang chính thức; các buổi diễn organ đặc biệt được ưa chuộng."),
    [
        {"title": "Wikipedia (RU) — Пензенская областная филармония", "url": "https://ru.wikipedia.org/wiki/Пензенская_областная_филармония"},
        {"title": "Yandex Maps — Пензенская филармония", "url": "https://yandex.com/maps/org/penza_regional_philharmonic/1087286806/"},
    ],
    ["theatre", "philharmonic", "music", "organ", "penza"],
    maps_org("https://yandex.com/maps/org/penza_regional_philharmonic/1087286806/", "Penza Regional Philharmonic", "Penza"),
))

# ============================ CẦU (bridge) ============================

# 23) Подвесной мост через Суру («Мост Дружбы») -------------------------------------
RECORDS.append(rec(
    "suspension-bridge-sura-penza",
    "Cầu treo qua sông Sura (Cầu Hữu nghị)",
    "Подвесной мост через Суру",
    "Suspension Bridge over the Sura",
    ["bridge"],
    53.183343, 45.016263,
    "Bắc qua sông Sura, khu ven sông trung tâm thành phố Penza, tỉnh Penza, Nga",
    "Cầu treo dành cho người đi bộ bắc qua sông Sura ở trung tâm Penza, quen gọi là 'Cầu Hữu nghị'. Điểm dạo chơi, ngắm sông và chụp ảnh được yêu thích, đặc biệt khi lên đèn buổi tối.",
    "Cầu treo qua sông Sura (Подвесной мост), thường được người dân gọi là 'Cầu Hữu nghị' (Мост Дружбы), là một cây cầu dành cho người đi bộ bắc ngang dòng Sura ở khu trung tâm Penza. Với kết cấu dây văng - dây treo đặc trưng, cầu hơi đung đưa nhẹ khi có nhiều người qua lại, tạo cảm giác thú vị và cũng vì thế mà trở thành điểm 'check-in' quen thuộc. Từ trên cầu, du khách có thể phóng tầm mắt ra mặt sông Sura và khu bờ sông (naberezhnaya) đã được chỉnh trang thành nơi dạo bộ. Buổi tối, cầu và khu ven sông lên đèn, phản chiếu xuống mặt nước, là bối cảnh lãng mạn cho những buổi đi dạo. Cây cầu nối khu trung tâm với các không gian nghỉ ngơi ven sông, thuận tiện kết hợp trong hành trình khám phá trung tâm thành phố. Đây là một điểm đến nhẹ nhàng, miễn phí và đậm nhịp sống đô thị của Penza.",
    [
        "Cầu treo đi bộ bắc qua sông Sura ở trung tâm - quen gọi 'Cầu Hữu nghị'",
        "Điểm dạo chơi, ngắm sông và chụp ảnh yêu thích, đung đưa nhẹ khi qua lại",
        "Lên đèn buổi tối cùng khu bờ sông, tạo khung cảnh lãng mạn",
    ],
    p("Không gian công cộng ngoài trời, qua lại tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15-30 phút.",
      "Chiều tối và buổi tối mùa ấm, khi cầu và bờ sông lên đèn.",
      "Kết hợp dạo khu ven sông Sura; chú ý cầu có thể rung nhẹ khi đông người."),
    [
        {"title": "Wikipedia (RU) — Пенза (река Сура, набережная)", "url": "https://ru.wikipedia.org/wiki/Пенза"},
        {"title": "Vatravel.ru — Мост Дружбы, Пенза", "url": "https://vatravel.ru/most-druzhby/"},
    ],
    ["bridge", "suspension", "river", "cityscape", "penza"],
    maps_text("Подвесной мост через Суру Мост Дружбы", "Пенза", "Suspension Bridge over the Sura", "Penza", 53.183343, 45.016263),
))

# ============================ THIÊN NHIÊN / KHÁC (other) ============================

# 24) Заповедник «Приволжская лесостепь» (участок «Попереченская степь») ------------
RECORDS.append(rec(
    "privolzhskaya-lesostep-reserve",
    "Khu Bảo tồn Thiên nhiên «Rừng-Thảo nguyên Volga» (thảo nguyên Poperechenskaya)",
    "Заповедник «Приволжская лесостепь»",
    "Privolzhskaya Lesostep Nature Reserve",
    ["other"],
    52.975000, 44.333000,
    "Khu (uchastok) 'Popperechenskaya step', vùng giáp huyện Penzensky - Kamensky, tỉnh Penza, Nga",
    "Khu bảo tồn thiên nhiên quốc gia bảo vệ những mảnh thảo nguyên (steppe) nguyên sinh hiếm hoi còn sót lại của vùng Volga. Điểm nhấn là thảo nguyên đồng cỏ Poperechenskaya - hệ sinh thái cỏ hoa quý được nghiên cứu và gìn giữ hơn một thế kỷ.",
    "Khu Bảo tồn Thiên nhiên Quốc gia 'Rừng-Thảo nguyên Volga' (Заповедник «Приволжская лесостепь») là một zapovednik gồm nhiều khu (uchastok) tách biệt, được lập nhằm bảo vệ các mảnh hệ sinh thái rừng-thảo nguyên đặc trưng của vùng cao Volga - vốn gần như đã biến mất do canh tác nông nghiệp. Nổi tiếng nhất là khu 'Thảo nguyên Poperechenskaya' (Попереченская степь), một trong những thảo nguyên đồng cỏ nguyên sinh được bảo vệ sớm nhất ở Nga (từ đầu thế kỷ 20), nơi gìn giữ thảm cỏ hoa đa dạng với hàng trăm loài thực vật, trong đó có những loài quý hiếm trong Sách Đỏ. Vào cuối xuân - đầu hè, thảo nguyên bừng nở muôn sắc hoa, là cảnh tượng tuyệt đẹp và hiếm thấy. Các khu khác của khu bảo tồn còn bảo vệ rừng sồi cổ và những đoạn thảo nguyên khác. Việc tham quan cần tuân thủ quy định nghiêm ngặt của zapovednik (thường phải xin phép và đi cùng hướng dẫn/theo tuyến sinh thái quy định) - đây là điểm đến dành cho người yêu thiên nhiên, muốn tìm hiểu hệ sinh thái thảo nguyên độc đáo của nước Nga.",
    [
        "Bảo vệ những mảnh thảo nguyên nguyên sinh hiếm hoi còn sót lại của vùng cao Volga",
        "Thảo nguyên Poperechenskaya - một trong những đồng cỏ được bảo vệ sớm nhất ở Nga, giàu loài thực vật quý",
        "Cuối xuân - đầu hè thảo nguyên bừng nở muôn sắc hoa, cảnh tượng độc đáo",
    ],
    p("Là khu bảo tồn nghiêm ngặt (zapovednik) - tham quan phải xin phép trước và theo tuyến/hướng dẫn quy định.",
      "Cần liên hệ ban quản lý về thủ tục; có thể thu phí tuyến sinh thái.",
      "Nửa ngày (gồm di chuyển và đi tuyến).",
      "Cuối tháng 5 đến tháng 6, khi thảo nguyên nở hoa rực rỡ nhất.",
      "Liên hệ ban quản lý khu bảo tồn ở Penza trước; tuân thủ nghiêm quy định bảo tồn, không tự ý vào vùng lõi; mang nước, mũ, giày đi bộ."),
    [
        {"title": "Wikipedia (RU) — Приволжская лесостепь", "url": "https://ru.wikipedia.org/wiki/Приволжская_лесостепь"},
        {"title": "Zapovednik zpls.ru — Попереченская степь", "url": "https://zpls.ru/o-zapovednike/territoriya/poperechenskaya-step.html"},
    ],
    ["other", "nature-reserve", "steppe", "zapovednik", "ecotourism", "penza"],
    maps_text("Заповедник Приволжская лесостепь Попереченская степь", "Пензенская область", "Privolzhskaya Lesostep Nature Reserve", "Penza Oblast", 52.975000, 44.333000),
))

# 25) Город Кузнецк -----------------------------------------------------------------
RECORDS.append(rec(
    "kuznetsk-town",
    "Thành phố Kuznetsk",
    "Город Кузнецк",
    "Kuznetsk Town",
    ["other"],
    53.116700, 46.600000,
    "Thành phố Kuznetsk, phía đông tỉnh Penza, tỉnh Penza, Nga",
    "Thành phố lớn thứ hai của tỉnh Penza, một trung tâm công nghiệp - thương mại lâu đời ở phía đông, nổi tiếng với truyền thống thủ công (đóng giày, dệt). Điểm dừng thú vị với nhà thờ, bảo tàng và không khí đô thị tỉnh lẻ Nga.",
    "Kuznetsk (Кузнецк) là thành phố lớn thứ hai của tỉnh Penza, nằm ở phía đông, trên tuyến giao thông nối Penza với vùng Ulyanovsk - Samara. Hình thành từ làng Truyovo thế kỷ 17 và trở thành thành phố (mang tên Kuznetsk, nghĩa là 'thành phố thợ rèn') từ cuối thế kỷ 18, đô thị này gắn với truyền thống thủ công phát đạt - đặc biệt nghề đóng giày, thuộc da và các nghề rèn, mộc. Trung tâm Kuznetsk còn lưu giữ những dãy phố buôn bán, nhà thờ và công trình từ thời tiền cách mạng, phản ánh diện mạo một thành phố thương nghiệp tỉnh lẻ điển hình. Du khách có thể ghé nhà thờ chính, bảo tàng lịch sử địa phương, dạo các quảng trường và tìm hiểu đời sống của một đô thị công nghiệp - thủ công vùng Volga. Kuznetsk cũng là cửa ngõ thuận tiện để khám phá phần phía đông của tỉnh, trong đó có điền trang - bảo tàng Radishchev ở Verkhnee Ablyazovo gần đó.",
    [
        "Thành phố lớn thứ hai của tỉnh Penza, trung tâm công nghiệp - thương mại phía đông",
        "Truyền thống thủ công lâu đời (đóng giày, thuộc da, nghề rèn) - tên gọi 'thành phố thợ rèn'",
        "Phố buôn bán, nhà thờ và công trình tiền cách mạng mang diện mạo đô thị tỉnh lẻ Nga",
    ],
    p("Là một thành phố - tham quan tự do; các bảo tàng, nhà thờ theo giờ riêng.",
      "Dạo phố miễn phí; bảo tàng có vé mức nhỏ.",
      "Khoảng nửa ngày.",
      "Mùa xuân đến mùa thu thuận tiện đi lại và dạo phố.",
      "Kuznetsk cách Penza khoảng 120 km về phía đông; dùng làm điểm dừng để thăm điền trang Radishchev gần đó."),
    [
        {"title": "Wikipedia (RU) — Кузнецк", "url": "https://ru.wikipedia.org/wiki/Кузнецк"},
        {"title": "Geodzen — Кузнецк", "url": "https://geodzen.com/ru/kuznetsk"},
    ],
    ["other", "town", "history", "craft", "kuznetsk", "penza"],
    maps_text("Город Кузнецк", "Пензенская область", "Kuznetsk", "Penza Oblast", 53.116700, 46.600000),
))


def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    existing_slugs = {q.get("slug") for q in data}
    existing_ids = {q.get("id") for q in data}

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
