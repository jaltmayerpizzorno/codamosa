# Automatically generated by Pynguin.
import ansible.module_utils.common.dict_transformations as module_0

def test_case_0():
    try:
        bytes_0 = b'\xe5\xf0^\xa0\x9b\xbb\xe4BM\xc0\x12'
        var_0 = module_0.camel_dict_to_snake_dict(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        dict_0 = {tuple_0: tuple_0}
        var_0 = module_0.camel_dict_to_snake_dict(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -907
        list_0 = [int_0, int_0, int_0]
        bytes_0 = None
        dict_0 = {int_0: list_0, bytes_0: bytes_0, bytes_0: int_0, bytes_0: list_0}
        var_0 = module_0.camel_dict_to_snake_dict(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b']\xb1[G\x19\xdf)m6\xe8?\x93\xf8\x1e'
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        list_0 = [set_0]
        var_0 = module_0.snake_dict_to_camel_dict(list_0)
        str_0 = '>6}\nHzoAn\\XQ'
        var_1 = module_0.recursive_diff(str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'k/'
        dict_0 = {str_0: str_0}
        var_0 = module_0.dict_merge(str_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '>6}\nHzoAn\\XQ'
        var_0 = module_0.recursive_diff(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ''
        var_0 = module_0.snake_dict_to_camel_dict(str_0)
        dict_0 = {str_0: str_0, str_0: str_0}
        var_1 = module_0.snake_dict_to_camel_dict(dict_0)
        complex_0 = None
        bytes_0 = b'\x88\xea@,'
        var_2 = module_0.snake_dict_to_camel_dict(dict_0, bytes_0)
        bool_0 = False
        str_1 = None
        dict_1 = {str_1: str_1, bool_0: complex_0, str_1: str_0}
        var_3 = module_0.dict_merge(bool_0, dict_1)
    except BaseException:
        pass