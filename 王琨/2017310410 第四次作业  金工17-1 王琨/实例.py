from Restaurant import Restaurant,IceCreamStand

rest=Restaurant('New Yorker','American food')#Restaurant的一个实例
rest.increment_number_served(88)

#IceCreamStand的两个实例
icecream1=IceCreamStand('Yili','Chinses ice cream',['apple','chocolate','banana'])
icecream2=IceCreamStand('Mengniu','Chinese ice cream',['blueberry','grape','orange'])

icecream1.show()
icecream2.show()
