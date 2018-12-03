class restaurant():
    #创建父类
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served

    def describe_restaurant(self):
        print("The reataurant's name is "+self.restaurant_name+".")
        print("The cuisine type of the restaurant is "+self.cuisine_type+".")
    
    def open_restaurant(self):
        print("The restaurant is opening.")

    def read_number_served(self):
        print(str(self.number_served)+' people have been served.')

    def set_number_served(self,number):
        self.number_served=number
        print(str(self.number_served)+"people is served.")
    
    def increment_number_served(self,customer_number):
        self.number_served+=customer_number
    
class IceCreamStand(restaurant):
    #继承
    def __init__(self,restaurant_name,cuisine_type,flavors):
        #初始化父类属性
        super().__init__(restaurant_name,cuisine_type,flavors)#初始化特有属性
        self.flavors=flavors

    def read_flavors(self):
        #显示冰淇淋口味
        print("The flavors we have: "+str(self.flavors))
    
    def describe_IceCreamStand(self):
        #打印冰淇淋店名字
        print("The IceCreamStand's name is "+self.restaurant_name)

my_restaurant=restaurant('ZAN','Thai Food',100)
my_restaurant.read_number_served()
#创建两个冰淇淋实例
IceCreamStand1=IceCreamStand('Sunny','icecream',['strawberry','blueberry','vanilla'])
IceCreamStand1.read_flavors()
IceCreamStand1.describe_IceCreamStand()
IceCreamStand2=IceCreamStand('Happy','icecream',['strawberry','blueberry','vanilla','chocolate'])
IceCreamStand2.read_flavors()
IceCreamStand2.describe_IceCreamStand()