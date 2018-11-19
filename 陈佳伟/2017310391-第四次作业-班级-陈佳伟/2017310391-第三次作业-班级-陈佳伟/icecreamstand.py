from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.number_served=0
        self.flavors=flavors
    def show_flavors(self):
        print("菜单:")
        for flavor in self.flavors:
            print(flavor)

restaurant_1=Restaurant("我的餐馆","Chinese food")
restaurant_1.set_number_served(5)
print("目前服务人数："+str(restaurant_1.number_served))

iceCreamStand_1=IceCreamStand("rock","chinese","chocolae","apple")
print("Restaurant's name："+iceCreamStand_1.restaurant_name)
iceCreamStand_1.show_flavors()
iceCreamStand_2=IceCreamStand("hello","japanese food","watermalon","orange")
print("Restaurant's name："+iceCreamStand_2.restaurant_name)
iceCreamStand_2.show_flavors()
