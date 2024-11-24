
is_stop = False
max_num = float('-inf')
while is_stop == False:
    text = input()
    if text == 'Stop':
        is_stop = True
    else:
        num = int(text)
        if num > max_num:
            max_num = num

print(max_num)