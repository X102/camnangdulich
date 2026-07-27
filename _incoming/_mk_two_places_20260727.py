# -*- coding: utf-8 -*-
"""Sinh _incoming/doc_<slug>.json cho 2 địa điểm: Nhạc viện Moskva (Tchaikovsky) & Cung điện Sheremetev.
Nội dung tiếng Việt NGUYÊN GỐC do agent biên soạn, có dẫn nguồn. Chạy: python3 _mk_two_places_20260727.py
"""
import json, os, unicodedata, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))


def img(fn, cap):
    return {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(fn), "caption": cap}


def nfc(o):
    if isinstance(o, str):
        return unicodedata.normalize("NFC", o)
    if isinstance(o, list):
        return [nfc(x) for x in o]
    if isinstance(o, dict):
        return {k: nfc(v) for k, v in o.items()}
    return o


docs = []

# ======================================================================
# 1) NHẠC VIỆN MOSKVA MANG TÊN P.I. TCHAIKOVSKY
# ======================================================================
docs.append({
    "slug": "tchaikovsky-conservatory",
    "name_vi": "Nhạc viện Moskva mang tên P.I. Tchaikovsky (Nhạc viện Traicốpxki)",
    "name_ru": "Московская консерватория имени П. И. Чайковского",
    "name_en": "Moscow Tchaikovsky Conservatory",
    "subtitle": "Thánh đường của âm nhạc cổ điển Nga trên phố Bolshaya Nikitskaya — nơi Tchaikovsky từng đứng lớp, nơi Đại Sảnh được ví như 'cây vĩ cầm Stradivarius khổng lồ' ngân vang cùng cây đàn organ Cavaillé-Coll, và là sân khấu truyền thống của Cuộc thi Tchaikovsky Quốc tế.",
    "sections": [
        {"heading": "Giới thiệu chung", "paras": [
            '''Nhạc viện Quốc gia Moskva mang tên P.I. Tchaikovsky là trường đào tạo âm nhạc bậc cao danh giá nhất nước Nga và là một trong những nhạc viện lừng lẫy nhất thế giới. Toạ lạc ngay trung tâm thủ đô, trên phố Bolshaya Nikitskaya, chỉ vài phút đi bộ từ Điện Kremlin, nơi đây vừa là giảng đường đào tạo nhạc sĩ, vừa là trung tâm hoà nhạc sống động của Moskva suốt hơn một thế kỷ rưỡi. Với người yêu nhạc cổ điển, cái tên "Nhạc viện Moskva" gợi lên hình ảnh một ngôi đền thiêng của nghệ thuật âm thanh.''',
            '''Trường được thành lập năm 1866 theo sáng kiến của nghệ sĩ dương cầm, nhạc trưởng Nikolai Rubinstein, cùng công lao đồng sáng lập của công tước Nikolai Troubetzkoy. Ngay từ những ngày đầu, nhà soạn nhạc trẻ Pyotr Ilyich Tchaikovsky đã được mời giảng dạy lý thuyết âm nhạc và hoà âm. Đến năm 1940, nhân kỷ niệm 100 năm ngày sinh của ông, nhạc viện chính thức mang tên Tchaikovsky — một sự tôn vinh xứng đáng với người đã gắn bó máu thịt cùng ngôi trường.''',
            '''Trái tim của quần thể là Đại Sảnh (Bolshoy Zal), khánh thành năm 1901. Khán phòng cổ điển tao nhã này nổi tiếng khắp hoàn cầu nhờ âm học tuyệt hảo — đến mức giới nghệ sĩ gọi vui là "cây vĩ cầm Stradivarius khổng lồ" — cùng cây đàn organ do bậc thầy người Pháp Aristide Cavaillé-Coll chế tác. Chân dung các nhà soạn nhạc vĩ đại viền quanh tường, biến mỗi buổi diễn thành một cuộc gặp gỡ với lịch sử âm nhạc.''',
            '''Từ năm 1958, Đại Sảnh trở thành sân khấu truyền thống của Cuộc thi Tchaikovsky Quốc tế — một trong những cuộc thi âm nhạc uy tín bậc nhất hành tinh, tổ chức bốn năm một lần. Bao thế hệ nghệ sĩ dương cầm, vĩ cầm, cello và ca sĩ đã bước lên bục vinh quang tại đây, biến nơi này thành biểu tượng của khát vọng vươn tới đỉnh cao nghệ thuật.''',
            '''Ngay trước toà nhà là tượng đài Tchaikovsky, tạc nhà soạn nhạc đang ngồi như trong khoảnh khắc bắt nhịp, được bao quanh bởi một hàng rào sắt uốn hình những khuông nhạc trích từ chính tác phẩm của ông. Đây là một trong những tượng đài âm nhạc được yêu thích nhất Moskva và là điểm chụp ảnh quen thuộc của du khách.''',
            '''Với người Việt, ngôi trường còn mang một ý nghĩa gần gũi: nghệ sĩ dương cầm Đặng Thái Sơn — người châu Á đầu tiên đoạt giải Nhất Cuộc thi Chopin (1980) — từng tu nghiệp tại Nhạc viện Moskva. Rất nhiều nhạc sĩ Việt Nam thế hệ trước cũng trưởng thành từ những mái trường âm nhạc Xô-viết, khiến Nhạc viện Tchaikovsky trở thành một điểm đến đầy cảm xúc trong hành trình khám phá nước Nga.''',
        ]},
        {"heading": "Vị trí & cách di chuyển", "paras": [
            '''Nhạc viện nằm tại số 13 phố Bolshaya Nikitskaya, quận Presnensky, thuộc khu trung tâm lịch sử của Moskva. Vị trí này cực kỳ thuận tiện: chỉ cách Điện Kremlin, Vườn Alexander và Quảng trường Manezhnaya một quãng đi bộ ngắn, nằm trong "vành đai vàng" của các công trình văn hoá quan trọng nhất thủ đô.''',
            '''Cách tiếp cận dễ nhất là bằng tàu điện ngầm. Các ga gần nhất gồm Okhotny Ryad (tuyến đỏ số 1), Biblioteka imeni Lenina, Aleksandrovsky Sad và Arbatskaya — tất cả đều là cụm ga trung chuyển lớn, từ đó chỉ mất khoảng 7–10 phút đi bộ. Ga Arbatskaya của tuyến xanh dương cũng rất tiện nếu bạn đến từ phía phố Arbat.''',
            '''Bản thân phố Bolshaya Nikitskaya là một con phố cổ yên tĩnh, nhiều cây xanh, hai bên là dinh thự quý tộc, đại sứ quán và các cơ sở giáo dục lâu đời. Đi bộ dọc con phố này đã là một trải nghiệm thú vị, giúp du khách cảm nhận nhịp sống thanh lịch của Moskva cũ trước khi bước vào không gian âm nhạc của nhạc viện.''',
            '''Nếu xuất phát từ Quảng trường Đỏ, bạn chỉ cần đi bộ chừng 12–15 phút: qua Vườn Alexander, băng qua phố Mokhovaya rồi rẽ vào Bolshaya Nikitskaya. Tuyến đường bằng phẳng, dễ đi và nhiều điểm ngắm cảnh, rất phù hợp để kết hợp trong một buổi dạo bộ trung tâm thành phố.''',
            '''Taxi và các ứng dụng gọi xe như Yandex Go phủ sóng dày đặc ở khu vực này. Tuy nhiên, do nằm trong lõi trung tâm nên giao thông giờ cao điểm khá đông và chỗ đỗ xe hạn chế; vì thế nếu có thể, đi tàu điện ngầm rồi tản bộ vẫn là lựa chọn nhanh và dễ chịu nhất, nhất là vào buổi tối đi nghe hoà nhạc.''',
            '''Một lưu ý nhỏ để tránh nhầm lẫn: Nhạc viện Moskva (trên Bolshaya Nikitskaya) khác với Phòng hoà nhạc Tchaikovsky (Zal imeni Chaikovskogo) nằm ở Quảng trường Triumfalnaya, gần ga Mayakovskaya. Cả hai đều mang tên nhà soạn nhạc nhưng là hai địa điểm hoàn toàn riêng biệt; khi mua vé, hãy kiểm tra kỹ địa chỉ ghi trên vé.''',
        ]},
        {"heading": "Lịch sử hình thành và phát triển", "paras": [
            '''Mảnh đất nơi nhạc viện toạ lạc có một lịch sử quý tộc đáng nể. Năm 1766, khu đất được nữ công tước Ekaterina Dashkova — người bạn thân của Nữ hoàng Ekaterina II và là người phụ nữ đầu tiên đứng đầu Viện Hàn lâm Khoa học Nga — mua lại. Trên nền đất này, một toà nhà bằng đá được dựng lên vào cuối thế kỷ 18, theo tư liệu là do kiến trúc sư trứ danh Vasily Bazhenov thiết kế.''',
            '''Sau khi Dashkova qua đời năm 1810, toà nhà thuộc về người cháu là bá tước Mikhail Vorontsov, một anh hùng trong Chiến tranh Vệ quốc 1812. Công trình bị hư hại trong trận hoả hoạn Moskva năm 1812 rồi được phục dựng. Nhiều thập niên sau, ngôi nhà quý tộc này sẽ trở thành cái nôi của nền giáo dục âm nhạc chuyên nghiệp ở Moskva.''',
            '''Ý tưởng lập một nhạc viện tại Moskva chín muồi vào giữa thế kỷ 19. Sau khi Nhạc viện Saint Petersburg ra đời năm 1862, nhu cầu về một cơ sở tương tự ở Moskva càng cấp thiết. Năm 1866, Nikolai Rubinstein cùng công tước Troubetzkoy chính thức thành lập Nhạc viện Đế quốc Moskva dưới sự bảo trợ của Hội Âm nhạc Nga; lễ khai giảng long trọng diễn ra ngày 1 tháng 9. Rubinstein làm giám đốc đầu tiên, còn Tchaikovsky được bổ nhiệm làm giáo sư lý thuyết và hoà âm.''',
            '''Trường phát triển nhanh chóng: từ vài chục học trò ban đầu, số sinh viên tăng vọt qua từng năm. Năm 1871, Hội Âm nhạc Nga thuê rồi đến năm 1878 mua hẳn dinh thự cũ của dòng họ Vorontsov trên phố Nikitskaya với giá 185.000 rúp. Nhưng chẳng bao lâu, toà nhà lại trở nên chật chội và nhu cầu có một phòng hoà nhạc riêng ngày càng lớn.''',
            '''Năm 1893, ban lãnh đạo quyết định xây toà nhà mới ngay trên nền dinh thự cũ. Công trình do viện sĩ kiến trúc Vasily Zagorsky chủ trì, cùng trợ lý Alexander Nisselsohn. Lễ đặt móng diễn ra tháng 6 năm 1895; việc xây dựng kéo dài khoảng tám năm dưới sự giám sát sát sao của giám đốc Vasily Safonov. Toà học đường và Sảnh Nhỏ hoàn thành năm 1898, còn Đại Sảnh khánh thành ngày 7 (20) tháng 4 năm 1901.''',
            '''Thế kỷ 20 chứng kiến nhiều thăng trầm. Năm 1940, trường mang tên Tchaikovsky. Trong Thế chiến thứ hai, một quả bom Đức năm 1941 đã phá huỷ ô cửa kính màu tuyệt đẹp của Đại Sảnh. Có giai đoạn Xô-viết trường suýt bị đổi tên, và một thời gian dài Đại Sảnh còn được dùng làm rạp chiếu bóng ban ngày. Dù vậy, ngôi trường vẫn kiên cường giữ vững vị thế, để rồi từ năm 1958 gắn liền với Cuộc thi Tchaikovsky Quốc tế và trải qua đợt trùng tu lớn khôi phục Đại Sảnh vào năm 2010–2011.''',
            '''Danh sách các giám đốc và giáo sư của nhạc viện tự nó đã là một pho sử âm nhạc Nga. Sau Rubinstein, chiếc ghế lãnh đạo lần lượt qua tay nhà soạn nhạc Sergei Taneyev, rồi Vasily Safonov — người trực tiếp giám sát việc xây Đại Sảnh — và về sau là bậc thầy dương cầm Heinrich Neuhaus. Đặc biệt, lớp học nội trú của giáo sư Nikolai Zverev cuối thế kỷ 19 đã ươm mầm cho những tài năng kiệt xuất như Rachmaninoff và Scriabin, đặt nền cho trường phái dương cầm Nga lừng danh sau này.''',
            '''Bản thân Tchaikovsky gắn bó với ngôi trường suốt hơn một thập niên, vừa đứng lớp vừa viết những tác phẩm đầu tay và cả một cuốn giáo trình về hoà âm. Dù về sau rời bục giảng để toàn tâm sáng tác, ông vẫn là linh hồn của nhạc viện. Việc trường mang tên ông năm 1940 và dựng tượng đài năm 1954 chỉ là sự khẳng định chính thức cho mối lương duyên vốn đã hình thành ngay từ những ngày đầu tiên.''',
        ]},
        {"heading": "Kiến trúc & đặc điểm nổi bật", "paras": [
            '''Ngày nay, nhạc viện là một quần thể kiến trúc hài hoà gồm ba toà học đường và năm phòng hoà nhạc. Khi thiết kế toà nhà mới đầu thế kỷ 20, kiến trúc sư Zagorsky đã khéo léo giữ lại phần mặt tiền với khối bán nguyệt trung tâm của công trình Bazhenov cũ — chi tiết này về sau trở thành biểu tượng nhận diện của Đại Sảnh. Một mái hiên nhỏ với cổng thức tam giác và hàng cột bao quanh, vốn để xe ngựa dừng đón khách, tạo nên vẻ trang nghiêm cổ điển.''',
            '''Đại Sảnh là kiệt tác trung tâm. Khán phòng theo phong cách cổ điển, sơn tông màu sáng, ban đầu có 1.853 chỗ (nay khoảng 1.852 chỗ). Dọc hai bên tường, dưới những ô cửa sổ bán nguyệt lớn, là dãy chân dung hình huy chương của các nhà soạn nhạc vĩ đại — từ Tchaikovsky, Beethoven, Bach, Mozart đến Glinka, Borodin — do hoạ sĩ Nikolay Bodarevsky thực hiện theo chỉ dẫn của giám đốc Safonov.''',
            '''Điều làm nên danh tiếng toàn cầu của Đại Sảnh chính là âm học. Sự cân bằng, ấm áp và trong trẻo của âm thanh trong khán phòng được giới chuyên môn xếp vào hàng xuất sắc nhất thế giới, đến mức người ta ví nó như "một cây vĩ cầm Stradivarius khổng lồ". Mô hình thu nhỏ của khán phòng từng được chế tạo năm 2010 để kiểm soát và bảo toàn đặc tính âm học quý giá này trong quá trình trùng tu.''',
            '''Cây đàn organ ngự trên sân khấu là một báu vật khác. Được hãng danh tiếng Aristide Cavaillé-Coll của Pháp chế tác năm 1899 và từng được vinh danh là một trong những cây organ hay nhất thế giới tại Hội chợ Thế giới Paris năm 1900, nhạc cụ này là món quà của nhà tài trợ, ông trùm đường sắt Sergei von Derviz. Đến nay, tiếng organ vẫn vang lên trong nhiều buổi hoà nhạc.''',
            '''Trên đường lên khán phòng, du khách gặp một tấm kính màu lớn khắc hoạ Thánh Cecilia — bổn mạng của âm nhạc. Tác phẩm nguyên bản đã bị phá huỷ bởi sức ép quả bom năm 1941; suốt nhiều năm, vị trí đó được che bằng bức tranh hoành tráng "Các nhà soạn nhạc Slav" của danh hoạ Ilya Repin. Mãi đến đợt trùng tu 2010–2011, ô kính Thánh Cecilia mới được tái tạo theo nguyên mẫu, trả lại vẻ đẹp thuở ban đầu.''',
            '''Vô số chi tiết trang trí gắn với chủ đề âm nhạc: phù điêu huy chương chân dung người sáng lập Nikolai Rubinstein trên vòm sân khấu, hoạ tiết đàn lyre và kèn trumpet trên đèn chùm và lan can, cùng những đường nét hoa lá đặc trưng của phong cách moderne. Ở tiền sảnh còn có hai bức tượng nữ chiến binh Amazon phỏng theo điêu khắc Hy Lạp cổ đại, tạo cảm giác như bước vào một ngôi đền nghệ thuật.''',
            '''Bên cạnh Đại Sảnh, quần thể còn có Sảnh Nhỏ (Maly Zal) khánh thành năm 1898 — không gian lý tưởng cho nhạc thính phòng — cùng Sảnh Rachmaninov và các phòng khác. Ngoài trời, tượng đài Tchaikovsky do nữ điêu khắc gia Vera Mukhina thực hiện (khánh thành năm 1954) với hàng rào uốn hình khuông nhạc là điểm nhấn thị giác không thể bỏ qua ngay trước cổng.''',
            '''Quần thể nhạc viện không chỉ có các phòng hoà nhạc. Ba toà học đường liền kề chứa giảng đường, phòng tập và Thư viện Khoa học Âm nhạc mang tên Taneyev — một trong những thư viện âm nhạc lớn nhất nước Nga — cùng Bảo tàng Rubinstein lưu giữ hiện vật quý về lịch sử trường. Đây thực sự là một "khu phức hợp âm nhạc", nơi việc học, nghiên cứu và biểu diễn diễn ra song hành mỗi ngày.''',
            '''Sảnh Nhỏ (Maly Zal) tuy khiêm tốn về quy mô nhưng lại được yêu thích cho recital và nhạc thính phòng nhờ sự gần gũi giữa nghệ sĩ và khán giả. Sảnh Rachmaninov, nằm trong toà nhà thứ ba mà nhạc viện tiếp quản đầu thập niên 1920, bổ sung thêm một không gian ấm cúng nữa. Nhờ vậy, trong cùng một buổi tối có thể có vài chương trình diễn ra song song ở các khán phòng khác nhau của quần thể.''',
        ]},
        {"heading": "Những điểm nhấn không thể bỏ lỡ", "paras": [
            '''Trải nghiệm đỉnh cao và cũng là lý do tồn tại của nơi này chính là được ngồi nghe một buổi hoà nhạc trong Đại Sảnh. Dù là một bản giao hưởng của dàn nhạc lớn hay một đêm độc tấu dương cầm, âm học huyền thoại của khán phòng sẽ khiến bạn cảm nhận âm nhạc theo cách khó nơi nào sánh được.''',
            '''Hãy dành thời gian ngắm cây đàn organ Cavaillé-Coll trên sân khấu — một tác phẩm nghệ thuật cơ khí hơn trăm tuổi. Nếu may mắn dự một buổi hoà nhạc có organ, âm thanh trầm hùng lấp đầy không gian sẽ là kỷ niệm khó quên.''',
            '''Bức tranh "Các nhà soạn nhạc Slav" của Repin trong khu sảnh nghỉ là một điểm dừng thú vị. Tác phẩm quy tụ chân dung các nhạc sĩ Nga, Ba Lan và Séc trong một khung cảnh tưởng tượng — một ẩn dụ về sự thống nhất của âm nhạc Slav. Kết hợp cùng dãy huy chương chân dung quanh khán phòng, đây là một "phòng tranh âm nhạc" thu nhỏ.''',
            '''Ô kính màu Thánh Cecilia được tái tạo là biểu tượng cho sức sống bền bỉ của ngôi trường qua chiến tranh và thời gian. Ánh sáng xuyên qua tấm kính khi bạn bước lên cầu thang chính tạo nên một khoảnh khắc thị giác đầy chất thơ.''',
            '''Bên ngoài, tượng đài Tchaikovsky và hàng rào khuông nhạc là điểm "check-in" gần như bắt buộc. Hãy thử nhìn kỹ những nốt nhạc trên hàng rào — chúng được trích từ chính các tác phẩm của ông, một chi tiết tinh tế mà không phải du khách nào cũng để ý.''',
            '''Nếu ngân sách eo hẹp, đừng bỏ qua các buổi hoà nhạc ở Sảnh Nhỏ và Sảnh Rachmaninov, nơi thường diễn ra nhạc thính phòng và recital của sinh viên với giá vé dễ chịu hơn nhiều. Chất lượng nghệ thuật vẫn rất cao, còn không gian lại ấm cúng, gần gũi.''',
            '''Với những ai đến Moskva đúng vào năm tổ chức Cuộc thi Tchaikovsky Quốc tế, việc mua vé xem một vòng thi hoặc đêm gala trao giải là cơ hội hiếm có để chứng kiến những tài năng âm nhạc trẻ của thế giới toả sáng trên sân khấu lịch sử này.''',
            '''Một chi tiết thú vị để tinh ý nhận ra: dãy huy chương chân dung nhạc sĩ quanh khán phòng từng bị thay đổi dưới thời Xô-viết, khi một vài gương mặt được thay bằng các nhà soạn nhạc Nga và Slav khác. Thử đối chiếu thứ tự các chân dung sẽ hé lộ cả một câu chuyện về cách mỗi thời đại "viết lại" không gian theo hệ giá trị của mình.''',
        ]},
        {"heading": "Ý nghĩa lịch sử – văn hoá", "paras": [
            '''Nhạc viện Moskva là chiếc nôi của nền giáo dục âm nhạc chuyên nghiệp Nga. Trong hơn 150 năm, nơi đây đã định hình các trường phái biểu diễn dương cầm, vĩ cầm và sáng tác, đặt nền móng cho vị thế cường quốc âm nhạc cổ điển của nước Nga và Liên Xô trên bản đồ thế giới.''',
            '''Danh sách những người từng học và dạy tại đây đọc lên như một "bảng vàng" của âm nhạc: Sergei Rachmaninoff, Alexander Scriabin, Sergei Taneyev, Emil Gilels, Sviatoslav Richter, David Oistrakh, Leonid Kogan, Mstislav Rostropovich, Aram Khachaturian, Sofia Gubaidulina, Alfred Schnittke, Gidon Kremer, Yuri Bashmet... Mỗi cái tên là một chương trong lịch sử biểu diễn thế kỷ 20.''',
            '''Cuộc thi Tchaikovsky Quốc tế, gắn bó với nhạc viện từ năm 1958, đã trở thành một sự kiện văn hoá mang tầm vóc ngoại giao. Chiến thắng vang dội của nghệ sĩ Mỹ Van Cliburn ngay tại kỳ thi đầu tiên — giữa cao trào Chiến tranh Lạnh — được xem như một khoảnh khắc "tan băng" hiếm hoi, cho thấy sức mạnh kết nối con người của âm nhạc vượt lên trên rào cản chính trị.''',
            '''Trong đời sống thủ đô, Đại Sảnh từ lâu là trung tâm của sinh hoạt hoà nhạc Moskva. Bao thế hệ khán giả đã tới đây để nghe những buổi công diễn quan trọng, khiến nơi này trở thành một phần bản sắc văn hoá và niềm tự hào của người dân thành phố.''',
            '''Với Việt Nam, mối liên hệ càng thêm gần gũi. Nghệ sĩ Đặng Thái Sơn từng tu nghiệp tại Nhạc viện Moskva, và nhiều nhạc sĩ, nghệ sĩ Việt Nam thế hệ trước đã trưởng thành trong hệ thống đào tạo âm nhạc Xô-viết. Bước vào ngôi trường này, du khách Việt có thể cảm nhận một sợi dây văn hoá thân thuộc.''',
            '''Toà nhà nhạc viện được công nhận là di sản kiến trúc — văn hoá được nhà nước bảo vệ. Không chỉ là một công trình, nó là biểu tượng sống động cho truyền thống âm nhạc hàn lâm Nga, nơi quá khứ huy hoàng vẫn tiếp tục được nuôi dưỡng qua từng thế hệ sinh viên mới.''',
            '''Điều làm nên tầm vóc của nhạc viện không chỉ là danh sách những cái tên, mà là các "trường phái" biểu diễn được truyền từ thầy sang trò qua nhiều đời. Trường phái dương cầm Nga với lối chơi giàu chất hát và kỹ thuật điêu luyện, hay trường phái vĩ cầm gắn với những tên tuổi như David Oistrakh và Leonid Kogan, đã lan toả ảnh hưởng sâu rộng tới cách chơi nhạc cổ điển trên khắp thế giới, khiến "phong cách Moskva" trở thành một chuẩn mực được kính trọng.''',
        ]},
        {"heading": "Trải nghiệm dành cho du khách", "paras": [
            '''Cần lưu ý rằng đây trước hết là một cơ sở giáo dục đang hoạt động, không phải bảo tàng mở cửa tự do. Vì vậy, cách "tham quan" đúng nghĩa và trọn vẹn nhất là mua vé một buổi hoà nhạc — khi ấy bạn vừa được thưởng thức nghệ thuật, vừa được bước vào không gian nội thất lộng lẫy của Đại Sảnh.''',
            '''Mùa hoà nhạc trải dài gần như quanh năm với vô số lựa chọn: giao hưởng, hoà tấu thính phòng, độc tấu dương cầm, đêm nhạc thanh nhạc hay organ. Bầu không khí trang trọng, khán giả am hiểu và yên lặng tuyệt đối, tạo nên trải nghiệm rất khác so với các phòng hoà nhạc thông thường.''',
            '''Vé nên được đặt trước qua trang chính thức mosconsv.ru, đặc biệt với các chương trình có nghệ sĩ nổi tiếng hay trong kỳ Cuộc thi Tchaikovsky. Giá vé đa dạng, từ những hạng ghế bình dân cho tới khu vực trung tâm đắt hơn; đặt sớm giúp bạn có chỗ ngồi ưng ý.''',
            '''Trước giờ diễn, hãy đến sớm để thong thả ngắm nội thất: cầu thang chính, ô kính Thánh Cecilia, bức "Các nhà soạn nhạc Slav" và dãy chân dung nhạc sĩ. Người Nga có thói quen ăn mặc lịch sự khi đi nghe hoà nhạc, nên một bộ trang phục chỉnh tề sẽ giúp bạn hoà nhập.''',
            '''Đừng quên chụp ảnh cùng tượng đài Tchaikovsky và hàng rào khuông nhạc ở sân trước — nơi luôn có du khách dừng chân. Con phố Bolshaya Nikitskaya về đêm, khi ánh đèn hắt lên mặt tiền nhạc viện, cũng mang một vẻ đẹp rất riêng.''',
            '''Ngoài các buổi diễn lớn, nhạc viện còn tổ chức nhiều recital của sinh viên và Bảo tàng Rubinstein trong khuôn viên. Đây là những lựa chọn tiết kiệm mà vẫn đậm chất nghệ thuật, phù hợp cho du khách muốn cảm nhận nhịp sống thực của một ngôi trường âm nhạc hàng đầu.''',
        ]},
        {"heading": "Mẹo tham quan", "paras": [
            '''Hãy đặt vé càng sớm càng tốt, nhất là vào các năm tổ chức Cuộc thi Tchaikovsky Quốc tế (bốn năm một lần) khi nhu cầu tăng vọt. Trang mosconsv.ru là kênh chính thức đáng tin cậy; nên tránh mua lại vé giá cao từ "chợ đen" bên ngoài.''',
            '''Thời điểm lý tưởng là mùa hoà nhạc thu – xuân, khi lịch diễn dày đặc và phong phú nhất. Nếu chuyến đi rơi đúng dịp cuộc thi (thường vào tháng 6), bạn có thể sắp xếp để dự một vòng thi hoặc đêm gala đáng nhớ.''',
            '''Ăn mặc lịch sự và đến trước giờ diễn khoảng 30 phút. Theo tập quán ở Nga, khán giả thường gửi áo khoác tại quầy giữ đồ (garderob) trước khi vào khán phòng — một nét văn hoá nhỏ nhưng nên tuân theo để lịch sự và thoải mái.''',
            '''Trong lúc biểu diễn, tuyệt đối giữ im lặng, tắt chuông điện thoại và không chụp ảnh có đèn flash. Hãy quan sát khán giả xung quanh để biết thời điểm vỗ tay phù hợp — với các tác phẩm nhiều chương, thường chỉ vỗ tay sau khi kết thúc toàn bộ tác phẩm.''',
            '''Kết hợp chuyến đi với các điểm lân cận trong cùng một buổi: vì nhạc viện rất gần Điện Kremlin và Quảng trường Đỏ, bạn có thể tham quan ban ngày rồi nghe hoà nhạc vào buổi tối, tối ưu hoá thời gian ở khu trung tâm.''',
            '''Về ngân sách, các buổi diễn ở Sảnh Nhỏ hay recital sinh viên có giá vé "mềm" hơn nhiều so với các đêm lớn ở Đại Sảnh. Di chuyển bằng tàu điện ngầm và đi bộ sẽ vừa nhanh vừa tiết kiệm, đồng thời cho bạn cơ hội thưởng lãm con phố cổ trên đường tới.''',
            '''Nếu không mua được vé hoà nhạc, bạn vẫn có thể ghé Bảo tàng Rubinstein trong khuôn viên hoặc đơn giản là tản bộ quanh toà nhà để chụp ảnh mặt tiền bán nguyệt và tượng đài Tchaikovsky. Với người học nhạc, chỉ cần đứng nhìn dòng sinh viên ra vào tập luyện cũng đã là một trải nghiệm truyền cảm hứng, cho thấy nhịp sống thật của một nhạc viện hàng đầu thế giới.''',
        ]},
        {"heading": "Khám phá xung quanh", "paras": [
            '''Ngay trên phố Bolshaya Nikitskaya, cách nhạc viện không xa là Nhà thờ Chúa Thăng Thiên Lớn — nơi thi hào Aleksandr Pushkin làm lễ cưới với người đẹp Natalia Goncharova năm 1831. Con phố còn có nhiều dinh thự cổ, Nhà hát Maly và Nhạc viện, tạo thành một "trục văn hoá" giàu câu chuyện.''',
            '''Chỉ vài phút đi bộ về phía đông nam là Điện Kremlin, Vườn Alexander, Trung tâm triển lãm Manezh và phố Mokhovaya — cụm điểm đến biểu tượng nhất của Moskva. Du khách dễ dàng ghép nhạc viện vào lịch trình tham quan trung tâm mà không tốn nhiều công di chuyển.''',
            '''Về phía Quảng trường Nhà hát là Nhà hát Bolshoi lừng danh, cùng khu ga Teatralnaya, trung tâm thương mại TsUM và phố Kuznetsky Most sầm uất. Đây là lựa chọn tuyệt vời cho những ai muốn nối tiếp một hành trình "Moskva của âm nhạc và sân khấu".''',
            '''Nếu thích không khí tản bộ, hãy hướng ra Đại lộ Nikitsky và khu phố Arbat cổ (Stary Arbat) — nơi có tượng đài, quán cà phê, nghệ sĩ đường phố và vô số cửa hàng lưu niệm. Khu vực này rất phù hợp để thư giãn trước hoặc sau buổi hoà nhạc.''',
            '''Xung quanh nhạc viện có nhiều quán cà phê và nhà hàng ấm cúng phục vụ cả ẩm thực Nga lẫn châu Âu, tiện cho một bữa tối nhẹ trước giờ diễn. Vào buổi tối, khu Bolshaya Nikitskaya mang không khí thanh lịch, an toàn và dễ chịu để đi dạo.''',
            '''Với người mê nhạc cổ điển, có thể thiết kế một "tour âm nhạc Moskva" trọn vẹn: ban ngày thăm Bảo tàng nhạc cụ hoặc nhà lưu niệm nhạc sĩ, chiều dạo phố cổ, tối nghe hoà nhạc ở Nhạc viện Tchaikovsky, và dành một buổi khác cho Nhà hát Bolshoi hoặc Phòng hoà nhạc Tchaikovsky.''',
            '''Một gợi ý nữa cho người mê nhạc: quanh khu vực trung tâm còn có nhiều nhà – bảo tàng của các nhân vật văn hoá Nga, cùng các hiệu sách và cửa hàng bán đĩa, nhạc cụ. Kết hợp tất cả, bạn hoàn toàn có thể dành trọn một ngày cho chủ đề "Moskva và âm nhạc", khép lại bằng đêm hoà nhạc tại Đại Sảnh — một cái kết khó quên cho hành trình khám phá thủ đô nước Nga.''',
        ]},
        {"heading": "Câu chuyện & giai thoại thú vị", "paras": [
            '''Biệt danh "cây vĩ cầm Stradivarius khổng lồ" mà giới nghệ sĩ dành cho Đại Sảnh không phải lời khen suông. Chất lượng âm học ở đây tinh tế đến mức trong đợt trùng tu 2010–2011, người ta phải chế tạo hẳn một mô hình thu nhỏ của khán phòng để bảo đảm không làm sai lệch đặc tính âm thanh quý giá vốn có.''',
            '''Câu chuyện nổi tiếng nhất gắn với nơi này là chiến thắng của Van Cliburn năm 1958. Chàng nghệ sĩ dương cầm 23 tuổi người Mỹ đã chinh phục khán giả Moskva bằng Concerto số 1 của Tchaikovsky và Concerto số 3 của Rachmaninoff, nhận tràng vỗ tay kéo dài nhiều phút. Giữa căng thẳng Chiến tranh Lạnh, ban giám khảo được cho là đã xin ý kiến lãnh đạo Khrushchev trước khi trao giải Nhất cho một người Mỹ — và ông đã đồng ý.''',
            '''Trở về nước, Van Cliburn được chào đón như một người hùng, thậm chí có cả lễ diễu hành rải giấy hoa (ticker-tape parade) ở New York — điều hiếm thấy với một nhạc công cổ điển. Câu chuyện ấy cho thấy sân khấu Đại Sảnh không chỉ là nơi tôn vinh tài năng, mà còn từng là điểm giao thoa của lịch sử thế giới.''',
            '''Tượng đài Tchaikovsky phía trước cũng có giai thoại riêng. Nữ điêu khắc gia Vera Mukhina — tác giả của tượng đài "Công nhân và Nữ nông trang viên" trứ danh — được giao thực hiện từ giữa thập nien 1940. Phương án đầu tiên tạc nhà soạn nhạc đứng chỉ huy bị cho là quá lớn so với khoảng sân, nên bà chuyển sang tư thế ngồi bắt nhịp đầy cảm hứng. Đáng tiếc, Mukhina qua đời năm 1953, trước khi tượng đài được khánh thành năm 1954.''',
            '''Số phận ô kính màu Thánh Cecilia là một câu chuyện đầy xúc động về chiến tranh và hồi sinh. Bị phá huỷ bởi sức ép quả bom Đức năm 1941, suốt bảy thập kỷ vị trí ấy được thay bằng tranh của Repin, cho tới khi tấm kính được tái tạo nguyên bản trong đợt trùng tu đầu thế kỷ 21 — như một cách hàn gắn vết thương lịch sử.''',
            '''Ít ai biết rằng hai nghệ sĩ khổng lồ Rachmaninoff và Scriabin từng là bạn học cùng khoá tại đây, tốt nghiệp đầu thập niên 1890; Rachmaninoff còn giành Huy chương Vàng Lớn danh giá. Và trong những năm 1920, Đại Sảnh lộng lẫy này thậm chí từng được trưng dụng làm rạp chiếu bóng "Kolossus" vào ban ngày — một chi tiết thú vị về những khúc quanh của lịch sử.''',
            '''Với du khách Việt, giai thoại gần gũi nhất có lẽ là hình bóng Đặng Thái Sơn và bao thế hệ nhạc sĩ Việt từng học tập trong hệ thống âm nhạc Nga – Xô-viết. Đứng dưới mái Nhạc viện Tchaikovsky, ta như chạm vào một mạch nguồn văn hoá đã âm thầm nuôi dưỡng nền âm nhạc hàn lâm Việt Nam suốt nhiều thập kỷ.''',
        ]},
    ],
    "highlights": [
        "Thành lập năm 1866 theo sáng kiến của Nikolai Rubinstein; Tchaikovsky dạy tại đây từ đầu, trường mang tên ông từ năm 1940.",
        "Đại Sảnh (Bolshoy Zal) khánh thành năm 1901, âm học vào loại hay nhất thế giới — được ví như 'cây vĩ cầm Stradivarius khổng lồ'.",
        "Cây đàn organ Cavaillé-Coll (1899), quà tặng của nhà tài trợ von Derviz, từng được vinh danh tại Hội chợ Thế giới Paris 1900.",
        "Sân khấu truyền thống của Cuộc thi Tchaikovsky Quốc tế từ năm 1958 — nơi Van Cliburn thắng giải năm đầu tiên giữa Chiến tranh Lạnh.",
        "Tượng đài Tchaikovsky của nữ điêu khắc gia Vera Mukhina (1954) với hàng rào uốn hình khuông nhạc trước cổng.",
        "Ô kính màu Thánh Cecilia và bức tranh 'Các nhà soạn nhạc Slav' của Repin — kho báu nghệ thuật trong Đại Sảnh.",
    ],
    "images": [
        img("Moscow 05-2017 img41 Conservatory.jpg", "Mặt tiền Nhạc viện Moskva nhìn từ phố Bolshaya Nikitskaya"),
        img("Moscow Conservatory - Great Hall stage.jpg", "Sân khấu Đại Sảnh (Bolshoy Zal) với cây đàn organ Cavaillé-Coll"),
        img("Moscow Conservatory 1901.jpg", "Toà nhà Nhạc viện Moskva năm 1901, thời điểm Đại Sảnh khánh thành"),
        img("Moscow Imperial Conservatory in 1894.jpg", "Nhạc viện Đế quốc Moskva năm 1894 (toà nhà cũ trước khi xây mới)"),
    ],
    "references": [
        {"title": "Moscow Conservatory — Wikipedia (tiếng Anh)", "url": "https://en.wikipedia.org/wiki/Moscow_Conservatory"},
        {"title": "The Grand Hall of the Moscow Conservatory — trang chính thức mosconsv.ru", "url": "https://www.mosconsv.ru/museum/english/bzk.html"},
        {"title": "The Architectural Ensemble of the Moscow Conservatory — mosconsv.ru", "url": "https://www.mosconsv.ru/museum/english/arch_ensemble.html"},
        {"title": "International Tchaikovsky Competition — Wikipedia", "url": "https://en.wikipedia.org/wiki/International_Tchaikovsky_Competition"},
        {"title": "Van Cliburn — Encyclopaedia Britannica", "url": "https://www.britannica.com/biography/Van-Cliburn"},
        {"title": "Pyotr Tchaikovsky Moscow State Conservatory and Monument — Rusmania", "url": "https://rusmania.com/central/moscow-federal-city/moscow/presnensky/within-the-golden-ring-around-the-beginning-of-ulitsa-bolshaya-nikitskaya/pyotr-tchaikovsky-moscow-state-conservatory-and-pyotr-tchaikovsky-monument"},
        {"title": "Trang chủ Nhạc viện Moskva mang tên P.I. Tchaikovsky", "url": "https://www.mosconsv.ru"},
    ],
    "sources": [
        "Wikipedia tiếng Anh, mục 'Moscow Conservatory' (truy cập tháng 7/2026) — lịch sử thành lập, toà nhà, danh sách giảng viên/cựu sinh viên, các mốc thời gian.",
        "Trang chính thức Nhạc viện Moskva (mosconsv.ru), phần Bảo tàng: 'The Grand Hall' và 'The Architectural Ensemble' — chi tiết về Đại Sảnh, organ Cavaillé-Coll, kính màu Thánh Cecilia, tranh Repin.",
        "Wikipedia, mục 'International Tchaikovsky Competition' — thông tin về cuộc thi từ năm 1958.",
        "Encyclopaedia Britannica và tư liệu báo chí (PBS, WFIMC) về Van Cliburn và kỳ thi Tchaikovsky 1958.",
        "Rusmania — hồ sơ Nhạc viện Tchaikovsky và tượng đài; tư liệu về tượng đài của Vera Mukhina.",
        "Dữ liệu địa điểm nội bộ dự án 'Cẩm nang Du lịch Nga' (địa chỉ, toạ độ, thông tin thực dụng).",
    ],
})

