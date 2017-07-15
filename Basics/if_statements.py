# if statements / if-else / if-elif-else
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age = 19
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 3
if age < 4:
    print("\nYour admission cost is $0.")
elif age < 18:
    print("\nYour admission cost is $5.")
else:
    print("\nYour admission cost is $10.")

age = 18
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("\nYour admission cost is $" + str(price) + ".")

age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("\nYour admission cost is $" + str(price) + ".")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!")
