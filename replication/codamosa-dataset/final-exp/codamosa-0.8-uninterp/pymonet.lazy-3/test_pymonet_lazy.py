# Automatically generated by Pynguin.
import pymonet.lazy as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    float_0 = 2594.086168
    lazy_0 = module_0.Lazy(float_0)

def test_case_2():
    int_0 = 0
    var_0 = lambda *args: Error(args[int_0])
    lazy_0 = module_0.Lazy(var_0)
    var_1 = lambda *args: Error(args[int_0])
    lazy_1 = module_0.Lazy(var_1)
    var_2 = lambda *args: Error(args[int_0])
    str_0 = lazy_0.__str__()
    lazy_2 = module_0.Lazy(var_2)
    var_3 = lambda *args: Error(args[int_0])
    lazy_3 = module_0.Lazy(var_3)
    var_4 = lazy_2 == lazy_3

def test_case_3():
    int_0 = 17
    lazy_0 = module_0.Lazy(int_0)
    var_0 = lazy_0 == lazy_0

def test_case_4():
    str_0 = "9'!\x0b|uP.xAz-K ;)tfD("
    dict_0 = {str_0: str_0}
    str_1 = 'D.G9['
    lazy_0 = module_0.Lazy(str_1)
    var_0 = lazy_0.map(dict_0)

def test_case_5():
    int_0 = 0
    var_0 = lambda *args: Error(args[int_0])
    lazy_0 = module_0.Lazy(var_0)
    var_1 = lambda *args: Error(args[lazy_0])
    lazy_1 = module_0.Lazy(var_1)
    var_2 = lambda *args: Error(args[int_0])
    lazy_2 = module_0.Lazy(var_2)
    var_3 = lambda *args: Error(args[int_0])
    float_0 = -921.460215
    var_4 = lazy_0.ap(float_0)
    lazy_3 = module_0.Lazy(var_3)
    var_5 = lazy_2 == lazy_3

def test_case_6():
    callable_0 = None
    object_0 = module_1.object()
    set_0 = {object_0, object_0}
    lazy_0 = module_0.Lazy(set_0)
    var_0 = lazy_0.bind(callable_0)
    bool_0 = True
    set_1 = {bool_0, bool_0, bool_0}
    lazy_1 = module_0.Lazy(set_1)
    var_1 = lazy_1.bind(var_0)

def test_case_7():
    dict_0 = {}
    lazy_0 = module_0.Lazy(dict_0)
    var_0 = lazy_0.to_try()

def test_case_8():
    object_0 = module_1.object()
    str_0 = 'Bm]]IgW;N:pM"S3N,OS,'
    lazy_0 = module_0.Lazy(str_0)
    bool_0 = lazy_0.__eq__(object_0)