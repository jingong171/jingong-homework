import json
import pygal
from pygal_maps_world.i18n import COUNTRIES

#if the country has a code,return it.Otherwise return None.
def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None

# Load the data into a list.
filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)
# Build a dictionary of gdp data.
cc_gdp={}
for gdp_dict in gdp_data:
    if int(gdp_dict['Year']) == 2010:
        country_name = gdp_dict['Country Name']
        gdp = gdp_dict['Value']
        code = get_country_code(country_name)
        if code:
            cc_gdp[code]=gdp
        
# Group the countries into 3 gdp levels.
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for cc, gdp in cc_gdp.items():
    if gdp < 100000000000:
        cc_gdp_1[cc] = gdp
    elif gdp < 10000000000000:
        cc_gdp_2[cc] = gdp
    else:
        cc_gdp_3[cc] = gdp
        
# See how many countries are in each level.        
print(len(cc_gdp_1), len(cc_gdp_2), len(cc_gdp_3))

#draw a picture and save it
wm = pygal.maps.world.World()
wm.title = 'World GDP in 2010, by Country'
wm.add('0-100000000000', cc_gdp_1)
wm.add('100000000000-10000000000000', cc_gdp_2)
wm.add('>10000000000000', cc_gdp_3)
wm.render_to_file('world_gdp.svg')
