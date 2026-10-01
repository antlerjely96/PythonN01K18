"""
    Nhap thang la 1 so nguyen. Hien thi so ngay trong thang do
"""

# Khai báo tháng
thang = int(input("Nhập tháng: "))
# Kiểm tra thang
if thang <= 0 or thang > 12:
    print("Nhap sai")
elif thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    print(f"Thang {thang} co 31 ngay")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print(f"Thang {thang} co 30 ngay")
else:
    # Khai báo và nhập năm
    nam = int(input("Nhap nam: "))
    # Kiểm tra nam
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        print(f"Thang {thang} co 29 ngay")
    else:
        print(f"Thang {thang} co 28 ngay")
    