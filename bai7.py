class GiaoDich:
    def __init__(self, ma_gd, ngay_gd, don_gia, so_luong ):
        self.ma_gd = ma_gd
        self.ngay_gd = ngay_gd
        self.don_gia = don_gia
        self.so_luong = so_luong

    def thanh_tien(self):
        return self.so_luong * self.don_gia
    
class GiaoDichTienTe(GiaoDich):
    def __init__(self, ma_giao_dich, ngay_giao_dich, don_gia, so_luong, loai_tien, loai_giao_dich):
        super().__init__(ma_giao_dich, ngay_giao_dich, don_gia, so_luong)
        self.loai_tien = loai_tien
        self.loai_giao_dich = loai_giao_dich

    def thanh_tien(self):
        if self.loai_giao_dich == "mua":
            return self.so_luong * self.don_gia
        elif self.loai_giao_dich == "ban":
            return (self.so_luong * self.don_gia) * 1.05
        
class QuanLyGiaoDich:
    def __init__(self):
        self.danh_sach_giao_dich = []

    def them_giao_dich(self, giao_dich):
        self.danh_sach_giao_dich.append(giao_dich)

    def xuat_giao_dich(self):
        for gd in self.danh_sach_giao_dich:
            print(gd)

    def tong_so_luong(self, loai):
        tong = 0
        for gd in self.danh_sach_giao_dich:
            if isinstance(gd, GiaoDichTienTe) and gd.loai_tien == loai:
                tong += gd.so_luong
        return tong
        
    def tong_thanh_tien(self, loai):
        tong = 0
        for gd in self.danh_sach_giao_dich:
            if isinstance(gd, GiaoDichTienTe) and gd.loai_tien == loai:
                tong += gd.thanh_tien()
        return tong
    

ql_gd = QuanLyGiaoDich()

# Thêm các giao dịch
gd_vang = GiaoDich("GD001", "01/10/2024", 5500000, 10)
gd_tien_te1 = GiaoDichTienTe("GD002", "01/10/2024", 23000, 1000, "USD", "mua")
gd_tien_te2 = GiaoDichTienTe("GD003", "02/10/2024", 25000, 2000, "USD", "ban")

ql_gd.them_giao_dich(gd_vang)
ql_gd.them_giao_dich(gd_tien_te1)
ql_gd.them_giao_dich(gd_tien_te2)

# Xuất danh sách giao dịch
ql_gd.xuat_giao_dich()

# Tính tổng số lượng và tổng thành tiền
print(f"Tổng số lượng USD: {ql_gd.tong_so_luong('USD')}")
print(f"Tổng thành tiền USD: {ql_gd.tong_thanh_tien('USD')}")


    
    
