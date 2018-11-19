##定义一个餐馆类，包含餐馆的各类属性
class Restaurant:
    """define a class to describe restaurants"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("The restaurant is named "+self.restaurant_name.title())
        print("The cuisine food of the restaurant is "+
              self.cuisine_type.title())
        
    def open_restaurant(self):
        print("The restaurant "+self.restaurant_name+" is now open.")

    def show_number_served(self):
        print("there are "+str(self.number_served)+" eating")

    def set_number_served(self,number):
        self.number_served = number

    def increase_number_served(self,number):
        self.number_served += number
##定义一个冰淇淋店类，并继承餐馆类的各项属性，添加口味这一属性，显示口味的方法
class IceCreamStand(Restaurant):
    """define a icecreamstand"""
    
    def __init__(self,restaurant_name,cuisine_type,
                 flavors = ['strawberry']):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
        
    def show_flavors(self):
        print("Reataurant_name: "+self.restaurant_name.title())
        print("Our restaurant has different flavors as follow:")
        for i in self.flavors:
            print("\t"+i)


