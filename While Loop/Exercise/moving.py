width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height
full_space = 0

is_full = False
is_done = False

while not is_done and not is_full:
    command = input()
    if command == 'Done':
        is_done = True
        break

    num = int(command)
    full_space += num

    if full_space >= free_space:
        is_full = True
        break

if not is_full:
    print(f'{free_space - full_space} Cubic meters left.')
else:
    print(f'No more free space! You need {full_space - free_space} Cubic meters more.')
