#定义类Restraurant
class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
           """initialize restaurant names and cuisine types"""
           self.restaurant_name=restaurant_name
           self.cuisine_type=cuisine_type
           self.number_served=0 #初始化为0


    def describe_restaurant(self):
        print("The restaurant is "+str(self.restaurant_name.title()))
        print("The cuisine type is "+str(self.cuisine_type))

    def open_restaurant(self):
        print(str(self.restaurant_name)+" is open now.")

##添加一个名为set_number_served() 的方法，能够设置就餐人数
    def set_number_served(self,value):
        """Set the people number to the given value."""
        self.number_served=value

    def show_number_served(self):
        print("The restaurant has "+str(self.number_served)+" persons now.")

##通过函数进行递增
    def increment_number_served(self,value):
        """Add the given amount to the number_served."""
        self.number_served += value

#定义类IceCreamStand类
class IceCreamStand(Restaurant):
##"""Models aspects of a restaurant, specific to an icecream stand."""    
    def __init__(self,restaurant_name,cuisine_type):
           """initialize restaurant names and cuisine types"""
           super().__init__(restaurant_name,cuisine_type)
           self.flavors=['milk','herb','strawberry','mango']

#设置一个显示冰淇淋口味的方法
    def show_flavors(self):
        for flavor in self.flavors:
            print("We have "+str(flavor)+" in our restaurant.")



        


           
        
        
    
 








