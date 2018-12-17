import json
##读取json 中的数据
filename="gdp_json.json"
with open(filename) as file:
    gdp=json.load(file)
##读取2010年的数据
gdp2010=[]
for gg in gdp:
    if gg['Year']==2010:
        gdp2010.append(gg)

from pygal_maps_world.i18n import COUNTRIES


##for i in COUNTRIES.values():
##    print(i)

##用国名取得国别码的函数
def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
##        else:
##            return '0'


##建立两位国别码的GDP字典
gdpmap={}
for country in gdp2010:
    ##如果gdp2010中的字典的国名能对的上
    ##就把它的国别码和GDP加到字典里
    name=country['Country Name']
    gdp=int(float(country['Value']))
    code=get_country_code(name)
    if code:
        gdpmap[code]=gdp

