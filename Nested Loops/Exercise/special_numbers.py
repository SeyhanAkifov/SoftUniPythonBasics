n = int(input())

START = 1111
END = 9999

def is_special(n, number):
    flag = False
    flag1 = False
    flag2 = False
    flag3 = False

    number_text = str( number)

    if int(number_text[0]) > 0 and  n % int(number_text[0]) == 0:
        flag = True

    if int(number_text[1]) > 0 and  n % int(number_text[1]) == 0:
        flag1 = True

    if int(number_text[2]) > 0 and  n % int(number_text[2]) == 0:
        flag2 = True

    if int(number_text[3]) > 0 and  n % int(number_text[3]) == 0:
        flag3 = True

    if flag and flag1 and flag2 and flag3:
        return True
    else:
        return False


for i in range(START, END + 1):
    if is_special(n, i):
        print(i, end = ' ')