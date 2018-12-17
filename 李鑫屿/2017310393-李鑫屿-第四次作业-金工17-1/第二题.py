from Restaurant import Restaurant   #调用

my_restaurant=Restaurant("kongfu","Chinese_food")
my_restaurant.set_number_served(100)

from Restaurant import IceCreamStand  #调用

my_IceCreamshop1=IceCreamStand("stormy","icecream")
my_IceCreamshop1.change_flavors(["blue berry","orange","apple"])
my_IceCreamshop1.IceCream_flavors()
   
my_IceCreamshop2=IceCreamStand("snow","icecream")
my_IceCreamshop2.change_flavors(["strawberry","grape","watermelon"])
my_IceCreamshop2.IceCream_flavors()
