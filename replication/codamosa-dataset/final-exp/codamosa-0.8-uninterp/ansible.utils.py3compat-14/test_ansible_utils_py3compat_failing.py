# Automatically generated by Pynguin.
import ansible.utils.py3compat as module_0

def test_case_0():
    try:
        bool_0 = True
        text_environ_0 = module_0._TextEnviron()
        var_0 = text_environ_0.__delitem__(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        text_environ_0 = module_0._TextEnviron()
        bytes_0 = b'\x85>\x1cR\xd4S'
        var_0 = text_environ_0.__getitem__(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        text_environ_0 = module_0._TextEnviron()
        set_0 = None
        list_0 = []
        tuple_0 = (set_0, list_0)
        text_environ_1 = module_0._TextEnviron()
        var_0 = text_environ_1.__setitem__(text_environ_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 9000
        str_0 = '.'
        tuple_0 = ()
        text_environ_0 = module_0._TextEnviron(tuple_0)
        var_0 = text_environ_0.__iter__()
        str_1 = 't+G c2gh0P6fuI+sf'
        set_0 = {str_1, str_0, str_1}
        text_environ_1 = module_0._TextEnviron(str_1, set_0)
        var_1 = text_environ_0.__len__()
        text_environ_2 = module_0._TextEnviron(str_0, text_environ_1)
        var_2 = text_environ_2.__delitem__(int_0)
    except BaseException:
        pass