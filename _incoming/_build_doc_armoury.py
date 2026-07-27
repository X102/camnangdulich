# -*- coding: utf-8 -*-
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

d = {
 "slug": "kremlin-armoury",
 "name_vi": "Bảo tàng Kho báu Kremlin (Oruzheynaya Palata)",
 "name_ru": "Оружейная палата",
 "name_en": "Kremlin Armoury (Armoury Chamber)",
 "subtitle": "Kho báu hoàng gia trong lòng Điện Kremlin — nơi cất giữ mũ miện Monomakh, những chiếc ngai vàng, xe ngựa dát vàng, lễ phục đăng quang và mười quả trứng Phục sinh Fabergé của các Sa hoàng Nga.",
 "sections": [],
 "highlights": [
   "Mười quả trứng Phục sinh Hoàng gia Fabergé — bộ sưu tập vào hàng lớn nhất thế giới; nổi bật là quả 'Điện Kremlin Moskva' (1906) lớn nhất, mô phỏng Nhà thờ Uspensky.",
   "Mũ miện Monomakh (thế kỷ 14) — vương miện cổ nhất, dùng để tấn phong các Sa hoàng suốt thế kỷ 16–17.",
   "Ngai đôi độc nhất vô nhị (1682) làm cho hai vị vua nhỏ tuổi Ivan V và Pyotr I, phía sau có ô cửa bí mật để nhiếp chính Sofia nhắc lời.",
   "Đại sảnh xe ngựa nghi lễ thế kỷ 16–18: xe của Nữ hoàng Elizaveta, của Ekaterina Đại đế và cỗ xe cưới hoàng gia Romanov.",
   "Lễ phục đăng quang và long bào đính hàng vạn viên ngọc trai, đá quý; kho vũ khí, áo giáp và mũ trụ 'Jericho' (1621) từng in trên quốc huy Nga.",
   "Cùng toà nhà còn có Quỹ Kim cương với Vương miện Lớn của Đế chế và viên kim cương Orlov (tham quan bằng vé riêng)."
 ],
 "images": [
   {"url":"https://commons.wikimedia.org/wiki/Special:FilePath/State%20Armoury%20Chamber%20fa%C3%A7ade%20-%20Moscow%20Kremlin%20(19344680373).jpg","caption":"Mặt tiền toà nhà Oruzheynaya Palata do KTS Konstantin Ton thiết kế (1851)"},
   {"url":"https://commons.wikimedia.org/wiki/Special:FilePath/Kremlin%20Armoury%20interior%2008%20by%20shakko.jpg","caption":"Không gian trưng bày lộng lẫy bên trong bảo tàng"},
   {"url":"https://commons.wikimedia.org/wiki/Special:FilePath/Monomakh%27s%20Cap%20-%20by%20shakko%2011.jpg","caption":"Mũ miện Monomakh — vương miện cổ nhất của các Sa hoàng"},
   {"url":"https://commons.wikimedia.org/wiki/Special:FilePath/Faberge%20eggs%20in%20Kremlin%20Armoury%2001%20by%20shakko.jpg","caption":"Bộ sưu tập trứng Phục sinh Fabergé trứ danh"},
   {"url":"https://commons.wikimedia.org/wiki/Special:FilePath/Moscow%20Kremlin%20Egg.jpg","caption":"Quả trứng 'Điện Kremlin Moskva' (1906) — lớn nhất trong bộ sưu tập"},
   {"url":"https://commons.wikimedia.org/wiki/Special:FilePath/Old%20Oruzheinaya%20Palata.jpg","caption":"Toà nhà Cung Vũ khí cũ trong tư liệu lịch sử"}
 ],
 "references": [
   {"title":"Kremlin Armoury — Wikipedia (tiếng Anh)","url":"https://en.wikipedia.org/wiki/Kremlin_Armoury"},
   {"title":"10 MAIN masterpieces of the Moscow Kremlin’s Armory Chamber — Gateway to Russia","url":"https://www.gw2ru.com/history/246121-moscow-kremlin-armory-chamber-masterpieces"},
   {"title":"Moscow Kremlin Museums — Vé & thông tin chính thức (kreml.ru)","url":"https://kreml.ru/en/tickets"},
   {"title":"Armoury Chamber — Rusmania","url":"https://rusmania.com/central/moscow-federal-city/moscow/central-moscow/around-the-kremlin/armoury-chamber"},
   {"title":"Moscow Kremlin: Tickets, What to See & Tips — Russiable","url":"https://russiable.com/kremlin-moscow-buy-tickets-online/"},
   {"title":"Diamond Fund (Quỹ Kim cương) — Wikipedia","url":"https://en.wikipedia.org/wiki/Diamond_Fund"},
   {"title":"Wikimedia Commons — Category: Kremlin Armoury","url":"https://commons.wikimedia.org/wiki/Category:Kremlin_Armoury"}
 ],
 "sources": [
   "Bách khoa toàn thư mở Wikipedia (mục 'Kremlin Armoury', tiếng Anh) — nguồn gốc kho vũ khí hoàng gia năm 1508, các lần sáp nhập, sắc lệnh năm 1806 của Aleksandr I, toà nhà năm 1851 của Konstantin Ton, 10 quả trứng Fabergé và việc Lenin ra lệnh dồn báu vật hoàng gia về đây.",
   "Gateway to Russia ('10 MAIN masterpieces of the Moscow Kremlin’s Armory Chamber') — ngày thành lập bảo tàng 10/3/1806, con số khoảng 4.000 hiện vật, cùng mô tả các kiệt tác: trứng Fabergé 'Điện Kremlin', mũ Monomakh, ngai đôi, xe ngựa của Elizaveta, mũ trụ Jericho của Nikita Davydov, cúp hình thuyền và bộ đồ sứ Olympic của xưởng Sèvres.",
   "Trang chính thức Bảo tàng Điện Kremlin (kreml.ru) — các khung giờ tham quan cố định, giá vé và quy định đặt vé trước.",
   "Rusmania — chi tiết hiện vật: ngai ngà voi của Ivan Bạo chúa, ngai đôi cùng ô cửa bí mật của nhiếp chính Sofia, bộ sưu tập xe ngựa và lễ phục hoàng gia.",
   "Russiable ('Moscow Kremlin: Tickets, What to See & Tips') — hướng dẫn thực tế: quầy vé số 6–8 ở Vườn Aleksandr, đến sớm khoảng 45 phút, mang hộ chiếu, quy định cấm chụp ảnh.",
   "Wikipedia (mục 'Diamond Fund') — Quỹ Kim cương đặt trong cùng toà nhà, với Vương miện Lớn của Đế chế và viên kim cương Orlov.",
   "Wikimedia Commons — nguồn hình ảnh tự do bản quyền (mặt tiền, nội thất, mũ Monomakh và trứng Fabergé)."
 ]
}

