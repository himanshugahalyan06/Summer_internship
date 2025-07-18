import datetime as dt 
import time as t

current=dt.datetime.now()
print(current)  # question 1

#question 2
date=dt.date.today()
print("Date is: ",date)

time=t.time()
print("Time is: ",time)

# formatted time 
time=t.strftime(("%H:%M:%S"))
print("Formatted Time is: ",time)

today=dt.datetime.now()
future=today + dt.timedelta(days=10) # timedelta is a class in datetime module 
print("Today: ",today)
print("Future Date (after 5 days): ",future)

