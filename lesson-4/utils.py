import requests

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
cod_currency = input('Введите код валюты USD или EUR: ')


def currency_rates(current):
    if len(current) == 3 and current.isalpha() == True:
        char_code = response.text.find(current)
        char_code_str = response.text[char_code:char_code + 92]
        char_code_str = char_code_str.split('>' '<')
        nominal_code_value = int(char_code_str[1][8:-9])
        value_code_value = char_code_str[3][6:-7]
        value_code_value_N1, value_code_value_N2 = value_code_value.split(',')
        value_code_value_N3 = (float(value_code_value_N1 + "." + value_code_value_N2))
        name_code = char_code_str[2][5:-6]
        return nominal_code_value, name_code, value_code_value_N3
    else:
        return
