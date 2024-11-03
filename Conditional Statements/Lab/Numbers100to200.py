LESS_TEXT = 'Less than 100'
BETWEEN_TEXT = 'Between 100 and 200'
GREATER_TEXT = 'Greater than 200'


number = int(input())

if number < 100:
    print(LESS_TEXT)
elif number > 200:
    print(GREATER_TEXT)
else:
    print(BETWEEN_TEXT)