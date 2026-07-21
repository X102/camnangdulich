import json, os

records = [
{
 "region":"sakhalin",
 "slug":"cape-velikan-sakhalin",
 "name_vi":"Mũi Velikan (Mys Velikan)",
 "name_ru":"Мыс Великан",
 "name_en":"Cape Velikan (Cape Giant)",
 "categories":["park_garden"],
 "lat":46.630280,
 "lon":143.515830,
 "address_vi":"Bán đảo Tonino-Aniva, huyện Korsakov, tỉnh Sakhalin, Nga (bờ biển Okhotsk, đông nam đảo Sakhalin)",
 "rating":None,
 "review_summary_vi":"Du khách thường choáng ngợp trước vẻ đẹp siêu thực của các vòm đá và mô tả nơi đây là điểm đến đáng nhớ nhất trên đảo Sakhalin. Điểm được nhắc tới nhiều nhất là đường đi rất xóc, phụ thuộc thời tiết và thủy triều, nên hầu hết đều khuyên đi theo tour xe địa hình có kinh nghiệm.",
 "presentation_short_vi":"Mũi Velikan là một trong những kỳ quan ven biển ngoạn mục nhất của đảo Sakhalin, nơi sóng và gió đã bào mòn những vách đá thành các vòm cổng, hang động và cột đá kỳ vĩ nhô lên từ biển Okhotsk. Nằm trên bán đảo hoang sơ Tonino-Aniva ở đông nam đảo, đây là điểm đến trong mơ của những ai yêu thiên nhiên nguyên bản và nhiếp ảnh.",
 "presentation_long_vi":"Nằm ở bờ đông bán đảo Tonino-Aniva, cách thành phố Yuzhno-Sakhalinsk vài giờ đường off-road, Mũi Velikan (nghĩa là 'Người khổng lồ') là điểm nhấn ngoạn mục nhất trên dải bờ biển Okhotsk của Sakhalin. Qua hàng nghìn năm, sóng biển và gió đã chạm khắc những khối đá trầm tích ven bờ thành một mê cung của vòm cổng đá, hang xuyên thủy, cột đá đơn độc (kekur) và các hốc đá kỳ dị. Khi thủy triều xuống, du khách có thể đi bộ dưới chân những chiếc cổng đá cao vút, len lỏi qua các khe đá và ngắm mặt biển đổi màu theo ánh sáng. Khu vực này còn là nơi trú ngụ của hải cẩu cùng nhiều đàn chim biển làm tổ trên vách đá, tạo nên một hệ sinh thái ven biển được bảo vệ. Không có đường nhựa dẫn tới đây; hầu hết du khách đi bằng xe địa hình UAZ theo tour trong ngày, thường kết hợp với các bãi biển và mũi đất lân cận. Chính sự khó tiếp cận đã giữ cho Mũi Velikan vẻ hoang sơ gần như nguyên vẹn. Vào mùa hè, khi sương mù tan và cỏ xanh phủ kín triền dốc, nơi đây trở thành thiên đường cho nhiếp ảnh gia và những người ưa khám phá vùng đất tận cùng nước Nga.",
 "highlights_vi":[
   "Vòm cổng đá và cột đá kekur khổng lồ được sóng biển bào mòn qua hàng nghìn năm",
   "Khám phá các hang động và khe đá lộ ra khi thủy triều xuống",
   "Đàn hải cẩu và chim biển làm tổ trên vách đá ven bờ Okhotsk"
 ],
 "practical":{
   "hours_vi":"Địa điểm ngoài trời, tham quan tự do; nên đến vào ban ngày và canh theo lịch thủy triều xuống.",
   "ticket_vi":"Bản thân mũi đất không thu phí; du khách chủ yếu trả tiền cho tour xe địa hình khứ hồi từ Yuzhno-Sakhalinsk.",
   "duration_vi":"Cả ngày (khoảng 8–10 tiếng tính cả di chuyển bằng xe địa hình).",
   "best_time_vi":"Tháng 6 đến tháng 9, chọn ngày trời quang và trùng lúc thủy triều xuống.",
   "tips_vi":"Đi giày chống nước, mang theo đồ ấm và nước uống; kiểm tra bảng thủy triều trước khi đi và ưu tiên tour có hướng dẫn viên bản địa vì gần như không có sóng điện thoại."
 },
 "photo_file":"File:Мыс Великан.jpg",
 "official_site":None,
 "tags":["cape","rock-arch","sea-of-okhotsk","nature","photography"]
},
{
 "region":"sakhalin",
 "slug":"tunaicha-lake",
 "name_vi":"Hồ Tunaicha (Ozero Tunaycha)",
 "name_ru":"Озеро Тунайча",
 "name_en":"Lake Tunaicha",
 "categories":["park_garden"],
 "lat":46.769444,
 "lon":143.225000,
 "address_vi":"Huyện Korsakov, gần làng Okhotskoye, cách Yuzhno-Sakhalinsk khoảng 50 km về đông nam, tỉnh Sakhalin, Nga",
 "rating":None,
 "review_summary_vi":"Người dân địa phương và du khách yêu thích Tunaicha vì khung cảnh yên bình, nước trong và không khí trong lành, xem đây là nơi lý tưởng để câu cá và cắm trại cuối tuần. Một số ý kiến lưu ý rằng cơ sở hạ tầng du lịch còn đơn sơ và muỗi khá nhiều vào mùa hè.",
 "presentation_short_vi":"Tunaicha là hồ nước lợ lớn thứ hai của đảo Sakhalin, một đầm phá rộng lớn nằm sát biển Okhotsk và chỉ ngăn cách với bãi biển bởi một dải cát hẹp. Nổi tiếng với làn nước trong, đàn thiên nga và nguồn cá dồi dào, đây là điểm nghỉ ngơi và câu cá yêu thích của người dân địa phương.",
 "presentation_long_vi":"Cách Yuzhno-Sakhalinsk khoảng 50 km về phía đông nam, hồ Tunaicha trải rộng trong vùng đất thấp Muravyov, ngăn cách với biển Okhotsk chỉ bởi một dải cát mỏng. Với diện tích lớn thứ hai trên toàn đảo Sakhalin, đây là một hồ nước lợ – nơi nước ngọt từ sông suối hòa cùng nước biển tràn vào, tạo nên một hệ sinh thái đầm phá phong phú hiếm có. Nước hồ nổi tiếng trong vắt, phản chiếu bầu trời cùng những rặng đồi thấp phủ rừng taiga xung quanh. Tunaicha là thiên đường của giới câu cá: hồ có tới gần 30 loài cá, trong đó có cá hồi chum, cá hồi hồng và nhiều loài cá nước lạnh quý, khiến câu cá trên mặt băng mùa đông trở thành thú vui phổ biến. Ven hồ còn là nơi dừng chân của nhiều loài chim di cư và thiên nga, một phần khu vực được đưa vào diện bảo tồn. Du khách tìm đến đây để cắm trại, chèo thuyền, tắm nắng bên bờ cát hoặc đơn giản là tận hưởng không khí trong lành và khung cảnh yên bình. Sự kết hợp giữa hồ, biển và rừng trong cùng một tầm mắt khiến Tunaicha trở thành một trong những bức tranh thiên nhiên đặc trưng và dễ tiếp cận nhất của miền nam Sakhalin.",
 "highlights_vi":[
   "Đầm phá nước lợ lớn thứ hai Sakhalin, chỉ cách biển Okhotsk một dải cát",
   "Gần 30 loài cá, thiên đường câu cá mùa hè lẫn câu cá trên băng mùa đông",
   "Điểm dừng chân của thiên nga và chim di cư trong khung cảnh hồ – biển – rừng taiga"
 ],
 "practical":{
   "hours_vi":"Khu vực thiên nhiên mở, tham quan tự do quanh năm.",
   "ticket_vi":"Miễn phí; có thể phát sinh chi phí thuê chỗ nghỉ, thuyền hoặc dịch vụ câu cá.",
   "duration_vi":"Từ nửa ngày đến trọn ngày, hoặc lưu trú qua đêm nếu cắm trại.",
   "best_time_vi":"Mùa hè (tháng 6–9) để tắm nắng, câu cá; mùa đông cho trải nghiệm câu cá trên băng.",
   "tips_vi":"Mang theo thuốc chống côn trùng, đồ cắm trại và nước sạch; tự thu gom rác để giữ gìn hệ sinh thái đầm phá."
 },
 "photo_file":None,
 "official_site":None,
 "tags":["lake","lagoon","fishing","birdwatching","nature"]
},
{
 "region":"sakhalin",
 "slug":"sakhalin-regional-museum",
 "name_vi":"Bảo tàng Địa phương học tỉnh Sakhalin (Sakhalinsky oblastnoy krayevedchesky muzey)",
 "name_ru":"Сахалинский областной краеведческий музей",
 "name_en":"Sakhalin Regional Museum",
 "categories":["museum","monument"],
 "lat":46.959000,
 "lon":142.744400,
 "address_vi":"Đại lộ Kommunistichesky 29, thành phố Yuzhno-Sakhalinsk, tỉnh Sakhalin, Nga",
 "rating":None,
 "review_summary_vi":"Du khách đánh giá cao tòa nhà lịch sử tuyệt đẹp cùng các bộ sưu tập đa dạng, phong phú về thiên nhiên và lịch sử đảo, và xem đây là điểm 'phải ghé' ở Yuzhno-Sakhalinsk. Một số nhận xét cho rằng phần chú thích hiện vật chủ yếu bằng tiếng Nga nên khách nước ngoài nên đi cùng hướng dẫn viên.",
 "presentation_short_vi":"Bảo tàng Địa phương học tỉnh Sakhalin nằm trong tòa nhà kiểu Nhật độc đáo xây năm 1937, thời kỳ nam đảo thuộc tỉnh Karafuto của Nhật Bản. Với kiến trúc 'teikan-zukuri' mái ngói cong đặc trưng, đây vừa là biểu tượng lịch sử vừa là kho tàng thiên nhiên và văn hóa bậc nhất của hòn đảo.",
 "presentation_long_vi":"Tọa lạc ngay trung tâm Yuzhno-Sakhalinsk trên đại lộ Kommunistichesky, Bảo tàng Địa phương học tỉnh Sakhalin là công trình dễ nhận biết nhất thành phố nhờ kiến trúc Nhật Bản hiếm có trên đất Nga. Tòa nhà được xây trong các năm 1935–1937 theo phong cách 'teikan-zukuri' (kiểu 'vương miện đế quốc') do kiến trúc sư Kaizuka Yoshio thiết kế, khi nửa nam Sakhalin còn thuộc tỉnh Karafuto của Nhật Bản. Mái ngói cong nhiều tầng, các chi tiết trang trí onigawara và cấu trúc gợi hình tháp thành quách khiến nó trông như một lâu đài phương Đông thu nhỏ giữa lòng thành phố Nga. Bên trong, bảo tàng lưu giữ những bộ sưu tập tiêu biểu cho thiên nhiên và lịch sử của đảo: hóa thạch khủng long Nipponosaurus và thú biển cổ Desmostylus, tiêu bản động thực vật quý hiếm, cùng hiện vật phong phú về các dân tộc bản địa Ainu, Nivkh và Uilta. Một trong bốn cột mốc biên giới đặt năm 1906 dọc vĩ tuyến 50 – từng chia đôi đảo giữa Nga và Nhật – cũng được trưng bày tại đây, nhắc nhớ về quá khứ đầy biến động của vùng đất này. Với sự kết hợp giữa kiến trúc di sản và nội dung trưng bày sâu sắc, đây là điểm khởi đầu lý tưởng để hiểu về Sakhalin trước mọi chuyến khám phá.",
 "highlights_vi":[
   "Tòa nhà kiểu 'teikan-zukuri' Nhật Bản năm 1937, di sản kiến trúc độc nhất vô nhị trên đất Nga",
   "Hóa thạch khủng long Nipponosaurus và bộ sưu tập thiên nhiên đặc hữu của đảo Sakhalin",
   "Hiện vật văn hóa các dân tộc bản địa Ainu, Nivkh, Uilta và cột mốc biên giới Nga–Nhật năm 1906"
 ],
 "practical":{
   "hours_vi":"Bảo tàng mở cửa gần như quanh năm; lịch và giờ mở cửa cụ thể có thể thay đổi, nên kiểm tra trên website chính thức trước khi đến.",
   "ticket_vi":"Vé vào cửa có thu phí ở mức phải chăng (một số khu trưng bày có thể tính vé riêng); xem bảng giá cập nhật trên trang chính thức sakhalinmuseum.ru.",
   "duration_vi":"Khoảng 1,5–2 tiếng.",
   "best_time_vi":"Quanh năm; là lựa chọn lý tưởng cho những ngày mưa hoặc mùa đông lạnh giá.",
   "tips_vi":"Đừng bỏ lỡ các hiện vật trưng bày ngoài trời trong khuôn viên; nên thuê hướng dẫn viên hoặc audio guide nếu muốn hiểu sâu vì chú thích chủ yếu bằng tiếng Nga."
 },
 "photo_file":"File:Japanese building of Yuzhno-Sakhalinsk Regional Museum (21469244223).jpg",
 "official_site":"https://sakhalinmuseum.ru",
 "tags":["museum","history","japanese-architecture","karafuto","ethnography"]
},
{
 "region":"sakhalin",
 "slug":"mountain-air-resort",
 "name_vi":"Khu thể thao – du lịch Gorny Vozdukh (Gornyy Vozdukh, 'Không khí núi')",
 "name_ru":"СТК «Горный воздух»",
 "name_en":"Gorny Vozdukh (Mountain Air) Resort",
 "categories":["other"],
 "lat":46.949610,
 "lon":142.797042,
 "address_vi":"Núi Bolshevik, thành phố Yuzhno-Sakhalinsk, tỉnh Sakhalin, Nga",
 "rating":None,
 "review_summary_vi":"Du khách khen ngợi vị trí thuận tiện ngay cạnh thành phố, đường trượt được bảo trì tốt và tầm nhìn ngoạn mục từ đỉnh núi. Một số phàn nàn về thời tiết gió và sương mù thất thường của Sakhalin có thể ảnh hưởng đến trải nghiệm, cùng cảnh đông đúc vào cuối tuần mùa cao điểm.",
 "presentation_short_vi":"Gorny Vozdukh ('Không khí núi') là khu nghỉ dưỡng trượt tuyết nằm ngay trên sườn núi Bolshevik, sát rìa thành phố Yuzhno-Sakhalinsk. Là một trong những khu trượt tuyết hiện đại nhất vùng Viễn Đông Nga, nơi đây hấp dẫn du khách quanh năm với cáp treo, đường trượt dài và tầm nhìn toàn cảnh thành phố.",
 "presentation_long_vi":"Nằm trên sườn núi Bolshevik ngay sát trung tâm Yuzhno-Sakhalinsk, Gorny Vozdukh (nghĩa là 'Không khí núi') là niềm tự hào và là khu liên hợp thể thao – du lịch trọng điểm của tỉnh Sakhalin. Chỉ vài phút từ phố xá, du khách đã có thể lên cáp treo và cáp ghế để vượt độ cao từ khoảng 100 m lên tới gần 750 m, chinh phục hệ thống đường trượt tổng chiều dài chừng 25 km với đủ mọi cấp độ. Mùa trượt tuyết kéo dài từ cuối tháng 11 đến đầu tháng 5, và nhờ hệ thống chiếu sáng, du khách còn có thể trượt cả về đêm trong khung cảnh lung linh. Nhưng Gorny Vozdukh không chỉ dành cho mùa đông: khi tuyết tan, cáp treo vẫn hoạt động để đưa khách lên đỉnh ngắm toàn cảnh thành phố, thung lũng Susuya và những dãy núi trùng điệp của đảo. Trên đỉnh có các lối đi bộ, điểm ngắm cảnh và quán cà phê, còn sườn núi trở thành nơi đạp xe địa hình, dã ngoại mùa hè. Với sự đầu tư liên tục về hạ tầng, đây được xem là một trong những khu trượt tuyết chất lượng nhất Viễn Đông Nga và là điểm đến gần như bắt buộc cho bất kỳ ai ghé thăm thủ phủ của đảo Sakhalin.",
 "highlights_vi":[
   "Đường trượt tuyết tổng chiều dài khoảng 25 km với chênh cao hơn 600 m, có trượt đêm",
   "Cáp treo lên đỉnh núi Bolshevik ngắm toàn cảnh thành phố Yuzhno-Sakhalinsk",
   "Điểm đến bốn mùa: trượt tuyết mùa đông, đi bộ và đạp xe địa hình mùa hè"
 ],
 "practical":{
   "hours_vi":"Mùa đông thường mở cửa hằng ngày khoảng 09:00–21:00 (có trượt đêm); mùa hè chạy cáp treo theo lịch riêng.",
   "ticket_vi":"Vé trượt tuyết trọn ngày mùa cao điểm vào khoảng 2.800 rúp (giá tham khảo); vé đi cáp treo ngắm cảnh rẻ hơn nhiều.",
   "duration_vi":"Từ nửa ngày đến trọn ngày.",
   "best_time_vi":"Từ tháng 12 đến tháng 3 cho trượt tuyết; tháng 7–9 cho đi cáp treo ngắm cảnh và dã ngoại.",
   "tips_vi":"Có thể thuê trang bị trượt tuyết tại chỗ; mặc ấm và chắn gió vì thời tiết trên núi đổi rất nhanh; nên đi ngày trong tuần để tránh đông."
 },
 "photo_file":"File:View of Yuzhno-Sakhalinsk from Gorny Vozduh.JPG",
 "official_site":None,
 "tags":["ski-resort","mountain","cable-car","winter-sports","viewpoint"]
},
{
 "region":"sakhalin",
 "slug":"iturup-white-rocks",
 "name_vi":"Vách Đá Trắng đảo Iturup (Belye skaly)",
 "name_ru":"Белые скалы (Итуруп)",
 "name_en":"White Rocks of Iturup",
 "categories":["park_garden"],
 "lat":45.033333,
 "lon":147.616667,
 "address_vi":"Bờ vịnh Prostor, đảo Iturup, quần đảo Kuril, huyện Kurilsk, tỉnh Sakhalin, Nga",
 "rating":None,
 "review_summary_vi":"Những ai từng đến đều mô tả Vách Đá Trắng là khung cảnh 'như ngoài hành tinh', đẹp đến nghẹt thở và xứng đáng với hành trình gian nan. Điểm được nhắc đến nhiều nhất là sự xa xôi, chi phí cao và việc phải xin giấy phép vào vùng biên giới, nên gần như bắt buộc phải đi theo tour tổ chức.",
 "presentation_short_vi":"Vách Đá Trắng là một trong những kỳ quan thiên nhiên siêu thực nhất của quần đảo Kuril: những vách đá bọt núi lửa trắng xóa trải dài nhiều cây số bên vịnh Prostor trên đảo Iturup. Dưới chân vách là bãi cát pha hạt titan – magnetit đen nhánh có từ tính, tạo nên khung cảnh tương phản như trên hành tinh khác.",
 "presentation_long_vi":"Ẩn mình ở bờ đại dương phía đông đảo Iturup thuộc nam quần đảo Kuril, Vách Đá Trắng (Belye skaly) là một trong những cảnh quan ngoạn mục và ít người đặt chân tới nhất nước Nga. Đây là những vách đá cấu tạo từ đá bọt và tro núi lửa trắng xóa, hình thành từ các đợt phun trào cổ xưa khi vùng đất này còn nằm dưới biển. Dải vách trắng trải dài gần 5 km dọc vịnh Prostor, bị mưa gió và sóng biển bào mòn thành những rãnh, khe và tháp đá kỳ ảo, sáng lóa dưới nắng đến mức gần như chói mắt. Ấn tượng nhất là bãi biển dưới chân vách: cát ở đây trộn giữa thạch anh trắng và hạt titan – magnetit đen, tạo thành những dải sọc trắng đen đầy ma mị, thậm chí còn nhiễm từ và hút được nam châm. Iturup nằm trong vùng biên giới, khá xa xôi và khó tiếp cận: du khách thường bay tới rồi đi từ thị trấn Kurilsk qua làng Reidovo, sau đó dùng xe địa hình hoặc thuyền máy để tới nơi. Chính sự hoang sơ tuyệt đối và vẻ đẹp khác lạ ấy đã biến Vách Đá Trắng thành 'thánh địa' trong mơ của các nhiếp ảnh gia và những nhà thám hiểm mê vùng đất núi lửa Viễn Đông.",
 "highlights_vi":[
   "Vách đá bọt núi lửa trắng xóa trải dài gần 5 km bên vịnh Prostor",
   "Bãi cát sọc trắng – đen từ thạch anh và titan-magnetit, nhiễm từ tính hút nam châm",
   "Cảnh quan hoang sơ bậc nhất nam Kuril, thiên đường của nhiếp ảnh và thám hiểm"
 ],
 "practical":{
   "hours_vi":"Địa điểm thiên nhiên ngoài trời, không giới hạn giờ; phụ thuộc lịch tour và thời tiết.",
   "ticket_vi":"Không có vé vào cửa; chi phí nằm ở tour, di chuyển tới đảo và giấy phép vùng biên giới Kuril.",
   "duration_vi":"Thường là một phần của tour Iturup kéo dài vài ngày; riêng khu vực vách đá tham quan khoảng nửa ngày.",
   "best_time_vi":"Cuối tháng 6 đến tháng 9, khi biển lặng và ít sương mù nhất.",
   "tips_vi":"Xin giấy phép vùng biên giới trước nhiều tuần; mang kem chống nắng và kính râm vì đá trắng phản nắng rất gắt; chuẩn bị tinh thần cho lịch trình linh hoạt vì thời tiết Kuril thay đổi liên tục."
 },
 "photo_file":"File:Iturup White cliffs.jpg",
 "official_site":None,
 "tags":["cliffs","pumice","kuril-islands","volcanic","black-sand-beach"]
},
{
 "region":"sakhalin",
 "slug":"moneron-island",
 "name_vi":"Đảo Moneron (Ostrov Moneron)",
 "name_ru":"Остров Монерон",
 "name_en":"Moneron Island",
 "categories":["park_garden"],
 "lat":46.250000,
 "lon":141.233000,
 "address_vi":"Đảo Moneron, biển Nhật Bản, cách cảng Nevelsk khoảng 43 km, huyện Nevelsk, tỉnh Sakhalin, Nga",
 "rating":None,
 "review_summary_vi":"Du khách trở về thường trầm trồ về làn nước trong, cảnh quan hoang sơ và trải nghiệm lặn biển hiếm có, xem Moneron là chuyến đi đáng giá nhất ở Sakhalin. Nhược điểm lớn nhất được nhắc tới là chuyến tàu vượt biển dễ say sóng và việc tour thường bị hoãn hoặc hủy vì thời tiết xấu.",
 "presentation_short_vi":"Moneron là hòn đảo nhỏ giữa biển Nhật Bản, cách bờ tây nam Sakhalin vài chục cây số, và là công viên tự nhiên biển đầu tiên của nước Nga. Nổi tiếng với làn nước trong xanh nhờ dòng hải lưu ấm Tsushima, nơi đây được mệnh danh là thiên đường lặn biển và ngắm chim của vùng Viễn Đông.",
 "presentation_long_vi":"Nằm đơn độc giữa biển Nhật Bản, cách cảng Nevelsk ở tây nam Sakhalin khoảng 43 km, đảo Moneron là viên ngọc quý và là công viên tự nhiên biển đầu tiên của nước Nga. Hòn đảo nhỏ chỉ dài hơn 7 km này từng thuộc Nhật Bản với tên gọi Kaiba-to, và ngày nay là khu bảo tồn được quản lý nghiêm ngặt. Điều làm nên danh tiếng của Moneron chính là làn nước biển trong vắt lạ thường: dòng hải lưu ấm Tsushima mang tới đây hệ sinh vật biển phong phú với rừng tảo bẹ, đàn cá rực rỡ và tầm nhìn dưới nước hiếm có ở vĩ độ cao, biến nơi đây thành điểm lặn biển hàng đầu Viễn Đông Nga. Trên mặt đất, những vách đá bazan dựng đứng, thác nước đổ thẳng ra biển và các cột đá ngoài khơi là nơi làm tổ của hàng nghìn con chim biển, trong khi hải cẩu và sư tử biển thường xuất hiện quanh đảo. Không có dân cư thường trú; du khách tới Moneron theo tour bằng tàu cao tốc hoặc trực thăng từ Nevelsk, và chỉ trong mùa hè khi biển đủ êm. Sự cô lập cùng vẻ đẹp nguyên sơ khiến chuyến đi tới Moneron trở thành một cuộc phiêu lưu đáng nhớ với những ai muốn chạm tới thiên nhiên hoang dã bậc nhất.",
 "highlights_vi":[
   "Công viên tự nhiên biển đầu tiên của Nga, làn nước trong nhờ hải lưu ấm Tsushima",
   "Thiên đường lặn biển với rừng tảo bẹ và sinh vật biển phong phú",
   "Vách đá bazan, thác nước đổ ra biển cùng các đàn chim biển, hải cẩu, sư tử biển"
 ],
 "practical":{
   "hours_vi":"Chỉ tham quan theo tour trong mùa hè; đảo là khu bảo tồn nên cần đăng ký trước.",
   "ticket_vi":"Không bán vé lẻ tại chỗ; chi phí trọn gói gồm tour tàu hoặc trực thăng và phí vào công viên tự nhiên.",
   "duration_vi":"Tour trong ngày hoặc lưu trú 1–2 ngày trên đảo.",
   "best_time_vi":"Tháng 7 đến tháng 9, khi biển lặng nhất.",
   "tips_vi":"Đặt tour sớm và chuẩn bị lịch trình dự phòng vì dễ bị hoãn do thời tiết; mang thuốc chống say sóng; nếu lặn, nên có chứng chỉ và đặt dịch vụ trước."
 },
 "photo_file":"File:Moneron Island.jpg",
 "official_site":None,
 "tags":["island","marine-park","diving","seabirds","sea-of-japan"]
},
{
 "region":"sakhalin",
 "slug":"dagi-hot-springs",
 "name_vi":"Suối nước nóng Dagi (Daginskiye termalnyye istochniki)",
 "name_ru":"Дагинские термальные источники",
 "name_en":"Daginskie Thermal Springs",
 "categories":["park_garden"],
 "lat":52.042540,
 "lon":143.084260,
 "address_vi":"Làng Goryachie Klyuchi, huyện Nogliki, đông bắc đảo Sakhalin, tỉnh Sakhalin, Nga",
 "rating":None,
 "review_summary_vi":"Du khách và người dân địa phương yêu thích cảm giác thư giãn dễ chịu của suối khoáng nóng và tin vào công dụng chữa bệnh của nước, đặc biệt thú vị khi ngâm mình giữa tiết trời lạnh giá. Một số ý kiến cho rằng vị trí xa xôi ở phía bắc đảo và cơ sở vật chất tại các bồn tắm tự nhiên còn khá giản dị.",
 "presentation_short_vi":"Suối nước nóng Dagi là một điểm nghỉ dưỡng thiên nhiên nổi tiếng ở phía bắc đảo Sakhalin, bên bờ vịnh Daginsky của biển Okhotsk. Dòng nước khoáng nóng 40–54°C giàu khoáng chất từ lâu đã được người dân địa phương tìm đến để ngâm mình chữa bệnh và thư giãn.",
 "presentation_long_vi":"Nằm cạnh làng Goryachie Klyuchi (nghĩa là 'Suối Nóng') thuộc huyện Nogliki ở đông bắc Sakhalin, suối nước nóng Dagi là một trong những di tích thiên nhiên được yêu thích nhất của hòn đảo. Bên bờ vịnh Daginsky (Nyisky) của biển Okhotsk, hàng loạt mạch nước khoáng nóng phun lên từ lòng đất với nhiệt độ dao động khoảng 40–54°C. Đây là loại nước khoáng clorua – natri, chứa nitơ và metan cùng các nguyên tố vi lượng, được cho là có tác dụng hỗ trợ điều trị các bệnh xương khớp, da liễu và thần kinh. Người bản địa Nivkh đã biết đến và sử dụng những mạch suối này từ rất lâu đời. Ngày nay, khu vực được công nhận là di tích thiên nhiên cấp vùng và đã được đầu tư với các bồn ngâm, nhà tắm có mái che, hồ lộ thiên cùng một khu điều dưỡng – nghỉ dưỡng. Điều đặc biệt là du khách có thể ngâm mình trong làn nước nóng bốc hơi nghi ngút giữa khung cảnh thiên nhiên hoang sơ, thậm chí ngay cả trong mùa đông tuyết phủ trắng xóa. Dù nằm khá xa các trung tâm du lịch phía nam, Dagi vẫn thu hút đông đảo người dân Sakhalin tìm về để phục hồi sức khỏe, xua tan mệt mỏi và tận hưởng liệu pháp suối khoáng giữa lòng thiên nhiên Viễn Đông.",
 "highlights_vi":[
   "Mạch nước khoáng nóng tự nhiên 40–54°C bên bờ vịnh Daginsky, biển Okhotsk",
   "Nước khoáng clorua – natri, được cho là hỗ trợ chữa bệnh xương khớp và da liễu",
   "Ngâm khoáng nóng giữa thiên nhiên hoang sơ, kỳ thú nhất vào mùa đông tuyết phủ"
 ],
 "practical":{
   "hours_vi":"Các bồn ngâm tự nhiên mở tự do; khu điều dưỡng và dịch vụ có giờ hoạt động riêng.",
   "ticket_vi":"Nhiều bồn suối tự nhiên có thể ngâm miễn phí; các dịch vụ nhà tắm, hồ và lưu trú của khu nghỉ dưỡng thu phí riêng.",
   "duration_vi":"Từ 1–2 tiếng ngâm khoáng đến lưu trú vài ngày để điều dưỡng.",
   "best_time_vi":"Quanh năm; đặc biệt ấn tượng vào mùa đông khi ngâm nước nóng giữa tuyết.",
   "tips_vi":"Mang theo đồ bơi, dép và khăn; không ngâm quá lâu và tránh khi có bệnh lý tim mạch; có thể kết hợp ghé thăm thị trấn Nogliki lân cận."
 },
 "photo_file":None,
 "official_site":"https://dagisakh.com",
 "tags":["hot-springs","thermal","wellness","nature","okhotsk-coast"]
},
{
 "region":"sakhalin",
 "slug":"cape-aniva-lighthouse",
 "name_vi":"Ngọn hải đăng Aniva (Mayak Aniva)",
 "name_ru":"Маяк Анива",
 "name_en":"Aniva Lighthouse",
 "categories":["monument"],
 "lat":46.018885,
 "lon":143.414077,
 "address_vi":"Mũi Aniva (đá Sivuchya), bán đảo Tonino-Aniva, huyện Korsakov, tỉnh Sakhalin, Nga",
 "rating":None,
 "review_summary_vi":"Du khách gần như đồng lòng ngưỡng mộ vẻ đẹp hoang tàn, ma mị của hải đăng và coi hành trình bằng thuyền tới đây là trải nghiệm đáng nhớ nhất chuyến đi. Điểm được nhắc tới nhiều nhất là chuyến vượt biển dài dễ say sóng và thường bị hủy vì thời tiết, cùng việc bên trong tháp đã xuống cấp, nguy hiểm nên cần hết sức thận trọng.",
 "presentation_short_vi":"Hải đăng Aniva là công trình bị bỏ hoang nổi tiếng bậc nhất Sakhalin, đứng chơ vơ trên một tảng đá giữa biển ở mũi cực nam bán đảo Tonino-Aniva. Được người Nhật xây dựng năm 1939, tòa tháp phủ rêu phong nay trở thành biểu tượng đầy ma mị và lãng mạn của hòn đảo.",
 "presentation_long_vi":"Sừng sững trên tảng đá Sivuchya ngoài khơi mũi Aniva – điểm cực nam của bán đảo Tonino-Aniva, ngọn hải đăng Aniva là một trong những công trình bị bỏ hoang được săn tìm nhiều nhất nước Nga. Tháp đèn cao khoảng 31 m được kỹ sư người Nhật Miura Shinobu thiết kế và hoàn thành năm 1939, khi nam Sakhalin còn thuộc tỉnh Karafuto. Vào thời hoàng kim, chín tầng tháp là nơi sinh sống và làm việc của khoảng mười hai người canh đèn, giúp dẫn đường cho tàu thuyền qua eo biển đầy sương mù và dòng chảy nguy hiểm. Năm 1990, hải đăng được tự động hóa bằng một nguồn pin nguyên tử strontium-90; nhưng khi thiết bị này hỏng vào năm 2006 và công nghệ định vị vệ tinh lên ngôi, ngọn đèn bị bỏ mặc cho gió biển và thời gian. Ngày nay, tòa tháp sọc trắng – đen loang lổ rêu phong đứng cô độc giữa sóng nước, mang một vẻ đẹp hoang tàn đầy ám ảnh khiến du khách và nhiếp ảnh gia mê mẩn. Không có đường bộ dẫn tới đây; cách duy nhất để chiêm ngưỡng hải đăng là đi tàu hoặc thuyền theo tour từ vùng Novikovo hay Korsakov, và chỉ khi biển đủ êm. Chính sự cô lập cùng câu chuyện lịch sử ấy đã biến Aniva thành biểu tượng lãng mạn, bí ẩn của đảo Sakhalin.",
 "highlights_vi":[
   "Tháp hải đăng do người Nhật xây năm 1939, kiệt tác kỹ thuật đứng giữa biển khơi",
   "Từng vận hành bằng pin nguyên tử strontium-90 trước khi bị bỏ hoang năm 2006",
   "Vẻ đẹp hoang tàn đầy ma mị, biểu tượng nhiếp ảnh nổi tiếng nhất Sakhalin"
 ],
 "practical":{
   "hours_vi":"Không có giờ mở cửa; chỉ tiếp cận được bằng thuyền theo tour, tùy thời tiết và mùa.",
   "ticket_vi":"Không thu phí tham quan; chi phí nằm ở tour thuyền hoặc cano khứ hồi từ Korsakov hay Novikovo.",
   "duration_vi":"Tour thường kéo dài cả ngày, trong đó thời gian ở gần hải đăng khoảng 1–2 tiếng.",
   "best_time_vi":"Từ cuối tháng 6 đến tháng 9, khi biển lặng nhất.",
   "tips_vi":"Uống thuốc chống say sóng; mang áo ấm, áo mưa và giày chống trượt; hết sức cẩn thận nếu lên tháp vì cấu trúc đã mục nát, nhiều người chỉ ngắm và chụp ảnh từ thuyền."
 },
 "photo_file":"File:Aniva Lighthouse by Vyacheslav Ovchinnikov.jpg",
 "official_site":None,
 "tags":["lighthouse","abandoned","japanese-heritage","coast","sea-of-okhotsk"]
}
]

out_dir = "/home/claude/russia-tourism/_incoming"
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "reg_sakhalin.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

# Validation / stats
nulls = {"photo_file":[], "official_site":[], "rating":[]}
for r in records:
    for k in nulls:
        if r.get(k) is None:
            nulls[k].append(r["slug"])
    # word count check
    wc = len(r["presentation_long_vi"].split())
    assert len(r["highlights_vi"]) == 3, r["slug"]
    print(f"{r['slug']:26s} cat={r['categories']} lat={r['lat']} lon={r['lon']} long_wc={wc} hl={len(r['highlights_vi'])}")

print("\nTotal records:", len(records))
print("photo_file nulls:", nulls["photo_file"])
print("official_site nulls:", nulls["official_site"])
print("rating nulls:", nulls["rating"])
print("Wrote:", path)
