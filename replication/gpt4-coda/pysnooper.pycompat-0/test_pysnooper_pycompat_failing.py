# Automatically generated by Pynguin.
import pysnooper.pycompat as module_0
import datetime as module_1

def test_case_0():
    try:
        str_0 = '@'
        var_0 = module_0.timedelta_format(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '7WEpP\r'
        var_0 = module_0.timedelta_parse(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '12:34:56.789012'
        var_0 = module_0.timedelta_parse(str_0)
        int_0 = 12
        str_1 = 'ZL%/X'
        dict_0 = {str_1: int_0}
        timedelta_0 = module_1.timedelta(**dict_0)
    except BaseException:
        pass