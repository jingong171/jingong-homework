class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        """initiate name and type"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print("The restaurant name is "+self.restaurant_name.title())
        print("The cuisine type is "+self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self):
        print("The number served in this restaurant is "+str(self.number_served))

    def increment_number_served(self,number):
        """The total number served in this restaurant may be"""
        self.number_served+=number
        


class IceCreamStand(Restaurant):
    """A type of a restaurant,specific to icecream"""

    def __init__(self,restaurant_name,cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=[]

    def describe_flavor(self):
        """Print the flavor of icecream"""
        print("The flavors of icecream inclue:"+str(self.flavors))

    
