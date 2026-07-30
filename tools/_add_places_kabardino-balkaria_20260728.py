# -*- coding: utf-8 -*-
"""_add_places_kabardino-balkaria_20260728.py — VÙNG: Cộng hoà Kabardino-Balkaria
(Кабардино-Балкарская Республика) — lần chạy tự động 2026-07-28.

Bối cảnh: kabardino-balkaria.json hiện có 7 địa điểm (mount-elbrus, chegem-waterfalls,
blue-lake-cherek, upper-balkaria, el-tyubyu-necropolis, nalchik-atazhukinsky-park,
cheget-mountain). Bổ sung 23 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại
hình → đưa vùng lên 30.

Phân bố loại hình (23 bản ghi mới):
- park_garden (12): Баксанское ущелье, Черекская теснина, Ущелье Адыр-Су, Озеро Гижгит,
  Озёра Шадхурей, Водопады Гедмишх (Царская корона), Урочище Джилы-Су + вд. Султан,
  Аушигерские термальные источники, Безенги (стена+ледник), Водопад Девичьи косы,
  Поляна нарзанов (Приэльбрусье), Перевал Актопрак.
- other (1): Обсерватория «Пик Терскол».
- museum (3): Национальный музей КБР, Музей ИЗО им. Ткаченко, «Наследие нартов».
- church (2): Соборная мечеть Нальчика (ислам), Симеоновский собор (православие).
- theatre (2): Кабардинский драмтеатр им. Али Шогенцукова, Государственный музыкальный театр.
- monument (2): Мемориал жертв политических репрессий 1944–1957, Ресторан-символ «Сосруко».
- square_street (1): Площадь Абхазии (центр Нальчика).

TOẠ ĐỘ — xác minh chéo 2026-07-28 (ru.wikipedia/geohack, 2ГИС firm-card center=lon,lat,
Yandex Maps org, các trang du lịch bolshayastrana/tourister/kavkaz.travel/vpoxod). Phạm vi
Kabardino-Balkaria: lat ~42,9–44,2; lon ~42,4–44,2 — mọi toạ độ nằm trong phạm vi, KHÔNG
đảo lat/lon:
  Баксанское ущелье 43.301314,42.730404; Черекская теснина 43.183333,43.516667 (ru.wiki
  43°11′N 43°31′E); Адыр-Су 43.231379,42.801773; Гижгит 43.463656,42.991940; Шадхурей
  43.706389,43.076111; Гедмишх 43.691961,42.848175; Джилы-Су/вд.Султан 43.433650,42.533587;
  Аушигер 43.374432,43.721007; Безенги (альплагерь) 43.111020,43.147560; Девичьи косы
  43.273979,42.492363; Поляна нарзанов 43.245359,42.523362; Перевал Актопрак 43.400410,
  43.094700; Обсерватория Пик Терскол 43.274722,42.500833 (ru.wiki 43°16′29″N 42°30′03″E);
  Нац. музей КБР 43.486716,43.608428 (2ГИС, ул. Горького 62); Музей ИЗО 43.480501,43.600367
  (2ГИС, пр. Ленина 35); Наследие нартов 43.486874,43.575591 (2ГИС, ул. Байсултанова 39);
  Соборная мечеть 43.488435,43.616783 (2ГИС, пр. Шогенцукова 41); Симеоновский собор
  43.484574,43.613961 (2ГИС, ул. Пятигорская 82); Драмтеатр Шогенцукова 43.475648,43.600753
  (2ГИС, пр. Шогенцукова 2); Музыкальный театр 43.485746,43.606460 (2ГИС, пр. Ленина 53а);
  Мемориал репрессий 43.453368,43.581099 (2ГИС, ул. Балкарова 4а); Сосруко 43.460562,
  43.599785 (Малая Кизиловка); Площадь Абхазии 43.471389,43.588056 (ru.wiki 43°28′17″N
  43°35′17″E).

Nội dung tiếng Việt NGUYÊN GỐC (tự viết/paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_kabardino-balkaria_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "kabardino-balkaria"
REGION_NAME_VI = "Cộng hoà Kabardino-Balkaria"
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


def outdoor_practical(duration, best_time, tips, ticket="Khu vực thiên nhiên ngoài trời, không có giờ đóng cửa cố định.",
                      hours="Tham quan ban ngày quanh năm; không có giờ mở cửa cố định."):
    return {
        "hours_vi": hours,
        "ticket_vi": ticket,
        "duration_vi": duration,
        "best_time_vi": best_time,
        "tips_vi": tips,
    }


RECORDS = []

# 1) Баксанское ущелье --------------------------------------------------------------
RECORDS.append(rec(
    "baksan-gorge",
    "Hẻm núi Baksan (Baksanskoe)",
    "Баксанское ущелье",
    "Baksan Gorge",
    ["park_garden"],
    43.301314, 42.730404,
    "Thung lũng sông Baksan, huyện Elbrussky, Cộng hoà Kabardino-Balkaria, Nga (tuyến A-158 dẫn tới Elbrus).",
    "Baksan là hẻm núi dài và nổi tiếng bậc nhất Trung Kavkaz, nơi con đường chạy dọc đáy hẻm dẫn thẳng tới chân núi Elbrus. Hai bên là vách đá dựng đứng, rừng thông, những ngôi làng cổ và hàng loạt suối khoáng narzan.",
    "Kéo dài theo dòng sông Baksan cuồn cuộn, hẻm Baksan được xem là cửa ngõ chính để vào vùng Prielbrusye và chinh phục Elbrus. Từ thị trấn Baksan, con đường A-158 luồn sâu vào núi, càng đi càng thu hẹp giữa những vách đá cao, xen kẽ rừng thông và bãi cỏ núi cao. Dọc hẻm là chuỗi làng cổ của người Balkar như Zayukovo, Kendelen, Verkhniy Baksan, Terskol, cùng nhiều nhánh hẻm phụ dẫn tới Adyr-Su, Adyl-Su và thung lũng Cheget. Phần thượng nguồn hẻm nằm trong Vườn quốc gia Prielbrusye, nơi tập trung suối khoáng, thác nước và các trạm cáp treo lên Elbrus. Cảnh quan biến đổi liên tục theo độ cao khiến hành trình xuyên hẻm Baksan trở thành một trong những cung đường núi đẹp nhất Bắc Kavkaz, vừa là tuyến du lịch vừa là con đường huyết mạch của cả vùng.",
    [
        "Tuyến đường chính dẫn tới núi Elbrus, luồn qua vách đá, rừng thông và làng cổ Balkar.",
        "Kết nối tới hàng loạt điểm đến: Adyr-Su, Poляna nарзанов, Terskol, Cheget và Azau.",
        "Nhiều suối khoáng narzan tự nhiên và điểm ngắm cảnh dọc đường.",
    ],
    outdoor_practical(
        "Nửa ngày đến cả ngày nếu dừng nhiều điểm dọc hẻm.",
        "Tháng 5–10 khi đường khô ráo; mùa đông cần lốp phù hợp cho vùng núi.",
        "Đường núi quanh co, lái xe cẩn thận; kết hợp ghé suối khoáng và các nhánh hẻm phụ.",
    ),
    [
        {"title": "Wikipedia (RU) — Баксанское ущелье", "url": "https://ru.wikipedia.org/wiki/Баксанское_ущелье"},
        {"title": "Bolshaya Strana — Баксанское ущелье", "url": "https://bolshayastrana.com/dostoprimechatelnosti/kabardino-balkariya/baksanskoe-ushchele-351"},
    ],
    ["gorge", "baksan", "prielbrusye", "nature", "scenic-road", "north-caucasus"],
    maps_text("Баксанское ущелье", "Кабардино-Балкария", "Baksan Gorge", "Kabardino-Balkaria", 43.301314, 42.730404),
))

# 2) Черекская теснина --------------------------------------------------------------
RECORDS.append(rec(
    "cherek-tesnina",
    "Hẻm hẹp Cherek (Cherekskaya tesnina)",
    "Черекская теснина",
    "Cherek Canyon (Tesnina)",
    ["park_garden"],
    43.183333, 43.516667,
    "Dọc sông Cherek Balkarsky, giữa Hồ Xanh Dưới và Thượng Balkaria, huyện Chereksky, Cộng hoà Kabardino-Balkaria, Nga.",
    "Cherekskaya tesnina là đoạn hẻm đá hẹp và ngoạn mục dài khoảng 6 km, nơi con đường được đục thẳng vào vách đá treo trên dòng sông Cherek cuộn xoáy. Có chỗ hai bờ đá chỉ cách nhau chừng 30 m còn vực sâu tới 300 m.",
    "Bắt đầu từ Hồ Xanh Dưới (Tserik-Kel) và men theo sông Cherek Balkarsky lên phía Thượng Balkaria, hẻm hẹp Cherek là một trong những cung đường gây choáng ngợp nhất Kabardino-Balkaria. Con đường cũ được người dân đục dần vào vách đá vôi qua nhiều thế hệ, chạy chênh vênh trên dòng nước xanh ngọc gào thét dưới sâu; ở những khúc hẹp nhất, khe đá chỉ rộng vài chục mét trong khi vách dựng đứng cao hàng trăm mét. Dọc đường vẫn còn dấu tích của lối đi bộ hiểm trở ngày xưa cùng những cây cầu nhỏ bắc qua vực. Cảnh quan hùng vĩ, ánh sáng thay đổi theo giờ trong ngày và tiếng nước réo khiến nơi đây trở thành điểm dừng bắt buộc trên tuyến tham quan Hồ Xanh – Thượng Balkaria, thường kết hợp cùng suối nước nóng Aushiger lân cận.",
    [
        "Con đường đục thẳng vào vách đá treo trên sông Cherek xanh ngọc sâu tới 300 m.",
        "Khúc hẹp nhất hai vách đá chỉ cách nhau khoảng 30 m, cảnh tượng ngoạn mục.",
        "Nằm ngay trên tuyến Hồ Xanh – Thượng Balkaria, dễ kết hợp trong một ngày.",
    ],
    outdoor_practical(
        "Khoảng 30–60 phút dừng ngắm; trọn ngày nếu kết hợp Hồ Xanh và Thượng Balkaria.",
        "Tháng 5–10 tầm nhìn đẹp nhất; tránh ngày mưa vì đá trơn.",
        "Đường hẹp một làn nhiều đoạn, lái xe nhường nhau; dừng ở các điểm ngắm có gờ an toàn.",
    ),
    [
        {"title": "Kavkaz.travel — Черекская теснина", "url": "https://kavkaz.travel/attractions/124"},
        {"title": "Travelask — Черекская теснина", "url": "https://travelask.ru/russia/kabardino-balkariya/vsyo-pro-cherekskoe-uschelie-cherekskuyu-tesninu-v-kabardino-balkarii"},
    ],
    ["canyon", "cherek", "gorge", "cliff-road", "nature", "north-caucasus"],
    maps_text("Черекская теснина", "Черекский район", "Cherek Canyon", "Kabardino-Balkaria", 43.183333, 43.516667),
))

# 3) Ущелье Адыр-Су -----------------------------------------------------------------
RECORDS.append(rec(
    "adyr-su-valley",
    "Hẻm núi Adyr-Su",
    "Ущелье Адыр-Су",
    "Adyr-Su Gorge",
    ["park_garden"],
    43.231379, 42.801773,
    "Nhánh hẻm phía nam thung lũng Baksan, đối diện làng Verkhniy Baksan, huyện Elbrussky, Cộng hoà Kabardino-Balkaria, Nga.",
    "Adyr-Su là một nhánh hẻm hoang sơ tách ra từ thung lũng Baksan, nổi tiếng với thang nâng ô tô kiểu đường ray độc đáo ngay cửa hẻm và đỉnh Ullu-Tau được người Balkar gọi trìu mến là 'Núi Mẹ'.",
    "Rẽ khỏi tuyến chính đối diện làng Verkhniy Baksan, hẻm Adyr-Su dài khoảng 14–15 km mở ra một thế giới núi non tĩnh lặng với chênh cao gần 1.000 m. Ngay đầu hẻm, du khách gặp một 'nút thắt' thú vị: vách đá dựng đứng khiến xe hơi phải lên một bệ nâng chạy trên đường ray nghiêng 45 độ để vượt qua, còn người đi bộ leo khoảng 300 bậc thang. Vượt qua rào cản đó, con đường men theo dòng Adyr-Su trong vắt, hai bên là rừng thông, đồng cỏ núi cao và những trại leo núi (alplager) lâu đời. Ở cuối hẻm sừng sững đỉnh Ullu-Tau (khoảng 4.207 m) với sông băng và hình dáng được ví như người mẹ dang tay, gắn với nhiều truyền thuyết Balkar. Adyr-Su là điểm đến quen thuộc của dân leo núi và những ai muốn đi bộ đường dài giữa thiên nhiên nguyên sơ của Prielbrusye.",
    [
        "Thang nâng ô tô trên đường ray nghiêng độc đáo ngay cửa hẻm.",
        "Đỉnh Ullu-Tau 'Núi Mẹ' với sông băng, gắn với truyền thuyết của người Balkar.",
        "Thiên nhiên hoang sơ, lý tưởng cho leo núi và trekking trong Prielbrusye.",
    ],
    outdoor_practical(
        "Nửa ngày đến cả ngày cho trekking sâu vào hẻm.",
        "Tháng 6–9 khi đường mòn khô ráo, tầm nhìn tốt.",
        "Đây là vùng biên giới/kiểm soát, mang theo giấy tờ tuỳ thân; đi giày leo núi và đồ ấm.",
    ),
    [
        {"title": "Bolshaya Strana — Ущелье Адыр-Су", "url": "https://bolshayastrana.com/dostoprimechatelnosti/kabardino-balkariya/ushchele-adyr-su-605"},
        {"title": "Vpoxod — Ущелье Адыр-Су", "url": "https://www.vpoxod.ru/page/toponym/adyrsu_info"},
    ],
    ["gorge", "adyr-su", "ullu-tau", "hiking", "mountaineering", "prielbrusye"],
    maps_text("Ущелье Адыр-Су", "Верхний Баксан", "Adyr-Su Gorge", "Kabardino-Balkaria", 43.231379, 42.801773),
))

# 4) Озеро Гижгит -------------------------------------------------------------------
RECORDS.append(rec(
    "gizhgit-lake",
    "Hồ Gizhgit (hồ Bylym)",
    "Озеро Гижгит",
    "Gizhgit Lake",
    ["park_garden"],
    43.463656, 42.991940,
    "Gần làng Bylym, thung lũng Baksan, huyện Elbrussky, Cộng hoà Kabardino-Balkaria, Nga.",
    "Gizhgit (còn gọi là hồ Bylym) nổi bật với mặt nước xanh ngọc lam kỳ ảo nằm lọt giữa những vách đá răng cưa. Hồ sâu tới 30 m, dài khoảng một cây số và là điểm 'sống ảo' được yêu thích ở Kabardino-Balkaria.",
    "Nằm trên một sườn núi phía trên làng Bylym trong thung lũng Baksan, hồ Gizhgit gây ấn tượng mạnh bằng gam màu xanh ngọc lam biến đổi theo ánh sáng và độ sâu. Hồ vốn hình thành từ hồ chứa bùn thải của tổ hợp khai khoáng Tyrnyauz trước kia, nhưng theo thời gian nước lắng trong và thiên nhiên hồi sinh, biến nơi đây thành một thắng cảnh được nhiều người tìm đến. Bao quanh mặt nước phẳng lặng là những dãy đá nhọn nhấp nhô và đồng cỏ khô, tạo khung hình tương phản đẹp mắt. Từ trên các mỏm đá cao, du khách có thể phóng tầm mắt xuống toàn cảnh hồ và thung lũng, đặc biệt lung linh vào sáng sớm và lúc hoàng hôn. Gizhgit thường được ghép vào cung đường lên Elbrus hoặc chuyến khám phá hẻm Baksan, và là điểm cắm trại, chụp ảnh nổi tiếng của vùng.",
    [
        "Mặt hồ xanh ngọc lam đặc trưng giữa những vách đá răng cưa.",
        "Điểm ngắm cảnh và chụp ảnh nổi tiếng, đẹp nhất lúc bình minh và hoàng hôn.",
        "Dễ kết hợp trên hành trình khám phá thung lũng Baksan và Elbrus.",
    ],
    outdoor_practical(
        "Khoảng 1–2 giờ ngắm cảnh và chụp ảnh.",
        "Tháng 5–10; buổi sáng sớm mặt nước phẳng lặng và trong xanh nhất.",
        "Đường lên hồ dốc và gồ ghề, nên đi xe gầm cao; không tắm vì bờ dốc và nước lạnh sâu.",
    ),
    [
        {"title": "Bolshaya Strana — Озеро Гижгит", "url": "https://bolshayastrana.com/dostoprimechatelnosti/kabardino-balkariya/ozero-gizhgit-544"},
        {"title": "Kukarta — Озеро Гижгит (Былымское)", "url": "https://kukarta.ru/ozero-gizhgit-bylymskoe-kabardino-balkariya-kak-dobratsya-foto-opisanie/"},
    ],
    ["lake", "turquoise", "bylym", "baksan", "viewpoint", "nature"],
    maps_text("Озеро Гижгит", "Былым", "Gizhgit Lake", "Kabardino-Balkaria", 43.463656, 42.991940),
))

# 5) Озёра Шадхурей -----------------------------------------------------------------
RECORDS.append(rec(
    "shadkhurey-lakes",
    "Hồ Shadkhurey",
    "Озёра Шадхурей",
    "Shadkhurey Lakes",
    ["park_garden"],
    43.706389, 43.076111,
    "Cách làng Kamennomostskoye khoảng 5 km về đông nam, huyện Zolsky, Cộng hoà Kabardino-Balkaria, Nga.",
    "Shadkhurey là nhóm hồ karst bí ẩn nằm dưới chân dãy Dzhinal ở độ cao hơn 1.000 m. Tên gọi có nghĩa 'vực nước tròn', với mặt nước sâu thẳm, tĩnh lặng đến kỳ lạ giữa vùng cao nguyên cỏ.",
    "Trải trên vùng cao nguyên phía đông huyện Zolsky, các hồ Shadkhurey hình thành do sụt lún karst khi nước ngầm hoà tan lớp đá vôi bên dưới lớp sa thạch. Trước kia có ba hồ, nhưng đầu thế kỷ XX một hồ bất ngờ cạn nước qua những quá trình ngầm chưa được lý giải, để lại lòng chảo sâu với một hồ nhỏ dưới đáy. Hai hồ còn lại nổi bật với mặt nước tối màu, phẳng lặng và tương phản mạnh với đồng cỏ xanh mướt xung quanh, tạo cảm giác vừa hùng vĩ vừa huyền bí – nên nhiều người ví von đây là 'vùng đất Sannikov' của Kabardino-Balkaria. Nằm trong cụm du lịch Nước khoáng Kavkaz và không xa Pyatigorsk, Shadkhurey là điểm dừng yêu thích cho những ai muốn cắm trại, câu cá và tận hưởng khung cảnh thảo nguyên núi yên bình.",
    [
        "Hồ karst 'vực nước tròn' sâu và tĩnh lặng dưới chân dãy Dzhinal.",
        "Khung cảnh thảo nguyên núi hoang sơ, huyền bí, thích hợp cắm trại và câu cá.",
        "Nằm trong cụm du lịch Nước khoáng Kavkaz, gần Pyatigorsk.",
    ],
    outdoor_practical(
        "Khoảng 1–2 giờ; lâu hơn nếu cắm trại hoặc câu cá.",
        "Cuối xuân đến đầu thu (tháng 5–9) khi thảo nguyên xanh và đường khô.",
        "Đường đất cuối tuyến gồ ghề, nên đi xe gầm cao; bờ hồ dốc, cẩn thận khi xuống nước.",
    ),
    [
        {"title": "Wikipedia (RU) — Шадхурей", "url": "https://ru.wikipedia.org/wiki/Шадхурей"},
        {"title": "Kulttourism — Озёра Шадхурей", "url": "https://culttourism.ru/kabardino_balkariya/ozyora_shadhurey.html"},
    ],
    ["lakes", "karst", "shadkhurey", "zolsky", "steppe", "nature"],
    maps_text("Озёра Шадхурей", "Зольский район", "Shadkhurey Lakes", "Kabardino-Balkaria", 43.706389, 43.076111),
))

# 6) Водопады Гедмишх (Царская корона) ----------------------------------------------
RECORDS.append(rec(
    "gedmishkh-waterfalls",
    "Thác Gedmishkh (Vương miện Sa hoàng)",
    "Водопады Гедмишх (Царская корона)",
    "Gedmishkh Waterfalls (Tsarskaya Korona)",
    ["park_garden"],
    43.691961, 42.848175,
    "Gần làng Khabaz, huyện Zolsky, Cộng hoà Kabardino-Balkaria, Nga (cách Pyatigorsk khoảng 70 km).",
    "Gedmishkh là cụm thác tuyệt đẹp còn có tên 'Vương miện Sa hoàng' hay 'Bảy mươi dòng', nơi hàng chục tia nước bung ra từ vách đá phủ rêu xanh mướt trông như một chiếc vương miện khổng lồ.",
    "Nằm trong thung lũng sông Gedmishkh ở huyện Zolsky, cụm thác này có nhiều tên gọi dân gian đầy hình ảnh: 'Vương miện Sa hoàng', 'Bảy mươi dòng' (Zhetmish-suu) hay 'thác Avatar'. Điều đặc biệt là nguồn nước không chảy từ một dòng sông lớn, mà rỉ ra từ một mạch ngầm ẩn trong lòng núi ở độ cao khoảng một trăm mét, rồi bung thành hàng chục tia nước mảnh xối xuống vách đá phủ đầy rêu và cây xanh. Khi ánh nắng chiếu vào, cả bức tường nước lấp lánh và toả hơi mát, tạo nên khung cảnh cổ tích khiến du khách liên tưởng đến những cảnh phim thần thoại. Dưới chân thác là hồ nước nhỏ trong vắt và những bậc đá để du khách tới gần. Đường tới Gedmishkh đi qua vùng cao nguyên trập trùng của Zolsky, thường được kết hợp với chuyến thăm các hồ Shadkhurey lân cận.",
    [
        "Hàng chục tia nước bung ra từ vách đá phủ rêu, xếp thành hình 'vương miện'.",
        "Nguồn nước độc đáo rỉ ra từ mạch ngầm trong lòng núi, không phải từ một dòng sông.",
        "Cảnh quan cổ tích, dễ kết hợp cùng các hồ Shadkhurey trong huyện Zolsky.",
    ],
    outdoor_practical(
        "Khoảng 1–2 giờ tại thác.",
        "Tháng 5–9 khi cây cỏ xanh và nước dồi dào.",
        "Đường vào là đường núi, nên đi xe gầm cao hoặc theo tour; đá quanh thác trơn, đi lại cẩn thận.",
    ),
    [
        {"title": "Tourister — Царские водопады (Гедмишх)", "url": "https://www.tourister.ru/world/europe/russia/city/selo-habaz/waterfall/26769"},
        {"title": "Turisticum — Царские водопады Гедмишх", "url": "https://turisticum.ru/gedmish/"},
    ],
    ["waterfall", "gedmishkh", "tsarskaya-korona", "zolsky", "nature", "scenic"],
    maps_text("Водопад Гедмишх Царская корона", "Хабаз", "Gedmishkh Waterfalls", "Kabardino-Balkaria", 43.691961, 42.848175),
))

# 7) Урочище Джилы-Су + водопад Султан -----------------------------------------------
RECORDS.append(rec(
    "dzhily-su-sultan-waterfall",
    "Thung Dzhily-Su và thác Sultan",
    "Урочище Джилы-Су и водопад Султан",
    "Dzhily-Su and Sultan Waterfall",
    ["park_garden"],
    43.433650, 42.533587,
    "Sườn bắc núi Elbrus, cách đỉnh khoảng 14 km về phía bắc, huyện Zolsky, Cộng hoà Kabardino-Balkaria, Nga (độ cao ~2.380 m).",
    "Dzhily-Su là vùng thung lũng khắc nghiệt mà tuyệt đẹp ở sườn bắc Elbrus, nổi tiếng với suối khoáng nóng chữa bệnh và thác Sultan hùng vĩ cao khoảng 40 m đổ xuống từ dòng nước băng tan.",
    "Ở độ cao khoảng 2.380 m dưới chân sườn bắc hoang dã của Elbrus, Dzhily-Su (tiếng Balkar nghĩa là 'nước ấm') là điểm đến kết hợp thiên nhiên kỳ vĩ và nguồn khoáng chữa bệnh. Những mạch nước khoáng nóng giàu sắt và carbonat từ lòng đất phun lên tạo thành các bồn tắm tự nhiên, từ lâu được người dân tin là có tác dụng trị liệu. Cách đó không xa, thác Sultan (Sultan-Su) đổ ầm ầm từ độ cao chừng 40 m; dòng thác do sông Kyzylkol tạo nên từ băng tan phía bắc Elbrus, mùa hè nước ngả màu xám do cuốn theo phù sa và cát. Xung quanh là cao nguyên núi lửa với những cột đá bazan, 'nấm đá', thảm hoa núi cao và tầm nhìn thẳng lên chóp băng Elbrus. Đường tới Dzhily-Su hiểm trở nhưng ngoạn mục, thu hút cả người hành hương khoáng nóng lẫn dân đi bộ đường dài.",
    [
        "Suối khoáng nóng tự nhiên giàu khoáng chất được xem là có tác dụng chữa bệnh.",
        "Thác Sultan hùng vĩ cao khoảng 40 m từ dòng nước băng tan của Elbrus.",
        "Cao nguyên núi lửa với cột đá bazan, 'nấm đá' và tầm nhìn thẳng lên chóp Elbrus.",
    ],
    outdoor_practical(
        "Cả ngày do đường xa và nhiều điểm ngắm (suối, thác, cao nguyên).",
        "Tháng 6–9 khi đèo mở và đường khô; ngoài mùa này đường có thể bị tuyết chặn.",
        "Đường núi rất khắc nghiệt, nên đi xe địa hình hoặc tour; mang đồ ấm vì thời tiết đổi nhanh ở độ cao lớn.",
    ),
    [
        {"title": "Bolshaya Strana — Урочище Джилы-Су", "url": "https://bolshayastrana.com/dostoprimechatelnosti/kabardino-balkariya/dzhily-su-446"},
        {"title": "33ways — Водопад Султан-Су (Джилы-Су)", "url": "https://33ways.ru/rossija/vodopad-sultan-su/"},
    ],
    ["dzhily-su", "sultan-waterfall", "elbrus", "hot-springs", "volcanic", "nature"],
    maps_text("Урочище Джилы-Су водопад Султан", "Приэльбрусье", "Dzhily-Su Sultan Waterfall", "Kabardino-Balkaria", 43.433650, 42.533587),
))

# 8) Аушигерские термальные источники -----------------------------------------------
RECORDS.append(rec(
    "aushiger-thermal-springs",
    "Suối nước nóng Aushiger",
    "Аушигерские термальные источники",
    "Aushiger Thermal Springs",
    ["park_garden"],
    43.374432, 43.721007,
    "Gần làng Aushiger, huyện Chereksky, Cộng hoà Kabardino-Balkaria, Nga (cách Nalchik khoảng 25 km).",
    "Aushiger là khu suối khoáng nóng lộ thiên nổi tiếng của Kabardino-Balkaria, nơi dòng nước ấm giàu khoáng chất từ lòng đất chảy vào các hồ tắm giữa khung cảnh đồng quê và núi non.",
    "Nằm trong thung lũng sông Cherek gần làng Aushiger, khu suối nước nóng này hình thành từ một mũi khoan địa chất thời Xô Viết bất ngờ gặp mạch nước khoáng nóng sâu trong lòng đất. Nước ở đây có nhiệt độ cao (thường quanh mức 45–50°C), giàu khoáng chất và được cho là tốt cho da, khớp và hệ thần kinh. Ngày nay khu vực được cải tạo thành các hồ và bể tắm lộ thiên, hoạt động quanh năm; đặc biệt hấp dẫn vào mùa lạnh khi du khách ngâm mình trong làn nước bốc hơi nghi ngút giữa tiết trời se lạnh, phóng tầm mắt ra đồng ruộng và dãy núi xa. Với giá vé bình dân, Aushiger là điểm thư giãn được yêu thích sau những chuyến khám phá Hồ Xanh, hẻm Cherek hay Thượng Balkaria, và thường xuất hiện trong hầu hết các tour ghép trong ngày quanh Nalchik.",
    [
        "Hồ tắm khoáng nóng lộ thiên quanh năm, ấm áp cả trong mùa đông.",
        "Nước giàu khoáng chất được cho là tốt cho da, khớp và thư giãn.",
        "Điểm nghỉ dưỡng giá bình dân, thường ghép cùng tour Hồ Xanh – Thượng Balkaria.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày, thường từ sáng đến tối muộn (thay đổi theo mùa và từng khu bể).",
        "ticket_vi": "Vé vào bể tắm mức bình dân (khoảng vài trăm rúp), kiểm tra giá cập nhật tại cổng.",
        "duration_vi": "Khoảng 1–2 giờ ngâm tắm và thư giãn.",
        "best_time_vi": "Quanh năm; thú vị nhất vào mùa thu–đông khi tắm nước nóng giữa trời lạnh.",
        "tips_vi": "Mang theo đồ bơi, dép và khăn; không ngâm quá lâu; tránh xuống nước khi vừa ăn no hoặc có bệnh tim mạch nặng.",
    },
    [
        {"title": "Club-Voshod — Термальные источники Аушигера", "url": "https://club-voshod.com/info/pohodnoe_info/dostoprimechatelnosti/prielbrusie/termalnye_istochniki_aushigera/"},
        {"title": "Enjoy-Kavkaz — Аушигерские источники", "url": "https://enjoy-kavkaz.ru/mesta/aushigerskie-istochniki"},
    ],
    ["thermal-springs", "aushiger", "spa", "cherek", "relaxation", "nature"],
    maps_text("Аушигерские термальные источники", "Аушигер", "Aushiger Thermal Springs", "Kabardino-Balkaria", 43.374432, 43.721007),
))

# 9) Безенги (стена и ледник) --------------------------------------------------------
RECORDS.append(rec(
    "bezengi-wall",
    "Bức tường Bezengi và sông băng",
    "Безенгийская стена и ледник Безенги",
    "Bezengi Wall and Glacier",
    ["park_garden"],
    43.111020, 43.147560,
    "Thượng nguồn thung lũng Bezengi, Khu bảo tồn núi cao Kabardino-Balkaria, huyện Chereksky, Cộng hoà Kabardino-Balkaria, Nga.",
    "Bezengi là 'thánh địa' của giới leo núi Nga: bức tường Bezengi dài khoảng 12 km là đoạn cao nhất của dãy Đại Kavkaz, quy tụ phần lớn các đỉnh trên 5.000 m, bên dưới là sông băng lớn nhất Kavkaz.",
    "Ẩn sâu trong thượng nguồn thung lũng Bezengi thuộc Khu bảo tồn núi cao Kabardino-Balkaria, khu vực này là trái tim của vùng núi cao nhất nước Nga ở châu Âu. 'Bức tường Bezengi' – một đoạn sống núi liên tục dài khoảng 12 km – được xem là phần cao và hiểm trở nhất của dãy Đại Kavkaz, nơi tập trung phần lớn những đỉnh 'năm nghìn' như Shkhara, Dzhangi-Tau, Katyn-Tau cùng đỉnh Dykhtau gần đó. Dưới chân tường là sông băng Bezengi dài hơn 17 km, sông băng lớn nhất Kavkaz, trườn xuống như một dòng sông đá và băng khổng lồ. Từ năm 1959, trại leo núi Bezengi ở độ cao khoảng 2.500 m đã trở thành căn cứ huyền thoại cho các đoàn chinh phục; từ đây có những cung đường mòn ngắm sông băng dành cho cả du khách không chuyên. Khung cảnh nơi đây khắc nghiệt, hùng vĩ và gần như nguyên sơ, là ước mơ của những người mê núi cao.",
    [
        "Bức tường Bezengi dài ~12 km, đoạn cao nhất dãy Đại Kavkaz với nhiều đỉnh trên 5.000 m.",
        "Sông băng Bezengi dài hơn 17 km – lớn nhất vùng Kavkaz.",
        "Trại leo núi Bezengi huyền thoại (từ 1959) và các cung trekking ngắm sông băng.",
    ],
    outdoor_practical(
        "Từ nửa ngày (đến trại và điểm ngắm) tới nhiều ngày cho leo núi chuyên nghiệp.",
        "Tháng 6–9 là mùa leo núi và trekking chính.",
        "Đây là vùng biên giới và núi cao: cần giấy tờ/giấy phép, hướng dẫn viên và trang bị phù hợp; không tự đi lên sông băng nếu thiếu kinh nghiệm.",
    ),
    [
        {"title": "Wikipedia (RU) — Безенги (ледник)", "url": "https://ru.wikipedia.org/wiki/Безенги_(ледник)"},
        {"title": "Vpoxod — Безенги", "url": "https://www.vpoxod.ru/page/toponym/bezengi_info"},
    ],
    ["bezengi", "glacier", "bezengi-wall", "mountaineering", "5000m-peaks", "nature"],
    maps_text("Альплагерь Безенги", "Черекский район", "Bezengi Alpine Camp", "Kabardino-Balkaria", 43.111020, 43.147560),
))

# 10) Водопад Девичьи косы -----------------------------------------------------------
RECORDS.append(rec(
    "devichi-kosy-waterfall",
    "Thác Devichi Kosy (Bím tóc thiếu nữ)",
    "Водопад Девичьи косы",
    "Devichi Kosy Waterfall (Maiden's Braids)",
    ["park_garden"],
    43.273979, 42.492363,
    "Sườn nam Pik Terskol, phía trên làng Terskol, thung lũng Baksan, huyện Elbrussky, Cộng hoà Kabardino-Balkaria, Nga (độ cao ~2.800 m).",
    "Devichi Kosy là thác nước duyên dáng trên sườn Pik Terskol, nơi dòng nước xoè ra thành vô số tia mảnh như những lọn tóc tết của thiếu nữ, đổ xuống từ độ cao khoảng 30 m.",
    "Nằm ở độ cao khoảng 2.800 m trên sườn nam của đỉnh Terskol, ngay trong khu Prielbrusye, thác 'Bím tóc thiếu nữ' được sông nhỏ Chyranbashi-Su (nghĩa tiếng Karachay-Balkar cũng là 'bím tóc thiếu nữ') tạo nên. Điều làm nên vẻ đẹp riêng của thác là cách dòng nước không đổ thành một khối, mà trải rộng trên vách đá đen thành hàng trăm tia nước mảnh song song, trông hệt như mái tóc dài được tết công phu, lấp lánh dưới nắng và toả hơi mát. Từ chân thác, du khách có thể ngắm toàn cảnh thung lũng Baksan và, trong ngày trời quang, cả chóp băng Elbrus phía xa. Con đường mòn lên thác cũng dẫn tiếp tới đài quan sát 'Pik Terskol' trên cao, nên đây là một trong những tuyến đi bộ ngắm cảnh được yêu thích nhất vùng chân Elbrus.",
    [
        "Dòng nước xoè thành hàng trăm tia mảnh như mái tóc tết, cao khoảng 30 m.",
        "Tầm nhìn xuống thung lũng Baksan và lên chóp băng Elbrus trong ngày quang.",
        "Cung đi bộ nối tiếp lên đài quan sát Pik Terskol trên cao.",
    ],
    outdoor_practical(
        "Khoảng 3–5 giờ cả đi và về từ Terskol (đi bộ lên dốc).",
        "Tháng 6–9 khi đường mòn khô ráo, nước dồi dào.",
        "Đường lên dốc và ở độ cao lớn, đi giày leo núi, mang nước và đồ ấm; khởi hành sớm để tránh mây chiều.",
    ),
    [
        {"title": "Vpoxod — Водопад Девичьи косы", "url": "https://www.vpoxod.ru/page/toponym/devichi-kosy-vodopad_info"},
        {"title": "Enjoy-Kavkaz — Водопад Девичьи косы", "url": "https://enjoy-kavkaz.ru/mesta/vodopad-devichi-kosy-ili-chyranbashi-su"},
    ],
    ["waterfall", "devichi-kosy", "terskol", "prielbrusye", "hiking", "nature"],
    maps_text("Водопад Девичьи косы", "Терскол", "Devichi Kosy Waterfall", "Kabardino-Balkaria", 43.273979, 42.492363),
))

# 11) Поляна нарзанов (Приэльбрусье) -------------------------------------------------
RECORDS.append(rec(
    "polyana-narzanov",
    "Đồng Narzan (Poляna nарзанов) Prielbrusye",
    "Поляна нарзанов (Приэльбрусье)",
    "Narzan Glade (Prielbrusye)",
    ["park_garden"],
    43.245359, 42.523362,
    "Thượng nguồn hẻm Baksan, gần làng Baydaevo, khu Prielbrusye, huyện Elbrussky, Cộng hoà Kabardino-Balkaria, Nga.",
    "Đồng Narzan là một thung lũng nhỏ giữa rừng thông và bạch dương ở thượng nguồn hẻm Baksan, nơi khoảng hai chục mạch nước khoáng narzan tự nhiên phun trào ngay trên mặt đất.",
    "Trải rộng chừng 3 km vuông giữa rừng thông và bạch dương ở thượng nguồn hẻm Baksan, gần làng Baydaevo, Đồng Narzan là điểm dừng chân thư giãn quen thuộc trên đường tới Elbrus. Ở đây, khoảng hai chục mạch nước khoáng narzan – loại nước khoáng có ga tự nhiên đặc trưng của Kavkaz – rỉ và phun lên từ lòng đất, để lại những vệt khoáng màu vàng cam quanh miệng nguồn. Du khách có thể trực tiếp nếm thử làn nước lạnh, chua nhẹ và sủi bọt được cho là tốt cho tiêu hoá. Bao quanh là đồng cỏ núi cao, suối chảy và tầm nhìn ra các đỉnh tuyết, khiến nơi đây trở thành điểm picnic lý tưởng. Khu vực có hạ tầng du lịch nhỏ gọn với quán cà phê, chòi nghỉ, cửa hàng lưu niệm và bãi đỗ xe, thuận tiện cho các đoàn đang trên hành trình khám phá vùng Prielbrusye.",
    [
        "Khoảng hai chục mạch nước khoáng narzan tự nhiên phun trào giữa đồng cỏ.",
        "Có thể nếm thử nước khoáng có ga lạnh, sủi bọt ngay tại nguồn.",
        "Điểm picnic giữa rừng thông với tầm nhìn ra các đỉnh tuyết của Prielbrusye.",
    ],
    outdoor_practical(
        "Khoảng 1 giờ nghỉ chân và nếm nước khoáng.",
        "Tháng 5–10; mùa hè mát mẻ và cây cỏ xanh tươi.",
        "Nếm thử nước khoáng vừa phải; kết hợp trên đường tới Terskol, Cheget hoặc Azau.",
    ),
    [
        {"title": "Kavkaz.travel — Поляна нарзанов", "url": "https://kavkaz.travel/attractions/31"},
        {"title": "Club-Voshod — Поляна Нарзанов в Приэльбрусье", "url": "https://club-voshod.com/info/pohodnoe_info/dostoprimechatelnosti/prielbrusie/polyana_narzanov/"},
    ],
    ["narzan", "mineral-springs", "prielbrusye", "baksan", "picnic", "nature"],
    maps_text("Поляна нарзанов", "Приэльбрусье", "Narzan Glade", "Kabardino-Balkaria", 43.245359, 42.523362),
))

# 12) Перевал Актопрак ---------------------------------------------------------------
RECORDS.append(rec(
    "aktoprak-pass",
    "Đèo Aktoprak",
    "Перевал Актопрак",
    "Aktoprak Pass",
    ["park_garden"],
    43.400410, 43.094700,
    "Nối thung lũng Baksan và Chegem, huyện Chegemsky/Baksansky, Cộng hoà Kabardino-Balkaria, Nga.",
    "Aktoprak là con đèo núi ngoạn mục nối hai thung lũng Baksan và Chegem, băng qua vùng đồi đá sét trắng trơ trọi mang vẻ đẹp gần như 'ngoài hành tinh'.",
    "Tên gọi Aktoprak trong tiếng Karachay-Balkar nghĩa là 'đất sét trắng', phản ánh đúng cảnh quan đặc trưng của con đèo: những sườn đồi trọc màu trắng ngà, xám và hồng nhạt uốn lượn không cây cối, gợi liên tưởng tới một hành tinh khác. Là lối tắt dài khoảng 22 km nối thung lũng Baksan với thung lũng Chegem, con đường đèo quanh co men theo sườn núi, mở ra hết tầm nhìn ngoạn mục này đến tầm nhìn khác, và trong ngày trời quang có thể thấy cả chóp Elbrus phía xa. Dọc đường còn có dấu vết của những tuyến thương mại và tháp canh cổ, cho thấy đây từng là hành lang giao thương quan trọng qua núi. Với cảnh sắc độc đáo và cảm giác phiêu lưu, Aktoprak là một trong những cung đường được dân mê xê dịch và nhiếp ảnh săn tìm ở Kabardino-Balkaria.",
    [
        "Cảnh quan đồi đá sét trắng trơ trọi độc đáo như 'ngoài hành tinh'.",
        "Cung đường đèo nối Baksan và Chegem, nhiều điểm ngắm toàn cảnh núi non.",
        "Ngày trời quang có thể thấy chóp Elbrus; dấu tích tuyến thương mại cổ.",
    ],
    outdoor_practical(
        "Khoảng 1,5–2 giờ chạy đèo (nên tính 3–4 giờ kể cả dừng ngắm).",
        "Cuối xuân đến đầu thu (tháng 5–10); mùa đông đường trơn tuyết, cần thận trọng.",
        "Đường hẹp, quanh co và một số đoạn không trải nhựa; nên đi xe gầm cao, lái chậm và nhường nhau.",
    ),
    [
        {"title": "Club-Voshod — Перевал Актопрак", "url": "https://club-voshod.com/info/pohodnoe_info/dostoprimechatelnosti/prielbrusie/pereval_aktoprak/"},
        {"title": "33ways — Перевал Актопрак", "url": "https://33ways.ru/rossija/pereval-aktoprack/"},
    ],
    ["mountain-pass", "aktoprak", "scenic-road", "baksan", "chegem", "nature"],
    maps_text("Перевал Актопрак", "Кабардино-Балкария", "Aktoprak Pass", "Kabardino-Balkaria", 43.400410, 43.094700),
))

# 13) Обсерватория «Пик Терскол» -----------------------------------------------------
RECORDS.append(rec(
    "terskol-observatory",
    "Đài thiên văn Pik Terskol",
    "Обсерватория «Пик Терскол»",
    "Peak Terskol Observatory",
    ["other"],
    43.274722, 42.500833,
    "Trên đỉnh Terskol, phía trên làng Terskol, khu Prielbrusye, huyện Elbrussky, Cộng hoà Kabardino-Balkaria, Nga (độ cao ~3.150 m).",
    "Pik Terskol là một đài thiên văn quốc tế nằm ở độ cao khoảng 3.150 m trên sườn Elbrus, một trong những vị trí quan sát bầu trời tốt nhất châu Âu nhờ không khí khô và trong.",
    "Được thành lập năm 1980 trên đỉnh Terskol, ngay trên làng cùng tên và chỉ cách chóp Elbrus khoảng 10 km, đài thiên văn quốc tế 'Pik Terskol' là một trong những cơ sở quan sát vũ trụ độc đáo nhất nước Nga. Ở độ cao khoảng 3.150 m, không khí nơi đây rất khô, ít hơi nước và cực kỳ trong, giúp bầu trời đêm đạt độ nét hiếm có với số giờ quang đãng lên tới cả nghìn giờ mỗi năm – khiến đây được đánh giá là một trong những điểm ngắm sao tốt nhất châu Âu. Đài được trang bị các kính thiên văn Zeiss (Zeiss-2000, Zeiss-600), kính mặt trời và hệ thống xử lý dữ liệu hiện đại, phục vụ nghiên cứu thiên văn của Nga và quốc tế. Với du khách, hành trình lên Pik Terskol vừa là chuyến đi bộ đường dài ngoạn mục dọc sườn Elbrus (thường ghép với thác Devichi Kosy), vừa là cơ hội chiêm ngưỡng một 'con mắt' khoa học đặt giữa mái nhà Kavkaz.",
    [
        "Đài thiên văn quốc tế ở độ cao ~3.150 m, chỉ cách chóp Elbrus khoảng 10 km.",
        "Một trong những điểm ngắm bầu trời tốt nhất châu Âu nhờ không khí khô và trong.",
        "Trang bị kính thiên văn Zeiss và kính mặt trời; hành trình lên đài rất ngoạn mục.",
    ],
    outdoor_practical(
        "Nửa ngày đến cả ngày cho hành trình đi bộ lên và về.",
        "Tháng 6–9 khi đường mòn khô ráo và tầm nhìn tốt.",
        "Đường lên ở độ cao lớn, cần thể lực và làm quen độ cao; tham quan bên trong đài cần liên hệ trước.",
        ticket="Khu vực núi ngoài trời miễn phí; tham quan bên trong đài (nếu có) cần đăng ký trước.",
        hours="Ngoài trời tự do ban ngày; tham quan nội bộ đài theo lịch hẹn.",
    ),
    [
        {"title": "Wikipedia (RU) — Обсерватория Пик Терскол", "url": "https://ru.wikipedia.org/wiki/Обсерватория_Пик_Терскол"},
        {"title": "Observatories.ru — Терскольская обсерватория", "url": "https://observatories.ru/pik-terskol/"},
    ],
    ["observatory", "astronomy", "pik-terskol", "elbrus", "science", "viewpoint"],
    maps_org("https://yandex.com/maps/org/pik_terskol/188069680998/", "Peak Terskol Observatory", "Kabardino-Balkaria"),
))

# 14) Национальный музей КБР ---------------------------------------------------------
RECORDS.append(rec(
    "national-museum-kbr",
    "Bảo tàng Quốc gia Kabardino-Balkaria",
    "Национальный музей КБР",
    "National Museum of Kabardino-Balkaria",
    ["museum"],
    43.486716, 43.608428,
    "Ул. Горького 62, thành phố Nalchik, Cộng hoà Kabardino-Balkaria, Nga.",
    "Bảo tàng Quốc gia Kabardino-Balkaria là bảo tàng lâu đời nhất nước cộng hoà, thành lập năm 1921, lưu giữ hàng loạt hiện vật tái hiện lịch sử, khảo cổ và văn hoá của các dân tộc bản địa.",
    "Ra đời năm 1921 trong những năm đầu chính quyền Xô Viết, Bảo tàng Quốc gia Kabardino-Balkaria (tiền thân là bảo tàng địa phương) là kho tàng ký ức phong phú của cả vùng đất. Từ một căn phòng nhỏ trong nhà riêng của vị giám đốc đầu tiên, bảo tàng đã phát triển thành cơ sở chính với bảy phòng trưng bày thường xuyên cùng nhiều phòng triển lãm, giới thiệu lịch sử các dân tộc Kabardin và Balkar từ thời tiền sử tới hiện đại. Bộ sưu tập trải rộng từ hiện vật khảo cổ, vũ khí, trang phục dân tộc, đồ thủ công, thảm dệt cho tới tài liệu về đời sống miền núi, phong tục và các sự kiện lịch sử của Bắc Kavkaz. Nằm ngay trung tâm Nalchik trên phố Gorky, đây là điểm khởi đầu lý tưởng để hiểu bối cảnh văn hoá – lịch sử trước khi khám phá thiên nhiên hùng vĩ của nước cộng hoà.",
    [
        "Bảo tàng lâu đời nhất nước cộng hoà (thành lập 1921).",
        "Bảy phòng trưng bày về lịch sử, khảo cổ và văn hoá dân tộc Kabardin – Balkar.",
        "Vị trí trung tâm Nalchik, thuận tiện kết hợp tham quan phố cổ.",
    ],
    {
        "hours_vi": "Thường mở cửa 10:00–18:00, nghỉ thứ Hai (nên kiểm tra lịch trước khi đến).",
        "ticket_vi": "Vé vào cửa mức bình dân; có ưu đãi cho học sinh, sinh viên và người cao tuổi.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm; phù hợp cho ngày mưa hoặc buổi nghỉ giữa các chuyến đi núi.",
        "tips_vi": "Kết hợp với Bảo tàng Mỹ thuật Ткаченко và Nhà thờ Hồi giáo lớn gần đó trong cùng một buổi.",
    },
    [
        {"title": "Culture.ru — Национальный музей КБР", "url": "https://www.culture.ru/institutes/20536/nacionalnyi-muzei-kabardino-balkarskoi-respubliki"},
        {"title": "2ГИС — Национальный музей КБР (ул. Горького 62)", "url": "https://2gis.ru/nalchik/firm/70000001023655420"},
    ],
    ["museum", "history", "archaeology", "ethnography", "nalchik"],
    maps_org("https://yandex.com/maps/org/natsionalny_muzey_kbr/1343032582/", "National Museum of Kabardino-Balkaria", "Nalchik"),
))

# 15) Музей ИЗО им. Ткаченко ---------------------------------------------------------
RECORDS.append(rec(
    "fine-arts-museum-tkachenko",
    "Bảo tàng Mỹ thuật Kabardino-Balkaria (Tkachenko)",
    "Кабардино-Балкарский музей изобразительных искусств им. А. Л. Ткаченко",
    "Tkachenko Fine Arts Museum",
    ["museum"],
    43.480501, 43.600367,
    "Пр. Ленина 35, thành phố Nalchik, Cộng hoà Kabardino-Balkaria, Nga.",
    "Bảo tàng Mỹ thuật mang tên A. L. Tkachenko là bảo tàng nghệ thuật chính của Kabardino-Balkaria, thành lập năm 1960, trưng bày tranh, tác phẩm nghệ thuật Nga, nước ngoài và của các nghệ sĩ địa phương.",
    "Được thành lập năm 1960 và mang tên nhà sư phạm Andrey Lukich Tkachenko – người hơn nửa thế kỷ dẫn dắt xưởng mỹ thuật thiếu nhi ở Nalchik – bảo tàng là trung tâm đời sống nghệ thuật tạo hình của nước cộng hoà. Tuy khiêm tốn về diện tích (nằm ở tầng trệt một toà nhà trên đại lộ Lenin trung tâm), bộ sưu tập lại phong phú với hàng trăm tác phẩm nghệ thuật Nga và nước ngoài cùng hàng nghìn hiện vật của các tác giả bản địa: tranh sơn dầu, đồ hoạ, điêu khắc, nghệ thuật trang trí ứng dụng và thảm dệt truyền thống. Bảo tàng thường xuyên tổ chức triển lãm luân phiên giới thiệu họa sĩ đương đại vùng Bắc Kavkaz, trở thành không gian quen thuộc của giới yêu nghệ thuật Nalchik. Vị trí ngay trung tâm khiến nơi đây dễ ghép cùng Bảo tàng Quốc gia và các điểm tham quan phố trung tâm trong một buổi đi bộ.",
    [
        "Bảo tàng nghệ thuật tạo hình chính của nước cộng hoà (thành lập 1960).",
        "Sưu tập tranh, đồ hoạ, điêu khắc Nga – quốc tế và của nghệ sĩ Bắc Kavkaz.",
        "Thường xuyên có triển lãm luân phiên; nằm ngay trung tâm Nalchik.",
    ],
    {
        "hours_vi": "Thường mở cửa 10:00–18:00, nghỉ thứ Hai (nên kiểm tra lịch trước khi đến).",
        "ticket_vi": "Vé vào cửa mức bình dân; có ưu đãi cho học sinh, sinh viên.",
        "duration_vi": "Khoảng 45 phút đến 1 giờ.",
        "best_time_vi": "Quanh năm; hợp cho ngày mưa hoặc buổi thư giãn trong thành phố.",
        "tips_vi": "Kiểm tra lịch triển lãm hiện hành; kết hợp cùng Bảo tàng Quốc gia KBR gần đó.",
    },
    [
        {"title": "Museum.ru — КБ музей ИЗО им. А. Л. Ткаченко", "url": "http://www.museum.ru/M1557"},
        {"title": "2ГИС — Музей ИЗО им. Ткаченко (пр. Ленина 35)", "url": "https://2gis.ru/nalchik/firm/70000001023661460"},
    ],
    ["museum", "fine-arts", "gallery", "tkachenko", "nalchik"],
    maps_text("Музей изобразительных искусств им. Ткаченко", "Нальчик", "Tkachenko Fine Arts Museum", "Nalchik", 43.480501, 43.600367),
))

# 16) «Наследие нартов» --------------------------------------------------------------
RECORDS.append(rec(
    "nartov-heritage-museum",
    "Bảo tàng 'Di sản người Nart'",
    "Музей культуры и искусства «Наследие нартов»",
    "Heritage of the Narts Museum",
    ["museum"],
    43.486874, 43.575591,
    "Ул. Байсултанова 39 (trung tâm 'Акрополь'), thành phố Nalchik, Cộng hoà Kabardino-Balkaria, Nga.",
    "'Nаследие нартов' là bảo tàng văn hoá – nghệ thuật hiện đại theo phong cách tương tác, đưa du khách vào thế giới sử thi Nart và di sản của các dân tộc Bắc Kavkaz.",
    "Nằm trong tổ hợp 'Акрополь' ở Nalchik, bảo tàng 'Di sản người Nart' là một điểm đến hiện đại, khác hẳn các bảo tàng cổ điển của thành phố. Không gian trưng bày được thiết kế theo hướng tương tác và trải nghiệm, lấy cảm hứng từ sử thi Nart – kho tàng thần thoại chung của nhiều dân tộc Kavkaz kể về những người anh hùng khổng lồ, thần lửa Sosruko và các chiến công huyền thoại. Qua hình ảnh, âm thanh, mô hình và các khu trải nghiệm, bảo tàng giới thiệu trang phục, vũ khí, nhạc cụ, phong tục và tinh thần của người Kabardin, Balkar cùng các tộc người lân cận một cách sinh động, dễ tiếp cận với cả trẻ em. Đây là lựa chọn thú vị cho gia đình và những ai muốn hiểu chiều sâu văn hoá bản địa theo cách trực quan, sinh động, đặc biệt thích hợp khi kết hợp cùng các bảo tàng truyền thống ở trung tâm Nalchik.",
    [
        "Bảo tàng tương tác hiện đại lấy cảm hứng từ sử thi Nart của Kavkaz.",
        "Trưng bày sinh động về trang phục, vũ khí, nhạc cụ và phong tục bản địa.",
        "Phù hợp cho gia đình và trẻ em nhờ cách trình bày trực quan.",
    ],
    {
        "hours_vi": "Thường mở cửa buổi trưa đến tối (khoảng 11:00–23:00); nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa theo bảng giá của tổ hợp; kiểm tra tại quầy.",
        "duration_vi": "Khoảng 1 giờ.",
        "best_time_vi": "Quanh năm; phù hợp cho buổi tối hoặc ngày thời tiết xấu.",
        "tips_vi": "Là bảo tàng tư nhân/hiện đại, nên xác nhận giờ mở cửa và giá vé trước khi đến.",
    },
    [
        {"title": "2ГИС — Наследие нартов (ул. Байсултанова 39)", "url": "https://2gis.ru/nalchik/firm/70000001076238963"},
    ],
    ["museum", "interactive", "nart-epic", "culture", "nalchik", "modern"],
    maps_text("Наследие нартов музей", "Нальчик", "Heritage of the Narts Museum", "Nalchik", 43.486874, 43.575591),
))

# 17) Соборная мечеть Нальчика -------------------------------------------------------
RECORDS.append(rec(
    "nalchik-cathedral-mosque",
    "Nhà thờ Hồi giáo lớn Nalchik",
    "Соборная (Центральная) мечеть Нальчика",
    "Nalchik Cathedral Mosque",
    ["church"],
    43.488435, 43.616783,
    "Пр. Шогенцукова 41, thành phố Nalchik, Cộng hoà Kabardino-Balkaria, Nga.",
    "Nhà thờ Hồi giáo lớn Nalchik là thánh đường Hồi giáo trung tâm của thành phố, khánh thành năm 2004, nổi bật với hai tháp minaret cao và mái vòm xanh giữa một quảng trường cây xanh.",
    "Khánh thành ngày 21 tháng 5 năm 2004, Nhà thờ Hồi giáo lớn (jum'a) của Nalchik là trung tâm tôn giáo của cộng đồng Hồi giáo nước cộng hoà và là một trong những công trình đẹp nhất trung tâm thành phố. Toạ lạc trong một quảng trường cây xanh ngay trên đại lộ Shogentsukov, thánh đường gây ấn tượng với khối kiến trúc cân đối, mái vòm chính màu xanh và đôi tháp minaret cao vươn lên bầu trời. Không gian bên trong rộng rãi, trang trí thanh nhã theo phong cách Hồi giáo với thư pháp và hoa văn hình học. Là nơi diễn ra các buổi cầu nguyện tập thể, đặc biệt vào thứ Sáu và các dịp lễ lớn, nhà thờ vừa là điểm sinh hoạt tâm linh vừa là biểu tượng của diện mạo Nalchik hiện đại. Du khách có thể tham quan bên ngoài và, nếu tôn trọng quy tắc trang phục và ứng xử, vào bên trong ngoài giờ cầu nguyện.",
    [
        "Thánh đường Hồi giáo trung tâm của Nalchik, khánh thành năm 2004.",
        "Kiến trúc cân đối với mái vòm xanh và đôi tháp minaret cao.",
        "Nằm trong quảng trường cây xanh ngay trung tâm, biểu tượng của thành phố.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày; ngoài giờ cầu nguyện du khách có thể vào tham quan.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; tránh đúng giờ cầu nguyện nếu chỉ muốn tham quan.",
        "tips_vi": "Ăn mặc kín đáo, phụ nữ nên trùm khăn; bỏ giày khi vào và giữ yên lặng, xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Wikipedia (RU) — Центральная мечеть Нальчика", "url": "https://ru.wikipedia.org/wiki/Центральная_мечеть_Нальчика"},
        {"title": "2ГИС — Соборная мечеть (пр. Шогенцукова 41)", "url": "https://2gis.ru/nalchik/firm/70000001029461663"},
    ],
    ["mosque", "islam", "religion", "nalchik", "landmark"],
    maps_text("Соборная мечеть", "Нальчик", "Nalchik Cathedral Mosque", "Nalchik", 43.488435, 43.616783),
))

# 18) Симеоновский собор -------------------------------------------------------------
RECORDS.append(rec(
    "simeon-stylites-cathedral",
    "Nhà thờ Chính thống giáo Thánh Simeon Stylites",
    "Собор преподобного Симеона Столпника",
    "Cathedral of St. Simeon Stylites",
    ["church"],
    43.484574, 43.613961,
    "Ул. Пятигорская 82, thành phố Nalchik, Cộng hoà Kabardino-Balkaria, Nga.",
    "Nhà thờ chính toà Thánh Simeon Stylites là nhà thờ Chính thống giáo chính của Nalchik, có gốc gác từ ngôi nhà thờ pháo đài thế kỷ XIX, ngày nay là di tích văn hoá cấp vùng.",
    "Nhà thờ Thánh Simeon Stylites gắn liền với lịch sử pháo đài Nalchik: ngôi nhà thờ đầu tiên được dựng năm 1851 dưới thời Hoàng đế Nikolai I, do các sĩ quan trung đoàn Kabardin xây dựng và cung hiến cho Thánh Simeon Stylites để tưởng nhớ một người thân qua đời trong trận dịch tả. Sau khi bị đóng cửa và phá huỷ vào cuối thập niên 1920, ngôi thánh đường được dựng lại năm 1943 tại vị trí một nhà nguyện trong nghĩa trang cũ và dần được mở rộng qua thời gian, có thêm bàn thờ phụ. Ngày nay đây là nhà thờ Chính thống giáo chính của thành phố, được công nhận là đối tượng di sản văn hoá cấp vùng, với kiến trúc truyền thống Nga, mái vòm và tháp chuông đặc trưng. Không gian yên tĩnh, các buổi lễ và tiếng chuông ngân khiến nơi đây là điểm đến tâm linh quan trọng của cộng đồng Chính thống giáo địa phương và cũng là một chứng nhân lịch sử của Nalchik.",
    [
        "Nhà thờ Chính thống giáo chính của Nalchik, gốc từ nhà thờ pháo đài năm 1851.",
        "Được công nhận là di tích văn hoá cấp vùng.",
        "Kiến trúc Nga truyền thống với mái vòm và tháp chuông, không gian tĩnh lặng.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày (nhiều khung giờ theo lịch lễ); có thể vào tham quan và cầu nguyện.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; sáng và giờ lễ có không khí trang nghiêm nhất.",
        "tips_vi": "Ăn mặc kín đáo, phụ nữ nên trùm khăn; giữ yên lặng và xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Sobory.ru — Церковь Симеона Столпника (Нальчик)", "url": "https://sobory.ru/article/?object=07053"},
        {"title": "2ГИС — Симеоновский собор (ул. Пятигорская 82)", "url": "https://2gis.ru/nalchik/firm/70000001023665767"},
    ],
    ["orthodox", "cathedral", "church", "religion", "nalchik", "heritage"],
    maps_text("Симеоновский собор", "Нальчик", "Cathedral of St. Simeon Stylites", "Nalchik", 43.484574, 43.613961),
))

# 19) Кабардинский драмтеатр им. Шогенцукова -----------------------------------------
RECORDS.append(rec(
    "drama-theatre-shogentsukov",
    "Nhà hát Kịch Kabardin (Ali Shogentsukov)",
    "Кабардинский драматический театр им. Али Шогенцукова",
    "Kabardian Drama Theatre named after Ali Shogentsukov",
    ["theatre"],
    43.475648, 43.600753,
    "Пр. Шогенцукова 2 (cạnh vườn Atazhukinsky), thành phố Nalchik, Cộng hoà Kabardino-Balkaria, Nga.",
    "Nhà hát Kịch Quốc gia Kabardin mang tên nhà thơ Ali Shogentsukov là sân khấu kịch tiếng Kabardin lâu đời, hoạt động từ năm 1937, với toà nhà bề thế ngay cửa vào vườn Atazhukinsky.",
    "Thành lập năm 1937, Nhà hát Kịch Quốc gia Kabardin là một trong những thiết chế văn hoá quan trọng nhất của nước cộng hoà, gìn giữ và phát triển nghệ thuật sân khấu bằng tiếng Kabardin. Nhà hát mang tên Ali Shogentsukov – nhà thơ, người đặt nền móng cho văn học Kabardin hiện đại – và trình diễn cả kịch cổ điển thế giới lẫn các vở dựa trên lịch sử, sử thi và đời sống của người Kabardin. Toà nhà nhà hát toạ lạc ngay lối vào công viên trung tâm Atazhukinsky trên đại lộ Shogentsukov, với mặt tiền bề thế đã trở thành một điểm nhấn kiến trúc quen thuộc của Nalchik. Bên cạnh sân khấu kịch Kabardin, khu vực này còn tập trung nhiều nhà hát khác của thành phố, tạo thành một 'khu văn hoá' sôi động. Với du khách, một buổi tối xem kịch ở đây (dù có thể cần hỗ trợ ngôn ngữ) là cách thú vị để cảm nhận đời sống nghệ thuật đương đại của vùng Bắc Kavkaz.",
    [
        "Sân khấu kịch tiếng Kabardin lâu đời, hoạt động từ năm 1937.",
        "Mang tên Ali Shogentsukov – người đặt nền móng văn học Kabardin hiện đại.",
        "Toà nhà bề thế ngay cửa vào vườn trung tâm Atazhukinsky, điểm nhấn của Nalchik.",
    ],
    {
        "hours_vi": "Mở cửa theo lịch biểu diễn; phòng vé hoạt động ban ngày và trước giờ diễn.",
        "ticket_vi": "Vé xem biểu diễn theo từng chương trình; mua tại phòng vé hoặc trực tuyến.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ; ngắm ngoại thất chỉ vài phút.",
        "best_time_vi": "Mùa diễn thường từ mùa thu đến mùa xuân; kiểm tra lịch trước.",
        "tips_vi": "Các vở chủ yếu bằng tiếng Kabardin/Nga; hỏi trước về nội dung nếu cần; kết hợp dạo công viên Atazhukinsky liền kề.",
    },
    [
        {"title": "Wikipedia (RU) — Кабардинский драматический театр", "url": "https://ru.wikipedia.org/wiki/Кабардинский_драматический_театр"},
        {"title": "2ГИС — Драмтеатр им. Али Шогенцукова (пр. Шогенцукова 2)", "url": "https://2gis.ru/nalchik/firm/70000001023668618"},
    ],
    ["theatre", "drama", "kabardian", "shogentsukov", "nalchik", "culture"],
    maps_org("https://yandex.com/maps/org/kabardinskiy_gosudarstvenny_dramaticheskiy_teatr_imeni_ali_shogentsukova/1077748846/", "Kabardian Drama Theatre", "Nalchik"),
))

# 20) Государственный музыкальный театр КБР ------------------------------------------
RECORDS.append(rec(
    "musical-theatre-kbr",
    "Nhà hát Nhạc kịch Quốc gia Kabardino-Balkaria",
    "Государственный музыкальный театр КБР",
    "State Musical Theatre of Kabardino-Balkaria",
    ["theatre"],
    43.485746, 43.606460,
    "Пр. Ленина 53а, thành phố Nalchik, Cộng hoà Kabardino-Balkaria, Nga.",
    "Nhà hát Nhạc kịch Quốc gia Kabardino-Balkaria là sân khấu ca nhạc chính của nước cộng hoà, nơi trình diễn opera, operetta, nhạc kịch và ballet, gắn với đời sống âm nhạc dân tộc.",
    "Nằm trên đại lộ Lenin trung tâm Nalchik, Nhà hát Nhạc kịch Quốc gia Kabardino-Balkaria là trung tâm của nghệ thuật ca nhạc sân khấu trong vùng. Đây là nơi dàn dựng và trình diễn đa dạng thể loại: opera, operetta, nhạc kịch, các chương trình ca múa nhạc dân tộc và những vở lấy cảm hứng từ văn hoá Kabardin – Balkar, bên cạnh các tác phẩm kinh điển của Nga và thế giới. Với dàn nghệ sĩ, nhạc công và vũ đoàn của nước cộng hoà, nhà hát góp phần gìn giữ và phổ biến âm nhạc dân gian Bắc Kavkaz đồng thời đưa các tác phẩm hàn lâm đến với công chúng địa phương. Toà nhà hiện đại với khán phòng nhiều tầng là điểm hẹn văn hoá quen thuộc của người dân Nalchik. Một buổi tối thưởng thức chương trình tại đây mang đến cho du khách trải nghiệm sống động về bản sắc âm nhạc và nghệ thuật biểu diễn của vùng đất này.",
    [
        "Sân khấu ca nhạc chính của nước cộng hoà: opera, operetta, nhạc kịch, ballet.",
        "Chương trình ca múa nhạc dân tộc Kabardin – Balkar bên cạnh tác phẩm kinh điển.",
        "Toà nhà hiện đại ngay trung tâm Nalchik, điểm hẹn văn hoá của thành phố.",
    ],
    {
        "hours_vi": "Mở cửa theo lịch biểu diễn; phòng vé hoạt động ban ngày và trước giờ diễn.",
        "ticket_vi": "Vé theo từng chương trình; mua tại phòng vé hoặc trực tuyến.",
        "duration_vi": "Một buổi diễn khoảng 2–2,5 giờ.",
        "best_time_vi": "Mùa diễn chính từ mùa thu đến mùa xuân; kiểm tra lịch trước.",
        "tips_vi": "Đặt vé trước cho các buổi diễn nổi bật; đến sớm để ổn định chỗ ngồi.",
    },
    [
        {"title": "2ГИС — Государственный музыкальный театр (пр. Ленина 53а)", "url": "https://2gis.ru/nalchik/firm/70000001029403284"},
    ],
    ["theatre", "musical", "opera", "ballet", "nalchik", "culture"],
    maps_text("Государственный музыкальный театр", "Нальчик", "State Musical Theatre", "Nalchik", 43.485746, 43.606460),
))

# 21) Мемориал жертв политических репрессий -----------------------------------------
RECORDS.append(rec(
    "deportation-memorial",
    "Đài tưởng niệm nạn nhân trục xuất người Balkar",
    "Мемориал жертв политических репрессий 1944–1957 годов",
    "Memorial to Victims of Political Repressions (1944-1957)",
    ["monument"],
    43.453368, 43.581099,
    "Ул. Балкарова 4а, khu Долинск, thành phố Nalchik, Cộng hoà Kabardino-Balkaria, Nga.",
    "Đài tưởng niệm nạn nhân đàn áp chính trị 1944–1957 tưởng nhớ bi kịch trục xuất toàn bộ dân tộc Balkar, kết hợp không gian tưởng niệm và bảo tàng ký ức xúc động.",
    "Đài tưởng niệm và bảo tàng này tưởng nhớ một trong những trang bi thương nhất lịch sử vùng đất: ngày 8 tháng 3 năm 1944, gần như toàn bộ dân tộc Balkar bị chính quyền Xô Viết cưỡng bức trục xuất khỏi quê hương tới Trung Á, và chỉ được trở về sau năm 1957. Nằm ở khu Dolinsk của Nalchik, tổ hợp gồm không gian tưởng niệm ngoài trời và một bảo tàng lưu giữ tài liệu, hình ảnh, hiện vật kể lại nỗi đau ly tán, mất mát và hành trình hồi hương của người Balkar. Kiến trúc và cách trưng bày mang tính biểu tượng cao, gợi lên sự tưởng nhớ và hoà giải. Đây là điểm đến có ý nghĩa lịch sử – nhân văn sâu sắc, giúp du khách hiểu thêm về ký ức tập thể và sức bền của các dân tộc Bắc Kavkaz. Nơi đây cũng thường là địa điểm tổ chức các sự kiện tưởng niệm hằng năm của cộng đồng.",
    [
        "Tưởng nhớ cuộc trục xuất toàn bộ dân tộc Balkar năm 1944.",
        "Kết hợp không gian tưởng niệm ngoài trời và bảo tàng ký ức xúc động.",
        "Điểm đến mang ý nghĩa lịch sử – nhân văn sâu sắc về ký ức và hoà giải.",
    ],
    {
        "hours_vi": "Bảo tàng thường mở 10:00–18:00, nghỉ thứ Hai (khu tưởng niệm ngoài trời có thể ghé mọi lúc).",
        "ticket_vi": "Vé vào bảo tàng mức bình dân; khu tưởng niệm ngoài trời miễn phí.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Đây là nơi tưởng niệm, hãy giữ thái độ trang nghiêm; nên tìm hiểu trước bối cảnh lịch sử để cảm nhận đầy đủ.",
    },
    [
        {"title": "2ГИС — Мемориал жертв политических репрессий 1944–1957 (ул. Балкарова 4а)", "url": "https://2gis.ru/nalchik/firm/70000001029392087"},
    ],
    ["memorial", "history", "deportation", "balkar", "nalchik", "museum"],
    maps_text("Мемориал жертв политических репрессий", "Нальчик", "Memorial to Victims of Political Repressions", "Nalchik", 43.453368, 43.581099),
))

# 22) Ресторан-символ «Сосруко» ------------------------------------------------------
RECORDS.append(rec(
    "sosruko-viewpoint",
    "Nhà hàng - biểu tượng 'Sosruko' và đài ngắm cảnh",
    "Ресторан «Сосруко» и смотровая площадка",
    "Sosruko Restaurant and Viewpoint",
    ["monument", "other"],
    43.460562, 43.599785,
    "Núi Malaya Kizilovka (ул. Профсоюзная 2а/1), thành phố Nalchik, Cộng hoà Kabardino-Balkaria, Nga.",
    "'Sosruko' là công trình biểu tượng của Nalchik trên đỉnh Malaya Kizilovka, tạo hình đầu và bàn tay cầm đuốc của người anh hùng huyền thoại Sosruko, kèm đài ngắm toàn cảnh thành phố.",
    "Xây dựng từ thập niên 1970 trên đỉnh núi Malaya Kizilovka nhìn xuống Nalchik, 'Sosruko' là một trong những công trình dễ nhận biết nhất của thành phố. Toà nhà (vốn là một nhà hàng) được tạo hình cách điệu thành đầu và bàn tay giơ cao ngọn đuốc của Sosruko – người anh hùng khổng lồ trong sử thi Nart, theo truyền thuyết đã mang lửa về cho loài người và bị các vị thần trừng phạt, thân thể lún vào núi chỉ còn lại cái đầu và cánh tay cầm lửa. Chính hình tượng độc đáo ấy khiến công trình trở thành biểu tượng và điểm 'phải chụp ảnh' của Nalchik. Trước công trình là đài quan sát toàn cảnh, nơi du khách phóng tầm mắt xuống thành phố, các hồ nước và dãy núi bao quanh, đặc biệt đẹp lúc hoàng hôn và khi lên đèn. Có thể lên đỉnh núi bằng ô tô hoặc bằng tuyến cáp treo ghế ngồi xuất phát từ khu công viên giải trí dưới chân núi.",
    [
        "Công trình biểu tượng tạo hình đầu và bàn tay cầm đuốc của anh hùng Nart Sosruko.",
        "Đài ngắm toàn cảnh Nalchik, hồ nước và núi, tuyệt đẹp lúc hoàng hôn.",
        "Lên đỉnh bằng ô tô hoặc cáp treo ghế ngồi từ công viên dưới chân núi.",
    ],
    {
        "hours_vi": "Đài ngắm cảnh và nhà hàng mở cửa hằng ngày (nhà hàng thường tới khuya); cáp treo hoạt động ban ngày.",
        "ticket_vi": "Lên đài ngắm cảnh và cáp treo thu phí; ngắm cảnh quanh khu vực miễn phí.",
        "duration_vi": "Khoảng 30–60 phút (lâu hơn nếu dùng bữa tại nhà hàng).",
        "best_time_vi": "Quanh năm; đẹp nhất vào chiều muộn – hoàng hôn khi thành phố lên đèn.",
        "tips_vi": "Kết hợp đi cáp treo qua hồ và công viên Atazhukinsky; mang máy ảnh cho khung cảnh toàn cảnh.",
    },
    [
        {"title": "Totrip — Ресторан Сосруко, Нальчик", "url": "https://totrip.info/nalchik/dostoprimechatelnosti_nalchika/restoran_sosruko"},
        {"title": "Yandex Maps — Ресторан Сосруко", "url": "https://yandex.com/maps/org/sosruko/3669566291/"},
    ],
    ["landmark", "sosruko", "viewpoint", "cable-car", "nalchik", "nart-epic"],
    maps_org("https://yandex.com/maps/org/sosruko/3669566291/", "Sosruko Restaurant Viewpoint", "Nalchik"),
))

# 23) Площадь Абхазии ----------------------------------------------------------------
RECORDS.append(rec(
    "abkhazia-square",
    "Quảng trường Abkhazia",
    "Площадь Абхазии",
    "Abkhazia Square",
    ["square_street"],
    43.471389, 43.588056,
    "Пр. Ленина, trung tâm thành phố Nalchik, Cộng hoà Kabardino-Balkaria, Nga.",
    "Quảng trường Abkhazia nằm ngay trung tâm Nalchik trên đại lộ Lenin, là không gian công cộng thoáng đãng với đài tưởng niệm và những khoảng cây xanh, vòi phun quen thuộc của người dân thành phố.",
    "Toạ lạc ngay giữa trung tâm Nalchik trên trục đại lộ Lenin, Quảng trường Abkhazia là một trong những không gian công cộng gắn bó với đời sống thường ngày của thành phố. Ở trung tâm quảng trường có đài tưởng niệm những người tình nguyện đã bảo vệ nền độc lập của Abkhazia trong cuộc chiến Gruzia – Abkhazia năm 1992–1993, thể hiện mối liên hệ lịch sử giữa các dân tộc Kavkaz. Xung quanh là các bồn hoa, thảm cỏ, hàng cây và lối đi dạo, tạo nên một góc phố xanh mát để người dân nghỉ ngơi, gặp gỡ. Nằm gần nhiều điểm tham quan trung tâm như các bảo tàng, nhà hát và nhà thờ Hồi giáo lớn, quảng trường là điểm định hướng thuận tiện khi khám phá phố trung tâm Nalchik bằng cách đi bộ, đặc biệt dễ chịu vào buổi chiều tối.",
    [
        "Quảng trường trung tâm trên đại lộ Lenin, không gian xanh của Nalchik.",
        "Đài tưởng niệm tình nguyện viên trong cuộc chiến Abkhazia 1992–1993.",
        "Điểm định hướng thuận tiện gần bảo tàng, nhà hát và nhà thờ Hồi giáo lớn.",
    ],
    {
        "hours_vi": "Không gian đô thị mở, dạo bộ tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–30 phút dạo và ngắm.",
        "best_time_vi": "Quanh năm; buổi chiều tối mát mẻ và nhộn nhịp nhất.",
        "tips_vi": "Dùng làm điểm xuất phát cho tuyến đi bộ tham quan trung tâm Nalchik.",
    },
    [
        {"title": "Delfin-tour — Площадь Согласия / центр Нальчика", "url": "https://www.delfin-tour.ru/poi/landmark/ploschad_soglasiya_v_nalchike"},
        {"title": "Wikipedia (RU) — Нальчик", "url": "https://ru.wikipedia.org/wiki/Нальчик"},
    ],
    ["square", "city-center", "monument", "nalchik", "walking"],
    maps_text("Площадь Абхазии", "Нальчик", "Abkhazia Square", "Nalchik", 43.471389, 43.588056),
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
