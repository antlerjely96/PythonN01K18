"""
    10. Nhap so nguyen n tu ban phim.
    Tinh n!
"""

def nhap():
    n = int(input())
    return n

def tinhGiaiThua(n):
    if n < 0:
        return "Khong ton tai"
    elif n == 0:
        return 1
    else:
        giaiThua = 1
        for i in range(1, n + 1):
            giaiThua *= i
        return giaiThua

# Nâng cao (tính bằng đệ quy)
def tinhGiaiThuaRecursion(n):
    if n == 1:
        return 1
    else:
        return n * tinhGiaiThuaRecurion(n - 1)
    
def main():
    print("n = ", end = "")
    n = nhap()
    print(f"n! = {tinhGiaiThua(n)}")
    print(f"n! = {tinhGiaiThua(n)}")
    
if __name__ == "__main__":
    main()