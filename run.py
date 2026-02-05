import pandas as pd
import json
import os
from datetime import datetime
from engine.boss_engine import select_boss
from engine.gift_engine import select_gift
from engine.story_engine import get_story_v1

def run_system():
    # 1. Cài đặt mệnh ngày hôm nay (Sau này có thể tự động hóa)
    TODAY_ELEMENT = "Moc" 
    
    print(f"🚀 Đang khởi động hệ thống Tiệm Lì Xì 2026...")

    # 2. Chạy Engine để chọn Sếp và Quà
    try:
        boss = select_boss(TODAY_ELEMENT)
        gift = select_gift(boss)
        story_data = get_story_v1(boss, gift) # Áp dụng KỂ CHUYỆN V1
    except Exception as e:
        print(f"❌ Lỗi khi chạy Engine: {e}")
        return

    # 3. Ghi lịch sử vào data/history.csv
    try:
        new_history = pd.DataFrame([{
            "date": datetime.now().strftime("%Y-%m-%d"),
            "boss_name": boss["name"],
            "product_name": gift["product_name"]
        }])
        new_history.to_csv("data/history.csv", mode='a', header=False, index=False)
        print(f"✅ Đã lưu lịch sử: {boss['name']} - {gift['product_name']}")
    except:
        print("⚠️ Không lưu được lịch sử (có thể thiếu file data/history.csv)")

    # 4. Tạo giao diện Web (index.html)
    html_content = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🧧 TIỆM LÌ XÌ 2026 🧧</title>
    <style>
        body {{ text-align:center; font-family:sans-serif; background:#d63031; color:white; padding:20px; }}
        .card {{ background:white; color:#333; padding:30px; border-radius:20px; display:inline-block; max-width:400px; box-shadow:0 10px 30px rgba(0,0,0,0.5); }}
        .story {{ background:#fff5f5; padding:15px; border-radius:10px; font-style:italic; border-left:5px solid #d63031; text-align:left; margin:20px 0; }}
        .btn {{ display:inline-block; background:#d63031; color:white; padding:15px 30px; text-decoration:none; border-radius:50px; font-weight:bold; }}
    </style>
</head>
<body>
    <div class="card">
        <h1 style="color:#d63031; margin-top:0;">🧧 SẾP HÔM NAY 🧧</h1>
        <h2 style="font-size:2em;">{boss['name']}</h2>
        <div class="story">
            <b>{story_data['loai']}:</b><br>
            "{story_data['content']}"
        </div>
        <hr>
        <p>Món quà duyên nợ: <b>{gift['product_name']}</b></p>
        <a href="{gift['product_link']}" target="_blank" class="btn">🛒 NHẬN QUÀ NGAY</a>
    </div>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("✅ Đã cập nhật xong giao diện Tiệm Lì Xì!")

if __name__ == "__main__":
    run_system()
