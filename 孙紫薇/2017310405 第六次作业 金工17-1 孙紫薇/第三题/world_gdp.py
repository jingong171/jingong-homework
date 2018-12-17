import json
import pygal
from country_codes import get_country_code
filename='gdp_json.json'
with open(filename) as f:
    pop_data=json.load(f)
cc_gdp={}
for pop_dict in pop_data:
    if pop_dict['Year']==2010:
        country_name=pop_dict['Country Name']
        gdp=int(float(pop_dict['Value']))
        code=get_country_code(country_name)
        if code:
            cc_gdp[code]=gdp
cc_gdp_1,cc_gdp_2,cc_gdp_3={},{},{}
for cc,gdp in cc_gdp.items():
    if gdp<10000000:
        cc_gdp_1[cc]=gdp
    elif gdp<1000000000:
        cc_gdp_2[cc]=gdp
    else:
        cc_gdp_3[cc]=gdp
print(len(cc_gdp_1),len(cc_gdp_2),len(cc_gdp_3))
wm=pygal.maps.world.World()
wm.title='World gdp in 2010,by Country'
wm.add('0-10000000',cc_gdp_1)
wm.add('10000000-1000000000',cc_gdp_2)
wm.add('>100000000000',cc_gdp_3)
wm.render_to_file('world_gdp.svg')
