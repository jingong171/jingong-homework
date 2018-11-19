class Restaurant():#Restaurant的类
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 3

    def describe_restaurant(self):
        print(self.restaurant_name.title() + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self,number):
        self.number_served = number
        print("The number is " + str(self.number_served))

    def increment_number_served(self,inc):
        self.number_served += inc
        print("The number is " + str(self.number_served))
        
class IceCreamStand(Restaurant):#Icecream的类
    def __init__(self,name,flavors):#继承自Restaurant
        self.name = name
        self.flavors = flavors#口味列表

    def show_flavors(self):#打印列表
        for flavor in self.flavors:
            print(flavor)
        print('')
