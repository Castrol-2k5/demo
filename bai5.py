from math import*
class Hinh:
    def tinh_dien_tich(self):
        pass

    def tinh_chu_vi(self):
        pass

    def hien_thi(self):
        print("Day la class hinh hoc")

class Hinh_tron(Hinh):
    def __init__(self,ban_kinh):
        self.ban_kinh = ban_kinh

    def tinh_chu_vi(self):
        return 2 * 3.14 * self.ban_kinh
    def tinh_dien_tich(self):
        return 3.14 * ( self.ban_kinh**2 )
    
class Hinh_Chu_Nhat(Hinh):
    def __init__(self, dai, rong):
        self.dai  = dai
        self.rong = rong

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)
    
class Hinh_tam_giac(Hinh):
    def __init__ (self,c1,c2,c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
    
    def tinh_chu_vi(self):
        return self.c1 + self.c2 + self.c3
    
    def tinh_dien_tich(self):
        s = (self.c1 + self.c2 + self.c3) / 2 
        return sqrt(s * (s - self.c1) * (s - self.c2) * (s - self.c3))
    
tron = Hinh_tron(5)
print("Diện tích hình tròn:", tron.tinh_dien_tich())
print("Chu vi hình tròn:", tron.tinh_chu_vi())

tam_giac = Hinh_tam_giac(3, 4, 5)
print("Diện tích tam giác:", tam_giac.tinh_dien_tich())
print("Chu vi tam giác:", tam_giac.tinh_chu_vi())

hcn = Hinh_Chu_Nhat(4, 7)
print("Diện tích hình chữ nhật:", hcn.tinh_dien_tich())
print("Chu vi hình chữ nhật:", hcn.tinh_chu_vi())


        
        