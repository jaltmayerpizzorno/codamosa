# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    try:
        bool_0 = False
        str_0 = '\nb|\t'
        bool_1 = False
        maybe_0 = module_0.Maybe(str_0, bool_1)
        var_0 = maybe_0.map(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ']An!OD\\|H'
        list_0 = [str_0, str_0, str_0, str_0]
        bool_0 = False
        maybe_0 = module_0.Maybe(list_0, bool_0)
        callable_0 = None
        var_0 = maybe_0.bind(callable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -473.6403
        str_0 = 'tZ@#D2Az?&V'
        str_1 = 'exy=\x0cA \tWERtY'
        bool_0 = True
        dict_0 = None
        tuple_0 = (str_1, bool_0, dict_0)
        tuple_1 = (float_0, str_0, tuple_0)
        dict_1 = {}
        bool_1 = False
        maybe_0 = module_0.Maybe(dict_1, bool_1)
        var_0 = maybe_0.ap(tuple_1)
    except BaseException:
        pass

def test_case_3():
    try:
        object_0 = module_1.object()
        bool_0 = True
        maybe_0 = module_0.Maybe(object_0, bool_0)
        var_0 = maybe_0.filter(bool_0)
        var_1 = None
        bool_1 = False
        maybe_1 = module_0.Maybe(var_1, bool_1)
        var_2 = maybe_1.filter(maybe_1)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'R'
        str_0 = "3;'\\D&k"
        bool_0 = False
        maybe_0 = module_0.Maybe(str_0, bool_0)
        var_0 = maybe_0.filter(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xa5h\x05\xeftle<\xd9\x90\xc0\xc2\x9eb\x8f\x8f\xf1c{\x17'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        str_0 = '\n        Take function, store it and call with Task value during calling fork function.\n        Return new Task with result of called.\n\n        :param fn: mapper function\n        :type fn: Function(value) -> B\n        :returns: new Task with mapped resolve attribute\n        :rtype: Task[Function(resolve, reject -> A | B]\n        '
        tuple_0 = ()
        dict_0 = {str_0: list_0}
        bool_0 = True
        maybe_0 = module_0.Maybe(dict_0, bool_0)
        object_0 = module_1.object()
        bool_1 = maybe_0.__eq__(object_0)
        var_0 = maybe_0.get_or_else(tuple_0)
        var_1 = maybe_0.to_box()
        maybe_1 = module_0.Maybe(maybe_0, bool_0)
        var_2 = maybe_1.to_box()
        dict_1 = {str_0: str_0, str_0: str_0}
        bool_2 = False
        var_3 = maybe_0.to_try()
        maybe_2 = module_0.Maybe(dict_1, bool_2)
        var_4 = maybe_2.to_box()
        var_5 = maybe_2.map(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        object_0 = module_1.object()
        bool_0 = True
        maybe_0 = module_0.Maybe(object_0, bool_0)
        var_0 = maybe_0.filter(bool_0)
        var_1 = maybe_0.to_box()
        var_2 = maybe_0.to_either()
        var_3 = None
        maybe_1 = module_0.Maybe(var_3, bool_0)
        int_0 = 435
        bool_1 = False
        maybe_2 = module_0.Maybe(var_3, bool_1)
        var_4 = maybe_2.filter(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'mEf;\x0c<v[U*;'
        tuple_0 = (str_0,)
        bool_0 = True
        maybe_0 = module_0.Maybe(str_0, bool_0)
        bool_1 = False
        maybe_1 = module_0.Maybe(tuple_0, bool_1)
        maybe_2 = module_0.Maybe(tuple_0, bool_1)
        var_0 = maybe_1.to_either()
        str_1 = '9\r0JY'
        str_2 = '!8'
        dict_0 = {str_1: str_1, str_2: str_1, str_2: tuple_0, str_1: str_0}
        var_1 = maybe_0.to_either()
        var_2 = None
        var_3 = maybe_0.get_or_else(var_2)
        var_4 = maybe_2.to_validation()
        var_5 = maybe_2.bind(dict_0)
    except BaseException:
        pass