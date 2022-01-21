friends = ["Michal", "Tomas", "Ivo"]
print(friends[0])

#print length of list

print(len(friends))

#list of list

#this example show how to run first element of first list in a list

friends2 = [["michal", 31], ["ivo", 34], ["tom", 24]]
print(friends2[0][0])

#add another element to list

friends3 = ["Michal", "Tomas", "Ivo"]
friends3.append("Petr")

##remove element from list
friends3.remove("Ivo")



########################### TUPLES ###############################
#Instead of list they cannot be changed (for example .append)
#are used mostly when you wanna keep them unchanded

friends = ("Michal", "Tom", "Petr")
friends = friends + ("ivo",)
print(friends)