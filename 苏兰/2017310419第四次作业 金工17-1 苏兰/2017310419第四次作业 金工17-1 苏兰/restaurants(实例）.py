"""导入restaurant模块"""
from restaurant import Restaurant,IceCreamStand

"""创建Restaurant实例并打印目前服务的人数"""
restaurant_1=Restaurant("greatpizza","pizza")
restaurant_1.set_number_served(81)
restaurant_1.read_number_served()
print("\n")

"""创建两个IceCreamStand类的实例，打印每个冰激凌店的名字和所提供的冰激凌的口味"""
IceCream1=IceCreamStand("ice-cream_land","icecream",['strawberry','yogurt','cheese','milk'])
IceCream1.describe_restaurant()
IceCream1.show_flavors()
IceCream2=IceCreamStand("best_ice-cream","icecream",['chocolate','strawberry','milk'])
IceCream2.describe_restaurant()
IceCream2.show_flavors()
