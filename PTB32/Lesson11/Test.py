# # Nhập số lượng bài tập
# n = int(input("Nhập số nguyên dương n: "))
# if n <= 0:
#     print("Vui lòng nhập số nguyên dương!")
# else:
#     diem_bai_tap = []
#     for i in range(n):
#         diem = float(input(f"Nhập điểm cho bài tập {i+1}: "))
#         diem_bai_tap.append(diem)
#     print("Danh sách điểm các bài tập:", diem_bai_tap)
# #1
# diem_bai_tap.sort()
# print(f"Điểm bài tập sai khi được sắp xếp là:{diem_bai_tap}")
# # 2
# diem_be_nhat = diem_bai_tap[0]
# so_lan = diem_bai_tap.count(diem_be_nhat)
# for i in range(so_lan) :
#     diem_bai_tap.remove(diem_be_nhat)
# print(f"Điểm bài tập sau khi xóa đi điểm bé nhất là {diem_bai_tap}")
# #4
# count = 0
# for i in range(len(diem_bai_tap)) :
#     if diem_bai_tap[i] >= 8 :
#         count += 1
#     else :
#         count += 0
# print(f"Số bài tập điểm lớn hơn 8 là: {count}")
#
# n = int(input("Nhập số n: "))
# tong = 0
# i = 0
# # for i in range(n + 1) :
# #     tong += i
# # print(tong)
# while True :
#     if i < n :
#         i += 1
#         tong += i
#     else :
#         break
# print(tong)

#
products = [
    "Pphone_1",
    "Pphone_2",
    "Pphone_3",
    "Pphone_4",
    "Pphone_5",
    "Pphone_6",
    "Pphone_7",
    "Pphone_8",
    "Pphone_9",
    "Pphone_10"
]
giohang = []
while True :
    yeucau = int(input("Bạn muốn yêu cầu nào(1:Xem giỏ hàng,2:Thêm sản phẩm vào giỏ hàng,3:Xóa sản phẩm khỏi giỏ hàng,4:Thoát chương trình,5: Xem sản phẩm) : "))
    if yeucau == 1 :
        print(giohang)
        continue
    elif yeucau == 2 :
        them_san_pham = int(input("Bạn muốn thêm sản phẩm nào(ghi số 1,2,3,4,...) : "))
        giohang.append(products[them_san_pham - 1])
        continue
    elif yeucau == 3 :
        xoa_san_pham = int(input("Bạn muốn xóa sản phẩm số mấy: "))
        giohang.remove(xoa_san_pham)
        continue
    elif yeucau == 4 :
        break    
    elif yeucau == 5 :
        print(products)
        continue

# products = [
#     "Pphone_1",
#     "Pphone_2",
#     "Pphone_3",
#     "Pphone_4",
#     "Pphone_5",
#     "Pphone_6",
#     "Pphone_7",
#     "Pphone_8",
#     "Pphone_9",
#     "Pphone_10"
# ]
# giohang = []

# while True:
#     yeucau = int(input("Bạn muốn yêu cầu nào (1:Xem giỏ hàng, 2:Thêm sản phẩm, 3:Xóa sản phẩm, 4:Thoát, 5:Xem sản phẩm): "))

#     if yeucau == 1:
#         if not giohang:
#             print("Giỏ hàng trống!")
#         else:
#             print("--- Giỏ hàng của bạn ---")
#             for i, sp in enumerate(giohang, 1):
#                 print(f"{i}. {sp}")
#     elif yeucau == 2:
#         print("--- Danh sách sản phẩm ---")
#         for i, sp in enumerate(products, 1):
#             print(f"{i}. {sp}")
#         them_san_pham = int(input("Bạn muốn thêm sản phẩm số mấy: "))
#         giohang.append(products[them_san_pham - 1])
#         print(f"Đã thêm {products[them_san_pham - 1]} vào giỏ hàng!")
#     elif yeucau == 3:
#         if not giohang:
#             print("Giỏ hàng trống!")
#             continue
#         print("--- Giỏ hàng ---")
#         for i, sp in enumerate(giohang, 1):
#             print(f"{i}. {sp}")
#         xoa_san_pham = int(input("Bạn muốn xóa sản phẩm số mấy: "))
#         removed = giohang.pop(xoa_san_pham - 1)
#         print(f"Đã xoá {removed} khỏi giỏ hàng!")
#     elif yeucau == 4:
#         print("Thoát chương trình!")
#         break
#     elif yeucau == 5:
#         print("--- Danh sách sản phẩm ---")
#         for i, sp in enumerate(products, 1):
#             print(f"{i}. {sp}")
#     else:
#         print("Lựa chọn không hợp lệ!")
