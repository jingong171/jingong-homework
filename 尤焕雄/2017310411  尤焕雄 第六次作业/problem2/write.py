from get_info import infos,distinct_num,get_name
from get_info import get_class,get_times

import csv

file='sign_up.csv'
##把签到信息写入一个csv文件
with open(file,'w',newline='') as f:
    fwriter=csv.writer(f)
    fwriter.writerow(['学号','姓名','班级','次数'])
    for dis in distinct_num:
        ##调用三个自定义的函数
        wriobj=[dis,get_name(dis),get_class(dis),get_times(dis)]
        fwriter.writerow(wriobj)


##画图，先把学号和次数装进两个列表里
import matplotlib.pyplot as plt
times=[]
intnum=[]
for num in distinct_num:
    if len(num)==10:
        times.append(get_times(num))
        intnum.append(int(num))
##把图画出来
plt.scatter(intnum,times,s=50,c='b')
plt.title("sign up times",fontsize=25)
plt.xlabel("number",fontsize=23)
plt.ylabel("times",fontsize=23)
plt.tick_params(axis='both',which='major',labelsize=12plt.show()
