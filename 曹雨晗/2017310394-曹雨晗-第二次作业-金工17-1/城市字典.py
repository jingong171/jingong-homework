cities={
    'Beijing':{
        'country':'China',
        'population':'1.4 billion',
        'fact':'China has the largest population.',
        },
    'Tokyo':{
        'country':'Japan',
        'population':'0.126 billion',
        'fact':'The Japanese are very civilized.',
        },
    'Washington, D.C':{
        'country':'America',
        'population':'0.3257 billion',
        'fact':'The United States is a powerful nation.',
        },
    }
for city,city_info in cities.items():
    print("\ncity:"+city)
    country=city_info['country']
    population=city_info['population']
    fact=city_info['fact']
    print("\tCountry:"+country)
    print("\tPopulation:"+population)
    print("\tFact:"+fact)
