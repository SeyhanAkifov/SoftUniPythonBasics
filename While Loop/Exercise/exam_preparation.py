bad_grades_count = int(input())
problems_count = 0
grade_total = 0
failed_count = 0
last_exam = ''
is_enough = False
while not is_enough and failed_count < bad_grades_count:
    exam_name = input()
    if exam_name == 'Enough':
        is_enough = True
        break
    else:
        last_exam = exam_name
        grade = float(input())
        if grade > 4:
            problems_count += 1
            grade_total += grade
        else:
            problems_count += 1
            grade_total += grade
            failed_count += 1

if failed_count == bad_grades_count:
    print(f'You need a break, {failed_count} poor grades.')
else:
    print(f'Average score: {(grade_total / problems_count):.2f}')
    print(f'Number of problems: {problems_count}')
    print(f'Last problem: {last_exam}')
