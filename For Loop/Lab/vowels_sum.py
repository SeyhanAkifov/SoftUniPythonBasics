vowels = {
    'a' : 1,
    'e' : 2,
    'i' : 3,
    'o' : 4,
    'u' : 5,
}

text = input()
sum = 0
for i in range (0, len (text)):
    if vowels.__contains__(text[i]):
        sum += vowels[text[i]]

print(sum)