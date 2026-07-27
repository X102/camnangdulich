# -*- coding: utf-8 -*-
"""Builder: doc_smolny-cathedral.json — Nhà thờ Smolny (Saint Petersburg).
Nội dung biên soạn nguyên gốc tiếng Việt, tổng hợp từ nguồn công khai (xem 'sources').
"""
import json, os, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))

def img(fname, caption):
    url = "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(fname)
    return {"url": url, "caption": caption}

doc = {
    "slug": "smolny-cathedral",
    "name_vi": "Nhà thờ Smolny (Nhà thờ Phục Sinh của Tu viện Smolny)",
    "name_ru": "Смольный собор (Воскресения Христова)",
    "name_en": "Smolny Cathedral (Cathedral of the Resurrection)",
    "subtitle": "Kiệt tác Baroque xanh–trắng do Francesco Bartolomeo Rastrelli khởi công năm 1748 cho Nữ hoàng Elizaveta; số phận dở dang gần một thế kỷ, tháp chuông khổng lồ chưa bao giờ mọc lên, nhưng vẻ đẹp thanh thoát của nó vẫn được xem là một trong những công trình tôn giáo đẹp nhất nước Nga.",
    "sections": [],
    "highlights": [
        "Kiệt tác Baroque của Francesco Bartolomeo Rastrelli — cùng cha đẻ của Cung điện Mùa Đông và Cung điện Ekaterina — khởi công ngày 30/10/1748.",
        "Khởi nguồn từ ước nguyện đi tu của Nữ hoàng Elizaveta, con gái Pyotr Đại đế; quần thể được thiết kế làm tu viện cho các thiếu nữ quý tộc.",
        "Tháp chuông trung tâm dự kiến cao khoảng 140 m — nếu dựng xong sẽ là công trình cao nhất Nga thời đó — rốt cuộc không bao giờ được xây.",
        "Công trình kéo dài gần 90 năm, chỉ hoàn tất năm 1835 dưới tay kiến trúc sư Vasily Stasov với nội thất tân cổ điển sáng bừng.",
        "Đài quan sát trên tháp chuông (khoảng 50 m, 277 bậc) từng là điểm ngắm toàn cảnh cao nhất trong hệ thống bảo tàng thành phố.",
        "Được trả lại cho Giáo hội Chính thống Nga năm 2015; nay vừa là nhà thờ hoạt động vừa là không gian hòa nhạc nổi tiếng về âm học.",
    ],
    "images": [
        img("Smolny Convent.jpg", "Toàn cảnh Nhà thờ Smolny với sắc xanh da trời và trắng đặc trưng — dáng vẻ 'năm vòm' quây quần quanh vòm trung tâm."),
        img("061. St. Petersburg. Smolny Cathedral.jpg", "Mặt tiền Baroque tầng tầng lớp lớp của Rastrelli, nhìn từ Quảng trường Rastrelli."),
        img("Saint Petersburg Smolny Cathedral IMG 5855 1280.jpg", "Cụm vòm và tháp chuông áp sát nhau tạo hiệu ứng thị giác vươn cao đặc trưng của Smolny."),
        img("Smolny Cathedral of Resurration of Christ, interior.JPG", "Nội thất tân cổ điển do Stasov hoàn thiện năm 1835 — trắng, cao và tràn ngập ánh sáng."),
        img("Smolny Cathedral of Resurration of Christ, interior, iconostasis.JPG", "Gian trong nhà thờ với sắc trắng chủ đạo, tương phản với vẻ lộng lẫy Baroque bên ngoài."),
    ],
    "references": [
        {"title": "Smolny Convent — Wikipedia (tiếng Anh)", "url": "https://en.wikipedia.org/wiki/Smolny_Convent"},
        {"title": "Smolny Institute — Wikipedia (tiếng Anh)", "url": "https://en.wikipedia.org/wiki/Smolny_Institute"},
        {"title": "The Smolny Cathedral — Saint-Petersburg.com", "url": "http://www.saint-petersburg.com/cathedrals/smolny-cathedral/"},
        {"title": "Smolny Cathedral — VisitRussia", "url": "https://visitrussia.com/citiesguide/spb/places/smolny_cathedral"},
        {"title": "Smolny Monastery — A View On Cities", "url": "https://aviewoncities.com/st-petersburg/smolny-monastery"},
        {"title": "1748–64, Smolny Cathedral — Chronology of Architecture", "url": "https://chronologyofarchitecture.wordpress.com/2016/05/08/1748-64-smolny-cathedral/"},
        {"title": "Category: Smolny Cathedral — Wikimedia Commons (ảnh)", "url": "https://commons.wikimedia.org/wiki/Category:Smolny_Cathedral"},
    ],
    "sources": [
        "Wikipedia tiếng Anh, mục 'Smolny Convent' — lịch sử khởi công 1748, vai trò Nữ hoàng Elizaveta, tháp chuông dở dang, Stasov hoàn tất 1835, đóng cửa 1923, trả lại Giáo hội năm 2015, gốc gác tên gọi 'smola' (nhựa/hắc ín).",
        "Wikipedia tiếng Anh, mục 'Smolny Institute' — Viện Smolny (kiến trúc sư Quarenghi), trường nữ sinh quý tộc, đại bản doanh Bolshevik và nơi ở của Lenin năm 1917.",
        "Saint-Petersburg.com — mô tả chi tiết nội thất (cột cẩm thạch trắng, lan can pha lê, Hòm Giao ước bằng bạc, tranh Venetsianov), thông tin vé và giờ mở cửa, ga metro Chernyshevskaya.",
        "VisitRussia và A View On Cities — chiều cao 93,7 m, cấu trúc 'một vòm giả năm vòm', đài quan sát tháp chuông ~50 m với 277 bậc.",
        "Dữ liệu điểm đến nội bộ dự án 'Cẩm nang Du lịch Nga' — tên gọi, tọa độ, địa chỉ Quảng trường Rastrelli 3/1, tóm tắt đánh giá du khách.",
        "Ảnh minh họa: Wikimedia Commons, Category: Smolny Cathedral (giấy phép tự do).",
    ],
}

