import random
import string
import json
import time
import os
from datetime import datetime

# 1. Hàm tạo link GitHub với mã ngẫu nhiên 5 ký tự
def tao_link_ngau_nhien():
    ma = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    # Đảm bảo link trỏ đúng vào file friends.csv mà bạn yêu cầu không được xóa
    link = f"https://github.com/namnguyen7133-png/cua-hang-di-dong/blob/main/friends.csv?v={ma}"
    return link

# 2. Hàm dọn dẹp và đổi tên tệp HTML theo chức năng/ngày
def quan_ly_tep_html():
    today = datetime.now().strftime("%d_%m")
    ten_file = f"nhiem_vu_{today}.html"
    
    if os.path.exists(ten_file):
        print(f"--- Đang mở tệp nhiệm vụ hôm nay: {ten_file} ---")
        # Logic thông báo các liên quan trong tệp ở đây...
        
        # Sau khi hoàn thành, đổi tên tệp để "dọn dẹp" (đánh dấu đã xong)
        os.rename(ten_file, f"DA_XU_LY_{ten_file}")
        return True
    return False

# 3. Hàm tạo nội dung Story tích hợp chờ 30 phút gắn link
def get_story_v1(boss, gift):
    rel = boss.get("relationship", "ban_be") 
    stories = {
        "tre_em": {"loai": "A. NGỤ NGÔN", "content": f"Chú thỏ nhỏ {boss['name']} đã tìm thấy {gift['product_name']}."},
        "cha_me": {"loai": "C. ĐỜI THƯỜNG", "content": f"Món quà {gift['product_name']} này như lời tri ân gửi đến {boss['name']}."},
        "ban_be": {"loai": "D. TIẾU LÂM", "content": f"Tình cờ thế nào mà {boss['name']} lại va phải {gift['product_name']}!"},
        "dan_ong": {"loai": "F. KIẾM TIỀN", "content": f"{gift['product_name']} sẽ là bạn đồng hành cùng {boss['name']}."},
        "phu_nu": {"loai": "G. TÌNH CẢM", "content": f"Gửi chút tinh tế qua {gift['product_name']} đến {boss['name']}."}
    }
    
    bai_dang = stories.get(rel, stories["ban_be"])
    
    # THỰC HIỆN QUY TRÌNH 30 PHÚT
    print(f"Đã đăng nội dung: {bai_dang['content']}")
    print("Robot đang chờ 30 phút để gắn link GitHub ngẫu nhiên...")
    
    # Tạm dừng 1800 giây (30 phút)
    time.sleep(1800) 
    
    link_final = tao_link_ngau_nhien()
    print(f"Đã gắn thêm link dự phòng vào bài đăng: {link_final}")
    
    return bai_dang, link_final
