""" resturant in 9-4 """

class Restuarant():
    """创建一家餐厅""" 
    def __init__(self,restuarant_name,cuisine_type):
        """初始化店名和菜品种类"""
        self.restuarant_name=restuarant_name
        self.cuisine_type=cuisine_type
        self.number_served= 0
    def describe_restuarant(self):
        """描述店名和菜品种类属性"""
        print("The restuarant name is: "+ self.restuarant_name)
        print("The cuisine type is:" + self.cuisine_type)
    def open_restuarant(self):
        """描述是否正常营业sh"""
        print("The restuarant is opening.")
    def get_number_served(self):
        """print the number of people restuarant served"""
        print("The number of customs is: "+str(self.number_served))
    def set_number_served(self,number):
        """设置就餐人数"""
        self.number_served=number
    def increment_number_served(self,people):
        """增加就餐人数"""
        self.number_served+=people
        
rest1 = Restuarant('shitang','Chinese food')
rest2 = Restuarant('kfc','American food')
rest1.describe_restuarant()
rest2.describe_restuarant()
rest1.open_restuarant()
rest2.get_number_served()
rest2.number_served=50
rest2.get_number_served()
rest1.set_number_served(46)
rest1.get_number_served()
rest1.increment_number_served(20)
rest1.get_number_served()
