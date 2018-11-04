Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> cities={
	'Beijing':{
		'country':'China',
		'population':'1.4 billion',
		'fact':'in Asia',
		},
	'New York':{
		'country':'America',
		'population':'300 million',
		'fact':'in North America',
		},
	'London':{
		'country':'the UK',
		'population':'66 million',
		'fact':'in Europe',
		},
	}
>>> for city,city_info in cities.items():
	print("\nCity:"+city)
	print("\tCountry:"+city_info['country'])
	print("\tPopulation:"+city_info['population'])
	print("\tFact:"+city_info['fact'])

	

City:Beijing
	Country:China
	Population:1.4 billion
	Fact:in Asia

City:New York
	Country:America
	Population:300 million
	Fact:in North America

City:London
	Country:the UK
	Population:66 million
	Fact:in Europe
>>> 
