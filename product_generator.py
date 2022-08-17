from ast import match_case
import re
import logging
from pymongo import MongoClient
import os
import random
clear = lambda: os.system('cls')

# Generate 10k-15k random collections of [product_id, product_name, category, price]
# Probably randomly pick a category with certain leaning to skew certain trends.
# From there Randomize the product ID, pull name and price from connected values.
# Get all and return a list of them.

def main():
    # Pre initialize vital files
    logging.basicConfig(filename = "product.log", level = logging.DEBUG, format = '%(asctime)s :: %(message)s')
    logging.info("*********************************************************")
    logging.info("Database Primed")
    client = MongoClient()
    db = client.get_database("Project2")
    
    database = product_gen(15000, 15, db)
    # product = [product_id, product_name, category, price]

    fname = "product_list.csv"
    with open(fname, "w") as f:
        for entry in database:
            if type(entry[3]) == type("Hi"):
                f.write(str(entry[0]) + "," + str(entry[1]) + "," + str(entry[2]) + "," + str(entry[3]) + ',\n')
            else:
                f.write(str(entry[0]) + "," + str(entry[1]) + "," + str(entry[2]) + "," + str(entry[3]) + ',\n')
    f.close()
    logging.info("Product List CSV constructed.")

def product_gen(iterations, rng, db):

    # Scattered throughout, add in low chance for rogue data.
    # At least for testing, add number of iterations for test cases

    counter = 0
    product_list = []
    for i in range(iterations):
        counter += 1

        # Randomly pick armor, weapon, or gear, setting which collection to search
        rand_collection = random.randint(1, 20)
        if (rand_collection > 0) and (rand_collection < 5):
            collection = db.Armor
            category = "Armor"
        elif (rand_collection > 4) and (rand_collection < 11):
            collection = db.Weapons
            category = "Weapons"
        else:
            collection = db.Gear
            category = "Gear"

        # Search random product id between the max and min for the selected table
        options = collection.find().sort('_id', 1).limit(1)
        for elem in options:
            low_end = int(elem.get('_id'))
        options = collection.find().sort('_id', -1).limit(1)
        for elem in options:
            high_end = int(elem.get('_id'))
        random_id = random.randint(low_end, high_end)
        #logging.info(f"Random ID {random_id} selected, loading product info...")

        # Pull and gather the related product info from the database
        product =  collection.find_one({'_id' : random_id})
        product_id = product.get('_id')
        product_name = product.get('name')
        price = product.get('cost')

        if rng != 0:
            rng1 = random.randint(1, rng)
            rng2 = random.randint(1, rng)
            if rng1 == rng2:
                product_id = random.randint(1, 100)
                if rng1 == 1:
                    product_id = "null"
                    product_name = "null"
                    price = "null"
                    category = "null"
                    logging.info("null error detected.")
            elif rng1 == 2*rng2:
                product_name = "null"
            elif rng2 == 2*rng1:
                price = random.randint(0, 10*rng) * random.random()
                price = round(price, 2)
            # else:
            #     logging.info("No errors.")

        # Gather everything into a list and return it
        product = [product_id, product_name, category, price, 2]

        # Testing log block
        # if type(price) == type("Hello"):
        #     logging.info(f"{product_name} with ID {product_id} and price {price} from category {category} selected.")
        # else:
        #     logging.info(f"{product_name} with ID {product_id} and price ${price:2f} from category {category} selected.")

        product_list.append(product)
        # use print for testing, return for implementation
        # print(str(counter) + ": " + str(product))
    
    return product_list
    
    # Second half of testing block
    # test = collection.find()
    # for elem in test:
    #     print(elem)

if __name__ == "__main__":
    main()