# Automatically generated by Pynguin.
import pymonet.lazy as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\xe3\x0f\xcd\xa02\xc2@\x91TA\xe0U\xe7'
    lazy_0 = module_0.Lazy(bytes_0)

def test_case_2():
    object_0 = module_1.object()
    list_0 = []
    lazy_0 = module_0.Lazy(list_0)
    bool_0 = lazy_0.__eq__(object_0)
    str_0 = lazy_0.__str__()

def test_case_3():
    object_0 = module_1.object()
    bytes_0 = b'\xe3\x0f\xcd\xa02\xc2@\x91TA\xe0U\xe7'
    lazy_0 = module_0.Lazy(bytes_0)
    bool_0 = lazy_0.__eq__(object_0)

def test_case_4():
    str_0 = '6Q9k)\x0c5B)^j'
    dict_0 = {str_0: str_0}
    lazy_0 = module_0.Lazy(dict_0)
    var_0 = lazy_0.map(str_0)
    object_0 = module_1.object()
    bool_0 = lazy_0.__eq__(object_0)

def test_case_5():
    set_0 = None
    bool_0 = False
    lazy_0 = module_0.Lazy(set_0)
    var_0 = lambda *args: bool_0
    var_1 = lazy_0 == lazy_0

def test_case_6():
    bool_0 = True
    str_0 = None
    str_1 = 'w8fH\tm'
    str_2 = 'op"\x0bS'
    dict_0 = {str_0: bool_0, str_1: str_0, str_2: str_0}
    list_0 = [bool_0, bool_0]
    lazy_0 = module_0.Lazy(list_0)
    var_0 = lazy_0.map(dict_0)
    var_1 = lambda *args: bool_0
    lazy_1 = module_0.Lazy(var_1)
    var_2 = lambda *args: bool_0
    var_3 = lambda *args: bool_0
    lazy_2 = module_0.Lazy(var_3)
    var_4 = lambda x: x
    var_5 = lazy_2.map(var_4)
    var_6 = lambda *args: bool_0
    lazy_3 = module_0.Lazy(var_6)
    var_7 = lambda x: x
    var_8 = lazy_3.map(var_7)
    str_3 = 'D<MN-nz_IK~yfF"p{~*u'
    bytes_0 = b'\x91\xe0/A\xf77\x11\xc3\x1b'
    dict_1 = {str_3: bytes_0, str_3: bytes_0}
    var_9 = lazy_3.map(dict_1)
    lazy_4 = module_0.Lazy(var_4)
    var_10 = lambda *args: var_3
    lazy_5 = module_0.Lazy(var_10)
    var_11 = lazy_4 == lazy_5
    list_1 = [lazy_2]
    var_12 = lazy_4.to_validation(*list_1)
    var_13 = lambda *args: bool_0
    lazy_6 = module_0.Lazy(var_13)
    var_14 = None
    var_15 = lambda *args: var_14
    lazy_7 = module_0.Lazy(var_15)
    var_16 = lazy_6 == lazy_7