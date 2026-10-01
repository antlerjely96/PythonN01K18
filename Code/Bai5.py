"""
    Nhap 3 so nguyen x, y, z. Tính
        a. x + y + z
        b. x * y * z
        c. x^2 + y^2 - z^2
        d. x^3 / y^2 * z
        e. x / y / z
        f. (x + y) - (x + z) - (y + z)
        g. (x * y) / (x + y + z)
        h. (x + y + z) /3
"""

# Khai báo x, y, z
x = None
y = None
z = None
# Nhập x, y, z
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
# Tính
a = x + y + z
b = x * y * z
c = x ** 2 + y ** 2 - z ** 2
d = x ** 3 / y ** 2 * z
e = x / y / z
f = (x + y) - (x + z) - (y + z)
g = (x * y) / (x + y + z)
h = (x + y + z) /3
# Hiển thị
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")
print(f"e = {e}")
print(f"f = {f}")
print(f"g = {g}")
print(f"h = {h}")