from utils import *

if cod_currency.islower()==True:
        cod_currency=cod_currency.upper()

currency_rates(cod_currency)
print (currency_rates(cod_currency))