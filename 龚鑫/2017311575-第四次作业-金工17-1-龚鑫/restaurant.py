"""该模块中包含一个名为Restaurant的类及一个继承于Restaurant的IceCreamStand类"""
class Restaurant():
    """该类中包含餐馆名字，提供菜品，就餐人次三个属性，同时还包含用于输出就餐人数,
       用于递增就餐人数，用于打印餐馆信息，用于打印营业状态的四个方法"""
    def __init__(self,restaurant_name,*cuisine_type): #通过用户输入的参数进行类的初始化
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0 #默认就餐人次为0

    def describe_restaurant(self): #打印出该饭店的名称
        print("The restaurant's name is "+self.restaurant_name+".")

    def decrcibe_cuisine_type(self): #打印出该饭店的菜谱
        print("The restaurant's cuisine type includes",end=" ")
        for i in self.cuisine_type:
            print(i,end=" ")
        print(".")

    def open_restaurant(self): #打印出该饭店正在营业的信息
        print("The "+self.restaurant_name+" is open.")

    def set_number_served(self,number_served): #打印出该饭店的就餐人次
        self.number_served=number_served
        print("The restaurant is serving for "+str(self.number_served)+" persons.")

    def increment_number_served(increment_number): #增加饭店就餐人次
        if increment_number>0: #判断增加人数是否为正
            print("The number should be positive.")
        else:
            self.number_served+=increment_number


class IceCreamStand(Restaurant):
    """该类中除了包含Restaurant中的信息外，还增加了口味属性和打印出提供口味的函数"""
    def __init__(self,restaurant_name,flavors,*cuisine_type):
        super().__init__(restaurant_name,*cuisine_type)
        self.flavors=flavors

    def describe_restaurant(self): #打印出该冰淇淋店的名称
        print("The Ice cream stand's name is "+self.restaurant_name+".")

    def falvors_show(self): #打印出该店提供的冰淇淋口味
        print("The Ice cream stand's flavors includes ",end=" ")
        for flavor in self.flavors:
            print(flavor,end=",")
        print(".")
        
