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

# Cannot copy a complex data structure like a dictionary
"""
stats = [{'name': 'Fred'}, {'age': 24}]

stats
[{'name': 'Fred'}, {'age': 24}]

copied_stats = stats[:]

copied_stats[0]['name'] = 'Fred'

copied_stats
[{'name': 'Fred'}, {'age': 24}]

stats
[{'name': 'Fred'}, {'age': 24}]

copied_stats[0]['name'] = 'Freddyal'
copied_stats
[{'name': 'Freddyal'}, {'age': 24}]

stats
[{'name': 'Freddyal'}, {'age': 24}]
"""

# You have to copy the complex data structure element for something like a dictionary


# is vs ==, is and == have two distinct purposes. is keyword is different for objects in memory while == works because the values are the same
"""
simple_list = [1, 2, 3, 4]
second_list = [1, 2, 3, 4]

simple_list == second_list
True

simple_list is second_list
False
"""

# Manipulating Data Structures
"""
Extending list function ( list.extend( second_list ) )

simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
print(simple_list)
"""

# Looping through a dictionary
"""
converting dictionary into a tuple ( dictionary.items() ). Grab keys and values of dict

d = {'name': 'Fred'}
print(d.items())
for k, v in d.items():
    print(k, v)
"""

# Checking the index of a tuple
"""
Checking the index of a tuple from the value ( tuple.index( value_of_tuple ) )

t = (1, 2, 3)
print(t.index(2))
"""

# Sets are a unique data set in that it only allows a single value to be the same
"""
s = {'Fred', 'Andreas', 'Katie'}
print(s)
"""

# Deleting an element from a data structure
"""
The del or del() function works only with lists or dictionaries,
It will not work with tuples or sets

simple_list = [1, 2, 3, 4]
del simple_list[0]
print(simple_list)

d = {'name': 'Fred'}
del(d['name'])
print(d)

t = (1, 2, 3)
print(t.index(1))
del(t[0])
print(t)

s = {'Fred', 'Andreas', 'Katie'}
del(s['Fred'])
print(s)
"""

# all vs any keyword
"""
all checks if ALL of the items in a list match a condition to TRUE. If all of them don't, then it's FALSE

any checks if ANY of the items in a list match a condition to TRUE. If none of them don't, then it's FALSE

new_list = [True, True, False]

any(new_list)
True

all(new_list)
False

number_list = [1, 2, 3, -5]

[el for el in number_list if el > 0]
[1, 2, 3]

[el > 0 for el in number_list]

[True, True, True, False]

all([el > 0 for el in number_list])
False
"""

# Strings
"""
Strings are immutable, but are loopable like a list

You can use the format function to inject variables into a string

'I am {} and I am {} years old.'.format(name, age)

'I am Fred and I am 24 years old.'

The parameters of a .format() function are injected in the order that the variables are placed in the parameters. You can use an infinite amount of parameters in the format function

'I am {0} and I am {1} years old.'.format(name, age)

'I am 24 and I am Fred years old.'

You can put numbers in the {} to allow for manipulation in which you can decide where to place the parameters.

name = Fred
age = 24

'I am {name} and I am {years} years old.'.format(name=name, years=age)

'I am Fred and I am 24 years old.'

You can even assign variables to the parameters to name the injected variable whatever you want and decide where to place those parameters.

Check out the docs for all the manipulations that you can do with the format function

You can also directly inject variables into a string using the f character
It works just like the format function

name = Fred
age = 24

>>> f'I am {name} and I am {age} years old.'
'I am Fred and I am 24 years old.'
"""
