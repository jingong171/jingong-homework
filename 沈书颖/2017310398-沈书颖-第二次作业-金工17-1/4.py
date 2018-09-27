cities={
    'Beijing':{'country':'China','population':'21730000','fact':'It has a long history.'},
    'London':{'country':'England','population':'8280000','fact':'It has The London Eye.'},
    'NYC':{'country':'America','population':'8510000','fact':'It is a international metropolis.'}}
#创建字典中嵌套字典的信息
for city_name,city_info in cities.items():
	print(city_name + " is in " + city_info['country'] + " with population of " + city_info['population'] + ".")
	print(city_info['fact'])
#打印信息成完整的句子
