import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    # If the country wasn't found, return None.
    return None
filename='gdp_json.json'
with open(filename) as file:
    gdp_data=json.load(file)
    cc_gdp={}
    for gdp_dict in gdp_data:
        if int(gdp_dict['Year'])==2010:
            country_name=gdp_dict['Country Name']
            gdp=float(gdp_dict[ 'Value'])
            code=get_country_code(country_name)
            if code:
                cc_gdp[code]=gdp
#1.根据gdp将所有国家分为三组
cc_gdp_1,cc_gdp_2,cc_gdp_3={},{},{}
for cc,gdp_ in cc_gdp.items():
    if gdp_<10000000000:
        cc_gdp_1[cc]=gdp_
    if gdp_<100000000000:
        cc_gdp_2[cc]=gdp_
    else:
        cc_gdp_3[cc]=gdp_

#2.打印每个分组包含多少个国家
print(len(cc_gdp_1),len(cc_gdp_2),len(cc_gdp_3))
wm = pygal.maps.world.World()
wm.title = "2010年各国gdp总数"
wm.add('0-1000万',cc_gdp_1)
wm.add('1000万-10亿',cc_gdp_2)
wm.add('大于10亿',cc_gdp_3)
wm.render_to_file("world_gdp.svg")