S = d["sections"]
def sec(h, paras): S.append({"heading": h, "paras": paras})

sec("Giới thiệu chung", [
"Ẩn mình ở góc tây nam bên trong Điện Kremlin, Oruzheynaya Palata — thường được dịch là 'Cung Vũ khí' — thực chất là kho báu hoàng gia và là một trong những bảo tàng lâu đời bậc nhất nước Nga. Cái tên dễ gây hiểu lầm: dù có nguồn gốc từ kho binh khí của các Sa hoàng, nơi đây ngày nay trưng bày chủ yếu những báu vật lộng lẫy nhất của vương triều Nga, chứ không phải gươm giáo.",
"Bộ sưu tập gồm khoảng bốn nghìn hiện vật nghệ thuật trang trí và ứng dụng, trải dài từ thế kỷ 5 đến thế kỷ 20, quy tụ tinh hoa thủ công của cả Nga, Tây Âu lẫn phương Đông. Ở đây có vương miện và quyền trượng, ngai vàng, lễ phục đăng quang, xe ngựa nghi lễ dát vàng, vũ khí và áo giáp danh dự, cùng vô số kiệt tác kim hoàn và quà tặng ngoại giao quý giá.",
"Những 'ngôi sao' của bảo tàng đủ khiến bất kỳ ai cũng phải trầm trồ: mười quả trứng Phục sinh Hoàng gia Fabergé — một trong những bộ sưu tập lớn nhất thế giới; mũ miện Monomakh huyền thoại từng đội lên đầu các Sa hoàng; chiếc ngai ngà voi của Ivan Bạo chúa; và cỗ ngai đôi độc nhất vô nhị làm cho hai vị vua nhỏ tuổi cùng trị vì.",
"Toàn bộ kho báu được trưng bày trong một toà nhà xây năm 1851 do kiến trúc sư Konstantin Ton thiết kế, nằm trong quần thể Đại Cung điện Kremlin. Chính người kiến trúc sư này cũng là tác giả của Đại Cung điện Kremlin và Nhà thờ Chúa Cứu Thế, nên toà bảo tàng hoà hợp trọn vẹn với phong cách của cả khu vực nghi lễ trong Kremlin.",
"Ngay trong cùng toà nhà còn có một 'kho báu trong kho báu': Quỹ Kim cương (Almazny Fond). Đây là nơi cất giữ Vương miện Lớn của Đế chế Nga cùng những viên kim cương trứ danh như Orlov — được tham quan bằng một tấm vé riêng. Sự hiện diện của Quỹ Kim cương biến khu vực này thành nơi tập trung nhiều bảo vật giá trị bậc nhất nước Nga.",
"Với người hướng dẫn, Oruzheynaya Palata là điểm đến 'đắt giá' nhất khi nói về sự xa hoa của vương triều Nga. Tuy nhiên, do là bảo tàng đặc biệt, nơi đây chỉ đón khách theo các khung giờ cố định và bán vé tách riêng với vé vào Kremlin. Vì thế, việc lên kế hoạch và đặt vé trước là điều bắt buộc để không bỏ lỡ."
])

