import random
from customer import Customer

def grabCustomer():
    '''
    grabCustomer

    Randomly selects a customer from a csv file.

    Returns a Customer object

    '''
    idx = random.randint(0,999)
    count = 0
    with open ("random_names.csv", "r", encoding="utf8") as f:
        for line in f:
            if count == idx:
                line = line.strip()
                data = line.split(',')
                return Customer(int(data[0]), data[1], data[2], data[3])
            else:
                count += 1

def grabProduct():
    '''
    grabProduct

    Randomly selects a product from the catalog
    TODO: get Ray F.'s work on this

    Returns a product (type unknown)
    
    '''
    pass

'''
with open("team1-records.csv", "w", encoding="utf8") as file:
    for i in range(10000):
        order_id = AUTOINCREMENT
        cust = grabCustomer()
        product = grabProduct()
        payment_type = ""
        qty = 0
        datetime = ""
        country = ""
        city = ""
        ecommerce_website_name = ""
        payment_txn_id = 0
        payment_txn_success = ""
        failure_reason = ""

        record = f"{order_id},{cust.nameIDString},{customer_name},{product.id},{product.name},{product.category},{payment_type},{qty},{product.price}, "
        record += f"{datetime},{cust.locationString},{ecommerce_website_name},{payment_txn_id},{payment_txn_success},{failure_reason}\n"
        file.write(record)

'''