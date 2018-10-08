#按照题目要求创建词典：
cities={
	'Tokyo':{
	'nation':'Japan',
	'population':'13,500,000',
	'fact':'Tokyo Tower is located in Tokyo.',
	},
	'Beijing':{
	'nation':'China',
	'population':'21,730,000',
	'fact':'Forbiden City is located in Beijing.',
	},
	'City of New York':{
	'nation':'America',
	'population':'8,510,000',
	'fact':'Statue of Liberty is located in NYC.',
	},
	}

#利用循环法输出词典：
for city,items in cities.items():
	print('\nCity: '+city)
	print('\tNation: '+items['nation'])
	print('\tPopulation: '+items['population'])
	print('\tFact: '+items['fact'])
