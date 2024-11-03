

safetyPlatesPerMeterPrice = 1.50
paintPerLitterPrice = 14.50
paintThinnerPerLiterPrice = 5.00

additionalPaintPercent = 10
additionalPlatesMeter = 2
bag = 0.40
costOfWorkersPercent = 30

volumeOfPlates = float(input())
litersOfPaints = float(input())
litersOfThinners = float(input())
workHours = float(input())


costOfPlates = (volumeOfPlates + additionalPlatesMeter) * safetyPlatesPerMeterPrice
costOfPaints = (litersOfPaints + ((additionalPaintPercent * litersOfPaints) / 100)) * paintPerLitterPrice
costOfThinners = litersOfThinners  * paintThinnerPerLiterPrice
costOfAllMaterials = costOfPaints + costOfThinners + costOfPlates + bag
costOfWorkers = (costOfAllMaterials * (costOfWorkersPercent / 100)) * workHours
total = costOfAllMaterials + costOfWorkers

print(total)