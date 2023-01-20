# exercise_07_09.py, Chapter 7, Python Crash Course
# 
# No Pastrami: Using the list sandwich_orders from exercise_07_08.py,
# make sure the sandwich 'pastrami' appears in the list at least three
# times. Add code near the beginning of your program to print a
# message saying the deli has run out of pastrami, and then use a while
# loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['tuna', 'pastrami', 'chicken', 'egg', 'pastrami',
                   'seafood', 'roast beef', 'pastrami', 'turkey',
                   'pastrami', 'grilled cheese']
finished_sandwiches = []

# remove each instance of pastrami
print("\n***The Deli is out of Pastrami***")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nSandwiches are being made: ")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("\tMaking sandwich: " + current_sandwich.title() + " sandwich")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich.title())

print("\nAll sandwiches have been made.\n")



