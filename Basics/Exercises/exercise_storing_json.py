# 11.08.2017
import json

filename = 'fav_number.json'
try:
    with open(filename) as f_obj:
        fav_number = json.load(f_obj)
except FileNotFoundError:
    fav_number = input("Enter your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(fav_number, f_obj)
else:
    print("I know your favorite number! It's " + fav_number + "!")
