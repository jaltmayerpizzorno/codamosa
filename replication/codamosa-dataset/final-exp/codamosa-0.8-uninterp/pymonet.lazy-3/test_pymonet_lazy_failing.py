# Automatically generated by Pynguin.
import pymonet.lazy as module_0

def test_case_0():
    try:
        dict_0 = {}
        lazy_0 = module_0.Lazy(dict_0)
        var_0 = lazy_0.to_maybe()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'K'
        lazy_0 = module_0.Lazy(str_0)
        var_0 = lazy_0.to_box()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 5
        lazy_0 = module_0.Lazy(int_0)
        var_0 = lazy_0.to_either()
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -726
        lazy_0 = module_0.Lazy(int_0)
        var_0 = lazy_0.to_validation()
    except BaseException:
        pass