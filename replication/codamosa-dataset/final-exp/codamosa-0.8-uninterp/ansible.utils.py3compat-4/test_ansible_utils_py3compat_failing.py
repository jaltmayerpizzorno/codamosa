# Automatically generated by Pynguin.
import ansible.utils.py3compat as module_0

def test_case_0():
    try:
        bytes_0 = None
        list_0 = [bytes_0]
        text_environ_0 = module_0._TextEnviron(list_0)
        set_0 = set()
        bytes_1 = b'\x90p'
        text_environ_1 = module_0._TextEnviron(bytes_1)
        var_0 = text_environ_1.__delitem__(set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1379.92
        tuple_0 = (float_0,)
        text_environ_0 = module_0._TextEnviron()
        var_0 = text_environ_0.__getitem__(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'YGEtF@OF'
        int_0 = 524
        list_0 = [str_0, str_0, str_0, int_0]
        text_environ_0 = module_0._TextEnviron()
        str_1 = '0^xI\nF;n%upSU"E2\\p1<'
        list_1 = [str_1]
        var_0 = text_environ_0.__len__()
        text_environ_1 = module_0._TextEnviron(str_1, list_1)
        var_1 = text_environ_1.__setitem__(list_0, text_environ_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xed\xb0\xf0L'
        text_environ_0 = module_0._TextEnviron()
        var_0 = text_environ_0.__iter__()
        text_environ_1 = module_0._TextEnviron()
        var_1 = text_environ_1.__len__()
        var_2 = text_environ_1.__iter__()
        var_3 = text_environ_1.__getitem__(bytes_0)
    except BaseException:
        pass