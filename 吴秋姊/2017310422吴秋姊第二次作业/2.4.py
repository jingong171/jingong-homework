Cities={'Urumqi':{'country':'China','population':'350 million ','fact':'Naan is one of the special food.'},
        'Munich':{'country':'Germany','population':'130 million ','fact':'Bayern Munich is famous.'},
        'New_York_City':{'country':'the United States of America','population':'860 million ','fact':'UNHQ'}}
for city,city_info in Cities.items():
    print("\nCity:"+city);
    print("Country:"+city_info['country']);
    print("Population:"+city_info['population']);
    print("Fact:"+city_info['fact']);
    
