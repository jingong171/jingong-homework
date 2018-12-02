from restaurant import Restaurant
"""导入类Reataurant"""

#创建一个Restaurant 实例，打印该餐厅目前服务的人数
my_restaurant = Restaurant('old_zhang_RST','Chinese_food')
my_restaurant.set_number_served(100)

from icecreamstand import IceCreamStand
"""导入类IceCreamStand"""

#创建两个IceCreamStand类的实例，打印每个冰淇淋店的名字和所提供的冰淇淋口味
my_icecreamstand = IceCreamStand('old_zhang_ice','tradion')
flavors = ['Vanilla','Chocolate','Strawberry']
my_icecreamstand.describe_IceCreamStand()
my_icecreamstand.show_flavors(flavors)

your_icecreamstand = IceCreamStand('little_zhang_ice','not_tradion')
flavors = ['Lemon ','Coconut','Cheese']
your_icecreamstand.describe_IceCreamStand()
your_icecreamstand.show_flavors(flavors)
