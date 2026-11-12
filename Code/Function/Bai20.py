"""
    20. Ve hinh
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
"""

def hienThi():
    for i in range(5):
        for j in range(i + 1):
            print(f"{j + 1}", end = " ")
        print()

def main():
    hienThi()

if __name__ == "__main__":
    main()