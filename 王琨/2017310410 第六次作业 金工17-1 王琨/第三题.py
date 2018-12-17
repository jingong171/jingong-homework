import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
     for code,name in COUNTRIES.items():
         if name==country_name:
             return code
     return None
filename='gdp_json.json'
with open(filename) as file:
     gdp_data=json.load(file)
     cc_gdp={}
     for gdp_dict in gdp_data:
         if int(gdp_dict['Year'])==2010:
             country_name=gdp_dict['Country Name']
             gdp=float(gdp_dict[ 'Value'])
             code=get_country_code(country_name)
             if code:
                 cc_gdp[code]=gdp

cc_gdp_1,cc_gdp_2,cc_gdp_3={},{},{}
for cc,gdp_ in cc_gdp.items():
     if gdp_<10000000000:
         cc_gdp_1[cc]=gdp_
     if gdp_<100000000000:
         cc_gdp_2[cc]=gdp_
     else:
         cc_gdp_3[cc]=gdp_


print(len(cc_gdp_1),len(cc_gdp_2),len(cc_gdp_3))
wm = pygal.maps.world.World()
wm.title = "The gross of GDP in 2010"
wm.add('0-10m',cc_gdp_1)
wm.add('10m-1b',cc_gdp_2)
wm.add('>1b',cc_gdp_3)
wm.render_to_file("world_gdp.svg")
