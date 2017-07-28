# 11.07.2017
# organizing a list
cars_def = ['bmw', 'audi', 'toyota', 'subaru']
cars = cars_def[:]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = cars_def[:]
print("\nHere is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list:")
print(cars)
print()
cars.reverse()
print(cars)
cars.reverse()
print(cars)
print("\nLength of a list cars: " + str(len(cars)))    # len()
