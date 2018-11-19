class Restaurant():
    def __init__(self,name,type,peple):
        self.restaurant_name=name
        self.restaurant_type=type
        self.restaurant_peple=peple

    def showName(self):
        print("the name is "+self.restaurant_name)

    def showType(self):
        print("the type is "+self.restaurant_type)

    def open_restaurant(self):
        print("the restaurant is onen")

    def showPeple(self):
        print("There are "+self.restaurant_peple+" waiters in "+self.restaurant_name+" right now.")
    
