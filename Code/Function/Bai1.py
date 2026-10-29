"""
    1. Nhập 2 số nguyên a, b. Tính +, -, *, / của 2 số
    7 function: nhập giá trị, tính +, tính -, tính *, tính /, hiển thị kết quả, main
"""

"""
    Cách xác định các function: liệt kê cần thực hiện bao nhiêu chức năng
    => Có bấy nhiêu function, cộng thêm function main()
    => Đặt tên cho từng function
    => Xác định function cần đầu vào là gì (cần Parameter nào)
    => Xác định function cần đầu ra là gì (Có cần return hay không)
"""

# Hàm nhập
def nhap():
    a = int(input())
    return a

# Hàm tính +
def tinhTong(x, y):
    tong = x + y
    return tong
    
# Hàm tính -
def tinhHieu(a, b):
    hieu = a - b
    return hieu
    
# Hàm tính *
def tinhTich(a, b):
    tich = a * b
    return tich
    
# Hàm tính /
def tinhThuong(a, b):
    if(b != 0):
        thuong = a / b
        return thuong
    else:
        return "Khong chia duoc"
    
# Hàm hiển thị
def hienThi(tong, hieu, tich, thuong):
    print(f"a + b = {tong}")
    print(f"a - b = {hieu}")
    print(f"a * b = {tich}")
    print(f"a / b = {thuong}")
    
# Hàm main
def main():
    a = nhap()
    b = nhap()
    tong = tinhTong(a, b)
    hieu = tinhHieu(a, b)
    tich = tinhTich(a, b)
    thuong = tinhThuong(a, b)
    hienThi(tong, hieu, tich, thuong)
    
# Gọi hàm main
if __name__ == "__main__":
    main()