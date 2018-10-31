cities={
   'Beijing':{
        'country':'China',
        'population':'20000000',
        'fact':'traditional',
        },
    'London':{
        'country':'Britian',
        'population':'7556900',
        'fact':'gentle',
        },
    'Paris':{
        'country':'France',
        'population':'2200000',
        'fact':'romantic',
        },
}

for cityname,city_info in cities.items():
    print('\nCityname:'+cityname)
    country=city_info['country']
    population=city_info['population']
    fact=city_info['fact']
    print('\tCountry:'+country.title())
    print('\tPopulatin:'+population.title())
    print('\tFact:'+fact.title())