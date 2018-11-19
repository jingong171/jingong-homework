class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        
    def describe_restaurant(self):
        print("The name of the restarant is "+ self.restaurant_name+'.')
        print("The cuisine_type is "+self.cuisine_type+'.')

    def open_restaurant(self):
        print("The restaurant is now opening.")

    def read_number(self):
        print("The number_served is "+str(self.number_served)+'.')

    def set_number_served(self,people):
        self.number_served=people

    def increment_number_served(self,customer):
        self.number_served+=customer


##restaurant=Restaurant('KFC','meat')
##restaurant.describe_restaurant()
##restaurant.read_number()
##
##restaurant.number_served=100
##restaurant.read_number()
##
##restaurant.set_number_served(50)
##restaurant.read_number()
##
##restaurant.increment_number_served(10)
##restaurant.read_number()

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['chocolate','mango','apple']
        
    def describe_flavors(self):
        for flavor in self.flavors:
            print(self.restaurant_name.title()+" provides "+self.cuisine_type.title()+" cuision and "+flavor+" ice cream.")

restaurant=IceCreamStand('kfc','meat')
restaurant.describe_flavors()
        
    
