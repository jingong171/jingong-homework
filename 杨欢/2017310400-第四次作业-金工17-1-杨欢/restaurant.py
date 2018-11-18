class Restaurant():
    """饭店类"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化饭店类，使其拥有名字、种类、就餐人数三个属性"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        """描述饭店的名字和种类"""
        print("This restaurant's name is " + self.restaurant_name.title())
        print("Its cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        """餐厅营业"""
        print(self.restaurant_name.title() + " is opening.")

    def set_number_served(self,number_served):
        """设置就餐人数"""
        self.number_served=number_served

    def increment_number_served(self,increment):
        """增加就餐人数"""
        self.number_served+=increment
