# 20.07.2017
favorite_places = {
    'cafe': ['eric', 'john', 'ted'],
    'library': ['john', 'eric'],
    'bar': ['ted', 'john'],
}

for places, mans in favorite_places.items():
    print("\n" + places.title() + ":")
    for man in mans:
        print("\t" + man.title())

favorite_numbers = {
    'anna': [55, 334, 87],
    'sarah': [16, 44],
    'liza': [83, 98],
    'jen': [67, 36],
    'amanda': [34, 287],
}

for names, numbers in favorite_numbers.items():
    print("\n" + names.title() + "s favorite number:")
    for number in numbers:
        print("\t" + str(number))
