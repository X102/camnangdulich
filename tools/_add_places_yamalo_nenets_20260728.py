# -*- coding: utf-8 -*-
"""_add_places_yamalo_nenets_20260728.py — VÙNG: Khu tự trị Yamalo-Nenets (Yamal)
(lần chạy tự động 2026-07-28).

Bối cảnh: yamalo-nenets.json hiện có 6 địa điểm. Vùng Bắc Cực thưa dân nhưng có nhiều
biểu tượng độc đáo; đợt này bổ sung 24 địa điểm THẬT (nâng 6 -> 30), đa dạng loại hình:
  church 6 · museum 6 · monument 2 · bridge 1 · park_garden 5 · other 3 · theatre 1.
Phân bố theo địa lý: Salekhard, Novy Urengoy, Nadym, Noyabrsk, Labytnangi, Yar-Sale,
và các điểm thiên nhiên/di sản Bắc Cực (hồ Bolshoye Shchuchye, hố khí Yamal,
VQG Gydansky, massif Rai-Iz/Ingilor - Polar Urals, khu bảo tồn Verkhne-Tazovsky).

TOẠ ĐỘ — xác minh chéo 2026-07 (ll= trong trang tổ chức Yandex.Maps; center= trong 2GIS;
sobory.ru; ru.wikipedia geo; RUSSPASS). Kiểm tra phạm vi YaNAO (lat ~62,8-73; lon ~65,6-84,2),
KHÔNG đảo lat/lon:
  Петропавловский собор Салехард 66.524825,66.591498 (sobory.ru obj.07673);
  Преображенский собор Салехард 66.539611,66.624018 (Арктическая 17; освящён 2024, крупнейший храм Арктики);
  Мост «Факел» Салехард 66.536602,66.600098 (вантовый мост через Шайтанку);
  Стела «Романтикам 70-х» Салехард 66.535847,66.638384 (N66°32'9.05" E66°38'18.18"; ул. Броднева);
  Ямальская филармония/КДЦ Салехард 66.534980,66.608507 (Арктическая 1);
  Национальная библиотека ЯНАО 66.535539,66.604661 (Чубынина 36; топ-10 достопр.);
  ОЦНК Салехард 66.529039,66.624964 (Республики 74); ЦКиС «Геолог» 66.536090,66.623957 (Матросова 31);
  Богоявленский собор Новый Уренгой 66.082739,76.657870 (мкр Оптимистов 1; 2014);
  Церковь Серафима Саровского Новый Уренгой 66.109333,76.678980 (ул. Захаренкова 2; первый храм города);
  Церковь Николая Чудотворца Надым 65.533311,72.512695 (Парковый пр.; освящён 1998);
  Музей истории и археологии Надыма 65.530248,72.518387 (Ленинградский 11);
  Дом природы Надым 65.535004,72.517471 (Парковый пр. 1); Экспозиция «История строительства» 65.535645,72.524640
  (Зверева 12/3; коллекция 501-й стройки/Надымское городище);
  Памятник комару Ноябрьск 63.190724,75.551709 (2ГИС; 2006, скульптор В. Чалый);
  Музейный ресурсный центр Ноябрьск 63.199416,75.463443 (Советская 82);
  Храм Архистратига Михаила Ноябрьск 63.200847,75.444433 (пр. Мира 72; 2005);
  ГЛК «Октябрьский» Лабытнанги 66.696610,66.570806 (мкр Октябрьский 5; у массива Рай-Из);
  Ямальский районный музей Яр-Сале 66.86259,70.85447 (Худи Сэроко 18);
  Озеро Большое Щучье 67.8833,66.3167 (67°53'N 66°19'E; глубочайшее на Урале ~136 м);
  Ямальский кратер 69.971111,68.370278 (69°58'16"N 68°22'13"E; ~30 км Ю Бованенково);
  Гыданский нацпарк 67.490373,78.738821 (Тазовский р-н; п-ов Гыдан);
  Массив Рай-Из/Ингилор/Харп 66.805678,65.803843 (координата п.г.т. Харп - ворота Полярного Урала);
  Верхне-Тазовский заповедник 62.858,84.190 (центр по границам 62°10'-63°33'N, 83°-85°23'E; Красноселькупский р-н).

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_yamalo_nenets_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "yamalo-nenets"
REGION_NAME_VI = "Khu tự trị Yamalo-Nenets"
FD = "Vùng Ural"


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


RECORDS = []

# 1) Петропавловский собор (Салехард) ------------------------------------------
RECORDS.append(rec(
    "salekhard-petropavlovsky-cathedral",
    "Nhà thờ Thánh Phêrô và Phaolô (Xô-bo Pi-ốt i Páp-la), Salekhard",
    "Петропавловский собор (Салехард)",
    "Saints Peter and Paul Cathedral (Salekhard)",
    ["church"],
    66.524825, 66.591498,
    "Số 1 phố Nikolaya Gogolya, trung tâm lịch sử Salekhard (Xa-lê-khác), Khu tự trị Yamalo-Nenets, Nga.",
    "Nhà thờ đá cổ nhất của Salekhard, xây năm 1886-1893 theo phong cách tân Gothic, là một trong những công trình tôn giáo lâu đời nhất vùng lãnh nguyên Ob. Ngôi thánh đường gạch đỏ nổi bật giữa phố cổ Obdorsk, đến nay vẫn là nhà thờ giáo xứ đang hoạt động.",
    "Nhà thờ Thánh Phêrô và Phaolô là ngôi nhà thờ đá đầu tiên và cổ nhất còn lại của Salekhard - thành phố xưa mang tên Obdorsk. Công trình được dựng trong các năm 1886-1893 bằng gạch nung, theo lối kiến trúc tân Gothic hiếm gặp ở Siberia, với những cửa sổ nhọn, tháp chuông vươn cao và mặt tường gạch đỏ trang trí tinh tế. Trong thời Xô Viết, nhà thờ bị đóng cửa và dùng làm kho, nhưng đến ngày 10-11-1990 được trao trả cho cộng đồng tín hữu và long trọng thánh hiến lại ngày 11-7-1991. Từ đó, đây trở thành trung tâm đời sống Chính Thống giáo của cả vùng cực bắc, gắn với lịch sử truyền giáo Obdorsk cho các dân tộc bản địa Nenets và Khanty. Nằm ngay lõi phố cổ, gần pháo đài gỗ Obdorsk phục dựng, nhà thờ là một điểm dừng quan trọng khi tản bộ khám phá khu trung tâm lịch sử Salekhard. Kiến trúc gạch đỏ của nó tạo tương phản ấn tượng với tuyết trắng mùa đông và là bối cảnh chụp ảnh được nhiều du khách yêu thích.",
    [
        "Nhà thờ đá cổ nhất Salekhard, xây 1886-1893 theo phong cách tân Gothic gạch đỏ.",
        "Gắn với lịch sử truyền giáo Obdorsk cho người Nenets, Khanty vùng cực bắc.",
        "Được trao trả tín hữu năm 1990-1991, nay là nhà thờ giáo xứ đang hoạt động.",
    ],
    {
        "hours_vi": "Mở theo giờ lễ; thường sáng đến tối. Nên xem lịch lễ tại chỗ.",
        "ticket_vi": "Vào tự do (công trình tôn giáo).",
        "duration_vi": "Khoảng 20-40 phút.",
        "best_time_vi": "Quanh năm; đẹp khi có tuyết hoặc dịp lễ lớn Chính Thống giáo.",
        "tips_vi": "Ăn mặc kín đáo khi vào bên trong; nữ nên trùm khăn. Kết hợp tham quan pháo đài Obdorsk gần đó.",
    },
    [
        {"title": "sobory.ru — Салехард, Церковь Петра и Павла", "url": "https://sobory.ru/article/?object=07673"},
        {"title": "Wikipedia (RU) — Петропавловский собор (Салехард)", "url": "https://ru.wikipedia.org/wiki/Петропавловский_собор_(Салехард)"},
    ],
    ["church", "orthodox", "neo-gothic", "salekhard", "historic"],
    maps_text("Петропавловский собор", "Салехард", "Saints Peter and Paul Cathedral", "Salekhard", 66.524825, 66.591498),
))

# 2) Преображенский собор (Салехард) -------------------------------------------
RECORDS.append(rec(
    "salekhard-preobrazhensky-cathedral",
    "Nhà thờ Chính toà Chúa Hiển Dung (Xô-bo Pri-ô-bra-gien-xki), Salekhard",
    "Кафедральный собор Преображения Господня (Салехард)",
    "Cathedral of the Transfiguration (Salekhard)",
    ["church"],
    66.539611, 66.624018,
    "Phố Arkticheskaya, Salekhard (Xa-lê-khác), Khu tự trị Yamalo-Nenets, Nga.",
    "Nhà thờ chính toà mới của Salekhard, được Thượng phụ Kirill thánh hiến năm 2024, là ngôi thánh đường Chính Thống giáo lớn nhất vùng Bắc Cực. Công trình đồ sộ với hai tầng thờ có thể chứa hơn 2.000 giáo dân, trở thành biểu tượng tâm linh mới của thủ phủ Yamal.",
    "Nhà thờ Chúa Hiển Dung là ngôi thánh đường lớn nhất và mới nhất của Salekhard, được mệnh danh là nhà thờ Chính Thống giáo lớn nhất toàn vùng Bắc Cực. Ngày 21-9-2024, đúng lễ Sinh Nhật Đức Mẹ, Thượng phụ Moskva và toàn Nga Kirill đã đích thân thánh hiến ngôi thánh đường - đánh dấu công trình trở thành nhà thờ chính (kafedralny sobor) của giáo phận Salekhard, thay vai trò trung tâm cho nhà thờ Phêrô và Phaolô cổ. Công trình gồm hai nhà thờ chồng lên nhau: nhà thờ trên chứa được khoảng 1.310 người, nhà thờ dưới khoảng 830 người, với năm bàn thờ dâng kính Chúa Hiển Dung, thánh Vasili Mangazeisky, thánh Dimitri Solunsky và lễ Đức Mẹ Bảo Trợ. Kiến trúc mang phong cách nhà thờ Nga truyền thống với những vòm củ hành mạ vàng lấp lánh, nổi bật giữa nền tuyết và bầu trời cực quang. Ngôi đền được xem là 'thành trì tinh thần của phương Bắc', là điểm đến hành hương và tham quan quan trọng bậc nhất của Salekhard hiện nay.",
    [
        "Nhà thờ Chính Thống giáo lớn nhất vùng Bắc Cực, thánh hiến năm 2024.",
        "Được Thượng phụ Kirill đích thân làm phép, trở thành nhà thờ chính toà của Yamal.",
        "Hai tầng thờ chứa hơn 2.000 giáo dân, vòm củ hành mạ vàng đặc trưng.",
    ],
    {
        "hours_vi": "Mở theo giờ lễ, thường từ sáng đến tối. Xem lịch lễ tại chỗ.",
        "ticket_vi": "Vào tự do (công trình tôn giáo).",
        "duration_vi": "Khoảng 30-45 phút.",
        "best_time_vi": "Quanh năm; đặc biệt các đại lễ Chính Thống giáo.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn khi vào. Không gian mới, hiện đại, thích hợp gia đình.",
    },
    [
        {"title": "sobory.ru — Салехард, Собор Преображения Господня", "url": "https://sobory.ru/article/?object=41185"},
        {"title": "Wikipedia (RU) — Преображенский собор (Салехард)", "url": "https://ru.wikipedia.org/wiki/Преображенский_собор_(Салехард)"},
    ],
    ["church", "orthodox", "cathedral", "salekhard", "arctic"],
    maps_text("Кафедральный собор Преображения Господня", "Салехард", "Cathedral of the Transfiguration", "Salekhard", 66.539611, 66.624018),
))

# 3) Мост «Факел» (Салехард) ---------------------------------------------------
RECORDS.append(rec(
    "salekhard-fakel-bridge",
    "Cầu dây văng 'Ngọn Đuốc' (Mốt Fa-cheo) bắc qua sông Shaitanka, Salekhard",
    "Мост «Факел» (Салехард)",
    "Fakel (Torch) Bridge, Salekhard",
    ["bridge"],
    66.536602, 66.600098,
    "Bắc qua sông Shaitanka (Preobrazhenka), nối trung tâm cũ và khu mới của Salekhard, Khu tự trị Yamalo-Nenets, Nga.",
    "Cầu dây văng mang tên 'Ngọn Đuốc', khánh thành tháng 12-2004, là biểu tượng kiến trúc hiện đại của Salekhard. Trên đỉnh cầu có nhà hàng lơ lửng hình chóp nón phát sáng như một ngọn đuốc, khiến đây thành cây cầu độc đáo và điểm ngắm cảnh nổi tiếng.",
    "Cầu 'Факел' (Ngọn Đuốc) là cây cầu dây văng bắc qua sông Shaitanka, khánh thành tháng 12-2004, nối liền phần phố cổ với khu đô thị mới của Salekhard. Điểm đặc biệt khiến cây cầu trở thành biểu tượng của thành phố chính là khối nhà hàng hình chóp nón treo lơ lửng giữa nhịp cầu: về đêm, mái vòm kính và khung lưới mạ vàng của nó phát sáng rực rỡ, trông hệt như một ngọn đuốc đang cháy giữa vùng lãnh nguyên - hình ảnh gợi nhớ ngọn lửa khí đốt, nguồn tài nguyên làm nên sự trù phú của Yamal. Trụ tháp cầu cao khoảng 60 mét. Nhà hàng trên cao cho thực khách vừa thưởng thức ẩm thực vừa phóng tầm mắt bao quát dòng sông và thành phố Bắc Cực. Với du khách, cầu 'Ngọn Đuốc' là một trong những địa điểm 'phải chụp ảnh' ở Salekhard, đặc biệt lộng lẫy vào buổi tối mùa đông khi lên đèn giữa nền tuyết trắng.",
    [
        "Cầu dây văng có nhà hàng hình ngọn đuốc treo lơ lửng giữa nhịp - độc nhất vô nhị.",
        "Khánh thành 2004, trụ tháp cao ~60 m, phát sáng rực rỡ về đêm.",
        "Biểu tượng hiện đại của Salekhard, điểm check-in và ngắm cảnh nổi tiếng.",
    ],
    {
        "hours_vi": "Cầu qua lại tự do suốt ngày đêm; nhà hàng trên cầu có giờ riêng.",
        "ticket_vi": "Đi qua cầu miễn phí; ăn uống tại nhà hàng tính phí.",
        "duration_vi": "Khoảng 15-30 phút ngắm cảnh, chụp ảnh.",
        "best_time_vi": "Buổi tối để ngắm đèn; mùa đông có tuyết rất đẹp.",
        "tips_vi": "Đặt bàn trước nếu muốn ăn tại nhà hàng trên cầu. Mặc ấm khi ra ngắm cảnh mùa lạnh.",
    },
    [
        {"title": "Wikipedia (RU) — Салехардский мост", "url": "https://ru.wikipedia.org/wiki/Салехардский_мост"},
        {"title": "Туристер.Ру — Мост «Факел», Салехард", "url": "https://www.tourister.ru/world/europe/russia/city/salekhard/bridges/31882"},
    ],
    ["bridge", "cable-stayed", "landmark", "salekhard", "restaurant"],
    maps_text("Мост «Факел»", "Салехард", "Fakel Torch Bridge", "Salekhard", 66.536602, 66.600098),
))

# 4) Стела «Романтикам 70-х» (Салехард) ----------------------------------------
RECORDS.append(rec(
    "salekhard-romantics-70s-stele",
    "Đài kỷ niệm 'Những người lãng mạn thập niên 70' (Xtê-la Rô-man-tri-cam), Salekhard",
    "Стела «Романтикам 70-х»",
    "Monument to the Romantics of the 1970s",
    ["monument"],
    66.535847, 66.638384,
    "Phố Brodneva, cách trung tâm Salekhard khoảng 2 km, Khu tự trị Yamalo-Nenets, Nga.",
    "Đài kỷ niệm dựng năm 2001 tôn vinh thế hệ thanh niên xung phong khai phá vùng dầu khí phương Bắc thập niên 1960-70. Khung thép tượng trưng giàn khoan với ngọn lửa khí đốt bập bùng, trên bệ đá granit khắc tên các thành phố dầu khí của Yamal.",
    "Đài 'Романтикам 70-х' (Những người lãng mạn thập niên 70) được dựng năm 2001 theo thiết kế của kiến trúc sư M. E. Tretyak, tưởng niệm cả một thế hệ thanh niên xung phong theo tiếng gọi của Đoàn thanh niên đã lên đường chinh phục vùng đất băng giá Yamal để khai thác dầu khí. Khung thép của đài mô phỏng hình một giàn khoan, ở giữa vươn lên hình tượng ngọn lửa khí đốt (gaz fakel) đang bập bùng - biểu tượng của kỷ nguyên vàng ngành công nghiệp khí đốt Bắc Cực. Trên bệ đá granit khắc tên hàng loạt thành phố của Khu tự trị Yamalo-Nenets, những 'điểm xuất phát' của công cuộc khai thác các mỏ khí khổng lồ. Nằm ven phố Brodneva, cách trung tâm khoảng 2 km, công trình là một biểu tượng gợi nhớ thời kỳ 'lãng mạn' đầy nhiệt huyết khi các đô thị dầu khí như Novy Urengoy, Nadym, Noyabrsk mọc lên giữa lãnh nguyên hoang vu. Đây là điểm dừng ý nghĩa để hiểu về lịch sử phát triển của cả vùng Yamal.",
    [
        "Tôn vinh thế hệ thanh niên xung phong khai phá dầu khí Yamal thập niên 1960-70.",
        "Khung thép hình giàn khoan với ngọn lửa khí đốt biểu tượng.",
        "Bệ đá khắc tên các thành phố dầu khí - điểm khởi đầu của công cuộc khai thác.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do suốt ngày đêm, quanh năm.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15 phút.",
        "best_time_vi": "Quanh năm; buổi tối có chiếu sáng.",
        "tips_vi": "Nằm hơi xa trung tâm, nên đi taxi hoặc kết hợp trên đường vào/ra thành phố.",
    },
    [
        {"title": "Wikimapia — Стела «Романтикам 70-х», Салехард", "url": "http://wikimapia.org/3650339/ru/Стела-«Романтикам-70-х»"},
        {"title": "guidebook.ru — Стела Романтикам 70-х (Салехард)", "url": "https://yam.guidebook.ru/salehard/places/stela-romantikam-70-ih.html"},
    ],
    ["monument", "oil-gas", "soviet", "salekhard", "landmark"],
    maps_text("Стела «Романтикам 70-х»", "Салехард", "Monument to the Romantics of the 1970s", "Salekhard", 66.535847, 66.638384),
))

# 5) Ямальская филармония / Культурно-деловой центр (Салехард) ------------------
RECORDS.append(rec(
    "salekhard-yamal-philharmonic",
    "Nhạc viện Yamal - Trung tâm Văn hoá & Kinh doanh (Ku-lơ-tuốc-nô đê-lô-vôi tsentr), Salekhard",
    "Ямальская филармония (Культурно-деловой центр)",
    "Yamal Philharmonic (Cultural and Business Center)",
    ["theatre"],
    66.534980, 66.608507,
    "Số 1 phố Arkticheskaya, Salekhard (Xa-lê-khác), Khu tự trị Yamalo-Nenets, Nga.",
    "Trung tâm biểu diễn nghệ thuật lớn nhất Yamal - nơi đặt Nhạc viện Yamal với khán phòng hoà nhạc hiện đại. Đây là sân khấu chính đón các đoàn nghệ thuật địa phương lẫn ngôi sao tầm cỡ quốc tế, đồng thời là không gian tổ chức sự kiện văn hoá của thủ phủ Bắc Cực.",
    "Trung tâm Văn hoá & Kinh doanh (Kulturno-delovoy tsentr) trên phố Arkticheskaya là một trong những thiết chế văn hoá lớn nhất Khu tự trị Yamalo-Nenets, hiện là nơi toạ lạc của Nhạc viện Yamal (Yamalskaya filarmoniya). Toà nhà hiện đại này sở hữu khán phòng hoà nhạc rộng, âm thanh chuyên nghiệp cùng hệ thống hậu đài đầy đủ, có thể đón cả những chương trình lớn. Sân khấu nơi đây thường xuyên đón các tập thể nghệ thuật dân gian địa phương biểu diễn dân ca, dân vũ của các dân tộc bản địa Nenets, Khanty, Selkup, xen kẽ với những buổi diễn của các nghệ sĩ, dàn nhạc nổi tiếng từ khắp nước Nga và quốc tế. Tầng trệt còn có khu trưng bày giới thiệu về vùng đất Yamal và các dự án phát triển. Với du khách, đây là điểm đến lý tưởng để thưởng thức đời sống nghệ thuật đương đại của thành phố Bắc Cực và tìm hiểu văn hoá phương Bắc qua các sự kiện, liên hoan diễn ra quanh năm.",
    [
        "Trung tâm biểu diễn nghệ thuật lớn nhất Yamal, nơi đặt Nhạc viện Yamal.",
        "Khán phòng hoà nhạc hiện đại, đón cả đoàn địa phương lẫn ngôi sao quốc tế.",
        "Sân khấu giới thiệu dân ca, dân vũ các dân tộc bản địa phương Bắc.",
    ],
    {
        "hours_vi": "Theo lịch biểu diễn và sự kiện; phòng vé thường mở giờ hành chính.",
        "ticket_vi": "Tuỳ chương trình; xem lịch và mua vé trên trang chính thức.",
        "duration_vi": "Khoảng 1,5-2,5 giờ mỗi buổi diễn.",
        "best_time_vi": "Quanh năm, theo lịch diễn; mùa đông có nhiều sự kiện lễ hội.",
        "tips_vi": "Đặt vé trước cho các chương trình lớn. Nằm gần chợ 'Dary Yamala' và trung tâm.",
    },
    [
        {"title": "Yandex Maps — Ямальская филармония (КДЦ), Салехард", "url": "https://yandex.com/maps/org/yamal_philharmonic_society/1190316295/"},
        {"title": "Culture.RF — Культурно-деловой центр г. Салехарда", "url": "https://www.culture.ru/afisha/yamalo-neneckiy-avtonomnyy-okrug-salehard/institute-21650-kulturno-delovoi-centr-g-salekharda"},
    ],
    ["theatre", "philharmonic", "concert-hall", "salekhard", "culture"],
    maps_org("https://yandex.com/maps/org/yamal_philharmonic_society/1190316295/", "Yamal Philharmonic Cultural Business Center", "Salekhard"),
))

# 6) Национальная библиотека ЯНАО (Салехард) -----------------------------------
RECORDS.append(rec(
    "salekhard-yanao-national-library",
    "Thư viện Quốc gia Yamalo-Nenets (Na-txi-ô-nan-na-ia bi-bli-ô-tê-ca), Salekhard",
    "Национальная библиотека ЯНАО",
    "National Library of Yamalo-Nenets Autonomous Okrug",
    ["other"],
    66.535539, 66.604661,
    "Số 36 phố Chubynina, Salekhard (Xa-lê-khác), Khu tự trị Yamalo-Nenets, Nga.",
    "Thư viện vùng hiện đại của Yamal, thường được xếp vào top 10 điểm tham quan của Salekhard. Không chỉ là kho sách quý về phương Bắc, đây còn là trung tâm văn hoá - giáo dục năng động với công nghệ tự mượn - trả sách, không gian đọc tiện nghi và nhiều hoạt động cộng đồng.",
    "Thư viện Quốc gia Khu tự trị Yamalo-Nenets là thư viện vùng lớn và hiện đại bậc nhất phương Bắc, nằm trên phố Chubynina ở Salekhard. Được người dân và du khách đánh giá cao (nằm trong danh sách 'top 10 điểm đáng đến' của Salekhard theo nhiều bảng xếp hạng du lịch), thư viện không đơn thuần là nơi lưu trữ sách mà là một trung tâm phát triển, học tập và giao lưu văn hoá đúng nghĩa. Nơi đây lưu giữ nhiều đầu sách quý, hiếm về lịch sử, thiên nhiên và các dân tộc bản địa vùng Yamal - nguồn tư liệu hấp dẫn cho ai muốn tìm hiểu sâu về vùng Bắc Cực. Thư viện được trang bị hệ thống tự động cho mượn và trả sách, không gian đọc yên tĩnh, tiện nghi, wifi, cùng lịch hoạt động dày đặc: workshop, trò chơi trí tuệ, chiếu phim tư liệu, gặp gỡ tác giả. Với kiến trúc và nội thất hiện đại, đây là điểm dừng thú vị, ấm áp giữa thành phố băng giá, phù hợp cho cả du khách lẫn gia đình có trẻ nhỏ.",
    [
        "Thư viện vùng hiện đại, được xếp vào top điểm tham quan của Salekhard.",
        "Kho sách quý về lịch sử, thiên nhiên và các dân tộc bản địa Yamal.",
        "Công nghệ tự mượn - trả sách, nhiều hoạt động văn hoá cộng đồng.",
    ],
    {
        "hours_vi": "Mở cửa các ngày trong tuần theo giờ thư viện; xem lịch tại chỗ.",
        "ticket_vi": "Vào tham quan tự do; một số dịch vụ (in, quét) tính phí nhỏ.",
        "duration_vi": "Khoảng 30-60 phút.",
        "best_time_vi": "Quanh năm; điểm trú ấm lý tưởng mùa đông.",
        "tips_vi": "Ghé xem khu sách địa phương về Yamal. Gần nhạc viện và trung tâm thành phố.",
    },
    [
        {"title": "Yandex Maps — Национальная библиотека ЯНАО", "url": "https://yandex.com/maps/org/natsionalnaya_biblioteka_yanao/139396168163/"},
        {"title": "Trang chính thức — nb.yanao.ru", "url": "https://nb.yanao.ru/"},
    ],
    ["library", "culture", "modern", "salekhard", "education"],
    maps_org("https://yandex.com/maps/org/natsionalnaya_biblioteka_yanao/139396168163/", "National Library of Yamalo-Nenets", "Salekhard"),
    official_site="https://nb.yanao.ru/",
))

# 7) Окружной центр национальных культур - ОЦНК (Салехард) ----------------------
RECORDS.append(rec(
    "salekhard-national-cultures-center",
    "Trung tâm Văn hoá các Dân tộc phương Bắc - OTsNK (Ô-cru-nôi tsentr), Salekhard",
    "Окружной центр национальных культур (ОЦНК)",
    "Okrug Center of National Cultures (OTsNK)",
    ["other"],
    66.529039, 66.624964,
    "Số 74 phố Respubliki, Salekhard (Xa-lê-khác), Khu tự trị Yamalo-Nenets, Nga.",
    "Nhà văn hoá vùng chuyên bảo tồn và trình diễn văn hoá các dân tộc bản địa Yamal (Nenets, Khanty, Selkup, Komi). Nơi đây có rạp chiếu phim, khán phòng hoà nhạc, thường xuyên tổ chức lễ hội dân tộc, biểu diễn dân ca - dân vũ và trưng bày trang phục, thủ công truyền thống.",
    "Trung tâm Văn hoá các Dân tộc phương Bắc (Okruzhnoy tsentr natsionalnykh kultur, viết tắt OTsNK) trên phố Respubliki là một trong những thiết chế văn hoá được yêu thích nhất Salekhard, chuyên gìn giữ và lan toả bản sắc của các dân tộc bản địa vùng Yamal như Nenets, Khanty, Selkup, Komi. Toà nhà tập hợp nhiều chức năng: khán phòng hoà nhạc, rạp chiếu phim, sảnh triển lãm và các câu lạc bộ nghệ thuật dân gian. Nơi đây là 'ngôi nhà' của nhiều tập thể nghệ thuật dân tộc nổi tiếng trong vùng, thường xuyên dàn dựng các chương trình dân ca, dân vũ rực rỡ sắc màu phương Bắc, cùng những dịp lễ hội truyền thống. Hành lang trung tâm còn có phòng trưng bày ảnh giới thiệu các tập thể nghệ thuật với trang phục thổ cẩm lộng lẫy, cùng quầy bán đồ lưu niệm, thủ công địa phương. Đây là điểm đến tuyệt vời để du khách chạm vào 'linh hồn' văn hoá bản địa Yamal - điều làm nên nét riêng có của vùng đất chăn tuần lộc này.",
    [
        "Nhà văn hoá bảo tồn bản sắc các dân tộc bản địa Nenets, Khanty, Selkup, Komi.",
        "Có rạp chiếu phim, khán phòng hoà nhạc, sảnh triển lãm và quầy lưu niệm.",
        "Thường xuyên tổ chức lễ hội dân tộc, biểu diễn dân ca - dân vũ phương Bắc.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày; sự kiện theo lịch riêng (thường đến 23h).",
        "ticket_vi": "Vào tham quan tự do; vé cho suất chiếu/biểu diễn tuỳ chương trình.",
        "duration_vi": "Khoảng 45-90 phút.",
        "best_time_vi": "Quanh năm; đặc biệt dịp lễ hội dân tộc.",
        "tips_vi": "Hỏi lịch biểu diễn dân gian để canh xem. Có bán đồ lưu niệm bản địa đẹp.",
    },
    [
        {"title": "Yandex Maps — Окружной центр национальных культур", "url": "https://yandex.com/maps/org/okruzhnoy_tsentr_natsionalnykh_kultur/1225227403/"},
        {"title": "Trang chính thức — ocnk.yanao.ru", "url": "https://ocnk.yanao.ru/"},
    ],
    ["culture", "indigenous", "nenets", "khanty", "salekhard"],
    maps_org("https://yandex.com/maps/org/okruzhnoy_tsentr_natsionalnykh_kultur/1225227403/", "Okrug Center of National Cultures", "Salekhard"),
    official_site="https://ocnk.yanao.ru/",
))

# 8) ЦКиС «Геолог» (Салехард) --------------------------------------------------
RECORDS.append(rec(
    "salekhard-geolog-culture-sport-center",
    "Trung tâm Văn hoá & Thể thao 'Geolog' (Tsentr Ku-lơ-tu-ri i xpo-rơ-ta Ghê-ô-lốc), Salekhard",
    "Центр культуры и спорта «Геолог»",
    "Geolog Culture and Sport Center",
    ["other"],
    66.536090, 66.623957,
    "Số 31 phố Matrosova, Salekhard (Xa-lê-khác), Khu tự trị Yamalo-Nenets, Nga.",
    "Tổ hợp văn hoá - thể thao trung tâm của Salekhard, kết hợp khán phòng biểu diễn, sân khấu kịch thiếu nhi, phòng tập và bể bơi. Đây là điểm sinh hoạt cộng đồng sôi động, nơi diễn ra nhiều buổi diễn, liên hoan và sự kiện quanh năm.",
    "Trung tâm Văn hoá & Thể thao 'Geolog' là một tổ hợp đa năng nằm ngay trung tâm Salekhard, kết hợp cả chức năng văn hoá lẫn thể thao. Về mặt văn hoá, nơi đây có khán phòng dàn dựng các vở kịch, chương trình nghệ thuật, đặc biệt là những buổi diễn dịp năm mới, lễ hội cho thiếu nhi và gia đình với sân khấu, phục trang được đầu tư công phu, được người dân đánh giá cao. Về thể thao, trung tâm có phòng tập đa dạng thiết bị và bể bơi phục vụ cả gia đình. Nhờ vị trí trung tâm và hoạt động phong phú, 'Geolog' là một trong những điểm hẹn văn hoá - giải trí quen thuộc bậc nhất của cư dân thủ phủ Yamal. Với du khách, đây là nơi có thể bắt gặp không khí sinh hoạt đời thường sôi động của một thành phố Bắc Cực, hoặc kết hợp thư giãn, vận động trong hành trình khám phá Salekhard.",
    [
        "Tổ hợp văn hoá - thể thao trung tâm, có khán phòng, phòng tập và bể bơi.",
        "Nổi tiếng với các chương trình nghệ thuật, kịch thiếu nhi dịp lễ, năm mới.",
        "Điểm sinh hoạt cộng đồng sôi động bậc nhất Salekhard.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày, thường đến 23h; sự kiện theo lịch riêng.",
        "ticket_vi": "Vé tuỳ chương trình/dịch vụ; dịch vụ thể thao và bể bơi tính phí.",
        "duration_vi": "Khoảng 1-2 giờ.",
        "best_time_vi": "Quanh năm; nhiều sự kiện mùa đông và dịp năm mới.",
        "tips_vi": "Xem trước lịch biểu diễn trên trang geolog89.ru. Có bể bơi cho gia đình.",
    },
    [
        {"title": "Yandex Maps — ЦКиС «Геолог», Салехард", "url": "https://yandex.com/maps/org/munitsipalnoye_avtonomnoye_uchrezhdeniye_kultury_tsentra_kultury_i_sporta_geolog/1044091176/"},
        {"title": "Trang chính thức — geolog89.ru", "url": "http://geolog89.ru/"},
    ],
    ["culture", "sport", "community", "salekhard", "events"],
    maps_org("https://yandex.com/maps/org/munitsipalnoye_avtonomnoye_uchrezhdeniye_kultury_tsentra_kultury_i_sporta_geolog/1044091176/", "Geolog Culture and Sport Center", "Salekhard"),
    official_site="http://geolog89.ru/",
))

# 9) Богоявленский собор (Новый Уренгой) ---------------------------------------
RECORDS.append(rec(
    "novy-urengoy-epiphany-cathedral",
    "Nhà thờ Chính toà Chúa Hiển Linh (Xô-bo Bô-ga-i-vlen-xki), Novy Urengoy",
    "Собор Богоявления Господня (Новый Уренгой)",
    "Cathedral of the Epiphany (Novy Urengoy)",
    ["church"],
    66.082739, 76.657870,
    "Số 1 vi khu Optimistov, Novy Urengoy (Nô-vư U-ren-gôi), Khu tự trị Yamalo-Nenets, Nga.",
    "Nhà thờ chính toà lớn nhất của Novy Urengoy - 'thủ đô khí đốt' của nước Nga, khánh thành năm 2014 sau 7 năm xây dựng. Ngôi đền hai tầng cao 36 m, sức chứa 650 người, là biểu tượng tâm linh nổi bật giữa đô thị công nghiệp trẻ ở Bắc Cực.",
    "Nhà thờ Chúa Hiển Linh là ngôi thánh đường chính toà lớn nhất của Novy Urengoy - thành phố được mệnh danh là 'thủ đô khí đốt' của nước Nga nhờ nằm cạnh những mỏ khí khổng lồ. Công trình được xây dựng ròng rã suốt 7 năm và khánh thành ngày 28-12-2014. Ngôi đền hai tầng cao khoảng 36 mét, sức chứa tới 650 giáo dân, mang kiến trúc Chính Thống giáo Nga truyền thống với các vòm củ hành mạ vàng lấp lánh nổi bật giữa những dãy nhà cao tầng của đô thị dầu khí. Là trung tâm của giáo phận Salekhard tại khu vực phía đông vùng Yamal, nhà thờ không chỉ là nơi thờ phụng mà còn có trường trung học Chính Thống giáo, khuôn viên được chăm chút. Giữa một thành phố công nghiệp trẻ mọc lên từ lãnh nguyên hoang vu, ngôi thánh đường vàng son này trở thành điểm nhấn kiến trúc và tinh thần, là nơi du khách ghé thăm để cảm nhận đời sống văn hoá - tâm linh của cư dân Novy Urengoy.",
    [
        "Nhà thờ chính toà lớn nhất Novy Urengoy - 'thủ đô khí đốt' của Nga.",
        "Khánh thành 2014, cao 36 m, hai tầng thờ chứa 650 người.",
        "Vòm củ hành mạ vàng nổi bật giữa đô thị dầu khí trẻ ở Bắc Cực.",
    ],
    {
        "hours_vi": "Mở theo giờ lễ, thường sáng đến tối. Xem lịch lễ tại chỗ.",
        "ticket_vi": "Vào tự do (công trình tôn giáo).",
        "duration_vi": "Khoảng 20-40 phút.",
        "best_time_vi": "Quanh năm; đẹp khi có tuyết và dịp đại lễ.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn. Có khuôn viên và trường Chính Thống giáo bên cạnh.",
    },
    [
        {"title": "Yandex Maps — Собор Богоявления Господня, Новый Уренгой", "url": "https://yandex.com/maps/org/pravoslavny_bogoyavlensky_sobor_russkoy_pravoslavnoy_tserkvi_moskovskogo_patriarkhata/1299197272/"},
        {"title": "sobory.ru — Новый Уренгой, Собор Богоявления Господня", "url": "https://sobory.ru/article/?object=24898"},
    ],
    ["church", "orthodox", "cathedral", "novy-urengoy", "gas-capital"],
    maps_org("https://yandex.com/maps/org/pravoslavny_bogoyavlensky_sobor_russkoy_pravoslavnoy_tserkvi_moskovskogo_patriarkhata/1299197272/", "Cathedral of the Epiphany", "Novy Urengoy"),
))

# 10) Церковь Серафима Саровского (Новый Уренгой) ------------------------------
RECORDS.append(rec(
    "novy-urengoy-seraphim-church",
    "Nhà thờ Thánh Seraphim thành Sarov (Tsê-rơ-cốp Xê-ra-phi-ma), Novy Urengoy",
    "Церковь Серафима Саровского (Новый Уренгой)",
    "Church of Saint Seraphim of Sarov (Novy Urengoy)",
    ["church"],
    66.109333, 76.678980,
    "Số 2 phố Zakharenkova, Novy Urengoy (Nô-vư U-ren-gôi), Khu tự trị Yamalo-Nenets, Nga.",
    "Ngôi nhà thờ đầu tiên của Novy Urengoy, gắn bó với nhiều thế hệ cư dân thành phố. Từng bị hoả hoạn thiêu rụi và được phục dựng nhanh chóng, nhà thờ Thánh Seraphim nay là một điểm tâm linh ấm cúng, khuôn viên xanh mát hiếm có ở vùng Bắc Cực.",
    "Nhà thờ Thánh Seraphim thành Sarov là ngôi nhà thờ đầu tiên được xây dựng tại Novy Urengoy, vì thế mang ý nghĩa đặc biệt trong lòng cư dân thành phố dầu khí này. Nhiều gia đình gắn bó với ngôi đền qua các nghi lễ hôn phối, rửa tội suốt nhiều thế hệ. Ngôi nhà thờ từng chịu một trận hoả hoạn nghiêm trọng nhưng đã được phục dựng hoàn chỉnh trong thời gian ngắn kỷ lục, thể hiện sự gắn kết của cộng đồng. Ngày nay, nhà thờ Thánh Seraphim là một không gian tôn giáo ấm cúng, tĩnh lặng, với khuôn viên được chăm chút, có cả quầy bán bánh mì và sản phẩm nhà thờ. Người dân yêu thích tìm về đây để cầu nguyện và tìm sự an yên. Giữa một đô thị công nghiệp trẻ giữa lãnh nguyên, ngôi đền nhỏ này lưu giữ chiều sâu lịch sử và tình cảm của những thế hệ đầu tiên đã đến khai phá vùng Urengoy.",
    [
        "Ngôi nhà thờ đầu tiên của Novy Urengoy, gắn với nhiều thế hệ cư dân.",
        "Từng bị hoả hoạn và được phục dựng nhanh chóng nhờ cộng đồng.",
        "Không gian tôn giáo ấm cúng với khuôn viên xanh mát hiếm có ở Bắc Cực.",
    ],
    {
        "hours_vi": "Mở theo giờ lễ, thường sáng đến tối.",
        "ticket_vi": "Vào tự do (công trình tôn giáo).",
        "duration_vi": "Khoảng 15-30 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn. Có quầy bánh và sản phẩm nhà thờ.",
    },
    [
        {"title": "Yandex Maps — Церковь Серафима Саровского, Новый Уренгой", "url": "https://yandex.com/maps/org/church_of_saint_seraphim_of_sarov/1352635488/"},
        {"title": "Салехардская епархия — yamalrpc.ru", "url": "http://yamalrpc.ru/"},
    ],
    ["church", "orthodox", "novy-urengoy", "first-church", "restored"],
    maps_org("https://yandex.com/maps/org/church_of_saint_seraphim_of_sarov/1352635488/", "Church of Saint Seraphim of Sarov", "Novy Urengoy"),
))

# 11) Церковь Николая Чудотворца (Надым) ---------------------------------------
RECORDS.append(rec(
    "nadym-st-nicholas-church",
    "Nhà thờ Thánh Nikolai (Tsê-rơ-cốp Ni-cô-la-ia Chu-đô-tvo-rơ-tsa), Nadym",
    "Церковь Николая Чудотворца (Надым)",
    "Church of St. Nicholas the Wonderworker (Nadym)",
    ["church"],
    65.533311, 72.512695,
    "Đường Parkovy proezd, Nadym (Na-đưm), Khu tự trị Yamalo-Nenets, Nga.",
    "Ngôi nhà thờ chính của Nadym, xây năm 1994-1998 và được đích thân Thượng phụ Aleksi II thánh hiến năm 1998. Đây là trung tâm tâm linh của thành phố dầu khí bên bờ sông Nadym, gắn với thời kỳ khai phá các mỏ khí khổng lồ Medvezhye, Urengoy.",
    "Nhà thờ Thánh Nikolai (Nicholas) là ngôi thánh đường chính của Nadym - một trong những đô thị dầu khí đầu tiên của Yamal, ra đời từ thập niên 1970 để phục vụ khai thác mỏ khí Medvezhye và tuyến ống dẫn khí. Công trình được xây dựng trong các năm 1994-1998 và long trọng thánh hiến ngày 3-9-1998, đặc biệt bởi chính Thượng phụ Moskva và toàn Nga Aleksi II - một vinh dự lớn cho thành phố trẻ vùng cực bắc. Mang kiến trúc Chính Thống giáo Nga với các vòm củ hành và tháp chuông, nhà thờ là trung tâm đời sống đức tin của cư dân Nadym, nơi diễn ra các nghi lễ và sinh hoạt cộng đồng quanh năm. Toạ lạc gần khu công viên trung tâm, ngôi đền là điểm nhấn tinh thần yên bình giữa nhịp sống công nghiệp, đồng thời là một điểm ghé thăm ý nghĩa để hiểu về lịch sử hình thành các thành phố khí đốt trên vùng lãnh nguyên Yamal.",
    [
        "Nhà thờ chính của Nadym, xây 1994-1998, thánh hiến 1998.",
        "Được đích thân Thượng phụ Aleksi II làm phép - vinh dự hiếm có.",
        "Trung tâm tâm linh của đô thị dầu khí bên sông Nadym.",
    ],
    {
        "hours_vi": "Mở theo giờ lễ, thường sáng đến tối.",
        "ticket_vi": "Vào tự do (công trình tôn giáo).",
        "duration_vi": "Khoảng 20-30 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn. Gần công viên trung tâm Nadym.",
    },
    [
        {"title": "sobory.ru — Надым, Церковь Николая Чудотворца", "url": "https://sobory.ru/article/?object=11710"},
        {"title": "Приход Надыма — nadym.cerkov.ru", "url": "https://nadym.cerkov.ru/"},
    ],
    ["church", "orthodox", "nadym", "oil-gas-town", "1998"],
    maps_text("Церковь Николая Чудотворца", "Надым", "Church of St Nicholas", "Nadym", 65.533311, 72.512695),
))

# 12) Музей истории и археологии города Надыма ---------------------------------
RECORDS.append(rec(
    "nadym-history-archaeology-museum",
    "Bảo tàng Lịch sử & Khảo cổ thành phố Nadym (Mu-dây i-xtô-ri i ar-khê-ô-lô-ghi)",
    "Музей истории и археологии города Надыма",
    "Museum of History and Archaeology of Nadym",
    ["museum"],
    65.530248, 72.518387,
    "Số 11 đại lộ Leningradsky, Nadym (Na-đưm), Khu tự trị Yamalo-Nenets, Nga.",
    "Bảo tàng trung tâm của Nadym, nổi bật với trưng bày về 'Thành cổ Nadym' (Nadymskoye gorodishe) - di chỉ khảo cổ độc đáo bảo tồn gỗ trong băng vĩnh cửu, cùng bộ sưu tập di tích tuyến 'Đường sắt Chết' 501. Điểm đến hàng đầu để hiểu lịch sử vùng lãnh nguyên.",
    "Bảo tàng Lịch sử & Khảo cổ thành phố Nadym là bảo tàng trung tâm và hấp dẫn nhất của thành phố, thành lập năm 2003. Điểm nhấn nổi tiếng nhất là trưng bày về 'Thành cổ Nadym' (Nadymskoye gorodishe) - một di chỉ khảo cổ độc đáo nơi lớp băng vĩnh cửu đã bảo tồn nguyên vẹn các cấu trúc gỗ, đồ dùng bằng gỗ, xương và da của cư dân bản địa qua nhiều thế kỷ; cách trưng bày ở đây được giới chuyên môn đánh giá không thua kém Bảo tàng Gỗ khảo cổ ở Sviyazhsk. Bảo tàng còn lưu giữ bộ sưu tập quý về tuyến 'Đường sắt Chết' (stройka 501, Salekhard-Igarka) với các đoạn ray, hiện vật của công trình bi tráng thời Stalin. Không gian trưng bày sinh động, đội ngũ hướng dẫn viên - nghiên cứu viên tâm huyết, kể chuyện cuốn hút về vùng đất khắc nghiệt mà giàu bản sắc này. Đây là điểm đến 'phải ghé' để hiểu chiều sâu lịch sử, khảo cổ và văn hoá của cả vùng Nadym và Yamal.",
    [
        "Trưng bày 'Thành cổ Nadym' - di chỉ gỗ bảo tồn kỳ diệu trong băng vĩnh cửu.",
        "Bộ sưu tập di tích 'Đường sắt Chết' (stройka 501) thời Stalin.",
        "Hướng dẫn viên - nghiên cứu viên tâm huyết, trưng bày sinh động.",
    ],
    {
        "hours_vi": "Thứ Ba-Chủ nhật, thường 10h-19h (thứ Năm đến 21h); thứ Hai đóng cửa.",
        "ticket_vi": "Vé khoảng 150-2.000 ₽ tuỳ loại (có tour hướng dẫn).",
        "duration_vi": "Khoảng 1-2 giờ.",
        "best_time_vi": "Quanh năm; lý tưởng cho ngày lạnh.",
        "tips_vi": "Nên mua vé kèm hướng dẫn để nghe kể về Thành cổ Nadym và tuyến 501.",
    },
    [
        {"title": "Yandex Maps — Музей истории и археологии города Надыма", "url": "https://yandex.com/maps/org/nadym_museum_of_history_and_archeology/1068949355/"},
        {"title": "Culture.RF — Музей истории и археологии г. Надыма", "url": "https://www.culture.ru/institutes/11337/muzei-istorii-i-arkheologii-g-nadyma"},
    ],
    ["museum", "archaeology", "nadym", "gorodishe", "permafrost"],
    maps_org("https://yandex.com/maps/org/nadym_museum_of_history_and_archeology/1068949355/", "Museum of History and Archaeology of Nadym", "Nadym"),
    official_site="https://museum.yanao.ru/",
))

# 13) Дом природы (Надым) ------------------------------------------------------
RECORDS.append(rec(
    "nadym-dom-prirody-museum",
    "Bảo tàng 'Ngôi nhà Thiên nhiên' (Đôm pri-rô-đư), Nadym",
    "Дом природы (Надым)",
    "Dom Prirody (House of Nature), Nadym",
    ["museum"],
    65.535004, 72.517471,
    "Số 1 đường Parkovy proezd, Nadym (Na-đưm), Khu tự trị Yamalo-Nenets, Nga.",
    "Bảo tàng thiên nhiên - sinh thái độc đáo của Nadym, có phòng động vật sống, khu thuỷ sinh và một lều chum (chum) truyền thống nơi khách được mời trà và nghe kể về đời sống người bản địa. Điểm đến ấm áp, thân thiện, được cả trẻ em lẫn người lớn yêu thích.",
    "Bảo tàng 'Ngôi nhà Thiên nhiên' (Dom prirody) ở Nadym, thành lập ngày 19-5-1987, là một trung tâm giáo dục sinh thái và văn hoá đặc sắc của vùng phương Bắc; năm 2007 trở thành chi nhánh của Bảo tàng Lịch sử & Khảo cổ thành phố Nadym. Điểm hấp dẫn nhất là 'phòng sống' với nhiều loài chim, thú và khu thuỷ sinh riêng - nơi trẻ em có thể quan sát, thậm chí cho ăn và chạm vào một số con vật (từ rùa đến những loài côn trùng lạ). Trong khuôn viên còn dựng một chiếc lều chum (chum) truyền thống của người Nenets, nơi khách được mời uống trà và nghe kể về phong tục, nếp sống của dân tộc chăn tuần lộc bản địa. Nơi đây giới thiệu tổng hợp cả lịch sử, phong tục và các giá trị tự nhiên - khoa học của vùng Yamal, với đội ngũ nhân viên yêu nghề, chăm sóc động vật chu đáo. Đây là điểm đến ấm cúng, giàu tính trải nghiệm, đặc biệt phù hợp cho các gia đình có trẻ nhỏ khi đến Nadym.",
    [
        "Bảo tàng sinh thái có phòng động vật sống và khu thuỷ sinh cho trẻ trải nghiệm.",
        "Có lều chum truyền thống, mời trà và giới thiệu văn hoá người Nenets.",
        "Trung tâm giáo dục sinh thái lâu đời (từ 1987), thân thiện gia đình.",
    ],
    {
        "hours_vi": "Thường mở Thứ Ba-Chủ nhật; xem lịch tại chỗ. Lều chum mở theo ngày nhất định.",
        "ticket_vi": "Vé tham quan có thu phí (mức phổ thông).",
        "duration_vi": "Khoảng 1-1,5 giờ.",
        "best_time_vi": "Quanh năm; rất hợp cho trẻ em ngày lạnh.",
        "tips_vi": "Hỏi trước lịch mở lều chum nếu muốn trải nghiệm trà và kể chuyện bản địa.",
    },
    [
        {"title": "Yandex Maps — Дом природы, Надым", "url": "https://yandex.com/maps/org/dom_prirody/1044772539/"},
        {"title": "Музей Надыма — museum.yanao.ru", "url": "https://museum.yanao.ru/"},
    ],
    ["museum", "nature", "nadym", "ecology", "family"],
    maps_org("https://yandex.com/maps/org/dom_prirody/1044772539/", "Dom Prirody House of Nature", "Nadym"),
))

# 14) Экспозиция «История строительства города» / 501-я стройка (Надым) --------
RECORDS.append(rec(
    "nadym-city-construction-exhibition",
    "Trưng bày 'Lịch sử xây dựng thành phố' & di tích 'Đường sắt Chết' 501, Nadym",
    "Экспозиционный зал «История строительства города» (Надым)",
    "'History of the City's Construction' Exhibition Hall (Nadym)",
    ["museum"],
    65.535645, 72.524640,
    "Số 12/3 phố Zvereva, Nadym (Na-đưm), Khu tự trị Yamalo-Nenets, Nga (tham quan theo hẹn trước).",
    "Sảnh trưng bày chuyên đề (chi nhánh của Bảo tàng Nadym) kể câu chuyện dựng thành phố dầu khí giữa lãnh nguyên, nổi bật với chuyên đề chấn động về 'Đường sắt Chết' - tuyến 501 do tù nhân Gulag xây thời Stalin. Có bản đồ đồng đúc trên sàn và sa bàn thành phố 'lơ lửng'.",
    "Sảnh trưng bày 'Lịch sử xây dựng thành phố' là một chi nhánh chuyên đề của Bảo tàng Lịch sử & Khảo cổ Nadym, mở từ năm 2002, tái hiện quá trình dựng nên một đô thị dầu khí hiện đại giữa vùng lãnh nguyên băng giá. Điểm gây ấn tượng mạnh nhất là chuyên đề về 'Đường sắt Chết' (Mёртвая дорога) - tuyến đường sắt xuyên cực Salekhard-Igarka (công trường số 501/503) mà chính quyền Stalin cho khởi công năm 1947 bằng sức lao động của hàng chục nghìn tù nhân trại cải tạo, rồi bỏ dở sau khi Stalin qua đời năm 1953. Trưng bày giúp người xem hình dung số phận bi thảm của những người tù và một trong những công trình khắc nghiệt, ám ảnh nhất lịch sử Xô Viết. Không gian còn có bản đồ vùng và thành phố bằng đồng đúc đặt trên sàn cùng sa bàn thành phố như 'lơ lửng' trong không trung, được dàn dựng công phu. Đây là điểm đến sâu lắng để hiểu cả trang sử hào hùng lẫn bi tráng của vùng Nadym và tuyến 501 huyền thoại.",
    [
        "Chuyên đề chấn động về 'Đường sắt Chết' 501 - công trình Gulag thời Stalin.",
        "Bản đồ đồng đúc trên sàn và sa bàn thành phố 'lơ lửng' dàn dựng công phu.",
        "Kể lại quá trình dựng đô thị dầu khí giữa lãnh nguyên Yamal.",
    ],
    {
        "hours_vi": "Tham quan theo hẹn trước (liên hệ Bảo tàng Nadym).",
        "ticket_vi": "Vé khoảng 100-2.000 ₽ tuỳ loại (có tour hướng dẫn).",
        "duration_vi": "Khoảng 45-90 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Nên đặt lịch và tour hướng dẫn trước để nghe trọn câu chuyện tuyến 501.",
    },
    [
        {"title": "Yandex Maps — Экспозиция «История строительства города», Надым", "url": "https://yandex.com/maps/org/ekspozitsionny_zal_muzeya_istorii_i_arkheologii_goroda_nadyma_istoriya_stroitelstva_goroda/131477632141/"},
        {"title": "Wikipedia (RU) — Трансполярная магистраль (Мёртвая дорога)", "url": "https://ru.wikipedia.org/wiki/Трансполярная_магистраль"},
    ],
    ["museum", "dead-road", "gulag", "nadym", "history"],
    maps_org("https://yandex.com/maps/org/ekspozitsionny_zal_muzeya_istorii_i_arkheologii_goroda_nadyma_istoriya_stroitelstva_goroda/131477632141/", "History of City Construction Exhibition", "Nadym"),
    official_site="https://museum.yanao.ru/",
))

# 15) Памятник комару (Ноябрьск) -----------------------------------------------
RECORDS.append(rec(
    "noyabrsk-mosquito-monument",
    "Tượng đài Con Muỗi (Pa-mi-át-nhic ca-ma-ru), Noyabrsk",
    "Памятник комару (Ноябрьск)",
    "Mosquito Monument (Noyabrsk)",
    ["monument"],
    63.190724, 75.551709,
    "Khu vực gần thành phố Noyabrsk (Nô-i-áp-rơ-xcơ), Khu tự trị Yamalo-Nenets, Nga.",
    "Tượng đài hài hước và độc đáo tôn vinh (hay 'than phiền') về loài muỗi - đặc sản khét tiếng của mùa hè lãnh nguyên. Dựng năm 2006 bằng khung kim loại, con muỗi khổng lồ cao khoảng 1,7 m đã trở thành biểu tượng vui nhộn và điểm check-in được yêu thích của Noyabrsk.",
    "Tượng đài Con Muỗi ở Noyabrsk là một trong những công trình điêu khắc hài hước và được nhắc đến nhiều nhất của cả vùng Yamal. Bất cứ ai từng trải qua mùa hè lãnh nguyên đều 'thấm' nỗi ám ảnh muỗi và côn trùng hút máu dày đặc, nên người dân Noyabrsk đã dựng hẳn một tượng đài để 'vinh danh' vị khách không mời này. Tác phẩm khánh thành năm 2006 theo sáng kiến của công nhân trạm nén khí, do nhà điêu khắc địa phương Valeri Chaly thực hiện, làm từ khung kim loại, với con muỗi cao khoảng 1,7 mét và sải cánh rộng chừng ba mét. Vừa hài hước vừa mang tính biểu tượng cho khí hậu khắc nghiệt của phương Bắc, tượng đài nhanh chóng trở thành điểm check-in được du khách thích thú và là 'thương hiệu' vui nhộn của Noyabrsk. Đây là minh chứng cho tinh thần lạc quan, biết cười với nghịch cảnh của cư dân vùng đất băng giá này.",
    [
        "Tượng đài hài hước tôn vinh loài muỗi - 'đặc sản' mùa hè lãnh nguyên.",
        "Dựng 2006, khung kim loại, con muỗi cao ~1,7 m, sải cánh ~3 m.",
        "Biểu tượng vui nhộn và điểm check-in được yêu thích của Noyabrsk.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do suốt ngày đêm, quanh năm.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10-15 phút.",
        "best_time_vi": "Quanh năm; mùa hè để 'cảm nhận' đủ vị muỗi Bắc Cực.",
        "tips_vi": "Mang thuốc chống côn trùng nếu đến mùa hè. Điểm chụp ảnh vui nhộn.",
    },
    [
        {"title": "2GIS — Памятник комару, Ноябрьск", "url": "https://2gis.ru/noyabrsk/geo/14496657085300750"},
        {"title": "Туристер.Ру — Памятник комару в Ноябрьске", "url": "https://www.tourister.ru/world/europe/russia/city/noyabrsk/placeofinterest/31852"},
    ],
    ["monument", "quirky", "mosquito", "noyabrsk", "photo-spot"],
    maps_text("Памятник комару", "Ноябрьск", "Mosquito Monument", "Noyabrsk", 63.190724, 75.551709),
))

# 16) Музейный ресурсный центр (Ноябрьск) --------------------------------------
RECORDS.append(rec(
    "noyabrsk-museum-resource-center",
    "Trung tâm Bảo tàng - Tài nguyên (Mu-dây-nưi rê-xuốc-nưi tsentr), Noyabrsk",
    "Музейный ресурсный центр (Ноябрьск)",
    "Museum Resource Center (Noyabrsk)",
    ["museum"],
    63.199416, 75.463443,
    "Số 82 phố Sovetskaya, Noyabrsk (Nô-i-áp-rơ-xcơ), Khu tự trị Yamalo-Nenets, Nga.",
    "Bảo tàng đa năng của Noyabrsk, giới thiệu lịch sử khai phá dầu khí, thiên nhiên và văn hoá bản địa vùng nam Yamal. Là trung tâm văn hoá - giáo dục năng động với các triển lãm, workshop và hoạt động cộng đồng thường xuyên.",
    "Trung tâm Bảo tàng - Tài nguyên là bảo tàng chính của Noyabrsk, thành phố dầu khí trẻ nằm ở cực nam Khu tự trị Yamalo-Nenets. Bảo tàng giới thiệu tổng hợp về quá trình hình thành và phát triển thành phố gắn với công cuộc khai thác các mỏ dầu khí, về thiên nhiên vùng taiga - lãnh nguyên phương Nam Yamal, cũng như đời sống, văn hoá của các dân tộc bản địa. Không chỉ là nơi trưng bày cố định, đây còn là một 'trung tâm tài nguyên' năng động, thường xuyên tổ chức các triển lãm chuyên đề luân phiên, buổi học ngoại khoá, workshop sáng tạo, trò chơi tương tác cho cả trẻ em và người lớn. Với đội ngũ cán bộ nhiệt tình và cách làm bảo tàng hiện đại, nơi đây là điểm đến văn hoá đáng chú ý của Noyabrsk, giúp du khách hiểu thêm về một lát cắt khác của vùng Yamal - những đô thị công nghiệp trẻ giữa rừng taiga phương Bắc.",
    [
        "Bảo tàng chính của Noyabrsk, giới thiệu lịch sử dầu khí và văn hoá nam Yamal.",
        "Trung tâm 'tài nguyên' năng động với triển lãm luân phiên, workshop.",
        "Cách làm bảo tàng hiện đại, tương tác, phù hợp cả gia đình.",
    ],
    {
        "hours_vi": "Thứ Ba-Chủ nhật 10h-18h (không nghỉ trưa); thứ Hai đóng cửa.",
        "ticket_vi": "Vé tham quan mức phổ thông; một số sự kiện riêng.",
        "duration_vi": "Khoảng 1-1,5 giờ.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Xem trước lịch triển lãm chuyên đề để canh chương trình hay.",
    },
    [
        {"title": "Culture.RF — Музейный ресурсный центр, г. Ноябрьск", "url": "https://www.culture.ru/institutes/12078/muzeinyi-resursnyi-centr-g-noyabrsk"},
        {"title": "Museum.ru — Музейный ресурсный центр (Ноябрьск)", "url": "http://www.museum.ru/M1854"},
    ],
    ["museum", "noyabrsk", "oil-gas", "local-history", "culture"],
    maps_text("Музейный ресурсный центр", "Ноябрьск", "Museum Resource Center", "Noyabrsk", 63.199416, 75.463443),
))

# 17) Храм Архистратига Михаила (Ноябрьск) -------------------------------------
RECORDS.append(rec(
    "noyabrsk-archangel-michael-church",
    "Nhà thờ Tổng lãnh Thiên thần Micae (Khram Ar-khi-xtra-ti-ga Mi-kha-i-la), Noyabrsk",
    "Храм Архистратига Михаила (Ноябрьск)",
    "Church of the Archangel Michael (Noyabrsk)",
    ["church"],
    63.200847, 75.444433,
    "Số 72 đại lộ Mira, khu ОГЦ-1, Noyabrsk (Nô-i-áp-rơ-xcơ), Khu tự trị Yamalo-Nenets, Nga.",
    "Ngôi nhà thờ Chính Thống giáo duy nhất và là trung tâm tâm linh của Noyabrsk, thánh hiến năm 2005. Toà thánh đường bốn tầng khang trang là điểm nhấn kiến trúc và đời sống đức tin của thành phố dầu khí phương nam Yamal.",
    "Nhà thờ Tổng lãnh Thiên thần Micae là ngôi thánh đường Chính Thống giáo duy nhất của Noyabrsk và là trung tâm đời sống đức tin của cả thành phố. Công trình được thánh hiến năm 2005, mang kiến trúc Chính Thống giáo Nga với các vòm củ hành và tháp chuông đặc trưng, nổi bật giữa các khu dân cư của đô thị dầu khí trẻ. Toà nhà thờ quy mô lớn (bốn tầng) không chỉ là nơi cử hành các nghi lễ, thánh lễ mà còn có các hoạt động mục vụ, thiện nguyện, giáo dục cho cộng đồng, và được thiết kế thân thiện với người khuyết tật. Là điểm quy tụ tinh thần của cư dân Noyabrsk giữa vùng taiga phương Bắc, ngôi đền cũng là một điểm ghé thăm đáng chú ý cho du khách muốn cảm nhận nhịp sống văn hoá - tâm linh của các thành phố mới trên vùng đất Yamal giàu dầu khí.",
    [
        "Nhà thờ Chính Thống giáo duy nhất của Noyabrsk, thánh hiến năm 2005.",
        "Toà thánh đường bốn tầng khang trang, vòm củ hành đặc trưng.",
        "Trung tâm đời sống đức tin của thành phố dầu khí nam Yamal.",
    ],
    {
        "hours_vi": "Mở theo giờ lễ; ngày thường lễ sáng 8h30, chiều 17h.",
        "ticket_vi": "Vào tự do (công trình tôn giáo).",
        "duration_vi": "Khoảng 20-30 phút.",
        "best_time_vi": "Quanh năm; đặc biệt các dịp lễ Chính Thống giáo.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn. Có lối tiếp cận cho người khuyết tật.",
    },
    [
        {"title": "2GIS — Храм Архистратига Божия Михаила, Ноябрьск", "url": "https://2gis.ru/noyabrsk/firm/14496489581577414"},
        {"title": "Приход — salehard-13.cerkov.ru", "url": "https://salehard-13.cerkov.ru/"},
    ],
    ["church", "orthodox", "noyabrsk", "2005", "oil-gas-town"],
    maps_text("Храм Архистратига Михаила", "Ноябрьск", "Church of Archangel Michael", "Noyabrsk", 63.200847, 75.444433),
))

# 18) Горнолыжный комплекс «Октябрьский» (Лабытнанги) --------------------------
RECORDS.append(rec(
    "labytnangi-oktyabrsky-ski-resort",
    "Khu trượt tuyết 'Oktyabrsky' (Goóc-nô-lư-nưi ком-plếch Ốc-ti-áp-rơ-xki), Labytnangi",
    "Горнолыжный комплекс «Октябрьский» (Лабытнанги)",
    "Oktyabrsky Ski Resort (Labytnangi)",
    ["other"],
    66.696610, 66.570806,
    "Số 5 vi khu Oktyabrsky, Labytnangi (La-bư-tnan-ghi), Khu tự trị Yamalo-Nenets, Nga.",
    "Khu trượt tuyết duy nhất và nổi tiếng nhất vùng Salekhard - Labytnangi, dưới chân dãy Ural Cực. Mở từ 2003, mùa trượt kéo dài từ tháng 11 đến tháng 5, với đường trượt, đường tuýp và khu riêng cho trẻ em - điểm vui chơi mùa đông được người dân Yamal yêu thích.",
    "Khu trượt tuyết 'Oktyabrsky' nằm ở thành phố Labytnangi, bên kia sông Ob đối diện thủ phủ Salekhard, dưới chân dãy Ural Cực (Polar Urals). Đây là khu trượt tuyết chính và được yêu thích nhất của cả khu vực Salekhard - Labytnangi, mở cửa từ năm 2003. Nhờ mùa đông dài và tuyết dày ở vùng cận cực, mùa trượt tại đây kéo dài từ tháng 11 đến tận tháng 5. Khu phức hợp có đường trượt chính dài khoảng 620 m với độ chênh cao chừng 110 m, hệ thống cáp kéo, cùng các khu trượt tuýp (phao), trượt xe trượt và một sườn dốc riêng cho trẻ em với 'baby-lift'. Định hướng chủ yếu vào nghỉ dưỡng gia đình và người mới tập, khu phức hợp gần đây được đầu tư nâng cấp hiện đại với thiết bị, trang phục thuê chất lượng và toà nhà dịch vụ mới. Được ví như 'viên ngọc' vui chơi mùa đông của Yamal, đây là điểm đến lý tưởng để du khách trải nghiệm trượt tuyết giữa khung cảnh núi non phương Bắc hùng vĩ.",
    [
        "Khu trượt tuyết chính của vùng Salekhard - Labytnangi, dưới chân dãy Ural Cực.",
        "Mở từ 2003, mùa trượt dài từ tháng 11 đến tháng 5 (tuyết cận cực).",
        "Có đường trượt ~620 m, khu tuýp và sườn riêng cho trẻ em.",
    ],
    {
        "hours_vi": "Theo mùa và giờ hoạt động riêng của khu; mở đông đúc cuối tuần.",
        "ticket_vi": "Vé cáp và thuê thiết bị tính phí theo lượt/buổi.",
        "duration_vi": "Nửa ngày đến trọn ngày.",
        "best_time_vi": "Tháng 11 đến tháng 5 (mùa tuyết); rực rỡ khi có cực quang.",
        "tips_vi": "Đến từ Salekhard/Labytnangi khá tiện. Mặc đồ giữ nhiệt tốt, có thuê thiết bị.",
    },
    [
        {"title": "Yandex Maps — Горнолыжный комплекс «Октябрьский», Лабытнанги", "url": "https://yandex.com/maps/org/oktyabrskiy/141087597187/"},
        {"title": "Администрация Лабытнанги — ГЛК «Октябрьский»", "url": "https://lbt.yanao.ru/district/places/7/"},
    ],
    ["ski", "winter", "polar-urals", "labytnangi", "family"],
    maps_org("https://yandex.com/maps/org/oktyabrskiy/141087597187/", "Oktyabrsky Ski Resort", "Labytnangi"),
))

# 19) Ямальский районный музей (Яр-Сале) ---------------------------------------
RECORDS.append(rec(
    "yar-sale-yamal-district-museum",
    "Bảo tàng huyện Yamal ở làng Yar-Sale (Ia-man-xki rai-ôn-nưi mu-dây)",
    "Ямальский районный музей (Яр-Сале)",
    "Yamal District Museum (Yar-Sale)",
    ["museum"],
    66.86259, 70.85447,
    "Số 18 phố Khudi Seroko, làng Yar-Sale (Ia-rơ Xa-lê), huyện Yamal, Khu tự trị Yamalo-Nenets, Nga.",
    "Bảo tàng địa phương ở Yar-Sale - 'thủ phủ' của huyện Yamal, trung tâm của vùng bán đảo Yamal nơi người Nenets chăn tuần lộc. Bảo tàng lưu giữ hiện vật quý về đời sống du mục, trang phục, tín ngưỡng của dân tộc bản địa - cửa ngõ tìm hiểu văn hoá tuần lộc đích thực.",
    "Bảo tàng huyện Yamal nằm ở làng Yar-Sale - trung tâm hành chính của huyện Yamal, một ngôi làng trên bán đảo Yamal huyền thoại, nơi tập trung cộng đồng người Nenets chăn tuần lộc lớn nhất thế giới. Tên gọi 'Yar-Sale' trong tiếng Nenets nghĩa là 'mũi đất cát'. Bảo tàng được thành lập ngày 27-8-1991 trên cơ sở bộ sưu tập của một bảo tàng học đường, đến nay lưu giữ nhiều hiện vật quý phản ánh đời sống du mục truyền thống: lều chum, xe trượt tuần lộc, trang phục lông thú, đồ dùng sinh hoạt, vật phẩm tín ngưỡng shaman và nghệ thuật dân gian của người Nenets, Khanty. Đây là một trong những nơi tốt nhất để hiểu về văn hoá tuần lộc đích thực của bán đảo Yamal - vùng đất mà nhiều gia đình bản địa đến nay vẫn di cư theo đàn tuần lộc qua lãnh nguyên. Ghé thăm bảo tàng ở Yar-Sale, du khách như bước vào 'trái tim' của di sản chăn tuần lộc Yamal, bổ trợ tuyệt vời cho trải nghiệm thăm các trại du mục (stойbище) ngoài lãnh nguyên.",
    [
        "Bảo tàng ở Yar-Sale - trung tâm huyện Yamal trên bán đảo chăn tuần lộc.",
        "Lưu giữ hiện vật về đời sống du mục, trang phục, tín ngưỡng người Nenets.",
        "Cửa ngõ tìm hiểu văn hoá tuần lộc đích thực của bán đảo Yamal.",
    ],
    {
        "hours_vi": "Thứ Hai-Thứ Sáu 9h-18h30; thứ Bảy 10h-17h. Nên xác nhận trước.",
        "ticket_vi": "Vé tham quan mức phổ thông.",
        "duration_vi": "Khoảng 1 giờ.",
        "best_time_vi": "Quanh năm; kết hợp mùa lễ hội tuần lộc để trải nghiệm trọn vẹn.",
        "tips_vi": "Yar-Sale cách Salekhard ~189 km, thường tới bằng máy bay/trực thăng hoặc đường mùa đông.",
    },
    [
        {"title": "Yandex Maps — Ямальский районный музей, Яр-Сале", "url": "https://yandex.com/maps/org/mbuk_yamalskiy_rayonny_muzey/1368597466"},
        {"title": "Culture.RF — Ямальский районный музей", "url": "https://www.culture.ru/institutes/11572/yamalskii-raionnyi-muzei"},
    ],
    ["museum", "nenets", "yamal-peninsula", "reindeer", "yar-sale"],
    maps_text("Ямальский районный музей", "Яр-Сале", "Yamal District Museum", "Yar-Sale", 66.86259, 70.85447),
))

# 20) Озеро Большое Щучье (Полярный Урал) --------------------------------------
RECORDS.append(rec(
    "bolshoye-shchuchye-lake",
    "Hồ Bolshoye Shchuchye - hồ sâu nhất dãy Ural (Ô-di-rô Ban-sô-ie Su-chi-ê)",
    "Озеро Большое Щучье",
    "Lake Bolshoye Shchuchye",
    ["park_garden"],
    67.8833, 66.3167,
    "Dãy Ural Cực (Polar Urals), huyện Priuralsky, Khu tự trị Yamalo-Nenets, Nga.",
    "Hồ nước ngọt lớn và sâu nhất của toàn dãy Ural (độ sâu tới ~136 m), nằm trong một thung lũng băng hà hẹp giữa dãy Ural Cực. Được ví như 'Baikal thu nhỏ' của phương Bắc, hồ dài gần 13 km với làn nước lạnh trong vắt và cảnh quan núi non hoang sơ ngoạn mục.",
    "Hồ Bolshoye Shchuchye (nghĩa là 'hồ Cá Măng Lớn') là hồ nước ngọt lớn nhất và sâu nhất của cả dãy núi Ural, nằm ẩn mình trong một thung lũng băng hà hẹp và sâu giữa dãy Ural Cực (Polar Urals) thuộc vùng Bắc Cực nước Nga. Hồ dài khoảng 12-13 km, rộng chừng 1 km nhưng có độ sâu tối đa lên tới khoảng 136 mét (một số nguồn ghi tới 140 m) - khiến nó được ví như một 'hồ Baikal thu nhỏ' của phương Bắc. Mặt hồ nằm ở độ cao 186 m so với mực nước biển, được bao bọc bởi những sườn núi dốc đứng dựng lên hàng trăm mét, tạo nên khung cảnh vịnh hẹp (fjord) nội địa vô cùng ngoạn mục. Nhờ lớp trầm tích đáy hồ dày, đây còn là 'kho lưu trữ' khí hậu quý giá, được các nhà khoa học quốc tế khoan lấy lõi để nghiên cứu lịch sử khí hậu, băng hà và thảm thực vật vùng cực suốt hàng chục nghìn năm. Với vẻ đẹp hoang sơ, làn nước lạnh trong vắt và sự tĩnh mịch tuyệt đối, Bolshoye Shchuchye là điểm đến trong mơ cho những chuyến thám hiểm, đi bộ đường dài và chèo thuyền giữa thiên nhiên Bắc Cực nguyên vẹn.",
    [
        "Hồ sâu nhất dãy Ural (~136 m), như 'Baikal thu nhỏ' của phương Bắc.",
        "Nằm trong thung lũng băng hà hẹp giữa dãy Ural Cực, cảnh quan ngoạn mục.",
        "Đáy hồ là 'kho lưu trữ' khí hậu quý, được khoa học quốc tế nghiên cứu.",
    ],
    {
        "hours_vi": "Thiên nhiên hoang dã, tiếp cận tự do nhưng cần chuẩn bị kỹ.",
        "ticket_vi": "Không có vé; chi phí chủ yếu là tour/vận chuyển thám hiểm.",
        "duration_vi": "Thường theo tour nhiều ngày.",
        "best_time_vi": "Cuối hè (7-8) khi ấm hơn; mùa đông cực lạnh và khó tiếp cận.",
        "tips_vi": "Vùng xa xôi, nên đi theo tour/hướng dẫn có kinh nghiệm; chuẩn bị đồ ấm và an toàn kỹ.",
    },
    [
        {"title": "Britannica — Lake Bolshoye Shchuchye", "url": "https://www.britannica.com/place/Lake-Bolshoye-Shchuchye"},
        {"title": "Journal of Quaternary Science — Lake Bolshoye Shchuchye sediment core", "url": "https://onlinelibrary.wiley.com/doi/10.1002/jqs.3400"},
    ],
    ["lake", "polar-urals", "nature", "deepest", "hiking"],
    maps_text("Озеро Большое Щучье", "Полярный Урал", "Lake Bolshoye Shchuchye", "Polar Urals", 67.8833, 66.3167),
))

# 21) Ямальский кратер (воронка газового выброса) ------------------------------
RECORDS.append(rec(
    "yamal-gas-crater",
    "Hố khí Yamal - miệng hố phun khí bí ẩn (Ia-man-xki cra-ter / vô-rôn-ca)",
    "Ямальский кратер (воронка газового выброса)",
    "Yamal Crater (gas emission crater)",
    ["other"],
    69.971111, 68.370278,
    "Bán đảo Yamal, gần mỏ khí Bovanenkovo, huyện Yamal, Khu tự trị Yamalo-Nenets, Nga.",
    "Miệng hố khổng lồ bí ẩn xuất hiện năm 2014 giữa lãnh nguyên bán đảo Yamal, gây chấn động giới khoa học thế giới. Được cho là hình thành do vụ nổ khí metan dưới lòng đất băng vĩnh cửu vì hiện tượng nóng lên toàn cầu - một hiện tượng địa chất kỳ lạ tiêu biểu của vùng Yamal.",
    "Hố khí Yamal (Yamalsky krater) là một miệng hố tròn khổng lồ, đường kính khoảng 20-40 m và sâu hơn 50 m với vách gần như thẳng đứng, bất ngờ xuất hiện trong khoảng thời gian từ mùa thu 2013 đến mùa xuân 2014 ở phần trung tâm bán đảo Yamal, cách mỏ khí Bovanenkovo chừng 30 km về phía nam. Khi được phát hiện năm 2014, 'hố đen' bí ẩn giữa lãnh nguyên đã gây chấn động và làm dấy lên vô số giả thuyết, thậm chí có người liên hệ nó với 'tam giác Bermuda'. Sau nhiều nghiên cứu, phần lớn các nhà khoa học đồng thuận rằng hố hình thành do một vụ nổ khí metan dưới lòng đất: khí gas hydrate tan chảy trong lớp băng vĩnh cửu tích tụ áp suất rồi phun trào, hất tung đất đá lên bề mặt tạo thành bờ 'lũy' quanh miệng hố. Hiện tượng này được cho là liên quan đến sự nóng lên toàn cầu làm tan băng vĩnh cửu ở Bắc Cực. Miệng hố nhanh chóng tích nước và đến năm 2016 đã biến thành một hồ nhỏ. Dù nằm ở vùng cực kỳ hẻo lánh, khó tiếp cận, hố khí Yamal đã trở thành một biểu tượng khoa học nổi tiếng thế giới của vùng đất này - lời nhắc nhở ấn tượng về những biến đổi đang diễn ra dưới lòng lãnh nguyên.",
    [
        "Miệng hố khổng lồ bí ẩn xuất hiện năm 2014, gây chấn động khoa học thế giới.",
        "Hình thành do nổ khí metan trong băng vĩnh cửu tan chảy vì nóng lên toàn cầu.",
        "Đã tích nước thành hồ nhỏ sau 2016 - biểu tượng biến đổi khí hậu Bắc Cực.",
    ],
    {
        "hours_vi": "Vùng hoang dã cực kỳ hẻo lánh; chỉ tiếp cận qua chuyến khảo sát chuyên biệt.",
        "ticket_vi": "Không có dịch vụ du lịch thông thường.",
        "duration_vi": "Theo chuyến khảo sát (thường dài ngày, bằng trực thăng).",
        "best_time_vi": "Mùa hè ngắn ngủi; điều kiện tiếp cận rất khắc nghiệt.",
        "tips_vi": "Không phải điểm du lịch đại chúng; chủ yếu tham quan gián tiếp qua bảo tàng, tư liệu.",
    },
    [
        {"title": "Wikipedia (RU) — Ямальский кратер", "url": "https://ru.wikipedia.org/wiki/Ямальский_кратер"},
        {"title": "Arctic Russia — Ямальский кратер", "url": "https://tourism.arctic-russia.ru/sights/yamalskiy-krater/"},
    ],
    ["gas-crater", "permafrost", "yamal-peninsula", "geology", "climate"],
    maps_text("Ямальский кратер", "полуостров Ямал", "Yamal Gas Crater", "Yamal Peninsula", 69.971111, 68.370278),
))

# 22) Гыданский национальный парк ----------------------------------------------
RECORDS.append(rec(
    "gydansky-national-park",
    "Vườn quốc gia Gydansky - bán đảo Gydan (Gư-đan-xki na-txi-ô-nan-nưi parc)",
    "Гыданский национальный парк",
    "Gydansky National Park",
    ["park_garden"],
    67.490373, 78.738821,
    "Bán đảo Gydan và các đảo biển Kara, huyện Tazovsky, Khu tự trị Yamalo-Nenets, Nga.",
    "Vườn quốc gia cực bắc trên bán đảo Gydan hoang vu, một trong những vùng lãnh nguyên Bắc Cực nguyên vẹn nhất nước Nga. Rộng gần 900.000 ha, là thiên đường của gấu Bắc Cực, hải mã, tuần lộc hoang và vô số chim di cư - điểm đến cho những chuyến thám hiểm sinh thái đỉnh cao.",
    "Vườn quốc gia Gydansky (nâng cấp từ khu bảo tồn thiên nhiên thành vườn quốc gia từ tháng 12-2024) nằm ở phần cực bắc của bán đảo Gydan thuộc huyện Tazovsky, trải ra tận các đảo trên biển Kara. Với tổng diện tích khoảng 898.000 ha, đây là một trong những vùng lãnh nguyên Bắc Cực còn nguyên vẹn và hoang sơ nhất của nước Nga, bao gồm các bán đảo Yavai, Mamonta, Oleny và những hòn đảo như Shokalsky, Pestsovye, Oleny giữa biển Kara băng giá. Nằm ở vĩ độ rất cao (điểm cực bắc lên tới trên 73°B), vườn quốc gia là địa bàn sinh sống và di cư của những loài động vật Bắc Cực biểu tượng: gấu trắng Bắc Cực, hải mã Atlantic, tuần lộc hoang, cùng hàng loạt loài chim nước và chim di cư quý hiếm về đây làm tổ mỗi mùa hè ngắn ngủi. Hệ sinh thái lãnh nguyên - ven biển ở đây gần như chưa bị con người tác động, mang giá trị bảo tồn toàn cầu. Dù cực kỳ hẻo lánh và chỉ tiếp cận được qua các chuyến thám hiểm sinh thái có tổ chức, Gydansky là 'chốn tận cùng thế giới' đầy mê hoặc cho những ai khao khát chạm tới thiên nhiên Bắc Cực nguyên bản.",
    [
        "Vườn quốc gia cực bắc trên bán đảo Gydan, gần 900.000 ha hoang sơ.",
        "Địa bàn của gấu Bắc Cực, hải mã, tuần lộc hoang và chim di cư quý hiếm.",
        "Một trong những vùng lãnh nguyên Bắc Cực nguyên vẹn nhất nước Nga.",
    ],
    {
        "hours_vi": "Khu bảo tồn hoang dã; vào phải xin phép Ban quản lý và có tổ chức.",
        "ticket_vi": "Theo quy định khu bảo tồn; chi phí chủ yếu là tour thám hiểm.",
        "duration_vi": "Theo chuyến thám hiểm (dài ngày).",
        "best_time_vi": "Mùa hè ngắn (7-8) khi động vật và chim hoạt động mạnh.",
        "tips_vi": "Cần giấy phép và hướng dẫn chuyên nghiệp; hành trình khắc nghiệt, chuẩn bị kỹ.",
    },
    [
        {"title": "Wikipedia (RU) — Гыданский национальный парк", "url": "https://ru.wikipedia.org/wiki/Гыданский_национальный_парк"},
        {"title": "Минприроды России — Гыданский заповедник", "url": "http://www.mnr.gov.ru/activity/oopt/gydanskiy_gosudarstvennyy_prirodnyy_zapovednik/"},
    ],
    ["national-park", "arctic", "gydan-peninsula", "polar-bear", "wildlife"],
    maps_text("Гыданский национальный парк", "Тазовский район", "Gydansky National Park", "Gydan Peninsula", 67.490373, 78.738821),
))

# 23) Массив Рай-Из / природный парк «Ингилор» / Харп (Полярный Урал) ----------
RECORDS.append(rec(
    "rai-iz-massif-ingilor-polar-urals",
    "Massif Rai-Iz & VQG Ingilor - cửa ngõ Kharp, dãy Ural Cực (Rai-Iz / In-ghi-lôr)",
    "Массив Рай-Из и природный парк «Ингилор» (Полярный Урал)",
    "Rai-Iz Massif and Ingilor Nature Park (Polar Urals)",
    ["park_garden"],
    66.805678, 65.803843,
    "Vùng dãy Ural Cực gần thị trấn Kharp (Kháp), huyện Priuralsky, Khu tự trị Yamalo-Nenets, Nga (toạ độ trỏ tới thị trấn cửa ngõ Kharp).",
    "Khối núi Rai-Iz hùng vĩ ở dãy Ural Cực (đỉnh cao ~1.316 m) cùng vườn thiên nhiên Ingilor - 'viên ngọc' của Polar Urals, nơi có trại nuôi bò xạ hương (musk ox) bán hoang dã lớn nhất thế giới. Thị trấn Kharp bên sông Sob dưới chân núi là cửa ngõ tiếp cận, dễ đến bằng tàu hoả.",
    "Massif Rai-Iz (còn viết Rayiz) là khối núi mở đầu phần tây nam của dãy Ural Cực (Polar Urals), có hình móng ngựa cong khổng lồ dài tới 55 km, với đỉnh cao nhất khoảng 1.316 m ở trung tâm cùng nhiều đỉnh như Pik Polyarny (1.309 m), Pik Topografov (1.287 m). Sườn núi dốc đứng về phía bắc và tây, quanh năm còn tuyết và cả những khối băng nhỏ; đây là điểm đến hấp dẫn cho leo núi, đi bộ đường dài và tìm khoáng vật. Bao quanh khối núi là vườn thiên nhiên Ingilor (Природный парк «Ингилор») - vườn thiên nhiên duy nhất của khu tự trị, rộng khoảng một triệu ha, gồm các phân khu 'Ingilor', 'Sob-Rai-Iz' và 'Polar-Ural'. Niềm tự hào lớn nhất của vườn là trại nuôi bò xạ hương (musk ox / овцебык) bán hoang dã được xem là lớn nhất thế giới, cùng đàn tuần lộc, cáo Bắc Cực và hệ động thực vật lãnh nguyên - miền núi phong phú. Cửa ngõ để tiếp cận cả Rai-Iz lẫn vườn Ingilor là thị trấn Kharp (nằm trên sông Sob, ngay dưới chân khối núi, trên vĩ tuyến 67), rất dễ đến bằng tàu hoả tuyến Labytnangi. Sự kết hợp của núi non hùng vĩ, thiên nhiên hoang sơ và đàn bò xạ hương độc đáo khiến khu vực này là một trong những điểm nhấn thiên nhiên tiêu biểu nhất của Yamal.",
    [
        "Khối núi Rai-Iz (đỉnh ~1.316 m) - điểm leo núi, đi bộ nổi bật của Ural Cực.",
        "Vườn thiên nhiên Ingilor có trại nuôi bò xạ hương bán hoang dã lớn nhất thế giới.",
        "Cửa ngõ Kharp bên sông Sob dưới chân núi, dễ tiếp cận bằng tàu hoả.",
    ],
    {
        "hours_vi": "Thiên nhiên hoang dã; vào vườn Ingilor và trại bò xạ hương nên theo tour có tổ chức.",
        "ticket_vi": "Theo quy định vườn thiên nhiên/tour; leo núi tự do nhưng cần chuẩn bị.",
        "duration_vi": "Từ nửa ngày (tham quan gần Kharp) đến nhiều ngày (leo núi, thám hiểm).",
        "best_time_vi": "Cuối xuân - mùa hè để đi bộ, leo núi; mùa đông cảnh tuyết và cực quang.",
        "tips_vi": "Xuất phát từ Kharp (tàu tuyến Labytnangi). Leo núi cần kinh nghiệm và đồ bảo hộ vì khí hậu cận cực khắc nghiệt.",
    },
    [
        {"title": "Ураловед — Массив Рай-Из", "url": "https://uraloved.ru/massiv-raj-iz"},
        {"title": "Красный Север — Природный парк «Ингилор»", "url": "https://ks-yanao.ru/narrative/obschestvo/zhemchuzhina-poljarnogo-urala-novyj-prirodnyj-park-ingilor"},
    ],
    ["polar-urals", "mountain", "ingilor", "musk-ox", "kharp"],
    maps_text("Массив Рай-Из", "Харп", "Rai-Iz Massif Polar Urals", "Kharp", 66.805678, 65.803843),
))

# 24) Верхне-Тазовский заповедник ----------------------------------------------
RECORDS.append(rec(
    "verkhne-tazovsky-nature-reserve",
    "Khu bảo tồn thiên nhiên Verkhne-Tazovsky (Vjéc-nhê Ta-dốp-xki da-pô-vét-nhic)",
    "Верхне-Тазовский заповедник",
    "Verkhne-Tazovsky Nature Reserve",
    ["park_garden"],
    62.858, 84.190,
    "Thượng nguồn sông Taz, huyện Krasnoselkup (đông nam Yamal), Khu tự trị Yamalo-Nenets, Nga (toạ độ trung tâm theo ranh giới khu bảo tồn).",
    "Khu bảo tồn thiên nhiên rộng lớn ở thượng nguồn sông Taz, phần đông nam hẻo lánh của Yamal - vùng rừng taiga phương bắc gần như nguyên sinh. Nơi trú ngụ của gấu nâu, chồn sable, tuần lộc rừng và là quê hương của người Selkup bản địa, một trong những vùng hoang dã nguyên vẹn hiếm hoi của Siberia.",
    "Khu bảo tồn thiên nhiên quốc gia Verkhne-Tazovsky nằm ở phần đông nam hẻo lánh của Khu tự trị Yamalo-Nenets, thuộc huyện Krasnoselkup, bao trọn vùng thượng nguồn sông Taz. Khu bảo tồn trải dài khoảng 150 km theo hướng bắc-nam (từ khoảng 62°10' đến 63°33' vĩ bắc) và 70 km theo hướng đông-tây, dọc theo đường phân thuỷ Ob - Taz - Yenisei. Đây là vùng rừng taiga phương bắc gần như nguyên sinh với những cánh rừng thông, tùng lá kim, đầm lầy và mạng lưới sông suối chằng chịt trong lành. Hệ động vật phong phú gồm gấu nâu, chồn sable (loài thú lông quý), chó sói, tuần lộc rừng, cùng nhiều loài chim; các dòng sông giàu cá quý. Vùng đất này cũng gắn bó mật thiết với người Selkup - một dân tộc bản địa Siberia sinh sống bằng săn bắt, đánh cá và chăn tuần lộc theo truyền thống lâu đời. Là một trong những khu vực taiga nguyên vẹn ít bị tác động nhất của Tây Siberia, Verkhne-Tazovsky mang giá trị bảo tồn và khoa học lớn, dành cho những chuyến khảo sát sinh thái chuyên biệt hơn là du lịch đại chúng.",
    [
        "Khu bảo tồn taiga nguyên sinh ở thượng nguồn sông Taz, đông nam Yamal.",
        "Nơi trú ngụ của gấu nâu, chồn sable quý, tuần lộc rừng và nhiều loài chim.",
        "Gắn với văn hoá người Selkup bản địa - săn bắt, đánh cá, chăn tuần lộc.",
    ],
    {
        "hours_vi": "Khu bảo tồn hoang dã; vào phải xin phép Ban quản lý (trụ sở ở Krasnoselkup).",
        "ticket_vi": "Theo quy định khu bảo tồn; chủ yếu phục vụ khảo sát, sinh thái.",
        "duration_vi": "Theo chuyến khảo sát (dài ngày).",
        "best_time_vi": "Mùa hè - đầu thu; mùa đông rất lạnh và khó tiếp cận.",
        "tips_vi": "Vùng rất hẻo lánh; cần giấy phép, hướng dẫn viên và chuẩn bị hậu cần kỹ lưỡng.",
    },
    [
        {"title": "Wikipedia (RU) — Верхне-Тазовский заповедник", "url": "https://ru.wikipedia.org/wiki/Верхне-Тазовский_заповедник"},
        {"title": "Минприроды России — Верхне-Тазовский заповедник", "url": "http://www.mnr.gov.ru/activity/oopt/verkhne_tazovskiy_gosudarstvennyy_prirodnyy_zapovednik/"},
    ],
    ["nature-reserve", "taiga", "selkup", "krasnoselkup", "wildlife"],
    maps_text("Верхне-Тазовский заповедник", "Красноселькуп", "Verkhne-Tazovsky Nature Reserve", "Krasnoselkup", 62.858, 84.190),
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
