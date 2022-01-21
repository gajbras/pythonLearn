friend = "tom"
user_name = input("Enter your friends name: ")

if user_name == friend:
    print("Hello, friend")
else:
    print("Hello Stranger")

#This print will run because it is not a part of if Stat

print("This runs too")


#################################################################

name = input("Enter your name: ")

print(bool(name))

if name:
    print("We know your name")

##################################################################

friends = ["Petr", "Jirka", "Ivo"]
family = ["Michal", "Tom"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello friend!")
elif user_name in family:
    print("Hello family!")
else:
    print("I dont know you")