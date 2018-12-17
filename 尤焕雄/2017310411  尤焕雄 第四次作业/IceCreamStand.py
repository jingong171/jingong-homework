from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,name,flavors):
        self.icecream_flavors=flavors
        super().__init__(name)

    def describe_restaurant(self):
        print("The name of stand is "+self.restaurant_name.title())

    def show_flavors(self):
        """把冰欺凌口味打印出来"""
        print("We have icecream of:")
        for fla in self.icecream_flavors:
            print(fla)



f1=["鸡蛋","大蒜","洋葱","香菜"]            
ICS1=IceCreamStand("臭小子",f1)
ICS1.describe_restaurant()
ICS1.show_flavors()
