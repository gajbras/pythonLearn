#don`t hold order and set's dont contain duplicate elements

art_friends = {"Michal", "Tom", "Petr"}
science_friends = {"Petr", "Jirka"}

art_no_science = art_friends.difference(science_friends)
science_no_art = science_friends.difference(art_friends)
print(art_no_science)
print(science_no_art)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

all_friend = art_friends.union(science_friends)
print(all_friend)

#### EXAMPLE

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend

friend = input("Enter name of the friend: ")
# Add the name to the empty set

user_friends.add(friend)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print(user_friends.intersection(nearby_people))