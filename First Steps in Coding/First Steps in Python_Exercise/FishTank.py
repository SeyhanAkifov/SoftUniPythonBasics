

length = float(input())
width = float(input())
height = float(input())
percent = float(input())

volume = length * width * height
literVolume = volume / 1000


neededLiters = literVolume * (1 - (percent / 100))

print(neededLiters)