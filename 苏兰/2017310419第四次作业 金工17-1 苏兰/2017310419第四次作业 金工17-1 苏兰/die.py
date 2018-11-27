class Die():
    """创建一个Die类"""
    def __init__(self,times):
        """初始化掷骰子的函数"""
        self.times=times
        self.sides=6

    def roll_die(self):
        """编写打印随机数的函数"""
        from random import randint
        x=randint(1,self.sides)
        print(x)

for i in range(1,11):
    """掷10次6面骰子"""
    times=Die(i)
    times.roll_die()
    
    
