n = int(input("số bài kiểm tra là: ")) #nhập số bài kiểm tra
diem_so = [2, 3,5, 5, 5, 6, 7,5, 8, 9, 9, 10] 
for index in range(n):# nhập số điểm 
     diem = float(input(f" nhập điểm cho bài kiểm tra thứ {index + 1}: ")) 
     diem_so.append(diem) 

# lập trình sắp xép điểm số theo chiều tăng dần (1, 2, ...)
def sap_xep_va_xoa_diem(diem_so):
     #sắp sép theo chiều tăng dần 
     diem_so.sort()
     # xoá điểmm số nhỏ nhất 
     while diem_so[0] == diem_so[1]: # kiểm tra nếu có 2 số nhỏ nhất 
          diem_so.remove(diem_so[0]) 
          diem_so.remove(diem_so[0]) 
     return diem_so 

# lập trình sử lí lớn hơn 8 
def diem_lon_hon_8(diem_so): 
     count = 0 
     for diem in diem_so: 
          if diem >= 8:
             coumt += 1 
     return count 

# gọi hàm và xuất ra danh sách sau khi xử lý 1 và 2 
sap_xep =  sap_xep_va_xoa_diem(diem_so) 
print(f"danh sách sau khi xử lý 1 và 2 là: {sap_xep}") 

# gọi hàm đếm số lượng diểm lớn hơn 8 
count = diem_lon_hon_8(diem_so) 
print(f"số lượng điểm hơn và băng 8 là: {count}") 




while True: 
   n = int(input("số nguyên dương là n: ")) 
   if n < 0:
       print("nhập lại số nguyên dương:  ") 
   elif n==0: 
       print("dừng trương trình ") 
       break 
   else: 
       tong = 0 
       for index in range(1, n + 1): 
           tong += index 
           print(f"tổng các số{n} là {tong}") 



 
     