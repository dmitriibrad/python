digits_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

num = input('Enter a number: ')


def num_translate_adv(number):
    try:
        if number[0].isupper():
            number = number.lower()
            return digits_dict[number].capitalize()
        else:
            return digits_dict[number]
    except:
        KeyError: None


print(num_translate_adv(num))
