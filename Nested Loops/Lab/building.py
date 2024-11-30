floor = int(input())
apartments = int(input())

EVEN_FLOORS_PREFIX_MASK = 'O{}{}'
ODD_FLOORS_PREFIX_MASK = 'A{}{}'
LAST_FLOOR_PREFIX_MASK = 'L{}{}'
building = []

for i in range(floor, 0, - 1 ):

    for apartment in range(apartments):
        if i == floor:
            print(LAST_FLOOR_PREFIX_MASK.format(i, apartment), end=" ")
        else:
            if i % 2 == 0:
                print(EVEN_FLOORS_PREFIX_MASK.format(i, apartment), end=" ")
            else:
                print(ODD_FLOORS_PREFIX_MASK.format(i, apartment), end=" ")
    print()