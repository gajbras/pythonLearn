age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

print(f"You can learn programming: {can_learn_programming}")


age = int(input("Enter your age:"))
usual_work = age < 18 or age > 65

print(f"at {age}, your are usually not working: {usual_work}")


name = input("Enter your name:")
surname = input("Enter your surname:")
greeting = name or f"Mr. {surname}"
print(greeting)