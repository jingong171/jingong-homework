"""一个可用于表示餐馆的类"""

class Restaurant():
    """一次模拟餐馆的简单尝试"""
    def _init_(self,restaurant_name,cuisine_type):
        """初始化描述餐厅的属性"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        """模拟餐馆名和菜单"""
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        """模拟提示参观正在营业"""
        print("餐馆正在营业")
    def set_number_served(self,number)
        """模拟设置就餐人数"""
        self.number_served=number
    def increment_number_served(self,people)
    """将就餐人数增加制定的量并设置上限"""
    if self.number_served+<=100:
        self.number_served+=poeple
    else:
        self.number_served=100
restaurant=Restaurant(店名，菜谱）
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.number_served)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served=30
restaurant.number_served()
restaurant.set_number_served(50)
restaurant.number_served()
restaurant.increment_number_served(100)
restaurant.increment_numbwe_served()

class IceCreamStand(Restaurant):
    """冰激凌店的独特之处"""
    def _init_(self,restaurant_name,cuisine_type，number_served):
    """初始化父类的属性"""
        super()._init_(restaurant._name,cuisine_type)
        self.flavors=flavorlist
    def show_flavor(self):
    """模拟显示冰激凌的口味"""
        for flavor in self.flavors:
            print(flavor)
