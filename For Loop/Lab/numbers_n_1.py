number = int(input())


reverse_numbers = []

for n in range(1, number + 1):
    reverse_numbers.append(n)

for n in reversed(reverse_numbers):
    print(n)