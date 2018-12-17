import json
import pygal
from pygal_maps_world.i18n import COUNTRIES

#得到国家代码
def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None



# 加载数据
filename = 'gdp_json'
with open(filename) as f:
    gdp_data = json.load(f)


cc_gdp={}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2010':
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp
        else:
            print('error - ' + country_name)

# 把国家分为三个水平.
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for cc, gdp in cc_gdp.items():
    if gdp < 1E9:
        cc_gdp_1[cc] = gdp
    elif pop < 1E12:
        cc_gdp_2[cc] = gdp
    else:
        cc_gdp_3[cc] = gdp
#制图  
wm = pygal.maps.world.World()
wm_style = pygal.style.RotateStyle("#336699")
wm = pygal.maps.world.World(style=wm_style)
wm.add('0-1E9', cc_gdp_1)
wm.add('1E9-1E12', cc_gdp_2)
wm.add('>1E12', cc_gdp_3)
wm.render_to_file('world_gap.svg')


