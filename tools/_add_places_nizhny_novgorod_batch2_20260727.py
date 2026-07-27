# -*- coding: utf-8 -*-
"""_add_places_nizhny_novgorod_batch2_20260727.py — VÙNG TIÊU ĐIỂM: Tỉnh Nizhny Novgorod
(lần chạy tự động 2026-07-27, đợt 2).

Bối cảnh: nizhny-novgorod.json hiện có 28 địa điểm (sau đợt 1). Tatarstan đã đạt 60 (≥50)
=> vùng tiêu điểm vẫn là Nizhny Novgorod (đầu danh sách ưu tiên còn <50). Nâng dần tới ~50–100.

Đợt này bổ sung 17 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình:
- Tu viện/nhà thờ: Благовещенский монастырь (1221), Спасский Староярмарочный собор (Montferrand),
  Спасо-Преображенский собор в Сормове, Свято-Троицкий Островоезерский монастырь (Ворсма, trên đảo).
- Bảo tàng: Музей А. Д. Сахарова, Музей истории ГАЗ.
- Quảng trường/bờ sông: площадь Минина и Пожарского, набережная Фёдоровского.
- Công viên/thiên nhiên: Александровский сад, парк «Швейцария», Ичалковский бор (hang karst),
  Керженский заповедник (biosphere), озеро Ключик/Голубое озеро.
- Vườn thú: «Лимпопо». Cầu: Канавинский мост. Thị trấn cổ/thủ công: Павлово, Балахна.

TOẠ ĐỘ: xác minh chéo ru.wikipedia, sobory.ru (nhà thờ/tu viện — Островоезерский 55.990277,43.293688),
Wikidata (Sakharov Q4306042), trang tổ chức Yandex Maps (org id), 2GIS — 2026-07.
Kiểm tra thứ tự & phạm vi (tỉnh NN: lat ~54,5–58,1; lon ~41,5–47,0; KHÔNG đảo lat/lon; đều nằm
trong tỉnh). Link bản đồ TRỎ-ĐỊA-ĐIỂM: ưu tiên URL trang tổ chức Yandex khi tra được; còn lại
dùng text-search theo tên_ru + thành phố, canh giữa theo toạ độ đã kiểm.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_nizhny_novgorod_batch2_20260727.py
       python3 tools/normalize_categories.py && python3 tools/build.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"

REGION = "nizhny-novgorod"
REGION_NAME_VI = "Tỉnh Nizhny Novgorod"
FD = "Vùng Volga"


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
        "rating": None,
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

# 1) Благовещенский монастырь -------------------------------------------------
RECORDS.append(rec(
    "blagoveshchensky-monastery",
    "Tu viện Truyền Tin (Blagoveshchensky monastyr)",
    "Благовещенский монастырь",
    "Annunciation Monastery",
    ["church", "monument"],
    56.323218, 43.977365,
    "Ngõ Melnichny (Мельничный переулок) số 1, bên bờ dốc phải sông Oka, thành phố Nizhny Novgorod, Nga.",
    "Tu viện Truyền Tin là một trong những tu viện lâu đời nhất Nizhny Novgorod, tương truyền được lập từ năm 1221 cùng thời điểm khai sinh thành phố. Quần thể nhà thờ đá trắng nằm trên sườn dốc cao bên sông Oka, nổi bật với nhà thờ chính toà Truyền Tin thế kỷ 17.",
    "Nép mình trên triền dốc cao ở hữu ngạn sông Oka, gần nơi con sông đổ vào Volga, Tu viện Truyền Tin gắn liền với chính buổi bình minh của Nizhny Novgorod. Theo truyền thống, tu viện được đại công tước Georgy Vsevolodovich – người sáng lập thành phố – cùng giám mục Simon cho lập năm 1221. Trải qua binh lửa và tàn phá, tu viện được hồi sinh vào nửa sau thế kỷ 14 nhờ công của thánh Aleksy, đô thành giáo chủ Moskva. Quần thể hiện nay chủ yếu hình thành trong thế kỷ 17, khi nhiều nhà thờ đá trắng được dựng lên: trung tâm là nhà thờ chính toà Truyền Tin năm cột năm vòm, cùng các nhà thờ Dòng Uspenskaya, Sergiy Radonezhsky và Aleksy. Thời Xô viết, tu viện bị đóng cửa và các toà nhà dùng cho mục đích khác, trong đó từng có cả một xưởng làm dụng cụ thiên văn – khí tượng. Từ thập niên 1990, tu viện được trả lại cho Giáo hội và trùng tu, trở lại là tu viện nam đang hoạt động. Ngày nay du khách tới đây vừa để chiêm ngưỡng cụm kiến trúc cổ kính bậc nhất thành phố, vừa để ngắm khung cảnh sông Oka mở ra bên dưới.",
    [
        "Một trong những tu viện cổ nhất Nizhny Novgorod, tương truyền lập từ năm 1221 cùng lúc khai sinh thành phố.",
        "Quần thể nhà thờ đá trắng thế kỷ 17 với nhà thờ chính toà Truyền Tin làm trung tâm.",
        "Vị trí tuyệt đẹp trên sườn dốc cao bên bờ sông Oka.",
    ],
    {
        "hours_vi": "Mở cửa cho khách hành hương và tham quan hằng ngày, thường khoảng 7:00–19:00 theo lịch tu viện.",
        "ticket_vi": "Vào tham quan tự do (miễn phí); hoan nghênh quyên góp tuỳ tâm.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; buổi sáng hoặc chiều muộn ánh sáng đẹp trên tường đá trắng.",
        "tips_vi": "Ăn mặc kín đáo; kết hợp đi bộ ra bờ sông Oka và cầu Kanavinsky gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Благовещенский монастырь (Нижний Новгород)", "url": "https://ru.wikipedia.org/wiki/%D0%91%D0%BB%D0%B0%D0%B3%D0%BE%D0%B2%D0%B5%D1%89%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%BE%D0%BD%D0%B0%D1%81%D1%82%D1%8B%D1%80%D1%8C_(%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4)"},
        {"title": "sobory.ru — Нижний Новгород, Благовещенский монастырь", "url": "https://sobory.ru/article/?object=00566"},
    ],
    ["monastery", "church", "history", "architecture", "oka"],
    maps_text("Благовещенский монастырь", "Нижний Новгород", "Annunciation Monastery", "Nizhny Novgorod", 56.323218, 43.977365),
    official_site="https://blagomm.ru",
))

# 2) Спасский Староярмарочный собор -------------------------------------------
RECORDS.append(rec(
    "spassky-old-fair-cathedral",
    "Nhà thờ chính toà Spassky Cũ của Hội chợ (Spassky Staroyarmarochny sobor)",
    "Спасский Староярмарочный собор",
    "Spassky Old Fair Cathedral",
    ["church", "monument"],
    56.331373, 43.954006,
    "Lối Yarmarochny (Ярмарочный проезд) số 10, khu Kanavino (khu vực Hội chợ), thành phố Nizhny Novgorod, Nga.",
    "Nhà thờ chính toà Spassky Cũ của Hội chợ là công trình cổ điển tráng lệ do kiến trúc sư lừng danh Auguste de Montferrand thiết kế, hoàn tất năm 1822. Với mái vòm lớn và hàng cột uy nghi, nhà thờ từng là trung tâm tinh thần của Hội chợ Nizhny Novgorod trứ danh.",
    "Dựng lên giữa khu Hội chợ Nizhny Novgorod sầm uất một thời, nhà thờ chính toà Spassky – quen gọi là 'nhà thờ Cũ của Hội chợ' để phân biệt với nhà thờ Aleksandr Nevsky 'Mới' xây sau – là một trong những công trình tân cổ điển đẹp nhất thành phố. Nhà thờ do Auguste de Montferrand, chính là kiến trúc sư của nhà thờ chính toà Thánh Isaac ở Sankt-Peterburg, thiết kế và hoàn thành vào năm 1822. Bố cục cân đối với mái vòm trung tâm bề thế đặt trên tang trống, bốn mặt là các hàng cột portico theo tinh thần cổ điển cao, gợi nhớ phong cách của thời đại. Đây từng là nơi thương nhân khắp nước Nga và nước ngoài tề tựu cầu nguyện trong những mùa hội chợ nhộn nhịp bậc nhất châu Âu thế kỷ 19. Nội thất được trang trí lộng lẫy dưới vòm cao tràn ngập ánh sáng. Sau thời gian bị đóng cửa và xuống cấp dưới thời Xô viết, nhà thờ đã được trùng tu và trả lại chức năng tôn giáo, đứng đó như một chứng nhân cho thời hoàng kim thương mại của thành phố.",
    [
        "Kiệt tác tân cổ điển do Auguste de Montferrand – tác giả nhà thờ Thánh Isaac – thiết kế, hoàn thành 1822.",
        "Trung tâm tinh thần của Hội chợ Nizhny Novgorod nổi tiếng thế kỷ 19.",
        "Mái vòm bề thế trên tang trống cùng các hàng cột portico cân đối bốn mặt.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày cho khách hành lễ và tham quan, thường khoảng 8:00–19:00.",
        "ticket_vi": "Vào tự do (miễn phí).",
        "duration_vi": "Khoảng 30–40 phút.",
        "best_time_vi": "Quanh năm; kết hợp khi tham quan cung Hội chợ và nhà thờ Aleksandr Nevsky gần đó.",
        "tips_vi": "Ăn mặc kín đáo khi vào; đi bộ vài phút là tới Cung Hội chợ (Yarmarka).",
    },
    [
        {"title": "Wikipedia (RU) — Спасский Староярмарочный собор", "url": "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B0%D1%81%D1%81%D0%BA%D0%B8%D0%B9_%D0%A1%D1%82%D0%B0%D1%80%D0%BE%D1%8F%D1%80%D0%BC%D0%B0%D1%80%D0%BE%D1%87%D0%BD%D1%8B%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80"},
        {"title": "Нижегородская митрополия — Спасский Староярмарочный собор", "url": "https://nne.ru/objects/spasskij-staroyarmarochnyj-sobor/"},
    ],
    ["cathedral", "church", "montferrand", "classicism", "fair"],
    maps_text("Спасский Староярмарочный собор", "Нижний Новгород", "Spassky Old Fair Cathedral", "Nizhny Novgorod", 56.331373, 43.954006),
))

# 3) Спасо-Преображенский собор в Сормове -------------------------------------
RECORDS.append(rec(
    "sormovo-transfiguration-cathedral",
    "Nhà thờ chính toà Chúa Biến Hình ở Sormovo (Spaso-Preobrazhensky sobor)",
    "Спасо-Преображенский собор (Сормово)",
    "Sormovo Transfiguration Cathedral",
    ["church"],
    56.350094, 43.872068,
    "Phố Shcherbakova (улица Щербакова) số 13а, quận Sormovsky, thành phố Nizhny Novgorod, Nga.",
    "Nhà thờ chính toà Chúa Biến Hình ở Sormovo là một trong những thánh đường đồ sộ và đẹp nhất Nizhny Novgorod, xây dựng năm 1900–1905 bằng kinh phí đóng góp của công nhân nhà máy Sormovo. Công trình theo phong cách tân Byzantine với mái vòm lớn và tháp chuông cao.",
    "Sừng sững ở quận công nghiệp Sormovo phía tây bắc thành phố, nhà thờ chính toà Chúa Biến Hình là niềm tự hào của cộng đồng thợ thuyền nhà máy đóng tàu và cơ khí Sormovo lừng danh. Nhà thờ được khởi công đặt móng long trọng năm 1900 và khánh thành năm 1905, xây bằng tiền quyên góp của chính công nhân nhà máy cùng ban giám đốc. Kiến trúc theo phong cách tân Byzantine (Nga – Byzantine) với khối trung tâm bề thế đội mái vòm lớn, bao quanh là các vòm phụ, cùng tháp chuông vươn cao. Không gian bên trong rộng thoáng, có thể chứa hàng nghìn giáo dân, gợi liên tưởng tới các thánh đường lớn cùng thời. Dưới thời Xô viết nhà thờ bị đóng cửa và dùng làm kho, nhưng may mắn không bị phá dỡ; sau này được trả lại và trùng tu, trở thành một trong những nhà thờ trung tâm của thành phố. Với quy mô và vẻ bề thế, đây là điểm đến đáng ghé khi khám phá phần phía bắc Nizhny Novgorod, ngay gần ga tàu điện ngầm Burevestnik.",
    [
        "Thánh đường tân Byzantine đồ sộ xây 1900–1905 bằng tiền quyên góp của công nhân nhà máy Sormovo.",
        "Mái vòm trung tâm lớn cùng tháp chuông cao, sức chứa hàng nghìn người.",
        "Sống sót qua thời Xô viết, nay là một trong những nhà thờ trung tâm của thành phố.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày, thường khoảng 7:30–19:00 (cuối tuần mở sớm hơn).",
        "ticket_vi": "Vào tự do (miễn phí).",
        "duration_vi": "Khoảng 30–40 phút.",
        "best_time_vi": "Quanh năm; đẹp khi nắng chiếu lên mái vòm.",
        "tips_vi": "Đi tàu điện ngầm tới ga Burevestnik rồi đi bộ; ăn mặc kín đáo khi vào.",
    },
    [
        {"title": "sobory.ru — Нижний Новгород, Собор Спаса Преображения в Сормове", "url": "https://sobory.ru/article/?object=01786"},
        {"title": "Нижегородская митрополия — Спасо-Преображенский собор", "url": "https://nne.ru/objects/spaso-preobrazhenskij-sobor/"},
    ],
    ["cathedral", "church", "neo-byzantine", "sormovo", "architecture"],
    maps_text("Спасо-Преображенский собор", "Нижний Новгород Сормово", "Sormovo Transfiguration Cathedral", "Nizhny Novgorod", 56.350094, 43.872068),
))

# 4) Музей А. Д. Сахарова -----------------------------------------------------
RECORDS.append(rec(
    "sakharov-museum-nn",
    "Bảo tàng - căn hộ Viện sĩ Andrei Sakharov (Muzey A. D. Sakharova)",
    "Музей А. Д. Сахарова",
    "Sakharov Museum (Apartment Museum)",
    ["museum"],
    56.232366, 43.950358,
    "Đại lộ Gagarin (проспект Гагарина) số 214, khu Shcherbinki, quận Prioksky, thành phố Nizhny Novgorod, Nga.",
    "Bảo tàng - căn hộ Andrei Sakharov nằm trong chính căn hộ nơi nhà vật lý đoạt giải Nobel Hoà bình sống những năm bị quản thúc ở thành phố Gorky (1980–1986). Bảo tàng mở cửa năm 1991, lưu giữ đồ đạc và tư liệu về cuộc đời và cuộc đấu tranh vì nhân quyền của ông.",
    "Nằm ở tầng trệt một chung cư mười hai tầng trên đại lộ Gagarin, khu Shcherbinki, đây là căn hộ nơi viện sĩ Andrei Sakharov – 'cha đẻ bom khinh khí' của Liên Xô đồng thời là nhà hoạt động nhân quyền đoạt giải Nobel Hoà bình – bị đưa đi quản thúc từ năm 1980 đến 1986. Khi ấy Nizhny Novgorod còn mang tên Gorky và là thành phố 'đóng' với người nước ngoài; Sakharov bị lưu đày tại đây vì phản đối cuộc chiến ở Afghanistan và lên tiếng đòi các quyền tự do. Bảo tàng mở cửa năm 1991, ngay sau khi ông qua đời, tái hiện gần như nguyên vẹn không gian sống khiêm nhường: bàn viết, sách vở, đồ đạc thường nhật, cùng các tư liệu, ảnh và hiện vật kể lại quãng đời khoa học lẫn hành trình bảo vệ nhân quyền của ông. Đây là một điểm đến giàu ý nghĩa lịch sử, cho thấy một lát cắt của thời kỳ Xô viết và câu chuyện về lương tri của một nhà khoa học.",
    [
        "Căn hộ nơi viện sĩ Andrei Sakharov bị quản thúc tại Gorky (1980–1986).",
        "Không gian sống được giữ gần như nguyên vẹn cùng tư liệu về cuộc đời và hoạt động nhân quyền của ông.",
        "Mở cửa năm 1991, một điểm đến giàu ý nghĩa lịch sử thời Xô viết.",
    ],
    {
        "hours_vi": "Thường mở 10:00–17:00; nghỉ thứ Sáu (nên kiểm tra lịch trước khi đến).",
        "ticket_vi": "Vé vào cửa giá phổ thông, mức thấp; có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm; nằm khá xa trung tâm nên tính thời gian di chuyển.",
        "tips_vi": "Đi tàu điện ngầm/ xe buýt về hướng Shcherbinki; nên gọi trước để xác nhận giờ mở.",
    },
    [
        {"title": "Wikipedia (RU) — Музей-квартира А. Д. Сахарова (Нижний Новгород)", "url": "https://ru.wikipedia.org/wiki/%D0%9C%D1%83%D0%B7%D0%B5%D0%B9-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D0%B0_%D0%90._%D0%94._%D0%A1%D0%B0%D1%85%D0%B0%D1%80%D0%BE%D0%B2%D0%B0_(%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4)"},
        {"title": "Culture.ru — Музей А.Д. Сахарова", "url": "https://www.culture.ru/institutes/10880/muzei-a-d-sakharova"},
    ],
    ["museum", "sakharov", "history", "soviet", "human-rights"],
    maps_text("Музей А. Д. Сахарова", "Нижний Новгород", "Sakharov Museum", "Nizhny Novgorod", 56.232366, 43.950358),
))

# 5) Музей истории ГАЗ --------------------------------------------------------
RECORDS.append(rec(
    "gaz-history-museum",
    "Bảo tàng lịch sử nhà máy ô tô GAZ (Muzey istorii GAZ)",
    "Музей истории ГАЗ",
    "GAZ History Museum",
    ["museum"],
    56.25098, 43.88926,
    "Đại lộ Lenin (проспект Ленина) số 95, quận Avtozavodsky, thành phố Nizhny Novgorod, Nga.",
    "Bảo tàng lịch sử nhà máy ô tô Gorky (GAZ) trưng bày bộ sưu tập xe hơi độc đáo, kể lại gần một thế kỷ ngành công nghiệp ô tô Nga. Nơi đây có nhiều mẫu xe huyền thoại như Volga, Chaika cùng các dòng xe quân sự.",
    "Đặt tại quận Avtozavodsky – 'thành phố ô tô' hình thành quanh nhà máy GAZ khổng lồ, Bảo tàng lịch sử GAZ là điểm hẹn của những người mê xe và tò mò về công nghiệp Xô viết. Nhà máy ô tô Gorky ra đời đầu thập niên 1930 với sự hỗ trợ kỹ thuật ban đầu từ Ford, và từ đó cho ra đời nhiều dòng xe gắn liền với lịch sử nước Nga. Bảo tàng bố trí trên hai tầng của Trung tâm đào tạo GAZ: một khu giới thiệu lịch sử và sự phát triển của nhà máy, khu còn lại là triển lãm 'Những chiếc xe và người tạo ra chúng' với dàn xe nguyên bản được gìn giữ cẩn thận. Khách tham quan có thể ngắm những mẫu xe biểu tượng như limousine Chaika, sedan Volga sang trọng, xe tải, cùng các xe quân sự và mẫu thử hiếm gặp. Đây là cách sinh động để hiểu về một trong những trụ cột công nghiệp của Nizhny Novgorod.",
    [
        "Bộ sưu tập xe hơi phong phú của nhà máy ô tô Gorky (GAZ) huyền thoại.",
        "Nhiều mẫu xe biểu tượng: limousine Chaika, sedan Volga, xe tải và xe quân sự.",
        "Kể lại gần một thế kỷ công nghiệp ô tô gắn với quận Avtozavodsky.",
    ],
    {
        "hours_vi": "Thứ Hai–Năm 9:00–18:00, thứ Sáu 9:00–17:00, thứ Bảy 9:00–16:00; Chủ nhật nghỉ.",
        "ticket_vi": "Vé vào cửa mức phổ thông; có thể đặt tour hướng dẫn.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm; nằm ở quận Avtozavodsky phía nam, tính thời gian di chuyển.",
        "tips_vi": "Đi tàu điện ngầm tới các ga khu Avtozavod; nên kiểm tra lịch mở cửa trước khi đến.",
    },
    [
        {"title": "Culture.ru — Музей истории ГАЗ", "url": "https://www.culture.ru/institutes/4662/muzei-istorii-gaz"},
        {"title": "Yandex Maps — Музей истории ГАЗ (просп. Ленина, 95)", "url": "https://yandex.ru/maps/org/muzey_istorii_gaz/1085889766/"},
    ],
    ["museum", "cars", "gaz", "industry", "avtozavod"],
    maps_org("https://yandex.ru/maps/org/muzey_istorii_gaz/1085889766/", "GAZ History Museum", "Nizhny Novgorod"),
))

# 6) Площадь Минина и Пожарского ----------------------------------------------
RECORDS.append(rec(
    "minin-pozharsky-square",
    "Quảng trường Minin và Pozharsky (ploshchad Minina i Pozharskogo)",
    "Площадь Минина и Пожарского",
    "Minin and Pozharsky Square",
    ["square_street", "monument"],
    56.327436, 44.006948,
    "Trung tâm lịch sử, ngay cạnh mặt đông nam của Kremlin, quận Nizhegorodsky, thành phố Nizhny Novgorod, Nga.",
    "Quảng trường Minin và Pozharsky là quảng trường chính và trái tim đô thị của Nizhny Novgorod, trải rộng ngay bên chân đồi của Kremlin. Đây là nơi diễn ra các lễ hội, sự kiện lớn và điểm khởi đầu lý tưởng để khám phá thành phố.",
    "Mang tên hai người anh hùng dân tộc Kuzma Minin và công tước Dmitry Pozharsky – những người đã tập hợp đội dân binh tại chính Nizhny Novgorod để giải phóng Moskva năm 1612 – quảng trường này là không gian công cộng quan trọng nhất của thành phố. Nằm ở phần cao (nagornaya) của trung tâm lịch sử, ngay sát mặt đông nam của Kremlin, quảng trường được bao quanh bởi nhiều công trình biểu tượng: Bảo tàng Mỹ thuật bang, các toà nhà thế kỷ 19 của trường đại học sư phạm, Cung Lao động, tháp Kladovaya của Kremlin. Từ đây, phố đi bộ Bolshaya Pokrovskaya và các tuyến bờ sông toả ra bốn phía, biến quảng trường thành điểm giao và điểm hẹn quen thuộc. Vào các dịp lễ lớn, ngày thành phố hay đêm giao thừa, nơi đây trở thành sân khấu ngoài trời rộn ràng với hàng nghìn người. Ngày thường, quảng trường vẫn là chốn dạo bộ, ngắm phố và chụp ảnh lý tưởng.",
    [
        "Quảng trường chính, trái tim đô thị của Nizhny Novgorod, ngay cạnh Kremlin.",
        "Mang tên Minin và Pozharsky – những người khởi xướng đội dân binh giải phóng Moskva năm 1612.",
        "Điểm khởi đầu của phố đi bộ Bolshaya Pokrovskaya và các tuyến bờ sông.",
    ],
    {
        "hours_vi": "Không gian mở, tham quan tự do suốt cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–40 phút dạo quanh; lâu hơn nếu vào các bảo tàng lân cận.",
        "best_time_vi": "Chiều muộn và buổi tối khi lên đèn; đặc biệt sôi động vào các dịp lễ.",
        "tips_vi": "Dùng làm điểm xuất phát: từ đây đi bộ vào Kremlin, xuống Cầu thang Chkalov hoặc dọc phố Pokrovskaya.",
    },
    [
        {"title": "Wikipedia (RU) — Площадь Минина и Пожарского", "url": "https://ru.wikipedia.org/wiki/%D0%9F%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D1%8C_%D0%9C%D0%B8%D0%BD%D0%B8%D0%BD%D0%B0_%D0%B8_%D0%9F%D0%BE%D0%B6%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B3%D0%BE"},
        {"title": "Yandex Maps — Площадь Минина и Пожарского", "url": "https://yandex.com/maps/47/nizhny-novgorod/geo/ploshchad_minina_i_pozharskogo/1520637017/"},
    ],
    ["square", "center", "landmark", "minin", "history"],
    maps_org("https://yandex.com/maps/47/nizhny-novgorod/geo/ploshchad_minina_i_pozharskogo/1520637017/", "Minin and Pozharsky Square", "Nizhny Novgorod"),
))

# 7) Набережная Фёдоровского --------------------------------------------------
RECORDS.append(rec(
    "fedorovsky-embankment",
    "Bờ sông Fedorovsky (Naberezhnaya Fyodorovskogo)",
    "Набережная Фёдоровского",
    "Fedorovsky Embankment",
    ["square_street", "park_garden"],
    56.32641, 43.987357,
    "Bờ dốc cao hữu ngạn sông Oka, gần phố cổ Rozhdestvenskaya, quận Nizhegorodsky, thành phố Nizhny Novgorod, Nga.",
    "Bờ sông Fedorovsky là tuyến đi dạo trên triền dốc cao nhìn ra sông Oka và bãi Strelka – nơi Oka gặp Volga. Đây là một trong những điểm ngắm hoàng hôn và toàn cảnh thành phố đẹp nhất Nizhny Novgorod.",
    "Uốn theo triền dốc cao ở hữu ngạn sông Oka, bờ sông Fedorovsky là một trong những điểm ngắm cảnh được yêu thích nhất Nizhny Novgorod. Từ các sân ngắm bậc thang ở đây, tầm mắt mở ra bao la: dòng Oka rộng lớn, bãi Strelka nơi Oka hoà vào Volga, cầu Kanavinsky cổ kính và cả những nhà thờ mái vòm phía bờ đối diện. Sau đợt cải tạo, tuyến bờ sông được trang bị lối đi lát đá, ghế ngồi hình bậc thang như khán đài, chòi nghỉ, đèn trang trí và các sân ngắm cảnh; nơi đây cũng có tượng đài đại văn hào Maxim Gorky. Buổi chiều tà, người dân và du khách kéo tới đây dạo bộ, ngắm hoàng hôn buông trên mặt sông – khung cảnh làm nên nhiều bức ảnh biểu tượng của thành phố. Bờ sông nằm ngay trên phố cổ Rozhdestvenskaya, nên rất dễ kết hợp trong hành trình đi bộ khám phá khu phố dưới.",
    [
        "Điểm ngắm toàn cảnh sông Oka, bãi Strelka và cầu Kanavinsky – đẹp nhất lúc hoàng hôn.",
        "Tuyến đi dạo cải tạo hiện đại với sân ngắm bậc thang, chòi nghỉ và tượng đài Maxim Gorky.",
        "Nằm ngay trên phố cổ Rozhdestvenskaya, dễ kết hợp tham quan khu phố dưới.",
    ],
    {
        "hours_vi": "Không gian mở, dạo chơi tự do cả ngày; đẹp nhất lúc chiều tà.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–60 phút.",
        "best_time_vi": "Cuối chiều để ngắm hoàng hôn; mùa ấm từ cuối xuân đến đầu thu.",
        "tips_vi": "Kết hợp đi bộ dọc phố Rozhdestvenskaya; mang máy ảnh để chụp toàn cảnh Strelka.",
    },
    [
        {"title": "KP.ru — Набережная Фёдоровского в Нижнем Новгороде", "url": "https://www.kp.ru/russia/nizhnij-novgorod/mesta/naberezhnaya-fedorovskogo/"},
        {"title": "Kudago — Набережная Фёдоровского", "url": "https://nn.kudago.com/place/naberezhnaya-fedorovskogo/"},
    ],
    ["embankment", "viewpoint", "oka", "strelka", "walk"],
    maps_text("Набережная Фёдоровского", "Нижний Новгород", "Fedorovsky Embankment", "Nizhny Novgorod", 56.32641, 43.987357),
))

# 8) Александровский сад -------------------------------------------------------
RECORDS.append(rec(
    "alexandrovsky-garden-nn",
    "Vườn Aleksandrovsky (Aleksandrovsky sad)",
    "Александровский сад",
    "Alexander Garden",
    ["park_garden"],
    56.3306, 44.0152,
    "Trên sườn dốc bờ sông Volga, giữa hai tuyến bờ sông Thượng và Hạ Volga, quận Nizhegorodsky, thành phố Nizhny Novgorod, Nga.",
    "Vườn Aleksandrovsky là công viên lâu đời trải dọc sườn dốc bờ Volga trong trung tâm lịch sử. Những lối đi uốn lượn giữa cây xanh mở ra tầm nhìn rộng ra dòng sông và nối liền từ Cầu thang Chkalov gần như tới ga cáp treo.",
    "Trải mình trên triền dốc thoai thoải bên bờ sông Volga, giữa tuyến bờ sông Thượng Volga (Verkhne-Volzhskaya) phía trên và Hạ Volga (Nizhne-Volzhskaya) phía dưới, Vườn Aleksandrovsky là một trong những công viên lâu đời và giàu chất thơ nhất Nizhny Novgorod. Công viên được lập từ nửa đầu thế kỷ 19 trên một dải đất hình tam giác giữa các đường dốc xuống sông, với hệ thống lối đi quanh co men theo sườn đồi. Dạo bước dưới tán cây, du khách vừa được che mát vừa liên tục bắt gặp những khung nhìn mở ra mặt sông Volga rộng lớn. Công viên có chiều dài đáng kể, kéo dài từ khu vực Cầu thang Chkalov gần như tới ga cáp treo, nên có thể kết hợp thành một tuyến đi dạo dài ngắm sông. Sau các đợt cải tạo, nơi đây có thêm lối đi, ghế nghỉ và điểm ngắm cảnh, trở thành chốn thư giãn quen thuộc của người dân thành phố.",
    [
        "Công viên lâu đời từ thế kỷ 19 trên sườn dốc bờ Volga giữa hai tuyến bờ sông.",
        "Lối đi uốn lượn dưới tán cây với nhiều khung nhìn mở ra sông Volga.",
        "Kéo dài từ Cầu thang Chkalov gần như tới ga cáp treo – tuyến đi dạo dài lý tưởng.",
    ],
    {
        "hours_vi": "Không gian mở, dạo chơi tự do cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 40–90 phút tuỳ tuyến đi.",
        "best_time_vi": "Mùa ấm từ cuối xuân đến đầu thu; đẹp cả buổi sáng lẫn chiều tà.",
        "tips_vi": "Đi giày thoải mái vì đường dốc; kết hợp với Cầu thang Chkalov và bờ Thượng Volga.",
    },
    [
        {"title": "Wikipedia (RU) — Александровский сад (Нижний Новгород)", "url": "https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%B0%D0%B4_(%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4)"},
        {"title": "Yandex Maps — Александровский сад", "url": "https://yandex.com/maps/org/aleksandrovskiy_sad/97201849390/"},
    ],
    ["park", "garden", "volga", "walk", "viewpoint"],
    maps_org("https://yandex.com/maps/org/aleksandrovskiy_sad/97201849390/", "Alexander Garden", "Nizhny Novgorod"),
))

# 9) Парк «Швейцария» ---------------------------------------------------------
RECORDS.append(rec(
    "shveytsariya-park",
    "Công viên «Thuỵ Sĩ» (Park «Shveytsariya»)",
    "Парк «Швейцария»",
    "Shvetsariya Park (Switzerland Park)",
    ["park_garden"],
    56.2806, 43.9755,
    "Đại lộ Gagarin (проспект Гагарина) số 35, quận Prioksky, ven bờ dốc sông Oka, thành phố Nizhny Novgorod, Nga.",
    "Công viên 'Thuỵ Sĩ' là công viên lớn nhất Nizhny Novgorod, trải dài ven bờ dốc sông Oka. Sau đợt cải tạo quy mô lớn, nơi đây trở thành không gian dạo chơi, thể thao và giải trí hiện đại được yêu thích bậc nhất thành phố.",
    "Nằm dọc theo bờ dốc cao của sông Oka ở quận Prioksky, công viên 'Thuỵ Sĩ' (Shveytsariya) là công viên lớn nhất và một trong những điểm đến được yêu thích nhất Nizhny Novgorod. Tên gọi 'Thuỵ Sĩ' gợi tới địa hình đồi dốc và cảnh quan xanh mướt của công viên. Trải qua một cuộc cải tạo toàn diện hoàn tất vào đầu thập niên 2020, công viên khoác diện mạo hiện đại với nhiều lối đi bộ và làn xe đạp, các khu vui chơi trẻ em, sân thể thao, khu vực biểu diễn, quán cà phê, đài phun nước và những điểm ngắm sông Oka. Trong khuôn viên còn có một vườn thú nhỏ. Công viên có nhiều cổng vào từ phía đại lộ Gagarin, mở cửa gần như cả ngày và vào tự do. Rộng rãi, nhiều cây xanh và tiện ích, đây là nơi lý tưởng để người dân và du khách thư giãn, tập thể thao hoặc dạo mát cuối tuần.",
    [
        "Công viên lớn nhất Nizhny Novgorod, trải dài ven bờ dốc sông Oka.",
        "Được cải tạo hiện đại với lối đi bộ, làn xe đạp, sân chơi, khu thể thao và điểm ngắm sông.",
        "Nhiều cổng vào từ đại lộ Gagarin, vào tự do, có cả vườn thú nhỏ bên trong.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày, khoảng 5:00–23:00 (vào đến ~22:00).",
        "ticket_vi": "Vào cửa miễn phí; một số dịch vụ, trò chơi thu phí riêng.",
        "duration_vi": "Khoảng 1–2 giờ hoặc hơn.",
        "best_time_vi": "Mùa ấm từ cuối xuân đến đầu thu; cuối tuần rất nhộn nhịp.",
        "tips_vi": "Vào bằng cổng chính gần bến 'Park Shveytsariya'; công viên rất rộng nên chọn tuyến trước.",
    },
    [
        {"title": "Culture.ru — Парк «Швейцария»", "url": "https://www.culture.ru/institutes/87164/park-shveicariya"},
        {"title": "Trang chính thức — Парк «Швейцария» (swissparknn.ru)", "url": "https://swissparknn.ru/"},
    ],
    ["park", "recreation", "oka", "family", "modern"],
    maps_text("Парк Швейцария", "Нижний Новгород", "Shvetsariya Park", "Nizhny Novgorod", 56.2806, 43.9755),
    official_site="https://swissparknn.ru/",
))

# 10) Зоопарк «Лимпопо» -------------------------------------------------------
RECORDS.append(rec(
    "limpopo-zoo",
    "Vườn thú «Limpopo» (Zoopark «Limpopo»)",
    "Зоопарк «Лимпопо»",
    "Limpopo Zoo",
    ["park_garden", "other"],
    56.334352, 43.854332,
    "Phố Yaroshenko (улица Ярошенко) số 7Б, rìa Công viên Sormovsky, quận Sormovsky, thành phố Nizhny Novgorod, Nga.",
    "Vườn thú 'Limpopo' là vườn thú tư nhân đầu tiên của nước Nga, nằm ở rìa Công viên Sormovsky. Nơi đây nuôi dưỡng hơn 270 loài với hàng nghìn cá thể từ khắp thế giới, là điểm đến quen thuộc cho gia đình.",
    "Toạ lạc ở rìa tây nam Công viên văn hoá Sormovsky, vườn thú 'Limpopo' được thành lập năm 2003 và được biết đến như vườn thú tư nhân đầu tiên tại Nga. Trên diện tích khoảng bảy héc-ta, vườn thú quy tụ hơn 270 loài động vật với hơn một nghìn năm trăm cá thể đến từ nhiều châu lục – từ hổ, sư tử, gấu, linh trưởng cho tới các loài chim, bò sát và thú nhỏ. Các chuồng trại và khu nuôi được bố trí dọc những lối đi rợp bóng cây trong công viên, kèm bảng thông tin, khu vui chơi và dịch vụ cho trẻ em. Vườn thú tham gia các chương trình nhân giống, chăm sóc và giáo dục bảo tồn, là điểm đến giải trí – học hỏi được nhiều gia đình ở Nizhny Novgorod yêu thích, đặc biệt vào cuối tuần và dịp nghỉ.",
    [
        "Vườn thú tư nhân đầu tiên của nước Nga, thành lập năm 2003.",
        "Hơn 270 loài với hàng nghìn cá thể từ khắp thế giới trên diện tích khoảng 7 ha.",
        "Nằm ở rìa Công viên Sormovsky, điểm đến quen thuộc cho gia đình và trẻ em.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày, khoảng 9:00–20:00 (bán vé đến ~19:00).",
        "ticket_vi": "Vé vào cửa theo giá niêm yết; có ưu đãi cho trẻ em và một số nhóm.",
        "duration_vi": "Khoảng 1,5–3 giờ.",
        "best_time_vi": "Mùa ấm từ cuối xuân đến đầu thu; đi sớm để tránh đông cuối tuần.",
        "tips_vi": "Đi tàu điện ngầm/ xe buýt về hướng Sormovo; kết hợp dạo Công viên Sormovsky bên cạnh.",
    },
    [
        {"title": "Wikipedia (RU) — Лимпопо (зоопарк)", "url": "https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D0%BC%D0%BF%D0%BE%D0%BF%D0%BE_(%D0%B7%D0%BE%D0%BE%D0%BF%D0%B0%D1%80%D0%BA)"},
        {"title": "Trang chính thức — Зоопарк «Лимпопо» (nnzoo.ru)", "url": "https://nnzoo.ru/"},
    ],
    ["zoo", "family", "animals", "sormovo", "recreation"],
    maps_org("https://yandex.com/maps/org/limpopo/1119526157/", "Limpopo Zoo", "Nizhny Novgorod"),
    official_site="https://nnzoo.ru/",
))

# 11) Канавинский мост --------------------------------------------------------
RECORDS.append(rec(
    "kanavinsky-bridge",
    "Cầu Kanavinsky (Kanavinsky most)",
    "Канавинский мост",
    "Kanavinsky Bridge",
    ["bridge"],
    56.32190, 43.97240,
    "Bắc qua sông Oka, nối phần cao (nagornaya) với phần bờ trái (zarechnaya) của thành phố Nizhny Novgorod, Nga.",
    "Cầu Kanavinsky là cây cầu cố định đầu tiên bắc qua sông Oka ở Nizhny Novgorod, khánh thành năm 1933. Cầu dài gần 800 m, nối trung tâm lịch sử với khu Kanavino, gần nơi Oka đổ vào Volga.",
    "Bắc ngang dòng Oka ngay gần chỗ con sông hoà vào Volga, cầu Kanavinsky là cây cầu cố định đầu tiên qua sông Oka trong lòng Nizhny Novgorod. Cầu được xây trong các năm 1930–1933 và thông xe ngày 2 tháng 4 năm 1933, dài khoảng 795,5 m và rộng hơn 23 m, nối phần cao (nagornaya) ở hữu ngạn với phần bờ trái (zarechnaya) bên khu Kanavino, nơi có Cung Hội chợ và ga đường sắt Moskovsky. Từng mang nhiều tên gọi qua các thời kỳ, cây cầu là một phần không thể thiếu của giao thông và diện mạo đô thị, đặc biệt khi lên đèn vào buổi tối. Với người đi bộ, cầu còn là nơi lý tưởng để ngắm toàn cảnh hai bờ sông, bãi Strelka và các bờ sông của thành phố. Đây là một trong những công trình hạ tầng mang tính biểu tượng, gắn với quá trình hiện đại hoá Nizhny Novgorod thế kỷ 20.",
    [
        "Cây cầu cố định đầu tiên bắc qua sông Oka ở Nizhny Novgorod, thông xe năm 1933.",
        "Dài gần 800 m, nối phần cao trung tâm với khu Kanavino gần bãi Strelka.",
        "Điểm ngắm cảnh hai bờ sông đẹp, đặc biệt khi lên đèn buổi tối.",
    ],
    {
        "hours_vi": "Công trình giao thông công cộng, qua lại tự do; đi bộ đẹp nhất ban ngày và tối.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–30 phút nếu đi bộ ngắm cảnh.",
        "best_time_vi": "Chiều tối khi lên đèn; mùa ấm dễ đi bộ.",
        "tips_vi": "Kết hợp ngắm từ bờ sông Fedorovsky hoặc bãi Strelka để có góc nhìn đẹp.",
    },
    [
        {"title": "Wikipedia (RU) — Канавинский мост", "url": "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BD%D0%B0%D0%B2%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%BE%D1%81%D1%82"},
        {"title": "Kudago — Канавинский мост", "url": "https://nn.kudago.com/place/kanavinskij-most/"},
    ],
    ["bridge", "oka", "landmark", "history", "engineering"],
    maps_text("Канавинский мост", "Нижний Новгород", "Kanavinsky Bridge", "Nizhny Novgorod", 56.32190, 43.97240),
))

# 12) Свято-Троицкий Островоезерский монастырь (Ворсма) -----------------------
RECORDS.append(rec(
    "ostrovoezersky-monastery-vorsma",
    "Tu viện Trinity Ostrovoezersky trên đảo hồ (Svyato-Troitsky Ostrovoezersky monastyr)",
    "Свято-Троицкий Островоезерский монастырь",
    "Holy Trinity Ostrovoezersky Monastery",
    ["church", "monument"],
    55.990277, 43.293688,
    "Trên một hòn đảo giữa hồ Tosканka (hồ Vorsma), thị trấn Vorsma, huyện Pavlovsky, tỉnh Nizhny Novgorod, Nga.",
    "Tu viện Trinity Ostrovoezersky là tu viện duy nhất của tỉnh nằm trên một hòn đảo giữa hồ. Được lập từ cuối thế kỷ 16 và mang các nhà thờ đá cuối thế kỷ 17, tu viện nối với bờ bằng một cây cầu nhỏ, tạo nên khung cảnh nên thơ hiếm có.",
    "Nổi lên giữa mặt nước hồ Tosканka (còn gọi là hồ Vorsma) ở rìa thị trấn Vorsma, Tu viện Trinity Ostrovoezersky là một trong những điểm đến nên thơ nhất tỉnh Nizhny Novgorod – tu viện duy nhất trong vùng thực sự 'đứng trên nước', trên một hòn đảo giữa hồ. Theo sử liệu, đời sống tu hành ở đây bắt đầu từ nửa sau thế kỷ 16 với vị ẩn tu Makary, dưới sự bảo trợ của dòng họ quý tộc Cherkassky. Sang cuối thế kỷ 17, dưới thời công tước Mikhail Yakovlevich Cherkassky, tu viện bước vào giai đoạn xây dựng bằng đá, tạo nên quần thể hài hoà gồm nhà thờ chính toà Trinity, nhà thờ Kazan, dãy phòng tu kèm nhà thờ cổng Mikhail Malein và tường thành có tháp. Phần lớn công trình gốc bị phá dỡ vào thập niên 1930–1950; từ năm 2007 tu viện được hồi sinh (nay là tu viện nữ) với nhà thờ Trinity và Kazan được dựng lại phỏng theo nguyên mẫu, còn nhà thờ cổng Mikhail Malein thế kỷ 17 vẫn giữ được nét nguyên bản. Đường vào đảo qua một cây cầu nhỏ; nhìn từ trên gò đất khi tiến vào Vorsma, cả tu viện hiện ra soi bóng xuống hồ, đẹp như tranh.",
    [
        "Tu viện duy nhất trong tỉnh nằm trên một hòn đảo giữa hồ Tosканka, nối bờ bằng cầu nhỏ.",
        "Được lập cuối thế kỷ 16, có các nhà thờ đá cuối thế kỷ 17 gắn với dòng họ Cherkassky.",
        "Khung cảnh soi bóng xuống mặt hồ đẹp như tranh, đặc biệt khi nhìn từ đường vào Vorsma.",
    ],
    {
        "hours_vi": "Mở cửa cho khách hành hương ban ngày; nên đi vào buổi sáng hoặc chiều.",
        "ticket_vi": "Vào tự do (miễn phí); hoan nghênh quyên góp tuỳ tâm.",
        "duration_vi": "Khoảng 45–60 phút; thêm thời gian di chuyển từ Nizhny Novgorod (~70 km).",
        "best_time_vi": "Mùa ấm khi hồ trong xanh; mùa thu lá vàng cũng rất đẹp.",
        "tips_vi": "Đi bằng ô tô là tiện nhất; ăn mặc kín đáo; dừng ở điểm cao đầu thị trấn để chụp toàn cảnh.",
    },
    [
        {"title": "Wikipedia (RU) — Свято-Троицкий Островоезерский монастырь", "url": "https://ru.wikipedia.org/wiki/%D0%A1%D0%B2%D1%8F%D1%82%D0%BE-%D0%A2%D1%80%D0%BE%D0%B8%D1%86%D0%BA%D0%B8%D0%B9_%D0%9E%D1%81%D1%82%D1%80%D0%BE%D0%B2%D0%BE%D0%B5%D0%B7%D0%B5%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%BE%D0%BD%D0%B0%D1%81%D1%82%D1%8B%D1%80%D1%8C"},
        {"title": "sobory.ru — Ворсма, Островоезерский Троицкий монастырь (Координаты 55.990277, 43.293688)", "url": "https://sobory.ru/article/?object=05553"},
    ],
    ["monastery", "church", "island", "vorsma", "lake"],
    maps_text("Островоезерский монастырь", "Ворсма", "Ostrovoezersky Monastery", "Vorsma", 55.990277, 43.293688),
))

# 13) Павлово -----------------------------------------------------------------
RECORDS.append(rec(
    "pavlovo-town",
    "Thị trấn thủ công Pavlovo bên sông Oka",
    "Павлово",
    "Pavlovo (Pavlovo-on-Oka)",
    ["monument", "museum"],
    55.9667, 43.0667,
    "Thị trấn Pavlovo, hữu ngạn sông Oka, cách Nizhny Novgorod khoảng 70 km về phía tây nam, tỉnh Nizhny Novgorod, Nga.",
    "Pavlovo là thị trấn cổ bên sông Oka nổi danh về nghề kim khí: dao, khoá, dụng cụ và những chiếc khoá tí hon tinh xảo. Phố cổ trên sườn đồi, bảo tàng nghề thủ công và truyền thống nuôi chim, trồng chanh cảnh tạo nên bản sắc riêng.",
    "Nằm trên các sườn đồi Peremilovsky bên hữu ngạn sông Oka, cách Nizhny Novgorod chừng 70 km, Pavlovo (Pavlovo-na-Oke) là một trong những thị trấn thủ công nổi tiếng nhất nước Nga. Từ nhiều thế kỷ, nơi đây là trung tâm nghề kim khí: thợ Pavlovo làm ra dao, kéo, khoá, dụng cụ y tế và cả những chiếc khoá, con dao siêu nhỏ tinh xảo được xem như tuyệt kỹ. Truyền thống ấy được kể lại sinh động trong Bảo tàng lịch sử Pavlovo. Bên cạnh đó, thị trấn còn nổi tiếng với những thú chơi độc đáo: nuôi ngỗng chọi, gà chọi, nuôi chim hoàng yến (canary) và trồng chanh cảnh 'Pavlovsky' trên bậu cửa sổ – những nét văn hoá dân dã đã thành thương hiệu. Dạo bước trên các con phố cổ men theo sườn đồi nhìn xuống sông Oka, du khách bắt gặp những ngôi nhà gỗ chạm khắc, nhà thờ và khung cảnh tỉnh lẻ Nga đặc trưng. Pavlovo là điểm đến thú vị cho ai muốn tìm hiểu di sản thủ công và đời sống địa phương ngoài thành phố lớn.",
    [
        "Thị trấn cổ nổi danh về nghề kim khí: dao, khoá, dụng cụ và khoá tí hon tinh xảo.",
        "Nổi tiếng với thú nuôi ngỗng chọi, chim hoàng yến và trồng chanh cảnh 'Pavlovsky'.",
        "Phố cổ trên sườn đồi nhìn xuống sông Oka cùng Bảo tàng lịch sử Pavlovo.",
    ],
    {
        "hours_vi": "Thị trấn tham quan tự do; bảo tàng thường mở khoảng 10:00–17:00 và nghỉ một ngày trong tuần.",
        "ticket_vi": "Dạo phố miễn phí; vé bảo tàng mức thấp.",
        "duration_vi": "Nửa ngày; cộng thời gian di chuyển từ Nizhny Novgorod.",
        "best_time_vi": "Mùa ấm từ cuối xuân đến đầu thu.",
        "tips_vi": "Đi bằng ô tô hoặc xe khách; kết hợp ghé tu viện trên đảo ở Vorsma gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Павлово (Нижегородская область)", "url": "https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D0%BE_(%D0%9D%D0%B8%D0%B6%D0%B5%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C)"},
        {"title": "nn-obl.ru — История города Павлово", "url": "https://www.nn-obl.ru/%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0-%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D0%BE/"},
    ],
    ["town", "crafts", "metalwork", "oka", "history"],
    maps_text("Павлово", "Нижегородская область", "Pavlovo", "Nizhny Novgorod Oblast", 55.9667, 43.0667),
))

# 14) Балахна -----------------------------------------------------------------
RECORDS.append(rec(
    "balakhna-town",
    "Thị trấn cổ Balakhna",
    "Балахна",
    "Balakhna",
    ["monument", "church"],
    56.4906, 43.5919,
    "Thị trấn Balakhna, hữu ngạn sông Volga, cách Nizhny Novgorod khoảng 34 km về phía tây bắc, tỉnh Nizhny Novgorod, Nga.",
    "Balakhna là thị trấn cổ bên sông Volga, quê hương của người anh hùng Kuzma Minin. Nổi tiếng với nghề làm muối, đóng thuyền và ren tay truyền thống, thị trấn còn giữ nhà thờ Nikolskaya năm 1552 – nhà thờ đá cổ nhất giáo phận.",
    "Trải dọc hữu ngạn sông Volga, cách Nizhny Novgorod khoảng 34 km về phía tây bắc, Balakhna là một trong những thị trấn cổ nhất vùng, được nhắc tới từ năm 1474. Đây là quê hương của Kuzma Minin – người anh hùng khởi xướng đội dân binh giải phóng Moskva năm 1612 – nên thị trấn mang ý nghĩa lịch sử đặc biệt với người Nga. Thời trung đại, Balakhna trù phú nhờ nghề nấu muối, đóng thuyền và về sau nổi danh với nghề ren tay (kruzhevo) tinh xảo của phụ nữ địa phương. Di sản kiến trúc nổi bật nhất là nhà thờ Nikolskaya (Thánh Nikolay) xây năm 1552 theo lệnh Ivan Bạo chúa để mừng chiến thắng Kazan – được xem là nhà thờ đá cổ nhất còn lại của giáo phận Nizhny Novgorod, với hình khối bát giác trên đế vuông gợi nhớ các nhà thờ gỗ mái nhọn. Bên cạnh đó còn có tu viện Pokrovsky và các nhà thờ, bảo tàng địa phương kể về nghề muối và ren. Balakhna phù hợp cho một chuyến đi trong ngày để cảm nhận chiều sâu lịch sử của vùng Volga.",
    [
        "Thị trấn cổ bên sông Volga (nhắc tới từ 1474), quê hương anh hùng Kuzma Minin.",
        "Nhà thờ Nikolskaya năm 1552 – nhà thờ đá cổ nhất giáo phận Nizhny Novgorod.",
        "Truyền thống nghề muối, đóng thuyền và ren tay tinh xảo.",
    ],
    {
        "hours_vi": "Thị trấn tham quan tự do; các nhà thờ và bảo tàng mở ban ngày, nên kiểm tra lịch.",
        "ticket_vi": "Dạo phố và vào nhà thờ miễn phí; vé bảo tàng mức thấp.",
        "duration_vi": "Nửa ngày; cộng thời gian di chuyển từ Nizhny Novgorod.",
        "best_time_vi": "Mùa ấm từ cuối xuân đến đầu thu.",
        "tips_vi": "Đi bằng ô tô hoặc tàu/ xe khách; ưu tiên ghé nhà thờ Nikolskaya cổ kính.",
    },
    [
        {"title": "Wikipedia (RU) — Балахна", "url": "https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D0%BB%D0%B0%D1%85%D0%BD%D0%B0"},
        {"title": "sobory.ru — Балахна, церковь Николая Чудотворца (1552)", "url": "https://sobory.ru/article/?object=01869"},
    ],
    ["town", "volga", "minin", "church", "history"],
    maps_text("Балахна", "Нижегородская область", "Balakhna", "Nizhny Novgorod Oblast", 56.4906, 43.5919),
))

# 15) Ичалковский бор ---------------------------------------------------------
RECORDS.append(rec(
    "ichalkovsky-bor",
    "Rừng Ichalkovsky và hang động karst (Ichalkovsky bor)",
    "Ичалковский бор",
    "Ichalkovsky Bor (Forest and Karst Caves)",
    ["park_garden", "other"],
    55.437297, 44.537652,
    "Gần làng Ichalki, huyện Perevozsky, bên khúc uốn sông Pyana, tỉnh Nizhny Novgorod, Nga.",
    "Ichalkovsky bor là khu bảo tồn thiên nhiên độc đáo bên khúc uốn sông Pyana, nổi tiếng với hàng nghìn hố sụt và hang động karst. Những vực đá, grotto và hồ ngầm giữa rừng thông tạo nên cảnh quan kỳ vĩ hiếm có ở đồng bằng Nga.",
    "Nằm trong khúc uốn quanh co của sông Pyana, cách làng Ichalki chừng vài cây số, Ichalkovsky bor là một trong những kỳ quan thiên nhiên đặc sắc nhất tỉnh Nizhny Novgorod. Trên diện tích khoảng 900 héc-ta rừng thông hỗn giao – kiểu rừng hiếm gặp ở vùng Volga – ẩn chứa hơn một nghìn hố sụt và hang động karst hình thành do nước mưa và nước sông bào mòn tầng đá vôi qua hàng nghìn năm. Du khách có thể men theo các lối mòn để khám phá những vực đá sâu hoắm, các grotto nổi tiếng như 'Kholodnaya' (Lạnh) và 'Teplaya' (Ấm) với hồ nước ngầm trong vắt dưới đáy, cùng những 'cây cầu đá' tự nhiên bắc ngang miệng vực. Cảnh quan hùng vĩ với vách đá dựng đứng, rừng thông cổ thụ và mặt nước ẩn hiện tạo cảm giác như lạc vào vùng núi, dù đang ở giữa đồng bằng. Khu vực được bảo vệ như một khu bảo tồn (zakaznik) từ đầu thập niên 1970. Đây là điểm đến lý tưởng cho người ưa đi bộ đường dài và chụp ảnh thiên nhiên.",
    [
        "Hơn một nghìn hố sụt và hang động karst giữa rừng thông cổ bên sông Pyana.",
        "Các grotto nổi tiếng 'Kholodnaya' và 'Teplaya' có hồ nước ngầm trong vắt.",
        "Cảnh quan vách đá, cầu đá tự nhiên kỳ vĩ hiếm có ở đồng bằng Nga.",
    ],
    {
        "hours_vi": "Không gian thiên nhiên mở; tham quan ban ngày, tự chịu trách nhiệm an toàn.",
        "ticket_vi": "Vào tự do (miễn phí).",
        "duration_vi": "Khoảng 2–4 giờ đi bộ khám phá.",
        "best_time_vi": "Cuối xuân đến đầu thu; đường khô ráo, an toàn hơn.",
        "tips_vi": "Đi giày bám tốt, cẩn thận mép vực trơn; nên đi cùng nhóm và mang đủ nước.",
    },
    [
        {"title": "Tonkosti.ru — Ичалковский бор", "url": "https://tonkosti.ru/%D0%98%D1%87%D0%B0%D0%BB%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B1%D0%BE%D1%80"},
        {"title": "Putidorogi-nn.ru — Ичалковский бор (Нижегородская область)", "url": "https://putidorogi-nn.ru/evropa/350-ichalkovskii-bor"},
    ],
    ["nature", "karst", "caves", "forest", "hiking"],
    maps_text("Ичалковский бор", "Нижегородская область", "Ichalkovsky Bor", "Nizhny Novgorod Oblast", 55.437297, 44.537652),
))

# 16) Керженский заповедник ---------------------------------------------------
RECORDS.append(rec(
    "kerzhensky-reserve",
    "Khu bảo tồn thiên nhiên Kerzhensky (Kerzhensky zapovednik)",
    "Керженский заповедник",
    "Kerzhensky Nature Reserve",
    ["park_garden", "other"],
    56.4719, 44.4917,
    "Trung tâm sinh thái tại làng Rustay, phố Oktyabrskaya số 17, tả ngạn sông Kerzhenets, tỉnh Nizhny Novgorod, Nga.",
    "Kerzhensky là khu bảo tồn thiên nhiên sinh quyển (UNESCO) ở tả ngạn sông Kerzhenets, bảo vệ hệ rừng taiga phương nam, đầm lầy và các loài quý hiếm. Trung tâm sinh thái ở làng Rustay giới thiệu cảnh quan và động thực vật của khu bảo tồn cho du khách.",
    "Trải rộng ở vùng Zavolzhye tả ngạn sông Kerzhenets, cách Nizhny Novgorod khoảng 55 km về phía đông bắc, Khu bảo tồn thiên nhiên Kerzhensky được thành lập năm 1993 và về sau được UNESCO công nhận là khu dự trữ sinh quyển. Khu bảo tồn gìn giữ một mẫu điển hình của hệ sinh thái taiga phương nam: rừng thông chiếm phần lớn diện tích, xen kẽ rừng cây lá nhỏ và những vùng đầm lầy rộng lớn. Đây là nơi trú ngụ của nhiều loài động vật – trong đó có chương trình phục hồi đàn hải ly và bảo tồn các loài chim quý – cùng thảm thực vật đặc trưng vùng Kerzhenets, vốn gắn với lịch sử của cộng đồng Tín đồ Cũ (Old Believers). Vì là khu bảo tồn nghiêm ngặt, phần lõi không mở cho tham quan tự do; thay vào đó, du khách đến trung tâm sinh thái ở làng Rustay – một toà nhà sáng sủa mái dốc – để tìm hiểu về cảnh quan, hệ động thực vật qua trưng bày và các tuyến đường mòn sinh thái được phép. Đây là điểm đến cho những ai yêu thiên nhiên hoang sơ và muốn tìm hiểu công tác bảo tồn.",
    [
        "Khu dự trữ sinh quyển UNESCO bảo vệ rừng taiga phương nam và đầm lầy bên sông Kerzhenets.",
        "Có chương trình phục hồi hải ly và bảo tồn nhiều loài chim, thú quý.",
        "Trung tâm sinh thái ở làng Rustay với trưng bày và tuyến đường mòn cho du khách.",
    ],
    {
        "hours_vi": "Trung tâm sinh thái mở theo lịch; các tuyến tham quan cần đăng ký trước với ban quản lý.",
        "ticket_vi": "Tham quan các tuyến sinh thái có thu phí/ theo tour; nên liên hệ trước.",
        "duration_vi": "Nửa ngày đến một ngày; cộng thời gian di chuyển.",
        "best_time_vi": "Cuối xuân đến đầu thu; mang đồ chống muỗi vào mùa hè.",
        "tips_vi": "Liên hệ đặt tour trước; phần lõi bảo tồn không vào tự do, hãy đi theo hướng dẫn.",
    },
    [
        {"title": "Wikipedia (RU) — Керженский заповедник", "url": "https://ru.wikipedia.org/wiki/%D0%9A%D0%B5%D1%80%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B7%D0%B0%D0%BF%D0%BE%D0%B2%D0%B5%D0%B4%D0%BD%D0%B8%D0%BA"},
        {"title": "ООПТ России — Керженский заповедник", "url": "http://oopt.info/index.php?oopt=786"},
    ],
    ["nature", "reserve", "biosphere", "taiga", "kerzhenets"],
    maps_text("Керженский заповедник экоцентр Рустай", "Нижегородская область", "Kerzhensky Reserve Ecocenter", "Rustay", 56.4719, 44.4917),
))

# 17) Озеро Ключик (Голубое озеро) --------------------------------------------
RECORDS.append(rec(
    "klyuchik-blue-lake",
    "Hồ Klyuchik (Hồ Xanh - Goluboe ozero)",
    "Озеро Ключик (Голубое озеро)",
    "Lake Klyuchik (Blue Lake)",
    ["park_garden", "other"],
    55.975531, 43.327413,
    "Gần làng Grudtsino, huyện Pavlovsky, giữa Vorsma và Dzerzhinsk, tỉnh Nizhny Novgorod, Nga.",
    "Hồ Klyuchik là một hồ karst nhỏ nổi tiếng với làn nước xanh ngọc trong vắt, quanh năm không đóng băng nhờ các mạch nước ngầm. Được công nhận là di tích thiên nhiên, đây là điểm dã ngoại và chụp ảnh được yêu thích.",
    "Ẩn mình gần làng Grudtsino, huyện Pavlovsky, hồ Klyuchik (thường được gọi chung là 'Hồ Xanh') là một trong những di tích thiên nhiên độc đáo nhất tỉnh Nizhny Novgorod. Đây là hồ có nguồn gốc karst, được nuôi bởi các mạch nước ngầm phun lên từ đáy, khiến nước trong đến mức có thể nhìn thấu xuống độ sâu đáng kể và mang sắc xanh ngọc bích rất đặc trưng. Nhờ dòng nước ngầm liên tục, hồ gần như không đóng băng ngay cả trong những ngày đông giá rét, tạo nên khung cảnh hơi nước bốc lên kỳ ảo giữa mùa tuyết. Xung quanh là rừng cây và bãi cỏ, thích hợp cho dã ngoại, chụp ảnh và tận hưởng thiên nhiên yên bình. Do là di tích thiên nhiên được bảo vệ và có mạch nước ngầm, du khách nên giữ gìn cảnh quan, không xả rác và cẩn trọng khi xuống nước vì nhiệt độ lạnh và địa hình đáy phức tạp. Hồ thường được kết hợp trong hành trình tới Vorsma và Pavlovo.",
    [
        "Hồ karst với làn nước xanh ngọc trong vắt, nhìn thấu đáy.",
        "Gần như không đóng băng quanh năm nhờ các mạch nước ngầm.",
        "Di tích thiên nhiên được bảo vệ, điểm dã ngoại và chụp ảnh nổi tiếng.",
    ],
    {
        "hours_vi": "Không gian thiên nhiên mở; tham quan ban ngày, tự chịu trách nhiệm an toàn.",
        "ticket_vi": "Vào tự do (miễn phí).",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Mùa hè để ngắm màu nước xanh; mùa đông có cảnh hơi nước kỳ ảo.",
        "tips_vi": "Không xả rác, giữ gìn di tích; nước rất lạnh và sâu, cẩn trọng khi tới gần mép.",
    },
    [
        {"title": "Iskatel.com — Озеро Ключик: где находится, описание", "url": "https://iskatel.com/places/ozero-klyuchik"},
        {"title": "budetinteresno.info — Голубые озёра", "url": "https://budetinteresno.info/lakes/golubye_ozera.htm"},
    ],
    ["nature", "lake", "karst", "spring", "grudtsino"],
    maps_text("Озеро Ключик", "Грудцино Нижегородская область", "Lake Klyuchik Blue Lake", "Grudtsino", 55.975531, 43.327413),
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
