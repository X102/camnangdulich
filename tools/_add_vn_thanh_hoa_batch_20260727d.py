# -*- coding: utf-8 -*-
"""Thanh Hóa — batch D (records 12-18)."""
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

# 12) Bãi biển Hải Tiến
new.append(R(
    "bien-hai-tien", "Bãi biển Hải Tiến", "Hai Tien Beach", "Пляж Хайтьен",
    ["other"], 19.8340, 105.9520,
    "Xã Hoằng Tiến, huyện Hoằng Hóa, tỉnh Thanh Hóa",
    4.2, 1100,
    "Du khách thích bãi biển dài, cát mịn, còn khá mới mẻ và ít đông đúc hơn Sầm Sơn. Nhiều gia đình chọn Hải Tiến vì có resort, hải sản tươi ngon; một số nhắc sóng đôi khi khá lớn.",
    "Bãi biển Hải Tiến ở huyện Hoằng Hóa là khu du lịch biển sôi động phát triển sau này, với bờ cát dài khoảng 12 km, nước trong và nhiều khu nghỉ dưỡng. Đây là lựa chọn yên tĩnh hơn Sầm Sơn cho kỳ nghỉ biển xứ Thanh.",
    "Hai Tien Beach in Hoang Hoa district is a lively, more recently developed seaside resort with about 12 km of sand, clear water and many resorts. It is a quieter alternative to Sam Son for a beach holiday in Thanh Hoa.",
    "Пляж Хайтьен в уезде Хоангхоа — оживлённый, недавно освоенный морской курорт с примерно 12 км песка, чистой водой и множеством отелей. Это более спокойная альтернатива Шамшону для пляжного отдыха в Тханьхоа.",
    "Bãi biển Hải Tiến nằm ở huyện Hoằng Hóa, cách thành phố Thanh Hóa khoảng 17 km về phía đông, được đưa vào khai thác du lịch từ những năm 2010 và nhanh chóng trở thành một trong những điểm nghỉ biển hấp dẫn của xứ Thanh. Bãi biển trải dài khoảng 12 km với bờ cát trắng mịn thoai thoải, nước biển trong xanh, sóng vừa phải, thích hợp cho tắm biển và các hoạt động thể thao dưới nước. So với Sầm Sơn đông đúc và lâu đời, Hải Tiến trẻ trung, thoáng đãng và yên tĩnh hơn, phù hợp với các gia đình muốn tìm không gian nghỉ dưỡng thư thái. Dọc bờ biển đã hình thành hệ thống khách sạn, resort, quảng trường biển, khu vui chơi và hàng quán hải sản tươi sống với giá phải chăng. Du khách có thể dạo biển lúc bình minh, tắm mát, chèo thuyền kayak, chơi mô tô nước, hay thưởng thức đặc sản như ghẹ, mực, tôm, cá của vùng biển Hoằng Hóa. Gần đó còn có các điểm tham quan như đền thờ Tô Hiến Thành, cồn nổi và làng chài để khám phá thêm đời sống ngư dân. Vào mùa hè, Hải Tiến trở nên nhộn nhịp với các lễ hội du lịch biển, là điểm đến lý tưởng cho kỳ nghỉ cuối tuần.",
    "Hai Tien Beach lies in Hoang Hoa district, about 17 km east of Thanh Hoa city. Opened to tourism in the 2010s, it quickly became one of the region's appealing seaside spots. The beach runs about 12 km with fine white sand sloping gently to clear water and moderate waves, ideal for swimming and water sports. Compared with crowded, long-established Sam Son, Hai Tien is younger, more open and quieter, suiting families seeking a relaxed retreat. Along the shore stand hotels, resorts, a seaside square, amusement areas and eateries serving fresh seafood at reasonable prices. Visitors can stroll the beach at dawn, swim, kayak, ride jet-skis or enjoy specialities such as crab, squid, shrimp and fish from the waters of Hoang Hoa. Nearby are attractions such as the temple of To Hien Thanh, offshore sandbanks and fishing villages for a glimpse of local life. In summer Hai Tien bustles with seaside tourism festivals, making it an ideal destination for a weekend getaway.",
    "Пляж Хайтьен находится в уезде Хоангхоа, примерно в 17 км к востоку от города Тханьхоа. Открытый для туризма в 2010-х годах, он быстро стал одним из привлекательных морских мест края. Пляж тянется примерно на 12 км с мелким белым песком, полого спускающимся к чистой воде с умеренными волнами, идеален для купания и водного спорта. По сравнению с многолюдным и давно освоенным Шамшоном Хайтьен моложе, просторнее и тише, что подходит семьям, ищущим спокойный отдых. Вдоль берега стоят отели, курорты, приморская площадь, зоны развлечений и кафе со свежими морепродуктами по разумным ценам. Посетители могут гулять по пляжу на рассвете, купаться, кататься на каяках и гидроциклах или пробовать местные блюда — крабов, кальмаров, креветок и рыбу из вод Хоангхоа. Поблизости есть достопримечательности — храм То Хьен Тханя, прибрежные песчаные отмели и рыбацкие деревни, дающие представление о местной жизни. Летом Хайтьен оживает от приморских туристических фестивалей, что делает его идеальным местом для отдыха на выходных.",
    ["Bãi cát dài ~12 km, nước trong, sóng vừa", "Trẻ trung, yên tĩnh hơn Sầm Sơn", "Nhiều resort và hải sản tươi ngon giá tốt"],
    ["About 12 km of sand, clear water, moderate waves", "Younger and quieter than Sam Son", "Many resorts and fresh, well-priced seafood"],
    ["Около 12 км песка, чистая вода, умеренные волны", "Моложе и спокойнее Шамшона", "Много курортов и свежих морепродуктов по хорошей цене"],
    {"hours_vi": "Bãi biển mở cả ngày.", "ticket_vi": "Miễn phí (phí gửi xe, thuê ghế dù riêng).",
     "duration_vi": "Nửa ngày đến vài ngày.", "best_time_vi": "Mùa hè (tháng 5–8); tắm biển sáng sớm hoặc chiều.",
     "tips_vi": "Đặt phòng trước dịp cao điểm; hỏi giá hải sản trước khi ăn; chú ý cờ báo sóng."},
    ["beach", "sea", "resort", "family"],
    [{"title": "Wikipedia (VI) — Hải Tiến", "url": "https://vi.wikipedia.org/wiki/Ho%E1%BA%B1ng_H%C3%B3a"}],
))

