from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,number_served):
        super().__init__(restaurant_name,cuisine_type="icecream",number_served=0)
        self.flavors = []

    def describe_flavors(self,a=[]):
        self.flavors = a
        print("Flavors are as follows:"+str(self.flavors))



