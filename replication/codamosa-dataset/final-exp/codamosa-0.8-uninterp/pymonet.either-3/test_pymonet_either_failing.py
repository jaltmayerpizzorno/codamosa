# Automatically generated by Pynguin.
import builtins as module_0
import pymonet.either as module_1

def test_case_0():
    try:
        callable_0 = None
        object_0 = module_0.object()
        either_0 = module_1.Either(object_0)
        var_0 = either_0.case(callable_0, callable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        int_0 = 338
        either_0 = module_1.Either(int_0)
        var_0 = either_0.to_lazy()
        right_0 = module_1.Right(bool_0)
        str_0 = '#-wM;7ZFXGt|a=?\r `E'
        var_1 = either_0.ap(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = None
        left_0 = module_1.Left(var_0)
        list_0 = [left_0, var_0, left_0, left_0]
        right_0 = module_1.Right(list_0)
        bool_0 = right_0.is_left()
        int_0 = -2824
        float_0 = 391.43
        var_1 = left_0.bind(bool_0)
        set_0 = {float_0, float_0}
        either_0 = module_1.Either(set_0)
        var_2 = either_0.to_try()
        var_3 = either_0.case(int_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        left_0 = module_1.Left(bool_0)
        bool_1 = left_0.is_left()
        float_0 = -89.742347
        left_1 = module_1.Left(float_0)
        str_0 = '\n    Perform left-to-right function composition.\n\n    :param value: argument of first applied function\n    :type value: Any\n    :param functions: list of functions to applied from left-to-right\n    :type functions: List[Function]\n    :returns: result of all functions\n    :rtype: Any\n    '
        right_0 = module_1.Right(str_0)
        var_0 = right_0.to_validation()
        str_1 = 's[yT;T'
        var_1 = left_1.to_maybe()
        either_0 = module_1.Either(str_1)
        var_2 = either_0.to_try()
        var_3 = left_1.to_validation()
        var_4 = either_0.is_right()
        var_5 = None
        list_0 = []
        object_0 = module_0.object(*list_0)
        either_1 = module_1.Either(var_5)
        bool_2 = either_1.__eq__(object_0)
        var_6 = either_0.is_right()
        callable_0 = None
        var_7 = either_0.to_lazy()
        var_8 = either_1.case(callable_0, callable_0)
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = None
        right_0 = module_1.Right(var_0)
        either_0 = module_1.Either(var_0)
        var_1 = either_0.is_right()
        left_0 = module_1.Left(var_0)
        var_2 = left_0.to_validation()
        var_3 = right_0.to_maybe()
        either_1 = module_1.Either(var_0)
        object_0 = module_0.object()
        bool_0 = either_1.__eq__(object_0)
        callable_0 = None
        var_4 = either_0.case(callable_0, callable_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xadx\xb7Mn&\xf0>=T)\x02'
        bool_0 = True
        right_0 = module_1.Right(bool_0)
        var_0 = right_0.map(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\x00\x05\x7f\x83~y\xe2&T\xbb\xd1'
        right_0 = module_1.Right(bytes_0)
        bool_0 = right_0.is_right()
        either_0 = module_1.Either(right_0)
        callable_0 = None
        var_0 = right_0.bind(callable_0)
    except BaseException:
        pass

def test_case_7():
    try:
        var_0 = None
        left_0 = module_1.Left(var_0)
        list_0 = [left_0, var_0, left_0, left_0]
        right_0 = module_1.Right(list_0)
        bool_0 = right_0.is_left()
        int_0 = -2824
        float_0 = 391.43
        set_0 = None
        var_1 = left_0.map(set_0)
        set_1 = {float_0, float_0}
        either_0 = module_1.Either(set_1)
        var_2 = either_0.to_try()
        var_3 = either_0.case(int_0, int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        object_0 = module_0.object(**dict_0)
        either_0 = module_1.Either(object_0)
        var_0 = either_0.is_right()
        bool_0 = True
        left_0 = module_1.Left(bool_0)
        bool_1 = left_0.is_left()
        float_0 = -89.742347
        left_1 = module_1.Left(float_0)
        str_0 = '\n    Perform left-to-right function composition.\n\n    :param value: argument of first applied function\n    :type value: Any\n    :param functions: list of functions to applied from left-to-right\n    :type functions: List[Function]\n    :returns: result of all functions\n    :rtype: Any\n    '
        var_1 = either_0.to_box()
        right_0 = module_1.Right(str_0)
        var_2 = right_0.to_validation()
        str_1 = 's[yT;T'
        var_3 = left_1.to_maybe()
        either_1 = module_1.Either(str_1)
        var_4 = either_1.to_try()
        var_5 = left_1.to_validation()
        var_6 = either_1.is_right()
        var_7 = None
        list_0 = []
        object_1 = module_0.object(*list_0)
        either_2 = module_1.Either(var_7)
        bool_2 = either_2.__eq__(object_1)
        var_8 = either_1.is_right()
        callable_0 = None
        var_9 = either_1.to_lazy()
        var_10 = either_2.case(callable_0, callable_0)
    except BaseException:
        pass