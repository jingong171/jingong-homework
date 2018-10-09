cities={'London':{
        'country':'British',
        'population':'8.6 million',
        'fact':'It`s the largest city In Europe'},
        'Tokyo':{
        'country':'Japan',
        'population':'37.8 million',
        'fact':'The 32nd Olympic Game will be held In there'},
        'Beijing':{
        'country':'China',
        'population':'21.7 million',
        'fact':'The capital of China'}}
for city,city_info in cities.items():
    print('\nCity:'+city)
    print('\tCountry:'+city_info['country'])
    print('\tPopulation:'+city_info['population'])
    print('\tA fact about it:'+city_info['fact'])
