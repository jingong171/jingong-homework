import pygal
from die import Die
#Create a D6 die and a D10 die.
die_1=Die()
die_2=Die(10)
#Make some rolls,and store results in a list.
results=[]
for roll_num in range(5000):
    result=die_1.roll()*die_2.roll()
    results.append(result)
#Analyse the results.
frequencies=[]
max_result=die_1.num_sides*die_2.num_sides
for value in range(1,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
#Visualize the results.
hist=pygal.Bar()
hist.title="Results of rolling a D6 die and a D10 die 5000 times."
hist.x_labels =['1','2','3','4','5','6','7','8','9','10','12','14','15','16','18','20','21','24','25','27','28','30','32','35','36','40','42','45','48','49','50','54','56','60']
hist.x_title="Result"
hist.y_title="Frequency of Resullt"
hist.add('D6*D10',frequencies)
hist.render_to_file('dice_visual_two_die_6_10.svg')
