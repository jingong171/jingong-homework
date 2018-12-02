class Restaurant:
    """创建Restaurant类"""
    def __init__(self,restaurant_name,cuisine_type):
        """创建init方法设置饭店属性"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        #服务人数默认值为0
        
    def describe_restaurant(self):
        """打印饭店信息"""
        print("The name of this restaurant is "+self.restaurant_name+".")
        print("The restaurant sells "+self.cuisine_type+".")
        
    def open_restaurant(self):
        """打印餐馆正在营业的消息"""
        print("Now the restaurant is open.")
        
    def set_number_served(self,new_number):
        """传递一个值来更改就餐人数"""
        self.number_served=new_number
        
    def increment_number_served(self,increased_number):
        """传递就餐人数增加值来增加就餐人数"""
        self.number_served+=increased_number

        
    
                
                

    
                
                
