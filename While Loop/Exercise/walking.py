GOAL = 10000

going_home = False
goal_reached = False
total_steps = 0
while not going_home and not goal_reached:
    text = input()
    if text == 'Going home':

        steps_to_home = int(input())
        total_steps += steps_to_home
        if total_steps >= GOAL:
            goal_reached = True
        going_home = True
        break
    else:
        total_steps += int(text)

    if total_steps >= GOAL:
        goal_reached = True
        break

if goal_reached:
    print(f'Goal reached! Good job!')
    print(f'{total_steps - GOAL} steps over the goal!')
else:
    print(f'{GOAL - total_steps} more steps to reach goal.')