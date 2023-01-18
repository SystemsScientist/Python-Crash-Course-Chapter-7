# pets.py, Chapter 7, Python Crash Course
# program removes all instances of 'cat'

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)



