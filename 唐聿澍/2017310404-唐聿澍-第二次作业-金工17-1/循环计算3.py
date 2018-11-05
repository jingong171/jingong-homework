#a是基数，b是3倍的a，c是b的平方。s作为求和

s = 0

for a in range(1,11):#for 循环求和
    b = a * 3
    c = b * b
    s = s + c
print(s)
    
