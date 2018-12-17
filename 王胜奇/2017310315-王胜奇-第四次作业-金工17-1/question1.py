from random import randint #导入模块
class Die():#定义die类
	def __init__(self,sides):
		self.sides=sides
	def roll_die(self):
		print(randint(1,self.sides))
for i in range(1,11):
	Die(6).roll_die()#投掷骰子10次
