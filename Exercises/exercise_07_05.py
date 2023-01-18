# exercise_07_05.py, Chapter 7, Python Crash Course
# 
# Movie Tickets: A movie theater charges different ticket
# prices depending on a person's age. If a person is under
# the age of 3, the ticket is free; if they are between 3
# and 12, the ticket is $10; and if they are over age 12,
# the ticket is $15. Write a loop in which you ask users
# their age, and then tell them the cost of their movie
# ticket.

prompt = "\nHow old are you (press '0' to end program)?  "

active = True
while active:
    age = int(input(prompt))
    
    if age == 0:
        active = False

    if age > 0 and age < 3:
        print("Your ticket is free!")
    elif age >= 3 and age <= 12:
        print("Your ticket is $10.")
    elif age > 12:
        print("Your ticket is $15.")

print("Enjoy your movie!")



