City ={
    'Ch':{
        'country':'china',
        'population':'1231565',
        'fact':'Ch'},
    'UA':{
        'country':'england',
        'population':'1652211',
        'fact':'UA'},
    'US':{
        'country':'america'
        'population':'2303203',
        'fact':'US'},
    }
for place,info in City.items():
    print('\nCity:'+place)
    print("information:")
    for key,value in value.items():
        print(key,":",value)
