# Automatically generated by Pynguin.
import pypara.exchange as module_0
import pypara.currencies as module_1
import decimal as module_2

def test_case_0():
    try:
        str_0 = '\n        Indicates if the ledger entry is a credit.\n        '
        str_1 = 'y_IOF!:'
        int_0 = -3912
        list_0 = [str_1, int_0, str_0, str_0]
        f_x_rate_0 = module_0.FXRate(*list_0)
        f_x_rate_1 = f_x_rate_0.__invert__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '#8H$J'
        int_0 = -94
        currency_type_0 = module_1.CurrencyType.MONEY
        decimal_0 = module_2.Decimal()
        int_1 = -2143
        currency_0 = module_1.Currency(str_0, str_0, int_0, currency_type_0, decimal_0, int_1)
        date_0 = None
        str_1 = 'SGD'
        currency_1 = module_1.Currency(str_1, str_0, int_0, currency_type_0, decimal_0, int_1)
        f_x_rate_lookup_error_0 = module_0.FXRateLookupError(currency_0, currency_1, date_0)
        dict_0 = {}
        f_x_rate_service_0 = module_0.FXRateService(**dict_0)
    except BaseException:
        pass