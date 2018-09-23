numbers=list(range(2,100))
print(2)
for a in numbers:
    dividers=list(range(2,a))
    squares=[]
    for b in dividers:
        c=a%b
        if c!=0:
            squares.append(c)
            d=len(squares)
            if d==a-2:
                print(a)

                
