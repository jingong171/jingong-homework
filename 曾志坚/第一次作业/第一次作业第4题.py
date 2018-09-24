prime_numbers=[1,2,3,5,7]
for prime_number in prime_numbers :
    print(prime_number) 
for s in range(8,101):
    if s == 1*int(s) :
        if s != 2*int(s/2) :
            if s != 3*int(s/3) :
                if s != 5*int(s/5) :
                    if s != 7*int(s/7) :
                        print(s)
        
