import pandas as pd
import os
import time

def run_robot():
    try:
        df = pd.read_csv('friends.csv')
    except:
        print("Không tìm thấy file friends.csv!")
        return

    if not os.path.exists('gift_pages'):
        os.makedirs('gift_pages')

    # Khởi tạo Trang Chủ (Index)
    index_html = f"""
    <html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VƯƠNG QUỐC LÌ XÌ 2026</title>
    <style>
        body {{ text-align: center; font-family: 'Segoe UI', Arial; background: #fff5f5; padding: 20px; }}
        .header {{ background: #d63031; color: white; padding: 20px; border-radius: 15px; margin-bottom: 20px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 15px; max-width: 1000px; margin: auto; }}
        .card {{ background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); text-decoration: none; color: #d63031; font-weight: bold; border: 2px solid #ff7675; }}
    </style></head>
    <body>
        <div class="header"><h1>🧧 DANH SÁCH 33 BAO LÌ XÌ 🧧</h1></div>
        <div class="grid">
    """

    for index, row in df.iterrows():
        stt = row['stt']
        element = str(row.get('element', 'Kim')).strip()
        p_link = row['product_link'] if not pd.isna(row['product_link']) else "https://shopee.vn"
        p_img = row['img_url'] if not pd.isna(row['img_url']) else "https://via.placeholder.com/300"
        
        # Tạo trang con với mã chống lưu cache (?v=...)
        child_html = f"""
        <html><body style="text-align:center; background:#d63031; color:white; font-family:sans-serif; padding:50px;">
            <div style="background:white; color:#333; padding:30px; border-radius:20px; display:inline-block; max-width:350px;">
                <h2 style="color:#d63031;">🧧 QUÀ TẶNG SỐ {stt} 🧧</h2>
                <img src="{p_img}" style="width:100%; border-radius:15px; margin-bottom:20px;">
                <br>
                <a href="{p_link}" target="_blank" style="display:inline-block; padding:15px 35px; background:#d63031; color:white; text-decoration:none; border-radius:50px; font-weight:bold; font-size:1.1em;">🛒 MUA QUÀ NGAY</a>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            <script>setInterval(() => {{ confetti({{ particleCount: 50, spread: 70, origin: {{ y: 0.6 }} }}); }}, 2000);</script>
        </body></html>
        """
        with open(f"gift_pages/friend_{stt}.html", "w", encoding="utf-8") as f:
            f.write(child_html)

        # Thêm nút vào trang chủ (kèm mã thời gian để tránh cache)
        index_html += f'<a href="gift_pages/friend_{stt}.html?v={time.time()}" class="card">🎁 SỐ {stt}<br><span style="font-size:10px; color:#666;">{element}</span></a>'

    index_html += "</div></body></html>"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

if __name__ == "__main__":
    run_robot()
