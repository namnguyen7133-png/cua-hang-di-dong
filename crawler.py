import pandas as pd

# Đây là danh sách hàng mà Robot tự đi tìm về
data = [
    {"name": "Đồ chơi Lego STEM cho bé", "price": 150000, "img": "https://picsum.photos/200", "link": "https://shope.ee/vidu1"},
    {"name": "Đèn học bảo vệ thị lực", "price": 250000, "img": "https://picsum.photos/201", "link": "https://shope.ee/vidu2"},
    {"name": "Bình nước giữ nhiệt 500ml", "price": 95000, "img": "https://picsum.photos/202", "link": "https://shope.ee/vidu3"}
]

# Robot lưu thành file database.csv để các file tre6, tre10, tre12 của bạn có thể đọc
df = pd.DataFrame(data)
df.to_csv('database.csv', index=False, encoding='utf-8-sig')
print("Robot đã cập nhật kho hàng thành công!")
