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


# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
with open('demo.txt', mode='w') as f:
    f.write(input('Write some text'))
    file_content = f.readlines()

for line in file_content:
    print(line[:-1])
line = f.readline()
while line:
    print(line)
    line = f.readline()
    f.write('Testing if this closes...')
user_input = input('Testing: ')
print('Done!')

# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.

# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

# 4) Adjust the logic to load the file content to work with pickled/ json data.
