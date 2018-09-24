w=60
h=1.78
t=w/h**2
if t<18:
    print("underweight")
elif 18<=t<=25:
    print("normal weight")
else:
    print("overweight")
