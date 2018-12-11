# Manipulating Data Structures

# Rule of thumb: If you can list comprehend a data, then you can run a for loop through it

# List manipulation
"""
A list is supported for list comprehension
You can use a for loop, index, and unpack a list.

Extending list function ( list.extend( second_list ) )

simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
print(simple_list)
"""

# Looping through a dictionary
"""
A dictionary is partially supported for list comprehension, you can only get keys. Unless you use .items to grabs the keys and values of the dictionary.
You can use a for loop, index, and unpack a dictionary.
These iterables only refer to the keys unless you use a .value() or .items() function to also grab the values

converting dictionary into a tuple ( dictionary.items() ). Grab keys and values of dict

d = {'name': 'Fred'}
print(d.items())
for k, v in d.items():
    print(k, v)
"""

# Checking the index of a tuple
"""
A tuple is supported for list comprehension
You can use a for loop, index, and unpack a tuple

Checking the index of a tuple from the value ( tuple.index( value_of_tuple ) )

t = (1, 2, 3)
print(t.index(2))
"""

# Sets are a unique data set in that it only allows a single value to be the same
"""
A set is supported for list comprehension
You can use a for loop and unpack a set.
You can't index a set because it is unordered.

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
