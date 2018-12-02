from Restaurant import Restaurant

class IceCreamStand(Restaurant):
    """this is a icecream shop"""
    def __init__(self,name,type,peple,flavors=['berry','wine','lemon','chocolate']):
        super().__init__(name,type,peple)
        
        self.flavors=flavors

    def showFlavors(self):
        print(self.flavors)
    
