"""
    17. Ve hinh
    *
    * *
    * * *
    * * * *
    * * * * *
    18. Ve hinh
    * * * * *
    * * * *
    * * *
    * *
    *
    19. Ve hinh
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
"""

def hienThiTamGiacXuoi():
    for i in range(5):
        for j in range(i + 1):
            print("*", end = " ")
        print()

def hienThiTamGiacNguoc():
    for i in range(5):
        for j in range(5 - i):
            print("*", end = " ")
        print()
        
def hienThiNguocVaXuoi():
    hienThiTamGiacXuoi()
    hienThiTamGiacNguoc()
    
def main():
    print("17.")
    hienThiTamGiacXuoi()
    print("18.")
    hienThiTamGiacNguoc()
    print("19.")
    hienThiNguocVaXuoi()

if __name__ == "__main__":
    main()