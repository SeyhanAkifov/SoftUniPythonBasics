WINNER_POINTS = 1250.5

name = input()
academy_points = float(input())
jury_count = int(input())

is_winner = False
for i in range (0, jury_count):
    jury_name = input()
    jury_points = float(input())
    academy_points += (len (jury_name) * jury_points) / 2
    if academy_points >= WINNER_POINTS:
        is_winner = True
        break

if is_winner:
    print(f'Congratulations, {name} got a nominee for leading role with {academy_points:.1f}!')
else:
    print(f'Sorry, {name} you need {(WINNER_POINTS - academy_points):.1f} more!')