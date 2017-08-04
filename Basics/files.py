# 04.08.2017
# reading from a file

with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
print("---")

filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
print("---")

filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
print("---")

filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
