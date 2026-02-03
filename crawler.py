import pandas as pd
import os
from datetime import datetime

# 1. Đọc danh sách bạn bè
try:
    df = pd.read_csv('friends.csv')
except Exception as e:
    print("❌ Lỗi: Không tìm thấy file friends.csv!")
    exit()

def robot_shopping_smart():
    # --- BƯỚC TỰ ĐỘNG XÓA CŨ (SÁNG TẠO) ---
    for f in ['database.csv', 'database10.csv', 'database6.csv']:
        if os.path.exists(f):
            os.remove(f)
            print(f"🧹 Đã dọn dẹp kệ hàng cũ: {f}")

    current_year = 2026
    print("🚀 Robot bắt đầu đi săn quà theo yêu cầu cá nhân hóa...")

    for _, row in df.iterrows():
        age = row['age']
        gender = row['gender']
        tags = row['last_chars']
        
        # 1. PHÂN LOẠI NHÓM TUỔI [cite: 2026-02-03]
        if age <= 8: target_file = 'database6.csv'
        elif age <= 11: target_file = 'database10.csv'
        else: target_file = 'database.csv'

        # 2. TẠO THÔNG TIN QUÀ TẶNG (NÂNG CẤP LẤY LINK THẬT)
        # Kiểm tra nếu có link thật trong CSV thì dùng, không thì dùng dự phòng [cite: 2026-02-03]
        real_img = row['img_url'] if 'img_url' in row and pd.notnull(row['img_url']) and str(row['img_url']).strip() != "" else "https://picsum.photos/200"
        real_link = row['product_link'] if 'product_link' in row and pd.notnull(row['product_link']) and str(row['product_link']).strip() != "" else "https://shope.ee/link_affiliate"

        item = {
            "name": f"Quà cho {row['name']} ({tags})",
            "price": 200000,
            "img": real_img,
            "link": real_link
        }
        
        # 3. GHI VÀO FILE
        item_df = pd.DataFrame([item])
        item_df.to_csv(target_file, mode='a', index=False, 
                       header=not os.path.exists(target_file), 
                       encoding='utf-8-sig')

    print("✨ XONG! Robot đã bày hàng thật lên kệ cho 3 chị em.")

# Chạy Robot
robot_shopping_smart()
