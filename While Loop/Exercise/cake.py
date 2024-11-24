length = int(input())
width = int(input())

cake_volume = length * width
piece_of_cake_taken = 0
piece_of_cake = 1
is_stop_command = False
end_of_cake = False

while not is_stop_command and not end_of_cake:
    command = input()
    if command == 'STOP':
        is_stop_command = True
        break
    piece_of_cake_count = int(command)

    piece_of_cake_taken += piece_of_cake_count
    if piece_of_cake_taken >= cake_volume:
        end_of_cake = True
        break

if piece_of_cake_taken < cake_volume:
    print(f'{cake_volume - piece_of_cake_taken} pieces are left.')
else:
    print(f'No more cake left! You need {piece_of_cake_taken - cake_volume} pieces more.')
