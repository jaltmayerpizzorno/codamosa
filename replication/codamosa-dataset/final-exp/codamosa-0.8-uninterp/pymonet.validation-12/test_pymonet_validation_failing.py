# Automatically generated by Pynguin.
import pymonet.validation as module_0

def test_case_0():
    try:
        str_0 = "S[ fPiy#yS{'C+4-v\x0c=J"
        bool_0 = False
        list_0 = [str_0, bool_0]
        validation_0 = module_0.Validation(str_0, list_0)
        bool_1 = False
        list_1 = []
        validation_1 = module_0.Validation(bool_1, list_1)
        float_0 = -3351.2
        validation_2 = module_0.Validation(validation_1, float_0)
        var_0 = validation_2.__eq__(validation_0)
        validation_3 = module_0.Validation(str_0, bool_0)
        var_1 = validation_3.__str__()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 3255.59234
        int_0 = -1277
        tuple_0 = (float_0, int_0)
        float_1 = 583.48285
        list_0 = [float_1]
        str_0 = '\n        Create not empty maybe.\n\n        :param mapper: value to store in Maybe\n        :type mapper: Any\n        :returns: Maybe[Any]\n        '
        validation_0 = module_0.Validation(list_0, str_0)
        var_0 = validation_0.to_either()
        str_1 = 'hU^E'
        validation_1 = module_0.Validation(float_0, tuple_0)
        var_1 = validation_1.to_box()
        validation_2 = module_0.Validation(list_0, str_1)
        var_2 = validation_2.to_box()
        var_3 = validation_2.map(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 132
        float_0 = -3010.1191
        validation_0 = module_0.Validation(int_0, float_0)
        var_0 = validation_0.to_box()
        str_0 = '\n        Transform Either to Maybe.\n\n        :returns: Maybe with previous value\n        :rtype: Maybe[A]\n        '
        float_1 = -2344.0
        validation_1 = module_0.Validation(str_0, str_0)
        var_1 = validation_1.bind(float_1)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        str_0 = '\n    Sum is a Monoid that will combine 2 numbers under addition.\n    '
        validation_0 = module_0.Validation(dict_0, str_0)
        bool_0 = True
        validation_1 = module_0.Validation(validation_0, dict_0)
        var_0 = validation_1.ap(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\x9c\xcd\xe9\xd2\x95\xf3\xefo\xe2N\xb2L\x0f\xf9\x87\xf10'
        int_0 = 3036
        validation_0 = module_0.Validation(bytes_0, int_0)
        var_0 = validation_0.to_try()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '_r/@'
        bool_0 = False
        set_0 = {bool_0, str_0, bool_0, bool_0}
        list_0 = [bool_0, bool_0, set_0]
        float_0 = 808.2369
        bytes_0 = None
        validation_0 = module_0.Validation(float_0, bytes_0)
        var_0 = validation_0.__eq__(validation_0)
        str_1 = '\n        Transform Box into Validation.\n\n        :returns: failed Validation monad with previous value as error\n        :rtype: Validation[None, [A]]\n        '
        validation_1 = module_0.Validation(str_1, list_0)
        var_1 = validation_0.to_box()
    except BaseException:
        pass