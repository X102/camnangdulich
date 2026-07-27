# -*- coding: utf-8 -*-
"""_add_three_places_am_moscow.py — Bo sung 3 dia diem con thieu (lan chay tu dong 2026-07-27, phien am / Moscow Oblast).

Ten file co hau to "_moscow" de TRANH DE LEN script _add_three_places_am.py (thuoc tac vu Viet Nam khac).

UU TIEN VUNG (a): cac THI TRAN/THANH PHO PHU CAN quanh Moskva (moscow-oblast.json).
Noi do Moskva & SPb da bao hoa; Leningrad Oblast (20) va Moscow Oblast (38) da phu day,
nhung Moscow Oblast VAN con vai danh thang that su noi tieng bi thieu -> bo sung 3 diem sau:

  1) Tu vien Pokrovsky Khotkov (Khotkovo)            [church]
        — mot trong nhung tu vien co nhat nuoc Nga (nhac toi tu 1308); noi tu hanh & an tang
          song than Thanh Sergius (Thanh Kirill & Maria); khach hanh huong vieng cha me truoc,
          roi moi len Trinity Lavra vieng nguoi con.
  2) Nha tho Tong lanh Thien than Mikhail (Bronnitsy) [church, monument]
        — nha tho co nhat Bronnitsy (1696-1705, thoi Pyotr Dai de); thap chuong 73 m cao nhat
          Tinh Moskva; mo cac nha Cach mang Thang Chap (Fonvizin, Pushchin) ngay ben tuong.
  3) Dai tuong niem Cao diem Peremilovo (Yakhroma)   [monument]
        — bieu tuong Tran Moskva 1941; tuong dai nguoi linh cao 28 m (1966); diem ngam canh
          kenh dao Moskva & TP Yakhroma.

TOA DO THAT (WGS84, doi chieu 2026-07 — Wikipedia/Yandex Maps, dung thu tu lat~55-56, lon~37-38):
  - Khotkov:   56.25083, 37.99389  (Wikipedia RU 56 deg 15'03"N 37 deg 59'38"E; Yandex org)
  - Bronnitsy: 55.42658, 38.26493  (Wikipedia RU / sobory.ru; ul. Sovetskaya 61)
  - Peremilovo:56.29802, 37.50014  (Wikipedia RU 56 deg 17'53"N 37 deg 30'00"E; Yandex org)

Noi dung tieng Viet NGUYEN GOC (paraphrase tu nguon mo, khong sao chep nguyen van; ghi nguon).
Chen AN TOAN: bo qua slug/id da ton tai; sao luu .bak truoc khi ghi.
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TODAY = "2026-07-27"
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

REGION_SLUG = "moscow-oblast"
REGION_NAME_VI = "Tỉnh Moskva"
FED = "Vùng Trung tâm"


def build_maps(lat, lon, name_ru, name_en, city_ru, city_en, org_url=None):
    """Link ban do TRO THANG toi dia diem. Uu tien URL trang to chuc tren Yandex (chinh xac nhat);
    neu khong co thi dung text=<ten Nga>, <thanh pho> + ll=lon,lat de mo dung the dia diem."""
    if org_url:
        yandex = org_url
    else:
        yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
        yandex = f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16"
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    google = f"https://www.google.com/maps/search/?api=1&query={gq}"
    return {"yandex": yandex, "google": google}


# ============================================================ 1) POKROVSKY KHOTKOV MONASTERY
KHOTKOV = {
    "id": "moscow-oblast-pokrovsky-khotkov-monastery",
    "slug": "pokrovsky-khotkov-monastery",
    "region": REGION_SLUG,
    "region_name_vi": REGION_NAME_VI,
    "federal_district": FED,
    "name_vi": "Tu viện Pokrovsky Khotkov (Покровский Хотьков монастырь)",
    "name_ru": "Покровский Хотьков монастырь",
    "name_en": "Pokrovsky Khotkov Monastery",
    "categories": ["church"],
    "coordinates": {"lat": 56.25083, "lon": 37.99389},
    "address_vi": "Phố Kooperativnaya 2, thị trấn Khotkovo, huyện Sergiev Posad, Tỉnh Moskva; bên sông Pazha, cách trung tâm Moskva khoảng 60 km về phía đông bắc và cách Tu viện Trinity Lavra (Sergiev Posad) chỉ khoảng 11 km.",
    "rating": None,
    "presentation_short_vi": "Tu viện Pokrovsky Khotkov là một trong những tu viện cổ nhất nước Nga, lần đầu được nhắc tới trong sử liệu năm 1308. Nơi đây gắn liền với song thân của Thánh Sergius thành Radonezh - hai vị được tôn phong là Thánh Kirill và Thánh Maria - đã khấn dòng, qua đời và được an táng tại Nhà thờ Pokrovsky, nơi lưu giữ thánh tích của các ngài đến ngày nay. Theo truyền thống lâu đời, khách hành hương ghé Khotkovo kính viếng cha mẹ trước, rồi mới lên Trinity Lavra kính viếng người con.",
    "presentation_long_vi": "Nằm bên dòng sông Pazha ở thị trấn Khotkovo, cách Moskva khoảng 60 km về phía đông bắc, Tu viện Pokrovsky Khotkov là một trong những tu viện lâu đời nhất của nước Nga, xuất hiện trong sử liệu từ năm 1308. Danh tiếng thiêng liêng của tu viện gắn chặt với gia đình Thánh Sergius thành Radonezh: vào thập niên 1330, song thân của ngài - hai vị được Giáo hội tôn phong là Thánh Kirill và Thánh Maria thành Radonezh - đã vào đây khấn dòng những năm cuối đời. Sau khi các ngài qua đời năm 1337, con cái an táng cha mẹ ngay trong tu viện; thánh tích của hai vị đến nay vẫn được lưu giữ và tôn kính trong Nhà thờ Pokrovsky (Cầu Bầu). Chính vì thế, suốt nhiều thế kỷ, người hành hương giữ lệ đến Khotkovo kính viếng song thân trước, rồi mới đến Sergiev Posad (Trinity Lavra) kính viếng người con - tạo thành một tuyến hành hương liền mạch nổi tiếng của vùng đông bắc Moskva. Quần thể ngày nay là một nữ tu viện đang hoạt động, nổi bật với hai ngôi thánh đường: Nhà thờ Pokrovsky khối tân cổ điển và Nhà thờ Nikolsky đồ sộ theo phong cách Nga - Byzantine, xây dựng trong các năm 1900-1904 với những mái vòm lớn và không gian nội thất khoáng đạt. Dạo bước trong khuôn viên tĩnh lặng sau tường bao, du khách cảm nhận bầu không khí trầm mặc, mộc mạc rất khác với sự nhộn nhịp của Lavra kề bên. Nhờ nằm ngay cạnh tuyến đường bộ và đường sắt đi Sergiev Posad, Khotkovo là điểm dừng chân dễ kết hợp trong hành trình khám phá Vành đai Vàng.",
    "highlights_vi": [
        "Một trong những tu viện cổ nhất nước Nga (được nhắc tới từ năm 1308), gắn liền với gia đình Thánh Sergius thành Radonezh.",
        "Nhà thờ Pokrovsky lưu giữ thánh tích song thân của Thánh Sergius - hai Thánh Kirill và Maria thành Radonezh - điểm hành hương quan trọng.",
        "Nhà thờ Nikolsky (1900-1904) bề thế theo phong cách Nga - Byzantine với những mái vòm lớn; rất dễ kết hợp viếng cùng Trinity Lavra gần đó.",
    ],
    "practical": {
        "hours_vi": "Là nữ tu viện đang hoạt động, mở cửa hằng ngày theo giờ lễ (khoảng sáng sớm đến chiều tối); giờ có thể thay đổi theo lịch phụng vụ.",
        "ticket_vi": "Vào tu viện tự do (khuyến khích công đức tuỳ tâm).",
        "duration_vi": "Khoảng 1-1,5 giờ.",
        "best_time_vi": "Quanh năm; các ngày lễ Chính Thống giáo và những ngày hè khô ráo là thời điểm dễ chịu nhất.",
        "tips_vi": "Trang phục kín đáo khi vào nhà thờ (nữ nên mang khăn trùm đầu, mặc váy dài). Từ Moskva đi tàu điện ngoại ô tuyến Yaroslavsky đến ga Khotkovo (khoảng 1 giờ) rồi đi bộ; rất thuận tiện kết hợp tham quan Trinity Lavra ở Sergiev Posad trong cùng ngày.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": build_maps(56.25083, 37.99389, "Покровский Хотьков монастырь", "Pokrovsky Khotkov Monastery",
                       "Хотьково", "Khotkovo",
                       org_url="https://yandex.com/maps/org/pokrovskiy_khotkov_monastyr/233074031128/"),
    "official_site": "https://khotkovmonastery.ru/",
    "sources": [
        {"title": "Wikipedia (RU) — Покровский Хотьков монастырь", "url": "https://ru.wikipedia.org/wiki/Покровский_Хотьков_монастырь"},
        {"title": "Соборы.ру — Хотьково, Покровский Хотьков монастырь", "url": "https://sobory.ru/article/?object=00076"},
        {"title": "Yandex Maps — Покровский Хотьков монастырь", "url": "https://yandex.com/maps/org/pokrovskiy_khotkov_monastyr/233074031128/"},
    ],
    "tags": ["church", "monastery", "orthodox", "pilgrimage", "sergiev-posad", "khotkovo", "history", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

# ============================================================ 2) CATHEDRAL OF ARCHANGEL MICHAEL (BRONNITSY)
BRONNITSY = {
    "id": "moscow-oblast-cathedral-archangel-michael-bronnitsy",
    "slug": "cathedral-archangel-michael-bronnitsy",
    "region": REGION_SLUG,
    "region_name_vi": REGION_NAME_VI,
    "federal_district": FED,
    "name_vi": "Nhà thờ Tổng lãnh Thiên thần Mikhail và quần thể quảng trường Nhà thờ (Bronnitsy)",
    "name_ru": "Собор Михаила Архангела (Бронницы)",
    "name_en": "Cathedral of the Archangel Michael (Bronnitsy)",
    "categories": ["church", "monument"],
    "coordinates": {"lat": 55.42658, "lon": 38.26493},
    "address_vi": "Phố Sovetskaya 61, thành phố Bronnitsy, Tỉnh Moskva; cách trung tâm Moskva khoảng 50-60 km về phía đông nam theo hướng Kolomna - Ryazan (cao tốc M5).",
    "rating": None,
    "presentation_short_vi": "Nhà thờ Tổng lãnh Thiên thần Mikhail, xây dựng năm 1696-1705 dưới thời Pyotr Đại đế, là công trình cổ nhất thành phố Bronnitsy. Cùng với Nhà thờ Ierusalimskaya và tháp chuông vươn cao 73 m - tháp chuông cao nhất Tỉnh Moskva - nó tạo thành quần thể quảng trường nhà thờ nổi bật. Ngay chân tường nhà thờ là những ngôi mộ của các nhà Cách mạng Tháng Chạp (Decembrist), trong đó có Ivan Pushchin, bạn thân thời trung học của thi hào Pushkin.",
    "presentation_long_vi": "Bronnitsy là một thành phố nhỏ giàu lịch sử bên con đường thiên lý cũ đi Kolomna - Ryazan, cách Moskva chừng 50-60 km về phía đông nam, xưa nổi tiếng với trại nuôi ngựa giống của triều đình. Trái tim của phố cổ là quần thể quảng trường nhà thờ, mà trung tâm là Nhà thờ Tổng lãnh Thiên thần Mikhail - ngôi đền cổ nhất thành phố, được dựng trong các năm 1696-1705 dưới thời Pyotr Đại đế theo lối kiến trúc chuyển tiếp cuối thế kỷ 17. Bên cạnh là Nhà thờ Ierusalimskaya (thờ Ảnh Đức Mẹ Jerusalem) xây thế kỷ 19, và nổi bật hơn cả là tháp chuông vươn cao 73 mét - tháp chuông cao nhất Tỉnh Moskva và thuộc hàng cao nhất vùng Moskva, chỉ sau tháp chuông Ivan Đại đế trong Điện Kremlin. Bộ ba công trình soi bóng xuống mặt nước tạo nên khung cảnh tiêu biểu của một thị trấn tỉnh lẻ nước Nga. Bronnitsy còn được biết đến là 'thành phố của những người Tháng Chạp' (Decembrist): ngay sát tường nhà thờ là phần mộ của các nhà cách mạng quý tộc Mikhail và Ivan Fonvizin cùng Ivan Pushchin - người bạn thân thiết thời trung học Lyceum của thi hào Pushkin. Trên mộ Fonvizin đặt cây thánh giá bằng đồng, còn trên mộ Pushchin là bức tượng thiên thần theo phong cách cổ điển. Với sự hòa quyện giữa kiến trúc tôn giáo, chiều sâu lịch sử và cảnh quan yên bình, quần thể là điểm dừng chân thú vị cho chuyến đi trong ngày về hướng đông nam Moskva, có thể kết hợp với hành trình tới thành phố cổ Kolomna.",
    "highlights_vi": [
        "Nhà thờ Tổng lãnh Thiên thần Mikhail (1696-1705) - công trình cổ nhất Bronnitsy, dựng dưới thời Pyotr Đại đế.",
        "Tháp chuông cao 73 m - tháp chuông cao nhất Tỉnh Moskva, chỉ sau tháp chuông Ivan Đại đế trong Kremlin - điểm nhấn của quần thể quảng trường nhà thờ.",
        "Mộ các nhà Cách mạng Tháng Chạp M. Fonvizin, I. Fonvizin và I. Pushchin (bạn thân của Pushkin) ngay bên tường nhà thờ.",
    ],
    "practical": {
        "hours_vi": "Nhà thờ đang hoạt động, mở cửa hằng ngày theo giờ lễ; quảng trường và khu mộ có thể tham quan tự do bên ngoài.",
        "ticket_vi": "Vào tự do (khuyến khích công đức tuỳ tâm).",
        "duration_vi": "Khoảng 1 giờ để tham quan quần thể nhà thờ và khu mộ Decembrist.",
        "best_time_vi": "Quanh năm; ngày trời quang là lúc đẹp nhất để chiêm ngưỡng và chụp ảnh tháp chuông.",
        "tips_vi": "Trang phục kín đáo khi vào nhà thờ. Từ Moskva có thể đi tàu ngoại ô/xe buýt hướng Kolomna hoặc tự lái theo cao tốc M5 (khoảng 1 giờ); thuận tiện kết hợp trong hành trình đi Kolomna.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": build_maps(55.42658, 38.26493, "Собор Михаила Архангела", "Cathedral of the Archangel Michael",
                       "Бронницы", "Bronnitsy"),
    "official_site": "https://bronnicy.cerkov.ru/",
    "sources": [
        {"title": "Wikipedia (RU) — Собор Михаила Архангела (Бронницы)", "url": "https://ru.wikipedia.org/wiki/Собор_Михаила_Архангела_(Бронницы)"},
        {"title": "Соборы.ру — Бронницы, Собор Михаила Архангела", "url": "https://sobory.ru/article/?object=00378"},
    ],
    "tags": ["church", "cathedral", "bell-tower", "decembrists", "bronnitsy", "history", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

# ============================================================ 3) PEREMILOVO HEIGHTS MEMORIAL (YAKHROMA)
PEREMILOVO = {
    "id": "moscow-oblast-peremilovo-heights-memorial",
    "slug": "peremilovo-heights-memorial",
    "region": REGION_SLUG,
    "region_name_vi": REGION_NAME_VI,
    "federal_district": FED,
    "name_vi": "Đài tưởng niệm Cao điểm Peremilovo (Перемиловская высота, Yakhroma)",
    "name_ru": "Перемиловская высота",
    "name_en": "Peremilovo Heights Memorial",
    "categories": ["monument"],
    "coordinates": {"lat": 56.29802, "lon": 37.50014},
    "address_vi": "Cao điểm Peremilovo, phía đông thành phố Yakhroma, huyện (округ) Dmitrov, Tỉnh Moskva; trên gò cao bên bờ đông kênh đào Moskva, cách trung tâm Moskva khoảng 65 km về phía bắc.",
    "rating": None,
    "presentation_short_vi": "Cao điểm Peremilovo bên bờ kênh đào Moskva ở thành phố Yakhroma là một trong những địa danh biểu tượng của Trận Moskva mùa đông 1941. Cuối tháng 11 - đầu tháng 12/1941, quân Đức tiến đến đây rồi bị chặn đứng và đẩy lui - một trong những điểm xa nhất mà quân địch chạm tới trên hướng bắc thủ đô. Năm 1966, trên đỉnh đồi người ta dựng tượng đài người lính cao 28 m để tưởng niệm các anh hùng.",
    "presentation_long_vi": "Nằm trên dải gò cao ở rìa đông thành phố Yakhroma, bên bờ đông kênh đào Moskva, cách thủ đô khoảng 65 km về phía bắc, Cao điểm Peremilovo là nơi ghi dấu một trong những khoảnh khắc quyết định của Trận Moskva mùa đông năm 1941. Cuối tháng 11/1941, các mũi thọc sâu của quân Đức đã chiếm Yakhroma và vượt sang bờ đông kênh đào - đây thuộc số những điểm xa nhất mà quân xâm lược tiến tới được trên hướng bắc Moskva. Chỉ trong ít ngày, Tập đoàn quân Xung kích số 1 của Hồng quân đã phản công dữ dội, đánh bật quân địch trở lại bờ tây và mở màn cho cuộc tổng phản công giải phóng vùng Dmitrov - góp phần vào bước ngoặt đẩy lùi thế tiến công của quân phát-xít Đức ngay trước cửa ngõ thủ đô. Để tưởng niệm, năm 1966 - nhân 25 năm sự kiện - trên đỉnh cao điểm người ta dựng một tượng đài hùng vĩ cao 28 mét: phần bệ cao 15 mét đỡ pho tượng đồng người chiến sĩ cao 13 mét, tay giương súng trong tư thế xung phong, hướng về phía kẻ thù. Bên cạnh là bức tường đá granite khắc dòng chữ tưởng niệm 'Gửi những anh hùng của Trận Moskva' cùng tên các đơn vị đã chiến đấu bảo vệ vùng Dmitrov. Từ khoảng sân ngắm cảnh dưới chân tượng đài, du khách phóng tầm mắt bao quát toàn cảnh thành phố Yakhroma, mặt nước kênh đào Moskva và vùng đồng bằng trải rộng - một điểm đến vừa mang ý nghĩa lịch sử sâu sắc, vừa là nơi ngắm cảnh đẹp, đặc biệt ý nghĩa vào dịp Ngày Chiến thắng 9/5.",
    "highlights_vi": [
        "Tượng đài người lính bằng đồng cao 28 m (bệ 15 m + tượng 13 m), dựng năm 1966, trong tư thế xung phong hướng về phía kẻ thù.",
        "Địa danh gắn với bước ngoặt của Trận Moskva 1941 - nơi quân Đức bị chặn đứng và đẩy lui khỏi bờ kênh đào Moskva.",
        "Điểm ngắm toàn cảnh thành phố Yakhroma và kênh đào Moskva; bên cạnh là bức tường granite tưởng niệm các anh hùng Trận Moskva.",
    ],
    "practical": {
        "hours_vi": "Đài tưởng niệm ngoài trời, tham quan tự do mọi thời điểm trong ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30-45 phút.",
        "best_time_vi": "Mùa hè và đầu thu để ngắm cảnh đẹp; dịp Ngày Chiến thắng 9/5 có các hoạt động tưởng niệm trang trọng.",
        "tips_vi": "Từ Moskva đi tàu điện ngoại ô tuyến Savyolovsky đến ga Yakhroma rồi đi bộ/taxi lên đồi, hoặc tự lái theo cao tốc Dmitrovskoye (~1,5 giờ). Có thể kết hợp tham quan thành phố Dmitrov (Thành Dmitrov Kremlin) gần đó.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": build_maps(56.29802, 37.50014, "Перемиловская высота", "Peremilovo Heights Memorial",
                       "Яхрома", "Yakhroma",
                       org_url="https://yandex.com/maps/org/peremilovskaya_vysota/127559941976/"),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Перемиловская высота", "url": "https://ru.wikipedia.org/wiki/Перемиловская_высота"},
        {"title": "Tonkosti.ru — Перемиловская высота", "url": "https://tonkosti.ru/Перемиловская_высота"},
        {"title": "Yandex Maps — Перемиловская высота", "url": "https://yandex.com/maps/org/peremilovskaya_vysota/127559941976/"},
    ],
    "tags": ["monument", "wwii", "memorial", "viewpoint", "yakhroma", "dmitrov", "history", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [KHOTKOV, BRONNITSY, PEREMILOVO],
}


def main():
    total_added = 0
    for fname, recs in PLAN.items():
        path = os.path.join(REGIONS, fname)
        arr = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
        if not isinstance(arr, list):
            print(f"  ! {fname}: noi dung khong phai mang — bo qua.")
            continue
        existing_slugs = {p.get("slug") for p in arr}
        existing_ids = {p.get("id") for p in arr}
        to_add = []
        for r in recs:
            if r["slug"] in existing_slugs or r["id"] in existing_ids:
                print(f"  = BO QUA (da co): {fname} :: {r['slug']}")
                continue
            to_add.append(r)
        if not to_add:
            continue
        if os.path.exists(path):
            bak = path + f".bak_add_{TS}"
            with open(bak, "w", encoding="utf-8") as f:
                json.dump(arr, f, ensure_ascii=False, indent=2)
            print(f"  ~ backup: {os.path.basename(bak)}")
        arr.extend(to_add)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        total_added += len(to_add)
        print(f"  + {fname}: them {len(to_add)} dia diem -> tong {len(arr)}")
        for r in to_add:
            print(f"        - {r['name_vi']}  [{','.join(r['categories'])}]  ({r['coordinates']['lat']},{r['coordinates']['lon']})")

    print(f"\nTong da them lan nay: {total_added} dia diem.")


if __name__ == "__main__":
    main()
