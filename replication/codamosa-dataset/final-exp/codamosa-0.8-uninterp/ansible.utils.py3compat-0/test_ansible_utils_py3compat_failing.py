# Automatically generated by Pynguin.
import ansible.utils.py3compat as module_0

def test_case_0():
    try:
        text_environ_0 = module_0._TextEnviron()
        int_0 = 200000
        str_0 = 'bl+'
        text_environ_1 = module_0._TextEnviron(str_0)
        var_0 = text_environ_1.__delitem__(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        text_environ_0 = module_0._TextEnviron()
        float_0 = 2398.951
        int_0 = -3567
        var_0 = text_environ_0.__setitem__(float_0, int_0)
    except BaseException:
        pass