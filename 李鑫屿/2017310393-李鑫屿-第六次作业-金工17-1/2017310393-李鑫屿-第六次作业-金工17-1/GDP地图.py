import json
from pygal_maps_world.i18n import COUNTRIES
import pygal
import pygal.maps.world


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


filename = 'gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)
    cc_GDP = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        GDP = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_GDP[code] = GDP
cc_GDP_1, cc_GDP_2, cc_GDP_3 = {}, {}, {}
for cc, GDP in cc_GDP.items():
    if GDP < 100000000:
        cc_GDP_1[cc] = GDP
    elif GDP < 1000000000:
        cc_GDP_2[cc] = GDP
    else:
        cc_GDP_3[cc] = GDP
print(len(cc_GDP_1), len(cc_GDP_2), len(cc_GDP_3))
wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('0-100m', cc_GDP_1)
wm.add('10m-1bn', cc_GDP_2)
wm.add('>1bn', cc_GDP_3)
wm.render_to_file('world_GDP.svg')
