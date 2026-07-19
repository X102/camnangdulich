# 🇷🇺 Cẩm nang Du lịch Nga — Cơ sở dữ liệu tiếng Việt (module, mở rộng dần)

Bộ công cụ biến cuốn sách *“1000 địa điểm nước Nga nên đến”* thành một **cơ sở dữ liệu du lịch tiếng Việt sống động**: mỗi địa điểm có thuyết trình ngắn & chi tiết, toạ độ + link bản đồ, đánh giá/bình luận từ web, đọc thành tiếng (TTS), bản đồ GIS và trình lập kế hoạch tour.

> **Bản mẫu hiện tại: Saint Petersburg (18 địa điểm tiêu biểu).** Hệ thống được thiết kế để mở rộng dần ra toàn nước Nga — mỗi lần thêm dữ liệu, giao diện tự cập nhật, **không phải sửa code**.

---

## 🚀 Mở sản phẩm

Chỉ cần mở các file HTML bằng trình duyệt (nhấp đúp):

| File | Công dụng |
|------|-----------|
| **index.html** | Trang chủ, thống kê, giới thiệu |
| **list.html** | Danh sách địa điểm dễ đọc, tìm kiếm/lọc, **nghe đọc** thuyết trình |
| **gis.html** | Bản đồ GIS + **lập kế hoạch tour** (chọn điểm → tối ưu lộ trình → chia ngày → xuất lịch trình) |

> Cần kết nối Internet để hiển thị ảnh nền bản đồ (map tiles) và ảnh địa điểm. Mọi tính năng còn lại (danh sách, đọc thành tiếng, lọc, lập tour) chạy được cả khi ngoại tuyến vì thư viện đã được nhúng sẵn.

---

## 🧩 Nguyên tắc thiết kế: “thêm dữ liệu, không sửa code”

```
russia-tourism/
├── index.html · list.html · gis.html      ← giao diện (không cần sửa khi thêm dữ liệu)
├── assets/
│   ├── app.css · common.js                ← lõi giao diện + bộ đọc TTS + tiện ích
│   └── vendor/                            ← thư viện bản đồ Leaflet (nhúng sẵn, chạy offline)
├── data/
│   ├── regions/<slug>.json               ← ★ NGUỒN DỮ LIỆU (mỗi vùng = 1 file)
│   ├── schema.json                       ← mô tả cấu trúc bản ghi
│   ├── index.json  · bundle.js           ← TỰ SINH bởi build.py (đừng sửa tay)
├── exports/                              ← TỰ SINH: places.csv/.xlsx/.geojson/.json
├── tools/
│   ├── build.py                          ← biên dịch dữ liệu → bundle.js + exports
│   ├── seed_saint_petersburg.py          ← ví dụ tạo dữ liệu vùng SPb
│   ├── region_template.json              ← khuôn mẫu 1 bản ghi để điền
│   └── seed_meta.py                      ← sinh hàng đợi vùng + tiến độ
├── _source/                             ← sách trích xuất, hàng đợi vùng, tiến độ tự động
├── AUTOMATION_GUIDE.md                  ← tác vụ tự động hằng giờ hoạt động thế nào
└── README.md
```

**Luồng dữ liệu:** `data/regions/*.json`  →  `python3 tools/build.py`  →  `bundle.js` + `exports/*`  →  giao diện đọc `bundle.js`.

---

## ➕ Cách thêm dữ liệu

### Thêm địa điểm vào một vùng đã có
1. Mở `data/regions/<vùng>.json`, thêm một bản ghi mới (chép từ `tools/region_template.json`, điền nội dung).
2. Chạy: `python3 tools/build.py`
3. Mở lại trang — xong. Không đụng tới HTML/JS.

### Thêm một vùng mới (ví dụ Moskva)
1. Tạo file `data/regions/moscow.json` = một **mảng** bản ghi (theo `schema.json`).
2. Chạy `python3 tools/build.py`. Bộ lọc “vùng” trên giao diện tự xuất hiện.

### Bảng loại hình (categories)
`museum` · `palace` · `church` · `fortress` · `monument` · `park_garden` · `bridge` · `square_street` · `theatre` · `other`
(Muốn thêm loại mới: khai báo nhãn + màu trong `assets/common.js` → `CATEGORIES`.)

---

## 📤 Các định dạng dữ liệu xuất ra (trong `exports/`)
- **places.csv** — bảng phẳng (Excel/Sheets mở trực tiếp, đã có BOM UTF-8).
- **places.xlsx** — bảng Excel định dạng sẵn để lập kế hoạch.
- **places.geojson** — nạp vào QGIS/ArcGIS/Mapbox… như một lớp bản đồ.
- **places.json** — toàn bộ dữ liệu cho lập trình/API sau này.

---

## 🔊 Đọc thành tiếng (TTS)
Dùng bộ đọc sẵn của trình duyệt (không cần cài thêm). Nếu máy chưa có **giọng tiếng Việt**, tính năng vẫn chạy nhưng nghe máy móc hơn — cài giọng vi-VN để hay nhất (Windows: *Cài đặt → Thời gian & Ngôn ngữ → Giọng nói → Thêm giọng*). Văn bản dài được tự chia câu nên không bị ngắt giữa chừng.

---

## 🤖 Tự động mở rộng
Xem **AUTOMATION_GUIDE.md**. Tác vụ tự động hằng giờ sẽ lần lượt xử lý các vùng trong `_source/regions_queue.json`, ghi vào `data/regions/`, rồi tự chạy `build.py`.

---

## 📇 Liên hệ
**Phạm Đăng Hiển** · ✉️ lopmaybay@gmail.com · 🌐 [fb.com/lopmaybay](https://fb.com/lopmaybay)

> *Về bản quyền:* Nội dung tiếng Việt là bản gốc, biên soạn mới từ dữ kiện thực tế và dữ liệu web; cuốn sách nguồn chỉ dùng làm **danh mục định hướng** các địa điểm, không sao chép nguyên văn.
