# -*- coding: utf-8 -*-
"""_add_vn_dak_lak_batch_20260727.py
Bổ sung địa điểm du lịch nổi tiếng của tỉnh ĐẮK LẮK (đơn vị MỚI sau sáp nhập
1/7/2025, gồm Đắk Lắk cũ + Phú Yên cũ; tỉnh lỵ Buôn Ma Thuột). Chèn an toàn:
nạp -> append -> ghi; bỏ qua slug đã có. Toạ độ THẬT; đủ VI/EN/RU.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
f = os.path.join(ROOT, "data", "regions", "vn-dak-lak.json")
d = json.load(open(f, encoding="utf-8")) if os.path.exists(f) else []
have = {p["slug"] for p in d}


def R(slug, name_vi, name_ru, name_en, cats, lat, lon, addr, fields):
    base = dict(
        id="vn-dak-lak-" + slug, slug=slug, region="vn-dak-lak", country="vietnam",
        region_name_vi="Đắk Lắk", federal_district="Miền Trung",
        name_vi=name_vi, name_ru=name_ru, name_en=name_en, categories=cats,
        coordinates={"lat": lat, "lon": lon}, address_vi=addr,
        photo=None, photo_credit=None, status="enriched", last_updated="2026-07-27",
    )
    base.update(fields)
    return base


new = []

# ============================ TÂY NGUYÊN — ĐẮK LẮK CŨ ============================

new += [
R("yok-don", "Vườn quốc gia Yok Đôn", "Национальный парк Йокдон", "Yok Don National Park",
  ["park_garden", "other"], 12.899, 107.788,
  "Xã Krông Na (khu vực Buôn Đôn), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Vườn quốc gia Yok Đôn ở khu vực Buôn Đôn là vườn quốc gia lớn nhất Việt Nam, rộng hơn 115.000 ha rừng khộp đặc trưng của Tây Nguyên. Nơi đây bảo tồn voi rừng, bò tót cùng hàng trăm loài chim thú và nổi tiếng với các tour 'thân thiện với voi' thay cho cưỡi voi. Dòng sông Sêrêpốk uốn lượn qua rừng tạo nên khung cảnh hoang sơ hiếm có.",
  "presentation_short_en": "Yok Don National Park, near Buôn Đôn, is the largest national park in Vietnam, protecting over 115,000 hectares of the region's distinctive dry dipterocarp (khộp) forest. It shelters wild elephants, gaur and hundreds of bird and mammal species, and is known for pioneering 'elephant-friendly' tours instead of elephant riding. The Serepok River winds through the reserve, creating a rare, untamed landscape.",
  "presentation_short_ru": "Национальный парк Йокдон близ Буондона — крупнейший национальный парк Вьетнама, охраняющий более 115 000 гектаров характерного для нагорья сухого диптерокарпового леса (кхоп). Здесь обитают дикие слоны, гауры и сотни видов птиц и млекопитающих, а сам парк известен «дружественными к слонам» турами вместо катания на слонах. Через заповедник петляет река Серепок, создавая редкий по красоте первозданный пейзаж.",
  "presentation_long_vi": "Trải rộng trên địa bàn Buôn Đôn và Ea Súp, Vườn quốc gia Yok Đôn là khu bảo tồn lớn nhất Việt Nam với hơn 115.000 ha, được đặt tên theo ngọn núi Yok Đôn giữa rừng. Điều làm nên bản sắc của Yok Đôn là kiểu rừng khộp — rừng cây họ dầu rụng lá theo mùa, mùa khô trơ cành xám bạc, mùa mưa lại xanh mướt — một hệ sinh thái hiếm gặp ở Đông Nam Á. Rừng là mái nhà của voi rừng, bò tót, nai, hàng trăm loài chim và nhiều loài quý hiếm trong Sách Đỏ. Dòng Sêrêpốk chảy ngược lên phía bắc len lỏi qua rừng, tạo những ghềnh thác và bãi bồi tuyệt đẹp. Du khách đến đây có thể đi bộ xuyên rừng cùng kiểm lâm, đạp xe, chèo thuyền và đặc biệt tham gia mô hình 'du lịch thân thiện với voi': đi bộ theo dõi đàn voi được thả tự do kiếm ăn thay vì cưỡi voi, một hướng bảo tồn nhân văn được quốc tế đánh giá cao. Vùng đệm còn gắn với văn hóa của người M'nông, Ê Đê và nghề thuần dưỡng voi lừng danh của Bản Đôn, khiến chuyến đi vừa là hành trình thiên nhiên vừa là trải nghiệm văn hóa.",
  "presentation_long_en": "Spanning the Buôn Đôn and Ea Súp areas, Yok Don National Park is Vietnam's largest protected reserve at more than 115,000 hectares, named after Yok Don mountain rising from the forest. Its defining feature is the khộp forest — a dry dipterocarp woodland that sheds its leaves in the dry season, turning silvery and bare, then greening again with the rains — a rare ecosystem in Southeast Asia. The forest is home to wild elephants, gaur, deer, hundreds of bird species and many rare animals listed in the Red Book. The Serepok, one of the few rivers that flows northward, threads through the park, forming beautiful rapids and sandbars. Visitors can trek with rangers, cycle, go rafting, and above all join the park's celebrated 'elephant-friendly tourism': walking to observe elephants roaming freely as they forage, rather than riding them — a humane conservation model praised internationally. The buffer zone is tied to the culture of the M'nông and Ê Đê peoples and to the legendary elephant-taming traditions of Bản Đôn, making a visit both a wildlife journey and a cultural encounter.",
  "presentation_long_ru": "Раскинувшийся в районах Буондон и Еашуп национальный парк Йокдон — крупнейший заповедник Вьетнама площадью более 115 000 гектаров, названный по горе Йокдон, поднимающейся среди леса. Его главная особенность — лес кхоп, сухой диптерокарповый лес, сбрасывающий листву в засушливый сезон и снова зеленеющий с дождями; такая экосистема редка для Юго-Восточной Азии. В лесу живут дикие слоны, гауры, олени, сотни видов птиц и многие редкие животные из Красной книги. Через парк течёт Серепок — одна из немногих рек, текущих на север, — образуя живописные пороги и отмели. Гости могут отправиться в поход с рейнджерами, покататься на велосипеде, сплавиться по реке и, главное, присоединиться к знаменитым «дружественным к слонам» турам: вместо катания туристы пешком наблюдают за слонами, свободно кормящимися в лесу, — гуманная модель охраны природы, получившая международное признание. Буферная зона связана с культурой народов мнонг и эде и легендарными традициями приручения слонов в Бандоне, поэтому поездка становится одновременно и путешествием к дикой природе, и знакомством с культурой.",
  "highlights_vi": [
    "Vườn quốc gia lớn nhất Việt Nam (hơn 115.000 ha) với rừng khộp rụng lá đặc trưng Tây Nguyên",
    "Mô hình 'du lịch thân thiện với voi' — quan sát voi tự do thay vì cưỡi voi",
    "Dòng Sêrêpốk chảy ngược về phía bắc và văn hóa thuần voi của Bản Đôn"],
  "highlights_en": [
    "Vietnam's largest national park (over 115,000 ha) with the Central Highlands' signature khộp forest",
    "'Elephant-friendly' tourism — watching elephants roam free instead of riding them",
    "The northward-flowing Serepok River and the elephant-taming heritage of Bản Đôn"],
  "highlights_ru": [
    "Крупнейший национальный парк Вьетнама (более 115 000 га) с характерным лесом кхоп",
    "«Дружественный к слонам» туризм — наблюдение за свободными слонами вместо катания",
    "Текущая на север река Серепок и традиции приручения слонов в Бандоне"],
  "practical": {
    "hours_vi": "Ban ngày; tour rừng nên đặt trước và đi cùng kiểm lâm/hướng dẫn.",
    "ticket_vi": "Vé vào cổng và phí tour thay đổi theo loại hình (đi bộ, đạp xe, xem voi); tham khảo tại trung tâm du lịch của vườn.",
    "duration_vi": "Nửa ngày đến 2 ngày (có tour nghỉ đêm trong rừng).",
    "best_time_vi": "Mùa khô (khoảng tháng 11–4) thuận tiện đi rừng và ngắm thú.",
    "tips_vi": "Mang giày đi rừng, nước, chống côn trùng; ưu tiên tour xem voi tự do; tôn trọng quy định bảo tồn."},
  "rating": {"value": 4.5, "count": 3200, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Du khách ấn tượng với rừng khộp hoang sơ và trải nghiệm ngắm voi tự do đầy nhân văn; nhiều người khen hướng dẫn viên tâm huyết. Một số lưu ý đường trong rừng còn hoang, nên đặt tour trước và chuẩn bị thể lực.",
  "tags": ["nature", "outdoor", "wildlife", "elephant", "daytrip", "top"],
  "sources": [
    {"title": "Wikipedia (EN) — Yok Don National Park", "url": "https://en.wikipedia.org/wiki/Yok_%C4%90%C3%B4n_National_Park"},
    {"title": "Wikipedia (VI) — Vườn quốc gia Yok Đôn", "url": "https://vi.wikipedia.org/wiki/V%C6%B0%E1%BB%9Dn_qu%E1%BB%91c_gia_Yok_%C4%90%C3%B4n"}]}),

R("chu-yang-sin", "Vườn quốc gia Chư Yang Sin", "Национальный парк Чуянгшин", "Chu Yang Sin National Park",
  ["park_garden", "other"], 12.42, 108.35,
  "Xã Krông Bông và Lắk (khu vực cũ), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Vườn quốc gia Chư Yang Sin bao quanh đỉnh Chư Yang Sin cao 2.442 m — nóc nhà của Đắk Lắk. Đây là vùng rừng nguyên sinh rộng lớn với suối thác, thông và đỗ quyên, là điểm đến ưa thích của dân trekking và người yêu thiên nhiên. Vườn bảo tồn nhiều loài đặc hữu và là đầu nguồn của nhiều dòng sông Tây Nguyên.",
  "presentation_short_en": "Chu Yang Sin National Park surrounds the 2,442 m Chu Yang Sin peak — the roof of Đắk Lắk. It is a vast expanse of primary forest with streams, waterfalls, pines and rhododendrons, a favourite of trekkers and nature lovers. The park protects many endemic species and is the source of several Central Highlands rivers.",
  "presentation_short_ru": "Национальный парк Чуянгшин раскинулся вокруг вершины Чуянгшин высотой 2442 м — «крыши» провинции Даклак. Это обширный первичный лес с ручьями, водопадами, соснами и рододендронами, любимый треккерами и любителями природы. Парк охраняет множество эндемичных видов и служит истоком нескольких рек нагорья.",
  "presentation_long_vi": "Nằm ở phía nam Đắk Lắk, Vườn quốc gia Chư Yang Sin được thành lập năm 2002, lấy tên theo đỉnh Chư Yang Sin cao 2.442 m — ngọn núi cao nhất tỉnh và là một trong những đỉnh cao của Tây Nguyên. Vườn trải trên địa hình núi non hiểm trở với nhiều đai khí hậu, nhờ đó hội tụ hệ thực vật phong phú: rừng thường xanh, rừng hỗn giao, những rừng thông và cả những vạt đỗ quyên nở rực trên cao. Đây là nơi cư trú của nhiều loài thú lớn, linh trưởng và hàng trăm loài chim, trong đó có các loài đặc hữu và quý hiếm. Với dân đi rừng, chinh phục đỉnh Chư Yang Sin là một trong những cung trekking đáng nhớ nhất miền Trung: băng qua suối, ngủ lều giữa rừng già, đón bình minh trên biển mây. Vườn còn giữ vai trò phòng hộ đầu nguồn cho các dòng sông chảy về đồng bằng, gắn bó mật thiết với đời sống của cộng đồng Ê Đê, M'nông quanh vùng. Một chuyến đi Chư Yang Sin đòi hỏi thể lực và sự chuẩn bị kỹ, nhưng bù lại là thiên nhiên nguyên sơ gần như chưa bị con người tác động.",
  "presentation_long_en": "In the south of Đắk Lắk, Chu Yang Sin National Park was established in 2002 and named after the 2,442 m Chu Yang Sin peak — the highest mountain in the province and one of the highest in the Central Highlands. The park covers rugged terrain spanning several climatic belts, giving it a rich flora: evergreen and mixed forests, stands of pine and even rhododendrons blooming at altitude. It shelters many large mammals, primates and hundreds of bird species, including endemic and endangered ones. For hikers, conquering Chu Yang Sin is one of central Vietnam's most memorable treks: crossing streams, camping in old-growth forest and greeting the dawn above a sea of clouds. The park also serves as a watershed protecting the rivers that flow to the lowlands, and is closely bound to the lives of the Ê Đê and M'nông communities nearby. A trip to Chu Yang Sin demands fitness and careful preparation, but rewards visitors with wild nature almost untouched by human hands.",
  "presentation_long_ru": "На юге провинции Даклак национальный парк Чуянгшин был создан в 2002 году и назван в честь вершины Чуянгшин высотой 2442 м — самой высокой горы провинции и одной из высочайших в нагорье. Парк занимает труднодоступную местность, охватывающую несколько климатических поясов, что обеспечивает богатую флору: вечнозелёные и смешанные леса, сосновые рощи и даже рододендроны, цветущие на высоте. Здесь обитают многие крупные млекопитающие, приматы и сотни видов птиц, в том числе эндемичные и редкие. Для любителей походов покорение Чуянгшина — один из самых запоминающихся треков центрального Вьетнама: переправы через ручьи, ночёвки в реликтовом лесу и встреча рассвета над морем облаков. Парк также выполняет водоохранную роль, защищая реки, текущие на равнины, и тесно связан с жизнью соседних общин эде и мнонг. Путешествие в Чуянгшин требует хорошей физической формы и тщательной подготовки, но вознаграждает первозданной природой, почти не тронутой человеком.",
  "highlights_vi": [
    "Bao quanh đỉnh Chư Yang Sin 2.442 m — ngọn núi cao nhất Đắk Lắk",
    "Rừng nguyên sinh nhiều đai khí hậu, có thông và đỗ quyên trên cao",
    "Cung trekking và săn mây nổi tiếng, đầu nguồn nhiều sông Tây Nguyên"],
  "highlights_en": [
    "Surrounds the 2,442 m Chu Yang Sin peak — the highest in Đắk Lắk",
    "Primary forest across several climatic belts, with highland pines and rhododendrons",
    "A famous trekking and cloud-hunting route and the source of Central Highlands rivers"],
  "highlights_ru": [
    "Окружает вершину Чуянгшин 2442 м — высшую точку Даклака",
    "Первичный лес нескольких климатических поясов, сосны и рододендроны на высоте",
    "Знаменитый трек и «охота за облаками», исток рек нагорья"],
  "practical": {
    "hours_vi": "Đi trong ngày hoặc tour nhiều ngày; cần đăng ký và có hướng dẫn của vườn.",
    "ticket_vi": "Phí tham quan và dịch vụ hướng dẫn/porter theo quy định của vườn.",
    "duration_vi": "Trek đỉnh thường 2 ngày 1 đêm.",
    "best_time_vi": "Mùa khô (tháng 12–4); tránh mùa mưa trơn trượt.",
    "tips_vi": "Cần thể lực tốt, giày trek, lều túi ngủ; đi theo đoàn có hướng dẫn bản địa."},
  "rating": {"value": 4.6, "count": 900, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Dân trekking đánh giá cao rừng già nguyên sơ và cảnh săn mây trên đỉnh; nhấn mạnh cần chuẩn bị kỹ và đi cùng người bản địa. Ít dịch vụ tiện nghi nên phù hợp người thích khám phá.",
  "tags": ["nature", "outdoor", "trekking", "viewpoint", "mountain"],
  "sources": [
    {"title": "Wikipedia (EN) — Chư Yang Sin National Park", "url": "https://en.wikipedia.org/wiki/Ch%C6%B0_Yang_Sin_National_Park"},
    {"title": "Wikipedia (VI) — Vườn quốc gia Chư Yang Sin", "url": "https://vi.wikipedia.org/wiki/V%C6%B0%E1%BB%9Dn_qu%E1%BB%91c_gia_Ch%C6%B0_Yang_Sin"}]}),
]

new += [
R("bao-tang-dak-lak", "Bảo tàng Đắk Lắk", "Музей Даклака", "Dak Lak Museum",
  ["museum"], 12.6659, 108.0466,
  "Số 12 Lê Duẩn, khu vực Buôn Ma Thuột, tỉnh Đắk Lắk", {
  "presentation_short_vi": "Bảo tàng Đắk Lắk ở trung tâm Buôn Ma Thuột là một trong những bảo tàng dân tộc học đặc sắc nhất Tây Nguyên. Tòa nhà lấy cảm hứng từ nhà dài Ê Đê, trưng bày về đa dạng sinh học, lịch sử và văn hóa của gần 50 tộc người sinh sống trên vùng đất này. Nhiều nội dung được chú thích bằng bốn thứ tiếng: Việt, Anh, Pháp và Ê Đê.",
  "presentation_short_en": "The Dak Lak Museum in central Buôn Ma Thuột is one of the finest ethnographic museums in the Central Highlands. Its building echoes the Ê Đê longhouse and presents the biodiversity, history and culture of the nearly fifty ethnic groups who live here. Many labels are given in four languages: Vietnamese, English, French and Ê Đê.",
  "presentation_short_ru": "Музей Даклака в центре Буонматхуота — один из лучших этнографических музеев нагорья. Здание напоминает длинный дом народа эде и рассказывает о биоразнообразии, истории и культуре почти пятидесяти этнических групп, живущих в этом крае. Многие подписи даны на четырёх языках: вьетнамском, английском, французском и эде.",
  "presentation_long_vi": "Khánh thành năm 2011 trong khuôn viên rợp bóng cây cổ thụ từng thuộc Biệt điện Bảo Đại, Bảo tàng Đắk Lắk là điểm đến hàng đầu để hiểu về vùng đất và con người Tây Nguyên. Kiến trúc bảo tàng cách điệu từ mái nhà dài truyền thống của người Ê Đê, hài hòa giữa hiện đại và bản sắc. Không gian trưng bày chia thành ba chủ đề lớn: đa dạng sinh học, văn hóa dân tộc và lịch sử. Du khách được chiêm ngưỡng bộ sưu tập cồng chiêng, ghế Kpan, trang phục thổ cẩm, thuyền độc mộc, nông cụ, nhạc cụ và hiện vật gắn với nghề thuần voi cùng đời sống buôn làng của người Ê Đê, M'nông, Gia Rai và nhiều tộc người khác. Nhiều nội dung được thuyết minh bằng bốn ngôn ngữ Việt, Anh, Pháp và Ê Đê — một điểm rất hiếm, thể hiện sự tôn trọng tiếng nói bản địa. Phần lịch sử tái hiện hai cuộc kháng chiến và chiến thắng Buôn Ma Thuột 1975. Nằm ngay trung tâm thành phố, gần Biệt điện Bảo Đại và các quán cà phê, bảo tàng là nơi lý tưởng để bắt đầu hành trình khám phá 'thủ phủ cà phê' và văn hóa cồng chiêng đã được UNESCO vinh danh.",
  "presentation_long_en": "Opened in 2011 in a shady, tree-filled compound that once belonged to the Bao Dai Palace, the Dak Lak Museum is the best place to understand the land and peoples of the Central Highlands. Its architecture reinterprets the traditional Ê Đê longhouse, blending modernity with local identity. The displays are arranged around three themes: biodiversity, ethnic culture and history. Visitors can admire collections of gongs, Kpan benches, brocade costumes, dugout canoes, farming tools, musical instruments and objects tied to elephant-taming and village life among the Ê Đê, M'nông, Gia Rai and other groups. Much of the interpretation appears in four languages — Vietnamese, English, French and Ê Đê — a rare touch that honours the indigenous tongue. The history section recounts the two wars of resistance and the 1975 liberation of Buôn Ma Thuột. Standing in the city centre, close to the Bao Dai Palace and the local cafés, the museum is an ideal starting point for exploring Vietnam's 'coffee capital' and the gong culture recognised by UNESCO.",
  "presentation_long_ru": "Открытый в 2011 году в тенистом парке со старыми деревьями, некогда принадлежавшем дворцу Бао Дая, Музей Даклака — лучшее место, чтобы понять землю и народы Центрального нагорья. Его архитектура переосмысливает традиционный длинный дом эде, сочетая современность и местную самобытность. Экспозиция построена вокруг трёх тем: биоразнообразие, этническая культура и история. Посетители видят коллекции гонгов, скамей кпан, парчовых костюмов, лодок-долблёнок, сельских орудий, музыкальных инструментов и предметов, связанных с приручением слонов и жизнью деревень народов эде, мнонг, зярай и других. Значительная часть подписей дана на четырёх языках — вьетнамском, английском, французском и эде, — что редкость и выражает уважение к языку коренных народов. Исторический раздел рассказывает о двух войнах сопротивления и освобождении Буонматхуота в 1975 году. Расположенный в центре города, рядом с дворцом Бао Дая и кофейнями, музей — идеальная отправная точка для знакомства с «кофейной столицей» Вьетнама и культурой гонгов, признанной ЮНЕСКО.",
  "highlights_vi": [
    "Kiến trúc lấy cảm hứng từ nhà dài Ê Đê, ba chủ đề: sinh thái – văn hóa – lịch sử",
    "Chú thích bốn thứ tiếng Việt, Anh, Pháp và Ê Đê — rất hiếm gặp",
    "Nằm trong khuôn viên Biệt điện Bảo Đại, giữa trung tâm Buôn Ma Thuột"],
  "highlights_en": [
    "Architecture inspired by the Ê Đê longhouse; three themes: ecology, culture, history",
    "Labels in four languages — Vietnamese, English, French and Ê Đê — a rare feature",
    "Set within the Bao Dai Palace grounds in the heart of Buôn Ma Thuột"],
  "highlights_ru": [
    "Архитектура в духе длинного дома эде; три темы: экология, культура, история",
    "Подписи на четырёх языках — вьетнамском, английском, французском и эде",
    "Расположен в парке дворца Бао Дая в центре Буонматхуота"],
  "practical": {
    "hours_vi": "Thường mở khoảng 7:30–11:30 và 13:30–17:00 (nên kiểm tra lại).",
    "ticket_vi": "Vé tham quan khoảng 20.000–30.000 VND/người; giá có thể thay đổi.",
    "duration_vi": "Khoảng 1–1,5 giờ.",
    "best_time_vi": "Quanh năm; kết hợp tham quan Biệt điện Bảo Đại kế bên.",
    "tips_vi": "Đi cùng thuyết minh để hiểu sâu văn hóa cồng chiêng; kết hợp thưởng cà phê gần đó."},
  "rating": {"value": 4.4, "count": 2100, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách khen trưng bày khoa học, mát mẻ và giàu thông tin về các dân tộc Tây Nguyên; thích chú thích đa ngữ. Vài ý kiến mong có thêm hoạt động tương tác.",
  "tags": ["museum", "culture", "indoor", "family", "history"],
  "sources": [
    {"title": "Wikipedia (VI) — Bảo tàng Đắk Lắk", "url": "https://vi.wikipedia.org/wiki/B%E1%BA%A3o_t%C3%A0ng_%C4%90%E1%BA%AFk_L%E1%BA%AFk"}]}),

R("biet-dien-bao-dai", "Biệt điện Bảo Đại (Buôn Ma Thuột)", "Дворец Бао Дая (Буонматхуот)", "Bao Dai Palace (Buon Ma Thuot)",
  ["palace", "museum"], 12.6669, 108.0490,
  "Số 02 Y Ngông, khu vực Buôn Ma Thuột, tỉnh Đắk Lắk", {
  "presentation_short_vi": "Biệt điện Bảo Đại ở Buôn Ma Thuột là dinh thự từng là nơi nghỉ và làm việc của vị vua cuối cùng triều Nguyễn khi lên Tây Nguyên. Tòa nhà mang phong cách kết hợp Pháp và bản địa, nằm giữa khuôn viên rợp bóng cổ thụ và những cây long não trăm tuổi. Đây là di tích lịch sử được nhiều du khách ghé thăm khi đến 'thủ phủ cà phê'.",
  "presentation_short_en": "The Bao Dai Palace in Buôn Ma Thuột is a mansion that once served as the residence and workplace of the last Nguyễn emperor during his stays in the Central Highlands. The building mixes French and local styles and sits amid a compound shaded by ancient trees and century-old camphor laurels. It is a historic site popular with visitors to the 'coffee capital'.",
  "presentation_short_ru": "Дворец Бао Дая в Буонматхуоте — особняк, служивший резиденцией и рабочим местом последнего императора династии Нгуен во время его приездов в нагорье. Здание сочетает французский и местный стили и стоит среди парка, затенённого старыми деревьями и столетними камфорными лаврами. Это историческое место, популярное у гостей «кофейной столицы».",
  "presentation_long_vi": "Nằm ngay trung tâm Buôn Ma Thuột, Biệt điện Bảo Đại nguyên là tòa nhà của công sứ Pháp, sau được vua Bảo Đại — vị hoàng đế cuối cùng của triều Nguyễn — sử dụng làm nơi nghỉ ngơi, săn bắn và làm việc mỗi khi lên cao nguyên. Công trình một tầng mang đường nét kiến trúc Pháp pha lẫn yếu tố bản địa, mái ngói, hành lang rộng, tọa lạc trong khuôn viên xanh mát với những cây long não, cây cổ thụ hàng trăm năm tuổi. Bên trong còn lưu giữ nội thất, hình ảnh, tư liệu về cuộc đời Bảo Đại và mối liên hệ của ông với vùng đất Tây Nguyên, cùng những hiện vật gắn với văn hóa các dân tộc bản địa. Nơi đây từng chứng kiến nhiều sự kiện lịch sử quan trọng và nay là di tích cấp quốc gia. Khuôn viên biệt điện liền kề Bảo tàng Đắk Lắk, tạo thành một quần thể tham quan lý tưởng ngay giữa lòng thành phố: du khách có thể tản bộ dưới tán cổ thụ, tìm hiểu lịch sử rồi ghé những quán cà phê nổi tiếng gần đó. Với vẻ trầm mặc, cổ kính, biệt điện là một điểm dừng chân giàu chiều sâu văn hóa và lịch sử của Buôn Ma Thuột.",
  "presentation_long_en": "In the centre of Buôn Ma Thuột, the Bao Dai Palace was originally the residence of the French résident, later used by Emperor Bảo Đại — the last Nguyễn monarch — as a place to rest, hunt and work whenever he came up to the highlands. The single-storey building blends French architecture with local touches: a tiled roof, wide verandas, set in a cool green compound of camphor laurels and trees that are centuries old. Inside are preserved furnishings, photographs and documents about Bảo Đại's life and his ties to the Central Highlands, together with objects from the cultures of the local peoples. The site witnessed many important historical events and is now a national relic. The palace grounds adjoin the Dak Lak Museum, forming an ideal sightseeing ensemble right in the city: visitors can stroll beneath the old trees, learn the history, then drop into the famous cafés nearby. Quiet and stately, the palace is a stop rich in the culture and history of Buôn Ma Thuột.",
  "presentation_long_ru": "В центре Буонматхуота дворец Бао Дая изначально был резиденцией французского резидента, а позже император Бао Дай — последний монарх династии Нгуен — использовал его для отдыха, охоты и работы во время приездов в нагорье. Одноэтажное здание сочетает французскую архитектуру с местными чертами: черепичная крыша, широкие веранды, прохладный зелёный парк с камфорными лаврами и вековыми деревьями. Внутри сохранены мебель, фотографии и документы о жизни Бао Дая и его связях с нагорьем, а также предметы культуры местных народов. Это место видело немало важных исторических событий и ныне является памятником национального значения. Территория дворца примыкает к Музею Даклака, образуя удобный экскурсионный ансамбль прямо в городе: можно прогуляться под старыми деревьями, узнать историю, а затем заглянуть в знаменитые кофейни поблизости. Тихий и величавый, дворец — остановка, богатая культурой и историей Буонматхуота.",
  "highlights_vi": [
    "Dinh thự gắn với vua Bảo Đại — hoàng đế cuối cùng triều Nguyễn — trên đất Tây Nguyên",
    "Kiến trúc Pháp pha bản địa giữa khuôn viên long não, cổ thụ trăm tuổi",
    "Di tích quốc gia, liền kề Bảo tàng Đắk Lắk ở trung tâm thành phố"],
  "highlights_en": [
    "A mansion linked to Emperor Bảo Đại, the last Nguyễn monarch, in the highlands",
    "French-and-local architecture amid a compound of century-old camphor trees",
    "A national relic adjoining the Dak Lak Museum in the city centre"],
  "highlights_ru": [
    "Особняк, связанный с императором Бао Даем — последним монархом Нгуенов",
    "Французско-местная архитектура среди вековых камфорных деревьев",
    "Памятник национального значения рядом с Музеем Даклака в центре города"],
  "practical": {
    "hours_vi": "Thường mở cửa ban ngày (nên kiểm tra lại giờ mở).",
    "ticket_vi": "Vé tham quan tượng trưng; giá có thể thay đổi.",
    "duration_vi": "Khoảng 45–60 phút.",
    "best_time_vi": "Buổi sáng mát; kết hợp Bảo tàng Đắk Lắk kế bên.",
    "tips_vi": "Đi bộ dưới tán long não rất dễ chịu; kết hợp tham quan bảo tàng và cà phê gần đó."},
  "rating": {"value": 4.3, "count": 1500, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Du khách thích không gian yên tĩnh, cổ kính và những hàng long não mát rượi; hiện vật gợi nhiều câu chuyện lịch sử. Một số mong nội thất được phục dựng đầy đủ hơn.",
  "tags": ["history", "palace", "indoor", "outdoor", "family"],
  "sources": [
    {"title": "Wikipedia (VI) — Biệt điện Bảo Đại (Buôn Ma Thuột)", "url": "https://vi.wikipedia.org/wiki/Bi%E1%BB%87t_%C4%91i%E1%BB%87n_B%E1%BA%A3o_%C4%90%E1%BA%A1i"}]}),

R("chua-khai-doan", "Chùa Sắc tứ Khải Đoan", "Пагода Кхайдоан", "Khai Doan Pagoda",
  ["church"], 12.664, 108.0489,
  "Số 117 Phan Bội Châu, khu vực Buôn Ma Thuột, tỉnh Đắk Lắk", {
  "presentation_short_vi": "Chùa Sắc tứ Khải Đoan là ngôi chùa lớn và nổi tiếng nhất Buôn Ma Thuột, cũng là ngôi chùa cuối cùng được triều Nguyễn ban 'sắc tứ'. Kiến trúc chùa độc đáo khi kết hợp lối nhà rường cung đình Huế với dáng nhà dài Ê Đê. Tên chùa ghép từ vua Khải Định và Hoàng thái hậu Đoan Huy.",
  "presentation_short_en": "Khai Doan Pagoda is the largest and most famous temple in Buôn Ma Thuột, and the last pagoda ever granted a royal 'sắc tứ' title by the Nguyễn dynasty. Its architecture uniquely blends the wooden royal style of Huế with the form of the Ê Đê longhouse. Its name combines Emperor Khải Định and Queen Mother Đoan Huy.",
  "presentation_short_ru": "Пагода Кхайдоан — самый большой и знаменитый храм Буонматхуота и последняя пагода, получившая королевский титул «сакты» от династии Нгуен. Её архитектура уникально соединяет деревянный дворцовый стиль Хюэ с формой длинного дома народа эде. Название сложено из имён императора Кхайдиня и вдовствующей императрицы Доанзюй.",
  "presentation_long_vi": "Tọa lạc trên đường Phan Bội Châu giữa lòng Buôn Ma Thuột, chùa Sắc tứ Khải Đoan được khởi dựng năm 1951 dưới sự bảo trợ của Hoàng thái hậu Đoan Huy (Từ Cung) — thân mẫu vua Bảo Đại. Tên chùa ghép từ chữ 'Khải' của vua Khải Định và 'Đoan' của bà Đoan Huy, và đây được xem là ngôi chùa cuối cùng được nhà Nguyễn phong 'sắc tứ'. Điểm đặc sắc của chùa nằm ở kiến trúc giao thoa: chính điện dựng theo lối nhà rường ba gian cung đình Huế với cột gỗ, chạm khắc tinh xảo, mái cong; nhưng phần sau lại kéo dài theo dáng nhà dài của người Ê Đê, thể hiện sự hòa quyện giữa Phật giáo với văn hóa Tây Nguyên. Trong khuôn viên có tượng Phật, chuông đồng lớn, vườn cây và tượng Quán Thế Âm thanh tịnh. Là trung tâm sinh hoạt Phật giáo lớn nhất tỉnh, chùa đặc biệt đông đúc vào các dịp lễ Phật đản, Vu lan và Tết. Với du khách, Khải Đoan không chỉ là nơi chiêm bái mà còn là điểm đến để cảm nhận sự gặp gỡ độc đáo giữa mỹ thuật cung đình miền Trung và bản sắc cao nguyên, ngay giữa 'thủ phủ cà phê'.",
  "presentation_long_en": "Standing on Phan Bội Châu street in the heart of Buôn Ma Thuột, Khai Doan Pagoda was begun in 1951 under the patronage of Queen Mother Đoan Huy (Từ Cung), mother of Emperor Bảo Đại. Its name joins the 'Khải' of Emperor Khải Định and the 'Đoan' of Đoan Huy, and it is regarded as the last pagoda granted a royal 'sắc tứ' title by the Nguyễn dynasty. Its distinction lies in a hybrid architecture: the main hall follows the three-bay wooden royal style of Huế, with timber columns, fine carving and curved roofs, while the rear extends in the form of an Ê Đê longhouse, expressing a fusion of Buddhism with Central Highlands culture. The grounds hold Buddha statues, a great bronze bell, gardens and a serene Avalokiteśvara. As the province's largest centre of Buddhist life, the pagoda is especially crowded at Vesak, the Vu Lan festival and Tết. For visitors, Khai Doan is not only a place of worship but a chance to feel the unique meeting of central-Vietnamese court art and highland identity, right in the 'coffee capital'.",
  "presentation_long_ru": "Стоящая на улице Фанбойтяу в самом сердце Буонматхуота пагода Кхайдоан была заложена в 1951 году под покровительством вдовствующей императрицы Доанзюй (Тыкунг), матери императора Бао Дая. Её название соединяет «Кхай» императора Кхайдиня и «Доан» императрицы Доанзюй; она считается последней пагодой, получившей королевский титул «сакты» от династии Нгуен. Её особенность — гибридная архитектура: главный зал выполнен в трёхпролётном деревянном дворцовом стиле Хюэ с колоннами, тонкой резьбой и изогнутыми крышами, а задняя часть вытянута в форме длинного дома эде, выражая слияние буддизма с культурой нагорья. На территории — статуи Будды, большой бронзовый колокол, сады и умиротворённая Авалокитешвара. Будучи крупнейшим центром буддийской жизни провинции, пагода особенно многолюдна в дни Весака, праздника Вулан и Тета. Для гостей Кхайдоан — не только место поклонения, но и возможность ощутить уникальную встречу придворного искусства центрального Вьетнама и самобытности нагорья прямо в «кофейной столице».",
  "highlights_vi": [
    "Ngôi chùa cuối cùng được triều Nguyễn ban 'sắc tứ', xây từ năm 1951",
    "Kiến trúc kết hợp nhà rường cung đình Huế và nhà dài Ê Đê",
    "Trung tâm Phật giáo lớn nhất Đắk Lắk, giữa trung tâm Buôn Ma Thuột"],
  "highlights_en": [
    "The last pagoda granted a royal 'sắc tứ' title by the Nguyễn dynasty, built from 1951",
    "Architecture blending Huế's royal timber style with the Ê Đê longhouse",
    "The largest Buddhist centre in Đắk Lắk, in central Buôn Ma Thuột"],
  "highlights_ru": [
    "Последняя пагода с королевским титулом «сакты» от Нгуенов, с 1951 года",
    "Архитектура, сочетающая дворцовый стиль Хюэ и длинный дом эде",
    "Крупнейший буддийский центр Даклака в центре Буонматхуота"],
  "practical": {
    "hours_vi": "Mở cửa ban ngày cho khách chiêm bái (miễn phí).",
    "ticket_vi": "Miễn phí.",
    "duration_vi": "Khoảng 30–45 phút.",
    "best_time_vi": "Sáng sớm hoặc chiều mát; đông vào lễ Phật đản, Vu lan, Tết.",
    "tips_vi": "Ăn mặc kín đáo, giữ yên tĩnh; bỏ giày khi vào chính điện."},
  "rating": {"value": 4.6, "count": 3000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Du khách khen chùa uy nghi, kiến trúc lạ mắt và không gian thanh tịnh giữa phố. Nhiều người ấn tượng với chính điện gỗ và tượng Quán Âm; dịp lễ khá đông.",
  "tags": ["temple", "architecture", "free", "culture", "top"],
  "sources": [
    {"title": "Wikipedia (VI) — Chùa Khải Đoan", "url": "https://vi.wikipedia.org/wiki/Ch%C3%B9a_Kh%E1%BA%A3i_%C4%90oan"}]}),

R("buon-ako-dhong", "Buôn Ako Dhong (Buôn Cô Thôn)", "Деревня Акодонг", "Ako Dhong Village",
  ["other"], 12.693, 108.05,
  "Phường Tân Lợi, khu vực Buôn Ma Thuột, tỉnh Đắk Lắk", {
  "presentation_short_vi": "Buôn Ako Dhong, còn gọi là Buôn Cô Thôn, là buôn làng Ê Đê nằm ngay rìa bắc Buôn Ma Thuột, được xem là buôn giàu và đẹp bậc nhất Tây Nguyên. Nơi đây giữ được nhiều nhà dài truyền thống, không gian cồng chiêng và những vườn cà phê xanh mướt. Du khách có thể tìm hiểu nếp sống Ê Đê và thưởng thức cà phê, rượu cần ngay trong buôn.",
  "presentation_short_en": "Ako Dhong, also called Buôn Cô Thôn, is an Ê Đê village on the northern edge of Buôn Ma Thuột, regarded as one of the richest and most beautiful villages in the Central Highlands. It preserves many traditional longhouses, a living gong culture and lush coffee gardens. Visitors can learn about Ê Đê life and enjoy coffee and rice wine right in the village.",
  "presentation_short_ru": "Акодонг, также называемая Буонкотхон, — деревня народа эде на северной окраине Буонматхуота, считающаяся одной из самых зажиточных и красивых в нагорье. Здесь сохранились многие традиционные длинные дома, живая культура гонгов и пышные кофейные сады. Гости могут узнать о быте эде и отведать кофе и рисовое вино прямо в деревне.",
  "presentation_long_vi": "Nằm cách trung tâm Buôn Ma Thuột chỉ vài cây số về phía bắc, Buôn Ako Dhong (theo tiếng Ê Đê nghĩa là 'buôn đầu nguồn suối') được khai lập từ giữa thế kỷ 20 và trở thành hình mẫu về một buôn làng Ê Đê no ấm, nề nếp. Điều khiến du khách yêu thích là con đường chính rợp bóng cây dẫn vào những căn nhà dài truyền thống mái cao, cầu thang gỗ chạm hình bầu vú và vầng trăng — biểu tượng của chế độ mẫu hệ. Trong buôn vẫn còn gìn giữ cồng chiêng, ghế Kpan, ché rượu cần và nghề dệt thổ cẩm; nhiều gia đình mở homestay, quán cà phê sân vườn để đón khách. Đến đây vào buổi chiều, du khách có thể dạo giữa vườn cà phê, nghe kể về phong tục mẫu hệ, thưởng thức ly cà phê nguyên chất của chính vùng đất này, và nếu đúng dịp lễ hội sẽ được hòa mình vào tiếng chiêng ngân vang, điệu xoang và men rượu cần nồng ấm. Ako Dhong là nơi lý tưởng để cảm nhận đời sống Ê Đê một cách bình dị và chân thực ngay sát đô thị, minh chứng cho sự hòa quyện giữa truyền thống và nhịp sống hiện đại của 'thủ phủ cà phê'.",
  "presentation_long_en": "Just a few kilometres north of central Buôn Ma Thuột, Ako Dhong (Ê Đê for 'the village at the head of the stream') was founded in the mid-20th century and became a model of a prosperous, well-ordered Ê Đê village. What visitors love is the tree-shaded main lane leading to traditional longhouses with high roofs and wooden stairs carved with breasts and a crescent moon — symbols of the matriarchal order. The village still keeps its gongs, Kpan benches, jars of rice wine and brocade weaving; many families run homestays and garden cafés for guests. Coming in the afternoon, visitors can wander among coffee gardens, hear about matriarchal customs, savour pure local coffee, and, if a festival falls on the day, be swept up in ringing gongs, communal dances and warm rice wine. Ako Dhong is an ideal place to feel Ê Đê life in a simple, authentic way right beside the city — proof of how tradition and modern rhythm intertwine in the 'coffee capital'.",
  "presentation_long_ru": "Всего в нескольких километрах к северу от центра Буонматхуота деревня Акодонг (на языке эде — «деревня у истока ручья») была основана в середине XX века и стала образцом зажиточной, упорядоченной деревни эде. Гостям особенно нравится тенистая главная аллея, ведущая к традиционным длинным домам с высокими крышами и деревянными лестницами, украшенными резьбой в виде груди и полумесяца — символами матриархального уклада. В деревне по-прежнему хранят гонги, скамьи кпан, кувшины с рисовым вином и ткачество из парчи; многие семьи держат гостевые дома и садовые кофейни. Приехав во второй половине дня, гости могут пройтись по кофейным садам, послушать о матриархальных обычаях, отведать чистый местный кофе, а если выпадет праздник — окунуться в звон гонгов, общинные танцы и тёплое рисовое вино. Акодонг — идеальное место, чтобы просто и подлинно почувствовать жизнь эде прямо у города, свидетельство того, как традиция и современный ритм переплетаются в «кофейной столице».",
  "highlights_vi": [
    "Buôn Ê Đê trù phú, còn giữ nhiều nhà dài truyền thống ngay sát Buôn Ma Thuột",
    "Không gian cồng chiêng, ghế Kpan, rượu cần và chế độ mẫu hệ",
    "Homestay, cà phê sân vườn giữa những vườn cà phê xanh mướt"],
  "highlights_en": [
    "A prosperous Ê Đê village keeping many longhouses right beside Buôn Ma Thuột",
    "Living gong culture, Kpan benches, rice wine and matriarchal customs",
    "Homestays and garden cafés amid lush coffee gardens"],
  "highlights_ru": [
    "Зажиточная деревня эде со множеством длинных домов у Буонматхуота",
    "Живая культура гонгов, скамьи кпан, рисовое вино и матриархат",
    "Гостевые дома и садовые кофейни среди пышных кофейных садов"],
  "practical": {
    "hours_vi": "Tham quan tự do ban ngày; homestay/quán cà phê theo giờ riêng.",
    "ticket_vi": "Vào buôn miễn phí; chi phí ăn uống, homestay, trải nghiệm tùy chọn.",
    "duration_vi": "Khoảng 1–2 giờ (hoặc nghỉ đêm homestay).",
    "best_time_vi": "Chiều mát; đẹp nhất vào mùa lễ hội cồng chiêng và mùa hoa cà phê (tháng 3).",
    "tips_vi": "Xin phép khi chụp ảnh nhà dân; ủng hộ cà phê, thổ cẩm của buôn; tôn trọng phong tục."},
  "rating": {"value": 4.4, "count": 1200, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách thích không khí yên bình, nhà dài đẹp và cà phê ngon ngay trong buôn; hợp để tìm hiểu văn hóa Ê Đê. Vài nhà đã hiện đại hóa nên cần chọn điểm còn giữ nếp cũ.",
  "tags": ["culture", "village", "coffee", "outdoor", "family"],
  "sources": [
    {"title": "Báo Đắk Lắk — Buôn Ako Dhông", "url": "https://vi.wikipedia.org/wiki/Bu%C3%B4n_Ma_Thu%E1%BB%99t"}]}),
]

new += [
R("tuong-dai-chien-thang-bmt", "Tượng đài Chiến thắng Buôn Ma Thuột (Ngã Sáu)", "Монумент Победы в Буонматхуоте", "Buon Ma Thuot Victory Monument",
  ["monument", "square_street"], 12.6786, 108.038,
  "Ngã Sáu, trung tâm Buôn Ma Thuột, tỉnh Đắk Lắk", {
  "presentation_short_vi": "Tượng đài Chiến thắng Buôn Ma Thuột ở vòng xoay Ngã Sáu là biểu tượng trung tâm của thành phố, ghi dấu chiến thắng ngày 10/3/1975 mở màn cho Đại thắng mùa Xuân. Cụm tượng đài có mô hình xe tăng vươn lên bầu trời cao nguyên. Đây là điểm hẹn quen thuộc và nơi chụp ảnh của người dân lẫn du khách.",
  "presentation_short_en": "The Buon Ma Thuot Victory Monument at the Ngã Sáu (Six-Way) roundabout is the city's central landmark, commemorating the victory of 10 March 1975 that opened the Spring Offensive. The monument features a tank rising toward the highland sky. It is a well-known meeting point and photo spot for locals and visitors alike.",
  "presentation_short_ru": "Монумент Победы в Буонматхуоте на кольцевой развязке Нгашау — центральный символ города, увековечивающий победу 10 марта 1975 года, открывшую Весеннее наступление. В композиции монумента — танк, устремлённый в небо нагорья. Это известное место встреч и фотографий для местных жителей и туристов.",
  "presentation_long_vi": "Nằm ngay vòng xoay Ngã Sáu — nút giao trung tâm và sầm uất nhất Buôn Ma Thuột — Tượng đài Chiến thắng là công trình biểu tượng gắn với sự kiện lịch sử trọng đại: rạng sáng 10/3/1975, quân giải phóng bất ngờ tiến công và làm chủ thị xã Buôn Ma Thuột, mở màn cho Chiến dịch Tây Nguyên và Đại thắng mùa Xuân 1975. Cụm tượng đài tái hiện hình ảnh chiếc xe tăng cùng những nhân vật đại diện cho các lực lượng và đồng bào các dân tộc Tây Nguyên, vươn lên mạnh mẽ giữa quảng trường rộng. Về đêm, đài được chiếu sáng lung linh, trở thành trái tim của thành phố với dòng xe cộ tấp nập vòng quanh. Với người dân Buôn Ma Thuột, Ngã Sáu vừa là mốc định vị quen thuộc, vừa là nơi diễn ra nhiều hoạt động cộng đồng, lễ hội đường phố, đặc biệt trong dịp kỷ niệm giải phóng thành phố và Lễ hội Cà phê. Với du khách, đây thường là điểm dừng chân đầu tiên khi dạo trung tâm: chụp ảnh bên tượng đài, cảm nhận nhịp sống cao nguyên rồi tỏa ra các quán cà phê, chợ và điểm tham quan lân cận. Một biểu tượng giản dị nhưng đầy tự hào của 'thủ phủ cà phê'.",
  "presentation_long_en": "At the Ngã Sáu (Six-Way) roundabout — the busiest central junction of Buôn Ma Thuột — the Victory Monument is an emblematic work tied to a momentous event: at dawn on 10 March 1975, liberation forces launched a surprise attack and took the town of Buôn Ma Thuột, opening the Central Highlands Campaign and the 1975 Spring Offensive. The monument depicts a tank together with figures representing the armed forces and the ethnic peoples of the highlands, rising boldly above a broad plaza. By night it is brightly lit, the heart of the city with traffic streaming around it. For the people of Buôn Ma Thuột, Ngã Sáu is both a familiar landmark and a stage for community events and street festivals, especially around the anniversary of the city's liberation and the Coffee Festival. For visitors it is often the first stop on a walk through the centre: a photo by the monument, a sense of the highland rhythm, then out to the nearby cafés, markets and sights. A simple but proud symbol of the 'coffee capital'.",
  "presentation_long_ru": "На кольцевой развязке Нгашау — самом оживлённом центральном перекрёстке Буонматхуота — Монумент Победы стал символом, связанным с важнейшим событием: на рассвете 10 марта 1975 года освободительные силы внезапно атаковали и заняли город Буонматхуот, открыв кампанию в Центральном нагорье и Весеннее наступление 1975 года. Композиция изображает танк вместе с фигурами, представляющими вооружённые силы и народы нагорья, мощно поднимающимися над широкой площадью. Ночью монумент ярко подсвечен и становится сердцем города, вокруг которого течёт поток машин. Для жителей Буонматхуота Нгашау — и привычный ориентир, и сцена общественных событий и уличных праздников, особенно в дни годовщины освобождения города и фестиваля кофе. Для гостей это часто первая остановка на прогулке по центру: фото у монумента, ощущение ритма нагорья, а затем — соседние кофейни, рынки и достопримечательности. Простой, но гордый символ «кофейной столицы».",
  "highlights_vi": [
    "Ghi dấu chiến thắng 10/3/1975 mở màn Chiến dịch Tây Nguyên",
    "Cụm tượng có mô hình xe tăng, đặt giữa vòng xoay Ngã Sáu trung tâm",
    "Điểm hẹn, chụp ảnh và trung tâm lễ hội đường phố của thành phố"],
  "highlights_en": [
    "Commemorates the 10 March 1975 victory that opened the Central Highlands Campaign",
    "A tank sculpture set in the central Six-Way roundabout",
    "A meeting point, photo spot and hub for the city's street festivals"],
  "highlights_ru": [
    "Увековечивает победу 10 марта 1975 года, открывшую кампанию в нагорье",
    "Скульптура с танком в центре развязки Нгашау",
    "Место встреч, фотографий и центр городских праздников"],
  "practical": {
    "hours_vi": "Ngoài trời, tham quan tự do cả ngày; đẹp về đêm khi lên đèn.",
    "ticket_vi": "Miễn phí.",
    "duration_vi": "Khoảng 15–20 phút.",
    "best_time_vi": "Chiều tối; dịp lễ giải phóng thành phố (10/3) và Lễ hội Cà phê rất sôi động.",
    "tips_vi": "Chú ý an toàn giao thông vòng xoay khi chụp ảnh; kết hợp dạo trung tâm."},
  "rating": {"value": 4.3, "count": 1800, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Du khách xem đây là biểu tượng dễ nhận biết của Buôn Ma Thuột, đẹp về đêm; tiện làm mốc dạo phố. Lưu ý giao thông vòng xoay khá đông.",
  "tags": ["monument", "history", "free", "night", "city"],
  "sources": [
    {"title": "Wikipedia (VI) — Chiến dịch Tây Nguyên (Buôn Ma Thuột 1975)", "url": "https://vi.wikipedia.org/wiki/Chi%E1%BA%BFn_d%E1%BB%8Bch_T%C3%A2y_Nguy%C3%AAn"}]}),

R("thac-thuy-tien", "Thác Thủy Tiên (Thác Ba Tầng)", "Водопад Тхуйтьен", "Thuy Tien Waterfall",
  ["park_garden", "other"], 12.997, 108.37,
  "Xã Ea Púk (khu vực Krông Năng), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Thác Thủy Tiên, còn gọi là thác Ba Tầng, là ngọn thác đẹp nằm giữa rừng ở khu vực Krông Năng. Dòng nước đổ qua ba tầng đá với những bồn tắm thiên nhiên trong veo, xung quanh là cây rừng rợp bóng. Đây là điểm dã ngoại, tắm mát được nhiều người yêu thiên nhiên tìm đến.",
  "presentation_short_en": "Thuy Tien Waterfall, also called the Three-Tier Falls, is a beautiful cascade set in the forest of the Krông Năng area. Its water tumbles over three rock tiers into clear natural pools, surrounded by shady jungle. It is a favourite picnic and bathing spot for nature lovers.",
  "presentation_short_ru": "Водопад Тхуйтьен, также называемый Трёхъярусным, — красивый каскад в лесу района Кронгнанг. Его вода спадает по трём каменным уступам в прозрачные природные бассейны среди тенистых джунглей. Это любимое место для пикников и купания у любителей природы.",
  "presentation_long_vi": "Ẩn mình giữa rừng ở khu vực Krông Năng, cách trung tâm Buôn Ma Thuột khoảng 55–60 km, thác Thủy Tiên gây ấn tượng bởi vẻ đẹp mềm mại được ví như dải lụa. Thác đổ qua ba tầng đá nối tiếp nhau — vì thế còn có tên thác Ba Tầng — mỗi tầng tạo thành một hồ nước nông trong vắt, nơi du khách có thể ngâm chân, tắm mát và nghe tiếng nước hòa cùng tiếng chim rừng. Xung quanh là rừng nguyên sinh với nhiều cây cổ thụ, dây leo và tảng đá phủ rêu, khiến không gian mát lành, hoang sơ. Vào mùa mưa, thác cuộn chảy mạnh mẽ và hùng vĩ; mùa khô nước hiền hòa hơn, lộ ra những bãi đá đẹp để cắm trại, dã ngoại. Đường vào thác đã thuận tiện hơn trước, phù hợp cho những chuyến đi trong ngày của gia đình và nhóm bạn muốn tránh xa phố thị. Gắn với thác còn có những truyền thuyết dân gian của người bản địa, tăng thêm nét huyền bí cho điểm đến. Thủy Tiên là một trong những thác nước đáng ghé nhất phía đông Đắk Lắk, đặc biệt với ai yêu cảnh sắc thiên nhiên nguyên sơ của cao nguyên.",
  "presentation_long_en": "Hidden in the forest of the Krông Năng area, about 55–60 km from central Buôn Ma Thuột, Thuy Tien Waterfall is admired for a soft beauty often likened to a ribbon of silk. The water drops over three successive rock tiers — hence its other name, the Three-Tier Falls — each forming a shallow, crystal-clear pool where visitors can soak their feet, bathe and listen to the water mingling with birdsong. All around is primary forest of old trees, vines and moss-covered boulders, keeping the air cool and the setting wild. In the rainy season the falls surge, powerful and grand; in the dry season the water is gentler, revealing lovely rocky flats for camping and picnics. The access road is now easier than before, suiting day trips for families and groups wishing to escape the city. Local folk legends are attached to the falls, adding a touch of mystery. Thuy Tien is one of the most worthwhile waterfalls in eastern Đắk Lắk, especially for those who love the untouched natural scenery of the highlands.",
  "presentation_long_ru": "Скрытый в лесу района Кронгнанг, примерно в 55–60 км от центра Буонматхуота, водопад Тхуйтьен восхищает мягкой красотой, которую часто сравнивают с шёлковой лентой. Вода спадает по трём последовательным каменным уступам — отсюда и второе название, Трёхъярусный водопад, — каждый образует мелкий кристально чистый бассейн, где можно окунуть ноги, искупаться и послушать шум воды вперемешку с пением птиц. Вокруг — первичный лес из старых деревьев, лиан и покрытых мхом валунов, сохраняющий прохладу и первозданность. В сезон дождей водопад бурлит, мощный и величественный; в сухой сезон вода спокойнее, открывая красивые каменные площадки для кемпинга и пикников. Дорога к водопаду теперь удобнее, чем раньше, и подходит для однодневных поездок семей и компаний, желающих сбежать из города. С водопадом связаны местные народные легенды, добавляющие ноту загадочности. Тхуйтьен — один из самых достойных водопадов востока Даклака, особенно для тех, кто любит нетронутую природу нагорья.",
  "highlights_vi": [
    "Thác ba tầng đổ qua các hồ nước nông trong vắt để tắm mát",
    "Bao quanh là rừng nguyên sinh, đá phủ rêu, mát lành hoang sơ",
    "Điểm dã ngoại trong ngày ở phía đông Đắk Lắk (Krông Năng)"],
  "highlights_en": [
    "A three-tier falls dropping into shallow, crystal-clear bathing pools",
    "Surrounded by primary forest and moss-covered rocks, cool and wild",
    "A day-trip picnic spot in eastern Đắk Lắk (Krông Năng)"],
  "highlights_ru": [
    "Трёхъярусный водопад с мелкими прозрачными бассейнами для купания",
    "В окружении первичного леса и замшелых камней, прохладно и дико",
    "Место для однодневных пикников на востоке Даклака (Кронгнанг)"],
  "practical": {
    "hours_vi": "Ban ngày; nên đi khi trời khô ráo, tránh mưa lũ.",
    "ticket_vi": "Phí tham quan/giữ xe tượng trưng; có thể thay đổi.",
    "duration_vi": "Khoảng 2–3 giờ (cả di chuyển và dã ngoại).",
    "best_time_vi": "Cuối mùa mưa đến đầu mùa khô; tránh ngày mưa lớn.",
    "tips_vi": "Cẩn thận đá trơn, không tắm khi nước dâng; mang đồ ăn, túi đựng rác."},
  "rating": {"value": 4.2, "count": 700, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách khen thác đẹp, nước trong, không khí mát và ít xô bồ; hợp dã ngoại. Một số nhắc dịch vụ còn ít, đá trơn cần cẩn thận.",
  "tags": ["nature", "waterfall", "outdoor", "daytrip"],
  "sources": [
    {"title": "Cổng thông tin du lịch Đắk Lắk — Thác Thủy Tiên", "url": "https://vi.wikipedia.org/wiki/Kr%C3%B4ng_N%C4%83ng"}]}),

R("ho-ea-kao", "Hồ Ea Kao", "Озеро Еакао", "Ea Kao Lake",
  ["park_garden", "other"], 12.628, 108.073,
  "Xã Ea Kao (khu vực Buôn Ma Thuột), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Hồ Ea Kao là hồ nước ngọt rộng ở ngoại ô phía nam Buôn Ma Thuột, được ví như 'lá phổi xanh' của thành phố. Mặt hồ phẳng lặng in bóng rừng cây và những bán đảo nhỏ, là nơi lý tưởng để dạo mát, chèo thuyền và ngắm hoàng hôn. Quanh hồ có các buôn làng Ê Đê và vườn cây, giữ được nét bình yên.",
  "presentation_short_en": "Ea Kao Lake is a broad freshwater reservoir on the southern edge of Buôn Ma Thuột, often called the city's 'green lung'. Its calm surface mirrors the surrounding woods and small peninsulas, making it ideal for strolling, boating and watching the sunset. Ê Đê villages and gardens around the shore keep the scene peaceful.",
  "presentation_short_ru": "Озеро Еакао — обширное пресноводное водохранилище на южной окраине Буонматхуота, которое часто называют «зелёными лёгкими» города. Его спокойная гладь отражает окрестные леса и небольшие полуострова, что делает его идеальным для прогулок, катания на лодке и любования закатом. Деревни эде и сады по берегам сохраняют умиротворённость.",
  "presentation_long_vi": "Cách trung tâm Buôn Ma Thuột khoảng 12 km về phía nam, hồ Ea Kao là hồ thủy lợi nhân tạo được hình thành từ việc ngăn dòng các con suối, nay trở thành một điểm sinh thái yêu thích của người dân địa phương. Hồ rộng, nhiều nhánh và bán đảo nhô ra mặt nước, xen giữa những rặng cây và vườn cà phê, tạo nên khung cảnh vừa khoáng đạt vừa nên thơ. Du khách có thể đi dạo ven bờ, thuê thuyền hoặc đạp vịt trên hồ, câu cá, cắm trại và đặc biệt ngắm cảnh bình minh, hoàng hôn khi mặt nước nhuộm ánh vàng cam. Quanh hồ là địa bàn sinh sống của cộng đồng Ê Đê với những buôn làng còn giữ nếp truyền thống, nên chuyến đi cũng là dịp tìm hiểu văn hóa bản địa và thưởng thức ẩm thực dân dã. Không gian trong lành, yên tĩnh khiến Ea Kao trở thành nơi 'trốn phố' quen thuộc vào dịp cuối tuần, phù hợp cho gia đình, nhóm bạn muốn thư giãn gần thành phố mà vẫn cảm nhận được thiên nhiên cao nguyên. Vào mùa nước đầy, hồ mênh mông xanh biếc; mùa khô lộ ra những bãi cỏ, bãi đất ven bờ lý tưởng để picnic.",
  "presentation_long_en": "About 12 km south of central Buôn Ma Thuột, Ea Kao Lake is a man-made irrigation reservoir formed by damming several streams, now a favourite eco-spot for locals. The lake is wide, with many arms and peninsulas jutting into the water among groves and coffee gardens, creating scenery at once open and poetic. Visitors can stroll the shore, hire a boat or pedal-boat, fish, camp, and above all watch sunrise and sunset when the water glows gold and orange. The surrounding land is home to Ê Đê communities whose villages still keep old ways, so a visit is also a chance to learn about local culture and enjoy rustic food. The fresh, quiet air makes Ea Kao a familiar weekend escape, well suited to families and groups who want to relax close to the city while still feeling the nature of the highlands. When the water is high the lake spreads out in deep blue; in the dry season it reveals grassy flats and shoreline patches ideal for picnics.",
  "presentation_long_ru": "Примерно в 12 км к югу от центра Буонматхуота озеро Еакао — искусственное ирригационное водохранилище, образованное запрудой нескольких ручьёв, а ныне любимое место отдыха местных жителей. Озеро широкое, со множеством заливов и полуостровов, выступающих в воду среди рощ и кофейных садов, что создаёт пейзаж одновременно просторный и поэтичный. Гости могут пройтись по берегу, взять лодку или катамаран, порыбачить, разбить лагерь и, главное, полюбоваться рассветом и закатом, когда вода отливает золотом и оранжевым. Окрестные земли населены общинами эде, чьи деревни хранят старые обычаи, поэтому поездка — ещё и повод узнать местную культуру и отведать простую еду. Свежий, тихий воздух делает Еакао привычным местом выходного дня, подходящим семьям и компаниям, желающим отдохнуть у города, но ощутить природу нагорья. В полноводье озеро широко разливается насыщенной синевой; в сухой сезон открываются травяные площадки у берега, идеальные для пикника.",
  "highlights_vi": [
    "Hồ nước ngọt rộng, 'lá phổi xanh' ở ngoại ô Buôn Ma Thuột",
    "Chèo thuyền, câu cá, cắm trại và ngắm bình minh – hoàng hôn",
    "Xung quanh là buôn làng Ê Đê và vườn cà phê yên bình"],
  "highlights_en": [
    "A broad freshwater lake, the 'green lung' on the edge of Buôn Ma Thuột",
    "Boating, fishing, camping and watching sunrise and sunset",
    "Surrounded by peaceful Ê Đê villages and coffee gardens"],
  "highlights_ru": [
    "Обширное пресноводное озеро, «зелёные лёгкие» у Буонматхуота",
    "Катание на лодке, рыбалка, кемпинг и любование рассветом и закатом",
    "В окружении спокойных деревень эде и кофейных садов"],
  "practical": {
    "hours_vi": "Tham quan tự do ban ngày; dịch vụ thuyền/đạp vịt theo điểm.",
    "ticket_vi": "Vào tự do; thuê thuyền, đạp vịt tính phí tùy dịch vụ.",
    "duration_vi": "Khoảng 1,5–2 giờ.",
    "best_time_vi": "Chiều muộn ngắm hoàng hôn; mùa nước đầy hồ đẹp nhất.",
    "tips_vi": "Mang đồ picnic, chống nắng; mặc áo phao khi lên thuyền; giữ vệ sinh ven hồ."},
  "rating": {"value": 4.1, "count": 900, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách thích cảnh hồ rộng, thoáng và hoàng hôn đẹp; hợp thư giãn cuối tuần. Một số nhận xét dịch vụ tự phát, cần thêm tiện ích.",
  "tags": ["nature", "lake", "outdoor", "family", "viewpoint"],
  "sources": [
    {"title": "Wikipedia (VI) — Ea Kao (Buôn Ma Thuột)", "url": "https://vi.wikipedia.org/wiki/Ea_Kao"}]}),

R("kdl-ko-tam", "Khu du lịch sinh thái Kô Tam", "Экотуристический комплекс Котам", "Ko Tam Ecotourism Area",
  ["park_garden", "other"], 12.656, 108.118,
  "Xã Ea Tu (khu vực Buôn Ma Thuột), Quốc lộ 26, tỉnh Đắk Lắk", {
  "presentation_short_vi": "Khu du lịch sinh thái Kô Tam nằm ở cửa ngõ phía đông Buôn Ma Thuột, là điểm đến kết hợp thiên nhiên, văn hóa Ê Đê và ẩm thực Tây Nguyên. Trong khuôn viên rộng có hồ nước, vườn hoa, nhà dài, không gian cồng chiêng và khu vui chơi. Đây là nơi lý tưởng để nghỉ ngơi, thưởng thức cà phê và cảm nhận bản sắc cao nguyên.",
  "presentation_short_en": "The Ko Tam Ecotourism Area, at the eastern gateway of Buôn Ma Thuột, blends nature, Ê Đê culture and Central Highlands cuisine. Its spacious grounds hold a lake, flower gardens, longhouses, a gong-performance space and play areas. It is an ideal place to relax, enjoy coffee and feel the identity of the highlands.",
  "presentation_short_ru": "Экотуристический комплекс Котам у восточных ворот Буонматхуота объединяет природу, культуру эде и кухню нагорья. На просторной территории есть озеро, цветники, длинные дома, площадка для выступлений с гонгами и зоны отдыха. Это идеальное место, чтобы отдохнуть, выпить кофе и ощутить самобытность нагорья.",
  "presentation_long_vi": "Nằm bên Quốc lộ 26, cách trung tâm Buôn Ma Thuột khoảng 9 km về phía đông, Khu du lịch sinh thái Kô Tam là một trong những điểm đến du lịch cộng đồng và sinh thái được đầu tư bài bản của Đắk Lắk. Trên diện tích rộng lớn, khu du lịch bố trí hài hòa giữa cảnh quan thiên nhiên và không gian văn hóa: hồ nước, thác nhân tạo, đồi hoa, vườn cây ăn trái, những căn nhà dài Ê Đê, khu ẩm thực và sân khấu biểu diễn cồng chiêng. Du khách có thể dạo bộ giữa vườn hoa, chèo thuyền trên hồ, tham gia trò chơi dân gian, xem múa xoang, nghe chiêng và thưởng thức các món đặc sản như gà nướng, cơm lam, canh cà đắng, rượu cần. Vào mùa hoa, những đồi hoa rực rỡ trở thành phông nền chụp ảnh được yêu thích. Kô Tam cũng thường tổ chức sự kiện, đám cưới, teambuilding và là điểm dừng chân quen thuộc trong dịp Lễ hội Cà phê Buôn Ma Thuột. Với sự kết hợp giữa nghỉ dưỡng, vui chơi và trải nghiệm văn hóa bản địa trong một không gian xanh mát, đây là lựa chọn phù hợp cho gia đình, nhóm bạn và du khách muốn cảm nhận Tây Nguyên một cách nhẹ nhàng, tiện lợi ngay gần thành phố.",
  "presentation_long_en": "On National Highway 26, about 9 km east of central Buôn Ma Thuột, the Ko Tam Ecotourism Area is one of Đắk Lắk's well-developed community and eco-tourism destinations. Across a large site it harmonises natural scenery with cultural spaces: a lake, an artificial waterfall, flower hills, orchards, Ê Đê longhouses, a food court and a stage for gong performances. Visitors can wander through flower gardens, row on the lake, join folk games, watch communal dances, listen to gongs and taste local specialities such as grilled chicken, bamboo-tube rice, bitter-eggplant soup and rice wine. In flowering season the bright hillsides become a favourite photo backdrop. Ko Tam also hosts events, weddings and team-building activities and is a familiar stop during the Buôn Ma Thuột Coffee Festival. Combining leisure, play and indigenous cultural experience in a cool green setting, it is a fitting choice for families, groups and travellers who want to feel the Central Highlands in an easy, convenient way close to the city.",
  "presentation_long_ru": "На национальном шоссе 26, примерно в 9 км к востоку от центра Буонматхуота, экотуристический комплекс Котам — один из хорошо развитых объектов общинного и экологического туризма Даклака. На большой территории он гармонично сочетает природные пейзажи и культурные пространства: озеро, искусственный водопад, цветочные холмы, фруктовые сады, длинные дома эде, зону питания и сцену для выступлений с гонгами. Гости могут гулять по цветникам, кататься на лодке по озеру, участвовать в народных играх, смотреть общинные танцы, слушать гонги и пробовать местные блюда — жареную курицу, рис в бамбуке, суп из горького баклажана и рисовое вино. В сезон цветения яркие склоны становятся любимым фоном для фотографий. В Котаме также проходят мероприятия, свадьбы и тимбилдинги, а во время фестиваля кофе это привычная остановка. Сочетая отдых, развлечения и знакомство с культурой коренных народов в прохладной зелёной среде, комплекс подходит семьям, компаниям и путешественникам, желающим легко и удобно ощутить нагорье рядом с городом.",
  "highlights_vi": [
    "Không gian sinh thái rộng: hồ, đồi hoa, nhà dài và sân khấu cồng chiêng",
    "Trải nghiệm văn hóa Ê Đê và ẩm thực Tây Nguyên tại chỗ",
    "Gần Buôn Ma Thuột, điểm dừng quen thuộc dịp Lễ hội Cà phê"],
  "highlights_en": [
    "A spacious eco-setting: lake, flower hills, longhouses and a gong stage",
    "Ê Đê cultural experiences and Central Highlands cuisine on site",
    "Close to Buôn Ma Thuột, a familiar stop during the Coffee Festival"],
  "highlights_ru": [
    "Просторная эко-среда: озеро, цветочные холмы, длинные дома и сцена гонгов",
    "Знакомство с культурой эде и кухней нагорья на месте",
    "Рядом с Буонматхуотом, привычная остановка во время фестиваля кофе"],
  "practical": {
    "hours_vi": "Thường mở khoảng 7:00–21:00 (khu ẩm thực buổi tối); nên kiểm tra lại.",
    "ticket_vi": "Vé vào cổng tham khảo khoảng 30.000–50.000 VND; dịch vụ tính riêng.",
    "duration_vi": "Khoảng 2–3 giờ (hoặc cả buổi nếu ăn uống, vui chơi).",
    "best_time_vi": "Mùa hoa nở và dịp Lễ hội Cà phê; cuối tuần đông vui.",
    "tips_vi": "Đặt suất ăn/biểu diễn trước nếu đi đoàn; kết hợp mua đặc sản cà phê."},
  "rating": {"value": 4.2, "count": 4000, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách khen khuôn viên xanh, sạch, nhiều góc chụp ảnh và món ăn ngon; hợp gia đình. Một vài ý kiến thấy đông vào cuối tuần và dịp lễ.",
  "tags": ["ecotourism", "culture", "family", "outdoor", "food"],
  "sources": [
    {"title": "Cổng du lịch Đắk Lắk — Khu du lịch Kô Tam", "url": "https://daklak.gov.vn/"}]}),

R("thac-krong-kmar", "Thác Krông Kmar", "Водопад Кронгкмар", "Krong Kmar Waterfall",
  ["park_garden", "other"], 12.46, 108.32,
  "Xã Krông Bông (khu vực cũ), dưới chân Chư Yang Sin, tỉnh Đắk Lắk", {
  "presentation_short_vi": "Thác Krông Kmar nằm dưới chân dãy Chư Yang Sin, là ngọn thác đẹp gắn với dòng suối cùng tên bắt nguồn từ đỉnh núi cao nhất Đắk Lắk. Thác chảy qua nhiều bậc đá lớn giữa rừng, có hồ nước phía dưới để chèo thuyền, dã ngoại. Đây cũng là điểm khởi đầu cho hành trình chinh phục Chư Yang Sin.",
  "presentation_short_en": "Krong Kmar Waterfall lies at the foot of the Chu Yang Sin range, a beautiful cascade fed by the stream of the same name that rises from Đắk Lắk's highest peak. It flows over large rock steps amid the forest, with a reservoir below for boating and picnics. It is also the starting point for treks up Chu Yang Sin.",
  "presentation_short_ru": "Водопад Кронгкмар расположен у подножия хребта Чуянгшин — красивый каскад, питаемый одноимённым ручьём, берущим начало на высочайшей вершине Даклака. Он течёт по крупным каменным ступеням среди леса, а внизу есть водохранилище для катания на лодке и пикников. Отсюда же начинаются походы на Чуянгшин.",
  "presentation_long_vi": "Thác Krông Kmar thuộc khu vực Krông Bông, cách Buôn Ma Thuột khoảng 60 km về phía đông nam, là một trong những thác nước đẹp và giàu tiềm năng của Đắk Lắk. Dòng suối Krông Kmar bắt nguồn từ đỉnh Chư Yang Sin — nóc nhà của tỉnh — mang nước mát quanh năm đổ xuống qua những bậc đá granit khổng lồ, tạo thành nhiều tầng thác tung bọt trắng xóa giữa rừng cây xanh mát. Phía dưới chân thác là hồ nước rộng, nơi du khách có thể thuê thuyền, đạp vịt, câu cá và nghỉ ngơi trên các bãi đá. Khung cảnh nơi đây kết hợp giữa sự hùng vĩ của núi rừng và nét thơ mộng của dòng suối, đặc biệt quyến rũ vào mùa mưa khi thác cuộn chảy mạnh mẽ. Với những người ưa mạo hiểm, Krông Kmar còn là điểm xuất phát quen thuộc để leo lên đỉnh Chư Yang Sin, băng qua rừng già và chinh phục độ cao 2.442 m. Gắn với vùng đất này còn có những buôn làng của người M'nông, Ê Đê và các câu chuyện văn hóa bản địa. Krông Kmar vì thế vừa là nơi dã ngoại, tắm thác thư giãn, vừa là cửa ngõ cho những hành trình khám phá thiên nhiên nguyên sơ của cao nguyên.",
  "presentation_long_en": "Krong Kmar Waterfall, in the Krông Bông area about 60 km southeast of Buôn Ma Thuột, is one of Đắk Lắk's most beautiful and promising falls. The Krông Kmar stream rises from Chu Yang Sin peak — the roof of the province — carrying cool water year-round down over huge granite steps to form several tiers foaming white amid green forest. Below the falls lies a broad reservoir where visitors can hire boats and pedal-boats, fish and rest on the rocks. The scene marries the grandeur of the mountains with the poetry of the stream, and is especially alluring in the rainy season when the falls surge. For the adventurous, Krong Kmar is also a familiar starting point for climbing Chu Yang Sin, crossing old-growth forest to conquer its 2,442 m summit. The area is home to M'nông and Ê Đê villages and their local cultural stories. Krong Kmar is thus at once a place to picnic and bathe beneath the falls and a gateway to journeys into the pristine nature of the highlands.",
  "presentation_long_ru": "Водопад Кронгкмар в районе Кронгбонг, примерно в 60 км к юго-востоку от Буонматхуота, — один из красивейших и перспективных водопадов Даклака. Ручей Кронгкмар берёт начало на вершине Чуянгшин — «крыше» провинции — и круглый год несёт прохладную воду вниз по огромным гранитным ступеням, образуя несколько ярусов, вспенивающихся белым среди зелёного леса. У подножия водопада — широкое водохранилище, где можно взять лодку или катамаран, порыбачить и отдохнуть на камнях. Пейзаж соединяет величие гор и поэзию ручья и особенно притягателен в сезон дождей, когда водопад бурлит. Для любителей приключений Кронгкмар — привычная отправная точка для восхождения на Чуянгшин через реликтовый лес к вершине 2442 м. В этих местах живут деревни мнонг и эде со своими культурными преданиями. Таким образом, Кронгкмар — это и место для пикника и купания под водопадом, и ворота к путешествиям в первозданную природу нагорья.",
  "highlights_vi": [
    "Suối bắt nguồn từ đỉnh Chư Yang Sin, thác đổ qua bậc đá granit lớn",
    "Có hồ nước phía dưới để chèo thuyền, câu cá, dã ngoại",
    "Điểm xuất phát leo đỉnh Chư Yang Sin cao 2.442 m"],
  "highlights_en": [
    "A stream from Chu Yang Sin peak; the falls drop over big granite steps",
    "A reservoir below for boating, fishing and picnics",
    "The starting point for climbing the 2,442 m Chu Yang Sin summit"],
  "highlights_ru": [
    "Ручей с вершины Чуянгшин; водопад по крупным гранитным ступеням",
    "Внизу водохранилище для лодок, рыбалки и пикников",
    "Отправная точка восхождения на вершину Чуянгшин (2442 м)"],
  "practical": {
    "hours_vi": "Ban ngày; mùa mưa cẩn thận nước lớn.",
    "ticket_vi": "Phí tham quan/giữ xe tượng trưng; dịch vụ thuyền tính riêng.",
    "duration_vi": "Khoảng 2–3 giờ; trek đỉnh cần 2 ngày.",
    "best_time_vi": "Mùa mưa thác đẹp; mùa khô thuận tiện dã ngoại và trek.",
    "tips_vi": "Không tắm khi nước dâng; đá trơn cần cẩn thận; muốn trek đỉnh nên có hướng dẫn."},
  "rating": {"value": 4.1, "count": 600, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách thích thác hùng vĩ, hồ nước mát và cảnh núi rừng; hợp dã ngoại và làm bàn đạp trek Chư Yang Sin. Một số nói dịch vụ còn cơ bản.",
  "tags": ["nature", "waterfall", "trekking", "outdoor", "daytrip"],
  "sources": [
    {"title": "Wikipedia (VI) — Krông Bông", "url": "https://vi.wikipedia.org/wiki/Kr%C3%B4ng_B%C3%B4ng"}]}),
]

# ============================ DUYÊN HẢI — PHÚ YÊN CŨ ============================

new += [
R("thap-nghinh-phong", "Tháp Nghinh Phong", "Башня Нгиньфонг", "Nghinh Phong Tower",
  ["monument", "square_street"], 13.0808, 109.33,
  "Quảng trường Nghinh Phong, đường Độc Lập, khu vực Tuy Hòa, tỉnh Đắk Lắk", {
  "presentation_short_vi": "Tháp Nghinh Phong là biểu tượng kiến trúc mới bên bờ biển Tuy Hòa, gồm hai cột tháp đá vươn cao tượng trưng cho Lạc Long Quân và Âu Cơ. Công trình lấy cảm hứng từ những cột đá bazan Gành Đá Đĩa, khe hở giữa hai tháp tạo hiệu ứng gió và âm thanh độc đáo. Về đêm, tháp rực rỡ ánh sáng và nhạc nước, thu hút đông người dân và du khách.",
  "presentation_short_en": "Nghinh Phong Tower is a striking new landmark on the Tuy Hòa seafront, made of two soaring stone towers symbolising the legendary ancestors Lạc Long Quân and Âu Cơ. Inspired by the basalt columns of Gành Đá Đĩa, the gap between the towers channels wind and sound in a unique way. By night it glows with lights and a water-music show, drawing crowds of locals and visitors.",
  "presentation_short_ru": "Башня Нгиньфонг — яркий новый символ на набережной Туйхоа: две устремлённые вверх каменные башни, олицетворяющие легендарных прародителей Лаклонгкуана и Ауко. Вдохновлённая базальтовыми колоннами Ганьдадя, щель между башнями по-особому направляет ветер и звук. Ночью башня сияет огнями и шоу «поющих» фонтанов, привлекая местных жителей и туристов.",
  "presentation_long_vi": "Khánh thành năm 2021 tại quảng trường ven biển thành phố Tuy Hòa, Tháp Nghinh Phong nhanh chóng trở thành biểu tượng du lịch mới của vùng đất 'hoa vàng cỏ xanh'. Công trình gồm hai khối tháp đá cao thấp khác nhau, đặt cạnh nhau tượng trưng cho Lạc Long Quân và Âu Cơ — cội nguồn 'con Rồng cháu Tiên' của người Việt. Kiến trúc lấy cảm hứng trực tiếp từ những cột đá bazan hình lăng trụ của thắng cảnh Gành Đá Đĩa gần đó, với khoảng 50 khối đá xếp chồng tạo nên dáng tháp vững chãi mà thanh thoát. Điểm độc đáo nằm ở khe hẹp giữa hai tháp: khi gió biển thổi qua sẽ tạo nên hiệu ứng âm thanh và luồng gió đặc biệt, đúng với tên gọi 'Nghinh Phong' — đón gió. Về đêm, tháp được thắp sáng bằng hệ thống đèn nghệ thuật kết hợp trình diễn nhạc nước sôi động, biến quảng trường thành nơi vui chơi, dạo mát nhộn nhịp bậc nhất thành phố. Công trình từng được vinh danh tại giải thưởng du lịch quốc tế, góp phần đưa hình ảnh Tuy Hòa đến gần hơn với du khách. Với vị trí ngay sát biển, gần Tháp Nhạn và các bãi tắm, Nghinh Phong là điểm check-in không thể bỏ qua khi đến vùng biển này.",
  "presentation_long_en": "Inaugurated in 2021 on the seaside plaza of Tuy Hòa, Nghinh Phong Tower quickly became the new tourism emblem of the land of 'yellow flowers on green grass'. It consists of two stone towers of differing heights, set side by side to symbolise Lạc Long Quân and Âu Cơ — the mythical ancestors of the Vietnamese 'Children of the Dragon and Fairy'. Its architecture draws directly on the prismatic basalt columns of nearby Gành Đá Đĩa, with around fifty stacked blocks forming a shape both sturdy and graceful. Its most unusual feature is the narrow gap between the towers: when the sea breeze passes through, it produces a special sound and airflow, living up to the name 'Nghinh Phong' — welcoming the wind. By night the towers are lit by an artistic lighting system paired with a lively water-music show, turning the plaza into one of the city's busiest places to play and stroll. The project has been honoured at an international travel award, helping bring the image of Tuy Hòa closer to travellers. Right by the sea and close to Nhạn Tower and the beaches, Nghinh Phong is an unmissable check-in spot in this coastal region.",
  "presentation_long_ru": "Открытая в 2021 году на приморской площади Туйхоа, башня Нгиньфонг быстро стала новым туристическим символом края «жёлтых цветов на зелёной траве». Она состоит из двух каменных башен разной высоты, поставленных рядом и символизирующих Лаклонгкуана и Ауко — мифических прародителей вьетнамцев, «детей Дракона и Феи». Её архитектура прямо отсылает к призматическим базальтовым колоннам близлежащего Ганьдадя: около пятидесяти сложенных блоков образуют форму одновременно прочную и изящную. Самая необычная черта — узкая щель между башнями: когда сквозь неё проходит морской бриз, возникают особый звук и поток воздуха, оправдывая название «Нгиньфонг» — «встречающая ветер». Ночью башни освещены художественной подсветкой в сочетании с живым шоу «поющих» фонтанов, превращая площадь в одно из самых оживлённых мест города для прогулок и отдыха. Проект был отмечен международной туристической премией, что помогло приблизить образ Туйхоа к путешественникам. Расположенная у самого моря, рядом с башней Нян и пляжами, Нгиньфонг — обязательное место для фотографий в этом приморском крае.",
  "highlights_vi": [
    "Hai cột tháp đá tượng trưng Lạc Long Quân – Âu Cơ, cảm hứng từ Gành Đá Đĩa",
    "Khe hẹp giữa tháp tạo hiệu ứng 'đón gió' và âm thanh độc đáo",
    "Nhạc nước, ánh sáng nghệ thuật về đêm; biểu tượng mới của Tuy Hòa"],
  "highlights_en": [
    "Two stone towers symbolising Lạc Long Quân and Âu Cơ, inspired by Gành Đá Đĩa",
    "A narrow gap that 'welcomes the wind' with a unique sound effect",
    "Night-time water-music and artistic lighting; the new emblem of Tuy Hòa"],
  "highlights_ru": [
    "Две каменные башни — Лаклонгкуан и Ауко, вдохновлены Ганьдадя",
    "Узкая щель «встречает ветер» с уникальным звуковым эффектом",
    "Вечерние «поющие» фонтаны и подсветка; новый символ Туйхоа"],
  "practical": {
    "hours_vi": "Quảng trường mở tự do; nhạc nước và đèn thường vào buổi tối (cuối tuần).",
    "ticket_vi": "Miễn phí.",
    "duration_vi": "Khoảng 30–60 phút.",
    "best_time_vi": "Buổi tối để xem đèn và nhạc nước; sáng sớm ngắm biển vắng.",
    "tips_vi": "Đến sớm chọn chỗ đẹp buổi tối; kết hợp dạo biển Tuy Hòa và Tháp Nhạn gần đó."},
  "rating": {"value": 4.6, "count": 5200, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Du khách khen tháp đẹp, hoành tráng, buổi tối lung linh với nhạc nước; quảng trường thoáng, sát biển. Nhiều người coi đây là điểm check-in số một ở Tuy Hòa.",
  "tags": ["monument", "landmark", "free", "night", "top", "seaside"],
  "sources": [
    {"title": "Vietnam Airlines — Tháp Nghinh Phong", "url": "https://www.vietnamairlines.com/nl/vi/plan-book/travel/travel-guide/thap-nghinh-phong"},
    {"title": "Cổng du lịch Phú Yên (Đắk Lắk) — Tháp Nghinh Phong", "url": "https://phuyentourism.gov.vn/diem-du-lich/thap-nghinh-phong-phu-yen.html"}]}),

R("bai-xep", "Bãi Xép (phim trường 'Hoa vàng cỏ xanh')", "Пляж Байсеп", "Bai Xep Beach",
  ["park_garden", "other"], 13.22, 109.301,
  "Xã An Chấn (khu vực Tuy An cũ, Phú Yên), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Bãi Xép là bãi biển nhỏ ở An Chấn, nổi tiếng sau khi trở thành phim trường của bộ phim 'Tôi thấy hoa vàng trên cỏ xanh'. Nơi đây có bãi cát vàng, đồng cỏ, hàng xương rồng và những ghềnh đá nhô ra biển xanh. Khung cảnh mộc mạc, nên thơ khiến Bãi Xép thành điểm check-in yêu thích của giới trẻ.",
  "presentation_short_en": "Bai Xep is a small beach in An Chấn, made famous as the filming location of 'Yellow Flowers on the Green Grass'. It has golden sand, grassy meadows, rows of cacti and rocky headlands jutting into the blue sea. Its simple, poetic scenery has made Bai Xep a favourite check-in spot for young travellers.",
  "presentation_short_ru": "Байсеп — небольшой пляж в общине Анчан, прославившийся как место съёмок фильма «Жёлтые цветы на зелёной траве». Здесь золотистый песок, травяные луга, ряды кактусов и скалистые мысы, выступающие в синее море. Простой, поэтичный пейзаж сделал Байсеп любимым местом для фотографий у молодых путешественников.",
  "presentation_long_vi": "Cách trung tâm Tuy Hòa khoảng 14 km về phía bắc, Bãi Xép thuộc xã An Chấn là một bãi biển nhỏ nhưng có sức hút đặc biệt. Trước đây chỉ là bãi biển của làng chài yên tĩnh, Bãi Xép trở nên nổi tiếng khắp cả nước sau khi đạo diễn Victor Vũ chọn làm bối cảnh chính cho bộ phim 'Tôi thấy hoa vàng trên cỏ xanh' (2015) — tác phẩm khắc họa tuổi thơ miền quê đầy hoài niệm. Điều làm nên vẻ đẹp của Bãi Xép là sự kết hợp hài hòa: bãi cát vàng thoai thoải, những triền cỏ xanh mướt, hàng xương rồng và cây bụi mọc trên đồi, cùng các ghềnh đá đen nhô ra ôm lấy làn nước biển trong xanh. Buổi bình minh, mặt trời nhô lên từ biển nhuộm hồng cả không gian; ban ngày, du khách có thể tản bộ trên đồi cỏ, chụp ảnh, tắm biển ở những vũng nước lặng và ngắm thuyền thúng của ngư dân. Nhiều điểm dừng chân nhỏ được dựng lên phục vụ khách tham quan, chụp ảnh. Với khung cảnh mộc mạc, thơ mộng gợi nhớ miền quê Việt, Bãi Xép là điểm đến không thể thiếu trong hành trình khám phá vùng biển Phú Yên xưa, nay thuộc tỉnh Đắk Lắk.",
  "presentation_long_en": "About 14 km north of central Tuy Hòa, Bai Xep in An Chấn commune is a small beach with a special charm. Once merely the shore of a quiet fishing village, it became famous nationwide after director Victor Vũ chose it as the main setting for the film 'Yellow Flowers on the Green Grass' (2015), a nostalgic portrait of rural childhood. Its beauty comes from a harmonious mix: gently sloping golden sand, lush green hillsides, rows of cacti and shrubs on the hills, and black rocky outcrops embracing the clear blue water. At dawn the sun rises from the sea and washes the scene in pink; by day visitors can stroll the grassy hills, take photos, swim in calm rock pools and watch the fishermen's coracles. Small rest stops have sprung up to serve sightseers and photographers. With its simple, poetic scenery evoking the Vietnamese countryside, Bai Xep is a must on any journey exploring the former Phú Yên coast, now part of Đắk Lắk province.",
  "presentation_long_ru": "Примерно в 14 км к северу от центра Туйхоа пляж Байсеп в общине Анчан — небольшой, но особенно обаятельный. Некогда просто берег тихой рыбацкой деревни, он прославился на всю страну после того, как режиссёр Виктор Ву выбрал его главным местом действия фильма «Жёлтые цветы на зелёной траве» (2015), ностальгического портрета сельского детства. Его красота — в гармоничном сочетании: пологий золотистый песок, сочные зелёные склоны, ряды кактусов и кустарников на холмах и чёрные скалистые выступы, обнимающие прозрачную синюю воду. На рассвете солнце поднимается из моря и заливает пейзаж розовым; днём гости могут гулять по травянистым холмам, фотографироваться, купаться в спокойных каменных заводях и смотреть на рыбацкие лодки-корзины. Появились небольшие площадки для отдыха и фотосъёмки. Своим простым, поэтичным пейзажем, напоминающим вьетнамскую деревню, Байсеп обязателен к посещению на маршруте вдоль бывшего побережья Фуйена, ныне входящего в провинцию Даклак.",
  "highlights_vi": [
    "Phim trường 'Tôi thấy hoa vàng trên cỏ xanh' (2015)",
    "Bãi cát vàng, đồi cỏ, hàng xương rồng và ghềnh đá đen",
    "Bình minh trên biển và làng chài mộc mạc, thơ mộng"],
  "highlights_en": [
    "Filming location of 'Yellow Flowers on the Green Grass' (2015)",
    "Golden sand, grassy hills, rows of cacti and black rocky outcrops",
    "Sunrise over the sea and a simple, poetic fishing village"],
  "highlights_ru": [
    "Место съёмок фильма «Жёлтые цветы на зелёной траве» (2015)",
    "Золотистый песок, травяные холмы, кактусы и чёрные скалы",
    "Рассвет над морем и простая, поэтичная рыбацкая деревня"],
  "practical": {
    "hours_vi": "Ban ngày; đẹp nhất lúc bình minh.",
    "ticket_vi": "Vé/giữ xe tượng trưng tại một số điểm; có thể thay đổi.",
    "duration_vi": "Khoảng 1–2 giờ.",
    "best_time_vi": "Sáng sớm đón bình minh; mùa khô (tháng 1–8) biển đẹp.",
    "tips_vi": "Đi sớm tránh nắng; giày bám tốt khi leo ghềnh đá; giữ gìn cảnh quan, mang rác về."},
  "rating": {"value": 4.3, "count": 2600, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách thích cảnh mộc mạc, đồi cỏ và ghềnh đá đẹp để chụp ảnh; bình minh ấn tượng. Một số lưu ý bãi nhỏ, dịch vụ ít và có nơi thu phí chụp ảnh.",
  "tags": ["beach", "film", "photo", "outdoor", "seaside"],
  "sources": [
    {"title": "Vntrip — Bãi Xép Phú Yên", "url": "https://www.vntrip.vn/cam-nang/bai-xep-phu-yen-21107"}]}),

R("mui-dien", "Mũi Điện (Mũi Đại Lãnh)", "Мыс Дьен (Дайлань)", "Dai Lanh Cape (Mui Dien)",
  ["monument", "other"], 12.879, 109.457,
  "Xã Hòa Tâm (khu vực Đông Hòa cũ, Phú Yên), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Mũi Điện, hay Mũi Đại Lãnh, là một trong những điểm cực Đông trên đất liền Việt Nam, nơi có ngọn hải đăng cổ do người Pháp xây từ năm 1890. Đây là địa điểm được yêu thích để đón ánh bình minh đầu tiên trên đất liền. Từ chân hải đăng, du khách phóng tầm mắt ra biển xanh và bãi Môn cát trắng phía dưới.",
  "presentation_short_en": "Dai Lanh Cape, also called Mui Dien, is one of the easternmost points on the Vietnamese mainland, crowned by an old lighthouse built by the French in 1890. It is a beloved place to greet the first sunrise on the mainland. From the lighthouse, visitors gaze over the blue sea and the white sands of Mon Beach below.",
  "presentation_short_ru": "Мыс Дайлань, также называемый Мыс Дьен, — одна из самых восточных точек материкового Вьетнама, увенчанная старым маяком, построенным французами в 1890 году. Это любимое место, чтобы встретить первый рассвет на материке. С маяка открывается вид на синее море и белый песок пляжа Мон внизу.",
  "presentation_long_vi": "Nằm trên bán đảo dưới chân đèo Cả, Mũi Điện (còn gọi Mũi Đại Lãnh) từ lâu được xem là một trong những nơi đón bình minh sớm nhất trên đất liền Việt Nam. Ngọn hải đăng Đại Lãnh sừng sững trên mỏm núi cao hơn 100 m so với mực nước biển, do người Pháp xây dựng năm 1890, thân tháp đá trắng cao khoảng 26 m, đến nay vẫn hoạt động dẫn đường cho tàu thuyền. Để lên tới hải đăng, du khách men theo con đường dốc uốn quanh sườn núi, hai bên là cây rừng và biển xanh mở ra trước mắt; càng lên cao, khung cảnh càng ngoạn mục với vịnh biển, ghềnh đá và bãi Môn hình vòng cung cát trắng nằm ngay bên dưới. Nhiều người chọn cắm trại hoặc thức dậy thật sớm để chờ khoảnh khắc mặt trời nhô lên từ mặt biển — cảm giác như chạm tới nơi bắt đầu một ngày mới của Tổ quốc. Bên cạnh giá trị cảnh quan, khu vực còn gắn với các câu chuyện lịch sử, hàng hải và có tấm bia đánh dấu tọa độ. Kết hợp cùng bãi Môn, vịnh Vũng Rô và đèo Cả gần đó, Mũi Điện tạo thành một cung khám phá tuyệt đẹp ở phía nam vùng biển Phú Yên cũ, nay thuộc Đắk Lắk.",
  "presentation_long_en": "On a peninsula at the foot of Cả Pass, Dai Lanh Cape (Mui Dien) has long been regarded as one of the earliest places to greet the sunrise on the Vietnamese mainland. The Dai Lanh lighthouse stands on a headland more than 100 m above the sea, built by the French in 1890; its white stone tower rises about 26 m and still guides ships today. To reach it, visitors follow a steep road winding around the mountainside, forest on one side and the blue sea opening before them; the higher they climb, the more spectacular the view of bays, rocky reefs and the crescent white sands of Mon Beach just below. Many camp or wake very early to await the moment the sun lifts from the sea — as if touching the place where a new day of the country begins. Beyond its scenery, the area is tied to stories of history and seafaring and has a marker recording its coordinates. Together with Mon Beach, Vũng Rô Bay and nearby Cả Pass, Dai Lanh Cape forms a beautiful exploration route in the south of the former Phú Yên coast, now part of Đắk Lắk.",
  "presentation_long_ru": "На полуострове у подножия перевала Ка мыс Дайлань (Мыс Дьен) издавна считается одним из самых ранних мест встречи рассвета на материковом Вьетнаме. Маяк Дайлань стоит на мысе высотой более 100 м над морем, построен французами в 1890 году; его белая каменная башня поднимается примерно на 26 м и до сих пор указывает путь судам. Чтобы подняться к нему, гости идут по крутой дороге, вьющейся вокруг склона: с одной стороны лес, а впереди открывается синее море; чем выше, тем эффектнее вид на бухты, скалистые рифы и белый серп пляжа Мон прямо внизу. Многие разбивают лагерь или встают очень рано, чтобы дождаться мгновения, когда солнце поднимается из моря, — словно касаясь места, где начинается новый день страны. Помимо пейзажей, местность связана с историей и мореходством, здесь есть знак с координатами. Вместе с пляжем Мон, бухтой Вунгро и близким перевалом Ка мыс Дайлань образует красивый маршрут на юге бывшего побережья Фуйена, ныне части Даклака.",
  "highlights_vi": [
    "Một trong những điểm cực Đông đất liền, đón bình minh sớm nhất",
    "Hải đăng Đại Lãnh do Pháp xây năm 1890, cao ~26 m, còn hoạt động",
    "Tầm nhìn ra vịnh biển và bãi Môn cát trắng phía dưới"],
  "highlights_en": [
    "One of the easternmost mainland points, greeting the earliest sunrise",
    "The Dai Lanh lighthouse, built by the French in 1890, ~26 m, still working",
    "Views over bays and the white sands of Mon Beach below"],
  "highlights_ru": [
    "Одна из самых восточных точек материка, самый ранний рассвет",
    "Маяк Дайлань, построен французами в 1890 году, ~26 м, действует",
    "Виды на бухты и белый песок пляжа Мон внизу"],
  "practical": {
    "hours_vi": "Nên đến sớm đón bình minh; leo bộ đoạn dốc lên hải đăng.",
    "ticket_vi": "Vé tham quan tượng trưng; có thể thay đổi.",
    "duration_vi": "Khoảng 2–3 giờ (cả leo và ngắm cảnh).",
    "best_time_vi": "Rạng sáng đón bình minh; mùa khô (tháng 1–8) trời quang.",
    "tips_vi": "Mang đèn pin, nước, giày leo; đi đèo Cả cẩn thận; kết hợp bãi Môn và Vũng Rô."},
  "rating": {"value": 4.6, "count": 3400, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Du khách mê cảnh bình minh và tầm nhìn hải đăng; nhiều người thấy xứng công leo dốc. Lưu ý đường lên khá dốc, nắng gắt giữa trưa.",
  "tags": ["viewpoint", "lighthouse", "sunrise", "outdoor", "top", "seaside"],
  "sources": [
    {"title": "Wikipedia (VI) — Mũi Đại Lãnh", "url": "https://vi.wikipedia.org/wiki/M%C5%A9i_%C4%90%E1%BA%A1i_L%C3%A3nh"}]}),

R("vung-ro", "Vịnh Vũng Rô", "Бухта Вунгро", "Vung Ro Bay",
  ["park_garden", "other"], 12.87, 109.41,
  "Xã Hòa Xuân Nam (khu vực Đông Hòa cũ, Phú Yên), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Vịnh Vũng Rô là vịnh biển kín gió nằm dưới chân đèo Cả, được núi non ôm trọn ba phía. Đây là di tích lịch sử gắn với những chuyến 'Tàu Không Số' trên Đường Hồ Chí Minh trên biển thời kháng chiến. Ngày nay, vịnh nổi tiếng với làn nước trong xanh, bè nuôi hải sản và những bãi tắm hoang sơ.",
  "presentation_short_en": "Vung Ro Bay is a sheltered bay at the foot of Cả Pass, embraced by mountains on three sides. It is a historic site tied to the 'unnumbered ships' of the sea route of the Hồ Chí Minh Trail during the war. Today the bay is known for its clear blue water, seafood rafts and pristine little beaches.",
  "presentation_short_ru": "Бухта Вунгро — защищённая от ветра бухта у подножия перевала Ка, окружённая горами с трёх сторон. Это историческое место, связанное с «безымянными кораблями» морского маршрута Тропы Хо Ши Мина во время войны. Сегодня бухта известна прозрачной синей водой, плотами для морепродуктов и нетронутыми пляжами.",
  "presentation_long_vi": "Nằm ở phía nam vùng biển Phú Yên cũ, ngay dưới chân đèo Cả hùng vĩ, vịnh Vũng Rô được ba dãy núi Đèo Cả, Đá Bia và Hòn Bà che chắn nên mặt nước quanh năm lặng sóng, xanh ngắt. Vịnh gồm nhiều bãi nhỏ như Bãi Lách, Bãi Mù U, Bãi Ngà... với cát mịn, nước trong và những rạn san hô. Nhưng trên hết, Vũng Rô là một địa danh lịch sử thiêng liêng: trong kháng chiến chống Mỹ, đây là bến tiếp nhận vũ khí của những con 'Tàu Không Số' vượt biển theo Đường Hồ Chí Minh trên biển, và 'Sự kiện Vũng Rô' năm 1965 đã đi vào lịch sử. Ngày nay, khu vực có bia di tích, tượng đài tưởng niệm để du khách tìm hiểu quá khứ hào hùng. Trên vịnh, những bè nổi nuôi tôm hùm, cá, hàu trải dài tạo nên khung cảnh trù phú; du khách có thể đi thuyền tham quan, lặn ngắm san hô, câu cá và thưởng thức hải sản tươi ngon ngay trên bè. Kết hợp với Mũi Điện, đèo Cả và bãi Môn liền kề, Vũng Rô là điểm đến hòa quyện giữa cảnh sắc thiên nhiên tuyệt đẹp và chiều sâu lịch sử, rất đáng ghé trong hành trình khám phá phía nam Đắk Lắk ngày nay.",
  "presentation_long_en": "In the south of the former Phú Yên coast, right at the foot of the mighty Cả Pass, Vung Ro Bay is shielded by three ranges — Đèo Cả, Đá Bia and Hòn Bà — so its waters stay calm and deep blue year-round. The bay holds many small beaches such as Bãi Lách, Bãi Mù U and Bãi Ngà, with fine sand, clear water and coral reefs. Above all, Vung Ro is a sacred historic place: during the war against the US it was a landing point for weapons carried by the 'unnumbered ships' crossing the sea along the Hồ Chí Minh Trail, and the 1965 'Vung Ro Incident' entered history. Today there are a relic marker and a memorial for visitors to learn about this heroic past. On the bay, floating rafts farming lobster, fish and oysters stretch across the water in a scene of plenty; visitors can take boat tours, snorkel over coral, fish and enjoy fresh seafood right on the rafts. Together with nearby Dai Lanh Cape, Cả Pass and Mon Beach, Vung Ro blends stunning natural scenery with historical depth, well worth a visit on any journey through the south of today's Đắk Lắk.",
  "presentation_long_ru": "На юге бывшего побережья Фуйена, у самого подножия могучего перевала Ка, бухта Вунгро защищена тремя хребтами — Дэока, Дабя и Хонба, — поэтому её воды круглый год спокойны и глубоко-сини. В бухте много небольших пляжей, таких как Байлать, Баймуу и Байнга, с мелким песком, прозрачной водой и коралловыми рифами. Но прежде всего Вунгро — священное историческое место: во время войны против США здесь принимали оружие с «безымянных кораблей», пересекавших море по Тропе Хо Ши Мина, а «Инцидент у Вунгро» 1965 года вошёл в историю. Сегодня здесь есть памятный знак и мемориал, чтобы гости узнали об этом героическом прошлом. На воде тянутся плавучие плоты, где выращивают лангустов, рыбу и устриц, создавая картину изобилия; можно совершить лодочную экскурсию, поплавать с маской над кораллами, порыбачить и отведать свежие морепродукты прямо на плотах. Вместе с близкими мысом Дайлань, перевалом Ка и пляжем Мон Вунгро соединяет великолепную природу и историческую глубину и достоин посещения на маршруте по югу нынешнего Даклака.",
  "highlights_vi": [
    "Vịnh kín gió dưới chân đèo Cả, nước trong xanh quanh năm",
    "Di tích 'Tàu Không Số' – Đường Hồ Chí Minh trên biển",
    "Bè nuôi tôm hùm, hải sản tươi và lặn ngắm san hô"],
  "highlights_en": [
    "A sheltered bay at the foot of Cả Pass, clear blue water year-round",
    "A relic of the 'unnumbered ships' of the maritime Hồ Chí Minh Trail",
    "Lobster-farming rafts, fresh seafood and coral snorkelling"],
  "highlights_ru": [
    "Защищённая бухта у подножия перевала Ка, прозрачная синяя вода",
    "Памятник «безымянных кораблей» морской Тропы Хо Ши Мина",
    "Плоты с лангустами, свежие морепродукты и снорклинг у кораллов"],
  "practical": {
    "hours_vi": "Ban ngày; đi thuyền tham quan nên hỏi giờ và thời tiết.",
    "ticket_vi": "Tham quan bến/di tích tự do; thuyền, ăn hải sản trên bè tính phí.",
    "duration_vi": "Khoảng 2–4 giờ.",
    "best_time_vi": "Mùa khô (tháng 1–8), biển êm; sáng sớm mát và đẹp.",
    "tips_vi": "Đi đèo Cả cẩn thận; mặc áo phao khi lên thuyền; hỏi giá hải sản trước khi ăn."},
  "rating": {"value": 4.4, "count": 1800, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách khen vịnh đẹp, nước trong, hải sản tươi và ý nghĩa lịch sử sâu sắc; đi thuyền ngắm bè rất thích. Một số nói đường ra một số bãi còn khó.",
  "tags": ["bay", "history", "seafood", "snorkel", "outdoor", "seaside"],
  "sources": [
    {"title": "Wikipedia (EN) — Vũng Rô Bay", "url": "https://en.wikipedia.org/wiki/V%C5%A9ng_R%C3%B4_Bay"}]}),

R("dam-o-loan", "Đầm Ô Loan", "Лагуна Олоан", "O Loan Lagoon",
  ["park_garden", "other"], 13.2833, 109.2842,
  "Xã An Hải/An Ninh (khu vực Tuy An cũ, Phú Yên), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Đầm Ô Loan là đầm nước lợ nổi tiếng của vùng Tuy An, được bao quanh bởi đồi núi và làng chài. Nhìn từ trên đèo Quán Cau, đầm hiện ra như một tấm gương uốn lượn giữa đồng quê. Nơi đây nức tiếng với sò huyết và hải sản tươi, là thắng cảnh cấp quốc gia.",
  "presentation_short_en": "O Loan Lagoon is a famous brackish-water lagoon in the Tuy An area, ringed by hills and fishing villages. Seen from Quán Cau Pass, it appears as a winding mirror amid the countryside. It is renowned for blood cockles and fresh seafood, and is a national scenic site.",
  "presentation_short_ru": "Лагуна Олоан — знаменитая солоноватоводная лагуна района Туйан, окружённая холмами и рыбацкими деревнями. С перевала Куанкау она выглядит как извилистое зеркало среди сельского пейзажа. Лагуна славится кровяными сердцевидками и свежими морепродуктами и является памятником природы национального значения.",
  "presentation_long_vi": "Nằm ở khu vực Tuy An, cách Tuy Hòa khoảng 25 km về phía bắc, đầm Ô Loan là một trong những thắng cảnh tiêu biểu của vùng biển Phú Yên cũ, đã được xếp hạng danh thắng cấp quốc gia. Đầm rộng khoảng 1.500 ha, là vùng nước lợ được ngăn cách với biển bởi những dải cồn cát, thông ra biển qua cửa Lễ Thịnh. Từ trên đèo Quán Cau nhìn xuống, đầm hiện ra mềm mại với nhiều nhánh uốn lượn như hình con chim phượng đang xòe cánh, xung quanh là ruộng đồng, xóm chài và những rặng núi thấp. Ô Loan nổi danh khắp nước nhờ đặc sản sò huyết béo ngọt, cùng hàu, cua, ghẹ, tôm, điệp... tươi rói được đánh bắt ngay trong đầm. Du khách có thể thuê thuyền dạo trên mặt đầm, ghé làng chài tìm hiểu nghề nuôi trồng thủy sản, ngắm bình minh hoặc hoàng hôn phản chiếu trên mặt nước, và thưởng thức hải sản tại các quán ven đầm. Vào mùng 7 Tết, nơi đây tổ chức lễ hội đua thuyền, đua sõng truyền thống rộn ràng. Với vẻ đẹp thanh bình, thơ mộng cùng ẩm thực trứ danh, đầm Ô Loan là điểm dừng chân khó quên trên cung đường ven biển phía bắc tỉnh Đắk Lắk ngày nay.",
  "presentation_long_en": "In the Tuy An area, about 25 km north of Tuy Hòa, O Loan Lagoon is one of the signature scenic spots of the former Phú Yên coast and is ranked a national landscape site. The lagoon covers around 1,500 hectares of brackish water, separated from the sea by sand spits and opening to it through the Lễ Thịnh mouth. Seen from Quán Cau Pass, it unfolds softly with many winding arms, likened to a phoenix spreading its wings, ringed by fields, fishing hamlets and low hills. O Loan is famous nationwide for its plump, sweet blood cockles, along with oysters, crab, shrimp and scallops caught fresh in the lagoon. Visitors can hire a boat to glide across the water, visit fishing villages to learn about aquaculture, watch the sunrise or sunset mirrored on the surface, and enjoy seafood at lagoon-side eateries. On the seventh day of the Lunar New Year, a lively traditional boat race is held here. With its peaceful, poetic beauty and celebrated cuisine, O Loan Lagoon is an unforgettable stop on the coastal route in the north of today's Đắk Lắk province.",
  "presentation_long_ru": "В районе Туйан, примерно в 25 км к северу от Туйхоа, лагуна Олоан — одно из знаковых живописных мест бывшего побережья Фуйена, отнесённое к памятникам природы национального значения. Лагуна занимает около 1500 гектаров солоноватой воды, отделённой от моря песчаными косами и соединяющейся с ним через устье Летхинь. С перевала Куанкау она мягко разворачивается множеством извилистых рукавов, напоминая феникса, расправляющего крылья, в окружении полей, рыбацких посёлков и невысоких холмов. Олоан славится на всю страну сочными сладкими кровяными сердцевидками, а также устрицами, крабами, креветками и гребешками, выловленными прямо в лагуне. Гости могут взять лодку и скользить по воде, посетить рыбацкие деревни и узнать об аквакультуре, полюбоваться рассветом или закатом, отражёнными на поверхности, и отведать морепродукты в прибрежных кафе. На седьмой день лунного Нового года здесь проводят оживлённые традиционные лодочные гонки. Своей тихой, поэтичной красотой и прославленной кухней лагуна Олоан — незабываемая остановка на прибрежном маршруте на севере нынешней провинции Даклак.",
  "highlights_vi": [
    "Danh thắng quốc gia, đầm nước lợ hình phượng nhìn từ đèo Quán Cau",
    "Nổi tiếng sò huyết, hàu và hải sản tươi ngon",
    "Làng chài, đua thuyền mùng 7 Tết và cảnh bình minh – hoàng hôn"],
  "highlights_en": [
    "A national scenic site; a phoenix-shaped lagoon seen from Quán Cau Pass",
    "Famous for blood cockles, oysters and fresh seafood",
    "Fishing villages, a New Year boat race and sunrise–sunset scenery"],
  "highlights_ru": [
    "Памятник природы; лагуна в форме феникса с перевала Куанкау",
    "Славится кровяными сердцевидками, устрицами и морепродуктами",
    "Рыбацкие деревни, новогодние лодочные гонки и рассветы–закаты"],
  "practical": {
    "hours_vi": "Tham quan tự do ban ngày; thuyền và quán hải sản ven đầm.",
    "ticket_vi": "Vào tự do; thuê thuyền và ăn uống tính phí.",
    "duration_vi": "Khoảng 1,5–2,5 giờ.",
    "best_time_vi": "Bình minh/hoàng hôn đẹp; mùng 7 Tết có lễ hội đua thuyền.",
    "tips_vi": "Dừng trên đèo Quán Cau ngắm toàn cảnh; hỏi giá hải sản trước; đi thuyền mặc áo phao."},
  "rating": {"value": 4.3, "count": 1600, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách khen cảnh đầm nên thơ nhìn từ đèo và sò huyết ngon nổi tiếng; hoàng hôn đẹp. Một số nhắc quán ven đầm nên hỏi giá trước.",
  "tags": ["lagoon", "seafood", "viewpoint", "outdoor", "seaside"],
  "sources": [
    {"title": "Wikipedia (VI) — Đầm Ô Loan", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BA%A7m_%C3%94_Loan"}]}),

R("nha-tho-mang-lang", "Nhà thờ Mằng Lăng", "Церковь Манглang", "Mang Lang Church",
  ["church"], 13.3478, 109.267,
  "Xã An Thạch (khu vực Tuy An cũ, Phú Yên), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Nhà thờ Mằng Lăng là một trong những nhà thờ cổ nhất Việt Nam, xây năm 1892 theo phong cách Gothic. Đây là nơi lưu giữ cuốn 'Phép giảng tám ngày' — cuốn sách in bằng chữ Quốc ngữ đầu tiên. Nhà thờ cũng gắn với chân phước Anrê Phú Yên, vị tử đạo tiên khởi của Việt Nam.",
  "presentation_short_en": "Mang Lang Church is one of the oldest churches in Vietnam, built in 1892 in the Gothic style. It preserves 'Phép giảng tám ngày', the first book ever printed in the Vietnamese romanised script. The church is also linked to Blessed Andrew of Phú Yên, Vietnam's first martyr.",
  "presentation_short_ru": "Церковь Манглanг — одна из старейших церквей Вьетнама, построенная в 1892 году в готическом стиле. Здесь хранится книга «Phép giảng tám ngày» — первая книга, напечатанная вьетнамской латиницей. Церковь также связана с блаженным Андреем Фуйенским, первым мучеником Вьетнама.",
  "presentation_long_vi": "Tọa lạc bên dòng sông Cái ở khu vực Tuy An, cách Tuy Hòa khoảng 35 km về phía bắc, nhà thờ Mằng Lăng được xây dựng năm 1892 và là một trong những nhà thờ Công giáo cổ nhất còn lại ở Việt Nam. Công trình mang đậm phong cách kiến trúc Gothic với hai tháp chuông vươn cao, những ô cửa vòm nhọn và gam màu xanh xám trầm mặc, nổi bật giữa khung cảnh làng quê thanh bình. Cái tên 'Mằng Lăng' được cho là bắt nguồn từ loài cây từng mọc nhiều quanh vùng. Điều làm nên giá trị đặc biệt của nhà thờ là mối liên hệ với lịch sử chữ Quốc ngữ: nơi đây lưu giữ và trưng bày cuốn 'Phép giảng tám ngày' của giáo sĩ Alexandre de Rhodes, in năm 1651 tại Roma — được xem là cuốn sách in bằng chữ Quốc ngữ đầu tiên. Mằng Lăng cũng gắn với chân phước Anrê Phú Yên, vị tử đạo tiên khởi của Giáo hội Công giáo Việt Nam. Trong khuôn viên có một hang đá nhân tạo trưng bày tư liệu về lịch sử nhà thờ và vùng đất. Với vẻ cổ kính, trầm mặc và ý nghĩa văn hóa – lịch sử sâu sắc, nhà thờ Mằng Lăng là điểm đến hấp dẫn không chỉ với tín hữu mà với mọi du khách quan tâm đến di sản của vùng biển Phú Yên xưa, nay thuộc Đắk Lắk.",
  "presentation_long_en": "On the bank of the Cái River in the Tuy An area, about 35 km north of Tuy Hòa, Mang Lang Church was built in 1892 and is one of the oldest surviving Catholic churches in Vietnam. It is strongly Gothic in style, with two tall bell towers, pointed arched windows and a subdued grey-blue tone, standing out amid a peaceful rural setting. The name 'Mằng Lăng' is thought to come from a tree once common in the area. What makes the church especially significant is its link to the history of the Vietnamese script: it keeps and displays a copy of Alexandre de Rhodes's 'Phép giảng tám ngày', printed in Rome in 1651 — regarded as the first book printed in the romanised Vietnamese script. Mang Lang is also tied to Blessed Andrew of Phú Yên, the first martyr of the Vietnamese Catholic Church. In the grounds an artificial grotto displays documents on the history of the church and the region. With its ancient, contemplative beauty and deep cultural and historical meaning, Mang Lang Church appeals not only to the faithful but to any traveller interested in the heritage of the former Phú Yên coast, now part of Đắk Lắk.",
  "presentation_long_ru": "На берегу реки Кай в районе Туйан, примерно в 35 км к северу от Туйхоа, церковь Манглanг была построена в 1892 году и является одной из старейших сохранившихся католических церквей Вьетнама. Она выдержана в готическом стиле — две высокие колокольни, стрельчатые арочные окна и приглушённый серо-голубой тон — и выделяется среди мирного сельского пейзажа. Считается, что название «Манглanг» происходит от дерева, некогда распространённого в этих местах. Особую значимость церкви придаёт связь с историей вьетнамской письменности: здесь хранится и выставлена книга «Phép giảng tám ngày» миссионера Александра де Рода, напечатанная в Риме в 1651 году и считающаяся первой книгой на вьетнамской латинице. Манглang также связана с блаженным Андреем Фуйенским, первым мучеником вьетнамской католической церкви. На территории искусственный грот с документами об истории церкви и края. Своей древней, созерцательной красотой и глубоким культурно-историческим смыслом церковь Манглang привлекает не только верующих, но и любого путешественника, интересующегося наследием бывшего побережья Фуйена, ныне части Даклака.",
  "highlights_vi": [
    "Một trong những nhà thờ cổ nhất Việt Nam (1892), phong cách Gothic",
    "Lưu giữ 'Phép giảng tám ngày' — sách in chữ Quốc ngữ đầu tiên (1651)",
    "Gắn với chân phước Anrê Phú Yên, vị tử đạo tiên khởi Việt Nam"],
  "highlights_en": [
    "One of Vietnam's oldest churches (1892), in the Gothic style",
    "Keeps 'Phép giảng tám ngày', the first romanised-Vietnamese book (1651)",
    "Linked to Blessed Andrew of Phú Yên, Vietnam's first martyr"],
  "highlights_ru": [
    "Одна из старейших церквей Вьетнама (1892) в готическом стиле",
    "Хранит «Phép giảng tám ngày» — первую книгу на вьетнамской латинице (1651)",
    "Связана с блаженным Андреем Фуйенским, первым мучеником Вьетнама"],
  "practical": {
    "hours_vi": "Mở cửa ban ngày cho khách tham quan; giữ trật tự khi có thánh lễ.",
    "ticket_vi": "Miễn phí.",
    "duration_vi": "Khoảng 45–60 phút.",
    "best_time_vi": "Buổi sáng ánh sáng đẹp; tránh giờ lễ nếu chỉ tham quan.",
    "tips_vi": "Ăn mặc lịch sự, giữ yên tĩnh; ghé hang đá xem sách cổ và tư liệu."},
  "rating": {"value": 4.6, "count": 2200, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Du khách ấn tượng vẻ cổ kính, kiến trúc Gothic và giá trị lịch sử của cuốn sách Quốc ngữ đầu tiên. Nhiều người thấy không gian yên bình, đáng chiêm nghiệm.",
  "tags": ["church", "history", "architecture", "free", "culture", "top"],
  "sources": [
    {"title": "Wikipedia (VI) — Nhà thờ Mằng Lăng", "url": "https://vi.wikipedia.org/wiki/Nh%C3%A0_th%E1%BB%9D_M%E1%BA%B1ng_L%C4%83ng"}]}),

R("nui-da-bia", "Núi Đá Bia", "Гора Дабя", "Da Bia Mountain",
  ["park_garden", "other"], 12.885, 109.383,
  "Xã Hòa Xuân Nam (khu vực Đông Hòa cũ, Phú Yên), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Núi Đá Bia là ngọn núi cao khoảng 706 m bên đèo Cả, trên đỉnh có khối đá khổng lồ nổi bật như tấm bia trời. Gắn với truyền thuyết vua Lê Thánh Tông, đây là điểm leo núi và ngắm toàn cảnh biển trời phía nam Phú Yên. Đường mòn xuyên rừng dẫn lên đỉnh là thử thách thú vị cho người ưa vận động.",
  "presentation_short_en": "Da Bia Mountain rises about 706 m beside Cả Pass, crowned by a huge boulder that stands out like a stele in the sky. Tied to a legend of King Lê Thánh Tông, it is a spot for hiking and sweeping views over the sea and land of southern Phú Yên. The forest trail to the top is an enjoyable challenge for active travellers.",
  "presentation_short_ru": "Гора Дабя высотой около 706 м стоит у перевала Ка, увенчанная огромным валуном, выделяющимся, словно стела в небе. Связанная с легендой о короле Ле Тхань Тонге, она — место для походов и панорамных видов на море и сушу юга Фуйена. Лесная тропа к вершине — приятное испытание для активных путешественников.",
  "presentation_long_vi": "Nằm sừng sững bên đèo Cả ở phía nam vùng biển Phú Yên cũ, núi Đá Bia cao khoảng 706 m và được nhận ra từ xa nhờ khối đá khổng lồ trên đỉnh, cao hàng chục mét, trông như một tấm bia dựng giữa trời — vì thế mà có tên Đá Bia. Ngọn núi gắn liền với truyền thuyết rằng vua Lê Thánh Tông trong chuyến nam chinh năm 1471 đã cho khắc chữ lên đá để đánh dấu cương vực, nên nơi đây còn được gọi là Thạch Bi Sơn và mang ý nghĩa lịch sử về mở cõi. Để chinh phục đỉnh, du khách theo con đường mòn dài khoảng 2,2 km xuyên qua rừng cây, vượt các bậc dốc và những đoạn đá, mất chừng một đến hai giờ leo. Phần thưởng cho nỗ lực ấy là khung cảnh ngoạn mục trên đỉnh: toàn cảnh vịnh Vũng Rô, đồng bằng Tuy Hòa, biển Đông xanh thẳm và đèo Cả uốn lượn hiện ra dưới chân. Vào những ngày trời quang, gió lồng lộng và mây vờn quanh khối đá tạo cảm giác phiêu diêu khó tả. Với sự kết hợp giữa thiên nhiên hùng vĩ, dấu ấn lịch sử và trải nghiệm leo núi, Đá Bia là điểm đến hấp dẫn cho những ai yêu khám phá khi đến phía nam tỉnh Đắk Lắk ngày nay.",
  "presentation_long_en": "Towering beside Cả Pass in the south of the former Phú Yên coast, Da Bia Mountain rises about 706 m and is recognised from afar by the huge boulder on its summit, tens of metres tall, looking like a stele set in the sky — hence the name Đá Bia (Stele Rock). The mountain is bound to a legend that King Lê Thánh Tông, during his southern campaign of 1471, had characters carved on the rock to mark the frontier, so it is also called Thạch Bi Sơn and carries historical meaning about expanding the realm. To reach the top, visitors follow a trail about 2.2 km long through the forest, climbing steps, slopes and rocky sections in roughly one to two hours. The reward is a spectacular summit panorama: all of Vũng Rô Bay, the Tuy Hòa plain, the deep-blue East Sea and the winding Cả Pass laid out below. On clear days, strong winds and clouds drifting around the boulder create an almost otherworldly feeling. Combining grand nature, a historical mark and a hiking experience, Da Bia is an appealing destination for explorers visiting the south of today's Đắk Lắk province.",
  "presentation_long_ru": "Возвышаясь у перевала Ка на юге бывшего побережья Фуйена, гора Дабя поднимается примерно на 706 м и узнаётся издалека по огромному валуну на вершине высотой в десятки метров, похожему на стелу в небе, — отсюда и название Дабя («Скала-стела»). Гора связана с легендой о том, что король Ле Тхань Тонг во время южного похода 1471 года велел вырезать на скале письмена, чтобы обозначить границу, поэтому её также называют Тхатьбишон, и она несёт исторический смысл расширения державы. Чтобы подняться на вершину, гости идут по тропе длиной около 2,2 км через лес, преодолевая ступени, склоны и каменистые участки примерно за один-два часа. Наградой становится захватывающая панорама с вершины: вся бухта Вунгро, равнина Туйхоа, тёмно-синее Восточное море и извилистый перевал Ка внизу. В ясные дни сильный ветер и облака, кружащие вокруг валуна, создают почти неземное ощущение. Сочетая величие природы, исторический след и походный опыт, Дабя — привлекательное место для любителей открытий на юге нынешней провинции Даклак.",
  "highlights_vi": [
    "Khối đá khổng lồ trên đỉnh cao ~706 m, gọi là Thạch Bi Sơn",
    "Gắn truyền thuyết vua Lê Thánh Tông khắc bia định cương vực (1471)",
    "Trek ~2,2 km, đỉnh nhìn ra Vũng Rô, đèo Cả và biển Đông"],
  "highlights_en": [
    "A giant boulder on the ~706 m summit, called Thạch Bi Sơn",
    "Legend of King Lê Thánh Tông carving a border stele (1471)",
    "A ~2.2 km trek; the summit overlooks Vũng Rô, Cả Pass and the sea"],
  "highlights_ru": [
    "Гигантский валун на вершине ~706 м, называемой Тхатьбишон",
    "Легенда о короле Ле Тхань Тонге и пограничной стеле (1471)",
    "Трек ~2,2 км; с вершины вид на Вунгро, перевал Ка и море"],
  "practical": {
    "hours_vi": "Nên bắt đầu leo buổi sáng sớm để tránh nắng; xuống trước chiều tối.",
    "ticket_vi": "Vé tham quan/leo núi tượng trưng; có thể thay đổi.",
    "duration_vi": "Khoảng 3–5 giờ cả lên xuống.",
    "best_time_vi": "Mùa khô (tháng 1–8), trời quang; sáng sớm mát mẻ.",
    "tips_vi": "Mang giày trek, nước, mũ; đi theo nhóm; không leo khi trời mưa trơn."},
  "rating": {"value": 4.4, "count": 1300, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Dân leo núi khen cung trek đẹp, đỉnh nhìn toàn cảnh biển và đèo Cả rất đáng công. Một số nhắc đường dốc, cần thể lực và chuẩn bị nước.",
  "tags": ["mountain", "trekking", "viewpoint", "history", "outdoor"],
  "sources": [
    {"title": "Wikipedia (VI) — Núi Đá Bia", "url": "https://vi.wikipedia.org/wiki/N%C3%BAi_%C4%90%C3%A1_Bia"}]}),
]

new += [
R("vinh-xuan-dai", "Vịnh Xuân Đài", "Залив Суандай", "Xuan Dai Bay",
  ["park_garden", "other"], 13.4667, 109.25,
  "Khu vực Sông Cầu (Phú Yên cũ), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Vịnh Xuân Đài là vịnh biển rộng và đẹp ở khu vực Sông Cầu, được xếp hạng danh thắng cấp quốc gia. Vịnh có nhiều vũng, đảo nhỏ và bán đảo, mặt nước lặng in bóng núi non trùng điệp. Đây còn là vựa tôm hùm, hàu nổi tiếng của vùng biển này.",
  "presentation_short_en": "Xuan Dai Bay is a broad, beautiful bay in the Sông Cầu area, ranked a national scenic site. It has many coves, islets and peninsulas, with calm water mirroring rows of mountains. It is also a renowned centre for lobster and oyster farming on this coast.",
  "presentation_short_ru": "Залив Суандай — широкий и красивый залив в районе Шонгкау, отнесённый к памятникам природы национального значения. В нём множество бухт, островков и полуостровов, а спокойная вода отражает гряды гор. Это также известный центр разведения лангустов и устриц на этом побережье.",
  "presentation_long_vi": "Nằm ở phía bắc vùng biển Phú Yên cũ, thuộc khu vực thị xã Sông Cầu, vịnh Xuân Đài trải rộng khoảng 13.000 ha với đường bờ uốn lượn dài hàng chục cây số, được công nhận là danh lam thắng cảnh cấp quốc gia. Vịnh được che chắn bởi dãy núi Cổ Ngựa chạy dài ra biển, tạo nên hình dáng độc đáo và mặt nước kín gió, êm ả quanh năm. Bên trong vịnh là cả một hệ thống vũng, gành, bãi tắm và đảo nhỏ như Vũng La, Vũng Sứ, Vũng Chào, Cù Lao Ông Xá... mỗi nơi một vẻ, nước trong xanh và cảnh sắc nguyên sơ. Từ trên đèo hoặc các điểm cao nhìn xuống, Xuân Đài hiện ra như một bức tranh thủy mặc với núi, biển, trời hòa quyện. Đây cũng là vùng nuôi trồng thủy sản trù phú, đặc biệt nổi tiếng với tôm hùm và hàu — những đặc sản khiến ẩm thực Sông Cầu được nhiều người tìm đến. Du khách có thể đi thuyền tham quan các vũng, tắm biển, lặn ngắm san hô, ghé bè nổi thưởng thức hải sản tươi, hoặc đơn giản là ngắm bình minh, hoàng hôn tuyệt đẹp. Với sự kết hợp giữa cảnh quan hùng vĩ và đời sống ngư dân sinh động, vịnh Xuân Đài là điểm đến hấp dẫn ở phía bắc tỉnh Đắk Lắk ngày nay.",
  "presentation_long_en": "In the north of the former Phú Yên coast, in the Sông Cầu area, Xuan Dai Bay spreads over about 13,000 hectares with a winding shoreline tens of kilometres long, recognised as a national scenic landscape. The bay is sheltered by the Cổ Ngựa range running out to sea, giving it a distinctive shape and calm, wind-protected water year-round. Within it lies a whole system of coves, headlands, beaches and islets — Vũng La, Vũng Sứ, Vũng Chào, Cù Lao Ông Xá and more — each with its own character, clear water and pristine scenery. Seen from a pass or high point, Xuan Dai appears like an ink-wash painting where mountains, sea and sky merge. It is also a rich aquaculture area, especially famous for lobster and oysters — specialities that draw many to Sông Cầu's cuisine. Visitors can take boat tours of the coves, swim, snorkel over coral, stop at floating rafts for fresh seafood, or simply enjoy the superb sunrises and sunsets. Combining majestic scenery with vivid fishing life, Xuan Dai Bay is an appealing destination in the north of today's Đắk Lắk province.",
  "presentation_long_ru": "На севере бывшего побережья Фуйена, в районе Шонгкау, залив Суандай раскинулся примерно на 13 000 гектаров с извилистой береговой линией в десятки километров и признан памятником природы национального значения. Залив защищён хребтом Конгыа, уходящим в море, что придаёт ему своеобразную форму и спокойную, укрытую от ветра воду круглый год. Внутри — целая система бухт, мысов, пляжей и островков: Вунгла, Вунгшы, Вунгтяо, Кулаоонгса и другие, каждый со своим характером, прозрачной водой и первозданными видами. С перевала или высокой точки Суандай выглядит как картина тушью, где сливаются горы, море и небо. Это также богатый район аквакультуры, особенно славящийся лангустами и устрицами — деликатесами, ради которых многие едут за кухней Шонгкау. Гости могут совершить лодочные экскурсии по бухтам, купаться, плавать с маской над кораллами, останавливаться у плавучих плотов ради свежих морепродуктов или просто любоваться великолепными рассветами и закатами. Сочетая величественные пейзажи и живую рыбацкую жизнь, залив Суандай — привлекательное место на севере нынешней провинции Даклак.",
  "highlights_vi": [
    "Danh thắng quốc gia, vịnh rộng ~13.000 ha nhiều vũng và đảo nhỏ",
    "Được núi Cổ Ngựa che chắn, nước lặng, cảnh như tranh thủy mặc",
    "Vựa tôm hùm, hàu; đi thuyền, lặn san hô và ăn hải sản trên bè"],
  "highlights_en": [
    "A national scenic site; a ~13,000 ha bay with many coves and islets",
    "Sheltered by the Cổ Ngựa range, calm water, ink-wash-like scenery",
    "A lobster and oyster hub; boat tours, coral snorkelling and raft seafood"],
  "highlights_ru": [
    "Памятник природы; залив ~13 000 га с множеством бухт и островков",
    "Укрыт хребтом Конгыа, спокойная вода, пейзаж как тушью",
    "Центр лангустов и устриц; лодки, снорклинг и морепродукты на плотах"],
  "practical": {
    "hours_vi": "Ban ngày; đi thuyền tham quan tùy thời tiết, nên hỏi trước.",
    "ticket_vi": "Ngắm cảnh tự do; thuyền và ăn hải sản trên bè tính phí.",
    "duration_vi": "Nửa ngày nếu đi thuyền quanh vịnh.",
    "best_time_vi": "Mùa khô (tháng 1–8), biển êm; bình minh và hoàng hôn đẹp.",
    "tips_vi": "Mặc áo phao khi lên thuyền; hỏi giá tôm hùm/hàu trước; chống nắng."},
  "rating": {"value": 4.4, "count": 1100, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách khen vịnh đẹp, yên bình, hải sản tươi ngon và đi thuyền ngắm cảnh thích; hoàng hôn ấn tượng. Một số nói cần chủ động thuê thuyền và hỏi giá.",
  "tags": ["bay", "seafood", "viewpoint", "boat", "outdoor", "seaside"],
  "sources": [
    {"title": "Wikipedia (VI) — Vịnh Xuân Đài", "url": "https://vi.wikipedia.org/wiki/V%E1%BB%8Bnh_Xu%C3%A2n_%C4%90%C3%A0i"}]}),

R("dap-dong-cam", "Đập Đồng Cam", "Плотина Донгкам", "Dong Cam Dam",
  ["monument", "other"], 13.0333, 109.117,
  "Xã Hòa Hội (khu vực Phú Hòa cũ, Phú Yên), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Đập Đồng Cam là công trình thủy nông lớn trên sông Ba, do người Pháp xây dựng những năm 1924–1932. Đập đưa nước tưới cho cả vùng đồng bằng Tuy Hòa, được coi là một kỳ tích kỹ thuật thời bấy giờ. Cảnh quan đập nước, kênh mương giữa núi đồi tạo nên nơi tham quan, chụp ảnh thú vị.",
  "presentation_short_en": "Dong Cam Dam is a major irrigation work on the Ba River, built by the French in 1924–1932. It brings water to the whole Tuy Hòa plain and was considered an engineering feat of its time. The scenery of the weir and canals among the hills makes for an interesting place to visit and photograph.",
  "presentation_short_ru": "Плотина Донгкам — крупное ирригационное сооружение на реке Ба, построенное французами в 1924–1932 годах. Она орошает всю равнину Туйхоа и считалась инженерным достижением своего времени. Пейзаж водослива и каналов среди холмов делает это место интересным для посещения и фотографий.",
  "presentation_long_vi": "Nằm ở khu vực Phú Hòa, cách Tuy Hòa khoảng 30 km về phía tây, đập Đồng Cam là một trong những công trình thủy nông có quy mô và giá trị lịch sử bậc nhất miền Trung. Được người Pháp khởi công năm 1924 và hoàn thành năm 1932, đập chắn ngang dòng sông Ba (sông Đà Rằng) để dâng nước, dẫn vào hệ thống kênh mương tưới cho hàng chục nghìn héc-ta ruộng đồng của cánh đồng Tuy Hòa — vựa lúa lớn của khu vực. Vào thời điểm ấy, việc xây dựng đập giữa vùng sông nước, núi non hiểm trở bằng sức người là một kỳ tích kỹ thuật, và không ít công nhân đã ngã xuống trong quá trình thi công; vì thế nơi đây còn có miếu thờ tưởng niệm. Ngày nay, đập vẫn vận hành, trở thành biểu tượng cho tinh thần lao động và trị thủy của người dân Phú Yên. Cảnh quan quanh đập rất nên thơ: dòng nước tràn qua thân đập tung bọt trắng, những tuyến kênh xanh mát chạy giữa đồng lúa và đồi núi. Hằng năm vào ngày mùng 8 tháng Giêng, lễ hội Đập Đồng Cam được tổ chức để tri ân những người xây đập, thu hút đông đảo người dân. Với du khách ưa tìm hiểu, Đồng Cam là điểm đến kết hợp giữa di sản kỹ thuật, lịch sử và cảnh quan đồng quê yên bình.",
  "presentation_long_en": "In the Phú Hòa area, about 30 km west of Tuy Hòa, Dong Cam Dam is one of central Vietnam's largest and most historically valuable irrigation works. Begun by the French in 1924 and completed in 1932, the dam spans the Ba River (Đà Rằng) to raise the water and feed a canal system irrigating tens of thousands of hectares of the Tuy Hòa fields — a major rice basket of the region. At the time, building the dam amid rugged rivers and mountains by hand was an engineering feat, and many workers died during construction, which is why a memorial shrine stands here. The dam still operates today and has become a symbol of the labour and water-taming spirit of the Phú Yên people. The surroundings are poetic: water spilling over the dam in white foam, and cool green canals running between rice fields and hills. Each year on the eighth day of the first lunar month, the Dong Cam Dam festival is held to honour those who built it, drawing large crowds. For inquisitive travellers, Dong Cam combines engineering heritage, history and peaceful rural scenery.",
  "presentation_long_ru": "В районе Фухоа, примерно в 30 км к западу от Туйхоа, плотина Донгкам — одно из крупнейших и наиболее исторически ценных ирригационных сооружений центрального Вьетнама. Начатая французами в 1924 году и завершённая в 1932-м, плотина перекрывает реку Ба (Дяранг), поднимая воду и питая систему каналов, орошающих десятки тысяч гектаров полей Туйхоа — крупной рисовой житницы региона. По тем временам возведение плотины среди труднодоступных рек и гор вручную было инженерным подвигом, и многие рабочие погибли при строительстве, поэтому здесь стоит поминальный храм. Плотина работает и сегодня и стала символом труда и водоукрощения народа Фуйена. Окрестности поэтичны: вода, переливающаяся через тело плотины белой пеной, и прохладные зелёные каналы среди рисовых полей и холмов. Ежегодно на восьмой день первого лунного месяца проводится праздник плотины Донгкам в честь её строителей, собирающий много людей. Для любознательных путешественников Донгкам сочетает инженерное наследие, историю и мирный сельский пейзаж.",
  "highlights_vi": [
    "Công trình thủy nông trên sông Ba do Pháp xây 1924–1932",
    "Tưới cho đồng Tuy Hòa; kỳ tích kỹ thuật, có miếu tưởng niệm",
    "Lễ hội Đập Đồng Cam mùng 8 tháng Giêng, cảnh kênh nước nên thơ"],
  "highlights_en": [
    "An irrigation work on the Ba River, built by the French in 1924–1932",
    "Waters the Tuy Hòa plain; an engineering feat with a memorial shrine",
    "The Dong Cam festival on the 8th of the first lunar month; poetic canals"],
  "highlights_ru": [
    "Ирригационное сооружение на реке Ба, построено французами в 1924–1932",
    "Орошает равнину Туйхоа; инженерный подвиг, есть поминальный храм",
    "Праздник Донгкам на 8-й день 1-го лунного месяца; поэтичные каналы"],
  "practical": {
    "hours_vi": "Tham quan tự do ban ngày; mùa nước tràn đập đẹp nhất.",
    "ticket_vi": "Miễn phí.",
    "duration_vi": "Khoảng 45–60 phút.",
    "best_time_vi": "Mùa nước lớn nước tràn đập; mùng 8 tháng Giêng có lễ hội.",
    "tips_vi": "Cẩn thận trơn trượt gần thân đập; kết hợp ngắm đồng lúa Tuy Hòa."},
  "rating": {"value": 4.3, "count": 800, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách thấy đập bề thế, cảnh nước tràn và đồng quê đẹp; ý nghĩa lịch sử rõ nét. Một số nói nên đi mùa nước để thấy đập tràn đẹp.",
  "tags": ["heritage", "history", "free", "outdoor", "countryside"],
  "sources": [
    {"title": "Wikipedia (VI) — Đập Đồng Cam", "url": "https://vi.wikipedia.org/wiki/%C4%90%E1%BA%ADp_%C4%90%E1%BB%93ng_Cam"}]}),

R("bai-mon", "Bãi Môn", "Пляж Мон", "Mon Beach",
  ["park_garden", "other"], 12.8815, 109.4525,
  "Xã Hòa Tâm (khu vực Đông Hòa cũ, Phú Yên), dưới chân Mũi Điện, tỉnh Đắk Lắk", {
  "presentation_short_vi": "Bãi Môn là bãi biển hình vòng cung nằm ngay dưới chân hải đăng Mũi Điện, với cát trắng mịn và làn nước trong xanh. Một dòng suối nước ngọt chảy vắt ngang bãi ra biển tạo nét độc đáo hiếm có. Đây là nơi lý tưởng để cắm trại, tắm biển và đón bình minh cực Đông.",
  "presentation_short_en": "Mon Beach is a crescent-shaped beach right at the foot of the Dai Lanh lighthouse, with fine white sand and clear blue water. A freshwater stream crosses the beach to the sea, a rare and distinctive touch. It is an ideal place to camp, swim and greet the easternmost sunrise.",
  "presentation_short_ru": "Пляж Мон — пляж в форме полумесяца у самого подножия маяка Дайлань, с мелким белым песком и прозрачной синей водой. Через пляж к морю течёт пресноводный ручей — редкая и характерная деталь. Это идеальное место, чтобы разбить лагерь, купаться и встретить самый восточный рассвет.",
  "presentation_long_vi": "Nằm ngay dưới chân ngọn hải đăng Mũi Điện ở phía nam vùng biển Phú Yên cũ, Bãi Môn là một trong những bãi biển đẹp và hoang sơ bậc nhất khu vực. Bãi có hình vòng cung dài khoảng 400 m, cát trắng mịn thoai thoải, hai đầu là những mỏm núi đá ôm lấy vùng nước trong xanh, tạo nên khung cảnh vừa kín đáo vừa nên thơ. Điểm đặc biệt của Bãi Môn là dòng suối nước ngọt từ trong núi chảy vắt ngang bãi cát rồi đổ ra biển — sự giao hòa hiếm thấy giữa nước ngọt và nước mặn, khiến du khách có thể vừa tắm biển vừa nghịch suối. Vì nằm gần điểm cực Đông trên đất liền, đây cũng là nơi lý tưởng để cắm trại qua đêm và thức dậy đón ánh bình minh đầu tiên trước khi leo lên hải đăng. Bãi còn khá vắng, giữ được vẻ tự nhiên với rừng cây, ghềnh đá và làn nước sạch, phù hợp cho những ai muốn tìm một nơi yên tĩnh, gần gũi thiên nhiên. Kết hợp cùng Mũi Điện, đèo Cả và vịnh Vũng Rô, Bãi Môn là mắt xích đẹp trong cung khám phá phía nam của tỉnh Đắk Lắk ngày nay, để lại ấn tượng khó quên về một vùng biển trong lành, hoang sơ.",
  "presentation_long_en": "Right at the foot of the Dai Lanh lighthouse in the south of the former Phú Yên coast, Mon Beach is one of the most beautiful and unspoilt beaches in the area. The crescent stretches about 400 m, with gently sloping fine white sand and rocky headlands at each end embracing the clear blue water, creating scenery both secluded and poetic. Its special feature is a freshwater stream flowing from the mountains across the sand and into the sea — a rare meeting of fresh and salt water, so visitors can swim in the sea and play in the stream at once. Being near the easternmost point of the mainland, it is an ideal place to camp overnight and wake to greet the first sunrise before climbing to the lighthouse. The beach is still quiet, keeping its natural feel with woods, rocks and clean water, suiting those who seek a tranquil, nature-close spot. Together with Dai Lanh Cape, Cả Pass and Vũng Rô Bay, Mon Beach is a lovely link in the southern exploration route of today's Đắk Lắk province, leaving an unforgettable impression of a fresh, pristine coast.",
  "presentation_long_ru": "У самого подножия маяка Дайлань на юге бывшего побережья Фуйена пляж Мон — один из красивейших и нетронутых пляжей района. Полумесяц тянется примерно на 400 м, с пологим мелким белым песком и скалистыми мысами по краям, обнимающими прозрачную синюю воду, что создаёт пейзаж одновременно уединённый и поэтичный. Его особенность — пресноводный ручей, стекающий с гор через песок в море: редкая встреча пресной и солёной воды, так что гости могут и купаться в море, и плескаться в ручье. Находясь у самой восточной точки материка, это идеальное место для ночёвки в палатке и встречи первого рассвета перед подъёмом к маяку. Пляж всё ещё тихий, сохраняет естественность с лесом, скалами и чистой водой и подходит тем, кто ищет спокойное, близкое к природе место. Вместе с мысом Дайлань, перевалом Ка и бухтой Вунгро пляж Мон — прекрасное звено южного маршрута нынешней провинции Даклак, оставляющее незабываемое впечатление о свежем, первозданном побережье.",
  "highlights_vi": [
    "Bãi cát trắng hình vòng cung ngay dưới hải đăng Mũi Điện",
    "Suối nước ngọt chảy vắt ngang bãi ra biển — rất hiếm gặp",
    "Cắm trại đón bình minh cực Đông, biển trong và hoang sơ"],
  "highlights_en": [
    "A crescent of white sand right below the Dai Lanh lighthouse",
    "A freshwater stream crossing the beach to the sea — very rare",
    "Camping to catch the easternmost sunrise; clear, pristine water"],
  "highlights_ru": [
    "Полумесяц белого песка прямо под маяком Дайлань",
    "Пресный ручей через пляж в море — большая редкость",
    "Кемпинг ради самого восточного рассвета; чистая, первозданная вода"],
  "practical": {
    "hours_vi": "Ban ngày; cắm trại qua đêm cần chuẩn bị và xin phép nếu có quy định.",
    "ticket_vi": "Vé/giữ xe tượng trưng (chung khu Mũi Điện); có thể thay đổi.",
    "duration_vi": "Khoảng 1,5–2 giờ (hoặc cắm trại qua đêm).",
    "best_time_vi": "Rạng sáng đón bình minh; mùa khô (tháng 1–8) biển đẹp.",
    "tips_vi": "Mang nước, đồ ăn, lều nếu cắm trại; giữ vệ sinh; cẩn thận sóng và đá."},
  "rating": {"value": 4.5, "count": 900, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách yêu bãi biển sạch, hoang sơ và suối ngọt độc đáo; cắm trại đón bình minh rất đáng. Một số nhắc dịch vụ ít, cần tự chuẩn bị.",
  "tags": ["beach", "camping", "sunrise", "outdoor", "seaside"],
  "sources": [
    {"title": "Wikipedia (VI) — Mũi Đại Lãnh (Bãi Môn)", "url": "https://vi.wikipedia.org/wiki/M%C5%A9i_%C4%90%E1%BA%A1i_L%C3%A3nh"}]}),

R("chua-thanh-luong", "Chùa Thanh Lương", "Пагода Тханьлыонг", "Thanh Luong Pagoda",
  ["church"], 13.265, 109.287,
  "Xã An Chấn (khu vực Tuy An cũ, Phú Yên), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Chùa Thanh Lương là ngôi chùa ven biển độc đáo ở An Chấn, nổi bật với kiến trúc trang trí bằng san hô, vỏ sò và những chiếc chum, bình gốm cổ. Chùa còn được biết đến với tượng Quán Thế Âm tương truyền trôi dạt từ biển vào. Không gian mộc mạc, gần gũi khiến nơi đây thành điểm tham quan tâm linh yêu thích.",
  "presentation_short_en": "Thanh Luong Pagoda is a distinctive seaside temple in An Chấn, notable for decoration made of coral, seashells and old ceramic jars. It is also known for a statue of Avalokiteśvara said to have floated ashore from the sea. Its simple, welcoming atmosphere makes it a favourite spiritual visit.",
  "presentation_short_ru": "Пагода Тханьлыонг — своеобразный приморский храм в общине Анчан, примечательный отделкой из кораллов, ракушек и старинных керамических кувшинов. Она также известна статуей Авалокитешвары, которая, по преданию, приплыла из моря. Простая, гостеприимная атмосфера делает её любимым местом духовного посещения.",
  "presentation_long_vi": "Nằm ở khu vực Tuy An, không xa bờ biển, chùa Thanh Lương gây ấn tượng ngay từ cái nhìn đầu tiên bởi lối kiến trúc và trang trí độc đáo hiếm nơi nào có. Thay vì chỉ dùng gạch ngói thông thường, nhà chùa tận dụng những vật liệu gắn với biển cả và đời sống dân dã: san hô, vỏ sò, vỏ ốc, cùng hàng trăm chiếc chum, vại, bình gốm cổ được sắp đặt khéo léo trên tường rào, cổng và các công trình, tạo nên vẻ mộc mạc mà lạ mắt, đậm chất làng quê ven biển. Chùa còn nổi tiếng với pho tượng Quán Thế Âm Bồ Tát mà theo lời kể của người dân địa phương đã trôi dạt từ biển vào và được rước về thờ, gắn với nhiều câu chuyện linh thiêng. Không gian chùa thanh tịnh, có hồ sen, tiểu cảnh và những góc sân rợp bóng cây, là nơi để du khách vãn cảnh, chiêm bái và tìm chút bình yên. Nhờ nét kiến trúc riêng có cùng vị trí gần các điểm tham quan như Bãi Xép, Gành Đá Đĩa, chùa Thanh Lương ngày càng được nhiều du khách ghé thăm khi khám phá vùng biển Phú Yên xưa, nay thuộc tỉnh Đắk Lắk, và trở thành một điểm dừng chân giàu bản sắc.",
  "presentation_long_en": "In the Tuy An area, not far from the shore, Thanh Luong Pagoda impresses at first sight with an architecture and decoration rarely seen elsewhere. Instead of ordinary brick and tile, the temple uses materials tied to the sea and rural life: coral, seashells, snail shells and hundreds of old jars, vats and ceramic pots, artfully arranged along the walls, gates and buildings to create a look that is simple yet striking, deeply rooted in the coastal countryside. The pagoda is also famous for a statue of Avalokiteśvara which, according to local accounts, floated ashore from the sea and was enshrined here, surrounded by many sacred stories. The grounds are serene, with a lotus pond, miniature landscapes and tree-shaded corners, a place for visitors to enjoy the scenery, pay respects and find a little peace. Thanks to its unique architecture and its position near sights such as Bai Xep and Gành Đá Đĩa, Thanh Luong Pagoda is increasingly visited by travellers exploring the former Phú Yên coast, now part of Đắk Lắk province, becoming a stop full of character.",
  "presentation_long_ru": "В районе Туйан, недалеко от берега, пагода Тханьлыонг поражает с первого взгляда архитектурой и отделкой, редко встречающимися где-либо ещё. Вместо обычных кирпича и черепицы храм использует материалы, связанные с морем и сельской жизнью: кораллы, раковины, панцири улиток и сотни старинных кувшинов, чанов и керамических горшков, искусно расставленных вдоль стен, ворот и построек, создавая вид простой, но яркий, глубоко укоренённый в приморской деревне. Пагода также славится статуей Авалокитешвары, которая, по рассказам местных жителей, приплыла из моря и была здесь установлена и окружена множеством священных преданий. Территория умиротворённая: пруд с лотосами, миниатюрные ландшафты и затенённые деревьями уголки — место, где гости любуются видами, поклоняются и находят немного покоя. Благодаря уникальной архитектуре и близости к таким местам, как Байсеп и Ганьдадя, пагода Тханьлыонг всё чаще посещается путешественниками, исследующими бывшее побережье Фуйена, ныне часть провинции Даклак, и становится остановкой, полной самобытности.",
  "highlights_vi": [
    "Trang trí độc đáo bằng san hô, vỏ sò và chum vại gốm cổ",
    "Tượng Quán Thế Âm tương truyền trôi dạt từ biển vào",
    "Gần Bãi Xép, Gành Đá Đĩa; không gian mộc mạc, thanh tịnh"],
  "highlights_en": [
    "Distinctive decoration of coral, seashells and old ceramic jars",
    "A statue of Avalokiteśvara said to have floated ashore",
    "Near Bai Xep and Gành Đá Đĩa; a simple, serene setting"],
  "highlights_ru": [
    "Своеобразная отделка из кораллов, ракушек и старинных кувшинов",
    "Статуя Авалокитешвары, по преданию приплывшая из моря",
    "Рядом с Байсеп и Ганьдадя; простая, умиротворённая обстановка"],
  "practical": {
    "hours_vi": "Mở cửa ban ngày cho khách chiêm bái (miễn phí).",
    "ticket_vi": "Miễn phí.",
    "duration_vi": "Khoảng 30–45 phút.",
    "best_time_vi": "Buổi sáng hoặc chiều mát; kết hợp Bãi Xép, Gành Đá Đĩa.",
    "tips_vi": "Ăn mặc lịch sự, giữ yên tĩnh; xin phép khi chụp ảnh khu thờ tự."},
  "rating": {"value": 4.4, "count": 700, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách thích kiến trúc lạ mắt bằng san hô, gốm cổ và không gian yên bình gần biển; hợp ghé cùng Bãi Xép. Một số thấy chùa nhỏ, nên đi kết hợp điểm khác.",
  "tags": ["temple", "architecture", "free", "culture", "seaside"],
  "sources": [
    {"title": "Cổng du lịch Phú Yên (Đắk Lắk) — Chùa Thanh Lương", "url": "https://phuyentourism.gov.vn/"}]}),

R("ganh-den", "Gành Đèn", "Мыс Ганьден", "Ganh Den",
  ["monument", "other"], 13.323, 109.305,
  "Xã An Ninh Đông (khu vực Tuy An cũ, Phú Yên), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Gành Đèn là ghềnh đá đẹp nằm gần Gành Đá Đĩa, nổi bật với những khối đá màu hồng cam và ngọn hải đăng nhỏ trắng đỏ trên mỏm. Nơi đây có làn nước biển trong xanh, sóng vỗ vào đá tung bọt trắng, khung cảnh hoang sơ và ít đông đúc. Đây là điểm chụp ảnh và ngắm biển yêu thích của giới trẻ.",
  "presentation_short_en": "Ganh Den is a beautiful rocky headland near Gành Đá Đĩa, notable for its pink-orange boulders and a small red-and-white lighthouse on the point. It has clear blue water, waves breaking into white foam, and a wild, uncrowded setting. It is a favourite spot for photos and sea views among young travellers.",
  "presentation_short_ru": "Ганьден — красивый скалистый мыс близ Ганьдадя, примечательный розово-оранжевыми валунами и небольшим красно-белым маяком на оконечности. Здесь прозрачная синяя вода, волны, разбивающиеся в белую пену, и дикая, немноголюдная обстановка. Это любимое место для фотографий и морских видов у молодых путешественников.",
  "presentation_long_vi": "Nằm ở khu vực Tuy An, chỉ cách thắng cảnh Gành Đá Đĩa nổi tiếng khoảng vài cây số, Gành Đèn là một ghềnh đá ven biển mang vẻ đẹp riêng biệt và còn khá hoang sơ. Điều khiến Gành Đèn cuốn hút là những khối đá lớn mang sắc hồng, cam pha vàng đặc trưng, xếp chồng lên nhau và nhô ra biển, tương phản rực rỡ với màu xanh của nước và trời. Trên mỏm đá cao có một ngọn hải đăng nhỏ sơn hai màu trắng – đỏ, vừa làm nhiệm vụ dẫn đường cho tàu thuyền, vừa trở thành điểm nhấn nổi bật cho khung cảnh, và cũng là nguồn gốc tên gọi 'Gành Đèn'. Sóng biển quanh năm vỗ vào chân gành tung bọt trắng xóa, tạo nên âm thanh và nhịp điệu cuốn hút. Vì đường ra gành phải men theo lối mòn qua rẫy, bãi đá nên nơi đây vẫn giữ được sự yên tĩnh, ít khách hơn so với Gành Đá Đĩa, rất hợp cho những ai muốn tìm góc biển riêng tư để chụp ảnh, ngắm bình minh hay cắm trại nhẹ nhàng. Kết hợp tham quan cùng Gành Đá Đĩa, đầm Ô Loan và nhà thờ Mằng Lăng gần đó, Gành Đèn góp thêm một điểm đến giàu chất thơ trong hành trình khám phá bờ biển phía bắc tỉnh Đắk Lắk ngày nay.",
  "presentation_long_en": "In the Tuy An area, just a few kilometres from the famous Gành Đá Đĩa, Ganh Den is a coastal rock formation with its own distinctive beauty and a still-wild feel. Its charm lies in the large boulders in characteristic pink, orange and yellow tones, stacked and jutting into the sea in vivid contrast with the blue of water and sky. On a high point stands a small red-and-white lighthouse that both guides ships and forms a striking accent in the scene — the source of the name 'Ganh Den' (Lamp Rock). Waves break against the base of the rocks year-round in white foam, creating an alluring sound and rhythm. Because reaching it means following a path across fields and rocks, the spot stays quiet and less crowded than Gành Đá Đĩa, ideal for those seeking a private stretch of coast to take photos, watch the sunrise or camp lightly. Combined with nearby Gành Đá Đĩa, O Loan Lagoon and Mang Lang Church, Ganh Den adds another poetic stop to the exploration of the northern coast of today's Đắk Lắk province.",
  "presentation_long_ru": "В районе Туйан, всего в нескольких километрах от знаменитого Ганьдадя, Ганьден — прибрежное скальное образование со своей особой красотой и всё ещё диким характером. Его очарование — в крупных валунах характерных розовых, оранжевых и жёлтых оттенков, нагромождённых и выступающих в море в ярком контрасте с синевой воды и неба. На высокой точке стоит небольшой красно-белый маяк, который и указывает путь судам, и служит выразительным акцентом пейзажа — отсюда название «Ганьден» («Скала-фонарь»). Волны круглый год разбиваются о подножие скал белой пеной, создавая притягательный звук и ритм. Поскольку добраться сюда можно лишь по тропе через поля и камни, место остаётся тихим и менее людным, чем Ганьдадя, и идеально для тех, кто ищет уединённый участок побережья, чтобы пофотографировать, встретить рассвет или устроить лёгкий кемпинг. Вместе с близкими Ганьдадя, лагуной Олоан и церковью Манглanг Ганьден добавляет ещё одну поэтичную остановку в исследовании северного побережья нынешней провинции Даклак.",
  "highlights_vi": [
    "Khối đá hồng cam nhô ra biển, tương phản với nước xanh",
    "Hải đăng nhỏ trắng – đỏ trên mỏm, nguồn gốc tên 'Gành Đèn'",
    "Yên tĩnh, ít khách hơn Gành Đá Đĩa; hợp chụp ảnh, ngắm bình minh"],
  "highlights_en": [
    "Pink-orange boulders jutting into the sea against blue water",
    "A small red-and-white lighthouse on the point, the source of the name",
    "Quieter and less crowded than Gành Đá Đĩa; good for photos and sunrise"],
  "highlights_ru": [
    "Розово-оранжевые валуны, выступающие в море на фоне синей воды",
    "Небольшой красно-белый маяк на мысе — источник названия",
    "Тише и менее людно, чем Ганьдадя; хорош для фото и рассвета"],
  "practical": {
    "hours_vi": "Ban ngày; đường ra gành đi bộ qua lối mòn, nên đi giày bám tốt.",
    "ticket_vi": "Thường miễn phí; có thể có phí giữ xe tượng trưng.",
    "duration_vi": "Khoảng 1–1,5 giờ.",
    "best_time_vi": "Sáng sớm đón bình minh; mùa khô (tháng 1–8) biển đẹp.",
    "tips_vi": "Cẩn thận đá trơn và sóng lớn; kết hợp Gành Đá Đĩa và Mằng Lăng gần đó."},
  "rating": {"value": 4.4, "count": 850, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách khen gành đá màu đẹp, biển trong và vắng người hơn Gành Đá Đĩa; góc ảnh ấn tượng. Lưu ý đường ra hơi khó và đá trơn.",
  "tags": ["seaside", "lighthouse", "photo", "viewpoint", "outdoor"],
  "sources": [
    {"title": "Cổng du lịch Phú Yên (Đắk Lắk) — Gành Đèn", "url": "https://phuyentourism.gov.vn/"}]}),

R("nui-chop-chai", "Núi Chóp Chài", "Гора Тьётьай", "Chop Chai Mountain",
  ["park_garden", "other"], 13.125, 109.285,
  "Khu vực Tuy Hòa (Phú Yên cũ), tỉnh Đắk Lắk", {
  "presentation_short_vi": "Núi Chóp Chài là ngọn núi đứng đơn độc cao khoảng 391 m ở ngoại ô Tuy Hòa, có hình dáng cân đối như kim tự tháp. Trên núi có các ngôi chùa cổ và đường lên đỉnh để ngắm toàn cảnh thành phố, đồng lúa và biển. Đây là điểm dã ngoại, hành hương và ngắm cảnh quen thuộc của người dân.",
  "presentation_short_en": "Chop Chai Mountain is a solitary peak of about 391 m on the edge of Tuy Hòa, with a balanced, pyramid-like shape. It holds old pagodas and a path to the summit for panoramic views of the city, rice fields and sea. It is a familiar spot for picnics, pilgrimage and sightseeing among locals.",
  "presentation_short_ru": "Гора Тьётьай — одиночная вершина высотой около 391 м на окраине Туйхоа, с уравновешенной, похожей на пирамиду формой. На ней стоят старые пагоды и есть тропа к вершине с панорамными видами на город, рисовые поля и море. Это привычное место для пикников, паломничества и осмотра окрестностей у местных жителей.",
  "presentation_long_vi": "Nằm ở phía bắc thành phố Tuy Hòa, núi Chóp Chài cao khoảng 391 m, nổi bật giữa vùng đồng bằng bằng phẳng nhờ dáng núi cân đối, nhọn dần lên đỉnh như một kim tự tháp tự nhiên. Từ lâu, đây đã là ngọn núi thiêng và điểm dã ngoại quen thuộc của người dân địa phương. Trên sườn và quanh chân núi có nhiều ngôi chùa, tịnh xá như chùa Khánh Sơn, chùa Bảo Lâm, Minh Sơn tự... tạo nên không gian tâm linh yên tĩnh giữa rừng cây. Du khách có thể theo con đường mòn hoặc đường bê tông men theo sườn để lên gần đỉnh, vừa đi vừa nghỉ tại các điểm chùa, hít thở không khí trong lành và nghe tiếng chim rừng. Phần thưởng khi lên cao là tầm nhìn khoáng đạt bao trọn thành phố Tuy Hòa, dòng sông Đà Rằng, những cánh đồng lúa xanh mướt trải dài và đường bờ biển cong cong phía xa. Vào buổi sáng sớm hay chiều muộn, khung cảnh càng thêm huyền ảo với sương giăng và ánh nắng dịu. Gần trung tâm, dễ tiếp cận, kết hợp được cả hành hương lẫn ngắm cảnh, núi Chóp Chài là một điểm đến nhẹ nhàng, thú vị cho du khách khi ghé vùng biển Tuy Hòa của tỉnh Đắk Lắk ngày nay.",
  "presentation_long_en": "North of Tuy Hòa city, Chop Chai Mountain rises about 391 m, standing out on the flat plain thanks to its balanced form tapering to a point like a natural pyramid. It has long been a sacred hill and a familiar picnic spot for locals. On its slopes and around its base are several pagodas and monasteries — Khánh Sơn, Bảo Lâm, Minh Sơn and others — creating a quiet spiritual space amid the trees. Visitors can follow a trail or a concrete path along the slope toward the summit, pausing at the temples, breathing the fresh air and listening to forest birds. The reward at the top is a sweeping view taking in all of Tuy Hòa, the Đà Rằng River, the long green rice fields and the curving coastline in the distance. In the early morning or late afternoon the scene grows dreamlike with drifting mist and soft light. Close to the centre, easy to reach and combining pilgrimage with sightseeing, Chop Chai Mountain is a gentle, enjoyable destination for travellers visiting the Tuy Hòa coast of today's Đắk Lắk province.",
  "presentation_long_ru": "К северу от города Туйхоа гора Тьётьай поднимается примерно на 391 м, выделяясь на плоской равнине уравновешенной формой, сужающейся к вершине, словно природная пирамида. Издавна это священный холм и привычное место пикников у местных жителей. На её склонах и у подножия — несколько пагод и монастырей: Кханьшон, Баолам, Миньшон и другие, создающие тихое духовное пространство среди деревьев. Гости могут идти по тропе или бетонной дорожке вдоль склона к вершине, останавливаясь у храмов, вдыхая свежий воздух и слушая лесных птиц. Наградой на вершине становится широкий вид, охватывающий весь Туйхоа, реку Дяранг, длинные зелёные рисовые поля и изгибающуюся вдали береговую линию. Ранним утром или под вечер пейзаж становится сказочным от плывущего тумана и мягкого света. Близкая к центру, легко доступная и сочетающая паломничество с осмотром окрестностей, гора Тьётьай — приятное, ненавязчивое место для путешественников на побережье Туйхоа нынешней провинции Даклак.",
  "highlights_vi": [
    "Núi đơn độc ~391 m dáng kim tự tháp ngay cạnh Tuy Hòa",
    "Nhiều chùa cổ trên núi: Khánh Sơn, Bảo Lâm, Minh Sơn tự...",
    "Đỉnh nhìn toàn cảnh thành phố, sông Đà Rằng, đồng lúa và biển"],
  "highlights_en": [
    "A solitary ~391 m pyramid-shaped mountain right by Tuy Hòa",
    "Several old pagodas on the hill: Khánh Sơn, Bảo Lâm, Minh Sơn and more",
    "The summit overlooks the city, the Đà Rằng River, rice fields and sea"],
  "highlights_ru": [
    "Одиночная гора ~391 м пирамидальной формы у Туйхоа",
    "Несколько старых пагод на холме: Кханьшон, Баолам, Миньшон и другие",
    "С вершины вид на город, реку Дяранг, рисовые поля и море"],
  "practical": {
    "hours_vi": "Ban ngày; leo bộ hoặc chạy xe một đoạn rồi đi bộ lên chùa.",
    "ticket_vi": "Miễn phí (viếng chùa).",
    "duration_vi": "Khoảng 2–3 giờ cả lên xuống.",
    "best_time_vi": "Sáng sớm hoặc chiều mát; mùa khô trời quang, tầm nhìn đẹp.",
    "tips_vi": "Mang nước, giày phù hợp; ăn mặc lịch sự khi vào chùa; tránh nắng trưa."},
  "rating": {"value": 4.3, "count": 650, "source": "Google", "as_of": "2026-07"},
  "review_summary_vi": "Khách thích không gian chùa yên tĩnh và tầm nhìn thành phố – đồng lúa từ trên núi; hợp dã ngoại nhẹ. Một số nói đường lên có đoạn dốc, nên đi sớm.",
  "tags": ["mountain", "temple", "viewpoint", "free", "outdoor"],
  "sources": [
    {"title": "Wikipedia (VI) — Núi Chóp Chài", "url": "https://vi.wikipedia.org/wiki/N%C3%BAi_Ch%C3%B3p_Ch%C3%A0i"}]}),
]

# ---INSERT-MORE-BLOCKS-HERE---

d += [p for p in new if p["slug"] not in have]
json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("gio co", len(d), "| them:", len([p for p in new if p["slug"] not in have]))
