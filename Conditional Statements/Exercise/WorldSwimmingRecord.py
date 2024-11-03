import math
YES_MESSAGE = 'Yes, he succeeded! The new world record is {} seconds.'
NO_MESSAGE = 'No, he failed! He was {} seconds slower.'
DELAY_IN_15_METER = 12.5

record_in_seconds = float(input())
distance_in_meters = float(input())
time_to_swim_one_meter_in_seconds = float(input())

time_to_swimm = distance_in_meters * time_to_swim_one_meter_in_seconds
delays = math.floor(distance_in_meters / 15) * DELAY_IN_15_METER

total = time_to_swimm + delays


if total < record_in_seconds:

     print(YES_MESSAGE.format("%.2f" % total))
else:
    diff =  total - record_in_seconds
    print(NO_MESSAGE.format("%.2f" % diff))