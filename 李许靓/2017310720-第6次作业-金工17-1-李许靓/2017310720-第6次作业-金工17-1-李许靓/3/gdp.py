import json
import pygal
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Return country code"""
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    return None

gdps={}
gdp1={}
gdp2={}
gdp3={}

filename='gdp_json.json'#提取相关数据
with open(filename) as f:
    gdp_data=json.load(f)

for gdp_dict in gdp_data:#提取2010年GDP数据
    if gdp_dict['Year']==2010:
        country_name=gdp_dict['Country Name']
        gdp=int(float(gdp_dict['Value']))
        code=get_country_code(country_name)
        if code:
            gdps[code]=gdp

for code,value in gdps.items():#将GDP分三类，0-10b，10b-1t,1t以上
    if value<10000000000:
        gdp1[code]=value
    elif value<1000000000000:
        gdp2[code]=value
    else:
        gdp3[code]=value

wm=pygal.maps.world.World()#pygal输出图像
wm.title='2010 World GDP,'
wm.add('0-10b',gdp1)
wm.add('10b-1t',gdp2)
wm.add('>1t',gdp3)
wm.render_to_file('WorldGdp in 2010.svg')