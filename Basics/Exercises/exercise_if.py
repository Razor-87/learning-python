alien_color = 'green'
if 'green' in alien_color:
    print("The player earned 5 points.")

alien_color = 'red'
if 'green' in alien_color:
    print("\nThe player earned 5 points.")

alien_color = 'yellow'
if 'yellow' in alien_color:
    print("\nThe player earned 5 points.")
else:
    print("\nThe player earned 10 points.")

alien_color = 'yellow'
if 'green' in alien_color:
    print("\nThe player earned 5 points.")
else:
    print("\nThe player earned 10 points.")

alien_color = 'green'
if 'green' in alien_color:
    print("\nThe player earned 5 points.")
elif 'yellow' in alien_color:
    print("\nThe player earned 10 points.")
elif 'red' in alien_color:
    print("\nThe player earned 15 points.")

alien_color = 'yellow'
if 'green' in alien_color:
    print("\nThe player earned 5 points.")
elif 'yellow' in alien_color:
    print("\nThe player earned 10 points.")
elif 'red' in alien_color:
    print("\nThe player earned 15 points.")

alien_color = 'red'
if 'green' in alien_color:
    print("\nThe player earned 5 points.")
elif 'yellow' in alien_color:
    print("\nThe player earned 10 points.")
elif 'red' in alien_color:    # else
    print("\nThe player earned 15 points.")

age = 88
if age < 2:
    print("\nThis is a child")
elif 2 <= age < 4:
    print("\nThis is a toddler")
elif 4 <= age < 13:
    print("\nThis is a kid")
elif 13 <= age < 20:
    print("\nThis is a teenager")
elif 20 <= age < 65:
    print("\nThis is an adult")
elif age >= 65:
    print("\nThis is an elder")

favorite_fruits = ['bananas', 'apples', 'pears']
if 'pears' in favorite_fruits:
    print("\nYoy really like pears!")
if 'apricots' in favorite_fruits:
    print("Yoy really like apricots!")
if 'bananas' in favorite_fruits:
    print("Yoy really like bananas!")
if 'apples' in favorite_fruits:
    print("Yoy really like apples!")
if 'cherries' in favorite_fruits:
    print("Yoy really like cherries!")
