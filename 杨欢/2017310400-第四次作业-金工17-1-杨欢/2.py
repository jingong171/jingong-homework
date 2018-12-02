from restaurant import *
from icecreamstand import IceCreamStand

myRestaurant=Restaurant("KFC","chinese food")
##创建饭店类
myRestaurant.set_number_served(20)
##设定就餐人数
print(myRestaurant.restaurant_name.title()+" is serving "+str(myRestaurant.number_served)+" people.")

myFlavors1=['chocolate','blueberry','banana']
##创建口味列表
myStand1=IceCreamStand("delicacy","dessert",myFlavors1)
##创建第一个冰淇淋站
print("This ice cream stand's name is " + myStand1.restaurant_name.title())
myStand1.describe_IceCream()

myFlavors2=['lemon','strawberry','milk']
##创建口味列表
myStand2=IceCreamStand("Hello dessert","dessert",myFlavors2)
##创建第一个冰淇淋站
print("This ice cream stand's name is "+ myStand2.restaurant_name.title())
myStand2.describe_IceCream()
