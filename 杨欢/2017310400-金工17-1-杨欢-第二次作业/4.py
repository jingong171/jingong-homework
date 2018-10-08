#在字典中存储字典
cities={
    'Wenzhou':{
        'Country':'China',
        'popularity':'7550000',
        'fact':'leather shoes'
        },
    'Paris':{
        'Country':'French',
        'popularity':'2240000',
        'fact':'Romanticism'
        },
    'Tokyo':{
        'Country':'Japan',
        'popularity':'37000000',
        'fact':'crowdy road'},
    }
#city_info为ciies字典的内部字典
for Key,city_info in cities.items():

    #提取内部字典的值    
    pop=city_info['popularity']
    fact=city_info['fact']

    #把字典输出为符合标准的日常语句
    print("\nCity:"+Key)
    print("\tpopularity:"+pop+"\n\tIt is famous for its "+fact+".")
