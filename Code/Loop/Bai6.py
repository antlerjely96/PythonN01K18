"""
    6. Nhap so nguyen n tu ban phim.
    Tinh tong cac chu so cua n
"""

n = int(input("n = "))
m = n
tong = 0
while m > 0:
    tong = tong + m % 10
    m = m // 10
print(f"Tổng các chữ số của {n}: {tong}")