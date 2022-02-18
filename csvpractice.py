import csv
with open(products_list.txt) as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)