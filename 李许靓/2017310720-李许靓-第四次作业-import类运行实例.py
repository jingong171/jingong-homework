from res import Restaurant, IceCreamStand       #导入Restaurant, IceCreamStand两个类
res1=Restaurant("KFC","American")               #设置Restaurant的一个实例
res1.set_number_served(100)                     #设置res1的就餐人数
res1.describe_served_number()                   #打印res1的就餐人数
flavors1=["lemon","apple","banna"]              #设置一个口味集
ice1=IceCreamStand("Yammy","Icecream")          #设置IceCreamStand的实例ice1
ice1.flavors=flavors1                           #将口味集flavors1赋给ice1
flavors2=["chocolate","orange"]                 #设置一个另口味集
ice2=IceCreamStand("Tasty","Icecream")          #设置IceCreamStand的实例ice2
ice2.flavors=flavors2                           #将口味集flavors2赋给ice2
ice1.describe_restaurant()                      #打印ice1名称
ice1.describe_flavors()                         #打印ice2名称
ice1.describe_restaurant()                      #打印ice1口味集
ice1.describe_flavors()                         #打印ice2口味集