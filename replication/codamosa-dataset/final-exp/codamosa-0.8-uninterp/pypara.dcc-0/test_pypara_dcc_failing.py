# Automatically generated by Pynguin.
import pypara.dcc as module_0
import datetime as module_1

def test_case_0():
    try:
        date_0 = None
        str_0 = 't@l6\x0b~gP'
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        optional_0 = d_c_c_registry_machinery_0.find(str_0)
        str_1 = '<aF1x{{!#8{m;JK'
        d_c_c_registry_machinery_1 = module_0.DCCRegistryMachinery()
        optional_1 = d_c_c_registry_machinery_1.find(str_1)
        list_0 = [optional_1, d_c_c_registry_machinery_1, d_c_c_registry_machinery_1, optional_1]
        d_c_c_0 = module_0.DCC(*list_0)
        bool_0 = False
        decimal_0 = d_c_c_0.calculate_fraction(date_0, date_0, date_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0]
        date_0 = module_1.date(*list_0)
        decimal_0 = module_0.dcfc_act_act(date_0, date_0, date_0)
        decimal_1 = module_0.dcfc_act_act_icma(date_0, date_0, date_0)
    except BaseException:
        pass