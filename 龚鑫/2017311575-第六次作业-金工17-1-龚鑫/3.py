import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country"""
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
        #if the country wasn't found,return none.
    return None
cc_value1={}
cc_value2={}
cc_value3={}
#Load the data into a list.
filename='gdp_json.json'
with open(filename) as f:
    pop_data=json.load(f)
    #Build a dictionary of population data.
    for pop_dict in pop_data:
        if str(pop_dict['Year']).strip()=='2010':
            country_name=pop_dict['Country Name']
            value=float(pop_dict['Value'])
            code=get_country_code(country_name)
            if code:
                if value<50000000000:
                    cc_value1[code]=value
                elif value<500000000000:
                    cc_value2[code]=value
                else:
                    cc_value3[code]=value


wm=pygal.maps.world.World()
wm.title='GDP in 2010,by Country'
wm.add('0-50b',cc_value1)
wm.add('50-500b',cc_value2)
wm.add('>500b',cc_value3)
wm.render_to_file('world_gdp.svg')
##
##wm.add('af',)

##get_country_code('China')
##a=type(COUNTRIES.items())
##print(a)
##for code,name in COUNTRIES.items():
##    print(code)
##    print(name)