sec("Vị trí & cách di chuyển", [
"Bảo tàng nằm ở góc tây nam bên trong Điện Kremlin, gần Tháp Borovitskaya. Muốn vào, du khách trước tiên phải tiến vào Kremlin qua cụm Tháp Kutafya và Tháp Troitskaya từ phía Vườn Aleksandr — đây là lối vào chính dành cho khách tham quan. Sau khi qua cửa an ninh, bạn sẽ đi bộ một quãng trong khuôn viên Kremlin để tới toà Oruzheynaya Palata.",
"Về tàu điện ngầm, khu vực này có cả một cụm nhà ga rất thuận tiện: Aleksandrovsky Sad, Biblioteka imeni Lenina, Borovitskaya và Arbatskaya nằm sát nhau và nối thông dưới lòng đất, ngoài ra ga Okhotny Ryad cũng chỉ cách vài phút đi bộ. Từ bất kỳ ga nào trong số này, bạn đều dễ dàng tìm đường ra Vườn Aleksandr để mua vé và xếp hàng.",
"Điểm mấu chốt là các quầy vé. Vé vào Oruzheynaya Palata được bán tại các quầy số 6, 7 và 8 đặt trong Vườn Aleksandr. Kinh nghiệm chung là nên có mặt sớm ít nhất 45 phút trước khung giờ tham quan của mình, để kịp mua/đổi vé, qua kiểm tra an ninh và đi bộ vào tới cửa bảo tàng mà không phải vội vàng.",
"Cần nhớ rằng vé Oruzheynaya Palata hoàn toàn tách biệt với vé tham quan khuôn viên Kremlin và Quảng trường Nhà thờ. Nếu muốn xem cả hai, bạn phải mua hai loại vé và sắp xếp thời gian khéo léo, bởi việc vào bảo tàng bị ràng buộc bởi khung giờ cố định in trên vé.",
"Bảo tàng áp dụng cơ chế vào cửa theo suất giờ và không cho ra vào tự do nhiều lần. Bên trong có phòng gửi đồ để khách gửi áo khoác, túi lớn trước khi tham quan. Vì là khu vực bảo mật cao trong Kremlin, du khách nên mang theo hộ chiếu và tuân thủ hướng dẫn của nhân viên an ninh.",
"Một cách sắp xếp hợp lý là kết hợp tham quan Oruzheynaya Palata với Quảng trường Nhà thờ ngay trong cùng buổi. Chẳng hạn, chọn suất bảo tàng buổi sáng rồi dành thời gian còn lại dạo các nhà thờ, ngắm Chuông Sa hoàng và Đại bác Sa hoàng trong khuôn viên — như vậy chỉ cần vào Kremlin một lần mà xem được nhiều điểm."
])

