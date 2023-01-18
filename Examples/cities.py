# cities.py, Chapter 7, Python Crash Course
# program runs until the user enters 'quit'

prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break;
    else:
        print("I'd love to go to " + city.title() + "!")



