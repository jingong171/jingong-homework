import json
import pygal
import pygal_maps_world.maps
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None
filename='gdp_json.json'
with open(filename) as f:
    pop_data=json.load(f)

cc_gdp={}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        gdp = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp
        else:
            print('error - ' + country_name)

cc_gdps_1, cc_gdps_2, cc_gdps_3 = {}, {}, {}
for cc, g in cc_gdp.items():
    if g < 10000000000:
        cc_gdps_1[cc] = g
    elif g < 100000000000:
        cc_gdps_2[cc] = g
    else:
        cc_gdps_3[cc] = g

wm = pygal.maps.world.World()
wm.title = 'World gdp in 2010, by Country'
wm.add('0-10b', cc_gdps_1)
wm.add('10b-100bn', cc_gdps_2)
wm.add('>100bn', cc_gdps_3)
wm.render_to_file('world_gdp_groups.svg')
