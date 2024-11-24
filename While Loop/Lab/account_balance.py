
total = 0
is_end = False
while  is_end == False:
    in_text = input()
    if in_text == 'NoMoreMoney':
        break

    if in_text.startswith('-'):
        print('Invalid operation!')
        is_end = True
    else:
        total += float(in_text)
        print(f'Increase: {float(in_text):.2f}')



print(f'Total: {total:.2f}')