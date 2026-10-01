# Nhập 1 số nguyên x. Kiểm tra x là số dương hay số âm

# Khai báo và nhập x
x = int(input("x = "))
"""
    Kiểm tra x.
    Nếu x > 0 => Kiểm tra x. Nếu x % 2 == 0 => x la so chan, con lai x la so le
    Còn nếu x < 0 => x la so am
    Còn lại => x la so khong am khong duong
"""
# Kiểm tra x > 0. Nếu x > 0 True thì kiểm tra x % 2 == 0
# Lệnh print(f"{x} la so chan") được thực hiện khi x % 2 == 0 True
# Lệnh print(f"{x} la so le") được thực hiện khi x % 2 == 0 False
if x > 0:
    if x % 2 == 0:
        print(f"{x} la so chan")
    else:
        print(f"{x} la so le")
# Kiểm tra x > 0. Nếu x > 0 False thì kiểm tra x < 0
# Lệnh print(f"{x} la so am") được thực hiện khi x < 0 True
elif x < 0:
    print(f"{x} la so am")
# Lệnh print(f"{x} la so khong am khong duong") được thực hiện khi x > 0 False, x < 0 False
else:
    print(f"{x} la so khong am khong duong")
    