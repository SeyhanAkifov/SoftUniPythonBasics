start_number = int(input())
end_number = int(input())
magic_number = int(input())
is_found = False
count = 0
result = ''
for i in range (start_number, end_number +1):
    if is_found:
        break
    for k in range(start_number, end_number + 1):
        count += 1
        if (i + k ) == magic_number:
            result = f'Combination N:{count} ({i} + {k} = {i + k})'
            is_found = True
            break


if not is_found:
    print(f'{count} combinations - neither equals {magic_number}')
else:
    print(result)
