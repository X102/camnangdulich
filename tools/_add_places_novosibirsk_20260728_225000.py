# -*- coding: utf-8 -*-
"""_add_places_novosibirsk_20260728_225000.py — VÙNG: Tỉnh Novosibirsk (Новосибирская область)
(lần chạy tự động 2026-07-28).

Bối cảnh: novosibirsk.json hiện có 7 địa điểm (NOVAT opera-ballet, Akademgorodok, Sở thú Novosibirsk,
Nhà thờ Alexander Nevsky, Biển hồ Ob, Bảo tàng kỹ thuật đường sắt Tây Siberia, Tượng đài Chuột phòng thí
nghiệm). Bổ sung 26 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 33.
TRÁNH trùng 7 điểm trên; KHÔNG thêm lại bảo tàng đường sắt / Akademgorodok tổng thể / Biển hồ Ob.

Trung tâm là thành phố Novosibirsk; mở rộng sang Академгородок (ботсад, музей Солнца), Бердск,
курорт Озеро Карачи (Chanovsky), Сузун (xưởng đúc tiền) và điểm thiên nhiên Карпысакский водопад (Toguchin).

Phân bố loại hình (26 bản ghi mới):
- museum (7): краеведческий, художественный, музей Солнца, музей Рериха, планетарий,
  музей мировой погребальной культуры, Сузун-Завод. Монетный двор.
- theatre (3): «Глобус», «Красный факел», Новосибирский цирк.
- church (3): Вознесенский собор, Троице-Владимирский собор, Часовня Николая Чудотворца (+monument).
- square_street (2): площадь Ленина, Красный проспект.
- bridge (3): Бугринский мост, Комсомольский ж/д мост, Новосибирский метромост.
- monument (3): вокзал Новосибирск-Главный, Стоквартирный дом, Монумент Славы.
- park_garden (4): ЦСБС, Заельцовский парк, курорт Озеро Карачи, Карпысакский водопад.
- other (1): город Бердск.

TOẠ ĐỘ — xác minh chéo (2GIS firm/geo carte-центр lon,lat trong og:image + link Маршрут; ru.wikipedia;
WebSearch snippet; 2026-07-28). Phạm vi Novosibirsk lat ~53.3–57, lon ~75–85 — tất cả toạ độ trong
phạm vi, KHÔNG đảo lat/lon:
  Часовня Николая 55.026463,82.92147 (2GIS, Красный пр.17а); краеведческий 55.028815,82.920267 (2GIS,
  Красный пр.23); художественный 55.021835,82.921243 (WebSearch/2GIS, Красный пр.5); музей Солнца
  55.061651,82.917003 (2GIS, Дуси Ковальчук 179/3 — địa chỉ hiện hành, site museumofsun.ru); музей
  Рериха 55.022805,82.920103 (2GIS, Коммунистическая 38); планетарий 54.980783,83.034906 (2GIS,
  Ключ-Камышенское плато 1/1); погребальной культуры 55.076114,83.064379 (2GIS, Военторговская 4/15,
  пос.Восход); Сузун монетный двор 53.786,82.314071 (2GIS, Сузун, Ленина 22в); «Глобус» 55.025576,
  82.929562 (2GIS/WebSearch, Каменская 1); «Красный факел» 55.028347,82.908263 (2GIS, Ленина 19);
  цирк 55.041804,82.909907 (2GIS, Челюскинцев 21); Вознесенский собор 55.042392,82.912383 (2GIS,
  Советская 91); Троице-Владимирский собор 54.984669,82.829157 (2GIS/WebSearch, Филатова 14а);
  площадь Ленина 55.029,82.9206; Красный проспект 55.030,82.9208 (đoạn trung tâm); Бугринский мост
  54.975185,82.962646 (ru.wiki/WebSearch); Комсомольский ж/д мост 54.961122,82.984353 (WebSearch/ruwiki);
  метромост 54.99425,82.9107 (điểm giữa nhịp qua sông Ob, giữa ga Студенческая 54.989278,82.906603 (2GIS)
  và ga Речной вокзал ~54.999,82.915); вокзал Новосибирск-Главный 55.035706,82.896166 (2GIS, Шамшурина 43);
  Стоквартирный дом 55.020882,82.924895 (2GIS, Красный пр.16); Монумент Славы 54.987074,82.873994 (2GIS,
  Сквер Славы); ЦСБС 54.820589,83.10452 (2GIS, Золотодолинская 101); Заельцовский парк 55.051474,82.840794
  (2GIS, Парковая 88); курорт Озеро Карачи 55.20465,76.57009 (WebSearch, Чановский р-н); Карпысакский
  водопад 55.053102,83.730957 (Yandex/WebSearch, Тогучинский р-н); Бердск 54.7551,83.0967 (WebSearch).

GHI CHÚ: KHÔNG thêm lại Akademgorodok / Bảo tàng đường sắt Tây Siberia / Biển hồ Ob (ĐÃ CÓ). Với
Музей Солнца dùng địa chỉ hiện hành (Дуси Ковальчук 179/3, theo 2GIS + trang chính thức) thay vì địa chỉ
Академгородок cũ. Метромост lấy toạ độ điểm giữa nhịp cầu qua sông Ob (trung điểm hai ga đầu cầu đã xác
minh). KHÔNG bịa toạ độ; các điểm không xác minh được đã bỏ qua.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_novosibirsk_20260728_225000.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "novosibirsk"
REGION_NAME_VI = "Tỉnh Novosibirsk"
FD = "Vùng Siberia"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def maps_org(yandex_org_url, name_en, city_en):
    """Ưu tiên URL trang tổ chức/địa điểm Yandex (chính xác nhất) + Google text-search."""
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": yandex_org_url,
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


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


def p(hours, ticket, duration, best, tips):
    return {"hours_vi": hours, "ticket_vi": ticket, "duration_vi": duration,
            "best_time_vi": best, "tips_vi": tips}


RECORDS = []

# ============================ BẢO TÀNG (museum) ============================

# 1) Bảo tàng Địa phương học Novosibirsk (краеведческий)
RECORDS.append(rec(
    "novosibirsk-regional-museum",
    "Bảo tàng Địa phương học Quốc gia Novosibirsk",
    "Новосибирский государственный краеведческий музей",
    "Novosibirsk State Regional (Local Lore) Museum",
    ["museum"],
    55.028815, 82.920267,
    "Đại lộ Krasny Prospekt 23, cạnh Quảng trường Lenin, trung tâm thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Bảo tàng lâu đời và lớn nhất tỉnh Novosibirsk, đặt trong Tòa Thương xá thành phố cổ kính bên Quảng trường Lenin. Nơi đây kể lại lịch sử, thiên nhiên và đời sống của cả vùng Siberia, với điểm nhấn là bộ xương voi ma mút hoàn chỉnh nổi tiếng.",
    "Bảo tàng Địa phương học Quốc gia Novosibirsk là bảo tàng lâu đời nhất và giàu hiện vật bậc nhất của vùng, ra đời từ năm 1920. Tòa nhà chính là Thương xá thành phố (Городской торговый корпус) xây năm 1910 theo thiết kế của kiến trúc sư Andrey Kryachkov, một công trình gạch đỏ trang nhã bên Quảng trường Lenin và được xếp hạng di tích kiến trúc cấp liên bang. Các gian trưng bày dẫn dắt du khách qua thiên nhiên Siberia, khảo cổ, dân tộc học của những tộc người bản địa và lịch sử phát triển của thành phố từ khi cây cầu đường sắt vượt sông Ob mở ra một đô thị mới. Hiện vật quý nhất là bộ xương voi ma mút gần như nguyên vẹn, cùng những bộ sưu tập trang phục, đồ dùng và cổ vật shaman giáo. Chi nhánh trưng bày lịch sử thiên nhiên và các chương trình tương tác khiến bảo tàng trở thành điểm khởi đầu lý tưởng để hiểu về vùng đất trẻ nhưng năng động này. Vị trí ngay trung tâm giúp du khách dễ kết hợp tham quan với Quảng trường Lenin và Nhà hát NOVAT gần đó.",
    [
        "Đặt trong Thương xá thành phố năm 1910 – di tích kiến trúc cấp liên bang bên Quảng trường Lenin.",
        "Bộ xương voi ma mút gần như hoàn chỉnh, biểu tượng của bảo tàng.",
        "Hành trình toàn cảnh về thiên nhiên, khảo cổ và lịch sử thành phố Novosibirsk.",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai (nên kiểm tra lịch trước).",
      "Vé vào cửa ở mức phải chăng (vài trăm rúp); có ưu đãi cho học sinh, sinh viên và người cao tuổi.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; rất hợp cho những ngày Siberia lạnh giá hoặc mưa tuyết.",
      "Nằm sát Quảng trường Lenin, dễ đi bộ kết hợp NOVAT và đại lộ Krasny Prospekt. Chú thích chủ yếu bằng tiếng Nga."),
    [
        {"title": "Wikipedia (RU) — Новосибирский государственный краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Новосибирский_государственный_краеведческий_музей"},
        {"title": "2GIS — Краеведческий музей, Красный проспект 23", "url": "https://2gis.ru/novosibirsk/firm/141265769354357"},
    ],
    ["museum", "history", "local-lore", "novosibirsk", "siberia", "mammoth"],
    maps_org("https://yandex.com/maps/org/novosibirskiy_gosudarstvenny_krayevedcheskiy_muzey/1131817495/", "Novosibirsk Regional Museum", "Novosibirsk"),
    official_site="https://youmuseum.ru",
))

# 2) Bảo tàng Mỹ thuật Quốc gia Novosibirsk (художественный)
RECORDS.append(rec(
    "novosibirsk-art-museum",
    "Bảo tàng Mỹ thuật Quốc gia Novosibirsk",
    "Новосибирский государственный художественный музей",
    "Novosibirsk State Art Museum",
    ["museum"],
    55.021835, 82.921243,
    "Đại lộ Krasny Prospekt 5, trung tâm thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Bảo tàng mỹ thuật hàng đầu của Siberia, nổi tiếng với bộ sưu tập tranh của danh họa Nicholas Roerich và hội họa Nga thế kỷ 18–20. Bảo tàng tọa lạc trong tòa nhà tân cổ điển bề thế của kiến trúc sư Kryachkov trên đại lộ chính.",
    "Bảo tàng Mỹ thuật Quốc gia Novosibirsk, thành lập năm 1958, là một trong những bộ sưu tập nghệ thuật giá trị nhất phía đông dãy Ural. Trụ sở là tòa nhà hành chính cũ do kiến trúc sư Andrey Kryachkov thiết kế theo phong cách tân cổ điển, nay là di tích trên đại lộ Krasny Prospekt. Bộ sưu tập trải rộng từ hội họa Nga cổ điển, tranh thánh (icon), nghệ thuật Xô Viết đến mỹ thuật đương đại, nhưng viên ngọc thực sự là loạt tranh của Nicholas Roerich với những dãy núi Himalaya rực rỡ sắc lam và huyền ảo. Bảo tàng còn lưu giữ đồ họa, điêu khắc và nghệ thuật trang trí ứng dụng, thường xuyên tổ chức triển lãm luân phiên và các chương trình giáo dục nghệ thuật. Đây là điểm đến không thể bỏ qua cho người yêu hội họa muốn khám phá chiều sâu văn hóa của thủ phủ Siberia. Vị trí trung tâm giúp dễ dàng kết hợp tham quan cùng các điểm khác trên Krasny Prospekt.",
    [
        "Bộ sưu tập tranh Nicholas Roerich thuộc hàng phong phú nhất nước Nga.",
        "Hội họa Nga thế kỷ 18–20, tranh thánh và nghệ thuật Xô Viết.",
        "Tòa nhà tân cổ điển của kiến trúc sư Kryachkov trên đại lộ Krasny Prospekt.",
    ],
    p("Thứ Ba–Chủ nhật, khoảng 10:00–18:00 (cuối tuần có thể mở tới 20:00); nghỉ Thứ Hai.",
      "Vé vào cửa vừa phải (vài trăm rúp); ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm; lý tưởng cho ngày thời tiết xấu.",
      "Nên xem trước lịch triển lãm tạm thời. Có thể kết hợp đi bộ dọc Krasny Prospekt tới Quảng trường Lenin."),
    [
        {"title": "Wikipedia (RU) — Новосибирский государственный художественный музей", "url": "https://ru.wikipedia.org/wiki/Новосибирский_государственный_художественный_музей"},
        {"title": "Trang chính thức — nsartmuseum.ru", "url": "https://www.nsartmuseum.ru/"},
    ],
    ["museum", "art", "roerich", "painting", "novosibirsk", "siberia"],
    maps_org("https://yandex.com/maps/org/novosibirskiy_gosudarstvenny_khudozhestvenny_muzey/1103959817/", "Novosibirsk State Art Museum", "Novosibirsk"),
    official_site="https://www.nsartmuseum.ru",
))

# 3) Bảo tàng Mặt Trời
RECORDS.append(rec(
    "museum-of-the-sun-novosibirsk",
    "Bảo tàng Mặt Trời",
    "Культурно-исторический музей Солнца",
    "Museum of the Sun",
    ["museum"],
    55.061651, 82.917003,
    "Phố Dusi Kovalchuk 179/3, quận Zayeltsovsky, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Bảo tàng độc nhất vô nhị trên thế giới dành trọn cho hình tượng Mặt Trời trong tín ngưỡng các dân tộc. Hàng nghìn phù điêu, tượng thần Mặt Trời được nghệ nhân chạm khắc thủ công, tái hiện từ Ai Cập, Ấn Độ đến người Slav cổ.",
    "Bảo tàng Mặt Trời khởi nguồn năm 1992 từ một câu lạc bộ chạm khắc gỗ ở Akademgorodok, do nghệ nhân Valery Lipenkov gây dựng, và nay đặt tại phố Dusi Kovalchuk trong thành phố. Đây được xem là bảo tàng duy nhất trên thế giới lấy Mặt Trời làm chủ đề xuyên suốt: bộ sưu tập gồm hàng nghìn bản sao thần Mặt Trời và biểu tượng thái dương của các nền văn minh cổ – từ Ai Cập, Lưỡng Hà, Ấn Độ, người da đỏ châu Mỹ đến người Kelt, Hy Lạp, La Mã và Slav cổ. Phần lớn hiện vật là phù điêu gỗ được chạm khắc, sơn màu thủ công công phu, tạo nên một không gian ấm áp và giàu tính giáo dục. Bảo tàng còn tổ chức các lễ hội Mặt Trời vào ngày hạ chí, đông chí và xuân phân, cùng các buổi hòa nhạc nhạc cụ dân tộc và lớp học sáng tạo. Không gian nhỏ nhưng đầy màu sắc này là điểm đến thú vị, khác lạ cho cả gia đình.",
    [
        "Bảo tàng duy nhất trên thế giới dành riêng cho hình tượng Mặt Trời.",
        "Hàng nghìn phù điêu thần Mặt Trời chạm khắc thủ công từ nhiều nền văn minh.",
        "Lễ hội Mặt Trời vào hạ chí, đông chí và xuân phân.",
    ],
    p("Hằng ngày theo lịch, thường khoảng 10:00–18:00; nên gọi hoặc đặt trước, có tour theo nhóm.",
      "Vé vào cửa khiêm tốn; các buổi diễn nhạc cụ và lớp học có phụ phí.",
      "Khoảng 1 giờ.",
      "Quanh năm; đặc biệt vào các dịp lễ Mặt Trời theo mùa.",
      "Nên đặt lịch trước để có hướng dẫn viên; phù hợp mang theo trẻ nhỏ."),
    [
        {"title": "Culture.ru — Музей Солнца", "url": "https://www.culture.ru/institutes/7986/muzei-solnca"},
        {"title": "Trang chính thức — museumofsun.ru", "url": "https://museumofsun.ru/"},
    ],
    ["museum", "sun", "culture", "folk-art", "novosibirsk", "unusual"],
    maps_text("Культурно-исторический музей Солнца", "Новосибирск", "Museum of the Sun", "Novosibirsk", 55.061651, 82.917003),
    official_site="https://museumofsun.ru",
))

# 4) Bảo tàng Nicholas Roerich
RECORDS.append(rec(
    "roerich-museum-novosibirsk",
    "Bảo tàng Nicholas Roerich (Nhà Roerich Siberia)",
    "Музей Н. К. Рериха",
    "Museum of Nicholas Roerich",
    ["museum"],
    55.022805, 82.920103,
    "Phố Kommunisticheskaya 38, quận Trung tâm, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Bảo tàng đầu tiên ở Siberia tôn vinh cuộc đời và di sản của họa sĩ – nhà tư tưởng Nicholas Roerich cùng gia đình ông. Tòa nhà được xây dựng bằng tiền quyên góp của cộng đồng, mang không gian tĩnh tại, giàu tinh thần.",
    "Bảo tàng Nicholas Roerich ở Novosibirsk là bảo tàng đầu tiên tại Siberia dành cho danh họa, nhà khảo cổ và triết gia Nicholas Roerich cùng cả gia đình ông. Công trình được xây dựng trong các năm 1997–2007 hoàn toàn bằng tiền quyên góp của Hội Roerich Siberia, nằm trong khu phố yên tĩnh giữa các phố Kommunisticheskaya, Sovetskaya, Sverdlova và đại lộ Krasny Prospekt. Bên trong trưng bày các bản sao và tư liệu về hành trình Trung Á lừng danh của Roerich, những bức tranh gợi cảm hứng tâm linh, cùng tài liệu về học thuyết Đạo đức Sống (Agni Yoga) mà gia đình ông truyền bá. Không gian bảo tàng gắn với các buổi hòa nhạc, chiếu phim, triển lãm và giảng đường văn hóa, thu hút những ai quan tâm đến nghệ thuật, phương Đông và tư tưởng nhân văn. Đây là điểm dừng tĩnh lặng và sâu lắng giữa nhịp sống đô thị Novosibirsk.",
    [
        "Bảo tàng Roerich đầu tiên của Siberia, xây bằng tiền quyên góp cộng đồng.",
        "Tư liệu về cuộc thám hiểm Trung Á và di sản nghệ thuật – tư tưởng của gia đình Roerich.",
        "Trung tâm văn hóa với hòa nhạc, triển lãm và giảng đường thường xuyên.",
    ],
    p("Thường 11:00–18:00 (mùa hè tới 19:00), Thứ Năm 13:00–20:00; nghỉ Thứ Ba.",
      "Vé vào cửa khiêm tốn; một số sự kiện có phụ phí.",
      "Khoảng 1 giờ.",
      "Quanh năm.",
      "Nên xem lịch sự kiện văn hóa trên trang của Hội Roerich; không gian yên tĩnh, phù hợp tham quan chậm rãi."),
    [
        {"title": "Trang chính thức Hội Roerich Novosibirsk — nsk.sibro.ru", "url": "https://nsk.sibro.ru/"},
        {"title": "2GIS — Музей Н.К. Рериха, Коммунистическая 38", "url": "https://2gis.ru/novosibirsk/firm/141265769360827"},
    ],
    ["museum", "roerich", "art", "culture", "novosibirsk"],
    maps_text("Музей Н. К. Рериха", "Новосибирск", "Museum of Nicholas Roerich", "Novosibirsk", 55.022805, 82.920103),
    official_site="https://nsk.sibro.ru",
))

# 5) Đại Thiên văn quán Novosibirsk (Planetarium)
RECORDS.append(rec(
    "novosibirsk-planetarium",
    "Đại Thiên văn quán Novosibirsk (mang tên nữ phi hành gia A. Kikina)",
    "Большой Новосибирский планетарий",
    "Grand Novosibirsk Planetarium",
    ["museum"],
    54.980783, 83.034906,
    "Ключ-Камышенское плато 1/1, quận Oktyabrsky, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Thiên văn quán lớn và hiện đại bậc nhất vùng Siberia, tọa lạc trên cao nguyên có tầm nhìn đẹp. Nơi đây có mái vòm chiếu sao, hai tháp quan sát, con lắc Foucault và công viên khoa học ngoài trời.",
    "Đại Thiên văn quán Novosibirsk, khánh thành năm 2012 và mang tên nữ phi hành gia Anna Kikina (người Novosibirsk), là trung tâm thiên văn – vũ trụ dành cho thiếu niên lớn nhất phía đông nước Nga. Công trình nằm trên cao nguyên Klyuch-Kamyshenskoye, một trong những điểm cao của thành phố, gồm mái vòm chiếu hình đường kính 16 mét với hệ thống chiếu sao và phim toàn cảnh hiện đại. Bên ngoài là hai tháp quan sát gắn kính thiên văn để ngắm Mặt Trời ban ngày và bầu trời đêm, cùng công viên Foucault với con lắc và các mô hình khoa học tương tác ngoài trời. Thiên văn quán tổ chức các buổi chiếu, bài giảng, quan sát thiên văn và sự kiện dành cho mọi lứa tuổi, đặc biệt hấp dẫn với trẻ em và gia đình. Từ đây còn có thể phóng tầm mắt ngắm toàn cảnh thành phố, khiến chuyến đi thêm trọn vẹn.",
    [
        "Thiên văn quán lớn nhất Siberia, mang tên nữ phi hành gia A. Kikina.",
        "Mái vòm chiếu sao 16 m cùng hai tháp quan sát và kính thiên văn.",
        "Công viên Foucault ngoài trời với con lắc và mô hình khoa học tương tác.",
    ],
    p("Thường mở cửa theo lịch suất chiếu, khoảng 10:00–19:00; nên đặt vé trước.",
      "Vé theo suất chiếu và chương trình, ở mức phải chăng; quan sát thiên văn có thể tính riêng.",
      "Khoảng 1,5–2 giờ.",
      "Đêm quang mây để quan sát bầu trời; ban ngày để ngắm Mặt Trời qua kính lọc.",
      "Kiểm tra lịch suất chiếu và thời tiết trước khi đi; đường lên cao nguyên hơi xa trung tâm."),
    [
        {"title": "Trang chính thức — nebo-nsk.ru", "url": "https://nebo-nsk.ru/"},
        {"title": "2GIS — Большой Новосибирский планетарий", "url": "https://2gis.ru/novosibirsk/firm/141265770966497"},
    ],
    ["museum", "planetarium", "science", "astronomy", "novosibirsk", "family"],
    maps_text("Большой Новосибирский планетарий", "Новосибирск", "Grand Novosibirsk Planetarium", "Novosibirsk", 54.980783, 83.034906),
    official_site="https://nebo-nsk.ru",
))

# 6) Bảo tàng Văn hóa Tang lễ Thế giới
RECORDS.append(rec(
    "museum-world-funeral-culture",
    "Bảo tàng Văn hóa Tang lễ Thế giới",
    "Музей мировой погребальной культуры",
    "Museum of World Funeral Culture",
    ["museum"],
    55.076114, 83.064379,
    "Phố Voyentorgovskaya 4/15, làng Voskhod (rìa bắc Novosibirsk), tỉnh Novosibirsk, Nga",
    "Bảo tàng độc đáo và duy nhất ở Nga về nghi lễ tang ma của các nền văn hóa, nằm trong tổ hợp Công viên Ký ức. Trưng bày trang phục tang, xe tang cổ, đồ trang sức tưởng niệm và tranh khắc, kể câu chuyện nhân văn về cái chết và sự sống.",
    "Bảo tàng Văn hóa Tang lễ Thế giới, mở cửa năm 2012, là bảo tàng đầu tiên và duy nhất thuộc loại này ở Nga, nằm trong tổ hợp Công viên Ký ức ở rìa bắc Novosibirsk. Dù chủ đề nghe có vẻ u ám, bảo tàng lại tiếp cận cái chết một cách tinh tế và nhân văn, giúp người xem suy ngẫm về sự sống và ký ức. Bộ sưu tập phong phú gồm trang phục tang thế kỷ 19, xe tang và kiệu tang cổ, đồ trang sức tưởng niệm làm từ tóc, tranh khắc, ảnh và tài liệu về phong tục tang ma khắp thế giới – từ châu Âu Victoria đến các nền văn hóa khác. Không gian trưng bày được dàn dựng công phu, kèm khu vườn, nhà nguyện và các hiện vật ngoài trời. Đây là một trong những bảo tàng gây ấn tượng và được đánh giá cao bậc nhất Novosibirsk, thu hút du khách tò mò muốn có trải nghiệm khác lạ.",
    [
        "Bảo tàng đầu tiên và duy nhất ở Nga về văn hóa tang lễ thế giới.",
        "Trang phục tang, xe tang cổ và đồ trang sức tưởng niệm thế kỷ 19.",
        "Cách tiếp cận nhân văn, tinh tế về đề tài cái chết và ký ức.",
    ],
    p("Thứ Ba–Chủ nhật, thường khoảng 11:00–19:00; nghỉ Thứ Hai (nên kiểm tra trước).",
      "Vé vào cửa trung bình; có tour hướng dẫn và ưu đãi cho nhóm.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm.",
      "Cách trung tâm khá xa về phía bắc; nên đi taxi/xe riêng. Chủ đề nhạy cảm, cân nhắc khi đi cùng trẻ nhỏ."),
    [
        {"title": "Trang chính thức — musei-smerti.ru", "url": "https://musei-smerti.ru/"},
        {"title": "2GIS — Музей Мировой Погребальной Культуры", "url": "https://2gis.ru/novosibirsk/firm/141266769902896"},
    ],
    ["museum", "history", "culture", "unusual", "novosibirsk"],
    maps_org("https://yandex.com/maps/org/muzey_mirovoy_pogrebalnoy_kultury/1034141834/", "Museum of World Funeral Culture", "Novosibirsk"),
    official_site="https://musei-smerti.ru",
))

# 7) Sузун-Завод. Xưởng đúc tiền (Suzun Mint)
RECORDS.append(rec(
    "suzun-mint-museum",
    "Tổ hợp bảo tàng Xưởng đúc tiền Suzun",
    "Музейно-туристический комплекс «Сузун-Завод. Монетный двор»",
    "Suzun Plant and Mint Museum Complex",
    ["museum"],
    53.786, 82.314071,
    "Phố Lenina 22в, thị trấn Suzun, huyện Suzunsky, tỉnh Novosibirsk, Nga (cách Novosibirsk ~180 km)",
    "Bảo tàng độc đáo ở thị trấn Suzun, nơi từng có xưởng đúc đồng tiền 'Siberia' riêng của đế quốc Nga thế kỷ 18. Các máy đúc tiền được phục dựng theo bản vẽ cổ, tái hiện toàn bộ quy trình làm ra đồng xu.",
    "Tổ hợp bảo tàng Xưởng đúc tiền Suzun là một chi nhánh của Bảo tàng Địa phương học Novosibirsk, nằm ở thị trấn cổ Suzun cách thành phố khoảng 180 km. Tại đây, từ năm 1764 đã có Nhà máy luyện đồng Nizhne-Suzunsky và xưởng đúc tiền, nơi trong các năm 1766–1781 đúc loại 'tiền Siberia' đặc biệt lưu hành riêng cho vùng Siberia. Bảo tàng phục dựng theo bản vẽ thế kỷ 18 các cỗ máy đúc tiền cỡ lớn có thể vận hành, giúp du khách hình dung toàn bộ quá trình chế tác từ nấu quặng đến dập xu. Ngoài khu 'Xưởng đúc tiền', tổ hợp còn có nhà xưởng, nhà quản đốc và các gian trưng bày về đời sống thợ mỏ, thợ đúc. Đây là điểm đến giàu giá trị lịch sử – công nghiệp, hé lộ một trang ít người biết về kinh tế tiền tệ của nước Nga ở Siberia. Chuyến đi phù hợp cho những ai yêu lịch sử và muốn khám phá vùng quê Novosibirsk.",
    [
        "Nơi duy nhất ở Siberia từng đúc loại 'tiền Siberia' riêng của đế quốc Nga (1766–1781).",
        "Máy đúc tiền phục dựng theo bản vẽ thế kỷ 18, có thể vận hành minh họa.",
        "Tổ hợp bảo tàng gắn với lịch sử nhà máy luyện đồng Nizhne-Suzunsky.",
    ],
    p("Thường Thứ Ba–Chủ nhật, khoảng 10:00–17:00; nên đặt lịch/tour trước (nghỉ Thứ Hai).",
      "Vé vào cửa phải chăng; các gói tham quan có hướng dẫn viên tính riêng.",
      "Khoảng 1,5–2 giờ (chưa tính di chuyển).",
      "Mùa hè và thu để thuận tiện di chuyển đường dài.",
      "Cách Novosibirsk ~180 km – nên đi xe riêng hoặc tour trong ngày; đặt trước để có thuyết minh."),
    [
        {"title": "Cổng du lịch Tỉnh Novosibirsk — Сузун-завод. Монетный двор", "url": "https://turizm.nso.ru/ru/content/muzeyno-turisticheskiy-kompleks-zavod-suzun-monetnyy-dvor"},
        {"title": "Culture.ru — Сузун-Завод. Монетный двор", "url": "https://www.culture.ru/institutes/22223/muzeino-turisticheskii-kompleks-suzun-zavod-monetnyi-dvor"},
    ],
    ["museum", "history", "mint", "coins", "industry", "suzun"],
    maps_text("Сузун-Завод. Монетный двор", "Сузун", "Suzun Plant and Mint", "Suzun", 53.786, 82.314071),
    official_site="https://youmuseum.ru",
))

# ============================ NHÀ HÁT / BIỂU DIỄN (theatre) ============================

# 8) Nhà hát Thanh thiếu niên Globus
RECORDS.append(rec(
    "globus-theatre-novosibirsk",
    "Nhà hát Thanh thiếu niên Hàn lâm «Globus»",
    "Новосибирский академический молодёжный театр «Глобус»",
    "Globus Academic Youth Theatre",
    ["theatre"],
    55.025576, 82.929562,
    "Phố Kamenskaya 1, trung tâm thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Một trong những nhà hát lâu đời và được yêu thích nhất Novosibirsk, nổi bật với tòa nhà hình con thuyền buồm căng gió. «Globus» dàn dựng đa dạng kịch mục cho cả thiếu nhi và người lớn.",
    "Nhà hát «Globus» ra đời năm 1930 với tên gọi ban đầu là Nhà hát Khán giả nhỏ tuổi, và là một trong những đoàn kịch giàu truyền thống nhất Novosibirsk. Tòa nhà hiện nay hoàn thành năm 1984, gây ấn tượng mạnh với hình khối cách điệu như một con thuyền buồm căng gió – biểu tượng kiến trúc quen thuộc của thành phố. Được phong danh hiệu 'hàn lâm', nhà hát có kịch mục phong phú từ cổ tích thiếu nhi, nhạc kịch đến những vở chính kịch kinh điển và hiện đại cho người lớn, cùng dàn diễn viên và đạo diễn nhiều thế hệ. Không gian nội thất hiện đại, hai khán phòng lớn nhỏ và sảnh rộng phù hợp cho nhiều loại hình biểu diễn. Với người dân địa phương, đây là địa chỉ văn hóa gần gũi, nơi nhiều thế hệ trẻ em Novosibirsk lần đầu làm quen với sân khấu. Vị trí trung tâm gần công viên Trung tâm khiến nhà hát dễ tiếp cận.",
    [
        "Tòa nhà cách điệu hình con thuyền buồm – biểu tượng kiến trúc của thành phố.",
        "Một trong những nhà hát lâu đời nhất Novosibirsk (từ năm 1930).",
        "Kịch mục đa dạng cho cả thiếu nhi và người lớn.",
    ],
    p("Biểu diễn chủ yếu buổi tối và cuối tuần theo lịch mùa diễn; phòng vé mở cửa hằng ngày.",
      "Giá vé thay đổi theo vở và hạng ghế, từ vài trăm đến hơn nghìn rúp; đặt trên trang chính thức globus-nsk.ru.",
      "Một buổi diễn thường 2–3 giờ (kể cả giải lao).",
      "Mùa diễn chính từ thu đến xuân.",
      "Đặt vé trước cho các vở nổi tiếng; đến sớm để gửi áo khoác và ngắm kiến trúc con thuyền."),
    [
        {"title": "Wikipedia (RU) — Глобус (театр, Новосибирск)", "url": "https://ru.wikipedia.org/wiki/Глобус_(театр,_Новосибирск)"},
        {"title": "Trang chính thức — globus-nsk.ru", "url": "https://www.globus-nsk.ru/"},
    ],
    ["theatre", "youth-theatre", "architecture", "culture", "novosibirsk"],
    maps_text("Молодёжный театр Глобус", "Новосибирск", "Globus Youth Theatre", "Novosibirsk", 55.025576, 82.929562),
    official_site="https://www.globus-nsk.ru",
))

# 9) Nhà hát kịch Krasny Fakel
RECORDS.append(rec(
    "krasny-fakel-theatre",
    "Nhà hát Kịch Hàn lâm «Krasny Fakel» (Ngọn đuốc đỏ)",
    "Новосибирский государственный академический драматический театр «Красный факел»",
    "Krasny Fakel Academic Drama Theatre",
    ["theatre"],
    55.028347, 82.908263,
    "Phố Lenina 19, trung tâm thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Nhà hát kịch danh giá bậc nhất Siberia, thường được gọi là 'Nhà hát Nghệ thuật Siberia'. Trụ sở là tòa nhà cổ điển đầu thế kỷ 20, sân khấu của nhiều vở diễn đoạt giải quốc gia.",
    "Nhà hát «Krasny Fakel» (Ngọn đuốc đỏ) thành lập năm 1920 tại Odessa bởi một nhóm nghệ sĩ trẻ, sau nhiều năm lưu diễn đã định cư tại Novosibirsk từ năm 1932. Với chất lượng dàn dựng cao và phong cách tinh tế, nhà hát được mệnh danh là 'Nhà hát Nghệ thuật Siberia', sánh với những sân khấu kịch hàng đầu nước Nga. Trụ sở là một tòa nhà cổ điển xây đầu thế kỷ 20 (nguyên là Câu lạc bộ Thương nhân), nằm trên phố Lenina yên tĩnh gần trung tâm. Kịch mục trải rộng từ các tác phẩm kinh điển Nga và thế giới đến những vở đương đại táo bạo, nhiều lần được vinh danh tại Giải Mặt nạ Vàng danh giá. Không khí trang trọng, dàn diễn viên tài năng và những buổi diễn giàu cảm xúc khiến đây là điểm đến không thể bỏ qua với người yêu sân khấu. Nhà hát nằm gần Quảng trường Lenin, thuận tiện kết hợp tham quan trung tâm.",
    [
        "Được mệnh danh 'Nhà hát Nghệ thuật Siberia', nhiều lần đoạt Giải Mặt nạ Vàng.",
        "Trụ sở là tòa nhà cổ điển đầu thế kỷ 20 gần trung tâm.",
        "Kịch mục từ kinh điển Nga – thế giới đến các vở đương đại.",
    ],
    p("Biểu diễn buổi tối, cuối tuần có suất ban ngày; phòng vé 10:00–20:00 theo lịch.",
      "Giá vé theo vở và hạng ghế, từ vài trăm đến vài nghìn rúp; mua trên red-torch.ru.",
      "Một buổi diễn thường 2–3 giờ.",
      "Mùa diễn chính từ thu đến xuân.",
      "Đặt vé sớm cho các vở nổi tiếng; ăn mặc lịch sự theo truyền thống xem kịch Nga."),
    [
        {"title": "Wikipedia (RU) — Красный факел", "url": "https://ru.wikipedia.org/wiki/Красный_факел"},
        {"title": "Trang chính thức — red-torch.ru", "url": "https://red-torch.ru/"},
    ],
    ["theatre", "drama", "culture", "novosibirsk", "siberia"],
    maps_org("https://yandex.ru/maps/org/1251250354", "Krasny Fakel Drama Theatre", "Novosibirsk"),
    official_site="https://red-torch.ru",
))

# 10) Rạp xiếc Novosibirsk
RECORDS.append(rec(
    "novosibirsk-circus",
    "Rạp xiếc Quốc gia Novosibirsk",
    "Новосибирский государственный цирк",
    "Novosibirsk State Circus",
    ["theatre"],
    55.041804, 82.909907,
    "Phố Chelyuskintsev 21, quận Zheleznodorozhny, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Rạp xiếc cố định lớn của Siberia với mái vòm tròn đặc trưng, nơi trình diễn những chương trình xiếc đẳng cấp cho khán giả mọi lứa tuổi. Điểm giải trí gia đình được yêu thích của thành phố.",
    "Rạp xiếc Quốc gia Novosibirsk khánh thành năm 1971, là một trong những rạp xiếc cố định lớn và hiện đại của vùng Siberia. Tòa nhà mang mái vòm tròn đặc trưng của kiến trúc rạp xiếc Xô Viết, với khán phòng khoảng hai nghìn chỗ bao quanh sàn diễn tròn kinh điển. Nơi đây thường xuyên đón các đoàn xiếc lưu diễn của Nga và quốc tế, mang đến những màn nhào lộn, thăng bằng, ảo thuật và tiết mục thú biểu diễn đầy màu sắc. Rạp xiếc là điểm giải trí gia đình được nhiều thế hệ người Novosibirsk yêu thích, đặc biệt hấp dẫn với trẻ em. Vị trí gần trung tâm và nhà ga giúp việc di chuyển thuận tiện. Trước và sau buổi diễn, du khách có thể dạo bộ khu phố lân cận hoặc ghé các điểm tham quan gần đó.",
    [
        "Rạp xiếc cố định lớn của Siberia với mái vòm tròn đặc trưng.",
        "Khán phòng khoảng hai nghìn chỗ quanh sàn diễn tròn kinh điển.",
        "Chương trình xiếc đa dạng, điểm giải trí gia đình được yêu thích.",
    ],
    p("Biểu diễn chủ yếu cuối tuần và ngày lễ theo lịch chương trình; phòng vé mở hằng ngày.",
      "Giá vé theo chương trình và hạng ghế, ở mức vừa phải; đặt trên circus-novosibirsk.ru.",
      "Một suất diễn thường khoảng 2 giờ.",
      "Quanh năm, theo lịch các đoàn lưu diễn.",
      "Đặt vé trước cho các chương trình đông khách; rất hợp đi cùng trẻ nhỏ."),
    [
        {"title": "Wikipedia (RU) — Новосибирский цирк", "url": "https://ru.wikipedia.org/wiki/Новосибирский_цирк"},
        {"title": "Trang chính thức — circus-novosibirsk.ru", "url": "https://www.circus-novosibirsk.ru/"},
    ],
    ["theatre", "circus", "entertainment", "family", "novosibirsk"],
    maps_org("https://yandex.com/maps/org/novosibirskiy_gosudarstvenny_tsirk/1099211147/", "Novosibirsk State Circus", "Novosibirsk"),
    official_site="https://www.circus-novosibirsk.ru",
))

# ============================ NHÀ THỜ (church) ============================

# 11) Nhà thờ chính tòa Voznesensky (Thăng Thiên)
RECORDS.append(rec(
    "ascension-cathedral-novosibirsk",
    "Nhà thờ Chính tòa Thăng Thiên (Voznesensky)",
    "Вознесенский кафедральный собор",
    "Ascension Cathedral",
    ["church"],
    55.042392, 82.912383,
    "Phố Sovetskaya 91, quận Zheleznodorozhny, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Nhà thờ chính tòa của Giáo phận Novosibirsk, khởi nguồn từ một ngôi nhà thờ gỗ năm 1913 rồi được mở rộng thành thánh đường lớn với những mái vòm dát vàng. Trung tâm đời sống Chính thống giáo của thành phố.",
    "Nhà thờ Chính tòa Thăng Thiên là ngôi thánh đường chính của Giáo phận Novosibirsk. Khởi đầu chỉ là một nhà thờ gỗ nhỏ dựng năm 1913, công trình đã trải qua nhiều lần mở rộng và tái thiết lớn, đặc biệt trong thập niên 1970 và 1980, để trở thành một thánh đường bề thế với nhiều mái vòm hành củ dát vàng lấp lánh. Bên trong, nhà thờ gây ấn tượng với các bức bích họa, tường icon (iconostasis) mạ vàng và không gian trang nghiêm, lưu giữ nhiều thánh tích được tín đồ tôn kính. Đây là nơi cử hành các nghi lễ trọng thể của Chính thống giáo trong vùng và là trung tâm hành hương của người dân Novosibirsk. Với du khách, nhà thờ là điểm đến để chiêm ngưỡng kiến trúc tôn giáo Nga rực rỡ và cảm nhận nhịp sống tâm linh của thành phố. Nhà thờ nằm gần rạp xiếc và khu trung tâm, dễ kết hợp tham quan.",
    [
        "Nhà thờ chính tòa của Giáo phận Novosibirsk với nhiều mái vòm dát vàng.",
        "Khởi nguồn từ nhà thờ gỗ năm 1913, được mở rộng thành thánh đường lớn.",
        "Tường icon mạ vàng và các thánh tích được tôn kính bên trong.",
    ],
    p("Mở cửa hằng ngày, thường từ khoảng 8:00 đến tối theo lịch lễ.",
      "Miễn phí vào viếng; hoan nghênh quyên góp tùy tâm.",
      "Khoảng 30–45 phút.",
      "Quanh năm; đặc biệt vào các dịp lễ lớn của Chính thống giáo.",
      "Ăn mặc kín đáo; phụ nữ nên trùm khăn khi vào bên trong. Giữ yên lặng trong giờ lễ."),
    [
        {"title": "Sobory.ru — Вознесенский кафедральный собор, Новосибирск", "url": "https://sobory.ru/article/?object=04429"},
        {"title": "2GIS — Вознесенский кафедральный собор", "url": "https://2gis.ru/novosibirsk/firm/141265769360825"},
    ],
    ["church", "cathedral", "orthodox", "religion", "novosibirsk"],
    maps_org("https://yandex.com/maps/org/voznesenskiy_kafedralny_sobor/1038694534/", "Ascension Cathedral", "Novosibirsk"),
))

# 12) Nhà thờ Chính tòa Troitse-Vladimirsky
RECORDS.append(rec(
    "holy-trinity-vladimir-cathedral",
    "Nhà thờ Chính tòa Ba Ngôi – Thánh Vladimir",
    "Троице-Владимирский собор",
    "Holy Trinity–Vladimir Cathedral",
    ["church"],
    54.984669, 82.829157,
    "Phố Filatova 14а, khu Zapadny, quận Leninsky, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Một trong những nhà thờ mới lớn nhất Novosibirsk, nổi bật với kiến trúc trắng – vàng bề thế theo phong cách Nga cổ. Điểm nhấn tôn giáo của khu vực tả ngạn sông Ob.",
    "Nhà thờ Chính tòa Ba Ngôi – Thánh Vladimir là một trong những công trình tôn giáo lớn và nổi bật nhất được xây dựng ở Novosibirsk trong thời hiện đại, khánh thành vào năm 2013 tại khu Zapadny thuộc quận Leninsky bên tả ngạn sông Ob. Thánh đường được dựng theo phong cách kiến trúc nhà thờ Nga truyền thống, với thân màu trắng thanh khiết, những mái vòm hành củ dát vàng và tháp chuông cao vươn lên bầu trời Siberia. Bên trong là không gian rộng rãi, sáng sủa với tường icon và bích họa được thực hiện công phu. Nhà thờ nhanh chóng trở thành trung tâm sinh hoạt tinh thần và biểu tượng của cả khu vực, đón đông đảo tín đồ vào các dịp lễ. Với du khách, đây là dịp ngắm nhìn kiến trúc Chính thống giáo đương đại được xây dựng theo chuẩn mực cổ điển. Vị trí bên tả ngạn cho phép kết hợp tham quan với các điểm khác của quận Leninsky.",
    [
        "Một trong những nhà thờ mới lớn nhất Novosibirsk (khánh thành 2013).",
        "Kiến trúc trắng – vàng theo phong cách Nga cổ với mái vòm hành củ dát vàng.",
        "Trung tâm tâm linh và biểu tượng của khu tả ngạn sông Ob.",
    ],
    p("Mở cửa hằng ngày, thường 8:00–20:00 theo lịch lễ.",
      "Miễn phí vào viếng; hoan nghênh quyên góp tùy tâm.",
      "Khoảng 30–45 phút.",
      "Quanh năm; đông vào các dịp lễ lớn.",
      "Ăn mặc kín đáo; phụ nữ nên trùm khăn. Nằm bên tả ngạn, hơi xa trung tâm phải ngạn."),
    [
        {"title": "Sobory.ru — Троице-Владимирский собор, Новосибирск", "url": "https://sobory.ru/article/?object=05382"},
        {"title": "2GIS — Троице-Владимирский собор, Филатова 14а", "url": "https://2gis.ru/novosibirsk/firm/141265769356398"},
    ],
    ["church", "cathedral", "orthodox", "religion", "novosibirsk"],
    maps_text("Троице-Владимирский собор", "Новосибирск", "Holy Trinity Vladimir Cathedral", "Novosibirsk", 54.984669, 82.829157),
))

# 13) Nhà nguyện Thánh Nikolai (Trung tâm nước Nga)
RECORDS.append(rec(
    "nikolsky-chapel-novosibirsk",
    "Nhà nguyện Thánh Nikolai Kỳ Diệu (biểu tượng 'trung tâm nước Nga')",
    "Часовня во имя Святого Николая Чудотворца",
    "Chapel of St. Nicholas the Wonderworker",
    ["church", "monument"],
    55.026463, 82.92147,
    "Đại lộ Krasny Prospekt 17а, trung tâm thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Nhà nguyện nhỏ xinh giữa đại lộ chính, được xem là biểu tượng của 'trung tâm địa lý nước Nga'. Công trình mang phong cách kiến trúc Pskov – Novgorod cổ kính, là điểm chụp ảnh và cầu nguyện quen thuộc.",
    "Nhà nguyện Thánh Nikolai Kỳ Diệu là một trong những biểu tượng đáng yêu nhất của Novosibirsk, nằm ngay giữa đại lộ Krasny Prospekt. Ngôi nhà nguyện đầu tiên được đặt viên đá năm 1914 nhân kỷ niệm 300 năm triều đại Romanov và gắn với truyền thuyết rằng nơi đây từng được coi là trung tâm địa lý của đế quốc Nga. Năm 1930, nhà nguyện bị phá bỏ, và mãi tới năm 1993 – nhân dịp 100 năm thành lập thành phố – mới được phục dựng gần vị trí cũ. Công trình gạch nhỏ nhắn hình khối vuông, một mái vòm, mang phong cách các nhà thờ Pskov – Novgorod thế kỷ 14–15, trắng sáng và duyên dáng. Trong tâm thức người dân, nhà nguyện đã trở thành biểu tượng của 'trung tâm nước Nga', là nơi cầu nguyện và cũng là điểm hẹn, chụp ảnh quen thuộc trên phố đi bộ. Du khách dễ dàng ghé thăm khi dạo bộ dọc đại lộ chính của thành phố.",
    [
        "Được xem là biểu tượng 'trung tâm địa lý nước Nga' ngay trên đại lộ chính.",
        "Kiến trúc gạch trắng phong cách Pskov – Novgorod thế kỷ 14–15.",
        "Phục dựng năm 1993 nhân 100 năm thành lập Novosibirsk.",
    ],
    p("Mở cửa hằng ngày theo lịch lễ (thường ban ngày tới chiều).",
      "Miễn phí vào viếng.",
      "Khoảng 10–20 phút.",
      "Quanh năm; đẹp nhất khi dạo bộ Krasny Prospekt.",
      "Nằm trên dải phân cách/vỉa hè đại lộ, dễ kết hợp tham quan trung tâm và Quảng trường Lenin gần đó."),
    [
        {"title": "Wikipedia (RU) — Часовня Николая Чудотворца (Новосибирск)", "url": "https://ru.wikipedia.org/wiki/Часовня_Николая_Чудотворца_(Новосибирск)"},
        {"title": "Sobory.ru — Часовня Николая Чудотворца на Красном проспекте", "url": "https://sobory.ru/article/?object=00494"},
    ],
    ["church", "chapel", "monument", "symbol", "novosibirsk", "landmark"],
    maps_text("Часовня Николая Чудотворца", "Новосибирск", "Chapel of St Nicholas", "Novosibirsk", 55.026463, 82.92147),
))

# ============================ QUẢNG TRƯỜNG / PHỐ (square_street) ============================

# 14) Quảng trường Lenin
RECORDS.append(rec(
    "lenin-square-novosibirsk",
    "Quảng trường Lenin",
    "Площадь Ленина",
    "Lenin Square",
    ["square_street"],
    55.029, 82.9206,
    "Trung tâm thành phố Novosibirsk, giữa đại lộ Krasny Prospekt, tỉnh Novosibirsk, Nga",
    "Trái tim của Novosibirsk, quảng trường trung tâm rộng lớn bao quanh bởi Nhà hát NOVAT, tượng đài Lenin và các công trình tiêu biểu. Nơi diễn ra lễ hội, sự kiện và là điểm hẹn quen thuộc của thành phố.",
    "Quảng trường Lenin là trung tâm hành chính, văn hóa và tinh thần của Novosibirsk, trải rộng dọc đại lộ Krasny Prospekt. Điểm nhấn nổi bật nhất là Nhà hát Opera và Ballet NOVAT với mái vòm bạc khổng lồ ở phía đông, đối diện là tổ hợp tượng đài Lenin dựng năm 1970 gồm tượng lãnh tụ và các nhóm tượng công nhân, chiến sĩ, thanh niên mang phong cách hiện thực Xô Viết. Quanh quảng trường còn có Thương xá thành phố (nay là Bảo tàng Địa phương học), nhà nguyện Thánh Nikolai và nhiều tòa nhà lịch sử. Đây là nơi tổ chức các lễ hội thành phố, hòa nhạc ngoài trời, chợ Giáng sinh và bắn pháo hoa; mùa đông thường dựng thành phố băng và cây thông lớn. Với du khách, quảng trường là điểm khởi đầu lý tưởng để khám phá trung tâm, chụp ảnh và cảm nhận nhịp sống của đô thị lớn nhất Siberia.",
    [
        "Quảng trường trung tâm lớn nhất Siberia, trước Nhà hát NOVAT.",
        "Tổ hợp tượng đài Lenin năm 1970 mang phong cách hiện thực Xô Viết.",
        "Nơi diễn ra lễ hội, hòa nhạc, chợ Giáng sinh và thành phố băng mùa đông.",
    ],
    p("Không gian công cộng mở cửa suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 30–45 phút dạo quanh.",
      "Mùa hè cho không khí lễ hội; mùa đông để ngắm thành phố băng và trang trí Giáng sinh.",
      "Điểm khởi đầu tham quan trung tâm; có ga tàu điện ngầm 'Площадь Ленина' ngay bên dưới."),
    [
        {"title": "Wikipedia (RU) — Площадь Ленина (Новосибирск)", "url": "https://ru.wikipedia.org/wiki/Площадь_Ленина_(Новосибирск)"},
        {"title": "Cổng thông tin thành phố — novo-sibirsk.ru", "url": "https://novo-sibirsk.ru/"},
    ],
    ["square_street", "square", "city-center", "monument", "novosibirsk"],
    maps_text("Площадь Ленина", "Новосибирск", "Lenin Square", "Novosibirsk", 55.029, 82.9206),
))

# 15) Đại lộ Krasny Prospekt
RECORDS.append(rec(
    "krasny-prospekt-novosibirsk",
    "Đại lộ Krasny Prospekt (Đại lộ Đỏ)",
    "Красный проспект",
    "Krasny Prospekt (Red Avenue)",
    ["square_street"],
    55.03, 82.9208,
    "Trục trung tâm thành phố Novosibirsk, chạy qua Quảng trường Lenin, tỉnh Novosibirsk, Nga",
    "Đại lộ chính và là 'xương sống' của Novosibirsk, dài khoảng 7 km với hai hàng cây và loạt công trình kiến trúc tiêu biểu. Trục đi bộ và dạo chơi trung tâm được người dân yêu thích.",
    "Krasny Prospekt (Đại lộ Đỏ) là trục đường trung tâm và biểu tượng của Novosibirsk, kéo dài khoảng 7 km từ nhà ga sông tới phía bắc thành phố – từng được xem là một trong những đại lộ thẳng dài nhất nước Nga. Nguyên là 'Nikolaevsky Prospekt' thời đầu thế kỷ 20, con phố tập trung phần lớn các công trình đẹp nhất của thành phố: Nhà hát NOVAT, Quảng trường Lenin, nhà nguyện Thánh Nikolai, ngôi nhà '100 căn hộ' (Stokvartirny) từng đoạt giải ở Paris, các bảo tàng, rạp chiếu bóng, nhà thờ và tòa nhà hành chính. Hai bên đại lộ rợp bóng cây, có vỉa hè rộng, quảng trường nhỏ và đài phun nước, là nơi người dân dạo bộ, hẹn hò và tổ chức sự kiện. Đi bộ dọc Krasny Prospekt là cách tuyệt vời để cảm nhận lịch sử phát triển và nhịp sống của thủ phủ Siberia. Đây cũng là tuyến kết nối nhiều điểm tham quan trung tâm.",
    [
        "Đại lộ chính dài khoảng 7 km – trục xương sống của Novosibirsk.",
        "Quy tụ NOVAT, Quảng trường Lenin, nhà '100 căn hộ' và nhiều di tích.",
        "Tuyến đi bộ rợp bóng cây được người dân yêu thích.",
    ],
    p("Không gian công cộng, đi lại tự do suốt ngày.",
      "Miễn phí.",
      "Tùy lộ trình đi bộ; đoạn trung tâm khoảng 1–2 giờ.",
      "Mùa hè và đầu thu để dạo bộ dễ chịu.",
      "Kết hợp đi bộ giữa Quảng trường Lenin, nhà nguyện Thánh Nikolai và các bảo tàng dọc đại lộ."),
    [
        {"title": "Wikipedia (RU) — Красный проспект", "url": "https://ru.wikipedia.org/wiki/Красный_проспект"},
        {"title": "2GIS — Красный проспект, Новосибирск", "url": "https://2gis.ru/novosibirsk/geo/141476222741301"},
    ],
    ["square_street", "avenue", "architecture", "walking", "novosibirsk"],
    maps_text("Красный проспект", "Новосибирск", "Krasny Prospekt", "Novosibirsk", 55.03, 82.9208),
))

# ============================ CẦU (bridge) ============================

# 16) Cầu Bugrinsky
RECORDS.append(rec(
    "bugrinsky-bridge",
    "Cầu Bugrinsky",
    "Бугринский мост",
    "Bugrinsky Bridge",
    ["bridge"],
    54.975185, 82.962646,
    "Bắc qua sông Ob, nối quận Kirovsky và Oktyabrsky, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Cây cầu vòm đỏ hiện đại vượt sông Ob, nổi tiếng với nhịp vòm giữa dài nhất khối SNG (380 m). Công trình khánh thành năm 2014, trở thành biểu tượng kỹ thuật mới của Novosibirsk.",
    "Cầu Bugrinsky là cây cầu thứ ba bắc qua sông Ob trong địa phận thành phố Novosibirsk, khánh thành tháng 10 năm 2014. Điểm độc đáo nhất của cầu là nhịp vòm mạng lưới (network arch) màu đỏ dài tới 380 mét – vào thời điểm hoàn thành được xem là nhịp vòm dài nhất trong không gian các nước SNG. Vòm thép đỏ cong mềm mại vươn lên trên mặt sông tạo nên hình ảnh ấn tượng, nhất là khi lên đèn vào buổi tối. Cầu nối quận Kirovsky ở tả ngạn với quận Oktyabrsky ở phải ngạn, giúp giảm tải giao thông cho các cây cầu cũ và mở rộng kết nối đô thị. Với kiến trúc táo bạo và quy mô lớn, Bugrinsky nhanh chóng trở thành một biểu tượng kỹ thuật – thẩm mỹ mới của thành phố. Du khách có thể ngắm cầu đẹp nhất từ bờ sông hoặc trên các chuyến du thuyền sông Ob.",
    [
        "Nhịp vòm mạng lưới màu đỏ dài 380 m – từng dài nhất khối SNG.",
        "Khánh thành năm 2014, biểu tượng kỹ thuật mới của Novosibirsk.",
        "Ngắm đẹp nhất từ bờ sông hoặc du thuyền, đặc biệt khi lên đèn buổi tối.",
    ],
    p("Công trình giao thông, có thể ngắm bất cứ lúc nào.",
      "Miễn phí (đi qua cầu).",
      "Khoảng 20–30 phút để ngắm và chụp ảnh.",
      "Chiều tối để ngắm vòm cầu lên đèn; mùa hè để đi du thuyền sông.",
      "Điểm ngắm đẹp từ bờ Kirovsky; kết hợp tản bộ ven sông Ob."),
    [
        {"title": "Wikipedia (RU) — Бугринский мост", "url": "https://ru.wikipedia.org/wiki/Бугринский_мост"},
        {"title": "Tourister.ru — Бугринский мост, Новосибирск", "url": "https://www.tourister.ru/world/europe/russia/city/novosibirsk/bridges/25991"},
    ],
    ["bridge", "architecture", "ob-river", "landmark", "novosibirsk"],
    maps_text("Бугринский мост", "Новосибирск", "Bugrinsky Bridge", "Novosibirsk", 54.975185, 82.962646),
))

# 17) Cầu đường sắt Komsomolsky
RECORDS.append(rec(
    "komsomolsky-railway-bridge",
    "Cầu đường sắt Komsomolsky",
    "Комсомольский железнодорожный мост",
    "Komsomolsky Railway Bridge",
    ["bridge"],
    54.961122, 82.984353,
    "Bắc qua sông Ob (tuyến đường sắt vòng), thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Cầu đường sắt lịch sử thứ hai vượt sông Ob của tuyến xuyên Siberia, xây dựng thần tốc năm 1930–1931. Khi hoàn thành từng là cầu đường sắt hai làn lớn nhất Liên Xô.",
    "Cầu đường sắt Komsomolsky là cây cầu đường sắt thứ hai vượt sông Ob tại Novosibirsk, xây dựng trong các năm 1930–1931 với tiến độ thần tốc theo thiết kế của Mostotrest. Đây là mắt xích quan trọng của tuyến xuyên Siberia, phục vụ tuyến đường sắt vòng tránh trung tâm thành phố (qua Inskaya – Sokur). Cầu có hai làn ray và dài khoảng một km, kết cấu dàn thép nhiều nhịp cùng các nhịp thông thuyền, và vào thời điểm hoàn thành từng được xem là cầu đường sắt hai làn lớn nhất Liên Xô. Cây cầu gắn liền với lịch sử công nghiệp hóa và vai trò của Novosibirsk như một đầu mối giao thông trọng yếu của Siberia. Dù là công trình phục vụ vận tải, cầu vẫn là điểm tham quan thú vị cho những ai yêu lịch sử đường sắt và muốn ngắm những đoàn tàu hàng dài chạy qua dòng Ob. Có thể quan sát cầu từ các điểm ven sông.",
    [
        "Cầu đường sắt thứ hai vượt sông Ob của tuyến xuyên Siberia (1930–1931).",
        "Xây dựng thần tốc, từng là cầu đường sắt hai làn lớn nhất Liên Xô.",
        "Gắn với lịch sử công nghiệp hóa và vai trò đầu mối giao thông của Novosibirsk.",
    ],
    p("Công trình đường sắt đang khai thác, chỉ ngắm từ bên ngoài.",
      "Miễn phí (quan sát từ xa).",
      "Khoảng 15–20 phút.",
      "Ban ngày để quan sát và chụp ảnh đoàn tàu qua cầu.",
      "Không xâm nhập khu vực đường sắt vì lý do an toàn; ngắm từ bờ sông."),
    [
        {"title": "Wikipedia (RU) — Комсомольский железнодорожный мост", "url": "https://ru.wikipedia.org/wiki/Комсомольский_железнодорожный_мост"},
        {"title": "2GIS — Комсомольский железнодорожный мост", "url": "https://2gis.ru/novosibirsk/geo/70030076192300827"},
    ],
    ["bridge", "railway", "history", "ob-river", "novosibirsk"],
    maps_text("Комсомольский железнодорожный мост", "Новосибирск", "Komsomolsky Railway Bridge", "Novosibirsk", 54.961122, 82.984353),
))

# 18) Cầu tàu điện ngầm (Metromost)
RECORDS.append(rec(
    "novosibirsk-metro-bridge",
    "Cầu Tàu điện ngầm Novosibirsk (Metromost)",
    "Новосибирский метромост",
    "Novosibirsk Metro Bridge",
    ["bridge"],
    54.99425, 82.9107,
    "Bắc qua sông Ob, nối ga Rechnoy Vokzal và Studencheskaya (tuyến Leninskaya), thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Cầu tàu điện ngầm có phần thân dài nhất thế giới, nối hai ga metro ở hai bờ sông Ob. Tổng chiều dài khoảng 2.145 m, là niềm tự hào kỹ thuật độc đáo của Novosibirsk.",
    "Cầu Tàu điện ngầm Novosibirsk (Metromost) là công trình có một không hai: cây cầu metro có mái che dài nhất thế giới. Cầu nối hai ga Rechnoy Vokzal (bờ phải) và Studencheskaya (bờ trái) của tuyến Leninskaya, đưa các đoàn tàu điện ngầm vượt sông Ob. Tổng chiều dài cầu cùng các cầu dẫn hai bên khoảng 2.145 mét, trong đó phần vượt lòng sông dài khoảng 896 mét. Cầu được đưa vào khai thác cùng ngày mở tuyến Leninskaya – 7 tháng 1 năm 1986 – và phần ống thép có mái che của cầu được thiết kế để chịu được biên độ nhiệt khắc nghiệt của Siberia, có thể co giãn tới cả mét theo mùa. Đây là niềm tự hào kỹ thuật của người dân thành phố và là một chi tiết thú vị của hệ thống metro Novosibirsk – hệ thống tàu điện ngầm duy nhất ở vùng Siberia. Hành khách đi metro qua đây có thể thoáng nhìn dòng sông Ob qua các ô cửa; từ bờ sông cũng có thể ngắm toàn cảnh cây cầu.",
    [
        "Cầu tàu điện ngầm có mái che dài nhất thế giới (khoảng 2.145 m).",
        "Vượt sông Ob, nối hai ga metro tuyến Leninskaya từ năm 1986.",
        "Ống thép có mái che co giãn theo biên độ nhiệt khắc nghiệt của Siberia.",
    ],
    p("Đi qua bằng tàu điện ngầm trong giờ hoạt động của metro (khoảng 5:45–24:00).",
      "Chỉ cần vé metro thông thường để trải nghiệm đi qua cầu.",
      "Vài phút khi đi tàu; ngắm từ bờ khoảng 20–30 phút.",
      "Ban ngày để nhìn rõ sông Ob khi tàu qua cầu.",
      "Muốn chụp toàn cảnh cầu, hãy ra khu bờ sông gần ga Rechnoy Vokzal."),
    [
        {"title": "Wikipedia (RU) — Новосибирский метромост", "url": "https://ru.wikipedia.org/wiki/Новосибирский_метромост"},
        {"title": "2GIS — Станция метро Студенческая (đầu cầu tả ngạn)", "url": "https://2gis.ru/novosibirsk/station/141523467371739"},
    ],
    ["bridge", "metro", "ob-river", "record", "novosibirsk"],
    maps_text("Новосибирский метромост", "Новосибирск", "Novosibirsk Metro Bridge", "Novosibirsk", 54.99425, 82.9107),
))

# ============================ CÔNG TRÌNH / DI TÍCH (monument) ============================

# 19) Ga Novosibirsk-Glavny
RECORDS.append(rec(
    "novosibirsk-glavny-station",
    "Ga Novosibirsk-Glavny",
    "Вокзал Новосибирск-Главный",
    "Novosibirsk-Glavny Railway Station",
    ["monument"],
    55.035706, 82.896166,
    "Phố Dmitriya Shamshurina 43, quận Zheleznodorozhny, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Nhà ga chính đồ sộ màu ngọc lam của Novosibirsk, một trong những nhà ga lớn nhất nước Nga. Kiến trúc độc đáo được ví như đầu máy hơi nước cách điệu, là cửa ngõ của thành phố trên tuyến xuyên Siberia.",
    "Ga Novosibirsk-Glavny là nhà ga đường sắt chính của thành phố và là một trong những nhà ga lớn, đẹp nhất trên toàn tuyến xuyên Siberia. Tòa nhà hiện tại khánh thành năm 1939, được thiết kế theo phong cách kết hợp giữa tân cổ điển và kiến trúc Xô Viết, với mặt tiền màu xanh ngọc lam nổi bật và sảnh trung tâm cao vòm cung – nhiều người ví hình khối của ga như một đầu máy hơi nước cách điệu đang lao tới. Vào thời điểm hoàn thành, đây được xem là nhà ga lớn nhất Liên Xô. Bên trong, sảnh chính rộng thoáng với trần cao, đèn chùm và không gian bề thế phục vụ hàng chục nghìn lượt khách mỗi ngày. Là cửa ngõ đón khách đến với thủ phủ Siberia, nhà ga vừa là công trình giao thông trọng yếu vừa là một di tích kiến trúc đáng chiêm ngưỡng. Du khách đi tàu xuyên Siberia thường dừng chân và chụp ảnh trước mặt tiền ngọc lam đặc trưng này.",
    [
        "Một trong những nhà ga lớn nhất nước Nga trên tuyến xuyên Siberia.",
        "Mặt tiền ngọc lam đặc trưng, hình khối ví như đầu máy hơi nước cách điệu.",
        "Khánh thành năm 1939, từng là nhà ga lớn nhất Liên Xô.",
    ],
    p("Hoạt động suốt ngày đêm với các chuyến tàu.",
      "Miễn phí vào sảnh ga; mua vé tàu theo hành trình.",
      "Khoảng 20–30 phút để tham quan và chụp ảnh.",
      "Quanh năm; đẹp khi mặt tiền lên đèn buổi tối.",
      "Điểm dừng quen thuộc của hành khách tuyến xuyên Siberia; chú ý giữ hành lý nơi đông người."),
    [
        {"title": "Wikipedia (RU) — Новосибирск-Главный", "url": "https://ru.wikipedia.org/wiki/Новосибирск-Главный"},
        {"title": "2GIS — Новосибирск-Главный, железнодорожный вокзал", "url": "https://2gis.ru/novosibirsk/firm/141265769369926"},
    ],
    ["monument", "railway", "architecture", "trans-siberian", "novosibirsk"],
    maps_text("Вокзал Новосибирск-Главный", "Новосибирск", "Novosibirsk-Glavny Station", "Novosibirsk", 55.035706, 82.896166),
))

# 20) Ngôi nhà 100 căn hộ (Stokvartirny dom)
RECORDS.append(rec(
    "stokvartirny-house",
    "Ngôi nhà 100 căn hộ (Stokvartirny dom)",
    "Стоквартирный дом",
    "The Hundred-Apartment House",
    ["monument"],
    55.020882, 82.924895,
    "Đại lộ Krasny Prospekt 16 / phố Sibrevkoma 1, trung tâm thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Chung cư kiến trúc hậu kiến tạo – tân cổ điển nổi tiếng, từng đoạt Grand Prix và Huy chương Vàng tại Triển lãm Thế giới Paris 1937. Một trong những công trình dân dụng biểu tượng của Novosibirsk.",
    "Ngôi nhà 100 căn hộ (Stokvartirny dom) là một trong những công trình kiến trúc dân dụng nổi tiếng nhất Novosibirsk, xây trong các năm 1934–1937 theo thiết kế của kiến trúc sư Andrey Kryachkov cùng Vasily Maslennikov. Tòa nhà tám tầng mang phong cách hậu kiến tạo (post-constructivism) pha tân cổ điển, với mặt đứng cân đối, hàng cột và các chi tiết trang trí thanh lịch. Vốn được xây làm nhà ở cho cán bộ ban chấp hành vùng Tây Siberia, công trình ban đầu có 100 căn hộ nhiều loại diện tích, nội thất sang trọng với sàn gỗ và gạch mosaic. Tại Triển lãm Nghệ thuật và Kỹ thuật Thế giới ở Paris năm 1937, thiết kế của tòa nhà đã giành Grand Prix cùng Huy chương Vàng – một vinh dự hiếm có, đưa tên tuổi kiến trúc Novosibirsk ra thế giới. Ngày nay đây là di tích kiến trúc cấp liên bang, vẫn được sử dụng làm nhà ở, và là điểm dừng đáng chú ý khi dạo bộ trên đại lộ Krasny Prospekt.",
    [
        "Đoạt Grand Prix và Huy chương Vàng tại Triển lãm Thế giới Paris 1937.",
        "Kiến trúc hậu kiến tạo – tân cổ điển của Andrey Kryachkov (1934–1937).",
        "Di tích kiến trúc cấp liên bang, biểu tượng dân dụng của thành phố.",
    ],
    p("Là nhà ở, chỉ tham quan mặt ngoài (không vào bên trong).",
      "Miễn phí (ngắm từ bên ngoài).",
      "Khoảng 15 phút.",
      "Quanh năm; đẹp khi có nắng để chụp mặt đứng.",
      "Kết hợp đi bộ dọc Krasny Prospekt cùng Bảo tàng Mỹ thuật và Quảng trường Lenin."),
    [
        {"title": "Wikipedia (RU) — Стоквартирный дом", "url": "https://ru.wikipedia.org/wiki/Стоквартирный_дом"},
        {"title": "2GIS — Красный проспект 16 (Стоквартирный дом)", "url": "https://2gis.ru/novosibirsk/geo/141373143521106"},
    ],
    ["monument", "architecture", "constructivism", "heritage", "novosibirsk"],
    maps_text("Стоквартирный дом", "Новосибирск", "Hundred-Apartment House", "Novosibirsk", 55.020882, 82.924895),
))

# 21) Đài Vinh quang (Monument Slavy)
RECORDS.append(rec(
    "monument-of-glory-novosibirsk",
    "Đài Vinh quang tưởng niệm chiến sĩ Siberia",
    "Монумент Славы",
    "Monument of Glory",
    ["monument"],
    54.987074, 82.873994,
    "Vườn Vinh quang (Сквер Славы), phố Stanislavskogo, quận Leninsky, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Đài tưởng niệm hoành tráng dành cho những người Siberia ngã xuống trong Chiến tranh Vệ quốc Vĩ đại. Quần thể gồm tượng người mẹ đau thương, Ngọn lửa Vĩnh cửu và năm trụ bê tông cao 10 m khắc tên hơn 30.000 liệt sĩ.",
    "Đài Vinh quang là một trong những đài tưởng niệm chiến tranh cảm động và bề thế nhất Novosibirsk, khánh thành ngày 6 tháng 11 năm 1967 tại Vườn Vinh quang thuộc quận Leninsky. Quần thể do họa sĩ đài kỷ niệm Alexander Chernobrovtsev cùng các đồng nghiệp thiết kế, trải rộng gần hai hecta. Trung tâm là hình tượng người mẹ đau thương, Ngọn lửa Vĩnh cửu và năm trụ bê tông cao mười mét, mỗi trụ khắc những cảnh tái hiện các giai đoạn của cuộc chiến. Mặt sau các trụ ép nổi tên bằng kim loại của hơn 30.000 người dân Novosibirsk đã ngã xuống ngoài mặt trận, tạo nên một 'bức tường ký ức' lặng người. Giữa các trụ đặt những chiếc bình chứa đất mang về từ các chiến trường khốc liệt. Đây là nơi diễn ra các lễ tưởng niệm trọng thể, đặc biệt vào Ngày Chiến thắng 9/5, và là địa điểm được người dân thành phố trân trọng gìn giữ. Quần thể được công nhận là di sản văn hóa của nước Nga.",
    [
        "Đài tưởng niệm hơn 30.000 người Siberia hy sinh trong Chiến tranh Vệ quốc.",
        "Năm trụ bê tông cao 10 m khắc cảnh chiến tranh và Ngọn lửa Vĩnh cửu.",
        "Nơi diễn ra lễ tưởng niệm trọng thể ngày Chiến thắng 9/5.",
    ],
    p("Không gian công cộng mở cửa suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 30–45 phút.",
      "Quanh năm; trang nghiêm nhất vào dịp Ngày Chiến thắng 9/5.",
      "Giữ thái độ trang nghiêm; nằm bên tả ngạn, gần ga metro 'Площадь Гарина-Михайловского'/Ленинский район."),
    [
        {"title": "Wikipedia (RU) — Монумент Славы (Новосибирск)", "url": "https://ru.wikipedia.org/wiki/Монумент_Славы_(Новосибирск)"},
        {"title": "2GIS — Монумент Славы, Сквер Славы", "url": "https://2gis.ru/novosibirsk/geo/141373143529935"},
    ],
    ["monument", "memorial", "wwii", "history", "novosibirsk"],
    maps_text("Монумент Славы", "Новосибирск", "Monument of Glory", "Novosibirsk", 54.987074, 82.873994),
))

# ============================ CÔNG VIÊN / THIÊN NHIÊN (park_garden) ============================

# 22) Vườn Bách thảo Trung tâm Siberia (CSBG)
RECORDS.append(rec(
    "central-siberian-botanical-garden",
    "Vườn Bách thảo Trung tâm Siberia (CSBG)",
    "Центральный сибирский ботанический сад СО РАН",
    "Central Siberian Botanical Garden",
    ["park_garden"],
    54.820589, 83.10452,
    "Phố Zolotodolinskaya 101, Akademgorodok, quận Sovetsky, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Vườn bách thảo lớn nhất vùng Siberia, trải rộng khoảng 850 hecta cạnh Akademgorodok. Nơi bảo tồn hàng nghìn loài thực vật cùng các nhà kính nhiệt đới và những cánh rừng taiga được gìn giữ.",
    "Vườn Bách thảo Trung tâm Siberia (CSBG) thuộc Phân viện Siberia của Viện Hàn lâm Khoa học Nga là vườn thực vật lớn nhất và quan trọng nhất của cả vùng Siberia, nằm cạnh Akademgorodok trên diện tích rộng tới khoảng 850 hecta. Đây vừa là trung tâm nghiên cứu khoa học hàng đầu về thực vật vừa là điểm dạo chơi, giáo dục sinh thái được yêu thích. Vườn lưu giữ hàng nghìn loài cây từ khắp nơi trên thế giới, gồm các bộ sưu tập cây gỗ, cây thuốc, hoa và những nhà kính nhiệt đới với xương rồng, phong lan, cây cọ. Bên trong khuôn viên còn có những cánh rừng taiga tự nhiên, các tuyến đường mòn sinh thái và khu vườn kiểu Nhật. Vào mỗi mùa, vườn khoác một vẻ đẹp riêng: hoa nở rộ mùa xuân hè, lá vàng rực mùa thu và tuyết phủ tĩnh lặng mùa đông. Đây là nơi lý tưởng để tản bộ, hít thở không khí trong lành và tìm hiểu hệ thực vật phong phú của Siberia.",
    [
        "Vườn bách thảo lớn nhất Siberia, rộng khoảng 850 hecta.",
        "Nhà kính nhiệt đới với xương rồng, phong lan cùng bộ sưu tập cây phong phú.",
        "Rừng taiga tự nhiên, đường mòn sinh thái và vườn kiểu Nhật.",
    ],
    p("Khuôn viên ngoài trời mở cửa hằng ngày; nhà kính và khu trưng bày theo giờ (thường 9:00–17:00).",
      "Vào khuôn viên phần lớn miễn phí; tham quan nhà kính/tour có thể tính phí nhỏ.",
      "Khoảng 2–3 giờ.",
      "Cuối xuân đến đầu thu cho cây cối tươi tốt; mùa thu lá vàng rất đẹp.",
      "Diện tích rất rộng – nên đi giày thoải mái, mang nước; nằm ở Akademgorodok, hơi xa trung tâm."),
    [
        {"title": "Wikipedia (RU) — Центральный сибирский ботанический сад", "url": "https://ru.wikipedia.org/wiki/Центральный_сибирский_ботанический_сад"},
        {"title": "Trang chính thức — csbg-nsk.ru", "url": "http://csbg-nsk.ru/"},
    ],
    ["park_garden", "botanical-garden", "nature", "akademgorodok", "novosibirsk"],
    maps_text("Центральный сибирский ботанический сад", "Новосибирск", "Central Siberian Botanical Garden", "Novosibirsk", 54.820589, 83.10452),
    official_site="http://csbg-nsk.ru",
))

# 23) Công viên Zayeltsovsky
RECORDS.append(rec(
    "zayeltsovsky-park",
    "Công viên Zayeltsovsky",
    "Заельцовский парк",
    "Zayeltsovsky Park",
    ["park_garden"],
    55.051474, 82.840794,
    "Phố Parkovaya 88, quận Zayeltsovsky, thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Công viên rừng thông lớn và được yêu thích ở phía bắc thành phố, lý tưởng để dạo bộ, đạp xe và nghỉ ngơi giữa thiên nhiên. Có khu vui chơi, đường dạo và gần sông Ob cùng sở thú.",
    "Công viên Zayeltsovsky là một trong những công viên rừng lớn và được yêu thích nhất Novosibirsk, nằm ở phía bắc thành phố giữa những cánh rừng thông xanh mát bên bờ sông Ob. Không gian rộng lớn với hàng thông cao vút, không khí trong lành và những con đường dạo rợp bóng khiến nơi đây trở thành 'lá phổi xanh' và điểm nghỉ ngơi cuối tuần quen thuộc của người dân. Công viên có khu vui chơi thiếu nhi, các tuyến đi bộ và đạp xe, khu picnic, sân trượt băng mùa đông và nhiều hoạt động giải trí ngoài trời. Gần đó là Sở thú Novosibirsk nổi tiếng, giúp du khách dễ dàng kết hợp một ngày tham quan trọn vẹn. Vào mùa hè, người dân đến đây tản bộ, chạy bộ và tắm nắng; mùa đông thì trượt tuyết, trượt băng và ngắm rừng thông phủ tuyết. Đây là nơi tuyệt vời để tận hưởng thiên nhiên ngay trong lòng đô thị Siberia.",
    [
        "Công viên rừng thông lớn, 'lá phổi xanh' phía bắc thành phố.",
        "Đường dạo bộ, đạp xe, khu vui chơi và hoạt động bốn mùa.",
        "Gần Sở thú Novosibirsk và bờ sông Ob.",
    ],
    p("Khuôn viên mở cửa suốt ngày; các trò chơi/dịch vụ theo giờ riêng.",
      "Vào công viên miễn phí; một số trò chơi và dịch vụ tính phí.",
      "Khoảng 2–3 giờ.",
      "Mùa hè để dạo bộ, mùa đông để trượt tuyết và ngắm rừng thông phủ tuyết.",
      "Kết hợp tham quan Sở thú gần đó; mang giày thoải mái để đi bộ đường dài."),
    [
        {"title": "Cổng du lịch Novosibirsk — Заельцовский парк", "url": "https://welcome-novosibirsk.ru/"},
        {"title": "2GIS — Заельцовский парк, Парковая 88", "url": "https://2gis.ru/novosibirsk/firm/141265769337474"},
    ],
    ["park_garden", "park", "forest", "nature", "recreation", "novosibirsk"],
    maps_text("Заельцовский парк", "Новосибирск", "Zayeltsovsky Park", "Novosibirsk", 55.051474, 82.840794),
))

# 24) Khu nghỉ dưỡng khoáng Hồ Karachi
RECORDS.append(rec(
    "lake-karachi-resort",
    "Khu nghỉ dưỡng khoáng Hồ Karachi",
    "Курорт «Озеро Карачи»",
    "Lake Karachi Health Resort",
    ["park_garden"],
    55.20465, 76.57009,
    "Làng nghỉ dưỡng Ozero-Karachi, huyện Chanovsky, tỉnh Novosibirsk, Nga (phía tây tỉnh)",
    "Khu nghỉ dưỡng chữa bệnh cấp liên bang bên hồ nước mặn Karachi, nổi tiếng với bùn khoáng và nước muối chữa bệnh. Nằm giữa thảo nguyên Baraba trong lành ở phía tây tỉnh Novosibirsk.",
    "Khu nghỉ dưỡng Hồ Karachi là một trong những điểm điều dưỡng lâu đời và nổi tiếng nhất vùng Siberia, nằm bên hồ nước mặn Karachi giữa thảo nguyên Baraba ở phía tây tỉnh Novosibirsk. Hồ nổi tiếng với lớp bùn khoáng sulfide đen quý giá và nước muối (rapa) đậm đặc, được sử dụng trong điều trị các bệnh về xương khớp, thần kinh, da liễu và phụ khoa từ cuối thế kỷ 19. Khu điều dưỡng cấp liên bang này có các cơ sở tắm bùn, tắm khoáng, vật lý trị liệu cùng nhà nghỉ, công viên và không gian thảo nguyên khoáng đạt trong lành. Nhiều du khách tìm đến đây không chỉ để chữa bệnh mà còn để thư giãn, tận hưởng khí hậu khô mát và trải nghiệm nổi bồng bềnh trên mặt nước mặn giống Biển Chết thu nhỏ. Dù cách thành phố Novosibirsk khá xa, Hồ Karachi vẫn là điểm đến đặc sắc cho những ai quan tâm đến du lịch nghỉ dưỡng và sức khỏe.",
    [
        "Khu điều dưỡng cấp liên bang bên hồ nước mặn với bùn khoáng chữa bệnh.",
        "Nước muối đậm đặc cho trải nghiệm nổi bồng bềnh như Biển Chết thu nhỏ.",
        "Nằm giữa thảo nguyên Baraba khô mát, trong lành phía tây tỉnh.",
    ],
    p("Cơ sở điều dưỡng hoạt động quanh năm; các liệu trình theo lịch đặt trước.",
      "Nghỉ dưỡng và liệu trình theo gói dịch vụ của khu điều dưỡng (đặt qua trang chính thức).",
      "Từ nửa ngày tham quan đến vài ngày lưu trú điều dưỡng.",
      "Mùa hè và đầu thu để tắm hồ và điều dưỡng thuận lợi.",
      "Cách Novosibirsk hàng trăm km về phía tây – nên đi tàu/xe và đặt phòng, liệu trình trước."),
    [
        {"title": "Trang chính thức khu điều dưỡng — okarachi.ru", "url": "https://okarachi.ru/"},
        {"title": "Komsomolskaya Pravda — Санаторий «Озеро Карачи»", "url": "https://www.kp.ru/russia/novosibirskaya-oblast/places/sanatorij-ozero-karachi/"},
    ],
    ["park_garden", "resort", "lake", "spa", "nature", "novosibirsk"],
    maps_text("Курорт Озеро Карачи", "Новосибирская область", "Lake Karachi Resort", "Chanovsky District", 55.20465, 76.57009),
    official_site="https://okarachi.ru",
))

# 25) Thác Karpysak
RECORDS.append(rec(
    "karpysak-waterfall",
    "Thác Karpysak",
    "Карпысакский водопад",
    "Karpysak Waterfall",
    ["park_garden"],
    55.053102, 83.730957,
    "Gần làng Karpysak, huyện Toguchinsky, tỉnh Novosibirsk, Nga (phía đông tỉnh)",
    "Thác nước cao khoảng 7 m hình thành từ một con đập, một trong những điểm dã ngoại thiên nhiên được yêu thích nhất tỉnh Novosibirsk. Cảnh quan đẹp, thích hợp cho chuyến đi trong ngày.",
    "Thác Karpysak là một trong những điểm đến thiên nhiên nổi tiếng và được yêu thích nhất tỉnh Novosibirsk, nằm ở huyện Toguchinsky phía đông tỉnh. Đây là thác nước nhân tạo hình thành khi dòng chảy tràn qua một đoạn đập bị vỡ tại nơi hai con suối Bugotak và Karpysak hợp lưu, tạo nên một dòng thác cao khoảng 7 mét đổ xuống ầm ào giữa khung cảnh đồng quê yên bình. Dù không quá hùng vĩ, thác lại có nét quyến rũ riêng: làn nước trắng xóa, hồ nước trong xanh phía dưới và những bãi cỏ, rừng cây xung quanh rất hợp để dã ngoại, cắm trại và chụp ảnh. Vào mùa hè, nơi đây thu hút đông người dân Novosibirsk đến picnic và tắm mát; mùa đông thác đóng băng tạo thành những cột băng độc đáo. Cảnh vật thay đổi theo mùa khiến Karpysak trở thành điểm đến hấp dẫn quanh năm cho những chuyến đi trong ngày rời xa phố thị.",
    [
        "Thác nước cao khoảng 7 m, một trong những điểm dã ngoại được yêu thích nhất tỉnh.",
        "Cảnh quan đồng quê đẹp, hợp cắm trại, picnic và chụp ảnh.",
        "Mùa đông thác đóng băng tạo thành những cột băng độc đáo.",
    ],
    p("Điểm thiên nhiên ngoài trời, tham quan tự do.",
      "Miễn phí (có thể mất phí gửi xe/dịch vụ tại các khu nghỉ lân cận).",
      "Khoảng 1–2 giờ tại thác (chưa kể di chuyển).",
      "Mùa hè để dã ngoại; mùa đông để ngắm thác băng.",
      "Cách Novosibirsk khoảng 70 km – nên đi xe riêng; đường có đoạn gồ ghề, đi giày phù hợp."),
    [
        {"title": "Báo Toguchinskaya — Карпысакский водопад", "url": "https://toggazeta.ru/karpysakskij-vodopad-unikalnaja-dostoprimechatelnost-toguchinskogo-rajona/"},
        {"title": "Yandex Maps — Карпысакский водопад", "url": "https://yandex.ru/maps/org/karpysakskiy/241706004508/"},
    ],
    ["park_garden", "waterfall", "nature", "day-trip", "novosibirsk"],
    maps_org("https://yandex.ru/maps/org/karpysakskiy/241706004508/", "Karpysak Waterfall", "Toguchinsky District"),
))

# ============================ KHÁC (other) ============================

# 26) Thành phố Berdsk
RECORDS.append(rec(
    "berdsk-city",
    "Thành phố Berdsk",
    "Бердск",
    "Berdsk",
    ["other"],
    54.7551, 83.0967,
    "Thành phố Berdsk, bên bờ Biển hồ Ob, phía nam thành phố Novosibirsk, tỉnh Novosibirsk, Nga",
    "Thành phố lớn thứ hai của tỉnh, nằm bên Biển hồ Ob với nhiều bãi biển, khu nghỉ dưỡng và rừng thông. Điểm nghỉ ngơi, tắm biển hồ và du lịch sinh thái quen thuộc của người Novosibirsk.",
    "Berdsk là thành phố lớn thứ hai của tỉnh Novosibirsk, nằm ở phía nam thủ phủ, ngay bên bờ Biển hồ Ob (hồ chứa nước rộng lớn hình thành từ đập thủy điện). Thành phố có lịch sử lâu đời, khởi nguồn từ một pháo đài Nga thế kỷ 18; khu phố cổ ban đầu đã bị ngập khi tạo hồ chứa, nên Berdsk ngày nay được xây dựng lại trên vị trí mới. Nhờ vị trí đắc địa bên biển hồ và những cánh rừng thông bao quanh, Berdsk trở thành điểm nghỉ dưỡng, tắm mát và du lịch sinh thái được người dân Novosibirsk yêu thích, với nhiều bãi biển, khu an dưỡng, trại hè và bến du thuyền. Không khí trong lành, phong cảnh sông nước và các hoạt động thể thao dưới nước khiến nơi đây nhộn nhịp vào mùa hè. Berdsk cũng là cửa ngõ để tiếp cận các điểm nghỉ dưỡng ven Biển hồ Ob và vùng ngoại ô phía nam Novosibirsk, thích hợp cho những chuyến đi cuối tuần thư giãn.",
    [
        "Thành phố lớn thứ hai của tỉnh, bên Biển hồ Ob với nhiều bãi biển.",
        "Khu nghỉ dưỡng, tắm biển hồ và du lịch sinh thái được yêu thích.",
        "Bao quanh bởi rừng thông trong lành, cửa ngõ nghỉ dưỡng phía nam Novosibirsk.",
    ],
    p("Thành phố – tham quan, nghỉ dưỡng tự do quanh năm.",
      "Miễn phí tham quan; dịch vụ bãi biển, nghỉ dưỡng, du thuyền tính phí riêng.",
      "Từ nửa ngày đến vài ngày nghỉ dưỡng.",
      "Mùa hè để tắm biển hồ và các hoạt động dưới nước.",
      "Cách Novosibirsk ~40 km về phía nam, đi tàu ngoại ô hoặc xe buýt thuận tiện; đông khách vào cuối tuần hè."),
    [
        {"title": "Wikipedia (RU) — Бердск", "url": "https://ru.wikipedia.org/wiki/Бердск"},
        {"title": "Cổng du lịch Tỉnh Novosibirsk — Бердск", "url": "https://turizm.nso.ru/"},
    ],
    ["other", "city", "ob-reservoir", "resort", "nature", "novosibirsk"],
    maps_text("Бердск", "Новосибирская область", "Berdsk", "Novosibirsk Oblast", 54.7551, 83.0967),
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
