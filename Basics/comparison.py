# 13.07.2017
# comparison
car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

age = 18
print(age == 18)

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("\nHold the anchovies")

answer = 17
if answer != 42:
    print("\nThat is not the correct answer. Please try again!\n")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)
print()

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)    # (age_0 >= 21) and (age_1 >= 21)
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)
