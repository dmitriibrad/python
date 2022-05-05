def number(value):
    if not value[0].isdigit():
        return num_3(value)
    else:
        return digit(value)


def digit(value):
    if value.isdigit():
        return '"' + num_2(value) + '"'
    else:
        return value


def num_3(value):
    if (value[0] == '+' or value[0] == '-') and len(value) > 1:
        return '"' + value[0] + num_2(value[1:]) + '"'
    else:
        return value


def num_2(value):
    if len(value) == 1:
        return '0' + value
    else:
        return value


weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
str1 = ''
for i in weather:
    str1 += (number(i) + ' ')
print(str1)
