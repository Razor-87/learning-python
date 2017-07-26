man = {
    'first_name': 'john',
    'last_name': 'smit',
    'age': 30,
    'city': 'los angeles'
}

print("First name: " + man['first_name'].title())
print("Last name: " + man['last_name'].title())
print("Age: " + str(man['age']))
print("City: " + man['city'].title())
print()

favorite_numbers = {
    'anna': 55,
    'sarah': 16,
    'liza': 83,
    'jen': 67,
    'amanda': 34
}

print("Anna's favorite number: " + str(favorite_numbers['anna']))
print("Sarah's favorite number: " + str(favorite_numbers['sarah']))
print("Liza's favorite number: " + str(favorite_numbers['liza']))
print("Jen's favorite number: " + str(favorite_numbers['jen']))
print("Amanda's favorite number: " + str(favorite_numbers['amanda']))

glossary = {
    'variable': 'is something that holds a value that may change.',
    'list': 'is mutable sequences, typically \
used to store collections of homogeneous items.',
    'string': 'is immutable sequences of Unicode code points.',
    'tuple': 'is immutable sequences, typically \
used to store collections of heterogeneous data.',
    'dictionary': 'is currently only one standard mapping type.'
}

print("\nThe variable " + glossary['variable'])
print("\nThe list " + glossary['list'])
print("\nThe string " + glossary['string'])
print("\nThe tuple " + glossary['tuple'])
print("\nThe dictionary " + glossary['dictionary'])
