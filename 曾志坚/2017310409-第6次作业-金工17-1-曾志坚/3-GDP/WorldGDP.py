import json
import pygal
from country_codes import get_country_code

gdps={}
gdps_1,gdps_2,gdps_3={},{},{}

filename='gdp_json.json'
with open(filename) as f:
    gdp_data=json.load(f)#打开文件，提取数据

for gdp_dict in gdp_data:
    if gdp_dict['Year']==2010:#时间筛选：2010
        country_name=gdp_dict['Country Name']
        gdp=int(float(gdp_dict['Value']))
        code=get_country_code(country_name)
        if code:
            gdps[code]=gdp

for code,value in gdps.items():#将GDP分三类：0-10b，10b-1t,>1t
    if value<10000000000:
        gdps_1[code]=value
    elif value<1000000000000:
        gdps_2[code]=value
    else:
        gdps_3[code]=value

wm=pygal.maps.world.World()#显示图像
wm.title='2010 World GDP,'
wm.add('0-10b',gdps_1)
wm.add('10b-1t',gdps_2)
wm.add('>1t',gdps_3)
wm.render_to_file('world_gdp.svg')
