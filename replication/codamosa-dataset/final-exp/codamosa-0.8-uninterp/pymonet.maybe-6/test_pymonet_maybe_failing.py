# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    try:
        callable_0 = None
        list_0 = []
        bool_0 = False
        maybe_0 = module_0.Maybe(list_0, bool_0)
        var_0 = maybe_0.map(callable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Sum[value={}]'
        tuple_0 = (str_0,)
        bool_0 = True
        maybe_0 = module_0.Maybe(tuple_0, bool_0)
        var_0 = maybe_0.to_box()
        bool_1 = False
        maybe_1 = module_0.Maybe(tuple_0, bool_1)
        object_0 = module_1.object()
        var_1 = maybe_1.bind(object_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        var_0 = None
        maybe_0 = module_0.Maybe(var_0, bool_0)
        callable_0 = None
        var_1 = maybe_0.filter(callable_0)
        callable_1 = None
        var_2 = maybe_0.bind(callable_1)
        bool_1 = False
        maybe_1 = module_0.Maybe(var_0, bool_1)
        var_3 = maybe_1.filter(callable_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = None
        int_0 = 1056
        bool_0 = False
        maybe_0 = module_0.Maybe(int_0, bool_0)
        var_0 = maybe_0.ap(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        var_0 = None
        maybe_0 = module_0.Maybe(var_0, bool_0)
        callable_0 = None
        var_1 = maybe_0.filter(callable_0)
        bool_1 = False
        maybe_1 = module_0.Maybe(var_0, bool_1)
        var_2 = maybe_1.filter(callable_0)
    except BaseException:
        pass