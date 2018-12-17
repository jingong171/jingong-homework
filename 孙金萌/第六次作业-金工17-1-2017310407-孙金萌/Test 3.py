import json
import pygal
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Return country code"""
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    return None

filename='gdp_json.json'
with open(filename) as f:
    gdp_data=json.load(f)

gdps={}
for gdp_dict in gdp_data:
    if gdp_dict['Year']==2010:
        country_name=gdp_dict['Country Name']
        code=get_country_code(country_name)
        gdp=int(float(gdp_dict['Value']))
        if code:
            gdps[code]=gdp

gdps1,gdps2,gdps3={},{},{}
for code,value in gdps.items():
    if value<10000000000:
        gdps1[code]=value
    elif value<1000000000000:
        gdps2[code]=value
    else:
        gdps3[code]=value

wm=pygal.maps.world.World()
wm.title='World GDP in 2010, by country'
wm.add('0-10b',gdps1)
wm.add('10-1t',gdps2)
wm.add('>1t',gdps3)
wm.render_to_file('world_gdp.svg')
