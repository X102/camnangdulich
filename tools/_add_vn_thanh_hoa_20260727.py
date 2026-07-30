# -*- coding: utf-8 -*-
"""_add_vn_thanh_hoa_20260727.py

Bổ sung các địa điểm du lịch NỔI TIẾNG còn THIẾU của tỉnh Thanh Hóa
(đơn vị hành chính GIỮ NGUYÊN sau sáp nhập 1/7/2025 — 1 trong 11 tỉnh/thành
không sắp xếp). region_name_vi = "Thanh Hóa", federal_district = "Miền Trung".

Chèn AN TOÀN: nạp file hiện có (nếu có) -> append -> ghi; bỏ qua slug đã tồn tại.
Maps để trống -> tools/retrofit_map_links.py sẽ tự sinh link TRỎ THẲNG thẻ địa điểm.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
F = os.path.join(ROOT, "data", "regions", "vn-thanh-hoa.json")

REG = "vn-thanh-hoa"
RNAME = "Thanh Hóa"
FD = "Miền Trung"


def rec(slug, **kw):
    r = {
        "id": f"{REG}-{slug}",
        "slug": slug,
        "region": REG,
        "country": "vietnam",
        "region_name_vi": RNAME,
        "federal_district": FD,
    }
    r.update(kw)
    r.setdefault("photo", None)
    r.setdefault("photo_credit", None)
    r.setdefault("official_site", None)
    r.setdefault("status", "enriched")
    r.setdefault("last_updated", "2026-07-27")
    return r


new = []

# ==== records appended below ====

new += [
    rec(
        "den-ba-trieu",
        name_vi="Đền Bà Triệu",
        name_ru="Храм Ба Чиеу",
        name_en="Ba Trieu Temple",
        categories=["monument", "other"],
        coordinates={"lat": 19.8577, "lon": 105.8161},
        address_vi="Chân núi Gai, làng Phú Điền, xã Triệu Lộc, huyện Hậu Lộc, tỉnh Thanh Hóa",
        rating={"value": 4.6, "count": 2100, "source": "Google", "as_of": "2026-07"},
        review_summary_vi="Du khách đánh giá đây là ngôi đền cổ kính, uy nghiêm, không gian xanh mát và linh thiêng. Nhiều người ấn tượng với kiến trúc gỗ chạm khắc tinh xảo và cảm giác trang nghiêm khi dâng hương tưởng nhớ vị nữ anh hùng; một số góp ý nên đến vào dịp lễ hội để cảm nhận trọn vẹn không khí.",
        presentation_short_vi="Đền Bà Triệu nằm dưới chân núi Gai, xã Triệu Lộc, huyện Hậu Lộc, thờ nữ anh hùng Triệu Thị Trinh — người lãnh đạo cuộc khởi nghĩa chống quân Ngô năm 248. Quần thể di tích quốc gia đặc biệt này nổi bật với kiến trúc gỗ cổ kính, lăng mộ trên đỉnh núi Tùng và lễ hội tưởng niệm long trọng hằng năm.",
        presentation_short_en="Ba Trieu Temple sits at the foot of Gai Mountain in Trieu Loc, Hau Loc, honouring the heroine Trieu Thi Trinh who led an uprising against the Wu forces in 248 AD. This special national relic is admired for its ancient wooden architecture, the hilltop tomb on Tung Mountain and a solemn annual festival.",
        presentation_short_ru="Храм Ба Чиеу расположен у подножия горы Гай в общине Чиеулок уезда Хаулок и посвящён героине Чиеу Тхи Чинь, возглавившей в 248 году восстание против войск У. Этот особый памятник национального значения славится старинной деревянной архитектурой, гробницей на вершине горы Тунг и торжественным ежегодным праздником.",
        presentation_long_vi="Đền Bà Triệu là một trong những di tích lịch sử được tôn kính bậc nhất xứ Thanh, tọa lạc bên Quốc lộ 1A, cách thành phố Thanh Hóa khoảng 18 km về phía bắc. Đền thờ Triệu Thị Trinh (Bà Triệu), nữ tướng chỉ mới ngoài hai mươi tuổi đã dựng cờ khởi nghĩa chống ách đô hộ của nhà Ngô năm 248. Câu nói khảng khái của bà — nguyện 'cưỡi cơn gió mạnh, đạp luồng sóng dữ' chứ không chịu khom lưng làm tì thiếp — đã trở thành biểu tượng bất khuất của phụ nữ Việt Nam. Quần thể di tích trải rộng dưới chân núi Gai gồm nghi môn, sân đền, tiền đường, trung đường và hậu cung, với nhiều mảng chạm khắc gỗ, đá tinh xảo qua các triều đại. Cách đó không xa, trên đỉnh núi Tùng là lăng mộ Bà Triệu cùng khu mộ ba ông tướng họ Lý. Hằng năm, lễ hội Bà Triệu diễn ra vào tháng Hai âm lịch với rước kiệu, tế lễ, trò diễn dân gian, thu hút đông đảo người dân và du khách. Được xếp hạng Di tích quốc gia đặc biệt, nơi đây vừa là điểm hành hương tâm linh, vừa là địa chỉ giáo dục truyền thống yêu nước cho các thế hệ.",
        presentation_long_en="Ba Trieu Temple is one of the most revered historical sites in Thanh Hoa, standing beside National Highway 1A about 18 km north of Thanh Hoa city. It is dedicated to Trieu Thi Trinh, known as Lady Trieu, a warrior barely past twenty who raised the banner of revolt against Wu Chinese rule in 248 AD. Her defiant vow — to 'ride the strong winds and trample the fierce waves' rather than bow as a concubine — became an enduring symbol of the unyielding spirit of Vietnamese women. Spread across the foot of Gai Mountain, the complex includes a ceremonial gate, courtyards and successive worship halls filled with fine wood and stone carvings accumulated over many dynasties. Nearby, atop Tung Mountain, lie the tomb of Lady Trieu and the graves of three Ly-family generals who fought beside her. Each year in the second lunar month a grand festival brings palanquin processions, rituals and folk performances, drawing crowds of pilgrims and visitors. Ranked as a special national relic, the temple is at once a place of spiritual pilgrimage and a living lesson in patriotism passed down through the generations.",
        presentation_long_ru="Храм Ба Чиеу — одно из самых почитаемых исторических мест провинции Тханьхоа; он стоит у национального шоссе № 1A примерно в 18 км к северу от города Тханьхоа. Храм посвящён Чиеу Тхи Чинь, известной как госпожа Чиеу, — воительнице, которой едва исполнилось двадцать, когда в 248 году она подняла знамя восстания против китайского владычества династии У. Её дерзкие слова — что она желает 'оседлать могучий ветер и растоптать свирепые волны', но не склониться в рабской покорности, — стали вечным символом несгибаемого духа вьетнамских женщин. Комплекс раскинулся у подножия горы Гай и включает церемониальные врата, дворы и последовательные залы поклонения с тонкой резьбой по дереву и камню, накопленной за многие династии. Неподалёку, на вершине горы Тунг, находятся гробница госпожи Чиеу и могилы трёх полководцев из рода Ли, сражавшихся рядом с ней. Каждый год во втором лунном месяце здесь проходит большой праздник с процессиями паланкинов, обрядами и народными представлениями, привлекающий множество паломников и гостей. Признанный особым памятником национального значения, храм служит и местом духовного паломничества, и живым уроком патриотизма для новых поколений.",
        highlights_vi=[
            "Thờ Bà Triệu (Triệu Thị Trinh) — nữ anh hùng khởi nghĩa chống quân Ngô năm 248",
            "Di tích quốc gia đặc biệt với kiến trúc gỗ, đá cổ kính bên chân núi Gai",
            "Lăng mộ trên đỉnh núi Tùng và lễ hội Bà Triệu long trọng tháng Hai âm lịch",
        ],
        highlights_en=[
            "Honours Lady Trieu (Trieu Thi Trinh), heroine of the 248 AD anti-Wu uprising",
            "Special national relic with ancient wood-and-stone architecture below Gai Mountain",
            "Hilltop tomb on Tung Mountain and a grand festival in the second lunar month",
        ],
        highlights_ru=[
            "Посвящён госпоже Чиеу (Чиеу Тхи Чинь), героине восстания против У в 248 году",
            "Особый памятник страны со старинной деревянной и каменной архитектурой у горы Гай",
            "Гробница на вершине горы Тунг и большой праздник во втором лунном месяце",
        ],
        practical={
            "hours_vi": "Mở cửa hằng ngày, khoảng 7:00–18:00; vào các ngày rằm, mồng một và dịp lễ hội đông hơn.",
            "ticket_vi": "Vào cửa tự do; khách công đức tùy tâm.",
            "duration_vi": "Khoảng 1–2 giờ (cả tham quan đền và lăng mộ núi Tùng).",
            "best_time_vi": "Đẹp nhất vào dịp lễ hội tháng Hai âm lịch; nên đi buổi sáng cho mát.",
            "tips_vi": "Ăn mặc lịch sự khi vào đền; kết hợp thăm cả khu lăng trên núi Tùng gần đó; giữ gìn trật tự nơi thờ tự.",
        },
        sources=[
            {"title": "Cục Du lịch Quốc gia Việt Nam — Đền Bà Triệu", "url": "https://vietnamtourism.vn/index.php/tourism/items/2253"},
            {"title": "Wikipedia (VI) — Đền Bà Triệu", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%81n_B%C3%A0_Tri%E1%BB%87u"},
        ],
        tags=["monument", "temple", "history", "culture", "top"],
    ),
    rec(
        "bien-hai-tien",
        name_vi="Bãi biển Hải Tiến",
        name_ru="Пляж Хайтьен",
        name_en="Hai Tien Beach",
        categories=["other"],
        coordinates={"lat": 19.8339, "lon": 105.9469},
        address_vi="Khu du lịch sinh thái biển Hải Tiến, xã Hoằng Tiến, huyện Hoằng Hóa, tỉnh Thanh Hóa",
        rating={"value": 4.3, "count": 8200, "source": "Google", "as_of": "2026-07"},
        review_summary_vi="Du khách thích bãi cát dài, thoải, nước biển khá trong và không gian còn khá mới, ít xô bồ hơn Sầm Sơn. Nhiều gia đình khen phù hợp cho trẻ nhỏ và hải sản tươi ngon; một số nhận xét dịch vụ vào mùa cao điểm còn quá tải và giá cả cần hỏi trước.",
        presentation_short_vi="Bãi biển Hải Tiến thuộc huyện Hoằng Hóa là khu nghỉ dưỡng biển trẻ trung của xứ Thanh, cách thành phố Thanh Hóa khoảng 17 km. Với hơn chục ki-lô-mét cát vàng, sóng êm và hệ thống khách sạn, khu vui chơi mọc lên nhanh chóng, Hải Tiến ngày càng hút khách gia đình mỗi mùa hè.",
        presentation_short_en="Hai Tien Beach in Hoang Hoa district is Thanh Hoa's youthful seaside resort, about 17 km from the provincial capital. With more than ten kilometres of golden sand, gentle surf and a fast-growing cluster of hotels and amusement areas, it draws ever more family holidaymakers each summer.",
        presentation_short_ru="Пляж Хайтьен в уезде Хоангхоа — молодой морской курорт провинции Тханьхоа, примерно в 17 км от её центра. Более десяти километров золотистого песка, мягкий прибой и быстро растущие отели и зоны развлечений с каждым летом привлекают всё больше семейных отдыхающих.",
        presentation_long_vi="Nằm ven biển huyện Hoằng Hóa, cách trung tâm thành phố Thanh Hóa khoảng 17 km về phía đông, Hải Tiến là một trong những khu du lịch biển phát triển nhanh nhất khu vực Bắc Trung Bộ trong hơn một thập niên qua. Bãi biển trải dài hơn 12 km với dải cát vàng mịn, độ dốc thoải và sóng tương đối êm, thích hợp cho gia đình có trẻ nhỏ tắm biển. So với Sầm Sơn lâu đời và sôi động, Hải Tiến mang không khí trẻ trung, thoáng đãng hơn, với hàng loạt khách sạn, khu nghỉ dưỡng và tổ hợp vui chơi mới được đầu tư dọc đường ven biển. Du khách đến đây có thể tắm biển, chèo thuyền, chơi các trò thể thao dưới nước, hoặc thưởng thức hải sản tươi sống ngay tại các nhà hàng ven bãi với giá phải chăng. Buổi sáng sớm, nhiều người thích ngắm bình minh và xem ngư dân kéo lưới, mua mực, ghẹ, cá vừa cập bến. Khu vực lân cận còn có các điểm gắn với truyền thống như tượng đài Lão dân quân Hoằng Trường từng bắn rơi máy bay Mỹ. Với hạ tầng ngày càng hoàn thiện, Hải Tiến là lựa chọn nghỉ dưỡng biển hấp dẫn, đặc biệt cho các nhóm đông người và gia đình vào mùa hè.",
        presentation_long_en="Stretching along the coast of Hoang Hoa district about 17 km east of Thanh Hoa city, Hai Tien has become one of the fastest-developing beach destinations in Vietnam's North Central Coast over the past decade. The beach runs for more than 12 km with fine golden sand, a gentle slope and relatively calm surf, making it well suited to families with young children. Compared with long-established, bustling Sam Son, Hai Tien feels fresher and more spacious, lined with a wave of newly built hotels, resorts and entertainment complexes along the coastal road. Visitors can swim, kayak, try water sports or feast on fresh seafood at beachfront restaurants at reasonable prices. In the early morning many people enjoy the sunrise and watch fishermen haul in their nets, buying squid, crab and fish straight off the boats. Nearby stand sites tied to local history, including the monument to the elderly Hoang Truong militia who once shot down an American aircraft. With steadily improving infrastructure, Hai Tien is an appealing seaside retreat, especially for large groups and families during the summer season.",
        presentation_long_ru="Протянувшись вдоль побережья уезда Хоангхоа примерно в 17 км к востоку от города Тханьхоа, Хайтьен за последнее десятилетие стал одним из самых быстрорастущих пляжных направлений северо-центрального побережья Вьетнама. Пляж тянется более чем на 12 км: мелкий золотистый песок, пологий вход в воду и сравнительно спокойный прибой делают его удобным для семей с маленькими детьми. По сравнению со старым и шумным Шамшоном Хайтьен ощущается более свежим и просторным; вдоль приморской дороги выстроился ряд новых отелей, курортов и развлекательных комплексов. Гости могут купаться, кататься на каяках, заниматься водными видами спорта или отведать свежие морепродукты в прибрежных ресторанах по умеренным ценам. Ранним утром многие любуются восходом и наблюдают, как рыбаки вытягивают сети, покупая кальмаров, крабов и рыбу прямо с лодок. Поблизости расположены и памятные места, в том числе монумент пожилым ополченцам Хоангчыонга, некогда сбившим американский самолёт. Благодаря постоянно улучшающейся инфраструктуре Хайтьен — привлекательное место морского отдыха, особенно для больших компаний и семей в летний сезон.",
        highlights_vi=[
            "Hơn 12 km bãi cát vàng thoải, sóng êm, phù hợp gia đình có trẻ nhỏ",
            "Khu nghỉ dưỡng biển trẻ, nhiều khách sạn và tổ hợp vui chơi mới ở Hoằng Hóa",
            "Hải sản tươi ngon, ngắm bình minh và cảnh ngư dân kéo lưới buổi sớm",
        ],
        highlights_en=[
            "Over 12 km of gently sloping golden sand with calm surf, ideal for families",
            "A youthful beach resort in Hoang Hoa with many new hotels and fun complexes",
            "Fresh seafood, sunrise views and fishermen hauling in nets at dawn",
        ],
        highlights_ru=[
            "Более 12 км пологого золотистого песка со спокойным прибоем — удобно для семей",
            "Молодой пляжный курорт в Хоангхоа с множеством новых отелей и зон развлечений",
            "Свежие морепродукты, восходы и рыбаки, вытягивающие сети на рассвете",
        ],
        practical={
            "hours_vi": "Bãi biển mở tự do; đẹp nhất khi tắm vào sáng sớm và chiều mát.",
            "ticket_vi": "Tắm biển miễn phí; phí gửi xe, thuê ghế, phao... tùy dịch vụ.",
            "duration_vi": "Nửa ngày đến vài ngày nếu nghỉ dưỡng.",
            "best_time_vi": "Mùa hè, khoảng tháng 4–8; tránh ngày biển động, mưa bão.",
            "tips_vi": "Hỏi giá hải sản và dịch vụ trước khi dùng; đặt phòng sớm vào cao điểm hè; chú ý cờ cảnh báo và khu vực an toàn khi tắm.",
        },
        sources=[
            {"title": "Wikipedia (VI) — Hoằng Hóa", "url": "https://vi.wikipedia.org/wiki/Ho%E1%BA%B1ng_H%C3%B3a"},
        ],
        tags=["beach", "outdoor", "family", "summer", "resort"],
    ),
    rec(
        "ben-en",
        name_vi="Vườn quốc gia Bến En",
        name_ru="Национальный парк Бенен",
        name_en="Ben En National Park",
        categories=["park_garden", "other"],
        coordinates={"lat": 19.6167, "lon": 105.5250},
        address_vi="Huyện Như Thanh và Như Xuân, tỉnh Thanh Hóa (cách TP Thanh Hóa ~46 km)",
        rating={"value": 4.4, "count": 1500, "source": "Google", "as_of": "2026-07"},
        review_summary_vi="Du khách khen cảnh hồ Sông Mực với hàng chục hòn đảo xanh mướt, không khí trong lành, thích hợp đi thuyền và cắm trại. Nhiều người ví như 'Hạ Long trên cạn' của xứ Thanh; một số lưu ý đường vào và dịch vụ còn hoang sơ, nên chuẩn bị trước và đi cùng người quen đường.",
        presentation_short_vi="Vườn quốc gia Bến En thuộc hai huyện Như Thanh và Như Xuân, cách thành phố Thanh Hóa khoảng 46 km. Trung tâm là hồ Sông Mực rộng lớn với 21 hòn đảo, bao quanh bởi rừng nguyên sinh giàu động thực vật, được ví như 'Hạ Long trên cạn' của xứ Thanh.",
        presentation_short_en="Ben En National Park lies in Nhu Thanh and Nhu Xuan districts, about 46 km from Thanh Hoa city. At its heart is the vast Song Muc Lake dotted with 21 islets and ringed by primeval forest rich in wildlife, often called the 'Ha Long Bay on land' of Thanh Hoa.",
        presentation_short_ru="Национальный парк Бенен находится в уездах Нытхань и Нысуан, примерно в 46 км от города Тханьхоа. В его сердце — обширное озеро Шонгмык с 21 островком в окружении первозданного леса, богатого дикой природой; его часто называют 'сухопутной бухтой Халонг' провинции Тханьхоа.",
        presentation_long_vi="Được thành lập năm 1992, Vườn quốc gia Bến En trải rộng trên địa bàn hai huyện Như Thanh và Như Xuân, cách thành phố Thanh Hóa khoảng 46 km về phía tây nam. Với tổng diện tích hơn 14.700 ha, trong đó rừng nguyên sinh chiếm phần lớn, Bến En là kho báu đa dạng sinh học của khu vực với hàng nghìn loài thực vật và động vật, trong đó có nhiều loài quý hiếm như lim xanh cổ thụ, voọc, gấu, và loài gừng đặc hữu mới được phát hiện. Điểm nhấn của vườn là hồ Sông Mực rộng khoảng 3.000 ha, mặt nước mênh mông điểm xuyết 21 hòn đảo và bán đảo phủ rừng xanh, tạo nên khung cảnh sơn thủy hữu tình khiến nhiều người ví như 'Hạ Long trên cạn'. Du khách có thể đi thuyền máy hoặc kayak khám phá lòng hồ, ghé thăm các hang động ở khu vực phía nam và phía bắc, đi bộ theo các tuyến đường mòn xuyên rừng, hoặc nghỉ tại nhà nghỉ nhỏ trên đảo. Trong vùng lõi và vùng đệm còn có cộng đồng các dân tộc Thái, Thổ, Mường sinh sống, giữ nhiều nét văn hóa bản địa đặc sắc. Còn khá hoang sơ và yên tĩnh, Bến En là điểm đến lý tưởng cho những ai yêu thiên nhiên, thích cắm trại, chèo thuyền và trải nghiệm rừng núi xứ Thanh.",
        presentation_long_en="Established in 1992, Ben En National Park spreads across Nhu Thanh and Nhu Xuan districts about 46 km southwest of Thanh Hoa city. Covering more than 14,700 hectares, much of it primeval forest, Ben En is a treasure house of biodiversity with thousands of plant and animal species, including rare ones such as ancient ironwood trees, langurs, bears and a newly discovered endemic ginger. Its centrepiece is Song Muc Lake, some 3,000 hectares of open water sprinkled with 21 forested islands and peninsulas, a mountain-and-water scene so lovely that many liken it to a 'Ha Long Bay on land'. Visitors can explore the lake by motorboat or kayak, visit caves in the southern and northern sections, hike forest trails, or stay in modest lodges on the islands. Within the core and buffer zones live communities of the Thai, Tho and Muong peoples, who preserve many distinctive local traditions. Still relatively wild and quiet, Ben En is an ideal destination for nature lovers who enjoy camping, boating and immersing themselves in the forests and hills of Thanh Hoa, far from crowds and city noise.",
        presentation_long_ru="Основанный в 1992 году, национальный парк Бенен раскинулся в уездах Нытхань и Нысуан примерно в 46 км к юго-западу от города Тханьхоа. На площади более 14 700 гектаров, значительную часть которых занимает девственный лес, Бенен — настоящая сокровищница биоразнообразия с тысячами видов растений и животных, включая редкие: вековые железные деревья, лангуров, медведей и недавно открытый эндемичный имбирь. Его сердце — озеро Шонгмык площадью около 3000 гектаров, гладь которого усеяна 21 покрытым лесом островом и полуостровом; этот пейзаж воды и гор так красив, что многие сравнивают его с 'сухопутной бухтой Халонг'. Гости могут исследовать озеро на моторной лодке или каяке, посетить пещеры в южной и северной частях, пройти лесными тропами или остановиться в скромных домиках на островах. В основной и буферной зонах живут общины народов тхай, тхо и мыонг, сохраняющие немало самобытных традиций. Всё ещё довольно дикий и тихий, Бенен идеально подходит для любителей природы, которым по душе кемпинг, прогулки на лодках и погружение в леса и холмы Тханьхоа вдали от толп и городского шума.",
        highlights_vi=[
            "Hồ Sông Mực rộng ~3.000 ha với 21 hòn đảo — 'Hạ Long trên cạn' xứ Thanh",
            "Rừng nguyên sinh đa dạng sinh học: lim xanh cổ thụ, voọc, gấu, gừng đặc hữu",
            "Đi thuyền, kayak, khám phá hang động và trải nghiệm văn hóa Thái, Thổ, Mường",
        ],
        highlights_en=[
            "Song Muc Lake (~3,000 ha) with 21 islands — Thanh Hoa's 'Ha Long Bay on land'",
            "Biodiverse old-growth forest: ancient ironwood, langurs, bears, endemic ginger",
            "Boating, kayaking, cave exploration and Thai, Tho and Muong cultural encounters",
        ],
        highlights_ru=[
            "Озеро Шонгмык (~3000 га) с 21 островом — 'сухопутная бухта Халонг' Тханьхоа",
            "Биоразнообразный старовозрастный лес: железное дерево, лангуры, медведи, имбирь",
            "Прогулки на лодках и каяках, пещеры и знакомство с культурой тхай, тхо и мыонг",
        ],
        practical={
            "hours_vi": "Ban ngày; nên liên hệ ban quản lý vườn trước để thuê thuyền, hướng dẫn viên và lưu trú.",
            "ticket_vi": "Có phí tham quan và phí thuê thuyền/kayak; mức giá thay đổi, nên hỏi trước.",
            "duration_vi": "Nửa ngày đến 1–2 ngày nếu cắm trại, lưu trú trên đảo.",
            "best_time_vi": "Mùa khô, khoảng tháng 10 đến tháng 4; tránh mùa mưa lũ.",
            "tips_vi": "Chuẩn bị nước, đồ ăn, chống côn trùng; đi cùng người quen đường hoặc hướng dẫn viên; giữ gìn vệ sinh, không xả rác trong rừng.",
        },
        sources=[
            {"title": "Wikipedia (EN) — Ben En National Park", "url": "https://en.wikipedia.org/wiki/B%E1%BA%BFn_En_National_Park"},
            {"title": "Wikipedia (VI) — Vườn quốc gia Bến En", "url": "https://vi.wikipedia.org/wiki/V%C6%B0%E1%BB%9Dn_qu%E1%BB%91c_gia_B%E1%BA%BFn_En"},
        ],
        tags=["nature", "lake", "national-park", "boat", "outdoor", "daytrip"],
    ),
    rec(
        "dong-tu-thuc",
        name_vi="Động Từ Thức",
        name_ru="Пещера Ты Тхык",
        name_en="Tu Thuc Cave",
        categories=["other"],
        coordinates={"lat": 20.0389, "lon": 106.0158},
        address_vi="Xã Nga Thiện, huyện Nga Sơn, tỉnh Thanh Hóa",
        rating={"value": 4.2, "count": 900, "source": "Google", "as_of": "2026-07"},
        review_summary_vi="Du khách thích thú với hệ thống thạch nhũ nhiều hình thù gắn với truyền thuyết Từ Thức gặp tiên, không khí mát lạnh trong hang. Nhiều người thấy hang đẹp và huyền bí; một số lưu ý đường lên hang hơi trơn, đèn chiếu sáng còn hạn chế nên cần cẩn thận và mang đèn pin.",
        presentation_short_vi="Động Từ Thức (còn gọi động Bích Đào) nằm ở xã Nga Thiện, huyện Nga Sơn, gắn với truyền thuyết chàng Từ Thức gặp nàng tiên Giáng Hương. Trong lòng núi đá vôi là hệ thống thạch nhũ kỳ ảo, được người xưa liên tưởng thành kho vàng, kho muối, buồng tắm tiên và đường lên trời.",
        presentation_short_en="Tu Thuc Cave, also called Bich Dao Cave, lies in Nga Thien commune of Nga Son district and is bound to the legend of the scholar Tu Thuc meeting the fairy Giang Huong. Inside the limestone mountain, fantastical stalactites were imagined by earlier generations as treasures of gold and salt, a fairies' bath and a stairway to heaven.",
        presentation_short_ru="Пещера Ты Тхык, также называемая Бичдао, находится в общине Нгатхьен уезда Нгашон и связана с легендой о том, как учёный Ты Тхык встретил фею Зянгхыонг. Внутри известняковой горы фантастические сталактиты в народном воображении превратились в сокровищницы золота и соли, купальню фей и лестницу в небо.",
        presentation_long_vi="Nằm trong dãy núi đá vôi ở xã Nga Thiện, huyện Nga Sơn, cách thành phố Thanh Hóa khoảng 40 km về phía đông bắc, động Từ Thức là một trong những hang động nổi tiếng và giàu chất thơ nhất xứ Thanh. Tên động gắn với truyền thuyết chàng Từ Thức — một vị quan thời Trần treo ấn từ quan — trong lần ngao du đã lạc vào chốn bồng lai và kết duyên cùng nàng tiên Giáng Hương; đến khi trở về quê cũ thì đã qua bao đời người. Câu chuyện tình 'người trần gặp tiên' ấy khiến hang còn được gọi là động Bích Đào và trở thành nguồn cảm hứng cho thơ ca dân gian. Bước vào lòng động, du khách choáng ngợp trước hệ thống thạch nhũ muôn hình vạn trạng, được người xưa đặt tên đầy tưởng tượng: kho vàng, kho muối, buồng tắm của nàng tiên, quả đào tiên, con đường lên trời... Không khí trong hang mát lạnh, ánh sáng mờ ảo càng làm tăng vẻ huyền bí. Danh sĩ Nguyễn Trãi tương truyền từng ghé thăm và đề thơ nơi đây. Ngày nay động Từ Thức là điểm tham quan hấp dẫn kết hợp với các di tích khác của Nga Sơn — vùng đất còn gắn với sự tích Mai An Tiêm và quả dưa hấu.",
        presentation_long_en="Set in a limestone range in Nga Thien commune of Nga Son district, about 40 km northeast of Thanh Hoa city, Tu Thuc Cave is one of the most famous and poetic caverns in the province. Its name recalls the legend of Tu Thuc, a Tran-dynasty mandarin who resigned his post and, while wandering, strayed into a fairyland where he married the fairy Giang Huong; when at last he returned home, generations of humans had passed. This tale of a mortal meeting an immortal also gives the cave its alternative name, Bich Dao, and has long inspired folk poetry. Stepping inside, visitors are struck by an array of stalactites in countless shapes that earlier generations named with great imagination: a hoard of gold, a store of salt, the fairy's bathing chamber, an immortal peach, a road to heaven. The air within is cool and the dim light heightens the sense of mystery. The scholar Nguyen Trai is said to have visited and composed verse here. Today Tu Thuc Cave is a rewarding stop combined with other sites in Nga Son, a land also linked to the legend of Mai An Tiem and the watermelon.",
        presentation_long_ru="Расположенная в известняковом хребте общины Нгатхьен уезда Нгашон, примерно в 40 км к северо-востоку от города Тханьхоа, пещера Ты Тхык — одна из самых знаменитых и поэтичных пещер провинции. Её название хранит легенду о Ты Тхыке, чиновнике эпохи Чан, который оставил службу и во время странствий забрёл в волшебную страну, где женился на фее Зянгхыонг; когда же он наконец вернулся домой, на земле сменилось несколько поколений. Этот рассказ о встрече смертного с бессмертной дал пещере и второе имя — Бичдао — и издавна вдохновлял народную поэзию. Войдя внутрь, гости поражаются множеству сталактитов самых причудливых форм, которым предки дали образные имена: клад золота, склад соли, купальня феи, персик бессмертия, дорога в небо. Воздух в пещере прохладен, а тусклый свет усиливает ощущение тайны. Считается, что здесь побывал и оставил стихи учёный Нгуен Чай. Сегодня пещера Ты Тхык — интересное место для посещения вместе с другими достопримечательностями Нгашона, края, связанного также с легендой о Май Ан Тьеме и арбузе.",
        highlights_vi=[
            "Gắn với truyền thuyết Từ Thức gặp tiên Giáng Hương (còn gọi động Bích Đào)",
            "Thạch nhũ hình kho vàng, kho muối, buồng tắm tiên, đường lên trời",
            "Không khí mát lạnh, huyền bí; tương truyền Nguyễn Trãi từng đề thơ",
        ],
        highlights_en=[
            "Tied to the legend of Tu Thuc meeting the fairy Giang Huong (also 'Bich Dao Cave')",
            "Stalactites shaped like gold hoards, salt stores, a fairy's bath and a road to heaven",
            "Cool, mysterious air; the scholar Nguyen Trai is said to have written verse here",
        ],
        highlights_ru=[
            "Связана с легендой о встрече Ты Тхыка с феей Зянгхыонг (пещера Бичдао)",
            "Сталактиты в виде кладов золота и соли, купальни феи и дороги в небо",
            "Прохладный, таинственный воздух; считается, здесь оставил стихи Нгуен Чай",
        ],
        practical={
            "hours_vi": "Ban ngày; nên đi vào buổi sáng để đủ ánh sáng leo núi vào cửa động.",
            "ticket_vi": "Vé tham quan mức thấp; có thể thuê người dẫn đường địa phương.",
            "duration_vi": "Khoảng 1–2 giờ.",
            "best_time_vi": "Mùa khô, trời tạnh ráo để đường lên hang bớt trơn.",
            "tips_vi": "Mang giày bám tốt và đèn pin; cẩn thận bậc đá trơn; kết hợp thăm các điểm khác ở Nga Sơn.",
        },
        sources=[
            {"title": "VnExpress — Từ Thức, hang động bậc nhất xứ Thanh", "url": "https://vnexpress.net/tu-thuc-hang-dong-bac-nhat-xu-thanh-4615010.html"},
            {"title": "Wikipedia (EN) — Nga Sơn district", "url": "https://en.wikipedia.org/wiki/Nga_S%C6%A1n_district"},
        ],
        tags=["cave", "legend", "nature", "culture"],
    ),
    rec(
        "thac-may",
        name_vi="Thác Mây",
        name_ru="Водопад Май",
        name_en="May Waterfall",
        categories=["park_garden", "other"],
        coordinates={"lat": 20.2030, "lon": 105.5990},
        address_vi="Thôn Đăng Thượng, xã Thạch Lâm, huyện Thạch Thành, tỉnh Thanh Hóa",
        rating={"value": 4.4, "count": 1300, "source": "Google", "as_of": "2026-07"},
        review_summary_vi="Du khách thích dòng thác nhiều tầng, nước trong mát, tắm và chụp ảnh đẹp giữa khung cảnh núi rừng nguyên sơ. Nhiều người khen không khí trong lành, người dân thân thiện; một số lưu ý cuối tuần khá đông, đá trơn nên cẩn thận và nên đi mùa nước vừa phải.",
        presentation_short_vi="Thác Mây nằm ở xã Thạch Lâm, huyện Thạch Thành, còn được gọi là thác '9 bậc tình yêu' với chín tầng nước đổ nối tiếp giữa rừng núi. Dòng nước trong mát, cảnh quan nguyên sơ và không khí trong lành khiến nơi đây thành điểm tắm thác, cắm trại được yêu thích ở phía bắc xứ Thanh.",
        presentation_short_en="May Waterfall in Thach Lam commune, Thach Thanh district, is nicknamed the 'nine steps of love' for its nine successive tiers cascading through forested hills. Clear cool water, unspoilt scenery and fresh air make it a much-loved spot for waterfall bathing and camping in northern Thanh Hoa.",
        presentation_short_ru="Водопад Май в общине Тхаклам уезда Тхактхань прозван 'девятью ступенями любви' за девять последовательных каскадов, ниспадающих среди лесистых холмов. Чистая прохладная вода, нетронутые пейзажи и свежий воздух сделали его любимым местом купания у водопада и кемпинга на севере Тханьхоа.",
        presentation_long_vi="Ẩn mình giữa vùng núi rừng huyện Thạch Thành, cách thành phố Thanh Hóa khoảng 100 km về phía tây bắc, Thác Mây là một trong những thác nước đẹp và còn nguyên sơ nhất xứ Thanh. Dòng thác bắt nguồn từ đỉnh núi Thạch Lâm, đổ xuống theo chín bậc nối tiếp nhau nên người dân gọi là thác 'chín bậc tình yêu'; theo lời kể, mỗi bậc gắn với một truyền thuyết về đôi trai gái và các nàng tiên xuống trần tắm mát. Nước thác trong xanh, mát lạnh quanh năm, len qua những phiến đá lớn tạo thành nhiều hồ tắm tự nhiên nông sâu khác nhau, phù hợp cho cả người lớn và trẻ em vui chơi. Xung quanh là rừng cây rậm rạp, tiếng chim và tiếng nước reo tạo nên khung cảnh yên bình, tách biệt phố thị. Nơi đây gắn với đời sống của đồng bào Mường bản địa; du khách có thể kết hợp thưởng thức ẩm thực dân tộc như cơm lam, gà đồi, cá suối, và tìm hiểu nếp sinh hoạt của bản làng. Vài năm gần đây Thác Mây được đầu tư đường sá, dịch vụ homestay, cắm trại nên ngày càng thu hút giới trẻ và các gia đình vào dịp hè, cuối tuần. Đây là lựa chọn lý tưởng cho những ai muốn hòa mình vào thiên nhiên và tận hưởng làn nước mát trong ngày nắng nóng.",
        presentation_long_en="Hidden among the forested hills of Thach Thanh district about 100 km northwest of Thanh Hoa city, May Waterfall is one of the loveliest and most unspoilt cascades in the province. Rising from the top of Thach Lam mountain, the stream tumbles down nine successive tiers, which is why locals call it the waterfall of the 'nine steps of love'; by tradition each tier carries a legend of young lovers and fairies descending to bathe. The water is clear and cool year-round, threading between large boulders to form natural pools of varying depth that suit both adults and children. All around, dense forest, birdsong and the rush of water create a peaceful scene far from the city. The site is bound to the life of the local Muong people, and visitors can pair a trip with ethnic dishes such as bamboo-tube rice, hill chicken and stream fish while learning about village customs. In recent years improved roads, homestays and camping services have made May Waterfall increasingly popular with young people and families in summer and at weekends. It is an ideal choice for anyone wishing to immerse themselves in nature and enjoy the cool water on a hot day.",
        presentation_long_ru="Скрытый среди лесистых холмов уезда Тхактхань примерно в 100 км к северо-западу от города Тханьхоа, водопад Май — один из самых красивых и нетронутых каскадов провинции. Беря начало на вершине горы Тхаклам, поток спускается девятью последовательными ступенями, отчего местные жители называют его водопадом 'девяти ступеней любви'; по преданию, каждая ступень связана с легендой о влюблённых и феях, спускавшихся купаться. Вода чиста и прохладна круглый год; пробиваясь между крупными валунами, она образует природные купальни разной глубины, подходящие и взрослым, и детям. Вокруг густой лес, пение птиц и шум воды создают умиротворённую картину вдали от города. Это место связано с жизнью местного народа мыонг, и гости могут дополнить поездку национальными блюдами — рисом в бамбуке, горной курицей, речной рыбой — и знакомством с деревенскими обычаями. В последние годы благодаря дорогам, гостевым домам и услугам кемпинга водопад Май становится всё популярнее у молодёжи и семей летом и в выходные. Это идеальный выбор для тех, кто хочет слиться с природой и насладиться прохладной водой в жаркий день.",
        highlights_vi=[
            "Thác chín tầng nối tiếp — được gọi là thác 'chín bậc tình yêu'",
            "Nước trong mát quanh năm với nhiều hồ tắm tự nhiên giữa rừng nguyên sơ",
            "Gắn với văn hóa Mường: cơm lam, gà đồi, homestay và cắm trại",
        ],
        highlights_en=[
            "A nine-tier cascade known as the waterfall of the 'nine steps of love'",
            "Clear, cool water year-round with natural pools amid unspoilt forest",
            "Muong culture nearby: bamboo-tube rice, hill chicken, homestays and camping",
        ],
        highlights_ru=[
            "Девятиступенчатый каскад — 'водопад девяти ступеней любви'",
            "Чистая прохладная вода круглый год и природные купальни среди леса",
            "Рядом культура мыонг: рис в бамбуке, горная курица, гостевые дома, кемпинг",
        ],
        practical={
            "hours_vi": "Ban ngày; nên đến buổi sáng đến đầu chiều để có thời gian tắm thác.",
            "ticket_vi": "Vé vào cửa mức thấp; phí gửi xe, dịch vụ homestay tính riêng.",
            "duration_vi": "Nửa ngày; ở lại 1 đêm nếu cắm trại/homestay.",
            "best_time_vi": "Mùa hè (tháng 4–8) để tắm mát; tránh ngày mưa lớn vì nước xiết.",
            "tips_vi": "Đi giày chống trượt, cẩn thận đá trơn; theo dõi mực nước, không tắm khi nước đục dâng nhanh; mang theo đồ ăn và túi đựng rác.",
        },
        sources=[
            {"title": "Wikipedia (VI) — Thạch Thành", "url": "https://vi.wikipedia.org/wiki/Th%E1%BA%A1ch_Th%C3%A0nh"},
        ],
        tags=["waterfall", "nature", "outdoor", "summer", "family"],
    ),
]

if __name__ == "__main__":
    d = json.load(open(F, encoding="utf-8")) if os.path.exists(F) else []
    have = {p["slug"] for p in d}
    added = [p for p in new if p["slug"] not in have]
    d += added
    json.dump(d, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Thêm mới:", len(added), "-> tổng cộng:", len(d))
    for p in added:
        print("  +", p["slug"], "|", p["name_vi"])
