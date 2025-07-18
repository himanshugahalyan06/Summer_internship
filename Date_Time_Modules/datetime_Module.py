import datetime as dt            

#synatx --> module_name.class_name.function_name()

today=dt.date.today()
print("Today Date: ",today)
print("Year: ",today.year)
print("Month: ",today.month)
print("Day: ",today.day)

t=dt.time(14,30,45,1000)
print(t)
print("Hour: ",t.hour)
print("Minute: ",t.minute)
print("Second: ",t.second)
print("Micro-Second: ",t.microsecond)
print("Micro-Second: ",t.min)

current=dt.datetime.now()  # datetime is class also in datetime module
print(current)
print("Formatted: ",current.strftime("%Y-%m-%d %H:%M:%S"))

# String-Parsed Time Function 
date_str="2025-07-08 12:00:00" # always give time and date in this formate
date_time=dt.datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")
print("Parsed DateTime: ",date_time) # this not include microsecond by default but now will include 

today=dt.datetime.now()
future=today + dt.timedelta(days=5) # timedelta is a class in datetime module 
print("Today: ",today)
print("Future Date (after 5 days): ",future)


import time as t

current_time=t.time()
print("Time in second since epoch: ",current_time)
print("Readable Time: ",t.ctime(current_time))

# Delay Ececution 
print(" Your Time Starts Now !!")
t.sleep(3)
print("End after 3-second Time Over !!")

#use localtime and strftime

local=t.localtime()
format=t.strftime("%Y-%m-%d %H:%M:%S",local)
print("Formatted local time: ",format)





