class  Restaurant():

	"""docstring for Restaurant"""

	def __init__(self,restaurant_name,cuisine_type):

		self.restaurant_name = restaurant_name

		self.cuisine_type = cuisine_type

		self.number_served = 0

	def describe_restaurant(self):

		print(self.restaurant_name,":",self.cuisine_type)

	def open_restaurant(self):

		print("Is opening")

	def set_number_served(self,number):

		self.number_served = number

	def get_number_served(self):

		print(str(self.number_served))

	def increment_number_served(self,number):

		while self.number_served < number:

			print(self.number_served)

			self.number_served += 1

class IceCreamStand(Restaurant):
        """Specific figure of IceCreamStand"""

        def __init__(self,restaurant_name,cuisine_type,flavors = ['strawberry','milk','choclate']):
                """初始化父类的属性"""
                super().__init__(restaurant_name,cuisine_type)
                self.flavors = flavors

        def describe_icecream(self):
                """Show these kinds of icecream"""
                print("Name:"+self.restaurant_name.title())
                print("The following flavors:")
                for i in self.flavors:
                        print("\t"+i)
