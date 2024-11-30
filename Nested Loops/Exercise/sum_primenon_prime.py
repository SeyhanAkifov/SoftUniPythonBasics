import math


is_stop = False
def check_is_prime(number):
    limit = math.ceil(math.sqrt(number))
    for i in range(2, limit + 1):
        if number % i == 0:
            return False

    return True


prime_sum = 0
non_prime_sum = 0

while not is_stop:
    command = input()
    if command == 'stop':
        is_stop = True
        break
    number = int(command)
    if number < 0:
        print('Number is negative.')
        continue
    elif number == 0:
        non_prime_sum += number
    elif number == 1:
        non_prime_sum += number
    elif number == 2:
        prime_sum += number
    elif check_is_prime(number):
        prime_sum += number
    elif not check_is_prime(number):
        non_prime_sum += number


print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')


