# -*- coding: utf-8 -*-
"""_add_three_places_al.py — Bo sung 3 dia diem du lich Viet Nam con thieu (lan chay tu dong 2026-07-27, phien al).

TINH MOI (sau sap nhap 1/7/2025): NINH BINH.
  Nghi quyet 60-NQ/TW 2025: hop nhat 3 tinh Ha Nam + Nam Dinh + Ninh Binh -> lay ten TINH NINH BINH,
  trung tam chinh tri - hanh chinh dat tai Ninh Binh cu. Ca 3 danh thang duoi day deu nam trong pham vi
  tinh Ninh Binh MOI (khu vuc Ninh Binh cu, nay phan lon thuoc thanh pho Hoa Lu). => region_name_vi = "Ninh Binh".
  federal_district = "Mien Bac" (dong bang song Hong).

Them (file MOI data/regions/vn-ninh-binh.json):
  1) Quan the danh thang Trang An (park_garden/other)
        — Di san The gioi HON HOP dau tien & duy nhat cua Viet Nam (UNESCO 2014); thuyen nan luon qua
          hang xuyen thuy & nui da voi; gan kinh do Hoa Lu; boi canh phim 'Kong: Skull Island'.
  2) Tam Coc - Bich Dong (park_garden/church)
        — 'Ha Long tren can'; thuyen tren song Ngo Dong qua 3 hang (Hang Ca/Hai/Ba); ruong lua chin thang 5-6;
          chua co Bich Dong 3 tang ben nui Ngu Nhac.
  3) Chua Bai Dinh (church/monument)
        — quan the chua lon nhat Viet Nam; khu chua co nghin nam + khu chua moi do so; nhieu ky luc
          (tuong Phat dong dat vang ~100 tan, hanh lang La Han 500 pho tuong da, Bao Thap 13 tang).

TOA DO THAT (WGS84 thap phan, doi chieu 2026-07):
  - Trang An: 20.2567, 105.8964  (Wikipedia/UNESCO: 20 deg 15'24"N 105 deg 53'47"E)
  - Tam Coc - Bich Dong: 20.2205, 105.9351  (ben thuyen Tam Coc, xa Ninh Hai cu, TP Hoa Lu)
  - Bai Dinh: 20.2757, 105.8640  (Wikipedia: 20 deg 16'32.61"N 105 deg 51'50.4"E; gan Co do Hoa Lu)

Noi dung 3 ngon ngu (VI/EN/RU) nguyen goc, paraphrase tu nguon mo, khong sao chep nguyen van.
Chen AN TOAN: tao file neu chua co; bo qua slug/id da ton tai; sao luu truoc khi ghi.
"""
import json, os, glob, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TODAY = "2026-07-27"
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

REGION_SLUG = "vn-ninh-binh"
REGION_NAME_VI = "Ninh Bình"
FED = "Miền Bắc"


def build_maps(lat, lon, name_ru, name_en):
    """Sinh link ban do dong bo voi tools/retrofit_map_links.py (Yandex theo ten Nga; Google theo ten Anh + vung + nuoc)."""
    y_name = (name_ru or name_en or "").strip()
    yq = urllib.parse.quote(y_name)
    yandex = f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16"
    reg_en = "Ninh Binh"
    parts = [name_en]
    if reg_en.lower() not in name_en.lower():
        parts.append(reg_en)
    parts.append("Vietnam")
    gq = urllib.parse.quote(", ".join(parts))
    google = f"https://www.google.com/maps/search/?api=1&query={gq}"
    return {"yandex": yandex, "google": google}


