from Restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.number_served=0
        self.flavors=flavors
    def show_flavors(self):
        print("The flavors of the icecream :"+self.flavors+".")

restaurant_1=Restaurant("1号餐馆","op")
restaurant_1.set_number_served(5)
print(restaurant_1.number_served)

flavors_1=["巧克力","香草"]
flavors_2=["草莓","巧克力"]
iceCreamStand_1=IceCreamStand("1号冰淇淋","op",str(flavors_1))
print("Restaurant's name："+iceCreamStand_1.restaurant_name)
iceCreamStand_1.show_flavors()
iceCreamStand_2=IceCreamStand("2号冰淇淋","op",str(flavors_2))
print("Restaurant's name："+iceCreamStand_2.restaurant_name)
iceCreamStand_2.show_flavors()
