# -*- coding: utf-8 -*-
"""Bổ sung địa điểm du lịch Việt Nam nổi tiếng còn thiếu (chạy nền tự động).

Đợt này: 7 tỉnh/thành MỚI (sau sáp nhập 1/7/2025) chưa có file:
  Lạng Sơn, Phú Thọ (gồm Vĩnh Phúc + Hòa Bình cũ), Hà Tĩnh,
  Thái Nguyên (gồm Bắc Kạn cũ), Quảng Ngãi (gồm Kon Tum cũ),
  Đồng Nai (gồm Bình Phước cũ), Bắc Ninh (gồm Bắc Giang cũ).

Chèn AN TOÀN: nạp – append – ghi; bỏ qua slug đã có. Toạ độ THẬT; đủ VI/EN/RU.
"""
import json, os, glob, re, urllib.parse

TODAY = "2026-07-27"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REG = os.path.join(ROOT, "data", "regions")

NEW = []
def add(d): NEW.append(d)


def _clean_name(name):
    name = re.sub(r"\s*\(.*?\)\s*", " ", name or "")
    name = name.split(" (")[0]
    return re.sub(r"\s+", " ", name).strip()


def _pretty_en(region_slug):
    base = region_slug[3:] if region_slug.startswith("vn-") else region_slug
    return base.replace("-", " ").title()


def vn_maps(name_en, region_slug, lat, lon):
    """Sinh link bản đồ TRỎ-ĐỊA-ĐIỂM giống tools/retrofit_map_links.py (Việt Nam)."""
    reg_en = _pretty_en(region_slug)
    gname = _clean_name(name_en)
    parts = [gname] + ([reg_en] if reg_en.lower() not in gname.lower() else []) + ["Vietnam"]
    q = urllib.parse.quote(", ".join(parts))
    return {
        "yandex": f"https://yandex.com/maps/?text={q}&ll={lon},{lat}&z=17",
        "google": f"https://www.google.com/maps/search/?api=1&query={q}",
    }


def finalize(d):
    lat = d["coordinates"]["lat"]; lon = d["coordinates"]["lon"]
    return {
        "id": f'{d["region"]}-{d["slug"]}',
        "slug": d["slug"],
        "region": d["region"],
        "country": "vietnam",
        "region_name_vi": d["region_name_vi"],
        "federal_district": d["federal_district"],
        "name_vi": d["name_vi"],
        "name_ru": d["name_ru"],
        "name_en": d["name_en"],
        "categories": d["categories"],
        "coordinates": d["coordinates"],
        "address_vi": d.get("address_vi", ""),
        "rating": d.get("rating"),
        "review_summary_vi": d.get("review_summary_vi", ""),
        "presentation_short_vi": d["presentation_short_vi"],
        "presentation_short_en": d["presentation_short_en"],
        "presentation_short_ru": d["presentation_short_ru"],
        "presentation_long_vi": d["presentation_long_vi"],
        "presentation_long_en": d["presentation_long_en"],
        "presentation_long_ru": d["presentation_long_ru"],
        "highlights_vi": d["highlights_vi"],
        "highlights_en": d["highlights_en"],
        "highlights_ru": d["highlights_ru"],
        "practical": d.get("practical", {}),
        "photo": d.get("photo"),
        "photo_credit": d.get("photo_credit"),
        "maps": vn_maps(d["name_en"], d["region"], lat, lon),
        "official_site": d.get("official_site"),
        "sources": d.get("sources", []),
        "tags": d.get("tags", []),
        "status": "enriched",
        "last_updated": TODAY,
    }


