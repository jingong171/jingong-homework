import json
import pygal
from country_codes import get_country_code

filename='gdp_json.json'
with open(filename)as f:
    gdp_data=json.load(f)
cc_gdps={}
for gdp_dict in gdp_data:
    if gdp_dict['Year']==1998:
        country_name=gdp_dict['Country Name']
        gdp=int(float(gdp_dict['Value']))
        code=get_country_code(country_name)
        if code:
            cc_gdps[code]=gdp


cc_gdps_1,cc_gdps_2,cc_gdps_3={},{},{}
for cc,gdp in cc_gdps.items():
    if gdp<100000000000:
        cc_gdps_1[cc]=gdp
    elif gdp<1000000000000:
        cc_gdps_2[cc]=gdp
    else:
        cc_gdps_3[cc]=gdp
print(len(cc_gdps_1),len(cc_gdps_2),len(cc_gdps_3))

wm=pygal.maps.world.World()
wm_style = pygal.style.RotateStyle("#336699", base_style=pygal.style.LightColorizedStyle)
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title='World GDP in 1998,by Country'
wm.add('0-10bn', cc_gdps_1)
wm.add('10bn-100bn', cc_gdps_2)
wm.add('>100bn', cc_gdps_3)
wm.render_to_file('world_gdp.svg')

