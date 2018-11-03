cities = {
    'New York':{
        'country':'USA',
        'population':8510000,
        'fact':"The biggest city in USA",
        },
    'Paris':{
        'country':'France',
        'population':11000000,
        'fact':"The capital of France",
        },
    'Florence':{
        'country':'Italy',
        'population':379100,
        'fact':"The centre of Renaissance",
        },
    }
for city,city_info in cities.items():
    print("\nCity: "+city)
    Country = city_info['country']
    Population = city_info['population']
    Fact = city_info['fact']
    print("\tCountry: "+Country)
    print("\tPopulation: "+str(Population))
    print("\tFact: "+Fact)
