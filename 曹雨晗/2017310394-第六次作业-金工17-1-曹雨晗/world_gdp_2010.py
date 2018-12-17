import json
import pygal

from country_code import get_country_code

#从文件中读取信息
filename = 'gdp_json.json'

with open(filename) as f:
    gdp = json.load(f)

    
#定义一个用来存储数据的空字典
gdp_data = {}
#将符合条件的数据和国别码存储到字典中
for g in gdp:
    if g['Year'] == 2010:
        gdp_value = int(float(g['Value']))
        country_name = g['Country Name']
        code = get_country_code(country_name)
        if code:
            gdp_data[code] = gdp_value


#定义三个用来分组的空字典
gdp_data1, gdp_data2, gdp_data3 = {}, {}, {}
#将符合条件的数据分别加入到空字典中进行分组
for c, value in gdp_data.items():
    if value < 100000000000:
        gdp_data1[c] = value
    elif value < 1000000000000:
        gdp_data2[c] = value
    else:
        gdp_data3[c] = value


#进行数据的可视化
wm = pygal.maps.world.World()
wm_style = pygal.style.RotateStyle('#336699')
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World GDP in 2010, by country'
wm.add('0-100bn', gdp_data1)
wm.add('100bn-1000bn', gdp_data2)
wm.add('>1000bn', gdp_data3)
wm.render_to_file('world_gdp_2010.svg')