sec("Lịch sử hình thành và phát triển", [
"Cội nguồn của bảo tàng là kho binh khí và các xưởng thủ công hoàng gia hình thành từ năm 1508. Đây là nơi quy tụ những nghệ nhân giỏi nhất Moskva: các thợ rèn súng lừng danh (anh em nhà Vyatkin), thợ kim hoàn tài hoa (Gavrila Ovdokimov) và các hoạ sĩ bậc thầy như Simon Ushakov. Kho không chỉ chế tạo vũ khí mà còn sản xuất, mua sắm và bảo quản trang sức cùng vật dụng của các Sa hoàng.",
"Theo thời gian, kho ngày càng giàu có và tinh hoa. Vào các năm 1640 và 1683, những xưởng vẽ icon và hội hoạ được mở ngay tại đây để truyền dạy nghề. Đến năm 1700, kho được bổ sung thêm báu vật từ các 'buồng Vàng' và 'buồng Bạc' của hoàng gia — hợp nhất nhiều dòng chảy quý vật về một đầu mối duy nhất trong Kremlin.",
"Bước ngoặt đến vào thời Pyotr Đại đế. Năm 1711, ông chuyển phần lớn thợ giỏi về kinh đô mới Sankt-Peterburg. Khoảng mười lăm năm sau, kho vũ khí được sáp nhập với Sân Ngân khố (kho lưu trữ báu vật lâu đời nhất), Kho Chuồng ngựa (giữ yên cương và xe) cùng Buồng May (lo trang phục cho hoàng gia), rồi đổi tên thành 'Buồng Vũ khí và Thợ cả'.",
"Cột mốc trở thành bảo tàng công cộng đến vào năm 1806. Ngày 10 tháng 3 năm ấy, Hoàng đế Aleksandr I ban sắc lệnh lập bảo tàng dựa trên các kho báu hoàng gia đã tích luỹ qua nhiều thế kỷ — biến Oruzheynaya Palata thành bảo tàng công cộng đầu tiên của Moskva. Tuy vậy, phải khoảng bảy năm sau, bộ sưu tập mới thực sự mở cửa đón công chúng.",
"Toà nhà hiện nay ra đời năm 1851, được kiến trúc sư Konstantin Ton dựng riêng cho bảo tàng như một phần của quần thể Đại Cung điện Kremlin. Suốt thế kỷ 19, nơi đây phát triển thành bảo tàng kho báu của đế chế, trưng bày một cách hệ thống những vương miện, lễ phục, vũ khí và kiệt tác kim hoàn của các triều đại.",
"Sau Cách mạng năm 1917, số phận của bảo tàng gắn với một biến động lớn. Khi các cung điện của hoàng gia bị tịch thu, báu vật của họ được chuyển về Kremlin Armoury theo lệnh của Lenin. Nhờ đó, rất nhiều bảo vật vốn phân tán khắp nơi đã được dồn về một chỗ, khiến bộ sưu tập thêm phong phú dù trong hoàn cảnh đầy xáo trộn.",
"Thời Xô-viết cũng để lại những mất mát. Trong thập niên 1920–1930, vì cần ngoại tệ, chính quyền đã bán ra nước ngoài một số báu vật, trong đó có vài quả trứng Fabergé — lý do vì sao ngày nay các quả trứng này nằm rải rác trong nhiều bộ sưu tập trên thế giới. Dù vậy, phần cốt lõi vẫn được gìn giữ, và ngày nay Oruzheynaya Palata là một thành viên trọng yếu của hệ thống Bảo tàng Điện Kremlin, nổi danh toàn cầu."
])

sec("Kiến trúc & đặc điểm nổi bật", [
"Toà nhà bảo tàng là tác phẩm của Konstantin Ton, kiến trúc sư trưởng dưới thời Nikolai I và cũng là tác giả của Đại Cung điện Kremlin liền kề. Ông theo phong cách Nga–Byzantine, dùng những đường nét và vật liệu ăn nhập với cung điện, để toà Oruzheynaya Palata trở thành một phần hài hoà của khu vực nghi lễ trong Kremlin thay vì một khối tách biệt.",
"Mặt tiền được điểm xuyết bằng các cột và chi tiết chạm khắc đá trắng tinh xảo, cùng những huy hiệu, phù điêu gợi nhắc các Sa hoàng Nga. Sự kết hợp giữa tường sáng màu và trang trí cầu kỳ mang lại vẻ trang trọng, uy nghi đúng với chức năng cất giữ báu vật quốc gia của công trình.",
"Bên trong, không gian trưng bày trải trên hai tầng với chín gian (hall) được tổ chức theo chủ đề. Các gian lần lượt dành cho đồ vàng bạc của Nga, đồ bạc nghệ thuật Tây Âu, kho vũ khí và áo giáp, ngai vàng cùng vương phục đăng quang, trang phục cung đình, và cuối cùng là đại sảnh xe ngựa với yên cương nghi lễ. Cách sắp đặt theo nhóm giúp du khách dễ theo dõi từng dòng báu vật.",
"Ánh sáng trong bảo tàng được giữ ở mức dịu và tập trung nhằm bảo vệ hiện vật — nhiều món trong số đó vô cùng nhạy cảm với ánh sáng và độ ẩm. Chính bầu không khí trầm, lấp lánh ánh vàng bạc sau những tủ kính ấy tạo cho không gian một vẻ huyền bí, khiến khách tham quan như lạc vào kho tàng của một câu chuyện cổ tích.",
"Cần lưu ý rằng bên trong Oruzheynaya Palata cấm chụp ảnh và quay phim để bảo vệ các di sản. Điều này khác với nhiều bảo tàng khác và khiến trải nghiệm ở đây mang tính 'chiêm ngưỡng bằng mắt' nhiều hơn. Vì thế, một máy thuyết minh hoặc hướng dẫn viên tốt sẽ giúp bạn ghi nhớ câu chuyện thay cho những bức ảnh.",
"Cũng trong toà nhà này, ở khu vực riêng, là Quỹ Kim cương — một triển lãm tách biệt với vé riêng. Việc bố trí hai bộ sưu tập vô giá trong cùng một công trình cho thấy vai trò của toà nhà như một 'két sắt' của quốc gia, nơi hội tụ những gì tinh xảo và quý giá nhất mà nghệ thuật Nga từng tạo ra."
])

