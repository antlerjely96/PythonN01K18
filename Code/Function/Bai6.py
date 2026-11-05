"""
    6. Nhập 3 số nguyên a, b, c. Tìm số nghiệm của phương trình a * x ** 2 + b * x + c = 0
"""

def nhap():
    a = int(input())
    return a

def timSoNghiem(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print(f"Phuong trinh {a} * x ** 2 + {b} * x + {c} = 0 co vo so nghiem")
            else:
                print(f"Phuong trinh {a} * x ** 2 + {b} * x + {c} = 0 vo nghiem")
        else:
            print(f"Phuong trinh {a} * x ** 2 + {b} * x + {c} = 0 co 1 nghiem")
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print(f"Phuong trinh {a} * x ** 2 + {b} * x + {c} = 0 vo nghiem")
        elif delta == 0:
            print(f"Phuong trinh {a} * x ** 2 + {b} * x + {c} = 0 co 1 nghiem")
        else:
            print(f"Phuong trinh {a} * x ** 2 + {b} * x + {c} = 0 co 2 nghiem")

def main():
    print("a = ", end = "")
    a = nhap()
    print("b = ", end = "")
    b = nhap()
    print("c = ", end = "")
    c = nhap()
    timSoNghiem(a, b, c)
    
if __name__ == "__main__":
    main()