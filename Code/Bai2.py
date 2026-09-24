# Nhập thông tin cá nhân từ bàn phím, hiển thị thông tin cá nhân vừa nhập

"""
    Nhập thông tin cá nhân bao gồm:
        - Họ tên
        - Ngày sinh
        - Địa chỉ
        - Số điện thoại
        - Email
"""

# Khai báo biến
ho_ten = None
ngay_sinh = None
dia_chi = None
so_dien_thoai = None
email = None
# Nhập thông tin
ho_ten = input()
ngay_sinh = input()
dia_chi = input()
so_dien_thoai = input()
email = input()
# Hiển thị thông tin
print("Họ tên: " + ho_ten)
print("Ngày sinh: " + ngay_sinh)
print("Địa chỉ: " + dia_chi)
print("Số điện thoại: " + so_dien_thoai)
print("Email: " + email)
# Chỉ có thể dùng str + str