import json
import pygal
# Load the data into a list.
filename='gdp_json.json'
with open(filename) as f:
    gdp_data=json.load(f)

#获取两个字母的国别码
from country_codes import get_country_code

cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2010:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdps[code] = gdp

# Group the countries into 3 population levels.
cc_gdps_1, cc_gdps_2, cc_gdps_3,cc_gdps_4,cc_gdps_5 = {}, {}, {},{},{}
for cc, gdp in cc_gdps.items():
    if gdp < 10000000000:
        cc_gdps_1[cc] = gdp
    elif gdp <50000000000:
        cc_gdps_2[cc] = gdp
    elif gdp <100000000000:
        cc_gdps_3[cc] = gdp
    elif gdp <1000000000000:
        cc_gdps_4[cc] = gdp
    else:
        cc_gdps_5[cc] = gdp

# See how many countries are in each level.        
print(len(cc_gdps_1), len(cc_gdps_2), len(cc_gdps_3),len(cc_gdps_4),len(cc_gdps_5))
wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('0-10bn', cc_gdps_1)
wm.add('10bn-50bn', cc_gdps_2)
wm.add('50bn-100bn', cc_gdps_3)
wm.add('100bn-1000bn', cc_gdps_4)
wm.add('>1000bn', cc_gdps_5)
wm.render_to_file('world_gdp1.svg')

