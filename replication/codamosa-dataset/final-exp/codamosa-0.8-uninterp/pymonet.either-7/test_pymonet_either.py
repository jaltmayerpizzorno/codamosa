# Automatically generated by Pynguin.
import pymonet.either as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = ''
    either_0 = module_0.Either(str_0)

def test_case_2():
    str_0 = 'x-P\x0b/JY'
    list_0 = [str_0, str_0]
    bytes_0 = b'\xfd8X\xac\xe3d\xa9\xdf\x92\xa6\x19\x1e\x0f\x10'
    left_0 = module_0.Left(bytes_0)
    var_0 = left_0.bind(list_0)
    either_0 = module_0.Either(var_0)
    var_1 = either_0.to_box()
    left_1 = module_0.Left(str_0)
    bool_0 = left_1.is_left()
    bytes_1 = b'6\xf4\xef\xb5\x91\x0c\x131V'
    list_1 = [bool_0, left_1, bool_0, either_0]
    right_0 = module_0.Right(list_1)
    list_2 = [bytes_1]
    var_2 = left_1.bind(list_2)
    list_3 = []
    either_1 = module_0.Either(list_3)
    var_3 = either_1.ap(var_2)
    left_2 = module_0.Left(bytes_1)
    var_4 = left_2.to_validation()
    set_0 = set()
    right_1 = module_0.Right(set_0)
    var_5 = right_1.to_validation()

def test_case_3():
    bytes_0 = b'\xaad`\x08\xe0\x0b\r&\x8a\x07\x90\xf7\x00T8\xdf\xfc\xdd'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    either_0 = module_0.Either(dict_0)
    var_0 = either_0.to_box()
    left_0 = module_0.Left(bytes_0)
    bool_0 = left_0.is_right()
    str_0 = '\n        :param fork: function to call during fork\n        :type fork: Function(reject, resolve) -> Any\n        '
    right_0 = module_0.Right(str_0)
    bool_1 = right_0.is_left()
    either_1 = module_0.Either(right_0)
    bool_2 = left_0.is_right()
    var_1 = either_1.to_lazy()
    var_2 = right_0.to_validation()
    var_3 = right_0.to_validation()

def test_case_4():
    float_0 = 2323.99144
    either_0 = module_0.Either(float_0)
    var_0 = either_0.to_try()
    tuple_0 = ()
    str_0 = "B~'^O"
    left_0 = module_0.Left(str_0)
    var_1 = left_0.ap(tuple_0)

def test_case_5():
    dict_0 = {}
    object_0 = module_1.object(**dict_0)
    left_0 = module_0.Left(object_0)
    var_0 = left_0.to_validation()
    list_0 = [var_0]
    right_0 = module_0.Right(object_0)
    var_1 = right_0.to_maybe()
    var_2 = left_0.bind(list_0)
    str_0 = '?('
    either_0 = module_0.Either(str_0)
    var_3 = either_0.to_lazy()

def test_case_6():
    callable_0 = None
    str_0 = '\reOeG:/#P0lP"FPSig'
    str_1 = 'KM!z9kP.Gb6'
    dict_0 = {str_0: str_0, str_1: str_0, str_0: str_0, str_0: str_1}
    left_0 = module_0.Left(dict_0)
    var_0 = left_0.map(callable_0)

def test_case_7():
    dict_0 = {}
    right_0 = module_0.Right(dict_0)
    var_0 = right_0.to_validation()
    bool_0 = right_0.is_left()
    int_0 = 1623
    str_0 = 'o~;^#*zQ?UK7?io'
    left_0 = module_0.Left(str_0)
    var_1 = left_0.bind(int_0)

def test_case_8():
    bool_0 = False
    left_0 = module_0.Left(bool_0)
    bool_1 = left_0.is_left()
    var_0 = None
    left_1 = module_0.Left(var_0)
    bool_2 = left_0.is_left()

def test_case_9():
    str_0 = '0Tqk\r56)J:<F]gP~u'
    bool_0 = False
    int_0 = 2174
    set_0 = {int_0}
    left_0 = module_0.Left(set_0)
    var_0 = left_0.bind(bool_0)
    left_1 = module_0.Left(var_0)
    var_1 = left_1.bind(str_0)
    list_0 = [var_1, int_0, int_0, bool_0]
    left_2 = module_0.Left(list_0)
    var_2 = left_2.to_maybe()
    bytes_0 = b'\xaa'
    list_1 = [bytes_0]
    right_0 = module_0.Right(list_1)
    bool_1 = right_0.is_right()

def test_case_10():
    int_0 = 1
    left_0 = module_0.Left(int_0)
    left_1 = module_0.Left(int_0)
    bool_0 = left_0.__eq__(left_1)
    left_2 = module_0.Left(int_0)
    int_1 = 2
    left_3 = module_0.Left(int_1)
    bool_1 = left_2.__eq__(left_3)
    left_4 = module_0.Left(int_0)
    right_0 = module_0.Right(int_0)
    bool_2 = left_4.__eq__(right_0)
    right_1 = module_0.Right(int_0)
    right_2 = module_0.Right(int_0)
    bool_3 = right_1.__eq__(right_2)
    right_3 = module_0.Right(int_0)
    right_4 = module_0.Right(int_1)
    var_0 = left_1.to_lazy()