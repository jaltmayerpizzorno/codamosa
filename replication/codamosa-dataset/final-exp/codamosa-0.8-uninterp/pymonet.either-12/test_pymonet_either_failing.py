# Automatically generated by Pynguin.
import pymonet.either as module_0
import builtins as module_1

def test_case_0():
    try:
        callable_0 = None
        bytes_0 = b'\x1e\x9a\x96'
        either_0 = module_0.Either(bytes_0)
        var_0 = either_0.case(callable_0, callable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        str_1 = "\\me'TLb"
        either_0 = module_0.Either(str_1)
        var_0 = either_0.ap(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = None
        left_0 = module_0.Left(var_0)
        str_0 = '+\\V8\x0b2ep:n`l[5Z'
        right_0 = module_0.Right(var_0)
        var_1 = right_0.to_validation()
        int_0 = False
        right_1 = module_0.Right(var_0)
        bool_0 = right_1.is_left()
        var_2 = left_0.ap(int_0)
        dict_0 = {str_0: left_0}
        object_0 = module_1.object(**dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -3015
        left_0 = module_0.Left(int_0)
        object_0 = module_1.object()
        str_0 = ''
        int_1 = 825
        right_0 = module_0.Right(int_1)
        var_0 = right_0.map(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        callable_0 = None
        bytes_0 = b'\xf1-\xdb\x141\xa2S\x01\xf8\xa5\r\x83W\x02n\x12'
        float_0 = -2440.4
        dict_0 = {bytes_0: bytes_0, float_0: float_0, float_0: bytes_0}
        right_0 = module_0.Right(dict_0)
        var_0 = right_0.bind(callable_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 1
        right_0 = module_0.Right(int_0)
        str_0 = 'error type: %s'
        var_0 = lambda err: str_0 % type(err)
        str_1 = 'success'
        var_1 = lambda suc: str_1
        var_2 = lambda err: str_0 % type(err)
        var_3 = lambda suc: str_1
        var_4 = right_0.case(var_2, var_3)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '-z\tY;@nvR}.u'
        either_0 = module_0.Either(str_0)
        var_0 = either_0.is_right()
        callable_0 = None
        var_1 = None
        left_0 = module_0.Left(var_1)
        var_2 = left_0.bind(str_0)
        right_0 = module_0.Right(var_1)
        var_3 = right_0.to_maybe()
        left_1 = module_0.Left(var_1)
        right_1 = module_0.Right(var_1)
        bool_0 = right_1.is_right()
        bool_1 = False
        either_1 = module_0.Either(bool_1)
        var_4 = either_1.case(callable_0, callable_0)
    except BaseException:
        pass