from pygal_maps_world.maps import World
import json
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
    gdp_data=json.load(f)

cc_gdps={}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] ==2010:
        country_name=gdp_dict['Country Name']
        gdp=int(gdp_dict['Value'])
        code=get_country_code(country_name)
        if code:
            cc_gdps[code]=gdp
#根据gdp数值对国家进行分组
cc_gdps_1,cc_gdps_2,cc_gdps_3={},{},{}
for cc,gdp in cc_gdps.items():
    if gdp<10000000000:
        cc_gdps_1[cc]=gdp
    elif gdp<1000000000000:
        cc_gdps_2[cc]=gdp
    else:
        cc_gdps_3[cc]=gdp
#绘制世界地图
wm=World()
wm.title='World GDP in 2010'
wm.add('0-10bn',cc_gdps_1)
wm.add('10bn-1000bn',cc_gdps_2)
wm.add('>1000bn',cc_gdps_3)

wm.render_to_file('World_GDP.svg')

