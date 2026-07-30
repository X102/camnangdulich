# -*- coding: utf-8 -*-
"""_add_places_chuvashia_20260728.py — VÙNG: Cộng hòa Chuvashia (Чувашская Республика)
(lần chạy tự động 2026-07-28).

Bối cảnh: chuvashia.json hiện có 7 địa điểm. Bổ sung 25 địa điểm THẬT SỰ nổi tiếng/đặc
sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 32 (≥30). Chỉ chọn danh lam thắng cảnh
có thật, có toạ độ xác minh được; KHÔNG bịa/nhồi.

Phân bố loại hình (25 bản ghi mới):
- museum (6): Музей истории пива, Музей В. И. Чапаева, Художественный музей, Музей истории
  трактора, Музей чувашской вышивки, Ибресинский этнографический музей.
- church (6): Свято-Троицкий мужской монастырь, Успенская церковь, Церковь Михаила
  Архангела, Спасо-Преображенский женский монастырь (Чебоксары), Владимирский собор
  (Новочебоксарск), Тихвинский Богородицкий женский монастырь (Цивильск).
- theatre (2): Чувашский драматический театр им. К. В. Иванова, Театр оперы и балета.
- monument (2): Памятник В. И. Чапаеву, Памятник Остапу Бендеру и Кисе Воробьянинову.
- square_street (3): Красная площадь, Бульвар купца Ефремова, Государева гора / Мариинский Посад.
- park_garden (5): Парк Победы, Лакреевский лес (ЦПКиО), Ельниковская роща (Новочебоксарск),
  Национальный парк «Чаваш вармане», Заповедник «Присурский».
- other (1): Национальная библиотека Чувашской Республики.

TOẠ ĐỘ — xác minh chéo (Yandex Maps org, sobory.ru «Координаты», komandirovka.ru GPS,
geometki.com, OpenStreetMap/Nominatim, 2026-07-28). Phạm vi Chuvashia: lat ~54.5–56.5,
lon ~46.0–48.5; tất cả toạ độ nằm trong phạm vi, KHÔNG đảo lat/lon:
  Свято-Троицкий мон. 56.151783,47.252857 (Yandex org 1111023774); Красная площадь
  56.146035,47.251367 (Yandex org 173679017495); Бульвар Ефремова 56.144692,47.251609
  (Yandex geo 11102901); Музей пива 56.144517,47.251882 (komandirovka GPS); Музей Чапаева
  56.116192,47.257546 (komandirovka GPS); Памятник Чапаеву 56.114971,47.258613 (geometki);
  Художественный музей 56.141126,47.261328 (komandirovka GPS); Драмтеатр им. Иванова
  56.145439,47.250749 (Yandex org 1116923127); Театр оперы и балета 56.144808,47.237517
  (Yandex org 1101196055); Успенская церковь 56.149961,47.252728 (sobory 04986); Церковь
  Михаила Архангела 56.151868,47.250034 (sobory 04987); Памятник Остапу Бендеру
  56.145239,47.252148 (Yandex org 99060888092); Парк Победы 56.147426,47.267840 (geometki);
  Лакреевский лес 56.117477,47.244434 (OSM rel 2739229); Нац. библиотека 56.127969,
  47.251986 (komandirovka GPS); Музей трактора 56.124326,47.284514 (komandirovka GPS);
  Музей вышивки 56.141326,47.249604 (OSM node 5842261207, ул. К. Маркса 32); Владимирский
  собор Новочебоксарск 56.107793,47.482470 (sobory 04988); Ельниковская роща 56.124456,
  47.475055 (OSM rel 2597709); Тихвинский мон. Цивильск 55.877097,47.473214 (Yandex org
  1761828163); Государева гора Мар. Посад 56.121287,47.739690 (OSM node 1937303725);
  НП «Чаваш Вармане» 54.828530,47.246880 (OSM rel 4759838); Заповедник «Присурский»
  54.991951,46.767026 (OSM rel 7376929); Спасо-Преображенский мон. 56.135090,47.230354
  (sobory 05007); Ибресинский этн. музей 55.302675,47.041869 (OSM node 9834578532).

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_chuvashia_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "chuvashia"
REGION_NAME_VI = "Cộng hòa Chuvashia"
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


RECORDS = []

# 1) Свято-Троицкий мужской монастырь (Чебоксары) ----------------------------------
RECORDS.append(rec(
    "holy-trinity-monastery-cheboksary",
    "Tu viện nam Chúa Ba Ngôi (Cheboksary)",
    "Свято-Троицкий православный мужской монастырь",
    "Holy Trinity Monastery (Cheboksary)",
    ["church"],
    56.151783, 47.252857,
    "Ул. Константина Иванова, 1, bên bờ Vịnh Cheboksary, trung tâm Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Được lập năm 1566 theo sắc lệnh của Sa hoàng Ivan Bạo chúa, đây là tu viện nam cổ nhất Cheboksary và một trong những trung tâm Chính Thống giáo lâu đời nhất vùng. Quần thể tường thành trắng, các nhà thờ mái vòm xanh nằm ngay bên bờ vịnh, sát trung tâm lịch sử.",
    "Tu viện nam Chúa Ba Ngôi là một trong những công trình tôn giáo lâu đời và giàu ý nghĩa nhất của Cheboksary. Được thành lập năm 1566 theo lệnh Sa hoàng Ivan Bạo chúa, tu viện ban đầu mang sứ mệnh truyền bá Chính Thống giáo trong cộng đồng người Chuvash, Mari và các dân tộc vùng Volga vừa sáp nhập vào nước Nga. Trải qua gần năm thế kỷ với nhiều lần cháy, tái thiết và bị đóng cửa dưới thời Xô Viết, tu viện hồi sinh từ đầu thập niên 1990 và nay là chốn tu tập sống động. Quần thể nằm nép mình bên bờ Vịnh Cheboksary, cửa sông Cheboksarka, với tường thành và tháp canh màu trắng bao quanh nhà thờ chính Chúa Ba Ngôi cùng nhà thờ Đức Mẹ Tolga và nhà thờ cổng. Những mái vòm hình củ hành xanh điểm sao vàng nổi bật trên nền trời và soi bóng xuống mặt nước, tạo nên một trong những khung hình đẹp nhất của thủ phủ. Với du khách, tu viện vừa là điểm chiêm ngưỡng kiến trúc Chính Thống giáo cổ, vừa là nơi cảm nhận bầu không khí trầm mặc, thanh tịnh ngay giữa lòng thành phố.",
    [
        "Tu viện nam cổ nhất Cheboksary, thành lập 1566 dưới thời Ivan Bạo chúa.",
        "Quần thể tường thành trắng và các nhà thờ mái vòm xanh soi bóng Vịnh Cheboksary.",
        "Gắn với lịch sử truyền bá Chính Thống giáo trong các dân tộc vùng Volga.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động; khuyến khích quyên góp).",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp lễ lớn của Chính Thống giáo.",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; nằm sát Vịnh Cheboksary nên dễ kết hợp dạo bờ kè và trung tâm.",
    },
    [
        {"title": "Wikipedia (RU) — Свято-Троицкий монастырь (Чебоксары)", "url": "https://ru.wikipedia.org/wiki/Свято-Троицкий_монастырь_(Чебоксары)"},
        {"title": "Yandex Maps — Свято-Троицкий мужской монастырь", "url": "https://yandex.ru/maps/org/svyato_troitskiy_muzhskoy_monastyr/1111023774/"},
    ],
    ["monastery", "church", "orthodox", "cheboksary", "architecture"],
    maps_org("https://yandex.ru/maps/org/svyato_troitskiy_muzhskoy_monastyr/1111023774/", "Holy Trinity Monastery", "Cheboksary"),
))

# 2) Красная площадь (Чебоксары) --------------------------------------------------
RECORDS.append(rec(
    "cheboksary-red-square",
    "Quảng trường Đỏ (Cheboksary)",
    "Красная площадь",
    "Red Square (Cheboksary)",
    ["square_street"],
    56.146035, 47.251367,
    "Красная площадь, bên bờ nam Vịnh Cheboksary, trung tâm Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Quảng trường trung tâm của Cheboksary trải dài bên bờ nam Vịnh Cheboksary, là sân khấu chính cho các lễ hội, hòa nhạc và sự kiện của cả nước cộng hòa. Từ đây có thể bao quát mặt vịnh, đài phun nước và những công trình biểu tượng của thành phố.",
    "Quảng trường Đỏ là trái tim sinh hoạt cộng đồng của Cheboksary, nằm ngay bên bờ nam Vịnh Cheboksary và nối liền với quần thể bờ kè, đài phun nước cùng cây cầu đi bộ biểu tượng. Đây là nơi tập trung của người dân trong những dịp trọng đại: lễ hội Ngày Cộng hòa Chuvashia, các buổi hòa nhạc ngoài trời, hội chợ, bắn pháo hoa và sân khấu lễ hội mùa đông. Không gian quảng trường thoáng rộng, lát đá, viền quanh là Bảo tàng Quốc gia Chuvash, các quán cà phê và bậc thang dẫn xuống mặt nước. Ban ngày, nơi đây là chốn dạo chơi, chụp ảnh và ngắm toàn cảnh vịnh với Tượng đài Mẹ Bảo Trợ ở phía xa; về đêm, ánh đèn và đài phun nước biến quảng trường thành điểm hẹn nhộn nhịp bậc nhất thành phố. Với du khách, Quảng trường Đỏ là điểm khởi đầu tự nhiên cho hành trình khám phá trung tâm lịch sử Cheboksary, khi hầu hết các điểm tham quan chính đều nằm trong tầm đi bộ.",
    [
        "Quảng trường trung tâm bên Vịnh Cheboksary — sân khấu chính của các lễ hội lớn.",
        "Điểm ngắm toàn cảnh vịnh, đài phun nước và Tượng đài Mẹ Bảo Trợ.",
        "Vị trí đắc địa, đi bộ tới Bảo tàng Quốc gia, bờ kè và cầu đi bộ.",
    ],
    {
        "hours_vi": "Không gian công cộng ngoài trời, tự do mọi thời điểm; đài phun nước hoạt động mùa ấm.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "30–60 phút (lâu hơn nếu có sự kiện).",
        "best_time_vi": "Chiều tối mùa hè để ngắm đèn và đài phun nước; các dịp lễ hội để cảm nhận không khí.",
        "tips_vi": "Kết hợp dạo bờ kè, cầu đi bộ và Bảo tàng Quốc gia Chuvash ngay cạnh; đông vào cuối tuần và ngày lễ.",
    },
    [
        {"title": "Wikipedia (RU) — Чебоксары", "url": "https://ru.wikipedia.org/wiki/Чебоксары"},
        {"title": "Yandex Maps — Красная площадь, Чебоксары", "url": "https://yandex.ru/maps/org/krasnaya_ploshchad/173679017495/"},
    ],
    ["square", "waterfront", "festival", "cheboksary", "free"],
    maps_org("https://yandex.ru/maps/org/krasnaya_ploshchad/173679017495/", "Red Square", "Cheboksary"),
))

# 3) Бульвар купца Ефремова (Чебоксарский Арбат) -----------------------------------
RECORDS.append(rec(
    "yefremov-boulevard",
    "Đại lộ đi bộ thương gia Yefremov (Arbat Cheboksary)",
    "Бульвар купца Ефремова",
    "Merchant Yefremov Boulevard (Cheboksary Arbat)",
    ["square_street"],
    56.144692, 47.251609,
    "Бульвар купца Ефремова, trung tâm lịch sử Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Con phố đi bộ được ví như 'Arbat của Cheboksary', mang tên gia đình thương gia giàu có Yefremov. Hai bên là những dinh thự và cửa hiệu cổ thế kỷ 19–20, xen kẽ quán cà phê, tượng nghệ thuật và điểm mua đồ lưu niệm.",
    "Bульвар купца Ефремова là tuyến phố đi bộ duyên dáng và giàu chất lịch sử bậc nhất Cheboksary, thường được người dân gọi thân mật là 'Arbat' của thành phố. Con phố mang tên dòng họ Yefremov — những thương gia lừng lẫy từng làm giàu và để lại dấu ấn qua hàng loạt biệt thự, cửa hiệu bằng đá và gạch nung dọc hai bên đường. Ngày nay, các tòa nhà cổ được gìn giữ và cải tạo thành bảo tàng, phòng tranh, tiệm cà phê và cửa hàng thủ công, tạo nên một không gian tản bộ ấm cúng nối trung tâm hành chính với khu vực Vịnh Cheboksary. Dọc phố còn có những bức tượng đồng, ghế nghệ thuật và tiểu cảnh để du khách chụp ảnh; vào mùa ấm, nghệ sĩ đường phố và các gian hàng nhỏ càng làm không khí thêm sôi động. Đây là nơi lý tưởng để cảm nhận nhịp sống thong thả của Cheboksary, ngắm kiến trúc thương nhân xưa và tìm mua những món quà lưu niệm mang đậm bản sắc Chuvash.",
    [
        "Phố đi bộ 'Arbat' của Cheboksary với dinh thự, cửa hiệu thương gia thế kỷ 19–20.",
        "Nhiều tượng đồng, tiểu cảnh nghệ thuật và điểm chụp ảnh dọc tuyến.",
        "Tập trung quán cà phê, phòng tranh và cửa hàng lưu niệm thủ công Chuvash.",
    ],
    {
        "hours_vi": "Phố đi bộ ngoài trời, tự do mọi lúc; quán xá hoạt động chủ yếu ban ngày tới tối.",
        "ticket_vi": "Miễn phí (dạo phố).",
        "duration_vi": "30–60 phút.",
        "best_time_vi": "Chiều tối mùa ấm khi phố nhộn nhịp; cuối tuần thường có nghệ sĩ đường phố.",
        "tips_vi": "Kết hợp đi xuống Quảng trường Đỏ và bờ Vịnh Cheboksary; ghé các tiệm thủ công tìm đồ thêu, quà lưu niệm.",
    },
    [
        {"title": "Wikipedia (RU) — Чебоксары", "url": "https://ru.wikipedia.org/wiki/Чебоксары"},
        {"title": "Yandex Maps — Бульвар купца Ефремова", "url": "https://yandex.com/maps/45/cheboksary/geo/bulvar_kuptsa_yefremova/11102901/"},
    ],
    ["pedestrian-street", "historic-architecture", "cheboksary", "shopping", "free"],
    maps_org("https://yandex.com/maps/45/cheboksary/geo/bulvar_kuptsa_yefremova/11102901/", "Merchant Yefremov Boulevard", "Cheboksary"),
))

# 4) Музей истории пива (Чебоксары) ------------------------------------------------
RECORDS.append(rec(
    "cheboksary-beer-museum",
    "Bảo tàng lịch sử bia (Cheboksary)",
    "Музей истории пива",
    "Museum of Beer History (Cheboksary)",
    ["museum"],
    56.144517, 47.251882,
    "Бульвар купца Ефремова, 6, trung tâm Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Bảo tàng bia độc đáo mở cửa từ năm 1997, tôn vinh truyền thống nấu bia và trồng hoa bia của Chuvashia — vùng đất từng nổi tiếng với hoa bia (hop) bậc nhất nước Nga. Trưng bày dụng cụ nấu bia cổ, lịch sử ngành và có cả quầy nếm thử.",
    "Nằm trên phố đi bộ Yefremov, Bảo tàng lịch sử bia là một trong những điểm tham quan độc đáo và vui nhộn nhất Cheboksary. Chuvashia vốn được mệnh danh là 'xứ sở hoa bia' của nước Nga, nơi cây hoa bia được trồng và chế biến từ lâu đời, nên một bảo tàng dành riêng cho bia ở đây mang ý nghĩa văn hóa rất rõ. Mở cửa năm 1997, bảo tàng dẫn khách qua toàn bộ câu chuyện của thức uống này: từ nghề nấu bia dân gian của người Chuvash với những công cụ gỗ mộc mạc, qua thời kỳ công nghiệp hóa, cho tới các thương hiệu bia hiện đại của vùng. Du khách được xem thùng ủ, cối, dụng cụ đo, nhãn mác, áp phích cổ và mô hình tái hiện quy trình sản xuất. Điểm nhấn được nhiều người thích thú là quầy nếm thử, nơi có thể thưởng thức một vài loại bia địa phương ngay trong không gian bảo tàng. Đây là một trải nghiệm nhẹ nhàng, đậm màu sắc dân dã, giúp du khách hiểu thêm một khía cạnh rất đời thường nhưng đặc trưng của văn hóa Chuvash.",
    [
        "Một trong số ít bảo tàng bia ở Nga, mở cửa từ năm 1997.",
        "Gắn với truyền thống trồng hoa bia và nấu bia lâu đời của Chuvashia.",
        "Có quầy nếm thử bia địa phương ngay trong bảo tàng.",
    ],
    {
        "hours_vi": "Thường mở cửa hằng ngày, giờ hành chính đến chiều tối; nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; nếm thử bia có thể tính phí riêng.",
        "duration_vi": "Khoảng 45 phút–1 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà); tiện ghé khi dạo phố đi bộ.",
        "tips_vi": "Nằm ngay trên phố Yefremov, dễ kết hợp với dạo bờ vịnh; đồ nếm thử dành cho người trên 18 tuổi.",
    },
    [
        {"title": "Komandirovka.ru — Музей пива, Чебоксары", "url": "https://www.komandirovka.ru/sights/cheboksary/muzey-piva/"},
        {"title": "Wikipedia (RU) — Чебоксары", "url": "https://ru.wikipedia.org/wiki/Чебоксары"},
    ],
    ["museum", "beer", "culture", "cheboksary", "gastronomy"],
    maps_text("Музей истории пива", "Чебоксары", "Museum of Beer History", "Cheboksary", 56.144517, 47.251882),
))

# 5) Музей В. И. Чапаева (Чебоксары) -----------------------------------------------
RECORDS.append(rec(
    "chapayev-museum",
    "Bảo tàng V. I. Chapayev (Cheboksary)",
    "Музей В. И. Чапаева",
    "V. I. Chapayev Museum (Cheboksary)",
    ["museum"],
    56.116192, 47.257546,
    "Проспект Ленина, 46А (сквер имени Чапаева), Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Bảo tàng dành riêng cho Vasily Chapayev — vị chỉ huy huyền thoại của Hồng quân trong Nội chiến Nga, sinh tại làng Budaika nay thuộc Cheboksary. Mở cửa năm 1974, bảo tàng nằm trong công viên Chapayev cùng tượng đài và ngôi nhà gỗ tưởng niệm.",
    "Vasily Ivanovich Chapayev là một trong những nhân vật nổi tiếng nhất bước ra từ vùng đất Chuvashia: vị chỉ huy sư đoàn Hồng quân dũng cảm thời Nội chiến Nga, sau này trở thành huyền thoại qua sách, phim và vô số giai thoại dân gian. Ông sinh năm 1887 tại làng Budaika, nay đã nằm trong địa phận thành phố Cheboksary, và chính tại đây, năm 1974, một bảo tàng tưởng niệm đã được mở để tôn vinh ông. Tòa nhà bảo tàng mang phong cách kiến trúc Xô Viết hiện đại, trưng bày tài liệu, ảnh, vũ khí, quân phục và hiện vật kể lại cuộc đời người chỉ huy từ tuổi thơ nghèo khó đến những trận đánh vang danh và cái chết bi tráng năm 1919. Trong khuôn viên công viên bao quanh còn có tượng đài Chapayev cưỡi ngựa oai phong và một ngôi nhà gỗ tái dựng gợi nhớ nếp sống làng quê nơi ông sinh ra. Với du khách, đây là điểm dừng chân để hiểu thêm về một chương lịch sử đầy biến động của nước Nga qua số phận một con người cụ thể.",
    [
        "Tưởng niệm Vasily Chapayev — chỉ huy Hồng quân huyền thoại, sinh tại Cheboksary (làng Budaika).",
        "Mở cửa năm 1974, trưng bày tài liệu, vũ khí, quân phục và hiện vật thời Nội chiến.",
        "Nằm trong công viên có tượng đài Chapayev cưỡi ngựa và nhà gỗ tưởng niệm.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nghỉ thứ Hai. Nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "Khoảng 45 phút–1 giờ (kể cả dạo công viên).",
        "best_time_vi": "Quanh năm; mùa ấm để kết hợp dạo công viên và ngắm tượng đài.",
        "tips_vi": "Công viên và tượng đài ngoài trời xem tự do; kết hợp tham quan khi di chuyển dọc проспект Ленина.",
    },
    [
        {"title": "Komandirovka.ru — Музей В. И. Чапаева", "url": "https://www.komandirovka.ru/sights/cheboksary/muzey-v-i-chapaeva/"},
        {"title": "Wikipedia (RU) — Чапаев, Василий Иванович", "url": "https://ru.wikipedia.org/wiki/Чапаев,_Василий_Иванович"},
    ],
    ["museum", "history", "chapayev", "cheboksary", "soviet"],
    maps_text("Музей В. И. Чапаева", "Чебоксары", "V. I. Chapayev Museum", "Cheboksary", 56.116192, 47.257546),
))

# 6) Памятник В. И. Чапаеву (Чебоксары) --------------------------------------------
RECORDS.append(rec(
    "chapayev-monument",
    "Tượng đài V. I. Chapayev (Cheboksary)",
    "Памятник В. И. Чапаеву",
    "Monument to V. I. Chapayev (Cheboksary)",
    ["monument"],
    56.114971, 47.258613,
    "Сквер имени Чапаева, проспект Ленина, Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Tượng đài Chapayev cưỡi ngựa xông trận đầy khí thế, đặt trong công viên mang tên ông ngay cạnh bảo tàng. Đây là một trong những biểu tượng dễ nhận biết và điểm chụp ảnh quen thuộc ở khu vực phía nam trung tâm Cheboksary.",
    "Nằm ngay trong công viên Chapayev bên cạnh bảo tàng cùng tên, tượng đài Vasily Chapayev là một điểm nhấn thị giác giàu khí thế của Cheboksary. Tác phẩm khắc họa vị chỉ huy Hồng quân trong tư thế cưỡi ngựa lao về phía trước, tay vung kiếm, áo choàng bay trong gió — hình ảnh gói trọn tinh thần quả cảm và sự lãng mạn bi tráng gắn với huyền thoại về ông. Chapayev sinh ra tại chính vùng đất này, nên với người dân Chuvashia, tượng đài không chỉ tôn vinh một nhân vật lịch sử mà còn là niềm tự hào về người con của quê hương. Bệ tượng và khoảng sân xung quanh là nơi người dân dạo chơi, chụp ảnh và đặt hoa vào các dịp kỷ niệm. Cùng với bảo tàng và ngôi nhà gỗ tưởng niệm kề bên, tượng đài tạo thành một cụm di tích thống nhất, thuận tiện cho du khách muốn tìm hiểu về Chapayev và một giai đoạn đầy biến động của lịch sử Nga.",
    [
        "Tượng Chapayev cưỡi ngựa xông trận — biểu tượng dễ nhận biết ở nam trung tâm Cheboksary.",
        "Nằm ngay cạnh Bảo tàng Chapayev, tạo thành cụm di tích thống nhất.",
        "Điểm chụp ảnh và đặt hoa quen thuộc trong các dịp kỷ niệm.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi thời điểm.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "15–20 phút.",
        "best_time_vi": "Ban ngày để ngắm rõ chi tiết; mùa ấm để kết hợp dạo công viên.",
        "tips_vi": "Kết hợp vào thăm Bảo tàng Chapayev ngay cạnh; nằm trên проспект Ленина, dễ tiếp cận bằng xe buýt.",
    },
    [
        {"title": "Geometki.com — Памятник Чапаеву, Чебоксары", "url": "https://geometki.com/places/65cfbcfb8f873"},
        {"title": "Wikipedia (RU) — Чапаев, Василий Иванович", "url": "https://ru.wikipedia.org/wiki/Чапаев,_Василий_Иванович"},
    ],
    ["monument", "chapayev", "cheboksary", "soviet", "free"],
    maps_text("Памятник В. И. Чапаеву", "Чебоксары", "Monument to V. I. Chapayev", "Cheboksary", 56.114971, 47.258613),
))

# 7) Чувашский государственный художественный музей --------------------------------
RECORDS.append(rec(
    "chuvash-art-museum",
    "Bảo tàng Mỹ thuật Quốc gia Chuvash",
    "Чувашский государственный художественный музей",
    "Chuvash State Art Museum",
    ["museum"],
    56.141126, 47.261328,
    "Ул. Калинина, 60, Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Bảo tàng mỹ thuật lớn nhất Chuvashia, hình thành từ năm 1939, lưu giữ bộ sưu tập phong phú tranh và tác phẩm nghệ thuật Nga, Xô Viết và Chuvash. Là trung tâm nghệ thuật hàng đầu của nước cộng hòa với nhiều triển lãm luân phiên.",
    "Bảo tàng Mỹ thuật Quốc gia Chuvash là kho tàng nghệ thuật lớn và quan trọng nhất của nước cộng hòa. Khởi nguồn từ một bộ sưu tập tranh trong Bảo tàng Quốc gia Chuvash cuối thập niên 1930, đến năm 1939 phòng tranh này ra đời và dần phát triển thành một bảo tàng mỹ thuật độc lập với hàng chục nghìn hiện vật. Các bộ sưu tập trải rộng từ hội họa và điêu khắc cổ điển Nga, nghệ thuật thời Xô Viết, cho tới tác phẩm của các họa sĩ Chuvash — những người đã đưa màu sắc, hoa văn và tinh thần dân tộc vào nghệ thuật tạo hình hiện đại. Bảo tàng còn lưu giữ đồ họa, nghệ thuật trang trí ứng dụng và các tác phẩm nghệ thuật dân gian, giúp khách hình dung dòng chảy thẩm mỹ của vùng đất này. Bên cạnh trưng bày thường xuyên, nơi đây liên tục tổ chức triển lãm chuyên đề, sự kiện giáo dục và giao lưu nghệ thuật. Với du khách yêu hội họa, đây là điểm đến để cảm nhận chiều sâu văn hóa của Chuvashia qua ngôn ngữ của màu sắc và hình khối.",
    [
        "Bảo tàng mỹ thuật lớn nhất Chuvashia, hình thành từ năm 1939.",
        "Sưu tập hội họa, điêu khắc Nga, Xô Viết và các họa sĩ Chuvash tiêu biểu.",
        "Thường xuyên tổ chức triển lãm chuyên đề và sự kiện nghệ thuật.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nghỉ thứ Hai. Nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; phí thêm cho triển lãm chuyên đề và tour hướng dẫn.",
        "duration_vi": "1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Kiểm tra lịch triển lãm trước khi đến; nằm ở trung tâm, dễ kết hợp với các điểm gần Vịnh Cheboksary.",
    },
    [
        {"title": "Komandirovka.ru — Чувашский государственный художественный музей", "url": "https://www.komandirovka.ru/sights/cheboksary/chuvashskiy-gosudarstvennyiy-hudojestvennyiy-muzey/"},
        {"title": "Wikipedia (RU) — Чувашский государственный художественный музей", "url": "https://ru.wikipedia.org/wiki/Чувашский_государственный_художественный_музей"},
    ],
    ["museum", "art", "painting", "cheboksary", "culture"],
    maps_text("Чувашский государственный художественный музей", "Чебоксары", "Chuvash State Art Museum", "Cheboksary", 56.141126, 47.261328),
))

# 8) Чувашский драматический театр им. К. В. Иванова -------------------------------
RECORDS.append(rec(
    "chuvash-drama-theatre",
    "Nhà hát kịch Chuvash mang tên K. V. Ivanov",
    "Чувашский государственный академический драматический театр имени К. В. Иванова",
    "Chuvash Academic Drama Theatre named after K. V. Ivanov",
    ["theatre"],
    56.145439, 47.250749,
    "Красная площадь, 7, Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Nhà hát kịch quốc gia bằng tiếng Chuvash, có gốc rễ từ năm 1918 và mang tên nhà thơ dân tộc Konstantin Ivanov. Đây là trung tâm gìn giữ ngôn ngữ, kịch nghệ và bản sắc Chuvash, tọa lạc ngay bên Quảng trường Đỏ.",
    "Nhà hát kịch Chuvash mang tên Konstantin Ivanov là biểu tượng của sân khấu và ngôn ngữ dân tộc Chuvash. Được thành lập từ năm 1918, ngay sau Cách mạng, nhà hát ra đời với sứ mệnh xây dựng một nền kịch nghệ chuyên nghiệp bằng chính tiếng Chuvash — điều có ý nghĩa lớn trong việc bảo tồn và phát triển văn hóa dân tộc. Nhà hát mang tên Konstantin Ivanov, nhà thơ được coi là người đặt nền móng cho văn học Chuvash cổ điển với trường ca 'Narspi'. Trải qua hơn một thế kỷ, đoàn kịch đã dàn dựng hàng trăm vở diễn: từ kịch dân gian, sử thi Chuvash, kịch kinh điển thế giới cho tới tác phẩm đương đại, nhiều vở được trình diễn bằng tiếng Chuvash với phụ đề hoặc tai nghe phiên dịch. Tòa nhà nhà hát bề thế nằm ngay bên Quảng trường Đỏ, trung tâm thành phố, là một điểm nhấn kiến trúc và văn hóa. Với du khách, một buổi tối tại đây là cơ hội hiếm có để tiếp xúc trực tiếp với tiếng nói và tâm hồn của người Chuvash qua nghệ thuật sân khấu.",
    [
        "Nhà hát kịch quốc gia bằng tiếng Chuvash, có gốc từ năm 1918.",
        "Mang tên Konstantin Ivanov — nhà thơ đặt nền móng văn học Chuvash ('Narspi').",
        "Tọa lạc ngay bên Quảng trường Đỏ, trung tâm gìn giữ bản sắc dân tộc.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch mùa, thường buổi tối và cuối tuần; phòng vé mở ban ngày.",
        "ticket_vi": "Vé giá phải chăng, thay đổi theo vở và hạng ghế.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ.",
        "best_time_vi": "Mùa diễn từ thu đến xuân; xem lịch trên trang chính thức của nhà hát.",
        "tips_vi": "Nhiều vở diễn bằng tiếng Chuvash — hỏi trước về phụ đề/phiên dịch; đặt vé sớm cho các vở nổi tiếng.",
    },
    [
        {"title": "Wikipedia (RU) — Чувашский драматический театр имени К. В. Иванова", "url": "https://ru.wikipedia.org/wiki/Чувашский_драматический_театр_имени_К._В._Иванова"},
        {"title": "Yandex Maps — Чувашский академический драматический театр", "url": "https://yandex.com/maps/org/chuvashskiy_akademicheskiy_dramaticheskiy_teatr_imeni_konstantina_ivanova/1116923127/"},
    ],
    ["theatre", "drama", "chuvash-language", "cheboksary", "culture"],
    maps_org("https://yandex.com/maps/org/chuvashskiy_akademicheskiy_dramaticheskiy_teatr_imeni_konstantina_ivanova/1116923127/", "Chuvash Academic Drama Theatre", "Cheboksary"),
))

# 9) Чувашский государственный театр оперы и балета -------------------------------
RECORDS.append(rec(
    "chuvash-opera-ballet-theatre",
    "Nhà hát Opera và Ballet Quốc gia Chuvash",
    "Чувашский государственный театр оперы и балета",
    "Chuvash State Opera and Ballet Theatre",
    ["theatre"],
    56.144808, 47.237517,
    "Московский проспект, 1, bên bờ tây Vịnh Cheboksary, Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Nhà hát opera và ballet của Chuvashia, hoạt động từ năm 1959, là sân khấu chính cho nhạc kịch cổ điển của nước cộng hòa. Nơi đây tổ chức Liên hoan Ballet quốc tế và Liên hoan Opera thường niên, trong tòa nhà nổi bật bên bờ vịnh.",
    "Nhà hát Opera và Ballet Quốc gia Chuvash là ngôi đền của nghệ thuật hàn lâm âm nhạc và vũ đạo ở Cheboksary. Ra đời năm 1959 và trở thành nhà hát opera–ballet độc lập vào cuối thập niên 1960, đây là nơi hội tụ các nghệ sĩ thanh nhạc và vũ công của nước cộng hòa. Chương trình biểu diễn trải rộng từ những vở opera và ballet kinh điển của Nga và thế giới — như các tác phẩm của Tchaikovsky, Verdi, Puccini — cho tới những vở mang màu sắc dân tộc Chuvash. Nhà hát đặc biệt nổi tiếng với hai sự kiện thường niên thu hút nghệ sĩ khắp nơi: Liên hoan Ballet quốc tế và Liên hoan Opera mang tên các nghệ sĩ tiêu biểu. Tòa nhà nhà hát bề thế, mái vươn rộng, tọa lạc trên gò cao bên bờ tây Vịnh Cheboksary, từ đó có thể ngắm mặt nước và trung tâm thành phố. Với du khách, thưởng thức một đêm opera hay ballet ở đây là cách sang trọng để hòa vào đời sống văn hóa của Cheboksary, đồng thời chiêm ngưỡng một trong những công trình biểu tượng của thành phố.",
    [
        "Nhà hát opera–ballet của Chuvashia, hoạt động từ năm 1959.",
        "Tổ chức Liên hoan Ballet quốc tế và Liên hoan Opera thường niên.",
        "Tòa nhà biểu tượng trên gò cao bên bờ tây Vịnh Cheboksary.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch mùa, chủ yếu buổi tối và cuối tuần; phòng vé mở ban ngày.",
        "ticket_vi": "Vé thay đổi theo vở diễn và hạng ghế, nhìn chung phải chăng.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ.",
        "best_time_vi": "Mùa diễn thu–xuân; đặc biệt vào các kỳ liên hoan opera/ballet.",
        "tips_vi": "Đặt vé trước cho mùa liên hoan; đến sớm để ngắm cảnh vịnh từ khu vực nhà hát và gửi áo khoác.",
    },
    [
        {"title": "Wikipedia (RU) — Чувашский театр оперы и балета", "url": "https://ru.wikipedia.org/wiki/Чувашский_театр_оперы_и_балета"},
        {"title": "Yandex Maps — Театр оперы и балета, Чебоксары", "url": "https://yandex.com/maps/org/chuvash_state_opera_and_ballet_theatre/1101196055/"},
    ],
    ["theatre", "opera", "ballet", "cheboksary", "culture"],
    maps_org("https://yandex.com/maps/org/chuvash_state_opera_and_ballet_theatre/1101196055/", "Chuvash State Opera and Ballet Theatre", "Cheboksary"),
))

# 10) Успенская церковь (Чебоксары) -----------------------------------------------
RECORDS.append(rec(
    "cheboksary-assumption-church",
    "Nhà thờ Đức Mẹ An Giấc (Uspenskaya, Cheboksary)",
    "Успенская церковь",
    "Assumption (Uspenskaya) Church, Cheboksary",
    ["church"],
    56.149961, 47.252728,
    "Ул. Митрополита Даниила (bờ Vịnh Cheboksary), Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Ngôi nhà thờ baroque xây năm 1763, một trong những công trình tôn giáo cổ đẹp nhất Cheboksary, nằm ngay bên bờ Vịnh Cheboksary. Từng bị ngập một phần khi hồ chứa dâng nước, nhà thờ vẫn giữ được dáng vẻ duyên dáng đặc trưng.",
    "Nhà thờ Đức Mẹ An Giấc (Uspenskaya) là một trong những công trình tôn giáo cổ kính và giàu sức gợi nhất của Cheboksary. Được xây dựng năm 1763 theo phong cách baroque tỉnh lẻ, nhà thờ có khối chính thanh thoát cùng tháp chuông vươn cao, từng là một phần của quần thể tu viện cổ ven sông Volga. Khi hồ chứa của nhà máy thủy điện Cheboksary dâng nước vào cuối thế kỷ 20, mực nước cao đã nhấn chìm phần chân móng và làm thay đổi cảnh quan quanh nhà thờ; để cứu công trình, người ta phải đắp đê và gia cố, khiến nay nhà thờ như đứng ngay sát mép Vịnh Cheboksary, tạo nên một hình ảnh vừa nên thơ vừa có phần khác thường. Bất chấp những thăng trầm, Uspenskaya vẫn giữ được vẻ đẹp kiến trúc đặc trưng và là điểm nhấn tôn giáo trong bức tranh toàn cảnh bờ vịnh. Với du khách dạo bờ kè, ngôi nhà thờ trắng bên làn nước là một khung hình đáng nhớ và là chứng nhân cho lịch sử biến đổi của thành phố.",
    [
        "Nhà thờ baroque xây năm 1763 — một trong những công trình cổ đẹp nhất Cheboksary.",
        "Nằm ngay bên bờ Vịnh Cheboksary, từng bị ảnh hưởng khi hồ chứa dâng nước.",
        "Khung hình nên thơ trong toàn cảnh bờ vịnh, gắn với lịch sử biến đổi của thành phố.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ; có thể ngắm kiến trúc từ bên ngoài bất cứ lúc nào.",
        "ticket_vi": "Miễn phí (nơi thờ phụng; khuyến khích quyên góp).",
        "duration_vi": "20–30 phút.",
        "best_time_vi": "Ban ngày để ngắm rõ kiến trúc và cảnh vịnh; hoàng hôn cho ảnh đẹp.",
        "tips_vi": "Nữ nên trùm khăn khi vào trong; kết hợp dạo bờ kè Vịnh Cheboksary ngay cạnh.",
    },
    [
        {"title": "Sobory.ru — Церковь Успения Пресвятой Богородицы, Чебоксары", "url": "https://sobory.ru/article/?object=04986"},
        {"title": "Wikipedia (RU) — Чебоксары", "url": "https://ru.wikipedia.org/wiki/Чебоксары"},
    ],
    ["church", "orthodox", "baroque", "cheboksary", "waterfront"],
    maps_text("Успенская церковь", "Чебоксары", "Assumption Church", "Cheboksary", 56.149961, 47.252728),
))

# 11) Церковь Михаила Архангела (Чебоксары) ---------------------------------------
RECORDS.append(rec(
    "cheboksary-archangel-michael-church",
    "Nhà thờ Tổng lãnh thiên thần Mikhail (Cheboksary)",
    "Церковь Михаила Архангела",
    "Church of Archangel Michael, Cheboksary",
    ["church"],
    56.151868, 47.250034,
    "Ул. Сеспеля, 20 (khu trung tâm lịch sử), Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Nhà thờ đá cổ xây năm 1702, thuộc hàng công trình tôn giáo lâu đời nhất Cheboksary. Với khối kiến trúc cân đối kiểu Nga thế kỷ 18 và vị trí gần Vịnh Cheboksary, đây là một điểm nhấn của khu trung tâm lịch sử.",
    "Nhà thờ Tổng lãnh thiên thần Mikhail là một trong những công trình đá cổ nhất còn lại của Cheboksary, được xây dựng năm 1702 — chỉ ít lâu sau Nhà thờ Vvedensky nổi tiếng. Ngôi nhà thờ mang những đặc trưng của kiến trúc nhà thờ Nga đầu thế kỷ 18: khối chính vững chãi đội mái vòm, gắn với gian ăn (trapeznaya) và tháp chuông, tường được trang trí bằng những chi tiết gạch mộc mạc nhưng cân đối. Trải qua các thời kỳ thăng trầm, kể cả giai đoạn bị đóng cửa dưới thời Xô Viết, nhà thờ đã được phục hồi và trở lại đời sống phụng vụ. Nằm trong khu trung tâm lịch sử, không xa Vịnh Cheboksary và các nhà thờ cổ khác, công trình góp phần tạo nên quần thể kiến trúc tôn giáo đặc sắc của thành phố. Với du khách quan tâm tới lịch sử và kiến trúc Chính Thống giáo, đây là một điểm dừng chân yên tĩnh, giàu chiều sâu thời gian, dễ kết hợp trong hành trình khám phá trung tâm Cheboksary.",
    [
        "Nhà thờ đá cổ xây năm 1702 — thuộc hàng lâu đời nhất Cheboksary.",
        "Kiến trúc nhà thờ Nga đầu thế kỷ 18 với khối chính, gian ăn và tháp chuông.",
        "Nằm trong khu trung tâm lịch sử, gần Vịnh Cheboksary và các nhà thờ cổ khác.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ; ngắm kiến trúc bên ngoài tự do.",
        "ticket_vi": "Miễn phí (nơi thờ phụng; khuyến khích quyên góp).",
        "duration_vi": "20–30 phút.",
        "best_time_vi": "Ban ngày để ngắm kiến trúc; giờ lễ để cảm nhận không khí phụng vụ.",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; kết hợp tham quan các nhà thờ cổ và bờ vịnh gần đó.",
    },
    [
        {"title": "Sobory.ru — Церковь Михаила Архангела, Чебоксары", "url": "https://sobory.ru/article/?object=04987"},
        {"title": "Wikipedia (RU) — Чебоксары", "url": "https://ru.wikipedia.org/wiki/Чебоксары"},
    ],
    ["church", "orthodox", "history", "cheboksary", "architecture"],
    maps_text("Церковь Михаила Архангела", "Чебоксары", "Church of Archangel Michael", "Cheboksary", 56.151868, 47.250034),
))

# 12) Памятник Остапу Бендеру и Кисе Воробьянинову (Чебоксары) --------------------
RECORDS.append(rec(
    "ostap-bender-monument",
    "Tượng đài Ostap Bender và Kisa Vorobyaninov (Cheboksary)",
    "Памятник Остапу Бендеру и Кисе Воробьянинову",
    "Monument to Ostap Bender and Kisa Vorobyaninov (Cheboksary)",
    ["monument"],
    56.145239, 47.252148,
    "Bульвар купца Ефремова (khu trung tâm), Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Nhóm tượng đồng vui nhộn khắc họa hai nhân vật Ostap Bender và Kisa Vorobyaninov trong tiểu thuyết trào phúng kinh điển 'Mười hai chiếc ghế'. Cheboksary được nhắc tới trong tác phẩm, khiến bức tượng thành điểm chụp ảnh yêu thích trên phố đi bộ.",
    "Trên phố đi bộ Yefremov ở trung tâm Cheboksary có một nhóm tượng đồng khiến ai đi qua cũng mỉm cười: Ostap Bender và Kisa Vorobyaninov — hai nhân vật chính trong tiểu thuyết trào phúng bất hủ 'Mười hai chiếc ghế' của Ilya Ilf và Yevgeny Petrov. Cheboksary được nhắc đến trong hành trình phiêu lưu của hai gã săn kho báu, và thành phố đã dựng bức tượng này như một lời chào hóm hỉnh gửi tới tác phẩm văn học được nhiều thế hệ độc giả Nga yêu thích. Tượng khắc họa Ostap Bender lịch lãm, tự tin bên cạnh Kisa lúng túng, với những chi tiết sinh động gợi lại tinh thần châm biếm dí dỏm của cuốn sách. Đây là một trong những điểm chụp ảnh vui nhộn nhất Cheboksary: du khách thường tạo dáng bắt tay, khoác vai hay ngồi cạnh các nhân vật. Bức tượng cũng cho thấy nét duyên của Cheboksary — một thành phố biết pha trộn giữa di sản nghiêm trang và sự hài hước gần gũi, đời thường.",
    [
        "Nhóm tượng đồng về hai nhân vật trong tiểu thuyết trào phúng 'Mười hai chiếc ghế'.",
        "Cheboksary được nhắc đến trong tác phẩm — bức tượng như lời chào hóm hỉnh.",
        "Điểm chụp ảnh vui nhộn bậc nhất trên phố đi bộ Yefremov.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi thời điểm.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "10–15 phút.",
        "best_time_vi": "Ban ngày hoặc chiều tối khi phố đi bộ nhộn nhịp.",
        "tips_vi": "Nằm ngay trên phố Yefremov, kết hợp dạo phố và ngắm kiến trúc thương gia; tạo dáng chụp ảnh cùng tượng.",
    },
    [
        {"title": "Yandex Maps — Памятник Остапу Бендеру и Кисе Воробьянинову", "url": "https://yandex.com/maps/org/ostap_bender_i_kisa_vorobyaninov/99060888092/"},
        {"title": "Wikipedia (RU) — Двенадцать стульев", "url": "https://ru.wikipedia.org/wiki/Двенадцать_стульев"},
    ],
    ["monument", "literature", "sculpture", "cheboksary", "photo-spot"],
    maps_org("https://yandex.com/maps/org/ostap_bender_i_kisa_vorobyaninov/99060888092/", "Monument to Ostap Bender and Kisa Vorobyaninov", "Cheboksary"),
))

# 13) Парк Победы (Мемориальный парк «Победа», Чебоксары) -------------------------
RECORDS.append(rec(
    "cheboksary-victory-park",
    "Công viên Chiến Thắng (Cheboksary)",
    "Мемориальный парк «Победа»",
    "Victory Park (Cheboksary)",
    ["park_garden", "monument"],
    56.147426, 47.267840,
    "Ул. Юрия Гагарина (bờ cao sông Volga), Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Công viên tưởng niệm trên gò cao nhìn ra sông Volga, với Ngọn lửa Vĩnh cửu, đài tưởng niệm các chiến sĩ hy sinh, khu trưng bày khí tài quân sự và nhà nguyện. Đây vừa là nơi tưởng niệm trang nghiêm vừa là điểm ngắm cảnh Volga tuyệt đẹp.",
    "Công viên Chiến Thắng là một trong những không gian tưởng niệm quan trọng và giàu cảm xúc nhất của Cheboksary, nằm trên gò đất cao bên bờ sông Volga. Trung tâm của công viên là đài tưởng niệm cùng Ngọn lửa Vĩnh cửu, tôn vinh những người con Chuvashia đã ngã xuống trong Chiến tranh Vệ quốc Vĩ đại. Từ quảng trường tưởng niệm, một trục cảnh quan trải dài với tượng đài Người Mẹ tiễn con ra trận, các tấm bia khắc tên và không gian trang nghiêm để đặt hoa. Trong khuôn viên còn có khu trưng bày khí tài quân sự ngoài trời — xe tăng, pháo, tên lửa — được nhiều gia đình và trẻ em thích thú tham quan, cùng nhà nguyện nhỏ mang tính tưởng niệm. Điều khiến công viên đặc biệt hấp dẫn du khách là vị trí trên bờ cao: từ đây có thể phóng tầm mắt ra dòng Volga mênh mông và cảnh quan hai bên bờ, đặc biệt đẹp vào lúc hoàng hôn. Đây là nơi hội tụ ba giá trị: tưởng niệm lịch sử, giáo dục thế hệ trẻ và thưởng ngoạn thiên nhiên.",
    [
        "Đài tưởng niệm và Ngọn lửa Vĩnh cửu tôn vinh chiến sĩ Chuvashia thời Thế chiến II.",
        "Khu trưng bày khí tài quân sự ngoài trời: xe tăng, pháo, tên lửa.",
        "Điểm ngắm sông Volga tuyệt đẹp từ bờ cao, đặc biệt vào hoàng hôn.",
    ],
    {
        "hours_vi": "Công viên ngoài trời, mở cửa tự do; khu trưng bày khí tài xem tự do ban ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "45 phút–1,5 giờ.",
        "best_time_vi": "Chiều tà để ngắm hoàng hôn trên Volga; dịp 9/5 có nhiều hoạt động tưởng niệm.",
        "tips_vi": "Mang giày thoải mái để dạo dốc; giữ thái độ trang nghiêm ở khu tưởng niệm; tuyệt vời để ngắm toàn cảnh sông.",
    },
    [
        {"title": "Geometki.com — Парк Победы, Чебоксары", "url": "https://geometki.com/places/65cfbd0509cbd"},
        {"title": "Wikipedia (RU) — Чебоксары", "url": "https://ru.wikipedia.org/wiki/Чебоксары"},
    ],
    ["park", "memorial", "war-memorial", "cheboksary", "viewpoint"],
    maps_text("Мемориальный парк Победа", "Чебоксары", "Victory Park", "Cheboksary", 56.147426, 47.267840),
))

# 14) Лакреевский лес (ЦПКиО, Чебоксары) ------------------------------------------
RECORDS.append(rec(
    "lakreevsky-forest-park",
    "Rừng công viên Lakreevsky (Cheboksary)",
    "Центральный парк культуры и отдыха «Лакреевский лес»",
    "Lakreevsky Forest Central Park (Cheboksary)",
    ["park_garden"],
    56.117477, 47.244434,
    "Ул. Пирогова, 20 (Ленинский район), Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Công viên văn hóa trung tâm của Cheboksary nằm trong một cánh rừng sồi cổ được xếp hạng di tích thiên nhiên. Không gian xanh mát này kết hợp cây cổ thụ, lối dạo, khu vui chơi và trò chơi giải trí, là chốn nghỉ ngơi quen thuộc của người dân.",
    "Rừng công viên Lakreevsky là 'lá phổi xanh' và công viên giải trí lâu đời của Cheboksary. Điểm đặc biệt của nơi này là nền tảng của nó — một cánh rừng sồi cổ thụ được công nhận là di tích thiên nhiên, với nhiều cây đã hàng trăm năm tuổi tỏa bóng mát quanh năm. Trên nền rừng ấy, người ta quy hoạch thành Công viên Văn hóa và Nghỉ ngơi Trung tâm, kết hợp hài hòa giữa thiên nhiên và các tiện ích giải trí. Du khách và người dân địa phương có thể dạo bộ dưới tán sồi, hít thở không khí trong lành, cho trẻ chơi ở khu trò chơi và đu quay, hay đơn giản là ngồi nghỉ trên những băng ghế giữa rừng. Vào mùa hè, công viên rộn ràng tiếng cười của các gia đình; mùa thu, sắc lá vàng rực của rừng sồi tạo nên khung cảnh thơ mộng; mùa đông, nơi đây trở thành chốn đi dạo và trượt tuyết nhẹ nhàng. Nằm không xa trung tâm, Lakreevsky là điểm đến lý tưởng để du khách tạm rời nhịp phố phường, tận hưởng một khoảng lặng xanh mát giữa lòng thủ phủ Chuvashia.",
    [
        "Công viên giải trí trên nền rừng sồi cổ được xếp hạng di tích thiên nhiên.",
        "Nhiều cây sồi hàng trăm năm tuổi, không khí trong lành giữa thành phố.",
        "Khu trò chơi, đu quay và lối dạo phù hợp cho gia đình quanh năm.",
    ],
    {
        "hours_vi": "Công viên mở cửa tự do; khu trò chơi hoạt động chủ yếu mùa ấm và theo giờ.",
        "ticket_vi": "Vào công viên miễn phí; một số trò chơi thu phí riêng.",
        "duration_vi": "1–2 giờ.",
        "best_time_vi": "Mùa hè cho hoạt động gia đình; mùa thu để ngắm lá vàng rừng sồi.",
        "tips_vi": "Đi giày thoải mái để dạo rừng; tiện kết hợp nghỉ ngơi sau khi tham quan trung tâm.",
    },
    [
        {"title": "OpenStreetMap — Лакреевский лес", "url": "https://www.openstreetmap.org/relation/2739229"},
        {"title": "Wikipedia (RU) — Чебоксары", "url": "https://ru.wikipedia.org/wiki/Чебоксары"},
    ],
    ["park", "forest", "nature", "cheboksary", "family"],
    maps_text("Лакреевский лес парк", "Чебоксары", "Lakreevsky Forest Park", "Cheboksary", 56.117477, 47.244434),
))

# 15) Национальная библиотека Чувашской Республики -------------------------------
RECORDS.append(rec(
    "chuvash-national-library",
    "Thư viện Quốc gia Cộng hòa Chuvashia",
    "Национальная библиотека Чувашской Республики",
    "National Library of the Chuvash Republic",
    ["other"],
    56.127969, 47.251986,
    "Проспект Ленина, 15, Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Thư viện lớn nhất và lâu đời nhất Chuvashia, thành lập năm 1871, là kho tri thức và trung tâm văn hóa hàng đầu của nước cộng hòa. Tòa nhà bề thế trên đại lộ Lenin lưu giữ hàng triệu ấn phẩm, trong đó có nhiều tư liệu quý về Chuvash.",
    "Thư viện Quốc gia Cộng hòa Chuvashia là trung tâm tri thức và văn hóa lớn nhất của vùng đất này. Được thành lập từ năm 1871, thư viện đã trải qua hơn một thế kỷ rưỡi phát triển để trở thành kho lưu giữ hàng triệu đầu sách, báo, tạp chí và tài liệu, bao gồm cả bộ sưu tập quý giá về ngôn ngữ, lịch sử và văn học Chuvash. Tòa nhà thư viện bề thế nằm trên đại lộ Lenin, là một điểm nhấn kiến trúc của trung tâm Cheboksary. Không chỉ là nơi đọc sách, thư viện còn đóng vai trò như một trung tâm văn hóa sôi động: tổ chức triển lãm, hội thảo, gặp gỡ tác giả, các buổi giới thiệu sách và những sự kiện tôn vinh di sản chữ viết Chuvash. Thư viện cũng chú trọng số hóa tư liệu và phục vụ nghiên cứu, trở thành địa chỉ quen thuộc của học sinh, sinh viên và các nhà nghiên cứu. Với du khách quan tâm tới văn hóa bản địa, đây là nơi có thể cảm nhận chiều sâu tri thức của Chuvashia và đôi khi bắt gặp những triển lãm, sự kiện đáng chú ý.",
    [
        "Thư viện lớn và lâu đời nhất Chuvashia, thành lập năm 1871.",
        "Lưu giữ hàng triệu ấn phẩm, nhiều tư liệu quý về ngôn ngữ và văn học Chuvash.",
        "Trung tâm văn hóa với triển lãm, hội thảo và sự kiện tôn vinh di sản Chuvash.",
    ],
    {
        "hours_vi": "Mở cửa các ngày trong tuần theo giờ hành chính, một số ngày cuối tuần; nghỉ theo lịch riêng.",
        "ticket_vi": "Vào tham quan/đọc miễn phí; một số dịch vụ có thể tính phí.",
        "duration_vi": "30 phút–1 giờ (nếu ghé triển lãm/sự kiện).",
        "best_time_vi": "Quanh năm; kiểm tra lịch triển lãm và sự kiện trước khi đến.",
        "tips_vi": "Nằm trên проспект Ленина, dễ kết hợp với các điểm trung tâm; hỏi lịch sự kiện văn hóa tại quầy.",
    },
    [
        {"title": "Komandirovka.ru — Национальная библиотека Чувашской Республики", "url": "https://www.komandirovka.ru/sights/cheboksary/natsionalnaya-biblioteka-chuvashskoy-respubliki/"},
        {"title": "Wikipedia (RU) — Национальная библиотека Чувашской Республики", "url": "https://ru.wikipedia.org/wiki/Национальная_библиотека_Чувашской_Республики"},
    ],
    ["library", "culture", "history", "cheboksary", "landmark"],
    maps_text("Национальная библиотека Чувашской Республики", "Чебоксары", "National Library of the Chuvash Republic", "Cheboksary", 56.127969, 47.251986),
))

# 16) Музей истории трактора (Чебоксары) ------------------------------------------
RECORDS.append(rec(
    "tractor-history-museum",
    "Bảo tàng Lịch sử Máy kéo (Cheboksary)",
    "Музей истории трактора",
    "Museum of Tractor History (Cheboksary)",
    ["museum"],
    56.124326, 47.284514,
    "Проспект Мира, 1, Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Bảo tàng chuyên đề độc đáo mở cửa năm 2011, dành riêng cho lịch sử ngành máy kéo của Nga và thế giới. Trưng bày nhiều mẫu máy kéo thật, mô hình và tư liệu, gắn với truyền thống chế tạo máy kéo của Cheboksary.",
    "Bảo tàng Lịch sử Máy kéo ở Cheboksary là một bảo tàng chuyên đề độc nhất vô nhị, phản ánh vai trò của thành phố như một trung tâm chế tạo máy kéo lớn của nước Nga. Được khai trương năm 2011 dưới sự bảo trợ của tổ hợp công nghiệp máy kéo, bảo tàng kể lại toàn bộ câu chuyện phát triển của cỗ máy đã làm thay đổi nền nông nghiệp thế giới. Các gian trưng bày dẫn khách đi từ những phát minh cơ giới hóa đầu tiên, qua thời kỳ hoàng kim của công nghiệp máy kéo Xô Viết, cho tới những mẫu máy hiện đại. Điểm hấp dẫn nhất là bộ sưu tập máy kéo thật với nhiều chủng loại và niên đại khác nhau — từ những chiếc cổ điển đến các mẫu công suất lớn — cho phép khách tận mắt chiêm ngưỡng và hình dung quy mô của ngành. Bên cạnh đó là mô hình, tài liệu, ảnh và các khu tương tác thú vị, đặc biệt hấp dẫn với trẻ em và những ai yêu kỹ thuật. Đây là một bảo tàng vừa mang tính giáo dục, vừa gợi mở góc nhìn về lịch sử công nghiệp và lao động của vùng Volga.",
    [
        "Bảo tàng chuyên đề độc đáo về lịch sử máy kéo, mở cửa năm 2011.",
        "Bộ sưu tập máy kéo thật đa dạng chủng loại và niên đại.",
        "Gắn với truyền thống công nghiệp chế tạo máy kéo của Cheboksary; hấp dẫn trẻ em.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nghỉ thứ Hai. Nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà); phù hợp đi cùng gia đình.",
        "tips_vi": "Nằm hơi xa trung tâm về phía đông; tiện đi bằng ô tô hoặc xe buýt; nhiều khu tương tác cho trẻ.",
    },
    [
        {"title": "Komandirovka.ru — Музей истории трактора, Чебоксары", "url": "https://www.komandirovka.ru/sights/cheboksary/museum-istorii-traktora/"},
        {"title": "Wikipedia (RU) — Музей истории трактора", "url": "https://ru.wikipedia.org/wiki/Музей_истории_трактора"},
    ],
    ["museum", "technology", "industry", "cheboksary", "family"],
    maps_text("Музей истории трактора", "Чебоксары", "Museum of Tractor History", "Cheboksary", 56.124326, 47.284514),
))

# 17) Музей чувашской вышивки (Чебоксары) -----------------------------------------
RECORDS.append(rec(
    "cheboksary-embroidery-museum",
    "Bảo tàng Thêu Chuvash (Cheboksary)",
    "Музей чувашской вышивки",
    "Museum of Chuvash Embroidery (Cheboksary)",
    ["museum"],
    56.141326, 47.249604,
    "Ул. Карла Маркса, 32, Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Bảo tàng chuyên đề dành riêng cho nghệ thuật thêu truyền thống Chuvash — một di sản văn hóa đặc sắc với hệ hoa văn và ký hiệu cổ. Nơi đây trưng bày trang phục, khăn, hoa văn thêu tinh xảo cùng câu chuyện về ý nghĩa biểu tượng của chúng.",
    "Thêu là một trong những di sản văn hóa rực rỡ và độc đáo nhất của người Chuvash, và Bảo tàng Thêu Chuvash ở Cheboksary được lập ra để tôn vinh chính di sản ấy. Nghệ thuật thêu Chuvash nổi bật với hệ thống hoa văn hình học phong phú, những ký hiệu cổ mang ý nghĩa tâm linh, biểu trưng cho vũ trụ, mặt trời, cây đời và sự sinh sôi. Bảo tàng trưng bày các bộ trang phục dân tộc, khăn thêu, tạp dề, mũ đội đầu và những mảnh vải với đường kim mũi chỉ tinh xảo, phản ánh tay nghề bậc thầy của các nghệ nhân qua nhiều thế hệ. Không chỉ giới thiệu hiện vật, bảo tàng còn giải mã ngôn ngữ biểu tượng ẩn trong từng hoa văn, giúp khách hiểu rằng với người Chuvash, thêu không đơn thuần là trang trí mà còn là cách ghi lại tín ngưỡng, thân phận và bản sắc. Nhiều nơi còn tổ chức lớp trải nghiệm hoặc trình diễn thêu tay. Với du khách, đây là một bảo tàng nhỏ nhưng đầy chiều sâu, chạm tới tâm hồn văn hóa của một dân tộc qua sợi chỉ và hoa văn.",
    [
        "Bảo tàng chuyên đề về nghệ thuật thêu truyền thống Chuvash.",
        "Trưng bày trang phục, khăn, hoa văn với hệ ký hiệu cổ mang ý nghĩa tâm linh.",
        "Giải mã ngôn ngữ biểu tượng ẩn trong hoa văn — chiều sâu bản sắc Chuvash.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nghỉ thứ Hai. Nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; có thể có lớp trải nghiệm thu phí riêng.",
        "duration_vi": "45 phút–1 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Kết hợp với Bảo tàng Quốc gia Chuvash để hiểu trọn văn hóa dân tộc; hỏi về buổi trình diễn/lớp thêu.",
    },
    [
        {"title": "OpenStreetMap — Музей чувашской вышивки", "url": "https://www.openstreetmap.org/node/5842261207"},
        {"title": "Wikipedia (RU) — Чувашская вышивка", "url": "https://ru.wikipedia.org/wiki/Чувашская_вышивка"},
    ],
    ["museum", "embroidery", "ethnography", "chuvash", "culture"],
    maps_text("Музей чувашской вышивки", "Чебоксары", "Museum of Chuvash Embroidery", "Cheboksary", 56.141326, 47.249604),
))

# 18) Владимирский собор (Новочебоксарск) -----------------------------------------
RECORDS.append(rec(
    "novocheboksarsk-vladimir-cathedral",
    "Nhà thờ chính tòa Thánh Vladimir (Novocheboksarsk)",
    "Собор святого равноапостольного князя Владимира",
    "Cathedral of St. Vladimir (Novocheboksarsk)",
    ["church"],
    56.107793, 47.482470,
    "Ул. Винокурова, 53 (Соборная площадь), thành phố Novocheboksarsk, Cộng hòa Chuvashia, Nga.",
    "Nhà thờ chính tòa của thành phố trẻ Novocheboksarsk, mang tên Thánh Vladimir — vị hoàng thân đã đưa Chính Thống giáo vào nước Nga. Ngôi thánh đường lớn với những mái vòm vàng là trung tâm tôn giáo và điểm nhấn kiến trúc của đô thị.",
    "Novocheboksarsk là thành phố trẻ, hình thành từ năm 1960 như một trung tâm công nghiệp lớn cạnh Cheboksary, và Nhà thờ chính tòa Thánh Vladimir chính là công trình tôn giáo tiêu biểu nhất của đô thị này. Nhà thờ mang tên Thánh Vladimir — vị đại công tước Kiev đã lựa chọn Chính Thống giáo làm quốc giáo của nước Nga cổ, một nhân vật có ý nghĩa nền tảng với văn hóa và tôn giáo Nga. Là một công trình được xây dựng và hoàn thiện trong những thập niên gần đây, nhà thờ có quy mô bề thế với khối chính vươn cao, nhiều mái vòm mạ vàng lấp lánh và không gian nội thất trang hoàng lộng lẫy. Tọa lạc trên quảng trường Sobornaya rộng rãi, nhà thờ trở thành trung tâm đời sống tâm linh của cộng đồng Chính Thống giáo địa phương, nơi diễn ra các buổi lễ trọng và sự kiện tôn giáo lớn. Với du khách ghé thăm Novocheboksarsk, đây là điểm đến để cảm nhận sự hồi sinh của đời sống tôn giáo Nga đương đại và chiêm ngưỡng một công trình kiến trúc Chính Thống giáo trang nghiêm, rực rỡ.",
    [
        "Nhà thờ chính tòa của Novocheboksarsk, mang tên Thánh Vladimir.",
        "Công trình bề thế với nhiều mái vòm mạ vàng, nội thất lộng lẫy.",
        "Trung tâm đời sống tâm linh trên quảng trường Sobornaya.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (nơi thờ phụng; khuyến khích quyên góp).",
        "duration_vi": "20–40 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp đại lễ Chính Thống giáo.",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; Novocheboksarsk cách Cheboksary ~15 km, tiện đi trong ngày.",
    },
    [
        {"title": "Sobory.ru — Собор Владимира равноапостольного, Новочебоксарск", "url": "https://sobory.ru/article/?object=04988"},
        {"title": "Wikipedia (RU) — Новочебоксарск", "url": "https://ru.wikipedia.org/wiki/Новочебоксарск"},
    ],
    ["church", "cathedral", "orthodox", "novocheboksarsk", "architecture"],
    maps_text("Собор святого князя Владимира", "Новочебоксарск", "Cathedral of St. Vladimir", "Novocheboksarsk", 56.107793, 47.482470),
))

# 19) Ельниковская роща (Новочебоксарск) ------------------------------------------
RECORDS.append(rec(
    "elnikovskaya-grove",
    "Rừng công viên Elnikovskaya (Novocheboksarsk)",
    "Ельниковская роща",
    "Elnikovskaya Grove (Novocheboksarsk)",
    ["park_garden"],
    56.124456, 47.475055,
    "Ельниковская роща, bên bờ sông Volga, thành phố Novocheboksarsk, Cộng hòa Chuvashia, Nga.",
    "Khu rừng công viên nghỉ dưỡng lớn của Novocheboksarsk bên bờ sông Volga, kết hợp rừng cây, bãi tắm, khu vui chơi và một vườn thú nhỏ. Đây là địa điểm dạo chơi, tắm sông và giải trí được người dân yêu thích nhất thành phố.",
    "Ельниковская роща là không gian xanh và khu nghỉ dưỡng được yêu thích nhất của Novocheboksarsk. Trải dài bên bờ sông Volga, khu rừng công viên này là nơi người dân tìm đến để tận hưởng thiên nhiên ngay sát đô thị. Điểm hấp dẫn của Elnikovskaya nằm ở sự đa dạng: những cánh rừng thông và cây lá rộng mát mẻ để dạo bộ và đạp xe, bãi tắm ven sông Volga vào mùa hè, các khu vui chơi, trò chơi giải trí cho trẻ em, và đặc biệt là một vườn thú nhỏ khiến nơi đây trở thành điểm đến lý tưởng cho các gia đình. Vào những ngày cuối tuần và dịp lễ mùa ấm, công viên rộn ràng người dạo chơi, cắm trại nhẹ, đạp vịt trên hồ và picnic dưới tán cây. Mùa đông, rừng khoác áo tuyết trở thành nơi đi bộ và trượt tuyết yên bình. Với du khách ghé Novocheboksarsk, Ельниковская роща là nơi thư giãn dễ chịu, kết hợp giữa vẻ đẹp của rừng, dòng Volga và không khí sinh hoạt gia đình đầm ấm của một thành phố công nghiệp trẻ.",
    [
        "Rừng công viên lớn bên sông Volga — điểm nghỉ dưỡng yêu thích của Novocheboksarsk.",
        "Có bãi tắm sông Volga, khu vui chơi và một vườn thú nhỏ.",
        "Không gian lý tưởng cho gia đình, dạo bộ, đạp xe và picnic.",
    ],
    {
        "hours_vi": "Công viên ngoài trời mở cửa tự do; vườn thú và trò chơi có giờ và phí riêng.",
        "ticket_vi": "Vào công viên miễn phí; vườn thú và một số dịch vụ thu phí.",
        "duration_vi": "1,5–3 giờ.",
        "best_time_vi": "Mùa hè để tắm sông và vui chơi; mùa thu để ngắm rừng đổi màu.",
        "tips_vi": "Mang đồ picnic và đồ bơi mùa hè; cách Cheboksary ~15 km, tiện kết hợp thăm Novocheboksarsk.",
    },
    [
        {"title": "OpenStreetMap — Ельниковская роща", "url": "https://www.openstreetmap.org/relation/2597709"},
        {"title": "Wikipedia (RU) — Новочебоксарск", "url": "https://ru.wikipedia.org/wiki/Новочебоксарск"},
    ],
    ["park", "forest", "volga", "novocheboksarsk", "family"],
    maps_text("Ельниковская роща", "Новочебоксарск", "Elnikovskaya Grove", "Novocheboksarsk", 56.124456, 47.475055),
))

# 20) Тихвинский Богородицкий женский монастырь (Цивильск) ------------------------
RECORDS.append(rec(
    "tsivilsk-tikhvin-convent",
    "Tu viện nữ Tikhvin Đức Mẹ (Tsivilsk)",
    "Тихвинский Богородицкий женский монастырь",
    "Tikhvin Convent of the Mother of God (Tsivilsk)",
    ["church"],
    55.877097, 47.473214,
    "Thành phố Tsivilsk, bên sông Bolshoy Tsivil, Cộng hòa Chuvashia, Nga (cách Cheboksary ~40 km).",
    "Tu viện nữ cổ kính ở thị trấn Tsivilsk, có nguồn gốc từ năm 1671 sau cuộc nổi dậy Razin, gắn với biểu tượng Đức Mẹ Tikhvin được tôn kính. Quần thể nhà thờ trắng, mái vòm xanh là một trung tâm hành hương quan trọng của Chuvashia.",
    "Tu viện nữ Tikhvin Đức Mẹ ở thị trấn Tsivilsk là một trong những trung tâm hành hương Chính Thống giáo lâu đời và được tôn kính của Chuvashia. Theo truyền thống, tu viện được lập vào năm 1671, ngay sau khi cư dân Tsivilsk vượt qua cuộc vây hãm trong thời kỳ khởi nghĩa nông dân do Stepan Razin lãnh đạo; người dân tin rằng chính sự chở che của Đức Mẹ Tikhvin đã giúp thị trấn thoát nạn, nên đã dựng tu viện để tạ ơn. Ban đầu là tu viện nam, đến cuối thế kỷ 19 nơi đây chuyển thành tu viện nữ và phát triển hưng thịnh. Trải qua thời kỳ bị đóng cửa dưới chính quyền Xô Viết, tu viện được hồi sinh từ đầu thập niên 1990 và ngày nay là nơi tu tập của các nữ tu. Quần thể gồm nhà thờ chính, các nhà nguyện, tường bao và tháp chuông, nổi bật với những bức tường trắng và mái vòm xanh điểm sao. Báu vật thiêng liêng nhất là biểu tượng Đức Mẹ Tikhvin được đông đảo tín đồ tìm đến cầu nguyện. Với du khách, tu viện là điểm dừng chân bình yên để tìm hiểu chiều sâu tín ngưỡng và lịch sử của vùng đất Chuvash.",
    [
        "Tu viện có nguồn gốc năm 1671, gắn với sự kiện Tsivilsk thoát vây thời khởi nghĩa Razin.",
        "Trung tâm hành hương với biểu tượng Đức Mẹ Tikhvin được tôn kính.",
        "Quần thể nhà thờ tường trắng, mái vòm xanh; nay là tu viện nữ đang hoạt động.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (nơi thờ phụng; khuyến khích quyên góp).",
        "duration_vi": "30–45 phút.",
        "best_time_vi": "Mùa ấm; các dịp lễ Đức Mẹ Tikhvin có không khí hành hương đặc biệt.",
        "tips_vi": "Nữ nên trùm khăn, mặc kín đáo; Tsivilsk cách Cheboksary ~40 km, tiện dừng khi đi về phía Kazan.",
    },
    [
        {"title": "Yandex Maps — Тихвинский Богородицкий монастырь, Цивильск", "url": "https://yandex.com/maps/org/sobor_ikony_bozhiyey_materi_tikhvinskaya_v_tsivilskom_tikhvinskom_monastyre/1761828163/"},
        {"title": "Wikipedia (RU) — Тихвинский Богородицкий монастырь (Цивильск)", "url": "https://ru.wikipedia.org/wiki/Тихвинский_Богородицкий_монастырь_(Цивильск)"},
    ],
    ["monastery", "church", "orthodox", "pilgrimage", "tsivilsk"],
    maps_org("https://yandex.com/maps/org/sobor_ikony_bozhiyey_materi_tikhvinskaya_v_tsivilskom_tikhvinskom_monastyre/1761828163/", "Tikhvin Convent", "Tsivilsk"),
))

# 21) Государева гора / Мариинский Посад -------------------------------------------
RECORDS.append(rec(
    "mariinsky-posad-tsar-hill",
    "Đồi Nhà Vua (Gosudareva Gora) và thị trấn Mariinsky Posad",
    "Государева гора (Мариинский Посад)",
    "Tsar's Hill (Gosudareva Gora), Mariinsky Posad",
    ["square_street", "park_garden"],
    56.121287, 47.739690,
    "Государева гора, thị trấn Mariinsky Posad, bên sông Volga, Cộng hòa Chuvashia, Nga (cách Cheboksary ~35 km).",
    "Ngọn đồi bên sông Volga tại thị trấn cổ Mariinsky Posad, gắn với truyền thuyết Sa hoàng Pyotr Đại đế từng dừng chân năm 1722. Đỉnh đồi là điểm ngắm toàn cảnh sông Volga và thị trấn thương nhân xinh xắn phía dưới.",
    "Государева гора — 'Đồi Nhà Vua' — là biểu tượng của thị trấn cổ Mariinsky Posad bên bờ sông Volga. Tên gọi của ngọn đồi gắn với truyền thuyết rằng năm 1722, trên đường viễn chinh xuống vùng Ba Tư, Sa hoàng Pyotr Đại đế đã dừng chân và leo lên đỉnh đồi để phóng tầm mắt ngắm dòng Volga hùng vĩ; từ đó ngọn đồi mang tên gắn với nhà vua. Mariinsky Posad vốn là một thị trấn thương nhân duyên dáng, hình thành từ làng Sundyr và được nâng cấp thành đô thị năm 1856 dưới thời Hoàng hậu Maria — người mà thị trấn được đặt tên theo. Đứng trên Государева гора, du khách có thể bao quát toàn cảnh: dòng Volga mênh mông uốn lượn, những mái nhà và nhà thờ của thị trấn nép mình bên sông, cùng khung cảnh thiên nhiên thanh bình đặc trưng của vùng trung lưu Volga. Khu vực đồi có công viên, lối dạo và điểm ngắm cảnh. Với những ai muốn rời xa nhịp phố Cheboksary, chuyến đi tới Mariinsky Posad và leo Государева гора mang lại trải nghiệm êm đềm về một góc tỉnh lẻ Nga giàu lịch sử và cảnh sắc.",
    [
        "Đồi ngắm cảnh bên sông Volga, gắn truyền thuyết Pyotr Đại đế dừng chân năm 1722.",
        "Điểm ngắm toàn cảnh dòng Volga và thị trấn thương nhân Mariinsky Posad.",
        "Thị trấn cổ duyên dáng, đặt tên theo Hoàng hậu Maria (nâng cấp đô thị năm 1856).",
    ],
    {
        "hours_vi": "Đồi và điểm ngắm cảnh ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "1–2 giờ (kể cả dạo thị trấn).",
        "best_time_vi": "Cuối xuân đến đầu thu để leo đồi và ngắm Volga; hoàng hôn cho cảnh đẹp nhất.",
        "tips_vi": "Đi giày thoải mái để leo đồi; cách Cheboksary ~35 km, tiện đi ô tô; kết hợp dạo trung tâm cổ Mariinsky Posad.",
    },
    [
        {"title": "OpenStreetMap — Государева гора", "url": "https://www.openstreetmap.org/node/1937303725"},
        {"title": "Wikipedia (RU) — Мариинский Посад", "url": "https://ru.wikipedia.org/wiki/Мариинский_Посад"},
    ],
    ["viewpoint", "volga", "nature", "mariinsky-posad", "history"],
    maps_text("Государева гора", "Мариинский Посад", "Tsar's Hill Gosudareva Gora", "Mariinsky Posad", 56.121287, 47.739690),
))

# 22) Национальный парк «Чаваш вармане» (Шемуршинский район) ----------------------
RECORDS.append(rec(
    "chavash-varmane-national-park",
    "Vườn quốc gia «Chavash Varmane» (Rừng Chuvash)",
    "Национальный парк «Чаваш вармане»",
    "Chavash Varmane National Park",
    ["park_garden"],
    54.828530, 47.246880,
    "Huyện Shemurshinsky, phía nam Cộng hòa Chuvashia, Nga (trung tâm hành chính ở làng Shemursha).",
    "Vườn quốc gia duy nhất của Chuvashia, thành lập năm 1993 ở vùng rừng phía nam. Tên gọi 'Chavash Varmane' nghĩa là 'Rừng Chuvash', bảo vệ những cánh rừng thông, sồi cùng hệ động thực vật phong phú, với các tuyến đường sinh thái và hồ đẹp.",
    "Национальный парк «Чаваш вармане» — trong tiếng Chuvash nghĩa là 'Rừng Chuvash' — là vườn quốc gia duy nhất của Cộng hòa Chuvashia, được thành lập năm 1993 ở vùng cực nam của nước cộng hòa, giáp ranh với Tatarstan và Ulyanovsk. Vườn bảo vệ một trong những vùng rừng nguyên vẹn và giá trị nhất của khu vực: những cánh rừng thông cổ, rừng sồi và cây lá rộng đan xen, cùng các đầm lầy, sông suối và hồ nước trong lành. Đây là mái nhà của nhiều loài động thực vật quý, trong đó có những loài được ghi vào Sách Đỏ. Vườn quốc gia phát triển du lịch sinh thái với các tuyến đường mòn, chòi quan sát, khu cắm trại và trung tâm giới thiệu thiên nhiên, giúp du khách khám phá rừng một cách có trách nhiệm. Nơi đây cũng gìn giữ dấu tích văn hóa của người Chuvash gắn với rừng — vốn có vị trí thiêng liêng trong tín ngưỡng và đời sống dân tộc. Với những ai yêu thiên nhiên và muốn trải nghiệm một Chuvashia hoang sơ, xanh mát ngoài các đô thị, chuyến đi tới 'Rừng Chuvash' mang lại không khí trong lành và cảm giác thư thái hiếm có.",
    [
        "Vườn quốc gia duy nhất của Chuvashia, thành lập năm 1993 ('Rừng Chuvash').",
        "Bảo vệ rừng thông, sồi, đầm hồ và nhiều loài trong Sách Đỏ.",
        "Có tuyến đường sinh thái, chòi quan sát và khu cắm trại cho du lịch xanh.",
    ],
    {
        "hours_vi": "Khu bảo tồn ngoài trời; tham quan các tuyến sinh thái nên đăng ký trước với ban quản lý.",
        "ticket_vi": "Có phí vào và phí tuyến tham quan; liên hệ ban quản lý để biết chi tiết.",
        "duration_vi": "Nửa ngày đến trọn ngày.",
        "best_time_vi": "Cuối xuân đến đầu thu để đi rừng thuận lợi.",
        "tips_vi": "Ở xa Cheboksary (~130 km về phía nam), nên đi ô tô và sắp xếp cả ngày; đặt trước hướng dẫn và chỗ nghỉ; mang đồ chống côn trùng.",
    },
    [
        {"title": "OpenStreetMap — Национальный парк «Чаваш Вармане»", "url": "https://www.openstreetmap.org/relation/4759838"},
        {"title": "Wikipedia (RU) — Чаваш вармане", "url": "https://ru.wikipedia.org/wiki/Чаваш_вармане"},
    ],
    ["national-park", "nature", "forest", "eco-tourism", "chuvashia"],
    maps_text("Национальный парк Чаваш вармане", "Шемурша", "Chavash Varmane National Park", "Shemursha", 54.828530, 47.246880),
))

# 23) Государственный заповедник «Присурский» (Алатырский район) ------------------
RECORDS.append(rec(
    "prisursky-nature-reserve",
    "Khu bảo tồn thiên nhiên «Prisursky»",
    "Государственный природный заповедник «Присурский»",
    "Prisursky Nature Reserve",
    ["park_garden"],
    54.991951, 46.767026,
    "Huyện Alatyrsky (khu chính bên sông Sura), phía nam Cộng hòa Chuvashia, Nga (ban quản lý đặt tại Alatyr).",
    "Khu bảo tồn thiên nhiên quốc gia của Chuvashia, thành lập năm 1995, nằm dọc sông Sura ở phía nam nước cộng hòa. Nơi đây bảo vệ rừng taiga phương nam và thảo nguyên rừng cùng hệ chim, thú phong phú, là địa bàn nghiên cứu và bảo tồn quan trọng.",
    "Государственный природный заповедник «Присурский» là khu bảo tồn thiên nhiên nghiêm ngặt cấp quốc gia của Chuvashia, được thành lập năm 1995 nhằm gìn giữ những hệ sinh thái tiêu biểu của vùng. Khu vực chính của khu bảo tồn nằm ở huyện Alatyrsky phía nam, dọc theo lưu vực sông Sura, nơi giao thoa giữa rừng taiga phương nam và vùng thảo nguyên rừng — tạo nên sự đa dạng sinh học đặc biệt. Заповедник bảo vệ những cánh rừng thông, sồi, các bãi bồi và đầm lầy ven sông, là nơi cư trú của nhiều loài chim, thú, bò sát và côn trùng, trong đó có những loài quý hiếm được ghi vào Sách Đỏ. Không giống công viên giải trí, đây là khu bảo tồn phục vụ nghiên cứu khoa học và bảo tồn, nên việc tham quan được kiểm soát chặt chẽ và thường theo các tuyến sinh thái có hướng dẫn. Ban quản lý ở thành phố Alatyr tổ chức các chương trình giáo dục môi trường và tham quan có tổ chức. Với du khách yêu thiên nhiên và quan tâm tới bảo tồn, Присурский mang đến cơ hội tìm hiểu về sự phong phú và mong manh của thiên nhiên vùng nam Chuvashia.",
    [
        "Khu bảo tồn thiên nhiên nghiêm ngặt cấp quốc gia, thành lập năm 1995.",
        "Bảo vệ giao thoa rừng taiga phương nam và thảo nguyên rừng dọc sông Sura.",
        "Nơi cư trú của nhiều loài chim, thú quý hiếm trong Sách Đỏ; phục vụ nghiên cứu.",
    ],
    {
        "hours_vi": "Khu bảo tồn nghiêm ngặt; tham quan phải đăng ký trước và đi theo tuyến có hướng dẫn.",
        "ticket_vi": "Có phí tham quan tuyến sinh thái; liên hệ ban quản lý ở Alatyr.",
        "duration_vi": "Nửa ngày đến trọn ngày (tuỳ tuyến).",
        "best_time_vi": "Cuối xuân đến đầu thu; mùa chim di cư đặc biệt thú vị cho người thích quan sát chim.",
        "tips_vi": "Bắt buộc liên hệ trước ban quản lý; không tự ý vào vùng lõi; mang đồ đi rừng và chống côn trùng.",
    },
    [
        {"title": "OpenStreetMap — Заповедник «Присурский»", "url": "https://www.openstreetmap.org/relation/7376929"},
        {"title": "Wikipedia (RU) — Присурский (заповедник)", "url": "https://ru.wikipedia.org/wiki/Присурский_(заповедник)"},
    ],
    ["nature-reserve", "nature", "birdwatching", "sura-river", "chuvashia"],
    maps_text("Государственный заповедник Присурский", "Алатырь", "Prisursky Nature Reserve", "Alatyr", 54.991951, 46.767026),
))

# 24) Спасо-Преображенский женский монастырь (Чебоксары) --------------------------
RECORDS.append(rec(
    "transfiguration-convent-cheboksary",
    "Tu viện nữ Chúa Hiển Dung (Cheboksary)",
    "Спасо-Преображенский женский монастырь",
    "Transfiguration Convent (Cheboksary)",
    ["church"],
    56.135090, 47.230354,
    "Ул. Владимирская горка (khu phía tây trung tâm), Cheboksary, Cộng hòa Chuvashia, Nga.",
    "Tu viện nữ Chính Thống giáo ở Cheboksary, có nguồn gốc từ cuối thế kỷ 19, hồi sinh sau thời Xô Viết. Quần thể nhà thờ và các công trình tu viện nằm trên một khu đất yên tĩnh phía tây trung tâm, là chốn tu tập và hành hương thanh bình.",
    "Tu viện nữ Chúa Hiển Dung (Спасо-Преображенский) là một trong những trung tâm tu tập nữ giới của Chính Thống giáo ở Cheboksary. Cộng đồng nữ tu ở đây có nguồn gốc từ cuối thế kỷ 19, khởi đầu là một cộng đoàn nhỏ rồi dần phát triển thành tu viện với nhà thờ mang tên lễ Chúa Hiển Dung. Như phần lớn các cơ sở tôn giáo ở Nga, tu viện bị đóng cửa và rơi vào cảnh hoang phế trong thời kỳ Xô Viết, để rồi được hồi sinh và tái lập từ những năm 1990 khi đời sống tôn giáo được khôi phục. Ngày nay, quần thể gồm nhà thờ chính, nhà nguyện, khu ở của các nữ tu và vườn tược, nằm trên một khu đất tĩnh lặng ở phía tây trung tâm thành phố, tách khỏi nhịp sống ồn ào. Không gian tu viện toát lên vẻ thanh bình, với tiếng chuông ngân, những luống hoa và bầu không khí trầm mặc đặc trưng. Với du khách quan tâm tới đời sống tâm linh và văn hóa Chính Thống giáo, đây là điểm dừng chân yên tĩnh, nơi cảm nhận rõ sự tương phản dịu dàng giữa chốn tu hành và thành phố hiện đại xung quanh.",
    [
        "Tu viện nữ có nguồn gốc cuối thế kỷ 19, hồi sinh sau thời Xô Viết.",
        "Nhà thờ mang tên lễ Chúa Hiển Dung cùng khu ở của các nữ tu và vườn.",
        "Không gian thanh bình ở phía tây trung tâm Cheboksary.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (nơi thờ phụng; khuyến khích quyên góp).",
        "duration_vi": "20–40 phút.",
        "best_time_vi": "Mùa ấm; giờ lễ để cảm nhận không khí phụng vụ.",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; giữ yên lặng, tôn trọng nếp sinh hoạt của các nữ tu.",
    },
    [
        {"title": "Sobory.ru — Спасо-Преображенский женский монастырь, Чебоксары", "url": "https://sobory.ru/article/?object=05007"},
        {"title": "Wikipedia (RU) — Чебоксары", "url": "https://ru.wikipedia.org/wiki/Чебоксары"},
    ],
    ["monastery", "convent", "orthodox", "cheboksary", "pilgrimage"],
    maps_text("Спасо-Преображенский женский монастырь", "Чебоксары", "Transfiguration Convent", "Cheboksary", 56.135090, 47.230354),
))

# 25) Ибресинский этнографический музей под открытым небом ------------------------
RECORDS.append(rec(
    "ibresi-ethnographic-museum",
    "Bảo tàng Dân tộc học ngoài trời Ibresi",
    "Ибресинский этнографический музей под открытым небом",
    "Ibresi Open-Air Ethnographic Museum",
    ["museum"],
    55.302675, 47.041869,
    "Ул. Комсомольская, thị trấn Ibresi, huyện Ibresinsky, Cộng hòa Chuvashia, Nga.",
    "Bảo tàng dân tộc học ngoài trời tại thị trấn Ibresi, thành lập năm 1980, tái hiện nếp sống làng quê Chuvash truyền thống. Khách có thể tham quan nhà gỗ, sân vườn, cối xay gió và các công trình dân gian với đồ dùng, dụng cụ sinh hoạt xưa.",
    "Ибресинский этнографический музей под открытым небом là một bảo tàng dân tộc học ngoài trời độc đáo nằm ở thị trấn Ibresi, phía nam Chuvashia. Được thành lập năm 1980, bảo tàng tái hiện sinh động khung cảnh và nếp sống của một ngôi làng Chuvash truyền thống ngay dưới bầu trời. Trên khuôn viên rộng, khách bước vào một 'ngôi làng thu nhỏ' với những căn nhà gỗ (izba) đích thực được sưu tầm và phục dựng, sân vườn, nhà kho, chuồng trại, nhà tắm hơi kiểu Nga (banya) và cả cối xay gió — biểu tượng của làng quê xưa. Bên trong các công trình là vô số đồ dùng sinh hoạt, nông cụ, khung cửi, đồ gốm và vật dụng thủ công, giúp du khách hình dung rõ ràng cuộc sống thường nhật của người Chuvash cuối thế kỷ 19 - đầu thế kỷ 20. Bảo tàng cũng lưu giữ các bộ trang phục, đồ thêu và tổ chức những sự kiện văn hóa dân gian, lễ hội truyền thống. Khác với bảo tàng trong nhà, trải nghiệm ngoài trời ở đây mang lại cảm giác chân thực và gần gũi, như thể được bước ngược thời gian về với cội nguồn văn hóa nông thôn Chuvash.",
    [
        "Bảo tàng dân tộc học ngoài trời, thành lập năm 1980, tái hiện làng quê Chuvash.",
        "Nhà gỗ đích thực, cối xay gió, banya và đầy đủ đồ dùng, nông cụ, khung cửi xưa.",
        "Tổ chức sự kiện văn hóa, lễ hội dân gian; trải nghiệm 'bước ngược thời gian'.",
    ],
    {
        "hours_vi": "Thường mở cửa ban ngày; một số công trình chỉ mở theo tour. Nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "1–1,5 giờ.",
        "best_time_vi": "Mùa ấm (tháng 5–9) vì là bảo tàng ngoài trời; đẹp nhất khi có lễ hội dân gian.",
        "tips_vi": "Ibresi ở phía nam, cách Cheboksary ~90 km; tiện đi ô tô hoặc tàu; mặc đồ phù hợp thời tiết vì tham quan ngoài trời.",
    },
    [
        {"title": "OpenStreetMap — Ибресинский этнографический музей", "url": "https://www.openstreetmap.org/node/9834578532"},
        {"title": "Wikipedia (RU) — Ибресинский этнографический музей", "url": "https://ru.wikipedia.org/wiki/Ибресинский_этнографический_музей"},
    ],
    ["museum", "open-air", "ethnography", "chuvash", "folk-culture"],
    maps_text("Ибресинский этнографический музей", "Ибреси", "Ibresi Open-Air Ethnographic Museum", "Ibresi", 55.302675, 47.041869),
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
