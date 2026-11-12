"""
    8. Nhap so nguyen n tu ban phim.
    Hien thi cac so tu 1 den n
"""

def nhap():
    n = int(input())
    return n

def hienThi(n):
    for i in range(1, n):
        print(i)

def main():
    print("n = ", end = "")
    n = nhap()
    hienThi(n)
    
if __name__ == "__main__":
    main()
    