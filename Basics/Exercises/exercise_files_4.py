# 06.08.2017
filename = 'text_files/poll.txt'
with open(filename, 'a') as f_object:
    while True:
        print("Enter 'q' or 'quit' when you want to exit the program.")
        answer = input("Why do you like programming? ")
        if answer.lower() != 'q' and answer.lower() != 'quit':
            print("Thanks for the answer.")
            f_object.write(answer + "\n")
        else:
            break