S = doc["sections"]

S.append({"heading": "Giới thiệu chung", "paras": [
    "Giữa muôn vàn cung điện và thánh đường của Saint Petersburg, Nhà thờ Smolny nổi lên như một nốt nhạc trong trẻo bậc nhất: một khối kiến trúc xanh da trời điểm trắng, vươn cao bên khúc quanh của sông Neva, nơi dòng nước rẽ về phía đông bắc thành phố. Tên đầy đủ của công trình là Nhà thờ Phục Sinh của Chúa (Voskresensky) thuộc Tu viện Nữ tu Smolny — nhưng với hầu hết du khách, người ta chỉ gọi giản dị là 'Smolny'. Đây là trái tim của cả một quần thể tu viện, được hình dung ngay từ đầu không phải như một nhà thờ đơn lẻ, mà như một tổ hợp khép kín gồm thánh đường trung tâm và các dãy nhà tu bao quanh.",
    "Điều khiến Smolny trở nên đặc biệt nằm ở sự tương phản giữa hai vẻ đẹp. Bên ngoài, đó là đỉnh cao của phong cách Baroque Nga thời Nữ hoàng Elizaveta: đường nét uốn lượn, cột trụ dồn dập, sắc xanh–trắng rực rỡ và cụm vòm mạ vàng lấp lánh dưới nắng. Bên trong, ngược lại, là một không gian tân cổ điển gần như trắng toát, cao vút, tràn ngập ánh sáng và tĩnh tại đến thanh thoát. Chính khoảng cách gần một thế kỷ giữa lúc khởi công và lúc hoàn thành đã tạo nên sự 'lệch pha' phong cách thú vị ấy — và cũng là một phần câu chuyện làm nên số phận độc đáo của công trình.",
    "Người thiết kế Smolny là Francesco Bartolomeo Rastrelli, kiến trúc sư trưởng của triều đình Elizaveta và là bậc thầy Baroque lừng danh nhất nước Nga thế kỷ 18. Cũng chính bàn tay ấy đã dựng nên Cung điện Mùa Đông, Cung điện Ekaterina ở Tsarskoye Selo và nhiều biểu tượng khác của kinh đô. Với nhiều nhà nghiên cứu, Smolny là tác phẩm mà Rastrelli dồn nhiều tâm huyết và tình cảm nhất, dẫu ông không có cơ hội nhìn thấy nó hoàn thành trọn vẹn.",
    "Số phận của Smolny gắn liền với những biến động của lịch sử Nga: khởi đầu từ ước nguyện đi tu của một nữ hoàng, đứt đoạn khi ngân khố cạn kiệt, hồi sinh dưới một triều đại và một khiếu thẩm mỹ khác, rồi trải qua thời kỳ Xô-viết với vai trò phòng hòa nhạc, để cuối cùng trở lại làm nơi thờ phượng. Ngày nay, công trình đảm nhiệm 'vai kép': vừa là nhà thờ Chính thống giáo có cử hành phụng vụ, vừa là một khán phòng hòa nhạc được yêu thích nhờ âm học tốt và không gian trang nghiêm.",
    "Với du khách, Smolny thường được nhắc đến như một trong những điểm đến 'đáng công đi xa hơn một chút'. Nó không nằm ngay trên trục trung tâm đông đúc quanh Đại lộ Nevsky, mà lùi về một góc yên tĩnh hơn của thành phố, nơi ít xô bồ và nhiều khoảng lặng. Đổi lại, người ta được chiêm ngưỡng một trong những mặt tiền đẹp nhất mà kiến trúc Nga từng sản sinh, lại thường ít phải chen chúc so với các thánh đường trứ danh khác.",
    "Trong khuôn khổ Cẩm nang Du lịch Nga, tài liệu này được biên soạn để phục vụ công tác thuyết minh nội bộ: cung cấp cho hướng dẫn viên và người làm nội dung một bức tranh đầy đủ về lịch sử, kiến trúc, ý nghĩa và trải nghiệm tham quan Smolny, kèm những mẩu chuyện có thể kể để bài thuyết minh thêm sống động. Toàn bộ nội dung được tổng hợp và diễn đạt lại bằng lời của nhóm biên soạn, có dẫn nguồn dữ kiện ở cuối bài.",
]})

