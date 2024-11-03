import math

bookSites = int(input())
sitesProHour = int(input())
days = int(input())

totalDurationOfRead = math.floor(bookSites / sitesProHour)
requiredHoursPerDay= totalDurationOfRead / days

print(int(requiredHoursPerDay))