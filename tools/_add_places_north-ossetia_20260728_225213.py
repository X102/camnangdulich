# -*- coding: utf-8 -*-
"""_add_places_north-ossetia_20260728_225213.py — VÙNG: Cộng hoà Bắc Ossetia–Alania
(Республика Северная Осетия — Алания), Vùng Bắc Kavkaz. Lần chạy tự động 2026-07-28.

Bối cảnh: north-ossetia.json hiện có 7 địa điểm (Dargavs «thành phố người chết», hẻm Kurtatinsky,
hẻm Tsey, pháo đài đá Dzivgis, thác Midagrabin, nhà thờ Hồi giáo Sunni Vladikavkaz, Vườn quốc gia
Alania). Bổ sung 25 địa điểm THẬT, nổi bật, đa dạng loại hình → đưa vùng lên 32. TRÁNH trùng 7 điểm.

Trung tâm là Vladikavkaz; mở rộng ra Alagir, Fiagdon/Kurtatinsky, Digoria, Kobansky/Karmadon,
Beslan, hẻm Daryal.

Phân bố loại hình (25 bản ghi mới):
- museum (3): Bảo tàng quốc gia RSO-Alania, Bảo tàng Mỹ thuật Tuganov, Bảo tàng Văn học Ossetia Khetagurov.
- church (6): Nhà thờ Ossetia Rождества (mộ Kosta Khetagurov), nhà thờ Armenia Grigor Lusavorich,
  đại giáo đường St. George, đại giáo đường Vознесения (Alagir), tu viện Uspensky (Hidikus, cao nhất Nga),
  tu viện nữ Bogoyavlensky (Alagir).
- theatre (3): Nhà hát Opera & Ballet, Nhà hát kịch Nga Vakhtangov, Nhạc viện (nhà thờ Luther Đức cũ).
- monument (3): Tượng tướng Issa Pliyev, tượng Uastyrdzhi bay ra vách hẻm Alagir, đài tưởng niệm Beslan «Thành phố Thiên thần».
- bridge (1): Cầu Gang (Chugunny most) qua sông Terek.
- square_street (2): Đại lộ Prospekt Mira, quảng trường Shtyb.
- fortress (1): Quần thể tháp cổ Tsymyti (Cmiti).
- park_garden (2): Công viên thiếu nhi Zhukovsky, Vườn bách thảo (Dendrarium) Vladikavkaz.
- other (4): hẻm Digorsky, hẻm Kobansky, hẻm Karmadon, hẻm Daryal (Verkhny Lars, phía Nga).

TOẠ ĐỘ — xác minh chéo qua OpenStreetMap/Nominatim (accept-language=ru), ru.wikipedia, culture.ru,
2GIS/Yandex, sobory.ru (2026-07-28). Phạm vi Bắc Ossetia lat ~42.5–44, lon ~43–45 — tất cả toạ độ
trong phạm vi, KHÔNG đảo lat/lon:
  Bảo tàng quốc gia 43.0272318,44.6805008 (OSM, пр.Мира 11); Bảo tàng Mỹ thuật Tuganov 43.0289756,
  44.6810974 (OSM+culture.ru, пр.Мира 12); Bảo tàng Văn học Khetagurov 43.0260071,44.6856963 (OSM);
  Nhà thờ Ossetia Rождества 43.0199400,44.6860176 (OSM+2ГИС, ул.Хетагурова 23а); Nhà thờ Armenia
  43.0223565,44.6815195 (OSM, ул.Армянская 1); St.George 43.0301582,44.6620316 (OSM, ул.Барбашова 38);
  Vознесения Alagir 43.0382880,44.2228098 (OSM, ул.Кодоева); Tu viện Uspensky Hidikus 42.8218000,
  44.2750000 (OSM); Tu viện Bogoyavlensky Alagir 42.9884239,44.2121725 (OSM); Opera&Ballet 43.0309746,
  44.6763897 (OSM, ул.Тхапсаева 18); Русский театр Vakhtangov 43.0303645,44.6791915 (OSM); Filармония/
  kirche 43.0366726,44.6780058 (OSM+culture.ru, ул.Миллера 34); Памятник Pliyev 43.0198510,44.6800822
  (OSM, пл.Плиева); Уастырджи 42.9590791,44.2118027 (OSM, Транскам ~37 км); Beslan Город ангелов
  43.1914803,44.5659323 (OSM); Чугунный мост 43.0206305,44.6809078 (OSM); Prospekt Mira 43.0299562,
  44.6805058 (OSM); Площадь Штыба 43.0213865,44.6819247 (OSM); Цмити 43.2065090,44.4150850 (OSM);
  Детский парк Жуковского 43.0357965,44.6814969 (OSM); Дендрарий 42.9762236,44.6602951 (OSM, Редант);
  Дигорское ущелье 42.8997684,43.6246609 (OSM); Кобанское ущелье/с.Кобан 42.9147000,44.4781950 (OSM);
  Кармадонское ущелье/с.Кармадон 42.8399203,44.5058513 (OSM); Дарьяльское ущелье/Верхний Ларс
  42.7717060,44.6305890 (OSM — điểm phía Nga, cửa hẻm giáp Gruzia).

GHI CHÚ: đã BỎ QUA vì không xác minh được toạ độ tin cậy trong OSM/nguồn (tránh bịa): khu trượt
tuyết Mамисон (Nominatim trả về nhầm làng ở Ingushetia), khu trượt Цей & thánh địa Реком (không có
node OSM riêng — hẻm Tsey đã có trong file), thác Мидаграбин (ĐÃ CÓ trong file), Тропа чудес
Кадаргаван & часовня Нузал (không có node OSM), ЦПКиО им. Хетагурова (không định vị được chính xác;
đã dùng 2 công viên khác). KHÔNG bịa toạ độ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_north-ossetia_20260728_225213.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "north-ossetia"
REGION_NAME_VI = "Cộng hoà Bắc Ossetia–Alania"
FD = "Vùng Bắc Kavkaz"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def maps_org(org_url, name_en, city_en, lat, lon):
    """Ưu tiên khi có URL trang tổ chức (org) của Yandex — trỏ thẳng thẻ địa điểm."""
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": org_url,
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

# 1) Национальный музей РСО-Алания ------------------------------------------------
RECORDS.append(rec(
    "vladikavkaz-national-museum",
    "Bảo tàng Quốc gia Cộng hoà Bắc Ossetia–Alania",
    "Национальный музей Республики Северная Осетия — Алания",
    "National Museum of the Republic of North Ossetia-Alania",
    ["museum"],
    43.0272318, 44.6805008,
    "Đại lộ Mira 11, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Bảo tàng lớn và lâu đời nhất của Bắc Ossetia, thành lập năm 1897, giới thiệu toàn cảnh thiên nhiên, khảo cổ, dân tộc học và lịch sử của người Ossetia. Trụ sở nằm ngay trung tâm Vladikavkaz trên đại lộ Mira.",
    "Bảo tàng Quốc gia Bắc Ossetia–Alania là kho lưu giữ di sản lớn nhất vùng, ra đời từ cuối thế kỷ 19 và ngày nay tập hợp hàng trăm nghìn hiện vật. Các gian trưng bày dẫn du khách đi qua giới tự nhiên vùng Kavkaz, các phát hiện khảo cổ của nền văn hoá Koban nổi tiếng, cho tới đời sống, trang phục, vũ khí và phong tục của người Alan–Ossetia. Bộ sưu tập dân tộc học đặc biệt phong phú, phản ánh truyền thống miền núi, tín ngưỡng và sử thi Nart. Bảo tàng cũng lưu giữ nhiều tư liệu về lịch sử thành phố Vladikavkaz và tiến trình hiện đại của nước cộng hoà. Đây là điểm khởi đầu lý tưởng để hiểu chiều sâu văn hoá Ossetia trước khi khám phá các hẻm núi và làng tháp cổ.",
    [
        "Bảo tàng lâu đời và lớn nhất Bắc Ossetia (thành lập cuối thế kỷ 19).",
        "Bộ sưu tập khảo cổ văn hoá Koban và dân tộc học Alan–Ossetia đồ sộ.",
        "Nằm trên đại lộ Mira, trung tâm lịch sử Vladikavkaz.",
    ],
    p("Thường mở cửa hằng ngày trừ một ngày nghỉ trong tuần, khoảng 10:00–18:00 (nên kiểm tra trước).",
      "Vé vào cửa khiêm tốn (vài trăm rúp); có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm; hợp cả những ngày thời tiết xấu.",
      "Kết hợp dạo bộ đại lộ Mira liền kề. Một phần trụ sở có thể đóng để trùng tu, nên hỏi trước gian nào đang mở; chú thích chủ yếu tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Национальный музей Республики Северная Осетия — Алания", "url": "https://ru.wikipedia.org/wiki/Национальный_музей_Республики_Северная_Осетия_—_Алания"},
        {"title": "Culture.ru — Национальный музей РСО-Алания", "url": "https://www.culture.ru/institutes/3139/nacionalnyi-muzei-respubliki-severnaya-osetiya-alaniya"},
    ],
    ["museum", "history", "ethnography", "vladikavkaz", "koban-culture"],
    maps_text("Национальный музей РСО-Алания", "Владикавказ", "National Museum of North Ossetia-Alania", "Vladikavkaz", 43.0272318, 44.6805008),
))

# 2) Северо-Осетинский художественный музей им. М. Туганова -----------------------
RECORDS.append(rec(
    "vladikavkaz-art-museum-tuganov",
    "Bảo tàng Mỹ thuật Bắc Ossetia mang tên Makharbek Tuganov",
    "Северо-Осетинский республиканский художественный музей имени М. С. Туганова",
    "Makharbek Tuganov Art Museum",
    ["museum"],
    43.0289756, 44.6810974,
    "Đại lộ Mira 12, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Bảo tàng mỹ thuật duy nhất của nước cộng hoà, đặt trong một dinh thự tráng lệ năm 1903 trên đại lộ Mira. Sưu tập tranh, đồ hoạ, điêu khắc Nga, Tây Âu và nghệ thuật Ossetia, mang tên hoạ sĩ Makharbek Tuganov.",
    "Bảo tàng Mỹ thuật Bắc Ossetia mở cửa từ năm 1939 và mang tên Makharbek Tuganov — hoạ sĩ, nhà minh hoạ sử thi Nart, học trò của Ilya Repin. Toà nhà tự thân đã là một tác phẩm: dinh thự thương gia dựng năm 1903, thuộc hàng công trình đẹp nhất Vladikavkaz. Bên trong lưu giữ hơn năm nghìn hiện vật gồm hội hoạ, đồ hoạ, điêu khắc và nghệ thuật trang trí ứng dụng, từ danh hoạ Nga thế kỷ 18–19, một số tác phẩm Tây Âu, đến các nghệ sĩ Ossetia hiện đại. Bộ sưu tập tranh của chính Tuganov cùng các tác phẩm lấy cảm hứng từ sử thi Nart là điểm nhấn độc đáo. Bảo tàng thường xuyên tổ chức triển lãm luân phiên và các buổi giới thiệu nghệ thuật.",
    [
        "Bảo tàng mỹ thuật duy nhất của Bắc Ossetia (mở năm 1939).",
        "Đặt trong dinh thự thương gia lộng lẫy năm 1903 trên đại lộ Mira.",
        "Di sản hội hoạ của Makharbek Tuganov và nghệ thuật lấy cảm hứng sử thi Nart.",
    ],
    p("Thứ Năm–Thứ Ba, khoảng 11:00–18:00; nghỉ Thứ Tư (nên kiểm tra trước).",
      "Vé người lớn khoảng 100 rúp, trẻ em và người cao tuổi khoảng 60 rúp.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; phù hợp mọi thời tiết.",
      "Ngay cạnh Bảo tàng Quốc gia và đại lộ đi bộ Mira — dễ ghép thành một buổi tham quan trung tâm. Chú thích chủ yếu tiếng Nga."),
    [
        {"title": "Culture.ru — Художественный музей им. Махарбека Туганова", "url": "https://www.culture.ru/institutes/11070/khudozhestvennyi-muzei-im-makharbeka-tuganova"},
        {"title": "Wikipedia (RU) — Северо-Осетинский художественный музей", "url": "https://ru.wikipedia.org/wiki/Северо-Осетинский_художественный_музей"},
    ],
    ["museum", "art", "painting", "vladikavkaz", "tuganov"],
    maps_text("Художественный музей им. М. Туганова", "Владикавказ", "Tuganov Art Museum", "Vladikavkaz", 43.0289756, 44.6810974),
))

# 3) Музей осетинской литературы им. Коста Хетагурова -----------------------------
RECORDS.append(rec(
    "vladikavkaz-ossetian-literature-museum",
    "Bảo tàng Văn học Ossetia mang tên Kosta Khetagurov",
    "Музей осетинской литературы имени Коста Хетагурова",
    "Museum of Ossetian Literature named after Kosta Khetagurov",
    ["museum"],
    43.0260071, 44.6856963,
    "Khu trung tâm lịch sử, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Bảo tàng chuyên đề dành cho văn học Ossetia, tôn vinh Kosta Khetagurov — nhà thơ, hoạ sĩ, người khai sinh nền văn học viết Ossetia. Trưng bày bản thảo, sách quý, ảnh và kỷ vật của các nhà văn dân tộc.",
    "Bảo tàng Văn học Ossetia là nơi lưu giữ ký ức chữ nghĩa của một dân tộc miền núi, với trung tâm là Kosta Khetagurov (1859–1906) — người được coi là cha đẻ của văn học và ngôn ngữ văn chương Ossetia. Các gian trưng bày dẫn dắt qua tiến trình hình thành nền văn học viết: từ những bản thảo, ấn phẩm đầu tiên, thư từ, đến ảnh tư liệu và đồ dùng cá nhân của Kosta cùng nhiều tác giả kế tục. Bên cạnh mảng văn học, bảo tàng còn giới thiệu tài năng hội hoạ của Kosta và mối liên hệ giữa văn chương với sử thi, âm nhạc, đời sống tinh thần Ossetia. Đây là điểm đến ý nghĩa cho ai muốn hiểu tâm hồn và bản sắc chữ viết của vùng đất này.",
    [
        "Tôn vinh Kosta Khetagurov — cha đẻ văn học viết Ossetia.",
        "Bản thảo, sách quý, thư từ và kỷ vật của các nhà văn dân tộc.",
        "Kết nối văn chương với hội hoạ và sử thi Nart.",
    ],
    p("Thường mở cửa các ngày trong tuần, khoảng 10:00–18:00 (nên kiểm tra trước).",
      "Vé vào cửa khiêm tốn (vài chục đến vài trăm rúp).",
      "Khoảng 45–60 phút.",
      "Quanh năm; phù hợp mọi thời tiết.",
      "Nằm trong khu trung tâm, dễ kết hợp với nhà thờ Ossetia (nơi có mộ Kosta) gần đó. Chú thích chủ yếu tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Хетагуров, Коста Леванович", "url": "https://ru.wikipedia.org/wiki/Хетагуров,_Коста_Леванович"},
        {"title": "Culture.ru — Музеи Владикавказа (Северная Осетия)", "url": "https://www.culture.ru/institutes/location-vladikavkaz"},
    ],
    ["museum", "literature", "khetagurov", "vladikavkaz", "culture"],
    maps_text("Музей осетинской литературы имени Коста Хетагурова", "Владикавказ", "Museum of Ossetian Literature", "Vladikavkaz", 43.0260071, 44.6856963),
))

# ============================ NHÀ THỜ / TU VIỆN (church) ============================

# 4) Осетинская церковь Рождества Пресвятой Богородицы ----------------------------
RECORDS.append(rec(
    "vladikavkaz-nativity-church",
    "Nhà thờ Ossetia (Giáng sinh Đức Mẹ) — nơi an nghỉ của Kosta Khetagurov",
    "Церковь Рождества Пресвятой Богородицы (Осетинская церковь)",
    "Church of the Nativity of the Virgin (Ossetian Church)",
    ["church"],
    43.0199400, 44.6860176,
    "Phố Kosta Khetagurov 23a, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Ngôi nhà thờ đá cổ nhất Vladikavkaz (thánh hiến năm 1824), quen gọi là «nhà thờ Ossetia». Trong khuôn viên có mộ Kosta Khetagurov cùng nhiều danh nhân Ossetia.",
    "Nhà thờ Giáng sinh Đức Mẹ, người dân quen gọi là «nhà thờ Ossetia», là công trình đá lâu đời nhất còn lại của Vladikavkaz: được dựng thay cho nhà thờ gỗ và thánh hiến năm 1824. Nằm trên sườn dốc nhìn ra sông Terek, đây từng là trung tâm tinh thần của cộng đồng Ossetia theo Chính thống giáo. Điều khiến nơi này trở thành điểm hành hương văn hoá là nghĩa trang nhỏ trong khuôn viên: tại đây an nghỉ Kosta Khetagurov — cha đẻ văn học Ossetia, cùng Gappo Baev (thị trưởng đầu tiên của Vladikavkaz) và nhà ngôn ngữ học lừng danh Vasily Abaev. Kiến trúc mộc mạc, khung cảnh yên tĩnh và ý nghĩa lịch sử khiến đây là một trong những địa chỉ được người Ossetia trân trọng nhất.",
    [
        "Công trình đá cổ nhất Vladikavkaz (thánh hiến năm 1824).",
        "Nơi an nghỉ của Kosta Khetagurov, Gappo Baev và Vasily Abaev.",
        "Vị trí trên sườn dốc nhìn ra sông Terek, gắn với lịch sử Ossetia Chính thống.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–18:00.",
      "Miễn phí (nhà thờ đang hoạt động; tuỳ tâm công đức).",
      "Khoảng 30–45 phút.",
      "Quanh năm; đẹp vào buổi sáng yên tĩnh.",
      "Là nơi thờ tự đang hoạt động: ăn mặc kín đáo, nữ nên trùm khăn. Ghé thăm mộ Kosta trong khuôn viên; kết hợp bảo tàng văn học gần đó."),
    [
        {"title": "Wikipedia (RU) — Храм Рождества Пресвятой Богородицы (Владикавказ)", "url": "https://ru.wikipedia.org/wiki/Храм_Рождества_Пресвятой_Богородицы_(Владикавказ)"},
        {"title": "Sobory.ru — Владикавказ, Церковь Рождества Пресвятой Богородицы", "url": "https://sobory.ru/article/?object=15964"},
    ],
    ["church", "orthodox", "heritage", "khetagurov", "vladikavkaz"],
    maps_org("https://yandex.com/maps/org/tserkov_rozhdestva_bogoroditsy/1121919117/", "Ossetian Church of the Nativity", "Vladikavkaz", 43.0199400, 44.6860176),
))

# 5) Армянская апостольская церковь Святого Григория Просветителя -----------------
RECORDS.append(rec(
    "vladikavkaz-armenian-church",
    "Nhà thờ Armenia Thánh Grigor Người Khai Sáng",
    "Армянская апостольская церковь Святого Григория Просветителя",
    "Armenian Church of St. Gregory the Illuminator",
    ["church"],
    43.0223565, 44.6815195,
    "Phố Armyanskaya 1, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Nhà thờ của cộng đồng Armenia Tông truyền, xây năm 1868 bên hữu ngạn sông Terek, gần cầu Gang. Một điểm nhấn kiến trúc tôn giáo của Vladikavkaz đa sắc tộc.",
    "Nhà thờ Thánh Grigor Người Khai Sáng minh chứng cho bức tranh đa tôn giáo, đa dân tộc của Vladikavkaz — nơi người Nga, Ossetia, Armenia, Gruzia và các cộng đồng khác cùng chung sống. Được cộng đồng Armenia dựng năm 1868 bên bờ phải sông Terek, ngay gần cầu Gang lịch sử, nhà thờ mang phong cách kiến trúc đặc trưng của Giáo hội Tông truyền Armenia với hình khối cân đối và trang trí giản dị mà trang nghiêm. Trải qua thời Xô Viết và được phục hồi, nơi đây tiếp tục là trung tâm sinh hoạt tinh thần của cộng đồng Armenia địa phương. Cùng với nhà thờ Hồi giáo Sunni, nhà thờ Ossetia và các giáo đường Chính thống, công trình góp phần tạo nên diện mạo tôn giáo phong phú của thành phố.",
    [
        "Nhà thờ Armenia Tông truyền, xây năm 1868.",
        "Bên hữu ngạn sông Terek, gần cầu Gang lịch sử.",
        "Biểu tượng cho tính đa tôn giáo, đa sắc tộc của Vladikavkaz.",
    ],
    p("Mở cửa theo giờ lễ, thường ban ngày (nên hỏi trước lịch cụ thể).",
      "Miễn phí (tuỳ tâm công đức).",
      "Khoảng 20–30 phút.",
      "Quanh năm.",
      "Ăn mặc kín đáo khi vào. Dễ kết hợp đi bộ dọc bờ Terek qua cầu Gang và nhà thờ Hồi giáo Sunni gần đó."),
    [
        {"title": "Ruwiki — Церковь Святого Григория Просветителя (Владикавказ)", "url": "https://ru.ruwiki.ru/wiki/Церковь_Святого_Григория_Просветителя_(Владикавказ)"},
        {"title": "Culture.ru — Армянская Апостольская церковь Святого Григория Просветителя", "url": "https://www.culture.ru/institutes/785/armyanskaya-apostolskaya-cerkov-svyatogo-grigoriya-prosvetitelya"},
    ],
    ["church", "armenian", "heritage", "vladikavkaz", "terek"],
    maps_text("Армянская церковь Святого Григория Просветителя", "Владикавказ", "Armenian Church of St. Gregory", "Vladikavkaz", 43.0223565, 44.6815195),
))

# 6) Свято-Георгиевский кафедральный собор ----------------------------------------
RECORDS.append(rec(
    "vladikavkaz-st-george-cathedral",
    "Đại giáo đường Chính thống Thánh George",
    "Свято-Георгиевский кафедральный собор",
    "St. George Orthodox Cathedral",
    ["church"],
    43.0301582, 44.6620316,
    "Phố Barbashova 38, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Ngôi đại giáo đường Chính thống lớn nhất Vladikavkaz, khởi công năm 1996 và cơ bản hoàn thành đầu những năm 2000, ở khu tây thành phố. Trung tâm của giáo phận Vladikavkaz.",
    "Đại giáo đường Thánh George là nhà thờ Chính thống lớn và bề thế nhất thủ phủ Bắc Ossetia. Công trình được khởi công năm 1996 trên một khu đất ở phần tây thành phố và cơ bản hoàn thiện vào đầu thập niên 2000, đóng vai trò nhà thờ chính toà của giáo phận. Với năm mái vòm mạ vàng, không gian nội thất rộng lớn và các bích hoạ, biểu tượng thánh (icon) được chăm chút, đây là nơi diễn ra các đại lễ quan trọng của cộng đồng Chính thống trong vùng. Thánh George — vị thánh chiến binh cưỡi ngựa — có ý nghĩa đặc biệt với người Ossetia, bởi hình tượng này gắn bó chặt chẽ với Uastyrdzhi, vị thần bảo hộ trong tín ngưỡng bản địa. Nhà thờ là điểm dừng đáng chú ý để cảm nhận đời sống tôn giáo đương đại của thành phố.",
    [
        "Đại giáo đường Chính thống lớn nhất Vladikavkaz.",
        "Khởi công năm 1996, năm mái vòm mạ vàng bề thế.",
        "Thánh George gắn với hình tượng Uastyrdzhi trong tín ngưỡng Ossetia.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–19:00.",
      "Miễn phí (tuỳ tâm công đức).",
      "Khoảng 30–45 phút.",
      "Quanh năm; các đại lễ Chính thống rất trang nghiêm.",
      "Nơi thờ tự đang hoạt động: ăn mặc kín đáo, nữ trùm khăn. Nằm ở khu tây, nên đi taxi/ô tô từ trung tâm."),
    [
        {"title": "Wikipedia (RU) — Свято-Георгиевский собор (Владикавказ)", "url": "https://ru.wikipedia.org/wiki/Свято-Георгиевский_собор_(Владикавказ)"},
        {"title": "Азбука паломника — Свято-Георгиевский кафедральный собор (Владикавказ)", "url": "https://azbyka.ru/palomnik/Свято-Георгиевский_кафедральный_собор_(Владикавказ)"},
    ],
    ["church", "orthodox", "cathedral", "vladikavkaz"],
    maps_text("Свято-Георгиевский кафедральный собор", "Владикавказ", "St George Cathedral", "Vladikavkaz", 43.0301582, 44.6620316),
))

# 7) Свято-Вознесенский собор (Алагир) --------------------------------------------
RECORDS.append(rec(
    "alagir-ascension-cathedral",
    "Đại giáo đường Thăng Thiên ở Alagir",
    "Свято-Вознесенский собор (Алагир)",
    "Holy Ascension Cathedral (Alagir)",
    ["church"],
    43.0382880, 44.2228098,
    "Phố Sergei Kodoev 97, thị trấn Alagir, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Nhà thờ Chính thống bằng đá xây giữa thế kỷ 19 (1850s) tại Alagir, nổi tiếng với bích hoạ do cha con dòng họ Khetagurov thực hiện. Di tích kiến trúc – nghệ thuật tiêu biểu của vùng.",
    "Đại giáo đường Thăng Thiên là biểu tượng của thị trấn Alagir — cửa ngõ dẫn vào hẻm núi Alagir và tuyến đường xuyên Kavkaz. Nhà thờ được xây dựng vào những năm 1850 bằng đá địa phương, theo phong cách kết hợp giữa kiến trúc Nga và những nét vùng núi Kavkaz, tạo nên vẻ trầm mặc, vững chãi. Giá trị đặc biệt của công trình nằm ở các bích hoạ nội thất, gắn với tên tuổi dòng họ Khetagurov — trong đó có phần đóng góp của thân phụ Kosta Khetagurov và của chính Kosta. Trải qua thời kỳ Xô Viết đầy biến động, nhà thờ được khôi phục và tiếp tục là trung tâm tinh thần của cư dân Alagir. Với du khách trên hành trình về phía các hẻm núi, đây là điểm dừng chân giàu lịch sử và mỹ cảm.",
    [
        "Nhà thờ đá giữa thế kỷ 19 (thập niên 1850) ở Alagir.",
        "Bích hoạ gắn với dòng họ Khetagurov, trong đó có Kosta.",
        "Cửa ngõ tinh thần dẫn vào hẻm núi Alagir và tuyến xuyên Kavkaz.",
    ],
    p("Mở cửa theo giờ lễ, thường ban ngày.",
      "Miễn phí (tuỳ tâm công đức).",
      "Khoảng 30 phút.",
      "Quanh năm; tiện dừng chân khi đi hẻm Alagir.",
      "Ăn mặc kín đáo. Kết hợp trên cùng hành trình với tượng Uastyrdzhi và tu viện Bogoyavlensky gần Alagir."),
    [
        {"title": "Wikipedia (RU) — Вознесенский собор (Алагир)", "url": "https://ru.wikipedia.org/wiki/Вознесенский_собор_(Алагир)"},
        {"title": "Sobory.ru — Алагир, Собор Вознесения Господня", "url": "https://sobory.ru/article/?object=09649"},
    ],
    ["church", "orthodox", "alagir", "khetagurov", "heritage"],
    maps_text("Свято-Вознесенский собор", "Алагир", "Ascension Cathedral", "Alagir", 43.0382880, 44.2228098),
))

# 8) Аланский Успенский мужской монастырь (Хидикус) -------------------------------
RECORDS.append(rec(
    "alania-dormition-monastery",
    "Tu viện Alania (Uspensky) ở Hidikus — tu viện cao nhất nước Nga",
    "Аланский Успенский мужской монастырь (Хидикус)",
    "Alania Holy Dormition Monastery (Hidikus)",
    ["church"],
    42.8218000, 44.2750000,
    "Làng Hidikus, hẻm núi Kurtatinsky (Fiagdon), huyện Alagirsky, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Tu viện nam Chính thống nằm cao nhất trên lãnh thổ Nga, tọa lạc giữa hẻm núi Kurtatinsky gần làng Hidikus và Fiagdon. Quần thể mang dáng dấp tháp canh Ossetia, nhìn xuống thung lũng núi non hùng vĩ.",
    "Tu viện Alania Uspensky được xem là tu viện Chính thống nằm ở độ cao lớn nhất nước Nga, ẩn mình giữa hẻm núi Kurtatinsky gần các làng cổ Hidikus và Fiagdon. Được lập vào cuối những năm 1990–2000, tu viện được xây theo phong cách gợi nhớ các tháp canh và pháo đài truyền thống của người Ossetia, với những bức tường đá màu xám hoà vào vách núi. Từ khuôn viên, tầm nhìn mở ra thung lũng sông Fiagdon, các sườn núi và làng tháp cổ — một khung cảnh vừa thanh tịnh vừa choáng ngợp. Nơi đây kết hợp đời sống tu hành với vai trò gìn giữ ký ức Kitô giáo Alan cổ xưa. Đường lên tu viện cũng chính là hành trình khám phá một trong những hẻm núi đẹp và giàu di sản nhất Bắc Ossetia.",
    [
        "Tu viện Chính thống ở độ cao lớn nhất nước Nga.",
        "Kiến trúc mô phỏng tháp canh, pháo đài Ossetia, hoà vào vách núi.",
        "Tầm nhìn tuyệt đẹp xuống thung lũng Fiagdon và các làng tháp cổ.",
    ],
    p("Mở cửa ban ngày cho khách hành hương; giờ lễ theo lịch tu viện.",
      "Miễn phí (tuỳ tâm công đức).",
      "Khoảng 45–60 phút (chưa kể đường đi).",
      "Cuối xuân đến đầu thu; mùa đông đường núi có thể khó đi.",
      "Ăn mặc kín đáo, nữ trùm khăn và mặc váy (thường có khăn/váy cho mượn). Nên đi cùng chuyến khám phá hẻm Kurtatinsky và pháo đài Dzivgis."),
    [
        {"title": "Wikipedia (RU) — Аланский Успенский монастырь", "url": "https://ru.wikipedia.org/wiki/Аланский_Успенский_монастырь"},
        {"title": "Комитет по туризму РСО-Алания — Аланский Успенский монастырь", "url": "http://tourism.alania.gov.ru/pages/"},
    ],
    ["church", "monastery", "orthodox", "kurtatinsky", "mountains"],
    maps_text("Аланский Успенский мужской монастырь", "Хидикус", "Alania Dormition Monastery", "Hidikus", 42.8218000, 44.2750000),
))

# 9) Аланский Богоявленский женский монастырь (Алагир) ---------------------------
RECORDS.append(rec(
    "alagir-epiphany-convent",
    "Tu viện nữ Alania Hiển Linh (Bogoyavlensky) gần Alagir",
    "Аланский Богоявленский женский монастырь (Алагир)",
    "Alania Epiphany Convent (Alagir)",
    ["church"],
    42.9884239, 44.2121725,
    "Gần thị trấn Alagir, huyện Alagirsky, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Tu viện nữ Chính thống lớn nhất Bắc Ossetia, nằm ở rìa thị trấn Alagir nơi cửa hẻm núi. Trung tâm hành hương và đời sống nữ tu của giáo phận Vladikavkaz.",
    "Tu viện nữ Bogoyavlensky (Hiển Linh) là cộng đồng nữ tu Chính thống lớn nhất Bắc Ossetia, tọa lạc ngay gần Alagir, nơi đồng bằng bắt đầu nhường chỗ cho những dãy núi Kavkaz. Được thành lập vào đầu thế kỷ 21, tu viện nhanh chóng trở thành một trung tâm hành hương của giáo phận Vladikavkaz–Alania, với nhà thờ, các gian phòng tu và khu vườn được chăm sóc chu đáo. Không gian tĩnh lặng, nề nếp và khung cảnh núi non làm nền khiến nơi đây thu hút cả tín đồ lẫn du khách muốn tìm chốn an yên. Nằm trên trục đường dẫn vào hẻm Alagir và tuyến xuyên Kavkaz, tu viện thường được ghép cùng đại giáo đường Thăng Thiên và tượng Uastyrdzhi trong một hành trình.",
    [
        "Tu viện nữ Chính thống lớn nhất Bắc Ossetia.",
        "Trung tâm hành hương của giáo phận Vladikavkaz–Alania.",
        "Vị trí cửa ngõ hẻm Alagir, khung cảnh núi non thanh tịnh.",
    ],
    p("Mở cửa ban ngày cho khách hành hương; giờ lễ theo lịch tu viện.",
      "Miễn phí (tuỳ tâm công đức).",
      "Khoảng 30–45 phút.",
      "Quanh năm; đẹp vào cuối xuân và mùa thu.",
      "Ăn mặc kín đáo, nữ trùm khăn và mặc váy. Dễ kết hợp với đại giáo đường Alagir và tượng Uastyrdzhi trên đường vào hẻm núi."),
    [
        {"title": "Wikipedia (RU) — Аланский Богоявленский монастырь", "url": "https://ru.wikipedia.org/wiki/Аланский_Богоявленский_монастырь"},
        {"title": "Комитет по туризму РСО-Алания — монастыри Осетии", "url": "http://tourism.alania.gov.ru/"},
    ],
    ["church", "convent", "monastery", "orthodox", "alagir"],
    maps_text("Аланский Богоявленский женский монастырь", "Алагир", "Alania Epiphany Convent", "Alagir", 42.9884239, 44.2121725),
))

# ============================ NHÀ HÁT (theatre) ============================

# 10) Северо-Осетинский театр оперы и балета --------------------------------------
RECORDS.append(rec(
    "vladikavkaz-opera-ballet-theatre",
    "Nhà hát Opera và Ballet Bắc Ossetia",
    "Северо-Осетинский государственный театр оперы и балета",
    "North Ossetian State Opera and Ballet Theatre",
    ["theatre"],
    43.0309746, 44.6763897,
    "Phố Tkhapsaev 18, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Nhà hát opera và ballet của nước cộng hoà, hoạt động từ năm 1958 và từ 2017 trở thành chi nhánh của Nhà hát Mariinsky trứ danh. Trung tâm nghệ thuật hàn lâm của Bắc Ossetia.",
    "Nhà hát Opera và Ballet Bắc Ossetia là niềm tự hào âm nhạc hàn lâm của nước cộng hoà — vùng đất nổi tiếng sản sinh nhiều giọng ca và nhạc sĩ tài năng. Được thành lập năm 1958, nhà hát dàn dựng các vở opera, ballet kinh điển thế giới cùng những tác phẩm mang bản sắc Ossetia và Kavkaz. Một dấu mốc quan trọng đến vào năm 2017, khi nhà hát trở thành chi nhánh của Nhà hát Mariinsky (Saint Petersburg) dưới sự bảo trợ của nhạc trưởng Valery Gergiev — người con của Bắc Ossetia — giúp nâng tầm chất lượng biểu diễn và thu hút nghệ sĩ danh tiếng. Toà nhà nằm ở khu trung tâm gần bờ sông Terek. Với người yêu nhạc cổ điển, một buổi tối tại đây là trải nghiệm văn hoá đáng nhớ ở miền Kavkaz.",
    [
        "Nhà hát opera & ballet của nước cộng hoà, hoạt động từ 1958.",
        "Từ 2017 là chi nhánh Nhà hát Mariinsky, gắn với nhạc trưởng Valery Gergiev.",
        "Chương trình gồm cả kinh điển thế giới lẫn tác phẩm bản sắc Ossetia.",
    ],
    p("Theo lịch biểu diễn; phòng vé thường mở ban ngày đến giờ diễn buổi tối.",
      "Giá vé đa dạng tuỳ suất và vị trí ghế, nhìn chung phải chăng so với các nhà hát lớn.",
      "Một buổi diễn khoảng 2–3 giờ.",
      "Mùa biểu diễn thu–xuân; nên đặt vé trước cho các suất nổi bật.",
      "Xem lịch trên trang chính thức và đặt vé sớm. Trang phục lịch sự khi vào nhà hát."),
    [
        {"title": "Wikipedia (RU) — Северо-Осетинский театр оперы и балета", "url": "https://ru.wikipedia.org/wiki/Северо-Осетинский_театр_оперы_и_балета"},
        {"title": "Комитет по туризму РСО-Алания — театр оперы и балета", "url": "http://tourism.alania.gov.ru/pages/247"},
    ],
    ["theatre", "opera", "ballet", "vladikavkaz", "mariinsky"],
    maps_text("Северо-Осетинский театр оперы и балета", "Владикавказ", "North Ossetian Opera and Ballet Theatre", "Vladikavkaz", 43.0309746, 44.6763897),
))

# 11) Русский академический театр им. Е. Вахтангова ------------------------------
RECORDS.append(rec(
    "vladikavkaz-russian-theatre",
    "Nhà hát Kịch Hàn lâm Nga mang tên Yevgeny Vakhtangov",
    "Русский академический театр имени Е. Вахтангова",
    "Russian Academic Theatre named after Yevgeny Vakhtangov",
    ["theatre"],
    43.0303645, 44.6791915,
    "Khu trung tâm, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Nhà hát kịch nói tiếng Nga lâu đời của Vladikavkaz, mang tên đạo diễn huyền thoại Yevgeny Vakhtangov — người sinh ra tại chính thành phố này. Một trong những sân khấu kịch cổ nhất vùng Bắc Kavkaz.",
    "Nhà hát Kịch Hàn lâm Nga ở Vladikavkaz gắn liền với tên tuổi Yevgeny Vakhtangov — nhà cải cách sân khấu Nga đầu thế kỷ 20, học trò của Stanislavski và là người con của Vladikavkaz. Nhà hát có lịch sử lâu đời, thuộc hàng những sân khấu kịch nói tiếng Nga cổ nhất ở Bắc Kavkaz, với tiết mục trải rộng từ kịch kinh điển Nga và thế giới đến các vở đương đại. Không gian khán phòng cổ điển, đội ngũ diễn viên gắn bó lâu năm và không khí văn hoá đậm chất tỉnh lỵ tạo nên sức hút riêng. Với du khách, đây là dịp để cảm nhận đời sống sân khấu Nga ngay giữa lòng một thành phố đa văn hoá miền núi.",
    [
        "Mang tên Yevgeny Vakhtangov — nhà cải cách sân khấu sinh tại Vladikavkaz.",
        "Một trong những nhà hát kịch nói tiếng Nga cổ nhất Bắc Kavkaz.",
        "Tiết mục từ kịch kinh điển Nga, thế giới đến đương đại.",
    ],
    p("Theo lịch biểu diễn; phòng vé mở ban ngày đến giờ diễn.",
      "Giá vé phải chăng, tuỳ suất và vị trí ghế.",
      "Một buổi diễn khoảng 2–3 giờ.",
      "Mùa biểu diễn thu–xuân.",
      "Vở diễn bằng tiếng Nga. Xem lịch và đặt vé trước; trang phục lịch sự."),
    [
        {"title": "Wikipedia (RU) — Русский академический театр имени Е. Вахтангова (Владикавказ)", "url": "https://ru.wikipedia.org/wiki/Русский_академический_театр_имени_Е._Вахтангова"},
        {"title": "Комитет по туризму РСО-Алания — театры Владикавказа", "url": "http://tourism.alania.gov.ru/"},
    ],
    ["theatre", "drama", "russian", "vladikavkaz", "vakhtangov"],
    maps_text("Русский академический театр имени Вахтангова", "Владикавказ", "Russian Academic Theatre Vakhtangov", "Vladikavkaz", 43.0303645, 44.6791915),
))

# 12) Северо-Осетинская государственная филармония (немецкая кирха) ---------------
RECORDS.append(rec(
    "vladikavkaz-philharmonic-kirche",
    "Nhạc viện Bắc Ossetia (trong nhà thờ Luther Đức cũ)",
    "Северо-Осетинская государственная филармония (бывшая немецкая кирха)",
    "North Ossetian State Philharmonic (former German Kirche)",
    ["theatre"],
    43.0366726, 44.6780058,
    "Phố Miller 34, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Nhạc viện quốc gia của nước cộng hoà, hoạt động từ năm 1944 trong toà nhà thờ Tin Lành Luther của cộng đồng Đức xưa. Một công trình kiến trúc độc đáo và không gian hoà nhạc giàu âm hưởng.",
    "Nhạc viện Bắc Ossetia là trung tâm âm nhạc giao hưởng và thính phòng của nước cộng hoà, đáng chú ý không chỉ vì các buổi hoà nhạc mà còn bởi chính toà nhà. Đây vốn là nhà thờ Tin Lành Luther (kirche) của cộng đồng người Đức từng sinh sống ở Vladikavkaz cho tới thập niên 1930. Sau khi cộng đồng tan rã, toà kiến trúc mang phong cách châu Âu này được chuyển đổi công năng và trở thành trụ sở nhạc viện từ năm 1944. Không gian với trần cao và mái vòm mang lại âm học đặc biệt, rất hợp cho nhạc cổ điển, organ và các buổi độc tấu. Với du khách, nơi đây vừa là điểm thưởng thức âm nhạc, vừa là một chứng tích cho lớp lịch sử đa sắc tộc của thành phố.",
    [
        "Đặt trong nhà thờ Luther Đức cũ, làm nhạc viện từ năm 1944.",
        "Kiến trúc châu Âu với âm học lý tưởng cho nhạc cổ điển và organ.",
        "Chứng tích lịch sử cộng đồng người Đức ở Vladikavkaz.",
    ],
    p("Theo lịch hoà nhạc; phòng vé mở ban ngày đến giờ diễn.",
      "Giá vé phải chăng, tuỳ chương trình.",
      "Một buổi hoà nhạc khoảng 1,5–2 giờ.",
      "Mùa hoà nhạc thu–xuân.",
      "Xem lịch trước để bắt được buổi biểu diễn organ hoặc giao hưởng. Toà nhà đẹp cả khi chụp ảnh bên ngoài."),
    [
        {"title": "Wikipedia (RU) — Северо-Осетинская государственная филармония", "url": "https://ru.wikipedia.org/wiki/Северо-Осетинская_государственная_филармония"},
        {"title": "Culture.ru — Государственная филармония РСО-Алания", "url": "https://www.culture.ru/institutes/97480/gosudarstvennaya-filarmoniya-respubliki-severnaya-osetiya-alaniya"},
    ],
    ["theatre", "philharmonic", "music", "architecture", "vladikavkaz"],
    maps_text("Северо-Осетинская государственная филармония", "Владикавказ", "North Ossetian Philharmonic", "Vladikavkaz", 43.0366726, 44.6780058),
))

# ============================ TƯỢNG ĐÀI (monument) ============================

# 13) Памятник Иссе Плиеву --------------------------------------------------------
RECORDS.append(rec(
    "vladikavkaz-pliyev-monument",
    "Tượng đài tướng Issa Pliyev",
    "Памятник Иссе Александровичу Плиеву",
    "Monument to General Issa Pliyev",
    ["monument"],
    43.0198510, 44.6800822,
    "Quảng trường Pliyev, bên bờ sông Terek, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Tượng đài kỵ mã tôn vinh Issa Pliyev — vị tướng Ossetia hai lần Anh hùng Liên Xô. Dựng năm 1997 trên quảng trường mang tên ông bên bờ sông Terek.",
    "Tượng đài Issa Pliyev là một trong những biểu tượng của Vladikavkaz, tôn vinh người con ưu tú nhất của Bắc Ossetia trong lịch sử quân sự — vị tướng kỵ binh hai lần được phong Anh hùng Liên Xô, nổi danh trong Thế chiến II và cả trong sự kiện khủng hoảng tên lửa Cuba. Được khánh thành năm 1997 bởi các nhà điêu khắc địa phương, tượng khắc họa Pliyev oai phong trên lưng ngựa trong quân phục, đặt tại quảng trường mang tên ông bên bờ sông Terek. Xung quanh là khu vườn quảng trường thoáng đãng, nơi người dân thường dạo chơi. Với người Ossetia, hình tượng người kỵ sĩ còn cộng hưởng với truyền thống thượng võ và tín ngưỡng Uastyrdzhi. Đây là điểm chụp ảnh và tìm hiểu lịch sử quen thuộc ở trung tâm thành phố.",
    [
        "Tôn vinh Issa Pliyev — tướng Ossetia hai lần Anh hùng Liên Xô.",
        "Tượng kỵ mã dựng năm 1997 bên bờ sông Terek.",
        "Đặt tại quảng trường cùng tên, khu dạo chơi trung tâm.",
    ],
    p("Ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15–20 phút.",
      "Quanh năm; đẹp vào chiều mát bên sông.",
      "Kết hợp đi bộ dọc kè sông Terek qua cầu Gang và đại lộ Mira gần đó."),
    [
        {"title": "Wikipedia (RU) — Плиев, Исса Александрович", "url": "https://ru.wikipedia.org/wiki/Плиев,_Исса_Александрович"},
        {"title": "Культурный туризм — Памятник Иссе Плиеву (Владикавказ)", "url": "https://culttourism.ru/severnaya_osetiya/vladikavkaz/pamyatnik_isse_plievu.html"},
    ],
    ["monument", "history", "military", "vladikavkaz", "pliyev"],
    maps_org("https://yandex.com/maps/org/issa_aleksandrovich_pliyev/188465614915/", "Monument to Issa Pliyev", "Vladikavkaz", 43.0198510, 44.6800822),
))

# 14) Памятник Уастырджи (Алагирское ущелье) ------------------------------------
RECORDS.append(rec(
    "uastyrdzhi-monument-alagir-gorge",
    "Tượng đài Uastyrdzhi bay ra từ vách núi (hẻm Alagir)",
    "Памятник Уастырджи в Алагирском ущелье",
    "Uastyrdzhi Monument in the Alagir Gorge",
    ["monument"],
    42.9590791, 44.2118027,
    "Đường xuyên Kavkaz (Transkam), khoảng km 37, hẻm núi Alagir, huyện Alagirsky, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Bức tượng khổng lồ hình vị thần Uastyrdzhi cưỡi ngựa lao ra từ vách đá, treo lơ lửng trên cao khoảng 22 m phía trên con đường xuyên Kavkaz. Được coi là một trong những tượng kỵ mã lớn nhất thế giới.",
    "Tượng Uastyrdzhi là hình ảnh gây choáng ngợp nhất trên tuyến đường xuyên Kavkaz qua hẻm núi Alagir: một kỵ sĩ khổng lồ cùng con ngựa như vừa phi thẳng ra khỏi vách đá và đóng băng giữa không trung, treo cao chừng 22 mét phía trên mặt đường. Tác phẩm được dựng năm 1995 theo thiết kế của nhà điêu khắc Nikolai Khodov, nặng nhiều tấn và neo vào sườn núi. Uastyrdzhi là vị thần trung tâm trong tín ngưỡng dân gian Ossetia — đấng bảo hộ của đàn ông, chiến binh và lữ khách, thường được đồng nhất với hình tượng Thánh George. Người đi đường có thói quen dừng lại kính lễ và cầu bình an cho hành trình. Đứng dưới bức tượng, du khách vừa kinh ngạc trước quy mô, vừa cảm nhận được chiều sâu tâm linh của vùng đất.",
    [
        "Tượng kỵ sĩ khổng lồ lao ra từ vách đá, cao ~22 m trên mặt đường.",
        "Dựng năm 1995 theo thiết kế của Nikolai Khodov.",
        "Uastyrdzhi — thần bảo hộ đàn ông, chiến binh, lữ khách trong tín ngưỡng Ossetia.",
    ],
    p("Ngoài trời bên đường Transkam, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15–20 phút.",
      "Cuối xuân đến đầu thu; mùa đông đường đèo có thể trơn tuyết.",
      "Có điểm dừng ven đường để ngắm và chụp ảnh. Kết hợp trong hành trình hẻm Alagir, tuyến đi khu Tsey và Mamison."),
    [
        {"title": "Wikipedia (RU) — Памятник Уастырджи", "url": "https://ru.wikipedia.org/wiki/Памятник_Уастырджи"},
        {"title": "Комитет по туризму РСО-Алания — Памятник Уастырджи в Алагирском ущелье", "url": "http://tourism.alania.gov.ru/pages/151"},
    ],
    ["monument", "sculpture", "uastyrdzhi", "alagir", "transkam"],
    maps_text("Памятник Уастырджи", "Алагирское ущелье", "Uastyrdzhi Monument", "Alagir Gorge", 42.9590791, 44.2118027),
))

# 15) Мемориал «Город ангелов» (Беслан) ------------------------------------------
RECORDS.append(rec(
    "beslan-city-of-angels",
    "Đài tưởng niệm Beslan «Thành phố Thiên thần»",
    "Мемориальное кладбище «Город ангелов» (Беслан)",
    "Beslan Memorial «City of Angels»",
    ["monument"],
    43.1914803, 44.5659323,
    "Thành phố Beslan, huyện Pravoberezhny, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Nghĩa trang – đài tưởng niệm dành cho các nạn nhân của thảm kịch trường học Beslan năm 2004, phần lớn là trẻ em. Một nơi tưởng niệm trang nghiêm và xúc động của toàn nước Nga.",
    "«Thành phố Thiên thần» là nghĩa trang tưởng niệm các nạn nhân của vụ bắt giữ con tin tại trường học số 1 ở Beslan đầu tháng 9 năm 2004 — một trong những thảm kịch đau thương nhất lịch sử nước Nga hiện đại, cướp đi sinh mạng hàng trăm người, phần lớn là học sinh. Khu tưởng niệm với những hàng bia mộ trắng và các tác phẩm điêu khắc thiên thần là nơi cộng đồng và du khách đến đặt hoa, tưởng nhớ và cầu nguyện cho hoà bình. Không xa đó, ngôi trường cũ được giữ lại như một đài tưởng niệm nhắc nhở về mất mát. Đây là một địa điểm mang ý nghĩa nhân văn sâu sắc; du khách đến thăm với sự tôn trọng và lặng lẽ. Việc ghé thăm giúp hiểu thêm một chương lịch sử bi thương và tinh thần kiên cường của người dân Bắc Ossetia.",
    [
        "Tưởng niệm các nạn nhân thảm kịch trường học Beslan năm 2004.",
        "Những hàng bia trắng và điêu khắc thiên thần trang nghiêm, xúc động.",
        "Địa điểm tưởng niệm mang ý nghĩa nhân văn của toàn nước Nga.",
    ],
    p("Ngoài trời, mở cửa cho khách viếng ban ngày.",
      "Miễn phí.",
      "Khoảng 30–45 phút.",
      "Quanh năm; đặc biệt trang trọng vào dịp đầu tháng 9.",
      "Đây là nơi tưởng niệm: giữ thái độ trang nghiêm, im lặng, ăn mặc lịch sự; nên hỏi trước khi chụp ảnh. Có thể kết hợp thăm khu trường cũ được bảo tồn."),
    [
        {"title": "Wikipedia (RU) — Мемориал «Город ангелов»", "url": "https://ru.wikipedia.org/wiki/Город_ангелов_(мемориал)"},
        {"title": "Wikipedia (RU) — Террористический акт в Беслане", "url": "https://ru.wikipedia.org/wiki/Террористический_акт_в_Беслане"},
    ],
    ["monument", "memorial", "beslan", "history", "remembrance"],
    maps_text("Мемориал Город ангелов", "Беслан", "City of Angels Memorial", "Beslan", 43.1914803, 44.5659323),
))

# ============================ CẦU (bridge) ============================

# 16) Чугунный мост -------------------------------------------------------------
RECORDS.append(rec(
    "vladikavkaz-chugunny-bridge",
    "Cầu Gang (Chugunny most) qua sông Terek",
    "Чугунный мост через Терек",
    "Chugunny (Cast-Iron) Bridge over the Terek",
    ["bridge"],
    43.0206305, 44.6809078,
    "Bắc qua sông Terek, khu trung tâm, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Cây cầu lịch sử bắc qua dòng Terek chảy xiết ngay giữa trung tâm Vladikavkaz, một trong những cây cầu biểu tượng nối hai bờ phố cổ. Điểm ngắm sông và dạo bộ quen thuộc.",
    "Cầu Gang là một trong những cây cầu lâu đời và mang tính biểu tượng của Vladikavkaz, bắc qua dòng Terek cuộn chảy chia đôi thành phố. Từ thời đế chế, nơi đây đã có cầu nối hai bờ với những kết cấu gang – sắt đặc trưng của thế kỷ 19, và trải qua nhiều lần tu sửa, xây mới nhưng vẫn giữ vai trò huyết mạch cùng cái tên quen thuộc. Đứng trên cầu, du khách có thể ngắm dòng Terek đục ngầu, hùng vĩ, phóng tầm mắt về phía dãy Kavkaz và các công trình ven sông như nhà thờ Hồi giáo Sunni, nhà thờ Armenia. Khu vực quanh cầu với kè đá và hàng cây là chốn dạo bộ ưa thích của người dân. Đây là một điểm dừng ngắn nhưng giàu chất Vladikavkaz cổ điển.",
    [
        "Cầu lịch sử bắc qua dòng Terek giữa trung tâm Vladikavkaz.",
        "Điểm ngắm sông và dãy Kavkaz, gắn với phố cổ hai bờ.",
        "Gần nhà thờ Hồi giáo Sunni và nhà thờ Armenia ven sông.",
    ],
    p("Ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Quanh năm; đẹp vào buổi chiều và khi lên đèn.",
      "Kết hợp đi bộ dọc kè Terek để thăm nhà thờ Hồi giáo Sunni, nhà thờ Armenia và các quảng trường trung tâm."),
    [
        {"title": "Wikipedia (RU) — Владикавказ (мосты через Терек)", "url": "https://ru.wikipedia.org/wiki/Владикавказ"},
        {"title": "OpenStreetMap — Чугунный мост, Владикавказ", "url": "https://www.openstreetmap.org/search?query=Чугунный%20мост%20Владикавказ"},
    ],
    ["bridge", "terek", "heritage", "vladikavkaz", "landmark"],
    maps_text("Чугунный мост", "Владикавказ", "Chugunny Bridge", "Vladikavkaz", 43.0206305, 44.6809078),
))

# ============================ QUẢNG TRƯỜNG / PHỐ (square_street) ============================

# 17) Проспект Мира -------------------------------------------------------------
RECORDS.append(rec(
    "vladikavkaz-prospekt-mira",
    "Đại lộ Prospekt Mira (đại lộ Hoà Bình)",
    "Проспект Мира",
    "Prospekt Mira (Peace Avenue)",
    ["square_street"],
    43.0299562, 44.6805058,
    "Trung tâm lịch sử, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Đại lộ đi bộ trung tâm và đẹp nhất Vladikavkaz, hai bên là dãy nhà cổ thế kỷ 19 – đầu 20 và những chuyến tàu điện lịch sử vẫn chạy qua. Trục dạo bộ, cà phê và văn hoá của thành phố.",
    "Prospekt Mira là linh hồn đô thị của Vladikavkaz — con đại lộ đi bộ rợp bóng cây, được ví như phòng khách ngoài trời của thành phố. Dọc hai bên là những toà nhà mang phong cách chiết trung, tân cổ điển và art nouveau từ cuối thế kỷ 19 đến đầu thế kỷ 20, phản ánh thời kỳ thịnh vượng khi Vladikavkaz là cửa ngõ quan trọng của vùng Kavkaz. Điểm đặc biệt là những toa tàu điện cổ vẫn lăn bánh giữa lòng đại lộ, tạo nên khung cảnh hoài niệm hiếm thấy. Đây là nơi tập trung bảo tàng, quán cà phê, cửa hàng và các đài phun nước, lý tưởng để dạo bộ, ngắm kiến trúc và cảm nhận nhịp sống địa phương. Hầu hết các điểm tham quan trung tâm đều nằm trên hoặc gần đại lộ này.",
    [
        "Đại lộ đi bộ trung tâm, kiến trúc cổ thế kỷ 19 – đầu 20.",
        "Những toa tàu điện lịch sử vẫn chạy dọc đại lộ.",
        "Tập trung bảo tàng, quán cà phê, đài phun nước của thành phố.",
    ],
    p("Ngoài trời, dạo bộ tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 1–2 giờ (tuỳ mức dừng chân).",
      "Quanh năm; dễ chịu nhất vào cuối xuân, mùa hè và đầu thu.",
      "Là trục xuất phát để thăm Bảo tàng Quốc gia, Bảo tàng Mỹ thuật và các nhà hát. Thử cà phê và bánh ngọt địa phương dọc đường."),
    [
        {"title": "Wikipedia (RU) — Проспект Мира (Владикавказ)", "url": "https://ru.wikipedia.org/wiki/Проспект_Мира_(Владикавказ)"},
        {"title": "Комитет по туризму РСО-Алания — Проспект Мира", "url": "http://tourism.alania.gov.ru/"},
    ],
    ["square_street", "avenue", "architecture", "tram", "vladikavkaz"],
    maps_text("Проспект Мира", "Владикавказ", "Prospekt Mira", "Vladikavkaz", 43.0299562, 44.6805058),
))

# 18) Площадь Штыба -------------------------------------------------------------
RECORDS.append(rec(
    "vladikavkaz-shtyb-square",
    "Quảng trường Shtyb",
    "Площадь Штыба",
    "Shtyb Square",
    ["square_street"],
    43.0213865, 44.6819247,
    "Trung tâm, thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Quảng trường xanh nhỏ giữa trung tâm Vladikavkaz, gần bờ sông Terek và đại lộ Mira. Không gian nghỉ chân với cây xanh, ghế đá và đài phun nước.",
    "Quảng trường Shtyb là một trong những khoảng xanh dễ chịu ở trung tâm Vladikavkaz, nằm gần bờ sông Terek và không xa đại lộ Mira. Với những lối đi rợp bóng cây, ghế đá, bồn hoa và đài phun nước, nơi đây là điểm dừng chân quen thuộc của người dân giữa nhịp phố. Quảng trường mang tên một nhân vật lịch sử gắn với thành phố và được bao quanh bởi những công trình cổ, tạo nên khung cảnh hài hoà giữa kiến trúc và cây xanh. Đây là nơi thích hợp để nghỉ ngơi, ngắm phố phường và chụp ảnh trong hành trình khám phá trung tâm. Vị trí thuận tiện giúp du khách dễ dàng kết nối tới cầu Gang, các nhà thờ và bảo tàng lân cận.",
    [
        "Quảng trường xanh giữa trung tâm, gần sông Terek và đại lộ Mira.",
        "Cây xanh, ghế đá, bồn hoa và đài phun nước để nghỉ chân.",
        "Vị trí thuận tiện nối tới cầu Gang, nhà thờ và bảo tàng.",
    ],
    p("Ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15–30 phút.",
      "Quanh năm; đẹp vào cuối xuân đến đầu thu.",
      "Điểm nghỉ chân lý tưởng khi đi bộ khám phá trung tâm; kết hợp với đại lộ Mira và kè sông Terek."),
    [
        {"title": "Wikipedia (RU) — Владикавказ (площади города)", "url": "https://ru.wikipedia.org/wiki/Владикавказ"},
        {"title": "OpenStreetMap — Площадь Штыба, Владикавказ", "url": "https://www.openstreetmap.org/search?query=Площадь%20Штыба%20Владикавказ"},
    ],
    ["square_street", "square", "park", "vladikavkaz", "center"],
    maps_text("Площадь Штыба", "Владикавказ", "Shtyb Square", "Vladikavkaz", 43.0213865, 44.6819247),
))

# ============================ PHÁO ĐÀI / THÁP (fortress) ============================

# 19) Башенный комплекс Цмити -----------------------------------------------------
RECORDS.append(rec(
    "tsymyti-tower-complex",
    "Quần thể tháp cổ Tsymyti (Cmiti)",
    "Средневековый башенный комплекс Цмити (Цымити)",
    "Tsymyti Medieval Tower Complex",
    ["fortress"],
    43.2065090, 44.4150850,
    "Làng Tsymyti, hẻm núi Kurtatinsky, huyện Alagirsky, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Ngôi làng – pháo đài cổ với quần thể tháp canh, tháp ở và nhà mồ (склеп) bằng đá thời trung cổ, nằm trên sườn hẻm núi Kurtatinsky. Một trong những bảo tàng ngoài trời sống động về kiến trúc phòng thủ Ossetia.",
    "Tsymyti là một trong những làng tháp cổ được bảo tồn ấn tượng nhất Bắc Ossetia, treo mình trên sườn dốc của hẻm núi Kurtatinsky. Quần thể gồm các tháp canh (боевые башни) vươn cao, tháp ở kiên cố (ганахи), cùng những nhà mồ đá (склепы) đặc trưng của văn hoá miền núi — tất cả xây bằng đá xếp khan, hoà lẫn vào địa hình. Từ thời trung cổ, đây là lãnh địa của các dòng họ quyền thế, với hệ thống tháp vừa để phòng thủ, vừa thể hiện vị thế gia tộc. Dạo bước giữa những công trình đá phủ rêu, du khách như lạc vào một thế giới cổ xưa, nơi kiến trúc phòng thủ, tín ngưỡng và đời sống thị tộc Ossetia đan xen. Khung cảnh núi non bao quanh khiến Tsymyti trở thành điểm đến giàu chất sử thi và lý tưởng cho nhiếp ảnh.",
    [
        "Làng tháp cổ với tháp canh, tháp ở và nhà mồ đá thời trung cổ.",
        "Nằm trên sườn hẻm núi Kurtatinsky, bảo tàng kiến trúc phòng thủ ngoài trời.",
        "Gắn với lãnh địa của các dòng họ quyền thế Ossetia.",
    ],
    p("Ngoài trời, tham quan tự do ban ngày.",
      "Thường miễn phí (đôi khi có phí nhỏ hoặc phí hướng dẫn tại chỗ).",
      "Khoảng 45–60 phút.",
      "Cuối xuân đến đầu thu; mùa đông đường núi khó đi.",
      "Đi giày bám tốt vì địa hình đá dốc. Nên ghép cùng pháo đài Dzivgis và tu viện Alania trong hành trình hẻm Kurtatinsky."),
    [
        {"title": "Wikipedia (RU) — Цмити", "url": "https://ru.wikipedia.org/wiki/Цмити"},
        {"title": "Комитет по туризму РСО-Алания — башенный комплекс Цмити", "url": "http://tourism.alania.gov.ru/"},
    ],
    ["fortress", "towers", "medieval", "kurtatinsky", "heritage"],
    maps_text("Башенный комплекс Цмити", "Куртатинское ущелье", "Tsymyti Tower Complex", "Kurtatinsky Gorge", 43.2065090, 44.4150850),
))

# ============================ CÔNG VIÊN / VƯỜN (park_garden) ============================

# 20) Детский парк им. Жуковского ------------------------------------------------
RECORDS.append(rec(
    "vladikavkaz-zhukovsky-childrens-park",
    "Công viên Thiếu nhi mang tên Zhukovsky",
    "Детский парк имени Жуковского",
    "Zhukovsky Children's Park",
    ["park_garden"],
    43.0357965, 44.6814969,
    "Thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Công viên cây xanh lâu đời ở trung tâm Vladikavkaz, không gian dạo chơi, trò chơi thiếu nhi và nghỉ ngơi quen thuộc của người dân. Điểm xanh mát giữa lòng thành phố.",
    "Công viên Thiếu nhi mang tên Zhukovsky là một trong những khoảng xanh được yêu thích ở trung tâm Vladikavkaz, gắn bó với nhiều thế hệ cư dân thành phố. Dưới tán cây cổ thụ là những lối đi rợp bóng, khu vui chơi cho trẻ em, sân chơi và các bãi cỏ để nghỉ ngơi. Không gian này mang không khí thư thái, gần gũi, phản ánh nhịp sống đời thường yên bình của Vladikavkaz. Vào những ngày nắng đẹp, công viên nhộn nhịp tiếng cười trẻ nhỏ và bước chân dạo bộ của người lớn tuổi. Đây là điểm dừng chân thư giãn lý tưởng, nhất là với gia đình có trẻ em, và nằm không xa các trục phố chính để dễ dàng kết nối với hành trình tham quan trung tâm.",
    [
        "Công viên cây xanh lâu đời ở trung tâm Vladikavkaz.",
        "Khu vui chơi thiếu nhi, lối dạo bộ rợp bóng cây.",
        "Không gian thư giãn thân thiện, hợp cho gia đình.",
    ],
    p("Ngoài trời, mở cửa tự do ban ngày đến tối.",
      "Miễn phí (một số trò chơi có thu phí).",
      "Khoảng 30–60 phút.",
      "Cuối xuân đến đầu thu.",
      "Điểm nghỉ chân dễ chịu cho gia đình; kết hợp với dạo bộ đại lộ Mira gần đó."),
    [
        {"title": "OpenStreetMap — Детский парк им. Жуковского, Владикавказ", "url": "https://www.openstreetmap.org/search?query=Детский%20парк%20Жуковского%20Владикавказ"},
        {"title": "Комитет по туризму РСО-Алания — парки Владикавказа", "url": "http://tourism.alania.gov.ru/"},
    ],
    ["park_garden", "park", "family", "vladikavkaz", "leisure"],
    maps_text("Детский парк имени Жуковского", "Владикавказ", "Zhukovsky Children's Park", "Vladikavkaz", 43.0357965, 44.6814969),
))

# 21) Дендрарий (Владикавказ, Редант) -------------------------------------------
RECORDS.append(rec(
    "vladikavkaz-arboretum",
    "Vườn Bách thảo (Dendrarium) Vladikavkaz",
    "Дендрарий (Владикавказ, Редант)",
    "Vladikavkaz Arboretum (Dendrarium)",
    ["park_garden"],
    42.9762236, 44.6602951,
    "Khu Redant, ngoại vi phía nam thành phố Vladikavkaz, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Vườn bách thảo với bộ sưu tập cây gỗ và cây bụi đa dạng, nằm ở khu Redant ven sông Terek phía nam Vladikavkaz. Không gian xanh yên tĩnh để dạo bộ và tìm hiểu thực vật vùng Kavkaz.",
    "Vườn Bách thảo Vladikavkaz là một góc xanh tĩnh lặng nằm ở khu Redant, nơi thành phố dần nhường chỗ cho những sườn núi Kavkaz và dòng Terek. Được gây dựng để sưu tập, nghiên cứu và giới thiệu các loài cây gỗ, cây bụi bản địa cùng nhiều loài nhập nội, khu vườn quy tụ bộ sưu tập thực vật phong phú theo mùa. Những lối đi giữa các khóm cây, tán lá đổi màu theo thời tiết và không khí trong lành của vùng chân núi mang lại trải nghiệm thư thái, khác hẳn nhịp phố trung tâm. Đây là điểm đến hợp với người yêu thiên nhiên, nhiếp ảnh và những ai muốn tìm hiểu hệ thực vật đặc trưng của Bắc Kavkaz. Vị trí ven sông Terek cũng mở ra khung cảnh núi non làm nền cho chuyến dạo bộ.",
    [
        "Bộ sưu tập cây gỗ, cây bụi bản địa và nhập nội đa dạng.",
        "Nằm ở khu Redant ven sông Terek, dưới chân núi Kavkaz.",
        "Không gian xanh yên tĩnh cho dạo bộ và tìm hiểu thực vật.",
    ],
    p("Ngoài trời, tham quan ban ngày (nên hỏi trước lịch mở cửa cụ thể).",
      "Thường miễn phí hoặc phí rất nhỏ.",
      "Khoảng 45–60 phút.",
      "Cuối xuân đến mùa thu, khi cây lá rực rỡ nhất.",
      "Mang giày đi bộ thoải mái; nằm ở ngoại vi nên tiện đi ô tô/taxi. Kết hợp với các điểm ven Terek phía nam thành phố."),
    [
        {"title": "OpenStreetMap — Дендрарий, Владикавказ (Редант)", "url": "https://www.openstreetmap.org/search?query=Дендрарий%20Владикавказ%20Редант"},
        {"title": "Комитет по туризму РСО-Алания — природа Владикавказа", "url": "http://tourism.alania.gov.ru/"},
    ],
    ["park_garden", "arboretum", "nature", "botany", "vladikavkaz"],
    maps_text("Дендрарий", "Владикавказ Редант", "Vladikavkaz Arboretum", "Vladikavkaz", 42.9762236, 44.6602951),
))

# ============================ THIÊN NHIÊN / KHÁC (other) ============================

# 22) Дигорское ущелье -----------------------------------------------------------
RECORDS.append(rec(
    "digorsky-gorge",
    "Hẻm núi Digorsky (Digoria)",
    "Дигорское ущелье",
    "Digorsky Gorge (Digoria)",
    ["other"],
    42.8997684, 43.6246609,
    "Huyện Irafsky (Digoria), tây nam Cộng hoà Bắc Ossetia–Alania, Nga",
    "Một trong những hẻm núi hoang sơ và ngoạn mục nhất Bắc Ossetia, ở vùng Digoria phía tây nam, với sông băng, thác nước, đồng cỏ núi cao và làng tháp cổ. Thiên đường cho trekking và ngắm cảnh.",
    "Hẻm núi Digorsky mở ra vùng Digoria — góc tây nam hoang sơ và giàu bản sắc nhất của Bắc Ossetia. Con đường men theo dòng sông Urukh dẫn du khách qua những vách đá dựng đứng, rừng cây, rồi vươn lên các đồng cỏ núi cao (subalpine) rực rỡ hoa dại vào mùa hè. Nơi đây là địa bàn của những sông băng như Karaugom và Taimazi, các thác nước hùng vĩ (trong đó có thác «Ba chị em»), cùng những làng cổ với tháp đá và nhà mồ mang đậm dấu ấn văn hoá miền núi. Digoria còn nổi tiếng với khu nghỉ và các tuyến trekking đưa lữ khách tới gần thế giới băng tuyết vĩnh cửu. Sự kết hợp giữa thiên nhiên nguyên sơ và di sản kiến trúc khiến hẻm Digorsky trở thành điểm đến trong mơ của những người mê núi.",
    [
        "Hẻm núi hoang sơ vùng Digoria với sông băng và thác nước hùng vĩ.",
        "Đồng cỏ núi cao rực rỡ hoa dại vào mùa hè.",
        "Làng cổ với tháp đá và nhà mồ mang đậm văn hoá miền núi.",
    ],
    p("Ngoài trời, tham quan tự do; các tuyến trekking theo ngày.",
      "Miễn phí để vào vùng; có thể phát sinh phí hướng dẫn, lưu trú, phương tiện.",
      "Nửa ngày đến vài ngày tuỳ hành trình.",
      "Cuối xuân đến đầu thu (tháng 6–9) là đẹp và an toàn nhất.",
      "Đường núi hiểm trở, nên đi xe gầm cao hoặc tour địa phương và mang trang bị trekking. Thời tiết đổi nhanh, chuẩn bị áo ấm."),
    [
        {"title": "Wikipedia (RU) — Дигорское ущелье", "url": "https://ru.wikipedia.org/wiki/Дигорское_ущелье"},
        {"title": "Комитет по туризму РСО-Алания — Дигория", "url": "http://tourism.alania.gov.ru/"},
    ],
    ["other", "gorge", "nature", "trekking", "digoria"],
    maps_text("Дигорское ущелье", "Северная Осетия", "Digorsky Gorge", "North Ossetia", 42.8997684, 43.6246609),
))

# 23) Кобанское ущелье -----------------------------------------------------------
RECORDS.append(rec(
    "kobansky-gorge",
    "Hẻm núi Kobansky (làng Koban)",
    "Кобанское ущелье",
    "Kobansky Gorge",
    ["other"],
    42.9147000, 44.4781950,
    "Làng Koban, huyện Prigorodny, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Hẻm núi bên sông Gizeldon nổi tiếng là cái nôi của nền văn hoá khảo cổ Koban thời đồ đồng. Cảnh quan vách đá, thác nước và làng cổ giàu di sản.",
    "Hẻm núi Kobansky, bao quanh làng Koban bên dòng sông Gizeldon, có ý nghĩa đặc biệt với khảo cổ học thế giới: chính tại đây, vào thế kỷ 19, người ta phát hiện những di vật đồng thau tinh xảo, đặt tên cho cả một nền văn hoá — «văn hoá Koban» thời đại đồ đồng muộn và đầu đồ sắt, lan toả khắp vùng trung Kavkaz. Ngày nay, hẻm núi hấp dẫn du khách bằng cảnh quan vách đá dựng đứng, dòng suối trong, những thác nước và ngôi làng cổ với kiến trúc đá đặc trưng. Đi giữa khung cảnh này, người ta vừa chiêm ngưỡng thiên nhiên vừa cảm nhận bề dày lịch sử hàng nghìn năm của vùng đất. Kobansky là điểm đến kết hợp thú vị giữa vẻ đẹp núi non và câu chuyện khảo cổ hiếm có.",
    [
        "Cái nôi của nền văn hoá khảo cổ Koban thời đồ đồng.",
        "Cảnh quan vách đá, thác nước bên sông Gizeldon.",
        "Làng cổ Koban với kiến trúc đá đặc trưng miền núi.",
    ],
    p("Ngoài trời, tham quan tự do ban ngày.",
      "Miễn phí (có thể phát sinh phí phương tiện, hướng dẫn).",
      "Khoảng nửa ngày.",
      "Cuối xuân đến đầu thu.",
      "Đường núi quanh co, nên đi xe gầm cao hoặc tour. Kết hợp với hẻm Karmadon và làng Dargavs gần đó."),
    [
        {"title": "Wikipedia (RU) — Кобанская культура", "url": "https://ru.wikipedia.org/wiki/Кобанская_культура"},
        {"title": "Wikipedia (RU) — Кобан (село)", "url": "https://ru.wikipedia.org/wiki/Кобан_(село)"},
    ],
    ["other", "gorge", "nature", "archaeology", "koban-culture"],
    maps_text("Кобанское ущелье", "Северная Осетия", "Kobansky Gorge", "North Ossetia", 42.9147000, 44.4781950),
))

# 24) Кармадонское ущелье --------------------------------------------------------
RECORDS.append(rec(
    "karmadon-gorge",
    "Hẻm núi Karmadon",
    "Кармадонское ущелье",
    "Karmadon Gorge",
    ["other"],
    42.8399203, 44.5058513,
    "Làng Karmadon, huyện Prigorodny, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Hẻm núi bên dòng Genaldon dưới chân đỉnh Kazbek, gắn với suối khoáng nóng và thảm kịch sông băng Kolka năm 2002. Cảnh quan hùng vĩ và đầy sức nặng lịch sử.",
    "Hẻm núi Karmadon nằm bên dòng Genaldon, dưới bóng những đỉnh núi cao vùng Kazbek, nổi tiếng cả vì vẻ đẹp lẫn ký ức bi thương. Khu vực này từ lâu được biết đến với các suối khoáng nóng Karmadon từng là nơi nghỉ dưỡng. Tháng 9 năm 2002, sông băng Kolka bất ngờ sạt lở, tạo thành dòng bùn – băng – đá khổng lồ tràn xuống hẻm núi, vùi lấp một phần thung lũng và cướp đi nhiều sinh mạng, trong đó có đoàn làm phim của đạo diễn Sergei Bodrov. Ngày nay, hẻm Karmadon vừa là điểm ngắm cảnh núi non hùng vĩ, vừa là nơi tưởng niệm, nhắc nhở về sức mạnh khôn lường của thiên nhiên. Du khách đến đây để chiêm ngưỡng khung cảnh, tìm hiểu câu chuyện Kolka và cảm nhận sự giao thoa giữa cái đẹp và sự khắc nghiệt của vùng cao Kavkaz.",
    [
        "Hẻm núi bên sông Genaldon, dưới chân vùng đỉnh Kazbek.",
        "Gắn với suối khoáng nóng Karmadon và thảm kịch sông băng Kolka (2002).",
        "Cảnh quan hùng vĩ kết hợp ý nghĩa tưởng niệm.",
    ],
    p("Ngoài trời, tham quan tự do ban ngày.",
      "Miễn phí (có thể phát sinh phí phương tiện, hướng dẫn).",
      "Khoảng nửa ngày.",
      "Cuối xuân đến đầu thu; tránh thời tiết xấu vì địa hình nhạy cảm.",
      "Đi cùng hướng dẫn viên/tour địa phương để an toàn và hiểu rõ lịch sử Kolka. Kết hợp với Dargavs và hẻm Kobansky."),
    [
        {"title": "Wikipedia (RU) — Кармадонское ущелье", "url": "https://ru.wikipedia.org/wiki/Кармадонское_ущелье"},
        {"title": "Wikipedia (RU) — Сход ледника Колка (2002)", "url": "https://ru.wikipedia.org/wiki/Сход_ледника_Колка"},
    ],
    ["other", "gorge", "nature", "kolka", "memorial"],
    maps_text("Кармадонское ущелье", "Северная Осетия", "Karmadon Gorge", "North Ossetia", 42.8399203, 44.5058513),
))

# 25) Дарьяльское ущелье (Верхний Ларс) -----------------------------------------
RECORDS.append(rec(
    "daryal-gorge",
    "Hẻm núi Daryal (cửa hẻm Verkhny Lars)",
    "Дарьяльское ущелье (Верхний Ларс)",
    "Daryal Gorge (Verkhny Lars)",
    ["other"],
    42.7717060, 44.6305890,
    "Gần làng Verkhny Lars, dọc sông Terek trên tuyến Quân lộ Gruzia, giáp biên giới Nga–Gruzia, Cộng hoà Bắc Ossetia–Alania, Nga",
    "Hẻm núi sâu và hiểm trở nơi sông Terek xẻ đôi dãy Kavkaz, nằm trên tuyến Quân lộ Gruzia huyền thoại ngay cửa ngõ biên giới. Cảnh quan vách đá dựng đứng từng làm say lòng Pushkin và Lermontov.",
    "Hẻm núi Daryal là một trong những hẻm núi nổi tiếng nhất vùng Kavkaz — nơi dòng Terek cắt xuyên qua khối núi tạo thành khe vực sâu hun hút giữa những vách đá granite dựng đứng. Từ xa xưa, đây là cửa ải chiến lược trên tuyến Quân lộ Gruzia nối Nga với vùng Ngoại Kavkaz, được nhắc đến trong sử sách và truyền thuyết cổ. Vẻ hoang sơ, dữ dội của hẻm núi từng khơi nguồn cảm hứng cho các đại thi hào Nga như Pushkin và Lermontov. Phía Nga của hẻm nằm gần làng Verkhny Lars, ngay cửa khẩu biên giới Nga–Gruzia, nơi du khách có thể ngắm dòng Terek gầm réo dưới chân những sườn núi cao. Đây là điểm dừng đầy ấn tượng cho ai đi dọc tuyến đường lịch sử này, cảm nhận sự giao thoa giữa thiên nhiên hùng vĩ và bề dày văn hoá.",
    [
        "Hẻm núi nơi sông Terek xẻ đôi dãy Kavkaz, vách đá dựng đứng.",
        "Nằm trên Quân lộ Gruzia lịch sử, ngay cửa ngõ biên giới Nga–Gruzia.",
        "Nguồn cảm hứng cho Pushkin và Lermontov.",
    ],
    p("Ngoài trời, ngắm cảnh dọc đường; khu vực gần cửa khẩu biên giới.",
      "Miễn phí để ngắm cảnh; qua biên giới cần giấy tờ hợp lệ.",
      "Khoảng 30–60 phút dừng chân.",
      "Cuối xuân đến đầu thu; mùa đông đường đèo có thể đóng do tuyết.",
      "Đây là khu vực sát biên giới: tuân thủ quy định, mang theo giấy tờ tuỳ thân. Kết hợp trong hành trình dọc Quân lộ Gruzia từ Vladikavkaz."),
    [
        {"title": "Wikipedia (RU) — Дарьяльское ущелье", "url": "https://ru.wikipedia.org/wiki/Дарьяльское_ущелье"},
        {"title": "Wikipedia (RU) — Верхний Ларс", "url": "https://ru.wikipedia.org/wiki/Верхний_Ларс"},
    ],
    ["other", "gorge", "terek", "nature", "georgian-military-road"],
    maps_text("Дарьяльское ущелье", "Верхний Ларс", "Daryal Gorge", "Verkhny Lars", 42.7717060, 44.6305890),
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
