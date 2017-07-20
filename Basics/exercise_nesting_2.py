pet_phil = {
    'name': 'phil',
    'kind': 'dog',
    'owner': 'john',
}

pet_dina = {
    'name': 'dina',
    'kind': 'dog',
    'owner': 'isabel',
}

pet_musya = {
    'name': 'musya',
    'kind': 'cat',
    'owner': 'piter',
}

pets = [pet_phil, pet_dina, pet_musya]
for pet in pets:
    print("\tName: " + pet['name'].title())
    print("\tKind: " + pet['kind'].title())
    print("\tOwner: " + pet['owner'].title() + "\n")

