friends = ["Petr", "Jirka", "Ivo"]

for friend in friends:
    print(friend)

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# _ variable is when we don't want to use this variable, and it is just used in a for loop
for _ in elements:
    print("Hello world!")

####################################################################################
students = [
    {"name": "Michal", "grade": 78},
    {"name": "Tom", "grade": 100},
    {"name": "Petr", "grade": 90}
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has grade {grade}")

########################### DESTRUCTURING SYNTAX #########################
friends = [("Petr", 30), ("Jirka", 31), ("Ivo", 34)]

for name, age in friends:
    print(f"{name} is {age} years old")

###################### How would you iterate over a dictionary's keys and values? ##################

my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}
for name, days in my_friends.items():
    print(f"I last saw {name} {days} ago")

# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

######### TEST PRACE POHOVOR ##############

list2 = [1, 2, 3, 4, 5]

for x in list2:
    y = x - 1
    z = y - 2
    val = y, z

print(val)

numbers2 = list(input("Enter some numbers: "))
for i in reversed(numbers2):
    print(i)

numbers3 = list(input("Enter some numbers: "))
print(numbers3)
numbers3.reverse()
print(numbers3)



numbers = list(input('Enter some numbers:'))
print(numbers)

def swapNumbers(numbers):

    first_item = 0
    last_item = len(numbers) - 1
    loops = len(numbers) // 2

    for i in range(loops):
        temp = numbers[first_item]
        numbers[first_item] = numbers[last_item]
        numbers[last_item] = temp
        first_item += 1
        last_item -= 1

    return numbers

print(swapNumbers(numbers))

