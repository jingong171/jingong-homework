"""一组用于表示餐厅和冰激凌餐厅的类"""

class Restaurant():
    """创建一个restaurant类"""
    
    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性name,type"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        """打印restaurant_name和cuisine_type"""
        print("restaurant`s name: "+self.restaurant_name.title())
        print("The cuisine it serves: "+self.cuisine_type.title())

    def open_restaurant(self):
        """打印餐馆正在营业的信息"""
        print(self.restaurant_name.title()+" is open.")

    def read_number_served(self):
        """打印出一条指出就餐人数的消息"""
        print(self.restaurant_name.title()+" is now serving "+str(self.number_served)+" people.")

    def set_number_served(self,new_number):
        """设置就餐人数"""
        if new_number >= self.number_served:
            self.number_served=new_number
        else:
            print("You can`t roll back the number of people!")

    def increment_number_served(self,number_incr):
        """就餐人数递增"""
        self.number_served += number_incr

class IceCreamStand(Restaurant):
    """创建一个继承Restaurant类属性的小店Icecream类"""

    def __init__(self,restaurant_name,cuisine_type,flavors):
        """添加名为flavors的属性"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors

    def show_flavors(self):
        """显示这些冰激凌的方法"""
        print("The falvors of ice-cream are: "+str(self.flavors))
        
##restaurant_1=Restaurant("greatpizza","pizza")
##restaurant_2=Restaurant("beefnoodles","beefnoodles")
##restaurant_3=Restaurant("cutecake","cakes")
##
##restaurant_1.describe_restaurant()
##restaurant_2.describe_restaurant()
##restaurant_3.describe_restaurant()
##
##restaurant_1.set_number_served(81)
##restaurant_1.read_number_served()
##
##restaurant_1.increment_number_served(5)
##restaurant_1.read_number_served()
##
##IceCream1=IceCreamStand("icecreamland","icecream")
##IceCream1.describe_restaurant()
##IceCream1.show_flavors()
