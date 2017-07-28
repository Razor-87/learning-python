# 25.07.2017
# using a function with a while loop


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' or 'Q' at any time to quit)")

    f_name = input("First name: ")
    if f_name.lower() == 'q':
        break

    l_name = input("Last name: ")
    if l_name.lower() == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
