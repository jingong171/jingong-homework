#一个有关餐馆的类
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        """对于餐馆名，做饭类型，就餐人数的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served  = 0

    def describe_restaurant(self):
        """打印餐馆的信息"""
        print("餐馆名字是：" + self.restaurant_name)
        print("参观口味是：" + self.cuisine_type)

    def open_restaurant(self):
        """打印餐馆正在营业"""
        print("The restaurant is opening!")

    def set_number_served(self):
        """设置就餐人数并且打印"""
        amount = int(input("请设置就餐人数："))
        self.number_served = amount
        print("该餐厅目前服务的人数为：" + str(self.number_served))

    def increment_number_served(self):
        """增加就餐人数并且打印"""
        add = int(input("请输入增加的就餐人数"))
        self.number_served = self.number_served + add
        print("该餐厅目前服务的人数为：" + str(self.number_served))

