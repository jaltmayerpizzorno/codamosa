# Automatically generated by Pynguin.
import pymonet.either as module_0
import builtins as module_1

def test_case_0():
    try:
        bytes_0 = b'Q\xa6\xbd\x1f\xd9\xa3\xf2Sn\xacg\x90l\xa0\xb5W\xbco\xca'
        either_0 = module_0.Either(bytes_0)
        bool_0 = True
        var_0 = either_0.case(bool_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        int_0 = False
        either_0 = module_0.Either(int_0)
        var_0 = either_0.ap(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '}1\\L^sg$DelK]'
        str_1 = 'kv'
        int_0 = 3413
        dict_0 = {str_0: str_0, str_0: str_0, str_1: int_0, str_0: str_1}
        bool_0 = False
        list_0 = [bool_0]
        tuple_0 = (bool_0, list_0)
        left_0 = module_0.Left(tuple_0)
        var_0 = left_0.map(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'aY1\x0b \nD@f2SR4\\)'
        bool_0 = False
        list_0 = [str_0, str_0, str_0, str_0]
        left_0 = module_0.Left(list_0)
        var_0 = left_0.bind(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        object_0 = module_1.object()
        either_0 = module_0.Either(object_0)
        bool_0 = either_0.__eq__(object_0)
        var_0 = either_0.is_right()
        float_0 = -103.9
        str_0 = 'L\t-Q!`k8,>2H&q-;7u"Q'
        right_0 = module_0.Right(str_0)
        object_1 = module_1.object()
        right_1 = module_0.Right(object_1)
        left_0 = module_0.Left(float_0)
        var_1 = left_0.to_validation()
        bool_1 = left_0.is_left()
        var_2 = right_1.to_maybe()
        left_1 = module_0.Left(float_0)
        var_3 = left_1.to_maybe()
        var_4 = left_1.to_maybe()
        float_1 = 448.97
        var_5 = right_0.map(float_1)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'?\xbe\x92\xea\\\xa7'
        either_0 = module_0.Either(bytes_0)
        var_0 = either_0.to_try()
        var_1 = either_0.to_lazy()
        float_0 = 161.934
        object_0 = module_1.object()
        bool_0 = either_0.__eq__(object_0)
        str_0 = '2MJ_8,'
        right_0 = module_0.Right(str_0)
        var_2 = right_0.map(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        callable_0 = None
        str_0 = "?6]5<t!'b[\t<{ ,X"
        dict_0 = {str_0: str_0, str_0: str_0}
        right_0 = module_0.Right(dict_0)
        var_0 = right_0.bind(callable_0)
    except BaseException:
        pass

def test_case_7():
    try:
        var_0 = None
        float_0 = -385.81691
        either_0 = module_0.Either(float_0)
        right_0 = module_0.Right(either_0)
        bool_0 = right_0.is_left()
        dict_0 = {var_0: var_0}
        either_1 = module_0.Either(dict_0)
        bool_1 = False
        either_2 = module_0.Either(bool_1)
        var_1 = either_2.case(dict_0, either_1)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        left_0 = module_0.Left(dict_0)
        str_0 = '0D^>(?lK+'
        bool_0 = left_0.is_right()
        var_0 = left_0.to_maybe()
        either_0 = module_0.Either(str_0)
        var_1 = either_0.to_box()
        var_2 = either_0.to_box()
        var_3 = either_0.to_try()
        var_4 = either_0.to_box()
        list_0 = None
        float_0 = -1034.1799585993076
        right_0 = module_0.Right(float_0)
        var_5 = left_0.to_maybe()
        var_6 = right_0.to_validation()
        int_0 = None
        var_7 = right_0.case(int_0, list_0)
    except BaseException:
        pass