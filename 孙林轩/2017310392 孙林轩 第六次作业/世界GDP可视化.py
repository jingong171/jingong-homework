import pygal_maps_world.maps as pmw
import json
from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None
with open('C:/Users/孙林轩/Desktop/gdp_json.json') as gdpF:
       data=json.load(gdpF)
       indexnum=[]
       for i in range(0,len(data)):
              if data[i]['Year']==2010:
                     indexnum.append(i)
wm=pmw.World()
wm.title = 'World map'
GDP_dic={}
for i in indexnum:
       GDP_dic[get_country_code(data[i]["Country Name"])]=data[i]['Value']
GDP1={}
GDP2={}
GDP3={}
for code,value in GDP_dic.items():
       if value<(1/3)*max(GDP_dic.values()):
              GDP1[code]=value
       elif value<(2/3)*max(GDP_dic.values()):
              GDP2[code]=value
       else:
              GDP3[code]=value
wm.add('2010 GDP under 1/3',GDP1)
wm.add('2010 GDP under 2/3',GDP2)
wm.add('2010 GDP developed',GDP3)
wm.render_to_file('na_populations.svg')

