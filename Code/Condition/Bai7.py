"""
    Nhập 1 số nguyên là thứ trong tuần. Hiển thị tên của thứ đó
"""
# Khai báo và nhập thứ
thu = int(input("Nhập thứ: "))
# Lựa chọn
match thu:
    case 2:
        print("Thứ Hai")
    case 3:
        print("Thứ Ba")
    case 4:
        print("Thứ Tư")
    case 5:
        print("Thứ Năm")
    case 6:
        print("Thứ Sáu")
    case 7:
        print("Thứ Bảy")
    case 8:
        print("Chủ nhật")
    case _:
        print("Thứ không tồn tại")