# ============================ RECORDS ============================
# ---------- LẠNG SƠN ----------
add({
  "region": "vn-lang-son", "slug": "dong-tam-thanh",
  "region_name_vi": "Lạng Sơn", "federal_district": "Miền Bắc",
  "name_vi": "Động Tam Thanh (Chùa Tam Thanh)",
  "name_en": "Tam Thanh Cave and Pagoda",
  "name_ru": "Пещера и пагода Тамтхань",
  "categories": ["church", "park_garden"],
  "coordinates": {"lat": 21.8558, "lon": 106.7539},
  "address_vi": "Phường Tam Thanh, thành phố Lạng Sơn, tỉnh Lạng Sơn",
  "rating": {"value": 4.4, "count": 3200, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Du khách thích không khí mát lạnh trong hang, hệ thạch nhũ đẹp và ngôi chùa cổ ngay trong lòng núi. Nhiều người kết hợp leo lên ngắm nàng Tô Thị và thành nhà Mạc gần đó; một số lưu ý bậc thang trơn nên đi giày bám tốt.",
  "presentation_short_vi": "Động Tam Thanh là danh thắng biểu tượng của xứ Lạng, một hang đá vôi lớn ngay trong lòng thành phố Lạng Sơn. Bên trong hang là chùa Tam Thanh cổ kính với tượng Phật A Di Đà tạc vào vách đá, cùng dòng suối 'Ngư Tuyền' trong mát và cửa hang 'Thông Thiên' đón ánh sáng trời.",
  "presentation_short_en": "Tam Thanh Cave is the emblematic landmark of Lang Son, a large limestone grotto in the heart of the city. Inside it shelters the ancient Tam Thanh Pagoda, with an Amitabha Buddha carved into the rock face, a clear underground spring and a natural 'sky-gate' opening that lets daylight pour in.",
  "presentation_short_ru": "Пещера Тамтхань — символ провинции Лангшон, большой известняковый грот в самом центре города Лангшон. Внутри укрыта старинная пагода Тамтхань с образом будды Амитабхи, высеченным в скале, прозрачный подземный источник и естественное «небесное окно», сквозь которое льётся дневной свет.",
  "presentation_long_vi": "Nằm ngay trong lòng thành phố Lạng Sơn, Động Tam Thanh từ lâu đã được ca ngợi là 'Đệ nhất bát cảnh xứ Lạng'. Đây là một hang động đá vôi rộng, mát lạnh quanh năm, gắn với ngôi chùa Tam Thanh có từ khoảng thời Lê. Điểm đặc biệt nhất là pho tượng Phật A Di Đà cao hơn hai mét được tạc nổi trực tiếp vào vách đá phía trong, mang phong cách nghệ thuật cổ độc đáo. Trong hang còn có hồ Âm Ty với dòng nước không bao giờ cạn, những khối thạch nhũ hình thù kỳ lạ và cửa 'Thông Thiên' mở lên trời, nơi ánh sáng rọi xuống tạo khung cảnh huyền ảo. Trên vách động lưu giữ nhiều bài thơ, văn khắc của các danh nhân qua các thời kỳ, trong đó có bút tích của Ngô Thì Sĩ thế kỷ 18. Ngay cạnh động là núi Tô Thị với tượng đá 'nàng Tô Thị' bồng con chờ chồng đã đi vào ca dao, và dấu tích thành nhà Mạc trên đỉnh đồi. Cụm di tích tạo nên một hành trình vừa tâm linh, vừa lịch sử, vừa thắng cảnh, rất thuận tiện cho du khách khi ghé thăm thành phố vùng biên.",
  "presentation_long_en": "Set right in the middle of Lang Son city, Tam Thanh Cave has long been praised as the finest of the 'eight scenic wonders' of this borderland province. It is a broad limestone grotto, cool throughout the year, that houses Tam Thanh Pagoda, thought to date from the Le dynasty. Its most remarkable feature is a relief statue of Amitabha Buddha, more than two metres tall, carved directly into the inner rock wall in a distinctive old artistic style. The cave also holds a pool whose water never runs dry, strangely shaped stalactites and a natural 'sky-gate' opening overhead through which daylight streams to magical effect. The cave walls preserve poems and inscriptions left by scholars across the centuries, including the hand of Ngo Thi Si in the 18th century. Immediately beside the cave rises To Thi Mountain, crowned by the stone figure of a woman holding her child as she waits for her husband — an image woven into Vietnamese folk verse — and the ruins of the Mac dynasty citadel. Together the sites make a short journey that is at once spiritual, historical and scenic, and easy to reach when visiting this frontier city.",
  "presentation_long_ru": "Расположенная прямо в центре города Лангшон, пещера Тамтхань издавна считается лучшим из «восьми чудес» этой приграничной провинции. Это широкий известняковый грот, прохладный круглый год, в котором укрыта пагода Тамтхань, предположительно относящаяся к эпохе Ле. Самая примечательная его черта — рельефный образ будды Амитабхи высотой более двух метров, высеченный прямо во внутренней скале в характерном древнем стиле. В пещере есть также водоём, который никогда не пересыхает, причудливые сталактиты и естественное «небесное окно» вверху, сквозь которое волшебно льётся дневной свет. На стенах сохранились стихи и надписи учёных разных веков, в том числе рука Нго Тхи Ши, жившего в XVIII веке. Прямо рядом с пещерой поднимается гора Тоши, увенчанная каменной фигурой женщины с ребёнком, ожидающей мужа, — образ, вошедший во вьетнамский фольклор, — и руины цитадели династии Мак. Вместе эти места складываются в короткий маршрут, одновременно духовный, исторический и живописный, и легко доступны при посещении приграничного города. Прохлада грота, эхо капающей воды и запах благовоний создают особое, медитативное настроение, а по выходным и в дни праздников сюда приходит немало паломников и школьных экскурсий.",
  "highlights_vi": [
    "Tượng Phật A Di Đà tạc nổi vào vách đá trong lòng hang, phong cách cổ độc đáo",
    "Được tôn là 'Đệ nhất bát cảnh xứ Lạng', có cửa 'Thông Thiên' và hồ nước không cạn",
    "Kề bên núi Tô Thị (nàng Tô Thị) và di tích thành nhà Mạc"
  ],
  "highlights_en": [
    "Amitabha Buddha carved in relief on the cave wall in a distinctive old style",
    "Honoured as Lang Son's finest scenic wonder, with a natural 'sky-gate' and an ever-full pool",
    "Beside To Thi Mountain (the waiting-wife stone) and the Mac dynasty citadel ruins"
  ],
  "highlights_ru": [
    "Рельефный образ будды Амитабхи на стене пещеры в характерном древнем стиле",
    "Считается лучшим чудом Лангшона; есть «небесное окно» и никогда не пересыхающий водоём",
    "Рядом гора Тоши (камень ждущей жены) и руины цитадели династии Мак"
  ],
  "practical": {
    "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
    "ticket_vi": "Vé tham quan thường khoảng 20.000–30.000 VND/người.",
    "duration_vi": "Khoảng 1–2 giờ (kết hợp núi Tô Thị, thành nhà Mạc).",
    "best_time_vi": "Mùa thu và mùa xuân; kết hợp phiên chợ Kỳ Lừa.",
    "tips_vi": "Đi giày bám tốt vì nền hang ẩm trơn; mang theo đèn pin nhỏ; nên ghé núi Tô Thị gần đó."
  },
  "tags": ["cave", "temple", "history", "viewpoint", "outdoor", "top"],
  "sources": [{"title": "Wikipedia (VI) — Động Tam Thanh", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%99ng_Tam_Thanh"}]
})

add({
  "region": "vn-lang-son", "slug": "nui-mau-son",
  "region_name_vi": "Lạng Sơn", "federal_district": "Miền Bắc",
  "name_vi": "Núi Mẫu Sơn",
  "name_en": "Mau Son Mountain",
  "name_ru": "Гора Маушон",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 21.8500, "lon": 107.0333},
  "address_vi": "Xã Mẫu Sơn, tỉnh Lạng Sơn (cách TP Lạng Sơn khoảng 30 km)",
  "rating": {"value": 4.3, "count": 2100, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Du khách mê không khí se lạnh, biển mây buổi sớm và những biệt thự Pháp cổ rêu phong. Mùa đông có năm xuất hiện băng giá hiếm thấy ở Việt Nam. Đường đèo lên núi nhiều khúc cua nên nhiều người khuyên tài xế đi chậm, chắc tay lái.",
  "presentation_short_vi": "Mẫu Sơn là vùng núi cao trên 1.500 m ở phía đông tỉnh Lạng Sơn, nơi khí hậu quanh năm mát lạnh, mùa đông có thể xuống dưới 0°C và xuất hiện băng giá. Du khách đến đây để săn mây, ngắm rừng nguyên sinh, thăm những biệt thự nghỉ dưỡng kiểu Pháp và thưởng thức đặc sản gà sáu ngón, rượu Mẫu Sơn.",
  "presentation_short_en": "Mau Son is a highland massif rising above 1,500 m in eastern Lang Son, cool all year round, where winter temperatures can drop below freezing and frost — even rare ice — sometimes forms. Visitors come to chase seas of cloud, walk in old-growth forest, explore French-era villas and taste local specialities such as six-toed chicken and Mau Son wine.",
  "presentation_short_ru": "Маушон — горный массив высотой более 1500 м на востоке провинции Лангшон, прохладный круглый год; зимой температура может опускаться ниже нуля, и порой образуется иней и даже редкий для Вьетнама лёд. Сюда приезжают, чтобы поймать «море облаков», гулять по девственному лесу, осматривать виллы французской эпохи и пробовать местные деликатесы.",
  "presentation_long_vi": "Cách thành phố Lạng Sơn khoảng 30 km về phía đông, khu du lịch Mẫu Sơn nằm trên một dãy núi gồm nhiều đỉnh, cao nhất khoảng 1.541 m so với mực nước biển. Nhờ độ cao và vị trí đón gió, nơi đây có khí hậu ôn đới hiếm có: mùa hè mát mẻ như một 'Sa Pa của vùng Đông Bắc', còn mùa đông nhiệt độ có thể xuống dưới 0°C, thỉnh thoảng phủ băng giá và sương muối thu hút đông du khách hiếu kỳ. Từ thời Pháp, Mẫu Sơn đã được chọn làm nơi nghỉ dưỡng, để lại quần thể hàng chục biệt thự đá nay phần lớn chỉ còn phế tích rêu phong, tạo nên vẻ đẹp hoài cổ giữa rừng núi. Vùng núi là địa bàn cư trú của người Dao với những tập tục, lễ hội và tri thức thảo dược đặc sắc; tắm lá thuốc người Dao là trải nghiệm được ưa chuộng. Mẫu Sơn còn nổi tiếng với các đặc sản như gà sáu ngón, ếch hương, chanh rừng, đào chuông và rượu Mẫu Sơn men lá. Buổi sớm, khi mây luồn qua các thung lũng và mặt trời nhô lên phía biên giới, khung cảnh trở nên kỳ vĩ, là phần thưởng cho những ai vượt qua con đèo quanh co để lên đỉnh.",
  "presentation_long_en": "About 30 km east of Lang Son city, the Mau Son resort area occupies a range of several peaks, the highest around 1,541 m above sea level. Thanks to its altitude and exposure to the wind, it enjoys a rare temperate climate: cool in summer, like a 'Sa Pa of the north-east', while in winter the temperature can fall below zero and frost — occasionally ice — draws crowds of curious visitors. The French chose Mau Son as a hill station, leaving behind dozens of stone villas, most now moss-covered ruins that lend a nostalgic beauty to the forested slopes. The mountains are home to the Dao people, whose customs, festivals and herbal knowledge are distinctive; a bath in Dao medicinal leaves is a favourite experience. Mau Son is also known for specialities such as six-toed chicken, fragrant frog, wild lime, bell-peach and leaf-fermented Mau Son wine. In the early morning, when cloud threads through the valleys and the sun rises over the nearby border, the scenery turns majestic — a reward for those who climb the winding pass to the top.",
  "presentation_long_ru": "Примерно в 30 км к востоку от города Лангшон курортная зона Маушон занимает гряду из нескольких вершин, самая высокая — около 1541 м над уровнем моря. Благодаря высоте и открытости ветрам здесь редкий для страны умеренный климат: летом прохладно, словно в «Шапе северо-востока», а зимой температура может падать ниже нуля, и иней — а порой и лёд — привлекает толпы любопытных. Ещё при французах Маушон стал горным курортом, оставившим десятки каменных вилл; большинство из них теперь поросшие мхом руины, придающие лесистым склонам ностальгическую красоту. В горах живёт народ зао со своими обычаями, праздниками и знанием трав; ванна из лечебных листьев зао — одно из любимых занятий гостей. Маушон славится и местными деликатесами: шестипалой курицей, ароматной лягушкой, дикими лаймами, «колокольчиковым» персиком и вином Маушон на листовой закваске. Ранним утром, когда облака струятся по долинам, а солнце встаёт над близкой границей, пейзаж становится величественным — награда тем, кто одолел извилистый перевал до вершины.",
  "highlights_vi": [
    "Vùng núi trên 1.500 m, mùa đông có băng giá hiếm thấy ở Việt Nam",
    "Quần thể biệt thự đá kiểu Pháp cổ nay là phế tích rêu phong giữa rừng",
    "Văn hóa người Dao, tắm lá thuốc và đặc sản gà sáu ngón, rượu Mẫu Sơn"
  ],
  "highlights_en": [
    "Highland above 1,500 m where winter frost — rare in Vietnam — can form",
    "Cluster of old French stone villas, now moss-covered ruins amid the forest",
    "Dao ethnic culture, herbal-leaf baths and specialities like six-toed chicken and Mau Son wine"
  ],
  "highlights_ru": [
    "Высокогорье выше 1500 м, где зимой образуется редкий для Вьетнама иней",
    "Комплекс старых французских каменных вилл, ныне поросших мхом руин в лесу",
    "Культура народа зао, ванны из лечебных трав и деликатесы Маушона"
  ],
  "practical": {
    "hours_vi": "Tham quan cả ngày (khu vực mở).",
    "ticket_vi": "Không có vé chung; chi phí gửi xe, dịch vụ và lưu trú tùy điểm.",
    "duration_vi": "Nửa ngày đến 2 ngày (nếu nghỉ đêm săn mây).",
    "best_time_vi": "Hè để tránh nóng; mùa đông (tháng 12–1) để đón băng giá.",
    "tips_vi": "Mang áo ấm kể cả mùa hè; đường đèo nhiều cua, lái xe chắc tay; đặt phòng trước dịp lạnh."
  },
  "tags": ["mountain", "nature", "viewpoint", "cool-climate", "outdoor", "top"],
  "sources": [{"title": "Wikipedia (VI) — Mẫu Sơn", "url": "https://vi.wikipedia.org/wiki/M%E1%BA%ABu_S%C6%A1n"}]
})

add({
  "region": "vn-lang-son", "slug": "ai-chi-lang",
  "region_name_vi": "Lạng Sơn", "federal_district": "Miền Bắc",
  "name_vi": "Ải Chi Lăng",
  "name_en": "Chi Lang Pass",
  "name_ru": "Перевал Чиланг",
  "categories": ["fortress", "monument"],
  "coordinates": {"lat": 21.6197, "lon": 106.5030},
  "address_vi": "Xã Chi Lăng, tỉnh Lạng Sơn (trên quốc lộ 1A, cách TP Lạng Sơn khoảng 40 km)",
  "rating": {"value": 4.4, "count": 900, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Điểm đến gợi nhiều tự hào lịch sử: cửa ải hiểm trở gắn với các chiến thắng chống ngoại xâm. Du khách thích khung cảnh núi non hùng vĩ và bảo tàng nhỏ tái hiện trận Chi Lăng 1427; nên có thuyết minh để hiểu hết ý nghĩa.",
  "presentation_short_vi": "Ải Chi Lăng là cửa ải hiểm yếu bậc nhất trên con đường thiên lý phía Bắc, nằm giữa những dãy núi đá dựng đứng ở tỉnh Lạng Sơn. Nơi đây gắn với nhiều chiến thắng oanh liệt chống quân xâm lược phương Bắc, tiêu biểu là trận Chi Lăng năm 1427 chém đầu tướng Liễu Thăng của nghĩa quân Lam Sơn.",
  "presentation_short_en": "Chi Lang Pass is one of the most formidable defiles on the ancient northern highway, squeezed between sheer rock ranges in Lang Son province. It is bound up with a string of glorious victories against northern invaders, above all the battle of Chi Lang in 1427, when the Lam Son insurgents killed the Ming general Liu Sheng.",
  "presentation_short_ru": "Перевал Чиланг — одна из самых неприступных теснин на старой северной дороге, зажатая между отвесными скалистыми грядами в провинции Лангшон. С ним связан ряд славных побед над северными захватчиками, прежде всего битва при Чиланге в 1427 году, когда повстанцы Ламшон обезглавили минского полководца Лю Шэна.",
  "presentation_long_vi": "Trải dài khoảng 20 km dọc quốc lộ 1A qua tỉnh Lạng Sơn, ải Chi Lăng là một thung lũng hẹp bị kẹp giữa dãy núi đá vôi Cai Kinh phía tây và núi đất Bảo Đài phía đông, chỉ có một lối đi độc đạo. Địa thế 'quỷ môn quan' hiểm trở ấy khiến Chi Lăng trở thành phòng tuyến then chốt che chở kinh đô Thăng Long trước các đạo quân từ phương Bắc trong suốt nhiều thế kỷ. Tại đây, quân dân Đại Việt đã lập nên hàng loạt chiến công vang dội: từ thời Lý, Trần chống Tống, chống Nguyên – Mông, cho đến trận Chi Lăng lịch sử năm 1427, khi nghĩa quân Lam Sơn do Lê Lợi lãnh đạo phục kích và tiêu diệt hơn một vạn quân Minh, chém đầu chủ tướng Liễu Thăng ngay dưới chân núi Mã Yên, mở đường cho thắng lợi hoàn toàn của khởi nghĩa Lam Sơn. Ngày nay, khu di tích Chi Lăng gồm nhiều điểm như núi Mã Yên, các lũy ải, tượng đài chiến thắng và một nhà trưng bày giới thiệu hiện vật, sơ đồ trận đánh. Đứng giữa cửa ải, phóng tầm mắt lên những vách núi dựng đứng, du khách dễ cảm nhận được khí thế hào hùng của một trong những 'yết hầu' quân sự nổi tiếng nhất lịch sử Việt Nam.",
  "presentation_long_en": "Stretching some 20 km along National Highway 1A through Lang Son province, Chi Lang Pass is a narrow valley pinched between the limestone Cai Kinh range to the west and the earthen Bao Dai hills to the east, leaving only a single corridor. This 'devil's gate' terrain made Chi Lang a crucial line of defence shielding the capital Thang Long from northern armies for many centuries. Here the soldiers and people of Dai Viet won a succession of resounding victories: against the Song under the Ly and Tran, against the Mongols, and above all in the historic battle of 1427, when the Lam Son insurgents led by Le Loi ambushed and destroyed more than ten thousand Ming troops and beheaded their commander Liu Sheng at the foot of Ma Yen hill, opening the way to the complete triumph of the uprising. Today the Chi Lang relic complex includes sites such as Ma Yen hill, ramparts and gateways, a victory monument and a small display hall presenting artefacts and battle maps. Standing in the pass beneath the sheer cliffs, visitors readily sense the heroic spirit of one of the most famous military 'throats' in Vietnamese history.",
  "presentation_long_ru": "Растянувшись примерно на 20 км вдоль национального шоссе 1A через провинцию Лангшон, перевал Чиланг представляет собой узкую долину, зажатую между известняковой грядой Кайкинь на западе и земляными холмами Баодай на востоке, с единственным проходом. Этот рельеф «дьявольских ворот» делал Чиланг ключевым рубежом обороны, прикрывавшим столицу Тханглонг от северных армий на протяжении многих веков. Здесь воины и народ Дайвьета одержали ряд громких побед: против Сун при династиях Ли и Чан, против монголов и прежде всего в исторической битве 1427 года, когда повстанцы Ламшон во главе с Ле Лоем устроили засаду и уничтожили более десяти тысяч минских солдат, обезглавив их командующего Лю Шэна у подножия холма Маен, что открыло путь к полной победе восстания. Сегодня комплекс Чиланг включает холм Маен, валы и ворота, монумент победы и небольшой выставочный зал с артефактами и схемами сражений. Стоя в теснине под отвесными скалами, гости легко ощущают героический дух одного из самых знаменитых военных «горл» в истории Вьетнама.",
  "highlights_vi": [
    "Cửa ải 'quỷ môn quan' hiểm trở, phòng tuyến che chở Thăng Long suốt nhiều thế kỷ",
    "Nơi diễn ra trận Chi Lăng 1427, nghĩa quân Lam Sơn chém đầu tướng Liễu Thăng",
    "Khu di tích có núi Mã Yên, tượng đài chiến thắng và nhà trưng bày hiện vật"
  ],
  "highlights_en": [
    "A 'devil's gate' defile that shielded Thang Long for centuries",
    "Site of the 1427 battle where Lam Son forces beheaded Ming general Liu Sheng",
    "Relic complex with Ma Yen hill, a victory monument and an artefact hall"
  ],
  "highlights_ru": [
    "Теснина «дьявольских ворот», веками прикрывавшая столицу Тханглонг",
    "Место битвы 1427 года, где войска Ламшон обезглавили минского полководца Лю Шэна",
    "Комплекс с холмом Маен, монументом победы и залом артефактов"
  ],
  "practical": {
    "hours_vi": "Khu di tích ngoài trời, tham quan ban ngày; nhà trưng bày giờ hành chính.",
    "ticket_vi": "Vào khu vực thường miễn phí hoặc phí tượng trưng.",
    "duration_vi": "Khoảng 1–2 giờ.",
    "best_time_vi": "Quanh năm; đẹp vào mùa thu trời quang.",
    "tips_vi": "Nên có hướng dẫn/thuyết minh để hiểu diễn biến trận đánh; kết hợp dừng chân trên hành trình Hà Nội – Lạng Sơn."
  },
  "tags": ["history", "battlefield", "monument", "outdoor", "daytrip"],
  "sources": [{"title": "Wikipedia (VI) — Ải Chi Lăng", "url": "https://vi.wikipedia.org/wiki/%E1%BA%A2i_Chi_L%C4%83ng"}]
})

# ---------- PHÚ THỌ (gồm Vĩnh Phúc + Hòa Bình cũ) ----------
add({
  "region": "vn-phu-tho", "slug": "den-hung",
  "region_name_vi": "Phú Thọ", "federal_district": "Miền Bắc",
  "name_vi": "Khu di tích lịch sử Đền Hùng",
  "name_en": "Hung Kings Temple (Den Hung)",
  "name_ru": "Храм королей Хунг (Денхунг)",
  "categories": ["church", "monument"],
  "coordinates": {"lat": 21.3661, "lon": 105.3167},
  "address_vi": "Núi Nghĩa Lĩnh, xã Hy Cương, thành phố Việt Trì, tỉnh Phú Thọ",
  "rating": {"value": 4.6, "count": 15000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Không gian linh thiêng, cội nguồn dân tộc; du khách xúc động khi leo qua các đền Hạ, Trung, Thượng lên đỉnh núi Nghĩa Lĩnh. Dịp Giỗ Tổ 10/3 âm lịch rất đông; ngày thường yên tĩnh, cây cối rợp bóng, thích hợp vãn cảnh.",
  "presentation_short_vi": "Khu di tích Đền Hùng trên núi Nghĩa Lĩnh là nơi thờ các Vua Hùng – những vị vua khai sinh nhà nước Văn Lang, được coi là cội nguồn của dân tộc Việt Nam. Quần thể gồm đền Hạ, đền Trung, đền Thượng, đền Giếng và lăng Vua Hùng, gắn với Giỗ Tổ Hùng Vương mồng 10 tháng 3 âm lịch.",
  "presentation_short_en": "The Hung Kings relic complex on Nghia Linh Mountain honours the Hung Kings, founders of the ancient Van Lang state and regarded as the ancestral origin of the Vietnamese nation. The ensemble of Lower, Middle and Upper temples, the Well Temple and the royal tomb is the focus of the national Hung Kings' commemoration on the tenth day of the third lunar month.",
  "presentation_short_ru": "Комплекс храма королей Хунг на горе Нгиалинь посвящён королям Хунг — основателям древнего государства Ванланг, которых считают прародителями вьетнамской нации. Ансамбль из Нижнего, Среднего и Верхнего храмов, храма Колодца и царской гробницы — центр общенационального поминовения королей Хунг в десятый день третьего лунного месяца.",
  "presentation_long_vi": "Nằm trên núi Nghĩa Lĩnh thuộc thành phố Việt Trì, tỉnh Phú Thọ, Khu di tích lịch sử Đền Hùng là nơi thờ tự các Vua Hùng và được xem là điểm hội tụ tâm linh, cội nguồn của cộng đồng người Việt. Theo truyền thuyết, đây là vùng đất kinh đô của nhà nước Văn Lang xưa. Con đường hành hương dẫn du khách lần lượt qua đền Hạ – nơi gắn với truyền thuyết mẹ Âu Cơ sinh bọc trăm trứng, đền Trung, đền Thượng trên đỉnh núi cùng lăng Vua Hùng, rồi xuống đền Giếng phía dưới. Xen giữa rừng cây cổ thụ là những bậc đá rêu phong, tạo nên không gian trầm mặc, thiêng liêng. Hằng năm vào ngày mồng 10 tháng 3 âm lịch, cả nước hướng về Giỗ Tổ Hùng Vương với câu ca 'Dù ai đi ngược về xuôi, nhớ ngày Giỗ Tổ mồng mười tháng ba', thu hút hàng triệu lượt người về dâng hương. 'Tín ngưỡng thờ cúng Hùng Vương ở Phú Thọ' đã được UNESCO ghi danh là Di sản văn hóa phi vật thể đại diện của nhân loại năm 2012. Ngoài giá trị tâm linh, khu di tích còn có Bảo tàng Hùng Vương và cảnh quan đồi rừng xanh mát, là điểm đến kết hợp hành hương và tham quan ý nghĩa.",
  "presentation_long_en": "On Nghia Linh Mountain in Viet Tri city, Phu Tho province, the Hung Kings Historical Relic Complex is dedicated to the Hung Kings and is regarded as the spiritual heart and ancestral cradle of the Vietnamese people. By legend this was the capital region of the ancient Van Lang state. A pilgrimage path leads visitors past the Lower Temple — linked to the legend of Mother Au Co and her sac of a hundred eggs — then the Middle Temple, the Upper Temple on the summit and the royal tomb, before descending to the Well Temple below. Moss-covered stone steps thread through ancient forest, creating a solemn, sacred atmosphere. Every year on the tenth day of the third lunar month the whole country turns towards the Hung Kings' commemoration, drawing millions to offer incense, as the proverb urges: 'Wherever you wander, remember the ancestral anniversary on the tenth of the third month.' The 'Worship of the Hung Kings in Phu Tho' was inscribed by UNESCO as an Intangible Cultural Heritage of Humanity in 2012. Beyond its spiritual value, the complex includes the Hung Kings Museum and cool, green wooded hills, making it a meaningful destination that blends pilgrimage with sightseeing.",
  "presentation_long_ru": "На горе Нгиалинь в городе Вьетчи провинции Футхо исторический комплекс королей Хунг посвящён королям Хунг и считается духовным сердцем и прародиной вьетнамского народа. По преданию, здесь находилась столица древнего государства Ванланг. Паломническая тропа ведёт мимо Нижнего храма, связанного с легендой о матери Ау Ко и её мешочке со ста яйцами, затем к Среднему храму, Верхнему храму на вершине и царской гробнице, после чего спускается к храму Колодца внизу. Поросшие мхом каменные ступени вьются сквозь древний лес, создавая торжественную, священную атмосферу. Ежегодно в десятый день третьего лунного месяца вся страна обращается к поминовению королей Хунг, и миллионы людей приходят возжечь благовония, как призывает пословица: «Куда бы ты ни шёл, помни день поминовения предков — десятое число третьего месяца». «Культ королей Хунг в Футхо» был внесён ЮНЕСКО в список нематериального наследия человечества в 2012 году. Помимо духовной ценности, комплекс включает музей королей Хунг и прохладные зелёные лесистые холмы, что делает его значимым местом, соединяющим паломничество и осмотр достопримечательностей.",
  "highlights_vi": [
    "Nơi thờ các Vua Hùng – cội nguồn dân tộc, gắn kinh đô Văn Lang xưa",
    "Giỗ Tổ Hùng Vương mồng 10 tháng 3 âm lịch, quốc lễ thu hút hàng triệu người",
    "Tín ngưỡng thờ cúng Hùng Vương được UNESCO ghi danh (2012)"
  ],
  "highlights_en": [
    "Shrine of the Hung Kings — the nation's ancestral origin, seat of ancient Van Lang",
    "National commemoration on the tenth of the third lunar month, drawing millions",
    "The worship of the Hung Kings inscribed by UNESCO (2012)"
  ],
  "highlights_ru": [
    "Святилище королей Хунг — прародина нации и столица древнего Ванланга",
    "Общенациональное поминовение в десятый день третьего лунного месяца",
    "Культ королей Хунг внесён в список ЮНЕСКО (2012)"
  ],
  "practical": {
    "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
    "ticket_vi": "Vé tham quan khoảng 10.000 VND; Bảo tàng Hùng Vương có vé riêng.",
    "duration_vi": "Khoảng 2–3 giờ (leo bộ lên đền Thượng).",
    "best_time_vi": "Ngày thường để tránh đông; dịp Giỗ Tổ (tháng 3 âm lịch) để dự lễ.",
    "tips_vi": "Mang giày thoải mái để leo bậc đá; đi sớm cho mát; ăn mặc lịch sự nơi thờ tự."
  },
  "tags": ["heritage", "unesco", "temple", "history", "pilgrimage", "top"],
  "sources": [{"title": "Wikipedia (VI) — Khu di tích lịch sử Đền Hùng", "url": "https://vi.wikipedia.org/wiki/Khu_di_t%C3%ADch_l%E1%BB%8Bch_s%E1%BB%AD_%C4%90%E1%BB%81n_H%C3%B9ng"}]
})

add({
  "region": "vn-phu-tho", "slug": "tam-dao",
  "region_name_vi": "Phú Thọ", "federal_district": "Miền Bắc",
  "name_vi": "Khu du lịch Tam Đảo",
  "name_en": "Tam Dao Hill Station",
  "name_ru": "Горный курорт Тамдао",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 21.4583, "lon": 105.6447},
  "address_vi": "Thị trấn Tam Đảo, tỉnh Phú Thọ (Vĩnh Phúc cũ), cách Hà Nội khoảng 80 km",
  "rating": {"value": 4.4, "count": 12000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Điểm nghỉ mát gần Hà Nội, khí hậu mát lạnh, sương mù lãng mạn. Du khách thích nhà thờ đá cổ, quán cà phê view mây và ẩm thực rau su su, gà đồi; có người phàn nàn cuối tuần đông và hay mưa mù che tầm nhìn.",
  "presentation_short_vi": "Tam Đảo là thị trấn nghỉ mát trên độ cao khoảng 900 m giữa dãy núi Tam Đảo, được người Pháp xây dựng từ đầu thế kỷ 20. Khí hậu quanh năm mát mẻ, thường xuyên chìm trong sương mù bảng lảng, cùng nhà thờ đá cổ, thác Bạc và những đồi su su xanh mướt tạo nên khung cảnh lãng mạn rất được yêu thích.",
  "presentation_short_en": "Tam Dao is a hill-station town at around 900 m amid the Tam Dao range, built by the French in the early 20th century. Cool all year and often wrapped in drifting mist, with its old stone church, Silver Waterfall and green terraces of chayote, it offers a romantic scenery that draws many weekenders from Hanoi.",
  "presentation_short_ru": "Тамдао — курортный городок на высоте около 900 м среди хребта Тамдао, построенный французами в начале XX века. Прохладный круглый год и часто окутанный дымкой тумана, со старой каменной церковью, Серебряным водопадом и зелёными террасами чайота, он дарит романтичные виды и привлекает множество гостей из Ханоя.",
  "presentation_long_vi": "Nằm cách Hà Nội khoảng 80 km, thị trấn Tam Đảo tọa lạc trên một thung lũng nhỏ ở độ cao chừng 900 m thuộc dãy núi Tam Đảo, nay thuộc tỉnh Phú Thọ (địa phận Vĩnh Phúc cũ). Được người Pháp phát hiện và xây dựng thành nơi nghỉ dưỡng từ những năm 1900, Tam Đảo có khí hậu ôn hòa đặc trưng: một ngày có thể mang đủ bốn mùa, thường xuyên mờ ảo trong sương mù, ban đêm se lạnh ngay cả giữa mùa hè. Biểu tượng của thị trấn là nhà thờ đá cổ kính rêu phong nằm trên sườn dốc, nơi du khách hay dừng chân chụp ảnh và ngắm mây. Từ đây có nhiều tuyến khám phá như leo bậc thang xuống thác Bạc tung bọt trắng giữa rừng, chinh phục đỉnh Rùng Rình, tháp truyền hình trên đỉnh cao nhất, hay tản bộ giữa những vườn su su xanh mướt đặc sản của vùng. Về đêm, thị trấn nhỏ lung linh ánh đèn, các quán cà phê và nhà hàng phục vụ món gà đồi, ngọn su su xào, lợn mán nướng ấm cúng. Không quá xa thủ đô, khí hậu mát lành và cảnh sắc thơ mộng khiến Tam Đảo trở thành lựa chọn nghỉ cuối tuần quen thuộc của người miền Bắc, nhất là các cặp đôi và gia đình.",
  "presentation_long_en": "About 80 km from Hanoi, the town of Tam Dao sits in a small valley at some 900 m in the Tam Dao range, now within Phu Tho province (formerly Vinh Phuc). Discovered and developed by the French as a resort from the 1900s, Tam Dao has a distinctive mild climate: a single day can hold all four seasons, mist drifts through constantly, and the nights are cool even in midsummer. The town's emblem is the mossy old stone church on the slope, a favourite spot to pause for photos and watch the clouds. From here run many trails: steps down to the Silver Waterfall foaming white in the forest, the climb to Rung Rinh Peak, the television tower on the highest summit, or a stroll among the green chayote gardens that are a local speciality. At night the little town glitters with lights, and cafes and restaurants serve hill chicken, stir-fried chayote shoots and grilled highland pork in a cosy atmosphere. Close to the capital, cool and dreamily scenic, Tam Dao has become a familiar weekend choice for northerners, especially couples and families.",
  "presentation_long_ru": "Примерно в 80 км от Ханоя городок Тамдао расположен в небольшой долине на высоте около 900 м в хребте Тамдао, ныне в составе провинции Футхо (прежде Виньфук). Открытый и обустроенный французами как курорт с 1900-х годов, Тамдао отличается мягким климатом: за один день здесь можно ощутить все четыре сезона, постоянно плывёт туман, а ночи прохладны даже в разгар лета. Символ городка — поросшая мхом старая каменная церковь на склоне, любимое место для фотографий и созерцания облаков. Отсюда расходятся многие тропы: ступени к Серебряному водопаду, пенящемуся белым в лесу, подъём на пик Рунгринь, телебашня на самой высокой вершине или прогулка среди зелёных огородов чайота — местного деликатеса. Ночью маленький город мерцает огнями, а кафе и рестораны в уютной обстановке подают горную курицу, обжаренные побеги чайота и жареную горную свинину. Недалеко от столицы, прохладный и мечтательно живописный, Тамдао стал привычным выбором северян для выходных, особенно пар и семей. Многие приезжают сюда просто ради тишины: посидеть в кафе с видом на облака, пройтись по влажным от тумана улочкам и почувствовать, как быстро в горах меняется погода.",
  "highlights_vi": [
    "Thị trấn nghỉ mát trên 900 m do người Pháp xây, một ngày đủ bốn mùa",
    "Nhà thờ đá cổ rêu phong biểu tượng và thác Bạc giữa rừng",
    "Đặc sản ngọn su su, gà đồi; cảnh mây mù lãng mạn gần Hà Nội"
  ],
  "highlights_en": [
    "A hill-station town above 900 m built by the French, four seasons in a day",
    "Iconic mossy old stone church and the Silver Waterfall in the forest",
    "Chayote shoots and hill chicken; romantic misty scenery near Hanoi"
  ],
  "highlights_ru": [
    "Курортный городок выше 900 м, построенный французами; четыре сезона за день",
    "Знаковая старая каменная церковь во мху и Серебряный водопад в лесу",
    "Побеги чайота и горная курица; романтичные туманы недалеко от Ханоя"
  ],
  "practical": {
    "hours_vi": "Thị trấn mở cả ngày; các điểm dịch vụ theo giờ riêng.",
    "ticket_vi": "Không có vé chung; một số điểm (thác Bạc, khu vui chơi) có phí nhỏ.",
    "duration_vi": "1–2 ngày (nên nghỉ đêm).",
    "best_time_vi": "Mùa hè (tháng 5–9) để tránh nóng đồng bằng.",
    "tips_vi": "Mang áo khoác nhẹ; đặt phòng sớm dịp cuối tuần; đề phòng đường trơn khi sương mù."
  },
  "tags": ["mountain", "cool-climate", "nature", "romantic", "daytrip", "top"],
  "sources": [{"title": "Wikipedia (VI) — Tam Đảo (thị trấn)", "url": "https://vi.wikipedia.org/wiki/Tam_%C4%90%E1%BA%A3o_(th%E1%BB%8B_tr%E1%BA%A5n)"}]
})

add({
  "region": "vn-phu-tho", "slug": "tay-thien",
  "region_name_vi": "Phú Thọ", "federal_district": "Miền Bắc",
  "name_vi": "Danh thắng Tây Thiên",
  "name_en": "Tay Thien Scenic and Spiritual Complex",
  "name_ru": "Комплекс Тэйтхьен",
  "categories": ["church", "park_garden"],
  "coordinates": {"lat": 21.5906, "lon": 105.5906},
  "address_vi": "Xã Đại Đình, tỉnh Phú Thọ (Vĩnh Phúc cũ), trong dãy Tam Đảo",
  "rating": {"value": 4.5, "count": 6000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Quần thể đền chùa linh thiêng giữa rừng núi Tam Đảo; du khách khen cáp treo tiện, cảnh suối thác đẹp và thiền viện thanh tịnh. Ngày lễ hội đầu xuân đông đúc; leo bộ khá dốc nên nhiều người chọn cáp treo.",
  "presentation_short_vi": "Tây Thiên là quần thể danh thắng và tâm linh nằm trên sườn dãy Tam Đảo, vừa là nơi thờ Quốc Mẫu Tây Thiên Lăng Thị Tiêu, vừa được xem là một trong những cái nôi của Phật giáo Việt Nam. Du khách hành hương qua hệ thống đền, chùa, thiền viện giữa rừng suối, có thể đi bộ hoặc dùng cáp treo.",
  "presentation_short_en": "Tay Thien is a scenic and spiritual complex on the slopes of the Tam Dao range, both a shrine to the National Mother Tay Thien and regarded as one of the cradles of Buddhism in Vietnam. Pilgrims move through temples, pagodas and a Zen monastery amid forest and streams, on foot or by cable car.",
  "presentation_short_ru": "Тэйтхьен — живописно-духовный комплекс на склонах хребта Тамдао, одновременно святилище Национальной Матери Тэйтхьен и одна из колыбелей буддизма во Вьетнаме. Паломники проходят через храмы, пагоды и дзен-монастырь среди леса и ручьёв — пешком или по канатной дороге.",
  "presentation_long_vi": "Nằm trên sườn tây nam dãy Tam Đảo, thuộc tỉnh Phú Thọ (địa phận Vĩnh Phúc cũ), Tây Thiên là một quần thể di tích và thắng cảnh nổi tiếng miền Bắc, độc đáo ở chỗ hòa quyện cả tín ngưỡng thờ Mẫu bản địa lẫn Phật giáo. Tương truyền nơi đây thờ Quốc Mẫu Tây Thiên Lăng Thị Tiêu, người có công giúp vua Hùng dựng nước và dạy dân trồng lúa; đồng thời Tây Thiên được coi là một trong những nơi Phật giáo được truyền vào Việt Nam từ rất sớm. Con đường hành hương men theo dòng suối Giải Oan và Bát Nhã, xuyên qua rừng cây cổ thụ, dẫn lên đền Thõng, đền Cậu, đền Cô, đền Thượng và Thiền viện Trúc Lâm Tây Thiên bề thế trên cao. Du khách có thể chọn leo bộ hàng nghìn bậc đá để cảm nhận trọn vẹn không gian rừng núi, tiếng suối reo, hoặc đi cáp treo vượt qua thung lũng để tiết kiệm sức. Vào dịp đầu xuân, lễ hội Tây Thiên kéo dài nhiều ngày thu hút đông đảo Phật tử và du khách thập phương về chiêm bái. Với sự kết hợp giữa cảnh quan rừng nguyên sinh, suối thác trong lành và chiều sâu văn hóa – tâm linh, Tây Thiên là điểm đến lý tưởng cho hành hương kết hợp vãn cảnh, tĩnh tâm.",
  "presentation_long_en": "On the south-western slopes of the Tam Dao range in Phu Tho province (formerly Vinh Phuc), Tay Thien is a celebrated complex of relics and scenery in the north, distinctive for blending indigenous Mother-Goddess worship with Buddhism. Tradition holds that it enshrines the National Mother Tay Thien Lang Thi Tieu, who helped a Hung King build the nation and taught the people to grow rice; Tay Thien is also considered one of the places where Buddhism entered Vietnam very early. The pilgrimage path follows the Giai Oan and Bat Nha streams through ancient forest up to the Thong, Cau, Co and Upper temples and the imposing Truc Lam Tay Thien Zen monastery on the heights. Visitors may climb thousands of stone steps to savour the mountain forest and murmuring streams, or take the cable car across the valley to save their strength. In early spring the Tay Thien festival runs for several days, drawing crowds of Buddhists and travellers to pay homage. With its blend of old-growth forest, clear streams and waterfalls, and cultural-spiritual depth, Tay Thien is an ideal destination for pilgrimage combined with sightseeing and quiet reflection.",
  "presentation_long_ru": "На юго-западных склонах хребта Тамдао в провинции Футхо (прежде Виньфук) Тэйтхьен — прославленный на севере комплекс памятников и природы, своеобразный тем, что соединяет местный культ Матери-богини с буддизмом. По преданию, здесь почитают Национальную Мать Тэйтхьен Ланг Тхи Тиеу, которая помогала королю Хунг строить страну и учила народ выращивать рис; Тэйтхьен также считают одним из мест, куда буддизм проник во Вьетнам очень рано. Паломническая тропа идёт вдоль ручьёв Зяйоан и Батня сквозь древний лес к храмам Тхонг, Кау, Ко и Верхнему, а также к внушительному дзен-монастырю Чуклам Тэйтхьен на высотах. Гости могут подняться по тысячам каменных ступеней, чтобы вполне ощутить горный лес и журчание ручьёв, либо проехать на канатной дороге через долину, сберегая силы. Ранней весной многодневный праздник Тэйтхьен собирает толпы буддистов и путешественников для поклонения. Сочетая девственный лес, чистые ручьи и водопады с культурно-духовной глубиной, Тэйтхьен — идеальное место для паломничества вместе с осмотром и тихим размышлением. Паломники обычно поднимаются неспешно, останавливаясь у каждого святилища, чтобы зажечь благовония, а с верхних площадок открывается вид на уходящие вдаль лесистые склоны Тамдао.",
  "highlights_vi": [
    "Hòa quyện tín ngưỡng thờ Quốc Mẫu và Phật giáo giữa rừng núi Tam Đảo",
    "Hệ thống đền, chùa và Thiền viện Trúc Lâm Tây Thiên bề thế trên cao",
    "Có cáp treo và đường leo bộ qua suối Giải Oan, Bát Nhã"
  ],
  "highlights_en": [
    "Blends Mother-Goddess worship and Buddhism amid the Tam Dao forest",
    "Temples, pagodas and the grand Truc Lam Tay Thien Zen monastery on the heights",
    "Cable car and a walking trail along the Giai Oan and Bat Nha streams"
  ],
  "highlights_ru": [
    "Соединяет культ Матери-богини и буддизм среди леса Тамдао",
    "Храмы, пагоды и внушительный дзен-монастырь Чуклам Тэйтхьен на высотах",
    "Канатная дорога и пешая тропа вдоль ручьёв Зяйоан и Батня"
  ],
  "practical": {
    "hours_vi": "Khoảng 6:00–18:00; cáp treo theo giờ vận hành.",
    "ticket_vi": "Cáp treo khứ hồi tham khảo khoảng 200.000–300.000 VND; xe điện có phí riêng.",
    "duration_vi": "Khoảng nửa ngày.",
    "best_time_vi": "Đầu xuân (mùa lễ hội) hoặc ngày thường để yên tĩnh.",
    "tips_vi": "Đi giày leo núi nếu chọn đường bộ; mang nước; ăn mặc lịch sự khi vào đền chùa."
  },
  "tags": ["temple", "pilgrimage", "nature", "cable-car", "mountain", "top"],
  "sources": [{"title": "Wikipedia (VI) — Tây Thiên (khu di tích)", "url": "https://vi.wikipedia.org/wiki/T%C3%A2y_Thi%C3%AAn"}]
})

add({
  "region": "vn-phu-tho", "slug": "mai-chau",
  "region_name_vi": "Phú Thọ", "federal_district": "Miền Bắc",
  "name_vi": "Thung lũng Mai Châu",
  "name_en": "Mai Chau Valley",
  "name_ru": "Долина Майтяу",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 20.6600, "lon": 105.0900},
  "address_vi": "Khu vực Mai Châu, tỉnh Phú Thọ (Hòa Bình cũ), cách Hà Nội khoảng 140 km",
  "rating": {"value": 4.5, "count": 5000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Thung lũng thanh bình với bản làng người Thái, nhà sàn, ruộng lúa và xe đạp dạo quanh. Du khách thích homestay ấm cúng, múa xòe, cơm lam; đường đèo Thung Khe lên Mai Châu đẹp nhưng nhiều sương.",
  "presentation_short_vi": "Mai Châu là thung lũng yên bình nằm giữa những dãy núi đá vôi, nổi tiếng với bản làng người Thái trắng, nhà sàn truyền thống và cánh đồng lúa xanh mướt. Du khách đến đây để nghỉ homestay, đạp xe qua các bản Lác, bản Pom Coọng, xem múa xòe và thưởng thức ẩm thực dân tộc.",
  "presentation_short_en": "Mai Chau is a peaceful valley cradled by limestone ranges, famous for its White Thai villages, traditional stilt houses and lush green rice fields. Visitors come to stay in homestays, cycle through hamlets such as Lac and Pom Coong, watch xoe dances and enjoy ethnic-minority cuisine.",
  "presentation_short_ru": "Майтяу — тихая долина в объятиях известняковых гряд, знаменитая деревнями белых тай, традиционными свайными домами и сочными зелёными рисовыми полями. Гости приезжают, чтобы остановиться в homestay, покататься на велосипеде по деревушкам Лак и Помконг, посмотреть танцы соэ и попробовать кухню национальных меньшинств.",
  "presentation_long_vi": "Cách Hà Nội khoảng 140 km về phía tây, thung lũng Mai Châu thuộc tỉnh Phú Thọ (địa phận Hòa Bình cũ) mở ra như một bức tranh đồng quê thanh bình sau khi vượt qua đèo Thung Khe quanh co, mờ sương. Bao quanh bởi những dãy núi đá vôi trùng điệp, lòng thung là các bản làng của người Thái trắng với những nếp nhà sàn gỗ mộc mạc, xen giữa ruộng lúa, nương ngô và vườn cây. Nổi tiếng nhất là bản Lác và bản Pom Coọng, nơi phát triển mô hình du lịch cộng đồng: du khách ngủ nhà sàn, thuê xe đạp thong dong trên những con đường nhỏ giữa cánh đồng, ghé các khung dệt thổ cẩm truyền thống và mua đồ lưu niệm dệt tay. Buổi tối, bên bếp lửa nhà sàn, khách được mời rượu cần, thưởng thức cơm lam, gà đồi, cá suối và xem những điệu múa xòe, múa sạp rộn ràng của các cô gái Thái. Không khí trong lành, nhịp sống chậm rãi cùng sự thân thiện của người dân khiến Mai Châu trở thành điểm nghỉ dưỡng, trải nghiệm văn hóa được yêu thích, đặc biệt hợp với những ai muốn tạm rời phố thị để hòa mình vào thiên nhiên và bản sắc vùng cao.",
  "presentation_long_en": "About 140 km west of Hanoi, Mai Chau Valley in Phu Tho province (formerly Hoa Binh) opens like a serene rural painting after the winding, misty Thung Khe Pass. Ringed by rolling limestone ranges, its floor holds White Thai villages of plain wooden stilt houses set among rice paddies, maize plots and gardens. Best known are Lac and Pom Coong hamlets, which have developed community-based tourism: guests sleep in stilt houses, rent bicycles to wander the little lanes across the fields, visit traditional brocade looms and buy handwoven souvenirs. In the evening, around the hearth of a stilt house, visitors are offered rice wine drunk through reeds and served bamboo-tube rice, hill chicken and stream fish, while Thai girls perform lively xoe and bamboo-pole dances. Fresh air, an unhurried pace and the warmth of the locals have made Mai Chau a beloved place to rest and experience culture, especially suited to those who wish to leave the city behind and immerse themselves in nature and highland identity.",
  "presentation_long_ru": "Примерно в 140 км к западу от Ханоя долина Майтяу в провинции Футхо (прежде Хоабинь) открывается как безмятежная сельская картина после извилистого, туманного перевала Тхунгкхе. Окружённая волнистыми известняковыми грядами, её дно занимают деревни белых тай с простыми деревянными свайными домами среди рисовых полей, кукурузных участков и садов. Наиболее известны деревушки Лак и Помконг, развившие общинный туризм: гости ночуют в свайных домах, берут напрокат велосипеды, чтобы бродить по узким тропам среди полей, заходят к традиционным ткацким станкам и покупают сувениры ручной работы. Вечером у очага свайного дома гостям предлагают рисовое вино, которое пьют через тростинки, подают рис в бамбуке, горную курицу и речную рыбу, а девушки тай исполняют живые танцы соэ и танцы с бамбуковыми шестами. Свежий воздух, неспешный ритм и радушие местных сделали Майтяу любимым местом отдыха и знакомства с культурой, особенно для тех, кто хочет оставить город позади и погрузиться в природу и самобытность высокогорья. Многие гости берут велосипед напрокат уже на рассвете, чтобы застать поля в мягком свете и туман, поднимающийся над рисом, — один из самых запоминающихся образов долины.",
  "highlights_vi": [
    "Thung lũng bình yên với bản Thái trắng, nhà sàn và ruộng lúa xanh",
    "Du lịch cộng đồng bản Lác, bản Pom Coọng: ngủ nhà sàn, đạp xe, dệt thổ cẩm",
    "Múa xòe, múa sạp, rượu cần và ẩm thực dân tộc bên bếp lửa"
  ],
  "highlights_en": [
    "Peaceful valley of White Thai villages, stilt houses and green rice fields",
    "Community tourism in Lac and Pom Coong: stilt-house stays, cycling, brocade weaving",
    "Xoe and bamboo-pole dances, reed wine and ethnic cuisine by the hearth"
  ],
  "highlights_ru": [
    "Тихая долина деревень белых тай, свайных домов и зелёных рисовых полей",
    "Общинный туризм в Лак и Помконг: ночлег в свайных домах, велосипед, ткачество",
    "Танцы соэ и с бамбуковыми шестами, вино через тростинки и кухня меньшинств"
  ],
  "practical": {
    "hours_vi": "Bản làng mở cả ngày; homestay nhận khách theo đặt trước.",
    "ticket_vi": "Vé vào bản tham khảo khoảng 10.000–20.000 VND; thuê xe đạp giá rẻ.",
    "duration_vi": "1–2 ngày (nên nghỉ đêm nhà sàn).",
    "best_time_vi": "Tháng 9–11 lúa chín; mùa xuân hoa nở.",
    "tips_vi": "Đặt homestay trước dịp cuối tuần; mang tiền mặt; tôn trọng phong tục địa phương."
  },
  "tags": ["valley", "ethnic-culture", "homestay", "cycling", "nature", "top"],
  "sources": [{"title": "Wikipedia (VI) — Mai Châu", "url": "https://vi.wikipedia.org/wiki/Mai_Ch%C3%A2u"}]
})

add({
  "region": "vn-phu-tho", "slug": "thuy-dien-hoa-binh",
  "region_name_vi": "Phú Thọ", "federal_district": "Miền Bắc",
  "name_vi": "Nhà máy Thủy điện Hòa Bình",
  "name_en": "Hoa Binh Hydropower Plant",
  "name_ru": "Гидроэлектростанция Хоабинь",
  "categories": ["monument", "other"],
  "coordinates": {"lat": 20.8133, "lon": 105.3283},
  "address_vi": "Phường Hòa Bình, tỉnh Phú Thọ (Hòa Bình cũ), trên sông Đà",
  "rating": {"value": 4.5, "count": 4000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Công trình thế kỷ trên sông Đà, tượng đài Bác Hồ và đài tưởng niệm các chuyên gia Liên Xô gây ấn tượng. Du khách thích view hồ, đập tràn xả lũ hùng vĩ và nhà truyền thống; khu vực nhà máy cần tuân thủ quy định an ninh.",
  "presentation_short_vi": "Nhà máy Thủy điện Hòa Bình trên sông Đà từng là công trình thủy điện lớn nhất Đông Nam Á, được xây dựng với sự giúp đỡ của Liên Xô trong thập niên 1980. Du khách có thể ngắm con đập khổng lồ, tượng đài Chủ tịch Hồ Chí Minh trên đồi, đài tưởng niệm các chuyên gia và bức thư gửi thế hệ mai sau.",
  "presentation_short_en": "The Hoa Binh Hydropower Plant on the Da River was once the largest hydroelectric project in Southeast Asia, built with Soviet assistance in the 1980s. Visitors can view the huge dam, the statue of President Ho Chi Minh on the hill, the memorial to the experts and the famous letter sealed for future generations.",
  "presentation_short_ru": "Гидроэлектростанция Хоабинь на реке Да когда-то была крупнейшим гидроэнергетическим объектом Юго-Восточной Азии и построена при помощи СССР в 1980-е годы. Гости могут увидеть огромную плотину, статую президента Хо Ши Мина на холме, мемориал специалистам и знаменитое письмо, запечатанное для будущих поколений.",
  "presentation_long_vi": "Nằm trên sông Đà, Nhà máy Thủy điện Hòa Bình thuộc tỉnh Phú Thọ (địa phận Hòa Bình cũ) là một biểu tượng của tình hữu nghị Việt – Xô và của công cuộc công nghiệp hóa đất nước. Được khởi công năm 1979 và hoàn thành năm 1994 với sự giúp đỡ to lớn của các chuyên gia Liên Xô, trong nhiều năm đây là nhà máy thủy điện lớn nhất Việt Nam và cả Đông Nam Á, giữ vai trò then chốt trong cung cấp điện, chống lũ và điều tiết nước cho vùng đồng bằng Bắc Bộ. Đến tham quan, du khách choáng ngợp trước con đập bê tông khổng lồ chắn ngang dòng Đà và mặt hồ mênh mông phía thượng lưu; những dịp xả lũ, dòng nước cuồn cuộn tung bọt trắng tạo nên cảnh tượng hùng vĩ. Trên đồi Ông Tượng gần đó là tượng đài Chủ tịch Hồ Chí Minh cao lớn, hướng nhìn ra công trình. Trong khuôn viên còn có đài tưởng niệm những công nhân, chuyên gia Việt Nam và Liên Xô đã hy sinh khi xây dựng nhà máy, cùng tấm bia đặt 'bức thư gửi thế hệ mai sau' dự kiến mở vào năm 2100. Kết hợp giữa quy mô kỹ thuật, ý nghĩa lịch sử và cảnh quan sông hồ, thủy điện Hòa Bình là điểm dừng chân độc đáo trên hành trình khám phá vùng Tây Bắc.",
  "presentation_long_en": "On the Da River, the Hoa Binh Hydropower Plant in Phu Tho province (formerly Hoa Binh) is a symbol of Vietnamese–Soviet friendship and of the country's industrialisation. Begun in 1979 and completed in 1994 with major help from Soviet experts, it was for many years the largest hydroelectric plant in Vietnam and in Southeast Asia, playing a key role in supplying power, controlling floods and regulating water for the northern delta. Visitors are awed by the vast concrete dam barring the Da River and the immense reservoir upstream; during flood discharges the surging, foaming water makes a majestic sight. On nearby Ong Tuong Hill stands a large statue of President Ho Chi Minh, gazing over the works. Within the grounds are a memorial to the Vietnamese and Soviet workers and specialists who died building the plant, and a stele holding a 'letter to future generations' due to be opened in 2100. Combining engineering scale, historical meaning and river-and-lake scenery, Hoa Binh Hydropower is a distinctive stop on a journey through the north-west.",
  "presentation_long_ru": "На реке Да гидроэлектростанция Хоабинь в провинции Футхо (прежде Хоабинь) — символ вьетнамско-советской дружбы и индустриализации страны. Начатая в 1979 году и завершённая в 1994-м при большой помощи советских специалистов, она долгие годы была крупнейшей ГЭС во Вьетнаме и во всей Юго-Восточной Азии, играя ключевую роль в снабжении электроэнергией, защите от наводнений и регулировании воды для северной дельты. Гостей поражает огромная бетонная плотина, перегородившая Да, и необъятное водохранилище выше по течению; при сбросе воды бурлящий, пенящийся поток создаёт величественное зрелище. На соседнем холме Онгтыонг стоит большая статуя президента Хо Ши Мина, обращённая к сооружению. На территории есть мемориал вьетнамским и советским рабочим и специалистам, погибшим при строительстве, и стела с «письмом будущим поколениям», которое должны вскрыть в 2100 году. Соединяя инженерный размах, историческое значение и виды реки и озера, ГЭС Хоабинь — необычная остановка на пути по северо-западу. Со смотровых площадок хорошо виден размах сооружения и спокойная гладь водохранилища между горами, а для многих вьетнамцев это место связано с гордостью за совместный труд двух народов.",
  "highlights_vi": [
    "Từng là nhà máy thủy điện lớn nhất Đông Nam Á, biểu tượng hữu nghị Việt – Xô",
    "Đập bê tông khổng lồ trên sông Đà, cảnh xả lũ hùng vĩ",
    "Tượng đài Bác Hồ, đài tưởng niệm chuyên gia và 'bức thư gửi thế hệ mai sau' (mở năm 2100)"
  ],
  "highlights_en": [
    "Once Southeast Asia's largest hydro plant, a symbol of Vietnamese–Soviet friendship",
    "A giant concrete dam on the Da River with dramatic flood discharges",
    "Ho Chi Minh statue, experts' memorial and a 'letter to the future' to open in 2100"
  ],
  "highlights_ru": [
    "Когда-то крупнейшая ГЭС Юго-Восточной Азии, символ вьетнамско-советской дружбы",
    "Гигантская бетонная плотина на реке Да с впечатляющими сбросами воды",
    "Статуя Хо Ши Мина, мемориал специалистам и «письмо будущему», вскрытие в 2100 году"
  ],
  "practical": {
    "hours_vi": "Khu tượng đài, nhà truyền thống mở ban ngày; nhà máy tham quan theo đoàn/đăng ký.",
    "ticket_vi": "Khu vực ngoài trời thường miễn phí; tham quan bên trong cần đăng ký.",
    "duration_vi": "Khoảng 1–2 giờ.",
    "best_time_vi": "Mùa xả lũ (khoảng tháng 7–9) để xem cảnh xả nước; quanh năm cho tham quan chung.",
    "tips_vi": "Tuân thủ quy định an ninh khu vực nhà máy; kết hợp lên đồi Ông Tượng ngắm toàn cảnh."
  },
  "tags": ["engineering", "history", "viewpoint", "river", "monument"],
  "sources": [{"title": "Wikipedia (VI) — Nhà máy thủy điện Hòa Bình", "url": "https://vi.wikipedia.org/wiki/Nh%C3%A0_m%C3%A1y_th%E1%BB%A7y_%C4%91i%E1%BB%87n_H%C3%B2a_B%C3%ACnh"}]
})

# ---------- HÀ TĨNH ----------
add({
  "region": "vn-ha-tinh", "slug": "nga-ba-dong-loc",
  "region_name_vi": "Hà Tĩnh", "federal_district": "Miền Trung",
  "name_vi": "Khu di tích Ngã ba Đồng Lộc",
  "name_en": "Dong Loc Junction Memorial",
  "name_ru": "Мемориал перекрёстка Донглок",
  "categories": ["monument", "museum"],
  "coordinates": {"lat": 18.4839, "lon": 105.6208},
  "address_vi": "Xã Đồng Lộc, tỉnh Hà Tĩnh (trên đường Trường Sơn)",
  "rating": {"value": 4.7, "count": 6000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Địa chỉ đỏ xúc động, nơi tưởng niệm 10 nữ thanh niên xung phong hy sinh năm 1968. Du khách lặng người trước khu mộ và tháp chuông; nhiều đoàn về dâng hương, tìm hiểu lịch sử. Không gian trang nghiêm, được chăm sóc chu đáo.",
  "presentation_short_vi": "Ngã ba Đồng Lộc là 'tọa độ lửa' trên tuyến đường Trường Sơn thời kháng chiến chống Mỹ, nơi 10 cô gái thanh niên xung phong đã anh dũng hy sinh năm 1968 khi tuổi đời còn rất trẻ. Khu di tích gồm khu mộ 10 cô, nhà bia, tháp chuông và nhà truyền thống, là địa chỉ tưởng niệm thiêng liêng.",
  "presentation_short_en": "Dong Loc Junction was a 'coordinate of fire' on the Truong Son (Ho Chi Minh) Trail during the war against the United States, where ten young female volunteers died heroically in 1968, most still in their teens or twenties. The memorial includes their ten graves, a stele house, a bell tower and a museum, forming a sacred place of remembrance.",
  "presentation_short_ru": "Перекрёсток Донглок был «координатой огня» на тропе Чыонгшон (тропе Хо Ши Мина) во время войны против США, где в 1968 году героически погибли десять юных девушек-добровольцев, большинству из которых не было и двадцати пяти. Мемориал включает их десять могил, павильон со стелой, колокольню и музей — священное место памяти.",
  "presentation_long_vi": "Ngã ba Đồng Lộc thuộc tỉnh Hà Tĩnh là một trong những địa danh bi tráng và thiêng liêng nhất của cuộc kháng chiến chống Mỹ. Trong những năm 1965–1968, đây là nút giao thông huyết mạch trên tuyến đường Trường Sơn nối hậu phương miền Bắc với chiến trường miền Nam, nên trở thành mục tiêu đánh phá ác liệt của không quân Mỹ. Người ta ước tính mỗi mét vuông đất nơi đây từng hứng chịu nhiều quả bom, biến ngã ba thành một 'tọa độ lửa'. Bất chấp mưa bom, các lực lượng thanh niên xung phong, bộ đội, công nhân giao thông vẫn ngày đêm bám trụ, san lấp hố bom, bảo đảm cho đoàn xe ra tiền tuyến. Ngày 24 tháng 7 năm 1968, một tiểu đội gồm 10 cô gái thanh niên xung phong tuổi từ 17 đến 24, do chị Võ Thị Tần làm tiểu đội trưởng, đã hy sinh khi một quả bom rơi trúng nơi các chị đang làm nhiệm vụ. Sự hy sinh của các chị trở thành biểu tượng cho lòng quả cảm và tuổi thanh xuân hiến dâng cho Tổ quốc. Ngày nay, khu di tích quốc gia đặc biệt Ngã ba Đồng Lộc gồm khu mộ 10 nữ liệt sĩ, tháp chuông, nhà bia tưởng niệm và nhà truyền thống trưng bày hiện vật, là nơi các thế hệ về dâng hương, tri ân và giáo dục truyền thống.",
  "presentation_long_en": "Dong Loc Junction in Ha Tinh province is one of the most tragic and sacred sites of the war against the United States. Between 1965 and 1968 it was a vital road junction on the Truong Son Trail linking the northern rear to the southern front, and so became a target of relentless US air raids. It is estimated that every square metre here absorbed many bombs, turning the crossroads into a 'coordinate of fire'. Despite the bombing, youth volunteers, soldiers and road workers held their ground day and night, filling craters to keep convoys moving to the front. On 24 July 1968 a squad of ten young female volunteers aged from 17 to 24, led by Vo Thi Tan, were killed when a bomb struck the spot where they were working. Their sacrifice became a symbol of courage and of youth given to the homeland. Today the special national relic site of Dong Loc includes the graves of the ten martyrs, a bell tower, a memorial stele house and a museum displaying artefacts, where generations come to offer incense, give thanks and learn their history.",
  "presentation_long_ru": "Перекрёсток Донглок в провинции Хатинь — одно из самых трагических и священных мест войны против США. В 1965–1968 годах это был жизненно важный дорожный узел на тропе Чыонгшон, связывавшей северный тыл с южным фронтом, и потому он стал целью непрерывных американских авианалётов. Считается, что каждый квадратный метр здесь принял множество бомб, превратив перекрёсток в «координату огня». Несмотря на бомбёжки, молодёжные добровольцы, солдаты и дорожные рабочие держались день и ночь, засыпая воронки, чтобы колонны шли к фронту. 24 июля 1968 года отделение из десяти девушек-добровольцев в возрасте от 17 до 24 лет во главе с Во Тхи Тан погибло, когда бомба попала в место их работы. Их жертва стала символом мужества и молодости, отданной родине. Сегодня особый национальный мемориал Донглок включает могилы десяти мучениц, колокольню, павильон со стелой и музей с артефактами, куда поколения приходят возжечь благовония, поблагодарить и узнать их историю. Многие приезжие оставляют у могил цветы, зеркальца и гребни — трогательная традиция в память о погибших молодых женщинах.",
  "highlights_vi": [
    "'Tọa độ lửa' trên đường Trường Sơn, hứng chịu bom đạn ác liệt 1965–1968",
    "Nơi tưởng niệm 10 nữ thanh niên xung phong hy sinh ngày 24/7/1968",
    "Khu di tích quốc gia đặc biệt: khu mộ, tháp chuông, nhà truyền thống"
  ],
  "highlights_en": [
    "A 'coordinate of fire' on the Truong Son Trail, heavily bombed in 1965–1968",
    "Memorial to ten young female volunteers who died on 24 July 1968",
    "Special national relic site: the graves, a bell tower and a museum"
  ],
  "highlights_ru": [
    "«Координата огня» на тропе Чыонгшон, сильно бомбившаяся в 1965–1968",
    "Мемориал десяти девушкам-добровольцам, погибшим 24 июля 1968 года",
    "Особый национальный памятник: могилы, колокольня и музей"
  ],
  "practical": {
    "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
    "ticket_vi": "Vào cửa miễn phí; có thể công đức tùy tâm.",
    "duration_vi": "Khoảng 1–1,5 giờ.",
    "best_time_vi": "Quanh năm; dịp 27/7 (Ngày Thương binh – Liệt sĩ) rất trang trọng.",
    "tips_vi": "Ăn mặc lịch sự, giữ trật tự trang nghiêm; nên nghe thuyết minh để hiểu sâu câu chuyện."
  },
  "tags": ["history", "memorial", "war", "monument", "education"],
  "sources": [{"title": "Wikipedia (VI) — Ngã ba Đồng Lộc", "url": "https://vi.wikipedia.org/wiki/Ng%C3%A3_ba_%C4%90%E1%BB%93ng_L%E1%BB%99c"}]
})

add({
  "region": "vn-ha-tinh", "slug": "chua-huong-tich",
  "region_name_vi": "Hà Tĩnh", "federal_district": "Miền Trung",
  "name_vi": "Chùa Hương Tích (Hà Tĩnh)",
  "name_en": "Huong Tich Pagoda (Ha Tinh)",
  "name_ru": "Пагода Хыонгтить (Хатинь)",
  "categories": ["church", "park_garden"],
  "coordinates": {"lat": 18.4183, "lon": 105.6864},
  "address_vi": "Núi Hồng Lĩnh, xã Thiên Lộc, tỉnh Hà Tĩnh",
  "rating": {"value": 4.5, "count": 3000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Ngôi chùa cổ trên núi Hồng Lĩnh, được ví là 'Hoan Châu đệ nhất danh lam'. Du khách thích đi thuyền qua hồ, cáp treo và đường rừng lên chùa, cảnh non nước hữu tình; đầu xuân hành hương rất đông.",
  "presentation_short_vi": "Chùa Hương Tích ở Hà Tĩnh là ngôi cổ tự nằm trên lưng chừng núi Hồng Lĩnh, được mệnh danh 'Hoan Châu đệ nhất danh lam' và gắn với truyền thuyết công chúa Diệu Thiện tu hành hóa Phật. Đây được xem là chốn Hương Tích 'gốc', có trước chùa Hương ở Hà Nội, hành trình lên chùa qua hồ nước, cáp treo và rừng thông.",
  "presentation_short_en": "Huong Tich Pagoda in Ha Tinh is an ancient temple set on the slopes of Hong Linh Mountain, praised as the 'finest scenic site of Hoan Chau' and linked to the legend of Princess Dieu Thien who attained Buddhahood here. Regarded as the 'original' Huong Tich, older than the Perfume Pagoda near Hanoi, it is reached across a lake, by cable car and through pine forest.",
  "presentation_short_ru": "Пагода Хыонгтить в Хатине — древний храм на склонах горы Хонглинь, прославленный как «лучшее живописное место Хоантяу» и связанный с легендой о принцессе Зьеутхьен, достигшей здесь состояния будды. Считается «изначальной» Хыонгтить, более старой, чем Ароматная пагода под Ханоем; к ней добираются через озеро, по канатной дороге и сквозь сосновый лес.",
  "presentation_long_vi": "Tọa lạc ở độ cao khoảng 650 m trên dãy núi Hồng Lĩnh thuộc tỉnh Hà Tĩnh, chùa Hương Tích là một trong những ngôi chùa cổ và nổi tiếng bậc nhất miền Trung, từ xưa đã được ca ngợi là 'Hoan Châu đệ nhất danh lam' – thắng cảnh đẹp nhất vùng Hoan Châu. Tương truyền chùa gắn với truyền thuyết công chúa Diệu Thiện, con vua Sở Trang Vương, đã tới đây tu hành và đắc đạo thành Phật Bà Quan Âm. Nhiều nhà nghiên cứu cho rằng đây mới là chốn 'Hương Tích' nguyên gốc, còn chùa Hương ở Hà Nội là được 'mô phỏng' về sau. Hành trình lên chùa là một trải nghiệm thú vị: du khách đi thuyền qua hồ Nhà Đường phẳng lặng, sau đó có thể chọn leo bộ theo con đường rừng thông rợp mát hoặc đi cáp treo vượt sườn núi. Trên đường, du khách lần lượt qua các điểm như miếu Cô, am Thánh Mẫu, nền Trang Vương, rồi tới cụm chùa chính ẩn mình dưới vách đá, quanh năm mây phủ. Đứng từ sân chùa phóng tầm mắt ra xa là cảnh núi rừng trùng điệp và đồng bằng, sông nước Hà Tĩnh. Mỗi độ xuân về, lễ hội chùa Hương Tích khai hội, dòng người hành hương nô nức đổ về cầu an, vãn cảnh, khiến nơi đây vừa linh thiêng vừa nên thơ.",
  "presentation_long_en": "At about 650 m on the Hong Linh range in Ha Tinh province, Huong Tich Pagoda is one of the oldest and most famous temples in central Vietnam, long praised as the 'finest scenic site of Hoan Chau'. Tradition ties it to the legend of Princess Dieu Thien, daughter of a Chu king, who came here to practise and attained enlightenment as the Bodhisattva Quan Am. Many scholars argue that this is the 'original' Huong Tich, with the Perfume Pagoda near Hanoi a later imitation. The ascent is itself a pleasure: visitors cross the calm Nha Duong lake by boat, then either climb a shady pine-forest path or take a cable car over the mountainside. Along the way they pass shrines such as Co Temple, the Holy Mother's hermitage and the Trang Vuong terrace, before reaching the main cluster of halls tucked beneath cliffs and often veiled in cloud. From the temple yard the view stretches over ranges of forested hills and the plains and rivers of Ha Tinh. Each spring the Huong Tich festival opens and streams of pilgrims come to pray for peace and enjoy the scenery, making the site at once sacred and poetic.",
  "presentation_long_ru": "На высоте около 650 м на гряде Хонглинь в провинции Хатинь пагода Хыонгтить — один из старейших и самых знаменитых храмов центрального Вьетнама, издавна прославленный как «лучшее живописное место Хоантяу». Предание связывает её с легендой о принцессе Зьеутхьен, дочери чуского правителя, которая пришла сюда подвижничать и достигла просветления как бодхисаттва Куанам. Многие исследователи считают, что именно это — «изначальная» Хыонгтить, а Ароматная пагода под Ханоем — более позднее подражание. Сам подъём приятен: гости пересекают спокойное озеро Нядыонг на лодке, а затем либо идут по тенистой тропе через сосновый лес, либо едут по канатной дороге над склоном. По пути они минуют святилища — храм Ко, скит Святой Матери и террасу Чангвыонг, — прежде чем добраться до главного скопления залов, укрытых под скалами и часто окутанных облаками. Со двора храма открывается вид на гряды лесистых холмов и равнины и реки Хатиня. Каждую весну открывается праздник Хыонгтить, и потоки паломников приходят молиться о мире и любоваться пейзажем, отчего место одновременно священно и поэтично.",
  "highlights_vi": [
    "'Hoan Châu đệ nhất danh lam' trên núi Hồng Lĩnh, được xem là Hương Tích 'gốc'",
    "Gắn truyền thuyết công chúa Diệu Thiện tu hành hóa Phật Bà Quan Âm",
    "Hành trình đi thuyền qua hồ, cáp treo và đường rừng thông lên chùa"
  ],
  "highlights_en": [
    "The 'finest site of Hoan Chau' on Hong Linh Mountain, seen as the original Huong Tich",
    "Tied to the legend of Princess Dieu Thien becoming the Bodhisattva Quan Am",
    "Reached by boat across a lake, by cable car and through pine forest"
  ],
  "highlights_ru": [
    "«Лучшее место Хоантяу» на горе Хонглинь, считается изначальной Хыонгтить",
    "Связана с легендой о принцессе Зьеутхьен, ставшей бодхисаттвой Куанам",
    "Путь на лодке через озеро, по канатной дороге и сквозь сосновый лес"
  ],
  "practical": {
    "hours_vi": "Khoảng 6:00–18:00; cáp treo và thuyền theo giờ vận hành.",
    "ticket_vi": "Vé thắng cảnh, thuyền và cáp treo tính riêng, tổng tham khảo vài trăm nghìn đồng.",
    "duration_vi": "Khoảng nửa ngày.",
    "best_time_vi": "Đầu xuân (mùa lễ hội, từ tháng Giêng âm lịch).",
    "tips_vi": "Đi giày thoải mái nếu leo bộ; mang nước; tránh ngày cao điểm lễ hội nếu ngại đông."
  },
  "tags": ["temple", "pilgrimage", "mountain", "cable-car", "nature"],
  "sources": [{"title": "Wikipedia (VI) — Chùa Hương Tích (Hà Tĩnh)", "url": "https://vi.wikipedia.org/wiki/Ch%C3%B9a_H%C6%B0%C6%A1ng_T%C3%ADch_(H%C3%A0_T%C4%A9nh)"}]
})

add({
  "region": "vn-ha-tinh", "slug": "khu-luu-niem-nguyen-du",
  "region_name_vi": "Hà Tĩnh", "federal_district": "Miền Trung",
  "name_vi": "Khu di tích Đại thi hào Nguyễn Du",
  "name_en": "Nguyen Du Memorial Site",
  "name_ru": "Мемориал великого поэта Нгуен Зу",
  "categories": ["monument", "museum"],
  "coordinates": {"lat": 18.6472, "lon": 105.7953},
  "address_vi": "Xã Tiên Điền, huyện Nghi Xuân, tỉnh Hà Tĩnh",
  "rating": {"value": 4.5, "count": 1200, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Nơi tưởng niệm tác giả 'Truyện Kiều' – danh nhân văn hóa thế giới. Du khách thích không gian yên tĩnh, nhà trưng bày hiện vật dòng họ Nguyễn Tiên Điền và mộ Nguyễn Du; hợp với người yêu văn học.",
  "presentation_short_vi": "Khu di tích Nguyễn Du ở làng Tiên Điền, huyện Nghi Xuân, Hà Tĩnh là nơi tưởng niệm Đại thi hào Nguyễn Du – tác giả kiệt tác 'Truyện Kiều' và là Danh nhân văn hóa được thế giới vinh danh. Quần thể gồm khu mộ, nhà thờ, nhà trưng bày và nhiều di vật gắn với dòng họ Nguyễn Tiên Điền.",
  "presentation_short_en": "The Nguyen Du Memorial Site in Tien Dien village, Nghi Xuan district, Ha Tinh, honours the great poet Nguyen Du, author of the masterpiece 'The Tale of Kieu' and a world-recognised cultural figure. The complex includes his tomb, an ancestral shrine, an exhibition house and many relics of the Nguyen Tien Dien family.",
  "presentation_short_ru": "Мемориал Нгуен Зу в деревне Тьендьен уезда Нгисуан провинции Хатинь посвящён великому поэту Нгуен Зу — автору шедевра «Повесть о Киеу» и признанному в мире деятелю культуры. Комплекс включает его гробницу, родовое святилище, выставочный дом и множество реликвий семьи Нгуен Тьендьен.",
  "presentation_long_vi": "Nằm ở làng Tiên Điền, huyện Nghi Xuân, tỉnh Hà Tĩnh, Khu di tích Đại thi hào Nguyễn Du là nơi lưu giữ và tôn vinh cuộc đời, sự nghiệp của Nguyễn Du (1765–1820) – nhà thơ lớn nhất trong lịch sử văn học Việt Nam. Ông là tác giả của 'Đoạn trường tân thanh', quen gọi là 'Truyện Kiều', áng thơ Nôm 3.254 câu lục bát đã trở thành kiệt tác dân tộc, được dịch ra hàng chục thứ tiếng và ăn sâu vào đời sống văn hóa người Việt. Năm 1965, Nguyễn Du được Hội đồng Hòa bình thế giới tôn vinh, và năm 2013 ông được UNESCO vinh danh là Danh nhân văn hóa. Khu di tích trải rộng trên đất quê hương dòng họ Nguyễn Tiên Điền nổi tiếng khoa bảng, bao gồm phần mộ Đại thi hào, nhà thờ Nguyễn Du, đền thờ và các công trình của dòng họ, cùng nhà bảo tàng trưng bày nhiều tư liệu, hiện vật quý như nghiên bút, sắc phong, các bản 'Truyện Kiều' cổ và tài liệu nghiên cứu về ông. Không gian nơi đây trầm mặc, rợp bóng cây, gợi cảm giác vừa thành kính vừa gần gũi. Với những ai yêu văn chương, ghé thăm quê hương và nơi an nghỉ của tác giả 'Truyện Kiều' là một cuộc hành hương văn hóa đầy xúc động, giúp hiểu hơn về con người và thời đại đã sản sinh ra một trong những di sản văn học vĩ đại nhất của Việt Nam.",
  "presentation_long_en": "In Tien Dien village, Nghi Xuan district, Ha Tinh province, the Nguyen Du Memorial Site preserves and honours the life and work of Nguyen Du (1765–1820), the greatest poet in the history of Vietnamese literature. He wrote 'Doan Truong Tan Thanh', popularly known as 'The Tale of Kieu', a 3,254-line poem in native Nom script and the luc-bat verse form that became a national masterpiece, translated into dozens of languages and woven deeply into Vietnamese culture. In 1965 he was honoured by the World Peace Council, and in 2013 UNESCO recognised him as a cultural figure. The site spreads across the home ground of the scholarly Nguyen Tien Dien family and includes the poet's tomb, his ancestral shrine, family halls and a museum displaying precious documents and artefacts such as inkstones and brushes, royal decrees, old editions of 'The Tale of Kieu' and research materials about him. The grounds are quiet and shaded by trees, evoking both reverence and intimacy. For lovers of literature, visiting the birthplace and resting place of the author of 'The Tale of Kieu' is a moving cultural pilgrimage that deepens understanding of the man and the age that produced one of Vietnam's greatest literary treasures.",
  "presentation_long_ru": "В деревне Тьендьен уезда Нгисуан провинции Хатинь мемориал Нгуен Зу хранит и чтит жизнь и творчество Нгуен Зу (1765–1820), величайшего поэта в истории вьетнамской литературы. Он создал «Доан чыонг тан тхань», известную как «Повесть о Киеу», — поэму из 3254 строк на письме ном в размере лукбат, ставшую национальным шедевром, переведённую на десятки языков и глубоко вплетённую во вьетнамскую культуру. В 1965 году его почтил Всемирный совет мира, а в 2013-м ЮНЕСКО признала его деятелем культуры. Мемориал раскинулся на родине учёного рода Нгуен Тьендьен и включает гробницу поэта, его родовое святилище, семейные залы и музей с ценными документами и предметами — тушечницами и кистями, императорскими указами, старыми изданиями «Повести о Киеу» и исследованиями о нём. Территория тиха и затенена деревьями, вызывая и благоговение, и близость. Для любителей литературы посещение родины и места упокоения автора «Повести о Киеу» — трогательное культурное паломничество, углубляющее понимание человека и эпохи, породившей одно из величайших литературных сокровищ Вьетнама.",
  "highlights_vi": [
    "Nơi tưởng niệm Nguyễn Du, tác giả kiệt tác 'Truyện Kiều'",
    "Danh nhân văn hóa được UNESCO vinh danh (2013)",
    "Có mộ Đại thi hào, nhà thờ dòng họ và bảo tàng nhiều hiện vật quý"
  ],
  "highlights_en": [
    "Memorial to Nguyen Du, author of the masterpiece 'The Tale of Kieu'",
    "A cultural figure recognised by UNESCO (2013)",
    "Includes the poet's tomb, the family shrine and a museum of precious relics"
  ],
  "highlights_ru": [
    "Мемориал Нгуен Зу, автора шедевра «Повесть о Киеу»",
    "Деятель культуры, признанный ЮНЕСКО (2013)",
    "Гробница поэта, родовое святилище и музей с ценными реликвиями"
  ],
  "practical": {
    "hours_vi": "Khoảng 7:00–17:00 (nghỉ trưa); nên hỏi trước ngày lễ.",
    "ticket_vi": "Vé tham quan tượng trưng khoảng 20.000–30.000 VND.",
    "duration_vi": "Khoảng 1–1,5 giờ.",
    "best_time_vi": "Quanh năm; dịp kỷ niệm Nguyễn Du có hoạt động văn hóa.",
    "tips_vi": "Nên có thuyết minh để hiểu về dòng họ và sự nghiệp; kết hợp thăm biển Nghi Xuân gần đó."
  },
  "tags": ["culture", "literature", "history", "museum", "memorial"],
  "sources": [{"title": "Wikipedia (VI) — Nguyễn Du", "url": "https://vi.wikipedia.org/wiki/Nguy%E1%BB%85n_Du"}]
})

add({
  "region": "vn-ha-tinh", "slug": "bien-thien-cam",
  "region_name_vi": "Hà Tĩnh", "federal_district": "Miền Trung",
  "name_vi": "Biển Thiên Cầm",
  "name_en": "Thien Cam Beach",
  "name_ru": "Пляж Тхьенкам",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 18.1189, "lon": 106.1017},
  "address_vi": "Thị trấn Thiên Cầm, huyện Cẩm Xuyên, tỉnh Hà Tĩnh",
  "rating": {"value": 4.3, "count": 2500, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Bãi biển thoải, cát mịn, nước sạch, hải sản tươi ngon và giá phải chăng. Du khách thích sự yên bình, ít xô bồ; một số nói dịch vụ còn giản dị, đông vào mùa hè cuối tuần.",
  "presentation_short_vi": "Thiên Cầm là bãi biển đẹp và nổi tiếng nhất Hà Tĩnh, với bờ cát trắng mịn thoai thoải dài nhiều cây số, nước biển trong xanh. Tên gọi 'Thiên Cầm' (đàn trời) gắn với truyền thuyết vua nghe tiếng sóng, gió và núi vọng lại như tiếng đàn. Nơi đây nổi tiếng hải sản tươi ngon, bình yên, hợp nghỉ dưỡng.",
  "presentation_short_en": "Thien Cam is the finest and best-known beach in Ha Tinh, with a gently sloping shore of fine white sand stretching for kilometres and clear blue water. Its name, 'Heaven's Lute', comes from a legend of a king who heard the waves, wind and hills echo like a lute. The area is celebrated for fresh seafood and a calm, restful atmosphere.",
  "presentation_short_ru": "Тхьенкам — лучший и самый известный пляж Хатиня, с полого спускающимся берегом мелкого белого песка длиной в несколько километров и чистой синей водой. Его название, «небесная лютня», связано с легендой о короле, услышавшем, как волны, ветер и холмы отзываются, словно лютня. Место славится свежими морепродуктами и спокойной, умиротворяющей атмосферой.",
  "presentation_long_vi": "Nằm ở huyện Cẩm Xuyên, cách thành phố Hà Tĩnh khoảng 20 km, biển Thiên Cầm từ lâu được coi là viên ngọc của du lịch biển Hà Tĩnh. Bãi tắm ở đây có địa hình khá đặc biệt: bờ cát trắng mịn, thoai thoải và nông dần ra xa nên khá an toàn, ôm lấy một vùng vịnh nhỏ được che chắn bởi núi Thiên Cầm và núi Đầu Voi ở hai đầu. Theo truyền thuyết, khi vua Hồ Quý Ly đi qua đây, nghe tiếng gió biển, sóng vỗ và tiếng thông reo trên núi hòa quyện như tiếng đàn trời, nên đặt tên vùng này là 'Thiên Cầm' – cây đàn của trời. Bên cạnh việc tắm biển, du khách có thể leo lên núi Thiên Cầm để thăm chùa và ngắm toàn cảnh bờ biển cong hình cánh cung, hoặc đi thuyền ra hòn Bơớc gần bờ. Vùng biển này nổi tiếng với nguồn hải sản phong phú, tươi ngon như mực, ghẹ, tôm, cá và đặc sản mực nhảy Vũng Áng lân cận; các quán ăn ven biển phục vụ món tươi với giá bình dân. So với nhiều bãi biển miền Trung sầm uất, Thiên Cầm giữ được nét mộc mạc, yên bình, không khí trong lành, thích hợp cho những kỳ nghỉ gia đình nhẹ nhàng và những ai muốn tìm một bãi biển đẹp mà chưa quá đông đúc.",
  "presentation_long_en": "In Cam Xuyen district, about 20 km from Ha Tinh city, Thien Cam Beach has long been regarded as the jewel of Ha Tinh's coastal tourism. Its bathing area has an unusual form: a gently shelving shore of fine white sand that deepens slowly, making it fairly safe, curving around a small bay sheltered by Thien Cam and Dau Voi hills at each end. Legend says that when King Ho Quy Ly passed here, he heard the sea wind, the breaking waves and the sighing pines on the hill blend like the music of a heavenly lute, and so named the place 'Thien Cam' — Heaven's Lute. Beyond swimming, visitors can climb Thien Cam hill to a pagoda and admire the whole bow-shaped coast, or take a boat to nearby Buoc islet. These waters are known for abundant, fresh seafood — squid, crab, prawns and fish, along with the famous 'jumping squid' of nearby Vung Ang; seaside eateries serve the catch at modest prices. Compared with many busier central-coast beaches, Thien Cam keeps a simple, peaceful character and clean air, ideal for gentle family holidays and for anyone seeking a beautiful beach that is not yet too crowded.",
  "presentation_long_ru": "В уезде Камсуйен, примерно в 20 км от города Хатинь, пляж Тхьенкам издавна считается жемчужиной прибрежного туризма провинции. Его купальная зона необычна: полого спускающийся берег мелкого белого песка, медленно уходящий на глубину, что делает его довольно безопасным, огибает небольшую бухту, укрытую холмами Тхьенкам и Заувой по краям. По легенде, когда король Хо Куи Ли проходил здесь, он услышал, как морской ветер, накат волн и шум сосен на холме сливаются, словно музыка небесной лютни, и назвал это место «Тхьенкам» — небесная лютня. Помимо купания, гости могут подняться на холм Тхьенкам к пагоде и полюбоваться всей дугой берега или доплыть на лодке до близкого островка Быок. Эти воды известны обилием свежих морепродуктов — кальмаров, крабов, креветок и рыбы, а также знаменитым «прыгающим кальмаром» соседнего Вунганга; прибрежные закусочные подают улов по скромным ценам. По сравнению со многими более людными пляжами центрального побережья Тхьенкам сохраняет простой, спокойный характер и чистый воздух, идеально подходя для неспешного семейного отдыха и тех, кто ищет красивый, но ещё не слишком многолюдный пляж.",
  "highlights_vi": [
    "Bãi biển đẹp nhất Hà Tĩnh: cát trắng mịn, thoai thoải, vịnh được núi che chắn",
    "Tên 'Thiên Cầm' (đàn trời) gắn truyền thuyết vua Hồ Quý Ly",
    "Hải sản tươi ngon, không khí bình yên, giá bình dân"
  ],
  "highlights_en": [
    "Ha Tinh's finest beach: fine white sand, a gentle slope, a hill-sheltered bay",
    "Name 'Heaven's Lute' tied to the legend of King Ho Quy Ly",
    "Fresh seafood, a peaceful atmosphere and modest prices"
  ],
  "highlights_ru": [
    "Лучший пляж Хатиня: мелкий белый песок, пологий вход, укрытая холмами бухта",
    "Название «небесная лютня» связано с легендой о короле Хо Куи Ли",
    "Свежие морепродукты, спокойная атмосфера и скромные цены"
  ],
  "practical": {
    "hours_vi": "Bãi biển mở cả ngày; đẹp nhất sáng sớm và chiều mát.",
    "ticket_vi": "Vào bãi thường miễn phí; dịch vụ ghế, phao, tắm nước ngọt có phí nhỏ.",
    "duration_vi": "Nửa ngày đến 2 ngày.",
    "best_time_vi": "Mùa hè (tháng 5–8); tránh mùa mưa bão (tháng 9–11).",
    "tips_vi": "Chú ý cờ báo an toàn khi tắm; thử mực nhảy, hải sản tươi; đặt phòng sớm cao điểm hè."
  },
  "tags": ["beach", "seafood", "family", "nature", "relax"],
  "sources": [{"title": "Wikipedia (VI) — Thiên Cầm", "url": "https://vi.wikipedia.org/wiki/Thi%C3%AAn_C%E1%BA%A7m"}]
})

# ---------- THÁI NGUYÊN (gồm Bắc Kạn cũ) ----------
add({
  "region": "vn-thai-nguyen", "slug": "ho-ba-be",
  "region_name_vi": "Thái Nguyên", "federal_district": "Miền Bắc",
  "name_vi": "Hồ Ba Bể (Vườn quốc gia Ba Bể)",
  "name_en": "Ba Be Lake (Ba Be National Park)",
  "name_ru": "Озеро Бабе (национальный парк Бабе)",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 22.4022, "lon": 105.6180},
  "address_vi": "Vườn quốc gia Ba Bể, tỉnh Thái Nguyên (Bắc Kạn cũ)",
  "rating": {"value": 4.6, "count": 4500, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Hồ nước ngọt trên núi đẹp như tranh, đi thuyền qua ao Tiên, động Puông, thác Đầu Đẳng rất thích. Du khách khen homestay người Tày, cảnh yên bình; đường tới hồ hơi xa và quanh co.",
  "presentation_short_vi": "Hồ Ba Bể là hồ nước ngọt tự nhiên trên núi lớn nhất Việt Nam, nằm trong Vườn quốc gia Ba Bể, tỉnh Thái Nguyên (Bắc Kạn cũ). Được bao quanh bởi núi đá vôi và rừng nguyên sinh, hồ gắn với các thắng cảnh như động Puông, thác Đầu Đẳng, ao Tiên và những bản làng người Tày ven hồ.",
  "presentation_short_en": "Ba Be Lake is the largest natural mountain freshwater lake in Vietnam, at the heart of Ba Be National Park in Thai Nguyen province (formerly Bac Kan). Ringed by limestone peaks and old-growth forest, it is linked to sights such as Puong Cave, Dau Dang Waterfall, the Fairy Pond and the Tay ethnic villages along its shores.",
  "presentation_short_ru": "Озеро Бабе — крупнейшее естественное горное пресноводное озеро Вьетнама, в сердце национального парка Бабе в провинции Тхайнгуен (прежде Баккан). Окружённое известняковыми вершинами и девственным лесом, оно связано с такими достопримечательностями, как пещера Пуонг, водопад Заудang, Пруд фей и деревни народа тай на берегах.",
  "presentation_long_vi": "Nằm ở vùng núi phía bắc, nay thuộc tỉnh Thái Nguyên (địa phận Bắc Kạn cũ), hồ Ba Bể là hồ nước ngọt tự nhiên trên núi lớn nhất cả nước, hình thành cách đây hàng trăm triệu năm giữa một vùng núi đá vôi. Hồ dài hơn 8 km, gồm ba nhánh hồ nối nhau (nên có tên 'Ba Bể' – ba hồ), mặt nước trong xanh phẳng lặng phản chiếu những vách núi và rừng cây rậm rạp. Đây là trung tâm của Vườn quốc gia Ba Bể, khu bảo tồn có hệ sinh thái đa dạng với nhiều loài động, thực vật quý hiếm, và từng được công nhận là khu Ramsar – vùng đất ngập nước có tầm quan trọng quốc tế. Trải nghiệm được yêu thích nhất là ngồi thuyền độc mộc hoặc thuyền máy dạo quanh hồ, ghé thăm động Puông – nơi dòng sông Năng chảy xuyên qua lòng núi đá dài cả cây số, thác Đầu Đẳng nước đổ qua các bậc đá, ao Tiên nhỏ xinh và đảo An Mã giữa hồ. Ven hồ là những bản làng của người Tày với nhà sàn truyền thống, nơi du khách có thể nghỉ homestay, thưởng thức ẩm thực địa phương và nghe hát then, đàn tính. Không khí trong lành, cảnh sắc nên thơ và nhịp sống bình dị khiến Ba Bể là điểm đến lý tưởng cho những ai yêu thiên nhiên và muốn khám phá vùng núi Đông Bắc.",
  "presentation_long_en": "In the northern mountains, now within Thai Nguyen province (formerly Bac Kan), Ba Be Lake is the country's largest natural mountain freshwater lake, formed hundreds of millions of years ago amid limestone ranges. More than 8 km long, it consists of three linked basins — hence the name 'Ba Be', three lakes — its calm, clear water mirroring the cliffs and dense forest. It lies at the heart of Ba Be National Park, a reserve of rich biodiversity with many rare species, once recognised as a Ramsar site of international importance. The favourite experience is a trip by dugout or motorboat around the lake, calling at Puong Cave, where the Nang River flows for a kilometre through the heart of the mountain, at Dau Dang Waterfall cascading over rock steps, at the little Fairy Pond and at An Ma islet in mid-lake. Along the shores are Tay villages of traditional stilt houses, where visitors can stay in homestays, enjoy local food and hear 'then' singing and the 'tinh' lute. Fresh air, poetic scenery and an unhurried way of life make Ba Be an ideal destination for nature lovers and for exploring the north-eastern highlands.",
  "presentation_long_ru": "В северных горах, ныне в составе провинции Тхайнгуен (прежде Баккан), озеро Бабе — крупнейшее в стране естественное горное пресноводное озеро, образовавшееся сотни миллионов лет назад среди известняковых гряд. Длиной более 8 км, оно состоит из трёх связанных котловин — отсюда название «Бабе», три озера, — а его спокойная прозрачная вода отражает скалы и густой лес. Оно лежит в сердце национального парка Бабе, заповедника с богатым биоразнообразием и многими редкими видами, когда-то признанного рамсарским угодьем международного значения. Любимое занятие — прогулка на долблёной лодке или моторке вокруг озера с заходом в пещеру Пуонг, где река Нанг на километр уходит сквозь толщу горы, к водопаду Заудang, спадающему по каменным ступеням, к маленькому Пруду фей и островку Анма посреди озера. По берегам стоят деревни тай с традиционными свайными домами, где гости могут остановиться в homestay, попробовать местную еду и услышать пение «тхен» и лютню «тинь». Свежий воздух, поэтичные виды и неспешный уклад жизни делают Бабе идеальным местом для любителей природы и знакомства с северо-восточным высокогорьем.",
  "highlights_vi": [
    "Hồ nước ngọt tự nhiên trên núi lớn nhất Việt Nam, từng là khu Ramsar",
    "Thuyền dạo hồ ghé động Puông, thác Đầu Đẳng, ao Tiên, đảo An Mã",
    "Bản người Tày ven hồ với nhà sàn, homestay, hát then đàn tính"
  ],
  "highlights_en": [
    "Vietnam's largest natural mountain freshwater lake, once a Ramsar site",
    "Boat tours to Puong Cave, Dau Dang Waterfall, the Fairy Pond and An Ma islet",
    "Lakeside Tay villages with stilt houses, homestays and 'then' singing"
  ],
  "highlights_ru": [
    "Крупнейшее естественное горное пресноводное озеро Вьетнама, бывшее рамсарское угодье",
    "Лодочные прогулки к пещере Пуонг, водопаду Заудang, Пруду фей и островку Анма",
    "Прибрежные деревни тай со свайными домами, homestay и пением «тхен»"
  ],
  "practical": {
    "hours_vi": "Bến thuyền hoạt động ban ngày; homestay theo đặt trước.",
    "ticket_vi": "Phí vào vườn quốc gia và thuê thuyền tính riêng; thuyền tham quan vài trăm nghìn/chuyến.",
    "duration_vi": "1–2 ngày (nên nghỉ đêm).",
    "best_time_vi": "Mùa khô (tháng 10–4); tránh mùa mưa lũ.",
    "tips_vi": "Đi thuyền nên mặc áo phao; mang tiền mặt; đặt homestay bản Pác Ngòi trước."
  },
  "tags": ["lake", "national-park", "nature", "boat", "homestay", "top"],
  "sources": [{"title": "Wikipedia (VI) — Hồ Ba Bể", "url": "https://vi.wikipedia.org/wiki/H%E1%BB%93_Ba_B%E1%BB%83"}]
})

add({
  "region": "vn-thai-nguyen", "slug": "ho-nui-coc",
  "region_name_vi": "Thái Nguyên", "federal_district": "Miền Bắc",
  "name_vi": "Hồ Núi Cốc",
  "name_en": "Nui Coc Lake",
  "name_ru": "Озеро Нуйкок",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 21.5500, "lon": 105.7167},
  "address_vi": "Hồ Núi Cốc, tỉnh Thái Nguyên (cách TP Thái Nguyên khoảng 15 km)",
  "rating": {"value": 4.1, "count": 3500, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Hồ nhân tạo rộng với nhiều đảo nhỏ, gắn truyền thuyết nàng Công – chàng Cốc. Du khách thích đi thuyền ngắm cảnh, khu vui chơi; một số hạng mục cũ nhưng cảnh hồ và đồi chè quanh vùng đẹp.",
  "presentation_short_vi": "Hồ Núi Cốc là hồ nước nhân tạo rộng lớn ở tỉnh Thái Nguyên, nổi tiếng với mặt hồ mênh mông điểm xuyết hàng chục hòn đảo nhỏ và truyền thuyết tình yêu 'nàng Công – chàng Cốc'. Đây là khu du lịch sinh thái quen thuộc, kết hợp đi thuyền, vui chơi và ngắm những đồi chè xanh mướt của vùng chè Thái Nguyên.",
  "presentation_short_en": "Nui Coc Lake is a large man-made reservoir in Thai Nguyen province, famous for its broad waters dotted with dozens of small islands and for the love legend of 'Lady Cong and Lad Coc'. It is a popular eco-tourism area combining boat rides, amusement facilities and views of the green tea hills for which Thai Nguyen is renowned.",
  "presentation_short_ru": "Озеро Нуйкок — большое искусственное водохранилище в провинции Тхайнгуен, знаменитое широкой гладью с десятками маленьких островов и легендой о любви «девы Конг и юноши Кок». Это популярная эколого-туристическая зона, сочетающая лодочные прогулки, аттракционы и виды зелёных чайных холмов, которыми славится Тхайнгуен.",
  "presentation_long_vi": "Nằm cách thành phố Thái Nguyên khoảng 15 km về phía tây, hồ Núi Cốc là một hồ chứa nước nhân tạo được hình thành từ việc chặn dòng sông Công vào những năm 1970 để phục vụ tưới tiêu và điều hòa nước. Trải qua thời gian, hồ trở thành một thắng cảnh và khu du lịch sinh thái nổi tiếng của vùng trung du Bắc Bộ. Mặt hồ rộng hàng nghìn hecta, uốn lượn giữa các dãy đồi thấp và rải rác hàng chục hòn đảo lớn nhỏ phủ đầy cây xanh, tạo nên khung cảnh vừa khoáng đạt vừa nên thơ. Hồ gắn liền với truyền thuyết tình yêu cảm động của nàng Công và chàng Cốc: đôi trai gái yêu nhau nhưng không được kết duyên, chàng hóa thành núi, nàng hóa thành dòng sông, để rồi tên núi, tên sông, tên hồ đều nhắc nhớ mối tình ấy. Du khách đến hồ Núi Cốc có thể lên thuyền dạo quanh, ghé các đảo như đảo Cái, thăm khu vui chơi giải trí, công viên nước, hang huyền thoại cung tái hiện truyền thuyết, hoặc tản bộ, cắm trại ven hồ. Xung quanh vùng hồ là những đồi chè xanh mướt đặc trưng của Thái Nguyên – 'đệ nhất danh trà'. Với khoảng cách gần Hà Nội và không gian thoáng đãng, hồ Núi Cốc là lựa chọn nghỉ ngơi, dã ngoại cuối tuần được nhiều gia đình yêu thích.",
  "presentation_long_en": "About 15 km west of Thai Nguyen city, Nui Coc Lake is a man-made reservoir formed by damming the Cong River in the 1970s for irrigation and water control. Over time it has become a well-known beauty spot and eco-tourism area of the northern midlands. Covering thousands of hectares, its waters wind among low hills and are scattered with dozens of green, tree-covered islands, creating scenery at once open and poetic. The lake is bound to the touching love legend of Lady Cong and Lad Coc: two young lovers who could not marry, so that he turned into a mountain and she into a river, and the names of mountain, river and lake all recall their love. Visitors can take a boat around the lake, call at islands such as Cai Island, visit amusement parks, a water park and a 'legend cave' that re-creates the story, or stroll and camp along the shore. The surrounding hills are covered with the lush tea gardens for which Thai Nguyen — 'the finest tea' — is celebrated. Close to Hanoi and pleasantly airy, Nui Coc Lake is a favourite weekend spot for family outings and relaxation.",
  "presentation_long_ru": "Примерно в 15 км к западу от города Тхайнгуен озеро Нуйкок — искусственное водохранилище, образованное перекрытием реки Конг в 1970-е годы для орошения и регулирования воды. Со временем оно стало известным живописным местом и эколого-туристической зоной северного среднегорья. Раскинувшись на тысячи гектаров, его воды вьются среди невысоких холмов и усеяны десятками зелёных, покрытых деревьями островов, создавая пейзаж одновременно просторный и поэтичный. Озеро связано с трогательной легендой о любви девы Конг и юноши Кок: молодые влюблённые не смогли пожениться, и он обратился в гору, а она — в реку, так что названия горы, реки и озера напоминают об их любви. Гости могут покататься на лодке по озеру, заглянуть на острова, например остров Кай, посетить парки аттракционов, аквапарк и «пещеру легенд», воссоздающую эту историю, или прогуляться и разбить лагерь на берегу. Окрестные холмы покрыты пышными чайными садами, которыми славится Тхайнгуен — «лучший чай». Близкое к Ханою и приятно просторное, озеро Нуйкок — любимое место семейного отдыха на выходных.",
  "highlights_vi": [
    "Hồ nhân tạo rộng lớn với hàng chục hòn đảo xanh giữa vùng trung du",
    "Gắn truyền thuyết tình yêu nàng Công – chàng Cốc",
    "Đi thuyền, khu vui chơi và ngắm đồi chè Thái Nguyên nổi tiếng"
  ],
  "highlights_en": [
    "A vast reservoir dotted with dozens of green islands in the midlands",
    "Tied to the love legend of Lady Cong and Lad Coc",
    "Boat rides, amusement areas and views of Thai Nguyen's famous tea hills"
  ],
  "highlights_ru": [
    "Обширное водохранилище с десятками зелёных островов в среднегорье",
    "Связано с легендой о любви девы Конг и юноши Кок",
    "Лодочные прогулки, зоны развлечений и виды знаменитых чайных холмов"
  ],
  "practical": {
    "hours_vi": "Khu du lịch mở khoảng 7:00–18:00.",
    "ticket_vi": "Vé vào cổng và các dịch vụ (thuyền, khu vui chơi) tính riêng.",
    "duration_vi": "Nửa ngày đến 1 ngày.",
    "best_time_vi": "Mùa hè cho hoạt động nước; mùa thu trời mát.",
    "tips_vi": "Kết hợp ghé vùng chè Tân Cương gần đó; mang đồ dã ngoại nếu muốn cắm trại."
  },
  "tags": ["lake", "family", "boat", "nature", "daytrip"],
  "sources": [{"title": "Wikipedia (VI) — Hồ Núi Cốc", "url": "https://vi.wikipedia.org/wiki/H%E1%BB%93_N%C3%BAi_C%E1%BB%91c"}]
})

add({
  "region": "vn-thai-nguyen", "slug": "atk-dinh-hoa",
  "region_name_vi": "Thái Nguyên", "federal_district": "Miền Bắc",
  "name_vi": "Khu di tích ATK Định Hóa",
  "name_en": "ATK Dinh Hoa Historic Site",
  "name_ru": "Историческая зона АТК Диньхоа",
  "categories": ["monument", "museum"],
  "coordinates": {"lat": 21.8992, "lon": 105.5486},
  "address_vi": "Xã Phú Đình, huyện Định Hóa, tỉnh Thái Nguyên",
  "rating": {"value": 4.6, "count": 1500, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Địa chỉ lịch sử về 'Thủ đô kháng chiến' của Việt Nam; du khách xúc động thăm lán Tỉn Keo, nơi Bác Hồ và Trung ương từng ở, làm việc. Không gian rừng núi trong lành, nhà trưng bày nhiều tư liệu quý.",
  "presentation_short_vi": "ATK Định Hóa là khu 'An toàn khu' – nơi Chủ tịch Hồ Chí Minh và các cơ quan Trung ương đặt căn cứ lãnh đạo cuộc kháng chiến chống Pháp (1947–1954), được ví là 'Thủ đô gió ngàn'. Khu di tích quốc gia đặc biệt gồm nhiều điểm như đồi Tỉn Keo, nơi phát lệnh mở chiến dịch Điện Biên Phủ.",
  "presentation_short_en": "ATK Dinh Hoa was the 'Safe Zone' where President Ho Chi Minh and central agencies based themselves to lead the resistance war against France (1947–1954), nicknamed the 'capital of the windy forests'. This special national relic site includes places such as Tin Keo Hill, where the order launching the Dien Bien Phu campaign was given.",
  "presentation_short_ru": "АТК Диньхоа была «безопасной зоной», где президент Хо Ши Мин и центральные органы разместили базу для руководства войной Сопротивления против Франции (1947–1954), прозванной «столицей лесных ветров». Этот особый национальный памятник включает такие места, как холм Тинкео, где был отдан приказ о начале кампании при Дьенбьенфу.",
  "presentation_long_vi": "Nằm giữa vùng rừng núi huyện Định Hóa, tỉnh Thái Nguyên, khu di tích ATK (An toàn khu) Định Hóa là một trong những 'địa chỉ đỏ' quan trọng nhất của lịch sử cách mạng Việt Nam. Trong những năm kháng chiến chống thực dân Pháp (1947–1954), vùng núi hiểm trở nhưng gần các tuyến giao thông này được chọn làm căn cứ địa, nơi Chủ tịch Hồ Chí Minh, Trung ương Đảng, Chính phủ và nhiều cơ quan đầu não đóng và làm việc. Chính tại đây, nhiều quyết sách trọng đại đã ra đời; đặc biệt trên đồi Tỉn Keo (xã Phú Đình), tháng 12 năm 1953, Bác Hồ và Bộ Chính trị đã họp và hạ quyết tâm mở chiến dịch Điện Biên Phủ – trận đánh làm nên chiến thắng 'lừng lẫy năm châu, chấn động địa cầu'. Ngày nay, khu di tích quốc gia đặc biệt ATK Định Hóa gồm nhiều điểm phân bố trong rừng: lán Tỉn Keo, nơi ở và làm việc của Bác, nhà trưng bày bảo tàng, nhà tưởng niệm Chủ tịch Hồ Chí Minh trên đỉnh đèo De, cùng các di tích của những cơ quan kháng chiến. Không gian nơi đây yên tĩnh, cây rừng rợp mát, gợi lại một thời gian khổ mà hào hùng. Đến với ATK Định Hóa, du khách vừa được tìm hiểu lịch sử, vừa được hòa mình vào cảnh sắc núi rừng vùng chiến khu Việt Bắc.",
  "presentation_long_en": "Amid the forested hills of Dinh Hoa district in Thai Nguyen province, the ATK (Safe Zone) Dinh Hoa relic site is one of the most important 'red addresses' in Vietnam's revolutionary history. During the resistance war against the French (1947–1954), this rugged yet well-connected upland was chosen as a base where President Ho Chi Minh, the Party Central Committee, the government and many top agencies lived and worked. Here many momentous decisions were made; above all, on Tin Keo Hill in Phu Dinh commune in December 1953, Ho Chi Minh and the Politburo met and resolved to launch the Dien Bien Phu campaign — the battle that produced a victory 'renowned across the five continents and shaking the earth'. Today the special national relic complex spans many points in the forest: the Tin Keo hut where Ho lived and worked, a museum display hall, a memorial house to Ho Chi Minh atop De Pass, and relics of various resistance agencies. The atmosphere is quiet and shaded by forest, evoking a time both hard and heroic. Visiting ATK Dinh Hoa, travellers can learn history while immersing themselves in the mountain scenery of the Viet Bac war zone.",
  "presentation_long_ru": "Среди лесистых холмов уезда Диньхоа в провинции Тхайнгуен памятник АТК (безопасной зоны) Диньхоа — один из важнейших «красных адресов» революционной истории Вьетнама. Во время войны Сопротивления против французов (1947–1954) это труднодоступное, но хорошо связанное нагорье было выбрано базой, где жили и работали президент Хо Ши Мин, ЦК партии, правительство и многие высшие органы. Здесь принимались судьбоносные решения; прежде всего на холме Тинкео в общине Фудинь в декабре 1953 года Хо Ши Мин и Политбюро собрались и решили начать кампанию при Дьенбьенфу — сражение, давшее победу, «прославленную на пяти континентах и потрясшую землю». Сегодня особый национальный комплекс охватывает множество точек в лесу: хижину Тинкео, где жил и работал Хо, музейный зал, мемориальный дом Хо Ши Мина на перевале Де и памятники разным органам Сопротивления. Атмосфера тиха и затенена лесом, напоминая о времени и трудном, и героическом. Посещая АТК Диньхоа, путешественники узнают историю, погружаясь в горные виды военной зоны Вьетбак. Прогулка между отдельными точками комплекса по лесным тропам приятна сама по себе и помогает представить условия, в которых жили и работали руководители Сопротивления.",
  "highlights_vi": [
    "'Thủ đô kháng chiến' – căn cứ của Bác Hồ và Trung ương thời chống Pháp",
    "Đồi Tỉn Keo: nơi quyết định mở chiến dịch Điện Biên Phủ (12/1953)",
    "Khu di tích quốc gia đặc biệt giữa rừng núi Việt Bắc"
  ],
  "highlights_en": [
    "The 'resistance capital' — base of Ho Chi Minh and the Party during the French war",
    "Tin Keo Hill: where the Dien Bien Phu campaign was decided (Dec 1953)",
    "A special national relic site amid the Viet Bac forests"
  ],
  "highlights_ru": [
    "«Столица Сопротивления» — база Хо Ши Мина и партии во время войны с французами",
    "Холм Тинкео: где решили начать кампанию при Дьенбьенфу (дек. 1953)",
    "Особый национальный памятник среди лесов Вьетбак"
  ],
  "practical": {
    "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
    "ticket_vi": "Vào cửa miễn phí hoặc phí tượng trưng.",
    "duration_vi": "Khoảng 2–3 giờ (nhiều điểm phân tán).",
    "best_time_vi": "Quanh năm; dịp 19/5, 2/9 có ý nghĩa đặc biệt.",
    "tips_vi": "Nên có xe riêng vì các điểm cách nhau; kết hợp thuyết minh; giữ trang nghiêm nơi tưởng niệm."
  },
  "tags": ["history", "revolution", "memorial", "forest", "education"],
  "sources": [{"title": "Wikipedia (VI) — ATK Định Hóa", "url": "https://vi.wikipedia.org/wiki/ATK_%C4%90%E1%BB%8Bnh_H%C3%B3a"}]
})

add({
  "region": "vn-thai-nguyen", "slug": "vung-che-tan-cuong",
  "region_name_vi": "Thái Nguyên", "federal_district": "Miền Bắc",
  "name_vi": "Vùng chè Tân Cương",
  "name_en": "Tan Cuong Tea Hills",
  "name_ru": "Чайные холмы Танкыонг",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 21.5497, "lon": 105.7639},
  "address_vi": "Xã Tân Cương, thành phố Thái Nguyên, tỉnh Thái Nguyên",
  "rating": {"value": 4.5, "count": 900, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Những đồi chè xanh mướt uốn lượn, không khí trong lành, trải nghiệm hái và pha chè rất thú. Du khách thích chụp ảnh, thăm nhà làm chè và mua trà đặc sản; nên ghé buổi sáng sớm khi còn sương.",
  "presentation_short_vi": "Tân Cương là vùng chè trứ danh của Thái Nguyên, nơi sản sinh loại trà được mệnh danh 'đệ nhất danh trà' của Việt Nam. Những đồi chè xanh mượt uốn lượn nối tiếp nhau tạo nên khung cảnh thanh bình; du khách có thể tham quan, trải nghiệm hái chè, sao chè và thưởng thức trà thơm ngay tại vườn.",
  "presentation_short_en": "Tan Cuong is the celebrated tea region of Thai Nguyen, home to the tea often called Vietnam's 'finest'. Rolling hills of glossy green tea bushes stretch one after another in peaceful scenery; visitors can tour the gardens, try picking and pan-roasting the leaves and taste fragrant tea right where it grows.",
  "presentation_short_ru": "Танкыонг — прославленный чайный край Тхайнгуена, родина чая, который часто называют «лучшим» во Вьетнаме. Волнистые холмы блестящих зелёных чайных кустов тянутся один за другим в умиротворяющем пейзаже; гости могут осмотреть сады, попробовать собирать и обжаривать листья и отведать ароматный чай прямо там, где он растёт.",
  "presentation_long_vi": "Cách trung tâm thành phố Thái Nguyên khoảng 10 km, xã Tân Cương từ lâu đã là 'thủ phủ' của cây chè Thái Nguyên – thứ đặc sản làm nên thương hiệu 'đệ nhất danh trà' của đất nước. Nhờ điều kiện thổ nhưỡng, khí hậu và nguồn nước đặc biệt, chè Tân Cương cho búp nhỏ, hương thơm cốm dịu, vị chát nhẹ rồi ngọt hậu rất đặc trưng, được người sành trà cả nước ưa chuộng. Đến Tân Cương, du khách như lạc vào một biển chè xanh: những đồi chè được cắt tỉa gọn gàng, uốn lượn theo sườn đồi, nối tiếp nhau đến tận chân trời, đẹp nhất vào sáng sớm khi sương còn đọng trên lá và ánh nắng vàng trải nhẹ. Nhiều nhà vườn và hợp tác xã chè mở cửa đón khách, cho phép trải nghiệm trọn vẹn quy trình làm trà: đội nón đi hái những búp 'một tôm hai lá', xem sao chè, vò chè bằng tay hoặc bằng máy, rồi ngồi thưởng thức chén trà nóng thơm lừng bên chủ nhà. Trong vùng còn có Không gian văn hóa Trà Tân Cương và bảo tàng, nhà trưng bày giới thiệu lịch sử, dụng cụ và văn hóa thưởng trà. Đây là điểm đến lý tưởng cho những ai muốn tìm hiểu văn hóa trà Việt, chụp ảnh giữa đồi chè và mua trà ngon về làm quà.",
  "presentation_long_en": "About 10 km from the centre of Thai Nguyen city, Tan Cuong commune has long been the 'capital' of Thai Nguyen tea — the speciality behind the country's reputation for its 'finest tea'. Thanks to special soil, climate and water, Tan Cuong tea yields small buds with a gentle young-rice fragrance and a mild astringency that turns to a lasting sweetness, prized by tea connoisseurs nationwide. Arriving in Tan Cuong, visitors seem to enter a green sea of tea: neatly trimmed bushes curve along the slopes and roll to the horizon, at their finest in early morning when dew still clings to the leaves and soft golden light spreads across them. Many gardens and tea cooperatives welcome guests to experience the whole process: donning a conical hat to pick the 'one bud, two leaves', watching the leaves pan-roasted, rolling them by hand or machine, then sitting down to a cup of fragrant hot tea with the host. The area also has a Tan Cuong Tea Cultural Space and museum introducing the history, tools and etiquette of tea. It is an ideal destination for anyone wishing to learn about Vietnamese tea culture, take photographs among the hills and buy fine tea to bring home.",
  "presentation_long_ru": "Примерно в 10 км от центра города Тхайнгуен община Танкыонг издавна была «столицей» чая Тхайнгуена — деликатеса, создавшего репутацию «лучшего чая» страны. Благодаря особой почве, климату и воде чай Танкыонг даёт мелкие почки с нежным ароматом молодого риса и лёгкой терпкостью, переходящей в долгую сладость, что ценят знатоки по всей стране. Приезжая в Танкыонг, гости словно попадают в зелёное море чая: аккуратно подстриженные кусты изгибаются по склонам и уходят к горизонту, особенно красивые ранним утром, когда на листьях ещё лежит роса, а мягкий золотой свет разливается по ним. Многие сады и чайные кооперативы принимают гостей, предлагая пройти весь процесс: надеть коническую шляпу и собрать «одну почку и два листа», посмотреть на обжаривание листьев, скрутить их вручную или на машине, а затем сесть за чашкой ароматного горячего чая с хозяином. В районе есть также Культурное пространство чая Танкыонг и музей, знакомящие с историей, инструментами и этикетом чаепития. Это идеальное место для тех, кто хочет узнать вьетнамскую чайную культуру, сделать снимки среди холмов и купить хороший чай в подарок.",
  "highlights_vi": [
    "Vùng chè trứ danh, cái nôi của trà Thái Nguyên 'đệ nhất danh trà'",
    "Đồi chè xanh uốn lượn, đẹp nhất buổi sáng sớm còn sương",
    "Trải nghiệm hái, sao, pha chè và thăm không gian văn hóa trà"
  ],
  "highlights_en": [
    "A renowned tea region, cradle of Thai Nguyen's 'finest tea'",
    "Rolling green tea hills, loveliest in the dewy early morning",
    "Hands-on picking, roasting and brewing, and a tea cultural space"
  ],
  "highlights_ru": [
    "Прославленный чайный край, колыбель «лучшего чая» Тхайнгуена",
    "Волнистые зелёные чайные холмы, красивее всего росистым ранним утром",
    "Сбор, обжарка и заваривание чая и культурное чайное пространство"
  ],
  "practical": {
    "hours_vi": "Nhà vườn đón khách ban ngày; nên liên hệ trước.",
    "ticket_vi": "Tham quan thường miễn phí; trải nghiệm/mua trà theo dịch vụ.",
    "duration_vi": "Khoảng 2–3 giờ.",
    "best_time_vi": "Sáng sớm; mùa chè xuân và thu búp đẹp.",
    "tips_vi": "Đi sớm cho mát và ảnh đẹp; nếm thử trước khi mua; kết hợp ghé hồ Núi Cốc."
  },
  "tags": ["tea", "nature", "culture", "photography", "daytrip"],
  "sources": [{"title": "Wikipedia (VI) — Chè Thái Nguyên", "url": "https://vi.wikipedia.org/wiki/Ch%C3%A8_Th%C3%A1i_Nguy%C3%AAn"}]
})

# ---------- QUẢNG NGÃI (gồm Kon Tum cũ) ----------
add({
  "region": "vn-quang-ngai", "slug": "dao-ly-son",
  "region_name_vi": "Quảng Ngãi", "federal_district": "Miền Trung",
  "name_vi": "Đảo Lý Sơn",
  "name_en": "Ly Son Island",
  "name_ru": "Остров Лишон",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 15.3833, "lon": 109.1167},
  "address_vi": "Đặc khu/huyện đảo Lý Sơn, tỉnh Quảng Ngãi",
  "rating": {"value": 4.5, "count": 5500, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Đảo núi lửa với biển xanh, cánh đồng tỏi và di tích Hải đội Hoàng Sa. Du khách mê cổng Tò Vò, đỉnh Thới Lới, hải sản tươi; đi tàu ra đảo có thể say sóng, nên xem dự báo thời tiết.",
  "presentation_short_vi": "Lý Sơn là đảo núi lửa nằm ngoài khơi tỉnh Quảng Ngãi, nổi tiếng với biển trong xanh, những miệng núi lửa cổ, cánh đồng tỏi và hành trứ danh nên được gọi là 'vương quốc tỏi'. Đảo còn là nơi lưu giữ di sản Hải đội Hoàng Sa, gắn với chủ quyền biển đảo thiêng liêng của Việt Nam.",
  "presentation_short_en": "Ly Son is a volcanic island off Quang Ngai province, famous for clear blue seas, ancient craters and fields of the garlic and shallots that earn it the title 'kingdom of garlic'. It also preserves the heritage of the Hoang Sa flotilla, tied to Vietnam's cherished maritime sovereignty.",
  "presentation_short_ru": "Лишон — вулканический остров у берегов провинции Куангнгай, знаменитый прозрачным синим морем, древними кратерами и полями чеснока и лука-шалота, за которые его зовут «королевством чеснока». Он также хранит наследие флотилии Хоангша, связанное с дорогим Вьетнаму морским суверенитетом.",
  "presentation_long_vi": "Nằm cách đất liền Quảng Ngãi khoảng 15 hải lý, đảo Lý Sơn được hình thành từ hoạt động phun trào của núi lửa cách đây hàng triệu năm, để lại những vách đá bazan kỳ vĩ, các miệng núi lửa đã tắt và bãi biển nước trong vắt. Hòn đảo nhỏ này được ví như 'đảo thiên đường' của miền Trung, nổi bật với đỉnh Thới Lới – miệng núi lửa lớn nhất, nay có hồ nước ngọt trên cao và điểm ngắm toàn cảnh đảo tuyệt đẹp; cổng Tò Vò – vòm đá bazan tự nhiên bên bờ biển, điểm 'sống ảo' và ngắm hoàng hôn nổi tiếng; cùng chùa Hang, hang Câu, đảo Bé (An Bình) với bãi tắm cát trắng. Lý Sơn được mệnh danh là 'vương quốc tỏi' nhờ những cánh đồng tỏi, hành trồng trên nền cát và đất bazan cho hương vị đặc biệt. Song điều khiến Lý Sơn thiêng liêng hơn cả là bề dày lịch sử gắn với chủ quyền biển đảo: nơi đây có Âm Linh Tự, những ngôi mộ gió và lễ Khao lề thế lính Hoàng Sa, tưởng nhớ các binh phu năm xưa vâng mệnh triều đình ra Hoàng Sa, Trường Sa cắm mốc, đo đạc, khẳng định chủ quyền. Với vẻ đẹp thiên nhiên hoang sơ, hải sản tươi ngon và chiều sâu văn hóa – lịch sử, Lý Sơn là điểm đến ngày càng hấp dẫn du khách trong và ngoài nước.",
  "presentation_long_en": "About 15 nautical miles off the Quang Ngai mainland, Ly Son Island was formed by volcanic eruptions millions of years ago, leaving dramatic basalt cliffs, extinct craters and beaches of crystal-clear water. This small island is likened to a 'paradise isle' of central Vietnam, marked by Thoi Loi Peak — the largest crater, now holding a freshwater lake and a superb viewpoint over the whole island; the To Vo Arch — a natural basalt vault by the shore, a famous spot for photos and sunsets; along with Hang Pagoda, Cau Cave and the Little Island (An Binh) with its white-sand beach. Ly Son is called the 'kingdom of garlic' for its fields of garlic and shallots grown on sand and basalt soil, which give them a special flavour. Yet what makes Ly Son most sacred is its history bound to maritime sovereignty: here stand the Am Linh shrine, symbolic 'wind graves' and the ritual of 'sending off the Hoang Sa soldiers', honouring the men who, by royal command, once sailed to the Hoang Sa (Paracel) and Truong Sa (Spratly) to set markers, survey and assert sovereignty. With wild natural beauty, fresh seafood and cultural-historical depth, Ly Son is an increasingly attractive destination for Vietnamese and foreign visitors alike.",
  "presentation_long_ru": "Примерно в 15 морских милях от материковой части Куангнгая остров Лишон образовался от извержений вулканов миллионы лет назад, оставивших эффектные базальтовые скалы, потухшие кратеры и пляжи с кристально чистой водой. Этот небольшой остров сравнивают с «райским островом» центрального Вьетнама; его отличают пик Тхойлой — крупнейший кратер, ныне с пресноводным озером и превосходной смотровой площадкой над всем островом; арка Тово — естественный базальтовый свод у берега, знаменитое место для снимков и закатов; а также пагода Ханг, пещера Кау и Малый остров (Анбинь) с белопесчаным пляжем. Лишон называют «королевством чеснока» за поля чеснока и лука-шалота, выращенных на песке и базальтовой почве, что придаёт им особый вкус. Но священным Лишон делает прежде всего история, связанная с морским суверенитетом: здесь стоят святилище Амлинь, символические «могилы ветра» и обряд «проводов солдат Хоангша» в память о людях, которые по велению двора когда-то ходили к Хоангша (Парасельским) и Чыонгша (Спратли) островам ставить знаки, вести съёмку и утверждать суверенитет. С дикой природной красотой, свежими морепродуктами и культурно-исторической глубиной Лишон становится всё привлекательнее для вьетнамских и иностранных гостей.",
  "highlights_vi": [
    "Đảo núi lửa với đỉnh Thới Lới, cổng Tò Vò và biển trong xanh",
    "'Vương quốc tỏi' – cánh đồng tỏi, hành trên nền cát và đất bazan",
    "Di sản Hải đội Hoàng Sa, lễ Khao lề thế lính gắn chủ quyền biển đảo"
  ],
  "highlights_en": [
    "A volcanic island with Thoi Loi Peak, the To Vo Arch and clear blue seas",
    "The 'kingdom of garlic' — garlic and shallot fields on sand and basalt",
    "Heritage of the Hoang Sa flotilla and the soldier-farewell ritual of sovereignty"
  ],
  "highlights_ru": [
    "Вулканический остров с пиком Тхойлой, аркой Тово и прозрачным синим морем",
    "«Королевство чеснока» — поля чеснока и лука на песке и базальте",
    "Наследие флотилии Хоангша и обряд проводов солдат, связанный с суверенитетом"
  ],
  "practical": {
    "hours_vi": "Tàu ra đảo chạy ban ngày theo lịch và thời tiết.",
    "ticket_vi": "Vé tàu cao tốc khứ hồi tham khảo khoảng 300.000–400.000 VND; thuê xe máy trên đảo.",
    "duration_vi": "1–2 ngày (nên nghỉ đêm trên đảo).",
    "best_time_vi": "Mùa khô (tháng 4–8), biển lặng; tránh mùa mưa bão.",
    "tips_vi": "Xem dự báo thời tiết trước khi đi tàu; mang thuốc say sóng; thử gỏi tỏi, hải sản; tôn trọng di tích tâm linh."
  },
  "tags": ["island", "beach", "volcano", "history", "seafood", "top"],
  "sources": [{"title": "Wikipedia (VI) — Lý Sơn", "url": "https://vi.wikipedia.org/wiki/L%C3%BD_S%C6%A1n"}]
})

add({
  "region": "vn-quang-ngai", "slug": "mang-den",
  "region_name_vi": "Quảng Ngãi", "federal_district": "Miền Trung",
  "name_vi": "Khu du lịch Măng Đen",
  "name_en": "Mang Den",
  "name_ru": "Мангден",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 14.6333, "lon": 108.2833},
  "address_vi": "Xã Măng Đen, huyện Kon Plông, tỉnh Quảng Ngãi (Kon Tum cũ)",
  "rating": {"value": 4.5, "count": 3000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Được ví là 'Đà Lạt của Tây Nguyên/thứ hai': rừng thông, hồ, thác và khí hậu mát lạnh. Du khách thích sự yên bình, sương sớm, đặc sản gà nướng, cá tầm; dịch vụ đang phát triển nên chưa quá đông đúc.",
  "presentation_short_vi": "Măng Đen là thị trấn nghỉ mát trên cao nguyên thuộc tỉnh Quảng Ngãi (Kon Tum cũ), được ví là 'Đà Lạt thứ hai' của Tây Nguyên nhờ rừng thông bạt ngàn, nhiều hồ, thác và khí hậu mát lạnh quanh năm. Nơi đây còn nổi tiếng với tượng Đức Mẹ Măng Đen và nét văn hóa của các dân tộc bản địa.",
  "presentation_short_en": "Mang Den is a highland resort town in Quang Ngai province (formerly Kon Tum), likened to a 'second Da Lat' of the Central Highlands for its vast pine forests, many lakes and waterfalls and cool year-round climate. It is also known for the statue of Our Lady of Mang Den and the culture of the local ethnic peoples.",
  "presentation_short_ru": "Мангден — высокогорный курортный городок в провинции Куангнгай (прежде Контум), который сравнивают со «вторым Далатом» Центрального нагорья за обширные сосновые леса, множество озёр и водопадов и прохладный круглый год климат. Он известен также статуей Богоматери Мангден и культурой местных народов.",
  "presentation_long_vi": "Nằm ở độ cao khoảng 1.200 m trên vùng cao nguyên Kon Plông, Măng Đen thuộc tỉnh Quảng Ngãi (địa phận Kon Tum cũ) là một điểm nghỉ dưỡng đang lên của Tây Nguyên, được nhiều người ưu ái gọi là 'Đà Lạt thứ hai' hay 'Đà Lạt của Kon Tum'. Bao quanh thị trấn nhỏ là những cánh rừng thông xanh ngút ngàn xen lẫn rừng nguyên sinh, cùng hệ thống hồ và thác nước đẹp như hồ Đăk Ke, thác Pa Sỹ, thác Đăk Ke, tạo nên khung cảnh nên thơ, mờ ảo trong sương sớm. Nhờ độ cao và rừng bao phủ, khí hậu Măng Đen mát mẻ, trong lành quanh năm, ban đêm se lạnh, rất dễ chịu so với cái nóng của vùng thấp. Du khách đến đây để tản bộ giữa rừng thông, cắm trại, câu cá, thưởng thức đặc sản như gà nướng, cá tầm, cá hồi nuôi ở vùng nước lạnh, rau rừng và rượu sim. Một điểm đến tâm linh nổi tiếng là tượng Đức Mẹ Măng Đen giữa rừng, thu hút đông đảo khách hành hương. Vùng đất này còn là nơi sinh sống của các dân tộc bản địa như Mơ Nâm, Xơ Đăng với những nét văn hóa, nhà rông, cồng chiêng đặc sắc. Còn khá hoang sơ và yên tĩnh, Măng Đen phù hợp với những ai muốn tìm một chốn nghỉ dưỡng gần gũi thiên nhiên, tránh xa ồn ào phố thị.",
  "presentation_long_en": "At around 1,200 m on the Kon Plong plateau, Mang Den in Quang Ngai province (formerly Kon Tum) is a rising resort of the Central Highlands, fondly called a 'second Da Lat' or the 'Da Lat of Kon Tum'. The little town is ringed by endless green pine forests mingled with old-growth woods, and by lovely lakes and waterfalls such as Dak Ke Lake, Pa Sy Falls and Dak Ke Falls, forming poetic scenery veiled in morning mist. Thanks to its altitude and forest cover, Mang Den enjoys a cool, fresh climate all year, with chilly nights that are a relief from the heat of the lowlands. Visitors come to stroll among the pines, camp, fish and enjoy specialities such as grilled chicken, sturgeon and salmon raised in cold water, wild greens and rose-myrtle wine. A famous spiritual site is the statue of Our Lady of Mang Den in the forest, which draws many pilgrims. The area is also home to indigenous peoples such as the Mo Nam and Xo Dang, with distinctive culture, communal 'rong' houses and gong music. Still fairly wild and quiet, Mang Den suits anyone seeking a retreat close to nature, far from the noise of the city.",
  "presentation_long_ru": "На высоте около 1200 м на плато Конплонг Мангден в провинции Куангнгай (прежде Контум) — восходящий курорт Центрального нагорья, ласково называемый «вторым Далатом» или «Далатом Контума». Городок окружён бескрайними зелёными сосновыми лесами вперемешку с девственными чащами, а также красивыми озёрами и водопадами — озером Дакке, водопадами Пашы и Дакке, — образующими поэтичный пейзаж, окутанный утренним туманом. Благодаря высоте и лесному покрову в Мангдене круглый год прохладный, свежий климат с холодными ночами, что спасает от жары низин. Гости приезжают гулять среди сосен, ставить палатки, рыбачить и пробовать местные блюда — жареную курицу, осетра и лосося, выращенных в холодной воде, дикие травы и вино из розовой мирты. Знаменитое духовное место — статуя Богоматери Мангден в лесу, привлекающая множество паломников. В этих краях живут коренные народы мономам и седанг с самобытной культурой, общинными домами «ронг» и музыкой гонгов. Ещё довольно дикий и тихий, Мангден подходит тем, кто ищет уединение рядом с природой, вдали от городского шума.",
  "highlights_vi": [
    "'Đà Lạt thứ hai' của Tây Nguyên: rừng thông, hồ, thác, khí hậu mát lạnh",
    "Tượng Đức Mẹ Măng Đen – điểm hành hương nổi tiếng giữa rừng",
    "Đặc sản cá tầm, gà nướng và văn hóa các dân tộc Mơ Nâm, Xơ Đăng"
  ],
  "highlights_en": [
    "A 'second Da Lat' of the highlands: pine forests, lakes, falls, cool climate",
    "The statue of Our Lady of Mang Den — a famous forest pilgrimage site",
    "Sturgeon and grilled-chicken specialities and Mo Nam / Xo Dang culture"
  ],
  "highlights_ru": [
    "«Второй Далат» нагорья: сосновые леса, озёра, водопады, прохладный климат",
    "Статуя Богоматери Мангден — знаменитое место паломничества в лесу",
    "Деликатесы из осетра и жареной курицы и культура народов мономам и седанг"
  ],
  "practical": {
    "hours_vi": "Thị trấn mở cả ngày; các điểm tham quan theo giờ riêng.",
    "ticket_vi": "Không có vé chung; một số thác, khu vui chơi thu phí nhỏ.",
    "duration_vi": "1–2 ngày.",
    "best_time_vi": "Quanh năm mát; mùa hoa (sim, mai anh đào) đầu năm rất đẹp.",
    "tips_vi": "Mang áo ấm; đặt phòng trước dịp lễ; đường đèo lên Măng Đen nên đi ban ngày."
  },
  "tags": ["highland", "cool-climate", "nature", "pine-forest", "pilgrimage", "top"],
  "sources": [{"title": "Wikipedia (VI) — Măng Đen", "url": "https://vi.wikipedia.org/wiki/M%C4%83ng_%C4%90en"}]
})

add({
  "region": "vn-quang-ngai", "slug": "nha-tho-go-kon-tum",
  "region_name_vi": "Quảng Ngãi", "federal_district": "Miền Trung",
  "name_vi": "Nhà thờ gỗ Kon Tum",
  "name_en": "Kon Tum Wooden Church",
  "name_ru": "Деревянная церковь Контум",
  "categories": ["church"],
  "coordinates": {"lat": 14.3533, "lon": 108.0067},
  "address_vi": "Phường Thống Nhất (TP Kon Tum cũ), tỉnh Quảng Ngãi",
  "rating": {"value": 4.7, "count": 4000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Nhà thờ gỗ hơn trăm tuổi kiến trúc Roman kết hợp nhà sàn Ba Na, màu nâu trầm rất đẹp. Du khách thích chụp ảnh, không gian yên bình; nên vào giờ mở cửa, giữ trật tự vì là nơi thờ phụng.",
  "presentation_short_vi": "Nhà thờ gỗ Kon Tum là ngôi nhà thờ Công giáo hơn một thế kỷ tuổi, được xây hoàn toàn bằng gỗ theo phong cách Roman kết hợp kiến trúc nhà sàn của người Ba Na bản địa. Với màu nâu trầm ấm và những chi tiết chạm khắc tinh tế, đây là một trong những công trình biểu tượng và được chụp ảnh nhiều nhất ở Tây Nguyên.",
  "presentation_short_en": "The Kon Tum Wooden Church is a Catholic church over a century old, built entirely of timber in a Romanesque style blended with the stilt-house architecture of the local Ba Na people. With its warm dark-brown tones and fine carvings, it is one of the most iconic and most photographed buildings in the Central Highlands.",
  "presentation_short_ru": "Деревянная церковь Контум — католический храм возрастом более века, полностью построенный из дерева в романском стиле в сочетании со свайной архитектурой местного народа бана. С тёплыми тёмно-коричневыми тонами и тонкой резьбой это одно из самых знаковых и фотографируемых сооружений Центрального нагорья.",
  "presentation_long_vi": "Tọa lạc ở trung tâm thành phố Kon Tum cũ, nay thuộc tỉnh Quảng Ngãi, Nhà thờ gỗ Kon Tum (tên chính thức là Nhà thờ Chính tòa Kon Tum) được các linh mục người Pháp khởi xướng và hoàn thành vào năm 1918. Điều làm nên sự độc đáo của công trình là toàn bộ được dựng bằng gỗ cà chít (sến đỏ) bền chắc, tường trát bằng hỗn hợp rơm trộn đất theo lối truyền thống, và đặc biệt là sự giao thoa tài tình giữa kiến trúc Roman phương Tây với hình dáng nhà sàn, nhà rông của người Ba Na Tây Nguyên. Nhà thờ nổi bật với gam màu nâu trầm ấm, mái ngói cao vút, tháp chuông vươn lên trời cùng những khung cửa, hàng cột, vòm trần bằng gỗ được chạm khắc tinh xảo; ánh sáng lọc qua các ô kính màu tạo nên không gian lung linh, tĩnh lặng bên trong. Khuôn viên rộng rãi còn có nhà trưng bày các sản phẩm thủ công, dệt thổ cẩm và sinh hoạt của cộng đồng giáo dân người dân tộc. Trải qua hơn một trăm năm dưới nắng gió cao nguyên, nhà thờ vẫn vững chãi và đẹp cổ kính, trở thành biểu tượng văn hóa – kiến trúc của vùng đất Kon Tum và là điểm đến không thể bỏ qua với du khách khi khám phá Bắc Tây Nguyên.",
  "presentation_long_en": "In the centre of the former Kon Tum city, now in Quang Ngai province, the Kon Tum Wooden Church (officially Kon Tum Cathedral) was begun by French priests and completed in 1918. What makes it unique is that it is built entirely of durable ca chit (red ironwood) timber, its walls plastered with a traditional mix of straw and earth, and above all its masterful blend of Western Romanesque architecture with the stilt-house and communal 'rong' house forms of the highland Ba Na people. The church stands out for its warm dark-brown tones, soaring tiled roof and bell tower reaching skyward, and its finely carved wooden doors, columns and vaulted ceilings; light filtering through stained-glass panes fills the interior with a shimmering, hushed atmosphere. The spacious grounds also hold a display of handicrafts, brocade weaving and the life of the local ethnic Catholic community. After more than a hundred years under the highland sun and wind, the church remains sturdy and beautifully old, an architectural and cultural symbol of Kon Tum and an unmissable stop for travellers exploring the northern Central Highlands.",
  "presentation_long_ru": "В центре бывшего города Контум, ныне в провинции Куангнгай, Деревянная церковь Контум (официально — кафедральный собор Контума) была начата французскими священниками и завершена в 1918 году. Её уникальность в том, что она целиком построена из прочного дерева качить (красного железного дерева), стены оштукатурены традиционной смесью соломы и глины, и прежде всего в искусном соединении западной романской архитектуры с формами свайного и общинного дома «ронг» горного народа бана. Церковь выделяется тёплыми тёмно-коричневыми тонами, взмывающей черепичной крышей и колокольней, устремлённой в небо, а также тонко резными деревянными дверями, колоннами и сводчатыми потолками; свет, проходящий сквозь витражи, наполняет интерьер мерцающей, притихшей атмосферой. На просторной территории есть также экспозиция ремёсел, ткачества и жизни местной этнической католической общины. Более чем через сто лет под солнцем и ветром нагорья церковь остаётся крепкой и красиво старинной, архитектурно-культурным символом Контума и обязательной остановкой для путешественников по северу Центрального нагорья. Вечером, подсвеченная тёплым светом, церковь выглядит особенно живописно, а на Рождество площадь перед храмом наполняется прихожанами разных народностей.",
  "highlights_vi": [
    "Nhà thờ hoàn toàn bằng gỗ, hoàn thành năm 1918, hơn một thế kỷ tuổi",
    "Giao thoa kiến trúc Roman và nhà sàn, nhà rông của người Ba Na",
    "Màu nâu trầm ấm, chạm khắc gỗ tinh xảo, biểu tượng của Kon Tum"
  ],
  "highlights_en": [
    "An all-timber church completed in 1918, over a century old",
    "A fusion of Romanesque architecture with Ba Na stilt- and 'rong'-house forms",
    "Warm dark-brown tones and fine woodcarving — a symbol of Kon Tum"
  ],
  "highlights_ru": [
    "Полностью деревянная церковь, завершённая в 1918 году, старше века",
    "Сплав романской архитектуры со свайными домами и «ронг» народа бана",
    "Тёплые тёмно-коричневые тона и тонкая резьба — символ Контума"
  ],
  "practical": {
    "hours_vi": "Mở cửa ban ngày; giờ lễ có thể hạn chế tham quan.",
    "ticket_vi": "Vào cửa miễn phí.",
    "duration_vi": "Khoảng 30–45 phút.",
    "best_time_vi": "Sáng hoặc chiều muộn cho ánh sáng đẹp; dịp Giáng sinh rất đông.",
    "tips_vi": "Ăn mặc lịch sự, giữ yên tĩnh; kết hợp thăm cầu treo Kon Klor, nhà rông gần đó."
  },
  "tags": ["church", "architecture", "heritage", "photography", "culture"],
  "sources": [{"title": "Wikipedia (VI) — Nhà thờ chính tòa Kon Tum", "url": "https://vi.wikipedia.org/wiki/Nh%C3%A0_th%E1%BB%9D_ch%C3%ADnh_t%C3%B2a_Kon_Tum"}]
})

add({
  "region": "vn-quang-ngai", "slug": "khu-chung-tich-son-my",
  "region_name_vi": "Quảng Ngãi", "federal_district": "Miền Trung",
  "name_vi": "Khu chứng tích Sơn Mỹ",
  "name_en": "Son My (My Lai) Memorial",
  "name_ru": "Мемориал Шонми (Милай)",
  "categories": ["monument", "museum"],
  "coordinates": {"lat": 15.1783, "lon": 108.8590},
  "address_vi": "Xã Tịnh Khê (Sơn Mỹ), tỉnh Quảng Ngãi",
  "rating": {"value": 4.6, "count": 1800, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Nơi tưởng niệm nạn nhân vụ thảm sát Sơn Mỹ 1968 – địa điểm lịch sử đau thương, nhắc nhở về hòa bình. Du khách lặng lẽ, xúc động trước tượng đài, nhà trưng bày hiện vật và ảnh tư liệu; không gian trang nghiêm.",
  "presentation_short_vi": "Khu chứng tích Sơn Mỹ ở tỉnh Quảng Ngãi là nơi tưởng niệm các nạn nhân của vụ thảm sát Sơn Mỹ (Mỹ Lai) ngày 16/3/1968, khi hàng trăm dân thường vô tội bị lính Mỹ sát hại. Khu di tích gồm tượng đài, nhà trưng bày và các dấu tích, là biểu tượng nhắc nhở về nỗi đau chiến tranh và khát vọng hòa bình.",
  "presentation_short_en": "The Son My Memorial in Quang Ngai province commemorates the victims of the Son My (My Lai) massacre of 16 March 1968, when hundreds of innocent civilians were killed by US soldiers. With its monument, museum and preserved traces, it stands as a symbol recalling the pain of war and the longing for peace.",
  "presentation_short_ru": "Мемориал Шонми в провинции Куангнгай увековечивает память жертв бойни в Шонми (Милай) 16 марта 1968 года, когда сотни ни в чём не повинных мирных жителей были убиты американскими солдатами. С монументом, музеем и сохранёнными следами он служит символом, напоминающим о боли войны и стремлении к миру.",
  "presentation_long_vi": "Nằm ở xã Tịnh Khê, tỉnh Quảng Ngãi, Khu chứng tích Sơn Mỹ là nơi ghi dấu một trong những trang bi thương nhất của chiến tranh Việt Nam. Sáng ngày 16 tháng 3 năm 1968, trong vụ thảm sát mà thế giới biết đến với tên gọi Sơn Mỹ hay Mỹ Lai, lính Mỹ đã sát hại 504 thường dân vô tội – phần lớn là người già, phụ nữ và trẻ em – tại các xóm làng nơi đây. Sự kiện khi được phơi bày đã gây chấn động dư luận quốc tế, góp phần thổi bùng phong trào phản chiến trên khắp thế giới và trở thành một biểu tượng đau đớn về hậu quả của chiến tranh đối với dân thường. Ngày nay, khu chứng tích được xây dựng ngay trên vùng đất diễn ra thảm kịch, gồm tượng đài tưởng niệm khắc họa nỗi đau và sự kiên cường, nhà trưng bày lưu giữ nhiều hình ảnh tư liệu, hiện vật và danh sách các nạn nhân, cùng những dấu tích như nền nhà, con mương, gốc cây được gìn giữ. Không gian nơi đây tĩnh lặng, trang nghiêm và đầy xúc động; nhiều du khách trong và ngoài nước, trong đó có cả cựu binh Mỹ, đã tìm đến để tưởng niệm, sám hối và bày tỏ mong ước về một thế giới không còn chiến tranh. Sơn Mỹ không chỉ là một địa chỉ lịch sử mà còn là lời nhắc nhở sâu sắc về giá trị của hòa bình và lòng nhân đạo.",
  "presentation_long_en": "In Tinh Khe commune, Quang Ngai province, the Son My Memorial marks one of the most tragic pages of the Vietnam War. On the morning of 16 March 1968, in the massacre the world knows as Son My or My Lai, US soldiers killed 504 innocent civilians — mostly the elderly, women and children — in the hamlets here. When it was exposed, the event shocked international opinion, helped fuel the anti-war movement worldwide and became a painful symbol of war's toll on civilians. Today the memorial stands on the very ground of the tragedy, with a monument depicting suffering and resilience, a museum preserving documentary photographs, artefacts and the list of victims, and traces such as house foundations, a ditch and tree stumps that have been kept. The place is quiet, solemn and deeply moving; many visitors, Vietnamese and foreign, including US veterans, have come to remember, to repent and to voice their hope for a world without war. Son My is not only a historical site but a profound reminder of the value of peace and of human compassion.",
  "presentation_long_ru": "В общине Тиньке провинции Куангнгай мемориал Шонми отмечает одну из самых трагических страниц Вьетнамской войны. Утром 16 марта 1968 года в бойне, известной миру как Шонми или Милай, американские солдаты убили 504 ни в чём не повинных мирных жителя — в основном стариков, женщин и детей — в здешних деревнях. Когда это было раскрыто, событие потрясло международное мнение, помогло разжечь антивоенное движение по всему миру и стало болезненным символом того, чего война стоит мирным людям. Сегодня мемориал стоит на самой земле трагедии: монумент, изображающий страдание и стойкость, музей с документальными снимками, артефактами и списком жертв, а также сохранённые следы — фундаменты домов, канава и пни деревьев. Место тихое, торжественное и глубоко трогательное; многие гости, вьетнамцы и иностранцы, включая американских ветеранов, приходили сюда, чтобы помянуть, покаяться и выразить надежду на мир без войн. Шонми — не только историческое место, но и глубокое напоминание о ценности мира и человеческого сострадания. Тихие дорожки среди зелени, скульптуры и уцелевшие следы деревни помогают посетителям в молчании осмыслить произошедшее и почтить память погибших.",
  "highlights_vi": [
    "Nơi tưởng niệm 504 nạn nhân vụ thảm sát Sơn Mỹ (Mỹ Lai) ngày 16/3/1968",
    "Tượng đài, nhà trưng bày hiện vật, ảnh tư liệu và các dấu tích được gìn giữ",
    "Biểu tượng về nỗi đau chiến tranh và khát vọng hòa bình"
  ],
  "highlights_en": [
    "Memorial to the 504 victims of the Son My (My Lai) massacre of 16 March 1968",
    "A monument, museum, documentary photos and preserved traces of the tragedy",
    "A symbol of war's suffering and the longing for peace"
  ],
  "highlights_ru": [
    "Мемориал 504 жертвам бойни в Шонми (Милай) 16 марта 1968 года",
    "Монумент, музей, документальные снимки и сохранённые следы трагедии",
    "Символ страданий войны и стремления к миру"
  ],
  "practical": {
    "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
    "ticket_vi": "Vé vào cửa tượng trưng khoảng 10.000–20.000 VND.",
    "duration_vi": "Khoảng 1 giờ.",
    "best_time_vi": "Quanh năm; ngày 16/3 có lễ tưởng niệm.",
    "tips_vi": "Giữ thái độ trang nghiêm, tôn trọng; nên nghe thuyết minh để hiểu bối cảnh lịch sử."
  },
  "tags": ["history", "war", "memorial", "peace", "museum"],
  "sources": [{"title": "Wikipedia (VI) — Thảm sát Sơn Mỹ", "url": "https://vi.wikipedia.org/wiki/Th%E1%BA%A3m_s%C3%A1t_S%C6%A1n_M%E1%BB%B9"}]
})

# ---------- ĐỒNG NAI (gồm Bình Phước cũ) ----------
add({
  "region": "vn-dong-nai", "slug": "vqg-cat-tien",
  "region_name_vi": "Đồng Nai", "federal_district": "Miền Nam",
  "name_vi": "Vườn quốc gia Cát Tiên",
  "name_en": "Cat Tien National Park",
  "name_ru": "Национальный парк Каттьен",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 11.4210, "lon": 107.3676},
  "address_vi": "Vườn quốc gia Cát Tiên, tỉnh Đồng Nai (giáp Lâm Đồng)",
  "rating": {"value": 4.6, "count": 3500, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Rừng nhiệt đới nguyên sinh rộng lớn, xem thú đêm, ngắm chim, đạp xe và trekking Bàu Sấu rất đáng. Du khách khen thiên nhiên hoang sơ, cây cổ thụ; cần chuẩn bị chống muỗi, vắt và đặt tour trước.",
  "presentation_short_vi": "Vườn quốc gia Cát Tiên là một trong những khu rừng nhiệt đới nguyên sinh lớn và quan trọng nhất Nam Bộ, trải trên địa phận Đồng Nai và các tỉnh lân cận. Nơi đây có hệ động thực vật phong phú, nổi tiếng với hoạt động xem thú đêm, ngắm chim, cây tung cổ thụ và khu đất ngập nước Bàu Sấu.",
  "presentation_short_en": "Cat Tien National Park is one of the largest and most important tracts of primary tropical forest in southern Vietnam, spanning Dong Nai and neighbouring provinces. It shelters rich flora and fauna and is famous for night safaris, birdwatching, giant tung trees and the Bau Sau (Crocodile Lake) wetlands.",
  "presentation_short_ru": "Национальный парк Каттьен — один из крупнейших и важнейших массивов первичного тропического леса юга Вьетнама, охватывающий Донгнай и соседние провинции. Он хранит богатую флору и фауну и знаменит ночными сафари, наблюдением за птицами, гигантскими деревьями тунг и водно-болотными угодьями Баушау (Крокодилье озеро).",
  "presentation_long_vi": "Nằm cách Thành phố Hồ Chí Minh khoảng 150 km, Vườn quốc gia Cát Tiên là một trong những khu bảo tồn thiên nhiên quan trọng bậc nhất của Việt Nam, với phần lớn diện tích thuộc tỉnh Đồng Nai. Đây là mảng rừng nhiệt đới ẩm thường xanh còn khá nguyên vẹn ở vùng Đông Nam Bộ, được UNESCO công nhận là Khu dự trữ sinh quyển thế giới Đồng Nai, và khu đất ngập nước Bàu Sấu được ghi vào danh sách Ramsar quốc tế. Cát Tiên có sự đa dạng sinh học đáng kinh ngạc với hàng nghìn loài thực vật, hàng trăm loài chim, thú, bò sát, trong đó nhiều loài quý hiếm. Du khách đến đây có thể tham gia nhiều trải nghiệm: đi bộ hoặc đạp xe trong rừng để chiêm ngưỡng những cây tung, cây gõ cổ thụ hàng trăm năm tuổi với bộ rễ bạnh khổng lồ; tour xem thú đêm bằng xe để bắt gặp nai, hoẵng, thỏ rừng; ngắm chim vào sáng sớm; và đặc biệt là chuyến trekking kết hợp chèo thuyền tới Bàu Sấu để quan sát cá sấu nước ngọt cùng đời sống chim nước. Ngoài ra còn có điểm tham quan Ghềnh Bến Cự, khu cứu hộ gấu và các bản làng người Mạ, S'Tiêng bản địa. Với không gian rừng già hoang sơ, trong lành, Cát Tiên là điểm đến lý tưởng cho những người yêu thiên nhiên, thích khám phá và du lịch sinh thái bền vững.",
  "presentation_long_en": "About 150 km from Ho Chi Minh City, Cat Tien National Park is one of Vietnam's most important nature reserves, most of it in Dong Nai province. It is a fairly intact tract of evergreen humid tropical forest in the south-east, recognised by UNESCO within the Dong Nai World Biosphere Reserve, while its Bau Sau wetland is listed as a Ramsar site of international importance. Cat Tien holds astonishing biodiversity, with thousands of plant species and hundreds of birds, mammals and reptiles, many of them rare. Visitors can enjoy many experiences: walking or cycling through the forest to admire centuries-old tung and go trees with giant buttress roots; night safaris by vehicle to spot deer, muntjac and wild hares; birdwatching at dawn; and above all a trek combined with a boat trip to Bau Sau (Crocodile Lake) to watch freshwater crocodiles and waterbird life. There are also the Ben Cu rapids, a bear rescue centre and villages of the indigenous Ma and S'Tieng peoples. With its wild, fresh old-growth forest, Cat Tien is an ideal destination for nature lovers and for those who enjoy exploration and sustainable eco-tourism.",
  "presentation_long_ru": "Примерно в 150 км от Хошимина национальный парк Каттьен — один из важнейших природных заповедников Вьетнама, большая часть которого находится в провинции Донгнай. Это довольно нетронутый массив вечнозелёного влажного тропического леса на юго-востоке, признанный ЮНЕСКО в составе Всемирного биосферного заповедника Донгнай, а его водно-болотное угодье Баушау внесено в список рамсарских угодий международного значения. Каттьен обладает поразительным биоразнообразием: тысячи видов растений и сотни видов птиц, млекопитающих и рептилий, многие из которых редки. Гостей ждёт множество занятий: пешие или велосипедные прогулки по лесу, чтобы полюбоваться вековыми деревьями тунг и го с гигантскими досковидными корнями; ночные сафари на машине, чтобы заметить оленей, мунтжаков и диких зайцев; наблюдение за птицами на рассвете; и прежде всего трек в сочетании с лодочной прогулкой к Баушау (Крокодильему озеру) для наблюдения за пресноводными крокодилами и жизнью водных птиц. Есть также пороги Бенкы, центр спасения медведей и деревни коренных народов ма и стиенг. С диким, свежим девственным лесом Каттьен — идеальное место для любителей природы и тех, кто ценит исследование и устойчивый экотуризм.",
  "highlights_vi": [
    "Rừng nhiệt đới nguyên sinh lớn, thuộc Khu dự trữ sinh quyển Đồng Nai (UNESCO)",
    "Xem thú đêm, ngắm chim, cây tung – gõ cổ thụ rễ bạnh khổng lồ",
    "Trekking – chèo thuyền Bàu Sấu (khu Ramsar) xem cá sấu, chim nước"
  ],
  "highlights_en": [
    "A large primary tropical forest within the Dong Nai UNESCO Biosphere Reserve",
    "Night safaris, birdwatching and ancient tung and go trees with giant buttress roots",
    "Trek-and-boat trips to Bau Sau (a Ramsar site) for crocodiles and waterbirds"
  ],
  "highlights_ru": [
    "Большой первичный тропический лес в биосферном заповеднике Донгнай (ЮНЕСКО)",
    "Ночные сафари, наблюдение за птицами и вековые деревья тунг и го",
    "Трек и лодка к Баушау (рамсарское угодье) — крокодилы и водные птицы"
  ],
  "practical": {
    "hours_vi": "Đón khách ban ngày; tour xem thú đêm theo lịch riêng.",
    "ticket_vi": "Vé vào vườn và các tour (Bàu Sấu, xem thú đêm) tính riêng.",
    "duration_vi": "1–2 ngày (nên nghỉ đêm để xem thú).",
    "best_time_vi": "Mùa khô (tháng 12–5); Bàu Sấu đẹp cuối mùa mưa.",
    "tips_vi": "Đặt tour và phòng trước; mang chống muỗi, vắt, giày lội nước; tuân thủ hướng dẫn kiểm lâm."
  },
  "tags": ["national-park", "nature", "wildlife", "trekking", "eco", "top"],
  "sources": [{"title": "Wikipedia (VI) — Vườn quốc gia Cát Tiên", "url": "https://vi.wikipedia.org/wiki/V%C6%B0%E1%BB%9Dn_qu%E1%BB%91c_gia_C%C3%A1t_Ti%C3%AAn"}]
})

add({
  "region": "vn-dong-nai", "slug": "nui-chua-chan",
  "region_name_vi": "Đồng Nai", "federal_district": "Miền Nam",
  "name_vi": "Núi Chứa Chan (Gia Ray)",
  "name_en": "Chua Chan Mountain (Gia Ray)",
  "name_ru": "Гора Тьыатян (Зярай)",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 10.9333, "lon": 107.4000},
  "address_vi": "Huyện Xuân Lộc, tỉnh Đồng Nai",
  "rating": {"value": 4.4, "count": 2000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Ngọn núi cao thứ hai Nam Bộ, leo núi/cắm trại săn mây và biển đồng bằng dưới chân. Du khách thích cáp treo lên chùa Bửu Quang, cây đa ba gốc một ngọn; đường leo bộ khá dốc nên cần sức khỏe.",
  "presentation_short_vi": "Núi Chứa Chan (còn gọi là núi Gia Ray) ở huyện Xuân Lộc, tỉnh Đồng Nai là ngọn núi cao thứ hai Nam Bộ, chỉ sau núi Bà Đen. Với độ cao hơn 800 m, đây là điểm leo núi, cắm trại săn mây quen thuộc, đồng thời có chùa Bửu Quang (chùa Gia Lào) và hệ thống cáp treo đưa khách hành hương lên núi.",
  "presentation_short_en": "Chua Chan Mountain (also called Gia Ray) in Xuan Loc district, Dong Nai province, is the second-highest peak in southern Vietnam after Ba Den Mountain. Rising above 800 m, it is a popular spot for hiking and cloud-hunting camps, and also home to Buu Quang Pagoda (Gia Lao Pagoda) and a cable car that carries pilgrims up the slope.",
  "presentation_short_ru": "Гора Тьыатян (также называемая Зярай) в уезде Суанлок провинции Донгнай — вторая по высоте вершина юга Вьетнама после горы Баден. Поднимаясь выше 800 м, она популярна для походов и лагерей «охоты за облаками», а также хранит пагоду Быукуанг (Зялао) и канатную дорогу, поднимающую паломников по склону.",
  "presentation_long_vi": "Sừng sững giữa vùng đồng bằng huyện Xuân Lộc, tỉnh Đồng Nai, núi Chứa Chan – tên dân gian là núi Gia Ray – cao khoảng 837 m, được xem là 'nóc nhà' thứ hai của Nam Bộ, chỉ sau núi Bà Đen ở Tây Ninh. Ngọn núi có hình dáng vòng cung mềm mại, quanh năm cây cối xanh tươi, khí hậu trên đỉnh mát mẻ, và đặc biệt vào sáng sớm thường xuất hiện biển mây bồng bềnh khiến nơi đây trở thành điểm 'săn mây' hấp dẫn của giới trẻ và dân phượt. Có hai cách chinh phục núi: leo bộ theo các bậc thang và đường mòn xuyên rừng để rèn luyện sức khỏe và cắm trại qua đêm ngắm bình minh, hoặc đi cáp treo hiện đại vượt sườn núi lên khu vực chùa. Trên lưng chừng núi có chùa Bửu Quang, quen gọi là chùa Gia Lào, một ngôi chùa linh thiêng nép mình bên vách đá, thu hút đông đảo phật tử và du khách hành hương, nhất là dịp đầu năm. Trên đường lên chùa, du khách sẽ gặp cây đa 'ba gốc một ngọn' độc đáo cùng nhiều hang, điện thờ. Từ trên cao phóng tầm mắt, cả một vùng đồng bằng, ruộng vườn, hồ Núi Le và thị trấn Gia Ray hiện ra khoáng đạt. Vừa mang giá trị tâm linh, vừa là điểm dã ngoại – thể thao leo núi, Chứa Chan là lựa chọn cuối tuần thú vị cho người dân khu vực và du khách phương xa.",
  "presentation_long_en": "Rising over the plains of Xuan Loc district in Dong Nai province, Chua Chan Mountain — popularly Gia Ray — is about 837 m high and reckoned the second 'roof' of southern Vietnam after Ba Den in Tay Ninh. Gently arc-shaped and green all year, it has a cool summit and, especially at dawn, often gathers a drifting sea of cloud that makes it an appealing 'cloud-hunting' spot for young people and backpackers. There are two ways up: climbing steps and forest trails for exercise and overnight camping to watch the sunrise, or taking a modern cable car up the slope to the pagoda area. Partway up stands Buu Quang Pagoda, commonly called Gia Lao Pagoda, a sacred temple tucked against the cliffs that draws crowds of Buddhists and pilgrims, especially at the start of the year. On the way up, visitors pass a curious 'three-trunk, one-crown' banyan and various caves and shrines. From the heights the eye sweeps over the plains, fields, Nui Le Lake and Gia Ray town. Both spiritual and a place for outings and mountain sport, Chua Chan is an enjoyable weekend choice for local people and travellers from afar.",
  "presentation_long_ru": "Возвышаясь над равнинами уезда Суанлок в провинции Донгнай, гора Тьыатян — в народе Зярай — высотой около 837 м считается вторым «домом-крышей» юга Вьетнама после Бадена в Тайнине. Плавно дугообразная и зелёная круглый год, она имеет прохладную вершину и, особенно на рассвете, часто собирает плывущее море облаков, что делает её привлекательным местом «охоты за облаками» для молодёжи и туристов с рюкзаками. Наверх ведут два пути: подъём по ступеням и лесным тропам ради нагрузки и ночёвки с палаткой для встречи рассвета или современная канатная дорога по склону к району пагоды. На полпути стоит пагода Быукуанг, обычно называемая Зялао, — священный храм, прижавшийся к скалам, привлекающий толпы буддистов и паломников, особенно в начале года. По пути наверх гости минуют любопытный баньян «три ствола — одна крона» и разные пещеры и святилища. С высот взгляд охватывает равнины, поля, озеро Нуйле и городок Зярай. Одновременно духовная и место для прогулок и горного спорта, Тьыатян — приятный выбор на выходные для местных жителей и приезжих издалека.",
  "highlights_vi": [
    "Núi cao thứ hai Nam Bộ (837 m), điểm săn mây, cắm trại, leo núi",
    "Chùa Bửu Quang (Gia Lào) linh thiêng bên vách đá, có cáp treo",
    "Cây đa 'ba gốc một ngọn' độc đáo và tầm nhìn bao quát đồng bằng"
  ],
  "highlights_en": [
    "The second-highest peak in the south (837 m) for cloud-hunting, camping and hiking",
    "Sacred Buu Quang (Gia Lao) Pagoda against the cliffs, served by a cable car",
    "A curious 'three-trunk, one-crown' banyan and sweeping plain views"
  ],
  "highlights_ru": [
    "Вторая по высоте вершина юга (837 м) для охоты за облаками, кемпинга и походов",
    "Священная пагода Быукуанг (Зялао) у скал с канатной дорогой",
    "Любопытный баньян «три ствола — одна крона» и широкие виды равнины"
  ],
  "practical": {
    "hours_vi": "Leo núi cả ngày; cáp treo và chùa theo giờ mở.",
    "ticket_vi": "Cáp treo khứ hồi tham khảo khoảng 150.000–250.000 VND; leo bộ miễn phí.",
    "duration_vi": "Nửa ngày (cáp treo) đến 1 ngày (leo bộ, cắm trại).",
    "best_time_vi": "Mùa khô; sáng sớm để săn mây.",
    "tips_vi": "Chuẩn bị nước, giày leo núi nếu đi bộ; theo dõi thời tiết; đầu năm chùa rất đông."
  },
  "tags": ["mountain", "hiking", "camping", "temple", "viewpoint"],
  "sources": [{"title": "Wikipedia (VI) — Núi Chứa Chan", "url": "https://vi.wikipedia.org/wiki/N%C3%BAi_Ch%E1%BB%A9a_Chan"}]
})

add({
  "region": "vn-dong-nai", "slug": "khu-du-lich-buu-long",
  "region_name_vi": "Đồng Nai", "federal_district": "Miền Nam",
  "name_vi": "Khu du lịch Bửu Long",
  "name_en": "Buu Long Tourist Area",
  "name_ru": "Туристическая зона Быулонг",
  "categories": ["park_garden", "other"],
  "coordinates": {"lat": 10.9528, "lon": 106.8156},
  "address_vi": "Phường Bửu Long, thành phố Biên Hòa, tỉnh Đồng Nai",
  "rating": {"value": 4.3, "count": 6000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Được ví 'vịnh Hạ Long thu nhỏ' với hồ Long Ẩn nước xanh ngọc, vách đá và chùa trên núi. Du khách thích chèo thuyền, chụp ảnh, không gian gần Sài Gòn; cuối tuần khá đông, có thu phí dịch vụ.",
  "presentation_short_vi": "Khu du lịch Bửu Long ở thành phố Biên Hòa được mệnh danh là 'vịnh Hạ Long thu nhỏ' của Nam Bộ, với hồ Long Ẩn nước xanh ngọc bích in bóng những vách đá và cột đá kỳ thú do khai thác đá để lại. Trong khu còn có núi Bửu Long, chùa Bửu Phong cổ kính và không gian cây xanh thoáng mát gần Sài Gòn.",
  "presentation_short_en": "The Buu Long Tourist Area in Bien Hoa city is dubbed a 'miniature Ha Long Bay' of the south, with the jade-green Long An Lake reflecting striking cliffs and rock pillars left by old quarrying. It also holds Buu Long hill, the ancient Buu Phong Pagoda and green, airy grounds close to Saigon.",
  "presentation_short_ru": "Туристическая зона Быулонг в городе Бьенхоа прозвана «миниатюрной бухтой Халонг» юга, с нефритово-зелёным озером Лонган, отражающим эффектные скалы и каменные столбы, оставшиеся от старой добычи камня. Здесь также есть холм Быулонг, старинная пагода Быуфонг и зелёная, просторная территория рядом с Сайгоном.",
  "presentation_long_vi": "Nằm bên bờ sông Đồng Nai, thuộc thành phố Biên Hòa, Khu du lịch Bửu Long là một trong những điểm dã ngoại quen thuộc và được yêu thích ở khu vực Đông Nam Bộ, chỉ cách Thành phố Hồ Chí Minh khoảng 30 km. Điểm nhấn nổi tiếng nhất nơi đây là hồ Long Ẩn – một hồ nước nhân tạo rộng, hình thành sau quá trình khai thác đá lâu năm, với làn nước xanh màu ngọc bích trong veo, nổi bật giữa những vách đá dựng đứng và các cột đá, đảo đá nhô lên mặt nước tạo nên khung cảnh kỳ ảo, được ví như 'vịnh Hạ Long thu nhỏ'. Du khách có thể thuê thuyền đạp vịt, thuyền kayak dạo quanh hồ, chụp ảnh bên những mỏm đá đẹp như tranh. Bên cạnh hồ là núi Bửu Long với cụm chùa cổ Bửu Phong có lịch sử hàng trăm năm, kiến trúc chạm khắc tinh xảo, nơi du khách leo những bậc đá lên viếng chùa và ngắm toàn cảnh vùng sông nước Biên Hòa. Trong khuôn viên rộng lớn còn có công viên, khu vui chơi, vườn tượng, cây xanh rợp bóng thích hợp cho các gia đình, nhóm bạn tổ chức picnic, cắm trại nhẹ nhàng. Nhờ cảnh quan độc đáo, không khí trong lành và vị trí thuận tiện, Bửu Long là lựa chọn nghỉ ngơi cuối tuần lý tưởng cho cư dân đô thị phương Nam.",
  "presentation_long_en": "On the bank of the Dong Nai River in Bien Hoa city, the Buu Long Tourist Area is one of the best-loved outing spots in the south-east, only about 30 km from Ho Chi Minh City. Its most famous feature is Long An Lake — a broad artificial lake left by many years of stone quarrying, its jade-green water crystal clear and set off by sheer cliffs and rock pillars and islets rising from the surface, a fantastical scene likened to a 'miniature Ha Long Bay'. Visitors can rent pedal boats or kayaks to glide around the lake and photograph the picturesque outcrops. Beside the lake stands Buu Long hill with the ancient Buu Phong Pagoda, centuries old and finely carved, where visitors climb stone steps to worship and take in the whole riverscape of Bien Hoa. The spacious grounds also hold a park, play areas, a sculpture garden and shady trees, ideal for families and groups of friends to picnic and camp lightly. With its unusual scenery, fresh air and convenient location, Buu Long is an ideal weekend retreat for the urban dwellers of the south.",
  "presentation_long_ru": "На берегу реки Донгнай в городе Бьенхоа туристическая зона Быулонг — одно из самых любимых мест отдыха на юго-востоке, всего примерно в 30 км от Хошимина. Её самая знаменитая черта — озеро Лонган, широкое искусственное озеро, оставшееся от многолетней добычи камня, с кристально чистой нефритово-зелёной водой, оттенённой отвесными скалами, каменными столбами и островками, поднимающимися над поверхностью, — фантастическая картина, которую сравнивают с «миниатюрной бухтой Халонг». Гости могут взять напрокат катамараны или каяки, чтобы скользить по озеру и фотографировать живописные выступы. У озера возвышается холм Быулонг со старинной пагодой Быуфонг, которой сотни лет и которая тонко украшена резьбой; посетители поднимаются по каменным ступеням, чтобы поклониться и охватить взглядом весь речной пейзаж Бьенхоа. На просторной территории есть также парк, игровые площадки, сад скульптур и тенистые деревья, идеальные для семейных пикников и лёгкого кемпинга. С необычным пейзажем, свежим воздухом и удобным расположением Быулонг — идеальное место отдыха на выходные для горожан юга. Вечером над водой становится прохладно, и семьи с детьми задерживаются у берега до заката, что делает Быулонг приятным местом неспешного отдыха недалеко от города.",
  "highlights_vi": [
    "Hồ Long Ẩn nước xanh ngọc bích, được ví 'vịnh Hạ Long thu nhỏ'",
    "Núi Bửu Long và chùa cổ Bửu Phong hàng trăm năm tuổi",
    "Gần Sài Gòn, thích hợp chèo thuyền, picnic, chụp ảnh cuối tuần"
  ],
  "highlights_en": [
    "Jade-green Long An Lake, likened to a 'miniature Ha Long Bay'",
    "Buu Long hill and the centuries-old Buu Phong Pagoda",
    "Close to Saigon — good for boating, picnics and weekend photos"
  ],
  "highlights_ru": [
    "Нефритово-зелёное озеро Лонган, «миниатюрная бухта Халонг»",
    "Холм Быулонг и старинная пагода Быуфонг, которой сотни лет",
    "Рядом с Сайгоном — лодки, пикники и снимки на выходных"
  ],
  "practical": {
    "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
    "ticket_vi": "Vé vào cổng khoảng 30.000–60.000 VND; thuyền, dịch vụ tính riêng.",
    "duration_vi": "Khoảng nửa ngày.",
    "best_time_vi": "Sáng hoặc chiều mát; cuối tuần đông hơn.",
    "tips_vi": "Mang đồ picnic; thuê thuyền để ngắm hồ đẹp nhất; leo chùa Bửu Phong đi giày thoải mái."
  },
  "tags": ["lake", "park", "family", "temple", "daytrip"],
  "sources": [{"title": "Wikipedia (VI) — Bửu Long", "url": "https://vi.wikipedia.org/wiki/B%E1%BB%ADu_Long"}]
})

# ---------- BẮC NINH (gồm Bắc Giang cũ) ----------
add({
  "region": "vn-bac-ninh", "slug": "den-do",
  "region_name_vi": "Bắc Ninh", "federal_district": "Miền Bắc",
  "name_vi": "Đền Đô (Đền Lý Bát Đế)",
  "name_en": "Do Temple (Temple of the Eight Ly Kings)",
  "name_ru": "Храм До (храм восьми королей Ли)",
  "categories": ["church", "monument"],
  "coordinates": {"lat": 21.1183, "lon": 105.9642},
  "address_vi": "Phường Đình Bảng, thành phố Từ Sơn, tỉnh Bắc Ninh",
  "rating": {"value": 4.6, "count": 4000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Đền cổ thờ tám vị vua nhà Lý, kiến trúc bề thế, hồ bán nguyệt và thủy đình đẹp. Du khách khen không gian trang nghiêm, nhiều giá trị lịch sử; dịp lễ hội đền Đô (rằm tháng 3) rất đông và đặc sắc.",
  "presentation_short_vi": "Đền Đô, còn gọi là đền Lý Bát Đế, ở phường Đình Bảng, tỉnh Bắc Ninh, là nơi thờ tám vị vua triều Lý – vương triều khai mở nền văn minh Đại Việt và dời đô về Thăng Long. Ngôi đền cổ có kiến trúc bề thế với nhà thủy đình trên hồ bán nguyệt, gắn với lễ hội truyền thống lớn của vùng Kinh Bắc.",
  "presentation_short_en": "Do Temple, also called the Temple of the Eight Ly Kings, in Dinh Bang ward, Bac Ninh province, honours the eight monarchs of the Ly dynasty — the house that opened the civilisation of Dai Viet and moved the capital to Thang Long. This ancient, imposing temple, with a water pavilion on a crescent lake, is the focus of a great traditional festival of the Kinh Bac region.",
  "presentation_short_ru": "Храм До, называемый также храмом восьми королей Ли, в квартале Диньбанг провинции Бакнинь, чтит восьмерых государей династии Ли — дома, открывшего цивилизацию Дайвьета и перенёсшего столицу в Тханглонг. Этот древний, внушительный храм с водным павильоном на полумесяцем озере — центр большого традиционного праздника региона Киньбак.",
  "presentation_long_vi": "Tọa lạc tại làng Đình Bảng, quê hương của nhà Lý, nay thuộc thành phố Từ Sơn, tỉnh Bắc Ninh, Đền Đô (tên chữ là Cổ Pháp điện, dân gian quen gọi đền Lý Bát Đế) là nơi thờ phụng tám vị hoàng đế của vương triều Lý – triều đại đã có công dời đô từ Hoa Lư ra Thăng Long năm 1010, mở ra thời kỳ phát triển rực rỡ của quốc gia Đại Việt. Tương truyền đền được khởi dựng từ thời Lý và trải nhiều lần trùng tu, mở rộng qua các thế kỷ. Quần thể kiến trúc rộng lớn được chia thành khu nội thành và ngoại thành, với nhiều công trình như Ngũ Long Môn, chính điện thờ tám vị vua, nhà tiền tế, cùng nhà Thủy đình duyên dáng soi bóng trên hồ bán nguyệt – nơi xưa kia dùng làm sân khấu biểu diễn rối nước và nay là hình ảnh biểu tượng của đền. Trong đền còn lưu giữ tấm bia 'Cổ Pháp điện tạo bi' ghi lại thân thế, sự nghiệp các vua Lý. Hằng năm vào rằm tháng Ba âm lịch, lễ hội đền Đô được tổ chức trọng thể với các nghi lễ rước kiệu, tế lễ và nhiều trò chơi dân gian, thu hút đông đảo nhân dân và du khách. Là biểu tượng cho đạo lý 'uống nước nhớ nguồn' và niềm tự hào về một trong những vương triều huy hoàng nhất lịch sử, Đền Đô là điểm đến giàu giá trị lịch sử – văn hóa của vùng Kinh Bắc.",
  "presentation_long_en": "In Dinh Bang village, homeland of the Ly dynasty and now part of Tu Son city, Bac Ninh province, Do Temple (formally Co Phap Palace, popularly the Temple of the Eight Ly Kings) enshrines the eight emperors of the Ly dynasty — the house that moved the capital from Hoa Lu to Thang Long in 1010, opening a brilliant age for the state of Dai Viet. Tradition says it was first built under the Ly and repeatedly restored and enlarged over the centuries. The vast architectural complex is divided into inner and outer precincts, with structures such as the Five-Dragon Gate, the main hall to the eight kings, the front worship house and a graceful water pavilion mirrored in a crescent lake — once a stage for water-puppet performances and now the temple's emblematic image. The temple also preserves the 'Co Phap Palace' stele recording the lives and deeds of the Ly kings. Each year, on the full moon of the third lunar month, the Do Temple festival is held with solemn palanquin processions, rituals and many folk games, drawing crowds of people and visitors. As a symbol of the ethic of 'remembering the source when drinking the water' and of pride in one of the most glorious dynasties in history, Do Temple is a destination rich in the historical and cultural value of the Kinh Bac region.",
  "presentation_long_ru": "В деревне Диньбанг, на родине династии Ли, ныне в составе города Тышон провинции Бакнинь, храм До (официально дворец Кофап, в народе — храм восьми королей Ли) хранит память о восьми императорах династии Ли — доме, перенёсшем столицу из Хоалы в Тханглонг в 1010 году и открывшем блистательную эпоху государства Дайвьет. По преданию, он был впервые построен при Ли и многократно восстанавливался и расширялся на протяжении веков. Обширный архитектурный комплекс делится на внутреннюю и внешнюю части и включает Врата пяти драконов, главный зал восьми королей, передний молитвенный дом и изящный водный павильон, отражающийся в озере-полумесяце, — некогда сцену для представлений водного театра кукол, а ныне символический образ храма. В храме хранится и стела «дворец Кофап», повествующая о жизни и деяниях королей Ли. Ежегодно в полнолуние третьего лунного месяца проходит праздник храма До с торжественными процессиями паланкинов, обрядами и множеством народных игр, привлекающий толпы людей и гостей. Как символ принципа «пьёшь воду — помни источник» и гордости за одну из славнейших династий истории, храм До — место, богатое исторической и культурной ценностью региона Киньбак.",
  "highlights_vi": [
    "Thờ tám vị vua nhà Lý – vương triều dời đô về Thăng Long năm 1010",
    "Nhà Thủy đình soi bóng hồ bán nguyệt, biểu tượng của đền",
    "Lễ hội đền Đô rằm tháng Ba với rước kiệu, tế lễ, trò chơi dân gian"
  ],
  "highlights_en": [
    "Enshrines the eight Ly kings — the dynasty that moved the capital to Thang Long in 1010",
    "A water pavilion mirrored in a crescent lake, the temple's emblem",
    "The Do Temple festival on the third-month full moon, with processions and folk games"
  ],
  "highlights_ru": [
    "Хранит память о восьми королях Ли — династии, перенёсшей столицу в Тханглонг в 1010",
    "Водный павильон, отражённый в озере-полумесяце, — эмблема храма",
    "Праздник храма До в полнолуние третьего месяца с процессиями и играми"
  ],
  "practical": {
    "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
    "ticket_vi": "Vào cửa thường miễn phí hoặc công đức tùy tâm.",
    "duration_vi": "Khoảng 1–1,5 giờ.",
    "best_time_vi": "Rằm tháng Ba âm lịch (lễ hội); ngày thường yên tĩnh.",
    "tips_vi": "Ăn mặc lịch sự; kết hợp thăm đình Đình Bảng, chùa Dâu, chùa Bút Tháp lân cận."
  },
  "tags": ["temple", "history", "dynasty", "festival", "culture", "top"],
  "sources": [{"title": "Wikipedia (VI) — Đền Đô", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%81n_%C4%90%C3%B4"}]
})

add({
  "region": "vn-bac-ninh", "slug": "chua-but-thap",
  "region_name_vi": "Bắc Ninh", "federal_district": "Miền Bắc",
  "name_vi": "Chùa Bút Tháp",
  "name_en": "But Thap Pagoda",
  "name_ru": "Пагода Буттхап",
  "categories": ["church", "monument"],
  "coordinates": {"lat": 21.0492, "lon": 106.0958},
  "address_vi": "Xã Thuận Thành, tỉnh Bắc Ninh (bên sông Đuống)",
  "rating": {"value": 4.6, "count": 1500, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Ngôi chùa cổ nổi tiếng với tượng Phật Bà Quan Âm nghìn mắt nghìn tay – bảo vật quốc gia. Du khách khen kiến trúc gỗ tinh xảo, tháp đá và không gian tĩnh lặng ven sông Đuống; ít xô bồ, hợp vãn cảnh.",
  "presentation_short_vi": "Chùa Bút Tháp là một trong những ngôi chùa cổ đẹp và nguyên vẹn bậc nhất Bắc Bộ, nằm bên sông Đuống ở tỉnh Bắc Ninh. Chùa nổi tiếng với pho tượng Phật Bà Quan Âm nghìn mắt nghìn tay bằng gỗ – bảo vật quốc gia, cùng tháp đá Báo Nghiêm và nghệ thuật chạm khắc gỗ, đá tinh xảo thời Lê.",
  "presentation_short_en": "But Thap Pagoda is one of the most beautiful and best-preserved ancient pagodas in northern Vietnam, standing by the Duong River in Bac Ninh province. It is famous for its wooden statue of the Thousand-Eyed, Thousand-Armed Avalokitesvara — a national treasure — along with the stone Bao Nghiem tower and exquisite Le-era carving in wood and stone.",
  "presentation_short_ru": "Пагода Буттхап — одна из красивейших и лучше всего сохранившихся древних пагод севера Вьетнама, стоящая у реки Зыонг в провинции Бакнинь. Она знаменита деревянной статуей тысячеглазой и тысячерукой Авалокитешвары — национальным сокровищем, — а также каменной башней Баонгьем и изысканной резьбой по дереву и камню эпохи Ле.",
  "presentation_long_vi": "Nằm bên bờ nam sông Đuống, thuộc xã Thuận Thành, tỉnh Bắc Ninh, chùa Bút Tháp (tên chữ là Ninh Phúc tự) là một danh lam cổ tự nổi tiếng và được coi là ngôi chùa còn giữ được nhiều giá trị nghệ thuật nguyên vẹn nhất của vùng đồng bằng Bắc Bộ. Chùa có lịch sử lâu đời, được trùng tu và mở rộng quy mô lớn vào thế kỷ 17 dưới thời Lê trung hưng với sự bảo trợ của hoàng thất, tạo nên một quần thể kiến trúc hài hòa gồm nhiều tòa nối tiếp nhau theo trục dọc, ẩn mình dưới bóng cây, cạnh dòng sông êm đềm. Báu vật nổi tiếng nhất của chùa là pho tượng Phật Bà Quan Âm nghìn mắt nghìn tay bằng gỗ sơn son thếp vàng, cao gần 3,7 m, do nghệ nhân Trương Thọ Nam tạc năm 1656 – một kiệt tác điêu khắc Phật giáo Việt Nam đã được công nhận là Bảo vật quốc gia. Ngoài ra, chùa còn có tòa tháp đá Báo Nghiêm nhiều tầng như một cây bút khổng lồ vươn lên trời (chính là nguồn gốc tên gọi 'Bút Tháp'), cầu đá, tòa Cửu phẩm liên hoa bằng gỗ có thể xoay, cùng vô số mảng chạm khắc gỗ, đá tinh xảo mô tả hoa lá, chim muông, cảnh vật. Yên tĩnh, cổ kính và giàu giá trị mỹ thuật, chùa Bút Tháp là điểm đến hấp dẫn cho du khách yêu di sản và những ai muốn tìm chốn thanh tịnh.",
  "presentation_long_en": "On the south bank of the Duong River in Thuan Thanh, Bac Ninh province, But Thap Pagoda (formally Ninh Phuc Temple) is a celebrated ancient monastery, regarded as the pagoda that best preserves its artistic values in the northern delta. Of long standing, it was greatly restored and enlarged in the 17th century under the restored Le, with royal patronage, forming a harmonious complex of halls arranged one behind another along a central axis, sheltered by trees beside the tranquil river. Its most famous treasure is the wooden statue of the Thousand-Eyed, Thousand-Armed Avalokitesvara, gilded and lacquered, nearly 3.7 m tall, carved by the artisan Truong Tho Nam in 1656 — a masterpiece of Vietnamese Buddhist sculpture recognised as a national treasure. The pagoda also has the multi-storey stone Bao Nghiem tower, rising like a giant writing brush toward the sky (the origin of the name 'But Thap', 'brush tower'), a stone bridge, a revolving wooden 'nine-tier lotus' pavilion and countless fine carvings in wood and stone depicting flowers, birds and landscapes. Quiet, ancient and rich in artistic value, But Thap Pagoda is an appealing destination for lovers of heritage and for anyone seeking a place of calm.",
  "presentation_long_ru": "На южном берегу реки Зыонг в общине Тхуантхань провинции Бакнинь пагода Буттхап (официально храм Ниньфук) — прославленный древний монастырь, считающийся пагодой, которая лучше всего сохранила свои художественные ценности в северной дельте. Имея давнюю историю, она была значительно перестроена и расширена в XVII веке при восстановленной династии Ле под покровительством двора, образовав гармоничный комплекс залов, расположенных один за другим вдоль центральной оси, под сенью деревьев у тихой реки. Её самое знаменитое сокровище — деревянная статуя тысячеглазой и тысячерукой Авалокитешвары, покрытая позолотой и лаком, высотой почти 3,7 м, вырезанная мастером Чыонг Тхо Намом в 1656 году, — шедевр вьетнамской буддийской скульптуры, признанный национальным сокровищем. В пагоде есть также многоярусная каменная башня Баонгьем, поднимающаяся к небу, словно гигантская кисть (отсюда название «Буттхап» — «башня-кисть»), каменный мост, вращающийся деревянный павильон «девятиярусный лотос» и бесчисленные тонкие резные изображения цветов, птиц и пейзажей по дереву и камню. Тихая, древняя и богатая художественной ценностью, пагода Буттхап — привлекательное место для любителей наследия и всех, кто ищет покоя.",
  "highlights_vi": [
    "Tượng Phật Bà Quan Âm nghìn mắt nghìn tay bằng gỗ (1656) – Bảo vật quốc gia",
    "Tháp đá Báo Nghiêm vươn cao như cây bút – nguồn gốc tên 'Bút Tháp'",
    "Kiến trúc và chạm khắc gỗ, đá tinh xảo thời Lê, còn nguyên vẹn"
  ],
  "highlights_en": [
    "Wooden Thousand-Armed Avalokitesvara (1656) — a national treasure",
    "The stone Bao Nghiem tower rising like a brush — origin of the name 'But Thap'",
    "Well-preserved Le-era architecture and fine wood-and-stone carving"
  ],
  "highlights_ru": [
    "Деревянная тысячерукая Авалокитешвара (1656) — национальное сокровище",
    "Каменная башня Баонгьем, поднимающаяся, как кисть, — источник названия «Буттхап»",
    "Хорошо сохранившаяся архитектура эпохи Ле и тонкая резьба по дереву и камню"
  ],
  "practical": {
    "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
    "ticket_vi": "Vào cửa miễn phí; công đức tùy tâm.",
    "duration_vi": "Khoảng 1 giờ.",
    "best_time_vi": "Quanh năm; đầu xuân có lễ chùa.",
    "tips_vi": "Xin phép trước khi chụp tượng thờ; ăn mặc lịch sự; kết hợp thăm chùa Dâu gần đó."
  },
  "tags": ["pagoda", "heritage", "national-treasure", "architecture", "culture"],
  "sources": [{"title": "Wikipedia (VI) — Chùa Bút Tháp", "url": "https://vi.wikipedia.org/wiki/Ch%C3%B9a_B%C3%BAt_Th%C3%A1p"}]
})

add({
  "region": "vn-bac-ninh", "slug": "chua-vinh-nghiem",
  "region_name_vi": "Bắc Ninh", "federal_district": "Miền Bắc",
  "name_vi": "Chùa Vĩnh Nghiêm (Đức La)",
  "name_en": "Vinh Nghiem Pagoda (Duc La)",
  "name_ru": "Пагода Виньнгьем (Дыкла)",
  "categories": ["church", "monument"],
  "coordinates": {"lat": 21.2342, "lon": 106.3533},
  "address_vi": "Phường Tân An (huyện Yên Dũng cũ, Bắc Giang), tỉnh Bắc Ninh",
  "rating": {"value": 4.6, "count": 1200, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Chốn tổ của Thiền phái Trúc Lâm, lưu giữ kho mộc bản được UNESCO ghi danh Ký ức thế giới. Du khách khen không gian cổ kính, bề thế, nhiều cổ vật; nên nghe giới thiệu về mộc bản để hiểu giá trị.",
  "presentation_short_vi": "Chùa Vĩnh Nghiêm (chùa Đức La) ở tỉnh Bắc Ninh (địa phận Bắc Giang cũ) là 'đại danh lam cổ tự', được coi là chốn tổ của Thiền phái Trúc Lâm Yên Tử. Chùa nổi tiếng với kho mộc bản kinh Phật quý giá đã được UNESCO ghi danh là Di sản tư liệu thuộc Chương trình Ký ức thế giới khu vực châu Á – Thái Bình Dương.",
  "presentation_short_en": "Vinh Nghiem Pagoda (Duc La) in Bac Ninh province (formerly Bac Giang) is a 'great ancient monastery', regarded as a founding seat of the Truc Lam Yen Tu Zen school. It is famous for its precious store of Buddhist woodblocks, inscribed by UNESCO in the Memory of the World register for Asia and the Pacific.",
  "presentation_short_ru": "Пагода Виньнгьем (Дыкла) в провинции Бакнинь (прежде Бакзянг) — «великий древний монастырь», считающийся одной из колыбелей дзен-школы Чуклам Йенты. Она знаменита ценным собранием буддийских печатных досок, внесённым ЮНЕСКО в реестр «Память мира» для Азиатско-Тихоокеанского региона.",
  "presentation_long_vi": "Tọa lạc nơi hợp lưu sông Thương và sông Lục Nam, thuộc tỉnh Bắc Ninh ngày nay (trước đây là huyện Yên Dũng, tỉnh Bắc Giang), chùa Vĩnh Nghiêm – tên Nôm là chùa Đức La – từ lâu được tôn xưng là 'đại danh lam cổ tự', một trong những trung tâm Phật giáo quan trọng bậc nhất của Việt Nam. Chùa gắn liền với sự ra đời và phát triển của Thiền phái Trúc Lâm do Phật hoàng Trần Nhân Tông sáng lập vào thế kỷ 13; tại đây, ba vị tổ Trúc Lâm là Trần Nhân Tông, Pháp Loa và Huyền Quang đã tu hành, thuyết pháp, đào tạo tăng đồ, nên chùa được xem như 'chốn tổ' của dòng thiền thuần Việt này. Quần thể chùa bề thế gồm nhiều tòa như tam quan, tòa Thiên đường, nhà tổ, gác chuông, nằm giữa khuôn viên cây cối cổ thụ rợp bóng. Báu vật vô giá của chùa là kho mộc bản gồm hàng nghìn tấm ván khắc kinh, sách thuốc, luật giới nhà Phật bằng chữ Hán và Nôm, được chế tác qua nhiều thế kỷ. Năm 2012, kho mộc bản chùa Vĩnh Nghiêm đã được UNESCO công nhận là Di sản tư liệu ký ức thế giới khu vực châu Á – Thái Bình Dương, khẳng định giá trị đặc biệt về tư tưởng, văn hóa và nghệ thuật khắc in. Với bề dày lịch sử, vị thế trong Phật giáo và di sản mộc bản độc đáo, chùa Vĩnh Nghiêm là điểm đến ý nghĩa cho hành hương và tìm hiểu văn hóa.",
  "presentation_long_en": "At the confluence of the Thuong and Luc Nam rivers, in present-day Bac Ninh province (formerly Yen Dung district, Bac Giang), Vinh Nghiem Pagoda — in the vernacular Duc La Pagoda — has long been honoured as a 'great ancient monastery', one of the foremost centres of Buddhism in Vietnam. It is bound to the birth and growth of the Truc Lam Zen school founded by the Buddha-King Tran Nhan Tong in the 13th century; here the three Truc Lam patriarchs — Tran Nhan Tong, Phap Loa and Huyen Quang — practised, preached and trained monks, so the pagoda is regarded as a 'founding seat' of this purely Vietnamese Zen tradition. The imposing complex comprises many halls — the triple gate, the main hall, the patriarchs' house and the bell tower — set among ancient shade trees. Its priceless treasure is a store of thousands of woodblocks carving sutras, medical texts and monastic precepts in Han and Nom scripts, made over many centuries. In 2012 the Vinh Nghiem woodblocks were recognised by UNESCO in the Memory of the World register for Asia and the Pacific, affirming their exceptional value in thought, culture and the art of block printing. With its deep history, standing in Buddhism and unique woodblock heritage, Vinh Nghiem Pagoda is a meaningful destination for pilgrimage and cultural discovery.",
  "presentation_long_ru": "У слияния рек Тхыонг и Люкнам, в нынешней провинции Бакнинь (прежде уезд Йензунг провинции Бакзянг), пагода Виньнгьем — на народном языке пагода Дыкла — издавна почитается как «великий древний монастырь», один из первейших центров буддизма во Вьетнаме. Она связана с рождением и развитием дзен-школы Чуклам, основанной королём-буддой Чан Нян Тонгом в XIII веке; здесь три патриарха Чуклам — Чан Нян Тонг, Фап Лоа и Хюен Куанг — подвизались, проповедовали и обучали монахов, поэтому пагоду считают «колыбелью» этой чисто вьетнамской дзен-традиции. Внушительный комплекс включает множество залов — тройные врата, главный зал, дом патриархов и колокольню — среди старых тенистых деревьев. Его бесценное сокровище — собрание из тысяч печатных досок с сутрами, медицинскими текстами и монашескими предписаниями на письме хан и ном, создававшихся на протяжении веков. В 2012 году доски Виньнгьема были признаны ЮНЕСКО в реестре «Память мира» для Азиатско-Тихоокеанского региона, что подтвердило их исключительную ценность в мысли, культуре и искусстве ксилографии. С глубокой историей, положением в буддизме и уникальным наследием печатных досок пагода Виньнгьем — значимое место для паломничества и знакомства с культурой.",
  "highlights_vi": [
    "Chốn tổ của Thiền phái Trúc Lâm Yên Tử, 'đại danh lam cổ tự'",
    "Kho mộc bản kinh Phật được UNESCO ghi danh Ký ức thế giới (2012)",
    "Quần thể chùa cổ bề thế nơi hợp lưu sông Thương – Lục Nam"
  ],
  "highlights_en": [
    "A founding seat of the Truc Lam Yen Tu Zen school, a 'great ancient monastery'",
    "Buddhist woodblocks inscribed by UNESCO in the Memory of the World (2012)",
    "An imposing old temple complex at the Thuong–Luc Nam river confluence"
  ],
  "highlights_ru": [
    "Колыбель дзен-школы Чуклам Йенты, «великий древний монастырь»",
    "Буддийские печатные доски в реестре ЮНЕСКО «Память мира» (2012)",
    "Внушительный старинный комплекс у слияния рек Тхыонг и Люкнам"
  ],
  "practical": {
    "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
    "ticket_vi": "Vào cửa miễn phí; công đức tùy tâm.",
    "duration_vi": "Khoảng 1–1,5 giờ.",
    "best_time_vi": "Đầu xuân (lễ hội chùa) hoặc ngày thường yên tĩnh.",
    "tips_vi": "Hỏi nhà chùa để tìm hiểu về mộc bản; ăn mặc lịch sự; kết hợp tuyến Tây Yên Tử."
  },
  "tags": ["pagoda", "zen", "heritage", "unesco", "history", "top"],
  "sources": [{"title": "Wikipedia (VI) — Chùa Vĩnh Nghiêm (Bắc Giang)", "url": "https://vi.wikipedia.org/wiki/Ch%C3%B9a_V%C4%A9nh_Nghi%C3%AAm_(B%E1%BA%AFc_Giang)"}]
})

# @@MARKER@@

# ============================ WRITE ============================
def main():
    by_file = {}
    for d in NEW:
        by_file.setdefault(d["region"], []).append(finalize(d))
    grand = 0
    for region, recs in sorted(by_file.items()):
        path = os.path.join(REG, region + ".json")
        cur = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
        if not isinstance(cur, list):
            cur = []
        have = {p.get("slug") for p in cur}
        added = [r for r in recs if r["slug"] not in have]
        cur += added
        json.dump(cur, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"{region}: +{len(added)} (skip {len(recs)-len(added)}) -> tong {len(cur)}")
        grand += len(added)
    print("TONG THEM:", grand)


if __name__ == "__main__":
    main()
