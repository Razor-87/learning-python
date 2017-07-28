# 26.07.2017
# passing an arbitrary number of arguments


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


def make_pizza_2(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

make_pizza_2(16, 'pepperoni')
make_pizza_2(12, 'mushrooms', 'green peppers', 'extra cheese')
