# 🤖 Tác vụ tự động hằng giờ — Hướng dẫn vận hành

Tài liệu này mô tả **chính xác** những gì tác vụ tự động làm mỗi khi chạy. Mỗi lần chạy là một phiên Claude mới, làm việc trực tiếp trong thư mục dự án trên máy bạn.

> ⚠️ **Điều kiện:** Vì dữ liệu lưu trong thư mục máy bạn, hãy **mở sẵn ứng dụng Claude trên máy tính** vào thời điểm tác vụ chạy. Nếu máy tắt/ứng dụng đóng, lần chạy đó sẽ bỏ qua và thử lại vào giờ kế tiếp.

---

## Mỗi lần chạy làm gì (một “lô”)

1. Đọc `_source/progress.json` (danh sách vùng đã xong) và `_source/regions_queue.json` (thứ tự vùng).
2. Chọn **vùng kế tiếp** chưa có trong `done`.
3. Xác định các địa điểm tiêu biểu của vùng đó (ưu tiên đối chiếu mục lục & nội dung sách trong `_source/book_raw.txt`, kết hợp hiểu biết + tra web). Xử lý tối đa `batch_size` địa điểm (mặc định 12).
4. Với **mỗi địa điểm**, tạo một bản ghi theo `data/schema.json`:
   - Tên VI/RU/EN, phân loại (categories).
   - **Toạ độ chính xác** (kiểm tra bằng tra cứu; nếu không chắc, ghi `status: "stub"` và để đánh giá null).
   - Link Yandex + Google Maps (sinh từ toạ độ).
   - **Thuyết trình ngắn** (2–3 câu) + **thuyết trình chi tiết** (~180–260 từ), tiếng Việt **nguyên bản**, hấp dẫn, chính xác.
   - Đánh giá sao + số lượng + nguồn + tóm tắt bình luận (tra web; để null nếu không có).
   - Giờ mở cửa/giá vé/thời lượng/thời điểm đẹp/mẹo; ảnh Wikimedia (Special:FilePath) nếu chắc chắn.
5. Ghi/append vào `data/regions/<slug>.json` (là một **mảng** bản ghi).
6. Cập nhật `_source/progress.json` (thêm vùng vào `done` khi hoàn tất, hoặc lưu `in_progress` nếu mới xong một phần).
7. Chạy `python3 tools/build.py` để tái sinh `bundle.js`, `index.json` và `exports/*`.
8. (Tuỳ chọn) Ghi vài dòng nhật ký vào `_source/run_log.txt`.

Kết quả: lần mở web tiếp theo, vùng mới tự xuất hiện trên Danh sách và Bản đồ GIS.

---

## Quy tắc chất lượng (bắt buộc)

- **Không sao chép nguyên văn sách.** Sách chỉ dùng làm danh mục địa điểm. Viết nội dung tiếng Việt mới từ dữ kiện.
- **Chính xác hơn số lượng.** Thà ít địa điểm nhưng đúng, còn hơn nhiều mà sai toạ độ/đánh giá.
- **Trung thực với dữ liệu web:** nếu không tìm được đánh giá → `rating.value = null`. Không bịa số sao, số lượt, hay URL ảnh.
- **Đánh dấu trạng thái:** dữ liệu tự sinh để `status: "enriched"`. Khi bạn (người) đã kiểm tra, đổi thành `"verified"`.
- **Toạ độ:** dùng thập phân 6 chữ số, đúng vị trí thật. Kiểm tra khớp tên địa điểm.
- **Nhất quán categories** theo bảng trong `README.md`.

---

## Chạy thủ công một lô (không cần chờ lịch)

Bạn có thể yêu cầu Claude: *“Xử lý vùng tiếp theo cho dự án du lịch Nga trong thư mục DU-LICH theo AUTOMATION_GUIDE.md”*. Claude sẽ làm đúng các bước trên cho một lô.

---

## Điều chỉnh / tạm dừng

- **Đổi số địa điểm mỗi lô:** sửa `batch_size` trong `_source/progress.json`.
- **Bỏ qua/định thứ tự vùng:** sửa `_source/regions_queue.json`.
- **Tạm dừng hoặc xoá lịch chạy:** nói với Claude “tạm dừng/xoá tác vụ tự động du lịch Nga”, hoặc quản lý trong mục Tác vụ đã lên lịch.
- **Làm lại một vùng:** xoá slug đó khỏi `done` trong `progress.json` và xoá file `data/regions/<slug>.json` tương ứng.

---

## Cấu trúc bản ghi
Xem `data/schema.json` (mô tả) và `data/regions/saint-petersburg.json` (18 ví dụ thực tế mẫu). Khuôn điền nhanh: `tools/region_template.json`.
