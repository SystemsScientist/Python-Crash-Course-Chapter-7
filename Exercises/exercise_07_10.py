# exercise_07_10.py, Chapter 7, Python Crash Course
# 
# Dream Vacation: Write a program that polls users
# about their dream vacation. Write a prompt similar
# to "If you could visit one place in the world, 
# where would you go?" Include a block of code that
# prints the results of the poll.

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    location = input("If you could visit one place in the world, " +
                     "\nwhere would you go? ")

    responses[name] = location

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, location in responses.items():
    print(name + " would like to visit " + location + ".")
print("\n")



