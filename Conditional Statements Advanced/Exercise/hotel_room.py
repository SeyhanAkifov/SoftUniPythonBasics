HOTEL_ROOM_PRICES = {
    'Studio': {
        'May': 50.00,
        'June': 75.20,
        'July': 76.00,
        'August': 76.00,
        'September': 75.20,
        'October': 50.00
    },
    'Apartment': {
        'May': 65.00,
        'June': 68.70,
        'July': 77.00,
        'August': 77.00,
        'September': 68.70,
        'October': 65.00
    }
}

DISCOUNTS = {
    'May' : {
          7 : 0.05,
          14 : 0.30
    } ,
    'October': {
            7 : 0.05,
            14 : 0.30
    },
    'June': {
             14: 0.20,
    },
    'September': {
            14: 0.20,
    }
}

GREATER_14_DAYS_DISCOUNT = 0.10

month = input()
days = int(input())

def get_price(month, days, type):
    hotel_price = HOTEL_ROOM_PRICES[type][month]
    total_price = hotel_price * days
    discount = 0
    if days > 14 and type == 'Apartment':
       discount = GREATER_14_DAYS_DISCOUNT
    elif type == 'Studio':
        if month in ['June', 'September'] and days > 14:
            discount = DISCOUNTS[month][14]
        if month in ['June', 'September'] and days <= 14:
           pass
        elif DISCOUNTS.__contains__(month) and days > 7:
            discount_days = 7 if (14 >= days > 7) else 14
            discount = DISCOUNTS[month][discount_days]
    booking_price = total_price  - total_price * discount
    return booking_price



studio_price = get_price(month, days, 'Studio')
apartment_price = get_price(month, days, 'Apartment')

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')