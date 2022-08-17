import logging, os, random
from pymongo import MongoClient
clear = lambda: os.system('cls')

# Generate 10k-15k random collections of [product_id, product_name, category, price]
# Probably randomly pick a category with certain leaning to skew certain trends.
# From there Randomize the product ID, pull name and price from connected values.
# Get all and return a list of them.

def grabProduct():
    # Pre initialize vital files
    logging.basicConfig(filename = "product.log", level = logging.DEBUG, format = '%(asctime)s :: %(message)s')
    logging.info("*********************************************************")
    logging.info("Database Primed")
    client = MongoClient()
    db = client.get_database("proj2")
    
    return product_gen(15, db)

def product_gen(rng, db):

    # Scattered throughout, add in low chance for rogue data.
    # At least for testing, add number of iterations for test cases
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
            product_id = "null"
            if rng1 == 1:
                product_id = "null"
                product_name = "null"
                price = "null"
                category = "null"
                logging.info(f"null error detected.")
        elif rng1 == 2*rng2:
            product_name = "null"
        elif rng2 == 2*rng1:
            price = "null"
        # else:
        #     logging.info("No errors.")

    # Gather everything into a list and return it
    product = [product_id, product_name, category, price, 2]

    return product