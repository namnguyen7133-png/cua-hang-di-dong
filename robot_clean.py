import pandas as pd
import os
import glob
from datetime import datetime

# 1. Tìm file trong raw_data (hộp nhận hàng)
raw_files = glob.glob('raw_data/*.csv')

if not raw_files:
    print("Robot: Chưa có file nào để dọn dẹp cả!")
    exit()

# 2. Đảm bảo có hộp chứa hàng sạch (processed_data)
if not os.path.exists('processed_data'):
    os.makedirs('processed_data')

# 3. Robot bắt đầu làm việc
for file_path in raw_files:
    try:
        # Đọc dữ liệu
        df = pd.read_csv(file_path)
        
        # Làm sạch: Xóa hàng trùng
        df = df.drop_duplicates()
        
        # Đặt tên mới theo ngày: Năm-Tháng-Ngày
        ten_moi = datetime.now().strftime('%Y-%m-%d') + "_Shopee_Clean.csv"
        duong_dan_moi = os.path.join('processed_data', ten_moi)
        
        # Lưu file sạch
        df.to_csv(duong_dan_moi, index=False)
        print(f"Robot: Đã dọn xong và cất vào {duong_dan_moi}")
        
        # Xóa file cũ để kho luôn sạch
        os.remove(file_path)
        
    except Exception as e:
        print(f"Robot: Gặp lỗi rồi đại ca ơi: {e}")
