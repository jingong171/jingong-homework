import json
import pygal
#载入GDP数据
filename='gdp_json.json'
with open(filename)as f:
    gdp_data=json.load(f)

#获取两个字母的国别码：
#首先定义一个函数：
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None
cc_gdp={}
#建立一个GDP和国别码的字典：
for gdp_dict in gdp_data:
    if gdp_dict['Year']=='2010':
        country_name=gdp_dict['Country Name']
        gdp=float(gdp_dict['Value'])
        print(country_name,gdp)
        code=get_country_code(country_name)
        if code:
            cc_gdp[code]=gdp
wm=pygal.maps.world.World()
wm.title='World GDP in 2010,by Country'
wm.add('2010,cc_gdp')
wm.reader_to_file('world_gdp.svg')
cc_gdp_1,cc_gdp_2,cc_gdp_3={},{},{}
for cc,gdp in cc_gdp.items():
    if gdp<10000000000:
        cc_gdp_1[cc]=gdp
    elif gdp<100000000000:
        cc_gdp_2[cc]=gdp
    else:
        cc_gdp_3[cc]=gdp
print(len(cc_gdp_1),len(cc_gdp_2),len(cc_gdp_3))
wm=pygal.maps.world.World()
wm.title='World GDP in 2010,by Country'
wm.add('0-100亿',cc_gdp_1)
wm.add('100亿-1000亿'，cc_gdp_2)
wm.add('1000亿以上'，cc_gdp_3)
wm.render_to_file('world_gdp.svg')

