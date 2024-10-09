from math import*

class triangle:
    def __init__ (self,c1,c2,c3,mau):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.mau = mau
    def chuvi(self):
        return self.c1 + self.c2 + self.c3 
    def dientich(self):
        s = (self.c1 + self.c2 + self.c3) / 2 
        return sqrt(s * (s - self.c1) * (s - self.c2) * (s - self.c3))
        
    def thongtin(self):
        print(f"Day la hinh tam giac co canh lan luot la: {self.c1},{self.c2},{self.c3}")
        print("tam giac co mau:",self.mau)

    def type(self):
        a, b, c = self.c1, self.c2, self.c3
        # Kiểm tra tam giác đều
        if a == b == c:
            return "Tam giác đều"
        # Kiểm tra tam giác cân
        elif a == b or b == c or a == c:
            # Kiểm tra tam giác vuông cân
            if self.is_right_angle():
                return "Tam giác vuông cân"
            return "Tam giác cân"
        # Kiểm tra tam giác vuông
        elif self.is_right_angle():
            return "Tam giác vuông"
        else:
            return "Tam giác thường"

    # Phương thức kiểm tra tam giác có vuông không
    def is_right_angle(self):
        a, b, c = sorted([self.c1, self.c2, self.c3]) 
        return isclose(a**2 + b**2, c**2)
        

ht1 = triangle(3,4,5,"do")
ht1.thongtin()
print(ht1.type())