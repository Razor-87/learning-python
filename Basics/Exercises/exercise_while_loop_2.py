# 22.07.2017
age = "\n(Enter 'q' or 'Q' when you are finished.)"
age += "\n\tEnter your age: "

active = True
while active:
    price = input(age)
    if str(price.lower()) == 'q':
        active = False
    elif int(price) < 3:
        print("For you, admission is free.")
    elif 3 <= int(price) <= 12:
        print("For you, the ticket price is $10.")
    elif int(price) > 12:
        print("For you, the ticket price is $15.")
