import json
import pygal_maps_world.maps
from country_codes import get_country_code

filename='gdp_json.json'
with open(filename) as f:
    gdp_data=json.load(f)

cc_gdp={} #字典用于存储国别码和gdp信息
for gdp_dict in gdp_data:
    if gdp_dict['Year']==2010: #筛选出所有2010年的数据
        country_name=gdp_dict['Country Name']
        gdp=int(float(gdp_dict['Value']))
        code=get_country_code(country_name)
        if code:
            cc_gdp[code]=gdp #国别码作为字典的键，gdp作为字典的值
            
cc_gdp_1,cc_gdp_2,cc_gdp_3={},{},{} #三个空字典用于分组
for cc,gdp in cc_gdp.items(): #遍历cc_gdp字典进行筛选
    if gdp<40000000000:
        cc_gdp_1[cc]=gdp #国别码作为字典的键，gdp作为字典的值
    elif gdp<250000000000:
        cc_gdp_2[cc]=gdp
    else:
        cc_gdp_3[cc]=gdp
        
wm=pygal_maps_world.maps.World()
wm.title='World GDP in 2010, by Country'
wm.add('0-40bn',cc_gdp_1)
wm.add('40bn-250bn',cc_gdp_2)
wm.add('>250bn',cc_gdp_3)

wm.render_to_file('world_gdp.svg')
