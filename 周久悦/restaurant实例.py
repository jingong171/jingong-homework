from restaurant import Restaurant,IceCreamStand

#创建restaurant的实例
rest=Restaurant('sugar','American flavor')
rest.set_number_served(30)
rest.show_number_served()
print()

#创建两个IceCreamStand类的实例
flavorlist_1=['chocolate','strawberry','blueberry','original']
flavorlist_2=['lemon','chocolate','strawberry','blueberry']
print("实例1")
my_IceCreamStand=IceCreamStand('icy','Chinese flavor',flavorlist_1)
my_IceCreamStand.describe_restaurant()
my_IceCreamStand.show_flavors()
print("实例2")
your_IceCreamStand=IceCreamStand('freezing','French flavor',flavorlist_2)
your_IceCreamStand.describe_restaurant()
your_IceCreamStand.show_flavors()
