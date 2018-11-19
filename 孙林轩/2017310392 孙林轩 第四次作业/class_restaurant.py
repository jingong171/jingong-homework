class Restaurant():

    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        """Restaurant类构造函数"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served

    def describe_restaurant(self):
        """打印餐馆名和菜单类型"""
        print("The restaurant name is:",self.restaurant_name)
        print("Our cuisine type is:",self.cuisine_type)

    def open_restaurant(self):
        """描述餐馆正在营业"""
        print("Now",self.restaurant_name,"is open,welcome to come!")

    def set_number_served(self):
        """打印目前餐馆有多少人就餐并修改就餐人数"""
        new_number=int(input("Please enter the number of customers in the restaurant:"))
        self.number_served=new_number
        print("Now,",self.number_served,"customers have been served in",self.restaurant_name)

    def increment_number_served(self):
        """将每天新增的就餐人数加到总就餐人数上并打印"""
        add_number=int(input("Today customers served in our restaurant is:"))
        self.number_served+=add_number
        print("Now,",self.number_served,"customers have been served in",self.restaurant_name)
class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type,number_served=0,*flavors):
        """IceCreamStand类构造函数"""
        super().__init__(restaurant_name,cuisine_type,number_served)
        self.flavors=[]
        for flavor in flavors:
            self.flavors.append(flavor)

    def describe_icecreamstand(self):
        """打印冰激凌店名字以及拥有的冰激凌口味"""
        print(self.restaurant_name,"has icecream of these flavors:")
        for flavor in self.flavors:
            print(flavor,end=' ')

Mi=Restaurant("米其林餐厅","法式",134)
Mi.describe_restaurant()
Mi.open_restaurant()
DQ=IceCreamStand("DairyQueen","cream",7,"Chocolate","Cream","Mango","Strawberry","Pineapple")
DQ.describe_icecreamstand()