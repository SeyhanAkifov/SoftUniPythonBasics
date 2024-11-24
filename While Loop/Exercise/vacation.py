vacation_needed_money = float(input())
money_the_have = float(input())
last_money_type = ''
spend_count_in_row = 0
days = 0
cannot_save = False
have_needed_money = False

while not cannot_save and not have_needed_money:
    days += 1
    money_type = input()
    money = float(input())
    if money_type == 'spend':

        spend_count_in_row += 1
        money_the_have -= money
        if money_the_have < 0:
            money_the_have = 0
    else:
        spend_count_in_row = 0
        money_the_have += money

    last_money_type = money_type
    if spend_count_in_row == 5:
        cannot_save = True
        break

    if money_the_have >= vacation_needed_money:
        have_needed_money = True
        break

if have_needed_money:
    print(f'You saved the money for {days} days.')
else:
    print(f'You can\'t save the money.')
    print(f'{days}')