from Restaurant import Restaurant
class icecreamstand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=["apple","banana","watermelon"]
    def describe_icecream(self):
        print("we have:")
        for show in self.flavors:
            print(show)
