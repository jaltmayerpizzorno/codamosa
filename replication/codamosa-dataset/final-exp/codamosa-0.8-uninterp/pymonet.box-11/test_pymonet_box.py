# Automatically generated by Pynguin.
import builtins as module_0
import pymonet.box as module_1

def test_case_0():
    pass

def test_case_1():
    object_0 = module_0.object()
    box_0 = module_1.Box(object_0)

def test_case_2():
    object_0 = module_0.object()
    float_0 = -2808.51
    box_0 = module_1.Box(float_0)
    var_0 = box_0.to_lazy()
    box_1 = module_1.Box(object_0)
    var_1 = box_0.to_either()
    bool_0 = box_0.__eq__(object_0)

def test_case_3():
    str_0 = '\n    Return increased by 1 argument.\n\n    :param value:\n    :type value: Int\n    :returns:\n    :rtype: Int\n    '
    box_0 = module_1.Box(str_0)
    str_1 = box_0.__str__()
    str_2 = 'oQxHh4"Wz,e[SX d'
    box_1 = module_1.Box(str_2)
    var_0 = box_1.to_maybe()

def test_case_4():
    str_0 = 'QKWw'
    box_0 = module_1.Box(str_0)
    var_0 = box_0.to_maybe()

def test_case_5():
    bool_0 = False
    box_0 = module_1.Box(bool_0)
    var_0 = box_0.to_either()
    str_0 = '\n        Two Validations are equals when values and errors lists are equal.\n        '
    box_1 = module_1.Box(str_0)
    var_1 = box_1.to_validation()

def test_case_6():
    object_0 = module_0.object()
    box_0 = module_1.Box(object_0)
    box_1 = module_1.Box(box_0)
    bytes_0 = b'\xc0\x8b4\xb8\x1f\x0e'
    box_2 = module_1.Box(bytes_0)
    var_0 = box_2.to_lazy()

def test_case_7():
    object_0 = module_0.object()
    box_0 = module_1.Box(object_0)
    var_0 = box_0.to_try()
    str_0 = 'b}A?j giB|t(4w\x0bE'
    var_1 = None
    box_1 = module_1.Box(var_1)
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_2 = box_1.to_either()
    box_2 = module_1.Box(dict_0)
    var_3 = box_2.to_maybe()

def test_case_8():
    str_0 = 'test'
    box_0 = module_1.Box(str_0)
    box_1 = module_1.Box(str_0)
    str_1 = 'test1'
    var_0 = box_1 == str_1
    box_2 = module_1.Box(str_0)
    box_3 = module_1.Box(str_0)
    box_4 = module_1.Box(str_0)
    box_5 = module_1.Box(str_1)
    var_1 = box_4 == box_5