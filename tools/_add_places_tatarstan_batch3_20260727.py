# -*- coding: utf-8 -*-
"""_add_places_tatarstan_batch3_20260727.py — VÙNG TIÊU ĐIỂM: Tatarstan (lần chạy tự động 2026-07-27, đợt 3).

Bối cảnh: các lần chạy trước đã nâng tatarstan.json lên 48 địa điểm.
Đợt này bổ sung 12 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU (đối chiếu 48 slug hiện có)
=> mục tiêu ~60/50, đưa Tatarstan vượt ngưỡng 50.

Đa dạng loại hình: tu viện – di sản UNESCO, thành cổ khảo cổ, công viên trung tâm, quảng
trường chính, tổ hợp đài tưởng niệm & bảo tàng tôn giáo, đài thiên văn + planetarium, đô thị
công nghệ hiện đại, bảo tàng văn học, điền trang quý tộc + khu thiên nhiên, bảo tàng tương tác,
đài tưởng niệm chiến tranh + công viên, bảo tàng hiện đại kiêm bến tàu sông.

TOẠ ĐỘ: xác minh chéo Wikipedia (RU/EN mục geo), Wikidata, culture.ru, visit-tatarstan,
sobory.ru, autotravel.ru, geomerid, 2GIS, Yandex Maps — 2026-07. Kiểm tra thứ tự (Nga:
Tatarstan lat ~54,5–56,0; lon ~48,6–52,8; KHÔNG đảo lat/lon; đều nằm trong Tatarstan).
Link bản đồ TRỎ-ĐỊA-ĐIỂM: ưu tiên URL trang tổ chức Yandex (yandex.../maps/org/.../<id>/)
khi tra được (Công viên Thiên niên kỷ, Bảo tàng Bánh mì, Bảo tàng Văn minh Bulgar, Điền trang
Molostvov); còn lại dùng text-search theo tên_ru + thành phố, canh giữa theo toạ độ đã kiểm.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

GHI CHÚ (HOÃN sang lần sau — chưa chốt được toạ độ pinpoint đáng tin, KHÔNG bịa):
  - Dom-muzey I. I. Shishkina (Nhà-bảo tàng danh hoạ Shishkin, ул. Набережная 12, Елабуга):
    marquee attraction nhưng snippet/geocoder chưa cho toạ độ chính xác => HOÃN.
  - Muzey-usadba N. A. Durovoy (nữ sĩ quan đầu tiên, ул. Московская 123, Елабуга) => HOÃN.
  - Literaturny muzey M. I. Tsvetaevoy (ул. Казанская 61, Елабуга) => HOÃN.
  (Cả 3 nằm trong lõi cổ Elabuga; thêm khi lấy được lat/lon chuẩn từ Yandex org / Wikidata.)

Chạy:  python3 tools/_add_places_tatarstan_batch3_20260727.py
       python3 tools/normalize_categories.py && python3 tools/build.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"

REGION = "tatarstan"
REGION_NAME_VI = "Cộng hoà Tatarstan"
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

# 1) Tu viện Đức Mẹ An Giấc Sviyazhsk (UNESCO) --------------------------------
RECORDS.append(rec(
    "sviyazhsk-assumption-monastery",
    "Tu viện Đức Mẹ An Giấc Sviyazhsk và Nhà thờ Uspensky (Bogoroditse-Uspensky) – Di sản UNESCO",
    "Успенский собор и монастырь острова-града Свияжск",
    "Assumption Cathedral and Monastery of the Island Town of Sviyazhsk",
    ["church", "museum"],
    55.769712, 48.65285,
    "Đảo Sviyazhsk, phố Uspenskaya, huyện Zelenodolsky, cách Kazan khoảng 30 km về phía tây, Cộng hoà Tatarstan.",
    "Tu viện nam Bogoroditse-Uspensky trên đảo Sviyazhsk được lập năm 1555, ngay sau khi Sa hoàng Ivan "
    "Bạo chúa dựng pháo đài gỗ Sviyazhsk làm bàn đạp chiếm Kazan. Điểm cốt lõi là Nhà thờ Uspensky "
    "(Đức Mẹ An Giấc) với cụm bích hoạ thế kỷ 16 hiếm có bậc nhất nước Nga, nhờ đó cả quần thể được "
    "UNESCO ghi danh Di sản Thế giới năm 2017.",
    "Nằm trên hòn đảo nhỏ nơi hợp lưu ba dòng Volga – Sviyaga – Shchuka, Tu viện Đức Mẹ An Giấc là "
    "'linh hồn' của thị trấn-đảo Sviyazhsk. Tu viện thành lập năm 1555 cùng lúc với việc lập Giáo phận "
    "Kazan, do Tổng linh mục German (sau này là Thánh German xứ Kazan) khai sơn. Nhà thờ chính – "
    "Nhà thờ Uspensky – được các thợ đá vùng Pskov xây năm 1560–1561 (gắn với kiến trúc sư Postnik "
    "Yakovlev, người đồng thời dựng Nhà thờ Thánh Basil ở Moskva). Bên trong còn giữ được gần như "
    "trọn vẹn chu trình bích hoạ từ thời Ivan Bạo chúa – một trong chỉ hai nơi ở Nga còn bảo tồn "
    "được kho tranh tường thế kỷ 16 nguyên vẹn đến vậy, trong đó có hình ảnh hiếm gặp về chính Sa "
    "hoàng. Quần thể còn có Nhà thờ Nikolskaya với tháp chuông cao, các bức tường và phòng ăn cổ. "
    "Sau thời gian dài bị đóng cửa và trưng dụng thời Xô viết, tu viện được phục hồi hoạt động tôn "
    "giáo từ năm 1997 và trở thành điểm hành hương – tham quan trung tâm của đảo Sviyazhsk, thường "
    "kết hợp với chuyến thăm cả thị trấn-đảo.",
    [
        "Nhà thờ Uspensky (1560–1561) lưu giữ chu trình bích hoạ thế kỷ 16 hiếm có bậc nhất nước Nga.",
        "Được UNESCO công nhận Di sản Thế giới năm 2017 nhờ giá trị lịch sử – nghệ thuật độc đáo.",
        "Nằm trên đảo Sviyazhsk giữa hợp lưu Volga – Sviyaga, khung cảnh sông nước ngoạn mục.",
    ],
    {
        "hours_vi": "Khuôn viên tu viện thường mở hằng ngày (khoảng 7:00–19:00); nội thất Nhà thờ Uspensky mở hạn chế để bảo vệ bích hoạ, thăm theo giờ/đoàn.",
        "ticket_vi": "Vào khuôn viên miễn phí; tham quan Nhà thờ Uspensky có bích hoạ thường theo vé/đoàn có hướng dẫn.",
        "duration_vi": "Khoảng 1–1,5 giờ (trong tổng thể nửa ngày tại Sviyazhsk).",
        "best_time_vi": "Cuối xuân đến đầu thu; đẹp vào buổi sáng khi ít khách.",
        "tips_vi": "Ăn mặc kín đáo khi vào khu tôn giáo; kết hợp tham quan cả thị trấn-đảo Sviyazhsk và Xưởng Ngựa (Konny dvor).",
    },
    [
        {"title": "Wikipedia (RU) — Свияжский Успенский монастырь", "url": "https://ru.wikipedia.org/wiki/%D0%A1%D0%B2%D0%B8%D1%8F%D0%B6%D1%81%D0%BA%D0%B8%D0%B9_%D0%A3%D1%81%D0%BF%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%BE%D0%BD%D0%B0%D1%81%D1%82%D1%8B%D1%80%D1%8C"},
        {"title": "Комиссия РФ по делам ЮНЕСКО — Успенский собор и монастырь Свияжска", "url": "https://unesco.ru/en/unescorussia/sites/s1525/"},
        {"title": "sobory.ru — Свияжск, Успенско-Богородичный монастырь", "url": "https://sobory.ru/article/?object=01000"},
    ],
    ["unesco", "monastery", "orthodox", "frescoes", "sviyazhsk", "16th-century", "island"],
    maps_text("Успенский собор и монастырь острова-града Свияжск", "Свияжск",
              "Assumption Cathedral and Monastery of Sviyazhsk", "Sviyazhsk", 55.769712, 48.65285),
))

# 2) Thành cổ Elabuga – "Thành Quỷ" ------------------------------------------
RECORDS.append(rec(
    "elabuga-devils-settlement",
    "Thành cổ Elabuga – 'Thành Quỷ' (Chёrtovo gorodishche)",
    "Елабужское (Чёртово) городище",
    "Yelabuga (Devil's) Ancient Settlement",
    ["fortress", "monument"],
    55.746483, 52.032483,
    "Trên mũi đất cao nơi sông Toima đổ vào sông Kama, rìa tây thành phố Elabuga, Cộng hoà Tatarstan.",
    "Thành cổ Elabuga là di tích khảo cổ trứ danh của người Bulgar vùng Volga, dựng trên một mũi đất "
    "cao nhìn xuống sông Kama. Biểu tượng của nơi này – và của cả thành phố Elabuga – là ngọn tháp "
    "đá tròn được phục dựng năm 1867, phần sót lại của một thành luỹ cổ mà dân gian quen gọi bằng "
    "cái tên đầy huyền bí 'Thành Quỷ'.",
    "Toạ lạc trên mỏm đất cao nơi dòng Toima hoà vào sông Kama, Thành cổ Elabuga (Елабужское "
    "городище) là một trong những di tích khảo cổ nổi tiếng nhất vùng Trung Volga. Ban đầu đây là "
    "nơi trú ẩn của các bộ tộc địa phương nửa sau thiên niên kỷ I, rồi trở thành thành luỹ – trung "
    "tâm của người Bulgar Hồi giáo vùng Volga trong các thế kỷ 10–14, với một pháo đài đá vuông có "
    "tháp canh ở góc. Trải qua nhiều thế kỷ, chỉ còn lại một ngọn tháp đá tròn; đến năm 1867, thị "
    "trưởng kiêm thương gia Ivan Vasilyevich Shishkin (cha của danh hoạ phong cảnh Ivan Shishkin) đã "
    "đứng ra phục dựng ngọn tháp trên nền móng cũ và lợp mái sắt, biến nó thành cột mốc cảnh quan "
    "quen thuộc. Vô số truyền thuyết – về rắn thần tiên tri, về những điều kỳ bí – khiến dân gian "
    "gọi nơi đây là 'Thành Quỷ'. Ngày nay, đứng bên ngọn tháp, du khách phóng tầm mắt ra khúc sông "
    "Kama rộng lớn và toàn cảnh Elabuga – một trong những điểm ngắm cảnh và chụp ảnh đẹp nhất vùng.",
    [
        "Ngọn tháp đá tròn phục dựng năm 1867 – biểu tượng của Elabuga, phần sót lại của thành luỹ Bulgar cổ.",
        "Di tích thành luỹ của người Bulgar vùng Volga thế kỷ 10–14 trên mũi đất cao bên sông Kama.",
        "Điểm ngắm toàn cảnh sông Kama và thành phố Elabuga – gắn với nhiều truyền thuyết 'Thành Quỷ'.",
    ],
    {
        "hours_vi": "Di tích ngoài trời, tham quan tự do cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Mùa ấm (tháng 5–9); đẹp lúc chiều tà khi nắng trải trên sông Kama.",
        "tips_vi": "Đường lên mũi đất có gió lớn; kết hợp thăm khu bảo tồn – bảo tàng Elabuga và quảng trường Thiên niên kỷ Elabuga gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Елабужское городище", "url": "https://ru.wikipedia.org/wiki/%D0%95%D0%BB%D0%B0%D0%B1%D1%83%D0%B6%D1%81%D0%BA%D0%BE%D0%B5_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B8%D1%89%D0%B5"},
        {"title": "Елабужский музей-заповедник — Елабужское городище", "url": "https://www.elabuga.com/ancientTown/aboutAncientTown.html"},
    ],
    ["archaeology", "bulgar", "tower", "kama", "elabuga", "viewpoint", "legend"],
    maps_text("Елабужское (Чёртово) городище", "Елабуга",
              "Yelabuga Devil's Settlement", "Yelabuga", 55.746483, 52.032483),
))

# 3) Công viên Thiên Niên Kỷ Kazan -------------------------------------------
RECORDS.append(rec(
    "millennium-park-kazan",
    "Công viên Thiên Niên Kỷ Kazan (Park Tysyacheletiya)",
    "Парк Тысячелетия Казани",
    "Millennium Park of Kazan",
    ["park_garden"],
    55.783470, 49.123562,
    "Phố Spartakovskaya, quận Vakhitovsky, gần bờ bắc hồ Nizhny (Blizhny) Kaban, trung tâm Kazan.",
    "Công viên Thiên Niên Kỷ khánh thành năm 2005 nhân dịp Kazan tròn 1000 tuổi, nằm ngay trung tâm "
    "bên hồ Kaban. Không gian xanh rộng gần 6 ha nổi bật với đài phun nước lớn, hồ chèo thuyền, khu "
    "trẻ em và những tượng rồng Zilant – linh vật của thành phố – đặt ở các cổng vào.",
    "Được mở cửa ngày 26/8/2005 đúng dịp đại lễ nghìn năm Kazan, Công viên Thiên Niên Kỷ (Парк "
    "Тысячелетия) là một trong những không gian công cộng dễ chịu nhất khu trung tâm. Trục chính của "
    "công viên (vốn là phố Degtyarnaya cũ) được thiết kế như một 'con đường nghìn năm' tượng trưng "
    "cho chặng phát triển của thành phố. Bảy cổng vào đều có tượng rồng Zilant – sinh vật huyền "
    "thoại trên quốc huy Kazan – canh giữ, tạo nét nhận diện riêng. Trong khuôn viên có đài phun "
    "nước lớn, hồ nhỏ cho thuê thuyền, khu vui chơi trẻ em 'Đảo Cổ tích', sân trượt patin, đường "
    "chạy – đạp xe và tượng nhà thơ Bulgar cổ Qol Ghali. Nằm sát hồ Nizhny Kaban và gần Nhà hát "
    "Kamal, đây là điểm dạo bộ, dã ngoại và chụp ảnh lý tưởng cho các gia đình, kết nối thuận tiện "
    "với cụm điểm tham quan trung tâm.",
    [
        "Mở cửa năm 2005 nhân đại lễ 1000 năm Kazan – 'con đường nghìn năm' ở trung tâm thành phố.",
        "Bảy cổng vào gắn tượng rồng Zilant – linh vật huyền thoại của Kazan.",
        "Đài phun nước lớn, hồ chèo thuyền và khu trẻ em bên hồ Kaban – điểm dạo chơi gia đình.",
    ],
    {
        "hours_vi": "Công viên mở tự do cả ngày; các trò chơi/khu dịch vụ hoạt động chủ yếu mùa ấm.",
        "ticket_vi": "Vào công viên miễn phí; một số trò chơi và thuê thuyền tính phí riêng.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; buổi chiều mát và lúc lên đèn.",
        "tips_vi": "Kết hợp dạo hồ Kaban và ghé Nhà hát Kamal gần đó; cuối tuần khá đông gia đình.",
    },
    [
        {"title": "Tourister.ru — Парк тысячелетия Казани", "url": "https://www.tourister.ru/world/europe/russia/city/kazan/parks/24664"},
        {"title": "2GIS Казань — Парк Тысячелетия", "url": "https://2gis.ru/kazan/firm/70000001097313173"},
    ],
    ["park", "millennium", "kazan", "zilant", "fountain", "family", "kaban"],
    maps_org("https://yandex.com/maps/org/park_tysyacheletiya/211811368168/",
             "Millennium Park of Kazan", "Kazan"),
))

# 4) Quảng trường Tự Do (Ploshchad Svobody) ----------------------------------
RECORDS.append(rec(
    "freedom-square-kazan",
    "Quảng trường Tự Do (Ploshchad Svobody)",
    "Площадь Свободы (Казань)",
    "Freedom Square (Kazan)",
    ["square_street"],
    55.795373, 49.124668,
    "Quận Vakhitovsky, trung tâm lịch sử Kazan, Cộng hoà Tatarstan.",
    "Quảng trường Tự Do là quảng trường hành chính – văn hoá lớn bậc nhất Kazan, được bao quanh bởi "
    "những công trình quan trọng nhất thành phố: Nhà hát Opera và Ballet, Nhà Chính phủ (Hội đồng "
    "Nhà nước), Toà thị chính, Nhạc viện và tượng đài Lenin. Đây là nơi diễn ra các lễ diễu hành và "
    "sự kiện lớn của thủ phủ Tatarstan.",
    "Nằm ở phần cao của trung tâm lịch sử, Quảng trường Tự Do (Площадь Свободы) là trái tim hành "
    "chính và văn hoá của Kazan, cùng với Quảng trường Thiên Niên Kỷ tạo thành hai quảng trường "
    "chính của thành phố. Hình thành từ đầu thế kỷ 19 (từng mang tên Quảng trường Nhà thờ, rồi "
    "Quảng trường Nhà hát), nơi đây quy tụ những công trình biểu trưng cho quyền lực và nghệ thuật: "
    "Nhà hát Opera và Ballet Tatar mang tên Musa Cälil bề thế, Nhà Chính phủ – trụ sở Hội đồng Nhà "
    "nước Tatarstan, Toà thị chính Kazan, Nhạc viện Nhà nước và Đại Kịch viện. Ở trung tâm quảng "
    "trường là tượng đài Lenin lớn, còn không gian rộng thoáng phía trước thường là nơi tổ chức "
    "diễu binh, hoà nhạc ngoài trời và các sự kiện trọng đại. Với du khách, đây là điểm dừng để cảm "
    "nhận diện mạo 'thủ đô' của Tatarstan và chụp ảnh kiến trúc công quyền tráng lệ, đồng thời là "
    "khởi điểm thuận tiện để đi bộ khám phá khu trung tâm.",
    [
        "Quảng trường hành chính – văn hoá chính của Kazan, quy tụ Nhà hát Opera-Ballet và Nhà Chính phủ.",
        "Nơi diễn ra diễu hành, hoà nhạc ngoài trời và các sự kiện lớn của thành phố.",
        "Có tượng đài Lenin và cụm kiến trúc công quyền bề thế – điểm ngắm 'bộ mặt' thủ phủ Tatarstan.",
    ],
    {
        "hours_vi": "Không gian công cộng ngoài trời, tham quan tự do cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; đẹp vào buổi tối khi các công trình lên đèn.",
        "tips_vi": "Kết hợp xem một buổi diễn tại Nhà hát Opera-Ballet; từ đây đi bộ xuống phố Bauman rất gần.",
    },
    [
        {"title": "Wikipedia (RU) — Площадь Свободы (Казань)", "url": "https://ru.wikipedia.org/wiki/%D0%9F%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D1%8C_%D0%A1%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D1%8B_(%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C)"},
        {"title": "101hotels — Площадь Свободы, Казань", "url": "https://101hotels.com/recreation/russia/kazan/points/square/ploschad_svobody"},
    ],
    ["square", "kazan", "civic", "opera", "lenin", "architecture", "city-center"],
    maps_text("Площадь Свободы", "Казань", "Freedom Square", "Kazan", 55.795373, 49.124668),
))

# 5) Đài tưởng niệm tiếp nhận Hồi giáo & Bảo tàng Kinh Qur'an lớn nhất --------
RECORDS.append(rec(
    "bolgar-quran-memorial",
    "Đài tưởng niệm việc tiếp nhận Hồi giáo và Bảo tàng 'Cuốn Kinh Qur'an lớn nhất thế giới' (Pamyatny znak)",
    "Памятный знак в честь принятия ислама волжскими булгарами и Музей Корана",
    "Memorial Sign of the Adoption of Islam and the Great Quran Museum",
    ["museum", "monument"],
    54.98577, 49.052669,
    "Khu bảo tồn lịch sử – kiến trúc Bolgar, huyện Spassky, thành phố Bolgar, Cộng hoà Tatarstan.",
    "Đài tưởng niệm hình bát giác mái vòm mạ vàng này được khánh thành năm 2012 để ghi dấu sự kiện "
    "người Bulgar vùng Volga tiếp nhận đạo Hồi năm 922. Bên trong lưu giữ cuốn Kinh Qur'an in lớn "
    "nhất thế giới – được ghi vào Sách Kỷ lục Guinness – cùng khu trưng bày về lịch sử Hồi giáo ở "
    "vùng Volga.",
    "Nằm trong quần thể Di sản Thế giới Bolgar, 'Đài tưởng niệm việc tiếp nhận Hồi giáo của người "
    "Bulgar vùng Volga năm 922' (Памятный знак) là công trình bát giác xây theo phong cách kiến "
    "trúc Bulgar cổ, tường phủ hoa văn và mái vòm bọc đồng mạ vàng lấp lánh, khánh thành ngày "
    "21/5/2012. Sảnh chính của đài đặt cuốn Kinh Qur'an in khổ lớn nhất thế giới, được Sách Kỷ lục "
    "Guinness công nhận: sách cao khoảng 2 m, rộng 1,5 m, nặng tới nửa tấn, gồm hàng trăm trang "
    "giấy đặc biệt; bìa bọc da bê, khảm malachite và nhiều loại đá bán quý trong khung bạc mạ vàng, "
    "phía trên là chiếc đèn chùm rèn khổng lồ. Xung quanh là khu trưng bày kể về lịch sử đạo Hồi và "
    "các mốc tôn giáo quan trọng của vùng Volga. Cùng với Nhà thờ Hồi giáo Trắng và khu thành cổ "
    "Bolgar, đài tưởng niệm là một trong những điểm hành hương – tham quan được ghé thăm nhiều nhất "
    "khi tới Bolgar.",
    [
        "Lưu giữ cuốn Kinh Qur'an in khổ lớn nhất thế giới (kỷ lục Guinness), bìa khảm đá bán quý.",
        "Công trình bát giác mái vòm mạ vàng theo phong cách Bulgar cổ, khánh thành năm 2012.",
        "Ghi dấu sự kiện người Bulgar vùng Volga tiếp nhận đạo Hồi năm 922 – trong quần thể Di sản UNESCO Bolgar.",
    ],
    {
        "hours_vi": "Thường mở hằng ngày khoảng 9:00–18:00 (theo lịch chung của khu bảo tồn Bolgar).",
        "ticket_vi": "Thường gồm trong vé tham quan khu bảo tồn Bolgar; kiểm tra tại cổng.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Mùa hè; nên đi cùng chuyến tham quan cả quần thể Bolgar.",
        "tips_vi": "Ăn mặc kín đáo, giữ yên tĩnh khi vào khu trưng bày Kinh Qur'an; kết hợp thăm Nhà thờ Hồi giáo Trắng gần đó.",
    },
    [
        {"title": "Visit Tatarstan — Памятный знак в честь принятия ислама (922)", "url": "https://visit-tatarstan.com/places/attractions/pamyatniyznak/"},
        {"title": "Tripadvisor — Memorial to Adoption of Islam, Bolgar", "url": "https://www.tripadvisor.ru/Attraction_Review-g2442886-d8670466-Reviews-Memorial_to_Adoption_of_Islam-Bolgar_Republic_of_Tatarstan_Volga_District.html"},
    ],
    ["islam", "quran", "guinness", "bolgar", "memorial", "museum", "unesco"],
    maps_text("Памятный знак принятия ислама", "Болгар",
              "Memorial to Adoption of Islam", "Bolgar", 54.98577, 49.052669),
))

# 6) Đài Thiên văn Engelhardt & Planetarium ----------------------------------
RECORDS.append(rec(
    "engelhardt-observatory",
    "Đài Thiên văn Engelhardt và Nhà chiếu hình vũ trụ (Planetarium ĐHLB Kazan)",
    "Астрономическая обсерватория имени В. П. Энгельгардта",
    "Engelhardt Astronomical Observatory and Planetarium",
    ["museum", "other"],
    55.83972, 48.8125,
    "Làng Oktyabrsky (Observatoriya), huyện Zelenodolsky, cách Kazan khoảng 20 km về phía tây, Cộng hoà Tatarstan.",
    "Đài Thiên văn Engelhardt khai trương năm 1901, là một trong những đài quan sát lịch sử nổi bật "
    "của Nga, thuộc Đại học Liên bang Kazan. Bên cạnh các kính viễn vọng và toà nhà cổ, nơi đây có "
    "nhà chiếu hình vũ trụ (planetarium) hiện đại với những chương trình 'đêm ngắm sao' hấp dẫn.",
    "Cách Kazan chừng 20 km về phía tây, trên một gò đất yên tĩnh cao khoảng 90 m, Đài Thiên văn "
    "Engelhardt (Астрономическая обсерватория им. В. П. Энгельгардта) được khánh thành năm 1901 và "
    "từ năm 1903 mang tên nhà thiên văn V. P. Engelhardt – người đã hiến tặng bộ dụng cụ quan sát "
    "của mình cho Đại học Kazan. Đây là một trong những đài quan sát cổ và giàu truyền thống nhất "
    "nước Nga, gắn với lịch sử thiên văn học Kazan. Quần thể gồm các toà tháp kính viễn vọng, nhà "
    "làm việc, công viên và cả phần mộ của Engelhardt. Từ năm 2013, một nhà chiếu hình vũ trụ "
    "(planetarium) hiện đại được xây trong khuôn viên, thiết kế tiện nghi và tiếp cận cho cả người "
    "khuyết tật; nhờ nằm ở vùng ngoại ô ít ô nhiễm ánh sáng, nơi đây tổ chức các chương trình 'đêm "
    "ngắm sao' cho phép quan sát thiên thể trực tiếp qua kính. Đài thiên văn là điểm đến độc đáo cho "
    "gia đình, học sinh và người yêu khoa học khi ghé vùng phụ cận Kazan.",
    [
        "Đài quan sát lịch sử khai trương năm 1901 – một trong những đài thiên văn cổ danh tiếng của Nga.",
        "Có planetarium hiện đại (2013) với chương trình 'đêm ngắm sao' qua kính viễn vọng.",
        "Khuôn viên yên tĩnh, ít ô nhiễm ánh sáng, thuộc Đại học Liên bang Kazan.",
    ],
    {
        "hours_vi": "Tham quan/planetarium theo lịch buổi và suất chiếu (thường buổi chiều tối và cuối tuần) – nên đặt trước.",
        "ticket_vi": "Bán vé theo chương trình (planetarium, tham quan, đêm ngắm sao); giá thay đổi theo suất.",
        "duration_vi": "Khoảng 1,5–2 giờ.",
        "best_time_vi": "Buổi tối trời quang để quan sát sao; kiểm tra lịch 'Night Show'.",
        "tips_vi": "Đặt vé/suất trước qua trang chính thức; mang áo ấm cho các buổi quan sát ngoài trời; tự lái xe tiện nhất.",
    },
    [
        {"title": "Wikipedia (RU) — Астрономическая обсерватория имени В. П. Энгельгардта", "url": "https://ru.wikipedia.org/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D1%81%D0%B5%D1%80%D0%B2%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8_%D0%92._%D0%9F._%D0%AD%D0%BD%D0%B3%D0%B5%D0%BB%D1%8C%D0%B3%D0%B0%D1%80%D0%B4%D1%82%D0%B0"},
        {"title": "Обсерватория Энгельгардта (КФУ) — официальный сайт", "url": "https://astro.kpfu.ru/"},
    ],
    ["observatory", "planetarium", "astronomy", "science", "kazan", "engelhardt", "stargazing"],
    maps_text("Астрономическая обсерватория имени Энгельгардта", "Зеленодольский район",
              "Engelhardt Astronomical Observatory", "Zelenodolsk District", 55.83972, 48.8125),
))

# 7) Iннополис – đô thị công nghệ trẻ nhất nước Nga --------------------------
RECORDS.append(rec(
    "innopolis",
    "Thành phố Innopolis – đô thị công nghệ trẻ nhất nước Nga",
    "Иннополис",
    "Innopolis",
    ["square_street", "other"],
    55.752085, 48.744618,
    "Huyện Verkhneuslonsky, cách Kazan khoảng 40 km về phía tây, Cộng hoà Tatarstan.",
    "Innopolis là thành phố được quy hoạch riêng cho công nghệ thông tin, thành lập năm 2012 và khai "
    "trương năm 2015 – đô thị trẻ nhất và ít dân nhất nước Nga. Nơi đây có Đại học Innopolis, đặc "
    "khu kinh tế công nghệ cao, kiến trúc hiện đại và là nơi thử nghiệm taxi tự lái.",
    "Cách Kazan chừng 40 km về phía tây, Innopolis (Иннополис) là một hiện tượng đô thị độc đáo của "
    "nước Nga hiện đại: một thành phố được thiết kế và xây mới hoàn toàn để phục vụ ngành công nghệ "
    "thông tin. Ý tưởng hình thành năm 2012 và thành phố chính thức khai trương năm 2015; quy hoạch "
    "tổng thể do kiến trúc sư Singapore Lưu Thái Khôn (Liu Thai Ker) chủ trì, mang phong cách gọn "
    "gàng, nhiều cây xanh. Đây là thành phố trẻ nhất và có dân số nhỏ nhất nước Nga, nhưng lại tập "
    "trung Đại học Innopolis chuyên về CNTT – robot, một đặc khu kinh tế công nghệ cao với nhiều "
    "công ty phần mềm, cùng hạ tầng 'thông minh'. Innopolis được biết đến như một trong những nơi "
    "đầu tiên ở Nga thử nghiệm và vận hành taxi không người lái trên đường phố thực tế. Với du "
    "khách quan tâm tới kiến trúc – công nghệ, một chuyến ghé Innopolis mang lại trải nghiệm tương "
    "phản thú vị so với vẻ cổ kính của Kazan hay Bolgar: hình dung về 'thành phố tương lai' kiểu Nga.",
    [
        "Đô thị được xây mới hoàn toàn cho ngành CNTT – thành phố trẻ nhất, ít dân nhất nước Nga.",
        "Có Đại học Innopolis và đặc khu kinh tế công nghệ cao; kiến trúc hiện đại nhiều cây xanh.",
        "Một trong những nơi đầu tiên ở Nga thử nghiệm taxi tự lái trên đường phố thực tế.",
    ],
    {
        "hours_vi": "Là một thành phố – đi lại tự do; các toà nhà/đại học có khu vực hạn chế ra vào.",
        "ticket_vi": "Miễn phí khi dạo phố; một số sự kiện/tham quan chuyên đề có thể cần đăng ký.",
        "duration_vi": "Khoảng 1–2 giờ (kết hợp trên đường Kazan – Sviyazhsk/Innopolis).",
        "best_time_vi": "Mùa ấm để đi bộ ngắm kiến trúc và không gian xanh.",
        "tips_vi": "Tiện kết hợp với chuyến đi đảo Sviyazhsk (cùng hướng tây Kazan); tôn trọng khu vực nội bộ của đại học/doanh nghiệp.",
    },
    [
        {"title": "Большая российская энциклопедия — Иннополис", "url": "https://bigenc.ru/c/innopolis-307664"},
        {"title": "Ruwiki — Иннополис", "url": "https://ru.ruwiki.ru/wiki/%D0%98%D0%BD%D0%BD%D0%BE%D0%BF%D0%BE%D0%BB%D0%B8%D1%81"},
    ],
    ["modern", "it-city", "innopolis", "university", "smart-city", "architecture", "self-driving"],
    maps_text("Иннополис", "Республика Татарстан", "Innopolis", "Tatarstan", 55.752085, 48.744618),
))

# 8) Bảo tàng Jaroslav Hašek (Bugulma) ---------------------------------------
RECORDS.append(rec(
    "bugulma-hasek-museum",
    "Bảo tàng Văn học – Tưởng niệm Jaroslav Hašek (Bugulma)",
    "Литературно-мемориальный музей Ярослава Гашека",
    "Yaroslav Hašek Literary Memorial Museum",
    ["museum"],
    54.53982, 52.79793,
    "Phố Sovetskaya 67, thành phố Bugulma, đông nam Cộng hoà Tatarstan.",
    "Đây là bảo tàng duy nhất trên thế giới dành cho nhà văn Séc Jaroslav Hašek – tác giả 'Vận mệnh "
    "người lính tốt Švejk'. Ông từng làm phó chỉ huy quân sự Bugulma cuối năm 1918; bảo tàng mở năm "
    "1966 trong chính toà nhà bộ chỉ huy khi ấy.",
    "Ít ai ngờ thành phố nhỏ Bugulma ở đông nam Tatarstan lại sở hữu bảo tàng duy nhất trên thế giới "
    "về Jaroslav Hašek – nhà văn trào phúng người Séc, cha đẻ của kiệt tác 'Vận mệnh người lính tốt "
    "Švejk'. Trong thời Nội chiến Nga, từ tháng 10 đến tháng 12/1918, Hašek phục vụ trong Hồng quân "
    "và được cử làm phó chỉ huy quân sự (komendant) thành phố Bugulma. Trải nghiệm này về sau trở "
    "thành chất liệu cho loạt truyện châm biếm 'Chỉ huy trưởng thành Bugulma'. Bảo tàng Văn học – "
    "Tưởng niệm Jaroslav Hašek khai trương ngày 15/1/1966, đặt trong chính toà nhà từng là bộ chỉ "
    "huy quân sự nơi ông làm việc. Không gian trưng bày gồm ba gian và một phòng tưởng niệm, giới "
    "thiệu cuộc đời, sự nghiệp của Hašek, mối liên hệ đặc biệt của ông với Bugulma và với văn học "
    "Séc. Đây là điểm đến thú vị cho những ai yêu văn chương và muốn khám phá một lát cắt bất ngờ "
    "trong quan hệ văn hoá Nga – Séc.",
    [
        "Bảo tàng duy nhất trên thế giới về nhà văn Séc Jaroslav Hašek – tác giả 'Người lính tốt Švejk'.",
        "Đặt trong toà nhà bộ chỉ huy quân sự nơi Hašek làm phó chỉ huy Bugulma năm 1918.",
        "Khai trương năm 1966; gợi mở lát cắt văn hoá Nga – Séc độc đáo giữa lòng Tatarstan.",
    ],
    {
        "hours_vi": "Thường mở 8:00–17:00 hằng ngày, nghỉ Chủ nhật, nghỉ trưa 12:00–13:00 (kiểm tra lại trước khi đến).",
        "ticket_vi": "Vé vào cửa mức phổ thông (giá thấp); có thể đặt hướng dẫn.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm; tiện khi đi qua tuyến đông nam Tatarstan (Bugulma – Almetyevsk).",
        "tips_vi": "Nên gọi trước xác nhận giờ mở cửa; kết hợp dạo trung tâm lịch sử Bugulma.",
    },
    [
        {"title": "Культура.РФ — Литературно-мемориальный музей Ярослава Гашека", "url": "https://www.culture.ru/institutes/4797/literaturno-memorialnyi-muzei-yaroslava-gasheka"},
        {"title": "Музей Ярослава Гашека — официальный сайт", "url": "https://gashekmuseum.ru/"},
    ],
    ["museum", "literature", "hasek", "svejk", "bugulma", "czech", "history"],
    maps_text("Литературно-мемориальный музей Ярослава Гашека", "Бугульма",
              "Yaroslav Hasek Museum", "Bugulma", 54.53982, 52.79793),
))

# 9) Điền trang Molostvov (Dolgaya Polyana) ----------------------------------
RECORDS.append(rec(
    "dolgaya-polyana",
    "Điền trang Molostvov ở Dolgaya Polyana (Usadba Molostvovykh)",
    "Усадьба Молоствовых (Долгая Поляна)",
    "Molostvov Estate at Dolgaya Polyana",
    ["palace", "park_garden"],
    55.0547, 48.9343,
    "Làng Dolgaya Poляna, phố Solnechnaya, huyện Tetyushsky, cách Tetyushi khoảng 14 km, bên hữu ngạn sông Volga, Cộng hoà Tatarstan.",
    "Đây là điền trang quý tộc nông thôn duy nhất ở Tatarstan còn được bảo tồn đến nay. Quần thể gồm "
    "toà nhà chính cuối thế kỷ 19 – đầu thế kỷ 20 cùng những hàng cây thông rụng lá, bồ đề, bạch "
    "dương và nhiều loài cây quý, nằm trên triền đồi Tetyushi nhìn xuống sông Volga.",
    "Trên dải đồi Tetyushi bên hữu ngạn sông Volga (hồ chứa Kuibyshev), làng Dolgaya Polyana lưu giữ "
    "điền trang của dòng họ quý tộc lâu đời Molostvov – điền trang nông thôn duy nhất còn sót lại "
    "của Tatarstan. Công cuộc xây dựng bắt đầu từ thập niên 1870; toà nhà chính hiện nay được dựng "
    "vào khoảng 1904–1907. Người chủ cuối cùng, Vladimir Molostvov, đã cho tạo lập một công viên "
    "dành tặng vợ là Elizaveta Ber, với những hàng cây thông rụng lá, bồ đề và bạch dương được "
    "trồng có chủ ý cùng nhiều loài cây – bụi quý hiếm. Toàn khu – rộng khoảng 400 ha gồm cả đồng "
    "cỏ và rừng lá rộng ven Volga – được xếp hạng là di tích tự nhiên – lịch sử – kiến trúc phức "
    "hợp. Dolgaya Polyana còn nổi tiếng với những câu chuyện huyền bí về một 'bãi trống dị thường' "
    "trong khu rừng, khiến nơi đây được nhiều du khách tò mò tìm đến. Với khung cảnh yên tĩnh, kiến "
    "trúc điền trang cổ và thiên nhiên đẹp, đây là điểm dã ngoại – tham quan lý tưởng khi kết hợp "
    "với Tetyushi và Bolgar.",
    [
        "Điền trang quý tộc nông thôn duy nhất còn được bảo tồn ở Tatarstan (toà nhà chính đầu thế kỷ 20).",
        "Công viên với hàng cây thông rụng lá – bồ đề – bạch dương và nhiều loài cây quý bên sông Volga.",
        "Gắn với truyền thuyết 'bãi trống dị thường' bí ẩn – điểm dã ngoại yên tĩnh vùng Tetyushi.",
    ],
    {
        "hours_vi": "Công viên ngoài trời tham quan tự do ban ngày; toà nhà/khu trưng bày mở theo giờ hành chính (nên hỏi trước).",
        "ticket_vi": "Vào công viên thường miễn phí; tham quan có hướng dẫn/nhà chính có thể thu phí.",
        "duration_vi": "Khoảng 1–1,5 giờ (chưa kể di chuyển).",
        "best_time_vi": "Cuối xuân đến đầu thu; mùa thu lá vàng rất đẹp.",
        "tips_vi": "Đường tới làng khá vắng, tự lái xe hoặc đi tour tiện nhất; kết hợp thăm Tetyushi và Bolgar (bên kia sông).",
    },
    [
        {"title": "Wikipedia (RU) — Долгая Поляна (Татарстан)", "url": "https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BB%D0%B3%D0%B0%D1%8F_%D0%9F%D0%BE%D0%BB%D1%8F%D0%BD%D0%B0_(%D0%A2%D0%B0%D1%82%D0%B0%D1%80%D1%81%D1%82%D0%B0%D0%BD)"},
        {"title": "Visit Tatarstan — Усадьба Молоствовых", "url": "https://visit-tatarstan.com/places/attractions/usadba_molostvovyh/"},
    ],
    ["estate", "manor", "molostvov", "park", "volga", "tetyushi", "nature"],
    maps_org("https://yandex.ru/maps/org/usadba_molostvovykh/226686467578/",
             "Molostvov Estate Dolgaya Polyana", "Tetyushi District"),
))

# 10) Bảo tàng Bánh mì (Bolgar) ----------------------------------------------
RECORDS.append(rec(
    "bolgar-bread-museum",
    "Bảo tàng Bánh mì (Muzey khleba), Bolgar",
    "Музей хлеба (Болгар)",
    "Museum of Bread (Bolgar)",
    ["museum"],
    54.966145, 49.064423,
    "Phố Kul Gali 3, thành phố Bolgar, huyện Spassky, Cộng hoà Tatarstan.",
    "Bảo tàng Bánh mì là một bảo tàng tương tác ngoài trời kể về lịch sử trồng trọt và làm bánh mì "
    "trên đất Tatarstan từ thời cổ đến thế kỷ 20. Quần thể gỗ rộng vài hecta gồm nhà người xay bột, "
    "cối xay gió và cối xay nước hoạt động, lò bánh, lò rèn và khu nông cụ.",
    "Nằm ở phần 'thành nhỏ' phía đông của khu bảo tồn Bolgar, gần lối vào phía dưới, Bảo tàng Bánh "
    "mì (Музей хлеба) mở cửa năm 2012 và nhanh chóng trở thành một trong những điểm được yêu thích "
    "nhất ở Bolgar, đặc biệt với gia đình có trẻ nhỏ. Đây là bảo tàng tương tác giới thiệu toàn bộ "
    "hành trình của hạt lúa và ổ bánh mì – từ nghề nông thời cổ trên vùng đất Bulgar tới đầu thế kỷ "
    "20. Trên khuôn viên khoảng 3,5 ha là một ngôi làng thu nhỏ gồm nhiều công trình gỗ theo lối "
    "truyền thống: nhà và sân của người thợ xay bột, một cối xay gió và một cối xay nước có thể vận "
    "hành, lò nướng bánh, lò rèn, khu trưng bày nông cụ ngoài trời và những dãy hàng của thợ thủ "
    "công. Du khách được xem cách xay bột, nướng bánh và tìm hiểu văn hoá ẩm thực – nông nghiệp của "
    "vùng. Bảo tàng Bánh mì bổ sung một trải nghiệm 'đời thường – dân dã' thú vị bên cạnh các công "
    "trình tôn giáo và khảo cổ đồ sộ của Bolgar.",
    [
        "Bảo tàng tương tác về lịch sử trồng lúa và làm bánh mì ở Tatarstan, mở cửa năm 2012.",
        "Quần thể gỗ ~3,5 ha: nhà thợ xay, cối xay gió & cối xay nước hoạt động, lò bánh, lò rèn.",
        "Trải nghiệm dân dã, thân thiện với gia đình – nằm trong quần thể Di sản UNESCO Bolgar.",
    ],
    {
        "hours_vi": "Thường mở hằng ngày khoảng 9:00–18:00 theo lịch khu bảo tồn Bolgar (mùa hè có thể dài hơn).",
        "ticket_vi": "Bán vé riêng hoặc gộp trong vé tham quan Bolgar; kiểm tra tại quầy.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Mùa ấm (tháng 5–9) khi các cối xay và hoạt động ngoài trời vận hành.",
        "tips_vi": "Đi cùng trẻ em rất phù hợp; thử bánh mì nóng tại lò; kết hợp tham quan cả thành cổ Bolgar.",
    },
    [
        {"title": "Wikipedia (RU) — Музей хлеба (Болгар)", "url": "https://ru.wikipedia.org/wiki/%D0%9C%D1%83%D0%B7%D0%B5%D0%B9_%D1%85%D0%BB%D0%B5%D0%B1%D0%B0_(%D0%91%D0%BE%D0%BB%D0%B3%D0%B0%D1%80)"},
        {"title": "Visit Tatarstan — Музей хлеба", "url": "https://visit-tatarstan.com/places/cultural/muzej_khleba/"},
    ],
    ["museum", "bread", "mill", "interactive", "bolgar", "family", "folk"],
    maps_org("https://yandex.ru/maps/org/muzey_khleba/136276856567/",
             "Museum of Bread Bolgar", "Bolgar"),
))

# 11) Công viên Chiến Thắng & Đài "Rodina-Mat" (Naberezhnye Chelny) ----------
RECORDS.append(rec(
    "chelny-victory-park",
    "Công viên Chiến Thắng và Đài tưởng niệm 'Rodina-Mat', Naberezhnye Chelny",
    "Парк Победы и мемориал «Родина-мать» (Набережные Челны)",
    "Victory Park and 'Motherland' Memorial, Naberezhnye Chelny",
    ["monument", "park_garden"],
    55.75277, 52.42092,
    "Công viên Chiến Thắng, thành phố Naberezhnye Chelny, Cộng hoà Tatarstan.",
    "Đây là quần thể tưởng niệm chính của Naberezhnye Chelny – thành phố lớn thứ hai Tatarstan, quê "
    "hương hãng xe tải KAMAZ. Mở năm 1975 nhân 30 năm Chiến thắng, quần thể gồm ngọn lửa vĩnh cửu, "
    "tượng đài 'Rodina-Mat' (Đất Mẹ) cách điệu và bức tường tưởng niệm khắc tên các liệt sĩ.",
    "Công viên Chiến Thắng (Парк Победы) là trái tim tưởng niệm của Naberezhnye Chelny – đô thị công "
    "nghiệp lớn thứ hai của Tatarstan, nơi đặt tổ hợp sản xuất xe tải KAMAZ trứ danh. Công viên hình "
    "thành từ năm 1980, gồm ba phần: khu tưởng niệm, khu rừng – công viên và khu trò chơi. Trung tâm "
    "là memorial 'Rodina-Mat' (Đất Mẹ) khánh thành ngày 9/5/1975 nhân 30 năm Chiến thắng trong Chiến "
    "tranh Vệ quốc Vĩ đại. Quần thể gồm ba thành phần: ngọn lửa vĩnh cửu, tượng đài Đất Mẹ và bức "
    "tường tang khắc tên 6.809 người con Naberezhnye Chelny đã ngã xuống nơi chiến trường. Điểm nhấn "
    "là tượng đài Đất Mẹ được tạo hình cách điệu như một con chim phượng hoàng, đôi cánh mang các "
    "phù điêu chân dung những người anh hùng. Xung quanh là không gian xanh rộng hơn 7 ha với các "
    "lối đi bộ, đài phun nước và khu vui chơi, là nơi người dân thành phố tưởng niệm, dạo chơi và tổ "
    "chức các sự kiện trọng đại. Với du khách, đây là điểm dừng tiêu biểu để cảm nhận diện mạo hiện "
    "đại và ký ức chiến tranh của 'thành phố KAMAZ'.",
    [
        "Quần thể tưởng niệm chính của Naberezhnye Chelny (mở 1975): lửa vĩnh cửu, tượng Đất Mẹ, tường khắc tên liệt sĩ.",
        "Tượng đài 'Rodina-Mat' cách điệu hình chim phượng hoàng với phù điêu các anh hùng.",
        "Công viên xanh hơn 7 ha ở thành phố lớn thứ hai Tatarstan – quê hương hãng xe tải KAMAZ.",
    ],
    {
        "hours_vi": "Không gian ngoài trời, tham quan tự do cả ngày.",
        "ticket_vi": "Miễn phí (khu trò chơi trong công viên có dịch vụ tính phí riêng).",
        "duration_vi": "Khoảng 40–60 phút.",
        "best_time_vi": "Mùa ấm; trang nghiêm nhất vào dịp 9/5 (Ngày Chiến thắng).",
        "tips_vi": "Kết hợp tham quan thành phố Naberezhnye Chelny và (nếu có dịp) trung tâm/khu công nghiệp KAMAZ; điểm dừng thuận tiện trên đường tới Elabuga.",
    },
    [
        {"title": "Visit Tatarstan — Парк Победы, г. Набережные Челны", "url": "https://visit-tatarstan.com/places/parki-i-mesta-dlya-progulok/park-pobedy-g-naberezhnykh-chelnov/"},
        {"title": "Komandirovka.ru — Родина-мать, Набережные Челны", "url": "https://www.komandirovka.ru/sights/nabchelny/rodina-mat/"},
    ],
    ["memorial", "wwii", "rodina-mat", "park", "naberezhnye-chelny", "kamaz", "victory"],
    maps_text("Мемориал Родина-мать, Парк Победы", "Набережные Челны",
              "Motherland Memorial Victory Park", "Naberezhnye Chelny", 55.75277, 52.42092),
))

# 12) Bảo tàng Văn minh Bulgar & Bến tàu sông --------------------------------
RECORDS.append(rec(
    "bolgar-civilization-museum",
    "Bảo tàng Văn minh Bulgar và Bến tàu sông (Muzey bolgarskoy tsivilizatsii)",
    "Музей болгарской цивилизации (Речной вокзал)",
    "Museum of Bulgarian (Bolgar) Civilization and River Station",
    ["museum"],
    54.98528, 49.05778,
    "Trên triền cao bờ sông Volga, khu bảo tồn Bolgar, huyện Spassky, thành phố Bolgar, Cộng hoà Tatarstan.",
    "Bảo tàng Văn minh Bulgar là công trình hiện đại ấn tượng, xây lấn vào triền đồi bên sông Volga "
    "để không phá vỡ đường chân trời cổ kính của thành cổ Bolgar. Toà nhà vừa là bến tàu sông đang "
    "hoạt động, vừa là bảo tàng với hơn 1.600 hiện vật về nền văn minh Bulgar vùng Volga.",
    "Khánh thành năm 2013, Bảo tàng Văn minh Bulgar (Музей болгарской цивилизации) là 'cánh cửa' "
    "hiện đại dẫn du khách vào quần thể Di sản Thế giới Bolgar. Toà nhà được thiết kế tài tình: một "
    "phần chìm dưới đất và ăn sâu vào triền đồi bên bờ cao sông Volga, sao cho khối kiến trúc mới "
    "không làm hỏng đường chân trời lịch sử của khu thành cổ Bulgar. Công trình đảm nhiệm hai vai "
    "trò: tầng dưới là bến tàu sông (речной вокзал) đang hoạt động, đón các tàu khách cập bến Bolgar "
    "từ sông Volga; các tầng trên là không gian trưng bày rộng hơn 2.000 m² với hơn 1.600 hiện vật "
    "kể về lịch sử hình thành, phát triển của nền văn minh Bulgar vùng Volga và thành phố Bolgar. "
    "Trên tầng cao có nhà hàng và một đài quan sát mở tầm nhìn tuyệt đẹp ra sông Volga cùng toàn "
    "cảnh khu thành cổ. Đây thường là điểm khởi đầu hợp lý cho hành trình khám phá Bolgar, đặc biệt "
    "với du khách đến bằng đường sông.",
    [
        "Bảo tàng hiện đại (2013) xây lấn triền đồi bên sông Volga để giữ nguyên đường chân trời thành cổ Bolgar.",
        "Kết hợp bến tàu sông đang hoạt động và trưng bày hơn 1.600 hiện vật về văn minh Bulgar vùng Volga.",
        "Đài quan sát tầng cao ngắm toàn cảnh sông Volga và khu Di sản UNESCO Bolgar.",
    ],
    {
        "hours_vi": "Thường mở hằng ngày khoảng 9:00–18:00 theo lịch khu bảo tồn Bolgar.",
        "ticket_vi": "Bán vé tham quan (thường gộp trong vé quần thể Bolgar); đài quan sát/nhà hàng có thể riêng.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Mùa hè – mùa tàu sông; đẹp khi ngắm hoàng hôn trên sông Volga từ đài quan sát.",
        "tips_vi": "Bắt đầu tham quan Bolgar từ đây để có cái nhìn tổng quan; lên đài quan sát chụp toàn cảnh trước khi xuống thành cổ.",
    },
    [
        {"title": "Культура.РФ — Музей болгарской цивилизации", "url": "https://www.culture.ru/institutes/54543/muzei-bolgarskoi-civilizacii"},
        {"title": "Visit Tatarstan — Музей болгарской цивилизации", "url": "https://visit-tatarstan.com/places/cultural/muzej_bolgarskoj_civilizacii/"},
    ],
    ["museum", "bolgar", "civilization", "river-station", "volga", "modern", "unesco"],
    maps_org("https://yandex.com/maps/org/muzey_bulgarskoy_tsivilizatsii/225954332288/",
             "Museum of Bulgarian Civilization Bolgar", "Bolgar"),
))


PLAN = {"tatarstan.json": RECORDS}


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