S.append({"heading": "Vị trí & cách di chuyển", "paras": [
    "Nhà thờ Smolny tọa lạc tại Quảng trường Rastrelli số 3/1, ở phía đông bắc trung tâm lịch sử Saint Petersburg, ngay sát khúc uốn của sông Neva. Vị trí này nằm hơi tách khỏi cụm điểm tham quan quen thuộc quanh Cung điện Mùa Đông và Đại lộ Nevsky, nên nhịp độ ở đây yên ả hơn hẳn. Quảng trường mang tên chính người kiến trúc sư đã tạo ra công trình — một cách hậu thế tri ân Rastrelli.",
    "Ga tàu điện ngầm gần nhất là Chernyshevskaya (tuyến số 1, tuyến đỏ), cách nhà thờ khoảng 1,5–2 km, tương ứng chừng 20–25 phút đi bộ. Đây là quãng đường dễ chịu nếu thời tiết đẹp, đi dọc các con phố rợp cây và ngang qua khu vực Viện Smolny lịch sử. Với những ai ngại đi bộ, từ ga có thể bắt thêm xe buýt hoặc trolleybus đi vài chặng về hướng nhà thờ.",
    "Cách tiếp cận thuận tiện nhất với nhiều du khách là dùng xe buýt và trolleybus chạy dọc phố Suvorovsky và các trục lân cận, xuống ở trạm gần Quảng trường Smolny. Mạng lưới giao thông mặt đất ở khu vực này khá dày; ứng dụng bản đồ hoặc gọi xe công nghệ đều hoạt động tốt và thường là lựa chọn nhanh gọn nếu nhóm đi đông hoặc mang theo hành lý.",
    "Nếu di chuyển bằng taxi hay xe riêng, hành trình từ khu trung tâm quanh Nevsky thường chỉ mất 10–15 phút khi đường thông thoáng. Khu vực quanh nhà thờ tương đối rộng rãi, dễ dừng đỗ hơn so với lõi trung tâm chật chội. Đây cũng là điểm có thể ghép khéo vào lịch trình cùng Cung điện Tauride hay tu viện Alexander Nevsky ở phía nam.",
    "Một gợi ý cho người thích tản bộ: có thể kết hợp Smolny với một đoạn đi dạo dọc bờ kè sông Neva. Từ phía bờ sông và từ cầu Bolsheokhtinsky bắc qua Neva, du khách có được những góc nhìn rất đẹp về khối nhà thờ nổi bật trên nền trời — đặc biệt vào những ngày quang mây khi sắc xanh–trắng của công trình ăn rơ với màu trời.",
    "Về thời điểm, nên tránh sát giờ đóng cửa để còn đủ thời gian vừa vãn cảnh bên ngoài, vừa vào trong và (nếu mở) leo tháp chuông. Vào mùa 'đêm trắng' cuối tháng 6, ánh sáng ban ngày kéo dài gần như thâu đêm, giúp việc chụp ảnh và ngắm cảnh trở nên lý tưởng; còn mùa đông, nhà thờ ánh lên vẻ đẹp trầm mặc khác hẳn trên nền tuyết.",
]})

