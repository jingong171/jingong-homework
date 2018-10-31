cities ={
    'Beijing':{
        'country':'China',
        'population':'21,730,000',
        'fact':'national capital city',
        },
    'London':{
        'country':'British',
        'population':'8,280,000',
        'fact':'Big Ben',
        },
    'New York':{
        'country':'America',
        'population':'8,510,000',
        'fact':'the Fifth Avenue',
        },
    }
for city,city_info in cities.items():
    print("\nCity: "+ city)
    print("\tCountry: "+ city_info['country'])
    print("\tPopulation: "+ city_info['population'])
    print("\tFact: "+ city_info['fact'])
