from restaurant import Restaurant
from icecreamstand import IceCreamStand

##建立新的Restaurant类
Pinor_restaurant = Restaurant('Pinor Food','Chinese food',0)
Pinor_restaurant.describle_restaurant()
Pinor_restaurant.set_number_served(0)

##建立两个IceCreamStand类
His_iceshop = IceCreamStand('HeFood','icecream',0)
Her_iceshop = IceCreamStand('SheFood','icecream',0,)

##分别描述两店名字以及产品种类
His_iceshop.describle_restaurant()
His_iceshop.describe_flavors(['stawburry','blueburry','herb'])

Her_iceshop.describle_restaurant()
Her_iceshop.describe_flavors(['chocolate','milk','lemon'])
