# Automatically generated by Pynguin.
import pymonet.box as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'a'
    box_0 = module_0.Box(str_0)

def test_case_2():
    bytes_0 = b'r'
    box_0 = module_0.Box(bytes_0)
    str_0 = box_0.__str__()
    object_0 = module_1.object()
    bool_0 = box_0.__eq__(object_0)

def test_case_3():
    bytes_0 = b'r'
    box_0 = module_0.Box(bytes_0)
    str_0 = box_0.__str__()

def test_case_4():
    list_0 = []
    box_0 = module_0.Box(list_0)
    box_1 = module_0.Box(box_0)
    var_0 = box_1.to_lazy()
    bytes_0 = b'r'
    box_2 = module_0.Box(bytes_0)
    str_0 = box_2.__str__()

def test_case_5():
    int_0 = 204
    box_0 = module_0.Box(int_0)
    box_1 = module_0.Box(box_0)
    object_0 = module_1.object()
    bool_0 = box_0.__eq__(object_0)
    var_0 = box_1.to_try()

def test_case_6():
    int_0 = 1
    box_0 = module_0.Box(int_0)
    box_1 = module_0.Box(int_0)
    int_1 = 2
    box_2 = module_0.Box(int_1)
    var_0 = box_0 == box_2