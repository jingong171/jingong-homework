#有关冰淇淋小店餐馆的类
from restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        """继承并且新添冰淇淋口味属性"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """显示冰淇淋的口味"""
        print("冰淇淋的口味有：")
        for flavor in self.flavors:
            print(flavor.title())
    
        

