#pokud chceme pouzit pokazde " v nasem stringu reseni je pomoci escaping \:

string_with_quotes = "He said \"You are amazing!\""
print(string_with_quotes)

#multiline string
multiline_string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque vel magna at erat sagittis consequat vitae vel metus. 
Fusce dignissim scelerisque purus, ac suscipit libero.
"""
print(multiline_string)


name = "Michal"
greetings = "hello, " + name
print(greetings)

#string conversion

age = 31
age_as_str = str(age)

print("You are " + age_as_str)


#STRING FORMATING

#misto pouziti nize zminene funkce muzeme od verze 3.6 vyuzit nasledujici
#age = 31
#age_as_str = str(age)
#print("You are " + age_as_str)

age = 31
print(f"You are {age}")

# .format usage

name = "Jose"
final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)

#dalsi moznost formatovani

#name = "Jose"
final_greeting = f"How are you, {name}?"
jose_greeting = final_greeting.format(name="jose")
print(jose_greeting)