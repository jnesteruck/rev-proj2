import datetime
import random 
"""y= pd.date_range('2022-1-1', '2022-8-16', freq='D''1H', name="list.date")
for val in y:
    
    print(val)"""
def rdt():
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 8, 17)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    # print(random_date)

    hour=random.randrange(0, 23)
    minute=random.randrange(0, 60)
    sec=random.randrange(0, 60)
    rt= f'{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(sec).zfill(2)}'
    # print(rt)
    rdt = f'{random_date} {rt}'
    if random.random() < 0.005:
        rdt = f'{random_date}{rt}'
    if random.random() < 0.005:
        rdt = f'{rt} {random_date}'
    # print(rdt)
    return rdt