from restaurant import Restaurant
#从restaurant.py中导入Rsetaurant类
class IceCreamStand(Restaurant):
    """创建冰淇淋站类，并继承饭店类"""
    def __init__(self,restaurant_name,cuisine_type,flavors):
        """创建冰淇淋站类的init方法"""
        super().__init__(restaurant_name,cuisine_type)
        #初始化父类属性
        self.flavors=flavors
        #建立子类特殊属性flavors
        
    def show_flavors(self):
        """显示冰淇淋的所有口味"""
        print("The flavors of ice cream are: ")
        for flavor in self.flavors:
            """循环打印出各个口味"""
            print(flavor)

                          
      
