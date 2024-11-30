
is_finish = False
standard_percent = 0
standard_count = 0

student_percent = 0
student_count = 0

kid_percent = 0
kid_count = 0
total_free = 0

while not is_finish:
    movie_name = input()
    if movie_name == 'Finish':
        is_finish = True
        break

    movie_standard_count = 0
    movie_student_count = 0
    movie_kid_count = 0
    free_places = int(input())
    total_free += free_places
    is_end = False
    while not is_end:
        ticket_type = input()
        if ticket_type == 'End':
            is_end = True
            break
        if ticket_type == 'student':
            student_percent += 1
            student_count += 1
            movie_student_count += 1

        elif ticket_type == 'standard':
            standard_percent += 1
            standard_count += 1
            movie_standard_count += 1

        elif ticket_type == 'kid':
            kid_percent += 1
            kid_count += 1
            movie_kid_count += 1

        if (movie_standard_count + movie_kid_count + movie_student_count) == free_places:
            is_end = True
            break


    movie_total =  movie_standard_count + movie_kid_count + movie_student_count
    print(f'{movie_name} - {(movie_total * 100 / free_places):.2f}% full.')


total_ticket = student_count + standard_count + kid_count
total_standard_percent = standard_percent * 100 / total_ticket
total_student_percent = student_percent * 100 / total_ticket
total_kid_percent = kid_percent * 100 / total_ticket

print(f'Total tickets: {total_ticket}')
print(f'{total_student_percent:.2f}% student tickets.')
print(f'{total_standard_percent:.2f}% standard tickets.')
print(f'{total_kid_percent:.2f}% kids tickets.')



