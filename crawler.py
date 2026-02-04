import pandas as pd
import os

# 1. Đọc danh sách bạn bè
try:
    # Đọc file friends.csv (chứa 33 người)
    df = pd.read_csv('friends.csv', encoding='utf-8')
except Exception as e:
    print("❌ Lỗi: Không tìm thấy file friends.csv hoặc file bị lỗi định dạng!")
    exit()

def robot_shopping_smart():
    # --- BƯỚC 1: DỌN DẸP KỆ HÀNG CŨ ---
    for f in ['database.csv', 'database10.csv', 'database6.csv']:
        if os.path.exists(f):
            os.remove(f)
            print(f"🧹 Đã dọn dẹp kệ hàng cũ: {f}")

    print("🚀 Robot bắt đầu phân loại và điền link cho 33 người...")

    # --- BƯỚC 2: ĐIỀN LINK TỰ ĐỘNG & PHÂN LOẠI ---
    updated_rows = []

    for _, row in df.iterrows():
        age = int(row['age'])
        gender = row['gender']
        
        # Logic tự chọn link nếu ô product_link đang trống
        if pd.isnull(row['product_link']) or str(row['product_link']).strip() == "":
            if age < 15:
                row['product_link'] = "https://s.shopee.vn/5fj08y0YQn" # Lâu đài Elsa
                row['img_url'] = "https://down-cvs-vn.img.susercontent.com/sg-11134201-7rfh8-m9y3lu0rp6zt11.webp"
            elif 15 <= age <= 40:
                row['product_link'] = "https://s.shopee.vn/3B1fCEuDYo" # Máy ảnh Instax
                row['img_url'] = "https://down-zl-vn.img.susercontent.com/vn-11134207-820l4-mj5e3i67rx8lbe.webp"
            else:
                row['product_link'] = "https://s.shopee.vn/InstaxMiniEvo" # Quà cao cấp
                row['img_url'] = "https://down-cvs-vn.img.susercontent.com/senior-product.webp"

        # Phân loại nhóm file dựa trên tuổi
        if age <= 8: target_file = 'database6.csv'
        elif age <= 11: target_file = 'database10.csv'
        else: target_file = 'database.csv'

        # Tạo thông tin quà tặng để ghi vào database
        item = {
            "stt": row['stt'],
            "name": f"Gợi ý cho STT {row['stt']}", # Ẩn danh tên thật
            "age": age,
            "img": row['img_url'],
            "link": row['product_link']
        }
        
        # Ghi vào file database tương ứng
        item_df = pd.DataFrame([item])
        item_df.to_csv(target_file, mode='a', index=False, 
                        header=not os.path.exists(target_file), 
                        encoding='utf-8-sig')
        
        updated_rows.append(row)

    # --- BƯỚC 3: CẬP NHẬT NGƯỢC LẠI FILE FRIENDS.CSV ---
    new_df = pd.DataFrame(updated_rows)
    new_df.to_csv('friends.csv', index=False, encoding='utf-8-sig')

    print("✨ XONG! Robot đã điền link vào friends.csv và phân loại ra các file database.")

# Chạy Robot
if __name__ == "__main__":
    robot_shopping_smart()
