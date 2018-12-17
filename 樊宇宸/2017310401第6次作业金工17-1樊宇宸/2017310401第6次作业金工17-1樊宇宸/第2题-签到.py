import csv
from matplotlib import pyplot as plt
filenames=['pythonsign_20181009.csv',
           'pythonsign_20181030.csv',
           'pythonsign_20181113.csv']
#提前建立好空列表用于储存学号，班级，姓名，签到次数
numbers,classes,names,counts=[],[],[],[]
#设置i用于记录是统计到的第i个学生，方便将其信息绑定在第i项
i=0
for filename in filenames:
    """依次读取三次签到表"""
    with open(filename) as f:
        reader=csv.reader(f)
        header_row=next(reader) 
        for row in reader:
            """依次读取签到表中的每一行"""
            num=row[0][7:]
            if num in numbers:
                """如若该学生信息已被统计，则在其签到次数+1即可"""
                #利用index函数检索该学生在列表中的位置，在其次数上加1
                counts[numbers.index(num)]+=1
            else:
                """如若该学生未被统计，则将其作为第i个学生并录入信息，且次数为1"""
                i+=1
                numbers.append(num)
                names.append(row[1])
                classes.append(row[3])
                counts.append(1)
#设置图像格式，分辨率
fig=plt.figure(dpi=128,figsize=(10,6))
#制作学号和签到次数的散点图，点为蓝色
plt.scatter(numbers,counts,c='blue',s=10)
#设置标题和x,y轴属性
plt.title("Counts of Attendence",fontsize=24)
plt.xlabel("number",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("counts",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=5)
plt.show()
    
            
        
           
    

        
