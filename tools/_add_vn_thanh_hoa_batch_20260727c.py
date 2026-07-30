# -*- coding: utf-8 -*-
"""Thanh Hóa — batch C (records 5-11)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.normpath(os.path.join(HERE, "..", "data", "regions", "vn-thanh-hoa.json"))
REG, RNV, FD, TODAY = "vn-thanh-hoa", "Thanh Hóa", "Miền Trung", "2026-07-27"


def R(slug, nv, ne, nr, cats, lat, lon, addr, rval, rcount, review,
      psv, pse, psr, plv, ple, plr, hlv, hle, hlr, practical, tags, sources=None):
    return {
        "id": f"{REG}-{slug}", "slug": slug, "region": REG, "country": "vietnam",
        "region_name_vi": RNV, "federal_district": FD,
        "name_vi": nv, "name_ru": nr, "name_en": ne,
        "categories": cats, "coordinates": {"lat": lat, "lon": lon},
        "address_vi": addr,
        "rating": {"value": rval, "count": rcount, "source": "Google", "as_of": "2026-07"},
        "review_summary_vi": review,
        "presentation_short_vi": psv, "presentation_short_en": pse, "presentation_short_ru": psr,
        "presentation_long_vi": plv, "presentation_long_en": ple, "presentation_long_ru": plr,
        "highlights_vi": hlv, "highlights_en": hle, "highlights_ru": hlr,
        "practical": practical, "photo": None, "photo_credit": None,
        "official_site": None, "sources": sources or [],
        "tags": tags, "status": "enriched", "last_updated": TODAY,
    }


new = []

# 5) Động Từ Thức
new.append(R(
    "dong-tu-thuc", "Động Từ Thức (Động Bích Đào)", "Tu Thuc Cave (Bich Dao Cave)", "Пещера Ты Тхык (Битьдао)",
    ["other", "park_garden"], 20.0470, 106.0080,
    "Xã Nga Thiện, huyện Nga Sơn, tỉnh Thanh Hóa",
    4.3, 600,
    "Du khách thích thú với các khối nhũ đá hình kho tiền, kho muối, buồng tắm tiên gắn với truyền thuyết Từ Thức gặp tiên. Nhiều người khen hang mát và huyền ảo; một số nhắc lối vào hơi trơn, nên mang đèn.",
    "Động Từ Thức ở huyện Nga Sơn gắn với truyền thuyết chàng Từ Thức lạc vào cõi tiên và gặp nàng Giáng Hương. Hang đá vôi nhiều tầng với nhũ đá kỳ ảo được ví như \"động tiên\", là danh thắng nổi tiếng của xứ Thanh.",
    "Tu Thuc Cave in Nga Son district is linked to the legend of Tu Thuc, who wandered into a fairyland and met the fairy Giang Huong. This multi-level limestone cave with fantastical stalactites is likened to a \"fairy grotto\" and is a famous scenic site of Thanh Hoa.",
    "Пещера Ты Тхык в уезде Нгашон связана с легендой о Ты Тхыке, забредшем в страну фей и встретившем фею Зянг Хыонг. Эта многоуровневая известняковая пещера с причудливыми сталактитами прозвана «пещерой фей» и является знаменитой достопримечательностью Тханьхоа.",
    "Động Từ Thức, còn gọi là động Bích Đào, nằm trong lòng núi đá vôi ở xã Nga Thiện, huyện Nga Sơn, phía đông bắc tỉnh Thanh Hóa. Hang gắn liền với thiên tình sử nổi tiếng: chàng Từ Thức thời Trần vì cởi áo chuộc lỗi cho một cô gái mà kết duyên, rồi theo nàng Giáng Hương lạc vào chốn bồng lai; khi trở về quê thì đã qua bao đời người. Bước vào động, du khách men theo những bậc đá để khám phá hệ thống hang nhiều ngăn với vô số nhũ đá và măng đá đủ hình thù, được dân gian đặt tên đầy tưởng tượng như kho tiền, kho muối, quả đào tiên, buồng tắm của nàng tiên, đôi chim thần… Ánh sáng lọt qua các khe hang khiến nhũ đá lấp lánh, tạo cảm giác lạc vào cõi thần tiên đúng như tên gọi. Xưa kia, danh sĩ như Lê Quý Đôn từng đến vãn cảnh và đề thơ trên vách đá. Động Từ Thức đã được công nhận là danh lam thắng cảnh cấp quốc gia. Kết hợp với vùng chiếu cói Nga Sơn và cửa biển Thần Phù gần đó, nơi đây là điểm tham quan hấp dẫn cho những ai yêu thích truyền thuyết và cảnh quan hang động.",
    "Tu Thuc Cave, also called Bich Dao Cave, lies within a limestone mountain in Nga Thien commune, Nga Son district, in the north-east of Thanh Hoa province. It is bound to a famous love legend: in the Tran dynasty, the scholar Tu Thuc gave up his coat to free a girl, later followed the fairy Giang Huong into a paradise, and on returning home found generations had passed. Entering the cave, visitors follow stone steps through a maze of chambers filled with stalactites and stalagmites of every shape, given imaginative folk names such as the money store, the salt store, the immortal peach, the fairy's bathing chamber and the pair of magic birds. Light filtering through crevices makes the formations glitter, giving the sense of stepping into a fairy realm just as the name suggests. In centuries past, scholars such as Le Quy Don came to admire the scenery and inscribed poems on the rock. Tu Thuc Cave is recognised as a national scenic landmark. Combined with the sedge-mat region of Nga Son and the nearby Than Phu estuary, it is an appealing destination for lovers of legend and cave scenery.",
    "Пещера Ты Тхык, называемая также Битьдао, находится в известняковой горе в общине Нгатхьен уезда Нгашон на северо-востоке провинции Тханьхоа. Она связана со знаменитой любовной легендой: при династии Чан учёный Ты Тхык отдал свой кафтан, чтобы освободить девушку, позже последовал за феей Зянг Хыонг в райскую страну, а вернувшись домой, обнаружил, что сменились поколения. Войдя в пещеру, посетители по каменным ступеням проходят лабиринт залов, полных сталактитов и сталагмитов всевозможных форм, которым народ дал образные названия: хранилище денег, хранилище соли, персик бессмертия, купальня феи, пара волшебных птиц. Свет, проникающий сквозь расщелины, заставляет натёки сверкать, создавая ощущение, будто ступаешь в страну фей, как и подсказывает название. В прошлые века учёные, такие как Ле Куи Дон, приезжали любоваться пейзажем и высекали стихи на камне. Пещера Ты Тхык признана национальным живописным памятником. Вместе с районом циновок из осоки Нгашон и близлежащим устьем Тханьфу это привлекательное место для любителей легенд и пещерных пейзажей.",
    ["Gắn với truyền thuyết Từ Thức gặp tiên Giáng Hương", "Hang đá vôi nhiều tầng, nhũ đá kỳ ảo", "Danh lam thắng cảnh cấp quốc gia ở Nga Sơn"],
    ["Tied to the legend of Tu Thuc and the fairy Giang Huong", "Multi-level limestone cave with fantastical stalactites", "National scenic landmark in Nga Son"],
    ["Связана с легендой о Ты Тхыке и фее Зянг Хыонг", "Многоуровневая известняковая пещера с причудливыми натёками", "Национальный живописный памятник в Нгашоне"],
    {"hours_vi": "Khoảng 7:00–17:00 hằng ngày.", "ticket_vi": "Vé tham quan khoảng 20.000–30.000 VND/người.",
     "duration_vi": "Khoảng 1 giờ.", "best_time_vi": "Mùa khô (tháng 10–4); nên đi buổi sáng.",
     "tips_vi": "Mang đèn pin, đi giày bám tốt vì lối trong hang trơn; kết hợp cửa Thần Phù, làng chiếu cói Nga Sơn."},
    ["cave", "legend", "nature", "outdoor"],
    [{"title": "Wikipedia (VI) — Động Từ Thức", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%99ng_T%E1%BB%AB_Th%E1%BB%A9c"}],
))

# 6) Đền Nưa – Am Tiên
new.append(R(
    "den-nua-am-tien", "Đền Nưa – Am Tiên (Ngàn Nưa)", "Nua Temple – Am Tien", "Храм Ныа — Ам Тьен",
    ["church", "park_garden"], 19.6083, 105.6300,
    "Đỉnh núi Nưa, xã Tân Ninh, huyện Triệu Sơn, tỉnh Thanh Hóa",
    4.5, 1500,
    "Du khách ấn tượng với huyệt đạo thiêng trên đỉnh Ngàn Nưa và giếng Tiên quanh năm không cạn. Nhiều người lên xin lộc dịp \"mở cổng trời\" mùng 9 Tết; một số nhắc đường lên núi quanh co, nên đi xe chắc.",
    "Đền Nưa – Am Tiên nằm trên đỉnh Ngàn Nưa cao khoảng 585 m, gắn với căn cứ khởi nghĩa của Bà Triệu. Nơi đây có huyệt đạo được xem là một trong ba huyệt đạo linh thiêng nhất Việt Nam, nổi tiếng với lễ \"mở cổng trời\" đầu năm.",
    "Nua Temple – Am Tien sits atop Ngan Nua mountain, about 585 m high, linked to Lady Trieu's uprising base. It holds an energy point regarded as one of Vietnam's three most sacred, famed for the \"opening of Heaven's gate\" ceremony at the start of the year.",
    "Храм Ныа — Ам Тьен расположен на вершине горы Нган Ныа высотой около 585 м и связан с базой восстания госпожи Чьеу. Здесь находится «энергетическая точка», считающаяся одной из трёх самых священных во Вьетнаме, и знаменит обряд «открытия небесных врат» в начале года.",
    "Quần thể Đền Nưa – Am Tiên tọa lạc trên đỉnh Ngàn Nưa, dãy núi cao khoảng 585 m ở huyện Triệu Sơn, phía tây nam tỉnh Thanh Hóa. Đây từng là căn cứ địa của cuộc khởi nghĩa Bà Triệu năm 248, nay là điểm du lịch tâm linh nổi tiếng bậc nhất xứ Thanh. Trên đỉnh núi có đền Am Tiên thờ Bà Triệu cùng các vị thần, giếng Tiên với dòng nước trong mát quanh năm không cạn, bàn cờ tiên và đặc biệt là \"huyệt đạo\" – nơi được giới phong thủy đánh giá là một trong ba huyệt khí thiêng của nước Việt, bên cạnh núi Đá Chông (Ba Vì) và núi Bà Đen (Tây Ninh). Người dân tin rằng đứng nơi huyệt đạo có thể cảm nhận nguồn sinh khí đặc biệt của đất trời. Vào ngày mùng 9 tháng Giêng âm lịch, lễ hội \"mở cổng trời\" thu hút hàng vạn người hành hương lên núi cầu tài lộc, bình an cho năm mới. Đường lên đỉnh nay đã thuận tiện hơn, du khách vừa vãn cảnh núi rừng, phóng tầm mắt xuống đồng bằng, vừa chiêm bái chốn linh thiêng gắn với khí phách nữ tướng họ Triệu.",
    "The Nua Temple – Am Tien complex crowns Ngan Nua, a range about 585 m high in Trieu Son district, south-west of Thanh Hoa province. It was once a base of Lady Trieu's uprising of 248 AD and is now one of the region's most famous spiritual destinations. On the summit stand Am Tien Temple, dedicated to Lady Trieu and other deities; the Fairy Well, whose cool clear water never dries; a fairy chessboard; and above all the \"energy point\" that geomancers rank among the three most sacred in Vietnam, alongside Da Chong Mountain (Ba Vi) and Ba Den Mountain (Tay Ninh). Locals believe that standing at this point one can feel a special vital energy of heaven and earth. On the 9th day of the first lunar month, the \"opening of Heaven's gate\" festival draws tens of thousands of pilgrims up the mountain to pray for fortune and peace in the new year. The road to the top is now easier; visitors can enjoy the mountain scenery, gaze down over the plain and pay homage at a sacred site bound to the spirit of the heroine of the Trieu family.",
    "Комплекс Храм Ныа — Ам Тьен венчает гору Нган Ныа высотой около 585 м в уезде Чьеушон на юго-западе провинции Тханьхоа. Некогда он был базой восстания госпожи Чьеу 248 года, а ныне — одно из самых знаменитых духовных мест края. На вершине стоят храм Ам Тьен, посвящённый госпоже Чьеу и другим божествам; Колодец фей с прохладной чистой водой, что не иссякает; «шахматная доска фей»; и, главное, «энергетическая точка», которую геоманты относят к трём самым священным во Вьетнаме, наряду с горой Дачонг (Бави) и горой Бадэн (Тэйнинь). Местные верят, что, стоя в этой точке, можно ощутить особую жизненную энергию неба и земли. На 9-й день первого лунного месяца праздник «открытия небесных врат» привлекает на гору десятки тысяч паломников, молящихся об удаче и мире в новом году. Дорога наверх теперь удобнее; посетители любуются горными пейзажами, смотрят вниз на равнину и поклоняются священному месту, связанному с духом героини из рода Чьеу.",
    ["Huyệt đạo được coi là 1 trong 3 huyệt thiêng nhất Việt Nam", "Căn cứ khởi nghĩa Bà Triệu trên đỉnh Ngàn Nưa", "Lễ \"mở cổng trời\" mùng 9 tháng Giêng"],
    ["An energy point ranked among Vietnam's three most sacred", "Lady Trieu's uprising base atop Ngan Nua", "The \"opening of Heaven's gate\" festival on the 9th of the first lunar month"],
    ["«Энергетическая точка», одна из трёх священнейших во Вьетнаме", "База восстания госпожи Чьеу на вершине Нган Ныа", "Праздник «открытия небесных врат» 9-го числа первого лунного месяца"],
    {"hours_vi": "Khoảng 6:30–18:00 hằng ngày.", "ticket_vi": "Vào cửa tự do; có phí gửi/di chuyển xe lên núi.",
     "duration_vi": "Khoảng 1,5–2 giờ.", "best_time_vi": "Đầu xuân, đặc biệt mùng 9 tháng Giêng.",
     "tips_vi": "Đi xe số/xe chắc lên dốc; mang nước; ngày lễ rất đông nên đi sớm."},
    ["spiritual", "mountain", "temple", "top", "outdoor"],
    [{"title": "Cổng TTĐT huyện Triệu Sơn — Núi Nưa – Đền Nưa – Am Tiên", "url": "http://trieuson.gov.vn/"}],
))

# 7) Vườn quốc gia Bến En
new.append(R(
    "vqg-ben-en", "Vườn quốc gia Bến En", "Ben En National Park", "Национальный парк Бенен",
    ["park_garden"], 19.6260, 105.5230,
    "Huyện Như Thanh và huyện Như Xuân, tỉnh Thanh Hóa",
    4.5, 800,
    "Du khách mê hồ Sông Mực xanh biếc điểm xuyết 21 hòn đảo, ví như \"Hạ Long trên núi\". Nhiều người thích đi thuyền, cắm trại giữa rừng nguyên sinh; một số lưu ý dịch vụ còn khá hoang sơ.",
    "Vườn quốc gia Bến En ở huyện Như Thanh có hồ Sông Mực rộng lớn với 21 hòn đảo nổi giữa rừng nguyên sinh. Cảnh sắc non nước hữu tình khiến nơi đây được ví như \"vịnh Hạ Long trên núi\" của xứ Thanh.",
    "Ben En National Park in Nhu Thanh district features the vast Song Muc Lake dotted with 21 islands amid primeval forest. Its harmonious mountains and water have earned it the nickname \"Ha Long Bay on the mountains\" of Thanh Hoa.",
    "Национальный парк Бенен в уезде Нытхань славится обширным озером Шонгмык с 21 островом среди девственного леса. Гармония гор и воды принесла ему прозвище «бухта Халонг в горах» провинции Тханьхоа.",
    "Vườn quốc gia Bến En được thành lập năm 1992, trải rộng trên địa bàn hai huyện Như Thanh và Như Xuân, cách thành phố Thanh Hóa khoảng 36 km về phía tây nam. Trung tâm của vườn là hồ Sông Mực (hồ Bến En) rộng khoảng 3.000 ha, mặt nước xanh biếc ôm lấy 21 hòn đảo và bán đảo lớn nhỏ phủ đầy cây xanh, tạo nên khung cảnh non nước thơ mộng khiến nhiều người ví là \"vịnh Hạ Long trên núi\". Vườn có hệ sinh thái rừng nhiệt đới phong phú với hàng nghìn loài thực vật, nhiều cây lim, lát cổ thụ hàng trăm năm tuổi, cùng các loài thú quý như voọc, khỉ, gấu và nhiều loài chim, bò sát. Du khách có thể thuê thuyền dạo hồ, len lỏi qua các đảo, câu cá, cắm trại, đi bộ xuyên rừng khám phá hang động và thác nước, hoặc ghé thăm bản làng của người Thái, người Mường để tìm hiểu văn hóa bản địa. Không khí trong lành, mát mẻ quanh năm cùng cảnh quan hoang sơ khiến Bến En trở thành điểm đến lý tưởng cho du lịch sinh thái, nghỉ dưỡng và trải nghiệm thiên nhiên ở xứ Thanh.",
    "Ben En National Park, established in 1992, spreads across Nhu Thanh and Nhu Xuan districts, about 36 km south-west of Thanh Hoa city. At its heart lies Song Muc Lake (Ben En Lake), roughly 3,000 ha of jade-green water embracing 21 large and small islands and peninsulas cloaked in greenery — scenery so poetic that many liken it to \"Ha Long Bay on the mountains\". The park holds a rich tropical forest ecosystem with thousands of plant species, including centuries-old ironwood and lat trees, and rare animals such as langurs, monkeys, bears and many birds and reptiles. Visitors can hire boats to cruise the lake and weave among the islands, fish, camp, trek through the forest to explore caves and waterfalls, or visit Thai and Muong villages to learn about local culture. The fresh, cool air year-round and the pristine landscape make Ben En an ideal destination for eco-tourism, retreats and nature experiences in Thanh Hoa.",
    "Национальный парк Бенен, основанный в 1992 году, раскинулся на территории уездов Нытхань и Нысуан, примерно в 36 км к юго-западу от города Тханьхоа. В его сердце — озеро Шонгмык (озеро Бенен) площадью около 3000 га с нефритово-зелёной водой, обнимающей 21 крупный и малый остров и полуостров, укрытые зеленью; пейзаж настолько поэтичен, что многие сравнивают его с «бухтой Халонг в горах». В парке богатая экосистема тропического леса с тысячами видов растений, включая столетние деревья лим и лат, и редкими животными — лангурами, обезьянами, медведями, множеством птиц и рептилий. Посетители могут арендовать лодки, чтобы плыть по озеру и пробираться между островами, рыбачить, ставить палатки, ходить по лесу к пещерам и водопадам или посещать деревни народов тай и мыонг, знакомясь с местной культурой. Круглый год свежий прохладный воздух и нетронутый ландшафт делают Бенен идеальным местом для экотуризма, отдыха и общения с природой в Тханьхоа.",
    ["Hồ Sông Mực với 21 hòn đảo – \"Hạ Long trên núi\"", "Rừng nguyên sinh nhiệt đới đa dạng sinh học", "Đi thuyền, cắm trại, khám phá bản làng Thái – Mường"],
    ["Song Muc Lake with 21 islands – \"Ha Long on the mountains\"", "Biodiverse primeval tropical forest", "Boating, camping and exploring Thai–Muong villages"],
    ["Озеро Шонгмык с 21 островом — «Халонг в горах»", "Биоразнообразный девственный тропический лес", "Лодки, кемпинг и знакомство с деревнями тай и мыонг"],
    {"hours_vi": "Khoảng 7:00–17:00 hằng ngày.", "ticket_vi": "Vé tham quan và thuê thuyền theo bảng giá của vườn.",
     "duration_vi": "Nửa ngày đến 1 ngày.", "best_time_vi": "Mùa khô (tháng 11–4); tránh mùa mưa bão.",
     "tips_vi": "Đặt thuyền/hướng dẫn viên trước; mang đồ chống muỗi; có thể lưu trú qua đêm để ngắm bình minh trên hồ."},
    ["nature", "national-park", "lake", "eco", "outdoor"],
    [{"title": "Wikipedia (VI) — Vườn quốc gia Bến En", "url": "https://vi.wikipedia.org/wiki/V%C6%B0%E1%BB%9Dn_qu%E1%BB%91c_gia_B%E1%BA%BFn_En"}],
))

# 8) Thác Mây
new.append(R(
    "thac-may", "Thác Mây (9 bậc tình yêu)", "May Waterfall (Nine Steps of Love)", "Водопад Май",
    ["park_garden", "other"], 20.3300, 105.4550,
    "Thôn Đăng Thượng, xã Thạch Lâm, huyện Thạch Thành, tỉnh Thanh Hóa",
    4.4, 700,
    "Du khách thích tắm mát dưới dòng thác trắng xóa chảy qua chín bậc đá giữa rừng núi. Nhiều người khen nước trong, cảnh đẹp; một số nhắc cuối tuần hè khá đông và đường tới hơi xa.",
    "Thác Mây ở xã Thạch Lâm, huyện Thạch Thành đổ xuống qua chín bậc nối tiếp nên được gọi là \"9 bậc tình yêu\". Dòng thác trắng xóa giữa núi rừng nguyên sơ là điểm check-in và tắm thác được yêu thích ở miền tây xứ Thanh.",
    "May Waterfall in Thach Lam commune, Thach Thanh district, cascades over nine successive steps, earning it the name \"Nine Steps of Love\". Its white torrent amid pristine mountains is a favourite spot for photos and bathing in western Thanh Hoa.",
    "Водопад Май в общине Тхаклам уезда Тхактхань спадает по девяти последовательным ступеням, за что и назван «Девятью ступенями любви». Его белый поток среди нетронутых гор — любимое место для фото и купания на западе Тханьхоа.",
    "Thác Mây nằm ở thôn Đăng Thượng, xã Thạch Lâm, huyện Thạch Thành, thuộc vùng núi phía bắc tỉnh Thanh Hóa, cách thành phố Thanh Hóa khoảng 100 km. Con thác bắt nguồn từ đỉnh núi Thạch Lâm, chảy dài chừng 100 m qua chín bậc đá vôi nối tiếp nhau, mỗi bậc là một tầng nước tung bọt trắng xóa. Người dân địa phương gọi những bậc thác này là \"9 bậc tình yêu\", ví hành trình leo thác như những cung bậc cảm xúc của tình yêu. Nước thác trong vắt, mát lạnh quanh năm, chảy qua các bồn đá tự nhiên tạo thành những vũng tắm lý tưởng giữa khung cảnh rừng núi nguyên sơ, cây cối xanh mát. Đến đây, du khách có thể ngâm mình dưới làn nước mát, leo dọc các bậc thác, chụp ảnh, cắm trại và thưởng thức đặc sản của người Mường bản địa như cơm lam, gà đồi, cá suối nướng. Vài năm gần đây, thác Mây được đầu tư thành điểm du lịch cộng đồng, có dịch vụ homestay, hàng quán, thu hút đông đảo bạn trẻ và các gia đình vào dịp hè. Đây là một trong những thác nước đẹp và hoang sơ nhất xứ Thanh.",
    "May Waterfall lies in Dang Thuong hamlet, Thach Lam commune, Thach Thanh district, in the northern mountains of Thanh Hoa province, about 100 km from Thanh Hoa city. Rising from the peak of Thach Lam mountain, it tumbles some 100 m over nine successive limestone steps, each a tier of white, foaming water. Locals call these steps the \"Nine Steps of Love\", likening the climb to the shifting emotions of romance. The water is crystal-clear and cool year-round, flowing through natural stone basins that form ideal bathing pools amid pristine forested scenery. Here visitors can soak in the cool current, climb along the steps, take photos, camp and enjoy local Muong specialities such as bamboo-tube rice, hill chicken and grilled stream fish. In recent years May Waterfall has been developed into a community-tourism site with homestays and eateries, drawing many young people and families in summer. It is one of the most beautiful and unspoiled waterfalls in Thanh Hoa.",
    "Водопад Май находится в деревушке Дангтхыонг общины Тхаклам уезда Тхактхань, в северных горах провинции Тханьхоа, примерно в 100 км от города Тханьхоа. Беря начало на вершине горы Тхаклам, он спадает почти на 100 м по девяти последовательным известняковым ступеням, каждая из которых — ярус белой пенящейся воды. Местные называют эти ступени «Девятью ступенями любви», сравнивая подъём с переменчивыми чувствами влюблённых. Вода кристально чистая и прохладная круглый год, стекает через природные каменные чаши, образующие идеальные купальни среди нетронутого лесного пейзажа. Здесь посетители могут окунуться в прохладный поток, взбираться по ступеням, фотографироваться, ставить палатки и пробовать местные блюда народа мыонг — рис в бамбуке, горную курицу и жареную речную рыбу. В последние годы водопад Май превратили в объект общинного туризма с гостевыми домами и кафе, привлекающий летом множество молодёжи и семей. Это один из самых красивых и первозданных водопадов Тханьхоа.",
    ["Thác chín bậc – \"9 bậc tình yêu\"", "Nước trong mát, nhiều vũng tắm tự nhiên", "Du lịch cộng đồng, homestay của người Mường"],
    ["Nine-step waterfall – the \"Nine Steps of Love\"", "Clear, cool water with natural bathing pools", "Community tourism and Muong homestays"],
    ["Девятиступенчатый водопад — «Девять ступеней любви»", "Чистая прохладная вода с природными купальнями", "Общинный туризм и гостевые дома мыонгов"],
    {"hours_vi": "Khoảng 7:00–18:00 hằng ngày.", "ticket_vi": "Vé vào khoảng 30.000–50.000 VND/người.",
     "duration_vi": "Nửa ngày.", "best_time_vi": "Mùa hè (tháng 5–9) để tắm thác; sau mưa nước nhiều.",
     "tips_vi": "Mang đồ bơi, dép chống trơn; đi cẩn thận khi leo bậc thác; đặt homestay nếu ở lại."},
    ["waterfall", "nature", "swimming", "outdoor"],
    [{"title": "VietnamNet — Thác Mây 9 bậc tình yêu", "url": "https://vietnamnet.vn/thac-may-9-bac-tinh-yeu-dep-me-man-o-mien-tay-xu-thanh-2032076.html"}],
))

# 9) Hòn Trống Mái
new.append(R(
    "hon-trong-mai", "Hòn Trống Mái", "Trong Mai Rocks (Cock and Hen Rocks)", "Скалы Чонгмай (Петух и Курица)",
    ["monument", "other"], 19.7345, 105.9070,
    "Hòn Cổ Giải, núi Trường Lệ, phường Sầm Sơn, tỉnh Thanh Hóa",
    4.4, 900,
    "Du khách thích thú với hai khối đá lớn tựa đôi chim trống mái chênh vênh trên núi Trường Lệ, gắn truyền thuyết tình yêu. Nhiều người check-in và ngắm biển Sầm Sơn từ trên cao; một số nhắc leo dốc hơi mệt.",
    "Hòn Trống Mái là hai khối đá tự nhiên tựa đôi chim trống – mái nằm chênh vênh trên núi Trường Lệ, Sầm Sơn. Gắn với truyền thuyết tình yêu thủy chung, đây là biểu tượng và điểm check-in nổi tiếng của phố biển xứ Thanh.",
    "Trong Mai Rocks are two natural boulders resembling a cock and a hen, perched on Truong Le Mountain in Sam Son. Bound to a legend of faithful love, they are a symbol and a famous photo spot of Thanh Hoa's seaside town.",
    "Скалы Чонгмай — два природных валуна, напоминающие петуха и курицу, что примостились на горе Чыонгле в Шамшоне. Связанные с легендой о верной любви, они — символ и знаменитое место для фото приморского города Тханьхоа.",
    "Hòn Trống Mái là một danh thắng độc đáo nằm trên núi Trường Lệ, ngay sát bãi biển Sầm Sơn nổi tiếng của tỉnh Thanh Hóa. Đó là cụm ba khối đá granit khổng lồ: một hòn lớn dáng bè tựa như con gà mái nằm ấp, một hòn thon cao nghiêng về phía trên như con gà trống, và một tảng đá bằng phẳng đỡ bên dưới. Điều kỳ lạ là hai khối đá nặng hàng chục tấn chỉ tựa vào nhau ở một điểm, chênh vênh giữa lưng núi mà vẫn vững vàng qua bao mưa nắng, bão gió. Dân gian gắn cho hòn đá truyền thuyết cảm động về đôi vợ chồng nghèo yêu thương nhau, khi gặp nạn đã hóa thành đôi chim rồi hóa đá để mãi mãi bên nhau, vì thế Hòn Trống Mái trở thành biểu tượng cho tình yêu son sắt, thủy chung. Từ vị trí này, du khách vừa chiêm ngưỡng tác phẩm điêu khắc kỳ diệu của tạo hóa, vừa phóng tầm mắt bao quát toàn cảnh bãi biển Sầm Sơn cong mình ôm lấy bờ cát vàng và biển xanh. Đây là điểm dừng chân, chụp ảnh không thể bỏ qua trong hành trình khám phá Sầm Sơn.",
    "Trong Mai Rocks are a striking landmark on Truong Le Mountain, right beside the famous Sam Son beach of Thanh Hoa province. They are a cluster of huge granite boulders: a broad, flat one like a brooding hen, a slimmer tall one leaning above like a cock, and a level slab supporting them below. Remarkably, the two boulders — weighing tens of tonnes — touch at only one point, poised on the mountainside yet standing firm through rain, sun and storm. Folklore attaches to them a moving legend of a poor, loving couple who, meeting disaster, turned into a pair of birds and then into stone so as to remain together forever; thus Trong Mai became a symbol of steadfast, faithful love. From here, visitors admire this marvellous sculpture of nature while gazing over the whole sweep of Sam Son beach curving around golden sand and blue sea. It is an unmissable stop for photos on any tour of Sam Son.",
    "Скалы Чонгмай — впечатляющая достопримечательность на горе Чыонгле, прямо у знаменитого пляжа Шамшон провинции Тханьхоа. Это группа огромных гранитных валунов: широкий плоский, похожий на наседку, более стройный высокий, склонившийся сверху, словно петух, и ровная плита, поддерживающая их снизу. Удивительно, что два валуна весом в десятки тонн соприкасаются лишь в одной точке, балансируя на склоне, но стоят твёрдо сквозь дождь, солнце и бури. Народ связывает с ними трогательную легенду о бедной любящей паре, которая, попав в беду, обратилась в пару птиц, а затем в камень, чтобы навеки быть вместе; так Чонгмай стал символом стойкой, верной любви. Отсюда посетители любуются этим чудесным творением природы и обозревают весь изгиб пляжа Шамшон, обнимающего золотой песок и синее море. Это обязательная остановка для фото в любой поездке по Шамшону.",
    ["Hai khối đá granit tựa đôi chim trống – mái", "Biểu tượng tình yêu thủy chung, gắn truyền thuyết", "Ngắm toàn cảnh biển Sầm Sơn từ trên núi Trường Lệ"],
    ["Two granite boulders shaped like a cock and a hen", "A symbol of faithful love bound to legend", "Panorama of Sam Son beach from Truong Le Mountain"],
    ["Два гранитных валуна в форме петуха и курицы", "Символ верной любви, связанный с легендой", "Панорама пляжа Шамшон с горы Чыонгле"],
    {"hours_vi": "Khu vực ngoài trời, tham quan cả ngày.", "ticket_vi": "Miễn phí (có thể mất phí gửi xe).",
     "duration_vi": "Khoảng 30–45 phút.", "best_time_vi": "Sáng sớm hoặc chiều mát; mùa hè kết hợp tắm biển.",
     "tips_vi": "Đi giày bám tốt để leo dốc; kết hợp đền Độc Cước, đền Cô Tiên trên núi Trường Lệ."},
    ["nature", "landmark", "beach", "legend", "outdoor"],
    [{"title": "Wikipedia (VI) — Hòn Trống Mái (Sầm Sơn)", "url": "https://vi.wikipedia.org/wiki/H%C3%B2n_Tr%E1%BB%91ng_M%C3%A1i_(S%E1%BA%A7m_S%C6%A1n)"}],
))

# 10) Đền Độc Cước
new.append(R(
    "den-doc-cuoc", "Đền Độc Cước", "Doc Cuoc Temple", "Храм Докыок",
    ["church", "monument"], 19.7515, 105.9075,
    "Chân núi Trường Lệ, phường Sầm Sơn, tỉnh Thanh Hóa",
    4.4, 800,
    "Du khách viếng ngôi đền cổ trên mỏm núi nhô ra biển, nghe sự tích thần Độc Cước xẻ đôi thân mình cứu dân. Nhiều người thắp hương cầu bình an trước khi tắm biển; một số nhắc bậc thang lên đền hơi cao.",
    "Đền Độc Cước tọa lạc trên mỏm núi Trường Lệ nhô ra biển Sầm Sơn, thờ vị thần một chân đã tự xẻ đôi thân mình để vừa giữ đất vừa ra khơi đánh quỷ cứu dân chài. Đây là ngôi đền linh thiêng biểu tượng của Sầm Sơn.",
    "Doc Cuoc Temple stands on a spur of Truong Le Mountain jutting into the sea at Sam Son. It honours the one-legged god who split his own body in two to guard the land and go to sea to fight demons and save the fishermen — a sacred emblem of Sam Son.",
    "Храм Докыок стоит на отроге горы Чыонгле, выступающем в море у Шамшона. Он посвящён одноногому богу, что рассёк своё тело надвое, чтобы и охранять сушу, и выходить в море сражаться с демонами, спасая рыбаков, — священный символ Шамшона.",
    "Đền Độc Cước là ngôi đền cổ nằm trên hòn Cổ Giải, mỏm đá của núi Trường Lệ vươn ra sát mép biển Sầm Sơn. Đền thờ thần Độc Cước – nghĩa là \"một chân\" – gắn với truyền thuyết đẹp về lòng vị tha. Xưa kia, vùng biển Sầm Sơn thường bị quỷ biển quấy phá, dân chài ra khơi thì bị hại mà ở nhà cũng không yên. Một chàng khổng lồ đã quyết xẻ đôi thân mình: một nửa theo thuyền ra khơi diệt quỷ bảo vệ ngư dân, nửa còn lại đứng canh trên núi giữ cho xóm làng bình yên. Cảm kích công đức, người dân lập đền thờ ngay trên mỏm núi, in dấu \"bàn chân\" khổng lồ trên đá. Đền có kiến trúc nhỏ nhắn nhưng cổ kính, mái ngói rêu phong, tựa lưng vào núi, mặt hướng ra biển lộng gió. Từ sân đền, du khách có thể ngắm bao quát bãi tắm Sầm Sơn và nghe tiếng sóng vỗ dưới chân. Đền Độc Cước cùng đền Cô Tiên, Hòn Trống Mái tạo thành cụm di tích – danh thắng núi Trường Lệ, là nơi người dân và du khách thường ghé thắp hương cầu bình an, thuận buồm xuôi gió trước mỗi chuyến đi biển.",
    "Doc Cuoc Temple is an ancient shrine on Co Giai rock, a spur of Truong Le Mountain reaching to the water's edge at Sam Son. It honours the god Doc Cuoc — meaning \"one leg\" — through a beautiful legend of selflessness. Long ago, sea demons harried the waters of Sam Son: fishermen going out were harmed, yet those staying home were not safe either. A giant youth resolved to split his own body in two: one half sailed out to destroy the demons and protect the fishermen, the other stood watch on the mountain to keep the village safe. Moved by his merit, the people built a temple on the very spur, marking a giant \"footprint\" on the rock. The temple is small but ancient, its mossy tiled roof backed by the mountain and facing the windswept sea. From its courtyard, visitors take in the whole of Sam Son beach and hear the waves breaking below. Together with Co Tien Temple and Trong Mai Rocks, Doc Cuoc forms the Truong Le Mountain relic-and-scenery cluster, where locals and visitors often light incense to pray for peace and fair winds before setting out to sea.",
    "Храм Докыок — древнее святилище на скале Когзяй, отроге горы Чыонгле, доходящем до кромки воды у Шамшона. Он посвящён богу Докыок — что значит «одна нога» — через прекрасную легенду о самоотверженности. Давным-давно морские демоны терзали воды Шамшона: рыбаков, выходивших в море, губили, но и оставшиеся дома не были в безопасности. Юноша-великан решил рассечь своё тело надвое: одна половина уплыла уничтожать демонов и защищать рыбаков, другая осталась стеречь гору, оберегая деревню. Тронутые его подвигом, люди построили храм прямо на отроге, отметив на камне гигантский «след». Храм невелик, но древен: его замшелая черепичная крыша прислонена к горе, а фасад обращён к обдуваемому ветром морю. С его двора посетители видят весь пляж Шамшон и слышат, как внизу разбиваются волны. Вместе с храмом Ко Тьен и скалами Чонгмай Докыок образует комплекс достопримечательностей горы Чыонгле, где местные и туристы часто зажигают благовония, моля о мире и попутном ветре перед выходом в море.",
    ["Đền cổ trên mỏm núi Trường Lệ nhô ra biển", "Sự tích thần Độc Cước xẻ đôi thân cứu dân chài", "Cụm danh thắng cùng Hòn Trống Mái, đền Cô Tiên"],
    ["Ancient temple on a Truong Le spur jutting into the sea", "Legend of the god Doc Cuoc splitting himself to save fishermen", "Scenic cluster with Trong Mai Rocks and Co Tien Temple"],
    ["Древний храм на отроге Чыонгле, выступающем в море", "Легенда о боге Докыок, рассёкшем себя ради рыбаков", "Живописный комплекс со скалами Чонгмай и храмом Ко Тьен"],
    {"hours_vi": "Khoảng 6:00–18:00 hằng ngày.", "ticket_vi": "Vào cửa tự do (công đức tùy tâm).",
     "duration_vi": "Khoảng 30–45 phút.", "best_time_vi": "Sáng sớm hoặc chiều; mùa hè kết hợp tắm biển Sầm Sơn.",
     "tips_vi": "Ăn mặc lịch sự; leo bậc đá lên đền; kết hợp Hòn Trống Mái, đền Cô Tiên."},
    ["temple", "spiritual", "beach", "legend"],
    [{"title": "Wikipedia (VI) — Đền Độc Cước", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%81n_%C4%90%E1%BB%99c_C%C6%B0%E1%BB%9Bc"}],
))

# 11) Đền Cô Tiên
new.append(R(
    "den-co-tien", "Đền Cô Tiên", "Co Tien Temple", "Храм Ко Тьен",
    ["church"], 19.7290, 105.9120,
    "Đầu nam núi Trường Lệ, phường Sầm Sơn, tỉnh Thanh Hóa",
    4.3, 500,
    "Du khách thích ngôi đền cổ nằm nơi cao nhất núi Trường Lệ, view biển rộng và không khí trong lành. Nhiều người ghé vì gắn với nơi Bác Hồ từng nghỉ năm 1960; một số nhắc đường lên hơi vắng.",
    "Đền Cô Tiên nằm ở phía nam núi Trường Lệ, Sầm Sơn, thờ một người con gái nhân hậu trong truyền thuyết. Đền còn được biết đến là nơi Chủ tịch Hồ Chí Minh từng dừng chân nghỉ khi về thăm Sầm Sơn năm 1960.",
    "Co Tien Temple sits on the southern side of Truong Le Mountain in Sam Son, honouring a kind-hearted girl of legend. It is also known as a place where President Ho Chi Minh rested during his visit to Sam Son in 1960.",
    "Храм Ко Тьен расположен на южной стороне горы Чыонгле в Шамшоне и посвящён добросердечной девушке из легенды. Он известен и как место, где президент Хо Ши Мин отдыхал во время визита в Шамшон в 1960 году.",
    "Đền Cô Tiên tọa lạc trên sườn phía nam núi Trường Lệ, ở vị trí cao thoáng nhìn ra biển Sầm Sơn, hợp cùng đền Độc Cước và Hòn Trống Mái tạo thành cụm di tích – danh thắng nổi tiếng của phố biển. Đền gắn với truyền thuyết về một cô gái nghèo hiền lành, hiếu thảo, chuyên hái thuốc cứu người; nàng bị cha ép gả nhưng vẫn giữ tấm lòng son, về sau được người đời lập đền thờ và tôn là \"Cô Tiên\", biểu tượng cho lòng nhân ái và thủy chung. Ngôi đền có kiến trúc cổ gồm ba gian, mái ngói rêu phong, nép mình dưới bóng cây giữa không gian tĩnh lặng, gió biển lồng lộng. Một điểm đặc biệt khiến đền thêm ý nghĩa là vào tháng 7 năm 1960, trong lần về thăm Sầm Sơn, Chủ tịch Hồ Chí Minh đã nghỉ chân tại đây; nơi Bác từng ngồi nay vẫn được gìn giữ như một kỷ niệm thiêng liêng. Đứng từ sân đền, du khách có thể phóng tầm mắt ra bãi biển cong dài, những rặng thông và cả vùng trời nước mênh mông. Đền Cô Tiên là điểm đến vừa tâm linh vừa thư thái, thích hợp để vãn cảnh, tưởng nhớ và tận hưởng không khí trong lành của núi Trường Lệ.",
    "Co Tien Temple stands on the southern slope of Truong Le Mountain, high with an open view over Sam Son beach, and together with Doc Cuoc Temple and Trong Mai Rocks forms a famous relic-and-scenery cluster of the seaside town. It is bound to the legend of a poor, gentle and devoted girl who gathered herbs to heal the sick; forced by her father into marriage, she kept a faithful heart, and later generations built a temple and revered her as \"Co Tien\" (the Fairy Girl), a symbol of kindness and constancy. The temple is old, with three bays and a mossy tiled roof, nestled under trees in a quiet space swept by sea breezes. A special detail deepens its meaning: in July 1960, during a visit to Sam Son, President Ho Chi Minh rested here, and the spot where he sat is still preserved as a sacred memory. From the courtyard, visitors gaze over the long curving beach, the pine groves and the vast expanse of sky and sea. Co Tien Temple is a destination both spiritual and restful, ideal for sightseeing, remembrance and enjoying the fresh air of Truong Le Mountain.",
    "Храм Ко Тьен стоит на южном склоне горы Чыонгле, высоко, с открытым видом на пляж Шамшон, и вместе с храмом Докыок и скалами Чонгмай образует знаменитый комплекс достопримечательностей приморского города. Он связан с легендой о бедной, кроткой и преданной девушке, что собирала травы для исцеления больных; принуждённая отцом к замужеству, она сохранила верное сердце, и позже потомки построили храм, почитая её как «Ко Тьен» (Девушку-фею), символ доброты и постоянства. Храм старинный, с тремя пролётами и замшелой черепичной крышей, уютно устроился под деревьями в тихом месте, обдуваемом морским бризом. Особая деталь углубляет его значение: в июле 1960 года во время визита в Шамшон здесь отдыхал президент Хо Ши Мин, и место, где он сидел, до сих пор хранится как священная память. Со двора посетители смотрят на длинный изогнутый пляж, сосновые рощи и бескрайний простор неба и моря. Храм Ко Тьен — место и духовное, и умиротворяющее, идеальное для осмотра, воспоминаний и наслаждения свежим воздухом горы Чыонгле.",
    ["Đền cổ ở vị trí cao trên núi Trường Lệ", "Truyền thuyết Cô Tiên nhân hậu, thủy chung", "Nơi Bác Hồ từng dừng chân năm 1960"],
    ["Ancient temple high on Truong Le Mountain", "Legend of the kind and faithful Fairy Girl", "Where Ho Chi Minh rested in 1960"],
    ["Древний храм высоко на горе Чыонгле", "Легенда о доброй и верной Девушке-фее", "Место, где Хо Ши Мин отдыхал в 1960 году"],
    {"hours_vi": "Khoảng 6:00–18:00 hằng ngày.", "ticket_vi": "Vào cửa tự do (công đức tùy tâm).",
     "duration_vi": "Khoảng 30 phút.", "best_time_vi": "Sáng hoặc chiều mát; kết hợp tham quan núi Trường Lệ.",
     "tips_vi": "Đi theo đường lên núi Trường Lệ; kết hợp Hòn Trống Mái và đền Độc Cước thành một vòng."},
    ["temple", "spiritual", "beach", "history"],
    [{"title": "Wikipedia (VI) — Đền Cô Tiên (Sầm Sơn)", "url": "https://vi.wikipedia.org/wiki/S%E1%BA%A7m_S%C6%A1n"}],
))

print("Batch C (records 5-11) defined:", len(new))

data = json.load(open(F, encoding="utf-8")) if os.path.exists(F) else []
have = {p["slug"] for p in data}
added = [p for p in new if p["slug"] not in have]
data += added
json.dump(data, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Đã thêm:", len(added), "| giờ có", len(data))
