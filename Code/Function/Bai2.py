"""
    2. Nhập 1 số nguyên x. Kiểm tra x là số dương hay số âm
"""

def kiem_tra(x):
    if x > 0:
       print("x la so duong")
    elif x < 0:
       print("x la so am")
    else:
       print("x la bang 0")
    
def main():
    x = int(input("Nhap x: "))
    kiem_tra(x)

if __name__ == "__main__":
    main()