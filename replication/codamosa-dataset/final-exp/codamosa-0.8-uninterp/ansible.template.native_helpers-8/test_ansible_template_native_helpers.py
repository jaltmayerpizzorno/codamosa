# Automatically generated by Pynguin.
import ansible.template.native_helpers as module_0

def test_case_0():
    bytes_0 = b"'\xdd\xc5\xaf\xd5\xbd\xc1Dd\xfa\xb4@"
    var_0 = module_0.ansible_native_concat(bytes_0)

def test_case_1():
    str_0 = 'Hj$0aS5GZi'
    str_1 = '6C(u$'
    str_2 = 'O\\|u%t02WPSc#Z='
    str_3 = 'localhost,%s,127.0.0.1'
    dict_0 = {str_1: str_1, str_2: str_1, str_0: str_1, str_3: str_0}
    tuple_0 = ()
    tuple_1 = (dict_0, dict_0, tuple_0, str_3)
    var_0 = module_0.ansible_native_concat(tuple_1)

def test_case_2():
    str_0 = 'M'
    var_0 = module_0.ansible_native_concat(str_0)

def test_case_3():
    str_0 = 'D.\x0b\x0bt%;BE%Kkw'
    var_0 = module_0.ansible_native_concat(str_0)

def test_case_4():
    int_0 = None
    set_0 = {int_0}
    var_0 = module_0.ansible_native_concat(set_0)

def test_case_5():
    dict_0 = {}
    var_0 = module_0.ansible_native_concat(dict_0)