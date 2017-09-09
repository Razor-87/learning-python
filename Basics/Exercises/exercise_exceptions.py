# 09.08.2017
print("Enter two numbers, I'll put them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break
    try:
        sum_numbers = int(first_number) + int(second_number)
    except ValueError:
        print("It is necessary to enter a number!")
    else:
        print(sum_numbers)
