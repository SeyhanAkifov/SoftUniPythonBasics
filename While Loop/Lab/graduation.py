student_name = input()
grade_year = 0
is_excluded = False
grade_total = 0
excluded_count = 0
first_exclude_year = 0

while grade_year < 12 and not is_excluded:
    grade = float(input())
    grade_year += 1
    if first_exclude_year != grade_year:
        excluded_count = 0
    if grade >= 4.00:
        grade_total += grade
    else:
        first_exclude_year = grade_year

        excluded_count += 1
        if excluded_count == 2:
            is_excluded = True
            break
        grade_year -= 1



average_grade = grade_total / grade_year

if grade_year == 12:
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
else:
    print(f'{student_name} has been excluded at {grade_year} grade')