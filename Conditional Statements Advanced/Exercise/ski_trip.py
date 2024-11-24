PRICES_FOR_ONE_NIGHT = {
    'room for one person': 18.00,
    'apartment': 25.00,
    'president apartment': 35.00
}

DISCOUNTS_GREATER_10_DAYS = {
    'apartment': 0.30,
    'president apartment': 0.10
}

DISCOUNTS_BETWEEN_10_15_DAYS = {
    'apartment': 0.35,
    'president apartment': 0.15
}

DISCOUNTS_GREATER_15_DAYS = {
    'apartment': 0.50,
    'president apartment': 0.20
}


days = int(input())
room_type = input()
rating = input()

nights = days - 1

price_for_all_nights = PRICES_FOR_ONE_NIGHT[room_type] * nights

def get_days_discount():
    if room_type == 'room for one person':
        return 0

    if nights < 10:
        return price_for_all_nights * DISCOUNTS_GREATER_10_DAYS[room_type]
    elif 10 <= nights <= 15:
        return price_for_all_nights * DISCOUNTS_BETWEEN_10_15_DAYS[room_type]
    else:
        return price_for_all_nights * DISCOUNTS_GREATER_15_DAYS[room_type]


discount_for_days = get_days_discount()

price_for_all_nights -= discount_for_days

if rating == 'positive':
    price_for_all_nights += price_for_all_nights * 0.25
else:
    price_for_all_nights -= price_for_all_nights * 0.10


print(f'{price_for_all_nights:.2f}')