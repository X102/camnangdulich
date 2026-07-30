# -*- coding: utf-8 -*-
"""_add_places_altai_krai_20260728.py — VÙNG: Vùng Altai (Алтайский край)
(lần chạy tự động 2026-07-28).

Bối cảnh: altai-krai.json hiện có 7 địa điểm. Bổ sung 25 địa điểm THẬT SỰ nổi tiếng/
đặc sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 32 (≥30).

Phân bố loại hình (25 bản ghi mới):
- museum (5): Алтайский краеведческий музей (cổ nhất Siberia, 1823), Художественный музей
  Алтайского края, Музей «Мир времени», Музей истории горного производства (Змеиногорск),
  Рубцовский краеведческий музей.
- church (4): Покровский кафедральный собор, Никольская церковь (Барнаул), Успенский
  собор (Бийск), Знаменский монастырь (Барнаул).
- theatre (4): Театр драмы им. Шукшина, Музыкальный театр (Барнаул), Рубцовский
  драмтеатр, Бийский драмтеатр.
- park_garden (7): Нагорный парк, гора Синюха, Белое озеро, озеро Ая, Малиновое озеро,
  Кулундинское озеро, Лебединое (Светлое) озеро.
- monument (3): Мемориал Славы (+square_street пл. Победы), Царский курган (Сентелек),
  Нулевой километр (Барнаул).
- other (2): Горная аптека (toà nhà đá cổ nhất Барнаул), Колыванский камнерезный завод.

TOẠ ĐỘ — xác minh chéo (sobory.ru dòng «Координаты» / 2gis firm-geo center=LON,LAT /
ru.wikipedia infobox / WebSearch, 2026-07-28). Phạm vi Altai Krai: lat ~50,5–54,5;
lon ~78–87; tất cả toạ độ nằm trong phạm vi, KHÔNG đảo lat/lon:
  Краеведческий музей 53.329461,83.787605 (Ползунова 46, org Яндекс 1007204258);
  Художественный музей 53.356433,83.769028 (пр. Ленина 88, 2gis); Горная аптека
  53.329970,83.789042 (Ползунова 42); Мир времени 53.365130,83.752433 (Матросова 12,
  org Яндекс 1023474740); Нагорный парк 53.324060,83.795016; Театр драмы им. Шукшина
  53.346703,83.773410 (Молодёжная 15); Музыкальный театр 53.350425,83.783970
  (Комсомольский 108); Мемориал Славы 53.350070,83.759600 (пл. Победы, org Яндекс
  80335652178); Никольская церковь 53.341559,83.784876 (sobory 09825, пр. Ленина 36);
  Успенский собор Бийск 52.544397,85.232343 (sobory 12116, Советская 13); Музей горного
  произв. Змеиногорск 51.154228,82.201242 (Щорса 13); Колыванский камнерезный завод
  51.317750,82.571514 (с. Колывань, Курьинский р-н); Синюха 51.241084,82.606356; Белое
  озеро 51.293668,82.648677; Ая 51.904794,85.853738; Малиновое озеро 51.678116,79.789375;
  Кулундинское озеро 53.000000,79.516667; Лебединое/Светлое 52.292616,85.654620 (с.
  Урожайное); Царский курган 51.185111,83.689475 (с. Сентелек); Рубцовский музей
  51.503580,81.208810; Рубцовский драмтеатр 51.510214,81.207280 (org Яндекс 1401367421);
  Бийский драмтеатр 52.539640,85.225220 (Советская 25); Нулевой километр 53.347394,
  83.778443 (пр. Ленина); Покровский собор 53.329521,83.774452 (sobory 09834, Никитина
  137); Знаменский монастырь 53.327585,83.796278 (sobory 19897, Б. Олонская 24).

BỎ (không đưa vào): Тигирекский заповедник — không nguồn nào hiển thị toạ độ số của
tâm/пос. Тигирек để xác minh chắc chắn → KHÔNG bịa, loại bỏ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_altai_krai_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "altai-krai"
REGION_NAME_VI = "Vùng Altai"
FD = "Vùng Siberia"


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

# 1) Алтайский государственный краеведческий музей --------------------------------
RECORDS.append(rec(
    "altai-state-local-lore-museum",
    "Bảo tàng địa phương quốc gia Altai (Barnaul)",
    "Алтайский государственный краеведческий музей",
    "Altai State Museum of Local Lore",
    ["museum"],
    53.329461, 83.787605,
    "Ул. Ползунова, 46, trung tâm lịch sử thành phố Barnaul, vùng Altai, Nga.",
    "Bảo tàng lâu đời nhất Siberia và là một trong những bảo tàng cổ nhất nước Nga, thành lập năm 1823. Nơi lưu giữ hàng trăm nghìn hiện vật về thiên nhiên, ngành khai mỏ Kolyvan-Voskresensk và lịch sử vùng Altai, đặt trong toà nhà phòng thí nghiệm mỏ cổ.",
    "Ra đời năm 1823 nhờ công của kỹ sư Pyotr Frolov và nhà tự nhiên học Friedrich Gebler, Bảo tàng địa phương quốc gia Altai là bảo tàng lâu đời nhất của toàn Siberia và thuộc hàng cổ nhất nước Nga. Bảo tàng toạ lạc ngay trong khu trung tâm lịch sử Barnaul, ở toà nhà từng là phòng thí nghiệm luyện kim của các nhà máy bạc Kolyvan-Voskresensk. Bộ sưu tập đồ sộ dẫn khách đi qua thế giới tự nhiên của rừng taiga và thảo nguyên Altai, khoáng vật và cổ sinh vật, cho tới di sản của ngành khai mỏ - luyện bạc từng làm nên sự giàu có của cả vùng. Điểm nhấn là các mô hình và di vật gắn với Ivan Polzunov, người chế tạo cỗ máy hơi nước đầu tiên của nước Nga tại Barnaul, cùng những cỗ máy thuỷ lực tài tình của Kozma Frolov. Các gian trưng bày còn kể về đời sống của cư dân bản địa, những đợt di dân khai hoang và quá trình hình thành đô thị mỏ Barnaul. Với du khách mới đến, đây là điểm khởi đầu lý tưởng để hiểu vì sao Altai được ví như 'trái tim khoáng sản' của đế quốc Nga xưa.",
    [
        "Bảo tàng lâu đời nhất Siberia (thành lập 1823), một trong những bảo tàng cổ nhất nước Nga.",
        "Trưng bày về thiên nhiên, khoáng vật và di sản khai mỏ - luyện bạc Kolyvan-Voskresensk.",
        "Di vật gắn với Ivan Polzunov - người chế tạo máy hơi nước đầu tiên của nước Nga.",
    ],
    {
        "hours_vi": "Thường mở cửa thứ Ba–Chủ nhật, nghỉ thứ Hai; nên kiểm tra lịch theo mùa.",
        "ticket_vi": "Vé vào cửa giá bình dân; có thêm phí cho tour hướng dẫn và triển lãm chuyên đề.",
        "duration_vi": "Khoảng 1,5–2 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà); tiện ghép với dạo bộ khu trung tâm lịch sử.",
        "tips_vi": "Nằm ngay khu Quảng trường Demidov, đi bộ được tới cột đài Demidov và bờ sông Barnaulka.",
    },
    [
        {"title": "Wikipedia (RU) — Алтайский государственный краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Алтайский_государственный_краеведческий_музей"},
        {"title": "Культура.РФ — Алтайский государственный краеведческий музей", "url": "https://www.culture.ru/institutes/22092/altaiskii-gosudarstvennyi-kraevedcheskii-muzei"},
    ],
    ["museum", "local-history", "barnaul", "mining", "polzunov", "siberia", "altai"],
    maps_org("https://yandex.ru/maps/org/altayskiy_gosudarstvenny_krayevedcheskiy_muzey/1007204258/", "Altai State Museum of Local Lore", "Barnaul"),
))

# 2) Государственный художественный музей Алтайского края --------------------------
RECORDS.append(rec(
    "altai-state-art-museum",
    "Bảo tàng Mỹ thuật quốc gia vùng Altai (Barnaul)",
    "Государственный художественный музей Алтайского края",
    "State Art Museum of Altai Krai",
    ["museum"],
    53.356433, 83.769028,
    "Пр. Ленина, 88, thành phố Barnaul, vùng Altai, Nga.",
    "Bảo tàng mỹ thuật lớn nhất vùng Altai với bộ sưu tập hơn mười lăm nghìn tác phẩm, từ thánh tượng cổ, hội hoạ Nga và châu Âu tới nghệ thuật đương đại của các danh hoạ Altai. Bộ sưu tập được trưng bày trong toà nhà bảo tàng hiện đại mới trên đại lộ Lenin.",
    "Thành lập năm 1958, Bảo tàng Mỹ thuật quốc gia vùng Altai là kho tàng nghệ thuật lớn nhất của cả vùng, sở hữu hơn mười lăm nghìn tác phẩm trải dài nhiều thế kỷ. Bộ sưu tập bao gồm những thánh tượng Chính Thống giáo cổ từ thế kỷ 16-18, tranh và tượng của các bậc thầy hội hoạ Nga, nghệ thuật trang trí - ứng dụng, cùng mỹ thuật châu Âu. Đặc biệt quý giá là mảng tác phẩm của các hoạ sĩ gốc Altai, trong đó có Grigory Choros-Gurkin - hoạ sĩ dân tộc Altai nổi tiếng với những bức tranh phong cảnh núi non hùng vĩ. Sau nhiều năm cải tạo, bảo tàng đã chuyển về một toà nhà trưng bày hiện đại rộng rãi trên đại lộ Lenin, nơi các không gian triển lãm được thiết kế theo chuẩn bảo tàng đương đại. Đây là điểm đến không thể bỏ qua cho những ai muốn cảm nhận đời sống nghệ thuật và tâm hồn sáng tạo của vùng đất Altai. Bảo tàng cũng thường xuyên tổ chức các triển lãm chuyên đề và hoạt động giáo dục nghệ thuật.",
    [
        "Bảo tàng mỹ thuật lớn nhất vùng Altai, hơn mười lăm nghìn tác phẩm.",
        "Sưu tập thánh tượng cổ, hội hoạ Nga - châu Âu và mỹ thuật đương đại Altai.",
        "Trưng bày tranh của Grigory Choros-Gurkin - danh hoạ dân tộc Altai.",
    ],
    {
        "hours_vi": "Thường mở cửa thứ Ba–Chủ nhật, nghỉ thứ Hai; nên kiểm tra lịch trước khi đến.",
        "ticket_vi": "Vé vào cửa giá phải chăng; triển lãm chuyên đề có thể thu phí riêng.",
        "duration_vi": "Khoảng 1,5–2 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Nằm trên trục đại lộ Lenin, dễ kết hợp với dạo phố và tham quan trung tâm Barnaul.",
    },
    [
        {"title": "Wikipedia (RU) — Государственный художественный музей Алтайского края", "url": "https://ru.wikipedia.org/wiki/Государственный_художественный_музей_Алтайского_края"},
        {"title": "Культура.РФ — Государственный художественный музей Алтайского края", "url": "https://www.culture.ru/institutes/11240/gosudarstvennyi-khudozhestvennyi-muzei-altaiskogo-kraya"},
    ],
    ["museum", "art", "barnaul", "painting", "icons", "gurkin", "altai"],
    maps_text("Государственный художественный музей Алтайского края", "Барнаул", "State Art Museum of Altai Krai", "Barnaul", 53.356433, 83.769028),
))

# 3) Горная аптека (музей-ресторан) -----------------------------------------------
RECORDS.append(rec(
    "gornaya-apteka-barnaul",
    "Hiệu thuốc Núi - toà nhà đá cổ nhất Barnaul (Gornaya Apteka)",
    "Горная аптека",
    "Gornaya Apteka (Mining Pharmacy)",
    ["other", "museum"],
    53.329970, 83.789042,
    "Ул. Ползунова, 42, trung tâm lịch sử thành phố Barnaul, vùng Altai, Nga.",
    "Toà nhà bằng đá cổ nhất còn lại của Barnaul, xây từ cuối thế kỷ 18 làm hiệu thuốc phục vụ các nhà máy mỏ Altai. Ngày nay là bảo tàng dược liệu kết hợp nhà hàng mang phong vị lịch sử.",
    "Nằm trong khu trung tâm lịch sử Barnaul, Hiệu thuốc Núi (Gornaya Apteka) là công trình bằng đá cổ nhất còn tồn tại của thành phố, được dựng vào những năm 1790. Trong hơn một thế kỷ, đây là hiệu thuốc trung tâm phục vụ toàn bộ hệ thống nhà máy khai mỏ - luyện bạc Kolyvan-Voskresensk, nơi bào chế và cấp phát dược phẩm cho công nhân và quan chức khu mỏ. Bên cạnh toà nhà từng có vườn cây thuốc trồng các loài thảo mộc chữa bệnh của vùng Altai. Sau khi được trùng tu công phu, công trình nay trở thành một tổ hợp văn hoá độc đáo gồm bảo tàng nhỏ tái hiện nghề dược cổ với các bình lọ, cân, dụng cụ bào chế, cùng một nhà hàng và cửa hàng bán trà thảo mộc, mật ong, siro và đặc sản Altai. Không gian gạch đá mộc mạc, trần vòm cổ kính đưa du khách trở về bầu không khí của một đô thị mỏ Siberia thế kỷ 18-19. Đây là điểm dừng chân thú vị vừa để tìm hiểu lịch sử, vừa để thưởng thức hương vị dược liệu núi rừng Altai.",
    [
        "Toà nhà bằng đá cổ nhất còn lại của Barnaul (thập niên 1790).",
        "Từng là hiệu thuốc trung tâm của cả hệ thống nhà máy mỏ Altai.",
        "Nay là bảo tàng dược liệu kết hợp nhà hàng và cửa hàng đặc sản thảo mộc.",
    ],
    {
        "hours_vi": "Cửa hàng và nhà hàng mở hằng ngày theo giờ phục vụ; khu bảo tàng nhỏ có thể xem kèm.",
        "ticket_vi": "Vào tham quan/cửa hàng miễn phí; ăn uống và mua đặc sản tính theo thực đơn.",
        "duration_vi": "Khoảng 30–60 phút.",
        "best_time_vi": "Quanh năm; tiện ghé cùng buổi dạo khu trung tâm lịch sử.",
        "tips_vi": "Thử trà thảo mộc và mật ong Altai; nằm sát Bảo tàng địa phương và Quảng trường Demidov.",
    },
    [
        {"title": "Wikipedia (RU) — Горная аптека (Барнаул)", "url": "https://ru.wikipedia.org/wiki/Горная_аптека"},
        {"title": "VisitAltai — Горная аптека", "url": "https://visitaltai.info/"},
    ],
    ["historic-building", "pharmacy-museum", "barnaul", "heritage", "cuisine", "altai"],
    maps_text("Горная аптека", "Барнаул", "Gornaya Apteka Mining Pharmacy", "Barnaul", 53.329970, 83.789042),
))

# 4) Музей «Мир времени» ----------------------------------------------------------
RECORDS.append(rec(
    "mir-vremeni-museum-barnaul",
    "Bảo tàng «Thế giới thời gian» (Mir Vremeni, Barnaul)",
    "Музей «Мир времени»",
    "Mir Vremeni (World of Time) Museum",
    ["museum"],
    53.365130, 83.752433,
    "Ул. Матросова, 12, thành phố Barnaul, vùng Altai, Nga.",
    "Bảo tàng tư nhân độc đáo của Barnaul với bộ sưu tập đồ vật phong phú, đủ mọi thời đại và chủ đề, được bày biện sống động như một 'ngôi nhà kỳ lạ' của thời gian. Du khách được chạm tay và trải nghiệm nhiều hiện vật thay vì chỉ ngắm nhìn.",
    "Bảo tàng «Thế giới thời gian» là một trong những điểm đến bất ngờ và được yêu thích nhất Barnaul - một bảo tàng tư nhân sinh ra từ bộ sưu tập cả đời của người sáng lập. Không gian nơi đây không theo lối trưng bày hàn lâm khô khan, mà là một mê cung ấm cúng chất đầy đồ vật thuộc đủ thời đại và lĩnh vực: từ vũ khí cổ, đồ gia dụng, máy móc, nhạc cụ, đồ nội thất quý, tranh tượng cho tới những vật dụng đời thường của thời Xô Viết. Điểm đặc biệt là tinh thần 'chạm được' và tương tác - du khách có thể cầm nắm, thử nghiệm nhiều hiện vật, nghe những câu chuyện sống động phía sau mỗi món đồ. Cách sắp đặt tài tình biến các phòng thành những khung cảnh gợi nhớ các thời kỳ khác nhau, khiến người xem như du hành xuyên thời gian. Đây là nơi thú vị cho cả gia đình, đặc biệt hấp dẫn với trẻ em và những ai mê đồ cổ, đồ sưu tầm. Bảo tàng cho thấy niềm đam mê và sự tinh tế của người Nga trong việc gìn giữ ký ức vật chất của các thế hệ.",
    [
        "Bảo tàng tư nhân độc đáo từ bộ sưu tập cả đời của người sáng lập.",
        "Hiện vật đủ mọi thời đại: vũ khí, đồ gia dụng, máy móc, nhạc cụ, đồ Xô Viết.",
        "Tinh thần tương tác 'chạm được' - phù hợp cả gia đình và trẻ em.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo lịch của bảo tàng; nên gọi/đặt trước dịp đông khách.",
        "ticket_vi": "Vé vào cửa giá bình dân; tour hướng dẫn giúp hiểu rõ hơn các bộ sưu tập.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Đi cùng hướng dẫn viên để nghe chuyện phía sau các hiện vật; hợp cho trẻ nhỏ.",
    },
    [
        {"title": "VisitAltai — Музей «Мир времени»", "url": "https://visitaltai.info/"},
        {"title": "Yandex Maps — Музей «Мир времени»", "url": "https://yandex.ru/maps/org/mir_vremeni/1023474740/"},
    ],
    ["museum", "private-museum", "barnaul", "collection", "interactive", "altai"],
    maps_org("https://yandex.ru/maps/org/mir_vremeni/1023474740/", "Mir Vremeni World of Time Museum", "Barnaul"),
))

# 5) Нагорный парк ----------------------------------------------------------------
RECORDS.append(rec(
    "barnaul-nagorny-park",
    "Công viên Nagorny nhìn ra sông Ob (Barnaul)",
    "Нагорный парк",
    "Nagorny Park",
    ["park_garden"],
    53.324060, 83.795016,
    "Trên đồi cao bên hữu ngạn sông Ob, gần trung tâm thành phố Barnaul, vùng Altai, Nga.",
    "Công viên bậc thang trên ngọn đồi cao bên sông Ob, là điểm ngắm toàn cảnh Barnaul đẹp nhất thành phố. Nổi bật với dòng chữ 'Барнаул' khổng lồ trên sườn đồi và nhà thờ Thánh Gioan Tiền Hô.",
    "Nằm trên ngọn đồi cao bên hữu ngạn sông Ob, Công viên Nagorny là ban công ngắm cảnh tuyệt đẹp của Barnaul. Từ đầu thế kỷ 20 nơi đây từng là khu hội chợ triển lãm, sau đó trở thành nghĩa trang thành phố, rồi được cải tạo toàn diện thành công viên hiện đại vào giữa thập niên 2010. Ngày nay công viên trải theo các bậc thang dẫn lên đỉnh đồi, với những lối dạo lát đá, đài quan sát và điểm chụp ảnh nhìn thẳng ra dòng Ob rộng mênh mông cùng toàn cảnh mái nhà, nhà thờ và cầu của thành phố. Biểu tượng nổi bật là dòng chữ 'Барнаул' cỡ lớn dựng trên sườn đồi theo phong cách các thành phố lớn thế giới, cùng ngôi nhà thờ Thánh Gioan Tiền Hô nhỏ xinh. Người dân địa phương thích lên đây tập thể dục buổi sáng, dạo mát buổi chiều và ngắm hoàng hôn buông trên sông. Vào các dịp lễ, công viên trở thành nơi tụ họp và bắn pháo hoa. Đây là điểm đến lý tưởng để thu vào tầm mắt vẻ đẹp của thủ phủ vùng Altai.",
    [
        "Điểm ngắm toàn cảnh Barnaul và sông Ob đẹp nhất thành phố.",
        "Dòng chữ 'Барнаул' khổng lồ trên sườn đồi và nhà thờ Thánh Gioan Tiền Hô.",
        "Công viên bậc thang với lối dạo, đài quan sát, nơi ngắm hoàng hôn lý tưởng.",
    ],
    {
        "hours_vi": "Công viên ngoài trời, mở tự do quanh năm; đẹp nhất ban ngày và lúc hoàng hôn.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Tháng 5–9 khi ấm áp; buổi chiều tối để ngắm hoàng hôn trên sông Ob.",
        "tips_vi": "Mang giày thoải mái để leo bậc thang; đi lúc chiều muộn để chụp ảnh thành phố lên đèn.",
    },
    [
        {"title": "Wikipedia (RU) — Нагорный парк (Барнаул)", "url": "https://ru.wikipedia.org/wiki/Нагорный_парк_(Барнаул)"},
        {"title": "VisitAltai — Нагорный парк", "url": "https://visitaltai.info/"},
    ],
    ["park", "viewpoint", "barnaul", "ob-river", "cityscape", "altai"],
    maps_text("Нагорный парк", "Барнаул", "Nagorny Park", "Barnaul", 53.324060, 83.795016),
))

# 6) Алтайский краевой театр драмы им. В. М. Шукшина ------------------------------
RECORDS.append(rec(
    "altai-drama-theatre-shukshin",
    "Nhà hát kịch vùng Altai mang tên V. M. Shukshin (Barnaul)",
    "Алтайский краевой театр драмы имени В. М. Шукшина",
    "Altai Regional Drama Theatre named after V. M. Shukshin",
    ["theatre"],
    53.346703, 83.773410,
    "Ул. Молодёжная, 15, thành phố Barnaul, vùng Altai, Nga.",
    "Nhà hát kịch lâu đời nhất vùng Altai, có lịch sử từ năm 1921, mang tên người con nổi tiếng của Altai - Vasily Shukshin. Sân khấu là trung tâm đời sống văn hoá của thủ phủ Barnaul.",
    "Nhà hát kịch vùng Altai là sân khấu kịch nói lâu đời và uy tín nhất của cả vùng, khởi nguồn từ năm 1921. Nhà hát mang tên Vasily Shukshin - nhà văn, đạo diễn, diễn viên huyền thoại sinh ra tại làng Srostki của Altai, như một cách tôn vinh người con vĩ đại của quê hương. Toà nhà bề thế nằm trên một quảng trường ở trung tâm Barnaul, là địa chỉ quen thuộc của người dân yêu nghệ thuật suốt hàng chục năm. Trên sân khấu này, các vở kinh điển của Chekhov, Ostrovsky, Gogol cùng nhiều tác phẩm Nga và thế giới hiện đại được dàn dựng công phu, bên cạnh những vở chuyển thể từ chính tác phẩm của Shukshin. Đoàn kịch của nhà hát nhiều lần lưu diễn và giành giải thưởng, góp phần đưa tên tuổi sân khấu Altai vượt ra ngoài Siberia. Một buổi tối xem kịch tại đây là cách thú vị để hoà vào nhịp sống văn hoá của thành phố; ngay cả khi không thạo tiếng Nga, du khách vẫn cảm nhận được không khí trang trọng và say mê nghệ thuật của khán phòng.",
    [
        "Nhà hát kịch lâu đời nhất vùng Altai, có lịch sử từ năm 1921.",
        "Mang tên Vasily Shukshin - người con nổi tiếng của làng Srostki, Altai.",
        "Dàn dựng kịch kinh điển Nga và các vở chuyển thể từ tác phẩm Shukshin.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch mùa, thường buổi tối và cuối tuần; phòng vé mở ban ngày.",
        "ticket_vi": "Vé giá phải chăng, thay đổi theo vở diễn và hạng ghế.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ.",
        "best_time_vi": "Mùa diễn từ thu đến xuân; xem lịch trên trang chính thức của nhà hát.",
        "tips_vi": "Đặt vé trước cho các vở nổi tiếng; đến sớm để gửi áo khoác mùa đông ở quầy garderob.",
    },
    [
        {"title": "Wikipedia (RU) — Алтайский краевой театр драмы имени В. М. Шукшина", "url": "https://ru.wikipedia.org/wiki/Алтайский_краевой_театр_драмы_имени_В._М._Шукшина"},
        {"title": "Культура.РФ — Алтайский краевой театр драмы", "url": "https://www.culture.ru/"},
    ],
    ["theatre", "drama", "barnaul", "shukshin", "culture", "altai"],
    maps_text("Алтайский краевой театр драмы имени В. М. Шукшина", "Барнаул", "Altai Regional Drama Theatre", "Barnaul", 53.346703, 83.773410),
))

# 7) Алтайский государственный музыкальный театр ---------------------------------
RECORDS.append(rec(
    "altai-musical-theatre-barnaul",
    "Nhà hát Nhạc kịch quốc gia Altai (Barnaul)",
    "Алтайский государственный музыкальный театр",
    "Altai State Musical Theatre",
    ["theatre"],
    53.350425, 83.783970,
    "Комсомольский проспект, 108, thành phố Barnaul, vùng Altai, Nga.",
    "Nhà hát nhạc kịch của vùng Altai, chuyên dàn dựng operetta, nhạc kịch (musical) và các vở diễn ca nhạc sôi động. Một trong những sân khấu giải trí được yêu thích nhất Barnaul.",
    "Thành lập vào năm 1960 với tiền thân là nhà hát operetta, Nhà hát Nhạc kịch quốc gia Altai mang đến cho Barnaul một sân khấu ca nhạc rực rỡ và sống động. Nơi đây dàn dựng đủ thể loại: từ operetta cổ điển của Kalman, Strauss, tới các vở nhạc kịch (musical) hiện đại, opera dân gian và những chương trình ca nhạc dành cho thiếu nhi. Toà nhà nhà hát nằm trên đại lộ Komsomolsky, với khán phòng khang trang và dàn nhạc, ca sĩ, vũ đoàn được đào tạo bài bản. Sự kết hợp giữa âm nhạc, vũ đạo và sân khấu tạo nên những buổi diễn giàu màu sắc, dễ tiếp cận với cả du khách nước ngoài bởi ngôn ngữ của giai điệu vượt qua rào cản tiếng nói. Nhà hát là điểm đến lý tưởng cho một buổi tối thư giãn, thưởng thức nghệ thuật biểu diễn của vùng Altai. Đây cũng là nơi diễn ra nhiều liên hoan và sự kiện văn hoá âm nhạc của thành phố.",
    [
        "Nhà hát nhạc kịch của vùng Altai, thành lập năm 1960 từ nhà hát operetta.",
        "Dàn dựng operetta cổ điển, nhạc kịch hiện đại và chương trình ca nhạc thiếu nhi.",
        "Sân khấu ca - vũ - nhạc rực rỡ, dễ thưởng thức với cả du khách nước ngoài.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch mùa, thường buổi tối và cuối tuần; phòng vé mở ban ngày.",
        "ticket_vi": "Vé giá phải chăng, thay đổi theo vở diễn và hạng ghế.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ.",
        "best_time_vi": "Mùa diễn từ thu đến xuân; xem lịch trên trang chính thức của nhà hát.",
        "tips_vi": "Operetta và nhạc kịch dễ xem cho người không rành tiếng Nga; đặt vé sớm cho suất cuối tuần.",
    },
    [
        {"title": "Wikipedia (RU) — Алтайский государственный музыкальный театр", "url": "https://ru.wikipedia.org/wiki/Алтайский_государственный_музыкальный_театр"},
        {"title": "Культура.РФ — Алтайский государственный музыкальный театр", "url": "https://www.culture.ru/"},
    ],
    ["theatre", "operetta", "musical", "barnaul", "culture", "altai"],
    maps_text("Алтайский государственный музыкальный театр", "Барнаул", "Altai State Musical Theatre", "Barnaul", 53.350425, 83.783970),
))

# 8) Мемориал Славы (площадь Победы) ----------------------------------------------
RECORDS.append(rec(
    "barnaul-memorial-slavy",
    "Đài tưởng niệm Vinh quang tại Quảng trường Chiến thắng (Barnaul)",
    "Мемориал Славы",
    "Memorial of Glory (Victory Square)",
    ["monument", "square_street"],
    53.350070, 83.759600,
    "Площадь Победы (Quảng trường Chiến thắng), thành phố Barnaul, vùng Altai, Nga.",
    "Quần thể đài tưởng niệm chính của Barnaul dành cho những người con Altai đã hy sinh trong Chiến tranh Vệ quốc Vĩ đại. Nổi bật với ngọn lửa vĩnh cửu và các trụ đài phù điêu cao lớn trên Quảng trường Chiến thắng.",
    "Đài tưởng niệm Vinh quang trên Quảng trường Chiến thắng là công trình tưởng niệm quan trọng nhất của Barnaul, khánh thành trong những năm đầu thập niên 1970 để tri ân hàng trăm nghìn người con Altai đã ngã xuống trong Chiến tranh Vệ quốc Vĩ đại (1941-1945). Trung tâm quần thể là ngọn lửa vĩnh cửu cháy không tắt, được canh giữ trang nghiêm, cùng hai trụ đài bê tông cao lớn khắc những bức phù điêu tái hiện cảnh tiễn đưa ra trận và niềm vui chiến thắng. Trên quảng trường còn có bức tượng người mẹ và người lính, cùng những phiến đá khắc tên các đơn vị và anh hùng quê hương Altai. Đây là nơi diễn ra lễ đặt hoa, duyệt binh và các nghi thức trọng thể vào Ngày Chiến thắng 9 tháng 5, khi hàng nghìn người dân tụ hội. Không gian rộng rãi, trang nghiêm của quảng trường cũng là điểm dừng chân để du khách hiểu về ký ức chiến tranh và lòng biết ơn sâu sắc của người dân Nga. Với người Việt, đây là nơi gợi nhắc những giá trị chung về hoà bình và tưởng nhớ.",
    [
        "Đài tưởng niệm chính của Barnaul với ngọn lửa vĩnh cửu canh giữ trang nghiêm.",
        "Hai trụ đài phù điêu cao lớn tái hiện cảnh tiễn quân và ngày chiến thắng.",
        "Trung tâm các nghi lễ trọng thể vào Ngày Chiến thắng 9 tháng 5.",
    ],
    {
        "hours_vi": "Quảng trường ngoài trời, mở tự do quanh năm; trang nghiêm nhất vào các dịp lễ.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Quanh năm; đặc biệt ý nghĩa vào Ngày Chiến thắng 9/5.",
        "tips_vi": "Giữ thái độ trang nghiêm gần ngọn lửa vĩnh cửu; buổi tối quảng trường được chiếu sáng đẹp.",
    },
    [
        {"title": "Wikipedia (RU) — Мемориал Славы (Барнаул)", "url": "https://ru.wikipedia.org/wiki/Мемориал_Славы_(Барнаул)"},
        {"title": "Yandex Maps — Мемориал Славы", "url": "https://yandex.ru/maps/org/memorial_slavy/80335652178/"},
    ],
    ["memorial", "wwii", "barnaul", "eternal-flame", "victory-square", "altai"],
    maps_org("https://yandex.ru/maps/org/memorial_slavy/80335652178/", "Memorial of Glory Victory Square", "Barnaul"),
))

# 9) Никольская церковь (Барнаул) -------------------------------------------------
RECORDS.append(rec(
    "barnaul-nikolskaya-church",
    "Nhà thờ Thánh Nikolai (Nikolskaya, Barnaul)",
    "Никольская церковь",
    "St. Nicholas Church (Barnaul)",
    ["church"],
    53.341559, 83.784876,
    "Пр. Ленина, 36, thành phố Barnaul, vùng Altai, Nga.",
    "Ngôi nhà thờ gạch đỏ duyên dáng trên đại lộ Lenin, xây năm 1904 làm nhà thờ trung đoàn của đồn trú Barnaul. Kiến trúc Nga - Byzantine với những mái vòm xanh là một điểm nhấn của phố chính.",
    "Nhà thờ Thánh Nikolai là một trong những công trình tôn giáo đẹp và dễ nhận biết nhất trên đại lộ Lenin của Barnaul. Được xây dựng vào năm 1904 làm nhà thờ trung đoàn phục vụ binh lính của đồn trú thành phố, ngôi thánh đường mang phong cách Nga - Byzantine với thân gạch đỏ nổi bật, viền trang trí trắng và những mái vòm xanh thanh thoát. Sau Cách mạng, nhà thờ bị đóng cửa và trải qua thời gian dài bị dùng làm câu lạc bộ quân đội, mất đi tháp chuông và các vòm. Đến thập niên 1990, công trình được trả lại cho Giáo hội Chính Thống và trùng tu, phục hồi gần như trọn vẹn diện mạo ban đầu, trở lại là nơi hành lễ sầm uất. Ngày nay, giữa nhịp phố hiện đại, ngôi nhà thờ gạch đỏ vẫn giữ nét cổ kính duyên dáng, là điểm dừng chân để du khách chiêm ngưỡng kiến trúc tôn giáo Nga và cảm nhận không gian tâm linh. Vị trí ngay trên trục phố chính khiến nhà thờ rất dễ ghé thăm khi dạo bộ trung tâm Barnaul.",
    [
        "Nhà thờ gạch đỏ kiểu Nga - Byzantine xây năm 1904, mái vòm xanh nổi bật.",
        "Vốn là nhà thờ trung đoàn của đồn trú Barnaul thời Sa hoàng.",
        "Được trùng tu phục hồi thập niên 1990, nằm ngay trên đại lộ Lenin.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp lễ lớn của Chính Thống giáo.",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; giữ yên lặng và xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Sobory.ru — Барнаул, Церковь Николая Чудотворца", "url": "https://sobory.ru/article/?object=09825"},
        {"title": "Wikipedia (RU) — Никольская церковь (Барнаул)", "url": "https://ru.wikipedia.org/wiki/Никольская_церковь_(Барнаул)"},
    ],
    ["church", "orthodox", "barnaul", "red-brick", "garrison-church", "altai"],
    maps_text("Никольская церковь", "Барнаул", "St. Nicholas Church", "Barnaul", 53.341559, 83.784876),
))

# 10) Успенский кафедральный собор (Бийск) ----------------------------------------
RECORDS.append(rec(
    "biysk-assumption-cathedral",
    "Nhà thờ chính toà Đức Mẹ An Nghỉ (Uspensky sobor, Biysk)",
    "Успенский кафедральный собор",
    "Assumption Cathedral (Biysk)",
    ["church"],
    52.544397, 85.232343,
    "Ул. Советская, 13, thành phố Biysk, vùng Altai, Nga.",
    "Nhà thờ chính toà của Biysk, xây đầu thế kỷ 20 bằng gạch đỏ theo phong cách Nga - Byzantine. Ngôi thánh đường năm vòm là trung tâm tôn giáo và một biểu tượng kiến trúc của thành phố cổ Biysk.",
    "Nhà thờ chính toà Đức Mẹ An Nghỉ là ngôi thánh đường Chính Thống giáo quan trọng nhất của Biysk - thành phố cổ thứ hai của vùng Altai và là điểm khởi đầu con đường huyền thoại Chuysky Trakt. Được xây dựng trong những năm 1898-1903 bằng gạch đỏ theo phong cách Nga - Byzantine, nhà thờ nổi bật với khối kiến trúc bề thế, năm mái vòm và tháp chuông vươn cao. Đây là một trong số ít nhà thờ ở Altai không bị phá huỷ hoàn toàn dưới thời Xô Viết; sau khi nhà thờ chính cũ của thành phố bị dỡ bỏ, Uspensky đã trở thành nhà thờ chính toà, giữ vai trò trung tâm đời sống tôn giáo của cả vùng nam Altai suốt nhiều thập niên. Bên trong lưu giữ những bức bích hoạ, thánh tượng được tôn kính và không gian thờ phụng trang nghiêm. Nằm trong khu phố thương gia cổ kính của Biysk, nhà thờ là điểm nhấn kiến trúc dễ nhận thấy và là nơi du khách có thể cảm nhận bề dày lịch sử của một đô thị buôn bán vùng biên. Đây cũng là điểm dừng chân ý nghĩa trước khi khởi hành khám phá Chuysky Trakt.",
    [
        "Nhà thờ chính toà của Biysk, kiến trúc gạch đỏ Nga - Byzantine (1898-1903).",
        "Một trong ít nhà thờ Altai không bị phá huỷ hoàn toàn thời Xô Viết.",
        "Điểm nhấn tâm linh của thành phố cổ Biysk - cửa ngõ Chuysky Trakt.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp lễ lớn của Chính Thống giáo.",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; kết hợp dạo khu phố thương gia cổ và bảo tàng Biysk.",
    },
    [
        {"title": "Sobory.ru — Бийск, Собор Успения Пресвятой Богородицы", "url": "https://sobory.ru/article/?object=12116"},
        {"title": "Wikipedia (RU) — Успенский собор (Бийск)", "url": "https://ru.wikipedia.org/wiki/Успенский_собор_(Бийск)"},
    ],
    ["church", "cathedral", "orthodox", "biysk", "red-brick", "altai"],
    maps_text("Успенский кафедральный собор", "Бийск", "Assumption Cathedral", "Biysk", 52.544397, 85.232343),
))

# 11) Музей истории развития горного производства (Змеиногорск) -------------------
RECORDS.append(rec(
    "zmeinogorsk-mining-museum",
    "Bảo tàng lịch sử ngành khai mỏ Zmeinogorsk",
    "Музей истории развития горного производства имени Акинфия Демидова",
    "Museum of the History of Mining (Zmeinogorsk)",
    ["museum"],
    51.154228, 82.201242,
    "Ул. Щорса, 13, thành phố Zmeinogorsk, vùng Altai, Nga.",
    "Bảo tàng kể về Zmeinogorsk - mỏ bạc giàu có bậc nhất của đế quốc Nga thế kỷ 18-19. Mang tên nhà công nghiệp Akinfiy Demidov, nơi đây trưng bày di sản kỹ thuật khai mỏ và luyện kim độc đáo của Altai.",
    "Thành phố nhỏ Zmeinogorsk từng là 'kho báu' của đế quốc Nga - nơi có mỏ bạc Zmeevsky giàu có bậc nhất, cung cấp phần lớn bạc và vàng cho triều đình Sa hoàng suốt thế kỷ 18-19. Bảo tàng lịch sử ngành khai mỏ, mang tên nhà công nghiệp Akinfiy Demidov, lưu giữ và kể lại câu chuyện phi thường ấy. Bộ sưu tập trưng bày các mẫu quặng, dụng cụ khai mỏ, bản đồ hầm lò và mô hình những công trình kỹ thuật tài tình của vùng - đặc biệt là hệ thống thuỷ lực và cỗ máy nâng do kỹ sư thiên tài Kozma Frolov thiết kế, được xem là kỳ tích công nghệ của thời đại. Du khách được tìm hiểu về đời sống thợ mỏ, công nghệ luyện bạc và vai trò của Zmeinogorsk trong lịch sử công nghiệp Nga. Bản thân thị trấn cũng còn lưu dấu các di tích khai mỏ cổ, đập nước và hầm lò. Đây là điểm đến hấp dẫn cho những ai yêu lịch sử kỹ thuật và muốn khám phá một trang sử ít biết nhưng vô cùng quan trọng của vùng Altai.",
    [
        "Kể về Zmeinogorsk - mỏ bạc giàu có bậc nhất của đế quốc Nga thế kỷ 18-19.",
        "Trưng bày công trình thuỷ lực và cỗ máy nâng tài tình của kỹ sư Kozma Frolov.",
        "Mẫu quặng, dụng cụ khai mỏ và câu chuyện đời sống thợ mỏ Altai.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà); mùa ấm tiện kết hợp thăm di tích mỏ ngoài trời.",
        "tips_vi": "Kết hợp dạo thị trấn Zmeinogorsk cổ, xem đập nước và dấu tích hầm mỏ lịch sử.",
    },
    [
        {"title": "Wikipedia (RU) — Змеиногорск", "url": "https://ru.wikipedia.org/wiki/Змеиногорск"},
        {"title": "Культура.РФ — Музей истории развития горного производства", "url": "https://www.culture.ru/"},
    ],
    ["museum", "mining-history", "zmeinogorsk", "silver", "frolov", "altai"],
    maps_text("Музей истории развития горного производства имени Акинфия Демидова", "Змеиногорск", "Museum of the History of Mining", "Zmeinogorsk", 51.154228, 82.201242),
))

# 12) Колыванский камнерезный завод -----------------------------------------------
RECORDS.append(rec(
    "kolyvan-stone-cutting-factory",
    "Nhà máy chế tác đá quý Kolyvan (Kolyvanskiy zavod)",
    "Колыванский камнерезный завод имени И. И. Ползунова",
    "Kolyvan Stone-Cutting Factory",
    ["other", "museum"],
    51.317750, 82.571514,
    "Làng Kolyvan, huyện Kuryinsky, vùng Altai, Nga.",
    "Nhà máy chế tác đá quý huyền thoại của Altai, nơi tạo ra 'Nữ hoàng của các bình hoa' - chiếc bình jasper khổng lồ nay đặt tại Bảo tàng Hermitage. Cơ sở còn có bảo tàng nghề chạm khắc đá lừng danh.",
    "Nằm ở làng Kolyvan dưới chân dãy núi cùng tên, Nhà máy chế tác đá quý Kolyvan là một trong những cơ sở chạm khắc đá cổ và danh tiếng nhất nước Nga, hoạt động từ đầu thế kỷ 19. Chính tại đây, những người thợ Altai đã chế tác nên vô số kiệt tác từ jasper, porphyr và các loại đá màu quý của vùng, cung cấp cho các cung điện và bảo tàng ở Sankt-Peterburg. Tuyệt phẩm lừng danh nhất là 'Nữ hoàng của các bình hoa' (Tsaritsa vaz) - chiếc bình bằng jasper xanh khổng lồ nặng khoảng 19 tấn, phải mất nhiều năm để chế tác và vận chuyển, nay là báu vật trưng bày tại Bảo tàng Hermitage và trở thành biểu tượng in trên huy hiệu vùng Altai. Nhà máy đến nay vẫn tiếp nối truyền thống chạm khắc đá, và có một bảo tàng nhỏ giới thiệu lịch sử, công cụ cùng các tác phẩm đá tinh xảo. Du khách đến đây được chiêm ngưỡng nghề thủ công độc đáo, tìm hiểu hành trình của những khối đá thô trở thành tác phẩm nghệ thuật, và cảm nhận niềm tự hào của người Altai với di sản đá quý của mình.",
    [
        "Nơi tạo ra 'Nữ hoàng của các bình hoa' - bình jasper 19 tấn ở Hermitage.",
        "Một trong những cơ sở chạm khắc đá quý cổ và danh tiếng nhất nước Nga.",
        "Có bảo tàng nghề chạm khắc đá với công cụ và tác phẩm tinh xảo.",
    ],
    {
        "hours_vi": "Bảo tàng nhà máy mở theo giờ hành chính, thường trong tuần; nên liên hệ/đặt trước.",
        "ticket_vi": "Vé vào bảo tàng giá bình dân; tham quan xưởng cần đăng ký trước.",
        "duration_vi": "Khoảng 1 giờ.",
        "best_time_vi": "Mùa ấm (tháng 5–9) tiện đường; có thể ghép với hồ Beloye và núi Sinyukha gần đó.",
        "tips_vi": "Làng ở xa, nên đi ô tô riêng; kết hợp tham quan hồ Beloye, núi Sinyukha cùng cụm Kolyvan.",
    },
    [
        {"title": "Wikipedia (RU) — Колыванская шлифовальная фабрика", "url": "https://ru.wikipedia.org/wiki/Колыванская_шлифовальная_фабрика"},
        {"title": "VisitAltai — Колыванский камнерезный завод", "url": "https://visitaltai.info/"},
    ],
    ["stone-carving", "craft", "kolyvan", "jasper", "hermitage-vase", "museum", "altai"],
    maps_text("Колыванский камнерезный завод имени И. И. Ползунова", "Курьинский район, Алтайский край", "Kolyvan Stone-Cutting Factory", "Kolyvan", 51.317750, 82.571514),
))

# 13) Гора Синюха ------------------------------------------------------------------
RECORDS.append(rec(
    "mount-sinyukha",
    "Núi Sinyukha - đỉnh cao nhất dãy Kolyvan (Sinyukha)",
    "Гора Синюха",
    "Mount Sinyukha",
    ["park_garden"],
    51.241084, 82.606356,
    "Huyện Kuryinsky, dãy Kolyvan, vùng Altai, Nga (đỉnh cao khoảng 1210 m).",
    "Đỉnh núi cao nhất của dãy Kolyvan (khoảng 1210 m), nổi bật với những khối đá granit kỳ vĩ và sắc xanh lam nhìn từ xa. Là điểm leo núi và hành hương nổi tiếng với cây thánh giá cùng nguồn nước thiêng trên đỉnh.",
    "Núi Sinyukha là đỉnh cao nhất của dãy Kolyvan ở tây nam vùng Altai, vươn lên khoảng 1210 mét giữa vùng thảo nguyên và rừng. Tên gọi 'Sinyukha' (nghĩa là 'màu xanh lam') bắt nguồn từ sắc xanh mờ ảo của ngọn núi khi nhìn từ xa, do rừng thông và lớp đá granit phủ sương. Sườn núi rải rác những khối đá granit khổng lồ bị phong hoá thành hình thù kỳ lạ, xen giữa rừng cây và đồng cỏ hoa. Trên đỉnh có một cây thánh giá Chính Thống giáo và những vũng nước đọng trong hốc đá được người hành hương xem là nước thiêng, khiến Sinyukha vừa là điểm leo núi hấp dẫn, vừa là nơi hành hương tâm linh. Đường lên đỉnh không quá khó, phù hợp với du khách có sức khoẻ trung bình, và phần thưởng là tầm nhìn bao la xuống hồ Beloye, làng Kolyvan cùng biển thảo nguyên trải dài tới tận chân trời. Vào mùa hè, cả sườn núi bừng nở hoa dại, còn không khí trong lành và khung cảnh hùng vĩ khiến Sinyukha trở thành một trong những điểm đến thiên nhiên được yêu thích nhất vùng Altai Krai.",
    [
        "Đỉnh cao nhất dãy Kolyvan (khoảng 1210 m) với sắc xanh lam đặc trưng.",
        "Những khối đá granit khổng lồ hình thù kỳ lạ xen giữa rừng và đồng hoa.",
        "Cây thánh giá và nguồn nước thiêng trên đỉnh - điểm hành hương và leo núi.",
    ],
    {
        "hours_vi": "Núi tự nhiên, leo tự do ban ngày; nên khởi hành sớm để kịp lên đỉnh và xuống trong ngày.",
        "ticket_vi": "Miễn phí; một số khu cắm trại hoặc dịch vụ dưới chân núi có thể thu phí.",
        "duration_vi": "Nửa ngày đến 1 ngày cho hành trình leo lên đỉnh và trở về.",
        "best_time_vi": "Tháng 6 đến tháng 9, khi thời tiết khô ráo và hoa dại nở rộ.",
        "tips_vi": "Mang giày leo núi, nước, đồ chống ve và áo ấm nhẹ vì đỉnh nhiều gió; kết hợp thăm hồ Beloye.",
    },
    [
        {"title": "Wikipedia (RU) — Синюха (гора)", "url": "https://ru.wikipedia.org/wiki/Синюха_(гора)"},
        {"title": "VisitAltai — Гора Синюха", "url": "https://visitaltai.info/"},
    ],
    ["mountain", "nature", "hiking", "granite", "pilgrimage", "kolyvan", "altai"],
    maps_text("Гора Синюха", "Курьинский район, Алтайский край", "Mount Sinyukha", "Kurya", 51.241084, 82.606356),
))

# 14) Белое озеро (Курьинский район) ----------------------------------------------
RECORDS.append(rec(
    "beloye-lake-kurya",
    "Hồ Beloye (Bạch Hồ) gần Kolyvan",
    "Белое озеро",
    "Beloye (White) Lake",
    ["park_garden"],
    51.293668, 82.648677,
    "Gần làng Kolyvan, huyện Kuryinsky, vùng Altai, Nga.",
    "Hồ nước ngọt tròn trịa nằm giữa vùng núi granit của dãy Kolyvan, với một mỏm đá đảo nổi giữa hồ gắn với truyền thuyết đúc bạc bí mật của Demidov. Điểm cắm trại và tắm mát được yêu thích ở tây nam Altai.",
    "Hồ Beloye là một trong những hồ đẹp và giàu huyền thoại nhất của vùng núi Kolyvan ở tây nam Altai. Hồ có hình gần tròn, đường kính chừng 3 km, làn nước trong lành được bao quanh bởi những sườn núi granit và rừng thông. Điểm đặc biệt nhất là một mỏm đá granit nhô lên giữa lòng hồ như một hòn đảo nhỏ; tương truyền vào thế kỷ 18, nhà công nghiệp Akinfiy Demidov đã cho lập một xưởng đúc bí mật trên đảo đá này để lén luyện bạc mà không nộp cho triều đình - câu chuyện khiến hồ Beloye phủ thêm màu sắc ly kỳ. Nước hồ mát và sạch, ven bờ có bãi thoải thích hợp để tắm vào mùa hè, còn khung cảnh núi đá phản chiếu trên mặt nước tạo nên những bức tranh thiên nhiên tuyệt đẹp. Du khách đến đây để bơi lội, chèo thuyền, câu cá, cắm trại và leo trèo khám phá các mỏm đá. Nằm gần làng Kolyvan và núi Sinyukha, hồ Beloye là một mắt xích lý tưởng trong hành trình khám phá cụm thắng cảnh Kolyvan của vùng Altai Krai.",
    [
        "Hồ nước ngọt tròn trịa giữa vùng núi granit của dãy Kolyvan.",
        "Đảo đá giữa hồ gắn với truyền thuyết xưởng đúc bạc bí mật của Demidov.",
        "Nước trong mát, bãi thoải để tắm, chèo thuyền và cắm trại mùa hè.",
    ],
    {
        "hours_vi": "Hồ tự nhiên, tham quan tự do quanh năm; sôi động nhất vào mùa hè.",
        "ticket_vi": "Vào hồ miễn phí; các khu cắm trại và dịch vụ quanh hồ thu phí riêng.",
        "duration_vi": "Nửa ngày đến 1 ngày; hoặc nghỉ qua đêm nếu cắm trại.",
        "best_time_vi": "Tháng 6 đến tháng 8, khi nước đủ ấm để tắm.",
        "tips_vi": "Mang theo nước, thực phẩm và đồ dùng vì tiện nghi hạn chế; ghép cùng núi Sinyukha và làng Kolyvan.",
    },
    [
        {"title": "Wikipedia (RU) — Белое озеро (Алтайский край)", "url": "https://ru.wikipedia.org/wiki/Белое_озеро_(Алтайский_край)"},
        {"title": "VisitAltai — Белое озеро", "url": "https://visitaltai.info/"},
    ],
    ["lake", "nature", "granite", "swimming", "camping", "kolyvan", "altai"],
    maps_text("Белое озеро", "Курьинский район, Алтайский край", "Beloye White Lake", "Kurya", 51.293668, 82.648677),
))

# 15) Озеро Ая --------------------------------------------------------------------
RECORDS.append(rec(
    "lake-aya",
    "Hồ Aya bên tả ngạn sông Katun (Aya)",
    "Озеро Ая",
    "Lake Aya",
    ["park_garden"],
    51.904794, 85.853738,
    "Huyện Altaysky, tả ngạn sông Katun, vùng Altai, Nga.",
    "Hồ nước ấm hiếm có bên tả ngạn sông Katun, với làn nước ấm áp lý tưởng để tắm và một hòn đảo nhỏ có đình nghỉ giữa hồ. Một trong những khu nghỉ mát và tắm hồ được yêu thích nhất vùng chân núi Altai.",
    "Hồ Aya là viên ngọc nhỏ nằm bên tả ngạn sông Katun thuộc huyện Altaysky, ngay cửa ngõ dẫn vào vùng núi Altai. Điều làm nên tên tuổi của hồ là làn nước ấm áp đặc biệt: hồ không có dòng chảy vào hay ra rõ rệt nên nước được mặt trời hâm nóng tới khoảng 20-22°C vào mùa hè, ấm hơn hẳn dòng Katun lạnh giá chảy sát bên - biến Aya thành một trong số ít nơi có thể tắm thoải mái ở vùng này. Giữa mặt hồ trong xanh nổi lên một hòn đảo đá nhỏ với đình nghỉ xinh xắn thường được gọi là 'Đảo Tình Yêu', là điểm chụp ảnh biểu tượng. Tên gọi 'Ay' trong tiếng Altai nghĩa là 'mặt trăng', gắn với những truyền thuyết dân gian thơ mộng về hồ. Xung quanh Aya là các sườn núi phủ rừng, bãi tắm, khu nghỉ dưỡng (turbaza) và nhiều hoạt động giải trí như đạp vịt, chèo thuyền, cắm trại. Vào mùa hè, khu vực hồ trở nên nhộn nhịp với du khách từ khắp Siberia đổ về nghỉ mát. Aya là điểm dừng chân lý tưởng để thư giãn, tắm mát và ngắm cảnh thiên nhiên chân núi Altai trước khi tiến sâu vào vùng núi cao.",
    [
        "Làn nước ấm hiếm có (khoảng 20-22°C mùa hè), lý tưởng để tắm.",
        "Hòn đảo nhỏ giữa hồ có đình nghỉ - 'Đảo Tình Yêu' biểu tượng.",
        "Khu nghỉ mát sôi động bên tả ngạn sông Katun, cửa ngõ vùng núi Altai.",
    ],
    {
        "hours_vi": "Hồ tự nhiên, tham quan tự do; bãi tắm và dịch vụ sôi động nhất vào mùa hè.",
        "ticket_vi": "Khu vực hồ có thể thu phí vào cổng/gửi xe theo mùa; dịch vụ bãi tắm tính riêng.",
        "duration_vi": "Nửa ngày đến 1 ngày; hoặc nghỉ dưỡng nhiều ngày tại turbaza quanh hồ.",
        "best_time_vi": "Tháng 6 đến tháng 8, khi nước ấm và thời tiết đẹp.",
        "tips_vi": "Đặt phòng turbaza sớm vào cao điểm hè; kết hợp tham quan sông Katun và các cầu treo gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Ая (озеро)", "url": "https://ru.wikipedia.org/wiki/Ая_(озеро)"},
        {"title": "VisitAltai — Озеро Ая", "url": "https://visitaltai.info/"},
    ],
    ["lake", "nature", "swimming", "resort", "katun", "altai"],
    maps_text("Озеро Ая", "Алтайский район, Алтайский край", "Lake Aya", "Altaysky District", 51.904794, 85.853738),
))

# 16) Малиновое озеро -------------------------------------------------------------
RECORDS.append(rec(
    "malinovoye-lake",
    "Hồ hồng Malinovoye (Malinovoye Ozero)",
    "Малиновое озеро",
    "Malinovoye (Raspberry) Lake",
    ["park_garden"],
    51.678116, 79.789375,
    "Gần làng Malinovoye Ozero, huyện Mikhaylovsky, vùng Altai, Nga.",
    "Hồ nước mặn nổi tiếng với sắc nước hồng - đỏ như quả mâm xôi, do vi sinh vật đặc trưng tạo nên. Muối hồng của hồ từng được tiến cống cho triều đình Sa hoàng và nay là điểm sống ảo độc đáo của vùng thảo nguyên Altai.",
    "Hồ Malinovoye - nghĩa đen là 'Hồ Mâm Xôi' - là một trong những kỳ quan thiên nhiên độc đáo nhất của vùng thảo nguyên Kulunda ở tây Altai. Điều khiến hồ nổi tiếng là màu nước hồng đến đỏ tía kỳ ảo, đặc biệt rực rỡ vào những ngày nắng và tuỳ theo mùa; sắc màu này do một loài vi sinh vật ưa mặn cùng loài tôm nước mặn tí hon sống trong hồ tạo ra. Đây là hồ nước mặn không có dòng chảy ra, giàu khoáng và muối. Từ thế kỷ 18, muối hồng khai thác ở đây được xem là đặc sản quý và tương truyền từng được tiến cống lên bàn tiệc của triều đình Sa hoàng, khiến hồ mang thêm màu sắc lịch sử. Ngày nay, hồ Malinovoye trở thành điểm đến hút khách nhờ khung cảnh siêu thực hiếm có: mặt nước hồng trải rộng giữa thảo nguyên, in bóng mây trời, là phông nền lý tưởng cho những bức ảnh ấn tượng. Du khách còn có thể ngâm mình trong nước mặn nổi bồng bềnh và trải nghiệm lớp bùn khoáng. Dù nằm khá xa và tiện nghi còn giản đơn, vẻ đẹp có một không hai của hồ vẫn thu hút những ai đam mê khám phá thiên nhiên kỳ lạ của Altai Krai.",
    [
        "Mặt nước hồng - đỏ tía kỳ ảo do vi sinh vật ưa mặn tạo nên.",
        "Muối hồng của hồ tương truyền từng được tiến cống triều đình Sa hoàng.",
        "Khung cảnh siêu thực giữa thảo nguyên - điểm chụp ảnh độc đáo bậc nhất Altai.",
    ],
    {
        "hours_vi": "Hồ tự nhiên, tham quan tự do quanh năm; màu hồng đẹp nhất vào ngày nắng mùa hè.",
        "ticket_vi": "Miễn phí; dịch vụ quanh hồ (nếu có) tính riêng.",
        "duration_vi": "1–2 giờ tại hồ; cả ngày nếu tính đường di chuyển xa.",
        "best_time_vi": "Cuối mùa hè (tháng 7–8), khi độ mặn cao và màu nước rực rỡ nhất.",
        "tips_vi": "Mang nước ngọt để tráng người sau khi ngâm; đội mũ, kem chống nắng vì bãi trống; đường xa nên đi ô tô.",
    },
    [
        {"title": "Wikipedia (RU) — Малиновое озеро (Алтайский край)", "url": "https://ru.wikipedia.org/wiki/Малиновое_озеро_(Алтайский_край)"},
        {"title": "VisitAltai — Малиновое озеро", "url": "https://visitaltai.info/"},
    ],
    ["salt-lake", "pink-lake", "nature", "steppe", "photography", "altai"],
    maps_text("Малиновое озеро", "Михайловский район, Алтайский край", "Malinovoye Raspberry Lake", "Mikhaylovsky District", 51.678116, 79.789375),
))

# 17) Кулундинское озеро ----------------------------------------------------------
RECORDS.append(rec(
    "kulundinskoye-lake",
    "Hồ Kulundinskoye - hồ lớn nhất vùng Altai (Kulundinskoye)",
    "Кулундинское озеро",
    "Kulundinskoye Lake",
    ["park_garden"],
    53.000000, 79.516667,
    "Vùng thảo nguyên Kulunda, huyện Blagoveshchensky/Suetsky, vùng Altai, Nga.",
    "Hồ lớn nhất của toàn vùng Altai, một biển nước mặn nông trải rộng giữa thảo nguyên Kulunda. Được người dân gọi thân thương là 'biển Kulunda' với làn nước ấm và bờ cát thoai thoải.",
    "Kulundinskoye là hồ lớn nhất của cả vùng Altai, một mặt nước mặn mênh mông trải rộng khoảng 728 km² giữa vùng thảo nguyên Kulunda bằng phẳng ở phía tây bắc. Do rộng lớn nhưng khá nông (chỉ sâu vài mét), hồ được người dân địa phương trìu mến gọi là 'biển Kulunda'. Nước hồ hơi mặn, giàu khoáng, mùa hè được sưởi ấm nhanh nên rất dễ chịu để tắm, trong khi bờ hồ là những dải cát và bãi thoai thoải trải dài. Xung quanh hồ là cảnh quan thảo nguyên đặc trưng với bầu trời rộng, gió lộng và các đàn chim nước; hồ cũng là nơi sinh sống của loài tôm nước mặn Artemia. Với người dân các vùng thảo nguyên khô hạn quanh đó, Kulundinskoye là điểm nghỉ mát, tắm 'biển' và câu cá quen thuộc mỗi mùa hè. Dù ít tiện nghi du lịch cao cấp, không gian khoáng đạt, làn nước ấm và cảm giác 'ra biển' giữa lòng Siberia mang lại trải nghiệm thư giãn thú vị. Đây là điểm đến hợp với những ai muốn cảm nhận vẻ đẹp bao la, mộc mạc của thiên nhiên thảo nguyên Altai.",
    [
        "Hồ lớn nhất vùng Altai (~728 km²), được gọi là 'biển Kulunda'.",
        "Nước mặn ấm áp, bờ cát thoai thoải lý tưởng để tắm mùa hè.",
        "Cảnh quan thảo nguyên khoáng đạt với chim nước và tôm Artemia.",
    ],
    {
        "hours_vi": "Hồ tự nhiên, tham quan tự do quanh năm; tắm mát vào mùa hè.",
        "ticket_vi": "Miễn phí; dịch vụ quanh hồ (nếu có) tính riêng.",
        "duration_vi": "Nửa ngày đến 1 ngày.",
        "best_time_vi": "Tháng 6 đến tháng 8, khi nước ấm.",
        "tips_vi": "Mang đầy đủ nước uống, thực phẩm và ô che vì bờ hồ trống trải; đường tới hồ khá xa.",
    },
    [
        {"title": "Wikipedia (RU) — Кулундинское озеро", "url": "https://ru.wikipedia.org/wiki/Кулундинское_озеро"},
        {"title": "VisitAltai — Кулундинское озеро", "url": "https://visitaltai.info/"},
    ],
    ["lake", "salt-lake", "largest-lake", "steppe", "swimming", "altai"],
    maps_text("Кулундинское озеро", "Алтайский край", "Kulundinskoye Lake", "Altai Krai", 53.000000, 79.516667),
))

# 18) Лебединое (Светлое) озеро ---------------------------------------------------
RECORDS.append(rec(
    "lebedinoye-svetloye-lake",
    "Hồ Thiên Nga (Svetloye) - khu bảo tồn thiên nga (Lebedinoye)",
    "Лебединое (Светлое) озеро",
    "Lebedinoye (Svetloye) Swan Lake",
    ["park_garden"],
    52.292616, 85.654620,
    "Gần làng Urozhaynoye, huyện Sovetsky, khu bảo tồn 'Lebediny', vùng Altai, Nga.",
    "Hồ nước ấm không đóng băng, nơi hàng trăm con thiên nga kêu (thiên nga whooper) về trú đông giữa mùa đông Siberia băng giá. Một hiện tượng thiên nhiên độc đáo và cảnh tượng thiên nga trên tuyết hiếm có ở Nga.",
    "Hồ Svetloye - thường được gọi là 'Hồ Thiên Nga' (Lebedinoye) - là trái tim của khu bảo tồn thiên nhiên 'Lebediny' gần làng Urozhaynoye, huyện Sovetsky. Điều làm nên sự kỳ diệu của nơi đây là hồ được nuôi dưỡng bởi các mạch nước ngầm ấm nên không bao giờ đóng băng, ngay cả khi nhiệt độ mùa đông Siberia xuống tới âm ba, bốn chục độ. Nhờ vậy, mỗi mùa đông, hàng trăm con thiên nga kêu (whooper swan) cùng vô số vịt trời từ phương bắc kéo về trú đông trên mặt hồ bốc hơi nghi ngút giữa tuyết trắng - một cảnh tượng thiên nhiên hiếm có và vô cùng ngoạn mục. Khu bảo tồn được thành lập từ năm 1973 để bảo vệ đàn thiên nga; ngày nay có đài quan sát và các quy định nghiêm ngặt để du khách ngắm chim mà không làm kinh động chúng. Cảnh những cánh thiên nga trắng muốt in trên nền tuyết và hơi nước mờ ảo đã trở thành biểu tượng thiên nhiên đặc trưng của Altai vào mùa đông. Đây là điểm đến độc nhất vô nhị cho những ai yêu thiên nhiên và muốn chứng kiến một kỳ quan sống động giữa mùa đông nước Nga.",
    [
        "Hồ nước ấm không đóng băng giữa mùa đông Siberia băng giá.",
        "Hàng trăm thiên nga kêu (whooper) về trú đông - cảnh tượng hiếm có.",
        "Khu bảo tồn 'Lebediny' (từ 1973) có đài quan sát ngắm thiên nga trên tuyết.",
    ],
    {
        "hours_vi": "Đài quan sát mở theo mùa, chủ yếu vào mùa đông; nên đi cùng tour có tổ chức.",
        "ticket_vi": "Có thể thu phí vào khu bảo tồn/đài quan sát; giá bình dân.",
        "duration_vi": "Khoảng 1–2 giờ tại đài quan sát; cả ngày nếu tính đường đi.",
        "best_time_vi": "Mùa đông (tháng 12 đến tháng 2), khi đàn thiên nga tụ hội đông nhất.",
        "tips_vi": "Mặc thật ấm và mang ống nhòm/tele; giữ yên lặng, không lại gần để tránh làm kinh động thiên nga.",
    },
    [
        {"title": "Wikipedia (RU) — Лебединый (заказник)", "url": "https://ru.wikipedia.org/wiki/Лебединый_(заказник)"},
        {"title": "VisitAltai — Лебединое озеро", "url": "https://visitaltai.info/"},
    ],
    ["nature-reserve", "swans", "winter", "birdwatching", "svetloye", "altai"],
    maps_text("Лебединое озеро (Светлое)", "Советский район, Алтайский край", "Lebedinoye Svetloye Swan Lake", "Sovetsky District", 52.292616, 85.654620),
))

# 19) Царский курган (Сентелек) ---------------------------------------------------
RECORDS.append(rec(
    "tsarsky-kurgan-sentelek",
    "Gò mộ Hoàng gia Sentelek (Tsarsky Kurgan)",
    "Царский курган (Сентелек)",
    "Tsarsky Kurgan (Royal Mound), Sentelek",
    ["monument"],
    51.185111, 83.689475,
    "Gần làng Sentelek, huyện Charyshsky, vùng Altai, Nga.",
    "Gò mộ hoàng gia thời Scythia (khoảng thế kỷ 6-5 TCN) lớn nhất vùng Altai Krai, với một hàng cột đá thẳng hàng theo mặt trời mọc. Di tích khảo cổ - thiên văn độc đáo giữa thung lũng sông Charysh.",
    "Nằm giữa thung lũng sông Charysh gần làng Sentelek, Gò mộ Hoàng gia (Tsarsky Kurgan) là một trong những di tích khảo cổ ấn tượng nhất của vùng Altai Krai. Đây là ngôi mộ đắp đất kiểu Scythia có niên đại khoảng thế kỷ 6-5 trước Công nguyên, thuộc thời đại đồ sắt sớm gắn với văn hoá Pazyryk lừng danh của Altai. Gò mộ có đường kính lớn, được cho là nơi an nghỉ của một thủ lĩnh hay quý tộc quyền lực. Điều làm nên sự đặc biệt là một hàng gồm nhiều cột đá dựng đứng (menhir) kéo dài về phía đông của gò mộ; các nhà nghiên cứu phát hiện hàng cột này được sắp đặt thẳng hàng theo hướng mặt trời mọc vào những thời điểm quan trọng trong năm, cho thấy người xưa có tri thức thiên văn và dùng nơi đây cho các nghi lễ gắn với chu kỳ mặt trời. Vì thế Tsarsky Kurgan không chỉ là một ngôi mộ, mà còn được xem như một 'đài quan sát' cổ đại. Ngày nay khu di tích được bảo tồn như một công viên khảo cổ ngoài trời, nơi du khách vừa chiêm ngưỡng cảnh núi non thung lũng Charysh, vừa chạm vào bí ẩn của các nền văn minh du mục cổ trên thảo nguyên Altai.",
    [
        "Gò mộ hoàng gia thời Scythia lớn nhất vùng Altai Krai (~thế kỷ 6-5 TCN).",
        "Hàng cột đá menhir thẳng hàng theo mặt trời mọc - di tích khảo cổ thiên văn.",
        "Công viên khảo cổ ngoài trời giữa cảnh núi thung lũng sông Charysh.",
    ],
    {
        "hours_vi": "Di tích ngoài trời, tham quan tự do ban ngày; đường vào xa và hoang sơ.",
        "ticket_vi": "Thường miễn phí; tour hướng dẫn hoặc dịch vụ tại chỗ có thể thu phí.",
        "duration_vi": "Khoảng 1 giờ tại di tích; cả ngày nếu tính đường di chuyển.",
        "best_time_vi": "Tháng 5 đến tháng 9, khi đường khô ráo và thời tiết thuận lợi.",
        "tips_vi": "Đi xe gầm cao vì đường xấu; mang nước, đồ ăn và thuốc chống ve; kết hợp khám phá thung lũng Charysh.",
    },
    [
        {"title": "Wikipedia (RU) — Царский курган (Сентелек)", "url": "https://ru.wikipedia.org/wiki/Царский_курган_(Сентелек)"},
        {"title": "VisitAltai — Царский курган", "url": "https://visitaltai.info/"},
    ],
    ["archaeology", "scythian", "kurgan", "menhirs", "charysh", "altai"],
    maps_text("Царский курган", "Сентелек, Чарышский район", "Tsarsky Kurgan Royal Mound", "Sentelek", 51.185111, 83.689475),
))

# 20) Рубцовский краеведческий музей ----------------------------------------------
RECORDS.append(rec(
    "rubtsovsk-local-lore-museum",
    "Bảo tàng địa phương Rubtsovsk",
    "Рубцовский краеведческий музей",
    "Rubtsovsk Museum of Local Lore",
    ["museum"],
    51.503580, 81.208810,
    "Пр. Ленина, 137А, thành phố Rubtsovsk, vùng Altai, Nga.",
    "Bảo tàng địa phương của Rubtsovsk - đô thị công nghiệp lớn ở nam Altai. Nơi kể về lịch sử khai hoang thảo nguyên, ngành chế tạo máy kéo và đời sống của một thành phố Siberia trẻ trung.",
    "Bảo tàng địa phương Rubtsovsk lưu giữ ký ức của Rubtsovsk - một trong những thành phố lớn của vùng Altai, nằm trên vùng thảo nguyên nam Altai gần biên giới Kazakhstan. Thành phố ra đời từ đầu thế kỷ 20 quanh nhà ga đường sắt và phát triển mạnh trong thời Xô Viết, đặc biệt nhờ nhà máy chế tạo máy kéo Altai (ATZ) từng nổi tiếng khắp Liên bang. Bảo tàng dẫn du khách qua nhiều lớp lịch sử: thiên nhiên và khảo cổ vùng thảo nguyên, những đợt di dân khai hoang, quá trình hình thành thành phố, và giai đoạn công nghiệp hoá với ngành chế tạo máy kéo là niềm tự hào của cư dân. Qua các hiện vật, tài liệu, ảnh và mô hình, bảo tàng khắc hoạ chân dung một đô thị Siberia trẻ trung được dựng nên từ mồ hôi của những người khai hoang và công nhân. Với du khách muốn khám phá Altai vượt ra ngoài thủ phủ Barnaul và các danh thắng thiên nhiên, đây là điểm dừng chân giá trị để hiểu về đời sống công nghiệp và tinh thần lao động của vùng đất thảo nguyên phía nam.",
    [
        "Bảo tàng của Rubtsovsk - đô thị công nghiệp lớn ở nam Altai.",
        "Kể về khai hoang thảo nguyên và ngành chế tạo máy kéo Altai (ATZ) lừng danh.",
        "Điểm tìm hiểu lịch sử địa phương bên ngoài thủ phủ Barnaul.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "Khoảng 1 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Kết hợp dạo trung tâm Rubtsovsk; thành phố nằm trên tuyến tới biên giới Kazakhstan.",
    },
    [
        {"title": "Wikipedia (RU) — Рубцовск", "url": "https://ru.wikipedia.org/wiki/Рубцовск"},
        {"title": "Культура.РФ — Рубцовский краеведческий музей", "url": "https://www.culture.ru/"},
    ],
    ["museum", "local-history", "rubtsovsk", "industry", "steppe", "altai"],
    maps_text("Рубцовский краеведческий музей", "Рубцовск", "Rubtsovsk Museum of Local Lore", "Rubtsovsk", 51.503580, 81.208810),
))

# 21) Рубцовский драматический театр ----------------------------------------------
RECORDS.append(rec(
    "rubtsovsk-drama-theatre",
    "Nhà hát kịch Rubtsovsk",
    "Рубцовский драматический театр",
    "Rubtsovsk Drama Theatre",
    ["theatre"],
    51.510214, 81.207280,
    "Ул. Карла Маркса, 141, thành phố Rubtsovsk, vùng Altai, Nga.",
    "Nhà hát kịch của Rubtsovsk, một trong những sân khấu chuyên nghiệp lâu đời ở vùng Altai ngoài thủ phủ Barnaul. Trung tâm đời sống văn hoá của thành phố công nghiệp nam Altai.",
    "Nhà hát kịch Rubtsovsk là một trong những sân khấu chuyên nghiệp lâu đời của vùng Altai bên ngoài Barnaul, với lịch sử bắt rễ từ những năm 1930. Trong suốt nhiều thập niên, nhà hát là trung tâm đời sống tinh thần của Rubtsovsk - thành phố công nghiệp lớn ở phía nam vùng - nơi công nhân, cư dân và học sinh tìm đến để thưởng thức nghệ thuật sân khấu. Trên sân khấu này, các vở kịch kinh điển của Nga và thế giới, những tác phẩm hiện đại cùng kịch dành cho thiếu nhi được dàn dựng đều đặn, nuôi dưỡng đời sống văn hoá cho một vùng thảo nguyên xa xôi. Đoàn kịch của nhà hát tham gia nhiều liên hoan sân khấu khu vực và góp phần lan toả nghệ thuật kịch nói tới đông đảo khán giả. Với du khách, ghé qua nhà hát hay xem một buổi diễn ở đây là cách thú vị để cảm nhận nhịp sống văn hoá đời thường của một thành phố Siberia, nơi nghệ thuật vẫn được trân trọng giữa bộn bề công nghiệp. Toà nhà nhà hát cũng là một điểm nhấn quen thuộc trong trung tâm Rubtsovsk.",
    [
        "Một trong những nhà hát kịch chuyên nghiệp lâu đời của Altai ngoài Barnaul.",
        "Trung tâm đời sống văn hoá của thành phố công nghiệp Rubtsovsk.",
        "Dàn dựng kịch kinh điển Nga, tác phẩm hiện đại và kịch thiếu nhi.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch mùa, thường buổi tối và cuối tuần; phòng vé mở ban ngày.",
        "ticket_vi": "Vé giá phải chăng, thay đổi theo vở diễn.",
        "duration_vi": "Một buổi diễn khoảng 2 giờ.",
        "best_time_vi": "Mùa diễn từ thu đến xuân; xem lịch trước khi đến.",
        "tips_vi": "Đặt vé trước cho suất cuối tuần; kết hợp tham quan trung tâm Rubtsovsk.",
    },
    [
        {"title": "Wikipedia (RU) — Рубцовский драматический театр", "url": "https://ru.wikipedia.org/wiki/Рубцовский_драматический_театр"},
        {"title": "Yandex Maps — Рубцовский драматический театр", "url": "https://yandex.ru/maps/org/rubtsovskiy_dramaticheskiy_teatr/1401367421/"},
    ],
    ["theatre", "drama", "rubtsovsk", "culture", "altai"],
    maps_org("https://yandex.ru/maps/org/rubtsovskiy_dramaticheskiy_teatr/1401367421/", "Rubtsovsk Drama Theatre", "Rubtsovsk"),
))

# 22) Бийский драматический театр -------------------------------------------------
RECORDS.append(rec(
    "biysk-drama-theatre",
    "Nhà hát kịch Biysk",
    "Бийский драматический театр",
    "Biysk Drama Theatre",
    ["theatre"],
    52.539640, 85.225220,
    "Ул. Советская, 25, thành phố Biysk, vùng Altai, Nga.",
    "Nhà hát kịch của Biysk - thành phố cổ thứ hai vùng Altai, thành lập giữa những năm chiến tranh. Sân khấu là trung tâm văn hoá của cửa ngõ dẫn vào con đường Chuysky Trakt.",
    "Nhà hát kịch Biysk được thành lập vào năm 1943, ngay giữa những năm tháng khốc liệt của Chiến tranh Vệ quốc Vĩ đại, như một điểm tựa tinh thần cho cư dân thành phố hậu phương. Biysk là thành phố cổ thứ hai của vùng Altai và là cửa ngõ khởi đầu con đường huyền thoại Chuysky Trakt, nên nhà hát cũng mang vai trò trung tâm văn hoá của cả vùng nam Altai. Trải qua hơn tám thập niên, nhà hát đã dàn dựng vô số vở kịch kinh điển Nga, tác phẩm thế giới và kịch đương đại, đồng thời là nơi ươm mầm cho nhiều thế hệ diễn viên. Toà nhà nhà hát nằm trong khu trung tâm với những công trình cổ kính của Biysk, gần các bảo tàng và nhà thờ, tạo thành một cụm văn hoá thuận tiện tham quan. Với du khách trên hành trình khám phá Altai, một buổi tối xem kịch ở Biysk là cơ hội để hoà vào đời sống văn hoá địa phương và cảm nhận không khí của một đô thị thương mại - văn hoá vùng biên. Nhà hát cũng thường tổ chức các liên hoan và sự kiện nghệ thuật thu hút khán giả khắp vùng.",
    [
        "Nhà hát kịch của Biysk, thành lập năm 1943 giữa những năm chiến tranh.",
        "Trung tâm văn hoá của thành phố cổ - cửa ngõ con đường Chuysky Trakt.",
        "Nằm trong cụm di sản trung tâm Biysk, gần bảo tàng và nhà thờ.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch mùa, thường buổi tối và cuối tuần; phòng vé mở ban ngày.",
        "ticket_vi": "Vé giá phải chăng, thay đổi theo vở diễn.",
        "duration_vi": "Một buổi diễn khoảng 2 giờ.",
        "best_time_vi": "Mùa diễn từ thu đến xuân; xem lịch trước khi đến.",
        "tips_vi": "Kết hợp dạo khu phố thương gia cổ Biysk, Nhà thờ Uspensky và Bảo tàng địa phương.",
    },
    [
        {"title": "Wikipedia (RU) — Бийский драматический театр", "url": "https://ru.wikipedia.org/wiki/Бийский_драматический_театр"},
        {"title": "Культура.РФ — Бийский драматический театр", "url": "https://www.culture.ru/"},
    ],
    ["theatre", "drama", "biysk", "culture", "chuysky-tract", "altai"],
    maps_text("Бийский драматический театр", "Бийск", "Biysk Drama Theatre", "Biysk", 52.539640, 85.225220),
))

# 23) Нулевой километр (Барнаул) ---------------------------------------------------
RECORDS.append(rec(
    "barnaul-nulevoy-kilometr",
    "Cột mốc Cây số 0 (Nulevoy Kilometr, Barnaul)",
    "Нулевой километр",
    "Zero Kilometre Marker (Barnaul)",
    ["monument"],
    53.347394, 83.778443,
    "Пр. Ленина, gần bưu điện trung tâm, thành phố Barnaul, vùng Altai, Nga.",
    "Cột mốc đánh dấu 'điểm khởi đầu' của các con đường vùng Altai, dựng bằng đá porphyr Korgon quý của Altai. Một biểu tượng nhỏ xinh và điểm chụp ảnh - ước nguyện quen thuộc giữa trung tâm Barnaul.",
    "Cột mốc Cây số 0 là một điểm nhấn nhỏ nhưng thú vị ngay giữa trung tâm Barnaul, gần toà bưu điện chính trên đại lộ Lenin. Được dựng vào đầu những năm 2000, cột mốc mang ý nghĩa tượng trưng là 'điểm khởi đầu' để tính khoảng cách của các tuyến đường trong vùng Altai. Điều đặc biệt là cột được chế tác từ đá porphyr Korgon - loại đá màu quý của vùng Altai từng được dùng cho các công trình hoàng gia ở Sankt-Peterburg, gắn liền với truyền thống chạm khắc đá lừng danh của xứ này. Dưới chân cột thường được trang trí các biểu tượng cung hoàng đạo hoặc phương hướng, tạo nét duyên dáng cho công trình. Người dân và du khách có thói quen dừng lại chụp ảnh, thả đồng xu và ước nguyện tại đây như một điểm 'lấy may' của thành phố. Nằm ngay trên trục phố đi bộ chính, cột mốc là điểm dừng chân nhẹ nhàng trong hành trình dạo bộ khám phá trung tâm Barnaul, thường được ghép cùng các điểm lân cận như Quảng trường Xô Viết, nhà thờ và các bảo tàng.",
    [
        "Cột mốc tượng trưng 'điểm khởi đầu' các con đường vùng Altai.",
        "Chế tác từ đá porphyr Korgon quý - di sản chạm khắc đá của Altai.",
        "Điểm chụp ảnh, thả xu ước nguyện quen thuộc giữa trung tâm Barnaul.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Quanh năm; đẹp khi dạo bộ trung tâm ban ngày hoặc buổi tối lên đèn.",
        "tips_vi": "Ghép cùng dạo đại lộ Lenin, Quảng trường Xô Viết và các bảo tàng trung tâm.",
    },
    [
        {"title": "Wikipedia (RU) — Барнаул", "url": "https://ru.wikipedia.org/wiki/Барнаул"},
        {"title": "VisitAltai — Нулевой километр (Барнаул)", "url": "https://visitaltai.info/"},
    ],
    ["monument", "landmark", "barnaul", "korgon-porphyry", "photo-spot", "altai"],
    maps_text("Нулевой километр", "Барнаул", "Zero Kilometre Marker", "Barnaul", 53.347394, 83.778443),
))

# 24) Покровский кафедральный собор (Барнаул) -------------------------------------
RECORDS.append(rec(
    "barnaul-pokrovsky-cathedral",
    "Nhà thờ chính toà Pokrovsky (Cầu Bầu, Barnaul)",
    "Покровский кафедральный собор",
    "Intercession Cathedral (Barnaul)",
    ["church"],
    53.329521, 83.774452,
    "Ул. Никитина, 137, thành phố Barnaul, vùng Altai, Nga.",
    "Nhà thờ chính toà bằng gạch đỏ theo phong cách Nga, xây năm 1898-1904. Ngôi thánh đường sống sót qua thời Xô Viết và từng là trung tâm Chính Thống giáo của cả vùng Altai suốt nhiều thập niên.",
    "Nhà thờ chính toà Pokrovsky (lễ Đức Mẹ Cầu Bầu) là một trong những ngôi thánh đường Chính Thống giáo quan trọng và đẹp nhất của Barnaul. Được xây dựng trong những năm 1898-1904 bằng gạch đỏ theo phong cách Nga - Byzantine, nhà thờ nổi bật với những mái vòm hành và tháp chuông vươn cao, trang trí tinh tế. Đây là một trong số ít nhà thờ ở Barnaul không bị phá huỷ dưới thời Xô Viết: sau khi bị đóng cửa những năm 1930, nhà thờ được mở lại vào năm 1944 giữa thời chiến và trong suốt các thập niên 1950-1980 - khi cả vùng Altai chỉ còn vài nhà thờ hoạt động - Pokrovsky đã giữ vai trò trung tâm đời sống tôn giáo, là nơi hàng vạn người dân đến rửa tội, cầu nguyện và làm lễ. Bên trong nhà thờ lưu giữ những bức bích hoạ giá trị được vẽ đầu thế kỷ 20 theo phong cách các danh hoạ Nga, cùng các thánh tượng được tôn kính. Ngày nay, sau khi được trùng tu và dựng lại tháp chuông, nhà thờ đã phục hồi gần như trọn vẹn diện mạo cổ kính, là điểm đến để du khách chiêm ngưỡng kiến trúc và cảm nhận chiều sâu tâm linh của Chính Thống giáo Nga tại Altai.",
    [
        "Nhà thờ chính toà gạch đỏ kiểu Nga - Byzantine (1898-1904).",
        "Một trong số ít nhà thờ Barnaul không bị phá huỷ thời Xô Viết, mở lại năm 1944.",
        "Bích hoạ đầu thế kỷ 20 và vai trò trung tâm Chính Thống giáo của cả vùng Altai.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp lễ lớn của Chính Thống giáo.",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; giữ yên lặng và xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Sobory.ru — Барнаул, Кафедральный собор Покрова Пресвятой Богородицы", "url": "https://sobory.ru/article/?object=09834"},
        {"title": "Wikipedia (RU) — Покровский собор (Барнаул)", "url": "https://ru.wikipedia.org/wiki/Покровский_собор_(Барнаул)"},
    ],
    ["church", "cathedral", "orthodox", "barnaul", "red-brick", "frescoes", "altai"],
    maps_text("Покровский кафедральный собор", "Барнаул", "Intercession Cathedral", "Barnaul", 53.329521, 83.774452),
))

# 25) Знаменский монастырь (Барнаул) ----------------------------------------------
RECORDS.append(rec(
    "barnaul-znamensky-convent",
    "Tu viện nữ Znamensky (Barnaul)",
    "Знаменский монастырь",
    "Znamensky Convent (Barnaul)",
    ["church"],
    53.327585, 83.796278,
    "Ул. Большая Олонская, 24, thành phố Barnaul, vùng Altai, Nga.",
    "Tu viện nữ Chính Thống giáo của Barnaul, hình thành quanh nhà thờ Znamensky gạch đỏ thế kỷ 19. Một ốc đảo tâm linh yên bình gần khu trung tâm cổ và Công viên Nagorny.",
    "Tu viện nữ Znamensky (Dấu Chỉ) là trung tâm tu hành nữ giới của Chính Thống giáo tại Barnaul, hình thành quanh ngôi nhà thờ Znamensky cổ kính. Nhà thờ chính của tu viện được xây bằng gạch trong những năm 1853-1858 theo phong cách Nga - Byzantine, với những mái vòm và trang trí đặc trưng. Dưới thời Xô Viết, nhà thờ bị đóng cửa năm 1933, bị dỡ tháp chuông cùng các vòm và trưng dụng làm kho lưu trữ, che lấp bởi nhiều công trình cơi nới. Đến năm 1992, nhà thờ được trả lại cho Giáo hội, và từ năm 1994 một tu viện nữ được thành lập tại đây. Qua nhiều năm trùng tu, các phần cơi nới bị dỡ bỏ, mái vòm và tháp chuông được dựng lại, giúp nhà thờ dần lấy lại diện mạo ban đầu. Tu viện lưu giữ nhiều thánh tích và thánh tượng được tôn kính, đồng thời gìn giữ một nguồn nước thiêng cổ (Nikolsky) được cho là có tính chữa lành. Nằm gần khu trung tâm lịch sử và Công viên Nagorny, tu viện là một ốc đảo tĩnh lặng, nơi du khách có thể cảm nhận không gian tu hành trầm mặc và chiêm ngưỡng kiến trúc tôn giáo Nga giữa lòng thành phố.",
    [
        "Tu viện nữ hình thành quanh nhà thờ Znamensky gạch đỏ (1853-1858).",
        "Được trả lại Giáo hội năm 1992, lập tu viện nữ từ năm 1994 và trùng tu phục hồi.",
        "Ốc đảo tâm linh yên bình gần trung tâm cổ và Công viên Nagorny.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (là tu viện đang hoạt động).",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp lễ lớn của Chính Thống giáo.",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; giữ yên lặng; kết hợp lên Công viên Nagorny gần đó ngắm sông Ob.",
    },
    [
        {"title": "Sobory.ru — Барнаул, Знаменский монастырь", "url": "https://sobory.ru/article/?object=19897"},
        {"title": "Wikipedia (RU) — Знаменский монастырь (Барнаул)", "url": "https://ru.wikipedia.org/wiki/Знаменский_монастырь_(Барнаул)"},
    ],
    ["convent", "monastery", "orthodox", "barnaul", "red-brick", "altai"],
    maps_text("Знаменский монастырь", "Барнаул", "Znamensky Convent", "Barnaul", 53.327585, 83.796278),
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
