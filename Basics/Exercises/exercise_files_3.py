# 06.08.2017
filename = 'text_files/guest_book.txt'
with open(filename, 'a') as f_object:
    while True:
        print("Enter 'q' or 'quit' when you want to exit the program.")
        name = input("Enter your name: ")
        if name.lower() != 'q' and name.lower() != 'quit':
            print("Hello, " + name.title())
            f_object.write(name + "\n")
        else:
            break
