# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    try:
        dict_0 = {}
        bool_0 = False
        maybe_0 = module_0.Maybe(dict_0, bool_0)
        str_0 = ''
        callable_0 = None
        bool_1 = True
        maybe_1 = module_0.Maybe(maybe_0, bool_1)
        var_0 = maybe_1.filter(callable_0)
        var_1 = maybe_0.filter(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        maybe_0 = module_0.Maybe(bool_0, bool_0)
        var_0 = maybe_0.map(maybe_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '>&Pl'
        str_1 = '\n        Transform Lazy into Either (Right) with constructor_fn result.\n\n        :returns: Right monad with constructor_fn result\n        :rtype: Right[A]\n        '
        str_2 = 'Sum'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1, str_2: str_0}
        str_3 = '$w0\n\nJ@@M}0[fS>w$UW'
        bool_0 = False
        maybe_0 = module_0.Maybe(str_3, bool_0)
        var_0 = maybe_0.bind(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        set_0 = set()
        object_0 = module_1.object()
        list_0 = [set_0, object_0]
        bool_0 = False
        maybe_0 = module_0.Maybe(list_0, bool_0)
        bool_1 = False
        object_1 = module_1.object()
        maybe_1 = module_0.Maybe(object_1, bool_1)
        var_0 = maybe_1.to_lazy()
        bool_2 = maybe_1.__eq__(object_1)
        list_1 = [var_0]
        maybe_2 = module_0.Maybe(list_1, bool_1)
        var_1 = maybe_2.ap(set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\rwlTo0+XT?~'
        set_0 = {str_0}
        dict_0 = {}
        bool_0 = False
        maybe_0 = module_0.Maybe(dict_0, bool_0)
        var_0 = maybe_0.filter(set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        maybe_0 = module_0.Maybe(bool_0, bool_0)
        callable_0 = None
        list_0 = []
        var_0 = maybe_0.get_or_else(list_0)
        var_1 = maybe_0.filter(callable_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        dict_0 = {}
        maybe_0 = module_0.Maybe(dict_0, bool_0)
        var_0 = maybe_0.to_try()
        bool_1 = False
        var_1 = maybe_0.to_box()
        maybe_1 = module_0.Maybe(bool_0, bool_1)
        var_2 = maybe_1.to_box()
        var_3 = maybe_1.to_lazy()
        var_4 = maybe_1.to_lazy()
        str_0 = ',3B)IeYe'
        var_5 = maybe_0.to_either()
        list_0 = [str_0, str_0, str_0, str_0]
        bool_2 = False
        maybe_2 = module_0.Maybe(list_0, bool_2)
        callable_0 = None
        var_6 = maybe_0.bind(callable_0)
        var_7 = maybe_2.to_lazy()
        var_8 = maybe_1.to_validation()
        var_9 = maybe_1.to_validation()
        bytes_0 = b"\x15>']\x14T\xc1f\x82\xdd"
        var_10 = maybe_2.map(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        int_0 = 1602
        maybe_0 = module_0.Maybe(int_0, bool_0)
        bool_1 = False
        maybe_1 = module_0.Maybe(maybe_0, bool_1)
        var_0 = maybe_1.to_box()
        bytes_0 = None
        int_1 = 2091
        bool_2 = False
        maybe_2 = module_0.Maybe(int_1, bool_2)
        var_1 = maybe_2.to_try()
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        bool_3 = False
        maybe_3 = module_0.Maybe(dict_0, bool_3)
        var_2 = maybe_3.bind(bytes_0)
    except BaseException:
        pass