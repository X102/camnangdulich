# -*- coding: utf-8 -*-
"""Sửa toạ độ Nhà hát lớn Hải Phòng (đang lệch) + thêm Ga Hải Phòng.
Toạ độ lấy từ OpenStreetMap. Chèn an toàn: bỏ qua nếu slug đã có. maps để trống (retrofit sẽ sinh).
"""
import json, os

F = "data/regions/vn-hai-phong.json"
REGION = "vn-hai-phong"
REGION_NAME_VI = "Hải Phòng"
FD = "Miền Bắc"

d = json.load(open(F, encoding="utf-8"))

# 1) Sửa toạ độ Nhà hát lớn Hải Phòng (OSM way 242055606: 20.857498, 106.681824)
for p in d:
    if p["slug"] == "nha-hat-lon-hai-phong":
        p["coordinates"] = {"lat": 20.8575, "lon": 106.6818}
        if not p.get("photo"):
            p["photo"] = "https://commons.wikimedia.org/wiki/Special:FilePath/03-OPERA_HOUSE.jpg"
            p["photo_credit"] = "HoangTuanAnh, CC BY-SA 3.0 (Wikimedia Commons)"
        p["maps"] = {}  # buộc retrofit sinh lại theo toạ độ đúng
        p["last_updated"] = "2026-07-28"
        print("Đã sửa toạ độ Nhà hát lớn ->", p["coordinates"])

