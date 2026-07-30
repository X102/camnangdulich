# -*- coding: utf-8 -*-
"""_add_places_volgograd_20260729_020000.py — VÙNG: Tỉnh Volgograd (Волгоградская область)
(lần chạy tự động 2026-07-29, Vùng Nam / Южный федеральный округ).

Bối cảnh: volgograd.json hiện có 7 địa điểm (Мамаев курган + «Родина-мать зовёт!»,
музей-панорама «Сталинградская битва», мельница Гергардта, «Старая Сарепта»,
Центральная набережная, Волго-Донской канал + памятник Ленину, Волжская ГЭС).
Bổ sung 26 địa điểm THẬT SỰ nổi tiếng CÒN THIẾU → đưa vùng lên 33. TRÁNH trùng 7 điểm trên
(đặc biệt KHÔNG thêm lại Мамаев курган/Родина-мать, панорама, мельница Гергардта, набережная).

Phân bố loại hình (26 bản ghi mới):
- monument (3): Дом Павлова, Тополь на Аллее Героев, пароход-музей «Гаситель».
- square_street (4): площадь Павших Борцов, Аллея Героев, площадь Ленина, площадь Ленина (Волжский).
- church (4): собор Александра Невского, Казанский собор, храм Иоанна Предтечи,
  храм Всех Святых на Мамаевом кургане.
- museum (5): краеведческий музей, музей ИЗО им. Машкова, музей «Память», мемориально-
  исторический музей, Камышинский историко-краеведческий музей.
- theatre (3): Новый Экспериментальный Театр (НЭТ), музыкальный театр, театр кукол.
- other (4): планетарий, «Волгоград Арена», речной вокзал, озеро Эльтон.
- bridge (1): Волгоградский («танцующий») мост.
- park_garden (1): Комсомольский сад.
- other/monument (1): железнодорожный вокзал Волгоград-1 (памятник сталинской архитектуры).

TOẠ ĐỘ — ru.wikipedia / Wikidata / 2GIS / Яндекс.Карты / sobory.ru (2026-07-29). Phạm vi tỉnh
Volgograd: lat ~47.5–51.2, lon ~41.1–47.5 (TP Волгоград ~48.71,44.51; Волжский ~48.79,44.77;
Камышин ~50.09,45.40; озеро Эльтон ~49.13,46.67). Tất cả toạ độ trong phạm vi, lat luôn > lon,
KHÔNG đảo lat/lon. Cụm trung tâm Волгоград (Дом Павлова, пл. Ленина, музеи, театры) nằm sát nhau
trong lõi lịch sử ~1 km nên toạ độ gần nhau là ĐÚNG thực tế.

GHI CHÚ: BỎ QUA vì đã có / trùng: Мамаев курган + «Родина-мать», музей-панорама «Сталинградская
битва», мельница Гергардта, «Старая Сарепта», Центральная набережная, Волго-Донской канал, Волжская
ГЭС. Các điểm thiên nhiên rủi ro toạ độ (Столбичи, Камышинские «Уши», Александровский грабен —
nhiều nguồn mâu thuẫn vị trí chính xác) KHÔNG đưa vào để tránh bịa; chỉ giữ озеро Эльтон (toạ độ
chắc chắn). KHÔNG bịa toạ độ, KHÔNG nhồi.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn).

Chạy:  python3 tools/_add_places_volgograd_20260729_020000.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "volgograd"
REGION_NAME_VI = "Tỉnh Volgograd"
FD = "Vùng Nam"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def maps_org(yandex_org_url, name_en, city_en):
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": yandex_org_url,
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def p(hours, ticket, duration, best, tips):
    return {"hours_vi": hours, "ticket_vi": ticket, "duration_vi": duration,
            "best_time_vi": best, "tips_vi": tips}


def rec(slug, name_vi, name_ru, name_en, categories, lat, lon, address_vi,
        short, long, highlights, practical, sources, tags, maps,
        official_site=None):
    return {
        "id": f"{REGION}-{slug}",
        "slug": slug,
        "region": REGION,
        "region_name_vi": REGION_NAME_VI,
        "federal_district": FD,
        "name_vi": name_vi,
        "name_ru": name_ru,
        "name_en": name_en,
        "categories": categories,
        "coordinates": {"lat": lat, "lon": lon},
        "address_vi": address_vi,
        "rating": {"value": None, "count": None, "source": None, "as_of": None},
        "review_summary_vi": "",
        "presentation_short_vi": short,
        "presentation_long_vi": long,
        "highlights_vi": highlights,
        "practical": practical,
        "photo": None,
        "photo_credit": None,
        "maps": maps,
        "official_site": official_site,
        "sources": sources,
        "tags": tags,
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia",
    }


RECORDS = []

# ============================ ĐÀI TƯỞNG NIỆM & QUẢNG TRƯỜNG ============================

# 1) Дом Павлова ------------------------------------------------------------------
RECORDS.append(rec(
    "pavlov-house",
    "Nhà Pavlov (phiên âm: Đôm Páp-lô-va)",
    "Дом Павлова",
    "Pavlov's House",
    ["monument"],
    48.71694, 44.53250,
    "Phố Sovetskaya 39, cạnh Quảng trường Lenin, quận Trung tâm, thành phố Volgograd, tỉnh Volgograd, Nga",
    "Nhà Pavlov là toà chung cư bốn tầng mà một nhóm chiến sĩ Hồng quân dưới sự chỉ huy của trung sĩ Yakov Pavlov đã cố thủ suốt gần hai tháng trong Trận Stalingrad. Trở thành biểu tượng của tinh thần kháng cự bất khuất, ngày nay bức tường đầu hồi được giữ lại như một đài tưởng niệm.",
    "Nhà Pavlov (Дом Павлова) là một trong những biểu tượng cảm động nhất của Trận Stalingrad. Vào mùa thu năm 1942, một nhóm nhỏ chiến sĩ Hồng quân do trung sĩ Yakov Pavlov và sau đó là trung uý Ivan Afanasyev chỉ huy đã biến toà chung cư bốn tầng bình thường này thành một pháo đài, cầm cự suốt khoảng 58 ngày đêm trước các đợt tấn công dồn dập của quân Đức. Toà nhà nằm ở vị trí then chốt trấn giữ quảng trường và con đường xuống bờ sông Volga, nên việc giữ được nó có ý nghĩa chiến thuật lớn. Người ta thường nhắc lại câu nói rằng quân Đức tổn thất trước ngôi nhà này còn nhiều hơn khi đánh chiếm một số thành phố châu Âu. Sau chiến tranh, toà nhà được phục dựng và trở thành một trong những công trình đầu tiên được khôi phục ở Stalingrad; bức tường đầu hồi hướng ra Quảng trường Lenin được gắn phù điêu tưởng niệm bằng gạch, ghi danh những người bảo vệ. Ngày nay Nhà Pavlov đứng cạnh khu di tích nhà máy xay Gergardt và Bảo tàng-Panorama, tạo thành một cụm tưởng niệm về những ngày ác liệt nhất của thành phố.",
    [
        "Toà nhà nơi nhóm chiến sĩ của trung sĩ Pavlov cố thủ gần 58 ngày trong Trận Stalingrad.",
        "Bức tường đầu hồi hướng ra Quảng trường Lenin được giữ làm phù điêu tưởng niệm.",
        "Nằm sát nhà máy xay Gergardt và Bảo tàng-Panorama, thành một cụm di tích chiến tranh.",
    ],
    p("Bên ngoài tham quan tự do suốt ngày; đây là toà nhà dân cư nên không vào bên trong.",
      "Miễn phí (tham quan phù điêu và bức tường tưởng niệm bên ngoài).",
      "Khoảng 15–20 phút.",
      "Quanh năm; kết hợp thăm cụm di tích Quảng trường Lenin.",
      "Đọc phù điêu tưởng niệm trên tường đầu hồi; kết hợp thăm nhà máy xay Gergardt và Panorama ngay cạnh."),
    [
        {"title": "Wikipedia (RU) — Дом Павлова", "url": "https://ru.wikipedia.org/wiki/Дом_Павлова"},
    ],
    ["monument", "wwii", "stalingrad", "memorial", "history", "volgograd"],
    maps_text("Дом Павлова", "Волгоград", "Pavlov's House", "Volgograd", 48.71694, 44.53250),
))

# 2) Площадь Павших Борцов --------------------------------------------------------
RECORDS.append(rec(
    "square-fallen-fighters",
    "Quảng trường Các Chiến Sĩ Đã Ngã Xuống (phiên âm: Plô-ssat Páp-sikh Bor-txốp)",
    "Площадь Павших Борцов",
    "Square of the Fallen Fighters",
    ["square_street"],
    48.70861, 44.51500,
    "Trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Quảng trường Các Chiến Sĩ Đã Ngã Xuống là quảng trường trung tâm chính của Volgograd, nơi có ngôi mộ tập thể và Ngọn lửa Vĩnh cửu tưởng niệm những người bảo vệ Tsaritsyn và Stalingrad. Đây là trái tim lịch sử và nghi lễ của thành phố.",
    "Quảng trường Các Chiến Sĩ Đã Ngã Xuống (Площадь Павших Борцов) là quảng trường trung tâm và trang trọng nhất của Volgograd. Tên gọi tưởng nhớ những chiến sĩ đã hy sinh trong Nội chiến bảo vệ Tsaritsyn, rồi sau này gắn thêm với ký ức bi tráng của Trận Stalingrad. Ở giữa quảng trường là ngôi mộ tập thể cùng một đài tháp (obelisk) và Ngọn lửa Vĩnh cửu cháy liên tục, nơi diễn ra nghi lễ đổi gác danh dự và các buổi lễ đặt hoa long trọng, nhất là dịp 9 tháng 5 (Ngày Chiến thắng) và 2 tháng 2 (kỷ niệm chiến thắng Stalingrad). Bên rìa quảng trường còn cây dương già nổi tiếng đã sống sót qua bom đạn, cùng nhiều công trình mang phong cách kiến trúc Xô viết hoành tráng được dựng lại sau chiến tranh. Từ quảng trường này, Đại lộ Anh Hùng (Аллея Героев) mở ra chạy thẳng xuống bờ sông Volga, tạo thành trục nghi lễ trung tâm của thành phố. Đây là điểm khởi đầu tự nhiên cho mọi hành trình khám phá Volgograd.",
    [
        "Quảng trường trung tâm chính của Volgograd với Ngọn lửa Vĩnh cửu và mộ tập thể.",
        "Nơi diễn ra nghi lễ đổi gác danh dự và lễ đặt hoa các dịp trọng đại.",
        "Điểm khởi đầu của trục nghi lễ Đại lộ Anh Hùng chạy xuống sông Volga.",
    ],
    p("Không gian công cộng ngoài trời, tham quan tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Quanh năm; dịp 9/5 và 2/2 không khí lễ hội, trang nghiêm đặc biệt.",
      "Xem nghi lễ đổi gác bên Ngọn lửa Vĩnh cửu; tìm cây dương sống sót qua chiến tranh gần đó."),
    [
        {"title": "Wikipedia (RU) — Площадь Павших Борцов (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Площадь_Павших_Борцов_(Волгоград)"},
    ],
    ["square_street", "memorial", "eternal-flame", "wwii", "center", "volgograd"],
    maps_text("Площадь Павших Борцов", "Волгоград", "Square of the Fallen Fighters", "Volgograd", 48.70861, 44.51500),
))

# 3) Аллея Героев -----------------------------------------------------------------
RECORDS.append(rec(
    "alley-of-heroes",
    "Đại lộ Anh Hùng (phiên âm: A-lê-ia Ghê-rô-ép)",
    "Аллея Героев",
    "Alley of Heroes",
    ["square_street"],
    48.70722, 44.51750,
    "Từ Quảng trường Các Chiến Sĩ Đã Ngã Xuống xuống Bến sông trung tâm, quận Trung tâm, thành phố Volgograd, tỉnh Volgograd, Nga",
    "Đại lộ Anh Hùng là dải phố đi bộ rợp bóng cây nối Quảng trường Các Chiến Sĩ Đã Ngã Xuống với bờ sông Volga. Dọc hai bên là những tấm bia khắc tên các Anh hùng Liên Xô gắn với Stalingrad, tạo nên trục tản bộ và tưởng niệm đẹp nhất thành phố.",
    "Đại lộ Anh Hùng (Аллея Героев) là một trong những không gian đi bộ được yêu thích nhất Volgograd, nối liền Quảng trường Các Chiến Sĩ Đã Ngã Xuống ở phía trên với bờ kè sông Volga ở phía dưới. Con đường rộng rợp bóng cây được thiết kế như một đại lộ tưởng niệm: dọc hai bên đặt những phiến đá khắc tên các Anh hùng Liên Xô đã lập chiến công trong bảo vệ Stalingrad, biến việc dạo bộ thành một hành trình tri ân lịch sử. Vào mùa hè, đây là nơi người dân và du khách thong thả tản bộ giữa hàng cây xanh mát, còn dịp lễ lớn thì trở thành tuyến đường diễu hành và đặt hoa. Từ đầu dưới của đại lộ, tầm nhìn mở ra bờ kè Tập đoàn quân 62 và dòng Volga rộng lớn, nơi có cầu thang đá hoành tráng và đài phun nước. Nằm ngay trung tâm, gần các nhà hát, bảo tàng và khách sạn, Đại lộ Anh Hùng là mạch nối tự nhiên giữa phần 'đô thị' và phần 'sông nước' của Volgograd.",
    [
        "Phố đi bộ tưởng niệm nối Quảng trường Các Chiến Sĩ với bờ sông Volga.",
        "Hai bên là các phiến đá khắc tên Anh hùng Liên Xô gắn với Stalingrad.",
        "Trục tản bộ trung tâm dẫn tới cầu thang đá và đài phun nước bên bờ kè.",
    ],
    p("Không gian công cộng ngoài trời, đi dạo tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 30–45 phút (cả tuyến ra tới bờ kè).",
      "Cuối xuân đến đầu thu khi cây xanh mát; buổi tối có đèn chiếu sáng đẹp.",
      "Đi bộ trọn tuyến ra tận bờ kè để ngắm sông Volga; đọc tên trên các phiến đá tưởng niệm."),
    [
        {"title": "Wikipedia (RU) — Аллея Героев (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Аллея_Героев_(Волгоград)"},
    ],
    ["square_street", "promenade", "memorial", "pedestrian", "center", "volgograd"],
    maps_text("Аллея Героев", "Волгоград", "Alley of Heroes", "Volgograd", 48.70722, 44.51750),
))

# 4) Площадь Ленина ---------------------------------------------------------------
RECORDS.append(rec(
    "lenin-square-volgograd",
    "Quảng trường Lenin (phiên âm: Plô-ssat Lê-nhi-na)",
    "Площадь Ленина",
    "Lenin Square",
    ["square_street"],
    48.71639, 44.53194,
    "Quận Trung tâm, gần bờ sông Volga, thành phố Volgograd, tỉnh Volgograd, Nga",
    "Quảng trường Lenin là quảng trường lịch sử gói trọn ba biểu tượng của Trận Stalingrad: Nhà Pavlov, khu di tích nhà máy xay Gergardt và tượng đài Lenin. Đây là một trong những địa điểm giàu sức nặng lịch sử nhất Volgograd.",
    "Quảng trường Lenin (Площадь Ленина) là một không gian đặc biệt vì tập hợp trên cùng một khoảnh đất nhiều chứng tích quan trọng nhất của Trận Stalingrad. Ở đây, du khách có thể đứng giữa Nhà Pavlov đã được phục dựng với bức tường tưởng niệm, khu tàn tích nhà máy xay Gergardt được cố ý giữ nguyên trạng đổ nát như một 'bảo tàng ngoài trời' của sự tàn phá, và tượng đài Vladimir Lenin cao lớn nhìn ra quảng trường. Chính tại vùng đất này, các chiến sĩ Hồng quân đã giành giật từng căn phòng, từng đống gạch vụn trong những tháng cuối năm 1942. Sự tương phản giữa toà nhà được khôi phục và toà nhà giữ nguyên vết đạn giúp người xem cảm nhận rõ ràng mức độ khốc liệt của cuộc chiến đô thị. Nằm sát bờ sông Volga và cách Bảo tàng-Panorama chỉ vài bước, Quảng trường Lenin là mắt xích không thể bỏ qua trong hành trình tìm hiểu về Stalingrad.",
    [
        "Nơi hội tụ Nhà Pavlov, tàn tích nhà máy xay Gergardt và tượng đài Lenin.",
        "Tương phản giữa công trình phục dựng và công trình giữ nguyên vết đạn chiến tranh.",
        "Sát bờ Volga, chỉ cách Bảo tàng-Panorama vài bước chân.",
    ],
    p("Không gian công cộng ngoài trời, tham quan tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 30 phút (cùng cụm di tích).",
      "Quanh năm; kết hợp buổi tham quan Panorama gần đó.",
      "Kết hợp cả cụm: Nhà Pavlov, nhà máy xay Gergardt, Panorama và bờ kè trong một vòng đi bộ."),
    [
        {"title": "Wikipedia (RU) — Площадь Ленина (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Площадь_Ленина_(Волгоград)"},
    ],
    ["square_street", "memorial", "wwii", "stalingrad", "center", "volgograd"],
    maps_text("Площадь Ленина", "Волгоград", "Lenin Square", "Volgograd", 48.71639, 44.53194),
))

# 5) Тополь на Аллее Героев --------------------------------------------------------
RECORDS.append(rec(
    "surviving-poplar-alley-heroes",
    "Cây dương sống sót qua Trận Stalingrad (phiên âm: Tô-pôl)",
    "Тополь, переживший Сталинградскую битву",
    "The Poplar that Survived the Battle of Stalingrad",
    ["monument"],
    48.70750, 44.51750,
    "Đại lộ Anh Hùng, gần Quảng trường Các Chiến Sĩ Đã Ngã Xuống, trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Cây dương cổ thụ này là một trong số ít cây sống sót qua sự tàn phá của Trận Stalingrad, khi gần như toàn bộ cây xanh trong thành phố bị bom đạn thiêu rụi. Thân cây còn mang những vết mảnh đạn, được gắn bia tưởng niệm và trở thành 'nhân chứng sống' của chiến tranh.",
    "Trên Đại lộ Anh Hùng ở trung tâm Volgograd có một cây dương già được người dân gìn giữ như báu vật: đây là một trong rất ít cây sống sót qua Trận Stalingrad, thời điểm mà bom đạn đã biến thành phố thành đống tro tàn và gần như xoá sạch mọi bóng cây. Thân cây vẫn còn giữ những vết sẹo do mảnh đạn găm vào, và một tấm bia nhỏ đặt bên gốc kể lại câu chuyện của nó như một 'nhân chứng sống' của những ngày ác liệt. Đối với người Volgograd, cây dương không chỉ là một thực vật mà là biểu tượng của sức sống bền bỉ, của khả năng hồi sinh sau huỷ diệt. Nhiều đôi tân hôn và du khách dừng lại bên cây để chụp ảnh và tưởng niệm. Nằm ngay trên tuyến đi bộ trung tâm, cây dương là một điểm dừng nhỏ nhưng đầy ý nghĩa, nhắc nhở rằng ngay cả sự sống mong manh nhất cũng có thể vượt qua chiến tranh.",
    [
        "Một trong số ít cây sống sót qua sự huỷ diệt của Trận Stalingrad.",
        "Thân cây còn giữ vết mảnh đạn, được gắn bia tưởng niệm.",
        "Biểu tượng sức sống và sự hồi sinh của thành phố, nằm trên Đại lộ Anh Hùng.",
    ],
    p("Không gian công cộng ngoài trời, tham quan tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 10 phút.",
      "Quanh năm; mùa hè khi cây xanh lá càng nổi bật ý nghĩa 'sống sót'.",
      "Đọc tấm bia bên gốc cây; kết hợp trên đường dạo Đại lộ Anh Hùng."),
    [
        {"title": "Wikipedia (RU) — Тополь (памятник природы, Волгоград)", "url": "https://ru.wikipedia.org/wiki/Тополь_(Волгоград)"},
    ],
    ["monument", "nature", "wwii", "memorial", "symbol", "volgograd"],
    maps_text("Тополь переживший Сталинградскую битву", "Волгоград", "Surviving Poplar", "Volgograd", 48.70750, 44.51750),
))

# ============================ TÀU-BẢO TÀNG & NHÀ THỜ ============================

# 6) Пароход-музей «Гаситель» ------------------------------------------------------
RECORDS.append(rec(
    "gasitel-fireboat-monument",
    "Tàu cứu hoả - đài tưởng niệm «Gasitel» (phiên âm: Ga-si-ten)",
    "Пароход-музей «Гаситель»",
    "Gasitel Fireboat Memorial",
    ["monument"],
    48.70167, 44.51361,
    "Bờ kè phía dưới, gần cửa sông Tsaritsa, quận Trung tâm, thành phố Volgograd, tỉnh Volgograd, Nga",
    "«Gasitel» là con tàu cứu hoả huyền thoại từng phục vụ ở Tsaritsyn/Stalingrad qua cả Nội chiến lẫn Trận Stalingrad, cứu người và dập lửa dưới mưa bom. Con tàu được trục vớt và đặt trên bờ kè như một đài tưởng niệm sống động về lòng dũng cảm của thuỷ thủ sông Volga.",
    "Con tàu hơi nước cứu hoả «Gasitel» (nghĩa là 'người dập lửa') là một trong những đài tưởng niệm độc đáo nhất Volgograd. Được đóng từ đầu thế kỷ 20, con tàu đã phục vụ trên sông Volga suốt nhiều thập niên đầy biến động: trong Nội chiến nó tham gia vận chuyển và chiến đấu, còn trong Trận Stalingrad năm 1942–1943 nó lăn xả cứu hoả, chở thương binh và tiếp tế giữa làn bom đạn dày đặc, nhiều lần bị bắn thủng và chìm nhưng vẫn được trục vớt, sửa chữa để tiếp tục hoạt động. Sau chiến tranh, để ghi nhớ chiến công của con tàu và của những người lính thuỷ Volga, «Gasitel» được nâng lên khỏi lòng sông và đặt trên bệ bên bờ kè phía dưới, gần cửa sông Tsaritsa, trở thành một tượng đài kiêm bảo tàng ngoài trời. Đứng bên con tàu gỉ sét với những vết đạn, du khách như chạm vào một chương ít được nhắc tới của trận chiến: cuộc chiến trên mặt nước. Đây là điểm dừng ý nghĩa khi dạo dọc bờ sông Volga ở trung tâm thành phố.",
    [
        "Tàu cứu hoả từng phục vụ qua Nội chiến và Trận Stalingrad, nhiều lần bị bắn chìm rồi trục vớt.",
        "Được nâng khỏi lòng sông, đặt trên bờ kè làm đài tưởng niệm - bảo tàng ngoài trời.",
        "Gợi nhớ 'cuộc chiến trên mặt nước' ít được biết tới của Trận Stalingrad.",
    ],
    p("Khu tưởng niệm ngoài trời, tham quan bên ngoài tự do; giờ mở khu vực có thể thay đổi.",
      "Miễn phí (khu vực ngoài trời).",
      "Khoảng 20–30 phút.",
      "Cuối xuân đến đầu thu; kết hợp dạo bờ kè.",
      "Kết hợp đi bộ dọc bờ kè và cửa sông Tsaritsa; mang giày thoải mái cho đoạn dốc xuống bờ."),
    [
        {"title": "Wikipedia (RU) — Гаситель (пожарный пароход)", "url": "https://ru.wikipedia.org/wiki/Гаситель_(пароход)"},
    ],
    ["monument", "ship", "wwii", "memorial", "volga", "volgograd"],
    maps_text("Пароход Гаситель", "Волгоград", "Gasitel Fireboat", "Volgograd", 48.70167, 44.51361),
))

# 7) Собор Александра Невского ----------------------------------------------------
RECORDS.append(rec(
    "alexander-nevsky-cathedral-volgograd",
    "Nhà thờ chính toà Alexander Nevsky (phiên âm: Xa-bo A-lếch-xan-đra Nhép-xkô-va)",
    "Собор Александра Невского",
    "Alexander Nevsky Cathedral",
    ["church"],
    48.70944, 44.51194,
    "Gần Quảng trường Các Chiến Sĩ Đã Ngã Xuống, trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Nhà thờ chính toà Alexander Nevsky là thánh đường Chính thống giáo lớn, được phục dựng và khánh thành năm 2021 tại trung tâm Volgograd, tái hiện ngôi nhà thờ nguy nga đầu thế kỷ 20 từng bị phá huỷ thời Xô viết. Với năm mái vòm vàng và tường trắng, đây là công trình tôn giáo tiêu biểu mới của thành phố.",
    "Nhà thờ chính toà Alexander Nevsky (Собор Александра Невского) là một trong những công trình tôn giáo bề thế và mới mẻ nhất của Volgograd. Ngôi nhà thờ nguyên bản được xây ở Tsaritsyn đầu thế kỷ 20 theo phong cách tân-Byzantine, từng là thánh đường tráng lệ bậc nhất vùng, nhưng đã bị giật đổ vào thập niên 1930 trong làn sóng bài tôn giáo thời Xô viết. Đầu thế kỷ 21, thành phố quyết định phục dựng nhà thờ gần vị trí lịch sử; công trình mới hoàn thành và được thánh hiến long trọng vào năm 2021. Với khối kiến trúc cân đối, tường trắng sáng, năm mái vòm dát vàng lấp lánh và tháp chuông cao, nhà thờ nhanh chóng trở thành điểm nhấn của trung tâm Volgograd, đủ sức chứa hàng nghìn giáo dân. Bên trong là nội thất được trang trí công phu với các bức bích hoạ và iconostas theo truyền thống Chính thống giáo. Nằm ngay gần Quảng trường Các Chiến Sĩ Đã Ngã Xuống và Đại lộ Anh Hùng, thánh đường vừa là nơi thờ phụng vừa là điểm tham quan kiến trúc hấp dẫn.",
    [
        "Thánh đường Chính thống giáo lớn được phục dựng, khánh thành năm 2021.",
        "Tái hiện nhà thờ tân-Byzantine đầu thế kỷ 20 từng bị phá huỷ thời Xô viết.",
        "Năm mái vòm dát vàng, tường trắng, nằm sát trung tâm và Đại lộ Anh Hùng.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 7:00–19:00; nên kiểm tra lịch lễ trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 30–40 phút.",
      "Quanh năm; dịp lễ lớn Chính thống giáo không khí trang nghiêm, đông đúc.",
      "Ăn mặc kín đáo, nữ nên có khăn trùm đầu; kết hợp thăm Quảng trường Các Chiến Sĩ ngay cạnh."),
    [
        {"title": "Wikipedia (RU) — Собор Александра Невского (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Собор_Александра_Невского_(Волгоград)"},
    ],
    ["church", "orthodox", "cathedral", "neo-byzantine", "landmark", "volgograd"],
    maps_text("Собор Александра Невского", "Волгоград", "Alexander Nevsky Cathedral", "Volgograd", 48.70944, 44.51194),
))

# 8) Казанский собор --------------------------------------------------------------
RECORDS.append(rec(
    "kazan-cathedral-volgograd",
    "Nhà thờ chính toà Kazan (phiên âm: Ka-dan-xki xa-bo)",
    "Казанский кафедральный собор",
    "Kazan Cathedral",
    ["church"],
    48.69417, 44.48694,
    "Phố Lipetskaya 10, quận Voroshilovsky, thành phố Volgograd, tỉnh Volgograd, Nga",
    "Nhà thờ chính toà Kazan là một trong những nhà thờ cổ hiếm hoi của Volgograd còn tồn tại, xây bằng gạch đỏ cuối thế kỷ 19 theo phong cách chiết trung Nga. Sống sót qua Trận Stalingrad, đây hiện là nhà thờ chính toà của giáo phận Volgograd.",
    "Nhà thờ chính toà Kazan (Казанский собор) là một trong số ít công trình tôn giáo cổ của thành phố còn sót lại đến ngày nay. Được khởi dựng vào cuối thế kỷ 19 bằng gạch đỏ trần theo phong cách chiết trung mang âm hưởng Nga cổ, nhà thờ ban đầu là một giáo đường bình dân ở vùng ngoại ô Tsaritsyn. Điều làm nên giá trị đặc biệt của công trình là nó đã trụ vững qua Trận Stalingrad khốc liệt - khi phần lớn thành phố bị san phẳng - dù cũng chịu hư hại và từng bị đóng cửa, sử dụng sai mục đích dưới thời Xô viết. Sau này nhà thờ được trùng tu, khôi phục và nâng lên thành nhà thờ chính toà của giáo phận Volgograd. Với sắc gạch đỏ ấm áp, những mái vòm hành xanh điểm sao vàng và tháp chuông duyên dáng, Казанский собор là một ví dụ quý giá về kiến trúc nhà thờ Nga trước cách mạng còn giữ được ở một thành phố gần như phải xây lại từ đầu. Đây là điểm hành hương và tham quan yên tĩnh, hơi tách khỏi lõi du lịch nhưng dễ tiếp cận.",
    [
        "Một trong số ít nhà thờ cổ (cuối thế kỷ 19) của Volgograd còn tồn tại.",
        "Sống sót qua Trận Stalingrad khi phần lớn thành phố bị san phẳng.",
        "Nhà thờ chính toà hiện nay của giáo phận Volgograd, gạch đỏ, mái vòm xanh.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 7:00–19:00; nên kiểm tra trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 30 phút.",
      "Quanh năm; dịp lễ lớn Chính thống giáo trang nghiêm, đông đúc.",
      "Ăn mặc kín đáo, nữ nên có khăn trùm đầu; giữ yên lặng trong giờ lễ."),
    [
        {"title": "Wikipedia (RU) — Казанский собор (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Казанский_собор_(Волгоград)"},
        {"title": "Sobory.ru — Собор Казанской иконы Божией Матери (Волгоград)", "url": "https://sobory.ru/geo/city/2016"},
    ],
    ["church", "orthodox", "cathedral", "brick", "historic", "volgograd"],
    maps_text("Казанский кафедральный собор", "Волгоград", "Kazan Cathedral", "Volgograd", 48.69417, 44.48694),
))

# 9) Храм Иоанна Предтечи ---------------------------------------------------------
RECORDS.append(rec(
    "john-baptist-church-volgograd",
    "Nhà thờ Thánh Gioan Tiền Hô (phiên âm: Khram I-ô-an-na Prét-te-tri)",
    "Храм Иоанна Предтечи",
    "Church of St. John the Baptist",
    ["church"],
    48.70333, 44.51583,
    "Gần cửa sông Tsaritsa, bờ sông Volga, quận Trung tâm, thành phố Volgograd, tỉnh Volgograd, Nga",
    "Nhà thờ Thánh Gioan Tiền Hô được xem là ngôi nhà thờ đầu tiên và cổ nhất của Tsaritsyn, có nguồn gốc từ cuối thế kỷ 16. Bị phá huỷ hoàn toàn thời Xô viết, nhà thờ được xây dựng lại vào những năm 1990–2000 gần vị trí lịch sử bên bờ Volga.",
    "Nhà thờ Thánh Gioan Tiền Hô (Храм Иоанна Предтечи) gắn liền với chính nguồn cội của thành phố: theo truyền thống, đây là ngôi nhà thờ đầu tiên của Tsaritsyn, có từ khoảng cuối thế kỷ 16, gần như cùng thời với sự ra đời của pháo đài Tsaritsyn bên sông Volga. Trải qua nhiều thế kỷ, nhà thờ được xây lại bằng đá và mở rộng, trở thành một trong những công trình tâm linh lâu đời và được kính trọng nhất vùng. Tuy nhiên vào thập niên 1930, nhà thờ bị giật đổ hoàn toàn trong chiến dịch bài tôn giáo, và khu đất về sau còn hứng chịu bom đạn Trận Stalingrad. Đến những năm 1990–2000, nhà thờ được phục dựng gần vị trí lịch sử, với dáng vẻ trắng thanh thoát, mái vòm hành và tháp chuông nhìn ra dòng Volga. Nằm gần cửa sông Tsaritsa và tàu tưởng niệm «Gasitel», ngôi nhà thờ nhỏ mang ý nghĩa biểu tượng lớn - đánh dấu điểm khởi nguồn của thành phố và sự hồi sinh của đời sống tâm linh sau nhiều biến động.",
    [
        "Được coi là nhà thờ đầu tiên, cổ nhất của Tsaritsyn (cuối thế kỷ 16).",
        "Bị phá huỷ thời Xô viết, phục dựng lại những năm 1990–2000 bên bờ Volga.",
        "Biểu tượng cho điểm khởi nguồn của thành phố và sự hồi sinh tâm linh.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–19:00; nên kiểm tra trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 20–30 phút.",
      "Quanh năm; kết hợp dạo bờ kè và thăm tàu «Gasitel» gần đó.",
      "Ăn mặc kín đáo khi vào trong; kết hợp cửa sông Tsaritsa và bờ kè phía dưới."),
    [
        {"title": "Wikipedia (RU) — Церковь Иоанна Предтечи (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Церковь_Иоанна_Предтечи_(Волгоград)"},
    ],
    ["church", "orthodox", "historic", "tsaritsyn", "riverside", "volgograd"],
    maps_text("Храм Иоанна Предтечи", "Волгоград", "Church of St John the Baptist", "Volgograd", 48.70333, 44.51583),
))

# 10) Храм Всех Святых на Мамаевом кургане ----------------------------------------
RECORDS.append(rec(
    "all-saints-church-mamayev-kurgan",
    "Nhà thờ Chư Thánh trên đồi Mamayev Kurgan (phiên âm: Khram Vsekh Svia-tưkh)",
    "Храм Всех Святых на Мамаевом кургане",
    "Church of All Saints on Mamayev Kurgan",
    ["church"],
    48.74139, 44.53694,
    "Sườn đồi Mamayev Kurgan, quận Trung tâm, thành phố Volgograd, tỉnh Volgograd, Nga",
    "Nhà thờ Chư Thánh là một thánh đường Chính thống giáo được xây trên chính đồi Mamayev Kurgan - nơi diễn ra những trận đánh đẫm máu nhất Trận Stalingrad. Khánh thành năm 2005, nhà thờ tưởng niệm các chiến sĩ đã ngã xuống, hoà quyện chức năng tôn giáo với ký ức chiến tranh.",
    "Nhà thờ Chư Thánh trên đồi Mamayev Kurgan (Храм Всех Святых) mang một ý nghĩa đặc biệt vì được dựng ngay trên ngọn đồi từng là điểm giao tranh khốc liệt nhất của Trận Stalingrad, nơi hàng vạn chiến sĩ đã hy sinh và được an nghỉ. Ý tưởng xây một ngôi nhà thờ tưởng niệm tại đây được ấp ủ từ lâu; công trình khởi công cuối thập niên 1990 và được thánh hiến vào năm 2005. Nhà thờ xây theo phong cách Nga truyền thống với tường trắng, các mái vòm hành dát vàng và tháp chuông, tạo cảm giác thanh khiết, trang nghiêm giữa quần thể tưởng niệm hoành tráng của Mamayev Kurgan. Với người hành hương và thân nhân các liệt sĩ, đây là nơi cầu nguyện, thắp nến cho những người đã khuất; với du khách, nhà thờ là một điểm dừng lắng đọng trên hành trình leo lên tượng đài «Tổ quốc vẫy gọi». Sự kết hợp giữa đài tưởng niệm quân sự khổng lồ và ngôi thánh đường tôn giáo khiến Mamayev Kurgan trở thành không gian tưởng niệm đa tầng nghĩa hiếm có.",
    [
        "Nhà thờ Chính thống giáo dựng ngay trên đồi Mamayev Kurgan lịch sử.",
        "Khánh thành năm 2005, tưởng niệm các chiến sĩ ngã xuống trong Trận Stalingrad.",
        "Kết hợp chức năng tôn giáo với ký ức chiến tranh, cạnh tượng «Tổ quốc vẫy gọi».",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–19:00; nên kiểm tra trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 20–30 phút.",
      "Quanh năm; kết hợp cùng buổi tham quan Mamayev Kurgan.",
      "Ăn mặc kín đáo khi vào trong; kết hợp trong hành trình leo lên tượng «Tổ quốc vẫy gọi»."),
    [
        {"title": "Wikipedia (RU) — Храм Всех Святых (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Храм_Всех_Святых_(Волгоград)"},
    ],
    ["church", "orthodox", "memorial", "mamayev-kurgan", "wwii", "volgograd"],
    maps_text("Храм Всех Святых на Мамаевом кургане", "Волгоград", "Church of All Saints Mamayev Kurgan", "Volgograd", 48.74139, 44.53694),
))

# ============================ BẢO TÀNG ============================

# 11) Волгоградский областной краеведческий музей ---------------------------------
RECORDS.append(rec(
    "regional-lore-museum-volgograd",
    "Bảo tàng Địa phương học tỉnh Volgograd (phiên âm: Kra-ê-vét-tre-xki mu-dây)",
    "Волгоградский областной краеведческий музей",
    "Volgograd Regional Museum of Local Lore",
    ["museum"],
    48.70917, 44.51528,
    "Đại lộ Lenin 5a (khu trung tâm), thành phố Volgograd, tỉnh Volgograd, Nga",
    "Bảo tàng Địa phương học tỉnh Volgograd là bảo tàng lâu đời nhất vùng, trưng bày toàn cảnh lịch sử tự nhiên và văn hoá của mảnh đất từ thời tiền sử, qua Tsaritsyn, tới Stalingrad và Volgograd hiện đại. Đây là điểm khởi đầu lý tưởng để hiểu chiều sâu lịch sử của vùng.",
    "Bảo tàng Địa phương học tỉnh Volgograd (Волгоградский областной краеведческий музей) là bảo tàng lâu đời và bao quát nhất của vùng, có nguồn gốc từ cuối thế kỷ 19 - đầu thế kỷ 20. Các gian trưng bày dẫn dắt người xem qua một hành trình dài: từ địa chất, cổ sinh vật và thiên nhiên thảo nguyên vùng hạ lưu Volga, qua thời kỳ các dân tộc du mục và Hãn quốc Kim Trướng, tới sự ra đời của pháo đài Tsaritsyn, đời sống thương mại nhộn nhịp bên sông, rồi những biến động của thế kỷ 20. Bộ sưu tập phong phú gồm hiện vật khảo cổ, trang phục, đồ dùng sinh hoạt, tiền cổ và cả những kỷ vật gắn với lịch sử quân sự của vùng. Nhờ cách kể chuyện mạch lạc, bảo tàng giúp du khách đặt Trận Stalingrad nổi tiếng vào một bối cảnh lịch sử rộng lớn hơn, hiểu vì sao vùng đất này lại quan trọng suốt nhiều thế kỷ. Toạ lạc ngay trung tâm thành phố trong một toà nhà lịch sử, đây là điểm dừng chân giàu thông tin cho những ai muốn tìm hiểu sâu về Volgograd và tỉnh của nó.",
    [
        "Bảo tàng lâu đời và bao quát nhất tỉnh Volgograd.",
        "Trưng bày từ địa chất, khảo cổ tới lịch sử Tsaritsyn - Stalingrad - Volgograd.",
        "Giúp đặt Trận Stalingrad vào bối cảnh lịch sử nhiều thế kỷ của vùng.",
    ],
    p("Thường mở cửa khoảng 10:00–18:00, nghỉ thứ Hai; nên kiểm tra lịch trước khi đến.",
      "Vé vào cửa phải trả phí, mức phổ thông (có ưu đãi cho học sinh, sinh viên, người cao tuổi).",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; thích hợp cả khi thời tiết xấu.",
      "Kết hợp thăm Quảng trường Các Chiến Sĩ và Đại lộ Anh Hùng ngay gần đó."),
    [
        {"title": "Wikipedia (RU) — Волгоградский областной краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Волгоградский_областной_краеведческий_музей"},
    ],
    ["museum", "history", "local-lore", "culture", "center", "volgograd"],
    maps_text("Волгоградский областной краеведческий музей", "Волгоград", "Volgograd Regional Museum of Local Lore", "Volgograd", 48.70917, 44.51528),
))

# 12) Музей изобразительных искусств им. Машкова ----------------------------------
RECORDS.append(rec(
    "mashkov-fine-arts-museum-volgograd",
    "Bảo tàng Mỹ thuật mang tên Mashkov (phiên âm: Mu-dây IZO im. Mát-cô-va)",
    "Волгоградский музей изобразительных искусств имени И. И. Машкова",
    "Mashkov Museum of Fine Arts",
    ["museum"],
    48.71222, 44.51750,
    "Đại lộ Lenin 21, trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Bảo tàng Mỹ thuật Mashkov là bảo tàng nghệ thuật chính của Volgograd, sở hữu bộ sưu tập hội hoạ, đồ hoạ và điêu khắc Nga từ thế kỷ 18 đến hiện đại. Bảo tàng mang tên danh hoạ Ilya Mashkov, người con của vùng đất này.",
    "Bảo tàng Mỹ thuật Volgograd mang tên Ilya Mashkov (Волгоградский музей изобразительных искусств им. И. И. Машкова) là trung tâm nghệ thuật tạo hình quan trọng nhất của vùng. Bảo tàng được thành lập vào giữa thế kỷ 20, khi thành phố đang hồi sinh sau chiến tranh, và dần xây dựng một bộ sưu tập đáng nể gồm hội hoạ, đồ hoạ, điêu khắc và nghệ thuật trang trí ứng dụng của Nga trải dài từ thế kỷ 18 đến nghệ thuật Xô viết và đương đại. Bảo tàng được đặt theo tên Ilya Mashkov - hoạ sĩ tiên phong nổi tiếng của trường phái tiên phong Nga đầu thế kỷ 20, người sinh ra tại vùng đất này, và lưu giữ nhiều tác phẩm cùng tư liệu liên quan đến ông. Bên cạnh bộ sưu tập thường trực, bảo tàng thường xuyên tổ chức các triển lãm chuyên đề, hoạt động giáo dục nghệ thuật và giao lưu văn hoá. Nằm ngay trên đại lộ trung tâm, đây là điểm đến lý tưởng cho những ai muốn tạm rời khỏi chủ đề chiến tranh để thưởng thức một khía cạnh tinh tế, giàu thẩm mỹ của văn hoá Nga.",
    [
        "Bảo tàng nghệ thuật tạo hình chính của Volgograd.",
        "Bộ sưu tập hội hoạ, đồ hoạ, điêu khắc Nga từ thế kỷ 18 đến đương đại.",
        "Mang tên hoạ sĩ tiên phong Ilya Mashkov, người con của vùng đất.",
    ],
    p("Thường mở cửa khoảng 10:00–18:00, nghỉ một ngày trong tuần; nên kiểm tra lịch trước.",
      "Vé vào cửa phải trả phí, mức phổ thông (có ưu đãi cho các nhóm đối tượng).",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; thích hợp cả khi thời tiết xấu.",
      "Kiểm tra lịch triển lãm chuyên đề đang diễn ra; kết hợp dạo đại lộ trung tâm."),
    [
        {"title": "Wikipedia (RU) — Волгоградский музей изобразительных искусств имени И. И. Машкова", "url": "https://ru.wikipedia.org/wiki/Волгоградский_музей_изобразительных_искусств_имени_И._И._Машкова"},
    ],
    ["museum", "art", "fine-arts", "culture", "center", "volgograd"],
    maps_text("Музей изобразительных искусств имени Машкова", "Волгоград", "Mashkov Museum of Fine Arts", "Volgograd", 48.71222, 44.51750),
))

# 13) Музей «Память» --------------------------------------------------------------
RECORDS.append(rec(
    "memory-museum-paulus-surrender",
    "Bảo tàng «Ký ức» - nơi Paulus đầu hàng (phiên âm: Mu-dây Pá-miat)",
    "Музей «Память»",
    "Memory Museum (Paulus Surrender Site)",
    ["museum"],
    48.70806, 44.51361,
    "Quảng trường Các Chiến Sĩ Đã Ngã Xuống 2 (tầng hầm cửa hàng bách hoá ЦУМ cũ), thành phố Volgograd, tỉnh Volgograd, Nga",
    "Bảo tàng «Ký ức» nằm ngay dưới tầng hầm nơi Thống chế Friedrich Paulus, tư lệnh Tập đoàn quân số 6 của Đức, bị bắt và đầu hàng ngày 31/1/1943 - dấu chấm hết cho Trận Stalingrad. Bảo tàng tái hiện chính căn phòng lịch sử này.",
    "Bảo tàng «Ký ức» (Музей «Память») là một trong những địa điểm mang sức nặng lịch sử bậc nhất Volgograd, bởi nó toạ lạc chính tại tầng hầm của toà nhà cửa hàng bách hoá trung tâm (ЦУМ) cũ - nơi bộ chỉ huy Tập đoàn quân số 6 của Đức đóng trong những ngày cuối, và là nơi Thống chế Friedrich Paulus bị bắt cùng bộ tham mưu vào ngày 31 tháng 1 năm 1943. Sự kiện này đánh dấu sự sụp đổ của đạo quân Đức bị vây hãm và thực sự khép lại Trận Stalingrad - một trong những bước ngoặt lớn nhất của Thế chiến thứ hai. Bảo tàng tái dựng căn phòng nơi Paulus đầu hàng, trưng bày vũ khí, quân phục, tài liệu, ảnh tư liệu và hiện vật của cả hai phía, giúp du khách hình dung sống động những giờ phút định mệnh dưới lòng đất ấy. Không gian tầng hầm chật, tối càng làm tăng cảm giác chân thực và bức bối của tình thế bị bao vây. Nằm ngay dưới Quảng trường Các Chiến Sĩ Đã Ngã Xuống, đây là điểm không thể bỏ qua đối với những ai quan tâm đến lịch sử Trận Stalingrad.",
    [
        "Nằm tại tầng hầm nơi Thống chế Paulus đầu hàng ngày 31/1/1943.",
        "Tái dựng căn phòng lịch sử khép lại Trận Stalingrad.",
        "Trưng bày hiện vật, tài liệu của cả hai phía dưới Quảng trường Các Chiến Sĩ.",
    ],
    p("Thường mở cửa khoảng 10:00–18:00, có thể nghỉ một ngày trong tuần; nên kiểm tra trước.",
      "Vé vào cửa phải trả phí, mức phổ thông (có ưu đãi).",
      "Khoảng 45 phút–1 giờ.",
      "Quanh năm; là điểm trong nhà, thích hợp mọi thời tiết.",
      "Kết hợp ngay với Quảng trường Các Chiến Sĩ phía trên; nên đi cùng hướng dẫn để hiểu bối cảnh."),
    [
        {"title": "Wikipedia (RU) — Музей «Память» (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Музей_«Память»_(Волгоград)"},
    ],
    ["museum", "wwii", "stalingrad", "history", "paulus", "volgograd"],
    maps_text("Музей Память", "Волгоград", "Memory Museum Paulus Surrender", "Volgograd", 48.70806, 44.51361),
))

# 14) Мемориально-исторический музей ----------------------------------------------
RECORDS.append(rec(
    "memorial-historical-museum-volgograd",
    "Bảo tàng Lịch sử - Tưởng niệm Volgograd (phiên âm: Me-mô-ri-an-nô is-tô-ri-tre-xki mu-dây)",
    "Мемориально-исторический музей",
    "Memorial and Historical Museum",
    ["museum"],
    48.71139, 44.51028,
    "Phố Gogolya 10, gần ga đường sắt, trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Bảo tàng Lịch sử - Tưởng niệm nằm trong một dinh thự thương gia cổ, chuyên về thời kỳ Nội chiến và cuộc bảo vệ Tsaritsyn (Volgograd trước đây) đầu thế kỷ 20. Đây là một chi nhánh của bảo tàng-panorama, bổ sung góc nhìn về lịch sử quân sự sớm của thành phố.",
    "Bảo tàng Lịch sử - Tưởng niệm (Мемориально-исторический музей) được đặt trong một toà dinh thự thương gia duyên dáng còn sót lại từ thời Tsaritsyn, gần khu vực nhà ga đường sắt trung tâm. Khác với các bảo tàng tập trung vào Thế chiến thứ hai, nơi đây kể câu chuyện của một giai đoạn sớm hơn nhưng cũng đầy kịch tính: thời kỳ Nội chiến Nga (1918–1920) và cuộc chiến giành - giữ Tsaritsyn, thành phố khi đó có vị trí chiến lược trên sông Volga. Các gian trưng bày giới thiệu vũ khí, quân phục, cờ hiệu, tài liệu và hiện vật của thời kỳ đầy biến động này, cùng ký ức về những nhân vật và sự kiện đã định hình số phận thành phố. Bản thân toà nhà, với nội thất và kiến trúc được gìn giữ, cũng là một hiện vật lịch sử. Là một phần của hệ thống bảo tàng-panorama «Trận Stalingrad», bảo tàng bổ sung chiều sâu cho hành trình tìm hiểu lịch sử quân sự của Volgograd, cho thấy thành phố đã trải qua không chỉ một mà nhiều cuộc chiến khốc liệt trong thế kỷ 20.",
    [
        "Đặt trong dinh thự thương gia cổ thời Tsaritsyn, gần ga đường sắt.",
        "Chuyên về Nội chiến Nga và cuộc bảo vệ Tsaritsyn đầu thế kỷ 20.",
        "Chi nhánh của bảo tàng-panorama, bổ sung góc nhìn lịch sử quân sự sớm.",
    ],
    p("Thường mở cửa khoảng 10:00–18:00, có thể nghỉ một ngày trong tuần; nên kiểm tra trước.",
      "Vé vào cửa phải trả phí, mức phổ thông (có ưu đãi).",
      "Khoảng 45 phút–1 giờ.",
      "Quanh năm; điểm trong nhà, thích hợp mọi thời tiết.",
      "Kết hợp thăm ga đường sắt Volgograd-1 gần đó; chú ý cả kiến trúc toà dinh thự."),
    [
        {"title": "Wikipedia (RU) — Мемориально-исторический музей (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Мемориально-исторический_музей_(Волгоград)"},
    ],
    ["museum", "history", "civil-war", "tsaritsyn", "mansion", "volgograd"],
    maps_text("Мемориально-исторический музей", "Волгоград", "Memorial and Historical Museum", "Volgograd", 48.71139, 44.51028),
))

# 15) Камышинский историко-краеведческий музей ------------------------------------
RECORDS.append(rec(
    "kamyshin-local-lore-museum",
    "Bảo tàng Lịch sử - Địa phương học Kamyshin (phiên âm: Ka-mư-sin-xki mu-dây)",
    "Камышинский историко-краеведческий музей",
    "Kamyshin Museum of History and Local Lore",
    ["museum"],
    50.09417, 45.41528,
    "Thành phố Kamyshin, bên sông Volga, tỉnh Volgograd, Nga",
    "Bảo tàng Lịch sử - Địa phương học Kamyshin nằm trong một toà nhà đẹp mắt của thị trấn thương mại cổ bên sông Volga, giới thiệu lịch sử, thiên nhiên và văn hoá vùng bắc tỉnh Volgograd. Kamyshin còn nổi tiếng là quê hương của phi công anh hùng Alexei Maresyev.",
    "Bảo tàng Lịch sử - Địa phương học Kamyshin (Камышинский историко-краеведческий музей) là điểm đến văn hoá chính của Kamyshin - một thành phố cảng sông cổ ở phía bắc tỉnh Volgograd, từng phát đạt nhờ buôn bán dưa hấu và giao thương trên sông Volga. Bảo tàng được đặt trong một toà nhà lịch sử duyên dáng, trưng bày các bộ sưu tập đa dạng về thiên nhiên thảo nguyên và cổ sinh vật của vùng (khu vực này nổi tiếng với những phát hiện hoá thạch và di chỉ địa chất), về lịch sử hình thành thành phố, đời sống thương nhân, thủ công và văn hoá dân gian địa phương. Một phần quan trọng dành cho những người con nổi bật của Kamyshin, đặc biệt là phi công huyền thoại Alexei Maresyev - người vẫn tiếp tục lái máy bay chiến đấu sau khi bị cụt cả hai chân, nguyên mẫu cho tác phẩm văn học nổi tiếng. Với du khách đi dọc sông Volga hoặc trên hành trình về phía hồ muối Elton, bảo tàng là dịp tốt để hiểu nhịp sống và bản sắc của vùng tỉnh Volgograd bên ngoài thành phố lớn.",
    [
        "Bảo tàng chính của thành phố cảng sông cổ Kamyshin bên bờ Volga.",
        "Trưng bày thiên nhiên, cổ sinh vật, lịch sử thương mại và văn hoá dân gian vùng.",
        "Tôn vinh phi công anh hùng Alexei Maresyev, người con của Kamyshin.",
    ],
    p("Thường mở cửa khoảng 9:00–18:00, có thể nghỉ một ngày trong tuần; nên kiểm tra trước.",
      "Vé vào cửa phải trả phí, mức phổ thông (có ưu đãi).",
      "Khoảng 1 giờ.",
      "Quanh năm; kết hợp khi ghé Kamyshin trên đường tới hồ Elton hoặc dọc sông Volga.",
      "Hỏi về khu trưng bày phi công Maresyev; kết hợp dạo bờ sông Volga ở Kamyshin."),
    [
        {"title": "Wikipedia (RU) — Камышин", "url": "https://ru.wikipedia.org/wiki/Камышин"},
    ],
    ["museum", "history", "local-lore", "kamyshin", "volga", "volgograd"],
    maps_text("Камышинский историко-краеведческий музей", "Камышин", "Kamyshin Museum of Local Lore", "Kamyshin", 50.09417, 45.41528),
))

# ============================ NHÀ HÁT & CÔNG TRÌNH BIỂU TƯỢNG ============================

# 16) Новый Экспериментальный Театр (НЭТ) -----------------------------------------
RECORDS.append(rec(
    "new-experimental-theatre-volgograd",
    "Nhà hát Thử nghiệm Mới NET (phiên âm: Nô-vưi Ếch-xpe-ri-men-tan-nưi Te-atr)",
    "Волгоградский Новый Экспериментальный Театр (НЭТ)",
    "Volgograd New Experimental Theatre",
    ["theatre"],
    48.70917, 44.51583,
    "Đại lộ Lenin 5, trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Nhà hát Thử nghiệm Mới (NET) là nhà hát kịch nổi tiếng nhất Volgograd, hoạt động trong toà nhà nhà hát kịch lịch sử ở trung tâm. Nổi bật với các dàn dựng táo bạo, đây là một trong những sân khấu được yêu thích và tranh luận nhiều nhất thành phố.",
    "Nhà hát Thử nghiệm Mới (Новый Экспериментальный Театр, viết tắt NET/НЭТ) là nhà hát kịch hàng đầu của Volgograd, nổi tiếng khắp nước Nga nhờ phong cách dàn dựng táo bạo và giàu tính thử nghiệm. Nhà hát hoạt động trong toà nhà nhà hát kịch lịch sử ở ngay trung tâm thành phố, một công trình đã gắn bó với đời sống sân khấu địa phương suốt nhiều thập niên. Dưới bàn tay của các đạo diễn giàu cá tính, NET xây dựng được một tiết mục đa dạng, từ kịch kinh điển Nga và thế giới đến những vở diễn hiện đại gây tranh luận, thu hút đông đảo khán giả và không ít lần trở thành tâm điểm chú ý của giới phê bình. Không gian khán phòng trang nhã cùng chất lượng biểu diễn cao khiến một buổi tối xem kịch tại đây trở thành trải nghiệm văn hoá đáng nhớ. Nằm trên đại lộ trung tâm, gần Quảng trường Các Chiến Sĩ và Đại lộ Anh Hùng, nhà hát là lựa chọn tuyệt vời để cảm nhận nhịp sống văn hoá đương đại của Volgograd, bên cạnh các điểm tưởng niệm chiến tranh.",
    [
        "Nhà hát kịch hàng đầu Volgograd, nổi tiếng với dàn dựng táo bạo, thử nghiệm.",
        "Hoạt động trong toà nhà nhà hát kịch lịch sử ở trung tâm.",
        "Tiết mục đa dạng từ kịch kinh điển tới các vở diễn hiện đại gây tranh luận.",
    ],
    p("Buổi diễn thường bắt đầu buổi tối; phòng vé mở ban ngày. Kiểm tra lịch diễn và đặt vé trước.",
      "Vé xem biểu diễn phải trả phí, tuỳ vở và vị trí ghế.",
      "Buổi diễn khoảng 2–3 giờ.",
      "Mùa diễn thường từ thu đến xuân; kiểm tra lịch trước khi tới.",
      "Đặt vé trước qua trang chính thức; đến sớm để chiêm ngưỡng nội thất khán phòng."),
    [
        {"title": "Wikipedia (RU) — Волгоградский Новый Экспериментальный театр", "url": "https://ru.wikipedia.org/wiki/Волгоградский_Новый_экспериментальный_театр"},
    ],
    ["theatre", "drama", "culture", "performing-arts", "center", "volgograd"],
    maps_text("Новый Экспериментальный театр", "Волгоград", "New Experimental Theatre", "Volgograd", 48.70917, 44.51583),
))

# 17) Волгоградский музыкальный театр ---------------------------------------------
RECORDS.append(rec(
    "musical-theatre-volgograd",
    "Nhà hát Nhạc kịch Volgograd (phiên âm: Mu-dư-kan-nưi te-atr)",
    "Волгоградский музыкальный театр",
    "Volgograd Musical Theatre",
    ["theatre"],
    48.70611, 44.51694,
    "Bờ kè Tập đoàn quân 62 số 6, trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Nhà hát Nhạc kịch Volgograd là sân khấu chuyên về operetta, nhạc kịch và các vở diễn ca nhạc, toạ lạc ngay bên bờ sông Volga. Với lịch sử lâu đời, đây là một trong những nhà hát được yêu thích của thành phố.",
    "Nhà hát Nhạc kịch Volgograd (Волгоградский музыкальный театр) là sân khấu ca nhạc chủ đạo của thành phố, chuyên trình diễn operetta, nhạc kịch (musical), các vở ca nhạc và chương trình hoà nhạc. Có nguồn gốc từ giữa thế kỷ 20, nhà hát đã xây dựng được truyền thống biểu diễn lâu đời và một lượng khán giả trung thành qua nhiều thế hệ. Tiết mục của nhà hát trải rộng từ những vở operetta cổ điển vui tươi của châu Âu đến các tác phẩm ca nhạc Nga và Xô viết, mang lại những buổi tối giải trí nhẹ nhàng, giàu giai điệu và màu sắc. Toà nhà nằm ở vị trí đắc địa ngay bên bờ kè sông Volga, gần Đại lộ Anh Hùng, nên việc đi xem một buổi diễn ở đây có thể kết hợp thuận tiện với một buổi dạo bộ ven sông lãng mạn. Đối với du khách muốn trải nghiệm đời sống văn hoá 'nhẹ nhàng' hơn của Volgograd, giữa những điểm tưởng niệm nặng tính lịch sử, nhà hát nhạc kịch là một lựa chọn dễ chịu và đáng thử.",
    [
        "Sân khấu chuyên operetta, nhạc kịch và các vở ca nhạc của Volgograd.",
        "Toạ lạc ngay bên bờ kè sông Volga, gần Đại lộ Anh Hùng.",
        "Truyền thống biểu diễn lâu đời với lượng khán giả trung thành.",
    ],
    p("Buổi diễn thường vào buổi tối; phòng vé mở ban ngày. Kiểm tra lịch và đặt vé trước.",
      "Vé xem biểu diễn phải trả phí, tuỳ vở và vị trí ghế.",
      "Buổi diễn khoảng 2–2,5 giờ.",
      "Mùa diễn thu–xuân; kiểm tra lịch trước khi tới.",
      "Kết hợp dạo bờ kè sông Volga trước hoặc sau buổi diễn."),
    [
        {"title": "Wikipedia (RU) — Волгоградский музыкальный театр", "url": "https://ru.wikipedia.org/wiki/Волгоградский_музыкальный_театр"},
    ],
    ["theatre", "operetta", "musical", "culture", "riverside", "volgograd"],
    maps_text("Волгоградский музыкальный театр", "Волгоград", "Volgograd Musical Theatre", "Volgograd", 48.70611, 44.51694),
))

# 18) Волгоградский областной театр кукол -----------------------------------------
RECORDS.append(rec(
    "puppet-theatre-volgograd",
    "Nhà hát Múa rối tỉnh Volgograd (phiên âm: Te-atr ku-kôn)",
    "Волгоградский областной театр кукол",
    "Volgograd Regional Puppet Theatre",
    ["theatre"],
    48.71056, 44.51667,
    "Đại lộ Lenin 15, trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Nhà hát Múa rối tỉnh Volgograd là một trong những nhà hát lâu đời nhất thành phố, chuyên các vở diễn rối dành cho thiếu nhi và gia đình. Đây là điểm đến văn hoá được nhiều thế hệ trẻ em Volgograd yêu thích.",
    "Nhà hát Múa rối tỉnh Volgograd (Волгоградский областной театр кукол) là một trong những nhà hát có tuổi đời lâu nhất của thành phố, ra đời từ những năm 1930 và tồn tại qua cả những năm tháng chiến tranh tàn khốc. Chuyên về nghệ thuật múa rối, nhà hát dàn dựng các vở diễn dựa trên truyện cổ tích Nga và thế giới, truyện dân gian và văn học thiếu nhi, với những con rối được chế tác tinh xảo và sân khấu nhiều màu sắc. Đây là nơi gắn bó với tuổi thơ của nhiều thế hệ người Volgograd, thường là 'nhà hát đầu tiên' mà các em nhỏ được đưa tới. Bên cạnh giá trị giải trí, các vở diễn còn mang tính giáo dục nhẹ nhàng, nuôi dưỡng trí tưởng tượng và tình yêu nghệ thuật cho trẻ em. Với các gia đình có con nhỏ đang du lịch Volgograd, đây là một điểm đến ấm áp, khác hẳn không khí trầm mặc của các đài tưởng niệm; còn với người lớn, nghệ thuật múa rối truyền thống Nga cũng là một trải nghiệm văn hoá thú vị. Nhà hát nằm ngay trên đại lộ trung tâm, rất dễ tiếp cận.",
    [
        "Một trong những nhà hát lâu đời nhất Volgograd (từ thập niên 1930).",
        "Chuyên các vở múa rối cho thiếu nhi dựa trên truyện cổ tích, dân gian.",
        "Điểm đến gia đình ấm áp ngay trung tâm, gắn với tuổi thơ nhiều thế hệ.",
    ],
    p("Buổi diễn thường vào cuối tuần và các buổi trong ngày; phòng vé mở ban ngày. Kiểm tra lịch trước.",
      "Vé xem biểu diễn phải trả phí, mức phải chăng, phù hợp gia đình.",
      "Buổi diễn khoảng 45 phút–1 giờ.",
      "Quanh năm; cuối tuần thường có nhiều suất diễn cho thiếu nhi.",
      "Phù hợp gia đình có trẻ nhỏ; đặt vé trước vào cuối tuần và dịp lễ."),
    [
        {"title": "Wikipedia (RU) — Волгоградский областной театр кукол", "url": "https://ru.wikipedia.org/wiki/Волгоградский_областной_театр_кукол"},
    ],
    ["theatre", "puppet", "family", "children", "culture", "volgograd"],
    maps_text("Волгоградский областной театр кукол", "Волгоград", "Volgograd Puppet Theatre", "Volgograd", 48.71056, 44.51667),
))

# 19) Волгоградский планетарий ----------------------------------------------------
RECORDS.append(rec(
    "volgograd-planetarium",
    "Cung Thiên văn Volgograd (phiên âm: Pla-nhe-ta-ri)",
    "Волгоградский планетарий",
    "Volgograd Planetarium",
    ["other"],
    48.72472, 44.51056,
    "Phố Gagarina 14, trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Cung Thiên văn Volgograd là một trong những cung thiên văn đẹp và cổ nhất nước Nga, khánh thành năm 1954 như 'món quà' từ nhân dân Đức. Toà nhà mang kiến trúc Stalin hoành tráng với đài thiên văn và bức tượng của nhà điêu khắc Vera Mukhina trên nóc.",
    "Cung Thiên văn Volgograd (Волгоградский планетарий) là một viên ngọc kiến trúc thời hậu chiến và là một trong những cung thiên văn được yêu thích nhất nước Nga. Được khánh thành năm 1954, công trình ra đời như một 'món quà' của nhân dân Cộng hoà Dân chủ Đức gửi tặng thành phố anh hùng đang hồi sinh từ đống tro tàn. Toà nhà mang phong cách Stalin bề thế với hàng cột, mái vòm và trang trí công phu; trên nóc là bức tượng do nữ điêu khắc gia lừng danh Vera Mukhina (tác giả tượng 'Công nhân và Nữ nông trang viên') thiết kế. Bên trong, khán phòng hình vòm với máy chiếu sao cho phép du khách 'du hành' qua bầu trời đêm, các chòm sao và hành tinh; nơi đây còn có đài quan sát với kính thiên văn để ngắm Mặt Trời và các thiên thể. Không chỉ là điểm giáo dục khoa học hấp dẫn cho cả trẻ em lẫn người lớn, cung thiên văn còn là một chứng tích văn hoá độc đáo về tình đoàn kết và công cuộc tái thiết thành phố sau chiến tranh. Đây là một điểm đến khác lạ, dễ chịu giữa các di tích quân sự của Volgograd.",
    [
        "Một trong những cung thiên văn cổ và đẹp nhất Nga, khánh thành năm 1954.",
        "Kiến trúc Stalin bề thế với tượng trên nóc của điêu khắc gia Vera Mukhina.",
        "Có khán phòng chiếu sao và đài quan sát với kính thiên văn.",
    ],
    p("Thường mở cửa theo lịch buổi chiếu, khoảng 10:00–18:00, nghỉ một ngày trong tuần; kiểm tra trước.",
      "Vé xem buổi chiếu và tham quan phải trả phí, mức phổ thông (có ưu đãi).",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; buổi quan sát Mặt Trời phụ thuộc thời tiết quang mây.",
      "Kiểm tra lịch buổi chiếu vòm sao và quan sát thiên văn trước khi đến; phù hợp gia đình."),
    [
        {"title": "Wikipedia (RU) — Волгоградский планетарий", "url": "https://ru.wikipedia.org/wiki/Волгоградский_планетарий"},
    ],
    ["other", "planetarium", "science", "architecture", "stalinist", "volgograd"],
    maps_text("Волгоградский планетарий", "Волгоград", "Volgograd Planetarium", "Volgograd", 48.72472, 44.51056),
))

# 20) Железнодорожный вокзал Волгоград-1 ------------------------------------------
RECORDS.append(rec(
    "volgograd-1-railway-station",
    "Ga đường sắt Volgograd-1 (phiên âm: Vôc-dan Vôn-ga-grát Ađin)",
    "Железнодорожный вокзал Волгоград-1",
    "Volgograd-1 Railway Station",
    ["other"],
    48.71194, 44.50889,
    "Quảng trường Nhà ga 1, trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Nhà ga trung tâm Volgograd-1 là một công trình tiêu biểu của kiến trúc Stalin hậu chiến, xây dựng lại vào năm 1954 với sảnh lớn, tháp đồng hồ và trang trí lộng lẫy. Đây vừa là cửa ngõ giao thông vừa là một điểm ngắm kiến trúc của thành phố.",
    "Nhà ga đường sắt Volgograd-1 (Волгоград-1) là một trong những công trình kiến trúc ấn tượng nhất thành phố và là ví dụ điển hình cho phong cách 'đế chế Stalin' (Stalinist Empire) của thời kỳ tái thiết sau chiến tranh. Nhà ga hiện tại được xây dựng lại và khánh thành năm 1954, thay cho công trình cũ đã bị phá huỷ trong Trận Stalingrad. Toà nhà gây ấn tượng với khối kiến trúc đối xứng bề thế, tháp trung tâm cao vút gắn đồng hồ và ngôi sao, cùng phần trang trí giàu chi tiết. Nội thất sảnh chính cũng nguy nga không kém, với trần cao, đèn chùm, phù điêu và tranh tường mô tả những đề tài lịch sử - lao động theo tinh thần thời đại. Với hàng triệu lượt khách qua lại mỗi năm, nhà ga không chỉ là điểm khởi đầu hay kết thúc của các chuyến tàu đường dài, mà còn là một 'cung điện của nhân dân' đúng nghĩa - nơi kiến trúc phục vụ đời sống thường nhật. Đối với du khách, dừng chân ngắm nhìn nhà ga và quảng trường phía trước là cách hay để cảm nhận diện mạo đô thị Volgograd thời hậu chiến.",
    [
        "Công trình tiêu biểu của kiến trúc 'đế chế Stalin', xây lại năm 1954.",
        "Tháp đồng hồ cao, sảnh nội thất nguy nga với phù điêu và tranh tường.",
        "Vừa là cửa ngõ giao thông vừa là điểm ngắm kiến trúc hậu chiến của thành phố.",
    ],
    p("Nhà ga hoạt động suốt ngày; có thể vào sảnh tham quan tự do (lưu ý an ninh nhà ga).",
      "Miễn phí tham quan bên ngoài và sảnh; vé tàu mua riêng nếu đi tàu.",
      "Khoảng 20–30 phút.",
      "Quanh năm; ban ngày dễ chiêm ngưỡng chi tiết kiến trúc và tháp đồng hồ.",
      "Chú ý phù điêu và tranh trần trong sảnh chính; giữ đồ cẩn thận nơi đông người."),
    [
        {"title": "Wikipedia (RU) — Волгоград I (вокзал)", "url": "https://ru.wikipedia.org/wiki/Волгоград-I"},
    ],
    ["other", "architecture", "railway-station", "stalinist", "landmark", "volgograd"],
    maps_text("Железнодорожный вокзал Волгоград-1", "Волгоград", "Volgograd-1 Railway Station", "Volgograd", 48.71194, 44.50889),
))

# ============================ THỂ THAO, CẦU, CÔNG VIÊN & THIÊN NHIÊN ============================

# 21) «Волгоград Арена» -----------------------------------------------------------
RECORDS.append(rec(
    "volgograd-arena-stadium",
    "Sân vận động «Volgograd Arena» (phiên âm: Vôn-ga-grát A-rê-na)",
    "«Волгоград Арена»",
    "Volgograd Arena",
    ["other"],
    48.78472, 44.53528,
    "Đại lộ Lenin 76, dưới chân đồi Mamayev Kurgan, thành phố Volgograd, tỉnh Volgograd, Nga",
    "«Volgograd Arena» là sân vận động hiện đại sức chứa khoảng 45.000 chỗ, xây cho World Cup 2018 ngay dưới chân đồi Mamayev Kurgan. Với thiết kế mặt ngoài dạng lưới thanh mảnh độc đáo, đây là công trình thể thao biểu tượng mới của thành phố.",
    "«Volgograd Arena» là sân vận động hiện đại và là một trong những công trình mới nổi bật nhất của thành phố, được xây dựng để phục vụ Giải vô địch bóng đá thế giới FIFA World Cup 2018. Sân toạ lạc ở vị trí giàu ý nghĩa, ngay dưới chân đồi Mamayev Kurgan và gần bờ sông Volga, trên nền một sân vận động cũ. Điểm nhấn kiến trúc của công trình là lớp vỏ ngoài dạng lưới kim loại đan chéo thanh mảnh bao quanh khối sân, tạo hiệu ứng thị giác nhẹ nhàng, hiện đại và được đánh giá cao. Với sức chứa khoảng 45.000 khán giả, sân đã tổ chức các trận đấu World Cup 2018 và hiện là sân nhà của câu lạc bộ bóng đá địa phương, đồng thời là nơi diễn ra các sự kiện thể thao, hoà nhạc và hoạt động cộng đồng. Từ khu vực sân, du khách có thể phóng tầm mắt lên tượng «Tổ quốc vẫy gọi» trên đỉnh Mamayev Kurgan, tạo nên sự đối thoại thú vị giữa quá khứ hào hùng và hiện tại năng động. Đây là điểm đến hấp dẫn cho người hâm mộ thể thao và những ai quan tâm tới kiến trúc đương đại.",
    [
        "Sân vận động ~45.000 chỗ xây cho World Cup 2018.",
        "Mặt ngoài dạng lưới kim loại đan chéo thanh mảnh, kiến trúc đương đại nổi bật.",
        "Nằm ngay dưới chân đồi Mamayev Kurgan, gần sông Volga.",
    ],
    p("Khu vực bên ngoài tham quan tự do; vào bên trong theo ngày có trận đấu, sự kiện hoặc tour.",
      "Miễn phí khu vực ngoài; vé xem trận đấu/sự kiện mua riêng.",
      "Khoảng 30 phút (bên ngoài) hoặc theo sự kiện.",
      "Quanh năm; sôi động nhất vào ngày có trận đấu bóng đá.",
      "Kết hợp với chuyến thăm Mamayev Kurgan ngay cạnh; kiểm tra lịch thi đấu nếu muốn vào xem."),
    [
        {"title": "Wikipedia (RU) — Волгоград Арена", "url": "https://ru.wikipedia.org/wiki/Волгоград_Арена"},
    ],
    ["other", "stadium", "football", "world-cup-2018", "modern", "volgograd"],
    maps_text("Волгоград Арена", "Волгоград", "Volgograd Arena", "Volgograd", 48.78472, 44.53528),
))

# 22) Волгоградский «танцующий» мост ----------------------------------------------
RECORDS.append(rec(
    "volgograd-dancing-bridge",
    "Cầu Volgograd - «cây cầu nhảy múa» (phiên âm: Tan-txu-si mốt)",
    "Волгоградский мост («танцующий мост»)",
    "Volgograd Bridge (the 'Dancing Bridge')",
    ["bridge"],
    48.75222, 44.60611,
    "Bắc qua sông Volga, nối trung tâm Volgograd với tả ngạn, thành phố Volgograd, tỉnh Volgograd, Nga",
    "Cầu Volgograd là cây cầu đường bộ dài bắc qua sông Volga, khánh thành năm 2009. Năm 2010, cầu bất ngờ nổi tiếng toàn cầu khi dao động uốn lượn mạnh trong gió, được đặt biệt danh «cây cầu nhảy múa».",
    "Cầu Volgograd (Волгоградский мост) là công trình hạ tầng lớn bắc qua sông Volga, nối trung tâm thành phố với vùng tả ngạn, được khánh thành năm 2009 sau nhiều năm xây dựng. Cây cầu vốn được kỳ vọng cải thiện giao thông cho khu vực, nhưng lại trở nên nổi tiếng thế giới vì một lý do bất ngờ: vào tháng 5 năm 2010, dưới tác động của gió mạnh, nhịp cầu bắt đầu dao động uốn lượn thành những 'con sóng' rõ rệt theo phương thẳng đứng. Các đoạn video ghi lại cảnh mặt cầu 'nhấp nhô như sóng' lan truyền khắp thế giới, khiến báo chí quốc tế đặt cho nó biệt danh «cây cầu nhảy múa» (dancing bridge). Hiện tượng cộng hưởng do gió này sau đó đã được khắc phục bằng việc lắp đặt các bộ giảm chấn, giúp cầu ổn định và an toàn trở lại. Ngày nay, cầu Volgograd hoạt động bình thường và là một trong những cây cầu vượt sông dài đáng chú ý ở Nga; với du khách, cái tên 'cây cầu nhảy múa' và câu chuyện đằng sau nó khiến công trình trở thành một điểm tham quan thú vị, đặc biệt khi ngắm từ bờ kè.",
    [
        "Cầu đường bộ dài bắc qua sông Volga, khánh thành năm 2009.",
        "Nổi tiếng thế giới năm 2010 khi dao động uốn lượn trong gió - «cây cầu nhảy múa».",
        "Đã được lắp giảm chấn để ổn định; là điểm ngắm cảnh sông Volga độc đáo.",
    ],
    p("Cầu giao thông hoạt động suốt ngày; ngắm cảnh từ bờ kè hoặc khi qua cầu.",
      "Miễn phí.",
      "Khoảng 15–20 phút (ngắm cảnh).",
      "Cuối xuân đến đầu thu; hoàng hôn trên sông Volga rất đẹp.",
      "Ngắm và chụp cầu từ bờ kè trung tâm; tìm hiểu câu chuyện 'cầu nhảy múa' năm 2010."),
    [
        {"title": "Wikipedia (RU) — Волгоградский мост", "url": "https://ru.wikipedia.org/wiki/Волгоградский_мост"},
    ],
    ["bridge", "volga", "engineering", "landmark", "modern", "volgograd"],
    maps_text("Волгоградский мост", "Волгоград", "Volgograd Dancing Bridge", "Volgograd", 48.75222, 44.60611),
))

# 23) Речной вокзал Волгограда ----------------------------------------------------
RECORDS.append(rec(
    "volgograd-river-station",
    "Bến tàu sông Volgograd (phiên âm: Rê-tri-nôi vôc-dan)",
    "Речной вокзал Волгограда",
    "Volgograd River Station",
    ["other"],
    48.70361, 44.51750,
    "Bờ kè Tập đoàn quân 62, trung tâm thành phố Volgograd, tỉnh Volgograd, Nga",
    "Bến tàu sông Volgograd được xem là bến tàu sông lớn nhất châu Âu, một công trình bê tông đồ sộ thời Xô viết bên bờ Volga. Ngoài chức năng bến tàu, đây còn là trung tâm hoà nhạc và sự kiện của thành phố.",
    "Bến tàu sông Volgograd (Речной вокзал) là một công trình gây choáng ngợp bởi quy mô, thường được nhắc tới như bến tàu sông lớn nhất châu Âu. Được xây dựng vào thập niên 1970–1980 dọc bờ kè sông Volga ở trung tâm thành phố, toà nhà là một khối kiến trúc hiện đại (modernist) khổng lồ, kéo dài hàng trăm mét với những đường nét bê tông mạnh mẽ đặc trưng cho thời kỳ cuối Xô viết. Nguyên thuỷ, đây là đầu mối cho các tuyến tàu thuỷ chở khách xuôi ngược sông Volga và các tuyến du lịch đường sông. Ngày nay, bên cạnh vai trò bến tàu, phần lớn không gian bên trong đã được cải tạo thành một trung tâm hoà nhạc và sự kiện lớn (concert hall), thường xuyên đón các buổi biểu diễn ca nhạc, sự kiện văn hoá và hội nghị. Vị trí ngay trên bờ kè trung tâm, gần chân Đại lộ Anh Hùng, khiến bến tàu sông trở thành một điểm mốc dễ nhận biết và là nơi lý tưởng để bắt đầu một chuyến du thuyền ngắm thành phố từ mặt nước, hoặc đơn giản là dạo bộ ngắm sông Volga.",
    [
        "Được xem là bến tàu sông lớn nhất châu Âu, xây thập niên 1970–1980.",
        "Khối kiến trúc modernist bê tông đồ sộ bên bờ kè sông Volga.",
        "Vừa là bến tàu, vừa là trung tâm hoà nhạc và sự kiện của thành phố.",
    ],
    p("Khu vực bờ kè và bên ngoài tham quan tự do; bên trong theo lịch sự kiện, buổi diễn.",
      "Miễn phí khu vực ngoài; vé sự kiện/du thuyền mua riêng.",
      "Khoảng 20–30 phút (bên ngoài).",
      "Cuối xuân đến đầu thu, mùa du thuyền trên sông; buổi tối có sự kiện.",
      "Hỏi về các tuyến du thuyền ngắm sông Volga; kết hợp dạo bờ kè và Đại lộ Anh Hùng."),
    [
        {"title": "Wikipedia (RU) — Речной вокзал (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Речной_вокзал_(Волгоград)"},
    ],
    ["other", "river-station", "modernist", "concert-hall", "volga", "volgograd"],
    maps_text("Речной вокзал", "Волгоград", "Volgograd River Station", "Volgograd", 48.70361, 44.51750),
))

# 24) Комсомольский сад -----------------------------------------------------------
RECORDS.append(rec(
    "komsomol-garden-volgograd",
    "Vườn Komsomol (phiên âm: Kôm-xa-môn-xki xát)",
    "Комсомольский сад",
    "Komsomol Garden",
    ["park_garden"],
    48.70694, 44.51306,
    "Trung tâm thành phố Volgograd, gần Quảng trường Các Chiến Sĩ Đã Ngã Xuống, tỉnh Volgograd, Nga",
    "Vườn Komsomol là công viên xanh mát ở ngay trung tâm Volgograd, một ốc đảo yên tĩnh giữa phố phường. Trong công viên có mộ và tượng đài của người anh hùng Ruben Ibarruri cùng nhiều đài tưởng niệm khác.",
    "Vườn Komsomol (Комсомольский сад) là một trong những công viên trung tâm lâu đời và được yêu thích của Volgograd, có nguồn gốc từ một khu vườn thành phố trước cách mạng. Nằm sát Quảng trường Các Chiến Sĩ Đã Ngã Xuống, công viên là một khoảng xanh dễ chịu với những hàng cây bóng mát, lối đi lát đá, ghế nghỉ và đài phun nước, nơi người dân thành phố tản bộ, thư giãn quanh năm. Bên cạnh chức năng nghỉ ngơi, công viên còn mang ý nghĩa tưởng niệm: tại đây có ngôi mộ và tượng đài của Ruben Ruiz Ibarruri - người con của nữ lãnh tụ cộng sản Tây Ban Nha Dolores Ibarruri ('La Pasionaria'), đã chiến đấu và hy sinh trong Trận Stalingrad, cùng một số bia và tượng tưởng niệm khác. Sự đan xen giữa không gian xanh thư thái và các chứng tích lịch sử là nét đặc trưng của nhiều địa điểm ở Volgograd. Với du khách, Vườn Komsomol là nơi lý tưởng để nghỉ chân, tránh nắng và tận hưởng nhịp sống thường nhật của thành phố, ngay giữa hành trình tham quan các điểm tưởng niệm trung tâm.",
    [
        "Công viên xanh trung tâm lâu đời, sát Quảng trường Các Chiến Sĩ.",
        "Có mộ và tượng đài Ruben Ibarruri, anh hùng hy sinh trong Trận Stalingrad.",
        "Ốc đảo yên tĩnh để nghỉ chân giữa các điểm tham quan trung tâm.",
    ],
    p("Không gian công cộng ngoài trời, dạo chơi tự do suốt ngày.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Cuối xuân đến đầu thu khi cây xanh mát; mùa hè là chỗ tránh nắng lý tưởng.",
      "Tìm tượng đài và mộ Ruben Ibarruri; kết hợp nghỉ chân giữa lịch trình tham quan trung tâm."),
    [
        {"title": "Wikipedia (RU) — Комсомольский сад (Волгоград)", "url": "https://ru.wikipedia.org/wiki/Комсомольский_сад_(Волгоград)"},
    ],
    ["park_garden", "park", "memorial", "green-space", "center", "volgograd"],
    maps_text("Комсомольский сад", "Волгоград", "Komsomol Garden", "Volgograd", 48.70694, 44.51306),
))

# 25) Озеро Эльтон ----------------------------------------------------------------
RECORDS.append(rec(
    "lake-elton",
    "Hồ muối Elton (phiên âm: Ô-dê-ra En-tôn)",
    "Озеро Эльтон",
    "Lake Elton",
    ["other"],
    49.13333, 46.66667,
    "Huyện Palasovka, gần biên giới Kazakhstan, phía đông tỉnh Volgograd, Nga",
    "Hồ Elton là hồ muối tự tiết lớn nhất châu Âu, mặt nước ánh sắc hồng đỏ đặc trưng nhờ vi tảo và khoáng chất. Đây là điểm du lịch thiên nhiên - chữa lành nổi tiếng, với bùn khoáng và nước muối được dùng để trị liệu.",
    "Hồ Elton (Озеро Эльтон) là kỳ quan thiên nhiên nổi bật nhất của tỉnh Volgograd và là hồ muối tự tiết (self-precipitating) lớn nhất châu Âu, nằm ở vùng thảo nguyên khô hạn phía đông tỉnh, gần biên giới với Kazakhstan. Với độ mặn rất cao, nước hồ đặc sánh và thường ánh lên những sắc hồng, đỏ, tím tuyệt đẹp do các loài vi tảo ưa mặn và khoáng chất tạo nên, khiến khung cảnh trở nên siêu thực, tựa như 'mặt hồ trên sao Hoả' hay 'biển hồng'. Xung quanh là thảo nguyên mênh mông, những cồn muối trắng và các suối khoáng đổ vào hồ. Từ lâu, Elton đã nổi tiếng như một trung tâm điều dưỡng - chữa lành: bùn khoáng đen và nước muối (rapa) của hồ được dùng trong các liệu pháp trị bệnh xương khớp, da liễu và thần kinh, và tại đây có khu điều dưỡng (sanatorium) phục vụ du khách. Đối với người yêu thiên nhiên và nhiếp ảnh, cảnh bình minh, hoàng hôn phản chiếu trên mặt hồ phẳng lặng là trải nghiệm khó quên. Dù nằm khá xa thành phố Volgograd, Elton vẫn là điểm đến đáng để dành trọn một chuyến đi cho những ai muốn khám phá thiên nhiên độc đáo của vùng.",
    [
        "Hồ muối tự tiết lớn nhất châu Âu, mặt nước ánh sắc hồng đỏ siêu thực.",
        "Trung tâm điều dưỡng - chữa lành với bùn khoáng đen và nước muối trị liệu.",
        "Cảnh thảo nguyên, cồn muối và bình minh/hoàng hôn tuyệt đẹp cho nhiếp ảnh.",
    ],
    p("Không gian thiên nhiên ngoài trời, tham quan ban ngày; khu điều dưỡng có giờ riêng.",
      "Tham quan hồ cơ bản miễn phí; dịch vụ điều dưỡng, trị liệu, lưu trú phải trả phí.",
      "Nửa ngày đến trọn ngày (hoặc lưu trú nhiều ngày để điều dưỡng).",
      "Cuối xuân đến đầu thu (khoảng tháng 5–9); mùa hè màu nước hồng đỏ rõ nhất.",
      "Mang mũ, kem chống nắng và nhiều nước; không tự ý dùng bùn/nước muối trị liệu khi chưa có tư vấn. Đi giày phù hợp cho nền muối."),
    [
        {"title": "Wikipedia (RU) — Эльтон (озеро)", "url": "https://ru.wikipedia.org/wiki/Эльтон_(озеро)"},
    ],
    ["other", "nature", "salt-lake", "pink-lake", "health-resort", "volgograd"],
    maps_text("Озеро Эльтон", "Волгоградская область", "Lake Elton", "Volgograd Oblast", 49.13333, 46.66667),
))

# 26) Площадь Ленина (Волжский) ---------------------------------------------------
RECORDS.append(rec(
    "volzhsky-lenin-square",
    "Quảng trường Lenin ở Volzhsky (phiên âm: Plô-ssat Lê-nhi-na, Vôn-giơ-xki)",
    "Площадь Ленина (Волжский)",
    "Lenin Square (Volzhsky)",
    ["square_street"],
    48.78694, 44.77639,
    "Trung tâm thành phố Volzhsky, tỉnh Volgograd, Nga",
    "Quảng trường Lenin là trái tim của Volzhsky - đô thị vệ tinh được quy hoạch bài bản của Volgograd, dựng lên cùng công trình thuỷ điện Volzhskaya GES. Quảng trường rợp cây xanh, đài phun nước và kiến trúc hài hoà, tiêu biểu cho một 'thành phố kiểu mẫu' thời Xô viết.",
    "Quảng trường Lenin (Площадь Ленина) là trung tâm hành chính và văn hoá của Volzhsky - thành phố lớn thứ hai của tỉnh, nằm bên tả ngạn sông Volga đối diện Volgograd. Volzhsky là một đô thị 'sinh ra' trong thập niên 1950 để phục vụ việc xây dựng nhà máy thuỷ điện Volzhskaya GES, và được quy hoạch từ đầu như một thành phố kiểu mẫu với những đại lộ rộng, nhiều cây xanh và các khu nhà hài hoà. Quảng trường Lenin phản ánh rõ tinh thần ấy: một không gian trung tâm khoáng đạt với toà nhà hành chính, đài phun nước, thảm cây xanh, lối đi lát đá và tượng đài Lenin, nơi diễn ra các sự kiện thành phố, lễ hội và hoạt động thường nhật của người dân. Volzhsky nổi tiếng là một trong những thành phố nhiều cây xanh nhất vùng, và khu vực quanh quảng trường thể hiện điều đó qua những hàng cây bóng mát dễ chịu. Với du khách, ghé Volzhsky và quảng trường trung tâm là cách thú vị để thấy một khía cạnh khác của tỉnh Volgograd: không phải chiến tranh và tưởng niệm, mà là câu chuyện quy hoạch đô thị và xây dựng thời hậu chiến. Có thể kết hợp với chuyến thăm nhà máy thuỷ điện Volzhskaya GES gần đó.",
    [
        "Trung tâm của Volzhsky - đô thị vệ tinh quy hoạch kiểu mẫu bên tả ngạn Volga.",
        "Không gian rợp cây xanh, đài phun nước, tượng đài Lenin và toà nhà hành chính.",
        "Tiêu biểu cho câu chuyện quy hoạch đô thị thời hậu chiến, gắn với thuỷ điện Volzhskaya.",
    ],
    p("Không gian công cộng ngoài trời, dạo chơi tự do suốt ngày.",
      "Miễn phí.",
      "Khoảng 30 phút.",
      "Cuối xuân đến đầu thu khi cây xanh mát và đài phun nước hoạt động.",
      "Kết hợp thăm nhà máy thuỷ điện Volzhskaya GES; Volzhsky nổi tiếng nhiều cây xanh, hợp dạo bộ."),
    [
        {"title": "Wikipedia (RU) — Волжский (Волгоградская область)", "url": "https://ru.wikipedia.org/wiki/Волжский_(Волгоградская_область)"},
    ],
    ["square_street", "city-square", "soviet-planning", "volzhsky", "green-city", "volgograd"],
    maps_text("Площадь Ленина", "Волжский", "Lenin Square Volzhsky", "Volzhsky", 48.78694, 44.77639),
))


def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    existing_slugs = {q.get("slug") for q in data}
    existing_ids = {q.get("id") for q in data}

    added, skipped = [], []
    for r in RECORDS:
        if r["slug"] in existing_slugs or r["id"] in existing_ids:
            skipped.append(r["slug"])
            continue
        data.append(r)
        existing_slugs.add(r["slug"])
        existing_ids.add(r["id"])
        added.append(r["slug"])

    if added:
        bak = f"{path}.bak_add_{TS}"
        shutil.copyfile(path, bak)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Backup: {os.path.basename(bak)}")

    print(f"REGION={REGION}  ADDED={len(added)}  SKIPPED(dup)={len(skipped)}  TOTAL_NOW={len(data)}")
    if added:
        print("  + " + "\n  + ".join(added))
    if skipped:
        print("  (skip dup): " + ", ".join(skipped))


if __name__ == "__main__":
    main()
