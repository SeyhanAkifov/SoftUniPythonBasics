juri_count = int(input())

is_finish = False
presentation_list = {}
total_grade = 0
grade_count = 0
while not is_finish:
    presentation_name = input()
    if presentation_name == 'Finish':
        is_finish = True
        break
    grade = 0
    for i in range(juri_count):
        gr = float(input())
        grade += gr
        grade_count += 1
    total_grade += grade

    print(f'{presentation_name} - {(grade / juri_count):.2f}.')

print(f'Student\'s final assessment is {(total_grade / grade_count):.2f}.')

