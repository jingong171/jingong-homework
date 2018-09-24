w=50
h=1.62
t=w/(h**2)
print(t)

if t<18:
    print('为低体重')
elif t<=25:
    print('为标准体重')
elif t<=27:
    print('为超重体重')
else:
    print('为肥胖')
   
