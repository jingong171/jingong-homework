import json
import pygal
from pygal_maps_world.i18n import COUNTRIES

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
    gdp_json = json.load(f)

# Build a dictionary of population data.
#World GDP in 2010, by Country
cc_gdp={}
for gdp_dict in gdp_json:
    if gdp_dict['Year'] == 2010:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp
        else:
            print('error - ' + country_name)
wm = pygal.maps.world.World()
wm.title = 'World GDP in 2010, by Country'
wm.add('2010', cc_gdp) 
wm.render_to_file('world_gdp.svg')


# Group the countries into 3 gdp levels.
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for code, gdp in cc_gdp.items():
    if gdp > 10000000000:
        cc_gdp_1[code] = gdp
    elif gdp > 5000000000:
        cc_gdp_2[code] = gdp
    else:
        cc_gdp_3[code] = gdp

wm = pygal.maps.world.World()
wm.title = 'World GDP in 2010, by Country'
wm.add('>10bn', cc_gdp_1)
wm.add('5bn-10bn', cc_gdp_2)
wm.add('0-5bn', cc_gdp_3)
wm.render_to_file('world_gdp_group.svg')



