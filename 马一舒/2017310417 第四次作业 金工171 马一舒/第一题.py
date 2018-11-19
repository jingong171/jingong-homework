from random import randint
class Die():
    """创建一个骰子类"""
    def __init__(self,sides=6):
        """初始化面数属性并设置默认值"""
        self.sides=sides
    def roll_die(self):
         """打印位于1和骰子面数之间的随机数"""
         print("掷出的点数为："+str(randint(1,self.sides)))
"""创建一个六面的骰子即使用默认值"""
shaizi=Die()
print("骰子的面数为6")
for i in range(1,11):
    """再掷十次骰子"""
    shaizi.roll_die()
