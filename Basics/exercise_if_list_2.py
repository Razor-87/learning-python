current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['USER1', 'user8', 'user7', 'User3', 'user9']
for user in new_users:
    user = user.lower()
    if user in current_users:
        print("\n" + user + ": You must enter a new username.")
    else:
        print("\n" + user + ": This name is suitable.")
