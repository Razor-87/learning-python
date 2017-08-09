# 09.08.2017
cats = 'text_files/cats.txt'
dogs = 'text_files/dogs.txt'
try:
    with open(cats) as f_obj:
        print("Cats:")
        lines = f_obj.readlines()
        for line in lines:
            print("\t" + line.rstrip())
except FileNotFoundError:
    # print(cats + " not found!")
    pass

try:
    with open(dogs) as f_obj:
        print("\nDogs:")
        lines = f_obj.readlines()
        for line in lines:
            print("\t" + line.rstrip())
except FileNotFoundError:
    # print("\n" + dogs + " not found!")
    pass
