a=list(range(0,10))
for b in a:
	for c in a:
		for d in a:
			e=b*100+c*10+d
			if e==b**3+c**3+d**3 and e>99 and e<1000:
				print(e)
