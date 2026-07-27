# -*- coding: utf-8 -*-
"""_add_three_places_ak.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-27, phiên ak).

ƯU TIÊN VÙNG (a): thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.
Chọn 3 danh thắng THỰC SỰ nổi tiếng còn THIẾU, đa dạng chủ đề (bảo tàng quân sự – nhà thờ/kremlin cổ –
hải đăng & tuyến «Con đường Sự sống»), phủ CẢ HAI vùng ưu tiên (2 ở Tỉnh Moskva, 1 ở Tỉnh Leningrad):

Thêm:
  1) Tỉnh Moskva (moscow-oblast): Bảo tàng Xe tăng - Thiết giáp Kubinka (huyện Odintsovo)
        (museum) — Bảo tàng Trung ương về Vũ khí & Kỹ thuật Thiết giáp; một trong những bảo tàng xe tăng lớn
        nhất thế giới, hơn 300 xe từ 14 quốc gia, gồm nhiều mẫu độc nhất (siêu tăng Đức Panzer VIII Maus,
        pháo tự hành khổng lồ Karl-Gerät, tăng thử nghiệm Object 279). Từ 2014 là chi nhánh Công viên Patriot.
  2) Tỉnh Moskva (moscow-oblast): Thành Mozhaysk Kremlin & Nhà thờ Ново-Никольский (Novo-Nikolsky)
        (church/fortress/monument) — cụm nhà thờ trên đồi Nikolskaya/Sobornaya, nơi từng là kremlin đá trắng
        Mozhaysk. Nhà thờ Ново-Никольский (1802-1814) mang phong cách «Gothic Nga» (giả Gothic) đỏ rực, nổi
        bật từ xa; gắn với hình tượng «Nikola Mozhaysky» (Thánh Nikolai cầm gươm và thành trì).
  3) Tỉnh Leningrad (leningrad-oblast): Hải đăng Osinovets & Bảo tàng «Con đường Sự sống» (huyện Vsevolozhsk)
        (monument/museum) — ngọn hải đăng đá cao ~70 m (một trong những hải đăng cao nhất nước Nga, xây
        1905-1910) trên mũi Osinovets bên hồ Ladoga; là điểm mốc bờ tây của «Con đường Sự sống» tiếp tế
        Leningrad thời phong toả 1941-1944. Gần đó là Bảo tàng «Con đường Sự sống» (chi nhánh Bảo tàng Hải quân).

ĐỐI CHIẾU TRÁNH TRÙNG (đã quét slug + toàn văn JSON các file vùng, non-bak; tổng 929 bản ghi trước khi thêm):
  - moscow-oblast.json (36 bản ghi): CHƯA có 'kubinka-tank-museum', 'mozhaysk', 'nikolsky-cathedral-mozhaysk'.
    ('kubinka' trước đây chỉ xuất hiện trong ĐỊA CHỈ bản ghi armed-forces-cathedral = Công viên Patriot —
     KHÔNG phải bảo tàng xe tăng này; hai đối tượng khác nhau, không trùng.)
  - leningrad-oblast.json (19 bản ghi): CHƯA có 'osinovets' hay 'lighthouse'.
    (Bản ghi 'broken-ring-memorial' cũng thuộc «Con đường Sự sống» nhưng là ĐÀI TƯỞNG NIỆM «Vòng tròn Bị
     phá vỡ» ở Kokkorevo/Vaganovo trên tuyến đường bộ - KHÁC hải đăng Osinovets ở CẢNG BỜ HỒ nơi khởi đầu
     tuyến đường thuỷ, cách nhau vài km; không trùng.)
  - Gatchina (Cung điện Gatchina + Cung điện Priory) đã ở saint-petersburg.json - không liên quan 3 mục này.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG sao chép/dịch nguyên văn), có ghi nguồn.

TOẠ ĐỘ THẬT — đối chiếu chéo ≥2 nguồn (thập phân WGS84), 2026-07:
  - Центральный музей бронетанкового вооружения и техники (Кубинка), Одинцовский р-н:  55.566850, 36.715750
        (Wikipedia EN 55°33′54″N 36°42′56″E ≈ 55.565,36.7156; MAMADO/2ГИС N55°34.011' E36°42.945'
         = 55.56685,36.71575 → khớp; ~64 km tây Moskva)
  - Ново-Никольский собор / Можайский кремль (Соборная/Никольская гора), г. Можайск:   55.504528, 36.015673
        (places.moscow «Соборная гора» 55.504528,36.015673; Yandex org 1337925585; ~110 km tây Moskva)
  - Осиновецкий маяк, мыс Осиновец, пос. Ладожское Озеро, Всеволожский р-н, Лен. обл.: 60.118765, 31.080604
        (Wikipedia EN «Osinovetsky Light» 60°7′7.6″N 31°4′49.6″E = 60.118778,31.080444; bolshayastrana
         60.118765,31.080604 → khớp; bờ tây hồ Ladoga, ~50 km đông bắc Saint Petersburg)
  Kiểm tra thứ tự lat/lon: lat 55-60 (∈41-70), lon 31-37 (∈19-180), KHÔNG đảo; đều nằm đúng phạm vi vùng.

LINK BẢN ĐỒ dạng TRỎ-ĐỊA-ĐIỂM:
  - Record 1 (Kubinka): URL TRANG TỔ CHỨC Yandex (org 1000296108) — chính xác nhất.
  - Record 2 (Mozhaysk kremlin): URL TRANG TỔ CHỨC Yandex (org 1337925585, «Ново-Никольский собор») — chính xác nhất.
  - Record 3 (Osinovets): helper maps_text (text=tên+địa danh, ll=toạ độ đã kiểm chứng) — mở đúng thẻ địa
        điểm hải đăng (hải đăng là công trình hàng hải, không có org-card riêng ổn định).
  Cả 3 vẫn LƯU coordinates{lat,lon} chuẩn cho bản đồ nội bộ/GIS.

Chạy:  python3 tools/_add_three_places_ak.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"


def _google(name_en, region_en):
    parts = [name_en]
    if region_en.lower() not in name_en.lower():
        parts.append(region_en)
    parts.append("Russia")
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(", ".join(parts))


def maps_text(name_ru, region_ru, name_en, region_en, lat, lon):
    """Trỏ thẳng tới địa điểm bằng tên + canh giữa theo toạ độ (khớp retrofit_map_links.py)."""
    yq = urllib.parse.quote(f"{name_ru}, {region_ru}")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": _google(name_en, region_en),
    }


# ============================================================ RECORD 1
KUBINKA_TANK_MUSEUM = {
    "id": "moscow-oblast-kubinka-tank-museum",
    "slug": "kubinka-tank-museum",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng Xe tăng - Thiết giáp Kubinka (Bảo tàng Trung ương về Vũ khí và Kỹ thuật Thiết giáp)",
    "name_ru": "Центральный музей бронетанкового вооружения и техники (Кубинка)",
    "name_en": "Kubinka Tank Museum (Central Museum of Armored Weapons and Equipment)",
    "categories": ["museum"],
    "coordinates": {"lat": 55.566850, "lon": 36.715750},
    "address_vi": (
        "Кубинка-1 (Kubinka-1), huyện Odintsovo, Tỉnh Moskva; nằm trong khu vực trường bắn - thử nghiệm thiết "
        "giáp Kubinka, cách trung tâm Moskva khoảng 64 km về phía tây theo đường cao tốc M1 «Belarus». Nay là "
        "một phân khu (Trung tâm Kỹ thuật) của Công viên Quân sự - Yêu nước «Patriot»."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Bảo tàng Xe tăng Kubinka là một trong những bảo tàng thiết giáp lớn và nổi tiếng nhất thế giới, trưng "
        "bày hơn 300 xe tăng, xe bọc thép và phương tiện chiến đấu đến từ khoảng 14 quốc gia, trong đó có gần "
        "60 mẫu độc nhất vô nhị không nơi nào khác còn giữ được. Bảo tàng ra đời từ bộ sưu tập của trường thử "
        "nghiệm thiết giáp tuyệt mật ở Kubinka - nơi Hồng quân từng thử nghiệm mọi thiết kế tăng mới cũng như "
        "các xe chiến lợi phẩm. Điểm nhấn là những «quái vật» huyền thoại như siêu tăng Đức Panzer VIII «Maus» "
        "nặng nhất lịch sử, pháo tự hành khổng lồ Karl-Gerät và tăng thử nghiệm Liên Xô Object 279."
    ),
    "presentation_long_vi": (
        "Lịch sử bảo tàng bắt đầu năm 1938, khi một «Bảo tàng xe chiến đấu» được lập ra trên cơ sở vài chục "
        "cỗ máy tại trường thử nghiệm thiết giáp Kubinka. Trong nhiều thập niên, đây là cơ sở quân sự tuyệt mật: "
        "mọi mẫu tăng và xe bọc thép do các viện thiết kế Liên Xô chế tạo đều được đưa về Kubinka để thử nghiệm, "
        "bên cạnh đó là hàng loạt xe nước ngoài thu được làm chiến lợi phẩm qua các cuộc chiến khắp thế giới để "
        "nghiên cứu điểm mạnh - điểm yếu. Bảo tàng mở cửa rộng rãi cho công chúng từ những năm 1970 và dần trở "
        "thành điểm đến quen thuộc của người yêu lịch sử quân sự. Bộ sưu tập trải trên các gian trưng bày trong "
        "nhà và khu ngoài trời rộng nhiều héc-ta, phân theo chủ đề: tăng hạng nặng và pháo tự hành Liên Xô, tăng "
        "hạng nhẹ và thiết giáp chở quân, xe chiến đấu bộ binh, cùng khu xe thiết giáp nước ngoài (Đức, Mỹ, Anh, "
        "Pháp, Nhật…). Nổi tiếng nhất là các hiện vật hiếm có: siêu tăng Đức Panzer VIII «Maus» - xe tăng nặng "
        "nhất từng được chế tạo, pháo cối tự hành hạng nặng Karl-Gerät, và nguyên mẫu tăng Liên Xô Object 279 với "
        "thân bốn xích đặc trưng. Từ năm 2014, bảo tàng trở thành một bộ phận của Công viên Quân sự - Yêu nước "
        "«Patriot», nơi kết hợp trưng bày lịch sử với các không gian triển lãm kỹ thuật quân sự hiện đại. Do vẫn "
        "nằm trong khuôn viên đơn vị quân đội, khách tham quan (đặc biệt là người nước ngoài) nên chuẩn bị giấy "
        "tờ tuỳ thân và lưu ý các quy định an ninh khi vào cửa."
    ),
    "highlights_vi": [
        "Bộ sưu tập hơn 300 xe tăng và xe bọc thép từ khoảng 14 quốc gia, với gần 60 mẫu độc nhất không nơi nào khác còn giữ - một trong những bảo tàng thiết giáp lớn nhất thế giới.",
        "Những «quái vật» huyền thoại: siêu tăng Đức Panzer VIII «Maus» nặng nhất lịch sử, pháo tự hành khổng lồ Karl-Gerät và nguyên mẫu tăng Liên Xô Object 279.",
        "Gốc gác từ trường thử nghiệm thiết giáp tuyệt mật Kubinka; từ năm 2014 là chi nhánh của Công viên «Patriot» - kết hợp lịch sử và kỹ thuật quân sự hiện đại.",
    ],
    "practical": {
        "hours_vi": "Thường mở cửa từ Thứ Tư đến Chủ Nhật, khoảng 10:00-18:00 (nghỉ Thứ Hai, Thứ Ba); lịch có thể thay đổi theo mùa và theo quy định của Công viên Patriot, nên kiểm tra trước khi đến.",
        "ticket_vi": "Có thu phí; vé vào các khu trưng bày dao động khoảng vài trăm rúp, có thể mua vé riêng theo từng khu. Tour có hướng dẫn (nhất là bằng tiếng Anh) đắt hơn đáng kể. Trẻ nhỏ thường được miễn phí. Giá thay đổi theo thời điểm.",
        "duration_vi": "Khoảng 2-4 giờ để đi hết các gian trưng bày xe tăng; sẽ lâu hơn nếu kết hợp tham quan các khu khác của Công viên Patriot.",
        "best_time_vi": "Quanh năm (phần lớn hiện vật ở trong nhà); dịp Ngày Chiến thắng (9/5) hay Ngày Lính tăng có nhiều sự kiện nhưng rất đông khách.",
        "tips_vi": "Từ Moskva có thể đi tàu ngoại ô (elektrichka) tuyến Belorussky đến ga Kubinka-1 rồi bắt xe địa phương, hoặc tự lái theo cao tốc M1 (~1-1,5 giờ). Do bảo tàng nằm trong khu quân sự, hãy mang theo giấy tờ tuỳ thân (khách nước ngoài nên có bản sao hộ chiếu); vũ khí và đồ uống có cồn bị cấm mang vào. Khu trưng bày rộng và tách biệt nên chuẩn bị giày đi bộ thoải mái.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": {
        # Task ƯU TIÊN URL trang tổ chức Yandex khi tra được org-id (chính xác nhất về vị trí thẻ địa điểm).
        "yandex": "https://yandex.com/maps/org/tankovy_muzey/1000296108/",
        "google": _google("Kubinka Tank Museum", "Kubinka, Odintsovsky District, Moscow Oblast"),
    },
    "official_site": "https://tankmuseum.ru/",
    "sources": [
        {"title": "Wikipedia (EN) — Kubinka Tank Museum", "url": "https://en.wikipedia.org/wiki/Kubinka_Tank_Museum"},
        {"title": "Wikipedia (RU) — Бронетанковый музей в Кубинке", "url": "https://ru.wikipedia.org/wiki/Бронетанковый_музей_в_Кубинке"},
        {"title": "Yandex Maps — Танковый музей (Кубинка)", "url": "https://yandex.com/maps/org/tankovy_muzey/1000296108/"},
    ],
    "tags": ["museum", "military", "tanks", "armor", "patriot-park", "kubinka", "history", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

# ============================================================ RECORD 2
MOZHAYSK_KREMLIN = {
    "id": "moscow-oblast-mozhaysk-kremlin",
    "slug": "mozhaysk-kremlin",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Thành Mozhaysk Kremlin & Nhà thờ Ново-Никольский (Novo-Nikolsky)",
    "name_ru": "Можайский кремль (Ново-Никольский собор)",
    "name_en": "Mozhaysk Kremlin (New St. Nicholas Cathedral)",
    "categories": ["church", "fortress", "monument"],
    "coordinates": {"lat": 55.504528, "lon": 36.015673},
    "address_vi": (
        "Đồi Nikolskaya (Соборная/Никольская гора), phố Borodinskaya, thành phố Mozhaysk, Tỉnh Moskva; nằm trên "
        "gò cao bên sông Mozhaika, cách trung tâm Moskva khoảng 110 km về phía tây theo đường Smolensk cổ (cao "
        "tốc M1)."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Trên đồi Nikolskaya bên rìa tây thành phố Mozhaysk từng sừng sững kremlin đá trắng - pháo đài canh giữ "
        "cửa ngõ phía tây Moskva. Thành cổ đã bị tháo dỡ cuối thế kỷ 18, nhưng nơi đây vẫn còn cụm nhà thờ ấn "
        "tượng, trung tâm là Nhà thờ Ново-Никольский (Novo-Nikolsky, xây 1802-1814) mang phong cách «Gothic Nga» "
        "(giả Gothic) với gạch đỏ, cửa nhọn và tháp vút cao trông thấy từ xa. Cụm di tích còn lưu giữ dấu vết "
        "cổng - tháp Nikolskaya và một đoạn tường thành, gắn với hình tượng nổi tiếng «Nikola Mozhaysky» - Thánh "
        "Nikolai một tay cầm gươm, một tay nâng mô hình thành trì."
    ),
    "presentation_long_vi": (
        "Mozhaysk là một trong những thành trấn cổ trấn giữ tuyến đường Smolensk - cửa ngõ phía tây dẫn về Moskva, "
        "nên từ sớm đã có kremlin phòng thủ. Ban đầu là thành gỗ, đến thế kỷ 17 được xây lại bằng đá trắng với "
        "tường và tháp kiên cố. Khi biên giới nước Nga đã lùi xa về phía tây, pháo đài mất vai trò quân sự và bị "
        "tháo dỡ vào những năm 1770-1780; vật liệu được tận dụng cho các công trình khác. Trên nền cũ, giữa các "
        "nhà thờ của kremlin, người ta dựng Nhà thờ Ново-Никольский trong giai đoạn 1802-1814 theo phong cách "
        "giả Gothic (thường gọi là «Gothic Nga») - một trong những nhà thờ đẹp và độc đáo bậc nhất vùng ngoại vi "
        "Moskva, với khối gạch đỏ, các chi tiết trắng, cửa sổ và tháp nhọn vươn cao. Nhà thờ được dựng ngay trên "
        "phần còn lại của cổng - tháp Nikolskaya cùng nhà thờ trên cổng cũ, nên vẫn ôm trong mình dấu tích tường "
        "thành của kremlin xưa. Bên cạnh là nhà thờ «cũ» (Petropavlovskaya / Nikolsky cổ) theo phong cách Nga - "
        "Byzantine. Mozhaysk cũng là quê hương của hình tượng «Nikola Mozhaysky» trứ danh - tượng - biểu tượng "
        "Thánh Nikolai một tay cầm gươm, một tay nâng mô hình thành có tường, được xem như vị thánh bảo hộ thành. "
        "Trong Thế chiến II, Mozhaysk từng bị chiếm đóng và giao tranh ác liệt (1941-1942), cụm nhà thờ hư hại "
        "nhưng sau đó được trùng tu. Ngày nay Ново-Никольский собор là nhà thờ đang hoạt động thuộc giáo phận "
        "Odintsovo, đồng thời là di sản kiến trúc nổi bật và điểm ngắm cảnh đẹp nhìn ra thành phố và vùng phụ cận."
    ),
    "highlights_vi": [
        "Nhà thờ Ново-Никольский (1802-1814) phong cách «Gothic Nga» đỏ rực với cửa nhọn và tháp vươn cao - một trong những nhà thờ độc đáo nhất vùng ngoại vi Moskva, nhìn thấy từ xa.",
        "Đồi Nikolskaya - nền của kremlin đá trắng Mozhaysk xưa; còn lưu dấu cổng - tháp Nikolskaya và một đoạn tường thành cổ được tích hợp vào nhà thờ.",
        "Cái nôi của hình tượng «Nikola Mozhaysky» - Thánh Nikolai cầm gươm và nâng mô hình thành trì, vị thánh bảo hộ nổi tiếng của thành phố.",
    ],
    "practical": {
        "hours_vi": "Là nhà thờ đang hoạt động, thường mở cửa hằng ngày theo giờ lễ (sáng sớm đến chiều tối); khu di tích trên đồi có thể tham quan tự do bên ngoài. Giờ lễ thay đổi theo lịch phụng vụ.",
        "ticket_vi": "Vào nhà thờ và khu đồi Nikolskaya tự do (khuyến khích công đức tuỳ tâm).",
        "duration_vi": "Khoảng 1-1,5 giờ để tham quan cụm nhà thờ và ngắm cảnh từ đồi; lâu hơn nếu kết hợp dạo phố cổ Mozhaysk.",
        "best_time_vi": "Quanh năm; ngày nắng đẹp là lúc lý tưởng để chiêm ngưỡng và chụp ảnh khối nhà thờ Gothic đỏ trên nền trời.",
        "tips_vi": "Trang phục kín đáo khi vào nhà thờ (nữ nên mang khăn trùm đầu). Từ Moskva đi tàu tuyến Belorussky đến ga Mozhaysk rồi đi bộ/xe buýt khoảng 2 km lên đồi, hoặc tự lái theo cao tốc M1 (~1,5 giờ). Có thể kết hợp trong hành trình đến chiến địa Borodino gần đó.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": {
        # Task ƯU TIÊN URL trang tổ chức Yandex khi tra được org-id (chính xác nhất về vị trí thẻ địa điểm).
        "yandex": "https://yandex.com/maps/org/novo_nikolskiy_sobor/1337925585/",
        "google": _google("Novo-Nikolsky Cathedral (Mozhaysk Kremlin)", "Mozhaysk, Moscow Oblast"),
    },
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Никольский собор (Можайск)", "url": "https://ru.wikipedia.org/wiki/Никольский_собор_(Можайск)"},
        {"title": "Соборы.ру — Можайск, Собор Николая Чудотворца", "url": "https://sobory.ru/article/?object=02335"},
        {"title": "Tourister.ru — Можайский кремль", "url": "https://www.tourister.ru/world/europe/russia/city/mozhaysk/placeofinterest/36820"},
        {"title": "Yandex Maps — Ново-Никольский собор", "url": "https://yandex.com/maps/org/novo_nikolskiy_sobor/1337925585/"},
    ],
    "tags": ["church", "cathedral", "kremlin", "russian-gothic", "orthodox", "mozhaysk", "history", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

# ============================================================ RECORD 3
OSINOVETS_LIGHTHOUSE = {
    "id": "leningrad-oblast-osinovets-lighthouse",
    "slug": "osinovets-lighthouse",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Hải đăng Osinovets & Bảo tàng «Con đường Sự sống»",
    "name_ru": "Осиновецкий маяк (и музей «Дорога жизни»)",
    "name_en": "Osinovets Lighthouse & Road of Life Museum",
    "categories": ["monument", "museum"],
    "coordinates": {"lat": 60.118765, "lon": 31.080604},
    "address_vi": (
        "Мыс Осиновец (mũi Osinovets), làng ga Ladozhskoye Ozero, huyện Vsevolozhsk, Tỉnh Leningrad; nằm trên "
        "bờ tây hồ Ladoga, cuối tuyến «Дорога жизни» (Con đường Sự sống), cách trung tâm Saint Petersburg "
        "khoảng 50 km về phía đông bắc."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Hải đăng Osinovets là ngọn hải đăng đá cao khoảng 70 m vươn lên trên mũi Osinovets bên bờ tây hồ Ladoga "
        "- một trong những hải đăng cao nhất nước Nga và châu Âu, hoạt động từ đầu thế kỷ 20 và vẫn dẫn đường cho "
        "tàu bè đến nay. Nơi đây mang ý nghĩa lịch sử đặc biệt: trong thời kỳ Leningrad bị phong toả (1941-1944), "
        "vùng bờ hồ quanh hải đăng chính là điểm mốc bờ tây của «Con đường Sự sống» - tuyến tiếp tế và sơ tán "
        "duy nhất băng qua hồ Ladoga (bằng tàu thuyền mùa hè, bằng đường băng trên mặt hồ đóng băng mùa đông). "
        "Ngay gần đó là Bảo tàng «Con đường Sự sống» với toà nhà hiện đại hình khối băng, trưng bày hiện vật về "
        "chiến công cứu thành phố."
    ),
    "presentation_long_vi": (
        "Quyết định xây hải đăng trên đoạn bờ nguy hiểm này của hồ Ladoga được đưa ra năm 1905; công trình hoàn "
        "thành trong những năm sau đó, tạo nên tháp đèn cao chừng 70 m với hàng trăm bậc thang xoắn ốc bên trong. "
        "Bản thân hải đăng là công trình hàng hải đang vận hành nên thường chỉ được chiêm ngưỡng từ bên ngoài, "
        "song dáng tháp sọc vươn cao trên nền hồ mênh mông đã trở thành một trong những hình ảnh biểu tượng của "
        "vùng Ladoga. Điều khiến Osinovets nổi tiếng nhất là vai trò trong Chiến tranh Vệ quốc Vĩ đại. Từ tháng "
        "9/1941, khi vòng vây siết chặt quanh Leningrad, hồ Ladoga trở thành hành lang sinh tử: các đoàn tàu, sà "
        "lan chở lương thực, nhiên liệu, đạn dược vượt hồ cập bờ tây ở khu vực cảng Osinovets ngay cạnh hải đăng, "
        "rồi theo đường sắt vào thành phố; chiều ngược lại đưa hàng trăm nghìn dân thường, nhất là trẻ em, ra "
        "khỏi vòng vây. Mùa đông, khi mặt hồ đóng băng, tuyến này biến thành «con đường băng» cho xe tải chạy - "
        "cả tuyến được người dân gọi bằng cái tên đầy xúc động: «Дорога жизни» (Con đường Sự sống). Ngày nay, "
        "bên cạnh hải đăng là Bảo tàng «Con đường Sự sống» - chi nhánh của Bảo tàng Hải quân Trung ương; toà nhà "
        "trưng bày hiện đại (khánh thành năm 2016) được tạo hình như một khối băng, giới thiệu tàu thuyền, xe cộ, "
        "máy bay và câu chuyện về những con người đã giữ cho tuyến đường sống còn hoạt động. Cùng cụm di tích còn "
        "có nhà ga - đài tưởng niệm «Ладожское Озеро». Osinovets vì thế vừa là một thắng cảnh thiên nhiên - kiến "
        "trúc bên hồ Ladoga, vừa là địa chỉ tưởng niệm quan trọng bậc nhất gắn với cuộc phong toả Leningrad."
    ),
    "highlights_vi": [
        "Ngọn hải đăng đá cao khoảng 70 m (một trong những hải đăng cao nhất nước Nga) vươn trên mũi Osinovets bên hồ Ladoga - biểu tượng và điểm chụp ảnh nổi tiếng, vẫn đang hoạt động.",
        "Điểm mốc bờ tây của «Con đường Sự sống» - tuyến tiếp tế và sơ tán băng qua hồ Ladoga cứu Leningrad trong thời kỳ phong toả 1941-1944.",
        "Bảo tàng «Con đường Sự sống» (chi nhánh Bảo tàng Hải quân) với toà nhà hình khối băng khánh thành năm 2016, trưng bày tàu thuyền, xe cộ và hiện vật lịch sử ngay bên hải đăng.",
    ],
    "practical": {
        "hours_vi": "Hải đăng có thể ngắm từ bên ngoài bất cứ lúc nào (không mở cửa vào trong vì là công trình hàng hải đang vận hành). Bảo tàng «Con đường Sự sống» thường mở cửa các ngày trong tuần (thường nghỉ Thứ Hai), giờ có thể thay đổi theo mùa - nên kiểm tra trước khi đến.",
        "ticket_vi": "Ngắm hải đăng và ra bờ hồ miễn phí. Vé vào Bảo tàng «Con đường Sự sống» ở mức phải chăng; giá thay đổi theo thời điểm và có thể miễn/giảm cho một số đối tượng.",
        "duration_vi": "Khoảng 1,5-3 giờ cho cả cụm: bờ hồ - hải đăng và tham quan bảo tàng.",
        "best_time_vi": "Mùa hè và đầu thu để dạo bờ hồ Ladoga và chụp ảnh hải đăng; ngày 27/1 (kỷ niệm phá vây Leningrad) và 9/5 có các sự kiện tưởng niệm trang nghiêm.",
        "tips_vi": "Từ Saint Petersburg thuận tiện nhất là đi tàu ngoại ô (elektrichka) từ ga Finlyandsky đến ga cuối «Ладожское Озеро», rồi đi bộ ra bờ hồ và bảo tàng; hoặc tự lái theo đường «Дорога жизни». Không trèo/không vào trong hải đăng. Có thể kết hợp với đài tưởng niệm «Vòng tròn Bị phá vỡ» (Broken Ring) trên cùng tuyến Con đường Sự sống.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text(
        "Осиновецкий маяк", "посёлок Ладожское Озеро, Всеволожский район, Ленинградская область",
        "Osinovets Lighthouse", "Vsevolozhsky District, Leningrad Oblast",
        60.118765, 31.080604,
    ),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Osinovetsky Light", "url": "https://en.wikipedia.org/wiki/Osinovetsky_Light"},
        {"title": "Большая Страна — Осиновецкий маяк: страж «Дороги жизни»", "url": "https://bolshayastrana.com/dostoprimechatelnosti/leningradskaya-oblast/osinoveckij-mayak-740"},
        {"title": "Tourister.ru — Осиновецкий маяк на Ладожском озере", "url": "https://www.tourister.ru/world/europe/russia/city/vsevolozhsk/placeofinterest/36956"},
    ],
    "tags": ["lighthouse", "monument", "museum", "road-of-life", "lake-ladoga", "wwii", "siege-of-leningrad", "vsevolozhsk", "leningrad-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


# ------------------------------------------------------------------ PLAN
PLAN = {
    "moscow-oblast.json": [KUBINKA_TANK_MUSEUM, MOZHAYSK_KREMLIN],
    "leningrad-oblast.json": [OSINOVETS_LIGHTHOUSE],
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
