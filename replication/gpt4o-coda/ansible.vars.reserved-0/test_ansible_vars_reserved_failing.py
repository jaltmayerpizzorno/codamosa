# Automatically generated by Pynguin.
import ansible.vars.reserved as module_0

def test_case_0():
    try:
        str_0 = '=oO(";\t}++yz"y{2'
        bytes_0 = b'\xd5i\xe3'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: bytes_0}
        list_0 = [dict_0, dict_0, dict_0, str_0]
        float_0 = 3453.87031
        var_0 = module_0.warn_if_reserved(list_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        var_0 = module_0.warn_if_reserved(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'A,'
        set_0 = {str_0, str_0}
        var_0 = module_0.is_reserved_name(set_0)
        complex_0 = None
        var_1 = module_0.get_reserved_names(complex_0)
        var_2 = module_0.warn_if_reserved(str_0, set_0)
        bytes_0 = b'\x9e\x03\xf0j\xb5Y\x11\xd9\x17>\xd5C\xfc\xe3\xe6\x82Z\x84\xf0\xeb'
        bool_0 = None
        var_3 = module_0.is_reserved_name(bool_0)
        bytes_1 = b'\xe28\xf6Y3\x0f\xaf\xb2\x9fN'
        var_4 = module_0.warn_if_reserved(bytes_0, bytes_1)
        var_5 = module_0.get_reserved_names()
        var_6 = module_0.get_reserved_names()
        list_0 = [bytes_0, set_0, var_1, var_6]
        bool_1 = False
        var_7 = module_0.warn_if_reserved(list_0, bool_1)
    except BaseException:
        pass