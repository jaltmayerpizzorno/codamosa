# Automatically generated by Pynguin.
import pypara.dcc as module_0
import datetime as module_1

def test_case_0():
    try:
        date_0 = None
        decimal_0 = module_0.dcfc_nl_365(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_1():
    try:
        date_0 = None
        decimal_0 = module_0.dcfc_act_act_icma(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_2():
    try:
        date_0 = None
        decimal_0 = module_0.dcfc_30_360_isda(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_3():
    try:
        date_0 = None
        decimal_0 = module_0.dcfc_act_365_a(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 12
        list_0 = [int_0, int_0, int_0]
        date_0 = module_1.date(*list_0)
        decimal_0 = module_0.dcfc_30_360_us(date_0, date_0, date_0)
        decimal_1 = module_0.dcfc_30_e_360(date_0, date_0, date_0)
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        int_1 = 43
        list_1 = [date_0, int_1]
        date_1 = module_1.date(*list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 12
        list_0 = [int_0, int_0, int_0]
        date_0 = module_1.date(*list_0)
        decimal_0 = module_0.dcfc_30_360_us(date_0, date_0, date_0)
        decimal_1 = module_0.dcfc_30_360_german(date_0, date_0, date_0)
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        date_1 = module_1.date()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'bei]p<O'
        date_0 = None
        none_type_0 = None
        list_0 = [str_0, str_0, str_0, str_0]
        d_c_c_0 = module_0.DCC(*list_0)
        decimal_0 = d_c_c_0.calculate_fraction(date_0, date_0, date_0, none_type_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'e)I'
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        date_0 = None
        list_0 = [str_0, d_c_c_registry_machinery_0, d_c_c_registry_machinery_0, d_c_c_registry_machinery_0]
        dict_0 = {}
        d_c_c_0 = module_0.DCC(*list_0, **dict_0)
        decimal_0 = d_c_c_0.calculate_daily_fraction(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 12
        list_0 = [int_0, int_0, int_0]
        date_0 = module_1.date(*list_0)
        decimal_0 = module_0.dcfc_30_360_us(date_0, date_0, date_0)
        decimal_1 = module_0.dcfc_nl_365(date_0, date_0, date_0)
        decimal_2 = module_0.dcfc_30_360_isda(date_0, date_0, date_0)
        decimal_3 = module_0.dcfc_act_act_icma(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 12
        list_0 = [int_0, int_0, int_0]
        date_0 = module_1.date(*list_0)
        decimal_0 = module_0.dcfc_30_360_us(date_0, date_0, date_0)
        decimal_1 = module_0.dcfc_nl_365(date_0, date_0, date_0)
        date_1 = None
        decimal_2 = module_0.dcfc_30_360_isda(date_0, date_1, date_1)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 12
        list_0 = [int_0, int_0, int_0]
        date_0 = module_1.date(*list_0)
        decimal_0 = module_0.dcfc_30_360_us(date_0, date_0, date_0)
        decimal_1 = module_0.dcfc_nl_365(date_0, date_0, date_0)
        decimal_2 = module_0.dcfc_30_360_isda(date_0, date_0, date_0)
        date_1 = module_1.date()
    except BaseException:
        pass