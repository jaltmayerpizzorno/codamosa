# Automatically generated by Pynguin.
import pymonet.utils as module_0

def test_case_0():
    try:
        var_0 = module_0.fn()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 2616
        int_1 = module_0.increase(int_0)
        var_0 = module_0.fn()
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = None
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        list_0 = [callable_1, callable_1]
        var_0 = module_0.compose(dict_0, *list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        callable_0 = None
        dict_0 = {callable_0: callable_0, callable_0: callable_0}
        tuple_0 = (dict_0, callable_0)
        list_0 = [tuple_0]
        var_0 = module_0.cond(list_0)
        list_1 = []
        var_1 = module_0.pipe(list_1)
        var_2 = module_0.fn()
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 2940.02798
        bool_0 = True
        int_0 = -1542
        int_1 = module_0.increase(int_0)
        var_0 = module_0.curry(float_0, bool_0)
        bool_1 = True
        var_1 = module_0.compose(bool_1)
        var_2 = module_0.fn()
    except BaseException:
        pass

def test_case_5():
    try:
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        list_0 = None
        str_0 = ']F\t0b.<ez GWI;Ms$,xJ'
        list_1 = [callable_1, list_0]
        var_0 = module_0.pipe(str_0, *list_1)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = None
        var_0 = module_0.cond(list_0)
        int_0 = 314
        var_1 = module_0.compose(int_0)
        int_1 = -1616
        list_1 = [int_0, var_0]
        var_2 = module_0.cond(list_0)
        var_3 = module_0.compose(int_1, *list_1)
    except BaseException:
        pass