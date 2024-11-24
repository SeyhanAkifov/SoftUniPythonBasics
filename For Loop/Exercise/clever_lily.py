age = int(input())
wash_machine_price  = float(input())
toy_price = float(input())

BROTHER_DISCOUNT = 1
EVEN_YEARS_BONUS = 10
toys_count = 0
cash_count = 0
cash = 0
toys_cost = 0

for i in range (1, age + 1):
    if i % 2 == 0:
        cash_count += 1
        cash += EVEN_YEARS_BONUS * cash_count
    else:
        toys_count += 1
        toys_cost += toy_price


brother_discount_sum = cash_count * BROTHER_DISCOUNT
cash = cash - brother_discount_sum
total = cash + toys_cost

if total >= wash_machine_price:
    print(f'Yes! {(total - wash_machine_price):.2f}')
else:
    print(f'No! {(wash_machine_price - total):.2f}')
