cities={
       "Beijing":{
       "country":"China",
       "population":"21,730,000",
       "fact":"the capital of China"
       },
       "London":{
       "country":"the UK",
       "population":"8,280,000",
       "fact":"the captial of the UK"
       },
       "Tokyo":{
       "country":"Japan",
       "population":"13,500,000",
       "fact":"the captial of Japan"
       },
}
for key,value in cities.items():
	print("\n",key,":")
	for key1,value1 in value.items():
		print("\n",key1,":",value1)
