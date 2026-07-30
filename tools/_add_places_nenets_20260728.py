# -*- coding: utf-8 -*-
"""_add_places_nenets_20260728.py — VÙNG: Khu tự trị Nenets (Nenets Autonomous Okrug).

Bối cảnh: nenets.json hiện có 5 địa điểm (naryan-mar, pustozersk,
nenets-local-lore-museum, epiphany-cathedral-naryan-mar, nenets-tundra-reindeer-camps).
Đây là vùng BẮC CỰC RẤT THƯA địa điểm (dân số ~42.000, ít dân nhất nước Nga). Đợt này
bổ sung 25 địa điểm THẬT (đưa tổng lên 30), đa dạng loại hình:
  church 1 · monument 2 · museum 1 · park_garden 3 · other 18
Gồm: các đối tượng ở Nаряn-Mar (nhà nguyện Thánh Nikolai của tín đồ Cũ phái Pomor,
tượng đài Lenin, tượng đài các tiểu đoàn vận tải tuần lộc, bảo tàng-khu bảo tồn Pustozersk),
thiên nhiên Bắc Cực (khu bảo tồn Nenetsky, đảo thánh Vaygach, đảo Kolguyev, suối nước nóng
Pym-Va-Shor, hẻm núi Bolshiye Vorota trên dãy Timan, hải đăng Khodovarikha, sông Pechora),
và các điểm dân cư/địa danh (Amderma, Indiga, Oma, Nes, Krasnoye, Iskateley, Telviska,
Oksino, Nelmin Nos, Bugrino, Karatayka, Ust-Kara, làng Varnek trên đảo Vaygach, mũi Kanin Nos).

TOẠ ĐỘ — xác minh chéo (Wikipedia EN/RU + infobox, sobory.ru, oopt.aari.ru, komandirovka.ru,
autotravel.ru, culture.ru, dic.academic mirror infobox ru.wiki, 2026-07):
  Nikolskaya (Pomorskaya molennaya) 67.640435,53.013318 (sobory object=12512; Pervomayskaya 27A);
  Памятник Ленину 67.6382,53.0067 (autotravel; пл. Ленина); Памятник оленно-транспортным
  батальонам 67.6401,53.0112 (ul. Pobedy, cạnh краевед. музей); Пустозерский музей (Дом
  Шевелёвых) 67.6413,53.0071 (ул. Тыко Вылки 4); Ненецкий заповедник 68.59306,53.75750
  (en.wiki, thành lập 1997, 313.400 ha); о. Вайгач 69.99694,59.57889 (en.wiki); о. Колгуев
  69.083,49.250 (en.wiki 69°05′N 49°15′E); Пым-Ва-Шор 67.18889,60.87306 (ru.wiki
  67°11′20″N 60°52′23″E); каньон Большие Ворота 67.3042,49.10 (ru.wiki bounds ~67°18′N
  49°06′E; ~40 km nam Indiga, sông Belaya); Ходовариха 68.95,53.75 (en.wiki 68°57′N 53°45′E);
  Печора (đoạn Nаряn-Mar) 67.6300,52.9800 (dòng sông chính chảy qua thủ phủ); Амдерма
  69.76306,61.66778 (biển Kara, bán đảo Yugorsky); Индига 67.6583,49.0164; Ома 66.6436,46.4923
  (komandirovka N66°38′37″ E46°29′32″); Несь 66.6004,44.6809 (komandirovka); Красное
  67.8356,53.5970; Искателей 67.6667,53.1333; Тельвиска 67.6360,52.8863 (OSM); Оксино
  67.5838,52.1777; Нельмин Нос 67.9815,52.9556; Бугрино 68.7829,49.3036 (о. Колгуев);
  Каратайка 68.7617,61.4099; Усть-Кара 69.2446,64.9206 (đông NAO, vịnh Kara); Варнек
  69.71528,60.06000 (en.wiki, o. Вайгач); мыс Канин Нос 68.6414,43.3847 (điểm cực tây NAO).
  Kiểm tra phạm vi Nenets AO (lat ~66–70; lon ~43–65; KHÔNG đảo lat/lon). Vài điểm ở rìa:
  Канин Нос (lon 43.38, cực tây), Усть-Кара (lon 64.92, cực đông) — đều là giá trị ĐÚNG.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_nenets_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "nenets"
REGION_NAME_VI = "Khu tự trị Nenets"
FD = "Vùng Tây Bắc"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=14",
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

# 1) Моленная (церковь) Николая Чудотворца — Нарьян-Мар ------------------------
RECORDS.append(rec(
    "st-nicholas-old-believer-church-naryan-mar",
    "Nhà nguyện gỗ Thánh Nikolai (tín đồ Cũ phái Pomor), Naryan-Mar",
    "Церковь (моленная) Николая Чудотворца",
    "Church of St. Nicholas (Pomorian Old Believers), Naryan-Mar",
    ["church"],
    67.640435, 53.013318,
    "Phố Pervomayskaya số 27A, Naryan-Mar, Khu tự trị Nenets, Nga.",
    "Ngôi nhà nguyện bằng gỗ của cộng đồng Tín đồ Cũ phái Pomor ở Naryan-Mar, thánh hiến cho Thánh Nikolai. Được dựng suốt sáu năm bằng tiền quyên góp của giáo dân và các nhà hảo tâm, công trình khánh thành ngày 18-19 tháng 12 năm 2008, đúng dịp lễ Thánh Nikolai và kỷ niệm 10 năm cộng đồng Pomor tại đây.",
    "Bên cạnh Nhà thờ chính tòa Hiển Linh của Chính thống giáo, Naryan-Mar còn có một ngôi nhà nguyện gỗ nhỏ nhắn nhưng đầy ý nghĩa của cộng đồng Tín đồ Cũ (Staroobryadtsy) phái Pomor - những người gìn giữ nghi lễ Chính thống giáo Nga trước cải cách thế kỷ 17, vốn gắn bó sâu sắc với vùng phương Bắc và với chính lịch sử bi tráng của Pustozersk (nơi tổng tư tế Avvakum bị thiêu). Ngôi nhà nguyện thánh hiến cho Thánh Nikolai - vị thánh bảo trợ của những người đi biển và dân phương Bắc. Công trình được thi công kiên nhẫn trong sáu năm bằng tiền quyên góp của giáo dân và các nhà hảo tâm, rồi khánh thành trọng thể vào ngày lễ Thánh Nikolai mùa đông (18-19 tháng 12 năm 2008), trùng với dịp kỷ niệm mười năm cộng đồng Tín đồ Cũ phái Pomor được thành lập ở Naryan-Mar. Với lối kiến trúc gỗ mộc mạc đặc trưng phương Bắc, ngôi nhà nguyện là minh chứng sống động cho sức sống bền bỉ của truyền thống Tín đồ Cũ giữa vùng lãnh nguyên Bắc Cực.",
    [
        "Nhà nguyện gỗ của cộng đồng Tín đồ Cũ phái Pomor - dòng chảy tín ngưỡng gắn với lịch sử Pustozersk.",
        "Thánh hiến cho Thánh Nikolai, khánh thành ngày lễ Thánh Nikolai mùa đông năm 2008.",
        "Kiến trúc gỗ mộc mạc đặc trưng phương Bắc, dựng suốt sáu năm bằng tiền quyên góp.",
    ],
    {
        "hours_vi": "Mở theo giờ cầu nguyện của cộng đồng; nên hỏi trước khi tới, tôn trọng không gian của Tín đồ Cũ.",
        "ticket_vi": "Vào tự do; khuyến khích đóng góp tuỳ tâm.",
        "duration_vi": "Khoảng 15-30 phút.",
        "best_time_vi": "Quanh năm; ý nghĩa nhất vào dịp lễ Thánh Nikolai (tháng 12).",
        "tips_vi": "Ăn mặc kín đáo, giữ yên lặng; cộng đồng Tín đồ Cũ có quy tắc riêng khác Chính thống giáo phổ thông.",
    },
    [
        {"title": "Соборы.ру — Нарьян-Мар, Моленная Николая Чудотворца", "url": "https://sobory.ru/article/?object=12512"},
    ],
    ["church", "old-believers", "wooden-architecture", "naryan-mar", "arctic"],
    maps_text("Церковь Николая Чудотворца", "Нарьян-Мар", "Church of St Nicholas", "Naryan-Mar", 67.640435, 53.013318),
))

# 2) Памятник В. И. Ленину — Нарьян-Мар ---------------------------------------
RECORDS.append(rec(
    "lenin-monument-naryan-mar",
    "Tượng đài V. I. Lenin, Naryan-Mar",
    "Памятник В. И. Ленину",
    "Lenin Monument, Naryan-Mar",
    ["monument"],
    67.6382, 53.0067,
    "Quảng trường Lenin (Ploshchad Lenina), Naryan-Mar, Khu tự trị Nenets, Nga.",
    "Tượng đài Lenin bằng đồng cao 3 m đứng giữa Quảng trường Lenin - quảng trường trung tâm của Naryan-Mar. Tác phẩm của nhà điêu khắc P. P. Yatsyno và kiến trúc sư G. I. Lutsky, được khánh thành ngày 19 tháng 4 năm 1970, là điểm nhấn của không gian công cộng chính thành phố.",
    "Nằm ở trái tim thủ phủ Bắc Cực, Quảng trường Lenin là nơi tụ họp, diễu hành và tổ chức các sự kiện lớn của Naryan-Mar. Chính giữa quảng trường là tượng đài lãnh tụ V. I. Lenin đúc bằng đồng, thể hiện toàn thân cao khoảng 3 mét, do nhà điêu khắc Pyotr Yatsyno và kiến trúc sư Georgy Lutsky thực hiện. Tượng được dựng và khánh thành ngày 19 tháng 4 năm 1970, đúng dịp kỷ niệm 100 năm ngày sinh Lenin - một mốc quan trọng của thời Xô Viết. Cùng với dãy công sở, nhà văn hoá bao quanh, quảng trường và tượng đài tạo nên bộ mặt hành chính - lịch sử của thành phố, nơi du khách thường ghé để cảm nhận không khí của một đô thị Xô Viết cũ giữa lãnh nguyên. Vào các ngày lễ, đặc biệt là Ngày Chiến thắng và Ngày hội Người chăn tuần lộc, quảng trường trở nên nhộn nhịp và rực rỡ sắc màu.",
    [
        "Tượng đồng Lenin cao 3 m, tác phẩm của điêu khắc gia P. P. Yatsyno, khánh thành 19/4/1970.",
        "Trung tâm Quảng trường Lenin - không gian công cộng chính của thủ phủ Bắc Cực.",
        "Nơi diễn ra diễu hành, lễ hội và các sự kiện lớn của Naryan-Mar.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15-20 phút.",
        "best_time_vi": "Mùa hè có mặt trời nửa đêm; dịp lễ lớn quảng trường đông vui nhất.",
        "tips_vi": "Là điểm định hướng trung tâm; dễ kết hợp đi bộ tới bảo tàng, nhà thờ và các tượng đài lân cận.",
    },
    [
        {"title": "Википедия (RU) — Памятник Ленину (Нарьян-Мар)", "url": "https://ru.wikipedia.org/wiki/Памятник_Ленину_(Нарьян-Мар)"},
        {"title": "Autotravel.ru — Памятник В. И. Ленину, Нарьян-Мар", "url": "https://autotravel.ru/otklik.php/33327"},
    ],
    ["monument", "lenin", "soviet", "square", "naryan-mar"],
    maps_text("Памятник Ленину", "Нарьян-Мар", "Lenin Monument", "Naryan-Mar", 67.6382, 53.0067),
))

# 3) Памятник оленно-транспортным батальонам — Нарьян-Мар ---------------------
RECORDS.append(rec(
    "reindeer-transport-battalions-monument-naryan-mar",
    "Tượng đài các Tiểu đoàn vận tải bằng tuần lộc, Naryan-Mar",
    "Памятник «Подвигу участников оленно-транспортных батальонов»",
    "Monument to the Reindeer-Transport Battalions, Naryan-Mar",
    ["monument"],
    67.6401, 53.0112,
    "Phố Pobedy (Chiến Thắng), cạnh Bảo tàng Địa phương học Nenets, Naryan-Mar, Khu tự trị Nenets, Nga.",
    "Tượng đài tôn vinh chiến công của các tiểu đoàn vận tải bằng tuần lộc trong Thế chiến II, khánh thành ngày 23 tháng 2 năm 2012. Tác phẩm của nhà điêu khắc Arkhangelsk Sergei Syukhin là bố cục một người Nenets, một con tuần lộc Bắc Cực và một con chó lãnh nguyên đứng trong vầng mặt trời.",
    "Một trong những trang sử độc đáo và cảm động nhất của vùng Nenets trong Chiến tranh Vệ quốc là sự đóng góp của những người chăn tuần lộc. Năm 1941, tại Cộng hoà Komi và Khu tự trị Nenets, người ta thành lập các tiểu đoàn vận tải đặc biệt gồm người chăn tuần lộc và ngư dân bản địa; họ cùng đàn tuần lộc và xe trượt hành quân tới Arkhangelsk rồi ra mặt trận phương Bắc, làm nhiệm vụ vận chuyển vũ khí, thương binh, khí tài trong điều kiện băng giá khắc nghiệt mà xe cơ giới bó tay. Để tưởng nhớ chiến công ấy, ngày 23 tháng 2 năm 2012 (Ngày Bảo vệ Tổ quốc), thành phố khánh thành tượng đài do nhà điêu khắc Sergei Syukhin ở Arkhangelsk sáng tác. Bố cục thể hiện một người Nenets, một con tuần lộc Bắc Cực và một con chó lãnh nguyên (laika) cùng đứng trong vòng tròn tượng trưng cho vầng mặt trời phương Bắc - hình ảnh cô đọng lòng dũng cảm và mối gắn bó giữa con người, con vật và thiên nhiên nơi đây. Tượng đài nằm ngay cạnh Bảo tàng Địa phương học, dễ dàng ghép vào lộ trình tham quan trung tâm.",
    [
        "Tôn vinh các tiểu đoàn vận tải bằng tuần lộc của người Nenets trong Thế chiến II.",
        "Bố cục người Nenets - tuần lộc - chó lãnh nguyên trong vầng mặt trời, của điêu khắc gia Sergei Syukhin.",
        "Khánh thành 23/2/2012, ngay cạnh Bảo tàng Địa phương học Nenets.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15-20 phút.",
        "best_time_vi": "Quanh năm; kết hợp đẹp với chuyến thăm bảo tàng bên cạnh.",
        "tips_vi": "Nên vào Bảo tàng Địa phương học ngay cạnh để hiểu sâu hơn về câu chuyện các tiểu đoàn tuần lộc.",
    },
    [
        {"title": "Википедия (RU) — Памятник «Подвигу участников оленно-транспортных батальонов»", "url": "https://ru.wikipedia.org/wiki/Памятник_«Подвигу_участников_оленно-транспортных_батальонов»"},
        {"title": "2ГИС — Памятник оленно-транспортным батальонам, Нарьян-Мар", "url": "https://2gis.ru/naryan-mar/geo/70030076166364182"},
    ],
    ["monument", "wwii", "reindeer", "nenets", "naryan-mar"],
    maps_text("Памятник оленно-транспортным батальонам", "Нарьян-Мар", "Reindeer-Transport Battalions Monument", "Naryan-Mar", 67.6401, 53.0112),
))

# 4) Историко-культурный музей-заповедник «Пустозерск» (Дом Шевелёвых) --------
RECORDS.append(rec(
    "pustozersk-museum-naryan-mar",
    "Bảo tàng - Khu bảo tồn Pustozersk (trụ sở Naryan-Mar, Nhà Shevelyov)",
    "Историко-культурный и ландшафтный музей-заповедник «Пустозерск»",
    "Pustozersk Historical-Cultural Museum-Reserve",
    ["museum"],
    67.6413, 53.0071,
    "Phố Tyko Vylki số 4 (Nhà Shevelyov), Naryan-Mar, Khu tự trị Nenets, Nga.",
    "Bảo tàng - khu bảo tồn chuyên nghiên cứu, gìn giữ và quảng bá di sản Pustozersk - thành phố Nga đầu tiên ở Bắc Cực. Trụ sở đặt trong 'Nhà Shevelyov' cổ ngay trung tâm Naryan-Mar, mở cửa từ ngày 5 tháng 11 năm 1991, là nơi trưng bày trước khi du khách ra thăm di chỉ Pustozersk ngoài đồng.",
    "Nếu di chỉ Pustozersk cách thành phố vài chục cây số chỉ còn là đồng cỏ lộng gió với những cây thánh giá, thì tại trung tâm Naryan-Mar, Bảo tàng - khu bảo tồn 'Pustozersk' chính là nơi lưu giữ và kể lại câu chuyện của đô thị Bắc Cực đầu tiên ấy. Được thành lập ngày 5 tháng 11 năm 1991 theo quyết định của chính quyền okrug, bảo tàng đặt trụ sở trong 'Nhà Shevelyov' (Dom Shevelyovykh) - một ngôi nhà cổ trên phố Tyko Vylki. Mục tiêu của bảo tàng là nghiên cứu, bảo tồn và phổ biến di sản lịch sử - văn hoá của Pustozersk, thành phố do người Nga lập năm 1499, từng là trung tâm hành chính, thương mại của vùng Pechora và Yugra, đồng thời gắn với số phận bi tráng của tổng tư tế Avvakum. Tại đây, du khách được xem hiện vật khảo cổ, tư liệu, mô hình và câu chuyện về đời sống, tín ngưỡng của cư dân phương Bắc, để rồi hiểu sâu hơn khi đặt chân tới chính di chỉ ngoài lãnh nguyên. Đây là điểm khởi đầu lý tưởng cho hành trình khám phá lịch sử Pustozersk.",
    [
        "Bảo tàng - khu bảo tồn dành riêng cho Pustozersk, thành phố Nga đầu tiên ở Bắc Cực (lập năm 1499).",
        "Trụ sở trong 'Nhà Shevelyov' cổ, phố Tyko Vylki, trung tâm Naryan-Mar; mở cửa từ 1991.",
        "Điểm trưng bày và tìm hiểu trước khi ra thăm di chỉ Pustozersk ngoài đồng.",
    ],
    {
        "hours_vi": "Thường mở các ngày trong tuần theo giờ hành chính; nên xác nhận lịch và đặt tour ra di chỉ trước.",
        "ticket_vi": "Có thu phí vào cửa mức bình dân; tour ra di chỉ Pustozersk tính phí riêng.",
        "duration_vi": "Khoảng 45-60 phút tại trụ sở; cả ngày nếu kết hợp ra di chỉ.",
        "best_time_vi": "Quanh năm; mùa hè đi thuyền, mùa đông đi xe trượt tuyết ra di chỉ.",
        "tips_vi": "Liên hệ bảo tàng để tổ chức chuyến ra di chỉ Pustozersk - nơi không có biển chỉ dẫn và dịch vụ.",
    },
    [
        {"title": "Культура.РФ — Музей-заповедник «Пустозерск»", "url": "https://www.culture.ru/institutes/10229/muzei-zapovednik-pustozersk"},
        {"title": "Википедия (RU) — Музей-заповедник «Пустозерск»", "url": "https://ru.wikipedia.org/wiki/Музей-заповедник_«Пустозерск»"},
    ],
    ["museum", "pustozersk", "history", "arctic", "naryan-mar"],
    maps_text("Музей-заповедник Пустозерск", "Нарьян-Мар", "Pustozersk Museum-Reserve", "Naryan-Mar", 67.6413, 53.0071),
))

# 5) Ненецкий заповедник ------------------------------------------------------
RECORDS.append(rec(
    "nenetsky-nature-reserve",
    "Khu bảo tồn thiên nhiên Nenetsky (Nenetsky Zapovednik)",
    "Ненецкий государственный природный заповедник",
    "Nenetsky Nature Reserve",
    ["park_garden"],
    68.59306, 53.75750,
    "Vùng châu thổ sông Pechora và bờ biển Barents (biển Pechora), phía đông bắc Naryan-Mar, Khu tự trị Nenets, Nga.",
    "Khu bảo tồn thiên nhiên nghiêm ngặt (zapovednik) ở đông bắc phần châu Âu nước Nga, thành lập năm 1997, rộng khoảng 313.400 ha. Bao trùm vùng châu thổ sông Pechora, các đảo và bờ biển Barents, đây là thiên đường của chim di cư, hải mã Đại Tây Dương và hệ sinh thái lãnh nguyên - đầm lầy Bắc Cực.",
    "Ở nơi sông Pechora hùng vĩ đổ ra biển Barents, thiên nhiên Bắc Cực bày ra một trong những vùng đất ngập nước quan trọng bậc nhất của nước Nga. Khu bảo tồn thiên nhiên Nenetsky được thành lập năm 1997 với diện tích khoảng 313.400 ha, gồm phần châu thổ sông Pechora, nhiều đảo nhỏ và dải bờ biển. Là một zapovednik - cấp bảo vệ nghiêm ngặt nhất trong hệ thống khu bảo tồn Nga - nơi đây gần như không có hoạt động kinh tế, dành trọn cho việc bảo tồn và nghiên cứu. Vùng đầm lầy, hồ và bãi triều là điểm dừng chân, làm tổ của hàng loạt loài chim di cư: các loài ngỗng (ngỗng đậu, ngỗng má trắng), thiên nga lãnh nguyên, vịt biển, chim lội nước… khiến khu bảo tồn được công nhận là vùng chim quan trọng quốc tế và đất ngập nước Ramsar. Vùng biển lân cận là nơi sinh sống của hải mã Đại Tây Dương, hải cẩu và đôi khi cả gấu Bắc Cực. Với nhà nghiên cứu và du khách sinh thái, đây là cửa sổ quý giá nhìn vào sự sống mong manh mà kỳ diệu của lãnh nguyên ven biển Bắc Cực.",
    [
        "Zapovendik ở châu thổ Pechora - biển Barents, thành lập 1997, rộng ~313.400 ha.",
        "Vùng chim di cư quốc tế: ngỗng, thiên nga lãnh nguyên, vịt biển, chim lội nước.",
        "Nơi sinh sống của hải mã Đại Tây Dương, hải cẩu; đất ngập nước tầm cỡ Ramsar.",
    ],
    {
        "hours_vi": "Vùng bảo vệ nghiêm ngặt; chỉ vào theo giấy phép và tour có hướng dẫn của ban quản lý.",
        "ticket_vi": "Cần xin phép trước; chi phí chủ yếu là thuê phương tiện (thuyền/trực thăng) và hướng dẫn.",
        "duration_vi": "Thường trọn ngày hoặc nhiều ngày do khoảng cách và tính hoang vắng.",
        "best_time_vi": "Mùa hè (tháng 7-8) khi chim làm tổ và có thể đi thuyền; ánh sáng ngày cực dài.",
        "tips_vi": "Liên hệ ban quản lý khu bảo tồn tại Naryan-Mar; mang trang phục chống gió, chống muỗi lãnh nguyên.",
    },
    [
        {"title": "Wikipedia (EN) — Nenets Nature Reserve", "url": "https://en.wikipedia.org/wiki/Nenets_Nature_Reserve"},
        {"title": "Wikidata — Nenets Nature Reserve (Q4317115)", "url": "https://www.wikidata.org/wiki/Q4317115"},
    ],
    ["nature-reserve", "birds", "wetland", "pechora-delta", "arctic"],
    maps_text("Ненецкий заповедник", "Ненецкий автономный округ", "Nenetsky Nature Reserve", "Nenets Autonomous Okrug", 68.59306, 53.75750),
))

# 6) Остров Вайгач ------------------------------------------------------------
RECORDS.append(rec(
    "vaygach-island",
    "Đảo Vaygach (thánh địa của người Nenets)",
    "Остров Вайгач",
    "Vaygach Island",
    ["other"],
    69.99694, 59.57889,
    "Giữa biển Pechora và biển Kara, ngăn cách với bán đảo Yugorsky bởi eo Yugorsky Shar, Khu tự trị Nenets, Nga.",
    "Hòn đảo lãnh nguyên rộng khoảng 3.383 km² nằm giữa biển Pechora và biển Kara, từ xa xưa là thánh địa thiêng liêng bậc nhất của người Nenets. Trên đảo từng có hai vị thần tượng gỗ - Vesako ở mũi nam và Hadako ở phía bắc - cùng vô số bàn thờ tế bằng gỗ trôi, gạc tuần lộc và sọ thú. Người ngoài gọi Vaygach là 'hòn đảo của thần chết'.",
    "Nằm ở nơi tận cùng phía bắc của Khu tự trị Nenets, giữa biển Pechora và biển Kara, đảo Vaygach (rộng khoảng 3.383 km², dài chừng 100 km) là một trong những nơi thiêng liêng nhất trong tín ngưỡng của người Nenets. Cái tên Vaygach, theo một cách giải nghĩa, mang hàm ý 'vùng đất của cái chết' - phản ánh sự huyền bí và nỗi kính sợ mà cư dân bản địa dành cho đảo. Cho tới thế kỷ 19, đây là trung tâm thờ cúng: trên đảo có hai vị thần tượng lớn - Vesako ('ông già') ở mũi nam và Hadako ('bà già') ở phía bắc - cùng những thần tượng gỗ nhiều đầu được bôi máu tuần lộc hiến tế, và các bàn thờ chất đầy gỗ trôi, gạc tuần lộc, sọ gấu và hươu. Dù người Nenets đã cải sang Chính thống giáo, họ vẫn giữ lòng kính sợ với những nơi thờ cổ này. Ngày nay Vaygach cũng là vùng thiên nhiên quý: một khu bảo tồn được phê duyệt năm 2007, đảo là nơi cư trú của gấu Bắc Cực, chim biển, và có ngôi làng duy nhất Varnek ở bờ nam. Vaygach thu hút những chuyến thám hiểm Bắc Cực tìm về cội nguồn tâm linh và thiên nhiên nguyên sơ.",
    [
        "Thánh địa cổ của người Nenets với hai thần tượng Vesako (nam) và Hadako (bắc).",
        "Được gọi là 'hòn đảo của thần chết'; các bàn thờ tế bằng gỗ trôi, gạc và sọ thú.",
        "Đảo lãnh nguyên ~3.383 km² giữa biển Pechora và biển Kara; khu bảo tồn (2007), có gấu Bắc Cực.",
    ],
    {
        "hours_vi": "Đảo hoang vắng vùng biên giới; tới nơi phải theo tour thám hiểm/tàu và cần giấy phép vùng biên.",
        "ticket_vi": "Không có vé; chi phí là tour thám hiểm Bắc Cực bằng tàu/trực thăng (rất cao).",
        "duration_vi": "Thường nằm trong hành trình nhiều ngày trên biển Bắc Cực.",
        "best_time_vi": "Mùa hè ngắn ngủi (tháng 7-8) khi biển bớt băng.",
        "tips_vi": "Cần giấy phép vùng biên giới; tôn trọng các di tích thờ cúng thiêng liêng, không xê dịch hiện vật.",
    },
    [
        {"title": "Wikipedia (EN) — Vaygach Island", "url": "https://en.wikipedia.org/wiki/Vaygach_Island"},
        {"title": "Wikidata — Vaygach Island (Q207677)", "url": "https://www.wikidata.org/wiki/Q207677"},
    ],
    ["sacred-site", "nenets", "island", "shamanism", "arctic"],
    maps_text("Остров Вайгач", "Ненецкий автономный округ", "Vaygach Island", "Nenets Autonomous Okrug", 69.99694, 59.57889),
))

# 7) Остров Колгуев -----------------------------------------------------------
RECORDS.append(rec(
    "kolguyev-island",
    "Đảo Kolguyev",
    "Остров Колгуев",
    "Kolguyev Island",
    ["other"],
    69.083, 49.250,
    "Đông nam biển Barents (tây biển Pechora), phía đông bắc bán đảo Kanin, Khu tự trị Nenets, Nga.",
    "Hòn đảo tròn trịa rộng khoảng 3.497 km² ở đông nam biển Barents, nổi tiếng là thiên đường chim và vùng chăn tuần lộc lâu đời của người Nenets. Điểm cao nhất chỉ 166 m, đảo phủ lãnh nguyên, đầm lầy và hồ. Làng duy nhất là Bugrino.",
    "Trồi lên giữa biển Barents lạnh giá, phía đông bắc bán đảo Kanin, đảo Kolguyev có hình dáng gần như tròn với diện tích khoảng 3.497 km² - lớn hơn cả đảo Vaygach. Đây là vùng đất thấp, điểm cao nhất (Gora Paarkov-Sarlopy) chỉ khoảng 166 m, phủ đầy lãnh nguyên, đầm lầy và vô số hồ nhỏ. Người Nenets đã sinh sống trên đảo qua nhiều thế kỷ, dùng nơi đây làm căn cứ săn hải cẩu, chăn tuần lộc và đánh cá. Nhờ hệ đầm lầy - hồ trù phú, Kolguyev là một trong những khu vực làm tổ quan trọng của chim nước Bắc Cực: các loài ngỗng, thiên nga, vịt biển tụ về đây mỗi mùa hè, biến hòn đảo thành điểm đến mơ ước của giới quan sát chim. Cư dân tập trung ở làng Bugrino nhỏ bé bên bờ eo Pomorsky - điểm dân cư duy nhất của đảo. Cách biệt và nguyên sơ, Kolguyev là hình ảnh tiêu biểu của thiên nhiên và lối sống bản địa nơi rìa Bắc Cực nước Nga.",
    [
        "Đảo lãnh nguyên ~3.497 km² ở biển Barents; điểm cao nhất chỉ 166 m.",
        "Vùng chăn tuần lộc, săn hải cẩu lâu đời của người Nenets; thiên đường chim nước.",
        "Làng Bugrino bên eo Pomorsky là điểm dân cư duy nhất trên đảo.",
    ],
    {
        "hours_vi": "Đảo xa xôi; tới nơi chủ yếu bằng trực thăng theo lịch hoặc tàu, cần giấy phép vùng biên.",
        "ticket_vi": "Không có vé; chi phí là vé trực thăng/tàu và tour (cao).",
        "duration_vi": "Thường nằm trong hành trình nhiều ngày.",
        "best_time_vi": "Mùa hè (tháng 6-8) khi chim làm tổ và thời tiết dịu hơn.",
        "tips_vi": "Chuẩn bị cho điều kiện hoang sơ, không dịch vụ; hỏi trước lịch bay tới Bugrino.",
    },
    [
        {"title": "Wikipedia (EN) — Kolguyev Island", "url": "https://en.wikipedia.org/wiki/Kolguyev_Island"},
        {"title": "Wikidata — Kolguyev Island (Q216161)", "url": "https://www.wikidata.org/wiki/Q216161"},
    ],
    ["island", "birds", "nenets", "reindeer", "arctic"],
    maps_text("Остров Колгуев", "Ненецкий автономный округ", "Kolguyev Island", "Nenets Autonomous Okrug", 69.083, 49.250),
))

# 8) Пым-Ва-Шор (термальные источники) ----------------------------------------
RECORDS.append(rec(
    "pym-va-shor-hot-springs",
    "Suối nước nóng Pym-Va-Shor (nóng nhất Bắc Cực châu Âu)",
    "Пым-Ва-Шор",
    "Pym-Va-Shor Thermal Springs",
    ["park_garden"],
    67.18889, 60.87306,
    "Lưu vực sông Adzva, vùng lãnh nguyên Bolshezemelskaya, gần ranh giới với Cộng hoà Komi, đông nam Khu tự trị Nenets, Nga.",
    "Cụm suối khoáng nóng độc đáo trong vùng lãnh nguyên Bolshezemelskaya - nơi được xem là điểm có suối nước nóng ở cực bắc của lục địa châu Âu, ngay phía trên vòng Bắc Cực. Khu urochishche gồm tám nguồn khoáng - nhiệt (20-28,5°C) chứa radon, iốt, cùng các di chỉ khảo cổ, được bảo vệ từ năm 2000.",
    "Giữa vùng lãnh nguyên Bolshezemelskaya bao la và băng giá, thiên nhiên tạo ra một điều kỳ diệu: Pym-Va-Shor - tên trong tiếng Komi nghĩa là 'con suối nước nóng'. Đây được coi là nơi cực bắc của lục địa châu Âu vẫn có các suối nước nóng hoạt động, nằm ngay phía trên vòng Bắc Cực, trong lưu vực sông Adzva sát ranh giới Khu tự trị Nenets và Cộng hoà Komi. Khu vực bảo vệ (thành lập năm 2000, rộng khoảng 2.425 ha) gồm một quần thể tám nguồn khoáng - nhiệt với nhiệt độ từ 20,3 đến 28,5°C, cùng năm suối karst lạnh (1,2-6°C). Nước chứa hàm lượng cao radon, iốt, radi, brom… và ngay giữa mùa đông băng giá, các nguồn nóng vẫn không đóng băng, khiến một số loài cây tiếp tục sinh trưởng. Vùng này còn có giá trị khảo cổ lớn với các di chỉ, trong đó có di tích thời đồ đá cũ được xem là ở cực bắc châu Âu. Với các nhà thám hiểm và du khách ưa mạo hiểm, được ngâm mình trong dòng nước nóng bốc hơi giữa lãnh nguyên trắng xoá là một trải nghiệm khó quên.",
    [
        "Điểm suối nước nóng ở cực bắc lục địa châu Âu, ngay trên vòng Bắc Cực.",
        "Tám nguồn khoáng - nhiệt (20-28,5°C) chứa radon, iốt; không đóng băng giữa mùa đông.",
        "Có di chỉ khảo cổ, gồm di tích đồ đá cũ được xem là cực bắc châu Âu; bảo vệ từ 2000.",
    ],
    {
        "hours_vi": "Địa điểm hoang vắng ngoài lãnh nguyên; tới nơi chỉ theo tour có hướng dẫn, không có dịch vụ tại chỗ.",
        "ticket_vi": "Không có cổng thu phí; chi phí là thuê phương tiện và hướng dẫn viên.",
        "duration_vi": "Thường là chuyến nhiều ngày do khoảng cách xa xôi.",
        "best_time_vi": "Cuối đông - đầu xuân đi xe trượt tuyết/vездeход; mùa hè khó tiếp cận qua đầm lầy.",
        "tips_vi": "Đi cùng hướng dẫn viên địa phương; mang đồ ấm, đồ bơi để ngâm nước nóng, và tôn trọng di chỉ khảo cổ.",
    },
    [
        {"title": "Википедия (RU) — Пым-Ва-Шор", "url": "https://ru.wikipedia.org/wiki/Пым-Ва-Шор"},
        {"title": "ООПТ России — Пым-Ва-Шор", "url": "http://oopt.aari.ru/oopt/Пым-Ва-Шор"},
    ],
    ["hot-springs", "natural-monument", "tundra", "archaeology", "arctic"],
    maps_text("Пым-Ва-Шор", "Ненецкий автономный округ", "Pym-Va-Shor thermal springs", "Nenets Autonomous Okrug", 67.18889, 60.87306),
))

# 9) Каньон «Большие Ворота» (река Белая, Тиман) ------------------------------
RECORDS.append(rec(
    "bolshiye-vorota-canyon",
    "Hẻm núi Bolshiye Vorota ('Cổng Lớn') trên sông Belaya",
    "Каньон «Большие Ворота»",
    "Bolshiye Vorota Canyon",
    ["park_garden"],
    67.3042, 49.1000,
    "Trung lưu sông Belaya (nhánh trái sông Indiga), cách làng Indiga khoảng 40 km về phía nam, dãy Timan, Khu tự trị Nenets, Nga.",
    "Hẻm núi ngoạn mục ở trung lưu sông Belaya trên dãy Timan, cách làng Indiga khoảng 40 km. Sông cắt qua những vách đá bazan cao 80-90 m thuộc kỷ Devon thượng, trong đá lấp lánh nhiều mã não và khoáng vật. Là di tích thiên nhiên được công nhận từ năm 1987.",
    "Ở phía tây Khu tự trị Nenets, nơi dãy Timan cổ xưa trồi lên giữa lãnh nguyên, sông Belaya (một nhánh của sông Indiga) đã bào mòn qua hàng triệu năm để tạo nên hẻm núi 'Bolshiye Vorota' - nghĩa là 'Cổng Lớn'. Cách làng Indiga khoảng 40 km về phía nam, ở khúc trung lưu, dòng sông uốn một vòng lớn rồi len qua những vách đá bazan dựng đứng cao 80-90 mét, hình thành từ dung nham kỷ Devon thượng. Cảnh quan hùng vĩ với các bờ đá đen sẫm, hẻm hẹp và dòng nước trong là điều hiếm thấy ở vùng lãnh nguyên vốn bằng phẳng. Trong đá bazan và trầm tích lòng sông, người ta tìm thấy nhiều mã não (agate) cùng các khoáng vật đẹp, khiến nơi đây hấp dẫn cả du khách lẫn người mê địa chất. Hẻm núi được công nhận là di tích thiên nhiên cấp vùng từ năm 1987, rộng khoảng 212 ha, và là một trong những điểm nhấn cảnh quan nổi bật nhất của phần Timan thuộc Nenets.",
    [
        "Hẻm núi bazan hùng vĩ, vách cao 80-90 m, kỷ Devon thượng, trên sông Belaya (dãy Timan).",
        "Trong đá và lòng sông có nhiều mã não và khoáng vật đẹp.",
        "Di tích thiên nhiên cấp vùng từ 1987, cách làng Indiga ~40 km về phía nam.",
    ],
    {
        "hours_vi": "Ngoài trời, hoang vắng; tới nơi theo tour sông nước/vездeход, không có dịch vụ tại chỗ.",
        "ticket_vi": "Không có cổng thu phí; chi phí là thuê thuyền/phương tiện và hướng dẫn.",
        "duration_vi": "Thường là chuyến nhiều ngày kết hợp sông Belaya - Indiga.",
        "best_time_vi": "Mùa hè (tháng 7-8) khi có thể đi thuyền và nước sông thuận lợi.",
        "tips_vi": "Đi cùng hướng dẫn viên; người mê khoáng vật có thể tìm mã não, nhưng nên bảo vệ cảnh quan di tích.",
    },
    [
        {"title": "Википедия (RU) — Каньон «Большие Ворота»", "url": "https://ru.wikipedia.org/wiki/Каньон_«Большие_Ворота»"},
        {"title": "Zapoved.net — Каньон «Большие Ворота»", "url": "http://www.zapoved.net/index.php/katalog/regiony-rossii/severo-zapadnyj-fo/nenetskij-avtonomnyj-okrug"},
    ],
    ["canyon", "basalt", "timan", "natural-monument", "arctic"],
    maps_text("Каньон Большие Ворота", "Ненецкий автономный округ", "Bolshiye Vorota Canyon", "Nenets Autonomous Okrug", 67.3042, 49.1000),
))

# 10) Ходовариха (маяк и метеостанция) ----------------------------------------
RECORDS.append(rec(
    "khodovarikha-lighthouse",
    "Hải đăng và trạm khí tượng Khodovarikha",
    "Ходовариха (маяк и метеостанция)",
    "Khodovarikha Lighthouse and Weather Station",
    ["other"],
    68.9500, 53.7500,
    "Dải cát nhô ra biển Pechora, gần bán đảo Russky Zavorot, Khu tự trị Nenets, Nga.",
    "Một mũi đất - dải cát cô đơn nhô ra biển Pechora, nơi có ngọn hải đăng gỗ từng là đèn hiệu quan trọng cho các đoàn tàu vận tải Bắc Cực thời Thế chiến II. Trạm khí tượng mở từ năm 1933 vẫn hoạt động, nổi tiếng nhờ phim tài liệu 'Arctic Limbo' (2015) về cuộc sống cô lập cùng cực nơi đây.",
    "Khodovarikha là một trong những nơi cô độc và giàu chất huyền thoại nhất của vùng biển Bắc Cực Nga - một dải cát dài nhô ra biển Pechora, gần bán đảo Russky Zavorot. Trạm khí tượng ở đây mở cửa ngày 17 tháng 11 năm 1933 và đến nay vẫn hoạt động, với chỉ vài người quanh năm bám trụ giữa bốn bề băng tuyết và bão biển. Ngọn hải đăng gỗ dựng từ tháng 7 năm 1934 từng là đèn hiệu sống còn cho tuyến đường hộ tống tàu vận tải đi qua eo Yugorsky trong Thế chiến II; năm 1942, trong chiến dịch 'Wunderland' của hải quân Đức, nơi đây từng bị nã pháo. Hải đăng ngừng hoạt động năm 1996, và đáng tiếc bị cháy rụi năm 2019 trong một vụ tai nạn khi tình nguyện viên tới trùng tu. Câu chuyện về sự cô lập tột cùng của những người canh trạm khí tượng nơi đây đã được khắc hoạ trong bộ phim tài liệu 'Arctic Limbo' (RT, 2015), biến Khodovarikha thành biểu tượng của đời sống con người ở tận cùng thế giới. Đây là điểm đến của những ai muốn chạm tới sự khắc nghiệt và vẻ đẹp trầm mặc của Bắc Cực.",
    [
        "Hải đăng gỗ (1934) - đèn hiệu cho đoàn tàu Bắc Cực thời Thế chiến II; từng bị nã pháo năm 1942.",
        "Trạm khí tượng mở từ 1933 vẫn hoạt động giữa sự cô lập cùng cực.",
        "Nổi tiếng qua phim tài liệu 'Arctic Limbo' (2015); hải đăng cháy rụi năm 2019.",
    ],
    {
        "hours_vi": "Địa điểm hẻo lánh vùng biên; không có tham quan thông thường, chỉ tiếp cận qua chuyến đi đặc biệt.",
        "ticket_vi": "Không áp dụng; chi phí là phương tiện chuyên dụng (trực thăng/tàu) và giấy phép.",
        "duration_vi": "Thường nằm trong hành trình thám hiểm dài ngày.",
        "best_time_vi": "Mùa hè ngắn (tháng 7-8) khi biển bớt băng.",
        "tips_vi": "Cần giấy phép vùng biên và chuẩn bị kỹ; tôn trọng công việc của nhân viên trạm khí tượng.",
    },
    [
        {"title": "Wikipedia (EN) — Khodovarikha", "url": "https://en.wikipedia.org/wiki/Khodovarikha"},
        {"title": "The Guardian — Slava of the Arctic: the world's most extreme weatherman", "url": "https://www.theguardian.com/artanddesign/2015/oct/26/slava-of-the-arctic-worlds-most-extreme-weatherman-evgenia-arbugaeva-photographs/"},
    ],
    ["lighthouse", "weather-station", "wwii", "remote", "arctic"],
    maps_text("Ходовариха", "Ненецкий автономный округ", "Khodovarikha", "Nenets Autonomous Okrug", 68.9500, 53.7500),
))

# 11) Река Печора (участок у Нарьян-Мара) --------------------------------------
RECORDS.append(rec(
    "pechora-river-naryan-mar",
    "Sông Pechora (đoạn qua Naryan-Mar)",
    "Река Печора",
    "Pechora River",
    ["other"],
    67.6300, 52.9800,
    "Hạ lưu sông Pechora tại thủ phủ Naryan-Mar, trước khi đổ ra biển Pechora (Barents), Khu tự trị Nenets, Nga.",
    "Con sông chính và huyết mạch của Khu tự trị Nenets, chảy từ dãy Ural bắc qua Komi rồi đổ ra biển Pechora. Đoạn hạ lưu rộng lớn ôm lấy thủ phủ Naryan-Mar - nơi đặt cảng sông quan trọng, tuyến vận tải hàng hoá chủ yếu vào mùa hè và là bối cảnh của lịch sử Pustozersk.",
    "Sông Pechora là dòng chảy định hình toàn bộ đời sống của vùng Nenets. Bắt nguồn từ phần bắc dãy Ural, con sông dài hơn một nghìn tám trăm cây số băng qua Cộng hoà Komi rồi mở ra một vùng châu thổ rộng lớn trước khi đổ vào biển Pechora (một phần biển Barents). Chính bên hạ lưu Pechora, thủ phủ Naryan-Mar đã hình thành quanh một bến cảng gỗ, và đến nay cảng sông - biển ở đây vẫn là cửa ngõ vận tải sống còn: vào mùa hè, khi băng tan, sông trở thành tuyến đường chính chở nhiên liệu, hàng hoá và vật tư cho cả vùng lãnh nguyên gần như không có đường bộ nối với phần còn lại của nước Nga. Dòng Pechora cũng là chứng nhân lịch sử - cách thành phố vài chục cây số, bên một nhánh sông xưa, từng mọc lên Pustozersk, đô thị Bắc Cực đầu tiên của người Nga. Với du khách, dạo bờ kè Pechora ở Naryan-Mar, ngắm những con tàu, đàn chim và ánh mặt trời nửa đêm phản chiếu trên mặt nước là cách cảm nhận rõ nhất nhịp sống của thủ phủ phương Bắc.",
    [
        "Con sông chính và huyết mạch vận tải của Khu tự trị Nenets, đổ ra biển Pechora (Barents).",
        "Đoạn hạ lưu ôm lấy thủ phủ Naryan-Mar - nơi có cảng sông - biển quan trọng.",
        "Gắn với lịch sử Pustozersk và là tuyến vận tải chính vào mùa hè.",
    ],
    {
        "hours_vi": "Bờ sông và bờ kè tại Naryan-Mar tham quan tự do; giao thông đường sông theo mùa.",
        "ticket_vi": "Miễn phí khi dạo bờ sông; đi tàu/du thuyền tính phí riêng.",
        "duration_vi": "Tuỳ ý; dạo bờ kè khoảng 30-60 phút.",
        "best_time_vi": "Mùa hè (tháng 6-8) khi sông thông thoáng, có mặt trời nửa đêm; mùa đông sông đóng băng.",
        "tips_vi": "Kết hợp dạo bờ kè với tham quan trung tâm Naryan-Mar; hỏi về tour thuyền ra hướng Pustozersk/châu thổ.",
    },
    [
        {"title": "Wikipedia (EN) — Pechora (river)", "url": "https://en.wikipedia.org/wiki/Pechora_(river)"},
    ],
    ["river", "port", "pechora", "waterway", "naryan-mar"],
    maps_text("Река Печора", "Нарьян-Мар", "Pechora River", "Naryan-Mar", 67.6300, 52.9800),
))

# 12) Амдерма -----------------------------------------------------------------
RECORDS.append(rec(
    "amderma",
    "Làng Amderma (căn cứ Bắc Cực bên biển Kara)",
    "Амдерма",
    "Amderma",
    ["other"],
    69.76306, 61.66778,
    "Bờ biển Kara, bán đảo Yugorsky, gần eo Yugorsky Shar và đảo Vaygach, đông Khu tự trị Nenets, Nga.",
    "Ngôi làng vùng cực bên bờ biển Kara, trên bán đảo Yugorsky, cách Naryan-Mar khoảng 490 km. Thành lập năm 1933 để khai thác fluorit, từng là đô thị sầm uất và căn cứ thám hiểm Bắc Cực với sân bay - căn cứ quân sự, nay dân cư thưa vắng giữa cảnh quan cực bắc.",
    "Amderma - trong tiếng Nenets nghĩa gần như 'bãi hải mã' - là một trong những điểm dân cư xa xôi và giàu ký ức nhất của vùng Nenets, nằm bên bờ biển Kara ở rìa đông bán đảo Yugorsky, gần eo Yugorsky Shar và đảo Vaygach, cách thủ phủ Naryan-Mar tới khoảng 490 km. Làng ra đời tháng 7 năm 1933 gắn với việc khai thác mỏ fluorit (đá huỳnh thạch), rồi được nâng cấp thành khu định cư kiểu đô thị năm 1936. Sau Thế chiến II, khi các mỏ fluorit ở nơi khác dễ khai thác hơn được tìm ra, mỏ Amderma đóng cửa, nhưng làng vẫn phát triển như một căn cứ nghiên cứu và thám hiểm Bắc Cực, có sân bay và căn cứ quân sự. Thời hoàng kim, dân số lên tới nhiều nghìn người; đến các cuộc điều tra gần đây chỉ còn vài trăm. Amderma trải qua đêm vùng cực và ngày cực dài, khí hậu khắc nghiệt điển hình duyên hải Bắc Cực. Gần trạm khí tượng còn có cột mốc 'Âu - Á' dựng năm 1975 bên bờ Yugorsky Shar. Với những ai đam mê Bắc Cực và lịch sử Xô Viết, Amderma là một 'thị trấn ma' đầy ám ảnh và hùng vĩ.",
    [
        "Làng cực bắc bên biển Kara, bán đảo Yugorsky; cách Naryan-Mar ~490 km.",
        "Lập năm 1933 để khai thác fluorit; từng là căn cứ thám hiểm Bắc Cực với sân bay - căn cứ quân sự.",
        "Nay dân cư thưa vắng; gần trạm khí tượng có cột mốc 'Âu - Á' (1975).",
    ],
    {
        "hours_vi": "Là điểm dân cư vùng biên; tới nơi bằng đường hàng không theo lịch, cần giấy phép vùng biên.",
        "ticket_vi": "Không áp dụng; chi phí là vé bay và dịch vụ hạn chế tại chỗ.",
        "duration_vi": "1-2 ngày, thường trong hành trình khám phá đông Nenets.",
        "best_time_vi": "Mùa hè có ngày cực dài; mùa đông cực lạnh và tối, chỉ hợp người chuẩn bị kỹ.",
        "tips_vi": "Chuẩn bị giấy phép vùng biên và trang phục Bắc Cực; dịch vụ rất hạn chế, nên lo hậu cần trước.",
    },
    [
        {"title": "Wikipedia (EN) — Amderma", "url": "https://en.wikipedia.org/wiki/Amderma"},
        {"title": "Википедия (RU) — Амдерма", "url": "https://ru.wikipedia.org/wiki/Амдерма"},
    ],
    ["settlement", "kara-sea", "soviet-history", "polar", "arctic"],
    maps_text("Амдерма", "Ненецкий автономный округ", "Amderma", "Nenets Autonomous Okrug", 69.76306, 61.66778),
))

# 13) Индига ------------------------------------------------------------------
RECORDS.append(rec(
    "indiga",
    "Làng Indiga (cửa sông ra biển Barents)",
    "Индига",
    "Indiga",
    ["other"],
    67.6583, 49.0164,
    "Cửa sông Indiga đổ vào vịnh Indiga (biển Barents), trung tâm Timansky selsoviet, Khu tự trị Nenets, Nga.",
    "Ngôi làng ven biển ở cửa sông Indiga, nơi con sông đổ vào vịnh Indiga của biển Barents. Là trung tâm của Timansky selsoviet, Indiga nằm ở vùng biên giới và được biết đến với dự án cảng biển nước sâu quanh năm cùng tuyến đường sắt Barentskomur trong tương lai.",
    "Nằm ở phía tây Khu tự trị Nenets, làng Indiga toạ lạc ngay cửa sông cùng tên, nơi sông Indiga hoà vào vịnh Indiga của biển Barents. Đây là trung tâm hành chính của Timansky selsoviet, một điểm dân cư nhỏ giữa vùng lãnh nguyên và ven biển thuộc khu vực biên giới. Dù khiêm nhường về quy mô, Indiga lại thường được nhắc tới trong các kế hoạch phát triển lớn của nước Nga: nhờ vị trí có vùng nước sâu và ít đóng băng hơn nhiều cảng Bắc Cực khác, nơi đây được quy hoạch xây dựng một cảng biển nước sâu hoạt động quanh năm, kết nối với mạng lưới đường sắt qua tuyến 'Barentskomur' (Barents - Komi - Ural) dự kiến. Với du khách, Indiga là điểm khởi hành thú vị để khám phá bờ biển Barents hoang sơ và là cửa ngõ tới hẻm núi Bolshiye Vorota trên sông Belaya cách đó khoảng 40 km, cũng như trải nghiệm đời sống ngư dân - người chăn tuần lộc nơi rìa lục địa.",
    [
        "Làng ven biển ở cửa sông Indiga đổ vào vịnh Indiga (biển Barents).",
        "Trung tâm Timansky selsoviet; quy hoạch cảng nước sâu và đường sắt Barentskomur.",
        "Cửa ngõ tới hẻm núi Bolshiye Vorota (~40 km) và bờ biển Barents hoang sơ.",
    ],
    {
        "hours_vi": "Điểm dân cư vùng biên; tới nơi chủ yếu bằng đường hàng không nhỏ, cần giấy phép vùng biên.",
        "ticket_vi": "Không áp dụng; chi phí là vé bay và dịch vụ hạn chế.",
        "duration_vi": "1-2 ngày, thường làm điểm xuất phát cho các tour thiên nhiên.",
        "best_time_vi": "Mùa hè (tháng 7-8) để đi thuyền trên sông Belaya và khám phá bờ biển.",
        "tips_vi": "Chuẩn bị giấy phép vùng biên; hỏi trước về tour ra hẻm núi Bolshiye Vorota.",
    },
    [
        {"title": "Википедия (RU) — Индига (посёлок)", "url": "https://ru.wikipedia.org/wiki/Индига_(посёлок)"},
    ],
    ["settlement", "barents-sea", "port-project", "timan", "arctic"],
    maps_text("Индига", "Ненецкий автономный округ", "Indiga", "Nenets Autonomous Okrug", 67.6583, 49.0164),
))

# 14) Ома ---------------------------------------------------------------------
RECORDS.append(rec(
    "oma-village",
    "Làng Oma",
    "Ома",
    "Oma",
    ["other"],
    66.6436, 46.4923,
    "Bên sông Oma, vùng biên giới phía tây Khu tự trị Nenets, trung tâm Omsky selsoviet, Nga.",
    "Ngôi làng bên sông Oma ở phía tây Khu tự trị Nenets, trung tâm của Omsky selsoviet. Nằm trong vùng biên giới, Oma là một điểm dân cư truyền thống của người phương Bắc, gắn với nghề cá, chăn tuần lộc và đời sống lãnh nguyên ven biển White - Barents.",
    "Ở phía tây nam Khu tự trị Nenets, làng Oma nằm bên con sông cùng tên, là trung tâm hành chính của Omsky selsoviet và thuộc vùng biên giới. Đây là một trong những điểm dân cư lâu đời của vùng, nơi cư dân - gồm người Nga phương Bắc (Pomor), Komi và Nenets - sống dựa vào nghề đánh cá, chăn nuôi tuần lộc và các nghề thủ công truyền thống thích nghi với khí hậu lãnh nguyên. Cuộc sống ở Oma phản ánh rõ nét nhịp điệu của phương Bắc: mùa hè ngắn ngủi rộn ràng đánh bắt và chăn thả, mùa đông dài chìm trong băng tuyết và bóng tối vùng cực. Do vị trí xa xôi và cách trở, làng chủ yếu kết nối bằng đường hàng không nhỏ và đường sông - biển theo mùa. Với du khách tìm kiếm trải nghiệm đời sống bản địa nguyên bản, xa rời du lịch đại chúng, Oma là một lát cắt chân thực về cộng đồng phương Bắc nơi ranh giới giữa biển Trắng và biển Barents.",
    [
        "Làng bên sông Oma, trung tâm Omsky selsoviet, vùng biên giới phía tây Nenets.",
        "Cộng đồng Pomor - Komi - Nenets sống bằng nghề cá và chăn tuần lộc.",
        "Điểm dân cư truyền thống, xa du lịch đại chúng, phản ánh nhịp sống lãnh nguyên.",
    ],
    {
        "hours_vi": "Điểm dân cư vùng biên; tới nơi bằng đường hàng không nhỏ hoặc đường sông - biển theo mùa; cần giấy phép vùng biên.",
        "ticket_vi": "Không áp dụng; chi phí là đi lại và dịch vụ hạn chế.",
        "duration_vi": "1-2 ngày cho trải nghiệm đời sống bản địa.",
        "best_time_vi": "Mùa hè khi giao thông thuận lợi và có thể tham gia hoạt động ngoài trời.",
        "tips_vi": "Chuẩn bị giấy phép vùng biên; tôn trọng nếp sống và phong tục của cộng đồng địa phương.",
    },
    [
        {"title": "Komandirovka.ru — Посёлок Ома, Ненецкий автономный округ", "url": "https://www.komandirovka.ru/cities/omafna/"},
        {"title": "Bankgorodov.ru — Ома (Ненецкий автономный округ)", "url": "https://www.bankgorodov.ru/place/oma"},
    ],
    ["settlement", "pomor", "nenets", "fishing", "arctic"],
    maps_text("Ома", "Ненецкий автономный округ", "Oma village", "Nenets Autonomous Okrug", 66.6436, 46.4923),
))

# 15) Несь --------------------------------------------------------------------
RECORDS.append(rec(
    "nes-village",
    "Làng Nes (gốc bán đảo Kanin)",
    "Несь",
    "Nes",
    ["other"],
    66.6004, 44.6809,
    "Bên hữu ngạn sông Nes gần vịnh Mezen (biển Trắng), gốc bán đảo Kanin, trung tâm Kaninsky selsoviet, Khu tự trị Nenets, Nga.",
    "Ngôi làng ở cực tây nam Khu tự trị Nenets, bên sông Nes gần nơi đổ ra vịnh Mezen của biển Trắng, ở gốc bán đảo Kanin. Là trung tâm của Kaninsky selsoviet, Nes là một trong những điểm dân cư lớn và lâu đời của vùng, gắn với người Pomor và Nenets.",
    "Nes nằm ở góc tây nam của Khu tự trị Nenets, bên hữu ngạn sông Nes cách cửa sông (đổ ra vịnh Mezen của biển Trắng) không xa, ngay gốc bán đảo Kanin. Là trung tâm hành chính của Kaninsky selsoviet, đây là một trong những làng lớn và có bề dày lịch sử của vùng, hình thành từ thời các volost phương Bắc cuối thế kỷ 19. Cộng đồng cư dân gồm người Nga phương Bắc (Pomor), Komi và Nenets, sống bằng nghề cá ven biển Trắng, chăn nuôi tuần lộc trên bán đảo Kanin và các nghề truyền thống. Vị trí gần biển Trắng khiến khí hậu ở đây dịu hơn đôi chút so với các vùng cực đông của okrug, nhưng vẫn khắc nghiệt và mang đậm sắc thái phương Bắc. Với du khách, Nes là điểm khởi đầu để tìm hiểu văn hoá Pomor - Nenets và là cửa ngõ tới bán đảo Kanin hoang sơ, nơi có những đồng cỏ lãnh nguyên rộng lớn và đường bờ biển gió lộng.",
    [
        "Làng ở cực tây nam Nenets, bên sông Nes gần vịnh Mezen (biển Trắng), gốc bán đảo Kanin.",
        "Trung tâm Kaninsky selsoviet; một trong những làng lớn, lâu đời của vùng.",
        "Cộng đồng Pomor - Komi - Nenets; cửa ngõ tới bán đảo Kanin hoang sơ.",
    ],
    {
        "hours_vi": "Điểm dân cư vùng biên; tới nơi bằng đường hàng không nhỏ hoặc đường thuỷ theo mùa; cần giấy phép vùng biên.",
        "ticket_vi": "Không áp dụng; chi phí là đi lại và dịch vụ hạn chế.",
        "duration_vi": "1-2 ngày; lâu hơn nếu kết hợp khám phá bán đảo Kanin.",
        "best_time_vi": "Mùa hè khi giao thông thuận lợi và có thể đi lại trên bán đảo.",
        "tips_vi": "Chuẩn bị giấy phép vùng biên; tìm hiểu trước lịch bay/thuyền vì tần suất thấp.",
    },
    [
        {"title": "Komandirovka.ru — Посёлок Несь, Ненецкий автономный округ", "url": "https://www.komandirovka.ru/cities/neskzx/"},
    ],
    ["settlement", "pomor", "kanin-peninsula", "white-sea", "arctic"],
    maps_text("Несь", "Ненецкий автономный округ", "Nes village", "Nenets Autonomous Okrug", 66.6004, 44.6809),
))

# 16) Красное -----------------------------------------------------------------
RECORDS.append(rec(
    "krasnoye-village",
    "Làng Krasnoye (làng chăn tuần lộc bên Pechora)",
    "Красное",
    "Krasnoye",
    ["other"],
    67.8356, 53.5970,
    "Bên nhánh Kuysky Shar của sông Pechora, cách Naryan-Mar khoảng 33 km theo đường sông, Khu tự trị Nenets, Nga.",
    "Ngôi làng bên một nhánh của châu thổ sông Pechora, cách thủ phủ Naryan-Mar khoảng hơn ba mươi cây số. Krasnoye là một trung tâm chăn nuôi tuần lộc quan trọng của vùng, nơi có thể tìm hiểu gần gũi đời sống người Nenets và nghề chăn tuần lộc truyền thống.",
    "Không xa thủ phủ Naryan-Mar, làng Krasnoye nằm bên nhánh Kuysky Shar trong vùng châu thổ rộng lớn của sông Pechora, cách thành phố khoảng 33 km theo đường sông. Đây là một trong những làng gắn bó mật thiết nhất với nghề chăn nuôi tuần lộc - trụ cột kinh tế và văn hoá của người Nenets. Quanh làng là địa bàn hoạt động của các hợp tác xã chăn tuần lộc, nơi những người olenevod vẫn duy trì lối di cư theo đàn trên lãnh nguyên. Nhờ vị trí tương đối gần Naryan-Mar, Krasnoye thường được nhắc tới như một điểm để du khách tiếp cận đời sống bản địa: tìm hiểu về chum (lều) truyền thống, trang phục da tuần lộc, ẩm thực và phong tục của cư dân lãnh nguyên. Vào mùa xuân, không khí lễ hội của Ngày hội Người chăn tuần lộc lan toả khắp vùng, và những làng như Krasnoye chính là nơi lưu giữ sống động nhất tinh thần ấy.",
    [
        "Làng bên nhánh Kuysky Shar của châu thổ Pechora, cách Naryan-Mar ~33 km.",
        "Trung tâm chăn nuôi tuần lộc, gắn với đời sống người Nenets.",
        "Điểm tiếp cận văn hoá bản địa: lều chum, trang phục da tuần lộc, phong tục lãnh nguyên.",
    ],
    {
        "hours_vi": "Điểm dân cư; tới nơi bằng thuyền/xe trượt tuyết theo mùa hoặc trực thăng.",
        "ticket_vi": "Không áp dụng; chi phí là đi lại và tour trải nghiệm (nếu có).",
        "duration_vi": "Nửa ngày đến 1 ngày.",
        "best_time_vi": "Cuối đông - đầu xuân dịp Ngày hội Người chăn tuần lộc; mùa hè đi thuyền.",
        "tips_vi": "Nên đi cùng hướng dẫn viên để sắp xếp gặp gỡ, trải nghiệm văn hoá Nenets đúng cách và tôn trọng.",
    },
    [
        {"title": "Академик (мирр. ru.wiki) — Красное (Ненецкий автономный округ)", "url": "https://dic.academic.ru/dic.nsf/ruwiki/1813055"},
    ],
    ["settlement", "reindeer", "nenets", "pechora", "arctic"],
    maps_text("Красное", "Ненецкий автономный округ", "Krasnoye village", "Nenets Autonomous Okrug", 67.8356, 53.5970),
))

# 17) Искателей ---------------------------------------------------------------
RECORDS.append(rec(
    "iskateley",
    "Thị trấn Iskateley ('Người tìm kiếm')",
    "Искателей",
    "Iskateley",
    ["other"],
    67.6667, 53.1333,
    "Hạ lưu Pechora, cách Naryan-Mar khoảng 4 km, Khu tự trị Nenets, Nga.",
    "Khu định cư kiểu đô thị lớn nhất của Khu tự trị Nenets, nằm sát Naryan-Mar về phía hạ lưu Pechora. Tên gọi 'Iskateley' (Người tìm kiếm) gắn với các nhà thăm dò địa chất dầu khí, phản ánh vai trò trung tâm hậu cần cho ngành dầu khí của vùng.",
    "Ngay sát thủ phủ Naryan-Mar, chỉ cách khoảng 4 km về phía hạ lưu sông Pechora, là Iskateley - khu định cư kiểu đô thị (posyolok gorodskogo tipa) lớn nhất của Khu tự trị Nenets. Cái tên Iskateley, nghĩa là 'những người tìm kiếm', được đặt để tôn vinh các nhà thăm dò, khảo sát địa chất - những người đã tìm ra các mỏ dầu khí làm nên sự phát triển của vùng. Ngày nay, Iskateley là trung tâm hậu cần và dân cư gắn với ngành dầu khí, gần như hợp thành một cụm đô thị với Naryan-Mar. Dù bản thân là một thị trấn công nghiệp hiện đại hơn là điểm du lịch cổ kính, Iskateley cho thấy gương mặt đương đại của Nenets: nơi ngành công nghiệp dầu khí phát triển song hành cùng nghề chăn tuần lộc truyền thống trên lãnh nguyên bao quanh. Với du khách, đây thường là điểm dừng chân về hạ tầng, dịch vụ khi khám phá khu vực thủ phủ.",
    [
        "Khu định cư kiểu đô thị lớn nhất Nenets, sát Naryan-Mar (~4 km).",
        "Tên 'Người tìm kiếm' tôn vinh các nhà thăm dò dầu khí của vùng.",
        "Trung tâm hậu cần ngành dầu khí, gương mặt đương đại của lãnh nguyên Nenets.",
    ],
    {
        "hours_vi": "Là thị trấn nên tham quan tự do; dịch vụ theo giờ hành chính.",
        "ticket_vi": "Không mất phí; chi phí sinh hoạt/dịch vụ tuỳ nhu cầu.",
        "duration_vi": "Nửa ngày hoặc kết hợp cùng Naryan-Mar.",
        "best_time_vi": "Quanh năm; thuận tiện nhất vào mùa hè.",
        "tips_vi": "Gần như liền kề Naryan-Mar; dễ kết hợp trong chuyến thăm thủ phủ.",
    },
    [
        {"title": "Академик (мирр. ru.wiki) — Искателей (посёлок)", "url": "https://dic.academic.ru/dic.nsf/ruwiki/1508381"},
    ],
    ["settlement", "oil-and-gas", "urban", "pechora", "arctic"],
    maps_text("Искателей", "Ненецкий автономный округ", "Iskateley", "Nenets Autonomous Okrug", 67.6667, 53.1333),
))

# 18) Тельвиска ---------------------------------------------------------------
RECORDS.append(rec(
    "telviska",
    "Làng Telviska",
    "Тельвиска",
    "Telviska",
    ["other"],
    67.6360, 52.8863,
    "Bên châu thổ Pechora, cách Naryan-Mar khoảng 5 km về phía tây, Khu tự trị Nenets, Nga.",
    "Ngôi làng cổ bên châu thổ sông Pechora, rất gần thủ phủ Naryan-Mar. Telviska từng là trung tâm hành chính khu vực thời kỳ đầu Xô Viết, gắn với lịch sử vùng Pustozersk - Pechora và cộng đồng người Nga phương Bắc, Komi, Nenets.",
    "Chỉ cách Naryan-Mar chừng 5 km về phía tây, làng Telviska nằm trên vùng châu thổ mênh mông của sông Pechora. Đây là một trong những điểm dân cư lâu đời của khu vực, có lịch sử gắn liền với vùng Pustozersk - Pechora: những năm đầu sau khi thành lập Khu tự trị Nenets (1929), Telviska từng là một trung tâm hành chính quan trọng trước khi vai trò ấy chuyển về Naryan-Mar. Cộng đồng cư dân gồm người Nga phương Bắc, Komi và Nenets, sống bằng nghề cá, chăn tuần lộc và nông nghiệp lãnh nguyên hạn chế. Ngày nay Telviska là một làng yên bình với những ngôi nhà gỗ phương Bắc, gần gũi thiên nhiên châu thổ Pechora. Nhờ khoảng cách gần thủ phủ, đây là điểm dễ ghé để cảm nhận nếp sống làng quê phương Bắc và khung cảnh sông nước lãnh nguyên, bổ sung cho trải nghiệm đô thị ở Naryan-Mar.",
    [
        "Làng cổ bên châu thổ Pechora, chỉ cách Naryan-Mar ~5 km.",
        "Từng là trung tâm hành chính khu vực thời kỳ đầu Xô Viết.",
        "Cộng đồng Nga phương Bắc - Komi - Nenets; nếp sống làng quê lãnh nguyên yên bình.",
    ],
    {
        "hours_vi": "Là làng nên tham quan tự do; tới nơi bằng đường sông/đường mùa đông từ Naryan-Mar.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Nửa ngày.",
        "best_time_vi": "Mùa hè đi thuyền; mùa đông theo đường băng (zimnik).",
        "tips_vi": "Dễ ghép vào chuyến thăm Naryan-Mar; hỏi trước phương tiện qua sông theo mùa.",
    },
    [
        {"title": "OpenStreetMap / Mapcarta — Telviska", "url": "https://mapcarta.com/N606607750"},
    ],
    ["settlement", "history", "pechora", "nenets", "arctic"],
    maps_text("Тельвиска", "Ненецкий автономный округ", "Telviska", "Nenets Autonomous Okrug", 67.6360, 52.8863),
))

# 19) Оксино ------------------------------------------------------------------
RECORDS.append(rec(
    "oksino",
    "Làng Oksino (làng Pomor cổ bên Pechora)",
    "Оксино",
    "Oksino",
    ["other"],
    67.5838, 52.1777,
    "Bên hữu ngạn sông Pechora, cách Naryan-Mar khoảng 40 km về phía thượng lưu, Khu tự trị Nenets, Nga.",
    "Ngôi làng Pomor cổ nằm bên hữu ngạn sông Pechora, cách Naryan-Mar khoảng bốn mươi cây số về phía thượng lưu. Oksino tiêu biểu cho các làng Nga phương Bắc dọc sông Pechora, gắn với nghề cá, chăn tuần lộc và kiến trúc gỗ truyền thống.",
    "Cách thủ phủ Naryan-Mar khoảng 40 km về phía thượng lưu, làng Oksino nép mình bên hữu ngạn sông Pechora - một trong những làng Pomor (người Nga phương Bắc) cổ tiêu biểu dọc con sông lớn này. Trải qua nhiều thế kỷ, cư dân Oksino sống dựa vào dòng Pechora: đánh cá, chăn nuôi tuần lộc và duy trì các nghề thủ công phương Bắc. Làng lưu giữ dáng vẻ của những điểm dân cư Nga cổ ở lãnh nguyên - những ngôi nhà gỗ, bến sông và nhịp sống gắn chặt với chu kỳ băng tan, băng đóng của Pechora. Nằm trên tuyến giao thông đường sông lịch sử nối Pustozersk với thượng nguồn, Oksino là một mắt xích trong mạng lưới làng mạc từng làm nên sức sống của vùng Pechora - Nenets. Với du khách, đây là nơi cảm nhận vẻ đẹp trầm mặc, chân chất của làng quê phương Bắc bên dòng sông huyền thoại.",
    [
        "Làng Pomor cổ bên hữu ngạn Pechora, cách Naryan-Mar ~40 km về thượng lưu.",
        "Đời sống gắn với nghề cá, chăn tuần lộc và kiến trúc gỗ phương Bắc.",
        "Mắt xích trong mạng lưới làng mạc lịch sử của vùng Pechora - Pustozersk.",
    ],
    {
        "hours_vi": "Là làng nên tham quan tự do; tới nơi bằng thuyền hoặc đường mùa đông từ Naryan-Mar.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Nửa ngày.",
        "best_time_vi": "Mùa hè đi thuyền trên Pechora; mùa đông theo đường băng.",
        "tips_vi": "Kết hợp trong tour đường sông Pechora; chú ý lịch phương tiện theo mùa.",
    },
    [
        {"title": "Академик (мирр. ru.wiki) — Оксино", "url": "https://dic.academic.ru/dic.nsf/ruwiki/1842663"},
    ],
    ["settlement", "pomor", "pechora", "wooden-architecture", "arctic"],
    maps_text("Оксино", "Ненецкий автономный округ", "Oksino", "Nenets Autonomous Okrug", 67.5838, 52.1777),
))

# 20) Нельмин Нос -------------------------------------------------------------
RECORDS.append(rec(
    "nelmin-nos",
    "Làng Nelmin Nos (làng dân tộc Nenets)",
    "Нельмин Нос",
    "Nelmin Nos",
    ["other"],
    67.9815, 52.9556,
    "Bên nhánh Tundrovy Shar của châu thổ Pechora, cách Naryan-Mar khoảng 60 km, Khu tự trị Nenets, Nga.",
    "Ngôi làng dân tộc Nenets bên một nhánh của châu thổ Pechora, cách Naryan-Mar khoảng sáu mươi cây số. Nelmin Nos là một trong những trung tâm gìn giữ văn hoá, ngôn ngữ Nenets và nghề chăn nuôi tuần lộc, gắn với hợp tác xã 'Vyucheysky'.",
    "Nằm bên nhánh Tundrovy Shar trong vùng châu thổ rộng lớn của sông Pechora, cách thủ phủ Naryan-Mar khoảng 60 km, Nelmin Nos là một 'làng dân tộc' tiêu biểu của người Nenets. Đây là nơi cộng đồng bản địa gìn giữ đậm đặc bản sắc: tiếng Nenets, phong tục, ẩm thực và trên hết là nghề chăn nuôi tuần lộc - hoạt động gắn với hợp tác xã mang tên nhà thơ - chiến sĩ Nenets Vyucheysky. Cuộc sống ở Nelmin Nos xoay quanh đàn tuần lộc và chu kỳ lãnh nguyên: người dân vẫn duy trì các chuyến di cư theo đàn, dựng lều chum truyền thống, và tổ chức những ngày hội gắn với văn hoá phương Bắc. Với những ai muốn tìm hiểu sâu về dân tộc Nenets và đời sống chăn tuần lộc đích thực - không phải qua trưng bày bảo tàng mà giữa khung cảnh thật của lãnh nguyên - Nelmin Nos là một trong những điểm đến giàu ý nghĩa nhất của vùng.",
    [
        "Làng dân tộc Nenets bên nhánh Tundrovy Shar của châu thổ Pechora (~60 km từ Naryan-Mar).",
        "Trung tâm gìn giữ tiếng Nenets, phong tục và nghề chăn tuần lộc.",
        "Gắn với hợp tác xã tuần lộc 'Vyucheysky'; trải nghiệm văn hoá bản địa đích thực.",
    ],
    {
        "hours_vi": "Điểm dân cư; tới nơi bằng trực thăng, thuyền hoặc đường mùa đông tuỳ mùa.",
        "ticket_vi": "Không áp dụng; chi phí là đi lại và tour trải nghiệm (nếu có).",
        "duration_vi": "Nửa ngày đến 1 ngày, hoặc dài hơn nếu ra lãnh nguyên cùng người chăn tuần lộc.",
        "best_time_vi": "Cuối đông - đầu xuân dịp lễ hội; mùa hè đi thuyền, tham gia hoạt động lãnh nguyên.",
        "tips_vi": "Nên qua hướng dẫn viên để thu xếp gặp gỡ và trải nghiệm văn hoá Nenets đúng cách, tôn trọng cộng đồng.",
    },
    [
        {"title": "Академик (мирр. ru.wiki) — Нельмин Нос", "url": "https://dic.academic.ru/dic.nsf/ruwiki/1825415"},
    ],
    ["settlement", "nenets", "reindeer", "indigenous-culture", "arctic"],
    maps_text("Нельмин Нос", "Ненецкий автономный округ", "Nelmin Nos", "Nenets Autonomous Okrug", 67.9815, 52.9556),
))

# 21) Бугрино (остров Колгуев) ------------------------------------------------
RECORDS.append(rec(
    "bugrino",
    "Làng Bugrino (điểm dân cư duy nhất trên đảo Kolguyev)",
    "Бугрино",
    "Bugrino",
    ["other"],
    68.7829, 49.3036,
    "Bờ nam đảo Kolguyev, bên eo Pomorsky (biển Barents), Khu tự trị Nenets, Nga.",
    "Ngôi làng nhỏ bên bờ nam đảo Kolguyev - điểm dân cư duy nhất trên hòn đảo lãnh nguyên biệt lập này. Cộng đồng Nenets ở Bugrino sống bằng nghề chăn tuần lộc, săn bắt và đánh cá, giữa thiên nhiên chim muông phong phú của đảo.",
    "Trên hòn đảo Kolguyev cô lập giữa biển Barents, Bugrino là điểm dân cư duy nhất - một ngôi làng nhỏ bên bờ nam đảo, nhìn ra eo Pomorsky. Cư dân chủ yếu là người Nenets, sống theo lối truyền thống của đảo: chăn nuôi tuần lộc trên những đồng lãnh nguyên rộng, săn bắt hải cẩu và đánh cá. Nằm cách biệt hoàn toàn với đất liền, cuộc sống ở Bugrino gắn chặt với nhịp thiên nhiên khắc nghiệt và với những chuyến bay trực thăng hiếm hoi - phương tiện chính nối đảo với Naryan-Mar. Xung quanh làng, hệ đầm lầy và hồ của Kolguyev là nơi trú ngụ, làm tổ của vô số chim nước Bắc Cực mỗi mùa hè. Với du khách, Bugrino là hình ảnh cô đọng của sự sống con người ở một trong những nơi hẻo lánh nhất châu Âu: nhỏ bé, kiên cường và hoà mình vào thiên nhiên nguyên sơ của đảo.",
    [
        "Điểm dân cư duy nhất trên đảo Kolguyev, bên bờ nam nhìn ra eo Pomorsky.",
        "Cộng đồng Nenets sống bằng chăn tuần lộc, săn hải cẩu, đánh cá.",
        "Cô lập giữa biển Barents, nối với đất liền chủ yếu bằng trực thăng.",
    ],
    {
        "hours_vi": "Điểm dân cư đảo xa; tới nơi bằng trực thăng theo lịch, cần giấy phép vùng biên.",
        "ticket_vi": "Không áp dụng; chi phí là vé trực thăng và dịch vụ rất hạn chế.",
        "duration_vi": "Thường nằm trong hành trình nhiều ngày ra đảo.",
        "best_time_vi": "Mùa hè (tháng 6-8) khi thời tiết dịu và chim làm tổ.",
        "tips_vi": "Lên kế hoạch kỹ về chuyến bay và hậu cần; tôn trọng cộng đồng nhỏ và thiên nhiên đảo.",
    },
    [
        {"title": "Академик (мирр. ru.wiki) — Бугрино", "url": "https://dic.academic.ru/dic.nsf/ruwiki/1366911"},
    ],
    ["settlement", "kolguyev", "nenets", "island", "arctic"],
    maps_text("Бугрино", "Ненецкий автономный округ", "Bugrino", "Nenets Autonomous Okrug", 68.7829, 49.3036),
))

# 22) Каратайка ---------------------------------------------------------------
RECORDS.append(rec(
    "karatayka",
    "Làng Karatayka (đông Nenets)",
    "Каратайка",
    "Karatayka",
    ["other"],
    68.7617, 61.4099,
    "Vùng đông Khu tự trị Nenets, gần lưu vực sông Korotaikha và bán đảo Yugorsky, Nga.",
    "Ngôi làng ở phía đông Khu tự trị Nenets, gần lưu vực sông Korotaikha và chân bán đảo Yugorsky. Karatayka là một điểm dân cư Nenets sống bằng nghề chăn tuần lộc và đánh cá, giữa vùng lãnh nguyên và đài nguyên gần dãy Pai-Khoy.",
    "Nằm ở phía đông Khu tự trị Nenets, làng Karatayka toạ lạc gần lưu vực sông Korotaikha, không xa chân bán đảo Yugorsky và dãy Pai-Khoy - phần kéo dài cực bắc của dãy Ural. Đây là một trong những làng xa xôi phía đông của okrug, nơi cộng đồng người Nenets duy trì lối sống chăn nuôi tuần lộc di cư và đánh cá trên các dòng sông lãnh nguyên. Cảnh quan quanh làng là lãnh nguyên bằng phẳng chuyển dần sang những đồi thấp của Pai-Khoy về phía đông, nơi mùa đông kéo dài và khắc nghiệt, mùa hè ngắn nhưng rực rỡ ánh sáng. Cách biệt với thủ phủ, Karatayka kết nối chủ yếu bằng đường hàng không nhỏ. Với du khách ưa khám phá vùng sâu, làng là điểm dừng chân hiếm hoi để tiếp cận đời sống bản địa và thiên nhiên hoang sơ của phần đông Nenets, gần các đối tượng địa chất độc đáo như dãy Pai-Khoy.",
    [
        "Làng đông Nenets, gần sông Korotaikha và chân bán đảo Yugorsky.",
        "Cộng đồng Nenets sống bằng chăn tuần lộc và đánh cá lãnh nguyên.",
        "Gần dãy Pai-Khoy - phần kéo dài cực bắc của dãy Ural.",
    ],
    {
        "hours_vi": "Điểm dân cư vùng sâu; tới nơi bằng đường hàng không nhỏ, cần giấy phép vùng biên.",
        "ticket_vi": "Không áp dụng; chi phí là đi lại và dịch vụ rất hạn chế.",
        "duration_vi": "1-2 ngày trong hành trình khám phá đông Nenets.",
        "best_time_vi": "Mùa hè khi giao thông thuận lợi và có thể đi lại trên lãnh nguyên.",
        "tips_vi": "Chuẩn bị giấy phép vùng biên và hậu cần; hỏi trước lịch bay vì tần suất thấp.",
    },
    [
        {"title": "Академик (мирр. ru.wiki) — Каратайка", "url": "https://dic.academic.ru/dic.nsf/ruwiki/1803865"},
    ],
    ["settlement", "nenets", "reindeer", "pай-khoy", "arctic"],
    maps_text("Каратайка", "Ненецкий автономный округ", "Karatayka", "Nenets Autonomous Okrug", 68.7617, 61.4099),
))

# 23) Усть-Кара ---------------------------------------------------------------
RECORDS.append(rec(
    "ust-kara",
    "Làng Ust-Kara (cực đông Nenets, bên biển Kara)",
    "Усть-Кара",
    "Ust-Kara",
    ["other"],
    69.2446, 64.9206,
    "Bờ đông vịnh Kara (biển Kara), cửa sông Kara - ranh giới đông của Khu tự trị Nenets, Nga.",
    "Ngôi làng ở cực đông Khu tự trị Nenets, bên bờ vịnh Kara của biển Kara, gần cửa sông Kara - ranh giới với vùng Yamal. Là điểm dân cư Nenets sống bằng chăn tuần lộc và đánh cá, gần cấu trúc va chạm thiên thạch Kara khổng lồ.",
    "Ở tận cùng phía đông Khu tự trị Nenets, nơi con sông Kara làm ranh giới với Khu tự trị Yamalo-Nenets, làng Ust-Kara nằm bên bờ vịnh Kara của biển Kara - vùng biển lạnh giá đóng băng hơn chín tháng mỗi năm. Đây là một điểm dân cư Nenets xa xôi, cư dân sống bằng nghề chăn nuôi tuần lộc và đánh cá giữa thiên nhiên đài nguyên khắc nghiệt. Điều đặc biệt là làng nằm gần cấu trúc va chạm thiên thạch Kara - một hố va chạm cổ khổng lồ hình thành cách đây khoảng 70 triệu năm (cuối kỷ Phấn Trắng), nay đã bị bào mòn nặng nhưng vẫn đạt đường kính khoảng 65 km, thuộc hàng những hố va chạm lớn nhất từng biết trên Trái Đất. Với các nhà địa chất và du khách mê khoa học Trái Đất, khu vực quanh Ust-Kara là một địa điểm nghiên cứu độc đáo. Cách biệt và hoang sơ, làng là điểm cực đông đáng nhớ trên bản đồ du hành vùng Nenets.",
    [
        "Làng cực đông Nenets, bên vịnh Kara (biển Kara), gần cửa sông Kara giáp Yamal.",
        "Cộng đồng Nenets sống bằng chăn tuần lộc và đánh cá.",
        "Gần cấu trúc va chạm thiên thạch Kara (đường kính ~65 km, ~70 triệu năm tuổi).",
    ],
    {
        "hours_vi": "Điểm dân cư vùng biên cực đông; tới nơi bằng đường hàng không nhỏ, cần giấy phép vùng biên.",
        "ticket_vi": "Không áp dụng; chi phí là đi lại và dịch vụ rất hạn chế.",
        "duration_vi": "1-2 ngày trong hành trình khám phá đông Nenets.",
        "best_time_vi": "Mùa hè ngắn (tháng 7-8) khi biển và giao thông thuận lợi hơn.",
        "tips_vi": "Chuẩn bị giấy phép vùng biên và hậu cần kỹ; tần suất giao thông rất thấp.",
    },
    [
        {"title": "Wikipedia (EN) — Kara crater", "url": "https://en.wikipedia.org/wiki/Kara_crater"},
        {"title": "Академик (мирр. ru.wiki) — Усть-Кара", "url": "https://dic.academic.ru/dic.nsf/ruwiki/1514969"},
    ],
    ["settlement", "kara-sea", "impact-crater", "nenets", "arctic"],
    maps_text("Усть-Кара", "Ненецкий автономный округ", "Ust-Kara", "Nenets Autonomous Okrug", 69.2446, 64.9206),
))

# 24) Варнек (остров Вайгач) --------------------------------------------------
RECORDS.append(rec(
    "varnek",
    "Làng Varnek (làng duy nhất trên đảo thánh Vaygach)",
    "Варнек",
    "Varnek",
    ["other"],
    69.71528, 60.06000,
    "Bờ nam đảo Vaygach, ven eo Yugorsky Shar, Khu tự trị Nenets, Nga.",
    "Ngôi làng duy nhất trên đảo thánh Vaygach, nằm ở bờ nam đảo. Ra đời từ đầu thập niên 1930, mang tên nhà thám hiểm Bắc Cực A. I. Varnek, làng gắn với một mỏ kẽm - chì thời Gulag và là điểm dân cư nhỏ bé, biệt lập nhất của vùng.",
    "Trên hòn đảo thiêng Vaygach giữa biển Bắc Cực, Varnek là ngôi làng duy nhất, nép ở bờ nam đảo ven eo Yugorsky Shar. Làng hình thành vào nửa đầu thập niên 1930 và được đặt theo tên nhà thám hiểm Bắc Cực người Nga Aleksandr Ivanovich Varnek. Lịch sử nơi đây phủ bóng thời kỳ khắc nghiệt: từ năm 1921, người ta phát hiện quặng kẽm - chì trong vùng, và một khu mỏ được lập nên với lao động của tù nhân Gulag. Sau này, mỏ đóng cửa, và Varnek trở thành một cộng đồng Nenets nhỏ bé sống bằng chăn nuôi tuần lộc, đánh cá và săn bắt trên đảo. Với dân số chỉ khoảng một trăm người, Varnek từng là điểm dân cư cuối cùng của Khu tự trị Nenets được kết nối điện thoại (năm 2011) - minh chứng cho sự cô lập tột cùng của nó. Nằm ngay trên hòn đảo giàu ý nghĩa tâm linh và thiên nhiên hoang sơ, Varnek là cửa ngõ hiếm hoi để những đoàn thám hiểm tiếp cận Vaygach.",
    [
        "Làng duy nhất trên đảo thánh Vaygach, ở bờ nam ven eo Yugorsky Shar.",
        "Lập đầu thập niên 1930, mang tên nhà thám hiểm Bắc Cực A. I. Varnek; gắn với mỏ kẽm - chì thời Gulag.",
        "Điểm dân cư cuối cùng của Nenets được kết nối điện thoại (2011); dân số chỉ ~100 người.",
    ],
    {
        "hours_vi": "Làng đảo xa vùng biên; tới nơi qua tour thám hiểm/tàu và cần giấy phép vùng biên.",
        "ticket_vi": "Không áp dụng; chi phí là tour thám hiểm Bắc Cực (cao).",
        "duration_vi": "Thường nằm trong hành trình nhiều ngày trên biển Bắc Cực.",
        "best_time_vi": "Mùa hè ngắn (tháng 7-8) khi biển bớt băng.",
        "tips_vi": "Cần giấy phép vùng biên; tôn trọng cộng đồng nhỏ và các di tích thờ cúng thiêng liêng trên đảo.",
    },
    [
        {"title": "Wikipedia (EN) — Varnek", "url": "https://en.wikipedia.org/wiki/Varnek"},
    ],
    ["settlement", "vaygach", "gulag-history", "nenets", "arctic"],
    maps_text("Варнек", "Ненецкий автономный округ", "Varnek", "Nenets Autonomous Okrug", 69.71528, 60.06000),
))

# 25) Мыс Канин Нос -----------------------------------------------------------
RECORDS.append(rec(
    "cape-kanin-nos",
    "Mũi Kanin Nos (điểm cực tây, có hải đăng)",
    "Мыс Канин Нос",
    "Cape Kanin Nos",
    ["other"],
    68.6414, 43.3847,
    "Mũi tây bắc bán đảo Kanin, điểm cực tây Khu tự trị Nenets, nơi biển Trắng gặp biển Barents, Nga.",
    "Mũi đất ở đầu tây bắc bán đảo Kanin - điểm cực tây của Khu tự trị Nenets, nơi biển Trắng gặp biển Barents. Trên mũi có hải đăng và trạm khí tượng, giữa cảnh quan lãnh nguyên gió lộng và những vách bờ biển hoang sơ.",
    "Ở đầu tây bắc bán đảo Kanin, mũi Kanin Nos vươn ra nơi biển Trắng hoà vào biển Barents, đánh dấu điểm cực tây của Khu tự trị Nenets. Đây là một địa danh hàng hải quan trọng: trên mũi có ngọn hải đăng và trạm khí tượng, từ lâu là điểm định vị cho tàu thuyền đi qua vùng biển thường xuyên bão gió này. Cảnh quan quanh Kanin Nos là lãnh nguyên ven biển trải rộng, những đồng cỏ gió lộng và đường bờ biển với các vách đá thấp - khung cảnh phương Bắc hoang sơ, khắc nghiệt mà hùng vĩ. Vùng biển ngoài khơi là nơi cá voi trắng (beluga) thường lui tới, đôi khi có cả cá nhà táng. Xa xôi và ít người lui tới, mũi Kanin Nos mang sức hút của những 'điểm tận cùng' trên bản đồ: nơi đất liền chấm dứt và đại dương Bắc Cực bắt đầu. Với du khách ưa phiêu lưu và người mê hải đăng, đây là một đích đến đầy chất sử thi ở rìa tây của vùng Nenets.",
    [
        "Điểm cực tây của Khu tự trị Nenets, nơi biển Trắng gặp biển Barents.",
        "Có hải đăng và trạm khí tượng - điểm định vị hàng hải giữa vùng biển bão gió.",
        "Cảnh quan lãnh nguyên ven biển hoang sơ; ngoài khơi có cá voi trắng (beluga).",
    ],
    {
        "hours_vi": "Địa danh hẻo lánh vùng biên; không có tham quan thông thường, chỉ tiếp cận qua chuyến đi đặc biệt.",
        "ticket_vi": "Không áp dụng; chi phí là phương tiện chuyên dụng và giấy phép.",
        "duration_vi": "Thường nằm trong hành trình thám hiểm bán đảo Kanin nhiều ngày.",
        "best_time_vi": "Mùa hè ngắn (tháng 7-8) khi thời tiết dịu hơn.",
        "tips_vi": "Cần giấy phép vùng biên và chuẩn bị kỹ cho gió bão; tôn trọng công việc của trạm hải đăng - khí tượng.",
    },
    [
        {"title": "Wikipedia (EN) — Kanin Peninsula (Cape Kanin Nos)", "url": "https://en.wikipedia.org/wiki/Kanin_Peninsula"},
    ],
    ["cape", "lighthouse", "kanin-peninsula", "white-sea", "arctic"],
    maps_text("Мыс Канин Нос", "Ненецкий автономный округ", "Cape Kanin Nos", "Nenets Autonomous Okrug", 68.6414, 43.3847),
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
