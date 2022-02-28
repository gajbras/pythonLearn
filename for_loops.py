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



######### TEST PRACE POHOVOR ##############

list = [1, 2, 3, 4, 5]

#Print list in reversed order

for i in reversed(list):
    print(i)

########################How to convert a list of integers into a single integer in Python##############

list_n = [1, 2, 3, 4, 5, 6]
strings_n = [str(integer) for integer in list_n]
a_string = "".join(strings_n)
an_integer = int(a_string)
print(an_integer)

