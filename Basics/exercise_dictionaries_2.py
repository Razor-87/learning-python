glossary = {
    'variable': 'is something that holds a value that may change.',
    'list': 'is mutable sequences, typically \
used to store collections of homogeneous items.',
    'string': 'is immutable sequences of Unicode code points.',
    'tuple': 'is immutable sequences, typically \
used to store collections of heterogeneous data.',
    'dictionary': 'is currently only one standard mapping type.'
}

for key, value in glossary.items():
    print("\n" + key.title() + " " + value)
