#装库
import json
import pygal
from pygal_maps_world.i18n import COUNTRIES

#获取国别码
def get_country_code(country_name):
    """Return country code"""
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    return None

gdps={}
gdps_1={}
gdps_2={}
gdps_3={}

#提取相关数据
filename='gdp_json.json'
with open(filename) as f:
    gdp_data=json.load(f)
    
#提取2010年GDP数据
for gdp_dict in gdp_data:
    if gdp_dict['Year']==2010:
        country_name=gdp_dict['Country Name']
        gdp=int(float(gdp_dict['Value']))
        code=get_country_code(country_name)
        if code:
            gdps[code]=gdp
            
#GDP分三类，0-10b，10b-1t,1t以上
for code,value in gdps.items():
    if value<10000000000:
        gdps_1[code]=value
    elif value<1000000000000:
        gdps_2[code]=value
    else:
        gdps_3[code]=value

#pygal输出图像
wm=pygal.maps.world.World()
wm.title='2010 World GDP,'
wm.add('0-10b',gdps_1)
wm.add('10b-1t',gdps_2)
wm.add('>1t',gdps_3)
wm.render_to_file('WorldGdp.svg')
