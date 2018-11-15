class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        """创建restaurant 类的初始化信息"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        """描述餐厅的信息的函数"""
        print("The" +restaurant_name.title()+"has"+cuisine_type.title()+".")


    def open_restaurant(self):
        """ 描述餐厅在开的函数"""
        print("The"+ restaurant_type.title()+"is opening.")

    def set_number_served(self,numbers):
        """将餐厅服务过人数进行设定，并禁止将回调"""
        if numbers>=self.number_served:
            self.number_served=numbers
            print("The number served in the restuarant is"+str(self.number_served))
        else:
            print("You can't roll back the number served")
            

    def increment_number_served(self,increased_number):
        """将在餐厅用餐人数增加特定的值"""
        self.number_serverd+=increased_number
        print("The number served in the restaurant is"+str(self.number_served)+"now")
        
        




class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        """创建冰淇淋站类，继承餐厅类，并在其中增加属性flavors"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=[]

    def show_the_flavor_of_the_icecreamstand(self):
        """打印出冰淇淋站中各种口味的冰淇淋"""
        for flavor in self.flavors:
            print("There is "+flavor+" in the"+self.restaurant_name.title()+".")



    
