# "epoch" = origin for time
# import time

# print()
# print(time.gmtime(0)) # utc
# print()
# print(time.localtime()) # converts utc -> local
# print()
#print(time.time()) # seconds since start of epoch
#print()
# time_here = time.localtime()
# print("Year:", time_here[0], '|', time_here.tm_year)
# print("Month", time_here[1], '|', time_here.tm_mon)
# print("Day", time_here[2], '|', time_here.tm_mday)

import time
#from time import time as my_timer  # used to convert to local time
#from time import perf_counter as my_timer # keeps utc time but more precise
#from time import monotonic as my_timer
#from time import process_time as my_timer # cpu's processing time
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer() # seconds from epoch

input("Press enter to stop")
end_time = my_timer() # seconds from epoch

print("Started at " + time.strftime("%X", time.localtime(start_time))) # %X local's appropriate time representation
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))