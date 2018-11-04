cities={
    "Beijing":{"Country":"China","Populations":2.173e7,"fact":"Used to be called Beiping"},
    "Baotou":{"Country":"China","Populations":2.8777e6,"fact":"Used to be called City of deer"},
    "Shanghai": {"Country": "China", "Populations": 2.42e7, "fact": "There is a Disneyland"},
}
for keys in cities:
    print(keys,":")
    for key in cities[keys]:
        print(cities[keys][key])