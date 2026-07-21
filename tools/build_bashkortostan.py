# -*- coding: utf-8 -*-
import json, os

records = [
    {
        "region": "bashkortostan",
        "slug": "shulgan-tash-cave",
        "name_vi": "Hang động Shulgan-Tash (Hang Kapova)",
        "name_ru": "Капова пещера (Шульган-Таш)",
        "name_en": "Shulgan-Tash Cave (Kapova Cave)",
        "categories": ["other", "park_garden"],
        "lat": 53.044417,
        "lon": 57.063890,
        "address_vi": "Khu bảo tồn thiên nhiên Shulgan-Tash, huyện Burzyan, Cộng hòa Bashkortostan, Nga (bên sông Belaya, cách Ufa khoảng 350–400 km về phía đông nam)",
        "rating": {"value": None, "count": None, "source": "Yandex Карты", "as_of": "2026-07"},
        "review_summary_vi": "Du khách coi đây là điểm đến mang tính biểu tượng của vùng Ural, ấn tượng trước giá trị khảo cổ và không gian huyền bí bên dòng Belaya. Nhiều người lưu ý bản gốc các bức vẽ đã đóng cửa để bảo tồn nên khách chủ yếu xem bản sao ở sảnh ngoài, song hành trình và cảnh quan vẫn rất đáng giá.",
        "presentation_short_vi": "Hang Shulgan-Tash, còn gọi là hang Kapova, là hang đá vôi nổi tiếng bên sông Belaya, nơi lưu giữ những bức tranh trong hang có niên đại tới hàng chục nghìn năm. Năm 2025, di sản này được UNESCO công nhận là Di sản Thế giới nhờ bộ tranh thời kỳ đồ đá cũ hiếm có.",
        "presentation_long_vi": "Nằm sâu trong khu bảo tồn thiên nhiên cùng tên bên tả ngạn sông Belaya, hang Shulgan-Tash là một trong những hang động nổi tiếng nhất nước Nga. Đây là hệ hang đá vôi ba tầng dài khoảng ba ki-lô-mét, có cả sông và hồ ngầm, nhưng điều làm nên danh tiếng của nó là hơn 190 bức vẽ thời kỳ đồ đá cũ. Các hình voi ma mút, ngựa hoang, tê giác, bò rừng và cả một con lạc đà hai bướu độc nhất được vẽ bằng thổ hoàng đỏ, có niên đại ước tính từ khoảng 14.500 đến hơn 36.000 năm trước. Với người Bashkir, hang gắn liền với truyền thuyết về Shulgan, vị thần cai quản thế giới ngầm, nên nơi đây vừa là kỳ quan khảo cổ vừa là chốn linh thiêng. Từ năm 2003, để bảo vệ các bức vẽ gốc khỏi hư hại, ban quản lý đã dựng bản sao ngay tại sảnh vào, còn phần hang chứa tranh thật được đóng lại. Du khách tham quan theo tour có hướng dẫn, khám phá những gian hang rộng lớn và nghe kể về lịch sử phát hiện. Vì hang nằm xa Ufa và giữa thiên nhiên hoang sơ, một chuyến ghé thăm thường trọn cả ngày, kết hợp cùng khu nuôi ong rừng và bảo tàng của khu bảo tồn.",
        "highlights_vi": [
            "Bộ tranh hang động thời đồ đá cũ với voi ma mút, ngựa, tê giác và cả hình lạc đà hai bướu độc nhất",
            "Được UNESCO ghi danh Di sản Thế giới năm 2025",
            "Hệ hang ba tầng dài khoảng 3 km với sông và hồ ngầm"
        ],
        "practical": {
            "hours_vi": "Mở cửa quanh năm, các tour thường bắt đầu từ 11:00; nên đặt trước qua ban quản lý khu bảo tồn.",
            "ticket_vi": "Khoảng 240–500 RUB tùy mùa và ngày trong tuần; tour dài đặc biệt tới 4.500–5.000 RUB; trẻ nhỏ và người cao tuổi được giảm giá.",
            "duration_vi": "Riêng tham quan hang khoảng 2–3 giờ; trọn chuyến từ Ufa thường mất cả ngày.",
            "best_time_vi": "Mùa hè (tháng 6–9) khi đường vào thuận lợi và có thêm tour dài.",
            "tips_vi": "Mang áo ấm vì trong hang lạnh; du khách chủ yếu xem tranh bản sao ở sảnh ngoài; kết hợp thăm khu nuôi ong rừng và bảo tàng của khu bảo tồn."
        },
        "photo_file": "File:Шульган-Таш летом.JPG",
        "official_site": "https://shulgan-tash.ru",
        "tags": ["cave", "unesco", "rock-art", "prehistory", "nature", "archaeology"]
    },
    {
        "region": "bashkortostan",
        "slug": "salavat-yulaev-monument",
        "name_vi": "Tượng đài Salavat Yulaev",
        "name_ru": "Памятник Салавату Юлаеву",
        "name_en": "Monument to Salavat Yulaev",
        "categories": ["monument"],
        "lat": 54.719444,
        "lon": 55.923889,
        "address_vi": "Quảng trường bên bờ cao sông Belaya (Agidel), trung tâm thành phố Ufa, Cộng hòa Bashkortostan, Nga",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Du khách gần như nhất trí xem đây là điểm phải ghé ở Ufa, ấn tượng với dáng tượng uy nghi và tầm nhìn tuyệt đẹp ra sông Belaya, đặc biệt lúc hoàng hôn. Nhiều người coi bức tượng là niềm tự hào và biểu tượng tinh thần của người Bashkir.",
        "presentation_short_vi": "Tượng đài Salavat Yulaev là biểu tượng của thành phố Ufa và cả Cộng hòa Bashkortostan, khắc họa người anh hùng dân tộc Bashkir cưỡi ngựa hiên ngang. Đây được xem là một trong những tượng kỵ sĩ lớn nhất nước Nga, dựng trên bờ cao nhìn ra sông Belaya.",
        "presentation_long_vi": "Sừng sững trên vách cao bên sông Belaya, tượng đài Salavat Yulaev là hình ảnh quen thuộc nhất mỗi khi người ta nhắc đến Ufa. Nhân vật được tôn vinh là Salavat Yulaev (1754–1800), nhà thơ kiêm chiến binh, người anh hùng dân tộc Bashkir đã cùng nghĩa quân Pugachev nổi dậy chống chế độ Nga hoàng trong những năm 1773–1775. Bức tượng đồng được khánh thành năm 1967, là tâm huyết gần ba mươi năm của nhà điêu khắc Soslanbek Tavasiev. Tượng cao 9,8 mét, nặng khoảng 40 tấn, thuộc hàng những tượng kỵ sĩ lớn nhất nước Nga và châu Âu. Điều khiến giới kỹ thuật nể phục là toàn bộ khối tượng đồ sộ chỉ tựa trên ba điểm đỡ, tạo dáng con ngựa đang chồm lên đầy khí thế. Hình ảnh người kỵ sĩ vung roi đã trở thành biểu tượng in trên quốc huy Cộng hòa Bashkortostan và được xếp vào 'Bảy kỳ quan của Bashkortostan'. Đứng dưới chân tượng, du khách có thể phóng tầm mắt bao quát dòng Belaya uốn lượn và cả một vùng thành phố. Đây cũng là nơi người dân tụ họp, chụp ảnh và tổ chức sự kiện, nhất là vào những buổi chiều tà khi ánh nắng nhuộm vàng bức tượng.",
        "highlights_vi": [
            "Tượng kỵ sĩ bằng đồng cao 9,8 m, nặng 40 tấn, thuộc hàng lớn nhất nước Nga",
            "Kỳ công kỹ thuật khi cả khối tượng chỉ tựa trên ba điểm đỡ",
            "Hình ảnh tượng đài xuất hiện trên quốc huy Cộng hòa Bashkortostan"
        ],
        "practical": {
            "hours_vi": "Ngoài trời, tham quan tự do mọi thời điểm trong ngày.",
            "ticket_vi": "Miễn phí.",
            "duration_vi": "Khoảng 20–40 phút.",
            "best_time_vi": "Chiều muộn và hoàng hôn khi ánh sáng đẹp; mùa ấm dễ dạo bộ bên bờ sông.",
            "tips_vi": "Kết hợp dạo quảng trường, Congress Hall và bờ kè; đây là điểm ngắm toàn cảnh sông Belaya lý tưởng để chụp ảnh."
        },
        "photo_file": "File:Ufa. Monument to Salavat Yulaev.jpg",
        "official_site": None,
        "tags": ["monument", "history", "viewpoint", "landmark", "bashkir"]
    },
    {
        "region": "bashkortostan",
        "slug": "toratau-shikhan",
        "name_vi": "Núi Toratau (shikhan Toratau)",
        "name_ru": "Шихан Торатау (Тратау)",
        "name_en": "Toratau Shikhan",
        "categories": ["other", "park_garden"],
        "lat": 53.554444,
        "lon": 56.098889,
        "address_vi": "Gần thành phố Ishimbay, phía nam Sterlitamak, Cộng hòa Bashkortostan, Nga (bên sông Belaya)",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Nhiều du khách mô tả Toratau là ngọn núi 'phải leo một lần', khen cảnh quan hùng vĩ và cảm giác chinh phục dù dốc khá đứng. Người ta cũng nhắc đến bầu không khí linh thiêng, lịch sử bi thương dưới chân núi và nỗi lo về nguy cơ bị khai thác.",
        "presentation_short_vi": "Toratau là ngọn núi đơn độc hình chóp nổi bật giữa đồng bằng Bashkiria, thực chất là dấu tích của một rạn san hô cổ hàng trăm triệu năm. Với hình dáng độc đáo và ý nghĩa thiêng liêng, đây là một trong những biểu tượng thiên nhiên được yêu mến nhất vùng.",
        "presentation_long_vi": "Nhô lên cô độc giữa đồng bằng bên sông Belaya, Toratau là một 'shikhan' điển hình — kiểu đồi đơn lẻ đặc trưng của Bashkiria. Nhìn xa như một kim tự tháp tự nhiên, nhưng thực chất ngọn núi là tàn tích của một rạn san hô hình thành trong lòng biển ấm cách nay gần 300 triệu năm, nên đá vôi ở đây chứa đầy hóa thạch sinh vật biển cổ. Đỉnh núi cao khoảng 338 mét so với mực nước biển và vươn chừng 220 mét trên mặt sông Belaya, đủ để ban tặng cho người leo một tầm nhìn bao quát cả thung lũng. Với người Bashkir, Toratau từ lâu được coi là ngọn núi thiêng, gắn với truyền thuyết và tín ngưỡng bản địa. Dưới chân núi là hồ Tugar-Salgan với hệ thực vật quý hiếm, đồng thời còn lưu dấu vết một trại giam thời Xô Viết — mảng lịch sử u ám ít người biết. Những năm gần đây, Toratau trở thành tâm điểm chú ý khi bị đe dọa khai thác làm nguyên liệu, giống số phận của ngọn Shakhtau kế bên đã gần như bị san phẳng; nhờ vị thế di tích thiên nhiên được bảo vệ, núi vẫn được giữ gìn. Đường lên tuy ngắn nhưng khá dốc, phần thưởng là khung cảnh và cảm giác đứng trên một kỳ quan địa chất sống động.",
        "highlights_vi": [
            "Rạn san hô cổ gần 300 triệu năm, nay là ngọn núi đá vôi đầy hóa thạch",
            "Đỉnh cao khoảng 338 m cho tầm nhìn bao quát thung lũng sông Belaya",
            "Ngọn núi thiêng của người Bashkir, dưới chân có hồ Tugar-Salgan và dấu tích trại giam cũ"
        ],
        "practical": {
            "hours_vi": "Ngoài trời, tự do tham quan cả ngày.",
            "ticket_vi": "Miễn phí.",
            "duration_vi": "Khoảng 2–3 giờ, gồm leo lên đỉnh và nghỉ ngắm cảnh.",
            "best_time_vi": "Cuối xuân đến đầu thu; nên leo vào sáng sớm hoặc chiều mát.",
            "tips_vi": "Đi giày bám tốt vì đường dốc và trơn; mang đủ nước; ghé hồ Tugar-Salgan dưới chân núi; tránh ngày mưa gió."
        },
        "photo_file": "File:Shihan Toratau.jpg",
        "official_site": None,
        "tags": ["mountain", "geology", "nature", "viewpoint", "hiking", "sacred"]
    },
    {
        "region": "bashkortostan",
        "slug": "iremel-mountain",
        "name_vi": "Núi Iremel",
        "name_ru": "Гора Иремель",
        "name_en": "Mount Iremel",
        "categories": ["other", "park_garden"],
        "lat": 54.515000,
        "lon": 58.840000,
        "address_vi": "Công viên thiên nhiên Iremel, huyện Beloretsk, Cộng hòa Bashkortostan, Nga (giáp tỉnh Chelyabinsk, dãy Nam Ural)",
        "rating": {"value": None, "count": None, "source": "Yandex Карты", "as_of": "2026-07"},
        "review_summary_vi": "Người leo núi ca ngợi khung cảnh choáng ngợp và cảm giác thiêng liêng trên đường lên đỉnh, dù chặng đường dài và thời tiết thất thường. Nhiều người khuyên chuẩn bị kỹ thể lực, trang phục và nhớ đăng ký tại trạm kiểm soát của công viên.",
        "presentation_short_vi": "Iremel là đỉnh núi cao thứ hai của dãy Nam Ural, được người Bashkir tôn kính như một ngọn núi thiêng. Cảnh quan hùng vĩ với rừng taiga, đồng cỏ núi cao và biển đá trên đỉnh khiến nơi đây trở thành điểm leo núi được yêu thích.",
        "presentation_long_vi": "Cao 1.582 mét, Iremel là đỉnh núi cao thứ hai của dãy Nam Ural, chỉ đứng sau Yamantau. Từ bao đời nay, người Bashkir xem đây là ngọn núi thiêng — một nơi 'tiếp thêm sức mạnh', và ngày nay núi vẫn thu hút cả người leo núi lẫn những ai tìm kiếm sự tĩnh tại. Toàn bộ khu vực nằm trong Công viên thiên nhiên Iremel, thành lập năm 2010, rộng gần 50.000 héc-ta với nhiều tuyến đường và các trạm kiểm soát ở lối vào. Cung leo kinh điển xuất phát từ làng Tyulyuk, dài khoảng mười lăm ki-lô-mét mỗi chiều, dẫn du khách qua rừng taiga rậm rạp, những đồng cỏ núi cao rồi lên tới đỉnh phủ đầy đá tảng khổng lồ. Ở độ cao này, khí hậu khắc nghiệt và thay đổi rất nhanh: mây mù có thể ập đến bất chợt, và tuyết đôi khi còn đọng lại ngay giữa mùa hè. Bù lại, người chinh phục được tưởng thưởng bằng biển mây, thảm thực vật vùng đài nguyên núi cao và cảm giác đứng trên nóc nhà của Bashkiria. Nhiều người đi trong ngày, số khác cắm trại qua đêm để đón bình minh. Dù đi kiểu nào, Iremel cũng đòi hỏi sự chuẩn bị nghiêm túc và thái độ trân trọng dành cho một vùng núi được coi là linh thiêng.",
        "highlights_vi": [
            "Đỉnh cao 1.582 m — nóc nhà thứ hai của dãy Nam Ural",
            "Ngọn núi thiêng gắn với truyền thuyết 'tiếp thêm sức mạnh' của người Bashkir",
            "Đỉnh là biển đá tảng, quanh năm có thể gặp tuyết ngay cả mùa hè"
        ],
        "practical": {
            "hours_vi": "Là công viên thiên nhiên; leo núi vào ban ngày, cần đăng ký hoặc qua trạm kiểm soát.",
            "ticket_vi": "Phí vào công viên nhỏ tại các trạm (khoảng vài trăm RUB); một số tuyến cần giấy phép.",
            "duration_vi": "Cả ngày (khoảng 8–12 giờ khứ hồi theo tuyến Tyulyuk); có thể cắm trại qua đêm.",
            "best_time_vi": "Tháng 6–9 khô ráo; mùa đông chỉ dành cho người có kinh nghiệm.",
            "tips_vi": "Mang giày leo núi, áo ấm và áo mưa; thời tiết đổi rất nhanh; tôn trọng tập tục vùng núi thiêng; nên đi theo nhóm hoặc có hướng dẫn."
        },
        "photo_file": "File:Mount Iremel.jpg",
        "official_site": None,
        "tags": ["mountain", "hiking", "nature", "sacred", "viewpoint", "nature-park"]
    },
    {
        "region": "bashkortostan",
        "slug": "askynskaya-ice-cave",
        "name_vi": "Hang băng Askynskaya (Hang băng Askinskaya)",
        "name_ru": "Аскинская ледяная пещера",
        "name_en": "Askynskaya Ice Cave",
        "categories": ["other", "park_garden"],
        "lat": 54.235694,
        "lon": 56.902833,
        "address_vi": "Gần làng Solontsy, huyện Arkhangelsk, Cộng hòa Bashkortostan, Nga (cách Ufa khoảng 130–150 km)",
        "rating": {"value": None, "count": None, "source": "Yandex Карты", "as_of": "2026-07"},
        "review_summary_vi": "Du khách sửng sốt trước những khối băng trong suốt khổng lồ và bầu không khí như bước vào cung điện băng. Nhiều người nhắc nhở đường vào hơi khó tìm, sàn băng trơn trượt và cần giữ gìn để không làm hư hại lớp băng mong manh.",
        "presentation_short_vi": "Hang băng Askynskaya là một hang đá vôi độc đáo, nơi quanh năm lạnh âm độ và lưu giữ những cột băng khổng lồ cổ xưa. Đây được xem là hang băng lớn nhất vùng Ural, với cột băng cao tới hơn chục mét như trong xứ sở thần tiên.",
        "presentation_long_vi": "Ẩn mình trong một sườn đồi rừng ở huyện Arkhangelsk, hang băng Askynskaya (còn phiên là Askinskaya) là một trong những kỳ quan thiên nhiên lạ lùng nhất Bashkiria. Khác với nhiều hang động khác, Askynskaya chỉ gồm một gian lớn duy nhất: dài khoảng 104 mét, rộng tới 61 mét và sâu chừng 26 mét. Nhờ cấu tạo như một cái 'bẫy lạnh', không khí băng giá bị giữ lại khiến nhiệt độ trong hang luôn ở mức âm 4°C suốt cả năm. Chính điều kiện đặc biệt đó đã nuôi dưỡng một khối băng cổ tồn tại hàng nghìn năm, với những cột và măng băng cao từ 8 đến 11 mét; cột băng lớn nhất vươn tới khoảng 15 mét, gần chạm trần hang như một ngọn tháp pha lê. Ánh sáng lọt vào phản chiếu qua lớp băng trong suốt tạo nên khung cảnh huyền ảo khiến ai cũng ngỡ ngàng. Được xếp hạng di tích thiên nhiên và mệnh danh là hang băng lớn nhất vùng Ural, Askynskaya từ xưa đã bao phủ một màu sắc huyền thoại. Vì băng rất dễ tổn thương, du khách được khuyến khích đi theo tour có hướng dẫn, chỉ ngắm nhìn mà không chạm hay leo trèo. Đường đến hang phải băng qua đoạn rừng, nên chuyến đi thường gộp chung thành một ngày trọn vẹn từ Ufa.",
        "highlights_vi": [
            "Cột băng khổng lồ cao khoảng 15 m, gần chạm tới trần hang",
            "Nhiệt độ âm 4°C quanh năm, giữ nguyên khối băng cổ như một sông băng tí hon",
            "Hang băng lớn nhất vùng Ural, được xếp hạng di tích thiên nhiên"
        ],
        "practical": {
            "hours_vi": "Ngoài trời, không có gác cổng; nên đi ban ngày và theo tour có hướng dẫn.",
            "ticket_vi": "Miễn phí nếu tự tham quan; tour trọn gói từ Ufa có tính phí riêng.",
            "duration_vi": "Tham quan hang khoảng 30–60 phút; trọn chuyến từ Ufa mất cả ngày.",
            "best_time_vi": "Cuối đông đến đầu xuân (tháng 2–5) khi băng dày và đẹp nhất.",
            "tips_vi": "Mặc ấm và đi giày chống trượt vì trong hang âm độ, băng rất trơn; mang đèn pin; tuyệt đối không trèo hay đập vào các cột băng."
        },
        "photo_file": None,
        "official_site": None,
        "tags": ["ice-cave", "cave", "nature", "winter", "geology"]
    },
    {
        "region": "bashkortostan",
        "slug": "lala-tulpan-mosque",
        "name_vi": "Thánh đường Hồi giáo Lyalya-Tyulpan (Lala Tulpan)",
        "name_ru": "Мечеть Ляля-Тюльпан",
        "name_en": "Lala Tulpan Mosque",
        "categories": ["church"],
        "lat": 54.819720,
        "lon": 56.055830,
        "address_vi": "Phố Komarova, thành phố Ufa, Cộng hòa Bashkortostan, Nga",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Du khách yêu thích kiến trúc độc đáo, hiện đại và khuôn viên yên bình của thánh đường, xem đây là một trong những điểm nhận diện của Ufa. Khách được đón tiếp thân thiện, với lưu ý nên ăn mặc kín đáo và giữ trật tự vì đây là nơi thờ tự đang hoạt động.",
        "presentation_short_vi": "Lyalya-Tyulpan, nghĩa là 'đóa uất kim hương đang nở', là thánh đường Hồi giáo hiện đại nổi bật nhất Ufa với hai tháp minaret hình nụ hoa tulip. Hoàn thành năm 1998, công trình là biểu tượng cho sự hồi sinh của đạo Hồi ở Bashkortostan.",
        "presentation_long_vi": "Giữa lòng Ufa, thánh đường Lyalya-Tyulpan gây ấn tượng ngay từ cái tên đầy chất thơ: trong tiếng Bashkir, 'Lyalya-Tyulpan' có nghĩa là đóa uất kim hương đang hé nở. Ý tưởng ấy được kiến trúc sư Wakil Davlyatshin thể hiện tài tình qua hai tháp minaret cao 53 mét vươn lên như hai nụ hoa, cùng phần ốp gạch đỏ và xanh gợi liên tưởng đến những cánh tulip chớm bung — biểu tượng của mùa xuân và sự tái sinh trong văn hóa các dân tộc Turk. Được xây dựng trong thập niên 1990 và khánh thành năm 1998, đây không chỉ là nơi cầu nguyện mà còn là một quần thể thánh đường kiêm trường học medrese, có phòng học và thư viện, với sảnh cầu nguyện đủ chỗ cho khoảng một nghìn tín đồ. Ra đời sau nhiều thập niên tôn giáo bị kìm hãm, công trình trở thành biểu tượng cho sự hồi sinh của đời sống Hồi giáo ở Bashkortostan và là một trong những thánh đường hiện đại dễ nhận biết nhất nước Nga. Lyalya-Tyulpan cũng góp phần khắc họa bản sắc đa tôn giáo của Ufa, nơi những mái vòm Hồi giáo và tháp chuông Chính thống giáo cùng tồn tại. Du khách thuộc mọi tín ngưỡng đều được chào đón đến chiêm ngưỡng, chỉ cần giữ thái độ tôn trọng nơi thờ tự.",
        "highlights_vi": [
            "Hai tháp minaret cao 53 m tạo hình nụ hoa uất kim hương đang hé nở",
            "Quần thể thánh đường kiêm trường học medrese, hoàn thành năm 1998",
            "Biểu tượng cho sự hồi sinh của văn hóa Hồi giáo ở Bashkortostan"
        ],
        "practical": {
            "hours_vi": "Mở cửa hằng ngày; khách tham quan nên đến ngoài giờ hành lễ, thường vào ban ngày.",
            "ticket_vi": "Miễn phí.",
            "duration_vi": "Khoảng 30–45 phút.",
            "best_time_vi": "Ban ngày; mùa xuân khi ý tưởng 'hoa tulip nở' càng thêm ý nghĩa; tránh trưa thứ Sáu.",
            "tips_vi": "Ăn mặc kín đáo, nữ nên trùm khăn; cởi giày khi vào; giữ im lặng và xin phép trước khi chụp ảnh bên trong."
        },
        "photo_file": "File:Lala Tulpan.jpg",
        "official_site": None,
        "tags": ["mosque", "architecture", "religion", "landmark", "islam"]
    },
    {
        "region": "bashkortostan",
        "slug": "pavlovka-reservoir",
        "name_vi": "Hồ chứa Pavlovka (Hồ Pavlovskoye)",
        "name_ru": "Павловское водохранилище",
        "name_en": "Pavlovka Reservoir",
        "categories": ["other", "park_garden"],
        "lat": 55.416700,
        "lon": 56.633300,
        "address_vi": "Trên sông Ufa, gần làng Pavlovka, huyện Nurimanov/Karaidel, Cộng hòa Bashkortostan, Nga (cách Ufa khoảng 90–115 km về phía đông bắc)",
        "rating": {"value": None, "count": None, "source": "Yandex Карты", "as_of": "2026-07"},
        "review_summary_vi": "Du khách khen cảnh sông hồ trong lành, không khí thư giãn và điều kiện câu cá tuyệt vời cả mùa hè lẫn mùa đông. Nhiều gia đình chọn nghỉ vài ngày ở các khu du lịch ven hồ, dù chất lượng dịch vụ giữa các cơ sở có thể chênh lệch.",
        "presentation_short_vi": "Hồ chứa Pavlovka là hồ nhân tạo dài hơn 150 km trên sông Ufa, hình thành từ đập thủy điện Pavlovka. Với mặt nước rộng giữa những sườn đồi rừng, đây là thiên đường nghỉ dưỡng, câu cá và chèo thuyền được người dân Bashkiria ưa chuộng.",
        "presentation_long_vi": "Trải dài hơn 150 ki-lô-mét trên sông Ufa, hồ chứa Pavlovka hình thành khi con đập của nhà máy thủy điện Pavlovka chặn dòng, biến khúc sông thành một hồ nước mênh mông len lỏi giữa những sườn đồi đá vôi phủ rừng thông. Khung cảnh sông núi trùng điệp khiến nơi đây được nhiều người trìu mến gọi là 'Thụy Sĩ của Bashkiria'. Dọc hai bờ hồ mọc lên hàng loạt khu nghỉ dưỡng, nhà nghỉ (turbaza) và điều dưỡng, phục vụ dòng du khách tìm về từ Ufa và các thành phố lân cận mỗi dịp cuối tuần hay kỳ nghỉ. Pavlovka đặc biệt nổi tiếng với dân câu cá: mặt hồ dồi dào cá măng, cá vược, cá tráp và nhiều loài khác, câu được cả mùa hè lẫn mùa đông khi mặt nước đóng băng. Ngoài câu cá, du khách còn có thể tắm, chèo thuyền, lặn, chơi các môn thể thao nước hoặc đơn giản là thả mình vào thiên nhiên yên tĩnh. Gần đó là suối karst Krasny Klyuch — một trong những mạch nước ngầm lớn nhất nước Nga và cũng là điểm tham quan hấp dẫn. Với sự kết hợp giữa cảnh quan, không khí trong lành và tiện nghi nghỉ dưỡng, Pavlovka là lựa chọn lý tưởng cho một kỳ nghỉ thư giãn gần gũi thiên nhiên.",
        "highlights_vi": [
            "Hồ nhân tạo dài hơn 150 km trên sông Ufa, tạo bởi đập thủy điện Pavlovka",
            "Điểm câu cá, chèo thuyền và nghỉ dưỡng bậc nhất Bashkiria với nhiều khu turbaza",
            "Cảnh quan đồi rừng đá vôi, gần suối karst khổng lồ Krasny Klyuch"
        ],
        "practical": {
            "hours_vi": "Khu vực ngoài trời, tham quan tự do; các khu nghỉ có giờ giấc và dịch vụ riêng.",
            "ticket_vi": "Vào khu vực hồ miễn phí; lưu trú, thuê thuyền và câu cá tại turbaza có tính phí.",
            "duration_vi": "Từ một ngày đến vài ngày nếu nghỉ dưỡng.",
            "best_time_vi": "Mùa hè để tắm, chèo thuyền, câu cá; mùa đông cho câu cá trên băng.",
            "tips_vi": "Đặt turbaza trước vào cao điểm hè; mang theo đồ câu; kết hợp ghé suối Krasny Klyuch; đi xe riêng từ Ufa là thuận tiện nhất."
        },
        "photo_file": "File:Pavlovka reservoir.jpg",
        "official_site": None,
        "tags": ["reservoir", "nature", "fishing", "recreation", "boating", "lake"]
    },
    {
        "region": "bashkortostan",
        "slug": "sterlitamak-shikhans",
        "name_vi": "Cụm núi shikhan Sterlitamak",
        "name_ru": "Стерлитамакские шиханы",
        "name_en": "Sterlitamak Shikhans",
        "categories": ["other", "park_garden"],
        "lat": 53.689781,
        "lon": 56.077161,
        "address_vi": "Chuỗi đồi ven sông Belaya quanh thành phố Sterlitamak và Ishimbay, Cộng hòa Bashkortostan, Nga",
        "rating": {"value": None, "count": None, "source": "Yandex Карты", "as_of": "2026-07"},
        "review_summary_vi": "Du khách xem cụm shikhan là kỳ quan địa chất hiếm có, thích leo Yuraktau hay Kushtau để ngắm toàn cảnh và tìm hiểu câu chuyện bảo vệ Kushtau. Nhiều người tiếc nuối trước cảnh Shakhtau bị khai thác và trân trọng nỗ lực gìn giữ những ngọn còn lại.",
        "presentation_short_vi": "Các shikhan Sterlitamak là chuỗi những ngọn đồi đơn độc kỳ lạ nhô lên bên sông Belaya, vốn là tàn tích của rạn san hô cổ gần 300 triệu năm. Bốn ngọn nổi tiếng — Toratau, Yuraktau, Kushtau và Shakhtau — là biểu tượng địa chất và tinh thần của vùng.",
        "presentation_long_vi": "Bên bờ sông Belaya gần thành phố Sterlitamak, một chuỗi những ngọn đồi đơn độc nhô lên đột ngột khỏi đồng bằng, kéo dài chừng 20 ki-lô-mét và được gọi là các 'shikhan'. Điều kỳ diệu là mỗi ngọn đồi đều là tàn tích của một rạn san hô hình thành trong biển ấm cách nay khoảng 280–300 triệu năm, khiến lớp đá vôi chứa đầy hóa thạch sinh vật biển cổ. Bốn shikhan nổi danh nhất là Toratau, Yuraktau, Kushtau và Shakhtau. Đáng buồn thay, Shakhtau gần như đã bị san phẳng vì bị khai thác từ năm 1950 làm nguyên liệu cho ngành sản xuất soda, để lại một hố mỏ khổng lồ thay cho ngọn núi. Số phận tương tự từng đe dọa Kushtau, nhưng vào năm 2020, làn sóng phản kháng ôn hòa của người dân đã buộc chính quyền dừng kế hoạch khai thác và trao cho ngọn núi quy chế bảo vệ — biến Kushtau (nơi còn có khu trượt tuyết) thành biểu tượng của phong trào bảo vệ môi trường ở Nga. Yuraktau là ngọn gần Sterlitamak nhất, còn Toratau nằm về phía nam gần Ishimbay. Được đưa vào danh sách dự kiến của UNESCO và các bảng bình chọn kỳ quan, cụm shikhan vừa là bảo tàng địa chất ngoài trời, vừa là nơi lý tưởng để leo núi ngắm toàn cảnh.",
        "highlights_vi": [
            "Chuỗi đồi là rạn san hô cổ gần 300 triệu năm, đầy hóa thạch biển",
            "Kushtau trở thành biểu tượng bảo vệ môi trường sau cuộc phản kháng năm 2020",
            "Shakhtau gần như bị san phẳng vì khai thác làm nguyên liệu sản xuất soda"
        ],
        "practical": {
            "hours_vi": "Ngoài trời, tự do tham quan cả ngày.",
            "ticket_vi": "Miễn phí (Kushtau có khu trượt tuyết thu phí dịch vụ vào mùa đông).",
            "duration_vi": "Nửa ngày đến cả ngày để thăm 2–3 shikhan.",
            "best_time_vi": "Cuối xuân đến đầu thu để leo núi; mùa đông trượt tuyết ở Kushtau.",
            "tips_vi": "Kết hợp leo Yuraktau và Kushtau gần Sterlitamak; đi giày bám tốt và mang nước; Toratau ở phía nam gần Ishimbay có thể thăm riêng."
        },
        "photo_file": None,
        "official_site": None,
        "tags": ["geology", "nature", "hiking", "viewpoint", "mountain", "environment"]
    }
]

