import json
import pygal
from country_codes import get_country_code
# Load the data into a list.
filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)
# Build a dictionary of gdp data.
cc_gdp={}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2010:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code=get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp
wm = pygal.maps.world.World()
wm.title = 'World GDP in 2010, by Country'
wm.add('2010', cc_gdp) 
wm.render_to_file('world_gdp.svg')

# Group the countries into 3 population levels.
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for cc, gdp in cc_gdp.items():
    if gdp < 10000000000:
        cc_gdp_1[cc] = gdp
    elif gdp < 100000000000:
        cc_gdp_2[cc] = gdp
    else:
        cc_gdp_3[cc] = gdp
# See how many countries are in each level.        
wm = pygal.maps.world.World()
wm_style = pygal.style.RotateStyle("#336699",base_style=pygal.style.LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World GDP in 2010, by Country'
wm.add('0-10m', cc_gdp_1)
wm.add('10m-1bn', cc_gdp_2)
wm.add('>1bn', cc_gdp_3)
wm.render_to_file('world_GDP.svg')
