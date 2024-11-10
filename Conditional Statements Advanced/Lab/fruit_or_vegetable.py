from contextlib import nullcontext

fruits = [
    ["fruit" , ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']],
    ["vegetable" , ['tomato', 'cucumber', 'pepper', 'carrot']]
]

UNKNOWN_TEXT = "unknown"

text = input()
c = [x for x in fruits if x[1].__contains__(text) == True]

if c:
    v = [x for x in fruits if x[1].__contains__(text) == True][0]
    print(v[0])
else:
    print(UNKNOWN_TEXT)