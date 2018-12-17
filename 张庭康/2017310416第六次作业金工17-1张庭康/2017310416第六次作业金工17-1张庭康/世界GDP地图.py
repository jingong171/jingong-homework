#引入json和pygal模块
import json
import pygal

from pygal_maps_world.i18n import COUNTRIES

filename = 'gdp_json.json'

#返回得到国别码
def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

#打开下载的文件
with open(filename)as f:
    gdp_data = json.load(f)
cc_gdp={}

#将2010年的数据筛选出来
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2010:
        country_name = gdp_dict['Country Name']
        gdp = int(gdp_dict['Value'])
        code = get_country_code(country_name)
        if code:
            cc_gdp[code]=gdp
            
#设置三个类别
cc_gdp_1 = {}
cc_gdp_2 = {}
cc_gdp_3 = {}

#将数据分别存入三个类别中
for cc,gdp in cc_gdp.items():
    if gdp<10000000000:
        cc_gdp_1[cc] = gdp
    elif gdp<100000000000:
        cc_gdp_2[cc] = gdp
    else:
        cc_gdp_3[cc] = gdp
        
#绘制地图        
wm = pygal.maps.world.World()
wm.tilte = '2010国家GDP'
wm.add('0-100b',cc_gdp_1)
wm.add('100b-1000b',cc_gdp_2)
wm.add('>1000b',cc_gdp_3)
wm.render_to_file('world_gdp.svg')
"保存为svg格式"


