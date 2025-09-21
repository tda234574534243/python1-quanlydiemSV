import json
import os

FILE = "sinhvien.json"
FILE_MONHOC = "monhoc.txt"

# ================== HÀM XỬ LÝ ==================
def tinh_diem_mon(d1, d2):
    return round(d1 * 0.4 + d2 * 0.6, 1)

def tinh_gpa(danh_sach_mon):
    if not danh_sach_mon:
        return 0.0
    tong = sum(mon["diem_mon"] for mon in danh_sach_mon)
    return round(tong / len(danh_sach_mon), 2)

def load_data():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("Lỗi khi đọc file:", e)
        return []

def save_data(data):
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print("Lỗi khi ghi file:", e)

def load_monhoc():
    if not os.path.exists(FILE_MONHOC):
        return []
    try:
        with open(FILE_MONHOC, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print("Lỗi khi đọc monhoc.txt:", e)
        return []

# ================== CRUD ==================
def them_sv(data):
    mssv = input("Nhập MSSV: ")

    # Kiểm tra trùng MSSV
    for sv in data:
        if sv["mssv"] == mssv:
            print("❌ MSSV đã tồn tại, không thể thêm!")
            return

    ho_ten = input("Nhập họ tên: ")
    mon_hoc = []

    ds_mon = load_monhoc()
    if not ds_mon:
        print("⚠️ Không có file monhoc.txt hoặc rỗng, không thể thêm môn học!")
    else:
        while True:
            print("\nDanh sách môn học có sẵn:")
            for i, ten in enumerate(ds_mon, 1):
                print(f"{i}. {ten}")
            chon = input("Chọn số để thêm môn (Enter để dừng): ")
            if chon == "":
                break
            if chon.isdigit():
                idx = int(chon) - 1
                if 0 <= idx < len(ds_mon):
                    try:
                        d1 = round(float(input("Điểm 40%: ")), 1)
                        d2 = round(float(input("Điểm 60%: ")), 1)
                        mon = {
                            "ten": ds_mon[idx],
                            "diem1": d1,
                            "diem2": d2,
                            "diem_mon": tinh_diem_mon(d1, d2)
                        }
                        mon_hoc.append(mon)
                        print(f"✅ Đã thêm môn {ds_mon[idx]}")
                    except:
                        print("❌ Nhập sai điểm, bỏ qua môn này!")
                else:
                    print("❌ Số không hợp lệ!")
            else:
                print("❌ Nhập sai, phải là số!")

    sv = {
        "mssv": mssv,
        "ho_ten": ho_ten,
        "mon_hoc": mon_hoc,
        "gpa": tinh_gpa(mon_hoc)
    }
    data.append(sv)
    save_data(data)
    print("🎉 Đã thêm sinh viên!")

def xem_sv(data):
    if not data:
        print("Danh sách rỗng.")
        return
    for sv in data:
        print(f"{sv['mssv']} - {sv['ho_ten']} - GPA: {sv['gpa']:.2f}")
        for mon in sv["mon_hoc"]:
            print(f"   {mon['ten']}: {mon['diem_mon']:.1f} (d1={mon['diem1']:.1f}, d2={mon['diem2']:.1f})")

def sua_sv(data):
    mssv = input("Nhập MSSV cần sửa: ")
    for sv in data:
        if sv["mssv"] == mssv:
            print("Tìm thấy sinh viên:", sv["ho_ten"])
            sv["ho_ten"] = input("Họ tên mới (Enter để giữ nguyên): ") or sv["ho_ten"]

            # Sửa điểm từng môn
            for mon in sv["mon_hoc"]:
                print(f"Sửa môn {mon['ten']}:")
                try:
                    d1 = input(f"  Điểm 40% ({mon['diem1']:.1f}): ")
                    d2 = input(f"  Điểm 60% ({mon['diem2']:.1f}): ")
                    if d1: mon["diem1"] = round(float(d1), 1)
                    if d2: mon["diem2"] = round(float(d2), 1)
                    mon["diem_mon"] = tinh_diem_mon(mon["diem1"], mon["diem2"])
                except:
                    print("Bỏ qua do nhập sai!")

            # === Thêm môn mới từ wordlist ===
            ds_mon = load_monhoc()
            if ds_mon:
                print("\nDanh sách môn học có sẵn:")
                for i, ten in enumerate(ds_mon, 1):
                    print(f"{i}. {ten}")
                chon = input("Chọn số để thêm môn mới (Enter để bỏ qua): ")
                if chon.isdigit():
                    idx = int(chon) - 1
                    if 0 <= idx < len(ds_mon):
                        try:
                            d1 = round(float(input("Điểm 40%: ")), 1)
                            d2 = round(float(input("Điểm 60%: ")), 1)
                            mon = {
                                "ten": ds_mon[idx],
                                "diem1": d1,
                                "diem2": d2,
                                "diem_mon": tinh_diem_mon(d1, d2)
                            }
                            sv["mon_hoc"].append(mon)
                            print(f"Đã thêm môn {ds_mon[idx]}")
                        except:
                            print("Nhập sai điểm, không thêm môn!")
            
            sv["gpa"] = tinh_gpa(sv["mon_hoc"])
            save_data(data)
            print("Đã sửa sinh viên!")
            return
    print("Không tìm thấy MSSV!")

def xoa_sv(data):
    mssv = input("Nhập MSSV cần xóa: ")
    for sv in data:
        if sv["mssv"] == mssv:
            data.remove(sv)
            save_data(data)
            print("Đã xóa sinh viên!")
            return
    print("Không tìm thấy MSSV!")

# ================== MENU ==================
def menu():
    data = load_data()
    while True:
        print("\n===== QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Xem danh sách")
        print("3. Sửa sinh viên")
        print("4. Xóa sinh viên")
        print("5. Thoát")

        choice = input("Chọn: ")
        if choice == "1":
            them_sv(data)
        elif choice == "2":
            xem_sv(data)
        elif choice == "3":
            sua_sv(data)
        elif choice == "4":
            xoa_sv(data)
        elif choice == "5":
            print("Bye")
            break
        else:
            print("Lựa chọn không hợp lệ!")

# ================== RUN ==================
if __name__ == "__main__":
    menu()
