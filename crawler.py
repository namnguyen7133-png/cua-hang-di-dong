import pandas as pd
import os

# 1. KHO HÀNG TỔNG HỢP
WAREHOUSE = {
    "NAM": { "link": "https://shopee.vn/product/1251482363/24987802265", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "NU": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a" },
    "TRE_EM": { "link": "https://shopee.vn/product/466965128/11526582452", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "NGUOI_GIA": { "link": "https://shopee.vn/product/416741194/7988383802", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c" },
    "BAN_BE": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "Kim": { "link": "https://shopee.vn/product/876246295/24883502296", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c" },
    "Mộc": { "link": "https://shopee.vn/product/126828504/16539778234", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c" },
    "Thủy": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "Hỏa": { "link": "https://shopee.vn/product/1251482363/24987802265", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "Thổ": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a" }
}

def run_robot():
    try:
        df = pd.read_csv('friend')
    except:
        print("Lỗi: Không tìm thấy tệp 'friend'!")
        return

    # Tạo thư mục chứa web nếu chưa có
    if not os.path.exists('gift_pages'):
        os.makedirs('gift_pages')

    for index, row in df.iterrows():
        stt = row['stt']
        element = row['element']
        zodiac = row['zodiac']
        
        # CHỌN QUÀ
        final_link = row['product_link']
        final_img = row['img_url']
        
        if pd.isna(final_link) or str(final_link).strip() == "":
            gift_data = WAREHOUSE.get(element, WAREHOUSE["BAN_BE"])
            final_link = gift_data['link']
            final_img = gift_data['img']

        # SÁNG TẠO: Tạo giao diện HTML cho từng người
        html_content = f"""
        <html>
            <body style="text-align: center; font-family: Arial;">
                <h1>Chúc Mừng Năm Mới - STT {stt}</h1>
                <p>Mệnh của bạn: {element} | Cung: {zodiac}</p>
                <img src="{final_img}" width="300px">
                <br><br>
                <a href="{final_link}" style="padding: 10px; background: red; color: white; text-decoration: none;">Bấm nhận quà lì xì</a>
            </body>
        </html>
        """
        
        # Lưu thành file html riêng cho mỗi người
        with open(f"gift_pages/friend_{stt}.html", "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print(f"✅ Đã tạo trang web cho STT {stt} thành công!")

if __name__ == "__main__":
    run_robot()
