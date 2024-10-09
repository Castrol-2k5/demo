# OOP quản lý nhân viên
""" 1 ngày có:
Ca 01: Sáng (Đăng kí làm bao nhiêu giờ trong buổi sáng)
Ca 02: Trưa
Ca 03: Chiều
Ca 04: Đêm
"""
luong_coban = 2340
class Nhanvien:
    def __init__(self, maso, hoten, ngaysinh, dk_giolam,xeploai, phucap, bap):
        self.maso = maso
        self.hoten = hoten
        self.ngaysinh = ngaysinh
        self.dk_giolam = dk_giolam
        self.xeploai = xeploai
        self.phucap = phucap
        self.bap = bap
    def so_luong(self):
        return luong_coban*self.bap + self.phucap
    def Hienthi_TT(self):
        print(f"  Mã số: {self.maso}")
        print(f"  Họ tên: {self.hoten}")
        print(f"  Ngày sinh: {self.ngaysinh}")
        print("  Danh sách giờ làm: ")
        for hour in self.dk_giolam:
            print(f"   - Ca số: {hour['ca_so']}, Số giờ làm: {hour['gio_lam']} giờ")
        print(f"  Xếp loại đánh giá: {self.xeploai} ")
        print(f"  Phụ cấp: {self.phucap}")
        print(f"  Bậc lương: {self.bap}" )
        print(f"  Tổng số lương: {self.so_luong()} nghìn đồng")

def Nhap_TT(list_nv = []):
    n = int(input("Nhập số lượng nhân viên: "))
    for i in range(n):
        maso = input("Nhập mã số nhân viên: ")
        hoten = input("Nhập họ tên nhân viên: ")
        ngaysinh = input("Nhập ngày sinh nhân viên: ")
        m = int(input("Nhập số ngày đã đăng ký ca làm: "))
        dk_giolam = []
        for j in range(m):
            print(f"Ngày thứ {j+1}:")
            ca_so = input("Nhập ca đã làm: ")
            gio_lam = input(" Nhập số giờ đã làm: ")
            dk_giolam.append({"ca_so": ca_so,"gio_lam": gio_lam})
        xeploai = input("Nhập xếp loại nhân viên (Tốt/Khá/Yếu): ")
        if xeploai == "Tốt":
            phucap = 3000
        elif xeploai == "Khá":
            phucap = 1500
        else:
            phucap = 0
        bap = float(input("Nhập bậc lương: "))
        nhanvien = Nhanvien(maso, hoten, ngaysinh, dk_giolam, xeploai, phucap, bap)
        list_nv.append(nhanvien)
    return list_nv
def Xuat_TT(list_nv):
    index = 1
    if not list_nv:
        print("Ko có dữ liệu !")
    for nv in list_nv:
        print('*'*20)
        print(f'Nhân viên thứ {index}')
        nv.Hienthi_TT()
        index += 1
def Tong_soluong(list_nv):
    tong_tien = 0
    for a in list_nv:
        if isinstance(a,Nhanvien):
            tong_tien += a.so_luong()
    return tong_tien
def Thongke_calam(list_nv):
    count_tk = {}
    for staff in list_nv:
        for h in staff.dk_giolam:
            ca_so = h['ca_so']
            if ca_so in count_tk:
                count_tk[ca_so]['count'] += 1
            else:
                count_tk[ca_so] = {'count': 1}
    if count_tk:
        print("{:^40}".format("Thống kê số lượng đăng kí ca làm")) 
        print('-'*40)
        for ca_so, value in count_tk.items():
            print(f" Ca số {ca_so}: {value['count']} lượt.")
def Nv_tichcucnhat(list_nv):
    count_nv = {}
    max_sc = 0
    for nv in list_nv:
        if len(nv.dk_giolam) > max_sc: 
            max_sc = len(nv.dk_giolam)
    print("{:^40}".format("Nhân viên tích cực nhất")) #căn lề giữa
    print('-'*40)
    for k in list_nv:
        if len(k.dk_giolam) == max_sc:
            k.Hienthi_TT()

def menu():
    list_nv = []
    while(True):
        print('*'*40)
        print("{:^40}".format("Quản lý nhân viên")) 
        print('-'*40)
        print('1. Nhập thông tin nhân viên. ')
        print('2. Hiển thị thông tin nhân viên.')
        print('3. Thống kê số lượng đăng ký ca làm.')
        print('4. Hiển thị thông tin Nhân viên tích cục làm việc nhất.')
        print('5. Tổng số tiền phải trả cho nhân viên.')
        print('z. Thoát chương trình.')
        choose = input('Chọn chức năng: ')
        print('-'*40)
        if choose == '1':
            list_nv = Nhap_TT(list_nv)
        elif  choose == '2':
            Xuat_TT(list_nv)
        elif  choose == '3':
            Thongke_calam(list_nv)
        elif  choose == '4':
            Nv_tichcucnhat(list_nv)
        elif  choose == '5':
            tong_tien = Tong_soluong(list_nv)
            print(f" Tống số tiền lương phải trả cho nhân viên: {tong_tien} nghìn đồng")
        elif  choose == 'z':
            print(" Kết thúc chương trình")
            break
        else:
            print(" Lực chọn chức năng ko đúng ! Vui lòng chọn lại.")
menu()