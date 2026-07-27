# -*- coding: utf-8 -*-
"""_add_three_places_ah.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26).

Ưu tiên VÙNG (a): thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.
Cả 3 địa điểm lần này đều thuộc Tỉnh Moskva (moscow-oblast) — các danh thắng A-list còn thiếu:

Thêm:
  1) Tỉnh Moskva (moscow-oblast): Bảo tàng - Khu bảo tồn A. S. Pushkin — Điền trang Vyazyomy & Zakharovo
        (museum/palace/park_garden/church) — nơi DUY NHẤT ở ngoại ô Moskva gắn với tuổi thơ Pushkin;
        cung điện Golitsyn thế kỷ 18 + nhà thờ Spaso-Preobrazhensky thời Boris Godunov.
  2) Tỉnh Moskva (moscow-oblast): Điền trang Serednikovo (gắn với M. Yu. Lermontov)
        (palace/park_garden) — quần thể cổ điển cuối thế kỷ 18 của dòng họ Stolypin; các mùa hè
        1829-1832 của Lermontov; nay là trung tâm văn hoá & phim trường nổi tiếng.
  3) Tỉnh Moskva (moscow-oblast): Bảo tàng Đồ chơi Nghệ thuật - Sư phạm (Sergiev Posad)
        (museum) — một trong những bảo tàng đồ chơi lâu đời nhất thế giới (1918), chuyển về SP năm 1931.

ĐỐI CHIẾU TRÁNH TRÙNG (đã quét slug/name toàn bộ file vùng + toàn CSDL, non-bak):
  - moscow-oblast.json (28 bản ghi): CHƯA có Vyazyomy/Zakharovo, Serednikovo, hay Bảo tàng Đồ chơi.
    (Có 'trinity-lavra-sergiev-posad' nhưng đó là TU VIỆN, không phải Bảo tàng Đồ chơi.)
  - Quét toàn CSDL: 'vyazyomy', 'zakharovo', 'serednikovo' -> KHÔNG trùng ở bất kỳ file nào.
  - Gatchina/Priory ĐÃ nằm ở saint-petersburg.json -> KHÔNG đụng tới.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, không sao chép nguyên văn), có ghi nguồn.

TOẠ ĐỘ THẬT — đối chiếu web 2026-07 (thập phân WGS84):
  - Усадьба Вязёмы (Большие Вязёмы, Одинцовский г.о.):  55.620000, 36.980000
        (ru.wikipedia «Вязёмы (усадьба)»: 55°37′12″ с.ш., 36°58′48″ в.д.; ven sông Вязёмка, ~30 km từ MKAD)
  - Усадьба Середниково (г.о. Солнечногорск):           55.928430, 37.241360
        (Wikidata Q2970685: 55°55′42.348″N, 37°14′28.896″E; gần ga Фирсановка, sát Zelenograd)
  - Музей игрушки (Сергиев Посад, пр. Красной Армии 123): 56.310750, 38.133040
        (đồi Конная Гора, tả ngạn hồ, ngay đối diện Trinity Lavra ở 56.3103,38.1312)
Kiểm tra thứ tự lat/lon: lat 55-56 (∈41-70), lon 36-38 (∈19-180), KHÔNG đảo; đều nằm trong phạm vi vùng.

LINK BẢN ĐỒ dạng TRỎ-ĐỊA-ĐIỂM: helper maps_text (text=tên+thành phố, ll=toạ độ đã kiểm chứng) —
mở đúng thẻ địa điểm và canh giữa bản đồ. coordinates{lat,lon} vẫn LƯU chuẩn cho GIS nội bộ.

Chạy:  python3 tools/_add_three_places_ah.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"


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
PUSHKIN_VYAZYOMY_ZAKHAROVO = {
    "id": "moscow-oblast-pushkin-museum-reserve-vyazyomy-zakharovo",
    "slug": "pushkin-museum-reserve-vyazyomy-zakharovo",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng - Khu bảo tồn A. S. Pushkin (Điền trang Vyazyomy và Zakharovo)",
    "name_ru": "Государственный историко-литературный музей-заповедник А. С. Пушкина (Вязёмы и Захарово)",
    "name_en": "A. S. Pushkin State Historical and Literary Museum-Reserve (Vyazyomy and Zakharovo)",
    "categories": ["museum", "palace", "park_garden", "church"],
    "coordinates": {"lat": 55.620000, "lon": 36.980000},
    "address_vi": (
        "Posёlok Bolshie Vyazyomy, thành phố (okrug) Odintsovo, Tỉnh Moskva (mã bưu chính 143050). "
        "Điền trang Vyazyomy nằm bên sông Vyazyomka sát cao tốc Mozhaysk (đường Smolensk cũ), cách Vành đai "
        "Moskva (MKAD) khoảng 30 km về phía tây; chi nhánh Zakharovo cách đó chừng 2-3 km."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Đây là nơi duy nhất ở ngoại ô Moskva gắn liền với tuổi thơ đại thi hào Aleksandr Pushkin. Khu bảo tồn "
        "hợp nhất hai điền trang lân cận: Vyazyomy - dinh cổ của dòng họ Golitsyn với cung điện thế kỷ 18 và nhà "
        "thờ Spaso-Preobrazhensky từ thời Boris Godunov - cùng Zakharovo, trang trại của bà ngoại Pushkin, nơi "
        "cậu bé Pushkin sống những mùa hè thơ ấu (1805-1810). Thành lập năm 1994, đây là một trong những bảo "
        "tàng văn học được yêu thích bậc nhất vùng Moskva."
    ),
    "presentation_long_vi": (
        "Vyazyomy (Вязёмы) được nhắc tới từ thế kỷ 16 như trạm dừng chân cuối cùng trước khi vào Moskva trên "
        "con đường lớn đi Smolensk. Cuối năm 1584, Sa hoàng Fyodor I ban vùng đất này cho anh vợ là Boris Godunov, "
        "người lập tức cho xây dựng quy mô lớn: nhà thờ năm mái Spaso-Preobrazhensky (thánh hiến năm 1600) cùng "
        "một звонница (tháp chuông) kiểu Pskov khác lạ so với kiến trúc vùng này - cả hai đến nay vẫn còn. Thời "
        "Loạn lạc (Smuta), Vyazyomy từng là hành cung của Lжедмитрий I. Năm 1694, Pyotr Đại đế ban điền trang cho "
        "công tước Boris Golitsyn, và từ đó Vyazyomy thành lãnh địa tổ truyền của dòng họ Golitsyn. Nửa sau thế kỷ "
        "18, dưới thời Nikolai Mikhailovich Golitsyn, toà cung điện đá và hai flügel theo phong cách cổ điển được "
        "dựng lên (hoàn tất khoảng năm 1784), kèm một công viên quy hoạch đều đặn. Tháng 9 năm 1812, ngay sau trận "
        "Borodino, đại bản doanh của Nguyên soái Kutuzov đặt tại Bolshie Vyazyomy; chỉ ít lâu sau, chính Napoleon "
        "cũng dừng chân tại dinh thự này trên đường tiến vào Moskva. Sợi dây gắn Vyazyomy với văn chương Nga đến từ "
        "điền trang Zakharovo cách đó vài cây số - nơi bà ngoại của Pushkin là Maria Alekseevna Gannibal sở hữu, và "
        "cậu bé Aleksandr đã trải qua những mùa hè tuổi thơ (1805-1810) trước khi vào trường Lyceum. Bên tường nhà "
        "thờ Vyazyomy còn có mộ người em trai yểu mệnh của thi hào - Nikolai Pushkin (1801-1807). Suốt thời Xô Viết, "
        "điền trang lần lượt là trại trẻ mồ côi, trường nhảy dù, trường tăng thiết giáp rồi các viện nghiên cứu. Cuối "
        "thập niên 1980, nhờ công của giới sử học địa phương, một bảo tàng nhân dân ra đời; đến năm 1994, hai điền "
        "trang Vyazyomy và Zakharovo chính thức hợp thành Khu bảo tồn lịch sử - văn học quốc gia mang tên A. S. "
        "Pushkin, với hơn hai mươi di tích lịch sử - văn hoá. Trong cung điện Golitsyn có phòng trưng bày nội thất "
        "tái hiện đời sống điền trang thời Pushkin cùng trưng bày tương tác «Những bức tranh sống dậy»; còn ở Zakharovo, "
        "ngôi nhà gỗ của bà Gannibal được phục dựng năm 1999, gợi lại không gian tuổi thơ của nhà thơ. Vào đầu tháng "
        "Sáu hằng năm, nơi đây tổ chức Ngày hội thơ Pushkin thu hút đông đảo du khách."
    ),
    "highlights_vi": [
        "Cung điện Golitsyn cổ điển (hoàn tất ~1784) cùng hai flügel; bên trong là trưng bày nội thất tái hiện đời sống điền trang thời Pushkin và trưng bày tương tác «Những bức tranh sống dậy».",
        "Nhà thờ Spaso-Preobrazhensky cuối thế kỷ 16 (thánh hiến 1600) và tháp chuông kiểu Pskov - kiệt tác kiến trúc thời Boris Godunov; bên tường có mộ em trai Pushkin là Nikolai (1801-1807).",
        "Điền trang Zakharovo gần đó - «quê ngoại» nơi Pushkin sống những mùa hè tuổi thơ 1805-1810; nhà gỗ của bà ngoại Gannibal được phục dựng năm 1999.",
    ],
    "practical": {
        "hours_vi": "Cung điện Vyazyomy và nhà Zakharovo thường mở cửa thứ Tư - Chủ nhật, khoảng 10:00-17:00; đóng cửa thứ Hai, thứ Ba và ngày vệ sinh cuối tháng. Nên kiểm tra lịch trên trang chính thức trước khi đến.",
        "ticket_vi": "Bán vé riêng cho khu Vyazyomy và khu Zakharovo, cùng vé gộp và vé tour có hướng dẫn; nhiều mức ưu đãi cho học sinh, sinh viên, người hưu trí.",
        "duration_vi": "Khoảng 2-3 giờ nếu thăm cả cung điện, nhà thờ và công viên Vyazyomy; nên dành thêm thời gian nếu ghé cả Zakharovo.",
        "best_time_vi": "Cuối xuân đến đầu thu; công viên và ao hồ đặc biệt đẹp mùa hè và mùa thu lá vàng, cũng là dịp có Ngày hội thơ Pushkin đầu tháng Sáu.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô từ ga Belorussky tới ga Golitsyno, rồi đi bộ/xe buýt tới Vyazyomy; hoặc ô tô theo cao tốc Mozhayskoye/Minskoye. Có thể kết hợp thăm cả Vyazyomy và Zakharovo trong cùng nửa ngày.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text(
        "Музей-заповедник А. С. Пушкина, усадьба Вязёмы", "Большие Вязёмы, Московская область",
        "Pushkin Museum-Reserve, Vyazyomy Estate", "Bolshiye Vyazyomy, Moscow Oblast",
        55.620000, 36.980000,
    ),
    "official_site": "https://museum-gol.ru/",
    "sources": [
        {"title": "Wikipedia (RU) — Вязёмы (усадьба)", "url": "https://ru.wikipedia.org/wiki/Вязёмы_(усадьба)"},
        {"title": "Wikipedia (EN) — Bolshiye Vyazyomy", "url": "https://en.wikipedia.org/wiki/Bolshiye_Vyazyomy"},
        {"title": "Trang chính thức — Музей-заповедник А. С. Пушкина (museum-gol.ru)", "url": "https://museum-gol.ru/"},
    ],
    "tags": ["museum", "estate", "palace", "literary", "pushkin", "golitsyn", "church", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

# ============================================================ RECORD 2
SEREDNIKOVO_ESTATE = {
    "id": "moscow-oblast-serednikovo-estate",
    "slug": "serednikovo-estate",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Điền trang Serednikovo (gắn với M. Yu. Lermontov)",
    "name_ru": "Усадьба Середниково",
    "name_en": "Serednikovo Estate",
    "categories": ["palace", "park_garden"],
    "coordinates": {"lat": 55.928430, "lon": 37.241360},
    "address_vi": (
        "Gần ga Firsanovka, thành phố (okrug) Solnechnogorsk, Tỉnh Moskva; cách Vành đai Moskva (MKAD) khoảng "
        "20-25 km về phía tây bắc, sát ranh giới thành phố Zelenograd, bên bờ sông Skhodnya."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Serednikovo là một trong những quần thể điền trang cổ điển đẹp và nguyên vẹn nhất quanh Moskva: toà nhà "
        "chính nối với các flügel bằng những hành lang cong có mái, giữa công viên rợp bóng cây, hồ nước và cây "
        "cầu đá lãng mạn. Nơi đây gắn với thời niên thiếu của thi hào Mikhail Lermontov, người đã trải qua các "
        "mùa hè 1829-1832 tại đây và viết những vần thơ đầu tay; ngày nay điền trang là trung tâm văn hoá và một "
        "phim trường quen thuộc của điện ảnh Nga."
    ),
    "presentation_long_vi": (
        "Quần thể kiến trúc - cảnh quan Serednikovo hình thành vào cuối thế kỷ 18 theo phong cách cổ điển: một "
        "toà nhà chính hai tầng đặt trên gò cao, nối với bốn flügel đối xứng bằng các hành lang cong có hàng cột, "
        "nhìn xuống hệ thống hồ và công viên trải dài. Trong công viên còn có nhà thờ, chuồng ngựa (manège) và mấy "
        "cây cầu đá, nổi tiếng nhất là «Cầu Quỷ» (Chyortov most) duyên dáng bắc qua khe suối. Đầu thế kỷ 19, điền "
        "trang thuộc về dòng họ Stolypin - họ hàng bên ngoại của Lermontov: bà ngoại nhà thơ, Elizaveta Arsenyeva "
        "(nhũ danh Stolypina), thường đưa cháu về đây nghỉ hè. Từ năm 1829 đến 1832, chàng thiếu niên Mikhail "
        "Lermontov đã sống những mùa hè ở Serednikovo, đọc sách say mê và tập viết những bài thơ đầu tiên - vì thế "
        "điền trang được coi là một trong những «cái nôi» của thơ ca Lermontov. Sang đầu thế kỷ 20, Serednikovo "
        "thuộc quyền nữ doanh nhân giàu có Vera Firsanova, người cho trùng tu toàn bộ quần thể và năm 1914, nhân "
        "kỷ niệm 100 năm ngày sinh Lermontov, đã dựng một đài tưởng niệm nhà thơ trong khuôn viên (ga xe lửa "
        "Firsanovka gần đó cũng mang tên dòng họ này). Thời Xô Viết, điền trang trở thành nhà điều dưỡng mang tên "
        "«Mtsyri» - theo tên trường ca nổi tiếng của Lermontov. Sau nhiều năm xuống cấp, Serednikovo được trùng tu "
        "và hồi sinh thành một trung tâm văn hoá quốc gia gắn với tên tuổi Lermontov; nhờ kiến trúc cổ điển nguyên "
        "vẹn và khung cảnh nên thơ, nơi đây trở thành phim trường quen thuộc cho hàng loạt phim lịch sử và cổ trang "
        "của điện ảnh Nga, đồng thời là điểm dạo chơi - chụp ảnh lý tưởng cho chuyến đi trong ngày từ thủ đô."
    ),
    "highlights_vi": [
        "Quần thể cổ điển cuối thế kỷ 18: toà nhà chính nối với các flügel bằng hành lang cong có hàng cột, giữa công viên, hồ nước và cây cầu đá «Cầu Quỷ» (Chyortov most) lãng mạn.",
        "Gắn với thời niên thiếu của thi hào Mikhail Lermontov (các mùa hè 1829-1832), nơi ông viết những bài thơ đầu tay; đài tưởng niệm Lermontov do bà Vera Firsanova dựng năm 1914.",
        "Từng thuộc dòng họ Stolypin rồi Firsanov; thời Xô Viết là nhà điều dưỡng «Mtsyri», nay là trung tâm văn hoá và phim trường quen thuộc của điện ảnh Nga.",
    ],
    "practical": {
        "hours_vi": "Khuôn viên công viên thường mở cửa hằng ngày; việc vào thăm toà nhà chính thường theo tour có hướng dẫn và có thể hạn chế vào những ngày diễn ra quay phim hoặc sự kiện. Nên kiểm tra lịch trên trang chính thức trước khi đến.",
        "ticket_vi": "Có thu phí vào cửa khu điền trang và vé riêng cho tour tham quan nội thất/các chương trình; giá thay đổi theo mùa và sự kiện.",
        "duration_vi": "Khoảng 1,5-2,5 giờ cho toà nhà chính, công viên, hồ và các cây cầu.",
        "best_time_vi": "Cuối xuân đến đầu thu, khi công viên xanh mát; mùa thu lá vàng đặc biệt hợp cho chụp ảnh.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô từ ga Leningradsky tới ga Firsanovka, rồi bắt xe buýt/taxi vài km tới điền trang; hoặc ô tô theo cao tốc Leningradskoye. Kiểm tra trước lịch quay phim/sự kiện vì có thể ảnh hưởng đến việc tham quan.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text(
        "Усадьба Середниково", "городской округ Солнечногорск, Московская область",
        "Serednikovo Estate", "Solnechnogorsk, Moscow Oblast",
        55.928430, 37.241360,
    ),
    "official_site": "https://serednikovo.su/",
    "sources": [
        {"title": "Wikidata — Serednikovo (Q2970685)", "url": "https://www.wikidata.org/wiki/Q2970685"},
        {"title": "Trang chính thức — Усадьба Середниково (serednikovo.su)", "url": "https://serednikovo.su/the-estate-serednikovo"},
        {"title": "Moscovery — Serednikovo Estate (Lermontov)", "url": "https://www.moscovery.com/serednikovo-estate/"},
    ],
    "tags": ["estate", "palace", "park", "literary", "lermontov", "stolypin", "film-location", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

# ============================================================ RECORD 3
TOY_MUSEUM_SERGIEV_POSAD = {
    "id": "moscow-oblast-toy-museum-sergiev-posad",
    "slug": "toy-museum-sergiev-posad",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng Đồ chơi Nghệ thuật - Sư phạm (Sergiev Posad)",
    "name_ru": "Художественно-педагогический музей игрушки имени Н. Д. Бартрама",
    "name_en": "Art and Pedagogical Museum of Toys (Sergiev Posad)",
    "categories": ["museum"],
    "coordinates": {"lat": 56.310750, "lon": 38.133040},
    "address_vi": (
        "Проспект Красной Армии, số 123, thành phố Sergiev Posad, Tỉnh Moskva (mã bưu chính 141300); toà nhà gạch "
        "đỏ trên đồi Konnaya Gora ở tả ngạn hồ, nhìn thẳng sang quần thể Tu viện Trinity Lavra."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Đây là một trong những bảo tàng đồ chơi lâu đời nhất thế giới, do hoạ sĩ Nikolai Bartram sáng lập tại "
        "Moskva năm 1918 và chuyển về Sergiev Posad năm 1931. Bộ sưu tập đồ sộ gồm hàng chục nghìn món: đồ chơi "
        "dân gian Nga, matryoshka và đồ gỗ Sergiev Posad, búp bê Tây Âu, cùng cả những món đồ chơi từng thuộc về "
        "các con của Nga hoàng Nikolai II. Toà nhà gạch đỏ trên đồi nhìn thẳng sang Tu viện Trinity Lavra."
    ),
    "presentation_long_vi": (
        "Bảo tàng Đồ chơi ra đời năm 1918 tại Moskva theo sáng kiến của hoạ sĩ - nhà sưu tầm Nikolai Dmitrievich "
        "Bartram, người dành cả đời nghiên cứu đồ chơi như một hiện tượng nghệ thuật và giáo dục. Năm 1931, bảo "
        "tàng được chuyển về Sergiev Posad (khi ấy mang tên Zagorsk) - vốn được coi là «thủ đô đồ chơi» của nước "
        "Nga, quê hương của nghề tiện gỗ và của con búp bê matryoshka. Bảo tàng đặt trong một toà nhà gạch đỏ đầu "
        "thế kỷ 20 trên đồi Konnaya Gora, ngay tả ngạn hồ, từ đây có thể nhìn bao quát quần thể Tu viện Trinity "
        "Lavra ở bờ bên kia. Bộ sưu tập tích luỹ qua hơn một thế kỷ nay lên tới hàng chục nghìn hiện vật, trải rộng "
        "từ đồ chơi dân gian Nga bằng gỗ và đất sét, đồ chơi tiện - sơn của chính Sergiev Posad, cho tới búp bê sứ "
        "và đồ chơi cơ khí tinh xảo của Tây Âu, đồ chơi phương Đông, cùng những bộ sưu tập gắn với lịch sử sư phạm. "
        "Một phần đặc biệt được nhiều người tìm đến là nhóm đồ chơi từng thuộc về các hoàng tử và công chúa - con "
        "của Nga hoàng Nikolai II, được chuyển về bảo tàng sau Cách mạng. Không chỉ trưng bày, bảo tàng còn giữ vai "
        "trò một trung tâm nghiên cứu và giáo dục về đồ chơi, thường tổ chức các chương trình cho trẻ em và gia "
        "đình. Nằm chỉ vài phút đi bộ từ Tu viện Trinity Lavra - trái tim tâm linh của Chính Thống giáo Nga và là "
        "Di sản Thế giới UNESCO - bảo tàng là điểm dừng chân thú vị, giàu màu sắc và rất hợp với các gia đình trong "
        "một ngày khám phá Sergiev Posad."
    ),
    "highlights_vi": [
        "Một trong những bảo tàng đồ chơi lâu đời nhất thế giới - thành lập năm 1918 tại Moskva bởi hoạ sĩ N. D. Bartram, chuyển về Sergiev Posad (Zagorsk) năm 1931.",
        "Bộ sưu tập hàng chục nghìn hiện vật: đồ chơi dân gian Nga, matryoshka và đồ gỗ Sergiev Posad, búp bê Tây Âu, cùng những món đồ chơi từng thuộc về các con của Nga hoàng Nikolai II.",
        "Toà nhà gạch đỏ trên đồi Konnaya Gora nhìn thẳng sang Tu viện Trinity Lavra - kết hợp lý tưởng trong một ngày tham quan Sergiev Posad, đặc biệt hợp với các gia đình.",
    ],
    "practical": {
        "hours_vi": "Thường mở cửa thứ Tư - Chủ nhật, khoảng 10:00-17:00 (nghỉ bán vé trước giờ đóng); đóng cửa thứ Hai, thứ Ba. Nên kiểm tra lịch chính thức trước khi đến vì giờ giấc có thể thay đổi theo mùa.",
        "ticket_vi": "Vé vào cửa ở mức phải chăng, có ưu đãi cho trẻ em, học sinh, sinh viên và người hưu trí; một số chương trình/giao lưu có phụ phí.",
        "duration_vi": "Khoảng 1-1,5 giờ; hợp để kết hợp cùng chuyến thăm Tu viện Trinity Lavra ở gần đó.",
        "best_time_vi": "Quanh năm vì trưng bày trong nhà; dịp cuối tuần và lễ thường có thêm hoạt động cho trẻ em.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô hoặc tàu tốc hành từ ga Yaroslavsky tới Sergiev Posad (khoảng 1-1,5 giờ), rồi đi bộ hoặc bắt xe tới đồi Konnaya Gora đối diện Lavra. Rất phù hợp cho gia đình có trẻ nhỏ.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text(
        "Художественно-педагогический музей игрушки", "Сергиев Посад, Московская область",
        "Museum of Toys", "Sergiev Posad, Moscow Oblast",
        56.310750, 38.133040,
    ),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Художественно-педагогический музей игрушки", "url": "https://ru.wikipedia.org/wiki/Художественно-педагогический_музей_игрушки"},
        {"title": "Rusmania — Toy Museum (Sergiev Posad)", "url": "https://rusmania.com/central/moscow-region/sergiev-posad/sights/around-the-city/toy-museum"},
        {"title": "Live the World — The Sergiev Posad Museum of Toys", "url": "https://www.livetheworld.com/activities/russia/the-sergiev-posad-museum-of-toys"},
    ],
    "tags": ["museum", "toys", "matryoshka", "bartram", "sergiev-posad", "family", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


# ------------------------------------------------------------------ PLAN
PLAN = {
    "moscow-oblast.json": [PUSHKIN_VYAZYOMY_ZAKHAROVO, SEREDNIKOVO_ESTATE, TOY_MUSEUM_SERGIEV_POSAD],
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