sec("Những điểm nhấn không thể bỏ lỡ", [
"Ngôi sao sáng nhất chắc chắn là bộ sưu tập trứng Phục sinh Fabergé. Bảo tàng lưu giữ mười quả trong số những quả trứng hoàng gia do nghệ nhân Carl Fabergé chế tác — món quà xa xỉ mà gia đình Sa hoàng tặng nhau mỗi dịp lễ Phục sinh. Nổi bật nhất là quả 'Điện Kremlin Moskva' (1906), quả lớn nhất, mô phỏng Nhà thờ Uspensky và làm để kỷ niệm chuyến thăm Moskva của Nikolai II.",
"Kế đến là các vương phục đăng quang, mà quan trọng nhất là mũ miện Monomakh có từ thế kỷ 14. Đây là chiếc mũ dùng để tấn phong hầu hết các Sa hoàng trong thế kỷ 16–17. Chiếc mũ lông viền vàng nạm đá quý này được cho là do thợ của Hãn quốc Kim Trướng chế tác, dù truyền thuyết lại kể rằng nó là quà của hoàng đế Byzantine tặng cho công tước Vladimir Monomakh.",
"Bộ sưu tập ngai vàng cũng đặc sắc không kém, từ những chiếc ngai bằng kim loại quý và đá quý cho tới ngai chạm từ ngà voi gắn với Ivan Bạo chúa. Độc đáo nhất là cỗ ngai đôi làm năm 1682 cho hai anh em Ivan V và Pyotr I cùng lên ngôi — phía sau ngai có một ô cửa bí mật, tương truyền để người chị nhiếp chính Sofia đứng nhắc lời cho hai vị vua nhỏ tuổi trong các buổi thiết triều.",
"Đại sảnh xe ngựa là một điểm dừng chân khó quên. Ở đây có đủ loại, từ những cỗ xe nhỏ xinh cho tới các cỗ xe hoàng gia mạ vàng lộng lẫy: xe của Nữ hoàng Elizaveta Petrovna (1746), xe của Ekaterina Đại đế, hay cỗ xe cưới của hoàng gia Romanov. Nhiều chiếc trong số đó từng lăn bánh trong các đoàn rước đăng quang tiến vào Kremlin.",
"Khu vũ khí và áo giáp giới thiệu tài nghệ của các thợ rèn Nga lẫn ngoại quốc. Nổi bật là chiếc mũ trụ 'Jericho' năm 1621 do nghệ nhân Nikita Davydov chế tác cho Sa hoàng Mikhail Fedorovich — vị vua Romanov đầu tiên. Sang thế kỷ 19, người ta thêu dệt rằng chiếc mũ từng thuộc về anh hùng Aleksandr Nevsky, và hình ảnh của nó thậm chí được đưa lên quốc huy lớn của Đế chế Nga.",
"Gian kim hoàn và đồ bạc trưng bày những kiệt tác gắn với đức tin và ngoại giao: icon 'Đức Mẹ Vladimir' trong khung bạc vàng thế kỷ 16, cùng vô số cúp và quà tặng của các sứ thần. Đáng chú ý có chiếc cúp hình con thuyền (1648) mà một vị đại thần dâng lên Sa hoàng Aleksey Mikhailovich, và bộ đồ sứ 'Olympic' do xưởng Sèvres của Pháp làm — vốn là quà Napoleon tặng Aleksandr I sau Hoà ước Tilsit.",
"Nếu còn thời gian và hứng thú, đừng bỏ lỡ Quỹ Kim cương ngay trong toà nhà (vé riêng). Đây là nơi trưng bày Vương miện Lớn của Đế chế Nga — chiếc vương miện làm năm 1762 cho lễ đăng quang của Ekaterina Đại đế, gắn hàng nghìn viên kim cương — cùng viên kim cương Orlov trứ danh. Đó là màn 'kết' hoàn hảo cho một hành trình ngập tràn châu báu."
])

