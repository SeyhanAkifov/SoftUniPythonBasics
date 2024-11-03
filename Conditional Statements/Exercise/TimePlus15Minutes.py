import math
time_hour = int(input())
time_minute = int(input())


total_time = time_hour * 60 + time_minute + 15

hours = math.floor(total_time / 60)
minutes = total_time % 60

if hours == 24:
    hours = 0

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')