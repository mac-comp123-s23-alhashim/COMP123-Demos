"""
@Auther: Amin G. Alhashim (aalhashi@macalester.edu)
"""

# using the built-in module to read and store as list of list
dataset_list = []
with open("./data/carvana.csv") as dataset_file:
    dataset_file.readline()
    for record in dataset_file:
        dataset_list.append(record.strip().split(','))

print(dataset_list)



# using the csv module
import csv
with open("./data/carvana.csv") as dataset:
    reader = csv.DictReader(dataset)

    field_names = reader.fieldnames
    print(field_names)

    for row in reader:
        print(row)
