from restaurant import Restaurant,IceCreamStand

#创建Restaurant 实例
r1=Restaurant('食堂','各种餐点')
r1.set_number_served(30)

#创建IceCreamStand实例
r2=IceCreamStand('ABC','icecream')
r2.flavors=['chocolate','cream','vanilia']
r2.show_the_flavor_of_the_icecreamstand()

r3=IceCreamStand('DEF','icecream')
r3.flavors=['chocolate','lemon','cream']
r3.show_the_flavor_of_the_icecreamstand()
