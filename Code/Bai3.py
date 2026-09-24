# Nhập 2 số nguyên từ bàn phím. Tính +, -, *, /, %, //, ** của 2 biến

# Khai báo 2 biến
a = None
b = None
# Nhập 2 biến
a = int(input("Nhap so nguyen thu nhat: "))
b = int(input("Nhap so nguyen thu hai: "))
# Tính +
tong = a + b
# Tính -
hieu = a - b
# Tính *
tich = a * b
# Tính /
thuong = a / b
# Tính %
so_du = a % b
# Tính //
phan_nguyen = a // b
# Tính **
luy_thua = a ** b
# Hiển thị kết quả
# Chỉ có thể dùng str + str, không thể dùng str + int
print("a + b = " + str(tong))
print(f"a - b = {hieu}") # Ưu tiên dùng cách này
print("a * b = ", tich)
print(f"a / b = {thuong}")
print(f"a % b = {so_du}")
print(f"a // b = {phan_nguyen}")
print(f"a ** b = {luy_thua}")