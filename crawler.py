import pandas as pd
import os

# 1. KHO HÀNG TỔNG HỢP (15 Nhóm Tâm Lý + 5 Ngũ Hành)
WAREHOUSE = {
    # --- 15 NHÓM TÂM LÝ ---
    "NAM": { "link": "https://shopee.vn/product/1251482363/24987802265", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#2c3e50" },
    "NU": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a", "color": "#e84393" },
    "TRE_EM": { "link": "https://shopee.vn/product/466965128/11526582452", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#fab1a0" },
    "NGUOI_GIA": { "link": "https://shopee.vn/product/416741194/7988383802", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#636e72" },
    "CHA_ME": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a", "color": "#6c5ce7" },
    "ANH_EM": { "link": "https://shopee.vn/product/1024364843/21081350503", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#0984e3" },
    "NGUOI_NGHEO": { "link": "https://shopee.vn/product/240881396/22041736497", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#b2bec3" },
    "NGUOI_GIAU": { "link": "https://shopee.vn/product/111109565/29016412955", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#f1c40f" },
    "NGUOI_YEU": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#ff7675" },
    "BAN_BE": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#55efc4" },
    "SEP": { "link": "https://shopee.vn/product/876246295/24883502296", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#2d3436" },
    "CAP_DUOI": { "link": "https://shopee.vn/product/724644824/18696382065", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#00cec9" },
    "KHACH_HANG": { "link": "https://shopee.vn/product/240881396/22041736497", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#74b9ff" },
    "NGUOI_GIOI": { "link": "https://shopee.vn/product/126828504/16539778234", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#a29bfe" },
    "VO": { "link": "https://shopee.vn", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a", "color": "#fd79a8" },

    # --- 5 NHÓM NGŨ HÀNH ---
    "Kim": { "link": "https://shopee.vn/product/876246295/24883502296", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#FFD700" },
    "Mộc": { "link": "https://shopee.vn/product/126828504/16539778234", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c", "color": "#2E8B57" },
    "Thủy": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#1E90FF" },
    "Hỏa": { "link": "https://shopee.vn/product/1251482363/24987802265", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1", "color": "#FF4500" },
    "Thổ": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a", "color": "#8B4513" }
}

def run_robot():
    try:
        df = pd.read_csv('friends.csv')
    except:
        print("Lỗi: Không tìm thấy file friends.csv!")
        return

    if not os.path.exists('gift_pages'):
        os.makedirs('gift_pages')

    # Header Trang Chủ
    index_html = """
    <html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { text-align: center; font-family: Arial; background: #fdf2f2; padding: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 15px; max-width: 900px; margin: auto; }
        .name-card { background: white; padding: 15px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-decoration: none; color: #d63031; font-weight: bold; border: 2px solid #fab1a0; }
        .name-card:hover { background: #ff7675; color: white; transform: scale(1.05); }
    </style></head>
    <body><h1>🧧 TIỆM LÌ XÌ TỔNG HỢP 2026 🧧</h1><div class="grid">
    """

    for index, row in df.iterrows():
        stt = row['stt']
        # Robot sẽ tìm quà theo 'element' (Mệnh) trước, nếu không thấy sẽ tìm theo 'category' (Tâm lý)
        key = str(row.get('element', row.get('category', 'BAN_BE'))).strip()
        gift = WAREHOUSE.get(key, WAREHOUSE["BAN_BE"])
        
        # Link và Ảnh (Ưu tiên file CSV)
        p_img = gift['img'] if pd.isna(row.get('img_url')) else row['img_url']
        p_link = gift['link'] if pd.isna(row.get('product_link')) else row['product_link']

        # Trang con
        page_content = f"""
        <html><body style="text-align:center; background:{gift['color']}; color:white; font-family:sans-serif; padding:50px;">
            <div style="background:rgba(255,255,255,0.2); padding:30px; border-radius:20px; display:inline-block; border:1px solid white;">
                <h1>🧧 LÌ XÌ STT {stt} 🧧</h1>
                <p>Nhóm: {key}</p>
                <img src="{p_img}" width="250" style="border-radius:15px; margin:20px 0;">
                <br><a href="{p_link}" style="padding:15px 25px; background:#d63031; color:white; text-decoration:none; border-radius:50px; font-weight:bold;">NHẬN QUÀ NGAY</a>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            <script>setInterval(() => {{ confetti({{ particleCount: 40, spread: 60, origin: {{ y: 0.7 }} }}); }}, 2000);</script>
        </body></html>
        """
        with open(f"gift_pages/friend_{stt}.html", "w", encoding="utf-8") as f:
            f.write(page_content)

        index_html += f'<a href="gift_pages/friend_{stt}.html" class="name-card">🎁 STT {stt}</a>'

    index_html += "</div></body></html>"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

if __name__ == "__main__":
    run_robot()
