# Automatically generated by Pynguin.
import pypara.currencies as module_0
import decimal as module_1
import pypara.exchange as module_2

def test_case_0():
    try:
        str_0 = 'u'
        str_1 = 'b7c$K[\\'
        int_0 = -2758
        currency_type_0 = module_0.CurrencyType.METAL
        decimal_0 = module_1.Decimal()
        int_1 = -4425
        currency_0 = module_0.Currency(str_0, str_1, int_0, currency_type_0, decimal_0, int_1)
        date_0 = None
        f_x_rate_lookup_error_0 = module_2.FXRateLookupError(currency_0, currency_0, date_0)
        currency_type_1 = None
        list_0 = [currency_type_1]
        decimal_1 = module_1.Decimal(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        int_0 = 2530
        str_1 = '&\\Us6q.&E+gklX'
        list_0 = [str_1, str_0, str_1, int_0]
        f_x_rate_0 = module_2.FXRate(*list_0)
        f_x_rate_1 = f_x_rate_0.__invert__()
        f_x_rate_service_0 = module_2.FXRateService()
    except BaseException:
        pass