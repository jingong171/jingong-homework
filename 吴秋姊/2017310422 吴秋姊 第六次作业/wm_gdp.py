import json
import pygal
# Load the data into a list.
filename='gdp_json.json'
with open(filename) as f:
    gdp_data=json.load(f)

# Build a dictionary of gdp data.
#获取两个字母的国别码

from country_codes import get_country_code

for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2010:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)


cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2010:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdps[code] = gdp
wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_gdps) 
wm.render_to_file('world_gdp.svg')
