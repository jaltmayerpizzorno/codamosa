# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    try:
        set_0 = set()
        float_0 = -1171.5
        tuple_0 = (set_0, float_0)
        tuple_1 = ()
        bool_0 = False
        maybe_0 = module_0.Maybe(tuple_1, bool_0)
        var_0 = maybe_0.map(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = None
        dict_0 = {var_0: var_0, var_0: var_0}
        bool_0 = False
        maybe_0 = module_0.Maybe(dict_0, bool_0)
        bool_1 = False
        var_1 = maybe_0.to_try()
        maybe_1 = module_0.Maybe(maybe_0, bool_1)
        callable_0 = None
        var_2 = maybe_1.bind(callable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b's\xb0s\xd0T7n\xd0/'
        bool_0 = True
        maybe_0 = module_0.Maybe(bytes_0, bool_0)
        var_0 = maybe_0.to_validation()
        bool_1 = True
        list_0 = [bool_1, bool_1, bool_1]
        var_1 = maybe_0.to_box()
        float_0 = -1726.67916
        bool_2 = False
        maybe_1 = module_0.Maybe(float_0, bool_2)
        var_2 = maybe_1.ap(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        object_0 = module_1.object()
        list_0 = [object_0]
        bool_0 = False
        maybe_0 = module_0.Maybe(list_0, bool_0)
        bool_1 = maybe_0.__eq__(object_0)
        tuple_0 = None
        var_0 = maybe_0.get_or_else(tuple_0)
        bytes_0 = b''
        bool_2 = None
        maybe_1 = module_0.Maybe(bytes_0, bool_2)
        var_1 = maybe_0.filter(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '~\tl~4CN>h:U1I!;*$`>'
        bool_0 = True
        maybe_0 = module_0.Maybe(str_0, bool_0)
        var_0 = maybe_0.to_either()
        var_1 = maybe_0.to_try()
    except BaseException:
        pass

def test_case_5():
    try:
        object_0 = module_1.object()
        bytes_0 = b'?a\x0f\xb3\x1e\x93\xfc$\x86"'
        dict_0 = {object_0: bytes_0, bytes_0: object_0, bytes_0: bytes_0, object_0: bytes_0}
        bool_0 = False
        maybe_0 = module_0.Maybe(dict_0, bool_0)
        var_0 = maybe_0.to_box()
        bool_1 = False
        maybe_1 = module_0.Maybe(maybe_0, bool_1)
        var_1 = maybe_1.to_validation()
        str_0 = 'Y33_1#!DF*'
        float_0 = -5326.095
        set_0 = {str_0, object_0, object_0}
        bool_2 = False
        maybe_2 = module_0.Maybe(set_0, bool_2)
        var_2 = maybe_2.filter(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        callable_0 = None
        str_0 = ''
        maybe_0 = module_0.Maybe(str_0, bool_0)
        var_0 = maybe_0.filter(callable_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -5
        bool_0 = True
        maybe_0 = module_0.Maybe(int_0, bool_0)
        maybe_1 = module_0.Maybe(int_0, bool_0)
        maybe_2 = module_0.Maybe(int_0, bool_0)
        var_0 = maybe_1 == bool_0
        maybe_3 = module_0.Maybe(int_0, bool_0)
        var_1 = maybe_2.filter(bool_0)
        object_0 = module_1.object()
        bool_1 = False
        maybe_4 = module_0.Maybe(object_0, bool_1)
        var_2 = maybe_1 != maybe_3
        bool_2 = True
        maybe_5 = module_0.Maybe(int_0, bool_2)
        var_3 = maybe_0 != maybe_5
        maybe_6 = module_0.Maybe(bool_2, bool_0)
        var_4 = maybe_0 == maybe_6
        object_1 = module_1.object()
        var_5 = maybe_6.to_validation()
        var_6 = maybe_6.get_or_else(object_1)
        var_7 = None
        bool_3 = False
        maybe_7 = module_0.Maybe(var_7, bool_3)
        list_0 = []
        var_8 = maybe_7.filter(list_0)
    except BaseException:
        pass