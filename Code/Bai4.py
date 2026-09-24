# Nhập 2 số thực từ bàn phím. Tính +, -, *, / của 2 biến

# Khai báo 2 biến
a = None
b = None
# Nhập 2 biến
a = float(input("Nhap so thuc thu nhat: "))
b = float(input("Nhap so thuc thu hai: "))
# Tính +
tong = a + b
# Tính -
hieu = a - b
# Tính *
tich = a * b
# Tính /
thuong = a / b
# Hiển thị kết quả
print(f"a + b = {tong}")
print(f"a - b = {hieu}")
print(f"a * b = {tich}")
print(f"a / b = {thuong}")