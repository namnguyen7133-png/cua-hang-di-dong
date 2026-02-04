import pandas as pd
import os

# 1. KHO HÀNG TỔNG HỢP (Tâm lý + Ngũ hành)
WAREHOUSE = {
    "Kim": { "link": "https://shopee.vn/product/876246295/24883502296", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#FFD700" }, # Vàng kim
    "Mộc": { "link": "https://shopee.vn/product/126828504/16539778234", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#2E8B57" }, # Xanh lá
    "Thủy": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#1E90FF" }, # Xanh dương
    "Hỏa": { "link": "https://shopee.vn/product/1251482363/24987802265", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#FF4500" }, # Đỏ cam
    "Thổ": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a", "color": "#8B4513" }, # Nâu đất
    "BAN_BE": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#f4f4f4" }
}

# 2. LỜI CHÚC THEO CUNG HOÀNG ĐẠO
ZODIAC_WISHES = {
    "Song Tử": "Chúc bạn luôn thông minh, nhạy bén và tràn đầy năng lượng sáng tạo!",
    "Thiên Bình": "Chúc bạn một năm mới luôn xinh đẹp, cân bằng và gặp nhiều điều may mắn!",
    "Sư Tử": "Chúc bạn luôn tỏa sáng như ánh mặt trời, bản lĩnh và thành công rực rỡ!",
    "Bảo Bình": "Chúc bạn có những ý tưởng đột phá và một năm mới tự do, hạnh phúc!",
    "Xử Nữ": "Chúc bạn một năm mới vẹn tròn, tinh tế và mọi việc đều suôn sẻ!",
    "Song Ngư": "Chúc bạn luôn mơ mộng hạnh phúc và gặp được những điều kỳ diệu!",
    "Bạch Dương": "Chúc bạn luôn giữ được lửa nhiệt huyết và dẫn đầu mọi cuộc chơi!",
    "Kim Ngưu": "Chúc bạn một năm mới sung túc, thịnh vượng và an yên!",
    "Cự Giải": "Chúc bạn luôn được bao bọc trong tình yêu thương ấm áp của gia đình!",
    "Bọ Cạp": "Chúc bạn luôn mạnh mẽ, quyết đoán và chinh phục mọi mục tiêu!",
    "Nhân Mã": "Chúc bạn có những hành trình mới đầy thú vị và niềm vui bất tận!",
    "Ma Kết": "Chúc bạn thăng tiến vững vàng và đạt được đỉnh cao sự nghiệp!"
}

def run_robot():
    try:
        df = pd.read_csv('friend')
    except:
        print("Lỗi: Không tìm thấy tệp 'friend'!")
        return

    if not os.path.exists('gift_pages'):
        os.makedirs('gift_pages')

    for index, row in df.iterrows():
        stt = row['stt']
        element = row.get('element', 'BAN_BE')
        zodiac = row.get('zodiac', 'Bạch Dương')
        
        # Lấy dữ liệu quà và màu sắc theo Mệnh
        gift_info = WAREHOUSE.get(element, WAREHOUSE["BAN_BE"])
        bg_color = gift_info['color']
        
        # Lấy lời chúc theo Cung
        wish = ZODIAC_WISHES.get(zodiac, "Chúc mừng năm mới 2026!")

        # Link và Ảnh (Ưu tiên từ CSV)
        final_link = row['product_link'] if not pd.isna(row['product_link']) else gift_info['link']
        final_img = row['img_url'] if not pd.isna(row['img_url']) else gift_info['img']

        # HTML SÁNG TẠO: Có pháo hoa và đổi màu nền
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{ text-align: center; background-color: {bg_color}; color: white; font-family: 'Segoe UI', sans-serif; padding: 50px; transition: 1s; }}
                .card {{ background: rgba(255, 255, 255, 0.2); padding: 30px; border-radius: 20px; backdrop-filter: blur(10px); display: inline-block; border: 1px solid white; }}
                img {{ border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); margin: 20px 0; }}
                .btn {{ display: inline-block; padding: 15px 30px; background: #ff4757; color: white; text-decoration: none; border-radius: 50px; font-weight: bold; font-size: 20px; box-shadow: 0 5px 15px rgba(255, 71, 87, 0.4); }}
                .btn:hover {{ transform: scale(1.1); background: #ff6b81; }}
                .wish {{ font-style: italic; font-size: 1.2em; margin: 20px 0; color: #fff; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🧧 LÌ XÌ MAY MẮN CHO STT {stt} 🧧</h1>
                <p>Bạn thuộc Mệnh: <b>{element}</b> | Cung: <b>{zodiac}</b></p>
                <div class="wish">"{wish}"</div>
                <img src="{final_img}" width="280px">
                <br>
                <a href="{final_link}" class="btn">MỞ QUÀ NGAY 🎁</a>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            <script>
                setInterval(() => {{
                    confetti({{ particleCount: 50, spread: 70, origin: {{ y: 0.6 }} }});
                }}, 3000);
            </script>
        </body>
        </html>
        """
        
        with open(f"gift_pages/friend_{stt}.html", "w", encoding="utf-8") as f:
            f.write(html_content)
            
    print(f"🚀 THÀNH CÔNG: Đã xuất 33 trang quà tặng 'Đúng-Đủ-Đẹp-Sáng Tạo' vào thư mục gift_pages!")

if __name__ == "__main__":
    run_robot()
