# Automatically generated by Pynguin.
import pymonet.either as module_0
import builtins as module_1

def test_case_0():
    try:
        bool_0 = True
        either_0 = module_0.Either(bool_0)
        float_0 = 573.9
        right_0 = module_0.Right(float_0)
        bool_1 = True
        var_0 = either_0.case(right_0, bool_1)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2511
        bytes_0 = b'q\x08&\xcf\xbcr\x89qp\xc9'
        callable_0 = None
        left_0 = module_0.Left(int_0)
        var_0 = left_0.map(callable_0)
        left_1 = module_0.Left(bytes_0)
        var_1 = left_1.bind(int_0)
        float_0 = -1241.97992
        either_0 = module_0.Either(float_0)
        left_2 = module_0.Left(either_0)
        tuple_0 = ()
        either_1 = module_0.Either(tuple_0)
        var_2 = either_1.ap(left_2)
        bool_0 = True
        str_0 = '\n    One is a Monoid that will combine 2 values of any type using logical disjunction OR on their coerced Boolean values.\n    '
        var_3 = either_0.case(bool_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 2544
        either_0 = module_0.Either(int_0)
        var_0 = either_0.to_box()
        callable_0 = None
        var_1 = either_0.case(callable_0, callable_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = True
        tuple_0 = ()
        left_0 = module_0.Left(tuple_0)
        var_0 = left_0.bind(int_0)
        var_1 = None
        callable_0 = None
        either_0 = module_0.Either(var_1)
        var_2 = either_0.case(callable_0, callable_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'N|%3Xq'
        str_1 = '\x0b.XRYxx9!#qxI x'
        var_0 = None
        right_0 = module_0.Right(var_0)
        right_1 = module_0.Right(var_0)
        float_0 = -618.99
        left_0 = module_0.Left(float_0)
        either_0 = module_0.Either(var_0)
        var_1 = either_0.to_lazy()
        var_2 = left_0.ap(right_1)
        right_2 = module_0.Right(str_1)
        bool_0 = right_2.is_left()
        var_3 = right_2.bind(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = {}
        object_0 = module_1.object(**dict_0)
        left_0 = module_0.Left(object_0)
        var_0 = left_0.to_validation()
        list_0 = []
        dict_1 = {}
        right_0 = module_0.Right(dict_1)
        var_1 = right_0.to_validation()
        var_2 = None
        either_0 = module_0.Either(var_2)
        str_0 = 'ua#|-\\2/Cx'
        var_3 = either_0.to_lazy()
        either_1 = module_0.Either(str_0)
        var_4 = either_1.to_box()
        float_0 = 961.65
        right_1 = module_0.Right(float_0)
        var_5 = right_1.to_maybe()
        object_1 = None
        bool_0 = right_0.is_left()
        either_2 = module_0.Either(list_0)
        bool_1 = either_2.__eq__(object_1)
        var_6 = either_2.to_lazy()
        var_7 = either_2.to_lazy()
        var_8 = right_0.bind(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\n        Returns successful Validation with value and empty errors list.\n\n        :params value: value to store in Validation\n        :type value: A\n        :returns: Successful Validation\n        :rtype: Validation[A, []]\n        '
        bool_0 = True
        right_0 = module_0.Right(bool_0)
        str_1 = '\n        Return monad value.\n\n        :returns: monad value\n        :rtype: A\n        '
        str_2 = ':XG+$L_'
        dict_0 = {str_0: str_0, str_1: str_0, str_0: str_0, str_2: str_0}
        right_1 = module_0.Right(dict_0)
        bool_1 = right_1.is_right()
        callable_0 = None
        var_0 = right_0.map(callable_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\n        Return resolved Task with stored value argument.\n\n        :param value: value to store in Task\n        :type value: A\n        :returns: resolved Task\n        :rtype: Task[Function(_, resolve) -> A]\n        '
        list_0 = [str_0, str_0, str_0, str_0]
        left_0 = module_0.Left(list_0)
        var_0 = left_0.to_maybe()
        float_0 = -329.0
        either_0 = module_0.Either(float_0)
        var_1 = either_0.is_right()
        dict_0 = {}
        right_0 = module_0.Right(dict_0)
        var_2 = right_0.to_maybe()
        left_1 = module_0.Left(dict_0)
        var_3 = right_0.bind(left_1)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 2
        right_0 = module_0.Right(int_0)
        var_0 = lambda value: int_0 * value
        var_1 = lambda value: value / int_0
        var_2 = right_0.case(var_0, var_1)
    except BaseException:
        pass