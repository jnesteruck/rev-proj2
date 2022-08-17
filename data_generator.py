import random, os
from customer import Customer
from prod_gen import grabProduct
from timegen import rdt
from transact import transactionTest

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
alpha = 'qwertyuiopasdfghjklzxcvbnm'
num = '1234567890'
alphanum = alpha + num

def stringScrambler(string):
    '''
    stringScrambler

    Takes a given string and outputs a similar string
    with induced typos and errors (only uses alphanumeric
    characters).

    Returns str

    '''
    new_str = ''
    for char in string:
        chars = alphanum
        if random.random() < 0.15:
            new_str += random.choice(chars)
        new_str += char

ecom = [
    'Amazon.com',
    'Etsy.com' ,
    'Walmart.com' ,
    'yeoldestore.com' ,
    'LarpersTrove.com' ,
    'Blacksmithery.com' ,
    'Hardhat.com '
]

cred = 0
venmo = 0
google = 0
apple = 0
cApp = 0
gift = 0
paypal = 0
souls = 0
prog = 0

with open("team1-data.csv", "w", encoding="utf8") as file:
    print("Progress:")
    print("0%")
    for i in range(15000):
        new_prog = round((i + 1) / 150)
        if new_prog > prog:
            prog = new_prog
            print("\033[A                             \033[A")
            print(f'{prog}%')
        order_id = i # AUTO INCREMENT Order ID

        cust = grabCustomer() # grab customer randomly from pre-generated list

        product = grabProduct() # generate product randomly from database

        # payment info generator
        paymentInfo = transactionTest()
        payType = paymentInfo[0]
        fail_reason = paymentInfo[2]
        if payType == "Credit Card":
            pay_id = cred
            cred += 1
        elif payType == "Venmo":
            pay_id = venmo
            venmo += 1
        elif payType == "Google pay":
            pay_id = google
            google += 1
        elif payType == "Apple pay":
            pay_id = apple
            apple += 1
        elif payType == "Cash app":
            pay_id = cApp
            cApp += 1
        elif payType == "Gift card":
            pay_id = gift
            gift += 1
        elif payType == "Paypal":
            pay_id = paypal
            paypal += 1
        elif payType == "Souls of my Enemys":
            pay_id = souls
            souls += 1

        web = random.choice(list(ecom))
        qty = random.randint(1, 10)
        if random.random() < 0.005:
            qty = random.choice(alpha)
        datetime = rdt()

        if random.random() < 0.01:
            payType = stringScrambler(paymentInfo[0])

        if random.random() < 0.01:
            fail_reason = stringScrambler(paymentInfo[2])

        record = f"{order_id},{cust.nameIDString()},{product[0]},{product[1]},{product[2]},{paymentInfo[0]},{qty},{product[3]},"
        record += f"{datetime},{cust.locationString()},{web},{pay_id},{paymentInfo[1]},{fail_reason}\n"
        file.write(record)