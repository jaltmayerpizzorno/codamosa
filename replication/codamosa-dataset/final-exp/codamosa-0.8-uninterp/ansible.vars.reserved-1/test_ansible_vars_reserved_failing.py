# Automatically generated by Pynguin.
import ansible.vars.reserved as module_0

def test_case_0():
    try:
        set_0 = set()
        var_0 = module_0.get_reserved_names(set_0)
        dict_0 = {}
        bool_0 = False
        tuple_0 = (dict_0, bool_0)
        var_1 = module_0.is_reserved_name(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '&'
        bool_0 = True
        var_0 = module_0.warn_if_reserved(str_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        var_0 = module_0.warn_if_reserved(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        var_0 = module_0.is_reserved_name(str_0)
        bool_0 = False
        var_1 = module_0.get_reserved_names()
        var_2 = module_0.get_reserved_names(bool_0)
        bytes_0 = b'r\xed5\x04\x14\xb1\xe1\xb7m\x80Z_\x93JX\xcb'
        var_3 = module_0.get_reserved_names()
        var_4 = module_0.warn_if_reserved(bytes_0)
        var_5 = module_0.is_reserved_name(str_0)
        str_1 = 'split_lines'
        var_6 = module_0.warn_if_reserved(str_1, str_1)
        bytes_1 = b'3\xb1 f\xd3\x15\xa7\xba\xe0r\xbd\xd2n\x8a'
        var_7 = module_0.is_reserved_name(bytes_1)
        float_0 = -1038.264271
        var_8 = module_0.warn_if_reserved(float_0)
    except BaseException:
        pass