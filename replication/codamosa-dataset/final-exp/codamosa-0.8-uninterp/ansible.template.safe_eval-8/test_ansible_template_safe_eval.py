# Automatically generated by Pynguin.
import ansible.template.safe_eval as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'FAILED_SETUP'
    var_0 = module_0.safe_eval(str_0)

def test_case_2():
    set_0 = None
    var_0 = module_0.safe_eval(set_0)

def test_case_3():
    str_0 = '3\t\rS"jv$yZI!Z)zg2['
    var_0 = module_0.safe_eval(str_0)

def test_case_4():
    bytes_0 = None
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    str_0 = 'o1kb+}]!@c6:C\\q'
    str_1 = '"E>[NaTlx,'
    bytes_1 = b"\xb3\x83\x92\x1e\xdb\xd3\xf7\x0f'dT"
    bytes_2 = b'U\xbf\xf9vuU\x04\x0c"Ji\xe1\xd5-Z'
    list_0 = []
    float_0 = -885.1541
    tuple_0 = (list_0, float_0)
    tuple_1 = (str_1, bytes_1, bytes_2, tuple_0)
    var_0 = module_0.safe_eval(dict_0, str_0, tuple_1)

def test_case_5():
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    var_0 = module_0.safe_eval(set_0, list_0)

def test_case_6():
    str_0 = 'SdkFPA>+V'
    dict_0 = {str_0: str_0}
    list_0 = None
    var_0 = module_0.safe_eval(str_0, dict_0, list_0)

def test_case_7():
    str_0 = 'SdkFPAYV'
    dict_0 = {str_0: str_0}
    list_0 = None
    var_0 = module_0.safe_eval(str_0, dict_0, list_0)

def test_case_8():
    str_0 = 'oC'
    str_1 = '\x0b;Xc:~qK;k3,AC'
    dict_0 = {str_1: str_0, str_1: str_1}
    tuple_0 = (str_1, dict_0, str_1, dict_0)
    var_0 = module_0.safe_eval(str_0, tuple_0, dict_0)
    list_0 = None
    float_0 = -1839.4173
    var_1 = module_0.safe_eval(str_1, float_0)
    var_2 = module_0.safe_eval(list_0)

def test_case_9():
    str_0 = '1'
    var_0 = module_0.safe_eval(str_0)
    str_1 = '[1, 2]'
    var_1 = module_0.safe_eval(str_1)
    str_2 = '{"a": "b"}'
    var_2 = module_0.safe_eval(str_2)
    str_3 = '1 | string'
    var_3 = module_0.safe_eval(str_3)
    str_4 = '2+2'
    var_4 = module_0.safe_eval(str_4)
    str_5 = '1+1'
    var_5 = {}
    bool_0 = True
    var_6 = module_0.safe_eval(str_5, var_5, bool_0)