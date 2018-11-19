class Restaurant():
    def __init__(self,name,type):
        self.name=name
        self.type=type
        self.number_served=0

    def describe_restaurant(self):
        print("The name of the restaurant is "+self.name.title())
        print("The cuisine type of the restaurant is "+self.type)

    def open_restaurant(self):
        print("Restaurant "+self.name.title()+" is open.")

    def set_number_served(self,number_served):
        """设置就餐人数"""
        self.number_served=number_served

    def increment_number_served(self,increment_number):
        """增加就餐人数"""
        self.number_served+=increment_number

    def show_number_served(self):
        """显示就餐人数"""
        print("餐厅目前服务人数："+str(self.number_served))


class IceCreamStand(Restaurant):
    def __init__(self,name,type,flavorlist):
        super().__init__(name,type)
        self.flavors=flavorlist
        
    def show_flavors(self):
        """显示各种口味的冰淇淋"""
        for flavor in self.flavors:
            print("One of the flavors is "+flavor)
