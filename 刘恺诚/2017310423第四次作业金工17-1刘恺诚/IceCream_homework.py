from Restaurant import Restaurant
from IceCreamStand import IceCreamStand

KFC=Restaurant('KFC','fastfood','12')
KFC.showPeple()

Lancys=IceCreamStand('Lancys','icecream_shop','3',['berry','wine','lemon','chocolate','vanilla'])
Miss_swiss=IceCreamStand('Miss_swiss','icecream_shop','2',['berry','wine','lemon','chocolate','oreo'])

Lancys.showName()
Lancys.showFlavors()
Miss_swiss.showName()
Miss_swiss.showFlavors()
