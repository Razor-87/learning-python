# 20.07.2017
# nesting
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'huskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite languages is:")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
