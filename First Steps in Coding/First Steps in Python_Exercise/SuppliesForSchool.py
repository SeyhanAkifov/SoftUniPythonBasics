

#Пакет химикали - 5.80 лв.
#Пакет маркери - 7.20 лв.
#Препарат - 1.20 лв (за литър)

packPencilsPrice = 5.80
packMarkersPrice = 7.20
cleaningMaterialsPrice = 1.20

countOfPencils = int(input())
countOfMarkers = int(input())
littersOfCleaningMaterials = int(input())
discount = int(input())

costOfPencils = packPencilsPrice * countOfPencils
costOfMarkers = packMarkersPrice * countOfMarkers
costOfCleaningMaterials = cleaningMaterialsPrice * littersOfCleaningMaterials

totalWithouDiscount = costOfMarkers + costOfPencils + costOfCleaningMaterials
totalDiscount = totalWithouDiscount * (discount / 100)
total = totalWithouDiscount - totalDiscount

print(total)


