favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

polling = ['jen', 'phil', 'anna', 'edward', 'sarah', 'robert']
for name in polling:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for participating in the survey.\n")
    else:
        print(name.title() + ", do you want to participate in a poll" +
              "in your favorite programming language?\n")
