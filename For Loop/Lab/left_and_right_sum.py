import math

n = int(input())

left_numbers = []
right_numbers = []


for i in range(0, n * 2):
    if i < n:
        left_numbers.append(int(input()))
    elif i >= n:
        right_numbers.append(int(input()))


if sum(left_numbers) != sum(right_numbers):
    print(f'No, diff = {math.fabs((sum(left_numbers) - sum(right_numbers))):.0f}')
else:
    print(f'Yes, sum = {sum(left_numbers):.0f}')