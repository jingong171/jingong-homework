digits=[]
for a in range(1,10):
	for b in range(0,10):
		for c in range(0,10):
			if a*a*a + b*b*b + c*c*c == 100*a + 10*b + c:
				digits.append(100*a + 10*b + c)
print(digits)
				
