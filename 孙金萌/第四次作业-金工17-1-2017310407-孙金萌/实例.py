from restaurant import Restaurant,IceCreamStand
my_own_restaurant = Restaurant('abc','H')
my_own_restaurant.describe_restaurant()

my_own_restaurant.set_number_served (23)
my_own_restaurant.get_number_served()

fla1 = ['strawberry','milk','choclate','vanilla']
fla2 = ['strawberry','milk','choclate','seasalt']

ice1 = IceCreamStand('1','icecream',fla1)
ice2 = IceCreamStand('2','icecream',fla2)

ice1.describe_icecream()
ice2.describe_icecream()
