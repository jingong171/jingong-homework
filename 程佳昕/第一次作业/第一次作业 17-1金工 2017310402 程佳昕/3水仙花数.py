for a in range(100,1000):
    b=a//100
    c=(a-b*100)//10
    d=a-b*100-c*10
    if a==b*b*b+c*c*c+d*d*d:
        print(a)
input("请输入回车键退出")
    
