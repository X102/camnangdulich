# -*- coding: utf-8 -*-
"""_add_places_sakha_20260729_010000.py — VÙNG: Cộng hoà Sakha (Yakutia) (Республика Саха)
(lần chạy tự động, nội dung tiếng Việt nguyên gốc, có ghi nguồn).

Bối cảnh: sakha.json hiện có 7 địa điểm (Ленские столбы, Царство вечной мерзлоты, Оймякон,
Музей мамонта, Тукулан/Саамыс Кумага, Старый город, Музей-заповедник «Дружба» в Соттинцах).
Bổ sung 24 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU của Yakutia, đa dạng loại hình →
đưa vùng lên 31. TRÁNH trùng 7 điểm trên (KHÔNG thêm lại Ленские столбы, Соттинцы «Дружба»,
Оймякон, Музей мамонта, Старый город...).

Phân bố loại hình (24 bản ghi mới):
- museum (8): Ярославского (краеведческий), Национальный художественный, Музей хомуса,
  Сокровищница РС(Я) (алмазы/золото), Музей археологии и этнографии СВФУ, Литературный музей
  Ойунского, Музей истории изучения вечной мерзлоты (Институт мерзлотоведения), Черкёхский
  музей «Якутская политическая ссылка» (под открытым небом, Таттинский улус).
- theatre (3): театр оперы и балета, Саха академический театр им. Ойунского, Русский
  драматический театр им. Пушкина.
- church (2): Градоякутский Преображенский собор, Градоякутский Никольский храм.
- monument (2): памятник П.И. Бекетову (основатель Якутска), мемориальный комплекс «Победа».
- square_street (1): площадь В.И. Ленина.
- park_garden (2): архитектурно-этнографический комплекс «Ысыах Туймаады» (Ус Хатын),
  Ботанический сад ЯНЦ СО РАН.
- other (6): Государственный цирк РС(Я), ледник Булуус, водопады Курулуур, Синские столбы,
  город Верхоянск (полюс холода), кимберлитовая трубка «Мир» (г. Мирный).

TOẠ ĐỘ — xác minh chéo (2GIS og:image center=LON,LAT + «Маршрут» points; ru.wikipedia infobox;
tonkosti.ru; 2GIS geo, 2026-07). Phạm vi Yakutia lat ~55–74, lon ~105–163 (TP Yakutsk ~62.03,
129.73) — tất cả toạ độ trong phạm vi, KHÔNG đảo lat/lon:
  Ярославского 62.030511,129.746876 (2gis firm); Нац. худ. музей 62.025482,129.73144 (2gis firm);
  Музей хомуса 62.0332,129.718105 (2gis firm); Сокровищница РС(Я) 62.025689,129.735543 (2gis firm);
  Музей археологии и этнографии СВФУ 62.017119,129.704638 (2gis firm); Литературный музей Ойунского
  62.026982,129.721583 (2gis firm); Музей вечной мерзлоты (Институт мерзлотоведения) 62.010932,
  129.661693 (2gis firm); театр оперы и балета 62.023314,129.719351 (2gis firm); Саха ак. театр
  62.033288,129.742247 (2gis firm); Русский драмтеатр им. Пушкина 62.028576,129.735134 (2gis firm);
  Преображенский собор 62.023918,129.736461 (2gis firm); Никольский храм 62.030137,129.7118 (2gis firm);
  памятник Бекетову 62.023527,129.738768 (2gis geo); площадь Ленина 62.027577,129.730589 (2gis geo);
  площадь Победы 62.040399,129.756242 (2gis geo); цирк РС(Я) 62.032418,129.724162 (2gis firm);
  Ысыах Туймаады/Ус Хатын 62.196833,129.782883 (2gis firm); ледник Булуус 61.337926,129.070526
  (esosedi/pikabu); водопады Курулуур 61.408438,129.557909 (2gis geo); Синские столбы 61.38284,
  126.656618 (tonkosti.ru); Верхоянск 67.55,133.383 (ru.wiki 67°33′N 133°23′E); трубка «Мир»
  62.528889,113.992778 (ru.wiki 62°31′44″N 113°59′34″E); Черкёхский музей 62.187298,133.244013
  (culture.ru/tonkosti); Ботанический сад ЯНЦ СО РАН 62.01868,129.606299 (2gis firm).

GHI CHÚ — đã BỎ QUA / KHÔNG thêm:
- Музей музыки и фольклора им. Решетниковой: cùng toà nhà và cùng toạ độ (ул. Кирова 31) với Музей
  хомуса → tránh trùng toạ độ.
- Гора Кисилях (Верхоянский р-н, священная гора «каменные люди»): NHIỀU đối tượng cùng tên ở các
  huyện khác nhau (Верхоянский, Нижнеколымский...), KHÔNG tìm được toạ độ chính xác đáng tin cậy cho
  ĐÚNG ngọn núi thiêng ở Верхоянский → BỎ để tránh bịa toạ độ.
- Усть-Ленский/Олёкминский заповедник, Ленская дельта, Тикси: không lấy được toạ độ điểm tham quan
  cụ thể đáng tin → BỎ trong lần này.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_sakha_20260729_010000.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "sakha"
REGION_NAME_VI = "Cộng hoà Sakha (Yakutia)"
FD = "Vùng Viễn Đông"


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

# 1) Якутский музей истории и культуры народов Севера им. Е.М. Ярославского ----------
RECORDS.append(rec(
    "yaroslavsky-museum-yakutsk",
    "Bảo tàng Lịch sử và Văn hoá các dân tộc phương Bắc mang tên Yaroslavsky (Ya-rô-xláp-xki)",
    "Якутский государственный объединённый музей истории и культуры народов Севера им. Е.М. Ярославского",
    "Yaroslavsky Museum of History and Culture of the Peoples of the North",
    ["museum"],
    62.030511, 129.746876,
    "Đại lộ Lenina 5/2, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Bảo tàng lâu đời và lớn nhất Yakutia, thành lập năm 1891, là 'kho ký ức' của cả vùng Viễn Đông băng giá. Nơi trưng bày toàn cảnh thiên nhiên, khảo cổ, dân tộc học và lịch sử của người Sakha cùng các dân tộc phương Bắc.",
    "Bảo tàng mang tên Yaroslavsky là bảo tàng lâu đời nhất Cộng hoà Sakha, khởi lập từ năm 1891 và ngày nay là bảo tàng tổng hợp lớn nhất vùng, với hàng trăm nghìn hiện vật. Bộ sưu tập trải rộng từ mẫu vật thiên nhiên, hoá thạch, khảo cổ, đến trang phục, đồ dùng, tín ngưỡng shaman và nghệ thuật dân gian của người Yakut (Sakha), Evenk, Even, Yukagir, Dolgan cùng các tộc người phương Bắc khác. Du khách có thể tìm hiểu về đời sống du mục, chăn tuần lộc, nghề săn bắt, tục thờ trời (Aiyy), lễ hội Ysyakh mùa hè, cũng như lịch sử người Nga khai hoang, thời kỳ lưu đày chính trị và thế kỷ 20 đầy biến động. Bảo tàng còn nổi tiếng với những bộ xương động vật cổ đại và các hiện vật gắn với khí hậu khắc nghiệt nhất hành tinh. Đây là điểm khởi đầu lý tưởng để hiểu bức tranh toàn cảnh về vùng đất rộng lớn, lạnh giá và giàu bản sắc bậc nhất nước Nga.",
    [
        "Bảo tàng lâu đời và lớn nhất Yakutia, thành lập từ năm 1891.",
        "Sưu tập phong phú về thiên nhiên, khảo cổ và dân tộc học các dân tộc phương Bắc.",
        "Nơi hiểu tổng quan về người Sakha, tín ngưỡng shaman và lịch sử khai hoang vùng cực.",
    ],
    p("Thường mở Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa ở mức phải chăng (vài trăm rúp); ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm; hợp cả những ngày lạnh giá ngoài trời.",
      "Nằm ngay trung tâm, gần đại lộ Lenina; thuyết minh chủ yếu bằng tiếng Nga, nên đi kèm hướng dẫn."),
    [
        {"title": "Culture.ru — Музей им. Е.М. Ярославского", "url": "https://www.culture.ru/institutes/10224/yakutskii-gosudarstvennyi-obedinennyi-muzei-istorii-i-kultury-narodov-severa-im-em-yaroslavskogo"},
        {"title": "Trang chính thức — yakutmuseum.ru", "url": "http://yakutmuseum.ru/"},
    ],
    ["museum", "history", "local-lore", "yakutsk", "ethnography", "sakha"],
    maps_text("Якутский музей истории и культуры народов Севера им. Е.М. Ярославского", "Якутск", "Yaroslavsky Museum of History and Culture", "Yakutsk", 62.030511, 129.746876),
    official_site="http://yakutmuseum.ru/",
))

# 2) Национальный художественный музей Республики Саха (Якутия) ----------------------
RECORDS.append(rec(
    "national-art-museum-sakha",
    "Bảo tàng Nghệ thuật Quốc gia Cộng hoà Sakha (Yakutia)",
    "Национальный художественный музей Республики Саха (Якутия)",
    "National Art Museum of the Republic of Sakha (Yakutia)",
    ["museum"],
    62.025482, 129.73144,
    "Phố Kirova 9, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Bảo tàng nghệ thuật lớn nhất vùng đông bắc Siberia, lưu giữ sưu tập hội hoạ Nga, nghệ thuật châu Âu và đặc biệt là mỹ thuật, điêu khắc ngà voi ma mút của các nghệ sĩ Yakut. Một điểm đến giàu chất bản địa giữa lòng Yakutsk.",
    "Bảo tàng Nghệ thuật Quốc gia Cộng hoà Sakha là kho tàng mỹ thuật lớn và quan trọng nhất ở vùng đông bắc nước Nga. Bộ sưu tập trải dài từ tranh biểu tượng (icon) cổ, hội hoạ và điêu khắc Nga thế kỷ 18–20, một số tác phẩm nghệ thuật Tây Âu và phương Đông, đến mảng đặc sắc nhất là nghệ thuật tạo hình của chính người Sakha. Tại đây, du khách được chiêm ngưỡng tranh phong cảnh Bắc Cực, chân dung, các tác phẩm phản ánh sử thi Olonkho (di sản truyền khẩu được UNESCO ghi danh), cùng nghệ thuật chạm khắc trứ danh trên ngà voi ma mút và xương – một nghề thủ công tinh xảo gắn liền với vùng đất băng vĩnh cửu. Bảo tàng thường xuyên tổ chức triển lãm chuyên đề, sự kiện và chương trình giáo dục, trở thành trung tâm đời sống văn hoá của thành phố. Ghé thăm nơi đây, người xem không chỉ thưởng lãm hội hoạ mà còn cảm nhận được tâm hồn, thiên nhiên và huyền thoại của xứ sở lạnh giá phương Bắc.",
    [
        "Bảo tàng nghệ thuật lớn nhất vùng đông bắc Siberia và Viễn Đông.",
        "Sưu tập đặc sắc về chạm khắc ngà voi ma mút và mỹ thuật của người Sakha.",
        "Nơi cảm nhận sử thi Olonkho và tâm hồn nghệ thuật xứ băng giá.",
    ],
    p("Thứ Tư 12:00–20:00; các ngày còn lại khoảng 11:00–19:00; nên kiểm tra lịch trước.",
      "Vé vào cửa ở mức phải chăng; ưu đãi cho học sinh, sinh viên và người cao tuổi.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; lý tưởng cho ngày thời tiết khắc nghiệt.",
      "Nằm ở trung tâm gần phố Kirova; kết hợp tham quan các bảo tàng lân cận trong ngày."),
    [
        {"title": "Culture.ru — Национальный художественный музей РС(Я)", "url": "https://www.culture.ru/institutes/10288/nacionalnyi-khudozhestvennyi-muzei-respubliki-sakha-yakutiya"},
        {"title": "Trang chính thức — sakhamuseum.ru", "url": "http://www.sakhamuseum.ru/"},
    ],
    ["museum", "art", "mammoth-ivory", "yakutsk", "olonkho", "sakha"],
    maps_text("Национальный художественный музей Республики Саха (Якутия)", "Якутск", "National Art Museum of Sakha", "Yakutsk", 62.025482, 129.73144),
    official_site="http://www.sakhamuseum.ru/",
))

# 3) Музей и центр хомуса народов мира -----------------------------------------------
RECORDS.append(rec(
    "khomus-museum-yakutsk",
    "Bảo tàng và Trung tâm đàn môi Khomus các dân tộc thế giới (Khô-mút)",
    "Музей и центр хомуса народов мира",
    "Museum and Centre of the Khomus (Jew's Harp) of the Peoples of the World",
    ["museum"],
    62.0332, 129.718105,
    "Phố Kirova 31 (tầng 3), thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Bảo tàng đàn môi duy nhất trên thế giới, lưu giữ hơn 1.700 cây khomus và các loại đàn môi tương tự của gần 60 dân tộc khắp năm châu. Nơi tôn vinh nhạc cụ dân gian biểu tượng của người Sakha.",
    "Bảo tàng và Trung tâm đàn môi Khomus là một địa chỉ độc nhất vô nhị: bảo tàng duy nhất trên thế giới dành riêng cho khomus – loại đàn môi (jew's harp) mà người Yakut coi là nhạc cụ dân tộc thiêng liêng. Bộ sưu tập gồm hơn 1.700 hiện vật, tập hợp khomus và các nhạc cụ đàn môi tương tự của gần 60 dân tộc từ khắp thế giới, cho thấy sự phổ biến kỳ diệu của loại nhạc cụ nhỏ bé này. Với người Sakha, tiếng khomus rung ngân được ví như hơi thở của thiên nhiên, tiếng gió, tiếng nước và giọng nói của tổ tiên; nghệ thuật chơi khomus gắn bó mật thiết với tín ngưỡng và tâm linh vùng cực. Tại bảo tàng, du khách không chỉ ngắm những cây đàn quý bằng kim loại, gỗ, xương chạm khắc tinh xảo mà còn được nghe trình diễn, tìm hiểu kỹ thuật diễn tấu và ý nghĩa văn hoá sâu xa của khomus. Đây là điểm đến nhỏ nhưng đầy chất thơ, mở ra một thế giới âm thanh và bản sắc rất riêng của Yakutia.",
    [
        "Bảo tàng đàn môi (khomus/jew's harp) DUY NHẤT trên thế giới.",
        "Hơn 1.700 cây khomus và nhạc cụ tương tự của gần 60 dân tộc năm châu.",
        "Được nghe trình diễn và hiểu ý nghĩa tâm linh của nhạc cụ biểu tượng Sakha.",
    ],
    p("Thứ Hai–Thứ Sáu khoảng 9:00–18:00, Thứ Bảy 10:00–17:00; Chủ nhật nghỉ (nên gọi trước).",
      "Vé vào cửa thấp; nên đặt trước nếu muốn xem trình diễn khomus.",
      "Khoảng 45–60 phút.",
      "Quanh năm.",
      "Bảo tàng ở tầng 3 phố Kirova 31; hỏi trước về suất biểu diễn và hướng dẫn tiếng Anh."),
    [
        {"title": "Culture.ru — Музей и Центр хомуса народов мира", "url": "https://www.culture.ru/institutes/27863/muzei-i-centr-khomusa-narodov-mira"},
        {"title": "Trang chính thức — ilkhomus.com", "url": "http://rus.ilkhomus.com/"},
    ],
    ["museum", "khomus", "jews-harp", "music", "yakutsk", "sakha"],
    maps_text("Музей и центр хомуса народов мира", "Якутск", "Khomus Jew's Harp Museum", "Yakutsk", 62.0332, 129.718105),
    official_site="http://rus.ilkhomus.com/",
))

# 4) Сокровищница Республики Саха (Якутия) -------------------------------------------
RECORDS.append(rec(
    "treasury-of-sakha",
    "Kho báu Cộng hoà Sakha (Yakutia) (Xô-crô-vi-sni-tsa)",
    "Сокровищница Республики Саха (Якутия)",
    "Treasury of the Republic of Sakha (Yakutia)",
    ["museum"],
    62.025689, 129.735543,
    "Phố Kirova 12 (tầng 3), thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Bảo tàng trưng bày kim cương, vàng và đá quý của 'xứ sở kim cương' Yakutia – vùng khai thác kim cương lớn nhất nước Nga. Nơi chiêm ngưỡng những viên đá thô, trang sức và cả các cục vàng tự nhiên độc đáo.",
    "Kho báu Cộng hoà Sakha là một bảo tàng đặc biệt, phản ánh nguồn tài nguyên đã làm nên tên tuổi của Yakutia trên bản đồ thế giới: kim cương và vàng. Cộng hoà Sakha là vùng khai thác kim cương hàng đầu nước Nga, và tại đây, du khách được tận mắt chiêm ngưỡng những viên kim cương thô lấp lánh, các sản phẩm chế tác, trang sức tinh xảo bằng kim cương, vàng, bạch kim cùng nhiều loại đá bán quý của vùng. Trưng bày còn có những cục vàng tự nhiên (samorodok) mang hình dáng kỳ lạ, các mẫu quặng, cùng câu chuyện về ngành công nghiệp kim cương – từ việc phát hiện các ống kimberlite giữa rừng taiga đến kỹ nghệ cắt mài hiện đại. Không gian trưng bày sang trọng, an ninh nghiêm ngặt, mang lại cảm giác như bước vào một 'hầm châu báu' thực thụ. Đây là điểm đến hấp dẫn để hiểu vì sao Yakutia được mệnh danh là 'xứ sở kim cương' và tài nguyên ấy gắn bó thế nào với đời sống, kinh tế của vùng.",
    [
        "Trưng bày kim cương, vàng và đá quý của 'xứ sở kim cương' Yakutia.",
        "Chiêm ngưỡng kim cương thô, trang sức tinh xảo và các cục vàng tự nhiên hiếm.",
        "Hiểu về ngành công nghiệp kim cương gắn với các ống kimberlite của Sakha.",
    ],
    p("Thường mở cửa hằng ngày (trừ ngày nghỉ) khoảng 10:00–18:00; nên kiểm tra trước.",
      "Vé vào cửa ở mức trung bình; có thể yêu cầu tham quan theo suất/hướng dẫn.",
      "Khoảng 45–60 phút.",
      "Quanh năm.",
      "An ninh chặt, thường không cho chụp ảnh tự do bên trong; hỏi trước quy định và suất tham quan."),
    [
        {"title": "2GIS — Сокровищница Республики Саха (Якутия)", "url": "https://2gis.ru/yakutsk/firm/7037402698760976"},
        {"title": "Wikipedia (EN) — Treasury of the Republic of Sakha", "url": "https://en.wikipedia.org/wiki/Special:Search?search=Treasury%20of%20the%20Republic%20of%20Sakha"},
    ],
    ["museum", "diamonds", "gold", "gemstones", "yakutsk", "sakha"],
    maps_text("Сокровищница Республики Саха (Якутия)", "Якутск", "Treasury of the Republic of Sakha", "Yakutsk", 62.025689, 129.735543),
))

# 5) Музей археологии и этнографии СВФУ им. М.К. Аммосова ----------------------------
RECORDS.append(rec(
    "archaeology-ethnography-museum-svfu",
    "Bảo tàng Khảo cổ và Dân tộc học Đại học Liên bang Đông Bắc SVFU",
    "Музей археологии и этнографии СВФУ им. М.К. Аммосова",
    "Museum of Archaeology and Ethnography of the North-Eastern Federal University",
    ["museum"],
    62.017119, 129.704638,
    "Phố Kulakovskogo 48 (khu KFEN, Đại học Liên bang Đông Bắc), thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Bảo tàng học thuật của Đại học Liên bang Đông Bắc, trưng bày các phát hiện khảo cổ và hiện vật dân tộc học về quá trình cư trú lâu đời của con người ở vùng cực đông bắc châu Á.",
    "Bảo tàng Khảo cổ và Dân tộc học thuộc Đại học Liên bang Đông Bắc mang tên Ammosov (SVFU) là một điểm đến giàu tính học thuật nhưng vẫn hấp dẫn du khách phổ thông. Tại đây trưng bày các hiện vật khai quật từ nhiều di chỉ khảo cổ khắp Yakutia, minh chứng cho việc con người đã sinh sống ở vùng đất băng giá này từ hàng chục nghìn năm trước – một trong những nơi khắc nghiệt nhất mà loài người từng chinh phục. Bộ sưu tập gồm công cụ đá, đồ gốm, vũ khí, đồ trang sức cổ, cùng các hiện vật dân tộc học phản ánh đời sống, tín ngưỡng, trang phục và phong tục của người Yakut, Evenk, Even, Yukagir và các tộc người phương Bắc. Bảo tàng cũng là nơi lưu giữ nhiều tư liệu nghiên cứu quý về khảo cổ vùng Bắc Cực. Với những ai yêu thích lịch sử sâu xa và muốn hiểu con đường di cư, thích nghi của con người nơi cực lạnh, đây là một điểm dừng đầy ý nghĩa, thường gắn với các chương trình tham quan có hướng dẫn của trường đại học.",
    [
        "Bảo tàng khảo cổ - dân tộc học của Đại học Liên bang Đông Bắc SVFU.",
        "Hiện vật minh chứng con người cư trú ở vùng cực từ hàng chục nghìn năm trước.",
        "Sưu tập công cụ, gốm và đồ dùng của người Yakut, Evenk, Even, Yukagir.",
    ],
    p("Mở cửa theo lịch của trường đại học, thường ngày làm việc; nên đặt trước.",
      "Vé vào cửa thấp; ưu tiên đi theo nhóm có hướng dẫn.",
      "Khoảng 45–60 phút.",
      "Quanh năm.",
      "Nằm trong khuôn viên SVFU (phố Kulakovskogo 48); liên hệ trước để sắp xếp tham quan."),
    [
        {"title": "2GIS — Музей археологии и этнографии СВФУ", "url": "https://2gis.ru/yakutsk/firm/7037402698778833"},
        {"title": "Trang trường — s-vfu.ru (музеи)", "url": "https://www.s-vfu.ru/universitet/rukovodstvo-i-struktura/vspomogatelnye-podrazdeleniya/muzei/etnomus/"},
    ],
    ["museum", "archaeology", "ethnography", "university", "yakutsk", "sakha"],
    maps_text("Музей археологии и этнографии СВФУ", "Якутск", "Museum of Archaeology and Ethnography NEFU", "Yakutsk", 62.017119, 129.704638),
))

# 6) Якутский государственный литературный музей им. П.А. Ойунского -------------------
RECORDS.append(rec(
    "oyunsky-literary-museum-yakutsk",
    "Bảo tàng Văn học Quốc gia Yakutsk mang tên Oyunsky (Ôi-un-xki)",
    "Якутский государственный литературный музей им. П.А. Ойунского",
    "Oyunsky State Literary Museum of Yakutia",
    ["museum"],
    62.026982, 129.721583,
    "Phố Oktyabrskaya 10, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Bảo tàng văn học dành riêng cho di sản của Platon Oyunsky – nhà văn, nhà thơ khai sáng nền văn học Yakut hiện đại và người ghi chép sử thi Olonkho. Nơi tôn vinh tiếng nói và văn chương của dân tộc Sakha.",
    "Bảo tàng Văn học Quốc gia mang tên Platon Oyunsky là trung tâm gìn giữ và tôn vinh di sản văn học của người Sakha. Platon Alekseevich Oyunsky (1893–1939) là một trong những người sáng lập nền văn học Yakut hiện đại, nhà thơ, nhà văn, nhà hoạt động văn hoá và là người có công lớn trong việc sưu tầm, ghi chép sử thi anh hùng Olonkho – kiệt tác truyền khẩu đã được UNESCO công nhận là Kiệt tác Di sản truyền khẩu và phi vật thể của nhân loại. Bảo tàng trưng bày bản thảo, thư từ, đồ dùng cá nhân, hình ảnh và tư liệu về cuộc đời cùng sự nghiệp của Oyunsky và nhiều nhà văn Yakut khác, dẫn dắt người xem qua hành trình hình thành nền văn học viết của một dân tộc phương Bắc. Không gian ấm cúng, giàu chất thơ, đồng thời thường tổ chức các buổi đọc thơ, gặp gỡ văn chương và chương trình giáo dục. Đây là điểm đến ý nghĩa cho ai muốn chạm tới chiều sâu tâm hồn, ngôn ngữ và huyền thoại của xứ Sakha.",
    [
        "Dành riêng cho Platon Oyunsky – người khai sáng văn học Yakut hiện đại.",
        "Gắn với sử thi Olonkho, Kiệt tác Di sản phi vật thể của nhân loại (UNESCO).",
        "Trưng bày bản thảo, thư từ và tư liệu quý về văn chương Sakha.",
    ],
    p("Thường mở Thứ Ba–Chủ nhật khoảng 9:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa thấp; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 45–60 phút.",
      "Quanh năm.",
      "Thuyết minh chủ yếu bằng tiếng Nga/Yakut; nên đi kèm hướng dẫn để hiểu sâu về Olonkho."),
    [
        {"title": "2GIS — Литературный музей им. П.А. Ойунского", "url": "https://2gis.ru/yakutsk/firm/7037402698748499"},
        {"title": "Trang chính thức — sakhalit.com", "url": "http://sakhalit.com/"},
    ],
    ["museum", "literature", "olonkho", "oyunsky", "yakutsk", "sakha"],
    maps_text("Якутский государственный литературный музей им. П.А. Ойунского", "Якутск", "Oyunsky Literary Museum", "Yakutsk", 62.026982, 129.721583),
    official_site="http://sakhalit.com/",
))

# 7) Институт мерзлотоведения — Музей истории изучения вечной мерзлоты ----------------
RECORDS.append(rec(
    "permafrost-institute-museum-yakutsk",
    "Bảo tàng Lịch sử nghiên cứu Băng vĩnh cửu (Viện Băng vĩnh cửu học)",
    "Институт мерзлотоведения СО РАН, Музей истории изучения вечной мерзлоты",
    "Permafrost Institute — Museum of the History of Permafrost Studies",
    ["museum"],
    62.010932, 129.661693,
    "Phố Merzlotnaya 36, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Bảo tàng của Viện Băng vĩnh cửu học SB RAS, nơi kể câu chuyện khoa học về hiện tượng đất đóng băng vĩnh cửu bao phủ Yakutia. Đặc biệt có hầm ngầm trong lòng đất băng vĩnh cửu để tham quan.",
    "Đặt tại Viện Băng vĩnh cửu học thuộc Phân viện Siberia của Viện Hàn lâm Khoa học Nga (một trong những trung tâm nghiên cứu băng vĩnh cửu hàng đầu thế giới), bảo tàng này kể câu chuyện khoa học hấp dẫn về permafrost – lớp đất đóng băng quanh năm bao phủ phần lớn Yakutia và có nơi dày hàng trăm mét. Trưng bày giới thiệu lịch sử khám phá, các phương pháp nghiên cứu, thiết bị khoan, mẫu lõi băng, cùng những phát hiện về hệ sinh thái cổ và tác động của biến đổi khí hậu lên vùng cực. Điểm hấp dẫn nhất là phòng thí nghiệm ngầm được đào sâu vào lòng đất băng vĩnh cửu, nơi nhiệt độ luôn âm và du khách có thể tận mắt thấy các lớp băng ngầm hình thành qua hàng nghìn năm. Với những ai tò mò về khoa học địa cực, đây là một trải nghiệm khác biệt so với các bảo tàng nghệ thuật – vừa mang tính giáo dục cao, vừa cho cảm giác 'chạm' vào chính hiện tượng thiên nhiên đã định hình vùng đất lạnh nhất có người sinh sống này.",
    [
        "Bảo tàng của Viện Băng vĩnh cửu học SB RAS – trung tâm nghiên cứu hàng đầu thế giới.",
        "Có phòng thí nghiệm ngầm đào sâu vào lòng đất băng vĩnh cửu để tham quan.",
        "Tìm hiểu khoa học permafrost, mẫu lõi băng và tác động biến đổi khí hậu vùng cực.",
    ],
    p("Tham quan theo đăng ký trước, thường vào ngày làm việc, khoảng từ 8:30.",
      "Có phí tham quan; nên liên hệ đặt lịch trước, nhất là khi muốn xuống hầm ngầm.",
      "Khoảng 1 giờ.",
      "Quanh năm; hầm ngầm luôn lạnh nên cần mặc ấm.",
      "Bắt buộc đặt trước; mang áo ấm, giày kín khi xuống hầm băng vĩnh cửu."),
    [
        {"title": "2GIS — Институт мерзлотоведения, Музей вечной мерзлоты", "url": "https://2gis.ru/yakutsk/firm/7037402698755718"},
        {"title": "Trang viện — mpi.ysn.ru", "url": "http://mpi.ysn.ru/"},
    ],
    ["museum", "permafrost", "science", "underground", "yakutsk", "sakha"],
    maps_text("Институт мерзлотоведения, Музей истории изучения вечной мерзлоты", "Якутск", "Permafrost Institute Museum", "Yakutsk", 62.010932, 129.661693),
    official_site="http://mpi.ysn.ru/",
))

# ============================ NHÀ HÁT (theatre) ============================

# 8) Государственный театр оперы и балета им. Д.К. Сивцева-Суорун Омоллоона -----------
RECORDS.append(rec(
    "sakha-opera-ballet-theatre",
    "Nhà hát Opera và Ballet Quốc gia Sakha (Xu-ô-run Ô-mô-lô-ôn)",
    "Государственный театр оперы и балета Республики Саха (Якутия) им. Д.К. Сивцева-Суорун Омоллоона",
    "Sakha State Opera and Ballet Theatre",
    ["theatre"],
    62.023314, 129.719351,
    "Đại lộ Lenina 46/1, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Nhà hát opera và ballet chuyên nghiệp đầu tiên và duy nhất ở vùng Viễn Đông Nga, biểu diễn cả các kiệt tác cổ điển thế giới lẫn opera, ballet dựa trên sử thi và huyền thoại Yakut.",
    "Nhà hát Opera và Ballet Quốc gia Sakha là một trong số rất ít nhà hát opera - ballet ở Siberia và Viễn Đông, và là nhà hát mang tầm vóc như vậy đầu tiên của vùng Viễn Đông Nga. Được nâng cấp thành nhà hát opera - ballet quốc gia vào đầu thập niên 1990 (trên nền tảng các đoàn nghệ thuật âm nhạc có từ giữa thế kỷ 20), nhà hát mang tên nhà văn - nhà hoạt động văn hoá Dmitry Sivtsev - Suorun Omolloon. Trên sân khấu, khán giả có thể thưởng thức những kiệt tác kinh điển như 'Hồ thiên nga', 'Giselle', 'Kẹp hạt dẻ', 'La Bayadère', cùng các vở opera và ballet nguyên bản lấy cảm hứng từ sử thi Olonkho, huyền thoại và lịch sử của dân tộc Sakha. Nhà hát cũng là nơi tổ chức liên hoan ballet cổ điển 'Sterkh' (mang tên loài sếu trắng Siberia) danh tiếng. Toà nhà hiện đại, hoành tráng nằm trên đại lộ Lenina là niềm tự hào văn hoá của Yakutsk – nơi tinh hoa nghệ thuật hàn lâm thế giới hoà quyện với bản sắc phương Bắc.",
    [
        "Nhà hát opera - ballet đầu tiên và duy nhất của vùng Viễn Đông Nga.",
        "Biểu diễn cả kiệt tác cổ điển thế giới và tác phẩm dựa trên sử thi Olonkho.",
        "Nơi tổ chức liên hoan ballet cổ điển 'Sterkh' (sếu trắng Siberia) nổi tiếng.",
    ],
    p("Phòng vé và giờ diễn theo lịch mùa diễn; thường mở khoảng 10:00–19:00.",
      "Giá vé đa dạng tuỳ vở diễn và vị trí ghế; nên đặt trước qua trang chính thức.",
      "Một buổi diễn khoảng 2–3 giờ.",
      "Mùa diễn thường từ mùa thu đến mùa xuân.",
      "Xem lịch và đặt vé trên sakha-opera.ru; trang phục lịch sự khi vào nhà hát."),
    [
        {"title": "Culture.ru — Театр оперы и балета им. Д.К. Сивцева-Суорун Омоллоона", "url": "https://www.culture.ru/institutes/27873/gosudarstvennyi-teatr-opery-i-baleta-im-d-k-sivceva-suorun-omolloona"},
        {"title": "Trang chính thức — sakha-opera.ru", "url": "http://sakha-opera.ru/"},
    ],
    ["theatre", "opera", "ballet", "yakutsk", "olonkho", "sakha"],
    maps_text("Театр оперы и балета им. Д.К. Сивцева-Суорун Омоллоона", "Якутск", "Sakha State Opera and Ballet Theatre", "Yakutsk", 62.023314, 129.719351),
    official_site="http://sakha-opera.ru/",
))

# 9) Саха академический театр им. П.А. Ойунского -------------------------------------
RECORDS.append(rec(
    "sakha-academic-theatre-oyunsky",
    "Nhà hát kịch Hàn lâm Sakha mang tên Oyunsky (Xa-kha, Ôi-un-xki)",
    "Саха академический театр им. П.А. Ойунского",
    "Sakha Academic Theatre named after P.A. Oyunsky",
    ["theatre"],
    62.033288, 129.742247,
    "Phố Ordzhonikidze 1 (Quảng trường Ordzhonikidze), thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Nhà hát kịch quốc gia bằng tiếng Yakut, sân khấu hàng đầu gìn giữ ngôn ngữ, sử thi và bản sắc dân tộc Sakha. Toà nhà mang kiến trúc dân tộc độc đáo là biểu tượng của trung tâm Yakutsk.",
    "Nhà hát kịch Hàn lâm Sakha mang tên Oyunsky là nhà hát kịch quốc gia biểu diễn bằng tiếng Yakut (Sakha) – trái tim của sân khấu kịch nói dân tộc ở Yakutia. Với lịch sử hình thành từ nửa đầu thế kỷ 20 và danh hiệu 'hàn lâm' cao quý, nhà hát dàn dựng cả các vở kịch kinh điển thế giới lẫn những tác phẩm dựa trên sử thi Olonkho, huyền thoại, lịch sử và đời sống của người Sakha, qua đó góp phần quan trọng gìn giữ và phát triển ngôn ngữ, văn hoá dân tộc. Toà nhà nhà hát ở trung tâm Yakutsk gây ấn tượng bởi kiến trúc mang đậm mô-típ dân tộc phương Bắc, trở thành một biểu tượng thị giác của thành phố. Các buổi diễn thường thu hút đông khán giả địa phương, tạo nên không khí văn hoá sôi nổi. Với du khách, ghé nhà hát – dù chỉ để chiêm ngưỡng công trình hay xem một vở diễn có phụ đề – là cách cảm nhận sống động tiếng nói và tâm hồn của dân tộc Sakha.",
    [
        "Nhà hát kịch quốc gia hàng đầu biểu diễn bằng tiếng Yakut (Sakha).",
        "Dàn dựng các tác phẩm dựa trên sử thi Olonkho và văn hoá dân tộc.",
        "Toà nhà kiến trúc dân tộc độc đáo, biểu tượng của trung tâm Yakutsk.",
    ],
    p("Phòng vé và giờ diễn theo lịch mùa diễn; thường trong khung 10:00–19:00.",
      "Giá vé phải chăng tuỳ vở diễn; nên đặt trước qua trang chính thức.",
      "Một buổi diễn khoảng 2–3 giờ.",
      "Mùa diễn chủ yếu từ mùa thu đến mùa xuân.",
      "Biểu diễn bằng tiếng Yakut, một số suất có phụ đề; xem lịch trên sakhatheatre.ru."),
    [
        {"title": "Culture.ru — Саха академический театр им. П.А. Ойунского", "url": "https://www.culture.ru/institutes/10673/sakha-akademicheskii-teatr-imeni-p-a-oiunskogo"},
        {"title": "Trang chính thức — sakhatheatre.ru", "url": "http://sakhatheatre.ru/"},
    ],
    ["theatre", "drama", "yakut-language", "olonkho", "yakutsk", "sakha"],
    maps_text("Саха академический театр им. П.А. Ойунского", "Якутск", "Sakha Academic Theatre", "Yakutsk", 62.033288, 129.742247),
    official_site="http://sakhatheatre.ru/",
))

# 10) Государственный академический русский драматический театр им. А.С. Пушкина ------
RECORDS.append(rec(
    "russian-drama-theatre-pushkin-yakutsk",
    "Nhà hát kịch Nga Hàn lâm Quốc gia mang tên Pushkin (Yakutsk)",
    "Государственный академический русский драматический театр им. А.С. Пушкина",
    "State Academic Russian Drama Theatre named after A.S. Pushkin",
    ["theatre"],
    62.028576, 129.735134,
    "Đại lộ Lenina 21, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Nhà hát lâu đời nhất Yakutia, thành lập năm 1920, biểu diễn kịch bằng tiếng Nga. Một trung tâm sân khấu quan trọng, dàn dựng cả kịch cổ điển Nga - thế giới lẫn tác phẩm đương đại.",
    "Nhà hát kịch Nga Hàn lâm Quốc gia mang tên A.S. Pushkin là nhà hát đầu tiên và lâu đời nhất của Yakutia, ra đời năm 1920 từ một nhóm những người yêu sân khấu và âm nhạc ở Yakutsk. Trải qua hơn một thế kỷ, nhà hát đã trở thành một trong những trung tâm sân khấu uy tín nhất vùng Viễn Đông, được trao tặng danh hiệu 'hàn lâm' và mang tên đại thi hào Nga Aleksandr Pushkin. Sân khấu ở đây biểu diễn bằng tiếng Nga, với kịch mục phong phú trải từ các vở kinh điển của Pushkin, Chekhov, Gogol, kịch cổ điển thế giới, đến những tác phẩm hiện đại và đương đại. Nhà hát đóng vai trò cầu nối văn hoá, phục vụ đông đảo cư dân nói tiếng Nga của thành phố đa sắc tộc này. Toà nhà khang trang nằm ngay trên đại lộ Lenina, trung tâm Yakutsk. Với du khách, một buổi tối tại nhà hát Pushkin là dịp thưởng thức nghệ thuật kịch nói chất lượng và hoà mình vào nhịp sống văn hoá của thủ phủ vùng cực.",
    [
        "Nhà hát lâu đời nhất Yakutia, thành lập năm 1920.",
        "Biểu diễn kịch bằng tiếng Nga, mang danh hiệu hàn lâm và tên Pushkin.",
        "Kịch mục phong phú từ cổ điển Nga - thế giới đến đương đại.",
    ],
    p("Phòng vé và giờ diễn theo lịch mùa diễn; thường mở khoảng 10:00–19:00.",
      "Giá vé phải chăng tuỳ vở diễn và vị trí; nên đặt trước qua trang chính thức.",
      "Một buổi diễn khoảng 2–3 giờ.",
      "Mùa diễn chủ yếu từ mùa thu đến mùa xuân.",
      "Biểu diễn bằng tiếng Nga; xem lịch và đặt vé trên gardt.ru."),
    [
        {"title": "Wikipedia (RU) — Русский драматический театр (Якутск)", "url": "https://ru.wikipedia.org/wiki/Русский_драматический_театр_(Якутск)"},
        {"title": "Culture.ru — Русский драматический театр им. А.С. Пушкина", "url": "https://www.culture.ru/institutes/27874/gosudarstvennyi-akademicheskii-russkii-dramaticheskii-teatr-im-a-s-pushkina"},
    ],
    ["theatre", "drama", "russian-theatre", "pushkin", "yakutsk", "sakha"],
    maps_text("Русский драматический театр им. А.С. Пушкина", "Якутск", "Russian Drama Theatre Pushkin", "Yakutsk", 62.028576, 129.735134),
    official_site="http://gardt.ru/",
))

# ============================ NHÀ THỜ (church) ============================

# 11) Градоякутский Преображенский кафедральный собор --------------------------------
RECORDS.append(rec(
    "preobrazhensky-cathedral-yakutsk",
    "Nhà thờ chính toà Chúa Hiển Dung Yakutsk (Prê-ô-bra-gien-xki)",
    "Градоякутский Преображенский кафедральный собор",
    "Transfiguration (Preobrazhensky) Cathedral of Yakutsk",
    ["church"],
    62.023918, 129.736461,
    "Phố Kirova 3, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Nhà thờ chính toà Chính thống giáo cổ nhất còn lại của Yakutsk, xây dựng năm 1826–1845 theo phong cách kiến trúc Nga giả cổ, do các thương gia Solovyov tài trợ. Một biểu tượng lịch sử - tâm linh của thành phố.",
    "Nhà thờ chính toà Chúa Hiển Dung (Preobrazhensky) là ngôi thánh đường Chính thống giáo cổ nhất còn tồn tại ở Yakutsk. Được xây dựng trong các năm 1826–1845 bằng nguồn tài trợ của gia đình thương gia giàu có Solovyov, nhà thờ mang phong cách kiến trúc Nga giả cổ (псевдорусский) với những đường nét trang nghiêm, mái vòm và tháp chuông đặc trưng. Suốt gần hai thế kỷ, công trình đã chứng kiến bao thăng trầm của thành phố: từ thời Đế quốc Nga, qua giai đoạn Xô Viết khi nhiều nhà thờ bị đóng cửa, đến khi được trả lại cho giáo hội năm 1994 và trùng tu hoàn tất vào đầu những năm 2000. Năm 2005, nhà thờ được nâng thành nhà thờ chính toà (собор) của giáo phận Yakutia. Ngày nay đây là trung tâm đời sống Chính thống giáo của vùng, với các nghi lễ trang trọng và không gian nội thất được phục dựng công phu. Với du khách, nhà thờ vừa là một di tích kiến trúc quý giá giữa lòng Yakutsk, vừa là nơi cảm nhận chiều sâu tâm linh và lịch sử khai hoang của người Nga nơi vùng cực.",
    [
        "Nhà thờ Chính thống giáo cổ nhất còn lại của Yakutsk (xây 1826–1845).",
        "Kiến trúc Nga giả cổ, do các thương gia Solovyov tài trợ xây dựng.",
        "Nhà thờ chính toà của giáo phận Yakutia, trung tâm tâm linh của vùng.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường từ khoảng 8:00; giờ lễ chính vào sáng và chiều.",
      "Miễn phí vào cửa (có thể quyên góp tuỳ tâm).",
      "Khoảng 20–30 phút.",
      "Quanh năm; đặc biệt trang trọng vào các dịp lễ Chính thống giáo.",
      "Trang phục kín đáo; nữ nên trùm khăn; giữ yên lặng và tôn trọng khi có nghi lễ."),
    [
        {"title": "Sobory.ru — Кафедральный собор Преображения Господня (Якутск)", "url": "https://sobory.ru/article/?object=09294"},
        {"title": "Азбука паломника — Собор Спаса Преображения (Якутск)", "url": "https://azbyka.ru/palomnik/Собор_Спаса_Преображения_(Якутск)"},
    ],
    ["church", "orthodox", "cathedral", "architecture", "yakutsk", "sakha"],
    maps_text("Градоякутский Преображенский кафедральный собор", "Якутск", "Transfiguration Cathedral", "Yakutsk", 62.023918, 129.736461),
))

# 12) Градоякутский Никольский храм --------------------------------------------------
RECORDS.append(rec(
    "nikolsky-church-yakutsk",
    "Nhà thờ Thánh Nikolai Yakutsk (Ni-côn-xki)",
    "Градоякутский Никольский храм",
    "St. Nicholas (Nikolsky) Church of Yakutsk",
    ["church"],
    62.030137, 129.7118,
    "Phố Oktyabrskaya 31, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Ngôi nhà thờ Chính thống giáo cổ kính thờ Thánh Nikolai – vị thánh bảo trợ của người đi biển và lữ khách, được người dân Yakutsk đặc biệt tôn kính. Một điểm hành hương ấm áp giữa thành phố lạnh giá.",
    "Nhà thờ Thánh Nikolai (Nikolsky) là một trong những ngôi thánh đường được yêu mến nhất của Yakutsk, thờ Thánh Nikolai kỳ diệu – vị thánh bảo trợ cho người đi đường, lữ khách và những ai gặp hoạn nạn, đặc biệt được sùng kính ở một vùng đất khắc nghiệt và xa xôi như Yakutia. Ngôi nhà thờ hiện nay được xây dựng vào giữa thế kỷ 19, kế thừa truyền thống thờ Thánh Nikolai có từ những nhà thờ gỗ đầu tiên của thành phố hồi thế kỷ 18. Với lối kiến trúc Chính thống giáo thanh thoát, mái vòm và tháp chuông duyên dáng, nhà thờ tạo nên một điểm nhấn tâm linh ấm áp giữa phố phường. Trải qua thời kỳ Xô Viết đầy biến động, nhà thờ đã được khôi phục và trở lại là nơi cử hành các nghi lễ, thu hút đông đảo tín hữu cũng như du khách. Không gian bên trong với các bức icon, ánh nến và tiếng cầu nguyện mang lại cảm giác bình an. Đây là điểm dừng ý nghĩa để tìm hiểu đời sống Chính thống giáo và lịch sử của cộng đồng người Nga ở vùng cực đông bắc.",
    [
        "Nhà thờ Chính thống giáo cổ thờ Thánh Nikolai, được người Yakutsk tôn kính.",
        "Kế thừa truyền thống nhà thờ Thánh Nikolai có từ thế kỷ 18 của thành phố.",
        "Không gian tâm linh ấm áp với icon, ánh nến giữa vùng đất lạnh giá.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường từ khoảng 8:00; lễ chính sáng và chiều.",
      "Miễn phí vào cửa (có thể quyên góp tuỳ tâm).",
      "Khoảng 20–30 phút.",
      "Quanh năm; đông tín hữu vào các dịp lễ Chính thống giáo.",
      "Trang phục kín đáo; nữ nên trùm khăn; giữ yên lặng khi có nghi lễ."),
    [
        {"title": "Drevo — Якутский Никольский храм", "url": "https://drevo-info.ru/articles/13676556.html"},
        {"title": "Азбука паломника — Градоякутский Никольский храм", "url": "https://azbyka.ru/palomnik/Градоякутский_Никольский_храм"},
    ],
    ["church", "orthodox", "st-nicholas", "yakutsk", "pilgrimage", "sakha"],
    maps_text("Градоякутский Никольский храм", "Якутск", "St. Nicholas Church", "Yakutsk", 62.030137, 129.7118),
))

# ============================ TƯỢNG ĐÀI / QUẢNG TRƯỜNG ============================

# 13) Памятник П.И. Бекетову ---------------------------------------------------------
RECORDS.append(rec(
    "beketov-monument-yakutsk",
    "Tượng đài Pyotr Beketov – người sáng lập Yakutsk (Bê-kê-tốp)",
    "Памятник П.И. Бекетову",
    "Monument to Pyotr Beketov, founder of Yakutsk",
    ["monument"],
    62.023527, 129.738768,
    "Bờ kè Moskovskaya (gần Phố Cổ), thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Tượng đài đồng cao 5 mét tôn vinh Pyotr Beketov – viên đội cận vệ (streltsy) đã lập nên pháo đài Yakutsk năm 1632, khai sinh thành phố. Một biểu tượng lịch sử bên bờ sông Lena.",
    "Tượng đài Pyotr Ivanovich Beketov tôn vinh người khai sinh thành phố Yakutsk. Beketov là một viên đội trưởng cận vệ (streltsy) của Nga, người được ghi công đã dựng nên pháo đài (ostrog) đầu tiên vào năm 1632, đặt nền móng cho sự ra đời của Yakutsk – nay là thủ phủ của cả một vùng rộng lớn. Bức tượng đồng cao khoảng 5 mét, đặt trên bệ ốp đá granite, được chế tác tại thành phố Smolensk và khánh thành ngày 27 tháng 9 năm 2007. Tác phẩm khắc hoạ hình ảnh Beketov trong tư thế trầm tư, gắn với hình tượng người tiên phong đã vượt hàng nghìn dặm đường rừng taiga giá lạnh để mở mang bờ cõi. Tượng đài nằm ở khu vực bờ kè Moskovskaya, gần quần thể Phố Cổ và bên dòng sông Lena hùng vĩ, tạo thành một điểm dừng chân ý nghĩa cho du khách muốn tìm hiểu cội nguồn lịch sử của thành phố. Đây cũng là nơi lý tưởng để chụp ảnh và ngắm cảnh sông nước, đặc biệt vào mùa hè khi bờ kè trở nên nhộn nhịp.",
    [
        "Tôn vinh Pyotr Beketov – người lập pháo đài Yakutsk năm 1632.",
        "Tượng đồng cao 5 mét, khánh thành năm 2007, chế tác tại Smolensk.",
        "Nằm bên bờ kè sông Lena, gần quần thể Phố Cổ Yakutsk.",
    ],
    p("Không gian ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15–20 phút.",
      "Mùa hè và đầu thu, khi bờ kè sông Lena nhộn nhịp và ấm áp.",
      "Kết hợp dạo Phố Cổ và bờ kè; mùa đông rất lạnh nên cần mặc thật ấm."),
    [
        {"title": "2GIS — Памятник П.И. Бекетову", "url": "https://2gis.ru/yakutsk/geo/7037570202468390"},
        {"title": "Туризм в Якутии — Памятник основателю Якутска П.И. Бекетову", "url": "https://virtualyakutia.ru/node/290"},
    ],
    ["monument", "beketov", "history", "founder", "yakutsk", "sakha"],
    maps_text("Памятник П.И. Бекетову", "Якутск", "Monument to Pyotr Beketov", "Yakutsk", 62.023527, 129.738768),
))

# 14) Площадь В.И. Ленина ------------------------------------------------------------
RECORDS.append(rec(
    "lenin-square-yakutsk",
    "Quảng trường Lenin Yakutsk (Plô-sat Lê-nin)",
    "Площадь В.И. Ленина",
    "Lenin Square (Yakutsk)",
    ["square_street"],
    62.027577, 129.730589,
    "Trung tâm thành phố Yakutsk (Đại lộ Lenina), Cộng hoà Sakha (Yakutia), Nga",
    "Quảng trường trung tâm chính của Yakutsk, nơi diễn ra các sự kiện, lễ hội lớn và là điểm hẹn quen thuộc của người dân. Mùa đông biến thành công viên băng với thành phố tuyết và sân trượt.",
    "Quảng trường Lenin là quảng trường trung tâm và quan trọng nhất của Yakutsk – trái tim của thủ phủ Cộng hoà Sakha. Đây là nơi tập trung các toà nhà hành chính, có tượng đài Lenin, và là không gian tổ chức những sự kiện lớn của thành phố: mít tinh, diễu hành, hoà nhạc, lễ hội và các hoạt động cộng đồng. Điểm đặc biệt khiến quảng trường trở thành điểm đến hấp dẫn với du khách chính là mùa đông: khi nhiệt độ xuống tới hàng chục độ âm, quảng trường được biến thành một 'thành phố băng' lộng lẫy với các công trình điêu khắc từ băng và tuyết, cầu trượt băng, cây thông năm mới và sân trượt – nơi người dân và du khách vui chơi bất chấp giá rét khắc nghiệt. Vào mùa hè, quảng trường lại là không gian dạo bộ thoáng đãng, gần các điểm tham quan trung tâm. Ghé quảng trường Lenin, du khách có thể cảm nhận nhịp sống đô thị của thành phố lạnh nhất thế giới và chứng kiến cách người Sakha biến cái lạnh thành niềm vui.",
    [
        "Quảng trường trung tâm chính, trái tim của thành phố Yakutsk.",
        "Nơi diễn ra các sự kiện, lễ hội và mít tinh lớn của thủ phủ Sakha.",
        "Mùa đông biến thành 'thành phố băng' với điêu khắc băng và sân trượt.",
    ],
    p("Không gian công cộng, mở cửa tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Mùa đông để xem thành phố băng; mùa hè để dạo bộ.",
      "Mùa đông cực lạnh, cần trang bị đồ giữ nhiệt kỹ khi vui chơi ngoài trời."),
    [
        {"title": "2GIS — Площадь В.И. Ленина (Якутск)", "url": "https://2gis.ru/yakutsk/geo/7037561612533774"},
        {"title": "Wikipedia (RU) — Якутск", "url": "https://ru.wikipedia.org/wiki/Якутск"},
    ],
    ["square_street", "central-square", "winter", "ice-city", "yakutsk", "sakha"],
    maps_text("Площадь В.И. Ленина", "Якутск", "Lenin Square", "Yakutsk", 62.027577, 129.730589),
))

# 15) Мемориальный комплекс «Победа» (площадь Победы) --------------------------------
RECORDS.append(rec(
    "victory-square-memorial-yakutsk",
    "Quảng trường Chiến thắng và Đài tưởng niệm 'Pobeda' (Plô-sat Pô-bê-đư)",
    "Площадь Победы, мемориальный комплекс «Победа»",
    "Victory Square and 'Pobeda' Memorial Complex",
    ["monument", "square_street"],
    62.040399, 129.756242,
    "Quảng trường Chiến thắng, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Quần thể tưởng niệm Chiến tranh Vệ quốc Vĩ đại, khánh thành năm 1975 nhân 30 năm Chiến thắng. Có Ngọn lửa vĩnh cửu, tượng đài kỵ sĩ, xe tăng T-34 và các phiến đá tưởng niệm những thành phố anh hùng.",
    "Quảng trường Chiến thắng cùng quần thể tưởng niệm 'Pobeda' là một trong những địa điểm được tôn kính nhất ở Yakutsk. Được khánh thành năm 1975 nhân kỷ niệm 30 năm Chiến thắng trong Chiến tranh Vệ quốc Vĩ đại, quần thể là nơi tưởng nhớ hàng nghìn người con của Yakutia đã ngã xuống hoặc góp sức cho tiền tuyến trong Thế chiến II. Trung tâm của quần thể là Ngọn lửa vĩnh cửu cháy không tắt, cùng bức phù điêu - tượng đài với hình tượng người kỵ sĩ, các phiến đá khắc tên những 'thành phố anh hùng' của Liên Xô, cảnh 'tiễn đưa ra mặt trận', một nhà nguyện và chiếc xe tăng huyền thoại T-34 được đặt trang trọng. Không gian rộng lớn, trang nghiêm này là nơi diễn ra các nghi lễ đặt hoa, lễ duyệt binh ngày 9/5 và những buổi tưởng niệm long trọng. Với du khách, đây không chỉ là một điểm tham quan lịch sử mà còn là nơi cảm nhận ký ức chiến tranh và lòng biết ơn sâu sắc của người dân vùng cực đối với những người đã hy sinh vì Tổ quốc.",
    [
        "Quần thể tưởng niệm Thế chiến II với Ngọn lửa vĩnh cửu, khánh thành năm 1975.",
        "Có tượng đài kỵ sĩ, xe tăng T-34 và phiến đá các thành phố anh hùng.",
        "Nơi diễn ra lễ tưởng niệm và duyệt binh Ngày Chiến thắng 9/5.",
    ],
    p("Không gian ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Quanh năm; trang nghiêm nhất vào dịp 9/5.",
      "Giữ thái độ tôn nghiêm; mùa đông rất lạnh nên cần mặc thật ấm."),
    [
        {"title": "Wikipedia (RU) — Мемориальный комплекс «Победа» (Якутск)", "url": "https://ru.wikipedia.org/wiki/Мемориальный_комплекс_«Победа»_(Якутск)"},
        {"title": "2GIS — Площадь Победы (Якутск)", "url": "https://2gis.ru/yakutsk/geo/7037561612533779"},
    ],
    ["monument", "memorial", "wwii", "victory", "yakutsk", "sakha"],
    maps_text("Площадь Победы, мемориальный комплекс Победа", "Якутск", "Victory Memorial Complex", "Yakutsk", 62.040399, 129.756242),
))

# ============================ CÔNG VIÊN / VƯỜN (park_garden) & KHÁC (other) ============================

# 16) Государственный цирк Республики Саха (Якутия) им. Марфы и Сергея Расторгуевых ---
RECORDS.append(rec(
    "sakha-state-circus-yakutsk",
    "Rạp xiếc Quốc gia Cộng hoà Sakha (Yakutia)",
    "Государственный цирк Республики Саха (Якутия) им. Марфы и Сергея Расторгуевых",
    "Sakha State Circus",
    ["other"],
    62.032418, 129.724162,
    "Phố Poyarkova 22, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Rạp xiếc quốc gia của Yakutia, một trong số ít rạp xiếc chuyên nghiệp ở vùng Viễn Đông, nổi tiếng với các chương trình biểu diễn hấp dẫn và trường phái xiếc mang bản sắc phương Bắc.",
    "Rạp xiếc Quốc gia Cộng hoà Sakha mang tên hai nghệ sĩ Marfa và Sergey Rastorguev là một địa chỉ giải trí được yêu mến bậc nhất ở Yakutsk, đặc biệt với các gia đình và trẻ em. Đây là một trong số ít rạp xiếc cố định, chuyên nghiệp ở vùng Viễn Đông Nga – điều khá đặc biệt với một thành phố xa xôi và khắc nghiệt như Yakutsk. Rạp thường xuyên tổ chức các chương trình biểu diễn đa dạng: nhào lộn, tung hứng, xiếc thú, ảo thuật, hề và các tiết mục mạo hiểm, cả của đoàn nhà lẫn các đoàn xiếc lưu diễn từ khắp nước Nga và quốc tế. Yakutia còn tự hào về truyền thống đào tạo nghệ sĩ xiếc riêng, góp phần nuôi dưỡng nhiều tài năng. Toà nhà rạp xiếc hiện đại ở trung tâm thành phố là điểm đến lý tưởng cho một buổi tối vui vẻ, ấm áp – nhất là vào mùa đông khi bên ngoài băng giá. Với du khách đi cùng trẻ nhỏ hoặc muốn trải nghiệm đời sống giải trí của người dân địa phương, đây là một lựa chọn thú vị và khác biệt.",
    [
        "Rạp xiếc quốc gia, một trong số ít rạp cố định ở vùng Viễn Đông Nga.",
        "Chương trình đa dạng: nhào lộn, xiếc thú, ảo thuật, hề, tiết mục mạo hiểm.",
        "Điểm giải trí ấm áp cho gia đình, đặc biệt vào mùa đông băng giá.",
    ],
    p("Buổi diễn theo lịch, thường vào cuối tuần và dịp lễ; phòng vé mở khoảng 10:00–19:00.",
      "Giá vé phải chăng, đa dạng theo vị trí; nên đặt trước cho các suất cuối tuần.",
      "Một chương trình khoảng 1,5–2 giờ.",
      "Quanh năm; rất phù hợp cho mùa đông.",
      "Xem lịch trên diamond-circus.ru; đi sớm để chọn chỗ đẹp nếu vé tự do."),
    [
        {"title": "2GIS — Государственный цирк Республики Саха (Якутия)", "url": "https://2gis.ru/yakutsk/firm/7037402698745796"},
        {"title": "Trang chính thức — diamond-circus.ru", "url": "http://diamond-circus.ru/"},
    ],
    ["other", "circus", "entertainment", "family", "yakutsk", "sakha"],
    maps_text("Государственный цирк Республики Саха (Якутия)", "Якутск", "Sakha State Circus", "Yakutsk", 62.032418, 129.724162),
    official_site="http://diamond-circus.ru/",
))

# 17) Ысыах Туймаады — архитектурно-этнографический комплекс (местность Ус Хатын) -----
RECORDS.append(rec(
    "ysyakh-tuymaady-us-khatyn",
    "Quần thể lễ hội Ysyakh Tuymaady tại Ус Хатын (Ư-xư-akh Tui-ma-a-đư)",
    "Ысыах Туймаады, архитектурно-этнографический комплекс (местность Ус Хатын)",
    "Ysyakh Tuymaady Ethnographic Complex (Us Khatyn)",
    ["park_garden", "other"],
    62.196833, 129.782883,
    "Vùng Ус Хатын, cách trung tâm Yakutsk khoảng 17 km về phía bắc, Cộng hoà Sakha (Yakutia), Nga",
    "Khu quần thể kiến trúc - dân tộc học ngoài trời, nơi tổ chức Ysyakh – lễ hội mừng năm mới và hạ chí lớn nhất của người Yakut. Có cột thiêng, lều urasa truyền thống, trường đua ngựa và các nghi lễ tế trời.",
    "Ysyakh Tuymaady tại vùng Ус Хатын là quần thể kiến trúc - dân tộc học ngoài trời quan trọng nhất của người Sakha, cách trung tâm Yakutsk khoảng 17 km. Đây là nơi tổ chức Ysyakh – lễ hội truyền thống lớn nhất và thiêng liêng nhất của người Yakut, diễn ra vào dịp hạ chí cuối tháng 6 để mừng năm mới, mừng mùa hè và tạ ơn các vị thần Aiyy. Trong những ngày lễ, hàng chục nghìn, thậm chí hàng trăm nghìn người đổ về đây, mặc trang phục dân tộc rực rỡ, tham dự nghi lễ tế trời với sữa ngựa lên men (kumys), điệu múa vòng osuokhai kéo dài, các cuộc thi thể thao dân tộc, đua ngựa và trình diễn khomus. Quần thể được bố trí với cột thiêng (serge), các lều urasa hình chóp bằng gỗ - vỏ cây truyền thống, khu tyusyulge của các cộng đồng, và một trường đua ngựa. Ngay cả ngoài dịp lễ, nơi đây vẫn là một không gian văn hoá mở, giúp du khách hình dung đời sống, tín ngưỡng và bản sắc rực rỡ của dân tộc Sakha. Nếu đến Yakutia vào cuối tháng 6, tham dự Ysyakh là một trải nghiệm khó quên bậc nhất.",
    [
        "Nơi tổ chức Ysyakh – lễ hội hạ chí và năm mới lớn nhất của người Yakut.",
        "Có cột thiêng serge, lều urasa truyền thống và trường đua ngựa.",
        "Dịp hạ chí quy tụ hàng vạn người với nghi lễ tế trời, múa osuokhai, đua ngựa.",
    ],
    p("Không gian ngoài trời; sôi động nhất trong dịp lễ Ysyakh cuối tháng 6 (thường 27–29/6).",
      "Ngoài dịp lễ thường vào tự do; một số sự kiện có thể thu phí.",
      "Nửa ngày trong dịp lễ; khoảng 1 giờ ngoài dịp lễ.",
      "Cuối tháng 6 (hạ chí) để dự lễ Ysyakh.",
      "Dịp lễ rất đông, nên đi sớm, mang nước và mũ; tôn trọng nghi lễ tế thiêng."),
    [
        {"title": "VisitYakutia — Ысыах Туймаады в Якутске", "url": "https://visityakutia.com/ysyah-jakutsk-jakutija/"},
        {"title": "2GIS — Ысыах Туймаады (Ус Хатын)", "url": "https://2gis.ru/yakutsk/firm/70000001027971093"},
    ],
    ["park_garden", "ysyakh", "festival", "ethnography", "yakutsk", "sakha"],
    maps_text("Ысыах Туймаады Ус Хатын", "Якутск", "Ysyakh Tuymaady Us Khatyn", "Yakutsk", 62.196833, 129.782883),
))

# 18) Ботанический сад Якутского научного центра СО РАН (ИБПК) -----------------------
RECORDS.append(rec(
    "yakutsk-botanical-garden",
    "Vườn Bách thảo Yakutsk (Viện IBPK, Phân viện Siberia)",
    "Ботанический сад Якутского научного центра СО РАН (ИБПК)",
    "Yakutsk Botanical Garden (Institute for Biological Problems of the Cryolithozone)",
    ["park_garden"],
    62.01868, 129.606299,
    "Đường Sergelyakhskoe shosse km 10, thành phố Yakutsk, Cộng hoà Sakha (Yakutia), Nga",
    "Vườn bách thảo khoa học nằm ở thung lũng sông Lena, cách trung tâm Yakutsk khoảng 10 km. Nơi bảo tồn và giới thiệu hệ thực vật phương Bắc thích nghi với điều kiện băng vĩnh cửu khắc nghiệt.",
    "Vườn Bách thảo Yakutsk thuộc Viện Các vấn đề sinh học vùng băng vĩnh cửu (IBPK) của Trung tâm Khoa học Yakutsk, Phân viện Siberia Viện Hàn lâm Khoa học Nga. Nằm trên bậc thềm sông của thung lũng sông Lena, cách trung tâm thành phố khoảng 10 km về phía nam, vườn là một trong những vườn bách thảo cực bắc của thế giới, nơi nghiên cứu và bảo tồn hệ thực vật có khả năng sống sót trong điều kiện băng vĩnh cửu và mùa đông cực lạnh. Tại đây, du khách có thể dạo bước qua các bộ sưu tập cây bản địa của rừng taiga và thảo nguyên Yakutia, các loài hoa, cây thuốc, cây bụi phương Bắc, cùng những khu vực giới thiệu thực vật du nhập được thử nghiệm thích nghi. Vườn còn có nhà kính, các luống hoa và không gian xanh mát – một mảng thiên nhiên dịu dàng hiếm hoi giữa vùng đất khắc nghiệt. Vào mùa hè ngắn ngủi, khi cây cỏ bừng nở, vườn trở nên đặc biệt hấp dẫn cho những ai yêu thiên nhiên và muốn hiểu cách sự sống thực vật thích nghi với 'xứ sở băng giá'.",
    [
        "Một trong những vườn bách thảo cực bắc của thế giới, bên thung lũng sông Lena.",
        "Bảo tồn hệ thực vật phương Bắc thích nghi với băng vĩnh cửu.",
        "Không gian xanh với cây bản địa taiga, hoa, cây thuốc và nhà kính.",
    ],
    p("Tham quan theo đăng ký trước, thường từ khoảng 9:00 vào mùa ấm.",
      "Vé vào cửa khoảng 500 rúp; ưu đãi cho các nhóm ưu tiên (khoảng 300 rúp).",
      "Khoảng 1–1,5 giờ.",
      "Mùa hè (tháng 6–8), khi cây cỏ nở rộ.",
      "Nên gọi đặt trước; đi giày thoải mái; mang chống muỗi vào mùa hè."),
    [
        {"title": "2GIS — Ботанический сад ЯНЦ СО РАН", "url": "https://2gis.ru/yakutsk/firm/7037402698744543"},
        {"title": "Trang viện — ibpc.ysn.ru", "url": "http://ibpc.ysn.ru/"},
    ],
    ["park_garden", "botanical-garden", "nature", "science", "yakutsk", "sakha"],
    maps_text("Ботанический сад Якутского научного центра СО РАН", "Якутск", "Yakutsk Botanical Garden", "Yakutsk", 62.01868, 129.606299),
    official_site="http://ibpc.ysn.ru/",
))

# 19) Ледник Булуус ------------------------------------------------------------------
RECORDS.append(rec(
    "buluus-ice-spring",
    "Băng hà Buluus (Bu-lú-t)",
    "Ледник Булуус",
    "Buluus Glacier (Ice Spring)",
    ["other"],
    61.337926, 129.070526,
    "Huyện Khangalassky, cách Yakutsk khoảng 100 km về phía tây nam, Cộng hoà Sakha (Yakutia), Nga",
    "Cánh đồng băng độc đáo hình thành từ các mạch nước ngầm, gần như không tan ngay cả giữa mùa hè nóng bức. Một 'ốc đảo băng' kỳ thú và điểm giải nhiệt yêu thích của người dân Yakutia.",
    "Buluus (tiếng Yakut nghĩa là 'băng') là một trong những kỳ quan thiên nhiên độc đáo và được yêu thích nhất của Yakutia, nằm ở huyện Khangalassky, cách Yakutsk khoảng 100 km. Đây là một cánh đồng băng khổng lồ hình thành nhờ các mạch nước ngầm tinh khiết trào lên mặt đất rồi đóng băng thành từng lớp dày, có nơi tới ba mét. Điều kỳ diệu là ngay cả trong những ngày hè nóng nhất, khi nhiệt độ ngoài trời có thể vượt +30°C, lớp băng ở Buluus vẫn gần như không tan, còn dòng nước suối chảy ra luôn lạnh buốt, trong vắt, chỉ khoảng 0–1°C và có thể uống trực tiếp. Khung cảnh tương phản kỳ lạ – băng tuyết trắng xoá giữa rừng taiga xanh mướt và bầu trời mùa hè – khiến Buluus trở thành điểm đến hấp dẫn để giải nhiệt, dã ngoại và chụp ảnh. Khu vực đã được đầu tư cơ sở phục vụ du khách với lối đi, chòi nghỉ và bãi đỗ. Ghé Buluus, du khách được tận hưởng một trải nghiệm 'mùa đông giữa mùa hè' rất đặc trưng của xứ băng vĩnh cửu.",
    [
        "Cánh đồng băng từ mạch nước ngầm, gần như không tan ngay cả giữa mùa hè.",
        "Nước suối băng lạnh 0–1°C, trong vắt và có thể uống trực tiếp.",
        "Khung cảnh tương phản 'mùa đông giữa mùa hè' độc đáo giữa rừng taiga.",
    ],
    p("Không gian ngoài trời; phù hợp tham quan ban ngày, chủ yếu vào mùa ấm.",
      "Thường có phí vào khu du lịch ở mức thấp; tự túc phương tiện hoặc theo tour.",
      "Khoảng 1–2 giờ (chưa kể đường đi).",
      "Mùa hè (tháng 6–8) để cảm nhận rõ sự tương phản băng - nắng.",
      "Cách Yakutsk ~100 km, nên đi theo tour hoặc xe riêng; mang áo ấm dù giữa hè."),
    [
        {"title": "Travel-YKT — Ледник Булуус", "url": "https://travel-ykt.ru/dostoprimechatelnosti/prirodnye-dostoprimechatelnosti/buluus.html"},
        {"title": "2GIS — Ледник Булуус", "url": "https://2gis.ru/yakutsk/geo/70030076164305800"},
    ],
    ["other", "nature", "glacier", "ice-spring", "khangalassky", "sakha"],
    maps_text("Ледник Булуус", "Хангаласский улус", "Buluus Glacier", "Yakutia", 61.337926, 129.070526),
))

# 20) Водопады Курулуур --------------------------------------------------------------
RECORDS.append(rec(
    "kurulur-waterfall",
    "Thác Kurulur (Cu-ru-lú-r)",
    "Водопады Курулуур (Күрүлүүр)",
    "Kurulur Waterfalls",
    ["other"],
    61.408438, 129.557909,
    "Sông Menda, huyện Khangalassky, cách Yakutsk khoảng 110 km, Cộng hoà Sakha (Yakutia), Nga",
    "Thác nước hiếm hoi giữa vùng đồng bằng trung tâm Yakutia, với dòng sông đá lô nhô, nhiều ghềnh nhỏ và thác cao khoảng hai mét. Điểm dã ngoại, tắm mát và nghỉ ngơi được ưa chuộng.",
    "Kurulur (tiếng Yakut: Күрүлүүр) là quần thể thác - ghềnh nằm trên sông Menda thuộc huyện Khangalassky, cách Yakutsk khoảng 110 km theo đường bộ. Điều khiến Kurulur đặc biệt là nó gần như là thác nước duy nhất giữa vùng đồng bằng trung tâm Yakutia vốn bằng phẳng – nơi vắng bóng núi non và thác ghềnh. Dòng sông ở đây chảy qua những bờ đá và vách đá cao khoảng 7–8 mét, tạo thành nhiều ghềnh nhỏ và một thác nước cao chừng hai mét, nước réo rắt tung bọt trắng. Vào mùa hè, khu vực trở thành điểm dã ngoại lý tưởng: người dân đến đây tắm mát ở những vũng nước trong, câu cá, nướng thịt và cắm trại. Khu vực đã được cải tạo phục vụ du khách với chòi nghỉ, ghế, lò nướng và các tiện ích cơ bản. Cảnh quan sông nước, đá và rừng taiga tạo nên một không gian thư giãn hiếm có. Kurulur thường được kết hợp trong hành trình một ngày cùng băng hà Buluus và các điểm tự nhiên khác của Khangalassky, mang lại trải nghiệm thiên nhiên tươi mát giữa xứ sở lạnh giá.",
    [
        "Thác nước hiếm hoi giữa vùng đồng bằng trung tâm Yakutia.",
        "Sông đá với nhiều ghềnh nhỏ và thác cao khoảng hai mét.",
        "Điểm dã ngoại, tắm mát mùa hè với chòi nghỉ và lò nướng.",
    ],
    p("Không gian ngoài trời; phù hợp tham quan ban ngày vào mùa ấm.",
      "Thường có phí vào khu vực ở mức thấp; tự túc phương tiện hoặc theo tour.",
      "Khoảng 1–2 giờ (chưa kể đường đi).",
      "Mùa hè (tháng 6–8) để dã ngoại và tắm mát.",
      "Cách Yakutsk ~110 km; nên đi tour/xe riêng, thường ghép cùng Buluus trong ngày."),
    [
        {"title": "Wikipedia (RU) — Кюрюлюр", "url": "https://ru.wikipedia.org/wiki/Кюрюлюр"},
        {"title": "Visit Yakutia — Водопад Курулуур", "url": "https://visit-yakutia.com/vodopad-kuruluur/"},
    ],
    ["other", "nature", "waterfall", "picnic", "khangalassky", "sakha"],
    maps_text("Водопады Курулуур", "Хангаласский улус", "Kurulur Waterfalls", "Yakutia", 61.408438, 129.557909),
))

# 21) Синские столбы -----------------------------------------------------------------
RECORDS.append(rec(
    "sinsk-pillars",
    "Cột đá Sinsk (Xin-xki-ê Xtôn-bư)",
    "Синские столбы",
    "Sinsk Pillars",
    ["other"],
    61.38284, 126.656618,
    "Hạ lưu sông Sinyaya, huyện Khangalassky, cách Yakutsk khoảng 200 km, Cộng hoà Sakha (Yakutia), Nga",
    "Những vách đá vôi dựng đứng chạy dọc sông Sinyaya, 'người anh em' ít nổi tiếng hơn của Cột đá Lena nhưng hoang sơ và kỳ vĩ. Cùng thuộc Di sản thế giới UNESCO 'Công viên tự nhiên Cột đá Lena'.",
    "Cột đá Sinsk (Синские столбы) là một quần thể vách đá kỳ vĩ trải dọc theo sông Sinyaya – một phụ lưu tả ngạn của sông Lena – ở hạ lưu con sông, thuộc huyện Khangalassky, cách Yakutsk khoảng 200 km. Được tạo thành từ đá vôi kỷ Cambri, những cột đá và vách đá dựng đứng ở đây cao tới hàng chục mét (nhiều nơi 70–110 m), kéo dài thành từng cụm dọc bờ sông như một 'khu rừng đá' hoang sơ. Sinsk chính là 'người anh em' của Cột đá Lena danh tiếng, và cùng được UNESCO ghi vào Danh sách Di sản thế giới trong khuôn khổ 'Công viên tự nhiên Cột đá Lena'. Điểm hấp dẫn riêng của Sinsk là sự yên tĩnh, hoang vắng, ít du khách hơn nhiều so với Cột đá Lena, mang lại cảm giác chinh phục thiên nhiên thực thụ. Trong các hang hốc và vách đá ở đây, giới khảo cổ đã phát hiện dấu tích cư trú của con người thời đồ đá mới, đồ đồng, cùng các hình vẽ trên đá cổ. Với những người ưa khám phá, một chuyến du thuyền hoặc chèo thuyền dọc sông Sinyaya để ngắm Cột đá Sinsk là hành trình đầy chất phiêu lưu.",
    [
        "Vách đá vôi kỷ Cambri cao tới 70–110 m dọc sông Sinyaya.",
        "Cùng Cột đá Lena thuộc Di sản thế giới UNESCO 'Công viên Cột đá Lena'.",
        "Hoang sơ, ít du khách, có dấu tích khảo cổ và hình vẽ đá cổ.",
    ],
    p("Điểm thiên nhiên hoang sơ, tiếp cận bằng thuyền theo tour; chủ yếu mùa hè.",
      "Chi phí theo tour du thuyền/chèo thuyền; không có vé lẻ tại chỗ.",
      "Thường là hành trình nhiều ngày kết hợp trên sông.",
      "Mùa hè (tháng 6–9), khi sông thông thuyền.",
      "Xa và hoang vắng, cần đi theo tour có hướng dẫn; chuẩn bị đồ cắm trại, chống muỗi."),
    [
        {"title": "Wikipedia (RU) — Синяя (приток Лены)", "url": "https://ru.wikipedia.org/wiki/Синяя_(приток_Лены)"},
        {"title": "InYakutia — Река Синяя, Синские столбы", "url": "https://www.inyakutia.ru/sights/sinskie-stolby/"},
    ],
    ["other", "nature", "rock-pillars", "unesco", "khangalassky", "sakha"],
    maps_text("Синские столбы", "Хангаласский улус", "Sinsk Pillars", "Yakutia", 61.38284, 126.656618),
))

# 22) Верхоянск — полюс холода -------------------------------------------------------
RECORDS.append(rec(
    "verkhoyansk-pole-of-cold",
    "Thành phố Verkhoyansk – Cực lạnh Bắc bán cầu (Ver-khô-i-an-xk)",
    "Верхоянск (полюс холода)",
    "Verkhoyansk — Pole of Cold",
    ["other", "monument"],
    67.55, 133.383,
    "Bờ phải sông Yana, huyện Verkhoyansky, phía bắc Cộng hoà Sakha (Yakutia), Nga",
    "Thành phố nhỏ nhất nước Nga và là một trong những nơi lạnh nhất địa cầu, từng ghi nhận -67,8°C. Được mệnh danh 'Cực lạnh của Bắc bán cầu', với đài kỷ niệm và biên độ nhiệt khắc nghiệt nhất thế giới.",
    "Verkhoyansk là thành phố cực bắc và nhỏ nhất của Yakutia (dân số chưa tới 800 người), nằm bên bờ phải sông Yana, được thành lập năm 1638 như một đồn lũy Cossack. Nổi tiếng toàn cầu, Verkhoyansk là một trong những nơi lạnh nhất Trái Đất có người sinh sống thường xuyên: năm 1885, tại đây đã ghi nhận nhiệt độ tới -67,8°C, và thành phố thường được gọi là 'Cực lạnh của Bắc bán cầu'. Đáng kinh ngạc hơn, vào năm 2020 Verkhoyansk lại ghi nhận +38°C – mức nhiệt cao kỷ lục ở phía bắc vòng Bắc Cực, khiến nơi đây được sách Kỷ lục Guinness ghi nhận là điểm có biên độ nhiệt lớn nhất thế giới (hơn 105 độ). Verkhoyansk cạnh tranh danh hiệu 'cực lạnh' với làng Oymyakon, và năm 2005 chính quyền đã chính thức trao danh hiệu này cho Verkhoyansk. Thành phố có một đài kỷ niệm (obelisk) dựng năm 1969 nhân 100 năm ngày phát hiện 'Cực lạnh', cùng bảo tàng nhỏ về khí hậu và lịch sử lưu đày. Với du khách ưa mạo hiểm và du lịch Bắc Cực, đặt chân tới Verkhoyansk là một trải nghiệm 'đến tận cùng cái lạnh' đầy tự hào, dù việc đi lại tốn kém và gian nan.",
    [
        "Một trong những nơi lạnh nhất Trái Đất, từng ghi nhận -67,8°C.",
        "Kỷ lục Guinness về biên độ nhiệt lớn nhất thế giới (hơn 105 độ).",
        "Thành phố nhỏ nhất nước Nga, có đài kỷ niệm 'Cực lạnh' dựng năm 1969.",
    ],
    p("Điểm đến vùng sâu Bắc Cực; tiếp cận qua sân bay Batagay rồi đường bộ, chủ yếu theo tour.",
      "Không có vé tham quan; chi phí chủ yếu là di chuyển và tour, khá cao.",
      "Thường là hành trình nhiều ngày.",
      "Mùa đông để trải nghiệm cái lạnh cực đoan; mùa hè dễ đi lại hơn.",
      "Đi lại tốn kém, hạ tầng hạn chế; cần chuẩn bị kỹ và đi theo tour chuyên nghiệp."),
    [
        {"title": "Wikipedia (RU) — Верхоянск", "url": "https://ru.wikipedia.org/wiki/Верхоянск"},
        {"title": "Wikipedia (EN) — Verkhoyansk", "url": "https://en.wikipedia.org/wiki/Verkhoyansk"},
    ],
    ["other", "pole-of-cold", "arctic", "extreme-climate", "verkhoyansk", "sakha"],
    maps_text("Верхоянск", "Республика Саха", "Verkhoyansk", "Sakha Republic", 67.55, 133.383),
))

# 23) Кимберлитовая трубка «Мир» (г. Мирный) ----------------------------------------
RECORDS.append(rec(
    "mir-diamond-mine-mirny",
    "Mỏ kim cương Mir (hố Mirny) (Mia, Mia-nứi)",
    "Кимберлитовая трубка «Мир» (город Мирный)",
    "Mir Diamond Mine (Mirny)",
    ["other"],
    62.528889, 113.992778,
    "Thành phố Mirny, huyện Mirninsky, phía tây Cộng hoà Sakha (Yakutia), Nga",
    "Một trong những hố khai thác nhân tạo lớn nhất thế giới – mỏ kim cương lộ thiên khổng lồ sâu tới hơn 500 m, rộng hơn 1 km. Biểu tượng của ngành công nghiệp kim cương Nga và 'thủ phủ kim cương' Mirny.",
    "Mỏ kim cương Mir (trong tiếng Nga 'Мир' nghĩa là 'hoà bình/thế giới') là một trong những hố khai thác nhân tạo lớn nhất và nổi tiếng nhất hành tinh, nằm ngay tại thành phố Mirny ở phía tây Yakutia. Được phát hiện năm 1955 và bắt đầu khai thác lộ thiên từ năm 1957, mỏ đã tạo nên một cái hố khổng lồ hình phễu sâu tới hơn 500 mét và đường kính hơn 1 km – lớn đến mức không phận phía trên từng bị hạn chế vì các dòng khí xoáy. Trong 44 năm, mỏ Mir đã cung cấp một lượng kim cương khổng lồ, biến Mirny thành 'thủ phủ kim cương' của Liên Xô và nước Nga, và đưa Yakutia trở thành vùng khai thác kim cương hàng đầu thế giới. Việc khai thác lộ thiên dừng lại năm 2001, chuyển sang khai thác hầm lò; ngày nay hố mỏ khổng lồ vẫn là một cảnh tượng gây choáng ngợp, thường được ngắm từ đài quan sát trên miệng hố. Du khách đến Mirny có thể tìm hiểu lịch sử ngành kim cương qua bảo tàng địa phương và chiêm ngưỡng quy mô phi thường của công trình khai khoáng này – một minh chứng cho sức mạnh con người giữa vùng đất băng vĩnh cửu.",
    [
        "Một trong những hố khai thác nhân tạo lớn nhất thế giới (sâu hơn 500 m).",
        "Mỏ kim cương lộ thiên biểu tượng, khai thác 1957–2001.",
        "Gắn với 'thủ phủ kim cương' Mirny và ngành kim cương hàng đầu của Nga.",
    ],
    p("Ngắm hố mỏ từ đài quan sát/điểm nhìn trên miệng hố; khu mỏ không cho vào tự do.",
      "Không có vé lẻ vào mỏ; tham quan điểm nhìn miễn phí hoặc theo tour có tổ chức.",
      "Khoảng 30–60 phút tại điểm ngắm.",
      "Quanh năm; mùa hè dễ đi lại hơn.",
      "Đến Mirny bằng máy bay; khu vực mỏ có quy định an ninh, nên đi theo tour địa phương."),
    [
        {"title": "Wikipedia (RU) — Мир (кимберлитовая трубка)", "url": "https://ru.wikipedia.org/wiki/Мир_(кимберлитовая_трубка)"},
        {"title": "Wikipedia (EN) — Mir mine", "url": "https://en.wikipedia.org/wiki/Mir_mine"},
    ],
    ["other", "diamond-mine", "mirny", "industry", "kimberlite", "sakha"],
    maps_text("Кимберлитовая трубка Мир", "Мирный", "Mir Diamond Mine", "Mirny", 62.528889, 113.992778),
))

# 24) Черкёхский музей «Якутская политическая ссылка» (под открытым небом) -----------
RECORDS.append(rec(
    "cherkyokh-open-air-museum",
    "Bảo tàng ngoài trời Cherkyokh 'Lưu đày chính trị Yakut' (Trê-ki-ốkh)",
    "Черкёхский историко-мемориальный музей «Якутская политическая ссылка»",
    "Cherkyokh Open-Air Museum 'Yakut Political Exile'",
    ["museum"],
    62.187298, 133.244013,
    "Làng Cherkyokh, huyện Tattinsky (Tatta), Cộng hoà Sakha (Yakutia), Nga",
    "Bảo tàng lịch sử - dân tộc học ngoài trời đầu tiên của Yakutia, tái hiện kiến trúc gỗ truyền thống và câu chuyện những người bị lưu đày chính trị. Quần thể hơn 20 công trình gỗ bên bờ sông Tatta.",
    "Bảo tàng Cherkyokh mang tên 'Lưu đày chính trị Yakut' là bảo tàng lịch sử - dân tộc học ngoài trời đầu tiên trên đất Cộng hoà Sakha, nằm ở làng Cherkyokh thuộc huyện Tattinsky – vùng đất được xem là 'cái nôi văn hoá' của người Yakut, quê hương của nhiều nhà văn, trí thức nổi tiếng. Được xây dựng theo ý tưởng của nhà văn - nhà hoạt động văn hoá Suorun Omolloon, bảo tàng trải rộng trên hơn 11 hecta bên bờ sông Tatta, gồm hơn 20 công trình: những ngôi nhà gỗ (yurt), lều truyền thống, nhà nguyện, cối xay và các di tích kiến trúc gỗ quý của người Yakut thế kỷ 19–20, trong đó có cả các bản sao nơi ở của những người từng bị chính quyền Nga hoàng lưu đày tới vùng đất xa xôi này. Qua đó, bảo tàng kể hai câu chuyện đan xen: đời sống, phong tục truyền thống của người Sakha, và lịch sử bi tráng của phong trào lưu đày chính trị ở Siberia. Không gian mộc mạc, giàu chất sử thi giữa thiên nhiên phương Bắc khiến nơi đây trở thành một điểm đến độc đáo, giúp du khách chạm tới cả bản sắc dân tộc lẫn ký ức lịch sử của Yakutia.",
    [
        "Bảo tàng ngoài trời đầu tiên của Yakutia, quần thể hơn 20 công trình gỗ.",
        "Tái hiện kiến trúc gỗ truyền thống của người Yakut thế kỷ 19–20.",
        "Kể câu chuyện phong trào lưu đày chính trị bên bờ sông Tatta.",
    ],
    p("Thường mở cửa ban ngày; nên liên hệ đặt trước, nhất là ngoài mùa hè.",
      "Vé vào cửa ở mức phải chăng; có thể thuê hướng dẫn.",
      "Khoảng 1,5–2 giờ.",
      "Mùa hè (tháng 6–8), thời tiết dễ chịu để đi ngoài trời.",
      "Cách Yakutsk khá xa (huyện Tattinsky); nên đi theo tour/xe riêng và hỏi trước giờ mở cửa."),
    [
        {"title": "Culture.ru — Черкёхский музей «Якутская политическая ссылка»", "url": "https://www.culture.ru/institutes/81875/cherkekhskii-istoriko-memorialnyi-muzei-yakutskaya-politicheskaya-ssylka"},
        {"title": "Tonkosti — Якутия (Черкех, музей «Якутская политическая ссылка»)", "url": "https://tonkosti.ru/Якутия"},
    ],
    ["museum", "open-air", "wooden-architecture", "political-exile", "tattinsky", "sakha"],
    maps_text("Черкёхский музей Якутская политическая ссылка", "Черкёх", "Cherkyokh Open-Air Museum", "Cherkyokh", 62.187298, 133.244013),
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
