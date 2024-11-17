budget = float(input())
season = input()
fisherman_qty = int(input())

ODD_DISCOUNT = 0.05

boat_price = {
    'Spring': 3000,
    'Summer': 4200,
    'Autumn': 4200,
    'Winter': 2600
}



price = boat_price[season]


def get_discount(cost):
    total = cost

    if fisherman_qty <= 6:
        total -= total *  0.10
    elif 7 <= fisherman_qty <= 11:
        total -= total * 0.15
    elif fisherman_qty > 11:
        total -= total * 0.25

    if fisherman_qty % 2 == 0 and season != 'Autumn':
        total -= total * ODD_DISCOUNT


    return total



price = get_discount(price)



if budget >= price:
    print(f'Yes! You have {budget - price:.2f} leva left.')
else:
    print(f'Not enough money! You need {price - budget:.2f} leva.')
