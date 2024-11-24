import math

n = int(input())
numbers = []
is_checked = False
half_sum = 0
for i in range(0, n):
    numbers.append(int(input()))


for i in numbers:
    if sum(numbers) - i == i:
        is_checked = True
        half_sum = i
        break



if is_checked:
    print(f'Yes \r\nSum = {half_sum}')
else:
    print(f'No \r\nDiff = {math.fabs(max(numbers) - (sum(numbers) - max(numbers))):.0f}')