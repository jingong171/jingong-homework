import json
import pygal
from country_codes import get_country_code
#将GDP数据加载到列表gdp_data中
filename='gdp_json.json'
with open(filename) as f:
    gdp_data=json.load(f)
#创建一个包含gdp的字典
cc_gdp_1,cc_gdp_2,cc_gdp_3={},{},{}
for gdp_dict in gdp_data:
    """遍历gdp_data中每个字典元素，加载出其国家和gdp"""
    if gdp_dict["Year"]==2010:
        """找到2010年的数据,获取其国别码和gdp"""
        country=gdp_dict['Country Name']
        gdp=int(float(gdp_dict['Value']))
        code=get_country_code(country)
        if code:
            if gdp<10000000000:
                cc_gdp_1[code]=gdp
            elif gdp<1000000000000:
                cc_gdp_2[code]=gdp
            else:
                cc_gdp_3[code]=gdp
        else:
            print('error-'+country)

wm=pygal.maps.world.World()
wm.title='World GDP in 2010,by Country'
wm.add("0-10bn",cc_gdp_1)
wm.add("10bn-1000bn",cc_gdp_2)
wm.add(">1000bn",cc_gdp_3)
wm.render_to_file('world_gdp.svg')
