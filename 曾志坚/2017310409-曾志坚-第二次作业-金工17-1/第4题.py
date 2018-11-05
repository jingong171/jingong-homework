cities = { 'Sysney':{'country':'Australia',
                     'population':'503 million',
                     'fact':'the biggest city of Australia',},
           'Brisbane':{'country':'Australia',
                     'population':'227 million',
                     'fact':'the third biggest city of Australia',},
           'Perth':{'country':'Australia',
                     'population':'202 million',
                     'fact':'forth biggest city of Australia',},
           }
for name,information in cities.items() :
    print( name.title())
    for category,content in information.items() :
        print(category.title() + ":" + content.title())
    print("\n")
