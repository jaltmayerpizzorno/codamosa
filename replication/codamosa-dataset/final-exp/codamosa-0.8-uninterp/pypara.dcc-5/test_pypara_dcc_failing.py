# Automatically generated by Pynguin.
import pypara.dcc as module_0
import pypara.currencies as module_1

def test_case_0():
    try:
        str_0 = "' does not exist"
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        optional_0 = d_c_c_registry_machinery_0.find(str_0)
        date_0 = None
        decimal_0 = module_0.dcfc_nl_365(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'CiNbG}qj9VL.'
        str_1 = '\\X,ypm-;C0+dN8(lk":\t'
        str_2 = 'V4'
        str_3 = 'I,"Mn8~bV4L;/M)'
        set_0 = {str_1, str_2, str_3, str_1}
        callable_0 = module_0.dcc(str_0, set_0)
        date_0 = None
        decimal_0 = module_0.dcfc_act_365_f(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_2():
    try:
        date_0 = None
        decimal_0 = module_0.dcfc_act_365_a(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'JfHa?>R{,7jtg[h@\\'
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        optional_0 = d_c_c_registry_machinery_0.find(str_0)
        date_0 = None
        decimal_0 = module_0.dcfc_30_360_isda(date_0, date_0, date_0, d_c_c_registry_machinery_0)
    except BaseException:
        pass

def test_case_4():
    try:
        date_0 = None
        decimal_0 = module_0.dcfc_30_360_us(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "' does not exist"
        str_1 = "'e@/wxtM\r"
        callable_0 = module_0.dcc(str_1)
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        optional_0 = d_c_c_registry_machinery_0.find(str_0)
        date_0 = None
        str_2 = 't,w&aiFZ= [n6k$i'
        set_0 = {str_2, str_0, str_2}
        callable_1 = module_0.dcc(str_0, set_0)
        decimal_0 = module_0.dcfc_act_365_l(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_6():
    try:
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        date_0 = None
        decimal_0 = module_0.dcfc_30_e_plus_360(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_7():
    try:
        date_0 = None
        decimal_0 = module_0.dcfc_act_360(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = "' does not exist"
        str_1 = "'e@/wxtM\r"
        callable_0 = module_0.dcc(str_1)
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        optional_0 = d_c_c_registry_machinery_0.find(str_0)
        date_0 = None
        str_2 = 't,w&aiFZ= [n6k$i'
        set_0 = {str_2, str_0, str_2}
        callable_1 = module_0.dcc(str_0, set_0)
        currency_type_0 = module_1.CurrencyType.METAL
        decimal_0 = module_0.dcfc_act_act_icma(date_0, date_0, date_0, currency_type_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\nq*.!'
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        optional_0 = d_c_c_registry_machinery_0.find(str_0)
        date_0 = None
        decimal_0 = module_0.dcfc_30_e_360(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '\nq*.!'
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        optional_0 = d_c_c_registry_machinery_0.find(str_0)
        date_0 = None
        decimal_0 = module_0.dcfc_30_360_german(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '\nq*.!'
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        optional_0 = d_c_c_registry_machinery_0.find(str_0)
        date_0 = None
        decimal_0 = module_0.dcfc_act_act(date_0, date_0, date_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'JfHa?>R{,7jtg[h@t'
        str_1 = "' does not exist"
        d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
        str_2 = '30/360 German'
        list_0 = [d_c_c_registry_machinery_0, str_1, str_2, str_0]
        d_c_c_0 = module_0.DCC(*list_0)
        d_c_c_registry_machinery_0.register(d_c_c_0)
    except BaseException:
        pass