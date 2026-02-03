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
    # Robot tự kiểm tra và xóa sạch dữ liệu cũ để không bị trùng lặp
    for f in ['database.csv', 'database10.csv', 'database6.csv']:
        if os.path.exists(f):
            os.remove(f)
            print(f"🧹 Đã dọn dẹp kệ hàng cũ: {f}")

    current_year = 2026
    print("🚀 Robot bắt đầu đi săn quà cho danh sách 32 người...")

    for _, row in df.iterrows():
        age = row['age']
        gender = row['gender']
        tags = row['last_chars']
        
        # 1. PHÂN LOẠI NHÓM TUỔI [cite: 2026-02-03]
        if age <= 8: target_file = 'database6.csv'
        elif age <= 11: target_file = 'database10.csv'
        else: target_file = 'database.csv'

        # 2. TẠO THÔNG TIN QUÀ TẶNG (SÁNG TẠO)
        item = {
            "name": f"Quà cho {row['name']} ({tags})",
            "price": 200000,
            "img": "https://picsum.photos/200",
            "link": "https://shope.ee/link_affiliate"
        }
        
        # 3. GHI VÀO FILE (Dùng mode='a' nhưng vì đã xóa ở trên nên luôn là hàng mới)
        item_df = pd.DataFrame([item])
        item_df.to_csv(target_file, mode='a', index=False, 
                       header=not os.path.exists(target_file), 
                       encoding='utf-8-sig')

    print("✨ XONG! Toàn bộ kệ hàng đã được thay mới hoàn toàn.")

# Chạy Robot
robot_shopping_smart()
