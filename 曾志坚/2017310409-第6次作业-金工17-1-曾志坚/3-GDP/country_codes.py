##import json
##
##filename='population_data.json'
##
##with open(filename)as f:
##    pop_data=json.load(f)
##for pop_dict in pop_data:
##    if pop_dict['Year']=='2010':
##        country_name=pop_dict['Country Name']
##        population=float(pop_dict['Value'])
##        print(country_name,population)

from pygal_maps_world.i18n import COUNTRIES
##for country_code in sorted(COUNTRIES.keys()):
##    print(country_code,COUNTRIES[country_code])

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

##print(get_country_code("Andorra"))
##print(get_country_code("United Arab Emirates"))
##print(get_country_code("Afghanistan"))