S.append({"heading": "Lịch sử hình thành và phát triển", "paras": [
    "Câu chuyện của Smolny bắt đầu từ một quyết định mang màu sắc cá nhân của Nữ hoàng Elizaveta Petrovna, con gái của Pyotr Đại đế. Sau những xáo trộn kế vị đầu thế kỷ 18, đã có lúc Elizaveta bị gạt khỏi ngai vàng và, theo các ghi chép, bà nuôi ý định lui về sống đời tu hành. Địa điểm được chọn để dựng tu viện chính là khu đất bên sông Neva mang tên 'Smolny' — nơi từng là bãi chưng cất nhựa thông, hắc ín phục vụ xưởng đóng tàu của Hải quân dưới thời Pyotr. Chữ 'smola' trong tiếng Nga nghĩa là nhựa/hắc ín, và cái tên dân dã ấy đã đi theo công trình đến tận ngày nay.",
    "Bước ngoặt xảy ra năm 1741, khi một cuộc đảo chính do đội cận vệ Preobrazhensky tiến hành đã lật đổ vị hoàng đế nhỏ tuổi Ivan VI và đưa Elizaveta lên ngôi. Từ một người định đi tu, bà trở thành nữ hoàng. Ý định khoác áo nữ tu không thành, nhưng dự án tu viện thì vẫn được xúc tiến — nay dưới sự bảo trợ hoàng gia và với quy mô tương xứng với một bậc quân vương. Công trình chính thức khởi công ngày 30 tháng 10 năm 1748, giao cho kiến trúc sư trưởng của triều đình là Rastrelli.",
    "Rastrelli hình dung một tổ hợp tráng lệ: thánh đường trung tâm theo lối 'năm vòm' truyền thống của Chính thống giáo, vây quanh là các dãy nhà tu, và điểm nhấn tham vọng nhất là một tháp chuông khổng lồ ở lối vào. Theo thiết kế, tháp chuông này cao khoảng 140 mét — nếu dựng xong, nó sẽ vượt cả gác chuông Nhà thờ Pyotr và Pavel để trở thành công trình cao nhất Saint Petersburg, thậm chí cao nhất nước Nga đương thời. Một mô hình gỗ đồ sộ của toàn bộ quần thể đã được chế tác để trình bày ý tưởng ấy, và mô hình này về sau trở thành hiện vật quý được lưu giữ.",
    "Nhưng lịch sử không chiều theo giấc mộng của người nghệ sĩ. Việc xây dựng ngốn ngân khố khổng lồ và tiến triển chậm chạp; đến khoảng năm 1761–1762, khi phần thân thánh đường cơ bản đã thành hình thì Nữ hoàng Elizaveta qua đời. Người kế vị, Nữ hoàng Ekaterina II (Catherine Đại đế), lại không ưa phong cách Baroque phồn thực mà chuộng sự tiết chế của tân cổ điển. Nguồn tài chính dành cho Smolny nhanh chóng cạn kiệt, tháp chuông vĩ đại bị gác lại vô thời hạn, còn Rastrelli thì bị cho thôi việc và rời nước Nga vào năm 1763.",
    "Trong nhiều thập niên sau đó, thánh đường đứng đó dở dang: bên ngoài gần như hoàn thiện nhưng nội thất vẫn trống trải, chưa được trang hoàng. Phải đến thập niên 1830, dưới thời Hoàng đế Nikolai I, số phận công trình mới sang trang. Năm 1832, nhà vua giao cho kiến trúc sư Vasily Stasov nhiệm vụ hoàn tất Smolny. Stasov tôn trọng dáng vẻ Baroque bên ngoài của Rastrelli, nhưng thiết kế phần nội thất theo tinh thần tân cổ điển đang thịnh hành — thanh thoát, sáng sủa, khác hẳn sự rậm rạp Baroque. Công trình được khánh thành và cung hiến ngày 22 tháng 7 năm 1835.",
    "Khi hoàn tất, bàn thờ chính của nhà thờ được dâng kính mầu nhiệm Phục Sinh của Chúa, còn hai bàn thờ phụ dâng kính Thánh Maria Magdalena và Thánh nữ Elizaveta — một cách tưởng nhớ vị nữ hoàng đã khai sinh dự án. Suốt phần còn lại của thế kỷ 19, Smolny hoạt động như một nhà thờ và gắn với các thiết chế giáo dục, từ thiện lân cận, trong đó nổi tiếng nhất là Viện Smolny dành cho các thiếu nữ quý tộc.",
    "Thời kỳ Xô-viết mang đến một chương gian nan. Các bảo vật của nhà thờ bị tịch thu đầu thập niên 1920, và đến năm 1923 thì Smolny bị đóng cửa. Trong nhiều năm, tòa nhà không được sưởi ấm, thiếu điện nước và dần xuống cấp; bức tường ngăn thánh (iconostasis) cũng bị tháo dỡ. Mãi về sau, công trình được trưng dụng làm không gian trưng bày rồi thành phòng hòa nhạc — vai trò giúp nó được bảo tồn và tiếp tục vang lên âm nhạc giữa lòng thành phố. Đến tháng 4 năm 2015, Smolny được trao trả cho Giáo hội Chính thống Nga; từ đó, nơi đây trở lại là một nhà thờ có cử hành phụng vụ, đồng thời vẫn giữ chức năng biểu diễn.",
]})

