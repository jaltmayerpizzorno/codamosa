# Automatically generated by Pynguin.
import pypara.currencies as module_0
import decimal as module_1
import pypara.exchange as module_2

def test_case_0():
    pass

def test_case_1():
    str_0 = '][OVH=yZ"QVEh=()'
    str_1 = '#\x0bc1)z]z$k'
    int_0 = 1127
    currency_type_0 = module_0.CurrencyType.METAL
    decimal_0 = module_1.Decimal()
    str_2 = ''
    int_1 = 899
    currency_type_1 = module_0.CurrencyType.CRYPTO
    decimal_1 = module_1.Decimal()
    int_2 = 1758
    currency_0 = module_0.Currency(str_0, str_2, int_1, currency_type_1, decimal_1, int_2)
    decimal_2 = currency_0.quantize(decimal_0)
    int_3 = -679
    currency_1 = module_0.Currency(str_0, str_1, int_0, currency_type_0, decimal_2, int_3)
    date_0 = None
    f_x_rate_lookup_error_0 = module_2.FXRateLookupError(currency_1, currency_0, date_0)