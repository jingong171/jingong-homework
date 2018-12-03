import json
filename = "favorite_number.json"
try:
   with open(filename) as favorite_object:
      favorite_number = json.load(favorite_object)
except FileNotFoundError:
   favorite_number = input("What's your favorite number?")
   with open(filename,'w') as favorite_object:#读取#
      json.dump(favorite_number,favorite_object)#记忆#
      print("I will remember your favorite number " + favorite_number + ".")
else:
   print("Your favorite number is " + favorite_number + "!")
