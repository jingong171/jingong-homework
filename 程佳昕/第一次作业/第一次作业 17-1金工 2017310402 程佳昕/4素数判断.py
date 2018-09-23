n=[];
a=2
for a in range(2,101):
        b=2
        for b in range(2,a):
            if(a%b==0):
                break
        else:
            n.append(a)
print(n)
input("请输入回车键退出")
    
