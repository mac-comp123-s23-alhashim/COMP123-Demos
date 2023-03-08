from helpers.printers import *
import urllib.request

# relative file path ===========================================================
print_seperator('relative path')
file_names = open('./../data/names.txt')

# skip the first line
file_names.readline()

# print the list of names numbered starting from 1
counter = 1
for current_name in file_names:
    print(counter, '\t', current_name.strip())
    counter += 1

file_names.close()


# absolute file path ===========================================================
print_seperator('absolute path')
file_names = urllib.request.urlopen('https://raw.githubusercontent.com/mac-comp123-s23-alhashim/files/main/names.txt')

# skip the first line
file_names.readline()

# print the list of names numbered starting from 1
counter = 1
for current_name in file_names:
    print(counter, '\t', current_name.strip())
    counter += 1

file_names.close()


# context manager ==============================================================
# we frequently forgot to close resources that we used, hence context manager
# was introduced to handel these common operations
print_seperator('context manager')
with open('./../data/names.txt') as file_names:
    # skip the first line
    file_names.readline()

    # print the list of names numbered starting from 1
    counter = 1
    for current_name in file_names:
        print(counter, '\t', current_name.strip())
        counter += 1

# the following line will cause error because the file will be closed
# automatically by the context manager
# file_names.read()
