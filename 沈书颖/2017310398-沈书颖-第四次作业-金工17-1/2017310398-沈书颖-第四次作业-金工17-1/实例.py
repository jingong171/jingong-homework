from restaurant import Restaurant,IceCreamStand

my_restaurant=Restaurant('海底捞','火锅')
my_restaurant.set_number_served(600000)

first_IceCreamStand=IceCreamStand('哈根达斯','冰淇淋')
first_IceCreamStand.flavors=['比利时巧克力','蓝莓口味','抹茶口味']
first_IceCreamStand.show_flavors()

second_IceCreamStand=IceCreamStand('DQ','冰淇淋')
second_IceCreamStand.flavors=['奥利奥','蒙布朗栗子','樱桃口味']
second_IceCreamStand.show_flavors()
