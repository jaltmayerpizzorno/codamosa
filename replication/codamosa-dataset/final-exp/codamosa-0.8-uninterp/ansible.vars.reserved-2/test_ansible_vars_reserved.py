# Automatically generated by Pynguin.
import ansible.vars.reserved as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = 0.0001
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.get_reserved_names(list_0)
    var_1 = module_0.get_reserved_names()
    str_0 = ''
    dict_0 = {}
    var_2 = module_0.get_reserved_names(dict_0)
    var_3 = module_0.is_reserved_name(str_0)

def test_case_2():
    str_0 = '`'
    var_0 = module_0.warn_if_reserved(str_0)

def test_case_3():
    complex_0 = None
    var_0 = module_0.is_reserved_name(complex_0)