# ======================================================================
# 2) CUNG ĐIỆN SHEREMETEV (FOUNTAIN HOUSE / FONTANNY DOM)
# ======================================================================
docs.append({
    "slug": "sheremetev-palace",
    "name_vi": "Cung điện Sheremetev (Sê-rê-mê-chép) – Nhà Đài Phun Nước (Fontanny Dom)",
    "name_ru": "Шереметевский дворец (Фонтанный дом)",
    "name_en": "Sheremetev Palace (Fountain House) – Museum of Music",
    "subtitle": "Dinh thự Baroque màu vàng của gia tộc bá tước Sheremetev bên sông Fontanka — 'Nhà Đài Phun Nước' của nhà hát nông nô lừng danh và mối tình Praskovya Zhemchugova, nay là Bảo tàng Âm nhạc với hơn 3.000 nhạc cụ và nơi lưu dấu nữ thi sĩ Anna Akhmatova.",
    "sections": [
        {"heading": "Giới thiệu chung", "paras": [
            '''Ẩn mình sau hàng rào sắt uy nghi bên bờ sông Fontanka, cách đại lộ Nevsky chỉ vài bước chân, Cung điện Sheremetev là một trong những dinh thự quý tộc lâu đời và giàu chất thơ nhất Saint Petersburg. Người dân quen gọi nơi đây bằng cái tên trìu mến "Nhà Đài Phun Nước" (Fontanny Dom), theo tên dòng sông và những đài phun nước từng điểm tô cho khu vườn.''',
            '''Trong gần hai thế kỷ, đây là tổ ấm của dòng họ bá tước Sheremetev — một trong những gia tộc quyền quý và giàu có bậc nhất nước Nga, nổi tiếng vì niềm đam mê nghệ thuật, âm nhạc và kịch nghệ. Toà nhà Baroque màu vàng ấm áp này từng vang lên tiếng đàn của dàn nhạc và đoàn hát nông nô riêng của gia đình, thu hút giới tinh hoa thủ đô.''',
            '''Rất hợp lẽ, ngày nay cung điện trở thành Bảo tàng Âm nhạc, lưu giữ bộ sưu tập hơn ba nghìn nhạc cụ từ khắp thế giới — một trong năm bộ sưu tập lớn nhất toàn cầu và lớn nhất nước Nga. Dạo qua các gian phòng nghi lễ được phục chế, du khách vừa chiêm ngưỡng nội thất quý tộc, vừa lần theo dòng chảy của lịch sử âm nhạc Nga.''',
            '''Cung điện gắn liền với một trong những chuyện tình nổi tiếng nhất lịch sử Nga: mối tình giữa bá tước Nikolai Sheremetev và Praskovya Zhemchugova — nàng ca sĩ giọng nữ cao xuất thân nông nô. Câu chuyện vượt rào cản đẳng cấp ấy đã để lại dấu ấn sâu đậm và khiến "Nhà Đài Phun Nước" trở thành một địa danh của tình yêu và bi kịch.''',
            '''Một điểm đặc biệt khác: trong khuôn viên cung điện còn có bảo tàng – căn hộ tưởng niệm nữ thi sĩ vĩ đại Anna Akhmatova, người đã sống ở đây suốt nhiều năm tháng khắc nghiệt của thời Xô-viết. Chính tại nơi này, bà đã viết nên những vần thơ bất hủ, biến Fontanny Dom thành một biểu tượng trong thi ca Nga thế kỷ 20.''',
            '''Sự giao thoa hiếm có giữa kiến trúc quý tộc, âm nhạc và văn chương khiến Cung điện Sheremetev trở thành một điểm dừng chân đặc biệt: bình yên, ít đông đúc, nhưng đầy chiều sâu. Đây là lựa chọn lý tưởng cho những ai muốn tìm một góc Saint Petersburg trầm lắng và giàu cảm xúc, tách khỏi dòng người tấp nập ở các cung điện lớn.''',
            '''So với những cung điện hoàng gia lộng lẫy như Cung điện Mùa Đông hay Peterhof, Sheremetev mang một vẻ đẹp trầm và "người" hơn — vẻ đẹp của một mái ấm quý tộc gắn với những con người cụ thể, những đam mê và cả bi kịch rất đời. Có lẽ chính điều đó khiến nơi đây để lại dư âm lâu dài trong lòng du khách, hơn là sự choáng ngợp thoáng qua.''',
        ]},
        {"heading": "Vị trí & cách di chuyển", "paras": [
            '''Cung điện toạ lạc tại số 34 kè sông Fontanka (Naberezhnaya reki Fontanki), thuộc quận trung tâm Saint Petersburg. Vị trí này rất đắc địa: chỉ cách đại lộ Nevsky — trục đường chính của thành phố — một quãng ngắn, nằm giữa lòng khu phố lịch sử với nhiều cung điện và bảo tàng.''',
            '''Cách đến thuận tiện nhất là bằng tàu điện ngầm. Hai ga gần nhất là Gostiny Dvor và Nevsky Prospekt (nằm sát nhau, ngay trên đại lộ Nevsky), từ đó chỉ mất khoảng 10 phút đi bộ dọc theo Nevsky rồi rẽ vào kè Fontanka. Ga Mayakovskaya cũng là một lựa chọn nếu bạn kết hợp thăm bảo tàng Akhmatova.''',
            '''Bảo tàng Âm nhạc trong toà chính của cung điện có lối vào từ phía kè Fontanka. Trong khi đó, Bảo tàng Akhmatova nằm ở phần cánh phụ, thường được tiếp cận qua khu vườn hoặc từ phía đại lộ Liteyny số 53. Nếu muốn thăm cả hai, hãy để ý kỹ hai lối vào riêng biệt này.''',
            '''Đi bộ là cách lý tưởng để đến cung điện, bởi đoạn kè Fontanka quanh đây rất đẹp, với những cây cầu duyên dáng và mặt tiền các dinh thự cổ soi bóng xuống dòng sông. Chỉ riêng quãng tản bộ từ Nevsky tới cổng cung điện đã là một trải nghiệm thị giác đáng nhớ.''',
            '''Taxi và ứng dụng gọi xe Yandex Go hoạt động rộng khắp; tuy nhiên khu trung tâm thường đông đúc và hạn chế đỗ xe, nên phương án tàu điện ngầm cộng đi bộ vẫn tối ưu. Nhiều tuyến xe buýt và xe điện bánh hơi cũng chạy dọc Nevsky, thuận tiện cho du khách.''',
            '''Vì nằm ngay lõi trung tâm, cung điện rất dễ ghép vào lịch trình cùng nhiều điểm đến nổi tiếng khác. Bạn có thể thong thả tham quan vào buổi sáng, sau đó tiếp tục khám phá đại lộ Nevsky và khu vực quanh sông Fontanka trong cùng một ngày.''',
            '''Với những ai ngại đi bộ nhiều, các tuyến xe điện bánh hơi và xe buýt chạy dọc Nevsky sẽ đưa bạn tới rất gần cung điện. Tuy nhiên, phần thưởng cho việc tản bộ dọc kè Fontanka là những khung hình tuyệt đẹp của mặt nước, cầu cổ và các dinh thự soi bóng — điều mà ngồi trên xe khó lòng cảm nhận trọn vẹn.''',
        ]},
        {"heading": "Lịch sử hình thành và phát triển", "paras": [
            '''Lịch sử cung điện bắt đầu từ năm 1712, khi Sa hoàng Pyotr Đại đế ban khu đất bên sông Fontanka cho Thống chế Boris Sheremetev — một trong những tướng lĩnh lừng danh của mình — kèm lệnh xây một dinh thự theo kiểu châu Âu. Thuở ấy, tư dinh chính của dòng họ nằm ở mũi đảo Vasilievsky, nên khu đất bên Fontanka ban đầu chỉ được dùng như một điền trang ngoại ô.''',
            '''Năm 1719, quyền thừa kế thuộc về Pyotr Borisovich Sheremetev. Đến cuối thập niên 1730, khi kiến trúc sư Rastrelli đang dựng các cung điện tráng lệ cho Nữ hoàng Elizabeth ở lân cận, gia đình mời kiến trúc sư Dmitriev xây một toà nhà đá một tầng tại đây, mở đầu cho quá trình kiến tạo kéo dài nhiều thế hệ.''',
            '''Khoảng hai thập niên sau, công trình được cải tạo thành dinh thự hai tầng bởi kiến trúc sư Savva Chevakinsky cùng Fyodor Argunov — điều đặc biệt là Argunov xuất thân từ một gia đình nông nô của chính dòng họ Sheremetev. Toà nhà mang phong cách Baroque, sơn hai tông vàng và trắng để hài hoà với các cung điện quý phái xung quanh. Năm 1788, kiến trúc sư Ivan Starov tiếp tục tu sửa nội thất.''',
            '''Vào thời hoàng kim cuối thế kỷ 18 – đầu thế kỷ 19, "Nhà Đài Phun Nước" là một trong những trung tâm văn hoá lớn của Saint Petersburg. Điền trang rộng lớn của gia tộc trải dài tới tận đại lộ Ligovsky, có cả bệnh viện và nhà hát riêng; nơi đây tổ chức những buổi hoà nhạc và dạ tiệc văn chương với sự góp mặt của các văn nhân danh tiếng. Năm 1838, kiến trúc sư Geronimo Corsini dựng hàng rào sắt uốn lộng lẫy mang huy hiệu gia tộc, tồn tại đến ngày nay.''',
            '''Sau Cách mạng Tháng Mười 1917, cung điện bị quốc hữu hoá. Từ năm 1918 đến 1931, nơi đây là "Bảo tàng Đời sống Quý tộc" dựa trên bộ sưu tập nghệ thuật mà dòng họ Sheremetev tích luỹ suốt hai thế kỷ. Về sau, bộ sưu tập được chuyển đi và toà nhà bị cải tạo thành một viện nghiên cứu, khiến phần lớn nội thất lịch sử bị phá bỏ — một mất mát lớn cho di sản.''',
            '''Bước ngoặt đến vào năm 1990, khi cung điện được giao cho Bảo tàng Sân khấu và Âm nhạc, mở đầu công cuộc trùng tu bền bỉ khôi phục các gian phòng nghi lễ. Kể từ đó, "Nhà Đài Phun Nước" hồi sinh trong vai trò Bảo tàng Âm nhạc, còn cánh phụ của cung điện trở thành bảo tàng tưởng niệm Anna Akhmatova từ năm 1989, khép lại một vòng lịch sử đầy biến động.''',
            '''Vào thời hoàng kim, cung điện còn nổi tiếng với bộ sưu tập nghệ thuật đồ sộ mà nhiều thế hệ Sheremetev tích luỹ — tương truyền có cả tranh của các bậc thầy châu Âu như Raphael, Correggio, Veronese và Rembrandt, cùng vô số đồ nội thất, sách quý và tư liệu gia tộc. Chính kho báu ấy đã trở thành nền tảng cho "Bảo tàng Đời sống Quý tộc" hoạt động trong những năm 1918–1931, trước khi bộ sưu tập bị phân tán và chuyển đi nơi khác.''',
            '''Không chỉ là nơi ở, điền trang Sheremetev từng như một "thành phố thu nhỏ" của lòng hảo tâm. Gia tộc duy trì bệnh viện, nhà tế bần và nhiều hoạt động từ thiện; truyền thống bảo trợ ấy còn nối dài tới Moskva, nơi bá tước Nikolai cho xây một nhà tế bần lớn để tưởng nhớ người vợ Praskovya — công trình về sau trở thành một trong những cơ sở y tế danh tiếng của thủ đô, minh chứng cho tấm lòng của ông với người vợ bình dân.''',
        ]},
        {"heading": "Kiến trúc & đặc điểm nổi bật", "paras": [
            '''Cung điện là một điển hình đẹp của kiến trúc dinh thự đô thị Nga thế kỷ 18. Toà nhà hai tầng theo phong cách Baroque, mặt tiền sơn tông vàng và trắng đặc trưng của trung tâm Saint Petersburg, được lùi vào trong so với đường kè và ngăn cách với phố bằng một sân danh dự (cour d'honneur) phía trước.''',
            '''Mặt tiền hướng ra sông Fontanka là mặt chính, được trang trí bằng các đường gờ, phào chỉ vữa, cột giả (pilaster) và một khối cổng thức trung tâm mang huy hiệu dòng họ Sheremetev. Vẻ đối xứng cân đối cùng sắc vàng ấm tạo nên dáng vẻ vừa bề thế vừa duyên dáng, phản chiếu xuống mặt nước Fontanka.''',
            '''Điểm nhấn kiến trúc bên ngoài là hàng rào sắt uốn tinh xảo do Geronimo Corsini thực hiện năm 1838. Trên cổng là huy hiệu bá tước Sheremetev với hình đôi sư tử và phương châm bằng tiếng Latinh "Deus conservat omnia" (Chúa gìn giữ muôn vật) — dòng chữ về sau đi vào thơ Akhmatova.''',
            '''Công trình là kết tinh công sức của nhiều thế hệ kiến trúc sư tài danh — Dmitriev, Chevakinsky, Argunov, Starov, Corsini — mỗi người bồi đắp thêm một lớp thẩm mỹ. Sự tham gia của Fyodor Argunov, một kiến trúc sư xuất thân nông nô, là minh chứng sống động cho truyền thống bảo trợ nghệ thuật đặc biệt của gia tộc.''',
            '''Bên trong, dãy phòng nghi lễ (enfilade) ở tầng hai đã được phục chế công phu dựa trên tư liệu lưu trữ, ảnh cũ và các bản mô tả. Mỗi gian phòng vừa tái hiện không khí quý tộc xưa, vừa trở thành một không gian trưng bày độc lập, cho phép du khách cảm nhận nếp sống thượng lưu của một thời đã qua.''',
            '''Ở cánh phía nam của cung điện là căn hộ nơi Anna Akhmatova từng sống. Không gian này được giữ gìn như một bảo tàng văn học – tưởng niệm, với đồ đạc, thư từ và di vật gợi lại đời sống tinh thần của nữ thi sĩ, tạo thành một mảng màu trầm lắng bổ sung cho vẻ lộng lẫy của toà chính.''',
            '''Bao quanh cung điện là khu vườn Sheremetev yên tĩnh — một ốc đảo xanh hiếm hoi giữa trung tâm nhộn nhịp. Khu vườn với những lối đi rợp bóng cây là nơi du khách có thể nghỉ chân, và cũng gắn với hình ảnh những chú mèo cùng những bức tường in dấu thơ ca quanh bảo tàng Akhmatova.''',
            '''Trong số các gian nghi lễ, du khách thường ấn tượng với những phòng khách lớn từng dùng để tiếp khách và tổ chức hoà nhạc, nơi trần cao, đèn chùm và các mảng trang trí vữa tái hiện gu thẩm mỹ quý tộc. Mỗi phòng được phục dựng như một "lát cắt thời gian", giúp hình dung không khí những buổi dạ tiệc âm nhạc mà gia tộc Sheremetev từng nổi tiếng khắp kinh đô.''',
            '''Bộ sưu tập của Bảo tàng Âm nhạc trải rộng từ nhạc cụ dân gian Nga, nhạc cụ cổ điển phương Tây đến những hiện vật quý từng thuộc về các nhạc sĩ danh tiếng. Nhiều cây đàn ở đây không chỉ có giá trị âm nhạc mà còn là tác phẩm thủ công mỹ nghệ tinh xảo, phản ánh trình độ chế tác qua nhiều thế kỷ và nhiều nền văn hoá — biến mỗi tủ trưng bày thành một câu chuyện nhỏ về hành trình của âm thanh.''',
        ]},
        {"heading": "Những điểm nhấn không thể bỏ lỡ", "paras": [
            '''Điểm nhấn hàng đầu là dãy phòng nghi lễ được phục chế ở tầng hai của toà chính. Đây là nơi bạn có thể hình dung rõ nhất khung cảnh những buổi hoà nhạc và dạ tiệc xa hoa của gia tộc Sheremetev, giữa các bức tường trang trí cầu kỳ và ánh sáng dịu từ những ô cửa lớn.''',
            '''Bộ sưu tập hơn 3.000 nhạc cụ của Bảo tàng Âm nhạc là "linh hồn" của cung điện ngày nay. Từ các loại đàn dây, kèn, nhạc cụ dân gian đến những cây vĩ cầm quý và nhạc cụ từng gắn với các nhạc sĩ danh tiếng, đây là một trong những sưu tập lớn và giá trị nhất thế giới — điểm đến mơ ước cho người yêu âm nhạc.''',
            '''Đừng bỏ lỡ hàng rào sắt và cổng mang huy hiệu Sheremetev bên bờ Fontanka. Chi tiết đôi sư tử cùng phương châm "Deus conservat omnia" không chỉ đẹp về tạo hình mà còn ẩn chứa câu chuyện về niềm tin và số phận của gia tộc, đồng thời là bối cảnh chụp ảnh rất "chất".''',
            '''Bảo tàng – căn hộ Anna Akhmatova trong khuôn viên là điểm đến không thể thiếu với những ai yêu văn chương. Bước vào không gian nơi bà từng sống và sáng tác, du khách như chạm vào một chương bi tráng của lịch sử tinh thần nước Nga thế kỷ 20.''',
            '''Nếu có dịp, hãy tham dự một buổi hoà nhạc cổ điển hoặc nhạc thính phòng tổ chức ngay trong các gian phòng của cung điện. Nghe nhạc sống trong chính không gian từng thuộc về một gia tộc mê âm nhạc là trải nghiệm mang đậm tính lịch sử và cảm xúc.''',
            '''Cuối cùng, khu vườn Sheremetev tĩnh lặng là nơi lý tưởng để khép lại chuyến thăm. Ngồi nghỉ dưới tán cây, ngắm mặt tiền vàng của cung điện, bạn sẽ cảm nhận được nhịp điệu chậm rãi và chiều sâu văn hoá làm nên nét quyến rũ riêng của "Nhà Đài Phun Nước".''',
            '''Trong bộ sưu tập nhạc cụ, hãy dành thời gian cho khu vực trưng bày những cây vĩ cầm cổ và các nhạc cụ hiếm được đặt trang trọng trong tủ kính. Không ít hiện vật gắn với tên tuổi lớn của âm nhạc Nga và châu Âu; đọc kỹ chú thích bên cạnh, bạn sẽ khám phá được nhiều mối liên hệ bất ngờ giữa cây đàn trước mặt và các nhà soạn nhạc, nghệ sĩ mà mình từng nghe tên.''',
        ]},
        {"heading": "Ý nghĩa lịch sử – văn hoá", "paras": [
            '''Cung điện Sheremetev là một chứng nhân sống động cho đời sống quý tộc Nga từ thời Pyotr Đại đế đến trước Cách mạng. Được chính Sa hoàng ban tặng cho một thống chế, rồi truyền qua nhiều thế hệ, nó phản ánh sự thăng trầm của tầng lớp đại quý tộc và vai trò bảo trợ văn hoá của họ đối với nghệ thuật Nga.''',
            '''Nhà hát nông nô của gia tộc Sheremetev từng thuộc hàng xuất sắc nhất nước Nga thế kỷ 18. Hiện tượng này cho thấy một khía cạnh đặc thù của xã hội Nga xưa: bên cạnh chế độ nông nô hà khắc, vẫn tồn tại những đoàn nghệ thuật tinh hoa mà thành viên là chính những người nông nô tài năng — như gia đình Argunov với các kiến trúc sư và hoạ sĩ nổi tiếng.''',
            '''Mối tình giữa bá tước Nikolai Sheremetev và nàng ca sĩ nông nô Praskovya Zhemchugova đã trở thành một biểu tượng văn hoá, được nhắc đến như câu chuyện về tình yêu vượt lên định kiến đẳng cấp. Nó đặt ra những câu hỏi nhân văn sâu sắc về thân phận con người, tài năng và tự do trong xã hội phong kiến Nga.''',
            '''Sang thế kỷ 20, cung điện lại mang một tầng ý nghĩa mới nhờ gắn với Anna Akhmatova — một trong những nhà thơ lớn nhất của Nga. Những năm tháng bà sống tại đây, giữa áp lực và mất mát của thời đại, đã kết tinh thành các tác phẩm bất hủ, khiến "Nhà Đài Phun Nước" trở thành một địa chỉ thiêng liêng của thi ca.''',
            '''Với vai trò Bảo tàng Âm nhạc hiện nay, cung điện còn là nơi bảo tồn và tôn vinh di sản âm nhạc — hoàn toàn phù hợp với truyền thống yêu nhạc của dòng họ Sheremetev. Bộ sưu tập nhạc cụ đồ sộ biến nơi đây thành một trung tâm nghiên cứu và giáo dục âm nhạc có tầm vóc quốc tế.''',
            '''Sự hội tụ của ba dòng chảy — quý tộc, âm nhạc và văn chương — trong một công trình khiến Cung điện Sheremetev trở thành một "lát cắt" cô đọng của văn hoá Nga. Đến đây, du khách không chỉ ngắm một dinh thự đẹp mà còn đọc được nhiều lớp lịch sử chồng lên nhau trong cùng một không gian.''',
            '''Riêng với Anna Akhmatova, "Nhà Đài Phun Nước" là chứng nhân của cả vinh quang lẫn khổ đau. Bà sống ở đây qua hai giai đoạn — bên cạnh nhà Đông phương học Vladimir Shileyko rồi nhà phê bình nghệ thuật Nikolai Punin — và chính trong những căn phòng này, nhiều phần của các tác phẩm lớn như trường ca "Khúc tưởng niệm" (Requiem) đã hình thành giữa bầu không khí ngột ngạt của thời kỳ thanh trừng, khi thơ bà bị cấm đoán.''',
        ]},
        {"heading": "Trải nghiệm dành cho du khách", "paras": [
            '''Trải nghiệm cốt lõi là thong thả dạo qua các gian phòng nghi lễ đã phục chế của Bảo tàng Âm nhạc, kết hợp chiêm ngưỡng bộ sưu tập nhạc cụ. Không gian ở đây thường yên tĩnh, ít đông đúc hơn hẳn các cung điện lớn, cho phép bạn thưởng lãm một cách chậm rãi và thư thái.''',
            '''Nhiều du khách đặc biệt yêu thích bầu không khí trầm lắng, quý phái của cung điện. Đây là điểm đến "gãi đúng chỗ ngứa" cho những ai muốn tránh cảnh chen chúc mà vẫn được đắm mình trong nội thất Baroque tinh tế và câu chuyện lịch sử phong phú.''',
            '''Nếu quan tâm đến âm nhạc, hãy kiểm tra lịch hoà nhạc trước khi đến. Cung điện thường xuyên tổ chức các buổi biểu diễn cổ điển và thính phòng; được nghe nhạc sống trong chính không gian lịch sử này là một trải nghiệm khó quên và rất đáng để sắp xếp thời gian.''',
            '''Với người yêu văn chương, việc ghé thêm bảo tàng – căn hộ Anna Akhmatova (mua vé riêng) sẽ làm trọn vẹn chuyến thăm. Không gian giản dị nhưng đầy sức nặng tinh thần này mang đến một góc nhìn khác hẳn so với sự lộng lẫy của toà chính.''',
            '''Một số du khách phản ánh rằng phần thuyết minh tiếng Anh còn hạn chế và nhân viên đôi khi chưa thật niềm nở. Vì vậy, thuê máy thuyết minh tự động (audio guide) hoặc chuẩn bị trước thông tin sẽ giúp bạn hiểu sâu hơn và chủ động hơn trong chuyến tham quan.''',
            '''Sau khi thăm bên trong, đừng vội rời đi: khu vườn Sheremetev là nơi tuyệt vời để nghỉ ngơi, chụp ảnh mặt tiền cung điện và tận hưởng một khoảnh khắc bình yên hiếm có ngay giữa trung tâm Saint Petersburg sôi động.''',
            '''Nếu đi cùng gia đình hoặc bạn đồng hành ít quan tâm tới bảo tàng, khu vườn và đoạn kè Fontanka phía trước vẫn đủ hấp dẫn để mọi người thư giãn trong lúc chờ. Sự linh hoạt ấy khiến Cung điện Sheremetev trở thành điểm dừng dễ chịu, phù hợp với nhiều kiểu du khách khác nhau, từ người mê nhạc, yêu văn chương cho đến người chỉ muốn tìm một góc yên tĩnh.''',
        ]},
        {"heading": "Mẹo tham quan", "paras": [
            '''Về giờ mở cửa, Bảo tàng Âm nhạc thường đón khách hằng ngày từ 11:00 đến 19:00 (ngừng nhận khách lúc 18:00), nghỉ vào thứ Ba và ngày thứ Tư cuối cùng của tháng. Nên kiểm tra lại lịch trên trang chính thức trước khi đi, vì giờ giấc có thể thay đổi theo mùa hoặc sự kiện.''',
            '''Vé vào cửa ở mức phải chăng (khoảng vài trăm rúp), và bạn có thể thuê thêm máy thuyết minh tự động với chi phí nhỏ. Lưu ý rằng bảo tàng Akhmatova bán vé riêng, nên nếu muốn thăm cả hai, hãy dự trù thêm thời gian và chi phí.''',
            '''Thời điểm lý tưởng để tham quan là buổi sáng các ngày thường, khi bảo tàng vắng khách nhất. Nếu có thể, hãy ghép chuyến thăm với một buổi hoà nhạc buổi tối tại cung điện để có trải nghiệm trọn vẹn cả về thị giác lẫn thính giác.''',
            '''Cân nhắc mua vé chụp ảnh nếu bạn muốn ghi lại nội thất, vì một số khu vực có thể yêu cầu phụ phí cho việc quay phim, chụp hình. Hãy tuân thủ quy định của bảo tàng và tránh dùng đèn flash để bảo vệ hiện vật.''',
            '''Do khu vực khá gần đại lộ Nevsky, bạn nên đi tàu điện ngầm tới ga Gostiny Dvor hoặc Nevsky Prospekt rồi đi bộ, vừa nhanh vừa ngắm được cảnh đẹp ven sông Fontanka. Ăn mặc thoải mái nhưng lịch sự, và mang giày êm chân cho quãng tản bộ.''',
            '''Cuối cùng, hãy dành thời gian tìm hiểu trước về mối tình Sheremetev – Zhemchugova và về Anna Akhmatova. Biết trước những câu chuyện này sẽ khiến mỗi gian phòng, mỗi hiện vật trở nên sống động và giàu ý nghĩa hơn rất nhiều khi bạn đứng trước chúng.''',
            '''Cũng nên nhớ mang theo một ít tiền mặt (rúp) cho các khoản vé và phụ phí nhỏ, vì không phải quầy nào cũng nhận thẻ nước ngoài. Nếu định nghe hoà nhạc buổi tối, hãy hỏi kỹ giờ mở cửa của bảo tàng trong ngày hôm đó, bởi lịch tham quan và lịch biểu diễn đôi khi được sắp xếp lệch nhau.''',
        ]},
        {"heading": "Khám phá xung quanh", "paras": [
            '''Cung điện nằm ngay cạnh đại lộ Nevsky huyền thoại — trục phố sầm uất và đẹp nhất Saint Petersburg, nơi tập trung cửa hàng, quán cà phê, nhà thờ và các công trình kiến trúc tráng lệ. Chỉ cần bước ra khỏi cổng, bạn đã ở giữa nhịp sống sôi động của thành phố.''',
            '''Rất gần đó, nơi Nevsky bắc qua sông Fontanka, là Cầu Anichkov nổi tiếng với bốn cụm tượng "Người thuần ngựa" của điêu khắc gia Klodt. Kế bên là Cung điện Anichkov và Cung điện Beloselsky-Belozersky mang sắc đỏ đặc trưng — những điểm ngắm kiến trúc hấp dẫn trong tầm đi bộ.''',
            '''Đi dọc kè Fontanka, du khách sẽ gặp nhiều dinh thự cổ, cây cầu duyên dáng và các góc phố nên thơ. Đây là một trong những tuyến tản bộ đẹp nhất thành phố, đặc biệt vào những đêm trắng mùa hè khi ánh sáng kéo dài đến tận khuya.''',
            '''Về phía quảng trường Ostrovsky gần đó là Nhà hát Alexandrinsky bề thế, Thư viện Quốc gia Nga và phố Kiến trúc sư Rossi — con phố được xem là hoàn hảo về tỷ lệ kiến trúc. Cụm điểm đến này rất thuận tiện để ghép cùng chuyến thăm cung điện.''',
            '''Nếu còn thời gian, bạn có thể hướng tới các biểu tượng lớn hơn của thành phố như Nhà thờ Máu Đổ, Bảo tàng Nga hay Cung điện Mùa Đông (Bảo tàng Hermitage) — tất cả đều nằm trong bán kính không quá xa dọc theo hoặc quanh đại lộ Nevsky.''',
            '''Khu vực quanh cung điện cũng có nhiều quán cà phê và nhà hàng ấm cúng, lý tưởng để nghỉ chân sau khi tham quan. Sự kết hợp giữa không gian tĩnh lặng của "Nhà Đài Phun Nước" và sức sống của Nevsky tạo nên một ngày khám phá cân bằng và trọn vẹn.''',
            '''Với người thích chủ đề văn học, có thể nối chuyến thăm với các địa chỉ gắn bó cùng giới văn nghệ sĩ Nga trong khu vực — từ những căn hộ – bảo tàng của các nhà văn đến các quán cà phê văn chương lâu đời quanh Nevsky. Khi ấy, "Nhà Đài Phun Nước" trở thành một mắt xích ý nghĩa trong hành trình khám phá tâm hồn văn hoá của Saint Petersburg, thành phố của Pushkin, Dostoevsky và Akhmatova.''',
        ]},
        {"heading": "Câu chuyện & giai thoại thú vị", "paras": [
            '''Câu chuyện nổi tiếng nhất gắn với cung điện là mối tình giữa bá tước Nikolai Sheremetev và Praskovya Zhemchugova. Sinh năm 1768 trong một gia đình nông nô của chính dòng họ, Praskovya bộc lộ giọng hát thiên phú và được đào tạo cho đoàn opera của gia đình; nghệ danh "Zhemchugova" bắt nguồn từ chữ "zhemchug" nghĩa là "ngọc trai".''',
            '''Nàng ra mắt sân khấu từ khi còn rất trẻ và nhanh chóng trở thành ngôi sao sáng nhất của đoàn hát nông nô, nổi tiếng với vai Eliane trong vở opera của Grétry mà nàng thể hiện suốt mười hai năm. Chính trong quá trình dàn dựng và bảo trợ nhà hát, bá tước Nikolai đã đem lòng yêu người ca sĩ tài hoa này.''',
            '''Vì rào cản đẳng cấp nghiệt ngã, họ phải giữ kín quan hệ trong nhiều năm — một quý tộc công khai xem nông nô là vợ là điều cấm kỵ trong xã hội thượng lưu bấy giờ. Năm 1798, Nikolai giải phóng Praskovya cùng gia đình khỏi thân phận nông nô; đến năm 1801, hai người bí mật kết hôn ở Moskva, thậm chí còn dựng cả một gia phả giả để "hợp thức hoá" nguồn gốc quý tộc cho nàng.''',
            '''Bi kịch ập đến khi Praskovya vốn yếu phổi qua đời ngay tại "Nhà Đài Phun Nước" vào năm 1803, khi mới 34 tuổi, chỉ hai mươi ngày sau khi sinh con trai. Đau đớn trước mất mát, bá tước Nikolai đã cho xây một nhà tế bần lớn ở Moskva để tưởng nhớ người vợ xuất thân bình dân mà ông hết mực yêu thương — một nghĩa cử để lại tiếng thơm.''',
            '''Phương châm của gia tộc Sheremetev khắc trên huy hiệu — "Deus conservat omnia" (Chúa gìn giữ muôn vật) — về sau được nữ thi sĩ Anna Akhmatova mượn làm đề từ cho trường ca nổi tiếng của bà. Chi tiết nhỏ ấy cho thấy sợi dây tinh thần nối liền quá khứ quý tộc của cung điện với đời sống văn chương thế kỷ 20.''',
            '''Chính cái tên "Nhà Đài Phun Nước" cũng là một giai thoại: nó bắt nguồn từ sông Fontanka và những đài phun nước từng điểm tô khu vườn thuở trước. Akhmatova là một trong những người đưa cách gọi thân thương này vào thi ca, biến một địa danh thành hình tượng nghệ thuật.''',
            '''Một chi tiết ít người để ý là vai trò của các nghệ nhân nông nô trong việc kiến tạo cung điện — tiêu biểu là Fyodor Argunov, kiến trúc sư xuất thân từ gia đình nông nô Argunov vốn còn sản sinh nhiều hoạ sĩ tài danh. Câu chuyện của họ, cũng như của Praskovya, nhắc ta rằng đằng sau vẻ nguy nga của cung điện là tài năng và số phận của những con người bình dị.''',
            '''Sự giàu có của gia tộc Sheremetev từng là huyền thoại ở nước Nga — đến mức người ta có cả cách nói ví von về lối sống xa hoa "theo kiểu Sheremetev". Chính khối tài sản khổng lồ ấy đã cho phép họ nuôi cả một nhà hát, dàn nhạc và bộ sưu tập nghệ thuật tầm cỡ bảo tàng; để rồi qua bao biến thiên, di sản đó nay quay về phục vụ công chúng dưới mái "Nhà Đài Phun Nước" — một cái kết đẹp cho câu chuyện kéo dài ba thế kỷ.''',
        ]},
    ],
    "highlights": [
        "Dinh thự Baroque màu vàng của gia tộc bá tước Sheremetev bên sông Fontanka, khởi nguồn từ khu đất Pyotr Đại đế ban năm 1712.",
        "Bảo tàng Âm nhạc với bộ sưu tập hơn 3.000 nhạc cụ — một trong năm bộ sưu tập lớn nhất thế giới, lớn nhất nước Nga.",
        "Mối tình huyền thoại giữa bá tước Nikolai Sheremetev và nàng ca sĩ nông nô Praskovya Zhemchugova.",
        "Bảo tàng – căn hộ tưởng niệm nữ thi sĩ Anna Akhmatova trong khuôn viên (mở cửa từ năm 1989).",
        "Hàng rào sắt và huy hiệu gia tộc do Geronimo Corsini dựng năm 1838, khắc phương châm 'Deus conservat omnia'.",
        "Dãy phòng nghi lễ Baroque đã phục chế cùng khu vườn Sheremetev yên tĩnh giữa trung tâm thành phố.",
    ],
    "images": [
        img("Sheremetev Palace 01.JPG", "Mặt tiền Cung điện Sheremetev nhìn từ kè sông Fontanka"),
        img("6509.1. St. Petersburg. Sheremetev Palace.jpg", "Cung điện Sheremetev (Nhà Đài Phun Nước) bên sông Fontanka"),
        img("6536.1. St. Petersburg. Sheremetev Palace.jpg", "Chi tiết mặt tiền Baroque màu vàng của Cung điện Sheremetev"),
        img("Шереметевский Дворец.jpg", "Cung điện Sheremetev (Фонтанный дом), Saint Petersburg"),
    ],
    "references": [
        {"title": "Fountain House (Saint Petersburg) — Wikipedia (tiếng Anh)", "url": "https://en.wikipedia.org/wiki/Fountain_House_(Saint_Petersburg)"},
        {"title": "Sheremetev Palace (Museum of Music) — saint-petersburg.com", "url": "http://www.saint-petersburg.com/palaces/sheremetyev-palace/"},
        {"title": "Anna Akhmatova Museum at the Fountain House — saint-petersburg.com", "url": "http://www.saint-petersburg.com/museums/anna-akhmatova-museum-at-the-fountain-house/"},
        {"title": "Praskovia Kovalyova-Zhemchugova — timenote.info", "url": "https://timenote.info/en/Praskovia-Kovalyova-Zhemchugova"},
        {"title": "Фонтанный дом — Wikipedia (tiếng Nga)", "url": "https://ru.wikipedia.org/wiki/Фонтанный_дом"},
        {"title": "Шереметевский дворец — Музей музыки (trang chính thức)", "url": "https://theatremuseum.ru/filial/sheremetevskiy_dvorec_muzey_muzyki"},
        {"title": "История одного здания: Шереметевский дворец — Culture.ru", "url": "https://www.culture.ru/materials/257633/istoriya-odnogo-zdaniya-sheremetevskii-dvorec"},
    ],
    "sources": [
        "Wikipedia tiếng Anh, mục 'Fountain House (Saint Petersburg)' (truy cập tháng 7/2026) — lịch sử xây dựng, các kiến trúc sư, giai đoạn Xô-viết, mối liên hệ Akhmatova.",
        "saint-petersburg.com — hồ sơ Cung điện Sheremetev (Bảo tàng Âm nhạc) và Bảo tàng Anna Akhmatova: kiến trúc, hàng rào Corsini, nhà hát nông nô, thông tin thực dụng.",
        "Tư liệu tiểu sử Praskovya Zhemchugova (timenote.info, findagrave.com, en-academic.com) — cuộc đời, sự nghiệp opera và hôn nhân với bá tước Nikolai Sheremetev.",
        "Wikipedia tiếng Nga 'Фонтанный дом' và Culture.ru ('История одного здания') — bối cảnh và quá trình phục chế cung điện.",
        "Trang chính thức Bảo tàng Sân khấu và Âm nhạc (theatremuseum.ru) — thông tin về Bảo tàng Âm nhạc và bộ sưu tập nhạc cụ.",
        "Orlando Figes, 'Natasha's Dance: A Cultural History of Russia' — tham chiếu về gia tộc Sheremetev và văn hoá quý tộc Nga.",
        "Dữ liệu địa điểm nội bộ dự án 'Cẩm nang Du lịch Nga' (địa chỉ, toạ độ, giờ mở cửa, nhận xét du khách).",
    ],
})

# ---- ghi file ----
for d in docs:
    d = nfc(d)
    fp = os.path.join(HERE, "doc_%s.json" % d["slug"])
    with open(fp, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    wc = sum(len(p.split()) for s in d["sections"] for p in s["paras"])
    print("wrote %s | sections=%d | words=%d | images=%d | refs=%d | sources=%d" % (
        os.path.basename(fp), len(d["sections"]), wc, len(d["images"]), len(d["references"]), len(d["sources"])))
