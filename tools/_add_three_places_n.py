# -*- coding: utf-8 -*-
"""_add_three_places_n.py — Bổ sung 3 địa điểm nổi tiếng còn thiếu (Moscow x1, SPB x2).
Nội dung tiếng Việt nguyên gốc, tọa độ thật, ghi nguồn. Chạy: python3 tools/_add_three_places_n.py"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"

NEW = [
    {
        "id": "moscow-immaculate-conception-cathedral",
        "slug": "immaculate-conception-cathedral",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Nhà thờ Đức Mẹ Vô Nhiễm Nguyên Tội (Công giáo)",
        "name_ru": "Собор Непорочного Зачатия Пресвятой Девы Марии",
        "name_en": "Cathedral of the Immaculate Conception of the Blessed Virgin Mary",
        "categories": ["church"],
        "coordinates": {"lat": 55.76722, "lon": 37.57111},
        "address_vi": "Phố Malaya Gruzinskaya 27/13 (ul. Malaya Gruzinskaya, 27/13), Moskva",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Nhiều du khách bất ngờ khi bắt gặp một thánh đường Tân Gothic bề thế ngay giữa Moskva, khen không gian trang nghiêm, mát lành và đặc biệt là các buổi hoà nhạc đại phong cầm giàu cảm xúc; một số lưu ý nhà thờ nằm hơi xa trung tâm và nên canh đúng giờ mở cửa hoặc lịch biểu diễn.",
        "presentation_short_vi": "Thánh đường Công giáo La Mã lớn nhất nước Nga — khối kiến trúc Tân Gothic bằng gạch đỏ với những tháp nhọn vươn cao, nổi tiếng với các buổi hoà nhạc đại phong cầm (organ) vang vọng dưới vòm mái.",
        "presentation_long_vi": "Cách Quảng trường Đỏ không xa, một nhà thờ Tân Gothic bằng gạch đỏ với những tháp nhọn vươn thẳng lên trời khiến nhiều du khách sững sờ, bởi nó gợi nhớ các thánh đường Tây Âu hơn là nước Nga Chính thống giáo. Đây là Nhà thờ Đức Mẹ Vô Nhiễm Nguyên Tội, thánh đường Công giáo La Mã lớn nhất nước Nga. Công trình khởi công năm 1901 và hoàn thành năm 1911, phục vụ cộng đồng Công giáo đông đảo gốc Ba Lan sinh sống quanh phố Malaya Gruzinskaya thời bấy giờ; mặt tiền lấy cảm hứng từ kiến trúc Gothic của Anh, còn phần chóp gợi liên tưởng tới thánh đường Milano. Số phận nhà thờ đầy thăng trầm: dưới thời Xô Viết, nó bị đóng cửa vào thập niên 1930, bị trưng dụng làm ký túc xá rồi nhà kho, nội thất nguyên bản gần như bị phá huỷ. Phải đến sau khi Liên Xô tan rã, nhà thờ mới được trả lại cho Giáo hội và trùng tu quy mô lớn, rồi được cung hiến lại năm 1999. Ngày nay, ngoài vai trò một giáo đường đang hoạt động, nơi đây còn nổi tiếng với cây đại phong cầm cỡ lớn cùng những buổi hoà nhạc organ và nhạc thính phòng thường kỳ, âm thanh trầm hùng lấp đầy không gian vòm cao, biến đây thành một điểm hẹn âm nhạc độc đáo của thủ đô.",
        "highlights_vi": [
            "Thánh đường Công giáo La Mã lớn nhất nước Nga; kiến trúc Tân Gothic gạch đỏ, khởi công 1901 và hoàn thành 1911.",
            "Thời Xô Viết bị đóng cửa, dùng làm ký túc xá và nhà kho; được trả lại cho Giáo hội và cung hiến lại năm 1999.",
            "Nổi tiếng với cây đại phong cầm lớn và các buổi hoà nhạc organ, nhạc thính phòng vang vọng dưới vòm mái."
        ],
        "practical": {
            "hours_vi": "Mở cửa hằng ngày theo giờ lễ (thường từ sáng sớm đến tối); giờ giấc có thể thay đổi theo lịch phụng vụ.",
            "ticket_vi": "Vào viếng miễn phí; các buổi hoà nhạc organ bán vé riêng.",
            "duration_vi": "30–45 phút (lâu hơn nếu dự hoà nhạc).",
            "best_time_vi": "Buổi tối có hoà nhạc organ; nên kiểm tra lịch trên trang của giáo xứ.",
            "tips_vi": "Gần ga metro Ulitsa 1905 Goda; là giáo đường đang hoạt động nên ăn mặc kín đáo và giữ yên lặng trong giờ lễ."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=37.57111,55.76722&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.76722,37.57111"
        },
        "official_site": None,
        "sources": [
            {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Cathedral_of_the_Immaculate_Conception_(Moscow)"}
        ],
        "tags": ["church", "architecture", "concert", "indoor", "landmark", "catholic"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-arctic-antarctic-museum",
        "slug": "arctic-antarctic-museum",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Bảo tàng Bắc Cực và Nam Cực Nga",
        "name_ru": "Российский государственный музей Арктики и Антарктики",
        "name_en": "Russian State Museum of the Arctic and Antarctic",
        "categories": ["museum"],
        "coordinates": {"lat": 59.927506, "lon": 30.353594},
        "address_vi": "Phố Marata 24a (ul. Marata, 24a), Saint Petersburg",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Khách tham quan thích chủ đề vùng cực độc đáo và không khí hoài cổ kiểu Xô Viết của các diorama, ấn tượng với khu trưng bày trạm trôi ‘Bắc Cực-1’ và với chính toà nhà nhà thờ cũ; một số nhận xét cách trưng bày hơi cũ và chủ yếu chú thích bằng tiếng Nga, nhưng nhìn chung đây là điểm đến lạ, hợp cho gia đình và người mê lịch sử khám phá.",
        "presentation_short_vi": "Bảo tàng lớn nhất thế giới về vùng cực, đặt trong một nhà thờ Cổ lễ mang phong cách Tân cổ điển; trưng bày hành trình chinh phục Bắc Cực và Nam Cực của nước Nga, nổi bật là trạm trôi ‘Bắc Cực-1’.",
        "presentation_long_vi": "Bên trong một toà nhà mái vòm bề thế trên phố Marata, vốn là nhà thờ Thánh Nikolai của phái Cổ lễ (Edinoverie) xây theo phong cách Tân cổ điển hồi đầu thế kỷ 19, là bảo tàng lớn nhất thế giới dành riêng cho hai vùng cực của Trái Đất. Thành lập năm 1930 và mở cửa đón khách năm 1937, Bảo tàng Bắc Cực và Nam Cực kể lại thiên anh hùng ca chinh phục băng giá của nước Nga: từ các đoàn thám hiểm tuyến đường biển phương Bắc, đội tàu phá băng, ngành hàng không vùng cực, cho tới công cuộc nghiên cứu Nam Cực thời Xô Viết. Hiện vật ngôi sao là mô hình và di vật của trạm nghiên cứu trôi trên băng ‘Bắc Cực-1’ (Severny Polyus-1) năm 1937 do Ivan Papanin dẫn đầu, khi bốn nhà khoa học sống nhiều tháng trên một tảng băng trôi giữa Bắc Băng Dương. Du khách còn được chiêm ngưỡng những mô hình tàu phá băng, chiếc máy bay thám hiểm treo lơ lửng, tấm bản đồ nổi khổng lồ và các diorama tái hiện cực quang, gấu trắng cùng cảnh quan băng tuyết. Không quá hào nhoáng nhưng đầy chất hoài niệm, bảo tàng là điểm đến thú vị cho những ai mê khám phá, lịch sử khoa học và các câu chuyện phiêu lưu nơi tận cùng thế giới.",
        "highlights_vi": [
            "Bảo tàng lớn nhất thế giới về vùng cực; thành lập năm 1930, mở cửa đón khách năm 1937.",
            "Đặt trong nhà thờ Thánh Nikolai phái Cổ lễ, công trình Tân cổ điển đầu thế kỷ 19 (thiết kế của kiến trúc sư A. Melnikov).",
            "Hiện vật nổi bật: trạm trôi ‘Bắc Cực-1’ (1937) của đoàn Papanin, cùng mô hình tàu phá băng và các diorama cực quang."
        ],
        "practical": {
            "hours_vi": "10:00–18:00; đóng cửa thứ Hai (và cả thứ Ba vào mùa hè 1/6–31/8) cùng thứ Sáu cuối tháng.",
            "ticket_vi": "Bán vé tại chỗ, giá phải chăng (khoảng vài trăm rúp); xem giá cập nhật trên trang chính thức.",
            "duration_vi": "1–1,5 giờ.",
            "best_time_vi": "Buổi sáng các ngày trong tuần để tránh đông; phù hợp đi cùng trẻ em.",
            "tips_vi": "Gần ga metro Vladimirskaya/Dostoevskaya; phần lớn chú thích bằng tiếng Nga, nên chuẩn bị app dịch hoặc thuê thuyết minh."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.353594,59.927506&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.927506,30.353594"
        },
        "official_site": "https://www.polarmuseum.ru",
        "sources": [
            {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Arctic_and_Antarctic_Museum"}
        ],
        "tags": ["museum", "indoor", "science", "history", "family"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-kshesinskaya-mansion",
        "slug": "kshesinskaya-mansion",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Dinh thự Kshesinskaya (Bảo tàng Lịch sử Chính trị Nga)",
        "name_ru": "Особняк Кшесинской (Музей политической истории России)",
        "name_en": "Kshesinskaya Mansion (Museum of the Political History of Russia)",
        "categories": ["museum"],
        "coordinates": {"lat": 59.95417, "lon": 30.32694},
        "address_vi": "Phố Kuybysheva 2-4 (ul. Kuybysheva, 2-4), Saint Petersburg",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Du khách đánh giá cao vẻ đẹp nội thất Art Nouveau và giá trị lịch sử đặc biệt của toà nhà, thấy phần trưng bày công phu, nhiều tư liệu và khá cân bằng khi kể về thời Xô Viết; một số cho biết chú thích tiếng Anh còn hạn chế nên thuê thuyết minh hoặc dùng app sẽ giúp hiểu sâu hơn.",
        "presentation_short_vi": "Dinh thự Art Nouveau tuyệt đẹp của nữ nghệ sĩ ballet Matilda Kshesinskaya — nơi năm 1917 trở thành đại bản doanh của phe Bolshevik và Lenin diễn thuyết từ ban công; nay là Bảo tàng Lịch sử Chính trị Nga.",
        "presentation_long_vi": "Toà dinh thự duyên dáng bên rìa Quảng trường Ba Ngôi (Troitskaya) là một trong những công trình Art Nouveau (phong cách Modern phương Bắc) đẹp nhất Saint Petersburg. Do kiến trúc sư Alexander von Gogen thiết kế và hoàn thành năm 1906, dinh thự được xây cho Matilda Kshesinskaya, ngôi sao ballet của Nhà hát Mariinsky và là người từng gắn với Hoàng thái tử Nikolai, tức Sa hoàng Nikolai II sau này. Bố cục bất đối xứng, cửa sổ đủ kích cỡ, mặt tường phối granit, gạch, gốm majolica và kim loại trang trí đã tạo nên một kiệt tác thanh lịch, tân tiến so với thời đại. Nhưng dinh thự nổi tiếng không chỉ vì cái đẹp: sau Cách mạng Tháng Hai 1917, phe Bolshevik chiếm toà nhà làm tổng hành dinh, và Lenin nhiều lần diễn thuyết trước đám đông từ ban công sau khi trở về Petrograd. Từ năm 1955, nơi đây trở thành bảo tàng, ngày nay là Bảo tàng Lịch sử Chính trị Nga, trải rộng trên hai dinh thự Art Nouveau liền kề được nối với nhau bằng một sảnh trưng bày hiện đại. Các gian phòng nghi lễ được phục dựng lộng lẫy, còn phần trưng bày dẫn dắt người xem qua hơn hai thế kỷ biến động chính trị Nga, từ đế chế, cách mạng, thời Xô Viết cho tới nước Nga đương đại, nhìn nhận cả những mảng tối như đàn áp và trại cải tạo.",
        "highlights_vi": [
            "Kiệt tác Art Nouveau (Modern phương Bắc) do Alexander von Gogen thiết kế, hoàn thành năm 1906 cho nữ nghệ sĩ ballet Matilda Kshesinskaya.",
            "Năm 1917 là đại bản doanh của phe Bolshevik; Lenin từng diễn thuyết trước đám đông từ ban công dinh thự.",
            "Từ năm 1955 là bảo tàng, nay là Bảo tàng Lịch sử Chính trị Nga trải trên hai dinh thự liền kề."
        ],
        "practical": {
            "hours_vi": "Thường 10:00–18:00 (một số ngày mở muộn hơn); đóng cửa một ngày trong tuần — nên xem lịch trên trang chính thức.",
            "ticket_vi": "Bán vé tại chỗ, giá phải chăng; có ưu đãi cho học sinh, sinh viên.",
            "duration_vi": "1,5–2 giờ.",
            "best_time_vi": "Kết hợp cùng chuyến thăm Pháo đài Petro-Pavlovsk ở gần đó.",
            "tips_vi": "Gần ga metro Gorkovskaya; đừng bỏ lỡ ban công lịch sử và các gian phòng nghi lễ được phục dựng."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.32694,59.95417&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.95417,30.32694"
        },
        "official_site": None,
        "sources": [
            {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Museum_of_Political_History_of_Russia"}
        ],
        "tags": ["museum", "architecture", "history", "indoor", "landmark"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    }
]


def main():
    added, skipped = [], []
    by_region = {}
    for r in NEW:
        by_region.setdefault(r["region"], []).append(r)

    for region, recs in by_region.items():
        path = os.path.join(REGIONS, f"{region}.json")
        data = json.load(open(path, encoding="utf-8"))
        have = {p.get("slug") for p in data}
        bak = f"{path}.bak_add_{STAMP}"
        with open(bak, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        changed = False
        for r in recs:
            if r["slug"] in have:
                skipped.append(f"{region}/{r['slug']}")
                continue
            data.append(r)
            added.append(f"{region}/{r['slug']}")
            changed = True
        if changed:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"[OK] {region}.json -> {len(data)} ban ghi (backup: {os.path.basename(bak)})")
        else:
            os.remove(bak)

    print("DA THEM:", added or "(khong co)")
    print("BO QUA (da ton tai):", skipped or "(khong)")


if __name__ == "__main__":
    main()