# 13) Bãi biển Hải Hòa
new.append(R(
    "bien-hai-hoa", "Bãi biển Hải Hòa", "Hai Hoa Beach", "Пляж Хайхоа",
    ["other"], 19.4180, 105.7300,
    "Phường Hải Hòa, thị xã Nghi Sơn, tỉnh Thanh Hóa",
    4.3, 700,
    "Du khách khen bãi biển sạch, cát trắng mịn, còn hoang sơ và bình yên. Nhiều người thích không khí trong lành, hải sản rẻ; một số nhắc dịch vụ chưa nhiều bằng Sầm Sơn.",
    "Bãi biển Hải Hòa thuộc thị xã Nghi Sơn, phía nam tỉnh Thanh Hóa, nổi tiếng với bờ cát trắng mịn, nước trong và không gian yên bình. Đây là điểm nghỉ biển hoang sơ, thích hợp cho những ai muốn tránh sự ồn ào đông đúc.",
    "Hai Hoa Beach in Nghi Son town, southern Thanh Hoa, is known for fine white sand, clear water and a peaceful atmosphere. It is an unspoiled seaside spot, well suited to those wishing to escape the crowds.",
    "Пляж Хайхоа в городе Нгишон на юге Тханьхоа известен мелким белым песком, чистой водой и спокойной атмосферой. Это нетронутое морское место, хорошо подходящее тем, кто хочет уйти от толп.",
    "Bãi biển Hải Hòa nằm ở thị xã Nghi Sơn, cách thành phố Thanh Hóa khoảng 45 km về phía nam, gần khu kinh tế Nghi Sơn. Khác với vẻ sầm uất của Sầm Sơn hay sự phát triển nhanh của Hải Tiến, Hải Hòa vẫn giữ được nét hoang sơ, bình yên vốn có. Bãi biển dài, bờ cát trắng mịn và thoải, nước biển trong xanh, sóng êm, rất an toàn cho tắm biển và thư giãn. Hàng phi lao xanh mát chạy dọc bờ tạo bóng râm và không khí trong lành, dễ chịu. Buổi sớm, du khách có thể ngắm bình minh lên từ mặt biển, xem thuyền chài trở về với những mẻ cá tươi rói; buổi chiều thì dạo bộ trên cát, hóng gió biển. Hải sản ở đây phong phú, tươi ngon và giá bình dân với đủ loại tôm, ghẹ, mực, cá được đánh bắt ngay trong ngày. Những năm gần đây, Hải Hòa dần được đầu tư thêm khách sạn, homestay và dịch vụ du lịch, nhưng vẫn giữ nhịp sống chậm rãi, mộc mạc. Đây là lựa chọn lý tưởng cho các gia đình và nhóm bạn muốn có một kỳ nghỉ biển yên tĩnh, gần gũi thiên nhiên ở phía nam xứ Thanh.",
    "Hai Hoa Beach is in Nghi Son town, about 45 km south of Thanh Hoa city, near the Nghi Son Economic Zone. Unlike bustling Sam Son or fast-growing Hai Tien, Hai Hoa retains its original wild, peaceful charm. The beach is long, with fine, gently sloping white sand, clear water and gentle waves, very safe for swimming and relaxing. A cool line of casuarina trees runs along the shore, giving shade and fresh, pleasant air. At dawn, visitors can watch the sunrise over the sea and fishing boats return with fresh catches; in the afternoon they stroll on the sand in the sea breeze. Seafood here is plentiful, fresh and inexpensive, with all kinds of shrimp, crab, squid and fish landed the same day. In recent years Hai Hoa has gained more hotels, homestays and tourist services, yet keeps its slow, rustic pace. It is an ideal choice for families and groups of friends seeking a quiet beach holiday close to nature in the south of Thanh Hoa.",
    "Пляж Хайхоа находится в городе Нгишон, примерно в 45 км к югу от города Тханьхоа, рядом с экономической зоной Нгишон. В отличие от шумного Шамшона или быстрорастущего Хайтьена, Хайхоа сохраняет свою изначальную дикую, мирную прелесть. Пляж длинный, с мелким, полого спускающимся белым песком, чистой водой и мягкими волнами, очень безопасен для купания и отдыха. Вдоль берега тянется прохладная полоса казуарин, дающих тень и свежий приятный воздух. На рассвете посетители могут любоваться восходом над морем и возвращением рыбацких лодок со свежим уловом; днём — гулять по песку под морским бризом. Морепродукты здесь обильны, свежи и недороги — всевозможные креветки, крабы, кальмары и рыба, выловленные в тот же день. В последние годы в Хайхоа появилось больше отелей, гостевых домов и туристических услуг, но он сохраняет неспешный, деревенский ритм. Это идеальный выбор для семей и компаний друзей, ищущих тихий пляжный отдых на природе на юге Тханьхоа.",
    ["Bãi biển hoang sơ, cát trắng mịn, sóng êm", "Yên bình, ít đông đúc, không khí trong lành", "Hải sản tươi ngon, giá bình dân"],
    ["Unspoiled beach with fine white sand and gentle waves", "Peaceful, uncrowded and fresh-aired", "Fresh, inexpensive seafood"],
    ["Нетронутый пляж с мелким белым песком и мягкими волнами", "Спокойный, немноголюдный, со свежим воздухом", "Свежие недорогие морепродукты"],
    {"hours_vi": "Bãi biển mở cả ngày.", "ticket_vi": "Miễn phí (phí gửi xe/ghế dù riêng).",
     "duration_vi": "Nửa ngày đến vài ngày.", "best_time_vi": "Mùa hè (tháng 5–8).",
     "tips_vi": "Đặt phòng trước cuối tuần hè; mang kem chống nắng; kết hợp tham quan khu Nghi Sơn."},
    ["beach", "sea", "quiet", "family"],
    [{"title": "Wikipedia (VI) — Nghi Sơn", "url": "https://vi.wikipedia.org/wiki/Nghi_S%C6%A1n"}],
))

