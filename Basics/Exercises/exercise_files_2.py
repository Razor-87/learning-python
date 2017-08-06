# 06.08.2017
name = input("Enter your name: ")
filename = 'text_files/guest.txt'
with open(filename, 'w') as f_object:
    f_object.write(name)
