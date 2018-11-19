class Restaurant(): #定义Restaurant类
    def __init__(self,name,number_served):
        self.number_served=number_served
        self.name=name
        print("The number of people being served in the restuarant "
              +str(self.name.title()) +" is "+str(self.number_served)+".\n")
              #打印餐厅服务人数
