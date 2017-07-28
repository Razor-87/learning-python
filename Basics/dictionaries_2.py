# 19.07.2017
# looping through a dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
print()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
print()

friends = ['phil', 'sarah']
for name in favorite_languages.keys():    # favorite_languages:
    print(name.title())

    if name in friends:
        print("   Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll")
print()

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\nThe following language have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\nThe following language have been mentioned:")
for language in set(favorite_languages.values()):   # set()
    print(language.title())
