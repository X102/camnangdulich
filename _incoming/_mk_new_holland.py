# -*- coding: utf-8 -*-
"""Builder: doc_new-holland-island.json — nội dung nguyên gốc tiếng Việt.
Chạy: python3 _incoming/_mk_new_holland.py  → ghi _incoming/doc_new-holland-island.json
"""
import json, os, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))

def img(fn, cap):
    return {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(fn), "caption": cap}

sections = [
 {"heading": "Giới thiệu chung", "paras": [
  "Đảo Tân Hà Lan – tiếng Nga là «Новая Голландия», phiên âm gần đúng là «Nô-vai-a Gôn-lan-đi-a» – là một hòn đảo nhân tạo hình tam giác nằm ngay giữa lòng Sankt-Peterburg. Được hình thành từ đầu thế kỷ XVIII bằng cách đào các con kênh, đây là một trong những góc đô thị độc đáo và được yêu mến nhất của thành phố, nơi lịch sử hải quân uy nghi hoà quyện với nhịp sống văn hoá đương đại sôi động.",
  "Điều làm nên nét quyến rũ riêng của Tân Hà Lan là sự tương phản đầy sức hút. Bao quanh đảo là những dãy nhà kho bằng gạch đỏ trầm mặc theo phong cách Cổ điển sớm, với chiếc vòm cổng đá trứ danh soi bóng xuống mặt nước. Bên trong lớp vỏ lịch sử ấy lại là một công viên xanh mướt, sân khấu ngoài trời, quán ăn, cửa hàng thiết kế và sân chơi cho trẻ em – một không gian sống động, trẻ trung.",
  "Tên gọi «Tân Hà Lan» gắn liền với Pyotr Đại đế và tình yêu của ông dành cho Hà Lan. Khu vực này ngay từ khi hình thành đã mang dáng dấp của một cảng Hà Lan với những con kênh và cầu vòm, một phần vì các thợ đóng tàu người Hà Lan được Sa hoàng đưa tới làm việc tại đây. Từ một khu kho gỗ phục vụ đóng tàu, hòn đảo dần trở thành một biểu tượng đặc biệt của đô thị.",
  "Trong gần hai thế kỷ, Tân Hà Lan là lãnh địa khép kín của Bộ Hải quân rồi của quân đội, gần như cách biệt hoàn toàn với đời sống dân sự. Phải tới năm 2011, sau một dự án hồi sinh quy mô lớn, hòn đảo mới lần đầu tiên rộng cửa đón công chúng kể từ thời Pyotr Đại đế – một sự kiện được xem như việc trả lại cho thành phố một mảnh ghép quý giá vốn bị niêm phong quá lâu.",
  "Ngày nay, Tân Hà Lan được biết đến như một «công viên văn hoá đô thị» kiểu mẫu. Bãi cỏ trung tâm rộng lớn là nơi người dân trải bạt nằm nghỉ, nghe hoà nhạc hay xem chiếu phim ngoài trời vào mùa hè; còn mùa đông, chính bãi cỏ ấy biến thành sân trượt băng lung linh ánh đèn. Các toà nhà lịch sử được cải tạo thành không gian ẩm thực, triển lãm và giáo dục.",
  "Với du khách, Tân Hà Lan mang lại một trải nghiệm khác hẳn những cung điện vàng son thường thấy ở Sankt-Peterburg. Đây là nơi để cảm nhận cách một di sản công nghiệp – quân sự được đánh thức và tái sinh, đồng thời là điểm dừng chân thư giãn, gần gũi giữa hành trình tham quan dày đặc các bảo tàng và nhà thờ.",
  "Chính sự kết hợp giữa chiều sâu lịch sử – từ Pyotr Đại đế, ngành đóng tàu, khoa học hàng hải tới nhà tù hải quân – và một đời sống văn hoá đương đại đầy năng lượng đã khiến Tân Hà Lan trở thành một trong những địa điểm giàu câu chuyện và dễ mến nhất để giới thiệu về một Sankt-Peterburg vừa cổ kính vừa hiện đại."
 ]},
 {"heading": "Vị trí & cách di chuyển", "paras": [
  "Tân Hà Lan nằm ở Quận Admiralteysky, thuộc khu trung tâm lịch sử của Sankt-Peterburg. Hòn đảo được bao bọc bởi sông Moika ở một phía và hai con kênh – kênh Kryukov và kênh Admiralteysky – ở các phía còn lại, tạo nên hình tam giác đặc trưng. Đảo thuộc khu Kolomna yên tĩnh, không xa Nhà hát Mariinsky và Nhà thờ Hải quân Thánh Nikolai.",
  "Ga tàu điện ngầm gần nhất là Admiralteyskaya, từ đó du khách đi bộ khoảng mười lăm tới hai mươi phút men theo bờ sông Moika để tới đảo. Ngoài ra, cụm ga Sadovaya – Sennaya Ploshchad – Spasskaya ở phía đông cũng là điểm xuống thuận tiện, rồi thả bộ qua khu Kolomna để tiếp cận từ phía kênh Kryukov.",
  "Một trong những cách tiếp cận đẹp nhất là đi bộ dọc kè sông Moika từ khu vực Quảng trường Cung điện và Bảo tàng Hermitage. Quãng đường chừng hai mươi tới hai mươi lăm phút này đưa du khách qua nhiều cây cầu và mặt tiền cổ kính, để rồi bất ngờ chạm mặt chiếc vòm cổng đá đỏ hiện ra bên kia mặt nước.",
  "Du khách vào đảo qua các lối cầu bộ hành bắc ngang kênh. Việc ra vào công viên nhìn chung miễn phí, song vào những ngày có sự kiện lớn hoặc lễ hội đông người, ban quản lý có thể điều tiết lượng khách để bảo đảm an toàn và không gian.",
  "Vì nằm trong khu trung tâm giàu điểm tham quan, Tân Hà Lan rất dễ kết hợp vào một lộ trình đi bộ. Nhiều du khách xem đây là điểm nghỉ chân thư giãn giữa chặng, sau khi đã tham quan các công trình bề thế như Nhà thờ Thánh Isaac hay Nhà hát Mariinsky ở gần đó.",
  "Đối với những ai thích ngắm thành phố từ mặt nước, các tuyến du thuyền trên sông Moika và hệ thống kênh của Sankt-Peterburg thường đi ngang Tân Hà Lan, mang lại góc nhìn ấn tượng về chiếc vòm cổng và các dãy kho gạch đỏ soi bóng xuống nước – một trong những khung hình được yêu thích nhất của thành phố.",
  "Về thời gian mở cửa, công viên hoạt động theo mùa với khung giờ thay đổi giữa mùa hè và mùa đông, vì vậy du khách nên kiểm tra lịch trước khi tới. Nhìn chung đảo mở cửa quanh năm kể từ khi hoàn tất giai đoạn cải tạo đầu tiên, và mỗi mùa lại mang một diện mạo riêng."
 ]},
 {"heading": "Lịch sử hình thành và phát triển", "paras": [
  "Lịch sử Tân Hà Lan gắn bó mật thiết với sự ra đời của Sankt-Peterburg và của hải quân Nga. Sau khi thành phố được lập năm 1703, tới năm 1704 Bộ Hải quân (Admiralty) được đặt ở bờ trái sông Neva. Để phục vụ đóng tàu và vận chuyển vật liệu, người ta cho đào các con kênh; và khi kênh Admiralteysky cùng kênh Kryukov nối sông Moika với sông Neva vào khoảng năm 1717–1719, một hòn đảo nhân tạo hình tam giác đã hình thành.",
  "Cái tên «Tân Hà Lan» xuất hiện ngay trong quá trình xây dựng. Khu vực quanh Bộ Hải quân với những nhà kho và cầu vòm mang dáng dấp Hà Lan, cộng thêm sự hiện diện của các thợ đóng tàu Hà Lan mà Pyotr Đại đế đưa tới, đã khiến nơi đây được gọi thân mật là «Holland». Tương truyền, ngay từ thời Pyotr, trên đảo đã có một cái ao và có thể cả một cung điện gỗ nhỏ dành cho Sa hoàng.",
  "Từ năm 1732, đảo được chuyển cho Hải quân quản lý. Kiến trúc sư Ivan Korobov được giao dựng hệ thống nhà kho gỗ để chứa gỗ đóng tàu; tới năm 1738 trên đảo đã có tám kho gỗ. Những nhà kho này có tường đan kiểu mắt cáo cho thoáng khí, giúp giữ gỗ luôn khô – một giải pháp kỹ thuật khéo léo cho khí hậu ẩm của Sankt-Peterburg.",
  "Giữa thế kỷ XVIII, khi các kho gỗ xuống cấp, Hải quân quyết định xây lại bằng đá. Kiến trúc sư Savva Chevakinsky – học trò của Korobov – đưa ra một hệ thống lưu trữ gỗ theo chiều đứng độc đáo, với hàng chục «tháp» hình chóp cụt cho phép chứa lượng gỗ khổng lồ. Phần mặt đứng của quần thể lại được giao cho kiến trúc sư người Pháp Jean-Baptiste Vallin de la Mothe, người tạo nên chiếc vòm cổng lừng danh; còn kỹ sư Johann Gerard đảm nhiệm phần thi công.",
  "Chiếc vòm cổng bằng gạch đỏ, hai bên là các cột đá granite đỏ, được dựng trong một quá trình gian nan kéo dài khoảng bảy năm và hoàn tất vào năm 1777. Mỗi khối granite làm cột nặng tới chừng bốn tấn, phải huy động máy móc và hàng trăm nhân công. Các nhà kho bắt đầu được sử dụng từ năm 1773 và công trình cơ bản hoàn thành vào cuối thế kỷ XVIII, dù các cuộc chiến với Thổ Nhĩ Kỳ và Thuỵ Điển cuối thập niên 1780 đã khiến một số hạng mục dang dở, trong đó có chiếc vòm cổng thứ hai dự kiến bắc qua kênh Kryukov.",
  "Diện mạo hoàn chỉnh của Tân Hà Lan chỉ định hình vào thế kỷ XIX. Năm 1828–1829, kiến trúc sư Aleksandr Shtaubert xây một nhà tù hải quân hình tròn với sân trong khép kín, sớm được dân gian gọi là «Cái Chai» (Butylka). Đến năm 1893, trên đảo còn có một bể thử dành cho các kỹ sư đóng tàu; chính tại đây, nhà bác học Aleksei Krylov đã thử nghiệm các mô hình tàu trong giai đoạn 1900–1908. Năm 1915, Hải quân xây tại đảo một trạm vô tuyến vào loại mạnh nhất nước Nga đế quốc.",
  "Sau Cách mạng 1917, các công trình thế kỷ XVIII của Tân Hà Lan dần rơi vào cảnh hoang phế. Từ năm 1918 tới 2004, hòn đảo được quân đội sử dụng như một cơ sở khép kín, gần như cách biệt hoàn toàn với công chúng. Mãi tới năm 2000, đảo mới hé mở đôi chút nhân Ngày Hải quân cho một dự án nghệ thuật, rồi tới năm 2004 mới chính thức được chuyển giao cho thành phố.",
  "Hành trình hồi sinh không hề bằng phẳng: cuộc thi năm 2006 từng chọn phương án của kiến trúc sư Norman Foster nhưng bị đình trệ vì khủng hoảng tài chính năm 2008. Đến năm 2010, dự án được trao cho tập đoàn Millhouse gắn với Quỹ Iris, và tháng 7 năm 2011 hòn đảo mở cửa đón công chúng lần đầu kể từ thời Pyotr Đại đế. Sau chương trình thử nghiệm «Mùa hè ở Tân Hà Lan» thu hút hàng trăm nghìn lượt khách, công viên chính thức khai trương năm 2016 với sự tham gia thiết kế cảnh quan của hãng West 8 (Hà Lan), rồi lần lượt các toà nhà lịch sử được cải tạo và đưa vào sử dụng."
 ]},
 {"heading": "Kiến trúc & đặc điểm nổi bật", "paras": [
  "Về mặt kiến trúc, quần thể Tân Hà Lan được xem là một trong những ví dụ tiêu biểu của Chủ nghĩa Cổ điển sớm ở Nga, đồng thời là một di sản kiến trúc công nghiệp quý hiếm. Vật liệu chủ đạo là gạch đỏ mộc không trát vữa, kết hợp với đá granite, tạo nên vẻ đẹp mạnh mẽ, khoẻ khoắn và rất thực dụng đúng với chức năng kho tàng của nó.",
  "Ngôi sao của cả quần thể là chiếc vòm cổng bắc qua con kênh dẫn vào bể nước bên trong đảo (gọi là «Kovsh»). Cao khoảng hai mươi ba mét, vòm cổng được nâng đỡ bởi những cột đá granite đỏ đồ sộ theo thức Tuscan, kết hợp giữa sự bề thế của cổ điển với chất liệu thô mộc của gạch đá. Đây là tác phẩm để đời của Vallin de la Mothe và từ lâu đã trở thành biểu tượng thị giác của Tân Hà Lan.",
  "Bao quanh đảo là các dãy nhà kho hai tầng chạy dài, tổ chức theo nhịp điệu vòm cuốn (arcade) đều đặn, gợi cảm giác về một pháo đài trầm mặc soi bóng xuống mặt nước. Bên trong từng là hệ thống lưu trữ gỗ theo chiều đứng đầy sáng tạo của Chevakinsky – một giải pháp kỹ thuật hiếm thấy, cho phép chứa đủ gỗ để đóng hàng chục con tàu.",
  "Toà nhà gây tò mò nhất là nhà tù hải quân hình tròn – «Cái Chai». Với mặt bằng hình vành khuyên và sân trong tròn khép kín, kết cấu độc đáo này khiến nó trở thành một trong những công trình dễ nhận biết nhất trên đảo, đồng thời để lại dấu ấn cả trong ngôn ngữ đời thường của người Nga.",
  "Trong lần cải tạo hiện đại, các công trình lịch sử khác cũng được đánh thức và trao chức năng mới. Toà Xưởng Rèn cũ (Kuznya) trở thành nhà hàng và không gian ẩm thực; Nhà Chỉ huy (Commandant's House) dành cho các chương trình giáo dục, đặc biệt cho trẻ em; còn «Cái Chai» được biến thành tổ hợp cửa hàng thiết kế, thời trang, ẩm thực. Toà «Nhà số 12» mới cải tạo bổ sung thêm nhà hàng, cửa hiệu, không gian triển lãm và trung tâm cộng đồng.",
  "Triết lý cải tạo ở đây là bảo tồn tối đa di sản gốc và tái sử dụng thích ứng, thay vì xây mới ồ ạt. Nhà đầu tư tuyên bố không dựng thêm công trình mới trên đảo; phần đất trống được dành cho công viên. Cảnh quan do hãng West 8 thiết kế, với bãi cỏ trung tâm rộng chừng hai vạn bảy nghìn mét vuông, các lối dạo trồng cây, một vườn thảo mộc và những khu chức năng như sân chơi trẻ em.",
  "Chính cách tiếp cận tôn trọng lịch sử này đã được ghi nhận: năm 2018, quần thể Tân Hà Lan nhận một giải thưởng quốc tế uy tín về bảo tồn công trình lịch sử, được đánh giá là dự án đô thị xuất sắc nhờ sự phối hợp chặt chẽ giữa các bên và chất lượng trùng tu di sản kiến trúc."
 ]},
 {"heading": "Những điểm nhấn không thể bỏ lỡ", "paras": [
  "Chiếc vòm cổng đá đỏ là điểm nhấn số một và cũng là khung hình biểu tượng nhất của Tân Hà Lan. Du khách thường dừng lại chụp ảnh vòm cổng từ phía bờ kênh đối diện, nơi có thể thu trọn cả dáng vòm bề thế lẫn hình phản chiếu của nó xuống mặt nước – đặc biệt đẹp vào lúc nắng xế hoặc hoàng hôn.",
  "Bãi cỏ trung tâm là trái tim của đời sống trên đảo. Vào mùa ấm, đây là nơi lý tưởng để trải bạt nằm nghỉ, dã ngoại, đọc sách hay tham dự các buổi hoà nhạc, chiếu phim và sự kiện ngoài trời trên sân khấu chính. Không khí thư thái, dân dã ở bãi cỏ này là một tương phản dễ chịu với sự trang nghiêm của các bảo tàng lớn.",
  "Toà «Cái Chai» – nhà tù hải quân hình tròn năm xưa – nay là một trong những điểm dừng chân được yêu thích nhất, với các cửa hàng thiết kế, thời trang, tiệm ăn và không gian sáng tạo bố trí quanh sân trong. Việc dạo quanh vành khuyên của toà nhà và ngắm sân tròn ở giữa là một trải nghiệm thú vị.",
  "Toà Xưởng Rèn cũ, nay là nhà hàng Kuznya, là trung tâm ẩm thực và giao lưu của đảo. Đây là nơi thích hợp để nghỉ chân, thưởng thức đồ ăn thức uống trong một không gian mang hơi thở lịch sử đã được cải tạo tinh tế.",
  "Với các gia đình có trẻ nhỏ, sân chơi mô phỏng chiến hạm cổ «Pyotr và Pavel» là một điểm nhấn đáng nhớ. Được tạo hình theo dáng một con tàu buồm, sân chơi này gợi nhắc trực tiếp tới quá khứ đóng tàu của hòn đảo, vừa vui nhộn vừa mang tính giáo dục.",
  "Ngoài ra, du khách có thể ghé vườn thảo mộc bên cạnh Xưởng Rèn, dạo quanh bể nước Kovsh phía trong, hay tìm ngắm các tác phẩm sắp đặt nghệ thuật thường được bố trí trên đảo. Vào mùa đông, sân trượt băng dựng ngay trên bãi cỏ trung tâm trở thành điểm hẹn hấp dẫn giữa khung cảnh lung linh.",
  "Nhìn tổng thể, sức hấp dẫn của Tân Hà Lan không nằm ở một hiện vật đơn lẻ, mà ở bầu không khí chung: sự đan xen giữa những dãy kho gạch đỏ trầm mặc, mặt nước phẳng lặng, thảm cỏ xanh và một đời sống văn hoá – ẩm thực trẻ trung, khiến mỗi lần ghé thăm đều mang lại cảm giác thư thái, dễ chịu."
 ]},
 {"heading": "Ý nghĩa lịch sử – văn hoá", "paras": [
  "Tân Hà Lan mang một ý nghĩa lịch sử đặc biệt vì nó gắn liền với buổi bình minh của Sankt-Peterburg và của hải quân Nga. Là nơi lưu trữ gỗ đóng tàu và là căn cứ hải quân buổi đầu, hòn đảo là một mắt xích trong tham vọng biến nước Nga thành cường quốc biển của Pyotr Đại đế – tham vọng đã khai sinh chính thành phố này.",
  "Về mặt kiến trúc, quần thể được các nhà nghiên cứu đánh giá là một trong những ví dụ xuất sắc của Chủ nghĩa Cổ điển sớm ở Nga và là di sản kiến trúc công nghiệp hiếm hoi còn lại. Sự kết hợp giữa công năng thực dụng của kho tàng và vẻ đẹp cổ điển của chiếc vòm cổng cho thấy tư duy thẩm mỹ cao ngay cả trong những công trình mang tính kỹ thuật.",
  "Hòn đảo còn là một địa chỉ của khoa học và công nghệ hàng hải. Bể thử mô hình tàu nơi viện sĩ Aleksei Krylov làm việc đầu thế kỷ XX gắn với những bước tiến của ngành đóng tàu và lý thuyết về độ ổn định của tàu – một di sản trí tuệ ít được biết đến nhưng rất đáng kể của Tân Hà Lan.",
  "Thú vị hơn, Tân Hà Lan còn để lại dấu ấn trong chính ngôn ngữ Nga. Nhà tù hình tròn mang biệt danh «Cái Chai» được cho là nguồn gốc của thành ngữ «đừng chui vào chai» (не лезь в бутылку) – ý nói đừng tự chuốc lấy rắc rối hay nổi nóng vô cớ. Một địa danh trở thành thành ngữ là điều không phải nơi nào cũng có.",
  "Trong thời hiện đại, Tân Hà Lan trở thành biểu tượng cho xu hướng tái sinh di sản và cải tạo đô thị. Việc biến một cơ sở quân sự khép kín, hoang phế thành một công viên văn hoá mở cho công chúng được xem là hình mẫu về cách một thành phố lịch sử có thể vừa gìn giữ quá khứ, vừa tạo ra không gian sống mới cho cư dân.",
  "Sự kiện hòn đảo mở cửa trở lại năm 2011 vì thế mang ý nghĩa biểu tượng: một mảnh đất từng bị niêm phong suốt gần hai thế kỷ được trả về cho đời sống dân sự. Với nhiều người Sankt-Peterburg, đây không chỉ là một công viên mới, mà là sự phục hồi của một phần ký ức đô thị.",
  "Ngày nay, Tân Hà Lan là một trung tâm văn hoá đích thực, nơi diễn ra các buổi hoà nhạc, liên hoan phim, chợ phiên, hoạt động giáo dục và sự kiện cộng đồng quanh năm. Sự chuyển hoá từ kho gỗ và nhà tù hải quân thành không gian sáng tạo là minh chứng sinh động cho sức sống bền bỉ của một di sản khi được trao cho vai trò mới."
 ]},
 {"heading": "Trải nghiệm dành cho du khách", "paras": [
  "Trải nghiệm cốt lõi ở Tân Hà Lan là thư giãn và tận hưởng không gian. Khác với nhịp tham quan hối hả ở các cung điện, tại đây du khách có thể chậm lại: trải bạt trên bãi cỏ, ngồi ghế xếp, nhâm nhi đồ uống và ngắm nhìn những dãy kho gạch đỏ phản chiếu xuống mặt nước.",
  "Đời sống sự kiện trên đảo rất phong phú. Vào mùa hè, sân khấu chính thường tổ chức hoà nhạc, chiếu phim ngoài trời, các buổi trò chuyện và biểu diễn; các chợ phiên và lễ hội theo mùa cũng thường xuyên diễn ra. Lịch sự kiện thay đổi liên tục, nên mỗi lần ghé thăm có thể là một trải nghiệm khác nhau.",
  "Về ẩm thực, du khách có nhiều lựa chọn từ nhà hàng Kuznya trong Xưởng Rèn cũ, tới các quầy đồ ăn nhanh và quán cà phê rải rác trên đảo. Không gian ăn uống ngoài trời bên mặt nước, giữa khung cảnh lịch sử, là một điểm cộng lớn khiến nhiều người muốn nán lại lâu hơn.",
  "Với người thích mua sắm, các cửa hàng thiết kế, thời trang và đồ thủ công trong toà «Cái Chai» và «Nhà số 12» là nơi thú vị để tìm những món đồ độc đáo, thường mang dấu ấn của các thương hiệu và nghệ nhân Nga đương đại.",
  "Tân Hà Lan cũng rất thân thiện với gia đình. Sân chơi hình chiến hạm và khu vui chơi cho trẻ nhỏ, cùng các chương trình giáo dục ở Nhà Chỉ huy, biến hòn đảo thành điểm đến lý tưởng cho các gia đình có trẻ em, nơi việc học và chơi hoà làm một.",
  "Những ai ưa vận động có thể tham gia các hoạt động thể thao nhẹ nhàng như bóng rổ đường phố hay pétanque trên đảo. Mùa đông, sân trượt băng trên bãi cỏ trung tâm là hoạt động được yêu thích nhất, mang lại một trải nghiệm rất «Sankt-Peterburg» giữa tiết trời lạnh giá.",
  "Nhờ tính linh hoạt ấy, Tân Hà Lan phù hợp với nhiều kiểu du khách: người tìm chốn nghỉ ngơi yên tĩnh, gia đình có trẻ nhỏ, người mê kiến trúc – lịch sử, hay khách trẻ muốn hoà vào đời sống văn hoá đương đại của thành phố. Đây là điểm đến hiếm hoi làm hài lòng gần như mọi nhóm khách."
 ]},
 {"heading": "Mẹo tham quan", "paras": [
  "Nên kiểm tra trước giờ mở cửa và lịch sự kiện, bởi công viên hoạt động theo mùa với khung giờ khác nhau giữa hè và đông. Vào những ngày có sự kiện lớn, lượng khách có thể rất đông và đôi khi bị điều tiết, nên đến sớm sẽ dễ chịu hơn.",
  "Về mùa tham quan, cuối xuân tới đầu thu là thời điểm đẹp nhất để tận hưởng bãi cỏ và không gian ngoài trời. Nếu tới vào mùa đông, hãy chuẩn bị trang phục thật ấm để trải nghiệm sân trượt băng và khung cảnh đảo lung linh dưới ánh đèn.",
  "Hãy mang theo một tấm khăn hoặc bạt mỏng để có thể ngồi, nằm thư giãn trên bãi cỏ như người dân địa phương. Một bữa dã ngoại nhẹ, hoặc đồ uống mua tại các quầy trên đảo, sẽ khiến trải nghiệm thêm trọn vẹn.",
  "Để có bức ảnh vòm cổng đẹp nhất, du khách nên tìm góc từ phía bờ kênh đối diện, nơi thu được cả dáng vòm và hình phản chiếu. Ánh sáng dịu vào buổi chiều muộn thường cho màu gạch đỏ ấm và mặt nước lặng, rất lý tưởng để chụp hình.",
  "Về di chuyển, cách tiện nhất là đi metro tới ga Admiralteyskaya rồi tản bộ men theo sông Moika. Hãy đi giày thoải mái vì bạn sẽ đi bộ khá nhiều cả khi tới đảo lẫn khi khám phá khu Kolomna xung quanh.",
  "Nên dành ít nhất một tới hai giờ cho Tân Hà Lan, và nhiều hơn nếu bạn muốn nghỉ ngơi hoặc tham dự sự kiện. Đây là nơi lý tưởng để «hạ nhiệt» giữa một ngày tham quan dày đặc, nên đừng vội vàng lướt qua.",
  "Cuối cùng, hãy kết hợp Tân Hà Lan với các điểm gần kề như Nhà hát Mariinsky hay Nhà thờ Hải quân Thánh Nikolai để tạo thành một buổi khám phá khu Kolomna trọn vẹn, cân bằng giữa di sản trang nghiêm và không gian thư giãn hiện đại."
 ]},
 {"heading": "Khám phá xung quanh", "paras": [
  "Ngay gần Tân Hà Lan là Nhà hát Mariinsky lừng danh – một trong những thánh đường opera và ballet của thế giới. Một buổi tối thưởng thức biểu diễn tại Mariinsky sau khi dạo đảo là sự kết hợp hoàn hảo giữa thư giãn ban ngày và nghệ thuật đỉnh cao buổi tối.",
  "Nhà thờ Hải quân Thánh Nikolai, với những mái vòm dát vàng và tháp chuông thanh thoát, nằm không xa và là một điểm đến rất đáng ghé. Ngôi thánh đường mang đậm tinh thần hải quân này cộng hưởng rất tự nhiên với chủ đề biển cả của Tân Hà Lan.",
  "Khu Kolomna bao quanh đảo là một trong những góc yên tĩnh, đậm chất văn chương của Sankt-Peterburg, với những con kênh, cây cầu và dãy nhà cổ. Dạo bộ trong khu này mang lại cảm giác về một thành phố đời thường, trầm lắng, khác hẳn sự hào nhoáng của các đại lộ trung tâm.",
  "Đi dọc bờ sông Moika, du khách có thể lần tới Cung điện Yusupov – nơi gắn với vụ ám sát nhân vật Rasputin đầy bí ẩn – và xa hơn là quần thể quanh Nhà thờ Thánh Isaac cùng Quảng trường Thượng viện với tượng Kỵ sĩ Đồng.",
  "Về phía đông, hệ thống kênh Griboyedov và Quảng trường Sennaya dẫn du khách tới những địa danh gắn với văn hào Dostoevsky, rồi nối ra đại lộ Nevsky sầm uất – trục xương sống của thành phố với vô số cửa hiệu, nhà thờ và cung điện.",
  "Nhờ vị trí trung tâm, Tân Hà Lan có thể đóng vai trò điểm neo cho một ngày khám phá phần phía tây nam của trung tâm lịch sử: kết hợp đảo với Mariinsky, Nhà thờ Thánh Nikolai, Cung điện Yusupov và những lối đi ven kênh của khu Kolomna.",
  "Với các tuyến du thuyền trên sông và kênh, du khách còn có thể tiếp cận Tân Hà Lan và các thắng cảnh lân cận từ mặt nước – một cách ngắm Sankt-Peterburg rất đặc trưng, giúp hiểu vì sao thành phố này thường được ví như «Venice của phương Bắc»."
 ]},
 {"heading": "Câu chuyện & giai thoại thú vị", "paras": [
  "Giai thoại được nhắc tới nhiều nhất về Tân Hà Lan là nguồn gốc của thành ngữ «đừng chui vào chai» (не лезь в бутылку). Theo cách giải thích phổ biến, thành ngữ này bắt nguồn từ nhà tù hải quân hình tròn trên đảo – toà nhà mang biệt danh «Cái Chai». Vì thế, «chui vào chai» được hiểu là tự chuốc lấy rắc rối hoặc nổi nóng một cách vô ích.",
  "Cái tên «Tân Hà Lan» cũng ẩn chứa câu chuyện về tình yêu của Pyotr Đại đế dành cho Hà Lan. Vốn từng cải trang đi học nghề đóng tàu ở Hà Lan, Sa hoàng đã đưa các thợ đóng tàu Hà Lan tới đây và cho khu vực này một diện mạo gợi nhớ những con kênh Amsterdam. Tương truyền, ông còn dựng một cung điện gỗ nhỏ bên chiếc ao trên đảo để nghỉ ngơi.",
  "Quá trình xây dựng chiếc vòm cổng để lại một giai thoại nghề nghiệp thú vị. Người ta kể rằng kỹ sư Johann Gerard, khi tiếp quản công trình, đã tuyên bố «làm mất» bản vẽ của Vallin de la Mothe để thi công theo phương án riêng; nhưng Bộ Hải quân vẫn giữ được một bản sao, buộc ông phải xây theo thiết kế gốc – một chi tiết cho thấy những va chạm giữa các kiến trúc sư và kỹ sư thời đó.",
  "Đầu thế kỷ XX, Tân Hà Lan còn là nơi đặt một trong những trạm vô tuyến mạnh nhất nước Nga đế quốc. Theo một số nguồn, chính trạm vô tuyến này đã tham gia truyền đi những thông điệp trong biến động cách mạng năm 1917 – một chi tiết thường được kể lại như minh chứng cho vai trò lịch sử bất ngờ của hòn đảo vốn chỉ được biết đến như kho gỗ và căn cứ hải quân.",
  "Suốt gần hai thế kỷ khép kín dưới sự quản lý của hải quân rồi quân đội, Tân Hà Lan phủ lên mình một lớp bí ẩn trong mắt người dân thành phố. Ở ngay trung tâm mà lại không thể bước vào, hòn đảo trở thành một «vùng trắng» đầy tò mò trên bản đồ Sankt-Peterburg – điều khiến sự kiện mở cửa năm 2011 càng thêm ý nghĩa.",
  "Chương hồi sinh đương đại của đảo gắn với những cái tên và sự kiện đáng chú ý. Dự án cải tạo được hậu thuẫn bởi Quỹ Iris và tập đoàn Millhouse; cuộc thi ý tưởng quốc tế quy tụ nhiều văn phòng kiến trúc danh tiếng thế giới, và phần thắng thuộc về một hãng đến từ New York với ý tưởng biến hòn đảo thành «một thành phố trong lòng thành phố».",
  "Ngày nay, những buổi hoà nhạc và sự kiện văn hoá trên bãi cỏ trung tâm đã viết tiếp chương mới cho hòn đảo. Từ một kho gỗ đóng tàu và một nhà tù hải quân, Tân Hà Lan đã trở thành nơi người ta tới để nghe nhạc, xem phim, trượt băng và gặp gỡ – một cái kết hậu đẹp đẽ cho câu chuyện dài của mảnh đất tam giác nhỏ bé giữa lòng Sankt-Peterburg."
 ]},
]

