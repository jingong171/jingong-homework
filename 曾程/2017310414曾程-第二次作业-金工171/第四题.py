cities={
    'Gui Yang':{
        'country':'China',
        'population':'4862000',
        'fact':'It is regarded as a forest city.',
        },
    'California':{
        'country':'America',
        'population':'112580',
        'fact':'It was named after Gergo Berkley.',
        },
    'London':{
        'country':'the UK',
        'population':'8280000',
        'fact':'It is the capital of the UK.',
        },
    }

for city,city_info in cities.items():
    print('\nCity: '+city)
    print('Country: '+city_info['country'])
    print('Population: '+city_info['population'])
    print('Fact: '+city_info['fact'])
