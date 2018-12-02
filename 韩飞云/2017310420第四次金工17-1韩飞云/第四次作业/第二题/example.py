from restaurant import Restaurant
from ice_cream_stand import IceCreamStand
#打印餐馆实例
my_restaurant = Restaurant('HFY','Chinese')
my_restaurant.set_number_served()
print('\n')

#打印冰淇淋小店的实例
one_shop = IceCreamStand('No.1','England')
two_shop = IceCreamStand('No.2','American')
#设置两个冰淇淋小店的冰淇淋口味
one_shop.flavors = ["chocolate","watermelon","apple"]
two_shop.flavors = ["strawberry","pear","bread","banana"]

print("餐馆的名字是：" + one_shop.restaurant_name)
print(one_shop.show_flavors())
print('\n')
print("餐馆的名字是：" + two_shop.restaurant_name)
print(two_shop.show_flavors())

