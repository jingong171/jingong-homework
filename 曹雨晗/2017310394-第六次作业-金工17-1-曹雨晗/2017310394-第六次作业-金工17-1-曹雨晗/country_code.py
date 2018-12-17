#创建一个能够读取国别码的函数
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #如果没有找到国家，返回值为None
    return None
