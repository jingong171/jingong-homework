from restaurant import *

restaurant1=Restaurant("examp","apple","tea","pear") #初始化一个饭店
restaurant1.set_number_served(3) #设定该饭店的就餐人次为3并打印

list1=["apple","stawberry","cola"] #icecream1的口味
list2=["watermelon","salt","hot"] #icecream2的口味

icecream1=IceCreamStand("ice1",list1,"ice","cream","water")
icecream2=IceCreamStand("ice2",list2,"pepper","berry")

icecream1.describe_restaurant() #打印icecream1的名称
icecream1.falvors_show() #打印icecream1的口味

icecream2.describe_restaurant() #打印icecream2的名称
icecream2.falvors_show() #打印icecream2的口味
