animalTypes = {
"dog" : "mammal",
    "crocodile" : "reptile",
    "tortoise" : "reptile",
    "snake" : "reptile",
    "others" : "unknown"
}

OTHERS = "unknown"

animal = input()

if animal.__contains__(animalTypes):
    print(animalTypes[animal])
else:
    print(OTHERS)

