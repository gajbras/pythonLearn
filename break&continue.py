cars = ["ok", "ok", "ok", "ok", "ok", "faulty", "ok", "ok", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}")

#######################################

cars = ["ok", "ok", "ok", "ok", "ok", "faulty", "ok", "ok", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found a faulty car!")
        continue
    print(f"This car is {status}")
    print("Shipping the car")