# dictionary of str-float pairs ================================================
dict1 = {'cake': 3.99, 'muffin': 4.99, 'pizza': 2.99}
# print(dict1)


# getting the value associated with a key ======================================
# print(dict1['cake'])
# print(dict1['muffin'])


# updating the value associated with a key =====================================
# dict1['cake'] = dict1['cake'] + 1
# print(dict1)


# deleting a key-value pair ====================================================
# del dict1['cake']
# print(dict1)


# getting number of key-value pairs (dictionary size) ==========================
# print(len(dict1))


# dictionary methods ===========================================================
# print(dict1.keys())         # keys in dictionary
# print(dict1.values())       # values in dictionary
# print(dict1.items())        # view of key-value pair tuples
# print(dict1.get('muffin'))  # get value associated with the key, otherwise
# None


# get vs [] operator when a key does not exist =================================
# print(dict1.get('banana'))
# print(dict1['banana'])


# iterate over a dictionary ====================================================
# for key in list(dict1.keys()):      # can be simplified to for key in dict1:
#     print(key, '\t', dict1[key])


# dictionary of str-str pairs ==================================================
dict2 = {'BFF': 'Best Friends Forever',
         'LOL': 'Laugh Out Loud',
         'BRB': 'Be Right Back',
         'TTYL': 'Talk To You Later',
         'YOLO': 'You Only Live Once',
         'FOMO': 'Fear Of Missing Out'}

# for key in dict2:
#     print(key, '\t', dict2[key])


# dictionary of tuple-int paris ================================================
dict3 = {(0,0): 1, (1,1): 1, (2,2):1}
# print(dict3[(0,0)])
