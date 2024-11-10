ERROR_TEXT = "Error"
WORKING_TEXT = "Working day"
WEEKEND_TEXT = "Weekend"
day = input()

if day == "Monday":
    print(WORKING_TEXT)
elif day == "Tuesday":
    print(WORKING_TEXT)
elif day == "Wednesday":
    print(WORKING_TEXT)
elif day == "Thursday":
    print(WORKING_TEXT)
elif day == "Friday":
    print(WORKING_TEXT)
elif day == "Saturday":
    print(WEEKEND_TEXT)
elif day == "Sunday":
    print(WEEKEND_TEXT)
else:
    print(ERROR_TEXT)
