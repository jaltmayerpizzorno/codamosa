# Automatically generated by Pynguin.
import builtins as module_0
import pymonet.immutable_list as module_1

def test_case_0():
    try:
        bool_0 = False
        object_0 = module_0.object()
        immutable_list_0 = module_1.ImmutableList()
        var_0 = None
        bool_1 = False
        immutable_list_1 = module_1.ImmutableList(object_0, bool_1)
        var_1 = immutable_list_1.append(var_0)
        tuple_0 = (var_1, object_0)
        immutable_list_2 = module_1.ImmutableList(tuple_0, bool_1)
        var_2 = immutable_list_2.unshift(immutable_list_0)
        immutable_list_3 = module_1.ImmutableList()
        bool_2 = immutable_list_3.__eq__(object_0)
        immutable_list_4 = module_1.ImmutableList(bool_0)
        optional_0 = immutable_list_4.find(immutable_list_4)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = None
        dict_0 = {}
        object_0 = module_0.object(**dict_0)
        immutable_list_0 = module_1.ImmutableList(var_0)
        var_1 = immutable_list_0.__add__(var_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        bool_1 = False
        immutable_list_0 = module_1.ImmutableList(bool_0, bool_1)
        var_0 = immutable_list_0.__len__()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        bool_0 = True
        immutable_list_0 = module_1.ImmutableList(bool_0, str_0)
        var_0 = immutable_list_0.to_list()
    except BaseException:
        pass

def test_case_4():
    try:
        immutable_list_0 = module_1.ImmutableList()
        var_0 = None
        var_1 = immutable_list_0.append(var_0)
        object_0 = module_0.object()
        bool_0 = immutable_list_0.__eq__(object_0)
        immutable_list_1 = module_1.ImmutableList(bool_0)
        float_0 = -438.888
        optional_0 = immutable_list_1.find(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        str_0 = '"\tje,'
        set_0 = {str_0}
        dict_0 = {str_0: set_0, str_0: set_0, str_0: str_0}
        immutable_list_0 = module_1.ImmutableList(set_0, dict_0)
        var_0 = immutable_list_0.map(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -1082
        bool_0 = False
        immutable_list_0 = module_1.ImmutableList(bool_0)
        var_0 = immutable_list_0.map(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        immutable_list_0 = module_1.ImmutableList()
        var_0 = immutable_list_0.filter(immutable_list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        immutable_list_0 = module_1.ImmutableList(bool_0)
        optional_0 = immutable_list_0.find(bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\n        If Maybe is empty or filterer returns False return default_value, in other case\n        return new instance of Maybe with the same value.\n\n        :param filterer:\n        :type filterer: Function(A) -> Boolean\n        :returns: copy of self when filterer returns True, in other case empty Maybe\n        :rtype: Maybe[A] | Maybe[None]\n        '
        str_1 = '/'
        dict_0 = {str_0: str_0, str_1: str_1}
        bool_0 = False
        immutable_list_0 = module_1.ImmutableList()
        var_0 = immutable_list_0.__len__()
        immutable_list_1 = module_1.ImmutableList(dict_0, bool_0)
        callable_0 = None
        var_1 = None
        var_2 = immutable_list_0.reduce(callable_0, var_1)
        var_3 = immutable_list_1.reduce(callable_0, var_2)
    except BaseException:
        pass

def test_case_10():
    try:
        object_0 = module_0.object()
        bool_0 = False
        list_0 = [bool_0]
        bool_1 = False
        immutable_list_0 = module_1.ImmutableList(bool_0, list_0, bool_1)
        bool_2 = immutable_list_0.__eq__(object_0)
        var_0 = None
        immutable_list_1 = module_1.ImmutableList()
        optional_0 = immutable_list_1.find(var_0)
        immutable_list_2 = module_1.ImmutableList()
        callable_0 = None
        var_1 = immutable_list_0.filter(callable_0)
    except BaseException:
        pass

def test_case_11():
    try:
        object_0 = module_0.object()
        bool_0 = False
        list_0 = [bool_0]
        immutable_list_0 = module_1.ImmutableList(bool_0, list_0, bool_0)
        bool_1 = immutable_list_0.__eq__(object_0)
        callable_0 = None
        optional_0 = immutable_list_0.find(callable_0)
    except BaseException:
        pass

def test_case_12():
    try:
        callable_0 = None
        var_0 = None
        bool_0 = False
        immutable_list_0 = module_1.ImmutableList(bool_0)
        var_1 = immutable_list_0.reduce(callable_0, var_0)
    except BaseException:
        pass