S.append({"heading": "Kiến trúc & đặc điểm nổi bật", "paras": [
    "Về tổng thể, Smolny là bản tuyên ngôn của phong cách Baroque Elizaveta — thứ Baroque Nga mang đậm dấu ấn Rastrelli với màu sắc tươi, khối hình bề thế và lớp trang trí dày đặc. Sắc xanh da trời phủ trên thân công trình, làm nền cho các chi tiết trắng của cột, phào, khung cửa và các mảng đắp nổi, trong khi những vòm mái ánh lên sắc vàng kim. Bảng màu ấy khiến nhà thờ như một món đồ sứ tinh xảo được đặt giữa trời, đặc biệt bắt mắt vào ngày nắng.",
    "Điểm tài hoa nhất trong thiết kế nằm ở cách Rastrelli xử lý cụm vòm. Nữ hoàng Elizaveta muốn giữ truyền thống 'năm vòm' vốn quen thuộc với nhà thờ Chính thống giáo Nga, nhưng Rastrelli lại thấm nhuần thẩm mỹ châu Âu. Ông dung hòa cả hai: nhìn từ xa, công trình hiện lên như một thánh đường năm vòm cổ điển; nhưng thực chất chỉ có một vòm trung tâm lớn, còn bốn 'vòm' còn lại là các tháp chuông nhỏ được đặt sát ngay chân vòm chính. Nhờ cách xếp đặt quây tụ này, cả cụm chóp như chụm lại và vươn lên thành một khối duy nhất — một hiệu ứng thị giác rất riêng, tạo cảm giác công trình đang bay lên khỏi mặt đất.",
    "Chiều cao của nhà thờ vào khoảng 93,7 mét — đủ để nó thống trị đường chân trời của cả khu vực đông bắc thành phố. Dù tháp chuông khổng lồ theo ý tưởng ban đầu không bao giờ được dựng, chính sự vắng mặt ấy lại vô tình khiến bố cục trở nên cô đọng và cân đối theo một cách khác: thánh đường tự nó là tâm điểm, không bị 'lấn át' bởi một cột tháp cao lênh khênh phía trước.",
    "Bao quanh thánh đường là các dãy nhà tu thấp, tạo thành một sân trong khép kín theo đúng ý tưởng tu viện. Lối vào khuôn viên từng được điểm bằng hàng rào gang uốn hình bán nguyệt với các trụ và cổng chạm trổ công phu — một chi tiết trang trí đặc trưng của thời kỳ, nay được nhắc đến trong nhiều mô tả lịch sử về công trình.",
    "Bước vào bên trong, du khách thường bất ngờ vì sự tương phản. Thay cho vẻ lộng lẫy Baroque của mặt tiền, nội thất do Stasov hoàn thiện lại theo tinh thần tân cổ điển: những mảng tường trắng, hàng cột cẩm thạch, không gian cao và mở, ánh sáng tự nhiên rót xuống khiến toàn bộ gian thờ như bừng sáng. Chính sự tiết chế màu sắc ấy tạo cảm giác thanh thoát, tĩnh lặng, nâng đỡ tâm thế chiêm niệm — rất khác các thánh đường lấp lánh vàng son khác của Nga.",
    "Các tư liệu lịch sử còn ghi lại rằng nội thất từng được trang hoàng bằng nhiều chi tiết quý: lan can pha lê cắt cạnh ở khu bàn thờ, cột và tường ốp cẩm thạch trắng, một Hòm Giao ước làm từ khối lượng bạc lớn, cùng nhiều bức icon và tranh tôn giáo — trong đó có tác phẩm 'Chúa Phục Sinh' của họa sĩ Aleksey Venetsianov. Nhiều bảo vật đã thất tán qua các biến động thế kỷ 20, nhưng bản thân kiến trúc và tinh thần của không gian vẫn được gìn giữ.",
    "Một đặc điểm được du khách hiện đại yêu thích là đài quan sát trên tháp chuông. Sau khi leo khoảng 277 bậc lên độ cao chừng 50 mét, người tham quan có thể phóng tầm mắt ra toàn cảnh sông Neva và các khu phố lịch sử — một trong những điểm ngắm thành phố ấn tượng, từng được giới thiệu như đài quan sát bảo tàng cao nhất Saint Petersburg.",
]})

S.append({"heading": "Những điểm nhấn không thể bỏ lỡ", "paras": [
    "Mặt tiền xanh–trắng nhìn từ Quảng trường Rastrelli: đây là 'bức ảnh để đời' của mọi chuyến thăm Smolny. Hãy dành thời gian đứng lùi ra xa để thu trọn cụm vòm quây tụ và lớp trang trí Baroque tầng tầng lớp lớp; ánh nắng xiên buổi sáng hoặc chiều làm nổi bật chiều sâu của các chi tiết đắp nổi.",
    "Cụm vòm 'giả năm vòm': hãy để ý cách vòm trung tâm và bốn tháp chuông nhỏ chụm sát nhau. Đây chính là 'ngón nghề' làm nên nét độc đáo của Smolny và là điểm nên chỉ ra khi thuyết minh — bởi thoạt nhìn ai cũng ngỡ là năm vòm cân xứng theo lối cổ điển.",
    "Nội thất trắng tân cổ điển: bước vào để cảm nhận sự đối lập giữa 'ngoài rực rỡ – trong thanh khiết'. Không gian cao, sáng và tĩnh là nơi lý tưởng để dừng lại đôi phút, cảm nhận âm học đặc biệt vốn khiến nơi đây trở thành phòng hòa nhạc.",
    "Đài quan sát tháp chuông: nếu sức khỏe cho phép và tháp đang mở cửa, đừng bỏ lỡ 277 bậc thang lên độ cao ~50 m. Phần thưởng là toàn cảnh sông Neva và những mái vòm, chóp tháp của thành phố trải dài phía dưới.",
    "Góc nhìn từ bờ sông Neva và cầu Bolsheokhtinsky: để thấy Smolny 'nổi' trên nền trời và mặt nước, hãy ra phía bờ kè. Đây là góc chụp toàn cảnh đẹp mà nhiều người bỏ qua khi chỉ loanh quanh trước cổng chính.",
    "Một buổi hòa nhạc (nếu có lịch): nghe nhạc cổ điển hoặc thánh ca vang lên dưới vòm trắng cao vút là trải nghiệm khó quên, kết hợp trọn vẹn giữa kiến trúc và âm thanh trong cùng một không gian.",
    "Mô hình gỗ và tư liệu về tháp chuông dang dở: nếu có dịp tiếp cận các tư liệu trưng bày hoặc hình ảnh phục dựng, hãy để ý hình dáng tháp chuông khổng lồ mà Rastrelli từng mơ ước. So sánh 'phiên bản lẽ ra' với công trình thực tế là cách tuyệt vời để hiểu tham vọng của người kiến trúc sư và những giới hạn mà lịch sử áp đặt.",
]})

