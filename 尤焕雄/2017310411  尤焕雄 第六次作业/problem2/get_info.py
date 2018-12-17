import csv

file1='pythonsign_20181009.csv'
file2='pythonsign_20181030.csv'
file3='pythonsign_20181113.csv'
file=[file1,file2,file3]
infos=[]
##对文件进行循环读取
for i in file:
    with open(i) as f:
        reader=csv.reader(f)
        head_row=next(reader)
        for row in reader:
            stu_dic={}
            stu_dic['no']=row[0]
            stu_dic['name']=row[1]
            stu_dic['class']=row[3]
            infos.append(stu_dic)

##把学生的学号提取出来，并建立一个不重复的列表
distinct_num=[]
for i in infos:
    distinct_num.append(i['no'])

distinct_num=set(distinct_num)

def get_name(num):
    ##同一个学生，可能第一次签到写了姓名，第二次没写
    name=''
    for info in infos:
        if info['no']==num:
            if name=='':
                name=info['name']
            else:
                break
    return name

def get_class(num):
    ##同一个同学，可能有时候写了班级，有时候没写
    _class=''
    for info in infos:
        if info['no']==num:
            ##如果之前读取的信息已经存有班级，就不再改写class
            if _class=='':
                _class=info['class']
            else:
                break
    return _class

def get_times(num):
    count=0
    for info in infos:
        if info['no']==num:
            count+=1

    return count
            
