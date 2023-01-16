# exercise_07_03.py, Chapter 7, Python Crash Course
# 
# Multiples of Ten: Ask the user for a number, and then report
# whether the number is a multiple of 10 or not.

number = input("Enter a number, and I'll tell you if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    if number == 0:
        print("The number " + str(number) + " is not a multiple of 10.")
    else:
        print("\nThe number " + str(number) + " is a multiple of 10.")
else:
    print("\nThe number " + str(number) + " is not a multiple of 10.")



