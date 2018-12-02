class Restaurant():
    """模拟一个餐馆"""
    
    def __init__(self,restaurant_name,cuisine_type):
        """初始化参观信息"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        
    def descirbe_restaurant(self):
        """打印餐馆信息"""
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        """打印餐馆正在营业的信息"""
        print(self.restaurant_name.title()+"is now open")

    def set_number_served(self,number_served):
        """设置就餐人数"""
        self.number_served=number_served
        print('The number that the restaurant have served is '+str(number_served))

    def increment_number_served(self,possible_num):
        """增加一个就餐人数"""
        self.number_served=number_served+possible_num

class IceCreamStand(Restaurant):
    """模拟冰激凌店"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化父类的属性"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=["vanilla","chocolate","matcha","strawberry"]

    def describe_ice_cream(self):
        """打印冰激凌信息"""
        for flavor in self.flavors:
            print(flavor.title()+" ",end='')
        
