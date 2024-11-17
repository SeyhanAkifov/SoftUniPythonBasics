flowers = {
    'Roses': 5.00,
    'Dahlias': 3.80,
    'Tulips': 2.80,
    'Narcissus': 3.00,
    'Gladiolus': 2.50
}



def flower_discount_calculate(flower, flower_qty):
    if flower == 'Roses' and flower_qty > 80:
        return flowers[flower] * flowers_qty - (flowers[flower] * flowers_qty * 0.10)
    elif flower == 'Dahlias' and flower_qty > 90:
        return flowers[flower] * flowers_qty - (flowers[flower] * flowers_qty * 0.15)
    elif flower == 'Tulips' and flower_qty > 80:
        return flowers[flower] * flowers_qty - (flowers[flower] * flowers_qty * 0.15)
    elif flower == 'Narcissus' and flower_qty < 120:
        return flowers[flower] * flowers_qty + (flowers[flower] * flowers_qty * 0.15)
    elif flower == 'Gladiolus' and flower_qty < 80:
        return flowers[flower] * flowers_qty + (flowers[flower] * flowers_qty * 0.20)
    else:
        return flowers[flower] * flowers_qty

YES_TEXT = 'Hey, you have a great garden with {} {} and {} leva left.'
NO_TEXT = 'Not enough money, you need {} leva more.'

flower = input()
flowers_qty = int(input())
budget = float(input())

flower_cost = flowers[flower] * flowers_qty
total = flower_discount_calculate(flower, flowers_qty)


if total <= budget:
    print(YES_TEXT.format(flowers_qty, flower, "%.2f" % (budget - total), ))
else:
    print(NO_TEXT.format("%.2f" % (total - budget)))





