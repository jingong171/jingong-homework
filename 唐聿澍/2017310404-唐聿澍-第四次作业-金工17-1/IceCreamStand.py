from restaurant import Restaurant,IceCreamStand#import2个类



rest_1 = Restaurant('Restaurant_1','Rice')
print("现在餐厅的人数：" + str(rest_1.number_served))#打印就餐人数

flavors_1 = ['strawberry','blueberry']#口味1
icecream_1 = IceCreamStand('Yami',flavors_1)#创建Icecream类1
print("冰淇淋店1的名字：" + str(icecream_1.name))
print("口味：")
icecream_1.show_flavors()#方法打印口味1

flavors_2 = ['chocolate','milk']#口味2
icecream_2 = IceCreamStand('Oishi',flavors_2)#创建Icecream类2
print("冰淇淋店2的名字：" + str(icecream_2.name))
print("口味：")
icecream_2.show_flavors()#方法打印口味2
