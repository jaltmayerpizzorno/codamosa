# Automatically generated by Pynguin.
import pymonet.either as module_0
import builtins as module_1

def test_case_0():
    try:
        str_0 = 'n~_,jdv8-}d*'
        str_1 = 'Z@vCH"Asp\x0bqi\x0c'
        int_0 = True
        list_0 = [int_0, int_0, int_0, int_0]
        either_0 = module_0.Either(list_0)
        var_0 = either_0.case(str_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 2
        right_0 = module_0.Right(int_0)
        var_0 = lambda v: v * int_0
        var_1 = lambda v: v / int_0
        var_2 = right_0.case(var_0, var_1)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = False
        right_0 = module_0.Right(int_0)
        bytes_0 = b'\xd2\x17\x15\x9dr\xa4D'
        list_0 = [bytes_0]
        right_1 = module_0.Right(list_0)
        var_0 = right_1.map(right_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        dict_0 = None
        object_0 = module_1.object()
        dict_1 = {dict_0: dict_0, object_0: dict_0, object_0: dict_0}
        right_0 = module_0.Right(dict_1)
        var_0 = right_0.bind(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xa6v\x8b\x12\xee3\x8c\xbc\x02\x16\xeeyw'
        either_0 = module_0.Either(bytes_0)
        str_0 = '@trjq{4)f=v9a'
        either_1 = module_0.Either(str_0)
        var_0 = either_1.to_box()
        var_1 = None
        list_0 = [var_0]
        right_0 = module_0.Right(list_0)
        var_2 = right_0.to_validation()
        int_0 = 3509
        object_0 = None
        bool_0 = either_1.__eq__(object_0)
        var_3 = either_0.case(int_0, var_1)
    except BaseException:
        pass