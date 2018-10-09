cities={
    "beijing":{
        "country":"China",
        "population":"2.3million",
        "fact":"capital of China"},
    "new York":{
        "country":"America",
        "population":"450 thousands",
        "fact":"the economical centre of America"},
    "tokyo":{
        "country":"Japan",
        "population":"13 million",
        "fact":"capital of Japan"}
    }
for city,information in cities.items():
    print("\n"+city.title())
    country=information["country"]
    population=information["population"]
    fact=information["fact"]
    print("\tcountry: "+country)
    print("\tpopulation: "+population)
    print("\tfact: "+fact)
