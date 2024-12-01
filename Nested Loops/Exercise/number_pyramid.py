number = int(input())
magic_number = 1
for i in range(1, number + 1):
    for k in range(1, i + 1):
        print(magic_number , end = ' ')
        magic_number += 1
        if magic_number == number +1 :

            break
    print()
    if magic_number == number +1 :

        break