"""
    1. Khai báo 1 list có n phần tử thực. Nhập và hiển thị n phần tử của list.
    
    Gợi ý:
    Nhập n
    Chạy vòng lặp từ 0 -> n
        Nhập giá trị cần thêm vào list
        append giá trị vào list
"""

# Nhập n
n = int(input("n = "))
# Khai báo list
danh_sach = []
# Chạy vòng lặp từ 0 đến n
for i in range(n):
    value = float(input("Nhập giá trị: "))
    danh_sach.append(value)
# Hiển thị list vừa nhập
for x in danh_sach:
    print(x, end = "    ")
# Hiển thị list vừa nhập theo index
for m in range(len(danh_sach)):
    print(danh_sach[m], end = "    ")