sec("Ý nghĩa lịch sử – văn hoá", [
"Oruzheynaya Palata là 'ký ức vật chất' của chế độ quân chủ Nga. Mỗi chiếc vương miện, quyền trượng hay long bào ở đây đều không đơn thuần là đồ trang sức, mà là biểu tượng của tính chính danh. Việc mũ Monomakh được gắn với truyền thuyết Byzantine chẳng hạn, chính là cách các Sa hoàng khẳng định họ thừa kế dòng quyền lực nối từ Kiev cổ và cả đế chế Đông La Mã.",
"Bảo tàng cũng là cái nôi của nghệ thuật ứng dụng Nga. Trong nhiều thế kỷ, các xưởng thủ công tại đây đã đào tạo hết thế hệ nghệ nhân này đến thế hệ khác — thợ kim hoàn, thợ rèn, hoạ sĩ icon. Nhìn vào những hiện vật trưng bày, ta đọc được cả một quá trình phát triển của tay nghề và thẩm mỹ Nga, từ thời trung cổ cho tới đỉnh cao xa hoa của thế kỷ 19.",
"Bộ sưu tập còn là một cuốn biên niên sử ngoại giao. Rất nhiều báu vật là quà tặng của các sứ đoàn từ Anh, Ba Tư, Ba Lan, Thổ Nhĩ Kỳ hay các nước Tây Âu, phản ánh mạng lưới bang giao rộng lớn của nước Nga qua các thời kỳ. Chiếc cúp hình thuyền hay bộ đồ sứ của Napoleon là những minh chứng sống động cho những mối quan hệ ấy.",
"Số phận thăng trầm của bảo tàng cũng mang nhiều tầng ý nghĩa. Việc dồn báu vật hoàng gia về đây sau cách mạng, rồi bán bớt một phần ra nước ngoài, phản ánh cả những biến động dữ dội của thế kỷ 20 lẫn giá trị vật chất khổng lồ của bộ sưu tập. Những gì còn lại hôm nay vì thế càng đáng quý, như những mảnh ghép sống sót của một thế giới đã mất.",
"Là kho lưu giữ vật phẩm đăng quang, bảo tàng còn tượng trưng cho tính liên tục của quyền lực. Nhiều hiện vật được sử dụng lặp đi lặp lại qua các lễ đăng quang diễn ra ngay trong Kremlin suốt nhiều thế kỷ. Đứng trước chúng, du khách như chạm vào sợi dây nối liền các triều đại — từ những Sa hoàng đầu tiên đến vị hoàng đế cuối cùng.",
"Với du khách Việt Nam, Oruzheynaya Palata có lẽ là nơi gần nhất để 'nhìn thấy tâm hồn' của nước Nga Sa hoàng chỉ trong vài gian phòng. Sự xa hoa tột bậc ở đây giúp ta hình dung rõ hơn về một thời đại quân chủ đã định hình nên phần lớn di sản văn hoá mà nước Nga tự hào cho đến ngày nay."
])

sec("Trải nghiệm dành cho du khách", [
"Một suất tham quan Oruzheynaya Palata thường kéo dài khoảng 1,5 đến 2 giờ, đi qua chín gian trưng bày. Không gian ở đây đậm đặc hiện vật quý, lấp lánh ánh vàng bạc sau những tủ kính, tạo cảm giác như bước vào một chiếc 'hộp trang sức' khổng lồ. Mật độ báu vật dày đặc khiến nhiều du khách choáng ngợp và phải đi chậm để cảm nhận hết.",
"Vì bên trong cấm chụp ảnh, trải nghiệm ở đây thiên về việc chiêm ngưỡng trực tiếp bằng mắt. Đây thực ra lại là một cái hay: không bận rộn với điện thoại, du khách có thể toàn tâm quan sát các chi tiết tinh xảo và lắng nghe câu chuyện phía sau từng hiện vật. Một chiếc máy thuyết minh vì thế trở thành người bạn đồng hành quý giá.",
"Vào các khung giờ cao điểm, bảo tàng khá đông vì lượng vé mỗi suất có hạn. Dù vậy, chính cảm giác 'phải xếp lịch, phải chờ đến suất của mình' lại làm tăng thêm sự trân trọng khi cuối cùng được bước vào. Nhiều người mô tả khoảnh khắc đứng trước mũ Monomakh hay trứng Fabergé là điểm nhấn đáng nhớ nhất của cả chuyến đi Nga.",
"Về ngôn ngữ, chú thích hiện vật chủ yếu bằng tiếng Nga, nên máy thuyết minh tiếng Anh hoặc một hướng dẫn viên là gần như bắt buộc để hiểu trọn giá trị của bộ sưu tập. Với những món gắn liền các câu chuyện lịch sử ly kỳ như ngai đôi hay mũ trụ Jericho, phần thuyết minh chính là thứ 'thổi hồn' vào hiện vật.",
"Về tiện ích và lưu ý thực tế: bảo tàng có phòng gửi đồ, và du khách nên hạn chế mang túi lớn. Vì phải đi bộ một quãng trong Kremlin để tới bảo tàng, hãy chuẩn bị giày thoải mái, nhất là trong thời tiết lạnh hoặc mưa. Người đi cùng trẻ nhỏ nên lưu ý không gian đông và nhiều tủ kính, cần trông chừng các em.",
"Để trọn vẹn, bạn có thể kết hợp Oruzheynaya Palata với Quỹ Kim cương (vé riêng, cùng toà nhà) và Quảng trường Nhà thờ trong khuôn viên Kremlin. Ba trải nghiệm này bổ sung cho nhau: báu vật hoàng gia, kim cương quốc bảo và các thánh đường cổ kính — cùng vẽ nên bức tranh đầy đủ về quyền lực và đức tin của nước Nga xưa."
])

