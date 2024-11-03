

chickenMenu = 10.35
fishMenu = 12.40
vegetarianMenu = 8.15
desertPercentWithoutDelivery = 20
delivery = 2.50

chickenMenus = int(input())
fishMenus = int(input())
vegetarianMenus = int(input())

costOfChickenMenus = chickenMenus * chickenMenu
costOfFishMenus = fishMenus * fishMenu
costOfVegetarianMenus = vegetarianMenus * vegetarianMenu
totalMenuCost = costOfVegetarianMenus + costOfFishMenus + costOfChickenMenus
costOfDesert = (desertPercentWithoutDelivery * totalMenuCost) / 100

total = totalMenuCost + costOfDesert + delivery

print("%.2f" % total)
