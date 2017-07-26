usernames = ['john11', 'user99', 'admin', 'tester55', 'guest22']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("\nHello Admin, would you like to see a status report?")
        else:
            print("\nHello " + username.title() +
                  ", thank you for logging in again.")
else:
    print("We need to find some users!")
