#restaurant模块
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):#输出名字和菜品的方法
        print("The restaurant's name is "+ self.restaurant_name)
        print("The restaurant's cuisine type is "+ self.cuisine_type)

    def open_restaurant(self):#输出餐厅正在营业消息的方法
        print("The restaurant is opening.")

    def set_number_served(self,number_served):#输出就餐人数的方法
        self.number_served = number_served

    def increment_number_served(self,number_served):#输出餐厅已经接待的就餐人数的方法
        self.number_served = self.number_served + number_served

class IceCreamStand(Restaurant):#继承Restaurant的类
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=[]

    def set_flavors(self,flavors):#设置冰淇淋口味的方法
        self.flavors=flavors
        
    def describe_icecream(self):#显示冰淇淋口味的方法
        print("The flavors of ice cream are:")
        for flavor in self.flavors:
            print(flavor)
