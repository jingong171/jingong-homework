import json
import pygal
from country_codes import get_country_code
filename='gdp_json.json'
with open(filename) as f:
    gdp_data=json.load(f)
gdps={}
for gdp_dict in gdp_data:
    if gdp_dict['Year']==2010:
        country_name=gdp_dict['Country Name']
        gdp=int(float(gdp_dict['Value']))
        code=get_country_code(country_name)
        if code:
            gdps[code]=gdp
gdps1,gdps2,gdps3={},{},{}
for code,value in gdps.items():
    if value<100000000000:
        gdps1[code]=value
    elif value<10000000000000:
        gdps2[code]=value
    else:
        gdps3[code]=value
print(len(gdps1),len(gdps2),len(gdps3))
wm=pygal.maps.world.World()
wm.title='World GDP in 2010,by Country'
wm.add('0-100000000000',gdps1)
wm.add('100000000000-10000000000000',gdps2)
wm.add('>10000000000000',gdps3)
wm.render_to_file('world_gdp.svg')
