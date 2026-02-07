import datetime

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
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    van = (day_of_year % 9) or 9
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Tạo file báo cáo kết quả
    with open(f"KET_QUA_VAN_{van}.csv", "w", encoding="utf-8-sig") as f:
        f.write("Ngày, Vận, Ngành hàng ưu tiên\n")
        f.write(f"{today}, Vận {van}, {DATA[van]}")

if __name__ == "__main__":
    logic_cuu_van()
