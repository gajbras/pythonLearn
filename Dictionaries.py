friend_ages = {"Michal": 31, "Tom": 24, "Petr": 30}

#adding element/key
friend_ages["Ivo"] = 34

#change attribute of key
friend_ages["Petr"] = 31

print(friend_ages["Michal"])

friend = (
    {"name": "Michal Zimcik", "age": 31},
    {"name": "Tom Zimcik", "age": 24},
    {"name": "Petr Kozmik", "age": 30}
)

print(friend[0]["name"])

#dict function = turns list of tuples to dictionary

friends = [("Mical", 31),("Tom", 24),("Ivo", 34)]
print(friends)
friend_ages = dict(friends)
print(friend_ages)
