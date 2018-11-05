cities={'bj':{'country':'China','population':'1','fact':'a'},
	    'sh':{'country':'China','population':'2','fact':'b'},
	    'gz':{'country':'China','population':'3','fact':'c'}}
for cities_name ,cities_infor in cities.items():
    print('\nCities_name:'+cities_name)
    Country_name=cities_infor['country']
    Population=cities_infor['population']
    Fact=cities_infor['fact']

    print('\tCountry_name:'+Country_name)
    print('\tPopulation:'+Population)
    print('\tFact:'+Fact)


