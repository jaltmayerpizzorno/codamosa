# Automatically generated by Pynguin.
import pymonet.lazy as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    callable_0 = None
    lazy_0 = module_0.Lazy(callable_0)

def test_case_2():
    bytes_0 = b')\xdf\xaes\xd9\x94\x02\x16\xa1\xea]{L'
    lazy_0 = module_0.Lazy(bytes_0)
    str_0 = lazy_0.__str__()
    str_1 = '\n        Take function (A) -> B and applied this function on current Validation value.\n\n        :param mapper: mapper function\n        :type mapper: Function(A) -> B\n        :returns: new Validation with mapped value and previous errors\n        :rtype: Validation[B, List[E]]\n        '
    lazy_1 = module_0.Lazy(str_1)

def test_case_3():
    str_0 = 'lazy1'
    lazy_0 = module_0.Lazy(str_0)
    var_0 = lazy_0 == lazy_0

def test_case_4():
    object_0 = module_1.object()
    set_0 = set()
    lazy_0 = module_0.Lazy(set_0)
    bool_0 = lazy_0.__eq__(object_0)
    bytes_0 = b'>o8\xd1\xb5'
    var_0 = lazy_0.ap(bytes_0)

def test_case_5():
    object_0 = module_1.object()
    bool_0 = False
    lazy_0 = module_0.Lazy(bool_0)
    bool_1 = lazy_0.__eq__(object_0)

def test_case_6():
    var_0 = lambda x: x
    lazy_0 = module_0.Lazy(var_0)
    list_0 = [lazy_0]
    var_1 = lazy_0.to_box(*list_0)
    int_0 = 2
    var_2 = lambda x: x * int_0
    var_3 = lazy_0.map(var_2)
    var_4 = lambda x, y: x + y
    lazy_1 = module_0.Lazy(var_4)
    var_5 = lambda x: x * int_0
    var_6 = lazy_1.map(var_5)

def test_case_7():
    var_0 = lambda x: x
    lazy_0 = module_0.Lazy(var_0)
    list_0 = [lazy_0]
    var_1 = lazy_0.to_box(*list_0)
    int_0 = 2
    var_2 = lambda x: x * int_0
    var_3 = lazy_0.map(var_2)
    var_4 = lambda x, y: x + y
    lazy_1 = module_0.Lazy(var_4)
    var_5 = lambda x: x * int_0
    var_6 = lazy_1.map(var_5)
    var_7 = lazy_0.to_box()