sec("Mẹo tham quan", [
"Trước hết, hãy nắm chắc lịch và khung giờ. Bảo tàng mở cửa hằng ngày trừ thứ Năm, và chỉ đón khách theo bốn suất cố định: 10:00, 12:00, 14:30 và 16:30. Vé của mỗi suất có hạn, nên bạn không thể vào tuỳ ý như nhiều bảo tàng khác — điều này bắt buộc phải tính trước khi lên lịch trình trong ngày.",
"Về giá vé, người lớn khoảng 1.400 rúp, khách dưới 16 tuổi khoảng 800 rúp, còn trẻ dưới 7 tuổi thường được miễn phí (giá có thể thay đổi theo thời điểm). Quan trọng nhất: hãy đặt vé trực tuyến trước qua trang tickets.kreml.ru. Vé thường mở bán trước ngày tham quan khoảng hơn hai tuần và rất dễ 'cháy' vào mùa cao điểm, nên đặt sớm là thượng sách.",
"Đến nơi, hãy dành đủ thời gian đệm. Nên có mặt ở Vườn Aleksandr sớm khoảng 45 phút trước suất của mình để lấy/đổi vé ở các quầy số 6, 7, 8, qua cửa an ninh tại Tháp Kutafya–Troitskaya và đi bộ vào bảo tàng. Nhớ mang theo hộ chiếu, vì giấy tờ có thể được yêu cầu khi kiểm tra.",
"Nếu có quyền chọn, hãy ưu tiên suất sáng lúc 10:00 — thường vắng hơn và ánh sáng cho hành trình trong ngày cũng đẹp hơn. Trường hợp bạn muốn xem cả Quỹ Kim cương, hãy nhớ đó là vé riêng và cũng theo suất giờ, nên cần phối hợp lịch của hai nơi cho khớp.",
"Hãy chuẩn bị tinh thần rằng bên trong cấm chụp ảnh và quay phim. Vì vậy, đừng phụ thuộc vào việc 'chụp để xem sau'; thay vào đó hãy thuê máy thuyết minh và tập trung quan sát. Cũng nên hạn chế mang túi lớn, và gửi áo khoác dày ở phòng gửi đồ để tham quan cho nhẹ nhàng.",
"Cuối cùng, hãy đặt Oruzheynaya Palata trong tổng thể một ngày ở Kremlin và Quảng trường Đỏ. Vé bảo tàng tách riêng với vé khuôn viên Kremlin, nên nếu muốn xem cả Quảng trường Nhà thờ, bạn cần mua thêm vé và sắp thứ tự hợp lý. Một lịch trình gợi ý: suất bảo tàng buổi sáng, sau đó thong dong thăm các nhà thờ, rồi ra Quảng trường Đỏ vào buổi chiều."
])

sec("Khám phá xung quanh", [
"Ngay trong khuôn viên Kremlin, điểm đến kề bên không thể bỏ qua là Quảng trường Nhà thờ. Tại đây quy tụ ba thánh đường cổ kính — Nhà thờ Uspensky (Đức Mẹ Lên Trời), Nhà thờ Arkhangelsky (Tổng lãnh thiên thần) và Nhà thờ Blagoveshchensky (Truyền Tin) — cùng Tháp chuông Ivan Đại đế. Đây chính là trái tim tôn giáo và nghi lễ của nước Nga suốt nhiều thế kỷ.",
"Cũng trong Kremlin, du khách sẽ gặp hai 'kỷ lục gia' nổi tiếng: Chuông Sa hoàng khổng lồ và Đại bác Sa hoàng — cả hai đều to đến mức chưa từng thực sự được sử dụng, nhưng lại là minh chứng cho tham vọng và tay nghề đúc kim loại của người Nga xưa. Đại Cung điện Kremlin uy nghi (nơi làm việc chính thức của nhà nước) cũng nằm ngay cạnh bảo tàng.",
"Bước ra khỏi Kremlin về phía Vườn Aleksandr, bạn sẽ thấy Mộ Chiến sĩ Vô danh với ngọn lửa vĩnh cửu và nghi thức đổi gác trang nghiêm. Khu vườn chạy dọc chân tường thành này là nơi lý tưởng để nghỉ chân, trước khi tản lên Quảng trường Manezhnaya rộng rãi ở phía trên.",
"Chỉ vài phút đi bộ là tới Quảng trường Đỏ trứ danh, với nhà thờ Thánh Basil nhiều màu, thương xá GUM lộng lẫy và Bảo tàng Lịch sử Quốc gia bằng gạch đỏ. Sự gần gũi này cho phép du khách nối liền hai trải nghiệm 'trong' và 'ngoài' Kremlin thành một hành trình mạch lạc trong cùng một ngày.",
"Về phía tây nam, khu vực quanh Tháp Borovitskaya dẫn tới Nhà Pashkov cổ điển tuyệt đẹp và bờ kè sông Moskva. Từ đây, bạn có thể thong thả tản bộ tới Nhà thờ Chúa Cứu Thế đồ sộ — cũng do chính kiến trúc sư Konstantin Ton thiết kế, tạo nên sự nối kết thú vị với toà bảo tàng bạn vừa thăm.",
"Nếu muốn đổi không khí sang hiện đại, công viên Zaryadye bên bờ sông (cách đó không xa) là lựa chọn hấp dẫn với cây cầu 'bay' nhìn ra Kremlin. Nhờ mạng lưới tàu điện ngầm dày đặc quanh khu vực, việc di chuyển tới các điểm xa hơn trong thành phố cũng hết sức thuận tiện."
])

