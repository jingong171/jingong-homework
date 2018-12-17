class Restaurant(): #Restaurant类
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("The restaurant is "+self.restaurant_name)
        print("The cuisine type of this reataurant is "+self.cuisine_type)
    def open_restaurant(self):
        print("This restaurant is open")
    def set_number_served(self,new_served):
        self.number_served=new_served
        print("This restaurant has served "+str(new_served)+" people")
    def increment_number_served(self,increment_served):
        self.number_served+=increment_served
flavors=[]
class IceCreamStand(Restaurant):#继承
    def __init__(self,restaurant_name,cuisine_type):
      super().__init__(restaurant_name,cuisine_type)
      self.flavors=0
    def change_flavors(self,changed_flavors):
        self.flavors=changed_flavors
    def IceCream_flavors(self):
        print("This Icecream shop has ",end="")
        print(self.flavors)
        
        
