for m in range(100,1000):
	if m==int(m/100)**3+(int(m/10)-int(m/100)*10)**3+(m-(int(m/10)-int(m/100)*10)*10-int(m/100)*100)**3:
		print(m)
