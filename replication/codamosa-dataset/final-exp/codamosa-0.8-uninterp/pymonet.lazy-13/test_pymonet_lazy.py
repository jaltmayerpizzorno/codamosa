# Automatically generated by Pynguin.
import pymonet.lazy as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    int_0 = 2492
    lazy_0 = module_0.Lazy(int_0)

def test_case_2():
    int_0 = 2492
    lazy_0 = module_0.Lazy(int_0)
    str_0 = lazy_0.__str__()

def test_case_3():
    var_0 = lambda v: v
    lazy_0 = module_0.Lazy(var_0)
    bool_0 = lazy_0.__eq__(lazy_0)

def test_case_4():
    object_0 = module_1.object()
    str_0 = '.<.;-NQ1Q'
    lazy_0 = module_0.Lazy(str_0)
    str_1 = 'oa~c5LE[c:-kg08B'
    var_0 = lazy_0.map(str_1)
    bool_0 = lazy_0.__eq__(object_0)

def test_case_5():
    dict_0 = {}
    bool_0 = False
    callable_0 = None
    lazy_0 = module_0.Lazy(callable_0)
    lazy_1 = module_0.Lazy(bool_0)
    var_0 = lazy_1.bind(dict_0)

def test_case_6():
    float_0 = -370.0
    bool_0 = False
    list_0 = [float_0, float_0, float_0, bool_0]
    bool_1 = False
    lazy_0 = module_0.Lazy(bool_1)
    var_0 = lazy_0.to_try()
    lazy_1 = module_0.Lazy(list_0)

def test_case_7():
    object_0 = module_1.object()
    str_0 = '.<.;-NQ1Q'
    lazy_0 = module_0.Lazy(str_0)
    bool_0 = lazy_0.__eq__(object_0)