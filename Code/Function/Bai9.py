"""
    9. Nhap so nguyen n tu ban phim.
    Hien thi cac so chan trong khoang tu 1 den n
"""

def nhap():
    n = int(input())
    return n

def hienThi(n):
    for i in range(1, n):
        if i % 2 == 0:
            print(i)

def main():
    print("n = ", end = "")
    n = nhap()
    hienThi(n)
    
if __name__ == "__main__":
    main()