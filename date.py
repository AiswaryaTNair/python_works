#import datetime
#import pandas as pd
#def date(start,end):
    #start = input("enter the start date")
    #end = input("enter the end date")

#date_generated = pd.date_range(start, end)


#print date_generated.strftime("%d-%m-%Y")

import pandas as pd
from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = input("enter the startdate")
end_dt = input("enter the end date")
for dt in daterange(start_dt, end_dt):
    print(dt.strftime("%Y-%m-%d"))


#extract month,day and year from the dataset 
pd.to_datetime(start_dt['Date']).dt.strftime('%m/%d/%Y')
pd.to_datetime(start_dt['Date'], errors = 'coerce')

start_dt['Year'] = start_dt['Date'].dt.year
start_dt['month'] = start_dt['Date'].dt.month
start_dt['day'] = start_dt['Date'].dt.day
start_dt['time'] = start_dt['Date'].dt.time