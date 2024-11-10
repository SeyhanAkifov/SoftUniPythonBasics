


age = float(input())
male = input()


if age >= 16:
    if male == 'f':
        print("Ms.")
    else:
        print("Mr.")
elif age < 16:
    if male == 'f':
        print("Miss")
    else:
        print("Master")