S.append({"heading": "Ý nghĩa lịch sử – văn hoá", "paras": [
    "Smolny là một 'lát cắt' cô đọng của lịch sử nghệ thuật Nga: nó khởi sinh trong thời hoàng kim của Baroque Elizaveta và hoàn tất trong kỷ nguyên tân cổ điển, nên bản thân công trình đã kể lại sự chuyển giao thẩm mỹ giữa hai thời đại. Ít có công trình nào phô bày rõ đến thế cuộc 'đối thoại' giữa hai phong cách trên cùng một khối kiến trúc — Baroque ở lớp vỏ, tân cổ điển ở lõi trong.",
    "Về mặt biểu tượng, Smolny gắn với hình ảnh người phụ nữ và giáo dục nữ giới ở Nga. Quần thể vốn được hình dung làm tu viện cho các thiếu nữ quý tộc, và ngay bên cạnh, Viện Smolny về sau trở thành cơ sở giáo dục nữ danh tiếng bậc nhất Đế quốc Nga. Cái tên 'Smolny' vì thế mang tầng nghĩa văn hóa vượt ra ngoài khuôn khổ một nhà thờ.",
    "Trong ký ức lịch sử hiện đại, khu vực Smolny còn được biết đến vì vai trò chính trị: chính tòa nhà Viện Smolny kề bên đã trở thành đại bản doanh của những người Bolshevik trong Cách mạng Tháng Mười năm 1917 và là nơi ở của Lenin một thời gian. Sự gần gũi địa lý ấy khiến khu vực này trở thành nơi giao thoa của tôn giáo, giáo dục và chính trị — ba dòng chảy lớn của lịch sử Nga cùng hội tụ.",
    "Việc thánh đường được chuyển thành phòng hòa nhạc thời Xô-viết, rồi trở lại làm nơi thờ phượng sau năm 2015, cũng phản ánh hành trình chung của rất nhiều công trình tôn giáo Nga qua thế kỷ 20: từ nơi cầu nguyện, sang không gian thế tục, rồi hồi sinh. Ở Smolny, sự chuyển hóa ấy diễn ra tương đối 'êm', và may mắn giúp giữ được cả kiến trúc lẫn công năng văn hóa.",
    "Cuối cùng, Smolny có ý nghĩa như một 'chữ ký' của Rastrelli. Dù ông không thấy công trình hoàn thành, hậu thế đã đặt tên quảng trường phía trước theo tên ông, và giới kiến trúc xem đây là một trong những đỉnh cao sáng tạo của bậc thầy Baroque. Câu chuyện về giấc mộng tháp chuông dang dở cũng trở thành một phần huyền thoại đô thị, nhắc nhớ rằng ngay cả những thiên tài cũng phải nhượng bộ trước dòng chảy của thời cuộc.",
]})

S.append({"heading": "Trải nghiệm dành cho du khách", "paras": [
    "Một chuyến thăm Smolny thường bắt đầu bằng khoảnh khắc 'ồ' đầy thích thú ngay khi công trình hiện ra ở cuối quảng trường. Nhịp độ ở đây chậm rãi và dễ chịu: du khách có thể thong thả đi vòng quanh, ngắm mặt tiền từ nhiều góc, rồi mới vào trong. So với các điểm 'nóng' quanh trung tâm, lượng khách ở Smolny thường vừa phải, nên trải nghiệm ít bị hối thúc.",
    "Bên trong, không gian trắng cao rộng tạo cảm giác thư thái. Nếu đến đúng dịp có biểu diễn, du khách có thể thưởng thức một buổi hòa nhạc cổ điển hoặc hợp xướng — đây là nét trải nghiệm đặc trưng khiến Smolny khác với những nhà thờ chỉ để tham quan. Âm học của gian thờ khiến tiếng đàn, tiếng hát lan tỏa đầy đặn dưới vòm.",
    "Với người yêu độ cao và thích 'săn' góc nhìn toàn cảnh, hành trình leo tháp chuông là điểm nhấn của chuyến đi. Bậc thang khá nhiều (khoảng 277 bậc) và có đoạn hẹp, nên cần đi chậm và giữ sức; bù lại, khung cảnh sông Neva mở ra ở phía trên là phần thưởng rất xứng đáng cho nỗ lực bỏ ra.",
    "Đây cũng là điểm đến thân thiện với nhiếp ảnh. Từ ngoài quảng trường, từ bờ sông, cho tới trên đài quan sát, mỗi vị trí lại cho một kiểu ảnh khác nhau: cận cảnh chi tiết Baroque, toàn cảnh công trình trên nền trời, hay panorama thành phố. Ánh sáng dịu của buổi sáng sớm và chiều muộn — hoặc ánh sáng kéo dài của mùa đêm trắng — đều rất lý tưởng.",
    "Là một nơi thờ phượng đang hoạt động trở lại, Smolny đòi hỏi du khách giữ thái độ tôn trọng: ăn mặc kín đáo, nói khẽ, và lưu ý các khu vực dành cho việc cầu nguyện. Sự chừng mực ấy không làm giảm trải nghiệm, mà ngược lại giúp cảm nhận trọn vẹn hơn bầu không khí trang nghiêm của công trình.",
    "Do nằm hơi xa cụm trung tâm, Smolny hợp với những ai muốn một buổi tham quan 'thảnh thơi', tránh cảnh chen chúc. Nhiều du khách chọn ghép Smolny với một buổi đi dạo dọc bờ Neva hoặc thăm khu Tauride gần đó, biến chuyến đi thành một lát cắt yên bình của Saint Petersburg.",
]})

