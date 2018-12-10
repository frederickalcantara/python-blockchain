# name = input('What is your name? ')
# age = float(input('How old are you? '))


# def print_text():
#     print(name + ' is ' + str(age))


# print_text()


# def print_sentence(first, second):
#     print(first + ' ' + second)


# print_sentence('Hello', 'World')


# def calc_decade(age):
#     decades = age // 10
#     return print('You have lived for ' + str(decades) + ' decades')


# calc_decade(24)

# names = ['Fred', 'freddyal', 'sean', 'andreas', 'sirfred']

# for name in names:
# 	print(name)
# 	print(name + ' has ' + str(len(name)) + ' characters')
# 	if len(name) > 5:
# 		print(name + ' is longer than 5 characters')
# 	if ('n' or 'N') in name:
# 		print(name + ' has an N or n in the name')

# while len(names) >= 1:
# 	names.pop()
# 	print(names)

# List comprehension
"""
simple_list = [1, 2, 3, 4]
simple_list
[1, 2, 3, 4]

doubled_list = [el * 2 for el in simple_list]
doubled_list
[2, 4, 6, 8]
"""

# List comprehension & if keyword
"""
simple_list = [1, 2, 3, 4]
dup_list = [el * 2 for el in simple_list if el % 2 == 0]

dup_list
[4, 8]

calc_items = [1, 2]
dup_list = [el * 2 for el in simple_list if el in calc_items]

dup_list
[2, 4]
"""

# Dictionary comprehension
"""
stats = [('age', 24), ('weight', 240), ('height', 72)]
stats
[('age', 24), ('weight', 240), ('height', 72)]

dict_stats = {key: value for (key, value) in stats}
dict_stats
{'age': 24, 'weight': 240, 'height': 72}
"""

# Copy a new list
"""
Original list
my_list = [1, 2, 3, 4, 5]
my_list
[1, 2, 3, 4, 5]

Copied list
dup_list = my_list[:]
dup_list[5] = 6
dup_list
[1, 2, 3, 4, 5, 6]
"""

# Range select a list
"""
Ranging a list will also copy the list

Original list
simple_list = [1, 2, 3, 4, 5]
simple_list
[1, 2, 3, 4, 5]

new_list = simple_list[0: 3]
The range selector only goes up to the last index
new_list
[1, 2, 3]

new_list = simple_list[:-1]
This range selector with a negative grabs the everything but the last value/s
new_list
[1, 2, 3, 4]
"""

# Range select a tuple
"""
Can also range a tuple because there is an order

tuple = (1, 2, 3, 4)
tuple
(1, 2, 3, 4)

tuple[0:2]
(1, 2)

tuple[:-1]
(1, 2, 3)
"""

# Cannot range a set because a set is unordered

# Cannot range a dictionary because a dictionary is unordered
