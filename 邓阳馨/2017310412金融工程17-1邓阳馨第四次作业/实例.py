from restaurant import Restaurant

restaurant1=Restaurant('KFC','fast food')
restaurant1.number_served=100
restaurant1.describe_restaurant()
restaurant1.set_number_served()


from restaurant import IceCreamStand

icecreamstand1=IceCreamStand('Ice Queen','icecream')
icecreamstand1.describe_restaurant()
icecreamstand1.flavors=['milk','chocolate']
icecreamstand1.describe_flavor()

icecreamstand2=IceCreamStand('Ice House','icecream')
icecreamstand2.describe_restaurant()
icecreamstand2.flavors=['lemon']
icecreamstand2.describe_flavor()

