from restaurant import *
#导入模块
#创建餐厅实例
restaurant1=Restaurant('dining hall','rice')
#设置餐厅人数为100,打印就餐人数
restaurant1.set_number_served(100)
#创建冰激凌店实例
icecreamstand1=IceCreamStand('Haagen_Dazs','ice cream')
icecreamstand2=IceCreamStand('Nestle','ice cream')
#打印冰激凌店信息
print(icecreamstand1.restaurant_name)
icecreamstand1.describe_ice_cream()
print('')
print(icecreamstand2.restaurant_name)
icecreamstand2.describe_ice_cream()
