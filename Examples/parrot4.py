# parrot4.py, Chapter 7, Python Crash Course
# program runs until the user enters 'quit'

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)



