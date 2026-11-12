"""
    11. Nhap so nguyen n tu ban phim.
    Tinh tong cac so chia het cho 3 hoac 7 trong khoang tu 1 den n
"""

def nhap():
    n = int(input())
    return n

def tinhTongCacSoChiaHetCho3Hoac7(n):
    tong = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 7 == 0:
            tong += i
    print(f"Tong cac so chia het cho 3 hoac 7 trong khoang tu 1 den n: {tong}")

def main():
    print("n = ", end = "")
    n = nhap()
    tinhTongCacSoChiaHetCho3Hoac7(n)
    
if __name__ == "__main__":
    main()