# ============================================================ 1) TRANG AN
TRANG_AN = {
    "id": "vn-ninh-binh-trang-an",
    "slug": "trang-an",
    "region": REGION_SLUG,
    "country": "vietnam",
    "region_name_vi": REGION_NAME_VI,
    "federal_district": FED,
    "name_vi": "Quần thể danh thắng Tràng An",
    "name_ru": "Комплекс живописных ландшафтов Чанган",
    "name_en": "Trang An Scenic Landscape Complex",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 20.2567, "lon": 105.8964},
    "address_vi": "Khu du lịch sinh thái Tràng An, thành phố Hoa Lư, tỉnh Ninh Bình",
    "rating": {"value": 4.6, "count": 21000, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách đặc biệt ấn tượng với khung cảnh non nước hữu tình và cảm giác yên bình khi thuyền trôi qua các hang tối. Nhiều người khen các tuyến tham quan được tổ chức bài bản, người chèo thuyền thân thiện; một số lưu ý nên đi sớm và mang mũ nón vì ngồi thuyền khá lâu dưới nắng.",
    "presentation_short_vi": "Quần thể danh thắng Tràng An ở tỉnh Ninh Bình là Di sản Thế giới hỗn hợp đầu tiên và duy nhất của Việt Nam, được UNESCO ghi danh năm 2014. Du khách ngồi thuyền nan luồn qua những dãy núi đá vôi trùng điệp và hệ thống hang động xuyên thủy huyền ảo, xen giữa là các đền, chùa cổ gắn với kinh đô Hoa Lư xưa.",
    "presentation_short_en": "The Trang An Scenic Landscape Complex in Ninh Binh is Vietnam's first and only mixed UNESCO World Heritage Site, inscribed in 2014. Visitors glide in small sampans through a maze of towering limestone karst, flooded caves and hidden valleys dotted with ancient temples linked to the former capital of Hoa Lu.",
    "presentation_short_ru": "Комплекс живописных ландшафтов Чанган в провинции Ниньбинь — первый и единственный во Вьетнаме смешанный объект Всемирного наследия ЮНЕСКО, внесённый в список в 2014 году. Гости плывут на традиционных лодках-сампанах сквозь лабиринт известняковых карстовых скал, затопленных пещер и укромных долин со старинными храмами, связанными с бывшей столицей Хоалы.",
    "presentation_long_vi": "Nằm ở phía nam đồng bằng sông Hồng, cách Hà Nội khoảng 90 km, Quần thể danh thắng Tràng An là niềm tự hào của tỉnh Ninh Bình và là Di sản Thế giới hỗn hợp đầu tiên của Việt Nam được UNESCO công nhận năm 2014. Trên diện tích hơn 6.000 ha, Tràng An hội tụ ba giá trị đan xen: cảnh quan karst đá vôi hàng trăm triệu năm tuổi, dấu tích văn hóa của con người thời tiền sử, và kinh đô Hoa Lư của các triều Đinh, Tiền Lê và buổi đầu nhà Lý. Trải nghiệm nổi tiếng nhất là hành trình thuyền nan kéo dài vài giờ, len lỏi qua những thung lũng nước phẳng lặng, luồn dưới các hang xuyên thủy tối mờ nơi thạch nhũ rủ sát mặt nước, rồi mở ra trước mắt những vách núi dựng đứng phản chiếu xuống dòng sông trong vắt. Dọc tuyến, du khách dừng chân viếng các ngôi đền cổ thờ những nhân vật lịch sử thời Đinh – Lê, cảm nhận sự hòa quyện giữa thiên nhiên và tâm linh. Vẻ đẹp hùng vĩ mà nên thơ của Tràng An từng được chọn làm bối cảnh cho bộ phim Hollywood 'Kong: Skull Island'. Người chèo thuyền địa phương, phần lớn là phụ nữ, nhiều khi chèo bằng chân rất điêu luyện, trở thành hình ảnh khó quên. Được ví như 'Hạ Long trên cạn', Tràng An mang đến cho người ghé thăm cảm giác thanh bình, tách biệt khỏi nhịp sống hối hả.",
    "presentation_long_en": "Set at the southern edge of the Red River delta about 90 km from Hanoi, the Trang An Scenic Landscape Complex is the pride of Ninh Binh province and became Vietnam's first mixed UNESCO World Heritage Site in 2014. Spread over more than 6,000 hectares, it weaves together three intertwined values: a limestone karst landscape hundreds of millions of years old, traces of prehistoric human occupation, and the tenth-century capital of Hoa Lu, seat of the Dinh, Early Le and early Ly dynasties. The signature experience is a boat trip of several hours in a traditional sampan, drifting across mirror-calm waters, ducking through dim flooded caves where stalactites hang close to the surface, and emerging beneath sheer cliffs reflected in the clear river. Along the way passengers stop at ancient temples honouring historical figures of the Dinh-Le era, where nature and spirituality blend seamlessly. The complex's majestic yet serene scenery served as a backdrop for the Hollywood film 'Kong: Skull Island'. The local rowers, mostly women who often paddle skilfully with their feet, are an unforgettable sight. Frequently called 'Ha Long Bay on land', Trang An offers a profound sense of peace and escape from the rush of modern life, and is best explored slowly, allowing time to savour the silence between the karst peaks.",
    "presentation_long_ru": "Расположенный у южной окраины дельты Красной реки, примерно в 90 км от Ханоя, комплекс Чанган — гордость провинции Ниньбинь и первый во Вьетнаме смешанный объект Всемирного наследия ЮНЕСКО (2014 год). На площади более 6000 гектаров здесь переплетаются три ценности: известняковый карстовый ландшафт, которому сотни миллионов лет, следы доисторического человека и столица Хоалы X века — резиденция династий Динь, Ранняя Ле и ранняя Ли. Главное впечатление — прогулка на несколько часов в традиционной лодке-сампане: путешественники скользят по зеркально-гладкой воде, проходят сквозь полутёмные затопленные пещеры, где сталактиты почти касаются поверхности, и оказываются под отвесными скалами, отражающимися в прозрачной реке. По пути лодки останавливаются у старинных храмов, посвящённых историческим деятелям эпохи Динь–Ле, где природа и духовность сливаются воедино. Величественные и вместе с тем умиротворяющие пейзажи Чангана стали фоном для голливудского фильма «Конг: Остров черепа». Местные гребцы — в основном женщины, нередко искусно гребущие ногами, — производят незабываемое впечатление. Чанган, который часто называют «сухопутной бухтой Халонг», дарит гостям глубокое чувство покоя и позволяет отдохнуть от суеты современной жизни. Оптимальный маршрут занимает несколько часов и включает остановки у пещер и храмов, поэтому на поездку стоит выделить хотя бы полдня. Утренние часы особенно хороши: вода спокойна, воздух свеж, а туристов ещё немного.",
    "highlights_vi": [
        "Di sản Thế giới hỗn hợp (thiên nhiên + văn hóa) đầu tiên và duy nhất của Việt Nam (UNESCO 2014)",
        "Hành trình thuyền nan luồn qua hệ thống hang động xuyên thủy và núi đá vôi kỳ vĩ",
        "Gắn liền với kinh đô Hoa Lư xưa; từng là bối cảnh phim 'Kong: Skull Island'",
    ],
    "highlights_en": [
        "Vietnam's first and only mixed (natural + cultural) UNESCO World Heritage Site (2014)",
        "Sampan boat journey through flooded caves and dramatic limestone karst",
        "Linked to the ancient capital of Hoa Lu; a filming location for 'Kong: Skull Island'",
    ],
    "highlights_ru": [
        "Первый и единственный во Вьетнаме смешанный (природа + культура) объект ЮНЕСКО (2014)",
        "Прогулка на сампане сквозь затопленные пещеры и впечатляющие карстовые скалы",
        "Связь со старинной столицей Хоалы; место съёмок фильма «Конг: Остров черепа»",
    ],
    "practical": {
        "hours_vi": "Bến thuyền thường mở khoảng 7:00–16:00 hằng ngày (chuyến cuối xuất phát đầu giờ chiều).",
        "ticket_vi": "Vé đi thuyền tham quan tham khảo khoảng 250.000 VND/người lớn, 120.000 VND/trẻ em; giá có thể thay đổi theo tuyến.",
        "duration_vi": "Khoảng 3–4 giờ cho một tuyến thuyền.",
        "best_time_vi": "Mùa khô; đẹp nhất khoảng tháng 1–3 (mùa lễ hội) và những sáng trời quang.",
        "tips_vi": "Đi sớm để tránh nắng và đông; mang mũ, kem chống nắng, nước uống; chuẩn bị tiền lẻ bồi dưỡng người chèo; mặc áo phao suốt hành trình.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": build_maps(20.2567, 105.8964, "Комплекс живописных ландшафтов Чанган", "Trang An Scenic Landscape Complex"),
    "official_site": None,
    "sources": [
        {"title": "UNESCO World Heritage Centre — Trang An Landscape Complex", "url": "https://whc.unesco.org/en/list/1438/"},
        {"title": "Wikipedia (EN) — Trang An Scenic Landscape Complex", "url": "https://en.wikipedia.org/wiki/Tr%C3%A0ng_An_Scenic_Landscape_Complex"},
    ],
    "tags": ["unesco", "top", "nature", "boat", "cave", "viewpoint", "outdoor", "daytrip"],
    "status": "enriched",
    "last_updated": TODAY,
}

# ============================================================ 2) TAM COC - BICH DONG
TAM_COC = {
    "id": "vn-ninh-binh-tam-coc-bich-dong",
    "slug": "tam-coc-bich-dong",
    "region": REGION_SLUG,
    "country": "vietnam",
    "region_name_vi": REGION_NAME_VI,
    "federal_district": FED,
    "name_vi": "Tam Cốc – Bích Động",
    "name_ru": "Тамкок — Бичдонг",
    "name_en": "Tam Coc – Bich Dong",
    "categories": ["park_garden", "church"],
    "coordinates": {"lat": 20.2205, "lon": 105.9351},
    "address_vi": "Khu du lịch Tam Cốc – Bích Động, thành phố Hoa Lư, tỉnh Ninh Bình",
    "rating": {"value": 4.5, "count": 12000, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Nhiều du khách mê mẩn khung cảnh sông nước, ruộng lúa và khen chuyến thuyền thư thái, đậm chất đồng quê. Một số nhắc nên chuẩn bị tiền bồi dưỡng cho người chèo và thỏa thuận trước để tránh bị mời mua hàng trên thuyền; đi vào mùa lúa chín là đẹp nhất.",
    "presentation_short_vi": "Tam Cốc – Bích Động là điểm đến biểu tượng của Ninh Bình, nơi dòng sông Ngô Đồng uốn lượn giữa những cánh đồng lúa và ba hang động xuyên núi. Du khách ngồi thuyền xuôi dòng, chui qua Hang Cả, Hang Hai, Hang Ba rồi vãn cảnh chùa Bích Động cổ kính tựa lưng vào núi Ngũ Nhạc.",
    "presentation_short_en": "Tam Coc - Bich Dong is one of Ninh Binh's iconic sights, where the gentle Ngo Dong River winds between rice fields and three cave tunnels. Travellers take a rowing boat through the caves of Hang Ca, Hang Hai and Hang Ba, then visit the centuries-old Bich Dong pagoda nestled against Ngu Nhac mountain.",
    "presentation_short_ru": "Тамкок — Бичдонг — одна из визитных карточек Ниньбиня, где спокойная река Нгодонг вьётся среди рисовых полей и трёх сквозных пещер. Путешественники плывут на лодке через пещеры Хангка, Хангхай и Хангба, а затем посещают старинную пагоду Бичдонг у подножия горы Нгунгак.",
    "presentation_long_vi": "Tam Cốc – Bích Động, thuộc vùng lõi Di sản Thế giới Tràng An của tỉnh Ninh Bình, từ lâu được mệnh danh là 'Hạ Long trên cạn'. 'Tam Cốc' nghĩa là 'ba hang' — Hang Cả, Hang Hai và Hang Ba — nối tiếp nhau trên dòng sông Ngô Đồng hiền hòa. Ngồi trên chiếc thuyền nan do người dân địa phương chèo tay (và đôi khi chèo bằng chân rất khéo), du khách chầm chậm trôi giữa hai bên là vách núi đá vôi sừng sững và những thửa ruộng trải dài ven sông, rồi lần lượt luồn qua ba hang mát rượi với thạch nhũ lấp lánh. Khung cảnh đổi thay theo mùa: khoảng cuối tháng 5 đến đầu tháng 6, lúa chín nhuộm vàng cả thung lũng, tạo nên bức tranh đồng quê đẹp mê hồn thu hút giới nhiếp ảnh khắp nơi. Cách bến thuyền không xa là Bích Động — cụm chùa cổ dựng bên sườn núi Ngũ Nhạc, được đặt tên từ thế kỷ 18, gồm ba ngôi chùa xếp tầng (Hạ, Trung, Thượng) mà xưa từng được ca ngợi là 'Nam thiên đệ nhị động' (động đẹp thứ nhì trời Nam). Leo dần lên các bậc đá qua hang xuyên núi, du khách vừa vãn cảnh chùa, vừa phóng tầm mắt ra vùng non nước bao la. Tam Cốc – Bích Động vì thế là sự kết hợp trọn vẹn giữa thiên nhiên thơ mộng và chiều sâu tâm linh.",
    "presentation_long_en": "Tam Coc - Bich Dong, within the core zone of Ninh Binh's Trang An World Heritage landscape, has long been nicknamed 'Ha Long Bay on land'. 'Tam Coc' means 'three caves' — Hang Ca, Hang Hai and Hang Ba — strung one after another along the placid Ngo Dong River. Seated in a small sampan rowed by a local (often skilfully with the feet), visitors drift slowly between towering limestone cliffs and riverside paddy fields before passing through the three cool tunnels, their ceilings glittering with stalactites. The scene changes with the seasons: from late May to early June the ripening rice turns the whole valley gold, creating an enchanting rural tableau that draws photographers from around the world. A short distance from the wharf lies Bich Dong, a cluster of ancient pagodas built into the flank of Ngu Nhac mountain and named in the eighteenth century. Its three tiered temples — Lower, Middle and Upper — were once praised as 'the second finest cave under the southern sky'. Climbing the stone steps and passing through a tunnel in the rock, travellers admire the shrines while gazing over a vast panorama of water and karst. Tam Coc - Bich Dong thus offers a complete blend of poetic scenery and spiritual depth, and is loveliest in the soft light of early morning.",
    "presentation_long_ru": "Тамкок — Бичдонг, входящий в основную зону объекта Всемирного наследия Чанган в провинции Ниньбинь, давно получил прозвище «сухопутная бухта Халонг». «Тамкок» означает «три пещеры» — Хангка, Хангхай и Хангба, — которые следуют одна за другой вдоль тихой реки Нгодонг. Сидя в небольшой лодке-сампане, которой управляет местный гребец (нередко искусно гребущий ногами), гости медленно скользят между отвесными известняковыми скалами и прибрежными рисовыми полями, а затем проходят сквозь три прохладные пещеры со сверкающими сталактитами. Пейзаж меняется по сезонам: с конца мая до начала июня созревающий рис окрашивает всю долину в золото, создавая чарующую сельскую картину, которая привлекает фотографов со всего мира. Недалеко от пристани находится Бичдонг — комплекс старинных пагод, встроенных в склон горы Нгунгак и получивших название ещё в XVIII веке. Его три яруса — Нижняя, Средняя и Верхняя пагоды — некогда прославлялись как «вторая по красоте пещера под южным небом». Поднимаясь по каменным ступеням и проходя сквозь тоннель в скале, путешественники осматривают святилища и любуются широкой панорамой воды и карста. Так Тамкок — Бичдонг сочетает поэтичную природу и духовную глубину и особенно прекрасен в мягком свете раннего утра. Многие путешественники сочетают прогулку по реке с подъёмом на соседнюю смотровую точку Хангмуа, откуда вся долина видна с высоты птичьего полёта.",
    "highlights_vi": [
        "Thuyền xuôi sông Ngô Đồng, chui qua ba hang xuyên núi Hang Cả – Hang Hai – Hang Ba",
        "Ruộng lúa chín vàng rực hai bên sông vào khoảng cuối tháng 5 đến đầu tháng 6",
        "Chùa Bích Động cổ ba tầng tựa núi Ngũ Nhạc, được mệnh danh 'Nam thiên đệ nhị động'",
    ],
    "highlights_en": [
        "Boat ride on the Ngo Dong River through three rock tunnels: Hang Ca, Hang Hai, Hang Ba",
        "Golden ripening rice fields lining the river from late May to early June",
        "The tiered ancient Bich Dong pagoda, once praised as 'the second finest cave under the southern sky'",
    ],
    "highlights_ru": [
        "Прогулка по реке Нгодонг сквозь три сквозные пещеры: Хангка, Хангхай, Хангба",
        "Золотые поля созревающего риса вдоль реки с конца мая до начала июня",
        "Старинная ярусная пагода Бичдонг — «вторая по красоте пещера под южным небом»",
    ],
    "practical": {
        "hours_vi": "Bến thuyền Tam Cốc mở khoảng 7:00–16:00; chùa Bích Động mở cửa ban ngày, vào cửa tự do.",
        "ticket_vi": "Vé thắng cảnh tham khảo khoảng 120.000 VND/người và vé thuyền khoảng 150.000 VND/thuyền (mỗi thuyền 2–3 khách); giá có thể thay đổi.",
        "duration_vi": "Khoảng 2 giờ đi thuyền, thêm khoảng 1 giờ vãn cảnh chùa Bích Động.",
        "best_time_vi": "Đẹp nhất mùa lúa chín (cuối tháng 5 – đầu tháng 6) và mùa lúa xanh (khoảng tháng 4).",
        "tips_vi": "Đi buổi sáng sớm mát mẻ; mang mũ và nước; chuẩn bị tiền lẻ; có thể kết hợp leo hang Múa gần đó để ngắm toàn cảnh.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": build_maps(20.2205, 105.9351, "Тамкок — Бичдонг", "Tam Coc – Bich Dong"),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Trang An Scenic Landscape Complex", "url": "https://en.wikipedia.org/wiki/Tr%C3%A0ng_An_Scenic_Landscape_Complex"},
        {"title": "Wikipedia (VI) — Tam Cốc – Bích Động", "url": "https://vi.wikipedia.org/wiki/Tam_C%E1%BB%91c_-_B%C3%ADch_%C4%90%E1%BB%99ng"},
    ],
    "tags": ["unesco", "top", "nature", "boat", "cave", "rice-field", "viewpoint", "outdoor", "daytrip"],
    "status": "enriched",
    "last_updated": TODAY,
}

# ============================================================ 3) CHUA BAI DINH
BAI_DINH = {
    "id": "vn-ninh-binh-bai-dinh",
    "slug": "bai-dinh",
    "region": REGION_SLUG,
    "country": "vietnam",
    "region_name_vi": REGION_NAME_VI,
    "federal_district": FED,
    "name_vi": "Chùa Bái Đính",
    "name_ru": "Пагода Байдинь",
    "name_en": "Bai Dinh Pagoda",
    "categories": ["church", "monument"],
    "coordinates": {"lat": 20.2757, "lon": 105.8640},
    "address_vi": "Khu núi chùa Bái Đính, gần Cố đô Hoa Lư, tỉnh Ninh Bình",
    "rating": {"value": 4.5, "count": 26000, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách choáng ngợp trước quy mô hoành tráng và không gian trang nghiêm của quần thể. Nhiều người khuyên nên đi xe điện vì khuôn viên rất rộng, mặc đồ kín đáo và tránh dịp lễ hội đầu năm nếu ngại đông; ảnh chụp ở hành lang La Hán rất ấn tượng.",
    "presentation_short_vi": "Chùa Bái Đính ở tỉnh Ninh Bình là quần thể chùa lớn nhất Việt Nam, gồm khu chùa cổ nghìn năm trên núi và khu chùa mới đồ sộ xây từ đầu thế kỷ 21. Nơi đây nắm giữ nhiều kỷ lục như tượng Phật bằng đồng dát vàng lớn nhất và hành lang La Hán dài với 500 pho tượng đá.",
    "presentation_short_en": "Bai Dinh Pagoda in Ninh Binh is the largest Buddhist temple complex in Vietnam, combining a thousand-year-old mountain shrine with a vast new complex begun in the early 2000s. It holds many records, including the country's largest gilded bronze Buddha and a long corridor lined with 500 stone Arhat statues.",
    "presentation_short_ru": "Пагода Байдинь в провинции Ниньбинь — крупнейший буддийский храмовый комплекс во Вьетнаме, объединяющий тысячелетнее горное святилище и огромный новый ансамбль, построенный в начале XXI века. Здесь множество рекордов, включая самую большую в стране позолоченную бронзовую статую Будды и длинную галерею с 500 каменными статуями архатов.",
    "presentation_long_vi": "Nằm ở cửa ngõ Cố đô Hoa Lư, cách trung tâm tỉnh Ninh Bình khoảng 15 km, chùa Bái Đính là quần thể tâm linh lớn nhất Việt Nam và là một trong những điểm hành hương nổi tiếng bậc nhất cả nước. Quần thể gồm hai phần: khu chùa Bái Đính cổ gần nghìn năm tuổi nằm trên sườn núi với các hang động thờ Phật, thờ Mẫu và thờ thần Cao Sơn; và khu chùa mới rộng lớn được khởi công từ năm 2003, mang kiến trúc bề thế với những mái cong, cột gỗ khổng lồ và sân điện mênh mông. Bái Đính giữ nhiều kỷ lục ấn tượng: pho tượng Phật Thích Ca bằng đồng dát vàng nặng khoảng 100 tấn, bộ tượng Tam Thế bằng đồng, quả chuông đồng lớn, và đặc biệt là hành lang La Hán dài hun hút với 500 pho tượng đá được tạc tỉ mỉ, mỗi vị một dáng vẻ và biểu cảm riêng. Tháp chuông và Bảo Tháp cao mười ba tầng cho phép du khách phóng tầm mắt ra toàn cảnh núi non. Vào mỗi dịp đầu xuân, nơi đây đón hàng vạn phật tử và du khách trẩy hội. Do quần thể rất rộng, du khách có thể đi bộ hoặc dùng xe điện để tham quan, kết hợp thuận tiện với hành trình khám phá Tràng An gần đó.",
    "presentation_long_en": "Standing at the gateway to the ancient capital of Hoa Lu, about 15 km from the centre of Ninh Binh province, Bai Dinh Pagoda is the largest spiritual complex in Vietnam and one of the country's most famous places of pilgrimage. It has two distinct parts: the old Bai Dinh temple, nearly a thousand years old, set on a hillside with caves dedicated to the Buddha, to the Mother Goddesses and to the mountain deity Cao Son; and a sprawling new complex begun in 2003, built on a monumental scale with sweeping tiled roofs, giant timber columns and vast ceremonial courtyards. Bai Dinh holds an array of records: a gilded bronze statue of Sakyamuni Buddha weighing about 100 tonnes, a set of bronze Tam The (Three Ages) Buddhas, a huge bronze bell, and above all a seemingly endless corridor lined with 500 finely carved stone Arhats, each with its own posture and expression. A thirteen-storey stupa and a bell tower offer sweeping views over the surrounding mountains. Each early spring the site welcomes tens of thousands of Buddhists and visitors for its festival. Because the grounds are so extensive, guests can explore on foot or by electric buggy, and a visit combines easily with the nearby Trang An landscape. Comfortable shoes and an early start are recommended to see it before the midday crowds.",
    "presentation_long_ru": "Расположенная у ворот древней столицы Хоалы, примерно в 15 км от центра провинции Ниньбинь, пагода Байдинь — крупнейший духовный комплекс Вьетнама и одно из самых известных мест паломничества в стране. Он состоит из двух частей: старой пагоды Байдинь, которой почти тысяча лет, расположенной на склоне горы с пещерами, посвящёнными Будде, Богиням-Матерям и горному божеству Каошон; и обширного нового ансамбля, заложенного в 2003 году, монументального по масштабу, с изогнутыми черепичными крышами, гигантскими деревянными колоннами и огромными церемониальными дворами. Байдинь хранит целый ряд рекордов: позолоченную бронзовую статую Будды Шакьямуни весом около 100 тонн, набор бронзовых будд Тамтхе («Три времени»), огромный бронзовый колокол и, прежде всего, кажущуюся бесконечной галерею с 500 искусно вырезанными каменными архатами, каждый из которых имеет свою позу и выражение лица. Тринадцатиярусная ступа и колокольня открывают широкую панораму окрестных гор. Каждую раннюю весну сюда стекаются десятки тысяч буддистов и туристов на храмовый праздник. Поскольку территория очень велика, гости осматривают её пешком или на электромобиле, и такое посещение легко сочетается с расположенным рядом ландшафтом Чанган. Рекомендуются удобная обувь и ранний приезд, чтобы увидеть комплекс до полуденной жары и толп. Многие паломники приезжают сюда помолиться о здоровье и удаче, а туристов привлекают масштаб построек и панорамные виды с холма.",
    "highlights_vi": [
        "Quần thể chùa lớn nhất Việt Nam, gồm khu chùa cổ trên núi và khu chùa mới đồ sộ",
        "Nhiều kỷ lục: tượng Phật đồng dát vàng khoảng 100 tấn, chuông đồng lớn, Bảo Tháp 13 tầng",
        "Hành lang La Hán với 500 pho tượng đá, mỗi tượng một dáng vẻ khác nhau",
    ],
    "highlights_en": [
        "The largest pagoda complex in Vietnam, pairing an ancient hillside temple with a vast new complex",
        "Many records: a ~100-tonne gilded bronze Buddha, a giant bronze bell and a 13-storey stupa",
        "An Arhat corridor lined with 500 stone statues, each carved in a different pose",
    ],
    "highlights_ru": [
        "Крупнейший пагодовый комплекс Вьетнама: древний горный храм и огромный новый ансамбль",
        "Множество рекордов: позолоченный бронзовый Будда ~100 тонн, большой колокол, 13-ярусная ступа",
        "Галерея архатов с 500 каменными статуями, каждая в своей позе",
    ],
    "practical": {
        "hours_vi": "Mở cửa hằng ngày, khoảng 6:00–21:00; các điện chính tham quan ban ngày.",
        "ticket_vi": "Vào cửa tự do; các dịch vụ có phí: xe điện khoảng 30.000–60.000 VND/lượt, vé lên Bảo Tháp và vé hướng dẫn tham quan tính riêng.",
        "duration_vi": "Khoảng 3–4 giờ cho cả khu chùa cổ và chùa mới.",
        "best_time_vi": "Đầu xuân (khoảng tháng 1–3 âm lịch) để trẩy hội, hoặc ngày thường để tránh đông.",
        "tips_vi": "Mang giày êm vì phải đi bộ nhiều; nên dùng xe điện; ăn mặc kín đáo, lịch sự; kết hợp tham quan Tràng An trong cùng ngày.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": build_maps(20.2757, 105.8640, "Пагода Байдинь", "Bai Dinh Pagoda"),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Bai Dinh Pagoda", "url": "https://en.wikipedia.org/wiki/B%C3%A1i_%C4%90%C3%ADnh_Pagoda"},
        {"title": "Wikipedia (VI) — Chùa Bái Đính", "url": "https://vi.wikipedia.org/wiki/Ch%C3%B9a_B%C3%A1i_%C4%90%C3%ADnh"},
    ],
    "tags": ["top", "temple", "pilgrimage", "architecture", "viewpoint", "family", "daytrip"],
    "status": "enriched",
    "last_updated": TODAY,
}


PLAN = {
    "vn-ninh-binh.json": [TRANG_AN, TAM_COC, BAI_DINH],
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
