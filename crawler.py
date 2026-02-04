import pandas as pd
import os

# 1. KHO HÀNG TỔNG HỢP (Tâm lý + Ngũ hành)
WAREHOUSE = {
    "Kim": { "link": "https://shopee.vn/product/876246295/24883502296", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#FFD700" },
    "Mộc": { "link": "https://shopee.vn/product/126828504/16539778234", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#2E8B57" },
    "Thủy": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#1E90FF" },
    "Hỏa": { "link": "https://shopee.vn/product/1251482363/24987802265", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#FF4500" },
    "Thổ": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a", "color": "#8B4513" },
    "BAN_BE": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#f4f4f4" }
}

# 2. LỜI CHÚC THEO CUNG HOÀNG ĐẠO
ZODIAC_WISHES = {
    "Song Tử": "Thông minh, nhạy bén và tràn đầy sáng tạo nhé!",
    "Thiên Bình": "Một năm mới cân bằng, xinh đẹp và nhiều may mắn!",
    "Sư Tử": "Luôn tỏa sáng rực rỡ và bản lĩnh như chính bạn!",
    "Bảo Bình": "Đột phá ý tưởng và luôn tự do, hạnh phúc!",
    "Xử Nữ": "Mọi việc vẹn tròn, tinh tế và suôn sẻ!",
    "Song Ngư": "Mơ mộng hạnh phúc và gặp nhiều điều kỳ diệu!",
    "Bạch Dương": "Giữ vững nhiệt huyết và dẫn đầu mọi cuộc chơi!",
    "Kim Ngưu": "Sung túc, thịnh vượng và an yên cả năm!",
    "Cự Giải": "Ấm áp tình thương và hạnh phúc đong đầy!",
    "Bọ Cạp": "Mạnh mẽ, quyết đoán và chinh phục đỉnh cao!",
    "Nhân Mã": "Hành trình mới đầy thú vị và niềm vui bất tận!",
    "Ma Kết": "Thăng tiến vững vàng, sự nghiệp hanh thông!"
}

def run_robot():
    # Đọc tệp friend
    try:
        df = pd.read_csv('friend')
    except:
        print("Lỗi: Không tìm thấy tệp 'friend'!")
        return

    # Tạo thư mục con nếu chưa có
    if not os.path.exists('gift_pages'):
        os.makedirs('gift_pages')

    # Bắt đầu soạn nội dung cho Trang Chủ (Index)
    index_html = """
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { text-align: center; font-family: 'Segoe UI', Arial; background: #fdf2f2; padding: 20px; }
            h1 { color: #d63031; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); }
            .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 15px; padding: 20px; max-width: 1000px; margin: auto; }
            .name-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-decoration: none; color: #d63031; font-weight: bold; transition: 0.3s; border: 2px solid #fab1a0; }
            .name-card:hover { background: #ff7675; color: white; transform: translateY(-5px); }
        </style>
    </head>
    <body>
        <h1>🧧 TIỆM LÌ XÌ MAY MẮN 2026 🧧</h1>
        <p>Tìm đúng số của bạn để nhận quà phong thủy nhé!</p>
        <div class="grid">
    """

    for index, row in df.iterrows():
        stt = row['stt']
        element = str(row.get('element', 'Kim')).strip()
        zodiac = str(row.get('zodiac', 'Bạch Dương')).strip()
        
        # Lấy quà từ kho
        gift_info = WAREHOUSE.get(element, WAREHOUSE["BAN_BE"])
        wish = ZODIAC_WISHES.get(zodiac, "Chúc mừng năm mới!")

        # Link và Ảnh (Ưu tiên từ CSV)
        final_link = row['product_link'] if not pd.isna(row['product_link']) else gift_info['link']
        final_img = row['img_url'] if not pd.isna(row['img_url']) else gift_info['img']

        # TẠO TRANG CON CHO TỪNG NGƯỜI
        page_content = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{ text-align: center; background-color: {gift_info['color']}; color: white; font-family: sans-serif; padding: 30px; }}
                .card {{ background: rgba(255,255,255,0.2); padding: 20px; border-radius: 20px; backdrop-filter: blur(10px); display: inline-block; border: 1px solid white; }}
                img {{ border-radius: 15px; margin: 20px 0; max-width: 100%; height: auto; }}
                .btn {{ display: inline-block; padding: 15px 25px; background: #d63031; color: white; text-decoration: none; border-radius: 50px; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>STT {stt} - LÌ XÌ MỆNH {element.upper()}</h2>
                <p>Cung {zodiac}: {wish}</p>
                <img src="{final_img}" width="250">
                <br>
                <a href="{final_link}" class="btn">MỞ QUÀ NGAY 🎁</a>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            <script>setInterval(() => {{ confetti({{ particleCount: 40, spread: 60, origin: {{ y: 0.7 }} }}); }}, 2500);</script>
        </body>
        </html>
        """
        with open(f"gift_pages/friend_{stt}.html", "w", encoding="utf-8") as f:
            f.write(page_content)

        # THÊM NÚT VÀO TRANG CHỦ
        index_html += f'<a href="gift_pages/friend_{stt}.html" class="name-card">🎁 STT {stt}</a>'

    # ĐÓNG FILE TRANG CHỦ
    index_html += "</div></body></html>"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

if __name__ == "__main__":
    run_robot()
