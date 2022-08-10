# READING THE FILEe

my_file = open("/Users/zimcimic/PycharmProjects/pythonLearn/data.txt", 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

# WRITING THE FILE

user_name = input('Enter your name: ')

my_file_writing = open("/Users/zimcimic/PycharmProjects/pythonLearn/data.txt", 'w')
my_file_writing.write(user_name)

my_file_writing.close()

# COPYING THE FILE

# 1) ask the user for a list of 3 friends
# 2) For each friend, we'll tell the user whether they are nearby
# 3) For each nearby friend, we'll save their name to 'nearby_friends.txt'

# hint: readlines()

friends = input('Enter three friends names, separated by comma (no spaces, please): ').split(',')

people = open("/Users/zimcimic/PycharmProjects/pythonLearn/people.txt", 'r')
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('/Users/zimcimic/PycharmProjects/pythonLearn/nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()
