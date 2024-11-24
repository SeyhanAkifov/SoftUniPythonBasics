n = int(input())

numbers = []
P1_RANGE = 200
P2_RANGE = 399
P3_RANGE = 599
P4_RANGE = 799
P5_RANGE = 800


p1_numbers = []
p2_numbers = []
p3_numbers = []
p4_numbers = []
p5_numbers = []

for i in range (0, n):
    num = int(input())
    numbers.append(num)

for item in numbers:
    if item < P1_RANGE:
        p1_numbers.append(item)
    elif P1_RANGE <= item <= P2_RANGE:
        p2_numbers.append(item)
    elif P2_RANGE < item <= P3_RANGE:
        p3_numbers.append(item)
    elif P3_RANGE < item <= P4_RANGE:
        p4_numbers.append(item)
    elif item >= P5_RANGE:
        p5_numbers.append(item)

p1_percent = len(p1_numbers) * 100 / len (numbers)
p2_percent = len(p2_numbers) * 100 / len (numbers)
p3_percent = len(p3_numbers) * 100 / len (numbers)
p4_percent = len(p4_numbers) * 100 / len (numbers)
p5_percent = len(p5_numbers) * 100 / len (numbers)


print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')