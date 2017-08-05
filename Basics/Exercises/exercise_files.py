# 05.08.2017
filename = 'text_files/learning_python.txt'
with open(filename) as file_object:
    print(file_object.read())
print("---\n")

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
print("\n---\n")

with open(filename) as file_object:
    lines = file_object.readlines()
file_strings = []
for line in lines:
    file_strings.append(line.rstrip())
for string in file_strings:
    print(string)
print("\n---\n")

with open(filename) as file_object:
    lines = file_object.readlines()
file_strings = []
for line in lines:
        file_strings.append(line.replace('Python', 'C').rstrip())
for string in file_strings:
    print(string)
