print("请输入两个数字")
k=0  #k用于记录用户输入了多少个数字
s=0  #s用于储存两个数字的加法结果
while k<2:
    """循环输入数字，直到输入了两个数字"""
    try:
        """输入一个数字并转换为整数类型"""
        x=int(input())
    except ValueError:
        """如果输入的是文本，将触发ValueError，对用户进行提醒"""
        print("你输入的不是数字哦。")
    else:
        """如若未出现异常，即输入的是数字，则输入数字数量加1，并加到结果s内"""
        s+=x
        k+=1
with open("加法结果.txt",'w') as f_obj:
    """将加法结果写入'加法结果.txt'中"""
    f_obj.write(str(s))
    

    

      
      
