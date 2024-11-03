

shoes = 40
equip = 20
ball = 1/4
accesoires = 1/5

costOfContractForYear = int(input())

costOfShoes = costOfContractForYear - ((shoes * costOfContractForYear) / 100)
costOfEquip = costOfShoes - ((equip * costOfShoes) / 100)
costOfBall = costOfEquip / 4
costOfAcessoires = costOfBall / 5

total = costOfContractForYear + costOfAcessoires + costOfShoes + costOfBall + costOfEquip


print(total)