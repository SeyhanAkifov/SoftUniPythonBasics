days = [
     "Monday",
     "Tuesday",
     "Wednesday",
     "Thursday",
     "Friday",
     "Saturday",
]

hour = int(input())
day = input()

if days.__contains__(day) and 10 <= hour <= 18:
    print('open')
else:
    print('closed')
