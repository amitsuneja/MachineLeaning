import time
import random

time_here = time.localtime()
myTypeof = type(time_here)
print(myTypeof)
print("__________________")

print(time_here)
print("Year: ", time_here[0],time_here.tm_year)
print("Month: ", time_here[1], time_here.tm_mon)
print("Date:" , time_here[2], time_here.tm_mday)
print("__________________")
input("Press Enter to Start:")
print("starting..........................")
start_time = time.time()
time.sleep(random.randint(5,10))
input("Press Enter to Stop:")
print("ending.............................")
stop_time = time.time()
print("timetaken = {0} seconds".format(int(stop_time - start_time)))
print("Start Time -" + time.strftime("%X %D",time.localtime(start_time)))
print("End Time -" + time.strftime("%X %D",time.localtime(stop_time)))
# Never use time.tzname[1] if your time.daytime show you 0 which means day light saving is not enabled
print("Local TimeZone =" +  time.tzname[0])
print("Current local time :" + time.strftime("%X %D", time.localtime()))
print("Curren time in UTC :" + time.strftime("%X %D", time.gmtime()))
print("__________________")


print(time.strftime("%X", time.localtime()))
print(time.strftime("%D", time.localtime()))
print(time.strftime("%b---%d---%Y------- %H:%M:%S", time.localtime()))
print(time.strftime("%X %D", time.localtime()))

print("__________________")

# Never use time.tzname[1] if your time.daytime show you 0 which means day light saving is not enabled
print(time.daylight)
print(time.timezone)
print(time.clock())
# print(time.time_ns())