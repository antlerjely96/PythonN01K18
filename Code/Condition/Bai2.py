"""
    Nhap so tuoi cua 1 nguoi tu ban phim (tuoi la so nguyen)
    Kiem tra:
        Neu tuoi > 0 and tuoi < 6: hoc mau giao
        Neu tuoi >= 6 and tuoi < 11: hoc cap 1
        Neu tuoi >= 11 and tuoi < 16: hoc cap 2
        Neu tuoi >= 16 and tuoi < 18: hoc cap 3
        Neu tuoi >= 18 and tuoi < 23: Hoc dai hoc
        Neu tuoi >= 23 and tuoi <= 65: Di lam
        Con lai: Nghi huu
"""

# Khai báo và nhập tuổi
tuoi = int(input("Nhap tuoi: "))
# Kiểm tra tuổi
if tuoi <= 0:
    print("Nhap sai!")
elif tuoi < 6:
    print("hoc mau giao")
elif tuoi < 11:
    print("hoc cap 1")
elif tuoi < 16:
    print("hoc cap 2")
elif tuoi < 18:
    print("hoc cap 3")
elif tuoi < 23:
    print("hoc cao dang hoac dai hoc")
elif tuoi <= 65:
    print("Di lam")
else:
    print("Nghi huu")