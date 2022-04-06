import requests

from requests.exceptions import HTTPError

for url in ['http://www.cbr.ru/scripts/XML_daily.asp']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success')


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


response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

cod_currency = input('Введите код валюты, например, USD, EUR: ')
if cod_currency.islower():
    cod_currency = cod_currency.upper()
currency_rates(cod_currency)
print(currency_rates(cod_currency))
