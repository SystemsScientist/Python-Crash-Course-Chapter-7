# parrot2.py, Chapter 7, Python Crash Course
# program runs until the user enters 'quit'

prompt = "\nTell me something, and I will repeat it back to you!"
prompt += "\nEnter 'quit' to end the program: "

message = " "
while message != 'quit':
    message = input(prompt)
    print(message)



