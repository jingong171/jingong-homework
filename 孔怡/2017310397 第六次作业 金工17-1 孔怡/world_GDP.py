import json
import pygal
from pygal_maps_world.i18n import COUNTRIES

filename = 'gdp_json.json'
with open(filename)as f:
    gdp_data=json.load(f)

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name== country_name:
            return code
        return None

cc_gdp={}
for gdp_dict in gdp_data:
    if int(gdp_dict['Year'])==2010:
        country_name=gdp_dict['Country Name']
        gdp=gdp_dict['Value']
        code=get_country_code(country_name)
        if code:
            cc_gdp[code]=gdp


cc_gdp_1,cc_gdp_2,cc_gdp_3 = {},{},{}
for cc, gdp in cc_gdp.items():
    if gdp<1000000000:
        cc_gdp_1[cc] = gdp
    elif gdp<10000000000:
        cc_gdp_2[cc] = gdp
    else:
        cc_gdp_3[cc] = gdp
        

print(len(cc_gdp_1),len(cc_gdp_2),len(cc_gdp_3))

wm = pygal.maps.world.World()
wm.title = 'World GDP in 2010,by Country'
wm.add('0-1000000000',cc_gdp_1)
wm.add('1000000000-10000000000',cc_gdp_2)
wm.add('>10000000000',cc_gdp_3)
wm.render_to_file('world_gdp.svg')
