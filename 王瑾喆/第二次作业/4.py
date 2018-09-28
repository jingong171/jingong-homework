cities={
    'London':{
        'country':'england',
        'population':'8 million',
        'fact':' a beautiful city'
        },
    'Beijing':{
        'country':'china',
        'population':'20 million',
        'fact':'a large population'
        },
    'Paris':{
        'country':'france',
        'population':'2 million',

        'fact':'romantic city'
        },
    }
for cityname,city_info in cities.items():
    print("\nCityname:"+cityname)
    country=city_info['country']
    fact=city_info['fact']
    print("\tCountry:"+country.title())
    print("\tPopulation:"+city_info['population'])
    print("\tFact:"+fact.title())
    
