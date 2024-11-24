import math

resto = float(input())

coins = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00]
coins_count = 0

while  resto > 0:
     max_coin = max(coins)
     if max_coin <= resto:
         resto = round(resto - max_coin, 2)
         coins_count += 1
     else:
         coins.remove(max_coin)


print(coins_count)