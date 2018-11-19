from restaurant import Restaurant #导入Restaurant类

Flavors=['chocolate','strawberry','blueberry','mango']
class IceCreamStand(Restaurant): #定义IceCreamStand类（继承Restaurant类)
    def __init__(self,name,number_served):
        super().__init__(name,number_served) #调用父类Restaurant函数
        self.flavors=Flavors
        
    def show_flavors(self): #展示冰激凌口味
        print("The icecream flavors provided in "
              +str(self.name.title())+ " are:")
        for i in range(0,4):
            print(self.flavors[i])
        print("\n")
