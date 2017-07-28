# 11.07.2017
# changing, addingm and removing elements
motorcycles_def = ['honda', 'yamaha', 'suzuki']
motorcycles = motorcycles_def[:]
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles = motorcycles_def[:]
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('honda')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
motorcycles = motorcycles_def[:]
print(motorcycles)
last_wned = motorcycles.pop()
print(motorcycles)
print(last_wned)
print("The last motorcycle I owned was a " + last_wned.title() + ".")
motorcycles = motorcycles_def[:]
first_owned = motorcycles.pop(0)
print(first_owned)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
motorcycles_2 = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles = motorcycles_2[:]
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = motorcycles_2[:]
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
