# -*- coding: utf-8 -*-
"""Seed — Moskva (13 địa điểm). Nội dung tiếng Việt nguyên bản. Chạy: python3 tools/seed_moscow.py"""
import json, os, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "data", "regions", "moscow.json")

REGION_SLUG = "moscow"
REGION_NAME_VI = "Moskva"
FEDERAL_DISTRICT = "Thành phố trực thuộc liên bang"
TODAY = "2026-07-16"


def maps(lat, lon):
    return {"yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=17&l=map",
            "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"}


def photo_url(fn):
    return ("https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(fn)) if fn else None


def wiki(name_en):
    return {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Special:Search?search=" + urllib.parse.quote(name_en)}


def place(slug, name_vi, name_ru, name_en, categories, lat, lon, address_vi, rating, review,
          short, long, highlights, practical, photo_file=None, official=None, tags=None, status="enriched"):
    return {
        "id": f"{REGION_SLUG}-{slug}", "slug": slug, "region": REGION_SLUG,
        "region_name_vi": REGION_NAME_VI, "federal_district": FEDERAL_DISTRICT,
        "name_vi": name_vi, "name_ru": name_ru, "name_en": name_en, "categories": categories,
        "coordinates": {"lat": lat, "lon": lon}, "address_vi": address_vi, "rating": rating,
        "review_summary_vi": review, "presentation_short_vi": short, "presentation_long_vi": long,
        "highlights_vi": highlights, "practical": practical, "photo": photo_url(photo_file),
        "photo_credit": ("Wikimedia Commons" if photo_file else None), "maps": maps(lat, lon),
        "official_site": official, "sources": [wiki(name_en)], "tags": tags or [],
        "status": status, "last_updated": TODAY,
    }


PLACES = [
    place("red-square", "Quảng trường Đỏ (Krasnaya Ploshchad)", "Красная площадь", "Red Square",
        ["square_street", "monument"], 55.754170, 37.620000, "Quảng trường Đỏ (Krasnaya ploshchad), Moskva",
        {"value": 4.7, "count": 20619, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách gần như đồng lòng gọi Quảng trường Đỏ là trái tim phải-đến của Moskva, trầm trồ trước quần thể Nhà thờ Thánh Basil, tường Kremlin, GUM và Lăng Lenin; nhiều người thấy ngoài đời ấn tượng hơn ảnh, nhất là về đêm. Phàn nàn chính: rất đông và thường bị đóng một phần khi có sự kiện, hoà nhạc hoặc tổng duyệt.",
        "Trái tim biểu tượng của Moskva và cả nước Nga — quần thể choáng ngợp gồm Nhà thờ Thánh Basil, tường thành Kremlin, cửa hàng GUM và Lăng Lenin, đặc biệt huyền ảo khi lên đèn.",
        "Không nơi nào gói trọn tinh thần nước Nga như Quảng trường Đỏ. Trải rộng ngay dưới chân tường thành Kremlin, đây là sân khấu của lịch sử Nga suốt nhiều thế kỷ — từ các phiên chợ thời trung cổ, những cuộc duyệt binh, tới lễ diễu binh Ngày Chiến thắng 9/5 hằng năm. Một điều thú vị: cái tên 'Đỏ' (Krasnaya) trong tiếng Nga cổ vốn có nghĩa là 'đẹp', chẳng liên quan gì tới màu sắc hay chủ nghĩa cộng sản. Đứng giữa quảng trường lát đá, bạn được bao quanh bởi những công trình biểu tượng nhất: mái vòm củ hành sặc sỡ của Nhà thờ Thánh Basil ở một đầu, bức tường gạch đỏ và các tháp canh của Kremlin, mặt tiền lộng lẫy của cửa hàng bách hoá GUM, và Lăng Lenin trầm mặc. Cùng với Kremlin, quảng trường được UNESCO công nhận Di sản Thế giới năm 1990. Du khách thường nói rằng ngoài đời nơi này còn ấn tượng hơn cả trong ảnh, nhất là về đêm khi mọi công trình lên đèn vàng rực. Hãy đến vào cả ban ngày lẫn buổi tối; lưu ý quảng trường đôi khi đóng một phần khi có sự kiện, hoà nhạc hay tổng duyệt diễu binh.",
        ["Tên 'Đỏ' (Krasnaya) trong tiếng Nga cổ nghĩa là 'đẹp', không liên quan tới màu sắc hay chủ nghĩa cộng sản.",
         "Cùng Kremlin được UNESCO công nhận Di sản Thế giới năm 1990.",
         "Là nơi diễn ra lễ diễu binh Ngày Chiến thắng 9/5 hằng năm, ngăn cách Kremlin với khu phố cổ thương nhân Kitai-gorod."],
        {"hours_vi": "Mở cửa 24/7 (quảng trường công cộng); đôi khi đóng khi có sự kiện, hoà nhạc hoặc tổng duyệt.",
         "ticket_vi": "Miễn phí.", "duration_vi": "1–2 giờ.",
         "best_time_vi": "Buổi tối khi lên đèn; mùa hè hoặc mùa đông tuyết phủ đều đẹp.",
         "tips_vi": "Kết hợp thăm Nhà thờ Thánh Basil, Kremlin, GUM ngay cạnh; kiểm tra lịch sự kiện phòng khi đóng quảng trường."},
        photo_file="Red Square, winter, Moscow, Russia.jpg", official=None,
        tags=["square", "free", "outdoor", "landmark", "unesco", "top"]),

    place("kremlin", "Điện Kremlin Moskva", "Московский Кремль", "Moscow Kremlin",
        ["fortress", "museum"], 55.752121, 37.617664, "Điện Kremlin, Moskva",
        {"value": 4.6, "count": 7934, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách gọi Kremlin là hùng vĩ và ngập tràn lịch sử, ấn tượng nhất với các nhà thờ ở Quảng trường Nhà thờ, kho báu Armoury cùng Chuông Sa hoàng và Đại bác Sa hoàng; mùa đông đặc biệt đẹp. Phàn nàn thường gặp: thủ tục vé rườm rà, cấm chụp ảnh trong nhà thờ, an ninh nghiêm ngặt kiểu sân bay.",
        "Thành luỹ quyền lực suốt hơn 500 năm của nước Nga — nơi ở của Tổng thống, với Quảng trường Nhà thờ, kho báu Armoury, Chuông Sa hoàng và Đại bác Sa hoàng khổng lồ.",
        "Sau bức tường gạch đỏ dài hơn hai cây số với hai mươi tháp canh là trung tâm quyền lực của nước Nga suốt hơn năm thế kỷ — Điện Kremlin. Được các kiến trúc sư người Ý xây dựng lại trong các năm 1485–1495, đây vừa là nơi ở chính thức của Tổng thống Nga, vừa là một bảo tàng lộ thiên khổng lồ. Trung tâm quần thể là Quảng trường Nhà thờ, nơi tụ hội những thánh đường dát vàng từng chứng kiến lễ đăng quang của các Sa hoàng. Kho báu Armoury trưng bày vương miện, long bào, xe ngựa hoàng gia và bộ sưu tập trứng Fabergé lừng danh. Ngoài sân, bạn sẽ gặp hai kỷ lục: Chuông Sa hoàng — quả chuông lớn nhất từng được đúc, nặng khoảng 202 tấn (nhưng chưa từng ngân vang vì bị nứt), và Đại bác Sa hoàng đồ sộ. Du khách thường choáng ngợp trước bề dày lịch sử, đặc biệt đẹp vào mùa đông tuyết phủ. Lưu ý: thủ tục vé khá rườm rà (phải đổi voucher online lấy vé giấy, xếp hàng), cấm chụp ảnh bên trong các nhà thờ, và an ninh nghiêm ngặt như ở sân bay. Hãy dành nửa ngày và mua vé sớm.",
        ["Nơi ở chính thức của Tổng thống Nga và là trung tâm quyền lực suốt hơn 500 năm.",
         "Tường gạch đỏ (xây 1485–1495 bởi kiến trúc sư Ý) dài khoảng 2.235 m với 20 tháp canh.",
         "Sở hữu Chuông Sa hoàng (~202 tấn, chuông lớn nhất từng đúc), Đại bác Sa hoàng và kho Armoury với trứng Fabergé, vương miện hoàng gia."],
        {"hours_vi": "Thứ 6–Thứ 4: mùa đông (1/10–14/5) 10:00–17:00, mùa hè (15/5–30/9) 09:30–18:00; đóng cửa Thứ Năm.",
         "ticket_vi": "Quảng trường Nhà thờ ~1.100 RUB; kho Armoury ~1.400 RUB; dưới 7 tuổi miễn phí.",
         "duration_vi": "3–4 giờ.", "best_time_vi": "Mùa đông tuyết phủ hoặc mùa hè; đi sớm để tránh xếp hàng vé.",
         "tips_vi": "Mua/đổi vé sớm; mang giấy tờ tuỳ thân; không chụp ảnh trong nhà thờ; đặt vé Armoury theo khung giờ."},
        photo_file="Kremlin y río Moscova, Moscú, Rusia, 2016-10-03, DD 20-21 HDR.jpg", official="https://www.kreml.ru",
        tags=["fortress", "museum", "indoor", "unesco", "top"]),

    place("st-basils", "Nhà thờ Thánh Basil (Sobor Vasiliya Blazhennogo)", "Собор Василия Блаженного", "Saint Basil's Cathedral",
        ["church"], 55.752500, 37.623060, "Quảng trường Đỏ, Moskva",
        {"value": 4.7, "count": 12444, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách mê mẩn những mái vòm củ hành 'kẹo ngọt', thường gọi đây là nhà thờ đẹp nhất từng thấy và điểm nhấn của chuyến đi Moskva. Bên trong là mê cung nguyện đường nhỏ, bích hoạ cổ, đôi khi có hát a cappella — nhưng nhiều người lưu ý không gian tối, chật và cầu thang dốc hẹp; nên đặt vé trước.",
        "Biểu tượng cổ tích của nước Nga với những mái vòm củ hành nhiều màu xoáy tròn — do Sa hoàng Ivan Bạo chúa cho xây, nay là Di sản Thế giới UNESCO.",
        "Nếu chỉ có một hình ảnh đại diện cho nước Nga, rất có thể đó là những mái vòm củ hành nhiều màu xoáy tròn của Nhà thờ Thánh Basil. Được Sa hoàng Ivan Bạo chúa cho xây trong các năm 1555–1561 để mừng chiến thắng chiếm hãn quốc Kazan, công trình có một cái tên chính thức dài và trang trọng: Nhà thờ Cầu bầu của Đức Mẹ Chí Thánh bên Hào nước. Điều khiến nó độc nhất vô nhị là cấu trúc: chín nhà thờ nhỏ riêng biệt được đặt chung trên một nền, mỗi tháp một sắc màu, tạo nên vẻ ngoài như bước ra từ truyện cổ tích. Bên trong không hề giống một đại giáo đường rộng lớn, mà là một mê cung của những nguyện đường nhỏ hẹp, tường phủ bích hoạ cổ, đôi khi vang lên tiếng hát a cappella réo rắt. Từ năm 1928, nơi đây là bảo tàng thuộc Bảo tàng Lịch sử Quốc gia, và được UNESCO công nhận Di sản Thế giới. Du khách thường gọi đây là nhà thờ đẹp nhất họ từng thấy. Lời khuyên: bên trong khá tối, chật và phải leo cầu thang dốc hẹp; nên đặt vé trước để đỡ xếp hàng.",
        ["Do Sa hoàng Ivan Bạo chúa cho xây 1555–1561, mừng chiến thắng chiếm hãn quốc Kazan.",
         "Tên chính thức là Nhà thờ Cầu bầu của Đức Mẹ bên Hào nước; gồm 9 nhà thờ nhỏ trên cùng một nền.",
         "Là bảo tàng từ năm 1928 (thuộc Bảo tàng Lịch sử Quốc gia) và Di sản Thế giới UNESCO."],
        {"hours_vi": "Hằng ngày ~10:00–19:00 (mùa hè có ngày tới ~21:00); đóng cửa Thứ Tư đầu tiên mỗi tháng.",
         "ticket_vi": "Người lớn ~1.000 RUB; khách nước ngoài có thể tới ~2.000 RUB; dưới 7 tuổi miễn phí.",
         "duration_vi": "1–1,5 giờ.", "best_time_vi": "Sáng sớm để tránh đông; kết hợp Quảng trường Đỏ.",
         "tips_vi": "Đặt vé trước; bên trong tối và chật, cầu thang dốc; đi giày thấp."},
        photo_file="Saint Basil's Cathedral in Moscow.jpg", official="https://shm.ru",
        tags=["church", "landmark", "indoor", "unesco", "top"]),

    place("lenin-mausoleum", "Lăng Lenin (Mavzoley Lenina)", "Мавзолей Ленина", "Lenin's Mausoleum",
        ["monument"], 55.753610, 37.619720, "Quảng trường Đỏ (bên tường Kremlin), Moskva",
        {"value": 4.0, "count": 1371, "source": "Tripadvisor", "as_of": "2026-07"},
        "Nhiều du khách thấy việc đi ngang thi hài ướp của Lenin là trải nghiệm siêu thực, có một không hai với lịch sử, và thích việc vào cửa miễn phí. Phàn nàn thường gặp: xếp hàng an ninh lâu rồi bị đi lướt qua chỉ 2–3 phút, cấm dừng/nói/chụp ảnh, không khí trang nghiêm và lính gác nghiêm nghị.",
        "Nơi lưu giữ thi hài ướp của Vladimir Lenin từ năm 1924, ngay trên Quảng trường Đỏ — một trải nghiệm lịch sử kỳ lạ, vào cửa miễn phí.",
        "Nằm sát chân tường Kremlin trên Quảng trường Đỏ, khối lăng bằng đá granite đỏ-đen trầm mặc này lưu giữ một trong những thi hài nổi tiếng nhất thế giới: Vladimir Lenin, lãnh tụ Cách mạng Nga, được ướp và trưng bày từ năm 1924 tới nay, dưới sự chăm sóc của cả một phòng thí nghiệm khoa học chuyên trách. Công trình granite hiện tại (1930) do kiến trúc sư Aleksey Shchusev thiết kế, từng là khán đài nơi các lãnh đạo Xô Viết đứng duyệt binh trên Quảng trường Đỏ. Vào lăng hoàn toàn miễn phí, nhưng là một trải nghiệm khác thường: du khách phải qua kiểm tra an ninh, gửi lại túi xách và máy ảnh, rồi lặng lẽ đi thành hàng ngang qua quan tài kính trong khoảng hai đến ba phút — cấm dừng lại, trò chuyện hay chụp ảnh. Nhiều người mô tả đây là cuộc chạm trán siêu thực, có một không hai với lịch sử. Không khí trang nghiêm, lính gác nghiêm nghị. Hãy cân nhắc nếu đi cùng trẻ nhỏ, và đến sớm vì giờ mở cửa khá hạn chế.",
        ["Thi hài ướp của Lenin được trưng bày từ năm 1924, do một phòng thí nghiệm khoa học chuyên trách bảo quản.",
         "Lăng granite hiện tại (1930) do Aleksey Shchusev thiết kế, từng là khán đài duyệt binh của lãnh đạo Xô Viết.",
         "Vào cửa miễn phí nhưng phải qua an ninh, gửi túi/máy ảnh và đi ngang trong im lặng tuyệt đối."],
        {"hours_vi": "Thứ 3,4,5,7,CN 10:00–13:00; đóng cửa Thứ Hai và Thứ Sáu.",
         "ticket_vi": "Miễn phí.", "duration_vi": "30–60 phút (đi bên trong ~3 phút).",
         "best_time_vi": "Đến sớm trong khung giờ mở cửa để tránh hàng dài.",
         "tips_vi": "Gửi túi/máy ảnh trước; giữ im lặng; cân nhắc nếu đi cùng trẻ nhỏ."},
        photo_file="Moscow LeninMausoleum 1547.JPG", official=None,
        tags=["monument", "free", "indoor", "history"]),

    place("gum", "Cửa hàng bách hoá GUM", "ГУМ", "GUM Department Store",
        ["square_street"], 55.754722, 37.621389, "Krasnaya ploshchad 3, Moskva",
        {"value": 4.4, "count": 6011, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách yêu GUM như một kỳ quan kiến trúc — dãy hành lang thế kỷ 19, mái vòm kính và trang trí lễ hội (nhất là dịp Năm Mới) rực rỡ — và khuyên cả người không mua sắm cũng nên ghé; kem GUM là món được khen nhiều. Điểm chê: hàng hiệu bên trong đắt đỏ, hướng tới du khách và giới nhà giàu nên giống bảo tàng hơn nơi dân địa phương mua sắm.",
        "Thương xá lịch sử tráng lệ bên Quảng trường Đỏ, mở từ 1893, với mái vòm kính, dãy hành lang cổ và trang trí lễ hội rực rỡ — nổi tiếng với kem GUM huyền thoại.",
        "Trải dài khoảng 242 mét dọc cạnh phía đông Quảng trường Đỏ, đối diện Kremlin, GUM là một trong những thương xá đẹp nhất thế giới. Mở cửa năm 1893 với tên gọi 'Dãy Thương mại Thượng hạng', công trình gây kinh ngạc bởi mái vòm kính-thép tiên phong do kỹ sư tài ba Vladimir Shukhov thiết kế. Dưới ánh sáng tự nhiên tràn qua mái vòm, ba tầng hành lang cong với những cây cầu nhỏ bắc ngang tạo nên một không gian vừa cổ kính vừa lộng lẫy. Cái tên GUM là viết tắt thời Xô Viết của 'Cửa hàng Bách hoá Nhà nước'. Ngày nay bên trong là các thương hiệu cao cấp, nhưng bạn không cần mua sắm để tận hưởng: nhiều du khách đến chỉ để ngắm kiến trúc, chụp ảnh, và nếm thử món kem GUM trứ danh — rẻ và ngon, được bán từ thời Xô Viết. Dịp Năm Mới và Giáng sinh, GUM khoác lên mình hàng triệu bóng đèn và trang trí lộng lẫy, trở thành một trong những điểm check-in đẹp nhất Moskva. Lời khuyên: cứ vào tự do ngắm nghía, đừng bỏ lỡ cây kem huyền thoại.",
        ["Mở cửa năm 1893 với tên 'Dãy Thương mại Thượng hạng', mái vòm kính-thép do Vladimir Shukhov thiết kế.",
         "Trải dài ~242 m dọc phía đông Quảng trường Đỏ, đối diện Kremlin.",
         "Tên GUM là viết tắt 'Cửa hàng Bách hoá Nhà nước' thời Xô Viết; nổi tiếng với kem GUM và triệu bóng đèn trang trí."],
        {"hours_vi": "Hằng ngày 10:00–22:00.", "ticket_vi": "Miễn phí (vào tham quan thương xá).",
         "duration_vi": "1–1,5 giờ.", "best_time_vi": "Dịp Năm Mới/Giáng sinh để ngắm trang trí; buổi tối khi lên đèn.",
         "tips_vi": "Vào tự do ngắm kiến trúc; thử kem GUM; đẹp nhất mùa lễ hội cuối năm."},
        photo_file="Gum Moscow.JPG", official="https://gumrussia.com",
        tags=["shopping", "free", "indoor", "architecture", "landmark"]),

    place("bolshoi-theatre", "Nhà hát Bolshoi", "Большой театр", "Bolshoi Theatre",
        ["theatre"], 55.760278, 37.618611, "Teatralnaya ploshchad 1, Moskva",
        {"value": 4.6, "count": 3916, "source": "Tripadvisor", "as_of": "2026-07"},
        "Khán giả ca ngợi ballet và opera đẳng cấp thế giới, khán phòng tân cổ điển đỏ-vàng tráng lệ và cảm giác chứng kiến lịch sử văn hoá Nga sống động. Phàn nàn thường gặp: trang web đặt vé chính thức lỗi thời khó dùng, ghế đặt cùng lần có thể không liền nhau, đồ ăn giờ giải lao rất đắt, đôi khi diễn bắt đầu trễ.",
        "Thánh đường ballet và opera của nước Nga, thành lập 1776, với khán phòng tân cổ điển đỏ-vàng lộng lẫy và cỗ xe tứ mã Apollo trên mặt tiền — biểu tượng trên tờ 100 rúp.",
        "Với người yêu nghệ thuật biểu diễn, Nhà hát Bolshoi là một điểm hành hương. Được thành lập năm 1776 dưới thời Nữ hoàng Ekaterina II, toà nhà hiện tại do kiến trúc sư Joseph Bové thiết kế và mở cửa năm 1825 sau khi các nhà hát trước đó bị hoả hoạn thiêu rụi. Mặt tiền tân cổ điển với hàng cột uy nghi, đỉnh là cỗ xe tứ mã bằng đồng do thần Apollo cầm cương, đã trở thành biểu tượng quốc gia — đến mức được in trên tờ tiền 100 rúp. Bên trong, khán phòng nhiều tầng đỏ thắm và dát vàng, những chùm đèn pha lê và tấm màn nhung khiến mỗi buổi diễn thành một sự kiện trọng thể. Bolshoi là quê nhà của một trong những đoàn ballet lâu đời và lớn nhất thế giới, với hơn hai trăm vũ công, sức chứa khoảng 1.740 khán giả. Một đêm xem 'Hồ Thiên Nga' hay 'Kẹp hạt dẻ' tại đây là trải nghiệm khó quên. Lưu ý: trang web bán vé chính thức khá khó dùng, ghế trong cùng một lần đặt có thể không liền nhau, và đồ ăn giờ giải lao rất đắt. Hãy đặt vé sớm và ăn mặc lịch sự.",
        ["Thành lập năm 1776 dưới thời Ekaterina II; toà nhà hiện tại (kiến trúc sư Joseph Bové) mở cửa năm 1825.",
         "Quê nhà một trong những đoàn ballet lâu đời và lớn nhất thế giới (hơn 200 vũ công), sức chứa ~1.740 khán giả.",
         "Mặt tiền với cỗ xe tứ mã của thần Apollo là biểu tượng quốc gia, được in trên tờ 100 rúp."],
        {"hours_vi": "Phòng vé hằng ngày ~11:00–20:00; suất diễn thường 12:00 (matinee) và 19:00 (tối).",
         "ticket_vi": "Tuỳ buổi diễn, ~2.000–15.000+ RUB; tour hậu trường ~2.500 RUB.",
         "duration_vi": "2–3 giờ (một buổi diễn).", "best_time_vi": "Mùa diễn thu–xuân; đặt vé sớm cho vở nổi tiếng.",
         "tips_vi": "Đặt vé sớm qua trang chính thức; ăn mặc lịch sự; kiểm tra ghế có liền nhau không."},
        photo_file="Moscow_Bolshoi_Theatre_2011.JPG", official="https://www.bolshoi.ru",
        tags=["theatre", "culture", "indoor", "evening"]),

    place("tretyakov-gallery", "Bảo tàng Tretyakov (Phòng tranh quốc gia)", "Третьяковская галерея", "State Tretyakov Gallery",
        ["museum"], 55.741389, 37.620864, "Lavrushinsky pereulok 10, Moskva",
        {"value": 4.7, "count": 5965, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách khâm phục bề dày nghệ thuật Nga từ icon trung cổ tới bậc thầy thế kỷ 19 và tiên phong đầu thế kỷ 20, cùng mặt tiền cổ tích của Vasnetsov; nhiều người nói tranh ngoài đời sống động hơn hẳn. Điểm chê: đông vào cuối tuần/lễ, một số tranh bị loá sáng, thiếu thang máy, và vé online thường cần thẻ ngân hàng Nga.",
        "Kho tàng nghệ thuật Nga vĩ đại nhất — từ icon trung cổ tới bậc thầy thế kỷ 19 — trong toà nhà mặt tiền cổ tích của hoạ sĩ Vasnetsov; nơi lưu giữ 'Chúa Ba Ngôi' của Rublev.",
        "Nếu muốn hiểu tâm hồn hội hoạ Nga, Bảo tàng Tretyakov là nơi phải đến. Được thương gia và nhà sưu tầm Pavel Tretyakov sáng lập năm 1856, ông đã hiến trọn bộ sưu tập của mình cho thành phố Moskva năm 1892. Ngày nay đây là bộ sưu tập mỹ thuật Nga hàng đầu thế giới với hơn 180.000 tác phẩm, trải dài từ những bức icon (thánh tượng) trung cổ tới các bậc thầy hiện thực thế kỷ 19 và nghệ thuật tiên phong đầu thế kỷ 20. Bạn sẽ được chiêm ngưỡng kiệt tác 'Chúa Ba Ngôi' của Andrei Rublev và bức icon 'Đức Mẹ Vladimir' được tôn kính. Bản thân toà nhà chính cũng là một tác phẩm: mặt tiền đỏ-trắng như trong cổ tích do chính hoạ sĩ Viktor Vasnetsov thiết kế, xây năm 1902–1904. Du khách thường nói tranh ở đây sống động hơn nhiều so với trong sách. Lưu ý: cuối tuần và ngày lễ rất đông, một số tranh bị loá sáng, ít thang máy giữa nhiều cầu thang, và vé online thường cần thẻ ngân hàng Nga (gây khó cho khách nước ngoài). Hãy dành 2–3 giờ và đi vào ngày thường.",
        ["Do thương gia Pavel Tretyakov sáng lập năm 1856; ông hiến trọn bộ sưu tập cho Moskva năm 1892.",
         "Bộ sưu tập mỹ thuật Nga hàng đầu thế giới, hơn 180.000 tác phẩm, gồm 'Chúa Ba Ngôi' của Rublev và 'Đức Mẹ Vladimir'.",
         "Mặt tiền đỏ-trắng cổ tích do hoạ sĩ Viktor Vasnetsov thiết kế, xây 1902–1904."],
        {"hours_vi": "Thứ 3,4,CN 10:00–18:00; Thứ 5,6,7 10:00–21:00; đóng cửa Thứ Hai.",
         "ticket_vi": "~700–1.000 RUB; giảm giá cho sinh viên và trẻ em.", "duration_vi": "2–3 giờ.",
         "best_time_vi": "Ngày thường; các buổi mở muộn (Thứ 5–7) ít đông hơn.",
         "tips_vi": "Đi ngày thường; chuẩn bị phương án vé (thẻ Nga/quầy); nhiều cầu thang nên đi giày êm."},
        photo_file="Moscow_05-2012_TretyakovGallery.jpg", official="https://www.tretyakovgallery.ru",
        tags=["museum", "art", "indoor", "top"]),

    place("christ-the-saviour", "Nhà thờ Chúa Cứu Thế (Khram Khrista Spasitelya)", "Храм Христа Спасителя", "Cathedral of Christ the Saviour",
        ["church"], 55.744444, 37.605556, "Ulitsa Volkhonka 15, Moskva",
        {"value": 4.4, "count": 2173, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách ấn tượng với quy mô đồ sộ, đá cẩm thạch trắng và mái vòm vàng, nhất là vị trí bên sông và ánh đèn ban đêm; nhiều người thích tầm nhìn Kremlin từ đài quan sát có thu phí. Điểm chê: dù tráng lệ, nơi đây có phần giống đài tưởng niệm hơn nơi cầu nguyện ấm cúng, và quy định vào đài quan sát đôi khi cứng nhắc.",
        "Thánh đường Chính thống giáo cao nhất thế giới (~103 m), mái vòm vàng bên sông Moskva — bản phục dựng của nhà thờ bị Stalin cho nổ tung năm 1931.",
        "Sừng sững bên bờ sông Moskva với mái vòm vàng lấp lánh, Nhà thờ Chúa Cứu Thế là thánh đường Chính thống giáo cao nhất thế giới, vươn lên khoảng 103 mét. Nhưng câu chuyện của nó cũng bi tráng như chính lịch sử nước Nga. Nhà thờ nguyên bản được thánh hiến năm 1883 để tạ ơn chiến thắng trước Napoléon; chính vì dịp này mà Tchaikovsky đã soạn bản 'Khúc mở màn 1812' lừng danh. Năm 1931, theo lệnh Stalin, công trình bị cho nổ tung để nhường chỗ cho một 'Cung điện Xô Viết' khổng lồ — dự án không bao giờ thành hình, và khu đất về sau biến thành một bể bơi ngoài trời. Chỉ sau khi Liên Xô tan rã, nhà thờ mới được phục dựng gần như y nguyên trong các năm 1994–2000. Bên trong là không gian bằng đá cẩm thạch trắng và vàng lộng lẫy; từ đài quan sát (có thu phí), bạn có thể ngắm toàn cảnh Kremlin và dòng sông. Du khách ấn tượng bởi quy mô hoành tráng, dù một số thấy nó giống một đài tưởng niệm hơn là nơi cầu nguyện ấm cúng. Đẹp nhất là về đêm khi lên đèn.",
        ["Cao ~103 m — thánh đường Chính thống giáo cao nhất thế giới.",
         "Nhà thờ nguyên bản (thánh hiến 1883) bị Stalin cho nổ tung năm 1931; bản hiện tại phục dựng 1994–2000.",
         "Tchaikovsky soạn 'Khúc mở màn 1812' cho lễ thánh hiến nhà thờ nguyên bản."],
        {"hours_vi": "Hằng ngày ~10:00–18:00 (Thứ Hai từ 13:00); có thánh lễ hằng ngày.",
         "ticket_vi": "Vào nhà thờ miễn phí; đài quan sát ~400 RUB.", "duration_vi": "30–60 phút.",
         "best_time_vi": "Về đêm khi lên đèn; leo đài quan sát ngắm Kremlin.",
         "tips_vi": "Ăn mặc kín đáo; cân nhắc lên đài quan sát ngắm toàn cảnh; miễn phí vào nhà thờ."},
        photo_file="Moscow_-_Cathedral_of_Christ_the_Saviour.jpg", official="http://www.xxc.ru",
        tags=["church", "free", "viewpoint", "landmark"]),

    place("novodevichy", "Tu viện Novodevichy", "Новодевичий монастырь", "Novodevichy Convent",
        ["church"], 55.726111, 37.556111, "Novodevichy proezd 1, Moskva",
        {"value": 4.4, "count": 1794, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách yêu khuôn viên tĩnh lặng sau tường trắng tháp đỏ, kiến trúc thế kỷ 16–17 được bảo tồn tốt, và nghĩa trang kề bên nơi nhiều danh nhân Nga an nghỉ. Điểm chê gần đây: một số nhà thờ đóng hoặc đang trùng tu, siết chặt tiếp cận từ khi giao cho Giáo hội, thường chỉ nhận tiền mặt, ít triển lãm lịch sử hơn trước.",
        "Tu viện tường trắng tháp đỏ theo phong cách Baroque Moskva (xây từ 1524), Di sản Thế giới UNESCO, cạnh nghĩa trang nơi Chekhov, Gogol, Shostakovich an nghỉ.",
        "Bên một hồ nước phía tây nam Moskva, Tu viện Novodevichy hiện lên thanh bình sau những bức tường trắng và tháp canh đỏ. Được Đại công tước Vasili III cho xây dựng năm 1524 để mừng việc giành lại Smolensk từ tay Litva, tu viện là một trong những ví dụ đẹp nhất của phong cách 'Baroque Moskva' cầu kỳ, và đã được UNESCO công nhận Di sản Thế giới năm 2004. Quần thể kiến trúc thế kỷ 16–17 được bảo tồn gần như nguyên vẹn, với nhà thờ trung tâm, tháp chuông và những bức tường thành như một pháo đài nhỏ. Nhưng với nhiều du khách, điều cuốn hút nhất nằm ngay bên cạnh: Nghĩa trang Novodevichy — nơi an nghỉ danh giá bậc nhất nước Nga, quy tụ mộ phần của những tên tuổi lớn như nhà văn Chekhov, Gogol, nhà soạn nhạc Shostakovich, và các nhà lãnh đạo Khrushchev, Yeltsin. Dạo bước giữa những bia mộ nghệ thuật là một trải nghiệm trầm mặc, đầy cảm xúc. Lưu ý: từ khi tu viện được giao lại cho Giáo hội, một số nhà thờ đóng hoặc đang trùng tu, thanh toán thường chỉ nhận tiền mặt. Hãy đến vào buổi sáng để tận hưởng sự yên tĩnh.",
        ["Do Đại công tước Vasili III cho xây năm 1524, mừng việc giành lại Smolensk từ Litva.",
         "Di sản Thế giới UNESCO (2004), ví dụ tiêu biểu của phong cách 'Baroque Moskva'.",
         "Nghĩa trang Novodevichy kề bên là nơi an nghỉ của Chekhov, Gogol, Shostakovich, Khrushchev và Yeltsin."],
        {"hours_vi": "Khuôn viên hằng ngày ~9:00–19:00; bảo tàng tu viện ~10:00–17:00 (đóng cửa Thứ Ba).",
         "ticket_vi": "Khuôn viên miễn phí; triển lãm bảo tàng ~300–500 RUB (phí chụp ảnh ~100 RUB).",
         "duration_vi": "1–2 giờ (lâu hơn nếu thăm nghĩa trang).", "best_time_vi": "Buổi sáng để yên tĩnh; thu hoặc đông đẹp.",
         "tips_vi": "Mang tiền mặt; kết hợp thăm Nghĩa trang Novodevichy; ăn mặc kín đáo."},
        photo_file="Novodevichy_Convent_3.jpg", official="https://novodev.msk.ru",
        tags=["church", "outdoor", "unesco", "history"]),

    place("vdnkh", "Công viên triển lãm VDNKh", "ВДНХ", "VDNKh",
        ["park_garden", "monument"], 55.834024, 37.630320, "Prospekt Mira 119, Moskva",
        {"value": 4.4, "count": 1883, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách yêu kiến trúc Xô Viết hoành tráng, các gian trưng bày cầu kỳ và đài phun nước mạ vàng (đặc biệt về đêm), và thích việc khuôn viên rộng có bảo tàng, vườn, ẩm thực, sự kiện cho cả ngày. Điểm chê: giá đồ ăn/quà lưu niệm cao, một số gian còn trống, đang tu sửa nhiều chỗ, và quá rộng để xem hết trong một lần.",
        "Quần thể triển lãm kiểu Xô Viết hoành tráng (mở 1939) với những gian trưng bày nguy nga và đài phun nước mạ vàng 'Tình hữu nghị các dân tộc' — rộng hơn cả Monaco.",
        "VDNKh (Triển lãm Thành tựu Kinh tế Quốc dân) là một trong những di sản Xô Viết ngoạn mục nhất Moskva. Mở cửa năm 1939, quần thể rộng khoảng 2,4 km² — lớn hơn cả công quốc Monaco — và từng có tới 82 gian trưng bày được xây theo phong cách các nước cộng hoà và ngành kinh tế Xô Viết. Trung tâm là những đài phun nước lộng lẫy, nổi bật nhất là 'Tình hữu nghị các dân tộc' với 16 pho tượng thiếu nữ mạ vàng tượng trưng cho các nước cộng hoà Liên Xô cũ. Ở lối vào sừng sững tượng đài 'Công nhân và Nữ nông trang viên' cao 25 mét — tác phẩm từng được tạo ra cho Hội chợ Thế giới Paris 1937. Ngày nay VDNKh là một không gian giải trí – văn hoá khổng lồ: bảo tàng, vườn, quán ăn, sân trượt băng mùa đông và vô số sự kiện, đủ cho cả một ngày dạo chơi. Du khách mê kiến trúc hoành tráng và các đài phun nước, nhất là khi lên đèn về đêm. Lưu ý: đồ ăn và quà lưu niệm khá đắt, một số gian trưng bày còn trống hoặc đang tu sửa, và diện tích quá rộng nên khó xem hết. Hãy chọn trước vài khu muốn thăm.",
        ["Mở cửa năm 1939, rộng ~2,4 km² (lớn hơn Monaco), từng có 82 gian trưng bày theo các nước cộng hoà và ngành kinh tế Xô Viết.",
         "Đài phun nước 'Tình hữu nghị các dân tộc' có 16 pho tượng thiếu nữ mạ vàng tượng trưng cho các nước cộng hoà Liên Xô cũ.",
         "Tượng đài 'Công nhân và Nữ nông trang viên' cao 25 m, vốn được tạo cho Hội chợ Thế giới Paris 1937."],
        {"hours_vi": "Khuôn viên mở cửa hằng ngày, miễn phí (thường ghi 24 giờ); phần lớn gian trưng bày/bảo tàng ~11:00–22:00 theo lịch riêng.",
         "ticket_vi": "Miễn phí vào khuôn viên; các gian, bảo tàng, sân trượt băng và trò chơi bán vé riêng (~200–600 RUB mỗi mục).",
         "duration_vi": "3–5 giờ (có thể chơi cả ngày).",
         "best_time_vi": "Mùa hè cho đài phun nước; mùa đông có sân trượt băng; buổi tối khi lên đèn.",
         "tips_vi": "Chọn trước vài khu muốn thăm; mang nước/đồ ăn nhẹ; đi giày thoải mái vì diện tích rộng."},
        photo_file="Moscow, VDNKh, Friendship of Nations fountain (10656732243).jpg", official="https://vdnh.ru",
        tags=["park", "free", "outdoor", "soviet", "family"]),

    place("gorky-park", "Công viên Gorky", "Парк Горького", "Gorky Park",
        ["park_garden"], 55.728333, 37.600000, "Krymsky Val 9, Moskva",
        {"value": 4.5, "count": 2803, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách khen không gian xanh ven sông rộng, sạch và nhiều hoạt động cho gia đình — đạp xe, trượt băng, bảo tàng, rạp ngoài trời, quán cà phê — gọi đây là 'công viên có tất cả'. Điểm chê thường gặp: giá đồ uống/đồ ăn cao và rất đông vào cuối tuần hoặc ngày đẹp trời, ít chỗ trú mưa.",
        "Công viên ven sông đầu tiên kiểu 'văn hoá và nghỉ ngơi' của Liên Xô (1928), nay hiện đại và miễn phí — đạp xe, trượt băng, bảo tàng, rạp chiếu ngoài trời.",
        "Trải dài bên bờ sông Moskva, Công viên Gorky là lá phổi xanh được yêu thích nhất của thủ đô. Mở cửa năm 1928, đây là công viên 'văn hoá và nghỉ ngơi' đầu tiên của Liên Xô, và được đặt tên theo nhà văn Maxim Gorky năm 1932. Suốt thời Xô Viết, nơi đây gắn với những vòng đu quay và hội chợ; nhưng một cuộc cải tạo lớn năm 2011 đã lột xác công viên: bỏ vé vào cửa (nay hoàn toàn miễn phí), dẹp các trò chơi cũ kỹ, và bổ sung một sân trượt băng mùa đông rộng khoảng 15.000 m² cùng Bảo tàng Nghệ thuật Đương đại Garage. Ngày nay Gorky là 'công viên có tất cả': đạp xe, trượt patin, yoga, quán cà phê ven sông, rạp chiếu phim ngoài trời và không gian sự kiện. Thú vị là công viên còn truyền cảm hứng cho một cuốn tiểu thuyết trinh thám nổi tiếng của phương Tây và được nhắc tới trong một ca khúc rock kinh điển thập niên 1990. Du khách khen không gian rộng, sạch và thân thiện với gia đình. Lưu ý: đồ uống và đồ ăn khá đắt, và rất đông vào cuối tuần hoặc ngày đẹp trời. Hãy đến vào buổi chiều muộn để tận hưởng hoàng hôn bên sông.",
        ["Mở cửa năm 1928 — công viên 'văn hoá và nghỉ ngơi' đầu tiên của Liên Xô; đặt tên theo nhà văn Maxim Gorky năm 1932.",
         "Cải tạo năm 2011: bỏ vé vào cửa (miễn phí), thêm sân trượt băng ~15.000 m² và Bảo tàng Nghệ thuật Đương đại Garage.",
         "Truyền cảm hứng cho tiểu thuyết trinh thám 'Gorky Park' và được nhắc tới trong một ca khúc rock nổi tiếng thập niên 1990."],
        {"hours_vi": "Mở cửa 24 giờ, miễn phí (khu vườn tượng Muzeon ~08:00–22:00).",
         "ticket_vi": "Miễn phí vào cửa; một số hoạt động thu phí riêng (bảo tàng Garage, sân trượt băng, trò chơi).",
         "duration_vi": "1,5–3 giờ.", "best_time_vi": "Chiều muộn mùa hè cho hoàng hôn ven sông; mùa đông có sân trượt băng.",
         "tips_vi": "Thuê xe đạp/patin; mang theo đồ ăn nhẹ vì giá trong công viên cao; tránh cuối tuần nếu ngại đông."},
        photo_file="Moscow_Gorky_Park_main_portal_08-2016_img1.jpg", official="https://parkgorkogo.ru",
        tags=["park", "free", "outdoor", "relax", "family"]),

    place("moscow-metro", "Tàu điện ngầm Moskva (ga Komsomolskaya & các ga nghệ thuật)", "Московский метрополитен", "Moscow Metro",
        ["monument"], 55.774722, 37.655000, "Ga Komsomolskaya, Komsomolskaya ploshchad, Moskva",
        {"value": 4.6, "count": 17077, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách ví các ga trung tâm như 'cung điện dưới lòng đất', trầm trồ trước đèn chùm, tranh khảm và cột cẩm thạch, đồng thời khen dịch vụ rẻ, sạch, đúng giờ và dày chuyến (vé chưa tới 1 euro). Điểm chê: biển chỉ dẫn chủ yếu tiếng Nga (Cyrillic) gây khó cho khách nước ngoài, và giờ cao điểm quá đông để ngắm hay chụp ảnh kiến trúc.",
        "Hệ thống metro như 'cung điện dưới lòng đất' — đèn chùm, tranh khảm, cột cẩm thạch; ga Komsomolskaya, Ploshchad Revolyutsii và Mayakovskaya là những điểm phải xem, vé chưa tới 1 euro.",
        "Ít ai ngờ một trong những điểm tham quan đẹp nhất Moskva lại nằm dưới lòng đất. Khai trương năm 1935, Tàu điện ngầm Moskva được xây dựng như những 'cung điện cho nhân dân' — và đến nay vẫn khiến du khách sững sờ. Các ga trung tâm lộng lẫy với đèn chùm pha lê, tranh khảm mosaic, tượng đồng, trần vòm và cột cẩm thạch. Toạ độ ở đây là ga Komsomolskaya trên tuyến Vành đai (Koltsevaya), mở năm 1952 — một trong những ga nguy nga nhất, với đại sảnh trần vàng theo phong cách Baroque, đèn chùm và tám bức khảm của hoạ sĩ Pavel Korin về các anh hùng quân sự Nga. Đừng bỏ lỡ ga Ploshchad Revolyutsii với 76 pho tượng đồng (du khách hay xoa mũi chú chó để lấy may), hay ga Art Deco Mayakovskaya từng đoạt Giải thưởng Lớn tại Hội chợ Thế giới New York 1939. Điều tuyệt vời: bạn chỉ trả đúng giá vé metro (chưa tới một euro) để chiêm ngưỡng tất cả, tàu lại sạch, đúng giờ và dày chuyến. Lưu ý: biển chỉ dẫn chủ yếu bằng tiếng Nga (Cyrillic) nên hơi khó cho khách nước ngoài, và giờ cao điểm rất đông. Hãy đi tham quan các ga vào giữa buổi để dễ chụp ảnh.",
        ["Toạ độ là ga Komsomolskaya (tuyến Vành đai, mở 1952) — đại sảnh trần vàng Baroque, đèn chùm và 8 bức khảm của Pavel Korin.",
         "Metro Moskva mở năm 1935, chở hàng triệu khách mỗi ngày, nhiều ga trung tâm được xây như 'cung điện cho nhân dân'.",
         "Các ga nổi bật khác: Ploshchad Revolyutsii với 76 tượng đồng, và Mayakovskaya Art Deco từng đoạt Giải thưởng Lớn tại Hội chợ Thế giới New York 1939."],
        {"hours_vi": "Metro chạy hằng ngày khoảng 05:30–01:00.",
         "ticket_vi": "Chỉ giá vé metro thường: ~75 RUB/lượt bằng thẻ Troika, hoặc ~90 RUB vé giấy (2026); không thu phí tham quan riêng.",
         "duration_vi": "1–2 giờ để tham quan các ga trung tâm nguy nga nhất.",
         "best_time_vi": "Giữa buổi (ngoài giờ cao điểm) để dễ chụp ảnh.",
         "tips_vi": "Dùng thẻ Troika cho rẻ; đi ngoài giờ cao điểm; ghi sẵn tên ga bằng Cyrillic để dễ tìm."},
        photo_file="Komsomolskaya (Koltsevaya Line) (19343583583).jpg", official="https://mosmetro.ru",
        tags=["architecture", "landmark", "cheap", "indoor", "top"]),

    place("zaryadye-park", "Công viên Zaryadye", "Парк Зарядье", "Zaryadye Park",
        ["park_garden", "bridge"], 55.751111, 37.628889, "Ulitsa Varvarka 6, Moskva",
        {"value": 3.9, "count": 946, "source": "Tripadvisor", "as_of": "2026-07"},
        "Du khách mê 'cầu bay' hình chữ V và tầm nhìn ra Kremlin cùng sông Moskva, vị trí ngay cạnh Quảng trường Đỏ, và ý tưởng tái hiện các vùng khí hậu Nga. Điểm chê thường gặp: các gian trong nhà đắt (nhiều người gọi 'Hang băng' là 'chặt chém'), thủ tục vào lộn xộn, nhân viên chưa niềm nở, và mùa đông cảnh hơi ảm đạm.",
        "Công viên hiện đại cạnh Quảng trường Đỏ (mở 2017) với 'cầu bay' hình chữ V vươn ra sông Moskva — tái hiện bốn vùng khí hậu của nước Nga.",
        "Ngay cạnh Quảng trường Đỏ, Zaryadye là công viên lớn đầu tiên được xây mới ở trung tâm Moskva trong hơn nửa thế kỷ. Mở cửa tháng 9/2017 trên nền khách sạn Rossiya cũ bị phá dỡ, công viên rộng khoảng 13 hecta này là một tuyên ngôn của Moskva hiện đại. Điểm nhấn nổi tiếng nhất là 'Cầu bay' (hay 'Cầu lơ lửng') hình chữ V: một khối bê tông vươn khoảng 70 mét ra trên sông Moskva mà không có trụ đỡ, mang đến tầm nhìn ngoạn mục ra Kremlin và dòng sông — một trong những góc check-in đắt giá nhất thành phố. Điều độc đáo là công viên tái hiện bốn vùng cảnh quan của nước Nga — rừng, thảo nguyên, đài nguyên (tundra) và đầm lầy — thu nhỏ ngay giữa lòng thủ đô. Zaryadye còn có phòng hoà nhạc, các gian trưng bày và rạp chiếu phim vòm. Tạp chí TIME từng đưa nơi đây vào danh sách 'Những địa điểm tuyệt vời nhất thế giới' năm 2018. Lưu ý: khuôn viên và cầu bay vào cửa tự do, nhưng các gian trong nhà (như 'Hang băng', phim vòm) thu phí và bị nhiều du khách chê đắt; thủ tục vào đôi khi lộn xộn; mùa đông cảnh hơi ảm đạm. Hãy đến để ngắm Kremlin từ cầu bay lúc hoàng hôn.",
        ["Mở cửa tháng 9/2017 trên nền khách sạn Rossiya cũ — công viên lớn đầu tiên ở trung tâm Moskva trong hơn 50 năm.",
         "'Cầu bay' hình chữ V vươn ~70 m ra sông Moskva mà không có trụ đỡ, cho tầm nhìn ra Kremlin.",
         "Rộng 13 hecta, tái hiện 4 vùng cảnh quan Nga (rừng, thảo nguyên, đài nguyên, đầm lầy); vào danh sách 'Địa điểm tuyệt vời nhất thế giới' của TIME 2018."],
        {"hours_vi": "Khuôn viên và cầu bay mở 24/7, miễn phí; các gian trong nhà ~10:00–21:00 (Thứ Hai từ 12:00).",
         "ticket_vi": "Công viên và cầu bay miễn phí; các gian thu phí: phim vòm ~700–900 RUB, 'Hang băng'/Florarium ~250–400 RUB.",
         "duration_vi": "1,5–2,5 giờ.", "best_time_vi": "Hoàng hôn để ngắm Kremlin từ cầu bay; mùa hè hoặc thu.",
         "tips_vi": "Ra cầu bay ngắm Kremlin; cân nhắc kỹ trước khi mua vé các gian trong nhà; kết hợp Quảng trường Đỏ."},
        photo_file="Hovering Bridge, Zaryadye Park (37237251426).jpg", official="https://www.zaryadyepark.ru",
        tags=["park", "free", "outdoor", "viewpoint", "modern"]),
]


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(PLACES, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(PLACES)} places -> {OUT}")


if __name__ == "__main__":
    main()
