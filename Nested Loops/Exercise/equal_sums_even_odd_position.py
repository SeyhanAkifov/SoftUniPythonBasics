start_number = int(input())
end_number = int(input())

for i in range(start_number, end_number + 1):
    odd_sum = 0
    even_sum = 0
    for k in range(len(str(i))):
        if k % 2 == 0:
            even_sum += int(str(i)[k])
        else:
            odd_sum += int(str(i)[k])

    if odd_sum == even_sum:
        print(i, end = ' ')