# -*- coding: utf-8 -*-
"""_add_places_nizhny_novgorod_batch3_20260727.py — VÙNG TIÊU ĐIỂM: Tỉnh Nizhny Novgorod
(lần chạy tự động 2026-07-27, đợt 3).

Bối cảnh: nizhny-novgorod.json hiện có 45 địa điểm (sau đợt 1+2). Tatarstan đã đạt 60 (≥50)
=> vùng tiêu điểm vẫn là Nizhny Novgorod (đầu danh sách ưu tiên còn <50). Nâng dần tới ~50–100.

Đợt này bổ sung 13 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình:
- Nhà thờ cổ trung tâm: Рождества Иоанна Предтечи на Торгу (Minin kêu gọi dân 1611),
  Жён-Мироносиц (храм kiểu «корабль» đầu tiên ở Nga, 1649), Успенская на Ильинской горе
  (mái «крещатая бочка» độc nhất, 1672), Илии Пророка (Ильинская слобода).
- Tu viện: Оранский Богородицкий (1634), Городецкий Феодоровский (nơi Aleksandr Nevsky
  qua đời 1263), Амвросиев Николаевский Дудин (1408, bên vách sông Oka).
- Đài tưởng niệm: Памятник Минину и Пожарскому (bản sao của Tsereteli, 2005).
- Hiện đại/khác: Стадион «Нижний Новгород» (World Cup 2018, Стрелка), Нижегородский цирк.
- Thiên nhiên: Пустынские озёра (chuỗi hồ karst), Вадское озеро (voklina, không đóng băng).
- Điền trang: Усадьба Приклонских-Рукавишниковых в Подвязье (di sản liên bang bên sông Oka).

TOẠ ĐỘ: xác minh chéo sobory.ru (Успенская 56.32634,43.99016; Илии Пророка 56.32819,43.99357),
ru.wikipedia/svyatsy (Оранский 55.895119,43.716106; Феодоровский 56.646416,43.477505;
Дудин 56.181734,43.385054), Wikidata (цирк 56.3185,43.9530), tra cứu toạ độ điểm
(стадион 56.337626,43.962753; Иоанна Предтечи 56.329792,43.998142; Жён-Мироносиц
56.32412,43.99484; памятник Минину 56.32972,43.99667; Пустынские 55.668564,43.565210;
Вадское 55.5395,44.192; Подвязье 56.16534,43.34911) — 2026-07.
Kiểm tra thứ tự & phạm vi (tỉnh NN: lat ~54,5–58,1; lon ~41,5–47,0; KHÔNG đảo lat/lon; đều
nằm trong tỉnh). Link bản đồ TRỎ-ĐỊA-ĐIỂM: ưu tiên URL trang tổ chức Yandex khi tra được
(Феодоровский, цирк); còn lại text-search theo tên_ru + thành phố, canh giữa theo toạ độ đã kiểm.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_nizhny_novgorod_batch3_20260727.py
       python3 tools/normalize_categories.py && python3 tools/build.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"

REGION = "nizhny-novgorod"
REGION_NAME_VI = "Tỉnh Nizhny Novgorod"
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

# 1) Церковь Рождества Иоанна Предтечи на Торгу -------------------------------
RECORDS.append(rec(
    "ioann-predtecha-church",
    "Nhà thờ Giáng Sinh Thánh Gioan Tiền Hô «trên chợ» (Rozhdestva Ioanna Predtechi na Torgu)",
    "Церковь Рождества Иоанна Предтечи на Торгу",
    "Church of the Nativity of John the Baptist on the Torg",
    ["church", "monument"],
    56.329792, 43.998142,
    "Phố Rozhdestvenskaya, số 1Б, ngay dưới chân tháp Ivanovskaya của Kremlin, thành phố Nizhny Novgorod, Nga.",
    "Ngôi nhà thờ trắng đứng ngay dưới chân Kremlin bên bến sông cũ là một trong những thánh đường cổ nhất Nizhny Novgorod: nhà thờ đá được thánh hiến năm 1683. Theo truyền thống, chính từ bậc thềm nhà thờ (khi còn bằng gỗ) mà Kuzma Minin đã kêu gọi dân thành đứng lên lập đội dân binh giải phóng Moskva năm 1611.",
    "Nhà thờ Giáng Sinh Thánh Gioan Tiền Hô «trên chợ» nằm ở khu Hạ (Nizhny Posad), ngay dưới chân tháp Ivanovskaya của Kremlin, nơi xưa kia là khu chợ và bến sông sầm uất của Nizhny Novgorod. Một nhà thờ gỗ mang tên thánh Gioan Tiền Hô «ở chợ» cạnh cầu Ivanovsky đã được nhắc tới trong sổ điền bạ 1621–1622; đến năm 1683 ngôi nhà thờ đá hiện nay được thánh hiến. Công trình tiêu biểu cho lối kiến trúc khu phố buôn Nizhny với khối tứ diện bề thế, năm mái vòm và tháp chuông. Địa điểm gắn với một trong những trang sử hào hùng nhất của nước Nga: theo truyền thống, từ bậc thềm nhà thờ này, người bán thịt Kuzma Minin đã cất lời hiệu triệu dân Nizhny Novgorod góp của, góp người lập đội dân binh (cùng công tước Dmitry Pozharsky) tiến về giải phóng Moskva khỏi quân can thiệp Ba Lan năm 1611–1612. Ngày nay nhà thờ đã được trùng tu, sơn trắng nổi bật, là điểm dừng chân quen thuộc khi đi bộ từ phố Rozhdestvenskaya lên Kremlin, ngay cạnh tượng đài Minin và Pozharsky.",
    [
        "Một trong những nhà thờ cổ nhất thành phố (nhà thờ đá thánh hiến 1683), ngay chân Kremlin.",
        "Gắn truyền thống nơi Kuzma Minin kêu gọi lập đội dân binh cứu nước năm 1611.",
        "Kiến trúc khu phố buôn Nizhny với năm mái vòm; nằm cạnh tượng đài Minin–Pozharsky.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ, thường ban ngày; nên vào giờ hành lễ hoặc buổi sáng.",
        "ticket_vi": "Vào tự do (nơi thờ tự đang hoạt động).",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; đẹp nhất khi kết hợp đi bộ phố Rozhdestvenskaya lên Kremlin.",
        "tips_vi": "Ăn mặc lịch sự khi vào; kết hợp thăm tượng đài Minin–Pozharsky và phố cổ ngay bên cạnh.",
    },
    [
        {"title": "Wikipedia (RU) — Церковь Рождества Иоанна Предтечи на Торгу", "url": "https://ru.wikipedia.org/wiki/Церковь_Рождества_Иоанна_Предтечи_на_Торгу"},
        {"title": "sobory.ru — Церковь Рождества Иоанна Предтечи на Торгу (object 01403)", "url": "https://sobory.ru/article/?object=01403"},
    ],
    ["church", "minin", "1611", "old-town", "rozhdestvenskaya"],
    maps_text("Церковь Рождества Иоанна Предтечи на Торгу", "Нижний Новгород", "Church of the Nativity of John the Baptist on the Torg", "Nizhny Novgorod", 56.329792, 43.998142),
))

# 2) Церковь Жён-Мироносиц ----------------------------------------------------
RECORDS.append(rec(
    "zhyon-mironosits-church",
    "Nhà thờ các Bà Mang Mộc Dược (Zhyon-Mironosits)",
    "Церковь Жён-Мироносиц на Верхнем посаде",
    "Church of the Holy Myrrh-Bearers",
    ["church"],
    56.32412, 43.99484,
    "Phố Dobrolyubova, số 13, khu Verkhny Posad, thành phố Nizhny Novgorod, Nga.",
    "Nhà thờ các Bà Mang Mộc Dược (1649) là nhà thờ đá giáo xứ đầu tiên của khu Thượng (Verkhny Posad) và được coi là ngôi thánh đường kiểu «con thuyền» (korabl) đầu tiên trong lịch sử kiến trúc Nga – bố cục thẳng trục gồm cung thánh, gian cầu nguyện, phòng ăn và tháp chuông trên lối vào phía tây.",
    "Toạ lạc trên phố Dobrolyubova ở khu Thượng của Nizhny Novgorod, nhà thờ các Bà Mang Mộc Dược được xây năm 1649 và giữ một vị trí đặc biệt trong lịch sử kiến trúc Nga: đây là ngôi nhà thờ đầu tiên áp dụng bố cục kiểu «con thuyền» (храм типа «корабль») – tức cung thánh, gian cầu nguyện, phòng ăn (trapeznaya) và tháp chuông được sắp thẳng theo một trục từ đông sang tây, một sơ đồ về sau trở nên phổ biến khắp nước Nga. Nhà thờ cũng gắn với ký ức về hai vị thánh Nga được tôn kính có gốc gác từ giáo xứ này. Trải qua nhiều thăng trầm thời Xô Viết, công trình đã được phục hồi và hiện là nơi thờ tự đang hoạt động, một điểm đến bình yên cho những ai quan tâm tới kiến trúc nhà thờ cổ và lịch sử tôn giáo của thành phố.",
    [
        "Nhà thờ đá giáo xứ đầu tiên của khu Thượng, xây năm 1649.",
        "Được coi là thánh đường kiểu «con thuyền» (korabl) đầu tiên trong kiến trúc Nga.",
        "Gắn với ký ức hai vị thánh Nga xuất thân từ giáo xứ này.",
    ],
    {
        "hours_vi": "Mở theo giờ lễ, thường ban ngày; kiểm tra lịch hành lễ.",
        "ticket_vi": "Vào tự do (nơi thờ tự đang hoạt động).",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Kết hợp dạo khu phố cổ Verkhny Posad và các nhà thờ lân cận (Ilyinskaya, Uspenskaya).",
    },
    [
        {"title": "Wikipedia (RU) — Церковь Жён-Мироносиц на Верхнем посаде", "url": "https://ru.wikipedia.org/wiki/Церковь_Жён-Мироносиц_на_Верхнем_посаде"},
        {"title": "sobory.ru — Церковь Жён-мироносиц на Верхнем посаде (object 00918)", "url": "https://sobory.ru/article/?object=00918"},
    ],
    ["church", "1649", "korabl", "architecture", "old-town"],
    maps_text("Церковь Жён-Мироносиц", "Нижний Новгород", "Church of the Holy Myrrh-Bearers", "Nizhny Novgorod", 56.32412, 43.99484),
))

# 3) Успенская церковь на Ильинской горе --------------------------------------
RECORDS.append(rec(
    "uspenskaya-church-ilyinskaya",
    "Nhà thờ Đức Mẹ An Nghỉ trên đồi Ilyinskaya (Uspenskaya)",
    "Успенская церковь на Ильинской горе",
    "Church of the Dormition on Ilyinskaya Hill",
    ["church", "monument"],
    56.32634, 43.99016,
    "Ngõ Krutoy, số 3, khu Zapochainye/đồi Ilyinskaya, thành phố Nizhny Novgorod, Nga.",
    "Nhà thờ Đức Mẹ An Nghỉ (1672) do thương nhân Afanasy Olisov xây, là công trình đá độc nhất vô nhị của nước Nga có phần mái hình «thùng chữ thập bốn mặt» (крещатая бочка в четыре лица) – kiểu mái vốn chỉ thấy trong kiến trúc gỗ. Nhà thờ còn nổi tiếng với các mảng gạch men Balakhna thế kỷ 17.",
    "Nằm trên đồi Ilyinskaya ở khu Zapochainye cổ kính, nhà thờ Đức Mẹ An Nghỉ được thương nhân giàu có Afanasy Firsovich Olisov cho xây năm 1672 theo lời khấn nguyện. Điểm khiến công trình trở nên độc nhất trong lịch sử kiến trúc đá Nga là phần mái hình «thùng chữ thập bốn mặt» (крещатая бочка в четыре лица) – một hình thức mái phổ biến trong kiến trúc gỗ dân gian nhưng hầu như chỉ được dựng bằng đá duy nhất ở Nizhny Novgorod. Các tang trống của những mái vòm nhỏ được trang trí bằng gạch men nhiều màu (изразцы) kiểu Balakhna đặc trưng thế kỷ 17. Trải qua nhiều lần cải tạo, thậm chí suýt bị phá bỏ thời Xô Viết, công trình được cứu nhờ nỗ lực của kiến trúc sư và được trùng tu; năm 2004 phần phòng ăn và tháp chuông đã mất được dựng lại trong khuôn khổ dự án «Ilyinskaya Sloboda». Trước nhà thờ có bia tưởng niệm nhà phát minh Ivan Kulibin, người sinh ra gần đó. Đây là một trong những viên ngọc kiến trúc cổ ít người biết nhưng rất đáng ghé của thành phố.",
    [
        "Công trình đá độc nhất ở Nga có mái «thùng chữ thập bốn mặt», xây 1672.",
        "Trang trí gạch men (изразцы) kiểu Balakhna thế kỷ 17 trên các tang trống.",
        "Được trùng tu trong dự án «Ilyinskaya Sloboda»; gần bia tưởng niệm Ivan Kulibin.",
    ],
    {
        "hours_vi": "Mở theo giờ lễ, thường ban ngày.",
        "ticket_vi": "Vào tự do (nơi thờ tự đang hoạt động).",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; buổi sáng có ánh sáng đẹp để ngắm mái và gạch men.",
        "tips_vi": "Kết hợp đi bộ khu phố cổ Zapochainye và ngắm điền trang cổ (Палаты Олисова) ngay bên cạnh.",
    },
    [
        {"title": "sobory.ru — Церковь Успения на Ильинской горе (object 00922)", "url": "https://sobory.ru/article/?object=00922"},
        {"title": "Wikipedia (RU) — Успенская церковь на Ильинской горе", "url": "https://ru.wikipedia.org/wiki/Успенская_церковь_на_Ильинской_горе"},
    ],
    ["church", "1672", "uzorochye", "izraztsy", "olisov", "zapochainye"],
    maps_text("Успенская церковь на Ильинской горе", "Нижний Новгород", "Assumption Church on Ilyinskaya Hill", "Nizhny Novgorod", 56.32634, 43.99016),
))

# 4) Церковь Илии Пророка -----------------------------------------------------
RECORDS.append(rec(
    "ilyinskaya-church",
    "Nhà thờ Tiên tri Ê-li-a (Ilyinskaya tserkov)",
    "Церковь Илии Пророка",
    "Church of Elijah the Prophet",
    ["church"],
    56.32819, 43.99357,
    "Phố Ilyinskaya, số 9, khu Zapochainye, thành phố Nizhny Novgorod, Nga.",
    "Nhà thờ Tiên tri Ê-li-a đứng trên phố cổ Ilyinskaya, trái tim của khu phố buôn Zapochainye. Theo truyền thống, nhà thờ gắn với việc thành phố thoát vây năm 1505; ngôi nhà thờ đá xuất hiện từ giữa thế kỷ 17 và đã được phục dựng.",
    "Nằm trên phố Ilyinskaya – con phố cổ dẫn lên đồi Ilyinskaya, từng là khu phố buôn sầm uất Zapochainye của Nizhny Novgorod – nhà thờ Tiên tri Ê-li-a có một truyền thuyết lập nên đáng nhớ: người ta kể rằng trong cuộc vây hãm năm 1505, một phát đại bác bắn đi từ ngọn đồi này đã hạ được thủ lĩnh quân địch, khiến vòng vây tan rã; để tạ ơn, dân thành dựng một nhà thờ gỗ mang tên Tiên tri Ê-li-a. Ngôi nhà thờ đá hiện nay hình thành từ giữa thế kỷ 17, sau đó được cải tạo nhiều lần. Thời Xô Viết nhà thờ bị đóng cửa và biến dạng, đến những thập niên gần đây mới được trả lại hình dáng và chức năng ban đầu. Ngày nay nhà thờ là một điểm nhấn của tuyến phố đi bộ lịch sử Ilyinskaya với nhiều dinh thự thương nhân được phục hồi, rất hợp để kết hợp trong hành trình khám phá khu phố cổ.",
    [
        "Điểm nhấn của phố cổ Ilyinskaya – khu phố buôn Zapochainye lịch sử.",
        "Truyền thuyết gắn với việc thành phố thoát vây năm 1505.",
        "Nhà thờ đá từ giữa thế kỷ 17, đã được phục dựng sau thời Xô Viết.",
    ],
    {
        "hours_vi": "Mở theo giờ lễ, thường ban ngày.",
        "ticket_vi": "Vào tự do (nơi thờ tự đang hoạt động).",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Đi bộ dọc phố Ilyinskaya ngắm các dinh thự thương nhân được phục hồi; kết hợp nhà thờ Uspenskaya gần đó.",
    },
    [
        {"title": "sobory.ru — Церковь Илии Пророка, Нижний Новгород (object 01402)", "url": "https://sobory.ru/article/?object=01402"},
        {"title": "Wikipedia (RU) — Ильинская церковь (Нижний Новгород)", "url": "https://ru.wikipedia.org/wiki/Ильинская_церковь_(Нижний_Новгород)"},
    ],
    ["church", "ilyinskaya", "zapochainye", "old-town"],
    maps_text("Церковь Илии Пророка", "Нижний Новгород", "Church of Elijah the Prophet", "Nizhny Novgorod", 56.32819, 43.99357),
))

# 5) Оранский Богородицкий монастырь ------------------------------------------
RECORDS.append(rec(
    "oransky-monastery",
    "Tu viện Oranky Bogoroditsky (Oransky monastyr)",
    "Оранский Богородицкий монастырь",
    "Oransky Bogoroditsky Monastery",
    ["church", "monument"],
    55.895119, 43.716106,
    "Làng Oranki, phố Pochtovaya số 2, huyện Bogorodsky, tỉnh Nizhny Novgorod, Nga (cách thành phố ~60 km về phía nam).",
    "Tu viện nam Oranky Bogoroditsky được lập năm 1634 để tôn kính bản sao icon Đức Mẹ Oranskaya. Là một trong những trung tâm hành hương lớn của tỉnh, tu viện có quần thể thánh đường và tháp chuông giữa vùng đồng quê yên tĩnh phía nam Nizhny Novgorod.",
    "Được quý tộc Pyotr Glyadkov lập năm 1634 như một ẩn thất để tôn kính bản sao icon Đức Mẹ Vladimir–Oranskaya, tu viện Oranky Bogoroditsky nằm ở làng Oranki, huyện Bogorodsky, cách thành phố Nizhny Novgorod khoảng 60 km về phía nam. Qua nhiều thế kỷ, nơi đây trở thành một trong những trung tâm hành hương quan trọng nhất của tỉnh, gắn với các cuộc rước icon Oranskaya nổi tiếng. Quần thể tu viện gồm thánh đường chính, các nhà thờ phụ và tháp chuông, được bao quanh bởi cảnh quan đồng quê thanh bình. Trong thế kỷ 20 đầy biến động, khu tu viện từng bị trưng dụng làm trại giam giữ trong một giai đoạn; sau này được trả lại cho Giáo hội và dần được phục hồi. Ngày nay tu viện đón khách hành hương và du khách muốn tìm một điểm đến tâm linh, tĩnh lặng ngoài thành phố.",
    [
        "Lập năm 1634, tôn kính icon Đức Mẹ Oranskaya; trung tâm hành hương lớn của tỉnh.",
        "Quần thể thánh đường và tháp chuông giữa vùng đồng quê phía nam Nizhny Novgorod.",
        "Gắn với các cuộc rước icon Oranskaya truyền thống.",
    ],
    {
        "hours_vi": "Ban ngày; giờ mở theo lịch tu viện và giờ lễ.",
        "ticket_vi": "Vào tự do; tuỳ tâm công đức.",
        "duration_vi": "Khoảng 1 giờ (chưa kể di chuyển).",
        "best_time_vi": "Cuối xuân đến đầu thu; các dịp lễ rước icon rất đông khách hành hương.",
        "tips_vi": "Cần xe riêng để tới; ăn mặc kín đáo, nữ nên mang khăn trùm đầu.",
    },
    [
        {"title": "svyatsy.org — Оранский Богородицкий мужской монастырь", "url": "https://svyatsy.org/churches/nizhegorodskaya_oblast/bogorodskiy_rayon/oranki/oranskiy_bogorodickiy_muzhskoy_monastyr/"},
        {"title": "sobory.ru — Оранки, Оранский Богородицкий монастырь (object 04995)", "url": "https://sobory.ru/article/?object=04995"},
    ],
    ["monastery", "pilgrimage", "1634", "oranskaya-icon", "bogorodsky"],
    maps_text("Оранский Богородицкий монастырь", "Оранки", "Oransky Bogoroditsky Monastery", "Oranki", 55.895119, 43.716106),
))

# 6) Городецкий Феодоровский монастырь ----------------------------------------
RECORDS.append(rec(
    "gorodets-feodorovsky-monastery",
    "Tu viện Feodorovsky ở Gorodets (nơi Aleksandr Nevsky qua đời)",
    "Городецкий Феодоровский монастырь",
    "Gorodets Feodorovsky Monastery",
    ["church", "monument"],
    56.646416, 43.477505,
    "Thành phố Gorodets, Quảng trường Proletarskaya số 34б, tỉnh Nizhny Novgorod, Nga (bên bờ sông Volga).",
    "Tu viện cổ bên bờ Volga ở Gorodets, gắn với sự kiện Đại công tước Aleksandr Nevsky đi tu và qua đời tại đây năm 1263 khi trở về từ Kim Trướng hãn quốc. Bị phá huỷ thời Xô Viết, tu viện được dựng lại năm 2008–2009 với thánh đường Feodorovsky là ngôi nhà thờ chính.",
    "Nằm bên bờ sông Volga tại thị trấn thủ công cổ Gorodets, tu viện Feodorovsky có bề dày lịch sử gắn liền với một nhân vật vĩ đại của nước Nga: Đại công tước Aleksandr Nevsky. Trên đường trở về từ Kim Trướng hãn quốc (Golden Horde) năm 1263, ông lâm bệnh nặng, đã khấn nguyện đi tu và nhận đại lược tu (схима) với tên Alexy, rồi qua đời tại tu viện này. Suốt nhiều thế kỷ, tu viện là một trung tâm tinh thần của vùng; đến những năm 1930 bị phá huỷ. Quần thể hiện nay được tái thiết trong các năm 2008–2009, với nhà thờ chính toà Feodorovsky (tôn kính icon Đức Mẹ Feodorovskaya) làm trung tâm và là nhà thờ chính của giáo phận Gorodets. Kết hợp cùng khu phố cổ Gorodets với nghề vẽ tranh Gorodets và bánh mật (пряник) trứ danh, tu viện là điểm dừng ý nghĩa cả về tâm linh lẫn lịch sử.",
    [
        "Nơi Đại công tước Aleksandr Nevsky đi tu và qua đời năm 1263.",
        "Thánh đường Feodorovsky là nhà thờ chính toà của giáo phận Gorodets.",
        "Tái thiết 2008–2009; kết hợp tốt với khu phố cổ Gorodets.",
    ],
    {
        "hours_vi": "Ban ngày; theo lịch tu viện và giờ lễ.",
        "ticket_vi": "Vào tự do; tuỳ tâm công đức.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; đẹp khi kết hợp tham quan Gorodets.",
        "tips_vi": "Đi cùng lượt tham quan phố cổ Gorodets (tranh Gorodets, bảo tàng bánh mật); ăn mặc lịch sự.",
    },
    [
        {"title": "Wikipedia (RU) — Феодоровский монастырь (Городец)", "url": "https://ru.wikipedia.org/wiki/Феодоровский_монастырь_(Городец)"},
        {"title": "sobory.ru — Городец, Феодоровский мужской монастырь (object 24204)", "url": "https://sobory.ru/article/?object=24204"},
    ],
    ["monastery", "gorodets", "alexander-nevsky", "volga", "feodorovskaya-icon"],
    maps_org("https://yandex.com/maps/org/gorodetskiy_feodorovskiy_muzhskoy_monastyr/1373652885/", "Gorodets Feodorovsky Monastery", "Gorodets"),
))

# 7) Амвросиев Николаевский Дудин монастырь -----------------------------------
RECORDS.append(rec(
    "dudin-monastery",
    "Tu viện Dudin (Amvrosiev Nikolaevsky) bên vách sông Oka",
    "Амвросиев Николаевский Дудин монастырь",
    "Amvrosiev Nikolaevsky Dudin Monastery",
    ["church", "monument"],
    56.181734, 43.385054,
    "Gần làng Teteryugino (Podyablonnoye), huyện Bogorodsky, bờ phải sông Oka, tỉnh Nizhny Novgorod, Nga.",
    "Tu viện trung cổ (khoảng năm 1408) nép mình trên vách cao dựng đứng của bờ phải sông Oka, được ví như «pháo đài tinh thần» của vùng. Truyền thống kể rằng thánh Sergy Radonezhsky từng ghé qua. Đường tới hiểm trở nên nơi đây giữ được vẻ tĩnh mịch, hoang sơ.",
    "Ẩn mình trên một vách đá cao chóng mặt của bờ phải sông Oka gần làng Teteryugino (đi qua Podyablonnoye), huyện Bogorodsky, tu viện Amvrosiev Nikolaevsky Dudin là một trong những tu viện cổ nhất vùng, có từ khoảng năm 1408. Được đặt tên Amvrosiev theo vị viện phụ đầu tiên và Nikolaevsky để tôn kính thánh Nikolai; theo truyền thống, thánh Sergy Radonezhsky từng ghé qua đây trên đường tới Nizhny Novgorod. Trong nhiều thế kỷ, tu viện là một «tiền đồn tinh thần» canh giữ tuyến sông Oka. Quần thể gồm nhà thờ Đức Mẹ An Nghỉ, tháp chuông và các dãy nhà tu; sau thời gian dài hoang phế, từ năm 2006 nơi đây bắt đầu được khôi phục. Do đường vào khá hiểm trở – phải đi đường đất rồi men lối mòn xuống phía sông – tu viện vẫn giữ được sự tĩnh mịch, hoang sơ và tầm nhìn ngoạn mục ra khúc sông Oka, hấp dẫn cả khách hành hương lẫn người yêu thiên nhiên.",
    [
        "Một trong những tu viện cổ nhất vùng (khoảng 1408), trên vách cao bờ phải sông Oka.",
        "Truyền thống gắn với chuyến ghé của thánh Sergy Radonezhsky.",
        "Cảnh quan hoang sơ, tầm nhìn đẹp ra sông Oka; đang được khôi phục từ 2006.",
    ],
    {
        "hours_vi": "Ban ngày; nên đi khi thời tiết khô ráo.",
        "ticket_vi": "Vào tự do; tuỳ tâm công đức.",
        "duration_vi": "Khoảng 1 giờ (chưa kể di chuyển khó khăn).",
        "best_time_vi": "Cuối xuân đến đầu thu; tránh sau mưa vì đường đất trơn lầy.",
        "tips_vi": "Cần xe gầm cao và đi bộ đoạn cuối; mang giày phù hợp; ăn mặc kín đáo.",
    },
    [
        {"title": "sobory.ru — Тетерюгино, Николаевский Амвросиев Дудин монастырь (object 03521)", "url": "https://sobory.ru/article/?object=03521"},
        {"title": "azbyka.ru (Азбука паломника) — Амвросиев Николаевский Дудин монастырь", "url": "https://azbyka.ru/palomnik/Амвросиев_Николаевский_Дудин_мужской_монастырь"},
    ],
    ["monastery", "oka", "medieval", "1408", "bogorodsky", "nature"],
    maps_text("Амвросиев Николаевский Дудин монастырь", "Тетерюгино", "Dudin Monastery", "Teteryugino", 56.181734, 43.385054),
))

# 8) Памятник Минину и Пожарскому ---------------------------------------------
RECORDS.append(rec(
    "minin-pozharsky-monument",
    "Tượng đài Minin và Pozharsky (bản sao ở Nizhny Novgorod)",
    "Памятник Минину и Пожарскому",
    "Monument to Minin and Pozharsky",
    ["monument", "square_street"],
    56.32972, 43.99667,
    "Quảng trường Narodnogo Edinstva (Đoàn kết Nhân dân), dưới chân Kremlin, cạnh nhà thờ Ioann Predtechi, thành phố Nizhny Novgorod, Nga.",
    "Tượng đài Kuzma Minin và công tước Dmitry Pozharsky – hai thủ lĩnh đội dân binh 1611–1612 – khánh thành ngày 4/11/2005. Đây là bản sao (nhỏ hơn bản gốc 5 cm) do điêu khắc gia Zurab Tsereteli thực hiện, phỏng theo tượng đài nổi tiếng của Ivan Martos trên Quảng trường Đỏ ở Moskva.",
    "Đứng ngay dưới chân Kremlin, trên Quảng trường Đoàn kết Nhân dân (площадь Народного единства) và bên cạnh nhà thờ Giáng Sinh Thánh Gioan Tiền Hô, tượng đài Minin và Pozharsky tôn vinh hai người anh hùng đã dẫn dắt đội dân binh Nizhny Novgorod giải phóng Moskva khỏi quân can thiệp Ba Lan trong Thời loạn (Smuta) năm 1611–1612. Tượng được khánh thành ngày 4 tháng 11 năm 2005 – đúng dịp Ngày Đoàn kết Nhân dân của nước Nga. Đây là một bản sao gần như y hệt (chỉ nhỏ hơn 5 cm) của tượng đài trứ danh do điêu khắc gia Ivan Martos tạc, hiện đặt trên Quảng trường Đỏ ở Moskva; tác giả bản sao là điêu khắc gia lừng danh Zurab Tsereteli. Vị trí đặt tượng mang tính biểu tượng: theo truyền thống, chính từ khu vực này – bên nhà thờ Ioann Predtechi – phong trào dân binh năm 1611 đã khởi phát. Đây là điểm chụp ảnh và tưởng niệm quen thuộc, thuận tiện kết hợp với lối lên Kremlin và phố cổ Rozhdestvenskaya.",
    [
        "Bản sao (nhỏ hơn 5 cm) tượng đài Minin–Pozharsky trên Quảng trường Đỏ, do Tsereteli thực hiện.",
        "Khánh thành 4/11/2005 nhân Ngày Đoàn kết Nhân dân của Nga.",
        "Đặt tại nơi truyền thống khởi phát đội dân binh 1611, dưới chân Kremlin.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–20 phút.",
        "best_time_vi": "Quanh năm; dịp 4/11 (Ngày Đoàn kết Nhân dân) có sự kiện.",
        "tips_vi": "Kết hợp tham quan nhà thờ Ioann Predtechi ngay bên và đi bộ lên Kremlin.",
    },
    [
        {"title": "Wikipedia (RU) — Памятник Минину и Пожарскому (Нижний Новгород)", "url": "https://ru.wikipedia.org/wiki/Памятник_Минину_и_Пожарскому_(Нижний_Новгород)"},
        {"title": "1000mest.ru — Памятник Минину и Пожарскому в Нижнем Новгороде", "url": "https://www.1000mest.ru/mininu_i_pozharskomu_nn"},
    ],
    ["monument", "minin", "pozharsky", "tsereteli", "kremlin", "2005"],
    maps_text("Памятник Минину и Пожарскому", "Нижний Новгород", "Monument to Minin and Pozharsky", "Nizhny Novgorod", 56.32972, 43.99667),
))

# 9) Стадион «Нижний Новгород» ------------------------------------------------
RECORDS.append(rec(
    "nizhny-novgorod-stadium",
    "Sân vận động «Nizhny Novgorod» (trên bãi Strelka)",
    "Стадион «Нижний Новгород»",
    "Nizhny Novgorod Stadium",
    ["other"],
    56.337626, 43.962753,
    "Phố Dolzhanskaya, số 2А, bãi Strelka (nơi sông Oka đổ vào Volga), thành phố Nizhny Novgorod, Nga.",
    "Sân vận động bóng đá hiện đại xây dựng năm 2015–2018 phục vụ World Cup 2018, đặt ngay trên bãi Strelka – điểm hợp lưu sông Oka và Volga. Sức chứa khoảng 45.000 chỗ, kiến trúc gợi hình sóng nước và gió; nay là sân nhà của CLB Pari Nizhny Novgorod.",
    "Toạ lạc trên bãi Strelka – mũi đất nơi sông Oka đổ vào sông Volga – sân vận động «Nizhny Novgorod» được xây dựng trong các năm 2015–2018 để phục vụ Giải vô địch bóng đá thế giới FIFA World Cup 2018. Công trình có sức chứa khoảng 45.000 khán giả, nổi bật với thiết kế cột trụ và mái nhẹ gợi liên tưởng tới nước và gió của vùng hợp lưu hai dòng sông. Trong kỳ World Cup, sân đã đăng cai nhiều trận đấu và nhanh chóng trở thành một biểu tượng kiến trúc mới của thành phố. Sau giải, sân là sân nhà của câu lạc bộ bóng đá Pari Nizhny Novgorod và được dùng làm tổ hợp thể thao – giải trí đa năng (những năm gần đây sân mang tên thương mại Sovcombank Arena). Cùng với các nhà kho Pakgauzy được cải tạo và nhà thờ Aleksandr Nevsky, sân vận động tạo nên quần thể hiện đại – lịch sử đặc sắc của bãi Strelka, một điểm dạo chơi và ngắm hoàng hôn bên sông rất được ưa thích.",
    [
        "Xây cho World Cup 2018, đặt trên bãi Strelka hợp lưu Oka–Volga.",
        "Sức chứa ~45.000; kiến trúc gợi hình sóng nước và gió.",
        "Sân nhà CLB Pari Nizhny Novgorod (tên thương mại gần đây: Sovcombank Arena).",
    ],
    {
        "hours_vi": "Vào sân theo ngày có trận đấu/sự kiện; khu vực Strelka quanh sân dạo tự do.",
        "ticket_vi": "Vé theo trận đấu/sự kiện; đôi khi có tour tham quan sân.",
        "duration_vi": "Khoảng 30–60 phút quanh khu vực (chưa kể xem trận).",
        "best_time_vi": "Mùa bóng đá; hoàng hôn trên bãi Strelka rất đẹp.",
        "tips_vi": "Kết hợp ngắm nhà kho Pakgauzy và nhà thờ Aleksandr Nevsky ngay cạnh trên Strelka.",
    },
    [
        {"title": "Wikipedia (RU) — Нижний Новгород (стадион)", "url": "https://ru.wikipedia.org/wiki/Нижний_Новгород_(стадион)"},
        {"title": "Стрелка (Нижний Новгород) — Википедия", "url": "https://ru.wikipedia.org/wiki/Стрелка_(Нижний_Новгород)"},
    ],
    ["stadium", "world-cup-2018", "strelka", "modern", "football"],
    maps_text("Стадион Нижний Новгород", "Нижний Новгород", "Nizhny Novgorod Stadium", "Nizhny Novgorod", 56.337626, 43.962753),
))

# 10) Нижегородский цирк ------------------------------------------------------
RECORDS.append(rec(
    "nizhny-novgorod-circus",
    "Rạp xiếc Nizhny Novgorod (mang tên M. P. Nazarova)",
    "Нижегородский цирк имени М. П. Назаровой",
    "Nizhny Novgorod Circus",
    ["theatre", "other"],
    56.3185, 43.9530,
    "Phố Kommunisticheskaya, số 38, khu Kanavino (gần ga Moskovsky), thành phố Nizhny Novgorod, Nga.",
    "Rạp xiếc Nizhny Novgorod mang tên nữ nghệ sĩ thuần hổ Margarita Nazarova. Sau đợt tái thiết dài, rạp mở cửa trở lại năm 2007 và được xem là một trong những tổ hợp xiếc lớn nhất châu Âu, nằm ở tả ngạn sông Oka gần ga Moskovsky.",
    "Rạp xiếc Nizhny Novgorod nằm ở khu Kanavino bên tả ngạn sông Oka, trong tầm đi bộ từ ga đường sắt Moskovsky và ga metro Moskovskaya. Rạp mang tên Margarita Nazarova – nữ nghệ sĩ thuần dưỡng hổ huyền thoại của Liên Xô. Sau một quá trình tái thiết kéo dài, công trình được khánh thành lại vào năm 2007 và khi đó được đánh giá là một trong những tổ hợp biểu diễn xiếc lớn và hiện đại nhất châu Âu, với khán phòng khoảng 2.000 chỗ cùng trang thiết bị sân khấu tiên tiến. Đây là điểm giải trí lý tưởng cho gia đình và trẻ em, thường xuyên đón các chương trình lưu diễn danh tiếng của Nga. Vị trí thuận tiện gần đầu mối giao thông khiến rạp xiếc dễ kết hợp trong hành trình khám phá khu vực tả ngạn (Hội chợ Nizhny Novgorod, nhà thờ Aleksandr Nevsky, bãi Strelka).",
    [
        "Mang tên nữ nghệ sĩ thuần hổ Margarita Nazarova.",
        "Tái thiết và mở lại năm 2007, thuộc hàng tổ hợp xiếc lớn nhất châu Âu.",
        "Khán phòng ~2.000 chỗ; gần ga Moskovsky, tiện cho gia đình và trẻ em.",
    ],
    {
        "hours_vi": "Theo lịch biểu diễn (thường cuối tuần và các suất chiều/tối); kiểm tra lịch trước.",
        "ticket_vi": "Mua vé theo chương trình; nhiều mức giá.",
        "duration_vi": "Mỗi suất diễn khoảng 2 giờ.",
        "best_time_vi": "Quanh năm; dịp lễ và nghỉ học có nhiều suất diễn.",
        "tips_vi": "Đặt vé sớm cho các chương trình lưu diễn nổi tiếng; kết hợp thăm khu tả ngạn Kanavino.",
    },
    [
        {"title": "Культура.РФ — Нижегородский государственный цирк", "url": "https://www.culture.ru/institutes/42792/nizhegorodskii-gosudarstvennyi-cirk"},
        {"title": "Wikidata — Nizhny Novgorod Circus (Q19911285)", "url": "https://www.wikidata.org/wiki/Q19911285"},
    ],
    ["circus", "nazarova", "family", "kanavino", "entertainment"],
    maps_org("https://yandex.com/maps/org/nizhegorodskiy_gosudarstvenny_tsirk_imeni_margarity_nazarovoy/1027981907/", "Nizhny Novgorod Circus", "Nizhny Novgorod"),
))

# 11) Пустынские озёра --------------------------------------------------------
RECORDS.append(rec(
    "pustynskie-lakes",
    "Hệ hồ Pustynskie (Pustynskie ozyora)",
    "Пустынские озёра",
    "Pustynskie Lakes",
    ["park_garden", "other"],
    55.668564, 43.565210,
    "Gần làng Staraya Pustyn, trên sông Serezha, huyện Arzamassky, tỉnh Nizhny Novgorod, Nga.",
    "Chuỗi tám hồ karst nối nhau trên sông Serezha, thuộc khu bảo tồn Pustynsky (thành lập 1934). Đây là hệ hồ lớn và đẹp bậc nhất tỉnh, giàu động vật hoang dã quý (chuột chũi nước vyhukhol, hải ly, rái cá) và hơn 160 loài chim.",
    "Trải dài trên sông Serezha gần làng Staraya Pustyn ở phía bắc huyện Arzamassky, Pustynskie ozyora là một chuỗi gồm tám hồ karst nối thông nhau – hệ hồ đẹp và nổi tiếng vào loại bậc nhất tỉnh Nizhny Novgorod. Các hồ hình thành do quá trình karst (đá vôi bị hoà tan tạo hố sụt) ngay trong lòng và ven sông Serezha. Toàn khu vực nằm trong khu bảo tồn thiên nhiên Pustynsky, được lập từ năm 1934, với hệ sinh thái phong phú: nơi đây có loài chuột chũi nước vyhukhol (desman) quý hiếm, hải ly, rái cá, chồn thông và nhiều loài dơi; đã ghi nhận hơn 160 loài chim, trong đó có đại bàng vàng, cắt lớn và ó cá. Cảnh sắc hồ nước lặng soi bóng rừng cây tạo nên khung cảnh yên bình, là điểm đến ưa thích cho du lịch sinh thái, chèo thuyền, câu cá và cắm trại. Vì là khu bảo tồn, du khách cần giữ gìn cảnh quan và tuân thủ quy định bảo vệ thiên nhiên.",
    [
        "Chuỗi tám hồ karst nối nhau trên sông Serezha – hệ hồ đẹp bậc nhất tỉnh.",
        "Thuộc khu bảo tồn Pustynsky (từ 1934); hệ sinh thái phong phú.",
        "Có chuột chũi nước vyhukhol quý hiếm và hơn 160 loài chim.",
    ],
    {
        "hours_vi": "Không gian thiên nhiên mở; tham quan ban ngày.",
        "ticket_vi": "Vào tự do; một số dịch vụ (thuyền, cơ sở nghỉ) thu phí.",
        "duration_vi": "Nửa ngày đến trọn ngày.",
        "best_time_vi": "Mùa hè (tắm, chèo thuyền, ngắm chim); thu để ngắm lá vàng.",
        "tips_vi": "Là khu bảo tồn – không xả rác, không gây ồn; mang chống muỗi; tôn trọng quy định bảo vệ động vật.",
    },
    [
        {"title": "kerzhenskiy.ru — Пустынские озёра. Нижегородское Поволжье", "url": "https://kerzhenskiy.ru/place/pustynskij/"},
        {"title": "tourismnn.ru — Пустынские озёра (природный заказник)", "url": "https://tourismnn.ru/maintour/eco/pustynskie-lake"},
    ],
    ["nature", "lakes", "karst", "zakaznik", "serezha", "vyhukhol", "arzamassky"],
    maps_text("Пустынские озёра", "Старая Пустынь", "Pustynskie Lakes", "Staraya Pustyn", 55.668564, 43.565210),
))

# 12) Вадское озеро -----------------------------------------------------------
RECORDS.append(rec(
    "vadskoye-lake",
    "Hồ Vad (Vadskoye ozero) – hồ karst với «voklina»",
    "Вадское озеро",
    "Lake Vad (Vadskoye)",
    ["park_garden", "other"],
    55.5395, 44.192,
    "Thị trấn Vad, huyện Vadsky, tỉnh Nizhny Novgorod, Nga (trên sông Vadok, nhánh của sông Pyana).",
    "Hồ karst hình thành từ các hố sụt trên sông Vadok. Nổi tiếng với «voklina» – những mạch nước ngầm karst phun mạnh từ đáy hồ tạo sóng đồng tâm trên mặt nước và giữ cho một khoảng hồ không đóng băng ngay giữa mùa đông. Là di tích thiên nhiên của tỉnh.",
    "Nằm ngay bên thị trấn Vad, hồ Vad (Vadskoye ozero) hình thành do sự hợp nhất của nhiều hố sụt karst trong lòng sông Vadok – một nhánh của sông Pyana. Điều làm nên danh tiếng của hồ là hiện tượng «voklina»: từ những phễu karst sâu dưới đáy, các mạch nước ngầm lạnh và trong vắt phun lên mạnh mẽ, tạo thành những vòng sóng đồng tâm lan toả trên mặt nước. Nhờ dòng chảy ngầm mạnh (lan tới khoảng 20 mét quanh miệng voklina), một khoảng mặt hồ không đóng băng ngay cả giữa mùa đông giá rét, tạo nên cảnh «polynya» (khoảng nước hở) kỳ thú giữa băng tuyết. Hồ được công nhận là di tích thiên nhiên của tỉnh, là điểm đến độc đáo cho những ai muốn tận mắt thấy hiện tượng thuỷ văn hiếm gặp, câu cá và dã ngoại. Du khách nên cẩn trọng khi tới gần mép nước vì có dòng chảy ngầm và nhiệt độ lạnh.",
    [
        "Hồ karst hình thành từ các hố sụt trên sông Vadok.",
        "Nổi tiếng với «voklina» – mạch nước ngầm phun tạo sóng đồng tâm.",
        "Một khoảng hồ không đóng băng giữa mùa đông; là di tích thiên nhiên.",
    ],
    {
        "hours_vi": "Không gian thiên nhiên mở; tham quan ban ngày.",
        "ticket_vi": "Vào tự do (miễn phí).",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Mùa hè để ngắm nước trong và voklina; mùa đông để thấy polynya không đóng băng.",
        "tips_vi": "Cẩn trọng khi tới gần mép nước (dòng ngầm, nước lạnh); giữ gìn di tích thiên nhiên.",
    },
    [
        {"title": "putidorogi-nn.ru — Озеро Вад (Нижегородская область)", "url": "https://putidorogi-nn.ru/evropa/353-ozero-vad"},
        {"title": "esosedi — Вадское озеро (координаты)", "url": "http://ru.esosedi.org/RU/NIZ/1000069079/vadskoe_ozero/"},
    ],
    ["nature", "lake", "karst", "voklina", "spring", "vadsky"],
    maps_text("Вадское озеро", "Вад", "Lake Vad", "Vad", 55.5395, 44.192),
))

# 13) Усадьба Приклонских-Рукавишниковых в Подвязье ---------------------------
RECORDS.append(rec(
    "podvyazye-estate",
    "Điền trang Priklonsky–Rukavishnikov ở Podvyazye",
    "Усадьба Приклонских-Рукавишниковых (Подвязье)",
    "Priklonsky-Rukavishnikov Estate (Podvyazye)",
    ["palace", "park_garden"],
    56.16534, 43.34911,
    "Làng Podvyazye, phố Okskaya, huyện Bogorodsky, tỉnh Nizhny Novgorod, Nga (mỏm đất cao bờ phải sông Oka, đối diện Zhelnino, cách thành phố ~40 km).",
    "Một trong những điền trang quý tộc lớn còn sót lại của tỉnh, di sản văn hoá cấp liên bang, nằm trên mỏm đất cao nhìn ra khúc quanh sông Oka. Từ thế kỷ 18 thuộc dòng họ Priklonsky, đến 1879 về tay triệu phú Sergei Rukavishnikov – người biến nơi đây thành trang trại kiểu mẫu với trại ngựa, tháp nước, nhà kính, điện, nước máy và sưởi hơi.",
    "Nằm trên một mỏm đất cao và hẹp của bờ phải sông Oka, đối diện khu Zhelnino và cách trung tâm Nizhny Novgorod khoảng 40 km, điền trang Priklonsky–Rukavishnikov ở làng Podvyazye là một trong những dinh cơ quý tộc lớn nhất còn sót lại của tỉnh và là di tích kiến trúc cấp liên bang. Nửa sau thế kỷ 18, điền trang thuộc về Mikhail Priklonsky (giám đốc Đại học Moskva); dòng họ Priklonsky đã cho dựng dinh chính, nhà phụ, các dãy nhà phục vụ và lập vườn cây ăn quả, đồng thời xây một nhà thờ Phục Sinh kiểu vòng tròn cột (rotunda) độc đáo để mừng chiến thắng Napoléon (nay chỉ còn phế tích cùng gác chuông hình khải hoàn môn). Năm 1879, điền trang về tay triệu phú Nizhny Novgorod Sergei Rukavishnikov; suốt gần 40 năm ông biến nơi đây thành một trang trại kiểu mẫu với trại nuôi ngựa, kết hợp các dãy nhà gạch đỏ (chuồng ngựa, lò rèn) cùng những công trình phong cách cổ điển và Tây Âu. Ông cho lắp đặt đủ tiện nghi tân tiến thời đó: nước máy, sưởi hơi nước, điện, nhà kính trồng dứa và đào chín ngay giữa mùa đông; dinh chính có cả vọng lâu (belveder) trên mái để ngắm cảnh. Ngày nay điền trang tuy xuống cấp nhưng vẫn giữ được nét bề thế; một tổ chức tình nguyện địa phương đang trùng tu và tổ chức tham quan, mang lại cơ hội chiêm ngưỡng một «tổ ấm quý tộc» cùng khung cảnh sông Oka thơ mộng.",
    [
        "Một trong những điền trang quý tộc lớn nhất còn sót lại của tỉnh; di sản cấp liên bang.",
        "Gắn với dòng họ Priklonsky (thế kỷ 18) và triệu phú Rukavishnikov (từ 1879).",
        "Trang trại kiểu mẫu với trại ngựa, tháp nước, nhà kính, điện; phế tích nhà thờ Phục Sinh hình rotunda.",
    ],
    {
        "hours_vi": "Ban ngày; nên liên hệ trước vì do tổ chức tình nguyện quản lý.",
        "ticket_vi": "Vé vào cửa (khoảng 250 rúp cho người lớn); có tổ chức tham quan.",
        "duration_vi": "Khoảng 1–1,5 giờ (chưa kể di chuyển).",
        "best_time_vi": "Cuối xuân đến đầu thu; cảnh sông Oka đẹp vào chiều muộn.",
        "tips_vi": "Cần xe riêng; mang giày đi bộ vì địa hình mỏm đất; nhiều công trình đang xuống cấp, cẩn trọng an toàn.",
    },
    [
        {"title": "putidorogi-nn.ru — Усадьба Рукавишниковых-Приклонских в Подвязье", "url": "https://putidorogi-nn.ru/evropa/352-usadba-podviaze"},
        {"title": "Wikipedia (RU) — Подвязье (усадьба)", "url": "https://ru.wikipedia.org/wiki/Подвязье_(усадьба)"},
    ],
    ["estate", "rukavishnikov", "priklonsky", "oka", "federal-heritage", "bogorodsky"],
    maps_text("Усадьба Приклонских-Рукавишниковых Подвязье", "Подвязье", "Priklonsky-Rukavishnikov Estate Podvyazye", "Podvyazye", 56.16534, 43.34911),
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
