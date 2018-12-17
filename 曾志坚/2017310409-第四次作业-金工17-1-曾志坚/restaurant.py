class Restaurant():

    def __init__(self,restaurant_name,cuisine_type,number_served):
        self.restaurant_name = str(restaurant_name)
        self.cuisine_type = str(cuisine_type)
        self.number_served = number_served

    def describle_restaurant(self):
        print("Restaurant's name is"+" "+self.restaurant_name+".")
        print("And it provide"+" "+self.cuisine_type +".")

    def open_restaurant(self):
        print(self.restaurant_name + " "+"now is opening.")

    def set_number_served(self,a):
        self.number_served = int(a)
        print("The number of customers it has served is "+str(a)+".")

    def increment_number_served(self,b):
        self.number_served += int(b)
        print("The number of customers it has served is "+str(b)+".")
                



