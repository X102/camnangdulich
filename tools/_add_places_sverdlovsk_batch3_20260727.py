# -*- coding: utf-8 -*-
"""_add_places_sverdlovsk_batch3_20260727.py — VÙNG TIÊU ĐIỂM: Tỉnh Sverdlovsk
(lần chạy tự động 2026-07-27, đợt 3).

Bối cảnh: sverdlovsk.json hiện có 37 địa điểm (sau đợt 1 & 2). tatarstan (60) và
nizhny-novgorod (58) đã ≥50 => vùng tiêu điểm vẫn là Sverdlovsk (slug kế trong danh
sách ưu tiên còn <50). Nâng dần tới ~50–100.

Đợt này bổ sung 15 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình
(museum 4 · theatre 1 · other 3 · monument 1 · church 2 · park_garden 4):
- Bảo tàng: Дом-музей Чайковского (Алапаевск), Музей истории камнерезного и
  ювелирного искусства (Екб), Художественный музей Эрнста Неизвестного (Екб),
  Музей истории Екатеринбурга.
- Nhà hát: Свердловский театр музыкальной комедии.
- Khác/hiện đại: Екатеринбургский цирк, стадион «Екатеринбург Арена» (World Cup 2018),
  Коуровская астрономическая обсерватория.
- Đài kỷ niệm: Памятник The Beatles (đầu tiên ở Nga).
- Nhà thờ/tu viện: Свято-Покровский женский монастырь (Верхотурье),
  Монастырь во имя новомучеников (Алапаевск, шахта Межная — nơi tưởng niệm Романовы).
- Thiên nhiên: природный парк «Бажовские места» (Сысерть), скалы «Семь братьев»,
  порог Ревун trên sông Исеть, гора Волчиха (đỉnh cao nhất quanh Yekaterinburg).

TOẠ ĐỘ — xác minh chéo (ru.wikipedia geohack / Ураловед / nashural, 2026-07):
  Дом-музей Чайковского 57.857778,61.703333 (57°51′28″N 61°42′12″E; Ленина 30);
  Музей камнерезного 56.838889,60.606667 (ru.wiki 56°50′20″N 60°36′24″E; Ленина 37,
  Горная аптека — có URL trang tổ chức Яндекс); Музей Эрнста Неизвестного
  56.831667,60.603611 (ru.wiki 56°49′54″N 60°36′13″E; Добролюбова 14);
  Музей истории Екатеринбурга 56.840556,60.611389 (ru.wiki 56°50′26″N 60°36′41″E;
  Карла Либкнехта 26, Дом Качки); Театр музкомедии 56.839722,60.611667 (ru.wiki
  56°50′23″N 60°36′42″E; Ленина 47); Екатеринбургский цирк 56.825833,60.605278
  (ru.wiki 56°49′33″N 60°36′19″E; 8 Марта 43); Екатеринбург Арена 56.832220,60.573610
  (Репина 5); Коуровская обсерватория 57.036713,59.547272 (gần Слобода/ст. Коуровка);
  Памятник The Beatles 56.833889,60.606667 (ru.wiki 56°50′02″N 60°36′24″E; Горького 8);
  Покровский монастырь Верхотурье 58.855799,60.810852; Монастырь новомучеников
  57.954167,61.701667 (ru.wiki 57°57′15″N 61°42′06″E; близ Синячихи); Бажовские места
  56.508605,60.736346 (Сысерть); Семь братьев 57.240500,60.230667 (N57°14.430′
  E60°13.840′; gần Верх-Нейвинский); порог Ревун 56.433833,61.602583 (sông Исеть, gần
  Бекленищево, huyện Каменский); гора Волчиха 56.827533,60.003967 (526 m, gần Ревда).
  Kiểm tra thứ tự & phạm vi (tỉnh Sverdlovsk: lat ~56,3–59,0; lon ~59,0–63,1; KHÔNG đảo
  lat/lon; đều nằm trong tỉnh). Link bản đồ TRỎ-ĐỊA-ĐIỂM: text-search theo tên_ru +
  thành phố, canh giữa theo toạ độ đã kiểm; riêng 2 bảo tàng có URL trang tổ chức Яндекс.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_sverdlovsk_batch3_20260727.py
       python3 tools/normalize_categories.py && python3 tools/build.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"

REGION = "sverdlovsk"
REGION_NAME_VI = "Tỉnh Sverdlovsk"
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


RECORDS = []

# 1) Дом-музей П. И. Чайковского (Алапаевск) -----------------------------------
RECORDS.append(rec(
    "tchaikovsky-house-museum-alapaevsk",
    "Nhà lưu niệm P. I. Tchaikovsky (Dom-muzey Chaykovskogo), Alapaevsk",
    "Дом-музей П. И. Чайковского",
    "P. I. Tchaikovsky House-Museum (Alapaevsk)",
    ["museum"],
    57.857778, 61.703333,
    "Улица Ленина, 30, thành phố Alapaevsk, tỉnh Sverdlovsk, Nga.",
    "Bảo tàng âm nhạc duy nhất ở vùng Trung Ural, đặt trong chính ngôi nhà nơi nhà soạn nhạc thiên tài Pyotr Tchaikovsky sống thời thơ ấu (1849–1850), khi cha ông làm quản đốc khu mỏ Alapaevsk. Ngoài không gian tưởng niệm gia đình Tchaikovsky, bảo tàng còn nổi tiếng với bộ sưu tập gần một nghìn nhạc cụ dân tộc từ khắp thế giới.",
    "Thị trấn công nghiệp nhỏ Alapaevsk ở phía đông tỉnh Sverdlovsk gắn liền với một cái tên lừng danh của âm nhạc thế giới: Pyotr Ilyich Tchaikovsky. Năm 1849, khi cậu bé Pyotr mới chín tuổi, gia đình chuyển tới đây vì cha cậu – kỹ sư Ilya Tchaikovsky – được bổ nhiệm làm quản đốc các nhà máy mỏ Alapaevsk; họ sống trong ngôi nhà gỗ khang trang này khoảng một năm. Bảo tàng mở cửa năm 1965 và là bảo tàng âm nhạc duy nhất của vùng Trung Ural. Phần trưng bày tưởng niệm tái hiện nếp sống của gia đình Tchaikovsky giữa thế kỷ 19 với nội thất, thư từ, tranh ảnh và những kỷ vật gợi lại tuổi thơ của nhà soạn nhạc tương lai. Điểm độc đáo khiến bảo tàng vượt xa một điểm lưu niệm thông thường là bộ sưu tập nhạc cụ dân tộc đồ sộ – khoảng một nghìn hiện vật từ nhiều quốc gia và dân tộc, từ đàn dây, kèn hơi tới bộ gõ, cho phép du khách hình dung sự phong phú của âm nhạc nhân loại. Vào các dịp lễ, bảo tàng tổ chức hoà nhạc thính phòng, đưa những giai điệu vang lên ngay trong không gian gắn với thời thơ ấu của Tchaikovsky. Đây là điểm dừng ý nghĩa trên hành trình khám phá Alapaevsk và các di tích lịch sử quanh vùng.",
    [
        "Ngôi nhà nơi Tchaikovsky sống thời thơ ấu (1849–1850) khi cha làm quản đốc mỏ Alapaevsk.",
        "Bảo tàng âm nhạc duy nhất ở vùng Trung Ural, mở cửa năm 1965.",
        "Bộ sưu tập gần 1.000 nhạc cụ dân tộc từ khắp thế giới; thường có hoà nhạc thính phòng.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật (giờ hành chính), nghỉ thứ Hai; nên kiểm tra lịch trước.",
        "ticket_vi": "Có vé vào cửa, giá bình dân; có tour hướng dẫn và chương trình âm nhạc theo dịp.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà); thú vị nhất khi có buổi hoà nhạc.",
        "tips_vi": "Alapaevsk cách Yekaterinburg khoảng 150 km; kết hợp thăm bảo tàng gỗ Nizhnyaya Sinyachikha và tu viện Novomucheniki gần đó.",
    },
    [
        {"title": "Свердловский областной краеведческий музей — Дом-музей П. И. Чайковского", "url": "https://uole-museum.ru/museums/dom-muzej-p-i-chajkovskogo/"},
        {"title": "Культура.РФ — Дом-музей П. И. Чайковского", "url": "https://www.culture.ru/institutes/41084/dom-muzei-p-i-chaikovskogo"},
    ],
    ["museum", "tchaikovsky", "music", "alapaevsk", "history"],
    maps_org("https://yandex.ru/maps/org/dom_muzey_p_i_chaykovskogo/1101815784/", "Tchaikovsky House-Museum", "Alapaevsk"),
))

# 2) Музей истории камнерезного и ювелирного искусства (Екатеринбург) ----------
RECORDS.append(rec(
    "stone-cutting-jewellery-museum-yekaterinburg",
    "Bảo tàng Lịch sử nghệ thuật chạm khắc đá và kim hoàn Ural",
    "Музей истории камнерезного и ювелирного искусства",
    "Museum of the History of Stone-Cutting and Jewellery Art",
    ["museum"],
    56.838889, 60.606667,
    "Проспект Ленина, 37, toà nhà «Горная аптека» (nhà thuốc của cục mỏ, 1821–1822), trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Bảo tàng đầu tiên ở Nga chuyên về nghệ thuật chạm khắc đá và kim hoàn, đặt trong toà «Горная аптека» cổ kính giữa trung tâm Yekaterinburg. Nơi đây phô diễn truyền thống chế tác đá quý – nhất là malachite (đá công) Ural – cùng các tác phẩm của hãng Fabergé và «Phòng ngọc lục bảo» rực rỡ.",
    "Vùng Ural từ lâu được mệnh danh là «hộp châu báu» của nước Nga nhờ trữ lượng đá quý và bán quý phong phú: malachite, jasper, thạch anh, ngọc lục bảo… Bảo tàng Lịch sử nghệ thuật chạm khắc đá và kim hoàn, thành lập năm 1992, là bảo tàng chuyên đề đầu tiên của cả nước tôn vinh nghề chế tác đá và kim hoàn Ural. Bảo tàng toạ lạc trong «Горная аптека» – nhà thuốc của cục mỏ do kiến trúc sư M. P. Malakhov thiết kế đầu thế kỷ 19, bản thân là một di tích kiến trúc cổ điển đẹp. Các gian trưng bày dẫn khách qua lịch sử nghề đá nghệ thuật thế kỷ 19 – đầu thế kỷ 20, những kiệt tác malachite, sản phẩm của Nhà máy mài đá Hoàng gia Yekaterinburg và xưởng «Русские самоцветы», cho tới nghệ thuật kim hoàn – chạm khắc đương đại của các nghệ nhân Ural. Niềm tự hào của bộ sưu tập là các hiện vật liên quan tới hãng trứ danh Fabergé, và từ năm 2015 là «Phòng ngọc lục bảo» (Изумрудная комната) lấp lánh được du khách đặc biệt yêu thích. Với những ai muốn hiểu vì sao Ural gắn liền với đá quý và với hình tượng «bà chúa Núi Đồng» trong truyện Bazhov, đây là điểm đến không thể bỏ qua.",
    [
        "Bảo tàng chuyên về nghệ thuật chạm khắc đá và kim hoàn đầu tiên ở Nga (1992).",
        "Trưng bày malachite Ural, sản phẩm Fabergé và «Phòng ngọc lục bảo» nổi tiếng.",
        "Đặt trong toà «Горная аптека» – di tích kiến trúc cổ điển đầu thế kỷ 19.",
    ],
    {
        "hours_vi": "Thường mở thứ Tư–Chủ nhật 11:00–18:00, thứ Năm tới 20:00; nghỉ thứ Hai–thứ Ba (kiểm tra lịch).",
        "ticket_vi": "Có vé vào cửa, giá bình dân; có thể mua thêm vé chuyên đề/tour hướng dẫn.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Nằm ngay cạnh площадь Труда và Plotinka; dễ kết hợp đi bộ tham quan trung tâm lịch sử Yekaterinburg.",
    },
    [
        {"title": "Wikipedia (RU) — Музей истории камнерезного и ювелирного искусства", "url": "https://ru.wikipedia.org/wiki/Музей_истории_камнерезного_и_ювелирного_искусства"},
        {"title": "Культура.РФ — Музей истории камнерезного и ювелирного искусства", "url": "https://www.culture.ru/institutes/10338/muzei-istorii-kamnereznogo-i-yuvelirnogo-iskusstva"},
    ],
    ["museum", "gemstones", "malachite", "faberge", "ural", "yekaterinburg"],
    maps_org("https://yandex.com/maps/org/muzey_istorii_kamnereznogo_i_yuvelirnogo_iskusstva/1159834482/", "Museum of Stone-Cutting and Jewellery Art", "Yekaterinburg"),
))

# 3) Художественный музей Эрнста Неизвестного (Екатеринбург) -------------------
RECORDS.append(rec(
    "ernst-neizvestny-art-museum",
    "Bảo tàng Mỹ thuật Ernst Neizvestny",
    "Художественный музей Эрнста Неизвестного",
    "Ernst Neizvestny Art Museum",
    ["museum"],
    56.831667, 60.603611,
    "Улица Добролюбова, 14 (nhà cổ giữa thế kỷ 19, di sản văn hoá), trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Bảo tàng đầu tiên ở Nga và thứ hai trên thế giới dành cho nhà điêu khắc, triết gia Ernst Neizvestny – người con của Yekaterinburg. Mở cửa năm 2013 đúng sinh nhật thứ 88 của ông, bảo tàng trưng bày các tác phẩm gốc: điêu khắc cỡ nhỏ, đồ hoạ, minh hoạ sách và ảnh tư liệu hiếm.",
    "Ernst Neizvestny (1925–2016) là một trong những nhà điêu khắc Nga nổi tiếng nhất thế kỷ 20, sinh ra tại Yekaterinburg (khi ấy là Sverdlovsk). Từng nổi tiếng vì cuộc tranh luận thẳng thắn với lãnh đạo Xô Viết Nikita Khrushchev về nghệ thuật, ông sau này di cư và tạo nên những tượng đài đồ sộ khắp thế giới, trong đó có «Mặt nạ đau thương» tưởng niệm nạn nhân của đàn áp chính trị, dựng tại chính Yekaterinburg năm 2017. Bảo tàng mang tên ông mở cửa năm 2013 – khi nghệ sĩ còn sống – và là bảo tàng đầu tiên ở Nga, thứ hai trên thế giới, dành riêng cho di sản của ông. Không gian trưng bày nằm trong một ngôi nhà đá cổ giữa thế kỷ 19 (di tích văn hoá) ngay trung tâm thành phố. Năm gian phòng dẫn khách qua triết lý và các giai đoạn sáng tạo của Neizvestny, với những tác phẩm được thừa nhận như «Trái tim Chúa», «Nhân mã cái và đứa trẻ», «Vụ nổ nguyên tử», «Orpheus»… cùng mô hình tượng đài «Mặt nạ đau thương: Âu – Á». Các màn hình đa phương tiện giới thiệu những tượng đài lớn của ông ở Kemerovo, Geneva, Moskva… Bảo tàng có audio-guide, video-guide và cả «game-guide» dành cho trẻ em, rất thân thiện với gia đình và người yêu nghệ thuật đương đại.",
    [
        "Bảo tàng đầu tiên ở Nga, thứ hai thế giới dành cho điêu khắc gia Ernst Neizvestny.",
        "Trưng bày tác phẩm gốc và mô hình tượng đài «Mặt nạ đau thương: Âu – Á».",
        "Đặt trong ngôi nhà đá cổ giữa thế kỷ 19, di sản văn hoá cấp vùng.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật 11:00–18:00; nghỉ thứ Hai (kiểm tra lịch chính thức).",
        "ticket_vi": "Có vé vào cửa, giá bình dân; có audio/video-guide và tour hướng dẫn.",
        "duration_vi": "Khoảng 1 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Kết hợp ghé «Mặt nạ đau thương» trên đồi Đá lều (nếu có thời gian) để thấy tác phẩm ngoài trời của ông.",
    },
    [
        {"title": "Wikipedia (RU) — Художественный музей Эрнста Неизвестного", "url": "https://ru.wikipedia.org/wiki/Художественный_музей_Эрнста_Неизвестного"},
        {"title": "Культура.РФ — Художественный музей Эрнста Неизвестного", "url": "https://www.culture.ru/institutes/12292/khudozhestvennyi-muzei-ernsta-neizvestnogo"},
    ],
    ["museum", "sculpture", "ernst-neizvestny", "art", "yekaterinburg"],
    maps_text("Художественный музей Эрнста Неизвестного", "Екатеринбург", "Ernst Neizvestny Art Museum", "Yekaterinburg", 56.831667, 60.603611),
    official_site="https://en-artmuseum.ru/",
))

# 4) Музей истории Екатеринбурга ----------------------------------------------
RECORDS.append(rec(
    "yekaterinburg-history-museum",
    "Bảo tàng Lịch sử Yekaterinburg (Dom Kachki)",
    "Музей истории Екатеринбурга",
    "Museum of the History of Yekaterinburg",
    ["museum"],
    56.840556, 60.611389,
    "Улица Карла Либкнехта, 26 («Дом Качки», di tích liên bang), trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Một trong những bảo tàng lâu đời nhất thành phố, kể câu chuyện đô thị Yekaterinburg từ thế kỷ 18 tới nay. Bảo tàng đặt trong «Дом Качки» – toà nhà đầu thế kỷ 19, di tích lịch sử – văn hoá cấp liên bang, nổi bật với cách trưng bày hiện đại, đa giác quan.",
    "Bảo tàng Lịch sử Yekaterinburg khởi nguồn từ năm 1939–1940, ban đầu là bảo tàng tưởng niệm Ya. M. Sverdlov, và sau lần cải tổ lớn năm 1995 mang tên gọi hiện nay. Bảo tàng chuyên khai thác đời sống thường nhật và văn hoá đô thị các thế kỷ 18–21: qua những đồ vật rất đỗi bình thường và các câu chuyện cá nhân, người xem cảm nhận được nhịp sống, tinh thần và biến chuyển của thành phố qua các thời kỳ. Toà nhà chính – «Дом Качки» – xây năm 1820, từng là khách sạn, dinh thự quý tộc, nhà cho thuê, nơi đặt thư viện tư nhân trứ danh của S. A. Tikhotskaya cuối thế kỷ 19; nay là di tích cấp liên bang. Sau đợt tái thiết – mở rộng năm 2004–2005, phần trưng bày mới cho phép du khách «du hành» từ thế kỷ 18 sang thế kỷ 21: dạo bước trên những con phố Yekaterinburg xưa, ngắm thành phố từ vũ trụ, xuống «thành phố ngầm» tìm hiểu lòng đất giàu khoáng sản và mạng lưới sông – đường của đô thị. Bảo tàng còn giữ nhiều bản gốc ảnh, tài liệu, sách quý và cả tác phẩm của các nghệ sĩ Ural. Đây là điểm khởi đầu lý tưởng để hiểu lịch sử và bản sắc của thủ phủ vùng Ural.",
    [
        "Một trong những bảo tàng lâu đời nhất Yekaterinburg (từ 1939–1940).",
        "Đặt trong «Дом Качки» đầu thế kỷ 19 – di tích lịch sử cấp liên bang.",
        "Trưng bày đa giác quan về đời sống đô thị thế kỷ 18–21, có «thành phố ngầm».",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật (giờ hành chính); nghỉ thứ Hai (kiểm tra lịch).",
        "ticket_vi": "Có vé vào cửa, giá bình dân; có tour và chương trình tương tác cho trẻ.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Nằm trên «Đường Đỏ» (Красная линия) đi bộ khám phá trung tâm; kết hợp Plotinka và Храм на Крови gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Музей истории Екатеринбурга", "url": "https://ru.wikipedia.org/wiki/Музей_истории_Екатеринбурга"},
        {"title": "Культура.РФ — Музей истории Екатеринбурга", "url": "https://www.culture.ru/institutes/4525/muzei-istorii-ekaterinburga"},
    ],
    ["museum", "city-history", "yekaterinburg", "heritage"],
    maps_text("Музей истории Екатеринбурга", "Екатеринбург", "Museum of the History of Yekaterinburg", "Yekaterinburg", 56.840556, 60.611389),
    official_site="https://m-i-e.ru/",
))

# 5) Свердловский театр музыкальной комедии ------------------------------------
RECORDS.append(rec(
    "sverdlovsk-musical-comedy-theatre",
    "Nhà hát Nhạc kịch Sverdlovsk (Teatr muzykalnoy komedii)",
    "Свердловский академический театр музыкальной комедии",
    "Sverdlovsk Academic Musical Comedy Theatre",
    ["theatre"],
    56.839722, 60.611667,
    "Проспект Ленина, 47, trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Một trong những nhà hát nhạc kịch (operetta – musical) hàng đầu nước Nga, thành lập năm 1933, từng được mệnh danh là «phòng thí nghiệm của operetta Xô Viết». Nhà hát giành tổng cộng mười sáu giải «Mặt nạ Vàng» danh giá và diễn trong toà nhà phong cách Modern đầu thế kỷ 20.",
    "Nhà hát Nhạc kịch Sverdlovsk mở màn ngày 8 tháng 7 năm 1933 và nhanh chóng trở thành một trong những sân khấu operetta – nhạc kịch được yêu thích nhất Liên Xô. Nhờ mạnh dạn dàn dựng cả kịch mục kinh điển lẫn tác phẩm đương đại, nhà hát có biệt danh «phòng thí nghiệm của operetta Xô Viết» và nhiều lần công diễn ra mắt thế giới các vở operetta, musical của tác giả Nga. Năm 1986, đây là nhà hát operetta đầu tiên được phong danh hiệu «hàn lâm» (academic). Bộ sưu tập giải thưởng của nhà hát rất đồ sộ: Giải Stalin (1946), Huân chương Cờ Đỏ Lao động (1983), Giải thưởng Chính phủ mang tên Fyodor Volkov (2004) và tổng cộng mười sáu giải «Mặt nạ Vàng» (Золотая маска) – giải thưởng sân khấu quốc gia cao quý nhất nước Nga, trong đó có ba giải cho «Vở diễn xuất sắc nhất». Toà nhà nhà hát vốn được xây năm 1915 theo phong cách Modern (kiến trúc sư K. T. Babykin) cho «Câu lạc bộ Thương mại», sau nhiều lần cải tạo và hợp nhất với rạp chiếu bóng «Loranzh» kế bên (1962) để có diện mạo hiện nay. Nhà hát cũng là nơi tổ chức nhiều liên hoan, cuộc thi nghệ thuật quốc tế thường niên, xứng đáng là điểm đến cho ai yêu âm nhạc và sân khấu khi tới Yekaterinburg.",
    [
        "Nhà hát operetta – nhạc kịch hàng đầu Nga, thành lập 1933, «hàn lâm» từ 1986.",
        "Giành tổng cộng 16 giải «Mặt nạ Vàng» – giải sân khấu quốc gia cao nhất.",
        "Toà nhà phong cách Modern (1915), hợp nhất với rạp «Loranzh» năm 1962.",
    ],
    {
        "hours_vi": "Phòng vé thường mở hằng ngày ~10:00–19:30; suất diễn chủ yếu buổi tối và cuối tuần.",
        "ticket_vi": "Mua vé theo vở diễn (nhiều mức giá); nên đặt trước qua trang chính thức.",
        "duration_vi": "Mỗi vở khoảng 2–3 giờ (có nghỉ giải lao).",
        "best_time_vi": "Mùa diễn thu – xuân; kiểm tra lịch để chọn vở phù hợp.",
        "tips_vi": "Nằm ngay trên пр. Ленина, gần Nhà hát Opera & Ballet; đến sớm để ngắm nội thất sảnh.",
    },
    [
        {"title": "Wikipedia (RU) — Свердловский академический театр музыкальной комедии", "url": "https://ru.wikipedia.org/wiki/Свердловский_театр_музыкальной_комедии"},
        {"title": "Культура.РФ — Свердловский государственный академический театр музыкальной комедии", "url": "https://www.culture.ru/institutes/5809/sverdlovskii-gosudarstvennyi-akademicheskii-teatr-muzykalnoi-komedii"},
    ],
    ["theatre", "operetta", "musical", "golden-mask", "yekaterinburg"],
    maps_text("Свердловский театр музыкальной комедии", "Екатеринбург", "Sverdlovsk Musical Comedy Theatre", "Yekaterinburg", 56.839722, 60.611667),
    official_site="https://www.muzkom.net/",
))

# 6) Екатеринбургский государственный цирк ------------------------------------
RECORDS.append(rec(
    "yekaterinburg-circus",
    "Rạp xiếc Quốc gia Yekaterinburg (mang tên V. Filatov)",
    "Екатеринбургский государственный цирк имени В. И. Филатова",
    "Yekaterinburg State Circus",
    ["other"],
    56.825833, 60.605278,
    "Улица 8 Марта, 43, bên hữu ngạn sông Iset, trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Rạp xiếc cố định của Yekaterinburg, khánh thành năm 1980, dễ nhận ra từ xa nhờ mái vòm rỗng đan bằng các nửa cung kim loại cao 50 mét – một biểu tượng kiến trúc độc đáo bên bờ sông Iset. Rạp có 2.558 chỗ ngồi và mang tên nghệ sĩ dạy thú lừng danh Valentin Filatov.",
    "Rạp xiếc quốc gia Yekaterinburg là một trong những công trình xiếc đẹp và độc đáo bậc nhất nước Nga. Toà nhà hiện nay được xây trên hữu ngạn sông Iset trong giai đoạn 1974–1979 và khánh thành ngày 1 tháng 2 năm 1980, thay cho rạp xiếc gỗ cũ đã bị hoả hoạn thiêu rụi năm 1976. Dấu ấn kiến trúc nổi bật nhất là phần mái vòm: một kết cấu rỗng, đan bằng các nửa cung (полуарки) vươn lên cao tới 50 mét (vòm trong 26 mét), tạo hình duyên dáng như chiếc vương miện và mang lại âm học tốt cho khán phòng. Nội thất được ốp đá Ural đặc trưng của vùng. Rạp có sức chứa 2.558 chỗ, hai sàn diễn (chính và tập luyện), được đánh giá là một trong những rạp xiếc tân tiến nhất châu Âu về mặt kỹ thuật, đủ sức dàn dựng những tiết mục phức tạp nhất. Từ năm 1996, nơi đây thường xuyên tổ chức các liên hoan nghệ thuật xiếc khu vực, toàn Nga và quốc tế; năm 2012 rạp được trao giải «Cirk của năm». Rạp mang tên Nghệ sĩ Nhân dân Liên Xô Valentin Filatov, bậc thầy tiết mục gấu biểu diễn. Đây là điểm giải trí hấp dẫn cho gia đình và cũng là một điểm nhấn kiến trúc thú vị của thành phố.",
    [
        "Mái vòm rỗng đan bằng nửa cung kim loại cao 50 m – biểu tượng kiến trúc bên sông Iset.",
        "Khánh thành 1980, sức chứa 2.558 chỗ, nội thất ốp đá Ural.",
        "Mang tên Nghệ sĩ Nhân dân Liên Xô Valentin Filatov; nơi tổ chức liên hoan xiếc quốc tế.",
    ],
    {
        "hours_vi": "Mở theo lịch biểu diễn (thường cuối tuần và kỳ nghỉ); phòng vé giờ hành chính.",
        "ticket_vi": "Mua vé theo suất diễn; nhiều mức giá tuỳ vị trí.",
        "duration_vi": "Mỗi buổi diễn khoảng 2–2,5 giờ.",
        "best_time_vi": "Theo mùa diễn và các chương trình lưu diễn; phù hợp đi cùng trẻ em.",
        "tips_vi": "Nằm gần Памятник клавиатуре và bờ kè Iset; dễ kết hợp dạo phố 8 Марта.",
    },
    [
        {"title": "Wikipedia (RU) — Екатеринбургский цирк", "url": "https://ru.wikipedia.org/wiki/Екатеринбургский_цирк"},
        {"title": "Культура.РФ — Екатеринбургский государственный цирк", "url": "https://www.culture.ru/institutes/42789/ekaterinburgskii-gosudarstvennyi-cirk"},
    ],
    ["circus", "architecture", "family", "yekaterinburg", "entertainment"],
    maps_text("Екатеринбургский государственный цирк", "Екатеринбург", "Yekaterinburg State Circus", "Yekaterinburg", 56.825833, 60.605278),
))

# 7) Стадион «Екатеринбург Арена» (Центральный стадион) -----------------------
RECORDS.append(rec(
    "yekaterinburg-arena-central-stadium",
    "Sân vận động Trung tâm «Ekaterinburg Arena»",
    "Стадион «Екатеринбург Арена» (Центральный стадион)",
    "Yekaterinburg Arena (Central Stadium)",
    ["other"],
    56.832220, 60.573610,
    "Улица Репина, 5, quận Verkh-Isetsky, phía tây trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Sân vận động lớn nhất Yekaterinburg, nơi diễn ra bốn trận vòng bảng World Cup 2018. Công trình độc đáo khi khối khán đài kính – thép hiện đại được «lắp» vào bên trong bức tường mặt tiền cổ điển kiểu Stalin thập niên 1950 vẫn được giữ nguyên.",
    "«Екатеринбург Арена» (trước năm 2018 mang tên «Центральный стадион») là công trình thể thao lớn nhất thành phố. Sân được xây dựng ban đầu trong giai đoạn 1953–1957 với mặt tiền tân cổ điển kiểu Stalin đặc trưng. Để đăng cai World Cup 2018, sân trải qua cuộc tái thiết lớn (2015–2017): các kiến trúc sư đã khéo léo «cấy» một khối arena hiện đại đạt chuẩn FIFA vào bên trong những bức tường lịch sử được bảo tồn – một giải pháp hiếm gặp, kết hợp di sản kiến trúc với công năng thể thao đương đại. Một chi tiết khiến sân trở nên «viral» khắp thế giới năm 2018 là hai khán đài tạm bằng giàn thép nhô hẳn ra ngoài phía sau hai khung thành để tăng sức chứa lên khoảng 35.000 chỗ cho các trận World Cup; hình ảnh khán giả ngồi ở phần khán đài lộ thiên bên ngoài sân đã trở thành biểu tượng vui nhộn của kỳ World Cup tại Nga. Sân đã tổ chức bốn trận đấu vòng bảng World Cup 2018 và nay là sân nhà của câu lạc bộ bóng đá địa phương, đồng thời phục vụ điền kinh và các sự kiện lớn. Với người hâm mộ thể thao và những ai quan tâm kiến trúc, đây là một điểm ghé thú vị ở phía tây thành phố.",
    [
        "Sân World Cup 2018 – tổ chức bốn trận vòng bảng tại Yekaterinburg.",
        "Khối arena kính – thép hiện đại lồng trong mặt tiền cổ điển kiểu Stalin (1953–1957).",
        "Nổi tiếng với hai khán đài tạm bằng giàn thép nhô ra ngoài sân dịp World Cup.",
    ],
    {
        "hours_vi": "Vào sân theo lịch trận đấu/sự kiện; đôi khi có tour tham quan sân (kiểm tra trước).",
        "ticket_vi": "Vé theo trận đấu hoặc sự kiện; tour tham quan (nếu có) tính phí riêng.",
        "duration_vi": "Xem trận ~2 giờ; tham quan ngoài ~30 phút.",
        "best_time_vi": "Mùa giải bóng đá (mùa ấm); ngắm mặt tiền lịch sử ban ngày.",
        "tips_vi": "Cách trung tâm vài km về phía tây; đi taxi/giao thông công cộng thuận tiện.",
    },
    [
        {"title": "Wikipedia (RU) — Екатеринбург Арена", "url": "https://ru.wikipedia.org/wiki/Екатеринбург_Арена"},
        {"title": "Яндекс Карты — Екатеринбург Арена, ул. Репина, 5", "url": "https://yandex.com/maps/org/yekaterinburg_arena/1036422350/"},
    ],
    ["stadium", "football", "world-cup-2018", "architecture", "yekaterinburg"],
    maps_org("https://yandex.com/maps/org/yekaterinburg_arena/1036422350/", "Yekaterinburg Arena", "Yekaterinburg"),
))

# 8) Коуровская астрономическая обсерватория ----------------------------------
RECORDS.append(rec(
    "kourovka-astronomical-observatory",
    "Đài thiên văn Kourovka (mang tên K. A. Barkhatova)",
    "Коуровская астрономическая обсерватория имени К. А. Бархатовой",
    "Kourovka Astronomical Observatory",
    ["other"],
    57.036713, 59.547272,
    "Bên bờ sông Chusovaya, gần làng Sloboda và ga Kourovka, huyện Pervouralsk, tỉnh Sverdlovsk, Nga.",
    "Đài thiên văn đại học lâu đời và nổi tiếng của vùng Ural, trực thuộc Đại học Liên bang Ural, nằm bên bờ sông Chusovaya thơ mộng. Nơi đây gắn với nhiều nghiên cứu thiên văn và có các kính viễn vọng phục vụ quan trắc, đồng thời đón khách tham quan tìm hiểu bầu trời.",
    "Đài thiên văn Kourovka được thành lập cuối thập niên 1960 theo sáng kiến của nữ giáo sư thiên văn Klavdiya Barkhatova và trở thành đài thiên văn đầu tiên, quan trọng nhất của vùng Ural, nay thuộc Viện Khoa học Tự nhiên – Đại học Liên bang Ural. Đài toạ lạc ở một vị trí đắc địa bên bờ sông Chusovaya, gần làng Sloboda và ga đường sắt Kourovka, nơi bầu trời còn tương đối ít ô nhiễm ánh sáng. Các kính viễn vọng của đài phục vụ quan trắc và nghiên cứu về sao biến quang, tiểu hành tinh, vệ tinh nhân tạo và nhiều đối tượng thiên văn khác; đây cũng là cơ sở thực hành cho sinh viên và là nơi tổ chức hội nghị thiên văn thường niên nổi tiếng dành cho giới trẻ. Với du khách, đài mở các buổi tham quan có hướng dẫn: khách được nghe giới thiệu về lịch sử thiên văn học, ngắm mô hình – thiết bị, và trong điều kiện thời tiết thuận lợi có thể quan sát bầu trời qua kính viễn vọng. Kết hợp cùng cảnh quan sông Chusovaya với những vách đá đẹp quanh Sloboda, chuyến đi tới Kourovka là trải nghiệm vừa khoa học vừa thiên nhiên hấp dẫn ở phía tây tỉnh Sverdlovsk.",
    [
        "Đài thiên văn đại học đầu tiên và nổi tiếng nhất vùng Ural, thuộc Đại học Liên bang Ural.",
        "Nằm bên sông Chusovaya, gần Sloboda – trời ít ô nhiễm ánh sáng.",
        "Có tour tham quan, giới thiệu thiên văn và quan sát qua kính viễn vọng (tuỳ thời tiết).",
    ],
    {
        "hours_vi": "Tham quan theo tour đặt trước (thường cuối tuần); quan sát bầu trời phụ thuộc thời tiết.",
        "ticket_vi": "Có phí tham quan; nên đặt lịch trước với đài/đơn vị tổ chức.",
        "duration_vi": "Khoảng 1,5–2 giờ (chưa kể di chuyển).",
        "best_time_vi": "Đêm quang mây để quan sát; mùa đông trời trong nhưng lạnh, cần giữ ấm.",
        "tips_vi": "Cách Yekaterinburg khoảng 80 km; kết hợp ngắm vách đá và sông Chusovaya quanh Sloboda.",
    },
    [
        {"title": "Wikipedia (RU) — Коуровская астрономическая обсерватория имени К. А. Бархатовой", "url": "https://ru.wikipedia.org/wiki/Коуровская_астрономическая_обсерватория_имени_К._А._Бархатовой"},
        {"title": "Ураловед — Коуровская обсерватория", "url": "https://uraloved.ru/kourovskaya-observatoriya"},
    ],
    ["observatory", "astronomy", "chusovaya", "science", "pervouralsk"],
    maps_text("Коуровская астрономическая обсерватория", "Слобода", "Kourovka Astronomical Observatory", "Sloboda", 57.036713, 59.547272),
))

# 9) Памятник The Beatles (Екатеринбург) --------------------------------------
RECORDS.append(rec(
    "beatles-monument-yekaterinburg",
    "Đài kỷ niệm nhóm The Beatles",
    "Памятник группе «The Beatles»",
    "The Beatles Monument (Yekaterinburg)",
    ["monument"],
    56.833889, 60.606667,
    "Улица Горького, 8, bên bờ sông Iset (gần cầu phố Malysheva), trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Đài kỷ niệm nhóm nhạc huyền thoại The Beatles đầu tiên ở Nga, khánh thành năm 2009 bên bờ sông Iset. Tác phẩm gồm bốn bóng đen bằng gang của các thành viên trên nền một bức tường gạch, kèm câu hát nổi tiếng của The Beatles.",
    "Nằm trên bờ sông Iset ngay trung tâm Yekaterinburg, đài kỷ niệm nhóm The Beatles là tượng đài đầu tiên tôn vinh «tứ quái Liverpool» trên đất Nga (và là tượng thứ ba trên toàn lãnh thổ Liên Xô cũ). Công trình do các thành viên câu lạc bộ người hâm mộ The Beatles vùng Ural khởi xướng; toàn bộ kinh phí khoảng 2,5 triệu rúp được quyên góp dần qua các buổi hoà nhạc và đấu giá. Tác giả phác thảo là hoạ sĩ Vadim Okladnikov, còn kiến trúc sư Artyom Alendeyev đảm nhận giải pháp không gian. Đài được khánh thành ngày 23 tháng 5 năm 2009, với khách mời danh dự là các thành viên ban nhạc The Quarrymen do John Lennon sáng lập kéo tấm phủ khai trương. Tượng đài gồm bốn bóng đen bằng gang của John, Paul, George và Ringo dựng trước một bức tường gạch, bên cạnh là dòng chữ trích từ ca khúc của nhóm: «The love you take is equal to the love you make». Theo thời gian, bức tường quanh tượng trở thành một dạng đài tưởng niệm tự phát của người hâm mộ, phủ đầy hình vẽ và chữ ký. Nằm sát bờ kè Iset và không xa Памятник клавиатуре, đây là điểm check-in được giới trẻ và du khách yêu âm nhạc ưa thích.",
    [
        "Tượng đài The Beatles đầu tiên ở Nga, khánh thành 23/5/2009.",
        "Bốn bóng đen bằng gang trên nền tường gạch, kèm câu hát nổi tiếng của nhóm.",
        "Kinh phí ~2,5 triệu rúp quyên góp từ cộng đồng người hâm mộ vùng Ural.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–20 phút.",
        "best_time_vi": "Mùa ấm và buổi chiều tối; dạo bờ kè Iset kết hợp.",
        "tips_vi": "Gần Памятник клавиатуре và trung tâm; dễ ghép vào lộ trình đi bộ ven sông.",
    },
    [
        {"title": "Wikipedia (RU) — Памятник The Beatles (Екатеринбург)", "url": "https://ru.wikipedia.org/wiki/Памятник_The_Beatles_(Екатеринбург)"},
        {"title": "Наш Урал — Памятник «Битлз»", "url": "https://nashural.ru/dostoprimechatelnosti-urala/sverdlovskaya-oblast/bitlz/"},
    ],
    ["monument", "the-beatles", "music", "iset", "yekaterinburg"],
    maps_text("Памятник группе The Beatles", "Екатеринбург", "The Beatles Monument", "Yekaterinburg", 56.833889, 60.606667),
))

# 10) Свято-Покровский женский монастырь (Верхотурье) -------------------------
RECORDS.append(rec(
    "verkhoturye-pokrovsky-convent",
    "Tu viện nữ Pokrovsky (Verkhoturye)",
    "Свято-Покровский женский монастырь",
    "Holy Protection (Pokrovsky) Convent, Verkhoturye",
    ["church"],
    58.855799, 60.810852,
    "Thành phố Verkhoturye, tỉnh Sverdlovsk, Nga (bên bờ sông Tura, khu phố lịch sử).",
    "Tu viện nữ đầu tiên ở phía đông dãy Ural, lập năm 1621 tại Verkhoturye – «thủ đô tâm linh» của vùng Ural. Quần thể có nhà thờ Cầu bầu (Pokrov) và nhà thờ Sinh nhật Thánh Gioan Tiền hô, là điểm hành hương và di sản kiến trúc quý.",
    "Verkhoturye – thành phố cổ nhỏ bé bên sông Tura ở phía bắc tỉnh Sverdlovsk – được xem là «thủ đô tâm linh» của vùng Ural nhờ mật độ dày đặc các nhà thờ, tu viện và gắn với Thánh Simeon xứ Verkhoturye. Trong lòng thành phố, Tu viện nữ Pokrovsky (Cầu bầu của Đức Mẹ) do vị giám mục đầu tiên của Siberia là Kiprian lập năm 1621, và được ghi nhận là tu viện nữ đầu tiên ở phía đông dãy Ural. Ban đầu tu viện dựng bằng gỗ, nhưng do nhiều lần hoả hoạn nên dần được xây lại bằng đá trong thế kỷ 18: nhà thờ Cầu bầu (Pokrovskaya, 1744–1753) và nhà thờ Sinh nhật Thánh Gioan Tiền hô (1768) được xây nhờ tài trợ của nhà công nghiệp Maxim Pokhodyashin. Trải qua thời Xô Viết bị đóng cửa, tu viện được hồi sinh và ngày nay là cộng đoàn nữ tu đang hoạt động, đón đông đảo khách hành hương – nhất là những người trên «con đường của Sa hoàng» và hành trình kính viếng Thánh Simeon. Với du khách, cùng với quần thể Điện Kremlin Verkhoturye và các nhà thờ khác trong thành phố, tu viện góp phần tạo nên một trong những điểm đến tôn giáo – lịch sử độc đáo nhất vùng Ural.",
    [
        "Tu viện nữ đầu tiên ở phía đông dãy Ural, lập năm 1621.",
        "Có nhà thờ Cầu bầu (1744–1753) và nhà thờ Sinh nhật Thánh Gioan Tiền hô (1768).",
        "Điểm hành hương quan trọng ở Verkhoturye – «thủ đô tâm linh» của Ural.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ; khách hành hương và tham quan nên tới ban ngày.",
        "ticket_vi": "Vào tự do; khuyến khích đóng góp tuỳ tâm.",
        "duration_vi": "Khoảng 45–60 phút; lâu hơn nếu kết hợp cả thành phố Verkhoturye.",
        "best_time_vi": "Mùa ấm; dịp lễ Thánh Simeon (tháng 9) rất đông khách hành hương.",
        "tips_vi": "Ăn mặc kín đáo, nữ mang khăn trùm đầu; kết hợp thăm Điện Kremlin Verkhoturye gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Покровский монастырь (Верхотурье)", "url": "https://ru.wikipedia.org/wiki/Покровский_монастырь_(Верхотурье)"},
        {"title": "Монастырский вестник — Свято-Покровский женский монастырь г. Верхотурье", "url": "https://monasterium.ru/monastyri/monastery/svyato-pokrovskiy-zhenskiy-monastyr-g-verkhoture/"},
    ],
    ["monastery", "orthodox-church", "verkhoturye", "pilgrimage", "heritage"],
    maps_text("Свято-Покровский женский монастырь", "Верхотурье", "Pokrovsky Convent", "Verkhoturye", 58.855799, 60.810852),
))

# 11) Монастырь во имя новомучеников (Алапаевск, шахта Межная) ----------------
RECORDS.append(rec(
    "alapaevsk-new-martyrs-monastery",
    "Tu viện Tân Tử đạo Nga bên hầm mỏ Mezhnaya (gần Alapaevsk)",
    "Монастырь во имя новомучеников и исповедников Церкви Русской",
    "Monastery of the New Martyrs of Russia (near Alapaevsk)",
    ["church", "monument"],
    57.954167, 61.701667,
    "Gần làng Sinyachikha, huyện Alapaevsky, cách Alapaevsk khoảng 18 km, tỉnh Sverdlovsk, Nga.",
    "Tu viện nam lập năm 1995 tại nơi các thành viên hoàng tộc Romanov bị sát hại đêm 18/7/1918 – bị ném xuống hầm mỏ Mezhnaya. Đây là nơi tưởng niệm bi thương gắn với Nữ Đại công tước Elizaveta Feodorovna, một điểm hành hương lặng lẽ giữa rừng.",
    "Chỉ một ngày sau khi Sa hoàng Nikolai II và gia đình bị hành quyết ở Yekaterinburg, đêm rạng sáng 18 tháng 7 năm 1918, một nhóm thành viên khác của hoàng tộc Romanov cùng những người thân cận – trong đó có Nữ Đại công tước Elizaveta Feodorovna (chị của Hoàng hậu Aleksandra) và nữ tu Varvara – bị đưa tới hầm mỏ bỏ hoang Mezhnaya thuộc mỏ sắt Nizhnyaya Selimskaya gần Alapaevsk, rồi bị ném sống xuống hầm và bị ném lựu đạn theo sau. Tổng cộng tám người đã thiệt mạng tại đây trong hoàn cảnh vô cùng bi thảm. Sau này Nữ Đại công tước Elizaveta Feodorovna và nữ tu Varvara được Giáo hội Chính thống Nga phong thánh. Để tưởng niệm, một cây thánh giá được dựng năm 1991, nhà nguyện Elizaveta xây năm 1992, và từ năm 1995 khởi công xây tu viện nam mang tên các Tân Tử đạo và Hiển tu nước Nga. Tu viện nằm giữa rừng, giản dị và tĩnh lặng hơn so với quần thể Ganina Yama, với miệng hầm mỏ cũ nay được rào lại và cây thánh giá tưởng niệm bên cạnh. Hằng năm vào dịp giỗ, đông đảo khách hành hương về đây. Đây là một điểm đến giàu ý nghĩa lịch sử – tâm linh, thường được ghép cùng «con đường của Sa hoàng», bảo tàng gỗ Nizhnyaya Sinyachikha và các di tích Alapaevsk.",
    [
        "Nơi tưởng niệm các thành viên hoàng tộc Romanov bị sát hại đêm 18/7/1918.",
        "Gắn với Nữ Đại công tước Elizaveta Feodorovna – được phong thánh sau này.",
        "Tu viện nam lập năm 1995 bên hầm mỏ Mezhnaya, điểm hành hương giữa rừng.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ và giờ tham quan; nên tới ban ngày.",
        "ticket_vi": "Vào tự do; khuyến khích đóng góp tuỳ tâm.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Mùa ấm; dịp 17–18/7 có lễ tưởng niệm và đông khách hành hương.",
        "tips_vi": "Ăn mặc kín đáo, giữ yên lặng; kết hợp thăm bảo tàng gỗ Nizhnyaya Sinyachikha và Alapaevsk.",
    },
    [
        {"title": "Wikipedia (RU) — Монастырь во имя новомучеников и исповедников Церкви Русской", "url": "https://ru.wikipedia.org/wiki/Монастырь_во_имя_новомучеников_и_исповедников_Церкви_Русской"},
        {"title": "Ураловед — Монастырь на месте гибели членов царской семьи близ Алапаевска", "url": "https://uraloved.ru/monastir-na-shahte-mezhnoy"},
    ],
    ["monastery", "romanov", "memorial", "orthodox-church", "alapaevsk", "pilgrimage"],
    maps_text("Монастырь новомучеников Российских", "Алапаевск", "Monastery of the New Martyrs of Russia", "Alapaevsk", 57.954167, 61.701667),
))

# 12) Природный парк «Бажовские места» (Сысерть) ------------------------------
RECORDS.append(rec(
    "bazhov-places-nature-park",
    "Công viên thiên nhiên «Vùng đất Bazhov» (Bazhovskie mesta)",
    "Природный парк «Бажовские места»",
    "Bazhov Places Nature Park",
    ["park_garden"],
    56.508605, 60.736346,
    "Khu đô thị Sysert, cách Yekaterinburg khoảng 60 km về phía nam, tỉnh Sverdlovsk, Nga.",
    "Công viên thiên nhiên rộng lớn quanh Sysert, đặt tên theo nhà văn Ural Pavel Bazhov – nơi bối cảnh các truyện cổ «hộp đá công» của ông. Nổi bật với hồ Talkov Kamen, núi Markov Kamen, sông suối và những tuyến đường mòn đi bộ, đạp xe xuyên rừng taiga.",
    "«Бажовские места» là công viên thiên nhiên (khu bảo tồn đặc biệt) được lập năm 2007 trong khu đô thị Sysert, nằm khoảng 60 km về phía nam Yekaterinburg, với diện tích hơn 61.000 ha. Tên gọi tôn vinh Pavel Bazhov – nhà văn Ural trứ danh với tập truyện cổ «Chiếc hộp malachite» (Малахитовая шкатулка); chính vùng rừng núi, hồ nước và mỏ đá quanh đây là bối cảnh cho những câu chuyện huyền ảo của ông về «Bà chúa Núi Đồng». Điểm đến nổi tiếng nhất trong công viên là hồ Talkov Kamen – một mỏ talc cũ ngập nước với vách đá dựng đứng soi bóng mặt hồ xanh thẫm, khung cảnh nên thơ được nhiều người tìm đến. Ngoài ra còn có núi đá Markov Kamen, các con sông – suối trong vắt, đầm lầy và rừng taiga đặc trưng của Trung Ural. Công viên có hệ thống đường mòn cho đi bộ, đạp xe và các tuyến tham quan sinh thái, cùng khu đón khách và chòi nghỉ. Đây là điểm dã ngoại cuối tuần được người dân Yekaterinburg yêu thích, phù hợp cho cả gia đình muốn hoà mình vào thiên nhiên và không gian cổ tích của xứ Ural.",
    [
        "Công viên thiên nhiên rộng >61.000 ha quanh Sysert, lập năm 2007.",
        "Đặt tên theo nhà văn Bazhov – bối cảnh các truyện cổ «hộp đá công» của Ural.",
        "Nổi bật hồ Talkov Kamen, núi Markov Kamen, đường mòn đi bộ – đạp xe xuyên taiga.",
    ],
    {
        "hours_vi": "Khu vực tự nhiên tham quan ban ngày; trung tâm đón khách theo giờ hành chính.",
        "ticket_vi": "Có phí vào cửa/đăng ký tuyến; một số dịch vụ (thuê xe đạp, hướng dẫn) tính thêm.",
        "duration_vi": "Nửa ngày đến trọn ngày tuỳ tuyến.",
        "best_time_vi": "Cuối xuân đến đầu thu để đi bộ, ngắm hồ; mùa đông có tuyến trượt tuyết.",
        "tips_vi": "Mang giày đi bộ, nước và chống côn trùng; hồ Talkov Kamen là điểm không nên bỏ lỡ.",
    },
    [
        {"title": "Wikipedia (RU) — Бажовские места", "url": "https://ru.wikipedia.org/wiki/Бажовские_места"},
        {"title": "Trang chính thức — Природный парк «Бажовские места»", "url": "https://bm-park.ru/"},
    ],
    ["nature-park", "bazhov", "talkov-kamen", "hiking", "sysert"],
    maps_text("Природный парк Бажовские места", "Сысерть", "Bazhov Places Nature Park", "Sysert", 56.508605, 60.736346),
    official_site="https://bm-park.ru/",
))

# 13) Скалы «Семь братьев» ----------------------------------------------------
RECORDS.append(rec(
    "seven-brothers-rocks",
    "Núi đá «Bảy anh em» (Sem bratyev)",
    "Скалы «Семь братьев»",
    "Seven Brothers Rocks",
    ["park_garden"],
    57.240500, 60.230667,
    "Đỉnh núi Semibratskaya (422 m), cách làng Verkh-Neyvinsky khoảng 6 km, huyện Nevyansk, tỉnh Sverdlovsk, Nga.",
    "Cụm đá granit hình tháp cao tới 30–40 mét trên đỉnh núi Semibratskaya, thuộc hàng thắng cảnh đá đẹp nhất Trung Ural. «Bảy anh em» là di tích thiên nhiên, điểm leo núi và dã ngoại nổi tiếng với truyền thuyết dân gian gắn liền.",
    "«Семь братьев» (Bảy anh em) là cụm đá tàn dư (останцы) granit dựng đứng trên đỉnh núi Semibratskaya cao 422 mét, gần làng Verkh-Neyvinsky ở phía tây tỉnh Sverdlovsk. Những khối đá xếp chồng nhô lên như một dãy tháp tự nhiên cao tới khoảng 30–40 mét, được xem là một trong những thắng cảnh đá đẹp và ngoạn mục nhất Trung Ural. Cụm đá được công nhận là di tích thiên nhiên có giá trị địa mạo và thực vật (nơi mọc của nhiều loài quý hiếm), đồng thời mang cả dấu ấn lịch sử. Dân gian lưu truyền nhiều truyền thuyết lãng mạn giải thích tên gọi – từ chuyện bảy anh em hoá đá cho tới các huyền thoại về «pháp sư» hay «người khổng lồ». Ngày nay «Семь братьев» là điểm đến ưa thích cho dã ngoại, leo núi thể thao và chụp ảnh: từ trên đỉnh đá, du khách phóng tầm mắt ra biển rừng taiga trải dài và hồ nước phía dưới. Đường lên núi đi qua rừng, không quá khó, phù hợp cho chuyến đi trong ngày từ Yekaterinburg. Đây là một trong những biểu tượng thiên nhiên được yêu thích của vùng.",
    [
        "Cụm đá granit hình tháp cao ~30–40 m trên đỉnh núi Semibratskaya (422 m).",
        "Một trong những thắng cảnh đá đẹp nhất Trung Ural; di tích địa mạo – thực vật.",
        "Điểm leo núi, dã ngoại và ngắm biển rừng taiga, gắn với nhiều truyền thuyết.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do; nên đi ban ngày.",
        "ticket_vi": "Miễn phí (tự túc di chuyển và leo núi).",
        "duration_vi": "Cả buổi: đi bộ lên – xuống khoảng 2–4 giờ tuỳ điểm xuất phát.",
        "best_time_vi": "Cuối xuân đến đầu thu; tránh ngày mưa vì đá trơn.",
        "tips_vi": "Mang giày bám tốt, nước, cẩn thận khi trèo lên đỉnh đá; xuất phát tiện nhất từ Verkh-Neyvinsky.",
    },
    [
        {"title": "Wikipedia (RU) — Семь Братьев и Одна Сестра", "url": "https://ru.wikipedia.org/wiki/Семь_Братьев_и_Одна_Сестра"},
        {"title": "Ураловед — Скалы Семь Братьев", "url": "https://uraloved.ru/sem-bratyev"},
    ],
    ["rocks", "nature-monument", "hiking", "granite", "nevyansk"],
    maps_text("Скалы Семь Братьев", "Верх-Нейвинский", "Seven Brothers Rocks", "Verkh-Neyvinsky", 57.240500, 60.230667),
))

# 14) Порог Ревун (река Исеть) ------------------------------------------------
RECORDS.append(rec(
    "revun-rapids-iset",
    "Ghềnh Revun trên sông Iset",
    "Порог Ревун (Буркан)",
    "Revun Rapids on the Iset River",
    ["park_garden"],
    56.433833, 61.602583,
    "Trên sông Iset gần làng Beklenishcheva, huyện Kamensky, cách Kamensk-Uralsky khoảng 20 km, tỉnh Sverdlovsk, Nga.",
    "Ghềnh thác nổi tiếng nhất tỉnh Sverdlovsk, nơi sông Iset xuyên qua hẻm đá porphyrite – diabase dựng đứng, nước réo ầm ầm (nên có tên «Ревун» – kẻ gào thét). Điểm hẹn quen thuộc của dân chèo thuyền vượt thác, leo núi đá và dã ngoại.",
    "«Ревун» (dân địa phương còn gọi là Burkan) là ghềnh thác trên sông Iset, thuộc huyện Kamensky, cách Yekaterinburg khoảng 80 km và cách Kamensk-Uralsky chừng 20 km về phía thượng nguồn, ngay dưới làng Beklenishcheva. Tại đây dòng Iset phá vỡ lớp đá porphyrite và diabase cứng, tạo thành một đoạn ghềnh trong hẻm đá với những vách dựng đứng, nước chảy xiết và gầm réo dữ dội – chính âm thanh ấy đã sinh ra cái tên «Ревун» (kẻ gào thét). Đây là một trong những thắng cảnh thiên nhiên được yêu thích và được chụp ảnh nhiều nhất tỉnh Sverdlovsk. Vào mùa xuân khi nước lớn, ghềnh trở nên hùng vĩ và là nơi tổ chức các cuộc thi, buổi tập chèo thuyền kayak – catamaran vượt thác của dân thể thao nước khắp vùng Ural. Những vách đá hai bên cũng là điểm leo núi thể thao quen thuộc. Gần ghềnh còn có hang Smolinskaya nổi tiếng, nên khu vực thường được ghép thành một tuyến khám phá thiên nhiên trong ngày. Với cảnh quan hẻm đá – dòng nước ấn tượng, Ревун là điểm dã ngoại, cắm trại và nhiếp ảnh hấp dẫn.",
    [
        "Ghềnh thác nổi tiếng nhất tỉnh Sverdlovsk, sông Iset xuyên hẻm đá porphyrite – diabase.",
        "Điểm chèo thuyền vượt thác (kayak, catamaran) và leo núi đá của dân Ural.",
        "Đẹp và hùng vĩ nhất vào mùa xuân nước lớn; gần hang Smolinskaya.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do; nên đi ban ngày.",
        "ticket_vi": "Miễn phí (tự túc di chuyển; cắm trại tuỳ khu vực).",
        "duration_vi": "Khoảng 1–3 giờ; lâu hơn nếu kết hợp hang Smolinskaya.",
        "best_time_vi": "Cuối tháng 4 – đầu tháng 5 (nước lớn, có thi chèo thuyền); mùa hè êm hơn để dã ngoại.",
        "tips_vi": "Đá trơn, cẩn thận gần mép nước; đi ô tô tiện nhất, kết hợp thăm hang Smolinskaya gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Ревун", "url": "https://ru.wikipedia.org/wiki/Ревун"},
        {"title": "Ураловед — Порог Ревун на реке Исеть", "url": "https://uraloved.ru/porog-revun"},
    ],
    ["rapids", "iset-river", "canyon", "rafting", "kamensk-uralsky"],
    maps_text("Порог Ревун", "Каменск-Уральский", "Revun Rapids", "Kamensk-Uralsky", 56.433833, 61.602583),
))

# 15) Гора Волчиха -----------------------------------------------------------
RECORDS.append(rec(
    "volchikha-mountain",
    "Núi Volchikha (Gora Volchikha)",
    "Гора Волчиха",
    "Volchikha Mountain",
    ["park_garden"],
    56.827533, 60.003967,
    "Bên hữu ngạn sông Chusovaya, khu đô thị Pervouralsk (gần Revda), cách Yekaterinburg khoảng 40 km về phía tây, tỉnh Sverdlovsk, Nga.",
    "Đỉnh núi cao nhất trong vùng lân cận Yekaterinburg (526 m), thuộc dãy Revdinsky. Mùa đông là khu trượt tuyết được yêu thích, mùa hè là điểm leo núi ngắm toàn cảnh hồ chứa Volchikhinskoye và sông Chusovaya – nơi được ví như «ngắm châu Âu từ trên cao».",
    "Волчиха là ngọn núi ở Trung Ural, đỉnh cao nhất trong khu vực quanh Yekaterinburg với độ cao 526 mét, thuộc dãy Revdinsky. Núi nằm bên hữu ngạn sông Chusovaya, trong khu đô thị Pervouralsk gần thành phố Revda, cách Yekaterinburg khoảng 40 km về phía tây – tức đã nằm bên phần «châu Âu» của ranh giới Âu – Á, nên dân leo núi hay đùa rằng lên đỉnh Волчиха là để «ngắm châu Âu từ trên cao». Vào mùa đông, sườn núi trở thành một trong những khu trượt tuyết phổ biến nhất gần Yekaterinburg, với hệ thống đường trượt và cáp treo, thu hút đông người dân thành phố cuối tuần. Sang mùa ấm, Волчиха là điểm đi bộ – leo núi nhẹ nhàng: từ trên đỉnh, du khách phóng tầm mắt ra hồ chứa Volchikhinskoye rộng lớn (nguồn cấp nước cho Yekaterinburg), khúc uốn của sông Chusovaya và biển rừng taiga trải dài tới chân trời. Nhờ vị trí gần thành phố, cảnh quan đẹp và dễ tiếp cận, đây là điểm dã ngoại, ngắm cảnh và chụp ảnh bốn mùa được yêu thích của người dân vùng Ural.",
    [
        "Đỉnh cao nhất quanh Yekaterinburg (526 m), thuộc dãy Revdinsky.",
        "Mùa đông là khu trượt tuyết phổ biến; mùa hè là điểm leo núi ngắm cảnh.",
        "Tầm nhìn ra hồ chứa Volchikhinskoye và khúc uốn sông Chusovaya.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do; khu trượt tuyết hoạt động theo mùa và giờ riêng.",
        "ticket_vi": "Leo núi miễn phí; dịch vụ trượt tuyết (vé cáp, thuê đồ) tính phí mùa đông.",
        "duration_vi": "Đi bộ lên – xuống khoảng 1,5–3 giờ.",
        "best_time_vi": "Mùa đông cho trượt tuyết; cuối xuân đến đầu thu cho leo núi, ngắm cảnh.",
        "tips_vi": "Mang giày bám tốt và nước; mùa đông cần đồ ấm. Đi ô tô theo trục Moskovsky trakt rất tiện.",
    },
    [
        {"title": "Wikipedia (RU) — Волчиха (гора)", "url": "https://ru.wikipedia.org/wiki/Волчиха_(гора)"},
        {"title": "Ураловед / Река Чусовая — Гора Волчиха", "url": "https://rekachusovaya.ru/putevoditel/verhnaya-chusovaya/gora-volchiha/"},
    ],
    ["mountain", "viewpoint", "ski", "chusovaya", "pervouralsk"],
    maps_text("Гора Волчиха", "Ревда", "Volchikha Mountain", "Revda", 56.827533, 60.003967),
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
