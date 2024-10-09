
class HocVien:
    def __init__(self,cccd,Hoten,namsinh):
        self.cccd = cccd
        self.Hoten = Hoten
        self.namsinh = namsinh
        self.danh_sach_mon_hoc = []
        
    def XuatThongTin(self):
        print("Số căn cước công dân: " + self.cccd)
        print("Họ và tên: " + self.Hoten)
        print("Năm sinh: " + self.namsinh)
        print("Các môn đã đăng ký:")
        for monhoc in self.danh_sach_mon_hoc:
            print(f" - Mã môn: {monhoc.Mamon}, Tên môn: {monhoc.tenMon}, Số tiết: {monhoc.sotiet}")
            
   
    
    def dang_ky_mon_hoc(self,monhoc):
        self.danh_sach_mon_hoc.append(monhoc)   
    
class MonHoc:
    def __init__(self,Mamon,tenMon,sotiet):
        self.Mamon = Mamon
        self.tenMon = tenMon
        self.sotiet = sotiet
        
        
class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sv = []
        
    def NhapThongTin(self):
        so_luong_sv = int(input("Nhập số lượng sinh viên cần nhập thông tin: "))
        for _ in range(so_luong_sv):
            cccd = input("nhập căn cước công dân : ")
            Hoten = input("nhập họ và tên sinh viên : ")
            namsinh = input("nhập năm sinh : ")
            
            sinhvien = HocVien(cccd,Hoten,namsinh)
            
            n = int(input("só môn mà sinh viên đăng ký : "))
            for i in range(n):
                Mamon = input("nhập mã môn : ")
                tenMon = input("nhập tên môn học : ")
                sotiet = int(input("nhập số tiết : "))
                
                monhoc = MonHoc(Mamon,tenMon,sotiet)
                sinhvien.dang_ky_mon_hoc(monhoc)
            
            self.danh_sach_sv.append(sinhvien)
    def XuatDanhSachSV(self):
        for sv in self.danh_sach_sv:
            sv.XuatThongTin()
    
    def LuuDanhSachVaoFile(self, file_name="dssv.txt"):
    # Ghi danh sách sinh viên vào tập tin
        with open(file_name, "w", encoding="utf-8") as file:
            if not self.danh_sach_sv:
                file.write("Danh sách sinh viên hiện đang trống.\n")
            else:
                for sv in self.danh_sach_sv:
                    file.write(f"Số căn cước công dân: {sv.cccd}\n")
                    file.write(f"Họ và tên: {sv.Hoten}\n")
                    file.write(f"Năm sinh: {sv.namsinh}\n")
                    file.write("Các môn đã đăng ký:\n")
                    for monhoc in sv.danh_sach_mon_hoc:
                        file.write(f" - Mã môn: {monhoc.Mamon}, Tên môn: {monhoc.tenMon}, Số tiết: {monhoc.sotiet}\n")
                    file.write('-' * 50 + "\n")  
   
    def hien_thi_hoc_vien_it_nhat_hai_mon(self):
        """Hiển thị thông tin học viên đăng ký ít nhất hai môn học"""
        print("Danh sách học viên đăng ký ít nhất hai môn học:")
        for sv in self.danh_sach_sv:
            if len(sv.danh_sach_mon_hoc) >= 2:
                sv.XuatThongTin()
    
    def mon_hoc_duoc_dang_ki_nhieu_nhat(self):
        thong_ke = {}
        for sv in self.danh_sach_sv:
            for monhoc in sv.danh_sach_mon_hoc:
                if monhoc.tenMon not in thong_ke:
                    thong_ke[monhoc.tenMon] = 0
                thong_ke[monhoc.tenMon] += 1
        # Tìm môn học có số lượng học viên đăng ký nhiều nhất
        mon_hoc_nhieu_nhat = max(thong_ke, key=thong_ke.get)
        so_hoc_vien = thong_ke[mon_hoc_nhieu_nhat]
        print(f"Môn học có nhiều học viên đăng ký nhất: {mon_hoc_nhieu_nhat} ({so_hoc_vien} học viên)")
        
    def thong_ke_so_luong_hoc_vien_tren_mon_hoc(self):
        """Thống kê số lượng học viên trên mỗi môn học"""
        thong_ke_mon_hoc = {}
        for sv in self.danh_sach_sv:
            for monhoc in sv.danh_sach_mon_hoc:
                if monhoc.tenMon not in thong_ke_mon_hoc:
                    thong_ke_mon_hoc[monhoc.tenMon] = 0
                thong_ke_mon_hoc[monhoc.tenMon] += 1

        print("Thống kê số lượng học viên trên mỗi môn học:")
        for mon, so_luong in thong_ke_mon_hoc.items():  
            print(f"{mon}: {so_luong} học viên")
            
qlsv = QuanLySinhVien()
qlsv.NhapThongTin()
qlsv.XuatDanhSachSV()  
qlsv.LuuDanhSachVaoFile("dssv.txt")
qlsv.hien_thi_hoc_vien_it_nhat_hai_mon()
qlsv.mon_hoc_duoc_dang_ki_nhieu_nhat()
qlsv.thong_ke_so_luong_hoc_vien_tren_mon_hoc()


