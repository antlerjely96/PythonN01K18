"""
    Nhap 3 so nguyen a, b, c.
    Hien thi so lon nhat va so nho nhat trong 3 so
"""

# Khai báo và nhập a, b, c
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
# Kiểm tra
if a > b:
    if a > c:
        print(f"max = {a}")
    else:
        print(f"max = {c}")
elif a < b:
    if b > c:
        print(f"max = {b}")
    else:
        print(f"max = {c}")
else:
    if a > c:
        print(f"max = {a}")
    else:
        print(f"max = {c}")