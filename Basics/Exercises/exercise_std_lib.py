# 03.08.2017
from collections import OrderedDict

glossary = OrderedDict()
glossary['variable'] = 'is something that holds a value that may change.'
glossary['list'] = 'is mutable sequences, typically \
used to store collections of homogeneous items.'
glossary['string'] = 'is immutable sequences of Unicode code points.'
glossary['tuple'] = 'is immutable sequences, typically \
used to store collections of heterogeneous data.'
glossary['dictionary'] = 'is currently only one standard mapping type.'

for key, value in glossary.items():
    print("\n" + key.title() + " " + value)
