import datetime
import random
import numpy
import pandas as pd
import calendar
from date import rdt
ecom = [
    'Amazon.com',
    'Etsy.com' ,
    'Walmart.com' ,
    'yeoldestore.com' ,
    'LarpersTrove.com' ,
    'Blacksmithery.com' ,
    'Hardhat.com '
]

columns = ['Qty_product', 'datetime', 'Ecommerece_website'] 
df= pd.DataFrame(columns= columns)
for i in range(10):
        web = random.choice(list(ecom))
        qty = random.randint(1, 10)
        df.loc[i] = [qty, rdt, web]
df.to_csv("test2.csv")
