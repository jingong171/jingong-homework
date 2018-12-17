import csv

filename1="pythonsign_20181009.csv"
filename2="pythonsign_20181030.csv"
filename3="pythonsign_20181113.csv"

with open(filename1) as sign1:
    with open(filename2) as sign2:
        with open(filename3) as sign3:##打开三个签到数据文件
            reader1=csv.reader(sign1)
            reader2=csv.reader(sign2)
            reader3=csv.reader(sign3)

            head_line1=next(reader1)
            head_line2=next(reader2)
            head_line3=next(reader3)##消去第一行对数据的影响

            ID_Number,Name,Class,Sign_Times=[],[],[],[]##创建四个装载学生不同信息的列表

            for row in reader1:
                try:
                    ID=row[0]
                    name=row[1]
                    c=row[3]
                    if row[8]=="<准时到达>":
                        times=1
                    else:
                        times=0

                except ValueError:
                    print("Blank")
                else:
                    ID_Number.append(ID)
                    Name.append(name)
                    Class.append(c)
                    Sign_Times.append(times)##将第一个文件的数据写入四个列表中

            print(len(Sign_Times))

            student_num=0
            for x in range(100):
                if x ==len(Sign_Times):
                    student_num=x##创建一个变量用于储存学生人数

            print(student_num)##与前文“print(len(Sign_Times))”对应，检查列表长度与学生人数是否相等
                    
            for row in reader2:##将第二个文件的数据写入列表，其中重点在于使用新变量“y_n”检测文件2中的学生是否与文件1中重复，重复则记录本次考勤，若没有重复，则为将本名同学的信息加入四个列表中
                y_n=0
                for i in range(len(ID_Number)):
                    if ID_Number[i]!=row[0]:
                        continue
                    else:
                        y_n=1
                        if row[8]=="<准时到达>":
                            Sign_Times[i]=2

                if y_n==0:
                    student_num+=1
                    try:
                        ID=row[0]
                        name=row[1]
                        c=row[3]
                        if row[8]=="<准时到达>":
                            times=1
                        else:
                            times=0

                    except ValueError:
                        print("Blank")
                    else:
                        ID_Number.append(ID)
                        Name.append(name)
                        Class.append(c)
                        Sign_Times.append(times)

            for row in reader3:##等同文件2的方法将文件3的数据写入列表中
                y_n=0
                for i in range(len(ID_Number)):
                    if ID_Number[i]!=row[0]:
                        continue
                    else:
                        y_n=1
                        if row[8]=="<准时到达>":
                            Sign_Times[i]+=1

                if y_n==0:
                    student_num+=1
                    try:
                        ID=row[0]
                        name=row[1]
                        c=row[3]
                        if row[8]=="<准时到达>":
                            times=1
                        else:
                            times=0

                    except ValueError:
                        print("Blank")
                    else:
                        ID_Number.append(ID)
                        Name.append(name)
                        Class.append(c)
                        Sign_Times.append(times)

            wrong_input=[]##数据录入完毕，检查出错误输入的学号，将其所有信息剔除
            for j in range(0,student_num):
                if len(ID_Number[j])!=10:
                    print(ID_Number[j])
                    wrong_input.append(j)
            print(wrong_input)
            wrong_input.reverse()
            for k in range(0,len(wrong_input)):
                print(ID_Number.pop(wrong_input[k]))
                Name.pop(wrong_input[k])
                Class.pop(wrong_input[k])
                Sign_Times.pop(wrong_input[k])

            student_num-=len(wrong_input)
            print("Number of Students: "+str(student_num))
                    
            print(len(Sign_Times))
            print(len(ID_Number))
            print(len(Class))
            print(len(Name))

            filename="sign_times.txt"##将签到信息写入新文件
            with open(filename,'a') as file_object:
                for n in range(0,student_num):
                    file_object.write(str(Name[n])+','+str(ID_Number[n])+','+str(Class[n])+','+str(Sign_Times[n])+'\n')

            import matplotlib.pyplot as plt##将签到信息写入散点图
            plt.scatter(Name,Sign_Times,s=14)
            plt.title("Sign Times", fontsize=24)
            plt.xlabel("Name", fontsize = 14)
            plt.ylabel("Times", fontsize = 14)
            plt.show()
