cities={'Beijing':{'country':'China',
                   'population':'2170.7万',
                   'fact':'is Chinese capital'},
        'Qujing':{'country':'China',
                  'population':'652.97万',
                  'fact':'is a beautiful city!'},
        'New York':{'country':'America',
                    'population':'581万',
                    'fact':'is the biggest city of America.'}}
for city,message in cities.items():
    print("\ncity:"+city)
    print("the messsge of the city:")
    print("country:"+message['country'])
    print("population:"+message['population'])
    print("fact:"+message['fact'])


                   
