# -*- coding: utf-8 -*-
"""_add_places_kurgan_20260728_221756.py — VÙNG: Tỉnh Kurgan (Курганская область)
(lần chạy tự động 2026-07-28).

Bối cảnh: kurgan.json hiện có 7 địa điểm (tu viện Uspensky Dalmatovsky, tu viện Chimeevsky,
Nhà-bảo tàng Decembrist, Bảo tàng địa phương học Kurgan (краеведческий), Bảo tàng Trung tâm
Ilizarov, Thánh địa Savin, Nhà thờ Alexander Nevsky). Bổ sung 24 địa điểm THẬT SỰ nổi tiếng/đặc
sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31. TRÁNH trùng 7 điểm trên.

Trung tâm là thành phố Kurgan; mở rộng sang Shadrinsk, Dalmatovo, Kurtamysh và các điểm thiên
nhiên (hồ mặn Medvezhye, hồ khoáng Gorkoye, vườn thực vật Prosvet, suối khoáng Zhemchuzhina
Zauralya).

Phân bố loại hình (24 bản ghi mới):
- museum (5): художественный музей (Травникова), авиационный музей, музей истории города Кургана,
  Шадринский краеведческий (Бирюкова), Куртамышский краеведческий (Томина).
- theatre (3): Курганский театр драмы, театр кукол «Гулливер», Курганская областная филармония.
- square_street (1): улица Кирова («Курганский Арбат»).
- monument (5): Мемориал «Вечный огонь» (пл. Славы), Царёво городище (+fortress), Пожарная
  каланча, памятник Т. С. Мальцеву, памятник Наташе Аргентовской.
- park_garden (5): Городской сад, озеро Медвежье, Просветский дендрарий, курорт «Озеро Горькое»,
  санаторий «Жемчужина Зауралья» (термальный/минеральный).
- church (4): Богоявленский собор (Курган), Спасо-Преображенский собор (Шадринск), Николаевская
  церковь (Далматово), Свято-Духовский храм (Курган).
- bridge (1): Кировский мост через Тобол.

TOẠ ĐỘ — xác minh chéo (ru.wikipedia geohack/infobox, Wikidata, OpenStreetMap/Nominatim,
sobory.ru, Yandex Maps, 2026-07-28). Phạm vi Kurgan lat ~54–57, lon ~62–68 — tất cả toạ độ
trong phạm vi, KHÔNG đảo lat/lon:
  Театр драмы 55.44083,65.34444 (ru.wiki + Yandex); Худ.музей 55.44083,65.35361 (ru.wiki);
  Авиамузей 55.46167,65.41111 (ru.wiki, у аэропорта); Музей истории города 55.43471,65.34865
  (OSM); Шадринский музей 56.08613,63.61872 (OSM, ул.Свердлова 41); Куртамышский музей
  54.90900,64.42888 (OSM); театр «Гулливер» 55.43686,65.35068 (OSM); филармония 55.4362,65.3548
  (OSM, Троицкая пл.1); ул.Кирова 55.43410,65.33833 (OSM, đoạn giữa phố đi bộ); Вечный огонь/пл.
  Славы 55.44021,65.33776 (OSM memorial); Царёво городище 55.41810,65.24756 (OSM + visitkurgan,
  пр.Конституции 32А); Пожарная каланча 55.43528,65.35111 (ru.wiki, ул.Куйбышева); памятник
  Мальцеву 55.46348,65.26700 (OSM); памятник Наташе Аргентовской 55.4361,65.3533 (ru.wiki,
  Троицкая пл.); Городской сад 55.43917,65.34444 (ru.wiki); озеро Медвежье 55.20000,68.01670
  (ru.wiki, Петуховский р-н — rìa đông vùng); Просветский дендрарий 55.59542,65.04855 (OSM,
  с.Старый Просвет); курорт «Озеро Горькое» 55.13132,62.52591 (OSM, Щучанский р-н); санаторий
  «Жемчужина Зауралья» 56.10004,63.55039 (OSM, gần Шадринск); Богоявленский собор 55.42923,
  65.34073 (OSM, ул.Климова 3); Спасо-Преображенский собор Шадринск 56.07707,63.63350 (ru.wiki);
  Николаевская церковь Далматово 56.2575,62.9306 (OSM/sobory, ул.Советская 162); Свято-Духовский
  храм 55.4286,65.3946 (Yandex org + OSM, Смолино); Кировский мост 55.428556,65.34650 (ru.wiki).

GHI CHÚ: đã BỎ QUA các đối tượng KHÔNG xác minh được toạ độ tin cậy / trùng điểm đã có / trùng
loại, gồm: Свято-Троицкий собор Кургана (собор lịch sử đã bị phá năm 1957 — không còn hiện vật),
Введенская церковь (Кетово — không có node OSM/wiki), «Порфириевская церковь» (không tìm thấy
nguồn), Николаевский кафедральный собор Шадринска (cách собор Спасо-Преображенский chỉ ~0,4 km,
đã chọn Спасо-Преображенский làm đại diện Shadrinsk để tránh chồng lấn), Далматовский Успенский
монастырь & Александро-Невский собор & краеведческий музей (ĐÃ CÓ trong file). KHÔNG bịa toạ độ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_kurgan_20260728_221756.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "kurgan"
REGION_NAME_VI = "Tỉnh Kurgan"
FD = "Vùng Ural"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
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

# 1) Курганский областной художественный музей ------------------------------------
RECORDS.append(rec(
    "kurgan-art-museum",
    "Bảo tàng Mỹ thuật tỉnh Kurgan (mang tên Travnikov)",
    "Курганский областной художественный музей имени Г. А. Травникова",
    "Kurgan Regional Art Museum",
    ["museum"],
    55.44083, 65.35361,
    "Phố Maksima Gorkogo 129, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Bảo tàng mỹ thuật duy nhất của tỉnh Kurgan, lưu giữ tranh, đồ hoạ và điêu khắc Nga từ thế kỷ 18 đến đương đại. Nổi bật là bộ sưu tập của hoạ sĩ đồng hương German Travnikov cùng nhiều tác phẩm nghệ thuật Xô Viết và địa phương.",
    "Bảo tàng Mỹ thuật tỉnh Kurgan, mang tên hoạ sĩ German Travnikov, là bảo tàng nghệ thuật chuyên biệt duy nhất của vùng Zauralye, mở cửa từ năm 1982. Bộ sưu tập trải rộng qua tranh sơn dầu, đồ hoạ, điêu khắc và nghệ thuật trang trí ứng dụng của Nga, từ thế kỷ 18 đến nay, trong đó có nhiều tác phẩm của các danh hoạ Nga cùng những nghệ sĩ gốc Zauralye. Điểm nhấn là di sản của German Travnikov — bậc thầy tranh màu nước được coi là niềm tự hào nghệ thuật của Kurgan. Bảo tàng thường xuyên tổ chức triển lãm luân phiên, các buổi giao lưu và chương trình giáo dục nghệ thuật, trở thành trung tâm đời sống văn hoá của thành phố. Đây là điểm dừng lý tưởng cho du khách yêu hội hoạ muốn cảm nhận dòng chảy nghệ thuật của vùng đất Siberia phía tây.",
    [
        "Bảo tàng mỹ thuật duy nhất của tỉnh Kurgan (mở năm 1982).",
        "Bộ sưu tập tranh, đồ hoạ và điêu khắc Nga từ thế kỷ 18 đến đương đại.",
        "Di sản tranh màu nước của hoạ sĩ đồng hương German Travnikov.",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa ở mức khiêm tốn (vài trăm rúp); có ưu đãi cho học sinh, sinh viên và người cao tuổi.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; hợp cả những ngày thời tiết xấu.",
      "Nằm ở trung tâm, dễ kết hợp đi bộ phố Kirov gần đó. Nên xem lịch triển lãm tạm thời trước khi đến; chú thích chủ yếu bằng tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Курганский областной художественный музей", "url": "https://ru.wikipedia.org/wiki/Курганский_областной_художественный_музей"},
        {"title": "Culture.ru — Курганский художественный музей", "url": "https://www.culture.ru/institutes/9564/kurganskii-oblastnoi-khudozhestvennyi-muzei"},
    ],
    ["museum", "art", "kurgan", "painting", "culture"],
    maps_text("Курганский областной художественный музей", "Курган", "Kurgan Regional Art Museum", "Kurgan", 55.44083, 65.35361),
))

# 2) Курганский авиационный музей --------------------------------------------------
RECORDS.append(rec(
    "kurgan-aviation-museum",
    "Bảo tàng Hàng không Kurgan (A-vi-a-mu-dây)",
    "Курганский авиационный музей",
    "Kurgan Aviation Museum",
    ["museum"],
    55.46167, 65.41111,
    "Phố Gagarina 41, gần sân bay Kurgan, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Bảo tàng hàng không ngoài trời hiếm hoi ở vùng Ural–Siberia, trưng bày máy bay, trực thăng và thiết bị bay thật. Du khách có thể lại gần, trèo vào buồng lái một số máy bay và tìm hiểu lịch sử ngành hàng không dân dụng vùng Zauralye.",
    "Bảo tàng Hàng không Kurgan là một trong số ít bảo tàng hàng không của vùng Ural–Tây Siberia, nằm cạnh sân bay Kurgan và mở cửa từ năm 1985 theo sáng kiến của những người yêu ngành bay địa phương. Khu trưng bày ngoài trời quy tụ hàng loạt máy bay và trực thăng thật — từ những chiếc vận tải, huấn luyện đến máy bay chở khách của thời Xô Viết như Yak, An, Mi cùng nhiều động cơ, khí tài. Điểm hấp dẫn với du khách, đặc biệt là trẻ em, là được lại gần, sờ vào thân máy bay và trong một số trường hợp trèo vào buồng lái để hình dung công việc của phi công. Bên trong khu nhà trưng bày còn lưu giữ mô hình, đồng phục, huy hiệu và tư liệu về lịch sử hàng không dân dụng và quân sự của vùng. Đây là điểm đến thú vị, khác biệt so với các bảo tàng truyền thống, phù hợp cho gia đình và người mê kỹ thuật.",
    [
        "Khu trưng bày ngoài trời với nhiều máy bay, trực thăng thật thời Xô Viết.",
        "Du khách có thể lại gần, trèo vào buồng lái một số máy bay (điểm nhấn cho trẻ em).",
        "Tư liệu về lịch sử hàng không dân dụng và quân sự vùng Zauralye.",
    ],
    p("Thường mở cửa theo mùa ấm (tháng 5–9) và cuối tuần; nên liên hệ trước để xác nhận giờ.",
      "Vé vào cửa thấp; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 1–1,5 giờ.",
      "Mùa hè, ngày khô ráo (khu trưng bày ngoài trời).",
      "Nằm ở rìa thành phố gần sân bay; nên đi ô tô hoặc taxi. Mang mũ, nước vào ngày nắng; kiểm tra lịch mở cửa vì có thể theo mùa."),
    [
        {"title": "Wikipedia (RU) — Курганский авиационный музей", "url": "https://ru.wikipedia.org/wiki/Курганский_авиационный_музей"},
        {"title": "VisitKurgan — Авиационный музей", "url": "https://visitkurgan.ru/"},
    ],
    ["museum", "aviation", "aircraft", "kurgan", "open-air", "technology"],
    maps_text("Курганский авиационный музей", "Курган", "Kurgan Aviation Museum", "Kurgan", 55.46167, 65.41111),
))

# 3) Музей истории города Кургана --------------------------------------------------
RECORDS.append(rec(
    "kurgan-city-history-museum",
    "Bảo tàng Lịch sử thành phố Kurgan",
    "Музей истории города Кургана",
    "Museum of the History of Kurgan City",
    ["museum"],
    55.43471, 65.34865,
    "Phố Kuybysheva 59, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Bảo tàng chuyên kể câu chuyện đô thị Kurgan, đặt trong một ngôi nhà lịch sử ở trung tâm. Trưng bày tái hiện đời sống thị dân, thương nhân và các giai đoạn phát triển của thành phố từ khi lập làng đến thế kỷ 20.",
    "Bảo tàng Lịch sử thành phố Kurgan là nơi kể riêng câu chuyện của đô thị này, bổ sung góc nhìn đô thị bên cạnh Bảo tàng địa phương học cấp tỉnh. Bảo tàng nằm trong một toà nhà lịch sử ở khu trung tâm cũ, gần cụm kiến trúc thương nhân thế kỷ 19. Các gian trưng bày đưa người xem qua nhiều lớp thời gian: từ khởi thuỷ là làng Tsarevo Gorodishche bên sông Tobol, qua thời kỳ Kurgan trở thành thị trấn thương mại sầm uất nhờ tuyến đường sắt xuyên Siberia, đến giai đoạn công nghiệp hoá và Thế chiến II khi thành phố đón nhiều nhà máy sơ tán. Bên cạnh hiện vật, bản đồ và ảnh tư liệu, bảo tàng còn tái hiện nội thất sinh hoạt, cửa hiệu và nghề thủ công của thị dân xưa. Đây là nơi phù hợp để hiểu cách một 'thị trấn lưu đày' Siberia vươn lên thành trung tâm hành chính của cả vùng Zauralye.",
    [
        "Bảo tàng chuyên về lịch sử đô thị Kurgan, đặt trong toà nhà lịch sử trung tâm.",
        "Tái hiện đời sống thị dân, thương nhân và nghề thủ công xưa.",
        "Kể hành trình từ làng Tsarevo Gorodishche đến trung tâm hành chính vùng Zauralye.",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa thấp; ưu đãi cho học sinh, sinh viên và người cao tuổi.",
      "Khoảng 1 giờ.",
      "Quanh năm; hợp cả ngày thời tiết xấu.",
      "Ở trung tâm cũ, dễ kết hợp đi bộ tham quan phố Kirov và các nhà thương nhân lịch sử. Thuyết minh chủ yếu bằng tiếng Nga."),
    [
        {"title": "Culture.ru — Музей истории города Кургана", "url": "https://www.culture.ru/institutes/9569/muzei-istorii-goroda-kurgana"},
        {"title": "VisitKurgan — Музеи Кургана", "url": "https://visitkurgan.ru/"},
    ],
    ["museum", "history", "kurgan", "city", "culture"],
    maps_text("Музей истории города Кургана", "Курган", "Museum of the History of Kurgan City", "Kurgan", 55.43471, 65.34865),
))

# 4) Шадринский краеведческий музей им. В. П. Бирюкова -----------------------------
RECORDS.append(rec(
    "shadrinsk-local-lore-museum",
    "Bảo tàng địa phương học Shadrinsk (mang tên Biryukov)",
    "Шадринский краеведческий музей имени В. П. Бирюкова",
    "Shadrinsk Museum of Local Lore (Biryukov)",
    ["museum"],
    56.08613, 63.61872,
    "Phố Sverdlova 41, thành phố Shadrinsk, tỉnh Kurgan, Nga",
    "Bảo tàng lâu đời của thành phố lịch sử Shadrinsk, mang tên nhà nghiên cứu vùng đất Vladimir Biryukov. Trưng bày phong phú về thiên nhiên, khảo cổ, lịch sử và nghề thủ công của vùng Zauralye phía bắc.",
    "Bảo tàng địa phương học Shadrinsk mang tên nhà văn hoá–dân tộc học Vladimir Biryukov, người khởi lập bộ sưu tập từ đầu thế kỷ 20. Đặt tại Shadrinsk — thành phố cổ thứ hai của tỉnh, giàu di sản kiến trúc thương nhân — bảo tàng lưu giữ ký ức của cả vùng Zauralye phía bắc. Các gian trưng bày trải rộng từ mẫu vật thiên nhiên, hoá thạch, hiện vật khảo cổ, đến đời sống nông dân, nghề thủ công truyền thống (gốm, dệt, rèn) và lịch sử thành phố qua các thời kỳ. Nhiều hiện vật gắn với những nhân vật và sự kiện nổi bật của Shadrinsk, cùng bộ sưu tập dân tộc học quý về phong tục địa phương. Bảo tàng cũng là trung tâm nghiên cứu và giáo dục, thường tổ chức triển lãm và sự kiện văn hoá. Với du khách ghé Shadrinsk, đây là nơi tốt nhất để hiểu chiều sâu lịch sử của thành phố trước khi dạo quanh các nhà thờ và phố cổ.",
    [
        "Một trong những bảo tàng lâu đời nhất tỉnh, gắn với nhà nghiên cứu Vladimir Biryukov.",
        "Bộ sưu tập thiên nhiên, khảo cổ và dân tộc học phong phú của vùng Zauralye phía bắc.",
        "Trưng bày nghề thủ công truyền thống và lịch sử thành phố thương nhân Shadrinsk.",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa thấp; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm.",
      "Cách Kurgan khoảng 145 km; dễ kết hợp tham quan các nhà thờ cổ và phố thương nhân Shadrinsk. Thuyết minh chủ yếu bằng tiếng Nga."),
    [
        {"title": "Culture.ru — Шадринский краеведческий музей", "url": "https://www.culture.ru/institutes/9571/shadrinskii-kraevedcheskii-muzei-im-v-p-biryukova"},
        {"title": "Wikipedia (RU) — Шадринск", "url": "https://ru.wikipedia.org/wiki/Шадринск"},
    ],
    ["museum", "history", "shadrinsk", "ethnography", "local-lore"],
    maps_text("Шадринский краеведческий музей", "Шадринск", "Shadrinsk Museum of Local Lore", "Shadrinsk", 56.08613, 63.61872),
))

# 5) Куртамышский краеведческий музей им. Н. Д. Томина -----------------------------
RECORDS.append(rec(
    "kurtamysh-museum",
    "Bảo tàng địa phương học Kurtamysh (mang tên Tomin)",
    "Куртамышский краеведческий музей имени Н. Д. Томина",
    "Kurtamysh Museum of Local Lore (Tomin)",
    ["museum"],
    54.90900, 64.42888,
    "Thành phố Kurtamysh, huyện Kurtamyshsky, tỉnh Kurgan, Nga",
    "Bảo tàng địa phương của thị trấn Kurtamysh ở phía nam tỉnh, mang tên thủ lĩnh kỵ binh Nikolay Tomin. Trưng bày lịch sử khai hoang, đời sống nông dân Cossack và thiên nhiên vùng thảo nguyên–rừng phía nam Zauralye.",
    "Bảo tàng địa phương học Kurtamysh, mang tên Nikolay Tomin — vị chỉ huy kỵ binh Nội chiến sinh ra ở vùng này, là điểm văn hoá trung tâm của thị trấn Kurtamysh phía nam tỉnh Kurgan. Kurtamysh vốn là một слобода (khu định cư) hình thành từ giữa thế kỷ 18 trong quá trình người Nga khai hoang vùng biên giới thảo nguyên, nên bảo tàng kể nhiều về lịch sử khẩn hoang, đời sống nông dân và cộng đồng Cossack từng trấn giữ tuyến phòng thủ phía nam. Bộ sưu tập gồm hiện vật khảo cổ, nông cụ, đồ gia dụng, trang phục dân gian cùng các mẫu vật thiên nhiên của vùng chuyển tiếp thảo nguyên–rừng. Bảo tàng cũng lưu giữ tư liệu về Nikolay Tomin và những người con tiêu biểu của địa phương. Đây là điểm dừng đáng chú ý cho ai muốn tìm hiểu một góc tỉnh Kurgan ít du khách, gắn với ký ức khẩn hoang và biên cương thảo nguyên.",
    [
        "Bảo tàng trung tâm của thị trấn khẩn hoang Kurtamysh, mang tên tướng kỵ binh Tomin.",
        "Trưng bày lịch sử khai hoang và đời sống nông dân–Cossack biên giới thảo nguyên.",
        "Hiện vật khảo cổ, nông cụ, trang phục dân gian và thiên nhiên vùng thảo nguyên–rừng.",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 9:00–17:00; nghỉ Thứ Hai (nên gọi xác nhận).",
      "Vé vào cửa thấp; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 1 giờ.",
      "Quanh năm.",
      "Cách Kurgan khoảng 90 km về phía tây nam; nên đi ô tô. Thuyết minh chủ yếu bằng tiếng Nga; gọi trước nếu muốn có hướng dẫn viên."),
    [
        {"title": "Culture.ru — Куртамышский краеведческий музей", "url": "https://www.culture.ru/institutes/9573/kurtamyshskii-kraevedcheskii-muzei-im-n-d-tomina"},
        {"title": "Wikipedia (RU) — Куртамыш", "url": "https://ru.wikipedia.org/wiki/Куртамыш"},
    ],
    ["museum", "history", "kurtamysh", "cossack", "local-lore"],
    maps_text("Куртамышский краеведческий музей", "Куртамыш", "Kurtamysh Museum of Local Lore", "Kurtamysh", 54.90900, 64.42888),
))

# ============================ NHÀ HÁT (theatre) ============================

# 6) Курганский государственный театр драмы ---------------------------------------
RECORDS.append(rec(
    "kurgan-drama-theatre",
    "Nhà hát Kịch bang Kurgan (Tê-a-tơ Đra-ma)",
    "Курганский государственный театр драмы",
    "Kurgan State Drama Theatre",
    ["theatre"],
    55.44083, 65.34444,
    "Phố Gogolya 58, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Nhà hát kịch chính của tỉnh Kurgan, sân khấu chuyên nghiệp lâu đời với tiết mục kịch cổ điển Nga và thế giới. Toà nhà hiện đại bên trung tâm thành phố là điểm hẹn văn hoá quen thuộc của người dân Zauralye.",
    "Nhà hát Kịch bang Kurgan là sân khấu kịch chuyên nghiệp hàng đầu của tỉnh, có lịch sử từ giữa thế kỷ 20 và giữ vai trò trung tâm trong đời sống văn hoá vùng Zauralye. Đoàn hát dựng đa dạng thể loại — từ bi kịch, chính kịch cổ điển Nga và thế giới đến hài kịch, nhạc kịch và các vở dành cho thiếu nhi. Toà nhà nhà hát bề thế nằm ở khu trung tâm Kurgan, gần các quảng trường và phố đi bộ, là nơi diễn ra nhiều liên hoan sân khấu, buổi công diễn và sự kiện văn hoá của thành phố. Nhà hát cũng thường lưu diễn và tham gia các festival sân khấu khu vực, góp phần đưa tên tuổi Kurgan ra ngoài tỉnh. Một buổi tối xem kịch tại đây là cách thú vị để du khách hoà vào nhịp sống văn hoá của người dân địa phương.",
    [
        "Nhà hát kịch chuyên nghiệp chủ lực của tỉnh Kurgan.",
        "Tiết mục đa dạng: kịch cổ điển Nga–thế giới, hài kịch và vở cho thiếu nhi.",
        "Toà nhà bề thế ở trung tâm, thường xuyên tổ chức liên hoan và sự kiện sân khấu.",
    ],
    p("Mở theo lịch biểu diễn và giờ bán vé; nên xem lịch trước.",
      "Có bán vé xem kịch; giá tuỳ suất diễn.",
      "Buổi diễn thường 2–3 giờ.",
      "Mùa diễn (thu–xuân); dịp liên hoan có nhiều vở đặc sắc.",
      "Đặt vé trước qua trang chính thức hoặc phòng vé; các vở chủ yếu bằng tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Курганский театр драмы", "url": "https://ru.wikipedia.org/wiki/Курганский_театр_драмы"},
        {"title": "Culture.ru — Курганский театр драмы", "url": "https://www.culture.ru/institutes/9560/kurganskii-gosudarstvennyi-teatr-dramy"},
    ],
    ["theatre", "drama", "kurgan", "culture", "performing-arts"],
    maps_text("Курганский государственный театр драмы", "Курган", "Kurgan State Drama Theatre", "Kurgan", 55.44083, 65.34444),
))

# 7) Курганский театр кукол «Гулливер» --------------------------------------------
RECORDS.append(rec(
    "gulliver-puppet-theatre",
    "Nhà hát Múa rối Gulliver (Kurgan)",
    "Курганский театр кукол «Гулливер»",
    "Gulliver Puppet Theatre (Kurgan)",
    ["theatre"],
    55.43686, 65.35068,
    "Phố Sovetskaya 104, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Nhà hát múa rối lâu đời và được yêu thích bậc nhất của Kurgan, chuyên các vở cổ tích cho thiếu nhi. Với tên gọi 'Gulliver', nơi đây là điểm đến quen thuộc của các gia đình có trẻ nhỏ ở vùng Zauralye.",
    "Nhà hát Múa rối 'Gulliver' là một trong những nhà hát dành cho thiếu nhi được yêu mến nhất tỉnh Kurgan, hoạt động từ giữa thế kỷ 20. Lấy tên nhân vật Gulliver, nhà hát chuyên dựng các vở cổ tích Nga và thế giới bằng nghệ thuật múa rối phong phú — từ rối tay, rối que đến rối dây và những con rối cỡ lớn. Sân khấu nhỏ ấm cúng ở trung tâm Kurgan là nơi nhiều thế hệ trẻ em địa phương lần đầu làm quen với nghệ thuật sân khấu. Ngoài các buổi diễn thường kỳ, nhà hát còn tham gia liên hoan múa rối, tổ chức chương trình giáo dục và sự kiện dịp lễ. Đây là lựa chọn thú vị cho du khách đi cùng trẻ em, đồng thời cho thấy đời sống sân khấu dành cho thiếu nhi khá sôi động ở một thành phố tỉnh lẻ.",
    [
        "Nhà hát múa rối được yêu thích bậc nhất Kurgan, dành cho thiếu nhi.",
        "Đa dạng loại rối: rối tay, rối que, rối dây và rối cỡ lớn.",
        "Điểm đến quen thuộc của các gia đình; thường tham gia liên hoan múa rối.",
    ],
    p("Mở theo lịch biểu diễn, thường vào cuối tuần và dịp lễ; xem lịch trước.",
      "Vé xem múa rối giá thấp, phù hợp gia đình.",
      "Buổi diễn thường 45–70 phút.",
      "Cuối tuần, dịp nghỉ lễ và mùa diễn.",
      "Phù hợp trẻ nhỏ; đặt vé trước vào dịp cao điểm. Các vở bằng tiếng Nga nhưng giàu hình ảnh, dễ theo dõi."),
    [
        {"title": "Culture.ru — Театр кукол «Гулливер»", "url": "https://www.culture.ru/institutes/9562/kurganskii-teatr-kukol-gulliver"},
        {"title": "VisitKurgan — Театр кукол «Гулливер»", "url": "https://visitkurgan.ru/"},
    ],
    ["theatre", "puppet", "kurgan", "children", "culture"],
    maps_text("Курганский театр кукол Гулливер", "Курган", "Gulliver Puppet Theatre", "Kurgan", 55.43686, 65.35068),
))

# 8) Курганская областная филармония ----------------------------------------------
RECORDS.append(rec(
    "kurgan-philharmonic",
    "Nhạc viện–Nhà hát giao hưởng tỉnh Kurgan (Fi-lac-mô-ni-a)",
    "Курганская областная филармония",
    "Kurgan Regional Philharmonic",
    ["theatre"],
    55.4362, 65.3548,
    "Quảng trường Troitskaya 1, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Trung tâm âm nhạc chính của tỉnh Kurgan, nơi tổ chức hoà nhạc giao hưởng, dân gian và các buổi biểu diễn nghệ thuật. Phòng hoà nhạc nằm bên quảng trường Troitskaya lịch sử ở trung tâm thành phố.",
    "Nhạc viện tỉnh Kurgan (Курганская областная филармония) là trung tâm âm nhạc hàn lâm và biểu diễn của cả vùng Zauralye. Đây là nơi đóng đô của các tập thể nghệ thuật của tỉnh — từ dàn nhạc, hợp xướng đến các nhóm nhạc dân gian — và thường xuyên đón các nghệ sĩ, dàn nhạc lưu diễn từ khắp nước Nga. Chương trình trải rộng từ nhạc cổ điển, giao hưởng, hoà nhạc thính phòng đến nhạc dân gian, jazz và các buổi diễn dành cho thiếu nhi. Phòng hoà nhạc toạ lạc bên quảng trường Troitskaya ở trung tâm lịch sử Kurgan, gần nhiều điểm tham quan khác, nên thuận tiện kết hợp trong hành trình khám phá thành phố. Một buổi hoà nhạc buổi tối tại đây là cách tinh tế để cảm nhận đời sống văn hoá của thủ phủ vùng Zauralye.",
    [
        "Trung tâm âm nhạc hàn lâm và biểu diễn chính của tỉnh Kurgan.",
        "Chương trình đa dạng: giao hưởng, thính phòng, dân gian, jazz và nhạc thiếu nhi.",
        "Vị trí bên quảng trường Troitskaya lịch sử ở trung tâm thành phố.",
    ],
    p("Mở theo lịch hoà nhạc và giờ bán vé; nên xem lịch trước.",
      "Có bán vé; giá tuỳ chương trình.",
      "Buổi diễn thường 1,5–2 giờ.",
      "Mùa hoà nhạc (thu–xuân).",
      "Đặt vé trước qua trang chính thức; kết hợp dạo quảng trường Troitskaya và trung tâm lịch sử."),
    [
        {"title": "Culture.ru — Курганская областная филармония", "url": "https://www.culture.ru/institutes/9566/kurganskaya-oblastnaya-filarmoniya"},
        {"title": "VisitKurgan — Филармония", "url": "https://visitkurgan.ru/"},
    ],
    ["theatre", "music", "concert", "kurgan", "philharmonic", "culture"],
    maps_text("Курганская областная филармония", "Курган", "Kurgan Regional Philharmonic", "Kurgan", 55.4362, 65.3548),
))

# ============================ PHỐ / QUẢNG TRƯỜNG (square_street) ============================

# 9) Улица Кирова -----------------------------------------------------------------
RECORDS.append(rec(
    "kirov-street",
    "Phố đi bộ Kirov — 'Arbat Kurgan'",
    "Улица Кирова",
    "Kirov Street (Kurgan Arbat)",
    ["square_street"],
    55.43410, 65.33833,
    "Phố Kirova (đoạn đi bộ), trung tâm thành phố Kurgan, tỉnh Kurgan, Nga",
    "Phố đi bộ trung tâm của Kurgan, thường được gọi là 'Arbat Kurgan'. Con phố lát đá với hàng cây, ghế nghỉ, tượng nhỏ và các toà nhà thương nhân cổ là nơi dạo bộ, gặp gỡ yêu thích của người dân.",
    "Phố Kirov là tuyến phố đi bộ trung tâm của Kurgan và được người dân trìu mến gọi là 'Arbat Kurgan', theo cách so sánh với phố Arbat nổi tiếng ở Moskva. Đoạn đi bộ được lát đá, trang trí bằng hàng cây, bồn hoa, đèn trang trí, ghế nghỉ và các tác phẩm điêu khắc đường phố nhỏ xinh, tạo nên không gian dạo bộ thư giãn giữa lòng thành phố. Hai bên phố là những toà nhà thương nhân cuối thế kỷ 19 – đầu thế kỷ 20, phản ánh thời kỳ Kurgan phồn thịnh nhờ buôn bán và tuyến đường sắt xuyên Siberia, xen kẽ với quán cà phê, cửa hàng và điểm văn hoá. Đây là nơi diễn ra nhiều sự kiện, hội chợ và biểu diễn đường phố, đồng thời là điểm hẹn quen thuộc của giới trẻ và các gia đình. Với du khách, dạo phố Kirov là cách dễ chịu nhất để cảm nhận nhịp sống và diện mạo lịch sử của trung tâm Kurgan.",
    [
        "Phố đi bộ trung tâm, biệt danh 'Arbat Kurgan'.",
        "Kiến trúc thương nhân cuối thế kỷ 19 – đầu thế kỷ 20 dọc hai bên phố.",
        "Không gian dạo bộ với tượng đường phố, quán cà phê và sự kiện văn hoá.",
    ],
    p("Không gian mở, dạo chơi tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 45–90 phút tuỳ nhịp dạo và ghé quán.",
      "Chiều mát và buổi tối; đẹp nhất mùa hè và các dịp lễ hội đường phố.",
      "Dễ kết hợp các bảo tàng, nhà thờ Alexander Nevsky và quảng trường ở trung tâm; nhiều quán cà phê để nghỉ chân."),
    [
        {"title": "VisitKurgan — Улица Кирова (пешеходная)", "url": "https://visitkurgan.ru/"},
        {"title": "Wikipedia (RU) — Курган (город)", "url": "https://ru.wikipedia.org/wiki/Курган_(город)"},
    ],
    ["square-street", "pedestrian", "kurgan", "city-center", "architecture", "walking"],
    maps_text("Улица Кирова", "Курган", "Kirov Street", "Kurgan", 55.43410, 65.33833),
))

# ============================ ĐÀI TƯỞNG NIỆM / TƯỢNG (monument) ============================

# 10) Мемориал «Вечный огонь» (площадь Славы) -------------------------------------
RECORDS.append(rec(
    "eternal-flame-memorial-kurgan",
    "Đài tưởng niệm Ngọn lửa Vĩnh cửu (Quảng trường Vinh quang, Kurgan)",
    "Мемориал «Вечный огонь» (площадь Славы)",
    "Eternal Flame Memorial (Glory Square)",
    ["monument"],
    55.44021, 65.33776,
    "Quảng trường Vinh quang (площадь Славы), phố Volodarskogo, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Đài tưởng niệm chiến sĩ hy sinh trong Chiến tranh Vệ quốc Vĩ đại của Kurgan, với Ngọn lửa Vĩnh cửu và tượng 'Người mẹ đau thương'. Đây là nơi diễn ra các nghi lễ trọng thể ngày 9/5 và điểm tưởng niệm thiêng liêng của thành phố.",
    "Đài tưởng niệm Ngọn lửa Vĩnh cửu trên Quảng trường Vinh quang là công trình tưởng niệm trung tâm của Kurgan dành cho những người con của vùng đã ngã xuống trong Chiến tranh Vệ quốc Vĩ đại (1941–1945). Trung tâm quần thể là ngọn lửa cháy không tắt cùng tượng đài 'Người mẹ đau thương' (Скорбящая мать) — biểu tượng của nỗi đau và lòng biết ơn với những người lính. Xung quanh là các phiến đá, bảng khắc tên và không gian nghiêm trang để người dân đặt hoa. Vào ngày Chiến thắng 9/5 và các dịp lễ quốc gia, nơi đây diễn ra những nghi lễ trọng thể, diễu hành 'Trung đoàn Bất tử' và lễ đặt vòng hoa. Đây vừa là địa điểm mang ý nghĩa lịch sử – tinh thần sâu sắc với người Kurgan, vừa là điểm dừng để du khách hiểu thêm về đóng góp và mất mát của vùng Zauralye trong chiến tranh.",
    [
        "Ngọn lửa Vĩnh cửu tưởng niệm chiến sĩ hy sinh trong Chiến tranh Vệ quốc Vĩ đại.",
        "Tượng đài 'Người mẹ đau thương' (Скорбящая мать) làm điểm nhấn.",
        "Nơi diễn ra nghi lễ trọng thể ngày Chiến thắng 9/5.",
    ],
    p("Không gian mở, tham quan tự do mọi lúc; trang nghiêm nhất vào ban ngày.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Quanh năm; đặc biệt dịp 9/5 (Ngày Chiến thắng).",
      "Giữ thái độ trang nghiêm; nằm ở trung tâm, gần nhà thờ Alexander Nevsky và phố Kirov."),
    [
        {"title": "VisitKurgan — Мемориал «Вечный огонь»", "url": "https://visitkurgan.ru/"},
        {"title": "Wikipedia (RU) — Курган (город)", "url": "https://ru.wikipedia.org/wiki/Курган_(город)"},
    ],
    ["monument", "memorial", "wwii", "eternal-flame", "kurgan", "history"],
    maps_text("Мемориал Вечный огонь площадь Славы", "Курган", "Eternal Flame Memorial", "Kurgan", 55.44021, 65.33776),
))

# 11) Царёво городище ------------------------------------------------------------
RECORDS.append(rec(
    "tsarevo-gorodishche",
    "Царёво городище — nơi khai sinh Kurgan (Tsa-rê-vô)",
    "Царёво городище",
    "Tsarevo Gorodishche",
    ["fortress", "monument"],
    55.41810, 65.24756,
    "Đại lộ Konstitutsii 32А, khu Energetikov, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Di chỉ và công viên lịch sử đánh dấu nơi khai sinh thành phố Kurgan, bên bờ sông Tobol. Có tháp gỗ và một phần tường thành đồn trú (острог) được phục dựng, tái hiện pháo đài biên giới Siberia thế kỷ 17.",
    "Царёво городище (Tsarevo Gorodishche) là nơi ra đời của thành phố Kurgan: giữa thế kỷ 17, một khu định cư có phòng thủ (слобода/острог) được lập bên bờ sông Tobol, cạnh một gò mộ cổ đồ sộ mà dân gian gọi là 'Царёв курган' — chính từ chữ 'kurgan' (gò mộ) này mà thành phố về sau mang tên. Ngày nay, tại khu vực gắn với di chỉ lịch sử, một công viên–bảo tàng ngoài trời đã được xây dựng với tháp canh bằng gỗ và một phần tường thành đồn trú phục dựng theo kiểu pháo đài biên giới Siberia thời khai hoang. Không gian này giúp du khách hình dung buổi đầu người Nga tiến về phía đông dãy Ural, dựng các острог để bảo vệ vùng biên trước các cuộc tập kích. Đây là điểm đến giàu ý nghĩa biểu tượng — 'điểm khởi đầu' của Kurgan — kết hợp giữa cảnh quan ven sông Tobol và câu chuyện lập thành phố.",
    [
        "Nơi khai sinh thành phố Kurgan bên bờ sông Tobol (thế kỷ 17).",
        "Tháp gỗ và một phần tường thành đồn trú (острог) phục dựng.",
        "Gắn với gò mộ cổ 'Царёв курган' — nguồn gốc tên gọi thành phố.",
    ],
    p("Công viên ngoài trời, tham quan ban ngày; các công trình phục dựng có thể có giờ mở riêng.",
      "Khu ngoài trời thường vào tự do; một số hoạt động/tham quan có hướng dẫn có thể thu phí.",
      "Khoảng 45–90 phút.",
      "Cuối xuân đến đầu thu (tháng 5–9), thời tiết ấm.",
      "Nằm ở khu Energetikov, hơi xa trung tâm; nên đi ô tô hoặc taxi. Kết hợp ngắm cảnh sông Tobol."),
    [
        {"title": "VisitKurgan — Царёво городище", "url": "https://visitkurgan.ru/"},
        {"title": "Wikipedia (RU) — Курган (город)", "url": "https://ru.wikipedia.org/wiki/Курган_(город)"},
    ],
    ["monument", "fortress", "history", "kurgan", "ostrog", "open-air"],
    maps_text("Царёво городище", "Курган", "Tsarevo Gorodishche", "Kurgan", 55.41810, 65.24756),
))

# 12) Пожарная каланча ------------------------------------------------------------
RECORDS.append(rec(
    "kurgan-fire-tower",
    "Tháp cứu hoả lịch sử Kurgan (Ka-lan-cha)",
    "Пожарная каланча",
    "Historic Fire Watchtower (Kurgan)",
    ["monument"],
    55.43528, 65.35111,
    "Phố Kuybysheva, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Tháp canh cứu hoả cổ, một trong những biểu tượng kiến trúc lịch sử của Kurgan. Toà tháp gạch cao vút với chòi quan sát bằng gỗ là điểm nhận diện quen thuộc ở khu trung tâm cũ.",
    "Tháp cứu hoả (Пожарная каланча) là một trong những công trình lịch sử được yêu thích và dễ nhận ra nhất ở trung tâm cũ của Kurgan. Được xây dựng vào cuối thế kỷ 19 – đầu thế kỷ 20 khi các đô thị Nga đều cần trạm cứu hoả với tháp quan sát, toà tháp gạch cao vươn lên trên nền phố thấp, phía đỉnh là chòi canh bằng gỗ nơi lính cứu hoả xưa đứng gác, phát hiện khói lửa để báo động kịp thời. Kiến trúc tháp mang nét trang trí gạch đặc trưng thời đó, trở thành điểm nhấn thị giác và biểu tượng đô thị. Ngày nay tháp cứu hoả được xem là di tích kiến trúc, thường xuất hiện trong ảnh và biểu trưng của thành phố; một mô hình lính cứu hoả trên đỉnh tháp còn tạo thêm nét sinh động thu hút du khách chụp ảnh. Đây là điểm dừng nhanh thú vị khi dạo khu trung tâm lịch sử Kurgan.",
    [
        "Tháp canh cứu hoả cổ (cuối thế kỷ 19 – đầu thế kỷ 20), biểu tượng đô thị Kurgan.",
        "Kiến trúc gạch trang trí với chòi quan sát bằng gỗ trên đỉnh.",
        "Điểm nhận diện quen thuộc và ưa thích để chụp ảnh ở trung tâm cũ.",
    ],
    p("Là công trình đô thị, ngắm từ bên ngoài tự do mọi lúc (bên trong thường không mở cho khách).",
      "Miễn phí (ngắm bên ngoài).",
      "Khoảng 15–20 phút.",
      "Quanh năm; đẹp khi có nắng để chụp ảnh.",
      "Nằm trên phố Kuybysheva ở trung tâm cũ, dễ kết hợp Bảo tàng lịch sử thành phố và phố Kirov gần đó."),
    [
        {"title": "Wikipedia (RU) — Пожарная каланча (Курган)", "url": "https://ru.wikipedia.org/wiki/Пожарная_каланча_(Курган)"},
        {"title": "VisitKurgan — Пожарная каланча", "url": "https://visitkurgan.ru/"},
    ],
    ["monument", "architecture", "kurgan", "landmark", "history"],
    maps_text("Пожарная каланча", "Курган", "Historic Fire Watchtower", "Kurgan", 55.43528, 65.35111),
))

# 13) Памятник Т. С. Мальцеву -----------------------------------------------------
RECORDS.append(rec(
    "maltsev-monument",
    "Tượng đài nhà nông học Terenty Maltsev (Man-txép)",
    "Памятник Т. С. Мальцеву",
    "Monument to Terenty Maltsev",
    ["monument"],
    55.46348, 65.26700,
    "Phố Terentiya Maltseva, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Tượng đài tôn vinh Terenty Maltsev — nhà nông học huyền thoại của vùng Zauralye, người tiên phong phương pháp canh tác không cày lật đất. Ông là niềm tự hào lớn của tỉnh Kurgan trong lĩnh vực nông nghiệp.",
    "Tượng đài Terenty Maltsev tưởng nhớ một trong những người con nổi tiếng nhất của vùng Zauralye — nhà nông học tự học Terenty Semyonovich Maltsev (1895–1994), người đã cống hiến cả đời cho khoa học canh tác trên đất thảo nguyên khô hạn của tỉnh Kurgan. Xuất thân nông dân, Maltsev phát triển phương pháp làm đất không cày lật (bảo tồn tầng đất mặt) và hệ thống canh tác thích hợp với vùng Zauralye, giúp nâng cao năng suất và chống xói mòn — những ý tưởng đi trước thời đại về nông nghiệp bền vững. Ông hai lần được phong Anh hùng Lao động Xã hội chủ nghĩa và trở thành biểu tượng của người nông dân – nhà khoa học. Tượng đài đặt tại Kurgan là nơi người dân bày tỏ lòng kính trọng với ông, đồng thời nhắc nhớ vai trò nông nghiệp trong lịch sử và bản sắc của tỉnh. Với du khách, đây là dịp để biết đến một nhân vật đặc biệt đã làm rạng danh vùng đất Kurgan.",
    [
        "Tôn vinh nhà nông học huyền thoại Terenty Maltsev (1895–1994) của vùng Zauralye.",
        "Gắn với phương pháp canh tác không cày lật đất, đi trước thời đại về nông nghiệp bền vững.",
        "Biểu tượng của người nông dân – nhà khoa học, niềm tự hào của tỉnh Kurgan.",
    ],
    p("Không gian ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15 phút.",
      "Quanh năm; đẹp khi có nắng.",
      "Kết hợp trong hành trình dạo thành phố; tìm hiểu thêm về Maltsev tại Bảo tàng địa phương học Kurgan."),
    [
        {"title": "Wikipedia (RU) — Мальцев, Терентий Семёнович", "url": "https://ru.wikipedia.org/wiki/Мальцев,_Терентий_Семёнович"},
        {"title": "VisitKurgan — Памятник Т. С. Мальцеву", "url": "https://visitkurgan.ru/"},
    ],
    ["monument", "kurgan", "agriculture", "science", "history"],
    maps_text("Памятник Т. С. Мальцеву", "Курган", "Monument to Terenty Maltsev", "Kurgan", 55.46348, 65.26700),
))

# 14) Памятник Наташе Аргентовской ------------------------------------------------
RECORDS.append(rec(
    "natasha-argentovskaya-monument",
    "Tượng đài Natasha Argentovskaya (Ac-ghen-tốp-xcai-a)",
    "Памятник Наташе Аргентовской",
    "Monument to Natasha Argentovskaya",
    ["monument"],
    55.4361, 65.3533,
    "Quảng trường Troitskaya, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Tượng đài tưởng niệm Natasha Argentovskaya — nữ chiến sĩ trẻ tuổi thời Nội chiến, một biểu tượng lịch sử của Kurgan. Bức tượng ở trung tâm thành phố gắn với câu chuyện bi tráng đầu thế kỷ 20.",
    "Tượng đài Natasha Argentovskaya tưởng niệm một nữ thiếu niên đã trở thành nhân vật lịch sử được nhắc nhớ ở Kurgan. Natalya (Natasha) Argentovskaya là cô gái trẻ tham gia phong trào cách mạng trong những năm Nội chiến đầy biến động ở vùng Zauralye và hy sinh khi tuổi đời còn rất trẻ, trở thành hình tượng về lòng dũng cảm và tuổi trẻ nhiệt huyết trong ký ức lịch sử Xô Viết của thành phố. Bức tượng đặt tại khu trung tâm Kurgan (gần quảng trường Troitskaya) là nơi ghi dấu câu chuyện của cô, đồng thời là một trong những đài tưởng niệm lâu đời gắn với lịch sử đầu thế kỷ 20 của thành phố. Với du khách, đây là điểm dừng ngắn để chạm vào một lát cắt lịch sử địa phương và hiểu thêm cách người Kurgan gìn giữ ký ức về những nhân vật của mình.",
    [
        "Tưởng niệm nữ chiến sĩ trẻ Natasha Argentovskaya thời Nội chiến.",
        "Một trong những đài tưởng niệm lịch sử gắn với đầu thế kỷ 20 của Kurgan.",
        "Vị trí trung tâm, gần quảng trường Troitskaya và nhạc viện.",
    ],
    p("Không gian ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Quanh năm.",
      "Nằm ở trung tâm, dễ kết hợp nhạc viện, quảng trường Troitskaya và phố Kirov."),
    [
        {"title": "Wikipedia (RU) — Памятник Наташе Аргентовской", "url": "https://ru.wikipedia.org/wiki/Памятник_Наташе_Аргентовской"},
        {"title": "VisitKurgan — Памятник Наташе Аргентовской", "url": "https://visitkurgan.ru/"},
    ],
    ["monument", "history", "kurgan", "civil-war", "memorial"],
    maps_text("Памятник Наташе Аргентовской", "Курган", "Monument to Natasha Argentovskaya", "Kurgan", 55.4361, 65.3533),
))

# ============================ CÔNG VIÊN / THIÊN NHIÊN (park_garden) ============================

# 15) Городской сад (Курган) ------------------------------------------------------
RECORDS.append(rec(
    "kurgan-city-garden",
    "Vườn Thành phố Kurgan (Ga-rôt-xkôi Xát)",
    "Городской сад",
    "Kurgan City Garden",
    ["park_garden"],
    55.43917, 65.34444,
    "Trung tâm thành phố Kurgan, tỉnh Kurgan, Nga",
    "Công viên lâu đời và trung tâm nhất của Kurgan, không gian cây xanh gắn với đời sống thị dân từ thế kỷ 19. Nơi đây có lối dạo, sân khấu, khu vui chơi và các sự kiện văn hoá quanh năm.",
    "Vườn Thành phố (Городской сад) là công viên lâu đời và mang tính biểu tượng nhất của Kurgan, gắn bó với đời sống thị dân từ cuối thế kỷ 19. Nằm ở trung tâm thành phố, khu vườn từng là nơi dạo chơi, nghỉ ngơi và giải trí quen thuộc của người dân qua nhiều thế hệ, với những hàng cây cổ thụ, lối đi rợp bóng và không gian xanh mát hiếm có giữa phố. Ngày nay, công viên kết hợp giữa cảnh quan truyền thống và các tiện ích hiện đại: sân khấu ngoài trời, khu trò chơi, quán giải khát và không gian tổ chức sự kiện, lễ hội thành phố. Vào mùa hè, đây là điểm hẹn của các gia đình, buổi hoà nhạc và hội chợ; mùa đông có thể có khu trượt và trang trí lễ hội. Với du khách, Городской сад là nơi dễ chịu để nghỉ chân, quan sát nhịp sống địa phương và tận hưởng chút thiên nhiên ngay giữa trung tâm Kurgan.",
    [
        "Công viên lâu đời và trung tâm nhất Kurgan (từ cuối thế kỷ 19).",
        "Hàng cây cổ thụ, lối dạo rợp bóng và không gian xanh giữa phố.",
        "Sân khấu ngoài trời, khu vui chơi và sự kiện văn hoá quanh năm.",
    ],
    p("Không gian mở, dạo chơi tự do; các trò chơi/tiện ích có giờ hoạt động riêng.",
      "Vào công viên miễn phí; một số trò chơi, dịch vụ thu phí.",
      "Khoảng 45–90 phút.",
      "Mùa hè cho cây xanh, sự kiện; mùa đông có trang trí lễ hội.",
      "Ở trung tâm, dễ kết hợp phố Kirov và các bảo tàng; có quán giải khát để nghỉ chân."),
    [
        {"title": "Wikipedia (RU) — Городской сад (Курган)", "url": "https://ru.wikipedia.org/wiki/Городской_сад_(Курган)"},
        {"title": "VisitKurgan — Городской сад", "url": "https://visitkurgan.ru/"},
    ],
    ["park-garden", "park", "kurgan", "city-center", "recreation", "nature"],
    maps_text("Городской сад", "Курган", "Kurgan City Garden", "Kurgan", 55.43917, 65.34444),
))

# 16) Озеро Медвежье --------------------------------------------------------------
RECORDS.append(rec(
    "medvezhye-lake",
    "Hồ mặn Medvezhye — 'Biển Chết' của vùng Zauralye (Mét-vê-gie)",
    "Озеро Медвежье",
    "Lake Medvezhye",
    ["park_garden"],
    55.20000, 68.01670,
    "Huyện Petukhovsky, gần làng Kurort-Ozero, tỉnh Kurgan, Nga",
    "Hồ nước mặn nổi tiếng nhất tỉnh Kurgan, được ví là 'Biển Chết' của vùng nhờ độ mặn cao giúp người tắm dễ nổi. Nước muối và bùn khoáng của hồ được dùng để chữa bệnh, tạo nên một khu điều dưỡng ăn khách.",
    "Hồ Medvezhye ở phía đông tỉnh Kurgan là hồ nước mặn không thoát nổi tiếng nhất vùng, thường được gọi là 'Biển Chết của vùng Zauralye'. Nước hồ có độ mặn rất cao — vào mùa hè khi hồ cạn bớt, nồng độ muối tăng đến mức người tắm gần như không thể chìm mà nổi bồng bềnh trên mặt nước, tương tự trải nghiệm ở Biển Chết. Đáy hồ tích tụ lớp bùn khoáng (bùn sulfua) cùng muối rapa được xem là có tác dụng chữa bệnh về xương khớp, da và hệ thần kinh; nhờ đó, một khu điều dưỡng (санаторий) đã hình thành bên bờ hồ, thu hút khách đến nghỉ dưỡng và trị liệu. Cảnh quan quanh hồ là thảo nguyên phẳng lặng với bờ muối trắng, mang vẻ đẹp mộc mạc, tĩnh lặng. Đây là điểm đến thiên nhiên – nghỉ dưỡng đặc trưng nhất của tỉnh Kurgan, phù hợp cho ai muốn kết hợp du lịch với chăm sóc sức khoẻ.",
    [
        "Hồ nước mặn nổi tiếng nhất tỉnh, được ví là 'Biển Chết vùng Zauralye'.",
        "Độ mặn cao giúp người tắm nổi bồng bềnh trên mặt nước.",
        "Bùn khoáng và nước muối (rapa) được dùng để trị liệu tại khu điều dưỡng bên hồ.",
    ],
    p("Bờ hồ tiếp cận tự do; dịch vụ tắm bùn, trị liệu theo giờ của khu điều dưỡng.",
      "Ra hồ thường miễn phí; dịch vụ spa/điều dưỡng và một số bãi tắm có thu phí.",
      "Nửa ngày đến vài ngày nếu nghỉ dưỡng.",
      "Mùa hè (tháng 6–8) khi nước ấm và độ mặn cao nhất.",
      "Cách Kurgan khoảng 180 km về phía đông; nên đi ô tô hoặc đặt gói tại санаторий. Mang nước ngọt để tráng người sau khi tắm mặn; tránh để nước muối vào mắt, vết thương."),
    [
        {"title": "Wikipedia (RU) — Медвежье (озеро, Курганская область)", "url": "https://ru.wikipedia.org/wiki/Медвежье_(озеро,_Курганская_область)"},
        {"title": "VisitKurgan — Озеро Медвежье", "url": "https://visitkurgan.ru/"},
    ],
    ["park-garden", "lake", "salt-lake", "health-resort", "mud-therapy", "nature"],
    maps_text("Озеро Медвежье", "Петуховский район", "Lake Medvezhye", "Petukhovsky District", 55.20000, 68.01670),
))

# 17) Просветский дендрарий -------------------------------------------------------
RECORDS.append(rec(
    "prosvet-arboretum",
    "Vườn thực vật Prosvet (Đen-đra-ri Pro-xvét)",
    "Просветский дендрарий",
    "Prosvet Arboretum",
    ["park_garden"],
    55.59542, 65.04855,
    "Làng Stary Prosvet, huyện Ketovsky, tỉnh Kurgan, Nga",
    "Vườn thực vật (dendrarium) nổi tiếng của tỉnh Kurgan, nơi sưu tập nhiều loài cây bản địa và ngoại lai. Không gian xanh yên bình giữa rừng thông, là điểm dạo chơi và tìm hiểu thực vật học được yêu thích.",
    "Vườn thực vật Prosvet (Просветский дендрарий) nằm cạnh làng Stary Prosvet, huyện Ketovsky, cách thành phố Kurgan khoảng 25 km, là một trong những điểm thiên nhiên có giá trị nhất của tỉnh. Được gây dựng gắn với lâm trường và công tác nghiên cứu trồng rừng từ thời Xô Viết, vườn sưu tập nhiều loài cây thân gỗ và cây bụi — cả bản địa vùng Zauralye lẫn nhập nội từ nhiều vùng khí hậu khác nhau — nhằm thử nghiệm khả năng thích nghi trên đất Tây Siberia. Dạo trong vườn giữa những hàng thông, tùng, cây lá kim và cây bụi hoa theo mùa, du khách có thể tận hưởng không khí trong lành, tìm hiểu đa dạng thực vật và chụp những khung hình đẹp qua bốn mùa — đặc biệt rực rỡ vào mùa thu. Đây là điểm đến lý tưởng cho những chuyến dã ngoại nhẹ nhàng, giáo dục thiên nhiên và nghỉ ngơi gần thành phố.",
    [
        "Vườn thực vật (dendrarium) sưu tập cây bản địa và nhập nội của vùng Zauralye.",
        "Không gian xanh yên bình giữa rừng thông, gần thành phố Kurgan.",
        "Điểm dã ngoại, chụp ảnh và giáo dục thiên nhiên đẹp bốn mùa, rực rỡ vào thu.",
    ],
    p("Khu ngoài trời, tham quan ban ngày; giờ có thể thay đổi theo mùa.",
      "Thường vào tự do hoặc phí thấp; tham quan có hướng dẫn có thể thu phí.",
      "Khoảng 1–2 giờ.",
      "Cuối xuân đến mùa thu; đẹp nhất vào mùa thu lá vàng.",
      "Cách Kurgan khoảng 25 km; nên đi ô tô. Mang giày đi bộ, nước và thuốc chống muỗi vào mùa ẩm."),
    [
        {"title": "VisitKurgan — Просветский дендрарий", "url": "https://visitkurgan.ru/"},
        {"title": "Wikipedia (RU) — Кетовский район", "url": "https://ru.wikipedia.org/wiki/Кетовский_район"},
    ],
    ["park-garden", "arboretum", "botanical", "nature", "kurgan", "walking"],
    maps_text("Просветский дендрарий", "Старый Просвет", "Prosvet Arboretum", "Stary Prosvet", 55.59542, 65.04855),
))

# 18) Курорт «Озеро Горькое» (Щучанский район) ------------------------------------
RECORDS.append(rec(
    "gorkoye-lake-resort",
    "Khu nghỉ dưỡng Hồ Gorkoye (Ô-dê-rô Goóc-kôi-e)",
    "Курорт «Озеро Горькое»",
    "Lake Gorkoye Resort",
    ["park_garden"],
    55.13132, 62.52591,
    "Làng Kurort-Ozero, huyện Shchuchansky, tỉnh Kurgan, Nga",
    "Hồ khoáng–bùn nổi tiếng ở phía tây tỉnh Kurgan, trung tâm của một khu điều dưỡng lâu đời. Nước kiềm và bùn sulfua của hồ được dùng để chữa bệnh, giữa khung cảnh rừng thông yên tĩnh.",
    "Hồ Gorkoye ở huyện Shchuchansky (phía tây tỉnh Kurgan) là một trong những hồ khoáng – bùn trị liệu quý của vùng Zauralye, gắn với khu điều dưỡng đã hoạt động từ đầu thế kỷ 20. Nước hồ có tính kiềm đặc trưng, mềm và trơn khi chạm vào da, cùng lớp bùn sulfua dưới đáy được xem là có tác dụng tốt cho các bệnh về da, xương khớp và hệ thần kinh. Nhờ vậy, quanh hồ hình thành khu санаторий với các liệu trình tắm bùn, tắm khoáng và vật lý trị liệu, thu hút khách nghỉ dưỡng từ nhiều nơi. Điều làm nên nét riêng của Gorkoye là khung cảnh: hồ nằm giữa vùng rừng thông (bор) thoáng đãng, mang lại không khí trong lành và cảm giác thư thái, khác với vẻ trơ trọi của nhiều hồ muối thảo nguyên. Đây là điểm đến kết hợp nghỉ dưỡng – thiên nhiên tiêu biểu ở phía tây tỉnh, phù hợp cho những chuyến đi chăm sóc sức khoẻ.",
    [
        "Hồ khoáng – bùn trị liệu nổi tiếng, trung tâm của khu điều dưỡng lâu đời.",
        "Nước kiềm và bùn sulfua được dùng chữa bệnh da, xương khớp, thần kinh.",
        "Khung cảnh rừng thông yên tĩnh, không khí trong lành.",
    ],
    p("Bờ hồ tiếp cận tự do; dịch vụ trị liệu theo giờ và gói của санаторий.",
      "Ra hồ thường miễn phí; dịch vụ tắm bùn/điều dưỡng thu phí.",
      "Nửa ngày đến vài ngày nếu nghỉ dưỡng.",
      "Mùa hè (tháng 6–8) khi nước ấm.",
      "Cách Kurgan khoảng 150 km về phía tây; nên đi ô tô hoặc đặt gói tại санаторий. Lưu ý phân biệt với hồ Gorkoye khác ở huyện Zverinogolovsky."),
    [
        {"title": "VisitKurgan — Курорт «Озеро Горькое»", "url": "https://visitkurgan.ru/"},
        {"title": "Wikipedia (RU) — Щучанский район", "url": "https://ru.wikipedia.org/wiki/Щучанский_район"},
    ],
    ["park-garden", "lake", "health-resort", "mud-therapy", "mineral-water", "nature"],
    maps_text("Курорт Озеро Горькое", "Щучанский район", "Lake Gorkoye Resort", "Shchuchansky District", 55.13132, 62.52591),
))

# 19) Санаторий «Жемчужина Зауралья» ----------------------------------------------
RECORDS.append(rec(
    "zhemchuzhina-zauralya",
    "Khu điều dưỡng suối khoáng nóng 'Ngọc trai Zauralye' (Giem-chu-gi-na)",
    "Санаторий «Жемчужина Зауралья»",
    "Zhemchuzhina Zauralya Sanatorium (thermal springs)",
    ["park_garden"],
    56.10004, 63.55039,
    "Gần thành phố Shadrinsk, huyện Shadrinsky, tỉnh Kurgan, Nga",
    "Khu điều dưỡng nổi tiếng với suối nước khoáng nóng và nước khoáng uống của vùng Zauralye. 'Ngọc trai Zauralye' gần Shadrinsk là điểm nghỉ dưỡng – trị liệu được nhiều du khách miền Ural tìm đến.",
    "Санаторий 'Жемчучина Зауралья' (Ngọc trai Zauralye) gần thành phố Shadrinsk là một trong những khu điều dưỡng nổi tiếng nhất tỉnh Kurgan, được biết đến nhờ nguồn nước khoáng nóng và nước khoáng khai thác từ lòng đất. Điểm đặc biệt là hồ bơi và bể ngâm nước khoáng nóng (thường ấm quanh năm, kể cả giữa mùa đông giá lạnh Siberia), cùng nước khoáng uống được dùng trong các liệu trình chữa bệnh tiêu hoá và trao đổi chất. Cơ sở cung cấp nhiều dịch vụ nghỉ dưỡng – trị liệu: ngâm khoáng, tắm bùn, vật lý trị liệu, chăm sóc sức khoẻ tổng quát trong khung cảnh yên tĩnh ven vùng nông thôn Zauralye. Nhờ vị trí thuận tiện gần Shadrinsk và chất lượng nguồn khoáng, nơi đây thu hút khách từ khắp vùng Ural đến nghỉ dưỡng, đặc biệt vào cuối tuần và mùa lễ. Với du khách, đây là lựa chọn thư giãn – phục hồi sức khoẻ, và trải nghiệm tắm khoáng nóng ngoài trời giữa mùa đông là điểm nhấn khó quên.",
    [
        "Suối nước khoáng nóng và nước khoáng uống đặc trưng của vùng Zauralye.",
        "Bể ngâm khoáng nóng ấm quanh năm, kể cả mùa đông Siberia.",
        "Liệu trình nghỉ dưỡng – trị liệu đa dạng gần thành phố Shadrinsk.",
    ],
    p("Dịch vụ theo giờ mở cửa của санаторий; hồ khoáng nóng thường mở cả ngày cho khách đăng ký.",
      "Có thu phí theo buổi hoặc gói lưu trú; nên đặt trước.",
      "Nửa ngày (dùng hồ khoáng) đến vài ngày nếu lưu trú.",
      "Quanh năm; tắm khoáng nóng ngoài trời đặc biệt ấn tượng vào mùa đông.",
      "Cách Kurgan khoảng 145 km, gần Shadrinsk; nên đi ô tô. Mang đồ bơi, dép; đặt lịch trước vào cuối tuần cao điểm."),
    [
        {"title": "VisitKurgan — Санаторий «Жемчужина Зауралья»", "url": "https://visitkurgan.ru/"},
        {"title": "Wikipedia (RU) — Шадринск", "url": "https://ru.wikipedia.org/wiki/Шадринск"},
    ],
    ["park-garden", "thermal-springs", "health-resort", "mineral-water", "shadrinsk", "wellness"],
    maps_text("Санаторий Жемчужина Зауралья", "Шадринск", "Zhemchuzhina Zauralya Sanatorium", "Shadrinsk", 56.10004, 63.55039),
))

# ============================ NHÀ THỜ (church) ============================

# 20) Богоявленский кафедральный собор (Курган) -----------------------------------
RECORDS.append(rec(
    "bogoyavlensky-cathedral-kurgan",
    "Nhà thờ chính toà Bogoyavlensky (Hiển Linh) ở Kurgan",
    "Богоявленский кафедральный собор",
    "Epiphany Cathedral (Kurgan)",
    ["church"],
    55.42923, 65.34073,
    "Phố Klimova 3, bên bờ sông Tobol, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Nhà thờ chính toà mới của Kurgan bên bờ sông Tobol, với những mái vòm mạ vàng nổi bật. Được xây dựng lại đầu thế kỷ 21 để tái hiện ngôi thánh đường Bogoyavlensky lịch sử từng bị phá huỷ thời Xô Viết.",
    "Nhà thờ chính toà Bogoyavlensky (Hiển Linh) là một trong những công trình tôn giáo bề thế và mới mẻ nhất của Kurgan, toạ lạc bên bờ sông Tobol ở khu trung tâm. Ngôi thánh đường được xây dựng lại vào đầu thế kỷ 21 nhằm khôi phục truyền thống của nhà thờ Bogoyavlensky lịch sử vốn từng đứng ở thành phố nhưng bị phá huỷ trong thời kỳ vô thần Xô Viết. Với khối kiến trúc lớn theo phong cách Nga cổ, những mái vòm hành củ tỏi mạ vàng lấp lánh và tháp chuông cao, nhà thờ trở thành một điểm nhấn cảnh quan bên sông và là nhà thờ chính toà quan trọng của giáo phận Kurgan. Nội thất rộng rãi với các bức icon, đèn chùm và bàn thờ được trang hoàng công phu tạo nên không gian trang nghiêm cho các buổi lễ lớn. Đây là điểm đến để du khách vừa chiêm ngưỡng kiến trúc Chính thống giáo đương đại, vừa ngắm cảnh sông Tobol và cảm nhận đời sống tôn giáo hồi sinh của thành phố.",
    [
        "Nhà thờ chính toà mới bên bờ sông Tobol với mái vòm mạ vàng nổi bật.",
        "Xây dựng lại đầu thế kỷ 21, nối tiếp truyền thống nhà thờ Bogoyavlensky lịch sử.",
        "Kiến trúc Nga cổ bề thế và nội thất icon trang hoàng công phu.",
    ],
    p("Mở cửa hàng ngày, thường từ khoảng 7:00–8:00; các buổi lễ sáng và chiều theo lịch phụng vụ.",
      "Vào cửa tự do (miễn phí); tuỳ tâm quyên góp.",
      "Khoảng 30–45 phút.",
      "Quanh năm; các dịp lễ lớn để cảm nhận không khí phụng vụ.",
      "Trang phục lịch sự, kín đáo; nữ nên mang khăn trùm đầu. Hạn chế chụp ảnh trong giờ lễ; kết hợp dạo bờ sông Tobol."),
    [
        {"title": "Sobory.ru — Богоявленский собор (Курган)", "url": "https://sobory.ru/geo/?ll=65.34073,55.42923"},
        {"title": "Wikipedia (RU) — Курганская епархия", "url": "https://ru.wikipedia.org/wiki/Курганская_епархия"},
    ],
    ["church", "cathedral", "orthodox", "kurgan", "architecture", "tobol"],
    maps_text("Богоявленский кафедральный собор", "Курган", "Epiphany Cathedral", "Kurgan", 55.42923, 65.34073),
))

# 21) Спасо-Преображенский собор (Шадринск) ---------------------------------------
RECORDS.append(rec(
    "shadrinsk-spaso-preobrazhensky",
    "Nhà thờ chính toà Chúa Biến Hình ở Shadrinsk (Xpa-xô Prê-a-bra-gien-xki)",
    "Спасо-Преображенский собор (Шадринск)",
    "Cathedral of the Transfiguration (Shadrinsk)",
    ["church"],
    56.07707, 63.63350,
    "Thành phố Shadrinsk, tỉnh Kurgan, Nga",
    "Nhà thờ đá cổ nhất và tiêu biểu nhất của thành phố Shadrinsk, xây từ giữa thế kỷ 18. Công trình Baroque Ural với tháp chuông cao là biểu tượng kiến trúc – tâm linh của cả vùng bắc tỉnh Kurgan.",
    "Nhà thờ chính toà Chúa Biến Hình (Спасо-Преображенский собор) là công trình tôn giáo cổ và tiêu biểu nhất của Shadrinsk — thành phố lịch sử lớn thứ hai của tỉnh Kurgan. Được khởi công từ giữa thế kỷ 18 (khoảng thập niên 1770) bằng đá, thay cho các nhà thờ gỗ trước đó, đây là một trong những nhà thờ đá lâu đời nhất vùng Zauralye. Kiến trúc mang phong cách 'Baroque Ural – Siberia' đặc trưng với bố cục nhiều tầng, tháp chuông cao vươn lên trên nền phố cổ và những đường nét trang trí mềm mại. Trải qua thời kỳ Xô Viết bị đóng cửa và sử dụng sai mục đích, nhà thờ đã được trả lại cho Giáo hội và trùng tu, khôi phục vai trò trung tâm đời sống Chính thống giáo của Shadrinsk. Cùng với quần thể nhà thương nhân và các nhà thờ khác, công trình góp phần tạo nên diện mạo đô thị lịch sử quyến rũ của thành phố. Đây là điểm không thể bỏ qua khi tham quan Shadrinsk.",
    [
        "Nhà thờ đá cổ và tiêu biểu nhất Shadrinsk (từ khoảng thập niên 1770).",
        "Kiến trúc Baroque Ural – Siberia với tháp chuông cao đặc trưng.",
        "Biểu tượng kiến trúc – tâm linh của thành phố lịch sử Shadrinsk.",
    ],
    p("Mở cửa hàng ngày, thường từ khoảng 7:00–8:00; các buổi lễ theo lịch phụng vụ.",
      "Vào cửa tự do (miễn phí); tuỳ tâm quyên góp.",
      "Khoảng 30–45 phút.",
      "Quanh năm; các dịp lễ lớn có không khí đặc biệt.",
      "Cách Kurgan khoảng 145 km; kết hợp Bảo tàng địa phương Shadrinsk và phố thương nhân. Trang phục kín đáo, nữ mang khăn trùm đầu."),
    [
        {"title": "Wikipedia (RU) — Спасо-Преображенский собор (Шадринск)", "url": "https://ru.wikipedia.org/wiki/Спасо-Преображенский_собор_(Шадринск)"},
        {"title": "Sobory.ru — Спасо-Преображенский собор (Шадринск)", "url": "https://sobory.ru/geo/?ll=63.63350,56.07707"},
    ],
    ["church", "cathedral", "orthodox", "shadrinsk", "baroque", "architecture", "history"],
    maps_text("Спасо-Преображенский собор", "Шадринск", "Cathedral of the Transfiguration", "Shadrinsk", 56.07707, 63.63350),
))

# 22) Николаевская церковь (Далматово) --------------------------------------------
RECORDS.append(rec(
    "dalmatovo-nikolaevsky-church",
    "Nhà thờ Thánh Nikolay ở Dalmatovo (Ni-ka-lai-ép-xcai-a)",
    "Николаевская церковь (Далматово)",
    "St. Nicholas Church (Dalmatovo)",
    ["church"],
    56.2575, 62.9306,
    "Phố Sovetskaya 162, thành phố Dalmatovo, tỉnh Kurgan, Nga",
    "Nhà thờ giáo xứ lịch sử của thị trấn Dalmatovo, gần quần thể tu viện Uspensky nổi tiếng. Ngôi thánh đường bằng đá là một phần di sản kiến trúc Chính thống giáo của vùng.",
    "Nhà thờ Thánh Nikolay (Николаевская церковь) là một trong những nhà thờ giáo xứ lịch sử của thị trấn Dalmatovo — nơi vốn nổi tiếng nhờ tu viện–pháo đài Uspensky cổ kính. Được xây bằng đá vào thế kỷ 19, nhà thờ phục vụ cộng đồng cư dân thị trấn hình thành quanh tu viện, và mang những nét kiến trúc Chính thống giáo tỉnh lẻ đặc trưng của vùng Zauralye. Giống nhiều nhà thờ Nga khác, công trình từng bị đóng cửa và chịu hư hại trong thời kỳ Xô Viết, sau đó được trả lại cho tín đồ và dần trùng tu, khôi phục sinh hoạt tôn giáo. Nằm không xa quần thể tu viện Dalmatovsky, nhà thờ Thánh Nikolay bổ sung thêm chiều sâu cho hành trình khám phá Dalmatovo — một trong những trung tâm lịch sử – tâm linh lâu đời nhất của tỉnh Kurgan. Du khách có thể ghé thăm kết hợp trong cùng chuyến đi tới tu viện.",
    [
        "Nhà thờ giáo xứ lịch sử bằng đá của thị trấn Dalmatovo (thế kỷ 19).",
        "Gắn với cộng đồng cư dân hình thành quanh tu viện Uspensky cổ kính.",
        "Bổ sung chiều sâu cho hành trình khám phá trung tâm lịch sử – tâm linh Dalmatovo.",
    ],
    p("Mở cửa theo lịch phụng vụ, thường vào giờ lễ sáng và chiều.",
      "Vào cửa tự do (miễn phí); tuỳ tâm quyên góp.",
      "Khoảng 20–30 phút.",
      "Quanh năm; kết hợp mùa ấm để đi tu viện Dalmatovsky.",
      "Cách Kurgan khoảng 190 km; đi cùng chuyến thăm tu viện Uspensky Dalmatovsky. Trang phục kín đáo, nữ mang khăn trùm đầu."),
    [
        {"title": "Sobory.ru — Церковь Николая Чудотворца (Далматово)", "url": "https://sobory.ru/geo/?ll=62.9306,56.2575"},
        {"title": "Wikipedia (RU) — Далматово", "url": "https://ru.wikipedia.org/wiki/Далматово"},
    ],
    ["church", "orthodox", "dalmatovo", "architecture", "history"],
    maps_text("Николаевская церковь", "Далматово", "St. Nicholas Church", "Dalmatovo", 56.2575, 62.9306),
))

# 23) Свято-Духовский храм (Курган) -----------------------------------------------
RECORDS.append(rec(
    "svyato-dukhovsky-church-kurgan",
    "Nhà thờ Chúa Thánh Thần Giáng Lâm ở Kurgan (Xvia-tô Đu-khốp-xki)",
    "Свято-Духовский храм",
    "Church of the Descent of the Holy Spirit (Kurgan)",
    ["church"],
    55.4286, 65.3946,
    "Khu Smolino, ngõ Maly 12, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Nhà thờ Chính thống giáo ở khu Smolino của Kurgan, một điểm thờ phụng gắn với đời sống giáo xứ địa phương. Không gian yên tĩnh, mộc mạc, tách khỏi nhịp sống trung tâm.",
    "Nhà thờ Chúa Thánh Thần Giáng Lâm (Свято-Духовский храм, còn gọi là nhà thờ Sошествия Святого Духа) nằm ở khu Smolino thuộc thành phố Kurgan. Đây là một giáo đường phục vụ cộng đồng tín đồ ở khu vực ngoại vi, mang không khí trầm mặc, gần gũi hơn so với các nhà thờ lớn ở trung tâm. Trong bối cảnh đời sống Chính thống giáo hồi sinh mạnh mẽ ở nước Nga sau thời Xô Viết, nhiều giáo xứ như Свято-Духовский храm được lập hoặc khôi phục để đáp ứng nhu cầu tâm linh của người dân từng khu phố. Ngôi nhà thờ với mái vòm và thánh giá vươn lên giữa khu dân cư là điểm sinh hoạt tôn giáo và tụ họp của cộng đồng địa phương. Với du khách muốn tìm hiểu đời sống Chính thống giáo đời thường của người Kurgan — bên ngoài những thánh đường du lịch nổi tiếng — đây là một điểm ghé thăm yên bình, chân thực.",
    [
        "Nhà thờ Chính thống giáo ở khu Smolino, ngoại vi thành phố Kurgan.",
        "Không gian yên tĩnh, mộc mạc gắn với đời sống giáo xứ địa phương.",
        "Phản ánh sự hồi sinh của các giáo xứ Nga sau thời Xô Viết.",
    ],
    p("Mở cửa theo lịch phụng vụ, thường vào giờ lễ sáng và chiều.",
      "Vào cửa tự do (miễn phí); tuỳ tâm quyên góp.",
      "Khoảng 20–30 phút.",
      "Quanh năm; vào giờ lễ để cảm nhận không khí phụng vụ.",
      "Nằm ở khu Smolino, cách trung tâm vài km; nên đi ô tô hoặc taxi. Trang phục kín đáo, nữ mang khăn trùm đầu."),
    [
        {"title": "Sobory.ru — Церковь Сошествия Святого Духа (Курган)", "url": "https://sobory.ru/geo/?ll=65.3946,55.4286"},
        {"title": "Wikipedia (RU) — Курганская епархия", "url": "https://ru.wikipedia.org/wiki/Курганская_епархия"},
    ],
    ["church", "orthodox", "kurgan", "smolino", "parish"],
    maps_text("Свято-Духовский храм", "Курган", "Church of the Descent of the Holy Spirit", "Kurgan", 55.4286, 65.3946),
))

# ============================ CẦU (bridge) ============================

# 24) Кировский мост (Курган) -----------------------------------------------------
RECORDS.append(rec(
    "kirovsky-bridge-kurgan",
    "Cầu Kirovsky bắc qua sông Tobol (Ki-rốp-xki)",
    "Кировский мост",
    "Kirovsky Bridge (Kurgan)",
    ["bridge"],
    55.428556, 65.34650,
    "Bắc qua sông Tobol, nối trung tâm với các khu phía nam, thành phố Kurgan, tỉnh Kurgan, Nga",
    "Cây cầu trung tâm bắc qua sông Tobol ở Kurgan, nối khu trung tâm lịch sử với các quận phía nam thành phố. Đây là một trong những cây cầu chính và điểm ngắm cảnh sông quen thuộc.",
    "Cầu Kirovsky là một trong những cây cầu chính bắc qua sông Tobol tại thành phố Kurgan, nối khu trung tâm lịch sử ở tả ngạn với các khu dân cư phía nam. Sông Tobol chia thành phố thành hai phần, nên những cây cầu như Kirovsky giữ vai trò huyết mạch giao thông và gắn bó mật thiết với đời sống đô thị. Từ trên cầu và khu bờ kè lân cận, du khách có thể ngắm dòng Tobol uốn lượn, đường chân trời thành phố cùng những mái vòm nhà thờ Bogoyavlensky phía bờ trung tâm — một khung cảnh đẹp, đặc biệt vào lúc hoàng hôn hay khi thành phố lên đèn. Khu vực quanh cầu và bờ sông cũng là nơi người dân dạo bộ, đạp xe và nghỉ ngơi. Tuy là công trình giao thông, cầu Kirovsky và cảnh quan sông Tobol tạo nên một điểm dừng chân dễ chịu, giúp du khách cảm nhận nhịp sống và địa thế sông nước của Kurgan.",
    [
        "Cây cầu trung tâm bắc qua sông Tobol, huyết mạch của thành phố Kurgan.",
        "Điểm ngắm cảnh sông Tobol và đường chân trời thành phố, đẹp lúc hoàng hôn.",
        "Khu bờ kè lân cận là nơi dạo bộ, đạp xe, nghỉ ngơi của người dân.",
    ],
    p("Không gian công cộng, qua lại và ngắm cảnh tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15–30 phút (kể cả dạo bờ kè).",
      "Mùa hè và mùa thu; đẹp lúc hoàng hôn và khi thành phố lên đèn.",
      "Kết hợp dạo bờ sông Tobol và ngắm nhà thờ Bogoyavlensky gần đó; chú ý an toàn giao thông khi chụp ảnh trên cầu."),
    [
        {"title": "Wikipedia (RU) — Курган (город)", "url": "https://ru.wikipedia.org/wiki/Курган_(город)"},
        {"title": "VisitKurgan — Река Тобол и мосты Кургана", "url": "https://visitkurgan.ru/"},
    ],
    ["bridge", "tobol", "river", "kurgan", "cityscape", "walking"],
    maps_text("Кировский мост", "Курган", "Kirovsky Bridge", "Kurgan", 55.428556, 65.34650),
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
