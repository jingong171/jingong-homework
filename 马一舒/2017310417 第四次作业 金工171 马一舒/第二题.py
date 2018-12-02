from icecreamstand import Restuarant,IceCreamStand
print("\n")
"""一个饭店实例并显示就餐人数"""
restuarant = Restuarant('pop','Japanese food')
restuarant.describe_restuarant()
restuarant.set_number_served(100)
restuarant.get_number_served()


"""创建两个冰淇淋店并设置不同口味"""
ice1=IceCreamStand('apple','dessert shop')
print("The name of this ice-cream shop is " +ice1.restuarant_name.title())
ice1.describe_flavor()

ice2=IceCreamStand('strawberry island','dessert ')
print("The name of this ice-cream shop is " +ice2.restuarant_name.title())
ice2.flavors="strawberry"
ice2.describe_flavor()
