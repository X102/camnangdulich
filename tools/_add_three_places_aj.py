# -*- coding: utf-8 -*-
"""_add_three_places_aj.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-27, phiên aj).

ƯU TIÊN VÙNG (a): thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.
Chọn 3 danh thắng THỰC SỰ nổi tiếng còn THIẾU, đa dạng chủ đề (điền trang văn học – tu viện cổ – điền trang
kiến trúc), phủ CẢ HAI vùng ưu tiên (2 ở Tỉnh Moskva, 1 ở Tỉnh Leningrad):

Thêm:
  1) Tỉnh Moskva (moscow-oblast): Bảo tàng - Khu bảo tồn A. A. Blok «Shakhmatovo» (huyện/okrug Solnechnogorsk)
        (museum/palace/park_garden) — điền trang mùa hè của thi hào Thời đại Bạc Aleksandr Blok, «góc thiên
        đường» của ông; khu bảo tồn 307 ha còn gồm điền trang Boblovo (nhà hoá học D. I. Mendeleev) và nhà thờ
        Tarakanovo nơi Blok kết hôn với L. Mendeleeva.
  2) Tỉnh Moskva (moscow-oblast): Tu viện Voznesenskaya Davidova Pustyn (làng Novy Byt, okrug Chekhov)
        (church/monument) — ẩn viện cổ lập năm 1515 bởi Thánh David bên sông Lopasnya; lưu giữ hài cốt Thánh
        David, hơn 200 thánh tích và một phần chiếc Đinh đóng đinh Chúa; điểm hành hương nổi tiếng phía nam Moskva.
  3) Tỉnh Leningrad (leningrad-oblast): Bảo tàng - Điền trang «Rozhdestveno» (okrug Gatchina)
        (museum/palace/park_garden) — dinh thự gỗ kiểu cổ điển cuối thế kỷ 18 gắn với đại văn hào Vladimir
        Nabokov (gia sản ông thừa kế năm 1916); công viên cổ với vách đá sa thạch đỏ, hang động bên sông Gryaznaya.

ĐỐI CHIẾU TRÁNH TRÙNG (đã quét slug + toàn văn JSON của file vùng + toàn CSDL 926 bản ghi, non-bak):
  - moscow-oblast.json (34 bản ghi): CHƯA có 'shakhmatovo/шахматово', 'davidova/давидова pustyn', 'bronnitsy'…
    ('kubinka' chỉ xuất hiện trong ĐỊA CHỈ của bản ghi armed-forces-cathedral = Công viên Patriot; KHÔNG phải
     tu viện/điền trang này — không trùng.)
  - leningrad-oblast.json (18 bản ghi): CHƯA có 'rozhdestveno/рождествено' hay 'nabokov/набоков'.
    ('blok/блок' trong file này là 'блокады' = cuộc phong toả Leningrad, KHÁC thi hào Blok — không liên quan.)
  - Gatchina (Cung điện Gatchina + Cung điện Priory) ĐÃ nằm ở saint-petersburg.json (cụm ngoại ô hoàng gia);
    Rozhdestveno là ĐIỀN TRANG RIÊNG ở làng Rozhdestveno cách Gatchina ~30 km — không trùng.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG sao chép/dịch nguyên văn), có ghi nguồn.

TOẠ ĐỘ THẬT — đối chiếu chéo ≥2 nguồn (thập phân WGS84), 2026-07:
  - Усадьба Шахматово (музей-заповедник А. А. Блока), д. Гудино, Солнечногорский р-н:  56.314589, 37.052254
        (2ГИС điểm đường đi N56.314598 E37.052249 ≈ Wikipedia 56°18′52″N 37°03′13″E; ~22 km bắc Solnechnogorsk)
  - Вознесенская Давидова пустынь, с. Новый Быт, г.о. Чехов:                          55.063935, 37.610412
        (KP.ru/2ГИС 55.063935,37.610412; Yandex org card ~55.0634,37.6110; ~85 km nam Moskva, bên sông Lopasnya)
  - Музей-усадьба «Рождествено», с. Рождествено, г.о. Гатчина, Лен. обл.:            59.325000, 29.935833
        (Wikipedia/РУВИКИ 59°19′30″N 29°56′09″E; ~30 km tây nam Gatchina trên tuyến P23)
Kiểm tra thứ tự lat/lon: lat 55-59 (∈41-70), lon 29-37 (∈19-180), KHÔNG đảo; đều nằm đúng phạm vi vùng.

LINK BẢN ĐỒ dạng TRỎ-ĐỊA-ĐIỂM:
  - Record 1 (Shakhmatovo): helper maps_text (text=tên+địa danh, ll=toạ độ đã kiểm chứng) — mở đúng thẻ địa điểm
        (không tra được org-id Yandex riêng cho điền trang này).
  - Record 2 (Davidova pustyn): URL TRANG TỔ CHỨC Yandex (org 1000307148) — chính xác nhất.
  - Record 3 (Rozhdestveno):   URL TRANG TỔ CHỨC Yandex (org 65101278888) — chính xác nhất.
  Cả 3 vẫn LƯU coordinates{lat,lon} chuẩn cho bản đồ nội bộ/GIS.

Chạy:  python3 tools/_add_three_places_aj.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"


def _google(name_en, region_en):
    parts = [name_en]
    if region_en.lower() not in name_en.lower():
        parts.append(region_en)
    parts.append("Russia")
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(", ".join(parts))


def maps_text(name_ru, region_ru, name_en, region_en, lat, lon):
    """Trỏ thẳng tới địa điểm bằng tên + canh giữa theo toạ độ (khớp retrofit_map_links.py)."""
    yq = urllib.parse.quote(f"{name_ru}, {region_ru}")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": _google(name_en, region_en),
    }


# ============================================================ RECORD 1
SHAKHMATOVO = {
    "id": "moscow-oblast-shakhmatovo-blok-museum-reserve",
    "slug": "shakhmatovo-blok-museum-reserve",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng - Khu bảo tồn A. A. Blok «Shakhmatovo»",
    "name_ru": "Государственный историко-литературный и природный музей-заповедник А. А. Блока «Шахматово»",
    "name_en": "Shakhmatovo — Alexander Blok Memorial Estate-Museum",
    "categories": ["museum", "palace", "park_garden"],
    "coordinates": {"lat": 56.314589, "lon": 37.052254},
    "address_vi": (
        "Деревня Гудино (làng Gudino), thành phố (okrug) Solnechnogorsk, Tỉnh Moskva; điền trang Shakhmatovo "
        "nằm cách làng Gudino khoảng 1 km về phía tây, gần làng Tarakanovo, cách Solnechnogorsk chừng 22 km về "
        "phía bắc theo đường Tarakanovskoye. Từ Moskva khoảng 85-90 km về hướng tây bắc."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Shakhmatovo là điền trang mùa hè của đại thi hào Thời đại Bạc Aleksandr Blok - nơi ông trìu mến gọi là "
        "«góc thiên đường» và gắn bó mỗi mùa hè từ thời thơ ấu cho đến năm 1916. Nằm giữa vùng đồi rừng thơ mộng "
        "phía bắc Solnechnogorsk, khu bảo tồn rộng 307 ha tái hiện ngôi nhà gỗ do chính Blok thiết kế lại năm 1910 "
        "(bị đốt năm 1921, phục dựng năm 2001) cùng các công trình phụ, khu vườn và cảnh quan đã đi vào thơ ông. "
        "Cụm bảo tàng còn bao gồm điền trang Boblovo của nhà hoá học lừng danh D. I. Mendeleev và nhà thờ Mikhail "
        "Arkhangel ở Tarakanovo - nơi Blok kết hôn với Lyubov Mendeleeva năm 1903."
    ),
    "presentation_long_vi": (
        "Điền trang Shakhmatovo được ông ngoại của Blok - nhà thực vật học nổi tiếng A. N. Beketov - mua lại năm "
        "1874. Từ năm 1881 đến 1916, cậu bé rồi chàng thi sĩ Aleksandr Blok hầu như mùa hè nào cũng về đây; khung "
        "cảnh đồng quê, những cánh rừng và con đường sắt gần đó đã hoá thành hình ảnh trong nhiều bài thơ trứ danh "
        "của ông. Năm 1910, Blok tự tay vẽ kiểu và cho xây lại ngôi nhà gỗ chính theo thiết kế riêng. Sau Cách mạng, "
        "năm 1921 điền trang bị nông dân địa phương đốt cháy; suốt nhiều thập niên nơi này chỉ còn là phế tích nhưng "
        "vẫn trở thành điểm hành hương của những người yêu thơ Blok. Nhà nước lập khu bảo tồn năm 1981 với diện tích "
        "được bảo vệ 307 ha, bao trùm cả điền trang Shakhmatovo lẫn làng Tarakanovo. Ngôi nhà chính được phục dựng "
        "và mở cửa năm 2001; từ đó tổ chức tham quan, sự kiện và lễ hội thơ thường niên. Khu bảo tồn thực chất là "
        "một cụm ba điền trang liên kết: Shakhmatovo (Blok), Boblovo (dành cho nhà hoá học D. I. Mendeleev - người "
        "có con gái Lyubov là vợ Blok) và Tarakanovo với nhà thờ Mikhail Arkhangel, nơi diễn ra hôn lễ của Blok và "
        "Lyubov Mendeleeva năm 1903. Đến Shakhmatovo, du khách vừa được thấy đời sống một điền trang trí thức Nga "
        "cuối thế kỷ 19 - đầu thế kỷ 20, vừa đắm mình trong chính khung cảnh thiên nhiên đã nuôi dưỡng thơ ca của "
        "một trong những nhà thơ lớn nhất nước Nga."
    ),
    "highlights_vi": [
        "Ngôi nhà gỗ chính do chính Blok thiết kế lại năm 1910, được phục dựng năm 2001 - cùng các công trình phụ và khu vườn từng đi vào thơ ông.",
        "Khu bảo tồn 307 ha gồm ba điền trang liên kết: Shakhmatovo (Blok), Boblovo (nhà hoá học D. I. Mendeleev) và Tarakanovo với nhà thờ Mikhail Arkhangel - nơi Blok cưới Lyubov Mendeleeva năm 1903.",
        "Khung cảnh đồi rừng «góc thiên đường» đặc trưng miền quê Nga cùng lễ hội thơ Blok truyền thống - một trong những điểm hành hương văn học nổi tiếng vùng ngoại vi Moskva.",
    ],
    "practical": {
        "hours_vi": "Thường mở cửa Thứ Tư - Chủ Nhật, khoảng 9:30-18:00 (nghỉ Thứ Hai và Thứ Ba); lịch có thể thay đổi theo mùa nên kiểm tra trước khi đến.",
        "ticket_vi": "Có thu phí; vé phổ thông từ khoảng 150 rúp. Có nhiều mức vé và tour có hướng dẫn cho từng điền trang (Shakhmatovo, Boblovo); giá thay đổi theo thời điểm.",
        "duration_vi": "Khoảng 2-3 giờ cho riêng Shakhmatovo; nửa ngày đến trọn ngày nếu kết hợp thăm Boblovo và nhà thờ Tarakanovo.",
        "best_time_vi": "Cuối xuân đến đầu thu khi vườn và rừng xanh mướt đúng như khung cảnh trong thơ Blok; mùa lễ hội thơ (thường vào tháng 8) có không khí đặc biệt.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô (elektrichka) tuyến Leningradsky đến ga Podsolnechnaya (Solnechnogorsk) rồi bắt xe buýt/taxi theo đường Tarakanovskoye; hoặc tự lái ~1,5 giờ. Nhiều lối trong khu bảo tồn là đường đất, nên đi giày thoải mái. Có thể gộp Boblovo và nhà thờ Tarakanovo trong cùng chuyến.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text(
        "Музей-заповедник А. А. Блока «Шахматово»", "Гудино, Солнечногорск, Московская область",
        "Shakhmatovo Estate (Alexander Blok Museum-Reserve)", "Gudino, Moscow Oblast",
        56.314589, 37.052254,
    ),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Шахматово", "url": "https://ru.wikipedia.org/wiki/Шахматово"},
        {"title": "Культура.РФ — Музей-заповедник Д. И. Менделеева и А. А. Блока (усадьба Шахматово)", "url": "https://www.culture.ru/institutes/22098/muzei-zapovednik-d-i-mendeleeva-i-a-a-bloka-usadba-shakhmatovo"},
        {"title": "RUSSPASS — Усадьба Шахматово (giờ mở cửa, toạ độ)", "url": "https://russpass.ru/event/6387856d810482a5a13da408"},
    ],
    "tags": ["blok", "literature", "silver-age", "estate", "museum", "park", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

# ============================================================ RECORD 2
DAVIDOVA_PUSTYN = {
    "id": "moscow-oblast-voznesenskaya-davidova-pustyn",
    "slug": "voznesenskaya-davidova-pustyn",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Tu viện Voznesenskaya Davidova Pustyn (Ẩn viện Thánh David - Chúa Thăng Thiên)",
    "name_ru": "Вознесенская Давидова пустынь",
    "name_en": "Ascension David Hermitage (Voznesenskaya Davidova Pustyn)",
    "categories": ["church", "monument"],
    "coordinates": {"lat": 55.063935, "lon": 37.610412},
    "address_vi": (
        "Село Новый Быт (làng Novy Byt), thành phố (okrug) Chekhov, Tỉnh Moskva; toạ lạc bên bờ sông Lopasnya "
        "(phụ lưu sông Oka), cách Moskva khoảng 85 km về phía nam và cách Serpukhov chừng 24 km."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Đây là một trong những tu viện cổ và được sùng kính bậc nhất phía nam Tỉnh Moskva, do Thánh David "
        "(Prepodobny David) lập năm 1515 bên bờ sông Lopasnya. Tương truyền chính Thánh David đã tự tay trồng "
        "những hàng cây bồ đề (đoan) quanh ẩn viện. Quần thể quy tụ nhiều nhà thờ thuộc các thời kỳ khác nhau với "
        "gam màu sáng nổi bật, lưu giữ hài cốt Thánh David cùng hơn 200 thánh tích các thánh và một phần chiếc Đinh "
        "đóng đinh Chúa - điểm hành hương quan trọng, chỉ cách Moskva chừng 85 km."
    ),
    "presentation_long_vi": (
        "Theo truyền thống, năm 1515 Thánh David cùng vài môn đệ đã tới vùng đất bên sông Lopasnya và dựng nhà thờ "
        "gỗ đầu tiên kính Chúa Thăng Thiên (Voznesenie) - khởi đầu cho ẩn viện mang tên ngài. Qua nhiều thế kỷ, tu "
        "viện lớn dần thành một quần thể gồm nhà thờ chính Chúa Thăng Thiên, nhà thờ Znamenie, nhà thờ Thánh Nikolai, "
        "nhà thờ Các Thánh cùng tháp chuông, được xây dựng và tu bổ qua các thời kỳ nên mang phong cách kiến trúc "
        "đa dạng. Dưới thời Xô Viết, tu viện bị đóng cửa (cuối thập niên 1920) và các công trình bị sử dụng cho nhiều "
        "mục đích khác, hư hại nhiều; đời sống đan tu chỉ được khôi phục từ năm 1995. Ngày nay đây là tu viện nam "
        "đang hoạt động thuộc giáo phận Podolsk của Giáo hội Chính Thống Nga và là di sản văn hoá cấp liên bang. Tu "
        "viện nổi tiếng nhờ kho thánh tích phong phú: hài cốt của chính Thánh David - người sáng lập, hơn 200 phần "
        "thánh tích của các thánh, và theo tu viện còn lưu giữ một phần chiếc Đinh đóng đinh Chúa Giêsu trong một "
        "hòm thánh tích riêng. Không gian yên tĩnh bên sông Lopasnya cùng những hàng cây cổ thụ khiến nơi đây trở "
        "thành điểm hành hương và tham quan được yêu thích, thuận tiện kết hợp trong hành trình về phía nam Moskva "
        "qua Chekhov - Serpukhov."
    ),
    "highlights_vi": [
        "Quần thể ẩn viện thành lập năm 1515 bởi Thánh David - một trong những tu viện cổ kính và linh thiêng nhất phía nam Tỉnh Moskva.",
        "Kho thánh tích quý: hài cốt Thánh David, hơn 200 phần thánh tích các thánh và (theo tu viện) một phần chiếc Đinh đóng đinh Chúa Giêsu.",
        "Cụm nhà thờ nhiều thời kỳ (nhà thờ chính Chúa Thăng Thiên, Znamenie, Thánh Nikolai…) bên sông Lopasnya cùng những hàng cây bồ đề cổ theo truyền thuyết do Thánh David trồng.",
    ],
    "practical": {
        "hours_vi": "Là tu viện đang hoạt động, mở cửa hằng ngày cho khách hành hương từ khoảng 7:45 đến hết buổi lễ chiều; giờ lễ thay đổi theo lịch phụng vụ.",
        "ticket_vi": "Vào cửa tự do (khuyến khích công đức tuỳ tâm); có thể liên hệ trước nếu muốn tham quan có hướng dẫn hoặc đi theo đoàn hành hương.",
        "duration_vi": "Khoảng 1-2 giờ để dạo quanh quần thể nhà thờ và khu thánh tích.",
        "best_time_vi": "Quanh năm; các dịp đại lễ Chính Thống giáo và ngày kính Thánh David không khí đặc biệt trang nghiêm, đông khách hành hương.",
        "tips_vi": "Trang phục kín đáo; nữ nên mang khăn trùm đầu và váy/quần dài. Từ Moskva thuận tiện nhất đi ô tô theo cao tốc M2 «Krym» hướng Chekhov rồi rẽ về Novy Byt (~1,5 giờ); hoặc đi tàu tới Chekhov rồi bắt xe buýt địa phương. Có thể kết hợp thăm thành phố Chekhov và điền trang Melikhovo gần đó.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": {
        # Task ƯU TIÊN URL trang tổ chức Yandex khi tra được org-id (chính xác nhất về vị trí thẻ địa điểm).
        "yandex": "https://yandex.com/maps/org/voznesenskaya_davidova_pustyn/1000307148/",
        "google": _google("Ascension David Hermitage (Davidova Pustyn)", "Novy Byt, Chekhov, Moscow Oblast"),
    },
    "official_site": "http://www.davidova-pustyn.ru/",
    "sources": [
        {"title": "Wikipedia (RU) — Вознесенская Давидова пустынь", "url": "https://ru.wikipedia.org/wiki/Вознесенская_Давидова_пустынь"},
        {"title": "Соборы.ру — Новый Быт, Вознесенская Давидова Пустынь", "url": "https://sobory.ru/article/?object=02624"},
        {"title": "Монастырский вестник — Вознесенская Давидова пустынь", "url": "https://monasterium.ru/monastyri/monastery/voznesenskaya-davidova-pustyn/"},
        {"title": "Trang chính thức — Вознесенская Давидова пустынь (davidova-pustyn.ru)", "url": "http://www.davidova-pustyn.ru/"},
    ],
    "tags": ["monastery", "church", "orthodox", "pilgrimage", "relics", "history", "chekhov", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

# ============================================================ RECORD 3
ROZHDESTVENO = {
    "id": "leningrad-oblast-rozhdestveno-nabokov-estate",
    "slug": "rozhdestveno-nabokov-estate",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Bảo tàng - Điền trang «Rozhdestveno» (gắn với V. V. Nabokov)",
    "name_ru": "Музей-усадьба «Рождествено»",
    "name_en": "Rozhdestveno Museum-Estate (Vladimir Nabokov)",
    "categories": ["museum", "palace", "park_garden"],
    "coordinates": {"lat": 59.325000, "lon": 29.935833},
    "address_vi": (
        "Село Рождествено (làng Rozhdestveno), ул. Музейная, д. 1, thành phố (okrug) Gatchina, Tỉnh Leningrad; "
        "nằm trên tuyến quốc lộ P23 (Kiyevskoye) phía tây nam Gatchina, cách Gatchina khoảng 30 km và cách Saint "
        "Petersburg chừng 70 km."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Rozhdestveno là toà dinh thự gỗ kiểu cổ điển hiếm hoi cuối thế kỷ 18, nổi bật với hàng cột trắng như một "
        "«ngôi đền» giữa vùng quê Tỉnh Leningrad. Điền trang gắn liền với đại văn hào Vladimir Nabokov: đây là gia "
        "sản ông thừa kế năm 1916 từ người cậu V. I. Rukavishnikov, và cả vùng Rozhdestveno - Vyra - Batovo đã trở "
        "thành «thiên đường tuổi thơ» in đậm trong hồi ký nổi tiếng của ông. Sau trận hoả hoạn năm 1995, toà nhà "
        "đã được phục dựng công phu và mở cửa làm bảo tàng, giữa một công viên cổ với vách đá sa thạch đỏ và hang "
        "động bên sông Gryaznaya."
    ),
    "presentation_long_vi": (
        "Toà nhà chính của điền trang Rozhdestveno là một dinh thự gỗ mang phong cách cổ điển (classicism), dựng vào "
        "cuối thế kỷ 18 với hàng cột và mái vòm khiến nó trông tựa một ngôi đền cổ - kiểu kiến trúc điền trang bằng "
        "gỗ nay còn lại rất ít ở Nga. Trong thế kỷ 19 - đầu thế kỷ 20, điền trang thuộc về dòng họ Rukavishnikov - "
        "gia đình bên ngoại của Vladimir Nabokov. Năm 1916, chàng thanh niên Nabokov thừa kế Rozhdestveno từ người "
        "cậu Vasily Ivanovich Rukavishnikov; cùng với điền trang Vyra (của mẹ ông) và Batovo (của bà ngoại) ở ngay "
        "gần, vùng quê này trở thành khung cảnh tuổi thơ mà về sau ông tái hiện đầy hoài niệm trong cuốn hồi ký "
        "«Speak, Memory» (bản tiếng Nga «Những bến bờ khác»). Chỉ hơn một năm sau, Cách mạng 1917 buộc gia đình "
        "Nabokov lưu vong, điền trang bị quốc hữu hoá và trải qua nhiều công năng. Toà nhà bắt đầu được dùng làm bảo "
        "tàng từ thập niên 1970 và dần chuyển trọng tâm sang đề tài Nabokov. Tháng 4 năm 1995, một trận hoả hoạn lớn "
        "đã thiêu rụi phần lớn dinh thự; công cuộc phục dựng tỉ mỉ sau đó đã trả lại diện mạo cho công trình. Bao "
        "quanh nhà là công viên cổ rộng khoảng 16 ha với những cây đoan (bồ đề) và sồi hàng trăm năm tuổi, dẫn tới "
        "hẻm sông Gryaznaya nơi có vách đá sa thạch đỏ, các mạch nước ngầm và hệ hang động - một cảnh quan thiên "
        "nhiên độc đáo hiếm thấy ở vùng tây bắc nước Nga. Ngày nay bảo tàng là một chi nhánh trong hệ thống bảo tàng "
        "của Tỉnh Leningrad."
    ),
    "highlights_vi": [
        "Toà dinh thự gỗ kiểu cổ điển cuối thế kỷ 18 với hàng cột trắng đặc trưng - một trong số ít «điền trang - đền thờ» bằng gỗ còn lại ở Nga, phục dựng sau hoả hoạn năm 1995.",
        "Gắn với Vladimir Nabokov: gia sản ông thừa kế năm 1916 và vùng quê tuổi thơ (Rozhdestveno - Vyra - Batovo) đi vào hồi ký «Speak, Memory» nổi tiếng của ông.",
        "Công viên cổ ~16 ha với cây đoan, sồi hàng trăm năm tuổi cùng vách đá sa thạch đỏ, mạch nước ngầm và hang động bên sông Gryaznaya.",
    ],
    "practical": {
        "hours_vi": "Bảo tàng thường mở cửa hằng ngày trừ ngày nghỉ cố định (thường nghỉ Thứ Hai - Thứ Ba và một ngày cuối tháng để vệ sinh); nên kiểm tra lịch trước khi đến.",
        "ticket_vi": "Có thu phí, giá vé phổ thông ở mức vừa phải; có vé riêng cho tham quan toà nhà và dạo công viên, cùng các tour có hướng dẫn.",
        "duration_vi": "Khoảng 1,5-2 giờ cho toà nhà và công viên; lâu hơn nếu khám phá vách đá, hang động và mạch nước ven sông.",
        "best_time_vi": "Cuối xuân đến đầu thu để dạo công viên và ngắm vách đá đỏ ven sông; mùa thu lá vàng đặc biệt đẹp.",
        "tips_vi": "Từ Saint Petersburg đi tàu ngoại ô hướng Luga/Oredezh hoặc xe buýt về Rozhdestveno (~1,5 giờ); nếu tự lái theo quốc lộ P23 (Kiyevskoye). Có thể kết hợp thăm điền trang Vyra (Bảo tàng «Nhà trạm bưu chính») và cảnh quan sông Oredezh gần đó. Lối xuống vách đá và hang khá trơn - nên đi giày bám tốt.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": {
        # Task ƯU TIÊN URL trang tổ chức Yandex khi tra được org-id (chính xác nhất về vị trí thẻ địa điểm).
        "yandex": "https://yandex.com/maps/org/muzey_usadba_rozhdestveno/65101278888/",
        "google": _google("Rozhdestveno Museum-Estate (Nabokov)", "Gatchina District, Leningrad Oblast"),
    },
    "official_site": None,
    "sources": [
        {"title": "Культура.РФ — Музей-усадьба «Рождествено»", "url": "https://www.culture.ru/institutes/11135/muzei-usadba-rozhdestveno"},
        {"title": "ГМЗ «Гатчина» — Музей-усадьба «Рождествено»", "url": "https://gatchinapalace.ru/visitors/okrest_ARHIV/rozdestveno.php"},
        {"title": "РУВИКИ — Рождествено (музей-усадьба)", "url": "https://ru.ruwiki.ru/wiki/Рождествено_(музей-усадьба)"},
    ],
    "tags": ["nabokov", "literature", "estate", "museum", "classicism", "park", "day-trip", "leningrad-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


# ------------------------------------------------------------------ PLAN
PLAN = {
    "moscow-oblast.json": [SHAKHMATOVO, DAVIDOVA_PUSTYN],
    "leningrad-oblast.json": [ROZHDESTVENO],
}


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
                print(f"  = BỎ QUA (đã có): {fname} :: {r['slug']}")
                continue
            to_add.append(r)
        if not to_add:
            continue
        bak = path + f".bak_add_{TS}"
        with open(bak, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        arr.extend(to_add)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        total_added += len(to_add)
        print(f"  + {fname}: thêm {len(to_add)} địa điểm -> tổng {len(arr)} (backup: {os.path.basename(bak)})")
        for r in to_add:
            print(f"        - {r['name_vi']}  [{','.join(r['categories'])}]  ({r['coordinates']['lat']},{r['coordinates']['lon']})")

    print(f"\nTổng đã thêm lần này: {total_added} địa điểm.")


if __name__ == "__main__":
    main()
