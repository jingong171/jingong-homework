from restaurant import Restaurant
##导入Restaurant类

class IceCreamStand(Restaurant):
    """冰淇淋小站类"""

    def __init__(self,restaurant_name,cuisine_type,flavors=[]):
        """在饭店类的基础上加上口味属性"""
        self.flavors=flavors
        super().__init__(restaurant_name,cuisine_type)

    def describe_IceCream(self):
        """描述冰淇淋"""
        print("We have ice cream of this flavors:",end='')
        for flavor in self.flavors:
            print(flavor,end=' ')
        print('')
