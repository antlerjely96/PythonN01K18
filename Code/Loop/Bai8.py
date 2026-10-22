"""
    8. Nhap so nguyen n tu ban phim
    Hien thi cac so nguyen to trong khoang tu 2 den n
"""
n = int(input("Nhap n: "))

print(f"Cac so nguyen to tu 2 den {n} la:")

for i in range(2, n + 1):
    dem = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dem += 1
            
    if dem == 2:
        print(i, end = " ")