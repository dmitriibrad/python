seconds = int(input('введите число в секундах: '))
day = seconds // 86400
hour = (seconds // 3600) % 24
minutes = (seconds // 60) % 60
sec = seconds % 60
print(day, 'дн', hour, 'час', minutes, 'мин', sec, 'сек')
