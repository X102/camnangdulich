# -*- coding: utf-8 -*-
"""_add_places_mari-el_20260728_220909.py — VÙNG: Cộng hoà Mari El (Республика Марий Эл)
(lần chạy tự động 2026-07-28).

Bối cảnh: mari-el.json hiện có 7 địa điểm (Bờ kè Bruges, Kremlin Tsarevokokshaysk, Lâu đài
Sheremetev ở Yurino, Vườn quốc gia Mari Chodra, thị trấn Kozmodemyansk, Rừng thiêng Mari,
Bảo tàng Quốc gia T. Evseev). Bổ sung 23 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa
dạng loại hình → đưa vùng lên 30.

Thủ phủ Yoshkar-Ola nổi tiếng vì kiến trúc "châu Âu thu nhỏ" bên các bờ kè phỏng theo Bruges,
Amsterdam; vì thế cụm nhà thờ, tháp đồng hồ, quảng trường và tượng đài trung tâm chiếm tỷ trọng
lớn (đúng bản chất điểm đến), bên cạnh chuỗi hồ karst - suối - rừng của Mari Chodra và vài điểm
xa thủ phủ (tu viện Ежово, hồ sâu Зрыв, hang khai thác đá Нолькин камень).

Phân bố loại hình (23 bản ghi mới):
- church (5): Благовещенский собор, Воскресенский собор, Троицкая церковь, Собор Вознесения
  Господня, Мироносицкий монастырь (Ежово).
- monument (4): Благовещенская башня (куранты), Йошкин кот, Грейс Келли & Ренье III, Рембрандт.
- square_street (2): площадь Оболенского-Ноготкова (đồng hồ có tượng lừa/icon), Патриаршая площадь.
- theatre (2): Республиканский театр кукол, Марийский нацтеатр драмы им. Шкетана.
- museum (1): Музей истории города Йошкар-Олы.
- palace (1): Дворец бракосочетаний (замок ЗАГС на набережной Брюгге).
- park_garden (7): Морской Глаз, Яльчик, Зелёный ключ, Дуб Пугачёва, Табашинское/Зрыв,
  Кленовая Гора, Кичиер.
- other (1): Нолькин камень (штольни-каменоломни).

TOẠ ĐỘ — xác minh chéo (API toạ độ ru.wikipedia prop=coordinates, OpenStreetMap/Nominatim,
sobory.ru, RGO/visit-mariel, 2026-07-28). Phạm vi Mari El lat ~55,8–57,4; lon ~45,6–50,3 — tất
cả toạ độ trong phạm vi, KHÔNG đảo lat/lon:
  Благовещенский собор 56.632793,47.904447 (ru.wiki); Воскресенский собор 56.636994,47.902788
  (ул.Вознесенская 45); Троицкая церковь 56.635557,47.902177 (ул.Вознесенская 53); Собор
  Вознесения 56.639492,47.903431 (ул.Вознесенская 31); Мироносицкий монастырь 56.71222,48.11944
  (ru.wiki, Ежово); Благовещенская башня 56.63384,47.90271 (площадь Республики); Йошкин кот
  56.631314,47.888584 (Ленинский пр.1); Грейс Келли & Ренье 56.633081,47.908841 (OSM, наб.Брюгге);
  Рембрандт 56.631216,47.899012 (OSM, наб.Амстердам); пл.Оболенского-Ноготкова 56.631568,47.886924
  (OSM); Патриаршая площадь 56.636908,47.906977 (OSM); театр кукол 56.637024,47.908544 (OSM,
  Царьградский пр.35); театр Шкетана 56.631729,47.891538 (ru.wiki, пл.Ленина 2); Музей истории
  города 56.638084,47.902445 (OSM, ул.Вознесенская 39); Дворец бракосочетаний 56.632846,47.909085
  (OSM, наб.Брюгге 5); Морской Глаз 56.1625,48.7601 (ru.wiki); Яльчик 56.0111,48.4083 (ru.wiki);
  Зелёный ключ 56.154892,48.425653 (OSM spring); Дуб Пугачёва 56.13472,48.46833 (ru.wiki);
  Табашинское/Зрыв 56.981482,47.805194 (OSM lake, Оршанский р-н); Кленовая Гора 56.13389,48.42667
  (ru.wiki); Кичиер 56.0695,48.3465 (ru.wiki); Нолькин камень 56.852,49.035 (ru.wiki, Сернурский р-н).

GHI CHÚ: đã BỎ QUA/không thêm các đối tượng không xác minh được toạ độ tin cậy hoặc dễ trùng: cầu
Театральный мост (không nổi bật), Национальная художественная галерея (đặt chung vị trí với
площадь Оболенского-Ноготкова nên gộp vào bản ghi quảng trường để tránh trùng toạ độ), một số
tượng nhỏ khác ở trung tâm. KHÔNG bịa toạ độ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_mari-el_20260728_220909.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "mari-el"
REGION_NAME_VI = "Cộng hoà Mari El"
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


def city_practical(hours, ticket, duration, best_time, tips):
    return {"hours_vi": hours, "ticket_vi": ticket, "duration_vi": duration,
            "best_time_vi": best_time, "tips_vi": tips}


def nature_practical(duration, best_time, tips):
    return {
        "hours_vi": "Đối tượng thiên nhiên ngoài trời, tham quan ban ngày; không có giờ cố định.",
        "ticket_vi": "Thường không thu vé; nếu thuộc vườn quốc gia Mari Chodra có thể cần đăng ký/phí dịch vụ.",
        "duration_vi": duration,
        "best_time_vi": best_time,
        "tips_vi": tips,
    }


RECORDS = []

# ============================ NHÀ THỜ / TU VIỆN (church) ============================

# 1) Благовещенский собор -----------------------------------------------------------
RECORDS.append(rec(
    "blagoveshchensky-cathedral-yoshkar-ola",
    "Nhà thờ chính toà Truyền Tin (Blagoveshchensky sobor)",
    "Благовещенский собор",
    "Annunciation Cathedral",
    ["church"],
    56.632793, 47.904447,
    "Площадь Республики и Пресвятой Девы Марии, trung tâm Yoshkar-Ola, Cộng hòa Mari El",
    "Nhà thờ chính toà Truyền Tin là ngôi thánh đường lớn và bề thế nhất Yoshkar-Ola, dựng năm 2010–2016 theo phong cách phỏng nhà thờ Nga cổ. Với những tháp nhọn trắng - xanh và mái vòm dát vàng bên quảng trường trung tâm, đây là biểu tượng tôn giáo mới của thành phố.",
    "Toạ lạc trên Quảng trường Cộng hòa và Đức Mẹ Đồng Trinh ngay tim Yoshkar-Ola, Благовещенский собор là nhà thờ chính toà của giáo phận Yoshkar-Ola. Dù mới được xây dựng trong các năm 2010–2016 và khánh thành năm 2016, công trình cố ý phỏng theo hình dáng những thánh đường Nga cổ điển - đặc biệt gợi nhớ nhà thờ Truyền Tin trong điện Kremlin Moskva - với khối tường trắng, các tháp nhọn màu lam điểm sao vàng và mái vòm hành củ dát vàng lấp lánh. Bên trong là không gian rộng, tranh thánh và bích hoạ theo truyền thống Chính Thống giáo. Nằm cùng quảng trường với tháp đồng hồ Blagoveshchenskaya và đối diện các bờ kè phỏng châu Âu, nhà thờ là một mắt xích quan trọng trong quần thể trung tâm 'Yoshkar-Ola thu nhỏ', nơi du khách thường dừng chân chụp ảnh và tìm hiểu diện mạo tôn giáo - kiến trúc đặc trưng của thành phố.",
    [
        "Nhà thờ chính toà lớn nhất Yoshkar-Ola, xây 2010–2016, phỏng theo thánh đường Nga cổ.",
        "Tháp nhọn trắng - lam điểm sao và mái vòm dát vàng nổi bật giữa quảng trường trung tâm.",
        "Nằm cùng quần thể với tháp đồng hồ Blagoveshchenskaya và các bờ kè phỏng châu Âu.",
    ],
    city_practical(
        "Mở cửa hằng ngày theo giờ lễ (thường sáng đến tối); nên tránh giờ hành lễ nếu chỉ tham quan.",
        "Miễn phí (là nơi thờ tự đang hoạt động).",
        "20–40 phút.",
        "Quanh năm; đẹp khi lên đèn buổi tối cùng quảng trường.",
        "Ăn mặc kín đáo, nữ nên có khăn trùm đầu; kết hợp tham quan tháp Blagoveshchenskaya và Bờ kè Bruges ngay gần.",
    ),
    [
        {"title": "Wikipedia (RU) — Благовещенский собор (Йошкар-Ола)", "url": "https://ru.wikipedia.org/wiki/%D0%91%D0%BB%D0%B0%D0%B3%D0%BE%D0%B2%D0%B5%D1%89%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80_(%D0%99%D0%BE%D1%88%D0%BA%D0%B0%D1%80-%D0%9E%D0%BB%D0%B0)"},
        {"title": "Sobory.ru — Кафедральный собор Благовещения Пресвятой Богородицы", "url": "https://sobory.ru/article/?object=21228"},
    ],
    ["church", "cathedral", "city", "architecture", "orthodox", "landmark"],
    maps_text("Благовещенский собор", "Йошкар-Ола", "Annunciation Cathedral", "Yoshkar-Ola", 56.632793, 47.904447),
))

# 2) Воскресенский собор ------------------------------------------------------------
RECORDS.append(rec(
    "voskresensky-cathedral-yoshkar-ola",
    "Nhà thờ Phục Sinh (Voskresensky sobor)",
    "Воскресенский собор",
    "Resurrection Cathedral",
    ["church"],
    56.636994, 47.902788,
    "ул. Вознесенская, 45, Yoshkar-Ola, Cộng hòa Mari El",
    "Nhà thờ Phục Sinh là thánh đường Chính Thống giáo màu trắng - vàng bên sông Malaya Kokshaga, được dựng lại năm 2008–2010 trên nền một nhà thờ cổ từng bị phá huỷ thời Xô Viết. Mặt tiền thanh thoát và tháp chuông cao khiến nó dễ nhận ra trong cụm nhà thờ trung tâm thành phố.",
    "Ngôi Воскресенский собор ngày nay được xây dựng lại trong các năm 2008–2010 và cung hiến năm 2010, tái hiện một nhà thờ Phục Sinh lịch sử của Tsaryovokokshaysk từng bị dỡ bỏ dưới thời Xô Viết. Nằm trên phố Voznesenskaya bên hữu ngạn sông Malaya Kokshaga, công trình mang khối tường trắng, các đường gờ trang trí và tháp chuông vươn cao, kết những mái vòm hành củ dát vàng. Đây là một trong ba nhà thờ cổ - phục dựng nằm gần nhau trên cùng con phố (cùng Troitskaya và nhà thờ Vознесения), tạo thành một 'trục hành hương' nhỏ ở lõi lịch sử thành phố. Với vị trí sát bờ sông và trung tâm, nhà thờ vừa là nơi thờ tự đang hoạt động, vừa là điểm ngắm kiến trúc thuận tiện cho du khách khi dạo bộ khám phá Yoshkar-Ola.",
    [
        "Dựng lại 2008–2010 trên dấu tích một nhà thờ Phục Sinh cổ bị phá thời Xô Viết.",
        "Tường trắng, tháp chuông cao, mái vòm dát vàng bên sông Malaya Kokshaga.",
        "Cùng cụm với Troitskaya và nhà thờ Vознесения trên phố Voznesenskaya.",
    ],
    city_practical(
        "Mở cửa theo giờ lễ hằng ngày.",
        "Miễn phí.",
        "15–30 phút.",
        "Quanh năm.",
        "Ăn mặc kín đáo; dễ ghép chung một vòng dạo bộ với hai nhà thờ lân cận và Bờ kè Bruges.",
    ),
    [
        {"title": "Sobory.ru — Собор Воскресения Христова (новый), Йошкар-Ола", "url": "https://sobory.ru/article/?object=17966"},
        {"title": "Культурный туризм — Воскресенский собор (Йошкар-Ола)", "url": "https://culttourism.ru/mari-el/yoshkar-ola/yoshkar-ola_voskresenskiy_sobor.html"},
    ],
    ["church", "cathedral", "city", "architecture", "orthodox", "riverside"],
    maps_text("Воскресенский собор", "Йошкар-Ола", "Resurrection Cathedral", "Yoshkar-Ola", 56.636994, 47.902788),
))

# 3) Троицкая церковь ---------------------------------------------------------------
RECORDS.append(rec(
    "troitskaya-church-yoshkar-ola",
    "Nhà thờ Chúa Ba Ngôi (Troitskaya tserkov)",
    "Троицкая церковь",
    "Holy Trinity Church",
    ["church"],
    56.635557, 47.902177,
    "ул. Вознесенская, 53, Yoshkar-Ola, Cộng hòa Mari El",
    "Nhà thờ Chúa Ba Ngôi là một trong những công trình tôn giáo lâu đời nhất Yoshkar-Ola, có gốc từ thế kỷ 17–18. Bị phá hỏng thời Xô Viết và được phục dựng, nay là ngôi nhà thờ gạch trắng duyên dáng nhắc nhớ thời kỳ Tsaryovokokshaysk.",
    "Troitskaya (Chúa Ba Ngôi) là một trong những nhà thờ cổ nhất trên đất Yoshkar-Ola: sử liệu nhắc tới ngôi nhà thờ gỗ đầu tiên từ giữa thế kỷ 17, còn tầng đá đầu tiên của nhà thờ hiện nay dựng vào năm 1736. Trải qua thời Xô Viết bị đóng cửa và hư hại nặng, công trình được phục dựng và trả lại cho giáo hội, khôi phục dáng vẻ nhà thờ Nga truyền thống với tường trắng, mái vòm và tháp chuông. Nằm trên phố Voznesenskaya cạnh nhà thờ Phục Sinh và nhà thờ Vознесения, Troitskaya góp phần tạo nên cụm di sản tôn giáo ở lõi lịch sử thành phố - nơi từng là trung tâm của Tsaryovokokshaysk xưa. Đây là điểm dừng ý nghĩa cho ai muốn cảm nhận chiều sâu lịch sử phía sau vẻ ngoài 'châu Âu thu nhỏ' hiện đại của Yoshkar-Ola.",
    [
        "Một trong những nhà thờ lâu đời nhất Yoshkar-Ola, gốc gỗ thế kỷ 17, tầng đá từ 1736.",
        "Bị đóng cửa, hư hại thời Xô Viết rồi được phục dựng theo lối Nga truyền thống.",
        "Nằm trong cụm ba nhà thờ cổ trên phố Voznesenskaya ở lõi lịch sử thành phố.",
    ],
    city_practical(
        "Mở cửa theo giờ lễ hằng ngày.",
        "Miễn phí.",
        "15–30 phút.",
        "Quanh năm.",
        "Ăn mặc kín đáo; kết hợp cùng nhà thờ Phục Sinh và nhà thờ Vознесения liền kề.",
    ),
    [
        {"title": "Sobory.ru — Церковь Троицы Живоначальной, Йошкар-Ола", "url": "https://sobory.ru/article/?object=05000"},
        {"title": "Приход — Церковь Пресвятой Троицы (Йошкар-Ола)", "url": "https://troitsky.cerkov.ru/"},
    ],
    ["church", "history", "city", "architecture", "orthodox", "heritage"],
    maps_text("Троицкая церковь", "Йошкар-Ола", "Holy Trinity Church", "Yoshkar-Ola", 56.635557, 47.902177),
))

# 4) Собор Вознесения Господня ------------------------------------------------------
RECORDS.append(rec(
    "voznesenskaya-church-yoshkar-ola",
    "Nhà thờ Chúa Thăng Thiên (Voznesensky sobor)",
    "Собор Вознесения Господня",
    "Ascension Cathedral",
    ["church"],
    56.639492, 47.903431,
    "ул. Вознесенская, 31, Yoshkar-Ola, Cộng hòa Mari El",
    "Nhà thờ Chúa Thăng Thiên là một trong số ít công trình đá thế kỷ 18 còn nguyên bản ở Yoshkar-Ola, dựng năm 1756 bằng tiền công đức của thương nhân Pchelin. Đây là mẫu kiến trúc Nga 'bát giác trên tứ giác' quý giá của thành phố.",
    "Được thương nhân Ivan Pchelin bỏ tiền xây năm 1756, Собор Вознесения Господня (nhà thờ Chúa Thăng Thiên) là một trong những di tích kiến trúc thế kỷ 18 hiếm hoi còn giữ được dáng nguyên bản ở Yoshkar-Ola. Công trình theo kiểu 'vосьмерик на четверике' - khối bát giác đặt trên đế tứ giác - đặc trưng của kiến trúc Nga đương thời, với tường trắng, cửa sổ viền chỉ và tháp chuông. Sau thời gian bị trưng dụng dưới chế độ Xô Viết, nhà thờ được trả lại cho giáo hội năm 1992 và mở lại sau trùng tu năm 1995. Nằm trên phố Voznesenskaya cùng cụm Troitskaya và nhà thờ Phục Sinh, đây là điểm nhấn cho những ai quan tâm tới kiến trúc tôn giáo cổ thật sự (khác với nhiều công trình phỏng cổ mới xây trong trung tâm), đồng thời rất tiện ghép vào một vòng dạo bộ ven sông.",
    [
        "Dựng năm 1756 bằng tiền thương nhân Pchelin - di tích đá thế kỷ 18 hiếm còn nguyên bản.",
        "Kiến trúc Nga 'bát giác trên tứ giác' (восьмерик на четверике) đặc trưng.",
        "Trả lại giáo hội 1992, trùng tu và mở lại 1995; nằm trong cụm nhà thờ phố Voznesenskaya.",
    ],
    city_practical(
        "Mở cửa theo giờ lễ hằng ngày.",
        "Miễn phí.",
        "15–30 phút.",
        "Quanh năm.",
        "Ăn mặc kín đáo; đi cùng hai nhà thờ lân cận để thấy trọn cụm di sản tôn giáo.",
    ),
    [
        {"title": "Sobory.ru — Собор Вознесения Господня, Йошкар-Ола", "url": "https://sobory.ru/article/?object=04977"},
        {"title": "Приход — Собор Вознесения Христова (Йошкар-Ола)", "url": "https://voznesenie-ola.cerkov.ru/"},
    ],
    ["church", "history", "18th-century", "architecture", "orthodox", "heritage"],
    maps_org("https://yandex.com/maps/org/sobor_vozneseniya_gospodnya/1144829691/", "Ascension Cathedral", "Yoshkar-Ola"),
))

# 5) Мироносицкий монастырь (Ежово) -------------------------------------------------
RECORDS.append(rec(
    "mironositsky-monastery-ezhovo",
    "Tu viện Mironositskaya (Ежово)",
    "Мироносицкий монастырь",
    "Mironositsky Convent",
    ["church"],
    56.71222, 48.11944,
    "làng Ежово, huyện Medvedevsky, cách Yoshkar-Ola ~15 km, Cộng hòa Mari El",
    "Tu viện Mironositskaya ở làng Ежово là một trong những tu viện lâu đời và được sùng kính nhất Mari El, lập từ năm 1647 quanh nơi hiển linh một thánh tượng. Ngày nay là nữ đan viện với quần thể tường trắng, tháp chuông và nhà thờ đá, điểm hành hương chính của vùng.",
    "Ежово-Mironositsky là tu viện được lập năm 1647 tại làng Ежово, huyện Medvedevsky, cách thủ phủ Yoshkar-Ola chừng 15 km, gắn với truyền thuyết về việc tìm thấy một thánh tượng các bà Mang Mộc Dược (Жёны-мироносицы) - từ đó có tên gọi. Qua nhiều thế kỷ, nơi đây trở thành trung tâm tôn giáo quan trọng của cả vùng; sau thời gian bị đóng cửa và tàn phá dưới chế độ Xô Viết, tu viện được khôi phục và nay hoạt động như một nữ đan viện. Quần thể gồm tường bao trắng, tháp chuông, các nhà thờ đá và khu vườn yên tĩnh giữa cảnh quê. Đây là điểm hành hương chính của người Chính Thống giáo ở Mari El, đồng thời là chuyến đi trong ngày dễ chịu từ Yoshkar-Ola cho du khách muốn tìm không gian tĩnh lặng, tách khỏi nhịp phố. Khách viếng được yêu cầu ăn mặc kín đáo và giữ thái độ trang nghiêm.",
    [
        "Tu viện lập năm 1647 quanh nơi hiển linh thánh tượng 'Жёны-мироносицы'.",
        "Nay là nữ đan viện với tường trắng, tháp chuông, nhà thờ đá - điểm hành hương chính của vùng.",
        "Cách Yoshkar-Ola ~15 km, hợp làm chuyến đi trong ngày tìm không gian tĩnh lặng.",
    ],
    city_practical(
        "Mở cửa đón khách hành hương hằng ngày theo giờ tu viện.",
        "Miễn phí (có thể công đức tuỳ tâm).",
        "1–1,5 giờ.",
        "Cuối xuân đến đầu thu; các dịp lễ Chính Thống giáo đông khách hành hương.",
        "Ăn mặc kín đáo (nữ nên có khăn trùm đầu và váy dài); giữ yên lặng; đi ô tô/taxi từ Yoshkar-Ola thuận tiện nhất.",
    ),
    [
        {"title": "Wikipedia (RU) — Мироносицкий монастырь", "url": "https://ru.wikipedia.org/wiki/%D0%9C%D0%B8%D1%80%D0%BE%D0%BD%D0%BE%D1%81%D0%B8%D1%86%D0%BA%D0%B8%D0%B9_%D0%BC%D0%BE%D0%BD%D0%B0%D1%81%D1%82%D1%8B%D1%80%D1%8C"},
        {"title": "Sobory.ru — Ежово, Мироносицкий женский монастырь", "url": "https://sobory.ru/article/?object=26341"},
    ],
    ["monastery", "pilgrimage", "history", "orthodox", "daytrip", "countryside"],
    maps_text("Мироносицкий монастырь", "Ежово Марий Эл", "Mironositsky Convent", "Ezhovo Mari El", 56.71222, 48.11944),
))

# ============================ TƯỢNG ĐÀI / THÁP (monument) ============================

# 6) Благовещенская башня -----------------------------------------------------------
RECORDS.append(rec(
    "blagoveshchenskaya-tower-yoshkar-ola",
    "Tháp Blagoveshchenskaya (đồng hồ куранты)",
    "Благовещенская башня",
    "Blagoveshchenskaya Tower",
    ["monument"],
    56.63384, 47.90271,
    "Площадь Республики и Пресвятой Девы Марии, 1, Yoshkar-Ola, Cộng hòa Mari El",
    "Tháp Blagoveshchenskaya cao khoảng 55 m là 'chuông đồng hồ' của Yoshkar-Ola: một phiên bản thu nhỏ của tháp Spasskaya điện Kremlin Moskva, với bộ đồng hồ куранты gõ giờ. Khánh thành năm 2007, tháp là điểm nhấn của Quảng trường Cộng hòa và Đức Mẹ Đồng Trinh.",
    "Sừng sững trên Quảng trường Cộng hòa và Đức Mẹ Đồng Trinh, Благовещенская башня cao chừng 55 m là một trong những biểu tượng dễ nhận nhất của Yoshkar-Ola. Khánh thành mùa hè năm 2007 theo thiết kế của viện 'Мариискгражданпроект', tháp mô phỏng gần như y hệt tháp Spasskaya của điện Kremlin Moskva, kể cả bộ đồng hồ куранты gõ giờ ngân vang trên quảng trường. Cùng nhà thờ chính toà Truyền Tin và các dãy nhà phỏng châu Âu bao quanh, tháp góp phần tạo nên khung cảnh 'Moskva và châu Âu thu nhỏ' rất riêng của thành phố - một dụng ý quy hoạch biến trung tâm Yoshkar-Ola thành 'bảo tàng kiến trúc trích dẫn' ngoài trời. Đây là phông nền chụp ảnh yêu thích, đẹp nhất khi lên đèn buổi tối, và là mốc định vị tiện lợi để bắt đầu vòng dạo trung tâm.",
    [
        "Tháp đồng hồ cao ~55 m, phiên bản thu nhỏ của tháp Spasskaya điện Kremlin Moskva.",
        "Bộ đồng hồ куранты gõ giờ; khánh thành năm 2007, biểu tượng của Quảng trường Cộng hòa.",
        "Điểm chụp ảnh nổi bật, lung linh khi lên đèn, mốc định vị của cụm trung tâm.",
    ],
    city_practical(
        "Không gian ngoài trời, ngắm tự do mọi lúc.",
        "Miễn phí (ngắm bên ngoài).",
        "15–20 phút.",
        "Buổi tối khi tháp và quảng trường lên đèn.",
        "Kết hợp cùng nhà thờ chính toà Truyền Tin và Bờ kè Bruges liền kề trong một buổi dạo.",
    ),
    [
        {"title": "Wikivoyage (RU) — Йошкар-Ола", "url": "https://ru.wikivoyage.org/wiki/%D0%99%D0%BE%D1%88%D0%BA%D0%B0%D1%80-%D0%9E%D0%BB%D0%B0"},
        {"title": "Туристический портал Марий Эл — Патриаршая площадь / центр", "url": "https://visit-mariel.ru/routs/sights/patriarshaya-ploshchad-v-yoshkar-ole/"},
    ],
    ["tower", "clock", "city", "architecture", "landmark", "photo-spot"],
    maps_text("Благовещенская башня", "Йошкар-Ола", "Blagoveshchenskaya Tower", "Yoshkar-Ola", 56.63384, 47.90271),
))

# 7) Памятник Йошкин кот ------------------------------------------------------------
RECORDS.append(rec(
    "yoshkin-cat-monument",
    "Tượng 'Yoshkin Kot' (Chú mèo Yoshkar)",
    "Памятник Йошкин кот",
    "Yoshkin Cat Monument",
    ["monument"],
    56.631314, 47.888584,
    "Ленинский проспект, 1 (trước Đại học Quốc gia Mari), Yoshkar-Ola, Cộng hòa Mari El",
    "'Yoshkin Kot' là bức tượng đồng vui nhộn hình chú mèo ngồi vắt vẻo trên ghế băng, chơi chữ từ thành ngữ Nga 'ёшкин кот' và tên thành phố Yoshkar-Ola. Đặt năm 2011 trước Đại học Mari, đây là điểm 'sờ mũi lấy may' và chụp ảnh được yêu thích nhất phố.",
    "Đặt vào tháng 6/2011 trong khuôn viên nhỏ trước Đại học Quốc gia Mari, 'Йошкин кот' nhanh chóng thành một trong những tượng đường phố được chụp ảnh nhiều nhất Yoshkar-Ola. Cái tên là lối chơi chữ tinh nghịch: thành ngữ dân gian Nga 'ёшкин кот' (một câu cảm thán vui) trùng âm với tên thành phố Yoshkar-Ola. Tác phẩm bằng đồng nặng khoảng 150 kg, đúc ở Kazan, tạo hình một chú mèo ngồi ngả ngớn trên chiếc ghế băng, vẻ mặt tinh quái. Ý tưởng do nhà bảo trợ Sergey Paramonov khởi xướng và tặng thành phố. Theo thói quen đã thành 'tục lệ', người dân và du khách thường xoa mũi (và đôi khi cả bàn chân) chú mèo để cầu may - khiến những chỗ ấy bóng loáng. Nhỏ nhắn, hài hước và dễ thương, đây là điểm dừng nhẹ nhàng, hợp chụp ảnh khi dạo trung tâm.",
    [
        "Tượng đồng chú mèo ngồi trên ghế băng, chơi chữ 'ёшкин кот' với tên Yoshkar-Ola.",
        "Đặt năm 2011 trước Đại học Mari; đúc ở Kazan, nặng ~150 kg.",
        "Tục xoa mũi mèo lấy may khiến bức tượng thành điểm chụp ảnh vui nhộn.",
    ],
    city_practical(
        "Không gian ngoài trời, tự do mọi lúc.",
        "Miễn phí.",
        "10–15 phút.",
        "Quanh năm.",
        "Xoa mũi mèo 'lấy may' theo thói quen địa phương; kết hợp dạo Bờ kè Bruges và trung tâm.",
    ),
    [
        {"title": "Wikipedia (RU) — Памятники Йошкар-Олы", "url": "https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D0%BD%D0%B8%D0%BA%D0%B8_%D0%99%D0%BE%D1%88%D0%BA%D0%B0%D1%80-%D0%9E%D0%BB%D1%8B"},
        {"title": "ТИЦ Йошкар-Олы — Йошкин кот", "url": "https://i-ola-visit.ru/articles/chto-posmotret/dostoprimechatelnosti/skulptury/yoshkin-kot/"},
    ],
    ["monument", "sculpture", "fun", "city", "photo-spot", "free"],
    maps_text("Памятник Йошкин кот", "Йошкар-Ола", "Yoshkin Cat Monument", "Yoshkar-Ola", 56.631314, 47.888584),
))

# 8) Памятник Грейс Келли и князю Ренье III -----------------------------------------
RECORDS.append(rec(
    "grace-kelly-rainier-monument",
    "Tượng đài Grace Kelly và Vương công Rainier III",
    "Памятник Грейс Келли и князю Монако Ренье III",
    "Monument to Grace Kelly and Prince Rainier III",
    ["monument"],
    56.633081, 47.908841,
    "Набережная Брюгге (cạnh Cung điện hôn nhân), Yoshkar-Ola, Cộng hòa Mari El",
    "Bức tượng đồng khắc hoạ 'đám cưới thế kỷ' của minh tinh Grace Kelly và Vương công Monaco Rainier III, đặt năm 2012 trên Bờ kè Bruges ngay cạnh Cung điện hôn nhân. Đây là biểu tượng lãng mạn gắn với chủ đề tình yêu - hôn nhân của khu bờ kè châu Âu.",
    "Khánh thành ngày 27/4/2012 trên Bờ kè Bruges, ngay bên Cung điện hôn nhân (замок ЗАГС) mới xây, tượng đài khắc hoạ cặp đôi nổi tiếng: nữ minh tinh Hollywood Grace Kelly và Vương công Monaco Rainier III, với ý tưởng lấy cảm hứng từ 'đám cưới thế kỷ' năm 1956 của họ. Tác phẩm bằng đồng do nhà điêu khắc Andrey Kovalchuk thực hiện, đặt ở vị trí đắc địa nơi các đôi tân hôn bước ra sau khi đăng ký kết hôn - biến nơi đây thành điểm chụp ảnh cưới và 'check-in' lãng mạn bậc nhất thành phố. Cùng với kiến trúc phỏng châu Âu của bờ kè và toà lâu đài ЗАГС, bức tượng củng cố chủ đề tình yêu - hôn nhân mà chính quyền địa phương dụng công gây dựng cho không gian trung tâm 'châu Âu thu nhỏ' của Yoshkar-Ola.",
    [
        "Tượng đồng về 'đám cưới thế kỷ' của Grace Kelly và Vương công Rainier III, đặt năm 2012.",
        "Đứng ngay bên Cung điện hôn nhân trên Bờ kè Bruges - điểm chụp ảnh cưới nổi tiếng.",
        "Tác phẩm của nhà điêu khắc Andrey Kovalchuk, tô đậm chủ đề tình yêu - hôn nhân của khu bờ kè.",
    ],
    city_practical(
        "Không gian ngoài trời, tự do mọi lúc.",
        "Miễn phí.",
        "10–15 phút.",
        "Chiều mát và buổi tối khi bờ kè lên đèn.",
        "Kết hợp cùng Cung điện hôn nhân, Bờ kè Bruges và tượng Rembrandt ở gần.",
    ),
    [
        {"title": "Interfax — Памятник Грейс Келли и князю Ренье появился в Йошкар-Оле", "url": "https://www.interfax-russia.ru/volga/news/pamyatnik-greys-kelli-i-knyazyu-rene-poyavilsya-v-yoshkar-ole"},
        {"title": "OpenStreetMap — Грейс Келли и князю Монако Ренье III", "url": "https://www.openstreetmap.org/search?query=%D0%93%D1%80%D0%B5%D0%B9%D1%81%20%D0%9A%D0%B5%D0%BB%D0%BB%D0%B8%20%D0%99%D0%BE%D1%88%D0%BA%D0%B0%D1%80-%D0%9E%D0%BB%D0%B0"},
    ],
    ["monument", "sculpture", "romance", "embankment", "city", "photo-spot"],
    maps_org("https://yandex.ru/maps/org/greys_kelli_i_knyaz_monako_renye_iii/123563131311/", "Grace Kelly and Prince Rainier III Monument", "Yoshkar-Ola"),
))

# 9) Памятник Рембрандту ------------------------------------------------------------
RECORDS.append(rec(
    "rembrandt-monument-yoshkar-ola",
    "Tượng đài danh hoạ Rembrandt",
    "Памятник Рембрандту",
    "Monument to Rembrandt",
    ["monument"],
    56.631216, 47.899012,
    "Набережная Амстердам, ven sông Malaya Kokshaga, Yoshkar-Ola, Cộng hòa Mari El",
    "Bức tượng đồng danh hoạ Hà Lan Rembrandt van Rijn đứng trên Bờ kè Amsterdam - một trong những bờ kè phỏng châu Âu của Yoshkar-Ola. Đặt năm 2013, tượng thể hiện tham vọng 'mang châu Âu về Volga' của thành phố.",
    "Đặt năm 2013 trên Bờ kè Amsterdam ven sông Malaya Kokshaga, tượng đài Rembrandt van Rijn - bậc thầy hội hoạ Hà Lan thế kỷ 17 - là một trong những tượng 'nhân vật châu Âu' mà Yoshkar-Ola cho dựng để củng cố hình ảnh 'châu Âu thu nhỏ'. Tác phẩm bằng đồng (nặng khoảng một tấn, đặt trên bệ đá granite) do nhà điêu khắc Andrey Kovalchuk thực hiện, khắc hoạ danh hoạ trong tư thế trầm ngâm. Việc chọn Rembrandt cho một bờ kè mang tên Amsterdam là dụng ý gắn kết chủ đề: những dãy nhà phỏng kiến trúc Hà Lan - Flanders dọc sông, cùng các tượng đài và tên gọi 'Bruges', 'Amsterdam', tạo nên một 'châu Âu trích dẫn' độc đáo. Bức tượng là điểm dừng thú vị khi dạo dọc bờ sông, nơi du khách vừa chụp ảnh vừa 'giải mã' ý tưởng quy hoạch khác thường của thành phố.",
    [
        "Tượng đồng danh hoạ Hà Lan Rembrandt, đặt năm 2013 trên Bờ kè Amsterdam.",
        "Tác phẩm của Andrey Kovalchuk, nặng ~1 tấn, trên bệ đá granite.",
        "Thể hiện dụng ý 'mang châu Âu về Volga' của trung tâm Yoshkar-Ola.",
    ],
    city_practical(
        "Không gian ngoài trời, tự do mọi lúc.",
        "Miễn phí.",
        "10 phút.",
        "Chiều mát và buổi tối khi bờ kè lên đèn.",
        "Kết hợp dạo dọc Bờ kè Amsterdam và Bờ kè Bruges cùng các tượng đài lân cận.",
    ),
    [
        {"title": "РИА Новости — В Йошкар-Оле открыли памятник Рембрандту", "url": "https://ria.ru/20131102/974371010.html"},
        {"title": "OpenStreetMap — Памятник Рембрандту ван Рейну", "url": "https://www.openstreetmap.org/search?query=%D0%A0%D0%B5%D0%BC%D0%B1%D1%80%D0%B0%D0%BD%D0%B4%D1%82%D1%83%20%D0%99%D0%BE%D1%88%D0%BA%D0%B0%D1%80-%D0%9E%D0%BB%D0%B0"},
    ],
    ["monument", "sculpture", "embankment", "european", "city", "photo-spot"],
    maps_text("Памятник Рембрандту", "Йошкар-Ола", "Monument to Rembrandt", "Yoshkar-Ola", 56.631216, 47.899012),
))

# ============================ QUẢNG TRƯỜNG (square_street) ============================

# 10) Площадь Оболенского-Ноготкова -------------------------------------------------
RECORDS.append(rec(
    "obolensky-nogotkov-square",
    "Quảng trường Obolensky-Nogotkov",
    "Площадь Оболенского-Ноготкова",
    "Obolensky-Nogotkov Square",
    ["square_street"],
    56.631568, 47.886924,
    "Trung tâm Yoshkar-Ola, bên Bờ kè Bruges (khu Национальной художественной галереи), Cộng hòa Mari El",
    "Quảng trường Obolensky-Nogotkov là quảng trường trung tâm khánh thành năm 2007, mang tên vị voevoda sáng lập thành phố. Điểm nhấn là toà Bảo tàng Mỹ thuật với chiếc đồng hồ cơ khí có tượng con lừa chở icon Đức Mẹ 'diễu hành' mỗi giờ, cùng tượng voevoda cưỡi ngựa.",
    "Hình thành năm 2007 sau khi cải tạo cả cụm kiến trúc bao quanh, Площадь Оболенского-Ноготкова được đặt theo tên voevoda Ivan Andreyevich Obolensky-Nogotkov - người sáng lập Tsaryovokokshaysk (tên cũ của Yoshkar-Ola). Giữa quảng trường là tượng đài vị voevoda cưỡi ngựa, còn 'ngôi sao' thu hút du khách là toà Национальная художественная галерея (Bảo tàng - phòng trưng bày Mỹ thuật) xây theo mô-típ dân tộc Mari. Trên toà nhà này gắn một chiếc đồng hồ cơ khí độc đáo: mỗi giờ, một cánh cửa mở ra và tượng con lừa chở icon Đức Mẹ (mô típ 'Chúa vào thành Jerusalem') từ từ 'diễu' quanh ban công rồi khuất vào trong - màn trình diễn nhỏ khiến đám đông thích thú chờ xem. Nằm ngay bên Bờ kè Bruges và sông Malaya Kokshaga, quảng trường là một trong những không gian 'sống ảo' và giàu chi tiết nhất trung tâm, lý tưởng để mở đầu hành trình khám phá 'Yoshkar-Ola thu nhỏ'.",
    [
        "Quảng trường trung tâm (2007) mang tên voevoda Obolensky-Nogotkov, người lập thành phố.",
        "Đồng hồ cơ khí trên Bảo tàng Mỹ thuật: tượng con lừa chở icon Đức Mẹ 'diễu' mỗi giờ.",
        "Có tượng voevoda cưỡi ngựa; nằm ngay bên Bờ kè Bruges, rất hợp chụp ảnh.",
    ],
    city_practical(
        "Không gian mở, dạo tự do mọi lúc; canh giờ chẵn để xem đồng hồ có tượng lừa hoạt động.",
        "Miễn phí (vào phòng trưng bày Mỹ thuật mua vé riêng).",
        "20–40 phút.",
        "Ban ngày để xem đồng hồ; buổi tối khi lên đèn.",
        "Đứng trước toà Bảo tàng Mỹ thuật vào đầu giờ để xem màn 'diễu hành' của tượng lừa và icon.",
    ),
    [
        {"title": "Туристический портал Марий Эл — Национальная художественная галерея", "url": "https://visit-mariel.ru/routs/sights/natsionalnaya-khudozhestvennaya-galereya/"},
        {"title": "ТИЦ Йошкар-Олы — Площадь Оболенского-Ноготкова", "url": "https://i-ola-visit.ru/articles/sobiraemsya-v-dorogu/o-gorode/top10/ploschad-obolenskogo-nogotkova/"},
    ],
    ["square", "clock", "city-center", "architecture", "landmark", "photo-spot"],
    maps_text("Площадь Оболенского-Ноготкова", "Йошкар-Ола", "Obolensky-Nogotkov Square", "Yoshkar-Ola", 56.631568, 47.886924),
))

# 11) Патриаршая площадь ------------------------------------------------------------
RECORDS.append(rec(
    "patriarch-square-yoshkar-ola",
    "Quảng trường Thượng Phụ (Patriarshaya ploshchad)",
    "Патриаршая площадь",
    "Patriarch Square",
    ["square_street"],
    56.636908, 47.906977,
    "Царьградский проспект, trung tâm Yoshkar-Ola, Cộng hòa Mari El",
    "Quảng trường Thượng Phụ là một trong những quảng trường trẻ và 'ăn ảnh' của Yoshkar-Ola, mang chủ đề tôn giáo - lịch sử. Bao quanh là toà Nhà hát Múa rối như lâu đài, tượng đài Thượng phụ Aleksy II và các công trình phỏng kiến trúc Nga - châu Âu.",
    "Патриаршая площадь (Quảng trường Thượng Phụ) là một trong những không gian công cộng mới của Yoshkar-Ola, nằm bên phố Царьградский. Quảng trường được đặt tên và trang trí theo chủ đề tôn giáo - lịch sử Chính Thống giáo: nổi bật là tượng đài Thượng phụ Moskva Aleksy II, cùng những cụm phù điêu và công trình phỏng kiến trúc Nga - Byzantine. Bao quanh quảng trường là toà Nhà hát Múa rối bằng gạch đỏ - trắng trông như một lâu đài Đức, các dãy nhà phỏng châu Âu và lối đi lát đá. Với nhiều chi tiết trang trí, tháp nhọn và tượng đài quây quần trong một không gian nhỏ, đây là điểm chụp ảnh được ưa chuộng và là mảnh ghép quan trọng trong bức tranh 'thành phố trích dẫn kiến trúc' của Yoshkar-Ola. Quảng trường tiện ghép cùng cụm Bờ kè Bruges, nhà thờ chính toà Truyền Tin và tháp đồng hồ trong một vòng dạo bộ trung tâm.",
    [
        "Quảng trường chủ đề tôn giáo - lịch sử với tượng đài Thượng phụ Aleksy II.",
        "Bao quanh có Nhà hát Múa rối như lâu đài và nhiều công trình phỏng kiến trúc Nga - châu Âu.",
        "Không gian nhỏ nhưng nhiều chi tiết, tháp nhọn - điểm chụp ảnh được ưa chuộng.",
    ],
    city_practical(
        "Không gian mở, dạo tự do mọi lúc.",
        "Miễn phí.",
        "20–30 phút.",
        "Chiều mát và buổi tối khi lên đèn.",
        "Kết hợp cùng Nhà hát Múa rối, nhà thờ chính toà Truyền Tin và Bờ kè Bruges gần đó.",
    ),
    [
        {"title": "Туристический портал Марий Эл — Патриаршая площадь в Йошкар-Оле", "url": "https://visit-mariel.ru/routs/sights/patriarshaya-ploshchad-v-yoshkar-ole/"},
        {"title": "OpenStreetMap — Патриаршая площадь (Йошкар-Ола)", "url": "https://www.openstreetmap.org/search?query=%D0%9F%D0%B0%D1%82%D1%80%D0%B8%D0%B0%D1%80%D1%88%D0%B0%D1%8F%20%D0%BF%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D1%8C%20%D0%99%D0%BE%D1%88%D0%BA%D0%B0%D1%80-%D0%9E%D0%BB%D0%B0"},
    ],
    ["square", "city-center", "architecture", "orthodox", "landmark", "photo-spot"],
    maps_text("Патриаршая площадь", "Йошкар-Ола", "Patriarch Square", "Yoshkar-Ola", 56.636908, 47.906977),
))

# ============================ NHÀ HÁT (theatre) ============================

# 12) Республиканский театр кукол ---------------------------------------------------
RECORDS.append(rec(
    "puppet-theatre-yoshkar-ola",
    "Nhà hát Múa rối Cộng hòa (toà nhà như lâu đài)",
    "Республиканский театр кукол",
    "Republican Puppet Theatre",
    ["theatre"],
    56.637024, 47.908544,
    "Царьградский проспект, 35 (Патриаршая площадь), Yoshkar-Ola, Cộng hòa Mari El",
    "Nhà hát Múa rối Cộng hòa Mari El nổi tiếng không chỉ vì các suất diễn cho thiếu nhi mà còn vì chính toà nhà: một 'lâu đài' gạch đỏ - trắng gợi liên tưởng lâu đài Neuschwanstein của Đức. Đây là một trong những công trình được chụp ảnh nhiều nhất Patriaршая площадь.",
    "Đoàn Múa rối Mari El hoạt động từ năm 1968 và đã đôi lần đổi trụ sở trước khi chuyển về ngôi nhà hiện nay vào năm 2014, trên phố Царьградский bên Quảng trường Thượng Phụ. Toà nhà là điểm nhấn thị giác của cả khu: khối gạch đỏ điểm trang trí trắng, nhiều tháp nhọn và ô cửa kiểu cổ tích, khiến du khách thường ví với những lâu đài Đức như Neuschwanstein. Bên trong có khán phòng lớn và nhỏ, sảnh rộng và một bảo tàng nhỏ về lịch sử nhà hát. Các suất diễn múa rối chủ yếu hướng tới thiếu nhi và gia đình, song với đông du khách, sức hút trước tiên đến từ chính diện mạo 'lâu đài' bên ngoài - một trong những phông nền chụp ảnh nổi tiếng của Yoshkar-Ola. Nếu đi cùng trẻ nhỏ, xem một buổi diễn là trải nghiệm đáng nhớ; còn lại, chỉ cần ngắm và chụp ảnh toà nhà cũng đã thú vị.",
    [
        "Toà nhà 'lâu đài' gạch đỏ - trắng gợi liên tưởng Neuschwanstein, điểm chụp ảnh nổi bật.",
        "Đoàn có từ 1968, chuyển về trụ sở hiện nay năm 2014 bên Quảng trường Thượng Phụ.",
        "Có khán phòng lớn - nhỏ và bảo tàng nhỏ về lịch sử nhà hát; diễn cho thiếu nhi, gia đình.",
    ],
    city_practical(
        "Ngắm bên ngoài tự do; suất diễn theo lịch (thường cuối tuần và dịp nghỉ), nên đặt vé trước.",
        "Ngắm bên ngoài miễn phí; vé xem diễn tra trên trang chính thức.",
        "15–20 phút (ngắm ngoài) hoặc ~1 giờ (xem diễn).",
        "Quanh năm; buổi tối toà nhà lên đèn rất đẹp.",
        "Đi cùng trẻ nhỏ nên xem một suất; kiểm tra lịch trên trang chính thức trước khi tới.",
    ),
    [
        {"title": "Культура.РФ — Республиканский театр кукол", "url": "https://www.culture.ru/institutes/21559/respublikanskii-teatr-kukol"},
        {"title": "Театр кукол Марий Эл — контакты (сайт)", "url": "https://teatrkukolmariel.ru/contact"},
    ],
    ["theatre", "puppet", "architecture", "family", "city", "photo-spot"],
    maps_org("https://yandex.com/maps/org/respublikanskiy_teatr_kukol/100391248409/", "Republican Puppet Theatre", "Yoshkar-Ola"),
    official_site="https://teatrkukolmariel.ru/",
))

# 13) Марийский национальный театр драмы им. Шкетана --------------------------------
RECORDS.append(rec(
    "shketan-mari-drama-theatre",
    "Nhà hát Kịch Quốc gia Mari mang tên M. Shketan",
    "Марийский национальный театр драмы им. М. Шкетана",
    "Mari National Drama Theatre named after M. Shketan",
    ["theatre"],
    56.631729, 47.891538,
    "пл. Ленина, 2, Yoshkar-Ola, Cộng hòa Mari El",
    "Nhà hát Kịch Quốc gia Mari mang tên nhà văn M. Shketan là nhà hát tiếng Mari đầu tiên và quan trọng nhất, cái nôi của sân khấu dân tộc. Toạ lạc bên Quảng trường Lenin, đây là trung tâm giữ gìn ngôn ngữ, kịch nghệ và bản sắc văn hoá Mari.",
    "Là nhà hát kịch nói tiếng Mari lâu đời và tiêu biểu nhất, Марийский национальный театр драмы mang tên nhà văn - nhà viết kịch Mari M. Shketan, được xem là cái nôi của nghệ thuật sân khấu dân tộc Mari. Trên sân khấu này, các vở diễn bằng tiếng Mari - từ kịch dân gian, lịch sử tới hiện đại - góp phần gìn giữ và phát triển ngôn ngữ cùng bản sắc của một trong những dân tộc Finno-Ugric ở vùng Volga. Nhà hát toạ lạc bên Quảng trường Lenin ở trung tâm Yoshkar-Ola, trong một toà nhà bề thế mang chức năng biểu diễn và văn hoá. Với du khách nước ngoài, rào cản ngôn ngữ khiến việc xem trọn một vở có thể khó, nhưng bản thân nhà hát là điểm đến để hiểu đời sống văn hoá đương đại của người Mari; nhiều buổi diễn còn kết hợp âm nhạc, trang phục và vũ điệu truyền thống đầy màu sắc. Đây là lựa chọn hợp cho ai muốn chạm tới 'linh hồn' văn hoá bản địa, vượt ra ngoài lớp kiến trúc phỏng châu Âu của trung tâm.",
    [
        "Nhà hát kịch tiếng Mari lâu đời và tiêu biểu nhất - cái nôi của sân khấu dân tộc Mari.",
        "Mang tên nhà văn - nhà viết kịch Mari M. Shketan; diễn bằng tiếng Mari.",
        "Bên Quảng trường Lenin, trung tâm gìn giữ ngôn ngữ và bản sắc văn hoá Mari.",
    ],
    city_practical(
        "Suất diễn theo lịch mùa (mùa diễn thường thu - xuân); nên đặt vé trước.",
        "Vé bán tại quầy hoặc trực tuyến; tra giá trên trang chính thức.",
        "2–3 giờ (một buổi diễn).",
        "Mùa diễn thu - xuân; các dịp liên hoan sân khấu.",
        "Kiểm tra lịch/ngôn ngữ vở diễn trước; hợp với ai muốn tìm hiểu văn hoá Mari đương đại.",
    ),
    [
        {"title": "Культура.РФ — Марийский национальный театр драмы им. М. Шкетана", "url": "https://www.culture.ru/institutes/10663/mariiskii-nacionalnyi-teatr-dramy-im-m-shketana"},
        {"title": "Марийский нацтеатр драмы им. М. Шкетана — сайт", "url": "https://shketan.ru/"},
    ],
    ["theatre", "drama", "mari-culture", "language", "city", "performing-arts"],
    maps_text("Марийский национальный театр драмы им. М. Шкетана", "Йошкар-Ола", "Mari National Drama Theatre", "Yoshkar-Ola", 56.631729, 47.891538),
    official_site="https://shketan.ru/",
))

# ============================ BẢO TÀNG (museum) ============================

# 14) Музей истории города Йошкар-Олы -----------------------------------------------
RECORDS.append(rec(
    "city-history-museum-yoshkar-ola",
    "Bảo tàng Lịch sử thành phố Yoshkar-Ola",
    "Музей истории города Йошкар-Олы",
    "Museum of the History of Yoshkar-Ola",
    ["museum"],
    56.638084, 47.902445,
    "ул. Вознесенская, 39, Yoshkar-Ola, Cộng hòa Mari El",
    "Bảo tàng Lịch sử thành phố kể câu chuyện Yoshkar-Ola từ pháo đài Tsaryovokokshaysk thế kỷ 16 tới thành phố 'châu Âu thu nhỏ' hôm nay. Trưng bày ảnh, đồ vật, mô hình về đời sống đô thị, nghề nghiệp và các nhân vật gắn với thành phố.",
    "Nằm trên phố Voznesenskaya trong khu lõi lịch sử, Музей истории города Йошкар-Олы chuyên về quá trình hình thành và phát triển của chính thành phố. Các gian trưng bày dẫn người xem qua chặng đường từ pháo đài Tsaryovokokshaysk lập cuối thế kỷ 16, qua thị trấn thương nhân tỉnh lẻ thời đế quốc Nga, tới đô thị Xô Viết và diện mạo 'châu Âu thu nhỏ' được tái thiết mạnh mẽ trong thập niên 2000. Bộ sưu tập gồm ảnh tư liệu, bản đồ, đồ dùng sinh hoạt, sản phẩm thủ công - công nghiệp địa phương, cùng những câu chuyện về các nhân vật, nghề nghiệp và biến đổi của phố phường. Quy mô vừa phải, nội dung cô đọng, bảo tàng là nơi lý tưởng để 'đọc' bối cảnh trước hoặc sau khi dạo bộ trung tâm - giúp du khách hiểu vì sao Yoshkar-Ola lại có gương mặt kiến trúc khác thường đến vậy.",
    [
        "Kể lịch sử Yoshkar-Ola từ pháo đài Tsaryovokokshaysk thế kỷ 16 tới thành phố hôm nay.",
        "Trưng bày ảnh tư liệu, bản đồ, đồ sinh hoạt và câu chuyện về phố phường, con người.",
        "Quy mô vừa, cô đọng - hợp để hiểu bối cảnh trước/sau khi dạo trung tâm.",
    ],
    city_practical(
        "Khoảng 9:00–18:00 (nên kiểm tra ngày nghỉ trong tuần trước khi đến).",
        "Vé phải chăng, mua tại quầy.",
        "1–1,5 giờ.",
        "Quanh năm; tiện ghép với cụm trung tâm.",
        "Kết hợp cùng Bờ kè Bruges và các nhà thờ trên phố Voznesenskaya ở gần.",
    ),
    [
        {"title": "2ГИС — Музей истории города Йошкар-Олы, ул. Вознесенская, 39", "url": "https://2gis.ru/yoshkarola/search/%D0%9C%D1%83%D0%B7%D0%B5%D0%B9%20%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D0%B8%20%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0"},
        {"title": "Туристический портал Марий Эл — музеи Йошкар-Олы", "url": "https://visit-mariel.ru/"},
    ],
    ["museum", "history", "city", "culture", "indoor"],
    maps_text("Музей истории города Йошкар-Олы", "Йошкар-Ола", "Museum of the History of Yoshkar-Ola", "Yoshkar-Ola", 56.638084, 47.902445),
))

# ============================ CUNG ĐIỆN / LÂU ĐÀI (palace) ============================

# 15) Дворец бракосочетаний (замок ЗАГС) --------------------------------------------
RECORDS.append(rec(
    "wedding-palace-yoshkar-ola",
    "Cung điện hôn nhân (Lâu đài ZAGS)",
    "Дворец бракосочетаний (замок ЗАГС)",
    "Wedding Palace (ZAGS Castle)",
    ["palace"],
    56.632846, 47.909085,
    "Набережная Брюгге, 5, Yoshkar-Ola, Cộng hòa Mari El",
    "Cung điện hôn nhân của Yoshkar-Ola là một toà 'lâu đài' cổ tích xây năm 2012 bên Bờ kè Bruges, nơi đăng ký kết hôn của thành phố. Với tháp nhọn, tường sáng màu và vị trí ven sông, đây là phông nền chụp ảnh cưới và 'check-in' nổi tiếng.",
    "Khánh thành năm 2012 trên Bờ kè Bruges, Дворец бракосочетаний (Cung điện hôn nhân, tức toà ЗАГС - cơ quan hộ tịch) được xây theo hình một lâu đài hoàng gia cổ tích, với tháp nhọn, mái dốc và mặt tiền sáng màu soi bóng xuống sông Malaya Kokshaga. Một nét thú vị được nhắc tới nhiều: các đôi uyên ương bước vào làm thủ tục từ phía phố Eshkinina, rồi bước ra Bờ kè Bruges với tư cách vợ chồng - như một 'nghi thức' nhỏ đầy chất điện ảnh. Ngay bên cạnh là tượng đài Grace Kelly và Vương công Rainier III, càng tô đậm chủ đề tình yêu - hôn nhân của cả khu bờ kè. Dù là cơ quan hành chính, toà lâu đài với kiến trúc phỏng châu Âu và vị trí đắc địa đã trở thành một trong những công trình 'ăn ảnh' và được yêu thích nhất trung tâm 'Yoshkar-Ola thu nhỏ'. Du khách thường ngắm và chụp ảnh từ bên ngoài dọc bờ kè.",
    [
        "Toà 'lâu đài' cổ tích xây năm 2012, là nơi đăng ký kết hôn của thành phố.",
        "Đôi uyên ương vào từ phố Eshkinina và bước ra Bờ kè Bruges - 'nghi thức' đầy chất phim.",
        "Ngay bên tượng đài Grace Kelly & Rainier III; phông nền chụp ảnh cưới nổi tiếng.",
    ],
    city_practical(
        "Ngắm bên ngoài tự do; bên trong là cơ quan hộ tịch, làm việc giờ hành chính (không phải điểm tham quan nội thất).",
        "Miễn phí (ngắm bên ngoài).",
        "15–20 phút.",
        "Chiều mát và buổi tối khi bờ kè lên đèn; cuối tuần thường có nhiều đám cưới.",
        "Chụp ảnh từ bờ kè; tôn trọng các đôi đang làm lễ; kết hợp cùng tượng Grace Kelly và Bờ kè Bruges.",
    ),
    [
        {"title": "Tonkosti.ru — Дворец бракосочетаний в Йошкар-Оле", "url": "https://tonkosti.ru/%D0%94%D0%B2%D0%BE%D1%80%D0%B5%D1%86_%D0%B1%D1%80%D0%B0%D0%BA%D0%BE%D1%81%D0%BE%D1%87%D0%B5%D1%82%D0%B0%D0%BD%D0%B8%D0%B9_%D0%B2_%D0%99%D0%BE%D1%88%D0%BA%D0%B0%D1%80-%D0%9E%D0%BB%D0%B5"},
        {"title": "Газета «Йошкар-Ола» — как менялся городской ЗАГС", "url": "https://www.gg12.ru/russkij-terem-dvorets-schastya-goticheskij-zamok-kak-menyalsya-gorodskoj-zags-joshkar-oly/"},
    ],
    ["palace", "castle", "wedding", "embankment", "architecture", "photo-spot"],
    maps_text("Дворец бракосочетаний", "Йошкар-Ола набережная Брюгге", "Wedding Palace ZAGS", "Yoshkar-Ola", 56.632846, 47.909085),
))

# ============================ THIÊN NHIÊN (park_garden) ============================

# 16) Озеро Морской Глаз -------------------------------------------------------------
RECORDS.append(rec(
    "morskoy-glaz-lake",
    "Hồ Mắt Biển (Morskoy Glaz / Mushyl)",
    "Озеро Морской Глаз",
    "Morskoy Glaz Lake (Sea Eye)",
    ["park_garden"],
    56.1625, 48.7601,
    "gần làng Sharyboksad, huyện Volzhsky, Cộng hòa Mari El",
    "Hồ Mắt Biển (Morskoy Glaz) là hồ karst tròn vành vạnh với làn nước màu lục ngọc bích lạ mắt, nằm nép bên sườn đồi ở huyện Volzhsky. Hình dáng cân đối và sắc nước độc đáo khiến nơi đây thành một trong những hồ 'check-in' nổi tiếng nhất Mari El.",
    "Nằm gần làng Sharyboksad thuộc huyện Volzhsky, Морской Глаз (nghĩa 'Mắt Biển'; người địa phương gọi đúng tên là Mushyl) là một hồ karst hình thành do sụt lún khoảng 20 nghìn năm trước. Hồ có dạng gần như tròn hoàn hảo, đường kính chỉ chừng 45–50 m nhưng sâu tới khoảng 37–42 m, với làn nước trong màu lục - ngọc bích rất riêng nhờ tảo và khoáng chất. Điểm đặc biệt là hồ nằm ngay bên một sườn dốc, khiến khi nhìn từ trên cao, mặt nước xanh biếc trông như một con mắt lấp lánh giữa cảnh đồi - đồng, tạo nên khung hình ngoạn mục. Hồ được xếp hạng di tích thiên nhiên và là điểm dừng chân, chụp ảnh, dã ngoại ăn khách; nhiều người kết hợp ghé trong hành trình khám phá vùng nông thôn phía nam Mari El. Do là hồ tự nhiên nhạy cảm, du khách nên giữ vệ sinh, cẩn thận ở mép dốc và không xả rác.",
    [
        "Hồ karst tròn vành vạnh, nước màu lục ngọc bích, sâu ~37–42 m dù đường kính chỉ ~45–50 m.",
        "Nằm bên sườn dốc, nhìn từ trên như một 'con mắt' xanh biếc - khung hình ngoạn mục.",
        "Di tích thiên nhiên, điểm chụp ảnh và dã ngoại nổi tiếng ở huyện Volzhsky.",
    ],
    nature_practical(
        "Nửa ngày (gồm di chuyển từ Yoshkar-Ola/Volzhsk).",
        "Cuối xuân đến đầu thu, ngày nắng để thấy rõ sắc nước ngọc bích.",
        "Cẩn thận ở mép dốc trơn; mang nước, đồ dã ngoại; đi ô tô thuận tiện nhất, không xả rác.",
    ),
    [
        {"title": "Wikipedia (RU) — Морской Глаз", "url": "https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D1%81%D0%BA%D0%BE%D0%B9_%D0%93%D0%BB%D0%B0%D0%B7"},
        {"title": "2ГИС — Озеро Морской Глаз, Волжский район", "url": "https://2gis.ru/geo/70030076167351110"},
    ],
    ["lake", "karst", "nature", "scenic", "photo-spot", "emerald"],
    maps_text("Озеро Морской Глаз", "Марий Эл Шарибоксад", "Morskoy Glaz Lake", "Mari El", 56.1625, 48.7601),
))

# 17) Озеро Яльчик ------------------------------------------------------------------
RECORDS.append(rec(
    "yalchik-lake",
    "Hồ Yalchik",
    "Озеро Яльчик",
    "Lake Yalchik",
    ["park_garden"],
    56.0111, 48.4083,
    "trung tâm huyện Volzhsky, trong Vườn quốc gia Mari Chodra, Cộng hòa Mari El",
    "Yalchik là hồ lớn nhất Mari El về diện tích và thể tích, một hồ karst nước trong giữa rừng thông của vườn quốc gia Mari Chodra. Dễ tiếp cận bằng cả tàu hoả lẫn ô tô, đây là điểm tắm hồ, cắm trại và nghỉ dưỡng được yêu thích nhất vùng Volga lân cận.",
    "Nằm trong Vườn quốc gia Mari Chodra ở huyện Volzhsky, Яльчик là hồ lớn nhất Cộng hòa Mari El xét về diện tích mặt nước (khoảng 149,6 ha) và thể tích. Hồ có nguồn gốc karst, hình thành từ sự hợp nhất của nhiều phễu sụt, thực chất gồm hai phần Yalchik Lớn và Yalchik Nhỏ nối nhau qua một eo nước. Bao quanh là rừng thông thơm ngát tốt cho sức khoẻ, khiến nơi đây thành điểm cắm trại, tắm mát, dã ngoại quen thuộc của người dân Mari El, Tatarstan và du khách xa. Một lợi thế lớn là khả năng tiếp cận: có ga tàu 'Yalchik' cách hồ chừng 10 phút đi bộ, cùng tuyến đường bộ và xe buýt từ Kazan, Volzhsk. Mùa hè hồ đông kín lều trại, người tắm, chèo thuyền và câu cá; mùa thu là mùa hái nấm và liên hoan ca hát 'bard'. Ai muốn tĩnh lặng hơn thường đi sâu vào rừng tới các hồ Glukhoe, Mushan-Yer. Vì nằm trong khu bảo tồn, du khách cần tuân thủ quy định phòng cháy và giữ vệ sinh.",
    [
        "Hồ lớn nhất Mari El (~149,6 ha), nguồn gốc karst, gồm Yalchik Lớn và Yalchik Nhỏ.",
        "Rừng thông trong lành, điểm tắm hồ - cắm trại - dã ngoại được yêu thích nhất vùng.",
        "Dễ đến: có ga tàu 'Yalchik' gần hồ, cùng đường bộ và xe buýt từ Kazan, Volzhsk.",
    ],
    nature_practical(
        "Một ngày hoặc cắm trại nhiều ngày.",
        "Tháng 6–8 cho tắm hồ, cắm trại; mùa thu cho hái nấm và cảnh lá vàng.",
        "Mang đồ cắm trại, thuốc chống côn trùng; hỏi lệnh cấm lửa trước khi đốt lửa trại; giữ vệ sinh khu bảo tồn.",
    ),
    [
        {"title": "Wikipedia (RU) — Яльчик", "url": "https://ru.wikipedia.org/wiki/%D0%AF%D0%BB%D1%8C%D1%87%D0%B8%D0%BA"},
        {"title": "Туристический портал Марий Эл — Озеро Яльчик", "url": "https://visit-mariel.ru/routs/sights/ozero-yalchik/"},
    ],
    ["lake", "karst", "forest", "camping", "swimming", "mari-chodra"],
    maps_text("Озеро Яльчик", "Марий Эл", "Lake Yalchik", "Mari El", 56.0111, 48.4083),
))

# 18) Зелёный ключ (родник) ---------------------------------------------------------
RECORDS.append(rec(
    "zeleny-klyuch-spring",
    "Suối nguồn Zeleny Klyuch (Chìa khoá Xanh)",
    "Зелёный ключ",
    "Zeleny Klyuch Spring",
    ["park_garden"],
    56.154892, 48.425653,
    "chân đồi Klenovaya Gora, ven sông Ilet, Vườn quốc gia Mari Chodra, huyện Volzhsky, Cộng hòa Mari El",
    "Zeleny Klyuch ('Chìa khoá/Nguồn Xanh') là mạch nước khoáng lớn nhất Vườn quốc gia Mari Chodra, phun lên từ đáy một phễu nhỏ dưới chân đồi Klenovaya Gora rồi chảy ra sông Ilet. Nước trong mát quanh năm, được cho là tốt cho sức khoẻ - điểm dừng chân được nhiều đoàn đi rừng ưa thích.",
    "Zeleny Klyuch là suối khoáng nổi tiếng nhất của Vườn quốc gia Mari Chodra, nằm dưới chân đồi Klenovaya Gora (Đồi Phong) bên bờ sông Ilet, huyện Volzhsky. Nước ngầm trào lên từ đáy một phễu nhỏ và tuôn thành dòng chảy ra sông, mang theo khoáng chất; mạch nước giữ nhiệt độ mát ổn định quanh năm, mùa đông không đóng băng còn mùa hè mát lạnh. Người địa phương và du khách xem đây là nguồn nước 'lành', thường ghé uống, rửa mặt và nghỉ chân. Khung cảnh quanh suối là rừng phong - thông và triền dốc Klenovaya Gora, một trong những nơi đẹp và trong lành nhất của Mari Chodra, gắn với các tuyến đi bộ, chèo thuyền trên sông Ilet và cây sồi cổ Pugachev ở gần. Là đối tượng thiên nhiên trong khu bảo tồn, suối cần được giữ sạch; du khách không nên xả rác hay làm xáo trộn mạch nước.",
    [
        "Suối khoáng lớn nhất Mari Chodra, phun từ đáy phễu dưới chân đồi Klenovaya Gora.",
        "Nước trong mát ổn định quanh năm, được xem là 'lành', tốt cho sức khoẻ.",
        "Gắn với các tuyến đi rừng, chèo sông Ilet và cây sồi Pugachev ở gần.",
    ],
    nature_practical(
        "1–2 giờ (thường ghép trong tuyến khám phá Klenovaya Gora - Mari Chodra).",
        "Cuối xuân đến đầu thu; mùa hè để tận hưởng nước mát.",
        "Đi giày đi bộ; kết hợp thăm sồi Pugachev và Đồi Phong; giữ sạch nguồn nước, không xả rác.",
    ),
    [
        {"title": "Марий Эл и Йошкар-Ола — Зелёный Ключ", "url": "https://www.mariel.ru/green-key/"},
        {"title": "OpenStreetMap — Зелёный Ключ (родник)", "url": "https://www.openstreetmap.org/search?query=%D0%97%D0%B5%D0%BB%D1%91%D0%BD%D1%8B%D0%B9%20%D0%9A%D0%BB%D1%8E%D1%87%20%D0%9C%D0%B0%D1%80%D0%B8%D0%B9%20%D0%A7%D0%BE%D0%B4%D1%80%D0%B0"},
    ],
    ["spring", "mineral-water", "nature", "mari-chodra", "hiking", "forest"],
    maps_org("https://yandex.ru/maps/org/zelyony_klyuch/241120877989/", "Zeleny Klyuch Spring", "Mari El"),
))

# 19) Дуб Пугачёва ------------------------------------------------------------------
RECORDS.append(rec(
    "pugachev-oak",
    "Cây sồi Pugachev (Dub Pugachyova)",
    "Дуб Пугачёва",
    "Pugachev Oak",
    ["park_garden"],
    56.13472, 48.46833,
    "trên đồi Klenovaya Gora, Vườn quốc gia Mari Chodra, huyện Volzhsky, Cộng hòa Mari El",
    "Sồi Pugachev là cây sồi cổ thụ khổng lồ cao ~26 m trên đồi Klenovaya Gora, gắn với truyền thuyết thủ lĩnh nông dân Yemelyan Pugachev từng dừng chân. Được công nhận là 'di tích thiên nhiên sống', đây là một trong những cây nổi tiếng nhất Mari El.",
    "Trên khối đồi Klenovaya Gora của Vườn quốc gia Mari Chodra, cách hồ Konanyer chừng 1 km về phía tây bắc, sừng sững cây Дуб Пугачёва - một cây sồi cổ thụ cao khoảng 26 m, chu vi thân rất lớn (đường kính ~1,59 m), tuổi ước tính vài trăm năm. Truyền thuyết dân gian kể rằng thủ lĩnh cuộc khởi nghĩa nông dân Yemelyan Pugachev từng dừng chân, thậm chí leo lên cây để quan sát vùng Kazan phía xa trong thế kỷ 18 - từ đó cây mang tên ông. Năm 2013, cây được trao danh hiệu 'di tích thiên nhiên sống' của nước Nga. Với kích thước ấn tượng và lớp vỏ sần sùi rêu phong, cây sồi là điểm đến gắn liền với các tuyến đi bộ trong rừng Mari Chodra, thường được ghép cùng suối Zeleny Klyuch và Đồi Phong. Đây là nơi để cảm nhận vẻ trầm mặc của rừng già và những lớp truyền thuyết phủ lên thiên nhiên Mari El.",
    [
        "Cây sồi cổ thụ cao ~26 m, đường kính thân ~1,59 m, tuổi vài trăm năm.",
        "Gắn truyền thuyết thủ lĩnh Pugachev từng dừng chân, leo cây quan sát vùng Kazan.",
        "Được công nhận 'di tích thiên nhiên sống' (2013); điểm đến trên đồi Klenovaya Gora.",
    ],
    nature_practical(
        "30–60 phút (thường ghép trong tuyến đi bộ Klenovaya Gora).",
        "Cuối xuân đến đầu thu.",
        "Đi giày đi bộ theo đường mòn; kết hợp thăm suối Zeleny Klyuch và hồ Konanyer; không làm hại cây.",
    ),
    [
        {"title": "Wikipedia (RU) — Дуб Пугачёва", "url": "https://ru.wikipedia.org/wiki/%D0%94%D1%83%D0%B1_%D0%9F%D1%83%D0%B3%D0%B0%D1%87%D1%91%D0%B2%D0%B0"},
        {"title": "Wikipedia (RU) — Марий Чодра", "url": "https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D0%B8%D0%B9_%D0%A7%D0%BE%D0%B4%D1%80%D0%B0"},
    ],
    ["nature", "tree", "legend", "mari-chodra", "hiking", "monument-of-nature"],
    maps_text("Дуб Пугачёва", "Марий Чодра", "Pugachev Oak", "Mari El", 56.13472, 48.46833),
))

# 20) Табашинское озеро (Зрыв) ------------------------------------------------------
RECORDS.append(rec(
    "tabashinskoye-zryv-lake",
    "Hồ Tabashinskoye (Zryv) - hồ sâu nhất vùng",
    "Табашинское озеро (Зрыв)",
    "Lake Tabashinskoye (Zryv)",
    ["park_garden"],
    56.981482, 47.805194,
    "cạnh làng Tabashino, huyện Orshansky, cách Yoshkar-Ola ~45 km về phía bắc, Cộng hòa Mari El",
    "Tabashinskoye (còn gọi Zryv) là hồ karst sâu nhất vùng trung Volga, nằm bên làng Tabashino ở huyện Orshansky. Nước trong đến mức có thể thấy những thân cây dựng đứng dưới đáy như một 'khu rừng ngầm', tạo cảnh quan huyền bí độc đáo.",
    "Nằm ngay cạnh làng Tabashino thuộc huyện Orshansky, cách Yoshkar-Ola khoảng 45 km về phía bắc, hồ Табашинское - người dân quen gọi là Зрыв ('chỗ sụt') - là hồ karst sâu nhất vùng trung Volga. Diện tích chỉ chừng 26 ha nhưng độ sâu phần giữa đạt trên 55 m (một số phép đo bằng máy dò còn cho số liệu lớn hơn nhiều), khiến hồ được ví như một cái 'giếng' khổng lồ giữa đồng quê. Nước hồ ngọt và trong khác thường: ở độ sâu tới khoảng 12 m vẫn có thể nhìn thấy những thân cây đứng thẳng dưới lòng hồ, tạo ấn tượng về một 'khu rừng chìm' huyền bí. Hồ là nguồn của sông Pizhanka và đã được công nhận là di tích thiên nhiên từ năm 1974. Với người mê cảnh quan lạ và địa chất karst, đây là điểm đến đáng giá; quanh hồ có tuyến đường mòn sinh thái xuất phát từ làng Tabashino. Do là hồ sâu nguy hiểm, du khách cần cẩn trọng khi xuống nước và giữ gìn môi trường.",
    [
        "Hồ karst sâu nhất vùng trung Volga (giữa hồ sâu trên 55 m) dù diện tích chỉ ~26 ha.",
        "Nước trong tới mức thấy thân cây đứng dưới đáy như 'khu rừng ngầm' huyền bí.",
        "Nguồn sông Pizhanka, di tích thiên nhiên từ 1974; có đường mòn sinh thái từ làng Tabashino.",
    ],
    nature_practical(
        "Nửa ngày (gồm di chuyển ~45 km từ Yoshkar-Ola).",
        "Cuối xuân đến đầu thu.",
        "Cẩn trọng vì hồ rất sâu; đi ô tô thuận tiện; theo đường mòn sinh thái và giữ vệ sinh.",
    ),
    [
        {"title": "РГО — Загадка озера Зрыв", "url": "https://www.rgo.ru/ru/article/zagadka-ozera-zryv"},
        {"title": "MariMedia — Табашинское озеро (Зрыв)", "url": "https://www.marimedia.ru/mariel/tourism/place/180/"},
    ],
    ["lake", "karst", "deepest", "nature", "scenic", "unusual"],
    maps_text("Табашинское озеро Зрыв", "Оршанский район Марий Эл", "Lake Tabashinskoye Zryv", "Mari El", 56.981482, 47.805194),
))

# 21) Кленовая Гора ------------------------------------------------------------------
RECORDS.append(rec(
    "klenovaya-gora",
    "Đồi Phong (Klenovaya Gora)",
    "Кленовая Гора",
    "Klenovaya Gora (Maple Mountain)",
    ["park_garden"],
    56.13389, 48.42667,
    "Vườn quốc gia Mari Chodra, huyện Volzhsky, Cộng hòa Mari El",
    "Klenovaya Gora ('Đồi Phong') là khối đồi rừng phong - thông trong Vườn quốc gia Mari Chodra, nổi tiếng với không khí trong lành, suối khoáng và cảnh quan đẹp. Đây là trung tâm của nhiều tuyến du lịch sinh thái, quy tụ suối Zeleny Klyuch, sồi Pugachev và các hồ karst.",
    "Кленовая Гора (Đồi Phong) là một khối đồi cao phủ rừng phong xen thông ở phía nam Vườn quốc gia Mari Chodra, bên vòng cung sông Ilet, huyện Volzhsky. Vùng này được xem là 'trái tim' cảnh quan của Mari Chodra: khí hậu tiểu vùng trong lành, nhiều mạch nước khoáng (nổi tiếng nhất là Zeleny Klyuch), cùng địa hình karst với hồ, phễu sụt và hang nhỏ. Trên và quanh đồi là hàng loạt điểm đến quen thuộc - suối Zeleny Klyuch, cây sồi cổ Pugachev, các hồ Konanyer, Mushan-Yer - liên kết bởi mạng lưới đường mòn đi bộ và tuyến chèo thuyền trên sông Ilet. Từng có khu điều dưỡng tận dụng nước khoáng và không khí nơi đây. Với du khách, Klenovaya Gora là địa bàn lý tưởng để đi bộ đường dài, dã ngoại và 'tắm rừng', đặc biệt rực rỡ vào mùa thu khi lá phong chuyển vàng đỏ. Là khu bảo tồn, du khách cần tuân thủ quy định và giữ gìn thiên nhiên.",
    [
        "Khối đồi rừng phong - thông, 'trái tim' cảnh quan của Vườn quốc gia Mari Chodra.",
        "Không khí trong lành, nhiều suối khoáng; quy tụ Zeleny Klyuch, sồi Pugachev, các hồ karst.",
        "Mạng lưới đường mòn và tuyến chèo sông Ilet; rực rỡ nhất mùa thu lá phong.",
    ],
    nature_practical(
        "Nửa ngày đến trọn ngày (đi bộ, dã ngoại).",
        "Mùa hè cho đi rừng, chèo thuyền; mùa thu cho cảnh lá phong vàng đỏ.",
        "Mang giày đi bộ, nước, thuốc chống côn trùng; tuân thủ quy định vườn quốc gia và phòng cháy.",
    ),
    [
        {"title": "Wikipedia (RU) — Кленовая Гора", "url": "https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F_%D0%93%D0%BE%D1%80%D0%B0"},
        {"title": "Wikipedia (RU) — Марий Чодра", "url": "https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D0%B8%D0%B9_%D0%A7%D0%BE%D0%B4%D1%80%D0%B0"},
    ],
    ["nature", "forest", "hills", "mari-chodra", "hiking", "autumn"],
    maps_text("Кленовая Гора", "Марий Чодра", "Klenovaya Gora", "Mari El", 56.13389, 48.42667),
))

# 22) Озеро Кичиер ------------------------------------------------------------------
RECORDS.append(rec(
    "kichier-lake",
    "Hồ Kichier",
    "Озеро Кичиер",
    "Lake Kichier",
    ["park_garden"],
    56.0695, 48.3465,
    "Vườn quốc gia Mari Chodra, huyện Volzhsky, Cộng hòa Mari El",
    "Kichier là chuỗi hồ karst nước trong hình thù uốn lượn trong Vườn quốc gia Mari Chodra, được yêu thích để tắm, chèo thuyền và nghỉ dưỡng. Bao quanh là rừng thông, có các khu điều dưỡng và trại hè bên bờ.",
    "Kichier là một trong những hồ đẹp và được biết đến nhiều của Vườn quốc gia Mari Chodra, thuộc huyện Volzhsky. Hồ có nguồn gốc karst, gồm các phần nối nhau tạo hình uốn lượn thon dài, nước trong và tương đối ấm vào mùa hè. Nằm giữa rừng thông thơm ngát, Kichier là điểm nghỉ dưỡng quen thuộc: quanh bờ có khu điều dưỡng (санаторий), trại hè cho thiếu nhi và các bãi tắm, chèo thuyền. So với Yalchik ồn ào hơn, Kichier thường được xem là lựa chọn dễ chịu cho những chuyến nghỉ gia đình gần gũi thiên nhiên. Hồ nằm trong tuyến khám phá Mari Chodra cùng Yalchik, Klenovaya Gora và sông Ilet, thuận tiện cho các hành trình nhiều ngày. Là hồ trong khu bảo tồn, du khách cần giữ vệ sinh và tuân thủ quy định phòng cháy khi cắm trại.",
    [
        "Hồ karst nước trong, hình uốn lượn thon dài giữa rừng thông Mari Chodra.",
        "Có khu điều dưỡng, trại hè và bãi tắm bên bờ - điểm nghỉ dưỡng gia đình.",
        "Nằm trong tuyến khám phá Mari Chodra cùng Yalchik, Klenovaya Gora và sông Ilet.",
    ],
    nature_practical(
        "Một ngày hoặc nghỉ nhiều ngày.",
        "Tháng 6–8 cho tắm hồ, nghỉ dưỡng.",
        "Mang đồ bơi, chống côn trùng; hỏi lệnh cấm lửa trước khi cắm trại; giữ vệ sinh khu bảo tồn.",
    ),
    [
        {"title": "Wikipedia (RU) — Кичиер", "url": "https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D1%87%D0%B8%D0%B5%D1%80"},
        {"title": "Wikipedia (RU) — Марий Чодра", "url": "https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D0%B8%D0%B9_%D0%A7%D0%BE%D0%B4%D1%80%D0%B0"},
    ],
    ["lake", "karst", "forest", "resort", "swimming", "mari-chodra"],
    maps_text("Озеро Кичиер", "Марий Чодра", "Lake Kichier", "Mari El", 56.0695, 48.3465),
))

# ============================ KHÁC (other) ============================

# 23) Нолькин камень (штольни) ------------------------------------------------------
RECORDS.append(rec(
    "nolkin-kamen-quarries",
    "Hang khai thác đá Nolkin Kamen",
    "Нолькин камень",
    "Nolkin Kamen Quarries",
    ["other"],
    56.852, 49.035,
    "gần làng Gornyak, huyện Sernursky, thung lũng sông Nolka, Cộng hòa Mari El",
    "Nolkin Kamen là hệ thống hang - đường hầm nhân tạo trong lòng núi đá, hình thành từ việc khai thác đá sa thạch làm cối xay ('đá Cheremis') xưa kia. Những đường hầm dài, mát lạnh cả mùa hè với nhũ đá thu hút dân ưa khám phá và speleo.",
    "Nằm trong thung lũng sông Nolka gần làng Gornyak thuộc huyện Sernursky (đông bắc Mari El), 'Нолькин камень' là quần thể hang - đường hầm nhân tạo trổ sâu vào vách núi đá. Chúng là dấu tích của nghề khai thác đá sa thạch thạch anh - loại 'đá Cheremis' cứng - dùng để đẽo cối xay từ nhiều thế kỷ trước. Các đường hầm đã được giới speleo khảo sát, có lối ăn sâu tới khoảng 300 m vào lòng núi; bên trong mát lạnh ngay cả giữa mùa hè, đọng lại những khối thạch nhũ - băng đá và bầu không khí bí ẩn. Đây là điểm đến hấp dẫn với người ưa mạo hiểm, thám hiểm hang và chụp ảnh khác lạ, thường kết hợp trong các tour off-road tới vùng nông thôn đông bắc. Tuy nhiên, việc chui vào hang tiềm ẩn rủi ro (sập đá, lạc, thiếu sáng), nên tuyệt đối cần đèn, trang bị phù hợp và tốt nhất đi cùng hướng dẫn viên/người có kinh nghiệm; không nên tự ý xuống hang nếu thiếu chuẩn bị.",
    [
        "Hệ thống hang - đường hầm nhân tạo do khai thác đá sa thạch làm cối xay ('đá Cheremis').",
        "Có lối ăn sâu ~300 m, mát lạnh cả mùa hè, đọng thạch nhũ - bầu không khí bí ẩn.",
        "Điểm thám hiểm hấp dẫn nhưng cần đèn, trang bị và hướng dẫn viên - không tự ý xuống hang.",
    ],
    nature_practical(
        "Nửa ngày đến trọn ngày (đường tới xa và phải đi bộ vào).",
        "Cuối xuân đến đầu thu; tránh mùa mưa lầy lội.",
        "Bắt buộc mang đèn pin, mũ bảo hộ, giày chắc; đi theo nhóm/có hướng dẫn; cẩn trọng nguy cơ sập, lạc.",
    ),
    [
        {"title": "Wikipedia (RU) — Нолькин камень", "url": "https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D0%BD_%D0%BA%D0%B0%D0%BC%D0%B5%D0%BD%D1%8C"},
        {"title": "ООПТ России — Нолькин камень", "url": "http://oopt.aari.ru/oopt/%D0%9D%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D0%BD-%D0%BA%D0%B0%D0%BC%D0%B5%D0%BD%D1%8C"},
    ],
    ["cave", "quarry", "speleo", "adventure", "nature", "unusual"],
    maps_text("Нолькин камень", "Сернурский район Марий Эл", "Nolkin Kamen", "Mari El", 56.852, 49.035),
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
