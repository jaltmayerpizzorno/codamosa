# Automatically generated by Pynguin.
import pymonet.lazy as module_0
import builtins as module_1

def test_case_0():
    try:
        set_0 = set()
        lazy_0 = module_0.Lazy(set_0)
        var_0 = lazy_0.to_either()
    except BaseException:
        pass

def test_case_1():
    try:
        object_0 = module_1.object()
        str_0 = 'z!23e*.r"9'
        lazy_0 = module_0.Lazy(str_0)
        var_0 = lazy_0.ap(object_0)
        list_0 = []
        float_0 = -1331.65
        list_1 = [float_0, list_0, list_0, float_0]
        bool_0 = True
        lazy_1 = module_0.Lazy(bool_0)
        var_1 = lazy_1.ap(list_1)
        bytes_0 = b'\x0e\xdc/\xcd7\xd2`y\xc26\x92'
        lazy_2 = module_0.Lazy(bytes_0)
        lazy_3 = module_0.Lazy(lazy_2)
        var_2 = lazy_3.to_maybe(*list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = set()
        bytes_0 = b'k\x8f\xa0;\xe4\xfe\x8eZ\x10E;\xe1P!L\xa2q*\x89'
        lazy_0 = module_0.Lazy(bytes_0)
        var_0 = lazy_0.bind(set_0)
        lazy_1 = module_0.Lazy(var_0)
        var_1 = lazy_1.to_maybe()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Z3nL)6u'
        lazy_0 = module_0.Lazy(str_0)
        var_0 = lazy_0.to_box()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'x1.lapPq0'
        lazy_0 = module_0.Lazy(str_0)
        var_0 = lazy_0.to_maybe()
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = []
        str_0 = '=h):}!'
        lazy_0 = module_0.Lazy(str_0)
        list_1 = [list_0]
        var_0 = lazy_0.to_try(*list_1)
        var_1 = lazy_0.map(list_0)
        list_2 = [var_1, str_0, list_0, var_1]
        lazy_1 = module_0.Lazy(list_2)
        var_2 = lazy_1.get()
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\xe3\x0f\xcd\xa02\xc2@\x91TA\xe0U\xe7'
        lazy_0 = module_0.Lazy(bytes_0)
        var_0 = lazy_0.to_validation()
    except BaseException:
        pass