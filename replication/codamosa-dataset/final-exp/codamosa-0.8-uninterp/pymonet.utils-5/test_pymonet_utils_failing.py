# Automatically generated by Pynguin.
import pymonet.utils as module_0

def test_case_0():
    try:
        var_0 = module_0.fn()
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        var_0 = module_0.pipe(dict_0)
        var_1 = module_0.fn()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 1315
        set_0 = {int_0, int_0}
        int_1 = 1120
        list_0 = [int_0, int_0, int_1, int_1]
        var_0 = module_0.pipe(set_0, *list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -1838.00504
        int_0 = -882
        var_0 = module_0.curry(float_0, int_0)
        bytes_0 = b'\xd4\x9ch'
        var_1 = module_0.curry(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        list_0 = [callable_1]
        var_0 = module_0.compose(callable_1, *list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\n    The Try control gives us the ability write safe code\n    without focusing on try-catch blocks in the presence of exceptions.\n    '
        callable_0 = None
        tuple_0 = (str_0, callable_0)
        list_0 = [tuple_0, tuple_0]
        var_0 = module_0.cond(list_0)
        callable_1 = None
        list_1 = [tuple_0, tuple_0]
        list_2 = None
        callable_2 = module_0.memoize(callable_1, list_2)
        var_1 = module_0.cond(list_1)
        callable_3 = module_0.memoize(callable_1)
        bool_0 = False
        tuple_1 = (bool_0,)
        var_2 = module_0.pipe(tuple_1)
        bytes_0 = b'\x81\x157\xc8\x13q\x9b\x1c\x05\nO'
        list_3 = [bytes_0, bytes_0, callable_2, var_1]
        var_3 = module_0.compose(bytes_0, *list_3)
    except BaseException:
        pass