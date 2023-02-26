# list of ints
list1 = [1, 10, 16]
print(list1)


# list of strings
list2 = ['comp123', 'is', 'a', 'fun', 'course']
print(list2)


# list of mix data types
list3 = ['Temp', 2023, 3, 27, 'is', 37.1, 'F']
print(list3)


# list of lists
list4 = [list1, list2, list3]
print(list4)


# empty list
list5 = []
print(list5)


# add lists together
list6 = list1 + list2 + list3
print(list6)


# repeat lists
list7 = list1 * 3
print(list7)


# update an element in the list
list7[2] = list7[2] * 100
print(list7)


# update a portion of a list
list7[0:2] = [1.1, 2.2]
print(list7)


# remove a portion from a list
list7[0:4] = []
print(list7)


# remove a portion from a list
del list7[2:]
print(list7)


# insert element to a list
list7[1:1] = [5.5, 6.6, 7.7]
print(list7)


# alias
list8 = list7
list8[0] = 1000
print(list8)
print(list7)


# sort function
list7.sort()
print(list7)


# reverse function
list7.reverse()
print(list7)


# concatenation operator vs append function
list7 + [3]         # concatenation operator
print(list7)

list7.append(7)     # append function
print(list7)


# modifier function: modify the passed list
def change_fun(list):
    for i in range(len(list)):
        list[i] = list[i]/2


change_fun(list7)
print(list7)
