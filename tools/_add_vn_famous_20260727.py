# -*- coding: utf-8 -*-
"""
_add_vn_famous_20260727.py — Bổ sung địa điểm DU LỊCH VIỆT NAM nổi tiếng còn thiếu.
Lô này: 8 tỉnh/thành MỚI (sau sáp nhập 1/7/2025): Cao Bằng, Điện Biên, Sơn La,
Thanh Hóa, Nghệ An, Hải Phòng, Cà Mau, Đồng Tháp.
Chèn AN TOÀN: tạo mới hoặc nạp–append–ghi; bỏ qua slug đã có; sao lưu trước khi ghi.
Link bản đồ sinh theo ĐÚNG quy ước retrofit_map_links.py (Yandex theo tên RU + ll; Google theo tên EN + vùng + nước).
"""
import json, os, glob, re, urllib.parse, datetime, shutil
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TODAY = "2026-07-27"


def _clean_name(name):
    """Bỏ phần phiên âm trong ngoặc và phần bổ nghĩa sau dấu phẩy để truy vấn bản đồ khớp POI."""
    name = re.sub(r"\s*\(.*?\)\s*", " ", name or "")
    name = name.split(" (")[0]
    return re.sub(r"\s+", " ", name).strip()


def maps_for(rec, region_slug):
    """Sinh link bản đồ TRỎ THẲNG tới thẻ địa điểm (đọc được bình luận/thông tin),
    canh giữa theo toạ độ THẬT để không mở lệch xa.
    - Google: deep link tìm theo TÊN (name_en) + tỉnh + nước -> mở đúng thẻ địa điểm.
    - Yandex: với VN dùng tên Latinh/địa phương (tên Nga hầu như không khớp POI Việt Nam),
              tìm theo tên + canh giữa ll + zoom cao -> mở thẻ địa điểm, không rơi lệch."""
    lat = rec["coordinates"]["lat"]
    lon = rec["coordinates"]["lon"]
    is_vn = (rec.get("country") == "vietnam") or region_slug.startswith("vn-")
    country_en = "Vietnam" if is_vn else "Russia"
    base = region_slug[3:] if region_slug.startswith("vn-") else region_slug
    reg_en = base.replace("-", " ").title()
    name_en = _clean_name(rec.get("name_en"))
    name_vi = _clean_name(rec.get("name_vi"))
    name_ru = _clean_name(rec.get("name_ru"))

    g_name = name_en or name_vi or name_ru
    gparts = [g_name] + ([reg_en] if reg_en.lower() not in g_name.lower() else []) + [country_en]
    google = "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(", ".join(gparts))

    y_name = (name_en or name_vi) if is_vn else (name_ru or name_en or name_vi)
    yparts = [y_name] + ([reg_en] if reg_en.lower() not in y_name.lower() else []) + [country_en]
    ytext = urllib.parse.quote(", ".join(yparts))
    yandex = f"https://yandex.com/maps/?text={ytext}&ll={lon},{lat}&z=17"

    return {"yandex": yandex, "google": google}


PLACES = []

