# Automatically generated by Pynguin.
import pymonet.utils as module_0

def test_case_0():
    try:
        callable_0 = None
        var_0 = None
        var_1 = module_0.identity(var_0)
        callable_1 = module_0.memoize(callable_0)
        list_0 = [callable_1, callable_0, callable_1, callable_0, callable_0, callable_0, callable_0, callable_1]
        var_2 = module_0.pipe(callable_1, *list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        int_0 = 185
        int_1 = module_0.increase(int_0)
        list_0 = [callable_1, callable_1, callable_0, callable_0, callable_0, callable_0, callable_0]
        var_0 = module_0.pipe(callable_1, *list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        list_0 = [callable_0, callable_1]
        var_0 = module_0.compose(callable_1, *list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        list_0 = [callable_1, callable_1, callable_0, callable_0, callable_0, callable_1]
        var_0 = module_0.pipe(callable_1, *list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = None
        var_0 = module_0.cond(list_0)
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        list_1 = [callable_1, callable_1, callable_0, callable_1, callable_0]
        var_1 = module_0.pipe(list_1, *list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\n        Transform Validation to Try.\n\n        :returns: successfully Try with Validation value value. Try is successful when Validation has no errors\n        :rtype: Try[A]\n        '
        float_0 = 2.0
        var_0 = module_0.curry(str_0, float_0)
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        list_0 = [callable_1, callable_0, callable_1, callable_1, callable_1]
        var_1 = module_0.pipe(list_0, *list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        callable_0 = None
        callable_1 = module_0.memoize(callable_0)
        bool_0 = False
        var_0 = module_0.curry(callable_0, bool_0)
        callable_2 = module_0.memoize(callable_1)
        str_0 = ''
        int_0 = -1492
        list_0 = [var_0, str_0, bool_0]
        var_1 = module_0.pipe(int_0, *list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = None
        callable_0 = None
        tuple_0 = (set_0, callable_0)
        list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
        str_0 = '8w,hE{\x0bpRv~~h8t}%Ev$'
        var_0 = module_0.cond(list_0)
        bool_0 = True
        list_1 = [str_0, var_0]
        var_1 = module_0.compose(bool_0, *list_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '8w]hE{\x0bpRv~~h8t%Ev$'
        list_0 = []
        var_0 = module_0.cond(list_0)
        list_1 = [str_0, var_0]
        var_1 = module_0.compose(list_0, *list_1)
    except BaseException:
        pass