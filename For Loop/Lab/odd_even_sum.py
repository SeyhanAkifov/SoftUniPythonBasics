import math

n = int(input())

odd_numbers = []
even_numbers = []


for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)


if sum(odd_numbers) != sum(even_numbers):
    print(f'No \r\nDiff = {math.fabs((sum(odd_numbers) - sum(even_numbers))):.0f}')
else:
    print(f'Yes \r\nSum = {sum(odd_numbers):.0f}')