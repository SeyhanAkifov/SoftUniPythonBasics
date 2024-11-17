degree = float(input())
day_time = input()

outfit = ''
shoes = ''

if 10 <= degree <= 18:
    if day_time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif day_time == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < degree <= 24:
    if day_time == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif  degree >= 25:
    if day_time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

def greater_than_5(x):
    return x > 5
def less_or_equal_5(x):
    return x <= 5
v = [(greater_than_5, 1), (less_or_equal_5, 2)]


print(f'It\'s {degree:.0f} degrees, get your {outfit} and {shoes}.')


