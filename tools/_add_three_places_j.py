# -*- coding: utf-8 -*-
"""_add_three_places_j.py — Bổ sung 3 địa điểm nổi tiếng/hiện đại còn thiếu (lần chạy tự động 2026-07-25, đợt j).

Thêm:
  1) Moskva            — Bảo tàng Moskva (Muzey Moskvy) — bảo tàng lịch sử thành phố trong tổ hợp Kho Quân lương.
  2) Saint Petersburg  — Cung điện Anichkov — toà nhà đá cổ nhất trên Nevsky, nay là Cung Sáng tạo Thiếu nhi.
  3) Krasnodar (Sochi) — Skypark AJ Hackett Sochi — công viên mạo hiểm với cầu treo SkyBridge dài 439 m.

Nội dung tiếng Việt nguyên gốc (không dịch/sao chép nguyên văn). Toạ độ thật đã kiểm chứng qua web.
Chạy:  python3 tools/_add_three_places_j.py
"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TODAY = "2026-07-25"
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def maps_for(lat, lon):
    return {
        "yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=17&l=map",
        "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
    }


MUSEUM_OF_MOSCOW = {
    "id": "moscow-museum-of-moscow",
    "slug": "museum-of-moscow",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Bảo tàng Moskva (Muzey Moskvy, Mu-dây Mát-xcơ-va)",
    "name_ru": "Музей Москвы",
    "name_en": "Museum of Moscow",
    "categories": ["museum"],
    "coordinates": {"lat": 55.73625, "lon": 37.59417},
    "address_vi": "Đại lộ Zubovsky, số 2, Moskva (tổ hợp Kho Quân lương — Proviantskie Sklady, bên Vành đai Vườn); gần ga tàu điện ngầm Park Kultury.",
    "rating": None,
    "review_summary_vi": "Khách tham quan xem đây là điểm đến dễ tiếp cận để nắm bắt lịch sử Moskva, với không gian kho cổ rộng rãi và các triển lãm dàn dựng chỉn chu. Nhiều người thích khoảng sân trong tổ chức sự kiện, hoà nhạc mùa hè cùng các hoạt động cho trẻ em. Một điểm nên lưu ý: nội dung trưng bày thay đổi theo từng triển lãm chuyên đề nên hãy xem trước lịch.",
    "presentation_short_vi": "Bảo tàng chính thức về lịch sử thủ đô Moskva, thành lập năm 1896. Từ năm 2008, bảo tàng đặt trong tổ hợp Kho Quân lương kiểu Đế chế nửa đầu thế kỷ 19 bên đại lộ Zubovsky, lưu giữ khoảng 790 nghìn hiện vật kể lại chặng đường phát triển của thành phố.",
    "presentation_long_vi": "Được Duma (Hội đồng) thành phố Moskva thành lập năm 1896 với tên gọi ban đầu là Bảo tàng Kinh tế Đô thị Moskva, đây là thiết chế chuyên sưu tầm, lưu giữ và kể lại lịch sử của chính thủ đô nước Nga. Trải qua hơn một thế kỷ, bảo tàng nhiều lần đổi tên và đổi chỗ, đến năm 2008 mới về hẳn tổ hợp Kho Quân lương (Proviantskie Sklady) bên đại lộ Zubovsky và mang tên gọn là Bảo tàng Moskva. Cụm ba toà nhà này dựng vào nửa đầu thế kỷ 19 theo thiết kế mẫu phong cách Đế chế (Empire) của kiến trúc sư Vasily Stasov, do Fyodor Shestakov thi công, vốn là kho dự trữ lương thực cho quân đội — nay là một di tích kiến trúc được nhà nước bảo vệ. Bộ sưu tập của bảo tàng gồm khoảng 790 nghìn hiện vật: từ các phát hiện khảo cổ dưới lòng Moskva, bản đồ cổ, tranh khắc, ảnh tư liệu cho tới đồ dùng sinh hoạt và trang phục gắn với đời sống thị dân qua các thời kỳ. Không gian rộng cùng khoảng sân trong của khu kho thường xuyên được dùng cho triển lãm chuyên đề, buổi thuyết trình, lớp học cho trẻ em và các lễ hội, hoà nhạc mùa hè. Nằm sát ga tàu điện ngầm Park Kultury và không xa Công viên Gorky, Bảo tàng Moskva là nơi lý tưởng để hiểu hành trình một khu định cư bên sông vươn mình thành siêu đô thị như ngày nay.",
    "highlights_vi": [
        "Bảo tàng chuyên khảo về lịch sử và đời sống của chính thành phố Moskva, thành lập năm 1896.",
        "Trụ sở là tổ hợp Kho Quân lương (Proviantskie Sklady) phong cách Đế chế nửa đầu thế kỷ 19 — di tích kiến trúc bên Vành đai Vườn, cạnh ga Park Kultury.",
        "Bộ sưu tập khoảng 790.000 hiện vật; sân trong thường xuyên có triển lãm, hoà nhạc, lễ hội và lớp học cho trẻ em.",
    ],
    "practical": {
        "hours_vi": "Mở cửa hầu hết các ngày trong tuần, thường nghỉ thứ Hai; nên kiểm tra giờ mở và lịch triển lãm trên trang chính thức trước khi đến.",
        "ticket_vi": "Vé vào khu trưng bày chính và vé triển lãm chuyên đề tính riêng; có ưu đãi cho học sinh, sinh viên, người cao tuổi. Giá thay đổi theo chương trình.",
        "duration_vi": "Khoảng 1,5–2 giờ; thêm thời gian nếu xem triển lãm chuyên đề.",
        "best_time_vi": "Buổi sáng ngày thường ít đông; mùa hè có thêm sự kiện ngoài sân.",
        "tips_vi": "Đi bộ vài phút từ ga Park Kultury; dễ kết hợp tham quan Công viên Gorky, công viên điêu khắc Muzeon và Phòng tranh Tretyakov Mới gần đó.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.73625, 37.59417),
    "official_site": "https://mosmuseum.ru",
    "sources": [
        {"title": "Museum of Moscow — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Museum_of_Moscow"},
        {"title": "Uỷ ban UNESCO của LB Nga — Bảo tàng Moskva", "url": "https://unesco.ru/en/news/56-museum-of-moscow/"},
        {"title": "Trang chính thức Bảo tàng Moskva", "url": "https://mosmuseum.ru"},
    ],
    "tags": ["museum", "history", "indoor", "family"],
    "status": "enriched",
    "last_updated": TODAY,
}


ANICHKOV_PALACE = {
    "id": "saint-petersburg-anichkov-palace",
    "slug": "anichkov-palace",
    "region": "saint-petersburg",
    "region_name_vi": "Saint Petersburg",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Cung điện Anichkov (Anichkov Dvorets, A-nhi-chcốp)",
    "name_ru": "Аничков дворец",
    "name_en": "Anichkov Palace",
    "categories": ["palace"],
    "coordinates": {"lat": 59.93278, "lon": 30.33972},
    "address_vi": "Đại lộ Nevsky, số 39, Sankt-Peterburg (bên sông Fontanka, cạnh Cầu Anichkov); gần ga tàu điện ngầm Gostiny Dvor và Ploshchad Vosstaniya.",
    "rating": None,
    "review_summary_vi": "Du khách thường ngắm cung điện từ Cầu Anichkov và đánh giá cao vị trí đắc địa ngay trên đại lộ Nevsky, bên dòng Fontanka. Nhiều người thấy thú vị khi biết toà nhà trông như một cung điện hoàng gia nay là nơi sinh hoạt của thiếu nhi thành phố. Vì là cơ sở giáo dục đang hoạt động, khách nên tìm hiểu trước về khả năng vào thăm nội thất.",
    "presentation_short_vi": "Toà nhà bằng đá cổ nhất trên đại lộ Nevsky, khởi công năm 1741 dưới thời Nữ hoàng Elizaveta và hoàn tất năm 1754. Từng là dinh thị thành của nhiều hoàng đế Nga tương lai, ngày nay cung điện là Cung Sáng tạo Thiếu nhi của thành phố Sankt-Peterburg.",
    "presentation_long_vi": "Nằm đúng nơi đại lộ Nevsky bắc qua sông Fontanka, ngay cạnh Cầu Anichkov trứ danh với bốn cụm tượng 'Người thuần ngựa' của điêu khắc gia Klodt, Cung điện Anichkov được xem là công trình bằng đá lâu đời nhất trên trục phố chính của Sankt-Peterburg. Nữ hoàng Elizaveta Petrovna cho khởi công năm 1741; các kiến trúc sư Mikhail Zemtsov rồi Bartolomeo Rastrelli nối tiếp, đến năm 1754 thì hoàn tất theo phong cách Baroque. Nữ hoàng ban toà cung cho bá tước Aleksey Razumovsky — người bạn đời không chính thức của bà. Về sau, Nữ hoàng Ekaterina II mua lại rồi tặng cho công tước Grigory Potemkin; kiến trúc sư Ivan Starov đã chỉnh sửa dáng vẻ bên ngoài theo hướng tân cổ điển điềm đạm hơn. Suốt thế kỷ 19, cung điện là nơi ở tại kinh đô của nhiều người thừa kế ngai vàng trước khi đăng quang, trong đó có các hoàng đế tương lai Nikolai I, Aleksandr II và Aleksandr III. Sau Cách mạng Tháng Mười năm 1917, toà nhà từng làm bảo tàng thành phố rồi trở thành Cung Thiếu niên Tiền phong Leningrad. Ngày nay, dưới tên Cung Sáng tạo Thiếu nhi thành phố Sankt-Peterburg, nơi đây vẫn rộn ràng các câu lạc bộ, lớp học ngoại khoá và sự kiện cho hàng nghìn em nhỏ, giữ vai trò một trung tâm giáo dục — văn hoá ngay giữa lòng phố Nevsky nhộn nhịp.",
    "highlights_vi": [
        "Công trình bằng đá lâu đời nhất trên đại lộ Nevsky, xây trong các năm 1741–1754 thời Nữ hoàng Elizaveta.",
        "Từng thuộc về bá tước Razumovsky rồi công tước Potemkin; là nơi ở của các hoàng đế Nga tương lai Nikolai I, Aleksandr II và Aleksandr III.",
        "Sau năm 1917 trở thành Cung Thiếu niên Tiền phong; nay là Cung Sáng tạo Thiếu nhi — trung tâm giáo dục ngoại khoá lớn của thành phố.",
    ],
    "practical": {
        "hours_vi": "Là cơ sở giáo dục đang hoạt động nên không mở cửa tự do như bảo tàng; nội thất lịch sử thường chỉ thăm được theo tour đặt trước. Mặt tiền và khu vườn có thể ngắm tự do.",
        "ticket_vi": "Tham quan các gian phòng lịch sử theo đoàn/đặt lịch; nhiều hoạt động cho thiếu nhi miễn phí hoặc theo chương trình.",
        "duration_vi": "Khoảng 30–45 phút ngắm mặt tiền và vườn; 1–1,5 giờ nếu có tour nội thất.",
        "best_time_vi": "Kết hợp khi dạo đại lộ Nevsky; buổi tối khu Cầu Anichkov và bờ Fontanka lên đèn rất đẹp.",
        "tips_vi": "Đứng trên Cầu Anichkov để ngắm cung điện cùng bốn cụm tượng ngựa của Klodt; gần thương xá Gostiny Dvor và Cung Beloselsky-Belozersky.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(59.93278, 30.33972),
    "official_site": "https://www.anichkov.ru",
    "sources": [
        {"title": "Anichkov Palace — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Anichkov_Palace"},
        {"title": "Anichkov Palace — saint-petersburg.com", "url": "http://www.saint-petersburg.com/palaces/anichkov-palace/"},
        {"title": "Cung Sáng tạo Thiếu nhi Sankt-Peterburg (trang chính thức)", "url": "https://www.anichkov.ru"},
    ],
    "tags": ["palace", "history", "architecture", "landmark", "nevsky"],
    "status": "enriched",
    "last_updated": TODAY,
}


SKYPARK_SOCHI = {
    "id": "krasnodar-skypark-sochi",
    "slug": "skypark-sochi",
    "region": "krasnodar",
    "region_name_vi": "Vùng Krasnodar",
    "federal_district": "Vùng Nam",
    "name_vi": "Skypark AJ Hackett Sochi (Công viên mạo hiểm & cầu treo SkyBridge, Xcai-pác)",
    "name_ru": "Скайпарк AJ Hackett Sochi",
    "name_en": "Skypark AJ Hackett Sochi (SkyBridge)",
    "categories": ["bridge", "park_garden"],
    "coordinates": {"lat": 43.52531, "lon": 39.99736},
    "address_vi": "Phố Krasnoflotskaya, số 54A, làng Kazachy Brod, thành phố Sochi, Vùng Krasnodar (hẻm núi Akhshtyr, thung lũng sông Mzymta, trên đường lên Krasnaya Polyana); cách Adler khoảng 20 km.",
    "rating": None,
    "review_summary_vi": "Du khách mô tả đây là trải nghiệm 'nghẹt thở' đáng nhớ: đi bộ trên cây cầu treo lắc lư giữa hẻm núi sâu, phóng tầm mắt ra núi và biển. Người mê cảm giác mạnh thích các cú bungee và đu khổng lồ, trong khi khách nhẹ nhàng vẫn tận hưởng cảnh quan khi qua cầu. Một số lưu ý giá vé các trò chơi khá cao và nên đặt trước vào mùa cao điểm.",
    "presentation_short_vi": "Công viên giải trí mạo hiểm bên hẻm núi sông Mzymta ở Sochi, khai trương năm 2014. Điểm nhấn là cầu treo đi bộ SkyBridge dài 439 m, treo cao khoảng 207 m so với đáy hẻm, cùng loạt trò cảm giác mạnh như nhảy bungee, đu khổng lồ và trượt dây.",
    "presentation_long_vi": "Skypark AJ Hackett Sochi là công viên phiêu lưu mạo hiểm do hãng bungee lừng danh của New Zealand — AJ Hackett — vận hành, nằm trong ranh giới Vườn quốc gia Sochi, nơi hẻm núi Akhshtyr thuộc thung lũng sông Mzymta, trên tuyến đường nối trung tâm Sochi với khu nghỉ dưỡng núi Krasnaya Polyana. Khai trương năm 2014, công viên gây tiếng vang nhờ cây cầu treo dành cho người đi bộ mang tên SkyBridge dài 439 mét, bắc ngang hẻm núi ở độ cao khoảng 207 mét — vào thời điểm khánh thành thuộc hàng cầu treo đi bộ dài nhất thế giới. Đứng giữa cầu, du khách thu vào tầm mắt khung cảnh dãy Kavkaz trùng điệp và thấp thoáng dải bờ Biển Đen phía xa. Với người ưa cảm giác mạnh, đây là 'thiên đường adrenaline': cú nhảy bungee Bungy 207 từ độ cao 207 mét (được giới thiệu là cao nhất châu Âu), phiên bản nhẹ hơn Bungy 69, chiếc đu khổng lồ SochiSwing, đường trượt dây MegaTroll đạt tốc độ tới 120 km/h, công viên dây 'Mowgli' cho trẻ em và tuyến leo vách Via Ferrata dẫn tới hang Nho. Ngay cả khách không chơi trò mạo hiểm cũng có thể mua vé đi bộ qua cầu để ngắm cảnh và chụp ảnh. Kết hợp thiên nhiên hùng vĩ với trải nghiệm vượt giới hạn bản thân, Skypark đã trở thành một biểu tượng du lịch hiện đại của vùng Sochi.",
    "highlights_vi": [
        "Cầu treo đi bộ SkyBridge dài 439 m, treo ở độ cao khoảng 207 m trên hẻm núi Mzymta — khi khánh thành năm 2014 thuộc hàng cầu treo đi bộ dài nhất thế giới.",
        "Loạt trò mạo hiểm: bungee Bungy 207 và Bungy 69, đu khổng lồ SochiSwing, trượt dây MegaTroll tới 120 km/h, công viên dây 'Mowgli' và tuyến Via Ferrata.",
        "Nằm trong Vườn quốc gia Sochi, trên đường lên Krasnaya Polyana; từ cầu nhìn được cả dãy Kavkaz lẫn Biển Đen.",
    ],
    "practical": {
        "hours_vi": "Mở cửa hằng ngày (giờ phổ biến khoảng 10:00–18:30, có thể thay đổi theo mùa); nên kiểm tra trang chính thức trước khi đi.",
        "ticket_vi": "Có vé vào cổng để đi bộ qua cầu và ngắm cảnh; các trò mạo hiểm (bungee, đu, trượt dây) tính phí riêng theo từng hoạt động.",
        "duration_vi": "Khoảng 1,5–3 giờ tuỳ số hoạt động tham gia.",
        "best_time_vi": "Từ mùa xuân đến mùa thu thời tiết đẹp; buổi sáng ít đông và ánh sáng thuận để chụp hẻm núi.",
        "tips_vi": "Từ Adler đi ô tô khoảng 30–40 phút; mang giày bám tốt và giấy tờ tuỳ thân; cân nhắc sức khoẻ trước khi chơi trò cảm giác mạnh.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(43.52531, 39.99736),
    "official_site": "https://skypark.ru",
    "sources": [
        {"title": "Sochi Skybridge — HighestBridges.com", "url": "https://www.highestbridges.com/wiki/index.php?title=Sochi_Skybridge"},
        {"title": "Skypark Sochi — Discover Russia", "url": "https://discoverrussia.travel/things-to-do/skypark-sochi"},
        {"title": "AJ Hackett Sochi (trang chính thức)", "url": "https://www.ajhackett.com/sochi/"},
    ],
    "tags": ["bridge", "outdoor", "adventure", "viewpoint", "modern", "top"],
    "status": "enriched",
    "last_updated": TODAY,
}


PLAN = {
    "moscow": [MUSEUM_OF_MOSCOW],
    "saint-petersburg": [ANICHKOV_PALACE],
    "krasnodar": [SKYPARK_SOCHI],
}


def main():
    total_added = 0
    for region, recs in PLAN.items():
        path = os.path.join(REGIONS, f"{region}.json")
        arr = json.load(open(path, encoding="utf-8"))
        have_slug = {p.get("slug") for p in arr}
        have_id = {p.get("id") for p in arr}
        # sao lưu trước khi ghi
        bak = f"{path}.bak_add_{STAMP}"
        json.dump(arr, open(bak, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        added_here = []
        for r in recs:
            if r["slug"] in have_slug or r["id"] in have_id:
                print(f"  = {region}: bo qua (da co) {r['slug']}")
                continue
            arr.append(r)
            added_here.append(r["slug"])
            total_added += 1
        json.dump(arr, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"  + {region}: them {len(added_here)} -> {added_here} | tong dia diem vung: {len(arr)} | backup: {os.path.basename(bak)}")
    print(f"TONG CONG THEM MOI: {total_added}")


if __name__ == "__main__":
    main()