S.append({"heading": "Mẹo tham quan", "paras": [
    "Chọn ngày nắng nếu có thể: sắc xanh–trắng của Smolny đẹp nhất dưới trời quang. Vào ngày âm u, màu sắc công trình dịu đi đáng kể, nên nếu lịch trình linh hoạt, hãy ưu tiên hôm thời tiết đẹp để chụp ảnh.",
    "Kiểm tra trước lịch mở cửa và lịch biểu diễn: vì Smolny vừa là nhà thờ vừa là phòng hòa nhạc, giờ mở cửa tham quan có thể thay đổi theo sự kiện. Nên tra cứu thông tin cập nhật trước khi đến để tránh trùng giờ đóng cửa hoặc buổi diễn riêng.",
    "Dành thời gian cho tháp chuông: nếu định leo đài quan sát, hãy đến sớm hơn giờ đóng cửa kha khá, vì việc lên–xuống 277 bậc và dừng ngắm cảnh mất khá nhiều thời gian. Đi giày thoải mái và mang theo nước.",
    "Mang theo tiền mặt lẻ: vé vào khu trưng bày và vé leo tháp chuông thường ở mức phải chăng, nhưng chuẩn bị sẵn tiền lẻ sẽ giúp việc mua vé nhanh gọn hơn, nhất là khi hệ thống thanh toán thẻ đôi lúc không tiện với khách nước ngoài.",
    "Ăn mặc phù hợp nơi thờ tự: nên có khăn/áo che vai, tránh quần quá ngắn; nữ giới có thể chuẩn bị một chiếc khăn trùm đầu khi vào khu vực cầu nguyện, theo tập quán Chính thống giáo.",
    "Kết hợp lộ trình thông minh: vì Smolny nằm lệch khỏi trung tâm, hãy ghép nó với các điểm lân cận (bờ kè Neva, khu Tauride) trong cùng một buổi, thay vì đi riêng một chuyến, để tiết kiệm thời gian di chuyển.",
    "Chọn khung giờ vắng để chụp ảnh: buổi sáng sớm ngay khi mở cửa thường ít khách nhất, thuận lợi cho việc chụp mặt tiền và nội thất mà không bị người qua lại chen vào khung hình. Buổi chiều muộn lại cho ánh sáng vàng ấm đổ lên lớp trang trí trắng, làm nổi khối kiến trúc.",
    "Lưu ý quy định chụp ảnh và quay phim: ở khu vực trưng bày và trên tháp chuông, việc chụp ảnh thường được cho phép, nhưng trong giờ cử hành phụng vụ nên hạn chế và tuyệt đối không dùng đèn flash hay chân máy nếu chưa được phép, để giữ sự trang nghiêm và tránh ảnh hưởng người hành lễ.",
]})

S.append({"heading": "Khám phá xung quanh", "paras": [
    "Viện Smolny (Smolny Institute) ngay kề bên là điểm đến gắn bó mật thiết với nhà thờ, cả về tên gọi lẫn lịch sử. Tòa nhà mang phong cách tân cổ điển thanh lịch do kiến trúc sư Giacomo Quarenghi thiết kế, từng là trường nữ sinh quý tộc, rồi trở thành đại bản doanh của cách mạng năm 1917 và nơi ở của Lenin. Dù công năng hành chính khiến việc vào trong hạn chế, khu vực quanh Viện vẫn đáng để tản bộ và tìm hiểu.",
    "Cung điện và Vườn Tauride (Tavrichesky) nằm không xa về phía tây nam, là một quần thể tân cổ điển với khu vườn cảnh rộng rãi — điểm dừng chân dễ chịu để nghỉ ngơi giữa hành trình. Đây từng là dinh thự gắn với công thần Grigory Potyomkin thời Ekaterina II, và khu vườn nay là không gian xanh được người dân địa phương ưa thích.",
    "Bờ kè sông Neva ở khu vực này mang vẻ khoáng đạt, ít khách du lịch hơn đoạn trung tâm. Đi dọc bờ sông, du khách có thể ngắm cầu Bolsheokhtinsky — một cây cầu thép lịch sử bắc qua Neva — và thu vào ống kính hình bóng Smolny in trên mặt nước.",
    "Về phía nam, Tu viện Alexander Nevsky (Alexander Nevsky Lavra) là một trong những trung tâm tôn giáo quan trọng nhất thành phố, nơi có các nghĩa trang danh nhân với phần mộ của nhiều nhạc sĩ, văn hào lừng danh như Tchaikovsky, Dostoevsky. Có thể ghép điểm này vào lịch trình nếu muốn một buổi khám phá theo chủ đề tâm linh – lịch sử.",
    "Khu vực quanh ga Chernyshevskaya và trục phố Suvorovsky có nhiều quán cà phê, tiệm ăn phục vụ người dân địa phương, là nơi thích hợp để nghỉ chân, thưởng thức ẩm thực Nga đời thường với mức giá dễ chịu hơn so với các nhà hàng ngay lõi du lịch.",
    "Nhìn rộng ra, cả cụm Smolny – Tauride – Nevsky Lavra tạo thành một 'vành đai' phía đông của trung tâm lịch sử, nơi du khách có thể trải nghiệm một Saint Petersburg trầm lắng, giàu chiều sâu và ít xô bồ hơn — bổ sung lý tưởng cho những ngày đã 'no' cung điện và bảo tàng ở khu lõi.",
    "Với người thích khám phá bằng đường sông, vào mùa hè có các tuyến du thuyền và tàu dạo trên sông Neva cùng hệ thống kênh đào. Ngắm Smolny và đường chân trời thành phố từ mặt nước là một góc nhìn hoàn toàn khác, giúp hiểu vì sao Saint Petersburg được mệnh danh là 'Venice của phương Bắc' và vì sao các kiến trúc sư xưa luôn tính toán dáng vẻ công trình khi nhìn từ sông.",
]})

