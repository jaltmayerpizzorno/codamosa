# Automatically generated by Pynguin.
import pysnooper.utils as module_0

def test_case_0():
    try:
        float_0 = 1177.1341
        var_0 = module_0.shitcode(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = None
        var_0 = module_0.normalize_repr(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "'FGwk2'^\x0bb2e<^"
        dict_0 = {str_0: str_0}
        bool_0 = False
        var_0 = module_0.truncate(dict_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 30
        var_0 = module_0.get_shortish_repr(int_0)
        str_0 = '`N<D9.K)!7F&J\r!71p'
        dict_0 = {int_0: int_0, int_0: str_0, int_0: var_0}
        var_1 = module_0.get_shortish_repr(str_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 10
        var_0 = module_0.get_shortish_repr(int_0)
        str_0 = '`|<D9.)!7F&\r7p'
        dict_0 = {var_0: var_0, int_0: str_0}
        var_1 = module_0.get_shortish_repr(str_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'LO-!~ \t31OJmqMYamcp\t'
        var_0 = module_0.shitcode(str_0)
        bytes_0 = b'h\x80&\\'
        var_1 = module_0.get_shortish_repr(bytes_0)
        float_0 = -0.8
        list_0 = None
        var_2 = module_0.truncate(float_0, list_0)
        set_0 = {str_0}
        var_3 = module_0.shitcode(set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = "'FGwk2'^\x0bb2e<^"
        dict_0 = {str_0: str_0}
        list_0 = [dict_0, str_0]
        var_0 = module_0.ensure_tuple(list_0)
        str_1 = 'LO-!~ \t31OJmqMYamcp\t'
        var_1 = module_0.shitcode(str_1)
        bytes_0 = b' *\x80l\xc5[p\x87vF'
        dict_1 = {}
        str_2 = 'sh~b}qb&\x0b].JGt<YtB?'
        var_2 = module_0.get_shortish_repr(bytes_0, dict_1, str_2)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = -928.23363
        var_0 = module_0.ensure_tuple(float_0)
        str_0 = 'uQRv:/WD\\F\r>As)_aN%D'
        list_0 = []
        dict_0 = None
        str_1 = 'SZ1/4(lTgWD;>V'
        var_1 = module_0.get_shortish_repr(str_0, list_0, dict_0, str_1)
        set_0 = {var_0, var_0}
        str_2 = 'c\x0c3\x0ct\tP'
        dict_1 = {str_2: set_0, str_2: var_0}
        var_2 = module_0.get_repr_function(set_0, dict_1)
    except BaseException:
        pass