# Automatically generated by Pynguin.
import ansible.utils.color as module_0

def test_case_0():
    try:
        str_0 = 'OqTy_H'
        var_0 = module_0.parsecolor(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        var_0 = module_0.parsecolor(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = None
        str_0 = "Invalid type %s for option '%s'"
        float_0 = 1111.825
        float_1 = -791.592
        var_0 = module_0.hostcolor(tuple_0, float_1)
        str_1 = "T:'}[']O\n*f9`MiS/8&T"
        list_0 = None
        var_1 = module_0.stringc(float_0, str_1, list_0)
        int_0 = 741
        bool_0 = False
        bytes_0 = b'\x0b\xdc\x84\xbd\xeaH^\no'
        var_2 = module_0.colorize(int_0, bool_0, bytes_0)
        str_2 = '_terms'
        bytes_1 = b'\x0f\xda\xf4\xc5\x8c*D\xb7\x18G\xc3~^\tT\xc7O'
        var_3 = module_0.colorize(str_0, str_2, bytes_1)
        var_4 = module_0.parsecolor(str_0)
    except BaseException:
        pass