DECOR = 10 / 100
GREATER_100_STATISTS = 10 / 100

budget = float(input())
count_of_statists = int(input())
price_of_dress_for_one_statist = float(input())

YES_MESSAGE = 'Action!\nWingard starts filming with {} leva left.'
NO_MESSAGE = 'Not enough money!\nWingard needs {} leva more.'

cost_of_decor = budget * DECOR
cost_of_dress = count_of_statists * price_of_dress_for_one_statist

if count_of_statists > 150:
     cost_of_dress = cost_of_dress - (cost_of_dress * GREATER_100_STATISTS)

total = cost_of_decor + cost_of_dress


if total <= budget:
    sum = budget - total
    print(YES_MESSAGE.format("%.2f" % sum))
else:
    sum = total - budget
    print(NO_MESSAGE.format("%.2f" % sum))
