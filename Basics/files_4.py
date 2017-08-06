# 06.08.2017
# writing to an empty file
filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming at Python.\n")
    file_object.write("I love creating new games.\n")
