# -*- coding: utf-8 -*-
"""Bổ sung địa điểm du lịch nổi tiếng còn thiếu cho tỉnh ĐẮK LẮK (mới, sau sáp nhập 1/7/2025).
Đắk Lắk mới = Đắk Lắk (cũ) + Phú Yên (cũ). region_name_vi = "Đắk Lắk"; federal_district = "Miền Trung".
Chèn an toàn: nạp -> append (bỏ qua slug đã có) -> ghi lại. Map links do retrofit_map_links.py sinh.
"""
import json, os, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
F = os.path.join(ROOT, "data", "regions", "vn-dak-lak.json")

REG = "vn-dak-lak"
REG_NAME = "Đắk Lắk"
TODAY = "2026-07-29"


def src(name_en, name_vi):
    return [
        {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Special:Search?search=" + urllib.parse.quote(name_en)},
        {"title": "Wikipedia (VI)", "url": "https://vi.wikipedia.org/wiki/Special:Search?search=" + urllib.parse.quote(name_vi)},
    ]


def mk(slug, name_vi, name_en, name_ru, lat, lon, cats, address, tags, rec):
    return {
        "id": f"{REG}-{slug}",
        "slug": slug,
        "region": REG,
        "country": "vietnam",
        "region_name_vi": REG_NAME,
        "federal_district": "Miền Trung",
        "name_vi": name_vi,
        "name_ru": name_ru,
        "name_en": name_en,
        "categories": cats,
        "coordinates": {"lat": lat, "lon": lon},
        "address_vi": address,
        "rating": rec.get("rating"),
        "review_summary_vi": rec.get("review_summary_vi", ""),
        "presentation_short_vi": rec["ps_vi"],
        "presentation_short_en": rec["ps_en"],
        "presentation_short_ru": rec["ps_ru"],
        "presentation_long_vi": rec["pl_vi"],
        "presentation_long_en": rec["pl_en"],
        "presentation_long_ru": rec["pl_ru"],
        "highlights_vi": rec["h_vi"],
        "highlights_en": rec["h_en"],
        "highlights_ru": rec["h_ru"],
        "practical": rec.get("practical", {}),
        "photo": None,
        "photo_credit": None,
        "official_site": rec.get("official_site"),
        "sources": src(name_en, name_vi),
        "tags": tags,
        "status": "enriched",
        "last_updated": TODAY,
    }


NEW = []

NEW.append(mk(
    "hon-yen", "Hòn Yến",
    "Hon Yen Islet", "Островок Хонъен",
    13.2545, 109.2925, ["park_garden", "other"],
    "Thôn Nhơn Hội, xã An Hòa Hải (huyện Tuy An cũ), tỉnh Đắk Lắk",
    ["top", "sea", "island", "viewpoint", "nature", "outdoor"],
    {
        "rating": {"value": 4.5, "count": 3200, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách say mê hòn đảo đá đen giữa biển xanh và rạn san hô lộ thiên khi thủy triều rút. Nhiều người khen cảnh hoang sơ, bình minh và hoàng hôn rất đẹp; một số lưu ý nên xem lịch con nước, đi giày rọ và giữ gìn san hô mong manh.",
        "ps_vi": "Hòn Yến là hòn đảo đá nhỏ nhô lên giữa biển ở thôn Nhơn Hội, cách thành phố Tuy Hòa khoảng 20 km về phía bắc. Nổi tiếng với rạn san hô lộ thiên độc đáo khi thủy triều xuống thấp, nơi đây là một trong những thắng cảnh biển hoang sơ đẹp nhất của vùng đất Phú Yên xưa.",
        "ps_en": "Hon Yen is a small rocky islet rising from the sea at Nhon Hoi hamlet, about 20 km north of Tuy Hoa city. Famous for the rare coral reef that surfaces at low tide, it is one of the most pristine coastal landscapes of the former Phu Yen area.",
        "ps_ru": "Хонъен — небольшой скалистый островок, поднимающийся из моря у деревни Нёнхой, примерно в 20 км к северу от города Туихоа. Он знаменит редким коралловым рифом, который обнажается во время отлива, и считается одним из самых нетронутых прибрежных пейзажей бывшей провинции Фуйен.",
        "pl_vi": "Hòn Yến là cụm đảo đá nhỏ nằm sát bờ ở thôn Nhơn Hội, xã An Hòa Hải, cách trung tâm thành phố Tuy Hòa khoảng 20 km về phía bắc. Ngọn núi đá màu đen sẫm cao chừng 70 m nhô lên giữa làn nước biếc, xưa kia là nơi chim yến về làm tổ nên có tên gọi Hòn Yến. Điều làm nên sức hút đặc biệt của nơi này là rạn san hô ven bờ: vào những ngày thủy triều xuống thấp nhất trong năm, thường rơi vào khoảng tháng 5 đến tháng 7 âm lịch, mặt nước rút đi để lộ ra cả một 'vườn' san hô nhiều màu ngay trên mặt biển, một cảnh tượng hiếm thấy ở Việt Nam. Du khách có thể lội ra ngắm san hô, chụp ảnh với những khối đá phủ rêu và hàu bám dày. Bình minh và hoàng hôn ở Hòn Yến đều rất đẹp, khi ánh sáng đổ xuống mặt nước và những chiếc thuyền thúng của ngư dân. Danh thắng Hòn Yến đã được xếp hạng Di tích quốc gia. Vì san hô rất mong manh, du khách được khuyến khích chỉ ngắm nhìn, không giẫm đạp hay bẻ san hô. Từ ngày 1 tháng 7 năm 2025, khu vực này thuộc tỉnh Đắk Lắk (trước đây thuộc tỉnh Phú Yên).",
        "pl_en": "Hon Yen is a cluster of small rocky islets close to the shore at Nhon Hoi hamlet, An Hoa Hai commune, about 20 km north of Tuy Hoa city. The dark, roughly 70-metre-high crag rising from turquoise water was once a nesting place for swiftlets, which gave it its name ('Swiftlet Islet'). Its special draw is the fringing coral reef: on the days of the year's lowest tides, usually around the fifth to seventh lunar months, the water pulls back to reveal a whole 'garden' of multicoloured coral at the surface, a sight rarely seen in Vietnam. Visitors can wade out to admire the coral and photograph the moss- and oyster-covered boulders. Both sunrise and sunset here are beautiful, when light spills over the water and the fishermen's round basket boats. Hon Yen has been ranked a National Scenic Relic. Because the coral is fragile, visitors are urged only to look and not to step on or break it. Since 1 July 2025 the area has belonged to Dak Lak Province (formerly Phu Yen Province).",
        "pl_ru": "Хонъен — группа небольших скалистых островков у берега возле деревни Нёнхой, община Анхоахай, примерно в 20 км к северу от города Туихоа. Тёмная скала высотой около 70 метров, поднимающаяся из бирюзовой воды, когда-то была местом гнездования саланган (стрижей-ласточек), что и дало название острову. Его главная особенность — окаймляющий коралловый риф: в дни самых низких отливов года, обычно в пятый–седьмой лунные месяцы, вода отступает и обнажает целый «сад» разноцветных кораллов у самой поверхности — зрелище, редкое для Вьетнама. Гости могут пройти по мелководью, чтобы рассмотреть кораллы и сфотографировать валуны, покрытые мхом и устрицами. Здесь красивы и рассвет, и закат, когда свет разливается по воде и по круглым лодкам-корзинам рыбаков. Хонъен внесён в список национальных живописных памятников. Поскольку кораллы хрупкие, посетителей просят только смотреть, не наступать на них и не ломать. С 1 июля 2025 года эта местность относится к провинции Даклак (ранее — провинция Фуйен).",
        "h_vi": ["Rạn san hô lộ thiên hiếm thấy khi thủy triều xuống thấp (tháng 5–7 âm lịch)", "Núi đá đen cao ~70 m nhô giữa biển, từng là nơi chim yến làm tổ", "Đã được xếp hạng Di tích – danh thắng quốc gia"],
        "h_en": ["Rare coral reef exposed at the lowest tides (5th–7th lunar months)", "A ~70 m dark crag in the sea, once a swiftlet nesting site", "Ranked a National Scenic Relic"],
        "h_ru": ["Редкий коралловый риф, обнажающийся при самых низких отливах (5–7 лунные месяцы)", "Тёмная скала ~70 м в море, бывшее место гнездования саланган", "Внесён в список национальных живописных памятников"],
        "practical": {
            "hours_vi": "Bãi biển tự nhiên, mở cả ngày; ngắm san hô phụ thuộc lịch thủy triều.",
            "ticket_vi": "Tham quan tự do (miễn phí); có thể thuê thuyền thúng của ngư dân.",
            "duration_vi": "Khoảng 2–3 giờ.",
            "best_time_vi": "Những ngày thủy triều thấp nhất (tháng 5–7 âm lịch); sáng sớm hoặc chiều muộn.",
            "tips_vi": "Xem lịch con nước trước khi đi; mang giày rọ chống trơn; không giẫm đạp hay bẻ san hô; mang mũ, nước và kem chống nắng.",
        },
    },
))

NEW.append(mk(
    "cau-go-ong-cop", "Cầu gỗ Ông Cọp",
    "Ong Cop Wooden Bridge", "Деревянный мост Онгкоп",
    13.4525, 109.2790, ["bridge", "other"],
    "Nối xã An Ninh Tây (huyện Tuy An cũ) với phường Xuân Đài (thị xã Sông Cầu cũ), tỉnh Đắk Lắk",
    ["bridge", "viewpoint", "photo", "rural", "outdoor"],
    {
        "rating": {"value": 4.3, "count": 2600, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích cây cầu gỗ mộc mạc vắt qua cửa sông, khung cảnh làng quê yên bình và ảnh check-in đẹp. Nhiều người thấy đi bộ trên cầu thú vị nhưng hơi rung; một số nhắc cầu hẹp, nên đi cẩn thận và tránh giờ đông xe máy.",
        "ps_vi": "Cầu gỗ Ông Cọp là cây cầu bằng gỗ ván dài nhất Việt Nam, bắc qua cửa sông Bình Bá gần cảng Tiên Châu, cách thành phố Tuy Hòa khoảng 35 km về phía bắc. Với những nhịp gỗ mộc mạc trải dài giữa khung cảnh làng quê và rừng dừa, đây là điểm dạo bộ và chụp ảnh được nhiều du khách yêu thích.",
        "ps_en": "Ong Cop Wooden Bridge is the longest plank wooden bridge in Vietnam, crossing the mouth of the Binh Ba River near Tien Chau port, about 35 km north of Tuy Hoa city. With its rustic timber spans stretched across a countryside of coconut groves, it is a favourite spot for strolling and photography.",
        "ps_ru": "Деревянный мост Онгкоп — самый длинный дощатый мост во Вьетнаме, перекинутый через устье реки Биньба у порта Тьентяу, примерно в 35 км к северу от города Туихоа. Своими простыми деревянными пролётами среди сельских пейзажей и кокосовых рощ он привлекает любителей прогулок и фотографий.",
        "pl_vi": "Cầu gỗ Ông Cọp, còn gọi là cầu Bình Thạnh hay cầu Miếu Ông Cọp, được xem là cây cầu gỗ dài nhất Việt Nam với chiều dài khoảng 700–800 m. Cầu bắc qua cửa sông Bình Bá (đổ ra cảng Tiên Châu), nối các thôn phía bắc xã An Ninh Tây với phường Xuân Đài, rút ngắn đáng kể quãng đường cho người dân giữa hai bờ. Toàn bộ mặt cầu được ghép từ ván gỗ và thân cây phi lao, tre, đặt trên hàng cọc gỗ cắm xuống lòng sông; mỗi mùa mưa lũ, cầu thường phải gia cố hoặc dựng lại nên mang dáng vẻ mộc mạc, tạm bợ rất đặc trưng. Đi bộ hay chạy xe máy chậm trên cầu, du khách có thể phóng tầm mắt ngắm dòng nước lấp lánh, những rặng dừa, ruộng đồng và làng chài hai bên bờ, đặc biệt đẹp vào lúc bình minh và hoàng hôn. Cây cầu đã trở thành biểu tượng bình dị của vùng 'hoa vàng cỏ xanh' và là background quen thuộc trong nhiều bộ ảnh du lịch. Từ ngày 1 tháng 7 năm 2025, khu vực này thuộc tỉnh Đắk Lắk (trước đây thuộc tỉnh Phú Yên).",
        "pl_en": "Ong Cop Wooden Bridge, also called Binh Thanh Bridge or Mieu Ong Cop Bridge, is regarded as the longest wooden bridge in Vietnam at roughly 700–800 m. It spans the mouth of the Binh Ba River (which flows out at Tien Chau port), linking the northern hamlets of An Ninh Tay with Xuan Dai and greatly shortening the journey between the two banks. The whole deck is assembled from planks and casuarina and bamboo poles laid over rows of wooden piles driven into the riverbed; because each rainy season tends to damage it, the bridge is repeatedly reinforced or rebuilt, giving it its characteristically rustic, makeshift look. Walking or riding slowly across, visitors take in the glittering water, coconut palms, paddy fields and fishing hamlets on either side, especially lovely at sunrise and sunset. The bridge has become a humble symbol of the 'yellow flowers on green grass' region and a familiar backdrop in countless travel photos. Since 1 July 2025 the area has belonged to Dak Lak Province (formerly Phu Yen Province).",
        "pl_ru": "Деревянный мост Онгкоп, также известный как мост Биньтхань или мост Мьеу-Онгкоп, считается самым длинным деревянным мостом во Вьетнаме — около 700–800 м. Он перекинут через устье реки Биньба (впадающей у порта Тьентяу) и соединяет северные деревни общины Аниньтай с Суандай, значительно сокращая путь между берегами. Всё полотно собрано из досок, стволов казуарины и бамбука, уложенных на ряды деревянных свай, вбитых в дно реки; поскольку каждый сезон дождей повреждает его, мост постоянно укрепляют или отстраивают заново, отчего он выглядит нарочито простым и временным. Проходя или медленно проезжая по мосту, гости любуются блестящей водой, кокосовыми пальмами, рисовыми полями и рыбацкими деревнями по обеим сторонам — особенно красиво на рассвете и закате. Мост стал скромным символом края «жёлтых цветов на зелёной траве» и привычным фоном для множества туристических фотографий. С 1 июля 2025 года эта местность относится к провинции Даклак (ранее — провинция Фуйен).",
        "h_vi": ["Cây cầu gỗ ván dài nhất Việt Nam (khoảng 700–800 m)", "Khung cảnh làng quê, rừng dừa và cửa sông thơ mộng", "Điểm check-in gắn với vùng đất 'hoa vàng cỏ xanh'"],
        "h_en": ["Vietnam's longest plank wooden bridge (about 700–800 m)", "Poetic scenery of countryside, coconut groves and river mouth", "A photo spot tied to the 'yellow flowers on green grass' land"],
        "h_ru": ["Самый длинный дощатый деревянный мост Вьетнама (около 700–800 м)", "Поэтичные виды деревни, кокосовых рощ и устья реки", "Место для фото, связанное с краем «жёлтых цветов на зелёной траве»"],
        "practical": {
            "hours_vi": "Qua cầu cả ngày; đẹp nhất lúc bình minh và hoàng hôn.",
            "ticket_vi": "Thu phí qua cầu rất thấp (vài nghìn đồng cho người đi bộ/xe máy).",
            "duration_vi": "Khoảng 30–45 phút.",
            "best_time_vi": "Sáng sớm hoặc chiều muộn; mùa khô tháng 1–8.",
            "tips_vi": "Đi cẩn thận vì cầu hẹp và hơi rung; nhường đường cho xe máy; kết hợp ghé đầm Ô Loan, Gành Đá Đĩa gần đó.",
        },
    },
))

NEW.append(mk(
    "dia-dao-go-thi-thung", "Địa đạo Gò Thì Thùng",
    "Go Thi Thung Tunnels", "Тоннели Готхитхунг",
    13.3520, 109.1520, ["fortress", "monument"],
    "Thôn Xuân Thành, xã An Xuân (huyện Tuy An cũ), cao nguyên Vân Hòa, tỉnh Đắk Lắk",
    ["history", "war", "unesco", "outdoor", "monument"],
    {
        "rating": {"value": 4.4, "count": 900, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách đánh giá cao giá trị lịch sử của hệ thống địa đạo trên cao nguyên Vân Hòa và không khí mát mẻ quanh năm. Nhiều người thấy đường hầm hẹp nhưng đáng trải nghiệm; một số nhắc nên có hướng dẫn và mang đèn để hiểu rõ cấu trúc.",
        "ps_vi": "Địa đạo Gò Thì Thùng là hệ thống đường hầm chiến tranh đào trên cao nguyên Vân Hòa, xã An Xuân, ở độ cao khoảng 400 m so với mực nước biển. Được xếp cùng địa đạo Củ Chi và Vịnh Mốc như ba địa đạo lớn nhất Việt Nam, đây là di tích lịch sử quốc gia gắn với kháng chiến chống Mỹ.",
        "ps_en": "Go Thi Thung Tunnels are a network of wartime tunnels dug on the Van Hoa plateau in An Xuan commune, at about 400 m above sea level. Counted alongside the Cu Chi and Vinh Moc tunnels as one of Vietnam's three great tunnel systems, it is a National Historical Relic of the resistance war against the United States.",
        "ps_ru": "Тоннели Готхитхунг — сеть военных подземных ходов, вырытых на плато Ванхоа в общине Ансуан, на высоте около 400 м над уровнем моря. Наряду с тоннелями Кути и Виньмок это одна из трёх крупнейших тоннельных систем Вьетнама и национальный исторический памятник времён войны сопротивления против США.",
        "pl_vi": "Địa đạo Gò Thì Thùng nằm ở thôn Xuân Thành, xã An Xuân, trên đỉnh cao nguyên Vân Hòa mát mẻ, cách trung tâm thành phố Tuy Hòa khoảng 45 km về phía bắc. Được quân và dân địa phương đào trong những năm 1964–1965 giữa cuộc kháng chiến chống Mỹ, hệ thống địa đạo có tổng chiều dài gần 2.000 m, rộng khoảng 0,8 m và sâu tới 4–5 m, với hàng trăm giếng và ngách thông hơi nối liền các hầm trú ẩn, hầm cứu thương và công sự chiến đấu. Từ lòng đất, du khách hình dung được cách người dân bám trụ, ẩn nấp và chiến đấu ngay dưới chân đối phương. Cùng với địa đạo Củ Chi (Thành phố Hồ Chí Minh) và địa đạo Vịnh Mốc (Quảng Trị), Gò Thì Thùng được xem là một trong ba địa đạo tiêu biểu nhất cả nước và đã được công nhận là Di tích lịch sử cấp quốc gia năm 2008. Khu vực xung quanh phủ cây xanh, khí hậu quanh năm dịu mát; vào dịp lễ hội, nơi đây còn tổ chức hội đua ngựa Gò Thì Thùng độc đáo của vùng cao nguyên. Từ ngày 1 tháng 7 năm 2025, khu vực này thuộc tỉnh Đắk Lắk (trước đây thuộc tỉnh Phú Yên).",
        "pl_en": "Go Thi Thung Tunnels lie in Xuan Thanh hamlet, An Xuan commune, on the cool summit of the Van Hoa plateau, about 45 km north of Tuy Hoa city. Dug by local troops and residents in 1964–1965 during the resistance war against the United States, the system runs nearly 2,000 m in total, about 0.8 m wide and up to 4–5 m deep, with hundreds of wells and ventilation shafts linking shelters, field hospitals and fighting positions. From underground, visitors sense how people held on, hid and fought right beneath the enemy's feet. Together with the Cu Chi Tunnels (Ho Chi Minh City) and the Vinh Moc Tunnels (Quang Tri), Go Thi Thung is regarded as one of the country's three most notable tunnel systems and was recognised as a National Historical Relic in 2008. The surrounding area is green and cool year-round; during festivals it hosts the distinctive Go Thi Thung horse race of the highlands. Since 1 July 2025 the area has belonged to Dak Lak Province (formerly Phu Yen Province).",
        "pl_ru": "Тоннели Готхитхунг находятся в деревне Суантхань, община Ансуан, на прохладной вершине плато Ванхоа, примерно в 45 км к северу от города Туихоа. Вырытые местными бойцами и жителями в 1964–1965 годах во время войны сопротивления против США, они имеют общую длину почти 2000 м, ширину около 0,8 м и глубину до 4–5 м, с сотнями колодцев и вентиляционных шахт, соединяющих укрытия, полевые госпитали и боевые позиции. Под землёй посетители чувствуют, как люди держались, прятались и сражались прямо под ногами противника. Вместе с тоннелями Кути (Хошимин) и Виньмок (Куангчи) Готхитхунг считается одной из трёх самых значимых тоннельных систем страны и в 2008 году признан национальным историческим памятником. Окрестности круглый год зелёные и прохладные; во время праздников здесь проводят самобытные конные скачки Готхитхунг, характерные для нагорья. С 1 июля 2025 года эта местность относится к провинции Даклак (ранее — провинция Фуйен).",
        "h_vi": ["Một trong ba địa đạo lớn nhất Việt Nam (cùng Củ Chi và Vịnh Mốc)", "Tổng chiều dài gần 2.000 m trên cao nguyên Vân Hòa cao 400 m", "Di tích lịch sử quốc gia (2008); có hội đua ngựa truyền thống"],
        "h_en": ["One of Vietnam's three largest tunnel systems (with Cu Chi and Vinh Moc)", "Nearly 2,000 m long on the 400 m-high Van Hoa plateau", "National Historical Relic (2008); hosts a traditional horse race"],
        "h_ru": ["Одна из трёх крупнейших тоннельных систем Вьетнама (с Кути и Виньмок)", "Общая длина почти 2000 м на плато Ванхоа высотой 400 м", "Национальный памятник (2008); проводятся традиционные конные скачки"],
        "practical": {
            "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
            "ticket_vi": "Phí tham quan thấp; nên hỏi tại chỗ.",
            "duration_vi": "Khoảng 1–2 giờ.",
            "best_time_vi": "Quanh năm mát mẻ; dịp hội đua ngựa (mùng 9 Tết) rất đông vui.",
            "tips_vi": "Nên có hướng dẫn viên để hiểu cấu trúc; mang đèn pin; mặc đồ gọn vì hầm hẹp; đi giày thoải mái.",
        },
    },
))

NEW.append(mk(
    "chua-da-trang", "Chùa Đá Trắng (Chùa Từ Quang)",
    "Da Trang Pagoda (Tu Quang Pagoda)", "Пагода Дачанг (пагода Тыкуанг)",
    13.3380, 109.2680, ["church", "other"],
    "Thôn Cần Lương, xã An Dân (huyện Tuy An cũ), tỉnh Đắk Lắk",
    ["temple", "history", "heritage", "spiritual", "viewpoint"],
    {
        "rating": {"value": 4.5, "count": 1100, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách yêu thích ngôi cổ tự yên tĩnh trên đồi đá trắng, vườn tháp rêu phong và vườn xoài cổ thụ. Nhiều người khen không gian trầm mặc, tầm nhìn thoáng; một số nhắc nên đi buổi sáng và ăn mặc kín đáo khi vào chùa.",
        "ps_vi": "Chùa Đá Trắng, tên chữ là Từ Quang tự, là một trong những ngôi chùa cổ nhất vùng đất Phú Yên xưa, dựng năm 1797 thời Tây Sơn trên một ngọn đồi đá trắng ở xã An Dân. Chùa nổi tiếng với vườn tháp mộ cổ, kiến trúc trầm mặc và giống xoài Đá Trắng tiến vua.",
        "ps_en": "Da Trang Pagoda, formally Tu Quang Pagoda, is one of the oldest temples of the former Phu Yen region, founded in 1797 under the Tay Son dynasty on a hill of white stone in An Dan commune. It is famous for its ancient stupa garden, contemplative architecture and the tribute 'Da Trang' mangoes.",
        "ps_ru": "Пагода Дачанг, официально Тыкуанг, — один из старейших храмов бывшего края Фуйен, основанный в 1797 году при династии Тэйшон на холме из белого камня в общине Андан. Она известна старинным садом ступ, созерцательной архитектурой и «дачангскими» манго, которые подносили королям.",
        "pl_vi": "Chùa Đá Trắng, tên chữ là Bạch Thạch Từ Quang tự, tọa lạc ở thôn Cần Lương, xã An Dân, cách thành phố Tuy Hòa khoảng 35 km về phía bắc. Chùa được Thiền sư Pháp Chuyên, đời thứ 36 phái Lâm Tế, khai sơn năm 1797 dưới triều vua Cảnh Thịnh (Quang Toản) nhà Tây Sơn, và được xem là một trong những cổ tự đầu tiên của vùng đất Phú Yên. Vì tọa lạc trên một ngọn đồi phủ đầy những khối đá trắng phau nên dân gian quen gọi là chùa Đá Trắng. Trong khuôn viên có ngôi chánh điện cổ kính cùng một vườn tháp mộ rêu phong chạm trổ hoa văn tinh tế, nơi an nghỉ của các vị thiền sư qua nhiều thế hệ. Chùa còn nổi danh với giống xoài Đá Trắng trái nhỏ, thơm ngọt, từng được chọn tiến vua triều Nguyễn; vườn xoài cổ hàng trăm năm tuổi quanh chùa đã được công nhận là Cây Di sản Việt Nam. Trong hai cuộc kháng chiến, chùa từng là cơ sở của phong trào yêu nước và cách mạng. Ngày nay, du khách đến vãn cảnh, lễ Phật và ngắm toàn cảnh đồng quê Tuy An từ trên đồi. Di tích đã được xếp hạng cấp quốc gia. Từ ngày 1 tháng 7 năm 2025, khu vực này thuộc tỉnh Đắk Lắk (trước đây thuộc tỉnh Phú Yên).",
        "pl_en": "Da Trang Pagoda, formally Bach Thach Tu Quang Pagoda, stands in Can Luong hamlet, An Dan commune, about 35 km north of Tuy Hoa city. It was founded in 1797 by the Zen master Phap Chuyen, 36th generation of the Lam Te school, under King Canh Thinh (Quang Toan) of the Tay Son dynasty, and is regarded as one of the first ancient temples of the Phu Yen region. Because it sits on a hill strewn with gleaming white boulders, locals simply call it the White Stone Pagoda. Its grounds hold a venerable main hall and a moss-covered garden of finely carved memorial stupas where generations of Zen masters rest. The temple is also famed for the small, fragrant 'Da Trang' mango, once presented as tribute to the Nguyen court; the centuries-old mango orchard around it has been recognised as a Vietnam Heritage Tree group. During both resistance wars the pagoda served as a base for patriotic and revolutionary movements. Today visitors come to enjoy the scenery, pay respects and take in a sweeping view of the Tuy An countryside from the hill. The site is a ranked National Relic. Since 1 July 2025 the area has belonged to Dak Lak Province (formerly Phu Yen Province).",
        "pl_ru": "Пагода Дачанг, официально Бактхать-Тыкуанг, стоит в деревне Кэнлыонг, община Андан, примерно в 35 км к северу от города Туихоа. Её основал в 1797 году дзен-мастер Фапчуен, 36-го поколения школы Ламте, при короле Каньтхинь (Куангтоан) династии Тэйшон, и она считается одним из первых древних храмов края Фуйен. Поскольку храм расположен на холме, усыпанном сверкающими белыми валунами, местные жители просто называют его пагодой Белого камня. На его территории — старинный главный зал и покрытый мхом сад тонко украшенных мемориальных ступ, где покоятся поколения дзен-мастеров. Пагода также славится небольшим ароматным манго «дачанг», которое некогда подносили ко двору Нгуенов; окружающий её многовековой манговый сад признан группой деревьев — наследия Вьетнама. В обе войны сопротивления пагода служила базой патриотического и революционного движения. Сегодня гости приходят полюбоваться пейзажем, поклониться Будде и окинуть взглядом сельские просторы Туйана с холма. Объект внесён в список национальных памятников. С 1 июля 2025 года эта местность относится к провинции Даклак (ранее — провинция Фуйен).",
        "h_vi": ["Cổ tự dựng năm 1797, một trong những chùa xưa nhất Phú Yên cũ", "Vườn tháp mộ rêu phong và chánh điện trầm mặc trên đồi đá trắng", "Xoài Đá Trắng tiến vua; vườn xoài cổ là Cây Di sản Việt Nam"],
        "h_en": ["Ancient temple founded in 1797, among the oldest in former Phu Yen", "Moss-covered stupa garden and quiet main hall on a white-stone hill", "Tribute 'Da Trang' mangoes; the old orchard is a Vietnam Heritage Tree group"],
        "h_ru": ["Древний храм, основанный в 1797 году, из старейших в бывшем Фуйене", "Покрытый мхом сад ступ и тихий главный зал на холме из белого камня", "Манго «дачанг» для королей; старый сад — деревья-наследие Вьетнама"],
        "practical": {
            "hours_vi": "Mở cửa ban ngày, khoảng 7:00–17:00.",
            "ticket_vi": "Miễn phí; công đức tuỳ tâm.",
            "duration_vi": "Khoảng 1 giờ.",
            "best_time_vi": "Sáng sớm cho mát; mùa xoài chín khoảng tháng 4–5.",
            "tips_vi": "Ăn mặc kín đáo, lịch sự; đi giày dễ leo bậc đá; kết hợp tham quan đầm Ô Loan, Gành Đá Đĩa.",
        },
    },
))

NEW.append(mk(
    "dam-cu-mong", "Đầm Cù Mông",
    "Cu Mong Lagoon", "Лагуна Кумонг",
    13.5400, 109.2650, ["park_garden", "other"],
    "Khu vực bắc thị xã Sông Cầu cũ, giáp tỉnh Gia Lai, tỉnh Đắk Lắk",
    ["sea", "lagoon", "nature", "seafood", "outdoor"],
    {
        "rating": {"value": 4.3, "count": 700, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích khung cảnh đầm phá yên bình với bè nuôi thủy sản, núi bao quanh và hải sản tươi ngon. Nhiều người khen tôm hùm, sò huyết Sông Cầu; một số nhắc dịch vụ còn dân dã, nên đi thuyền cùng người địa phương.",
        "ps_vi": "Đầm Cù Mông là một đầm nước lợ lớn ở phía bắc vùng Sông Cầu, gần ranh giới với Gia Lai. Được dãy núi Cù Mông ôm quanh và thông ra biển qua một cửa hẹp, đầm nổi tiếng với cảnh quan bình yên, những bè nuôi tôm hùm và hải sản trứ danh của vùng đất Phú Yên xưa.",
        "ps_en": "Cu Mong Lagoon is a large brackish lagoon in the northern Song Cau area, near the boundary with Gia Lai. Embraced by the Cu Mong mountains and opening to the sea through a narrow mouth, it is known for peaceful scenery, floating lobster farms and the celebrated seafood of the former Phu Yen region.",
        "ps_ru": "Лагуна Кумонг — крупная солоноватоводная лагуна на севере района Шонгкау, у границы с провинцией Гиалай. Окружённая горами Кумонг и соединённая с морем узким проливом, она известна умиротворяющими пейзажами, плавучими фермами лангустов и прославленными морепродуктами бывшего края Фуйен.",
        "pl_vi": "Đầm Cù Mông là một trong những đầm nước lợ lớn của vùng đất Phú Yên xưa, nằm ở phía bắc khu vực Sông Cầu, ngay dưới chân đèo Cù Mông giáp ranh với Gia Lai. Đầm có diện tích rộng, được dãy núi Cù Mông và những bán đảo, cồn cát ôm lấy, chỉ thông ra biển qua một cửa hẹp nên mặt nước quanh năm lặng sóng. Trên đầm là hàng loạt bè nổi và lồng nuôi tôm hùm, cá mú, sò huyết, hàu; nghề nuôi trồng thủy sản khiến nơi đây trở thành một trong những vựa hải sản nổi tiếng của miền Trung. Du khách có thể thuê thuyền của ngư dân dạo quanh đầm, ghé thăm các bè nuôi, tự tay chọn tôm hùm rồi thưởng thức hải sản tươi ngay trên mặt nước. Khung cảnh sớm mai với sương giăng trên đầm, thuyền câu và bóng núi phản chiếu xuống mặt nước rất nên thơ, thích hợp cho những ai muốn tìm sự yên tĩnh, mộc mạc, tránh xa các bãi biển đông đúc. Vùng quanh đầm còn có nhiều làng chài và những vịnh, gành đá đẹp. Từ ngày 1 tháng 7 năm 2025, khu vực này thuộc tỉnh Đắk Lắk (trước đây thuộc tỉnh Phú Yên).",
        "pl_en": "Cu Mong Lagoon is one of the large brackish lagoons of the former Phu Yen region, lying in the northern Song Cau area at the foot of the Cu Mong Pass on the boundary with Gia Lai. The broad lagoon is enclosed by the Cu Mong mountains and by peninsulas and sandbars, opening to the sea only through a narrow mouth, so its surface stays calm year-round. It is dotted with floating rafts and cages farming lobster, grouper, blood cockles and oysters; this aquaculture has made it one of central Vietnam's celebrated seafood baskets. Visitors can hire a fisherman's boat to cruise the lagoon, call at the farms, pick their own lobster and enjoy the freshest seafood right on the water. The early-morning scene of mist over the lagoon, fishing boats and mountains mirrored in the water is deeply poetic, ideal for those seeking calm and simplicity away from crowded beaches. Around the lagoon are fishing villages and beautiful bays and rocky headlands. Since 1 July 2025 the area has belonged to Dak Lak Province (formerly Phu Yen Province).",
        "pl_ru": "Лагуна Кумонг — одна из крупных солоноватоводных лагун бывшего края Фуйен, расположенная на севере района Шонгкау у подножия перевала Кумонг, на границе с провинцией Гиалай. Широкая лагуна окружена горами Кумонг, полуостровами и песчаными косами и соединяется с морем лишь узким проливом, поэтому её поверхность круглый год спокойна. Она усеяна плавучими плотами и садками, где разводят лангустов, груперов, кровяных моллюсков и устриц; это рыбоводство сделало её одной из знаменитых «корзин морепродуктов» Центрального Вьетнама. Гости могут нанять рыбацкую лодку, чтобы обойти лагуну, заглянуть на фермы, самим выбрать лангуста и отведать свежайшие морепродукты прямо на воде. Утренний пейзаж с туманом над лагуной, рыбацкими лодками и отражением гор в воде очень поэтичен и идеален для тех, кто ищет тишину и простоту вдали от людных пляжей. Вокруг лагуны — рыбацкие деревни, красивые бухты и скалистые мысы. С 1 июля 2025 года эта местность относится к провинции Даклак (ранее — провинция Фуйен).",
        "h_vi": ["Đầm nước lợ lớn dưới chân đèo Cù Mông, mặt nước quanh năm lặng sóng", "Vựa tôm hùm, sò huyết, hàu nổi tiếng của Phú Yên cũ", "Đi thuyền thăm bè nuôi và thưởng thức hải sản tươi trên đầm"],
        "h_en": ["Large brackish lagoon below Cu Mong Pass, calm all year", "A famed basket of lobster, blood cockle and oyster of former Phu Yen", "Boat trips to the farms and fresh seafood on the water"],
        "h_ru": ["Крупная солоноватоводная лагуна под перевалом Кумонг, спокойная круглый год", "Знаменитая «корзина» лангустов, моллюсков и устриц бывшего Фуйена", "Прогулки на лодке к фермам и свежие морепродукты на воде"],
        "practical": {
            "hours_vi": "Khu vực mở cả ngày; đi thuyền nên vào buổi sáng.",
            "ticket_vi": "Tham quan tự do; thuê thuyền và ăn hải sản trả phí theo dịch vụ.",
            "duration_vi": "Khoảng 2–3 giờ.",
            "best_time_vi": "Mùa khô tháng 2–8; sáng sớm trời êm.",
            "tips_vi": "Thỏa thuận giá thuyền và hải sản trước; mang mũ, kem chống nắng; kết hợp ghé Vịnh Xuân Đài, Gành Đá Đĩa.",
        },
    },
))

NEW.append(mk(
    "cao-nguyen-van-hoa", "Cao nguyên Vân Hòa",
    "Van Hoa Plateau", "Плато Ванхоа",
    13.3000, 109.1050, ["park_garden", "other"],
    "Khu vực các xã Sơn Xuân, Sơn Long, Sơn Định (huyện Sơn Hòa cũ), tỉnh Đắk Lắk",
    ["nature", "viewpoint", "rural", "daytrip", "outdoor"],
    {
        "rating": {"value": 4.4, "count": 500, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích cao nguyên đất đỏ mát mẻ với đồi thông, vườn cây trái và không khí trong lành. Nhiều người ví như 'Đà Lạt của Phú Yên'; một số nhắc dịch vụ du lịch còn ít, nên chủ động phương tiện.",
        "ps_vi": "Cao nguyên Vân Hòa là vùng đất đỏ bazan cao khoảng 400 m so với mực nước biển, trải trên các xã của huyện Sơn Hòa cũ. Khí hậu quanh năm mát mẻ, cảnh quan đồi thông, vườn cây trái và những di tích lịch sử khiến nơi đây được ví như 'Đà Lạt' của vùng đất Phú Yên xưa.",
        "ps_en": "The Van Hoa Plateau is a red basaltic upland about 400 m above sea level, spread across communes of the former Son Hoa district. Its cool year-round climate, pine hills, orchards and historical sites have earned it the nickname the 'Da Lat' of the former Phu Yen region.",
        "ps_ru": "Плато Ванхоа — красное базальтовое нагорье на высоте около 400 м над уровнем моря, раскинувшееся по общинам бывшего района Шонхоа. Прохладный круглый год климат, сосновые холмы, фруктовые сады и исторические места принесли ему прозвище «Далат» бывшего края Фуйен.",
        "pl_vi": "Cao nguyên Vân Hòa là một cao nguyên đất đỏ bazan nằm ở phía tây bắc vùng đất Phú Yên xưa, trải rộng trên địa bàn các xã Sơn Xuân, Sơn Long, Sơn Định thuộc huyện Sơn Hòa cũ, ở độ cao khoảng 400 m so với mực nước biển. Nhờ vị trí trên cao và lớp phủ thực vật dày, khí hậu nơi đây quanh năm dịu mát, sáng sớm thường có sương mù bảng lảng, nên được nhiều người ví von là 'Đà Lạt' của Phú Yên. Vùng cao nguyên nổi tiếng với những đồi thông, rừng cây, các vườn cây ăn trái như mít, bơ, dứa và những trảng cỏ, ruộng bậc thang xen kẽ. Đây cũng là vùng đất giàu dấu ấn lịch sử: trên cao nguyên có địa đạo Gò Thì Thùng và Nhà thờ Bác Hồ – di tích căn cứ của tỉnh trong kháng chiến. Du khách đến Vân Hòa để tận hưởng không khí trong lành, ngắm cảnh đồng quê, tham quan các nhà vườn và thưởng thức đặc sản địa phương. Dù hạ tầng du lịch còn khá sơ khai, chính sự mộc mạc và yên bình lại là điều hấp dẫn những ai muốn khám phá một Phú Yên khác, mát mẻ và xanh mướt trên vùng cao. Từ ngày 1 tháng 7 năm 2025, khu vực này thuộc tỉnh Đắk Lắk (trước đây thuộc tỉnh Phú Yên).",
        "pl_en": "The Van Hoa Plateau is a red basaltic upland in the north-west of the former Phu Yen region, spread across the communes of Son Xuan, Son Long and Son Dinh in the former Son Hoa district, at about 400 m above sea level. Thanks to its elevation and thick vegetation, the climate is cool all year and mornings often bring drifting mist, so many liken it to a 'Da Lat' of Phu Yen. The plateau is known for pine hills, woodland, orchards of jackfruit, avocado and pineapple, and a patchwork of grassland and terraced fields. It is also rich in history: it holds the Go Thi Thung Tunnels and the 'Uncle Ho Temple', a relic of the province's wartime base. Visitors come to Van Hoa to breathe the fresh air, enjoy rural scenery, tour the garden farms and sample local produce. Although tourist infrastructure is still basic, that very simplicity and calm is what attracts those wishing to discover a different, cool and verdant side of Phu Yen in the highlands. Since 1 July 2025 the area has belonged to Dak Lak Province (formerly Phu Yen Province).",
        "pl_ru": "Плато Ванхоа — красное базальтовое нагорье на северо-западе бывшего края Фуйен, раскинувшееся по общинам Шонсуан, Шонлонг и Шондинь бывшего района Шонхоа, на высоте около 400 м над уровнем моря. Благодаря высоте и густой растительности климат здесь прохладный круглый год, а по утрам часто стелется туман, поэтому многие сравнивают эти места с «Далатом» Фуйена. Плато славится сосновыми холмами, лесами, садами джекфрута, авокадо и ананасов, а также чередованием лугов и террасных полей. Оно богато и историей: здесь находятся тоннели Готхитхунг и «Храм дядюшки Хо» — памятник провинциальной базы военных лет. Гости приезжают на Ванхоа подышать свежим воздухом, полюбоваться сельскими пейзажами, посетить садовые хозяйства и попробовать местные продукты. Хотя туристическая инфраструктура пока скромна, именно эта простота и покой привлекают тех, кто хочет открыть другую — прохладную и зелёную — сторону Фуйена в нагорье. С 1 июля 2025 года эта местность относится к провинции Даклак (ранее — провинция Фуйен).",
        "h_vi": ["Cao nguyên đất đỏ ~400 m, khí hậu mát mẻ quanh năm", "Được ví như 'Đà Lạt' của Phú Yên cũ với đồi thông, nhà vườn", "Nơi có địa đạo Gò Thì Thùng và Nhà thờ Bác Hồ (di tích căn cứ)"],
        "h_en": ["Red-soil plateau ~400 m high, cool all year round", "Nicknamed the 'Da Lat' of former Phu Yen, with pine hills and orchards", "Home to the Go Thi Thung Tunnels and the 'Uncle Ho Temple' base relic"],
        "h_ru": ["Плато из красной почвы ~400 м, прохладное круглый год", "Прозвано «Далатом» бывшего Фуйена: сосновые холмы и сады", "Здесь тоннели Готхитхунг и «Храм дядюшки Хо» — памятник базы"],
        "practical": {
            "hours_vi": "Vùng cảnh quan mở cả ngày.",
            "ticket_vi": "Tham quan tự do; một số nhà vườn có thể thu phí nhỏ.",
            "duration_vi": "Nửa ngày đến cả ngày.",
            "best_time_vi": "Sáng sớm nhiều sương; mát mẻ quanh năm, đẹp mùa cây trái.",
            "tips_vi": "Chủ động xe máy/ô tô vì điểm tham quan cách xa nhau; mang áo khoác mỏng vì buổi sáng se lạnh; kết hợp thăm địa đạo Gò Thì Thùng.",
        },
    },
))

NEW.append(mk(
    "cau-treo-buon-don", "Cầu treo Buôn Đôn",
    "Buon Don Suspension Bridge", "Подвесной мост Буондон",
    12.9030, 107.7920, ["bridge", "other"],
    "Buôn Trí A, xã Krông Na, huyện Buôn Đôn, tỉnh Đắk Lắk",
    ["bridge", "river", "nature", "ethnic", "viewpoint"],
    {
        "rating": {"value": 4.2, "count": 3400, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích cây cầu tre – gỗ đung đưa bắc qua sông Sêrêpôk và cảm giác đi bộ trên tán cây ven sông. Nhiều người thấy vui và mạo hiểm nhẹ; một số nhắc cầu rung, đông khách và nên đi giày bám tốt.",
        "ps_vi": "Cầu treo Buôn Đôn là hệ thống cầu tre và gỗ bắc qua dòng sông Sêrêpôk huyền thoại tại trung tâm du lịch Buôn Đôn, cách Buôn Ma Thuột khoảng 45 km. Những nhịp cầu đung đưa nối các cây si cổ thụ và cù lao giữa sông, mang lại trải nghiệm khám phá đặc trưng của vùng đất voi Tây Nguyên.",
        "ps_en": "Buon Don Suspension Bridge is a system of bamboo-and-timber footbridges strung across the legendary Serepok River at the Buon Don tourist centre, about 45 km from Buon Ma Thuot. Its swaying spans link ancient banyan trees and river islets, offering an experience typical of the elephant land of the Central Highlands.",
        "ps_ru": "Подвесной мост Буондон — система бамбуково-деревянных пешеходных мостиков, переброшенных через легендарную реку Серепок в туристическом центре Буондон, примерно в 45 км от Буонматхуота. Раскачивающиеся пролёты соединяют старые баньяны и речные островки, даря впечатление, характерное для «слоновьего края» Центрального нагорья.",
        "pl_vi": "Cầu treo Buôn Đôn là một trong những biểu tượng du lịch của huyện Buôn Đôn, nằm trong khu du lịch cầu treo bên dòng Sêrêpôk – con sông hiếm hoi chảy ngược về phía tây sang đất Campuchia. Cây cầu được người dân dựng chủ yếu từ tre, nứa, song mây và gỗ, gác lên những thân cây si cổ thụ hàng trăm năm tuổi mọc ven bờ và trên các cù lao giữa sông, tạo thành một mạng lưới cầu và sàn nghỉ đung đưa theo nhịp bước chân. Đi trên cầu, du khách vừa lắc lư giữa tán lá xanh mát, vừa ngắm dòng Sêrêpôk cuộn chảy qua ghềnh đá phía dưới, cảm nhận rõ vẻ hoang sơ, hùng vĩ của núi rừng Tây Nguyên. Khu vực này gắn liền với văn hóa của người Ê Đê, M'Nông và Lào, nổi tiếng với nghề săn bắt và thuần dưỡng voi rừng; quanh cầu còn có nhà sàn cổ, mộ vua săn voi và các buôn làng truyền thống. Buôn Đôn cũng là nơi du khách tìm hiểu đời sống của các cộng đồng bản địa và thưởng thức ẩm thực, rượu cần đặc trưng. Trung tâm du lịch thường mở cửa ban ngày và thu vé vào cổng. Cây cầu treo mộc mạc chính là điểm 'phải trải nghiệm' khi đặt chân đến vùng đất voi.",
        "pl_en": "Buon Don Suspension Bridge is one of the tourism symbols of Buon Don district, set within the suspension-bridge park beside the Serepok, a rare river that flows westward toward Cambodia. Local people built it mainly from bamboo, rattan and timber, resting it on the trunks of centuries-old banyan trees along the bank and on river islets, forming a network of bridges and rest platforms that sway with every step. Crossing it, visitors bob among cool green foliage while watching the Serepok surge over rapids below, feeling the wild grandeur of the Central Highlands forest. The area is bound up with the culture of the Ede, M'Nong and Lao peoples, famed for capturing and taming wild elephants; nearby stand old stilt houses, the elephant hunters' tombs and traditional villages. Buon Don is also where travellers learn about the life of indigenous communities and sample local food and can ruou (jar wine). The tourist centre is usually open by day with an entrance fee. The rustic suspension bridge is the must-try experience on arriving in the elephant land.",
        "pl_ru": "Подвесной мост Буондон — один из туристических символов района Буондон, расположенный в парке подвесных мостов у реки Серепок, редкой реки, текущей на запад в сторону Камбоджи. Местные жители построили его в основном из бамбука, ротанга и дерева, опирая на стволы вековых баньянов вдоль берега и на речные островки, образуя сеть мостиков и площадок для отдыха, которые раскачиваются при каждом шаге. Проходя по нему, гости покачиваются среди прохладной зелёной листвы и наблюдают, как Серепок несётся по порогам внизу, ощущая дикое величие лесов Центрального нагорья. Эти места связаны с культурой народов эде, мнонг и лао, прославленных ловлей и приручением диких слонов; поблизости стоят старые свайные дома, гробницы охотников на слонов и традиционные деревни. В Буондоне путешественники также знакомятся с жизнью коренных общин, пробуют местную кухню и рисовое вино из кувшина. Туристический центр обычно открыт днём и берёт плату за вход. Простой подвесной мост — обязательное впечатление по прибытии в «слоновий край».",
        "h_vi": ["Cầu tre – gỗ đung đưa bắc qua sông Sêrêpôk huyền thoại", "Gác trên những cây si cổ thụ hàng trăm năm ven sông", "Gắn với văn hóa voi và các buôn làng Ê Đê, M'Nông, Lào"],
        "h_en": ["Swaying bamboo-and-timber bridge over the legendary Serepok River", "Resting on centuries-old banyan trees along the bank", "Tied to elephant culture and Ede, M'Nong and Lao villages"],
        "h_ru": ["Раскачивающийся бамбуково-деревянный мост над легендарной рекой Серепок", "Опирается на вековые баньяны вдоль берега", "Связан с культурой слонов и деревнями эде, мнонг и лао"],
        "practical": {
            "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
            "ticket_vi": "Vé vào khu du lịch khoảng 40.000 VND/người lớn (tham khảo).",
            "duration_vi": "Khoảng 1,5–2 giờ (cả khu Buôn Đôn).",
            "best_time_vi": "Mùa khô tháng 11–4; buổi sáng mát.",
            "tips_vi": "Đi giày bám tốt vì cầu rung và trơn; giữ trẻ nhỏ cẩn thận; kết hợp thăm mộ vua săn voi, nhà sàn cổ và Vườn quốc gia Yok Đôn.",
        },
    },
))

NEW.append(mk(
    "dinh-lac-giao", "Đình Lạc Giao",
    "Lac Giao Communal House", "Общинный дом Лакзяо",
    12.6720, 108.0430, ["monument", "other"],
    "Số 67 đường Phan Bội Châu, trung tâm thành phố Buôn Ma Thuột, tỉnh Đắk Lắk",
    ["history", "heritage", "spiritual", "city", "monument"],
    {
        "rating": {"value": 4.4, "count": 800, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách đánh giá cao ngôi đình Việt đầu tiên ở Tây Nguyên với kiến trúc truyền thống và ý nghĩa lịch sử. Nhiều người thấy không gian trang nghiêm, yên tĩnh giữa phố; một số nhắc nên tìm hiểu trước để cảm nhận rõ giá trị di tích.",
        "ps_vi": "Đình Lạc Giao là ngôi đình của người Việt đầu tiên trên vùng đất Tây Nguyên, tọa lạc ngay trung tâm thành phố Buôn Ma Thuột. Khởi dựng năm 1928, đình thờ Thành hoàng và các bậc tiền hiền, gắn với quá trình lập làng Lạc Giao và nhiều sự kiện lịch sử của Đắk Lắk; đây là Di tích lịch sử cấp quốc gia.",
        "ps_en": "Lac Giao Communal House is the first Vietnamese communal house in the Central Highlands, standing in the heart of Buon Ma Thuot city. Founded in 1928, it venerates the village guardian deity and pioneers, is tied to the founding of Lac Giao village and to many events in Dak Lak's history, and is a National Historical Relic.",
        "ps_ru": "Общинный дом Лакзяо — первый вьетнамский общинный дом в Центральном нагорье, стоящий в самом центре города Буонматхуот. Основанный в 1928 году, он посвящён духу-покровителю деревни и первопоселенцам, связан с основанием деревни Лакзяо и многими событиями истории Даклака и является национальным историческим памятником.",
        "pl_vi": "Đình Lạc Giao tọa lạc tại số 67 đường Phan Bội Châu, ngay trung tâm thành phố Buôn Ma Thuột, và được xem là ngôi đình của cộng đồng người Việt đầu tiên được dựng lên trên vùng đất Tây Nguyên. Đình được khởi dựng năm 1928 (ban đầu bằng tranh tre) và xây lại kiên cố vào năm 1932, thờ Thành hoàng cùng các bậc tiền hiền có công khai phá, lập nên làng Lạc Giao của những lưu dân người Kinh đầu thế kỷ 20. Cái tên 'Lạc Giao' mang ý nghĩa về mối giao hòa, đoàn kết giữa người Kinh và đồng bào các dân tộc bản địa. Không chỉ là nơi thờ tự và sinh hoạt tín ngưỡng, đình còn chứng kiến nhiều sự kiện lịch sử quan trọng: đây là nơi ra mắt Ủy ban Quân quản thị xã Buôn Ma Thuột tháng 3 năm 1975 và là nơi tưởng niệm các nạn nhân trong biến cố đêm 1 tháng 12 năm 1945. Với những giá trị đó, Đình Lạc Giao đã được Bộ Văn hóa – Thông tin xếp hạng Di tích lịch sử cấp quốc gia năm 1990. Ngày nay, ngôi đình mang kiến trúc truyền thống với mái ngói, sân gạch và cây xanh là một điểm đến để tìm hiểu lịch sử hình thành đô thị Buôn Ma Thuột.",
        "pl_en": "Lac Giao Communal House stands at 67 Phan Boi Chau Street in the heart of Buon Ma Thuot city and is regarded as the first Vietnamese communal house built in the Central Highlands. First raised in 1928 (originally of thatch and bamboo) and rebuilt in solid form in 1932, it venerates the guardian deity and the pioneers who cleared the land and founded Lac Giao village for early-20th-century Kinh settlers. The name 'Lac Giao' evokes harmony and solidarity between the Kinh and the indigenous peoples. More than a place of worship and ritual, the house has witnessed important historical events: it is where the Buon Ma Thuot Military Management Committee was launched in March 1975 and where the victims of the tragedy on the night of 1 December 1945 are commemorated. For these values, the Ministry of Culture and Information ranked Lac Giao a National Historical Relic in 1990. Today the house, with its traditional tiled roof, brick courtyard and greenery, is a place to learn the story of how the city of Buon Ma Thuot came to be.",
        "pl_ru": "Общинный дом Лакзяо стоит по адресу улица Фанбойтяу, 67, в самом центре города Буонматхуот и считается первым вьетнамским общинным домом, построенным в Центральном нагорье. Впервые возведённый в 1928 году (изначально из тростника и бамбука) и перестроенный в капитальном виде в 1932 году, он посвящён духу-покровителю и первопоселенцам, которые расчистили землю и основали деревню Лакзяо для переселенцев-кинь начала XX века. Название «Лакзяо» напоминает о гармонии и единстве между кинь и коренными народами. Это не только место поклонения и обрядов: дом стал свидетелем важных исторических событий — здесь в марте 1975 года был учреждён Военно-управленческий комитет Буонматхуота и поминают жертв трагедии в ночь на 1 декабря 1945 года. За эти заслуги Министерство культуры и информации в 1990 году внесло Лакзяо в список национальных исторических памятников. Сегодня дом с традиционной черепичной крышей, кирпичным двором и зеленью — место, где можно узнать историю становления города Буонматхуот.",
        "h_vi": ["Ngôi đình của người Việt đầu tiên trên đất Tây Nguyên (khởi dựng 1928)", "Gắn với việc lập làng Lạc Giao và nhiều sự kiện lịch sử Buôn Ma Thuột", "Di tích lịch sử cấp quốc gia (1990), kiến trúc đình truyền thống"],
        "h_en": ["First Vietnamese communal house in the Central Highlands (founded 1928)", "Tied to founding Lac Giao village and to Buon Ma Thuot history", "National Historical Relic (1990) with traditional communal-house architecture"],
        "h_ru": ["Первый вьетнамский общинный дом в Центральном нагорье (основан в 1928)", "Связан с основанием деревни Лакзяо и историей Буонматхуота", "Национальный памятник (1990) с традиционной архитектурой"],
        "practical": {
            "hours_vi": "Ban ngày, khoảng 7:00–17:00; các dịp lễ có tế lễ.",
            "ticket_vi": "Miễn phí; công đức tuỳ tâm.",
            "duration_vi": "Khoảng 30–45 phút.",
            "best_time_vi": "Quanh năm; dịp lễ tế Thành hoàng rất đặc sắc.",
            "tips_vi": "Ăn mặc lịch sự, giữ trang nghiêm; kết hợp tham quan Bảo tàng Đắk Lắk, Nhà đày Buôn Ma Thuột gần đó.",
        },
    },
))

NEW.append(mk(
    "troh-bu", "Khu du lịch sinh thái Troh Bư",
    "Troh Bu Ecotourism Garden", "Экопарк Чобы",
    12.7150, 107.9550, ["park_garden", "other"],
    "Buôn Niêng 3, xã Ea Nuôl, huyện Buôn Đôn, tỉnh Đắk Lắk",
    ["nature", "garden", "orchid", "family", "outdoor"],
    {
        "rating": {"value": 4.4, "count": 2100, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích khu vườn sinh thái xanh mát với hồ nước, suối, vườn lan rừng và nhiều góc chụp ảnh đẹp. Nhiều người khen không gian yên tĩnh, gần Buôn Ma Thuột; một số nhắc dịch vụ ăn uống nên đặt trước.",
        "ps_vi": "Khu du lịch sinh thái Troh Bư nằm ở xã Ea Nuôl, huyện Buôn Đôn, cách Buôn Ma Thuột khoảng 10 km. Nổi bật với vườn lan rừng tự nhiên vào loại lớn nhất Việt Nam cùng hồ nước, suối và cây rừng, Troh Bư được xem là 'khu vườn cảnh quan' đẹp của Tây Nguyên.",
        "ps_en": "Troh Bu Ecotourism Garden lies in Ea Nuol commune, Buon Don district, about 10 km from Buon Ma Thuot. Distinguished by one of Vietnam's largest natural forest-orchid gardens along with a lake, streams and woodland, Troh Bu is regarded as a beautiful 'landscape garden' of the Central Highlands.",
        "ps_ru": "Экопарк Чобы находится в общине Еануол, район Буондон, примерно в 10 км от Буонматхуота. Он выделяется одним из крупнейших во Вьетнаме природных садов лесных орхидей, а также озером, ручьями и лесом, и считается красивым «ландшафтным садом» Центрального нагорья.",
        "pl_vi": "Khu du lịch sinh thái Troh Bư tọa lạc tại buôn Niêng 3, xã Ea Nuôl, huyện Buôn Đôn, chỉ cách trung tâm Buôn Ma Thuột khoảng 10 km về phía tây. Trong tiếng Ê Đê, 'Troh Bư' có nghĩa là 'thung lũng cá lóc suối', gắn với một truyền thuyết của người bản địa. Khởi đầu là một khu vườn rừng do người dân gây dựng và bảo tồn, nơi đây dần trở thành điểm du lịch sinh thái nổi tiếng với diện tích hơn hai héc-ta, được ví như một 'khu vườn cảnh quan' đẹp bậc nhất Tây Nguyên. Điểm đặc sắc nhất của Troh Bư là vườn sưu tập và bảo tồn lan rừng thuộc loại lớn nhất Việt Nam, quy tụ hàng trăm loài lan quý; bên cạnh đó là hồ nước trong, những con suối nhỏ, cầu tre, nhà sàn và các loài cây rừng bản địa xanh mát quanh năm. Du khách đến đây để dạo bộ giữa thiên nhiên, chèo thuyền, chụp ảnh, tìm hiểu về hệ thực vật Tây Nguyên và thưởng thức ẩm thực địa phương. Không gian yên tĩnh, trong lành và gần thành phố khiến Troh Bư trở thành lựa chọn lý tưởng cho những chuyến dã ngoại, nghỉ dưỡng ngắn ngày và các gia đình có trẻ nhỏ khi ghé thăm thủ phủ cà phê Buôn Ma Thuột.",
        "pl_en": "Troh Bu Ecotourism Garden sits in Buon Nieng 3, Ea Nuol commune, Buon Don district, only about 10 km west of central Buon Ma Thuot. In the Ede language 'Troh Bu' means 'valley of the stream snakehead fish', linked to an indigenous legend. Beginning as a forest garden created and conserved by locals, it has grown into a well-known ecotourism site of over two hectares, likened to one of the finest 'landscape gardens' of the Central Highlands. Its highlight is a collection and conservation garden of forest orchids counted among the largest in Vietnam, gathering hundreds of rare species; alongside are a clear lake, small streams, bamboo bridges, stilt houses and native forest trees that stay green all year. Visitors come to stroll through nature, row boats, take photos, learn about Central Highlands flora and enjoy local cuisine. Its quiet, fresh setting close to the city makes Troh Bu an ideal choice for picnics, short retreats and families with children visiting the coffee capital of Buon Ma Thuot.",
        "pl_ru": "Экопарк Чобы расположен в деревне Буонньенг-3, община Еануол, район Буондон, всего примерно в 10 км к западу от центра Буонматхуота. На языке эде «Чобы» означает «долина ручьёвой змееголовой рыбы» и связано с легендой коренного народа. Начавшись как лесной сад, созданный и сохранённый местными жителями, он превратился в известный объект экотуризма площадью более двух гектаров, который сравнивают с одним из лучших «ландшафтных садов» Центрального нагорья. Его главная особенность — коллекционно-заповедный сад лесных орхидей, входящий в число крупнейших во Вьетнаме и объединяющий сотни редких видов; рядом — прозрачное озеро, небольшие ручьи, бамбуковые мостики, свайные дома и местные лесные деревья, зелёные круглый год. Гости приходят прогуляться среди природы, покататься на лодке, пофотографировать, узнать о флоре нагорья и отведать местную кухню. Тихая, свежая обстановка вблизи города делает Чобы идеальным выбором для пикников, коротких выездов и семей с детьми, приезжающих в кофейную столицу Буонматхуот.",
        "h_vi": ["Vườn sưu tập lan rừng thuộc loại lớn nhất Việt Nam", "Hồ nước, suối, cầu tre và cây rừng xanh mát, chỉ cách BMT ~10 km", "Tên Ê Đê nghĩa là 'thung lũng cá lóc suối', gắn với truyền thuyết bản địa"],
        "h_en": ["One of Vietnam's largest forest-orchid collection gardens", "Lake, streams, bamboo bridges and green forest, just ~10 km from BMT", "Ede name means 'valley of the stream snakehead', from a local legend"],
        "h_ru": ["Один из крупнейших во Вьетнаме садов лесных орхидей", "Озеро, ручьи, бамбуковые мостики и зелёный лес, всего ~10 км от БМТ", "Название на эде — «долина ручьёвой змееголовой», из местной легенды"],
        "practical": {
            "hours_vi": "Khoảng 7:30–18:00 hằng ngày.",
            "ticket_vi": "Vé vào cổng thấp; dịch vụ ăn uống, chèo thuyền tính riêng.",
            "duration_vi": "Khoảng 2–3 giờ.",
            "best_time_vi": "Mùa khô tháng 11–4; sáng hoặc chiều mát.",
            "tips_vi": "Đặt trước nếu muốn ăn trưa; mang giày đi bộ; thích hợp cho gia đình, kết hợp tuyến Buôn Đôn.",
        },
    },
))

NEW.append(mk(
    "thac-bay-nhanh", "Thác Bảy Nhánh (Buôn Đôn)",
    "Bay Nhanh (Seven-Branch) Waterfall", "Водопад Байнянь (Семь рукавов)",
    12.8990, 107.8050, ["park_garden", "other"],
    "Xã Krông Na (khu vực Buôn Đôn), bên sông Sêrêpôk, tỉnh Đắk Lắk",
    ["waterfall", "river", "nature", "adventure", "outdoor"],
    {
        "rating": {"value": 4.2, "count": 900, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích thác trải rộng thành nhiều nhánh giữa rừng và các trải nghiệm cầu treo, chèo thuyền, cưỡi voi lội sông. Nhiều người thấy hoang sơ, thú vị; một số nhắc mùa khô nước ít, nên đi mùa mưa để thác đẹp hơn.",
        "ps_vi": "Thác Bảy Nhánh là thác nước trên dòng Sêrêpôk ở khu vực Buôn Đôn, nơi con sông tách ra thành nhiều nhánh chảy vòng quanh các cù lao và ghềnh đá rồi hợp lại. Nằm giữa rừng khộp Tây Nguyên, thác gắn với các trải nghiệm cầu treo, chèo thuyền độc mộc và khám phá thiên nhiên hoang sơ.",
        "ps_en": "Bay Nhanh (Seven-Branch) Waterfall is a cascade on the Serepok River in the Buon Don area, where the river splits into several branches winding around islets and rocky rapids before rejoining. Set amid the dry dipterocarp forest of the Central Highlands, it pairs with suspension-bridge walks, dugout canoeing and wild nature.",
        "ps_ru": "Водопад Байнянь («Семь рукавов») — каскад на реке Серепок в районе Буондон, где река разделяется на несколько рукавов, огибающих островки и скалистые пороги, а затем вновь сливается. Расположенный среди сухого диптерокарпового леса Центрального нагорья, он сочетается с прогулками по подвесным мостам, греблей на долблёнках и дикой природой.",
        "pl_vi": "Thác Bảy Nhánh nằm trên dòng sông Sêrêpôk thuộc khu vực Buôn Đôn, huyện Buôn Đôn, cách trung tâm Buôn Ma Thuột khoảng 40 km. Sở dĩ có tên gọi này vì đến đoạn thác, dòng Sêrêpôk bị các cù lao và bãi đá chia cắt, tách ra thành nhiều nhánh nước chảy len lỏi qua rừng cây rồi lại hợp dòng, tạo nên khung cảnh sông nước – thác ghềnh vừa mềm mại vừa mạnh mẽ. Xung quanh thác là những cánh rừng khộp và cây cổ thụ ven sông đặc trưng của Tây Nguyên, khí hậu mát mẻ, không gian yên tĩnh. Đây là một phần trong quần thể du lịch Buôn Đôn, nơi du khách có thể đi bộ trên các cầu treo bắc qua sông, ngồi thuyền độc mộc, trải nghiệm cưỡi voi lội sông (một hoạt động truyền thống đang dần được thay bằng du lịch thân thiện với voi), câu cá hay cắm trại giữa thiên nhiên. Vào mùa mưa, lượng nước dồi dào khiến các nhánh thác tung bọt trắng xóa, đẹp và hùng vĩ hơn hẳn mùa khô. Thác Bảy Nhánh cùng cầu treo, mộ vua săn voi và các buôn làng tạo nên chuỗi điểm đến hấp dẫn của vùng đất voi Buôn Đôn.",
        "pl_en": "Bay Nhanh Waterfall lies on the Serepok River in the Buon Don area, about 40 km from central Buon Ma Thuot. It owes its name to the way the Serepok, meeting islets and rock bars at this stretch, splits into several branches that thread through the trees before rejoining, creating a river-and-rapids scene at once gentle and powerful. Around it stand the dry dipterocarp forest and old riverside trees typical of the Central Highlands, with a cool climate and quiet air. It forms part of the Buon Don tourism complex, where visitors can walk the suspension bridges across the river, ride dugout canoes, try elephant river-crossing rides (a tradition gradually giving way to elephant-friendly tourism), fish or camp in nature. In the rainy season abundant water sends the branches foaming white, far grander than in the dry months. Together with the suspension bridge, the elephant hunters' tombs and the villages, Bay Nhanh Waterfall forms an appealing chain of destinations in the Buon Don elephant land.",
        "pl_ru": "Водопад Байнянь находится на реке Серепок в районе Буондон, примерно в 40 км от центра Буонматхуота. Своё название он получил из-за того, что Серепок, встречая на этом участке островки и каменные гряды, разделяется на несколько рукавов, пробирающихся между деревьями и вновь сливающихся, создавая речной пейзаж с порогами — одновременно мягкий и мощный. Вокруг — сухой диптерокарповый лес и старые прибрежные деревья, характерные для Центрального нагорья, прохладный климат и тишина. Он входит в туристический комплекс Буондон, где гости могут пройти по подвесным мостам через реку, покататься на долблёных лодках, попробовать переправу на слонах через реку (традиция, постепенно уступающая место дружественному к слонам туризму), порыбачить или разбить лагерь на природе. В сезон дождей обильная вода вспенивает рукава добела, и водопад выглядит гораздо величественнее, чем в сухие месяцы. Вместе с подвесным мостом, гробницами охотников на слонов и деревнями водопад Байнянь образует привлекательную цепочку мест «слоновьего края» Буондон.",
        "h_vi": ["Sông Sêrêpôk tách thành nhiều nhánh qua cù lao và ghềnh đá", "Nằm trong quần thể du lịch Buôn Đôn với cầu treo, thuyền độc mộc", "Đẹp và hùng vĩ nhất vào mùa mưa khi nước dồi dào"],
        "h_en": ["The Serepok splits into many branches through islets and rapids", "Part of the Buon Don complex with suspension bridges and dugout canoes", "Grandest in the rainy season when water is abundant"],
        "h_ru": ["Серепок разделяется на множество рукавов среди островков и порогов", "Часть комплекса Буондон с подвесными мостами и долблёнками", "Наиболее величествен в сезон дождей при обилии воды"],
        "practical": {
            "hours_vi": "Khoảng 7:00–18:00 hằng ngày (theo khu du lịch Buôn Đôn).",
            "ticket_vi": "Vé và dịch vụ theo khu du lịch Buôn Đôn.",
            "duration_vi": "Khoảng 1–2 giờ.",
            "best_time_vi": "Mùa mưa (khoảng tháng 6–10) thác nhiều nước và đẹp nhất.",
            "tips_vi": "Đi giày bám tốt, cẩn thận đá trơn; ưu tiên trải nghiệm thân thiện với voi; kết hợp cầu treo và Yok Đôn.",
        },
    },
))

NEW.append(mk(
    "mo-vua-san-voi", "Mộ Vua Săn Voi (Khunjunob)",
    "Tomb of the Elephant Hunting King (Khunjunob)", "Гробница «короля охотников на слонов» (Кхунжуноб)",
    12.9050, 107.7850, ["monument", "other"],
    "Buôn Trí, xã Krông Na, huyện Buôn Đôn, tỉnh Đắk Lắk",
    ["history", "ethnic", "heritage", "monument"],
    {
        "rating": {"value": 4.3, "count": 600, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thấy thú vị với ngôi mộ kết hợp kiến trúc Ê Đê, Lào và tháp Khmer, gắn với huyền thoại săn voi. Nhiều người khen câu chuyện lịch sử hấp dẫn; một số nhắc nên có hướng dẫn để hiểu ý nghĩa.",
        "ps_vi": "Mộ Vua Săn Voi là khu lăng mộ của N'Thu K'Nul – người khai lập Buôn Đôn và được tôn xưng là 'vua săn voi' (Khunjunob) nhờ tài săn bắt, thuần dưỡng hàng trăm con voi rừng. Ngôi mộ ở Buôn Trí, xã Krông Na, mang kiến trúc pha trộn Ê Đê – Lào – Khmer độc đáo.",
        "ps_en": "The Tomb of the Elephant Hunting King is the mausoleum of N'Thu K'Nul, founder of Buon Don, honoured as the 'elephant hunting king' (Khunjunob) for capturing and taming hundreds of wild elephants. Located in Buon Tri, Krong Na commune, it blends a distinctive Ede–Lao–Khmer architecture.",
        "ps_ru": "Гробница «короля охотников на слонов» — мавзолей Нтху Кнула, основателя Буондона, почитаемого как «король охотников на слонов» (Кхунжуноб) за поимку и приручение сотен диких слонов. Расположенная в деревне Буончи, община Кронгна, она сочетает самобытную архитектуру эде, лао и кхмеров.",
        "pl_vi": "Mộ Vua Săn Voi nằm ở buôn Trí, xã Krông Na, huyện Buôn Đôn, là nơi an nghỉ của N'Thu K'Nul – vị tù trưởng huyền thoại được xem là người khai sinh ra Buôn Đôn và nghề săn bắt, thuần dưỡng voi rừng ở Tây Nguyên. Tương truyền, ông đã săn và thuần được hàng trăm con voi, trong đó có cả voi trắng quý hiếm đem tặng vua Xiêm, nhờ đó được phong tặng danh hiệu 'Khunjunob', nghĩa là 'vua săn voi'. Khu mộ nổi bật với lối kiến trúc pha trộn giữa nét nhà mồ của người Ê Đê, M'Nông với phong cách chùa tháp Lào và Khmer, thể hiện qua các chóp nhọn, hoa văn và màu sắc đặc trưng; đây là dấu ấn của sự giao thoa văn hóa các dân tộc từng sinh sống, buôn bán ở vùng biên giới này. Xung quanh còn có mộ của những người kế nghiệp săn voi và các nhà mồ khác. Đến đây, du khách không chỉ chiêm ngưỡng công trình độc đáo mà còn được nghe những câu chuyện, huyền thoại về nghề săn voi lừng danh một thời của Buôn Đôn. Khu mộ thường được ghép trong hành trình tham quan cầu treo, nhà sàn cổ và các buôn làng của vùng đất voi.",
        "pl_en": "The Tomb of the Elephant Hunting King stands in Buon Tri, Krong Na commune, Buon Don district, the resting place of N'Thu K'Nul, the legendary chieftain regarded as the founder of Buon Don and of the Central Highlands craft of capturing and taming wild elephants. He is said to have hunted and tamed hundreds of elephants, including a rare white elephant given to the King of Siam, for which he received the title 'Khunjunob', meaning 'elephant hunting king'. The tomb is striking for an architecture blending the Ede and M'Nong grave-house tradition with Lao and Khmer temple-tower styles, seen in its pointed spires, ornament and distinctive colours, a mark of the cultural mixing among the peoples who once lived and traded in this border region. Around it lie the tombs of his successors in elephant hunting and other grave houses. Visitors here not only admire the unusual monument but also hear the tales and legends of Buon Don's once-famous elephant-hunting craft. The tomb is usually combined with tours of the suspension bridge, old stilt houses and villages of the elephant land.",
        "pl_ru": "Гробница «короля охотников на слонов» стоит в деревне Буончи, община Кронгна, район Буондон, — место упокоения Нтху Кнула, легендарного вождя, которого считают основателем Буондона и центральнонагорного ремесла ловли и приручения диких слонов. Говорят, он поймал и приручил сотни слонов, в том числе редкого белого слона, подаренного королю Сиама, за что получил титул «Кхунжуноб» — «король охотников на слонов». Гробница поражает архитектурой, сочетающей традицию домов-могил эде и мнонг с лаосским и кхмерским стилем храмовых башен: остроконечные шпили, орнамент и характерные цвета — знак смешения культур народов, некогда живших и торговавших в этом приграничье. Рядом покоятся его преемники в охоте на слонов и другие дома-могилы. Здесь гости не только любуются необычным памятником, но и слушают предания и легенды о некогда знаменитом слоновьем промысле Буондона. Гробницу обычно включают в маршруты с посещением подвесного моста, старых свайных домов и деревень «слоновьего края».",
        "h_vi": ["Nơi an nghỉ của 'vua săn voi' N'Thu K'Nul, người khai lập Buôn Đôn", "Kiến trúc pha trộn Ê Đê – Lào – Khmer độc đáo", "Gắn với huyền thoại săn và thuần dưỡng hàng trăm con voi rừng"],
        "h_en": ["Resting place of the 'elephant hunting king' N'Thu K'Nul, founder of Buon Don", "Distinctive Ede–Lao–Khmer blended architecture", "Tied to legends of hunting and taming hundreds of wild elephants"],
        "h_ru": ["Место упокоения «короля охотников на слонов» Нтху Кнула, основателя Буондона", "Самобытная архитектура, сочетающая эде, лао и кхмеров", "Связана с легендами о поимке и приручении сотен диких слонов"],
        "practical": {
            "hours_vi": "Ban ngày theo tuyến du lịch Buôn Đôn.",
            "ticket_vi": "Thường gộp trong vé khu du lịch Buôn Đôn.",
            "duration_vi": "Khoảng 30–45 phút.",
            "best_time_vi": "Mùa khô tháng 11–4; đi cùng tuyến cầu treo Buôn Đôn.",
            "tips_vi": "Nên có hướng dẫn viên để hiểu ý nghĩa kiến trúc và huyền thoại; giữ trang nghiêm nơi mộ.",
        },
    },
))

NEW.append(mk(
    "buon-jun", "Buôn Jun (Hồ Lắk)",
    "Jun Village (Lak Lake)", "Деревня Джун (озеро Лак)",
    12.4230, 108.1850, ["other", "park_garden"],
    "Thị trấn Liên Sơn, huyện Lắk, bên hồ Lắk, tỉnh Đắk Lắk",
    ["ethnic", "lake", "culture", "nature", "homestay"],
    {
        "rating": {"value": 4.3, "count": 1500, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích buôn làng M'Nông bên hồ Lắk với nhà sàn dài, thuyền độc mộc và không gian yên bình. Nhiều người khen trải nghiệm văn hóa và cảnh hồ; một số nhắc nên ưu tiên du lịch thân thiện với voi.",
        "ps_vi": "Buôn Jun là một buôn làng cổ của người M'Nông nằm bên bờ hồ Lắk – hồ nước ngọt tự nhiên lớn nhất Tây Nguyên, thuộc thị trấn Liên Sơn, huyện Lắk. Với những ngôi nhà sàn dài truyền thống, thuyền độc mộc và nếp sống bản địa, Buôn Jun là điểm đến để trải nghiệm văn hóa và cảnh quan hồ nước thanh bình.",
        "ps_en": "Buon Jun is an old M'Nong village on the shore of Lak Lake, the largest natural freshwater lake in the Central Highlands, in Lien Son town, Lak district. With its traditional longhouses, dugout canoes and indigenous way of life, Buon Jun is a place to experience culture and the serene lake scenery.",
        "ps_ru": "Буон Джун — старинная деревня народа мнонг на берегу озера Лак, крупнейшего природного пресноводного озера Центрального нагорья, в посёлке Лиеншон, район Лак. Со своими традиционными длинными свайными домами, долблёными лодками и укладом коренного народа Буон Джун — место, где знакомятся с культурой и безмятежными пейзажами озера.",
        "pl_vi": "Buôn Jun là một buôn làng lâu đời của người M'Nông R'Lăm, nằm ngay bên bờ hồ Lắk thuộc thị trấn Liên Sơn, huyện Lắk, cách thành phố Buôn Ma Thuột khoảng 55 km về phía nam. Hồ Lắk là hồ nước ngọt tự nhiên lớn nhất Tây Nguyên và thuộc hàng lớn nhất Việt Nam, quanh năm phẳng lặng, được núi rừng và những cánh đồng lúa bao quanh. Trong buôn còn lưu giữ nhiều ngôi nhà sàn dài truyền thống lợp mái, nơi các gia đình M'Nông sinh sống qua nhiều thế hệ, cùng nghề dệt thổ cẩm, đan lát và văn hóa cồng chiêng, rượu cần. Du khách đến Buôn Jun thường ngồi thuyền độc mộc lướt trên mặt hồ, ngắm hoàng hôn, tìm hiểu đời sống bản địa, nghỉ tại các nhà sàn homestay và thưởng thức ẩm thực dân tộc. Không xa buôn là Biệt điện Bảo Đại trên đồi cao nhìn xuống hồ, từng là nơi nghỉ của vị vua cuối cùng triều Nguyễn. Cưỡi voi quanh hồ từng là hoạt động phổ biến, nay được khuyến khích thay bằng các hình thức du lịch thân thiện với voi. Buôn Jun và hồ Lắk mang lại một trải nghiệm Tây Nguyên đậm bản sắc, yên bình và gần gũi thiên nhiên.",
        "pl_en": "Buon Jun is a long-established village of the M'Nong R'Lam people on the shore of Lak Lake in Lien Son town, Lak district, about 55 km south of Buon Ma Thuot city. Lak Lake is the largest natural freshwater lake in the Central Highlands and among the largest in Vietnam, calm year-round and ringed by mountains and rice fields. The village still keeps many traditional roofed longhouses where M'Nong families have lived for generations, along with brocade weaving, basketry and the culture of gongs and jar wine. Visitors to Buon Jun often ride dugout canoes across the lake, watch the sunset, learn about indigenous life, stay in longhouse homestays and enjoy ethnic cuisine. Not far away, the Bao Dai Villa crowns a hill overlooking the lake, once a retreat of the last Nguyen emperor. Riding elephants around the lake was once common but is now being encouraged to give way to elephant-friendly tourism. Buon Jun and Lak Lake offer a deeply authentic, peaceful Central Highlands experience close to nature.",
        "pl_ru": "Буон Джун — давно основанная деревня народа мнонг-рлам на берегу озера Лак в посёлке Лиеншон, район Лак, примерно в 55 км к югу от города Буонматхуот. Озеро Лак — крупнейшее природное пресноводное озеро Центрального нагорья и одно из крупнейших во Вьетнаме, спокойное круглый год и окружённое горами и рисовыми полями. В деревне сохранилось множество традиционных крытых длинных домов, где семьи мнонг живут из поколения в поколение, а также ткачество парчи, плетение и культура гонгов и рисового вина из кувшина. Гости Буон Джуна часто катаются на долблёных лодках по озеру, любуются закатом, знакомятся с жизнью коренного народа, останавливаются в длинных домах-хоумстеях и пробуют национальную кухню. Неподалёку на холме над озером возвышается вилла Бао Дая, некогда резиденция последнего императора династии Нгуен. Катание на слонах вокруг озера прежде было обычным делом, но теперь его призывают заменять дружественным к слонам туризмом. Буон Джун и озеро Лак дарят по-настоящему самобытное, умиротворённое впечатление Центрального нагорья в близости к природе.",
        "h_vi": ["Buôn làng M'Nông cổ bên hồ Lắk – hồ nước ngọt lớn nhất Tây Nguyên", "Nhà sàn dài truyền thống, thuyền độc mộc, cồng chiêng, rượu cần", "Gần Biệt điện Bảo Đại; nên ưu tiên du lịch thân thiện với voi"],
        "h_en": ["Old M'Nong village by Lak Lake, the Central Highlands' largest freshwater lake", "Traditional longhouses, dugout canoes, gongs and jar wine", "Near the Bao Dai Villa; favour elephant-friendly tourism"],
        "h_ru": ["Старинная деревня мнонг у озера Лак, крупнейшего пресного озера нагорья", "Традиционные длинные дома, долблёнки, гонги и рисовое вино", "Рядом вилла Бао Дая; предпочтителен дружественный к слонам туризм"],
        "practical": {
            "hours_vi": "Buôn làng mở cả ngày; thuyền và homestay theo dịch vụ.",
            "ticket_vi": "Vé tham quan/đi thuyền thấp; homestay và ăn uống tính riêng.",
            "duration_vi": "Nửa ngày (hoặc nghỉ đêm homestay).",
            "best_time_vi": "Mùa khô tháng 11–4; hoàng hôn trên hồ rất đẹp.",
            "tips_vi": "Đi thuyền độc mộc ngắm hồ; tôn trọng phong tục bản địa; ưu tiên trải nghiệm thân thiện với voi; kết hợp Biệt điện Bảo Đại.",
        },
    },
))

NEW.append(mk(
    "nha-tho-chinh-toa-bmt", "Nhà thờ Chính tòa Buôn Ma Thuột (Nhà thờ Thánh Tâm)",
    "Buon Ma Thuot Cathedral (Sacred Heart Cathedral)", "Кафедральный собор Буонматхуота (собор Святого Сердца)",
    12.6640, 108.0490, ["church"],
    "Đường Phan Chu Trinh, trung tâm thành phố Buôn Ma Thuột, tỉnh Đắk Lắk",
    ["church", "architecture", "city", "spiritual", "photo"],
    {
        "rating": {"value": 4.6, "count": 2300, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách ấn tượng với nhà thờ mang dáng nhà rông Tây Nguyên, mái dài lợp ngói và kết cấu gỗ ấm áp. Nhiều người khen kiến trúc độc đáo, hòa quyện văn hóa bản địa; một số nhắc giữ yên tĩnh khi có thánh lễ.",
        "ps_vi": "Nhà thờ Chính tòa Buôn Ma Thuột, còn gọi là nhà thờ Thánh Tâm, là nhà thờ chính của Giáo phận Buôn Ma Thuột. Công trình nổi bật với kiến trúc mô phỏng dáng nhà rông – nhà dài Tây Nguyên, mái ngói vươn dài trên khung gỗ, tạo nên vẻ đẹp hòa quyện giữa Công giáo và văn hóa bản địa.",
        "ps_en": "Buon Ma Thuot Cathedral, also called Sacred Heart Cathedral, is the mother church of the Buon Ma Thuot Diocese. It stands out for architecture echoing the Central Highlands' rong and longhouses, with a long tiled roof over a timber frame, blending Catholic and indigenous cultures.",
        "ps_ru": "Кафедральный собор Буонматхуота, также называемый собором Святого Сердца, — главный храм епархии Буонматхуот. Он выделяется архитектурой, напоминающей общинные и длинные дома Центрального нагорья: длинная черепичная крыша на деревянном каркасе сочетает католическую и коренную культуру.",
        "pl_vi": "Nhà thờ Chính tòa Buôn Ma Thuột, quen gọi là nhà thờ Thánh Tâm, tọa lạc trên đường Phan Chu Trinh ngay trung tâm thành phố và là nhà thờ mẹ của Giáo phận Buôn Ma Thuột. Điều khiến ngôi thánh đường này trở nên đặc biệt và thu hút du khách chính là lối kiến trúc độc đáo: thay vì kiểu nhà thờ Gothic quen thuộc, công trình được thiết kế mô phỏng hình dáng ngôi nhà rông, nhà dài của đồng bào các dân tộc Tây Nguyên. Gian nhà thờ có mái ngói dốc dài vươn thấp xuống, đỡ bởi hệ khung và hàng cột gỗ lớn, bên trong ấm áp với vật liệu gỗ và ánh sáng dịu, gợi cảm giác gần gũi, mộc mạc mà vẫn trang nghiêm. Sự kết hợp giữa tinh thần Công giáo và bản sắc văn hóa bản địa khiến nhà thờ Thánh Tâm được xem là một trong những nhà thờ có kiến trúc đẹp và riêng biệt nhất vùng Tây Nguyên. Đây vừa là nơi sinh hoạt tôn giáo của cộng đồng giáo dân, vừa là điểm tham quan, chụp ảnh được nhiều du khách yêu thích khi đến Buôn Ma Thuột. Du khách nên đến vào ban ngày để chiêm ngưỡng kiến trúc và giữ yên tĩnh, tôn trọng khi có thánh lễ diễn ra.",
        "pl_en": "Buon Ma Thuot Cathedral, popularly the Sacred Heart Cathedral, stands on Phan Chu Trinh Street in the heart of the city and is the mother church of the Buon Ma Thuot Diocese. What makes this church special and draws visitors is its unusual architecture: instead of the familiar Gothic style, it is designed to echo the rong and longhouses of the Central Highlands peoples. The nave has a long, steep tiled roof sweeping low, carried on a frame and rows of large wooden columns, and inside it feels warm with timber and soft light, at once intimate, rustic and solemn. This blend of Catholic spirit and indigenous identity makes Sacred Heart one of the most beautiful and distinctive churches in the Central Highlands. It serves both as a place of worship for the parish community and as a sightseeing and photography spot much loved by travellers to Buon Ma Thuot. Visitors are best coming by day to admire the architecture, keeping quiet and respectful when Mass is being held.",
        "pl_ru": "Кафедральный собор Буонматхуота, в народе — собор Святого Сердца, стоит на улице Фантютринь в центре города и является главным храмом епархии Буонматхуот. Особенным и привлекательным для гостей его делает необычная архитектура: вместо привычного готического стиля он спроектирован так, чтобы напоминать общинные и длинные дома народов Центрального нагорья. У нефа длинная крутая черепичная крыша, низко спускающаяся вниз, опирающаяся на каркас и ряды больших деревянных колонн, а внутри тепло от дерева и мягкого света — уютно, просто и вместе с тем торжественно. Такое сочетание католического духа и коренной самобытности делает собор Святого Сердца одним из самых красивых и своеобразных храмов Центрального нагорья. Он служит и местом богослужения для прихода, и объектом осмотра и фотосъёмки, любимым путешественниками, приезжающими в Буонматхуот. Приходить лучше днём, чтобы полюбоваться архитектурой, соблюдая тишину и уважение во время мессы.",
        "h_vi": ["Nhà thờ mẹ của Giáo phận Buôn Ma Thuột, dáng nhà rông – nhà dài Tây Nguyên", "Mái ngói dài trên khung và cột gỗ lớn, không gian ấm áp", "Kiến trúc hòa quyện Công giáo và văn hóa bản địa độc đáo"],
        "h_en": ["Mother church of the diocese, shaped like a Central Highlands rong/longhouse", "Long tiled roof on a timber frame with big wooden columns", "A rare blend of Catholic and indigenous architecture"],
        "h_ru": ["Главный храм епархии в форме общинного/длинного дома нагорья", "Длинная черепичная крыша на деревянном каркасе с большими колоннами", "Редкое сочетание католической и коренной архитектуры"],
        "practical": {
            "hours_vi": "Mở cửa ban ngày; giờ thánh lễ nên tra trước.",
            "ticket_vi": "Miễn phí.",
            "duration_vi": "Khoảng 30–45 phút.",
            "best_time_vi": "Ban ngày để ngắm kiến trúc; tránh làm ồn khi có lễ.",
            "tips_vi": "Ăn mặc lịch sự; giữ yên tĩnh khi có thánh lễ; kết hợp Bảo tàng Thế giới Cà phê, Đình Lạc Giao.",
        },
    },
))

NEW.append(mk(
    "bai-bien-tuy-hoa", "Bãi biển Tuy Hòa",
    "Tuy Hoa Beach", "Пляж Туихоа",
    13.0870, 109.3170, ["park_garden", "other"],
    "Dọc đường Độc Lập, trung tâm thành phố Tuy Hòa, tỉnh Đắk Lắk",
    ["beach", "sea", "city", "family", "outdoor"],
    {
        "rating": {"value": 4.5, "count": 4200, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích bãi biển thành phố dài, cát vàng, sóng vừa và bình minh đẹp ngay trung tâm Tuy Hòa. Nhiều người khen sạch, thoáng, tiện đi dạo và ăn hải sản; một số nhắc trưa nắng gắt, nên tắm sáng sớm hoặc chiều.",
        "ps_vi": "Bãi biển Tuy Hòa là bãi biển trung tâm của thành phố Tuy Hòa, trải dài với bờ cát vàng phẳng, hàng dừa và rặng phi lao xanh. Nằm ngay trong lòng đô thị, đây là nơi lý tưởng để tắm biển, đón bình minh và tản bộ, gắn liền với đời sống của người dân vùng đất Phú Yên xưa.",
        "ps_en": "Tuy Hoa Beach is the central beach of Tuy Hoa city, a long stretch of flat golden sand fringed by coconut palms and casuarina. Right within the urban core, it is ideal for swimming, greeting the sunrise and strolling, and is woven into the daily life of the former Phu Yen area.",
        "ps_ru": "Пляж Туихоа — центральный пляж города Туихоа, длинная полоса ровного золотистого песка, окаймлённая кокосовыми пальмами и казуаринами. Находясь в самом центре города, он идеален для купания, встречи рассвета и прогулок и тесно вплетён в повседневную жизнь бывшего края Фуйен.",
        "pl_vi": "Bãi biển Tuy Hòa là bãi tắm nằm ngay trung tâm thành phố Tuy Hòa, chạy dài dọc theo đường Độc Lập với bờ cát vàng rộng, thoai thoải và tương đối phẳng. Khác với nhiều bãi biển tách biệt, bãi biển Tuy Hòa gắn liền với nhịp sống đô thị: mỗi sáng sớm và chiều muộn, người dân ra biển tắm, tập thể dục, đá bóng, còn du khách thì tản bộ trên con đường ven biển rợp bóng dừa và phi lao. Vì quay mặt về hướng đông, đây là một trong những nơi đón bình minh đẹp, khi mặt trời từ từ nhô lên khỏi mặt biển, nhuộm hồng cả bờ cát và những chiếc thuyền ngoài khơi. Dọc bờ biển có quảng trường, tượng đài, công viên, khách sạn và nhiều quán hải sản, khiến nơi đây trở thành trung tâm vui chơi, thư giãn của thành phố. Cách bãi không xa là các điểm nổi tiếng như Tháp Nhạn, Núi Chóp Chài, giúp du khách dễ dàng kết hợp trong hành trình khám phá thành phố. Với vẻ đẹp mộc mạc, sạch sẽ và thuận tiện, bãi biển Tuy Hòa là điểm dừng chân quen thuộc của mọi du khách khi đến vùng đất 'hoa vàng cỏ xanh'. Từ ngày 1 tháng 7 năm 2025, khu vực này thuộc tỉnh Đắk Lắk (trước đây thuộc tỉnh Phú Yên).",
        "pl_en": "Tuy Hoa Beach is the bathing beach right in the centre of Tuy Hoa city, running along Doc Lap Street with a broad, gently sloping and fairly flat shore of golden sand. Unlike many secluded beaches, Tuy Hoa Beach is bound up with city life: at dawn and dusk locals come to swim, exercise and play football, while visitors stroll the seaside promenade shaded by coconut palms and casuarina. Facing east, it is one of the finer places to greet the sunrise, when the sun climbs slowly from the sea and tints the sand and the offshore boats pink. Along the shore are a square, monuments, parks, hotels and many seafood eateries, making it the city's hub of leisure and relaxation. Not far away stand famous sights such as Nhan Tower and Chop Chai Mountain, easy to combine on a city tour. With its simple, clean and convenient charm, Tuy Hoa Beach is a familiar stop for every traveller to the 'yellow flowers on green grass' land. Since 1 July 2025 the area has belonged to Dak Lak Province (formerly Phu Yen Province).",
        "pl_ru": "Пляж Туихоа — купальный пляж в самом центре города Туихоа, тянущийся вдоль улицы Доклап широкой, полого спускающейся и довольно ровной полосой золотистого песка. В отличие от многих уединённых пляжей, Туихоа тесно связан с городской жизнью: на рассвете и закате местные жители приходят купаться, заниматься спортом и играть в футбол, а гости прогуливаются по приморской набережной в тени кокосовых пальм и казуарин. Обращённый на восток, он — одно из лучших мест для встречи рассвета, когда солнце медленно поднимается из моря и окрашивает песок и лодки вдали в розовый цвет. Вдоль берега — площадь, памятники, парки, отели и множество рыбных кафе, что делает пляж центром отдыха города. Неподалёку находятся знаменитые достопримечательности — башня Нян и гора Тьоптяй, которые легко совместить в городской прогулке. Простой, чистый и удобный, пляж Туихоа — привычная остановка для каждого путешественника по краю «жёлтых цветов на зелёной траве». С 1 июля 2025 года эта местность относится к провинции Даклак (ранее — провинция Фуйен).",
        "h_vi": ["Bãi biển ngay trung tâm thành phố Tuy Hòa, cát vàng phẳng dài", "Đón bình minh đẹp; đường ven biển rợp dừa và phi lao", "Gần Tháp Nhạn, Núi Chóp Chài, tiện kết hợp tham quan"],
        "h_en": ["City-centre beach of Tuy Hoa with long, flat golden sand", "Fine sunrise spot; seaside promenade shaded by palms and casuarina", "Near Nhan Tower and Chop Chai Mountain for easy combining"],
        "h_ru": ["Пляж в центре города Туихоа с длинным ровным золотистым песком", "Отличное место рассвета; набережная в тени пальм и казуарин", "Рядом башня Нян и гора Тьоптяй — удобно совместить"],
        "practical": {
            "hours_vi": "Bãi công cộng, mở cả ngày; đẹp nhất bình minh và chiều.",
            "ticket_vi": "Miễn phí.",
            "duration_vi": "Khoảng 1–2 giờ.",
            "best_time_vi": "Bình minh và chiều muộn; mùa khô tháng 1–8.",
            "tips_vi": "Tắm sáng sớm hoặc chiều để tránh nắng gắt; chú ý sóng và dòng chảy; kết hợp Tháp Nhạn gần đó.",
        },
    },
))

NEW.append(mk(
    "hon-chua", "Hòn Chùa",
    "Hon Chua Island", "Остров Хонтюа",
    13.1650, 109.3540, ["park_garden", "other"],
    "Ngoài khơi xã An Phú (khu vực Long Thủy), thành phố Tuy Hòa, tỉnh Đắk Lắk",
    ["island", "sea", "snorkeling", "nature", "outdoor"],
    {
        "rating": {"value": 4.4, "count": 800, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thích hòn đảo hoang sơ với nước trong, rạn san hô và lặn ngắm biển. Nhiều người khen yên tĩnh, ít dịch vụ nên còn nguyên vẻ tự nhiên; một số nhắc nên đi thuyền của ngư dân và mang theo đồ ăn, nước.",
        "ps_vi": "Hòn Chùa là hòn đảo nhỏ hoang sơ nằm ngoài khơi làng biển Long Thủy, xã An Phú, cách bờ khoảng vài km. Với làn nước trong xanh, rạn san hô và bãi đá đẹp, đảo là điểm lặn ngắm biển, dã ngoại và tận hưởng thiên nhiên yên tĩnh của vùng đất Phú Yên xưa.",
        "ps_en": "Hon Chua is a small, unspoiled island off the fishing village of Long Thuy in An Phu commune, a few kilometres from shore. With clear water, coral reefs and pretty rocks, it is a spot for snorkelling, picnicking and enjoying the quiet nature of the former Phu Yen area.",
        "ps_ru": "Хонтюа — небольшой нетронутый остров у рыбацкой деревни Лонгтхюй в общине Анфу, в нескольких километрах от берега. С прозрачной водой, коралловыми рифами и красивыми скалами это место для снорклинга, пикников и тихого отдыха на природе бывшего края Фуйен.",
        "pl_vi": "Hòn Chùa là một hòn đảo nhỏ nằm ngoài khơi làng biển Long Thủy, xã An Phú, cách trung tâm thành phố Tuy Hòa khoảng 10 km. Cùng với hai đảo nhỏ lân cận là Hòn Than và Hòn Dứa, Hòn Chùa tạo thành một cụm đảo ven bờ còn giữ được vẻ hoang sơ, ít chịu tác động của du lịch ồ ạt. Để ra đảo, du khách thường thuê thuyền của ngư dân Long Thủy, lênh đênh chừng hai mươi phút đến nửa giờ trên mặt biển. Quanh đảo, nước biển trong xanh với những rạn san hô và đàn cá đủ màu, là nơi lý tưởng để lặn ống thở ngắm san hô, bơi lội và câu cá. Trên đảo có bãi đá, bãi cát nhỏ và thảm thực vật tự nhiên, thích hợp cho các nhóm bạn, gia đình tổ chức dã ngoại, cắm trại và nướng hải sản. Vì gần như chưa có dịch vụ cố định, du khách nên chuẩn bị sẵn đồ ăn, nước uống, dụng cụ lặn và thỏa thuận giờ đón với chủ thuyền. Chính sự vắng vẻ, trong lành và gần gũi thiên nhiên đã khiến Hòn Chùa trở thành lựa chọn yêu thích của những người muốn trốn khỏi phố thị, khám phá biển đảo theo cách mộc mạc. Từ ngày 1 tháng 7 năm 2025, khu vực này thuộc tỉnh Đắk Lắk (trước đây thuộc tỉnh Phú Yên).",
        "pl_en": "Hon Chua is a small island off the fishing village of Long Thuy in An Phu commune, about 10 km from central Tuy Hoa city. Together with two neighbouring islets, Hon Than and Hon Dua, it forms a coastal cluster that keeps its wild character, little touched by mass tourism. To reach it, visitors usually hire a Long Thuy fisherman's boat for a twenty-minute to half-hour crossing. Around the island the water is clear, with coral reefs and shoals of colourful fish, making it ideal for snorkelling, swimming and fishing. On the island are rocky shores, small sandy patches and natural vegetation, good for groups and families to picnic, camp and grill seafood. Because there are almost no fixed services, visitors should bring their own food, water and snorkelling gear and agree a pick-up time with the boat owner. Its very emptiness, freshness and closeness to nature make Hon Chua a favourite for those wanting to escape the town and explore island life the simple way. Since 1 July 2025 the area has belonged to Dak Lak Province (formerly Phu Yen Province).",
        "pl_ru": "Хонтюа — небольшой остров у рыбацкой деревни Лонгтхюй в общине Анфу, примерно в 10 км от центра города Туихоа. Вместе с двумя соседними островками, Хонтхан и Хонзыа, он образует прибрежную группу, сохраняющую дикий характер и мало затронутую массовым туризмом. Чтобы добраться до него, гости обычно нанимают лодку рыбака из Лонгтхюя и плывут двадцать–тридцать минут. Вокруг острова прозрачная вода с коралловыми рифами и стайками разноцветных рыб — идеальное место для снорклинга, купания и рыбалки. На острове — скалистые берега, небольшие песчаные участки и естественная растительность, удобные для пикников, кемпинга и приготовления морепродуктов на гриле группами и семьями. Поскольку постоянных услуг почти нет, гостям стоит взять с собой еду, воду и снаряжение для снорклинга и договориться с владельцем лодки о времени возвращения. Именно безлюдность, свежесть и близость к природе делают Хонтюа любимым местом тех, кто хочет сбежать из города и просто исследовать островную жизнь. С 1 июля 2025 года эта местность относится к провинции Даклак (ранее — провинция Фуйен).",
        "h_vi": ["Đảo nhỏ hoang sơ ngoài khơi làng biển Long Thủy", "Nước trong, rạn san hô – điểm lặn ống thở và câu cá", "Gần như chưa có dịch vụ, hợp dã ngoại và cắm trại mộc mạc"],
        "h_en": ["Small unspoiled island off Long Thuy fishing village", "Clear water and coral reefs for snorkelling and fishing", "Almost no services, ideal for simple picnics and camping"],
        "h_ru": ["Небольшой нетронутый остров у рыбацкой деревни Лонгтхюй", "Прозрачная вода и коралловые рифы для снорклинга и рыбалки", "Почти нет услуг — идеален для простых пикников и кемпинга"],
        "practical": {
            "hours_vi": "Ra đảo ban ngày; đi và về theo thuyền ngư dân.",
            "ticket_vi": "Không thu vé; chi phí chính là thuê thuyền (thỏa thuận).",
            "duration_vi": "Nửa ngày đến cả ngày.",
            "best_time_vi": "Biển êm mùa khô tháng 2–8; đi buổi sáng.",
            "tips_vi": "Thỏa thuận giá và giờ đón với chủ thuyền; mang đồ ăn, nước, dụng cụ lặn; mặc áo phao; chú ý thời tiết.",
        },
    },
))

# ===INSERT_RECORDS_ABOVE===

def main():
    d = json.load(open(F, encoding="utf-8")) if os.path.exists(F) else []
    have = {p["slug"] for p in d}
    added = [p for p in NEW if p["slug"] not in have]
    d += added
    json.dump(d, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Them moi:", len(added), "| tong hien co:", len(d))
    print("Slug them:", ", ".join(p["slug"] for p in added))
    skipped = [p["slug"] for p in NEW if p["slug"] in have]
    if skipped:
        print("Bo qua (da co):", ", ".join(skipped))


if __name__ == "__main__":
    main()
