from restaurant import Restaurant
from ice_cream_stand import IceCreamStand
#分别导入饭店和冰淇淋站两个类
restaurant1=Restaurant("Noodles lover","noodles")
#建立饭店实例restaurant1
restaurant1.set_number_served(50)
#调用函数设置就餐人数
print("饭店目前的就餐人数为："+str(restaurant1.number_served))
#打印就餐人数

ice1=IceCreamStand("DQ","ice cream",["milk","chocolate","banana"])
ice1.describe_restaurant()
ice1.show_flavors()

ice2=IceCreamStand("Ice Man","ice cream",["coffee","chocolate","banana"])
ice2.describe_restaurant()
ice2.show_flavors()
