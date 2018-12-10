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


# Dictionary comprehension
"""
stats = [('age', 24), ('weight', 240), ('height', 72)]
stats
[('age', 24), ('weight', 240), ('height', 72)]

dict_stats = {key: value for (key, value) in stats}
dict_stats
{'age': 24, 'weight': 240, 'height': 72}
"""