# 14) Đền thờ Lê Hoàn
new.append(R(
    "den-le-hoan", "Đền thờ Lê Hoàn", "Le Hoan Temple", "Храм Ле Хоана",
    ["church", "monument"], 19.9330, 105.4700,
    "Xã Xuân Lập, huyện Thọ Xuân, tỉnh Thanh Hóa",
    4.5, 500,
    "Du khách trân trọng ngôi đền cổ thờ vua Lê Đại Hành, khen kiến trúc gỗ chạm khắc tinh xảo và không gian trầm mặc. Nhiều người về dịp lễ hội tháng Ba âm lịch; một số mong có thêm thuyết minh lịch sử.",
    "Đền thờ Lê Hoàn ở huyện Thọ Xuân là nơi thờ vua Lê Đại Hành (Lê Hoàn) – người sáng lập nhà Tiền Lê, đánh tan quân Tống năm 981. Được xem là một trong những ngôi đền cổ nhất Thanh Hóa, đền là Di tích quốc gia đặc biệt.",
    "Le Hoan Temple in Tho Xuan district honours Emperor Le Dai Hanh (Le Hoan), founder of the Early Le dynasty, who crushed the Song army in 981. Considered one of the oldest temples in Thanh Hoa, it is a Special National Relic.",
    "Храм Ле Хоана в уезде Тхосуан посвящён императору Ле Дай Ханю (Ле Хоану), основателю ранней династии Ле, разгромившему армию Сун в 981 году. Считается одним из древнейших храмов Тханьхоа и является особым национальным памятником.",
    "Đền thờ Lê Hoàn nằm ở xã Xuân Lập, huyện Thọ Xuân, ngay trên chính quê hương của vua Lê Đại Hành – vị hoàng đế sáng lập triều Tiền Lê. Lê Hoàn (941–1005) vốn là thập đạo tướng quân, được suy tôn lên ngôi trong bối cảnh nhà Đinh suy yếu và quân Tống lăm le xâm lược. Năm 981, ông lãnh đạo quân dân Đại Cồ Việt đánh tan cuộc xâm lược của nhà Tống trên cả hai mặt trận thủy – bộ, giữ vững nền độc lập non trẻ, rồi tiếp tục củng cố đất nước, phát triển nông nghiệp và mở mang bờ cõi. Ngôi đền được dựng để tưởng nhớ công lao của ông, trải qua nhiều lần trùng tu nhưng vẫn giữ được kiến trúc gỗ cổ kính với những mảng chạm khắc rồng, hoa lá tinh xảo, cùng nhiều hiện vật, sắc phong quý giá. Đây được coi là một trong những ngôi đền có niên đại lâu đời nhất ở Thanh Hóa. Hằng năm, lễ hội đền thờ Lê Hoàn được tổ chức vào khoảng ngày 7–8 tháng Ba âm lịch, tái hiện nghi lễ truyền thống và các trò chơi dân gian, thu hút đông đảo nhân dân. Đền đã được xếp hạng Di tích lịch sử quốc gia đặc biệt, là điểm đến ý nghĩa với những ai muốn tìm hiểu lịch sử dựng nước và giữ nước.",
    "Le Hoan Temple stands in Xuan Lap commune, Tho Xuan district, on the very homeland of Emperor Le Dai Hanh, founder of the Early Le dynasty. Le Hoan (941–1005), once a supreme general, was raised to the throne as the Dinh dynasty weakened and the Song threatened invasion. In 981 he led the people of Dai Co Viet to smash the Song invasion on both land and water, safeguarding the young nation's independence, then went on to strengthen the country, develop agriculture and expand its borders. The temple was built to honour his merit; restored many times, it keeps its ancient wooden architecture with fine carvings of dragons and foliage, along with many precious artefacts and royal edicts. It is regarded as one of the oldest temples in Thanh Hoa. Each year the Le Hoan Temple Festival is held around the 7th–8th of the third lunar month, re-enacting traditional rites and folk games and drawing large crowds. The temple is ranked a Special National Historical Relic, a meaningful destination for those wishing to learn the history of building and defending the nation.",
    "Храм Ле Хоана стоит в общине Суанлап уезда Тхосуан, на самой родине императора Ле Дай Ханя, основателя ранней династии Ле. Ле Хоан (941–1005), некогда верховный полководец, был возведён на престол, когда династия Динь ослабла, а Сун грозили вторжением. В 981 году он повёл народ Дайковьета разгромить сунское нашествие и на суше, и на воде, отстояв независимость молодого государства, а затем укреплял страну, развивал земледелие и расширял её пределы. Храм был построен в честь его заслуг; многократно отреставрированный, он сохраняет древнюю деревянную архитектуру с тонкой резьбой драконов и растений, а также множество ценных реликвий и царских указов. Он считается одним из древнейших храмов Тханьхоа. Ежегодно около 7–8-го числа третьего лунного месяца проходит фестиваль храма Ле Хоана, воссоздающий традиционные обряды и народные игры и привлекающий большие толпы. Храм отнесён к особым национальным историческим памятникам и является значимым местом для тех, кто хочет узнать историю созидания и защиты страны.",
    ["Thờ vua Lê Đại Hành, người phá Tống năm 981", "Một trong những đền cổ nhất Thanh Hóa, kiến trúc gỗ chạm khắc", "Di tích quốc gia đặc biệt; lễ hội tháng Ba âm lịch"],
    ["Honours Emperor Le Dai Hanh, who defeated the Song in 981", "One of Thanh Hoa's oldest temples with carved wooden architecture", "Special National Relic; festival in the third lunar month"],
    ["Посвящён императору Ле Дай Ханю, разбившему Сун в 981 году", "Один из древнейших храмов Тханьхоа с резной деревянной архитектурой", "Особый национальный памятник; фестиваль в третьем лунном месяце"],
    {"hours_vi": "Khoảng 7:00–17:30 hằng ngày.", "ticket_vi": "Vào cửa tự do (công đức tùy tâm).",
     "duration_vi": "Khoảng 45–60 phút.", "best_time_vi": "Dịp lễ hội tháng Ba âm lịch hoặc buổi sáng.",
     "tips_vi": "Kết hợp tham quan Lam Kinh, Thành nhà Hồ trong cùng vùng Thọ Xuân – Vĩnh Lộc."},
    ["history", "temple", "heritage", "dynasty"],
    [{"title": "Wikipedia (VI) — Đền thờ Lê Hoàn", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%81n_th%E1%BB%9D_L%C3%AA_Ho%C3%A0n"}],
))

# 15) Làng cổ Đông Sơn
new.append(R(
    "lang-co-dong-son", "Làng cổ Đông Sơn", "Dong Son Ancient Village", "Древняя деревня Донгшон",
    ["other", "monument"], 19.8130, 105.7620,
    "Phường Hàm Rồng, TP Thanh Hóa, tỉnh Thanh Hóa",
    4.3, 400,
    "Du khách thích những ngõ nhỏ, nhà cổ và không gian làng quê yên bình gắn với nền văn hóa Đông Sơn. Nhiều người tò mò về nơi phát hiện trống đồng nổi tiếng; một số mong có bảo tàng tại chỗ đầy đủ hơn.",
    "Làng cổ Đông Sơn bên bờ sông Mã (TP Thanh Hóa) là nơi khởi nguồn tên gọi \"văn hóa Đông Sơn\" – nền văn minh trống đồng rực rỡ của người Việt cổ. Ngôi làng còn giữ nhiều nhà cổ, ngõ xóm mang tên Nhân – Nghĩa – Trí – Dũng.",
    "Dong Son Ancient Village on the bank of the Ma River (Thanh Hoa city) gave its name to the \"Dong Son culture\", the brilliant bronze-drum civilisation of the ancient Viet. The village still keeps old houses and lanes named after the virtues Nhan, Nghia, Tri and Dung.",
    "Древняя деревня Донгшон на берегу реки Ма (город Тханьхоа) дала имя «культуре Донгшон» — блестящей цивилизации бронзовых барабанов древних вьетов. В деревне до сих пор сохранились старинные дома и переулки, названные в честь добродетелей Нян, Нгиа, Чи и Зунг.",
    "Làng cổ Đông Sơn nằm bên bờ nam sông Mã, dưới chân núi Rồng thuộc phường Hàm Rồng, thành phố Thanh Hóa. Đây chính là nơi mà năm 1924, những hiện vật đồng đầu tiên được phát hiện, để rồi tên ngôi làng được đặt cho cả một nền văn hóa khảo cổ rực rỡ – văn hóa Đông Sơn (khoảng thế kỷ 7 trước Công nguyên đến thế kỷ 1–2 sau Công nguyên), với biểu tượng là chiếc trống đồng tinh xảo, minh chứng cho trình độ luyện kim và đời sống phong phú của người Việt cổ. Ngôi làng nhỏ nằm nép mình bên sông vẫn lưu giữ được dáng vẻ làng quê Bắc Trung Bộ truyền thống với cây đa, giếng nước, những nếp nhà cổ mái ngói, tường đá và hệ thống ngõ xóm được đặt tên theo bốn đức tính Nhân – Nghĩa – Trí – Dũng. Dạo bước trong làng, du khách như ngược dòng thời gian, cảm nhận không gian tĩnh lặng, mộc mạc và bề dày lịch sử. Làng cổ Đông Sơn nằm trong quần thể danh thắng Hàm Rồng, thuận tiện kết hợp tham quan cầu Hàm Rồng, động Long Quang, thiền viện và các di tích lân cận, tạo nên một hành trình vừa khám phá lịch sử vừa thư giãn giữa thiên nhiên.",
    "Dong Son Ancient Village lies on the southern bank of the Ma River, at the foot of Dragon Mountain in Ham Rong ward, Thanh Hoa city. It was here, in 1924, that the first bronze artefacts were discovered, and the village's name was given to a brilliant archaeological culture — the Dong Son culture (about the 7th century BC to the 1st–2nd century AD), symbolised by the finely worked bronze drum, proof of the metallurgy and rich life of the ancient Viet. The small village nestled by the river still keeps the look of a traditional north-central hamlet, with a banyan tree, a well, old tile-roofed and stone-walled houses, and a network of lanes named after the four virtues Nhan (benevolence), Nghia (righteousness), Tri (wisdom) and Dung (courage). Strolling through the village, visitors seem to travel back in time, feeling the quiet, rustic space and the depth of history. Part of the Ham Rong scenic complex, Dong Son village is easily combined with visits to Ham Rong Bridge, Long Quang Cave, the meditation monastery and nearby relics, forming a journey that blends historical discovery with relaxation in nature.",
    "Древняя деревня Донгшон лежит на южном берегу реки Ма, у подножия горы Дракона в квартале Хамронг города Тханьхоа. Именно здесь в 1924 году были найдены первые бронзовые артефакты, и имя деревни было дано блестящей археологической культуре — культуре Донгшон (примерно с VII века до н. э. по I–II век н. э.), символом которой стал тонко выполненный бронзовый барабан, свидетельство металлургии и богатой жизни древних вьетов. Маленькая деревня, приютившаяся у реки, до сих пор хранит облик традиционного северо-центрального селения — с баньяном, колодцем, старыми домами под черепицей и каменными стенами и сетью переулков, названных в честь четырёх добродетелей: Нян (человеколюбие), Нгиа (справедливость), Чи (мудрость) и Зунг (мужество). Прогуливаясь по деревне, посетители словно возвращаются во времени, ощущая тихое, деревенское пространство и глубину истории. Входя в живописный комплекс Хамронг, деревня Донгшон легко сочетается с посещением моста Хамронг, пещеры Лонгкуанг, медитационного монастыря и близлежащих памятников, образуя маршрут, соединяющий историческое открытие с отдыхом на природе.",
    ["Nơi khởi nguồn tên gọi văn hóa Đông Sơn (trống đồng)", "Làng quê cổ bên sông Mã, ngõ Nhân – Nghĩa – Trí – Dũng", "Nằm trong quần thể danh thắng Hàm Rồng"],
    ["Birthplace of the name 'Dong Son culture' (bronze drums)", "Old riverside village with lanes of the four virtues", "Part of the Ham Rong scenic complex"],
    ["Место, давшее имя «культуре Донгшон» (бронзовые барабаны)", "Старая деревня у реки с переулками четырёх добродетелей", "Часть живописного комплекса Хамронг"],
    {"hours_vi": "Khu vực làng, tham quan ban ngày.", "ticket_vi": "Miễn phí tham quan làng.",
     "duration_vi": "Khoảng 1 giờ.", "best_time_vi": "Buổi sáng hoặc chiều mát.",
     "tips_vi": "Kết hợp cầu Hàm Rồng, động Long Quang; tôn trọng nếp sinh hoạt của người dân trong làng."},
    ["history", "village", "archaeology", "heritage"],
    [{"title": "Wikipedia (VI) — Văn hóa Đông Sơn", "url": "https://vi.wikipedia.org/wiki/V%C4%83n_h%C3%B3a_%C4%90%C3%B4ng_S%C6%A1n"}],
))

# 16) Nhà thờ Chính tòa Thanh Hóa
new.append(R(
    "nha-tho-chinh-toa-thanh-hoa", "Nhà thờ Chính tòa Thanh Hóa", "Thanh Hoa Cathedral", "Кафедральный собор Тханьхоа",
    ["church"], 19.8035, 105.7760,
    "Phường Trường Thi, TP Thanh Hóa, tỉnh Thanh Hóa",
    4.5, 600,
    "Du khách ấn tượng với nhà thờ mang kiến trúc Gothic uy nghi, tháp chuông cao và không gian trang nghiêm. Nhiều người tới chụp ảnh và dự lễ dịp Giáng sinh; một số nhắc nên giữ yên tĩnh khi có thánh lễ.",
    "Nhà thờ Chính tòa Thanh Hóa là nhà thờ mẹ của Giáo phận Thanh Hóa, tọa lạc tại trung tâm thành phố. Công trình mang phong cách kiến trúc Gothic với tháp chuông cao vút, là điểm nhấn tôn giáo và kiến trúc của xứ Thanh.",
    "Thanh Hoa Cathedral is the mother church of the Diocese of Thanh Hoa, in the city centre. Built in Gothic style with a soaring bell tower, it is a religious and architectural landmark of the province.",
    "Кафедральный собор Тханьхоа — главный храм епархии Тханьхоа в центре города. Построенный в готическом стиле с устремлённой ввысь колокольней, он является религиозной и архитектурной достопримечательностью провинции.",
    "Nhà thờ Chính tòa Thanh Hóa nằm ở trung tâm thành phố Thanh Hóa, là nhà thờ chính tòa – nơi đặt ngai tòa của giám mục Giáo phận Thanh Hóa. Được xây dựng và tôn tạo qua nhiều giai đoạn, công trình mang đậm phong cách kiến trúc Gothic châu Âu với mặt tiền bề thế, những ô cửa vòm nhọn, các cột trụ vươn cao và đặc biệt là tháp chuông cao vút nổi bật trên nền trời thành phố. Bên trong thánh đường rộng rãi, trần cao, ánh sáng dịu chan hòa qua các ô kính màu, tạo nên không gian trang nghiêm và tĩnh lặng. Đây không chỉ là trung tâm sinh hoạt tôn giáo của cộng đồng Công giáo trong vùng mà còn là một điểm tham quan kiến trúc thu hút du khách. Vào các dịp lễ trọng như Giáng sinh, Phục sinh, nhà thờ được trang hoàng lộng lẫy, thu hút đông đảo giáo dân và người dân đến dự lễ, thưởng ngoạn. Với vẻ đẹp cổ điển, uy nghi giữa lòng phố, nhà thờ Chính tòa Thanh Hóa là nơi lý tưởng để tìm hiểu đời sống tôn giáo địa phương, chiêm ngưỡng kiến trúc và lưu lại những bức ảnh đẹp. Khi tham quan, du khách nên ăn mặc lịch sự và giữ trật tự, nhất là trong giờ có thánh lễ.",
    "Thanh Hoa Cathedral stands in the centre of Thanh Hoa city as the cathedral church — the seat of the bishop of the Diocese of Thanh Hoa. Built and embellished over several phases, it bears a strong European Gothic style, with an imposing façade, pointed arched windows, soaring columns and, above all, a lofty bell tower that stands out against the city sky. Inside, the nave is spacious and high, soft light streaming through stained-glass windows to create a solemn, quiet space. It is not only the religious hub of the region's Catholic community but also an architectural attraction for visitors. On great feast days such as Christmas and Easter, the church is splendidly decorated and draws crowds of parishioners and residents to attend Mass and admire it. With its classical, dignified beauty in the heart of the city, Thanh Hoa Cathedral is an ideal place to learn about local religious life, appreciate the architecture and take fine photographs. When visiting, guests should dress modestly and keep quiet, especially during Mass.",
    "Кафедральный собор Тханьхоа стоит в центре города Тханьхоа как соборный храм — резиденция епископа епархии Тханьхоа. Построенный и украшавшийся в несколько этапов, он несёт выраженный европейский готический стиль: внушительный фасад, стрельчатые окна, взмывающие колонны и, главное, высокая колокольня, выделяющаяся на фоне городского неба. Внутри неф просторный и высокий, мягкий свет струится сквозь витражи, создавая торжественное, тихое пространство. Это не только религиозный центр католической общины края, но и архитектурная достопримечательность для гостей. В большие праздники, такие как Рождество и Пасха, храм пышно украшают, и он привлекает толпы прихожан и жителей на мессу и для осмотра. Своей классической, величавой красотой в сердце города собор Тханьхоа — идеальное место, чтобы узнать о местной религиозной жизни, оценить архитектуру и сделать красивые фотографии. При посещении гостям следует одеваться скромно и соблюдать тишину, особенно во время мессы.",
    ["Nhà thờ mẹ của Giáo phận Thanh Hóa", "Kiến trúc Gothic, tháp chuông cao vút", "Trang hoàng lộng lẫy dịp Giáng sinh, Phục sinh"],
    ["Mother church of the Diocese of Thanh Hoa", "Gothic architecture with a soaring bell tower", "Splendidly decorated at Christmas and Easter"],
    ["Главный храм епархии Тханьхоа", "Готическая архитектура с высокой колокольней", "Пышно украшен на Рождество и Пасху"],
    {"hours_vi": "Mở cửa ban ngày; giờ lễ theo lịch nhà thờ.", "ticket_vi": "Miễn phí.",
     "duration_vi": "Khoảng 30 phút.", "best_time_vi": "Ngoài giờ lễ để tham quan; dịp Giáng sinh rất đẹp.",
     "tips_vi": "Ăn mặc lịch sự, giữ yên tĩnh; xin phép trước khi chụp ảnh trong giờ lễ."},
    ["church", "architecture", "gothic", "city"],
    [{"title": "Giáo phận Thanh Hóa — Nhà thờ Chính tòa", "url": "https://giaophanthanhhoa.org/"}],
))

# 17) Bảo tàng tỉnh Thanh Hóa
new.append(R(
    "bao-tang-thanh-hoa", "Bảo tàng tỉnh Thanh Hóa", "Thanh Hoa Provincial Museum", "Провинциальный музей Тханьхоа",
    ["museum"], 19.8065, 105.7810,
    "Đường Trường Thi, phường Điện Biên, TP Thanh Hóa, tỉnh Thanh Hóa",
    4.3, 300,
    "Du khách đánh giá cao bộ sưu tập trống đồng Đông Sơn và hiện vật khảo cổ quý. Nhiều người thấy bảo tàng hữu ích để hiểu lịch sử xứ Thanh; một số mong trưng bày hiện đại và mở cửa ổn định hơn.",
    "Bảo tàng tỉnh Thanh Hóa lưu giữ hàng nghìn hiện vật về lịch sử – văn hóa xứ Thanh, nổi bật là bộ sưu tập trống đồng và cổ vật văn hóa Đông Sơn. Đây là nơi lý tưởng để tìm hiểu chiều sâu lịch sử của vùng đất địa linh nhân kiệt.",
    "Thanh Hoa Provincial Museum holds thousands of artefacts on the history and culture of the region, notably a collection of bronze drums and Dong Son antiquities. It is an ideal place to grasp the depth of history of this storied land.",
    "Провинциальный музей Тханьхоа хранит тысячи экспонатов по истории и культуре края, прежде всего коллекцию бронзовых барабанов и древностей культуры Донгшон. Это идеальное место, чтобы постичь глубину истории этой прославленной земли.",
    "Bảo tàng tỉnh Thanh Hóa nằm ở trung tâm thành phố, là nơi lưu giữ và trưng bày hàng nghìn hiện vật phản ánh bề dày lịch sử, văn hóa của xứ Thanh – vùng đất được mệnh danh \"địa linh nhân kiệt\", quê hương của nhiều triều đại và anh hùng dân tộc. Bộ sưu tập của bảo tàng trải dài từ thời tiền sử, sơ sử với các di chỉ khảo cổ nổi tiếng, đặc biệt là hiện vật văn hóa Đông Sơn cùng những chiếc trống đồng tinh xảo – biểu tượng của nền văn minh trống đồng rực rỡ; cho tới các thời kỳ phong kiến với gốm sứ, vũ khí, bia đá, sắc phong, và các hiện vật cách mạng, kháng chiến của thế kỷ 20. Nhiều cổ vật ở đây có giá trị đặc biệt, giúp người xem hình dung sinh động về đời sống, tín ngưỡng và tài năng của cư dân xứ Thanh qua các thời đại. Không gian trưng bày được sắp xếp theo tiến trình lịch sử, kèm chú thích và hình ảnh minh họa. Đối với du khách và học sinh, đây là điểm đến bổ ích để tìm hiểu cội nguồn văn hóa trước khi khám phá các di tích như Thành nhà Hồ, Lam Kinh, Đông Sơn. Du khách nên liên hệ trước hoặc kiểm tra giờ mở cửa vì bảo tàng có thể đóng vào một số ngày trong tuần.",
    "Thanh Hoa Provincial Museum stands in the city centre, preserving and displaying thousands of artefacts that reflect the depth of the region's history and culture — a land dubbed \"sacred and rich in talent\", home to many dynasties and national heroes. Its collection ranges from prehistory and protohistory, with famous archaeological sites — especially Dong Son culture objects and finely worked bronze drums, symbols of a brilliant bronze-drum civilisation — through the feudal eras, with ceramics, weapons, stone steles and royal edicts, to revolutionary and wartime relics of the 20th century. Many antiquities here are of special value, helping viewers vividly picture the life, beliefs and talent of the people of Thanh Hoa across the ages. The displays are arranged chronologically, with captions and illustrative images. For visitors and students, it is a rewarding place to understand cultural origins before exploring relics such as the Ho Citadel, Lam Kinh and Dong Son. Guests should check opening hours in advance, as the museum may close on certain days of the week.",
    "Провинциальный музей Тханьхоа находится в центре города и хранит и выставляет тысячи экспонатов, отражающих глубину истории и культуры края — земли, прозванной «священной и богатой талантами», родины многих династий и национальных героев. Его собрание охватывает время от доистории и протоистории с известными археологическими памятниками — прежде всего предметами культуры Донгшон и тонко выполненными бронзовыми барабанами, символами блестящей цивилизации бронзовых барабанов, — через феодальные эпохи с керамикой, оружием, каменными стелами и царскими указами до революционных и военных реликвий XX века. Многие древности здесь имеют особую ценность и помогают зрителям живо представить жизнь, верования и талант народа Тханьхоа сквозь века. Экспозиция выстроена в хронологическом порядке, с подписями и иллюстрациями. Для гостей и школьников это полезное место, чтобы понять истоки культуры перед осмотром памятников — цитадели Хо, Ламкиня и Донгшона. Гостям стоит заранее уточнить часы работы, так как музей может быть закрыт в некоторые дни недели.",
    ["Bộ sưu tập trống đồng và cổ vật Đông Sơn", "Hiện vật trải dài từ tiền sử đến kháng chiến", "Điểm khởi đầu để hiểu lịch sử xứ Thanh"],
    ["Collection of bronze drums and Dong Son antiquities", "Artefacts from prehistory to the resistance wars", "A starting point for understanding Thanh Hoa's history"],
    ["Коллекция бронзовых барабанов и древностей Донгшон", "Экспонаты от доистории до войн сопротивления", "Отправная точка для понимания истории Тханьхоа"],
    {"hours_vi": "Giờ hành chính (nên kiểm tra trước; có thể nghỉ một số ngày).", "ticket_vi": "Vé thấp hoặc miễn phí (tùy chương trình).",
     "duration_vi": "Khoảng 1 giờ.", "best_time_vi": "Ngày thường, buổi sáng.",
     "tips_vi": "Liên hệ trước để chắc chắn giờ mở cửa; kết hợp tham quan các di tích trong thành phố."},
    ["museum", "history", "archaeology", "city"],
    [{"title": "Wikipedia (VI) — Bảo tàng tỉnh Thanh Hóa", "url": "https://vi.wikipedia.org/wiki/Thanh_H%C3%B3a"}],
))

# 18) Hồ Cửa Đạt
new.append(R(
    "ho-cua-dat", "Hồ Cửa Đạt", "Cua Dat Reservoir", "Водохранилище Кыадат",
    ["other", "park_garden"], 19.9050, 105.3350,
    "Xã Vạn Xuân, huyện Thường Xuân, tỉnh Thanh Hóa",
    4.4, 400,
    "Du khách choáng ngợp trước hồ nước mênh mông giữa núi rừng và con đập bê tông đồ sộ. Nhiều người kết hợp đi thuyền và viếng đền Cửa Đặt gần đó; một số nhắc đường vào khá xa trung tâm.",
    "Hồ Cửa Đạt ở huyện Thường Xuân là hồ chứa nước nhân tạo lớn với đập bê tông đầm lăn quy mô hàng đầu Việt Nam. Mặt hồ rộng mênh mông giữa núi rừng, gần đền Cửa Đặt linh thiêng, tạo nên điểm du lịch sinh thái – tâm linh hấp dẫn.",
    "Cua Dat Reservoir in Thuong Xuan district is a large man-made lake with one of Vietnam's foremost roller-compacted concrete dams. Its vast waters amid mountains, near the sacred Cua Dat Temple, make an appealing eco- and spiritual destination.",
    "Водохранилище Кыадат в уезде Тхыонгсуан — крупное искусственное озеро с одной из ведущих во Вьетнаме плотин из укатанного бетона. Его обширные воды среди гор, рядом со священным храмом Кыадат, образуют привлекательное экологическое и духовное место.",
    "Hồ Cửa Đạt là hồ chứa nước lớn nằm trên thượng nguồn sông Chu thuộc huyện Thường Xuân, phía tây tỉnh Thanh Hóa. Công trình hồ – đập Cửa Đạt được xây dựng nhằm cung cấp nước tưới, phát điện, cắt lũ và cấp nước sinh hoạt cho vùng hạ du rộng lớn. Điểm nhấn của công trình là con đập bê tông đầm lăn cao và dài vào loại lớn nhất Việt Nam khi hoàn thành, chắn ngang dòng sông, tạo nên một hồ nước mênh mông trải dài giữa điệp trùng núi rừng miền tây xứ Thanh. Nước hồ xanh biếc, tĩnh lặng, phản chiếu mây trời và những dãy núi, khiến khung cảnh vừa hùng vĩ vừa nên thơ. Du khách đến đây có thể đứng trên thân đập ngắm toàn cảnh, đi thuyền dạo hồ, câu cá, hoặc khám phá các bản làng của đồng bào Thái quanh vùng lòng hồ. Ngay gần đó là khu di tích đền Cửa Đặt, nơi thờ danh nhân Cầm Bá Thước – thủ lĩnh phong trào Cần Vương chống Pháp và Bà Chúa Thượng Ngàn, thu hút đông người hành hương, nhất là dịp đầu năm. Sự kết hợp giữa cảnh quan thiên nhiên kỳ vĩ, công trình thủy lợi hiện đại và không gian tâm linh khiến Cửa Đạt trở thành điểm dừng chân thú vị trên hành trình khám phá miền núi Thanh Hóa.",
    "Cua Dat Reservoir is a large lake on the upper Chu River in Thuong Xuan district, western Thanh Hoa. The Cua Dat lake-and-dam project was built to supply irrigation, generate power, control floods and provide domestic water for a broad downstream area. Its centrepiece is a roller-compacted concrete dam, among the tallest and longest in Vietnam when completed, damming the river to form a vast lake stretching across the layered mountains of western Thanh Hoa. The jade-green, still water reflects clouds, sky and mountain ranges, making the scene both grand and poetic. Here visitors can stand on the dam to take in the panorama, cruise the lake by boat, fish, or explore the Thai villages around the lakeshore. Nearby is the Cua Dat Temple relic, dedicated to the notable Cam Ba Thuoc — a leader of the anti-French Can Vuong movement — and the Lady of the Highlands, drawing many pilgrims, especially at the start of the year. The blend of majestic natural scenery, a modern hydraulic works and a spiritual site makes Cua Dat an interesting stop on a journey through mountainous Thanh Hoa.",
    "Водохранилище Кыадат — большое озеро в верховьях реки Тю в уезде Тхыонгсуан на западе Тханьхоа. Проект озера и плотины Кыадат был построен для орошения, выработки электроэнергии, борьбы с паводками и снабжения питьевой водой обширной низовой территории. Его центр — плотина из укатанного бетона, одна из самых высоких и длинных во Вьетнаме на момент завершения, перегораживающая реку и образующая обширное озеро, что тянется среди ярусов гор западного Тханьхоа. Нефритово-зелёная, спокойная вода отражает облака, небо и горные хребты, делая пейзаж и величественным, и поэтичным. Здесь посетители могут встать на плотину, чтобы охватить панораму, покататься по озеру на лодке, порыбачить или исследовать деревни тай вокруг берегов. Рядом — памятник храм Кыадат, посвящённый выдающемуся Кам Ба Тхыоку, вождю антифранцузского движения Кангвыонг, и Владычице нагорий, привлекающий множество паломников, особенно в начале года. Сочетание величественных природных пейзажей, современного гидротехнического сооружения и духовного места делает Кыадат интересной остановкой в путешествии по горному Тханьхоа.",
    ["Hồ chứa lớn, đập bê tông đầm lăn quy mô hàng đầu VN", "Mặt hồ mênh mông giữa núi rừng miền tây xứ Thanh", "Gần đền Cửa Đặt thờ Cầm Bá Thước, Bà Chúa Thượng Ngàn"],
    ["Large reservoir with a leading roller-compacted concrete dam", "Vast lake amid the mountains of western Thanh Hoa", "Near Cua Dat Temple honouring Cam Ba Thuoc and the Lady of the Highlands"],
    ["Крупное водохранилище с ведущей плотиной из укатанного бетона", "Обширное озеро среди гор западного Тханьхоа", "Рядом храм Кыадат в честь Кам Ба Тхыока и Владычицы нагорий"],
    {"hours_vi": "Khu vực ngoài trời, tham quan ban ngày.", "ticket_vi": "Miễn phí tham quan; thuê thuyền theo thỏa thuận.",
     "duration_vi": "Nửa ngày.", "best_time_vi": "Mùa khô (tháng 10–4); tránh mùa mưa lũ.",
     "tips_vi": "Kết hợp viếng đền Cửa Đặt; hỏi giá thuyền trước; chuẩn bị đồ ăn nhẹ vì ít hàng quán."},
    ["lake", "nature", "reservoir", "spiritual", "outdoor"],
    [{"title": "Wikipedia (VI) — Hồ Cửa Đạt", "url": "https://vi.wikipedia.org/wiki/H%E1%BB%93_C%E1%BB%ADa_%C4%90%E1%BA%A1t"}],
))

print("Batch D (records 12-18) defined:", len(new))

data = json.load(open(F, encoding="utf-8")) if os.path.exists(F) else []
have = {p["slug"] for p in data}
added = [p for p in new if p["slug"] not in have]
data += added
json.dump(data, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Đã thêm:", len(added), "| giờ có", len(data))
