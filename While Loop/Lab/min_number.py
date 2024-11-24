is_stop = False
min_num = float('inf')
while not is_stop:
    text = input()
    if text == 'Stop':
        is_stop = True
    else:
        num = int(text)
        if num < min_num:
            min_num = num

print(min_num)