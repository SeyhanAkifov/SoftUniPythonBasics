animalTypes = {
    "dog" : "mammal",
    "crocodile" : "reptile",
    "tortoise" : "reptile",
    "snake" : "reptile",
}

OTHERS = "unknown"

animal = input()

if animalTypes.__contains__(animal):
    print(animalTypes[animal])
else:
    print(OTHERS)

