cities={
    'London':{
        'country':'England',
        'population':'8,28 million',
        'fact':'In 2012, London became the first city to have hosted three modern Summer Olympic Games.',
        },
    
    'New York':{
        'country':'America',
        'population':'8.51 million',
        'fact':'New York is the most densely populated major city in the US.',
        },
    
    'Tokyo':{
        'country':'Japan',
        'population':'13.5 million',
        'fact':"Architecture in Tokyo has largely been shaped by Tokyo's history.",
        },
    }

for city, city_info in cities.items():
    print('\nCity:'+ city)
    print('\tCountry;'+city_info['country'])
    print('\tPopulation:'+city_info['population'])
    print('\tFact:'+city_info['fact'])
