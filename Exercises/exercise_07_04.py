# exercise_07_04.py, Chapter 7, Python Crash Course
# 
# Pizza Toppings: Write a loop that prompts the user to enter
# a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you'll
# add that topping to their pizza.

pizza_toppings = []

prompt = "\nPlease enter the pizza topping you want. "
prompt += "\nEnter 'quit' to end the program: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        pizza_toppings.append(message) # code added for fun
        print("We added " + message + " to your pizza.")

# code added for fun
print("\nYour pizza includes the following toppings: ")
for topping in pizza_toppings[:]:
    print("\t" + topping)

print("\nYour pizza will be ready in 15 minutes!")



