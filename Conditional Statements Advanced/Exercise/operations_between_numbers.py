n1 = int(input())
n2 = int(input())
operator = input()

try :
    if operator in ['+', '-', '*']:
        result = (n1 + n2) if operator == '+' else (n1 - n2) if operator == '-' else (n1  * n2) if operator == '*' else 0
        print(f'{n1} {operator} {n2} = {result} - {"even" if (result % 2 == 0) else "odd"}')
    elif operator == '/':
        print(f'{n1} / {n2} = {n1 / n2:.2f}')
    elif operator == '%':
        print(f'{n1} % {n2} = {n1 % n2}')
except:
        print(f"Cannot divide {n1} by zero")