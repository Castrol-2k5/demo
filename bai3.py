class toan_hoc:
    def __init__(self,*nso):
        self.nso = nso


    def tinh_tong(self):
        a = list(self.nso)
        sum = 0
        for i in range(len(a)):
            sum += a[i]
        return sum
    
    def tinh_trung_binh(self):
        a = list(self.nso)
        sum = 0
        for i in range(len(a)):
            sum += a[i]
        tbc = sum / len(a)
        return tbc
    
    def tim_max(self):
        a = list(self.nso)
        lon_nhat = max(a)
        return lon_nhat
    
    def tim_min(self):
        a = list(self.nso)
        nho_nhat = min(a)
        return nho_nhat
    
    def HienThi(self):
        a = list(self.nso)
        for i in range(len(a)):
            print(a[i],end = " ")

        print()
        print(self.tinh_tong())
        print(self.tinh_trung_binh())
        print(self.tim_max())
        print(self.tim_min())
       
    
        

so = toan_hoc(1,2,3,4,5)
so.HienThi()

    


        
        