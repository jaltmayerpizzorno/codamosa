# Automatically generated by Pynguin.
import pymonet.lazy as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'c\\@[-T94Eo#yK)367kTa'
    lazy_0 = module_0.Lazy(str_0)
    str_1 = lazy_0.__str__()
    object_0 = module_1.object()
    list_0 = []
    lazy_1 = module_0.Lazy(list_0)
    bool_0 = lazy_1.__eq__(object_0)

def test_case_2():
    object_0 = None
    lazy_0 = module_0.Lazy(object_0)
    bool_0 = lazy_0.__eq__(object_0)

def test_case_3():
    object_0 = None
    list_0 = [object_0, object_0, object_0, object_0]
    int_0 = -1503
    lazy_0 = module_0.Lazy(int_0)
    var_0 = lazy_0.map(list_0)

def test_case_4():
    bytes_0 = b'\xa7\xdb\x1b+\xfb\xa5)\x18\xe1j^\xb9'
    lazy_0 = module_0.Lazy(bytes_0)
    var_0 = lazy_0.to_try()

def test_case_5():
    var_0 = lambda x: x
    lazy_0 = module_0.Lazy(var_0)
    var_1 = lazy_0 == lazy_0

def test_case_6():
    var_0 = lambda x: x
    lazy_0 = module_0.Lazy(var_0)
    list_0 = [var_0]
    var_1 = lazy_0.to_maybe(*list_0)
    var_2 = lambda : var_0
    lazy_1 = module_0.Lazy(var_2)
    object_0 = module_1.object()
    bool_0 = lazy_1.__eq__(object_0)
    var_3 = lazy_1 == lazy_1
    var_4 = lambda x: x
    var_5 = lambda x: x
    var_6 = lazy_0.to_validation()