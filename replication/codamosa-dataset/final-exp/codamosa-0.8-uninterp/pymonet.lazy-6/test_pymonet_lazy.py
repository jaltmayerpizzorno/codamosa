# Automatically generated by Pynguin.
import pymonet.lazy as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    float_0 = 2336.8
    list_0 = [float_0, float_0]
    lazy_0 = module_0.Lazy(list_0)

def test_case_2():
    list_0 = []
    lazy_0 = module_0.Lazy(list_0)
    object_0 = module_1.object()
    bool_0 = lazy_0.__eq__(object_0)
    str_0 = lazy_0.__str__()

def test_case_3():
    str_0 = '\n    Unt test for __eq__ method of class Lazy.\n    '
    lazy_0 = module_0.Lazy(str_0)
    var_0 = lazy_0 == lazy_0

def test_case_4():
    var_0 = lambda x: x
    lazy_0 = module_0.Lazy(var_0)
    lazy_1 = module_0.Lazy(var_0)
    var_1 = None
    var_2 = lambda *x: var_1
    var_3 = lazy_1 == lazy_1
    list_0 = [var_0]
    var_4 = lazy_1.to_maybe(*list_0)
    str_0 = lazy_1.__str__()
    var_5 = lazy_1.to_maybe()
    object_0 = module_1.object()