from Restaurant import *
#restaurant实例(两种不同的现实人数方法)
favorite_restaurant=Restaurant('Hot_Pot','Chinese food')
favorite_restaurant.describe_restaurant()
favorite_restaurant.show_number_served()

favorite_restaurant=Restaurant('Hot_Pot','Chinese food')
favorite_restaurant.describe_restaurant()
favorite_restaurant.set_number_served(25)
favorite_restaurant.show_number_served()

favorite_restaurant.increment_number_served(30)
favorite_restaurant.show_number_served()

#icecreamstand实例
my_icecreamstand=IceCreamStand('Big_Pizza','American food')
your_icecreamstand=IceCreamStand('NAKKA','Japanese food')
my_icecreamstand.describe_restaurant()
my_icecreamstand.show_flavors()
your_icecreamstand.describe_restaurant()
your_icecreamstand.show_flavors()






