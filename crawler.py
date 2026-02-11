import pandas as pd
import os
import time
import datetime

def calculate_menh_hour():
    now = datetime.datetime.now()
    # Công thức: (Ngày * Giờ) mod 24, nếu 0 lấy 24
    val = (now.day * now.hour) % 24
    return val if val != 0 else 24

def run_robot():
    # 1. Đọc file CSV
    try:
        df = pd.read_csv("friends.csv", encoding="utf-8")
    except FileNotFoundError:
        print("❌ Không tìm thấy file friends.csv")
        return

    # 2. Tính toán Mệnh Giờ hiện tại
    current_menh_hour = calculate_menh_hour()
    print(f"🤖 Robot khởi động - Mệnh Giờ hiện tại: {current_menh_hour}")

    # 3. Tạo thư mục
    os.makedirs("gift_pages", exist_ok=True)

    # 4. Header Trang chủ
    index_html = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VƯƠNG QUỐC LÌ XÌ 2026</title>
<style>
body { text-align:center; font-family:'Segoe UI', Arial; background:#fff5f5; padding:20px; }
.header { background:#d63031; color:white; padding:20px; border-radius:15px; margin-bottom:20px; }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(140px,1fr)); gap:15px; max-width:1000px; margin:auto; }
.card { background:white; padding:15px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,.1);
        text-decoration:none; color:#d63031; font-weight:bold; border:2px solid #ff7675; position:relative; overflow:hidden;}
.best-choice { border: 3px solid #f1c40f; background: #fff9e6; transform: scale(1.05); }
.badge { position:absolute; top:0; right:0; background:#f1c40f; color:black; font-size:10px; padding:2px 5px; }
</style>
</head>
<body>
<div class="header">
    <h1>🧧 TIỆM LÌ XÌ ROBOT BRAIN 🧧</h1>
    <p>Mệnh Giờ Hệ Thống: <strong>{current_menh_hour}</strong></p>
</div>
<div class="grid">
""".replace("{current_menh_hour}", str(current_menh_hour))

    # 5. Tạo từng trang con và xử lý logic Chọn Sếp
    # Giả sử chúng ta coi những bao lì xì có STT khớp với Mệnh Giờ là "Sếp"
    for _, row in df.iterrows():
        try:
            stt = int(row["stt"])
        except: continue

        element = str(row.get("element", "Kim")).strip()
        product_link = str(row.get("product_link", "https://shopee.vn"))
        img_url = str(row.get("img_url", "https://via.placeholder.com/300"))

        # Xác định xem đây có phải là "Sếp" được chọn không
        is_best = "best-choice" if stt == current_menh_hour else ""
        badge = '<div class="badge">SẾP CHỌN</div>' if stt == current_menh_hour else ""

        # Ghi file HTML trang con (Giữ nguyên logic của bạn)
        child_html = f"""
<!DOCTYPE html>
<html lang="vi">
<head><meta charset="UTF-8"><title>QUÀ TẶNG {stt}</title></head>
<body style="text-align:center; background:#d63031; color:white; font-family:sans-serif; padding:50px;">
    <div style="background:white; color:#333; padding:30px; border-radius:20px; display:inline-block; max-width:350px;">
        <h2 style="color:#d63031;">🧧 QUÀ TẶNG SỐ {stt} 🧧</h2>
        <p style="color:#666;">Mệnh: {element}</p>
        <img src="{img_url}" style="width:100%; border-radius:15px; margin-bottom:20px;">
        <br>
        <a href="{product_link}" target="_blank"
           style="display:inline-block; padding:15px 35px; background:#d63031; color:white;
                  text-decoration:none; border-radius:50px; font-weight:bold; font-size:1.1em;">
           🛒 MUA QUÀ NGAY
        </a>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>setInterval(() => {{ confetti({{ particleCount: 50, spread: 70, origin: {{ y: 0.6 }} }}); }}, 2000);</script>
</body>
</html>
"""
        with open(f"gift_pages/friend_{stt}.html", "w", encoding="utf-8") as f:
            f.write(child_html)

        # Thêm vào trang chủ với class highlight nếu là "Sếp"
        index_html += (
            f'<a href="gift_pages/friend_{stt}.html?v={int(time.time())}" class="card {is_best}">'
            f'{badge}🎁 SỐ {stt}<br><span style="font-size:10px;color:#666;">{element}</span></a>'
        )

    # 6. Đóng trang chủ
    index_html += "</div><p style='margin-top:20px; color:#999;'>Last Update: " + datetime.datetime.now().strftime("%H:%M:%S") + "</p></body></html>"

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    print(f"✅ Đã cập nhật Tiệm Lì Xì với Mệnh Giờ {current_menh_hour}!")

if __name__ == "__main__":
    run_robot()