sec("Câu chuyện & giai thoại thú vị", [
"Giai thoại được yêu thích nhất gắn với cỗ ngai đôi. Khi hai anh em Ivan V và Pyotr I cùng lên ngôi năm 1682 lúc còn nhỏ tuổi, người ta làm riêng cho hai vị một chiếc ngai có hai chỗ ngồi. Phía sau ngai được khoét một ô cửa kín đáo, tương truyền để người chị nhiếp chính Sofia đứng khuất mà thì thầm nhắc các em cách đối đáp trong những buổi thiết triều trang trọng.",
"Bản thân mũ Monomakh cũng là một 'kho' truyền thuyết. Dù các nhà nghiên cứu cho rằng nó do thợ Hãn quốc Kim Trướng chế tác, câu chuyện dân gian lại khăng khăng đó là quà của hoàng đế Byzantine gửi tặng công tước Vladimir Monomakh. Từ chiếc mũ này mà tiếng Nga có thành ngữ 'Nặng thay chiếc mũ Monomakh', được đại thi hào Pushkin đưa vào tác phẩm để nói về gánh nặng quyền lực.",
"Chiếc mũ trụ 'Jericho' lại vướng vào một sự nhầm lẫn ngoạn mục. Vốn do nghệ nhân Nikita Davydov làm cho Sa hoàng Romanov đầu tiên vào năm 1621, đến thế kỷ 19 nó bỗng bị gán cho là mũ của anh hùng Aleksandr Nevsky sống trước đó tận bốn thế kỷ. Sự nhầm lẫn 'sang trọng' này thậm chí đưa hình chiếc mũ lên quốc huy lớn của Đế chế Nga.",
"Những quả trứng Fabergé thì ẩn chứa cả một thế giới kỳ diệu. Mỗi quả đều giấu bên trong một 'bất ngờ' tinh xảo — từ mô hình cung điện, đoàn tàu tí hon cho tới cơ cấu đồng hồ, chim hót. Sau cách mạng, bộ sưu tập bị phân tán và bán bớt ra nước ngoài, khiến hành trình lưu lạc của từng quả trứng trở thành đề tài cho vô số cuốn sách và bộ phim tài liệu.",
"Bộ đồ sứ 'Olympic' mang một nghịch lý lịch sử thú vị. Đó là quà Napoleon tặng Hoàng đế Aleksandr I để đánh dấu Hoà ước Tilsit năm 1807 — biểu tượng của tình hữu nghị. Vậy mà chỉ ít năm sau, hai đế chế lao vào cuộc chiến khốc liệt năm 1812. Món quà xa hoa ấy vì thế trở thành chứng nhân câm lặng cho sự đổi thay chóng vánh của bang giao quyền lực.",
"Cuối cùng, những chiếc cúp và bình quý cũng kể chuyện về phong tục cung đình. Chiếc cúp hình con thuyền năm 1648, do một vị đại thần dâng lên Sa hoàng, gợi nhớ nghi thức tiệc tùng và đãi rượu nơi cung đình Nga. Cùng vô số quà tặng của các sứ đoàn, chúng biến Oruzheynaya Palata thành nơi mà mỗi hiện vật đều là một mẩu chuyện đang chờ được kể."
])

out = os.path.join(HERE, "doc_kremlin-armoury.json")
json.dump(d, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
wc = sum(len(p.split()) for s in d["sections"] for p in s["paras"])
print("WROTE", out)
print("sections:", len(d["sections"]), "| total words:", wc)
for s in d["sections"]:
    print(f"  {s['heading']}: {len(s['paras'])} paras, {sum(len(p.split()) for p in s['paras'])} words")
