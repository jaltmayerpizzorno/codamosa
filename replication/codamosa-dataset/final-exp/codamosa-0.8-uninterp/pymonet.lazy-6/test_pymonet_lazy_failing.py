# Automatically generated by Pynguin.
import pymonet.lazy as module_0
import builtins as module_1

def test_case_0():
    try:
        bytes_0 = b'g,\xf1i\xa1]\xd8\xa7AtqH\xa4'
        lazy_0 = module_0.Lazy(bytes_0)
        var_0 = lazy_0.to_maybe()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'g,\xf1v\xa1]\xf1\x84AtqH\xa4'
        list_0 = []
        dict_0 = {}
        lazy_0 = module_0.Lazy(dict_0)
        var_0 = lazy_0.map(list_0)
        lazy_1 = module_0.Lazy(bytes_0)
        var_1 = lazy_1.to_maybe()
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = None
        str_0 = ",LXmQN.uA{'pp"
        lazy_0 = module_0.Lazy(str_0)
        var_0 = lazy_0.ap(list_0)
        list_1 = None
        bool_0 = True
        lazy_1 = module_0.Lazy(bool_0)
        var_1 = lazy_1.to_either(*list_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\n        If Maybe is empty return new empty Maybe, in other case\n        takes mapper function and returns result of mapper.\n\n        :param mapper: function to call with Maybe.value\n        :type mapper: Function(A) -> Maybe[B]\n        :returns: Maybe[B | None]\n        '
        tuple_0 = ()
        tuple_1 = ()
        dict_0 = {str_0: tuple_1}
        lazy_0 = module_0.Lazy(dict_0)
        var_0 = lazy_0.bind(tuple_0)
        callable_0 = None
        lazy_1 = module_0.Lazy(callable_0)
        lazy_2 = module_0.Lazy(str_0)
        var_1 = lazy_2.to_validation()
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 631.39
        lazy_0 = module_0.Lazy(float_0)
        var_0 = lazy_0.to_box()
    except BaseException:
        pass

def test_case_5():
    try:
        object_0 = module_1.object()
        lazy_0 = module_0.Lazy(object_0)
        lazy_1 = module_0.Lazy(lazy_0)
        var_0 = lazy_1.to_either()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'Validation.success[{}]'
        lazy_0 = module_0.Lazy(str_0)
        var_0 = lazy_0.to_try()
        var_1 = lazy_0.to_validation()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'Validation.success[{}]'
        lazy_0 = module_0.Lazy(str_0)
        var_0 = lazy_0.to_validation()
    except BaseException:
        pass