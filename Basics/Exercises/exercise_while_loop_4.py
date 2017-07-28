# 23.07.2017
sandwich_orders = [
    'cheeseburger',
    'cheesesteak',
    'hamburger',
    'pilgrim',
    'runza',
    'fluffernutter',
]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich.title() + ".")
    finished_sandwiches.append(sandwich)
print("\nManufactured sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich.title())
