# Automatically generated by Pynguin.
import pymonet.utils as module_0

def test_case_0():
    try:
        var_0 = None
        var_1 = module_0.identity(var_0)
        var_2 = module_0.identity(var_1)
        var_3 = module_0.identity(var_2)
        list_0 = [var_1, var_3, var_0, var_2]
        var_4 = module_0.pipe(var_3, *list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = True
        int_1 = module_0.increase(int_0)
        var_0 = module_0.fn()
    except BaseException:
        pass

def test_case_2():
    try:
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        list_0 = [callable_1]
        var_0 = module_0.compose(callable_1, *list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        dict_0 = {str_0: str_0}
        bool_0 = False
        var_0 = module_0.curry(dict_0, bool_0)
        var_1 = module_0.fn()
    except BaseException:
        pass