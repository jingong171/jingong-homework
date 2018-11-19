class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        self.total_estimated_number=0
        
    def describe_restaurant(self):#打印饭馆名字与食物种类
        print("The name of restaurant is "+self.restaurant_name.title()+".")
        print("The restaurant has "+self.cuisine_type+".")

    def open_restaurant(self):#开张信息
        print("The restaurant is open.")

    def set_number_served(self,number):#点餐人数
        print(str(self.number))

    def increment_number_served(self,estimated_number):#来过餐厅的总用餐人数
         self.total_estimated_number+=estimated_number
         print(str(self.total_estimated_number))


class IceCreamStand(Restaurant):#Restaurant的子类
    def __init__(self,restaurant_name,cuisine_type,flavors=[]):
        self.flavors=flavors
        super().__init__(restaurant_name,cuisine_type)
        
    def show(self):#打印名称及口味
        print('The taste of '+self.restaurant_name+' are:',end='')
        for flavor in self.flavors:
            print(flavor+' ',end='')
        print('\n')
