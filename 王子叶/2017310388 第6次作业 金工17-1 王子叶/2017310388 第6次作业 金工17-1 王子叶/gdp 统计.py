import json
import pygal #读取json文件中的数值和图#
from pygal_maps_world.il8n import COUNTRIES #地图引入#
filename="gdp.json"
with open(filename)as f:
    gdp_data=json.load(f)
    for gdp_dict in gdp_data:
        if gdp_dict["year"]=="2010"
        country_name=gdp_dict["country name"]
        gdp=float(gdp_dict["value"])
def get_country_code(country_name):#国别码#
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
        else:
            return None
from country_codes import get_country_code
code=get_country_code(country_name)
if code:
    print(code,gdp)
eles:
    print("error-"+country_name)
cc_gdp={}
if code:
    cc_gdp[code]=gdp
#创建分类#
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for cc, gdp in cc_gdp.items():
    if gdp < 10000000000000:
        cc_gdp_1[cc] = gdp
    elif pop < 20000000000000:
        cc_gdp_2[cc] = gdp
    else:
        cc_gdp_3[cc] = gdp
print(len(cc_gdp_1), len(cc_gdp_2), len(cc_gdp_3))
wm = pygal.maps.world.World()
wm.title = 'World GDP in 2010, by Country'
wm.add('0~10000000000000', cc_gdp_1)
wm.add('10000000000000~20000000000000', cc_gdp_2)
wm.add('>20000000000000', cc_gdp_3)
wm.render_to_file('world_gdp.svg')



