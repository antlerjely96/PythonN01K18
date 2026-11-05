"""
    7. Nhap 3 so thuc tu ban phim. Kiem tra 3 so do co phai canh cua 1 tam giac hay khong
"""

def nhap():
    a = float(input())
    return a

def kiemTraTamGiac(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            print(f"{a}, {b}, {c} la 3 canh tam giac")
        else:
            print(f"{a}, {b}, {c} khong la 3 canh tam giac")
    else:
        print(f"{a}, {b}, {c} la 3 canh tam giac")

def main():
    print("a = ", end = "")
    a = nhap()
    print("b = ", end = "")
    b = nhap()
    print("c = ", end = "")
    c = nhap
    kiemTraTamGiac(a, b, c)

if __name__ = "__main__":
    main()