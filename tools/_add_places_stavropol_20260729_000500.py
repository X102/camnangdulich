# -*- coding: utf-8 -*-
"""_add_places_stavropol_20260729_000500.py — VÙNG: Vùng Stavropol (Ставропольский край)
(lần chạy tự động 2026-07-29).

Bối cảnh: stavropol.json hiện có 7 địa điểm (Машук+Проваль, Кисловодский нац. парк,
Нарзанная галерея, Ессентукский курорт, Железноводский курорт, Медовые водопады,
Казанский собор Ставрополя). Vùng nghỉ dưỡng Кавказские Минеральные Воды (KavMinVody)
rất giàu điểm tham quan → bổ sung 25 địa điểm THẬT SỰ nổi bật, đa dạng loại hình,
đưa vùng lên 32. TRÁNH trùng 7 điểm cũ.

Toạ độ đã xác minh chéo (ru.wikipedia, sobory.ru, 2GIS, culture.ru, komandirovka, 2026-07-29).
Phạm vi Stavropol: lat ~43.7–46.2, lon ~41.9–43.5. KHÔNG đảo lat/lon. Các thành phố KMV:
Пятигорск ~44.04,43.08; Кисловодск ~43.90,42.72; Ессентуки ~44.05,42.86;
Железноводск ~44.13,43.03; TP Ставрополь ~45.04,41.97.

GHI CHÚ (không thêm / hiệu chỉnh):
- Hồ ở Железноводск: tên chuẩn là «Курортное озеро» (còn gọi «озеро 30-летия Победы»);
  KHÔNG có nguồn xác nhận tên «озеро Островского» → dùng tên Курортное озеро.
- Нарзанная колоннада (1912, Курортный бульвар 14/1) KHÁC với «Нарзанная галерея» (đã có
  trong file) và KHÁC với «Колоннада» 1951 của một an dưỡng → đã dùng toạ độ colonnade 1912.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_stavropol_20260729_000500.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "stavropol"
REGION_NAME_VI = "Vùng Stavropol"
FD = "Vùng Bắc Kavkaz"


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
        "rating": None,
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

# ============================ PYATIGORSK ============================

# 1) Место дуэли Лермонтова -------------------------------------------------------
RECORDS.append(rec(
    "lermontov-duel-place-pyatigorsk",
    "Nơi đấu súng của Lermontov (Mê-xtô đu-e-li)",
    "Место дуэли М. Ю. Лермонтова",
    "Site of Lermontov's Duel",
    ["monument"],
    44.058889, 43.076944,
    "Sườn tây bắc núi Mashuk, ngoại vi phía bắc thành phố Pyatigorsk, vùng Kavkaz Mineralnye Vody, tỉnh Stavropol, Nga",
    "Đài tưởng niệm nơi thi hào Mikhail Lermontov ngã xuống trong cuộc đấu súng định mệnh ngày 15/7/1841, dưới chân núi Mashuk. Một trong những địa điểm bi tráng và được viếng thăm nhiều nhất của văn học Nga.",
    "Nơi đấu súng của Lermontov là một trong những địa điểm gắn với bi kịch lớn của văn chương Nga: chiều ngày 15 (theo lịch cũ 27) tháng 7 năm 1841, nhà thơ - sĩ quan Mikhail Yuryevich Lermontov, khi ấy mới 26 tuổi, đã tử thương trong cuộc đấu súng với Nikolai Martynov ngay dưới sườn tây bắc núi Mashuk. Địa điểm chính xác từ lâu vẫn còn tranh cãi, song đài tưởng niệm hiện nay được dựng năm 1915 theo thiết kế của kiến trúc sư Boris Mikeshin: một tấm bia đá cao hình tháp với bức phù điêu chân dung nhà thơ ở giữa, bao quanh là hàng cột đá thấp nối bằng xích và bốn tượng kền kền ở bốn góc. Khu vực nằm trong không gian rừng cây yên tĩnh ven thành phố, trở thành nơi hành hương của những người yêu văn học Nga, đặc biệt vào dịp kỷ niệm ngày mất của Lermontov. Kết hợp cùng Nhà Lermontov trong trung tâm Pyatigorsk, địa điểm này giúp du khách hình dung trọn vẹn quãng đời cuối và cái chết đầy day dứt của một trong những thi hào lớn nhất nước Nga.",
    [
        "Nơi thi hào Lermontov tử thương trong cuộc đấu súng ngày 15/7/1841 dưới chân núi Mashuk",
        "Đài tưởng niệm bằng đá dựng năm 1915 (KTS Boris Mikeshin) với phù điêu chân dung nhà thơ",
        "Điểm hành hương của người yêu văn học Nga, nằm trong rừng cây yên tĩnh ven thành phố",
    ],
    p("Không gian ngoài trời, tham quan tự do; ban ngày là hợp lý nhất.",
      "Miễn phí.",
      "Khoảng 30–45 phút.",
      "Cuối xuân đến đầu thu; sáng hoặc chiều mát.",
      "Kết hợp đi cáp treo Mashuk và ghé Nhà Lermontov ở trung tâm; nên đi taxi hoặc xe vì nằm khá xa khu phố chính."),
    [
        {"title": "Wikipedia (RU) — Место дуэли Лермонтова", "url": "https://ru.wikipedia.org/wiki/Место_дуэли_Лермонтова"},
        {"title": "Государственный музей-заповедник М. Ю. Лермонтова", "url": "https://domik-lermontova.ru/"},
    ],
    ["monument", "lermontov", "literature", "pyatigorsk", "memorial", "history"],
    maps_text("Место дуэли Лермонтова", "Пятигорск", "Site of Lermontov's Duel", "Pyatigorsk", 44.058889, 43.076944),
))

# 2) Эолова арфа ------------------------------------------------------------------
RECORDS.append(rec(
    "aeolian-harp-pyatigorsk",
    "Đền Đàn hạc Aeolian (Ê-ô-lô-va ạc-pha)",
    "Беседка «Эолова арфа»",
    "Aeolian Harp Pavilion",
    ["monument"],
    44.040278, 43.086667,
    "Trên gờ núi Mashuk phía trên công viên nghỉ dưỡng, thành phố Pyatigorsk, vùng Kavkaz Mineralnye Vody, tỉnh Stavropol, Nga",
    "Vọng lâu tròn kiểu cổ điển dựng năm 1831 trên mỏm đá Mashuk, biểu tượng lãng mạn của Pyatigorsk. Từng đặt đàn hạc gió tự ngân theo gió, nay là một trong những đài ngắm toàn cảnh đẹp nhất thành phố.",
    "Đền Đàn hạc Aeolian là một trong những biểu tượng kiến trúc - lãng mạn nổi tiếng nhất của Pyatigorsk, được dựng năm 1831 theo thiết kế của hai anh em kiến trúc sư người Ý Bernardetti trên một mỏm đá nhô ra của núi Mashuk. Vọng lâu hình tròn theo phong cách cổ điển với tám cột đá đỡ mái vòm, tên gọi lấy từ Aeolus - vị thần gió trong thần thoại Hy Lạp. Thuở ban đầu, bên trong đặt một cây đàn hạc đặc biệt: gió lùa qua các dây đàn khiến nó tự ngân lên những âm thanh du dương, biến kiến trúc thành một 'nhạc cụ khổng lồ' của thiên nhiên. Ngày nay tiếng đàn được tái tạo bằng thiết bị điện tử, nhưng sức hút lớn nhất của nơi này là tầm nhìn: từ gờ đá, du khách phóng mắt bao trọn thành phố Pyatigorsk, thảo nguyên Kavkaz và khi trời trong là dãy núi tuyết xa xa, trong đó có đỉnh Elbrus. Đền Đàn hạc cũng xuất hiện trong tác phẩm của Lermontov, càng làm dày thêm lớp trầm tích văn hoá của điểm đến này.",
    [
        "Vọng lâu cổ điển tám cột dựng năm 1831 trên mỏm đá núi Mashuk",
        "Từng đặt đàn hạc gió tự ngân theo luồng gió - nguồn gốc cái tên Aeolian",
        "Đài ngắm toàn cảnh Pyatigorsk và dãy Kavkaz, được nhắc trong văn Lermontov",
    ],
    p("Không gian ngoài trời, tham quan tự do cả ngày.",
      "Miễn phí.",
      "Khoảng 20–40 phút.",
      "Cuối xuân đến đầu thu; sáng sớm trời quang để nhìn xa nhất.",
      "Có thể đi bộ lên theo đường dạo trong công viên hoặc kết hợp tuyến cáp treo Mashuk; mang giày êm vì đường hơi dốc."),
    [
        {"title": "Wikipedia (RU) — Эолова арфа (Пятигорск)", "url": "https://ru.wikipedia.org/wiki/Эолова_арфа_(Пятигорск)"},
        {"title": "Kukarta.ru — Эолова арфа", "url": "https://kukarta.ru/eolova-arfa/"},
    ],
    ["monument", "pavilion", "viewpoint", "pyatigorsk", "architecture", "lermontov"],
    maps_text("Беседка Эолова арфа", "Пятигорск", "Aeolian Harp Pavilion", "Pyatigorsk", 44.040278, 43.086667),
))

# 3) Грот Дианы -------------------------------------------------------------------
RECORDS.append(rec(
    "diana-grotto-pyatigorsk",
    "Hang Diana (Grôt Đi-a-nứ)",
    "Грот Дианы",
    "Diana's Grotto",
    ["other"],
    44.035778, 43.081726,
    "Trong công viên Tsvetnik, chân núi Goryachaya, trung tâm thành phố Pyatigorsk, tỉnh Stavropol, Nga",
    "Hang nhân tạo mát lạnh dưới chân núi Goryachaya, xây năm 1830-1831 để kỷ niệm chuyến chinh phục đỉnh Elbrus. Nơi Lermontov từng dự vũ hội chỉ vài ngày trước khi qua đời.",
    "Hang Diana là một hang nhân tạo duyên dáng nằm trong công viên Tsvetnik, dưới chân núi Goryachaya ở trung tâm Pyatigorsk. Công trình được các kỹ sư anh em Bernardazzi xây dựng năm 1830-1831 để đánh dấu lần đầu tiên con người chinh phục đỉnh Elbrus (1829), và ban đầu mang tên 'Hang Elbrus' trước khi được đổi thành Hang Diana - nữ thần săn bắn trong thần thoại La Mã. Hang được tạo hình từ đá tự nhiên với vòm trần thấp, bên trong mát lạnh ngay cả giữa mùa hè nóng bức, có ghế đá và mạch nước nhỏ. Điểm khiến nơi này đặc biệt trong ký ức người Nga: chỉ vài ngày trước khi qua đời trong cuộc đấu súng năm 1841, Lermontov cùng bạn bè đã tổ chức một buổi khiêu vũ ngay trước cửa hang. Ngày nay Hang Diana là một góc nghỉ chân mát mẻ, lãng mạn và giàu giai thoại, thường được ghép trong lộ trình dạo bộ qua công viên Tsvetnik cùng Nhà nghỉ Lermontov và các suối khoáng nóng lân cận.",
    [
        "Hang nhân tạo xây 1830-1831 kỷ niệm lần đầu chinh phục đỉnh Elbrus",
        "Không gian đá mát lạnh giữa mùa hè, mang tên nữ thần săn bắn Diana",
        "Nơi Lermontov dự vũ hội chỉ vài ngày trước khi tử nạn năm 1841",
    ],
    p("Nằm trong công viên Tsvetnik, tham quan tự do ban ngày.",
      "Miễn phí.",
      "Khoảng 15–20 phút.",
      "Quanh năm; mùa hè đặc biệt dễ chịu vì trong hang mát.",
      "Kết hợp dạo công viên Tsvetnik, Nhà nghỉ Lermontov (Lermontovskaya galereya) và Đền Đàn hạc gần đó."),
    [
        {"title": "Wikipedia (RU) — Грот Дианы (Пятигорск)", "url": "https://ru.wikipedia.org/wiki/Грот_Дианы_(Пятигорск)"},
        {"title": "2GIS — Грот Дианы, Пятигорск", "url": "https://2gis.ru/pyatigorsk/geo/12526332248326322"},
    ],
    ["other", "grotto", "pyatigorsk", "tsvetnik", "lermontov", "history"],
    maps_text("Грот Дианы", "Пятигорск", "Diana's Grotto", "Pyatigorsk", 44.035778, 43.081726),
))

# 4) Домик Лермонтова / музей-заповедник ------------------------------------------
RECORDS.append(rec(
    "lermontov-house-museum-pyatigorsk",
    "Nhà - Bảo tàng Lermontov Pyatigorsk (Đô-mík Léc-môn-tô-va)",
    "Государственный музей-заповедник М. Ю. Лермонтова («Домик Лермонтова»)",
    "Lermontov State Museum-Reserve (Lermontov's House)",
    ["museum"],
    44.039914, 43.077782,
    "Phố Lermontova 4, trung tâm thành phố Pyatigorsk, tỉnh Stavropol, Nga",
    "Ngôi nhà mái tranh nơi Lermontov sống những tuần cuối đời và được đặt thi hài sau cuộc đấu súng năm 1841. Bảo tàng văn học - tưởng niệm lâu đời nhất nước Nga về nhà thơ, mở cửa từ 1912.",
    "Nhà Lermontov là trái tim của Khu bảo tàng - di tích quốc gia mang tên Mikhail Yuryevich Lermontov ở Pyatigorsk, và là một trong những bảo tàng văn học - tưởng niệm lâu đời nhất nước Nga (thành lập năm 1912). Đây chính là ngôi nhà nhỏ mái tranh, tường trát trắng mà nhà thơ thuê ở trong mùa hè cuối cùng của đời mình năm 1841; ông đã sống, làm việc tại đây và sau cuộc đấu súng định mệnh dưới chân Mashuk, thi hài ông được đưa về chính căn nhà này. Nội thất bên trong được phục dựng gần như nguyên trạng theo hồi ức của người đương thời: bàn viết, giường, đồ đạc giản dị gợi lại không khí sinh hoạt của Lermontov. Khu bảo tàng ngày nay mở rộng ra nhiều toà nhà lân cận, trưng bày bản thảo, thư từ, tranh vẽ (bản thân Lermontov cũng là hoạ sĩ có tài), chân dung và hiện vật về cuộc đời, sự nghiệp cùng vùng Kavkaz đã in đậm trong thơ ông. Với người yêu văn học Nga, đây là điểm đến gần như bắt buộc khi tới vùng Kavkaz Mineralnye Vody.",
    [
        "Ngôi nhà mái tranh Lermontov sống mùa hè cuối cùng và được đặt thi hài năm 1841",
        "Bảo tàng văn học - tưởng niệm về nhà thơ lâu đời nhất nước Nga (từ 1912)",
        "Trưng bày bản thảo, thư từ và cả tranh do chính Lermontov vẽ",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa mức phải chăng (vài trăm rúp); ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; hợp cả những ngày thời tiết xấu.",
      "Nằm ngay trung tâm, gần công viên Tsvetnik; thuyết minh chủ yếu bằng tiếng Nga, nên tìm hiểu trước về Lermontov."),
    [
        {"title": "Государственный музей-заповедник М. Ю. Лермонтова", "url": "https://domik-lermontova.ru/"},
        {"title": "Culture.ru — Музей-заповедник М. Ю. Лермонтова", "url": "https://www.culture.ru/institutes/20880/gosudarstvennyi-muzei-zapovednik-m-yu-lermontova"},
    ],
    ["museum", "lermontov", "literature", "pyatigorsk", "memorial-house", "history"],
    maps_text("Домик Лермонтова музей", "Пятигорск", "Lermontov House Museum", "Pyatigorsk", 44.039914, 43.077782),
    official_site="https://domik-lermontova.ru/",
))

# 5) Лермонтовская галерея --------------------------------------------------------
RECORDS.append(rec(
    "lermontov-gallery-pyatigorsk",
    "Nhà nghỉ Lermontov (Léc-môn-tôp-xcai-a ga-lê-rê-ia)",
    "Лермонтовская галерея",
    "Lermontov Gallery",
    ["monument", "other"],
    44.036681, 43.081991,
    "Trong công viên Tsvetnik, trung tâm thành phố Pyatigorsk, tỉnh Stavropol, Nga",
    "Toà nhà kính - kim loại lộng lẫy màu xanh dựng năm 1901 trong công viên Tsvetnik, một trong những công trình 'kính - thép' nổi bật của kiến trúc nghỉ dưỡng Nga. Nay là phòng hoà nhạc và triển lãm.",
    "Nhà nghỉ Lermontov là một trong những công trình kiến trúc bắt mắt nhất công viên Tsvetnik ở trung tâm Pyatigorsk. Được dựng năm 1901 nhân 60 năm ngày mất của nhà thơ Lermontov, toà nhà thuộc dòng kiến trúc 'kính - kim loại' thịnh hành cuối thế kỷ 19: khung thép nhẹ kết hợp những mảng kính lớn nhiều màu, tạo cảm giác thanh thoát, lộng lẫy như một cung điện pha lê. Các cấu kiện kim loại đúc sẵn được đặt mua từ nhà máy tại Nizhny Novgorod và lắp ráp tại chỗ, tương tự 'người anh em' là Nhà nghỉ Pushkin ở Zheleznovodsk. Ngay từ đầu, công trình đã đóng vai trò trung tâm giải trí - văn hoá của khu nghỉ dưỡng: nơi tổ chức hoà nhạc, biểu diễn sân khấu, khiêu vũ và triển lãm. Cho đến nay, Nhà nghỉ Lermontov vẫn là một phòng hoà nhạc và triển lãm đang hoạt động, đồng thời là phông nền chụp ảnh yêu thích giữa khung cảnh xanh mát của Tsvetnik, gắn kết hài hoà với Hang Diana và các suối khoáng nóng lân cận.",
    [
        "Công trình 'kính - kim loại' màu xanh dựng năm 1901 trong công viên Tsvetnik",
        "Khung thép đúc sẵn từ Nizhny Novgorod, kiến trúc nghỉ dưỡng đặc trưng cuối thế kỷ 19",
        "Vẫn hoạt động như phòng hoà nhạc và triển lãm, điểm chụp ảnh nổi bật",
    ],
    p("Khu công viên tham quan tự do; buổi biểu diễn/triển lãm theo lịch riêng.",
      "Dạo bên ngoài miễn phí; vé sự kiện tuỳ chương trình.",
      "Khoảng 20–30 phút (chưa kể xem biểu diễn).",
      "Quanh năm; đẹp nhất khi công viên nhiều hoa (cuối xuân - hè).",
      "Kết hợp dạo trọn công viên Tsvetnik cùng Hang Diana; xem lịch hoà nhạc nếu muốn vào bên trong."),
    [
        {"title": "Wikipedia (RU) — Лермонтовская галерея", "url": "https://ru.wikipedia.org/wiki/Лермонтовская_галерея"},
        {"title": "2GIS — Лермонтовская галерея, Пятигорск", "url": "https://2gis.ru/pyatigorsk/geo/70030077044313715"},
    ],
    ["monument", "architecture", "concert-hall", "pyatigorsk", "tsvetnik", "resort"],
    maps_text("Лермонтовская галерея", "Пятигорск", "Lermontov Gallery", "Pyatigorsk", 44.036681, 43.081991),
))

# 6) Парк «Цветник» ---------------------------------------------------------------
RECORDS.append(rec(
    "tsvetnik-park-pyatigorsk",
    "Công viên Tsvetnik (Xvét-nhích)",
    "Парк «Цветник»",
    "Tsvetnik Park",
    ["park_garden"],
    44.036808, 43.081791,
    "Chân núi Goryachaya, trung tâm thành phố Pyatigorsk, tỉnh Stavropol, Nga",
    "Công viên nghỉ dưỡng lâu đời và đẹp nhất Pyatigorsk, lập năm 1828 dưới chân núi Goryachaya. Quần tụ Nhà nghỉ Lermontov, Hang Diana, nhà tắm khoáng và bức tượng đồng Kislyi vui nhộn.",
    "Công viên Tsvetnik (nghĩa là 'vườn hoa') là công viên nghỉ dưỡng cổ nhất và được yêu thích nhất của Pyatigorsk, hình thành từ năm 1828 dưới chân núi Goryachaya, ngay trung tâm thành phố. Đây từng là nơi giới quý tộc và văn nghệ sĩ Nga thế kỷ 19 dạo chơi, nghỉ dưỡng, và khung cảnh của nó in dấu trong tiểu thuyết 'Một anh hùng thời đại' của Lermontov. Công viên tập hợp một loạt điểm nhấn kiến trúc và lịch sử: Nhà nghỉ Lermontov bằng kính - thép, Hang Diana mát lạnh, nhà tắm khoáng Yermolov, các luống hoa rực rỡ, đài phun nước và những con đường dạo bộ rợp bóng cây. Trước lối vào là bức tượng đồng 'Kislyi' (chàng trai ôm bình nước khoáng) - hình tượng vui nhộn gợi nhắc nhân vật hài trong văn học và đã thành 'linh vật' chụp ảnh của du khách. Từ Tsvetnik, các lối mòn dẫn lên núi Goryachaya với tượng đại bàng - biểu tượng của toàn vùng Kavkaz Mineralnye Vody. Tsvetnik chính là điểm khởi đầu tự nhiên cho mọi hành trình khám phá trung tâm lịch sử Pyatigorsk.",
    [
        "Công viên nghỉ dưỡng cổ nhất Pyatigorsk, lập năm 1828 dưới chân núi Goryachaya",
        "Quần tụ Nhà nghỉ Lermontov, Hang Diana, nhà tắm khoáng và luống hoa rực rỡ",
        "Tượng đồng 'Kislyi' vui nhộn và lối lên núi Goryachaya với tượng đại bàng biểu tượng",
    ],
    p("Không gian mở, dạo chơi tự do cả ngày.",
      "Miễn phí (một số điểm trong công viên có thể thu vé riêng).",
      "Khoảng 1–1,5 giờ.",
      "Cuối xuân đến đầu thu khi hoa nở rộ; buổi sáng và chiều mát dễ chịu.",
      "Điểm xuất phát tốt để khám phá trung tâm; từ đây leo tiếp lên núi Goryachaya ngắm tượng đại bàng."),
    [
        {"title": "Wikipedia (RU) — Цветник (Пятигорск)", "url": "https://ru.wikipedia.org/wiki/Цветник_(Пятигорск)"},
        {"title": "2GIS — Парк Цветник, Пятигорск", "url": "https://2gis.ru/pyatigorsk/geo/12526272118934160"},
    ],
    ["park_garden", "pyatigorsk", "resort", "lermontov", "walking", "landmark"],
    maps_text("Парк Цветник", "Пятигорск", "Tsvetnik Park", "Pyatigorsk", 44.036808, 43.081791),
))

# 7) Спасский собор (Пятигорск) ---------------------------------------------------
RECORDS.append(rec(
    "spassky-cathedral-pyatigorsk",
    "Nhà thờ Chính toà Spassky, Pyatigorsk (Xpát-xki xô-bo)",
    "Спасский кафедральный собор (Пятигорск)",
    "Spassky (Christ the Saviour) Cathedral, Pyatigorsk",
    ["church"],
    44.036949, 43.078133,
    "Phố Sobornaya 1A, trung tâm thành phố Pyatigorsk, tỉnh Stavropol, Nga",
    "Nhà thờ chính toà Chính thống giáo của Pyatigorsk, mô phỏng theo Nhà thờ Đấng Cứu Thế ở Moskva. Bản gốc thế kỷ 19 bị phá thời Liên Xô, được phục dựng và thánh hiến lại năm 2012.",
    "Nhà thờ Chính toà Spassky (Đấng Cứu Thế) là ngôi thánh đường Chính thống giáo trung tâm của Pyatigorsk, toạ lạc trên một gò đất cao ở khu phố cổ. Nhà thờ đầu tiên được xây dựng vào nửa sau thế kỷ 19 theo phong cách 'Nga - Byzantine', lấy cảm hứng từ Nhà thờ Đấng Cứu Thế (Khram Khrista Spasitelya) hoành tráng ở Moskva, và từng là công trình tôn giáo lớn bậc nhất vùng Kavkaz Mineralnye Vody. Trong thời kỳ Xô-viết chống tôn giáo, ngôi nhà thờ bị đóng cửa rồi phá huỷ vào những năm 1930. Đến đầu thế kỷ 21, thánh đường được xây dựng lại gần như nguyên mẫu trên vị trí cũ và được thánh hiến lại năm 2012. Ngày nay Spassky nổi bật với năm mái vòm mạ vàng, mặt tiền trắng trang nghiêm và nội thất trang trí công phu, vừa là nơi hành lễ chính của thành phố vừa là điểm nhấn thị giác trong bức toàn cảnh trung tâm Pyatigorsk. Với du khách, nhà thờ là một minh chứng cho sự hồi sinh của di sản tôn giáo Nga sau thế kỷ 20 nhiều biến động.",
    [
        "Nhà thờ chính toà của Pyatigorsk, mô phỏng Nhà thờ Đấng Cứu Thế ở Moskva",
        "Bản gốc thế kỷ 19 bị phá thời Xô-viết, phục dựng và thánh hiến lại năm 2012",
        "Năm mái vòm mạ vàng, mặt tiền trắng nổi bật trên gò cao khu phố cổ",
    ],
    p("Mở cửa hằng ngày cho khách hành hương và tham quan, khoảng 7:00–19:00; giờ lễ có thể đông.",
      "Miễn phí (hoan nghênh quyên góp).",
      "Khoảng 30–45 phút.",
      "Quanh năm.",
      "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu; giữ yên lặng khi có lễ."),
    [
        {"title": "Sobory.ru — Спасский собор (Пятигорск)", "url": "https://sobory.ru/article/?object=23406"},
        {"title": "Wikipedia (RU) — Спасский собор (Пятигорск)", "url": "https://ru.wikipedia.org/wiki/Спасский_собор_(Пятигорск)"},
    ],
    ["church", "cathedral", "orthodox", "pyatigorsk", "architecture", "religion"],
    maps_text("Спасский собор", "Пятигорск", "Spassky Cathedral", "Pyatigorsk", 44.036949, 43.078133),
))

# ============================ KISLOVODSK ============================

# 8) Замок коварства и любви ------------------------------------------------------
RECORDS.append(rec(
    "castle-guile-love-kislovodsk",
    "Lâu đài 'Mưu mô và Tình yêu' (Za-mốc cô-vác-xtva)",
    "Замок коварства и любви",
    "Castle of Guile and Love",
    ["other"],
    43.896116, 42.664931,
    "Hẻm núi Alikonovka, ngoại ô tây nam thành phố Kislovodsk, tỉnh Stavropol, Nga",
    "Vách đá tự nhiên hình lâu đài trung cổ trong hẻm núi Alikonovka, gắn với truyền thuyết tình yêu bi thương. Dưới chân là khách sạn - nhà hàng xây theo phong cách lâu đài đá.",
    "Lâu đài 'Mưu mô và Tình yêu' thực chất là một khối đá tự nhiên nhô cao trong hẻm núi Alikonovka, cách trung tâm Kislovodsk vài km về phía tây nam, có hình dáng gợi liên tưởng đến một toà lâu đài trung cổ với những tháp canh và tường thành. Cái tên lãng mạn của nó bắt nguồn từ một truyền thuyết dân gian vùng Kavkaz: chuyện tình bi thương giữa cô con gái một lãnh chúa và chàng chăn cừu nghèo; đôi trẻ hẹn cùng gieo mình xuống vực để được ở bên nhau, nhưng vào phút cuối chàng trai đã nhảy còn cô gái chùn bước, để rồi sống trong ân hận - bi kịch của 'mưu mô' và 'tình yêu'. Dưới chân vách đá, người ta đã dựng một khách sạn - nhà hàng bằng đá mô phỏng kiến trúc lâu đài, khiến khung cảnh càng thêm phần huyền hoặc. Ngày nay đây là điểm dạo chơi, chụp ảnh và thưởng thức ẩm thực Kavkaz yêu thích, thường được ghép cùng hành trình tới thác Mật ong (Medovye vodopady) và núi Vòng gần đó trong một vòng khám phá thiên nhiên quanh Kislovodsk.",
    [
        "Vách đá tự nhiên hình lâu đài trung cổ trong hẻm núi Alikonovka",
        "Gắn với truyền thuyết tình yêu bi thương của vùng Kavkaz",
        "Dưới chân có khách sạn - nhà hàng đá phong cách lâu đài, thưởng thức ẩm thực Kavkaz",
    ],
    p("Không gian ngoài trời, tham quan tự do; nhà hàng theo giờ riêng.",
      "Tham quan vách đá miễn phí; ăn uống tại nhà hàng tính phí.",
      "Khoảng 1–1,5 giờ (chưa kể ăn uống).",
      "Cuối xuân đến đầu thu; tránh ngày mưa vì đường hẻm núi trơn.",
      "Dễ kết hợp thác Mật ong và núi Vòng trong một tour thiên nhiên; nên đi xe hoặc tour vì nằm ngoài trung tâm."),
    [
        {"title": "Wikipedia (RU) — Замок коварства и любви", "url": "https://ru.wikipedia.org/wiki/Замок_коварства_и_любви"},
        {"title": "Kislovodsk-kurort — Замок коварства и любви", "url": "https://kislovodsk-kurort.org/"},
    ],
    ["other", "nature", "rock", "legend", "kislovodsk", "viewpoint"],
    maps_text("Замок коварства и любви", "Кисловодск", "Castle of Guile and Love", "Kislovodsk", 43.896116, 42.664931),
))

# 9) Нарзанная колоннада ----------------------------------------------------------
RECORDS.append(rec(
    "narzan-colonnade-kislovodsk",
    "Hàng cột Narzan, Kislovodsk (Nạc-dan-nai-a cô-lôn-na-đa)",
    "Нарзанная колоннада (Кисловодск)",
    "Narzan Colonnade, Kislovodsk",
    ["monument"],
    43.898802, 42.716681,
    "Đại lộ nghỉ dưỡng (Kurortny bulvar) 14/1, lối vào Công viên Quốc gia Kislovodsk, thành phố Kislovodsk, tỉnh Stavropol, Nga",
    "Hàng cột đá bán nguyệt tráng lệ dựng năm 1912-1913 làm cổng biểu tượng dẫn vào Công viên nghỉ dưỡng Kislovodsk. Một trong những công trình được chụp ảnh nhiều nhất của thành phố suối khoáng.",
    "Hàng cột Narzan là một trong những công trình biểu tượng và được yêu thích nhất của Kislovodsk, nằm ở cuối Đại lộ nghỉ dưỡng (Kurortny bulvar), ngay lối vào Công viên Quốc gia Kislovodsk. Được xây dựng năm 1912-1913 theo thiết kế của kiến trúc sư Nikolai Semyonov nhân kỷ niệm 100 năm nước Nga chiến thắng Napoléon, công trình mang hình dáng bán nguyệt uy nghi với hai tầng hàng cột đá trắng theo phong cách cổ điển, bắc qua dòng suối Olkhovka nhỏ. Đây vừa là 'cổng khải hoàn' dẫn vào không gian nghỉ dưỡng, vừa là nơi du khách dạo bộ, hóng mát và chụp ảnh. Bên trong quần thể từng có điểm phát nước khoáng Narzan trứ danh - loại nước khoáng có gas tự nhiên đã làm nên tên tuổi Kislovodsk (tên thành phố nghĩa là 'nước chua'). Hàng cột kết nối liền mạch với Đại lộ nghỉ dưỡng nhộn nhịp một bên và không gian xanh mênh mông của công viên quốc gia một bên, trở thành điểm khởi đầu tự nhiên cho mọi lộ trình dạo chơi ở Kislovodsk.",
    [
        "Hàng cột đá bán nguyệt hai tầng dựng 1912-1913, cổng biểu tượng vào công viên",
        "Kỷ niệm 100 năm chiến thắng Napoléon, phong cách cổ điển bắc qua suối Olkhovka",
        "Điểm dạo bộ, chụp ảnh và khởi đầu Đại lộ nghỉ dưỡng nhộn nhịp của Kislovodsk",
    ],
    p("Không gian công cộng, tham quan tự do cả ngày.",
      "Miễn phí (vào sâu Công viên Quốc gia có thể thu vé).",
      "Khoảng 20–30 phút.",
      "Quanh năm; đẹp khi lên đèn buổi tối.",
      "Kết hợp dạo Đại lộ nghỉ dưỡng và đi tiếp vào Công viên Quốc gia Kislovodsk (đã có trong cẩm nang)."),
    [
        {"title": "Wikipedia (RU) — Нарзанная колоннада", "url": "https://ru.wikipedia.org/wiki/Нарзанная_колоннада"},
        {"title": "2GIS — Нарзанная колоннада, Кисловодск", "url": "https://2gis.ru/kislovodsk/geo/12526272118939644"},
    ],
    ["monument", "colonnade", "architecture", "kislovodsk", "resort", "landmark"],
    maps_text("Нарзанная колоннада", "Кисловодск", "Narzan Colonnade", "Kislovodsk", 43.898802, 42.716681),
))

# 10) Гора-Кольцо -----------------------------------------------------------------
RECORDS.append(rec(
    "ring-mountain-kislovodsk",
    "Núi Vòng (Ga-ra Côn-txô)",
    "Гора-Кольцо (Кольцо-гора)",
    "Ring Mountain (Koltso-gora)",
    ["other"],
    43.941389, 42.693611,
    "Rìa bắc thành phố Kislovodsk, gần làng Podkumok, tỉnh Stavropol, Nga",
    "Vòm đá tự nhiên hình chiếc nhẫn khổng lồ trên sườn dãy Borgustan, do gió và nước bào mòn suốt hàng nghìn năm. Được Lermontov nhắc trong tiểu thuyết 'Một anh hùng thời đại'.",
    "Núi Vòng là một thắng cảnh thiên nhiên độc đáo ở rìa bắc Kislovodsk: một lỗ hổng tròn khổng lồ xuyên qua vách đá của dãy Borgustan, tạo thành hình dáng như một chiếc nhẫn hay chiếc vòng khổng lồ đóng khung bầu trời và cảnh quan phía sau. 'Chiếc nhẫn đá' này là kết quả của quá trình phong hoá tự nhiên: gió, mưa và biến đổi nhiệt độ đã bào mòn lớp đá sa thạch mềm trong suốt hàng nghìn năm, khoét thủng thành một trong nhiều hốc đá dọc sườn núi, mà lỗ lớn nhất chính là 'chiếc vòng' nổi tiếng với đường kính vài mét. Nơi đây gắn với văn học Nga: Lermontov đã nhắc tới Núi Vòng trong tiểu thuyết 'Một anh hùng thời đại', càng làm tăng sức hút. Du khách có thể leo lên tới sát chiếc vòng để ngắm toàn cảnh thung lũng sông Podkumok và thành phố Kislovodsk, đồng thời chụp những bức ảnh 'đóng khung' đặc trưng. Đây là điểm dừng thiên nhiên - văn hoá thường được ghép trong hành trình quanh vùng ngoại vi Kislovodsk.",
    [
        "Vòm đá tự nhiên hình chiếc nhẫn do phong hoá tạo nên qua hàng nghìn năm",
        "Điểm ngắm toàn cảnh thung lũng sông Podkumok và Kislovodsk",
        "Được Lermontov nhắc trong tiểu thuyết 'Một anh hùng thời đại'",
    ],
    p("Không gian ngoài trời, tham quan tự do ban ngày.",
      "Vào cửa miễn phí hoặc phí tượng trưng tuỳ thời điểm.",
      "Khoảng 1–1,5 giờ.",
      "Cuối xuân đến đầu thu; sáng hoặc chiều để ánh sáng đẹp.",
      "Đường lên hơi dốc và trơn khi mưa, nên đi giày bám tốt; kết hợp các điểm ngoại ô Kislovodsk."),
    [
        {"title": "Wikipedia (RU) — Кольцо (гора)", "url": "https://ru.wikipedia.org/wiki/Кольцо_(гора)"},
        {"title": "Kavkaz.rgo — Гора-Кольцо", "url": "https://kavkaz.rgo.ru/"},
    ],
    ["other", "nature", "rock-arch", "kislovodsk", "viewpoint", "lermontov"],
    maps_text("Гора-Кольцо", "Кисловодск", "Ring Mountain Koltso-gora", "Kislovodsk", 43.941389, 42.693611),
))

# 11) Кисловодская горная астрономическая станция ----------------------------------
RECORDS.append(rec(
    "kislovodsk-astronomical-station",
    "Đài quan sát Thiên văn Núi Kislovodsk (Ax-tra-nô-mi-tra-xcai-a)",
    "Кисловодская горная астрономическая станция",
    "Kislovodsk Mountain Astronomical Station",
    ["other"],
    43.746111, 42.523611,
    "Cao nguyên Shatzhatmaz, cách Kislovodsk khoảng 25-30 km về phía nam, tỉnh Stavropol, Nga",
    "Trạm quan sát Mặt Trời trên cao nguyên Shatzhatmaz ở độ cao ~2.100 m, thuộc Đài thiên văn Pulkovo. Nổi tiếng với chuỗi quan trắc vành nhật hoa (Mặt Trời) liên tục hàng đầu thế giới.",
    "Trạm Thiên văn Núi Kislovodsk là một cơ sở khoa học đặc biệt nằm trên cao nguyên Shatzhatmaz ở độ cao khoảng 2.100 m, cách trung tâm Kislovodsk chừng 25-30 km về phía nam. Được thành lập năm 1948 như một chi nhánh của Đài thiên văn chính Pulkovo (Saint Petersburg), trạm chuyên quan sát Mặt Trời nhờ điều kiện khí quyển trong lành, ổn định và nhiều ngày quang mây của vùng núi cao Kavkaz. Trái tim của trạm là chiếc kính nhật hoa (coronograph) cho phép nghiên cứu vành nhật hoa - lớp khí quyển ngoài cùng của Mặt Trời - mà không cần chờ nhật thực. Nơi đây duy trì một trong những chuỗi số liệu quan trắc hoạt động của Mặt Trời liên tục và có giá trị bậc nhất thế giới, phục vụ dự báo 'thời tiết vũ trụ'. Với du khách yêu thiên văn, trạm là điểm đến hiếm có để tìm hiểu về khoa học Mặt Trời giữa khung cảnh núi non hùng vĩ; các chuyến thăm thường cần đăng ký trước và đi bằng phương tiện riêng vì đường lên khá xa và hoang sơ.",
    [
        "Trạm quan sát Mặt Trời trên cao nguyên Shatzhatmaz ~2.100 m, thuộc Đài Pulkovo",
        "Kính nhật hoa nghiên cứu vành nhật hoa Mặt Trời không cần nhật thực",
        "Chuỗi số liệu quan trắc hoạt động Mặt Trời liên tục hàng đầu thế giới",
    ],
    p("Cơ sở khoa học, chỉ tham quan theo đăng ký/tour hẹn trước.",
      "Theo thoả thuận của chương trình tham quan.",
      "Nửa ngày (kể cả đường đi).",
      "Mùa hè và đầu thu khi đường lên núi thuận lợi.",
      "Đường xa và hoang sơ, cần xe địa hình và liên hệ trước; mang áo ấm vì trên cao lạnh và gió."),
    [
        {"title": "Wikipedia (RU) — Кисловодская горная астрономическая станция", "url": "https://ru.wikipedia.org/wiki/Кисловодская_горная_астрономическая_станция"},
        {"title": "Главная (Пулковская) астрономическая обсерватория РАН", "url": "https://www.gaoran.ru/"},
    ],
    ["other", "observatory", "science", "kislovodsk", "mountain", "astronomy"],
    maps_text("Кисловодская горная астрономическая станция", "Кисловодск", "Kislovodsk Mountain Astronomical Station", "Kislovodsk", 43.746111, 42.523611),
))

# 12) Курортный бульвар -----------------------------------------------------------
RECORDS.append(rec(
    "kurortny-boulevard-kislovodsk",
    "Đại lộ Nghỉ dưỡng Kislovodsk (Cu-rôt-nứi bun-va)",
    "Курортный бульвар (Кисловодск)",
    "Kurortny Boulevard, Kislovodsk",
    ["square_street"],
    43.901900, 42.716850,
    "Trung tâm thành phố Kislovodsk, nối tới lối vào Công viên Quốc gia, tỉnh Stavropol, Nga",
    "Phố đi bộ trung tâm và nhộn nhịp nhất Kislovodsk, chạy dọc theo dòng suối Olkhovka tới Hàng cột Narzan. Nơi tập trung kiến trúc nghỉ dưỡng, quán cà phê, đài phun nhạc nước và Nhà tắm Narzan.",
    "Đại lộ Nghỉ dưỡng là trục phố đi bộ sầm uất và mang tính biểu tượng nhất của Kislovodsk, trải dài ở trung tâm thành phố và dẫn thẳng tới Hàng cột Narzan cùng lối vào Công viên Quốc gia Kislovodsk. Con phố hình thành cùng sự phát triển của khu nghỉ dưỡng suối khoáng từ thế kỷ 19, hai bên là những công trình mang phong cách cổ điển và tân nghệ thuật (modern) duyên dáng: các sanatorium, khách sạn, cửa hàng và đặc biệt là toà Nhà tắm Narzan (Narzannye vanny) bằng gạch đỏ - trắng nổi bật. Dọc đại lộ có đài phun nước nhạc nước, những hàng cây, ghế nghỉ và vô số quán cà phê, nơi du khách vừa dạo bộ vừa nhâm nhi nước khoáng Narzan trứ danh. Không có xe cộ ồn ào, không khí trong lành từ dòng Olkhovka và những vườn cây khiến đây là nơi lý tưởng để thong dong ngắm phố, cảm nhận nhịp sống thư thái đặc trưng của một thành phố nghỉ dưỡng Nga. Đại lộ Nghỉ dưỡng chính là 'phòng khách ngoài trời' của Kislovodsk và điểm kết nối mọi thắng cảnh trung tâm.",
    [
        "Phố đi bộ trung tâm chạy dọc suối Olkhovka tới Hàng cột Narzan",
        "Kiến trúc nghỉ dưỡng cổ điển, Nhà tắm Narzan gạch đỏ - trắng và đài nhạc nước",
        "Vô số quán cà phê, không khí trong lành, nhịp sống thư thái đặc trưng",
    ],
    p("Phố đi bộ công cộng, dạo chơi tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 45–60 phút.",
      "Quanh năm; đẹp nhất lúc chiều tối khi lên đèn và đài nhạc nước hoạt động.",
      "Điểm khởi đầu để vào Công viên Quốc gia và tới Hàng cột Narzan; nên thử nếm nước khoáng Narzan tại chỗ."),
    [
        {"title": "Wikipedia (RU) — Курортный бульвар (Кисловодск)", "url": "https://ru.wikipedia.org/wiki/Курортный_бульвар_(Кисловодск)"},
        {"title": "2GIS — Курортный бульвар, Кисловодск", "url": "https://2gis.ru/kislovodsk/geo/12526375198009290"},
    ],
    ["square_street", "boulevard", "kislovodsk", "resort", "walking", "architecture"],
    maps_text("Курортный бульвар", "Кисловодск", "Kurortny Boulevard", "Kislovodsk", 43.901900, 42.716850),
))

# ============================ ZHELEZNOVODSK ============================

# 13) Дворец эмира Бухарского -----------------------------------------------------
RECORDS.append(rec(
    "emir-bukhara-palace-zheleznovodsk",
    "Cung điện Tiểu vương Bukhara, Zheleznovodsk (Đvo-rét e-mi-ra)",
    "Дворец эмира Бухарского (Железноводск)",
    "Palace of the Emir of Bukhara, Zheleznovodsk",
    ["palace"],
    44.134581, 43.029740,
    "Trong Công viên nghỉ dưỡng Zheleznovodsk, chân núi Zheleznaya, thành phố Zheleznovodsk, tỉnh Stavropol, Nga",
    "Dinh thự nghỉ dưỡng lộng lẫy phong cách phương Đông xây đầu thế kỷ 20 cho Tiểu vương Bukhara. Nổi bật với tháp nhọn, gạch men và cầu thang trang trí sư tử, nay thuộc một sanatorium.",
    "Cung điện Tiểu vương Bukhara là một trong những công trình kiến trúc lãng mạn và khác lạ nhất của Zheleznovodsk, nằm trong Công viên nghỉ dưỡng dưới chân núi Zheleznaya. Dinh thự được khởi công đầu thế kỷ 20 (những năm 1900s) theo đơn đặt hàng của Tiểu vương xứ Bukhara (Trung Á) làm nơi nghỉ dưỡng, với thiết kế pha trộn phong cách phương Đông và chiết trung châu Âu: mái vòm, tháp nhọn kiểu minaret, ban công trổ hoa văn, tường ốp gạch men và những chi tiết trang trí tinh xảo. Cầu thang dẫn lên dinh được canh giữ bởi các tượng sư tử, tạo dáng vẻ vương giả. Tuy nhiên vị Tiểu vương qua đời trước khi công trình hoàn tất; sau đó dinh thự được hiến tặng và trải qua nhiều công năng. Thời Xô-viết, nơi đây trở thành một phần của sanatorium nghỉ dưỡng và vẫn giữ vai trò đó đến nay. Với du khách, cung điện là điểm nhấn kiến trúc bắt mắt trong công viên, một 'lát cắt phương Đông' bất ngờ giữa vùng núi Kavkaz và là phông nền chụp ảnh được yêu thích.",
    [
        "Dinh thự nghỉ dưỡng phong cách phương Đông xây đầu thế kỷ 20 cho Tiểu vương Bukhara",
        "Tháp nhọn kiểu minaret, gạch men trang trí và cầu thang canh giữ bởi tượng sư tử",
        "Nay là một phần sanatorium trong Công viên nghỉ dưỡng dưới chân núi Zheleznaya",
    ],
    p("Nằm trong khu sanatorium/công viên; ngắm bên ngoài tự do, vào trong tuỳ quy định của sanatorium.",
      "Dạo công viên miễn phí; tham quan nội thất có thể hạn chế.",
      "Khoảng 30–45 phút.",
      "Cuối xuân đến đầu thu khi công viên xanh mát.",
      "Kết hợp dạo Công viên nghỉ dưỡng, Nhà nghỉ Pushkin và các suối khoáng Zheleznovodsk gần đó."),
    [
        {"title": "Wikipedia (RU) — Дворец эмира Бухарского (Железноводск)", "url": "https://ru.wikipedia.org/wiki/Дворец_эмира_Бухарского_(Железноводск)"},
        {"title": "2GIS — Дворец эмира Бухарского, Железноводск", "url": "https://2gis.ru/zheleznovodsk/geo/70030077127304865"},
    ],
    ["palace", "architecture", "oriental", "zheleznovodsk", "resort", "history"],
    maps_text("Дворец эмира Бухарского", "Железноводск", "Palace of the Emir of Bukhara", "Zheleznovodsk", 44.134581, 43.029740),
))

# 14) Курортное озеро (Железноводск) ----------------------------------------------
RECORDS.append(rec(
    "kurortnoye-lake-zheleznovodsk",
    "Hồ Nghỉ dưỡng Zheleznovodsk (Cu-rôt-nôi-e ô-ze-rô)",
    "Курортное озеро (Железноводск)",
    "Kurortnoye (Resort) Lake, Zheleznovodsk",
    ["park_garden"],
    44.136809, 43.048494,
    "Rìa đông thành phố Zheleznovodsk, dưới chân núi Zheleznaya và Razvalka, tỉnh Stavropol, Nga",
    "Hồ nước nhân tạo thư giãn (còn gọi 'hồ 30 năm Chiến thắng') ở ngoại vi Zheleznovodsk. Bãi tắm, đạp vịt, khu vui chơi và tầm nhìn ra các núi laccolith bao quanh.",
    "Hồ Nghỉ dưỡng là một hồ nước nhân tạo nằm ở rìa đông Zheleznovodsk, còn được người dân gọi là 'hồ 30 năm Chiến thắng' (озеро 30-летия Победы). Hồ được tạo lập trong thời Xô-viết như một khu vui chơi - nghỉ ngơi bên nước cho khách an dưỡng và người dân địa phương, trong khung cảnh được bao quanh bởi các ngọn núi laccolith đặc trưng của vùng Kavkaz Mineralnye Vody như núi Zheleznaya, Razvalka và Beshtau xa xa. Quanh hồ có bãi tắm mùa hè, khu cho thuê thuyền đạp vịt và ca-nô, đường dạo bộ, quán ăn nhẹ và các trò chơi giải trí, tạo nên một không gian thư giãn dễ chịu khác hẳn nhịp 'chữa bệnh' trầm lắng của các suối khoáng. Sau các đợt cải tạo, khu vực bờ hồ được chỉnh trang khang trang hơn với bến bãi, lối đi và tiểu cảnh. Đây là điểm đến gia đình lý tưởng vào mùa hè: buổi sáng đi uống nước khoáng và dạo Công viên nghỉ dưỡng, buổi chiều ra hồ tắm mát, chèo thuyền và ngắm hoàng hôn buông trên nền các đỉnh núi Kavkaz.",
    [
        "Hồ nhân tạo thư giãn còn gọi 'hồ 30 năm Chiến thắng' ở rìa Zheleznovodsk",
        "Bãi tắm mùa hè, thuyền đạp vịt, ca-nô và khu vui chơi gia đình",
        "Tầm nhìn ra các núi laccolith Zheleznaya, Razvalka và Beshtau",
    ],
    p("Không gian ngoài trời, ra vào tự do; dịch vụ tắm và thuê thuyền theo mùa hè.",
      "Vào khu vực miễn phí; thuê thuyền/dịch vụ tính phí.",
      "Khoảng 1–2 giờ.",
      "Mùa hè (tháng 6–9) khi có thể tắm và chèo thuyền.",
      "Kết hợp buổi sáng ở Công viên nghỉ dưỡng và buổi chiều ra hồ; mang đồ bơi nếu định tắm."),
    [
        {"title": "Tourister.ru — Курортное озеро (Железноводск)", "url": "https://www.tourister.ru/world/europe/russia/city/zheleznovodsk/lakes/33437"},
        {"title": "Wikipedia (RU) — Железноводск", "url": "https://ru.wikipedia.org/wiki/Железноводск"},
    ],
    ["park_garden", "lake", "recreation", "zheleznovodsk", "family", "nature"],
    maps_text("Курортное озеро", "Железноводск", "Kurortnoye Resort Lake", "Zheleznovodsk", 44.136809, 43.048494),
))

# 15) Пушкинская галерея (Железноводск) -------------------------------------------
RECORDS.append(rec(
    "pushkin-gallery-zheleznovodsk",
    "Nhà nghỉ Pushkin, Zheleznovodsk (Pút-skin-xcai-a ga-lê-rê-ia)",
    "Пушкинская галерея (Железноводск)",
    "Pushkin Gallery, Zheleznovodsk",
    ["monument", "other"],
    44.135037, 43.031651,
    "Trong Công viên nghỉ dưỡng Zheleznovodsk, chân núi Zheleznaya, thành phố Zheleznovodsk, tỉnh Stavropol, Nga",
    "Toà nhà kính - kim loại thanh thoát dựng năm 1901 trong Công viên nghỉ dưỡng, 'người anh em' của Nhà nghỉ Lermontov ở Pyatigorsk. Nay là không gian hoà nhạc, sân khấu và triển lãm.",
    "Nhà nghỉ Pushkin là một trong những biểu tượng kiến trúc của Zheleznovodsk, toạ lạc giữa Công viên nghỉ dưỡng dưới chân núi Zheleznaya. Được dựng năm 1901, công trình thuộc dòng kiến trúc 'kính - kim loại' của kỷ nguyên nghỉ dưỡng cuối thế kỷ 19 - đầu thế kỷ 20: khung thép đúc sẵn kết hợp những mảng kính lớn, mái vòm nhẹ nhàng và trang trí tinh tế, tạo cảm giác trong trẻo, sang trọng. Các cấu kiện được sản xuất tại nhà máy ở Nizhny Novgorod rồi vận chuyển và lắp ráp tại chỗ - cùng một 'gia đình' thiết kế với Nhà nghỉ Lermontov ở Pyatigorsk. Ngay từ đầu, toà nhà đóng vai trò trung tâm sinh hoạt văn hoá của khu nghỉ dưỡng: nơi tổ chức hoà nhạc, biểu diễn sân khấu, khiêu vũ và triển lãm nghệ thuật cho khách an dưỡng. Trải qua hơn một thế kỷ và nhiều lần trùng tu, Nhà nghỉ Pushkin vẫn hoạt động như một phòng hoà nhạc - triển lãm, đồng thời là điểm nhấn thị giác duyên dáng và phông nền chụp ảnh yêu thích giữa khung cảnh xanh mát của công viên.",
    [
        "Công trình 'kính - kim loại' dựng năm 1901, 'anh em' với Nhà nghỉ Lermontov ở Pyatigorsk",
        "Khung thép đúc sẵn từ Nizhny Novgorod, kiến trúc nghỉ dưỡng đầu thế kỷ 20",
        "Vẫn là phòng hoà nhạc - triển lãm hoạt động trong Công viên nghỉ dưỡng",
    ],
    p("Khu công viên tham quan tự do; buổi biểu diễn/triển lãm theo lịch riêng.",
      "Dạo bên ngoài miễn phí; vé sự kiện tuỳ chương trình.",
      "Khoảng 20–30 phút.",
      "Cuối xuân đến đầu thu khi công viên xanh mát.",
      "Kết hợp Cung điện Tiểu vương Bukhara và các suối khoáng Zheleznovodsk trong cùng công viên."),
    [
        {"title": "Wikipedia (RU) — Пушкинская галерея (Железноводск)", "url": "https://ru.wikipedia.org/wiki/Пушкинская_галерея_(Железноводск)"},
        {"title": "2GIS — Пушкинская галерея, Железноводск", "url": "https://2gis.ru/zheleznovodsk/firm/12526165744759942"},
    ],
    ["monument", "architecture", "concert-hall", "zheleznovodsk", "resort", "landmark"],
    maps_text("Пушкинская галерея", "Железноводск", "Pushkin Gallery", "Zheleznovodsk", 44.135037, 43.031651),
))

# ============================ ESSENTUKI ============================

# 16) Грязелечебница им. Семашко --------------------------------------------------
RECORDS.append(rec(
    "semashko-mud-baths-essentuki",
    "Nhà tắm bùn Semashko, Essentuki (Gri-di-lê-tráp-nhi-xa Xê-mát-cô)",
    "Грязелечебница имени Н. А. Семашко (Ессентуки)",
    "Semashko Mud Baths, Essentuki",
    ["monument", "other"],
    44.049580, 42.867046,
    "Phố Semashko, gần Công viên nghỉ dưỡng, thành phố Essentuki, tỉnh Stavropol, Nga",
    "Toà nhà trị liệu bùn khoáng nguy nga theo phong cách tân cổ điển La Mã, xây năm 1913-1915. Được coi là một trong những công trình y tế - nghỉ dưỡng đẹp nhất châu Âu đầu thế kỷ 20.",
    "Nhà tắm bùn Semashko là công trình biểu tượng và tráng lệ bậc nhất của Essentuki - thành phố nổi tiếng với nước khoáng và trị liệu bùn. Được xây dựng năm 1913-1915 theo thiết kế của kiến trúc sư Yevgeny Shreter nhân kỷ niệm 300 năm triều đại Romanov, toà nhà mô phỏng phong cách các nhà tắm (terma) La Mã cổ đại: khối kiến trúc tân cổ điển đồ sộ với hàng cột uy nghi, các bức tượng thần thoại, cổng vào trang trí đầu bò và sư tử, sân trong theo lối atrium. Ngay từ khi khánh thành, đây đã được xem là một trong những cơ sở trị liệu bùn hiện đại và đẹp nhất châu Âu thời bấy giờ. Cơ sở sử dụng bùn khoáng lấy từ hồ Tambukan gần đó để chữa các bệnh về khớp, thần kinh và da. Sau này công trình được đặt theo tên Nikolai Semashko - người đặt nền móng cho hệ thống y tế Xô-viết. Ngày nay nhà tắm bùn vẫn hoạt động phục vụ điều trị, đồng thời mở cửa cho du khách tham quan kiến trúc và chụp ảnh - một điểm đến kết hợp giữa di sản y tế, lịch sử và mỹ thuật.",
    [
        "Nhà tắm bùn phong cách nhà tắm La Mã cổ đại, xây 1913-1915",
        "Một trong những cơ sở trị liệu bùn đẹp nhất châu Âu đầu thế kỷ 20",
        "Sử dụng bùn khoáng hồ Tambukan; mang tên nhà tổ chức y tế Xô-viết Semashko",
    ],
    p("Là cơ sở y tế đang hoạt động; tham quan kiến trúc bên ngoài tự do, vào trong theo tour hoặc dịch vụ.",
      "Ngắm bên ngoài miễn phí; tham quan có hướng dẫn/điều trị tính phí.",
      "Khoảng 30–45 phút.",
      "Quanh năm.",
      "Kết hợp dạo Công viên nghỉ dưỡng Essentuki (đã có trong cẩm nang) và các gian uống nước khoáng gần đó."),
    [
        {"title": "Culture.ru — Грязелечебница им. Н. А. Семашко", "url": "https://www.culture.ru/institutes/38474/gryazelechebnica-imeni-n-a-semashko"},
        {"title": "Wikipedia (RU) — Грязелечебница имени Семашко", "url": "https://ru.wikipedia.org/wiki/Грязелечебница_имени_Н._А._Семашко"},
    ],
    ["monument", "architecture", "spa", "essentuki", "history", "neoclassical"],
    maps_text("Грязелечебница имени Семашко", "Ессентуки", "Semashko Mud Baths", "Essentuki", 44.049580, 42.867046),
))

# 17) Свято-Пантелеимоновский храм (Ессентуки) ------------------------------------
RECORDS.append(rec(
    "panteleimon-church-essentuki",
    "Nhà thờ Thánh Panteleimon, Essentuki (Pan-tê-lê-i-môn)",
    "Свято-Пантелеимоновский храм (Ессентуки)",
    "St. Panteleimon Church, Essentuki",
    ["church"],
    44.048137, 42.859492,
    "Phố Andzhievskogo 2, thành phố Essentuki, tỉnh Stavropol, Nga",
    "Nhà thờ Chính thống giáo dâng kính Thánh Panteleimon - thánh chữa lành, biểu tượng hợp với thành phố nghỉ dưỡng. Bản gốc thế kỷ 19 bị phá thời Xô-viết, được xây lại khang trang đầu thế kỷ 21.",
    "Nhà thờ Thánh Panteleimon là một trong những thánh đường Chính thống giáo đáng chú ý của Essentuki, dâng kính vị Đại tử đạo Panteleimon - trong truyền thống Chính thống giáo là thánh bảo trợ của y học và sự chữa lành, một biểu tượng rất phù hợp với thành phố nổi tiếng về nước khoáng và trị liệu. Ngôi nhà thờ đầu tiên được dựng vào cuối thế kỷ 19, từng là một trong những công trình tôn giáo đẹp của vùng, nhưng đã bị phá huỷ trong giai đoạn bài trừ tôn giáo thời Xô-viết những năm 1930. Đến đầu thế kỷ 21, một nhà thờ mới được xây dựng để nối lại truyền thống, với kiến trúc Chính thống giáo truyền thống: mái vòm mạ vàng hình củ hành, tường sáng màu, các bích hoạ và biểu tượng thánh (icon) bên trong. Ngày nay nhà thờ là nơi hành lễ, cầu nguyện cho sức khoẻ của giáo dân và du khách, đồng thời là một điểm đến tâm linh yên tĩnh, bổ sung cho trải nghiệm nghỉ dưỡng - chữa lành đặc trưng của Essentuki.",
    [
        "Dâng kính Thánh Panteleimon - thánh bảo trợ y học và sự chữa lành",
        "Bản gốc cuối thế kỷ 19 bị phá thời Xô-viết, xây lại đầu thế kỷ 21",
        "Kiến trúc Chính thống truyền thống với mái vòm mạ vàng hình củ hành",
    ],
    p("Mở cửa hằng ngày cho khách hành hương và tham quan; giờ lễ có thể đông.",
      "Miễn phí (hoan nghênh quyên góp).",
      "Khoảng 20–30 phút.",
      "Quanh năm.",
      "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu; kết hợp Công viên nghỉ dưỡng Essentuki gần đó."),
    [
        {"title": "Sobory.ru — Церковь Пантелеимона Целителя (Ессентуки)", "url": "https://sobory.ru/article/?object=14964"},
        {"title": "Wikipedia (RU) — Ессентуки", "url": "https://ru.wikipedia.org/wiki/Ессентуки"},
    ],
    ["church", "orthodox", "essentuki", "religion", "healing", "architecture"],
    maps_text("Свято-Пантелеимоновский храм", "Ессентуки", "St Panteleimon Church", "Essentuki", 44.048137, 42.859492),
))

# ============================ TP STAVROPOL ============================

# 18) Музей-заповедник им. Прозрителева и Праве -----------------------------------
RECORDS.append(rec(
    "prozritelev-prave-museum-stavropol",
    "Bảo tàng Địa phương học Stavropol (Prô-dri-tê-lép và Pra-vê)",
    "Ставропольский музей-заповедник им. Г. Н. Прозрителева и Г. К. Праве",
    "Stavropol Museum-Reserve (Prozritelev & Prave)",
    ["museum"],
    45.044674, 41.968131,
    "Phố Dzerzhinskogo 135, trung tâm thành phố Stavropol, tỉnh Stavropol, Nga",
    "Bảo tàng địa phương học lâu đời và lớn nhất vùng Stavropol, thành lập năm 1905. Nổi tiếng với bộ sưu tập khảo cổ, cổ sinh (bao gồm hoá thạch voi răng kiếm) và lịch sử vùng Bắc Kavkaz.",
    "Bảo tàng - khu bảo tồn Stavropol mang tên hai nhà sáng lập Grigory Prozritelev và Georgy Prave là bảo tàng địa phương học chủ chốt của cả vùng Stavropol và là một trong những bảo tàng lâu đời nhất Bắc Kavkaz, hình thành năm 1905 từ việc hợp nhất hai bộ sưu tập tư nhân. Đây là 'kho ký ức' tổng hợp của vùng, với hơn 300.000 hiện vật trải rộng nhiều lĩnh vực: cổ sinh vật học (nổi bật là các bộ xương hoá thạch voi cổ đại tìm thấy trong vùng), khảo cổ học các nền văn hoá thảo nguyên và Kavkaz, dân tộc học các dân tộc sinh sống nơi đây, lịch sử quân sự, tự nhiên và đời sống thế kỷ 19-20. Các gian trưng bày dẫn dắt người xem từ thời tiền sử, qua thời kỳ lập pháo đài Stavropol trên tuyến phòng thủ Kavkaz, đến những biến động của thế kỷ 20. Với du khách, đây là điểm khởi đầu lý tưởng để hiểu tổng thể thiên nhiên, lịch sử và các dân tộc của vùng đất giao thoa Âu - Á này trước khi khám phá các thành phố suối khoáng.",
    [
        "Bảo tàng địa phương học lớn nhất vùng, thành lập năm 1905, hơn 300.000 hiện vật",
        "Bộ sưu tập cổ sinh nổi tiếng với hoá thạch voi cổ đại tìm thấy trong vùng",
        "Trưng bày khảo cổ, dân tộc học và lịch sử lập pháo đài Stavropol",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa mức phải chăng (vài trăm rúp); ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm; hợp cả những ngày thời tiết xấu.",
      "Nằm ngay trung tâm, gần Đồi Pháo đài; thuyết minh chủ yếu bằng tiếng Nga."),
    [
        {"title": "Ставропольский музей-заповедник (сайт)", "url": "https://www.stavmuseum.ru/"},
        {"title": "Wikipedia (RU) — Ставропольский музей-заповедник", "url": "https://ru.wikipedia.org/wiki/Ставропольский_государственный_историко-культурный_и_природно-ландшафтный_музей-заповедник_имени_Г._Н._Прозрителева_и_Г._К._Праве"},
    ],
    ["museum", "history", "local-lore", "stavropol", "archaeology", "paleontology"],
    maps_text("Ставропольский музей-заповедник Прозрителева и Праве", "Ставрополь", "Stavropol Museum-Reserve Prozritelev Prave", "Stavropol", 45.044674, 41.968131),
    official_site="https://www.stavmuseum.ru/",
))

# 19) Ставропольский краевой музей изобразительных искусств -----------------------
RECORDS.append(rec(
    "stavropol-fine-arts-museum",
    "Bảo tàng Mỹ thuật Vùng Stavropol (I-zô-bra-di-ten-nức ix-cút-xtv)",
    "Ставропольский краевой музей изобразительных искусств",
    "Stavropol Regional Museum of Fine Arts",
    ["museum"],
    45.045157, 41.974545,
    "Phố Dzerzhinskogo 115-119, trung tâm thành phố Stavropol, tỉnh Stavropol, Nga",
    "Bảo tàng mỹ thuật chính của vùng, sở hữu bộ sưu tập hội hoạ Nga và châu Âu, nghệ thuật phương Đông và mỹ thuật Xô-viết. Trưng bày trong các toà nhà lịch sử ở trung tâm Stavropol.",
    "Bảo tàng Mỹ thuật Vùng Stavropol là bảo tàng nghệ thuật hàng đầu của vùng, hình thành từ giữa thế kỷ 20 và ngày nay sở hữu một bộ sưu tập đa dạng, có giá trị. Các gian trưng bày trải rộng từ hội hoạ Nga thế kỷ 18-19 (bao gồm tác phẩm của các bậc thầy phong cảnh và chân dung), nghệ thuật Xô-viết, đến mỹ thuật châu Âu Tây Âu, đồ hoạ, điêu khắc và nghệ thuật trang trí ứng dụng; đặc biệt bảo tàng còn có sưu tập nghệ thuật phương Đông (Nhật Bản, Trung Quốc, Ấn Độ) khá thú vị. Bảo tàng đặt trong những toà nhà lịch sử ở trung tâm thành phố, bản thân kiến trúc cũng góp phần vào trải nghiệm tham quan. Bên cạnh bộ sưu tập thường trực, nơi đây thường xuyên tổ chức các triển lãm chuyên đề, sự kiện giáo dục nghệ thuật và giao lưu văn hoá, trở thành một trung tâm đời sống nghệ thuật của Stavropol. Với du khách, đây là điểm dừng lý tưởng để thưởng lãm nghệ thuật và cảm nhận đời sống văn hoá đô thị của thủ phủ vùng.",
    [
        "Bảo tàng mỹ thuật hàng đầu vùng Stavropol với bộ sưu tập đa dạng",
        "Hội hoạ Nga và châu Âu, mỹ thuật Xô-viết cùng sưu tập nghệ thuật phương Đông",
        "Trưng bày trong các toà nhà lịch sử ở trung tâm thành phố",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa mức phải chăng; ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; hợp cả những ngày thời tiết xấu.",
      "Nằm ở trung tâm, dễ kết hợp Bảo tàng địa phương học và Đồi Pháo đài; xem lịch triển lãm trước khi đến."),
    [
        {"title": "Ставропольский краевой музей изобразительных искусств (сайт)", "url": "https://www.artmuseum26.ru/"},
        {"title": "2GIS — Музей изобразительных искусств, Ставрополь", "url": "https://2gis.ru/stavropol/firm/8022565117231599"},
    ],
    ["museum", "art", "stavropol", "painting", "culture", "oriental-art"],
    maps_text("Ставропольский краевой музей изобразительных искусств", "Ставрополь", "Stavropol Museum of Fine Arts", "Stavropol", 45.045157, 41.974545),
    official_site="https://www.artmuseum26.ru/",
))

# 20) Крепостная гора (Ставрополь) ------------------------------------------------
RECORDS.append(rec(
    "fortress-hill-stavropol",
    "Đồi Pháo đài Stavropol (Cre-pốt-nai-a ga-ra)",
    "Крепостная гора (Ставрополь)",
    "Fortress Hill, Stavropol",
    ["fortress", "monument"],
    45.049743, 41.974869,
    "Trung tâm lịch sử thành phố Stavropol, tỉnh Stavropol, Nga",
    "Nơi khai sinh thành phố Stavropol: pháo đài trên tuyến phòng thủ Azov - Mozdok năm 1777. Nay là quảng trường - công viên với tàn tích tường thành, tượng đài lính canh Kavkaz và tầm nhìn thành phố.",
    "Đồi Pháo đài là cái nôi lịch sử của Stavropol - chính tại đây năm 1777, một pháo đài đã được dựng lên như một mắt xích trong tuyến phòng thủ Azov - Mozdok của Đế quốc Nga ở Bắc Kavkaz, và từ pháo đài ấy thành phố Stavropol dần hình thành (tên thành phố trong tiếng Hy Lạp nghĩa là 'thành phố của thánh giá'). Ngày nay, ngọn đồi ở trung tâm thành phố được quy hoạch thành một không gian quảng trường - công viên tưởng niệm, nơi vẫn còn lưu giữ một đoạn tường thành pháo đài bằng đá được bảo tồn/phục dựng như một di tích. Điểm nhấn nổi bật là tượng đài người lính canh Kavkaz (памятник солдату-красногвардейцу / 'lính canh') và các đài kỷ niệm gắn với lịch sử quân sự của vùng. Từ trên đồi, du khách có tầm nhìn thoáng ra trung tâm thành phố cùng nhà thờ, quảng trường và những đại lộ cây xanh. Đây là điểm đến cô đọng nhất để cảm nhận nguồn gốc 'thành phố pháo đài' của Stavropol, thường được ghép với các bảo tàng và phố đi bộ trung tâm lân cận.",
    [
        "Nơi dựng pháo đài Stavropol năm 1777 trên tuyến phòng thủ Azov - Mozdok",
        "Còn lưu đoạn tường thành đá và tượng đài người lính canh Kavkaz",
        "Quảng trường - công viên trung tâm với tầm nhìn ra thành phố",
    ],
    p("Không gian công cộng ngoài trời, tham quan tự do cả ngày.",
      "Miễn phí.",
      "Khoảng 30–45 phút.",
      "Cuối xuân đến đầu thu; đẹp vào chiều mát.",
      "Kết hợp Bảo tàng địa phương học, Bảo tàng Mỹ thuật và phố trung tâm; là điểm định vị lịch sử tốt để bắt đầu tham quan Stavropol."),
    [
        {"title": "Wikipedia (RU) — Крепостная гора (Ставрополь)", "url": "https://ru.wikipedia.org/wiki/Крепостная_гора_(Ставрополь)"},
        {"title": "Wikipedia (RU) — Ставрополь", "url": "https://ru.wikipedia.org/wiki/Ставрополь"},
    ],
    ["fortress", "monument", "stavropol", "history", "viewpoint", "landmark"],
    maps_text("Крепостная гора", "Ставрополь", "Fortress Hill", "Stavropol", 45.049743, 41.974869),
))

# 21) Тифлисские ворота (Ставрополь) ----------------------------------------------
RECORDS.append(rec(
    "tiflis-gate-stavropol",
    "Cổng Tiflis, Stavropol (Típ-lít-xki-e vô-rô-ta)",
    "Тифлисские ворота (Ставрополь)",
    "Tiflis Gate, Stavropol",
    ["monument"],
    45.052164, 41.992818,
    "Đại lộ Karla Marksa / phố Ermolova, trung tâm thành phố Stavropol, tỉnh Stavropol, Nga",
    "Cổng khải hoàn bằng đá xây năm 1841 đánh dấu điểm khởi đầu con đường lịch sử từ Stavropol đi Tiflis (Tbilisi). Bị phá thời Xô-viết, được phục dựng năm 1998 và trở thành biểu tượng đô thị.",
    "Cổng Tiflis là một trong những biểu tượng lịch sử của Stavropol, một cổng khải hoàn bằng đá dựng năm 1841 do thương gia Gavriil Tamamshev tài trợ, nhằm kỷ niệm 25 năm ngày tướng Aleksey Yermolov nhậm chức chỉ huy vùng Kavkaz và đánh dấu điểm khởi đầu tuyến đường quân sự - thương mại lịch sử nối Stavropol với Tiflis (nay là Tbilisi, thủ đô Gruzia). Công trình mang phong cách cổ điển với vòm cuốn uy nghi, từng là 'cửa ngõ phía nam' quan trọng của thành phố, nơi đưa tiễn và đón chào lữ khách trên con đường Kavkaz. Trong thời Xô-viết, cổng bị dỡ bỏ vào những năm 1930 khi mở rộng đường phố. Đến năm 1998, nhân dịp kỷ niệm thành phố, Cổng Tiflis được phục dựng gần đúng vị trí và hình dáng cũ, trở lại là một điểm nhấn kiến trúc - lịch sử và biểu tượng nhận diện của Stavropol. Ngày nay cổng nằm trên trục đại lộ trung tâm, là nơi du khách dừng chân chụp ảnh và tìm hiểu về quá khứ 'thành phố cửa ngõ Kavkaz'.",
    [
        "Cổng khải hoàn đá năm 1841 đánh dấu đường lịch sử Stavropol - Tiflis (Tbilisi)",
        "Bị phá thời Xô-viết, phục dựng năm 1998 thành biểu tượng đô thị",
        "Nằm trên trục đại lộ trung tâm, điểm dừng chụp ảnh và tìm hiểu lịch sử",
    ],
    p("Không gian công cộng ngoài trời, tham quan tự do cả ngày.",
      "Miễn phí.",
      "Khoảng 15–20 phút.",
      "Quanh năm; đẹp khi lên đèn buổi tối.",
      "Kết hợp dạo đại lộ trung tâm và các bảo tàng, quảng trường lân cận."),
    [
        {"title": "Wikipedia (RU) — Тифлисские ворота (Ставрополь)", "url": "https://ru.wikipedia.org/wiki/Тифлисские_ворота_(Ставрополь)"},
        {"title": "2GIS — Тифлисские ворота, Ставрополь", "url": "https://2gis.ru/stavropol/geo/8022672491490852"},
    ],
    ["monument", "triumphal-arch", "stavropol", "history", "architecture", "landmark"],
    maps_text("Тифлисские ворота", "Ставрополь", "Tiflis Gate", "Stavropol", 45.052164, 41.992818),
))

# 22) Ставропольский театр драмы им. Лермонтова -----------------------------------
RECORDS.append(rec(
    "lermontov-drama-theatre-stavropol",
    "Nhà hát Kịch Lermontov, Stavropol (Tê-a-tơ đra-mứ)",
    "Ставропольский академический театр драмы им. М. Ю. Лермонтова",
    "Stavropol Lermontov Academic Drama Theatre",
    ["theatre"],
    45.043069, 41.966209,
    "Quảng trường Lenina 1, trung tâm thành phố Stavropol, tỉnh Stavropol, Nga",
    "Nhà hát kịch lâu đời nhất vùng Bắc Kavkaz, có gốc từ năm 1845. Mang tên thi hào Lermontov, biểu diễn trong toà nhà bề thế bên Quảng trường Lenin - trung tâm đời sống sân khấu của Stavropol.",
    "Nhà hát Kịch hàn lâm Stavropol mang tên Mikhail Lermontov là một trong những nhà hát kịch lâu đời và giàu truyền thống nhất miền nam nước Nga cũng như toàn vùng Bắc Kavkaz, với lịch sử được tính từ giữa thế kỷ 19 (khoảng năm 1845), khi những buổi diễn sân khấu chuyên nghiệp đầu tiên xuất hiện ở Stavropol. Trải qua gần hai thế kỷ, nhà hát đã trở thành trung tâm đời sống sân khấu của vùng, dàn dựng cả kịch cổ điển Nga - thế giới lẫn các vở đương đại, và được phong danh hiệu 'hàn lâm' (академический) - danh hiệu cao dành cho các đoàn nghệ thuật xuất sắc. Việc mang tên Lermontov gắn nhà hát với truyền thống văn học Nga và với chính vùng Kavkaz đã in đậm trong sáng tác của nhà thơ. Ngày nay nhà hát biểu diễn trong một toà nhà bề thế thời Xô-viết bên Quảng trường Lenin ở trung tâm thành phố. Với du khách, một buổi tối xem kịch (hoặc chỉ ngắm kiến trúc và không khí quảng trường) là cách thú vị để chạm vào đời sống văn hoá đương đại của thủ phủ vùng Stavropol.",
    [
        "Nhà hát kịch lâu đời nhất Bắc Kavkaz, có gốc từ khoảng năm 1845",
        "Mang danh hiệu 'hàn lâm' và tên thi hào Lermontov",
        "Biểu diễn trong toà nhà bề thế bên Quảng trường Lenin ở trung tâm",
    ],
    p("Biểu diễn theo lịch mùa diễn (thường buổi tối); phòng vé mở ban ngày.",
      "Giá vé tuỳ vở và vị trí ghế, nhìn chung phải chăng.",
      "Buổi diễn khoảng 2–3 giờ; ngắm ngoài nhanh hơn.",
      "Mùa diễn thu - xuân; mùa hè có thể nghỉ hoặc lưu diễn.",
      "Kiểm tra lịch và đặt vé trước; biểu diễn bằng tiếng Nga. Kết hợp dạo Quảng trường Lenin."),
    [
        {"title": "Ставропольский театр драмы им. Лермонтова (сайт)", "url": "https://www.stavdrama.ru/"},
        {"title": "2GIS — Театр драмы им. Лермонтова, Ставрополь", "url": "https://2gis.ru/stavropol/firm/8022565117237728"},
    ],
    ["theatre", "drama", "stavropol", "culture", "lermontov", "performing-arts"],
    maps_text("Ставропольский театр драмы имени Лермонтова", "Ставрополь", "Stavropol Lermontov Drama Theatre", "Stavropol", 45.043069, 41.966209),
    official_site="https://www.stavdrama.ru/",
))

# 23) Центральный парк (Ставрополь) -----------------------------------------------
RECORDS.append(rec(
    "central-park-stavropol",
    "Công viên Trung tâm Stavropol (Xen-tran-nứi pác)",
    "Центральный парк культуры и отдыха (Ставрополь)",
    "Central Park, Stavropol",
    ["park_garden"],
    45.043696, 41.975947,
    "Trung tâm thành phố Stavropol, gần Đại lộ Karla Marksa, tỉnh Stavropol, Nga",
    "Công viên văn hoá - giải trí lâu đời nhất thành phố, khởi nguồn từ khu vườn thượng lưu thế kỷ 19. Không gian xanh trung tâm với cây cổ thụ, lối dạo, trò chơi và các công trình lịch sử nhỏ.",
    "Công viên Trung tâm là 'lá phổi xanh' và không gian nghỉ ngơi lâu đời nhất của Stavropol, có nguồn gốc từ một khu vườn được lập nên hồi thế kỷ 19, khi giới quý tộc và thị dân bắt đầu kiến tạo các vườn dạo (bulvar) trong thành phố pháo đài đang lớn dần. Trải qua thời gian, khu vườn phát triển thành một công viên văn hoá - giải trí đúng nghĩa với những hàng cây cổ thụ rợp bóng, các lối dạo lát đá, đài phun nước, sân khấu ngoài trời và khu trò chơi cho thiếu nhi. Đây là nơi người dân Stavropol dạo bộ, hẹn hò, đưa trẻ đi chơi và tổ chức các sự kiện, lễ hội thành phố. Công viên nằm ngay trung tâm, liền kề trục đại lộ Karla Marksa và các bảo tàng, nên rất dễ ghép vào lộ trình tham quan. Với du khách, đây là điểm dừng chân thư giãn dễ chịu giữa hành trình khám phá trung tâm lịch sử, đồng thời là nơi quan sát nhịp sống đời thường bình dị và thân thiện của người dân thủ phủ vùng Stavropol.",
    [
        "Công viên văn hoá - giải trí lâu đời nhất thành phố, gốc từ vườn dạo thế kỷ 19",
        "Cây cổ thụ, lối dạo lát đá, đài phun nước và khu trò chơi thiếu nhi",
        "Nằm ngay trung tâm, liền kề đại lộ Karla Marksa và các bảo tàng",
    ],
    p("Không gian mở, dạo chơi tự do cả ngày; khu trò chơi theo giờ riêng.",
      "Vào cửa miễn phí; các trò chơi/dịch vụ tính phí.",
      "Khoảng 45–60 phút.",
      "Cuối xuân đến đầu thu khi cây xanh mát; buổi chiều dễ chịu.",
      "Dễ kết hợp dạo đại lộ trung tâm, các bảo tàng và Đồi Pháo đài lân cận."),
    [
        {"title": "Wikipedia (RU) — Центральный парк (Ставрополь)", "url": "https://ru.wikipedia.org/wiki/Центральный_парк_(Ставрополь)"},
        {"title": "2GIS — Центральный парк, Ставрополь", "url": "https://2gis.ru/stavropol/firm/8022565117267059"},
    ],
    ["park_garden", "stavropol", "recreation", "walking", "family", "city-center"],
    maps_text("Центральный парк культуры и отдыха", "Ставрополь", "Central Park", "Stavropol", 45.043696, 41.975947),
))

# ============================ THIÊN NHIÊN / KMV ============================

# 24) Гора Бештау ------------------------------------------------------------------
RECORDS.append(rec(
    "beshtau-mountain",
    "Núi Beshtau (Bét-tau)",
    "Гора Бештау",
    "Mount Beshtau",
    ["other"],
    44.098346, 43.022109,
    "Giữa các thành phố Pyatigorsk, Zheleznovodsk và Lermontov, vùng Kavkaz Mineralnye Vody, tỉnh Stavropol, Nga",
    "Ngọn núi - laccolith năm đỉnh cao nhất vùng Kavkaz Mineralnye Vody (1.401 m), 'nóc nhà' của cả cụm núi trơ trọi. Điểm leo núi, ngắm toàn cảnh KMV và điểm đến gắn với tu viện Beshtau.",
    "Núi Beshtau là ngọn núi cao nhất và mang tính biểu tượng nhất của vùng Kavkaz Mineralnye Vody, cao 1.401 m. Tên gọi trong các ngôn ngữ Turk nghĩa là 'năm ngọn núi' (besh - năm, tau - núi), mô tả chính xác hình dáng năm đỉnh nhọn quây quần của nó; và cũng chính từ Beshtau mà thành phố dưới chân núi mang tên Pyatigorsk ('thành phố năm núi'). Đây là một laccolith - núi hình thành do magma xâm nhập nâng các lớp đá lên nhưng không phun trào, đặc trưng địa chất của cả vùng KMV với hàng loạt 'núi cô đơn' mọc lên giữa thảo nguyên. Beshtau trơ trọi vươn cao giữa Pyatigorsk, Zheleznovodsk và thị trấn Lermontov, là điểm leo núi (trekking) được yêu thích: từ trên các đỉnh, du khách thu vào tầm mắt toàn cảnh vùng KMV với chuỗi núi laccolith, các thành phố suối khoáng và khi trời quang là dãy Đại Kavkaz cùng đỉnh Elbrus phủ tuyết ở phía nam. Trên sườn núi còn có tu viện Chính thống Beshtau, khiến ngọn núi vừa là điểm đến thiên nhiên - thể thao, vừa mang ý nghĩa tâm linh.",
    [
        "Núi - laccolith năm đỉnh cao nhất vùng KMV (1.401 m), gốc tên 'Pyatigorsk'",
        "Điểm trekking ngắm toàn cảnh chuỗi núi laccolith và đỉnh Elbrus khi trời quang",
        "Trên sườn núi có tu viện Chính thống Beshtau - điểm đến tâm linh",
    ],
    p("Không gian thiên nhiên, leo núi tự do; nên đi ban ngày và về trước tối.",
      "Miễn phí.",
      "Nửa ngày đến trọn ngày tuỳ tuyến leo.",
      "Cuối xuân đến đầu thu; tránh ngày mưa gió, sương mù.",
      "Cần giày leo núi, đủ nước và áo gió; đi theo nhóm/tuyến có dấu, xuất phát sớm. Kết hợp thăm tu viện Beshtau."),
    [
        {"title": "Wikipedia (RU) — Бештау", "url": "https://ru.wikipedia.org/wiki/Бештау"},
        {"title": "Kavkaz.rgo — Бештау", "url": "https://kavkaz.rgo.ru/"},
    ],
    ["other", "mountain", "laccolith", "hiking", "kmv", "viewpoint"],
    maps_text("Гора Бештау", "Пятигорск", "Mount Beshtau", "Pyatigorsk", 44.098346, 43.022109),
))

# 25) Второ-Афонский Успенский Бештаугорский монастырь ----------------------------
RECORDS.append(rec(
    "second-afon-monastery-beshtau",
    "Tu viện Beshtau (Vtô-rô A-phôn-xki)",
    "Второ-Афонский Успенский Бештаугорский мужской монастырь",
    "Second-Athos Dormition Monastery, Beshtau",
    ["church"],
    44.089232, 43.011186,
    "Sườn tây nam núi Beshtau, gần thành phố Lermontov, vùng Kavkaz Mineralnye Vody, tỉnh Stavropol, Nga",
    "Tu viện nam Chính thống giáo trên sườn núi Beshtau, lập năm 1904 bởi các tu sĩ từ Núi Athos (Hy Lạp). Bị đóng thời Xô-viết, hồi sinh từ những năm 1990, điểm hành hương giữa thiên nhiên KMV.",
    "Tu viện Beshtau (tên đầy đủ: Tu viện nam Đức Mẹ An Nghỉ Vtoro-Afonsky trên núi Beshtau) là một tu viện Chính thống giáo nằm trên sườn tây nam ngọn núi Beshtau, gần thành phố Lermontov. Tu viện được thành lập năm 1904 bởi các tu sĩ Nga vốn tu hành tại Núi Athos (Afon) ở Hy Lạp - cái nôi của đời sống đan tu Chính thống giáo - nên mang tên 'Afon thứ hai', với mong muốn tái lập tinh thần khổ tu Athos trên đất Nga giữa khung cảnh núi non thanh tịnh của vùng KMV. Trong thời kỳ Xô-viết chống tôn giáo, tu viện bị đóng cửa và tàn phá vào những năm 1920-1930. Từ những năm 1990, cùng làn sóng phục hưng tôn giáo, tu viện dần được xây dựng lại và hồi sinh đời sống đan tu. Ngày nay nơi đây có nhà thờ, các công trình tu viện và là điểm hành hương yên tĩnh, nơi tín hữu và du khách tìm đến để cầu nguyện, chiêm nghiệm và tận hưởng không khí trong lành, tầm nhìn rộng mở của sườn Beshtau. Tu viện cũng thường được ghép trong hành trình leo núi Beshtau.",
    [
        "Tu viện Chính thống lập năm 1904 bởi tu sĩ từ Núi Athos, nên gọi 'Afon thứ hai'",
        "Bị phá thời Xô-viết, hồi sinh từ những năm 1990",
        "Điểm hành hương thanh tịnh trên sườn núi Beshtau với tầm nhìn rộng mở",
    ],
    p("Mở cửa cho khách hành hương ban ngày; giữ quy tắc nơi tu viện.",
      "Miễn phí (hoan nghênh quyên góp).",
      "Khoảng 45–60 phút (chưa kể đường lên núi).",
      "Cuối xuân đến đầu thu; tránh ngày mưa vì đường núi trơn.",
      "Ăn mặc kín đáo, nữ mang khăn trùm đầu và váy; đường lên là đường núi, nên đi giày phù hợp. Kết hợp leo núi Beshtau."),
    [
        {"title": "Sobory.ru — Второ-Афонский Бештаугорский монастырь", "url": "https://sobory.ru/article/?object=01079"},
        {"title": "Wikipedia (RU) — Второ-Афонский Бештаугорский монастырь", "url": "https://ru.wikipedia.org/wiki/Второ-Афонский_Бештаугорский_монастырь"},
    ],
    ["church", "monastery", "orthodox", "beshtau", "pilgrimage", "kmv"],
    maps_text("Второ-Афонский Бештаугорский монастырь", "Лермонтов", "Second-Athos Beshtau Monastery", "Lermontov", 44.089232, 43.011186),
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
