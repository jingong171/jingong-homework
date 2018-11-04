cities={
'Beijing':{'country':'China','population':2171,'fact':'capital of China'},
'Washington':{'country':'America','population':64.6,'fact':'capital of America'},
'London':{'country':'The United Kingdom','population':828,'fact':'capital of the United Kingdom'},
}

for city,info in cities.items():
    print(city+"\ninfo:")
    print("国家："+info['country']+"，人口："+str(info['population'])+"万，事实："+info['fact']+"。")
