# Automatically generated by Pynguin.
import datetime as module_0
import pypara.dcc as module_1

def test_case_0():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0]
        date_0 = module_0.date(*list_0)
        date_1 = module_0.date(*list_0)
        decimal_0 = module_1.dcfc_30_e_plus_360(date_0, date_0, date_1)
        decimal_1 = module_1.dcfc_act_act_icma(date_1, date_0, date_0)
    except BaseException:
        pass

def test_case_1():
    try:
        date_0 = None
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0, dict_0]
        d_c_c_0 = module_1.DCC(*list_0)
        decimal_0 = d_c_c_0.calculate_daily_fraction(date_0, date_0, date_0)
    except BaseException:
        pass