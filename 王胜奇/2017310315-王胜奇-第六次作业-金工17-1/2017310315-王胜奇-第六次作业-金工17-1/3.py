# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:59:36 2018

@author: WSQ
"""

import json
import pygal
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    #Return country code#
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    return None

with open('gdp_json.json') as f:
    gdp_data=json.load(f)
#提取数据
gdp={}
for gdp_dict in gdp_data:
    if gdp_dict['Year']==2010:
        country_name=gdp_dict['Country Name']
        code=get_country_code(country_name)
        gdp=float(gdp_dict['Value'])
        if code:
            gdp[code]=gdp
    else:
    	pass
#分类
gdp_1,gdp_2,gdp_3={},{},{}
for code,value in gdps.items():
    if value<50000000000:
        gdp_1[code]=value
    elif value<5000000000000:
        gdp_2[code]=value
    else:
        gdp_3[code]=value
#画图
wm=pygal.maps.world.World()
wm.title='2010年世界经济'
wm.add('0到五百亿',gdps1)
wm.add('五百亿到五万亿',gdps2)
wm.add('大于五万亿',gdps3)
wm.render_to_file('world_gdp.svg')

