# -*- coding: utf-8 -*-
"""_add_places_tomsk_20260729_021500.py — VÙNG: Tỉnh Tomsk (Томская область)
(lần chạy tự động 2026-07-29).

Bối cảnh: tomsk.json hiện có 7 địa điểm (Деревянное зодчество, Императорский университет/ТГУ,
памятник Чехову, Воскресенская церковь, Богоявленский собор, Новособорная площадь, музей «Следственная
тюрьма НКВД»). Bổ sung 24 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31.
TRÁNH trùng 7 điểm trên (đặc biệt KHÔNG thêm lại: памятник Чехову, Воскресенская церковь, Богоявленский
собор, Новособорная площадь, музей НКВД, деревянное зодчество, ТГУ).

Trung tâm là thành phố Tomsk (Воскресенская гора, проспект Ленина, набережная Томи); mở rộng ra Томский
район (Семилужки, Синий Утёс, Таловские чаши) và bắc tỉnh (Нарым - làng lưu đày cổ).

Phân bố loại hình (24 bản ghi mới):
- museum (5): краеведческий музей им. Шатилова, художественный музей, музей славянской мифологии,
  музей истории Томска (пожарная каланча), Нарымский музей политической ссылки (+square_street).
- theatre (2): областной театр драмы, театр живых кукол «2+ку».
- church (4): Петропавловский собор, Богородице-Алексиевский монастырь, Красная соборная мечеть (tag mosque),
  Польский костёл Покрова.
- fortress (2): Воскресенская гора / камень основания Томска (+monument), Семилуженский острог.
- square_street (3): проспект Ленина, набережная реки Томи, Нарым (кèm museum ở trên).
- monument (3): памятник рублю, памятник счастью «Щас спою» (волк), Дом с драконами.
- park_garden (5): Университетская роща, Сибирский ботанический сад ТГУ, Лагерный сад (+monument),
  Городской сад, Синий Утёс.
- other/nature (1): Таловские чаши (природный памятник) → xếp park_garden.

TOẠ ĐỘ — xác minh chéo (Yandex Maps org, 2GIS firm/geo, sobory.ru, ru.wikipedia, openarium, 2026-07-29).
Phạm vi tỉnh Tomsk lat ~55.7–61, lon ~75–89 (TP Tomsk ~56.49, 84.95) — tất cả toạ độ trong phạm vi, KHÔNG
đảo lat/lon:
  краеведческий музей (Асташевский особняк) 56.476612,84.950721 (Yandex, пр. Ленина 75);
  художественный музей 56.482662,84.947406 (Yandex, пер. Нахановича 3); музей славянской мифологии
  56.488756,84.954146 (2GIS, Загорная 12); музей истории Томска/каланча 56.488875,84.952742 (Yandex,
  Бакунина 3); театр драмы 56.487279,84.947094 (2GIS, пл. Ленина 4); театр «2+ку» 56.456912,84.941683
  (2GIS, Южный пер. 29 — địa chỉ HIỆN HÀNH, không phải Шишкова 14); Петропавловский собор 56.480543,84.969941
  (sobory.ru, Алтайская 47); Богородице-Алексиевский монастырь 56.481865,84.955065 (sobory.ru, Крылова 12);
  Красная соборная мечеть 56.478600,84.945541 (2GIS, Татарская 24); Польский костёл 56.489743,84.952608
  (2GIS, Бакунина 4); Воскресенская гора/камень основания 56.488614,84.952841 (2GIS); проспект Ленина
  56.477900,84.951500 (điểm giữa tuyến, gần Новособорной); набережная Томи 56.485556,84.944722 (điểm đại
  diện, у устья Ушайки); памятник рублю 56.474172,84.950875 (openarium, Новособорная пл. — điểm 2GIS bị
  gán SAI về Воскресенская гора nên KHÔNG dùng); памятник счастью «волк» 56.477329,84.991911 (2GIS, Шевченко
  19/1); Дом с драконами 56.472272,84.966002 (2GIS, Красноармейская 68); Университетская роща 56.469577,
  84.948510 (Yandex, пр. Ленина 36); ботанический сад ТГУ 56.466505,84.946180 (Yandex, пр. Ленина 34/1);
  Лагерный сад 56.453518,84.948376 (Yandex, ул. Нахимова, берег Томи); Городской сад 56.472466,84.954782
  (Yandex, Герцена 6); Таловские чаши 56.300000,85.416667 (ru.wiki, Томский р-н, sai số ~±1 км do toạ độ
  chỉ đến phút cung); Синий Утёс 56.334991,84.921460 (2GIS, у Коларово); Нарым 58.925913,81.598748 (ru.wiki,
  Парабельский р-н); Семилуженский острог 56.617541,85.353229 (2GIS, с. Семилужки).

GHI CHÚ:
- Красная соборная мечеть xếp category "church" theo quy ước dự án cho công trình tôn giáo, kèm tag "mosque".
- «Дом с драконами» và «Дом с жар-птицами» là kiến trúc gỗ; «Дом с жар-птицами» đã nằm trong bản ghi
  «Деревянное зодчество Томска» có sẵn (Ngôi nhà Chim Lửa) → CHỈ thêm riêng «Дом с драконами» (đủ nổi bật).
- Театр «2+ку»: sau hoả hoạn/di dời, địa chỉ hiện hành theo 2GIS/Yandex là Южный переулок 29 (gần Лагерный
  сад), KHÔNG còn ở Шишкова 14 → dùng toạ độ hiện hành.
- Университетская роща tách riêng khỏi bản ghi ТГУ đã có (là công viên - vườn thực vật lịch sử độc lập).
- KHÔNG thêm lại các điểm ĐÃ CÓ: памятник Чехову, Воскресенская церковь, Богоявленский собор,
  Новособорная площадь, музей НКВД. KHÔNG bịa toạ độ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_tomsk_20260729_021500.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "tomsk"
REGION_NAME_VI = "Tỉnh Tomsk"
FD = "Vùng Siberia"


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

# 1) Томский областной краеведческий музей им. М.Б. Шатилова -----------------------
RECORDS.append(rec(
    "tomsk-regional-museum",
    "Bảo tàng Địa phương học Tỉnh Tomsk (mang tên M. Shatilov)",
    "Томский областной краеведческий музей им. М.Б. Шатилова",
    "Tomsk Regional Museum of Local Lore",
    ["museum"],
    56.476612, 84.950721,
    "Đại lộ Lenina 75 (dinh thự Astashev), trung tâm thành phố Tomsk, tỉnh Tomsk, Nga",
    "Bảo tàng địa phương học chính của tỉnh Tomsk, đặt trong dinh thự Astashev tráng lệ giữa trung tâm. Đây là nơi lý tưởng để hiểu tổng thể lịch sử, thiên nhiên và văn hoá đa sắc tộc của vùng đất Siberia bên sông Tom.",
    "Bảo tàng Địa phương học Tỉnh Tomsk mang tên nhà nghiên cứu M. B. Shatilov là 'kho ký ức' của cả vùng, thành lập năm 1922 và ngày nay đặt trong dinh thự cổ của thương gia - thị trưởng Astashev trên đại lộ Lenina - một công trình kiến trúc thế kỷ 19 mang nét cổ điển với mái tháp và nội thất sang trọng. Bộ sưu tập trải rộng từ khảo cổ, dân tộc học của các dân tộc Siberia, lịch sử khai hoang và đời sống thương nhân Tomsk, đến những trang sử bi thương của thế kỷ 20. Các gian trưng bày dẫn dắt người xem qua thời kỳ pháo đài gỗ đầu tiên, con đường buôn bán trà xuyên Siberia, thời hoàng kim của thành phố đại học, cho tới giai đoạn Xô Viết. Bảo tàng có nhiều chi nhánh trong tỉnh và thường xuyên tổ chức triển lãm chuyên đề. Với du khách, đây là điểm khởi đầu tốt nhất để nắm bắt bức tranh toàn cảnh trước khi khám phá phố phường Tomsk.",
    [
        "Đặt trong dinh thự Astashev cổ kính (thế kỷ 19) - một kiến trúc đẹp bậc nhất trên đại lộ Lenina",
        "Sưu tập phong phú về khảo cổ, dân tộc học và lịch sử khai hoang vùng Siberia",
        "Điểm khởi đầu lý tưởng để hiểu tổng thể lịch sử và văn hoá tỉnh Tomsk",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–19:00; nghỉ Thứ Hai (nên kiểm tra lịch trước khi đến).",
      "Vé vào cửa ở mức phải chăng (vài trăm rúp); có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm; rất hợp cho những ngày thời tiết xấu.",
      "Nằm ngay trung tâm, gần Quảng trường Novosobornaya; thuyết minh chủ yếu bằng tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Томский областной краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Томский_областной_краеведческий_музей"},
        {"title": "Culture.ru — Томский областной краеведческий музей", "url": "https://www.culture.ru/institutes/12703/tomskii-oblastnoi-kraevedcheskii-muzei-im-m-b-shatilova"},
    ],
    ["museum", "history", "local-lore", "tomsk", "siberia", "architecture"],
    maps_text("Томский областной краеведческий музей", "Томск", "Tomsk Regional Museum of Local Lore", "Tomsk", 56.476612, 84.950721),
))

# 2) Томский областной художественный музей ---------------------------------------
RECORDS.append(rec(
    "tomsk-art-museum",
    "Bảo tàng Mỹ thuật Tỉnh Tomsk",
    "Томский областной художественный музей",
    "Tomsk Regional Art Museum",
    ["museum"],
    56.482662, 84.947406,
    "Ngõ Nakhanovicha 3, trung tâm thành phố Tomsk, tỉnh Tomsk, Nga",
    "Bảo tàng mỹ thuật hàng đầu của tỉnh, lưu giữ tranh và tác phẩm nghệ thuật từ thời kỳ cổ điển Nga, các danh hoạ thế kỷ 18–20 cho đến nghệ thuật Siberia đương đại. Không gian trưng bày ấm cúng trong một toà nhà lịch sử ở trung tâm.",
    "Bảo tàng Mỹ thuật Tỉnh Tomsk là điểm đến dành cho người yêu hội hoạ, tách ra từ bảo tàng địa phương học và trở thành một bảo tàng độc lập từ năm 1979. Bộ sưu tập trải dài từ nghệ thuật tôn giáo Nga cổ (biểu tượng - icon), tranh của các danh hoạ thế kỷ 18–19, đến mỹ thuật Xô Viết và nghệ thuật đương đại của các hoạ sĩ Siberia. Bảo tàng cũng tự hào có mảng nghệ thuật phương Tây Âu và một số hiện vật nghệ thuật phương Đông. Đặt trong một toà nhà lịch sử duyên dáng ở trung tâm Tomsk, nơi đây thường xuyên luân phiên các triển lãm chuyên đề, tổ chức chương trình giáo dục và những buổi giao lưu nghệ thuật. Đây là điểm dừng tinh tế, yên tĩnh giữa hành trình khám phá thành phố gỗ.",
    [
        "Sưu tập trải dài từ icon Nga cổ, danh hoạ thế kỷ 18–19 đến mỹ thuật Siberia đương đại",
        "Có cả mảng nghệ thuật Tây Âu và một số hiện vật phương Đông",
        "Không gian triển lãm ấm cúng trong toà nhà lịch sử ngay trung tâm",
    ],
    p("Thứ Tư–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai và Thứ Ba (nên kiểm tra trước).",
      "Vé ở mức phải chăng; có ưu đãi cho học sinh, sinh viên và người cao tuổi.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; hợp cả ngày mưa hay tuyết.",
      "Gần Quảng trường Lenina và nhà hát kịch; thuyết minh chủ yếu tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Томский областной художественный музей", "url": "https://ru.wikipedia.org/wiki/Томский_областной_художественный_музей"},
        {"title": "Culture.ru — Томский областной художественный музей", "url": "https://www.culture.ru/institutes/12704/tomskii-oblastnoi-khudozhestvennyi-muzei"},
    ],
    ["museum", "art", "gallery", "tomsk", "siberia", "culture"],
    maps_text("Томский областной художественный музей", "Томск", "Tomsk Regional Art Museum", "Tomsk", 56.482662, 84.947406),
))

# 3) Первый музей славянской мифологии ---------------------------------------------
RECORDS.append(rec(
    "slavic-mythology-museum-tomsk",
    "Bảo tàng Thần thoại Slav đầu tiên",
    "Первый музей славянской мифологии",
    "First Museum of Slavic Mythology",
    ["museum"],
    56.488756, 84.954146,
    "Phố Zagornaya 12, gần đồi Voskresenskaya, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Bảo tàng tư nhân độc đáo dành riêng cho thần thoại, cổ tích và văn hoá dân gian của các dân tộc Slav. Không gian trưng bày sống động với tranh, tượng và những nhân vật huyền thoại như Baba Yaga, Vodyanoy hay chim lửa.",
    "Bảo tàng Thần thoại Slav đầu tiên (mở cửa năm 2007) là một điểm đến hiếm có ở Nga, hoàn toàn dành cho thế giới huyền thoại, cổ tích và tín ngưỡng dân gian của người Slav cổ. Bộ sưu tập gồm tranh của các hoạ sĩ đương đại lấy cảm hứng từ sử thi bylina, tượng, đồ thủ công, bùa hộ mệnh và những phiên bản tái hiện các vị thần, tinh linh trong thần thoại Slav - từ Perun, Veles đến những nhân vật quen thuộc như Baba Yaga, Vodyanoy (thần nước), Domovoy (thần nhà) hay Zhar-ptitsa (chim lửa). Không gian được thiết kế giàu tính kể chuyện, phù hợp cả với người lớn lẫn trẻ em, kèm nhiều chương trình tương tác, lớp học sáng tạo và một cửa hàng lưu niệm thủ công. Đây là nơi lý tưởng để chạm vào cội nguồn văn hoá dân gian Nga qua lăng kính nghệ thuật đương đại.",
    [
        "Bảo tàng độc nhất về thần thoại và cổ tích Slav với tranh, tượng, đồ thủ công dân gian",
        "Tái hiện các nhân vật huyền thoại: Baba Yaga, Vodyanoy, Domovoy, chim lửa Zhar-ptitsa",
        "Không gian giàu tính kể chuyện, hợp cả gia đình có trẻ em, có lớp học sáng tạo",
    ],
    p("Mở cửa gần như hằng ngày, khoảng 10:00–19:00 (nên kiểm tra lịch trước).",
      "Vé ở mức phải chăng; có tour thuyết minh và lớp học tính thêm phí.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; rất hợp ngày lạnh hoặc mưa.",
      "Gần đồi Voskresenskaya - có thể kết hợp tham quan; nên đặt trước nếu muốn hướng dẫn viên."),
    [
        {"title": "Wikipedia (RU) — Первый музей славянской мифологии", "url": "https://ru.wikipedia.org/wiki/Первый_музей_славянской_мифологии"},
        {"title": "Trang chính thức — slavmuseum.ru", "url": "https://slavmuseum.ru/"},
    ],
    ["museum", "folklore", "slavic", "mythology", "tomsk", "family"],
    maps_text("Первый музей славянской мифологии", "Томск", "First Museum of Slavic Mythology", "Tomsk", 56.488756, 84.954146),
    official_site="https://slavmuseum.ru/",
))

# 4) Музей истории Томска (пожарная каланча) ---------------------------------------
RECORDS.append(rec(
    "tomsk-history-museum-fire-tower",
    "Bảo tàng Lịch sử Thành phố Tomsk (tháp cứu hoả)",
    "Музей истории Томска",
    "Museum of the History of Tomsk",
    ["museum"],
    56.488875, 84.952742,
    "Phố Bakunina 3, trên đồi Voskresenskaya, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Bảo tàng kể câu chuyện thành phố Tomsk từ pháo đài gỗ đầu tiên, nổi bật với tháp cứu hoả (kalancha) cổ có đài ngắm toàn cảnh và bức tượng 'người lính cứu hoả' vui nhộn trên nóc. Nằm ngay cái nôi khai sinh của thành phố.",
    "Bảo tàng Lịch sử Thành phố Tomsk toạ lạc trên đồi Voskresenskaya - chính nơi pháo đài gỗ đầu tiên được dựng năm 1604 khai sinh ra thành phố. Bảo tàng đặt trong một toà nhà cổ gắn liền với tháp cứu hoả (pozharnaya kalancha) mang tính biểu tượng: du khách có thể leo lên đài quan sát trên tháp để phóng tầm mắt bao quát khu phố cổ, mái vòm nhà thờ và dòng sông Tom. Trên nóc tháp còn có bức tượng 'người lính cứu hoả' đội mũ đồng đứng canh - một chi tiết được người dân yêu thích. Bên trong, các gian trưng bày tái hiện lịch sử đô thị: từ đời sống pháo đài, thời thương gia buôn trà, cho đến ký ức thế kỷ 20, kèm nhiều triển lãm tương tác. Đây là điểm dừng gọn gàng nhưng giàu ý nghĩa, gắn liền với cả cụm di tích trên đồi Voskresenskaya.",
    [
        "Tháp cứu hoả cổ với đài quan sát ngắm toàn cảnh khu phố cổ và sông Tom",
        "Tượng 'người lính cứu hoả' đồng vui nhộn đứng canh trên nóc tháp - biểu tượng được yêu thích",
        "Nằm ngay đồi Voskresenskaya - cái nôi khai sinh thành phố Tomsk năm 1604",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé rẻ; leo tháp quan sát có thể tính vé riêng.",
      "Khoảng 1–1,5 giờ.",
      "Mùa hè và đầu thu để lên đài ngắm cảnh đẹp nhất.",
      "Kết hợp tham quan cả cụm đồi Voskresenskaya (camень основания, костёл); mang giày thoải mái để leo tháp."),
    [
        {"title": "Wikipedia (RU) — Музей истории Томска", "url": "https://ru.wikipedia.org/wiki/Музей_истории_Томска"},
        {"title": "Culture.ru — Музей истории Томска", "url": "https://www.culture.ru/institutes/12718/muzei-istorii-tomska"},
    ],
    ["museum", "history", "fire-tower", "viewpoint", "tomsk", "old-town"],
    maps_text("Музей истории Томска", "Томск", "Museum of the History of Tomsk", "Tomsk", 56.488875, 84.952742),
))

# ============================ NHÀ HÁT (theatre) ============================

# 5) Томский областной театр драмы ------------------------------------------------
RECORDS.append(rec(
    "tomsk-drama-theatre",
    "Nhà hát Kịch Tỉnh Tomsk",
    "Томский областной театр драмы",
    "Tomsk Regional Drama Theatre",
    ["theatre"],
    56.487279, 84.947094,
    "Quảng trường Lenina 4, trung tâm thành phố Tomsk, tỉnh Tomsk, Nga",
    "Nhà hát kịch chính của thành phố, một trong những đoàn kịch lâu đời của Siberia, đặt trong toà nhà hiện đại bề thế bên Quảng trường Lenina. Sân khấu sáng đèn quanh năm với các vở kịch cổ điển Nga và đương đại.",
    "Nhà hát Kịch Tỉnh Tomsk có bề dày lịch sử từ thế kỷ 19, là một trong những đoàn kịch chuyên nghiệp lâu đời và uy tín của vùng Siberia. Toà nhà hiện nay - khối kiến trúc hoành tráng thời Xô Viết bên Quảng trường Lenina, gần bờ sông Tom - có sân khấu lớn và không gian khán phòng rộng rãi. Tiết mục của nhà hát phong phú, từ các vở kinh điển Nga (Chekhov, Ostrovsky, Gogol) đến kịch nước ngoài và những dàn dựng đương đại, phục vụ cả khán giả lớn tuổi lẫn giới trẻ. Nhà hát thường xuyên tham gia các liên hoan sân khấu, mời đạo diễn khách và duy trì đời sống văn hoá sôi động cho thành phố đại học. Với du khách, một buổi tối xem kịch ở đây là cách thú vị để cảm nhận nhịp sống văn hoá của Tomsk, ngay cả khi chưa thạo tiếng Nga vẫn có thể thưởng thức không khí và thiết kế sân khấu.",
    [
        "Một trong những đoàn kịch chuyên nghiệp lâu đời của Siberia",
        "Toà nhà bề thế bên Quảng trường Lenina, gần bờ sông Tom",
        "Tiết mục đa dạng: kinh điển Nga, kịch nước ngoài và dàn dựng đương đại",
    ],
    p("Buổi biểu diễn thường vào buổi tối (khoảng 18:00–19:00); phòng vé mở ban ngày.",
      "Giá vé tuỳ vở và vị trí ghế, nhìn chung phải chăng.",
      "Một buổi diễn khoảng 2–3 giờ.",
      "Mùa thu, đông và xuân (mùa diễn); nên đặt vé trước.",
      "Xem lịch diễn trên trang chính thức; phần lớn vở diễn bằng tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Томский областной театр драмы", "url": "https://ru.wikipedia.org/wiki/Томский_областной_театр_драмы"},
        {"title": "Trang chính thức — tomskdrama.ru", "url": "https://tomskdrama.ru/"},
    ],
    ["theatre", "drama", "culture", "tomsk", "performance", "siberia"],
    maps_text("Томский областной театр драмы", "Томск", "Tomsk Regional Drama Theatre", "Tomsk", 56.487279, 84.947094),
    official_site="https://tomskdrama.ru/",
))

# 6) Театр живых кукол «2+ку» ------------------------------------------------------
RECORDS.append(rec(
    "living-puppet-theatre-2ku-tomsk",
    "Nhà hát Rối sống '2+ku'",
    "Театр живых кукол «2+ку»",
    "'2+ku' Living Puppet Theatre",
    ["theatre"],
    56.456912, 84.941683,
    "Ngõ Yuzhny 29 (gần Lagerny sad), thành phố Tomsk, tỉnh Tomsk, Nga",
    "Nhà hát rối nhỏ đầy chất thơ do nghệ sĩ Vladimir Zakharov sáng lập, nổi tiếng với những con rối tự chế tinh xảo và không gian ấm cúng như một ngôi nhà cổ tích. Một viên ngọc văn hoá độc đáo của Tomsk.",
    "Nhà hát Rối sống '2+ku' (đọc là 'dva plyus ku') là một trong những điểm văn hoá độc đáo và được yêu mến nhất của Tomsk, do nghệ sĩ tài hoa Vladimir Zakharov (1946–2017) sáng lập. Đây không phải nhà hát lớn hào nhoáng mà là một không gian nhỏ, ấm cúng, gần như một 'ngôi nhà cổ tích' bằng gỗ, nơi những con rối do chính Zakharov chế tác 'sống dậy' trong tay các nghệ sĩ. Sân khấu thân mật khiến khán giả - cả trẻ em lẫn người lớn - cảm thấy như được kể chuyện riêng. Sau biến cố hoả hoạn và sự ra đi của người sáng lập, nhà hát được các học trò gìn giữ và tiếp tục biểu diễn tại địa chỉ mới gần khu Lagerny sad. Những buổi diễn ở đây mang màu sắc trữ tình, giàu chất triết lý và sự ấm áp thủ công - một trải nghiệm khó quên, khác hẳn các nhà hát rối thông thường.",
    [
        "Do nghệ sĩ Vladimir Zakharov sáng lập, với những con rối tự chế tinh xảo",
        "Không gian nhỏ, ấm cúng như một ngôi nhà cổ tích bằng gỗ",
        "Trải nghiệm sân khấu thân mật, giàu chất thơ, hợp cả trẻ em và người lớn",
    ],
    p("Biểu diễn theo lịch (thường cuối tuần và buổi tối); cần đặt trước.",
      "Vé phải chăng; số ghế rất ít nên nên mua sớm.",
      "Một buổi diễn khoảng 1–1,5 giờ.",
      "Quanh năm; đặc biệt ấm áp vào mùa đông.",
      "Kiểm tra lịch và đặt vé trước vì khán phòng nhỏ; đến sớm để cảm nhận không gian."),
    [
        {"title": "Wikipedia (RU) — Театр живых кукол «2+ку»", "url": "https://ru.wikipedia.org/wiki/Театр_живых_кукол_«2%2Bку»"},
        {"title": "TomskGO / Товики — Театр «2+ку»", "url": "https://towiki.ru/view/Театр_живых_кукол_«2%2Bку»"},
    ],
    ["theatre", "puppet", "culture", "tomsk", "family", "unique"],
    maps_text("Театр живых кукол 2+ку", "Томск", "2+ku Living Puppet Theatre", "Tomsk", 56.456912, 84.941683),
))

# ============================ TÔN GIÁO (church) ============================

# 7) Петропавловский собор ---------------------------------------------------------
RECORDS.append(rec(
    "peter-paul-cathedral-tomsk",
    "Nhà thờ chính toà Thánh Phêrô và Phaolô",
    "Петропавловский собор",
    "Cathedral of Saints Peter and Paul",
    ["church"],
    56.480543, 84.969941,
    "Phố Altayskaya 47, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Nhà thờ Chính thống giáo xây theo phong cách Byzantine-Nga đầu thế kỷ 20, nổi bật với gạch đỏ, mái vòm và trang trí công phu. Một trong những công trình tôn giáo đẹp và nguyên vẹn nhất của Tomsk.",
    "Nhà thờ chính toà Thánh Phêrô và Phaolô (Petropavlovsky sobor) được khởi công đầu thế kỷ 20 và là một trong những nhà thờ đẹp nhất còn nguyên vẹn của Tomsk. Công trình xây bằng gạch đỏ theo phong cách 'Nga - Byzantine', với khối kiến trúc chắc khoẻ, các mái vòm hành củ tỏi (kupola) và những chi tiết trang trí gạch tinh tế. Điều đặc biệt là nhà thờ hầu như không đóng cửa trong suốt thời Xô Viết, nhờ đó giữ được nội thất, tranh tường và nhiều biểu tượng (icon) quý giá gần như nguyên bản - điều hiếm thấy ở Nga. Không gian bên trong ấm áp, trầm mặc với ánh nến và mùi hương trầm, mang lại cảm giác linh thiêng đích thực. Nằm hơi tách khỏi trung tâm ở khu Peski, nhà thờ là điểm đến ý nghĩa cho ai muốn tìm hiểu chiều sâu tôn giáo và kiến trúc gạch cổ của thành phố.",
    [
        "Kiến trúc gạch đỏ phong cách Nga - Byzantine đầu thế kỷ 20, mái vòm công phu",
        "Gần như không đóng cửa suốt thời Xô Viết nên giữ được nội thất và icon nguyên bản",
        "Không gian trầm mặc, linh thiêng với tranh tường và biểu tượng cổ",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–19:00.",
      "Vào cửa tự do (miễn phí); có thể quyên góp tuỳ tâm.",
      "Khoảng 30–45 phút.",
      "Quanh năm; đẹp nhất vào các dịp lễ Chính thống giáo.",
      "Ăn mặc kín đáo, nữ nên trùm khăn; giữ yên lặng và xin phép trước khi chụp ảnh bên trong."),
    [
        {"title": "sobory.ru — Петропавловский собор (Томск)", "url": "https://sobory.ru/article/?object=08811"},
        {"title": "Wikipedia (RU) — Петропавловский собор (Томск)", "url": "https://ru.wikipedia.org/wiki/Петропавловский_собор_(Томск)"},
    ],
    ["church", "orthodox", "cathedral", "architecture", "tomsk", "heritage"],
    maps_text("Петропавловский собор", "Томск", "Cathedral of Saints Peter and Paul", "Tomsk", 56.480543, 84.969941),
))

# 8) Богородице-Алексиевский монастырь ---------------------------------------------
RECORDS.append(rec(
    "bogoroditse-alekseevsky-monastery-tomsk",
    "Tu viện Đức Mẹ - Thánh Alexis",
    "Богородице-Алексиевский монастырь",
    "Bogoroditse-Alekseevsky Monastery",
    ["church"],
    56.481865, 84.955065,
    "Phố Krylova 12, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Một trong những tu viện Chính thống giáo lâu đời nhất Siberia, có gốc từ thế kỷ 17. Quần thể với nhà thờ Kazan uy nghi là nơi hành hương gắn với thánh Feodor Tomsky bí ẩn.",
    "Tu viện Đức Mẹ - Thánh Alexis (Bogoroditse-Alekseevsky) là một trong những tu viện nam lâu đời nhất của Siberia, có nguồn gốc từ thế kỷ 17, gần như song hành cùng lịch sử thành phố Tomsk. Trung tâm quần thể là nhà thờ Đức Mẹ Kazan bằng đá, khối kiến trúc trắng - xanh thanh thoát với mái vòm mạ vàng. Tu viện gắn liền với một trong những huyền thoại nổi tiếng nhất nước Nga: thánh Feodor Kuzmich (Feodor Tomsky) - vị ẩn sĩ bí ẩn mà dân gian tin rằng chính là Sa hoàng Aleksandr I giả chết để đi tu; hài cốt của ông được tôn kính tại đây và thu hút nhiều người hành hương. Trong khuôn viên còn có nhà nguyện, mộ phần và không gian tĩnh lặng gợi chiều sâu tâm linh. Đây là điểm đến ý nghĩa cho ai muốn tìm hiểu lịch sử Chính thống giáo và những câu chuyện huyền bí của Tomsk.",
    [
        "Một trong những tu viện Chính thống giáo lâu đời nhất Siberia (gốc thế kỷ 17)",
        "Nhà thờ Đức Mẹ Kazan trắng - xanh với mái vòm mạ vàng thanh thoát",
        "Gắn với huyền thoại thánh ẩn sĩ Feodor Tomsky - được cho là Sa hoàng Aleksandr I",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 7:00–19:00.",
      "Vào cửa tự do (miễn phí); quyên góp tuỳ tâm.",
      "Khoảng 30–45 phút.",
      "Quanh năm; đông người hành hương vào các dịp lễ.",
      "Ăn mặc kín đáo, nữ trùm khăn; giữ trang nghiêm, hỏi trước khi chụp ảnh trong nhà thờ."),
    [
        {"title": "sobory.ru — Богородице-Алексиевский монастырь (Томск)", "url": "https://sobory.ru/article/?object=00987"},
        {"title": "Wikipedia (RU) — Богородице-Алексиевский монастырь", "url": "https://ru.wikipedia.org/wiki/Богородице-Алексиевский_монастырь"},
    ],
    ["church", "monastery", "orthodox", "pilgrimage", "tomsk", "heritage"],
    maps_text("Богородице-Алексиевский монастырь", "Томск", "Bogoroditse-Alekseevsky Monastery", "Tomsk", 56.481865, 84.955065),
))

# 9) Красная соборная мечеть ------------------------------------------------------
RECORDS.append(rec(
    "red-mosque-tomsk",
    "Thánh đường Hồi giáo Đỏ (Krasnaya mechet)",
    "Красная соборная мечеть",
    "Red Cathedral Mosque",
    ["church"],
    56.478600, 84.945541,
    "Phố Tatarskaya 24, khu Tatarskaya sloboda, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Thánh đường Hồi giáo bằng gạch đỏ cuối thế kỷ 19 giữa khu phố Tatar cổ, với ngọn tháp minaret cao vút. Biểu tượng của cộng đồng Hồi giáo Siberia và vẻ đẹp đa văn hoá của Tomsk.",
    "Thánh đường Hồi giáo Đỏ là công trình tôn giáo tiêu biểu của cộng đồng người Tatar tại Tomsk, được xây bằng gạch đỏ vào cuối thế kỷ 19 giữa khu phố lịch sử Tatarskaya sloboda (làng Tatar). Ngọn tháp minaret cao vươn lên khỏi những mái nhà gỗ thấp tạo nên một hình ảnh rất đặc trưng, phản ánh sự đa dạng tôn giáo - sắc tộc của thành phố Siberia này. Dưới thời Xô Viết, thánh đường bị đóng cửa và chuyển đổi công năng, nhưng đến cuối thế kỷ 20 đã được trả lại cho cộng đồng Hồi giáo, trùng tu và khôi phục hoạt động. Ngày nay đây là trung tâm sinh hoạt tôn giáo của người Hồi giáo Tomsk, đồng thời là một điểm nhấn kiến trúc đáng chú ý khi dạo qua khu phố Tatar cổ với những ngôi nhà gỗ chạm khắc. Công trình cho thấy Tomsk từ lâu đã là nơi giao thoa của nhiều nền văn hoá.",
    [
        "Thánh đường gạch đỏ cuối thế kỷ 19 với tháp minaret cao vút",
        "Nằm giữa khu phố Tatar cổ (Tatarskaya sloboda) nhiều nhà gỗ chạm khắc",
        "Biểu tượng của cộng đồng Hồi giáo và sự đa văn hoá của Tomsk",
    ],
    p("Mở cửa theo giờ cầu nguyện; khách tham quan nên đến ngoài giờ lễ.",
      "Vào cửa tự do (miễn phí).",
      "Khoảng 20–30 phút.",
      "Quanh năm; kết hợp dạo khu phố Tatar cổ.",
      "Ăn mặc kín đáo, cởi giày khi vào; nữ nên trùm khăn; xin phép trước khi chụp ảnh bên trong."),
    [
        {"title": "Wikipedia (RU) — Красная соборная мечеть (Томск)", "url": "https://ru.wikipedia.org/wiki/Красная_соборная_мечеть"},
        {"title": "Товики — Красная мечеть", "url": "https://towiki.ru/view/Красная_мечеть"},
    ],
    ["church", "mosque", "islam", "tatar", "tomsk", "architecture"],
    maps_text("Красная соборная мечеть", "Томск", "Red Cathedral Mosque", "Tomsk", 56.478600, 84.945541),
))

# 10) Католический костёл Покрова Пресвятой Богородицы -----------------------------
RECORDS.append(rec(
    "tomsk-catholic-church",
    "Nhà thờ Công giáo Ba Lan (Costel)",
    "Католический костёл Покрова Пресвятой Богородицы",
    "Catholic Church of the Intercession",
    ["church"],
    56.489743, 84.952608,
    "Phố Bakunina 4, trên đồi Voskresenskaya, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Nhà thờ Công giáo (kostel) xây giữa thế kỷ 19, kiến trúc Gothic thanh thoát trên đồi Voskresenskaya. Di sản của cộng đồng người Ba Lan bị lưu đày đến Siberia, nay là nhà thờ Công giáo chính của thành phố.",
    "Nhà thờ Công giáo Đức Mẹ Vô Nhiễm (thường gọi là 'kostel' theo tiếng Ba Lan) được xây giữa thế kỷ 19 trên đồi Voskresenskaya, là một trong những nhà thờ Công giáo lâu đời nhất Siberia. Công trình mang phong cách Gothic thanh thoát với tháp nhọn, cửa sổ hình vòm nhọn và khối kiến trúc trắng thanh nhã, nổi bật giữa những mái nhà gỗ xung quanh. Nhà thờ ra đời từ nhu cầu của cộng đồng đông đảo người Ba Lan bị đày sang Siberia sau các cuộc khởi nghĩa, cùng với người Litva, Đức và các dân tộc Công giáo khác - một minh chứng cảm động cho lịch sử lưu đày của vùng đất này. Sau thời Xô Viết, nhà thờ được trả lại cho giáo hội và phục hồi hoạt động. Ngày nay đây vừa là nơi hành lễ, vừa thi thoảng tổ chức các buổi hoà nhạc organ, và là điểm nhấn kiến trúc đẹp trong cụm di tích trên đồi Voskresenskaya.",
    [
        "Kiến trúc Gothic thanh thoát với tháp nhọn, giữa cụm di tích đồi Voskresenskaya",
        "Di sản của cộng đồng người Ba Lan và các dân tộc Công giáo bị lưu đày đến Siberia",
        "Thi thoảng có các buổi hoà nhạc organ trong không gian nhà thờ",
    ],
    p("Mở cửa theo giờ lễ; nên đến ngoài giờ hành lễ để tham quan.",
      "Vào cửa tự do (miễn phí); hoà nhạc có thể bán vé riêng.",
      "Khoảng 20–30 phút.",
      "Quanh năm; kết hợp tham quan cả đồi Voskresenskaya.",
      "Giữ trang nghiêm; hỏi lịch hoà nhạc organ nếu muốn thưởng thức âm nhạc."),
    [
        {"title": "Wikipedia (RU) — Костёл Покрова Пресвятой Девы Марии (Томск)", "url": "https://ru.wikipedia.org/wiki/Костёл_Покрова_Пресвятой_Девы_Марии_(Томск)"},
        {"title": "Товики — Католический костёл", "url": "https://towiki.ru/view/Католический_костёл"},
    ],
    ["church", "catholic", "gothic", "polish", "tomsk", "heritage"],
    maps_text("Католический костёл Покрова", "Томск", "Catholic Church of the Intercession", "Tomsk", 56.489743, 84.952608),
))

# ============================ PHÁO ĐÀI / DI TÍCH (fortress) ============================

# 11) Воскресенская гора / камень основания Томска ---------------------------------
RECORDS.append(rec(
    "voskresenskaya-hill-tomsk",
    "Đồi Voskresenskaya và Đá lập thành Tomsk",
    "Воскресенская гора и камень основания Томска",
    "Voskresenskaya Hill and Tomsk Founding Stone",
    ["fortress", "monument"],
    56.488614, 84.952841,
    "Đồi Voskresenskaya (khu phố cổ), thành phố Tomsk, tỉnh Tomsk, Nga",
    "Ngọn đồi lịch sử nơi pháo đài gỗ đầu tiên khai sinh thành phố Tomsk năm 1604, nay có tảng đá kỷ niệm lập thành và mô hình tái hiện tường thành gỗ. Điểm ngắm toàn cảnh và cái nôi của cả thành phố.",
    "Đồi Voskresenskaya (Voskresenskaya gora - 'đồi Phục Sinh') là cái nôi khai sinh của Tomsk: chính tại đây, năm 1604, những người Cossack đã dựng lên pháo đài gỗ (Tomsky ostrog) theo sắc lệnh của Sa hoàng, mở đầu cho lịch sử thành phố. Ngày nay trên đồi đặt một tảng đá kỷ niệm lớn khắc dòng chữ ghi dấu nơi thành phố được thành lập, cùng một đoạn tường thành và tháp gỗ tái hiện để du khách hình dung diện mạo pháo đài xưa. Từ đỉnh đồi có thể phóng tầm mắt bao quát khu phố cổ với những nhà gỗ, mái vòm nhà thờ và dòng sông Tom phía xa. Cả khu vực là một quần thể di tích cô đọng: cạnh đó là Bảo tàng Lịch sử Thành phố với tháp cứu hoả, nhà thờ Công giáo Ba Lan và nhà thờ Voskresenskaya. Đây là điểm không thể bỏ qua để bắt đầu hiểu về nguồn cội của Tomsk.",
    [
        "Nơi pháo đài gỗ đầu tiên khai sinh thành phố Tomsk năm 1604",
        "Tảng đá kỷ niệm lập thành và đoạn tường - tháp gỗ tái hiện pháo đài xưa",
        "Điểm ngắm toàn cảnh khu phố cổ và sông Tom, giữa cụm di tích trên đồi",
    ],
    p("Không gian ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 30–45 phút (kể cả ghé bảo tàng và nhà thờ lân cận).",
      "Mùa hè và đầu thu để ngắm cảnh; mùa đông tuyết phủ cũng nên thơ.",
      "Kết hợp tham quan cả Bảo tàng Lịch sử, tháp cứu hoả và nhà thờ Công giáo ngay cạnh."),
    [
        {"title": "Wikipedia (RU) — Воскресенская гора (Томск)", "url": "https://ru.wikipedia.org/wiki/Воскресенская_гора_(Томск)"},
        {"title": "Товики — Камень основания Томска", "url": "https://towiki.ru/view/Камень_на_месте_основания_Томска"},
    ],
    ["fortress", "monument", "history", "viewpoint", "tomsk", "old-town"],
    maps_text("Воскресенская гора камень основания Томска", "Томск", "Voskresenskaya Hill Tomsk Founding Stone", "Tomsk", 56.488614, 84.952841),
))

# 12) Семилуженский острог ---------------------------------------------------------
RECORDS.append(rec(
    "semiluzhki-fort-tomsk",
    "Pháo đài gỗ Semiluzhki (Semiluzhensky ostrog)",
    "Семилуженский острог",
    "Semiluzhensky Ostrog (Wooden Fort)",
    ["fortress"],
    56.617541, 85.353229,
    "Làng Semiluzhki, đường Irkutsky trakt, huyện Tomsk, tỉnh Tomsk, Nga",
    "Pháo đài gỗ Cossack được một người dân đam mê lịch sử phục dựng thủ công tại làng Semiluzhki. Bảo tàng sống ngoài trời tái hiện đời sống Siberia thế kỷ 17 với tường thành, tháp canh và các hoạt động trải nghiệm.",
    "Pháo đài gỗ Semiluzhki (Semiluzhensky ostrog) là một dự án tâm huyết độc đáo: nhà phục dựng Vladimir Ilyin đã tự tay dựng lại một pháo đài Cossack thế kỷ 17 tại làng Semiluzhki, cách Tomsk khoảng 40 km trên tuyến đường Irkutsk cổ. Quần thể gồm tường thành gỗ, tháp canh, nhà nguyện và các công trình mô phỏng đời sống người khai hoang Siberia. Đây là một 'bảo tàng sống' ngoài trời, nơi du khách không chỉ tham quan mà còn được thử bắn cung, ném rìu, mặc giáp Cossack, nếm ẩm thực dân dã và nghe những câu chuyện lịch sử sinh động do chính người sáng lập kể. Không khí mộc mạc, chân thật và giàu tính giáo dục khiến nơi đây đặc biệt hấp dẫn với gia đình có trẻ em và những ai yêu thích lịch sử Siberia. Chuyến đi thường kết hợp trong một tour ngày từ Tomsk.",
    [
        "Pháo đài gỗ Cossack thế kỷ 17 được phục dựng thủ công công phu",
        "Bảo tàng sống ngoài trời: bắn cung, ném rìu, mặc giáp, nếm ẩm thực dân dã",
        "Trải nghiệm lịch sử Siberia sinh động, hợp gia đình có trẻ em",
    ],
    p("Mở cửa theo hẹn/theo tour; nên liên hệ hoặc đi cùng đoàn để có người thuyết minh.",
      "Có phí tham quan và trải nghiệm ở mức phải chăng.",
      "Khoảng 1,5–2 giờ tại chỗ (chưa kể di chuyển).",
      "Mùa hè và đầu thu; các lễ hội dân gian rất sôi động.",
      "Cách Tomsk ~40 km - nên đi ô tô hoặc tour; đặt lịch trước để chắc chắn mở cửa."),
    [
        {"title": "Wikipedia (RU) — Семилужки", "url": "https://ru.wikipedia.org/wiki/Семилужки"},
        {"title": "Товики — Семилуженский острог", "url": "https://towiki.ru/view/Семилуженский_острог"},
    ],
    ["fortress", "history", "cossack", "open-air", "tomsk-region", "family"],
    maps_text("Семилуженский острог", "Семилужки", "Semiluzhensky Ostrog", "Semiluzhki", 56.617541, 85.353229),
))

# ============================ QUẢNG TRƯỜNG / PHỐ (square_street) ============================

# 13) Проспект Ленина --------------------------------------------------------------
RECORDS.append(rec(
    "lenin-avenue-tomsk",
    "Đại lộ Lenina (Prospekt Lenina)",
    "Проспект Ленина",
    "Lenin Avenue",
    ["square_street"],
    56.477900, 84.951500,
    "Đại lộ Lenina - trục trung tâm chạy dọc thành phố Tomsk, tỉnh Tomsk, Nga",
    "Trục đại lộ chính và lâu đời nhất của Tomsk, nơi tập trung phần lớn công trình lịch sử: trường đại học, nhà thờ, dinh thự thương gia, quảng trường và tượng đài. Con phố dạo bộ để cảm nhận trọn vẹn tinh thần thành phố.",
    "Đại lộ Lenina là 'xương sống' của Tomsk - trục phố chính chạy dọc thành phố, kế thừa con đường thương mại cổ và ngày nay quy tụ phần lớn di sản kiến trúc quan trọng. Dạo bộ dọc đại lộ, du khách lần lượt đi qua khuôn viên Đại học Quốc gia Tomsk với rừng cây cổ, các dinh thự thương gia thế kỷ 19, Quảng trường Novosobornaya, Quảng trường Lenina bên sông Tom, nhà thờ, bảo tàng và vô số quán cà phê, hiệu sách. Kiến trúc hai bên phố pha trộn phong cách cổ điển, tân nghệ thuật (Art Nouveau) và cả những mảng nhà gỗ chạm khắc đặc trưng. Đây là nơi nhịp sống sinh viên trẻ trung hoà cùng vẻ trầm mặc của một thành phố hơn 400 năm tuổi. Chỉ cần thong dong đi hết đại lộ là đã nắm được phần lớn tinh thần và câu chuyện của Tomsk - vì vậy đây thường là tuyến tham quan bộ đầu tiên mà du khách nên chọn.",
    [
        "Trục phố chính quy tụ đại học, nhà thờ, dinh thự và các quảng trường lịch sử",
        "Kiến trúc pha trộn cổ điển, Art Nouveau và nhà gỗ chạm khắc",
        "Tuyến đi bộ lý tưởng để cảm nhận trọn vẹn tinh thần thành phố đại học Tomsk",
    ],
    p("Không gian đô thị công cộng, dạo bộ tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 1,5–3 giờ nếu thong dong dạo bộ và ghé các điểm dọc đường.",
      "Mùa hè và đầu thu ban ngày; buổi tối lên đèn cũng đẹp.",
      "Đi giày thoải mái; kết hợp ghé đại học, bảo tàng và các quảng trường dọc đại lộ."),
    [
        {"title": "Wikipedia (RU) — Проспект Ленина (Томск)", "url": "https://ru.wikipedia.org/wiki/Проспект_Ленина_(Томск)"},
        {"title": "Товики — Проспект Ленина", "url": "https://towiki.ru/view/Проспект_Ленина_(Томск)"},
    ],
    ["square_street", "avenue", "walking", "architecture", "tomsk", "city-center"],
    maps_text("Проспект Ленина", "Томск", "Lenin Avenue", "Tomsk", 56.477900, 84.951500),
))

# 14) Набережная реки Томи ---------------------------------------------------------
RECORDS.append(rec(
    "tom-river-embankment-tomsk",
    "Bờ kè sông Tom (Naberezhnaya Tomi)",
    "Набережная реки Томи",
    "Tom River Embankment",
    ["square_street"],
    56.485556, 84.944722,
    "Bờ phải sông Tom, gần cửa sông Ushayka, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Bờ kè dạo bộ ven sông Tom ở trung tâm thành phố, nơi có tượng đài Anton Chekhov nổi tiếng và tầm nhìn thoáng rộng ra dòng sông. Không gian thư giãn được người dân và du khách yêu thích.",
    "Bờ kè sông Tom là một trong những không gian công cộng dễ chịu nhất của Tomsk, trải dọc bờ phải con sông ngay khu trung tâm, gần nơi sông Ushayka nhỏ đổ vào sông Tom. Đây là chốn dạo bộ, hóng gió và ngắm hoàng hôn quen thuộc của người dân, với lối đi lát đá, ghế nghỉ và tầm nhìn thoáng ra mặt sông rộng cùng bờ bên kia. Điểm nhấn nổi tiếng nhất là tượng đài Anton Chekhov đầy hài hước - khắc hoạ nhà văn theo góc nhìn châm biếm 'qua con mắt của một gã say nằm dưới mương', ra đời để đáp lại lời chê bai Tomsk mà Chekhov từng viết. Vào mùa hè, khu bờ kè trở nên sôi động với các sự kiện, quán cà phê và hoạt động ngoài trời. Từ đây du khách dễ dàng kết nối lên Quảng trường Lenina, đại lộ Lenina và khu phố cổ, khiến bờ kè trở thành điểm dừng chân thư giãn lý tưởng giữa hành trình khám phá thành phố.",
    [
        "Lối dạo bộ ven sông Tom thoáng đãng ngay trung tâm thành phố",
        "Nơi đặt tượng đài Anton Chekhov hài hước nổi tiếng của Tomsk",
        "Không gian ngắm hoàng hôn và các sự kiện ngoài trời mùa hè",
    ],
    p("Không gian ngoài trời, dạo bộ tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 30–60 phút.",
      "Mùa hè và đầu thu, đẹp nhất lúc hoàng hôn.",
      "Kết hợp ngắm tượng Chekhov, lên Quảng trường Lenina và đại lộ Lenina gần đó."),
    [
        {"title": "Wikipedia (RU) — Томь (приток Оби)", "url": "https://ru.wikipedia.org/wiki/Томь_(приток_Оби)"},
        {"title": "Товики — Набережная реки Томи", "url": "https://towiki.ru/view/Набережная_реки_Томи"},
    ],
    ["square_street", "embankment", "river", "walking", "tomsk", "cityscape"],
    maps_text("Набережная реки Томи", "Томск", "Tom River Embankment", "Tomsk", 56.485556, 84.944722),
))

# 15) Нарым (село) + Нарымский музей политической ссылки ---------------------------
RECORDS.append(rec(
    "narym-tomsk",
    "Làng Narym và Bảo tàng Lưu đày Chính trị",
    "Нарым и Нарымский музей политической ссылки",
    "Narym Village and Museum of Political Exile",
    ["museum", "square_street"],
    58.925913, 81.598748,
    "Làng Narym, huyện Parabel, bắc tỉnh Tomsk, Nga (bên sông Ob)",
    "Ngôi làng cổ hẻo lánh bên sông Ob, một trong những nơi lưu đày khắc nghiệt nhất của nước Nga Sa hoàng và Xô Viết. Nay có bảo tàng lưu đày chính trị kể lại số phận của những người bị đày biệt xứ đến Siberia.",
    "Narym là một trong những địa danh mang sức nặng lịch sử đặc biệt của tỉnh Tomsk: một ngôi làng cổ nằm sâu ở phương bắc, bên bờ sông Ob, được lập từ thế kỷ 16 và từ sớm đã trở thành nơi lưu đày. Câu nói chua chát 'Chúa ở xa, Sa hoàng ở cao, còn Narym thì cách xa tất cả' phần nào diễn tả sự heo hút, khắc nghiệt của vùng đất này. Suốt thời Đế quốc rồi thời Xô Viết, hàng vạn người - từ các nhà cách mạng (trong đó có cả những nhân vật nổi tiếng), tù chính trị, cho đến những gia đình bị đày biệt xứ - đã bị đưa đến đây trong điều kiện lạnh giá, muỗi mòng và cô lập. Bảo tàng Lưu đày Chính trị Narym gìn giữ ký ức bi thương ấy qua hiện vật, hình ảnh, thư từ và tư liệu về đời sống của những người lưu đày. Đến Narym là một hành trình xa và trầm lắng, dành cho những ai muốn hiểu chiều sâu lịch sử đau thương của Siberia.",
    [
        "Ngôi làng lưu đày cổ bên sông Ob, biểu tượng cho sự khắc nghiệt của Siberia",
        "Bảo tàng Lưu đày Chính trị lưu giữ hiện vật và tư liệu về số phận người bị đày",
        "Điểm đến lịch sử trầm lắng, gắn với ký ức lưu đày thời Sa hoàng và Xô Viết",
    ],
    p("Bảo tàng mở cửa theo giờ hành chính (nên liên hệ trước vì ở xa); làng tham quan tự do.",
      "Vé bảo tàng rẻ; chi phí chính là di chuyển.",
      "Nửa ngày tại chỗ (chưa kể quãng đường dài từ Tomsk).",
      "Mùa hè (đường và sông thuận lợi); mùa đông rất lạnh và khó đi.",
      "Cách Tomsk hàng trăm km về phía bắc - cần lên kế hoạch kỹ; nên đi theo tour hoặc tìm hiểu lịch trình trước."),
    [
        {"title": "Wikipedia (RU) — Нарым", "url": "https://ru.wikipedia.org/wiki/Нарым"},
        {"title": "Culture.ru — Нарымский музей политической ссылки", "url": "https://www.culture.ru/institutes/12730/narymskii-muzei-politicheskoi-ssylki"},
    ],
    ["museum", "history", "exile", "ob-river", "tomsk-region", "memorial"],
    maps_text("Нарым", "Томская область", "Narym village", "Tomsk Oblast", 58.925913, 81.598748),
))

# ============================ TƯỢNG ĐÀI (monument) ============================

# 16) Памятник рублю ---------------------------------------------------------------
RECORDS.append(rec(
    "ruble-monument-tomsk",
    "Tượng đài Đồng Rúp",
    "Памятник рублю",
    "Monument to the Ruble",
    ["monument"],
    56.474172, 84.950875,
    "Quảng trường Novosobornaya, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Tượng đài bằng gỗ hình đồng rúp - đơn vị tiền tệ Nga - do sinh viên Tomsk dựng nên một cách vui nhộn. Một điểm chụp ảnh 'cầu may tài lộc' độc đáo và mang tính bản địa của thành phố.",
    "Tượng đài Đồng Rúp là một trong những tượng đài kỳ khôi và dễ thương của Tomsk - thành phố nổi tiếng với óc hài hước của giới sinh viên. Tác phẩm khắc hoạ hình đồng rúp (đơn vị tiền tệ của Nga) được làm chủ yếu bằng gỗ - vật liệu biểu tượng của 'thủ đô kiến trúc gỗ' - đặt ở khu vực trung tâm gần Quảng trường Novosobornaya. Ý tưởng nửa nghiêm túc nửa đùa vui này vừa tôn vinh đồng tiền quốc gia, vừa trở thành nơi người dân và du khách đến chạm tay 'cầu may tài lộc', chụp ảnh kỷ niệm. Cùng với hàng loạt tượng nhỏ dí dỏm khác rải rác khắp thành phố (chú chó hạnh phúc, người thợ, đôi tình nhân...), Tượng đài Đồng Rúp góp phần tạo nên bầu không khí trẻ trung, vui tươi rất riêng của Tomsk. Đây là điểm dừng chân nhẹ nhàng, thú vị khi dạo bộ khu trung tâm.",
    [
        "Tượng đài hình đồng rúp làm bằng gỗ - vật liệu biểu tượng của Tomsk",
        "Điểm chạm tay 'cầu may tài lộc' và chụp ảnh vui của du khách",
        "Một trong nhiều tượng nhỏ dí dỏm làm nên tinh thần hài hước của thành phố",
    ],
    p("Không gian ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Quanh năm; đẹp nhất khi kết hợp dạo Quảng trường Novosobornaya.",
      "Kết hợp 'săn' các tượng nhỏ dí dỏm khác của Tomsk trong cùng khu trung tâm."),
    [
        {"title": "Товики — Памятник рублю", "url": "https://towiki.ru/view/Памятник_рублю"},
        {"title": "Openarium — Памятник рублю (Томск)", "url": "https://openarium.ru/russia/tomsk/dostoprimechatelnosti/"},
    ],
    ["monument", "wooden", "quirky", "photo-spot", "tomsk", "city-center"],
    maps_text("Памятник рублю", "Томск", "Monument to the Ruble", "Tomsk", 56.474172, 84.950875),
))

# 17) Памятник счастью «Щас спою» (волк) -------------------------------------------
RECORDS.append(rec(
    "happiness-monument-wolf-tomsk",
    "Tượng đài Hạnh phúc (chú Sói 'Để tôi hát')",
    "Памятник счастью («Щас спою!»)",
    "Monument to Happiness (the Wolf)",
    ["monument"],
    56.477329, 84.991911,
    "Phố Shevchenko 19/1, gần Cung Thể thao, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Tượng đồng chú Sói no nê từ phim hoạt hình Xô Viết 'Ngày xửa ngày xưa có một chú chó', tay xoa bụng thốt lên 'Để tôi hát...'. Biểu tượng dễ thương của sự mãn nguyện, gắn với ký ức tuổi thơ nhiều thế hệ.",
    "Tượng đài Hạnh phúc là một trong những tượng nhỏ được yêu thích nhất Tomsk, khắc hoạ chú Sói bụng no tròn từ bộ phim hoạt hình Xô Viết kinh điển 'Ngày xửa ngày xưa có một chú chó' (Zhil-byl pyos). Trong phim, sau bữa tiệc no nê, chú Sói mãn nguyện xoa bụng và thốt lên câu thoại đã đi vào huyền thoại: 'Shchas spoyu!' ('Để tôi hát một bài...'). Bức tượng đồng tái hiện đúng khoảnh khắc ấy - gương mặt lim dim hạnh phúc, tay đặt lên chiếc bụng tròn - trở thành biểu tượng vui nhộn của sự no đủ, mãn nguyện và bình yên. Với người Nga, hình ảnh này khơi gợi cả một trời ký ức tuổi thơ. Du khách thường chạm tay vào bụng chú Sói để 'cầu' sung túc, hạnh phúc và chụp ảnh kỷ niệm. Đặt gần Cung Thể thao, đây là điểm dừng chân dễ thương, mang đậm chất văn hoá đại chúng Nga - Xô.",
    [
        "Chú Sói no nê từ phim hoạt hình 'Ngày xửa ngày xưa có một chú chó' với câu thoại 'Để tôi hát'",
        "Biểu tượng dí dỏm của sự mãn nguyện, no đủ và hạnh phúc",
        "Điểm chạm tay 'cầu sung túc' và chụp ảnh gắn với ký ức tuổi thơ Xô Viết",
    ],
    p("Không gian ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Quanh năm.",
      "Chạm tay vào bụng chú Sói để 'cầu may'; kết hợp các tượng dí dỏm khác của Tomsk."),
    [
        {"title": "Wikipedia (RU) — Памятник счастью (Томск)", "url": "https://ru.wikipedia.org/wiki/Памятник_счастью_(Томск)"},
        {"title": "Товики — Памятник счастью", "url": "https://towiki.ru/view/Памятник_счастью"},
    ],
    ["monument", "cartoon", "quirky", "photo-spot", "tomsk", "soviet-culture"],
    maps_text("Памятник счастью Щас спою", "Томск", "Monument to Happiness Wolf", "Tomsk", 56.477329, 84.991911),
))

# 18) Дом с драконами --------------------------------------------------------------
RECORDS.append(rec(
    "house-with-dragons-tomsk",
    "Ngôi nhà Rồng (Dom s drakonami)",
    "Дом с драконами",
    "House with Dragons",
    ["monument"],
    56.472272, 84.966002,
    "Phố Krasnoarmeyskaya 68, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Ngôi nhà gỗ độc đáo đầu thế kỷ 20 với những đầu rồng chạm khắc vươn ra từ mái, một trong những biểu tượng kiến trúc gỗ nổi tiếng nhất Tomsk. Kiệt tác của phong cách 'tân nghệ thuật gỗ' Siberia.",
    "Ngôi nhà Rồng là một trong những công trình gỗ được chụp ảnh nhiều nhất và mang tính biểu tượng bậc nhất của Tomsk. Được dựng đầu thế kỷ 20 trên phố Krasnoarmeyskaya - con phố mệnh danh là 'bảo tàng kiến trúc gỗ lộ thiên' của thành phố - ngôi nhà gây ấn tượng mạnh bởi bảy đầu rồng chạm khắc bằng gỗ vươn ra từ mái và đỉnh đầu hồi, tạo dáng vẻ vừa cổ tích vừa huyền bí. Đây là ví dụ tiêu biểu của phong cách kết hợp giữa hoa văn dân gian Nga, đường nét tân nghệ thuật (Art Nouveau) và trí tưởng tượng phóng khoáng của những người thợ mộc Siberia. Cùng với 'Ngôi nhà Chim Lửa' gần đó, Ngôi nhà Rồng là điểm nhấn không thể bỏ qua khi dạo bộ khám phá di sản gỗ của Tomsk. Ngôi nhà hiện được sử dụng làm cơ sở giáo dục, nhưng vẻ đẹp mặt tiền vẫn là 'thỏi nam châm' hút du khách dừng chân chiêm ngưỡng và chụp ảnh.",
    [
        "Bảy đầu rồng chạm gỗ vươn ra từ mái - hình ảnh cổ tích, huyền bí độc đáo",
        "Nằm trên phố Krasnoarmeyskaya - 'bảo tàng kiến trúc gỗ lộ thiên' của Tomsk",
        "Kiệt tác kết hợp hoa văn dân gian Nga và phong cách tân nghệ thuật gỗ Siberia",
    ],
    p("Không gian ngoài trời, ngắm mặt tiền tự do mọi lúc (bên trong là cơ sở giáo dục, không tham quan).",
      "Miễn phí (chỉ ngắm và chụp ảnh từ bên ngoài).",
      "Khoảng 10–15 phút.",
      "Ban ngày trời nắng để thấy rõ hoa văn chạm khắc; mùa đông tuyết phủ cũng đẹp.",
      "Kết hợp dạo cả phố Krasnoarmeyskaya để ngắm 'Ngôi nhà Chim Lửa' và các nhà gỗ khác."),
    [
        {"title": "Wikipedia (RU) — Дом с драконами (Томск)", "url": "https://ru.wikipedia.org/wiki/Дом_с_драконами_(Томск)"},
        {"title": "Товики — Дом с драконами", "url": "https://towiki.ru/view/Дом_с_драконами"},
    ],
    ["monument", "wooden-architecture", "art-nouveau", "photo-spot", "tomsk", "heritage"],
    maps_text("Дом с драконами", "Томск", "House with Dragons", "Tomsk", 56.472272, 84.966002),
))

# ============================ CÔNG VIÊN / VƯỜN (park_garden) ============================

# 19) Университетская роща ТГУ -----------------------------------------------------
RECORDS.append(rec(
    "university-grove-tomsk",
    "Rừng cây Đại học (Universitetskaya roshcha)",
    "Университетская роща ТГУ",
    "Tomsk University Grove",
    ["park_garden"],
    56.469577, 84.948510,
    "Đại lộ Lenina 36, khuôn viên Đại học Quốc gia Tomsk, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Khu rừng cây cổ thụ được vun trồng từ cuối thế kỷ 19 trong khuôn viên Đại học Quốc gia Tomsk. Một 'lá phổi xanh' lịch sử với những hàng cây tuyết tùng, sồi và các tượng đài học thuật.",
    "Rừng cây Đại học là một trong những không gian xanh đẹp và giàu ý nghĩa nhất Tomsk, được quy hoạch và vun trồng ngay từ khi Đại học Hoàng gia Tomsk - trường đại học đầu tiên của Siberia - ra đời vào cuối thế kỷ 19. Những người sáng lập đã cho trồng hàng nghìn cây, nhiều loài được mang từ vườn ươm và các vùng khác về, biến khu đất trước toà nhà đại học cổ kính thành một công viên - vườn thực vật thu nhỏ. Ngày nay, dưới tán những cây tuyết tùng, thông, sồi và bạch dương cả trăm tuổi là các lối đi rợp bóng, tượng đài các nhà khoa học và không khí học thuật trầm lắng. Đây vừa là nơi sinh viên dạo bộ, ôn bài, vừa là điểm tham quan gắn liền với lịch sử giáo dục Siberia. Vào mùa thu, sắc lá vàng rực khiến khu rừng trở nên thơ mộng đặc biệt, còn mùa đông tuyết phủ lại mang vẻ đẹp tĩnh lặng cổ điển.",
    [
        "Rừng cây cổ thụ trồng từ cuối thế kỷ 19 cùng thời Đại học đầu tiên của Siberia",
        "Tuyết tùng, thông, sồi trăm tuổi cùng các tượng đài nhà khoa học",
        "Không gian xanh học thuật thơ mộng, đặc biệt đẹp vào mùa thu lá vàng",
    ],
    p("Không gian ngoài trời, dạo bộ tự do ban ngày.",
      "Miễn phí.",
      "Khoảng 30–45 phút.",
      "Mùa thu (lá vàng) và mùa hè; mùa đông tuyết phủ cũng rất đẹp.",
      "Kết hợp tham quan toà nhà chính Đại học Quốc gia Tomsk và bảo tàng trong trường."),
    [
        {"title": "Wikipedia (RU) — Университетская роща (Томск)", "url": "https://ru.wikipedia.org/wiki/Университетская_роща"},
        {"title": "Товики — Университетская роща", "url": "https://towiki.ru/view/Университетская_роща"},
    ],
    ["park_garden", "grove", "university", "nature", "tomsk", "walking"],
    maps_text("Университетская роща ТГУ", "Томск", "Tomsk University Grove", "Tomsk", 56.469577, 84.948510),
))

# 20) Сибирский ботанический сад ТГУ -----------------------------------------------
RECORDS.append(rec(
    "siberian-botanical-garden-tomsk",
    "Vườn Bách thảo Siberia (ĐH Tomsk)",
    "Сибирский ботанический сад ТГУ",
    "Siberian Botanical Garden",
    ["park_garden"],
    56.466505, 84.946180,
    "Đại lộ Lenina 34/1, Đại học Quốc gia Tomsk, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Vườn bách thảo lâu đời của Đại học Tomsk, nổi tiếng với những nhà kính nhiệt đới cao vút trồng cọ, chuối và hàng nghìn loài thực vật từ khắp thế giới. Một ốc đảo xanh giữa mùa đông Siberia khắc nghiệt.",
    "Vườn Bách thảo Siberia thuộc Đại học Quốc gia Tomsk là một trong những vườn bách thảo lâu đời và lớn nhất vùng Siberia, được thành lập từ cuối thế kỷ 19 cùng thời với trường đại học. Điểm đặc biệt nhất là những nhà kính (oranzhereya) cao vút - có nhà kính thuộc loại cao nhất nước Nga - nơi cây cọ, chuối, dứa và hàng nghìn loài thực vật nhiệt đới, cận nhiệt đới vẫn xanh tươi bất chấp cái lạnh -30°C ngoài trời. Bước vào đây giữa mùa đông tuyết trắng, du khách như lạc sang một thế giới nhiệt đới ẩm ướt đầy hương hoa. Vườn còn có các bộ sưu tập ngoài trời về hệ thực vật Siberia, cây thuốc và cây quý hiếm, phục vụ cả nghiên cứu khoa học lẫn tham quan. Đây là điểm đến lý tưởng cho gia đình, người yêu thiên nhiên và bất kỳ ai muốn 'sưởi ấm' tâm hồn bằng màu xanh giữa mùa đông Siberia.",
    [
        "Nhà kính nhiệt đới thuộc loại cao nhất nước Nga, trồng cọ, chuối, dứa",
        "Ốc đảo xanh nhiệt đới giữa mùa đông Siberia -30°C",
        "Bộ sưu tập hàng nghìn loài thực vật phục vụ cả nghiên cứu và tham quan",
    ],
    p("Tham quan nhà kính theo tour có hướng dẫn, thường giờ hành chính; nên đặt trước.",
      "Có vé vào cửa ở mức phải chăng; tour nhà kính có thể tính phí riêng.",
      "Khoảng 1–1,5 giờ.",
      "Tuyệt vời nhất vào mùa đông - tương phản với tuyết lạnh bên ngoài.",
      "Liên hệ đặt lịch trước vì vào nhà kính thường theo nhóm có hướng dẫn viên."),
    [
        {"title": "Wikipedia (RU) — Сибирский ботанический сад", "url": "https://ru.wikipedia.org/wiki/Сибирский_ботанический_сад"},
        {"title": "Trang chính thức — sbg.tsu.ru", "url": "http://sbg.tsu.ru/"},
    ],
    ["park_garden", "botanical-garden", "greenhouse", "nature", "tomsk", "family"],
    maps_text("Сибирский ботанический сад ТГУ", "Томск", "Siberian Botanical Garden", "Tomsk", 56.466505, 84.946180),
    official_site="http://sbg.tsu.ru/",
))

# 21) Лагерный сад -----------------------------------------------------------------
RECORDS.append(rec(
    "lagerny-sad-tomsk",
    "Công viên Lagerny sad và Đài tưởng niệm",
    "Лагерный сад",
    "Lagerny Sad Park",
    ["park_garden", "monument"],
    56.453518, 84.948376,
    "Phố Nakhimova, bên bờ dốc cao sông Tom, thành phố Tomsk, tỉnh Tomsk, Nga",
    "Công viên trên bờ dốc cao nhìn ra sông Tom, nơi đặt Đài tưởng niệm Chiến công và Lao động của người Tomsk với ngọn lửa vĩnh cửu. Không gian tưởng niệm trang nghiêm kết hợp cảnh quan thiên nhiên tuyệt đẹp.",
    "Lagerny sad ('vườn doanh trại' - tên gọi có từ thời từng là nơi đóng quân) là một trong những công viên tiêu biểu và giàu ý nghĩa nhất Tomsk, trải trên bờ dốc cao phía nam thành phố nhìn xuống dòng sông Tom rộng lớn. Đây vừa là không gian dạo bộ thiên nhiên với rừng cây, đường dạo và tầm nhìn thoáng đãng, vừa là địa điểm tưởng niệm quan trọng: trung tâm công viên là Đài tưởng niệm Chiến công và Lao động của người Tomsk trong Chiến tranh Vệ quốc Vĩ đại, với tượng đài 'Mẫu quốc - Mẹ Tổ quốc' tiễn con ra trận và đón về, cùng ngọn lửa vĩnh cửu tưởng nhớ những người đã ngã xuống. Vào các dịp lễ, đặc biệt là Ngày Chiến thắng 9/5, nơi đây trở thành điểm hội tụ trang nghiêm của cả thành phố. Bờ dốc Lagerny sad còn là địa điểm địa chất thú vị và là chỗ ngắm hoàng hôn trên sông Tom được yêu thích.",
    [
        "Đài tưởng niệm Chiến công và Lao động với tượng 'Mẹ Tổ quốc' và ngọn lửa vĩnh cửu",
        "Công viên trên bờ dốc cao ngắm toàn cảnh sông Tom",
        "Điểm hội tụ trang nghiêm của thành phố vào Ngày Chiến thắng 9/5",
    ],
    p("Không gian ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 45–60 phút.",
      "Mùa hè và đầu thu; đẹp lúc hoàng hôn bên sông Tom.",
      "Giữ trang nghiêm ở khu đài tưởng niệm; đi giày thoải mái để dạo bờ dốc."),
    [
        {"title": "Wikipedia (RU) — Лагерный сад", "url": "https://ru.wikipedia.org/wiki/Лагерный_сад"},
        {"title": "Товики — Лагерный сад", "url": "https://towiki.ru/view/Лагерный_сад"},
    ],
    ["park_garden", "monument", "memorial", "river-view", "tomsk", "wwii"],
    maps_text("Лагерный сад", "Томск", "Lagerny Sad Park", "Tomsk", 56.453518, 84.948376),
))

# 22) Городской сад (Горсад) -------------------------------------------------------
RECORDS.append(rec(
    "gorodskoy-sad-tomsk",
    "Vườn Thành phố (Gorodskoy sad)",
    "Городской сад",
    "City Garden (Gorsad)",
    ["park_garden"],
    56.472466, 84.954782,
    "Phố Gertsena 6, gần trung tâm thành phố Tomsk, tỉnh Tomsk, Nga",
    "Công viên giải trí lâu đời ngay trung tâm Tomsk, với vòng đu quay, các trò chơi, sân khấu ngoài trời và không gian dạo bộ xanh mát. Chốn vui chơi quen thuộc của các gia đình và giới trẻ.",
    "Vườn Thành phố (thường gọi thân mật là 'Gorsad') là công viên văn hoá - giải trí lâu đời và được người dân Tomsk yêu mến, nằm ngay gần trung tâm cạnh khuôn viên đại học. Có lịch sử từ thế kỷ 19, nơi đây từ lâu đã là chốn dạo chơi, hò hẹn và giải trí của nhiều thế hệ. Công viên kết hợp không gian xanh với các trò chơi hiện đại: vòng đu quay khổng lồ (ferris wheel) cho tầm nhìn bao quát thành phố, đu quay ngựa gỗ, các trò cảm giác mạnh, khu vui chơi trẻ em, cùng sân khấu ngoài trời thường xuyên diễn ra sự kiện, lễ hội và biểu diễn. Vào mùa hè, Gorsad rộn ràng tiếng nhạc và tiếng cười; mùa đông, một phần công viên biến thành 'thị trấn băng' với cầu trượt tuyết và trang trí năm mới. Đây là điểm đến thư giãn, vui vẻ, đặc biệt phù hợp cho các gia đình có trẻ nhỏ giữa hành trình khám phá thành phố.",
    [
        "Công viên giải trí lâu đời ngay trung tâm với vòng đu quay ngắm toàn cảnh",
        "Nhiều trò chơi, khu thiếu nhi và sân khấu ngoài trời tổ chức sự kiện",
        "Mùa đông biến thành 'thị trấn băng' với cầu trượt tuyết và trang trí năm mới",
    ],
    p("Mở cửa hằng ngày, thường khoảng 10:00–22:00 (mùa hè); các trò chơi theo giờ riêng.",
      "Vào công viên miễn phí; các trò chơi bán vé riêng.",
      "Khoảng 1–2 giờ.",
      "Mùa hè cho các trò chơi; dịp năm mới cho không gian băng tuyết.",
      "Hợp gia đình có trẻ em; kết hợp gần đại học và các điểm trung tâm."),
    [
        {"title": "Wikipedia (RU) — Городской сад (Томск)", "url": "https://ru.wikipedia.org/wiki/Городской_сад_(Томск)"},
        {"title": "Товики — Городской сад", "url": "https://towiki.ru/view/Городской_сад"},
    ],
    ["park_garden", "amusement", "family", "recreation", "tomsk", "city-center"],
    maps_text("Городской сад", "Томск", "City Garden Gorsad", "Tomsk", 56.472466, 84.954782),
))

# 23) Синий Утёс ------------------------------------------------------------------
RECORDS.append(rec(
    "siny-utyos-tomsk",
    "Vách đá Siny Utyos (Mỏm đá Xanh)",
    "Синий Утёс",
    "Siny Utyos (Blue Cliff)",
    ["park_garden"],
    56.334991, 84.921460,
    "Gần làng Kolarovo, bờ sông Tom, huyện Tomsk, tỉnh Tomsk, Nga",
    "Vách đá cao dựng đứng bên sông Tom, ánh lên sắc xanh lam đặc trưng vào những ngày trời quang. Một trong những thắng cảnh thiên nhiên đẹp và được yêu thích nhất vùng ngoại ô Tomsk.",
    "Vách đá Siny Utyos ('mỏm đá xanh') là một trong những cảnh quan thiên nhiên nổi tiếng nhất của vùng ngoại ô Tomsk, nằm bên bờ sông Tom gần làng Kolarovo, cách thành phố khoảng 25–30 km. Đây là một bờ đá cao dựng đứng, cấu tạo từ đá phiến sét chứa khoáng chất khiến bề mặt ánh lên sắc xanh lam - xám đặc trưng, đặc biệt rõ vào những ngày nắng đẹp, và cũng là nguồn gốc của cái tên 'mỏm đá xanh'. Từ trên đỉnh vách, du khách có tầm nhìn tuyệt đẹp bao quát khúc sông Tom uốn lượn và những cánh rừng taiga trải dài phía chân trời. Khu vực này là điểm dã ngoại, đi bộ đường dài và nghỉ dưỡng quen thuộc của người Tomsk (gần đó có khu điều dưỡng cùng tên). Vào mùa hè, đây là chốn cắm trại, ngắm cảnh lý tưởng; mùa thu, sắc lá vàng đỏ càng làm khung cảnh thêm ngoạn mục. Một chuyến đi ngắn ra Siny Utyos là cách tuyệt vời để chạm vào thiên nhiên Siberia ngay sát thành phố.",
    [
        "Vách đá cao dựng đứng bên sông Tom, ánh sắc xanh lam đặc trưng",
        "Tầm nhìn ngoạn mục bao quát khúc sông uốn lượn và rừng taiga",
        "Điểm dã ngoại, cắm trại và ngắm cảnh yêu thích của người Tomsk",
    ],
    p("Không gian thiên nhiên ngoài trời, tham quan tự do.",
      "Miễn phí (chỉ tốn chi phí di chuyển).",
      "Nửa ngày (kể cả di chuyển từ Tomsk).",
      "Mùa hè để dã ngoại; mùa thu cho sắc lá đẹp nhất.",
      "Cách Tomsk ~25–30 km - nên đi ô tô; cẩn thận khi đứng gần mép vách đá cao."),
    [
        {"title": "Wikipedia (RU) — Синий Утёс", "url": "https://ru.wikipedia.org/wiki/Синий_Утёс"},
        {"title": "Товики — Синий Утёс", "url": "https://towiki.ru/view/Синий_Утёс"},
    ],
    ["park_garden", "nature", "cliff", "tom-river", "tomsk-region", "viewpoint"],
    maps_text("Синий Утёс", "Коларово, Томская область", "Siny Utyos Blue Cliff", "Tomsk Oblast", 56.334991, 84.921460),
))

# 24) Таловские чаши --------------------------------------------------------------
RECORDS.append(rec(
    "talovskie-chashi-tomsk",
    "Chén đá Talovskie (Talovskie chashi)",
    "Таловские чаши",
    "Talovskie Chashi (Stone Bowls)",
    ["park_garden"],
    56.300000, 85.416667,
    "Vùng rừng gần làng Basandaika, huyện Tomsk, tỉnh Tomsk, Nga",
    "Những 'chiếc chén' đá vôi tự nhiên kỳ lạ giữa rừng taiga, hình thành từ khoáng chất kết tủa quanh mạch nước ngầm. Một di tích thiên nhiên độc đáo và bí ẩn của tỉnh Tomsk.",
    "Chén đá Talovskie là một di tích thiên nhiên độc nhất vô nhị của tỉnh Tomsk: giữa rừng taiga hoang sơ, cách thành phố khoảng 40 km về phía đông nam, xuất hiện những 'chiếc chén' bằng đá có thành cao, lòng chứa đầy nước trong vắt. Chúng được hình thành hoàn toàn tự nhiên: nước ngầm giàu khoáng chất (chủ yếu là canxi cacbonat - đá vôi travertine) trào lên và kết tủa dần qua hàng nghìn năm, tạo nên những vành đá bao quanh mạch nước như những chiếc bồn tắm khổng lồ. Có vài chiếc chén lớn nhỏ khác nhau, chiếc lớn nhất đủ để một người ngồi lọt vào trong. Hình dạng kỳ lạ và cơ chế hình thành hiếm gặp khiến nơi đây được công nhận là đài kỷ niệm thiên nhiên và bao phủ bởi nhiều truyền thuyết dân gian. Đường vào khá hoang sơ, phải đi bộ xuyên rừng một đoạn, nên chuyến tham quan mang màu sắc phiêu lưu, dành cho những ai yêu thích khám phá thiên nhiên nguyên bản của Siberia.",
    [
        "Những 'chén' đá vôi tự nhiên chứa nước trong, hình thành qua hàng nghìn năm",
        "Di tích thiên nhiên độc đáo giữa rừng taiga, được công nhận đài kỷ niệm thiên nhiên",
        "Chuyến khám phá mang màu sắc phiêu lưu, phải đi bộ xuyên rừng",
    ],
    p("Không gian thiên nhiên hoang sơ, tham quan tự do; nên đi ban ngày.",
      "Miễn phí (chỉ tốn chi phí di chuyển).",
      "Cả ngày (di chuyển xa và đi bộ trong rừng).",
      "Mùa hè và đầu thu, khi đường rừng khô ráo, dễ đi.",
      "Cách Tomsk ~40 km - nên đi ô tô địa hình và có người dẫn đường/định vị GPS; mang giày lội và chống muỗi."),
    [
        {"title": "Wikipedia (RU) — Таловские чаши", "url": "https://ru.wikipedia.org/wiki/Таловские_чаши"},
        {"title": "Товики — Таловские чаши", "url": "https://towiki.ru/view/Таловские_чаши"},
    ],
    ["park_garden", "nature", "natural-monument", "taiga", "tomsk-region", "adventure"],
    maps_text("Таловские чаши", "Томский район", "Talovskie Chashi Stone Bowls", "Tomsk Oblast", 56.300000, 85.416667),
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
