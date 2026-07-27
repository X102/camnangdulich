# -*- coding: utf-8 -*-
"""Bổ sung 3 địa điểm nổi tiếng/hiện đại còn thiếu vào Cẩm nang Du lịch Nga.
Lần chạy E (2026-07-25): MAMM + Bảo tàng Nghệ thuật Phương Đông (Moskva) và
Cung điện Beloselsky-Belozersky (Saint Petersburg).
Nội dung tiếng Việt nguyên gốc (không sao chép/dịch nguyên văn), có ghi nguồn.
Tạo backup trước khi ghi, kiểm tra trùng slug/id.
Chạy: python3 tools/_add_three_places_e.py"""
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
            "id": "moscow-multimedia-art-museum",
            "slug": "multimedia-art-museum",
            "region": "moscow",
            "region_name_vi": "Moskva",
            "federal_district": "Thành phố trực thuộc liên bang",
            "name_vi": "Bảo tàng Nghệ thuật Đa phương tiện Moskva (MAMM / Multimedia Art Museum)",
            "name_ru": "Мультимедиа Арт Музей, Москва (МАММ)",
            "name_en": "Multimedia Art Museum, Moscow (MAMM)",
            "categories": ["museum"],
            "coordinates": {"lat": 55.7416, "lon": 37.5987},
            "address_vi": "Phố Ostozhenka (Ô-xtô-gien-ka), số 16, Moscow 119034; gần ga tàu điện ngầm Kropotkinskaya (Crô-pốt-kin-xkai-a) và Nhà thờ Chúa Cứu Thế.",
            "rating": null_rating(),
            "review_summary_vi": "Nhiều du khách đánh giá cao không gian trưng bày hiện đại, sáng sủa và các triển lãm luôn thay mới; một số lưu ý nên xem trước lịch triển lãm vì nội dung mỗi tầng thay đổi liên tục theo mùa.",
            "presentation_short_vi": "Bảo tàng nghệ thuật đương đại và nhiếp ảnh hàng đầu Moskva, phát triển từ 'Ngôi nhà Nhiếp ảnh Moskva' (thành lập năm 1996) và mở cửa trở lại năm 2010 trong toà nhà hiện đại trên phố Ostozhenka. Không có bộ sưu tập cố định, MAMM liên tục thay đổi với các triển lãm nhiếp ảnh, video và nghệ thuật số luân phiên.",
            "presentation_long_vi": "Bảo tàng Nghệ thuật Đa phương tiện Moskva khởi nguồn từ 'Ngôi nhà Nhiếp ảnh Moskva' (Moskovsky Dom Fotografii) — bảo tàng đầu tiên của nước Nga dành riêng cho nghệ thuật nhiếp ảnh, do nhà giám tuyển Olga Sviblova sáng lập năm 1996. Sau đợt cải tạo lớn, năm 2010 công trình mở cửa trở lại dưới tên gọi mới MAMM trong một toà nhà hiện đại nhiều tầng ngay trên phố Ostozhenka, cách Nhà thờ Chúa Cứu Thế không xa. Khác với những bảo tàng cổ điển trưng bày bộ sưu tập cố định, MAMM hoạt động như một không gian triển lãm luân phiên: mỗi mùa, các tầng nhà lại thay đổi hoàn toàn với những dự án nhiếp ảnh, video art, nghệ thuật số và nghệ thuật đương đại của cả tác giả Nga lẫn quốc tế. Đây cũng là nơi tổ chức hai liên hoan lớn do bảo tàng khởi xướng là 'Photobiennale' và 'Thời trang và Phong cách trong Nhiếp ảnh', quy tụ nhiều tên tuổi hàng đầu. Với kiến trúc tối giản, ánh sáng hiện đại và nội dung liên tục đổi mới, MAMM được xem là một trong những địa chỉ nghệ thuật đương đại năng động nhất Moskva, đặc biệt thu hút giới trẻ, người yêu nhiếp ảnh và du khách muốn cảm nhận nhịp sáng tạo mới của thành phố bên cạnh những bảo tàng kinh điển.",
            "highlights_vi": [
                "Phát triển từ 'Ngôi nhà Nhiếp ảnh Moskva' (1996) — bảo tàng nhiếp ảnh đầu tiên của Nga do Olga Sviblova sáng lập; mang tên MAMM từ năm 2010.",
                "Không trưng bày cố định mà xoay vòng nhiều triển lãm nhiếp ảnh, video art và nghệ thuật số theo mùa.",
                "Nơi tổ chức các liên hoan 'Photobiennale' và 'Thời trang và Phong cách trong Nhiếp ảnh'.",
            ],
            "practical": {
                "hours_vi": "Mở cửa thứ Ba–Chủ nhật 12:00–21:00 (quầy vé đóng khoảng 20:30). Nghỉ thứ Hai.",
                "ticket_vi": "Giá vé tham khảo dao động khoảng 50–500 rúp tuỳ triển lãm; Chủ nhật thứ ba hằng tháng thường miễn phí. Nên kiểm tra giá và lịch trên trang chính thức.",
                "duration_vi": "Khoảng 1–2 giờ.",
                "best_time_vi": "Ngày thường để tránh đông; có thể kết hợp dạo phố Ostozhenka – Prechistenka và Nhà thờ Chúa Cứu Thế gần đó.",
                "tips_vi": "Nội dung thay đổi theo mùa nên xem trước lịch triển lãm; phù hợp với người yêu nhiếp ảnh và nghệ thuật đương đại.",
            },
            "photo": None,
            "photo_credit": None,
            "maps": maps_for(55.7416, 37.5987),
            "official_site": "https://mamm-mdf.ru",
            "sources": [
                {"title": "Trang chính thức — Multimedia Art Museum, Moscow (MAMM)", "url": "https://mamm-mdf.ru/en/"},
                {"title": "Wikipedia (EN) — Multimedia Art Museum, Moscow", "url": "https://en.wikipedia.org/wiki/Multimedia_Art_Museum,_Moscow"},
            ],
            "tags": ["modern", "museum", "photography", "contemporary-art", "indoor"],
            "status": "enriched",
            "last_updated": TODAY,
        },
        {
            "id": "moscow-oriental-art-museum",
            "slug": "oriental-art-museum",
            "region": "moscow",
            "region_name_vi": "Moskva",
            "federal_district": "Thành phố trực thuộc liên bang",
            "name_vi": "Bảo tàng Nghệ thuật Phương Đông Quốc gia (Muzey Vostoka)",
            "name_ru": "Государственный музей Востока",
            "name_en": "State Museum of Oriental Art",
            "categories": ["museum"],
            "coordinates": {"lat": 55.7564, "lon": 37.5999},
            "address_vi": "Đại lộ Nikitsky (Ni-kít-xki), số 12A, Moscow; gần Cổng Nikitsky và các ga tàu điện ngầm Arbatskaya, Tverskaya. Bảo tàng đặt trong 'Nhà Lunin' (Dom Luninykh) kiểu đế chế do kiến trúc sư Domenico Gilardi xây dựng đầu thế kỷ 19.",
            "rating": null_rating(),
            "review_summary_vi": "Du khách thường nhận xét bảo tàng yên tĩnh, ít đông đúc, trưng bày phong phú và bất ngờ về chiều sâu; nhiều người thích không gian nội thất cổ kính của toà 'Nhà Lunin' và khu dành cho hoạ sĩ Nikolai Rerikh.",
            "presentation_short_vi": "Bảo tàng quốc gia lớn của nước Nga về nghệ thuật các dân tộc phương Đông, thành lập năm 1918. Bộ sưu tập trải rộng từ Trung Á, Kavkaz, Trung Quốc, Nhật Bản, Triều Tiên, Ấn Độ đến Đông Nam Á, đặt trong 'Nhà Lunin' kiểu đế chế do kiến trúc sư Domenico Gilardi xây ở đầu thế kỷ 19.",
            "presentation_long_vi": "Được thành lập năm 1918, Bảo tàng Nghệ thuật Phương Đông Quốc gia là một trong những bảo tàng lớn và độc đáo nhất nước Nga, chuyên sưu tầm, gìn giữ và giới thiệu nghệ thuật của các dân tộc châu Á và phương Đông. Kho hiện vật đồ sộ của bảo tàng trải dài trên một không gian địa lý rộng lớn: từ nghệ thuật Trung Á và vùng Kavkaz, đồ sứ cùng tranh cuộn Trung Quốc, tranh khắc gỗ và kiếm Nhật Bản, cho tới điêu khắc Ấn Độ, nghệ thuật Triều Tiên, Iran và các nước Đông Nam Á. Một điểm nhấn được nhiều người tìm đến là bộ sưu tập và các gian tưởng niệm dành cho hoạ sĩ – nhà tư tưởng Nikolai Rerikh (Roerich) cùng gia đình ông, những người gắn bó sâu sắc với văn hoá phương Đông và dãy Himalaya. Bảo tàng toạ lạc trong 'Nhà Lunin' (Dom Luninykh) trên đại lộ Nikitsky — một dinh thự kiểu đế chế (empire) thanh lịch do kiến trúc sư người Ý Domenico Gilardi thiết kế vào đầu thế kỷ 19, bản thân toà nhà đã là một di tích kiến trúc. Với những ai muốn khám phá một khía cạnh khác của văn hoá Nga — nơi giao thoa giữa châu Âu và châu Á — đây là điểm đến giàu chiều sâu, yên tĩnh và khác biệt so với các bảo tàng nghệ thuật châu Âu quen thuộc ở trung tâm Moskva.",
            "highlights_vi": [
                "Bảo tàng quốc gia chuyên về nghệ thuật phương Đông, thành lập năm 1918; một trong những bộ sưu tập nghệ thuật châu Á lớn nhất nước Nga.",
                "Hiện vật trải rộng từ Trung Á, Kavkaz, Trung Quốc, Nhật Bản, Triều Tiên, Ấn Độ đến Iran và Đông Nam Á.",
                "Có bộ sưu tập và gian tưởng niệm hoạ sĩ Nikolai Rerikh (Roerich); đặt trong 'Nhà Lunin' kiểu đế chế của kiến trúc sư Domenico Gilardi.",
            ],
            "practical": {
                "hours_vi": "Mở cửa thứ Ba, thứ Sáu, thứ Bảy và Chủ nhật 11:00–20:00 (quầy vé đến 19:30); thứ Tư và thứ Năm 12:00–21:00 (quầy vé đến 20:30). Nghỉ thứ Hai. Nên kiểm tra lại lịch trên trang chính thức.",
                "ticket_vi": "Giá vé tham khảo khoảng 300 rúp/người lớn (thay đổi theo triển lãm và ưu đãi); thứ Năm tuần thứ tư hằng tháng thường miễn phí cho người dưới 18 tuổi và sinh viên. Nên kiểm tra giá mới trên trang chính thức.",
                "duration_vi": "Khoảng 1,5–2 giờ.",
                "best_time_vi": "Ngày thường để tận hưởng không gian yên tĩnh; có thể kết hợp dạo phố Nikitsky, khu Cổng Nikitsky và Nhạc viện Traicốpxki gần đó.",
                "tips_vi": "Không gian yên tĩnh, hợp cho người yêu văn hoá châu Á; đừng bỏ qua khu tưởng niệm Nikolai Rerikh và kiến trúc nội thất của 'Nhà Lunin'.",
            },
            "photo": None,
            "photo_credit": None,
            "maps": maps_for(55.7564, 37.5999),
            "official_site": "https://orientmuseum.ru",
            "sources": [
                {"title": "Trang chính thức — Государственный музей Востока", "url": "https://orientmuseum.ru/"},
                {"title": "Wikipedia (EN) — State Museum of Oriental Art", "url": "https://en.wikipedia.org/wiki/State_Museum_of_Oriental_Art"},
            ],
            "tags": ["museum", "asian-art", "oriental", "indoor", "history"],
            "status": "enriched",
            "last_updated": TODAY,
        },
    ],
    "saint-petersburg": [
        {
            "id": "saint-petersburg-beloselsky-belozersky-palace",
            "slug": "beloselsky-belozersky-palace",
            "region": "saint-petersburg",
            "region_name_vi": "Saint Petersburg",
            "federal_district": "Thành phố trực thuộc liên bang",
            "name_vi": "Cung điện Beloselsky-Belozersky (Bê-lô-xen-xkikh – Bê-lô-déc-xkikh)",
            "name_ru": "Дворец Белосельских-Белозерских",
            "name_en": "Beloselsky-Belozersky Palace",
            "categories": ["palace"],
            "coordinates": {"lat": 59.9328, "lon": 30.3440},
            "address_vi": "Đại lộ Nevsky (Nhe-vxki), số 41 / bờ kè sông Fontanka số 42, cạnh Cầu Anichkov, Saint Petersburg; gần ga tàu điện ngầm Gostiny Dvor và Mayakovskaya.",
            "rating": null_rating(),
            "review_summary_vi": "Du khách đặc biệt ấn tượng với mặt tiền đỏ rực và các tượng thần Atlas (atlant); nhiều người khen nội thất dát vàng, cầu thang và các sảnh lộng lẫy khi tham quan theo tour, cùng vị trí đắc địa ngay Cầu Anichkov.",
            "presentation_short_vi": "Cung điện tân Baroque lộng lẫy với mặt tiền đỏ – trắng và những tượng thần Atlas (atlant) đỡ ban công, nằm ngay góc đại lộ Nevsky và sông Fontanka bên Cầu Anichkov. Được kiến trúc sư Andrei Stackenschneider xây lại năm 1847–1848, đây được xem là dinh thự quý tộc tư nhân lớn cuối cùng dựng trên đại lộ Nevsky trong thế kỷ 19.",
            "presentation_long_vi": "Nằm ở một trong những góc phố đẹp nhất Saint Petersburg — nơi đại lộ Nevsky gặp sông Fontanka bên Cầu Anichkov — Cung điện Beloselsky-Belozersky nổi bật với mặt tiền màu đỏ thẫm điểm chi tiết trắng và những pho tượng thần khổng lồ Atlas (atlant) như đang gồng mình đỡ lấy ban công. Công trình được kiến trúc sư Andrei Stackenschneider xây dựng lại trong hai năm 1847–1848 theo phong cách tân Baroque (đôi khi gọi là 'Baroque thứ hai'), cố ý gợi lại vẻ tráng lệ của những cung điện do Rastrelli thiết kế thời Nữ hoàng Elizaveta, như Cung điện Stroganov gần đó. Những tượng atlant trên mặt tiền là tác phẩm của nhà điêu khắc David Jensen. Đây được xem là dinh thự quý tộc tư nhân lớn cuối cùng được dựng trên đại lộ Nevsky trong thế kỷ 19. Từ năm 1884, cung điện thuộc về Đại công tước Sergei Aleksandrovich — em trai Hoàng đế Aleksandr III — và có thời được gọi là 'Cung điện Sergievsky'. Ngày nay, cung điện là một trung tâm văn hoá: du khách có thể tham quan các gian phòng và cầu thang nội thất được gìn giữ theo tour hướng dẫn, thưởng thức hoà nhạc thính phòng, và vào một số thời điểm còn có trưng bày tượng sáp. Ngay cả khi chỉ đứng ngắm từ bên ngoài, mặt tiền rực rỡ của cung điện cũng là một trong những khung hình được yêu thích nhất trên đại lộ Nevsky.",
            "highlights_vi": [
                "Cung điện tân Baroque với mặt tiền đỏ – trắng và tượng thần Atlas (atlant), do Andrei Stackenschneider xây lại năm 1847–1848.",
                "Được xem là dinh thự quý tộc tư nhân lớn cuối cùng dựng trên đại lộ Nevsky; từ năm 1884 thuộc Đại công tước Sergei Aleksandrovich ('Cung điện Sergievsky').",
                "Nằm ngay góc Nevsky và sông Fontanka bên Cầu Anichkov; nay là trung tâm văn hoá với tour nội thất và hoà nhạc thính phòng.",
            ],
            "practical": {
                "hours_vi": "Nội thất tham quan chủ yếu theo tour hướng dẫn, thường trong khung khoảng 12:00–18:00; lịch có thể thay đổi theo sự kiện và buổi hoà nhạc. Nên đặt/kiểm tra trước trên trang chính thức.",
                "ticket_vi": "Giá vé tham quan và vé hoà nhạc thay đổi tuỳ chương trình; nên xem lịch và giá cập nhật trên trang chính thức hoặc tại quầy vé.",
                "duration_vi": "Khoảng 1–1,5 giờ cho tour nội thất.",
                "best_time_vi": "Kết hợp khi dạo đại lộ Nevsky và Cầu Anichkov; buổi tối có thể xem hoà nhạc thính phòng trong không gian cung điện.",
                "tips_vi": "Nên kiểm tra lịch tour và hoà nhạc trước; ngay cả khi không vào trong, mặt tiền bên Cầu Anichkov cũng rất đáng chụp ảnh.",
            },
            "photo": None,
            "photo_credit": None,
            "maps": maps_for(59.9328, 30.3440),
            "official_site": None,
            "sources": [
                {"title": "Wikipedia (EN) — Beloselsky-Belozersky Palace", "url": "https://en.wikipedia.org/wiki/Beloselsky-Belozersky_Palace"},
                {"title": "Wikipedia (RU) — Дворец Белосельских-Белозерских", "url": "https://ru.wikipedia.org/wiki/Дворец_Белосельских-Белозерских"},
                {"title": "saint-petersburg.com — Beloselsky-Belozersky Palace", "url": "http://www.saint-petersburg.com/palaces/beloselskiy-belozerskiy-palace/"},
            ],
            "tags": ["palace", "neo-baroque", "nevsky", "fontanka", "historic"],
            "status": "enriched",
            "last_updated": TODAY,
        },
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
