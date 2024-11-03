GRAFFIK_CARD_PRICE = 250
PROCESSOR_PRICE_PERCENT = 35 / 100
RAM_PRICE_PERCENT = 10 / 100
MORE_CARDS_DISCOUNT = 15 / 100

YES_MESSAGE = 'You have {} leva left!'
NO_MESSAGE = 'Not enough money! You need {} leva more!'


budget = float(input())
count_of_graffic_cards = int(input())
count_of_processors = int(input())
count_of_rams = int(input())

cost_of_cards = count_of_graffic_cards * GRAFFIK_CARD_PRICE
cost_of_processors = count_of_processors * (cost_of_cards * PROCESSOR_PRICE_PERCENT)
cost_of_rams = count_of_rams * (cost_of_cards * RAM_PRICE_PERCENT)

total = cost_of_rams + cost_of_processors + cost_of_cards
if count_of_graffic_cards > count_of_processors:
    total = total - (total * MORE_CARDS_DISCOUNT)

if total <= budget:
     diff = budget - total
     print(YES_MESSAGE.format("%.2f" % diff))
else:
    diff =  total - budget
    print(NO_MESSAGE.format("%.2f" % diff))
