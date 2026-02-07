import datetime
import os

# Dữ liệu chuẩn Cửu Vận bạn đã cung cấp
DATA = {
    1: "Giáo dục, vận tải thủy, bưu chính, sách vở",
    2: "Nông nghiệp, bất động sản, y tế cổ truyền",
    3: "Gỗ, giấy, dệt may, truyền thông",
    4: "Xuất bản, giáo dục, nghệ thuật, thiết kế",
    5: "Xây dựng, khoáng sản, quân sự",
    6: "Cơ khí, hàng không, tài chính, trang sức",
    7: "Giải trí, âm nhạc, phim ảnh, viễn thông",
    8: "Địa ốc, vật liệu xây dựng, logistics",
    9: "AI, công nghệ số, làm đẹp, y tế, tâm linh"
}

def logic_cuu_van():
    # Tính toán vận
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    van = (day_of_year % 9) or 9
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 1. Đảm bảo file kết quả chui vào đúng chỗ, không nằm đè lên friends.csv
    target_dir = 'processed_data'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 2. Tạo tên file có ngày tháng để không bị trùng lặp
    file_name = f"KET_QUA_VAN_{today}.csv"
    file_path = os.path.join(target_dir, file_name)
    
    # 3. Ghi kết quả
    try:
        with open(file_path, "w", encoding="utf-8-sig") as f:
            f.write("Ngày, Vận, Ngành hàng ưu tiên\n")
            f.write(f"{today}, Vận {van}, {DATA[van]}")
        print(f"Robot Cử Vạn: Đã xem quẻ xong! Kết quả cất tại {file_path}")
    except Exception as e:
        print(f"Robot Cử Vạn: Đại ca ơi, không ghi được sổ rồi: {e}")

if __name__ == "__main__":
    logic_cuu_van()
