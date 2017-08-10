# 09.08.2017
# storing data
import json

filename = 'numbers.json'

numbers = [2, 3, 5, 7, 11, 13]
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numbers_load = json.load(f_obj)
print(numbers_load)