data = {
 "slug": "new-holland-island",
 "name_vi": "Đảo Tân Hà Lan (Nô-vai-a Gôn-lan-đi-a)",
 "name_ru": "Новая Голландия",
 "name_en": "New Holland Island",
 "subtitle": "Hòn đảo nhân tạo hình tam giác ở trung tâm Sankt-Peterburg, hình thành từ đầu thế kỷ XVIII bởi sông Moika và hai con kênh: khởi đầu là kho gỗ đóng tàu và căn cứ hải quân của Pyotr Đại đế, nổi tiếng với chiếc vòm cổng đá đỏ của Vallin de la Mothe và nhà tù tròn «Cái Chai», khép kín gần hai thế kỷ rồi hồi sinh từ năm 2011 thành một công viên văn hoá đô thị được yêu mến.",
 "sections": sections,
 "highlights": [
   "Hòn đảo nhân tạo hình tam giác ở trung tâm Sankt-Peterburg, hình thành khoảng năm 1719 từ sông Moika và hai con kênh.",
   "Do Pyotr Đại đế lập làm kho gỗ đóng tàu và căn cứ hải quân; tên «Tân Hà Lan» gợi nhớ tình yêu của ông với Hà Lan.",
   "Vòm cổng đá đỏ trứ danh của kiến trúc sư Vallin de la Mothe, cao khoảng 23 m — biểu tượng của đảo.",
   "Nhà tù hải quân hình tròn mang biệt danh «Cái Chai» (Butylka) — được cho là nguồn gốc một thành ngữ Nga.",
   "Bể thử mô hình tàu nơi viện sĩ Aleksei Krylov làm việc đầu thế kỷ XX.",
   "Từ 2011 hồi sinh thành công viên văn hoá, mở cửa cho công chúng lần đầu kể từ thời Pyotr Đại đế.",
 ],
 "images": [
   img("Арка Новой Голландии.jpg", "Vòm cổng đá đỏ của Tân Hà Lan — biểu tượng của đảo"),
   img("Ансамбль «Новая Голландия», Санкт-Петербург.jpg", "Quần thể kho gạch đỏ và vòm cổng nhìn từ mặt nước"),
   img("Санкт-Петербург, Новая Голландия сверху.jpg", "Toàn cảnh hòn đảo tam giác nhìn từ trên cao"),
   img("New Holland Park, St. Petersburg.jpg", "Bãi cỏ và công viên trung tâm trên đảo"),
   img("Новая Голландия в Санкт-Петербурге летом 2017 года.jpg", "Không gian công viên Tân Hà Lan mùa hè"),
   img("Новая Голландия, кузня.jpg", "Toà Xưởng Rèn (Kuznya) đã được cải tạo thành không gian ẩm thực"),
 ],
 "references": [
   {"title": "Wikipedia — New Holland Island", "url": "https://en.wikipedia.org/wiki/New_Holland_Island"},
   {"title": "New Holland (chính thức) — Lịch sử thế kỷ XVIII", "url": "https://www.newhollandsp.ru/en/history/xviii-century/"},
   {"title": "New Holland (chính thức) — Lịch sử cận đại (Recent history)", "url": "https://www.newhollandsp.ru/en/history/recent-history/"},
   {"title": "Wikipedia — Jean-Baptiste Vallin de la Mothe", "url": "https://en.wikipedia.org/wiki/Jean-Baptiste_Vallin_de_la_Mothe"},
   {"title": "Saint-Petersburg.com — New Holland", "url": "http://www.saint-petersburg.com/buildings/new-holland/"},
   {"title": "In Your Pocket — New Holland: the most famous island in the city", "url": "https://www.inyourpocket.com/st-petersburg-en/new-holland-the-most-famous-island-in-the-city_75476f"},
   {"title": "Russiable — New Holland Island St. Petersburg: Visit Guide", "url": "https://russiable.com/new-holland-island-st-petersburg/"},
   {"title": "Wikimedia Commons — Category: New Holland (Saint Petersburg)", "url": "https://commons.wikimedia.org/wiki/Category:New_Holland_(Saint_Petersburg)"},
 ],
 "sources": [
   "Wikipedia tiếng Anh, mục «New Holland Island» (hình thành 1719, tên gọi, kho gỗ, vòm cổng de la Mothe, nhà tù, bể thử tàu của Krylov, trạm vô tuyến 1915, lịch sử tái thiết).",
   "Trang chính thức newhollandsp.ru, phần «History — XVIII century»: Korobov, Chevakinsky và hệ lưu trữ gỗ theo chiều đứng, Vallin de la Mothe, kỹ sư Gerard, quá trình dựng vòm cổng.",
   "Trang chính thức newhollandsp.ru, phần «Recent history»: chuyển giao 2004, phương án Foster 2006, Millhouse 2010, mở cửa 2011, công viên 2016, các toà nhà 2016–2022, giải thưởng 2018.",
   "Wikipedia tiếng Anh, mục «Jean-Baptiste Vallin de la Mothe» (kiến trúc sư của vòm cổng).",
   "Các trang du lịch saint-petersburg.com, inyourpocket.com và russiable.com về lịch sử «Cái Chai», kích thước vòm cổng và trải nghiệm tham quan.",
   "Kho ảnh Wikimedia Commons, chuyên mục «New Holland (Saint Petersburg)» và «Arch of New Holland» (đối chiếu hình ảnh, tên file).",
 ],
}

out = os.path.join(HERE, "doc_new-holland-island.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

wc = sum(len(p.split()) for s in sections for p in s["paras"])
print("WROTE", out)
print("sections:", len(sections), "| body words:", wc)
