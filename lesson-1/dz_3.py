for i in range(100):
    newStr = str(i + 1)
    new_list = list(newStr)
    if int(new_list[-1]) == 1 and i + 1 != 11:
        print('{} процент'.format(i + 1))
    elif 1 < int(new_list[-1]) <= 4:
        if 10 < i + 1 <= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))
