days = {
     1 : "Monday",
     2 : "Tuesday",
     3 : "Wednesday",
     4 : "Thursday",
     5 : "Friday",
     6 : "Saturday",
     7 : "Sunday",
}

ERROR_TEXT = "Error"

number = int(input())


if days.__contains__(number):
    print(days[number])
else:
    print(ERROR_TEXT)