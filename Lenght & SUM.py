grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

average = total / length
print(average)

######################### EXAM ##########################

lottery_numbers = {13, 21, 22, 5, 8}

#Define a list with two players (you can come up with their names and numbers).


players = [
    {
        "name": "Michal",
        "numbers": {1, 2, 3, 4, 5}
    },
    {
        "name": "Tom",
        "numbers": {13, 5, 21, 22, 7}
    }
]


"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.
"""
name = players[0]["name"]
numbers = players[0]["numbers"].intersection(lottery_numbers)

print(format(f"Player {name} got {len(numbers)} numbers right"))

name = players[1]["name"]
numbers = players[1]["numbers"].intersection(lottery_numbers)

print(format(f"Player {name} got {len(numbers)} numbers right"))

#Remember: the string must contain the player's name and the amount of numbers they got right!
