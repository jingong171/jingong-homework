cities = {
	'beijing':{
		'contry':'China',
		'population':'21707000',
		'infomation':'capital of China'
		},
	'Istanbul':{
		'contry':'Turkey',
		'population':'15029231',
		'infomation':'Beautiful city'
		},
	'Mumbai':{
		'contry':'India',
		'population':'12442373',
		'infomation':'...'
		},
}
for city,city_info in cities.items():
	print('\ncity:'+city)
	contry = city_info['contry']
	population = city_info['population']
	infomation=city_info['infomation']
	print('\tcontry:'+contry)
	print('\tpopulation:'+population)
	print('\tinfomation:'+infomation)

