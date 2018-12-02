class Restaurant():
    """用于打印出餐馆的信息"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化类reataurant的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆的名称和菜种"""
        print("The restaurant name is "+self.restaurant_name)
        print("cuisine_type : "+self.cuisine_type)

    def open_restaurant(self):
        """打印餐馆正在营业的信息"""
        print("The restaurant is opening.")

    def set_number_served(self,numbers):
        """设置就餐人数并打印"""
        self.number_served = numbers
        print("The number_served of "+self.restaurant_name+" is "+str(self.number_served)+'\n')

    def increment_number_served(self,number):
        """设置增加的就餐人数"""
        self.number_served += number
        
    
        
