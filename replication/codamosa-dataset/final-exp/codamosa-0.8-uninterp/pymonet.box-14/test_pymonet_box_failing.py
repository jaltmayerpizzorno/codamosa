# Automatically generated by Pynguin.
import pymonet.box as module_0

def test_case_0():
    try:
        callable_0 = None
        bool_0 = False
        box_0 = module_0.Box(bool_0)
        var_0 = box_0.to_either()
        bytes_0 = b'm\x90\x9d\x93\x0e'
        box_1 = module_0.Box(bytes_0)
        var_1 = box_1.to_lazy()
        var_2 = box_1.map(callable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        str_0 = "\x0crU;~A'C"
        box_0 = module_0.Box(str_0)
        var_0 = box_0.bind(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = None
        bool_0 = True
        list_0 = [bool_0, var_0]
        float_0 = 4672.0
        box_0 = module_0.Box(float_0)
        var_1 = box_0.ap(list_0)
    except BaseException:
        pass