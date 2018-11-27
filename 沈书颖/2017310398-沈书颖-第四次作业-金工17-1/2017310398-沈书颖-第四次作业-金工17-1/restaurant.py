class Restaurant():
    #创建餐厅的类

    def __init__(self,restaurant_name,cuisine_type):
        """设置餐厅名字，菜品，用餐人数三个属性"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    
    def describe_restaurant(self):
        """打印餐厅基本信息的函数"""
        print("The restaurant named"+self.restaurant_name+"has"+self.cuisine_type+".")

    def open_restaurant(self):
        """打印餐厅正在营业的函数"""
        print(self.restaurant_name+"is open.")

    def set_number_served(self,number):
        """设置就餐人数"""
        self.number_served=number
        print(str(self.number_served)+" people have been served in the restaurant.")

    def increment_number_served(self,number):
        """增加就餐的人数"""
        self.number_served+=number


class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        """继承父类和创建新的属性"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['chocolate','cream','strawberry']

    def show_flavors(self):
        """显示冰淇淋店的口味"""
        print('The ice cream stand named '+self.restaurant_name+' has these flavors:')

        for show_flavors in self.flavors:
            print(show_flavors)
