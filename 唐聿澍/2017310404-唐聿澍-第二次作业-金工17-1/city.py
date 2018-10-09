#城市名字，定义列表
cities = {
    'Beijing':{
        'country':'China',
        'population':'20,000,000',
        'fact':'big',
        },
        
    'London':{
        'country':'UK',
        'population':'8,300,000',
        'fact':'ease',
        },
    
    'NewYork':{
        'country':'US',
        'population':'8,500,000',
        'fact':'mess',
        },
    }

for city , infor in cities.items():#遍历城市输出
    print('Name：' + city)
    print('\tCountry：' + infor['country'])
    print('\tPopulation：' + infor['population'])
    print('\tFact：' + infor['fact'] + '\n')
