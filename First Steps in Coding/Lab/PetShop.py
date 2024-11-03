DOG_FOOD_PRICE = 2.50
CAT_FOOD_PRICE = 4

dog_food_packs = int(input())
cat_food_packs = int(input())

cost_of_dog_foods = dog_food_packs * DOG_FOOD_PRICE
cost_of_Cat_foods = cat_food_packs * CAT_FOOD_PRICE

total = cost_of_Cat_foods + cost_of_dog_foods

print(f'{total} lv.')
