n = int(input())
count = 0
for i in range(n + 1):
    for k in range(n + 1):
        for l in range(n + 1):
            if (i + k + l) == n:
                count += 1

print(count)

