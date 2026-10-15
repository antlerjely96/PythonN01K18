"""
    2. Nhap so nguyen n tu ban phim.
    Hien thi cac so tu 1 den n

"""
n = int(input("Nhập số nguyên n: "))
print(f"các số 1 đến {n} là:")
for i in range(1, n + 1):
    print(i, end=" ")