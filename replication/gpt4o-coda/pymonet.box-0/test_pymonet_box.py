# Automatically generated by Pynguin.
import pymonet.box as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'rk?'
    box_0 = module_0.Box(str_0)

def test_case_2():
    object_0 = module_1.object()
    box_0 = module_0.Box(object_0)
    bool_0 = box_0.__eq__(object_0)

def test_case_3():
    var_0 = None
    box_0 = module_0.Box(var_0)
    list_0 = [box_0]
    list_1 = [list_0, list_0, box_0]
    box_1 = module_0.Box(list_1)
    str_0 = box_1.__str__()

def test_case_4():
    bool_0 = True
    box_0 = module_0.Box(bool_0)
    object_0 = None
    bool_1 = box_0.__eq__(object_0)
    var_0 = box_0.to_maybe()
    var_1 = box_0.to_lazy()

def test_case_5():
    int_0 = 1447
    box_0 = module_0.Box(int_0)
    var_0 = box_0.to_lazy()

def test_case_6():
    int_0 = -1490
    box_0 = module_0.Box(int_0)
    var_0 = box_0.to_try()

def test_case_7():
    int_0 = -1048
    box_0 = module_0.Box(int_0)
    var_0 = box_0.to_validation()
    var_1 = box_0.to_try()