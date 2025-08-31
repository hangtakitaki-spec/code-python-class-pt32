Listsp = ["P1","P2","P3","P4","P5","P6"] # tên các sản phẩm 
product = ["apple","samsung","lenovo"] 
shoppinglist = []

# hiển thị sản phẩm 
def product_list(product): 
    #hiển thị sản phẩm 
    for index in range(len(product)): 
         print(f"{index + 1}: {product[index]}") 

product_list(product) 

# xem giỏ hàng 
def shopping(shopping_list): 
     #khi dỏ hàng rỗng 
     if not shopping_list: # nếu dỏ hàng rỗng 
          print("hết hàng") 
     else: 
          print(f"mặt hàng của bạn là : {shoppinglist} ") 
          for index in range(len(shoppinglist)): 
               print(f"{index + 1}: {shoppinglist[index]}") 
#họi hàm shopping để xem giỏ hàng 
shopping(shoppinglist) 
# chọn sản phẩm  
def add_shopping_list(product,shopping_list): 
     print("danh sách sản phẩm là: ")
     product_list(product) # gọi hàm product_list(product) dể hiển thị sản phẩm 
     # tạo biến số lưu trữ vị trí sản phẩm 
     item_index = int(input("nhập sản phẩm bạn muốn thêm vào: "))
     if item_index >= 0 and item_index(len(product)): 
           selected_item = product(item_index) # tạo biến số lưu trữ sản phẩm đã chọn 
           shopping_list.append(selected_item) 
           print(f"{selected_item} dã thêm vào giỏ hàng của bạn ")
     else: 
        print("không hợp lệ ") 

# gọi lại add_shopping_list(product,shopping_list) 
add_shopping_list(product,shopping_list)


# 4. xoá sản phẩm ra khỏi giỏ hàng 
def remove_item(shopping_list): 
     if not shopping_list: 
         print("giỏ hàng của bạn đang trống ")
     else: 
          print("các sản phẩm có trong giỏ  hàng là:")
