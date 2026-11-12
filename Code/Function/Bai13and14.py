"""
    13. Nhap so nguyen n tu ban phim
    Kiem tra n co phai so nguyen to hay khong
    14. Nhap so nguyen n tu ban phim
    Hien thi cac so nguyen to trong khoang tu 2 den n
"""

def nhap():
    n = int(input())
    return n

def kiemTraNguyenTo(n):
    if n < 2:
        return False
    else:
        count = 0
        for i in range(2, n):
            if n % i == 0:
                count += 1
        if count == 0:
            return True
        else:
            return False

def hienThiCacSoNguyenTo(n):
    for i in range(2, n):
        kiemTraNguyenTo(i)
        if kiemTraNguyenTo(i):
            print(f"{i}", end = "	")

def main():
    print("n = ", end = "")
    n = nhap()
    if kiemTraNguyenTo(n):
        print(f"{n} la so nguyen to")
    else:
        print(f"{n} khong la so nguyen to")
    hienThiCacSoNguyenTo(n)
    
if __name__ == "__main__":
    main()