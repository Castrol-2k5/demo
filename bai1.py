price = input("Nhap don gia: ")
size = input("Nhap so luong: ")
bef = int(price) * int(size)
thue = bef / 10
aft = bef + thue
print('{0:>26} {1:>15}' .format("Tong tien truoc thue: ", str(price) + '*' + str(size) + '=' + str(bef)))
print('{0:>26} {1:>15}' .format("Tien thue: ", thue))
print('{0:>26} {1:>15}' .format("Tong tien sau thue: ", aft))