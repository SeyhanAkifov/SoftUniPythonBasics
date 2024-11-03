SLOW_TEXT = 'slow'
AVERAGE_TEXT = 'average'
FAST_TEXT = 'fast'
ULTRA_FAST_TEXT = 'ultra fast'
EXTREMELY_FAST_TEXT = 'extremely fast'

speed = float(input())

if speed <= 10:
    print(SLOW_TEXT)
elif 10 < speed <= 50:
    print(AVERAGE_TEXT)
elif 50 < speed <= 150:
    print(FAST_TEXT)
elif 150 < speed <= 1000:
    print(ULTRA_FAST_TEXT)
else:
    print(EXTREMELY_FAST_TEXT)