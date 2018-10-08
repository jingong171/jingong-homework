cities={
    'foshan':
    {'country':'China','population':'20万','fact':'Liukaicheng住的地方'},
    'xining':
    {'country':'China','population':'210万','fact':'Hanfeiyun的家乡'},
    'qujing':
    {'country':'China','population':'650万','fact':'Zhangingkang的家乡'}}
for city,message in cities.items():
    print("Citie is "+city )
    print("信息分别是：")
    print('country: '+message['country'])
    print('population: '+message['population'])
    print('fact: '+message['fact']+'\n')
