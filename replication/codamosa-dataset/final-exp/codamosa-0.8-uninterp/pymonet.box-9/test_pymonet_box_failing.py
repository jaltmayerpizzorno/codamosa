# Automatically generated by Pynguin.
import pymonet.box as module_0

def test_case_0():
    try:
        callable_0 = None
        bool_0 = True
        box_0 = module_0.Box(bool_0)
        var_0 = box_0.map(callable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -1571
        bool_0 = True
        box_0 = module_0.Box(bool_0)
        var_0 = box_0.bind(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        str_0 = 't>vt_iI~_r%"sPX^-.'
        box_0 = module_0.Box(str_0)
        var_0 = box_0.ap(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        float_0 = -37.314396
        box_0 = module_0.Box(float_0)
        var_0 = box_0.to_try()
        box_1 = module_0.Box(bool_0)
        var_1 = box_1.to_maybe()
        str_0 = 'aR3F|aawG]E1d?qmr'
        bool_1 = True
        box_2 = module_0.Box(bool_1)
        var_2 = box_2.map(str_0)
    except BaseException:
        pass