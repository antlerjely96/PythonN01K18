"""
    7. Nhap so nguyen n tu ban phim
    Kiem tra n co phai so nguyen to hay khong
"""
# Khai báo và nhập n
n = int(input("n = "))
# Khai báo đếm để đếm số lượng số trong khoảng từ 2 đến n - 1 là ước của n
dem = 0;
# Kiểm tra n <= 1
if n <= 1:
    print(f"{n} khong la so nguyen to")
else:
    # Chạy vòng lặp i từ 2 => n - 1
    for i in range(2, n):
        # Kiểm tra n có chia hết cho số nào trong khoảng từ 2 => n - 1 không
        if n % i == 0:
            dem += 1
    # Kiểm tra đếm: nếu đếm vẫn bằng 0 => n không chia hết cho số nào
    if dem == 0:
        print(f"{n} la so nguyen to")
    else:
        print(f"{n} khong la so nguyen to")
        