# ===================== CAO BẰNG (Miền Bắc) =====================
PLACES += [
  {
    "id": "vn-cao-bang-ban-gioc",
    "slug": "ban-gioc",
    "region": "vn-cao-bang",
    "country": "vietnam",
    "region_name_vi": "Cao Bằng",
    "federal_district": "Miền Bắc",
    "name_vi": "Thác Bản Giốc (Ban Zốc)",
    "name_ru": "Водопад Банзёк",
    "name_en": "Ban Gioc Waterfall",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 22.8536, "lon": 106.7225},
    "address_vi": "Xã Đàm Thủy, huyện Trùng Khánh, tỉnh Cao Bằng (biên giới Việt – Trung)",
    "rating": {"value": 4.7, "count": 9800, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách choáng ngợp trước dòng thác nhiều tầng hùng vĩ vắt ngang biên giới, nước tung bọt trắng xóa giữa khung cảnh núi non xanh mướt. Nhiều người khuyên đi bè tre để tới gần chân thác và đến vào mùa nước đổ; một số lưu ý đường xa và nên kết hợp thăm động Ngườm Ngao gần đó.",
    "presentation_short_vi": "Thác Bản Giốc ở tỉnh Cao Bằng là thác nước tự nhiên lớn nhất Đông Nam Á và là một trong những thác biên giới đẹp nhất thế giới. Dòng thác nhiều tầng đổ xuống từ độ cao khoảng 30 m, tung bọt trắng giữa khung cảnh núi đá vôi và ruộng lúa, tạo nên bức tranh sơn thủy hữu tình nơi địa đầu Tổ quốc.",
    "presentation_short_en": "Ban Gioc Waterfall in Cao Bang province is the largest natural waterfall in Southeast Asia and one of the finest transnational falls in the world. Its tiered curtains of water tumble some 30 metres amid limestone peaks and rice paddies, painting an idyllic landscape on Vietnam's far northern frontier.",
    "presentation_short_ru": "Водопад Банзёк в провинции Каобанг — крупнейший естественный водопад Юго-Восточной Азии и один из красивейших пограничных водопадов мира. Многоступенчатые потоки падают с высоты около 30 метров среди известняковых гор и рисовых полей, создавая идиллический пейзаж на дальнем севере Вьетнама.",
    "presentation_long_vi": "Nằm trên dòng sông Quây Sơn ở xã Đàm Thủy, huyện Trùng Khánh, cách thành phố Cao Bằng khoảng 90 km, Thác Bản Giốc là biểu tượng thiên nhiên của vùng non nước Cao Bằng và là thác nước tự nhiên lớn nhất Đông Nam Á. Thác nằm ngay trên đường biên giới Việt Nam – Trung Quốc, gồm thác chính và thác phụ, đổ xuống thành nhiều tầng từ độ cao chừng 30 m, rộng hàng trăm mét. Vào mùa mưa (khoảng tháng 6 đến tháng 9) nước dâng cuồn cuộn, ầm ào tung bọt trắng xóa; mùa thu nước trong xanh, êm dịu, hai bên là ruộng lúa và rặng núi đá vôi soi bóng. Du khách thường ngồi bè tre trôi ra gần chân thác để cảm nhận hơi nước mát lạnh và chụp ảnh cận cảnh những dải nước bạc. Gần thác có chùa Phật Tích Trúc Lâm Bản Giốc trên sườn núi, nơi phóng tầm mắt bao quát toàn cảnh. Bản Giốc nằm trong vùng Công viên địa chất toàn cầu UNESCO Non nước Cao Bằng, thường được kết hợp tham quan cùng động Ngườm Ngao chỉ cách vài cây số. Khung cảnh vừa hùng vĩ vừa nên thơ khiến nơi đây được xem là một trong những thác nước đẹp nhất Việt Nam.",
    "presentation_long_en": "Set on the Quay Son River in Dam Thuy commune, Trung Khanh district, about 90 km from Cao Bang city, Ban Gioc is the natural emblem of the Cao Bang uplands and the largest natural waterfall in Southeast Asia. It lies directly on the Vietnam–China border and is made up of a main fall and a secondary fall, cascading in several tiers from a height of roughly 30 metres across a front hundreds of metres wide. During the rainy season (about June to September) the water surges and thunders in clouds of white spray; in autumn it turns clear and gentle, framed by rice paddies and limestone peaks mirrored in the pools. Visitors typically drift out on bamboo rafts to the foot of the falls, feeling the cool mist and photographing the silver ribbons of water up close. On a nearby hillside stands the Truc Lam Ban Gioc pagoda, which offers a sweeping panorama of the whole scene. Ban Gioc lies within the UNESCO Non Nuoc Cao Bang Global Geopark and is usually combined with a visit to Nguom Ngao Cave, only a few kilometres away. At once majestic and poetic, it is widely regarded as one of the most beautiful waterfalls in Vietnam.",
    "presentation_long_ru": "Расположенный на реке Куэйшон в общине Дамтхюи уезда Чунгкхань, примерно в 90 км от города Каобанг, водопад Банзёк — природный символ горного края Каобанг и крупнейший естественный водопад Юго-Восточной Азии. Он находится прямо на границе Вьетнама и Китая и состоит из главного и второстепенного каскадов, падающих несколькими ступенями с высоты около 30 метров на фронте в сотни метров. В сезон дождей (примерно с июня по сентябрь) вода бурлит и грохочет облаками белых брызг; осенью она становится прозрачной и спокойной, обрамлённой рисовыми полями и известняковыми вершинами, отражающимися в заводях. Туристы обычно выплывают на бамбуковых плотах к подножию водопада, ощущая прохладную водяную пыль и фотографируя вблизи серебристые ленты воды. На соседнем склоне стоит пагода Чуклам-Банзёк, откуда открывается широкая панорама всей картины. Банзёк входит в глобальный геопарк ЮНЕСКО «Нонныок-Каобанг» и обычно осматривается вместе с пещерой Нгыомнгао, до которой всего несколько километров. Одновременно величественный и поэтичный, он по праву считается одним из красивейших водопадов Вьетнама.",
    "highlights_vi": [
      "Thác nước tự nhiên lớn nhất Đông Nam Á, nằm trên biên giới Việt – Trung",
      "Nằm trong Công viên địa chất toàn cầu UNESCO Non nước Cao Bằng",
      "Đi bè tre ra sát chân thác; đẹp nhất mùa nước đổ (tháng 6–9) và mùa lúa chín"
    ],
    "highlights_en": [
      "The largest natural waterfall in Southeast Asia, straddling the Vietnam–China border",
      "Part of the UNESCO Non Nuoc Cao Bang Global Geopark",
      "Bamboo-raft rides to the foot of the falls; best in the high-water season (Jun–Sep) and at harvest time"
    ],
    "highlights_ru": [
      "Крупнейший естественный водопад Юго-Восточной Азии на границе Вьетнама и Китая",
      "Входит в глобальный геопарк ЮНЕСКО «Нонныок-Каобанг»",
      "Прогулки на бамбуковых плотах к подножию; лучше всего в полноводный сезон (июнь–сентябрь) и в пору урожая"
    ],
    "practical": {
      "hours_vi": "Khu du lịch mở khoảng 6:00–18:00 hằng ngày.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 45.000 VND/người; đi bè tre tính phí riêng.",
      "duration_vi": "Khoảng 2–3 giờ (nửa ngày nếu kết hợp Ngườm Ngao).",
      "best_time_vi": "Tháng 6–9 nước nhiều; tháng 9–10 nước trong và có lúa chín vàng.",
      "tips_vi": "Mang giày chống trượt, áo mưa mỏng vì hơi nước; kết hợp thăm động Ngườm Ngao và chùa Trúc Lâm Bản Giốc; nhớ mang giấy tờ tùy thân vì đây là khu vực biên giới."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Thác Bản Giốc", "url": "https://vi.wikipedia.org/wiki/Th%C3%A1c_B%E1%BA%A3n_Gi%E1%BB%91c"},
      {"title": "UNESCO Global Geopark — Non Nuoc Cao Bang", "url": "https://www.unesco.org/en/iggp/non-nuoc-cao-bang"}
    ],
    "tags": ["nature", "waterfall", "geopark", "viewpoint", "outdoor", "top", "border"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-cao-bang-nguom-ngao",
    "slug": "nguom-ngao",
    "region": "vn-cao-bang",
    "country": "vietnam",
    "region_name_vi": "Cao Bằng",
    "federal_district": "Miền Bắc",
    "name_vi": "Động Ngườm Ngao",
    "name_ru": "Пещера Нгыомнгао",
    "name_en": "Nguom Ngao Cave",
    "categories": ["other", "park_garden"],
    "coordinates": {"lat": 22.8453, "lon": 106.7061},
    "address_vi": "Bản Gun, xã Đàm Thủy, huyện Trùng Khánh, tỉnh Cao Bằng",
    "rating": {"value": 4.6, "count": 3200, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách trầm trồ trước hệ thạch nhũ khổng lồ muôn hình vạn trạng và không khí mát lạnh trong lòng núi. Nhiều người thấy động ít đông, lối đi được lắp đèn và lan can khá an toàn; một số nhắc nền đá trơn nên đi giày bám tốt.",
    "presentation_short_vi": "Động Ngườm Ngao ở huyện Trùng Khánh, tỉnh Cao Bằng là một hang động đá vôi kỳ vĩ dài khoảng 2 km, được người Tày phát hiện từ hơn một thế kỷ trước. Trong lòng động là rừng thạch nhũ và măng đá lộng lẫy, được ánh đèn tôn lên thành muôn hình kỳ ảo.",
    "presentation_short_en": "Nguom Ngao Cave in Trung Khanh district, Cao Bang province, is a spectacular limestone cave about 2 km long, discovered by local Tay people over a century ago. Inside lies a glittering forest of stalactites and stalagmites, sculpted by nature and lit into countless fantastical shapes.",
    "presentation_short_ru": "Пещера Нгыомнгао в уезде Чунгкхань провинции Каобанг — впечатляющая известняковая пещера длиной около 2 км, обнаруженная местными тай более века назад. Внутри — сверкающий лес сталактитов и сталагмитов, подсвеченный так, что он превращается в бесчисленные фантастические образы.",
    "presentation_long_vi": "Cách Thác Bản Giốc chỉ khoảng 3 km, Động Ngườm Ngao nằm trong lòng dãy núi đá vôi ở bản Gun, xã Đàm Thủy. Trong tiếng Tày, 'Ngườm Ngao' nghĩa là 'hang hổ', gắn với truyền thuyết xưa từng có hổ dữ trú ngụ. Hang được hình thành cách đây hàng trăm triệu năm do quá trình phong hóa đá vôi, tổng chiều dài khoảng 2 km với ba cửa chính. Đường tham quan đã lắp hệ thống đèn và lối đi lát đá dài chừng 1 km, đưa du khách len qua những vòm hang cao rộng, nơi thạch nhũ và măng đá buông rủ tạo thành vô số hình thù: thửa ruộng bậc thang, cây tơ hồng, búp sen, con người và muông thú. Nổi tiếng nhất là khối nhũ hình 'cây tơ hồng' và 'đài sen úp ngược' mọc từ dưới lên. Không khí trong hang mát lạnh quanh năm, tương phản với cái nắng bên ngoài. Ngườm Ngao cũng nằm trong tuyến tham quan của Công viên địa chất toàn cầu UNESCO Non nước Cao Bằng và gần như luôn được ghép cùng Bản Giốc trong một hành trình. Vẻ đẹp nguyên sơ, kỳ ảo và còn khá vắng khách khiến động trở thành điểm đến hấp dẫn cho những ai ưa khám phá thiên nhiên.",
    "presentation_long_en": "Just about 3 km from Ban Gioc Waterfall, Nguom Ngao Cave burrows into a limestone range at Gun hamlet in Dam Thuy commune. In the Tay language 'Nguom Ngao' means 'tiger cave', recalling a legend that fierce tigers once lived here. Formed hundreds of millions of years ago by the weathering of limestone, the cave runs about 2 km with three main entrances. A lit walkway of roughly 1 km leads visitors through soaring chambers where stalactites and stalagmites hang and rise into countless shapes: terraced fields, a lotus bud, a 'love vine', human figures and animals. The most celebrated formation is the upside-down lotus dais growing from the floor. The air inside stays cool all year, a welcome contrast to the heat outside. Nguom Ngao is part of the UNESCO Non Nuoc Cao Bang Global Geopark and is almost always paired with Ban Gioc on the same itinerary. Its pristine, otherworldly beauty and still-modest crowds make it a rewarding stop for anyone who loves exploring nature underground.",
    "presentation_long_ru": "Всего в 3 км от водопада Банзёк пещера Нгыомнгао уходит в известняковый массив у деревни Гун в общине Дамтхюи. На языке тай «Нгыомнгао» означает «тигриная пещера» — по легенде, здесь когда-то жили свирепые тигры. Образованная сотни миллионов лет назад в результате выветривания известняка, пещера тянется примерно на 2 км и имеет три главных входа. Освещённая дорожка длиной около 1 км ведёт гостей сквозь высокие залы, где сталактиты и сталагмиты складываются в бесчисленные формы: террасные поля, бутон лотоса, «лиану любви», человеческие фигуры и животных. Самое знаменитое образование — перевёрнутый лотосовый пьедестал, растущий от пола вверх. Воздух внутри круглый год прохладный — приятный контраст с жарой снаружи. Нгыомнгао входит в глобальный геопарк ЮНЕСКО «Нонныок-Каобанг» и почти всегда осматривается вместе с Банзёк в одном маршруте. Первозданная, потусторонняя красота и пока ещё небольшое число туристов делают пещеру желанной остановкой для всех, кто любит исследовать подземную природу. Прохладный микроклимат сохраняется здесь круглый год, а благоустроенная подсвеченная тропа делает прогулку удобной; благодаря близости к водопаду Банзёк обе достопримечательности легко осмотреть за один день.",
    "highlights_vi": [
      "Hang đá vôi dài ~2 km với rừng thạch nhũ, măng đá muôn hình",
      "Tên Tày nghĩa là 'hang hổ'; nằm trong Geopark UNESCO Non nước Cao Bằng",
      "Cách Thác Bản Giốc ~3 km, lý tưởng để ghép chung một hành trình"
    ],
    "highlights_en": [
      "A ~2 km limestone cave with a forest of stalactites and stalagmites",
      "Its Tay name means 'tiger cave'; part of the UNESCO Cao Bang Geopark",
      "Only ~3 km from Ban Gioc Waterfall — ideal to combine in one trip"
    ],
    "highlights_ru": [
      "Известняковая пещера длиной ~2 км с лесом сталактитов и сталагмитов",
      "Название на языке тай означает «тигриная пещера»; часть геопарка ЮНЕСКО",
      "Всего в ~3 км от водопада Банзёк — удобно объединить в один маршрут"
    ],
    "practical": {
      "hours_vi": "Khoảng 8:00–17:00 hằng ngày.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 45.000 VND/người.",
      "duration_vi": "Khoảng 1–1,5 giờ.",
      "best_time_vi": "Quanh năm; thuận tiện nhất khi kết hợp cùng Bản Giốc vào mùa khô.",
      "tips_vi": "Đi giày bám tốt vì nền đá ẩm trơn; mang theo áo khoác mỏng vì trong hang mát; nên thuê hướng dẫn để hiểu các khối nhũ."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (EN) — Nguom Ngao Cave", "url": "https://en.wikipedia.org/wiki/Ng%C6%B0%E1%BB%9Dm_Ngao_Cave"},
      {"title": "UNESCO Global Geopark — Non Nuoc Cao Bang", "url": "https://www.unesco.org/en/iggp/non-nuoc-cao-bang"}
    ],
    "tags": ["cave", "nature", "geopark", "indoor", "outdoor", "daytrip"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-cao-bang-pac-bo",
    "slug": "pac-bo",
    "region": "vn-cao-bang",
    "country": "vietnam",
    "region_name_vi": "Cao Bằng",
    "federal_district": "Miền Bắc",
    "name_vi": "Khu di tích Quốc gia đặc biệt Pác Bó",
    "name_ru": "Особый национальный историко-мемориальный комплекс Пакбо",
    "name_en": "Pac Bo Special National Relic Site",
    "categories": ["monument", "park_garden"],
    "coordinates": {"lat": 22.9903, "lon": 106.1783},
    "address_vi": "Xã Trường Hà, huyện Hà Quảng, tỉnh Cao Bằng",
    "rating": {"value": 4.6, "count": 2600, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách xúc động khi đến nơi Chủ tịch Hồ Chí Minh sống và làm việc sau ngày về nước, giữa khung cảnh suối Lê-nin xanh ngọc và núi Các Mác. Nhiều người khen không gian trong lành, thiêng liêng; một số lưu ý phải đi bộ khá xa từ bãi xe vào hang.",
    "presentation_short_vi": "Khu di tích Pác Bó ở xã Trường Hà, huyện Hà Quảng, tỉnh Cao Bằng là nơi Chủ tịch Hồ Chí Minh trở về nước năm 1941 sau 30 năm bôn ba, trực tiếp lãnh đạo cách mạng Việt Nam. Giữa cảnh suối Lê-nin trong xanh và hang Cốc Bó, nơi đây trở thành 'cội nguồn' thiêng liêng của cách mạng.",
    "presentation_short_en": "The Pac Bo relic site in Truong Ha commune, Ha Quang district, Cao Bang province, is where President Ho Chi Minh returned to Vietnam in 1941 after 30 years abroad to lead the revolution directly. With the jade-green Lenin Stream and Coc Bo Cave, it is revered as a sacred cradle of the Vietnamese revolution.",
    "presentation_short_ru": "Мемориал Пакбо в общине Чыонгха уезда Хакуанг провинции Каобанг — место, куда в 1941 году после 30 лет за границей вернулся президент Хо Ши Мин, чтобы непосредственно возглавить революцию. С нефритово-зелёным ручьём Ленина и пещерой Кокбо он почитается как священная колыбель вьетнамской революции.",
    "presentation_long_vi": "Nằm sát biên giới phía bắc, cách thành phố Cao Bằng khoảng 50 km, Pác Bó (tiếng Nùng nghĩa là 'đầu nguồn') là một trong những địa chỉ đỏ quan trọng bậc nhất của lịch sử Việt Nam hiện đại. Ngày 28/1/1941, sau 30 năm hoạt động ở nước ngoài, lãnh tụ Nguyễn Ái Quốc – Hồ Chí Minh đã vượt qua cột mốc 108 để trở về Tổ quốc, chọn hang Cốc Bó làm nơi ở và làm việc trong những ngày đầu chuẩn bị cho cách mạng. Tại đây, Người đã dịch 'Lịch sử Đảng Cộng sản Liên Xô', soạn thảo nhiều tài liệu quan trọng và trực tiếp chỉ đạo phong trào. Chính Người đã đặt tên dòng suối trong vắt trước hang là suối Lê-nin và ngọn núi sừng sững phía sau là núi Các Mác, gửi gắm lý tưởng cách mạng. Du khách ngày nay đi dọc con đường ven suối màu xanh ngọc bích, ghé thăm hang Cốc Bó nhỏ bé đơn sơ, chiếc bàn đá 'chông chênh dịch sử Đảng', cùng nhà tưởng niệm và đền thờ Bác Hồ trang nghiêm. Khung cảnh núi rừng nguyên sơ, tĩnh lặng hòa cùng chiều sâu lịch sử khiến Pác Bó vừa là điểm về nguồn giàu cảm xúc, vừa là nơi thư thái giữa thiên nhiên vùng biên viễn.",
    "presentation_long_en": "Close to the northern border and about 50 km from Cao Bang city, Pac Bo (meaning 'water source' in the Nung language) is one of the most important 'red addresses' in modern Vietnamese history. On 28 January 1941, after 30 years abroad, the leader Nguyen Ai Quoc – Ho Chi Minh crossed border marker 108 to return home and chose Coc Bo Cave as his home and workplace in the first days of preparing the revolution. Here he translated a history of the Soviet Communist Party, drafted key documents and directed the movement in person. It was he who named the crystal-clear stream before the cave the Lenin Stream and the towering peak behind it Karl Marx Mountain, investing the landscape with revolutionary ideals. Today visitors walk along the jade-green stream, step into the small, spartan Coc Bo Cave, see the rough stone table where he 'translated Party history', and pay respects at the memorial house and temple dedicated to Ho Chi Minh. The pristine, hushed mountain setting, layered with historical meaning, makes Pac Bo both a moving pilgrimage and a peaceful retreat in Vietnam's frontier nature.",
    "presentation_long_ru": "Расположенный у северной границы, примерно в 50 км от города Каобанг, Пакбо (на языке нунг — «исток воды») — один из важнейших «красных адресов» современной истории Вьетнама. 28 января 1941 года, после 30 лет за рубежом, вождь Нгуен Ай Куок — Хо Ши Мин пересёк пограничный столб № 108 и вернулся на родину, избрав пещеру Кокбо своим жилищем и рабочим местом в первые дни подготовки революции. Здесь он перевёл историю Коммунистической партии СССР, составил ряд ключевых документов и лично руководил движением. Именно он назвал кристально чистый ручей перед пещерой ручьём Ленина, а возвышающуюся позади вершину — горой Карла Маркса, наделив пейзаж революционным смыслом. Сегодня посетители идут вдоль нефритово-зелёного ручья, заходят в маленькую аскетичную пещеру Кокбо, видят грубый каменный стол, за которым он «переводил историю партии», и отдают дань уважения в мемориальном доме и храме Хо Ши Мина. Первозданная, тихая горная обстановка, наполненная историческим смыслом, делает Пакбо одновременно волнующим паломничеством и умиротворяющим уголком в приграничной природе Вьетнама.",
    "highlights_vi": [
      "Nơi Chủ tịch Hồ Chí Minh về nước (1941) và trực tiếp lãnh đạo cách mạng",
      "Hang Cốc Bó, suối Lê-nin, núi Các Mác và bàn đá 'dịch sử Đảng'",
      "Di tích Quốc gia đặc biệt, điểm 'về nguồn' bên cột mốc biên giới 108"
    ],
    "highlights_en": [
      "Where Ho Chi Minh returned to Vietnam (1941) and led the revolution in person",
      "Coc Bo Cave, the Lenin Stream, Karl Marx Mountain and the stone worktable",
      "A Special National Relic and pilgrimage site beside border marker 108"
    ],
    "highlights_ru": [
      "Место возвращения Хо Ши Мина во Вьетнам (1941) и личного руководства революцией",
      "Пещера Кокбо, ручей Ленина, гора Карла Маркса и каменный рабочий стол",
      "Особый национальный памятник и место паломничества у пограничного столба № 108"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
      "ticket_vi": "Vé và phí dịch vụ (xe điện) tham khảo khoảng 25.000–50.000 VND/người.",
      "duration_vi": "Khoảng 2–3 giờ.",
      "best_time_vi": "Mùa khô (tháng 10–4); suối Lê-nin xanh trong nhất vào mùa thu.",
      "tips_vi": "Mang giày đi bộ vì phải đi khá xa từ bãi xe; giữ trang nghiêm ở khu đền thờ; kết hợp ngắm cảnh đồng ruộng Hà Quảng."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Khu di tích Pác Bó", "url": "https://vi.wikipedia.org/wiki/Khu_di_t%C3%ADch_P%C3%A1c_B%C3%B3"}
    ],
    "tags": ["history", "monument", "memorial", "nature", "outdoor", "top"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-cao-bang-thang-hen",
    "slug": "thang-hen",
    "region": "vn-cao-bang",
    "country": "vietnam",
    "region_name_vi": "Cao Bằng",
    "federal_district": "Miền Bắc",
    "name_vi": "Hồ Thang Hen",
    "name_ru": "Озеро Тхангхен",
    "name_en": "Thang Hen Lake",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 22.7683, "lon": 106.3550},
    "address_vi": "Xã Quốc Toản, huyện Trà Lĩnh (nay thuộc huyện Trùng Khánh), tỉnh Cao Bằng",
    "rating": {"value": 4.5, "count": 1400, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách ví hồ như 'tuyệt tình cốc' với mặt nước xanh ngọc giữa vách núi đá và rừng cây. Nhiều người thích chèo thuyền, cắm trại yên tĩnh; một số lưu ý mực nước và màu hồ thay đổi theo mùa.",
    "presentation_short_vi": "Hồ Thang Hen ở huyện Trà Lĩnh, tỉnh Cao Bằng là một hồ nước ngọt trên núi ở độ cao hơn 1.000 m, nổi tiếng với làn nước xanh ngọc bích giữa những vách đá vôi. Được ví như 'tuyệt tình cốc', hồ là điểm dừng thơ mộng trong Công viên địa chất toàn cầu Non nước Cao Bằng.",
    "presentation_short_en": "Thang Hen Lake in Tra Linh district, Cao Bang province, is a freshwater mountain lake perched above 1,000 metres, famed for its jade-green water enclosed by limestone cliffs. Often likened to a hidden 'fairy pool', it is a poetic stop within the Non Nuoc Cao Bang Global Geopark.",
    "presentation_short_ru": "Озеро Тхангхен в уезде Чалинь провинции Каобанг — пресноводное горное озеро на высоте более 1000 метров, знаменитое нефритово-зелёной водой в кольце известняковых скал. Его часто называют укромным «сказочным прудом»; это поэтичная остановка в геопарке ЮНЕСКО «Нонныок-Каобанг».",
    "presentation_long_vi": "Nằm giữa vùng núi non trùng điệp cách thành phố Cao Bằng khoảng 30 km, Hồ Thang Hen thực chất là một quần thể gồm nhiều hồ nhỏ nối thông nhau qua các hang ngầm trong lòng núi đá vôi. Trong tiếng Tày, 'Thang Hen' nghĩa là 'đuôi ong', gợi hình dáng thon dài của hồ. Điều đặc biệt là mực nước và dòng chảy của hồ thay đổi theo mùa và thậm chí trong ngày do hệ thống hang karst ngầm, tạo nên hiện tượng thủy văn hiếm gặp. Mặt hồ phẳng lặng mang màu xanh ngọc bích, phản chiếu vách núi dựng đứng và rừng cây rậm rạp bao quanh, khiến nhiều người ví nơi đây như 'tuyệt tình cốc' chốn bồng lai. Du khách có thể thuê thuyền hoặc bè chèo dọc mặt nước, len qua các eo hồ tĩnh mịch, hoặc cắm trại, dã ngoại bên bờ. Vào mùa mưa, nước dâng cao nối liền các hồ; mùa khô, hồ thu hẹp để lộ những bãi đá và thảm cỏ ven bờ. Là một trong những điểm tiêu biểu của Công viên địa chất toàn cầu UNESCO Non nước Cao Bằng, Thang Hen thường được kết hợp với Bản Giốc và Ngườm Ngao, mang lại trải nghiệm thiên nhiên trong lành, yên bình và đậm chất hoang sơ vùng cao.",
    "presentation_long_en": "Cradled among rolling mountains about 30 km from Cao Bang city, Thang Hen is in fact a cluster of small lakes linked to one another through underground caves within the limestone massif. In the Tay language 'Thang Hen' means 'bee's tail', evoking the lake's slender shape. Remarkably, its water level and current shift with the seasons and even during the day because of the underground karst system, a rare hydrological phenomenon. The still surface glows jade-green, mirroring sheer cliffs and dense forest all around, so that many liken it to a secret 'fairy pool' from a fable. Visitors can hire a boat or raft to glide across the water, weaving through quiet inlets, or simply camp and picnic on the shore. In the rainy season the water rises and merges the lakes; in the dry season it retreats to reveal rocky flats and grassy banks. As one of the signature sites of the UNESCO Non Nuoc Cao Bang Global Geopark, Thang Hen is usually combined with Ban Gioc and Nguom Ngao, offering a fresh, peaceful and wonderfully unspoilt taste of the northern highlands.",
    "presentation_long_ru": "Укрытое среди холмистых гор примерно в 30 км от города Каобанг, Тхангхен — это на самом деле группа небольших озёр, соединённых друг с другом подземными пещерами внутри известнякового массива. На языке тай «Тхангхен» означает «пчелиный хвост», намекая на вытянутую форму озера. Примечательно, что уровень воды и течение меняются в зависимости от сезона и даже в течение дня из-за подземной карстовой системы — редкое гидрологическое явление. Спокойная гладь светится нефритово-зелёным, отражая отвесные скалы и густой лес вокруг, так что многие сравнивают её с тайным «сказочным прудом». Гости могут взять лодку или плот и скользить по воде, петляя по тихим заводям, либо просто разбить лагерь и устроить пикник на берегу. В сезон дождей вода поднимается и объединяет озёра; в сухой сезон отступает, обнажая каменистые отмели и травянистые берега. Как один из знаковых объектов геопарка ЮНЕСКО «Нонныок-Каобанг», Тхангхен обычно осматривают вместе с Банзёк и Нгыомнгао, даря свежие, умиротворяющие и удивительно нетронутые впечатления от северного высокогорья.",
    "highlights_vi": [
      "Hồ nước ngọt trên núi cao >1.000 m, nước xanh ngọc bích",
      "Mực nước đổi theo mùa/ngày nhờ hệ hang karst ngầm — hiện tượng hiếm",
      "Điểm nhấn của Geopark UNESCO Non nước Cao Bằng, hợp để chèo thuyền, cắm trại"
    ],
    "highlights_en": [
      "A freshwater mountain lake above 1,000 m with jade-green water",
      "Water levels shift with season and time of day via an underground karst system — a rare sight",
      "A highlight of the UNESCO Cao Bang Geopark, great for boating and camping"
    ],
    "highlights_ru": [
      "Пресноводное горное озеро выше 1000 м с нефритово-зелёной водой",
      "Уровень воды меняется по сезонам и в течение дня через подземный карст — редкое явление",
      "Изюминка геопарка ЮНЕСКО «Каобанг», подходит для лодок и кемпинга"
    ],
    "practical": {
      "hours_vi": "Mở cửa cả ngày (khu vực ngoài trời).",
      "ticket_vi": "Phí tham quan/thuyền tham khảo khoảng 20.000–50.000 VND/người tùy dịch vụ.",
      "duration_vi": "Khoảng 1,5–2 giờ.",
      "best_time_vi": "Khoảng tháng 8–10 khi nước dâng, hồ xanh và cảnh đẹp nhất.",
      "tips_vi": "Đường lên hồ quanh co, đi xe cẩn thận; mang đồ ăn nhẹ nếu muốn dã ngoại; kết hợp tuyến Bản Giốc – Ngườm Ngao."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Hồ Thang Hen", "url": "https://vi.wikipedia.org/wiki/H%E1%BB%93_Thang_Hen"},
      {"title": "UNESCO Global Geopark — Non Nuoc Cao Bang", "url": "https://www.unesco.org/en/iggp/non-nuoc-cao-bang"}
    ],
    "tags": ["nature", "lake", "geopark", "viewpoint", "outdoor", "boat"],
    "status": "enriched",
    "last_updated": TODAY
  },
]

# ===================== ĐIỆN BIÊN (Miền Bắc) =====================
PLACES += [
  {
    "id": "vn-dien-bien-doi-a1",
    "slug": "doi-a1",
    "region": "vn-dien-bien",
    "country": "vietnam",
    "region_name_vi": "Điện Biên",
    "federal_district": "Miền Bắc",
    "name_vi": "Di tích Đồi A1",
    "name_ru": "Холм A1 (Элиан 2)",
    "name_en": "A1 Hill (Eliane 2)",
    "categories": ["fortress", "monument"],
    "coordinates": {"lat": 21.3835, "lon": 103.0242},
    "address_vi": "Phường Mường Thanh, thành phố Điện Biên Phủ, tỉnh Điện Biên",
    "rating": {"value": 4.6, "count": 3600, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách xúc động khi đứng trên cứ điểm ác liệt nhất của chiến dịch Điện Biên Phủ, còn nguyên hầm hào, xe tăng và hố bộc phá nghìn cân. Nhiều người khen di tích được gìn giữ tốt, thuyết minh giàu cảm xúc.",
    "presentation_short_vi": "Đồi A1 ở thành phố Điện Biên Phủ là cứ điểm phòng ngự then chốt và khốc liệt nhất trong Chiến dịch Điện Biên Phủ năm 1954. Nơi đây còn lưu giữ hệ thống hầm hào, xác xe tăng và hố bộc phá khổng lồ, chứng tích của 39 ngày đêm chiến đấu đẫm máu.",
    "presentation_short_en": "A1 Hill in Dien Bien Phu city was the pivotal and most ferocious defensive strongpoint of the 1954 Dien Bien Phu Campaign. It still preserves trenches, a wrecked tank and the vast crater of a dynamite charge — relics of 39 days and nights of bloody fighting.",
    "presentation_short_ru": "Холм A1 в городе Дьенбьенфу был ключевым и самым ожесточённым оборонительным опорным пунктом кампании при Дьенбьенфу 1954 года. Здесь до сих пор сохранились траншеи, разбитый танк и огромная воронка от подрыва — свидетельства 39 дней и ночей кровопролитных боёв.",
    "presentation_long_vi": "Đồi A1 (quân Pháp gọi là Eliane 2) là ngọn đồi nằm ở trung tâm thành phố Điện Biên Phủ, từng là cứ điểm quan trọng bậc nhất trong tập đoàn cứ điểm của quân Pháp năm 1954. Đây là nơi diễn ra những trận đánh giằng co, ác liệt và kéo dài nhất của Chiến dịch Điện Biên Phủ: bộ đội Việt Nam và quân Pháp giành nhau từng thước hào, từng ụ súng suốt 39 ngày đêm. Đỉnh điểm là rạng sáng 7/5/1954, khối bộc phá gần 1.000 kg thuốc nổ được đặt trong đường hầm đào ngầm dưới lòng đồi phát nổ, mở đường cho đợt tổng công kích cuối cùng, góp phần quyết định làm nên chiến thắng 'lừng lẫy năm châu, chấn động địa cầu'. Ngày nay, du khách leo theo bậc thang lên đỉnh đồi, đi giữa hệ thống giao thông hào được phục dựng, tận mắt thấy xác chiếc xe tăng của quân Pháp, khẩu pháo, hầm chỉ huy và miệng hố bộc phá sâu hoắm nay đã thành 'chứng nhân' lịch sử. Trên đỉnh đồi có đài tưởng niệm và mộ các liệt sĩ. Gắn liền với Bảo tàng Chiến thắng Điện Biên Phủ và các cứ điểm lân cận, Đồi A1 là điểm đến không thể bỏ qua để hiểu về một trong những chiến thắng vĩ đại nhất lịch sử Việt Nam.",
    "presentation_long_en": "A1 Hill (called Eliane 2 by the French) rises in the centre of Dien Bien Phu city and was among the most important strongpoints in the French fortified complex of 1954. It saw the longest and most savage seesaw combat of the Dien Bien Phu Campaign, as Vietnamese troops and the French garrison fought for every metre of trench and every gun emplacement over 39 days and nights. The climax came at dawn on 7 May 1954, when a charge of nearly 1,000 kg of explosives, placed in a tunnel dug beneath the hill, was detonated to open the way for the final assault — a decisive stroke in a victory that 'shook the globe'. Today visitors climb steps to the summit, walk through reconstructed communication trenches, and see the wreck of a French tank, an artillery piece, the command bunker and the gaping crater of the explosion, now a silent witness to history. A memorial and the graves of fallen soldiers crown the hilltop. Paired with the Dien Bien Phu Victory Museum and neighbouring strongpoints, A1 Hill is an essential stop for understanding one of the greatest victories in Vietnamese history.",
    "presentation_long_ru": "Холм A1 (у французов — Элиан 2) возвышается в центре города Дьенбьенфу и был одним из важнейших опорных пунктов французского укреплённого района 1954 года. Здесь развернулись самые продолжительные и жестокие переменные бои кампании при Дьенбьенфу: вьетнамские войска и французский гарнизон сражались за каждый метр траншеи и каждую огневую точку в течение 39 дней и ночей. Кульминация наступила на рассвете 7 мая 1954 года, когда заряд почти в 1000 кг взрывчатки, заложенный в прорытом под холмом туннеле, был подорван, открыв путь для решающего штурма — переломного удара в победе, которая «потрясла мир». Сегодня посетители поднимаются по ступеням на вершину, проходят по восстановленным ходам сообщения и видят остов французского танка, орудие, командный бункер и зияющую воронку от взрыва — молчаливого свидетеля истории. Вершину венчают мемориал и могилы павших бойцов. Вместе с Музеем победы при Дьенбьенфу и соседними опорными пунктами холм A1 — обязательная остановка для понимания одной из величайших побед в истории Вьетнама.",
    "highlights_vi": [
      "Cứ điểm ác liệt nhất Chiến dịch Điện Biên Phủ 1954 (Pháp gọi Eliane 2)",
      "Còn nguyên giao thông hào, xác xe tăng và hố bộc phá gần 1.000 kg thuốc nổ",
      "Gắn với đại thắng 7/5/1954 'lừng lẫy năm châu, chấn động địa cầu'"
    ],
    "highlights_en": [
      "The fiercest strongpoint of the 1954 Dien Bien Phu Campaign (French Eliane 2)",
      "Preserved trenches, a wrecked tank and the crater of a ~1,000 kg charge",
      "Site of the decisive 7 May 1954 victory that 'shook the globe'"
    ],
    "highlights_ru": [
      "Самый ожесточённый опорный пункт кампании 1954 года (франц. Элиан 2)",
      "Сохранены траншеи, разбитый танк и воронка от заряда ~1000 кг",
      "Место решающей победы 7 мая 1954 года, которая «потрясла мир»"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 15.000–20.000 VND/người.",
      "duration_vi": "Khoảng 1 giờ.",
      "best_time_vi": "Mùa khô (tháng 10–4); dịp kỷ niệm Chiến thắng 7/5 rất sôi động.",
      "tips_vi": "Kết hợp Bảo tàng Chiến thắng Điện Biên Phủ, Hầm Đờ Cát và Nghĩa trang A1 gần đó; nên thuê thuyết minh."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Đồi A1", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%93i_A1"}
    ],
    "tags": ["history", "war", "monument", "fortress", "top", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-dien-bien-ham-de-castries",
    "slug": "ham-de-castries",
    "region": "vn-dien-bien",
    "country": "vietnam",
    "region_name_vi": "Điện Biên",
    "federal_district": "Miền Bắc",
    "name_vi": "Hầm Đờ Cát (Sở chỉ huy tập đoàn cứ điểm)",
    "name_ru": "Бункер генерала де Кастри",
    "name_en": "De Castries' Bunker",
    "categories": ["monument", "fortress"],
    "coordinates": {"lat": 21.3878, "lon": 103.0083},
    "address_vi": "Cánh đồng Mường Thanh, thành phố Điện Biên Phủ, tỉnh Điện Biên",
    "rating": {"value": 4.5, "count": 1700, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách thích thú khi thấy căn hầm chỉ huy kiên cố còn nguyên vẹn, nơi tướng Đờ Cát bị bắt sống ngày 7/5/1954. Nhiều người khen nằm giữa cánh đồng Mường Thanh, dễ hình dung trận đánh; một số mong có thêm bảng thuyết minh.",
    "presentation_short_vi": "Hầm Đờ Cát là sở chỉ huy của tướng Christian de Castries, chỉ huy tập đoàn cứ điểm Điện Biên Phủ của quân Pháp. Chiều 7/5/1954, bộ đội Việt Nam tràn vào bắt sống toàn bộ bộ chỉ huy, kết thúc chiến dịch và cuộc kháng chiến chống Pháp.",
    "presentation_short_en": "De Castries' Bunker was the command post of General Christian de Castries, commander of the French fortified complex at Dien Bien Phu. On the afternoon of 7 May 1954 Vietnamese troops stormed it and captured the entire staff, ending the campaign and the war against France.",
    "presentation_short_ru": "Бункер де Кастри был командным пунктом генерала Кристиана де Кастри, командующего французским укреплённым районом при Дьенбьенфу. Днём 7 мая 1954 года вьетнамские войска ворвались в него и взяли в плен весь штаб, завершив кампанию и войну против Франции.",
    "presentation_long_vi": "Nằm giữa cánh đồng Mường Thanh, ngay trung tâm lòng chảo Điện Biên, Hầm Đờ Cát là căn hầm chỉ huy kiên cố của tướng Christian de Castries, tổng chỉ huy tập đoàn cứ điểm Điện Biên Phủ – pháo đài mà quân Pháp từng tự tin là 'bất khả xâm phạm'. Căn hầm dài khoảng 20 m, rộng 8 m, được gia cố bằng nhiều lớp bao cát, ván gỗ và tấm ghi sắt, chia thành các phòng làm việc và nghỉ của bộ chỉ huy, xung quanh là hệ thống hàng rào dây thép gai và hầm hào dày đặc. Sau 56 ngày đêm 'khoét núi, ngủ hầm, mưa dầm, cơm vắt', vào 17 giờ 30 ngày 7/5/1954, các chiến sĩ Việt Nam đã đánh thẳng vào sở chỉ huy, bắt sống tướng de Castries cùng toàn bộ ban tham mưu, cắm lá cờ 'Quyết chiến quyết thắng' trên nóc hầm. Khoảnh khắc ấy đánh dấu sự sụp đổ hoàn toàn của tập đoàn cứ điểm và chiến thắng lịch sử Điện Biên Phủ. Ngày nay, du khách có thể chui vào lòng hầm còn được bảo tồn gần như nguyên trạng, đi giữa những dấu vết chiến tranh và hình dung khoảnh khắc quyết định của lịch sử dân tộc.",
    "presentation_long_en": "Standing in the middle of the Muong Thanh field at the heart of the Dien Bien basin, De Castries' Bunker was the fortified command post of General Christian de Castries, overall commander of the Dien Bien Phu fortified complex — a stronghold the French had confidently deemed 'impregnable'. About 20 m long and 8 m wide, the bunker was reinforced with layers of sandbags, timber and steel matting and divided into offices and quarters for the staff, ringed by dense barbed wire and trenches. After 56 days and nights of 'digging into hills, sleeping in trenches, soaked by rain and eating cold rice', at 17:30 on 7 May 1954 Vietnamese soldiers charged straight into the command post, captured de Castries and his entire staff, and planted the 'Determined to Fight, Determined to Win' flag on its roof. That moment marked the total collapse of the complex and the historic victory of Dien Bien Phu. Today visitors can step down into the bunker, preserved almost intact, walking among the traces of war and imagining that decisive moment in the nation's history.",
    "presentation_long_ru": "Стоящий посреди поля Мыонгтхань в центре котловины Дьенбьен, бункер де Кастри был укреплённым командным пунктом генерала Кристиана де Кастри, главнокомандующего укреплённым районом Дьенбьенфу — крепости, которую французы уверенно считали «неприступной». Длиной около 20 м и шириной 8 м, бункер был усилён слоями мешков с песком, брёвен и стальных настилов и разделён на кабинеты и жилые помещения штаба, окружённые густыми рядами колючей проволоки и траншеями. После 56 дней и ночей, когда бойцы «врубались в горы, спали в окопах, мокли под дождём и ели холодный рис», в 17:30 7 мая 1954 года вьетнамские солдаты ворвались прямо в командный пункт, взяли в плен де Кастри со всем штабом и водрузили на крыше знамя «Решимость сражаться, решимость победить». Этот момент ознаменовал полный крах укреплённого района и историческую победу при Дьенбьенфу. Сегодня посетители могут спуститься в почти нетронутый бункер, пройти среди следов войны и представить себе тот решающий момент в истории страны. Бункер обычно осматривают вместе с холмом A1, Музеем победы и другими опорными пунктами поля Мыонгтхань, что помогает восстановить в воображении весь ход сражения; сам осмотр занимает всего около получаса.",
    "highlights_vi": [
      "Sở chỉ huy của tướng de Castries — 'trái tim' tập đoàn cứ điểm Điện Biên Phủ",
      "Nơi bộ đội Việt Nam bắt sống bộ chỉ huy Pháp lúc 17h30 ngày 7/5/1954",
      "Căn hầm gia cố còn gần nguyên trạng giữa cánh đồng Mường Thanh"
    ],
    "highlights_en": [
      "Command post of General de Castries — the 'heart' of the Dien Bien Phu complex",
      "Where Vietnamese troops captured the French command at 17:30 on 7 May 1954",
      "A reinforced bunker preserved almost intact on the Muong Thanh field"
    ],
    "highlights_ru": [
      "Командный пункт генерала де Кастри — «сердце» укрепрайона Дьенбьенфу",
      "Место пленения французского командования в 17:30 7 мая 1954 года",
      "Усиленный бункер, сохранившийся почти нетронутым, посреди поля Мыонгтхань"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 15.000 VND/người.",
      "duration_vi": "Khoảng 30–45 phút.",
      "best_time_vi": "Mùa khô (tháng 10–4).",
      "tips_vi": "Kết hợp Đồi A1 và Bảo tàng Chiến thắng; hầm thấp và tối, chú ý khi bước xuống."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Trận Điện Biên Phủ", "url": "https://vi.wikipedia.org/wiki/Chi%E1%BA%BFn_d%E1%BB%8Bch_%C4%90i%E1%BB%87n_Bi%C3%AAn_Ph%E1%BB%A7"}
    ],
    "tags": ["history", "war", "monument", "fortress", "indoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-dien-bien-tuong-dai-chien-thang",
    "slug": "tuong-dai-chien-thang",
    "region": "vn-dien-bien",
    "country": "vietnam",
    "region_name_vi": "Điện Biên",
    "federal_district": "Miền Bắc",
    "name_vi": "Tượng đài Chiến thắng Điện Biên Phủ",
    "name_ru": "Монумент Победы при Дьенбьенфу",
    "name_en": "Dien Bien Phu Victory Monument",
    "categories": ["monument"],
    "coordinates": {"lat": 21.3897, "lon": 103.0189},
    "address_vi": "Đồi D1, phường Mường Thanh, thành phố Điện Biên Phủ, tỉnh Điện Biên",
    "rating": {"value": 4.6, "count": 2100, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách ấn tượng với tượng đài đồng đồ sộ trên đỉnh đồi D1, nhìn bao quát thành phố. Nhiều người leo bậc thang lên chân tượng để chụp ảnh và ngắm toàn cảnh lòng chảo Điện Biên.",
    "presentation_short_vi": "Tượng đài Chiến thắng Điện Biên Phủ trên đỉnh đồi D1 là quần thể tượng đài bằng đồng lớn bậc nhất Việt Nam, khánh thành năm 2004 nhân 50 năm chiến thắng. Tượng khắc họa nhóm bộ đội với lá cờ và em bé Thái, biểu tượng cho khát vọng hòa bình.",
    "presentation_short_en": "The Dien Bien Phu Victory Monument atop D1 Hill is one of Vietnam's largest bronze monuments, unveiled in 2004 for the 50th anniversary of the victory. It depicts a group of soldiers with a flag and a Thai ethnic child, a symbol of the yearning for peace.",
    "presentation_short_ru": "Монумент Победы при Дьенбьенфу на вершине холма D1 — один из крупнейших бронзовых памятников Вьетнама, открытый в 2004 году к 50-летию победы. Он изображает группу солдат со знаменем и ребёнка из народа тай — символ стремления к миру.",
    "presentation_long_vi": "Sừng sững trên đỉnh đồi D1 giữa trung tâm thành phố Điện Biên Phủ, Tượng đài Chiến thắng Điện Biên Phủ là công trình được khánh thành ngày 30/4/2004, đúng dịp kỷ niệm 50 năm chiến thắng lịch sử. Đây là một trong những tượng đài bằng đồng nguyên khối lớn nhất Việt Nam: cụm tượng cao khoảng 12,6 m (tính cả bệ), nặng tới 220 tấn, được đúc từ nhiều tấn đồng và ghép từ hàng trăm khối. Tác phẩm khắc họa nhóm ba chiến sĩ đứng quây quần: một người giương cao lá cờ 'Quyết chiến quyết thắng', một người bồng em bé dân tộc Thái tay cầm bó hoa, thể hiện tình đoàn kết quân dân và khát vọng hòa bình sau chiến tranh. Từ chân tượng, du khách leo hơn 300 bậc thang, vừa đi vừa phóng tầm mắt bao quát toàn cảnh lòng chảo Mường Thanh, cánh đồng lúa và những cứ điểm lịch sử như Đồi A1, Hầm Đờ Cát phía xa. Vào các dịp lễ, nơi đây rực rỡ cờ hoa và là điểm hành hương của người dân cả nước. Kết hợp cùng Bảo tàng Chiến thắng và các di tích lân cận, tượng đài giúp du khách cảm nhận trọn vẹn tầm vóc và ý nghĩa của chiến thắng 'chấn động địa cầu'.",
    "presentation_long_en": "Towering on the summit of D1 Hill in the centre of Dien Bien Phu city, the Victory Monument was inaugurated on 30 April 2004 for the 50th anniversary of the historic triumph. It is one of the largest solid bronze monuments in Vietnam: the sculptural group stands about 12.6 m tall including its base and weighs some 220 tonnes, cast from many tonnes of bronze and assembled from hundreds of sections. The work portrays three soldiers grouped together: one raising the 'Determined to Fight, Determined to Win' flag, another cradling a Thai ethnic child holding a bunch of flowers, expressing the bond between army and people and the longing for peace after war. From the base, visitors climb more than 300 steps, taking in a sweeping view of the Muong Thanh basin, its rice fields and historic strongpoints such as A1 Hill and De Castries' Bunker in the distance. On public holidays the site blazes with flags and flowers and draws pilgrims from across the country. Together with the Victory Museum and nearby relics, the monument lets visitors grasp the full scale and meaning of a victory that 'shook the globe'.",
    "presentation_long_ru": "Возвышаясь на вершине холма D1 в центре города Дьенбьенфу, Монумент Победы был открыт 30 апреля 2004 года к 50-летию исторического триумфа. Это один из крупнейших цельнобронзовых памятников Вьетнама: скульптурная группа достигает около 12,6 м в высоту вместе с постаментом и весит примерно 220 тонн, отлитая из многих тонн бронзы и собранная из сотен секций. Композиция изображает трёх бойцов: один поднимает знамя «Решимость сражаться, решимость победить», другой держит на руках ребёнка из народа тай с букетом цветов, выражая единство армии и народа и стремление к миру после войны. От подножия посетители поднимаются более чем по 300 ступеням, любуясь широкой панорамой котловины Мыонгтхань, её рисовых полей и исторических опорных пунктов — холма A1 и бункера де Кастри вдали. В праздничные дни здесь пестрят флаги и цветы, сюда съезжаются паломники со всей страны. Вместе с Музеем победы и соседними памятниками монумент позволяет в полной мере осознать масштаб и значение победы, которая «потрясла мир».",
    "highlights_vi": [
      "Tượng đài đồng lớn bậc nhất Việt Nam, khánh thành 2004 (50 năm chiến thắng)",
      "Cụm tượng ~12,6 m, nặng ~220 tấn trên đỉnh đồi D1",
      "Điểm ngắm toàn cảnh lòng chảo Mường Thanh và các cứ điểm lịch sử"
    ],
    "highlights_en": [
      "One of Vietnam's largest bronze monuments, unveiled in 2004 (50th anniversary)",
      "A ~12.6 m, ~220-tonne sculptural group atop D1 Hill",
      "A panoramic viewpoint over the Muong Thanh basin and battle sites"
    ],
    "highlights_ru": [
      "Один из крупнейших бронзовых памятников Вьетнама, открыт в 2004 году",
      "Скульптурная группа ~12,6 м и ~220 тонн на вершине холма D1",
      "Панорамная точка над котловиной Мыонгтхань и полями сражений"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 15.000 VND/người.",
      "duration_vi": "Khoảng 45 phút–1 giờ.",
      "best_time_vi": "Chiều muộn mát mẻ; dịp 7/5 rất trang trọng.",
      "tips_vi": "Chuẩn bị leo hơn 300 bậc; mang nước; kết hợp Đồi A1 và Bảo tàng Chiến thắng gần đó."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Tượng đài Chiến thắng Điện Biên Phủ", "url": "https://vi.wikipedia.org/wiki/T%C6%B0%E1%BB%A3ng_%C4%91%C3%A0i_Chi%E1%BA%BFn_th%E1%BA%AFng_%C4%90i%E1%BB%87n_Bi%C3%AAn_Ph%E1%BB%A7"}
    ],
    "tags": ["history", "monument", "viewpoint", "top", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
]

# ===================== SƠN LA (Miền Bắc) =====================
PLACES += [
  {
    "id": "vn-son-la-moc-chau",
    "slug": "moc-chau",
    "region": "vn-son-la",
    "country": "vietnam",
    "region_name_vi": "Sơn La",
    "federal_district": "Miền Bắc",
    "name_vi": "Cao nguyên Mộc Châu",
    "name_ru": "Плато Мокчау",
    "name_en": "Moc Chau Plateau",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 20.8377, "lon": 104.6386},
    "address_vi": "Thị xã Mộc Châu, tỉnh Sơn La",
    "rating": {"value": 4.6, "count": 5200, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách mê mẩn những đồi chè xanh mướt, vườn mận, vườn dâu và biển mây buổi sớm. Nhiều người khen khí hậu mát lạnh quanh năm, mùa hoa mận/hoa cải trắng rất đẹp; một số nhắc cuối tuần khá đông.",
    "presentation_short_vi": "Cao nguyên Mộc Châu ở tỉnh Sơn La là vùng cao nguyên xanh mát ở độ cao trên 1.000 m, nổi tiếng với đồi chè trập trùng, đồng cỏ nuôi bò sữa và các mùa hoa nối tiếp quanh năm. Đây là điểm nghỉ dưỡng, 'săn mây' và trải nghiệm văn hóa dân tộc Thái, Mông hấp dẫn ở Tây Bắc.",
    "presentation_short_en": "The Moc Chau Plateau in Son La province is a cool green highland above 1,000 metres, famed for rolling tea hills, dairy pastures and a year-round succession of flower seasons. It is a beloved Northwest retreat for cloud-hunting and for experiencing Thai and Hmong ethnic culture.",
    "presentation_short_ru": "Плато Мокчау в провинции Шонла — прохладное зелёное нагорье выше 1000 метров, знаменитое холмами чайных плантаций, молочными пастбищами и сменяющими друг друга круглый год сезонами цветения. Это любимое место отдыха на Северо-Западе для «охоты за облаками» и знакомства с культурой тай и хмонг.",
    "presentation_long_vi": "Cách Hà Nội khoảng 180 km theo quốc lộ 6, Cao nguyên Mộc Châu trải rộng trên độ cao trung bình hơn 1.000 m, mang khí hậu ôn hòa, mát mẻ quanh năm – được ví như 'Đà Lạt của Tây Bắc'. Nổi bật nhất là những đồi chè xanh mướt uốn lượn theo triền đồi, trong đó có đồi chè trái tim nổi tiếng, cùng những đồng cỏ chăn nuôi bò sữa quy mô lớn. Mộc Châu quyến rũ du khách bằng các mùa hoa nối tiếp: hoa mận, hoa đào nở trắng hồng khắp thung lũng dịp cuối đông – đầu xuân; hoa cải trắng, cải vàng vào đầu đông; hoa ban, dã quỳ theo mùa. Buổi sớm, du khách có thể 'săn mây' trên những đỉnh đồi, ngắm biển mây bồng bềnh phủ kín thung lũng. Vùng đất này còn là nơi sinh sống của đồng bào Thái, Mông, Dao với chợ phiên rực rỡ sắc màu, những bản làng homestay ấm cúng, điệu xòe Thái và ẩm thực núi rừng như bê chao, cá suối, sữa chua Mộc Châu. Ngoài ra còn có thác Dải Yếm, rừng thông bản Áng, hang Dơi, thung lũng mận Nà Ka. Với thiên nhiên trong lành và trải nghiệm văn hóa đậm đà, Mộc Châu là điểm đến bốn mùa lý tưởng cho những chuyến nghỉ dưỡng và khám phá.",
    "presentation_long_en": "About 180 km from Hanoi along Highway 6, the Moc Chau Plateau spreads across an average altitude of more than 1,000 metres, with a mild, cool climate all year — often called the 'Da Lat of the Northwest'. Its signature sight is the sweep of emerald tea hills curving over the slopes, including the celebrated heart-shaped tea plot, alongside large dairy pastures. Moc Chau charms visitors with a relay of flower seasons: plum and peach blossom whiten the valleys in late winter and early spring; white and yellow mustard flowers bloom in early winter; bauhinia and wild sunflowers follow in turn. At dawn, travellers go cloud-hunting on the hilltops, watching seas of mist drift over the valleys. The plateau is home to Thai, Hmong and Dao communities, with vivid market days, cosy homestay villages, the Thai xoe dance and mountain fare such as fried veal, stream fish and Moc Chau yoghurt. Nearby attractions include Dai Yem Waterfall, the Ban Ang pine forest, Bat Cave and the Na Ka plum valley. With its fresh nature and rich cultural life, Moc Chau is an ideal four-season destination for both relaxation and discovery.",
    "presentation_long_ru": "Примерно в 180 км от Ханоя по шоссе № 6 плато Мокчау раскинулось на средней высоте более 1000 метров, с мягким прохладным климатом круглый год — его часто называют «Далатом Северо-Запада». Его визитная карточка — изумрудные чайные холмы, изгибающиеся по склонам, включая знаменитую плантацию в форме сердца, а также обширные молочные пастбища. Мокчау очаровывает гостей чередой сезонов цветения: сливы и персики белеют в долинах в конце зимы и начале весны; белая и жёлтая горчица цветёт в начале зимы; следом идут баугиния и дикие подсолнухи. На рассвете путешественники «охотятся за облаками» на вершинах холмов, наблюдая, как моря тумана плывут над долинами. Плато населяют общины тай, хмонг и зао, здесь яркие базарные дни, уютные деревни-хоумстеи, танец сое народа тай и горная кухня — жареная телятина, речная рыба и йогурт Мокчау. Поблизости — водопад Зайем, сосновый лес Бананг, Пещера летучих мышей и сливовая долина Нака. Благодаря свежей природе и насыщенной культурной жизни Мокчау — идеальное всесезонное направление и для отдыха, и для открытий.",
    "highlights_vi": [
      "'Đà Lạt của Tây Bắc': đồi chè, đồng cỏ bò sữa, khí hậu mát quanh năm",
      "Các mùa hoa nối tiếp: mận, đào, cải trắng; sớm mai 'săn mây'",
      "Văn hóa Thái – Mông – Dao, chợ phiên, homestay và ẩm thực núi rừng"
    ],
    "highlights_en": [
      "The 'Da Lat of the Northwest': tea hills, dairy pastures, year-round cool air",
      "A relay of flower seasons — plum, peach, mustard; sunrise cloud-hunting",
      "Thai–Hmong–Dao culture, market days, homestays and mountain cuisine"
    ],
    "highlights_ru": [
      "«Далат Северо-Запада»: чайные холмы, молочные пастбища, прохлада круглый год",
      "Череда сезонов цветения — слива, персик, горчица; «охота за облаками» на рассвете",
      "Культура тай–хмонг–зао, базарные дни, хоумстеи и горная кухня"
    ],
    "practical": {
      "hours_vi": "Khu vực mở quanh năm; các điểm tham quan mở ban ngày.",
      "ticket_vi": "Nhiều điểm thu vé riêng (đồi chè, vườn hoa, thác) khoảng 20.000–60.000 VND.",
      "duration_vi": "1–2 ngày để tham quan trọn vẹn.",
      "best_time_vi": "Cuối đông – đầu xuân (mùa hoa mận, đào); tháng 11 hoa cải; mùa hè mát mẻ.",
      "tips_vi": "Mang áo ấm vì đêm lạnh; đặt homestay sớm dịp lễ; thử sữa chua, bê chao Mộc Châu."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Mộc Châu", "url": "https://vi.wikipedia.org/wiki/M%E1%BB%99c_Ch%C3%A2u"}
    ],
    "tags": ["nature", "highland", "tea", "flowers", "viewpoint", "family", "top", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-son-la-nha-tu-son-la",
    "slug": "nha-tu-son-la",
    "region": "vn-son-la",
    "country": "vietnam",
    "region_name_vi": "Sơn La",
    "federal_district": "Miền Bắc",
    "name_vi": "Nhà tù Sơn La",
    "name_ru": "Тюрьма Шонла",
    "name_en": "Son La Prison",
    "categories": ["monument", "museum"],
    "coordinates": {"lat": 21.3283, "lon": 103.9089},
    "address_vi": "Đồi Khau Cả, phường Tô Hiệu, thành phố Sơn La, tỉnh Sơn La",
    "rating": {"value": 4.5, "count": 1500, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách lặng người trước những dãy xà lim, cùm sắt và cây đào Tô Hiệu gắn với người tù cộng sản. Nhiều người đánh giá đây là 'địa chỉ đỏ' giàu cảm xúc, thuyết minh sâu sắc.",
    "presentation_short_vi": "Nhà tù Sơn La do thực dân Pháp xây năm 1908 trên đồi Khau Cả để giam cầm tù chính trị. Nơi đây từng giam nhiều nhà cách mạng Việt Nam và gắn với cây đào Tô Hiệu, biểu tượng cho ý chí kiên cường giữa lao tù.",
    "presentation_short_en": "Son La Prison was built by the French colonial regime in 1908 on Khau Ca Hill to hold political prisoners. It once confined many Vietnamese revolutionaries and is remembered for the 'To Hieu peach tree', a symbol of unbroken will behind bars.",
    "presentation_short_ru": "Тюрьма Шонла была построена французской колониальной администрацией в 1908 году на холме Кхаука для содержания политических заключённых. Здесь томились многие вьетнамские революционеры; с ней связано «персиковое дерево То Хьеу» — символ несломленной воли в неволе.",
    "presentation_long_vi": "Tọa lạc trên đỉnh đồi Khau Cả giữa thành phố Sơn La, Nhà tù Sơn La được thực dân Pháp xây dựng từ năm 1908 và mở rộng nhiều lần, biến vùng rừng thiêng nước độc này thành nơi giam cầm, đày ải các chiến sĩ cách mạng Việt Nam trong những năm 1930–1945. Với khí hậu khắc nghiệt, chế độ hà khắc cùng những xà lim chật hẹp, cùm chân bằng sắt, thực dân Pháp hòng dùng nơi đây để tiêu hao ý chí của những người yêu nước. Thế nhưng chính trong ngục tù, các đảng viên cộng sản đã biến nhà tù thành 'trường học cách mạng', tổ chức chi bộ, ra báo bí mật 'Suối Reo' và bồi dưỡng nhiều cán bộ ưu tú. Gắn liền với di tích là hình ảnh đồng chí Tô Hiệu và cây đào ông trồng bên xà lim – 'cây đào Tô Hiệu' đã trở thành biểu tượng bất diệt cho sức sống và tinh thần lạc quan cách mạng. Trải qua bom đạn chiến tranh, phần lớn nhà tù đổ nát, nay được bảo tồn cùng bảo tàng trưng bày hiện vật, tư liệu. Đến đây, du khách đi giữa những bức tường loang lổ, dãy xà lim tối, lặng mình tưởng nhớ và cảm phục ý chí kiên trung của các thế hệ đi trước.",
    "presentation_long_en": "Set atop Khau Ca Hill in the middle of Son La city, Son La Prison was built by the French from 1908 and enlarged several times, turning this harsh, malaria-ridden upland into a place to jail and wear down Vietnamese revolutionaries in the years 1930–1945. With a brutal climate, a merciless regime, cramped cells and iron leg-shackles, the colonial authorities meant to break the patriots' spirit. Yet within the walls the communist prisoners turned the jail into a 'school of revolution', forming a party cell, issuing the clandestine newspaper 'Suoi Reo' (Murmuring Stream) and training many capable cadres. The site is bound to the memory of To Hieu and the peach tree he planted beside his cell — the 'To Hieu peach tree' has become an enduring symbol of vitality and revolutionary optimism. Largely ruined by wartime bombing, the prison is now preserved alongside a museum displaying artefacts and documents. Walking among the pockmarked walls and dim cell blocks, visitors fall silent in remembrance and admiration for the steadfast will of earlier generations.",
    "presentation_long_ru": "Расположенная на вершине холма Кхаука в центре города Шонла, тюрьма Шонла была построена французами с 1908 года и несколько раз расширялась, превратив это суровое, кишащее малярией нагорье в место заключения и изнурения вьетнамских революционеров в 1930–1945 годах. Жестокий климат, беспощадный режим, тесные камеры и железные кандалы — так колониальные власти намеревались сломить дух патриотов. Но за стенами заключённые-коммунисты превратили тюрьму в «школу революции»: создали партийную ячейку, выпускали подпольную газету «Суой Рео» («Журчащий ручей») и подготовили немало способных кадров. С памятником связана память о То Хьеу и посаженном им у камеры персиковом дереве — «персиковое дерево То Хьеу» стало непреходящим символом жизненной силы и революционного оптимизма. Сильно разрушенная бомбардировками военных лет, тюрьма ныне сохранена вместе с музеем, где выставлены артефакты и документы. Проходя среди испещрённых стен и сумрачных камер, посетители умолкают в память и в восхищении перед стойкой волей прежних поколений. Весной у стен вновь распускается персиковое дерево То Хьеу, а соседний музей дополняет рассказ подлинными документами, фотографиями и личными вещами узников, поэтому визит сюда часто совмещают с осмотром центра города Шонла.",
    "highlights_vi": [
      "Nhà tù do Pháp xây 1908, 'địa ngục trần gian' giam tù chính trị 1930–1945",
      "Được biến thành 'trường học cách mạng'; báo bí mật 'Suối Reo'",
      "Gắn với đồng chí Tô Hiệu và cây đào Tô Hiệu biểu tượng"
    ],
    "highlights_en": [
      "A prison built by the French in 1908 to jail political prisoners (1930–1945)",
      "Turned by inmates into a 'school of revolution' with the secret paper 'Suoi Reo'",
      "Bound to To Hieu and the symbolic 'To Hieu peach tree'"
    ],
    "highlights_ru": [
      "Тюрьма, построенная французами в 1908 году для политзаключённых (1930–1945)",
      "Превращена узниками в «школу революции» с подпольной газетой «Суой Рео»",
      "Связана с То Хьеу и символическим «персиковым деревом То Хьеу»"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 20.000 VND/người.",
      "duration_vi": "Khoảng 1–1,5 giờ.",
      "best_time_vi": "Quanh năm; mùa xuân cây đào Tô Hiệu nở hoa.",
      "tips_vi": "Nên thuê thuyết minh để hiểu chiều sâu lịch sử; giữ trang nghiêm; kết hợp thăm Quảng trường Tây Bắc gần đó."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Nhà tù Sơn La", "url": "https://vi.wikipedia.org/wiki/Nh%C3%A0_t%C3%B9_S%C6%A1n_La"}
    ],
    "tags": ["history", "monument", "museum", "memorial", "indoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-son-la-thac-dai-yem",
    "slug": "thac-dai-yem",
    "region": "vn-son-la",
    "country": "vietnam",
    "region_name_vi": "Sơn La",
    "federal_district": "Miền Bắc",
    "name_vi": "Thác Dải Yếm",
    "name_ru": "Водопад Зайем",
    "name_en": "Dai Yem Waterfall",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 20.8000, "lon": 104.5800},
    "address_vi": "Xã Mường Sang, thị xã Mộc Châu, tỉnh Sơn La",
    "rating": {"value": 4.3, "count": 2400, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách thích dòng thác trắng xóa nhiều tầng giữa rừng cây và cây cầu kính 'tình yêu' để chụp ảnh. Nhiều người khen mùa hè – thu nước đẹp; một số nhắc mùa khô nước ít.",
    "presentation_short_vi": "Thác Dải Yếm ở Mộc Châu, tỉnh Sơn La là dòng thác đẹp buông xuống nhiều tầng như dải lụa, gắn với truyền thuyết tình yêu của người Thái. Xung quanh có cầu kính và không gian check-in, là điểm dừng chân mát lành trên cao nguyên.",
    "presentation_short_en": "Dai Yem Waterfall in Moc Chau, Son La province, spills in silky tiers and is tied to a Thai legend of love. With a glass bridge and photo spots nearby, it is a refreshing stop on the plateau.",
    "presentation_short_ru": "Водопад Зайем в Мокчау, провинция Шонла, падает шелковистыми ступенями и связан с легендой народа тай о любви. Рядом стеклянный мост и площадки для фото — освежающая остановка на плато.",
    "presentation_long_vi": "Nằm ở xã Mường Sang, cách trung tâm Mộc Châu khoảng 5 km, Thác Dải Yếm là một trong những thác nước đẹp nhất vùng Tây Bắc. Tên gọi 'Dải Yếm' bắt nguồn từ truyền thuyết về một cô gái Thái đã dùng dải yếm của mình làm dây cứu chàng trai thoát khỏi dòng nước lũ, và dòng thác chính là hiện thân của tình yêu ấy. Thác bắt nguồn từ hai khe nước trên núi, đổ xuống thành nhiều tầng bậc đá, khi thì tuôn trắng xóa mạnh mẽ, khi lại mềm mại như dải lụa vắt ngang sườn đồi xanh. Vào mùa mưa và đầu thu (khoảng tháng 4 đến tháng 10), nước dồi dào, thác đẹp và hùng vĩ nhất; mùa khô nước ít hơn nhưng khung cảnh vẫn nên thơ. Khu vực quanh thác được đầu tư thành điểm tham quan với lối đi, vườn hoa, và đặc biệt là cây cầu kính 'tình yêu' cùng các tiểu cảnh chụp ảnh thu hút giới trẻ. Không khí trong lành, mát rượi cùng tiếng nước reo giữa rừng cây khiến nơi đây trở thành điểm dừng chân thư giãn lý tưởng khi khám phá cao nguyên Mộc Châu, thường được kết hợp cùng đồi chè, rừng thông bản Áng và các vườn hoa.",
    "presentation_long_en": "In Muong Sang commune, about 5 km from central Moc Chau, Dai Yem Waterfall is one of the loveliest falls in the Northwest. The name 'Dai Yem' (a girl's silk bodice-sash) comes from a Thai legend in which a young woman used her sash as a rope to save a drowning man from a flash flood, the waterfall being the embodiment of that love. Fed by two mountain streams, it drops over many rocky tiers — at times pouring in a powerful white cascade, at times as soft as silk draped over the green slope. In the rainy season and early autumn (roughly April to October) the water is abundant and the falls at their most majestic; in the dry season the flow thins but the scene stays poetic. The surroundings have been developed with walkways, flower gardens and, above all, a 'love' glass bridge and photo installations popular with young travellers. The fresh, cool air and the song of falling water amid the forest make this an ideal relaxing stop while exploring the Moc Chau Plateau, usually combined with the tea hills, the Ban Ang pine forest and the flower gardens.",
    "presentation_long_ru": "В общине Мыонгсанг, примерно в 5 км от центра Мокчау, водопад Зайем — один из красивейших на Северо-Западе. Название «Зайем» (шёлковый пояс-корсаж девушки) происходит из легенды народа тай, в которой девушка использовала свой пояс как верёвку, чтобы спасти тонущего юношу во время внезапного паводка, — водопад стал воплощением этой любви. Питаемый двумя горными ручьями, он падает по многим каменным ступеням: то мощным белым каскадом, то мягко, словно шёлк, наброшенный на зелёный склон. В сезон дождей и ранней осенью (примерно с апреля по октябрь) воды много, и водопад наиболее величествен; в сухой сезон поток слабеет, но пейзаж остаётся поэтичным. Окрестности благоустроены дорожками, цветниками и, главное, стеклянным «мостом любви» и фотозонами, популярными у молодёжи. Свежий прохладный воздух и песня падающей воды среди леса делают это место идеальной остановкой для отдыха при знакомстве с плато Мокчау — обычно вместе с чайными холмами, сосновым лесом Бананг и цветниками. Дорога к водопаду проходит через живописные окрестности Мокчау, поэтому его удобно включить в однодневный маршрут по плато; у входа есть кафе и парковка, а спуск к воде занимает лишь несколько минут.",
    "highlights_vi": [
      "Thác nhiều tầng mềm như dải lụa, gắn truyền thuyết tình yêu người Thái",
      "Có cầu kính 'tình yêu' và nhiều tiểu cảnh check-in",
      "Đẹp nhất mùa mưa – đầu thu (tháng 4–10), hợp ghép tuyến Mộc Châu"
    ],
    "highlights_en": [
      "A silky multi-tier fall tied to a Thai legend of love",
      "Features a 'love' glass bridge and many photo spots",
      "Best in the rainy season to early autumn (Apr–Oct); pairs with Moc Chau tours"
    ],
    "highlights_ru": [
      "Шелковистый многоступенчатый водопад из легенды тай о любви",
      "Стеклянный «мост любви» и множество фотозон",
      "Лучше всего с сезона дождей до ранней осени (апрель–октябрь)"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 20.000 VND; cầu kính tính phí riêng.",
      "duration_vi": "Khoảng 1–1,5 giờ.",
      "best_time_vi": "Tháng 4–10 nước nhiều; tránh giữa mùa khô nước cạn.",
      "tips_vi": "Đi giày bám tốt vì đá trơn; kết hợp đồi chè, rừng thông bản Áng; mang đồ chụp ảnh."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Thác Dải Yếm", "url": "https://vi.wikipedia.org/wiki/Th%C3%A1c_D%E1%BA%A3i_Y%E1%BA%BFm"}
    ],
    "tags": ["nature", "waterfall", "viewpoint", "outdoor", "daytrip"],
    "status": "enriched",
    "last_updated": TODAY
  },
]

# ===================== THANH HÓA (Miền Trung) =====================
PLACES += [
  {
    "id": "vn-thanh-hoa-thanh-nha-ho",
    "slug": "thanh-nha-ho",
    "region": "vn-thanh-hoa",
    "country": "vietnam",
    "region_name_vi": "Thanh Hóa",
    "federal_district": "Miền Trung",
    "name_vi": "Thành nhà Hồ",
    "name_ru": "Цитадель династии Хо",
    "name_en": "Citadel of the Ho Dynasty",
    "categories": ["fortress", "monument"],
    "coordinates": {"lat": 20.0781, "lon": 105.6047},
    "address_vi": "Xã Vĩnh Long, huyện Vĩnh Lộc, tỉnh Thanh Hóa",
    "rating": {"value": 4.5, "count": 2900, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách kinh ngạc trước những khối đá xanh khổng lồ xếp khít không cần chất kết dính, nhất là bốn cổng vòm cổ kính. Nhiều người khen giá trị lịch sử độc đáo; một số mong có thêm khu trưng bày và cây xanh che nắng.",
    "presentation_short_vi": "Thành nhà Hồ ở huyện Vĩnh Lộc, tỉnh Thanh Hóa là tòa thành đá độc nhất vô nhị của Việt Nam, xây năm 1397 làm kinh đô nhà Hồ. Được UNESCO công nhận Di sản Thế giới năm 2011, thành nổi bật với kỹ thuật ghép đá khổng lồ tài tình còn nguyên vẹn hơn 600 năm.",
    "presentation_short_en": "The Citadel of the Ho Dynasty in Vinh Loc district, Thanh Hoa province, is Vietnam's only stone citadel, built in 1397 as the Ho dynasty capital. Inscribed by UNESCO as a World Heritage Site in 2011, it is famed for the masterful fitting of colossal stone blocks, intact for over 600 years.",
    "presentation_short_ru": "Цитадель династии Хо в уезде Виньлок провинции Тханьхоа — единственная во Вьетнаме каменная цитадель, построенная в 1397 году как столица династии Хо. Внесённая ЮНЕСКО в список Всемирного наследия в 2011 году, она знаменита виртуозной подгонкой колоссальных каменных блоков, целых уже более 600 лет.",
    "presentation_long_vi": "Thành nhà Hồ (còn gọi là thành Tây Đô) được Hồ Quý Ly cho xây dựng chỉ trong khoảng ba tháng năm 1397, làm kinh đô mới của nước Đại Ngu thay cho Thăng Long. Đây là công trình thành lũy bằng đá có quy mô lớn hiếm hoi còn lại ở Đông Nam Á. Điều khiến giới nghiên cứu khắp thế giới thán phục là kỹ thuật xây dựng: những khối đá xanh nặng hàng chục tấn được đẽo gọt vuông vức rồi xếp chồng khít lên nhau mà không cần vôi vữa, đứng vững suốt hơn sáu thế kỷ qua bao biến động. Tường thành hình gần vuông, mỗi cạnh dài khoảng 800–900 m, mở ra bốn cổng vòm ở bốn hướng, trong đó cổng Nam là lớn nhất với ba vòm cuốn uy nghi. Xung quanh thành từng có hào nước, la thành và đàn tế Nam Giao. Với những giá trị nổi bật toàn cầu về kiến trúc và quy hoạch kinh đô theo thuyết phong thủy, năm 2011 Thành nhà Hồ được UNESCO ghi danh là Di sản Văn hóa Thế giới. Ngày nay, du khách có thể đi qua cổng đá đồ sộ, tham quan khu trưng bày hiện vật khảo cổ và tận mắt chiêm ngưỡng bằng chứng sống động cho tài năng của người Việt xưa.",
    "presentation_long_en": "The Citadel of the Ho Dynasty (also called Tay Do, the 'Western Capital') was built by Ho Quy Ly in only about three months in 1397 as the new capital of the Dai Ngu state, replacing Thang Long. It is one of very few large stone fortresses surviving in Southeast Asia. What astonishes researchers worldwide is its construction technique: blue-stone blocks weighing tens of tonnes were squared off and stacked tightly together without mortar, standing firm through more than six centuries of upheaval. The nearly square rampart, each side about 800–900 m long, opens through four arched gates, the southern one grandest with three vaulted passages. The citadel was once surrounded by a moat, an outer wall and the Nam Giao esplanade for heaven-worship rites. For its outstanding universal value in architecture and in laying out a capital according to feng shui, the citadel was inscribed by UNESCO as a World Cultural Heritage Site in 2011. Today visitors can pass through the massive stone gate, view displays of archaeological finds and behold living proof of the skill of the Vietnamese of old.",
    "presentation_long_ru": "Цитадель династии Хо (её называют также Тэйдо — «Западная столица») была построена Хо Куй Ли всего за три месяца в 1397 году как новая столица государства Дайнгу вместо Тханглонга. Это одна из очень немногих крупных каменных крепостей, сохранившихся в Юго-Восточной Азии. Исследователей всего мира поражает техника строительства: блоки синего камня весом в десятки тонн обтёсывали до прямоугольной формы и плотно укладывали друг на друга без раствора — и они стоят уже более шести веков, пережив множество потрясений. Почти квадратный вал, каждая сторона которого около 800–900 м, прорезан четырьмя арочными воротами; южные — самые величественные, с тремя сводчатыми проходами. Некогда цитадель окружали ров, внешняя стена и алтарь Намзяо для обрядов поклонения небу. За выдающуюся универсальную ценность в архитектуре и планировке столицы по фэншуй в 2011 году цитадель была внесена ЮНЕСКО в список Всемирного культурного наследия. Сегодня посетители проходят сквозь массивные каменные ворота, осматривают выставку археологических находок и воочию видят живое свидетельство мастерства вьетнамцев прошлого.",
    "highlights_vi": [
      "Tòa thành đá độc nhất Việt Nam, xây năm 1397 (kinh đô nhà Hồ)",
      "Kỹ thuật ghép đá khổng lồ không cần vữa, vững hơn 600 năm",
      "Di sản Văn hóa Thế giới UNESCO (2011)"
    ],
    "highlights_en": [
      "Vietnam's only stone citadel, built in 1397 (Ho dynasty capital)",
      "Colossal mortar-free stone masonry, standing firm for over 600 years",
      "UNESCO World Cultural Heritage Site (2011)"
    ],
    "highlights_ru": [
      "Единственная во Вьетнаме каменная цитадель, построена в 1397 году",
      "Колоссальная кладка без раствора, стоящая уже более 600 лет",
      "Объект Всемирного культурного наследия ЮНЕСКО (2011)"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–17:30 hằng ngày.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 40.000 VND/người.",
      "duration_vi": "Khoảng 1–1,5 giờ.",
      "best_time_vi": "Mùa thu – đông (tháng 9–4) mát mẻ; buổi sáng ít nắng.",
      "tips_vi": "Ít bóng mát, mang mũ và nước; thuê xe điện tham quan các cổng; kết hợp Lam Kinh, suối cá Cẩm Lương."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "UNESCO World Heritage Centre — Citadel of the Ho Dynasty", "url": "https://whc.unesco.org/en/list/1358/"},
      {"title": "Wikipedia (VI) — Thành nhà Hồ", "url": "https://vi.wikipedia.org/wiki/Th%C3%A0nh_nh%C3%A0_H%E1%BB%93"}
    ],
    "tags": ["unesco", "history", "fortress", "monument", "top", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-thanh-hoa-sam-son",
    "slug": "sam-son",
    "region": "vn-thanh-hoa",
    "country": "vietnam",
    "region_name_vi": "Thanh Hóa",
    "federal_district": "Miền Trung",
    "name_vi": "Bãi biển Sầm Sơn",
    "name_ru": "Пляж Шамшон",
    "name_en": "Sam Son Beach",
    "categories": ["other", "park_garden"],
    "coordinates": {"lat": 19.7534, "lon": 105.9080},
    "address_vi": "Thành phố Sầm Sơn, tỉnh Thanh Hóa",
    "rating": {"value": 4.3, "count": 6100, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách thích bãi cát dài thoải, sóng lớn và không khí sôi động, hải sản phong phú. Nhiều người khen hạ tầng du lịch nâng cấp mạnh; một số lưu ý cao điểm hè rất đông và cần hỏi giá dịch vụ trước.",
    "presentation_short_vi": "Bãi biển Sầm Sơn ở Thanh Hóa là một trong những bãi tắm lâu đời và nổi tiếng nhất miền Bắc, được người Pháp khai thác từ đầu thế kỷ 20. Bờ cát dài thoải, sóng lớn cùng cụm danh thắng hòn Trống Mái, đền Độc Cước tạo nên điểm nghỉ mát sôi động.",
    "presentation_short_en": "Sam Son Beach in Thanh Hoa is one of northern Vietnam's oldest and most famous seaside resorts, developed by the French in the early 20th century. Its long gentle sands, lively surf and nearby sights such as the Trong Mai rocks and Doc Cuoc Temple make it a bustling summer getaway.",
    "presentation_short_ru": "Пляж Шамшон в Тханьхоа — один из старейших и самых известных морских курортов севера Вьетнама, освоенный французами в начале XX века. Длинный пологий песок, оживлённый прибой и близлежащие достопримечательности — скалы Чонгмай и храм Докок — делают его шумным местом летнего отдыха.",
    "presentation_long_vi": "Cách thành phố Thanh Hóa khoảng 16 km, Sầm Sơn là bãi biển được người Pháp phát hiện và xây dựng thành nơi nghỉ dưỡng từ năm 1907, nay là một trong những đô thị du lịch biển nhộn nhịp nhất miền Bắc. Bãi biển trải dài nhiều cây số với bờ cát vàng thoải, nước trong và sóng khá lớn, phù hợp cho tắm biển và các trò chơi bãi biển. Bên cạnh biển, Sầm Sơn còn hấp dẫn bởi cụm di tích – danh thắng trên núi Trường Lệ: hòn Trống Mái với hai tảng đá tựa đôi chim tình tứ gắn truyền thuyết tình yêu, đền Độc Cước thờ vị thần 'xẻ đôi thân mình' để vừa cứu dân trên bờ vừa diệt quỷ ngoài biển, cùng đền Cô Tiên và những vọng cảnh nhìn ra vịnh. Những năm gần đây, hạ tầng du lịch được đầu tư mạnh với quảng trường biển, các khu vui chơi, khách sạn và tổ hợp nghỉ dưỡng hiện đại, biến Sầm Sơn thành điểm đến sôi động cả ngày lẫn đêm. Ẩm thực nơi đây phong phú với hải sản tươi, mực một nắng, nước mắm truyền thống. Mùa hè, Sầm Sơn đón hàng triệu lượt khách, mang không khí náo nhiệt, rộn ràng đặc trưng của một thành phố biển.",
    "presentation_long_en": "About 16 km from Thanh Hoa city, Sam Son is a beach the French discovered and turned into a resort as early as 1907, and it is now one of the busiest seaside towns in the north. The shore stretches for several kilometres with gently sloping golden sand, clear water and fairly strong surf, ideal for swimming and beach games. Beyond the sea, Sam Son charms visitors with the cluster of relics on Truong Le Mountain: the Trong Mai (Cock and Hen) rocks, two boulders resembling affectionate birds tied to a love legend; Doc Cuoc Temple, dedicated to a deity who 'split his own body in two' to save people on shore while slaying demons at sea; along with Co Tien Temple and lookouts over the bay. In recent years tourism infrastructure has been heavily upgraded with a seafront square, amusement zones, hotels and modern resort complexes, making Sam Son lively day and night. The cuisine is rich in fresh seafood, sun-dried squid and traditional fish sauce. In summer Sam Son welcomes millions of visitors, radiating the bustling, festive spirit typical of a Vietnamese beach city.",
    "presentation_long_ru": "Примерно в 16 км от города Тханьхоа Шамшон — пляж, который французы открыли и превратили в курорт ещё в 1907 году; сегодня это один из самых оживлённых приморских городов севера. Берег тянется на несколько километров с полого спускающимся золотым песком, прозрачной водой и довольно сильным прибоем — идеально для купания и пляжных игр. Помимо моря, Шамшон привлекает комплексом памятников на горе Чыонгле: скалы Чонгмай («петух и курица») — два валуна, похожие на нежных птиц, связанные с легендой о любви; храм Докок, посвящённый божеству, что «рассекло себя надвое», чтобы спасать людей на берегу и разить демонов в море; а также храм Котьен и смотровые площадки над заливом. В последние годы туристическая инфраструктура сильно обновлена — набережная площадь, парки развлечений, отели и современные курортные комплексы — так что Шамшон оживлён и днём, и ночью. Кухня богата свежими морепродуктами, вяленым кальмаром и традиционным рыбным соусом. Летом Шамшон принимает миллионы гостей, излучая шумный, праздничный дух, свойственный вьетнамскому приморскому городу.",
    "highlights_vi": [
      "Bãi biển nghỉ mát lâu đời (từ 1907), sôi động bậc nhất miền Bắc",
      "Danh thắng núi Trường Lệ: hòn Trống Mái, đền Độc Cước, đền Cô Tiên",
      "Quảng trường biển, khu vui chơi hiện đại và hải sản phong phú"
    ],
    "highlights_en": [
      "A historic seaside resort (since 1907), among the liveliest in the north",
      "Truong Le Mountain sights: Trong Mai rocks, Doc Cuoc and Co Tien temples",
      "A modern seafront square, amusement zones and abundant seafood"
    ],
    "highlights_ru": [
      "Исторический морской курорт (с 1907 года), один из самых оживлённых на севере",
      "Достопримечательности горы Чыонгле: скалы Чонгмай, храмы Докок и Котьен",
      "Современная набережная площадь, парки развлечений и изобилие морепродуктов"
    ],
    "practical": {
      "hours_vi": "Bãi biển mở cả ngày; tắm đẹp buổi sáng sớm và chiều.",
      "ticket_vi": "Miễn phí vào bãi; dịch vụ (ghế, phao, tắm nước ngọt) tính riêng.",
      "duration_vi": "Nửa ngày đến vài ngày nghỉ dưỡng.",
      "best_time_vi": "Mùa hè (tháng 5–8) sôi động; tránh ngày biển động.",
      "tips_vi": "Hỏi giá hải sản/dịch vụ trước khi dùng; chú ý cờ cảnh báo sóng; đặt phòng sớm dịp cao điểm."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Sầm Sơn", "url": "https://vi.wikipedia.org/wiki/S%E1%BA%A7m_S%C6%A1n"}
    ],
    "tags": ["beach", "sea", "family", "summer", "outdoor", "resort"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-thanh-hoa-lam-kinh",
    "slug": "lam-kinh",
    "region": "vn-thanh-hoa",
    "country": "vietnam",
    "region_name_vi": "Thanh Hóa",
    "federal_district": "Miền Trung",
    "name_vi": "Khu di tích lịch sử Lam Kinh",
    "name_ru": "Историко-мемориальный комплекс Ламкинь",
    "name_en": "Lam Kinh Historical Site",
    "categories": ["monument", "park_garden"],
    "coordinates": {"lat": 19.9250, "lon": 105.4083},
    "address_vi": "Xã Xuân Lam, huyện Thọ Xuân, tỉnh Thanh Hóa",
    "rating": {"value": 4.6, "count": 2000, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách yêu thích không gian cổ kính, rừng cây rợp bóng và các lăng mộ, bia đá thời Lê. Nhiều người ấn tượng với 'cây ổi cười' kỳ lạ và không khí linh thiêng, trong lành.",
    "presentation_short_vi": "Lam Kinh ở huyện Thọ Xuân, tỉnh Thanh Hóa là đất phát tích của nhà Hậu Lê và là nơi an nghỉ của vua Lê Thái Tổ (Lê Lợi) cùng nhiều vua, hoàng hậu. Khu di tích quốc gia đặc biệt này lưu giữ điện miếu, lăng mộ và các tấm bia đá vô giá giữa rừng cây cổ thụ.",
    "presentation_short_en": "Lam Kinh in Tho Xuan district, Thanh Hoa province, is the ancestral land of the Later Le dynasty and the resting place of King Le Thai To (Le Loi) and many kings and queens. This special national relic preserves shrines, royal tombs and priceless stone steles amid an ancient forest.",
    "presentation_short_ru": "Ламкинь в уезде Тхосуан провинции Тханьхоа — родовая земля династии Поздние Ле и место упокоения короля Ле Тхай То (Ле Лоя) и многих королей и королев. Этот особый национальный памятник хранит святилища, царские гробницы и бесценные каменные стелы среди древнего леса.",
    "presentation_long_vi": "Lam Kinh (còn gọi là Tây Kinh) là quê hương của người anh hùng dân tộc Lê Lợi, nơi ông dấy binh khởi nghĩa Lam Sơn đánh đuổi quân Minh đầu thế kỷ 15. Sau khi lên ngôi và lập nên nhà Hậu Lê, các vua Lê đã cho xây dựng nơi đây thành khu điện miếu và lăng tẩm bề thế để thờ cúng tổ tiên và an táng hoàng gia. Trải rộng trên vùng đồi thấp bên sông Chu, khu di tích gồm chính điện Lam Kinh (Quang Đức, Sùng Hiếu, Diên Khánh) được phục dựng bằng gỗ lim đồ sộ, hệ thống lăng mộ các vua như Vĩnh Lăng (Lê Thái Tổ), Hựu Lăng, cùng những tấm bia đá cổ. Nổi bật là bia Vĩnh Lăng do danh nhân Nguyễn Trãi soạn, một áng văn – sử liệu quý giá. Bao trùm khu di tích là rừng cây cổ thụ hàng trăm năm tuổi rợp bóng mát, tạo nên không gian trầm mặc, linh thiêng. Du khách còn thích thú với 'cây ổi cười' kỳ lạ tương truyền rung lá khi được vuốt nhẹ. Được xếp hạng Di tích Quốc gia đặc biệt, Lam Kinh là điểm về nguồn giàu giá trị lịch sử, kiến trúc và tâm linh của xứ Thanh.",
    "presentation_long_en": "Lam Kinh (also called Tay Kinh, the 'Western Capital') is the homeland of the national hero Le Loi, where he raised the Lam Son uprising to drive out the Ming army in the early 15th century. After taking the throne and founding the Later Le dynasty, the Le kings developed the site into a grand complex of shrines and royal tombs to worship their ancestors and bury the royal family. Spread over low hills beside the Chu River, the relic includes the reconstructed Lam Kinh main halls (Quang Duc, Sung Hieu, Dien Khanh) in massive ironwood, the tombs of kings such as Vinh Lang (Le Thai To) and Huu Lang, and ancient stone steles. Foremost among them is the Vinh Lang stele, composed by the great scholar Nguyen Trai — a precious work of literature and history. The whole site is shaded by centuries-old forest, lending a solemn, sacred atmosphere. Visitors are also intrigued by the curious 'laughing guava tree', said to quiver its leaves when gently stroked. Ranked a Special National Relic, Lam Kinh is a rewarding pilgrimage rich in the history, architecture and spirituality of the Thanh land.",
    "presentation_long_ru": "Ламкинь (называемый также Тэйкинь — «Западная столица») — родина национального героя Ле Лоя, где он поднял восстание Лamшон и в начале XV века изгнал минскую армию. Взойдя на престол и основав династию Поздние Ле, короли Ле превратили это место в величественный комплекс святилищ и царских усыпальниц для поклонения предкам и погребения королевской семьи. Раскинувшись на невысоких холмах у реки Чу, памятник включает восстановленные главные залы Ламкиня (Куангдык, Шунгхьеу, Зьенкхань) из массивного железного дерева, гробницы королей — Виньланг (Ле Тхай То), Хыуланг — и древние каменные стелы. Первая среди них — стела Виньланг, составленная великим учёным Нгуен Чаем, — драгоценное литературное и историческое произведение. Весь комплекс укрыт тенью многовекового леса, придающего ему торжественную, священную атмосферу. Посетителей интригует и удивительное «смеющееся дерево гуавы», которое, по преданию, дрожит листвой, если его тихонько погладить. Признанный особым национальным памятником, Ламкинь — благодатное место паломничества, богатое историей, архитектурой и духовностью земли Тхань. Ежегодный праздник Ламкинь в память о Ле Лое собирает множество паломников с торжественными обрядами и народными играми, а тенистый вековой лес делает прогулку приятной даже в летнюю жару.",
    "highlights_vi": [
      "Đất phát tích nhà Hậu Lê, nơi an nghỉ của Lê Lợi và các vua Lê",
      "Chính điện gỗ lim phục dựng, lăng mộ và bia Vĩnh Lăng (Nguyễn Trãi soạn)",
      "Di tích Quốc gia đặc biệt giữa rừng cổ thụ; có 'cây ổi cười' kỳ lạ"
    ],
    "highlights_en": [
      "Ancestral land of the Later Le dynasty; tombs of Le Loi and the Le kings",
      "Reconstructed ironwood halls, royal tombs and the Vinh Lang stele (by Nguyen Trai)",
      "A Special National Relic in ancient forest, with the curious 'laughing guava tree'"
    ],
    "highlights_ru": [
      "Родовая земля династии Поздние Ле; гробницы Ле Лоя и королей Ле",
      "Восстановленные залы из железного дерева, царские гробницы и стела Виньланг (Нгуен Чай)",
      "Особый национальный памятник в древнем лесу со «смеющимся деревом гуавы»"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 30.000 VND/người.",
      "duration_vi": "Khoảng 1,5–2 giờ.",
      "best_time_vi": "Mát mẻ quanh năm nhờ rừng cây; lễ hội Lam Kinh khoảng 22/8 âm lịch.",
      "tips_vi": "Đi giày thoải mái để dạo rừng; giữ trang nghiêm ở lăng mộ; kết hợp Thành nhà Hồ."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Lam Kinh", "url": "https://vi.wikipedia.org/wiki/Lam_Kinh"}
    ],
    "tags": ["history", "monument", "temple", "nature", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-thanh-hoa-pu-luong",
    "slug": "pu-luong",
    "region": "vn-thanh-hoa",
    "country": "vietnam",
    "region_name_vi": "Thanh Hóa",
    "federal_district": "Miền Trung",
    "name_vi": "Khu bảo tồn thiên nhiên Pù Luông",
    "name_ru": "Природный заповедник Пулуонг",
    "name_en": "Pu Luong Nature Reserve",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 20.4833, "lon": 105.1500},
    "address_vi": "Huyện Bá Thước và Quan Hóa, tỉnh Thanh Hóa",
    "rating": {"value": 4.7, "count": 3300, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách say mê ruộng bậc thang xanh vàng, guồng nước, bản làng người Thái và các khu nghỉ hòa mình vào thiên nhiên. Nhiều người khen yên tĩnh, trong lành, hợp trekking; một số nhắc đường núi quanh co.",
    "presentation_short_vi": "Pù Luông ở tỉnh Thanh Hóa là khu bảo tồn thiên nhiên với rừng nguyên sinh, ruộng bậc thang và bản làng người Thái, Mường bình yên. Được ví như 'thiên đường xanh' của xứ Thanh, nơi đây hấp dẫn du khách ưa trekking, nghỉ dưỡng sinh thái và 'sống chậm'.",
    "presentation_short_en": "Pu Luong in Thanh Hoa province is a nature reserve of primeval forest, terraced rice fields and tranquil Thai and Muong villages. Hailed as a 'green paradise' of the Thanh land, it draws travellers who love trekking, eco-retreats and slow living.",
    "presentation_short_ru": "Пулуонг в провинции Тханьхоа — природный заповедник с девственным лесом, террасными рисовыми полями и тихими деревнями тай и мыонг. Прозванный «зелёным раем» земли Тхань, он привлекает любителей трекинга, экоотдыха и «медленной жизни».",
    "presentation_long_vi": "Nằm ở phía tây bắc tỉnh Thanh Hóa, trên hai huyện Bá Thước và Quan Hóa, Khu bảo tồn thiên nhiên Pù Luông rộng hơn 17.600 ha, bảo vệ hệ sinh thái rừng nhiệt đới trên núi đá vôi với đa dạng sinh học phong phú. 'Pù Luông' trong tiếng Thái nghĩa là đỉnh núi cao nhất vùng. Điều làm nên sức hút của Pù Luông là sự hòa quyện tuyệt đẹp giữa thiên nhiên hoang sơ và cảnh quan nông nghiệp: những thửa ruộng bậc thang uốn lượn theo sườn đồi, chuyển từ xanh non sang vàng óng theo mùa lúa, xen giữa là các bản làng nhà sàn của người Thái, người Mường, những chiếc guồng nước quay đều bên suối và rừng luồng bạt ngàn. Du khách đến đây để trekking xuyên rừng và bản, ngắm ruộng bậc thang từ trên cao, tắm suối, đạp xe qua các bản Đôn, Kho Mường, Hiêu, hay đơn giản là nghỉ tại những khu resort sinh thái với bể bơi vô cực nhìn ra thung lũng. Ẩm thực địa phương mộc mạc với cơm lam, vịt Cổ Lũng, cá suối, rau rừng. Khí hậu mát mẻ quanh năm cùng nhịp sống chậm rãi khiến Pù Luông trở thành điểm đến lý tưởng để tái tạo năng lượng, ngày càng được cả du khách trong nước và quốc tế yêu thích.",
    "presentation_long_en": "In the north-west of Thanh Hoa province, across Ba Thuoc and Quan Hoa districts, the Pu Luong Nature Reserve covers more than 17,600 hectares, protecting a tropical forest ecosystem on limestone mountains with rich biodiversity. 'Pu Luong' in the Thai language means the highest peak of the area. Its appeal lies in the beautiful blend of wild nature and farming landscape: terraced rice fields curving along the slopes, shifting from tender green to golden with the harvest, dotted with stilt-house villages of the Thai and Muong, water wheels turning by the streams and endless groves of bamboo. Visitors come to trek through forest and hamlets, admire the terraces from above, bathe in streams, cycle through the villages of Don, Kho Muong and Hieu, or simply relax at eco-resorts with infinity pools overlooking the valley. Local fare is rustic — bamboo-tube rice, Co Lung duck, stream fish and wild greens. A cool climate all year and an unhurried pace make Pu Luong an ideal place to recharge, increasingly loved by domestic and international travellers alike.",
    "presentation_long_ru": "На северо-западе провинции Тханьхоа, в уездах Батхыок и Куанхоа, природный заповедник Пулуонг занимает более 17 600 гектаров, оберегая экосистему тропического леса на известняковых горах с богатым биоразнообразием. «Пулуонг» на языке тай означает высочайшую вершину края. Его очарование — в прекрасном сочетании дикой природы и земледельческого ландшафта: террасные рисовые поля, изгибающиеся по склонам и меняющие цвет от нежно-зелёного до золотого к урожаю, деревни свайных домов тай и мыонг, водяные колёса, вращающиеся у ручьёв, и бескрайние бамбуковые рощи. Сюда приезжают, чтобы совершать треккинг сквозь лес и деревни, любоваться террасами сверху, купаться в ручьях, кататься на велосипеде по деревням Дон, Кхомыонг и Хьеу или просто отдыхать в экокурортах с бассейнами-инфинити над долиной. Местная кухня простая — рис в бамбуке, утка Колунг, речная рыба и дикие травы. Прохладный климат круглый год и неспешный ритм делают Пулуонг идеальным местом, чтобы восстановить силы; его всё больше любят и вьетнамские, и иностранные путешественники. Лучшее время для поездки — периоды созревания риса, когда террасы становятся золотыми; заранее забронированный хоумстей и местный проводник сделают путешествие удобным, а прохладный горный воздух — приятным даже в разгар лета.",
    "highlights_vi": [
      "Rừng nguyên sinh trên núi đá vôi, đa dạng sinh học phong phú (>17.600 ha)",
      "Ruộng bậc thang, guồng nước và bản nhà sàn người Thái, Mường",
      "Thiên đường trekking và nghỉ dưỡng sinh thái, khí hậu mát quanh năm"
    ],
    "highlights_en": [
      "Primeval forest on limestone mountains with rich biodiversity (>17,600 ha)",
      "Terraced fields, water wheels and Thai/Muong stilt-house villages",
      "A paradise for trekking and eco-retreats, cool all year round"
    ],
    "highlights_ru": [
      "Девственный лес на известняковых горах с богатым биоразнообразием (>17 600 га)",
      "Террасные поля, водяные колёса и свайные деревни тай/мыонг",
      "Рай для трекинга и экоотдыха, прохладный круглый год"
    ],
    "practical": {
      "hours_vi": "Khu vực mở quanh năm (du lịch cộng đồng, không có cổng vé chung).",
      "ticket_vi": "Không thu vé chung; chi phí tùy homestay/resort và tour trekking.",
      "duration_vi": "2–3 ngày để trải nghiệm trọn vẹn.",
      "best_time_vi": "Mùa lúa: khoảng cuối tháng 5–6 và tháng 9–10 (ruộng bậc thang đẹp nhất).",
      "tips_vi": "Đặt homestay/resort trước; đi giày trekking; thuê người dẫn đường bản địa; mang áo khoác mỏng."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Khu bảo tồn thiên nhiên Pù Luông", "url": "https://vi.wikipedia.org/wiki/Khu_b%E1%BA%A3o_t%E1%BB%93n_thi%C3%AAn_nhi%C3%AAn_P%C3%B9_Lu%C3%B4ng"}
    ],
    "tags": ["nature", "trekking", "terraces", "ecotourism", "viewpoint", "outdoor", "top"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-thanh-hoa-suoi-ca-cam-luong",
    "slug": "suoi-ca-cam-luong",
    "region": "vn-thanh-hoa",
    "country": "vietnam",
    "region_name_vi": "Thanh Hóa",
    "federal_district": "Miền Trung",
    "name_vi": "Suối cá thần Cẩm Lương",
    "name_ru": "Священный рыбный ручей Камлыонг",
    "name_en": "Cam Luong Divine Fish Stream",
    "categories": ["other", "park_garden"],
    "coordinates": {"lat": 20.2350, "lon": 105.4083},
    "address_vi": "Xã Cẩm Lương, huyện Cẩm Thủy, tỉnh Thanh Hóa",
    "rating": {"value": 4.3, "count": 1300, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách thích thú khi thấy hàng nghìn con cá lớn tập trung dày đặc nơi cửa hang, dạn dĩ với người. Nhiều người thấy độc đáo, hợp đi cùng gia đình; một số nhắc quãng đường xa và nên kết hợp điểm khác.",
    "presentation_short_vi": "Suối cá thần Cẩm Lương ở huyện Cẩm Thủy, tỉnh Thanh Hóa nổi tiếng với hàng nghìn con cá lớn sống quần tụ nơi cửa hang núi đá. Người dân địa phương coi đàn cá là 'cá thần' linh thiêng, không bao giờ đánh bắt, tạo nên hiện tượng thiên nhiên kỳ thú.",
    "presentation_short_en": "The Cam Luong Divine Fish Stream in Cam Thuy district, Thanh Hoa, is famed for the thousands of large fish that gather at the mouth of a limestone cave. Locals revere them as sacred 'divine fish' and never catch them, creating a fascinating natural phenomenon.",
    "presentation_short_ru": "Священный рыбный ручей Камлыонг в уезде Камтхюи провинции Тханьхоа знаменит тысячами крупных рыб, что собираются у входа в известняковую пещеру. Местные жители почитают их как священную «божественную рыбу» и никогда не ловят — рождается удивительное природное явление.",
    "presentation_long_vi": "Nằm dưới chân núi Trường Sinh, bên bờ sông Mã thuộc xã Cẩm Lương, huyện Cẩm Thủy, Suối cá thần là một trong những hiện tượng thiên nhiên độc đáo và bí ẩn bậc nhất Việt Nam. Dòng suối nhỏ chảy ra từ một hang động trong lòng núi đá vôi, nơi quần tụ hàng nghìn con cá to, có con nặng vài kilôgam, thuộc loài cá dốc (một dạng cá trong họ cá chép) với thân xanh, vây và môi ánh hồng. Điều kỳ lạ là đàn cá dày đặc chen chúc nơi cửa hang nhưng nước suối vẫn trong vắt, không hề tanh; cá rất dạn người, có thể chạm nhẹ mà không bơi đi. Đồng bào Mường nơi đây từ bao đời tin rằng đàn cá là 'cá thần' bảo vệ bản làng, mang lại bình an và mùa màng tốt tươi, nên tuyệt đối không ai đánh bắt hay ăn thịt. Chính niềm tin tâm linh cùng sự bảo vệ nghiêm ngặt đã giúp đàn cá sinh sôi và tồn tại qua nhiều thế hệ. Du khách đến đây vừa chiêm ngưỡng cảnh tượng kỳ thú, vừa tìm hiểu văn hóa, tín ngưỡng độc đáo của người Mường, thường kết hợp tham quan hang động và các bản làng, ruộng đồng yên bình xung quanh.",
    "presentation_long_en": "At the foot of Truong Sinh Mountain, on the bank of the Ma River in Cam Luong commune, Cam Thuy district, the Divine Fish Stream is one of Vietnam's most unusual and mysterious natural phenomena. A small stream flows out of a cave within the limestone mountain, where thousands of large fish gather — some weighing several kilograms — of the 'ca doc' species (a member of the carp family), with green bodies and pinkish fins and lips. Remarkably, though the fish crowd densely at the cave mouth, the water stays crystal-clear and free of any fishy smell; the fish are so tame they can be gently touched without swimming away. For generations the local Muong people have believed the fish are 'divine fish' that protect their village, bringing peace and good harvests, so no one ever catches or eats them. This spiritual belief and strict protection have allowed the shoal to thrive across many generations. Visitors come to marvel at the spectacle and to learn the distinctive culture and beliefs of the Muong, usually combining a look into the cave with the peaceful villages and fields nearby.",
    "presentation_long_ru": "У подножия горы Чыонгшинь, на берегу реки Ма в общине Камлыонг уезда Камтхюи, Священный рыбный ручей — одно из самых необычных и загадочных природных явлений Вьетнама. Небольшой ручей вытекает из пещеры в известняковой горе, где собираются тысячи крупных рыб — иные весом в несколько килограммов — вида «ка док» (из семейства карповых), с зеленоватым телом и розоватыми плавниками и губами. Удивительно, что, хотя рыбы плотно теснятся у входа в пещеру, вода остаётся кристально чистой и без рыбного запаха; рыбы столь ручные, что их можно осторожно погладить, и они не уплывают. Поколениями местные мыонг верят, что это «божественная рыба», оберегающая деревню, приносящая мир и добрый урожай, поэтому её никто не ловит и не ест. Именно эта духовная вера и строгая охрана позволили стае процветать многие поколения. Гости приезжают подивиться зрелищу и познакомиться с самобытной культурой и верованиями мыонг, обычно совмещая осмотр пещеры с окрестными тихими деревнями и полями. Через ручей перекинут подвесной мост, а в соседней деревне мыонг можно отведать местную кухню, поэтому визит часто объединяют с цитаделью династии Хо и заповедником Пулуонг в одном маршруте по горной части Тханьхоа.",
    "highlights_vi": [
      "Hàng nghìn con cá lớn quần tụ nơi cửa hang, nước vẫn trong vắt",
      "Người Mường coi là 'cá thần', không bao giờ đánh bắt — tín ngưỡng độc đáo",
      "Hiện tượng thiên nhiên kỳ thú, hợp trải nghiệm cùng gia đình"
    ],
    "highlights_en": [
      "Thousands of large fish crowd the cave mouth, yet the water stays crystal-clear",
      "Revered by the Muong as 'divine fish' and never caught — a unique belief",
      "A fascinating natural phenomenon, great for a family visit"
    ],
    "highlights_ru": [
      "Тысячи крупных рыб теснятся у входа в пещеру, а вода остаётся прозрачной",
      "Мыонг чтят их как «божественную рыбу» и никогда не ловят — уникальное поверье",
      "Удивительное природное явление, отлично для семейного визита"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–18:00 hằng ngày.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 20.000 VND/người.",
      "duration_vi": "Khoảng 1 giờ.",
      "best_time_vi": "Mùa khô (tháng 10–4); tránh ngày mưa lũ nước đục.",
      "tips_vi": "Không cho cá ăn đồ lạ; giữ vệ sinh suối; kết hợp Thành nhà Hồ, Pù Luông trong tuyến miền núi Thanh Hóa."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Suối Cá thần", "url": "https://vi.wikipedia.org/wiki/Su%E1%BB%91i_C%C3%A1_th%E1%BA%A7n"}
    ],
    "tags": ["nature", "unique", "family", "culture", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
]

# ===================== NGHỆ AN (Miền Trung) =====================
PLACES += [
  {
    "id": "vn-nghe-an-kim-lien",
    "slug": "kim-lien",
    "region": "vn-nghe-an",
    "country": "vietnam",
    "region_name_vi": "Nghệ An",
    "federal_district": "Miền Trung",
    "name_vi": "Khu di tích Kim Liên (quê Bác Hồ)",
    "name_ru": "Мемориальный комплекс Кимльен (родина Хо Ши Мина)",
    "name_en": "Kim Lien Relic Site (Ho Chi Minh's Birthplace)",
    "categories": ["monument", "museum"],
    "coordinates": {"lat": 18.6786, "lon": 105.5036},
    "address_vi": "Xã Kim Liên, huyện Nam Đàn, tỉnh Nghệ An",
    "rating": {"value": 4.7, "count": 6800, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách xúc động khi thăm ngôi nhà tranh đơn sơ nơi Bác Hồ sinh ra và lớn lên, giữa làng quê thanh bình. Nhiều người khen không gian giản dị, thiêng liêng, thuyết minh truyền cảm.",
    "presentation_short_vi": "Khu di tích Kim Liên ở huyện Nam Đàn, tỉnh Nghệ An là quê hương của Chủ tịch Hồ Chí Minh, gồm làng Sen (quê nội) và Hoàng Trù (quê ngoại). Những ngôi nhà tranh mộc mạc nơi Người sinh ra và sống thời niên thiếu là 'địa chỉ đỏ' thiêng liêng bậc nhất Việt Nam.",
    "presentation_short_en": "The Kim Lien relic site in Nam Dan district, Nghe An province, is the homeland of President Ho Chi Minh, comprising Sen village (his father's home) and Hoang Tru (his mother's home). The simple thatched houses where he was born and spent his youth are among Vietnam's most revered memorials.",
    "presentation_short_ru": "Мемориальный комплекс Кимльен в уезде Намдан провинции Нгеан — родина президента Хо Ши Мина; он включает деревню Сен (дом отца) и Хоангчу (дом матери). Скромные тростниковые дома, где он родился и провёл юность, — одни из самых почитаемых мемориалов Вьетнама.",
    "presentation_long_vi": "Cách thành phố Vinh khoảng 15 km, Khu di tích Kim Liên gắn liền với tuổi thơ của Chủ tịch Hồ Chí Minh – vị lãnh tụ kính yêu của dân tộc Việt Nam. Quần thể gồm hai cụm chính: làng Hoàng Trù, quê ngoại, nơi cậu bé Nguyễn Sinh Cung (tên thuở nhỏ của Bác) chào đời năm 1890 trong ngôi nhà tranh nhỏ của ông bà ngoại; và làng Sen (Kim Liên), quê nội, nơi Người sống những năm niên thiếu cùng gia đình cụ Phó bảng Nguyễn Sinh Sắc. Đến đây, du khách được đi giữa khung cảnh làng quê Việt Nam đặc trưng với lũy tre, ao sen, giếng Cốc, cây đa, con đường đất, và tận mắt thấy những ngôi nhà tranh vách nứa đơn sơ cùng các kỷ vật giản dị: khung cửi, chõng tre, bộ phản gỗ, án thư. Chính không gian mộc mạc, thanh bình ấy đã nuôi dưỡng tâm hồn và hun đúc ý chí của người thanh niên yêu nước sau này ra đi tìm đường cứu nước. Khu di tích còn có nhà tưởng niệm, khu mộ bà Hoàng Thị Loan (thân mẫu của Bác) trên núi Động Tranh. Là Di tích Quốc gia đặc biệt, Kim Liên mỗi năm đón hàng triệu lượt người về nguồn, tri ân và tìm hiểu về cuộc đời vị lãnh tụ.",
    "presentation_long_en": "About 15 km from Vinh city, the Kim Lien relic site is tied to the childhood of President Ho Chi Minh, the beloved leader of the Vietnamese nation. The complex has two main clusters: Hoang Tru village, his mother's home, where the boy Nguyen Sinh Cung (Ho Chi Minh's childhood name) was born in 1890 in his maternal grandparents' small thatched house; and Sen village (Kim Lien), his father's home, where he spent his youth with the family of the scholar Nguyen Sinh Sac. Here visitors walk through a quintessential Vietnamese village landscape of bamboo hedges, lotus ponds, the Coc well, banyan trees and earthen lanes, and see the humble thatched-and-wattle houses with their simple keepsakes: a loom, a bamboo cot, a wooden plank bed, a writing desk. It was this rustic, peaceful setting that nurtured the spirit and forged the will of the young patriot who would later leave to seek a path to save his country. The site also has a memorial house and the tomb of Hoang Thi Loan (his mother) on Dong Tranh Mountain. A Special National Relic, Kim Lien welcomes millions of pilgrims each year who come to pay tribute and learn about the leader's life.",
    "presentation_long_ru": "Примерно в 15 км от города Винь мемориал Кимльен связан с детством президента Хо Ши Мина — любимого вождя вьетнамского народа. Комплекс состоит из двух главных частей: деревни Хоангчу, дома матери, где мальчик Нгуен Шинь Кунг (детское имя Хо Ши Мина) родился в 1890 году в маленьком тростниковом доме бабушки и дедушки по материнской линии; и деревни Сен (Кимльен), дома отца, где он провёл юность в семье учёного Нгуен Шинь Шака. Здесь посетители проходят сквозь типичный вьетнамский деревенский пейзаж с бамбуковыми изгородями, лотосовыми прудами, колодцем Кок, баньянами и грунтовыми тропами и видят скромные дома из тростника и плетня с простыми реликвиями: ткацкий станок, бамбуковую лежанку, деревянный настил-кровать, письменный столик. Именно эта простая, мирная обстановка взрастила душу и закалила волю юного патриота, который позднее отправится искать путь спасения родины. В комплексе также есть мемориальный дом и гробница Хоанг Тхи Лоан (его матери) на горе Донгчань. Как особый национальный памятник Кимльен ежегодно принимает миллионы паломников, приезжающих отдать дань уважения и узнать о жизни вождя.",
    "highlights_vi": [
      "Quê hương Chủ tịch Hồ Chí Minh: làng Sen (nội) và Hoàng Trù (ngoại)",
      "Nhà tranh vách nứa nơi Bác sinh ra (1890) và sống thời niên thiếu",
      "Di tích Quốc gia đặc biệt; có mộ bà Hoàng Thị Loan trên núi Động Tranh"
    ],
    "highlights_en": [
      "Homeland of Ho Chi Minh: Sen village (paternal) and Hoang Tru (maternal)",
      "The thatched houses where he was born (1890) and spent his youth",
      "A Special National Relic; the tomb of his mother on Dong Tranh Mountain"
    ],
    "highlights_ru": [
      "Родина Хо Ши Мина: деревня Сен (отца) и Хоангчу (матери)",
      "Тростниковые дома, где он родился (1890) и провёл юность",
      "Особый национальный памятник; гробница его матери на горе Донгчань"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
      "ticket_vi": "Miễn phí tham quan (có thể có phí gửi xe/hướng dẫn).",
      "duration_vi": "Khoảng 2 giờ (cả làng Sen và Hoàng Trù).",
      "best_time_vi": "Mùa sen nở (khoảng tháng 5–6) làng quê đẹp nhất; dịp sinh nhật Bác 19/5 đông khách.",
      "tips_vi": "Ăn mặc lịch sự, giữ trang nghiêm; nên thuê thuyết minh; kết hợp thăm thành phố Vinh và biển Cửa Lò."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Khu di tích Kim Liên", "url": "https://vi.wikipedia.org/wiki/Khu_di_t%C3%ADch_Kim_Li%C3%AAn"}
    ],
    "tags": ["history", "monument", "memorial", "culture", "top", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-nghe-an-cua-lo",
    "slug": "cua-lo",
    "region": "vn-nghe-an",
    "country": "vietnam",
    "region_name_vi": "Nghệ An",
    "federal_district": "Miền Trung",
    "name_vi": "Bãi biển Cửa Lò",
    "name_ru": "Пляж Кыало",
    "name_en": "Cua Lo Beach",
    "categories": ["other", "park_garden"],
    "coordinates": {"lat": 18.8060, "lon": 105.7170},
    "address_vi": "Phường Cửa Lò, thành phố Vinh, tỉnh Nghệ An",
    "rating": {"value": 4.4, "count": 4200, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách khen bãi cát mịn, nước trong, sóng vừa phải và hải sản tươi ngon, giá hợp lý. Nhiều người thích không khí sôi động mùa hè; một số nhắc cao điểm khá đông và nên đặt phòng sớm.",
    "presentation_short_vi": "Bãi biển Cửa Lò ở tỉnh Nghệ An là một trong những bãi tắm đẹp và nổi tiếng nhất Bắc Trung Bộ, với bờ cát trắng mịn dài hàng cây số và nước biển trong xanh. Gần thành phố Vinh và quê Bác, Cửa Lò là điểm nghỉ mát, thưởng thức hải sản lý tưởng vào mùa hè.",
    "presentation_short_en": "Cua Lo Beach in Nghe An province is one of the loveliest and most famous beaches of the North Central Coast, with kilometres of fine white sand and clear blue water. Close to Vinh city and Ho Chi Minh's homeland, it is an ideal summer resort for relaxing and enjoying seafood.",
    "presentation_short_ru": "Пляж Кыало в провинции Нгеан — один из красивейших и известнейших пляжей Северо-Центрального побережья, с километрами мелкого белого песка и прозрачной синей водой. Рядом с городом Винь и родиной Хо Ши Мина Кыало — идеальный летний курорт для отдыха и морепродуктов.",
    "presentation_long_vi": "Cách thành phố Vinh khoảng 16 km về phía đông, Cửa Lò là thị xã biển được yêu thích bậc nhất khu vực Bắc Trung Bộ, phát triển du lịch từ thời Pháp thuộc. Bãi biển ở đây trải dài khoảng 10 km với bờ cát trắng mịn, thoai thoải, nước trong xanh và sóng êm hơn nhiều bãi biển lân cận, rất an toàn cho tắm biển. Dọc bờ là hàng phi lao xanh mát và tuyến đường ven biển hiện đại với quảng trường, công viên, khách sạn san sát. Ngoài tắm biển, du khách có thể đi thuyền ra đảo Lan Châu nhô ra sát bờ, hay đảo Ngư (Song Ngư) với chùa cổ và giếng nước ngọt giữa biển, ngắm bình minh trên biển và thưởng thức hải sản tươi rói: mực nhảy, ghẹ, tôm, cá thu. Cửa Lò nổi tiếng với mực một nắng và các món chế biến từ hải sản vừa tươi vừa hợp túi tiền. Nhờ vị trí gần Khu di tích Kim Liên – quê Bác và thành phố Vinh, Cửa Lò thường là điểm dừng nghỉ dưỡng kết hợp hành trình về nguồn. Vào mùa hè, thị xã sôi động, đông vui với dòng khách từ khắp miền Bắc và miền Trung đổ về.",
    "presentation_long_en": "About 16 km east of Vinh city, Cua Lo is among the best-loved beach towns of the North Central Coast, developed for tourism since the French colonial era. Its beach runs some 10 km with fine, gently sloping white sand, clear blue water and gentler surf than many neighbouring shores, making it very safe for swimming. Along the front stand cool casuarina rows and a modern coastal boulevard lined with squares, parks and hotels. Beyond swimming, visitors can boat out to Lan Chau Island jutting close to shore, or Ngu (Song Ngu) Island with its ancient pagoda and a freshwater well amid the sea, watch the sunrise over the water and enjoy just-caught seafood: 'jumping' squid, crab, prawns and mackerel. Cua Lo is famous for sun-dried squid and seafood dishes that are both fresh and affordable. Thanks to its closeness to the Kim Lien relic site — Ho Chi Minh's homeland — and to Vinh city, Cua Lo is often a relaxing stop combined with a pilgrimage. In summer the town buzzes with visitors pouring in from across the north and centre of the country.",
    "presentation_long_ru": "Примерно в 16 км к востоку от города Винь Кыало — один из самых любимых приморских городков Северо-Центрального побережья, развивавшийся как курорт ещё со времён французского колониального периода. Пляж тянется около 10 км с мелким, полого спускающимся белым песком, прозрачной синей водой и более спокойным прибоем, чем у многих соседних берегов, что делает купание очень безопасным. Вдоль набережной — прохладные ряды казуарин и современный приморский бульвар с площадями, парками и отелями. Помимо купания, можно доплыть на лодке до острова Ланьтяу у самого берега или до острова Нгы (Шонгнгы) со старинной пагодой и пресным колодцем посреди моря, встретить рассвет над водой и отведать только что выловленные морепродукты: «прыгающего» кальмара, крабов, креветок и скумбрию. Кыало славится вяленым кальмаром и блюдами из морепродуктов — свежими и недорогими. Благодаря близости к мемориалу Кимльен — родине Хо Ши Мина — и к городу Винь Кыало часто становится местом отдыха, совмещённого с паломничеством. Летом городок бурлит от гостей, съезжающихся со всего севера и центра страны.",
    "highlights_vi": [
      "Bãi cát trắng mịn dài ~10 km, sóng êm, an toàn cho tắm biển",
      "Đảo Lan Châu, đảo Ngư và hải sản tươi (mực nhảy, mực một nắng)",
      "Gần thành phố Vinh và quê Bác — hợp tuyến nghỉ dưỡng kết hợp về nguồn"
    ],
    "highlights_en": [
      "About 10 km of fine white sand, gentle surf and safe swimming",
      "Lan Chau and Ngu islands and fresh seafood ('jumping' and sun-dried squid)",
      "Near Vinh city and Ho Chi Minh's homeland — pairs beach and pilgrimage"
    ],
    "highlights_ru": [
      "Около 10 км мелкого белого песка, спокойный прибой и безопасное купание",
      "Острова Ланьтяу и Нгы, свежие морепродукты («прыгающий» и вяленый кальмар)",
      "Рядом с городом Винь и родиной Хо Ши Мина — пляж плюс паломничество"
    ],
    "practical": {
      "hours_vi": "Bãi biển mở cả ngày; tắm đẹp sáng sớm và chiều.",
      "ticket_vi": "Miễn phí vào bãi; dịch vụ bãi biển tính riêng.",
      "duration_vi": "Nửa ngày đến vài ngày nghỉ dưỡng.",
      "best_time_vi": "Mùa hè (tháng 4–8); ngắm bình minh trên biển rất đẹp.",
      "tips_vi": "Thử mực nhảy tại chỗ; hỏi giá trước; đặt phòng sớm dịp cao điểm; kết hợp quê Bác."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Cửa Lò", "url": "https://vi.wikipedia.org/wiki/C%E1%BB%ADa_L%C3%B2"}
    ],
    "tags": ["beach", "sea", "seafood", "family", "summer", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
]

# ===================== HẢI PHÒNG (Miền Bắc) =====================
PLACES += [
  {
    "id": "vn-hai-phong-cat-ba",
    "slug": "cat-ba",
    "region": "vn-hai-phong",
    "country": "vietnam",
    "region_name_vi": "Hải Phòng",
    "federal_district": "Miền Bắc",
    "name_vi": "Quần đảo Cát Bà",
    "name_ru": "Архипелаг Катба",
    "name_en": "Cat Ba Archipelago",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 20.7280, "lon": 107.0480},
    "address_vi": "Đặc khu Cát Hải (đảo Cát Bà), thành phố Hải Phòng",
    "rating": {"value": 4.6, "count": 12000, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách mê cảnh biển đảo hoang sơ, vịnh Lan Hạ xanh ngọc, rừng quốc gia và các bãi tắm nhỏ xinh. Nhiều người thích chèo kayak, leo núi; một số nhắc cuối tuần hè đông và nên đi phà/cáp treo sớm.",
    "presentation_short_vi": "Quần đảo Cát Bà thuộc thành phố Hải Phòng gồm hơn 360 hòn đảo lớn nhỏ, là hòn đảo lớn nhất vịnh Bắc Bộ. Với Vườn quốc gia Cát Bà, vịnh Lan Hạ tuyệt đẹp và hệ sinh thái đa dạng, năm 2023 nơi đây cùng vịnh Hạ Long được UNESCO ghi danh Di sản Thế giới.",
    "presentation_short_en": "The Cat Ba Archipelago, part of Hai Phong city, comprises over 360 islands and holds the largest island in the Gulf of Tonkin. With Cat Ba National Park, the stunning Lan Ha Bay and rich ecosystems, in 2023 it was inscribed alongside Ha Long Bay as a UNESCO World Heritage Site.",
    "presentation_short_ru": "Архипелаг Катба, часть города Хайфон, насчитывает более 360 островов и включает крупнейший остров залива Бакбо (Тонкинского). С национальным парком Катба, изумительным заливом Ланьха и богатыми экосистемами он в 2023 году был внесён вместе с бухтой Халонг в список Всемирного наследия ЮНЕСКО.",
    "presentation_long_vi": "Nằm ở phía đông nam thành phố Hải Phòng, Quần đảo Cát Bà gồm hơn 360 đảo đá vôi lớn nhỏ, trong đó đảo Cát Bà là đảo lớn nhất và đông dân nhất vùng vịnh Bắc Bộ. Đây là viên ngọc thiên nhiên hội tụ đủ rừng, biển và núi đá: Vườn quốc gia Cát Bà rộng lớn bảo tồn rừng nguyên sinh cùng loài voọc Cát Bà (voọc đầu trắng) cực kỳ quý hiếm chỉ còn ở đây; vịnh Lan Hạ với hàng trăm đảo đá nhô lên từ làn nước xanh ngọc, xen giữa là những bãi tắm cát trắng nhỏ xinh và làng chài nổi. Du khách đến Cát Bà để tắm biển ở các bãi Cát Cò, chèo kayak khám phá hang động và áng nước giữa vịnh Lan Hạ, leo núi trong vườn quốc gia, thăm động Trung Trang, pháo đài Thần Công với tầm nhìn toàn cảnh, hay ngủ đêm trên du thuyền giữa vịnh. Năm 2023, Quần đảo Cát Bà cùng vịnh Hạ Long được UNESCO công nhận là Di sản Thiên nhiên Thế giới liên tỉnh đầu tiên của Việt Nam, khẳng định giá trị cảnh quan và địa chất toàn cầu. Vẻ đẹp còn hoang sơ, ít ồn ào hơn Hạ Long khiến Cát Bà ngày càng hấp dẫn du khách trong và ngoài nước.",
    "presentation_long_en": "In the south-east of Hai Phong city, the Cat Ba Archipelago comprises over 360 limestone islands, of which Cat Ba is the largest and most populous in the Gulf of Tonkin. It is a natural jewel combining forest, sea and karst: the extensive Cat Ba National Park protects primeval forest and the critically endangered Cat Ba langur (white-headed langur), found nowhere else on Earth; Lan Ha Bay scatters hundreds of rocky islets across jade-green water, dotted with small white-sand beaches and floating fishing villages. Visitors come to swim at the Cat Co beaches, kayak through caves and hidden lagoons in Lan Ha Bay, hike in the national park, explore Trung Trang Cave and the Cannon Fort with its panoramic views, or spend a night on a cruise boat in the bay. In 2023 the Cat Ba Archipelago and Ha Long Bay were together recognised by UNESCO as Vietnam's first inter-provincial Natural World Heritage Site, affirming their global scenic and geological value. More unspoilt and less crowded than Ha Long, Cat Ba grows ever more appealing to domestic and foreign travellers alike.",
    "presentation_long_ru": "На юго-востоке города Хайфон архипелаг Катба насчитывает более 360 известняковых островов, крупнейший и самый населённый из которых, остров Катба, — главный в заливе Бакбо (Тонкинском). Это природная жемчужина, соединяющая лес, море и карст: обширный национальный парк Катба оберегает девственный лес и находящегося на грани исчезновения катбайского лангура (белоголового), который не встречается больше нигде на Земле; залив Ланьха рассыпает сотни скалистых островков по нефритово-зелёной воде, среди которых прячутся маленькие пляжи с белым песком и плавучие рыбацкие деревни. Сюда приезжают купаться на пляжах Катко, ходить на каяках сквозь пещеры и укромные лагуны Ланьха, совершать походы в национальном парке, осматривать пещеру Чунгчанг и Пушечный форт с панорамными видами или ночевать на круизном судне посреди залива. В 2023 году архипелаг Катба вместе с бухтой Халонг был признан ЮНЕСКО первым во Вьетнаме межпровинциальным объектом Всемирного природного наследия, что подтвердило их глобальную пейзажную и геологическую ценность. Более нетронутый и менее многолюдный, чем Халонг, Катба всё сильнее притягивает и вьетнамских, и иностранных путешественников.",
    "highlights_vi": [
      "Đảo lớn nhất vịnh Bắc Bộ; Vườn quốc gia Cát Bà và voọc Cát Bà quý hiếm",
      "Vịnh Lan Hạ tuyệt đẹp với hàng trăm đảo đá, bãi tắm và làng chài nổi",
      "Di sản Thiên nhiên Thế giới UNESCO (2023, cùng vịnh Hạ Long)"
    ],
    "highlights_en": [
      "The largest island in the Gulf of Tonkin; Cat Ba National Park and the rare Cat Ba langur",
      "The stunning Lan Ha Bay with hundreds of islets, beaches and floating villages",
      "UNESCO Natural World Heritage Site (2023, together with Ha Long Bay)"
    ],
    "highlights_ru": [
      "Крупнейший остров залива Бакбо; нацпарк Катба и редкий катбайский лангур",
      "Изумительный залив Ланьха с сотнями островков, пляжами и плавучими деревнями",
      "Объект Всемирного природного наследия ЮНЕСКО (2023, вместе с бухтой Халонг)"
    ],
    "practical": {
      "hours_vi": "Đảo tham quan quanh năm; tour vịnh Lan Hạ ban ngày.",
      "ticket_vi": "Vé Vườn quốc gia ~40.000 VND; tour vịnh/kayak tính riêng.",
      "duration_vi": "1–2 ngày để trải nghiệm biển đảo và vườn quốc gia.",
      "best_time_vi": "Mùa hè (tháng 4–9) tắm biển; tránh ngày bão.",
      "tips_vi": "Ra đảo bằng phà/cáp treo hoặc cao tốc từ Hải Phòng; đặt tour Lan Hạ và phòng sớm dịp hè."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "UNESCO World Heritage Centre — Ha Long Bay – Cat Ba Archipelago", "url": "https://whc.unesco.org/en/list/672/"},
      {"title": "Wikipedia (VI) — Quần đảo Cát Bà", "url": "https://vi.wikipedia.org/wiki/C%C3%A1t_B%C3%A0"}
    ],
    "tags": ["unesco", "island", "beach", "nature", "kayak", "top", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-hai-phong-do-son",
    "slug": "do-son",
    "region": "vn-hai-phong",
    "country": "vietnam",
    "region_name_vi": "Hải Phòng",
    "federal_district": "Miền Bắc",
    "name_vi": "Khu du lịch Đồ Sơn",
    "name_ru": "Курорт Дошон",
    "name_en": "Do Son Resort Town",
    "categories": ["other", "park_garden"],
    "coordinates": {"lat": 20.7130, "lon": 106.7880},
    "address_vi": "Quận Đồ Sơn, thành phố Hải Phòng",
    "rating": {"value": 4.1, "count": 3800, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách thích bán đảo nhô ra biển với đồi thông, biệt thự cổ kiểu Pháp và không khí nghỉ mát lâu đời. Nhiều người ấn tượng lễ hội chọi trâu truyền thống; một số nhận xét nước biển phù sa, không trong như biển miền Trung.",
    "presentation_short_vi": "Đồ Sơn ở thành phố Hải Phòng là khu nghỉ mát biển lâu đời, một bán đảo xanh mát nhô ra vịnh Bắc Bộ với đồi thông và biệt thự cổ kiểu Pháp. Nơi đây nổi tiếng với bãi biển, đền Bà Đế linh thiêng và lễ hội chọi trâu truyền thống độc đáo.",
    "presentation_short_en": "Do Son in Hai Phong is a long-established seaside resort, a green peninsula reaching into the Gulf of Tonkin with pine hills and old French villas. It is known for its beaches, the sacred Ba De Temple and the unique traditional buffalo-fighting festival.",
    "presentation_short_ru": "Дошон в Хайфоне — давний морской курорт, зелёный полуостров, вдающийся в залив Бакбо, с сосновыми холмами и старыми французскими виллами. Он известен пляжами, священным храмом Баде и уникальным традиционным фестивалем боёв буйволов.",
    "presentation_long_vi": "Cách trung tâm thành phố Hải Phòng khoảng 20 km, Đồ Sơn là một bán đảo dài vươn ra biển, được người Pháp chọn làm nơi nghỉ dưỡng từ cuối thế kỷ 19 với hệ thống biệt thự, dinh thự cổ nay vẫn còn – tiêu biểu là Biệt thự Bảo Đại trên đồi cao nhìn ra biển. Bờ biển Đồ Sơn chia thành nhiều khu, nước biển mang màu phù sa đặc trưng của vùng cửa sông đồng bằng Bắc Bộ, sóng êm, thích hợp tắm mát và dạo chơi hơn là lặn ngắm. Điểm hấp dẫn của Đồ Sơn nằm ở khung cảnh đồi thông xanh mát, những con đường ven biển thơ mộng và chiều sâu văn hóa – tâm linh: đền Bà Đế nép bên chân núi sát mép sóng, gắn với truyền thuyết bi thương và linh thiêng, là nơi cầu an của ngư dân; chùa Hang, tháp Tường Long thời Lý trên đỉnh núi. Đặc biệt, Đồ Sơn nổi tiếng cả nước với Lễ hội chọi trâu truyền thống tổ chức vào mùng 9 tháng 8 âm lịch – di sản văn hóa phi vật thể quốc gia, thu hút đông đảo du khách. Với bề dày lịch sử nghỉ mát và sự pha trộn giữa biển, rừng, kiến trúc Pháp và tín ngưỡng dân gian, Đồ Sơn là điểm đến gần gũi, giàu bản sắc của miền biển Bắc Bộ.",
    "presentation_long_en": "About 20 km from central Hai Phong, Do Son is a long peninsula reaching out to sea that the French chose as a retreat from the late 19th century, leaving behind old villas and mansions — notably the Bao Dai Villa on a hilltop overlooking the water. Its shoreline is divided into several zones; the sea carries the silt-tinted colour typical of the Red River delta's estuaries, with gentle waves better suited to bathing and strolling than to diving. Do Son's charm lies in its cool green pine hills, romantic coastal roads and cultural-spiritual depth: Ba De Temple, nestled at the foot of a hill right by the waves and bound to a sorrowful, sacred legend, is where fishermen pray for safety; there is also the Hang (Cave) Pagoda and the Ly-dynasty Tuong Long Tower on the summit. Above all, Do Son is nationally famous for its traditional buffalo-fighting festival held on the ninth day of the eighth lunar month — a national intangible cultural heritage that draws large crowds. With its long resort history and its blend of sea, forest, French architecture and folk belief, Do Son is an accessible, character-rich destination on the northern coast.",
    "presentation_long_ru": "Примерно в 20 км от центра Хайфона Дошон — длинный полуостров, вдающийся в море, который французы избрали местом отдыха ещё в конце XIX века, оставив старые виллы и особняки — прежде всего виллу Бао Дая на вершине холма с видом на воду. Береговая линия разделена на несколько зон; море несёт характерный для устьев дельты Красной реки илистый оттенок, с мягкими волнами, больше подходящими для купания и прогулок, чем для дайвинга. Очарование Дошона — в прохладных зелёных сосновых холмах, романтичных прибрежных дорогах и культурно-духовной глубине: храм Баде, приютившийся у подножия холма у самых волн и связанный с печальной, священной легендой, — место, где рыбаки молятся о безопасности; есть также Пещерная пагода и башня Тыонглонг эпохи Ли на вершине. Но прежде всего Дошон знаменит на всю страну традиционным фестивалем боёв буйволов, что проходит в девятый день восьмого лунного месяца, — это национальное нематериальное культурное наследие, собирающее большие толпы. С его давней курортной историей и сочетанием моря, леса, французской архитектуры и народных верований Дошон — доступное, самобытное направление на северном побережье.",
    "highlights_vi": [
      "Bán đảo nghỉ mát lâu đời với đồi thông và biệt thự cổ kiểu Pháp (Biệt thự Bảo Đại)",
      "Đền Bà Đế linh thiêng, chùa Hang, tháp Tường Long thời Lý",
      "Lễ hội chọi trâu truyền thống (9/8 âm lịch) — di sản văn hóa phi vật thể quốc gia"
    ],
    "highlights_en": [
      "A historic resort peninsula with pine hills and old French villas (Bao Dai Villa)",
      "The sacred Ba De Temple, Hang Pagoda and the Ly-dynasty Tuong Long Tower",
      "The traditional buffalo-fighting festival (9th day, 8th lunar month) — national heritage"
    ],
    "highlights_ru": [
      "Исторический курортный полуостров с сосновыми холмами и французскими виллами (вилла Бао Дая)",
      "Священный храм Баде, Пещерная пагода и башня Тыонглонг эпохи Ли",
      "Традиционный фестиваль боёв буйволов (9-й день 8-го лунного месяца) — наследие"
    ],
    "practical": {
      "hours_vi": "Khu du lịch mở cả ngày; các điểm tham quan mở ban ngày.",
      "ticket_vi": "Vào bãi biển cơ bản miễn phí; một số điểm/di tích thu vé nhỏ.",
      "duration_vi": "Nửa ngày đến 1 ngày.",
      "best_time_vi": "Mùa hè (tháng 5–8); mùa lễ hội chọi trâu (tháng 8 âm lịch).",
      "tips_vi": "Kết hợp thăm Biệt thự Bảo Đại và đền Bà Đế; hải sản phong phú; nước biển đục phù sa là bình thường."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Đồ Sơn", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BB%93_S%C6%A1n"}
    ],
    "tags": ["beach", "sea", "history", "festival", "culture", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
]

# ===================== CÀ MAU (Miền Nam) =====================
PLACES += [
  {
    "id": "vn-ca-mau-mui-ca-mau",
    "slug": "mui-ca-mau",
    "region": "vn-ca-mau",
    "country": "vietnam",
    "region_name_vi": "Cà Mau",
    "federal_district": "Miền Nam",
    "name_vi": "Mũi Cà Mau (Đất Mũi)",
    "name_ru": "Мыс Камау (Датмуй)",
    "name_en": "Ca Mau Cape (Dat Mui)",
    "categories": ["park_garden", "monument"],
    "coordinates": {"lat": 8.6197, "lon": 104.7223},
    "address_vi": "Xã Đất Mũi, huyện Ngọc Hiển, tỉnh Cà Mau",
    "rating": {"value": 4.6, "count": 4300, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách tự hào khi đặt chân tới điểm cực Nam Tổ quốc, chụp ảnh bên cột mốc tọa độ và biểu tượng con tàu. Nhiều người thích đi vỏ lãi xuyên rừng đước, ngắm bãi bồi; một số nhắc đường xa, nên đi trọn ngày.",
    "presentation_short_vi": "Mũi Cà Mau ở xã Đất Mũi, tỉnh Cà Mau là điểm cực Nam trên đất liền của Việt Nam, nơi có thể ngắm mặt trời mọc trên Biển Đông và lặn xuống Vịnh Thái Lan. Vùng đất mũi với rừng đước ngập mặn và bãi bồi lấn biển là biểu tượng thiêng liêng của Tổ quốc.",
    "presentation_short_en": "Ca Mau Cape in Dat Mui commune, Ca Mau province, is the southernmost point of mainland Vietnam, where one can watch the sun rise over the East Sea and set into the Gulf of Thailand. With its mangrove forest and seaward-growing mudflats, the cape is a cherished national symbol.",
    "presentation_short_ru": "Мыс Камау в общине Датмуй провинции Камау — самая южная точка материкового Вьетнама, где можно видеть, как солнце восходит над Восточным морем и садится в Сиамский залив. С мангровым лесом и намывными отмелями, растущими в море, мыс — заветный символ страны.",
    "presentation_long_vi": "Mũi Cà Mau là mảnh đất thiêng liêng nơi tận cùng cực Nam của Tổ quốc, thuộc xã Đất Mũi, huyện Ngọc Hiển, cách thành phố Cà Mau khoảng 100 km. Đây là điểm duy nhất trên đất liền Việt Nam mà du khách có thể ngắm cả mặt trời mọc trên Biển Đông lẫn hoàng hôn buông xuống Vịnh Thái Lan trong cùng một ngày. Vùng đất này nằm trong Vườn quốc gia Mũi Cà Mau – khu dự trữ sinh quyển thế giới và vùng đất ngập nước Ramsar, với hệ sinh thái rừng ngập mặn đước, mắm bạt ngàn. Điều đặc biệt của Đất Mũi là 'đất biết đi': phù sa sông Mê Kông bồi đắp khiến mũi đất mỗi năm lấn ra biển hàng chục mét, mở rộng lãnh thổ quốc gia. Tại đây có cột mốc tọa độ quốc gia GPS 0001, biểu tượng con tàu Đất Mũi hướng ra khơi, cột cờ Hà Nội thu nhỏ và những cây cầu, đài quan sát giữa rừng đước. Du khách thường đi 'vỏ lãi' (xuồng máy) len lỏi qua kênh rạch và rừng ngập mặn, thăm bãi bồi, trải nghiệm cuộc sống của cư dân miền cực Nam và thưởng thức hải sản như cua Cà Mau, ba khía, cá thòi lòi. Đến Mũi Cà Mau, mỗi người Việt Nam đều mang trong lòng niềm xúc động thiêng liêng khi chạm tới điểm cuối cùng của dải đất hình chữ S.",
    "presentation_long_en": "Ca Mau Cape is the sacred land at the far southern tip of Vietnam, in Dat Mui commune, Ngoc Hien district, about 100 km from Ca Mau city. It is the only place on the Vietnamese mainland where visitors can watch both the sunrise over the East Sea and the sunset into the Gulf of Thailand on the same day. The area lies within Mui Ca Mau National Park — a world biosphere reserve and a Ramsar wetland — with vast mangrove ecosystems of duoc and mam trees. What makes Dat Mui special is its 'walking land': silt from the Mekong builds the cape outward by tens of metres each year, extending the national territory. Here stand the national coordinate marker GPS 0001, the symbolic Dat Mui 'ship' pointing out to sea, a miniature Hanoi flag tower, and boardwalks and observation decks amid the mangroves. Visitors typically ride a 'vo lai' (motor sampan) threading through canals and mangrove forest, visit the growing mudflats, experience the life of the far-southern communities, and enjoy seafood such as Ca Mau crab, ba khia (fermented fiddler crab) and mudskipper. For every Vietnamese, reaching Ca Mau Cape stirs a sacred emotion at touching the very end of the S-shaped homeland.",
    "presentation_long_ru": "Мыс Камау — священная земля на самой южной оконечности Вьетнама, в общине Датмуй уезда Нгокхьен, примерно в 100 км от города Камау. Это единственное место на материковом Вьетнаме, где в один и тот же день можно видеть и восход над Восточным морем, и закат в Сиамском заливе. Территория входит в национальный парк Муйкамау — всемирный биосферный заповедник и Рамсарское водно-болотное угодье — с обширными мангровыми экосистемами деревьев дыок и мам. Особенность Датмуй — «идущая земля»: ил Меконга наращивает мыс в сторону моря на десятки метров ежегодно, расширяя территорию страны. Здесь установлены национальный координатный столб GPS 0001, символический «корабль» Датмуй, устремлённый в море, уменьшенная копия ханойской флаговой башни, а также настилы и смотровые площадки среди мангров. Туристы обычно плывут на «во лай» (моторной лодке-сампане) по каналам и мангровому лесу, посещают намывные отмели, знакомятся с жизнью общин крайнего юга и пробуют морепродукты — краба Камау, «ба кхиа» (квашеного краба-скрипача) и илистого прыгуна. Для каждого вьетнамца достичь мыса Камау — значит испытать священное волнение, коснувшись самого конца S-образной родины.",
    "highlights_vi": [
      "Điểm cực Nam trên đất liền của Việt Nam; cột mốc tọa độ GPS 0001",
      "Vườn quốc gia Mũi Cà Mau — khu dự trữ sinh quyển & vùng Ramsar, rừng đước bạt ngàn",
      "'Đất biết đi' lấn biển; ngắm bình minh Biển Đông và hoàng hôn Vịnh Thái Lan"
    ],
    "highlights_en": [
      "The southernmost point of mainland Vietnam; the GPS 0001 coordinate marker",
      "Mui Ca Mau National Park — biosphere reserve and Ramsar site, vast mangroves",
      "'Walking land' growing seaward; sunrise over the East Sea and sunset into the Gulf of Thailand"
    ],
    "highlights_ru": [
      "Самая южная точка материкового Вьетнама; координатный столб GPS 0001",
      "Нацпарк Муйкамау — биосферный заповедник и Рамсарский объект, обширные мангры",
      "«Идущая земля», растущая в море; восход над Восточным морем и закат в Сиамский залив"
    ],
    "practical": {
      "hours_vi": "Khu du lịch mở khoảng 7:00–18:00.",
      "ticket_vi": "Vé tham quan tham khảo khoảng 40.000–60.000 VND; đi vỏ lãi tính riêng.",
      "duration_vi": "Nửa ngày đến 1 ngày (tính cả di chuyển).",
      "best_time_vi": "Mùa khô (tháng 12–4) đường đi thuận lợi.",
      "tips_vi": "Đường xa, nên khởi hành sớm; thử cua Cà Mau, ba khía; mang chống nắng, chống muỗi khi vào rừng đước."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Mũi Cà Mau", "url": "https://vi.wikipedia.org/wiki/M%C5%A9i_C%C3%A0_Mau"},
      {"title": "Wikipedia (EN) — Mui Ca Mau National Park", "url": "https://en.wikipedia.org/wiki/M%C5%A9i_C%C3%A0_Mau_National_Park"}
    ],
    "tags": ["nature", "landmark", "mangrove", "national-park", "top", "outdoor", "viewpoint"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-ca-mau-u-minh-ha",
    "slug": "u-minh-ha",
    "region": "vn-ca-mau",
    "country": "vietnam",
    "region_name_vi": "Cà Mau",
    "federal_district": "Miền Nam",
    "name_vi": "Vườn quốc gia U Minh Hạ",
    "name_ru": "Национальный парк Уминьха",
    "name_en": "U Minh Ha National Park",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 9.2550, "lon": 104.9500},
    "address_vi": "Huyện U Minh và Trần Văn Thời, tỉnh Cà Mau",
    "rating": {"value": 4.4, "count": 900, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách thích không gian rừng tràm ngập nước nguyên sơ, đi xuồng len lỏi giữa rừng và trải nghiệm 'ăn ong' lấy mật. Nhiều người thấy yên tĩnh, gần gũi thiên nhiên; một số nhắc nhiều muỗi, nên chuẩn bị kỹ.",
    "presentation_short_vi": "Vườn quốc gia U Minh Hạ ở tỉnh Cà Mau bảo tồn hệ sinh thái rừng tràm trên đất than bùn ngập nước đặc trưng của miền Tây Nam Bộ. Là khu dự trữ sinh quyển thế giới, nơi đây nổi tiếng với rừng tràm bạt ngàn, đa dạng chim thú và nghề 'gác kèo ong' lấy mật truyền thống.",
    "presentation_short_en": "U Minh Ha National Park in Ca Mau province preserves the melaleuca (cajuput) forest ecosystem on flooded peatland typical of Vietnam's south-west. A world biosphere reserve, it is famed for vast cajuput forests, abundant birdlife and the traditional craft of 'beam-hanging' for wild honey.",
    "presentation_short_ru": "Национальный парк Уминьха в провинции Камау сохраняет экосистему мелалеукового (каюпутового) леса на затопленных торфяниках, характерных для юго-запада Вьетнама. Всемирный биосферный заповедник знаменит бескрайними каюпутовыми лесами, обилием птиц и традиционным промыслом сбора дикого мёда.",
    "presentation_long_vi": "Vườn quốc gia U Minh Hạ nằm trên địa bàn hai huyện U Minh và Trần Văn Thời, là một trong những khu rừng tràm ngập nước trên đất than bùn tiêu biểu và quý giá bậc nhất của đồng bằng sông Cửu Long. Cùng với U Minh Thượng, khu rừng này tạo nên vùng U Minh huyền thoại đã đi vào văn học qua tác phẩm 'Đất rừng phương Nam'. Rừng tràm mọc dày trên lớp than bùn dày, quanh năm ngập nước màu nâu đỏ đặc trưng, tạo môi trường sống cho nhiều loài động vật hoang dã như rái cá, khỉ, trăn, rắn, rùa, cùng vô số loài chim, cò và ong mật. U Minh Hạ được UNESCO công nhận là vùng lõi của Khu dự trữ sinh quyển thế giới Mũi Cà Mau. Đến đây, du khách đi xuồng máy hoặc xuồng chèo len lỏi giữa những con kênh phủ bèo và tán tràm rợp mát, leo tháp quan sát ngắm rừng bao la, tìm hiểu nghề 'gác kèo ong' – cách người dân đặt kèo cho ong rừng làm tổ để thu mật tràm thơm ngon nức tiếng. Ẩm thực nơi đây dân dã mà độc đáo với cá lóc nướng trui, lươn, rắn, mật ong rừng. U Minh Hạ mang đến trải nghiệm sinh thái nguyên sơ, đậm chất miền Tây sông nước.",
    "presentation_long_en": "U Minh Ha National Park, spanning U Minh and Tran Van Thoi districts, is one of the most representative and precious flooded peatland cajuput forests in the Mekong Delta. Together with U Minh Thuong, it forms the legendary U Minh region immortalised in the novel 'The Southern Land'. Cajuput trees grow densely on a thick peat layer flooded year-round with its characteristic reddish-brown water, creating a habitat for wildlife such as otters, monkeys, pythons, snakes and turtles, along with countless birds, storks and honeybees. U Minh Ha is recognised by UNESCO as a core zone of the Mui Ca Mau World Biosphere Reserve. Here visitors ride motorised or paddled sampans through canals cloaked in duckweed and shaded by cajuput canopies, climb observation towers to survey the endless forest, and learn the craft of 'beam-hanging' — the way locals set wooden beams for wild bees to nest so they can harvest the region's famously fragrant cajuput honey. The cuisine is rustic yet distinctive: field-grilled snakehead fish, eel, snake and wild honey. U Minh Ha offers a pristine ecological experience steeped in the watery character of the western delta.",
    "presentation_long_ru": "Национальный парк Уминьха, охватывающий уезды Уминь и Чанвантхой, — один из самых показательных и ценных затопленных торфяниковых каюпутовых лесов дельты Меконга. Вместе с Уминьтхыонг он образует легендарный край Уминь, воспетый в романе «Южная земля». Каюпутовые деревья густо растут на толстом слое торфа, круглый год затопленном характерной красновато-бурой водой, создавая местообитание для выдр, обезьян, питонов, змей и черепах, а также бесчисленных птиц, аистов и медоносных пчёл. Уминьха признан ЮНЕСКО ядром всемирного биосферного заповедника Муйкамау. Здесь туристы плывут на моторных или вёсельных сампанах по каналам, укрытым ряской и тенью каюпутовых крон, поднимаются на смотровые вышки, чтобы окинуть взглядом бескрайний лес, и знакомятся с промыслом «подвешивания балок» — так местные жители устанавливают деревянные балки, чтобы дикие пчёлы вили гнёзда, и собирают знаменитый ароматный каюпутовый мёд. Кухня простая, но самобытная: змееголов, жаренный в поле, угорь, змея и дикий мёд. Уминьха дарит первозданные экологические впечатления, пропитанные водным духом западной дельты. В сухой сезон дороги удобнее, а в пору паводка лес особенно живописен, хотя стоит запастись средством от комаров; поездку сюда легко совместить с посещением мыса Камау на крайнем юге страны.",
    "highlights_vi": [
      "Rừng tràm ngập nước trên đất than bùn — vùng lõi Khu dự trữ sinh quyển thế giới",
      "Đi xuồng xuyên rừng, leo tháp ngắm cảnh, đa dạng chim thú hoang dã",
      "Nghề 'gác kèo ong' truyền thống và mật ong tràm nổi tiếng"
    ],
    "highlights_en": [
      "Flooded peatland cajuput forest — a core zone of a World Biosphere Reserve",
      "Sampan rides through the forest, observation towers, abundant wildlife",
      "The traditional 'beam-hanging' craft and famous cajuput honey"
    ],
    "highlights_ru": [
      "Затопленный торфяниковый каюпутовый лес — ядро всемирного биосферного заповедника",
      "Прогулки на сампанах сквозь лес, смотровые вышки, обилие дикой природы",
      "Традиционный промысел «подвешивания балок» и знаменитый каюпутовый мёд"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
      "ticket_vi": "Vé và dịch vụ xuồng tham khảo khoảng 30.000–100.000 VND tùy tuyến.",
      "duration_vi": "Khoảng 2–3 giờ.",
      "best_time_vi": "Mùa khô (tháng 12–4); mùa nước nổi cảnh cũng đẹp nhưng nhiều muỗi.",
      "tips_vi": "Mang chống muỗi, kem chống nắng; đi cùng hướng dẫn; kết hợp tuyến Mũi Cà Mau."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Vườn quốc gia U Minh Hạ", "url": "https://vi.wikipedia.org/wiki/V%C6%B0%E1%BB%9Dn_qu%E1%BB%91c_gia_U_Minh_H%E1%BA%A1"}
    ],
    "tags": ["nature", "national-park", "mangrove", "ecotourism", "boat", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
]

# ===================== ĐỒNG THÁP (Miền Nam) =====================
PLACES += [
  {
    "id": "vn-dong-thap-tram-chim",
    "slug": "tram-chim",
    "region": "vn-dong-thap",
    "country": "vietnam",
    "region_name_vi": "Đồng Tháp",
    "federal_district": "Miền Nam",
    "name_vi": "Vườn quốc gia Tràm Chim",
    "name_ru": "Национальный парк Чамтьим",
    "name_en": "Tram Chim National Park",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 10.7200, "lon": 105.5200},
    "address_vi": "Huyện Tam Nông, tỉnh Đồng Tháp",
    "rating": {"value": 4.5, "count": 1600, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách thích đi tắc ráng giữa rừng tràm, đồng sen, lúa ma và ngắm chim nước bay rợp trời lúc bình minh, hoàng hôn. Nhiều người mê mùa nước nổi; một số mong thấy sếu đầu đỏ (chỉ xuất hiện theo mùa).",
    "presentation_short_vi": "Vườn quốc gia Tràm Chim ở huyện Tam Nông, tỉnh Đồng Tháp là mô hình thu nhỏ của vùng Đồng Tháp Mười, với rừng tràm, đồng cỏ ngập nước và hệ chim nước phong phú. Đây là khu Ramsar thứ 2.000 của thế giới, nổi tiếng là nơi trú ngụ của loài sếu đầu đỏ quý hiếm.",
    "presentation_short_en": "Tram Chim National Park in Tam Nong district, Dong Thap province, is a miniature of the Dong Thap Muoi wetlands, with cajuput forest, flooded grasslands and rich waterbird life. It is the world's 2,000th Ramsar site, famed as a refuge of the rare red-crowned crane.",
    "presentation_short_ru": "Национальный парк Чамтьим в уезде Тамнонг провинции Донгтхап — уменьшенная модель водно-болотных угодий Донгтхапмыой, с каюпутовым лесом, затопленными лугами и богатым миром водоплавающих птиц. Это 2000-й в мире Рамсарский объект, знаменитый как убежище редкого японского журавля.",
    "presentation_long_vi": "Vườn quốc gia Tràm Chim rộng khoảng 7.500 ha, được ví như 'Đồng Tháp Mười thu nhỏ', bảo tồn hệ sinh thái đất ngập nước tiêu biểu của vùng trũng Đồng Tháp Mười xưa. Cảnh quan nơi đây là sự đan xen của rừng tràm, các trảng cỏ năn, lác, lúa ma (lúa trời) và những đầm sen, súng nở rực rỡ. Tràm Chim là thiên đường của các loài chim nước với hơn 230 loài được ghi nhận, trong đó quý giá nhất là sếu đầu đỏ (sếu cổ trụi) – loài chim biểu tượng, có tên trong Sách Đỏ, thường về kiếm ăn vào mùa khô. Năm 2012, Tràm Chim được công nhận là khu Ramsar (vùng đất ngập nước có tầm quan trọng quốc tế) thứ tư của Việt Nam và thứ 2.000 của thế giới. Du khách đến đây đi tắc ráng (xuồng máy nhỏ) len lỏi qua các kênh rạch phủ đầy bèo và sen, leo đài quan sát ngắm toàn cảnh đồng bưng mênh mông, xem chim về tổ lúc hoàng hôn và trải nghiệm cuộc sống mùa nước nổi đặc trưng miền Tây. Ẩm thực dân dã hấp dẫn với cá lóc nướng, bông súng mắm kho, ốc, lẩu cá linh bông điên điển. Tràm Chim mang đến trải nghiệm sinh thái trong lành và cơ hội hiếm có để chiêm ngưỡng thiên nhiên hoang dã của đồng bằng sông Cửu Long.",
    "presentation_long_en": "Covering about 7,500 hectares, Tram Chim National Park is likened to a 'miniature Dong Thap Muoi', preserving the representative wetland ecosystem of the old Plain of Reeds. Its landscape interweaves cajuput forest, meadows of eleocharis and sedge, wild rice, and ponds ablaze with lotus and water lilies. Tram Chim is a paradise for waterbirds, with more than 230 recorded species — the most precious being the red-crowned (sarus) crane, an emblematic Red-List bird that comes to feed in the dry season. In 2012 Tram Chim was recognised as Vietnam's fourth Ramsar site (a wetland of international importance) and the 2,000th in the world. Visitors ride a 'tac rang' (small motor sampan) through canals carpeted with duckweed and lotus, climb observation towers for a panorama of the vast marsh, watch birds return to roost at dusk, and experience the region's distinctive floating-season life. The rustic cuisine is a draw: grilled snakehead fish, water-lily stems with braised fish sauce, snails and a hotpot of linh fish with sesbania flowers. Tram Chim offers a fresh ecological experience and a rare chance to admire the wild nature of the Mekong Delta.",
    "presentation_long_ru": "Занимающий около 7500 гектаров, национальный парк Чамтьим называют «уменьшенным Донгтхапмыой»: он сохраняет показательную водно-болотную экосистему былой Тростниковой равнины. Его пейзаж переплетает каюпутовый лес, луга ситника и осоки, дикий рис и пруды, пылающие лотосами и кувшинками. Чамтьим — рай для водоплавающих птиц: здесь отмечено более 230 видов, ценнейший из которых — индийский (красноголовый) журавль, эмблематичная птица из Красной книги, прилетающая кормиться в сухой сезон. В 2012 году Чамтьим был признан четвёртым во Вьетнаме и 2000-м в мире Рамсарским объектом (водно-болотным угодьем международного значения). Туристы плывут на «так ранг» (небольшом моторном сампане) по каналам, устланным ряской и лотосами, поднимаются на смотровые вышки ради панорамы бескрайнего болота, наблюдают, как птицы возвращаются на ночлег в сумерках, и знакомятся с самобытной жизнью «сезона большой воды». Привлекает и простая кухня: жареный змееголов, стебли кувшинок с тушёным рыбным соусом, улитки и суп-хотпот из рыбы линь с цветами сесбании. Чамтьим дарит свежие экологические впечатления и редкую возможность полюбоваться дикой природой дельты Меконга.",
    "highlights_vi": [
      "'Đồng Tháp Mười thu nhỏ': rừng tràm, đồng sen, lúa ma, hơn 230 loài chim",
      "Khu Ramsar thứ 2.000 thế giới; nơi trú ngụ của sếu đầu đỏ quý hiếm",
      "Đi tắc ráng, leo đài quan sát, đẹp nhất mùa nước nổi và mùa sen"
    ],
    "highlights_en": [
      "A 'miniature Dong Thap Muoi': cajuput forest, lotus, wild rice, 230+ bird species",
      "The world's 2,000th Ramsar site; a refuge of the rare red-crowned crane",
      "Sampan rides and observation towers; best in the floating season and lotus season"
    ],
    "highlights_ru": [
      "«Уменьшенный Донгтхапмыой»: каюпутовый лес, лотосы, дикий рис, 230+ видов птиц",
      "2000-й в мире Рамсарский объект; убежище редкого красноголового журавля",
      "Прогулки на сампанах и смотровые вышки; лучше всего в сезон воды и лотосов"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
      "ticket_vi": "Vé và thuê tắc ráng tham khảo khoảng 100.000–350.000 VND tùy tuyến/nhóm.",
      "duration_vi": "Khoảng 2–3 giờ.",
      "best_time_vi": "Mùa nước nổi (khoảng tháng 9–11) và mùa sen; sáng sớm/chiều muộn xem chim.",
      "tips_vi": "Đi sớm để xem chim; mang chống nắng, chống muỗi; đặt tắc ráng trước dịp lễ."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Vườn quốc gia Tràm Chim", "url": "https://vi.wikipedia.org/wiki/V%C6%B0%E1%BB%9Dn_qu%E1%BB%91c_gia_Tr%C3%A0m_Chim"}
    ],
    "tags": ["nature", "national-park", "birdwatching", "wetland", "ramsar", "boat", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-dong-thap-lang-hoa-sa-dec",
    "slug": "lang-hoa-sa-dec",
    "region": "vn-dong-thap",
    "country": "vietnam",
    "region_name_vi": "Đồng Tháp",
    "federal_district": "Miền Nam",
    "name_vi": "Làng hoa Sa Đéc",
    "name_ru": "Цветочная деревня Шадек",
    "name_en": "Sa Dec Flower Village",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 10.2980, "lon": 105.7550},
    "address_vi": "Phường Tân Quy Đông, thành phố Sa Đéc, tỉnh Đồng Tháp",
    "rating": {"value": 4.4, "count": 2500, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách thích ngắm những ruộng hoa, giàn hoa treo rực rỡ và các nhà vườn kiểng đủ loại. Nhiều người khen chụp ảnh đẹp, người dân thân thiện; một số nói hoa nhiều và đẹp nhất dịp giáp Tết.",
    "presentation_short_vi": "Làng hoa Sa Đéc ở thành phố Sa Đéc, tỉnh Đồng Tháp là một trong những vựa hoa kiểng lớn và lâu đời nhất miền Nam, với hơn trăm năm tuổi nghề. Quanh năm rực rỡ sắc màu của hàng nghìn loài hoa và cây cảnh, nơi đây là điểm tham quan, chụp ảnh và mua hoa nổi tiếng.",
    "presentation_short_en": "Sa Dec Flower Village in Sa Dec city, Dong Thap province, is one of the largest and oldest ornamental-flower hubs in southern Vietnam, with over a century of tradition. Ablaze year-round with thousands of species of flowers and bonsai, it is a famed spot for sightseeing, photography and buying blooms.",
    "presentation_short_ru": "Цветочная деревня Шадек в городе Шадек провинции Донгтхап — один из крупнейших и старейших центров декоративного цветоводства юга Вьетнама, с более чем вековой традицией. Круглый год пылая тысячами видов цветов и бонсай, она славится как место для прогулок, фотографий и покупки цветов.",
    "presentation_long_vi": "Nằm bên bờ sông Tiền, Làng hoa Sa Đéc (tập trung ở phường Tân Quy Đông) có lịch sử hơn 100 năm, được xem là một trong những trung tâm sản xuất hoa kiểng lớn nhất Đồng bằng sông Cửu Long và cả miền Nam. Trên diện tích hàng trăm hecta, người dân trồng hàng nghìn loài hoa và cây cảnh: hoa hồng nhiều màu, cúc, cẩm chướng, hướng dương, hoa giấy, cùng vô số loại kiểng lá, kiểng bonsai được tạo dáng công phu. Nét độc đáo của làng là kỹ thuật trồng hoa trên những luống cao, giàn giá ngập nước, người làm vườn phải di chuyển bằng xuồng để chăm sóc – hình ảnh đặc trưng chỉ có ở miền sông nước. Quanh năm làng hoa khoác lên mình sắc màu rực rỡ, nhưng nhộn nhịp và lộng lẫy nhất là vào dịp giáp Tết Nguyên đán, khi hoa được xuất đi khắp các tỉnh thành. Ngày nay, bên cạnh nghề truyền thống, Sa Đéc phát triển du lịch với các khu vườn hoa mở cửa đón khách tham quan, những giàn hoa treo, con đường hoa và tiểu cảnh check-in đẹp mắt. Du khách còn có thể kết hợp thăm nhà cổ Huỳnh Thủy Lê gắn với chuyện tình trong tiểu thuyết 'Người tình', thưởng thức đặc sản hủ tiếu Sa Đéc trứ danh. Làng hoa mang đến trải nghiệm thư thái, đầy màu sắc và đậm hồn quê Nam Bộ.",
    "presentation_long_en": "On the bank of the Tien River, Sa Dec Flower Village (centred on Tan Quy Dong ward) has more than a century of history and is regarded as one of the largest ornamental-flower production centres in the Mekong Delta and the whole south. Across hundreds of hectares, growers raise thousands of species of flowers and plants: multicoloured roses, chrysanthemums, carnations, sunflowers, paper flowers, and countless foliage plants and artfully shaped bonsai. The village's signature is its technique of growing flowers on raised beds and racks standing in water, so gardeners must move by sampan to tend them — an image found only in this land of rivers. The village glows with colour all year, but is at its busiest and most dazzling in the run-up to the Lunar New Year, when its flowers are shipped to provinces across the country. Today, alongside the traditional trade, Sa Dec has developed tourism, with flower gardens open to visitors, hanging flower trellises, floral lanes and photogenic installations. Visitors can also combine a look at the old Huynh Thuy Le House, tied to the romance in the novel 'The Lover', with a taste of the celebrated Sa Dec hu tieu noodle soup. The flower village offers a relaxing, colourful experience steeped in the soul of the southern countryside.",
    "presentation_long_ru": "На берегу реки Тьен цветочная деревня Шадек (сосредоточенная в квартале Танкуйдонг) насчитывает более века истории и считается одним из крупнейших центров декоративного цветоводства дельты Меконга и всего юга. На сотнях гектаров цветоводы выращивают тысячи видов цветов и растений: разноцветные розы, хризантемы, гвоздики, подсолнухи, бугенвиллеи, а также бесчисленные лиственные растения и искусно сформированные бонсай. Визитная карточка деревни — техника выращивания цветов на высоких грядках и стеллажах, стоящих в воде, так что садовникам приходится передвигаться на сампанах, чтобы ухаживать за ними, — образ, встречающийся лишь в этом краю рек. Деревня пылает красками круглый год, но особенно оживлена и ослепительна в преддверии лунного Нового года, когда её цветы развозят по провинциям всей страны. Сегодня наряду с традиционным промыслом Шадек развивает туризм: цветники открыты для гостей, есть подвесные шпалеры, цветочные аллеи и фотогеничные площадки. Посетители могут также осмотреть старинный дом Хюинь Тхюи Ле, связанный с романом «Любовник», и отведать знаменитый суп-лапшу «ху тьеу» из Шадека. Цветочная деревня дарит спокойные, красочные впечатления, пропитанные душой южной деревни.",
    "highlights_vi": [
      "Vựa hoa kiểng hơn 100 năm tuổi, lớn bậc nhất miền Nam",
      "Trồng hoa trên giàn ngập nước, chăm sóc bằng xuồng — nét độc đáo miền Tây",
      "Rực rỡ nhất giáp Tết; gần nhà cổ Huỳnh Thủy Lê và hủ tiếu Sa Đéc"
    ],
    "highlights_en": [
      "A century-old ornamental-flower hub, among the largest in the south",
      "Flowers grown on water-standing racks, tended by sampan — a delta specialty",
      "Most dazzling before Tet; near the Huynh Thuy Le House and Sa Dec noodles"
    ],
    "highlights_ru": [
      "Столетний центр декоративного цветоводства, один из крупнейших на юге",
      "Цветы на стоящих в воде стеллажах, уход с сампанов — особенность дельты",
      "Ослепительнее всего перед Тетом; рядом дом Хюинь Тхюи Ле и лапша Шадек"
    ],
    "practical": {
      "hours_vi": "Các nhà vườn/khu du lịch mở khoảng 7:00–18:00.",
      "ticket_vi": "Một số vườn thu vé tham khảo khoảng 20.000–40.000 VND.",
      "duration_vi": "Khoảng 1,5–2 giờ.",
      "best_time_vi": "Đẹp nhất giáp Tết (tháng 12 âm lịch – trước Tết); quanh năm vẫn có hoa.",
      "tips_vi": "Đi sáng sớm mát và đủ sáng chụp ảnh; kết hợp nhà cổ Huỳnh Thủy Lê, ăn hủ tiếu Sa Đéc."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Làng hoa Sa Đéc", "url": "https://vi.wikipedia.org/wiki/L%C3%A0ng_hoa_Sa_%C4%90%C3%A9c"}
    ],
    "tags": ["flowers", "garden", "culture", "photography", "family", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
  {
    "id": "vn-dong-thap-go-thap",
    "slug": "go-thap",
    "region": "vn-dong-thap",
    "country": "vietnam",
    "region_name_vi": "Đồng Tháp",
    "federal_district": "Miền Nam",
    "name_vi": "Khu di tích Gò Tháp",
    "name_ru": "Археологический комплекс Готхап",
    "name_en": "Go Thap Archaeological Site",
    "categories": ["monument", "other"],
    "coordinates": {"lat": 10.6333, "lon": 105.6733},
    "address_vi": "Xã Tân Kiều/Mỹ Hòa, huyện Tháp Mười, tỉnh Đồng Tháp",
    "rating": {"value": 4.4, "count": 800, "source": "Google", "as_of": "2026-07"},
    "review_summary_vi": "Du khách thấy thú vị khi vừa khám phá di tích khảo cổ văn hóa Óc Eo, vừa viếng đền thờ và tận hưởng không gian đồng bưng Đồng Tháp Mười. Nhiều người đến vào mùa lễ hội; một số nhắc nên đi kèm hướng dẫn để hiểu lịch sử.",
    "presentation_short_vi": "Khu di tích Gò Tháp ở huyện Tháp Mười, tỉnh Đồng Tháp là quần thể khảo cổ – lịch sử – tâm linh độc đáo giữa vùng Đồng Tháp Mười. Nơi đây lưu giữ dấu tích văn hóa Óc Eo cổ xưa cùng các đền thờ anh hùng dân tộc, được xếp hạng Di tích Quốc gia đặc biệt.",
    "presentation_short_en": "The Go Thap site in Thap Muoi district, Dong Thap province, is a unique archaeological, historical and spiritual complex in the heart of the Plain of Reeds. It preserves traces of the ancient Oc Eo culture along with temples to national heroes, and is ranked a Special National Relic.",
    "presentation_short_ru": "Комплекс Готхап в уезде Тхапмыой провинции Донгтхап — уникальный археологический, исторический и духовный комплекс в сердце Тростниковой равнины. Он хранит следы древней культуры Окео и храмы национальным героям и отнесён к особым национальным памятникам.",
    "presentation_long_vi": "Gò Tháp là một quần thể di tích rộng lớn nằm giữa vùng Đồng Tháp Mười, hội tụ nhiều tầng giá trị: khảo cổ, lịch sử và tâm linh. Về khảo cổ, đây là một trong những trung tâm quan trọng của nền văn hóa Óc Eo – vương quốc Phù Nam cổ tồn tại cách nay khoảng 1.500–2.000 năm; các nhà khảo cổ đã phát hiện nền móng đền tháp bằng gạch, tượng thần, linh vật và nhiều hiện vật bằng vàng, đá quý, chứng minh nơi đây từng là một thánh địa sầm uất. Về lịch sử cận đại, Gò Tháp gắn với cuộc kháng chiến chống Pháp: đây từng là đại bản doanh của hai vị anh hùng Thiên Hộ Dương (Võ Duy Dương) và Đốc Binh Kiều giữa thế kỷ 19, nay có đền thờ tưởng niệm hai ông. Về tâm linh, khu di tích còn có miếu Bà Chúa Xứ và tổ chức các kỳ lễ hội lớn thu hút hàng vạn người hành hương mỗi năm. Bao quanh các gò đất cổ là cảnh quan đồng bưng, rừng tràm, sen súng đặc trưng của Đồng Tháp Mười. Với những giá trị nổi bật, Gò Tháp đã được xếp hạng Di tích Quốc gia đặc biệt. Du khách đến đây vừa tìm hiểu chiều sâu văn hóa – lịch sử hàng nghìn năm, vừa viếng đền, trẩy hội và tận hưởng không gian thiên nhiên yên bình của miền Tây.",
    "presentation_long_en": "Go Thap is a large relic complex in the heart of the Plain of Reeds, bringing together layers of archaeological, historical and spiritual value. Archaeologically, it is one of the important centres of the Oc Eo culture — the ancient kingdom of Funan that flourished some 1,500–2,000 years ago; archaeologists have uncovered brick temple foundations, statues of deities, sacred figures and many artefacts of gold and precious stone, proving it was once a thriving holy site. In modern history, Go Thap is tied to the resistance against the French: it served as the headquarters of two heroes, Thien Ho Duong (Vo Duy Duong) and Doc Binh Kieu, in the mid-19th century, and temples now honour them. Spiritually, the site also has the Ba Chua Xu shrine and hosts major festivals that draw tens of thousands of pilgrims each year. The ancient earthen mounds are surrounded by the marshes, cajuput forest and lotus typical of the Plain of Reeds. For its outstanding values, Go Thap has been ranked a Special National Relic. Visitors come to explore thousands of years of cultural and historical depth, to worship at the temples, join the festivals and enjoy the peaceful natural setting of the western delta.",
    "presentation_long_ru": "Готхап — обширный комплекс памятников в сердце Тростниковой равнины, соединяющий пласты археологической, исторической и духовной ценности. В археологическом плане это один из важных центров культуры Окео — древнего царства Фунан, процветавшего около 1500–2000 лет назад; археологи обнаружили кирпичные основания храмов, статуи божеств, священные фигуры и множество изделий из золота и драгоценного камня, доказывающих, что здесь некогда было оживлённое святилище. В новой истории Готхап связан с сопротивлением французам: в середине XIX века он служил ставкой двух героев — Тхьен Хо Зыонга (Во Зуй Зыонга) и Док Бинь Кьеу, которым ныне посвящены храмы. В духовном отношении на территории есть и святилище Ба Тюа Сы, где ежегодно проходят крупные праздники, собирающие десятки тысяч паломников. Древние земляные холмы окружены болотами, каюпутовым лесом и лотосами, характерными для Тростниковой равнины. За выдающиеся ценности Готхап отнесён к особым национальным памятникам. Гости приезжают, чтобы прикоснуться к тысячелетней культурно-исторической глубине, помолиться в храмах, принять участие в праздниках и насладиться мирной природой западной дельты.",
    "highlights_vi": [
      "Trung tâm văn hóa Óc Eo – Phù Nam cổ (~1.500–2.000 năm), nhiều cổ vật vàng, đá quý",
      "Đền thờ anh hùng Thiên Hộ Dương, Đốc Binh Kiều và miếu Bà Chúa Xứ",
      "Di tích Quốc gia đặc biệt giữa cảnh quan Đồng Tháp Mười"
    ],
    "highlights_en": [
      "A centre of the ancient Oc Eo–Funan culture (~1,500–2,000 years), with gold and gem artefacts",
      "Temples to heroes Thien Ho Duong and Doc Binh Kieu, and the Ba Chua Xu shrine",
      "A Special National Relic amid the Plain of Reeds landscape"
    ],
    "highlights_ru": [
      "Центр древней культуры Окео–Фунан (~1500–2000 лет) с золотыми и самоцветными артефактами",
      "Храмы героям Тхьен Хо Зыонгу и Док Бинь Кьеу и святилище Ба Тюа Сы",
      "Особый национальный памятник среди пейзажа Тростниковой равнины"
    ],
    "practical": {
      "hours_vi": "Khoảng 7:00–17:00 hằng ngày.",
      "ticket_vi": "Vé tham quan cơ bản thấp/miễn phí; lễ hội đông vào các kỳ chính.",
      "duration_vi": "Khoảng 1,5–2 giờ.",
      "best_time_vi": "Mùa lễ hội (rằm tháng 3 và rằm tháng 11 âm lịch); mùa khô đi lại thuận tiện.",
      "tips_vi": "Nên thuê thuyết minh để hiểu văn hóa Óc Eo; giữ trang nghiêm ở đền miếu; mang chống nắng."
    },
    "photo": None,
    "photo_credit": None,
    "official_site": None,
    "sources": [
      {"title": "Wikipedia (VI) — Gò Tháp", "url": "https://vi.wikipedia.org/wiki/G%C3%B2_Th%C3%A1p"}
    ],
    "tags": ["history", "archaeology", "monument", "temple", "culture", "outdoor"],
    "status": "enriched",
    "last_updated": TODAY
  },
]

# <<INSERT_MARKER>>

# ===================== LOGIC CHÈN =====================
def main():
    byreg = defaultdict(list)
    for p in PLACES:
        byreg[p["region"]].append(p)

    grand_added = 0
    for region, recs in byreg.items():
        path = os.path.join(REGIONS, region + ".json")
        data = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
        if not isinstance(data, list):
            print(f"  ! {region}: nội dung không phải mảng, bỏ qua"); continue
        have = {r.get("slug") for r in data}
        if os.path.exists(path) and data:
            bak = path + ".bak_add_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            shutil.copy(path, bak)
        added = 0
        for r in recs:
            if r["slug"] in have:
                print(f"    - bỏ qua trùng slug: {region}/{r['slug']}"); continue
            r["maps"] = maps_for(r, region)
            data.append(r); have.add(r["slug"]); added += 1
        json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        grand_added += added
        print(f"  + {region}: thêm {added}, hiện có {len(data)}")
    print(f"TỔNG cộng thêm {grand_added} địa điểm vào {len(byreg)} tỉnh/thành.")


if __name__ == "__main__":
    main()
