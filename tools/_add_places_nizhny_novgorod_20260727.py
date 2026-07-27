# -*- coding: utf-8 -*-
"""_add_places_nizhny_novgorod_20260727.py — VÙNG TIÊU ĐIỂM: Tỉnh Nizhny Novgorod (lần chạy tự động 2026-07-27).

Bối cảnh: nizhny-novgorod.json hiện có 10 địa điểm (kremlin, cầu thang Chkalov, Diveyevo,
Makaryev, Gorodets, điền trang Boldino, hội chợ, Semyonov-Khokhloma, phố Bolshaya Pokrovskaya,
cáp treo). Tatarstan đã đạt 60 (≥50) => vùng tiêu điểm chuyển sang Nizhny Novgorod (đầu danh
sách ưu tiên còn <50).

Đợt này bổ sung 18 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình:
nhà thờ/tu viện (Строгановская церковь, собор Александра Невского, Печёрский монастырь,
Воскресенский собор Арзамаса), bảo tàng (Художественный музей, Домик Каширина, музей Чкалова,
Щёлоковский хутор, планетарий), điền trang quý tộc (Усадьба Рукавишниковых), nhà hát
(драмы им. Горького, оперы и балета им. Пушкина), công trình kiến trúc (Госбанк), phố cổ &
bờ sông (Рождественская улица, Верхне-Волжская набережная), không gian văn hoá hiện đại
(Пакгаузы на Стрелке), thắng cảnh thiên nhiên & truyền thuyết (озеро Светлояр), di tích kỹ
thuật (Шуховская башня на Оке).

TOẠ ĐỘ: xác minh chéo ru.wikipedia (mục Координаты), Wikidata, sobory.ru (nhà thờ/tu viện),
trang tổ chức Yandex Maps (yandex.../maps/org/.../<id>/) — 2026-07. Kiểm tra thứ tự & phạm vi
(NN: lat ~54,5–58,1; lon ~41,5–47,0; KHÔNG đảo lat/lon; đều nằm trong tỉnh). Link bản đồ
TRỎ-ĐỊA-ĐIỂM: ưu tiên URL trang tổ chức Yandex khi tra được; còn lại dùng text-search theo
tên_ru + thành phố, canh giữa theo toạ độ đã kiểm.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_nizhny_novgorod_20260727.py
       python3 tools/normalize_categories.py && python3 tools/build.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"

REGION = "nizhny-novgorod"
REGION_NAME_VI = "Tỉnh Nizhny Novgorod"
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
    """Ưu tiên URL trang tổ chức Yandex (chính xác nhất) + Google text-search."""
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
        "rating": None,
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

# 1) Nhà thờ Rождества (Строгановская) — kiệt tác Baroque nhà Stroganov -------
RECORDS.append(rec(
    "rozhdestvenskaya-stroganov-church",
    "Nhà thờ Giáng Sinh Đức Mẹ (nhà thờ Stroganov, Rozhdestvenskaya / Stroganovskaya tserkov)",
    "Рождественская (Строгановская) церковь",
    "Church of the Nativity of Our Lady (Stroganov Church)",
    ["church"],
    56.32722, 43.98500,
    "Phố Rozhdestvenskaya (Rождественская) số 34А, khu phố dưới ven sông Oka, thành phố Nizhny Novgorod, tỉnh Nizhny Novgorod, Nga.",
    "Nhà thờ Stroganov là một trong những kiệt tác đẹp nhất của phong cách 'Baroque nhà Stroganov' ở Nga. Công trình được nhà đại phú thương Grigory Stroganov cho xây dựng trong khoảng 1696–1719, nổi bật với những mảng chạm khắc đá trắng tinh xảo trên nền tường đỏ và năm vòm dát vàng.",
    "Sừng sững trên phố cổ Rozhdestvenskaya của khu phố dưới, Nhà thờ Giáng Sinh Đức Mẹ – quen gọi là nhà thờ Stroganov – được xây bằng kinh phí của gia tộc thương nhân – nhà công nghiệp muối Stroganov, khởi công năm 1696 và hoàn tất khoảng năm 1719. Đây được xem là mẫu mực tiêu biểu nhất của 'Baroque nhà Stroganov', một biến thể lộng lẫy của kiến trúc Nga cuối thế kỷ 17. Điều làm du khách sững sờ là những dải hoa văn chạm nổi bằng đá trắng: từng chùm nho, quả lựu, hoa lá cuốn quanh cửa sổ và cổng vào, tương phản rực rỡ với thân tường sơn đỏ và những vòm củ hành nhiều màu. Tháp chuông có chiếc đồng hồ cổ nhiều mặt độc đáo. Tương truyền chính Pyotr Đại đế từng ghé thăm và có giai thoại ông cho đóng cửa nhà thờ một thời gian. Trải qua thời Xô viết bị đóng cửa và dùng làm kho, công trình được trùng tu và trả lại cho Giáo hội, nay vừa là nơi hành lễ vừa là một trong những biểu tượng kiến trúc được yêu thích nhất của Nizhny Novgorod.",
    [
        "Kiệt tác 'Baroque nhà Stroganov' với hoa văn đá trắng chạm nổi cực kỳ tinh xảo trên nền tường đỏ.",
        "Do đại phú thương Grigory Stroganov xây dựng năm 1696–1719, di tích kiến trúc cấp liên bang.",
        "Tháp chuông gắn đồng hồ cổ độc đáo, nằm ngay trên phố cổ Rozhdestvenskaya sầm uất.",
    ],
    {
        "hours_vi": "Mở cửa cho khách tham quan và hành lễ hằng ngày, thường khoảng 8:00–19:00 theo lịch nhà thờ.",
        "ticket_vi": "Vào tham quan tự do (miễn phí); hoan nghênh quyên góp tuỳ tâm.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm; đẹp nhất khi nắng chiếu làm nổi bật hoa văn đá trắng và vòm mái nhiều màu.",
        "tips_vi": "Ăn mặc kín đáo khi vào; kết hợp dạo bộ dọc phố Rozhdestvenskaya và ra bờ sông Oka gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Рождественская церковь (Нижний Новгород)", "url": "https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D0%B6%D0%B4%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D1%86%D0%B5%D1%80%D0%BA%D0%BE%D0%B2%D1%8C_(%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4)"},
        {"title": "sobory.ru — Нижний Новгород, церковь Собора Пресвятой Богородицы (Рождественская)", "url": "https://sobory.ru/article/?object=01787"},
    ],
    ["church", "stroganov-baroque", "architecture", "17th-century", "rozhdestvenskaya"],
    maps_text("Рождественская Строгановская церковь", "Нижний Новгород",
              "Stroganov Church of the Nativity", "Nizhny Novgorod", 56.32722, 43.98500),
    official_site="https://stroganovskaya.ru",
))

# 2) Nhà thờ chính toà Aleksandr Nevsky (bên bãi Strelka) ---------------------
RECORDS.append(rec(
    "alexander-nevsky-cathedral-nn",
    "Nhà thờ chính toà Aleksandr Nevsky (Novoyarmarochny sobor)",
    "Кафедральный собор во имя святого благоверного князя Александра Невского",
    "Alexander Nevsky Cathedral (Novoyarmarochny)",
    ["church"],
    56.33360, 43.97118,
    "Mũi đất Strelka (Стрелка), nơi sông Oka đổ vào sông Volga, gần sân vận động Nizhny Novgorod, thành phố Nizhny Novgorod, Nga.",
    "Nhà thờ Aleksandr Nevsky vươn cao bên bãi Strelka – nơi hai dòng Oka và Volga gặp nhau – là một trong những nhà thờ Chính thống giáo cao nhất nước Nga (khoảng 87 m). Được giới thương nhân hội chợ Nizhny Novgorod góp tiền dựng năm 1868–1881, công trình có dáng vẻ uy nghi với thân tháp lều nhọn vút.",
    "Được xây dựng trong khoảng 1868–1881 bằng tiền quyên góp của các thương nhân đến buôn bán tại Hội chợ Nizhny Novgorod danh tiếng, Nhà thờ chính toà Aleksandr Nevsky (còn gọi là 'nhà thờ Tân hội chợ') là một trong những thánh đường Chính thống giáo cao nhất nước Nga, đỉnh tháp vươn tới khoảng 87 mét. Nhà thờ mọc lên ngay tại mũi đất Strelka – điểm hợp lưu ngoạn mục của sông Oka và sông Volga – nên từ xa đã thấy khối tháp lều (shatyor) nhọn vút in trên nền trời. Công trình từng suýt bị phá huỷ thời Xô viết: mái vòm bị dỡ, bên trong biến thành kho, thậm chí có kế hoạch cho nổ mìn. Từ thập niên 1980–1990 nhà thờ dần được phục dựng và trở lại là thánh đường trung tâm của giáo phận. Ngày nay công trình đứng cạnh sân vận động Nizhny Novgorod hiện đại và quần thể Пакгаузы trên Strelka, tạo nên một trong những cụm cảnh quan gây ấn tượng mạnh nhất thành phố, đặc biệt khi ngắm từ phía kremlin bên kia sông hay lúc lên đèn buổi tối.",
    [
        "Một trong những nhà thờ Chính thống giáo cao nhất nước Nga, đỉnh tháp khoảng 87 m.",
        "Do thương nhân Hội chợ Nizhny Novgorod góp tiền xây năm 1868–1881, dáng tháp lều nhọn đặc trưng.",
        "Toạ lạc trên bãi Strelka – hợp lưu Oka và Volga – cạnh sân vận động và quần thể Пакгаузы.",
    ],
    {
        "hours_vi": "Mở cửa hành lễ và tham quan hằng ngày, thường khoảng 7:00–19:00.",
        "ticket_vi": "Vào tự do (miễn phí); có thể quyên góp tuỳ tâm.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm; đẹp lúc hoàng hôn hoặc khi thắp đèn, ngắm cùng khung cảnh hợp lưu hai sông.",
        "tips_vi": "Kết hợp tham quan Пакгаузы trên Strelka và ngắm sân vận động; ăn mặc kín đáo khi vào nhà thờ.",
    },
    [
        {"title": "Wikipedia (RU) — Собор Александра Невского (Нижний Новгород)", "url": "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%B1%D0%BE%D1%80_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80%D0%B0_%D0%9D%D0%B5%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_(%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4)"},
        {"title": "sobory.ru — Нижний Новгород, собор Александра Невского Новоярмарочный", "url": "https://sobory.ru/article/?object=01788"},
    ],
    ["church", "cathedral", "strelka", "19th-century", "landmark"],
    maps_org("https://yandex.com/maps/org/alexander_nevsky_cathedral/1061156993/",
             "Alexander Nevsky Cathedral", "Nizhny Novgorod"),
))

# 3) Tu viện Thăng Thiên Pechyory (Vознесенский Печёрский) --------------------
RECORDS.append(rec(
    "pechersky-ascension-monastery",
    "Tu viện Thăng Thiên Pechyory (Voznesensky Pechyorsky monastyr)",
    "Вознесенский Печёрский монастырь",
    "Ascension Pechyorsky Monastery",
    ["church", "monument"],
    56.32357, 44.04705,
    "Slobodá Privolzhskaya (Приволжская слобода) số 108, ven bờ cao sông Volga phía đông trung tâm, thành phố Nizhny Novgorod, Nga.",
    "Tu viện Thăng Thiên Pechyory là một trong những tu viện cổ kính và đẹp nhất Nizhny Novgorod, nằm nép mình bên bờ cao sông Volga. Được Thánh Dionysius lập vào khoảng năm 1328–1330, quần thể trắng muốt hiện nay gồm nhà thờ chính, tháp chuông nghiêng và tường bao được dựng lại từ thế kỷ 17 sau khi công trình gốc bị lở đất phá huỷ.",
    "Nằm bên triền dốc thoải xuống sông Volga ở khu Pechyory phía đông thành phố, Tu viện Thăng Thiên Pechyorsky là một trong những trung tâm tôn giáo – lịch sử lâu đời nhất vùng. Tu viện do Thánh Dionysius xứ Suzdal khai lập vào khoảng năm 1328–1330 và từng là một trung tâm chép sách, tu học quan trọng thời trung cổ. Năm 1597, một trận lở đất lớn đã phá huỷ gần như toàn bộ quần thể gốc, buộc tu viện phải dời lên vị trí cao hơn ngày nay và được xây dựng lại trong thế kỷ 17. Quần thể hiện tại là một tổ hợp kiến trúc Nga thế kỷ 17 hài hoà: Nhà thờ Thăng Thiên năm mái vòm làm trung tâm, cùng các nhà thờ nhỏ, phòng ăn, tường thành và một tháp chuông nổi tiếng hơi nghiêng. Khung cảnh những mái vòm trắng – vàng trên nền sông Volga mênh mông khiến nơi đây trở thành một trong những góc chụp ảnh đẹp nhất Nizhny Novgorod. Tu viện đang hoạt động tôn giáo trở lại và có một bảo tàng nhỏ về lịch sử giáo phận.",
    [
        "Tu viện do Thánh Dionysius lập khoảng 1328–1330, một trong những nơi cổ kính nhất vùng.",
        "Quần thể kiến trúc Nga thế kỷ 17 với nhà thờ Thăng Thiên năm vòm và tháp chuông hơi nghiêng.",
        "Vị trí tuyệt đẹp bên bờ cao sông Volga, góc ngắm và chụp ảnh lý tưởng.",
    ],
    {
        "hours_vi": "Khuôn viên mở hằng ngày, thường khoảng 7:00–20:00; bảo tàng giáo phận mở theo giờ riêng.",
        "ticket_vi": "Vào khuôn viên miễn phí; bảo tàng có thể thu phí nhỏ.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; đẹp vào sáng sớm hoặc chiều muộn khi ánh sáng dịu.",
        "tips_vi": "Đi giày thoải mái vì địa hình dốc ven sông; ăn mặc kín đáo khi vào khu tu viện.",
    },
    [
        {"title": "Wikipedia (RU) — Вознесенский Печёрский монастырь", "url": "https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%B7%D0%BD%D0%B5%D1%81%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%9F%D0%B5%D1%87%D1%91%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%BE%D0%BD%D0%B0%D1%81%D1%82%D1%8B%D1%80%D1%8C"},
        {"title": "sobory.ru — Нижний Новгород, Вознесенский Печёрский монастырь", "url": "https://sobory.ru/article/?object=00896"},
    ],
    ["monastery", "orthodox", "14th-century", "volga", "architecture"],
    maps_text("Вознесенский Печёрский монастырь", "Нижний Новгород",
              "Ascension Pechersky Monastery", "Nizhny Novgorod", 56.32357, 44.04705),
))

# 4) Nhà thờ chính toà Phục Sinh ở Arzamas ------------------------------------
RECORDS.append(rec(
    "arzamas-resurrection-cathedral",
    "Nhà thờ chính toà Phục Sinh ở Arzamas (Voskresensky sobor)",
    "Воскресенский собор (Арзамас)",
    "Resurrection Cathedral in Arzamas",
    ["church"],
    55.38668, 43.81342,
    "Quảng trường Nhà thờ (Соборная площадь), thành phố Arzamas, tỉnh Nizhny Novgorod, cách Nizhny Novgorod khoảng 110 km về phía nam, Nga.",
    "Nhà thờ Phục Sinh là biểu tượng bề thế của thành phố cổ Arzamas, được dựng năm 1814–1842 để tạ ơn chiến thắng Napoléon năm 1812. Công trình tân cổ điển đồ sộ với năm vòm mái, hàng cột lớn bốn phía và nội thất vẽ theo lối grisaille (đơn sắc) do kiến trúc sư người Arzamas Mikhail Korinfsky thiết kế.",
    "Ngự trên đỉnh đồi giữa Quảng trường Nhà thờ của Arzamas, Nhà thờ chính toà Phục Sinh là một trong những thánh đường tân cổ điển hùng vĩ nhất vùng Volga. Nhà thờ được xây trong gần ba thập niên (1814–1842) như một đài kỷ niệm chiến thắng của nước Nga trước quân Napoléon năm 1812; phần lớn kinh phí đến từ đóng góp của người dân Arzamas. Người thiết kế là Mikhail Korinfsky, một kiến trúc sư sinh tại chính Arzamas và là học trò của bậc thầy Andrey Voronikhin. Khối nhà thờ vuông vức đội năm vòm mái lớn, bốn mặt đều có hàng cột portico đồ sộ, tạo dáng vẻ cân đối trang nghiêm nhìn thấy từ khắp thành phố. Bên trong, các bức tường và vòm được trang trí bằng tranh grisaille – kỹ thuật vẽ đơn sắc mô phỏng phù điêu đá – hiếm gặp và rất được ngưỡng mộ. Ngày nay nhà thờ vẫn là trung tâm tôn giáo và điểm tham quan chính khi ghé Arzamas, thường được kết hợp với việc dạo quanh quần thể các nhà thờ cổ vây quanh quảng trường.",
    [
        "Đài kỷ niệm chiến thắng Napoléon 1812, xây dựng 1814–1842.",
        "Kiến trúc tân cổ điển đồ sộ với năm vòm mái và bốn hàng cột, do Mikhail Korinfsky thiết kế.",
        "Nội thất trang trí bằng tranh grisaille đơn sắc mô phỏng phù điêu, độc đáo bậc nhất.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày, thường khoảng 7:00–19:00 theo lịch hành lễ.",
        "ticket_vi": "Vào tự do (miễn phí); quyên góp tuỳ tâm.",
        "duration_vi": "Khoảng 40–60 phút (kèm dạo quảng trường).",
        "best_time_vi": "Cuối xuân đến đầu thu; buổi sáng ánh sáng đẹp cho khối kiến trúc trắng.",
        "tips_vi": "Kết hợp tham quan cả cụm nhà thờ quanh Quảng trường Nhà thờ; ăn mặc kín đáo khi vào.",
    },
    [
        {"title": "Wikipedia (RU) — Воскресенский собор (Арзамас)", "url": "https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D1%81%D0%BA%D1%80%D0%B5%D1%81%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80_(%D0%90%D1%80%D0%B7%D0%B0%D0%BC%D0%B0%D1%81)"},
        {"title": "sobory.ru — Арзамас, собор Воскресения Христова", "url": "https://sobory.ru/article/?object=00903"},
    ],
    ["church", "cathedral", "arzamas", "neoclassical", "1812", "grisaille"],
    maps_text("Воскресенский собор", "Арзамас",
              "Resurrection Cathedral", "Arzamas", 55.38668, 43.81342),
))

# 5) Điền trang Rukavishnikov (bảo tàng-bảo tồn NN) ---------------------------
RECORDS.append(rec(
    "rukavishnikov-estate",
    "Điền trang Rukavishnikov (Usadba Rukavishnikovykh)",
    "Усадьба Рукавишниковых",
    "Rukavishnikov Estate (Mansion)",
    ["palace", "museum"],
    56.32933, 44.01624,
    "Bờ sông Thượng Volga (Верхне-Волжская набережная) số 7, thành phố Nizhny Novgorod, Nga.",
    "Điền trang Rukavishnikov là dinh thự lộng lẫy bậc nhất trên bờ sông Thượng Volga, xây năm 1875–1877 cho gia đình đại thương nhân Sergei Rukavishnikov theo phong cách cung điện Ý. Mặt tiền trang trí dày đặc phù điêu, tượng thần vác mái (atlant), nội thất mạ vàng nay là trụ sở chính của Bảo tàng – Bảo tồn Lịch sử & Kiến trúc bang Nizhny Novgorod.",
    "Trải dài trên bờ cao Thượng Volga, Điền trang Rukavishnikov là biểu tượng cho thời hoàng kim của tầng lớp thương nhân giàu có Nizhny Novgorod cuối thế kỷ 19. Dinh thự được xây dựng trong khoảng 1875–1877 cho gia đình Sergei Mikhailovich Rukavishnikov, mô phỏng một palazzo (cung điện) kiểu Ý thời Phục Hưng. Mặt tiền phủ kín hoa văn đắp nổi, những bức tượng thần atlant vạm vỡ chống đỡ ban công, còn bên trong là chuỗi phòng khách xa hoa với trần vẽ, gương lớn, cầu thang cẩm thạch và đồ trang trí mạ vàng – phô diễn sự giàu sang gần như không giới hạn của chủ nhân. Sau Cách mạng, toà nhà được quốc hữu hoá và trở thành bảo tàng; ngày nay đây là trụ sở trung tâm của Bảo tàng – Bảo tồn Lịch sử & Kiến trúc bang Nizhny Novgorod, giới thiệu các trưng bày về lịch sử vùng đất và chính đời sống quý tộc – thương nhân xưa. Tham quan các phòng nội thất được phục dựng công phu là một trải nghiệm không nên bỏ lỡ, giúp hình dung nhịp sống thượng lưu bên sông Volga hơn một thế kỷ trước.",
    [
        "Dinh thự thương nhân lộng lẫy nhất bờ Thượng Volga, xây 1875–1877 theo kiểu palazzo Ý.",
        "Mặt tiền dày đặc phù điêu và tượng thần atlant; nội thất mạ vàng, cầu thang cẩm thạch.",
        "Trụ sở chính Bảo tàng – Bảo tồn Lịch sử & Kiến trúc bang Nizhny Novgorod với nhiều trưng bày.",
    ],
    {
        "hours_vi": "Thường mở cửa khoảng 10:00–18:00, nghỉ một ngày trong tuần (thường thứ Hai); kiểm tra lịch trước khi đi.",
        "ticket_vi": "Bán vé tham quan bảo tàng; có vé riêng cho các trưng bày/tour theo phòng nội thất.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (điểm tham quan trong nhà); kết hợp dạo bờ Thượng Volga khi trời đẹp.",
        "tips_vi": "Nên đi tour có hướng dẫn để vào các phòng nội thất đẹp nhất; kết hợp cầu thang Chkalov gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Усадьба Рукавишниковых", "url": "https://ru.wikipedia.org/wiki/%D0%A3%D1%81%D0%B0%D0%B4%D1%8C%D0%B1%D0%B0_%D0%A0%D1%83%D0%BA%D0%B0%D0%B2%D0%B8%D1%88%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D1%85"},
        {"title": "Bảo tàng – Bảo tồn Lịch sử & Kiến trúc bang NN (ngmii.ru)", "url": "https://www.ngiamz.ru"},
    ],
    ["mansion", "museum", "merchant", "19th-century", "volga", "architecture"],
    maps_org("https://yandex.com/maps/org/manor_of_rukavishnikov/142204953534/",
             "Rukavishnikov Manor", "Nizhny Novgorod"),
))

# 6) Bảo tàng Mỹ thuật bang Nizhny Novgorod (НГХМ) ---------------------------
RECORDS.append(rec(
    "nizhny-novgorod-art-museum",
    "Bảo tàng Mỹ thuật bang Nizhny Novgorod (NGHM)",
    "Нижегородский государственный художественный музей",
    "Nizhny Novgorod State Art Museum",
    ["museum"],
    56.32952, 44.00640,
    "Toà nhà Nghệ thuật Nga: khuôn viên Kremlin, dãy nhà số 3 (nhà cựu Toàn quyền quân sự), thành phố Nizhny Novgorod, Nga.",
    "Bảo tàng Mỹ thuật bang Nizhny Novgorod thành lập năm 1896, là một trong những bảo tàng nghệ thuật lâu đời và giàu có nhất tỉnh. Bộ sưu tập nghệ thuật Nga đặt trong toà nhà cựu Toàn quyền quân sự bên trong Kremlin, nổi tiếng với bức tranh khổng lồ 'Lời hiệu triệu của Minin' của Konstantin Makovsky.",
    "Ra đời năm 1896 nhân dịp Triển lãm Toàn Nga tổ chức tại Nizhny Novgorod, Bảo tàng Mỹ thuật bang là một trong những bảo tàng nghệ thuật tỉnh lâu đời nhất nước Nga. Phần trưng bày nghệ thuật Nga được đặt trong toà nhà cựu dinh Toàn quyền quân sự nằm ngay trong khuôn viên Kremlin, quy tụ tác phẩm của hầu hết các bậc thầy hội hoạ Nga thế kỷ 18–20 như Repin, Levitan, Aivazovsky, Serov, Roerich. Kho báu nổi tiếng nhất là bức 'Lời hiệu triệu của Kuzma Minin' – tấm toan khổ khổng lồ của Konstantin Makovsky, tái hiện khoảnh khắc người anh hùng Minin kêu gọi dân Nizhny Novgorod đứng lên cứu nước năm 1611; bức tranh lớn đến mức có hẳn một phòng riêng. Bảo tàng còn có chi nhánh trưng bày nghệ thuật Tây Âu đặt trong toà nhà Sirotkin bên bờ Thượng Volga, với các tác phẩm châu Âu từ thế kỷ 15 đến 20. Đây là điểm đến hàng đầu cho người yêu hội hoạ khi tới thành phố, lại rất tiện vì nằm ngay trong Kremlin.",
    [
        "Bảo tàng nghệ thuật tỉnh lâu đời (từ 1896) với sưu tập phong phú các bậc thầy Nga.",
        "Sở hữu bức tranh khổng lồ 'Lời hiệu triệu của Minin' của Konstantin Makovsky, trưng bày trong phòng riêng.",
        "Toà nhà Nghệ thuật Nga nằm ngay trong Kremlin; chi nhánh nghệ thuật Tây Âu ở nhà Sirotkin bên sông.",
    ],
    {
        "hours_vi": "Thường mở khoảng 11:00–18:00 (một số ngày muộn hơn), nghỉ một ngày trong tuần; kiểm tra lịch trước.",
        "ticket_vi": "Bán vé vào cửa; vé kết hợp cho cả hai toà nhà; có ưu đãi cho học sinh, người cao tuổi.",
        "duration_vi": "Khoảng 1–2 giờ mỗi toà nhà.",
        "best_time_vi": "Quanh năm (tham quan trong nhà).",
        "tips_vi": "Kết hợp tham quan Kremlin cùng lượt; dành thời gian cho phòng tranh Makovsky.",
    },
    [
        {"title": "Wikipedia (RU) — Нижегородский художественный музей", "url": "https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B9_%D1%85%D1%83%D0%B4%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BC%D1%83%D0%B7%D0%B5%D0%B9"},
        {"title": "Trang chính thức Bảo tàng Mỹ thuật NN (artmuseumnn.ru)", "url": "https://artmuseumnn.ru"},
    ],
    ["museum", "art", "makovsky", "russian-painting", "kremlin"],
    maps_org("https://yandex.com/maps/org/nizhny_novgorod_art_museum/1084670002/",
             "Nizhny Novgorod Art Museum", "Nizhny Novgorod"),
    official_site="https://artmuseumnn.ru",
))

# 7) Domik Kashirina — Bảo tàng tuổi thơ Maxim Gorky -------------------------
RECORDS.append(rec(
    "kashirin-house-gorky-museum",
    "Nhà Kashirin – Bảo tàng tuổi thơ Maxim Gorky (Domik Kashirina)",
    "Музей детства А. М. Горького «Домик Каширина»",
    "Kashirin House – Museum of Maxim Gorky's Childhood",
    ["museum"],
    56.32388, 43.99077,
    "Phố Pochtovy sъezd (Почтовый съезд) số 21, thành phố Nizhny Novgorod, Nga.",
    "'Nhà nhỏ Kashirin' là ngôi nhà gỗ nơi văn hào Maxim Gorky sống thời thơ ấu bên gia đình ông ngoại Vasily Kashirin. Chính nơi đây đã trở thành bối cảnh cho cuốn tiểu thuyết tự truyện nổi tiếng 'Thời thơ ấu'; bảo tàng phục dựng nguyên vẹn nội thất một gia đình thợ nhuộm Nga giữa thế kỷ 19.",
    "Nằm trên con dốc Pochtovy sъezd dẫn xuống sông Oka, 'Nhà nhỏ Kashirin' là một trong những bảo tàng văn học được yêu mến nhất Nizhny Novgorod – quê hương của đại văn hào Maxim Gorky (Alexei Peshkov). Đây chính là ngôi nhà của ông bà ngoại Kashirin, nơi cậu bé Alexei được gửi tới sống sau khi cha mất và đã trải qua những năm tháng tuổi thơ nhọc nhằn. Những gì diễn ra dưới mái nhà này – xưởng nhuộm của ông ngoại, không khí gia trưởng ngột ngạt xen lẫn tình thương của bà ngoại – về sau được Gorky tái hiện sống động trong tiểu thuyết tự truyện 'Thời thơ ấu' (Детство). Mở cửa làm bảo tàng từ năm 1938, ngôi nhà gỗ cùng sân, nhà kho và xưởng nhuộm được phục dựng tỉ mỉ theo đúng mô tả trong tác phẩm và ký ức đương thời, tái hiện chân thực nếp sống của một gia đình thị dân – thợ thủ công Nga giữa thế kỷ 19. Với người yêu văn học Nga, ghé thăm nơi này giống như bước thẳng vào từng trang sách của Gorky.",
    [
        "Ngôi nhà gỗ nơi Maxim Gorky sống thời thơ ấu cùng ông bà ngoại Kashirin.",
        "Bối cảnh có thật của tiểu thuyết tự truyện 'Thời thơ ấu' (Детство).",
        "Nội thất, sân và xưởng nhuộm phục dựng nguyên vẹn nếp sống thị dân Nga giữa thế kỷ 19.",
    ],
    {
        "hours_vi": "Thường mở khoảng 9:00–17:00, nghỉ một ngày trong tuần; kiểm tra lịch trước khi đến.",
        "ticket_vi": "Vé vào cửa giá phổ thông, khá rẻ; có ưu đãi cho học sinh, sinh viên.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm; dễ chịu nhất vào mùa ấm khi đi bộ trên dốc.",
        "tips_vi": "Đọc trước vài trang 'Thời thơ ấu' để cảm nhận sâu hơn; kết hợp các bảo tàng Gorky khác trong thành phố.",
    },
    [
        {"title": "Wikipedia (RU) — Домик Каширина", "url": "https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%B8%D0%BA_%D0%9A%D0%B0%D1%88%D0%B8%D1%80%D0%B8%D0%BD%D0%B0"},
        {"title": "Bảo tàng A. M. Gorky Nizhny Novgorod (museumgorkogo.ru)", "url": "https://museumgorkogo.ru"},
    ],
    ["museum", "literature", "gorky", "childhood", "wooden-house"],
    maps_org("https://yandex.com/maps/org/gorky_childhood_museum_kashirin_house/1107072794/",
             "Kashirin House Gorky Childhood Museum", "Nizhny Novgorod"),
))

# 8) Bảo tàng tưởng niệm V. P. Chkalov ở Chkalovsk --------------------------
RECORDS.append(rec(
    "chkalov-museum-chkalovsk",
    "Bảo tàng tưởng niệm phi công V. P. Chkalov (Chkalovsk)",
    "Мемориальный музей В. П. Чкалова",
    "V. P. Chkalov Memorial Museum",
    ["museum"],
    56.765074, 43.265766,
    "Phố Chkalov (ул. Чкалова) số 5, thành phố Chkalovsk, tỉnh Nizhny Novgorod, bên hồ chứa Gorky trên sông Volga, Nga.",
    "Bảo tàng tưởng niệm nằm tại quê hương của Valery Chkalov (1904–1938) – phi công huyền thoại Liên Xô, người đầu tiên bay xuyên Bắc Cực từ Moskva sang Mỹ năm 1937. Khu bảo tàng gồm ngôi nhà thời thơ ấu của ông và một nhà vòm lớn trưng bày những chiếc máy bay gắn liền tên tuổi ông, trong đó có chiếc ANT-25.",
    "Thành phố nhỏ Chkalovsk bên hồ chứa Gorky vốn mang tên Vasilyovo, được đổi tên để vinh danh người con nổi tiếng nhất của mình: phi công thử nghiệm Valery Chkalov (1904–1938). Chkalov là anh hùng Liên Xô, nổi danh toàn thế giới sau chuyến bay lịch sử năm 1937 khi ông cùng đồng đội lái chiếc ANT-25 bay thẳng từ Moskva, vượt qua Bắc Cực và hạ cánh xuống Vancouver (bang Washington, Mỹ) – chuyến bay xuyên cực đầu tiên nối liền hai lục địa. Bảo tàng tưởng niệm được lập ngay tại quê ông, gồm ngôi nhà gỗ nơi ông sinh ra và lớn lên (phục dựng nội thất đầu thế kỷ 20) cùng một nhà vòm – ăng-ga lớn trưng bày các máy bay thật gắn với sự nghiệp của ông, đáng chú ý nhất là chiếc ANT-25 huyền thoại và một số phi cơ tiêm kích, thuỷ phi cơ ông từng thử nghiệm. Đây là điểm đến hấp dẫn cho những ai yêu lịch sử hàng không, đồng thời là dịp khám phá một thị trấn ven sông Volga yên bình.",
    [
        "Quê hương phi công huyền thoại Valery Chkalov (1904–1938), Anh hùng Liên Xô.",
        "Nhà vòm – ăng-ga trưng bày máy bay thật, nổi bật là chiếc ANT-25 bay xuyên Bắc Cực sang Mỹ (1937).",
        "Ngôi nhà thời thơ ấu của Chkalov phục dựng nguyên trạng đầu thế kỷ 20.",
    ],
    {
        "hours_vi": "Thường mở khoảng 9:00–17:00, nghỉ một ngày trong tuần; nên kiểm tra lịch trước.",
        "ticket_vi": "Bán vé vào cửa; vé riêng cho nhà ăng-ga trưng bày máy bay.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; kết hợp dạo bờ hồ chứa Gorky khi trời đẹp.",
        "tips_vi": "Chkalovsk cách Nizhny Novgorod khoảng 100 km; thuận tiện đi bằng ô tô, có thể ghép cùng Gorodets.",
    },
    [
        {"title": "Wikipedia (RU) — Чкалов, Валерий Павлович", "url": "https://ru.wikipedia.org/wiki/%D0%A7%D0%BA%D0%B0%D0%BB%D0%BE%D0%B2,_%D0%92%D0%B0%D0%BB%D0%B5%D1%80%D0%B8%D0%B9_%D0%9F%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D0%B8%D1%87"},
        {"title": "Yandex Maps — Мемориальный музей В. П. Чкалова (Дом Валерия Чкалова)", "url": "https://yandex.ru/maps/org/memorialny_muzey_v_p_chkalova_dom_valeriya_chkalova/134959545013/"},
    ],
    ["museum", "aviation", "chkalov", "ant-25", "history"],
    maps_org("https://yandex.ru/maps/org/memorialny_muzey_v_p_chkalova_dom_valeriya_chkalova/134959545013/",
             "Chkalov Memorial Museum", "Chkalovsk"),
))

# 9) Bảo tàng ngoài trời Shchelokovsky Khutor -------------------------------
RECORDS.append(rec(
    "shchelokovsky-khutor-museum",
    "Bảo tàng kiến trúc gỗ ngoài trời Shchelokovsky Khutor",
    "Музей архитектуры и быта народов Нижегородского Поволжья «Щёлоковский хутор»",
    "Shchelokovsky Khutor Museum of Wooden Architecture",
    ["museum", "park_garden"],
    56.27417, 44.01056,
    "Phố Gorbatovskaya (Горбатовская ул.) số 41, trong công viên rừng Shchelokovsky Khutor phía nam thành phố Nizhny Novgorod, Nga.",
    "Shchelokovsky Khutor là bảo tàng kiến trúc gỗ ngoài trời của thành phố, nằm giữa một công viên rừng phía nam. Nơi đây quy tụ những nhà thờ gỗ, nhà nông dân (izba), cối xay gió và giếng nước thế kỷ 17–19 được di dời từ khắp vùng Volga về, tái hiện đời sống làng quê Nga xưa.",
    "Ẩn mình trong một công viên rừng ở rìa nam Nizhny Novgorod, Bảo tàng Kiến trúc và Đời sống các dân tộc vùng Volga Nizhny Novgorod – quen gọi là 'Shchelokovsky Khutor' – là bảo tàng ngoài trời (skansen) tái hiện làng quê Nga truyền thống. Được thành lập từ đầu thập niên 1970, bảo tàng sưu tầm và di dời về đây những công trình gỗ tiêu biểu thế kỷ 17–19 từ khắp các huyện trong tỉnh: vài ngôi nhà thờ gỗ mái vòm thanh thoát dựng hoàn toàn không dùng đinh, các izba (nhà nông dân) với nội thất sinh hoạt nguyên bản, cối xay gió, kho thóc và giếng nước cần trục. Dạo bước trên những lối mòn giữa rừng bạch dương, du khách như lạc vào một ngôi làng Nga của mấy thế kỷ trước, tìm hiểu cách người nông dân dựng nhà, sưởi ấm, dệt vải và thờ phụng. Vào mùa hè nơi đây thường tổ chức các lễ hội dân gian, còn mùa đông tuyết phủ khiến khung cảnh những mái nhà gỗ càng thêm nên thơ. Đây là điểm đến thư giãn, kết hợp thiên nhiên và di sản, rất hợp cho gia đình.",
    [
        "Bảo tàng gỗ ngoài trời (skansen) với nhà thờ, izba, cối xay gió thế kỷ 17–19.",
        "Các công trình di dời từ khắp vùng Volga, nhiều nhà thờ gỗ dựng không dùng đinh.",
        "Nằm giữa công viên rừng yên tĩnh phía nam thành phố, hay có lễ hội dân gian mùa hè.",
    ],
    {
        "hours_vi": "Khu ngoài trời thường mở hằng ngày khoảng 10:00–18:00 (mùa đông có thể ngắn hơn); một số nhà mở theo giờ.",
        "ticket_vi": "Vé vào cửa giá phổ thông; có thể thu thêm phí cho một số nhà trưng bày hoặc sự kiện.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Mùa hè cho lễ hội và cây xanh; mùa đông tuyết phủ cũng rất đẹp.",
        "tips_vi": "Đi giày thoải mái để dạo đường rừng; mang nước và đồ chống muỗi vào mùa ấm.",
    },
    [
        {"title": "Wikipedia (RU) — Щёлоковский хутор (музей)", "url": "https://ru.wikipedia.org/wiki/%D0%A9%D1%91%D0%BB%D0%BE%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D1%85%D1%83%D1%82%D0%BE%D1%80_(%D0%BC%D1%83%D0%B7%D0%B5%D0%B9)"},
        {"title": "Culture.ru — Музей «Щёлоковский хутор»", "url": "https://www.culture.ru/institutes/11994/muzej-shyolokovskij-hutor"},
    ],
    ["museum", "open-air", "wooden-architecture", "skansen", "folk-life"],
    maps_text("Музей Щёлоковский хутор", "Нижний Новгород",
              "Shchelokovsky Khutor Museum", "Nizhny Novgorod", 56.27417, 44.01056),
))

# 10) Cung thiên văn Nizhny Novgorod (planetarium) --------------------------
RECORDS.append(rec(
    "nizhny-novgorod-planetarium",
    "Cung thiên văn Nizhny Novgorod mang tên G. M. Grechko",
    "Нижегородский планетарий имени Г. М. Гречко",
    "Nizhny Novgorod Planetarium named after G. M. Grechko",
    ["museum", "other"],
    56.31855, 43.95484,
    "Phố Revolyutsii (ул. Революции) số 20, gần khu Hội chợ, thành phố Nizhny Novgorod, Nga.",
    "Cung thiên văn Nizhny Novgorod là một trong những cung thiên văn lâu đời nhất nước Nga (từ năm 1948) và là cung thiên văn đầu tiên trong nước được trang bị hệ chiếu vòm kỹ thuật số hiện đại. Toà nhà mới (2005) mang tên nhà du hành vũ trụ Georgy Grechko, có nhà hát ngôi sao, đài quan sát và nhiều chương trình khoa học.",
    "Khai trương từ năm 1948, Cung thiên văn Nizhny Novgorod nằm trong số những cung thiên văn hoạt động lâu đời nhất nước Nga. Sau nhiều thập niên đặt trong một nhà thờ cũ, cung thiên văn chuyển tới toà nhà hiện đại được xây riêng trên phố Revolyutsii vào năm 2005, và trở thành cung thiên văn đầu tiên ở Nga lắp đặt hệ thống máy chiếu vòm kỹ thuật số toàn cảnh. Công trình mang tên Georgy Grechko – nhà du hành vũ trụ Liên Xô hai lần Anh hùng, người có nhiều gắn bó với thành phố. Bên trong có 'Nhà hát Ngôi sao' với mái vòm lớn trình chiếu bầu trời đêm và các bộ phim khoa học vòm 360 độ, cùng phòng trưng bày tương tác, đài quan sát với kính thiên văn để ngắm Mặt Trăng và các hành tinh trong những buổi tối trời quang. Đây là điểm đến giáo dục – giải trí hấp dẫn, đặc biệt phù hợp với gia đình có trẻ em và những người yêu thích thiên văn, đồng thời là một lựa chọn thú vị cho ngày thời tiết xấu.",
    [
        "Một trong những cung thiên văn lâu đời nhất nước Nga (từ 1948).",
        "Cung thiên văn Nga đầu tiên có hệ chiếu vòm kỹ thuật số toàn cảnh (toà nhà mới 2005).",
        "Mang tên nhà du hành vũ trụ Georgy Grechko; có Nhà hát Ngôi sao, đài quan sát và trưng bày tương tác.",
    ],
    {
        "hours_vi": "Mở theo lịch suất chiếu, thường khoảng 9:00–19:00; nghỉ một ngày trong tuần.",
        "ticket_vi": "Bán vé theo từng suất chương trình; nên đặt trước cho suất đông khách và cuối tuần.",
        "duration_vi": "Khoảng 45–60 phút mỗi chương trình.",
        "best_time_vi": "Quanh năm; buổi tối trời quang thích hợp cho quan sát qua kính thiên văn.",
        "tips_vi": "Xem lịch suất chiếu và chọn chương trình phù hợp độ tuổi; đặt vé trực tuyến khi có thể.",
    },
    [
        {"title": "Wikipedia (RU) — Нижегородский планетарий", "url": "https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0%D1%80%D0%B8%D0%B9"},
        {"title": "Trang chính thức Cung thiên văn NN (planetariumnn.ru)", "url": "https://planetariumnn.ru"},
    ],
    ["planetarium", "science", "astronomy", "family", "grechko"],
    maps_org("https://yandex.com/maps/org/nizhny_novgorod_planetarium_named_after_grechko/1105202712/",
             "Nizhny Novgorod Planetarium", "Nizhny Novgorod"),
    official_site="https://planetariumnn.ru",
))

# 11) Nhà hát kịch bang mang tên M. Gorky ----------------------------------
RECORDS.append(rec(
    "gorky-drama-theatre",
    "Nhà hát kịch hàn lâm bang Nizhny Novgorod mang tên M. Gorky",
    "Нижегородский государственный академический театр драмы имени М. Горького",
    "Nizhny Novgorod State Academic Drama Theatre named after M. Gorky",
    ["theatre"],
    56.32416, 44.00135,
    "Phố đi bộ Bolshaya Pokrovskaya (Большая Покровская) số 13, thành phố Nizhny Novgorod, Nga.",
    "Nhà hát kịch mang tên M. Gorky là một trong những nhà hát lâu đời nhất nước Nga, có gốc từ năm 1798. Toà nhà lộng lẫy hiện nay khánh thành năm 1896 trên phố đi bộ Bolshaya Pokrovskaya, do kiến trúc sư Viktor Schröter thiết kế theo phong cách chiết trung cầu kỳ.",
    "Toạ lạc ngay trên phố đi bộ sầm uất Bolshaya Pokrovskaya, Nhà hát kịch bang Nizhny Novgorod là một trong những đoàn kịch lâu đời nhất nước Nga, với lịch sử truy về tận năm 1798. Toà nhà nhà hát hiện nay được khánh thành năm 1896 – đúng dịp Triển lãm Toàn Nga tổ chức tại thành phố – theo thiết kế của kiến trúc sư danh tiếng Viktor Schröter. Mặt tiền trang trí công phu với các chi tiết đắp nổi, tượng và ban công, còn khán phòng bên trong lộng lẫy theo phong cách sân khấu cổ điển châu Âu. Nhà hát mang tên đại văn hào Maxim Gorky – người con của thành phố – và trên sân khấu này nhiều vở kịch kinh điển của ông cùng các tác gia Nga và thế giới vẫn được dàn dựng đều đặn. Ngay cả khi không xem biểu diễn, du khách vẫn thường dừng chân trước nhà hát để chiêm ngưỡng một trong những công trình đẹp nhất của phố Pokrovskaya và chụp ảnh cùng bức tượng đồng nghệ sĩ đặt gần đó.",
    [
        "Một trong những nhà hát lâu đời nhất nước Nga, có gốc từ năm 1798.",
        "Toà nhà tráng lệ khánh thành 1896 do kiến trúc sư Viktor Schröter thiết kế.",
        "Nằm ngay trên phố đi bộ Bolshaya Pokrovskaya, mang tên đại văn hào Maxim Gorky.",
    ],
    {
        "hours_vi": "Phòng vé mở ban ngày; suất diễn thường vào buổi tối và cuối tuần theo lịch mùa diễn.",
        "ticket_vi": "Mua vé theo vở diễn tại phòng vé hoặc trực tuyến; giá đa dạng theo hạng ghế.",
        "duration_vi": "Ngắm bên ngoài ~15 phút; một buổi diễn khoảng 2–3 giờ.",
        "best_time_vi": "Mùa diễn (thu–xuân); mặt tiền đẹp cả ngày lẫn khi lên đèn.",
        "tips_vi": "Xem lịch diễn và đặt vé trước; kết hợp dạo trọn phố đi bộ Bolshaya Pokrovskaya.",
    },
    [
        {"title": "Wikipedia (RU) — Нижегородский театр драмы имени М. Горького", "url": "https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D0%B5%D0%B0%D1%82%D1%80_%D0%B4%D1%80%D0%B0%D0%BC%D1%8B"},
        {"title": "Trang chính thức Nhà hát kịch NN (dramteatr.nnov.ru)", "url": "https://dramteatr.nnov.ru"},
    ],
    ["theatre", "drama", "architecture", "pokrovskaya", "gorky"],
    maps_org("https://yandex.com/maps/org/drama_theatre/1142767990/",
             "Nizhny Novgorod Drama Theatre", "Nizhny Novgorod"),
    official_site="https://dramteatr.nnov.ru",
))

# 12) Nhà hát Opera và Ballet mang tên A. S. Pushkin ------------------------
RECORDS.append(rec(
    "nizhny-novgorod-opera-ballet",
    "Nhà hát Opera và Ballet hàn lâm bang mang tên A. S. Pushkin",
    "Нижегородский государственный академический театр оперы и балета имени А. С. Пушкина",
    "Nizhny Novgorod State Academic Opera and Ballet Theatre named after A. S. Pushkin",
    ["theatre"],
    56.31583, 44.01696,
    "Phố Belinskogo (ул. Белинского) số 59, thành phố Nizhny Novgorod, Nga.",
    "Nhà hát Opera và Ballet mang tên A. S. Pushkin là sân khấu nhạc kịch chính của Nizhny Novgorod, thành lập năm 1935. Đây cũng là nơi tổ chức Liên hoan nghệ thuật quốc tế 'Những buổi hoà nhạc Sakharov' danh tiếng, quy tụ nhiều nghệ sĩ opera và ballet hàng đầu.",
    "Được thành lập năm 1935, Nhà hát Opera và Ballet hàn lâm bang Nizhny Novgorod là trung tâm nghệ thuật hàn lâm hàng đầu của thành phố trong lĩnh vực nhạc kịch. Nhà hát mang tên đại thi hào Aleksandr Pushkin, gắn với việc khai trương đúng dịp kỷ niệm 100 năm ngày mất của ông. Trên sân khấu này, các vở opera kinh điển Nga và thế giới – từ Tchaikovsky, Rimsky-Korsakov đến Verdi, Puccini – cùng những vở ballet lớn được dàn dựng công phu với dàn nhạc, hợp xướng và đoàn múa riêng. Nhà hát đặc biệt nổi tiếng nhờ là nơi tổ chức Liên hoan Nghệ thuật quốc tế mang tên viện sĩ Andrei Sakharov, sự kiện âm nhạc uy tín thu hút nghệ sĩ và khán giả từ nhiều quốc gia. Với những ai muốn thưởng thức một đêm opera hoặc ballet đúng chất Nga trong không gian trang trọng, đây là lựa chọn hàng đầu tại Nizhny Novgorod.",
    [
        "Sân khấu opera – ballet chính của thành phố, thành lập năm 1935.",
        "Mang tên đại thi hào A. S. Pushkin; dàn dựng nhiều vở kinh điển Nga và thế giới.",
        "Nơi tổ chức Liên hoan Nghệ thuật quốc tế mang tên viện sĩ Sakharov danh tiếng.",
    ],
    {
        "hours_vi": "Phòng vé mở ban ngày; suất diễn chủ yếu buổi tối và cuối tuần theo lịch mùa diễn.",
        "ticket_vi": "Mua vé theo vở tại phòng vé hoặc trực tuyến; giá theo hạng ghế và chương trình.",
        "duration_vi": "Một buổi opera/ballet thường 2–3 giờ.",
        "best_time_vi": "Mùa diễn (thu–xuân); dịp Liên hoan Sakharov có nhiều chương trình đặc sắc.",
        "tips_vi": "Đặt vé sớm cho các buổi diễn lớn; đến sớm để ổn định chỗ và gửi áo khoác.",
    },
    [
        {"title": "Wikipedia (RU) — Нижегородский театр оперы и балета", "url": "https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D0%B5%D0%B0%D1%82%D1%80_%D0%BE%D0%BF%D0%B5%D1%80%D1%8B_%D0%B8_%D0%B1%D0%B0%D0%BB%D0%B5%D1%82%D0%B0"},
        {"title": "Trang chính thức Nhà hát Opera & Ballet NN (operann.ru)", "url": "https://operann.ru"},
    ],
    ["theatre", "opera", "ballet", "sakharov-festival", "pushkin"],
    maps_org("https://yandex.com/maps/org/nizhny_novgorod_state_academic_opera_and_ballet_theater_named_after_a_s_pushkin/157011455751/",
             "Nizhny Novgorod Opera and Ballet Theatre", "Nizhny Novgorod"),
    official_site="https://operann.ru",
))

# 13) Toà nhà Ngân hàng Nhà nước (Госбанк) ---------------------------------
RECORDS.append(rec(
    "state-bank-building-nn",
    "Toà nhà Ngân hàng Nhà nước Nizhny Novgorod (Gosbank)",
    "Здание Государственного банка (Нижний Новгород)",
    "State Bank Building",
    ["monument"],
    56.32031, 43.99886,
    "Phố đi bộ Bolshaya Pokrovskaya (Большая Покровская) số 26, thành phố Nizhny Novgorod, Nga.",
    "Toà nhà Ngân hàng Nhà nước là một trong những công trình gây ấn tượng mạnh nhất Nizhny Novgorod, xây năm 1911–1913 nhân 300 năm triều Romanov. Kiến trúc sư Vladimir Pokrovsky dựng nó theo phong cách 'tân Nga' như một lâu đài cổ tích, với nội thất bích hoạ theo phác thảo của trường phái Ivan Bilibin.",
    "Đứng trên phố đi bộ Bolshaya Pokrovskaya, Toà nhà Ngân hàng Nhà nước trông chẳng khác một lâu đài bước ra từ truyện cổ tích Nga. Công trình được xây dựng năm 1911–1913 nhân dịp kỷ niệm 300 năm vương triều Romanov, theo thiết kế của kiến trúc sư Vladimir Pokrovsky – bậc thầy của phong cách 'tân Nga' (neo-russky) phỏng theo kiến trúc terem và nhà thờ Nga cổ. Mặt ngoài toà nhà là một tổ hợp tháp nhọn, cổng vòm, mái dốc và những chi tiết chạm khắc tinh vi, kèm chiếc đồng hồ và hàng rào sắt uốn cầu kỳ. Bên trong, các sảnh được phủ bích hoạ rực rỡ theo phác thảo gắn với trường phái hoạ sĩ minh hoạ trứ danh Ivan Bilibin, cùng đèn chùm, cầu thang và trần vòm lộng lẫy. Điều đặc biệt là toà nhà đến nay vẫn là một chi nhánh hoạt động của Ngân hàng Trung ương Nga, nên nội thất chỉ mở cửa cho công chúng vào những dịp hiếm hoi (như 'Đêm bảo tàng'). Dù chỉ ngắm từ bên ngoài, đây vẫn là một trong những điểm chụp ảnh và kiến trúc đáng nhớ nhất thành phố.",
    [
        "Toà nhà kiểu 'tân Nga' như lâu đài cổ tích, xây 1911–1913 nhân 300 năm triều Romanov.",
        "Do kiến trúc sư Vladimir Pokrovsky thiết kế; bích hoạ nội thất theo trường phái Ivan Bilibin.",
        "Vẫn là chi nhánh Ngân hàng Trung ương hoạt động; nội thất chỉ mở cửa dịp đặc biệt.",
    ],
    {
        "hours_vi": "Ngắm bên ngoài bất cứ lúc nào; nội thất chỉ mở cho công chúng vào dịp đặc biệt (ví dụ 'Đêm bảo tàng').",
        "ticket_vi": "Ngắm ngoài miễn phí; tham quan nội thất theo sự kiện có tổ chức riêng.",
        "duration_vi": "Ngắm ngoài ~15–20 phút.",
        "best_time_vi": "Quanh năm; đẹp khi lên đèn buổi tối làm nổi bật các chi tiết tháp mái.",
        "tips_vi": "Kết hợp dạo phố Bolshaya Pokrovskaya; theo dõi lịch 'Đêm bảo tàng' nếu muốn vào trong.",
    },
    [
        {"title": "Wikipedia (RU) — Здание Государственного банка (Нижний Новгород)", "url": "https://ru.wikipedia.org/wiki/%D0%97%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%93%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D0%B1%D0%B0%D0%BD%D0%BA%D0%B0_(%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4)"},
        {"title": "Culture.ru — Здание Государственного банка в Нижнем Новгороде", "url": "https://www.culture.ru/institutes/nizhny-novgorod"},
    ],
    ["architecture", "neo-russian", "pokrovsky", "bilibin", "landmark"],
    maps_org("https://yandex.com/maps/org/state_bank/1252312610/",
             "State Bank Building Nizhny Novgorod", "Nizhny Novgorod"),
))

# 14) Phố cổ Rozhdestvenskaya ----------------------------------------------
RECORDS.append(rec(
    "rozhdestvenskaya-street",
    "Phố cổ Rozhdestvenskaya (Rozhdestvenskaya ulitsa)",
    "Рождественская улица (Нижний Новгород)",
    "Rozhdestvenskaya Street",
    ["square_street"],
    56.32833, 43.98750,
    "Phố Rozhdestvenskaya (Рождественская улица), khu phố dưới ven sông Oka, thành phố Nizhny Novgorod, Nga.",
    "Rozhdestvenskaya là con phố cổ đẹp nhất khu phố dưới của Nizhny Novgorod, chạy song song bờ sông Oka. Hai bên phố là dãy dinh thự thương nhân, ngân hàng và nhà thờ thế kỷ 18–19 được trùng tu, trong đó có nhà thờ Stroganov; nay là khu tản bộ nhiều quán cà phê, nhà hàng và bảo tàng nhỏ.",
    "Nếu phố Bolshaya Pokrovskaya là trục đi bộ của khu phố trên, thì Rozhdestvenskaya chính là 'linh hồn' của khu phố dưới ven sông Oka. Con phố cong mềm mại này từng là trung tâm buôn bán sầm uất của giới thương nhân Nizhny Novgorod thế kỷ 18–19, và đến nay vẫn giữ được một quần thể kiến trúc lịch sử gần như trọn vẹn: những dinh thự, nhà kho, ngân hàng và khách sạn cổ với mặt tiền được phục chế tỉ mỉ, điểm xuyết bằng viên ngọc kiến trúc là nhà thờ Stroganov lộng lẫy. Sau các đợt chỉnh trang, Rozhdestvenskaya trở thành một trong những không gian tản bộ được yêu thích nhất thành phố, nơi tập trung nhiều quán cà phê, nhà hàng, phòng trưng bày và bảo tàng nhỏ, thường xuyên diễn ra các sự kiện văn hoá và lễ hội đường phố. Đi dạo dọc con phố này, du khách vừa thưởng ngoạn kiến trúc, vừa cảm nhận nhịp sống thư thái bên sông – rất hợp để kết thúc bằng một bữa tối hoặc ly cà phê ngắm hoàng hôn trên sông Oka.",
    [
        "Con phố cổ đẹp nhất khu phố dưới, giữ gần trọn vẹn kiến trúc thương nhân thế kỷ 18–19.",
        "Có nhà thờ Stroganov cùng nhiều dinh thự, ngân hàng cổ được phục chế công phu.",
        "Không gian tản bộ sôi động với quán cà phê, nhà hàng, phòng tranh và lễ hội đường phố.",
    ],
    {
        "hours_vi": "Phố mở tự do suốt ngày; quán xá và bảo tàng nhỏ theo giờ riêng.",
        "ticket_vi": "Dạo phố miễn phí; chi phí tuỳ theo quán ăn, quán cà phê, bảo tàng ghé thăm.",
        "duration_vi": "Khoảng 1–2 giờ (kèm nghỉ chân).",
        "best_time_vi": "Cuối xuân đến đầu thu; đẹp vào chiều muộn và buổi tối khi lên đèn.",
        "tips_vi": "Kết hợp thăm nhà thờ Stroganov và ra bờ sông Oka; nhiều nhà hàng ngon nằm ngay trên phố.",
    },
    [
        {"title": "Wikipedia (RU) — Рождественская улица (Нижний Новгород)", "url": "https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D0%B6%D0%B4%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D1%83%D0%BB%D0%B8%D1%86%D0%B0_(%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4)"},
        {"title": "Culture.ru — Рождественская улица", "url": "https://www.culture.ru/institutes/nizhny-novgorod"},
    ],
    ["street", "old-town", "merchant-architecture", "promenade", "oka"],
    maps_text("Рождественская улица", "Нижний Новгород",
              "Rozhdestvenskaya Street", "Nizhny Novgorod", 56.32833, 43.98750),
))

# 15) Bờ sông Thượng Volga (Verkhne-Volzhskaya naberezhnaya) ---------------
RECORDS.append(rec(
    "verkhne-volzhskaya-embankment",
    "Bờ sông Thượng Volga (Verkhne-Volzhskaya naberezhnaya)",
    "Верхне-Волжская набережная",
    "Upper Volga Embankment",
    ["square_street", "park_garden"],
    56.32833, 44.02333,
    "Bờ sông Thượng Volga (Верхне-Волжская набережная), dọc bờ cao hữu ngạn sông Volga, thành phố Nizhny Novgorod, Nga.",
    "Bờ sông Thượng Volga là tuyến tản bộ sang trọng chạy dọc bờ cao hữu ngạn sông Volga, nối từ Cầu thang Chkalov về phía đông. Con đường rợp cây, viền bởi các dinh thự lịch sử như điền trang Rukavishnikov và nhà Sirotkin, mở ra tầm nhìn toàn cảnh dòng Volga mênh mông và bờ bên kia.",
    "Chạy dọc mép bờ cao hữu ngạn sông Volga, Bờ sông Thượng Volga là một trong những tuyến đi bộ được yêu thích và 'quý phái' nhất Nizhny Novgorod. Từ khu vực quảng trường Minin và đỉnh Cầu thang Chkalov, con đường trải dài về phía đông dưới những hàng cây, một bên là dãy dinh thự và biệt thự lịch sử cuối thế kỷ 19 – đầu thế kỷ 20 (nổi bật là điền trang Rukavishnikov lộng lẫy và toà nhà Sirotkin nay là bảo tàng), bên kia là lan can nhìn thẳng ra dòng Volga rộng lớn. Đây là nơi người dân thành phố và du khách ưa thả bộ, đạp xe, ngắm hoàng hôn và chụp ảnh toàn cảnh sông nước. Dọc theo tuyến còn có đài tưởng niệm phi công Valery Chkalov đặt ngay đầu cầu thang mang tên ông, cùng nhiều điểm ngắm cảnh lý tưởng. Kết hợp giữa kiến trúc thanh lịch, không gian xanh và khung cảnh sông Volga hùng vĩ, bờ sông Thượng Volga là điểm dừng gần như bắt buộc để cảm nhận vẻ đẹp đặc trưng của 'thành phố trên đồi cao bên sông' Nizhny Novgorod.",
    [
        "Tuyến tản bộ sang trọng dọc bờ cao sông Volga, nối liền với Cầu thang Chkalov.",
        "Viền bởi dinh thự lịch sử như điền trang Rukavishnikov và nhà Sirotkin.",
        "Điểm ngắm hoàng hôn và toàn cảnh sông Volga đẹp bậc nhất thành phố.",
    ],
    {
        "hours_vi": "Mở tự do suốt ngày; đẹp cả sáng sớm lẫn chiều tối.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 40–60 phút thả bộ.",
        "best_time_vi": "Cuối xuân đến đầu thu; hoàng hôn cho khung cảnh và ánh sáng đẹp nhất.",
        "tips_vi": "Kết hợp Cầu thang Chkalov, đài tưởng niệm Chkalov và điền trang Rukavishnikov trên cùng tuyến.",
    },
    [
        {"title": "Wikipedia (RU) — Верхне-Волжская набережная", "url": "https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D1%80%D1%85%D0%BD%D0%B5-%D0%92%D0%BE%D0%BB%D0%B6%D1%81%D0%BA%D0%B0%D1%8F_%D0%BD%D0%B0%D0%B1%D0%B5%D1%80%D0%B5%D0%B6%D0%BD%D0%B0%D1%8F"},
        {"title": "Culture.ru — Верхне-Волжская набережная, Нижний Новгород", "url": "https://www.culture.ru/institutes/nizhny-novgorod"},
    ],
    ["embankment", "promenade", "volga", "viewpoint", "architecture"],
    maps_text("Верхне-Волжская набережная", "Нижний Новгород",
              "Upper Volga Embankment", "Nizhny Novgorod", 56.32833, 44.02333),
))

# 16) Pakgauzy trên bãi Strelka (không gian văn hoá hiện đại) ---------------
RECORDS.append(rec(
    "strelka-pakgauzy",
    "Pakgauzy trên bãi Strelka – nhà hoà nhạc & triển lãm (Pakgauzy na Strelke)",
    "Пакгаузы на Стрелке",
    "The Pakgauzy on the Strelka",
    ["other", "theatre"],
    56.33524, 43.97395,
    "Bãi Strelka (Стрелка), nơi sông Oka đổ vào sông Volga, gần sân vận động Nizhny Novgorod, thành phố Nizhny Novgorod, Nga.",
    "Пакгаузы là cặp nhà kho khung thép thế kỷ 19 trên bãi Strelka, được cải tạo tài tình năm 2021–2022 thành một nhà hoà nhạc và một không gian triển lãm bọc kính hiện đại. Khung sắt lịch sử lộ ra ngoài lớp vỏ kính trong suốt đã biến nơi đây thành biểu tượng văn hoá mới của thành phố.",
    "Trên mũi đất Strelka – nơi sông Oka gặp sông Volga – hai kết cấu khung thép cũ từng bị lãng quên dưới lớp tường kho hàng nay đã hồi sinh ngoạn mục thành quần thể 'Пакгаузы'. Bộ khung kim loại có từ thế kỷ 19, được cho là gắn với các gian trưng bày của Triển lãm Công nghiệp – Nghệ thuật Toàn Nga từng tổ chức tại Nizhny Novgorod năm 1896, thuộc thời kỳ hoàng kim của kỹ thuật kết cấu thép Nga. Khi được phát hiện còn nguyên vẹn, thành phố đã quyết định bảo tồn và cải tạo (hoàn thành 2021–2022): một nhà kho biến thành nhà hoà nhạc hiện đại với âm thanh đạt chuẩn, nhà kho còn lại thành không gian triển lãm; cả hai được bọc trong lớp vỏ kính trong suốt để lộ ra bộ khung sắt lịch sử như một tác phẩm điêu khắc. Kết quả là một công trình vừa tôn vinh di sản kỹ thuật, vừa mang hơi thở đương đại, ban đêm lên đèn lung linh soi bóng xuống sông. Пакгаузы nhanh chóng trở thành một trong những địa điểm 'phải check-in' mới của Nizhny Novgorod, đặc biệt khi đứng cạnh sân vận động và nhà thờ Aleksandr Nevsky tạo thành cụm cảnh quan Strelka độc đáo.",
    [
        "Khung thép nhà kho thế kỷ 19 (được cho là từ Triển lãm Toàn Nga 1896) bọc trong vỏ kính hiện đại.",
        "Cải tạo 2021–2022 thành một nhà hoà nhạc và một không gian triển lãm đương đại.",
        "Biểu tượng văn hoá mới trên bãi Strelka, cạnh sân vận động và nhà thờ Aleksandr Nevsky.",
    ],
    {
        "hours_vi": "Không gian triển lãm và sự kiện mở theo lịch chương trình; khu ngoài trời ngắm được cả ngày.",
        "ticket_vi": "Ngắm bên ngoài miễn phí; vé riêng cho hoà nhạc và triển lãm bên trong.",
        "duration_vi": "Ngắm ngoài ~20–30 phút; kèm buổi hoà nhạc/triển lãm thì lâu hơn.",
        "best_time_vi": "Quanh năm; buổi tối khi lên đèn đẹp nhất để chụp ảnh.",
        "tips_vi": "Theo dõi lịch hoà nhạc và triển lãm để đặt vé; kết hợp tham quan cụm Strelka.",
    },
    [
        {"title": "Wikipedia (RU) — Пакгаузы на Стрелке", "url": "https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BA%D0%B3%D0%B0%D1%83%D0%B7%D1%8B_%D0%BD%D0%B0_%D0%A1%D1%82%D1%80%D0%B5%D0%BB%D0%BA%D0%B5"},
        {"title": "Culture.ru — Пакгаузы на Стрелке, Нижний Новгород", "url": "https://www.culture.ru/institutes/nizhny-novgorod"},
    ],
    ["modern", "concert-hall", "exhibition", "strelka", "architecture", "landmark"],
    maps_org("https://yandex.com/maps/org/pakgauzy/61011722775/",
             "Pakgauzy on the Strelka", "Nizhny Novgorod"),
))

# 17) Hồ Svetloyar (truyền thuyết thành phố Kitezh) ------------------------
RECORDS.append(rec(
    "svetloyar-lake",
    "Hồ Svetloyar – hồ thiêng gắn truyền thuyết thành phố Kitezh",
    "Озеро Светлояр",
    "Lake Svetloyar",
    ["park_garden"],
    56.8186, 45.0931,
    "Gần làng Vladimirskoye (Владимирское), huyện Voskresensky, tỉnh Nizhny Novgorod, cách Nizhny Novgorod khoảng 130 km về phía đông bắc, Nga.",
    "Hồ Svetloyar là một hồ nước nhỏ nhưng sâu khác thường, nổi tiếng khắp nước Nga nhờ truyền thuyết về thành phố Kitezh 'vô hình' đã chìm xuống đáy hồ để tránh quân Mông Cổ. Cảnh quan thiên nhiên tĩnh lặng cùng huyền thoại đã biến nơi đây thành điểm hành hương và di tích tự nhiên được bảo vệ.",
    "Nằm giữa vùng rừng và đồng quê huyện Voskresensky, bên làng Vladimirskoye, hồ Svetloyar là một trong những thắng cảnh gắn liền huyền thoại nổi tiếng nhất nước Nga. Mặt hồ hình bầu dục tuy không lớn nhưng lại sâu khác thường và nước trong vắt, khiến từ xưa dân gian đã bao phủ nơi đây bằng những câu chuyện kỳ bí. Nổi tiếng nhất là truyền thuyết về Kitezh – 'thành phố vô hình': tương truyền khi đại quân Batu Khan tràn tới, cả thành phố cùng nhà thờ đã chìm xuống lòng hồ để không rơi vào tay giặc, và người có tâm trong sáng vào những đêm tĩnh lặng còn nghe thấy tiếng chuông vọng lên từ đáy nước. Huyền thoại này đã truyền cảm hứng cho vở opera bất hủ 'Thành phố vô hình Kitezh' của nhà soạn nhạc Rimsky-Korsakov. Ngày nay Svetloyar vừa là di tích tự nhiên được bảo vệ, vừa là nơi hành hương: mỗi mùa hè người ta tổ chức lễ rước quanh hồ, và nơi đây cũng gắn với các nghi lễ dân gian cổ. Với du khách, đó là chốn thiên nhiên yên bình để đi bộ quanh hồ, đắm mình trong không khí huyền thoại và tìm hiểu văn hoá tâm linh Nga.",
    [
        "Hồ nhỏ nhưng sâu và trong khác thường, di tích tự nhiên được bảo vệ.",
        "Gắn truyền thuyết thành phố 'vô hình' Kitezh chìm xuống hồ để tránh quân Mông Cổ.",
        "Nguồn cảm hứng cho vở opera 'Thành phố vô hình Kitezh' của Rimsky-Korsakov; nơi hành hương mùa hè.",
    ],
    {
        "hours_vi": "Khu vực hồ mở tự do; trung tâm du khách và bảo tàng làng Vladimirskoye theo giờ riêng.",
        "ticket_vi": "Tham quan hồ miễn phí; một số bảo tàng/hoạt động ở làng có thể thu phí nhỏ.",
        "duration_vi": "Khoảng 1–2 giờ (đi bộ quanh hồ).",
        "best_time_vi": "Cuối xuân đến đầu thu; đầu tháng 7 có lễ hội truyền thống quanh hồ.",
        "tips_vi": "Cách NN khoảng 130 km, nên đi bằng ô tô; mang giày đi bộ và giữ gìn cảnh quan thiêng.",
    },
    [
        {"title": "Wikipedia (RU) — Светлояр", "url": "https://ru.wikipedia.org/wiki/%D0%A1%D0%B2%D0%B5%D1%82%D0%BB%D0%BE%D1%8F%D1%80"},
        {"title": "Wikipedia (EN) — Lake Svetloyar", "url": "https://en.wikipedia.org/wiki/Lake_Svetloyar"},
    ],
    ["lake", "nature", "legend", "kitezh", "pilgrimage", "voskresensky"],
    maps_text("Озеро Светлояр", "Владимирское Нижегородская область",
              "Lake Svetloyar", "Vladimirskoye", 56.8186, 45.0931),
))

# 18) Tháp Shukhov trên sông Oka (di tích kỹ thuật) ------------------------
RECORDS.append(rec(
    "shukhov-tower-oka",
    "Tháp Shukhov trên sông Oka (Shukhovskaya bashnya na Oke)",
    "Шуховская башня на Оке",
    "Shukhov Tower on the Oka",
    ["monument"],
    56.1933, 43.5431,
    "Bên tả ngạn sông Oka gần làng Dudenevo, huyện Bogorodsky, gần thành phố Dzerzhinsk, tỉnh Nizhny Novgorod, Nga.",
    "Tháp Shukhov trên sông Oka là một tháp lưới thép hyperboloid cao khoảng 128 m, do kỹ sư thiên tài Vladimir Shukhov thiết kế và dựng năm 1927–1929 để đỡ đường dây tải điện vượt sông Oka. Đây là tháp truyền tải kiểu hyperboloid nhiều tầng duy nhất còn sót lại trên thế giới, một di tích kỹ thuật quý giá.",
    "Vươn cao bên bờ sông Oka gần Dzerzhinsk, Tháp Shukhov trên sông Oka là một kiệt tác kỹ thuật độc nhất vô nhị của nước Nga. Tháp được kỹ sư – nhà phát minh lỗi lạc Vladimir Shukhov thiết kế và xây dựng trong khoảng 1927–1929, thuộc một cặp tháp dùng để đỡ đường dây điện cao thế vượt qua sông Oka, phục vụ nhà máy điện NiGRES. Điểm đặc biệt nằm ở kết cấu 'hyperboloid': thân tháp được tạo bởi những thanh thép thẳng đan chéo thành lưới, nhưng tổng thể lại cong mềm như chiếc eo, cho độ vững chắc cao mà lại nhẹ và tiết kiệm vật liệu – nguyên lý mà chính Shukhov đã phát minh và đăng ký từ cuối thế kỷ 19. Cao khoảng 128 mét với nhiều tầng lưới xếp chồng, đây là tháp truyền tải kiểu hyperboloid nhiều tầng duy nhất còn tồn tại trên thế giới (tháp còn lại trong cặp đã bị tháo dỡ). Sau khi bị hư hại vì nạn trộm kim loại, tháp đã được trùng tu và công nhận là di tích di sản. Với người yêu kiến trúc – kỹ thuật, đây là một điểm đến hiếm có, minh chứng cho tài năng vượt thời đại của kỹ sư Shukhov.",
    [
        "Tháp lưới thép hyperboloid cao khoảng 128 m, do kỹ sư Vladimir Shukhov dựng năm 1927–1929.",
        "Tháp truyền tải kiểu hyperboloid nhiều tầng duy nhất còn sót lại trên thế giới.",
        "Di tích kỹ thuật độc đáo bên sông Oka, minh chứng cho nguyên lý kết cấu thiên tài của Shukhov.",
    ],
    {
        "hours_vi": "Khu vực ngoài trời, tiếp cận tự do ban ngày; không có giờ mở cửa cố định.",
        "ticket_vi": "Miễn phí (ngắm từ bên ngoài; không leo lên tháp).",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu, khi thời tiết thuận lợi cho việc di chuyển và chụp ảnh.",
        "tips_vi": "Nằm ở khu vực ven sông hẻo lánh gần Dzerzhinsk, nên đi bằng ô tô; đi giày phù hợp địa hình.",
    },
    [
        {"title": "Wikipedia (RU) — Шуховская башня на Оке", "url": "https://ru.wikipedia.org/wiki/%D0%A8%D1%83%D1%85%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D0%B1%D0%B0%D1%88%D0%BD%D1%8F_%D0%BD%D0%B0_%D0%9E%D0%BA%D0%B5"},
        {"title": "Wikipedia (EN) — NiGRES tower / Shukhov Oka Towers", "url": "https://en.wikipedia.org/wiki/Shukhov_Tower_on_the_Oka_River"},
    ],
    ["engineering", "hyperboloid", "shukhov", "monument", "oka", "industrial-heritage"],
    maps_text("Шуховская башня на Оке", "Дзержинск",
              "Shukhov Tower on the Oka", "Dzerzhinsk", 56.1933, 43.5431),
))

PLAN = {"nizhny-novgorod.json": RECORDS}


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
