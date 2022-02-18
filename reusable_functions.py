import csv

# REUSABLE FUNCTIONS
def read_csv(file_name):
    data = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
#//My version
import csv
def read_csv(csv_file_name):
    data = []
    with open(csv_file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
            #return data
    return data 
#/end of function i think
products = read_csv('products_list.csv') #variable comes from read_csv
print(products)
#//



def write_csv(file_name, data):
    with open(file_name, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def update_order(orders):
    for index, order in enumerate(orders):
        print(index, order)

    chosen_order_index = int(input("pick an order: "))

    for index, status in enumerate(statuses):
        print(index, status)

    chosen_status_index = int(input("pick a status: "))

    orders[chosen_order_index]["status"] = statuses[chosen_status_index]

    return orders


# GLOBAL VARIABLES
products = ["coke", "fanta"]
couriers = ["john"]
statuses = ["preparing", "out-for-delivery", "delivered"]
orders = read_csv("orders.csv")


# App
update_order(orders)
write_csv("orders.csv", orders)