# Automatically generated by Pynguin.
import ansible.vars.reserved as module_0

def test_case_0():
    try:
        var_0 = module_0.get_reserved_names()
        float_0 = 724.0
        float_1 = 0.0
        str_0 = 'name_parts'
        tuple_0 = ()
        dict_0 = {}
        var_1 = module_0.get_reserved_names(dict_0)
        dict_1 = {float_1: str_0, float_0: tuple_0}
        var_2 = module_0.is_reserved_name(dict_1)
    except BaseException:
        pass

def test_case_1():
    try:
        complex_0 = None
        bool_0 = True
        var_0 = module_0.warn_if_reserved(complex_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = module_0.get_reserved_names()
        list_0 = []
        tuple_0 = None
        var_1 = module_0.is_reserved_name(tuple_0)
        list_1 = [list_0, list_0]
        bytes_0 = b'-\x96\xaawD\xceux\xd6\xcb\xb1\xefD'
        var_2 = module_0.warn_if_reserved(list_1, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        var_0 = module_0.is_reserved_name(str_0)
        bytes_0 = b'\xb1\x82A\xae<n\xb9\xab\xbfF'
        str_1 = '(c\r'
        tuple_0 = (bytes_0, str_1)
        var_1 = module_0.warn_if_reserved(tuple_0)
        var_2 = module_0.get_reserved_names()
        str_2 = 'MV'
        var_3 = module_0.warn_if_reserved(str_2, str_2)
        int_0 = 323
        var_4 = module_0.warn_if_reserved(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = module_0.get_reserved_names()
        list_0 = [var_0, var_0, var_0, var_0]
        var_1 = module_0.is_reserved_name(list_0)
    except BaseException:
        pass