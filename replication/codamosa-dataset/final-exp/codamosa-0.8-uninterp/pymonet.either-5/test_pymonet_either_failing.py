# Automatically generated by Pynguin.
import builtins as module_0
import pymonet.either as module_1

def test_case_0():
    try:
        str_0 = 'U'
        dict_0 = {}
        object_0 = module_0.object(**dict_0)
        int_0 = -1115
        either_0 = module_1.Either(int_0)
        bool_0 = either_0.__eq__(object_0)
        var_0 = None
        either_1 = module_1.Either(var_0)
        var_1 = either_1.ap(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        callable_0 = None
        str_0 = 'S'
        list_0 = [str_0, str_0, str_0]
        either_0 = module_1.Either(list_0)
        var_0 = either_0.case(callable_0, callable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -999.6749
        right_0 = module_1.Right(float_0)
        either_0 = module_1.Either(right_0)
        str_0 = 'OM\x0b/fxf.1+CgN@c\n=Gd'
        dict_0 = {str_0: str_0}
        var_0 = either_0.ap(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        object_0 = module_0.object()
        either_0 = module_1.Either(object_0)
        var_0 = either_0.to_box()
        bool_0 = True
        list_0 = [var_0, var_0, either_0, object_0]
        right_0 = module_1.Right(list_0)
        var_1 = right_0.map(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '7LsKF?'
        either_0 = module_1.Either(str_0)
        var_0 = either_0.is_right()
        var_1 = either_0.to_try()
        var_2 = either_0.to_lazy()
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = None
        right_0 = module_1.Right(var_0)
        var_1 = right_0.to_validation()
        either_0 = module_1.Either(var_0)
        left_0 = module_1.Left(var_0)
        left_1 = module_1.Left(var_0)
        var_2 = left_1.ap(left_0)
        callable_0 = None
        var_3 = right_0.to_maybe()
        var_4 = either_0.to_lazy()
        var_5 = either_0.case(callable_0, callable_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        float_0 = 3130.194
        left_0 = module_1.Left(float_0)
        object_0 = module_0.object(**dict_0)
        str_0 = '+iR^C9Bvln?**W$--['
        var_0 = None
        var_1 = left_0.map(dict_0)
        tuple_0 = (str_0, var_0)
        right_0 = module_1.Right(float_0)
        var_2 = right_0.to_validation()
        either_0 = module_1.Either(tuple_0)
        right_1 = module_1.Right(either_0)
        var_3 = right_1.map(object_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = "qn!F2=mk/'i#Exc+,/X`"
        str_1 = 'h>YO]=\\#\tq?Bp'
        right_0 = module_1.Right(str_1)
        dict_0 = {str_0: str_0}
        dict_1 = {str_0: str_1, str_0: right_0, str_0: str_0}
        left_0 = module_1.Left(dict_1)
        var_0 = left_0.bind(dict_0)
        str_2 = '7\x0cH7;Ky'
        left_1 = module_1.Left(str_2)
        var_1 = left_1.ap(var_0)
        var_2 = right_0.bind(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 4
        right_0 = module_1.Right(int_0)
        var_0 = lambda _: int_0
        var_1 = lambda x: x % int_0
        var_2 = right_0.case(var_0, var_1)
    except BaseException:
        pass