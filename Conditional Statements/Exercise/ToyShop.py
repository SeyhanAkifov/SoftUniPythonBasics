import math
PUZZLE = 2.60
SPEAKING_PUPPY = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2
GREATER_50_PERCENT = 25 / 100
SHOP_TAX_PERCENT = 10 / 100

YES_MESSAGE = 'Yes! {} lv left.'
NO_MESSAGE = 'Not enough money! {} lv needed.'

cost_of_holiday = float(input())
count_of_puzzles = int(input())
count_of_speaking_puppies = int(input())
count_of_teddy_bears = int(input())
count_of_minions = int(input())
count_of_trucks = int(input())

count_of_toys = count_of_trucks + count_of_puzzles + count_of_minions + count_of_teddy_bears + count_of_speaking_puppies

win_from_puzzles = count_of_puzzles * PUZZLE
win_from_speaking_puppies = count_of_speaking_puppies * SPEAKING_PUPPY
win_from_teddy_bears = count_of_teddy_bears * TEDDY_BEAR
win_from_minions = count_of_minions * MINION
win_from_trucks = count_of_trucks * TRUCK

win_total = win_from_trucks + win_from_minions + win_from_puzzles + win_from_teddy_bears + win_from_speaking_puppies
discount = 0

if count_of_toys >= 50:
    discount = win_total * GREATER_50_PERCENT

total = win_total - discount

shop_tax =  total * SHOP_TAX_PERCENT

total = total - shop_tax



if total >= cost_of_holiday:
      sum = total - cost_of_holiday
      print(YES_MESSAGE.format("%.2f" % sum))
else:
      sum = cost_of_holiday - total
      print(NO_MESSAGE.format("%.2f" % sum))

