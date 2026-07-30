# -*- coding: utf-8 -*-
"""_add_places_ulyanovsk_20260729_020000.py — VÙNG: Tỉnh Ulyanovsk (Ульяновская область)
(lần chạy tự động bảo trì 2026-07-29).

Bối cảnh: ulyanovsk.json hiện có 7 địa điểm (Ленинский мемориал, музей-заповедник «Родина
Ленина»/Симбирск, музей ГА, Ундоровский геопарк, Императорский мост, краеведческий музей,
музей «Симбирская классическая гимназия»). Bổ sung ~25 địa điểm THẬT SỰ nổi tiếng còn thiếu,
đa dạng loại hình → đưa vùng lên ~32. TRÁNH trùng 7 điểm trên (đặc biệt KHÔNG thêm lại
Императорский мост — cầu đường sắt lịch sử; ở đây thêm Президентский мост là cầu ô tô 2009).

Phân bố loại hình (25 bản ghi mới):
- bridge (1): Президентский мост (cầu ô tô 2009, một trong những cầu dài nhất châu Âu, ~5,8 km).
- church (4): Спасо-Вознесенский кафедральный собор, Воскресенско-Германовский собор,
  Неопалимовский кафедральный собор, Свято-Никольский собор (Димитровград).
- museum (6): Дом-музей В.И. Ленина, музей И.А. Гончарова, областной художественный музей,
  музей современного искусства им. Пластова, музей-усадьба Пластова (Прислониха),
  Димитровградский краеведческий музей.
- theatre (2): драмтеатр им. Гончарова, театр кукол им. Леонтьевой.
- square_street (2): бульвар Новый Венец, площадь Ленина (Соборная).
- park_garden (5): Карамзинский сквер, парк Дружбы народов, Винновская роща,
  НП «Сенгилеевские горы», Белое озеро (Николаевский р-н).
- monument (4): памятник букве «Ё», памятник Н.М. Карамзину, памятник И.А. Гончарову,
  Обелиск Славы / Вечный огонь (пл. 30-летия Победы).
- other (1): Дворец книги (Дворянское собрание) — kèm tag palace/library.
(Bổ sung nếu đủ chỗ: усадьба-парк Языково, Акшуатский дендропарк, Никольская гора — Сурское,
 Обломовский диван.)

TOẠ ĐỘ: phiên chạy này KHÔNG có truy cập web (WebSearch cạn hạn mức, web_fetch/proxy bị chặn),
nên toạ độ lấy từ kiến thức địa lý về TP Ulyanovsk và tỉnh — tất cả trong phạm vi hợp lệ
(lat ~52.9–54.9, lon ~46.0–50.5; TP Ulyanovsk ~54.32,48.39; Dimitrovgrad ~54.22,49.62),
lat luôn > lon, KHÔNG đảo lat/lon. Link Yandex dùng truy vấn theo tên tiếng Nga (maps_text) nên
pin bản đồ tự định vị đúng theo tên kể cả khi ll gần đúng. KHÔNG bịa toạ độ ngoài phạm vi,
KHÔNG nhồi. Các điểm nông thôn dùng toạ độ cấp làng/thị trấn.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_ulyanovsk_20260729_020000.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "ulyanovsk"
REGION_NAME_VI = "Tỉnh Ulyanovsk"
FD = "Vùng Volga"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
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


def p(hours, ticket, duration, best, tips):
    return {"hours_vi": hours, "ticket_vi": ticket, "duration_vi": duration,
            "best_time_vi": best, "tips_vi": tips}


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
        "review_summary_vi": None,
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

# ============================ CẦU (bridge) ============================

# 1) Президентский мост -----------------------------------------------------------
RECORDS.append(rec(
    "presidential-bridge-ulyanovsk",
    "Cầu Tổng thống (Prezidentsky most)",
    "Президентский мост",
    "Presidential Bridge",
    ["bridge", "monument"],
    54.3009, 48.4880,
    "Cầu đường bộ bắc qua sông Volga (hồ Kuybyshev), nối trung tâm với khu Zavolzhye, Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Cầu Tổng thống là cây cầu đường bộ khổng lồ bắc qua sông Volga tại Ulyanovsk, thông xe năm 2009. Với phần vượt sông dài khoảng 5,8 km (toàn tuyến kể cả đường dẫn gần 13 km), đây là một trong những cây cầu dài nhất nước Nga và châu Âu, trở thành biểu tượng hiện đại của thành phố.",
    "Cầu Tổng thống (Президентский мост) là công trình giao thông hoành tráng bậc nhất Ulyanovsk và là niềm tự hào hiện đại của thành phố quê hương Lenin. Được khởi công từ cuối thập niên 1980 nhưng phải nhiều năm gián đoạn, cây cầu chỉ thông xe vào năm 2009 nhân dịp có sự hiện diện của Tổng thống Nga - từ đó có tên gọi 'Cầu Tổng thống'. Phần cầu vượt mặt nước dài khoảng 5,8 km, còn toàn tuyến kể cả các đoạn đường dẫn lên tới gần 13 km, đưa công trình vào hàng những cây cầu dài nhất nước Nga và châu Âu. Cầu bắc qua lòng hồ Kuybyshev mênh mông (đoạn sông Volga bị chặn dòng), nối phần trung tâm lịch sử trên hữu ngạn với khu đô thị mới Zavolzhye ở tả ngạn, giải toả áp lực giao thông vốn trước kia dồn cả lên Cầu Hoàng gia đường sắt. Với hai tầng thiết kế và hàng loạt nhịp thép vươn dài trên mặt nước, cây cầu tạo nên khung cảnh ấn tượng, đặc biệt khi nhìn từ bờ kè Venets hay lúc lên đèn ban đêm. Đây là điểm ngắm cảnh, chụp ảnh và là dấu ấn kỹ thuật tiêu biểu của Ulyanovsk đương đại.",
    [
        "Một trong những cây cầu dài nhất nước Nga và châu Âu (phần vượt sông ~5,8 km).",
        "Thông xe năm 2009, nối trung tâm lịch sử với khu đô thị mới Zavolzhye qua sông Volga.",
        "Cảnh quan hùng vĩ trên hồ Kuybyshev, đẹp nhất khi ngắm từ bờ kè Venets và lúc lên đèn.",
    ],
    p("Cầu giao thông hoạt động 24/7; ngắm cảnh tự do từ bờ kè và các điểm nhìn ven sông.",
      "Miễn phí (điểm tham quan ngoài trời).",
      "Khoảng 20–40 phút để ngắm và chụp ảnh.",
      "Hoàng hôn và buổi tối khi cầu lên đèn; mùa hè trời trong.",
      "Ngắm và chụp cầu đẹp nhất từ bờ kè Venets hoặc công viên ven sông; không đi bộ trái phép trên lòng cầu."),
    [
        {"title": "Wikipedia (RU) — Президентский мост", "url": "https://ru.wikipedia.org/wiki/Президентский_мост"},
        {"title": "Wikipedia (EN) — Presidential Bridge (Ulyanovsk)", "url": "https://en.wikipedia.org/wiki/Presidential_Bridge"},
    ],
    ["bridge", "volga", "modern", "engineering", "landmark", "ulyanovsk"],
    maps_text("Президентский мост", "Ульяновск", "Presidential Bridge", "Ulyanovsk", 54.3009, 48.4880),
))

# ============================ NHÀ THỜ / TÔN GIÁO (church) ============================

# 2) Спасо-Вознесенский кафедральный собор ----------------------------------------
RECORDS.append(rec(
    "spaso-voznesensky-cathedral-ulyanovsk",
    "Nhà thờ chính toà Chúa Thăng Thiên (Spaxo-Voznexenxki)",
    "Спасо-Вознесенский кафедральный собор",
    "Cathedral of the Ascension",
    ["church"],
    54.3162, 48.3922,
    "Trung tâm thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Nhà thờ chính toà Chúa Thăng Thiên là thánh đường chính đương đại của Ulyanovsk, được xây dựng lại và cung hiến trong những năm 2010 để thay cho ngôi nhà thờ cổ bị phá huỷ thời Xô viết. Công trình bề thế với những mái vòm dát vàng đã trở thành trung tâm đời sống Chính thống giáo của thành phố.",
    "Nhà thờ chính toà Chúa Thăng Thiên (Спасо-Вознесенский собор) là ngôi thánh đường chính của Giáo phận Simbirsk và của thành phố Ulyanovsk ngày nay. Nhà thờ cổ cùng tên vốn tồn tại ở trung tâm Simbirsk từ thế kỷ 18 nhưng đã bị phá huỷ trong thời kỳ Xô viết, khi thành phố mang tên Ulyanovsk và gắn với hình ảnh 'quê hương Lenin' thay vì các biểu tượng tôn giáo. Sau khi Liên Xô tan rã, cộng đồng Chính thống giáo địa phương đã khởi xướng việc phục dựng, và ngôi nhà thờ mới bề thế được xây dựng, hoàn thiện và cung hiến trong những năm 2010. Với khối kiến trúc cao lớn, tháp chuông vươn cao cùng cụm mái vòm dát vàng lấp lánh, công trình nhanh chóng trở thành một điểm nhấn cảnh quan và là trung tâm sinh hoạt tôn giáo, lễ hội của người dân. Bên trong, không gian rộng rãi với bích hoạ và iconostas theo truyền thống Nga tạo nên bầu không khí trang nghiêm. Nằm ở khu trung tâm, nhà thờ là điểm ghé thăm ý nghĩa để hiểu về sự hồi sinh của đời sống tâm linh tại thành phố từng là 'thủ phủ' của tư tưởng vô thần.",
    [
        "Thánh đường chính đương đại của Ulyanovsk, phục dựng thay ngôi nhà thờ cổ bị phá thời Xô viết.",
        "Kiến trúc bề thế với tháp chuông cao và cụm mái vòm dát vàng.",
        "Trung tâm đời sống Chính thống giáo và lễ hội tôn giáo của thành phố.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 7:00–19:00; nên kiểm tra lịch lễ trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 30–45 phút.",
      "Quanh năm; dịp Giáng sinh và Phục sinh Chính thống giáo không khí đặc biệt trang nghiêm.",
      "Ăn mặc kín đáo, nữ nên có khăn trùm đầu; giữ yên lặng trong giờ lễ."),
    [
        {"title": "Wikipedia (RU) — Спасо-Вознесенский собор (Ульяновск)", "url": "https://ru.wikipedia.org/wiki/Спасо-Вознесенский_собор_(Ульяновск)"},
        {"title": "Симбирская епархия — соборы Ульяновска", "url": "https://sim-eparhia.ru/"},
    ],
    ["church", "orthodox", "cathedral", "landmark", "ulyanovsk"],
    maps_text("Спасо-Вознесенский собор", "Ульяновск", "Cathedral of the Ascension", "Ulyanovsk", 54.3162, 48.3922),
))

# 3) Воскресенско-Германовский собор ----------------------------------------------
RECORDS.append(rec(
    "voskresensko-germanovsky-cathedral-ulyanovsk",
    "Nhà thờ Phục Sinh - Thánh German (Voxkrexenxko-Germanovxki)",
    "Воскресенско-Германовский собор",
    "Resurrection-German Cathedral",
    ["church"],
    54.3112, 48.3945,
    "Trung tâm thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Nhà thờ Phục Sinh - Thánh German là một trong những thánh đường Chính thống giáo quan trọng của Ulyanovsk, gắn với ký ức về ngôi nhà thờ Германовская cổ ở trung tâm Simbirsk. Công trình được phục dựng sau thời kỳ Xô viết và là nơi thờ phụng, hành hương quen thuộc của người dân.",
    "Nhà thờ Phục Sinh - Thánh German (Воскресенско-Германовский собор) mang tên gắn với Thánh German xứ Kazan và với truyền thống nhà thờ Германовская từng hiện diện ở trung tâm Simbirsk. Cũng như nhiều thánh đường khác của thành phố, ngôi nhà thờ cổ đã chịu số phận bị đóng cửa và phá huỷ trong thời kỳ Xô viết, khi Simbirsk đổi tên thành Ulyanovsk và trở thành trung tâm tuyên truyền vô thần gắn với tên tuổi Lenin. Sau khi tự do tôn giáo được khôi phục, cộng đồng Chính thống giáo địa phương đã dựng lại nhà thờ, tiếp nối truyền thống thờ phụng. Công trình hiện nay có kiến trúc Nga truyền thống với các mái vòm và tháp chuông, là nơi cử hành các nghi lễ, bảo quản một số biểu tượng thánh được người dân sùng kính. Nằm trong khu trung tâm lịch sử, nhà thờ là một điểm dừng chân giúp du khách cảm nhận nhịp sống tâm linh của thành phố và tìm hiểu quá trình hồi sinh của các thánh đường vùng Volga sau nhiều thập kỷ gián đoạn.",
    [
        "Thánh đường Chính thống giáo quan trọng, nối tiếp truyền thống nhà thờ Германовская cổ.",
        "Phục dựng sau thời kỳ Xô viết, kiến trúc Nga truyền thống với mái vòm và tháp chuông.",
        "Nơi thờ phụng và hành hương quen thuộc ở trung tâm lịch sử Ulyanovsk.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–19:00; nên kiểm tra trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 20–30 phút.",
      "Quanh năm; các dịp lễ lớn Chính thống giáo.",
      "Ăn mặc kín đáo khi vào trong; giữ yên lặng trong giờ lễ."),
    [
        {"title": "Wikipedia (RU) — Воскресенско-Германовский собор", "url": "https://ru.wikipedia.org/wiki/Воскресенско-Германовский_собор"},
        {"title": "Симбирская епархия", "url": "https://sim-eparhia.ru/"},
    ],
    ["church", "orthodox", "cathedral", "historic", "ulyanovsk"],
    maps_text("Воскресенско-Германовский собор", "Ульяновск", "Resurrection-German Cathedral", "Ulyanovsk", 54.3112, 48.3945),
))

# 4) Неопалимовский кафедральный собор --------------------------------------------
RECORDS.append(rec(
    "neopalimovsky-cathedral-ulyanovsk",
    "Nhà thờ chính toà Neopalimovsky (Bụi gai không cháy)",
    "Неопалимовский кафедральный собор",
    "Neopalimovsky Cathedral",
    ["church"],
    54.3195, 48.3820,
    "Phố Kirova, thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Nhà thờ Neopalimovsky là một trong số ít thánh đường của Ulyanovsk còn hoạt động liên tục và từng giữ vai trò nhà thờ chính toà của giáo phận. Tên gọi gắn với biểu tượng Đức Mẹ 'Bụi gai không cháy', đây là nơi lưu giữ nhiều di vật được người dân sùng kính.",
    "Nhà thờ Neopalimovsky (Неопалимовский собор) mang tên biểu tượng Đức Mẹ 'Bụi gai không cháy' (Неопалимая Купина) - hình ảnh gắn với sự chở che khỏi hoả hoạn. Điều đặc biệt là trong khi hầu hết các thánh đường lớn của Simbirsk - Ulyanovsk bị phá huỷ hoặc đóng cửa thời Xô viết, ngôi nhà thờ này nằm ở khu nghĩa trang cũ ngoài rìa trung tâm nên may mắn được giữ lại và duy trì hoạt động qua nhiều thập kỷ. Nhờ vậy, trong một thời gian dài đây từng đảm nhận vai trò nhà thờ chính toà (собор) của giáo phận, là trung tâm đời sống Chính thống giáo hiếm hoi còn sáng đèn của thành phố. Công trình có kiến trúc khiêm nhường nhưng ấm cúng, bên trong lưu giữ những biểu tượng thánh và di vật được tín đồ đặc biệt sùng kính, thu hút đông người đến cầu nguyện và hành hương. Với du khách quan tâm đến lịch sử tôn giáo, Neopalimovsky là một điểm đến giàu ý nghĩa, minh chứng cho sự bền bỉ của đức tin ngay tại 'quê hương Lenin'.",
    [
        "Một trong số ít thánh đường Ulyanovsk hoạt động liên tục qua thời Xô viết.",
        "Từng giữ vai trò nhà thờ chính toà (собор) của giáo phận Simbirsk.",
        "Tên gắn với biểu tượng Đức Mẹ 'Bụi gai không cháy', nơi hành hương quen thuộc.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 7:30–19:00; nên kiểm tra trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 20–30 phút.",
      "Quanh năm; các dịp lễ Chính thống giáo.",
      "Ăn mặc kín đáo, nữ nên có khăn trùm đầu; giữ yên lặng và tôn trọng người đang cầu nguyện."),
    [
        {"title": "Wikipedia (RU) — Неопалимовский собор (Ульяновск)", "url": "https://ru.wikipedia.org/wiki/Неопалимовский_собор_(Ульяновск)"},
        {"title": "Симбирская епархия", "url": "https://sim-eparhia.ru/"},
    ],
    ["church", "orthodox", "cathedral", "pilgrimage", "ulyanovsk"],
    maps_text("Неопалимовский собор", "Ульяновск", "Neopalimovsky Cathedral", "Ulyanovsk", 54.3195, 48.3820),
))

# 5) Свято-Никольский собор (Димитровград) ----------------------------------------
RECORDS.append(rec(
    "st-nicholas-cathedral-dimitrovgrad",
    "Nhà thờ chính toà Thánh Nikolai (Dimitrovgrad)",
    "Свято-Никольский собор",
    "St. Nicholas Cathedral (Dimitrovgrad)",
    ["church"],
    54.2145, 49.6165,
    "Trung tâm thành phố Dimitrovgrad, tỉnh Ulyanovsk, Nga",
    "Nhà thờ chính toà Thánh Nikolai là thánh đường Chính thống giáo trung tâm của Dimitrovgrad - thành phố lớn thứ hai của tỉnh Ulyanovsk (nguyên là Melekess). Công trình với những mái vòm truyền thống là điểm tâm linh và cảnh quan quan trọng của thành phố.",
    "Nhà thờ chính toà Thánh Nikolai (Свято-Никольский собор) là trung tâm đời sống Chính thống giáo của Dimitrovgrad - đô thị lớn thứ hai tỉnh Ulyanovsk, vốn mang tên lịch sử Melekess (Мелекесс) trước năm 1972. Là thành phố công nghiệp và khoa học (nổi tiếng với viện nghiên cứu lò phản ứng NIIAR), Dimitrovgrad vẫn giữ được một khu trung tâm cũ mang dáng dấp thị trấn thương nhân vùng Volga, và ngôi nhà thờ Thánh Nikolai là một trong những điểm nhấn kiến trúc - tâm linh của nơi này. Được xây dựng theo phong cách Nga truyền thống với cụm mái vòm và tháp chuông, nhà thờ là nơi diễn ra các nghi lễ chính của cộng đồng, thu hút đông đảo tín đồ đặc biệt vào các dịp lễ lớn. Với du khách ghé Dimitrovgrad, thánh đường là điểm dừng chân quen thuộc, thường kết hợp cùng việc dạo qua khu phố cũ Melekess với những ngôi nhà thương nhân bằng gạch cuối thế kỷ 19 - đầu 20 để cảm nhận trọn vẹn bề dày lịch sử của đô thị này.",
    [
        "Thánh đường Chính thống giáo trung tâm của Dimitrovgrad (Melekess cũ).",
        "Kiến trúc Nga truyền thống với cụm mái vòm và tháp chuông.",
        "Kết hợp tham quan khu phố cũ thương nhân Melekess thế kỷ 19–20.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 7:30–19:00; nên kiểm tra trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 30 phút.",
      "Quanh năm; các dịp lễ Chính thống giáo.",
      "Ăn mặc kín đáo; kết hợp dạo trung tâm cổ Melekess của Dimitrovgrad."),
    [
        {"title": "Wikipedia (RU) — Димитровград (Ульяновская область)", "url": "https://ru.wikipedia.org/wiki/Димитровград_(Ульяновская_область)"},
        {"title": "Симбирская епархия — Мелекесская епархия", "url": "https://sim-eparhia.ru/"},
    ],
    ["church", "orthodox", "cathedral", "dimitrovgrad", "melekess", "landmark"],
    maps_text("Свято-Никольский собор", "Димитровград", "St Nicholas Cathedral", "Dimitrovgrad", 54.2145, 49.6165),
))

# ============================ BẢO TÀNG (museum) ============================

# 6) Дом-музей В.И. Ленина ---------------------------------------------------------
RECORDS.append(rec(
    "lenin-house-museum-ulyanovsk",
    "Nhà - Bảo tàng V.I. Lenin (Dom-muzey Lenina)",
    "Дом-музей В.И. Ленина",
    "Lenin House Museum",
    ["museum", "monument"],
    54.3130, 48.3950,
    "Phố Lenina 70, thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Nhà - Bảo tàng V.I. Lenin là ngôi nhà gỗ nơi gia đình Ulyanov (gia đình Lenin) từng sinh sống nhiều năm ở Simbirsk. Bảo tàng tái hiện nguyên vẹn không gian sinh hoạt cuối thế kỷ 19 và là một trong những địa chỉ 'kinh điển' khi tìm hiểu về tuổi thơ của Lenin.",
    "Nhà - Bảo tàng V.I. Lenin (Дом-музей В.И. Ленина) tại phố Lenina là ngôi nhà gỗ hai tầng nơi gia đình Ulyanov đã sống trong những năm 1878–1887, quãng thời gian Vladimir Ulyanov (sau này là Lenin) trải qua tuổi thiếu niên và học tại trường trung học Simbirsk. Đây là căn nhà duy nhất mà gia đình sở hữu tại thành phố. Được biến thành bảo tàng tưởng niệm từ thời Xô viết, ngôi nhà giữ nguyên bài trí nội thất, đồ đạc, sách vở và không gian sinh hoạt của một gia đình trí thức Nga cuối thế kỷ 19: phòng làm việc của người cha - một thanh tra giáo dục, phòng học của các con, đàn piano, thư phòng... Bảo tàng nằm trong quần thể khu bảo tồn 'Quê hương Lenin' (Симбирск) và là một trong những điểm được ghé thăm nhiều nhất. Ngay cả với du khách không quan tâm đến chính trị, không gian này vẫn hấp dẫn như một 'lát cắt' chân thực về nếp sống, giáo dục và sinh hoạt gia đình của tầng lớp trí thức tỉnh lẻ Nga thời Sa hoàng.",
    [
        "Ngôi nhà gia đình Ulyanov (Lenin) sinh sống các năm 1878–1887 tại Simbirsk.",
        "Nội thất và đồ dùng được giữ nguyên, tái hiện nếp sống trí thức Nga cuối thế kỷ 19.",
        "Điểm 'kinh điển' trong quần thể khu bảo tồn 'Quê hương Lenin'.",
    ],
    p("Thường 10:00–18:00, đóng cửa thứ Hai và ngày cuối tháng (nên kiểm tra trước).",
      "Vé phổ thông khoảng 150–250 rúp; có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 45–60 phút.",
      "Quanh năm; kết hợp tham quan cả khu bảo tồn Simbirsk trong nửa ngày.",
      "Mua vé gộp để thăm nhiều nhà - bảo tàng trong quần thể; có hướng dẫn viên nếu đặt trước."),
    [
        {"title": "Wikipedia (RU) — Дом-музей В.И. Ленина (Ульяновск)", "url": "https://ru.wikipedia.org/wiki/Дом-музей_В._И._Ленина_(Ульяновск)"},
        {"title": "Музей-заповедник «Родина В.И. Ленина»", "url": "https://ulzapovednik.ru/"},
    ],
    ["museum", "lenin", "history", "memorial", "house-museum", "ulyanovsk"],
    maps_text("Дом-музей В.И. Ленина", "Ульяновск", "Lenin House Museum", "Ulyanovsk", 54.3130, 48.3950),
))

# 7) Историко-мемориальный центр-музей И.А. Гончарова ------------------------------
RECORDS.append(rec(
    "goncharov-museum-ulyanovsk",
    "Bảo tàng I.A. Goncharov (Muzey Goncharova)",
    "Историко-мемориальный центр-музей И.А. Гончарова",
    "Ivan Goncharov Museum",
    ["museum"],
    54.3133, 48.3966,
    "Phố Goncharova 20, thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Bảo tàng I.A. Goncharov nằm trong ngôi nhà nơi đại văn hào Ivan Goncharov - tác giả tiểu thuyết 'Oblomov' - chào đời tại Simbirsk. Toà nhà nổi bật với tháp đồng hồ biểu tượng của thành phố và trưng bày về cuộc đời, sự nghiệp của nhà văn.",
    "Bảo tàng I.A. Goncharov (музей И.А. Гончарова) toạ lạc trong chính ngôi nhà nơi Ivan Goncharov (1812–1891) - một trong những tiểu thuyết gia lớn của văn học Nga thế kỷ 19 - sinh ra tại Simbirsk. Goncharov là tác giả của bộ ba tiểu thuyết nổi tiếng 'Câu chuyện thường ngày', 'Oblomov' và 'Vách đá' ('Обрыв'), trong đó nhân vật Oblomov đã trở thành biểu tượng văn hoá về sự trì trệ, mộng mơ. Toà nhà lịch sử của gia đình Goncharov nổi bật với tháp đồng hồ đặc trưng đã trở thành một biểu tượng của Ulyanovsk. Bảo tàng trưng bày bản thảo, thư từ, đồ dùng cá nhân, ấn phẩm và tái hiện không gian sống, gợi lại thế giới của nhà văn cũng như đời sống thương nhân - quý tộc Simbirsk thời bấy giờ. Đây là điểm đến quan trọng cho những ai yêu văn học Nga, đồng thời cũng là dịp tìm hiểu bối cảnh xã hội đã sản sinh ra một trong những nhân vật văn học kinh điển nhất của nước Nga.",
    [
        "Nhà nơi văn hào Ivan Goncharov, tác giả 'Oblomov', chào đời tại Simbirsk.",
        "Toà nhà có tháp đồng hồ - một biểu tượng của thành phố Ulyanovsk.",
        "Trưng bày bản thảo, thư từ, đồ dùng và không gian sống của nhà văn.",
    ],
    p("Thường 10:00–18:00, đóng cửa thứ Hai (nên kiểm tra trước).",
      "Vé phổ thông khoảng 150–300 rúp; có ưu đãi cho học sinh, sinh viên.",
      "Khoảng 60 phút.",
      "Quanh năm; kết hợp dạo phố Goncharova - trục phố chính của thành phố.",
      "Chú ý ngắm tháp đồng hồ bên ngoài; có thể đặt tour theo chủ đề văn học."),
    [
        {"title": "Wikipedia (RU) — Гончаров, Иван Александрович", "url": "https://ru.wikipedia.org/wiki/Гончаров,_Иван_Александрович"},
        {"title": "Музей-заповедник «Родина В.И. Ленина» — музей Гончарова", "url": "https://ulzapovednik.ru/"},
    ],
    ["museum", "literature", "goncharov", "history", "ulyanovsk"],
    maps_text("Историко-мемориальный музей Гончарова", "Ульяновск", "Ivan Goncharov Museum", "Ulyanovsk", 54.3133, 48.3966),
))

# 8) Ульяновский областной художественный музей -----------------------------------
RECORDS.append(rec(
    "ulyanovsk-art-museum",
    "Bảo tàng Mỹ thuật tỉnh Ulyanovsk",
    "Ульяновский областной художественный музей",
    "Ulyanovsk Regional Art Museum",
    ["museum"],
    54.3168, 48.4038,
    "Bulvar Novy Venets 3/4 (Nhà - đài tưởng niệm Goncharov), thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Bảo tàng Mỹ thuật tỉnh Ulyanovsk sở hữu bộ sưu tập nghệ thuật phong phú từ hội hoạ Nga, châu Âu cổ điển đến nghệ thuật thế kỷ 20. Bảo tàng đặt trong toà nhà lịch sử 'Nhà - đài tưởng niệm Goncharov' bề thế trên bờ kè Venets.",
    "Bảo tàng Mỹ thuật tỉnh Ulyanovsk (Ульяновский областной художественный музей) là một trong những kho tàng nghệ thuật quan trọng của vùng Volga. Bộ sưu tập trải rộng từ hội hoạ Nga thế kỷ 18–20 với các tên tuổi lớn, nghệ thuật châu Âu Tây Âu (Ý, Hà Lan, Đức, Pháp) đến đồ hoạ, điêu khắc, nghệ thuật trang trí - ứng dụng và một phần bộ sưu tập tranh của hoạ sĩ đồng hương Arkady Plastov. Bảo tàng được đặt trong toà nhà 'Nhà - đài tưởng niệm I.A. Goncharov' (Дом-памятник Гончарову) - một công trình kỷ niệm bề thế đầu thế kỷ 20 nằm ngay cạnh Quảng trường Lenin và bờ kè Novy Venets, cùng địa chỉ với Bảo tàng Địa phương học. Không gian trưng bày trang nhã, ánh sáng tốt, cho phép người xem thưởng thức các tác phẩm trong bầu không khí cổ điển. Đây là điểm đến lý tưởng cho người yêu nghệ thuật, đồng thời rất thuận tiện để kết hợp với việc dạo bờ kè và tham quan trung tâm lịch sử thành phố.",
    [
        "Bộ sưu tập hội hoạ Nga và châu Âu cổ điển, đồ hoạ, điêu khắc phong phú.",
        "Đặt trong 'Nhà - đài tưởng niệm Goncharov' bề thế trên bờ kè Novy Venets.",
        "Ngay cạnh Quảng trường Lenin, thuận tiện kết hợp tham quan trung tâm.",
    ],
    p("Thường 10:00–18:00, đóng cửa thứ Hai (nên kiểm tra trước).",
      "Vé phổ thông khoảng 200–350 rúp; có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 60–90 phút.",
      "Quanh năm; kết hợp dạo bờ kè Novy Venets sau khi tham quan.",
      "Cùng toà nhà với Bảo tàng Địa phương học - có thể tham quan gộp trong buổi."),
    [
        {"title": "Wikipedia (RU) — Ульяновский областной художественный музей", "url": "https://ru.wikipedia.org/wiki/Ульяновский_областной_художественный_музей"},
        {"title": "Ульяновский областной художественный музей (сайт)", "url": "https://uart-museum.ru/"},
    ],
    ["museum", "art", "gallery", "painting", "ulyanovsk"],
    maps_text("Ульяновский областной художественный музей", "Ульяновск", "Ulyanovsk Regional Art Museum", "Ulyanovsk", 54.3168, 48.4038),
))

# 9) Музей современного изобразительного искусства имени А.А. Пластова -------------
RECORDS.append(rec(
    "plastov-modern-art-museum-ulyanovsk",
    "Bảo tàng Mỹ thuật đương đại mang tên A.A. Plastov",
    "Музей современного изобразительного искусства имени А.А. Пластова",
    "Plastov Museum of Contemporary Art",
    ["museum"],
    54.3145, 48.3980,
    "Phố Lva Tolstogo 51, thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Bảo tàng Mỹ thuật đương đại mang tên A.A. Plastov tôn vinh danh hoạ Arkady Plastov - bậc thầy hội hoạ Xô viết quê ở Ulyanovsk - và trưng bày nghệ thuật thế kỷ 20–21. Bảo tàng đặt trong một biệt thự thương nhân cổ ở trung tâm thành phố.",
    "Bảo tàng Mỹ thuật đương đại mang tên A.A. Plastov (Музей современного изобразительного искусства имени А.А. Пластова) được đặt theo tên Arkady Plastov (1893–1972) - một trong những hoạ sĩ hiện thực Xô viết được yêu mến nhất, người con của làng Prislonikha thuộc tỉnh Ulyanovsk, nổi tiếng với những bức tranh về đời sống nông thôn Nga đầy ánh sáng và sức sống. Bảo tàng lưu giữ, giới thiệu các tác phẩm của Plastov cùng nghệ thuật tạo hình Nga và Xô viết thế kỷ 20, đồng thời tổ chức nhiều triển lãm đương đại luân phiên. Không gian trưng bày nằm trong một biệt thự cổ mang phong cách hiện đại (modern) đầu thế kỷ 20 ở khu trung tâm, tạo nên sự hoà quyện giữa kiến trúc lịch sử và nghệ thuật đương thời. Đây là địa chỉ hấp dẫn cho người yêu mỹ thuật muốn hiểu thêm về trường phái hội hoạ gắn với vùng đất Volga, cũng như theo dõi các dòng chảy nghệ thuật mới của nước Nga hôm nay.",
    [
        "Tôn vinh danh hoạ Arkady Plastov - bậc thầy hội hoạ hiện thực Xô viết quê Ulyanovsk.",
        "Trưng bày nghệ thuật thế kỷ 20–21 và các triển lãm đương đại luân phiên.",
        "Đặt trong biệt thự cổ phong cách modern đầu thế kỷ 20 ở trung tâm.",
    ],
    p("Thường 10:00–18:00, đóng cửa thứ Hai (nên kiểm tra trước).",
      "Vé phổ thông khoảng 150–300 rúp; có ưu đãi cho học sinh, sinh viên.",
      "Khoảng 60 phút.",
      "Quanh năm; theo dõi lịch triển lãm đương đại trên trang chính thức.",
      "Kết hợp tham quan cùng Bảo tàng Mỹ thuật tỉnh gần đó để có cái nhìn trọn vẹn."),
    [
        {"title": "Wikipedia (RU) — Пластов, Аркадий Александрович", "url": "https://ru.wikipedia.org/wiki/Пластов,_Аркадий_Александрович"},
        {"title": "Ульяновский областной художественный музей — филиалы", "url": "https://uart-museum.ru/"},
    ],
    ["museum", "art", "plastov", "contemporary", "ulyanovsk"],
    maps_text("Музей современного искусства имени Пластова", "Ульяновск", "Plastov Museum of Contemporary Art", "Ulyanovsk", 54.3145, 48.3980),
))

# 10) Музей-усадьба А.А. Пластова (Прислониха) ------------------------------------
RECORDS.append(rec(
    "plastov-museum-estate-prislonikha",
    "Bảo tàng - điền trang A.A. Plastov (làng Prislonikha)",
    "Музей-усадьба А.А. Пластова в Прислонихе",
    "Plastov Museum-Estate in Prislonikha",
    ["museum", "monument"],
    54.3280, 47.4530,
    "Làng Prislonikha, huyện Karsunsky, tỉnh Ulyanovsk, Nga",
    "Bảo tàng - điền trang A.A. Plastov tại làng Prislonikha là nơi danh hoạ Arkady Plastov sinh ra, sống và sáng tác. Ngôi làng và cảnh quan xung quanh chính là nguồn cảm hứng cho nhiều bức tranh nổi tiếng của ông về nông thôn Nga.",
    "Bảo tàng - điền trang A.A. Plastov (музей-усадьба Пластова) nằm ở làng Prislonikha thuộc huyện Karsunsky, cách thành phố Ulyanovsk khoảng vài chục cây số. Đây là quê hương của hoạ sĩ Arkady Plastov (1893–1972), nơi ông sinh ra, gắn bó suốt đời và tạo nên phần lớn những tác phẩm để đời. Quần thể bảo tàng bao gồm ngôi nhà - xưởng vẽ của gia đình Plastov cùng khung cảnh làng quê được gìn giữ gần như nguyên vẹn: những nếp nhà gỗ, con đường làng, dòng suối, cánh đồng và ngọn đồi - tất cả chính là 'người mẫu' và bối cảnh trong các bức tranh nổi tiếng của ông về lao động, lễ hội và thiên nhiên nông thôn Nga. Chuyến thăm Prislonikha vì thế không chỉ là vào một bảo tàng, mà là bước vào chính thế giới hội hoạ của Plastov ngoài đời thực, cảm nhận thứ ánh sáng và không khí đã làm nên tên tuổi ông. Đây là điểm đến đặc sắc cho người yêu nghệ thuật muốn kết hợp trải nghiệm văn hoá với cảnh sắc đồng quê vùng Volga.",
    [
        "Quê hương và nơi sáng tác của danh hoạ Arkady Plastov.",
        "Ngôi nhà - xưởng vẽ và cảnh quan làng quê được gìn giữ nguyên vẹn.",
        "Chính là bối cảnh trong nhiều bức tranh nổi tiếng của Plastov về nông thôn Nga.",
    ],
    p("Thường mở theo giờ hành chính, nên liên hệ đặt trước (điểm ở nông thôn).",
      "Vé phổ thông khoảng 150–250 rúp; có ưu đãi.",
      "Khoảng 1,5–2 giờ kể cả di chuyển và dạo làng.",
      "Cuối xuân đến đầu thu khi cảnh làng quê đẹp và thuận tiện đi lại.",
      "Nên tự lái xe hoặc đặt tour; kiểm tra lịch mở cửa trước khi đi vì ở xa trung tâm."),
    [
        {"title": "Wikipedia (RU) — Прислониха", "url": "https://ru.wikipedia.org/wiki/Прислониха"},
        {"title": "Wikipedia (RU) — Пластов, Аркадий Александрович", "url": "https://ru.wikipedia.org/wiki/Пластов,_Аркадий_Александрович"},
    ],
    ["museum", "art", "plastov", "estate", "countryside", "karsun"],
    maps_text("Музей-усадьба Пластова", "Прислониха", "Plastov Museum-Estate", "Prislonikha", 54.3280, 47.4530),
))

# 11) Димитровградский краеведческий музей ----------------------------------------
RECORDS.append(rec(
    "dimitrovgrad-local-lore-museum",
    "Bảo tàng Địa phương học Dimitrovgrad",
    "Димитровградский краеведческий музей",
    "Dimitrovgrad Local Lore Museum",
    ["museum"],
    54.2148, 49.6190,
    "Trung tâm thành phố Dimitrovgrad, tỉnh Ulyanovsk, Nga",
    "Bảo tàng Địa phương học Dimitrovgrad giới thiệu lịch sử, thiên nhiên và đời sống của thành phố Melekess - Dimitrovgrad cùng vùng phụ cận. Bảo tàng đặt trong một toà nhà thương nhân cổ, là điểm khởi đầu để hiểu về đô thị lớn thứ hai của tỉnh.",
    "Bảo tàng Địa phương học Dimitrovgrad (Димитровградский краеведческий музей) là nơi lưu giữ và kể lại câu chuyện của thành phố từng mang tên Melekess (Мелекесс) - một trung tâm buôn bán ngũ cốc và sản xuất bột mì sầm uất bên bờ sông Bolshoy Cheremshan từ thế kỷ 19. Bộ sưu tập trải rộng qua nhiều chủ đề: khảo cổ và thiên nhiên vùng đất, đời sống thương nhân và thủ công thời trước cách mạng, quá trình công nghiệp hoá thời Xô viết cho tới việc thành phố đổi tên thành Dimitrovgrad năm 1972 (theo tên lãnh tụ Bulgaria Georgi Dimitrov) và trở thành trung tâm khoa học hạt nhân với viện NIIAR. Bảo tàng thường đặt trong một dinh thự thương nhân cổ bằng gạch - bản thân toà nhà đã là một hiện vật kiến trúc. Đây là điểm dừng chân lý tưởng để du khách nắm bắt bức tranh tổng thể về lịch sử, kinh tế và văn hoá của Dimitrovgrad trước khi khám phá khu phố cổ Melekess và các công trình xung quanh.",
    [
        "Giới thiệu lịch sử Melekess - Dimitrovgrad, đô thị lớn thứ hai của tỉnh.",
        "Bộ sưu tập từ thời thương nhân buôn ngũ cốc đến thời khoa học hạt nhân.",
        "Đặt trong dinh thự thương nhân cổ bằng gạch - hiện vật kiến trúc sống động.",
    ],
    p("Thường 10:00–18:00, đóng cửa thứ Hai (nên kiểm tra trước).",
      "Vé phổ thông khoảng 100–200 rúp; có ưu đãi.",
      "Khoảng 60 phút.",
      "Quanh năm; kết hợp dạo khu phố cổ Melekess.",
      "Hỏi nhân viên về tuyến tham quan các dinh thự thương nhân gần đó."),
    [
        {"title": "Wikipedia (RU) — Димитровград (Ульяновская область)", "url": "https://ru.wikipedia.org/wiki/Димитровград_(Ульяновская_область)"},
        {"title": "Wikipedia (RU) — Мелекесс", "url": "https://ru.wikipedia.org/wiki/Мелекесс"},
    ],
    ["museum", "local-lore", "history", "dimitrovgrad", "melekess"],
    maps_text("Димитровградский краеведческий музей", "Димитровград", "Dimitrovgrad Local Lore Museum", "Dimitrovgrad", 54.2148, 49.6190),
))

# ============================ NHÀ HÁT (theatre) ============================

# 12) Ульяновский драматический театр им. И.А. Гончарова ---------------------------
RECORDS.append(rec(
    "goncharov-drama-theatre-ulyanovsk",
    "Nhà hát Kịch tỉnh Ulyanovsk mang tên I.A. Goncharov",
    "Ульяновский драматический театр имени И.А. Гончарова",
    "Ulyanovsk Goncharov Drama Theatre",
    ["theatre"],
    54.3158, 48.4003,
    "Phố Spasskaya 12, thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Nhà hát Kịch tỉnh Ulyanovsk mang tên đại văn hào Goncharov là nhà hát lâu đời và uy tín bậc nhất thành phố, với truyền thống sân khấu kéo dài hơn hai thế kỷ. Đây là trung tâm đời sống nghệ thuật kịch nói của cả vùng.",
    "Nhà hát Kịch tỉnh Ulyanovsk mang tên I.A. Goncharov (Ульяновский драматический театр имени И.А. Гончарова) có nguồn gốc từ những buổi diễn sân khấu ở Simbirsk từ nửa đầu thế kỷ 19, khiến nó trở thành một trong những nhà hát tỉnh lâu đời của nước Nga. Được đặt theo tên người con vĩ đại của thành phố - nhà văn Ivan Goncharov, nhà hát là 'ngôi đền' của nghệ thuật kịch nói địa phương, dàn dựng cả kịch kinh điển Nga và thế giới lẫn các vở đương đại. Toà nhà nhà hát trên phố Spasskaya là một công trình bề thế ở trung tâm thành phố, thường được trang hoàng lộng lẫy vào buổi tối diễn. Đoàn kịch của nhà hát từng nhận nhiều danh hiệu và giải thưởng, được xem là niềm tự hào văn hoá của Ulyanovsk. Với du khách, việc thưởng thức một buổi diễn ở đây - hoặc chỉ đơn giản là chiêm ngưỡng kiến trúc và không khí sân khấu - là cách thú vị để chạm vào đời sống văn hoá đương đại của thành phố bên bờ Volga.",
    [
        "Một trong những nhà hát tỉnh lâu đời của Nga, truyền thống từ thế kỷ 19.",
        "Mang tên đại văn hào đồng hương Ivan Goncharov.",
        "Trung tâm nghệ thuật kịch nói, dàn dựng cả kinh điển lẫn đương đại.",
    ],
    p("Phòng vé và giờ diễn theo lịch mùa diễn; buổi tối thường bắt đầu 18:00–19:00.",
      "Vé tuỳ vở và vị trí, thường khoảng 300–1.000 rúp.",
      "Buổi diễn khoảng 2–3 giờ.",
      "Mùa diễn từ thu đến xuân; đặt vé trước cho các vở nổi bật.",
      "Xem lịch diễn trên trang chính thức; đến sớm để ngắm kiến trúc và nội thất nhà hát."),
    [
        {"title": "Wikipedia (RU) — Ульяновский драматический театр", "url": "https://ru.wikipedia.org/wiki/Ульяновский_драматический_театр_имени_И._А._Гончарова"},
        {"title": "Ульяновский драматический театр (сайт)", "url": "https://uldramteatr.ru/"},
    ],
    ["theatre", "drama", "culture", "goncharov", "ulyanovsk"],
    maps_text("Ульяновский драматический театр", "Ульяновск", "Ulyanovsk Goncharov Drama Theatre", "Ulyanovsk", 54.3158, 48.4003),
))

# 13) Ульяновский театр кукол им. В.М. Леонтьевой ---------------------------------
RECORDS.append(rec(
    "ulyanovsk-puppet-theatre",
    "Nhà hát Múa rối Ulyanovsk mang tên V.M. Leontyeva",
    "Ульяновский театр кукол имени В.М. Леонтьевой",
    "Ulyanovsk Puppet Theatre",
    ["theatre"],
    54.3128, 48.3968,
    "Phố Goncharova 10, thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Nhà hát Múa rối Ulyanovsk mang tên nữ phát thanh viên huyền thoại Valentina Leontyeva là điểm đến văn hoá được các gia đình và trẻ em yêu thích. Nhà hát dàn dựng những vở rối cổ tích sinh động, gìn giữ nghệ thuật rối truyền thống Nga.",
    "Nhà hát Múa rối Ulyanovsk (Ульяновский театр кукол) mang tên Valentina Leontyeva - nữ phát thanh viên - dẫn chương trình truyền hình huyền thoại của Liên Xô, người gắn bó với Ulyanovsk. Là một trong những nhà hát dành cho thiếu nhi lâu đời của vùng, đây là nơi khơi dậy tình yêu sân khấu cho nhiều thế hệ trẻ em thành phố. Tiết mục của nhà hát chủ yếu là các vở kịch rối dựa trên truyện cổ tích Nga và thế giới, kết hợp con rối thủ công tinh xảo, âm nhạc, ánh sáng và diễn xuất sống động, mang lại những buổi biểu diễn vừa vui nhộn vừa giàu tính giáo dục. Toà nhà nhà hát ở khu trung tâm cũng thường được trang trí bắt mắt, thân thiện với trẻ nhỏ. Với các gia đình du lịch cùng con, đây là một lựa chọn giải trí ấm áp; còn với người lớn yêu nghệ thuật, nghệ thuật rối truyền thống Nga tại đây là một trải nghiệm văn hoá đáng khám phá, cho thấy chiều sâu của sân khấu dân gian được gìn giữ và làm mới.",
    [
        "Nhà hát múa rối lâu đời, mang tên phát thanh viên huyền thoại Valentina Leontyeva.",
        "Dàn dựng các vở rối cổ tích Nga và thế giới sinh động, phù hợp gia đình.",
        "Gìn giữ và làm mới nghệ thuật rối truyền thống Nga.",
    ],
    p("Buổi diễn chủ yếu cuối tuần và ngày lễ theo lịch; nên kiểm tra trước.",
      "Vé thường khoảng 200–500 rúp.",
      "Buổi diễn khoảng 45–70 phút.",
      "Quanh năm; cuối tuần có nhiều suất phù hợp cho trẻ em.",
      "Đặt vé trước cho suất cuối tuần; hợp với gia đình có trẻ nhỏ."),
    [
        {"title": "Wikipedia (RU) — Ульяновский театр кукол", "url": "https://ru.wikipedia.org/wiki/Ульяновский_театр_кукол"},
        {"title": "Ульяновский театр кукол (сайт)", "url": "https://teatrkukol73.ru/"},
    ],
    ["theatre", "puppet", "family", "children", "ulyanovsk"],
    maps_text("Ульяновский театр кукол", "Ульяновск", "Ulyanovsk Puppet Theatre", "Ulyanovsk", 54.3128, 48.3968),
))

# ============================ QUẢNG TRƯỜNG / PHỐ (square_street) ============================

# 14) Бульвар Новый Венец ---------------------------------------------------------
RECORDS.append(rec(
    "novy-venets-boulevard-ulyanovsk",
    "Bulvar Novy Venets (Bờ kè - đại lộ Vành đai mới)",
    "Бульвар Новый Венец",
    "Novy Venets Boulevard",
    ["square_street", "park_garden"],
    54.3182, 48.4040,
    "Bulvar Novy Venets, trung tâm lịch sử thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Bulvar Novy Venets là đại lộ đi bộ chạy dọc mép cao nguyên nhìn xuống sông Volga - địa điểm dạo chơi, ngắm cảnh được yêu thích nhất Ulyanovsk. Từ đây có tầm nhìn khoáng đạt bao trọn dòng Volga và các cây cầu.",
    "Bulvar Novy Venets ('Vành đai mới') là tuyến đại lộ đi bộ nổi tiếng nhất Ulyanovsk, chạy dọc theo rìa cao nguyên nơi thành phố toạ lạc, nhìn thẳng xuống dòng Volga rộng lớn phía dưới. Cái tên 'Venets' (vương miện/vành đai) gợi đúng vị trí của con phố như một 'vành đai' ôm lấy đỉnh dốc bờ sông. Dọc đại lộ là hàng cây rợp bóng, những lối đi lát đá, ghế nghỉ, đài phun nước và một loạt công trình quan trọng: Bảo tàng Địa phương học và Bảo tàng Mỹ thuật (trong Nhà - đài tưởng niệm Goncharov), Đài tưởng niệm Lenin, các tượng đài và vọng cảnh. Đây là nơi người dân địa phương tản bộ, hẹn hò, chụp ảnh cưới và du khách dừng chân để ngắm hoàng hôn trên sông. Từ các điểm nhìn của bờ kè, tầm mắt trải rộng bao trọn mặt nước Volga, Cầu Hoàng gia và Cầu Tổng thống ở phía xa, tạo nên một trong những khung cảnh đẹp nhất của cả vùng. Novy Venets vì thế được xem là 'trái tim' cảnh quan và là điểm khởi đầu tự nhiên cho mọi hành trình khám phá trung tâm lịch sử Ulyanovsk.",
    [
        "Đại lộ đi bộ dọc mép cao nguyên với tầm nhìn khoáng đạt xuống sông Volga.",
        "Tập trung nhiều bảo tàng, tượng đài và đài tưởng niệm quan trọng của thành phố.",
        "Điểm ngắm hoàng hôn, chụp ảnh và dạo chơi được yêu thích nhất Ulyanovsk.",
    ],
    p("Không gian công cộng ngoài trời, mở cửa tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 45–90 phút để dạo và ngắm cảnh.",
      "Chiều muộn và hoàng hôn để ngắm ánh nắng trên sông Volga.",
      "Kết hợp tham quan các bảo tàng và Đài tưởng niệm Lenin ngay dọc đại lộ."),
    [
        {"title": "Wikipedia (RU) — Венец (Ульяновск)", "url": "https://ru.wikipedia.org/wiki/Венец_(Ульяновск)"},
        {"title": "Официальный туризм Ульяновской области", "url": "https://ultourism.ru/"},
    ],
    ["square_street", "boulevard", "promenade", "volga", "viewpoint", "ulyanovsk"],
    maps_text("Бульвар Новый Венец", "Ульяновск", "Novy Venets Boulevard", "Ulyanovsk", 54.3182, 48.4040),
))

# 15) Площадь Ленина (Соборная площадь) -------------------------------------------
RECORDS.append(rec(
    "lenin-square-ulyanovsk",
    "Quảng trường Lenin (Ploshchad Lenina / Sobornaya)",
    "Площадь Ленина (Соборная площадь)",
    "Lenin Square (Cathedral Square)",
    ["square_street", "monument"],
    54.3168, 48.3990,
    "Quảng trường Lenin, trung tâm thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Quảng trường Lenin - nguyên là Quảng trường Nhà thờ (Sobornaya) - là quảng trường trung tâm lịch sử của Ulyanovsk, nơi đặt tượng đài Lenin và diễn ra các sự kiện lớn của thành phố. Đây là điểm hội tụ của trung tâm và mở ra bờ kè Novy Venets.",
    "Quảng trường Lenin (Площадь Ленина) là quảng trường trung tâm và giàu ý nghĩa lịch sử bậc nhất của Ulyanovsk. Trước cách mạng, nơi đây mang tên Quảng trường Nhà thờ (Соборная площадь) với ngôi thánh đường lớn của Simbirsk toạ lạc ở trung tâm - công trình đã bị phá huỷ trong thời Xô viết. Sau đó quảng trường được đổi tên và trở thành không gian nghi lễ chính, nơi đặt tượng đài V.I. Lenin bề thế và diễn ra các cuộc mít tinh, diễu hành, sự kiện văn hoá lớn của thành phố. Quảng trường rộng rãi, nối liền với bờ kè Novy Venets và cụm bảo tàng, tượng đài xung quanh, tạo thành 'lõi' của trung tâm lịch sử. Đứng tại đây, du khách vừa cảm nhận được quy mô của không gian đô thị được quy hoạch trang trọng, vừa có thể phóng tầm mắt về phía sông Volga. Đây là điểm định hướng thuận tiện và là nơi bắt đầu lý tưởng cho hành trình đi bộ khám phá trung tâm Ulyanovsk, kết nối tới bờ kè, các bảo tàng và những công trình biểu tượng khác.",
    [
        "Quảng trường trung tâm lịch sử của Ulyanovsk, nguyên là Quảng trường Nhà thờ.",
        "Nơi đặt tượng đài Lenin và diễn ra các sự kiện lớn của thành phố.",
        "Kết nối trực tiếp với bờ kè Novy Venets và cụm bảo tàng trung tâm.",
    ],
    p("Không gian công cộng ngoài trời, mở cửa tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 20–40 phút.",
      "Quanh năm; dịp lễ lớn có sự kiện, trang hoàng đặc biệt.",
      "Điểm khởi đầu thuận tiện để đi bộ tham quan trung tâm và bờ kè Novy Venets."),
    [
        {"title": "Wikipedia (RU) — Площадь Ленина (Ульяновск)", "url": "https://ru.wikipedia.org/wiki/Площадь_Ленина_(Ульяновск)"},
        {"title": "Официальный туризм Ульяновской области", "url": "https://ultourism.ru/"},
    ],
    ["square_street", "square", "lenin", "center", "ulyanovsk"],
    maps_text("Площадь Ленина", "Ульяновск", "Lenin Square", "Ulyanovsk", 54.3168, 48.3990),
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
            skipped.append(r["slug"]); continue
        data.append(r)
        existing_slugs.add(r["slug"]); existing_ids.add(r["id"])
        added.append(r["slug"])
    if added:
        bak = f"{path}.bak_add_{TS}"
        shutil.copyfile(path, bak)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Backup: {os.path.basename(bak)}")
    print(f"REGION={REGION}  ADDED={len(added)}  SKIPPED(dup)={len(skipped)}  TOTAL_NOW={len(data)}")
    if added: print("  + " + "\n  + ".join(added))
    if skipped: print("  (skip dup): " + ", ".join(skipped))


if __name__ == "__main__":
    main()
