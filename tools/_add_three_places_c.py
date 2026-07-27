# -*- coding: utf-8 -*-
"""Bổ sung 3 địa điểm còn thiếu vào cơ sở dữ liệu Cẩm nang Du lịch Nga.
Tạo backup trước khi ghi, kiểm tra trùng slug/id. Chạy: python3 tools/_add_three_places_c.py"""
import json, os, shutil, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-25"


def maps_for(lat, lon):
    return {
        "yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=16&l=map",
        "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
    }


def null_rating():
    return {"value": None, "count": None, "source": None, "as_of": None}


RECORDS = {
    "moscow": [
        {
            "id": "moscow-northern-river-terminal",
            "slug": "northern-river-terminal",
            "region": "moscow",
            "region_name_vi": "Moskva",
            "federal_district": "Thành phố trực thuộc liên bang",
            "name_vi": "Ga đường sông phía Bắc (Severny Rechnoy Vokzal)",
            "name_ru": "Северный речной вокзал",
            "name_en": "Northern River Terminal",
            "categories": ["monument", "park_garden"],
            "coordinates": {"lat": 55.85109, "lon": 37.46693},
            "address_vi": "Đại lộ Leningradskoe (Leningradskoe shosse) 51, Moskva",
            "rating": null_rating(),
            "review_summary_vi": "Du khách yêu thích không gian ven hồ rộng thoáng và toà nhà lịch sử được phục dựng tinh tế, xem đây là điểm dạo chơi, chụp ảnh và lên tàu du ngoạn lý tưởng ở phía bắc Moskva.",
            "presentation_short_vi": "Toà nhà 'cảng của năm biển' bên hồ Khimki — công trình theo phong cách Đế chế Stalin năm 1937 với ngọn tháp gắn sao, vừa được trùng tu và mở cửa lại năm 2020 thành một trong những không gian dạo chơi ven sông đẹp nhất Moskva.",
            "presentation_long_vi": "Khánh thành năm 1937 bên bờ hồ chứa Khimki mới đào, Ga đường sông phía Bắc từng được ví là 'cảng của năm biển' — bởi qua hệ thống kênh đào, tàu bè từ đây có thể ra tới cả năm vùng biển: Baltic, Trắng, Azov, Đen và Caspi. Do các kiến trúc sư Alexei Rukhlyadev và Vladimir Krinsky thiết kế theo phong cách Đế chế Stalin, toà nhà trải dài như một con tàu, ở giữa vươn lên ngọn tháp cao khoảng 75 m gắn ngôi sao năm cánh; nơi đây cũng là bối cảnh của nhiều bộ phim Liên Xô kinh điển như 'Volga-Volga'. Sau nhiều năm xuống cấp, cả toà nhà lẫn công viên bị đóng cửa năm 2009; công cuộc trùng tu quy mô lớn diễn ra từ 2018 và hoàn tất đúng dịp Ngày thành phố năm 2020. Kiến trúc lịch sử được giữ gìn tối đa, trong khi hạ tầng được làm mới hoàn toàn. Ngày nay, du khách tới đây để dạo bước trong công viên rộng rãi hai bên, ngắm những đài phun nước, thuê xe đạp, thưởng thức ẩm thực ở nhà hàng 'Volga-Volga' trong toà nhà, hay lên tàu du ngoạn dọc kênh Moskva. Vào buổi tối, ngọn tháp và mặt tiền lên đèn soi bóng xuống mặt nước, tạo nên khung cảnh nên thơ. Ga nằm ngay cạnh ga tàu điện ngầm cùng tên Rechnoy Vokzal, rất dễ tiếp cận.",
            "highlights_vi": [
                "Được gọi là 'cảng của năm biển' vì qua hệ thống kênh đào, tàu từ đây ra được biển Baltic, Biển Trắng, Azov, Biển Đen và Caspi.",
                "Đóng cửa năm 2009, trùng tu quy mô lớn giai đoạn 2018–2020 và mở lại đúng Ngày thành phố Moskva.",
                "Ngọn tháp cao khoảng 75 m gắn sao là bối cảnh của bộ phim Liên Xô kinh điển 'Volga-Volga'.",
            ],
            "practical": {
                "hours_vi": "Công viên mở cửa hằng ngày (không gian công cộng ngoài trời); nhà ga và nhà hàng theo giờ riêng.",
                "ticket_vi": "Vào công viên miễn phí; tour du thuyền và một số dịch vụ tính phí riêng.",
                "duration_vi": "1–2 giờ.",
                "best_time_vi": "Chiều muộn tới tối mùa hè, khi công viên và toà nhà lên đèn.",
                "tips_vi": "Đi tàu điện ngầm tới ga Rechnoy Vokzal; kết hợp du ngoạn bằng tàu trên kênh Moskva; thử nhà hàng Volga-Volga trong ga.",
            },
            "photo": None,
            "photo_credit": None,
            "maps": maps_for(55.85109, 37.46693),
            "official_site": None,
            "sources": [
                {"title": "Wikipedia (EN) — North River Terminal", "url": "https://en.wikipedia.org/wiki/North_River_Terminal"},
                {"title": "The Moscow Times — North River Terminal Opens After More Than a Decade (2020)", "url": "https://www.themoscowtimes.com/2020/09/11/north-river-terminal-opens-in-moscow-after-more-than-a-decade-a71374"},
            ],
            "tags": ["modern", "landmark", "park", "architecture", "riverside", "outdoor"],
            "status": "enriched",
            "last_updated": TODAY,
        }
    ],
    "saint-petersburg": [
        {
            "id": "saint-petersburg-tauride-garden-palace",
            "slug": "tauride-garden-palace",
            "region": "saint-petersburg",
            "region_name_vi": "Saint Petersburg",
            "federal_district": "Thành phố trực thuộc liên bang",
            "name_vi": "Vườn và Cung điện Tauride (Tavrichesky sad, Ta-vrit-xki)",
            "name_ru": "Таврический сад и дворец",
            "name_en": "Tauride Garden and Palace",
            "categories": ["park_garden", "palace"],
            "coordinates": {"lat": 59.9481, "lon": 30.3736},
            "address_vi": "Phố Shpalernaya 47 (lối vào vườn từ phố Kirochnaya / Potemkinskaya), Quận Trung tâm, Saint Petersburg",
            "rating": null_rating(),
            "review_summary_vi": "Du khách và người dân địa phương yêu mến khu vườn yên tĩnh với hồ nước, thảm cỏ rộng và bầu không khí thư thái ngay giữa trung tâm; nhiều người tiếc là cung điện lịch sử phía trước hiếm khi mở cửa cho khách tham quan tự do.",
            "presentation_short_vi": "Cung điện tân cổ điển lớn nhất nước Nga thế kỷ 18, do Nữ hoàng Ekaterina II ban tặng Công tước Potemkin, cùng khu vườn cảnh kiểu Anh phía sau — nơi khai sinh nghị viện Nga đầu tiên và một công viên công cộng được yêu thích.",
            "presentation_long_vi": "Cung điện Tauride được kiến trúc sư Ivan Starov xây dựng trong các năm 1783–1789 làm dinh thự tại kinh đô cho Công tước Grigory Potemkin — vị sủng thần của Nữ hoàng Ekaterina II, người mang tước hiệu 'Công tước xứ Tauride' sau khi bán đảo Crimea (Tavrida) được sáp nhập vào Đế quốc Nga. Với mặt tiền Palladio giản dị nhưng nội thất lộng lẫy và đại sảnh có hàng cột bề thế, đây được xem là dinh thự quý tộc lớn và sang trọng bậc nhất nước Nga thời bấy giờ, trở thành hình mẫu cho vô số điền trang khắp đế quốc. Phía sau cung điện là Vườn Tauride — một trong những khu vườn cảnh kiểu Anh đầu tiên ở Nga, do người làm vườn William Guld quy hoạch với hồ nước uốn lượn, gò đồi, cầu nhỏ và nhà kính trồng cây. Năm 1866, khu vườn mở cửa cho công chúng và trở thành công viên thành phố. Cung điện in đậm những dấu mốc lịch sử trọng đại: năm 1906 nơi đây đặt trụ sở Đuma Quốc gia — nghị viện đầu tiên của Nga; sau Cách mạng Tháng Hai 1917, cả Chính phủ Lâm thời lẫn Xô viết Petrograd cùng hoạt động trong hai cánh của toà nhà. Ngày nay cung điện là trụ sở Hội đồng Liên Nghị viện các nước SNG (thường không mở tham quan tự do), còn khu vườn vẫn là nơi dạo chơi, trượt băng mùa đông và thư giãn được người dân yêu thích.",
            "highlights_vi": [
                "Từng là cung điện tân cổ điển lớn nhất nước Nga thế kỷ 18, hình mẫu cho nhiều điền trang khắp đế quốc.",
                "Năm 1906 trở thành trụ sở Đuma Quốc gia — nghị viện đầu tiên của Nga; năm 1917 là sân khấu của cách mạng.",
                "Vườn phía sau là một trong những vườn cảnh kiểu Anh đầu tiên ở Nga, mở cho công chúng từ năm 1866.",
            ],
            "practical": {
                "hours_vi": "Vườn mở cửa hằng ngày (giờ thay đổi theo mùa). Cung điện là cơ quan Liên Nghị viện SNG, thường không mở tham quan tự do.",
                "ticket_vi": "Vào vườn miễn phí.",
                "duration_vi": "1–1,5 giờ.",
                "best_time_vi": "Mùa hè cây xanh mát; mùa đông có sân trượt băng.",
                "tips_vi": "Kết hợp thăm Nhà thờ Smolny gần đó; ngắm cung điện từ phía phố Shpalernaya, dạo vườn từ lối phố Kirochnaya hoặc Potemkinskaya.",
            },
            "photo": None,
            "photo_credit": None,
            "maps": maps_for(59.9481, 30.3736),
            "official_site": None,
            "sources": [
                {"title": "Wikipedia (EN) — Tauride Palace", "url": "https://en.wikipedia.org/wiki/Tauride_Palace"},
                {"title": "Wikipedia (EN) — Tauride Garden", "url": "https://en.wikipedia.org/wiki/Tauride_Garden"},
            ],
            "tags": ["park", "palace", "free", "outdoor", "family", "history"],
            "status": "enriched",
            "last_updated": TODAY,
        }
    ],
    "tatarstan": [
        {
            "id": "tatarstan-palace-of-farmers",
            "slug": "palace-of-farmers",
            "region": "tatarstan",
            "region_name_vi": "Cộng hoà Tatarstan",
            "federal_district": "Vùng Volga",
            "name_vi": "Cung điện Nông dân (Dvorets Zemledeltsev, Đvô-rét Dem-lê-đen-txép)",
            "name_ru": "Дворец земледельцев",
            "name_en": "Palace of Farmers (Agricultural Palace)",
            "categories": ["palace", "monument"],
            "coordinates": {"lat": 55.8006, "lon": 49.1122},
            "address_vi": "Quảng trường Cung điện (Dvortsovaya ploshchad), phố Fedoseevskaya 36, gần Điện Kremlin Kazan",
            "rating": null_rating(),
            "review_summary_vi": "Nhiều du khách trầm trồ trước quy mô tráng lệ và 'Cây Đời' lấp lánh về đêm, xem đây là điểm chụp ảnh không thể bỏ qua ở Kazan; một số ý kiến cho rằng phong cách toà nhà hơi phô trương và có phần lạc lõng bên cạnh Kremlin cổ.",
            "presentation_short_vi": "Toà nhà Bộ Nông nghiệp Tatarstan (2010) cạnh Điện Kremlin Kazan — công trình tân cổ điển hoành tráng với mái vòm cao 48 m và 'Cây Đời' bằng đồng cao 20 m rực sáng về đêm, một trong những biểu tượng hiện đại được chụp ảnh nhiều nhất thành phố.",
            "presentation_long_vi": "Hoàn thành năm 2010 sau hai năm xây dựng, Cung điện Nông dân là trụ sở Bộ Nông nghiệp và Lương thực Cộng hoà Tatarstan, toạ lạc trên Quảng trường Cung điện ngay sát bức tường phía bắc của Điện Kremlin Kazan và bờ kè sông Kazanka. Do kiến trúc sư Leonid Gornik cùng hãng 'Antika-Plus' thiết kế, toà nhà gây choáng ngợp bởi vẻ hoành tráng tân cổ điển: hai cánh đối xứng, khối trung tâm vươn lên mái vòm cao tới 48 m, gợi liên tưởng tới Petit Palais ở Paris hay đài Vittoriano ở Roma. Điểm nhấn ngoạn mục nhất là 'Cây Đời' bằng đồng cao 20 m đặt trong vòm cổng lớn ở chính giữa — biểu tượng cho sự phồn thịnh, đất đai màu mỡ và hoà hợp với thiên nhiên. Vào buổi tối, cả mái vòm và tán cây được chiếu sáng bằng ánh xanh lục, biến công trình thành khung cảnh lung linh soi bóng xuống dòng Kazanka. Vị trí sát Kremlin — Di sản Thế giới của UNESCO — từng khiến toà nhà gây tranh cãi gay gắt, người khen kẻ chê về mức độ phù hợp với khu phố cổ. Dù vậy, Cung điện Nông dân nhanh chóng trở thành một trong những địa điểm hiện đại được du khách chụp ảnh nhiều nhất Kazan. Đây là cơ quan nhà nước nên không mở cửa vào bên trong; du khách chủ yếu chiêm ngưỡng và chụp ảnh từ quảng trường phía trước, đẹp nhất là khi lên đèn.",
            "highlights_vi": [
                "'Cây Đời' bằng đồng cao 20 m trong vòm cổng trung tâm, phát sáng xanh về đêm — biểu tượng cho phồn thịnh và đất đai màu mỡ.",
                "Mái vòm cao 48 m; kiến trúc gợi liên tưởng Petit Palais (Paris) và đài Vittoriano (Roma).",
                "Nằm sát Điện Kremlin Kazan (Di sản UNESCO), từng gây tranh cãi nhưng nay là điểm chụp ảnh nổi tiếng bậc nhất thành phố.",
            ],
            "practical": {
                "hours_vi": "Chiêm ngưỡng bên ngoài 24/7; bên trong là cơ quan nhà nước, không mở tham quan.",
                "ticket_vi": "Miễn phí (ngắm và chụp ảnh từ quảng trường).",
                "duration_vi": "20–40 phút.",
                "best_time_vi": "Sau khi trời tối, khi toà nhà và 'Cây Đời' lên đèn xanh.",
                "tips_vi": "Kết hợp tham quan Điện Kremlin Kazan và bờ kè Kazanka ngay cạnh; góc chụp đẹp từ Quảng trường Cung điện phía trước.",
            },
            "photo": None,
            "photo_credit": None,
            "maps": maps_for(55.8006, 49.1122),
            "official_site": "https://agro.tatarstan.ru",
            "sources": [
                {"title": "Wikipedia (EN) — Agricultural Palace", "url": "https://en.wikipedia.org/wiki/Agricultural_Palace"},
                {"title": "Visit Tatarstan — Agricultural Palace", "url": "https://visit-tatarstan.com/en/places/sightseeings/dvorets-zemledeltsev/"},
            ],
            "tags": ["modern", "architecture", "landmark", "night", "photo"],
            "status": "enriched",
            "last_updated": TODAY,
        }
    ],
}


def main():
    summary = []
    for region, recs in RECORDS.items():
        path = os.path.join(REGIONS, region + ".json")
        arr = json.load(open(path, encoding="utf-8"))
        existing_slugs = {r.get("slug") for r in arr}
        existing_ids = {r.get("id") for r in arr}
        to_add = []
        for rec in recs:
            if rec["slug"] in existing_slugs or rec["id"] in existing_ids:
                print(f"  ~ Bo qua (da ton tai): {region}/{rec['slug']}")
                continue
            to_add.append(rec)
        if not to_add:
            continue
        bak = path + f".bak_add_{STAMP}"
        shutil.copy2(path, bak)
        arr.extend(to_add)
        json.dump(arr, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        for rec in to_add:
            summary.append(f"{region}: + {rec['name_vi']} ({rec['coordinates']['lat']},{rec['coordinates']['lon']})")
        print(f"  + {region}: them {len(to_add)} ban ghi (tong file: {len(arr)}); backup: {os.path.basename(bak)}")
    print("\n=== DA THEM ===")
    for s in summary:
        print(" -", s)


if __name__ == "__main__":
    main()
