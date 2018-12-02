from Restaurant import Restaurant
from icecreamstand import icecreamstand
my_restaurant=Restaurant("Big","pizza")
print(my_restaurant.number_served)
my_icecream=icecreamstand("Yammy","icecream")
your_icecream=icecreamstand("Lily","icecream")
print(my_icecream.restaurant_name)
print(my_icecream.describe_icecream())
print(your_icecream.restaurant_name)
print(your_icecream.describe_icecream())
