# 11.07.2017
guest_list = [
    'Lao Tzu',
    'Gaius Julius Caesar',
    'Aristotle',
    'Leonardo da Vinci']
print(guest_list[0] + " you are invited to dinner.")
print(guest_list[1] + " you are invited to dinner.")
print(guest_list[2] + " you are invited to dinner.")
print(guest_list[3] + " you are invited to dinner.")
print("\n" + guest_list[2] + " can not come.")
guest_list[2] = 'Socrates'
print(guest_list[0] + " you are invited to dinner.")
print(guest_list[1] + " you are invited to dinner.")
print(guest_list[2] + " you are invited to dinner.")
print(guest_list[3] + " you are invited to dinner.")
print("\nFor the dinner will be invited three more guests.")
guest_list.insert(0, 'Plato')
guest_list.insert(3, 'Georg Wilhelm Friedrich Hegel')
guest_list.append('Immanuel Kant')
print(guest_list)
print(guest_list[0] + " you are invited to dinner.")
print(guest_list[1] + " you are invited to dinner.")
print(guest_list[2] + " you are invited to dinner.")
print(guest_list[3] + " you are invited to dinner.")
print(guest_list[4] + " you are invited to dinner.")
print(guest_list[5] + " you are invited to dinner.")
print(guest_list[6] + " you are invited to dinner.")
print("\nOnly two guests will be invited to dinner.")
print(guest_list.pop() + " I regret the cancellation of your invitation to dinner.")
print(guest_list.pop() + " I regret the cancellation of your invitation to dinner.")
print(guest_list.pop() + " I regret the cancellation of your invitation to dinner.")
print(guest_list.pop() + " I regret the cancellation of your invitation to dinner.")
print(guest_list.pop() + " I regret the cancellation of your invitation to dinner.")
print(guest_list)
print("\n" + guest_list[0] + " your invitation to dinner remained in force.")
print(guest_list[1] + " your invitation to dinner remained in force.\n")
del guest_list[0:2]    # del guest_list [:]
print(guest_list)
