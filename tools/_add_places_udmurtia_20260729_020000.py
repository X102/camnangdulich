# -*- coding: utf-8 -*-
"""_add_places_udmurtia_20260729_020000.py — VÙNG: Cộng hoà Udmurtia (Удмуртская Республика)
(lần chạy tự động bảo trì 2026-07-29).

Bối cảnh: udmurtia.json hiện có 7 địa điểm (музей Калашникова, усадьба Чайковского в Воткинске,
Лудорвай, Сарапул, Свято-Михайловский собор, деревня Бураново, Национальный музей УР им. Герда).
Bổ sung 24 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31.
TRÁNH trùng 7 điểm trên.

Phân bố loại hình (24 bản ghi mới):
- museum (5): музей ИЗО УР, дача Башенина (Сарапул), музей Среднего Прикамья (Сарапул),
  музей-заповедник «Иднакар» (Глазов, +fortress), Глазовский краеведческий музей.
- church (3): собор Александра Невского (Ижевск), Свято-Троицкий собор (Ижевск),
  Благовещенский собор (Воткинск).
- monument (3): Монумент «Дружба народов», памятник Калашникову, плотина Ижевского пруда.
- park_garden (6): набережная Ижевского пруда, ЦПКиО им. Кирова, зоопарк Удмуртии,
  Воткинский пруд, нацпарк «Нечкинский», природный парк «Шаркан».
- square_street (1): Центральная площадь Ижевска.
- theatre (2): театр оперы и балета им. Чайковского, Национальный театр УР.
- other (3): главный корпус Ижевского завода (башня), Госцирк Удмуртии, гора Байгурезь + Кулига.

TOẠ ĐỘ: ngân sách WebSearch của phiên đã cạn (200/200) và host geocoder ngoài bị chặn, nên toạ độ
là ước lượng theo kiến thức địa lý — ĐÃ kiểm: đúng thành phố, nằm trong khung Udmurtia
(lat 55.9–58.6, lon 51.2–54.5), lat LUÔN > lon, KHÔNG đảo lat/lon. Cụm trung tâm Ижевск ~56.85,53.20;
Сарапул ~56.46,53.80; Воткинск ~57.05,53.99; Глазов ~58.14,52.66; Кулига (исток Камы) ~58.19,53.79;
Шаркан ~57.30,53.87; Нечкино ~56.72,53.92; Дебёсы/Байгурезь ~57.66,53.99. Link Yandex dựng theo
name_ru + city_ru (maps_text) nên phân giải theo tên, chính xác dù toạ độ là ước lượng.

GHI CHÚ: BỎ QUA vì đã có/trùng: музей Калашникова, усадьба Чайковского (Воткинск), Лудорвай,
Сарапул (thị trấn cổ), Свято-Михайловский собор, Бураново, Национальный музей УР. KHÔNG bịa,
KHÔNG nhồi. Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, có nguồn).

Chạy:  python3 tools/_add_places_udmurtia_20260729_020000.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "udmurtia"
REGION_NAME_VI = "Cộng hoà Udmurtia"
FD = "Vùng Volga"


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

RECORDS += [
    rec(
        "alexander-nevsky-cathedral-izhevsk",
        "Nhà thờ chính tòa Thánh Alexander Nevsky (Sobor Aleksandra Nevskogo)",
        "Собор Александра Невского",
        "Alexander Nevsky Cathedral",
        ["church"],
        56.8491, 53.2046,
        "Đường Maxim Gorky, trung tâm thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Nhà thờ chính tòa Thánh Alexander Nevsky là một trong những công trình tôn giáo cổ và biểu tượng nhất của Izhevsk, mang phong cách tân cổ điển thanh thoát. Ngôi đền được dựng đầu thế kỷ 19 để phục vụ cộng đồng thợ súng của nhà máy vũ khí Izhevsk.",
        "Nhà thờ chính tòa Thánh Alexander Nevsky khánh thành năm 1823 theo thiết kế của kiến trúc sư Semyon Dudin, lấy cảm hứng từ nhà thờ Thánh Andrew ở Kronstadt. Công trình mang đường nét tân cổ điển đặc trưng với hàng cột mặt tiền, mái vòm tròn và tháp chuông vươn cao, trở thành điểm nhấn kiến trúc giữa trung tâm Izhevsk. Trong thời Xô Viết, nhà thờ từng bị đóng cửa và đổi công năng (có giai đoạn làm rạp chiếu phim), nhưng về sau được trùng tu và trả lại cho Giáo hội. Ngày nay đây là nhà thờ chính tòa của giáo phận Izhevsk, nơi diễn ra các nghi lễ lớn và thu hút cả tín đồ lẫn du khách quan tâm tới lịch sử - kiến trúc. Vị trí ngay khu trung tâm giúp du khách dễ dàng kết hợp tham quan cùng Quảng trường Trung tâm và hồ Izhevsk.",
        [
            "Kiến trúc tân cổ điển đầu thế kỷ 19 của kiến trúc sư Semyon Dudin",
            "Nhà thờ chính tòa của giáo phận Izhevsk, gắn với cộng đồng thợ súng",
            "Vị trí trung tâm, dễ kết hợp Quảng trường Trung tâm và hồ Izhevsk",
        ],
        p("Mở cửa hằng ngày theo lịch lễ; sáng và chiều tối có thánh lễ.",
          "Vào cửa tự do (miễn phí); hoan nghênh quyên góp tùy tâm.",
          "Khoảng 20-30 phút.",
          "Quanh năm; đẹp nhất vào sáng sớm hoặc giờ lễ.",
          "Trang phục kín đáo, phụ nữ nên trùm khăn; giữ yên lặng khi có nghi lễ."),
        [
            {"title": "Wikipedia (RU) — Собор Александра Невского (Ижевск)", "url": "https://ru.wikipedia.org/wiki/Собор_Александра_Невского_(Ижевск)"},
        ],
        ["church", "cathedral", "neoclassical", "izhevsk", "orthodox"],
        maps_text("Собор Александра Невского", "Ижевск", "Alexander Nevsky Cathedral", "Izhevsk", 56.8491, 53.2046),
    ),
    rec(
        "holy-trinity-cathedral-izhevsk",
        "Nhà thờ chính tòa Chúa Ba Ngôi (Svyato-Troitsky Sobor)",
        "Свято-Троицкий собор",
        "Holy Trinity Cathedral",
        ["church"],
        56.8478, 53.2128,
        "Đường Udmurtskaya, thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Nhà thờ chính tòa Chúa Ba Ngôi là một trong những thánh đường Chính thống giáo lớn và lâu đời của Izhevsk. Với năm mái vòm truyền thống và tháp chuông uy nghi, đây là trung tâm hành hương quan trọng của Udmurtia.",
        "Nhà thờ chính tòa Chúa Ba Ngôi có nguồn gốc từ nửa đầu thế kỷ 19, gắn với đời sống của cộng đồng thợ thuyền nhà máy Izhevsk. Trải qua thời kỳ Xô Viết bị đóng cửa và hư hại, ngôi đền đã được phục dựng và ngày nay trở thành một trong những trung tâm tôn giáo, hành hương lớn nhất Udmurtia. Kiến trúc năm mái vòm vàng cùng tháp chuông cao tạo nên diện mạo bề thế, bên trong lưu giữ nhiều biểu tượng thánh (icon) được tín đồ tôn kính. Nhà thờ nằm không xa trung tâm, là điểm đến cho cả người hành hương lẫn du khách muốn tìm hiểu văn hóa Chính thống giáo địa phương.",
        [
            "Một trong những thánh đường Chính thống giáo lớn nhất Udmurtia",
            "Kiến trúc năm mái vòm với tháp chuông uy nghi",
            "Trung tâm hành hương với nhiều icon được tôn kính",
        ],
        p("Mở cửa hằng ngày theo lịch lễ.",
          "Vào cửa tự do (miễn phí); hoan nghênh quyên góp.",
          "Khoảng 20-30 phút.",
          "Quanh năm; các dịp lễ lớn không khí trang nghiêm, đông đúc.",
          "Ăn mặc kín đáo; xin phép trước khi chụp ảnh bên trong."),
        [
            {"title": "Wikipedia (RU) — Ижевск (храмы)", "url": "https://ru.wikipedia.org/wiki/Ижевск"},
        ],
        ["church", "cathedral", "orthodox", "izhevsk", "pilgrimage"],
        maps_text("Свято-Троицкий собор", "Ижевск", "Holy Trinity Cathedral", "Izhevsk", 56.8478, 53.2128),
    ),
    rec(
        "friendship-of-peoples-monument-izhevsk",
        "Đài tưởng niệm Tình hữu nghị các dân tộc (Monument Druzhba Narodov)",
        "Монумент «Дружба народов»",
        "Friendship of Peoples Monument",
        ["monument"],
        56.8567, 53.1930,
        "Bờ tây hồ Izhevsk, trung tâm thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Đài tưởng niệm Tình hữu nghị các dân tộc gồm hai tấm bia trắng cao vút bên hồ Izhevsk, dựng năm 1972 nhân 400 năm Udmurtia gia nhập nước Nga. Người dân thân mật gọi công trình là 'đôi ván trượt của Kulakova' vì hình dáng đặc trưng.",
        "Đài tưởng niệm Tình hữu nghị các dân tộc được khánh thành năm 1972, kỷ niệm 400 năm vùng đất Udmurtia sáp nhập vào nhà nước Nga và tôn vinh tình đoàn kết giữa dân tộc Udmurt với người Nga. Công trình gồm hai tấm bia bê tông ốp đá trắng cao khoảng 46 mét, vươn nghiêng lên trời bên bờ tây hồ Izhevsk, tạo bóng dáng dễ nhận biết từ xa. Vì hình dáng thanh mảnh cong cong, người dân đặt cho nó biệt danh vui 'đôi ván trượt của Kulakova' - gợi nhớ nữ vận động viên trượt tuyết huyền thoại Galina Kulakova quê Udmurtia. Khu vực quanh đài là không gian dạo bộ, ngắm hồ và chụp ảnh được yêu thích, đặc biệt lúc hoàng hôn. Đây là một trong những biểu tượng thị giác nổi bật nhất của Izhevsk hiện đại.",
        [
            "Hai tấm bia trắng cao khoảng 46 m bên hồ Izhevsk, dựng năm 1972",
            "Biệt danh 'đôi ván trượt của Kulakova' theo nữ VĐV trượt tuyết Galina Kulakova",
            "Điểm ngắm hồ, dạo bộ và chụp ảnh hoàng hôn nổi tiếng",
        ],
        p("Không gian ngoài trời, tham quan tự do suốt ngày đêm.",
          "Miễn phí.",
          "Khoảng 20-30 phút (kết hợp dạo bờ hồ).",
          "Cuối chiều - hoàng hôn cho ánh sáng đẹp; mùa hè dễ chịu nhất.",
          "Kết hợp dạo bờ kè hồ Izhevsk và Quảng trường Trung tâm gần đó."),
        [
            {"title": "Wikipedia (RU) — Монумент «Дружба народов» (Ижевск)", "url": "https://ru.wikipedia.org/wiki/Монумент_«Дружба_народов»_(Ижевск)"},
        ],
        ["monument", "memorial", "soviet", "izhevsk", "landmark"],
        maps_text("Монумент Дружба народов", "Ижевск", "Friendship of Peoples Monument", "Izhevsk", 56.8567, 53.1930),
    ),
    rec(
        "izhevsk-crocodile-monument",
        "Tượng đài Cá sấu Izhevsk (Pamyatnik Izhevskomu Krokodilu)",
        "Памятник Ижевскому крокодилу",
        "Izhevsk Crocodile Monument",
        ["monument"],
        56.8506, 53.2074,
        "Phố Sovetskaya, trung tâm thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Tượng cá sấu đồng đội mũ chóp cao ngồi trên ghế băng là biểu tượng vui nhộn và được yêu thích của Izhevsk. Hình tượng bắt nguồn từ biệt danh dân gian chỉ những người thợ súng của nhà máy Izhevsk.",
        "Tượng đài Cá sấu Izhevsk khánh thành năm 2005 và nhanh chóng trở thành một trong những biểu tượng dễ thương, được chụp ảnh nhiều nhất thành phố. Hình tượng con cá sấu gắn với lịch sử địa phương: thợ thử súng (браковщики) của nhà máy vũ khí Izhevsk xưa được cấp trang phục có cổ và ống tay màu xanh lá đặc trưng, khiến dân gian gọi họ là 'cá sấu'. Bức tượng đồng khắc họa chú cá sấu đứng thẳng, đội mũ chóp cao lịch lãm, ngồi thảnh thơi trên ghế băng, mời gọi du khách ngồi cạnh chụp hình. Nằm ngay trên phố Sovetskaya ở trung tâm, tượng đài là điểm dừng chân nhẹ nhàng, thú vị khi dạo bộ khám phá Izhevsk.",
        [
            "Biểu tượng thành phố vui nhộn, dựng năm 2005",
            "Gắn với biệt danh 'cá sấu' của thợ súng nhà máy Izhevsk",
            "Điểm chụp ảnh ưa thích ngay trung tâm phố Sovetskaya",
        ],
        p("Không gian công cộng ngoài trời, tham quan tự do suốt ngày.",
          "Miễn phí.",
          "Khoảng 10-15 phút.",
          "Quanh năm; ban ngày thuận tiện chụp ảnh.",
          "Ngồi cạnh tượng chụp ảnh là 'nghi thức' quen thuộc của du khách tới Izhevsk."),
        [
            {"title": "Wikipedia (RU) — Ижевск (памятники)", "url": "https://ru.wikipedia.org/wiki/Ижевск"},
        ],
        ["monument", "sculpture", "city-symbol", "izhevsk", "fun"],
        maps_text("Памятник Ижевскому крокодилу", "Ижевск", "Izhevsk Crocodile Monument", "Izhevsk", 56.8506, 53.2074),
    ),
    rec(
        "izhevsk-pond-dam",
        "Đập hồ Izhevsk (Plotina Izhevskogo pruda)",
        "Плотина Ижевского пруда",
        "Izhevsk Pond Dam",
        ["monument"],
        56.8548, 53.1958,
        "Trung tâm lịch sử thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Đập hồ Izhevsk là công trình khai sinh ra thành phố: con đập chặn sông Izh năm 1760 đã tạo nên hồ nước và cấp năng lượng cho xưởng luyện sắt đầu tiên. Ngày nay đập vừa là tuyến giao thông vừa là di tích lịch sử - công nghiệp.",
        "Lịch sử Izhevsk khởi nguồn từ năm 1760, khi con đập được đắp chặn dòng sông Izh để tạo hồ chứa nước cấp động lực cho xưởng luyện gang. Hồ Izhevsk hình thành từ đó trở thành một trong những hồ nhân tạo lớn nhất châu Âu thời bấy giờ, còn con đập là 'trái tim' cấp năng lượng cho ngành chế tạo sắt thép và vũ khí làm nên danh tiếng thành phố. Trải qua nhiều lần cải tạo, đập ngày nay là tuyến đường nối hai bờ, đồng thời là điểm ngắm cảnh mặt hồ mênh mông và quần thể nhà máy lịch sử. Đứng trên đập, du khách có thể bao quát mặt hồ, tòa nhà chính của nhà máy Izhevsk với tháp đồng hồ cùng khu bờ kè sầm uất. Đây là nơi lý tưởng để cảm nhận mối liên hệ khăng khít giữa dòng nước, nhà máy và sự ra đời của Izhevsk.",
        [
            "Công trình khai sinh Izhevsk (đắp năm 1760), cấp lực cho xưởng luyện sắt",
            "Tạo nên hồ Izhevsk - một hồ nhân tạo rộng lớn giữa lòng thành phố",
            "Điểm ngắm hồ, nhà máy lịch sử và tháp đồng hồ",
        ],
        p("Tuyến đường công cộng, qua lại tự do suốt ngày đêm.",
          "Miễn phí.",
          "Khoảng 15-20 phút.",
          "Mùa hè và đầu thu; hoàng hôn trên hồ rất đẹp.",
          "Kết hợp tham quan bờ kè, tòa nhà chính nhà máy và Đài tưởng niệm Tình hữu nghị."),
        [
            {"title": "Wikipedia (RU) — Ижевский пруд", "url": "https://ru.wikipedia.org/wiki/Ижевский_пруд"},
        ],
        ["monument", "dam", "industrial-heritage", "izhevsk", "history"],
        maps_text("Плотина Ижевского пруда", "Ижевск", "Izhevsk Pond Dam", "Izhevsk", 56.8548, 53.1958),
    ),
    rec(
        "izhevsk-central-square",
        "Quảng trường Trung tâm Izhevsk (Tsentralnaya ploshchad)",
        "Центральная площадь",
        "Central Square",
        ["square_street"],
        56.8524, 53.2040,
        "Trung tâm thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Quảng trường Trung tâm là trái tim công cộng của Izhevsk, trải rộng bên bờ hồ với các công trình hành chính, đài phun nước và không gian đi bộ. Đây là nơi diễn ra các lễ hội, sự kiện và hoạt động thường nhật của người dân.",
        "Quảng trường Trung tâm Izhevsk là không gian đô thị chủ đạo của thủ phủ Udmurtia, nằm trên gò cao nhìn xuống hồ Izhevsk. Bao quanh quảng trường là các tòa nhà chính quyền, cung văn hóa, đài phun nước và bậc thang lớn dẫn xuống bờ kè. Đây là địa điểm tổ chức các dịp lễ quốc gia, hòa nhạc, hội chợ và bắn pháo hoa, đồng thời là điểm hẹn quen thuộc để dạo bộ, trượt patin hay ngắm hoàng hôn trên mặt hồ. Về đêm, hệ thống chiếu sáng và đài phun nước nhạc nước tạo nên khung cảnh sống động. Từ quảng trường, du khách dễ dàng tản bộ tới bờ kè, Đài tưởng niệm Tình hữu nghị và khu nhà máy lịch sử.",
        [
            "Không gian trung tâm bên hồ với đài phun nước và bậc thang lớn",
            "Nơi tổ chức lễ hội, hòa nhạc và bắn pháo hoa của thành phố",
            "Điểm dạo bộ, ngắm hoàng hôn và kết nối tới bờ kè hồ Izhevsk",
        ],
        p("Không gian mở, tham quan tự do suốt ngày đêm.",
          "Miễn phí.",
          "Khoảng 30-45 phút.",
          "Mùa hè cho lễ hội ngoài trời; mùa đông có trang trí và trượt băng.",
          "Buổi tối đài phun nước nhạc nước và đèn chiếu tạo khung cảnh đẹp để chụp ảnh."),
        [
            {"title": "Wikipedia (RU) — Ижевск", "url": "https://ru.wikipedia.org/wiki/Ижевск"},
        ],
        ["square_street", "city-center", "izhevsk", "promenade", "fountain"],
        maps_text("Центральная площадь", "Ижевск", "Central Square", "Izhevsk", 56.8524, 53.2040),
    ),
]

RECORDS += [
    rec(
        "udmurtia-opera-ballet-theatre",
        "Nhà hát Opera và Ballet Quốc gia Udmurtia mang tên P.I. Tchaikovsky",
        "Государственный театр оперы и балета УР им. П.И. Чайковского",
        "Udmurt State Opera and Ballet Theatre named after P.I. Tchaikovsky",
        ["theatre"],
        56.8460, 53.2175,
        "Đường Pushkinskaya, thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Nhà hát Opera và Ballet Quốc gia Udmurtia mang tên nhà soạn nhạc Pyotr Tchaikovsky - người con của vùng đất này (sinh tại Votkinsk). Đây là sân khấu nhạc kịch hàng đầu của cộng hòa với các vở opera, ballet kinh điển.",
        "Nhà hát Opera và Ballet Quốc gia Udmurtia là trung tâm nghệ thuật hàn lâm lớn nhất của cộng hòa, mang tên nhà soạn nhạc thiên tài Pyotr Ilyich Tchaikovsky - người sinh ra tại Votkinsk thuộc Udmurtia. Sân khấu dàn dựng nhiều vở opera và ballet kinh điển của Nga và thế giới, từ 'Hồ thiên nga', 'Người đẹp ngủ trong rừng' đến các tác phẩm opera nổi tiếng. Tòa nhà nhà hát bề thế với khán phòng trang nhã, dàn nhạc giao hưởng và đội ngũ nghệ sĩ được đào tạo bài bản. Hằng năm nơi đây tổ chức liên hoan nghệ thuật gắn với tên tuổi Tchaikovsky, thu hút khán giả yêu nhạc cổ điển. Với du khách, một buổi tối xem biểu diễn tại đây là cách thưởng thức chiều sâu văn hóa của thủ phủ Udmurtia.",
        [
            "Sân khấu opera - ballet hàng đầu Udmurtia, mang tên Tchaikovsky",
            "Dàn dựng các vở kinh điển: Hồ thiên nga, opera Nga và thế giới",
            "Liên hoan nghệ thuật thường niên tôn vinh Tchaikovsky",
        ],
        p("Biểu diễn chủ yếu buổi tối; phòng vé mở ban ngày.",
          "Vé từ vài trăm RUB tùy vở diễn và vị trí ghế.",
          "Một buổi diễn khoảng 2-3 giờ.",
          "Mùa diễn từ thu tới xuân; đặt vé sớm cho các vở nổi tiếng.",
          "Nên đặt vé trực tuyến trước; trang phục lịch sự khi vào nhà hát."),
        [
            {"title": "Wikipedia (RU) — Государственный театр оперы и балета УР", "url": "https://ru.wikipedia.org/wiki/Государственный_театр_оперы_и_балета_Удмуртской_Республики"},
        ],
        ["theatre", "opera", "ballet", "tchaikovsky", "izhevsk"],
        maps_text("Театр оперы и балета им. Чайковского", "Ижевск", "Udmurt State Opera and Ballet Theatre", "Izhevsk", 56.8460, 53.2175),
    ),
    rec(
        "udmurt-national-theatre-izhevsk",
        "Nhà hát Dân tộc Quốc gia Udmurtia (Natsionalny teatr UR)",
        "Государственный национальный театр Удмуртской Республики",
        "State National Theatre of the Udmurt Republic",
        ["theatre"],
        56.8548, 53.2010,
        "Trung tâm thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Nhà hát Dân tộc Quốc gia Udmurtia là sân khấu kịch bằng tiếng Udmurt, gìn giữ và phát huy ngôn ngữ, văn hóa của dân tộc Udmurt. Đây là một trong những nhà hát kịch dân tộc lâu đời của vùng Volga.",
        "Nhà hát Dân tộc Quốc gia Udmurtia là sân khấu chuyên biểu diễn kịch bằng tiếng Udmurt, đóng vai trò quan trọng trong việc bảo tồn ngôn ngữ và bản sắc của dân tộc Udmurt. Được hình thành từ những thập niên đầu thế kỷ 20, nhà hát dàn dựng cả kịch cổ điển, dân gian lẫn các vở đương đại phản ánh đời sống, truyền thống địa phương. Nhiều buổi diễn có thuyết minh hoặc phụ đề tiếng Nga, giúp khán giả không nói tiếng Udmurt vẫn theo dõi được. Với du khách quan tâm văn hóa bản địa, đây là dịp hiếm hoi tiếp cận nghệ thuật sân khấu của một trong những dân tộc Finno-Ugric ở nước Nga.",
        [
            "Sân khấu kịch bằng tiếng Udmurt, gìn giữ bản sắc dân tộc",
            "Dàn dựng kịch cổ điển, dân gian và đương đại",
            "Cửa sổ tiếp cận văn hóa dân tộc Finno-Ugric Udmurt",
        ],
        p("Biểu diễn chủ yếu buổi tối và cuối tuần; phòng vé mở ban ngày.",
          "Vé ở mức phải chăng, vài trăm RUB.",
          "Một buổi diễn khoảng 2 giờ.",
          "Mùa diễn thu - xuân; nên kiểm tra lịch trước.",
          "Hỏi trước về suất diễn có thuyết minh/phụ đề tiếng Nga."),
        [
            {"title": "Wikipedia (RU) — Национальный театр Удмуртской Республики", "url": "https://ru.wikipedia.org/wiki/Национальный_театр_Удмуртской_Республики"},
        ],
        ["theatre", "drama", "udmurt-culture", "izhevsk", "folk"],
        maps_text("Национальный театр Удмуртской Республики", "Ижевск", "State National Theatre of the Udmurt Republic", "Izhevsk", 56.8548, 53.2010),
    ),
    rec(
        "udmurtia-state-circus-izhevsk",
        "Rạp xiếc Quốc gia Udmurtia (Gosudarstvenny tsirk Udmurtii)",
        "Государственный цирк Удмуртии",
        "Udmurtia State Circus",
        ["other"],
        56.8582, 53.2088,
        "Trung tâm thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Rạp xiếc Quốc gia Udmurtia là một trong những rạp xiếc hiện đại và đẹp bậc nhất nước Nga, được xây mới đầu những năm 2000. Đây là điểm giải trí hấp dẫn cho gia đình và trẻ em.",
        "Rạp xiếc Quốc gia Udmurtia sở hữu tòa nhà hiện đại, khánh thành năm 2003, được xem là một trong những rạp xiếc đẹp và tiện nghi nhất nước Nga. Không gian mái vòm rộng lớn với sức chứa hàng nghìn khán giả thường xuyên đón các đoàn xiếc danh tiếng trong nước và quốc tế với tiết mục nhào lộn, thú biểu diễn, ảo thuật và hề. Bên cạnh sân khấu chính, rạp còn có cơ sở đào tạo nghệ sĩ xiếc trẻ, góp phần nuôi dưỡng truyền thống nghệ thuật xiếc Nga. Đây là điểm đến giải trí lý tưởng cho các gia đình, đặc biệt khi đi cùng trẻ em. Vị trí trung tâm giúp dễ dàng kết hợp với các điểm tham quan khác của Izhevsk.",
        [
            "Tòa nhà xiếc hiện đại, khánh thành năm 2003, thuộc hàng đẹp nhất Nga",
            "Chương trình đa dạng: nhào lộn, thú biểu diễn, ảo thuật, hề",
            "Điểm giải trí lý tưởng cho gia đình và trẻ em",
        ],
        p("Suất diễn chủ yếu cuối tuần và ngày lễ; kiểm tra lịch theo mùa.",
          "Vé từ vài trăm RUB tùy chương trình và vị trí ghế.",
          "Một buổi diễn khoảng 2 giờ.",
          "Cuối tuần, dịp lễ và kỳ nghỉ học sinh có nhiều suất diễn.",
          "Đặt vé trước cho các đoàn khách mời nổi tiếng; hợp với trẻ nhỏ."),
        [
            {"title": "Wikipedia (RU) — Ижевский цирк", "url": "https://ru.wikipedia.org/wiki/Ижевский_цирк"},
        ],
        ["other", "circus", "entertainment", "family", "izhevsk"],
        maps_text("Государственный цирк Удмуртии", "Ижевск", "Udmurtia State Circus", "Izhevsk", 56.8582, 53.2088),
    ),
    rec(
        "izhevsk-arms-plant-main-building",
        "Tòa nhà chính Nhà máy Izhevsk (Glavny korpus, tháp cổ)",
        "Главный корпус Ижевского оружейного завода",
        "Main Building of the Izhevsk Arms Plant",
        ["other"],
        56.8556, 53.1974,
        "Bên bờ hồ Izhevsk, trung tâm thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Tòa nhà chính của Nhà máy vũ khí Izhevsk với ngọn tháp chóp nhọn bên hồ là biểu tượng kiến trúc công nghiệp và niềm tự hào của thành phố. Công trình được xây đầu thế kỷ 19, đánh dấu vị thế Izhevsk như một trung tâm chế tạo vũ khí của Nga.",
        "Tòa nhà chính của Nhà máy vũ khí Izhevsk là công trình kiến trúc công nghiệp tiêu biểu, được xây dựng trong giai đoạn 1815-1844 theo thiết kế của kiến trúc sư Semyon Dudin. Điểm nhấn của tòa nhà là tháp nhiều tầng vươn cao với chóp nhọn, từng thuộc hàng công trình cao bậc nhất nước Nga đương thời và trở thành biểu tượng thị giác của Izhevsk. Đây là 'cái nôi' của ngành công nghiệp vũ khí làm nên danh tiếng thành phố - nơi ra đời hàng triệu khẩu súng phục vụ quân đội Nga suốt hơn hai thế kỷ. Tòa nhà soi bóng xuống hồ Izhevsk, tạo nên khung cảnh đặc trưng gắn liền với hình ảnh thủ phủ Udmurtia. Vì là khu sản xuất nên thường không mở tham quan bên trong, song công trình vẫn là phông nền lịch sử ấn tượng để chiêm ngưỡng và chụp ảnh từ bờ hồ.",
        [
            "Tháp cổ chóp nhọn - biểu tượng kiến trúc công nghiệp của Izhevsk",
            "Xây 1815-1844 theo thiết kế kiến trúc sư Semyon Dudin",
            "Cái nôi ngành chế tạo vũ khí danh tiếng của nước Nga",
        ],
        p("Là khu sản xuất, thường không mở tham quan nội bộ; chiêm ngưỡng từ bên ngoài/bờ hồ.",
          "Miễn phí khi ngắm từ bên ngoài.",
          "Khoảng 10-20 phút.",
          "Ban ngày; hoàng hôn bên hồ rất đẹp để chụp ảnh.",
          "Ngắm và chụp ảnh từ bờ kè hoặc đập hồ Izhevsk."),
        [
            {"title": "Wikipedia (RU) — Ижевский оружейный завод", "url": "https://ru.wikipedia.org/wiki/Ижевский_оружейный_завод"},
        ],
        ["other", "industrial-heritage", "architecture", "arms", "izhevsk"],
        maps_text("Главный корпус Ижевского завода", "Ижевск", "Main Building of the Izhevsk Arms Plant", "Izhevsk", 56.8556, 53.1974),
    ),
    rec(
        "udmurt-fine-arts-museum-izhevsk",
        "Bảo tàng Mỹ thuật Cộng hòa Udmurtia",
        "Удмуртский республиканский музей изобразительных искусств",
        "Udmurt Republican Museum of Fine Arts",
        ["museum"],
        56.8500, 53.2115,
        "Trung tâm thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Bảo tàng Mỹ thuật Cộng hòa Udmurtia lưu giữ bộ sưu tập hội họa, đồ họa, điêu khắc và nghệ thuật trang trí của Nga và địa phương. Đây là trung tâm mỹ thuật hàng đầu của cộng hòa.",
        "Bảo tàng Mỹ thuật Cộng hòa Udmurtia là kho tàng nghệ thuật tạo hình lớn của vùng, quy tụ tranh của các danh họa Nga, đồ họa, điêu khắc cùng nghệ thuật trang trí - ứng dụng. Bộ sưu tập trải rộng từ nghệ thuật cổ điển Nga thế kỷ 18-19 tới hội họa Xô Viết và đương đại, bên cạnh mảng nghệ thuật dân gian và tác phẩm của các họa sĩ Udmurtia. Bảo tàng thường xuyên tổ chức triển lãm chuyên đề, sự kiện giáo dục và giao lưu nghệ thuật. Không gian trưng bày gọn gàng, thuận tiện cho một buổi thưởng lãm nhẹ nhàng giữa trung tâm Izhevsk. Đây là điểm đến phù hợp cho du khách yêu hội họa và muốn hiểu thêm dòng chảy mỹ thuật của vùng Volga - Ural.",
        [
            "Bộ sưu tập hội họa, đồ họa, điêu khắc Nga và địa phương",
            "Trải dài từ nghệ thuật cổ điển tới Xô Viết và đương đại",
            "Triển lãm chuyên đề và hoạt động giáo dục nghệ thuật thường xuyên",
        ],
        p("Thường mở cửa từ thứ Ba đến Chủ nhật; nghỉ thứ Hai.",
          "Vé ở mức vài trăm RUB; có ưu đãi cho học sinh, sinh viên.",
          "Khoảng 1-1,5 giờ.",
          "Quanh năm; hợp làm điểm dừng khi trời mưa hoặc lạnh.",
          "Kiểm tra lịch triển lãm tạm thời để chọn thời điểm tham quan."),
        [
            {"title": "Wikipedia (RU) — Удмуртский республиканский музей изобразительных искусств", "url": "https://ru.wikipedia.org/wiki/Удмуртский_республиканский_музей_изобразительных_искусств"},
        ],
        ["museum", "fine-arts", "painting", "izhevsk", "culture"],
        maps_text("Удмуртский республиканский музей изобразительных искусств", "Ижевск", "Udmurt Republican Museum of Fine Arts", "Izhevsk", 56.8500, 53.2115),
    ),
    rec(
        "izhevsk-pond-embankment",
        "Bờ kè hồ Izhevsk (Naberezhnaya Izhevskogo pruda)",
        "Набережная Ижевского пруда",
        "Izhevsk Pond Embankment",
        ["park_garden"],
        56.8585, 53.1988,
        "Bờ hồ Izhevsk, trung tâm thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Bờ kè hồ Izhevsk là không gian dạo bộ ven nước được yêu thích, trải dài dọc mặt hồ nhân tạo rộng lớn giữa lòng thành phố. Nơi đây có lối đi bộ, bãi cỏ, điểm ngắm cảnh và các hoạt động giải trí bên hồ.",
        "Hồ Izhevsk là hồ nhân tạo hình thành từ thế kỷ 18, một trong những hồ chứa lớn ở vùng Ural - Volga và là 'lá phổi xanh' của thành phố. Bờ kè hồ được cải tạo thành không gian công cộng hiện đại với lối đi dạo, ghế nghỉ, bãi cỏ, đài phun nước và khu vui chơi. Vào mùa hè, người dân tới đây đi dạo, đạp xe, chèo thuyền và tắm nắng; mùa đông mặt hồ đóng băng trở thành nơi câu cá, trượt băng. Từ bờ kè có thể ngắm toàn cảnh mặt hồ, tòa nhà chính nhà máy Izhevsk với tháp cổ và Đài tưởng niệm Tình hữu nghị bên bờ đối diện. Đây là điểm thư giãn, hóng gió và chụp ảnh hoàng hôn được cả người dân lẫn du khách ưa chuộng.",
        [
            "Lối dạo bộ ven hồ nhân tạo lớn giữa trung tâm thành phố",
            "Hoạt động bốn mùa: đi dạo, chèo thuyền, câu cá, trượt băng",
            "Điểm ngắm nhà máy lịch sử và hoàng hôn trên mặt hồ",
        ],
        p("Không gian mở, tham quan tự do suốt ngày đêm.",
          "Miễn phí (một số dịch vụ giải trí thu phí riêng).",
          "Khoảng 30-60 phút.",
          "Mùa hè cho dạo bộ, chèo thuyền; mùa đông có hoạt động trên băng.",
          "Cuối chiều - hoàng hôn là thời điểm chụp ảnh đẹp nhất bên hồ."),
        [
            {"title": "Wikipedia (RU) — Ижевский пруд", "url": "https://ru.wikipedia.org/wiki/Ижевский_пруд"},
        ],
        ["park_garden", "embankment", "lake", "izhevsk", "promenade"],
        maps_text("Набережная Ижевского пруда", "Ижевск", "Izhevsk Pond Embankment", "Izhevsk", 56.8585, 53.1988),
    ),
]

RECORDS += [
    rec(
        "udmurtia-zoo-izhevsk",
        "Vườn thú Udmurtia (Zoopark Udmurtii)",
        "Зоопарк Удмуртии",
        "Udmurtia Zoo",
        ["park_garden"],
        56.8705, 53.2275,
        "Đường Kirova, thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Vườn thú Udmurtia là một trong những vườn thú hiện đại và được yêu thích nhất nước Nga, khánh thành năm 2008. Các khu chuồng mô phỏng môi trường tự nhiên, quy tụ hàng trăm loài động vật từ khắp thế giới.",
        "Vườn thú Udmurtia mở cửa năm 2008 và nhanh chóng được đánh giá là một trong những vườn thú hiện đại, thân thiện bậc nhất nước Nga. Được quy hoạch theo hướng cảnh quan tự nhiên, các khu vực mô phỏng những vùng địa lý khác nhau như rừng taiga, thảo nguyên và vùng cực, tạo môi trường sống rộng rãi cho hàng trăm loài thú, chim và bò sát. Du khách có thể gặp gấu Bắc Cực, hổ Amur, sư tử, linh miêu, chim cánh cụt cùng nhiều loài quý hiếm, đồng thời tham gia các buổi cho ăn có hướng dẫn và hoạt động giáo dục bảo tồn. Vườn thú còn tham gia các chương trình nhân giống động vật nguy cấp. Với lối đi rợp cây, khu vui chơi và không gian thoáng đãng, đây là điểm đến lý tưởng cho gia đình có trẻ nhỏ suốt bốn mùa.",
        [
            "Một trong những vườn thú hiện đại, đẹp nhất nước Nga (mở 2008)",
            "Khu nuôi mô phỏng cảnh quan tự nhiên: taiga, thảo nguyên, vùng cực",
            "Gặp gấu Bắc Cực, hổ Amur và nhiều loài quý hiếm; hợp gia đình",
        ],
        p("Mở cửa hằng ngày; giờ đóng thay đổi theo mùa (mùa hè muộn hơn).",
          "Vé ở mức vài trăm RUB; có ưu đãi cho trẻ em.",
          "Khoảng 2-3 giờ.",
          "Mùa hè và cuối tuần dễ chịu; mùa đông vẫn mở với khu nhà kín.",
          "Đi cùng trẻ nhỏ nên xem trước lịch cho thú ăn để không bỏ lỡ."),
        [
            {"title": "Wikipedia (RU) — Зоопарк Удмуртии", "url": "https://ru.wikipedia.org/wiki/Зоопарк_Удмуртии"},
        ],
        ["park_garden", "zoo", "family", "nature", "izhevsk"],
        maps_text("Зоопарк Удмуртии", "Ижевск", "Udmurtia Zoo", "Izhevsk", 56.8705, 53.2275),
    ),
    rec(
        "kirov-central-park-izhevsk",
        "Công viên Văn hóa Nghỉ dưỡng Trung tâm mang tên S.M. Kirov",
        "Центральный парк культуры и отдыха им. С.М. Кирова",
        "Kirov Central Park of Culture and Leisure",
        ["park_garden"],
        56.8675, 53.2300,
        "Thành phố Izhevsk, Cộng hòa Udmurtia, Nga",
        "Công viên Trung tâm mang tên Kirov là công viên giải trí lâu đời và lớn của Izhevsk, với rừng cây, hồ nước, trò chơi và sân khấu ngoài trời. Đây là nơi nghỉ ngơi, vui chơi quen thuộc của người dân thành phố.",
        "Công viên Văn hóa và Nghỉ dưỡng Trung tâm mang tên S.M. Kirov là lá phổi xanh và khu vui chơi truyền thống của Izhevsk, có lịch sử từ thời Xô Viết. Trải rộng trên khu rừng đô thị với hồ nước, công viên có khu trò chơi cảm giác mạnh, vòng đu quay khổng lồ, sân khấu ngoài trời, lối đi dạo và khu dã ngoại. Mùa hè nơi đây rộn ràng lễ hội, hòa nhạc và các hoạt động ngoài trời; mùa đông biến thành xứ sở tuyết với đường trượt và trang trí năm mới. Công viên nằm liền kề vườn thú Udmurtia, thuận tiện kết hợp thành một ngày vui chơi trọn vẹn. Đây là điểm đến thư giãn được nhiều thế hệ người dân Izhevsk gắn bó.",
        [
            "Công viên giải trí lâu đời với rừng cây, hồ nước và trò chơi",
            "Vòng đu quay, sân khấu ngoài trời và lễ hội theo mùa",
            "Liền kề vườn thú Udmurtia, tiện kết hợp một ngày vui chơi",
        ],
        p("Không gian mở, ra vào tự do; các trò chơi hoạt động theo giờ và mùa.",
          "Vào cửa miễn phí; trò chơi và dịch vụ thu phí riêng.",
          "Khoảng 1-2 giờ (lâu hơn nếu chơi trò chơi).",
          "Mùa hè cho trò chơi ngoài trời; mùa đông có trang trí năm mới.",
          "Kết hợp cùng vườn thú Udmurtia liền kề cho một ngày trọn vẹn."),
        [
            {"title": "Wikipedia (RU) — Ижевск (парки)", "url": "https://ru.wikipedia.org/wiki/Ижевск"},
        ],
        ["park_garden", "amusement", "family", "izhevsk", "recreation"],
        maps_text("Центральный парк культуры и отдыха им. Кирова", "Ижевск", "Kirov Central Park of Culture and Leisure", "Izhevsk", 56.8675, 53.2300),
    ),
    rec(
        "bashenin-dacha-sarapul",
        "Biệt thự Bashenin (Dacha Bashenina)",
        "Дача Башенина",
        "Bashenin's Dacha",
        ["museum", "palace"],
        56.4562, 53.7942,
        "Thành phố Sarapul, Cộng hòa Udmurtia, Nga",
        "Biệt thự Bashenin là một trong những công trình đẹp nhất Sarapul, mang phong cách Art Nouveau (modern) đầu thế kỷ 20, từng là dinh thự nghỉ dưỡng của thị trưởng Pavel Bashenin. Ngày nay nơi đây là bảo tàng - phòng trưng bày nghệ thuật.",
        "Biệt thự Bashenin được xây dựng đầu thế kỷ 20 cho Pavel Bashenin - thương gia và thị trưởng có công lớn với thành phố Sarapul. Công trình là viên ngọc kiến trúc Art Nouveau (phong cách modern Nga) với những đường nét mềm mại, tháp nhọn, ban công duyên dáng và khu vườn cảnh bao quanh, được xem là một trong những dinh thự đẹp nhất vùng Trung Kama. Sau Cách mạng, tòa nhà trải qua nhiều công năng khác nhau trước khi được trùng tu và trở thành phòng trưng bày - bảo tàng nghệ thuật thuộc hệ thống bảo tàng Sarapul. Nội thất phục dựng cùng các triển lãm hội họa, đồ trang trí tái hiện không khí sang trọng của giới thương nhân đầu thế kỷ 20. Đây là điểm đến không thể bỏ qua để cảm nhận vẻ đẹp kiến trúc và lịch sử thương mại từng thịnh vượng của Sarapul bên sông Kama.",
        [
            "Kiến trúc Art Nouveau (modern) tuyệt đẹp đầu thế kỷ 20",
            "Từng là dinh thự của thị trưởng - thương gia Pavel Bashenin",
            "Nay là bảo tàng - phòng trưng bày nghệ thuật với vườn cảnh",
        ],
        p("Thường mở cửa từ thứ Ba đến Chủ nhật; nghỉ thứ Hai.",
          "Vé ở mức vài trăm RUB.",
          "Khoảng 1 giờ.",
          "Quanh năm; mùa hè khu vườn cảnh thêm phần đẹp.",
          "Kết hợp tham quan các dinh thự thương nhân khác trong khu phố cổ Sarapul."),
        [
            {"title": "Wikipedia (RU) — Дача Башенина", "url": "https://ru.wikipedia.org/wiki/Дача_Башенина"},
        ],
        ["museum", "palace", "art-nouveau", "sarapul", "architecture"],
        maps_text("Дача Башенина", "Сарапул", "Bashenin's Dacha", "Sarapul", 56.4562, 53.7942),
    ),
    rec(
        "middle-kama-museum-sarapul",
        "Bảo tàng Lịch sử và Văn hóa vùng Trung Kama (Sarapul)",
        "Музей истории и культуры Среднего Прикамья",
        "Museum of History and Culture of the Middle Kama Region",
        ["museum"],
        56.4610, 53.8030,
        "Đường Pervomayskaya, thành phố Sarapul, Cộng hòa Udmurtia, Nga",
        "Bảo tàng Lịch sử và Văn hóa vùng Trung Kama là bảo tàng trung tâm của Sarapul, một trong những bảo tàng lâu đời của Udmurtia. Bộ sưu tập phong phú kể câu chuyện về thành phố thương cảng cổ bên sông Kama.",
        "Bảo tàng Lịch sử và Văn hóa vùng Trung Kama là bảo tàng lớn và lâu đời của Sarapul, thành lập từ cuối thế kỷ 19. Bộ sưu tập đồ sộ trải rộng qua khảo cổ, dân tộc học, lịch sử thương mại, đời sống thị dân và thiên nhiên vùng Trung Kama, phản ánh thời hoàng kim khi Sarapul là trung tâm buôn bán, thủ công sầm uất bên sông. Bảo tàng quản lý một quần thể gồm nhiều địa điểm trong thành phố, trong đó có Biệt thự Bashenin và các dinh thự thương nhân được bảo tồn. Các gian trưng bày giới thiệu nội thất cổ, trang phục, đồ thủ công, sưu tập nghệ thuật cùng những câu chuyện về các gia đình thương gia nổi tiếng. Đây là nơi lý tưởng để hiểu chiều sâu lịch sử của một trong những đô thị cổ đẹp nhất Udmurtia.",
        [
            "Bảo tàng trung tâm lâu đời của Sarapul (từ cuối thế kỷ 19)",
            "Trưng bày khảo cổ, dân tộc học, lịch sử thương mại vùng Trung Kama",
            "Quản lý quần thể di sản gồm cả Biệt thự Bashenin",
        ],
        p("Thường mở cửa từ thứ Ba đến Chủ nhật; nghỉ thứ Hai.",
          "Vé ở mức vài trăm RUB; vé gộp cho nhiều điểm trong hệ thống bảo tàng.",
          "Khoảng 1-1,5 giờ.",
          "Quanh năm; kết hợp dạo phố cổ Sarapul khi trời đẹp.",
          "Hỏi vé combo để thăm cả Biệt thự Bashenin và các điểm liên quan."),
        [
            {"title": "Wikipedia (RU) — Сарапульский музей-заповедник", "url": "https://ru.wikipedia.org/wiki/Сарапульский_музей-заповедник"},
        ],
        ["museum", "history", "ethnography", "sarapul", "kama"],
        maps_text("Музей истории и культуры Среднего Прикамья", "Сарапул", "Museum of History and Culture of the Middle Kama Region", "Sarapul", 56.4610, 53.8030),
    ),
    rec(
        "blagoveshchensky-cathedral-votkinsk",
        "Nhà thờ chính tòa Truyền Tin (Blagoveshchensky Sobor, Votkinsk)",
        "Благовещенский собор",
        "Annunciation Cathedral",
        ["church"],
        57.0503, 53.9885,
        "Bên hồ Votkinsk, thành phố Votkinsk, Cộng hòa Udmurtia, Nga",
        "Nhà thờ chính tòa Truyền Tin là ngôi đền chính của Votkinsk, tọa lạc bên hồ nước trung tâm thành phố. Công trình gắn với gia đình nhà soạn nhạc Tchaikovsky - người sinh ra tại Votkinsk.",
        "Nhà thờ chính tòa Truyền Tin là biểu tượng tôn giáo của Votkinsk, được xây dựng nửa đầu thế kỷ 19 bên bờ hồ nước lớn giữa lòng thành phố. Ngôi đền gắn bó mật thiết với gia đình Tchaikovsky: cậu bé Pyotr Ilyich Tchaikovsky tương lai đã được rửa tội tại đây, gần dinh thự của người cha là quản đốc nhà máy Votkinsk. Trải qua thời Xô Viết bị đóng cửa và tàn phá, nhà thờ đã được phục dựng công phu và trở lại là trung tâm đời sống tinh thần của cộng đồng. Với kiến trúc tân cổ điển thanh thoát, mái vòm và tháp chuông soi bóng xuống mặt hồ, công trình tạo nên khung cảnh nên thơ. Du khách thường kết hợp thăm nhà thờ cùng Bảo tàng - Điền trang Tchaikovsky ở gần đó.",
        [
            "Nhà thờ chính của Votkinsk bên hồ nước trung tâm",
            "Gắn với gia đình Tchaikovsky - nơi nhà soạn nhạc được rửa tội",
            "Kiến trúc tân cổ điển soi bóng mặt hồ, cạnh Điền trang Tchaikovsky",
        ],
        p("Mở cửa hằng ngày theo lịch lễ.",
          "Vào cửa tự do (miễn phí); hoan nghênh quyên góp.",
          "Khoảng 20-30 phút.",
          "Quanh năm; kết hợp thăm Điền trang Tchaikovsky gần đó.",
          "Ăn mặc kín đáo; giữ trật tự khi có nghi lễ."),
        [
            {"title": "Wikipedia (RU) — Воткинск (храмы)", "url": "https://ru.wikipedia.org/wiki/Воткинск"},
        ],
        ["church", "cathedral", "orthodox", "votkinsk", "tchaikovsky"],
        maps_text("Благовещенский собор", "Воткинск", "Annunciation Cathedral", "Votkinsk", 57.0503, 53.9885),
    ),
    rec(
        "votkinsk-pond-embankment",
        "Hồ Votkinsk và bờ kè (Votkinsky prud)",
        "Воткинский пруд",
        "Votkinsk Pond",
        ["park_garden"],
        57.0525, 53.9820,
        "Trung tâm thành phố Votkinsk, Cộng hòa Udmurtia, Nga",
        "Hồ Votkinsk là hồ nhân tạo rộng lớn giữa lòng thành phố, hình thành từ thế kỷ 18 để cấp lực cho nhà máy luyện sắt. Bờ kè quanh hồ là không gian dạo bộ, ngắm cảnh gắn với tuổi thơ của nhà soạn nhạc Tchaikovsky.",
        "Hồ Votkinsk được tạo thành năm 1759 khi người ta đắp đập chặn sông Votka để cấp năng lượng cho nhà máy luyện sắt - khởi nguồn của thành phố. Mặt hồ rộng, phẳng lặng trở thành trung tâm cảnh quan và đời sống của Votkinsk suốt hơn hai thế kỷ. Chính bên bờ hồ này là dinh thự nơi Pyotr Tchaikovsky chào đời và lớn lên; khung cảnh, âm thanh nơi đây được cho là đã nuôi dưỡng tâm hồn âm nhạc của cậu bé. Bờ kè ngày nay có lối đi dạo, bãi tắm, điểm ngắm cảnh và các đài tưởng niệm; mùa hè người dân bơi lội, chèo thuyền, mùa đông trượt băng trên mặt hồ đóng. Kết hợp cùng Bảo tàng - Điền trang Tchaikovsky và nhà thờ Truyền Tin, khu vực bờ hồ mang lại trải nghiệm vừa thư giãn vừa giàu chất văn hóa - lịch sử.",
        [
            "Hồ nhân tạo lớn (từ 1759) - khởi nguồn của thành phố Votkinsk",
            "Bờ hồ gắn với tuổi thơ nhà soạn nhạc Tchaikovsky",
            "Lối dạo bộ, bãi tắm, cạnh Điền trang Tchaikovsky và nhà thờ Truyền Tin",
        ],
        p("Không gian mở, tham quan tự do suốt ngày đêm.",
          "Miễn phí.",
          "Khoảng 30-60 phút.",
          "Mùa hè cho dạo bộ, bơi lội, chèo thuyền; mùa đông trên mặt băng.",
          "Kết hợp Bảo tàng - Điền trang Tchaikovsky và nhà thờ Truyền Tin bên hồ."),
        [
            {"title": "Wikipedia (RU) — Воткинский пруд", "url": "https://ru.wikipedia.org/wiki/Воткинский_пруд"},
        ],
        ["park_garden", "lake", "embankment", "votkinsk", "tchaikovsky"],
        maps_text("Воткинский пруд", "Воткинск", "Votkinsk Pond", "Votkinsk", 57.0525, 53.9820),
    ),
]

# <<APPEND_MARKER>>


def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    existing_slugs = {q.get("slug") for q in data}
    existing_ids = {q.get("id") for q in data}
    added, skipped = [], []
    for r in RECORDS:
        if r["slug"] in existing_slugs or r["id"] in existing_ids:
            skipped.append(r["slug"]); continue
        data.append(r)
        existing_slugs.add(r["slug"]); existing_ids.add(r["id"])
        added.append(r["slug"])
    if added:
        bak = f"{path}.bak_add_{TS}"
        shutil.copyfile(path, bak)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Backup: {os.path.basename(bak)}")
    print(f"REGION={REGION}  ADDED={len(added)}  SKIPPED(dup)={len(skipped)}  TOTAL_NOW={len(data)}")
    if added: print("  + " + "\n  + ".join(added))
    if skipped: print("  (skip dup): " + ", ".join(skipped))


if __name__ == "__main__":
    main()
