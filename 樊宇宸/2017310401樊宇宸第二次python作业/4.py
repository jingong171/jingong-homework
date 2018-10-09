cities={
    'Beijing':{
        'country':'China',
        'population':'2173w',
        'fact':'famous'
        },
    'Tokyo':{
        'country':'Japan',
        'population':'1350w',
        'fact':'quiet'
        },
    'Paris':{
        'country':'France',
        'population':'1100w',
        'fact':'romantic'
        }
    }
for city,information in cities.items():
    print('\nCity:'+city)
    country=information['country']
    population=information['population']
    fact=information['fact']
    print('\tCountry: '+country)
    print('\tPopulation: '+population)
    print('\tFact: '+fact)
