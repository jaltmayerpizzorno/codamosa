# Automatically generated by Pynguin.
import pymonet.box as module_0
import builtins as module_1

def test_case_0():
    int_0 = 10
    box_0 = module_0.Box(int_0)

def test_case_1():
    object_0 = module_1.object()
    bool_0 = True
    box_0 = module_0.Box(bool_0)
    bool_1 = box_0.__eq__(object_0)

def test_case_2():
    set_0 = set()
    box_0 = module_0.Box(set_0)
    str_0 = box_0.__str__()

def test_case_3():
    dict_0 = {}
    box_0 = module_0.Box(dict_0)
    var_0 = box_0.to_maybe()
    tuple_0 = ()
    box_1 = module_0.Box(tuple_0)
    var_1 = box_1.to_lazy()

def test_case_4():
    bytes_0 = b'\x18'
    box_0 = module_0.Box(bytes_0)
    var_0 = box_0.to_either()
    int_0 = 1276
    box_1 = module_0.Box(int_0)
    var_1 = box_1.to_try()

def test_case_5():
    set_0 = set()
    box_0 = module_0.Box(set_0)
    var_0 = box_0.to_lazy()

def test_case_6():
    str_0 = 'QGBt%b!{\x0bZdr[y?<J"5S'
    box_0 = module_0.Box(str_0)
    var_0 = box_0.to_try()
    bytes_0 = b'\xc6Q\x8aqv\x8d\x89-t\x95\xfc\x04\xdb\xe3\xda'
    int_0 = 1220
    box_1 = module_0.Box(int_0)
    var_1 = box_1.to_validation()
    box_2 = module_0.Box(bytes_0)

def test_case_7():
    int_0 = 1
    box_0 = module_0.Box(int_0)
    box_1 = module_0.Box(int_0)
    box_2 = module_0.Box(int_0)
    int_1 = 2
    box_3 = module_0.Box(int_1)
    var_0 = box_2 == box_3
    box_4 = module_0.Box(int_0)