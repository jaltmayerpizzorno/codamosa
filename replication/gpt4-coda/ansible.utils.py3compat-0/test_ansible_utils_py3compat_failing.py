# Automatically generated by Pynguin.
import ansible.utils.py3compat as module_0

def test_case_0():
    try:
        str_0 = '}'
        int_0 = -27
        text_environ_0 = module_0._TextEnviron(int_0)
        var_0 = text_environ_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x01\xd1\xbf"\x89\x03\x12\x99\x178\xe4\xab\x9e\x1c\x06\xa2\xbeV>'
        text_environ_0 = module_0._TextEnviron()
        var_0 = text_environ_0.__getitem__(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 493
        float_0 = 1179.902
        str_0 = 'r{U!d&My'
        float_1 = 100.0
        text_environ_0 = module_0._TextEnviron(str_0, float_1)
        var_0 = text_environ_0.__setitem__(int_0, float_0)
    except BaseException:
        pass