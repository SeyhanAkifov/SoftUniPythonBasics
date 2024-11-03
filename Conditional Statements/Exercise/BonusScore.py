start_points = int(input())

LESS_OR_EQUAL_100_POINTS = 5
GREATER_100_AND_LESS_OR_EQUAL_1000_POINTS_PERCENT = 20  / 100
GREATER_1000_POINTS_PERCENT = 10 / 100
ODD_NUMBER_POINTS = 1
ENDS_WITH_5_POINTS = 2

bonus = 0.0
if start_points % 2 == 0:
    bonus += ODD_NUMBER_POINTS

if start_points % 10 == 5:
    bonus += ENDS_WITH_5_POINTS

if start_points <= 100:
    bonus += LESS_OR_EQUAL_100_POINTS
elif 100 < start_points <= 1000:
    bonus += start_points * GREATER_100_AND_LESS_OR_EQUAL_1000_POINTS_PERCENT
elif  start_points > 1000:
    bonus += start_points * GREATER_1000_POINTS_PERCENT



total = start_points + bonus


print(bonus)
print(total)


