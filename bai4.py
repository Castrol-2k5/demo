from math import*
class Diem:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y 
        self.color = color

    def hien_thi(self):
        print(f"diem co toa do:{self.x},{self.y} va co mau: {self.color}")

    def tinh_tien_hoanh(self,x_hoanh):
        # ham tinh tien theo truc hoanh
        self.x += x_hoanh

    def tinh_tien_2_huong(self,x_hoanh,y_tung):
        # ham tinh tien theo 2 truc 0x,0y
        self.x += x_hoanh
        self.y += y_tung

    def khoang_cach_voi_goc(self):
        #Hàm tính khoảng cách từ điểm đến gốc tọa độ O(0, 0)
        return sqrt(self.x**2 + self.y**2)
    
    def khoang_cach_voi_diem(self,x_diem,y_diem):
        #Hàm tính khoảng cách từ điểm bat ky
        return sqrt((self.x - x_diem)**2 + (self.y - y_diem)**2)
    

diem1 = Diem(3, 4, "Đỏ")
diem1.hien_thi()  

# Tịnh tiến điểm theo trục hoành
diem1.tinh_tien_hoanh(2)
diem1.hien_thi()

# Tịnh tiến điểm theo cả hai trục Ox và Oy
diem1.tinh_tien_2_huong(1, -3)
diem1.hien_thi()  

# Tính khoảng cách từ điểm đến gốc tọa độ
khoang_cach_goc = diem1.khoang_cach_voi_goc()
print(f"Khoảng cách từ điểm đến gốc tọa độ: {khoang_cach_goc}")

# Tính khoảng cách giữa hai điểm
khoang_cach_diem = diem1.khoang_cach_voi_diem(5,6)
print(f"Khoảng cách giữa hai điểm: {khoang_cach_diem}")
            