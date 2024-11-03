

PRICE_FOR_ONE_METER = 7.61
DISCOUNT_PERCENT = 18 / 100

volume_to_greening = float(input())


total = volume_to_greening * PRICE_FOR_ONE_METER
discount = total * DISCOUNT_PERCENT
sum = total - discount
print(f'The final price is {sum}')
print(f'The discount is {discount}')

