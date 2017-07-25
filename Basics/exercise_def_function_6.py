def show_magicians(names):
    """Displays a name from the list."""
    print("Magicians: ")
    for name in names:
        print(name.title())


# def make_great(names):
#     """Added 'Great'"""
#     for name in names:
#         name2 = names.pop()
#         name2 = name2 + 'Great '
#         names.append(name)


magicians = ['phil', 'robert', 'ted']
# make_great(magicians)
show_magicians(magicians)
