class Restaurant():#将最新的Restaurant 类存储在一个模块中
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number =0
	def describe_restaurant(self):
		print("餐厅名称:"+self.restaurant_name)
		print("餐厅类型:"+self.cuisine_type)
	def serve(self,number):
		self.number=number
	def increase_serve(self,increase):
		self.number+=increase
	def number_show(self):
		print(self.number)
class IceCreamStand(Restaurant):#编写IceCreamStand类让它继承Restaurant 类
	def __init__(self,restaurant_name,cuisine_type,flavors):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=flavors
	def restaurant_flavors(self):
		print("这里口味有:"+self.flavors)
		