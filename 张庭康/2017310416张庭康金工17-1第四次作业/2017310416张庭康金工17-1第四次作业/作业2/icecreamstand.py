from restaurant import Restaurant
"""导入类Retaurant"""

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        """初始化类Restaurant的属性，再初始化类IceCreamStand的特有属性"""
        super().__init__(restaurant_name,cuisine_type)
        flavorslist = []    #创建口味列表
        self.flavors = flavorslist

    def describe_IceCreamStand(self):
        print("The IceCreamStand is "+self.restaurant_name)

    def show_flavors(self,flavors):
        """打印显示出各种口味的冰淇淋"""
        print("The icecream of this IceCreamStand is ")
        for i in flavors:
            print(i)
        print('\n')
