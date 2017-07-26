def show_magicians(names):
    """Displays a name from the list."""
    print("\nMagicians: ")
    for name in names:
        print(name.title())


def make_great(names):
    """Added 'Great'"""
    for name in names:
        great = 'Great '
        name2 = names.pop()
        names.insert(0, great + name2)
    return names


magicians = ['phil', 'robert', 'ted']
magicians2 = make_great(magicians[:])

show_magicians(magicians2)
show_magicians(magicians)
