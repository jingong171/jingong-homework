cities={'taiyuan':{'country':'china','population':'5000000','fact':'historical'},
        'Paris':{'country':'franch','population':'10000000','fact':'beauty'},
        'la':{'country':'usa','population':'12000000','fact':'happy'}
        }
for city in cities.keys():
	print (city)
	aa=cities[city]
	for mz,jt in aa.items():
                print (mz+"; "+jt)
                
