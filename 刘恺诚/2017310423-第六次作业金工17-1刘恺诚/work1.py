import pygal
import matplotlib.pyplot as plt

from die import Die
#Create a D6.
dieA=Die()
dieB=Die()

results=[]
for roll_num in range(100):
    result=dieA.roll()*dieB.roll()
    results.append(result)

x_values=list(range(1,101))
plt.scatter(x_values,results,linewidth=2,marker='+')
plt.title("The product of throw 2 dies 100 times.",fontsize=14)
plt.xlabel("times",fontsize=14)
plt.ylabel("values",fontsize=14)

plt.show()
