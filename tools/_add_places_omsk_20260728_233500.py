# -*- coding: utf-8 -*-
"""_add_places_omsk_20260728_233500.py — VÙNG: Tỉnh Omsk (Омская область)
(lần chạy tự động 2026-07-28).

Bối cảnh: omsk.json hiện có 7 địa điểm (Успенский собор / Dormition cathedral, Любинский проспект,
Омская крепость, Литературный музей им. Достоевского, парк «Птичья гавань», Ачаирский монастырь,
музей им. Врубеля). Bổ sung 30 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình →
đưa vùng lên 37. TRÁNH trùng 7 điểm trên (đặc biệt: KHÔNG thêm lại Успенский/Dormition, Ачаир, Врубель).

Trung tâm là thành phố Omsk; mở rộng ra Большеречье (vườn thú + «Старина Сибирская»), Тара (thành phố
cổ nhất tỉnh) và các điểm thiên nhiên (озеро Линёво «Пять озёр», солёные озёра Эбейты và Ульжай).

Phân bố loại hình (30 bản ghi mới):
- museum (4): историко-краеведческий музей, Либеров-центр, Дом-музей Кондратия Белова, «Старина Сибирская».
- theatre (4): академический театр драмы, музыкальный театр, театр «Арлекин», филармония (концертный зал).
- square_street (3): Соборная площадь, улица Чокана Валиханова, площадь Бухгольца («Держава»).
- monument (5): Тарские ворота (+fortress), «Слесарь Степаныч», Пожарная каланча, памятник Достоевскому,
  город Тара (+square_street).
- palace (1): особняк Батюшкина / «Дом Колчака».
- church (6): Никольский казачий собор, Крестовоздвиженский собор, Соборная мечеть (tag mosque),
  Христорождественский собор, Спасский собор (Тара).  (Соборная мечеть xếp category "church" theo quy
  ước của dự án cho công trình tôn giáo, kèm tag "mosque".)
- park_garden (6): Парк Победы, Зелёный остров, Большереченский зоопарк, озеро Линёво, озеро Эбейты, озеро Ульжай.
- bridge (2): Юбилейный мост (через Ом), Метромост им. 60-летия Победы (через Иртыш).

TOẠ ĐỘ — xác minh chéo (2GIS og:image center=LON,LAT; sobory.ru; ru.wikipedia; openarium.ru; omskmap.ru;
Yandex Maps, 2026-07-28). Phạm vi Omsk lat ~53.5–58, lon ~70–77 (TP Omsk ~54.99, 73.37) — tất cả toạ độ
trong phạm vi, KHÔNG đảo lat/lon:
  историко-краеведческий музей 54.980051,73.378274 (2gis geo); Либеров-центр 54.983793,73.382590 (2gis firm
  + Yandex org); Дом-музей Белова 54.974552,73.380414 (2gis firm); театр драмы 54.987849,73.370892 (2gis firm);
  музыкальный театр 54.982456,73.382709 (2gis firm); «Арлекин» 54.957487,73.387470 (2gis firm, Карла Маркса 41А);
  филармония/концертный зал 54.977038,73.379005 (2gis firm, Ленина 27А); Соборная площадь 54.990362,73.367032
  (2gis geo); ул. Чокана Валиханова 54.974743,73.380067 (2gis geo); Тарские ворота 54.987692,73.367980 (2gis geo);
  «Слесарь Степаныч» 54.985315,73.374481 (2gis geo, Ленина); Пожарная каланча 54.991362,73.370735 (2gis geo,
  Интернациональная 41); памятник Достоевскому 54.985128,73.367876 (2gis geo); пл. Бухгольца/«Держава»
  54.980721,73.372782 (2gis geo); особняк Батюшкина/Дом Колчака 54.979097,73.374248 (2gis, Иртышская наб. 9);
  Никольский казачий собор 54.977597,73.379545 (2gis + Yandex org, Ленина 27); Крестовоздвиженский собор
  54.997101,73.368695 (2gis, Тарская 33); Соборная мечеть 54.985190,73.423691 (2gis, 20-я линия 102);
  Христорождественский собор 54.994118,73.290782 (2gis, Степанца 5); Парк Победы 54.963511,73.360722 (2gis geo);
  Зелёный остров (ПКиО) 55.003604,73.338515 (2gis firm, Старозагородная Роща 10/3); Большереченский зоопарк
  56.089631,74.642267 (2gis + Yandex org, пгт Большеречье); «Старина Сибирская» 56.093674,74.640606 (2gis,
  Большеречье); озеро Линёво 56.406900,75.623900 (openarium.ru + omskmap.ru, Муромцевский р-н); озеро Эбейты
  54.644432,71.737852 (2gis geo); озеро Ульжай 54.253161,75.108634 (2gis geo, Черлакский р-н); Юбилейный мост
  54.982575,73.376567 (2gis geo); Метромост 60-летия Победы 54.989739,73.349304 (2gis geo); город Тара
  56.902500,74.370833 (ru.wiki); Спасский собор (Тара) 56.896424,74.383503 (sobory.ru object 07876).

GHI CHÚ: đã BỎ QUA / KHÔNG thêm các đối tượng trùng điểm đã có hoặc rủi ro, gồm: Успенский (Dormition) собор,
Ачаирский монастырь, музей им. Врубеля (ĐÃ CÓ trong file); скульптура «Люба»/«Любочка» (đã nằm trong bản ghi
Любинский проспект — tránh chồng lấn); озеро Данилово («Пять озёр») — nhiều nguồn xếp về ranh giới/Кыштовский
р-н Новосибирской обл., nên chọn озеро Линёво (nằm HẲN trong Муромцевский р-н Омской обл.) làm đại diện «Пять
озёр». KHÔNG bịa toạ độ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_omsk_20260728_233500.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "omsk"
REGION_NAME_VI = "Tỉnh Omsk"
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

# 1) Омский государственный историко-краеведческий музей ---------------------------
RECORDS.append(rec(
    "omsk-local-lore-museum",
    "Bảo tàng Lịch sử - Địa phương học Quốc gia Omsk (Kra-ê-vét-trê-xki)",
    "Омский государственный историко-краеведческий музей",
    "Omsk State Museum of History and Local Lore",
    ["museum"],
    54.980051, 73.378274,
    "Phố Lenina 23А, trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Bảo tàng lâu đời và lớn nhất tỉnh Omsk, thành lập từ năm 1878, lưu giữ hơn 200.000 hiện vật về thiên nhiên, khảo cổ, dân tộc học và lịch sử vùng Prииртышье. Đây là nơi tốt nhất để hiểu tổng thể vùng đất Siberia bên sông Irtysh.",
    "Bảo tàng Lịch sử - Địa phương học Quốc gia Omsk là một trong những bảo tàng lâu đời nhất Siberia, khởi lập từ năm 1878 dưới thời Đế quốc Nga và ngày nay giữ vai trò 'kho ký ức' của cả vùng Prииртышье. Bộ sưu tập đồ sộ với hơn 200.000 hiện vật trải rộng từ mẫu vật thiên nhiên, hoá thạch, sưu tập khảo cổ và dân tộc học của các dân tộc Siberia, đến vũ khí, tiền cổ, sách hiếm, tài liệu lưu trữ và tác phẩm nghệ thuật. Một trong những báu vật nổi tiếng của bảo tàng là lá cờ (знамя) gắn với đoàn thám hiểm lập nên Omsk và các di sản Cossack. Các gian trưng bày thường trực cùng nhiều triển lãm luân phiên dẫn dắt người xem qua lịch sử khai hoang, đời sống nông dân - thị dân, thời kỳ đường sắt xuyên Siberia và thế kỷ 20 đầy biến động. Với du khách, đây là điểm khởi đầu lý tưởng để nắm bắt bức tranh toàn cảnh về thiên nhiên, con người và lịch sử của tỉnh Omsk.",
    [
        "Một trong những bảo tàng lâu đời nhất Siberia (thành lập 1878) với hơn 200.000 hiện vật.",
        "Sưu tập phong phú về thiên nhiên, khảo cổ và dân tộc học của vùng Prииртышье.",
        "Lưu giữ nhiều báu vật gắn với lịch sử khai hoang và di sản Cossack Omsk.",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa ở mức phải chăng (vài trăm rúp); ưu đãi cho học sinh, sinh viên và người cao tuổi.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm; hợp cả những ngày thời tiết xấu.",
      "Nằm ngay trung tâm, gần Quảng trường Nhà thờ và bảo tàng Vrubel; thuyết minh chủ yếu bằng tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Омский государственный историко-краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Омский_государственный_историко-краеведческий_музей"},
        {"title": "Culture.ru — Омский историко-краеведческий музей", "url": "https://www.culture.ru/institutes/11023/omskii-gosudarstvennyi-istoriko-kraevedcheskii-muzei"},
    ],
    ["museum", "history", "local-lore", "omsk", "archaeology", "siberia"],
    maps_text("Омский государственный историко-краеведческий музей", "Омск", "Omsk State Museum of History and Local Lore", "Omsk", 54.980051, 73.378274),
))

# 2) Либеров-центр ----------------------------------------------------------------
RECORDS.append(rec(
    "liberov-center",
    "Bảo tàng Nghệ thuật 'Trung tâm Liberov' (Li-bê-rốp)",
    "Городской музей «Искусство Омска» / Либеров-центр",
    "Liberov Center Art Museum",
    ["museum"],
    54.983793, 73.382590,
    "Phố Dumskaya 3, trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Bảo tàng nghệ thuật ấm cúng dành riêng cho di sản của hoạ sĩ Aleksey Liberov - bậc thầy tranh phấn màu (pastel) của Siberia. Đặt trong một biệt thự gỗ cổ duyên dáng, nơi đây còn là không gian triển lãm và giáo dục nghệ thuật.",
    "Trung tâm Liberov (Либеров-центр) là một bảo tàng - trung tâm nghệ thuật nhỏ nhưng đầy chất thơ ở trung tâm Omsk, dành để tôn vinh sự nghiệp của Aleksey Nikolaevich Liberov (1911–2001) - hoạ sĩ nhân dân Nga, người được coi là bậc thầy tranh phấn màu (pastel) của trường phái phong cảnh Siberia. Bảo tàng đặt trong một biệt thự gỗ đầu thế kỷ 20 mang phong cách kiến trúc gỗ đặc trưng của Omsk, tạo nên bầu không khí ấm áp, thân mật hiếm có. Bên trong trưng bày nhiều tác phẩm của Liberov cùng các nghệ sĩ Omsk, phản ánh vẻ đẹp trầm lắng của thiên nhiên và đời sống vùng Tây Siberia. Ngoài triển lãm thường trực, trung tâm còn tổ chức các triển lãm chuyên đề, buổi hoà nhạc nhỏ, lớp học nghệ thuật cho trẻ em và người lớn, trở thành một 'ốc đảo văn hoá' được người dân yêu mến. Đây là điểm dừng tinh tế cho du khách muốn cảm nhận một góc nghệ thuật đương đại và không gian gỗ cổ điển của thành phố.",
    [
        "Bảo tàng dành riêng cho hoạ sĩ Aleksey Liberov - bậc thầy tranh phấn màu Siberia.",
        "Đặt trong biệt thự gỗ cổ đầu thế kỷ 20, kiến trúc gỗ đặc trưng của Omsk.",
        "Không gian triển lãm, hoà nhạc nhỏ và lớp học nghệ thuật ấm cúng.",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa thấp; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 45–60 phút.",
      "Quanh năm; hợp cả ngày mưa lạnh.",
      "Nằm ở trung tâm, dễ kết hợp dạo phố Lenin; xem lịch triển lãm và sự kiện trước khi đến."),
    [
        {"title": "Culture.ru — Либеров-центр", "url": "https://www.culture.ru/institutes/11020/liberov-centr"},
        {"title": "Gotoomsk.ru — Либеров-центр", "url": "https://gotoomsk.ru/places/liberov-centr/"},
    ],
    ["museum", "art", "pastel", "omsk", "culture", "siberia"],
    maps_org("https://yandex.com/maps/org/liberov_tsentr/1207060226/", "Liberov Center Art Museum", "Omsk"),
))

# 3) Дом-музей художника Кондратия Белова ------------------------------------------
RECORDS.append(rec(
    "kondraty-belov-art-museum",
    "Nhà - Bảo tàng hoạ sĩ Kondraty Belov (Bê-lốp)",
    "Музей Кондратия Белова (Дом-музей художника)",
    "Kondraty Belov Art Museum",
    ["museum"],
    54.974552, 73.380414,
    "Phố Chokana Valikhanova 10, thành phố Omsk, tỉnh Omsk, Nga",
    "Bảo tàng - nhà tưởng niệm hoạ sĩ Kondraty Belov, đặt trong một biệt thự gỗ trạm trổ tinh xảo bậc nhất Omsk. Đây vừa là điểm chiêm ngưỡng tranh phong cảnh Siberia, vừa là mẫu kiến trúc gỗ độc đáo.",
    "Bảo tàng Kondraty Belov nằm trong một trong những ngôi biệt thự gỗ đẹp nhất còn lại của Omsk - một công trình đầu thế kỷ 20 với đầu hồi, cửa sổ và diềm mái chạm khắc gỗ (наличники) tinh xảo, bản thân nó đã là một tác phẩm nghệ thuật và di tích kiến trúc. Bảo tàng dành để tưởng nhớ Kondraty Petrovich Belov (1900–1988) - hoạ sĩ nhân dân RSFSR, người nổi tiếng với những bức tranh phong cảnh hùng vĩ về sông Irtysh và thiên nhiên Siberia. Bên trong trưng bày các tác phẩm của ông cùng tư liệu về cuộc đời, xưởng vẽ và gia đình nghệ sĩ, đưa người xem vào thế giới sáng tạo gắn bó máu thịt với vùng đất quê hương. Bảo tàng cũng thường tổ chức triển lãm, sự kiện văn hoá và là điểm chụp ảnh yêu thích nhờ vẻ đẹp cổ kính của toà nhà. Ghé thăm nơi đây, du khách vừa thưởng lãm hội hoạ, vừa chiêm ngưỡng di sản kiến trúc gỗ đang dần hiếm hoi của Siberia.",
    [
        "Đặt trong biệt thự gỗ chạm trổ tinh xảo bậc nhất Omsk - bản thân là di tích kiến trúc.",
        "Tôn vinh hoạ sĩ Kondraty Belov với những bức tranh phong cảnh sông Irtysh và Siberia.",
        "Không gian tưởng niệm gồm tranh, tư liệu và xưởng vẽ của nghệ sĩ.",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa thấp; ưu đãi cho học sinh, sinh viên và người cao tuổi.",
      "Khoảng 45–60 phút.",
      "Quanh năm; toà nhà gỗ đặc biệt đẹp khi có nắng và có tuyết phủ.",
      "Nằm gần bờ sông Irtysh và phố đi bộ Chokan Valikhanov; đừng quên chụp ảnh mặt tiền gỗ chạm khắc."),
    [
        {"title": "Culture.ru — Музей Кондратия Белова", "url": "https://www.culture.ru/institutes/11019/muzei-kondratiya-belova"},
        {"title": "Gotoomsk.ru — Дом-музей Кондратия Белова", "url": "https://gotoomsk.ru/places/muzej-kondratiya-belova/"},
    ],
    ["museum", "art", "wooden-architecture", "omsk", "painting", "siberia"],
    maps_text("Музей Кондратия Белова", "Омск", "Kondraty Belov Art Museum", "Omsk", 54.974552, 73.380414),
))

# 4) «Старина Сибирская» (Большеречье) ---------------------------------------------
RECORDS.append(rec(
    "starina-sibirskaya",
    "Khu phức hợp Lịch sử - Văn hóa 'Starina Sibirskaya' (Xta-ri-na Xi-bia-xkai-a)",
    "Историко-культурный комплекс «Старина Сибирская»",
    "Starina Sibirskaya Historical-Cultural Complex",
    ["museum"],
    56.093674, 74.640606,
    "Phố Krasnoarmeyskaya, làng đô thị Bolsherechye, huyện Bolsherechensky, tỉnh Omsk, Nga",
    "Bảo tàng ngoài trời tái hiện ngôi làng Siberia xưa, với những ngôi nhà gỗ, nhà thờ, xưởng thủ công và nông cụ nguyên bản. Nơi đây cho du khách 'sống lại' đời sống nông dân khai hoang vùng Tây Siberia.",
    "'Starina Sibirskaya' (nghĩa là 'Miền Siberia xưa') là một khu phức hợp lịch sử - văn hoá kiểu bảo tàng ngoài trời (скансен) tại thị trấn Bolsherechye, cách Omsk khoảng 200 km về phía bắc. Tại đây, những ngôi nhà gỗ nông dân, nhà thương gia, nhà nguyện, trường làng, xưởng rèn và cối xay được sưu tầm, phục dựng và sắp đặt thành một 'ngôi làng Siberia' sống động của thế kỷ 19 - đầu thế kỷ 20. Du khách có thể bước vào từng ngôi izba với bếp lò Nga, đồ gia dụng, khung cửi và tự tay trải nghiệm các nghề thủ công truyền thống như dệt, làm gốm, nướng bánh. Khu phức hợp thường xuyên tổ chức lễ hội dân gian, các nghi thức phong tục Nga (đám cưới, Maslenitsa, hội chợ) với trang phục và âm nhạc cổ truyền. Kết hợp với vườn thú Bolsherechye ngay gần đó, 'Starina Sibirskaya' biến chuyến đi về vùng nông thôn phía bắc Omsk thành một hành trình ngược thời gian đầy màu sắc, đặc biệt hấp dẫn với gia đình và người yêu văn hoá dân gian.",
    [
        "Bảo tàng ngoài trời tái hiện làng Siberia thế kỷ 19 - đầu thế kỷ 20 với nhà gỗ, nhà nguyện, xưởng thủ công.",
        "Trải nghiệm nghề truyền thống (dệt, gốm, nướng bánh) và các nghi lễ, lễ hội dân gian Nga.",
        "Kết hợp thuận tiện với vườn thú Bolsherechye trong cùng chuyến đi.",
    ],
    p("Thường mở cửa hằng ngày khoảng 9:00–18:00 (có thể thay đổi theo mùa và ngày lễ); nên gọi xác nhận.",
      "Vé vào cửa mức phải chăng; các lớp trải nghiệm thủ công và tour có hướng dẫn tính phí thêm.",
      "Khoảng 1,5–2,5 giờ; tính cả di chuyển nên dành trọn một ngày cho Bolsherechye.",
      "Mùa hè cho cảnh quan đẹp; các dịp lễ dân gian (Maslenitsa, hội chợ) rất giàu không khí.",
      "Cách Omsk khoảng 200 km; nên đi ô tô hoặc tour. Kết hợp tham quan vườn thú Bolsherechye kề bên."),
    [
        {"title": "Culture.ru — «Старина Сибирская»", "url": "https://www.culture.ru/institutes/11036/istoriko-kulturnyi-kompleks-starina-sibirskaya"},
        {"title": "Gotoomsk.ru — «Старина Сибирская»", "url": "https://gotoomsk.ru/places/starina-sibirskaya/"},
    ],
    ["museum", "open-air", "ethnography", "folk", "bolsherechye", "siberia"],
    maps_text("Историко-культурный комплекс Старина Сибирская", "Большеречье", "Starina Sibirskaya", "Bolsherechye", 56.093674, 74.640606),
))

# ============================ NHÀ HÁT (theatre) ============================

# 5) Омский государственный академический театр драмы -----------------------------
RECORDS.append(rec(
    "omsk-academic-drama-theatre",
    "Nhà hát Kịch Hàn lâm Quốc gia Omsk (Tê-a-tơ Đra-ma)",
    "Омский государственный академический театр драмы",
    "Omsk State Academic Drama Theatre",
    ["theatre"],
    54.987849, 73.370892,
    "Phố Lenina 8А, trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Nhà hát kịch lâu đời và danh giá bậc nhất Siberia, thành lập năm 1874, được phong danh hiệu 'Hàn lâm'. Toà nhà tráng lệ năm 1905 với những bức tượng trang trí là một trong những công trình biểu tượng của Omsk.",
    "Nhà hát Kịch Hàn lâm Quốc gia Omsk là một trong những nhà hát kịch lâu đời và uy tín nhất nước Nga bên ngoài hai thủ đô, có lịch sử từ năm 1874 khi người dân Omsk góp tiền lập nên sân khấu đầu tiên. Toà nhà nhà hát bề thế hiện nay được xây năm 1905 theo phong cách chiết trung lộng lẫy, với mặt tiền trang trí tượng và tác phẩm điêu khắc 'Nàng thơ với đàn lia' trên nóc - từ lâu đã trở thành biểu tượng kiến trúc của thành phố. Đoàn kịch Omsk nổi tiếng cả nước về chất lượng dàn dựng, nhiều lần đoạt giải 'Mặt nạ vàng' (Золотая маска) danh giá và lưu diễn khắp Nga cùng quốc tế. Tiết mục trải rộng từ bi kịch, chính kịch cổ điển Nga và thế giới đến các vở đương đại. Ngay cả khi không xem diễn, du khách vẫn nên ghé ngắm toà nhà và không gian phố Lenin quanh đó. Một buổi tối thưởng thức kịch tại đây là trải nghiệm văn hoá đáng nhớ, giúp cảm nhận đời sống tinh thần sâu sắc của 'thủ phủ sân khấu' vùng Siberia.",
    [
        "Nhà hát kịch lâu đời (1874) và danh giá bậc nhất Siberia, nhiều lần đoạt giải 'Mặt nạ vàng'.",
        "Toà nhà năm 1905 lộng lẫy với tượng 'Nàng thơ với đàn lia' trên nóc - biểu tượng của Omsk.",
        "Tiết mục chất lượng cao từ kịch cổ điển Nga - thế giới đến sân khấu đương đại.",
    ],
    p("Mở theo lịch biểu diễn và giờ bán vé; nên xem lịch và đặt vé trước.",
      "Có bán vé xem kịch; giá tuỳ suất diễn và hạng ghế.",
      "Buổi diễn thường 2–3 giờ; ngắm toà nhà bên ngoài khoảng 15 phút.",
      "Mùa diễn (thu–xuân); dịp liên hoan sân khấu có nhiều vở đặc sắc.",
      "Đặt vé qua trang chính thức hoặc phòng vé; các vở bằng tiếng Nga. Nằm ngay trung tâm, dễ kết hợp dạo phố."),
    [
        {"title": "Wikipedia (RU) — Омский академический театр драмы", "url": "https://ru.wikipedia.org/wiki/Омский_академический_театр_драмы"},
        {"title": "Culture.ru — Омский государственный академический театр драмы", "url": "https://www.culture.ru/institutes/10196/omskii-gosudarstvennyi-akademicheskii-teatr-dramy"},
    ],
    ["theatre", "drama", "omsk", "architecture", "culture", "siberia"],
    maps_text("Омский государственный академический театр драмы", "Омск", "Omsk State Academic Drama Theatre", "Omsk", 54.987849, 73.370892),
))

# 6) Омский государственный музыкальный театр -------------------------------------
RECORDS.append(rec(
    "omsk-music-theatre",
    "Nhà hát Nhạc kịch Quốc gia Omsk (Mu-di-can-nưi Tê-a-tơ)",
    "Омский государственный музыкальный театр",
    "Omsk State Music Theatre",
    ["theatre"],
    54.982456, 73.382709,
    "Phố 10 let Oktyabrya 2, thành phố Omsk, tỉnh Omsk, Nga",
    "Nhà hát nhạc kịch chính của Omsk, dựng opera, operetta, nhạc kịch và ballet. Toà nhà hiện đại thập niên 1980 với hình khối độc đáo tựa 'chiếc đàn dương cầm bay' là một điểm nhận diện kiến trúc của thành phố.",
    "Nhà hát Nhạc kịch Quốc gia Omsk là trung tâm nghệ thuật âm nhạc - sân khấu hàng đầu của thành phố, có nguồn gốc từ nhà hát nhạc kịch thành lập giữa thế kỷ 20 và chuyển về toà nhà mới bề thế vào năm 1982. Công trình mang kiến trúc hiện đại thời Xô Viết với phần mái vươn dốc đặc trưng mà người dân ví như một 'cây đàn dương cầm khổng lồ' hay con tàu đang lướt, trở thành điểm nhận diện dễ nhớ ở khu vực bên sông Om. Đoàn hát dàn dựng đa dạng thể loại: opera, operetta, nhạc kịch (musical), ballet và các chương trình hoà nhạc, với dàn nhạc, hợp xướng và vũ đoàn riêng. Không gian khán phòng rộng lớn thường xuyên sáng đèn với các vở kinh điển lẫn tác phẩm mới, thu hút đông đảo khán giả mọi lứa tuổi. Với du khách, một buổi tối xem operetta hay nhạc kịch tại đây là cách thưởng thức nghệ thuật giàu cảm xúc, đồng thời chiêm ngưỡng một biểu tượng kiến trúc hiện đại của Omsk.",
    [
        "Nhà hát nhạc kịch chính của Omsk: opera, operetta, nhạc kịch và ballet.",
        "Toà nhà năm 1982 với hình khối hiện đại độc đáo tựa 'cây đàn dương cầm bay'.",
        "Có dàn nhạc, hợp xướng và vũ đoàn riêng, chương trình đa dạng cho mọi lứa tuổi.",
    ],
    p("Mở theo lịch biểu diễn và giờ bán vé; nên xem lịch và đặt vé trước.",
      "Có bán vé; giá tuỳ chương trình và hạng ghế.",
      "Buổi diễn thường 2–2,5 giờ.",
      "Mùa diễn (thu–xuân); dịp lễ có nhiều chương trình đặc biệt.",
      "Đặt vé qua trang chính thức hoặc phòng vé; các vở bằng tiếng Nga nhưng nhạc kịch/ballet dễ thưởng thức."),
    [
        {"title": "Wikipedia (RU) — Омский музыкальный театр", "url": "https://ru.wikipedia.org/wiki/Омский_музыкальный_театр"},
        {"title": "Culture.ru — Омский государственный музыкальный театр", "url": "https://www.culture.ru/institutes/10199/omskii-gosudarstvennyi-muzykalnyi-teatr"},
    ],
    ["theatre", "music", "opera", "operetta", "omsk", "architecture"],
    maps_text("Омский государственный музыкальный театр", "Омск", "Omsk State Music Theatre", "Omsk", 54.982456, 73.382709),
))

# 7) Омский театр куклы, актёра, маски «Арлекин» ----------------------------------
RECORDS.append(rec(
    "arlekin-puppet-theatre",
    "Nhà hát Rối, Diễn viên và Mặt nạ 'Arlekin' (A-rờ-lê-kin)",
    "Омский театр куклы, актёра, маски «Арлекин»",
    "Arlekin Puppet, Actor and Mask Theatre",
    ["theatre"],
    54.957487, 73.387470,
    "Đại lộ Karla Marksa 41А, thành phố Omsk, tỉnh Omsk, Nga",
    "Nhà hát múa rối được yêu thích của Omsk, kết hợp nghệ thuật rối, diễn viên sống và mặt nạ. Đây là điểm đến quen thuộc của các gia đình có trẻ nhỏ, với những vở cổ tích sinh động.",
    "Nhà hát 'Arlekin' là nhà hát múa rối hàng đầu của Omsk, mang một cái tên đầy đủ độc đáo - 'nhà hát của rối, diễn viên và mặt nạ' - phản ánh phong cách dàn dựng phong phú kết hợp con rối, diễn viên bằng xương bằng thịt và nghệ thuật mặt nạ. Ra đời từ giữa thế kỷ 20, nhà hát chuyên các vở cổ tích Nga và thế giới dành cho thiếu nhi, nhưng cũng có những tác phẩm dành cho khán giả lớn tuổi. Toà nhà hiện đại, sáng sủa với không gian thân thiện là nơi nhiều thế hệ trẻ em Omsk lần đầu làm quen với sân khấu. Bên cạnh các buổi diễn thường kỳ, 'Arlekin' còn tham gia liên hoan múa rối trong nước và quốc tế, tổ chức chương trình giáo dục và các sự kiện dịp lễ. Với du khách đi cùng con nhỏ, đây là lựa chọn thú vị và ấm áp; các vở giàu hình ảnh, màu sắc và âm nhạc nên dễ theo dõi ngay cả khi không thạo tiếng Nga.",
    [
        "Nhà hát múa rối hàng đầu Omsk, kết hợp rối - diễn viên - mặt nạ.",
        "Chuyên các vở cổ tích cho thiếu nhi, cũng có tác phẩm cho người lớn.",
        "Thường tham gia liên hoan múa rối trong nước và quốc tế.",
    ],
    p("Mở theo lịch biểu diễn, thường cuối tuần và dịp lễ; xem lịch trước.",
      "Vé xem múa rối giá thấp, phù hợp gia đình.",
      "Buổi diễn thường 50–80 phút.",
      "Cuối tuần, dịp nghỉ lễ và mùa diễn.",
      "Phù hợp trẻ nhỏ; đặt vé trước dịp cao điểm. Vở giàu hình ảnh, dễ theo dõi dù không rành tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Омский театр куклы, актёра, маски «Арлекин»", "url": "https://ru.wikipedia.org/wiki/Омский_театр_куклы,_актёра,_маски_«Арлекин»"},
        {"title": "Culture.ru — Театр «Арлекин»", "url": "https://www.culture.ru/institutes/10205/omskii-gosudarstvennyi-teatr-kukly-aktyora-maski-arlekin"},
    ],
    ["theatre", "puppet", "children", "omsk", "culture", "siberia"],
    maps_text("Омский театр куклы актёра маски Арлекин", "Омск", "Arlekin Puppet Theatre", "Omsk", 54.957487, 73.387470),
))

# 8) Омская филармония (Концертный зал) -------------------------------------------
RECORDS.append(rec(
    "omsk-philharmonic",
    "Nhạc viện Omsk - Phòng hòa nhạc (Fi-lac-mô-ni-a)",
    "Омская филармония (Концертный зал)",
    "Omsk Philharmonic (Concert Hall)",
    ["theatre"],
    54.977038, 73.379005,
    "Phố Lenina 27А, trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Trung tâm âm nhạc hàn lâm của Omsk, nơi tổ chức hoà nhạc giao hưởng, organ, dân gian và jazz. Phòng hoà nhạc lớn với đại phong cầm (organ) là không gian biểu diễn danh tiếng của vùng Prииртышье.",
    "Nhạc viện (Омская филармония) là trung tâm âm nhạc hàn lâm và biểu diễn chủ lực của tỉnh Omsk, nơi đóng đô của Dàn nhạc Giao hưởng Học thuật Omsk cùng nhiều tập thể nghệ thuật khác - dàn nhạc dân gian, hợp xướng, các nhóm nhạc thính phòng và jazz. Phòng hoà nhạc chính của nhạc viện được trang bị một cây đại phong cầm (organ) lớn, cho phép tổ chức những buổi hoà nhạc organ trang trọng bên cạnh các chương trình giao hưởng, thính phòng, nhạc dân gian và biểu diễn dành cho thiếu nhi. Nhạc viện Omsk thường xuyên đón các nghệ sĩ, dàn nhạc danh tiếng từ khắp nước Nga và quốc tế đến lưu diễn, đồng thời là nơi tổ chức nhiều liên hoan âm nhạc. Toạ lạc ngay khu trung tâm trên phố Lenin, gần Nhà thờ Cossack Nikolsky, đây là điểm đến thuận tiện để kết hợp trong hành trình khám phá thành phố. Một buổi hoà nhạc buổi tối tại đây là cách tinh tế để tận hưởng đời sống âm nhạc sôi động của Omsk.",
    [
        "Trung tâm âm nhạc hàn lâm của tỉnh, nơi đóng đô của Dàn nhạc Giao hưởng Omsk.",
        "Phòng hoà nhạc lớn có đại phong cầm (organ) cho các buổi diễn trang trọng.",
        "Chương trình đa dạng: giao hưởng, organ, thính phòng, dân gian, jazz và nhạc thiếu nhi.",
    ],
    p("Mở theo lịch hoà nhạc và giờ bán vé; nên xem lịch trước.",
      "Có bán vé; giá tuỳ chương trình.",
      "Buổi diễn thường 1,5–2 giờ.",
      "Mùa hoà nhạc (thu–xuân).",
      "Đặt vé qua trang chính thức; nằm ngay trung tâm, dễ kết hợp Nhà thờ Nikolsky và phố Lenin."),
    [
        {"title": "Wikipedia (RU) — Омская филармония", "url": "https://ru.wikipedia.org/wiki/Омская_филармония"},
        {"title": "Culture.ru — Омская филармония", "url": "https://www.culture.ru/institutes/10202/omskaya-filarmoniya"},
    ],
    ["theatre", "music", "concert", "organ", "omsk", "philharmonic"],
    maps_text("Омская филармония концертный зал", "Омск", "Omsk Philharmonic Concert Hall", "Omsk", 54.977038, 73.379005),
))

# ============================ PHỐ / QUẢNG TRƯỜNG (square_street) ============================

# 9) Соборная площадь -------------------------------------------------------------
RECORDS.append(rec(
    "sobornaya-square-omsk",
    "Quảng trường Nhà thờ (Xô-boóc-nai-a Plô-sat)",
    "Соборная площадь",
    "Cathedral (Sobornaya) Square",
    ["square_street"],
    54.990362, 73.367032,
    "Trung tâm thành phố Omsk, tỉnh Omsk, Nga (bao quanh Nhà thờ Chính tòa Đức Mẹ An Giấc)",
    "Quảng trường trung tâm và trang trọng nhất Omsk, nơi toạ lạc Nhà thờ Chính tòa Đức Mẹ An Giấc lộng lẫy. Đây là không gian tổ chức lễ hội, sự kiện và là điểm hẹn quen thuộc của người dân thành phố.",
    "Quảng trường Nhà thờ (Соборная площадь) là quảng trường chính, uy nghi bậc nhất của Omsk, nằm ngay trung tâm lịch sử thành phố. Điểm nhấn của quảng trường là Nhà thờ Chính tòa Đức Mẹ An Giấc (Успенский собор) với những mái vòm rực rỡ - ngôi thánh đường đã được phục dựng nguyên bản đầu thế kỷ 21 và trở thành biểu tượng của Omsk. Quảng trường có lịch sử lâu đời, từng mang nhiều tên gọi qua các thời kỳ và luôn giữ vai trò trung tâm trong đời sống công cộng: đây là nơi diễn ra các nghi lễ, mít tinh, hội chợ, lễ hội thành phố, chợ Giáng sinh mùa đông cũng như những buổi hoà nhạc, sự kiện lớn. Không gian rộng thoáng với đài phun nước, thảm cỏ, bồn hoa và lối dạo bộ khiến quảng trường trở thành điểm hẹn, chụp ảnh và thư giãn quen thuộc của người dân lẫn du khách. Đứng giữa Quảng trường Nhà thờ, du khách có thể cảm nhận trọn vẹn nhịp sống, đức tin và vẻ đẹp kiến trúc của trái tim Omsk bên sông Irtysh.",
    [
        "Quảng trường trung tâm và trang trọng nhất Omsk, bao quanh Nhà thờ Đức Mẹ An Giấc.",
        "Nơi diễn ra lễ hội, hội chợ, chợ Giáng sinh và các sự kiện lớn của thành phố.",
        "Không gian rộng với đài phun nước, bồn hoa - điểm hẹn và chụp ảnh quen thuộc.",
    ],
    p("Không gian mở, dạo chơi tự do mọi lúc; nhộn nhịp nhất ban ngày và các dịp sự kiện.",
      "Miễn phí.",
      "Khoảng 30–45 phút (kết hợp tham quan nhà thờ).",
      "Cuối xuân đến đầu thu cho thời tiết dễ chịu; mùa đông có chợ và trang trí Giáng sinh.",
      "Kết hợp tham quan Nhà thờ Đức Mẹ An Giấc và bảo tàng gần đó; ăn mặc lịch sự khi vào nhà thờ."),
    [
        {"title": "Wikipedia (RU) — Соборная площадь (Омск)", "url": "https://ru.wikipedia.org/wiki/Соборная_площадь_(Омск)"},
        {"title": "Gotoomsk.ru — Соборная площадь", "url": "https://gotoomsk.ru/places/sobornaya-ploshhad/"},
    ],
    ["square-street", "square", "city-center", "omsk", "landmark", "siberia"],
    maps_text("Соборная площадь", "Омск", "Cathedral Square", "Omsk", 54.990362, 73.367032),
))

# 10) Улица Чокана Валиханова -----------------------------------------------------
RECORDS.append(rec(
    "chokan-valikhanov-street",
    "Phố đi bộ Chokan Valikhanov (Trô-kan Va-li-kha-nốp)",
    "Улица Чокана Валиханова",
    "Chokan Valikhanov Street",
    ["square_street"],
    54.974743, 73.380067,
    "Phố Chokana Valikhanova, ven sông Irtysh, trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Một trong những phố đi bộ đẹp và hiện đại nhất Omsk, được cải tạo công phu với đèn trang trí, tiểu cảnh và các hoạ tiết mang phong cách phương Đông. Con phố ven sông Irtysh là điểm dạo bộ, chụp ảnh yêu thích.",
    "Phố Chokan Valikhanov mang tên nhà khoa học, nhà thám hiểm và khai sáng người Kazakh Chokan Valikhanov - người từng gắn bó với Omsk thời trẻ. Sau đợt cải tạo lớn, con phố đã 'lột xác' thành một trong những không gian đi bộ đẹp và hiện đại nhất thành phố: mặt đường lát đá sang trọng, hệ thống đèn nghệ thuật, vòm ánh sáng, đài phun nước, ghế nghỉ và các tiểu cảnh trang trí mang cảm hứng phương Đông, tôn vinh tình hữu nghị Nga - Kazakhstan. Nằm ngay gần bờ sông Irtysh và khu trung tâm, phố Valikhanov nối liền không gian đô thị với bờ kè, tạo thành tuyến dạo bộ lý tưởng để ngắm cảnh, chụp ảnh và thư giãn. Vào buổi tối, khi đèn trang trí bật sáng, con phố trở nên đặc biệt lung linh, thu hút giới trẻ, gia đình và du khách. Đây cũng là nơi thường diễn ra các sự kiện, triển lãm ngoài trời và lễ hội đường phố, phản ánh diện mạo hiện đại, năng động của Omsk hôm nay.",
    [
        "Phố đi bộ hiện đại, cải tạo công phu với đèn nghệ thuật, vòm sáng và tiểu cảnh phương Đông.",
        "Mang tên nhà khai sáng Kazakh Chokan Valikhanov, tôn vinh hữu nghị Nga - Kazakhstan.",
        "Ven sông Irtysh, đặc biệt lung linh về đêm - điểm dạo bộ và chụp ảnh yêu thích.",
    ],
    p("Không gian mở, dạo chơi tự do mọi lúc; đẹp nhất vào buổi tối khi lên đèn.",
      "Miễn phí.",
      "Khoảng 45–60 phút.",
      "Cuối xuân đến đầu thu; buổi tối mùa hè khi đèn trang trí bật sáng rất nên thơ.",
      "Kết hợp dạo bờ kè sông Irtysh và Nhà - Bảo tàng Kondraty Belov gần đó."),
    [
        {"title": "Gotoomsk.ru — Улица Чокана Валиханова", "url": "https://gotoomsk.ru/places/ulica-chokana-valihanova/"},
        {"title": "Wikipedia (RU) — Улица Валиханова (Омск)", "url": "https://ru.wikipedia.org/wiki/Улица_Валиханова_(Омск)"},
    ],
    ["square-street", "pedestrian", "city-center", "omsk", "walking", "embankment"],
    maps_text("Улица Чокана Валиханова", "Омск", "Chokan Valikhanov Street", "Omsk", 54.974743, 73.380067),
))

# 11) Площадь Бухгольца и скульптура «Держава» ------------------------------------
RECORDS.append(rec(
    "buchholz-square-derzhava",
    "Quảng trường Bukholts và tượng cầu 'Derzhava' (Bú-khôn, 'Đéc-gia-va')",
    "Площадь Бухгольца (скульптура «Держава»)",
    "Buchholz Square and the Derzhava Sphere",
    ["square_street", "monument"],
    54.980721, 73.372782,
    "Quảng trường Bukholts, gần bờ sông Irtysh, trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Quảng trường mang tên Ivan Bukholts - người sáng lập Omsk, với điểm nhấn là quả cầu kim loại lớn 'Derzhava' chạm nổi cảnh khai hoang Siberia. Đây là biểu tượng về cội nguồn ra đời của thành phố.",
    "Quảng trường Bukholts nằm gần nơi hợp lưu sông Om và Irtysh, được đặt theo tên Ivan Dmitrievich Bukholts - viên sĩ quan chỉ huy đoàn thám hiểm đã dựng nên pháo đài Omsk đầu tiên năm 1716, tức người khai sinh ra thành phố. Trung tâm quảng trường là tác phẩm điêu khắc nổi tiếng 'Derzhava' (nghĩa là 'Vương quyền/Quả cầu quyền lực') - một quả cầu kim loại rỗng khổng lồ, trên bề mặt chạm nổi những hình ảnh về công cuộc khai hoang, chinh phục và định cư vùng Siberia thời các đoàn Cossack. Quả cầu đã trở thành một biểu tượng thị giác quen thuộc và điểm hẹn, chụp ảnh của người dân Omsk. Từ quảng trường, du khách có thể phóng tầm mắt ra dòng Irtysh rộng lớn và khu bờ kè, cảm nhận địa thế sông nước đã làm nên số phận của thành phố. Đây là một điểm dừng giàu ý nghĩa lịch sử - biểu tượng, gắn liền với câu chuyện về những ngày đầu Omsk ra đời giữa vùng biên cương Siberia.",
    [
        "Quảng trường mang tên Ivan Bukholts - người sáng lập pháo đài Omsk năm 1716.",
        "Tượng cầu kim loại lớn 'Derzhava' chạm nổi cảnh khai hoang, định cư Siberia.",
        "Vị trí ven sông Irtysh, gần hợp lưu Om - Irtysh, điểm ngắm cảnh và chụp ảnh.",
    ],
    p("Không gian mở, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Cuối xuân đến đầu thu; đẹp lúc hoàng hôn bên sông Irtysh.",
      "Kết hợp dạo bờ kè Irtysh và Pháo đài Omsk gần đó; chú ý an toàn khi ra sát bờ sông."),
    [
        {"title": "Wikipedia (RU) — Площадь Бухгольца", "url": "https://ru.wikipedia.org/wiki/Площадь_Бухгольца"},
        {"title": "Gotoomsk.ru — Площадь Бухгольца и «Держава»", "url": "https://gotoomsk.ru/places/ploshhad-buhgolca/"},
    ],
    ["square-street", "monument", "history", "omsk", "irtysh", "landmark"],
    maps_text("Площадь Бухгольца Держава", "Омск", "Buchholz Square Derzhava", "Omsk", 54.980721, 73.372782),
))

# ============================ ĐÀI TƯỞNG NIỆM / TƯỢNG (monument) ============================

# 12) Тарские ворота --------------------------------------------------------------
RECORDS.append(rec(
    "tarskiye-vorota",
    "Cổng Tara (Tác-xki-ê Va-rô-ta)",
    "Тарские ворота",
    "Tarskiye Vorota (Tara Gate)",
    ["monument", "fortress"],
    54.987692, 73.367980,
    "Phố Spartakovskaya (khu Pháo đài Omsk), trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Cổng thành phục dựng của pháo đài Omsk thứ hai - một biểu tượng lịch sử của thành phố. Cổng Tara gắn với ký ức về những năm tù đày của văn hào Dostoevsky và là điểm check-in nổi tiếng.",
    "Cổng Tara (Тарские ворота) là một trong những biểu tượng lịch sử được yêu thích nhất của Omsk. Cổng nguyên bản được xây năm 1792 như một trong bốn cổng của pháo đài Omsk thứ hai, mở về hướng thành phố Tara ở phía bắc - do đó có tên gọi này. Qua cổng vòm màu trắng ấy, các tù nhân khổ sai từng bị dẫn tới nhà tù trong pháo đài, và chính văn hào Fyodor Dostoevsky đã đi qua nơi đây trong những năm thụ án (1850–1854). Cổng gốc bị phá bỏ năm 1959, nhưng đến năm 1991, nhân dịp kỷ niệm 275 năm thành phố, Cổng Tara được phục dựng nguyên bản tại vị trí cũ và trở thành một cột mốc ký ức quan trọng. Ngày nay, cổng vòm trắng thanh thoát nằm trong không gian khu pháo đài lịch sử là điểm tham quan, chụp ảnh quen thuộc, đồng thời là nơi bắt đầu nhiều hành trình khám phá trung tâm cũ của Omsk. Đứng dưới vòm cổng, du khách như chạm vào lịch sử quân sự và văn học đặc biệt của thành phố bên sông Irtysh.",
    [
        "Cổng thành phục dựng (1991) theo nguyên bản năm 1792 của pháo đài Omsk thứ hai.",
        "Gắn với ký ức Dostoevsky và các tù nhân khổ sai từng đi qua để vào nhà tù pháo đài.",
        "Cổng vòm trắng thanh thoát - biểu tượng và điểm check-in nổi tiếng ở trung tâm cũ.",
    ],
    p("Không gian mở, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15–20 phút.",
      "Quanh năm; đẹp khi có nắng để chụp ảnh, và lung linh khi lên đèn buổi tối.",
      "Kết hợp tham quan khu Pháo đài Omsk, Bảo tàng Dostoevsky và Quảng trường Nhà thờ gần đó."),
    [
        {"title": "Wikipedia (RU) — Тарские ворота (Омск)", "url": "https://ru.wikipedia.org/wiki/Тарские_ворота_(Омск)"},
        {"title": "Gotoomsk.ru — Тарские ворота", "url": "https://gotoomsk.ru/places/tarskie-vorota/"},
    ],
    ["monument", "fortress", "history", "dostoevsky", "omsk", "landmark"],
    maps_text("Тарские ворота", "Омск", "Tarskiye Vorota Tara Gate", "Omsk", 54.987692, 73.367980),
))

# 13) Скульптура «Слесарь Степаныч» -----------------------------------------------
RECORDS.append(rec(
    "plumber-stepanych-sculpture",
    "Tượng thợ sửa ống nước 'Stepanych' (Xtê-pa-nứt)",
    "Скульптура «Слесарь Степаныч»",
    "Stepanych the Plumber Sculpture",
    ["monument"],
    54.985315, 73.374481,
    "Phố Lenina (gần Đại lộ Lyubinsky), trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Bức tượng đồng hài hước hình một người thợ sửa ống nước chui lên từ nắp cống, một trong những tác phẩm điêu khắc đường phố được yêu thích nhất Omsk. Đây là điểm chụp ảnh vui nhộn quen thuộc trên phố Lenin.",
    "'Slesar Stepanych' (Bác thợ Stepanych) là một trong những tác phẩm điêu khắc đường phố nổi tiếng và được yêu thích nhất Omsk. Được đặt vào năm 1998 nhân dịp kỷ niệm thành phố, bức tượng đồng khắc hoạ hình ảnh một người thợ sửa ống nước tinh nghịch đang nhô nửa người lên khỏi nắp hố ga, tay chống cằm, mỉm cười quan sát dòng người qua lại. Nằm ngay trên vỉa hè phố Lenin, gần khu Đại lộ Lyubinsky lịch sử, 'Stepanych' đã trở thành một 'cư dân' quen thuộc và đáng yêu của trung tâm thành phố. Người dân và du khách thường dừng lại chụp ảnh, xoa tay hoặc trò chuyện đùa với bức tượng như một người bạn. Tác phẩm mang phong cách điêu khắc đô thị hóm hỉnh, đời thường - xu hướng làm mềm không gian phố phường bằng những nhân vật gần gũi. Cùng với tượng 'Lyubochka' gần đó, 'Stepanych' góp phần tạo nên nét duyên riêng, ấm áp và giàu tính người cho khu trung tâm Omsk.",
    [
        "Tượng đồng hài hước hình thợ sửa ống nước nhô lên từ nắp hố ga (đặt năm 1998).",
        "Một trong những tác phẩm điêu khắc đường phố được yêu thích nhất Omsk.",
        "Điểm chụp ảnh vui nhộn trên phố Lenin, gần Đại lộ Lyubinsky.",
    ],
    p("Không gian ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 10 phút.",
      "Quanh năm; đẹp khi có nắng để chụp ảnh.",
      "Kết hợp dạo Đại lộ Lyubinsky và tìm các tượng đồng nhỏ khác dọc phố Lenin."),
    [
        {"title": "Gotoomsk.ru — Скульптура «Слесарь Степаныч»", "url": "https://gotoomsk.ru/places/skulptura-slesar-stepanych/"},
        {"title": "Wikipedia (RU) — Омск (городская скульптура)", "url": "https://ru.wikipedia.org/wiki/Омск"},
    ],
    ["monument", "sculpture", "street-art", "omsk", "city-center", "photo-spot"],
    maps_text("Скульптура Слесарь Степаныч", "Омск", "Stepanych the Plumber Sculpture", "Omsk", 54.985315, 73.374481),
))

# 14) Пожарная каланча ------------------------------------------------------------
RECORDS.append(rec(
    "omsk-fire-tower",
    "Tháp cứu hỏa lịch sử Omsk (Ka-lan-cha)",
    "Пожарная каланча",
    "Historic Fire Watchtower (Omsk)",
    ["monument"],
    54.991362, 73.370735,
    "Phố Internatsionalnaya 41, trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Tháp canh cứu hỏa bằng gạch đầu thế kỷ 20, một di tích kiến trúc và biểu tượng đô thị của Omsk. Trên đỉnh tháp có mô hình người lính cứu hỏa 'Стёпаныч' đang đứng gác, tạo nét sinh động độc đáo.",
    "Tháp cứu hỏa Omsk (Пожарная каланча) là một di tích kiến trúc đặc sắc ở trung tâm thành phố, được xây dựng năm 1915 theo thiết kế của kiến trúc sư I. G. Khvorinov - cũng chính là người thiết kế toà nhà Nhà hát Kịch. Toà tháp gạch đỏ cao khoảng 30 mét vươn lên trên nền phố, phía đỉnh là chòi quan sát bằng gỗ nơi lính cứu hỏa xưa đứng gác để phát hiện đám cháy trong thành phố gỗ dễ bén lửa. Với kiến trúc gạch trang trí duyên dáng, tháp từ lâu đã trở thành một điểm nhận diện quen thuộc và biểu tượng của Omsk. Ngày nay, trên ban công đỉnh tháp có đặt một mô hình người lính cứu hỏa (được người dân gọi thân mật là 'Стёпаныч') trong tư thế đang canh gác, khiến toà tháp thêm sinh động và thu hút du khách chụp ảnh. Đây là một điểm dừng thú vị khi dạo khu trung tâm, vừa chiêm ngưỡng di sản kiến trúc, vừa hình dung công việc phòng cháy của một đô thị Siberia đầu thế kỷ 20.",
    [
        "Tháp cứu hỏa gạch đỏ năm 1915 do kiến trúc sư Khvorinov thiết kế - biểu tượng đô thị Omsk.",
        "Chòi quan sát bằng gỗ trên đỉnh, cao khoảng 30 mét.",
        "Mô hình lính cứu hỏa 'Стёпаныч' đứng gác trên ban công đỉnh tháp, điểm chụp ảnh độc đáo.",
    ],
    p("Là công trình đô thị, ngắm từ bên ngoài tự do mọi lúc (bên trong thường không mở cho khách).",
      "Miễn phí (ngắm bên ngoài).",
      "Khoảng 15 phút.",
      "Quanh năm; đẹp khi có nắng để chụp ảnh.",
      "Nằm ở trung tâm, dễ kết hợp với Quảng trường Nhà thờ và các điểm lân cận."),
    [
        {"title": "Wikipedia (RU) — Пожарная каланча (Омск)", "url": "https://ru.wikipedia.org/wiki/Пожарная_каланча_(Омск)"},
        {"title": "Gotoomsk.ru — Пожарная каланча", "url": "https://gotoomsk.ru/places/pozharnaya-kalancha/"},
    ],
    ["monument", "architecture", "landmark", "omsk", "history", "siberia"],
    maps_text("Пожарная каланча", "Омск", "Historic Fire Watchtower", "Omsk", 54.991362, 73.370735),
))

# 15) Памятник Ф. М. Достоевскому -------------------------------------------------
RECORDS.append(rec(
    "dostoevsky-monument-omsk",
    "Tượng đài văn hào F. M. Dostoevsky (Đa-xtôi-ep-xki)",
    "Памятник Ф. М. Достоевскому",
    "Monument to F. M. Dostoevsky (Omsk)",
    ["monument"],
    54.985128, 73.367876,
    "Gần Quảng trường Nhà thờ và khu Pháo đài Omsk, trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Tượng đài tưởng nhớ văn hào Fyodor Dostoevsky - người từng chịu án khổ sai bốn năm tại pháo đài Omsk. Bức tượng khắc hoạ nhà văn trong dáng trầm tư, gắn với một trang đời và văn học đặc biệt của thành phố.",
    "Tượng đài Fyodor Mikhailovich Dostoevsky là một trong những đài tưởng niệm mang ý nghĩa văn học sâu sắc nhất Omsk. Thành phố có mối liên hệ đặc biệt với văn hào: từ năm 1850 đến 1854, Dostoevsky đã thụ án khổ sai bốn năm tại nhà tù trong pháo đài Omsk - trải nghiệm đau thương nhưng hằn sâu, về sau kết tinh thành kiệt tác 'Bút ký từ ngôi nhà chết'. Để tưởng nhớ giai đoạn ấy và tôn vinh nhà văn, thành phố dựng tượng đài khắc hoạ Dostoevsky trong dáng vẻ trầm tư, khắc khổ, đặt gần khu pháo đài lịch sử và Quảng trường Nhà thờ - chính nơi ông từng sống những ngày tù đày. Bức tượng trở thành điểm dừng ý nghĩa cho những người yêu văn học Nga và cho du khách muốn hiểu lát cắt tinh thần của Omsk. Cùng với Bảo tàng Văn học mang tên Dostoevsky và Cổng Tara ngay gần đó, tượng đài tạo nên một 'cụm ký ức Dostoevsky' đáng để dành thời gian khám phá trong hành trình tham quan trung tâm cũ của thành phố.",
    [
        "Tưởng nhớ Dostoevsky - người chịu án khổ sai bốn năm (1850–1854) tại pháo đài Omsk.",
        "Bức tượng khắc hoạ nhà văn trong dáng trầm tư, đặt gần pháo đài lịch sử.",
        "Nằm trong 'cụm ký ức Dostoevsky' cùng bảo tàng văn học và Cổng Tara.",
    ],
    p("Không gian ngoài trời, tham quan tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Quanh năm.",
      "Kết hợp tham quan Bảo tàng Văn học Dostoevsky, Pháo đài Omsk và Cổng Tara gần đó."),
    [
        {"title": "Gotoomsk.ru — Памятник Достоевскому", "url": "https://gotoomsk.ru/places/pamyatnik-dostoevskomu/"},
        {"title": "Wikipedia (RU) — Достоевский в Омске", "url": "https://ru.wikipedia.org/wiki/Достоевский,_Фёдор_Михайлович"},
    ],
    ["monument", "dostoevsky", "literature", "omsk", "history", "siberia"],
    maps_text("Памятник Достоевскому", "Омск", "Monument to Dostoevsky", "Omsk", 54.985128, 73.367876),
))

# 16) Город Тара ------------------------------------------------------------------
RECORDS.append(rec(
    "tara-town",
    "Thành phố cổ Tara (Ta-ra)",
    "Город Тара",
    "Tara (Historic Town)",
    ["monument", "square_street"],
    56.902500, 74.370833,
    "Thành phố Tara, huyện Tarsky, tỉnh Omsk, Nga (cách Omsk khoảng 300 km về phía bắc)",
    "Thành phố cổ nhất tỉnh Omsk, lập năm 1594, từng là tiền đồn quan trọng trên đường mở đất Siberia. Trung tâm Tara còn giữ nhiều nhà gỗ, nhà thương gia và nhà thờ cổ, mang đậm không khí lịch sử.",
    "Tara là thành phố lâu đời nhất tỉnh Omsk và là một trong những đô thị cổ của Siberia, được thành lập năm 1594 theo lệnh Sa hoàng như một pháo đài trấn giữ và bàn đạp mở rộng lãnh thổ về phía đông. Ra đời sớm hơn cả Omsk hơn một thế kỷ, Tara từng là trung tâm hành chính, quân sự và thương mại sầm uất trên tuyến giao thương Siberia, nơi hội tụ thương nhân Nga, Bukhara và nhiều dân tộc. Ngày nay, thành phố nhỏ bên sông Irtysh này vẫn lưu giữ một trung tâm lịch sử giàu sức gợi: những dãy nhà gỗ chạm trổ, dinh thự thương gia bằng gạch, nhà thờ cổ và các quảng trường yên tĩnh. Điểm nhấn là Nhà thờ Chính tòa Spassky - công trình đá cổ nhất còn lại của cả tỉnh. Tara cũng có bảo tàng địa phương học và nhiều tượng đài gắn với lịch sử khai hoang. Với du khách ưa khám phá và hoài cổ, chuyến đi xa lên Tara là dịp chạm vào cội nguồn hình thành vùng đất Omsk, trong một không gian tỉnh lẻ trầm mặc, hiếm bóng du khách.",
    [
        "Thành phố cổ nhất tỉnh Omsk (lập năm 1594), có trước Omsk hơn một thế kỷ.",
        "Trung tâm lịch sử với nhà gỗ chạm trổ, dinh thự thương gia và nhà thờ cổ.",
        "Gắn với lịch sử khai hoang Siberia và tuyến giao thương xưa bên sông Irtysh.",
    ],
    p("Là đô thị nên tham quan tự do; các bảo tàng, nhà thờ có giờ mở riêng (thường ban ngày).",
      "Dạo phố miễn phí; vé vào bảo tàng và một số điểm ở mức thấp.",
      "Khoảng nửa ngày tại Tara; tính cả di chuyển nên dành trọn 1–2 ngày.",
      "Cuối xuân đến đầu thu cho đường đi và thời tiết thuận lợi.",
      "Cách Omsk khoảng 300 km về phía bắc; nên đi ô tô hoặc xe khách. Kết hợp thăm Nhà thờ Spassky và bảo tàng địa phương."),
    [
        {"title": "Wikipedia (RU) — Тара (город)", "url": "https://ru.wikipedia.org/wiki/Тара_(город)"},
        {"title": "Gotoomsk.ru — Город Тара", "url": "https://gotoomsk.ru/places/gorod-tara/"},
    ],
    ["monument", "square-street", "historic-town", "tara", "history", "siberia"],
    maps_text("Город Тара", "Тара", "Tara town", "Tara", 56.902500, 74.370833),
))

# ============================ DINH THỰ (palace) ============================

# 17) Особняк Батюшкина (Дом Колчака) ---------------------------------------------
RECORDS.append(rec(
    "kolchak-mansion-batyushkin",
    "Biệt thự thương gia Batyushkin ('Nhà Kolchak' - Côn-trắc)",
    "Особняк Батюшкина (Дом Колчака)",
    "Batyushkin Mansion (Kolchak's House)",
    ["palace"],
    54.979097, 73.374248,
    "Phố Irtyshskaya naberezhnaya 9, ven sông Irtysh, thành phố Omsk, tỉnh Omsk, Nga",
    "Biệt thự thương gia đầu thế kỷ 20 duyên dáng bên bờ sông Irtysh, nổi tiếng vì từng là dinh của Đô đốc Kolchak - 'Lãnh tụ Tối cao' của phong trào Bạch vệ. Một địa chỉ lịch sử gắn với thời Nội chiến Nga.",
    "Biệt thự Batyushkin là một trong những dinh thự thương gia đẹp nhất còn lại của Omsk, xây năm 1902 theo đơn đặt của thương nhân Kapiton Batyushkin, bên bờ kè sông Irtysh. Công trình gạch trang nhã với những chi tiết trang trí tinh tế phản ánh gu thẩm mỹ và sự thịnh vượng của giới thương gia Omsk đầu thế kỷ 20. Ngôi nhà đi vào lịch sử khi trong thời Nội chiến (1918–1919), Omsk trở thành 'thủ đô' của chính phủ Bạch vệ và biệt thự này được chọn làm dinh của Đô đốc Aleksandr Kolchak - người được phong 'Lãnh tụ Tối cao nước Nga'. Tại đây từng xảy ra một vụ mưu sát bằng thuốc nổ nhằm vào Kolchak, khiến toà nhà hư hại và về sau được tu sửa. Trải qua thế kỷ 20, ngôi nhà được dùng vào nhiều mục đích khác nhau; hiện nay là trụ sở của một cơ quan hộ tịch và có không gian trưng bày nhỏ liên quan tới lịch sử. Với du khách quan tâm đến giai đoạn Nội chiến Nga và số phận Omsk, đây là một địa chỉ giàu câu chuyện, đồng thời là mẫu kiến trúc thương gia đáng chiêm ngưỡng bên dòng Irtysh.",
    [
        "Biệt thự thương gia năm 1902 bên bờ sông Irtysh, kiến trúc gạch trang nhã.",
        "Từng là dinh của Đô đốc Kolchak - 'Lãnh tụ Tối cao' phong trào Bạch vệ thời Nội chiến.",
        "Gắn với vụ mưu sát bằng thuốc nổ nhằm vào Kolchak; nay có không gian trưng bày nhỏ.",
    ],
    p("Ngắm bên ngoài tự do mọi lúc; bên trong tuỳ chức năng hiện tại và không gian trưng bày (giờ hành chính).",
      "Ngắm bên ngoài miễn phí; tham quan trưng bày (nếu có) mức phí thấp.",
      "Khoảng 20–30 phút.",
      "Cuối xuân đến đầu thu; đẹp khi dạo bờ kè Irtysh.",
      "Kết hợp dạo bờ kè sông Irtysh và phố Chokan Valikhanov gần đó; hỏi trước nếu muốn vào bên trong."),
    [
        {"title": "Gotoomsk.ru — Особняк Батюшкина (Дом Колчака)", "url": "https://gotoomsk.ru/places/osobnyak-batyushkina/"},
        {"title": "Wikipedia (RU) — Особняк Батюшкина", "url": "https://ru.wikipedia.org/wiki/Особняк_Батюшкина"},
    ],
    ["palace", "mansion", "history", "kolchak", "omsk", "architecture"],
    maps_text("Особняк Батюшкина Дом Колчака", "Омск", "Batyushkin Mansion Kolchak House", "Omsk", 54.979097, 73.374248),
))

# ============================ NHÀ THỜ / CÔNG TRÌNH TÔN GIÁO (church) ============================

# 18) Свято-Никольский казачий собор ----------------------------------------------
RECORDS.append(rec(
    "nikolsky-cossack-cathedral",
    "Nhà thờ Chính tòa Cossack Thánh Nikolai (Ni-côn-xki)",
    "Свято-Никольский казачий собор",
    "St. Nicholas Cossack Cathedral",
    ["church"],
    54.977597, 73.379545,
    "Phố Lenina 27, trung tâm thành phố Omsk, tỉnh Omsk, Nga",
    "Ngôi nhà thờ cổ nhất còn tồn tại của Omsk, khởi công năm 1833, gắn bó mật thiết với cộng đồng Cossack Siberia. Đây là nhà thờ quân đội duy nhất sống sót qua thời Xô Viết và là một di sản đặc biệt.",
    "Nhà thờ Chính tòa Cossack Thánh Nikolai là ngôi thánh đường cổ nhất còn tồn tại ở Omsk, được khởi công năm 1833 và hoàn thành năm 1840 theo thiết kế mang phong cách cổ điển gắn với tên tuổi kiến trúc sư danh tiếng Vasily Stasov. Ngay từ đầu, nhà thờ đã là ngôi đền quân đội của Đội quân Cossack Siberia và giữ vai trò trung tâm tâm linh của cộng đồng Cossack vùng Prииртышье. Nơi đây từng lưu giữ lá cờ (знамя) thiêng của quân đoàn Ermak Timofeevich - thủ lĩnh Cossack huyền thoại mở đất Siberia. Qua thời Xô Viết, khi hàng loạt nhà thờ ở Omsk bị phá hủy, đây là ngôi nhà thờ quân đội hiếm hoi còn trụ lại (dù từng bị đóng cửa và dùng vào việc khác), rồi được trả về cho giáo hội và phục hồi. Ngày nay, với mặt tiền cổ điển thanh thoát và bầu không khí trang nghiêm, nhà thờ là điểm hành hương, sinh hoạt tôn giáo và cũng là một di tích lịch sử - kiến trúc quan trọng ngay trung tâm phố Lenin. Du khách có thể ghé chiêm bái và tìm hiểu về di sản Cossack đặc sắc của vùng đất Omsk.",
    [
        "Ngôi nhà thờ cổ nhất còn tồn tại của Omsk (khởi công 1833), phong cách cổ điển.",
        "Đền quân đội của Đội quân Cossack Siberia; từng lưu giữ cờ thiêng của Ermak.",
        "Nhà thờ quân đội hiếm hoi sống sót qua thời Xô Viết, nay là di tích lịch sử - kiến trúc.",
    ],
    p("Mở cửa hằng ngày, thường khoảng 8:00–19:00; có các buổi lễ sáng và chiều.",
      "Vào cửa miễn phí; có thể quyên góp tùy tâm hoặc mua nến, đồ lưu niệm.",
      "Khoảng 20–30 phút.",
      "Buổi sáng khi có lễ; các đại lễ Chính Thống giáo không khí trang nghiêm.",
      "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu; giữ yên lặng khi có buổi lễ. Nằm ngay phố Lenin trung tâm."),
    [
        {"title": "Wikipedia (RU) — Никольский казачий собор (Омск)", "url": "https://ru.wikipedia.org/wiki/Никольский_казачий_собор_(Омск)"},
        {"title": "Sobory.ru — Собор Николая Чудотворца (Омск)", "url": "https://sobory.ru/geo/?ll=73.379545,54.977597"},
    ],
    ["church", "orthodox", "cathedral", "cossack", "omsk", "history"],
    maps_org("https://yandex.com/maps/org/svyato_nikolskiy_kazachiy_sobor/1023263094/", "St. Nicholas Cossack Cathedral", "Omsk"),
))

# 19) Крестовоздвиженский собор ---------------------------------------------------
RECORDS.append(rec(
    "exaltation-cross-cathedral-omsk",
    "Nhà thờ Chính tòa Nâng Cao Thánh Giá (Krê-xtô-vốt-vi-gien-xki)",
    "Крестовоздвиженский собор",
    "Exaltation of the Cross Cathedral (Omsk)",
    ["church"],
    54.997101, 73.368695,
    "Phố Tarskaya 33, thành phố Omsk, tỉnh Omsk, Nga",
    "Nhà thờ Chính Thống giáo giữa thế kỷ 19, một trong số ít thánh đường của Omsk còn hoạt động liên tục qua thời Xô Viết. Đây từng giữ vai trò nhà thờ chính tòa của thành phố trong nhiều thập kỷ.",
    "Nhà thờ Chính tòa Nâng Cao Thánh Giá (Крестовоздвиженский собор) là một trong những thánh đường Chính Thống giáo quan trọng và giàu ý nghĩa của Omsk. Được xây dựng vào giữa thế kỷ 19 (khánh thành năm 1870) bằng nguồn quyên góp của thị dân, nhà thờ mang phong cách kiến trúc Nga truyền thống với mặt tiền vàng ấm và các mái vòm hành củ. Điều đặc biệt là trong suốt thời kỳ Xô Viết đầy khắc nghiệt với tôn giáo, đây là một trong rất ít nhà thờ của Omsk không bị phá hủy và có những giai đoạn vẫn duy trì hoạt động; nhờ đó, trong nhiều thập kỷ, Крестовоздвиженский собор thực tế đảm nhận vai trò nhà thờ chính tòa của thành phố, là nơi gìn giữ đời sống đức tin Chính Thống giáo của người dân Omsk. Bên trong lưu giữ nhiều tranh thánh và thánh tích được tín đồ tôn kính. Ngày nay, khi thành phố đã có Nhà thờ Đức Mẹ An Giấc phục dựng, Крестовоздвиженский собор vẫn là một trung tâm tôn giáo sống động và một di tích lịch sử - tâm linh đáng ghé thăm ở khu phố Tarskaya.",
    [
        "Nhà thờ Chính Thống giáo giữa thế kỷ 19 (khánh thành 1870), phong cách Nga truyền thống.",
        "Một trong số ít thánh đường Omsk không bị phá hủy thời Xô Viết.",
        "Từng giữ vai trò nhà thờ chính tòa của thành phố trong nhiều thập kỷ.",
    ],
    p("Mở cửa hằng ngày, thường khoảng 8:00–19:00; có các buổi lễ sáng và chiều.",
      "Vào cửa miễn phí; có thể quyên góp tùy tâm hoặc mua nến.",
      "Khoảng 20–30 phút.",
      "Buổi sáng khi có lễ; các đại lễ Chính Thống giáo giàu không khí.",
      "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu; giữ yên lặng khi có buổi lễ đang diễn ra."),
    [
        {"title": "Wikipedia (RU) — Крестовоздвиженский собор (Омск)", "url": "https://ru.wikipedia.org/wiki/Крестовоздвиженский_собор_(Омск)"},
        {"title": "Sobory.ru — Крестовоздвиженский собор (Омск)", "url": "https://sobory.ru/geo/?ll=73.368695,54.997101"},
    ],
    ["church", "orthodox", "cathedral", "omsk", "history", "siberia"],
    maps_text("Крестовоздвиженский собор", "Омск", "Exaltation of the Cross Cathedral", "Omsk", 54.997101, 73.368695),
))

# 20) Соборная мечеть (Омск) ------------------------------------------------------
RECORDS.append(rec(
    "omsk-cathedral-mosque",
    "Thánh đường Hồi giáo Trung tâm Omsk (Xô-boóc-nai-a mê-tréc)",
    "Соборная мечеть",
    "Omsk Cathedral Mosque",
    ["church"],
    54.985190, 73.423691,
    "Phố 20-ya liniya 102, thành phố Omsk, tỉnh Omsk, Nga",
    "Thánh đường Hồi giáo chính của Omsk, trung tâm tinh thần của cộng đồng Hồi giáo Siberia. Ngôi đền với tháp minaret cao vút và mái vòm là biểu tượng cho sự đa dạng tôn giáo của vùng đất bên sông Irtysh.",
    "Thánh đường Hồi giáo Trung tâm Omsk (Соборная мечеть) là ngôi đền Hồi giáo chính và là trái tim tinh thần của cộng đồng người Hồi giáo (chủ yếu là người Tatar, Kazakh và các dân tộc khác) ở Omsk và cả vùng Siberia. Vùng đất Omsk có truyền thống chung sống lâu đời giữa Chính Thống giáo và Hồi giáo, và ngôi thánh đường này là biểu tượng nổi bật cho bức tranh đa văn hoá, đa tôn giáo ấy. Công trình mang kiến trúc Hồi giáo đặc trưng với tháp minaret cao vươn lên bầu trời, mái vòm và những chi tiết trang trí phương Đông tinh tế; đây cũng là nơi đặt trụ sở của cơ quan quản lý tôn giáo Hồi giáo khu vực. Bên cạnh chức năng thờ phụng và tổ chức các nghi lễ, lễ hội Hồi giáo (như Eid), thánh đường còn là trung tâm giáo dục và sinh hoạt cộng đồng. Với du khách, ghé thăm bên ngoài ngôi đền là dịp cảm nhận sự phong phú về tín ngưỡng của Omsk; khi vào bên trong cần tôn trọng các quy tắc trang phục và ứng xử trong không gian thờ tự Hồi giáo.",
    [
        "Thánh đường Hồi giáo chính của Omsk, trung tâm tinh thần của cộng đồng Hồi giáo Siberia.",
        "Kiến trúc Hồi giáo đặc trưng với tháp minaret cao và mái vòm trang trí phương Đông.",
        "Biểu tượng cho bức tranh đa văn hoá, đa tôn giáo của vùng đất bên sông Irtysh.",
    ],
    p("Mở cửa cho tín đồ hằng ngày theo giờ lễ nguyện; khách tham quan nên đến ngoài giờ cầu nguyện.",
      "Vào cửa miễn phí; có thể quyên góp tùy tâm.",
      "Khoảng 20–30 phút.",
      "Quanh năm; các dịp lễ Hồi giáo (Eid) không khí đặc biệt.",
      "Ăn mặc kín đáo, nữ nên trùm khăn; cởi giày khi vào khu cầu nguyện và tôn trọng nghi thức. Nên hỏi phép trước khi chụp ảnh bên trong."),
    [
        {"title": "Gotoomsk.ru — Соборная мечеть Омска", "url": "https://gotoomsk.ru/places/sobornaya-mechet/"},
        {"title": "Culttourism.ru — Соборная мечеть (Омск)", "url": "https://culttourism.ru/omskaya/omsk/"},
    ],
    ["church", "mosque", "islam", "religion", "omsk", "siberia"],
    maps_text("Соборная мечеть", "Омск", "Omsk Cathedral Mosque", "Omsk", 54.985190, 73.423691),
))

# 21) Христорождественский собор --------------------------------------------------
RECORDS.append(rec(
    "nativity-cathedral-omsk",
    "Nhà thờ Chính tòa Chúa Giáng Sinh (Khri-xtô-rốt-đê-xtven-xki)",
    "Христорождественский собор",
    "Cathedral of the Nativity of Christ (Omsk)",
    ["church"],
    54.994118, 73.290782,
    "Phố Stepantsa 5, khu Kristall (tả ngạn Irtysh), thành phố Omsk, tỉnh Omsk, Nga",
    "Nhà thờ Chính Thống giáo hiện đại lớn ở tả ngạn sông Irtysh, xây dựng cuối thế kỷ 20 - đầu thế kỷ 21. Ngôi thánh đường trắng với mái vòm vàng là trung tâm tâm linh nổi bật của các khu dân cư phía tây Omsk.",
    "Nhà thờ Chính tòa Chúa Giáng Sinh (Христорождественский собор) là một trong những thánh đường Chính Thống giáo lớn và nổi bật của Omsk hiện đại, phục vụ cộng đồng dân cư đông đúc ở tả ngạn (bờ trái) sông Irtysh - khu vực phát triển mạnh trong thời kỳ Xô Viết và hậu Xô Viết vốn thiếu vắng nhà thờ. Được xây dựng vào những năm cuối thế kỷ 20 - đầu thế kỷ 21, nhà thờ mang phong cách kiến trúc Chính Thống giáo truyền thống với khối tường trắng, nhiều mái vòm hành củ dát vàng và tháp chuông, nổi bật giữa cảnh quan đô thị hiện đại. Đây là một 'nhà thờ mới' tiêu biểu cho làn sóng phục hưng đời sống tôn giáo ở nước Nga sau thời Xô Viết. Bên cạnh chức năng thờ phụng và tổ chức các buổi lễ, nhà thờ còn có hoạt động giáo dục, từ thiện và sinh hoạt cộng đồng. Với du khách, ngôi thánh đường là điểm nhấn kiến trúc dễ nhận ra khi khám phá phần thành phố ở bờ trái Irtysh, đồng thời cho thấy sức sống của đức tin Chính Thống giáo trong đô thị Omsk đương đại.",
    [
        "Nhà thờ Chính Thống giáo hiện đại lớn ở tả ngạn sông Irtysh (xây cuối TK20 - đầu TK21).",
        "Khối tường trắng với nhiều mái vòm hành củ dát vàng, nổi bật giữa đô thị hiện đại.",
        "Tiêu biểu cho làn sóng phục hưng đời sống tôn giáo ở Nga sau thời Xô Viết.",
    ],
    p("Mở cửa hằng ngày, thường khoảng 8:00–19:00; có các buổi lễ sáng và chiều.",
      "Vào cửa miễn phí; có thể quyên góp tùy tâm hoặc mua nến.",
      "Khoảng 20–30 phút.",
      "Buổi sáng khi có lễ; các đại lễ Chính Thống giáo (đặc biệt Giáng sinh) giàu không khí.",
      "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu; nằm ở bờ trái Irtysh, nên đi ô tô hoặc xe buýt."),
    [
        {"title": "Sobory.ru — Христорождественский собор (Омск)", "url": "https://sobory.ru/geo/?ll=73.290782,54.994118"},
        {"title": "Gotoomsk.ru — Христорождественский собор", "url": "https://gotoomsk.ru/places/hristorozhdestvenskij-sobor/"},
    ],
    ["church", "orthodox", "cathedral", "omsk", "modern", "siberia"],
    maps_text("Христорождественский собор", "Омск", "Cathedral of the Nativity of Christ", "Omsk", 54.994118, 73.290782),
))

# 22) Спасский кафедральный собор (Тара) ------------------------------------------
RECORDS.append(rec(
    "spassky-cathedral-tara",
    "Nhà thờ Chính tòa Đấng Cứu Thế ở Tara (Xpát-xki xô-bo)",
    "Спасский кафедральный собор (Тара)",
    "Spassky (Saviour) Cathedral in Tara",
    ["church"],
    56.896424, 74.383503,
    "Thành phố Tara, huyện Tarsky, tỉnh Omsk, Nga (cách Omsk khoảng 300 km về phía bắc)",
    "Nhà thờ đá cổ nhất còn tồn tại của cả tỉnh Omsk, xây giữa thế kỷ 18 tại thành phố cổ Tara. Ngôi thánh đường theo phong cách baroque Siberia là một di sản kiến trúc - tâm linh vô giá.",
    "Nhà thờ Chính tòa Đấng Cứu Thế (Спасский собор) ở thành phố Tara là công trình bằng đá cổ nhất còn lại của toàn tỉnh Omsk - một di sản kiến trúc đặc biệt quý giá. Được khởi công năm 1753 và hoàn thành năm 1776, nhà thờ mang phong cách baroque Siberia (сибирское барокко) với đường nét trang trí mềm mại, các mái vòm và tháp chuông đặc trưng, phản ánh trình độ xây dựng và đời sống tâm linh của Tara khi thành phố còn là trung tâm thương mại sầm uất trên tuyến giao thương Siberia. Trải qua gần ba thế kỷ với bao thăng trầm, kể cả thời Xô Viết khi bị đóng cửa và dùng vào việc khác, nhà thờ vẫn được gìn giữ, trùng tu và trả lại chức năng thờ phụng, nay là nhà thờ chính tòa của địa hạt. Với vẻ đẹp cổ kính hiếm có và giá trị lịch sử vượt trội, Спасский собор là điểm đến hàng đầu khi ghé thăm Tara, đồng thời là một trong những công trình đáng chiêm ngưỡng nhất của cả vùng Prииртышье đối với du khách yêu di sản và kiến trúc.",
    [
        "Công trình đá cổ nhất còn lại của cả tỉnh Omsk (xây 1753–1776).",
        "Phong cách baroque Siberia với mái vòm và tháp chuông đặc trưng.",
        "Di sản kiến trúc - tâm linh quý giá ở thành phố cổ Tara.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–18:00.",
      "Vào cửa miễn phí; có thể quyên góp tùy tâm hoặc mua nến.",
      "Khoảng 30 phút.",
      "Cuối xuân đến đầu thu cho đường đi thuận lợi; các đại lễ Chính Thống giáo giàu không khí.",
      "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu. Cách Omsk khoảng 300 km; kết hợp tham quan trung tâm cổ Tara."),
    [
        {"title": "Sobory.ru — Спасский собор (Тара)", "url": "https://sobory.ru/article/?object=07876"},
        {"title": "Wikipedia (RU) — Спасская церковь (Тара)", "url": "https://ru.wikipedia.org/wiki/Спасская_церковь_(Тара)"},
    ],
    ["church", "orthodox", "cathedral", "baroque", "tara", "history"],
    maps_text("Спасский кафедральный собор Тара", "Тара", "Spassky Cathedral Tara", "Tara", 56.896424, 74.383503),
))

# ============================ CÔNG VIÊN / THIÊN NHIÊN (park_garden) ============================

# 23) Парк Победы -----------------------------------------------------------------
RECORDS.append(rec(
    "victory-park-omsk",
    "Công viên Chiến thắng (Pác Pa-bê-đư)",
    "Парк Победы",
    "Victory Park (Omsk)",
    ["park_garden"],
    54.963511, 73.360722,
    "Bên bờ sông Irtysh, khu Kirovsky (tả ngạn), thành phố Omsk, tỉnh Omsk, Nga",
    "Công viên tưởng niệm rộng lớn bên sông Irtysh, dành để vinh danh chiến thắng trong Chiến tranh Vệ quốc Vĩ đại. Nơi đây có đài tưởng niệm, khí tài quân sự trưng bày và không gian xanh cho gia đình dạo chơi.",
    "Công viên Chiến thắng (Парк Победы) là một trong những công viên tưởng niệm quan trọng và rộng lớn của Omsk, nằm bên bờ sông Irtysh. Được lập nên để vinh danh chiến thắng của nhân dân Liên Xô trong Chiến tranh Vệ quốc Vĩ đại (1941–1945), công viên kết hợp không gian tưởng niệm trang nghiêm với khu vực dạo chơi, nghỉ ngơi xanh mát. Trong khuôn viên có các đài tưởng niệm, tượng đài và khu trưng bày ngoài trời với khí tài quân sự như xe tăng, pháo và thiết bị thời chiến, tạo thành một 'bảo tàng ngoài trời' thu hút cả người lớn lẫn trẻ em. Vào ngày Chiến thắng 9/5 và các dịp lễ quốc gia, nơi đây diễn ra những nghi lễ, mít tinh, đặt vòng hoa và hoạt động cộng đồng đầy xúc động. Ngày thường, công viên là nơi người dân đi bộ, đạp xe, đưa trẻ dạo chơi và tận hưởng cảnh quan ven sông. Với du khách, đây vừa là điểm tìm hiểu ký ức chiến tranh và lòng tri ân của người Omsk, vừa là không gian thư giãn dễ chịu bên dòng Irtysh.",
    [
        "Công viên tưởng niệm Chiến tranh Vệ quốc Vĩ đại, bên bờ sông Irtysh.",
        "Khu trưng bày ngoài trời với xe tăng, pháo và khí tài quân sự - hấp dẫn trẻ em.",
        "Nơi diễn ra nghi lễ ngày Chiến thắng 9/5 và không gian dạo chơi ven sông.",
    ],
    p("Không gian mở, dạo chơi tự do mọi lúc; đẹp nhất ban ngày.",
      "Miễn phí.",
      "Khoảng 1–1,5 giờ.",
      "Cuối xuân đến đầu thu; đặc biệt dịp 9/5 (Ngày Chiến thắng).",
      "Giữ thái độ trang nghiêm ở khu tưởng niệm; nằm ở bờ trái Irtysh, tiện đi cùng gia đình."),
    [
        {"title": "Gotoomsk.ru — Парк Победы", "url": "https://gotoomsk.ru/places/park-pobedy/"},
        {"title": "Wikipedia (RU) — Омск", "url": "https://ru.wikipedia.org/wiki/Омск"},
    ],
    ["park", "memorial", "wwii", "military", "omsk", "family"],
    maps_text("Парк Победы", "Омск", "Victory Park", "Omsk", 54.963511, 73.360722),
))

# 24) Зелёный остров --------------------------------------------------------------
RECORDS.append(rec(
    "green-island-park-omsk",
    "Công viên 'Zelyony Ostrov' - Đảo Xanh (Dê-li-ô-nứi Ô-xtrốp)",
    "Парк культуры и отдыха «Зелёный остров»",
    "Zelyony Ostrov (Green Island) Park",
    ["park_garden"],
    55.003604, 73.338515,
    "Phố Starozagorodnaya Roshcha 10/3, khu Sovetsky, ven sông Irtysh, thành phố Omsk, tỉnh Omsk, Nga",
    "Công viên văn hóa - nghỉ ngơi trên dải đất ven sông Irtysh, thành lập năm 1985. Nơi đây có rừng cây, khu trò chơi, bến du thuyền và bãi tắm, là điểm thư giãn, vui chơi được người dân Omsk yêu thích.",
    "Công viên Văn hóa và Nghỉ ngơi 'Zelyony Ostrov' (Đảo Xanh) là một trong những khu vui chơi giải trí ngoài trời được yêu thích nhất của Omsk, nằm trên dải đất bên bờ phải sông Irtysh thuộc khu Sovetsky, được lập nên vào năm 1985. Đúng như tên gọi, công viên nổi bật với những cánh rừng cây rậm rạp và các lối mòn quanh co dành cho người thích dạo bộ, chạy bộ trong không gian yên tĩnh, tách khỏi ồn ào phố thị. Bên cạnh đó là khu trò chơi cảm giác mạnh và cầu trượt cho trẻ em, câu lạc bộ du thuyền, dịch vụ chèo thuyền, ca-nô và bãi tắm ven sông vào mùa hè; mùa đông, công viên biến thành nơi trượt băng, trượt tuyết. Nhiều quán cà phê, khu ăn uống và sân khấu ngoài trời cũng nằm trong khuôn viên, thường xuyên tổ chức lễ hội, hoà nhạc và sự kiện thành phố. Với sự pha trộn giữa thiên nhiên, mặt nước và các hoạt động giải trí, 'Zelyony Ostrov' là điểm đến lý tưởng cho gia đình và những ai muốn thư giãn, vận động giữa cảnh quan ven sông Irtysh.",
    [
        "Công viên văn hóa - nghỉ ngơi ven sông Irtysh (thành lập 1985) với rừng cây xanh mát.",
        "Khu trò chơi cảm giác mạnh, câu lạc bộ du thuyền, chèo thuyền và bãi tắm mùa hè.",
        "Mùa đông trượt băng, trượt tuyết; thường xuyên có lễ hội và sự kiện ngoài trời.",
    ],
    p("Không gian mở, dạo chơi tự do; các khu trò chơi và dịch vụ theo giờ (thường ban ngày, mùa ấm).",
      "Vào công viên miễn phí; các trò chơi, thuê thuyền, dịch vụ tính phí riêng.",
      "Khoảng 1,5–2,5 giờ.",
      "Mùa hè cho chèo thuyền, tắm sông và trò chơi; mùa đông cho trượt băng.",
      "Đi giày thoải mái; mang đồ bơi vào mùa hè nếu muốn tắm sông. Kiểm tra lịch sự kiện trước khi đến."),
    [
        {"title": "Gotoomsk.ru — Парк «Зелёный остров»", "url": "https://gotoomsk.ru/places/park-zelenyj-ostrov/"},
        {"title": "2GIS — Зелёный остров, парк культуры и отдыха", "url": "https://2gis.ru/omsk/firm/70000001022954632"},
    ],
    ["park", "nature", "recreation", "irtysh", "omsk", "family"],
    maps_text("Парк культуры и отдыха Зелёный остров", "Омск", "Zelyony Ostrov Green Island Park", "Omsk", 55.003604, 73.338515),
))

# 25) Большереченский зоопарк -----------------------------------------------------
RECORDS.append(rec(
    "bolsherechye-zoo",
    "Vườn thú Bolsherechye (Bôn-sê-rê-tren-xki da-ô-pác)",
    "Большереченский зоопарк имени В. Д. Соломатина",
    "Bolsherechye Zoo (named after V. D. Solomatin)",
    ["park_garden"],
    56.089631, 74.642267,
    "Làng đô thị Bolsherechye, huyện Bolsherechensky, tỉnh Omsk, Nga (cách Omsk khoảng 200 km về phía bắc)",
    "Vườn thú nông thôn duy nhất của nước Nga, nằm ở thị trấn nhỏ Bolsherechye phía bắc Omsk. Nơi đây nuôi giữ hàng trăm loài động vật, từ thú Siberia bản địa đến các loài ngoại lai, giữa khung cảnh làng quê.",
    "Vườn thú Bolsherechye là một hiện tượng độc đáo: đây là vườn thú cấp nhà nước duy nhất của nước Nga nằm ở một làng/thị trấn nông thôn, chứ không phải trong một đô thị lớn. Hình thành từ giữa thế kỷ 20 và mang tên nhà sáng lập V. D. Solomatin, vườn thú nằm bên bờ sông Bolsheretka ở thị trấn Bolsherechye, cách Omsk khoảng 200 km về phía bắc. Bất chấp vị trí xa xôi và quy mô của một thị trấn nhỏ, nơi đây nuôi giữ một bộ sưu tập động vật phong phú đến bất ngờ - hàng trăm loài gồm cả thú, chim, bò sát bản địa Siberia lẫn nhiều loài ngoại lai như hổ, sư tử, gấu, khỉ, đà điểu và các loài quý hiếm. Vườn thú tham gia các chương trình bảo tồn, nhân giống động vật và giáo dục môi trường, đồng thời là niềm tự hào của cả vùng. Kết hợp với khu phức hợp 'Starina Sibirskaya' ngay gần đó, Bolsherechye trở thành điểm đến cuối tuần lý tưởng cho gia đình: vừa ngắm động vật, vừa khám phá văn hoá làng Siberia trong một chuyến đi giàu trải nghiệm.",
    [
        "Vườn thú nông thôn cấp nhà nước DUY NHẤT của nước Nga.",
        "Hàng trăm loài động vật - từ thú Siberia bản địa đến hổ, sư tử, gấu, khỉ, đà điểu.",
        "Kết hợp thuận tiện với khu phức hợp làng cổ 'Starina Sibirskaya' kề bên.",
    ],
    p("Mở cửa hằng ngày, thường khoảng 9:00–19:00 mùa hè và ngắn hơn về mùa đông; nên kiểm tra trước.",
      "Vé vào cửa mức phải chăng; ưu đãi cho trẻ em, học sinh, sinh viên.",
      "Khoảng 1,5–2,5 giờ; tính cả di chuyển nên dành trọn một ngày.",
      "Mùa hè cho thời tiết đẹp và nhiều động vật hoạt động; cuối tuần đông vui.",
      "Cách Omsk khoảng 200 km; nên đi ô tô hoặc tour. Kết hợp tham quan 'Starina Sibirskaya' gần đó."),
    [
        {"title": "Wikipedia (RU) — Большереченский зоопарк", "url": "https://ru.wikipedia.org/wiki/Большереченский_зоопарк"},
        {"title": "Culture.ru — Большереченский зоопарк", "url": "https://www.culture.ru/institutes/12345/bolsherechenskii-zoopark"},
    ],
    ["park", "zoo", "wildlife", "family", "bolsherechye", "siberia"],
    maps_org("https://yandex.ru/maps/org/bolsherechenskiy_gosudarstvenny_zoopark_imeni_v_d_solomatina/35363208762/", "Bolsherechye Zoo", "Bolsherechye"),
))

# 26) Озеро Линёво («Пять озёр») --------------------------------------------------
RECORDS.append(rec(
    "linevo-lake-five-lakes",
    "Hồ Linyovo - cụm 'Năm Hồ' huyền thoại (Li-nhi-ô-vô)",
    "Озеро Линёво (система «Пять озёр»)",
    "Lake Linyovo (Five Lakes)",
    ["park_garden"],
    56.406900, 75.623900,
    "Huyện Muromtsevsky, tỉnh Omsk, Nga (cách Omsk khoảng 250 km về phía bắc, gần làng Muromtsevo)",
    "Hồ nước trong nằm giữa rừng thông ở phía bắc Omsk, thuộc cụm 'Năm Hồ' huyền thoại. Truyền thuyết kể các hồ hình thành từ thiên thạch và nước có khả năng chữa lành, thu hút đông du khách và người tìm sự tĩnh lặng.",
    "Hồ Linyovo là một trong những viên ngọc thiên nhiên nổi tiếng nhất tỉnh Omsk, nằm giữa rừng thông xanh mát ở huyện Muromtsevsky phía bắc, gần khu Muromtsevo được mệnh danh là vùng đất huyền bí của Siberia. Hồ thuộc cụm 'Năm Hồ' (Пять озёр) - gồm Linyovo, Danilovo, Shaitan, Urmannoye và một hồ ẩn danh trong truyền thuyết. Theo huyền thoại địa phương, các hồ này hình thành từ những mảnh thiên thạch rơi xuống hàng nghìn năm trước, và nước hồ được cho là có khả năng chữa lành - dù đặc tính 'kỳ diệu' ấy chưa được khoa học xác nhận. Hồ Linyovo trong vắt, sâu tới khoảng 11 mét, được bao quanh bởi rừng lá kim nhiều nấm và quả mọng, có bãi cắm trại, khu nghỉ dưỡng và bến tắm. Vào mùa hè, nơi đây thu hút đông đảo du khách đến bơi lội, câu cá, hái nấm và tận hưởng không khí trong lành. Với những ai tìm kiếm sự tĩnh lặng, thiên nhiên nguyên sơ và một chút màu sắc huyền thoại, chuyến đi lên 'Năm Hồ' là trải nghiệm khó quên ở vùng Siberia của Omsk.",
    [
        "Thuộc cụm 'Năm Hồ' (Пять озёр) huyền thoại giữa rừng thông phía bắc Omsk.",
        "Truyền thuyết về nguồn gốc thiên thạch và nước hồ 'chữa lành' (chưa được khoa học xác nhận).",
        "Hồ trong vắt sâu ~11 m, có khu nghỉ dưỡng, cắm trại, bơi lội và hái nấm quanh rừng.",
    ],
    p("Khu vực thiên nhiên mở, tham quan tự do; các khu nghỉ dưỡng, cắm trại có dịch vụ và phí riêng.",
      "Vào khu vực thường miễn phí; lưu trú, dịch vụ tại các cơ sở nghỉ dưỡng tính phí.",
      "Nên dành trọn 1–2 ngày (kể cả di chuyển và lưu trú).",
      "Mùa hè (tháng 6–8) cho bơi lội, cắm trại; đầu thu cho hái nấm và không khí trong lành.",
      "Cách Omsk khoảng 250 km; nên đi ô tô hoặc tour. Mang đồ chống muỗi, lều trại hoặc đặt cơ sở lưu trú trước."),
    [
        {"title": "Openarium.ru — Озеро Линёво", "url": "https://openarium.ru/poi/11651944/"},
        {"title": "OmskMap.ru — озеро Линёво (Муромцевский район)", "url": "http://www.omskmap.ru/point/ozero_linevo"},
    ],
    ["park", "nature", "lake", "five-lakes", "muromtsevo", "siberia"],
    maps_text("Озеро Линёво Пять озёр", "Муромцево", "Lake Linyovo Five Lakes", "Muromtsevo", 56.406900, 75.623900),
))

# 27) Озеро Эбейты ----------------------------------------------------------------
RECORDS.append(rec(
    "ebeyty-lake",
    "Hồ mặn Ebeyty (Ê-bây-tư)",
    "Озеро Эбейты",
    "Lake Ebeyty (salt lake)",
    ["park_garden"],
    54.644432, 71.737852,
    "Vùng ranh giới các huyện Moskalensky, Poltavsky và Isilkulsky, tỉnh Omsk, Nga (phía tây nam Omsk)",
    "Hồ mặn lớn nhất tỉnh Omsk, một di tích thiên nhiên cấp vùng với bùn khoáng và nước muối được cho là có tác dụng chữa bệnh. Cảnh quan hồ nước trắng muối giữa thảo nguyên tạo nên khung cảnh siêu thực.",
    "Hồ Ebeyty là hồ nước mặn lớn nhất của tỉnh Omsk và là một trong những di tích thiên nhiên (памятник природы) quan trọng nhất của vùng, nằm ở phía tây nam, nơi giáp ranh nhiều huyện giữa vùng thảo nguyên. Đây là một hồ tự nhiên khép kín, không có dòng chảy ra, khiến nước bốc hơi để lại độ mặn rất cao và một lớp muối, bùn khoáng dày dưới đáy. Bùn sulfua và nước muối đậm đặc của hồ từ lâu được người dân địa phương tin là có tác dụng chữa lành các bệnh về da, xương khớp, nên hồ có tiềm năng như một điểm điều dưỡng thiên nhiên. Vào những thời điểm nhất định trong năm, khi mực nước rút và muối kết tinh, mặt hồ và bờ hồ khoác lên sắc trắng hồng lấp lánh giữa thảo nguyên mênh mông, tạo nên khung cảnh siêu thực, độc đáo cho nhiếp ảnh. Do vị trí xa xôi và hạ tầng hạn chế, Ebeyty phù hợp với du khách ưa khám phá thiên nhiên hoang sơ; chuyến đi tới đây mang lại trải nghiệm về một cảnh quan hiếm gặp và giá trị sinh thái đặc biệt của vùng Omsk.",
    [
        "Hồ nước mặn lớn nhất tỉnh Omsk, di tích thiên nhiên cấp vùng.",
        "Bùn khoáng và nước muối được cho là có tác dụng chữa bệnh (điều dưỡng thiên nhiên).",
        "Cảnh quan mặt hồ trắng muối giữa thảo nguyên - khung cảnh siêu thực cho nhiếp ảnh.",
    ],
    p("Khu vực thiên nhiên hoang sơ, tham quan tự do; không có hạ tầng dịch vụ chính quy.",
      "Miễn phí.",
      "Nên dành trọn một ngày do khoảng cách xa.",
      "Cuối xuân đến cuối hè, khi thời tiết khô ráo và muối kết tinh rõ nét.",
      "Vị trí xa và đường khó; nên đi ô tô gầm cao, mang đủ nước, thức ăn và định vị GPS. Cẩn thận với bùn lún ven hồ."),
    [
        {"title": "Wikipedia (RU) — Эбейты", "url": "https://ru.wikipedia.org/wiki/Эбейты"},
        {"title": "OmskMap.ru — озеро Эбейты", "url": "http://www.omskmap.ru/point/ozero_ebeity"},
    ],
    ["park", "nature", "salt-lake", "healing-mud", "steppe", "siberia"],
    maps_text("Озеро Эбейты", "Омская область", "Lake Ebeyty salt lake", "Omsk Oblast", 54.644432, 71.737852),
))

# 28) Озеро Ульжай ----------------------------------------------------------------
RECORDS.append(rec(
    "ulzhay-lake",
    "Hồ khoáng Ulzhay (Un-giai)",
    "Озеро Ульжай",
    "Lake Ulzhay (mineral lake)",
    ["park_garden"],
    54.253161, 75.108634,
    "Huyện Cherlaksky, tỉnh Omsk, Nga (phía đông nam Omsk)",
    "Hồ mặn khoáng ở phía đông nam tỉnh Omsk, nổi tiếng với bùn sulfua chữa bệnh. Đây là một di tích thiên nhiên và điểm điều dưỡng dân gian giữa vùng thảo nguyên khô hạn.",
    "Hồ Ulzhay là một hồ nước mặn - khoáng nằm ở huyện Cherlaksky phía đông nam tỉnh Omsk, được xếp là di tích thiên nhiên (памятник природы) cấp vùng. Giống nhiều hồ khép kín của vùng thảo nguyên Nam Siberia, Ulzhay có độ khoáng hoá cao và tích tụ dưới đáy một lớp bùn sulfua đen đặc trưng. Từ lâu, người dân địa phương đã tìm đến hồ để dùng nước muối và bùn khoáng nhằm hỗ trợ điều trị các bệnh về da, cơ xương khớp và thần kinh, biến nơi đây thành một điểm điều dưỡng dân gian tự phát. Xung quanh hồ là cảnh quan thảo nguyên thoáng đãng đặc trưng của vùng biên giới phía nam Omsk. Do hạ tầng còn sơ khai, Ulzhay chủ yếu thu hút những du khách và người bệnh chủ động tìm đến vì mục đích chữa lành và trải nghiệm thiên nhiên, hơn là du lịch đại chúng. Chuyến đi tới hồ là dịp khám phá một mặt ít được biết đến của tỉnh Omsk: những hồ muối khoáng giàu giá trị y - sinh thái nằm rải rác giữa thảo nguyên rộng lớn.",
    [
        "Hồ mặn - khoáng ở phía đông nam Omsk, di tích thiên nhiên cấp vùng.",
        "Bùn sulfua và nước muối được dùng hỗ trợ chữa bệnh da, xương khớp (điều dưỡng dân gian).",
        "Cảnh quan thảo nguyên hoang sơ vùng biên giới phía nam tỉnh Omsk.",
    ],
    p("Khu vực thiên nhiên, tham quan tự do; hạ tầng dịch vụ hạn chế.",
      "Miễn phí.",
      "Nên dành trọn một ngày do khoảng cách xa.",
      "Mùa hè khô ráo (tháng 6–8) cho việc tắm bùn và di chuyển thuận lợi.",
      "Vị trí xa và đường khó; nên đi ô tô gầm cao, mang đủ nước và thức ăn. Tham khảo ý kiến y tế trước khi dùng bùn khoáng."),
    [
        {"title": "Wikipedia (RU) — Ульжай", "url": "https://ru.wikipedia.org/wiki/Ульжай"},
        {"title": "OmskMap.ru — озеро Ульжай (Черлакский район)", "url": "http://www.omskmap.ru/point/ozero_ulzhay"},
    ],
    ["park", "nature", "salt-lake", "healing-mud", "steppe", "siberia"],
    maps_text("Озеро Ульжай", "Черлак", "Lake Ulzhay mineral lake", "Cherlak", 54.253161, 75.108634),
))

# ============================ CẦU (bridge) ============================

# 29) Юбилейный мост --------------------------------------------------------------
RECORDS.append(rec(
    "yubileyny-bridge-omsk",
    "Cầu Yubileyny bắc qua sông Om (I-u-bi-lây-nứi)",
    "Юбилейный мост",
    "Yubileyny Bridge (over the Om River)",
    ["bridge"],
    54.982575, 73.376567,
    "Bắc qua sông Om, nối trung tâm lịch sử với phần thành phố phía nam, thành phố Omsk, tỉnh Omsk, Nga",
    "Cây cầu bắc qua sông Om ngay trung tâm Omsk, nối khu phố lịch sử với các quận phía nam. Từ cầu và bờ kè, du khách có thể ngắm dòng sông Om, đường chân trời thành phố và các mái vòm nhà thờ.",
    "Cầu Yubileyny (nghĩa là 'cầu Kỷ niệm') là một trong những cây cầu trung tâm bắc qua sông Om tại Omsk, nối khu trung tâm lịch sử ở khu vực Đại lộ Lyubinsky và Quảng trường Nhà thờ với phần thành phố ở bờ nam. Sông Om - con sông đã cho thành phố cái tên của mình - chảy qua trung tâm và đổ vào sông Irtysh ngay gần đó, nên những cây cầu như Yubileyny vừa là huyết mạch giao thông, vừa gắn bó mật thiết với cảnh quan và đời sống đô thị. Từ trên cầu và các bờ kè lân cận, du khách có thể phóng tầm mắt ngắm dòng Om, những công trình cổ ven sông, mái vòm nhà thờ và đường chân trời thành phố - một khung cảnh đặc biệt đẹp vào lúc hoàng hôn hay khi thành phố lên đèn. Khu vực quanh cầu, gần Đại lộ Lyubinsky và trung tâm, cũng là nơi người dân dạo bộ và nghỉ ngơi. Tuy là công trình giao thông, Yubileyny cùng cảnh sông Om tạo nên một điểm dừng chân dễ chịu, giúp du khách cảm nhận địa thế sông nước làm nên diện mạo của Omsk.",
    [
        "Cầu trung tâm bắc qua sông Om, nối khu phố lịch sử với phần thành phố phía nam.",
        "Điểm ngắm dòng sông Om, mái vòm nhà thờ và đường chân trời thành phố.",
        "Gần Đại lộ Lyubinsky và trung tâm - khu vực dạo bộ, nghỉ ngơi của người dân.",
    ],
    p("Không gian công cộng, qua lại và ngắm cảnh tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15–30 phút (kể cả dạo bờ kè).",
      "Mùa hè và mùa thu; đẹp lúc hoàng hôn và khi thành phố lên đèn.",
      "Kết hợp dạo Đại lộ Lyubinsky và Quảng trường Nhà thờ gần đó; chú ý an toàn giao thông khi chụp ảnh."),
    [
        {"title": "Gotoomsk.ru — Мосты Омска", "url": "https://gotoomsk.ru/places/mosty-omska/"},
        {"title": "Wikipedia (RU) — Омь (река)", "url": "https://ru.wikipedia.org/wiki/Омь"},
    ],
    ["bridge", "om-river", "cityscape", "omsk", "walking", "siberia"],
    maps_text("Юбилейный мост", "Омск", "Yubileyny Bridge over Om", "Omsk", 54.982575, 73.376567),
))

# 30) Метромост имени 60-летия Победы ---------------------------------------------
RECORDS.append(rec(
    "metro-bridge-60-let-pobedy",
    "Cầu Metro mang tên 60 năm Chiến thắng (Mê-trô-mốt)",
    "Метромост имени 60-летия Победы",
    "Metro Bridge named after the 60th Anniversary of Victory",
    ["bridge"],
    54.989739, 73.349304,
    "Bắc qua sông Irtysh, nối hai bờ thành phố Omsk, tỉnh Omsk, Nga",
    "Cây cầu hai tầng bắc qua sông Irtysh, khánh thành năm 2005 nhân 60 năm Chiến thắng. Nổi tiếng với nhà ga tàu điện ngầm 'Biblioteka imeni Pushkina' được xây sẵn nhưng chưa từng vận hành - biểu tượng của 'tàu điện ngầm không tồn tại'.",
    "Cầu Metro mang tên 60 năm Chiến thắng (Метромост им. 60-летия Победы) là một trong những cây cầu lớn và độc đáo nhất Omsk, bắc qua sông Irtysh và khánh thành năm 2005 đúng dịp kỷ niệm 60 năm Chiến thắng trong Chiến tranh Vệ quốc Vĩ đại. Cầu được thiết kế hai tầng: tầng trên cho ô tô, tầng dưới dự kiến dành cho tuyến tàu điện ngầm (metro) của Omsk. Câu chuyện đằng sau cây cầu đã trở thành một huyền thoại đô thị nổi tiếng cả nước: dự án metro Omsk kéo dài hàng chục năm nhưng không bao giờ hoàn thành, để lại một nhà ga duy nhất mang tên 'Thư viện Pushkin' (Библиотека имени Пушкина) được xây xong nhưng chưa từng đón một chuyến tàu nào - được ví von là 'nhà ga của đoàn tàu ma' hay 'metro ngắn nhất/không tồn tại nhất thế giới'. Chính nghịch lý này khiến cầu Metro và câu chuyện metro Omsk trở thành một 'điểm tham quan' mang màu sắc trớ trêu, thu hút sự tò mò của du khách. Từ cầu, du khách cũng có thể ngắm dòng Irtysh rộng lớn và toàn cảnh hai bờ thành phố.",
    [
        "Cầu hai tầng bắc qua sông Irtysh, khánh thành năm 2005 nhân 60 năm Chiến thắng.",
        "Gắn với 'metro không tồn tại' của Omsk và nhà ga 'Thư viện Pushkin' chưa từng vận hành.",
        "Điểm ngắm sông Irtysh và toàn cảnh hai bờ thành phố.",
    ],
    p("Không gian công cộng, qua lại và ngắm cảnh tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 15–20 phút.",
      "Mùa hè và mùa thu; đẹp lúc hoàng hôn bên sông Irtysh.",
      "Ngắm cảnh và tìm hiểu câu chuyện 'metro Omsk' độc đáo; chú ý an toàn giao thông khi chụp ảnh trên cầu."),
    [
        {"title": "Wikipedia (RU) — Метромост (Омск)", "url": "https://ru.wikipedia.org/wiki/Метромост_(Омск)"},
        {"title": "Gotoomsk.ru — Метромост им. 60-летия Победы", "url": "https://gotoomsk.ru/places/metromost/"},
    ],
    ["bridge", "irtysh", "metro", "cityscape", "omsk", "siberia"],
    maps_text("Метромост имени 60-летия Победы", "Омск", "Metro Bridge 60th Anniversary of Victory", "Omsk", 54.989739, 73.349304),
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
