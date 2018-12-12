"""
def unlimited_arguments(*args):
    print(args)
    for argument in args:
        print(argument)


unlimited_arguments(*[1, 2, 3, 4])
"""

# Unpacking function arguments
"""
You can use the * symbol in a parameter to turn a group of arguments into a tuple
It's useful for unpacking arguments to single value, works for lists & tuples

You can also use the ** in a paramter to turn loop through the keys of dictionary.
It's useful for unpacking many arguments to single value, if you use dictionaries as an arguments
"""
