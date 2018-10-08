Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> cities={
	"BEIJING":{
		"population":"21730000",
		"name":"BEIJING",
		"country":"China",
		"fact":"capital",
		},
        "SHANGHAI":{
		"population":"14395000",
		"name":"SHANGHAI",
		"country":"China",
		"fact":"finance center"
		},
	"HONGKONG":{
		"population":"7264000",
		"name":"HONGKONG",
		"country":"China",
		"fact":"SAR",
		},
	}
>>> for c_name,c_info in cities.items():
	print(c_name)
	for key,value in c_info.items():
		print('\t'+key+':',end='')
		print(value)

		
BEIJING
	population:21730000
	name:BEIJING
	country:China
	fact:capital
SHANGHAI
	population:14395000
	name:SHANGHAI
	country:China
	fact:finance center
HONGKONG
	population:7264000
	name:HONGKONG
	country:China
	fact:SAR
>>> 
