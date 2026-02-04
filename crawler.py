import pandas as pd

# 1. KHO HÀNG TỔNG HỢP (Gộp cả Tâm lý và Ngũ hành)
WAREHOUSE = {
    # --- NHÓM TÂM LÝ ---
    "NAM": { "link": "https://shopee.vn/product/1251482363/24987802265", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "NU": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a" },
    "TRE_EM": { "link": "https://shopee.vn/product/466965128/11526582452", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "NGUOI_GIA": { "link": "https://shopee.vn/product/416741194/7988383802", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c" },
    "CHA_ME": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a" },
    "ANH_EM": { "link": "https://shopee.vn/product/1024364843/21081350503", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "NGUOI_NGHEO": { "link": "https://shopee.vn/product/240881396/22041736497", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "NGUOI_GIAU": { "link": "https://shopee.vn/product/111109565/29016412955", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c" },
    "NGUOI_YEU": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "BAN_BE": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "SEP": { "link": "https://shopee.vn/product/876246295/24883502296", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c" },
    "CAP_DUOI": { "link": "https://shopee.vn/product/724644824/18696382065", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "KHACH_HANG": { "link": "https://shopee.vn/product/240881396/22041736497", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "NGUOI_GIOI": { "link": "https://shopee.vn/product/126828504/16539778234", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c" },
    "VO": { "link": "https://shopee.vn", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a" },
    
    # --- NHÓM NGŨ HÀNH ---
    "Kim": { "link": "https://shopee.vn/product/876246295/24883502296", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c" },
    "Mộc": { "link": "https://shopee.vn/product/126828504/16539778234", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r95j9z5v3c" },
    "Thủy": { "link": "https://shopee.vn/product/187219278/54200999615", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "Hỏa": { "link": "https://shopee.vn/product/1251482363/24987802265", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r8z7p5z5e1" },
    "Thổ": { "link": "https://shopee.vn/product/375938299/27602165886", "img": "https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m4p5r91v6k8l3a" }
}

def run_robot():
    # Đọc tệp friend (Hãy đảm bảo file này đã được upload lên cùng thư mục)
    try:
        df = pd.read_csv('friend')
    except Exception as e:
        print("Lỗi: Không tìm thấy tệp 'friend'. Kiểm tra lại tên file nhé!")
        return

    for index, row in df.iterrows():
        # Lấy thông tin cơ bản
        stt = row['stt']
        element = row['element']
        zodiac = row['zodiac']
        
        # LOGIC CHỌN QUÀ THÔNG MINH:
        # 1. Ưu tiên link riêng trong file CSV (nếu có)
        final_link = row['product_link']
        final_img = row['img_url']
        
        # 2. Nếu link trong CSV trống, Robot tự tra trong WAREHOUSE theo Mệnh (element)
        if pd.isna(final_link) or str(final_link).strip() == "":
            gift_data = WAREHOUSE.get(element, WAREHOUSE["BAN_BE"]) # Mặc định là bạn bè nếu không tìm thấy mệnh
            final_link = gift_data['link']
            final_img = gift_data['img']
            
        print(f"✅ Đã xử lý xong STT {stt}: Mệnh {element} - Cung {zodiac}")
        print(f"   -> Quà: {final_link}")

if __name__ == "__main__":
    run_robot()
