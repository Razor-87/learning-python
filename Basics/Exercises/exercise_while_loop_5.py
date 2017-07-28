# 23.07.2017
sandwich_orders = [
    'cheeseburger',
    'cheesesteak',
    'pastrami',
    'hamburger',
    'pilgrim',
    'pastrami',
    'runza',
    'fluffernutter',
    'pastrami',
]

finished_sandwiches = []

print("Pastrami is over.")

# First option:
"""
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich.title() + ".")
    finished_sandwiches.append(sandwich)
"""

# The second option:
while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
        continue
    else:
        sandwich = sandwich_orders.pop()
        print("I made your " + sandwich.title() + ".")
        finished_sandwiches.append(sandwich)

print("\nManufactured sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich.title())
