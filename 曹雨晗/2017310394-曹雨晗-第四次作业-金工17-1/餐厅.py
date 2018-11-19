from restaurant import Restaurant

r1=Restaurant("BestRestaurant" , "Chinese food")
r1.set_number_served(10)
print("The number of people the restaurant served is:" + str(r1.number_served))
r1.increment_number_served(20)
print("There are " + str(r1.number_served) + " people have been served.")

from restaurant import IceCreamStand

Icecream1=IceCreamStand("LittleGirl","dessert")
Icecream2=IceCreamStand("MyFavorite","dessert")
Icecream1.describe_restaurant()
Icecream1.set_flavors(['orange','apple','banana'])
Icecream1.describe_icecream()
Icecream2.describe_restaurant()
Icecream2.set_flavors(['strawberry','blue berry','melon'])
Icecream2.describe_icecream()
