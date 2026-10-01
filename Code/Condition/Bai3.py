"""
    Nhap diem trung binh cua 1 hoc sinh.
    Neu diem >= 0 && diem < 5 => Yeu
    Neu diem >= 5 && diem < 6.5 => trung binh
    Neu diem >= 6.5 && diem < 8 => Kha
    Con lai => gioi
"""

# Khai báo và nhập điểm
diem = float(input("Nhap diem: "))
# Kiểm tra điểm
if diem < 0 or diem > 10:
    print("Nhap sai")
elif diem < 5:
    print("Yeu")
elif diem < 6.5:
    print("Trung binh")
elif diem < 8:
    print("Kha")
else:
    print("Gioi")