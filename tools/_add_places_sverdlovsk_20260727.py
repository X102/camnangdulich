# -*- coding: utf-8 -*-
"""_add_places_sverdlovsk_20260727.py — VÙNG TIÊU ĐIỂM: Tỉnh Sverdlovsk
(lần chạy tự động 2026-07-27).

Bối cảnh: sverdlovsk.json hiện có 9 địa điểm. tatarstan (60) và nizhny-novgorod (58)
đã ≥50 => vùng tiêu điểm chuyển sang Sverdlovsk (slug kế trong danh sách ưu tiên còn <50).
Nâng dần tới ~50–100.

Đợt này bổ sung 13 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình:
- Cung điện/điền trang: Дом Севастьянова (dinh thự tân-Gothic bên hồ thành phố),
  Усадьба Расторгуева–Харитонова + Харитоновский сад (điền trang cổ điển lớn nhất TP).
- Bảo tàng: Музейный комплекс УГМК (bảo tàng kỹ thuật quân sự & ô tô lớn bậc nhất, V. Pyshma),
  Завод-музей истории горнозаводской техники (Нижний Тагил, xưởng-bảo tàng đầu tiên ở Nga),
  Нижнесинячихинский музей деревянного зодчества (kiến trúc gỗ ngoài trời), Ирбитский музей
  мотоциклов (bảo tàng mô-tô nhà nước duy nhất ở Nga).
- Nhà thờ: Крестовоздвиженский собор (Верхотурье) — nhà thờ lớn thứ ba nước Nga.
- Đài/công trình: Белая башня (tháp nước kiến tạo Uralmash), Сторожевая башня на Лисьей горе
  (biểu tượng Нижний Тагил).
- Nhà hát: Екатеринбургский театр оперы и балета («Bạch Thiên Nga»).
- Thiên nhiên: Шарташские каменные палатки, скалы Чёртово городище, озеро Тальков камень.

TOẠ ĐỘ: xác minh chéo Wikidata/Wikipedia (Севастьянов 56.83889,60.60583; Расторгуев–Харитонов
56.84583,60.61333; Белая башня 56.89306,60.57250; Шарташские п. 56.842971,60.678783;
Чёртово городище 56.9415,60.34808; Тальков камень 56.492749,60.727663; Лисья гора
57.899588,59.946822; Крестовоздвиженский собор 58.86306,60.80972 [58°51'47"N 60°48'35"E];
Ирбитский музей 57.66334,63.08893 [N57°39'48"E63°05'20"]), nguồn du lịch/địa phương
(Завод-музей НТ 57.905371,59.950334; УГМК Пышма 56.959724,60.585830; Синячиха 57.94792,61.76563
[N57°56.875'E61°45.938']; Оперный театр 56.838953,60.616702 [nashural.ru GPS]) — 2026-07.
Kiểm tra thứ tự & phạm vi (tỉnh Sverdlovsk: lat ~56,3–59,0; lon ~59,2–63,1; KHÔNG đảo lat/lon;
đều nằm trong tỉnh). Link bản đồ TRỎ-ĐỊA-ĐIỂM: ưu tiên URL trang tổ chức Yandex khi tra được
(УГМК, Ирбитский музей); còn lại text-search theo tên_ru + thành phố, canh giữa theo toạ độ đã kiểm.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_sverdlovsk_20260727.py
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

# 1) Дом Севастьянова ---------------------------------------------------------
RECORDS.append(rec(
    "sevastyanov-house",
    "Dinh thự Sevastyanov (Dom Sevastyanova)",
    "Дом Севастьянова",
    "Sevastyanov House",
    ["palace", "monument"],
    56.83889, 60.60583,
    "Проспект Ленина, 35, bên bờ đông hồ Thành phố (City Pond), trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Dinh thự lộng lẫy bên bờ hồ Thành phố được xem là một trong những toà nhà đẹp nhất Yekaterinburg. Công trình nổi bật với lối trang trí tân-Gothic pha sắc thái Moor cùng ba màu trắng – lục – đỏ hiếm gặp. Sau đợt trùng tu 2008, dinh thự trở thành dinh tiếp tân của Tổng thống Liên bang Nga tại Yekaterinburg.",
    "Đứng ngay góc phố Lenin và bờ đông hồ Thành phố, dinh thự Sevastyanov là một trong những công trình dân dụng tráng lệ và được yêu thích nhất Yekaterinburg. Toà nhà hình thành từ đầu thế kỷ 19 và được cải tạo lớn vào những năm 1860 cho viên quan Nikolai Sevastyanov, mang diện mạo độc đáo pha trộn tân-Gothic với các mô-típ Moor: những vòm nhọn, hoa văn chạm khắc tinh xảo và bảng màu trắng – lục – đỏ rất riêng, ít thấy ở kiến trúc Nga. Có nhiều giai thoại quanh chủ nhân và sự xa hoa của dinh thự, khiến nó sớm trở thành đề tài truyền miệng của người dân thành phố. Thời Xô Viết, toà nhà là Nhà Công đoàn (Дом профсоюзов). Đến năm 2008, nhân dịp thành phố chuẩn bị đón các hội nghị quốc tế lớn, dinh thự được trùng tu toàn diện và trở thành dinh tiếp tân của Tổng thống Nga tại Yekaterinburg. Vì công năng đặc biệt này, bên trong thường không mở cho khách tham quan tự do, nhưng bản thân mặt tiền rực rỡ soi bóng xuống hồ đã là một điểm ngắm và chụp ảnh không thể bỏ qua trên trục phố Lenin, gần sát quảng trường Lịch sử (Plotinka).",
    [
        "Một trong những toà nhà đẹp và độc đáo nhất Yekaterinburg, phong cách tân-Gothic pha Moor.",
        "Bảng màu trắng – lục – đỏ hiếm gặp, soi bóng bên bờ hồ Thành phố trên phố Lenin.",
        "Từ 2008 là dinh tiếp tân của Tổng thống Nga tại Yekaterinburg (thường không mở tham quan bên trong).",
    ],
    {
        "hours_vi": "Ngắm mặt ngoài mọi lúc; bên trong hạn chế/không mở tham quan tự do do là dinh tiếp tân.",
        "ticket_vi": "Ngắm bên ngoài miễn phí.",
        "duration_vi": "Khoảng 15–20 phút chụp ảnh mặt tiền.",
        "best_time_vi": "Chiều muộn và buổi tối khi toà nhà lên đèn, soi bóng xuống hồ rất đẹp.",
        "tips_vi": "Kết hợp đi bộ quảng trường Lịch sử (Plotinka) và trục phố Lenin ngay bên cạnh.",
    },
    [
        {"title": "Wikidata — Sevastyanov's house (Q4165394)", "url": "https://www.wikidata.org/wiki/Q4165394"},
        {"title": "Wikipedia (EN) — Yekaterinburg (Sevastyanov House)", "url": "https://en.wikipedia.org/wiki/Yekaterinburg"},
    ],
    ["architecture", "neo-gothic", "landmark", "city-pond", "yekaterinburg"],
    maps_text("Дом Севастьянова", "Екатеринбург", "Sevastyanov House", "Yekaterinburg", 56.83889, 60.60583),
))

# 2) Усадьба Расторгуева–Харитонова + Харитоновский сад -----------------------
RECORDS.append(rec(
    "rastorguyev-kharitonov-palace",
    "Điền trang Rastorguyev–Kharitonov và vườn Kharitonov",
    "Усадьба Расторгуева — Харитонова",
    "Rastorguyev-Kharitonov Palace",
    ["palace", "park_garden"],
    56.84583, 60.61333,
    "Улица Карла Либкнехта, 44, trên đồi Voznesenskaya, đối diện Nhà thờ Trên Máu, Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Điền trang cổ điển lớn nhất Yekaterinburg, dựng đầu thế kỷ 19 trên đồi Voznesenskaya, đối diện Nhà thờ Trên Máu. Quần thể gắn với nhiều truyền thuyết về hầm ngầm và lối đi bí mật của phái Ly khai (Old Believers). Bên cạnh là vườn Kharitonov – công viên công cộng cổ với hồ nước và đình vọng cảnh.",
    "Toạ lạc trên đồi Voznesenskaya, đối diện Nhà thờ Trên Máu, điền trang Rastorguyev–Kharitonov là quần thể kiến trúc cổ điển bề thế và lớn nhất còn lại của Yekaterinburg. Công trình được khởi dựng đầu thế kỷ 19 cho thương gia giàu có Lev Rastorguyev rồi truyền sang con rể Pyotr Kharitonov, với sự tham gia của nhiều kiến trúc sư; kết quả là một dinh cơ đồ sộ gồm toà nhà chính có hàng cột, các dãy nhà phụ, cổng và sân trong. Cả hai chủ nhân đều là tín đồ phái Ly khai giàu có, nên quanh điền trang lưu truyền vô số giai thoại ly kỳ về những căn hầm ngầm, đường hầm bí mật và cả những bi kịch gia đình. Sau Cách mạng, dinh thự được dùng cho mục đích giáo dục và ngày nay là Cung Sáng tạo Thiếu nhi. Liền kề là vườn Kharitonov (Харитоновский сад) – một trong những công viên công cộng lâu đời nhất thành phố, với hồ nước nhân tạo, hòn đảo nhỏ và đình vọng cảnh hình tròn (rotunda) đã trở thành biểu tượng quen thuộc. Đây là nơi lý tưởng để tản bộ, chèo thuyền mùa hè và kết hợp tham quan cùng Nhà thờ Trên Máu gần đó.",
    [
        "Điền trang cổ điển lớn nhất Yekaterinburg, xây đầu thế kỷ 19 cho các thương gia phái Ly khai.",
        "Gắn với nhiều truyền thuyết về hầm ngầm và lối đi bí mật.",
        "Kề bên là vườn Kharitonov với hồ nước và đình rotunda – công viên công cộng cổ nhất thành phố.",
    ],
    {
        "hours_vi": "Vườn Kharitonov mở cửa tự do ban ngày; toà điền trang là Cung Thiếu nhi, tham quan bên trong hạn chế.",
        "ticket_vi": "Dạo vườn miễn phí.",
        "duration_vi": "Khoảng 45–60 phút cho cả điền trang và vườn.",
        "best_time_vi": "Mùa hè để dạo vườn và chèo thuyền trên hồ; mùa thu lá vàng rất đẹp.",
        "tips_vi": "Kết hợp tham quan Nhà thờ Trên Máu ngay đối diện; ngắm đình rotunda soi bóng trên hồ.",
    },
    [
        {"title": "Wikipedia (EN) — Kharitonov Palace", "url": "https://en.wikipedia.org/wiki/Kharitonov_Palace"},
        {"title": "Wikidata — Rastorguyev-Kharitonov Palace (Q1984395)", "url": "https://www.wikidata.org/wiki/Q1984395"},
    ],
    ["estate", "classicism", "kharitonov-garden", "old-believers", "yekaterinburg"],
    maps_text("Усадьба Расторгуева — Харитонова", "Екатеринбург", "Rastorguyev-Kharitonov Palace", "Yekaterinburg", 56.84583, 60.61333),
))

# 3) Белая башня (Уралмаш) ----------------------------------------------------
RECORDS.append(rec(
    "white-tower-uralmash",
    "Tháp Trắng ở Uralmash (Belaya bashnya)",
    "Белая башня",
    "White Tower (Yekaterinburg)",
    ["monument", "other"],
    56.89306, 60.57250,
    "Улица Бакинских Комиссаров, 2, khu công nghiệp Uralmash, Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Tháp nước theo phong cách Kiến tạo (Constructivism) dựng năm 1929–1931 tại khu Uralmash, do kiến trúc sư Moisei Reisher thiết kế. Cao khoảng 29 m, đây là một trong những biểu tượng tiên phong của kiến trúc avant-garde Xô Viết và là biểu tượng không chính thức của Uralmash.",
    "Tháp Trắng là một trong những công trình mang tính biểu tượng nhất của kiến trúc Kiến tạo (Constructivism) Xô Viết và là niềm tự hào của khu công nghiệp Uralmash ở phía bắc Yekaterinburg. Được kiến trúc sư trẻ Moisei Reisher thiết kế và xây trong các năm 1929–1931, tháp cao khoảng 29 mét, gồm một bồn chứa nước lớn đặt trên thân trụ – nhưng thay vì che giấu công năng kỹ thuật, hình khối lại được xử lý táo bạo, khúc chiết theo tinh thần avant-garde, biến một công trình hạ tầng thành tác phẩm nghệ thuật. Đây từng là một trong những kết cấu bê tông cốt thép đầu tiên của thành phố. Khi mạng cấp nước phát triển vào thập niên 1960, tháp ngừng hoạt động và xuống cấp dần. Những năm gần đây, nhờ nỗ lực của nhóm tình nguyện viên kiến trúc, tháp được bảo tồn, phục hồi và trở thành không gian văn hoá – nơi tổ chức triển lãm, sự kiện về di sản kiến tạo. Được công nhận là di sản văn hoá, Tháp Trắng thu hút những người yêu kiến trúc và là điểm nhấn nhận diện của Uralmash.",
    [
        "Tháp nước Kiến tạo (Constructivism) 1929–1931, kiến trúc sư Moisei Reisher.",
        "Cao ~29 m, một trong những kết cấu bê tông cốt thép đầu tiên của thành phố.",
        "Biểu tượng của Uralmash; nay là không gian văn hoá sau khi được phục hồi.",
    ],
    {
        "hours_vi": "Ngắm bên ngoài mọi lúc; bên trong mở theo lịch sự kiện/triển lãm của nhóm bảo tồn.",
        "ticket_vi": "Ngắm bên ngoài miễn phí; vào trong tuỳ sự kiện.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; nên xem lịch sự kiện nếu muốn vào bên trong.",
        "tips_vi": "Nằm ở khu Uralmash khá xa trung tâm; tiện đi metro/xe tới rồi kết hợp khám phá kiến trúc Xô Viết quanh khu.",
    },
    [
        {"title": "Wikipedia (EN) — White Tower (Yekaterinburg)", "url": "https://en.wikipedia.org/wiki/White_Tower_(Yekaterinburg)"},
        {"title": "Ủy ban UNESCO Nga — Bạch Tháp (Белая башня)", "url": "https://unesco.ru/en/news/45-belaya-bashnya/"},
    ],
    ["constructivism", "avant-garde", "water-tower", "uralmash", "heritage"],
    maps_text("Белая башня", "Екатеринбург", "White Tower", "Yekaterinburg", 56.89306, 60.57250),
))

# 4) Шарташские каменные палатки ----------------------------------------------
RECORDS.append(rec(
    "shartash-stone-tents",
    "Lều Đá hồ Shartash (Shartashskie kamennye palatki)",
    "Шарташские каменные палатки",
    "Shartash Stone Tents",
    ["park_garden", "monument"],
    56.842971, 60.678783,
    "Улица Владимира Высоцкого, 11, gần hồ Shartash, rìa đông Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Di tích thiên nhiên cấp vùng ngay trong Yekaterinburg, gần hồ Shartash: những khối đá granite xếp chồng lên nhau như các phiến bàn (matrasnye), tạo thành «lều đá» đặc trưng hình thành hàng trăm triệu năm trước. Quanh hồ từng có nhiều di chỉ khảo cổ của người cổ đại.",
    "Nằm ở rìa đông Yekaterinburg, sát bờ hồ Shartash, Lều Đá Shartash là một di tích thiên nhiên cấp vùng và cũng là điểm dã ngoại quen thuộc của người dân thành phố. «Lều đá» là những cụm đá granite khổng lồ bị phong hoá thành các phiến phẳng xếp chồng lên nhau tựa như nệm (dạng đá matrasovidnye), hình thành từ khối granite có tuổi khoảng 300 triệu năm. Từ trên các phiến đá cao có thể phóng tầm mắt ra mặt hồ và rừng thông xung quanh. Khu vực này không chỉ có giá trị địa chất mà còn giàu ý nghĩa khảo cổ: theo các nghiên cứu, ven hồ Shartash từng tồn tại nhiều điểm cư trú và trại săn của người cổ đại, với những dấu tích sớm nhất được cho là thuộc thiên niên kỷ thứ 3 trước Công nguyên. Ngày nay, nhờ nằm ngay trong ranh giới thành phố và dễ tiếp cận, Lều Đá Shartash là nơi lý tưởng để đi bộ, leo trèo nhẹ, ngắm cảnh và picnic cuối tuần. Là di tích thiên nhiên, du khách được nhắc giữ gìn cảnh quan, không viết vẽ lên đá và không xả rác.",
    [
        "Đá granite phong hoá xếp chồng dạng phiến («lều đá»), tuổi khoảng 300 triệu năm.",
        "Di tích thiên nhiên cấp vùng, nằm ngay trong Yekaterinburg, gần hồ Shartash.",
        "Khu vực giàu di chỉ khảo cổ của người cổ đại quanh hồ.",
    ],
    {
        "hours_vi": "Không gian ngoài trời, tham quan ban ngày.",
        "ticket_vi": "Vào tự do (miễn phí).",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; sáng hoặc chiều mát để leo đá và ngắm hồ.",
        "tips_vi": "Mang giày bám tốt khi leo phiến đá; giữ gìn cảnh quan, không viết vẽ lên đá.",
    },
    [
        {"title": "Wikipedia (RU) — Шарташские каменные палатки", "url": "https://ru.wikipedia.org/wiki/Шарташские_каменные_палатки"},
        {"title": "Ураловед — Шарташские каменные палатки", "url": "https://uraloved.ru/shartashskie-kamennie-palatki"},
    ],
    ["nature", "granite", "rocks", "natural-monument", "shartash", "archaeology"],
    maps_text("Шарташские каменные палатки", "Екатеринбург", "Shartash Stone Tents", "Yekaterinburg", 56.842971, 60.678783),
))

# 5) Скалы Чёртово городище ---------------------------------------------------
RECORDS.append(rec(
    "chertovo-gorodishche-rocks",
    "Núi đá Chyortovo Gorodishche («Thành Quỷ»)",
    "Скалы Чёртово городище",
    "Chertovo Gorodishche Rocks",
    ["park_garden", "other"],
    56.9415, 60.34808,
    "Cách Yekaterinburg khoảng 25 km về phía tây bắc, gần làng Iset, tỉnh Sverdlovsk, Nga.",
    "Một trong những «tác phẩm điêu khắc thiên nhiên» nổi tiếng nhất vùng ngoại ô Yekaterinburg: dải đá granite dựng đứng trên đỉnh núi cùng tên (cao 347 m), phần chóp là bức tường đá răng lược cao khoảng 20 m. Đá được tạo thành từ granite núi lửa khoảng 300 triệu năm trước.",
    "Chyortovo Gorodishche («Thành Quỷ») là một trong những núi đá kỳ vĩ và được ưa thích nhất trong vùng phụ cận Yekaterinburg, nằm cách thành phố khoảng 25 km về phía tây bắc và cách làng Iset chừng 6 km. Đỉnh núi cao 347 mét so với mực nước biển, nhưng gây ấn tượng mạnh nhất là 20 mét cuối cùng: một dải tường đá granite dựng đứng, xếp thành hàng răng lược chạy từ đông nam sang tây bắc, trông như bức thành do bàn tay khổng lồ dựng nên – nguồn gốc của cái tên «Thành Quỷ» trong dân gian. Khối granite ở đây có nguồn gốc núi lửa, hình thành khoảng 300 triệu năm trước và bị phong hoá thành các phiến chồng lớp đặc trưng. Từ trên đỉnh, du khách được thưởng cảnh rừng taiga bạt ngàn của vùng Trung Ural. Đây là điểm đi bộ đường dài (hiking) và leo núi thể thao rất phổ biến; để lên chóp đá có lắp một cầu thang gỗ hỗ trợ. Là di tích thiên nhiên cấp vùng, khu vực thu hút đông người vào cuối tuần, thường kết hợp với các cụm đá lân cận (như đá Petra Gronskogo). Du khách nên đi giày phù hợp, cẩn trọng khi leo và giữ gìn cảnh quan.",
    [
        "Dải tường đá granite răng lược cao ~20 m trên đỉnh núi 347 m.",
        "Granite núi lửa khoảng 300 triệu năm tuổi; di tích thiên nhiên cấp vùng.",
        "Điểm hiking và leo núi nổi tiếng gần Yekaterinburg, có cầu thang gỗ lên chóp.",
    ],
    {
        "hours_vi": "Không gian thiên nhiên mở; nên đi ban ngày, thời tiết khô ráo.",
        "ticket_vi": "Vào tự do (miễn phí).",
        "duration_vi": "Nửa ngày (gồm đi bộ tiếp cận từ bãi đỗ/ga gần nhất).",
        "best_time_vi": "Cuối xuân đến đầu thu; tránh khi đá trơn ướt sau mưa hoặc băng giá.",
        "tips_vi": "Mang giày leo núi và nước; cẩn trọng ở đoạn chóp đá và cầu thang; giữ gìn cảnh quan.",
    },
    [
        {"title": "Wikipedia (RU) — Чёртово городище (гора)", "url": "https://ru.wikipedia.org/wiki/Чёртово_городище_(гора)"},
        {"title": "Ураловед — Гора Чёртово Городище", "url": "https://uraloved.ru/chertovo-gorodishe"},
    ],
    ["nature", "granite", "rocks", "hiking", "natural-monument", "middle-urals"],
    maps_text("Скалы Чёртово городище", "Исеть", "Chertovo Gorodishche Rocks", "Iset", 56.9415, 60.34808),
))

# 6) Озеро Тальков камень -----------------------------------------------------
RECORDS.append(rec(
    "talkov-kamen-lake",
    "Hồ Talkov Kamen (mỏ talc ngập nước)",
    "Озеро Тальков камень",
    "Talkov Kamen Lake",
    ["park_garden", "other"],
    56.492749, 60.727663,
    "Cách thành phố Sysert khoảng 4 km về phía tây, trong công viên thiên nhiên «Bazhov Places», tỉnh Sverdlovsk, Nga.",
    "Hồ nhân tạo tuyệt đẹp hình thành từ một mỏ khai thác talc bị bỏ hoang rồi ngập nước, nằm trong công viên thiên nhiên «Những nơi của Bazhov» gần Sysert. Vách hồ là những lớp đá phiến talc dựng đứng, nước sâu tới hơn 30 m, phản chiếu rừng thông tạo khung cảnh nên thơ.",
    "Talkov Kamen là một hồ nước nhỏ nhưng ngoạn mục, nằm cách thị trấn Sysert khoảng 4 km về phía tây, trong ranh giới công viên thiên nhiên «Những nơi của Bazhov» (Bazhovskie mesta) – vùng đất gắn với nhà văn Ural Pavel Bazhov. Hồ không phải do tự nhiên tạo ra mà là dấu tích của một mỏ khai thác talc (đá phấn) hoạt động vào cuối thế kỷ 19 – đầu thế kỷ 20. Khi việc khai thác dừng lại và các máy bơm thoát nước ngừng chạy, nước ngầm và nước mưa dần dâng lên lấp đầy moong mỏ, tạo thành một hồ nước trong xanh có chỗ sâu tới hơn 30 mét. Bao quanh hồ là những vách đá phiến talc dựng đứng, xám ánh bạc, xen giữa rừng thông, tạo nên khung cảnh vừa hùng vĩ vừa nên thơ soi bóng xuống mặt nước. Ngày nay đây là điểm dã ngoại, tắm mát mùa hè và chụp ảnh rất được ưa chuộng của người dân Yekaterinburg và vùng lân cận; quanh hồ có đường mòn đi bộ và khu vực nghỉ. Vì nằm trong công viên thiên nhiên, du khách cần tuân thủ quy định bảo vệ cảnh quan.",
    [
        "Hồ hình thành từ mỏ talc bỏ hoang ngập nước, sâu hơn 30 m.",
        "Vách đá phiến talc dựng đứng xen rừng thông, soi bóng mặt nước rất đẹp.",
        "Nằm trong công viên thiên nhiên «Những nơi của Bazhov» gần Sysert.",
    ],
    {
        "hours_vi": "Không gian thiên nhiên mở; tham quan ban ngày.",
        "ticket_vi": "Có thể thu phí vào công viên thiên nhiên/bãi đỗ; bản thân hồ vào tự do.",
        "duration_vi": "Nửa ngày (gồm đi bộ từ cổng công viên).",
        "best_time_vi": "Mùa hè để tắm và dã ngoại; mùa thu ngắm lá vàng ven hồ.",
        "tips_vi": "Cẩn trọng khi bơi vì nước sâu và lạnh; giữ gìn cảnh quan; kết hợp thăm các điểm khác của công viên Bazhov.",
    },
    [
        {"title": "Wikipedia (RU) — Тальков Камень", "url": "https://ru.wikipedia.org/wiki/Тальков_Камень"},
        {"title": "Ураловед — Озеро Тальков Камень", "url": "https://uraloved.ru/ozero-talkov-kamen"},
    ],
    ["nature", "lake", "flooded-quarry", "talc", "bazhov-places", "sysert"],
    maps_text("Озеро Тальков Камень", "Сысерть", "Talkov Kamen Lake", "Sysert", 56.492749, 60.727663),
))

# 7) Сторожевая башня на Лисьей горе (Нижний Тагил) ---------------------------
RECORDS.append(rec(
    "lisya-gora-watchtower",
    "Tháp canh trên núi Lisya (Lisya gora), Nizhny Tagil",
    "Сторожевая башня на Лисьей горе",
    "Watchtower on Lisya Gora",
    ["monument", "other"],
    57.899588, 59.946822,
    "Улица Лисогорская, đỉnh núi Lisya (Lysaya), trung tâm thành phố Nizhny Tagil, tỉnh Sverdlovsk, Nga.",
    "Tháp canh nhỏ xây đầu thế kỷ 19 theo phong cách cổ điển trên đỉnh núi Lisya (Núi Cáo) giữa trung tâm Nizhny Tagil. Đây là điểm nhấn kiến trúc và biểu tượng chính của thành phố, đồng thời được ví là «bảo tàng nhỏ nhất nước Nga».",
    "Vươn lên trên đỉnh núi Lisya (còn gọi là Lysaya – Núi Trọc/Núi Cáo) ngay giữa trung tâm Nizhny Tagil, tháp canh Lisegorskaya là biểu tượng dễ nhận ra nhất của thành phố công nghiệp này. Tháp được dựng vào đầu thế kỷ 19 theo phong cách cổ điển (classicism); qua thời gian nó từng đảm nhận nhiều vai trò khác nhau như trạm quan sát hoả hoạn, đài quan trắc, trạm tín hiệu. Dù kích thước khiêm tốn, vị trí đắc địa trên đỉnh đồi khiến tháp trở thành điểm cao ngắm toàn cảnh thành phố, hồ Tagil và các nhà máy lịch sử phía dưới. Sau đợt trùng tu, bên trong tháp mở một không gian trưng bày tí hon giới thiệu lịch sử ngọn đồi và thành phố – được quảng bá vui là «bảo tàng nhỏ nhất nước Nga». Leo lên Lisya gora và tháp canh là trải nghiệm gần như bắt buộc với du khách tới Nizhny Tagil, đặc biệt vào lúc hoàng hôn khi cả thành phố công nghiệp trải ra trong ánh chiều.",
    [
        "Tháp canh cổ điển đầu thế kỷ 19 trên đỉnh núi Lisya – biểu tượng của Nizhny Tagil.",
        "Điểm ngắm toàn cảnh thành phố, hồ Tagil và các nhà máy lịch sử.",
        "Bên trong là không gian trưng bày được ví «bảo tàng nhỏ nhất nước Nga».",
    ],
    {
        "hours_vi": "Lên đồi tự do; phòng trưng bày trong tháp mở theo giờ (thường mùa ấm), nên kiểm tra trước.",
        "ticket_vi": "Lên đồi miễn phí; vào trưng bày trong tháp có vé nhỏ.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; đẹp nhất vào hoàng hôn.",
        "tips_vi": "Đường lên hơi dốc, mang giày phù hợp; kết hợp tham quan xưởng-bảo tàng dưới chân đồi.",
    },
    [
        {"title": "Wikipedia (RU) — Сторожевая башня (Нижний Тагил)", "url": "https://ru.wikipedia.org/wiki/Сторожевая_башня_(Нижний_Тагил)"},
        {"title": "Wikipedia (RU) — Лисья гора", "url": "https://ru.wikipedia.org/wiki/Лисья_гора"},
    ],
    ["landmark", "watchtower", "classicism", "viewpoint", "nizhny-tagil"],
    maps_text("Сторожевая башня на Лисьей горе", "Нижний Тагил", "Watchtower on Lisya Gora", "Nizhny Tagil", 57.899588, 59.946822),
))

# 8) Завод-музей истории горнозаводской техники (Нижний Тагил) ----------------
RECORDS.append(rec(
    "nizhny-tagil-factory-museum",
    "Xưởng–bảo tàng lịch sử kỹ thuật luyện kim Nizhny Tagil",
    "Завод-музей истории горнозаводской техники",
    "Factory-Museum of Mining and Metallurgy History",
    ["museum"],
    57.905371, 59.950334,
    "Проспект Ленина, 1 (khu xưởng cũ trên sông Tagil), thành phố Nizhny Tagil, tỉnh Sverdlovsk, Nga.",
    "Xưởng luyện gang – thép cổ của dòng họ Demidov (khởi nguồn từ năm 1725) được bảo tồn nguyên trạng và biến thành bảo tàng ngoài trời – được xem là xưởng-bảo tàng đầu tiên của nước Nga. Nơi đây trưng bày dây chuyền, lò cao, máy móc luyện kim qua các thời kỳ.",
    "Nizhny Tagil ra đời và lớn lên nhờ nghề khai mỏ – luyện kim của dòng họ Demidov, và không nơi nào kể câu chuyện đó rõ hơn Xưởng–bảo tàng lịch sử kỹ thuật luyện kim. Đây chính là khu nhà máy gang – sắt cổ, có nguồn gốc từ xưởng Demidov khởi dựng năm 1725, sau khi ngừng sản xuất đã được giữ lại gần như nguyên trạng và chuyển thành bảo tàng ngoài trời – thường được nhắc tới như xưởng-bảo tàng (zavod-muzey) đầu tiên của nước Nga. Trên khuôn viên bên bờ sông Tagil, du khách có thể đi giữa những lò cao, đập nước, cầu trục, đường ray, máy hơi nước và các dây chuyền luyện kim thuộc nhiều thời kỳ, hình dung được cả một thời đại công nghiệp đã tạo nên «vương quốc sắt thép» của vùng Ural. Xưởng-bảo tàng là hạt nhân của Khu bảo tồn – bảo tàng «Gornozavodskoy Ural», cùng với các bảo tàng vệ tinh khác trong thành phố. Với những ai quan tâm tới di sản công nghiệp, lịch sử Demidov và kỹ thuật luyện kim, đây là điểm đến độc đáo bậc nhất nước Nga, kết hợp tốt với việc leo núi Lisya gora ngay gần đó.",
    [
        "Xưởng luyện kim Demidov (gốc từ 1725) bảo tồn nguyên trạng làm bảo tàng ngoài trời.",
        "Được xem là xưởng-bảo tàng (zavod-muzey) đầu tiên của nước Nga.",
        "Trưng bày lò cao, đập nước, cầu trục, máy móc luyện kim qua các thời kỳ.",
    ],
    {
        "hours_vi": "Theo giờ của Khu bảo tồn «Gornozavodskoy Ural»; tham quan ngoài trời thường vào mùa ấm.",
        "ticket_vi": "Có vé vào cửa; nên đặt tour có hướng dẫn để hiểu dây chuyền công nghệ.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu (khu ngoài trời).",
        "tips_vi": "Mang giày đi bộ; kết hợp leo tháp canh Lisya gora và các bảo tàng khác của thành phố.",
    },
    [
        {"title": "Wikipedia (RU) — Завод-музей истории горнозаводской техники", "url": "https://ru.wikipedia.org/wiki/Завод-музей_истории_горнозаводской_техники"},
        {"title": "museum-nt.ru — Нижнетагильский музей-заповедник «Горнозаводской Урал»", "url": "https://museum-nt.ru/"},
    ],
    ["museum", "industrial-heritage", "demidov", "metallurgy", "open-air", "nizhny-tagil"],
    maps_text("Завод-музей истории горнозаводской техники", "Нижний Тагил", "Factory-Museum of Mining and Metallurgy History", "Nizhny Tagil", 57.905371, 59.950334),
))

# 9) Крестовоздвиженский собор (Верхотурье) -----------------------------------
RECORDS.append(rec(
    "verkhoturye-krestovozdvizhensky-cathedral",
    "Nhà thờ Suy Tôn Thánh Giá ở Verkhoturye (Krestovozdvizhensky sobor)",
    "Крестовоздвиженский собор (Верхотурье)",
    "Exaltation of the Cross Cathedral (Verkhoturye)",
    ["church", "monument"],
    58.86306, 60.80972,
    "Улица Воинская, 1А, trong Tu viện Thánh Nicholas (Nikolaevsky), thành phố Verkhoturye, tỉnh Sverdlovsk, Nga.",
    "Thánh đường khổng lồ trong Tu viện Thánh Nicholas ở Verkhoturye – được coi là nhà thờ lớn thứ ba nước Nga về thể tích, chỉ sau Nhà thờ Chúa Cứu Thế (Moskva) và Nhà thờ Thánh Isaac (Saint Petersburg). Khởi công 1905, thánh hiến 1913, nơi lưu giữ di hài Thánh Simeon xứ Verkhoturye.",
    "Verkhoturye được mệnh danh là «thủ đô tâm linh của vùng Ural», và công trình gây choáng ngợp nhất nơi đây là Nhà thờ Suy Tôn Thánh Giá (Krestovozdvizhensky sobor) trong Tu viện nam Thánh Nicholas. Được khởi công năm 1905 và thánh hiến năm 1913 nhân dịp kỷ niệm 300 năm triều đại Romanov, thánh đường có quy mô đồ sộ theo phong cách Nga – Byzantine và thường được xếp là nhà thờ lớn thứ ba nước Nga xét theo thể tích, chỉ sau Nhà thờ Chúa Cứu Thế ở Moskva và Nhà thờ Thánh Isaac ở Saint Petersburg. Điểm đặc biệt của nội thất là những bộ khung thờ (iconostasis) bằng gốm sứ tráng men – một giải pháp hiếm gặp và rất ấn tượng. Nhà thờ là nơi tôn kính và lưu giữ di hài Thánh Simeon xứ Verkhoturye, vị thánh bảo trợ của vùng Ural, nên hằng năm thu hút đông đảo tín đồ hành hương. Cùng với điện Kremlin Verkhoturye ở gần đó, tu viện và thánh đường tạo nên một quần thể lịch sử – tôn giáo bậc nhất của tỉnh Sverdlovsk, đưa du khách trở về với cội nguồn của quá trình người Nga khai phá Siberia qua «cửa ngõ» Verkhoturye.",
    [
        "Được coi là nhà thờ lớn thứ ba nước Nga về thể tích.",
        "Khởi công 1905, thánh hiến 1913; phong cách Nga–Byzantine với iconostasis bằng gốm men.",
        "Nơi lưu giữ di hài Thánh Simeon xứ Verkhoturye – điểm hành hương lớn của vùng Ural.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ tu viện và giờ lễ, thường ban ngày.",
        "ticket_vi": "Vào tự do; tuỳ tâm công đức.",
        "duration_vi": "Khoảng 45–60 phút cho cả tu viện.",
        "best_time_vi": "Cuối xuân đến đầu thu; dịp lễ Thánh Simeon rất đông khách hành hương.",
        "tips_vi": "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu; kết hợp thăm điện Kremlin Verkhoturye gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Собор Воздвижения Креста Господня (Верхотурье)", "url": "https://ru.wikipedia.org/wiki/Собор_Воздвижения_Креста_Господня_(Верхотурье)"},
        {"title": "sobory.ru — Верхотурье, Николаевский монастырь, собор Воздвижения Креста (object 05754)", "url": "https://sobory.ru/article/?object=05754"},
    ],
    ["cathedral", "monastery", "pilgrimage", "verkhoturye", "simeon", "romanov-300"],
    maps_text("Крестовоздвиженский собор", "Верхотурье", "Exaltation of the Cross Cathedral", "Verkhoturye", 58.86306, 60.80972),
))

# 10) Ирбитский государственный музей мотоциклов ------------------------------
RECORDS.append(rec(
    "irbit-motorcycle-museum",
    "Bảo tàng Mô-tô Quốc gia Irbit (Irbitsky muzey mototsiklov)",
    "Ирбитский государственный музей мотоциклов",
    "Irbit State Motorcycle Museum",
    ["museum"],
    57.66334, 63.08893,
    "Улица Советская, 100А, thành phố Irbit, tỉnh Sverdlovsk, Nga.",
    "Bảo tàng mô-tô cấp nhà nước duy nhất ở Nga, đặt tại Irbit – quê hương của nhà máy mô-tô Ural (IMZ). Bộ sưu tập gồm khoảng 120 mẫu xe trong và ngoài nước (Anh, Đức, Mỹ, Nhật) sản xuất từ 1935 đến 1989, cùng nhiều mẫu Ural quân sự và dân dụng.",
    "Thành phố nhỏ Irbit ở phía đông tỉnh Sverdlovsk nổi tiếng khắp nước Nga nhờ nhà máy mô-tô Ural (IMZ) – nơi cho ra đời những chiếc mô-tô ba bánh có thùng bên (sidecar) huyền thoại từ thời Chiến tranh Vệ quốc Vĩ đại. Chính vì thế, Irbit là nơi đặt Bảo tàng Mô-tô Quốc gia – bảo tàng mô-tô cấp nhà nước duy nhất của nước Nga, chính thức mở cửa năm 2004. Bộ sưu tập quy tụ khoảng 120 mẫu xe, trong đó có các dòng mô-tô hạng nặng nội địa từ thập niên 1940 trở đi, những nguyên mẫu thử nghiệm hiếm và cả các mẫu xe của những hãng lừng danh nước ngoài (Anh, Đức, Mỹ, Nhật) sản xuất trong giai đoạn 1935–1989. Nhiều hiện vật gắn với các kỷ lục, chuyến đi vòng quanh thế giới hoặc lịch sử quân sự, giúp người xem hình dung cả một chương phát triển của ngành công nghiệp mô-tô Nga và thế giới. Đây là điểm đến hấp dẫn không chỉ với dân mê xe mà cả gia đình và những ai muốn khám phá một Irbit từng là thị trấn hội chợ sầm uất của vùng Ural.",
    [
        "Bảo tàng mô-tô cấp nhà nước duy nhất ở Nga, mở cửa năm 2004.",
        "Khoảng 120 mẫu xe, gồm cả Ural nội địa và các hãng Anh, Đức, Mỹ, Nhật (1935–1989).",
        "Đặt tại Irbit – quê hương nhà máy mô-tô Ural (IMZ).",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–thứ Bảy (giờ hành chính), nghỉ Chủ nhật và thứ Hai; nên kiểm tra lịch trước.",
        "ticket_vi": "Có vé vào cửa; nên đặt trước cho đoàn/tour có hướng dẫn.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Irbit cách Yekaterinburg khá xa (~200 km), nên đi trong ngày bằng ô tô; kết hợp thăm phố cổ hội chợ Irbit.",
    },
    [
        {"title": "Wikipedia (RU) — Ирбитский государственный музей мотоциклов", "url": "https://ru.wikipedia.org/wiki/Ирбитский_государственный_музей_мотоциклов"},
        {"title": "Культура.РФ — Ирбитский государственный музей мотоциклов", "url": "https://www.culture.ru/institutes/6622/irbitskii-gosudarstvennyi-muzei-motociklov"},
    ],
    ["museum", "motorcycles", "ural-imz", "irbit", "technology"],
    maps_org("https://yandex.com/maps/org/muzey_mototsiklov/1047427073/", "Irbit State Motorcycle Museum", "Irbit"),
))

# 11) Музейный комплекс УГМК (военной и автомобильной техники), Верхняя Пышма -
RECORDS.append(rec(
    "ummc-museum-verkhnyaya-pyshma",
    "Tổ hợp Bảo tàng kỹ thuật quân sự & ô tô UGMK (Verkhnyaya Pyshma)",
    "Музейный комплекс УГМК военной и автомобильной техники",
    "UMMC Museum Complex of Military and Automotive Equipment",
    ["museum"],
    56.959724, 60.585830,
    "Улица Александра Козицына, 2, thành phố Verkhnyaya Pyshma, tỉnh Sverdlovsk, Nga (giáp ranh phía bắc Yekaterinburg).",
    "Một trong những bảo tàng kỹ thuật quân sự và ô tô lớn nhất thế giới, do Tập đoàn Luyện kim Ural (UGMK) xây dựng tại Verkhnyaya Pyshma. Khai trương ngày 9/5/2005, khu phức hợp rộng khoảng 13 ha với nhiều toà trưng bày và khu ngoài trời, quy tụ tới 15.000 hiện vật, gồm ~1.500 phương tiện quân sự và dân dụng.",
    "Chỉ cách trung tâm Yekaterinburg một quãng ngắn về phía bắc, thành phố vệ tinh Verkhnyaya Pyshma là nơi đặt một trong những bảo tàng kỹ thuật ấn tượng nhất nước Nga: Tổ hợp Bảo tàng UGMK. Được Tập đoàn Khai mỏ – Luyện kim Ural (UGMK) đầu tư và khai trương đúng ngày Chiến thắng 9/5/2005 nhân 60 năm kết thúc Chiến tranh Vệ quốc Vĩ đại, bảo tàng không ngừng mở rộng và nay là một khu phức hợp rộng khoảng 13 ha gồm nhiều trung tâm trưng bày kết hợp khu triển lãm ngoài trời. Bộ sưu tập lên tới khoảng 15.000 hiện vật, trong đó có chừng 1.500 phương tiện quân sự và dân dụng: xe tăng, pháo tự hành, xe bọc thép, đầu máy và toa tàu bọc thép, máy bay chiến đấu, cùng bộ sưu tập xe hơi và mô-tô cổ vào loại phong phú nhất nước Nga (kể cả xe đua Xô Viết và một số khí tài Lend-Lease của Mỹ như xe tăng Sherman, Stuart). Từ năm 2011, bảo tàng trở thành chi nhánh của Bảo tàng Trung ương Lực lượng Vũ trang Liên bang Nga. Với quy mô hoành tráng và cách trưng bày hiện đại, đây là điểm đến hàng đầu cho gia đình, người mê lịch sử quân sự và xe cộ khi tới vùng Ural.",
    [
        "Một trong những bảo tàng kỹ thuật quân sự & ô tô lớn nhất thế giới, do UGMK xây dựng.",
        "Khai trương 9/5/2005; ~13 ha, tới 15.000 hiện vật gồm ~1.500 phương tiện (tăng, pháo, máy bay, xe cổ).",
        "Từ 2011 là chi nhánh của Bảo tàng Trung ương Lực lượng Vũ trang Nga.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật (khoảng 10:00–19:00); nghỉ thứ Hai; nên kiểm tra lịch trước.",
        "ticket_vi": "Có vé vào cửa cho các toà trưng bày; khu ngoài trời một số phần xem tự do.",
        "duration_vi": "Khoảng 2–3 giờ cho toàn khu phức hợp.",
        "best_time_vi": "Quanh năm; khu ngoài trời đẹp và thoải mái nhất vào mùa ấm.",
        "tips_vi": "Đi từ Yekaterinburg rất tiện (xe buýt/ô tô ~30–40 phút); dành đủ thời gian vì khu rất rộng.",
    },
    [
        {"title": "Wikipedia (EN) — UMMC Museum Complex", "url": "https://en.wikipedia.org/wiki/UMMC_Museum_Complex"},
        {"title": "Культура.РФ — Музей военной техники УГМК", "url": "https://www.culture.ru/institutes/53301/muzei-voennoi-tekhniki-ugmk"},
    ],
    ["museum", "military", "vehicles", "ugmk", "verkhnyaya-pyshma", "open-air"],
    maps_org("https://yandex.ru/maps/org/muzey_voyennoy_tekhniki_ugmk/67679774434/", "UMMC Museum of Military Equipment", "Verkhnyaya Pyshma"),
))

# 12) Нижнесинячихинский музей-заповедник деревянного зодчества --------------
RECORDS.append(rec(
    "nizhnyaya-sinyachikha-museum",
    "Bảo tàng ngoài trời kiến trúc gỗ Nizhnyaya Sinyachikha",
    "Нижнесинячихинский музей-заповедник деревянного зодчества и народного искусства",
    "Nizhnyaya Sinyachikha Museum of Wooden Architecture",
    ["museum", "park_garden"],
    57.94792, 61.76563,
    "Улица Первомайская, 20, làng Nizhnyaya Sinyachikha, huyện Alapayevsky, tỉnh Sverdlovsk, Nga.",
    "Bảo tàng ngoài trời về kiến trúc gỗ và nghệ thuật dân gian Ural, do nhà bảo tồn Ivan Samoylov gây dựng, mở cửa năm 1978. Trong khuôn viên bên sông Sinyachikha quy tụ nhà gỗ (izba), nhà nguyện, tháp canh, cối xay gió… cùng bộ sưu tập tranh vẽ trang trí nhà cửa (rospis) đặc trưng vùng Ural.",
    "Nằm ở làng Nizhnyaya Sinyachikha, cách Alapayevsk không xa về phía bắc Yekaterinburg, đây là một trong những bảo tàng ngoài trời hấp dẫn nhất vùng Ural về kiến trúc gỗ và nghệ thuật dân gian. Bảo tàng là thành quả tâm huyết cả đời của ông Ivan Danilovich Samoylov – người đã bỏ nhiều thập niên để tìm kiếm, phục dựng và di dời các công trình gỗ cổ từ khắp vùng về đây; bảo tàng chính thức mở cửa năm 1978. Trên diện tích rộng bên bờ sông Sinyachikha, du khách như lạc vào một ngôi làng Ural xưa với những căn nhà gỗ (izba) qua các thế kỷ, nhà nguyện, tháp canh, cối xay gió, chòi canh lửa, kho thóc… được sắp đặt sinh động. Trái tim của bảo tàng là nhà thờ Spaso-Preobrazhenskaya theo phong cách Baroque Ural, nơi trưng bày bộ sưu tập độc đáo về tranh vẽ trang trí nội thất nhà nông dân (roспись) – nghệ thuật vẽ hoa lá, chim muông rực rỡ lên tường, cửa chớp và đồ dùng, vốn là nét đặc sắc của văn hoá dân gian Ural. Đây là điểm đến lý tưởng để hiểu đời sống, tín ngưỡng và thẩm mỹ của cư dân Ural xưa, kết hợp tốt với hành trình khám phá vùng Alapayevsk giàu di tích.",
    [
        "Bảo tàng ngoài trời về nhà gỗ (izba), nhà nguyện, tháp canh, cối xay… của vùng Ural.",
        "Do Ivan Samoylov gây dựng, mở cửa năm 1978, bên bờ sông Sinyachikha.",
        "Bộ sưu tập tranh vẽ trang trí nhà cửa (rospis) Ural trong nhà thờ Baroque Spaso-Preobrazhenskaya.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày ban ngày; kiểm tra lịch mùa đông vì một số phần ngoài trời.",
        "ticket_vi": "Có vé vào cửa; có thể mua vé lẻ hoặc trọn gói các công trình.",
        "duration_vi": "Khoảng 1,5–2 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu để dạo khu ngoài trời; mùa đông cảnh tuyết cũng rất đẹp.",
        "tips_vi": "Cách Yekaterinburg ~150 km, nên đi ô tô trong ngày; kết hợp thăm các di tích vùng Alapayevsk.",
    },
    [
        {"title": "museum.ru — Нижнесинячихинский музей-заповедник деревянного зодчества им. И.Д. Самойлова", "url": "http://www.museum.ru/M1961"},
        {"title": "Ураловед — Нижняя Синячиха и музей-заповедник деревянного зодчества", "url": "https://uraloved.ru/nizhnaya-sinyachiha"},
    ],
    ["museum", "wooden-architecture", "folk-art", "open-air", "samoylov", "alapayevsky"],
    maps_text("Нижнесинячихинский музей-заповедник деревянного зодчества", "Нижняя Синячиха", "Nizhnyaya Sinyachikha Museum of Wooden Architecture", "Nizhnyaya Sinyachikha", 57.94792, 61.76563),
))

# 13) Екатеринбургский театр оперы и балета -----------------------------------
RECORDS.append(rec(
    "yekaterinburg-opera-ballet-theatre",
    "Nhà hát Opera và Ballet Yekaterinburg («Bạch Thiên Nga»)",
    "Екатеринбургский театр оперы и балета",
    "Yekaterinburg Opera and Ballet Theatre",
    ["theatre"],
    56.838953, 60.616702,
    "Проспект Ленина, 46А, quảng trường Công xã Paris, trung tâm Yekaterinburg, tỉnh Sverdlovsk, Nga.",
    "Nhà hát opera và ballet lâu đời của Yekaterinburg, khánh thành năm 1912, tọa lạc trên quảng trường Công xã Paris giữa trục phố Lenin. Toà nhà tân-baroque duyên dáng được người dân trìu mến gọi là «Bạch Thiên Nga»; ngày nay hoạt động dưới thương hiệu «Ural Opera Ballet».",
    "Đứng giữa quảng trường Công xã Paris trên trục phố Lenin, Nhà hát Opera và Ballet Yekaterinburg là một trong những công trình đẹp và giàu lịch sử nhất thành phố. Toà nhà được xây dựng chỉ trong khoảng hai năm và khánh thành vào tháng 9 năm 1912 bằng vở opera «Cuộc đời vì Sa hoàng» của Mikhail Glinka. Thiết kế thắng cuộc thi kiến trúc toàn Nga thuộc về kỹ sư Vladimir Semyonov, còn người hiện thực hoá công trình là kiến trúc sư Konstantin Babykin – người được coi là ông tổ của trường phái kiến trúc Ural. Với mặt tiền tân-baroque thanh thoát, những nàng thơ (muse) trên đỉnh và âm học tuyệt vời, nhà hát sớm được người dân trìu mến gọi là «Bạch Thiên Nga». Từ giữa thập niên 1920, sân khấu này nổi danh là một trong những «phòng thí nghiệm của opera Xô Viết», nơi khởi nghiệp của nhiều giọng ca lừng danh như Sergei Lemeshev và Ivan Kozlovsky; năm 1966 nhà hát được phong danh hiệu «hàn lâm». Ngày nay, dưới thương hiệu «Ural Opera Ballet», đây là một trong những nhà hát opera – ballet hàng đầu ngoài hai thủ đô, với các chương trình chất lượng cao và cả đoàn ballet thiếu nhi «Shchelkunchik». Dù chỉ ngắm mặt tiền hay thưởng thức một buổi diễn, nhà hát đều là điểm nhấn không thể bỏ qua ở trung tâm Yekaterinburg.",
    [
        "Khánh thành 1912 bằng vở opera «Cuộc đời vì Sa hoàng» của Glinka.",
        "Kiến trúc tân-baroque, biệt danh «Bạch Thiên Nga»; do K. Babykin hiện thực hoá.",
        "Nơi khởi nghiệp của Lemeshev, Kozlovsky; nay là «Ural Opera Ballet» hàng đầu ngoài hai thủ đô.",
    ],
    {
        "hours_vi": "Theo lịch biểu diễn (thường buổi tối và một số suất chiều cuối tuần); phòng vé mở ban ngày.",
        "ticket_vi": "Mua vé theo chương trình; nhiều mức giá.",
        "duration_vi": "Ngắm mặt tiền ~15 phút; xem một buổi diễn khoảng 2–3 giờ.",
        "best_time_vi": "Mùa biểu diễn (thu – xuân); mùa hè có thể ít suất hơn.",
        "tips_vi": "Đặt vé sớm cho các vở nổi tiếng; kết hợp dạo trục phố Lenin và quảng trường lân cận.",
    },
    [
        {"title": "Wikipedia (RU) — Екатеринбургский театр оперы и балета", "url": "https://ru.wikipedia.org/wiki/Екатеринбургский_театр_оперы_и_балета"},
        {"title": "Наш Урал — Екатеринбургский театр оперы и балета (GPS)", "url": "https://nashural.ru/dostoprimechatelnosti-urala/sverdlovskaya-oblast/ekaterinburgskij-teatr-opery-i-baleta/"},
    ],
    ["theatre", "opera", "ballet", "architecture", "white-swan", "yekaterinburg"],
    maps_text("Екатеринбургский театр оперы и балета", "Екатеринбург", "Yekaterinburg Opera and Ballet Theatre", "Yekaterinburg", 56.838953, 60.616702),
    official_site="https://uralopera.ru/",
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
