# Automatically generated by Pynguin.
import pysnooper.utils as module_0

def test_case_0():
    try:
        set_0 = set()
        var_0 = module_0.normalize_repr(set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = ()
        int_0 = 10
        var_1 = module_0.get_shortish_repr(int_0, var_0, int_0)
        bytes_0 = b'eggg'
        var_2 = module_0.get_shortish_repr(bytes_0, bytes_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '1b<V?Ox2myX4T_.H'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.get_repr_function(str_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '$_'
        bool_0 = False
        var_0 = module_0.ensure_tuple(bool_0)
        str_1 = 'Ca|+\tn5!/\\d'
        list_0 = [str_0, str_1, str_1, bool_0]
        var_1 = module_0.normalize_repr(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'rb'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        list_0 = [str_0, dict_0, str_0, str_0]
        var_0 = module_0.get_repr_function(dict_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = lambda x: x
        str_0 = 'my lambda'
        var_1 = (var_0, str_0)
        var_2 = (var_1,)
        bool_0 = True
        var_3 = module_0.get_shortish_repr(var_0, var_2, bool_0)
        var_4 = lambda x: x
        int_0 = 12
        var_5 = module_0.get_shortish_repr(var_4, int_0)
    except BaseException:
        pass