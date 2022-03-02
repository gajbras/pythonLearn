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
