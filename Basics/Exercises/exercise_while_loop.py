# 21.07.2017
prompt = "\n(Enter 'quit' when you are finished.)"
prompt += "\n\tEnter the ingredients for the pizza: "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message.title() + " is included in the order.")
