filenames=['cats.txt','dogs.txt']
#建立小狗名字和小猫名字的列表

def show_name(filename):
    """利用函数对文本中名字进行读取"""
    try:
        """打开文本并读取其中信息"""
        with open(filename) as f_obj:
            names=f_obj.readlines()
            #逐行读取文本中的名字，并存储在names列表中
            print(filename+"中的名字是：")
            for name in names:
                """循环读取names里表中的所有名字"""
                print(name.strip())
                #打印名字时用strip消除不必要的空格
    except FileNotFoundError:
        """如果找不到文本选择沉默不语"""
        pass

for filename in filenames:
    """循环对两个文本进行读取操作"""
    show_name(filename)
