# Automatically generated by Pynguin.
import pymonet.lazy as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'D\x17=\x1cV\xc0\x83\x94\xfd'
    lazy_0 = module_0.Lazy(bytes_0)

def test_case_2():
    str_0 = ';d'
    bytes_0 = b'\xe6#\xfa\x92^\xfdA\x13\xcc\xf3U\x8dp\x97'
    lazy_0 = module_0.Lazy(bytes_0)
    str_1 = lazy_0.__str__()
    lazy_1 = module_0.Lazy(str_0)
    str_2 = lazy_1.__str__()

def test_case_3():
    var_0 = lambda x: x
    lazy_0 = module_0.Lazy(var_0)
    bool_0 = lazy_0.__eq__(lazy_0)

def test_case_4():
    callable_0 = None
    bytes_0 = b'\\\xb1\xcc'
    lazy_0 = module_0.Lazy(bytes_0)
    var_0 = lazy_0.map(callable_0)

def test_case_5():
    bytes_0 = b'WV'
    object_0 = None
    float_0 = 2748.22893
    lazy_0 = module_0.Lazy(float_0)
    dict_0 = {bytes_0: bytes_0, bytes_0: object_0, bytes_0: bytes_0}
    callable_0 = None
    list_0 = [dict_0, bytes_0, dict_0, bytes_0]
    int_0 = False
    var_0 = lazy_0.ap(int_0)
    bool_0 = lazy_0.__eq__(object_0)
    var_1 = lazy_0.map(list_0)
    lazy_1 = module_0.Lazy(callable_0)

def test_case_6():
    callable_0 = None
    bytes_0 = b'\\\xb1\xcc'
    lazy_0 = module_0.Lazy(bytes_0)
    object_0 = module_1.object()
    bool_0 = lazy_0.__eq__(object_0)
    var_0 = lazy_0.map(callable_0)
    var_1 = lazy_0.to_try()

def test_case_7():
    object_0 = module_1.object()
    str_0 = '!\t_kg?;]8{'
    lazy_0 = module_0.Lazy(str_0)
    bool_0 = lazy_0.__eq__(object_0)

def test_case_8():
    var_0 = lambda x: x
    lazy_0 = module_0.Lazy(var_0)
    var_1 = lambda x: x
    lazy_1 = module_0.Lazy(var_1)
    bool_0 = lazy_0.__eq__(lazy_1)
    var_2 = lambda x: x
    list_0 = [var_2]
    var_3 = lazy_1.get(*list_0)
    lazy_2 = module_0.Lazy(var_2)
    object_0 = module_1.object()

def test_case_9():
    var_0 = lambda x: x
    lazy_0 = module_0.Lazy(var_0)
    var_1 = lambda x: x
    lazy_1 = module_0.Lazy(var_1)
    bool_0 = lazy_0.__eq__(lazy_1)
    var_2 = lambda x: x
    list_0 = [var_2]
    var_3 = lazy_1.get(*list_0)
    lazy_2 = module_0.Lazy(var_2)
    var_4 = lazy_1.get()

def test_case_10():
    var_0 = lambda x: x
    lazy_0 = module_0.Lazy(var_0)
    var_1 = lambda x: x
    lazy_1 = module_0.Lazy(var_1)
    list_0 = [lazy_0]
    var_2 = lazy_1.to_either(*list_0)
    bool_0 = lazy_0.__eq__(lazy_1)
    var_3 = lambda x: x
    list_1 = [var_3]
    var_4 = lazy_1.get(*list_1)
    lazy_2 = module_0.Lazy(var_3)
    var_5 = lazy_1.get()