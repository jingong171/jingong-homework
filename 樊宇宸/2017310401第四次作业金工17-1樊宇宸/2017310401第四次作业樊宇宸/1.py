from random import randint
class Die:
    """创建骰子类"""
    def __init__(self,sides=6):
        """创建设置方法，属性sides初始值为6"""
        self.sides=sides
        
    def roll_die(self):
        """摇骰子函数"""
        x=randint(1,self.sides)
        #随机掷骰子，结果为1到sides的随机数
        print(x)

my_die=Die()
#创建我的骰子，这里未输入参数，默认六面
for i in range (1,11):
    my_die.roll_die()
#掷10次骰子
