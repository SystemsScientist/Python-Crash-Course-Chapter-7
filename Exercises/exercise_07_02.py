# exercise_07_02.py, Chapter 7, Python Crash Course
# 
# Restaurant Seating: Write a program that asks the user
# how many people are in their dinner group. If the answer
# is more than eight, print a message saying they'll have
# to wait for a table. Otherwise, report that their table
# is ready.

number_of_people = input("How many people are in your dinner party? ")
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("Our apologies. Your party of " + str(number_of_people) + " will need to wait for a table.")
else:
    print("Excellent! Your dinner party of " + str(number_of_people) + " may be seated right away.")



