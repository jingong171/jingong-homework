cities={
    'Beijing':{
        'nation':'China',
        'population': 13000000,
        'fact':'capital',
        },
    
    'Paris':{
        'nation':'France',
        'population': 1000000,
        'fact':'Effel Tower',
        },
    
    'New York':{
        'nation':'America',
        'population': 700000,
        'fact':'NYC',
        },
    
    }
for cityname,city_info in cities.items():
    print("\nCityname:"+cityname)
    nation=city_info['nation']
    population=str(city_info['population'])
    fact=city_info['fact']
    print("\tnation:"+nation)
    print("\tpopulation:"+population)
    print("\tfact:"+fact)
    
