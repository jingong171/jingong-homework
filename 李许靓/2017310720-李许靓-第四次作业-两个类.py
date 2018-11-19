class Restaurant():
    """创建一个Restaurant类"""
    def __init__(self,retaurant_name,restaurant_type):      #初始化描述Restaurant的属性
        self.retaurant_name=retaurant_name
        self.restaurant_type=restaurant_type
        number_served=0

    def describe_restaurant(self):                          #创建一个描述restaurant的函数
        print("The restaurant name is "+self.retaurant_name.title())
        print("The restaurant type is "+self.restaurant_type.title())

    def open_restaurant(self):                              #创建指出参观正在营业的函数
        print("The restaurant is open .")

    def set_number_served(self,number):                     #创建设置就餐人数的函数
        self.number_served=number

    def increment_number_served(self,incre_number):         #创建能够递增就餐人数的函数
        self.number_served+=incre_number

    def describe_served_number(self):                       #创建描述就餐人数的函数
        print("Now there are "+str(self.number_served)+" people in the restaurant. ")

class IceCreamStand(Restaurant):                                        #创建IceCreamStand类，以Restaurant为父类
    def __init__(self,retaurant_name,restaurant_type):         #初始化子类IceCreamStand的属性
        super().__init__(retaurant_name,restaurant_type)
        self.flavors=[]

    def describe_restaurant(self):                                      #改写父类函数
        print("The restaurant name is "+self.retaurant_name.title())

    def describe_flavors(self):
        print("The flavors of the icecream are as follows: ")
        for flavor in self.flavors:
            print(flavor)

