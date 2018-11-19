from restaurant import Restaurant,IceCreamStand
##建立一个餐馆，并显示服务人数
rest1 = Restaurant('qingfeng','chinese')
rest1.set_number_served(200)
rest1.show_number_served()
##定义两个列表，用于传递给对象
flavor1 = ['Strawberry','Chocolate','Vanilla','Matcha ',
           'Strawberry','Coconut']
flavor2 = ['Strawberry','Chocolate','Vanilla','Matcha ',
           'Caramel','Raspberry','Cheese']
##建立两个冰淇淋店对象，并打印各自的口味
ice1 = IceCreamStand('love and you','american',flavor1)
ice2 = IceCreamStand('encountering','icecream',flavor2)
ice1.show_flavors()
ice2.show_flavors()
