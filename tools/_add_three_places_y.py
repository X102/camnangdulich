# -*- coding: utf-8 -*-
"""_add_three_places_y.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26).

Ưu tiên VÙNG: các thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.

Thêm:
  1) Tỉnh Moskva (moscow-oblast)   : Nhà - Bảo tàng P. I. Tchaikovsky ở Klin (museum)
  2) Tỉnh Moskva (moscow-oblast)   : Thành Dmitrov Kremlin (fortress/church/museum)
  3) Tỉnh Leningrad (leningrad-oblast): Nhà - Bảo tàng N. A. Rimsky-Korsakov ở Tikhvin (museum)

Nội dung tiếng Việt nguyên gốc, có ghi nguồn. Toạ độ thật (đã đối chiếu web 2026-07,
Wikipedia/Wikidata + nguồn Nga). Link bản đồ theo dạng TRỎ-ĐỊA-ĐIỂM (khớp convention của
tools/retrofit_map_links.py: Yandex tìm theo tên Nga + vùng, canh giữa bằng ll=lon,lat).

Chạy:  python3 tools/_add_three_places_y.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"


def maps_for(name_ru, name_en, region_ru, region_en, lat, lon):
    """Trỏ thẳng tới địa điểm (khớp tools/retrofit_map_links.py để idempotent)."""
    yq = urllib.parse.quote(f"{name_ru}, {region_ru}")
    parts = [name_en]
    if region_en.lower() not in name_en.lower():
        parts.append(region_en)
    parts.append("Russia")
    gq = urllib.parse.quote(", ".join(parts))
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


# ------------------------------------------------------------------ RECORDS
TCHAIKOVSKY_KLIN = {
    "id": "moscow-oblast-tchaikovsky-house-museum-klin",
    "slug": "tchaikovsky-house-museum-klin",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Nhà - Bảo tàng P. I. Tchaikovsky ở Klin",
    "name_ru": "Дом-музей П. И. Чайковского",
    "name_en": "Tchaikovsky House-Museum (Klin)",
    "categories": ["museum"],
    "coordinates": {"lat": 56.32923, "lon": 36.74718},
    "address_vi": "Phố Chaykovskogo số 48, thành phố Klin, Tỉnh Moskva; cách trung tâm Moskva khoảng 85 km về phía tây bắc, gần ga đường sắt Klin trên tuyến Moskva – Saint Petersburg.",
    "rating": None,
    "presentation_short_vi": (
        "Ngôi nhà gỗ hai tầng nơi nhà soạn nhạc vĩ đại Pyotr Ilyich Tchaikovsky sống những "
        "tháng cuối đời (1892–1893) và hoàn tất Bản giao hưởng số 6 'Bi thương'. Sau khi ông "
        "qua đời, người em Modest đã biến ngôi nhà thành bảo tàng - được xem là bảo tàng âm nhạc "
        "tưởng niệm đầu tiên của nước Nga, gìn giữ gần như nguyên vẹn không gian sống và cây đàn "
        "piano của nhạc sĩ."
    ),
    "presentation_long_vi": (
        "Nằm ở rìa thị trấn Klin phía tây bắc Moskva, đây là ngôi nhà cuối cùng gắn với cuộc đời "
        "Tchaikovsky. Suốt thập niên 1880 nhạc sĩ khao khát một chốn tĩnh lặng ngoài đô thị để "
        "sáng tác; ông lần lượt thuê nhà ở làng Maidanovo rồi Frolovskoye gần đó, trước khi từ "
        "tháng 5 năm 1892 dọn về căn nhà rộng rãi của gia đình Sakharov ngay cạnh đường lớn đi "
        "Moskva - chính là toà nhà nay thành bảo tàng. Ông ở tầng hai, còn tầng trệt dành cho gia "
        "đình người hầu thân tín Aleksei Sofronov. Trong hơn một năm sống tại Klin, Tchaikovsky đã "
        "soát in tổng phổ các vở 'Iolanta' và 'Kẹp hạt dẻ' (The Nutcracker), viết nhiều tiểu phẩm "
        "piano và đặc biệt là Bản giao hưởng số 6 giọng Si thứ - 'Pathétique', tác phẩm lớn cuối "
        "cùng, hoàn thành trên chiếc bàn gỗ mộc kê nhìn ra vườn. Đầu tháng 10 năm 1893 ông rời "
        "Klin lên Moskva rồi Saint Petersburg để chỉ huy buổi công diễn giao hưởng số 6, và qua "
        "đời tại đó ít ngày sau ở tuổi 53. Người em - nhà viết kịch Modest Tchaikovsky, cùng người "
        "cháu Vladimir Davydov, đã gìn giữ nguyên trạng ngôi nhà và lập nên bảo tàng, dựng thêm "
        "một toà nhà phụ trong khuôn viên để lưu trữ bản thảo, thư từ và thư viện của nhạc sĩ; "
        "Modest mong bảo tàng noi theo cách bảo tồn nhà Mozart ở Salzburg và nhà Beethoven ở Bonn. "
        "Năm 1921 nơi đây chính thức trở thành tài sản nhà nước. Trong Thế chiến II, bộ sưu tập "
        "được sơ tán về Votkinsk - quê sinh của Tchaikovsky, còn ngôi nhà bị lính Đức chiếm đóng "
        "làm doanh trại; sau chiến tranh, bảo tàng mở lại đúng dịp sinh nhật nhạc sĩ tháng 5 năm "
        "1945. Điểm quý nhất là phòng khách kiêm phòng làm việc với cây đại dương cầm hiệu Becker; "
        "theo truyền thống có từ giữa thế kỉ 20, những người đoạt giải Cuộc thi Tchaikovsky Quốc "
        "tế (như Van Cliburn năm 1958) được mời tới Klin chơi chính cây đàn này, và các nhạc sĩ "
        "còn có lệ trồng cây sồi trong khu vườn đầy hoa linh lan mà ông yêu thích."
    ),
    "highlights_vi": [
        "Nơi Tchaikovsky sống 1892–1893 và hoàn thành Bản giao hưởng số 6 'Pathétique'.",
        "Bảo tàng âm nhạc tưởng niệm đầu tiên của nước Nga, do em trai Modest lập và giữ nguyên trạng.",
        "Cây đại dương cầm Becker mà các quán quân Cuộc thi Tchaikovsky Quốc tế được mời tới chơi.",
    ],
    "practical": {
        "hours_vi": "Thường mở 10:00–18:00, nghỉ thứ Tư và thứ Năm cuối tháng; giờ có thể thay đổi nên xem trang chính thức.",
        "ticket_vi": "Có bán vé vào cửa, nhiều mức ưu đãi cho học sinh - sinh viên - người cao tuổi (xem giá hiện hành).",
        "duration_vi": "Khoảng 1,5–2 giờ (nhà tưởng niệm và khu trưng bày, dạo vườn).",
        "best_time_vi": "Ngày thường để tránh đông; mùa xuân - hè khi khu vườn nở hoa linh lan đẹp nhất.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô (elektrichka) từ ga Leningradsky tới ga Klin rồi bắt xe buýt/taxi; có thể kết hợp buổi hoà nhạc thính phòng thường tổ chức tại bảo tàng.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Дом-музей П. И. Чайковского", "Tchaikovsky House-Museum (Klin)", "Московская область", "Moscow Oblast", 56.32923, 36.74718),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Tchaikovsky State House-Museum", "url": "https://en.wikipedia.org/wiki/Tchaikovsky_State_House-Museum"},
        {"title": "Museum.ru — P.I. Tchaikovsky State House-Museum in Klin", "url": "http://www.museum.ru/mscreg/e5_hist.htm"},
        {"title": "Rusmania — Pyotr Tchaikovsky House-Museum (Klin)", "url": "https://rusmania.com/central/moscow-region/klin/sights/around-the-city/pyotr-tchaikovsky-house-museum"},
    ],
    "tags": ["museum", "music", "tchaikovsky", "memorial", "klin", "composer"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


DMITROV_KREMLIN = {
    "id": "moscow-oblast-dmitrov-kremlin",
    "slug": "dmitrov-kremlin",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Thành Dmitrov Kremlin",
    "name_ru": "Дмитровский кремль",
    "name_en": "Dmitrov Kremlin",
    "categories": ["fortress", "church", "museum"],
    "coordinates": {"lat": 56.34431, "lon": 37.52056},
    "address_vi": "Khu Kremlin ở trung tâm lịch sử thành phố Dmitrov, Tỉnh Moskva; cách Moskva khoảng 65 km về phía bắc, bên sông Yakhroma và kênh đào Moskva.",
    "rating": None,
    "presentation_short_vi": (
        "Quần thể thành cổ ở trái tim Dmitrov - một trong những đô thị lâu đời nhất Tỉnh Moskva, "
        "do công tước Yuri Dolgoruky lập năm 1154 (cùng người khai sinh Moskva). Nổi bật là vòng "
        "luỹ đất cao 7–9 m còn gần như nguyên vẹn, ôm lấy Nhà thờ Đức Mẹ Lên Trời (Uspensky) đầu "
        "thế kỉ 16 - biểu tượng của thành phố."
    ),
    "presentation_long_vi": (
        "Thành Dmitrov ra đời năm 1154 do đại công tước Yuri Dolgoruky - người cũng khai sinh "
        "Moskva - cho lập tại nơi con trai ông là Vsevolod 'Tổ Lớn' chào đời; tên thành lấy theo "
        "thánh bổn mạng Dmitry (Demetrius) của vị hoàng tử. Trải các thế kỉ, Dmitrov từng là thủ "
        "phủ của một công quốc nhỏ, chứng kiến thời hoàng kim đầu thế kỉ 16 dưới thời công tước "
        "Yuri Ivanovich. Di sản đặc sắc nhất của khu Kremlin là vòng luỹ đất (val) chu vi khoảng "
        "990 m, cao 7–9 m, đắp trong khoảng thế kỉ 12–13; xưa trên đỉnh luỹ là tường gỗ cùng các "
        "tháp canh và cổng thành, nay chỉ còn gò đất cỏ xanh mà du khách có thể leo lên đi dạo "
        "vòng quanh. Bên trong luỹ sừng sững Nhà thờ Đức Mẹ Lên Trời (Uspensky sobor) xây khoảng "
        "1509–1533, thuộc dòng kiến trúc 'kiểu Ý' của Moskva đầu thế kỉ 16, nổi tiếng với những "
        "bức phù điêu gốm men màu quý hiếm gắn trên tường. Ngày nay cả khu là bảo tàng ngoài trời "
        "'Bảo tàng - Khu bảo tồn Dmitrovsky Kremlin', bao gồm cổng thành Nikolskiye bằng gỗ được "
        "phục dựng, dãy nhà trưng bày lịch sử - đời sống địa phương, cùng các đài tưởng niệm Yuri "
        "Dolgoruky và nhà tư tưởng - công tước Pyotr Kropotkin (người sống những năm cuối đời ở "
        "Dmitrov). Với quy mô gọn gàng, không khí tỉnh lỵ yên bình và bề dày gần chín thế kỉ lịch "
        "sử, Dmitrov Kremlin là điểm đến lý tưởng cho một chuyến đi trong ngày từ Moskva."
    ),
    "highlights_vi": [
        "Vòng luỹ đất chu vi ~990 m, cao 7–9 m từ thế kỉ 12–13, có thể đi bộ dạo trên đỉnh.",
        "Nhà thờ Đức Mẹ Lên Trời (Uspensky) đầu thế kỉ 16 với phù điêu gốm men màu quý hiếm.",
        "Bảo tàng - khu bảo tồn ngoài trời cùng cổng gỗ phục dựng và tượng đài Yuri Dolgoruky, Kropotkin.",
    ],
    "practical": {
        "hours_vi": "Không gian luỹ đất - quảng trường mở tự do cả ngày; các nhà trưng bày của bảo tàng thường mở 9:00–17:00, nghỉ đầu tuần (xem lịch cụ thể).",
        "ticket_vi": "Dạo khu Kremlin và luỹ đất miễn phí; vào các gian trưng bày của bảo tàng và nhà thờ có thể mua vé riêng.",
        "duration_vi": "Khoảng 1,5–2 giờ cho khu Kremlin; nửa ngày nếu dạo thêm phố cổ Dmitrov.",
        "best_time_vi": "Mùa hè hoặc đầu thu trời khô ráo để leo luỹ đất; cuối tuần phố đi bộ nhộn nhịp hơn.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô từ ga Savyolovsky tới ga Dmitrov (khoảng 1,5 giờ) rồi đi bộ vào trung tâm; kết hợp dạo phố Kropotkinskaya với nhiều tượng đồng sinh động.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Дмитровский кремль", "Dmitrov Kremlin", "Московская область", "Moscow Oblast", 56.34431, 37.52056),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Dmitrov", "url": "https://en.wikipedia.org/wiki/Dmitrov"},
        {"title": "Wikipedia (RU) — Успенский собор (Дмитров)", "url": "https://ru.wikipedia.org/wiki/Успенский_собор_(Дмитров)"},
        {"title": "Sobory.ru — Дмитров, Собор Успения Пресвятой Богородицы", "url": "https://sobory.ru/article/?object=00398"},
    ],
    "tags": ["fortress", "kremlin", "church", "history", "museum-reserve", "dmitrov", "day-trip"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


RIMSKY_KORSAKOV_TIKHVIN = {
    "id": "leningrad-oblast-rimsky-korsakov-house-museum-tikhvin",
    "slug": "rimsky-korsakov-house-museum-tikhvin",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Nhà - Bảo tàng N. A. Rimsky-Korsakov ở Tikhvin",
    "name_ru": "Мемориальный дом-музей Н. А. Римского-Корсакова",
    "name_en": "Rimsky-Korsakov House-Museum (Tikhvin)",
    "categories": ["museum"],
    "coordinates": {"lat": 59.65354, "lon": 33.51491},
    "address_vi": "Phố Rimskogo-Korsakova số 12, thành phố Tikhvin, Tỉnh Leningrad; bên bờ sông Tikhvinka, đối diện Tu viện Đức Mẹ Lên Trời Tikhvin, cách Saint Petersburg khoảng 200 km về phía đông.",
    "rating": None,
    "presentation_short_vi": (
        "Ngôi nhà gỗ đầu thế kỉ 19 bên sông Tikhvinka - nơi nhà soạn nhạc Nikolai Rimsky-Korsakov "
        "chào đời năm 1844 và trải qua tuổi thơ. Khánh thành năm 1944 nhân 100 năm ngày sinh của "
        "ông, đây là bảo tàng tưởng niệm gìn giữ đồ đạc nguyên bản của gia đình cùng những kỉ vật "
        "gắn với thời niên thiếu của người nhạc sĩ."
    ),
    "presentation_long_vi": (
        "Toà nhà gỗ khang trang bên bờ sông Tikhvinka, nhìn thẳng sang Tu viện Đức Mẹ Lên Trời "
        "Tikhvin, do gia đình quý tộc Rimsky-Korsakov dựng từ năm 1801. Chính tại đây, ngày 18 "
        "tháng 3 năm 1844, Nikolai Andreyevich Rimsky-Korsakov cất tiếng khóc chào đời và sống "
        "trọn tuổi thơ cho tới khoảng mười hai tuổi, trước khi lên Saint Petersburg vào học "
        "Trường Thiếu sinh quân Hải quân. Ông về sau trở thành một trong những cột trụ của nhóm "
        "'Khoẻ khoắn' (Moguchaya kuchka) và là bậc thầy phối khí, tác giả của tổ khúc giao hưởng "
        "'Sheherazade', các vở opera 'Con gà trống vàng', 'Nàng tuyết', cùng khúc 'Chuyến bay của "
        "ong nghệ' quen thuộc khắp thế giới. Ngôi nhà được mở thành bảo tàng vào tháng 7 năm 1944, "
        "đúng dịp kỉ niệm 100 năm ngày sinh nhạc sĩ. Không gian bên trong tái hiện nếp sống của một "
        "gia đình quý tộc tỉnh lẻ giữa thế kỉ 19: bàn ghế, tranh chân dung, sách vở và nhạc cụ "
        "nguyên bản của gia đình, trong đó có cây đàn piano gắn với những bài học âm nhạc đầu đời "
        "của cậu bé Nikolai. Khu vườn và mặt sông phía trước tạo nên khung cảnh nên thơ; bảo tàng "
        "thường xuyên tổ chức các buổi hoà nhạc thính phòng và sự kiện tưởng niệm. Nằm ngay cạnh "
        "quần thể tu viện nổi tiếng của Tikhvin, ngôi nhà - bảo tàng là điểm dừng chân giàu chất "
        "văn hoá cho hành trình khám phá vùng đông Tỉnh Leningrad."
    ),
    "highlights_vi": [
        "Ngôi nhà nơi Nikolai Rimsky-Korsakov chào đời (1844) và sống thời thơ ấu.",
        "Bảo tàng mở năm 1944 nhân 100 năm ngày sinh, giữ nguyên đồ đạc và nhạc cụ của gia đình.",
        "Vị trí nên thơ bên sông Tikhvinka, đối diện Tu viện Đức Mẹ Lên Trời Tikhvin.",
    ],
    "practical": {
        "hours_vi": "Thường mở 10:00–18:00, nghỉ thứ Hai và ngày vệ sinh cuối tháng; giờ có thể thay đổi nên xem trang chính thức.",
        "ticket_vi": "Có bán vé vào cửa, nhiều mức ưu đãi cho học sinh - sinh viên - người cao tuổi.",
        "duration_vi": "Khoảng 1 giờ (có thể lâu hơn nếu trùng buổi hoà nhạc).",
        "best_time_vi": "Mùa hè khi khu vườn ven sông đẹp nhất; nên hỏi lịch hoà nhạc thính phòng.",
        "tips_vi": "Tiện kết hợp thăm Tu viện Đức Mẹ Lên Trời Tikhvin ngay đối diện; từ Saint Petersburg có tàu hoả và xe khách tới Tikhvin.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Мемориальный дом-музей Н. А. Римского-Корсакова", "Rimsky-Korsakov House-Museum (Tikhvin)", "Ленинградская область", "Leningrad Oblast", 59.65354, 33.51491),
    "official_site": None,
    "sources": [
        {"title": "Culture.ru — Мемориальный дом-музей Н. А. Римского-Корсакова", "url": "https://www.culture.ru/institutes/11116/memorialnyi-dom-muzei-n-a-rimskogo-korsakova"},
        {"title": "KudaGo — Дом-музей Н. Римского-Корсакова в Тихвине", "url": "https://kudago.com/spb/place/dom-muzej-n-rimskogo-korsakova-v-g-tihvin/"},
        {"title": "Lonely Planet — Rimsky-Korsakov House-Museum (Tikhvin)", "url": "https://www.lonelyplanet.com/russia/st-petersburg/around-st-petersburg/tikhvin/attractions/rimsky-korsakov-house-museum/a/poi-sig/1474161/1315169"},
    ],
    "tags": ["museum", "music", "rimsky-korsakov", "memorial", "tikhvin", "composer"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [TCHAIKOVSKY_KLIN, DMITROV_KREMLIN],
    "leningrad-oblast.json": [RIMSKY_KORSAKOV_TIKHVIN],
}


def main():
    total_added = 0
    for fname, recs in PLAN.items():
        path = os.path.join(REGIONS, fname)
        arr = json.load(open(path, encoding="utf-8"))
        existing_slugs = {p.get("slug") for p in arr}
        existing_ids = {p.get("id") for p in arr}
        to_add = []
        for r in recs:
            if r["slug"] in existing_slugs or r["id"] in existing_ids:
                print(f"  = BỎ QUA (đã có): {fname} :: {r['slug']}")
                continue
            to_add.append(r)
        if not to_add:
            continue
        bak = path + f".bak_add_{TS}"
        with open(bak, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        arr.extend(to_add)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        total_added += len(to_add)
        print(f"  + {fname}: thêm {len(to_add)} địa điểm -> tổng {len(arr)} (backup: {os.path.basename(bak)})")
        for r in to_add:
            print(f"        - {r['name_vi']}  [{','.join(r['categories'])}]  ({r['coordinates']['lat']},{r['coordinates']['lon']})")

    print(f"\nTổng đã thêm lần này: {total_added} địa điểm.")


if __name__ == "__main__":
    main()
