pizza_kinds = ['neapolitan pizza', 'chicago pizza', 'sicilian pizza']
friend_pizzas = pizza_kinds[:]
pizza_kinds.append('california pizza')
friend_pizzas.append('greek pizza')

print("My favorite pizzas are:")
for pizza in pizza_kinds:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
