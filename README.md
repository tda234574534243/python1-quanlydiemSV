# README — Chương trình Quản lý Sinh viên (Console)

**Ngôn ngữ:** Python 

## Mô tả

Đây là một chương trình console nhỏ để quản lý danh sách sinh viên, mỗi sinh viên có mã số (MSSV), họ tên, danh sách môn học và điểm từng môn. Chương trình hỗ trợ thêm, xem, sửa, xóa sinh viên và lưu dữ liệu vào file JSON (`sinhvien.json`). Danh sách tên môn khả dụng được đọc từ file `monhoc.txt`.

## Tệp trong dự án

* `sinhvien.json` — file dữ liệu chính chứa danh sách sinh viên (JSON). Nếu chưa tồn tại, chương trình khởi tạo danh sách rỗng.
* `monhoc.txt` — file văn bản chứa danh sách tên môn (mỗi môn trên 1 dòng). Dùng khi thêm/sửa sinh viên để chọn môn.
* `quanly.py` (hoặc tên file script chứa code) — chương trình chính (console) mà bạn đã cung cấp.

## Yêu cầu

* Python 3.6+ (để đảm bảo `json` và f-string hoạt động bình thường).

## Cách chạy

1. Đặt `sinhvien.json`, `monhoc.txt` và file script Python vào cùng một thư mục.
2. Mở terminal/cmd trong thư mục đó.
3. Chạy: `python quanly.py` (hoặc `python3 quanly.py` tuỳ hệ thống).
4. Giao diện console sẽ hiện menu với các lựa chọn:

   1. Thêm sinh viên
   2. Xem danh sách
   3. Sửa sinh viên
   4. Xóa sinh viên
   5. Thoát

## Định dạng dữ liệu

Mỗi sinh viên trong `sinhvien.json` có dạng JSON object:

```json
{
  "mssv": "SV001",
  "ho_ten": "Nguyen Van A",
  "mon_hoc": [
    {
      "ten": "Cơ sở dữ liệu",
      "diem1": 8.0,
      "diem2": 7.5,
      "diem_mon": 7.7
    }
  ],
  "gpa": 7.25
}
```

* `diem1`: điểm 40% (float, 1 chữ số thập phân)
* `diem2`: điểm 60% (float, 1 chữ số thập phân)
* `diem_mon`: điểm tổng kết môn, tính theo công thức trong chương trình
* `gpa`: điểm trung bình (tính là trung bình các `diem_mon` của sinh viên)

## Công thức tính

* `diem_mon = round(diem1 * 0.4 + diem2 * 0.6, 1)` — làm tròn tới 1 chữ số thập phân.
* `gpa = round(sum(diem_mon) / so_mon, 2)` — làm tròn tới 2 chữ số thập phân.

## Tính năng chính (mô tả các hàm)

* `tinh_diem_mon(d1, d2)` — tính điểm môn.
* `tinh_gpa(danh_sach_mon)` — tính gpa từ danh sách môn.
* `load_data()` / `save_data(data)` — đọc/ghi `sinhvien.json`.
* `load_monhoc()` — đọc danh sách môn từ `monhoc.txt`.
* `them_sv(data)` — thêm sinh viên mới (kiểm tra trùng MSSV, chọn môn từ `monhoc.txt`, nhập điểm).
* `xem_sv(data)` — in danh sách sinh viên và điểm.
* `sua_sv(data)` — sửa thông tin và điểm sinh viên; cho phép thêm môn mới từ `monhoc.txt`.
* `xoa_sv(data)` — xóa sinh viên theo MSSV.
* `menu()` — vòng lặp menu chính.

## Lưu ý & gợi ý cải tiến

* Hiện tại chương trình lưu ngay sau mỗi thao tác (thêm/sửa/xóa). Nếu muốn xử lý theo batch, có thể hoãn `save_data` tới khi thoát.
* Không có xác thực mạnh với điểm (ngoại trừ catch ngoại lệ khi nhập). Có thể thêm kiểm tra phạm vi điểm (0.0 - 10.0).
* Với danh sách môn nhiều, giao diện console có thể kém trực quan — cân nhắc chuyển sang giao diện đơn giản hơn hoặc dùng CLI argument.
* Hiện MSSV so sánh bằng chuỗi; nếu muốn chuẩn hoá, có thể trim/upper/lower trước khi so sánh.
* Khi `monhoc.txt` không tồn tại, chức năng thêm môn sẽ bị vô hiệu — nên thêm mặc định hoặc hiển thị hướng dẫn tạo file.

## Cách chạy
#command: 
* window
'python<version> quanly.py'
* linux
'chmod +x quanly.py
./quanly.py'

* Thêm sinh viên mới: chạy chương trình → chọn 1 → nhập MSSV, họ tên → chọn môn từ danh sách `monhoc.txt` → nhập điểm 40% và 60% → chương trình tự tính `diem_mon` và `gpa` và lưu vào `sinhvien.json`.
