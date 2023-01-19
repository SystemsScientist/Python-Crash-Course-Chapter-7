# exercise_07_08.py, Chapter 7, Python Crash Course
# 
# Deli: Make a lit called sandwich_orders and fill it
# with the names of various sandwiches. Then make an
# empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for 
# each order, such as "I made your tuna sandwich". As
# each sandwich is made, move it to the list of finished
# sandwiches. After all the sandwiches have been made,
# print a message listing each sandwich that was made.

sandwich_orders = ['tuna', 'chicken', 'egg', 'seafood', 
                   'roast beef', 'grilled cheese', 'turkey']
finished_sandwiches = []

print("\nSandwiches are being made: ")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("\tMaking sandwich: " + current_sandwich.title() + " sandwich")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich.title())

print("\nAll sandwiches have been made.\n")



