class Restaurant():
    def __init__(self,name,cuisine):
        """属性有店名和菜品"""
        self.restaurant_name=name
        self.cuisine_type=cuisine
        self.number_served=0

    def describe_restaurant(self):
        """打印店名和菜品"""
        print("The name of restaurant is "+restaurant_name.title())
        print("Food served here is "+cuisine_type.title())

    def open_restaurant(self):
        print("Restaurant is serving!")

    def set_number_served(self,num):
        """设置就餐人数并打印"""
        self.number_served=num
        print(str(self.number_served))

    def increment_number_served(self,increment):
        """增加就餐人数"""
        self.number_served+=increment
