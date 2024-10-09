from math import pi

class circle:
    def __init__ (self,ban_kinh):
        self.ban_kinh = ban_kinh
    def chuvi(self):
        return 2*pi*self.ban_kinh
    def dientich(self):
        return pi * self.ban_kinh * self.ban_kinh
    
    def thongtin(self):
        print(f"Day la hinh tron co ban kinh: {self.ban_kinh}")


ht1 = circle(5)
print(ht1.chuvi())
print(ht1.dientich())
print(ht1.thongtin())
