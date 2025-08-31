print('''
   Tạo 1 chương trình "Shopping Phone"
      1. Tạo ra danh sách sản phẩm
      2. Xem giỏ hàng
      3. Thêm sản phẩm vào giỏ hàng
      4. Xoá sản phẩm ra khỏi giỏ hàng 
      5. Thoát chương trình 
''')
products = [
    "0.Sữa tươi",
    "1.Bánh mì",
    "2.Mì gói",
    "3.Nước ngọt",
    "4.Gạo",
    "5.Dầu ăn",
    "6.Đường",
    "7.Muối",
    "8.Trứng gà",
    "9.Thịt heo",
    "10.Rau xanh",
    "11.Nước mắm",
    "12.Bánh kẹo",
    "13.Kem đánh răng",
    "14.Xà phòng",
    "15.Nước rửa chén"
]

def xem_gio_hang(dohang):
        print(dohang)

def san_pham(products):
    print(products)
dohang = []
print(products)
while True:
    nhap = int(input("nhap lua chon:"))
    if nhap == 1:
        san_pham(products)
        continue
    if nhap ==2:
        xem_gio_hang(dohang)
        continue
    if nhap ==3:
         item = int(input("nhap so thu tu cua do:"))
         print(f"ban da them {products[item]}")
         dohang.append(products[item])
    if nhap ==4:
         so = input("nhap san pham can xoa:")
         if so in dohang:
              dohang.remove(so)
    if nhap == 5:
         break
    