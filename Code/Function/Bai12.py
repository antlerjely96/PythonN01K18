"""
    12. Nhap so nguyen n tu ban phim.
    Tinh tong cac chu so cua n
"""

def nhap():
    n = int(input())
    return n

def tinhTongCacChuSo(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n = n // 10
    return tong

def main():
    print("n = ", end = "")
    n = nhap()
    print(f"Tong cac chu so cua n: {tinhTongCacChuSo(n)}")
    
if __name__ == "__main__":
    main()