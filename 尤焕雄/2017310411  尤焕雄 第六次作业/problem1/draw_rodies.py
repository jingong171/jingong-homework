import pygal

from results_of_1000 import frequency,elements


hist=pygal.Bar()
hist.title="Results of rolling a D6 and a D10 dies"
hist.x_labels=map(str,elements)
hist.x_title="Elements"
hist.y_title="Frequecy"
hist.add('D6&D10',frequency)
hist.render_to_file("rolling dies.svg")
