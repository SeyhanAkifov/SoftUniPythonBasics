WORKDAY_PRICES = {
    'banana': 2.50,
    'apple' : 1.20,
    'orange' : 0.85,
    'grapefruit' : 1.45,
    'kiwi' : 2.70,
    'pineapple' : 5.50,
    'grapes' : 3.85
}

WEEKEND_PRICES = {
    'banana': 2.70,
    'apple' : 1.25,
    'orange' : 0.90,
    'grapefruit' : 1.60,
    'kiwi' : 3.00,
    'pineapple' : 5.60,
    'grapes' : 4.20
}

def get_price(list, item, qty):
    return list[item] * qty

def is_valid_day(day):
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        return True
    else:
        return False

def is_valid_item(item):
    if WORKDAY_PRICES.__contains__(item) or WEEKEND_PRICES.__contains__(item):
        return True
    else:
        return False


def is_workday(day):
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        return True
    elif day in ['Saturday', 'Sunday']:
        return False
    else:
        return -1

item = input()
day = input()
qty = float(input())

if is_valid_day(day) and is_valid_item(item):
   if is_workday(day):
      print("%.2f" % get_price(WORKDAY_PRICES, item, qty))
   else:
       print("%.2f" % get_price(WEEKEND_PRICES, item, qty))
else:
   print('error')
