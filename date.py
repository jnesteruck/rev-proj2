import datetime
import pandas as pd
import random 
"""y= pd.date_range('2022-1-1', '2022-8-16', freq='D''1H', name="list.date")

for val in y:
    
    print(val)"""

start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 8, 17)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)

print(random_date)

hour=random.randrange(1, 12)
minute=random.randrange(0, 60)
pmOrAm=random.choice(["A.M.","P.M."])
rt= f'{hour}:{minute}{pmOrAm}'
print(rt)
rdt = f'{random_date} {rt}'
print(rdt)