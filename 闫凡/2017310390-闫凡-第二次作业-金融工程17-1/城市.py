cities={
    'beijing':{
        'country':'china',
        'population':'21730000',
        'fact':'very big',
        },

    'hangzhou':{
        'country':'china',
        'population':'9468000',
        'fact':'very beautiful',
        },

    'zhangjiakou':{
        'country':'china',
        'population':'4433000',
        'fact':'very beautiful and it is my hometown',
        },
    }
for cityname, cityfeature in cities.items():
    print("\ncityname:\t"+cityname)
    country=cityfeature['country']
    population=cityfeature['population']
    fact=cityfeature['fact']
    print("country:\t"+country.title())
    print("population:\t"+population)
    print("fact:\t"+fact)
