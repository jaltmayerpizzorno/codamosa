# Automatically generated by Pynguin.
import pymonet.validation as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = False
    str_0 = '\n        :param semigroup: other semigroup to concat\n        :type semigroup: Max[B]\n        :returns: new Max with largest value\n        :rtype: Max[A | B]\n        '
    validation_0 = module_0.Validation(int_0, str_0)

def test_case_2():
    tuple_0 = ()
    bytes_0 = b'rm\xdf\xb2Q\x8c/\xc0^\xd8 \x84\x92l^%'
    validation_0 = module_0.Validation(tuple_0, bytes_0)
    list_0 = [validation_0, bytes_0]
    var_0 = validation_0.__eq__(list_0)

def test_case_3():
    tuple_0 = ()
    bytes_0 = b'rm\xdf\xb2Q\x8c/\xc0^\xd8 \x84\x92l^%'
    validation_0 = module_0.Validation(tuple_0, bytes_0)
    var_0 = validation_0.__str__()

def test_case_4():
    tuple_0 = ()
    bytes_0 = b'\xca\xd5\x05\x96\xb6O\xeeF!\xf3\x8e'
    validation_0 = module_0.Validation(tuple_0, bytes_0)
    var_0 = validation_0.to_either()
    bytes_1 = b'rm\xdf\xb2Q\x8c/\xc0^\xd8 \x84\x92l^%'
    validation_1 = module_0.Validation(tuple_0, bytes_1)
    var_1 = validation_1.__str__()

def test_case_5():
    tuple_0 = ()
    bytes_0 = b'rm\xdf\xb2Q\x8c/\xc0^\xd8 \x84\x92l^%'
    validation_0 = module_0.Validation(tuple_0, bytes_0)
    list_0 = [validation_0, bytes_0]
    var_0 = validation_0.to_box()
    var_1 = validation_0.__eq__(list_0)

def test_case_6():
    float_0 = 40.61
    set_0 = {float_0, float_0, float_0}
    str_0 = '0q"\x0ct2C-,\x0by\nR'
    validation_0 = module_0.Validation(set_0, str_0)
    validation_1 = module_0.Validation(validation_0, set_0)
    var_0 = validation_1.to_lazy()

def test_case_7():
    bool_0 = False
    bytes_0 = None
    dict_0 = {bool_0: bytes_0, bytes_0: bytes_0}
    validation_0 = module_0.Validation(dict_0, bool_0)
    str_0 = '\n        Transform Either into Validation.\n\n        :returns: successfull Validation monad with previous value\n        :rtype: Validation[A, []]\n        '
    float_0 = 1782.632
    validation_1 = module_0.Validation(str_0, float_0)
    var_0 = validation_1.__eq__(validation_0)
    str_1 = 't\x0b\r'
    str_2 = 'D\t\x0cIk6IF'
    bytes_1 = None
    str_3 = 'eW5\x0c8b!)Xe'
    str_4 = '5N'
    list_0 = [bool_0, str_1, str_4, str_2]
    validation_2 = module_0.Validation(str_4, list_0)
    var_1 = validation_2.is_success()
    validation_3 = module_0.Validation(bytes_1, str_3)
    bytes_2 = b'N\\\x92^\xb0wW\xb3\x04\xc36`\r\x02\x06D'
    float_1 = 505.0
    validation_4 = module_0.Validation(bytes_2, float_1)
    float_2 = -412.3
    var_2 = validation_3.__eq__(float_2)

def test_case_8():
    str_0 = 'n*lGWb/FL='
    float_0 = -974.6
    str_1 = 'WzBZID'
    set_0 = set()
    validation_0 = module_0.Validation(str_1, set_0)
    var_0 = validation_0.to_box()
    dict_0 = {float_0: float_0, float_0: float_0}
    bool_0 = None
    int_0 = 1002
    validation_1 = module_0.Validation(dict_0, int_0)
    var_1 = validation_1.__eq__(bool_0)
    float_1 = -251.69
    bytes_0 = b'\xe7\xc6\xef\xfc'
    list_0 = [str_0]
    validation_2 = module_0.Validation(bytes_0, list_0)
    validation_3 = module_0.Validation(validation_2, validation_2)
    validation_4 = module_0.Validation(float_1, validation_3)
    var_2 = validation_4.to_lazy()
    validation_5 = module_0.Validation(str_0, dict_0)
    var_3 = validation_5.to_either()
    bytes_1 = b'\xaa1\x91z\xb86\xab\xbdC\xe4\x94\xe0F}\xa1\xe9\x84'
    str_2 = ',ztv\x0bk(N'
    str_3 = '\n        Transform Lazy into not empty Maybe with constructor_fn result.\n\n        :returns: not empty Maybe monad with constructor_fn result\n        :rtype: Maybe[A]\n        '
    list_1 = []
    dict_1 = {str_2: bytes_1, str_2: bytes_1, bytes_1: bytes_1}
    validation_6 = module_0.Validation(list_1, dict_1)
    var_4 = validation_6.to_maybe()
    var_5 = validation_3.__eq__(bytes_1)
    var_6 = validation_3.__eq__(validation_1)
    var_7 = validation_6.is_success()
    tuple_0 = (str_3,)
    validation_7 = module_0.Validation(str_2, tuple_0)
    var_8 = validation_4.__eq__(validation_4)