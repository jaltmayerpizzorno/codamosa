# Automatically generated by Pynguin.
import ansible.module_utils.common.parameters as module_0

def test_case_0():
    try:
        var_0 = module_0.env_fallback()
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        list_0 = [set_0]
        var_0 = module_0.remove_values(list_0, list_0)
        int_0 = 3089
        var_1 = module_0.set_fallbacks(set_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        dict_0 = {}
        dict_1 = {str_0: str_0}
        list_0 = [dict_1, str_0, dict_1, dict_1]
        var_0 = module_0.set_fallbacks(dict_0, list_0)
        bytes_0 = b'\xbe\xddzt\xea\x99\x88\xcfn/z\xd6\x12G/V'
        str_1 = '2^\x0b+$1\x0cjGY^Vb|B\r&'
        var_1 = module_0.remove_values(bytes_0, str_1)
        var_2 = module_0.remove_values(dict_0, dict_1)
        dict_2 = None
        var_3 = module_0.sanitize_keys(dict_2, bytes_0)
        bytes_1 = b'\xe8|\xb3\\\x81\xc2A\x1d\xa8ny\xa6\x96\x10^\xf8%\x818\x14'
        list_1 = [var_3, dict_0, dict_1, str_0]
        var_4 = module_0.sanitize_keys(str_0, list_1)
        int_0 = -382
        var_5 = module_0.sanitize_keys(str_0, bytes_1, int_0)
        var_6 = module_0.remove_values(int_0, list_1)
        tuple_0 = ()
        var_7 = module_0.sanitize_keys(tuple_0, str_0, tuple_0)
        var_8 = module_0.env_fallback(**dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'RH\x0bM[A;(\x0c7J^l+j[,t}O'
        complex_0 = None
        list_0 = [str_0, complex_0, complex_0, str_0]
        dict_0 = {str_0: complex_0}
        var_0 = module_0.env_fallback(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'foo'
        str_1 = 'foo_fallback'
        str_2 = 'bar'
        str_3 = 'bar_fallback'
        str_4 = 'type'
        str_5 = 'str'
        str_6 = {str_4: str_5}
        str_7 = 'fallback'
        str_8 = 'env_fallback'
        str_9 = (str_8, str_2)
        str_10 = {str_4: str_5, str_7: str_9}
        str_11 = {str_4: str_5}
        str_12 = (str_8, str_0)
        str_13 = {str_4: str_5, str_7: str_12}
        str_14 = {str_0: str_6, str_1: str_10, str_2: str_11, str_3: str_13}
        str_15 = {str_0: str_0}
        var_0 = module_0.set_fallbacks(str_14, str_15)
    except BaseException:
        pass