# -*- coding: utf-8 -*-
"""_add_places_kalmykia_20260728.py — VÙNG: Cộng hoà Kalmykia (Республика Калмыкия)
(lần chạy tự động 2026-07-28).

Bối cảnh: kalmykia.json hiện có 7 địa điểm (Golden Abode/Central Khurul, Chess City,
Pagoda Bảy Ngày, Сякюсн-Сюме/chùa vàng cũ, cánh đồng tulip Manych, Cổng Vàng Altn Bosch,
Bảo tàng Quốc gia). Bổ sung 23 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại
hình → đưa vùng lên 30.

Kalmykia là nước cộng hoà Phật giáo duy nhất ở châu Âu; vì vậy các khurul (chùa) là loại
danh lam đặc trưng nhất — chiếm tỷ trọng lớn (đúng bản chất vùng), bên cạnh thảo nguyên/hồ,
tượng đài Elista, nhà hát và quảng trường.

Phân bố loại hình (23 bản ghi mới):
- park_garden (7): Маныч-Гудило, Меклетинские розовые озёра, Одинокий тополь, Большое
  Яшалтинское (солёное) озеро, заповедник «Чёрные земли» (сайгаки), парк «Дружба»,
  Чограйское водохранилище.
- church (7 — dùng cho công trình tôn giáo): Лаганский хурул, Цаган-Аманский хурул, Ступа
  Просветления (Элиста), Казанский кафедральный собор (православный), Чёёря-хурул (Ики-Чонос),
  Троицкий хурул «Оргьен Сангак Чойлинг», хурул в Яшалте.
- monument (6): Золотой всадник, памятник Остапу Бендеру, «Исход и Возвращение» (Э.Неизвестный),
  памятник Оке Городовикову, скульптура «Белый старец / Цаган Аав», Мемориал героев (Вечный огонь).
- theatre (2): Нацдрамтеатр им. Б. Басангова, Русский театр драмы и комедии.
- square_street (1): площадь Ленина (Элиста).

TOẠ ĐỘ — xác minh chéo (ru.wikipedia geohack/infobox, OpenStreetMap/Nominatim, autotravel/
tonkosti/russpass toạ độ text N.. E.., 2026-07-28). Phạm vi Kalmykia lat ~44,5–47,6; lon
~42,2–47,4 — tất cả toạ độ trong phạm vi, KHÔNG đảo lat/lon:
  Маныч-Гудило 46.2306,42.9605 (N46 13.836 E42 57.63); Меклетинское 45.675356,45.656290;
  Одинокий тополь 46.28028,44.01111 (ru.wiki 46°16′49″N 44°00′40″E); Б.Яшалтинское
  46.2649,42.4184 (N46 15.894 E42 25.104); заповедник «Чёрные земли»/офис 45.3331863,46.0422631
  (OSM, п.Комсомольский, ул.Некрасова); парк «Дружба» 46.307122,44.263228; Чограйское
  водохранилище 45.5319587,44.4136828 (OSM, Ики-Бурульский р-н); Лаганский хурул
  45.4062449,47.3412538 (OSM, ул.Автомобилистов, Лагань); Цаган-Аманский хурул
  47.5447479,46.7341932 (OSM, ул.Тогмед-Гавджи — điểm cực bắc vùng, sát biên Astrakhan);
  Ступа Просветления 46.3010,44.3011 (N46 18.06 E44 18.066); Казанский собор 46.3087,44.2318
  (N46 18.522 E44 13.908); Чёёря-хурул 46.4246450,44.4689497 (OSM, Ики-Чонос); Троицкий хурул
  46.4212609,44.2589751 (OSM, с.Троицкое); хурул Яшалта 46.3388587,42.2671662 (OSM); Золотой
  всадник 46.318135,44.258273; памятник Остапу Бендеру 46.3037,44.3036 (N46 18.222 E44 18.216);
  «Исход и Возвращение» 46.30056,44.31472 (ru.wiki 46°18′02″N 44°18′53″E); памятник
  Городовикову 46.31933,44.27852 (N046 19.160 E044 16.711); «Белый старец» 46.3075303,44.26618
  (OSM, ул.Ленина); Мемориал/Вечный огонь 46.305859,44.2591709 (OSM); Драмтеатр Басангова
  46.3049051,44.2632157 (OSM, ул.Сусеева 21); Русский театр 46.3096481,44.2685214 (OSM,
  ул.М.Горького 23); площадь Ленина 46.3077,44.2697 (N46 18.462 E44 16.182).

GHI CHÚ: đã BỎ QUA các đối tượng KHÔNG xác minh được toạ độ tin cậy / trùng vị trí / nằm ngoài
vùng, gồm: Хошеутовский хурул (thực tế thuộc Астраханская область — ngoài Kalmykia), Сарпинские
озёра & озеро Барманцак (hệ hồ phân tán, một phần thuộc Волгоградская обл., không có điểm OSM
tin cậy), озеро Деед-Хулсун (không có node OSM tên rõ, lại trùng loại «hồ bồ nông» với Маныч),
«марсианские пейзажи» Адык (không có toạ độ tin cậy). KHÔNG bịa toạ độ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_kalmykia_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "kalmykia"
REGION_NAME_VI = "Cộng hoà Kalmykia"
FD = "Vùng Nam"


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


def steppe_practical(duration, best_time, tips):
    return {
        "hours_vi": "Đối tượng thiên nhiên ngoài trời, tham quan ban ngày; không có giờ cố định.",
        "ticket_vi": "Khu ngoài trời thường không thu vé cố định; một số khu bảo tồn thu phí và yêu cầu đăng ký/hướng dẫn viên.",
        "duration_vi": duration,
        "best_time_vi": best_time,
        "tips_vi": tips,
    }


RECORDS = []

# ============================ THIÊN NHIÊN / THẢO NGUYÊN / HỒ ============================

# 1) Озеро Маныч-Гудило -------------------------------------------------------------
RECORDS.append(rec(
    "manych-gudilo-lake",
    "Hồ Manych-Gudilo",
    "Озеро Маныч-Гудило",
    "Lake Manych-Gudilo",
    ["park_garden"],
    46.2306, 42.9605,
    "Nằm ở ranh giới Cộng hoà Kalmykia - vùng Stavropol - tỉnh Rostov (phía tây Kalmykia), Nga.",
    "Manych-Gudilo là hồ nước mặn di tích khổng lồ trải dài khoảng 150 km trên vùng trũng Kuma-Manych, mặn hơn cả Biển Đen. Đây là thiên đường chim di cư của thảo nguyên Nga, nổi tiếng với đảo Ptichy (đảo Chim) - nơi bồ nông, thiên nga và nhiều loài quý hiếm làm tổ.",
    "Trải dài khoảng 150 km dọc vùng trũng Kuma-Manych, Manych-Gudilo là một trong những hồ nước mặn lớn và cổ xưa nhất miền nam nước Nga, phần lớn nằm ở ranh giới Kalmykia với vùng Stavropol và tỉnh Rostov. Nước hồ mặn hơn cả Biển Đen, diện tích thay đổi theo mùa, để lộ những dải cồn và đảo nhỏ giữa thảo nguyên bao la. Tên gọi 'Gudilo' (nghĩa gần với 'gào rú') bắt nguồn từ tiếng gió rít lạ lùng trên mặt hồ trống trải. Đây là khu vực trọng yếu trên đường bay di cư của chim: trên đảo Ptichy (đảo Chim) và các đảo lân cận, hàng loạt loài làm tổ như bồ nông hồng và bồ nông xoăn (đều nằm trong Sách Đỏ), cò thìa, mòng biển, thiên nga cổ trắng, choi choi... Vào mùa xuân, bờ hồ và các đảo còn rực sắc tulip và hoa thảo nguyên hoang dã. Hồ là một phần của khu bảo tồn sinh quyển 'Đảo Vodny/Chёрные земли' và vùng đất ngập nước có ý nghĩa quốc tế, là điểm ngắm chim và chụp ảnh thiên nhiên hàng đầu của Kalmykia.",
    [
        "Hồ nước mặn di tích dài khoảng 150 km, mặn hơn Biển Đen, giữa thảo nguyên Kuma-Manych.",
        "Đảo Ptichy (đảo Chim) - nơi bồ nông, cò thìa, thiên nga và nhiều loài quý hiếm làm tổ.",
        "Điểm ngắm chim di cư và ngắm tulip hoang dã mùa xuân bậc nhất miền nam nước Nga.",
    ],
    steppe_practical(
        "Khoảng nửa ngày (nên đi cùng tour/thuyền để ra gần các đảo chim).",
        "Cuối tháng 4 - đầu tháng 5 (mùa tulip nở và chim làm tổ) là đẹp nhất.",
        "Đi cùng hướng dẫn viên hoặc tour thuyền địa phương; mang ống nhòm, kem chống nắng, nước; không lại quá gần tổ chim.",
    ),
    [
        {"title": "Wikipedia (RU) — Маныч-Гудило", "url": "https://ru.wikipedia.org/wiki/Маныч-Гудило"},
        {"title": "КП — Озеро Маныч-Гудило", "url": "https://www.kp.ru/russia/kalmykiya/mesta/ozero-manych-gudilo/"},
    ],
    ["lake", "birdwatching", "pelican", "steppe", "nature", "ramsar"],
    maps_text("Озеро Маныч-Гудило", "Калмыкия", "Lake Manych-Gudilo", "Kalmykia", 46.2306, 42.9605),
))

# 2) Меклетинские розовые озёра -----------------------------------------------------
RECORDS.append(rec(
    "meklety-pink-lakes",
    "Hồ hồng Meklety (Mekletinskoye)",
    "Меклетинские розовые озёра",
    "Meklety Pink Lakes",
    ["park_garden"],
    45.675356, 45.656290,
    "Quận Chernozemelsky (gần làng Adyk), Cộng hoà Kalmykia, Nga.",
    "Hồ hồng Meklety là hồ nước mặn nổi tiếng nhất Kalmykia với sắc nước hồng rực siêu thực do vi tảo tiết sắc tố đỏ. Mùa hè nước cạn để lại lớp muối kết tinh, tạo nên khung cảnh 'như hành tinh khác' giữa thảo nguyên hoang mạc.",
    "Nằm trong quận Chernozemelsky, giữa vùng bán hoang mạc phía đông nam Kalmykia, Meklety là quần thể hồ nước mặn nổi tiếng nhờ màu nước hồng đến đỏ tía kỳ ảo. Sắc hồng sinh ra từ vi tảo (và vi khuẩn ưa mặn) tiết sắc tố đỏ khi độ mặn tăng cao dưới nắng gắt. Vào mùa hè, hồ cạn dần, muối kết tinh thành những dải trắng nối các vũng nước hồng, khiến nhiều người tưởng có nhiều hồ riêng biệt và ví cảnh vật 'như trên sao Hỏa'. Hành trình tới hồ thường bắt đầu từ làng Adyk - nơi cũng gần các 'cảnh quan sao Hỏa' đất sét đặc trưng. Đây là điểm chụp ảnh và ngắm hoàng hôn ăn khách, đồng thời nằm trong vùng lân cận khu bảo tồn thảo nguyên, nơi thi thoảng bắt gặp linh dương saiga. Do là hồ muối tự nhiên trong khu vực nhạy cảm, du khách nên giữ gìn môi trường và không mang muối/khoáng vật ra khỏi khu vực.",
    [
        "Nước hồng - đỏ tía siêu thực do vi tảo ưa mặn, đẹp nhất khi nắng gắt mùa hè.",
        "Muối kết tinh trắng xen các vũng hồng tạo khung cảnh 'như hành tinh khác'.",
        "Kết hợp làng Adyk và 'cảnh quan sao Hỏa' đất sét gần đó; điểm ngắm hoàng hôn nổi tiếng.",
    ],
    steppe_practical(
        "Khoảng 1,5–2 giờ tại hồ (chưa kể đường đi khá xa, nên đi trong ngày).",
        "Tháng 6–8 khi nước cạn và độ mặn cao, màu hồng rõ nhất; đẹp lúc bình minh/hoàng hôn.",
        "Cần xe gầm cao hoặc tour; mang nhiều nước, mũ, kem chống nắng; không có bóng mát và dịch vụ; đi giày dễ rửa vì bùn muối.",
    ),
    [
        {"title": "Заповедник «Чёрные земли» — Меклетинские розовые озёра", "url": "https://zapovednik-chernyezemli.ru/mekletinskiye_rozovyye_ozera"},
        {"title": "RUSSPASS — Меклетинское розовое озеро", "url": "https://russpass.ru/event/6683e66cdc7bb1a0eaa80c20"},
    ],
    ["pink-lake", "salt-lake", "steppe", "nature", "photography", "adyk"],
    maps_text("Меклетинское розовое озеро", "Черноземельский район", "Meklety Pink Lake", "Kalmykia", 45.675356, 45.656290),
))

# 3) Одинокий тополь с каскадом родников --------------------------------------------
RECORDS.append(rec(
    "lonely-poplar-khar-buluk",
    "Cây dương cô độc và dòng suối thiêng (Odinokiy Topol)",
    "Одинокий тополь с каскадом родников",
    "The Lonely Poplar with Cascade of Springs",
    ["park_garden"],
    46.28028, 44.01111,
    "Sườn nam dãy Khamur, cách làng Khar-Buluk khoảng 5 km, quận Tselinny, Cộng hoà Kalmykia, Nga.",
    "Odinokiy Topol là cây dương cổ thụ đứng đơn độc giữa thảo nguyên, được xem là thánh tích của Phật tử Kalmykia. Tương truyền một nhà sư trồng cây từ hạt mang về từ Tây Tạng; quanh gốc có suối khoáng và một quần thể bảo tháp trắng.",
    "Trên sườn nam dãy đồi Khamur ở nam vùng Ergeni, cách làng Khar-Buluk chừng 5 km, một cây dương lá nguyệt quế cao khoảng 20 m đứng đơn độc giữa thảo nguyên mênh mông - hình ảnh đã thành biểu tượng thiêng của Kalmykia. Theo truyền thuyết được lưu truyền rộng rãi, nhà sư Purdash-bakshi Dzhungruev, trụ trì một đại tự, sau chuyến hành hương Tây Tạng đã mang hạt dương giấu trong khe cây tích trượng; ông chôn tích trượng trên điểm cao nhất của gò đất gần Khar-Buluk và từ đó cây dương mọc lên. Cây được công nhận là di tích thiên nhiên cấp vùng (từ 1981) và ghi vào sổ bộ cây cổ thụ nước Nga. Dưới chân cây có những mạch suối nước ngọt và nước khoáng được cho là có tác dụng chữa bệnh. Từ năm 2013, quanh cây hình thành một thánh địa Phật giáo với bảo tháp (stupa) và tám bệ đá trắng. Ngày nay đây là nơi hành hương, buộc khăn cầu nguyện và ngắm hoàng hôn thảo nguyên; năm 2019 cây từng đoạt danh hiệu 'Cây của năm' toàn Nga.",
    [
        "Cây dương cổ thụ đơn độc cao ~20 m, biểu tượng thiêng của thảo nguyên Kalmykia.",
        "Gắn truyền thuyết nhà sư mang hạt từ Tây Tạng; có bảo tháp và tám bệ đá trắng bao quanh.",
        "Suối nước ngọt và nước khoáng dưới gốc, được coi là có tác dụng chữa bệnh.",
    ],
    steppe_practical(
        "Khoảng 45–60 phút; tiện kết hợp trên đường ra/vào Elista.",
        "Cuối xuân đến đầu thu; đẹp nhất lúc bình minh và hoàng hôn.",
        "Đường từ Elista khá gần nhưng đoạn cuối là đường đất; tôn trọng nghi lễ, đi vòng quanh bảo tháp theo chiều kim đồng hồ; có thể buộc khăn cầu nguyện (khadag).",
    ),
    [
        {"title": "Wikipedia (RU) — Одинокий тополь с каскадом родников", "url": "https://ru.wikipedia.org/wiki/Одинокий_тополь_с_каскадом_родников"},
        {"title": "NazAccent — Одинокий тополь: священное место в Калмыкии", "url": "https://nazaccent.ru/content/28288-odinokij-topol-svyashennoe-mesto-v-kalmykii/"},
    ],
    ["sacred-tree", "buddhist", "steppe", "nature", "pilgrimage", "spring"],
    maps_text("Одинокий тополь", "Хар-Булук, Калмыкия", "Lonely Poplar", "Khar-Buluk, Kalmykia", 46.28028, 44.01111),
))

# 4) Большое Яшалтинское (солёное) озеро ---------------------------------------------
RECORDS.append(rec(
    "yashalta-salt-lake",
    "Hồ muối Bolshoye Yashaltinskoye (Hồ Muối)",
    "Большое Яшалтинское солёное озеро",
    "Bolshoye Yashaltinskoye Salt Lake",
    ["park_garden"],
    46.2649, 42.4184,
    "Quận Yashalta (giữa các làng Berezovskoye và Solyonoye), phía tây Cộng hoà Kalmykia, Nga.",
    "Bolshoye Yashaltinskoye là hồ muối lớn ở tây Kalmykia, nổi tiếng với bùn khoáng sulfid chữa bệnh. Bên hồ là khu điều dưỡng 'Solyonoye Ozero' thuộc hàng đầu về trị liệu bằng bùn và nước muối của Nga.",
    "Nằm ở quận Yashalta phía tây Kalmykia, giữa các làng Berezovskoye và Solyonoye, Bolshoye Yashaltinskoye là hồ nước mặn rộng khoảng 40 km2 (dài tới 8 km, rộng tới 5 km). Điều làm hồ nổi tiếng là trữ lượng lớn bùn khoáng sulfid (bùn đen) có giá trị trị liệu, cùng nước muối đậm đặc. Trên bờ hồ có khu điều dưỡng - nghỉ dưỡng 'Solyonoye Ozero' (Hồ Muối), được xếp vào nhóm cơ sở trị liệu bằng bùn hàng đầu ở Nga, chuyên điều trị và phòng ngừa các bệnh cơ xương khớp, ngoài da, thần kinh... Vào mùa hè, độ mặn cao khiến nước có thể ánh sắc hồng nhạt và bờ hồ đóng muối trắng, tạo khung cảnh thảo nguyên hoang sơ đặc trưng. Đây là điểm đến kết hợp nghỉ dưỡng - chữa bệnh và trải nghiệm thiên nhiên độc đáo ở vùng cực tây của nước cộng hoà.",
    [
        "Hồ muối lớn (~40 km2) với bùn khoáng sulfid chữa bệnh nổi tiếng.",
        "Khu điều dưỡng 'Solyonoye Ozero' thuộc hàng đầu về trị liệu bằng bùn của Nga.",
        "Nước muối đậm đặc, bờ đóng muối trắng, cảnh thảo nguyên hoang sơ.",
    ],
    steppe_practical(
        "Nửa ngày trở lên nếu trải nghiệm tắm bùn/điều dưỡng.",
        "Mùa hè (tháng 6–8) khi hồ ấm và độ mặn cao.",
        "Muốn trị liệu nên đặt trước tại khu điều dưỡng; tắm bùn cần tư vấn y tế; mang dép, nước ngọt để tráng người sau khi tắm muối.",
    ),
    [
        {"title": "Wikipedia (RU) — Большое Яшалтинское", "url": "https://ru.wikipedia.org/wiki/Большое_Яшалтинское"},
        {"title": "Votpusk — Большое Яшалтинское озеро", "url": "https://www.votpusk.ru/article/attractions/rossiya-yug/kalmykiya/bolshoe_yashaltinskoe_ozero-a"},
    ],
    ["salt-lake", "healing-mud", "spa", "nature", "yashalta"],
    maps_text("Большое Яшалтинское озеро", "Яшалтинский район", "Bolshoye Yashaltinskoye Salt Lake", "Kalmykia", 46.2649, 42.4184),
))

# 5) Заповедник «Чёрные земли» -------------------------------------------------------
RECORDS.append(rec(
    "chernye-zemli-reserve",
    "Khu bảo tồn sinh quyển Chernye Zemli (Đất Đen) - vương quốc linh dương saiga",
    "Государственный биосферный заповедник «Чёрные земли»",
    "Chernye Zemli (Black Lands) Nature Reserve",
    ["park_garden"],
    45.3331863, 46.0422631,
    "Trụ sở khu bảo tồn: làng Komsomolsky, phố Nekrasova 31, quận Chernozemelsky, Cộng hoà Kalmykia, Nga.",
    "Chernye Zemli là khu bảo tồn sinh quyển duy nhất ở Nga bảo vệ quần thể linh dương saiga - loài thú thảo nguyên cổ xưa, biểu tượng của Kalmykia. Được lập năm 1990, khu bảo tồn rộng hơn 121.000 ha gồm phân khu thảo nguyên - bán hoang mạc và phân khu đất ngập nước ở hồ Manych-Gudilo.",
    "Được thành lập năm 1990 và mang tầm khu dự trữ sinh quyển của UNESCO, 'Chёрные земли' ('Đất Đen' - vì tuyết mỏng, đất lộ sẫm màu quanh năm) là thành trì bảo vệ đàn linh dương saiga - loài thú móng guốc cổ xưa từ thời băng hà, nay cực kỳ nguy cấp và là biểu tượng sống của thảo nguyên Kalmykia. Khu bảo tồn rộng hơn 121.000 ha, chia làm hai cụm: cụm thảo nguyên - bán hoang mạc rộng lớn (nơi saiga sinh sống và di cư) ở các quận Chernozemelsky và Yashkulsky, và cụm đất ngập nước quanh hồ Manych-Gudilo (điểm dừng chân của hàng vạn chim nước di cư). Đây là một trong số ít nơi ở châu Âu còn cảnh quan hoang mạc - bán hoang mạc gần như nguyên vẹn, với các loài đặc hữu và quý hiếm. Ban quản lý ở làng Komsomolsky tổ chức tuyến sinh thái, 'trung tâm phục hồi saiga' và các chương trình quan sát động vật hoang dã; du khách cần đăng ký trước và đi cùng kiểm lâm.",
    [
        "Khu bảo tồn duy nhất ở Nga dành cho linh dương saiga - biểu tượng thảo nguyên Kalmykia.",
        "Rộng hơn 121.000 ha, gồm cụm thảo nguyên - bán hoang mạc và cụm đất ngập nước Manych-Gudilo.",
        "Khu dự trữ sinh quyển với tuyến sinh thái và trung tâm phục hồi saiga.",
    ],
    steppe_practical(
        "Nửa ngày đến trọn ngày tuỳ tuyến (khoảng cách trong khu rất lớn).",
        "Mùa xuân (tulip nở, chim di cư) và đầu mùa thu; sáng sớm/chiều muộn dễ thấy saiga.",
        "Bắt buộc đăng ký trước với ban quản lý và đi cùng kiểm lâm; cần xe phù hợp, nước, ống nhòm; tuyệt đối không tự ý vào vùng lõi.",
    ),
    [
        {"title": "Wikipedia (RU) — Чёрные земли (заповедник)", "url": "https://ru.wikipedia.org/wiki/Чёрные_земли_(заповедник)"},
        {"title": "Заповедник «Чёрные земли» — официальный сайт", "url": "https://zapovednik-chernyezemli.ru/about"},
    ],
    ["nature-reserve", "saiga", "steppe", "biosphere", "wildlife", "unesco"],
    maps_text("Заповедник Чёрные земли", "Комсомольский, Калмыкия", "Chernye Zemli Nature Reserve", "Kalmykia", 45.3331863, 46.0422631,),
    official_site="https://zapovednik-chernyezemli.ru/",
))

# 6) Парк «Дружба» (Элиста) ----------------------------------------------------------
RECORDS.append(rec(
    "druzhba-park-elista",
    "Công viên Druzhba (Hữu Nghị), Elista",
    "Парк «Дружба»",
    "Druzhba (Friendship) Park",
    ["park_garden"],
    46.307122, 44.263228,
    "Phố Lenin 220v, trung tâm thành phố Elista, Cộng hoà Kalmykia, Nga.",
    "Công viên Druzhba là lá phổi xanh và không gian dạo chơi lâu đời nhất Elista (từ 1937), nằm ngay trung tâm dọc phố Lenin. Trong công viên có nhiều tác phẩm điêu khắc dân tộc, đài tưởng niệm chiến tranh và các khu vui chơi.",
    "Ra đời từ năm 1937, Druzhba ('Hữu Nghị') là công viên văn hoá - nghỉ ngơi trung tâm và lâu đời nhất của Elista, trải dài dọc phố Lenin ngay tim thành phố. Đây là nơi người dân thủ phủ dạo bộ, đưa trẻ vui chơi và tổ chức lễ hội, hoà quyện bóng cây xanh mát hiếm hoi giữa thảo nguyên khô hạn với không gian đô thị. Công viên là một 'bảo tàng ngoài trời' thu nhỏ của văn hoá Kalmykia: rải rác trong khuôn viên là các tác phẩm điêu khắc dân tộc và biểu tượng tâm linh (trong đó có tượng 'Bạch Lão' Tsagan Aav nổi tiếng gần lối vào), khu vui chơi, sân khấu và đài tưởng niệm các anh hùng Nội chiến và Vệ quốc với Ngọn lửa Vĩnh cửu. Với vị trí trung tâm, Druzhba là điểm khởi đầu lý tưởng để khám phá Elista - gần quảng trường Lenin, Pagoda Bảy Ngày và các tuyến phố chính.",
    [
        "Công viên trung tâm lâu đời nhất Elista (từ 1937), lá phổi xanh giữa thảo nguyên.",
        "Nhiều tác phẩm điêu khắc dân tộc và biểu tượng tâm linh Kalmykia trong khuôn viên.",
        "Vị trí trung tâm, sát quảng trường Lenin và Pagoda Bảy Ngày.",
    ],
    {
        "hours_vi": "Công viên mở cửa tự do; khu trò chơi thường hoạt động ban ngày đến tối.",
        "ticket_vi": "Vào công viên miễn phí; một số trò chơi/dịch vụ thu phí riêng.",
        "duration_vi": "Khoảng 45–90 phút dạo chơi.",
        "best_time_vi": "Chiều mát và buổi tối; đẹp vào các dịp lễ hội thành phố.",
        "tips_vi": "Kết hợp tham quan quảng trường Lenin và Pagoda Bảy Ngày gần đó; mùa hè nên đi lúc chiều muộn cho mát.",
    },
    [
        {"title": "Ruwiki — Дружба (парк, Элиста)", "url": "https://ru.ruwiki.ru/wiki/Дружба_(парк,_Элиста)"},
        {"title": "Официальный сайт парка «Дружба»", "url": "https://druzhba08.ru/about-the-park/"},
    ],
    ["park", "city-park", "elista", "sculptures", "recreation"],
    maps_text("Парк Дружба", "Элиста", "Druzhba Park", "Elista", 46.307122, 44.263228),
))

# 7) Чограйское водохранилище -------------------------------------------------------
RECORDS.append(rec(
    "chograyskoye-reservoir",
    "Hồ chứa Chograyskoye",
    "Чограйское водохранилище",
    "Chograyskoye Reservoir",
    ["park_garden"],
    45.5319587, 44.4136828,
    "Trên sông Vostochny Manych, quận Iki-Burul (ranh giới Kalmykia - vùng Stavropol), Nga.",
    "Chograyskoye là hồ chứa lớn trên sông Vostochny Manych ở tây nam Kalmykia, nổi tiếng là thiên đường chim nước và điểm câu cá. Vùng bờ lau sậy rộng lớn thu hút bồ nông, thiên nga và vô số loài chim di cư.",
    "Nằm trên sông Vostochny Manych ở quận Iki-Burul, nơi giáp ranh Kalmykia và vùng Stavropol, Chograyskoye là hồ chứa nhân tạo lớn được xây trong hệ thống tưới tiêu thảo nguyên. Mặt nước rộng cùng những dải lau sậy và bãi lầy ven bờ đã biến hồ thành một trong những điểm tập trung chim nước quan trọng của vùng: bồ nông hồng và bồ nông xoăn, thiên nga, các loài vịt, diệc, mòng biển... về đây kiếm ăn, làm tổ và dừng chân khi di cư. Đây cũng là điểm câu cá được ưa chuộng (cá chép, cá măng, cá trắm...) và là nơi ngắm hoàng hôn thảo nguyên mênh mông. Với giới yêu thiên nhiên và nhiếp ảnh chim, Chograyskoye là một điểm dừng hấp dẫn khi khám phá miền tây nam Kalmykia, gần các khu bảo tồn và tuyến thảo nguyên.",
    [
        "Hồ chứa lớn trên sông Vostochny Manych, điểm tập trung chim nước quan trọng.",
        "Bồ nông, thiên nga, diệc và nhiều loài chim di cư tụ về vùng lau sậy ven bờ.",
        "Điểm câu cá và ngắm hoàng hôn thảo nguyên nổi tiếng.",
    ],
    steppe_practical(
        "Vài giờ đến nửa ngày (ngắm chim, câu cá).",
        "Mùa xuân và thu (mùa chim di cư) là lý tưởng.",
        "Mang ống nhòm, đồ câu nếu cần; ít dịch vụ tại chỗ nên tự chuẩn bị nước, đồ ăn; chú ý an toàn ven bờ lầy.",
    ),
    [
        {"title": "OpenStreetMap — Чограйское водохранилище", "url": "https://www.openstreetmap.org/relation/4032976"},
        {"title": "Wikipedia (RU) — Чограйское водохранилище", "url": "https://ru.wikipedia.org/wiki/Чограйское_водохранилище"},
    ],
    ["reservoir", "birdwatching", "fishing", "nature", "iki-burul"],
    maps_text("Чограйское водохранилище", "Ики-Бурульский район", "Chograyskoye Reservoir", "Kalmykia", 45.5319587, 44.4136828),
))

# ============================ CÔNG TRÌNH TÔN GIÁO (church) ============================

# 8) Лаганский хурул -----------------------------------------------------------------
RECORDS.append(rec(
    "lagan-khurul",
    "Chùa Lagan (Lagan Dargyeling Khurul) và tượng Phật Di Lặc",
    "Лаганский хурул (Лагань Даргьелинг)",
    "Lagan Khurul (Lagan Dargyeling)",
    ["church"],
    45.4062449, 47.3412538,
    "Phố Avtomobilistov, khu bắc thành phố Lagan, quận Lagansky, Cộng hoà Kalmykia, Nga.",
    "Chùa Lagan là ngôi chùa Phật giáo lớn ở Lagan - thành phố thứ hai của Kalmykia gần bờ Caspi. Khánh thành năm 1995 với sự bảo trợ của Đức Đạt Lai Lạt Ma; năm 2019 khu chùa dựng thêm tượng Phật Di Lặc được xem là lớn nhất châu Âu.",
    "Ở thành phố cảng Lagan gần bờ biển Caspi - đô thị lớn thứ hai của Kalmykia - ngôi chùa Lagan (Lagan Dargyeling Khurul) là trung tâm Phật giáo quan trọng của cả vùng đông nam nước cộng hoà. Chùa khánh thành ngày 27/5/1995; Đức Đạt Lai Lạt Ma thứ 14 trong chuyến thăm Kalmykia năm 1992 đã đóng góp tịnh tài, làm lễ gia trì và tặng chùa một bức thangka hình Phật Thích Ca cùng dấu bàn tay của Ngài. Về sau, quần thể được mở rộng với ngôi chùa mới và các bảo tháp, tạo thành một tổ hợp kiến trúc Phật giáo bề thế giữa đô thị thảo nguyên - ven biển. Điểm nhấn đặc biệt là pho tượng Phật Di Lặc (Maitreya) cao 13,5 m khánh thành năm 2019, được giới thiệu là tượng Di Lặc lớn nhất châu Âu. Với người dân Lagan và Phật tử khắp vùng, đây là nơi hành lễ, cầu an và là niềm tự hào kiến trúc - tâm linh của thành phố.",
    [
        "Chùa Phật giáo lớn ở Lagan, khánh thành 1995 dưới sự bảo trợ của Đức Đạt Lai Lạt Ma.",
        "Tượng Phật Di Lặc cao 13,5 m (2019) - được xem là tượng Di Lặc lớn nhất châu Âu.",
        "Tổ hợp chùa và bảo tháp giữa thành phố cảng gần biển Caspi.",
    ],
    {
        "hours_vi": "Mở cửa hàng ngày, thường ban ngày (khoảng 9:00–18:00); giờ có thể đổi theo lịch lễ.",
        "ticket_vi": "Miễn phí vào cửa; chùa nhận công đức tuỳ tâm.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm; dịp lễ Phật giáo (Zul, Tsagan Sar) có nghi lễ đặc sắc.",
        "tips_vi": "Ăn mặc kín đáo, bỏ giày khi vào chính điện; đi vòng quanh chùa và bảo tháp theo chiều kim đồng hồ; kết hợp tham quan bờ biển Caspi gần Lagan.",
    },
    [
        {"title": "Буддизм в Калмыкии — Лаганский хурул", "url": "http://khurul.ru/2009/01/laganskij-xurul/"},
        {"title": "LowVolga — Лаганский хурул и статуя Будды Майтрейи", "url": "https://www.lowvolga.ru/object/laganskij-hurul-i-samaja-bolshaja-v-evrope-statuja-buddy-majtreji/"},
    ],
    ["buddhist", "temple", "khurul", "lagan", "maitreya", "caspian"],
    maps_text("Лаганский хурул", "Лагань", "Lagan Khurul", "Lagan, Kalmykia", 45.4062449, 47.3412538),
))

# 9) Цаган-Аманский хурул -----------------------------------------------------------
RECORDS.append(rec(
    "tsagan-aman-khurul",
    "Chùa Tsagan-Aman (Tsagan-Amansky Khurul)",
    "Цаган-Аманский хурул",
    "Tsagan-Aman Khurul",
    ["church"],
    47.5447479, 46.7341932,
    "Phố Togmed-Gavdzhi 24, thị trấn Tsagan-Aman, quận Yustinsky, Cộng hoà Kalmykia, Nga.",
    "Chùa Tsagan-Aman là ngôi chùa Phật giáo ở thị trấn Tsagan-Aman - điểm duy nhất Kalmykia chạm tới sông Volga, nơi cực bắc của vùng. Chùa được phục dựng cạnh nhà của lama Tugmyud-gavdzhi, tiếp nối truyền thống có từ thế kỷ 18.",
    "Tsagan-Aman ('Bờ Trắng') nằm bên hữu ngạn cao của sông Volga, là khu dân cư duy nhất của Kalmykia vươn tới dòng Volga, cách Elista khoảng 300 km về phía đông bắc, sát biên giới tỉnh Astrakhan - và cũng là điểm cực bắc trên hành trình khám phá vùng. Ngôi chùa đầu tiên ở vùng đất Tsagan-Aman đã có từ năm 1798 nhưng bị phá huỷ những năm đầu Xô Viết. Đầu thập niên 1990, chùa được phục dựng ngay cạnh ngôi nhà nơi lama Tugmyud-gavdzhi (1887–1980) - một bậc thầy Phật học từng tu học nhiều năm ở Nội Mông - sinh sống và hành lễ. Chùa được dựng theo đúng truyền thống kiến trúc Phật giáo (kiến trúc sư V. Gilyandikov) với tôn tượng Phật Thích Ca cao hơn 2 m bên trong. Nằm ở một góc xa xôi bên bờ Volga, chùa Tsagan-Aman mang không khí trầm mặc, là trung tâm tâm linh của cộng đồng Phật tử vùng đông bắc và điểm dừng đáng nhớ cho ai muốn tới nơi Kalmykia gặp sông Volga.",
    [
        "Chùa Phật giáo ở Tsagan-Aman - nơi duy nhất Kalmykia chạm tới sông Volga.",
        "Phục dựng cạnh nhà của lama Tugmyud-gavdzhi, tiếp nối truyền thống từ năm 1798.",
        "Tôn tượng Phật Thích Ca cao hơn 2 m; không khí trầm mặc bên bờ Volga.",
    ],
    {
        "hours_vi": "Mở cửa hàng ngày, thường ban ngày; giờ có thể thay đổi theo lịch lễ.",
        "ticket_vi": "Miễn phí vào cửa; chùa nhận công đức tuỳ tâm.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; dịp lễ Phật giáo có nghi lễ đặc sắc.",
        "tips_vi": "Ở rất xa Elista (khoảng 300 km), nên đi khi kết hợp tuyến đông bắc/qua Volga; ăn mặc kín đáo, bỏ giày khi vào chính điện.",
    },
    [
        {"title": "Туристер.Ру — Цаган-Аманский хурул", "url": "https://www.tourister.ru/world/europe/russia/city/cagan-aman/temples/41565"},
        {"title": "OpenStreetMap — Цаган-Аманский хурул", "url": "https://www.openstreetmap.org/node/2864971390"},
    ],
    ["buddhist", "temple", "khurul", "tsagan-aman", "volga", "yustinsky"],
    maps_org("https://yandex.ru/maps/org/khurul/172314426181/", "Tsagan-Aman Khurul", "Tsagan-Aman, Kalmykia"),
))

# 10) Ступа Просветления (Элиста) ---------------------------------------------------
RECORDS.append(rec(
    "stupa-enlightenment-elista",
    "Bảo tháp Giác Ngộ (Stupa Prosvetleniya), Elista",
    "Ступа Просветления",
    "Stupa of Enlightenment",
    ["church"],
    46.3010, 44.3011,
    "Đại lộ Pyotr Anatsky 7A, thành phố Elista, Cộng hoà Kalmykia, Nga.",
    "Bảo tháp Giác Ngộ cao 11 m là một trong những bảo tháp Phật giáo tiêu biểu của Elista, dựng năm 1999. Bên trong tôn trí bàn thờ và bánh xe cầu nguyện chứa hàng nghìn câu chú cùng nhiều thánh vật.",
    "Được xây dựng năm 1999 theo thiết kế của các kiến trúc sư V. Kosovsky và V. Gilyandikov, Bảo tháp Giác Ngộ (Stupa Prosvetleniya) cao 11 m là một trong những bảo tháp Phật giáo nổi bật của thủ phủ Elista. Trong truyền thống Phật giáo Tây Tạng - Kalmykia, bảo tháp Giác Ngộ tượng trưng cho sự chiến thắng chướng ngại, cho mục tiêu giác ngộ và giải thoát tâm trí. Bên trong tháp có bàn thờ và một bánh xe cầu nguyện 'kюрде' chứa hàng nghìn câu chú (mantra), cùng đất từ nơi Đức Phật đản sinh và nhiều thánh vật khác. Bảo tháp nằm trong khuôn viên một trung tâm Phật giáo theo truyền thống Kim Cương thừa Karma Kagyu, cạnh một ngôi chùa nhỏ - tạo thành một điểm chiêm bái yên tĩnh giữa lòng thành phố. Với du khách, đây là nơi tìm hiểu ý nghĩa biểu tượng của kiến trúc bảo tháp và thực hành nghi thức đi nhiễu (đi vòng quanh tháp theo chiều kim đồng hồ).",
    [
        "Bảo tháp Phật giáo cao 11 m (1999), biểu tượng của sự giác ngộ và vượt chướng ngại.",
        "Bên trong có bánh xe cầu nguyện chứa hàng nghìn câu chú và nhiều thánh vật.",
        "Thuộc trung tâm Phật giáo Kim Cương thừa Karma Kagyu, không gian chiêm bái yên tĩnh.",
    ],
    {
        "hours_vi": "Khu bảo tháp ngoài trời, chiêm bái ban ngày; chùa cạnh bên mở theo giờ riêng.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; buổi sáng và chiều mát dễ chịu.",
        "tips_vi": "Đi nhiễu quanh bảo tháp theo chiều kim đồng hồ và quay bánh xe cầu nguyện; ăn mặc kín đáo, giữ yên tĩnh.",
    },
    [
        {"title": "Tonkosti — Ступа Просветления в Элисте", "url": "https://tonkosti.ru/Ступа_Просветления_в_Элисте"},
        {"title": "AutoTravel — Ступа Просветления (Элиста)", "url": "https://autotravel.ru/otklik.php/20237"},
    ],
    ["buddhist", "stupa", "elista", "karma-kagyu", "spiritual"],
    maps_text("Ступа Просветления", "Элиста", "Stupa of Enlightenment", "Elista", 46.3010, 44.3011),
))

# 11) Казанский кафедральный собор (Элиста) -----------------------------------------
RECORDS.append(rec(
    "kazan-cathedral-elista",
    "Nhà thờ Chính thống giáo Kazan (Elista)",
    "Казанский кафедральный собор",
    "Kazan Cathedral (Elista)",
    ["church"],
    46.3087, 44.2318,
    "Khu Nam thành phố Elista, Cộng hoà Kalmykia, Nga.",
    "Nhà thờ Kazan là thánh đường Chính thống giáo lớn nhất Kalmykia, trung tâm của giáo phận Elista. Xây năm 1996, kiến trúc baroque muộn với mái vòm bát giác - điểm nhấn Kitô giáo giữa một nước cộng hoà Phật giáo.",
    "Giữa Elista - thủ phủ của nước cộng hoà Phật giáo duy nhất châu Âu - Nhà thờ Kazan (Собор Казанской иконы Божией Матери) là thánh đường Chính thống giáo lớn nhất và là nhà thờ chính toà của giáo phận Elista - Kalmykia thuộc Giáo hội Chính thống Nga. Được xây dựng năm 1996 và cung hiến ngày 7/6/1997 bởi Thượng phụ Aleksey II, nhà thờ mang phong cách baroque muộn: một khối kiến trúc bát giác một vòm với phần rotonda phía trên, đỉnh gắn thánh giá. Nhà thờ nằm trong một quần thể của giáo phận (gồm toà nhà hành chính và nhà thờ Thánh Giá), phục vụ cộng đồng tín hữu Chính thống - chủ yếu là người Nga và các sắc dân khác sống tại Kalmykia. Sự hiện diện của ngôi thánh đường bên cạnh các khurul và bảo tháp Phật giáo cho thấy bức tranh đa tôn giáo hoà hợp đặc trưng của vùng đất thảo nguyên này, và là một điểm tham quan kiến trúc - tâm linh đáng chú ý ở Elista.",
    [
        "Thánh đường Chính thống giáo lớn nhất Kalmykia, nhà thờ chính toà của giáo phận Elista.",
        "Kiến trúc baroque muộn, khối bát giác một vòm, cung hiến năm 1997.",
        "Điểm nhấn Kitô giáo trong bức tranh đa tôn giáo hoà hợp của vùng Phật giáo.",
    ],
    {
        "hours_vi": "Mở cửa hàng ngày theo giờ lễ (thường sáng sớm đến tối); có thánh lễ cuối tuần.",
        "ticket_vi": "Miễn phí vào cửa; nhận công đức tuỳ tâm.",
        "duration_vi": "Khoảng 30 phút.",
        "best_time_vi": "Quanh năm; dịp lễ lớn Chính thống giáo đông tín hữu.",
        "tips_vi": "Ăn mặc kín đáo; nữ nên mang khăn trùm đầu khi vào; giữ yên tĩnh, xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Wikipedia (RU) — Казанский собор (Элиста)", "url": "https://ru.wikipedia.org/wiki/Казанский_собор_(Элиста)"},
        {"title": "Казанский кафедральный собор города Элисты — епархия", "url": "https://sobor-elista.prihod.ru/"},
    ],
    ["orthodox", "cathedral", "elista", "christian", "architecture"],
    maps_text("Казанский кафедральный собор", "Элиста", "Kazan Cathedral", "Elista", 46.3087, 44.2318),
))

# 12) Чёёря-хурул (Ики-Чонос) --------------------------------------------------------
RECORDS.append(rec(
    "cheorya-khurul",
    "Chùa cổ Cheorya (Chёёря-khurul), Iki-Chonos",
    "Чёёря-хурул",
    "Cheorya Khurul",
    ["church"],
    46.4246450, 44.4689497,
    "Ngõ Sandzhiev, làng Iki-Chonos, quận Tselinny, Cộng hoà Kalmykia, Nga.",
    "Cheorya-khurul ở làng Iki-Chonos là một trong những chùa Phật giáo giàu lịch sử nhất Kalmykia. Chùa gốc dựng năm 1903, từng có trường Phật học Tsannid Choira danh tiếng và là nơi đặt residence của Shajin-lama - lãnh tụ Phật giáo Kalmykia.",
    "Ở làng Iki-Chonos thuộc quận Tselinny, Cheorya-khurul (Chёёря-хурул) là một trong những ngôi chùa có bề dày lịch sử nhất của Phật giáo Kalmykia. Ngôi chùa đầu tiên dựng đầu năm 1903, sức chứa tới hai nghìn tín đồ; vị lama đầu tiên chính là nhà khai sáng, nhà thơ Boovan Badma. Năm 1913, chùa mở trường Phật học Tsannid Choira - nơi tăng sĩ nghiên cứu triết học và nghi quỹ Phật giáo; từ năm 1920, chùa còn là nơi đặt residence của Shajin-lama, vị lãnh tụ tinh thần của người Kalmykia. Sau khi bị phá huỷ thời Xô Viết, Cheorya-khurul được phục dựng và khánh thành ngày 6/7/1997 - đúng ngày sinh của Đức Đạt Lai Lạt Ma thứ 14. Toà chùa hai tầng với mái ba lớp 'bay' lợp ngói ánh vàng vươn lên thanh thoát giữa nền thảo nguyên. Trước chùa đặt các bánh xe cầu nguyện (kюрде) mà khách hành hương quay theo chiều kim đồng hồ trước khi vào lễ. Đây là điểm hành hương giàu ý nghĩa lịch sử, gắn với thời hoàng kim của Phật học Kalmykia.",
    [
        "Chùa lịch sử: bản gốc dựng 1903, sức chứa tới 2.000 tín đồ, lama đầu tiên là nhà thơ Boovan Badma.",
        "Từng có trường Phật học Tsannid Choira và là nơi đặt residence của Shajin-lama Kalmykia.",
        "Phục dựng năm 1997; kiến trúc hai tầng, mái ba lớp lợp ngói ánh vàng giữa thảo nguyên.",
    ],
    {
        "hours_vi": "Mở cửa ban ngày; giờ có thể thay đổi theo lịch lễ và mùa.",
        "ticket_vi": "Miễn phí vào cửa; nhận công đức tuỳ tâm.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; dịp lễ Phật giáo có nghi lễ đặc sắc.",
        "tips_vi": "Nằm ở làng nhỏ ngoài Elista, nên đi bằng xe riêng/tour; ăn mặc kín đáo, quay các bánh xe cầu nguyện theo chiều kim đồng hồ.",
    },
    [
        {"title": "Wikipedia (RU) — Чёёря-хурул", "url": "https://ru.wikipedia.org/wiki/Чёёря-хурул"},
        {"title": "Таинственная Калмыкия — Хурул на земле Ики-Чонос", "url": "https://www.kalmykiatour.com/sights/khurul-iki-chonos/"},
    ],
    ["buddhist", "temple", "khurul", "historic", "iki-chonos", "tsannid-choira"],
    maps_text("Чёёря-хурул", "Ики-Чонос, Калмыкия", "Cheorya Khurul", "Iki-Chonos, Kalmykia", 46.4246450, 44.4689497),
))

# 13) Троицкий хурул «Оргьен Сангак Чойлинг» ----------------------------------------
RECORDS.append(rec(
    "troitsky-khurul",
    "Chùa Troitskoye (Orgyen Sangak Choling) - chùa Nyingma duy nhất ở Nga",
    "Троицкий хурул «Оргьен Сангак Чойлинг»",
    "Troitsky Khurul (Orgyen Sangak Choling)",
    ["church"],
    46.4212609, 44.2589751,
    "Làng Troitskoye, quận Tselinny, Cộng hoà Kalmykia, Nga.",
    "Chùa ở làng Troitskoye (Orgyen Sangak Choling) là ngôi chùa Phật giáo duy nhất ở Nga thuộc phái Nyingma (dòng Ripa) - trường phái cổ xưa nhất của Phật giáo Tây Tạng. Chùa được xây và cung hiến năm 2015, cạnh có một bảo tháp.",
    "Tại Troitskoye - làng thủ phủ quận Tselinny gần Elista - có một ngôi chùa Phật giáo độc đáo: Orgyen Sangak Choling, được xem là chùa duy nhất ở Nga thuộc phái Nyingma (cụ thể là dòng truyền thừa Ripa) - trường phái 'cổ mật' lâu đời nhất trong Phật giáo Tây Tạng. Tên Tây Tạng của chùa mang nghĩa gần với 'Uddiyana - nơi hoằng dương Mật chú thừa'. Chùa được xây dựng và cung hiến năm 2015, bên cạnh có một bảo tháp (stupa), nằm gần một quần thể tưởng niệm trong làng. Trong bức tranh Phật giáo Kalmykia vốn chủ yếu theo phái Gelug (Cách-lỗ), sự hiện diện của một ngôi chùa Nyingma khiến Troitskoye trở thành một điểm đến đặc biệt với người quan tâm tới các dòng truyền thừa Tây Tạng. Kết hợp với chùa cổ Syakusn-Syume gần đó (đã có trong cẩm nang), khu vực Troitskoye là một mảnh ghép thú vị của bản đồ Phật giáo vùng thảo nguyên.",
    [
        "Chùa Phật giáo duy nhất ở Nga thuộc phái Nyingma (dòng Ripa) - trường phái cổ xưa nhất của Phật giáo Tây Tạng.",
        "Tên Tây Tạng nghĩa gần với 'Uddiyana - nơi hoằng dương Mật chú thừa'; xây và cung hiến năm 2015.",
        "Có bảo tháp bên cạnh; nằm ở làng thủ phủ quận Tselinny gần Elista.",
    ],
    {
        "hours_vi": "Mở cửa ban ngày; giờ có thể thay đổi theo lịch lễ.",
        "ticket_vi": "Miễn phí vào cửa; nhận công đức tuỳ tâm.",
        "duration_vi": "Khoảng 30 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; dịp lễ Phật giáo có nghi lễ đặc sắc.",
        "tips_vi": "Đi bằng xe riêng/tour từ Elista; ăn mặc kín đáo, giữ yên tĩnh; có thể kết hợp thăm chùa cổ Syakusn-Syume gần khu vực.",
    },
    [
        {"title": "Wikipedia (RU) — Троицкий хурул", "url": "https://ru.wikipedia.org/wiki/Троицкий_хурул"},
        {"title": "VATravel — Хурул Оргьен Сангак Чойлинг", "url": "https://vatravel.ru/xurul-orgen-sangak-chojling/"},
    ],
    ["buddhist", "temple", "khurul", "nyingma", "troitskoye", "tselinny"],
    maps_text("Троицкий хурул", "Троицкое, Калмыкия", "Troitsky Khurul", "Troitskoye, Kalmykia", 46.4212609, 44.2589751),
))

# 14) Хурул в Яшалте ----------------------------------------------------------------
RECORDS.append(rec(
    "yashalta-khurul",
    "Chùa Yashalta (khurul làng Yashalta)",
    "Хурул в Яшалте",
    "Yashalta Khurul",
    ["church"],
    46.3388587, 42.2671662,
    "Ngõ Kommunalny, làng Yashalta, quận Yashalta, phía tây Cộng hoà Kalmykia, Nga.",
    "Chùa Yashalta là ngôi khurul phục vụ cộng đồng Phật tử ở Yashalta - làng thủ phủ quận cực tây Kalmykia. Ngôi chùa nhỏ giữa vùng nông nghiệp và hồ muối là minh chứng cho sự hồi sinh của Phật giáo Kalmykia thời hậu Xô Viết.",
    "Yashalta là làng thủ phủ của quận cùng tên ở cực tây Kalmykia, vùng đất trù phú với nông nghiệp và hồ muối Bolshoye Yashaltinskoye nổi tiếng. Như hầu hết các trung tâm quận của nước cộng hoà Phật giáo này, Yashalta có một ngôi khurul (chùa) phục vụ đời sống tâm linh của cộng đồng địa phương. Được dựng trong làn sóng phục hưng Phật giáo Kalmykia sau thời Xô Viết, ngôi chùa tuy khiêm tốn về quy mô nhưng giữ vai trò quan trọng: nơi tăng sĩ hành lễ, người dân cầu an, tổ chức các nghi lễ theo lịch Phật giáo Tây Tạng (Zul, Tsagan Sar...) và gìn giữ bản sắc Oirat - Kalmykia ở vùng biên tây. Với du khách trên tuyến phía tây (kết hợp hồ muối Yashalta và hồ Manych-Gudilo), ngôi chùa là một điểm dừng nhỏ để cảm nhận nhịp sống tôn giáo bình dị của thảo nguyên.",
    [
        "Chùa Phật giáo (khurul) ở làng thủ phủ quận Yashalta, cực tây Kalmykia.",
        "Biểu tượng cho sự phục hưng Phật giáo Kalmykia thời hậu Xô Viết.",
        "Điểm dừng tâm linh trên tuyến phía tây, gần hồ muối Yashalta và hồ Manych-Gudilo.",
    ],
    {
        "hours_vi": "Mở cửa ban ngày; giờ tuỳ theo lịch lễ và sinh hoạt của chùa.",
        "ticket_vi": "Miễn phí vào cửa; nhận công đức tuỳ tâm.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; dịp lễ Phật giáo có nghi lễ đặc sắc.",
        "tips_vi": "Kết hợp tham quan hồ muối Yashalta; ăn mặc kín đáo, giữ yên tĩnh, hỏi ý trước khi chụp ảnh nghi lễ.",
    },
    [
        {"title": "OpenStreetMap — Хурул, Яшалта", "url": "https://www.openstreetmap.org/node/9418837659"},
        {"title": "Wikipedia (RU) — Яшалта", "url": "https://ru.wikipedia.org/wiki/Яшалта"},
    ],
    ["buddhist", "temple", "khurul", "yashalta", "steppe"],
    maps_text("Хурул", "Яшалта, Калмыкия", "Yashalta Khurul", "Yashalta, Kalmykia", 46.3388587, 42.2671662),
))

# ============================ TƯỢNG ĐÀI / ĐIÊU KHẮC (monument) ============================

# 15) Золотой всадник ---------------------------------------------------------------
RECORDS.append(rec(
    "golden-horseman-elista",
    "Kỵ Sĩ Vàng (Zolotoy Vsadnik)",
    "Золотой всадник",
    "The Golden Horseman",
    ["monument"],
    46.318135, 44.258273,
    "Cửa ngõ vào Elista, vi khu 1, giao phố Dzhangar và Budyonny, Cộng hoà Kalmykia, Nga.",
    "Kỵ Sĩ Vàng là tượng đài dát vàng cao 8 m trên cột bia 15 m ở cửa ngõ Elista, khắc hoạ người anh hùng trong sử thi Kalmykia 'Dzhangar'. Bức tượng như 'bay' trên trời cao, canh giữ 'viên ngọc thảo nguyên' Elista.",
    "Đứng sừng sững ở cửa ngõ phía tây bắc Elista (vi khu 1, chỗ giao phố Dzhangar và Budyonny), 'Kỵ Sĩ Vàng' (Zolotoy Vsadnik) là một trong những biểu tượng ấn tượng nhất của thủ phủ Kalmykia. Tác phẩm của nhà điêu khắc Nikolai Mozhaev (Rostov), khánh thành ngày 1/5/2007, khắc hoạ một dũng sĩ trong sử thi anh hùng 'Dzhangar' - thiên trường ca huyền thoại về xứ Bumba lý tưởng của người Kalmykia. Bức tượng cao 8 m dát vàng lá, đặt trên một cột bia (stele) cao 15 m dựng trên gò nhân tạo, khiến kỵ sĩ như đang 'bay' giữa bầu trời thảo nguyên. Tay phải chàng cầm ngọn cờ, tay trái cầm cây cung kiểu Mông Cổ; theo ý tưởng của các tác giả, người kỵ sĩ đang canh giữ và che chở cho 'viên ngọc thảo nguyên' Elista cùng cư dân. Đây là điểm chào đón du khách và là một trong những địa điểm chụp ảnh biểu tượng nhất khi tới Kalmykia.",
    [
        "Tượng dát vàng cao 8 m trên cột bia 15 m, khắc hoạ anh hùng sử thi 'Dzhangar'.",
        "Đặt trên gò nhân tạo ở cửa ngõ Elista, kỵ sĩ như 'bay' giữa trời thảo nguyên.",
        "Khánh thành 2007 (điêu khắc gia N. Mozhaev), biểu tượng chào đón của thủ phủ.",
    ],
    {
        "hours_vi": "Tượng đài ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–20 phút.",
        "best_time_vi": "Quanh năm; đẹp khi nắng làm lớp vàng lá rực sáng và lúc hoàng hôn.",
        "tips_vi": "Nằm ở cửa ngõ thành phố cạnh đường lớn, chú ý an toàn giao thông khi dừng chụp ảnh.",
    },
    [
        {"title": "Wikipedia (RU) — Золотой всадник (Элиста)", "url": "https://ru.wikipedia.org/wiki/Золотой_всадник_(Элиста)"},
        {"title": "БольшаяСтрана — Элиста", "url": "https://bolshayastrana.com/blog/ehlista-527"},
    ],
    ["monument", "elista", "dzhangar", "epic", "landmark", "gilded"],
    maps_text("Золотой всадник", "Элиста", "The Golden Horseman", "Elista", 46.318135, 44.258273),
))

# 16) Памятник Остапу Бендеру -------------------------------------------------------
RECORDS.append(rec(
    "ostap-bender-monument",
    "Tượng Ostap Bender",
    "Памятник Остапу Бендеру",
    "Monument to Ostap Bender",
    ["monument"],
    46.3037, 44.3036,
    "Đại lộ Ostap Bender, giữa các vi khu 6-7-8, trên đường tới Chess City, Elista, Cộng hoà Kalmykia, Nga.",
    "Tượng Ostap Bender ở Elista tôn vinh nhân vật văn học lừng danh của Ilf và Petrov - kẻ mơ biến làng Vasyuki thành 'thủ đô cờ vua thế giới'. Quanh tượng xếp bán nguyệt '12 chiếc ghế' đúng như tên tiểu thuyết trứ danh.",
    "Trên đại lộ mang tên chính nhân vật, trên đường dẫn tới khu Chess City (Thành phố Cờ Vua), tượng Ostap Bender là một trong những điểm chụp ảnh vui nhộn và giàu 'chất văn học' nhất Elista. Ostap Bender là nhân vật hài hước trứ danh trong hai tiểu thuyết châm biếm của Ilf và Petrov ('Mười hai chiếc ghế' và 'Con bê vàng'); trong 'Mười hai chiếc ghế', gã 'đại chiến lược gia' từng mơ biến ngôi làng Vasyuki tỉnh lẻ thành 'New Vasyuki' - kinh đô cờ vua thế giới. Chính giấc mơ đó đã trở thành hiện thực đầy trớ trêu tại Elista khi thành phố xây Chess City và đăng cai các sự kiện cờ vua quốc tế. Bức tượng dựng năm 1999, và quanh nó xếp thành hình bán nguyệt là 12 chiếc ghế cùng những chiếc bàn - lời nhắc tinh nghịch tới nhan đề cuốn tiểu thuyết. Đây là nơi du khách thích ngồi lên ghế chụp ảnh và tìm hiểu mối duyên đặc biệt giữa Elista và môn cờ vua.",
    [
        "Tượng nhân vật văn học Ostap Bender - kẻ mơ biến Vasyuki thành 'thủ đô cờ vua thế giới'.",
        "Quanh tượng xếp bán nguyệt '12 chiếc ghế' theo tên tiểu thuyết của Ilf và Petrov.",
        "Trên đường tới Chess City, gắn với danh tiếng cờ vua của Elista.",
    ],
    {
        "hours_vi": "Tượng ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15 phút.",
        "best_time_vi": "Quanh năm; ban ngày thuận cho chụp ảnh.",
        "tips_vi": "Ngồi lên một trong '12 chiếc ghế' để chụp ảnh; kết hợp tham quan Chess City gần đó.",
    },
    [
        {"title": "Таинственная Калмыкия — Памятник Остапу Бендеру", "url": "https://www.kalmykiatour.com/sights/ostap-bender/"},
        {"title": "Яндекс Карты — Остап Бендер (жанровая скульптура)", "url": "https://yandex.ru/maps/org/ostap_bender/91810365661/"},
    ],
    ["monument", "elista", "ostap-bender", "chess", "literature", "photo-spot"],
    maps_org("https://yandex.ru/maps/org/ostap_bender/91810365661/", "Monument to Ostap Bender", "Elista"),
))

# 17) Мемориал «Исход и Возвращение» ------------------------------------------------
RECORDS.append(rec(
    "exodus-return-memorial",
    "Đài tưởng niệm 'Ra Đi và Trở Về' (Iskhod i Vozvrashcheniye)",
    "Памятник «Исход и Возвращение»",
    "Exodus and Return Memorial",
    ["monument"],
    46.30056, 44.31472,
    "Phía đông thành phố Elista, Cộng hoà Kalmykia, Nga.",
    "'Ra Đi và Trở Về' là đài tưởng niệm nạn trục xuất người Kalmykia đi Siberia năm 1943, tác phẩm của nhà điêu khắc lừng danh Ernst Neizvestny. Cụm tượng đặt trên gò đất, dưới chân có toa tàu chở người đi đày và đường ray tưởng niệm.",
    "Ở phía đông Elista, đài tưởng niệm 'Ra Đi và Trở Về' (Iskhod i Vozvrashcheniye) là một trong những tượng đài xúc động nhất của Kalmykia, tưởng niệm cuộc trục xuất bi thảm toàn dân tộc Kalmykia tới Siberia năm 1943 và các nạn nhân của đàn áp Stalin. Tác giả là Ernst Neizvestny - nhà điêu khắc gốc Nga nổi tiếng thế giới; tượng được đúc đồng tại New York và khánh thành ngày 29/12/1996. Bản thân tượng đặt trên đỉnh một gò đất nhân tạo; lối lên là con đường xoắn ốc đi theo chiều kim đồng hồ, phỏng theo nghi thức đi nhiễu quanh chùa (khurul). Dưới chân gò là một toa tàu hàng đặt trên đường ray - biểu tượng cho những toa tàu chở người Kalmykia đi đày; dọc ray có 14 cột đá granite, tượng trưng cho 14 năm lưu đày (1943–1957). Trên khối tượng là vô số hình tượng ẩn dụ: con ngựa (dòng chảy thời gian), con cừu khóc thương đứa trẻ (sự nhẫn nhịn), hoa sen chứa phôi thai (sự tái sinh - trở về), gươm giáo (bạo lực)... Mỗi năm vào ngày 28/12, người dân tới đây tưởng niệm nạn nhân của cuộc trục xuất.",
    [
        "Đài tưởng niệm cuộc trục xuất người Kalmykia đi Siberia (1943) - tác phẩm của Ernst Neizvestny.",
        "Đúc đồng tại New York, khánh thành 1996; lối lên xoắn ốc phỏng theo nghi thức đi nhiễu quanh chùa.",
        "Dưới chân có toa tàu đi đày và 14 cột đá tượng trưng cho 14 năm lưu đày.",
    ],
    {
        "hours_vi": "Khu tưởng niệm ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30 phút.",
        "best_time_vi": "Quanh năm; ngày 28/12 có lễ tưởng niệm nạn nhân trục xuất.",
        "tips_vi": "Đây là nơi tưởng niệm nghiêm trang, nên giữ thái độ tôn trọng; đi lên theo đường xoắn ốc theo chiều kim đồng hồ.",
    },
    [
        {"title": "Wikipedia (RU) — Исход и Возвращение (памятник)", "url": "https://ru.wikipedia.org/wiki/Исход_и_Возвращение_(памятник)"},
        {"title": "Delfin-tour — Памятник «Исход и Возвращение»", "url": "https://www.delfin-tour.ru/poi/landmark/pamyatnik__ishod_i_vozvraschenie_"},
    ],
    ["memorial", "elista", "deportation", "ernst-neizvestny", "history", "kalmyk"],
    maps_text("Памятник Исход и Возвращение", "Элиста", "Exodus and Return Memorial", "Elista", 46.30056, 44.31472),
))

# 18) Памятник Оке Городовикову -----------------------------------------------------
RECORDS.append(rec(
    "gorodovikov-monument-elista",
    "Tượng đài Oka Gorodovikov",
    "Памятник Оке Городовикову",
    "Monument to Oka Gorodovikov",
    ["monument"],
    46.31933, 44.27852,
    "Quảng trường Gorodovikov, vi khu 4, thành phố Elista, Cộng hoà Kalmykia, Nga.",
    "Tượng đài kỵ mã Oka Gorodovikov là tượng đài lớn nhất Elista, tôn vinh vị tướng kỵ binh huyền thoại người Kalmykia, Anh hùng Liên Xô. Bức tượng khánh thành năm 1976, đứng uy nghi trên quảng trường mang tên ông.",
    "Trên quảng trường Gorodovikov (vi khu 4) của Elista, tượng đài kỵ mã Oka Gorodovikov là tượng đài lớn nhất thành phố và là một biểu tượng của niềm tự hào dân tộc Kalmykia. Oka Ivanovich Gorodovikov (1879–1960) là một vị tướng kỵ binh lừng danh, Anh hùng Liên Xô, xuất thân từ người Kalmykia, gắn với những chiến công của kỵ binh Xô Viết. Khánh thành ngày 16/11/1976, bức tượng khắc hoạ vị tướng oai phong trên lưng ngựa, đặt trên bệ hình nón vươn cao, tổ chức lại toàn bộ không gian quảng trường xung quanh. Hình tượng người kỵ sĩ - chiến binh gắn bó sâu sắc với văn hoá du mục và truyền thống thượng võ của người Kalmykia, khiến tượng đài không chỉ tưởng niệm một cá nhân mà còn gợi nhớ cả một di sản. Đây là một điểm dừng ý nghĩa để hiểu thêm về lịch sử hiện đại và bản sắc của nước cộng hoà thảo nguyên.",
    [
        "Tượng đài lớn nhất Elista, khắc hoạ tướng kỵ binh Oka Gorodovikov trên lưng ngựa.",
        "Tôn vinh Anh hùng Liên Xô người Kalmykia; khánh thành năm 1976.",
        "Đặt trên bệ hình nón cao, trung tâm của quảng trường Gorodovikov.",
    ],
    {
        "hours_vi": "Tượng đài ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15 phút.",
        "best_time_vi": "Quanh năm; ban ngày và chiều tối lên đèn.",
        "tips_vi": "Kết hợp dạo trung tâm Elista; lưu ý phân biệt với tượng bán thân tướng B. B. Gorodovikov (cháu ông) trong công viên Druzhba.",
    },
    [
        {"title": "Wikipedia (RU) — Памятник Оке Городовикову (Элиста)", "url": "https://ru.wikipedia.org/wiki/Памятник_Оке_Городовикову_(Элиста)"},
        {"title": "Gorod-Elista — Памятник О.И. Городовикову", "url": "https://www.gorod-elista.ru/gorod-elista/dostoprimechatelnosti/pamyatnik-geroyu-sovetskogo-soyuza-o-i-gorodovikovu-4-mkr-/"},
    ],
    ["monument", "elista", "gorodovikov", "cavalry", "soviet-hero", "history"],
    maps_text("Памятник Оке Городовикову", "Элиста", "Monument to Oka Gorodovikov", "Elista", 46.31933, 44.27852),
))

# 19) Скульптура «Белый старец» (Цаган Аав) -----------------------------------------
RECORDS.append(rec(
    "tsagan-aav-white-elder",
    "Tượng 'Bạch Lão' Tsagan Aav (Ông Già Trắng)",
    "Скульптура «Белый старец» (Цаган Аав)",
    "The White Elder (Tsagan Aav) Statue",
    ["monument"],
    46.3075303, 44.26618,
    "Phố Lenin (khu vực công viên Druzhba), thành phố Elista, Cộng hoà Kalmykia, Nga.",
    "Tsagan Aav ('Bạch Lão' - Ông Già Trắng) là vị thần bảo hộ vạn vật trong tín ngưỡng Kalmykia. Tượng bằng đá cẩm thạch trắng Ural cao 3 m (1998) khắc hoạ ông cùng sói, linh dương saiga và chim - biểu tượng của sự sung túc, an hoà.",
    "Đặt bên phố Lenin gần công viên Druzhba ở trung tâm Elista, tượng 'Bạch Lão' Tsagan Aav (Ông Già Trắng) là một trong những biểu tượng văn hoá - tâm linh được yêu mến nhất của người Kalmykia. Trong tín ngưỡng dân gian hoà quyện với Phật giáo, Tsagan Aav là vị thần già râu tóc bạc phơ - đấng bảo hộ của muôn loài trên mặt đất, thần giữ gìn của cải, sự sung túc và hạnh phúc gia đình, tượng trưng cho sự tinh khiết, vĩnh hằng, đức tin và hoà hợp. Bức tượng bằng đá cẩm thạch trắng vùng Ural cao khoảng 3 m, do nhà điêu khắc N. Eledzhiev thực hiện năm 1998, khắc hoạ ông cùng những sinh vật của thảo nguyên: con sói, linh dương saiga và chim - thể hiện mối giao hoà giữa con người, thần linh và thiên nhiên. Với du khách, đây là nơi tìm hiểu thế giới quan độc đáo của người Kalmykia và là một điểm dừng chân dễ chịu trong hành trình dạo bộ trung tâm thủ phủ.",
    [
        "'Bạch Lão' Tsagan Aav - vị thần bảo hộ vạn vật, biểu tượng của sung túc và an hoà.",
        "Tượng đá cẩm thạch trắng Ural cao ~3 m (1998, điêu khắc gia N. Eledzhiev).",
        "Khắc hoạ ông cùng sói, linh dương saiga và chim - giao hoà người, thần và thiên nhiên.",
    ],
    {
        "hours_vi": "Tượng ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Quanh năm; kết hợp dạo công viên Druzhba và phố Lenin.",
        "tips_vi": "Nằm ngay tuyến dạo bộ trung tâm; tiện kết hợp công viên Druzhba, quảng trường Lenin và Pagoda Bảy Ngày.",
    },
    [
        {"title": "Elistory — Скульптура «Цаган Аав»", "url": "https://elistory.ru/places/153"},
        {"title": "Gorod-Elista — Цаган Аав (Белый Старец)", "url": "https://gorod-elista.ru/gorod-elista/dostoprimechatelnosti/tsagan-aav-belyy-starets/"},
    ],
    ["monument", "elista", "tsagan-aav", "white-elder", "folklore", "culture"],
    maps_text("Белый старец Цаган Аав", "Элиста", "White Elder Tsagan Aav", "Elista", 46.3075303, 44.26618),
))

# 20) Мемориал героев / Вечный огонь ------------------------------------------------
RECORDS.append(rec(
    "war-memorial-eternal-flame-elista",
    "Đài tưởng niệm Anh hùng và Ngọn Lửa Vĩnh Cửu (Elista)",
    "Мемориал героев Гражданской и Великой Отечественной войн (Вечный огонь)",
    "Memorial to Heroes of the Civil and Great Patriotic Wars (Eternal Flame)",
    ["monument"],
    46.305859, 44.2591709,
    "Khu vực công viên Druzhba (phố Verkhnyaya Lomonosova), thành phố Elista, Cộng hoà Kalmykia, Nga.",
    "Đài tưởng niệm với Ngọn Lửa Vĩnh Cửu tôn vinh các anh hùng Nội chiến và Chiến tranh Vệ quốc Vĩ đại. Được dựng năm 1965 nhân 20 năm Chiến thắng, đây là nơi tưởng niệm trang nghiêm bên rìa công viên Druzhba.",
    "Nằm bên rìa công viên Druzhba ở trung tâm Elista, quần thể đài tưởng niệm các anh hùng Nội chiến và Chiến tranh Vệ quốc Vĩ đại (với Ngọn Lửa Vĩnh Cửu) là một trong những địa điểm tưởng niệm quan trọng nhất của thủ phủ Kalmykia. Đài được xây dựng năm 1965 nhân kỷ niệm 20 năm Chiến thắng phát xít, do các kiến trúc sư M. và D. Pyurveev cùng nhà điêu khắc N. Sandzhiev thực hiện. Trung tâm quần thể là Ngọn Lửa Vĩnh Cửu cháy không ngừng, tưởng nhớ những người con Kalmykia đã ngã xuống trong hai cuộc chiến. Vào các dịp lễ trọng như Ngày Chiến thắng 9/5, nơi đây trở thành điểm hội tụ của người dân với những vòng hoa và nghi thức tưởng niệm. Với du khách, đài tưởng niệm là một điểm dừng để hiểu thêm về những trang sử bi tráng của vùng đất và tưởng nhớ các nạn nhân, anh hùng của thế kỷ 20.",
    [
        "Ngọn Lửa Vĩnh Cửu tưởng niệm anh hùng Nội chiến và Chiến tranh Vệ quốc Vĩ đại.",
        "Dựng năm 1965 nhân 20 năm Chiến thắng; điểm tưởng niệm trang nghiêm của Elista.",
        "Nằm bên rìa công viên Druzhba, trung tâm các nghi lễ dịp Ngày Chiến thắng 9/5.",
    ],
    {
        "hours_vi": "Khu tưởng niệm ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15 phút.",
        "best_time_vi": "Quanh năm; đặc biệt trang nghiêm dịp Ngày Chiến thắng 9/5.",
        "tips_vi": "Giữ thái độ tôn trọng nơi tưởng niệm; kết hợp dạo công viên Druzhba liền kề.",
    },
    [
        {"title": "Gorod-Elista — Мемориальный комплекс героев (Вечный огонь)", "url": "https://www.gorod-elista.ru/gorod-elista/dostoprimechatelnosti/memorialnyy-kompleks-v-chest-geroev-grazhdanskoy-i-velikoy-otechestvennoy-voyn/"},
        {"title": "OpenStreetMap — Вечный огонь (Элиста)", "url": "https://www.openstreetmap.org/node/973842966"},
    ],
    ["memorial", "elista", "eternal-flame", "wwii", "history"],
    maps_text("Мемориал героев Вечный огонь", "Элиста", "Eternal Flame Memorial", "Elista", 46.305859, 44.2591709),
))

# ============================ NHÀ HÁT (theatre) ============================

# 21) Национальный драматический театр им. Б. Басангова ------------------------------
RECORDS.append(rec(
    "kalmyk-drama-theatre-basangov",
    "Nhà hát Kịch Quốc gia Kalmykia mang tên Baatr Basangov",
    "Национальный драматический театр им. Б. Басангова",
    "Kalmyk National Drama Theatre named after B. Basangov",
    ["theatre"],
    46.3049051, 44.2632157,
    "Phố Aksyon Suseev 21, thành phố Elista, Cộng hoà Kalmykia, Nga.",
    "Nhà hát Kịch Quốc gia Kalmykia mang tên Baatr Basangov là nhà hát kịch tiếng Kalmyk hàng đầu của nước cộng hoà. Có nguồn gốc từ xưởng kịch Kalmyk đầu tiên (1936), nhà hát là trung tâm gìn giữ ngôn ngữ, sử thi và văn hoá sân khấu Kalmykia.",
    "Ở trung tâm Elista (phố Aksyon Suseev 21), Nhà hát Kịch Quốc gia mang tên Baatr Basangov là ngôi nhà của nghệ thuật sân khấu tiếng Kalmyk - một trụ cột trong đời sống văn hoá của nước cộng hoà. Tiền thân là xưởng kịch Kalmyk đầu tiên trong lịch sử, hình thành từ giữa thập niên 1930 (năm 1936); đến năm 1961, nhà hát được mang tên nhà văn - nhà viết kịch Kalmyk Baatr Basangov. Trải qua nhiều thăng trầm và được tái cơ cấu năm 2011 thành Nhà hát Kịch Quốc gia, đây là nơi dàn dựng các vở diễn dựa trên sử thi 'Dzhangar', truyện dân gian, kịch bản của các tác giả Kalmyk và kinh điển thế giới - phần lớn bằng tiếng Kalmyk, góp phần gìn giữ ngôn ngữ dân tộc. Toà nhà nhà hát với cổng chính có hàng cột và phù điêu trang trí là một điểm nhấn kiến trúc của thành phố. Xem một buổi diễn ở đây là cách sống động để cảm nhận tâm hồn, âm nhạc và ngôn ngữ của người Kalmykia.",
    [
        "Nhà hát kịch tiếng Kalmyk hàng đầu, tiền thân là xưởng kịch Kalmyk đầu tiên (1936).",
        "Mang tên nhà văn - nhà viết kịch Baatr Basangov (từ 1961); tái cơ cấu năm 2011.",
        "Dàn dựng sử thi 'Dzhangar', kịch dân gian và kinh điển, gìn giữ ngôn ngữ Kalmyk.",
    ],
    {
        "hours_vi": "Mở theo lịch biểu diễn và giờ bán vé; nên xem lịch trước.",
        "ticket_vi": "Có bán vé xem kịch; giá tuỳ suất diễn.",
        "duration_vi": "Buổi diễn thường 1,5–2,5 giờ.",
        "best_time_vi": "Mùa diễn (thu - xuân); dịp liên hoan sân khấu có nhiều vở đặc sắc.",
        "tips_vi": "Đặt vé trước qua trang chính thức; nhiều vở diễn bằng tiếng Kalmyk, nên hỏi trước về phụ đề/nội dung.",
    },
    [
        {"title": "Wikipedia (RU) — Калмыцкий драматический театр имени Баатра Басангова", "url": "https://ru.wikipedia.org/wiki/Калмыцкий_государственный_драматический_театр_имени_Баатра_Басангова"},
        {"title": "Culture.ru — Национальный драматический театр им. Б. Басангова", "url": "https://www.culture.ru/institutes/21605/nacionalnyi-dramaticheskii-teatr-im-b-basangova"},
    ],
    ["theatre", "elista", "kalmyk", "culture", "drama"],
    maps_org("https://yandex.ru/maps/org/natsionalny_dramaticheskiy_teatr_im_b_basangova/1106181218/", "Kalmyk National Drama Theatre", "Elista"),
    official_site="https://kalmteatr.ru/",
))

# 22) Русский театр драмы и комедии -------------------------------------------------
RECORDS.append(rec(
    "russian-drama-theatre-elista",
    "Nhà hát Kịch và Hài kịch Nga (Elista)",
    "Республиканский русский театр драмы и комедии",
    "Republican Russian Drama and Comedy Theatre",
    ["theatre"],
    46.3096481, 44.2685214,
    "Phố Maksim Gorky 23, thành phố Elista, Cộng hoà Kalmykia, Nga.",
    "Nhà hát Kịch và Hài kịch Nga ở Elista là nhà hát tiếng Nga của Kalmykia, tách ra từ đoàn kịch Nga của Nhà hát Kịch Kalmyk. Sân khấu quy tụ kịch cổ điển và hài kịch, thường tham gia các liên hoan sân khấu toàn Nga và quốc tế.",
    "Nằm ở phố Maksim Gorky 23 tại trung tâm Elista, Nhà hát Kịch và Hài kịch Nga của nước cộng hoà (Республиканский русский театр драмы и комедии) là sân khấu tiếng Nga tiêu biểu của Kalmykia, bổ sung cho Nhà hát Kịch Quốc gia tiếng Kalmyk và tạo nên đời sống sân khấu song ngữ đặc sắc của thủ phủ. Nhà hát được thành lập năm 1991 trên cơ sở đoàn kịch tiếng Nga vốn thuộc Nhà hát Kịch Nhà nước Kalmyk (có từ năm 1939). Trong tiết mục có cả kịch chính kịch lẫn hài kịch, dựa trên kịch bản kinh điển Nga - thế giới và các vở đương đại. Nhà hát thường xuyên tham gia các liên hoan sân khấu toàn Nga và quốc tế, nhờ đó được biết đến rộng rãi. Đây là lựa chọn hấp dẫn cho du khách nói tiếng Nga muốn thưởng thức một buổi tối nghệ thuật ở Elista, đồng thời phản ánh sự đa dạng văn hoá của nước cộng hoà thảo nguyên.",
    [
        "Nhà hát kịch tiếng Nga của Kalmykia, tách từ đoàn kịch Nga của Nhà hát Kịch Kalmyk (1939).",
        "Thành lập năm 1991; tiết mục gồm cả chính kịch và hài kịch.",
        "Thường tham gia các liên hoan sân khấu toàn Nga và quốc tế.",
    ],
    {
        "hours_vi": "Mở theo lịch biểu diễn và giờ bán vé; nên xem lịch trước.",
        "ticket_vi": "Có bán vé xem kịch; giá tuỳ suất diễn.",
        "duration_vi": "Buổi diễn thường 1,5–2,5 giờ.",
        "best_time_vi": "Mùa diễn (thu - xuân); dịp liên hoan có nhiều vở đặc sắc.",
        "tips_vi": "Đặt vé trước qua trang chính thức; các vở chủ yếu bằng tiếng Nga.",
    },
    [
        {"title": "Culture.ru — Русский театр драмы и комедии", "url": "https://www.culture.ru/institutes/21606/russkii-teatr-dramy-i-komedii"},
        {"title": "Республиканский русский театр драмы и комедии — официальный сайт", "url": "https://rudramt.ru/"},
    ],
    ["theatre", "elista", "russian", "drama", "comedy", "culture"],
    maps_text("Республиканский русский театр драмы и комедии", "Элиста", "Russian Drama and Comedy Theatre", "Elista", 46.3096481, 44.2685214),
    official_site="https://rudramt.ru/",
))

# ============================ QUẢNG TRƯỜNG (square_street) ============================

# 23) Площадь Ленина (Элиста) -------------------------------------------------------
RECORDS.append(rec(
    "lenin-square-elista",
    "Quảng trường Lenin (Trung tâm Elista)",
    "Площадь Ленина",
    "Lenin Square",
    ["square_street"],
    46.3077, 44.2697,
    "Giao phố Lenin và phố Pushkin, trung tâm thành phố Elista, Cộng hoà Kalmykia, Nga.",
    "Quảng trường Lenin là quảng trường trung tâm và trái tim hành chính - lễ hội của Elista. Bao quanh là Nhà Chính phủ, đài phun nước nhạc - ánh sáng 'Ba Đoá Sen' và biểu tượng Pagoda Bảy Ngày với bánh xe cầu nguyện khổng lồ.",
    "Ở tim thành phố Elista, chỗ giao phố Lenin và phố Pushkin, Quảng trường Lenin (Площадь Ленина) là quảng trường trung tâm và không gian công cộng quan trọng nhất của thủ phủ Kalmykia - nơi diễn ra các sự kiện, lễ hội và tụ họp của người dân. Bao quanh quảng trường là những công trình tiêu biểu của thành phố: Nhà Chính phủ nước cộng hoà, đài phun nước nhạc - ánh sáng 'Ba Đoá Sen' (Tri Lotosa) - đài phun nước nhạc - ánh sáng đầu tiên của vùng, và đặc biệt là Pagoda Bảy Ngày (Пагода Семи дней) với bánh xe cầu nguyện lớn bên trong - một biểu tượng Phật giáo đã thành 'thương hiệu' của Elista. Sự pha trộn giữa kiến trúc hành chính hiện đại, biểu tượng Phật giáo và không gian cây xanh, đài phun nước khiến quảng trường trở thành điểm khởi đầu tự nhiên cho hành trình khám phá thành phố. Buổi tối, khi đài phun nước và Pagoda lên đèn, quảng trường trở nên lung linh và là nơi hóng mát yêu thích của cư dân.",
    [
        "Quảng trường trung tâm và trái tim lễ hội - hành chính của Elista.",
        "Bao quanh có Nhà Chính phủ, đài phun nước nhạc - ánh sáng 'Ba Đoá Sen'.",
        "Biểu tượng Pagoda Bảy Ngày với bánh xe cầu nguyện khổng lồ đặt ngay quảng trường.",
    ],
    {
        "hours_vi": "Không gian mở, dạo chơi tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–45 phút (chưa kể vào tham quan Pagoda Bảy Ngày).",
        "best_time_vi": "Chiều mát và buổi tối khi đài phun nước, Pagoda lên đèn.",
        "tips_vi": "Kết hợp tham quan Pagoda Bảy Ngày ngay tại quảng trường và công viên Druzhba gần đó; buổi tối mùa hè có đài phun nước nhạc nước.",
    },
    [
        {"title": "Wikipedia (RU) — Площадь Ленина (Элиста)", "url": "https://ru.wikipedia.org/wiki/Площадь_Ленина_(Элиста)"},
        {"title": "AutoTravel — Площадь Ленина (Элиста)", "url": "https://autotravel.ru/otklik.php/4597"},
    ],
    ["square", "elista", "city-center", "pagoda", "fountain", "landmark"],
    maps_text("Площадь Ленина", "Элиста", "Lenin Square", "Elista", 46.3077, 44.2697),
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
