for num in range(1,2001):
    numbers_2=[]
    for num_2 in range(1,2000):
	    if num>num_2:
		    t=num%num_2
		    if t==0:
			    numbers_2.append(num_2)
    if num==sum(numbers_2):
            print(str(num)+',')
