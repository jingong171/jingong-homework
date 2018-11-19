from Restaurant import Restaurant,IceCreamStand
Restaurant=Restaurant('一楼食堂','美食')
Restaurant.serve(10)#初始人数
Restaurant.increase_serve(10)#增加人数
Restaurant.number_show()#人数展示
IceCreamStand_1=IceCreamStand("KFC","甜品站","苹果、雪碧")
IceCreamStand_1.restaurant_flavors()#打印第一个IceCreamStand实例
IceCreamStand_2=IceCreamStand("MC","甜品站","水蜜桃")
IceCreamStand_2.restaurant_flavors()#打印第二个IceCreamStand实例