# 2) Thêm Ga Hải Phòng (OSM way 241081956: 20.855961, 106.687365)
ga = {
    "id": f"{REGION}-ga-hai-phong",
    "slug": "ga-hai-phong",
    "region": REGION,
    "country": "vietnam",
    "region_name_vi": REGION_NAME_VI,
    "federal_district": FD,
    "name_vi": "Ga Hải Phòng",
    "name_ru": "Железнодорожный вокзал Хайфона",
    "name_en": "Hai Phong Railway Station",
    "categories": ["other", "monument"],
    "coordinates": {"lat": 20.8560, "lon": 106.6874},
    "address_vi": "75 Lương Khánh Thiện, phường Cầu Đất, quận Ngô Quyền, thành phố Hải Phòng",
    "rating": {"value": 4.5, "count": 1600, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách yêu thích kiến trúc Pháp cổ màu vàng đặc trưng và bầu không khí hoài niệm của nhà ga trăm tuổi; nhiều người ghé chụp ảnh, ngắm đoàn tàu và tản bộ khu phố xung quanh. Một số lưu ý nên tránh giờ tàu đông và giữ an toàn khi chụp gần đường ray.",
    "presentation_short_vi": "Ga Hải Phòng là nhà ga xe lửa cổ kính khánh thành năm 1902, điểm cuối của tuyến đường sắt Hà Nội – Hải Phòng. Với kiến trúc Pháp màu vàng thanh lịch, đây là một trong những nhà ga đẹp và giàu hoài niệm nhất Việt Nam.",
    "presentation_short_en": "Hai Phong Railway Station, opened in 1902, is the terminus of the Hanoi–Hai Phong line. With its elegant yellow French architecture, it is one of Vietnam's most beautiful and nostalgic railway stations.",
    "presentation_short_ru": "Железнодорожный вокзал Хайфона, открытый в 1902 году, — конечная станция линии Ханой–Хайфон. Со своей изящной жёлтой французской архитектурой это один из красивейших и самых ностальгических вокзалов Вьетнама.",
    "presentation_long_vi": "Toạ lạc ngay trung tâm thành phố, Ga Hải Phòng là một trong những nhà ga xe lửa lâu đời và đẹp nhất Việt Nam, được người Pháp xây dựng và đưa vào hoạt động từ năm 1902. Đây là điểm cuối của tuyến đường sắt Hà Nội – Hải Phòng, đồng thời từng là một mắt xích của tuyến đường sắt khổ hẹp nối tới tận Vân Nam (Trung Quốc). Nhà ga khoác lên mình lối kiến trúc Pháp cổ điển với gam vàng đặc trưng, mái ngói, những ô cửa vòm và hàng chữ 'GA HẢI PHÒNG' nổi bật phía trước, gợi lại không khí của một thời đã xa. Trải qua hơn một thế kỷ, ga vẫn hoạt động đều đặn, mỗi ngày đón tiễn những chuyến tàu chở khách xuôi ngược giữa Hải Phòng và thủ đô. Với nhiều du khách, đi tàu hoả từ Hà Nội xuống Hải Phòng rồi bước xuống sân ga cổ kính này là một trải nghiệm du lịch đầy chất thơ và hoài niệm. Khu vực quanh ga cũng nhộn nhịp với hàng quán, phố phường mang dấu ấn đô thị cảng lâu đời. Không chỉ là đầu mối giao thông, Ga Hải Phòng còn là một biểu tượng kiến trúc – lịch sử của thành phố Hoa phượng đỏ, là nơi lý tưởng để chụp ảnh, tìm hiểu lịch sử đường sắt và cảm nhận nhịp sống đặc trưng của người dân đất Cảng.",
    "presentation_long_en": "In the very heart of the city, Hai Phong Railway Station is one of the oldest and most beautiful train stations in Vietnam, built by the French and opened in 1902. It is the terminus of the Hanoi–Hai Phong line and was once a link in the narrow-gauge railway that ran all the way to Yunnan in China. The station wears classic French architecture in its signature yellow, with a tiled roof, arched windows and the bold letters 'GA HAI PHONG' across its face, evoking the atmosphere of a bygone era. After more than a century it still works steadily, each day seeing off and welcoming passenger trains that run between Hai Phong and the capital. For many travellers, taking the train down from Hanoi and stepping onto this old platform is a poetic, nostalgic experience. The area around the station also bustles with shops and streets that carry the imprint of a long-established port city. More than a transport hub, Hai Phong Railway Station is an architectural and historical symbol of the City of the Red Flamboyant, an ideal place to take photographs, learn about railway history and feel the distinctive rhythm of the port city's people.",
    "presentation_long_ru": "В самом сердце города железнодорожный вокзал Хайфона — один из старейших и красивейших вокзалов Вьетнама, построенный французами и открытый в 1902 году. Это конечная станция линии Ханой–Хайфон, а некогда и звено узкоколейной железной дороги, тянувшейся вплоть до Юньнани в Китае. Вокзал одет в классическую французскую архитектуру своего фирменного жёлтого цвета, с черепичной крышей, арочными окнами и крупной надписью «GA HAI PHONG» на фасаде, воскрешая атмосферу ушедшей эпохи. Спустя более чем столетие он по-прежнему исправно работает, ежедневно провожая и встречая пассажирские поезда между Хайфоном и столицей. Для многих путешественников поездка на поезде из Ханоя и выход на этот старый перрон — поэтичное, ностальгическое переживание. Район вокруг вокзала тоже оживлён лавками и улицами, хранящими отпечаток давнего портового города. Больше чем транспортный узел, вокзал Хайфона — архитектурный и исторический символ Города красных огненных деревьев, идеальное место, чтобы фотографировать, знакомиться с историей железных дорог и ощущать особый ритм жизни жителей портового города.",
    "highlights_vi": [
        "Nhà ga khánh thành năm 1902, điểm cuối tuyến đường sắt Hà Nội – Hải Phòng",
        "Kiến trúc Pháp cổ điển màu vàng đặc trưng, biểu tượng của đất Cảng",
        "Điểm chụp ảnh, du lịch hoài niệm ngay trung tâm thành phố",
    ],
    "highlights_en": [
        "A station opened in 1902, terminus of the Hanoi–Hai Phong line",
        "Classic French architecture in signature yellow, a symbol of the port city",
        "A photo and nostalgic-travel spot right in the city centre",
    ],
    "highlights_ru": [
        "Вокзал, открытый в 1902 году, конечная линии Ханой–Хайфон",
        "Классическая французская архитектура в фирменном жёлтом, символ порта",
        "Место для фото и ностальгических путешествий в центре города",
    ],
    "practical": {
        "hours_vi": "Mở cửa theo lịch tàu chạy hằng ngày; ban ngày dễ tham quan, chụp ảnh bên ngoài.",
        "ticket_vi": "Vào khu vực ga không mất phí; vé tàu Hà Nội – Hải Phòng tham khảo khoảng 70.000–120.000 VND/lượt.",
        "duration_vi": "Khoảng 30–45 phút tham quan, chụp ảnh.",
        "best_time_vi": "Sáng sớm hoặc chiều muộn ánh sáng đẹp; tránh giờ cao điểm tàu đông.",
        "tips_vi": "Giữ an toàn, không đứng chụp ảnh trên/gần đường ray khi có tàu; kết hợp tản bộ khu phố Pháp và Nhà hát lớn gần đó.",
    },
    "photo": "https://commons.wikimedia.org/wiki/Special:FilePath/Ga_Hai_Phong.JPG",
    "photo_credit": "Wikimedia Commons, CC BY-SA 3.0",
    "maps": {},
    "official_site": None,
    "sources": [
        {"title": "Hải Phòng station (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Haiphong_station"},
        {"title": "Ga Hải Phòng — OpenStreetMap (way 241081956)", "url": "https://www.openstreetmap.org/way/241081956"},
    ],
    "tags": ["historic", "railway", "photo", "architecture", "city", "family"],
    "status": "enriched",
    "last_updated": "2026-07-28",
}

have = {p["slug"] for p in d}
if ga["slug"] not in have:
    d.append(ga)
    print("Đã thêm Ga Hải Phòng.")
else:
    print("Ga Hải Phòng đã tồn tại, bỏ qua.")

json.dump(d, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Tổng Hải Phòng:", len(d))
