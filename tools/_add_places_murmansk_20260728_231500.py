# -*- coding: utf-8 -*-
"""_add_places_murmansk_20260728_231500.py — VÙNG: Tỉnh Murmansk (Мурманская область)
(lần chạy tự động 2026-07-28).

Bối cảnh: murmansk.json hiện có 7 địa điểm (Teriberka, dãy Khibiny, Kirovsk — Làng Tuyết & Vườn
thực vật Cực–Núi cao, Murmansk — 'Alyosha' & tàu phá băng nguyên tử 'Lenin', Lovozero–Seydozero,
Giếng khoan siêu sâu Kola, đài ngắm Abram-Mys). Bổ sung 24 địa điểm THẬT SỰ nổi tiếng/đặc sắc
CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31. TRÁNH trùng 7 điểm trên.

LƯU Ý CHỐNG TRÙNG: tàu phá băng nguyên tử 'Lenin' và tượng đài 'Alyosha' ĐÃ CÓ (slug
murmansk-alyosha-lenin-icebreaker) → KHÔNG thêm lại. Vườn thực vật Cực–Núi cao & khu trượt tuyết
Bolshoy Vudyavr đã nằm trong bản ghi Kirovsk/Khibiny → KHÔNG tách riêng. Thác Batareysky đã được
mô tả trong bản ghi Teriberka → KHÔNG tách riêng.

Phân bố loại hình (24 bản ghi mới):
- museum (6): краеведческий музей, художественный музей, Военно-морской музей Северного флота,
  Музей ВВС Северного флота (Сафоново), подводная лодка-музей К-21 (Североморск), геологический
  музей им. Белькова (Апатиты).
- church (6): Спас-на-водах (Мурманск), Свято-Никольский кафедральный собор (Мурманск),
  Благовещенский собор (Кола), собор Вознесения Господня (Мончегорск), Трифонов Печенгский
  монастырь (Луостари), Успенская церковь (Варзуга).
- monument (5): Мемориал морякам, погибшим в мирное время (маяк + рубка «Курск»), памятник коту
  Семёну, мемориал «Долина Славы», каменный лабиринт «Вавилон» (+other), памятник Кириллу и
  Мефодию.
- square_street (1): площадь Пять Углов.
- theatre (1): Мурманский областной драматический театр.
- park_garden/other (5): Лапландский заповедник, Кандалакшский заповедник, озеро Имандра,
  полуостров Рыбачий, Мурманский океанариум.

TOẠ ĐỘ — xác minh chéo (2GIS og:image center=lon,lat & URL «Маршрут»; Yandex org ll=; sobory.ru
mục «Координаты»; ru.wikipedia geohack; culture.ru, 2026-07-28). Phạm vi Murmansk lat ~66–70,
lon ~28–41 — tất cả toạ độ trong phạm vi, KHÔNG đảo lat/lon:
  Краеведческий 68.973926,33.086506 (2GIS, Ленина 90); Художественный 68.972828,33.075918 (2GIS,
  Коминтерна 13); Военно-морской СФ 69.024742,33.080355 (2GIS, Торцева 15); Музей ВВС Сафоново
  69.037217,33.292926 (Yandex org); К-21 Североморск 69.080912,33.433095 (Yandex org); Геол.музей
  Апатиты 67.568056,33.405000 (culture.ru/wiki, Ферсмана 14); Спас-на-водах 68.987080,33.094020
  (sobory + Yandex org); Никольский собор 68.943380,33.068950 (sobory/2GIS, Зелёная 11);
  Благовещенский Кола 68.881710,33.020600 (sobory); Вознесенский Мончегорск 67.926475,32.963404
  (sobory, Красноармейская 15А); Печенгский монастырь Луостари 69.427128,31.057227 (sobory);
  Успенская Варзуга 66.395132,36.589799 (sobory); Маяк-мемориал морякам 68.985451,33.093908
  (Yandex org); Кот Семён 68.994223,33.094419 (2GIS, Семёновское озеро); Долина Славы
  69.310417,32.204498 (2GIS/Yandex org, Р-21 ~74 км); Лабиринт «Вавилон» 67.116289,32.480489
  (2GIS/Yandex org, устье Нивы); Кирилл и Мефодий 68.970016,33.086706 (wiki, С.Перовской);
  Пять Углов 68.970671,33.074928 (2GIS центр); Драмтеатр 68.961613,33.074422 (2GIS, Ленина 49);
  Лапландский заповедник (Чунозерская усадьба) 67.624239,32.712532 (esosedi/laplandzap);
  Кандалакшский заповедник (управление) 67.133076,32.417749 (2GIS, Линейная 35); озеро Имандра
  67.836822,33.221112 (точка на озере); мыс Немецкий (п-ов Рыбачий) 69.951944,31.940556 (wiki);
  Океанариум 68.994705,33.089676 (Героев-Североморцев 4).

GHI CHÚ: đã BỎ QUA/không tách các đối tượng trùng hoặc chồng lấn: tàu 'Lenin' & 'Alyosha' (ĐÃ CÓ),
Полярно-альпийский ботанический сад & горнолыжный курорт «Большой Вудъявр» (đã gộp trong
Kirovsk/Khibiny), водопад Батарейский (đã mô tả trong Teriberka), Семёновское озеро như bản ghi
riêng (đã có океанариум + памятник коту Семёну + Спас-на-водах + маяк-мемориал quanh cùng hồ → gộp).
KHÔNG bịa toạ độ. Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn).

Chạy:  python3 tools/_add_places_murmansk_20260728_231500.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "murmansk"
REGION_NAME_VI = "Tỉnh Murmansk"
FD = "Vùng Tây Bắc"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def maps_org(yandex_org_url, name_en, city_en):
    """Link bản đồ ưu tiên URL tổ chức (org) THẲNG tới địa điểm trên Yandex Maps."""
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

# 1) Мурманский областной краеведческий музей -------------------------------------
RECORDS.append(rec(
    "murmansk-regional-museum",
    "Bảo tàng Địa phương học tỉnh Murmansk (Kra-ve-đtre-xki)",
    "Мурманский областной краеведческий музей",
    "Murmansk Regional Museum of Local Lore",
    ["museum"],
    68.973926, 33.086506,
    "Đại lộ Lenina 90, thành phố Murmansk, tỉnh Murmansk, Nga",
    "Bảo tàng lâu đời nhất tỉnh Murmansk (thành lập 1926), kể trọn câu chuyện về thiên nhiên, lịch sử và con người bán đảo Kola. Điểm nhấn hiếm có là 'khu rừng cực' phát quang và bộ sưu tập khoáng vật, động vật vùng Bắc Cực.",
    "Bảo tàng Địa phương học tỉnh Murmansk là bảo tàng lâu đời và lớn nhất vùng, ra đời năm 1926 khi thành phố cảng còn rất trẻ. Ba tầng trưng bày dẫn du khách đi từ địa chất và thiên nhiên bán đảo Kola — với những mẫu khoáng vật lấp lánh, mô hình lãnh nguyên, taiga và thế giới biển Barents — đến khảo cổ, dân tộc học của người Sami bản địa và lịch sử khai phá vùng cực. Một phần quan trọng dành cho thời Chiến tranh Vệ quốc Vĩ đại, khi Murmansk là điểm cuối của các đoàn tàu tiếp tế Bắc Cực (Arctic Convoys) và chịu những trận không kích dữ dội. Bảo tàng nổi tiếng với khối đá 'gỗ hoá thạch' và bộ sưu tập khoáng vật huỳnh quang phát sáng dưới đèn cực tím — một trải nghiệm thị giác đặc biệt phản ánh sự giàu có địa chất của Khibiny và Kola. Nằm ngay trên đại lộ Lenina trung tâm, đây là điểm khởi đầu lý tưởng để hiểu vùng đất Bắc Cực trước khi khám phá các địa danh xa hơn.",
    [
        "Bảo tàng lâu đời nhất tỉnh Murmansk (1926), ba tầng về thiên nhiên, lịch sử, dân tộc học Kola.",
        "Bộ sưu tập khoáng vật huỳnh quang phát sáng và 'gỗ hoá thạch' độc đáo.",
        "Trưng bày sâu về các đoàn tàu tiếp tế Bắc Cực và Murmansk thời Thế chiến II.",
    ],
    p("Thường mở thứ Tư–Chủ nhật, khoảng 11:00–18:00; nghỉ thứ Hai, thứ Ba (nên kiểm tra trước).",
      "Vé vào cửa ở mức phải chăng; có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm; hợp cả những ngày Bắc Cực lạnh giá hay bão tuyết.",
      "Nằm trên đại lộ Lenina, dễ đi bộ kết hợp quảng trường Pyat Uglov và Bảo tàng Mỹ thuật gần đó. Thuyết minh chủ yếu bằng tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Мурманский областной краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Мурманский_областной_краеведческий_музей"},
        {"title": "Culture.ru — Мурманский областной краеведческий музей", "url": "https://www.culture.ru/institutes/11653/murmanskii-oblastnoi-kraevedcheskii-muzei"},
    ],
    ["museum", "history", "murmansk", "arctic", "local-lore", "minerals"],
    maps_text("Мурманский областной краеведческий музей", "Мурманск", "Murmansk Regional Museum", "Murmansk", 68.973926, 33.086506),
))

# 2) Мурманский областной художественный музей ------------------------------------
RECORDS.append(rec(
    "murmansk-art-museum",
    "Bảo tàng Mỹ thuật tỉnh Murmansk",
    "Мурманский областной художественный музей",
    "Murmansk Regional Art Museum",
    ["museum"],
    68.972828, 33.075918,
    "Phố Kominterna 13, thành phố Murmansk, tỉnh Murmansk, Nga",
    "Bảo tàng mỹ thuật duy nhất của tỉnh, đặt trong toà nhà gạch cổ nhất còn lại ở Murmansk (năm 1927). Bộ sưu tập tập trung vào nghệ thuật vùng cực: tranh phong cảnh Bắc Cực, đề tài biển và cuộc sống người phương Bắc.",
    "Bảo tàng Mỹ thuật tỉnh Murmansk là bảo tàng nghệ thuật chuyên biệt duy nhất của vùng, khai trương năm 1989 trong một trong những công trình gạch lâu đời nhất thành phố — toà nhà từng là cửa hàng thương mại quân đội xây năm 1927, nay là di tích kiến trúc. Bộ sưu tập giới thiệu hội hoạ, đồ hoạ và điêu khắc Nga từ thế kỷ 18 đến đương đại, nhưng linh hồn của bảo tàng là dòng nghệ thuật phương Bắc: những bức tranh khắc hoạ ánh sáng địa cực, biển Barents, đội tàu đánh cá, lãnh nguyên phủ tuyết và đời sống người Sami. Nhiều tác phẩm do các hoạ sĩ gắn bó với Murmansk sáng tác, phản ánh vẻ đẹp khắc nghiệt mà nên thơ của xứ Bắc Cực. Bảo tàng còn có khu trưng bày nghệ thuật trang trí, thuỷ tinh nghệ thuật và tổ chức triển lãm luân phiên. Với vị trí trung tâm, đây là điểm dừng văn hoá tinh tế, bổ sung góc nhìn nghệ thuật cho hành trình khám phá thành phố cảng.",
    [
        "Bảo tàng mỹ thuật duy nhất của tỉnh, trong toà nhà gạch cổ nhất Murmansk (1927).",
        "Bộ sưu tập đậm chất phương Bắc: tranh phong cảnh Bắc Cực, biển và đời sống Sami.",
        "Có khu nghệ thuật trang trí, thuỷ tinh nghệ thuật và triển lãm luân phiên.",
    ],
    p("Thường mở thứ Tư–Chủ nhật, khoảng 11:00–18:00; nghỉ thứ Hai, thứ Ba (nên kiểm tra trước).",
      "Vé vào cửa phải chăng; ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; hợp ngày thời tiết xấu.",
      "Ở trung tâm, gần Bảo tàng Địa phương học và quảng trường Pyat Uglov. Chú thích chủ yếu bằng tiếng Nga; nên xem lịch triển lãm tạm thời."),
    [
        {"title": "Wikipedia (RU) — Мурманский областной художественный музей", "url": "https://ru.wikipedia.org/wiki/Мурманский_областной_художественный_музей"},
        {"title": "Culture.ru — Мурманский областной художественный музей", "url": "https://www.culture.ru/institutes/11655/murmanskii-oblastnoi-khudozhestvennyi-muzei"},
    ],
    ["museum", "art", "murmansk", "arctic", "painting", "culture"],
    maps_text("Мурманский областной художественный музей", "Мурманск", "Murmansk Regional Art Museum", "Murmansk", 68.972828, 33.075918),
))

# 3) Военно-морской музей Северного флота ------------------------------------------
RECORDS.append(rec(
    "northern-fleet-naval-museum",
    "Bảo tàng Hải quân Hạm đội Phương Bắc (Mua-man)",
    "Военно-морской музей Северного флота",
    "Naval Museum of the Northern Fleet",
    ["museum"],
    69.024742, 33.080355,
    "Phố Aleksandra Tortseva 15, thành phố Murmansk, tỉnh Murmansk, Nga",
    "Bảo tàng chuyên đề về Hạm đội Phương Bắc — lực lượng hải quân trấn giữ Bắc Cực của Nga. Trưng bày mô hình tàu chiến, tàu ngầm, vũ khí, quân kỳ và hiện vật gắn với những trận hải chiến khốc liệt thời Thế chiến II.",
    "Bảo tàng Hải quân Hạm đội Phương Bắc, thành lập năm 1946, là nơi lưu giữ ký ức về lực lượng hải quân bảo vệ vùng cực và Tuyến đường Biển Bắc của nước Nga. Qua hàng chục nghìn hiện vật, du khách theo dòng lịch sử từ những ngày đầu lập hạm đội, chiến công của các thuỷ thủ và tàu ngầm trong Chiến tranh Vệ quốc Vĩ đại — khi Hạm đội Phương Bắc hộ tống các đoàn tàu tiếp tế Đồng minh và ngăn chặn hải quân đối phương ở biển Barents — đến thời kỳ tàu ngầm nguyên tử và chinh phục Bắc Cực. Các gian trưng bày đầy mô hình chiến hạm, tàu ngầm, ngư lôi, vũ khí, đồng phục, cờ hiệu, hải đồ cùng những kỷ vật cá nhân của thuỷ thủ. Nhiều hiện vật kể lại các chiến dịch nổi tiếng và những con người anh hùng của phương Bắc. Đây là điểm đến hấp dẫn cho người yêu lịch sử quân sự và hàng hải, giúp hiểu vì sao Murmansk gắn bó máu thịt với biển và hạm đội.",
    [
        "Bảo tàng chuyên đề về Hạm đội Phương Bắc (thành lập 1946).",
        "Mô hình tàu chiến, tàu ngầm, ngư lôi, vũ khí và kỷ vật thuỷ thủ.",
        "Trưng bày sâu về hải chiến biển Barents và hộ tống đoàn tàu tiếp tế thời Thế chiến II.",
    ],
    p("Thường mở thứ Tư–Chủ nhật (nghỉ đầu tuần); nên gọi hoặc kiểm tra giờ trước khi đến.",
      "Vé vào cửa thấp; ưu đãi cho học sinh, sinh viên; một số ngày ưu tiên quân nhân.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm.",
      "Nằm ở khu phía bắc thành phố (quận Rosta), nên đi taxi hoặc xe buýt. Thuyết minh chủ yếu bằng tiếng Nga; có thể mang giấy tờ tuỳ thân theo quy định."),
    [
        {"title": "Wikipedia (RU) — Военно-морской музей Северного флота", "url": "https://ru.wikipedia.org/wiki/Военно-морской_музей_Северного_флота"},
        {"title": "Culture.ru — Военно-морской музей Северного флота", "url": "https://www.culture.ru/institutes/11660/voenno-morskoi-muzei-severnogo-flota"},
    ],
    ["museum", "navy", "military", "murmansk", "wwii", "history"],
    maps_text("Военно-морской музей Северного флота", "Мурманск", "Naval Museum of the Northern Fleet", "Murmansk", 69.024742, 33.080355),
))

# 4) Музей военно-воздушных сил Северного флота (Сафоново) -------------------------
RECORDS.append(rec(
    "northern-fleet-aviation-museum",
    "Bảo tàng Không quân Hải quân Hạm đội Phương Bắc (Sa-phô-nô-vô)",
    "Музей военно-воздушных сил Северного флота",
    "Northern Fleet Air Force Museum",
    ["museum"],
    69.037217, 33.292926,
    "Làng Safonovo, thành phố đóng kín Severomorsk, tỉnh Murmansk, Nga",
    "Bảo tàng không quân hải quân độc đáo với khu máy bay ngoài trời, đặt tại làng Safonovo gần Severomorsk. Trưng bày tiêm kích, trực thăng, thuỷ phi cơ thật cùng câu chuyện các phi công anh hùng của Hạm đội Phương Bắc.",
    "Bảo tàng Không quân Hải quân Hạm đội Phương Bắc ở làng Safonovo là một trong những bảo tàng hàng không quân sự thú vị nhất miền cực Bắc nước Nga. Ra đời năm 1976, bảo tàng gồm khu nhà trưng bày trong nhà và một sân bay bảo tàng ngoài trời quy tụ hàng loạt máy bay, trực thăng và thuỷ phi cơ thật — từ tiêm kích, cường kích đến máy bay tuần tra biển của không quân hải quân qua nhiều thời kỳ. Điểm nhấn đặc biệt là những hiện vật liên quan tới các phi công anh hùng phương Bắc, trong đó có Boris Safonov — phi công ách chủ bài lừng danh thời Thế chiến II mà làng được đặt theo tên, cùng kỷ vật của phi hành đoàn từng bay hộ tống các đoàn tàu Bắc Cực. Bên trong bảo tàng còn có cả những chiếc máy bay Anh, Mỹ liên quan đến thời kỳ Đồng minh viện trợ. Với người mê hàng không và lịch sử quân sự, đây là điểm đến giàu cảm xúc; du khách nên lưu ý bảo tàng nằm trong khu vực quân sự đóng kín (ZATO) nên cần thu xếp giấy phép trước.",
    [
        "Bảo tàng không quân hải quân với sân bay - bảo tàng ngoài trời nhiều máy bay, trực thăng thật.",
        "Gắn với phi công ách chủ bài Boris Safonov và các phi công anh hùng phương Bắc.",
        "Có hiện vật máy bay Đồng minh (Anh, Mỹ) thời viện trợ Bắc Cực Thế chiến II.",
    ],
    p("Thường mở thứ Tư–Chủ nhật (nghỉ đầu tuần); giờ có thể thay đổi theo mùa.",
      "Vé vào cửa thấp; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 1,5–2 giờ.",
      "Mùa hè, ngày khô ráo để tham quan khu ngoài trời thuận lợi.",
      "Safonovo nằm trong ZATO Severomorsk (khu đóng kín): công dân Nga cần đăng ký, du khách nước ngoài cần giấy phép ra vào — hãy sắp xếp trước qua tour hoặc cơ quan chức năng."),
    [
        {"title": "Wikipedia (RU) — Музей ВВС Северного флота", "url": "https://ru.wikipedia.org/wiki/Музей_ВВС_Северного_флота"},
        {"title": "Yandex Maps — Музей ВВС Северного флота (Сафоново)", "url": "https://yandex.com/maps/org/muzey_voyenno_vozdushnykh_sil_severnogo_flota/126809425302/"},
    ],
    ["museum", "aviation", "navy", "military", "severomorsk", "open-air"],
    maps_org("https://yandex.com/maps/org/muzey_voyenno_vozdushnykh_sil_severnogo_flota/126809425302/",
             "Northern Fleet Air Force Museum", "Safonovo Severomorsk"),
))

# 5) Подводная лодка-музей К-21 (Североморск) --------------------------------------
RECORDS.append(rec(
    "submarine-k21-museum",
    "Tàu ngầm - bảo tàng K-21 (Severomorsk)",
    "Подводная лодка-музей К-21",
    "Submarine Museum K-21",
    ["museum"],
    69.080912, 33.433095,
    "Quảng trường Muzhestva (Dũng cảm), thành phố Severomorsk, tỉnh Murmansk, Nga",
    "Chiếc tàu ngầm huyền thoại K-21 thời Thế chiến II, nay được đặt trên bờ ở Severomorsk và biến thành bảo tàng. Du khách bước vào bên trong thân tàu thật để tận mắt thấy đời sống, vũ khí và khoang chiến đấu của thuỷ thủ tàu ngầm.",
    "K-21 là một trong những tàu ngầm nổi tiếng nhất của Hạm đội Phương Bắc, gắn với chiến công trong Chiến tranh Vệ quốc Vĩ đại — nổi bật là cuộc tấn công táo bạo nhằm vào thiết giáp hạm Tirpitz của hải quân Đức năm 1942 do thuyền trưởng Nikolay Lunin chỉ huy. Sau chiến tranh, con tàu được đưa lên bờ tại Severomorsk (căn cứ chính của Hạm đội Phương Bắc) và mở cửa thành bảo tàng từ năm 1983. Một phần thân tàu được giữ nguyên trạng để du khách chui qua các khoang chật hẹp: khoang ngư lôi, phòng chỉ huy, buồng động cơ, nơi nghỉ của thuỷ thủ — cảm nhận rõ sự khắc nghiệt và tinh thần thép của lính tàu ngầm; phần còn lại là gian trưng bày về lịch sử hạm đội và chiến công của K-21. Đây là bảo tàng dạng 'hiện vật sống' hiếm có, mang lại trải nghiệm rất chân thực. Lưu ý Severomorsk là thành phố quân sự đóng kín (ZATO), nên việc ra vào cần được thu xếp giấy phép trước.",
    [
        "Tàu ngầm thật thời Thế chiến II, gắn với cuộc tấn công thiết giáp hạm Tirpitz (1942).",
        "Du khách vào bên trong các khoang tàu nguyên bản: ngư lôi, chỉ huy, động cơ.",
        "Nằm ở Severomorsk - căn cứ chính của Hạm đội Phương Bắc; mở làm bảo tàng từ 1983.",
    ],
    p("Thường mở thứ Tư–Chủ nhật (nghỉ đầu tuần); giờ có thể thay đổi, nên kiểm tra trước.",
      "Vé vào cửa thấp; ưu đãi cho học sinh, sinh viên và quân nhân.",
      "Khoảng 45–60 phút.",
      "Quanh năm.",
      "Severomorsk là ZATO (khu đóng kín): cần đăng ký/giấy phép ra vào, du khách nước ngoài nên đi theo tour có tổ chức. Khoang tàu chật, thấp - chú ý khi di chuyển."),
    [
        {"title": "Wikipedia (RU) — К-21 (подводная лодка)", "url": "https://ru.wikipedia.org/wiki/К-21_(подводная_лодка)"},
        {"title": "Yandex Maps — Подводная лодка К-21 (Североморск)", "url": "https://yandex.com/maps/org/podvodnaya_lodka_k_21/148516750756/"},
    ],
    ["museum", "submarine", "navy", "military", "severomorsk", "wwii"],
    maps_org("https://yandex.com/maps/org/podvodnaya_lodka_k_21/148516750756/",
             "Submarine Museum K-21", "Severomorsk"),
))

# 6) Геологический музей им. И. В. Белькова (Апатиты) ------------------------------
RECORDS.append(rec(
    "apatity-geology-museum",
    "Bảo tàng Địa chất & Khoáng vật (Apatity)",
    "Геологический музей им. И. В. Белькова",
    "Geological Museum (Apatity)",
    ["museum"],
    67.568056, 33.405000,
    "Phố Fersmana 14, thành phố Apatity, tỉnh Murmansk, Nga (thuộc Viện Địa chất, Trung tâm Khoa học Kola)",
    "Bảo tàng khoáng vật của Viện Địa chất thuộc Trung tâm Khoa học Kola, nơi phô diễn kho báu đá quý và khoáng vật của bán đảo Kola — một trong những vùng giàu khoáng vật bậc nhất thế giới. Có nhiều mẫu khoáng vật lần đầu được phát hiện tại Khibiny.",
    "Bảo tàng Địa chất mang tên I. V. Belkov ở Apatity là điểm đến hấp dẫn cho ai mê khoáng vật và khoa học Trái Đất. Trực thuộc Viện Địa chất của Trung tâm Khoa học Kola (Viện Hàn lâm Khoa học Nga), bảo tàng trưng bày hàng nghìn mẫu vật thu thập từ bán đảo Kola và khối núi Khibiny — vùng đất nổi tiếng chứa hơn một nghìn loài khoáng vật, trong đó nhiều loại lần đầu được khoa học phát hiện chính tại đây. Du khách được chiêm ngưỡng những tinh thể apatit, nepheline, eudialyte (đá 'máu Lapland' đỏ), astrophyllite và vô số khoáng vật quý, rực rỡ sắc màu, cùng bộ mẫu phát quang dưới đèn cực tím. Các gian trưng bày được sắp xếp khoa học theo nhóm khoáng vật và mỏ quặng, giới thiệu cả lịch sử thăm dò địa chất vùng cực — công cuộc gắn với tên tuổi viện sĩ Aleksandr Fersman. Đây là bảo tàng học thuật nhưng dễ tiếp cận, đặc biệt thú vị khi kết hợp cùng chuyến đi Khibiny–Kirovsk gần đó.",
    [
        "Kho khoáng vật của bán đảo Kola - một trong những vùng giàu khoáng vật nhất thế giới.",
        "Nhiều mẫu khoáng vật lần đầu được phát hiện ở Khibiny; bộ mẫu phát quang dưới đèn UV.",
        "Trực thuộc Viện Địa chất, Trung tâm Khoa học Kola; gắn với di sản viện sĩ A. Fersman.",
    ],
    p("Thường mở các ngày trong tuần theo giờ hành chính; nên gọi/đặt trước vì là bảo tàng thuộc viện nghiên cứu.",
      "Vé vào cửa thấp; có thể cần đăng ký trước để có hướng dẫn.",
      "Khoảng 1 giờ.",
      "Quanh năm; dễ kết hợp trong hành trình Apatity - Kirovsk - Khibiny.",
      "Nằm trong toà nhà Viện Địa chất (Ферсмана 14) - hỏi lễ tân về lối vào bảo tàng. Thuyết minh chủ yếu bằng tiếng Nga."),
    [
        {"title": "Culture.ru — Геологический музей (Апатиты)", "url": "https://www.culture.ru/institutes/12120/geologicheskii-muzei"},
        {"title": "Wikipedia (RU) — Геологический институт КНЦ РАН", "url": "https://ru.wikipedia.org/wiki/Геологический_институт_КНЦ_РАН"},
    ],
    ["museum", "geology", "minerals", "apatity", "khibiny", "science"],
    maps_text("Геологический музей", "Апатиты", "Geological Museum", "Apatity", 67.568056, 33.405000),
))

# ============================ NHÀ THỜ / TU VIỆN (church) ============================

# 7) Церковь Спаса Нерукотворного Образа («Спас-на-водах») -------------------------
RECORDS.append(rec(
    "spas-na-vodakh-church",
    "Nhà thờ Đấng Cứu Thế trên Sóng nước 'Spas-na-Vodakh' (Mua-man)",
    "Церковь Спаса Нерукотворного Образа («Спас-на-водах»)",
    "Church of the Saviour on the Waters (Spas-na-Vodakh)",
    ["church"],
    68.987080, 33.094020,
    "Đại lộ Geroev-Severomortsev 1, gần hồ Semyonovskoye, thành phố Murmansk, tỉnh Murmansk, Nga",
    "Nhà thờ Chính thống giáo trắng muốt trên đồi cạnh hồ Semyonovskoye, được xây dựng để tưởng nhớ những thuỷ thủ và ngư dân đã bỏ mình trên biển. Đây là ngôi nhà thờ bằng đá đầu tiên trên vùng cao của Murmansk và là biểu tượng tâm linh của thành phố.",
    "Nhà thờ 'Spas-na-Vodakh' (Đấng Cứu Thế trên Sóng nước) là một trong những công trình tâm linh nổi bật nhất Murmansk, dựng nhân dịp thành phố tròn 85 tuổi bằng tiền quyên góp của người dân và khánh thành đầu những năm 2000. Toạ lạc trên một ngọn đồi bên hồ Semyonovskoye, ngôi nhà thờ tường trắng, mái vòm vàng theo phong cách kiến trúc Nga cổ vươn lên nổi bật giữa nền trời phương Bắc, trở thành điểm nhấn của toàn khu tưởng niệm ven hồ. Nhà thờ được xây để tưởng nhớ những thuỷ thủ, ngư dân và người đi biển của vùng cực đã hy sinh — một chủ đề day dứt với thành phố cảng nơi biển vừa nuôi sống vừa lấy đi bao sinh mạng. Kề bên là quần thể tưởng niệm với ngọn hải đăng - đài tưởng niệm 'những người đi biển hy sinh thời bình', chiếc mỏ neo lớn và một phần tháp chỉ huy của tàu ngầm nguyên tử 'Kursk'. Từ khoảng sân nhà thờ, du khách còn được ngắm toàn cảnh hồ nước và một phần thành phố. Đây là nơi vừa thiêng liêng, vừa gợi nhắc mối gắn bó máu thịt của Murmansk với đại dương.",
    [
        "Nhà thờ đá đầu tiên trên vùng cao Murmansk, tường trắng - mái vòm vàng bên hồ Semyonovskoye.",
        "Xây để tưởng nhớ thuỷ thủ, ngư dân vùng cực đã hy sinh trên biển.",
        "Kề khu tưởng niệm có hải đăng, mỏ neo và tháp chỉ huy tàu ngầm 'Kursk'.",
    ],
    p("Mở cửa hằng ngày theo lịch phụng vụ, thường giờ lễ sáng và chiều; khuôn viên ngoài trời vào tự do.",
      "Vào cửa tự do (miễn phí); tuỳ tâm quyên góp.",
      "Khoảng 30–45 phút (kể cả khu tưởng niệm ven hồ).",
      "Quanh năm; mùa đông có thể kết hợp ngắm cực quang trên hồ Semyonovskoye.",
      "Trang phục kín đáo, nữ nên mang khăn trùm đầu. Kết hợp thăm khu tưởng niệm hải đăng, mỏ neo và tháp 'Kursk' ngay bên cạnh."),
    [
        {"title": "Wikipedia (RU) — Спас-на-Водах (Мурманск)", "url": "https://ru.wikipedia.org/wiki/Спас-на-Водах_(Мурманск)"},
        {"title": "Sobory.ru — Церковь Спаса Нерукотворного Образа (Мурманск)", "url": "https://sobory.ru/article/?object=03405"},
    ],
    ["church", "orthodox", "murmansk", "memorial", "arctic"],
    maps_org("https://yandex.ru/maps/org/tserkov_spasa_preobrazheniya_na_vodakh/1032161599/",
             "Church of the Saviour on the Waters", "Murmansk"),
))

# 8) Свято-Никольский кафедральный собор (Мурманск) -------------------------------
RECORDS.append(rec(
    "st-nicholas-cathedral-murmansk",
    "Thánh đường Thánh Nikolai (Nhà thờ chính toà Murmansk)",
    "Свято-Никольский кафедральный собор",
    "St. Nicholas Cathedral (Murmansk)",
    ["church"],
    68.943380, 33.068950,
    "Phố Zelyonaya 11, thành phố Murmansk, tỉnh Murmansk, Nga",
    "Nhà thờ chính toà của giáo phận Murmansk, dâng kính Thánh Nikolai — vị thánh bảo trợ người đi biển. Quần thể nhà thờ trắng - vàng bề thế trên một ngọn đồi là trung tâm đời sống Chính thống giáo của thành phố cảng Bắc Cực.",
    "Thánh đường Thánh Nikolai là nhà thờ chính toà (kafedralny sobor) của giáo phận Murmansk, được xây dựng những năm 1980 và trở thành trung tâm tôn giáo lớn nhất thành phố. Dâng kính Thánh Nikolai — vị thánh được người đi biển khắp thế giới tôn làm đấng bảo trợ, điều rất ý nghĩa với một hải cảng như Murmansk. Quần thể toạ lạc trên đồi ở khu phía nam thành phố, gồm nhà thờ chính với năm mái vòm, nhà thờ nhỏ dâng kính Thánh Trifon vùng Pechenga, nhà nguyện, cùng các công trình hành chính và trường học Chủ nhật của giáo phận. Kiến trúc trắng chủ đạo điểm mái vòm vàng, bên trong là bàn thờ chạm khắc, tranh thánh (icon) và không gian phụng vụ trang nghiêm. Đây là nơi diễn ra các đại lễ Chính thống giáo, thu hút đông tín đồ vào dịp Giáng sinh, Phục sinh và ngày lễ Thánh Nikolai. Với du khách, nhà thờ là điểm dừng để cảm nhận chiều sâu tâm linh và tìm hiểu vai trò của Chính thống giáo trong đời sống người dân phương Bắc.",
    [
        "Nhà thờ chính toà của giáo phận Murmansk, dâng kính Thánh Nikolai - đấng bảo trợ người đi biển.",
        "Quần thể trên đồi gồm nhà thờ chính năm vòm, nhà thờ Thánh Trifon Pechenga và trường Chủ nhật.",
        "Trung tâm các đại lễ Chính thống giáo lớn nhất thành phố (Giáng sinh, Phục sinh).",
    ],
    p("Mở cửa hằng ngày, thường khoảng 7:30–20:30; các lễ vào giờ phụng vụ sáng và chiều.",
      "Vào cửa tự do (miễn phí); tuỳ tâm quyên góp.",
      "Khoảng 30–45 phút.",
      "Quanh năm; đông và trang trọng nhất vào các dịp đại lễ.",
      "Trang phục kín đáo, nữ mang khăn trùm đầu; hạn chế chụp ảnh trong giờ lễ. Nằm ở khu phía nam, nên đi taxi hoặc xe buýt."),
    [
        {"title": "Wikipedia (RU) — Свято-Никольский кафедральный собор (Мурманск)", "url": "https://ru.wikipedia.org/wiki/Свято-Никольский_кафедральный_собор_(Мурманск)"},
        {"title": "Sobory.ru — Мурманск, Николая Чудотворца, кафедральный собор", "url": "https://sobory.ru/article/?object=13634"},
    ],
    ["church", "orthodox", "cathedral", "murmansk", "religion"],
    maps_text("Свято-Никольский кафедральный собор", "Мурманск", "St. Nicholas Cathedral", "Murmansk", 68.943380, 33.068950),
))

# 9) Благовещенский собор (Кола) --------------------------------------------------
RECORDS.append(rec(
    "kola-annunciation-cathedral",
    "Nhà thờ Truyền Tin ở Kola - nhà thờ đá cổ nhất bán đảo",
    "Благовещенский собор (Кола)",
    "Annunciation Cathedral (Kola)",
    ["church"],
    68.881710, 33.020600,
    "Đại lộ Zashchitnikov Zapolyarya 8, thành phố Kola, tỉnh Murmansk, Nga",
    "Nhà thờ Truyền Tin ở thị trấn cổ Kola là công trình bằng đá lâu đời nhất trên toàn bán đảo Kola (đầu thế kỷ 19). Đây là di tích quý giá, chứng nhân cho lịch sử hàng trăm năm của vùng cực trước khi Murmansk ra đời.",
    "Nằm ở thị trấn Kola — khu định cư cổ từng là trung tâm hành chính của cả vùng cực trước khi Murmansk được lập năm 1916 — Nhà thờ Truyền Tin (Blagoveshchensky) là công trình bằng đá cổ nhất còn tồn tại trên bán đảo Kola. Được khởi công cuối thế kỷ 18 và hoàn thành đầu thế kỷ 19, nhà thờ đánh dấu bước chuyển từ các thánh đường gỗ sang kiến trúc đá bền vững ở một vùng đất khắc nghiệt và hẻo lánh. Trải qua nhiều biến động — chiến tranh, thời kỳ đóng cửa các nhà thờ dưới thời Xô Viết — công trình vẫn được gìn giữ và phục hồi, nay là di tích lịch sử - kiến trúc cấp liên bang và đang hoạt động trở lại như một nhà thờ. Bên trong lưu giữ những di vật gắn với lịch sử Chính thống giáo lâu đời của phương Bắc. Với du khách, ghé Kola và nhà thờ Truyền Tin là dịp chạm vào lớp lịch sử sâu hơn của bán đảo — nơi con người đã sống, cầu nguyện và bám trụ ở rìa Bắc Cực từ nhiều thế kỷ trước.",
    [
        "Công trình bằng đá cổ nhất còn lại trên bán đảo Kola (đầu thế kỷ 19).",
        "Ở thị trấn Kola - trung tâm hành chính vùng cực trước khi Murmansk ra đời (1916).",
        "Di tích lịch sử - kiến trúc cấp liên bang, nay hoạt động trở lại làm nhà thờ.",
    ],
    p("Mở cửa theo lịch phụng vụ, thường giờ lễ sáng và chiều; ngoài giờ có thể liên hệ trước.",
      "Vào cửa tự do (miễn phí); tuỳ tâm quyên góp.",
      "Khoảng 30 phút.",
      "Quanh năm.",
      "Kola cách trung tâm Murmansk khoảng 12 km, dễ đi bằng xe buýt hoặc taxi. Trang phục kín đáo, nữ mang khăn trùm đầu."),
    [
        {"title": "Wikipedia (RU) — Благовещенская церковь (Кола)", "url": "https://ru.wikipedia.org/wiki/Благовещенская_церковь_(Кола)"},
        {"title": "Sobory.ru — Кола, Благовещения Пресвятой Богородицы, собор", "url": "https://sobory.ru/article/?object=03486"},
    ],
    ["church", "orthodox", "kola", "historic", "landmark"],
    maps_text("Благовещенский собор", "Кола", "Annunciation Cathedral", "Kola", 68.881710, 33.020600),
))

# 10) Собор Вознесения Господня (Мончегорск) --------------------------------------
RECORDS.append(rec(
    "monchegorsk-ascension-cathedral",
    "Nhà thờ Chúa Thăng Thiên (Monchegorsk)",
    "Собор Вознесения Господня (Мончегорск)",
    "Cathedral of the Ascension (Monchegorsk)",
    ["church"],
    67.926475, 32.963404,
    "Phố Krasnoarmeyskaya 15А, thành phố Monchegorsk, tỉnh Murmansk, Nga",
    "Nhà thờ chính của thành phố công nghiệp Monchegorsk, với kiến trúc trắng - vòm vàng theo phong cách Nga cổ. Đây là một trong những thánh đường đẹp và bề thế nhất tỉnh Murmansk, điểm nhấn tâm linh giữa vùng lãnh nguyên.",
    "Nhà thờ Chúa Thăng Thiên là công trình tôn giáo trung tâm của Monchegorsk — thành phố mọc lên từ giữa thế kỷ 20 quanh tổ hợp luyện kim màu Severonickel, giữa khung cảnh núi non và hồ Imandra. Được xây dựng vào cuối những năm 1990 và hoàn thiện đầu thế kỷ 21, nhà thờ mang dáng dấp kiến trúc Nga cổ truyền thống: khối tường trắng, những mái vòm dát vàng lấp lánh và tháp chuông vươn cao, trở thành một trong những thánh đường bề thế và ưa nhìn nhất vùng Murmansk. Bên trong là không gian phụng vụ trang nghiêm với tranh thánh và bàn thờ chạm khắc. Sự hiện diện của một nhà thờ đẹp giữa thành phố công nghiệp phương Bắc mang ý nghĩa đặc biệt, như biểu tượng của đời sống tinh thần bên cạnh lao động khắc nghiệt nơi vùng cực. Nhà thờ nằm ở khu trung tâm Monchegorsk, thuận tiện ghé thăm khi trên đường tới Lapland — khu bảo tồn thiên nhiên nổi tiếng gần đó, hoặc trong hành trình khám phá vùng Khibiny - Imandra.",
    [
        "Nhà thờ chính của Monchegorsk, kiến trúc Nga cổ tường trắng - vòm vàng bề thế.",
        "Một trong những thánh đường đẹp nhất tỉnh Murmansk, điểm nhấn giữa thành phố công nghiệp.",
        "Vị trí thuận tiện gần khu bảo tồn Lapland và vùng hồ Imandra.",
    ],
    p("Mở cửa hằng ngày theo lịch phụng vụ, thường giờ lễ sáng và chiều.",
      "Vào cửa tự do (miễn phí); tuỳ tâm quyên góp.",
      "Khoảng 30 phút.",
      "Quanh năm.",
      "Monchegorsk cách Murmansk khoảng 145 km. Trang phục kín đáo, nữ mang khăn trùm đầu; kết hợp ghé khu bảo tồn Lapland gần đó."),
    [
        {"title": "Wikipedia (RU) — Собор Вознесения Господня (Мончегорск)", "url": "https://ru.wikipedia.org/wiki/Собор_Вознесения_Господня_(Мончегорск)"},
        {"title": "Sobory.ru — Мончегорск, Вознесения Господня, кафедральный собор", "url": "https://sobory.ru/article/?object=25635"},
    ],
    ["church", "orthodox", "cathedral", "monchegorsk", "architecture"],
    maps_text("Собор Вознесения Господня", "Мончегорск", "Cathedral of the Ascension", "Monchegorsk", 67.926475, 32.963404),
))

# 11) Свято-Троицкий Трифонов Печенгский монастырь --------------------------------
RECORDS.append(rec(
    "trifonov-pechenga-monastery",
    "Tu viện Trifonov Pechenga - tu viện cực bắc thế giới (Lu-ô-sta-ri)",
    "Свято-Троицкий Трифонов Печенгский монастырь",
    "Trifonov Pechenga Monastery",
    ["church"],
    69.427128, 31.057227,
    "Làng Luostari, huyện Pechengsky, tỉnh Murmansk, Nga (gần biên giới Na Uy)",
    "Tu viện Chính thống giáo nằm ở cực bắc nhất thế giới, có nguồn gốc từ thế kỷ 16 gắn với Thánh Trifon vùng Pechenga. Ngôi tu viện gỗ được phục dựng giữa lãnh nguyên hoang vắng sát biên giới Na Uy, là chứng nhân của lịch sử truyền giáo phương Bắc.",
    "Tu viện Trifonov Pechenga được xem là tu viện Chính thống giáo nằm ở vị trí cực bắc nhất thế giới. Nền móng lịch sử của nó có từ giữa thế kỷ 16, gắn với Thánh Trifon vùng Pechenga — nhà truyền giáo đã đến vùng đất của người Sami để rao giảng đạo. Trải qua gần năm thế kỷ đầy biến động — các cuộc tập kích, tàn phá (trong đó có vụ thảm sát các tu sĩ năm 1589), di dời, hoả hoạn và thời kỳ đóng cửa dưới chế độ Xô Viết — tu viện nhiều lần bị xoá sổ rồi hồi sinh. Ngôi tu viện ngày nay được phục dựng bằng gỗ theo kiểu truyền thống ở khu vực Luostari những năm đầu thế kỷ 21, sau một trận hoả hoạn, với nhà thờ Ba Ngôi (Troitsky) và các công trình tu hành nép mình giữa lãnh nguyên hoang vắng gần biên giới Na Uy. Không gian tĩnh mịch, xa xôi càng làm nổi bật ý nghĩa tâm linh và sức bền bỉ của đức tin nơi rìa Bắc Cực. Đây là điểm đến đặc biệt cho hành hương và cho du khách muốn chạm tới lớp lịch sử tôn giáo sâu nhất của vùng cực.",
    [
        "Tu viện Chính thống giáo ở vị trí cực bắc nhất thế giới, gốc từ thế kỷ 16.",
        "Gắn với Thánh Trifon vùng Pechenga và lịch sử truyền giáo cho người Sami.",
        "Nhà thờ Ba Ngôi bằng gỗ phục dựng giữa lãnh nguyên gần biên giới Na Uy.",
    ],
    p("Mở cửa theo lịch tu viện và phụng vụ; nên liên hệ trước khi đến vì ở khu vực xa xôi.",
      "Vào cửa tự do (miễn phí); tuỳ tâm quyên góp.",
      "Khoảng 45–60 phút.",
      "Mùa hè (tháng 6–9) đường dễ đi; mùa đông đường tuyết khó khăn.",
      "Nằm ở vùng biên giới hẻo lánh (Luostari, gần Nikel/Zapolyarny): nên đi ô tô gầm cao hoặc theo tour. Trang phục kín đáo; tôn trọng nếp sinh hoạt tu viện."),
    [
        {"title": "Wikipedia (RU) — Трифонов Печенгский монастырь", "url": "https://ru.wikipedia.org/wiki/Трифонов_Печенгский_монастырь"},
        {"title": "Sobory.ru — Луостари, Трифонов Печенгский монастырь", "url": "https://sobory.ru/article/?object=20179"},
    ],
    ["church", "monastery", "orthodox", "pechenga", "arctic", "pilgrimage"],
    maps_text("Свято-Троицкий Трифонов Печенгский монастырь", "Луостари", "Trifonov Pechenga Monastery", "Luostari", 69.427128, 31.057227),
))

# 12) Успенская церковь (Варзуга) -------------------------------------------------
RECORDS.append(rec(
    "varzuga-uspenskaya-church",
    "Nhà thờ gỗ Uspenskaya ở Varzuga (Va-rơ-du-ga)",
    "Успенская церковь (Варзуга)",
    "Assumption Church (Varzuga)",
    ["church"],
    66.395132, 36.589799,
    "Làng Varzuga, huyện Tersky (bờ biển Tersky, Bạch Hải), tỉnh Murmansk, Nga",
    "Kiệt tác kiến trúc gỗ Nga năm 1674: nhà thờ mái chóp (shatyor) cao vút không dùng một chiếc đinh sắt, đứng bên sông ở làng cổ Varzuga. Đây là một trong những công trình gỗ đẹp và quý giá nhất miền Bắc nước Nga.",
    "Nhà thờ Uspenskaya (Đức Mẹ Yên Nghỉ) ở làng Varzuga trên bờ biển Tersky của Bạch Hải là viên ngọc của kiến trúc gỗ Nga phương Bắc. Dựng năm 1674 hoàn toàn bằng gỗ theo kỹ thuật truyền thống — ghép mộng không dùng đinh sắt — nhà thờ có dáng 'shatyor' (mái chóp nhọn) cao khoảng 34 m vươn thẳng lên trời, thân thu nhỏ dần theo tầng, tạo nên vẻ đẹp thanh thoát mà hùng vĩ hiếm thấy. Varzuga là một trong những làng Nga cổ nhất trên bán đảo Kola, hình thành từ thời trung cổ nhờ nghề đánh cá hồi trên sông Varzuga, và cụm nhà thờ gỗ nơi đây (gồm cả nhà thờ Uspenskaya cùng các công trình phụ) là di sản kiến trúc quý giá được bảo tồn. Bên trong còn lưu giữ bức tường tranh thánh (iconostasis) cổ. Đứng bên dòng sông giữa khung cảnh làng quê phương Bắc yên bình, nhà thờ mang đến cảm giác như bước ngược thời gian. Đường tới Varzuga khá xa và hoang sơ, nhưng chính điều đó khiến chuyến đi trở nên đáng nhớ với những ai mê kiến trúc gỗ và văn hoá Nga cổ.",
    [
        "Nhà thờ gỗ mái chóp (shatyor) năm 1674, cao ~34 m, dựng không dùng đinh sắt.",
        "Ở Varzuga - một trong những làng Nga cổ nhất bán đảo Kola, bên bờ Bạch Hải.",
        "Kiệt tác kiến trúc gỗ phương Bắc, còn lưu giữ tường tranh thánh cổ.",
    ],
    p("Mở cửa theo lịch phụng vụ và mùa; ở làng xa nên liên hệ/hỏi trước khi đến.",
      "Vào cửa tự do (miễn phí); tuỳ tâm quyên góp.",
      "Khoảng 30–45 phút (kể cả dạo làng).",
      "Mùa hè (tháng 6–9) khi đường tới bờ Tersky dễ đi và làng đẹp nhất.",
      "Varzuga cách Murmansk khoảng 300 km, đường dài và có đoạn xấu - nên đi ô tô gầm cao hoặc theo tour. Trang phục kín đáo; mang theo đồ ăn, nước vì dịch vụ ít."),
    [
        {"title": "Wikipedia (RU) — Успенская церковь (Варзуга)", "url": "https://ru.wikipedia.org/wiki/Успенская_церковь_(Варзуга)"},
        {"title": "Sobory.ru — Варзуга, Успения Пресвятой Богородицы, церковь", "url": "https://sobory.ru/article/?object=06714"},
    ],
    ["church", "wooden-architecture", "varzuga", "historic", "white-sea", "landmark"],
    maps_text("Успенская церковь", "Варзуга", "Assumption Church", "Varzuga", 66.395132, 36.589799),
))

# ============================ ĐÀI TƯỞNG NIỆM / TƯỢNG (monument) ============================

# 13) Мемориал морякам, погибшим в мирное время (маяк + рубка «Курск») ------------
RECORDS.append(rec(
    "sailors-peacetime-memorial",
    "Đài tưởng niệm thuỷ thủ hy sinh thời bình - Hải đăng & tháp tàu 'Kursk'",
    "Мемориал «Морякам, погибшим в мирное время»",
    "Memorial to Sailors Who Died in Peacetime",
    ["monument"],
    68.985451, 33.093908,
    "Bên hồ Semyonovskoye (khu Verkhne-Rostinskoye), thành phố Murmansk, tỉnh Murmansk, Nga",
    "Quần thể tưởng niệm ven hồ Semyonovskoye gồm một ngọn hải đăng - đài tưởng niệm, chiếc mỏ neo lớn và một phần tháp chỉ huy trục vớt từ tàu ngầm nguyên tử 'Kursk'. Đây là nơi tưởng nhớ các thuỷ thủ Murmansk đã bỏ mình trên biển thời bình.",
    "Trên đồi cao bên hồ Semyonovskoye, đài tưởng niệm 'Những người đi biển hy sinh thời bình' là một trong những công trình gây xúc động nhất Murmansk. Điểm nhấn là một ngọn hải đăng bằng đá cao được dựng làm đài tưởng niệm — bên trong có 'Sổ ký ức' ghi tên những thuỷ thủ, ngư dân của vùng đã tử nạn trên biển ngoài thời chiến. Cạnh đó là chiếc mỏ neo lớn và, đặc biệt, một phần tháp chỉ huy (rubka) được trục vớt từ tàu ngầm nguyên tử 'Kursk' — con tàu gặp thảm hoạ chìm ở biển Barents năm 2000 khiến toàn bộ 118 thuỷ thủ thiệt mạng, một bi kịch để lại nỗi đau sâu sắc trong lòng người dân phương Bắc. Quần thể nằm liền kề nhà thờ 'Spas-na-Vodakh', cùng tạo thành một khu tưởng niệm biển cả trọn vẹn. Từ đây du khách có thể phóng tầm mắt xuống hồ nước và thành phố; về đêm mùa đông, đây cũng là điểm ngắm cực quang. Không gian trầm mặc, thiêng liêng này nhắc nhớ cái giá mà một thành phố biển phải trả, và lòng biết ơn với những người con của đại dương.",
    [
        "Ngọn hải đăng - đài tưởng niệm với 'Sổ ký ức' tên các thuỷ thủ tử nạn thời bình.",
        "Có một phần tháp chỉ huy trục vớt từ tàu ngầm nguyên tử 'Kursk' (thảm hoạ năm 2000).",
        "Liền kề nhà thờ 'Spas-na-Vodakh', hợp thành khu tưởng niệm biển cả bên hồ Semyonovskoye.",
    ],
    p("Ngoài trời, mở tự do; hải đăng - đài tưởng niệm có thể vào trong theo giờ nhất định.",
      "Miễn phí.",
      "Khoảng 30–45 phút (kết hợp nhà thờ 'Spas-na-Vodakh').",
      "Quanh năm; đêm đông có thể ngắm cực quang trên hồ.",
      "Giữ thái độ trang nghiêm; mặc đồ ấm chống gió. Kết hợp thăm nhà thờ 'Spas-na-Vodakh' và khu nghỉ ven hồ Semyonovskoye ngay cạnh."),
    [
        {"title": "Wikipedia (RU) — Мемориал морякам, погибшим в мирное время", "url": "https://ru.wikipedia.org/wiki/Мемориал_морякам,_погибшим_в_мирное_время"},
        {"title": "Yandex Maps — Морякам, погибшим в мирное время (Мурманск)", "url": "https://yandex.com/maps/org/moryakam_pogibshim_v_mirnoye_vremya/29301073759/"},
    ],
    ["monument", "memorial", "murmansk", "navy", "kursk", "sea"],
    maps_org("https://yandex.com/maps/org/moryakam_pogibshim_v_mirnoye_vremya/29301073759/",
             "Memorial to Sailors Who Died in Peacetime", "Murmansk"),
))

# 14) Памятник коту Семёну --------------------------------------------------------
RECORDS.append(rec(
    "cat-semyon-monument",
    "Tượng đài chú mèo Semyon (Xê-mi-ôn)",
    "Памятник коту Семёну",
    "Monument to the Cat Semyon",
    ["monument"],
    68.994223, 33.094419,
    "Bên hồ Semyonovskoye (công viên Naydyonova), thành phố Murmansk, tỉnh Murmansk, Nga",
    "Bức tượng đồng ngộ nghĩnh bên hồ Semyonovskoye tôn vinh chú mèo Semyon - con vật đi lạc đã tự tìm đường về nhà suốt 6 năm, vượt khoảng 2.000 km từ Moskva về Murmansk. Một điểm chụp ảnh dễ thương, được người dân và du khách yêu thích.",
    "Giữa những đài tưởng niệm hùng tráng của thành phố cảng, tượng đài chú mèo Semyon mang đến một câu chuyện ấm áp và đầy cảm hứng. Theo truyền thuyết đô thị được người Murmansk kể lại, vào đầu những năm 1990, một gia đình đi nghỉ ở Moskva đã lạc mất con mèo Semyon; suốt khoảng sáu năm sau đó, chú mèo được cho là đã tự mình băng qua gần 2.000 km đường trường để trở về đúng ngôi nhà của chủ ở Murmansk. Câu chuyện về lòng trung thành và ý chí phi thường ấy đã lay động cộng đồng, và một bức tượng đồng nhỏ hình chú mèo ngồi với chiếc khăn tay buộc thành túi hành lý được dựng bên hồ Semyonovskoye để tôn vinh. Tượng nhanh chóng trở thành 'linh vật' đáng yêu của thành phố, điểm hẹn chụp ảnh và là nơi người ta tin rằng chạm/xoa vào tượng sẽ gặp may mắn. Nằm trong khu công viên nghỉ dưỡng ven hồ, cạnh océanarium và các đài tưởng niệm biển, tượng mèo Semyon là điểm dừng vui vẻ, giàu tính người giữa hành trình khám phá Murmansk.",
    [
        "Tượng đồng tôn vinh chú mèo Semyon tự tìm đường về nhà ~2.000 km từ Moskva.",
        "Biểu tượng dễ thương của Murmansk, điểm chụp ảnh và 'cầu may' được yêu thích.",
        "Nằm trong công viên ven hồ Semyonovskoye, gần océanarium và khu nghỉ.",
    ],
    p("Ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Quanh năm; mùa hè dạo công viên ven hồ dễ chịu nhất.",
      "Kết hợp dạo công viên ven hồ Semyonovskoye, thăm océanarium và các đài tưởng niệm biển gần đó."),
    [
        {"title": "Wikipedia (RU) — Памятник коту Семёну", "url": "https://ru.wikipedia.org/wiki/Памятник_коту_Семёну"},
        {"title": "Culttourism.ru — Памятник коту Семёну (Мурманск)", "url": "https://culttourism.ru/murmanskaya/murmansk/pamyatnik_kotu_semyonu.html"},
    ],
    ["monument", "murmansk", "quirky", "cat", "photo-spot", "park"],
    maps_text("Памятник коту Семёну", "Мурманск", "Monument to the Cat Semyon", "Murmansk", 68.994223, 33.094419),
))

# 15) Мемориал «Долина Славы» -----------------------------------------------------
RECORDS.append(rec(
    "valley-of-glory-memorial",
    "Đài tưởng niệm 'Thung lũng Vinh quang' (Dolina Slavy)",
    "Мемориал «Долина Славы»",
    "Valley of Glory Memorial",
    ["monument"],
    69.310417, 32.204498,
    "Bên đường Р-21 'Kola', khoảng km 74–75, thung lũng sông Zapadnaya Litsa, huyện Kolsky, tỉnh Murmansk, Nga",
    "Khu tưởng niệm chiến tranh lớn giữa lãnh nguyên, tại nơi từng diễn ra những trận đánh ác liệt nhất bảo vệ Murmansk trong Thế chiến II. Từng mang tên 'Thung lũng Tử thần', nay là 'Thung lũng Vinh quang' với các đài, mộ và bia tưởng niệm binh sĩ hy sinh.",
    "Bên đường cao tốc R-21 'Kola' nối Murmansk với biên giới Na Uy, giữa lãnh nguyên hoang vắng bên sông Zapadnaya Litsa, là 'Thung lũng Vinh quang' — một trong những đài tưởng niệm chiến tranh quan trọng nhất tỉnh Murmansk. Chính tại thung lũng này, trong Chiến tranh Vệ quốc Vĩ đại (1941–1944), Hồng quân đã chặn đứng bước tiến của quân đội Đức Quốc xã hướng về Murmansk trong những trận đánh vô cùng khốc liệt; tuyến phòng thủ giữ vững suốt nhiều năm khiến hải cảng chiến lược này không bao giờ thất thủ. Cái giá phải trả là hàng nghìn sinh mạng, vì thế nơi đây ban đầu được gọi là 'Thung lũng Tử thần' (Dolina Smerti), về sau đổi thành 'Thung lũng Vinh quang' để tôn vinh chiến công. Khu tưởng niệm gồm các đài, tượng, bia khắc tên, những ngôi mộ tập thể và khí tài quân sự trưng bày, trải rộng giữa cảnh quan núi non trơ trọi. Vào ngày Chiến thắng 9/5 và các dịp lễ, người dân từ khắp vùng tới đây đặt hoa. Với du khách trên hành trình về phía bắc, đây là điểm dừng đầy xúc động để hiểu vai trò và sự hy sinh của Murmansk trong chiến tranh.",
    [
        "Nơi diễn ra các trận đánh ác liệt chặn quân Đức tiến về Murmansk (1941–1944).",
        "Từng gọi là 'Thung lũng Tử thần', nay là 'Thung lũng Vinh quang' với đài, mộ, bia tưởng niệm.",
        "Nằm giữa lãnh nguyên bên sông Zapadnaya Litsa, cạnh cao tốc R-21 'Kola'.",
    ],
    p("Ngoài trời, mở tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 30–45 phút.",
      "Cuối xuân đến đầu thu (tháng 5–9); đặc biệt trang trọng dịp 9/5.",
      "Nằm cách Murmansk khoảng 70–75 km trên đường R-21, nên đi ô tô. Mặc đồ ấm chống gió; giữ thái độ trang nghiêm."),
    [
        {"title": "Wikipedia (RU) — Долина Славы", "url": "https://ru.wikipedia.org/wiki/Долина_Славы"},
        {"title": "Yandex Maps — Мемориальный комплекс «Долина Славы»", "url": "https://yandex.com/maps/org/memorialny_kompleks_dolina_slavy/4056380224/"},
    ],
    ["monument", "memorial", "wwii", "murmansk", "history", "tundra"],
    maps_org("https://yandex.com/maps/org/memorialny_kompleks_dolina_slavy/4056380224/",
             "Valley of Glory Memorial", "Murmansk Oblast"),
))

# 16) Каменный лабиринт «Вавилон» (Кандалакша) ------------------------------------
RECORDS.append(rec(
    "kandalaksha-labyrinth",
    "Mê cung đá cổ 'Vavilon' ở Kandalaksha (Ma-cung Va-vi-lon)",
    "Каменный лабиринт «Вавилон»",
    "Kandalaksha Stone Labyrinth (Vavilon)",
    ["monument", "other"],
    67.116289, 32.480489,
    "Gần cửa sông Niva, bờ vịnh Kandalaksha (Bạch Hải), thành phố Kandalaksha, tỉnh Murmansk, Nga",
    "Mê cung đá bí ẩn có tuổi hàng nghìn năm, xếp bằng những viên đá cuội thành các vòng xoáy đồng tâm bên bờ Bạch Hải. Đây là một trong những di tích khảo cổ độc đáo nhất phương Bắc, gắn với tín ngưỡng của người cổ đại.",
    "Trên bờ vịnh Kandalaksha thuộc Bạch Hải, gần cửa sông Niva, ẩn mình một di tích khảo cổ kỳ bí: mê cung đá 'Vavilon'. Đây là một labyrinth (vòng mê cung) được người cổ đại xếp bằng những viên đá cuội thành các đường xoáy đồng tâm trên mặt đất, có đường kính khoảng vài chục mét. Những mê cung kiểu này rải rác dọc bờ biển phương Bắc (Kola, Karelia, Scandinavia) và được cho là có niên đại hàng nghìn năm, từ thời đồ đá mới hoặc đồ đồng. Ý nghĩa thật sự của chúng đến nay vẫn là ẩn số: giới nghiên cứu đưa ra nhiều giả thuyết — nơi thực hành nghi lễ, bẫy đánh cá tượng trưng, biểu tượng ranh giới giữa thế giới người sống và người chết, hay công cụ liên quan tín ngưỡng săn bắt. Chính sự huyền bí ấy khiến 'Vavilon' trở nên hấp dẫn. Mê cung nằm trong khung cảnh bờ biển hoang sơ với đá, rêu và nước, gần khu bảo tồn thiên nhiên Kandalaksha. Đến đây, du khách vừa chạm vào một bí ẩn cổ xưa của loài người, vừa tận hưởng vẻ đẹp nguyên sơ của bờ Bạch Hải.",
    [
        "Mê cung đá cổ xếp bằng đá cuội thành vòng xoáy đồng tâm bên bờ Bạch Hải.",
        "Niên đại ước tính hàng nghìn năm (thời đồ đá mới/đồ đồng), ý nghĩa vẫn là ẩn số.",
        "Nằm trong khung cảnh bờ biển hoang sơ, gần khu bảo tồn thiên nhiên Kandalaksha.",
    ],
    p("Ngoài trời, tiếp cận tự do; đi bộ theo đường mòn ven biển từ Kandalaksha.",
      "Miễn phí.",
      "Khoảng 30–45 phút tại chỗ (chưa kể đường đi bộ).",
      "Mùa hè (tháng 6–9) khi đường mòn khô ráo, thuỷ triều thấp dễ quan sát.",
      "Đi giày chắc, chú ý thuỷ triều và địa hình đá trơn; không giẫm xô lệch các viên đá của mê cung để bảo tồn di tích."),
    [
        {"title": "Wikipedia (RU) — Кандалакшский лабиринт", "url": "https://ru.wikipedia.org/wiki/Кандалакшский_лабиринт"},
        {"title": "Yandex Maps — Каменный лабиринт «Вавилон» (Кандалакша)", "url": "https://yandex.com/maps/org/kamenny_labirint_vavilon/67746498826/"},
    ],
    ["monument", "archaeology", "kandalaksha", "ancient", "white-sea", "offbeat"],
    maps_org("https://yandex.com/maps/org/kamenny_labirint_vavilon/67746498826/",
             "Kandalaksha Stone Labyrinth Vavilon", "Kandalaksha"),
))

# 17) Памятник Кириллу и Мефодию --------------------------------------------------
RECORDS.append(rec(
    "cyril-methodius-monument",
    "Tượng đài hai Thánh Kirill và Mefodiy (Ki-rin & Mê-phô-đi)",
    "Памятник Кириллу и Мефодию",
    "Monument to Cyril and Methodius",
    ["monument"],
    68.970016, 33.086706,
    "Phố Sofyi Perovskoy, trước Thư viện Khoa học tỉnh Murmansk, thành phố Murmansk, tỉnh Murmansk, Nga",
    "Tượng đài hai vị thánh Kirill và Mefodiy - những người sáng tạo bảng chữ cái Slav, đặt trước Thư viện Khoa học tỉnh. Đây là bản sao món quà hữu nghị từ Bulgaria và là biểu tượng của văn hoá, chữ viết Slav ở Murmansk.",
    "Trước Thư viện Khoa học tỉnh Murmansk sừng sững tượng đài hai vị thánh Kirill (Cyril) và Mefodiy (Methodius) — hai anh em truyền giáo người Byzantine thế kỷ 9 được tôn vinh là cha đẻ của bảng chữ cái Slav (nền tảng của chữ Kirin/Cyrillic mà tiếng Nga, tiếng Bulgaria và nhiều ngôn ngữ Slav dùng đến nay). Bức tượng ở Murmansk là bản sao của tượng đài nổi tiếng đặt trước Thư viện Quốc gia Bulgaria ở Sofia, được trao tặng như biểu tượng của tình hữu nghị và cội nguồn văn hoá chung giữa các dân tộc Slav. Hai vị thánh được khắc hoạ trang nghiêm, tay nâng cuộn sách và thánh giá, tượng trưng cho tri thức và đức tin. Vị trí trước thư viện khiến tượng đài mang ý nghĩa đặc biệt về giáo dục, chữ viết và văn hoá. Hằng năm vào Ngày Văn tự và Văn hoá Slav (24/5), nơi đây thường diễn ra các sự kiện kỷ niệm. Với du khách, đây là điểm dừng ngắn ở trung tâm để cảm nhận chiều sâu văn hoá Slav trong lòng thành phố Bắc Cực.",
    [
        "Tượng đài hai Thánh Kirill và Mefodiy - cha đẻ bảng chữ cái Slav (chữ Kirin).",
        "Bản sao món quà hữu nghị từ Bulgaria, đặt trước Thư viện Khoa học tỉnh.",
        "Gắn với Ngày Văn tự và Văn hoá Slav (24/5), biểu tượng tri thức và văn hoá.",
    ],
    p("Ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Quanh năm; đặc biệt dịp 24/5 (Ngày Văn tự Slav).",
      "Nằm ở trung tâm, dễ kết hợp dạo đại lộ Lenina và quảng trường Pyat Uglov; ghé Thư viện Khoa học tỉnh ngay sau tượng."),
    [
        {"title": "Wikipedia (RU) — Памятник Кириллу и Мефодию (Мурманск)", "url": "https://ru.wikipedia.org/wiki/Памятник_Кириллу_и_Мефодию_(Мурманск)"},
        {"title": "Culttourism.ru — Памятник Кириллу и Мефодию (Мурманск)", "url": "https://culttourism.ru/murmanskaya/murmansk/pamyatnik_kirillu_i_mefodiyu.html"},
    ],
    ["monument", "murmansk", "culture", "slavic", "history"],
    maps_text("Памятник Кириллу и Мефодию", "Мурманск", "Monument to Cyril and Methodius", "Murmansk", 68.970016, 33.086706),
))

# ============================ PHỐ / QUẢNG TRƯỜNG (square_street) ============================

# 18) Площадь Пять Углов ----------------------------------------------------------
RECORDS.append(rec(
    "five-corners-square",
    "Quảng trường Năm Góc 'Pyat Uglov' (Piát U-glốp)",
    "Площадь Пять Углов",
    "Five Corners Square (Pyat Uglov)",
    ["square_street"],
    68.970671, 33.074928,
    "Trung tâm thành phố (giao đại lộ Lenina, phố Vorovskogo, phố Leningradskaya), thành phố Murmansk, tỉnh Murmansk, Nga",
    "Quảng trường trung tâm và trái tim của Murmansk, nơi giao nhau của nhiều tuyến phố lớn. Xung quanh là toà nhà hành chính, khách sạn Azimut cao nhất vùng, cửa hàng và là nơi diễn ra các sự kiện, lễ hội của thành phố.",
    "Quảng trường Pyat Uglov ('Năm Góc') là trung tâm và biểu tượng đô thị của Murmansk, hình thành từ điểm giao cắt của nhiều tuyến phố lớn — đại lộ Lenina, phố Vorovskogo, phố Leningradskaya và các trục lân cận, tạo nên hình dáng nhiều góc mà từ đó có tên gọi. Đây là không gian công cộng sầm uất nhất thành phố: bao quanh quảng trường là các toà nhà hành chính, khách sạn Azimut (toà nhà cao tầng nổi bật, một trong những công trình cao nhất vùng cực), trung tâm thương mại, cửa hàng và quán cà phê. Quảng trường là nơi tổ chức các sự kiện lớn — lễ hội thành phố, hội chợ, chợ Giáng sinh, các buổi hoà nhạc ngoài trời và đón năm mới; mùa đông thường được trang hoàng rực rỡ và dựng cây thông lớn. Với nhịp sống nhộn nhịp và vị trí trung tâm, Pyat Uglov là điểm khởi đầu tự nhiên để dạo bộ khám phá Murmansk, từ đây toả đi các bảo tàng, đài tưởng niệm và bến cảng. Đứng giữa quảng trường, du khách cảm nhận rõ Murmansk là một đô thị hiện đại, sống động ngay giữa vùng Bắc Cực.",
    [
        "Quảng trường trung tâm - trái tim đô thị của Murmansk, giao nhiều tuyến phố lớn.",
        "Bao quanh có toà nhà hành chính, khách sạn cao tầng Azimut, trung tâm thương mại.",
        "Nơi diễn ra lễ hội thành phố, chợ Giáng sinh và các sự kiện đón năm mới.",
    ],
    p("Không gian mở, dạo chơi tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 20–40 phút.",
      "Quanh năm; rực rỡ nhất dịp lễ hội và Giáng sinh - năm mới khi được trang hoàng.",
      "Điểm trung tâm dễ tiếp cận, khởi đầu cho hành trình đi bộ; nhiều quán cà phê, cửa hàng để nghỉ chân."),
    [
        {"title": "Wikipedia (RU) — Площадь Пять Углов (Мурманск)", "url": "https://ru.wikipedia.org/wiki/Площадь_Пять_Углов_(Мурманск)"},
        {"title": "Culttourism.ru — Площадь Пять Углов (Мурманск)", "url": "https://culttourism.ru/murmanskaya/murmansk/ploschad_pyat_uglov.html"},
    ],
    ["square-street", "murmansk", "city-center", "landmark", "walking"],
    maps_text("Площадь Пять Углов", "Мурманск", "Five Corners Square", "Murmansk", 68.970671, 33.074928),
))

# ============================ NHÀ HÁT (theatre) ============================

# 19) Мурманский областной драматический театр -----------------------------------
RECORDS.append(rec(
    "murmansk-drama-theatre",
    "Nhà hát Kịch tỉnh Murmansk (Tê-a-tơ Đra-ma)",
    "Мурманский областной драматический театр",
    "Murmansk Regional Drama Theatre",
    ["theatre"],
    68.961613, 33.074422,
    "Đại lộ Lenina 49, thành phố Murmansk, tỉnh Murmansk, Nga",
    "Nhà hát kịch chính của tỉnh Murmansk, sân khấu chuyên nghiệp phục vụ đời sống văn hoá thành phố cảng từ thời Xô Viết. Toà nhà cột lớn bề thế trên đại lộ Lenina là một trong những công trình văn hoá tiêu biểu của Murmansk.",
    "Nhà hát Kịch tỉnh Murmansk là sân khấu kịch chuyên nghiệp chủ lực của vùng cực, có lịch sử từ những năm 1930 và giữ vai trò trung tâm trong đời sống văn hoá của thành phố cảng. Đoàn hát dựng đa dạng thể loại — từ kịch cổ điển Nga và thế giới, chính kịch, hài kịch đến các vở dành cho thiếu nhi — mang nghệ thuật sân khấu đến với một trong những đô thị ở xa xôi nhất châu Âu. Toà nhà nhà hát bề thế với hàng cột lớn theo phong cách kiến trúc Xô Viết cổ điển, toạ lạc trên đại lộ Lenina trung tâm, là một điểm nhấn kiến trúc và văn hoá của Murmansk. Nhà hát thường xuyên tổ chức các mùa diễn, tham gia liên hoan sân khấu và đón các đoàn nghệ thuật lưu diễn, góp phần làm phong phú đời sống tinh thần nơi vùng Bắc Cực. Một buổi tối xem kịch tại đây là cách thú vị để du khách hoà vào nhịp sống văn hoá của người dân địa phương và cảm nhận rằng nghệ thuật vẫn rực sáng ngay giữa xứ tuyết.",
    [
        "Nhà hát kịch chuyên nghiệp chủ lực của tỉnh Murmansk (từ thập niên 1930).",
        "Tiết mục đa dạng: kịch cổ điển Nga - thế giới, hài kịch, vở cho thiếu nhi.",
        "Toà nhà cột lớn phong cách Xô Viết cổ điển trên đại lộ Lenina trung tâm.",
    ],
    p("Mở theo lịch biểu diễn và giờ bán vé; nên xem lịch trước.",
      "Có bán vé xem kịch; giá tuỳ suất diễn.",
      "Buổi diễn thường 2–3 giờ.",
      "Mùa diễn (thu–xuân); dịp liên hoan có nhiều vở đặc sắc.",
      "Đặt vé trước qua trang chính thức hoặc phòng vé; các vở chủ yếu bằng tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Мурманский областной драматический театр", "url": "https://ru.wikipedia.org/wiki/Мурманский_областной_драматический_театр"},
        {"title": "Culture.ru — Мурманский областной драматический театр", "url": "https://www.culture.ru/institutes/11640/murmanskii-oblastnoi-dramaticheskii-teatr"},
    ],
    ["theatre", "drama", "murmansk", "culture", "performing-arts"],
    maps_text("Мурманский областной драматический театр", "Мурманск", "Murmansk Regional Drama Theatre", "Murmansk", 68.961613, 33.074422),
))

# ============================ THIÊN NHIÊN / CÔNG VIÊN (park_garden / other) ============================

# 20) Лапландский государственный природный биосферный заповедник -----------------
RECORDS.append(rec(
    "lapland-nature-reserve",
    "Khu bảo tồn thiên nhiên Lapland (Chu-nô-dê-rô)",
    "Лапландский государственный природный биосферный заповедник",
    "Lapland Nature Reserve",
    ["park_garden", "other"],
    67.624239, 32.712532,
    "Trung tâm Chunozero (Чунозерская усадьба), gần thành phố Monchegorsk, tỉnh Murmansk, Nga",
    "Một trong những khu bảo tồn thiên nhiên lớn và lâu đời nhất châu Âu (thành lập 1930), giữa rừng taiga nguyên sinh và núi lãnh nguyên bán đảo Kola. Nơi bảo tồn đàn tuần lộc hoang dã và cũng là 'nhà của Ông già Tuyết' phương Bắc.",
    "Khu bảo tồn thiên nhiên sinh quyển Lapland là một trong những vùng rừng taiga nguyên sinh được bảo vệ lớn và lâu đời bậc nhất châu Âu, thành lập năm 1930 ở phía tây thành phố Monchegorsk. Trên diện tích rộng hàng nghìn km², khu bảo tồn gìn giữ rừng vân sam - thông cổ thụ (có những cây hàng trăm năm tuổi), các dãy núi lãnh nguyên, hồ trong vắt và hệ động vật phương Bắc — nổi bật là đàn tuần lộc hoang dã bản địa mà việc bảo vệ chúng chính là một trong những lý do khu bảo tồn ra đời. Trung tâm đón khách đặt tại Chunozerskaya usadba bên hồ Chunozero, nơi có các tuyến đường sinh thái, nhà trưng bày về thiên nhiên và lịch sử khu bảo tồn. Vào mùa đông, Lapland còn nổi tiếng với 'ngôi nhà của Ông già Tuyết' (Ded Moroz) phương Bắc — một điểm nhấn được trẻ em yêu thích, cùng khung cảnh rừng tuyết cổ tích và cơ hội ngắm cực quang. Đây là điểm đến lý tưởng cho những ai muốn đắm mình trong thiên nhiên hoang sơ, tìm hiểu sinh thái vùng cực; du khách cần đặt trước và đi theo tuyến có hướng dẫn để bảo vệ khu bảo tồn.",
    [
        "Một trong những khu bảo tồn taiga lâu đời và lớn nhất châu Âu (1930).",
        "Bảo tồn đàn tuần lộc hoang dã bản địa và rừng vân sam - thông cổ thụ.",
        "Có trung tâm Chunozero, tuyến sinh thái và 'nhà Ông già Tuyết' phương Bắc mùa đông.",
    ],
    p("Tham quan theo tuyến có hướng dẫn và phải đặt trước; trung tâm Chunozero mở theo lịch, chương trình đông - hè khác nhau.",
      "Có thu phí vào cửa và phí tour/hướng dẫn; chương trình 'nhà Ông già Tuyết' mùa đông tính vé riêng.",
      "Từ nửa ngày (tuyến sinh thái) đến trọn ngày.",
      "Mùa đông (tháng 12–3) cho cảnh tuyết, Ông già Tuyết và cực quang; mùa hè (tháng 7–9) cho trekking và ngắm thiên nhiên.",
      "Bắt buộc đặt trước qua ban quản lý khu bảo tồn; đi cùng hướng dẫn viên, không tự ý rời tuyến; mặc đồ ấm, chống ẩm. Cách Monchegorsk vài chục km, nên đi ô tô."),
    [
        {"title": "Wikipedia (RU) — Лапландский заповедник", "url": "https://ru.wikipedia.org/wiki/Лапландский_заповедник"},
        {"title": "Trang chính thức — Лапландский заповедник (laplandzap.ru)", "url": "https://laplandzap.ru/"},
    ],
    ["park_garden", "nature-reserve", "taiga", "reindeer", "arctic", "aurora"],
    maps_text("Лапландский заповедник Чунозерская усадьба", "Мончегорск", "Lapland Nature Reserve", "Monchegorsk", 67.624239, 32.712532),
    official_site="https://laplandzap.ru/",
))

# 21) Кандалакшский государственный природный заповедник --------------------------
RECORDS.append(rec(
    "kandalaksha-nature-reserve",
    "Khu bảo tồn thiên nhiên Kandalaksha (chim biển)",
    "Кандалакшский государственный природный заповедник",
    "Kandalaksha Nature Reserve",
    ["park_garden", "other"],
    67.133076, 32.417749,
    "Ban quản lý & Bảo tàng Thiên nhiên: phố Lineynaya 35, thành phố Kandalaksha, tỉnh Murmansk, Nga",
    "Khu bảo tồn thiên nhiên trên các đảo và vùng nước của vịnh Kandalaksha (Bạch Hải) và biển Barents, nổi tiếng bảo vệ chim biển - đặc biệt là vịt biển eider. Thành lập năm 1932, đây là một trong những khu bảo tồn biển - đảo lâu đời của Nga.",
    "Khu bảo tồn thiên nhiên Kandalaksha, thành lập năm 1932, là một trong những khu bảo tồn lâu đời của nước Nga, được lập ra ban đầu để bảo vệ loài vịt biển eider (gaga) quý — loài chim cho lớp lông tơ (down) ấm áp nổi tiếng. Khu bảo tồn không phải một khối liền mạch mà gồm hàng trăm hòn đảo, mỏm đá và vùng nước rải rác trong vịnh Kandalaksha thuộc Bạch Hải và dọc bờ biển Barents của bán đảo Kola. Đây là thiên đường của chim biển và chim nước: eider, hải âu, nhạn biển, chim lặn và nhiều loài di cư dừng chân theo mùa, cùng hệ sinh thái biển - đảo phương Bắc phong phú. Vì là vùng bảo vệ nghiêm ngặt, phần lớn các đảo hạn chế ra vào để giữ yên cho chim làm tổ; du khách thường tìm hiểu khu bảo tồn qua Bảo tàng Thiên nhiên và ban quản lý ở thành phố Kandalaksha, hoặc theo các tuyến/tour được phép. Với người yêu thiên nhiên và quan sát chim, Kandalaksha là điểm đến đặc biệt để hiểu về hệ sinh thái Bạch Hải và công cuộc bảo tồn ở vùng cực.",
    [
        "Khu bảo tồn biển - đảo lâu đời (1932), lập ra để bảo vệ vịt biển eider quý.",
        "Gồm hàng trăm đảo, mỏm đá và vùng nước ở vịnh Kandalaksha (Bạch Hải) và biển Barents.",
        "Thiên đường chim biển; tìm hiểu qua Bảo tàng Thiên nhiên và ban quản lý ở Kandalaksha.",
    ],
    p("Ban quản lý & Bảo tàng Thiên nhiên ở Kandalaksha mở theo giờ hành chính (nên gọi trước); ra các đảo phải xin phép và theo tuyến được phép.",
      "Bảo tàng Thiên nhiên thu phí thấp; ra vùng lõi khu bảo tồn cần giấy phép/tour riêng.",
      "Bảo tàng khoảng 1 giờ; tuyến quan sát chim có thể trọn ngày.",
      "Cuối xuân đến mùa hè (tháng 5–8) là mùa chim làm tổ và quan sát chim tốt nhất.",
      "Không tự ý lên các đảo bảo vệ nghiêm ngặt; liên hệ ban quản lý (Линейная 35) để được hướng dẫn tuyến hợp pháp."),
    [
        {"title": "Wikipedia (RU) — Кандалакшский заповедник", "url": "https://ru.wikipedia.org/wiki/Кандалакшский_заповедник"},
        {"title": "Trang chính thức — Кандалакшский заповедник", "url": "https://www.kandalaksha-reserve.org/"},
    ],
    ["park_garden", "nature-reserve", "birds", "kandalaksha", "white-sea", "eider"],
    maps_text("Кандалакшский заповедник", "Кандалакша", "Kandalaksha Nature Reserve", "Kandalaksha", 67.133076, 32.417749),
    official_site="https://www.kandalaksha-reserve.org/",
))

# 22) Озеро Имандра --------------------------------------------------------------
RECORDS.append(rec(
    "lake-imandra",
    "Hồ Imandra - hồ lớn nhất tỉnh Murmansk (I-man-đra)",
    "Озеро Имандра",
    "Lake Imandra",
    ["park_garden", "other"],
    67.836822, 33.221112,
    "Phía tây bán đảo Kola, dưới chân dãy Khibiny (giữa Monchegorsk, Apatity, Kirovsk), tỉnh Murmansk, Nga",
    "Hồ nước ngọt lớn nhất tỉnh Murmansk và là một trong những hồ lớn của châu Âu, trải dài khoảng 120 km dưới chân dãy Khibiny. Với hàng trăm hòn đảo, hồ là điểm câu cá, chèo thuyền, trượt tuyết buồm và ngắm cảnh núi non tuyệt đẹp.",
    "Imandra là hồ lớn nhất tỉnh Murmansk và thuộc hàng những hồ lớn nhất châu Âu, một 'biển nội địa' vùng cực trải dài khoảng 120 km theo hướng bắc - nam ở phía tây bán đảo Kola. Hồ có hình dáng phức tạp với ba phần lớn (Bolshaya Imandra, Yokostrovskaya Imandra, Babinskaya Imandra) nối nhau qua các eo, cùng hơn một trăm hòn đảo lớn nhỏ. Cảnh quan quanh hồ đặc biệt ngoạn mục: bờ đông là khối núi Khibiny sừng sững, còn quanh đó là các thành phố Monchegorsk, Apatity và Kirovsk. Imandra là điểm đến bốn mùa cho những người yêu thiên nhiên và hoạt động ngoài trời — mùa hè để câu cá, chèo thuyền, cắm trại và dạo các đảo; mùa đông, khi mặt hồ đóng băng, đây là nơi lý tưởng cho trượt tuyết buồm (snowkiting), câu cá trên băng và ngắm dãy Khibiny phủ tuyết. Về đêm mùa đông, mặt hồ băng mênh mông cũng là 'sân khấu' tuyệt đẹp để ngắm cực quang. Vừa hùng vĩ vừa dễ tiếp cận từ các thành phố lân cận, hồ Imandra là một trong những viên ngọc thiên nhiên nổi bật của bán đảo Kola.",
    [
        "Hồ lớn nhất tỉnh Murmansk, dài ~120 km, thuộc hàng hồ lớn nhất châu Âu.",
        "Hơn 100 hòn đảo, khung cảnh soi bóng dãy núi Khibiny bên bờ đông.",
        "Điểm câu cá, chèo thuyền mùa hè; trượt tuyết buồm, câu cá băng và ngắm cực quang mùa đông.",
    ],
    p("Không gian thiên nhiên mở, tiếp cận tự do từ các thành phố ven hồ; hoạt động trên hồ tuỳ mùa.",
      "Vào khu vực hồ miễn phí; thuê thuyền, thiết bị hoặc tour (snowkiting, câu cá) tính phí riêng.",
      "Từ vài giờ ngắm cảnh đến trọn ngày cho hoạt động ngoài trời.",
      "Mùa hè (tháng 7–9) cho câu cá, chèo thuyền; mùa đông (tháng 1–4) cho hoạt động trên băng và cực quang.",
      "Dễ tiếp cận từ Monchegorsk, Apatity, Kirovsk hoặc ga Imandra. Chú ý an toàn băng mùa đông; mặc đồ ấm, chống gió."),
    [
        {"title": "Wikipedia (RU) — Имандра", "url": "https://ru.wikipedia.org/wiki/Имандра"},
        {"title": "Вода России — Озеро Имандра", "url": "https://water-rf.ru/Водные_объекты/154/Имандра"},
    ],
    ["park_garden", "lake", "nature", "khibiny", "kola", "aurora"],
    maps_text("Озеро Имандра", "Мурманская область", "Lake Imandra", "Murmansk Oblast", 67.836822, 33.221112),
))

# 23) Полуостров Рыбачий (мыс Немецкий) -------------------------------------------
RECORDS.append(rec(
    "rybachy-peninsula",
    "Bán đảo Rybachy - điểm cực bắc đất liền châu Âu Nga (Rư-ba-tri)",
    "Полуостров Рыбачий",
    "Rybachy Peninsula",
    ["other", "park_garden"],
    69.951944, 31.940556,
    "Cực tây bắc bán đảo Kola, huyện Pechengsky, tỉnh Murmansk, Nga (mũi Nemetsky - điểm cực bắc)",
    "Bán đảo hoang sơ ở cực tây bắc bán đảo Kola, vươn ra Bắc Băng Dương với mũi Nemetsky - điểm cực bắc của phần đất liền châu Âu thuộc Nga. Nổi tiếng với cảnh quan lãnh nguyên khắc nghiệt, vách đá biển và di tích chiến tranh.",
    "Bán đảo Rybachy ('bán đảo Ngư dân') là dải đất tận cùng phía tây bắc của bán đảo Kola, nhô ra biển Barents và Bắc Băng Dương, nơi có mũi Nemetsky được xem là điểm cực bắc của phần lục địa châu Âu thuộc nước Nga. Đây là một trong những vùng hoang sơ và ấn tượng nhất Bắc Cực Nga: lãnh nguyên trơ trọi trải dài, những vách đá dựng đứng bị sóng biển bào mòn, bãi đá, thác nước nhỏ đổ ra biển và bờ biển gió lộng quanh năm. Do vị trí chiến lược án ngữ lối vào các vịnh, Rybachy từng là chiến trường ác liệt trong Thế chiến II — nơi bộ đội Xô Viết giữ vững tuyến phòng thủ cực bắc suốt cuộc chiến; đến nay bán đảo vẫn còn rải rác các công sự, khẩu đội pháo, xác khí tài và đài tưởng niệm. Với dân phượt và người mê xe địa hình, Rybachy là điểm đến trong mơ: cảnh quan tận cùng thế giới, không khí phiêu lưu và cơ hội ngắm cực quang. Tuy nhiên đường đi rất khó, hoang vắng và thời tiết khắc nghiệt, nên hầu hết du khách đến đây bằng xe địa hình theo tour có hướng dẫn.",
    [
        "Cực tây bắc bán đảo Kola; mũi Nemetsky là điểm cực bắc lục địa châu Âu thuộc Nga.",
        "Cảnh quan lãnh nguyên hoang sơ, vách đá biển và bờ Bắc Băng Dương gió lộng.",
        "Chiến trường Thế chiến II với công sự, pháo và đài tưởng niệm còn sót lại.",
    ],
    p("Vùng thiên nhiên mở; một phần từng là khu vực biên giới hạn chế - kiểm tra quy định trước khi đi.",
      "Vào vùng thiên nhiên miễn phí; tour xe địa hình có hướng dẫn tính phí (thường trọn gói).",
      "Từ 1 ngày đến vài ngày (cắm trại) tuỳ hành trình.",
      "Mùa hè (tháng 7–9) khi đường đỡ khó và có ngày địa cực; mùa đông đường gần như bất khả thi cho xe thường.",
      "Đường rất xấu, chỉ đi được bằng xe địa hình - nên theo tour có hướng dẫn; chuẩn bị đồ ấm, chống gió mưa, đồ ăn nước dự phòng; sóng điện thoại yếu."),
    [
        {"title": "Wikipedia (RU) — Рыбачий (полуостров)", "url": "https://ru.wikipedia.org/wiki/Рыбачий_(полуостров)"},
        {"title": "Wikipedia (RU) — Немецкий (мыс)", "url": "https://ru.wikipedia.org/wiki/Немецкий_(мыс)"},
    ],
    ["other", "peninsula", "arctic", "tundra", "wwii", "aurora"],
    maps_text("Полуостров Рыбачий мыс Немецкий", "Мурманская область", "Rybachy Peninsula Cape Nemetsky", "Murmansk Oblast", 69.951944, 31.940556),
))

# 24) Мурманский океанариум -------------------------------------------------------
RECORDS.append(rec(
    "murmansk-oceanarium",
    "Océanarium Murmansk - thuỷ cung cực bắc châu Âu",
    "Мурманский океанариум",
    "Murmansk Oceanarium",
    ["other"],
    68.994705, 33.089676,
    "Đại lộ Geroev-Severomortsev 4, bên hồ Semyonovskoye, thành phố Murmansk, tỉnh Murmansk, Nga",
    "Thuỷ cung nằm ở cực bắc nhất châu Âu, chuyên về các loài thú biển Bắc Cực. Điểm nhấn là chương trình biểu diễn của hải cẩu và hải cẩu xám được huấn luyện - một trải nghiệm hiếm có ngay giữa vùng cực.",
    "Océanarium Murmansk là thuỷ cung biểu diễn nằm ở vị trí cực bắc nhất châu Âu, hoạt động từ năm 1996 bên hồ Semyonovskoye trong lòng thành phố. Điểm độc đáo của nơi đây là chuyên về các loài thú biển vùng cực — đặc biệt là hải cẩu (nerpa), hải cẩu xám (tjuleni) và hải cẩu đàn hạc — được các huấn luyện viên dạy trình diễn những màn nhào lộn, giữ thăng bằng, 'hát', vẽ tranh và tương tác với khán giả. Đây được xem là cơ sở duy nhất ở châu Âu huấn luyện thành công các loài hải cẩu phương Bắc biểu diễn, dựa trên chương trình nghiên cứu khoa học về khả năng thích nghi và trí thông minh của chúng. Những buổi diễn vừa vui nhộn vừa mang tính giáo dục, giúp người xem hiểu thêm về hệ sinh vật biển Bắc Cực và tầm quan trọng của việc bảo vệ chúng. Với vị trí trung tâm, gần các đài tưởng niệm biển và tượng chú mèo Semyon, océanarium là điểm đến lý tưởng cho gia đình có trẻ em và cho bất kỳ ai muốn khám phá thế giới sinh vật biển vùng cực.",
    [
        "Thuỷ cung ở vị trí cực bắc nhất châu Âu (hoạt động từ 1996).",
        "Chương trình biểu diễn của hải cẩu phương Bắc được huấn luyện - độc đáo ở châu Âu.",
        "Vừa giải trí vừa giáo dục về sinh vật biển Bắc Cực; hợp gia đình có trẻ em.",
    ],
    p("Mở cửa theo lịch, các buổi biểu diễn vào giờ cố định trong ngày (thường nghỉ một số ngày đầu tuần); nên kiểm tra lịch diễn trước.",
      "Có bán vé; giá phải chăng, ưu đãi cho trẻ em.",
      "Buổi biểu diễn khoảng 45–60 phút.",
      "Quanh năm; canh theo giờ biểu diễn trong ngày.",
      "Đặt/canh lịch buổi diễn trước; nằm bên hồ Semyonovskoye, dễ kết hợp thăm tượng mèo Semyon, nhà thờ 'Spas-na-Vodakh' và khu tưởng niệm biển gần đó."),
    [
        {"title": "Wikipedia (RU) — Мурманский океанариум", "url": "https://ru.wikipedia.org/wiki/Мурманский_океанариум"},
        {"title": "Culttourism.ru — Мурманский океанариум", "url": "https://culttourism.ru/murmanskaya/murmansk/murmanskiy_okeanarium.html"},
    ],
    ["other", "oceanarium", "murmansk", "family", "seals", "arctic"],
    maps_text("Мурманский океанариум", "Мурманск", "Murmansk Oceanarium", "Murmansk", 68.994705, 33.089676),
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
