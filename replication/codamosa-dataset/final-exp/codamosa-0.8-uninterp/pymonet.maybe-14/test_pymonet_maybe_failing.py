# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    try:
        bool_0 = False
        bool_1 = True
        maybe_0 = module_0.Maybe(bool_1, bool_1)
        var_0 = maybe_0.filter(bool_0)
        str_0 = '\t:?9'
        str_1 = 'Bs-'
        dict_0 = {str_0: str_0, str_1: bool_1}
        object_0 = module_1.object(**dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        bool_1 = False
        maybe_0 = module_0.Maybe(bool_0, bool_1)
        var_0 = maybe_0.to_validation()
        maybe_1 = None
        var_1 = maybe_0.map(maybe_1)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = None
        bool_0 = True
        maybe_0 = module_0.Maybe(var_0, bool_0)
        complex_0 = None
        int_0 = -1083
        bool_1 = False
        var_1 = maybe_0.to_validation()
        maybe_1 = module_0.Maybe(int_0, bool_1)
        var_2 = maybe_1.bind(complex_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        bool_0 = False
        maybe_0 = module_0.Maybe(dict_0, bool_0)
        var_0 = maybe_0.to_lazy()
        var_1 = maybe_0.to_either()
        object_0 = module_1.object()
        int_0 = -969
        var_2 = maybe_0.ap(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        object_0 = module_1.object()
        str_0 = 'Y5733BJ]pSz'
        bool_0 = True
        maybe_0 = module_0.Maybe(str_0, bool_0)
        bool_1 = maybe_0.__eq__(object_0)
        set_0 = set()
        var_0 = maybe_0.ap(set_0)
        var_1 = None
        var_2 = maybe_0.ap(var_1)
        maybe_1 = module_0.Maybe(var_1, bool_0)
        int_0 = -1474
        var_3 = maybe_0.filter(int_0)
        dict_0 = {}
        var_4 = maybe_1.get_or_else(dict_0)
        bool_2 = False
        maybe_2 = module_0.Maybe(var_1, bool_2)
        var_5 = maybe_2.to_lazy()
        var_6 = maybe_0.to_box()
        var_7 = maybe_1.to_try()
        var_8 = maybe_0.to_validation()
        bool_3 = False
        maybe_3 = module_0.Maybe(var_1, bool_3)
        var_9 = maybe_0.to_try()
        callable_0 = None
        var_10 = maybe_3.filter(callable_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xff\xb7f\x92]\x9b'
        bool_0 = False
        callable_0 = None
        list_0 = [callable_0, bytes_0, bytes_0]
        maybe_0 = module_0.Maybe(bool_0, bool_0)
        var_0 = maybe_0.get_or_else(list_0)
        str_0 = '\n        Transform Box into not empty Maybe.\n\n        :returns: non empty Maybe monad with previous value\n        :rtype: Maybe[A]\n        '
        maybe_1 = module_0.Maybe(str_0, bool_0)
        var_1 = maybe_1.filter(callable_0)
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = None
        str_0 = '\n        Applies the function inside the Box[A] structure to another applicative type.\n\n        :param applicative: applicative contains function\n        :type applicative: Box[B]\n        :returns: new Box with result of contains function\n        :rtype: Box[A(B)]\n        '
        str_1 = 'v;@.\n4q'
        dict_0 = {str_0: var_0, str_1: var_0}
        bool_0 = True
        maybe_0 = module_0.Maybe(dict_0, bool_0)
        var_1 = maybe_0.to_lazy()
        list_0 = []
        bool_1 = False
        bool_2 = True
        str_2 = ':\x0bG3'
        maybe_1 = module_0.Maybe(str_2, bool_1)
        var_2 = maybe_1.to_lazy()
        bool_3 = False
        maybe_2 = module_0.Maybe(bool_2, bool_3)
        var_3 = maybe_2.to_try()
        maybe_3 = module_0.Maybe(list_0, bool_1)
        var_4 = maybe_3.filter(var_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        bool_1 = False
        maybe_0 = module_0.Maybe(bool_0, bool_1)
        var_0 = lambda x: x
        var_1 = maybe_0.filter(var_0)
        var_2 = var_1.value
        var_3 = None
        maybe_1 = module_0.Maybe(var_3, bool_0)
        var_4 = lambda x: x
        var_5 = maybe_1.filter(var_4)
        var_6 = var_5.is_nothing
        int_0 = 2
        maybe_2 = module_0.Maybe(int_0, bool_1)
        var_7 = lambda x: x % int_0 == bool_1
        var_8 = maybe_2.filter(var_7)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        bool_1 = False
        maybe_0 = module_0.Maybe(bool_0, bool_1)
        var_0 = lambda x: x
        var_1 = maybe_0.filter(var_0)
        var_2 = var_1.value
    except BaseException:
        pass