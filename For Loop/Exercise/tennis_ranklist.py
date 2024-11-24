import math

points = {
    'W': 2000,
    'F' : 1200,
    'SF' : 720
}


tournir_counts = int(input())
start_points = int(input())
final_points = start_points
wins = 0
for i in range (0, tournir_counts):
    result = input()
    final_points += points[result]
    if result == 'W':
        wins += 1


print(f'Final points: {final_points}')
print(f'Average points: {math.floor(((final_points - start_points) / tournir_counts)):.0f}')
print(f'{(wins / tournir_counts * 100):.2f}%')
