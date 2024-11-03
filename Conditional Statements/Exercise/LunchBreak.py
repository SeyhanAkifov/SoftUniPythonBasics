import math
YES_MESSAGE = 'You have enough time to watch {} and left with {} minutes free time.'
NO_MESSAGE = 'You don\'t have enough time to watch {}, you need {} more minutes.'
LUNCH_TIME_DIVIDER = 8
REST_TIME_DIVIDER = 4

serial_name = input()
duration_of_serial = float(input())
duration_of_lunch_break = float(input())

lunch_time = duration_of_lunch_break / LUNCH_TIME_DIVIDER
rest_time = duration_of_lunch_break / REST_TIME_DIVIDER

rest_lunch_time = lunch_time + rest_time

needed_time = rest_lunch_time + duration_of_serial

if needed_time <= duration_of_lunch_break:
    diff = math.ceil(duration_of_lunch_break - needed_time)
    print(YES_MESSAGE.format(serial_name, "%.0f" % diff))
else:
    diff = math.ceil(needed_time - duration_of_lunch_break)
    print(NO_MESSAGE.format(serial_name, "%.0f" % diff))

