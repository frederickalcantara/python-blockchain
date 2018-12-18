# with open('demo.txt', mode='w') as f:
# f.write('Add this content!\n')
# file_content = f.readlines()
# f.close()

# for line in file_content:
#     print(line[:-1])
# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()
#     f.write('Testing if this closes...')
# user_input = input('Testing: ')
# print('Done!')

# with keyword automatically closes the file

import json
import pickle

# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.

"""
with open('demo.txt', mode='w') as f:
    writing = True
    while writing:
        print('Pick a number')
        print('1: Enter 1 to Say Yo')
        print('2: Enter 2 to Say Hi')
        print('F: Enter F to Write to File')
        print('Q: Enter Q to quit')
        user_input = input('Enter a key: ')
        if user_input == '1':
            print('Yo')
        if user_input == '2':
            print('Hi')
        if user_input == 'F':
            with open('demo.txt', mode='w') as f:
                written = f.write(input('Write text to add to file: '))
        if user_input == 'Q':
            writing = False
"""

# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.

"""
with open('demo.txt', mode='r') as f:
    print(f.read())
"""

# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

"""
def print_menu(text):
    print(text)
    print('A: Enter A to Add Items to a List')
    print('Q: Enter Q to Escape the program')


lists = []
writing = True
while writing:
    print_menu('Enter a letter')
    user_input = input('Enter your choice: ')
    if user_input == 'A':
        user_text = input('Add an Item to your List: ')
        lists.append(user_text)
        with open('demo.txt', mode='w') as f:
            f.write(json.dumps(lists))
        with open('demo.txt', mode='r') as f:
            file_content = json.loads(f.read())
            for line in file_content:
                print(line)
        print(lists)
    if user_input == 'Q':
        writing = False
"""

# 4) Adjust the logic to load the file content to work with pickled/ json data.


def print_menu(text):
    print(text)
    print('A: Enter A to Add Items to a List')
    print('Q: Enter Q to Escape the program')


lists = []
writing = True
while writing:
    print_menu('Enter a letter')
    user_input = input('Enter your choice: ')
    if user_input == 'A':
        user_text = input('Add an Item to your List: ')
        lists.append(user_text)
        with open('demo.p', mode='wb') as f:
            f.write(pickle.dumps(lists))
        with open('demo.p', mode='rb') as f:
            file_content = pickle.loads(f.read())
            for line in file_content:
                print(line)
        print(lists)
    if user_input == 'Q':
        writing = False
