# 1. Create a list of dictionaries with people's name, age, and list of hobbies

people = [
    {"name": 'Fred', "age": 24, "hobbies": ['soccer', 'vg', 'code']},
    {"name": 'Sean', "age": 25, "hobbies": ['running', 'tv', 'games']},
    {"name": 'Carlos', "age": 19, "hobbies": ['fishing', 'anime', 'vg']}
]

# 2. Convert list of people into a list of names

print([person['name'] for person in people])

# 3. Check if all people are older than 20

print(all([el['age'] > 20 for el in people]))

# 4. Copy the person list to edit the name of the first person without changing the list

people_copy = [person.copy() for person in people]
people_copy[0]['name'] = 'John'
print(people_copy)
print(people)

# 5. Unpack the person list into different variable and print these variables
p1, p2, p3 = people
print(p1)
print(p2)
print(p3)
print(people)
