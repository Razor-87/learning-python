# 23.07.2017
dream_vavation = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where do you want to spend your vacation? ")
    dream_vavation[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in dream_vavation.items():
    print(name.title() + " wants to spend his holidays in " +
          response.title() + ".")
