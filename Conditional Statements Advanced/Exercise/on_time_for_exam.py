exam_scheduled_time_hour = int(input())
exam_scheduled_time_minute = int(input())
arrived_time_hour = int(input())
arrived_time_minute = int(input())

convert_to_minute_exam_time = exam_scheduled_time_hour * 60 + exam_scheduled_time_minute
convert_to_minute_arrived_time = arrived_time_hour * 60 + arrived_time_minute

time_diff = convert_to_minute_exam_time - convert_to_minute_arrived_time
result2 = ''
if time_diff > 30:
    print('Early')
    result2 = 'before'
elif time_diff < 0:
    print('Late')
    result2 = 'after'
else:
    print('On time')
    result2 = 'before'

hours = abs(time_diff) // 60
minutes = abs(time_diff) % 60

def get_hours_text():
    if hours == 0:
        return f'{minutes}'
    else:
        return f'{hours}:{minutes:02d}'




result = ''

if hours > 0:
    result += get_hours_text()

    print(result + ' hours ' + result2 + ' the start')
else:
    result += get_hours_text()
    print(result + ' minutes ' + result2 +  ' the start')
