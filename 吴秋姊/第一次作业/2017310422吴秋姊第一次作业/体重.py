w=49
h=1.65
t=w/(h**2)
if t<18:
    message="轻"
elif t<=25:
    message="正常"
elif t<=27:
    message="超重"
else:
    message="肥胖"

print(t)
print("你是"+str(message)+"体重。")


    
