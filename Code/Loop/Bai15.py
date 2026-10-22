"""
    Nhập số nguyên n từ bàn phím
    1. Khi gặp giá trị đầu tiên trong khoảng từ 1 đến n mà giá trị đó chia hết cho 3 thì dừng lại
    2. Chạy vòng lặp in ra các số từ 1 đến n, không in ra các số chia hết cho 5
"""
n = int(input("n = "))

for i in range(1, n):
    if(i % 3 == 0):
        break
    print(i, end = "  ")
print()
    
for i in range(1, n):
    if(i % 5 == 0):
        continue
    print(i, end = "  ")