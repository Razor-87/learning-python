man_1 = {
    'first_name': 'john',
    'last_name': 'smit',
    'age': 30,
    'city': 'los angeles'
}

man_2 = {
    'first_name': 'bred',
    'last_name': 'nelson',
    'age': 40,
    'city': 'new york'
}

man_3 = {
    'first_name': 'david',
    'last_name': 'wilson',
    'age': 20,
    'city': 'boston'
}

people = [man_1, man_2, man_3]

for man in people:
    print("\nFull name: " + man['first_name'].title() +
          " " + man['last_name'].title())
    print("Age: " + str(man['age']))
    print("City: " + man['city'].title())
