user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We are running!")
    user_input = input("Do you wish to run the program? (yes/no): ")

print("We have stopped running ")

######################## EXAM ######################################

user_input = input("Welcome do you want to pres P and continue or Q and terminate the program?")

while user_input == "P":
    user_input = input("Do you want to run the program still?")
    if user_input == "P":
        print("Hello")
    elif user_input == "Q":
        print("We have stopped")

############### ORIGINAL FROM TEST ###################################
user_input = input("Welcome do you want to pres P and continue or Q and terminate the program?")

while user_input != "q":
    # Inside our loop, check if they typed 'p'. If they did, print "Hello"
    if user_input == "p":
        print("Hello")
    # Now we must ask the user for their input again—otherwise we would be in an infinite loop!
    user_input = input("Enter q or p: ")


i = 0
while i < 10:
    # do stuff and manipulate `i` as much as you like
    if i==5:
        i+=3

    print(i)

    # don't forget to increment `i` manually
    i += 1
