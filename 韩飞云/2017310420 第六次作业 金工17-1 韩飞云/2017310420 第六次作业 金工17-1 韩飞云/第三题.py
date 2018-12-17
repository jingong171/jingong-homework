import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
filename='gdp_json.json'

#get country
def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name ==country_name:
            return code
    return None

#open the file
with open(filename)as f:
    gdp_data=json.load(f)
cc_gdp={}

#get data
for gdp_dict in gdp_data:
    if gdp_dict['Year']==2010:
        country_name=gdp_dict['Country Name']
        gdp=int(gdp_dict['Value'])
        code=get_country_code(country_name)
        if code:
            cc_gdp[code]=gdp

#set three class
cc_gdp_1,cc_gdp_2,cc_gdp_3={},{},{}
for cc,gdp in cc_gdp.items():
    if gdp<10000000000:
        cc_gdp_1[cc]=gdp
    elif gdp<100000000000:
        cc_gdp_2[cc]=gdp
    else:
        cc_gdp_3[cc]=gdp

#paint       
wm=pygal.maps.world.World()
print(len(cc_gdp_1), len(cc_gdp_2), len(cc_gdp_3))
wm.tilte='2010国家GDP'
wm.add('0-100b',cc_gdp_1)
wm.add('100b-1000b',cc_gdp_2)
wm.add('>1000b',cc_gdp_3)

#save
wm.render_to_file('world_gdp.svg')


