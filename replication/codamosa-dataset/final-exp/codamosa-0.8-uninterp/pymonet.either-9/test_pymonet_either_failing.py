# Automatically generated by Pynguin.
import builtins as module_0
import pymonet.either as module_1

def test_case_0():
    try:
        object_0 = module_0.object()
        int_0 = True
        either_0 = module_1.Either(int_0)
        callable_0 = None
        var_0 = either_0.case(either_0, callable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '?a`/0Lxfu&NGa'
        str_1 = '\x0cW\\G!'
        either_0 = module_1.Either(str_1)
        var_0 = either_0.ap(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = False
        float_0 = 1719.3928
        tuple_0 = (float_0,)
        int_1 = 1382
        left_0 = module_1.Left(int_1)
        bool_0 = left_0.is_left()
        var_0 = left_0.map(tuple_0)
        bool_1 = left_0.is_left()
        str_0 = 'biTH;'
        str_1 = '\'3%[*\x0ca4"Q_W'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0, str_1: str_1}
        right_0 = module_1.Right(dict_0)
        var_1 = right_0.bind(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        dict_1 = {}
        left_0 = module_1.Left(dict_1)
        bool_0 = left_0.is_right()
        right_0 = module_1.Right(dict_0)
        var_0 = right_0.to_validation()
        var_1 = right_0.to_maybe()
        float_0 = 3141.879
        var_2 = left_0.ap(float_0)
        str_0 = 'wnWi$5RDZ}!<RKk#H\t'
        bool_1 = left_0.is_left()
        list_0 = [str_0, right_0]
        var_3 = right_0.bind(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        object_0 = module_0.object()
        str_0 = 'W](nMPE?4YV9kc'
        left_0 = module_1.Left(str_0)
        var_0 = left_0.to_validation()
        dict_0 = {}
        str_1 = 'w\n!\rcBUg`aw%o'
        right_0 = module_1.Right(str_1)
        var_1 = right_0.map(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        callable_0 = None
        list_0 = None
        var_0 = None
        either_0 = module_1.Either(var_0)
        right_0 = module_1.Right(var_0)
        list_1 = [list_0]
        right_1 = module_1.Right(list_1)
        var_1 = right_1.map(callable_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        list_1 = [bool_0, bool_0, bool_0]
        right_0 = module_1.Right(list_1)
        var_0 = right_0.bind(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'U'
        left_0 = module_1.Left(str_0)
        bool_0 = left_0.is_left()
        bool_1 = True
        right_0 = module_1.Right(bool_1)
        bool_2 = right_0.is_left()
        bool_3 = False
        left_1 = module_1.Left(bool_3)
        bool_4 = left_1.is_left()
        float_0 = 614.6
        var_0 = right_0.bind(float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 1
        str_0 = 'fail'
        var_0 = lambda value: str_0
        str_1 = 'success'
        var_1 = lambda value: str_1
        right_0 = module_1.Right(int_0)
        var_2 = lambda value: str_0
        var_3 = lambda value: str_1
        var_4 = right_0.case(var_2, var_3)
    except BaseException:
        pass