is_end = False
while not is_end:
    command = input()
    if command == 'End':
        break

    destination = command
    needed_budget = float(input())
    total = 0
    while total < needed_budget:
        command = input()
        total += float(command)
        if total >= needed_budget:
            print(f'Going to {destination}!')
            break