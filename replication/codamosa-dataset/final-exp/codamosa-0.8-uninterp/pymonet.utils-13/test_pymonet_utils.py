# Automatically generated by Pynguin.
import pymonet.utils as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = False
    int_1 = module_0.increase(int_0)

def test_case_2():
    bool_0 = False
    list_0 = []
    var_0 = module_0.cond(list_0)
    list_1 = [var_0]
    var_1 = module_0.pipe(bool_0, *list_1)

def test_case_3():
    callable_0 = None
    callable_1 = module_0.memoize(callable_0)