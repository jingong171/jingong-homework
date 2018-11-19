class Restaurant(object):
	def __init__ (self,name,types):                
		self.restaurant_name=name
		self.cuisine_type=types
		self.number_served=0
	def describe_restaurant(self):
		print("Rsetaurant name is %.\n Cuisine type is %s."%(self.restaurant_name,self.cuisine_type))
	def open_restaurant(self):
		print("Open restaurant.")
	def set_number_served(self,num):
		self.number_served=num
	def increment_number_served(self,num):
		self.number_served+=num

		
class IcecreamStand(Restaurant):
	def __init__ (self,name,types):
		super().__init__(name,types)
		"""加属性，各种口味"""
		self.flavours=["vanilla","strawberry","chocolate","rum"]
	def show_flavours(self):
		print(self.flavours)
		"""实例调用"""
a=IcecreamStand("ssss","chinese")
a.show_flavours()
