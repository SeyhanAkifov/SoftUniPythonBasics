tabs = {
      'Facebook' : 150,
      'Instagram' : 100,
      'Reddit' : 50
}

lost = 0
is_lost_salary = False
open_tabs = int(input())
salary = float(input())

for i in range (1, open_tabs + 1):
    tab = input()
    if tabs.__contains__(tab):
        lost += tabs[tab]

    if salary <= lost:
        is_lost_salary = True
        break

if is_lost_salary:
    print(f'You have lost your salary.')
else:
    print(f'{salary - lost:.0f}')