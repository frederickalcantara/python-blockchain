"""
def unlimited_arguments(*args):
    print(args)
    for argument in args:
        print(argument)


print(unlimited_arguments(*[1, 2, 3, 4]))
"""


# Unpacking function arguments
"""
You can use the * symbol in a parameter to turn a group of arguments into a tuple
It's useful for unpacking arguments to single value, works for lists & tuples

You can also use the ** in a paramter to turn loop through the keys of dictionary.
It's useful for unpacking many arguments to single value, if you use dictionaries as an arguments
"""

# 1. Write a function that accepts another function as an argument
"""
simple_list = [1, 2, 3, 4]

def multiply(el):
    return el * 4

print(list(map(multiply, simple_list)))
"""

# 2. Write a function like #1 but with a lambda function
"""
simple_list = [1, 2, 3, 4]

print(list(map(lambda el: el * 4, simple_list)))
"""

# 3. Write a function that allows for infinite arguments

"""
def multiply4(fn, *args):
    for arg in args:
        print(fn(arg))


print(multiply4(lambda x: x * 4, 1, 2, 3, 4, 5))
"""

# 4. Format output to have numbers look nice and are centered in a 20 character column

simple_list = [1, 2, 3, 4]

print('Number format: {:^20}'.format(str(simple_list)))
