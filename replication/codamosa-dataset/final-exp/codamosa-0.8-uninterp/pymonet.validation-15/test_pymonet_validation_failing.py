# Automatically generated by Pynguin.
import pymonet.validation as module_0

def test_case_0():
    try:
        str_0 = '3~jtqD-\tr+j*'
        bool_0 = True
        validation_0 = module_0.Validation(str_0, bool_0)
        var_0 = validation_0.to_try()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        bool_1 = True
        validation_0 = module_0.Validation(bool_0, bool_1)
        validation_1 = module_0.Validation(validation_0, validation_0)
        bool_2 = False
        validation_2 = module_0.Validation(validation_1, bool_2)
        var_0 = validation_2.is_fail()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Zl#rX[6#b%$ '
        float_0 = 1969.0
        validation_0 = module_0.Validation(str_0, float_0)
        str_1 = '\n        Transform Box into Right either.\n\n        :returns: right Either monad with previous value\n        :rtype: Right[A]\n        '
        var_0 = validation_0.map(str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xf4GY\xc8'
        bool_0 = False
        list_0 = [bool_0, bool_0]
        float_0 = -355.3
        bool_1 = False
        bytes_1 = None
        validation_0 = module_0.Validation(bool_1, bytes_1)
        tuple_0 = (bool_0, list_0, float_0, validation_0)
        validation_1 = module_0.Validation(tuple_0, float_0)
        var_0 = validation_1.bind(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'<P\x08\xde_\xe3\xd8\r\xc6'
        str_0 = '\n        Transform Box into Validation.\n\n        :returns: failed Validation monad with previous value as error\n        :rtype: Validation[None, [A]]\n        '
        validation_0 = module_0.Validation(str_0, str_0)
        var_0 = validation_0.ap(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'<P\x08\xde_\xe3\xd8\r\xc6'
        str_0 = '\n        Transform Box into Validation.\n\n        :returns: failed Validation monad with previous value as error\n        :rtype: Validation[None, [A]]\n        '
        list_0 = [bytes_0, str_0, bytes_0, bytes_0]
        validation_0 = module_0.Validation(list_0, bytes_0)
        var_0 = validation_0.to_either()
        validation_1 = module_0.Validation(str_0, str_0)
        var_1 = validation_1.ap(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'IT7`-BQ48`Co'
        int_0 = -3053
        validation_0 = module_0.Validation(str_0, int_0)
        dict_0 = None
        bytes_0 = b'R\xff\x82\xfb\x9c\x8e\x16t\xaa"\x03\x8d\x02*%V'
        var_0 = validation_0.__eq__(bytes_0)
        var_1 = validation_0.map(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = True
        bytes_0 = b'*\x7fQ\x18\xb4'
        list_0 = []
        validation_0 = module_0.Validation(bytes_0, list_0)
        var_0 = validation_0.is_fail()
        var_1 = validation_0.to_either()
        str_0 = None
        var_2 = validation_0.is_success()
        validation_1 = module_0.Validation(int_0, str_0)
        var_3 = validation_1.to_lazy()
        var_4 = validation_0.__str__()
        var_5 = validation_1.to_either()
    except BaseException:
        pass