S.append({"heading": "Câu chuyện & giai thoại thú vị", "paras": [
    "Giai thoại được yêu thích nhất về Smolny xoay quanh tháp chuông chưa bao giờ mọc lên. Theo thiết kế của Rastrelli, đó phải là một tháp cao chừng 140 mét, đủ sức vượt qua gác chuông Nhà thờ Pyotr và Pavel để trở thành công trình cao nhất nước Nga. Nhưng khi Elizaveta qua đời và Ekaterina II lên ngôi với gu thẩm mỹ trái ngược, ngân khố cạn kiệt đã 'chôn vùi' giấc mộng ấy. Điều thú vị là mô hình gỗ khổng lồ thể hiện ý tưởng tháp chuông vẫn còn được lưu giữ, cho phép hậu thế hình dung một Smolny 'lẽ ra đã như thế' — một trong những 'công trình chưa hoàn thành' nổi tiếng nhất lịch sử kiến trúc Nga.",
    "Một mẩu chuyện thường được kể trong giới hướng dẫn viên liên quan đến kiến trúc sư Giacomo Quarenghi — người theo trường phái tân cổ điển và về nguyên tắc 'kỵ' phong cách Baroque. Tương truyền, mỗi lần đi ngang Smolny, vị kiến trúc sư khó tính này đều ngả mũ kính cẩn và thốt lên đại ý 'Kìa, mới đúng là một nhà thờ!'. Dù giai thoại khó kiểm chứng đến từng chữ, nó phản ánh sự ngưỡng mộ mà ngay cả những người 'đối lập gu' cũng dành cho tác phẩm của Rastrelli.",
    "Bản thân nguồn gốc cái tên 'Smolny' cũng là một câu chuyện nhỏ đáng kể. Trước khi trở thành nơi tọa lạc của một trong những thánh đường đẹp nhất nước Nga, khu đất này chỉ là bãi chưng nhựa thông, hắc ín ('smola') phục vụ việc đóng và bảo dưỡng tàu thời Pyotr Đại đế. Từ một 'xưởng hắc ín' bình dị, địa danh đã 'thăng hạng' thành biểu tượng kiến trúc — một minh chứng cho cách lịch sử đô thị có thể biến đổi ý nghĩa của một cái tên.",
    "Số phận 'lệch pha' của công trình cũng sinh ra một nghịch lý thú vị: người khởi công (Rastrelli) tạo nên lớp vỏ Baroque lộng lẫy, còn người hoàn tất gần một thế kỷ sau (Stasov) lại tạo nên phần lõi tân cổ điển giản dị. Vì thế, khi bước từ ngoài vào trong Smolny, du khách như đi xuyên qua hai thời đại thẩm mỹ khác nhau chỉ trong vài bước chân — điều hiếm gặp ở một công trình duy nhất.",
    "Trong thế kỷ 20, cái tên 'Smolny' còn mang một sắc thái hoàn toàn khác trong ký ức nhiều người: không phải nhà thờ, mà là trung tâm quyền lực cách mạng, do Viện Smolny kề bên là nơi đặt bản doanh Bolshevik năm 1917. Sự 'chồng lớp' ý nghĩa này khiến một địa danh có thể gợi lên đồng thời hình ảnh mái vòm thánh đường và những biến cố chính trị long trời — tùy vào người nghe thuộc thế hệ hay lĩnh vực nào.",
    "Cuối cùng, hành trình 'hồi sinh' của Smolny — từ nhà thờ bị đóng cửa và xuống cấp, sang phòng hòa nhạc, rồi trở lại làm nơi thờ phượng năm 2015 — tự nó đã là một câu chuyện đẹp để khép lại bài thuyết minh. Nó cho thấy cách một công trình có thể 'sống nhiều cuộc đời', thích ứng với từng thời kỳ mà vẫn giữ được cốt cách, để đến hôm nay tiếng chuông và tiếng nhạc lại cùng vang lên dưới những mái vòm xanh–trắng của Rastrelli.",
]})

out = os.path.join(HERE, "doc_smolny-cathedral.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=2)

wc = sum(len(p.split()) for s in doc["sections"] for p in s["paras"])
print("WROTE", out)
print("sections:", len(doc["sections"]), "| total word-tokens:", wc)
for s in doc["sections"]:
    print("  -", s["heading"], "|", sum(len(p.split()) for p in s["paras"]))
