cities={
    'Chengdu':{
        'country':'China',
        'population':'1604.47万',
        'fact':'capital of Sichuan Province',
        },
    'Tokyo':{
        'country':'Japan',
        'population':'4200万',
        'fact':'capital city of Japan',
        },
    'Madrid':{
        'country':'Spain',
        'population':'452万',
        'fact':'capital of Spain',
        },
    }
for city,city_information in cities.items():
    print("City:"+city)
    print("\tCountry:"+city_information['country'])
    print("\tPopulation:"+city_information['population'])
    print("\tFact:"+city_information['fact'])
          
