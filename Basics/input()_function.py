# 21.07.2017
# input() function
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
