# Write program to display information on the following clocks:
# time.time(), time.perf_counter(), time.monotonic(), and time.process_time()
#
# Use documentation for the get_clock_info() function to work out how to
# call it for each of the clocks.

import time

# Create the 4 clocks
clock = []
clock.append(time.time())
clock.append(time.perf_counter())
clock.append(time.monotonic())
clock.append(time.process_time())

# Get information on the 4 clocks and display them
clock_names = ['time', 'perf_counter', 'monotonic', 'process_time']
for i in range(len(clock_names)):
    print(f'{clock_names[i]}:\n\t{time.get_clock_info(clock_names[i])}\n\t{clock[i]}\n')

