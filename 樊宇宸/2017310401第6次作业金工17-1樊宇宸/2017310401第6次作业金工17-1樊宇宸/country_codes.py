from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code,name in COUNTRIES.items():
        """遍历COUNTRIES寻找指定国家，返回其国别码"""
        if name==country_name:
            return code
    #如果没找到，就返回None
    return None