out_path = os.path.join(os.path.dirname(__file__), "..", "_incoming", "reg_bashkortostan.json")
out_path = os.path.abspath(out_path)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

# Validation / reporting
allowed = {"museum","palace","church","fortress","monument","park_garden","bridge","square_street","theatre","other"}
null_fields = []
for r in records:
    for cat in r["categories"]:
        assert cat in allowed, f"BAD CATEGORY {cat} in {r['slug']}"
    assert len(r["highlights_vi"]) == 3, f"highlights != 3 in {r['slug']}"
    assert set(r["practical"].keys()) == {"hours_vi","ticket_vi","duration_vi","best_time_vi","tips_vi"}, r["slug"]
    wc = len(r["presentation_long_vi"].split())
    if r["rating"]["value"] is None:
        null_fields.append(f"{r['slug']}: rating.value")
    if r["rating"]["count"] is None:
        null_fields.append(f"{r['slug']}: rating.count")
    if r["photo_file"] is None:
        null_fields.append(f"{r['slug']}: photo_file")
    if r["official_site"] is None:
        null_fields.append(f"{r['slug']}: official_site")
    print(f"{r['slug']:26s} cats={r['categories']} long_words={wc} photo={'Y' if r['photo_file'] else 'null'} site={'Y' if r['official_site'] else 'null'}")

print("\nRecords:", len(records))
print("Wrote:", out_path)
print("\nNULL fields (", len(null_fields), "):")
for nf in null_fields:
    print("  -", nf)
