# -*- coding: utf-8 -*-
"""_add_places_khanty-mansi_20260728_221916.py — VÙNG: Khu tự trị Khanty-Mansi – Yugra
(Ханты-Мансийский автономный округ — Югра). Lần chạy tự động 2026-07-28.

Bối cảnh: khanty-mansi.json hiện có 7 địa điểm (Археопарк, Торум Маа, Самаровский чугас,
Музей Природы и Человека, природный парк Нумто, площадь Фонтанов, Кондинские озёра).
Bổ sung 25 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 32.

Yugra là "thủ phủ dầu khí" của Nga; danh lam trải trên các thành phố Ханты-Мансийск (thủ phủ),
Сургут (lớn nhất), Нижневартовск, Нефтеюганск, Когалым, cùng các khu bảo tồn thiên nhiên rộng
lớn (taiga). Vì vậy bộ sưu tập gồm bảo tàng, nhà thờ, nhà hát, đài tưởng niệm/tượng đài, công
viên/khu bảo tồn, cầu vantовый, khu văn hoá lịch sử, và điểm hiện đại (trung tâm thể thao mùa
đông/biathlon, khu phức hợp giải trí – aquapark/oceanarium).

Phân bố loại hình (25 bản ghi mới):
- museum (6): Гос. художественный музей, Дом-музей Игошева, Музей геологии/нефти/газа
  (Ханты-Мансийск), Сургутский краеведческий музей, Нижневартовский музей им. Шуваева,
  Музей реки Обь (Нефтеюганск).
- church (4): Собор Воскресения Христова (Ханты-Мансийск), Храм Преображения Господня (Сургут),
  Храм Рождества Христова (Нижневартовск), Церковь Святого Духа (Нефтеюганск).
- theatre (2): КТЦ «Югра-Классик», Театр обско-угорских народов «Солнце» (Ханты-Мансийск).
- monument (6): Стела «Первооткрывателям земли Югорской», Мемориал Славы/Парк Победы
  (Ханты-Мансийск), Мемориал Славы/Вечный огонь (Сургут), Памятник основателям Сургута,
  скульптура «Чёрный лис» (Сургут), Памятник «Покорителям Самотлора» (Нижневартовск).
- park_garden (3): Парк «Долина ручьёв» (Ханты-Мансийск), заповедник «Малая Сосьва»,
  Юганский заповедник.
- bridge (1): Мост им. В. Солохина / Югорский мост («Красный дракон»), Сургут.
- square_street (1): Историко-культурный центр «Старый Сургут».
- other (2): Центр зимних видов спорта им. Филипенко / Биатлонный центр (Ханты-Мансийск),
  СОК «Галактика» — аквапарк/океанариум (Когалым).

TOẠ ĐỘ — xác minh chéo (ru.wikipedia geohack/infobox & GeoData, OpenStreetMap/Nominatim,
Yandex Maps org, 2026-07-28). Phạm vi Yugra lat ~58–66, lon ~59–86 — tất cả toạ độ trong phạm
vi, KHÔNG đảo lat/lon. Toạ độ đọc từ DMS ru.wiki:
  Мост Солохина/Югорский 61.226111,73.159722 (ru.wiki 61°13′34″N 73°09′35″E);
  заповедник Малая Сосьва 62.082778,64.096389 (ru.wiki 62°04′58″N 64°05′47″E — территория,
  контора в г. Советский, ул. Ленина 46); Юганский заповедник 59.655833,74.630000
  (ru.wiki 59°39′21″N 74°37′48″E — территория, центр. усадьба в с. Угут).
Toạ độ thập phân từ OSM/Yandex/ru.wiki GeoData: Собор Воскресения Христова 60.998136,69.024867;
  Гос. худ. музей 61.001335,69.016750; Дом-музей Игошева 61.004821,69.029351; Биатлонный центр/
  Центр зимних видов спорта 60.983824,69.026113; Югра-Классик 61.006834,69.025075; Театр «Солнце»
  61.004294,69.019410; Стела первооткрывателям 60.972486,69.057156 (Yandex org); Долина ручьёв
  61.000016,69.033573 (Yandex org); Парк Победы/Мемориал 61.004142,69.021753; Музей геологии
  61.002440,69.028023; Старый Сургут 61.236548,73.409047; Сургутский краеведческий музей
  61.253858,73.422913; Храм Преображения (Сургут) 61.235481,73.435368; Мемориал Славы/Вечный
  огонь (Сургут) 61.237775,73.393798; Памятник основателям Сургута 61.254030,73.396286; Чёрный
  лис 61.236745,73.407073 (Yandex org); Покорителям Самотлора 60.969234,76.531523; Музей
  им. Шуваева (Нижневартовск) 60.940335,76.561480; Храм Рождества Христова (Нижневартовск)
  60.924928,76.590871; СОК Галактика (Когалым) 62.253183,74.530745; Церковь Святого Духа
  (Нефтеюганск) 61.084462,72.611759 (Yandex org); Музей реки Обь (Нефтеюганск) 61.097633,72.618530.

GHI CHÚ: đã BỎ QUA vì không xác minh được toạ độ lãnh thổ tin cậy / trùng vị trí: природный парк
«Сибирские Увалы» (chỉ có toạ độ văn phòng đại diện ở Нижневартовск, lãnh thổ thật cách ~370 km
về ĐB, không có toạ độ nguồn tin cậy); Сургутский художественный музей (trùng toà nhà/toạ độ với
Сургутский краеведческий музей — đã giữ lại краеведческий). KHÔNG bịa toạ độ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_khanty-mansi_20260728_221916.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "khanty-mansi"
REGION_NAME_VI = "Khu tự trị Khanty-Mansi"
FD = "Vùng Ural"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
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


def prac(hours, ticket, duration, best_time, tips):
    return {
        "hours_vi": hours,
        "ticket_vi": ticket,
        "duration_vi": duration,
        "best_time_vi": best_time,
        "tips_vi": tips,
    }


RECORDS = []

# ==================================== KHANTY-MANSIYSK ====================================

# 1) Собор Воскресения Христова -------------------------------------------------------
RECORDS.append(rec(
    "resurrection-cathedral-khanty-mansiysk",
    "Nhà thờ Chính toà Phục Sinh Chúa Kitô",
    "Храм Воскресения Христова (Ханты-Мансийск)",
    "Cathedral of the Resurrection of Christ",
    ["church"],
    60.998136, 69.024867,
    "Đường Gagarina, khu quần thể chính thống giáo trung tâm thành phố Khanty-Mansiysk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Nhà thờ Phục Sinh là ngôi thánh đường Chính thống giáo lớn và nổi bật nhất Khanty-Mansiysk, nằm trong một quần thể tôn giáo có tháp chuông cao vút và bậc thang bằng đá dẫn xuống công viên. Những vòm mái mạ vàng lấp lánh giữa nền trời Siberia khiến đây thành một trong những công trình biểu tượng của thủ phủ Yugra.",
    "Nhà thờ Phục Sinh Chúa Kitô là trung tâm của một quần thể tôn giáo – văn hoá được xây dựng đầu những năm 2000 tại trung tâm Khanty-Mansiysk. Công trình theo phong cách kiến trúc Nga truyền thống với năm vòm mái dát vàng, bên cạnh là tháp chuông cao trội hẳn lên trên đường chân trời thành phố. Từ khuôn viên nhà thờ, một cầu thang đá lớn cùng dãy bậc thềm dẫn xuống công viên phía dưới, tạo thành điểm ngắm cảnh và dạo bộ được người dân yêu thích. Bên trong, nội thất được trang trí công phu với các bích hoạ và biểu tượng thánh (icon). Quần thể còn có nhà nguyện, khu vườn và không gian giáo lý, trở thành trung tâm đời sống tinh thần của cộng đồng Chính thống giáo địa phương. Với vị trí trung tâm và vẻ ngoài bề thế, nhà thờ là một trong những điểm dừng chân quen thuộc của du khách khi khám phá thủ phủ 'vùng đất của những chú ma-mút'.",
    [
        "Thánh đường Chính thống giáo lớn nhất Khanty-Mansiysk với năm vòm mái dát vàng.",
        "Tháp chuông cao và cầu thang đá dẫn xuống công viên — điểm ngắm cảnh trung tâm thành phố.",
        "Nội thất trang trí bích hoạ, icon; là trung tâm đời sống tinh thần của cộng đồng địa phương.",
    ],
    prac(
        "Mở cửa hằng ngày theo giờ lễ (thường khoảng 8:00–19:00); giờ có thể thay đổi theo mùa và ngày lễ.",
        "Vào cửa tự do (miễn phí).",
        "30–45 phút.",
        "Đẹp quanh năm; buổi chiều nắng làm vòm vàng lấp lánh, mùa đông tuyết phủ cho khung cảnh ấn tượng.",
        "Trang phục lịch sự, kín đáo khi vào bên trong; phụ nữ nên mang khăn trùm đầu; hạn chế chụp ảnh trong giờ lễ.",
    ),
    [
        {"title": "Wikipedia (RU) — Собор Воскресения Христова (Ханты-Мансийск)", "url": "https://ru.wikipedia.org/wiki/Собор_Воскресения_Христова_(Ханты-Мансийск)"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Храм+Воскресения+Христова+Ханты-Мансийск"},
    ],
    ["orthodox", "cathedral", "landmark", "khanty-mansiysk", "gold-dome"],
    maps_text("Храм Воскресения Христова", "Ханты-Мансийск", "Cathedral of the Resurrection of Christ", "Khanty-Mansiysk", 60.998136, 69.024867),
))

# 2) Государственный художественный музей ---------------------------------------------
RECORDS.append(rec(
    "khanty-mansiysk-state-art-museum",
    "Bảo tàng Mỹ thuật Quốc gia Yugra",
    "Государственный художественный музей (Ханты-Мансийск)",
    "State Art Museum (Khanty-Mansiysk)",
    ["museum"],
    61.001335, 69.016750,
    "Số 2 đường Mira, thành phố Khanty-Mansiysk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Bảo tàng Mỹ thuật Quốc gia là kho tàng nghệ thuật hàng đầu của Yugra, lưu giữ bộ sưu tập tranh và đồ hoạ quý gồm cả tác phẩm của các bậc thầy Nga như Aivazovsky, Shishkin, Repin. Đây là điểm đến văn hoá không thể bỏ qua ở trung tâm Khanty-Mansiysk.",
    "Bảo tàng Mỹ thuật Quốc gia Khanty-Mansiysk sở hữu một trong những bộ sưu tập nghệ thuật giá trị nhất vùng Ural – Siberia. Trọng tâm là bộ sưu tập hội hoạ, đồ hoạ và điêu khắc Nga thế kỷ 18–20, trong đó có tác phẩm của những tên tuổi lớn như Ivan Aivazovsky, Ivan Shishkin, Ilya Repin, Vasily Surikov cùng nhiều hoạ sĩ danh tiếng khác, phần lớn hình thành từ bộ sưu tập của tập đoàn dầu khí và các nhà sưu tầm chuyển giao cho vùng. Bảo tàng còn có bộ icon (tượng thánh) cổ, nghệ thuật trang trí – ứng dụng, và các triển lãm luân phiên giới thiệu mỹ thuật đương đại cùng nghệ thuật của các dân tộc bản địa Khanty và Mansi. Không gian trưng bày hiện đại, nằm ngay trung tâm hành chính – văn hoá của thành phố, thuận tiện kết hợp với các bảo tàng lân cận. Đây là nơi lý tưởng để hiểu chiều sâu văn hoá của một vùng thường được biết đến chủ yếu qua dầu mỏ và thiên nhiên hoang dã.",
    [
        "Bộ sưu tập hội hoạ Nga quý với tác phẩm của Aivazovsky, Shishkin, Repin, Surikov.",
        "Bộ icon (tượng thánh) cổ và nghệ thuật trang trí – ứng dụng đặc sắc.",
        "Triển lãm luân phiên về mỹ thuật đương đại và nghệ thuật bản địa Khanty – Mansi.",
    ],
    prac(
        "Thứ Ba–Chủ nhật, thường 10:00–18:00 (thứ Năm mở muộn hơn); nghỉ thứ Hai. Nên kiểm tra trước.",
        "Vé vào cửa khoảng 150–300 rúp; có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
        "1–1,5 giờ.",
        "Quanh năm; hợp làm điểm tham quan trong nhà cho những ngày đông giá rét.",
        "Có thể đặt tour thuyết minh; kết hợp cùng Bảo tàng Thiên nhiên và Con người và Bảo tàng Địa chất – Dầu – Khí ở gần đó.",
    ),
    [
        {"title": "Culture.ru — Государственный художественный музей (Ханты-Мансийск)", "url": "https://www.culture.ru/institutes/10457/gosudarstvennyi-khudozhestvennyi-muzei"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Государственный+художественный+музей+Ханты-Мансийск"},
    ],
    ["art-museum", "painting", "aivazovsky", "icons", "khanty-mansiysk"],
    maps_text("Государственный художественный музей", "Ханты-Мансийск", "State Art Museum", "Khanty-Mansiysk", 61.001335, 69.016750),
))

# 3) Дом-музей В. А. Игошева ----------------------------------------------------------
RECORDS.append(rec(
    "igoshev-house-museum",
    "Nhà lưu niệm hoạ sĩ V. A. Igoshev",
    "Дом-музей народного художника СССР В. А. Игошева",
    "V. A. Igoshev House-Museum",
    ["museum"],
    61.004821, 69.029351,
    "Số 7 đường Lopareva, thành phố Khanty-Mansiysk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Nhà lưu niệm dành riêng cho Vladimir Igoshev — hoạ sĩ Nhân dân Liên Xô, người dành cả đời vẽ về thiên nhiên và con người phương Bắc, đặc biệt là các dân tộc Khanty, Mansi. Toà nhà nhỏ xinh trưng bày các bức tranh do chính ông tặng cho Yugra.",
    "Dom-muzey V. A. Igosheva là bảo tàng cá nhân tôn vinh Vladimir Aleksandrovich Igoshev (1921–2007), hoạ sĩ được phong tặng danh hiệu Nghệ sĩ Nhân dân Liên Xô. Suốt sự nghiệp, Igoshev nhiều lần đến vùng phương Bắc Tây Siberia và say mê khắc hoạ đời sống, khuôn mặt cùng thiên nhiên của các dân tộc bản địa Khanty và Mansi — những người chăn tuần lộc, thợ săn, các bà mẹ phương Bắc. Bảo tàng được khánh thành năm 2001 trong một toà nhà được thiết kế riêng, nơi trưng bày nhiều tác phẩm mà hoạ sĩ đã hiến tặng cho vùng Yugra, cùng xưởng vẽ tái hiện, đồ dùng cá nhân và tư liệu về cuộc đời ông. Các phòng tranh dẫn dắt người xem qua hành trình sáng tác kéo dài hơn nửa thế kỷ, từ chân dung, phong cảnh taiga đến những cảnh sinh hoạt đậm chất phương Bắc. Đây là một điểm đến ấm cúng, giàu cảm xúc, giúp du khách cảm nhận vẻ đẹp và tâm hồn của vùng đất Yugra qua con mắt một danh hoạ.",
    [
        "Bảo tàng cá nhân của Vladimir Igoshev — Nghệ sĩ Nhân dân Liên Xô, danh hoạ của phương Bắc.",
        "Nhiều tranh chân dung và phong cảnh về các dân tộc Khanty, Mansi do chính hoạ sĩ hiến tặng.",
        "Xưởng vẽ tái hiện, đồ dùng cá nhân và tư liệu cuộc đời trong toà nhà thiết kế riêng.",
    ],
    prac(
        "Thứ Ba–Chủ nhật, thường 10:00–18:00; nghỉ thứ Hai. Nên kiểm tra trước.",
        "Vé vào cửa khoảng 100–200 rúp; có ưu đãi cho các đối tượng.",
        "45 phút – 1 giờ.",
        "Quanh năm; điểm tham quan trong nhà lý tưởng cho ngày lạnh.",
        "Có tour thuyết minh; gần trung tâm nên dễ đi bộ kết hợp các bảo tàng khác.",
    ),
    [
        {"title": "Culture.ru — Дом-музей народного художника СССР В. А. Игошева", "url": "https://www.culture.ru/institutes/10460/dom-muzei-narodnogo-khudozhnika-sssr-v-a-igosheva"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Дом-музей+Игошева+Ханты-Мансийск"},
    ],
    ["art-museum", "igoshev", "khanty", "mansi", "portrait", "khanty-mansiysk"],
    maps_text("Дом-музей Игошева", "Ханты-Мансийск", "Igoshev House-Museum", "Khanty-Mansiysk", 61.004821, 69.029351),
))

# 4) Центр зимних видов спорта / Биатлонный центр -------------------------------------
RECORDS.append(rec(
    "khanty-mansiysk-winter-sports-center",
    "Trung tâm Thể thao Mùa đông (Tổ hợp Biathlon)",
    "Центр зимних видов спорта имени А. В. Филипенко (Биатлонный центр)",
    "A. V. Filipenko Winter Sports Centre (Biathlon Centre)",
    ["other"],
    60.983824, 69.026113,
    "Dưới chân đồi rừng Samarovsky chugas, thành phố Khanty-Mansiysk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Trung tâm Thể thao Mùa đông mang tên A. V. Filipenko là tổ hợp biathlon và trượt tuyết băng đồng đẳng cấp thế giới, nơi từng tổ chức Giải Vô địch Biathlon Thế giới và nhiều chặng World Cup. Nằm giữa rừng taiga ngay trong lòng thành phố, đây là niềm tự hào thể thao của Yugra.",
    "Trung tâm Thể thao Mùa đông (thường gọi là Trung tâm Biathlon Khanty-Mansiysk) là một trong những tổ hợp thi đấu thể thao mùa đông hiện đại và nổi tiếng nhất nước Nga. Toạ lạc dưới chân đồi rừng Samarovsky chugas ngay trong thành phố, khu phức hợp gồm trường bắn biathlon tiêu chuẩn quốc tế, hệ thống đường trượt tuyết băng đồng (cross-country) uốn lượn qua rừng, khán đài lớn, khu bắn súng và đường lăn (roller-ski) dùng cho tập luyện mùa hè. Nơi đây đã đăng cai Giải Vô địch Biathlon Thế giới (các năm 2003 và 2011), Giải Vô địch Trượt tuyết định hướng và rất nhiều chặng Cúp Thế giới về biathlon, thu hút những ngôi sao hàng đầu và hàng nghìn khán giả. Ngoài mùa thi đấu, trung tâm mở cửa cho người dân và du khách trượt tuyết, đi bộ, chạy roller-ski và tham quan. Với hạ tầng đồng bộ và khung cảnh rừng taiga bao quanh, đây là biểu tượng cho hình ảnh Yugra như một 'thủ đô thể thao mùa đông' của Nga.",
    [
        "Tổ hợp biathlon và trượt tuyết băng đồng tầm cỡ quốc tế giữa rừng taiga trong thành phố.",
        "Từng đăng cai Giải Vô địch Biathlon Thế giới (2003, 2011) và nhiều chặng Cúp Thế giới.",
        "Mùa hè có đường roller-ski và lối đi bộ; mở cho du khách trải nghiệm thể thao ngoài trời.",
    ],
    prac(
        "Khuôn viên mở cửa ban ngày; lịch thi đấu và dịch vụ trượt tuyết thay đổi theo mùa — nên xem lịch trước.",
        "Vào khuôn viên thường miễn phí; vé xem giải đấu và thuê thiết bị tính riêng.",
        "1–2 giờ (lâu hơn nếu trượt tuyết hoặc xem thi đấu).",
        "Mùa đông (khoảng tháng 12–3) cho không khí thể thao và tuyết đẹp; mùa hè hợp đi bộ, roller-ski.",
        "Mang giày ấm chống trượt vào mùa đông; kiểm tra lịch sự kiện để trải nghiệm không khí giải đấu.",
    ),
    [
        {"title": "Wikipedia (RU) — Биатлонный центр Ханты-Мансийска", "url": "https://ru.wikipedia.org/wiki/Биатлонный_центр_Ханты-Мансийска"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Центр+зимних+видов+спорта+Филипенко"},
    ],
    ["biathlon", "winter-sports", "ski", "stadium", "world-cup", "khanty-mansiysk"],
    maps_text("Центр зимних видов спорта имени Филипенко", "Ханты-Мансийск", "Biathlon Centre", "Khanty-Mansiysk", 60.983824, 69.026113),
))

# 5) КТЦ «Югра-Классик» ---------------------------------------------------------------
RECORDS.append(rec(
    "yugra-classic-concert-theatre",
    "Trung tâm Hoà nhạc – Sân khấu 'Yugra-Classic'",
    "Концертно-театральный центр «Югра-Классик»",
    "Yugra-Classic Concert and Theatre Centre",
    ["theatre"],
    61.006834, 69.025075,
    "Số 22 đường Mira, thành phố Khanty-Mansiysk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Yugra-Classic là trung tâm hoà nhạc và biểu diễn nghệ thuật hàn lâm bậc nhất của vùng, với đại sảnh hoà nhạc trang bị đàn organ hoành tráng. Đây là 'ngôi đền âm nhạc' của thủ phủ Khanty-Mansiysk, nơi diễn ra các buổi hoà nhạc giao hưởng, opera, ballet và festival.",
    "Concertno-teatralny tsentr 'Yugra-Classic' là tổ hợp biểu diễn nghệ thuật hàn lâm hiện đại, một trong những công trình văn hoá tiêu biểu của Khanty-Mansiysk. Trung tâm sở hữu đại sảnh hoà nhạc với âm học chuẩn mực và một cây đàn organ ống lớn — hiếm có ở vùng Siberia — cùng các phòng biểu diễn nhỏ hơn cho nhạc thính phòng và sự kiện. Đây là nơi làm việc của dàn nhạc và các tập thể nghệ thuật của vùng, thường xuyên đón các nghệ sĩ và đoàn nghệ thuật danh tiếng từ Moskva, Saint Petersburg và quốc tế. Chương trình trải rộng từ hoà nhạc giao hưởng, độc tấu organ và piano, opera, ballet đến các liên hoan âm nhạc, nhạc kịch cho thiếu nhi và sự kiện của vùng. Với kiến trúc hiện đại và vị trí trung tâm, Yugra-Classic không chỉ là điểm hẹn văn hoá của người dân địa phương mà còn là lựa chọn thú vị cho du khách muốn thưởng thức một buổi tối nghệ thuật giữa lòng Yugra.",
    [
        "Đại sảnh hoà nhạc hiện đại với đàn organ ống lớn — hiếm có ở Siberia.",
        "Chương trình đa dạng: giao hưởng, opera, ballet, nhạc thính phòng và các liên hoan.",
        "Thường đón các nghệ sĩ, đoàn nghệ thuật hàng đầu của Nga và quốc tế.",
    ],
    prac(
        "Mở cửa theo lịch biểu diễn; phòng vé thường hoạt động ban ngày và trước giờ diễn.",
        "Giá vé tuỳ chương trình (thường vài trăm rúp trở lên).",
        "1,5–2,5 giờ mỗi buổi diễn.",
        "Mùa biểu diễn chính từ thu đến xuân; đặc biệt sôi động vào các dịp lễ, liên hoan.",
        "Đặt vé trước cho các chương trình lớn; trang phục lịch sự; đến sớm để tham quan sảnh.",
    ),
    [
        {"title": "Culture.ru — Концертно-театральный центр «Югра-Классик»", "url": "https://www.culture.ru/institutes/10480/koncertno-teatralnyi-centr-yugra-klassik"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Югра-Классик"},
    ],
    ["concert-hall", "organ", "classical-music", "theatre", "khanty-mansiysk"],
    maps_text("Концертно-театральный центр Югра-Классик", "Ханты-Мансийск", "Yugra-Classic Concert Hall", "Khanty-Mansiysk", 61.006834, 69.025075),
))

# 6) Театр обско-угорских народов «Солнце» --------------------------------------------
RECORDS.append(rec(
    "ob-ugric-solntse-theatre",
    "Nhà hát các dân tộc Ob-Ugri 'Mặt Trời'",
    "Театр обско-угорских народов «Солнце»",
    "Ob-Ugric Peoples' Theatre 'Solntse' (Sun)",
    ["theatre"],
    61.004294, 69.019410,
    "Nhà Hữu nghị Các dân tộc, số 14A đường Mira, thành phố Khanty-Mansiysk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Nhà hát 'Solntse' (Mặt Trời) là nhà hát độc đáo dành riêng cho văn hoá các dân tộc Ob-Ugri — Khanty và Mansi. Các vở diễn dựa trên huyền thoại, cổ tích và nghi lễ bản địa, đưa khán giả vào thế giới tâm linh của những cư dân bản địa phương Bắc.",
    "Teatr obsko-ugorskikh narodov 'Solntse' là một trong số rất ít nhà hát trên thế giới tập trung gìn giữ và tái hiện di sản sân khấu của các dân tộc Ob-Ugri — người Khanty và người Mansi bản địa của Tây Siberia. Ra đời từ cuối những năm 1990, nhà hát dàn dựng các vở kịch, chương trình dân ca – dân vũ và trình diễn dựa trên huyền thoại, sử thi, cổ tích và nghi lễ truyền thống, thường sử dụng tiếng bản địa cùng nhạc cụ, phục trang và mặt nạ dân tộc. Sân khấu của 'Solntse' đặt trong Nhà Hữu nghị Các dân tộc ở trung tâm Khanty-Mansiysk. Ngoài các buổi diễn cố định, đoàn còn tham gia nhiều liên hoan nghệ thuật của các dân tộc thiểu số phương Bắc trong và ngoài nước, trở thành 'đại sứ văn hoá' cho tiếng nói và tâm hồn của các cư dân bản địa Yugra. Đây là trải nghiệm hiếm có cho du khách muốn tiếp cận trực tiếp văn hoá phi vật thể của phương Bắc.",
    [
        "Nhà hát chuyên biệt gìn giữ di sản sân khấu của các dân tộc bản địa Khanty và Mansi.",
        "Các vở diễn dựa trên huyền thoại, sử thi, cổ tích và nghi lễ, dùng tiếng bản địa và nhạc cụ dân tộc.",
        "Đặt trong Nhà Hữu nghị Các dân tộc — trung tâm văn hoá đa sắc tộc của Yugra.",
    ],
    prac(
        "Mở cửa theo lịch biểu diễn; nên hỏi lịch tại phòng vé hoặc website.",
        "Giá vé phải chăng (thường vài trăm rúp).",
        "1–2 giờ mỗi buổi diễn.",
        "Quanh năm; sôi động vào các dịp lễ hội và liên hoan văn hoá bản địa.",
        "Kiểm tra lịch diễn trước; một số buổi bằng tiếng bản địa nhưng phần trình diễn giàu tính hình ảnh, dễ cảm nhận.",
    ),
    [
        {"title": "Culture.ru — Театр обско-угорских народов «Солнце»", "url": "https://www.culture.ru/institutes/10501/teatr-obsko-ugorskikh-narodov-solnce"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Театр+обско-угорских+народов+Солнце"},
    ],
    ["theatre", "khanty", "mansi", "indigenous", "folklore", "khanty-mansiysk"],
    maps_text("Театр обско-угорских народов Солнце", "Ханты-Мансийск", "Ob-Ugric Peoples Theatre", "Khanty-Mansiysk", 61.004294, 69.019410),
))

# 7) Стела «Первооткрывателям земли Югорской» -----------------------------------------
RECORDS.append(rec(
    "yugra-pioneers-stele",
    "Đài tưởng niệm 'Những người khai phá đất Yugra' (Tháp kim tự tháp)",
    "Стела «Первооткрывателям земли Югорской»",
    "Stele to the Pioneers of the Yugra Land",
    ["monument"],
    60.972486, 69.057156,
    "Số 1 đại lộ Pervootkryvateley, trên đồi Samarovsky chugas, thành phố Khanty-Mansiysk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Đài tưởng niệm hình kim tự tháp cao vút vinh danh những người khai phá vùng đất Yugra — các nhà thám hiểm, địa chất và thợ dầu khí. Bên trong có nhà hàng và đài quan sát trên đỉnh, phóng tầm mắt bao quát toàn thành phố và sông Irtysh.",
    "Stela 'Pervootkryvatelyam zemli Yugorskoy' là một trong những công trình biểu tượng gây ấn tượng nhất Khanty-Mansiysk. Được khánh thành năm 2003 nhân dịp kỷ niệm thành phố, đài tưởng niệm cao khoảng 62 m có hình dáng như một 'chiếc lều/kim tự tháp' vươn lên trên đỉnh đồi Samarovsky chugas, tôn vinh các thế hệ đã khám phá và khai mở vùng đất Yugra — từ những nhà thám hiểm Cossack, người bản địa, đến các nhà địa chất và công nhân dầu khí đã biến taiga hoang vu thành trung tâm năng lượng của nước Nga. Mặt ngoài công trình ốp kim loại và kính, ban đêm được chiếu sáng rực rỡ. Bên trong có nhà hàng và một đài quan sát trên cao, nơi du khách có thể phóng tầm mắt ngắm toàn cảnh thành phố, những cánh rừng taiga và hợp lưu Ob – Irtysh. Đây vừa là biểu tượng lịch sử, vừa là điểm 'sống ảo' và ngắm cảnh được yêu thích của thủ phủ Yugra.",
    [
        "Đài tưởng niệm hình kim tự tháp cao ~62 m trên đồi Samarovsky chugas — biểu tượng của thành phố.",
        "Vinh danh các thế hệ khai phá đất Yugra: thám hiểm, địa chất, thợ dầu khí.",
        "Có nhà hàng và đài quan sát trên cao ngắm toàn cảnh thành phố và taiga.",
    ],
    prac(
        "Ngắm bên ngoài tự do 24/7; nhà hàng/đài quan sát bên trong mở theo giờ riêng — nên hỏi trước.",
        "Ngắm ngoài trời miễn phí; sử dụng dịch vụ bên trong tính phí.",
        "30–45 phút (lâu hơn nếu lên đài quan sát hoặc dùng bữa).",
        "Đẹp cả ngày lẫn đêm; ban đêm công trình được chiếu sáng, hoàng hôn nhìn ra Irtysh rất đẹp.",
        "Kết hợp cùng Arkheopark và đồi Samarovsky chugas gần đó; mặc ấm vì trên đồi nhiều gió.",
    ),
    [
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Стела+Первооткрывателям+земли+Югорской"},
        {"title": "Yandex Maps — Первооткрывателям земли Югорской", "url": "https://yandex.ru/maps/org/pervootkryvatelyam_zemli_yugorskoy/39609051604/"},
    ],
    ["monument", "stele", "viewpoint", "oil-pioneers", "landmark", "khanty-mansiysk"],
    maps_org("https://yandex.ru/maps/org/pervootkryvatelyam_zemli_yugorskoy/39609051604/", "Stele to the Pioneers of Yugra", "Khanty-Mansiysk"),
))

# 8) Парк «Долина ручьёв» -------------------------------------------------------------
RECORDS.append(rec(
    "valley-of-streams-park",
    "Công viên 'Thung lũng Suối' (Dolina Ruchyov)",
    "Парк «Долина ручьёв»",
    "Valley of Streams Park",
    ["park_garden"],
    61.000016, 69.033573,
    "Đường Patrisa Lumumby, thành phố Khanty-Mansiysk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Dolina Ruchyov là công viên cảnh quan trong lòng Khanty-Mansiysk, nương theo địa hình khe suối và đồi rừng tự nhiên. Những cây cầu gỗ, lối đi lát sàn và tiểu cảnh ven suối biến nơi đây thành điểm dạo bộ, thư giãn ưa thích của người dân.",
    "Park 'Dolina ruchyov' (Thung lũng Những dòng suối) là một công viên cảnh quan được quy hoạch khéo léo dựa trên địa hình tự nhiên đặc trưng của Khanty-Mansiysk — thành phố nằm giữa những ngọn đồi rừng và khe suối. Thay vì san phẳng, các nhà thiết kế giữ lại dòng suối, sườn dốc và cây rừng, rồi bổ sung hệ thống lối đi lát sàn gỗ, cầu nhỏ bắc qua suối, bậc thang, đèn trang trí, chòi nghỉ và tiểu cảnh. Kết quả là một không gian xanh mềm mại uốn lượn theo thung lũng, nơi người dân đến đi bộ, chạy bộ, đưa trẻ dạo chơi và chụp ảnh. Vào mùa hè, cây cối tươi tốt và tiếng suối róc rách tạo cảm giác thư thái ngay giữa đô thị; mùa đông, tuyết phủ và ánh đèn biến nơi đây thành khung cảnh cổ tích. Gần trung tâm và các bảo tàng, công viên là điểm dừng chân dễ chịu để tận hưởng thiên nhiên đô thị của thủ phủ Yugra.",
    [
        "Công viên cảnh quan bám theo khe suối và đồi rừng tự nhiên giữa lòng thành phố.",
        "Lối đi lát sàn gỗ, cầu nhỏ, bậc thang và tiểu cảnh ven suối — lý tưởng để dạo bộ, chụp ảnh.",
        "Đẹp cả bốn mùa; mùa đông tuyết phủ và đèn trang trí tạo khung cảnh cổ tích.",
    ],
    prac(
        "Không gian ngoài trời, mở cửa tự do (thường có chiếu sáng buổi tối).",
        "Miễn phí.",
        "45 phút – 1 giờ.",
        "Mùa hè cây xanh và suối chảy; mùa đông tuyết đẹp — cả hai đều hấp dẫn.",
        "Giày thoải mái; buổi tối có đèn nên hợp đi dạo; kết hợp tham quan trung tâm gần đó.",
    ),
    [
        {"title": "Yandex Maps — Парк «Долина ручьёв»", "url": "https://yandex.ru/maps/org/park_dolina_ruchyev/156654720481/"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Долина+ручьёв+Ханты-Мансийск"},
    ],
    ["park", "urban-nature", "walking", "stream", "khanty-mansiysk"],
    maps_org("https://yandex.ru/maps/org/park_dolina_ruchyev/156654720481/", "Valley of Streams Park", "Khanty-Mansiysk"),
))

# 9) Мемориал Славы / Парк Победы -----------------------------------------------------
RECORDS.append(rec(
    "khanty-mansiysk-victory-park-memorial",
    "Công viên Chiến thắng và Đài tưởng niệm Vinh quang",
    "Парк Победы и Мемориал Славы (Ханты-Мансийск)",
    "Victory Park and Memorial of Glory (Khanty-Mansiysk)",
    ["monument"],
    61.004142, 69.021753,
    "Trung tâm thành phố Khanty-Mansiysk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Công viên Chiến thắng cùng Đài tưởng niệm Vinh quang là không gian tưởng niệm những người con Yugra đã ngã xuống trong Thế chiến II. Ngọn lửa vĩnh cửu, tượng đài và các tấm bia tên tạo nên nơi trang nghiêm bậc nhất thành phố.",
    "Park Pobedy (Công viên Chiến thắng) và Memorial Slavy (Đài tưởng niệm Vinh quang) ở trung tâm Khanty-Mansiysk là quần thể tưởng niệm dành cho những người dân Yugra đã hy sinh trong Cuộc Chiến tranh Vệ quốc Vĩ đại (1941–1945). Trung tâm quần thể là ngọn Lửa Vĩnh cửu cùng tượng đài chiến sĩ và các bức tường/bia khắc tên những người ngã xuống, được bao quanh bởi công viên cây xanh, lối đi và các không gian nghi lễ. Vào ngày 9 tháng 5 (Ngày Chiến thắng) và các dịp lễ trọng, nơi đây diễn ra lễ đặt hoa, diễu hành và những hoạt động tưởng niệm thu hút đông đảo người dân. Ngày thường, công viên là không gian yên tĩnh để dạo bộ và tưởng nhớ. Là một trong những địa điểm mang ý nghĩa lịch sử – tinh thần quan trọng nhất của thành phố, quần thể giúp du khách hiểu thêm về ký ức chiến tranh và lòng tự hào của cộng đồng phương Bắc.",
    [
        "Ngọn Lửa Vĩnh cửu, tượng đài chiến sĩ và các bia khắc tên người con Yugra hy sinh trong Thế chiến II.",
        "Không gian nghi lễ trung tâm dịp Ngày Chiến thắng 9/5 với lễ đặt hoa và diễu hành.",
        "Công viên cây xanh yên tĩnh, mang ý nghĩa lịch sử – tinh thần quan trọng của thành phố.",
    ],
    prac(
        "Không gian ngoài trời, mở cửa tự do.",
        "Miễn phí.",
        "20–40 phút.",
        "Quanh năm; đặc biệt trang nghiêm và đông đúc vào ngày 9/5.",
        "Giữ thái độ tôn nghiêm; kết hợp dạo trung tâm thành phố lân cận.",
    ),
    [
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Парк+Победы+Мемориал+Славы+Ханты-Мансийск"},
        {"title": "OpenStreetMap — Парк Победы (Ханты-Мансийск)", "url": "https://www.openstreetmap.org/way/37355528"},
    ],
    ["memorial", "wwii", "eternal-flame", "victory-park", "khanty-mansiysk"],
    maps_text("Мемориал Славы Парк Победы", "Ханты-Мансийск", "Victory Park Memorial", "Khanty-Mansiysk", 61.004142, 69.021753),
))

# 10) Музей геологии, нефти и газа ----------------------------------------------------
RECORDS.append(rec(
    "museum-geology-oil-gas",
    "Bảo tàng Địa chất, Dầu và Khí",
    "Музей геологии, нефти и газа",
    "Museum of Geology, Oil and Gas",
    ["museum"],
    61.002440, 69.028023,
    "Số 9 đường Chekhova, thành phố Khanty-Mansiysk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Bảo tàng Địa chất, Dầu và Khí là bảo tàng chuyên đề độc đáo kể câu chuyện Yugra đã trở thành 'trái tim dầu khí' của nước Nga như thế nào. Các trưng bày về địa chất, khoáng vật, lịch sử thăm dò và khai thác dầu khí giúp du khách hiểu bản sắc kinh tế của vùng.",
    "Muzey geologii, nefti i gaza ở Khanty-Mansiysk là bảo tàng nhà nước hiếm hoi ở Nga dành riêng cho lịch sử địa chất và ngành công nghiệp dầu khí — ngành đã định hình toàn bộ vận mệnh vùng Yugra. Được thành lập từ năm 1993, bảo tàng có các bộ sưu tập phong phú về đá, khoáng vật, mẫu lõi khoan (core), hoá thạch, thiết bị thăm dò và bản đồ địa chất, cùng những trưng bày tương tác tái hiện cấu trúc lòng đất Tây Siberia và cách hình thành các mỏ dầu. Một phần quan trọng dành cho lịch sử 'cơn sốt dầu' những năm 1960 – khi các nhà địa chất phát hiện những mỏ khổng lồ như Samotlor, biến taiga hoang vu thành trung tâm năng lượng của Liên Xô và nước Nga. Bảo tàng cũng khắc hoạ chân dung những nhà địa chất, kỹ sư tiên phong và đời sống của các đô thị dầu khí. Đây là điểm đến giàu tính giáo dục và bất ngờ thú vị, đặc biệt với những ai muốn hiểu vì sao Yugra được gọi là 'thủ đô dầu khí' của nước Nga.",
    [
        "Bảo tàng chuyên đề hiếm có về địa chất và công nghiệp dầu khí — bản sắc của Yugra.",
        "Bộ sưu tập đá, khoáng vật, mẫu lõi khoan, hoá thạch và trưng bày tương tác về lòng đất Tây Siberia.",
        "Kể lại 'cơn sốt dầu' thập niên 1960 và phát hiện các mỏ khổng lồ như Samotlor.",
    ],
    prac(
        "Thứ Ba–Chủ nhật, thường 10:00–18:00; nghỉ thứ Hai. Nên kiểm tra trước.",
        "Vé vào cửa khoảng 150–300 rúp; có ưu đãi cho các đối tượng.",
        "1–1,5 giờ.",
        "Quanh năm; điểm tham quan trong nhà lý tưởng cho ngày lạnh.",
        "Có tour thuyết minh và trưng bày tương tác hợp cho gia đình; gần các bảo tàng trung tâm.",
    ),
    [
        {"title": "Culture.ru — Музей геологии, нефти и газа", "url": "https://www.culture.ru/institutes/10467/muzei-geologii-nefti-i-gaza"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Музей+геологии+нефти+и+газа+Ханты-Мансийск"},
    ],
    ["museum", "geology", "oil-gas", "science", "khanty-mansiysk"],
    maps_text("Музей геологии, нефти и газа", "Ханты-Мансийск", "Museum of Geology Oil and Gas", "Khanty-Mansiysk", 61.002440, 69.028023),
))

# ==================================== СУРГУТ (SURGUT) ====================================

# 11) Мост им. В. Солохина / Югорский мост -------------------------------------------
RECORDS.append(rec(
    "yugorsky-bridge-surgut",
    "Cầu dây văng Yugorsky (Cầu 'Rồng Đỏ' Surgut)",
    "Мост имени Валентина Солохина (Югорский мост)",
    "Yugorsky Bridge (Valentin Solokhin Bridge)",
    ["bridge"],
    61.226111, 73.159722,
    "Bắc qua sông Ob, cách trung tâm Surgut khoảng 5 km về phía tây, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Cầu Yugorsky bắc qua sông Ob ở Surgut là một trong những cây cầu dây văng biểu tượng của nước Nga, nổi tiếng với nhịp chính do MỘT trụ tháp duy nhất cao 150 m nâng đỡ — kỷ lục thế giới. Dàn cáp xoè như cánh khiến người ta gọi cầu là 'Rồng Đỏ'.",
    "Most imeni Valentina Solokhina, quen gọi là Yugorsky most (cầu Yugorsky), là cây cầu dây văng bắc qua sông Ob gần Surgut, khánh thành tháng 9 năm 2000 sau 5 năm xây dựng. Cầu dài 2.110 m với nhịp chính 408 m; điều khiến nó nổi danh thế giới là nhịp chính chỉ được nâng đỡ bởi MỘT trụ tháp (pylon) duy nhất cao 150 m — một kỷ lục được ghi nhận. Nhìn từ xa, hệ cáp văng toả ra từ đỉnh trụ tạo hình như một cánh buồm hay đôi cánh, và vào lúc hoàng hôn hay khi được chiếu sáng, dáng vẻ ấy khiến cây cầu được ví như một 'con rồng đỏ' vắt ngang dòng Ob. Cầu là mắt xích giao thông chiến lược nối Surgut với các vùng khai thác dầu khí của Yugra và Yamal với 'đất liền lớn'; trước khi có cầu, việc qua sông chỉ nhờ phà mùa hè và đường băng trên băng mùa đông. Nhân kỷ niệm 9 năm, ngay dưới chân cầu đã mở một bảo tàng nhỏ về những người xây cầu. Từng được bình chọn là một trong những cây cầu đẹp nhất nước Nga, đây là biểu tượng và điểm 'sống ảo' nổi bật của Surgut.",
    [
        "Nhịp chính 408 m chỉ do MỘT trụ tháp cao 150 m nâng đỡ — kỷ lục thế giới về cầu một trụ.",
        "Tổng chiều dài 2.110 m bắc qua sông Ob; dàn cáp xoè cánh nên được gọi là 'Rồng Đỏ'.",
        "Từng được bình chọn là một trong những cây cầu đẹp nhất nước Nga; có bảo tàng nhỏ dưới chân cầu.",
    ],
    prac(
        "Cầu giao thông, hoạt động 24/7; ngắm cảnh từ các điểm ven bờ và bãi gần chân cầu.",
        "Miễn phí (đường bộ công cộng).",
        "20–40 phút để ngắm và chụp ảnh.",
        "Đẹp nhất lúc hoàng hôn và ban đêm khi cầu lên đèn; mùa hè dễ tiếp cận bờ sông.",
        "Đến các điểm ngắm ven bờ để có góc nhìn trọn cây cầu; chú ý an toàn giao thông, không dừng trên lòng cầu.",
    ),
    [
        {"title": "Wikipedia (RU) — Мост имени Валентина Солохина (Югорский мост)", "url": "https://ru.wikipedia.org/wiki/Мост_имени_Валентина_Солохина"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Югорский+мост+Сургут"},
    ],
    ["bridge", "cable-stayed", "ob-river", "record", "red-dragon", "surgut"],
    maps_text("Югорский мост", "Сургут", "Yugorsky Bridge", "Surgut", 61.226111, 73.159722),
))

# 12) Историко-культурный центр «Старый Сургут» --------------------------------------
RECORDS.append(rec(
    "old-surgut-cultural-center",
    "Khu văn hoá – lịch sử 'Surgut Cổ'",
    "Историко-культурный центр «Старый Сургут»",
    "Old Surgut Historical and Cultural Centre",
    ["square_street"],
    61.236548, 73.409047,
    "Số 2 đường Energetikov, thành phố Surgut, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "'Stary Surgut' (Surgut Cổ) là một quần thể tái hiện phố cổ bằng những ngôi nhà gỗ truyền thống, tái dựng diện mạo Surgut thế kỷ 19 – đầu 20. Đây là 'tấm danh thiếp' của thành phố, nơi tập trung bảo tàng, xưởng thủ công và ngôi nhà thờ gỗ độc đáo.",
    "Istoriko-kulturny tsentr 'Stary Surgut' là một khu bảo tồn – tái hiện phố cổ giữa lòng thành phố dầu khí hiện đại Surgut. Quần thể gồm hơn chục ngôi nhà gỗ theo lối kiến trúc Siberia truyền thống, một số được phục dựng, một số là nhà cổ di dời về, tái hiện diện mạo Surgut vào cuối thế kỷ 19 – đầu thế kỷ 20 khi nơi đây còn là một thị trấn thương nhân và Cossack ven sông Ob. Bên trong các ngôi nhà là bảo tàng và không gian trưng bày về lịch sử thành phố, đời sống thương nhân, văn hoá các dân tộc bản địa, cùng các xưởng thủ công (rèn, dệt, gốm). Điểm nhấn kiến trúc là ngôi nhà thờ gỗ 'Đền thờ Đấng Cứu Thế Nhân Từ' màu đen độc đáo, dựng hoàn toàn bằng gỗ theo kỹ thuật truyền thống. Quần thể còn có 'cây cột dân tộc', khu tượng và các lễ hội dân gian theo mùa. Với không khí hoài niệm và giá trị giáo dục, 'Stary Surgut' là điểm đến hàng đầu để hiểu cội nguồn của một trong những đô thị trẻ, giàu có nhất Siberia.",
    [
        "Quần thể phố cổ bằng nhà gỗ tái hiện Surgut cuối thế kỷ 19 – đầu 20.",
        "Nhà thờ gỗ 'Đấng Cứu Thế Nhân Từ' màu đen dựng theo kỹ thuật truyền thống — độc đáo hiếm thấy.",
        "Các bảo tàng, xưởng thủ công và lễ hội dân gian — 'tấm danh thiếp' của thành phố Surgut.",
    ],
    prac(
        "Khuôn viên mở cửa ban ngày; các bảo tàng bên trong thường 10:00–18:00, một số nghỉ thứ Hai.",
        "Dạo khuôn viên thường miễn phí; vé vào từng bảo tàng/xưởng tính riêng (thường vài chục đến vài trăm rúp).",
        "1–2 giờ.",
        "Đẹp quanh năm; mùa hè dễ dạo bộ, các dịp lễ có hội dân gian; mùa đông nhà gỗ phủ tuyết rất nên thơ.",
        "Nên đi cùng thuyết minh để hiểu lịch sử; dành thời gian xem nhà thờ gỗ và các xưởng thủ công.",
    ),
    [
        {"title": "Wikipedia (RU) — Старый Сургут", "url": "https://ru.wikipedia.org/wiki/Старый_Сургут"},
        {"title": "OpenStreetMap — Старый Сургут", "url": "https://www.openstreetmap.org/way/97703787"},
    ],
    ["open-air-museum", "wooden-architecture", "old-town", "history", "surgut"],
    maps_text("Историко-культурный центр Старый Сургут", "Сургут", "Old Surgut", "Surgut", 61.236548, 73.409047),
))

# 13) Сургутский краеведческий музей -------------------------------------------------
RECORDS.append(rec(
    "surgut-museum-local-lore",
    "Bảo tàng Địa phương học Surgut",
    "Сургутский краеведческий музей",
    "Surgut Museum of Local Lore",
    ["museum"],
    61.253858, 73.422913,
    "Số 21/2 đường 30 let Pobedy, thành phố Surgut, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Bảo tàng Địa phương học Surgut là một trong những bảo tàng lâu đời nhất Yugra, lưu giữ câu chuyện của vùng đất từ thời tiền sử, thời Surgut là pháo đài Cossack, đến kỷ nguyên dầu khí. Các bộ sưu tập khảo cổ, dân tộc học và lịch sử phong phú giúp hiểu trọn hành trình của thành phố.",
    "Surgutsky krayevedchesky muzey là bảo tàng tổng hợp về lịch sử, thiên nhiên và văn hoá của Surgut cùng vùng phụ cận — một trong những bảo tàng ra đời sớm nhất ở Yugra (từ những năm 1960). Bộ sưu tập trải rộng qua nhiều chủ đề: khảo cổ học với hiện vật của các nền văn hoá cổ ven sông Ob; dân tộc học về người Khanty bản địa (trang phục, đồ dùng, tín ngưỡng); lịch sử Surgut từ khi được lập làm pháo đài (ostrog) Cossack năm 1594 để bảo vệ tuyến đường Siberia; và giai đoạn bùng nổ dầu khí thế kỷ 20 biến thị trấn nhỏ thành đô thị công nghiệp lớn. Bảo tàng còn quản lý nhiều chi nhánh trong thành phố, trong đó có các ngôi nhà – bảo tàng lịch sử. Với các trưng bày thường xuyên và triển lãm luân phiên, đây là nơi lý tưởng để du khách nắm bắt bức tranh toàn cảnh về quá khứ và bản sắc của Surgut, vượt ra ngoài hình ảnh quen thuộc của một 'thành phố dầu mỏ'.",
    [
        "Một trong những bảo tàng lâu đời nhất Yugra, kể lịch sử Surgut từ thời tiền sử đến kỷ nguyên dầu khí.",
        "Bộ sưu tập khảo cổ ven sông Ob và dân tộc học về người Khanty bản địa.",
        "Trưng bày về pháo đài Cossack Surgut (lập năm 1594) và giai đoạn bùng nổ dầu khí.",
    ],
    prac(
        "Thứ Ba–Chủ nhật, thường 10:00–18:00; nghỉ thứ Hai. Nên kiểm tra trước.",
        "Vé vào cửa khoảng 100–250 rúp; có ưu đãi cho các đối tượng.",
        "1–1,5 giờ.",
        "Quanh năm; điểm tham quan trong nhà lý tưởng cho ngày lạnh.",
        "Có tour thuyết minh và nhiều chi nhánh; hỏi để mua vé liên tuyến nếu muốn thăm nhiều điểm.",
    ),
    [
        {"title": "Culture.ru — Сургутский краеведческий музей", "url": "https://www.culture.ru/institutes/10520/surgutskii-kraevedcheskii-muzei"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Сургутский+краеведческий+музей"},
    ],
    ["museum", "local-lore", "archaeology", "ethnography", "history", "surgut"],
    maps_text("Сургутский краеведческий музей", "Сургут", "Surgut Museum of Local Lore", "Surgut", 61.253858, 73.422913),
))

# 14) Храм Преображения Господня (Сургут) --------------------------------------------
RECORDS.append(rec(
    "transfiguration-church-surgut",
    "Nhà thờ Chúa Hiển Dung Surgut",
    "Храм в честь Преображения Господня (Сургут)",
    "Church of the Transfiguration of the Lord (Surgut)",
    ["church"],
    61.235481, 73.435368,
    "Khu vực đường Melik-Karamova, thành phố Surgut, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Nhà thờ Chúa Hiển Dung là một trong những thánh đường Chính thống giáo lớn và đẹp nhất Surgut, nổi bật với các vòm mái dát vàng và kiến trúc Nga truyền thống. Đây là trung tâm tôn giáo quan trọng của thành phố.",
    "Khram v chest Preobrazheniya Gospodnya (Nhà thờ Chúa Hiển Dung) là một trong những công trình tôn giáo Chính thống giáo tiêu biểu của Surgut, được xây dựng trong giai đoạn thành phố phát triển mạnh cuối thế kỷ 20 – đầu thế kỷ 21. Nhà thờ mang phong cách kiến trúc Nga truyền thống với khối chính bề thế, nhiều vòm mái hình củ hành dát vàng lấp lánh và tháp chuông, tạo điểm nhấn nổi bật trên nền các khu phố hiện đại. Bên trong, không gian được trang trí bằng bích hoạ, iconostas (vách ngăn đặt icon) và các biểu tượng thánh. Nhà thờ không chỉ là nơi hành lễ mà còn là trung tâm sinh hoạt cộng đồng của giáo dân Surgut, với trường giáo lý và các hoạt động từ thiện, văn hoá. Với quy mô và vẻ đẹp của mình, đây là một trong những địa điểm được du khách ghé thăm khi tìm hiểu đời sống tinh thần và kiến trúc tôn giáo của đô thị dầu khí lớn nhất Yugra.",
    [
        "Một trong những thánh đường Chính thống giáo lớn và đẹp nhất Surgut.",
        "Kiến trúc Nga truyền thống với nhiều vòm mái củ hành dát vàng và tháp chuông.",
        "Nội thất bích hoạ, iconostas; trung tâm sinh hoạt tôn giáo – cộng đồng của thành phố.",
    ],
    prac(
        "Mở cửa hằng ngày theo giờ lễ (thường khoảng 8:00–19:00); có thể thay đổi.",
        "Vào cửa tự do (miễn phí).",
        "20–40 phút.",
        "Quanh năm; buổi lễ lớn và các dịp lễ Chính thống giáo rất trang nghiêm.",
        "Trang phục kín đáo; phụ nữ nên trùm khăn; hạn chế chụp ảnh trong giờ lễ.",
    ),
    [
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Храм+Преображения+Господня+Сургут"},
        {"title": "OpenStreetMap — Храм Преображения Господня (Сургут)", "url": "https://www.openstreetmap.org/way/78193609"},
    ],
    ["orthodox", "church", "gold-dome", "surgut"],
    maps_text("Храм Преображения Господня", "Сургут", "Church of the Transfiguration", "Surgut", 61.235481, 73.435368),
))

# 15) Мемориал Славы / Вечный огонь (Сургут) -----------------------------------------
RECORDS.append(rec(
    "surgut-glory-memorial",
    "Đài tưởng niệm Vinh quang và Lửa Vĩnh cửu Surgut",
    "Мемориал Славы (Сургут)",
    "Memorial of Glory (Surgut)",
    ["monument"],
    61.237775, 73.393798,
    "Trung tâm thành phố Surgut, gần quảng trường trung tâm, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Đài tưởng niệm Vinh quang Surgut là quần thể tưởng nhớ những người con của thành phố đã hy sinh trong Thế chiến II, với Lửa Vĩnh cửu và các bức tường khắc tên. Đây là địa điểm nghi lễ trang nghiêm bậc nhất của Surgut.",
    "Memorial Slavy (Đài tưởng niệm Vinh quang) là quần thể tưởng niệm trung tâm của Surgut, dành cho những người dân thành phố và vùng đã ngã xuống trong Cuộc Chiến tranh Vệ quốc Vĩ đại 1941–1945. Trung tâm quần thể là ngọn Lửa Vĩnh cửu cùng tượng đài và các bức tường/bia khắc tên những người hy sinh, được bố trí trên một quảng trường lát đá với không gian mở dành cho nghi lễ. Vào ngày 9 tháng 5 (Ngày Chiến thắng) và các dịp trọng đại, nơi đây diễn ra lễ đặt vòng hoa, phút mặc niệm và các hoạt động tưởng niệm với sự tham dự của cựu chiến binh, học sinh và đông đảo người dân. Ngày thường, đây là không gian tĩnh lặng để tưởng nhớ và là điểm hẹn quen thuộc của thành phố. Là biểu tượng cho lòng biết ơn và ký ức lịch sử, đài tưởng niệm giúp du khách cảm nhận chiều sâu tinh thần của một đô thị trẻ nhưng gắn bó với truyền thống chung của nước Nga.",
    [
        "Ngọn Lửa Vĩnh cửu và các bức tường khắc tên người Surgut hy sinh trong Thế chiến II.",
        "Quảng trường nghi lễ trung tâm — nơi tổ chức lễ Ngày Chiến thắng 9/5.",
        "Không gian trang nghiêm, mang ý nghĩa lịch sử – tinh thần của thành phố.",
    ],
    prac(
        "Không gian ngoài trời, mở cửa tự do.",
        "Miễn phí.",
        "20–30 phút.",
        "Quanh năm; đặc biệt trang nghiêm và đông đúc vào ngày 9/5.",
        "Giữ thái độ tôn nghiêm; kết hợp dạo trung tâm thành phố lân cận.",
    ),
    [
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Мемориал+Славы+Сургут"},
        {"title": "OpenStreetMap — Мемориал Славы (Сургут)", "url": "https://www.openstreetmap.org/relation/2080823"},
    ],
    ["memorial", "wwii", "eternal-flame", "surgut"],
    maps_text("Мемориал Славы", "Сургут", "Memorial of Glory", "Surgut", 61.237775, 73.393798),
))

# 16) Памятник основателям Сургута ---------------------------------------------------
RECORDS.append(rec(
    "surgut-founders-monument",
    "Tượng đài Những người sáng lập Surgut",
    "Памятник основателям Сургута",
    "Monument to the Founders of Surgut",
    ["monument"],
    61.254030, 73.396286,
    "Ven sông (khu vực đường Ostrovskogo), thành phố Surgut, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Tượng đài Những người sáng lập Surgut khắc hoạ nhóm nhân vật đã lập nên pháo đài Surgut năm 1594: viên quản đốc (voivode), vị linh mục, người Cossack và người Khanty bản địa. Đây là một trong những tượng đài lịch sử được yêu thích nhất thành phố.",
    "Pamyatnik osnovatelyam Surguta (Tượng đài Những người sáng lập Surgut) được khánh thành năm 2002, tôn vinh những con người đã khai sinh ra thành phố khi pháo đài (ostrog) Surgut được lập năm 1594 trên bờ sông Ob theo lệnh của Sa hoàng, nhằm kiểm soát và bảo vệ tuyến đường chinh phục Siberia. Cụm tượng đồng gồm bốn nhân vật tiêu biểu: viên quản đốc/voivode (đại diện chính quyền), vị linh mục Chính thống giáo (đại diện đức tin), người lính Cossack (đại diện lực lượng khai phá) và người Khanty bản địa (đại diện cư dân bản xứ) — cùng nhau tượng trưng cho sự hình thành đa tầng của thành phố. Tác phẩm đặt tại khu vực đẹp ven sông, trở thành điểm dừng chân, chụp ảnh và tìm hiểu lịch sử được người dân lẫn du khách yêu thích. Đây là một trong những biểu tượng lịch sử quan trọng, nhắc nhớ rằng dưới lớp áo hiện đại của 'thủ đô dầu khí', Surgut là một trong những đô thị lâu đời nhất Siberia.",
    [
        "Cụm tượng đồng bốn nhân vật: voivode, linh mục, người Cossack và người Khanty bản địa.",
        "Kỷ niệm việc lập pháo đài Surgut năm 1594 — một trong những đô thị cổ nhất Siberia.",
        "Đặt tại khu vực đẹp ven sông; điểm chụp ảnh và tìm hiểu lịch sử được yêu thích.",
    ],
    prac(
        "Không gian ngoài trời, mở cửa tự do 24/7.",
        "Miễn phí.",
        "15–30 phút.",
        "Đẹp nhất mùa hè khi dạo ven sông; hoàng hôn cho ảnh đẹp.",
        "Kết hợp dạo bờ sông Ob và trung tâm Surgut; mặc ấm nếu đi vào mùa lạnh.",
    ),
    [
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Памятник+основателям+Сургута"},
        {"title": "OpenStreetMap — Памятник основателям Сургута", "url": "https://www.openstreetmap.org/node/1669882821"},
    ],
    ["monument", "sculpture", "history", "founders", "cossack", "surgut"],
    maps_text("Памятник основателям Сургута", "Сургут", "Monument to the Founders of Surgut", "Surgut", 61.254030, 73.396286),
))

# 17) Скульптура «Чёрный лис» (Сургут) -----------------------------------------------
RECORDS.append(rec(
    "black-fox-sculpture-surgut",
    "Tượng 'Cáo Đen' — biểu tượng Surgut",
    "Скульптура «Чёрный лис»",
    "Black Fox Sculpture",
    ["monument"],
    61.236745, 73.407073,
    "Gần khu văn hoá 'Stary Surgut', đường Energetikov, thành phố Surgut, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Tượng 'Cáo Đen' (Chyorny Lis) là hiện thân của biểu tượng trên huy hiệu thành phố Surgut — con cáo/chồn zibelin đen quý giá, gắn với nghề săn lông thú từng làm nên sự giàu có của vùng. Bức tượng đồng duyên dáng là điểm 'sống ảo' được du khách yêu thích.",
    "Skulptura 'Chyorny lis' (Cáo Đen) là một tác phẩm điêu khắc đô thị gắn liền với bản sắc Surgut, đặt gần khu văn hoá – lịch sử 'Stary Surgut'. Con cáo đen (gợi nhắc loài chồn zibelin/cáo lông đen quý) chính là hình tượng trung tâm trên huy hiệu (coat of arms) của thành phố, biểu trưng cho nghề săn và buôn bán lông thú — nguồn của cải từng khiến Surgut trở nên trù phú thời còn là thị trấn thương nhân Siberia. Bức tượng đồng khắc hoạ con cáo trong tư thế sống động, duyên dáng, đứng trên bệ đá, nhanh chóng trở thành một trong những điểm chụp ảnh được yêu thích và một 'linh vật' thân thương của người dân. Nhiều du khách tin rằng chạm vào tượng sẽ mang lại may mắn. Nhỏ gọn nhưng giàu ý nghĩa, 'Cáo Đen' là cách thú vị để kể câu chuyện về cội nguồn và biểu tượng của thành phố dầu khí lớn nhất Yugra.",
    [
        "Hiện thân của con cáo/chồn đen trên huy hiệu thành phố Surgut — biểu tượng nghề săn lông thú.",
        "Tượng đồng sống động, duyên dáng — điểm 'sống ảo' và 'linh vật' được người dân yêu thích.",
        "Nằm ngay cạnh khu văn hoá 'Stary Surgut', dễ kết hợp tham quan.",
    ],
    prac(
        "Không gian ngoài trời, mở cửa tự do 24/7.",
        "Miễn phí.",
        "10–20 phút.",
        "Đẹp quanh năm; hợp kết hợp khi thăm 'Stary Surgut'.",
        "Đi cùng lịch trình 'Stary Surgut'; chú ý chụp góc đẹp với bệ tượng.",
    ),
    [
        {"title": "Yandex Maps — Скульптура «Чёрный лис»", "url": "https://yandex.ru/maps/org/chyorny_lis/32063757346/"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Чёрный+лис+Сургут"},
    ],
    ["sculpture", "symbol", "fox", "coat-of-arms", "surgut"],
    maps_org("https://yandex.ru/maps/org/chyorny_lis/32063757346/", "Black Fox Sculpture", "Surgut"),
))

# ==================================== НИЖНЕВАРТОВСК ====================================

# 18) Памятник «Покорителям Самотлора» -----------------------------------------------
RECORDS.append(rec(
    "samotlor-conquerors-monument",
    "Tượng đài 'Những người chinh phục Samotlor' (Alyosha)",
    "Памятник «Покорителям Самотлора»",
    "Monument to the Conquerors of Samotlor",
    ["monument"],
    60.969234, 76.531523,
    "Lối vào thành phố Nizhnevartovsk (phía đường cao tốc), Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Tượng đài 'Những người chinh phục Samotlor' — người dân trìu mến gọi là 'Alyosha' — là biểu tượng của Nizhnevartovsk: một người thợ khoan dầu khổng lồ nâng cao ngọn đuốc/giọt dầu. Tượng tôn vinh những con người đã khai phá mỏ dầu Samotlor huyền thoại.",
    "Pamyatnik 'Pokoritelyam Samotlora' là tượng đài biểu tượng của thành phố Nizhnevartovsk, khánh thành năm 1978 và trở thành 'linh hồn' của đô thị dầu khí này. Bức tượng cao khoảng 22 m khắc hoạ hình ảnh một người thợ khoan dầu (nefteyanik) vạm vỡ, một tay giơ cao như nâng ngọn lửa/giọt dầu đầu tiên — hình ảnh anh hùng ca về những con người đã 'chinh phục' Samotlor, mỏ dầu khổng lồ được phát hiện năm 1965 và là một trong những mỏ lớn nhất thế giới, đưa Liên Xô lên hàng cường quốc dầu mỏ. Người dân trìu mến gọi tượng là 'Alyosha'. Đặt trên gò cao ngay cửa ngõ vào thành phố, tượng đài đón chào du khách và là nơi diễn ra các sự kiện, lễ kỷ niệm của thành phố; các cặp đôi cưới cũng thường tới đây chụp ảnh. Là tượng đài dầu khí nổi tiếng bậc nhất nước Nga, đây là điểm không thể bỏ qua để hiểu tinh thần và niềm tự hào của Yugra – 'trái tim dầu khí' của quốc gia.",
    [
        "Tượng người thợ khoan dầu cao ~22 m — biểu tượng của Nizhnevartovsk, gọi thân mật là 'Alyosha'.",
        "Tôn vinh những người khai phá mỏ dầu Samotlor huyền thoại (phát hiện 1965).",
        "Đặt trên gò cao cửa ngõ thành phố — nơi tổ chức sự kiện và điểm chụp ảnh biểu tượng.",
    ],
    prac(
        "Không gian ngoài trời, mở cửa tự do 24/7.",
        "Miễn phí.",
        "15–30 phút.",
        "Đẹp quanh năm; hoàng hôn và ban đêm khi có đèn chiếu cho ảnh ấn tượng.",
        "Nằm ở cửa ngõ thành phố, tiện dừng khi ra/vào; chú ý an toàn vì gần đường lớn.",
    ),
    [
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Покорителям+Самотлора+Нижневартовск"},
        {"title": "OpenStreetMap — Покорителям Самотлора", "url": "https://www.openstreetmap.org/node/5899405017"},
    ],
    ["monument", "oil", "samotlor", "symbol", "nizhnevartovsk"],
    maps_text("Памятник Покорителям Самотлора", "Нижневартовск", "Monument to the Conquerors of Samotlor", "Nizhnevartovsk", 60.969234, 76.531523),
))

# 19) Нижневартовский краеведческий музей им. Т. Д. Шуваева ---------------------------
RECORDS.append(rec(
    "nizhnevartovsk-shuvaev-museum",
    "Bảo tàng Địa phương học Nizhnevartovsk (mang tên T. D. Shuvaev)",
    "Нижневартовский краеведческий музей имени Т. Д. Шуваева",
    "Nizhnevartovsk Museum of Local Lore (T. D. Shuvaev)",
    ["museum"],
    60.940335, 76.561480,
    "Số 9/1 đường Lenina, thành phố Nizhnevartovsk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Bảo tàng Địa phương học Nizhnevartovsk mang tên nhà sưu tầm T. D. Shuvaev, lưu giữ lịch sử vùng đất từ thiên nhiên taiga, văn hoá Khanty bản địa đến kỷ nguyên khai phá mỏ dầu Samotlor. Đây là bảo tàng chủ đạo của thành phố dầu khí trẻ trung này.",
    "Nizhnevartovsky krayevedchesky muzey imeni T. D. Shuvaeva là bảo tàng tổng hợp chính của Nizhnevartovsk, mang tên Timofey Dmitrievich Shuvaev — người có công gây dựng bộ sưu tập ban đầu. Bảo tàng giới thiệu bức tranh nhiều mặt về vùng đất: thiên nhiên taiga và đầm lầy Tây Siberia; khảo cổ học và di sản của người Khanty bản địa với trang phục, đồ dùng, tín ngưỡng; và đặc biệt là câu chuyện phát hiện, khai phá mỏ dầu khổng lồ Samotlor giữa những năm 1960 đã khai sinh ra thành phố. Các không gian trưng bày kết hợp hiện vật gốc, mô hình và tư liệu, tái hiện đời sống của những người tiên phong đến vùng đầm lầy hoang vu dựng nên đô thị. Bảo tàng gồm nhiều bộ phận, trong đó có phòng trưng bày dân tộc học và lịch sử tự nhiên. Với vai trò 'ký ức của thành phố', đây là điểm đến giúp du khách hiểu Nizhnevartovsk đã ra đời và lớn lên cùng dòng dầu Samotlor như thế nào.",
    [
        "Bảo tàng chủ đạo của Nizhnevartovsk, mang tên nhà sưu tầm T. D. Shuvaev.",
        "Trưng bày về thiên nhiên taiga, khảo cổ và văn hoá Khanty bản địa.",
        "Kể câu chuyện khai phá mỏ dầu Samotlor đã khai sinh ra thành phố.",
    ],
    prac(
        "Thứ Ba–Chủ nhật, thường 10:00–18:00; nghỉ thứ Hai. Nên kiểm tra trước.",
        "Vé vào cửa khoảng 100–250 rúp; có ưu đãi cho các đối tượng.",
        "1–1,5 giờ.",
        "Quanh năm; điểm tham quan trong nhà lý tưởng cho ngày lạnh.",
        "Có tour thuyết minh; kết hợp cùng tượng đài 'Purители Самотлора' khi thăm thành phố.",
    ),
    [
        {"title": "Culture.ru — Нижневартовский краеведческий музей им. Т. Д. Шуваева", "url": "https://www.culture.ru/institutes/10538/nizhnevartovskii-kraevedcheskii-muzei-imeni-t-d-shuvaeva"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Нижневартовский+краеведческий+музей+Шуваева"},
    ],
    ["museum", "local-lore", "ethnography", "oil", "samotlor", "nizhnevartovsk"],
    maps_text("Нижневартовский краеведческий музей имени Шуваева", "Нижневартовск", "Nizhnevartovsk Museum of Local Lore", "Nizhnevartovsk", 60.940335, 76.561480),
))

# 20) Храм Рождества Христова (Нижневартовск) ----------------------------------------
RECORDS.append(rec(
    "nizhnevartovsk-nativity-church",
    "Nhà thờ Chúa Giáng Sinh Nizhnevartovsk",
    "Храм Рождества Христова (Нижневартовск)",
    "Church of the Nativity of Christ (Nizhnevartovsk)",
    ["church"],
    60.924928, 76.590871,
    "Số 68 đường 60 let Oktyabrya, thành phố Nizhnevartovsk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Nhà thờ Chúa Giáng Sinh là thánh đường Chính thống giáo chính của Nizhnevartovsk, với những vòm mái vàng và tháp chuông nổi bật. Đây là trung tâm tôn giáo và một trong những công trình kiến trúc đẹp của thành phố.",
    "Khram Rozhdestva Khristova (Nhà thờ Chúa Giáng Sinh) là ngôi thánh đường Chính thống giáo trung tâm của Nizhnevartovsk, được xây dựng trong thời kỳ thành phố phát triển mạnh. Công trình theo phong cách kiến trúc nhà thờ Nga cổ điển với khối chính bề thế, các vòm mái hình củ hành dát vàng và tháp chuông vươn cao, trở thành điểm nhấn tôn giáo giữa lòng đô thị dầu khí trẻ. Bên trong, nhà thờ được trang hoàng bằng bích hoạ, iconostas nhiều tầng và các biểu tượng thánh, tạo không gian trang nghiêm cho các buổi lễ. Ngoài chức năng thờ phụng, nhà thờ còn là trung tâm sinh hoạt cộng đồng với trường giáo lý Chủ nhật và các hoạt động thiện nguyện, văn hoá. Nằm ở khu vực dễ tiếp cận, đây là một trong những địa điểm được du khách ghé thăm để tìm hiểu đời sống tinh thần và kiến trúc tôn giáo của Nizhnevartovsk.",
    [
        "Thánh đường Chính thống giáo chính của Nizhnevartovsk với vòm mái vàng và tháp chuông cao.",
        "Kiến trúc nhà thờ Nga cổ điển, nội thất bích hoạ và iconostas nhiều tầng.",
        "Trung tâm tôn giáo – cộng đồng của thành phố với trường giáo lý và hoạt động thiện nguyện.",
    ],
    prac(
        "Mở cửa hằng ngày theo giờ lễ (thường khoảng 8:00–19:00); có thể thay đổi.",
        "Vào cửa tự do (miễn phí).",
        "20–40 phút.",
        "Quanh năm; các dịp lễ Chính thống giáo (đặc biệt Giáng Sinh) rất trang nghiêm.",
        "Trang phục kín đáo; phụ nữ nên trùm khăn; hạn chế chụp ảnh trong giờ lễ.",
    ),
    [
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Храм+Рождества+Христова+Нижневартовск"},
        {"title": "OpenStreetMap — Церковь Рождества Христова (Нижневартовск)", "url": "https://www.openstreetmap.org/way/175274824"},
    ],
    ["orthodox", "church", "gold-dome", "nizhnevartovsk"],
    maps_text("Храм Рождества Христова", "Нижневартовск", "Church of the Nativity", "Nizhnevartovsk", 60.924928, 76.590871),
))

# ==================================== КОГАЛЫМ (KOGALYM) ====================================

# 21) СОК «Галактика» -----------------------------------------------------------------
RECORDS.append(rec(
    "galaktika-aquapark-kogalym",
    "Tổ hợp giải trí 'Galaktika' — Công viên nước & Thuỷ cung",
    "Спортивно-оздоровительный комплекс «Галактика»",
    "Galaktika Entertainment Complex (Aquapark and Oceanarium)",
    ["other"],
    62.253183, 74.530745,
    "Số 60 đường Druzhby Narodov, thành phố Kogalym, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "'Galaktika' là tổ hợp giải trí – nghỉ dưỡng hoành tráng ở thành phố dầu khí Kogalym, gồm công viên nước trong nhà, thuỷ cung (oceanarium), khu 'rừng nhiệt đới' và nhiều tiện ích — một 'ốc đảo nhiệt đới' giữa vùng Bắc Siberia băng giá.",
    "Sportivno-ozdorovitelny kompleks 'Galaktika' là một trong những điểm giải trí trong nhà ấn tượng nhất miền Bắc nước Nga, mở cửa năm 2016 tại Kogalym — thành phố nhỏ nhưng giàu có nhờ dầu khí. Tổ hợp khổng lồ này gồm nhiều khu chức năng dưới một mái vòm: công viên nước (aquapark) với hệ thống cầu trượt, hồ tạo sóng, dòng sông lười; một thuỷ cung (oceanarium) trưng bày cá mập, cá đuối và hàng trăm loài sinh vật biển; khu 'rừng nhiệt đới' nhân tạo với cây xanh, thác nước và động vật; cùng khu spa, phòng tập, khu vui chơi trẻ em và nhà hàng. Điều khiến 'Galaktika' đặc biệt là sự tương phản kỳ thú: bên ngoài là mùa đông Siberia khắc nghiệt dài nhiều tháng, còn bên trong là bầu không khí nhiệt đới ấm áp quanh năm. Đây là điểm đến gia đình lý tưởng và là niềm tự hào của Kogalym, minh chứng cho việc các đô thị dầu khí phương Bắc đầu tư mạnh cho chất lượng sống. Với du khách, đó là trải nghiệm 'mùa hè nhiệt đới' bất ngờ giữa taiga.",
    [
        "Công viên nước trong nhà với cầu trượt, hồ tạo sóng và dòng sông lười.",
        "Thuỷ cung (oceanarium) với cá mập, cá đuối và khu 'rừng nhiệt đới' nhân tạo.",
        "'Ốc đảo nhiệt đới' ấm áp quanh năm giữa mùa đông Siberia — điểm đến gia đình lý tưởng.",
    ],
    prac(
        "Mở cửa hằng ngày (thường khoảng 10:00–22:00); giờ từng khu có thể khác nhau — nên xem trước.",
        "Vé vào cửa tính theo khu và thời lượng (thường vài trăm đến hơn nghìn rúp); có gói gia đình.",
        "Nửa ngày đến cả ngày.",
        "Quanh năm; đặc biệt hấp dẫn vào mùa đông để 'trốn' cái lạnh.",
        "Mang đồ bơi, dép; đặt vé trước vào cuối tuần/lễ; phù hợp cho gia đình có trẻ nhỏ.",
    ),
    [
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Галактика+Когалым"},
        {"title": "OpenStreetMap — СОК «Галактика» (Когалым)", "url": "https://www.openstreetmap.org/relation/10358145"},
    ],
    ["aquapark", "oceanarium", "family", "entertainment", "indoor", "kogalym"],
    maps_text("Спортивно-оздоровительный комплекс Галактика", "Когалым", "Galaktika Aquapark", "Kogalym", 62.253183, 74.530745),
))

# ==================================== НЕФТЕЮГАНСК ====================================

# 22) Церковь Святого Духа (Нефтеюганск) ---------------------------------------------
RECORDS.append(rec(
    "holy-spirit-church-nefteyugansk",
    "Nhà thờ Chúa Thánh Thần Nefteyugansk",
    "Церковь Святого Духа (Нефтеюганск)",
    "Church of the Holy Spirit (Nefteyugansk)",
    ["church"],
    61.084462, 72.611759,
    "Số 14 đường Gagarina, thành phố Nefteyugansk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Nhà thờ Chúa Thánh Thần là thánh đường Chính thống giáo chính của Nefteyugansk, với nhà thờ hạ (kèm nguyện đường Thánh Panteleimon) và những vòm mái vàng. Đây là trung tâm tôn giáo và điểm nhấn kiến trúc của thành phố dầu khí trên đảo giữa sông Ob.",
    "Tserkov Svyatogo Dukha (Nhà thờ Chúa Thánh Thần) là ngôi thánh đường Chính thống giáo trung tâm của Nefteyugansk — thành phố dầu khí nằm trên một hòn đảo giữa vùng ngập nước của sông Ob. Nhà thờ có cấu trúc gồm nhà thờ thượng và nhà thờ hạ (với nguyện đường kính Thánh Panteleimon – vị thánh chữa lành), mang phong cách kiến trúc Nga truyền thống với các vòm mái dát vàng và tháp chuông. Bên trong được trang hoàng bằng bích hoạ, iconostas và các biểu tượng thánh, tạo không gian trang nghiêm cho các buổi lễ và nghi thức. Ngoài chức năng thờ phụng, nhà thờ còn là nơi sinh hoạt cộng đồng với trường giáo lý và các hoạt động văn hoá – thiện nguyện, gắn bó mật thiết với đời sống người dân. Là công trình tôn giáo tiêu biểu nhất của Nefteyugansk, nhà thờ vừa là chốn hành hương của giáo dân, vừa là điểm tham quan cho du khách muốn khám phá đời sống tinh thần của các đô thị dầu khí Yugra.",
    [
        "Thánh đường Chính thống giáo chính của Nefteyugansk với nhà thờ thượng – hạ và vòm mái vàng.",
        "Nhà thờ hạ kính Thánh Panteleimon (thánh chữa lành); nội thất bích hoạ và iconostas.",
        "Trung tâm tôn giáo – cộng đồng của thành phố đảo giữa sông Ob.",
    ],
    prac(
        "Mở cửa hằng ngày theo giờ lễ (thường khoảng 8:00–19:00); có thể thay đổi.",
        "Vào cửa tự do (miễn phí).",
        "20–40 phút.",
        "Quanh năm; các dịp lễ Chính thống giáo rất trang nghiêm.",
        "Trang phục kín đáo; phụ nữ nên trùm khăn; hạn chế chụp ảnh trong giờ lễ.",
    ),
    [
        {"title": "Yandex Maps — Церковь Святого Духа (Нефтеюганск)", "url": "https://yandex.ru/maps/org/tserkov_svyatogo_dukha_s_nizhnim_khramom_panteleimona_tselitelya/15271453468/"},
        {"title": "Wikipedia (RU) — tìm kiếm", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Церковь+Святого+Духа+Нефтеюганск"},
    ],
    ["orthodox", "church", "gold-dome", "nefteyugansk"],
    maps_org("https://yandex.ru/maps/org/tserkov_svyatogo_dukha_s_nizhnim_khramom_panteleimona_tselitelya/15271453468/", "Church of the Holy Spirit", "Nefteyugansk"),
))

# 23) Музей реки Обь (Нефтеюганск) ----------------------------------------------------
RECORDS.append(rec(
    "ob-river-museum-nefteyugansk",
    "Bảo tàng Sông Ob (Nefteyugansk)",
    "Музей реки Обь (Нефтеюганск)",
    "Museum of the Ob River (Nefteyugansk)",
    ["museum"],
    61.097633, 72.618530,
    "Vi khu (mikrorayon) số 9, nhà 28, thành phố Nefteyugansk, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Bảo tàng Sông Ob là bảo tàng chủ đề độc đáo dành cho dòng sông lớn Ob — mạch sống của Nefteyugansk và cả vùng Yugra. Các trưng bày về thiên nhiên, hệ sinh thái sông nước, nghề cá và văn hoá bản địa giúp du khách hiểu mối gắn bó giữa con người và dòng sông.",
    "Muzey reki Ob (Bảo tàng Sông Ob) ở Nefteyugansk là một bảo tàng chuyên đề thú vị, lấy chính dòng sông Ob — một trong những con sông dài nhất thế giới — làm nhân vật trung tâm. Nằm trên một hòn đảo giữa vùng ngập nước của sông, thành phố Nefteyugansk gắn bó mật thiết với dòng nước, và bảo tàng kể câu chuyện ấy qua nhiều chủ đề: hệ sinh thái sông và đầm lầy Tây Siberia, các loài cá và động vật hoang dã, nghề đánh cá truyền thống, giao thông đường thuỷ, cùng đời sống và tín ngưỡng của người Khanty bản địa vốn xem sông nước là thiêng liêng. Bộ sưu tập kết hợp mẫu vật tự nhiên, hiện vật dân tộc học, mô hình tàu thuyền và các trưng bày tương tác, phù hợp cho cả gia đình. Đây là một điểm đến giàu tính giáo dục, mang đến góc nhìn khác lạ và gần gũi về vùng đất Yugra thông qua lăng kính của dòng sông đã nuôi dưỡng nó.",
    [
        "Bảo tàng chuyên đề độc đáo về sông Ob — 'mạch sống' của Nefteyugansk và Yugra.",
        "Trưng bày về hệ sinh thái sông, các loài cá, nghề đánh cá và giao thông đường thuỷ.",
        "Hiện vật dân tộc học Khanty và các trưng bày tương tác phù hợp cho gia đình.",
    ],
    prac(
        "Thứ Ba–Chủ nhật, thường 10:00–18:00; nghỉ thứ Hai. Nên kiểm tra trước.",
        "Vé vào cửa khoảng 100–200 rúp; có ưu đãi cho các đối tượng.",
        "45 phút – 1 giờ.",
        "Quanh năm; điểm tham quan trong nhà lý tưởng cho ngày lạnh.",
        "Có tour thuyết minh; hợp cho gia đình có trẻ nhỏ với các trưng bày tương tác.",
    ),
    [
        {"title": "Culture.ru — Музей реки Обь (Нефтеюганск)", "url": "https://www.culture.ru/institutes/10555/muzei-reki-ob"},
        {"title": "OpenStreetMap — Музей реки Обь", "url": "https://www.openstreetmap.org/node/4006780834"},
    ],
    ["museum", "river", "ob", "nature", "ethnography", "nefteyugansk"],
    maps_text("Музей реки Обь", "Нефтеюганск", "Museum of the Ob River", "Nefteyugansk", 61.097633, 72.618530),
))

# ==================================== KHU BẢO TỒN THIÊN NHIÊN ====================================

# 24) Заповедник «Малая Сосьва» ------------------------------------------------------
RECORDS.append(rec(
    "malaya-sosva-reserve",
    "Khu bảo tồn thiên nhiên Malaya Sosva",
    "Государственный природный заповедник «Малая Сосьва»",
    "Malaya Sosva Nature Reserve",
    ["park_garden"],
    62.082778, 64.096389,
    "Lưu vực sông Malaya Sosva, quận Sovetsky và Beryozovsky; văn phòng tại số 46 đường Lenina, thành phố Sovetsky, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Malaya Sosva là khu bảo tồn thiên nhiên nghiêm ngặt (zapovednik) nổi tiếng của Yugra, kế thừa khu bảo tồn hải ly – chồn zibelin đầu tiên của vùng. Rộng hơn 225.000 ha rừng taiga nguyên sinh, nơi đây là 'ngôi nhà' của hải ly Tây Siberia quý hiếm và hệ động thực vật phương Bắc phong phú.",
    "Gosudarstvenny prirodny zapovednik 'Malaya Sosva' im. V. V. Raevskogo là khu bảo tồn thiên nhiên nghiêm ngặt nằm trong thung lũng sông Malaya Sosva, trên địa bàn các quận Sovetsky và Beryozovsky. Thành lập năm 1976 trên diện tích khoảng 225.562 ha, khu bảo tồn là hậu thân của Kondo-Sosvinsky — một trong những zapovednik đầu tiên của Nga (từ 1929), vốn được lập để bảo vệ và phục hồi hải ly cùng chồn zibelin của taiga Tây Siberia. Đây là vương quốc của rừng taiga nguyên sinh với thông tuyết (kedr), vân sam, linh sam, xen kẽ những đầm lầy sphagnum rộng lớn. Hệ sinh vật rất phong phú: hơn 400 loài thực vật có mạch, 40 loài thú (gấu nâu, chồn zibelin, chồn ecmin, nai sừng tấm...), hơn 200 loài chim, cùng quần thể hải ly Tây Siberia quý hiếm được ghi trong Sách Đỏ. Là khu bảo tồn nghiêm ngặt, phần lõi không mở cho du lịch tự do, nhưng có bảo tàng thiên nhiên và các tuyến giáo dục sinh thái có kiểm soát tại văn phòng ở thành phố Sovetsky. Malaya Sosva là biểu tượng cho nỗ lực gìn giữ thiên nhiên hoang dã của Yugra.",
    [
        "Khu bảo tồn nghiêm ngặt rộng hơn 225.000 ha, hậu thân của một trong những zapovednik đầu tiên của Nga (1929).",
        "Rừng taiga nguyên sinh (thông tuyết kedr, vân sam) và đầm lầy — nơi cư trú của hải ly Tây Siberia quý hiếm.",
        "Hơn 400 loài thực vật, 40 loài thú và hơn 200 loài chim; có bảo tàng thiên nhiên tại Sovetsky.",
    ],
    prac(
        "Phần lõi là khu bảo tồn nghiêm ngặt, KHÔNG vào tự do; tham quan qua bảo tàng và tuyến sinh thái có tổ chức. Liên hệ ban quản lý trước.",
        "Bảo tàng và tour sinh thái có thu phí/theo đăng ký; cần giấy phép để vào các tuyến.",
        "Từ nửa ngày (bảo tàng/tuyến gần) trở lên.",
        "Cuối xuân đến đầu thu cho tuyến sinh thái; mùa đông khắc nghiệt và hạn chế tiếp cận.",
        "Đăng ký trước với ban quản lý; đi cùng hướng dẫn viên; mang chống muỗi/côn trùng và trang bị phù hợp taiga.",
    ),
    [
        {"title": "Wikipedia (RU) — Малая Сосьва (заповедник)", "url": "https://ru.wikipedia.org/wiki/Малая_Сосьва_(заповедник)"},
        {"title": "Trang chính thức — Заповедник «Малая Сосьва»", "url": "https://m-sosva.ru/"},
    ],
    ["nature-reserve", "zapovednik", "taiga", "beaver", "wildlife", "yugra"],
    maps_text("Заповедник Малая Сосьва", "Советский, Югра", "Malaya Sosva Nature Reserve", "Yugra", 62.082778, 64.096389),
))

# 25) Юганский заповедник ------------------------------------------------------------
RECORDS.append(rec(
    "yugansky-nature-reserve",
    "Khu bảo tồn thiên nhiên Yugansky",
    "Юганский государственный природный заповедник",
    "Yugansky Nature Reserve",
    ["park_garden"],
    59.655833, 74.630000,
    "Vùng giữa hai sông Negusyakh và Maly Yugan, quận Surgut; trụ sở trung tâm tại làng Ugut, Khu tự trị Khanty-Mansi – Yugra, Nga.",
    "Yugansky là một trong những khu bảo tồn thiên nhiên nghiêm ngặt lớn nhất châu Âu và Nga, rộng gần 650.000 ha rừng taiga và đầm lầy nguyên sơ ở lưu vực sông Bolshoy Yugan. Đây là 'lá phổi' hoang dã bảo tồn hệ sinh thái trung taiga Tây Siberia gần như nguyên vẹn.",
    "Yugansky gosudarstvenny prirodny zapovednik là khu bảo tồn thiên nhiên nghiêm ngặt được thành lập năm 1982 tại quận Surgut, nằm giữa hai con sông Negusyakh và Maly Yugan (các nhánh của Bolshoy Yugan, phụ lưu tả ngạn sông Ob). Với diện tích khoảng 648.700 ha, đây là một trong những zapovednik lớn nhất phần châu Âu – Tây Siberia của nước Nga, được lập nhằm bảo tồn nguyên vẹn hệ sinh thái trung taiga vùng Trung Priobye. Cảnh quan chủ đạo là rừng vân sam – thông tuyết (kedr) trên các gờ đất thoát nước tốt, xen kẽ những đầm lầy oligotrophic lồi rộng mênh mông — hai kiểu hệ sinh thái đan xen đặc trưng của Tây Siberia. Hệ sinh vật gồm khoảng 320 loài thực vật có mạch, 40 loài thú (gấu, linh miêu, chồn gulô, nai sừng tấm, tuần lộc rừng...) và hơn 200 loài chim; nhiều loài quý hiếm trong Sách Đỏ được ghi nhận. Trụ sở trung tâm đặt tại làng Ugut, nơi có bảo tàng và các chương trình giáo dục sinh thái. Là khu bảo tồn nghiêm ngặt, phần lõi không mở cho du lịch đại chúng, nhưng Yugansky là niềm tự hào và biểu tượng cho thiên nhiên hoang dã nguyên sơ của Yugra.",
    [
        "Một trong những khu bảo tồn nghiêm ngặt lớn nhất Nga — gần 650.000 ha taiga và đầm lầy nguyên sơ.",
        "Bảo tồn hệ sinh thái trung taiga Tây Siberia với rừng vân sam – thông tuyết và đầm lầy lồi mênh mông.",
        "Khoảng 320 loài thực vật, 40 loài thú và hơn 200 loài chim; trụ sở và bảo tàng tại làng Ugut.",
    ],
    prac(
        "Phần lõi là khu bảo tồn nghiêm ngặt, KHÔNG vào tự do; tham quan qua bảo tàng và tuyến sinh thái có tổ chức tại Ugut. Liên hệ ban quản lý trước.",
        "Tour và bảo tàng có thu phí/theo đăng ký; cần giấy phép để vào các tuyến.",
        "Từ nửa ngày (tại Ugut) trở lên; các tuyến sâu cần nhiều thời gian và chuẩn bị.",
        "Cuối xuân đến đầu thu; mùa hè nhiều muỗi, mùa đông khắc nghiệt và khó tiếp cận.",
        "Đăng ký trước; đi cùng kiểm lâm/hướng dẫn viên; mang chống côn trùng và trang bị dã ngoại taiga.",
    ),
    [
        {"title": "Wikipedia (RU) — Юганский заповедник", "url": "https://ru.wikipedia.org/wiki/Юганский_заповедник"},
        {"title": "Trang chính thức — Юганский заповедник", "url": "https://ugansky.ru/"},
    ],
    ["nature-reserve", "zapovednik", "taiga", "wildlife", "wetland", "yugra"],
    maps_text("Юганский заповедник", "Угут, Югра", "Yugansky Nature Reserve", "Yugra", 59.655833, 74.630000),
))


def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    existing_slugs = {p.get("slug") for p in data}
    existing_ids = {p.get("id") for p in data}

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
