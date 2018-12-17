import json
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code
# 将数据加载到列表中
filename = 'gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)
# 创建一个关于世界GDP的字典
cc_GDP= {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        GDP = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_GDP[code] = GDP
#依据GDP将国家划分为三个等级
cc_GDP_1, cc_GDP_2, cc_GDP_3 = {}, {}, {}
for cc, GDP in cc_GDP.items():
    if GDP < 20000000000:
        cc_GDP_1[cc] = GDP
    elif GDP < 100000000000:
        cc_GDP_2[cc] = GDP
    else:
        cc_GDP_3[cc] = GDP
#打印出每一个层级的国家个数       
print(len(cc_GDP_1), len(cc_GDP_2), len(cc_GDP_3))

wm_style = RS('#336699', base_style=LCS)
wm = pygal.Worldmap(style=wm_style)
wm.title = 'World GDP in 2010, by Country'
wm.add('0-20bn', cc_GDP_1)
wm.add('20bn-1100bn', cc_GDP_2)
wm.add('>100bn', cc_GDP_3)
    
wm.render_to_file('world_GDP.svg')
