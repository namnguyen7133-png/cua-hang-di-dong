import pandas as pd
import os

def run_robot():
    try:
        # Đọc dữ liệu từ file CSV của bạn
        df = pd.read_csv('friends.csv')
    except:
        print("Không tìm thấy file friends.csv!")
        return

    # Tạo thư mục chứa trang quà tặng cá nhân
    if not os.path.exists('gift_pages'):
        os.makedirs('gift_pages')

    # --- KHỞI TẠO GIAO DIỆN TRANG CHỦ TỔNG (Dành cho 33 người) ---
    index_html = """
    <html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VƯƠNG QUỐC LÌ XÌ 2026</title>
    <style>
        body { text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #fff5f5; padding: 20px; color: #333; }
        .header { background: linear-gradient(135deg, #ff7675, #d63031); color: white; padding: 30px; border-radius: 20px; margin-bottom: 30px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 20px; max-width: 1000px; margin: auto; }
        .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.08); text-decoration: none; color: #d63031; font-weight: bold; border: 2px solid #ff7675; transition: 0.3s; display: flex; flex-direction: column; align-items: center; justify-content: center; }
        .card:hover { transform: translateY(-5px); background: #ff7675; color: white; }
        .card span { font-size: 0.9em; color: #636e72; margin-top: 5px; }
        .card:hover span { color: white; }
    </style></head>
    <body>
        <div class="header"><h1>🧧 VƯƠNG QUỐC LÌ XÌ MAY MẮN 🧧</h1><p>Danh sách 33 thành viên nhận quà Tết 2026</p></div>
        <div class="grid">
    """

    for index, row in df.iterrows():
        stt = row['stt']
        element = str(row.get('element', 'Kim')).strip()
        zodiac = str(row.get('zodiac', 'Song Tử')).strip()
        
        # Sửa lỗi link: Nếu link sản phẩm trống, lấy link ảnh làm link mua (hoặc ngược lại)
        p_link = row['product_link'] if not pd.isna(row['product_link']) else "https://shopee.vn"
        p_img = row['img_url'] if not pd.isna(row['img_url']) else "https://via.placeholder.com/300"
        
        # Màu sắc theo mệnh
        colors = {"Kim": "#f1c40f", "Mộc": "#2ecc71", "Thủy": "#3498db", "Hỏa": "#e67e22", "Thổ": "#a14a06"}
        bg_color = colors.get(element, "#d63031")

        # --- TẠO TRANG CHI TIẾT CHO TỪNG NGƯỜI ---
        child_html = f"""
        <html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
        <body style="text-align:center; background:{bg_color}; color:white; font-family:sans-serif; padding:50px;">
            <div style="background:rgba(255,255,255,0.95); color:#333; padding:40px; border-radius:30px; display:inline-block; max-width:400px; box-shadow: 0 20px 40px rgba(0,0,0,0.3);">
                <h2 style="color:{bg_color}">🧧 QUÀ TẶNG STT {stt} 🧧</h2>
                <div style="background:#f9f9f9; padding:15px; border-radius:15px; margin-bottom:20px;">
                    <p><b>Mệnh:</b> {element} | <b>Cung:</b> {zodiac}</p>
                </div>
                <img src="{p_img}" style="width:100%; border-radius:20px; margin-bottom:25px; border: 5px solid {bg_color};">
                <br>
                <a href="{p_link}" target="_blank" style="display:inline-block; padding:18px 40px; background:{bg_color}; color:white; text-decoration:none; border-radius:50px; font-weight:bold; font-size:1.2em; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">🛒 MUA QUÀ NGAY</a>
                <p style="margin-top:20px; font-size:0.8em; color:#636e72;">(Bấm nút trên để đến cửa hàng Shopee)</p>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            <script>setInterval(() => {{ confetti({{ particleCount: 50, spread: 70, origin: {{ y: 0.6 }} }}); }}, 2000);</script>
        </body></html>
        """
        with open(f"gift_pages/friend_{stt}.html", "w", encoding="utf-8") as f:
            f.write(child_html)

        # Thêm nút bấm vào trang chủ chính
        index_html += f'''
        <a href="gift_pages/friend_{stt}.html" class="card">
            🎁 SỐ {stt}
            <span>{element} - {zodiac}</span>
        </a>'''

    index_html += "</div></body></html>"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

if __name__ == "__main__":
    run_robot()
