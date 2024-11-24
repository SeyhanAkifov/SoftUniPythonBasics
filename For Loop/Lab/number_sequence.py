numbers = []

n = int(input())
max_number = 0
min_number = 0
for i in range(0, n):
    num = int(input())
    if i == 0:
        min_number = num
        max_number = num

    if num > max_number:
        max_number = num

    if num < min_number:
        min_number = num
    numbers.append(num)


print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
