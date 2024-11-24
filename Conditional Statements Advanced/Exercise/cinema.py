types = {
    'Premiere': 12.00,
    'Normal': 7.50,
    'Discount': 5.00
}

type = input()
rows = int(input())
cols = int(input())

total = rows * cols * types[type]

print(f"{total:.2f}")

