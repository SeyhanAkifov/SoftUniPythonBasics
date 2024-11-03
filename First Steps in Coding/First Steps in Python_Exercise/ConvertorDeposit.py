import math

depositAmount = float(input())
depositDuring = float(input())
depositYearRate = float(input())


depositMainRateTotal = depositAmount * (depositYearRate / 100)
depositMonthRate = depositMainRateTotal / 12
total = depositAmount + (depositDuring *  depositMonthRate)

print(total)


