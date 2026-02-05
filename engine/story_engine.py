import json

def get_story_v1(boss, gift):
    rel = boss.get("relationship", "ban_be") 
    stories = {
        "tre_em": {"loai": "A. NGỤ NGÔN", "content": f"Chú thỏ nhỏ {boss['name']} đã tìm thấy {gift['product_name']}."},
        "cha_me": {"loai": "C. ĐỜI THƯỜNG", "content": f"Món quà {gift['product_name']} này như lời tri ân gửi đến {boss['name']}."},
        "ban_be": {"loai": "D. TIẾU LÂM", "content": f"Tình cờ thế nào mà {boss['name']} lại va phải {gift['product_name']}!"},
        "dan_ong": {"loai": "F. KIẾM TIỀN", "content": f"{gift['product_name']} sẽ là bạn đồng hành cùng {boss['name']}."},
        "phu_nu": {"loai": "G. TÌNH CẢM", "content": f"Gửi chút tinh tế qua {gift['product_name']} đến {boss['name']}."}
    }
    return stories.get(rel, stories["ban_be"])
