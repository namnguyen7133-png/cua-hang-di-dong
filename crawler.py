import pandas as pd
import os

# 1. KHO HÀNG TỔNG HỢP
WAREHOUSE = {
    "Kim": { "link": "https://shopee.vn/product/876246295/24883502296", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#FFD700" },
    "Mộc": { "link": "https://shopee.vn/product/126828504/16539778234", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#2E8B57" },
    "Thủy": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#1E90FF" },
    "Hỏa": { "link": "https://shopee.vn/product/1251482363/24987802265", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#FF4500" },
    "Thổ": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a", "color": "#8B4513" },
    "BAN_BE": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#f4f4f4" }
}

def run_robot():
    try:
        df = pd.read_csv('friends.csv') # Đảm bảo file tên là friends.csv như trong ảnh bạn up
    except:
        print("Lỗi: Không tìm thấy file friends.csv!")
        return

    if not os.path.exists('gift_pages'): os.makedirs('gift_pages')

    # Khởi tạo nội dung Trang Chủ (Index)
    index_html = """
    <html>
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { text-align: center; font-family: Arial; background: #fdf2f2; padding: 20px; }
            .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 15px; padding: 20px; }
            .name-card { background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-decoration: none; color: #d63031; font-weight: bold; }
            .name-card:hover { background: #ff7675; color: white; transform: scale(1.05); }
        </style>
    </head>
    <body>
        <h1>🧧 DANH SÁCH NHẬN QUÀ TẾT 2026 🧧</h1>
        <div class="grid">
    """

    for index, row in df.iterrows():
        stt = row['stt']
        element = str(row.get('element', 'Kim')).strip()
        gift_info = WAREHOUSE.get(element, WAREHOUSE["BAN_BE"])
        
        # Tạo trang con (gift_pages/friend_x.html)
        page_content = f"""
        <html><body style="text-align:center; background:{gift_info['color']}; color:white; font-family:sans-serif; padding:50px;">
            <div style="background:rgba(255,255,255,0.2); padding:20px; border-radius:20px; display:inline-block; border:1px solid white;">
                <h1>LÌ XÌ CHO STT {stt}</h1>
                <p>Mệnh: {element}</p>
                <img src="{gift_info['img']}" width="250" style="border-radius:15px; margin:20px 0;">
                <br><a href="{gift_info['link']}" style="padding:15px 25px; background:#d63031; color:white; text-decoration:none; border-radius:50px; font-weight:bold;">MỞ QUÀ NGAY 🎁</a>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            <script>setInterval(() => {{ confetti({{ particleCount: 40, spread: 60, origin: {{ y: 0.7 }} }}); }}, 2000);</script>
        </body></html>
        """
        with open(f"gift_pages/friend_{stt}.html", "w", encoding="utf-8") as f: f.write(page_content)

        # Thêm nút vào Trang Chủ
        index_html += f'<a href="gift_pages/friend_{stt}.html" class="name-card">🎁 Bao Lì Xì {stt}</a>'

    index_html += "</div></body></html>"
    with open("index.html", "w", encoding="utf-8") as f: f.write(index_html)

if __name__ == "__main__":
    run_robot()
