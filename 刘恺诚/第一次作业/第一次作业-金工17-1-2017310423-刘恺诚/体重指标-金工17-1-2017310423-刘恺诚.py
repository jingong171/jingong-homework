w=int(input('enter your weight(kg):'))
h=float(input('enter your high(m):'))

t=w/h**2

if t<18:
    print("低体重")
elif 18<=t<=25:
    print("正常体重")
elif 25<t<=27:
    print("超重体重")
elif t>27:
    print("肥胖")

    
